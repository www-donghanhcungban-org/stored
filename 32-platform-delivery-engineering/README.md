# 32. Platform & Delivery Engineering: từ môi trường phát triển đến triển khai có thể quay lui

> Nghiên cứu 4/11/2026 phục vụ xưởng phát triển phần mềm. Mục 13 giữ bản đồ stack/DevOps; mục này đào sâu **hợp đồng môi trường, thay đổi hạ tầng, promotion artifact và khôi phục**. Đây là hồ sơ/đánh giá, không chứa implementation triển khai. Đọc LICENSE, spec, implementation/callsite và CI theo phạm vi bên dưới; không cài/build/chạy upstream, không tạo tài nguyên cloud.

## 1. Trần chất lượng và phạm vi

Một pipeline xanh chỉ chứng minh các job được chọn đã thành công. Xưởng cần trả lời: dev và CI có cùng dependency không; ai được apply plan nào; image digest nào chạy ở staging/production; khi lỗi có phục hồi dữ liệu và dịch vụ được không. Các lớp artifact/signing ở [mục 31](../31-software-supply-chain-security/README.md), test ở [mục 30](../30-software-testing-quality/README.md) và SLO/incident ở [mục 33](../33-reliability-observability-operations/README.md) là cổng liên quan, không được thay bằng trạng thái sync của công cụ triển khai.

| Lớp | Artifact làm hợp đồng | Cổng nghiệm thu ở dự án tích hợp |
|---|---|---|
| Môi trường phát triển/CI | Runtime pin, dependency lock, image/Feature ref, cấu hình và lệnh readiness | Tạo môi trường mới rồi build/test một luồng thật; kiểm cả khởi động lại, không chỉ cache nóng |
| Hạ tầng | Source commit, provider lock, plan gắn workspace/state, người duyệt | Plan được review là plan được apply; xử lý drift, concurrency và secret trong state |
| Phát hành ứng dụng | Image/package digest + config/migration version, bằng chứng test/provenance | Promote cùng artifact; kiểm health và hành vi đại diện sau deploy, có điều kiện rollback |
| Môi trường tạm | Owner, TTL, dữ liệu mẫu và đường teardown | Test xong xóa được tài nguyên/secret; môi trường PR không cầm credential production |
| Khôi phục | Revision cũ, khả năng tương thích schema/dữ liệu, backup đã thử | Revert/sync/restore được diễn tập; mục tiêu phục hồi theo sản phẩm và chi phí chấp nhận được |

<a id="factory-devcontainers-2026-11-04"></a>

## 2. Development Container Specification: hợp đồng setup có lifecycle và quyền host

| Thuộc tính | Kết quả đọc |
|---|---|
| Repo / nguồn | `devcontainers/spec`, đặc tả do Microsoft và cộng đồng phát triển; README trỏ `containers.dev`, CLI tham chiếu và `devcontainers/ci` |
| Phiên bản / mức kiểm | HEAD `c95ffeed1d059abfe9ffbe79762dc2fa4e7c2421`; **docs-read**: đọc đặc tả, schema và license. Repo spec không là binary runtime; không gán code-read hay kết quả CI của CLI cho nó |
| License | Nội dung spec: **CC-BY-4.0** trong `LICENSE`/README; mã có `LICENSE-CODE` MIT. Không gán MIT cho toàn bộ nội dung đặc tả |
| Cơ chế | `devcontainer.json`/JSONC mô tả image/build, Features, mounts, user, environment và lifecycle; host thực thi phải hỗ trợ các trường tương ứng |
| Ranh giới | `initializeCommand` chạy trên **host**; `onCreateCommand`/`postCreateCommand` chạy trong container. Container không tự thành sandbox bảo vệ host khi mount socket/thư mục nhạy cảm hoặc bật privileged |
| Tích hợp | Dùng cho local/CI nếu cần cùng hợp đồng setup; startup/readiness phải là lệnh được kiểm trong tool thực tế, không chỉ file JSON schema pass |

Đặc tả phân biệt `remoteUser` (user cho tool/subprocess) với `containerUser` (user cho các operation trong container); mặc định có thể kế thừa root từ image. `waitFor` mặc định `updateContentCommand`, nên một tool attach thành công chưa chứng minh `postCreateCommand` đã hoàn tất. Lifecycle thất bại sẽ bỏ các script tiếp theo; cần lưu log và kiểm kết quả tác vụ. [Tham chiếu lifecycle/user/mount]( https://github.com/devcontainers/spec/blob/c95ffeed1d059abfe9ffbe79762dc2fa4e7c2421/docs/specs/devcontainerjson-reference.md ) · [schema]( https://github.com/devcontainers/spec/blob/c95ffeed1d059abfe9ffbe79762dc2fa4e7c2421/schemas/devContainer.base.schema.json ) · [spec license]( https://github.com/devcontainers/spec/blob/c95ffeed1d059abfe9ffbe79762dc2fa4e7c2421/LICENSE ) · [code license]( https://github.com/devcontainers/spec/blob/c95ffeed1d059abfe9ffbe79762dc2fa4e7c2421/LICENSE-CODE ).

**Chọn thay thế:** runtime pin + package manager lock khi repo nhỏ; Nix/devenv (mục 13) khi cần mô hình package/environment khác; Dev Containers khi nhóm đã dùng container/IDE hỗ trợ. Mỗi cách vẫn phải kiểm dependency nền, architecture, proxy/CA và secret injection theo môi trường thực; không bảo đảm mọi host tương đương bit-for-bit.

<a id="factory-opentofu-2026-11-04"></a>

## 3. OpenTofu: review thay đổi và apply đúng artifact

Hồ sơ gốc đã có ở [mục 13](../13-dev-stack-devops/README.md); đây là phạm vi đọc sâu mới. `opentofu/opentofu`, MPL-2.0, HEAD `c570669d0fed5787f18d2f017f56b2658e2e6cce`. Đã đọc LICENSE, CLI `PlanCommand`, backend local, docs plan/state và workflow Quick Checks. Không chạy plan/apply hay kiểm provider thật.

**Exit code có ba trạng thái.** Với `-detailed-exitcode`, docs và `internal/command/plan.go` khớp: 0 = thành công không thay đổi, 1 = lỗi, 2 = thành công có thay đổi. Wrapper `set -e` coi exit 2 là lỗi nếu không xử lý, còn `|| true` có thể nuốt cả lỗi thật. CI nên phân loại từng mã rồi chạy policy/diff review trên plan; “có thay đổi” chưa phải “được phép apply”. [CLI implementation]( https://github.com/opentofu/opentofu/blob/c570669d0fed5787f18d2f017f56b2658e2e6cce/internal/command/plan.go ) · [contract mã thoát]( https://github.com/opentofu/opentofu/blob/c570669d0fed5787f18d2f017f56b2658e2e6cce/website/docs/cli/commands/plan.mdx ).

**Gắn plan với state.** Backend local có kiểm lineage/serial của saved plan với metadata state; lệch lineage hoặc state thay đổi sẽ báo không khớp/stale khi có metadata tương ứng. Đây là một lớp concurrency/correctness, không thay phân quyền review/apply của tổ chức và không chứng minh mọi provider action quay lui được. [Kiểm saved plan]( https://github.com/opentofu/opentofu/blob/c570669d0fed5787f18d2f017f56b2658e2e6cce/internal/backend/local/backend_local.go ).

**Secret và lưu trữ.** Docs ghi state có thể chứa password/private key, và plan có thể giữ dữ liệu nhạy cảm dù terminal đã che; cần bảo vệ artifact/state, hạn chế đọc, retention và cấu hình encryption nếu dùng. Không đưa plan JSON vào comment PR public theo mặc định. [Sensitive state]( https://github.com/opentofu/opentofu/blob/c570669d0fed5787f18d2f017f56b2658e2e6cce/website/docs/language/state/sensitive-data.mdx ) · [plan file]( https://github.com/opentofu/opentofu/blob/c570669d0fed5787f18d2f017f56b2658e2e6cce/website/docs/cli/commands/plan.mdx ) · [CI Quick Checks]( https://github.com/opentofu/opentofu/blob/c570669d0fed5787f18d2f017f56b2658e2e6cce/.github/workflows/checks.yml ) · [license]( https://github.com/opentofu/opentofu/blob/c570669d0fed5787f18d2f017f56b2658e2e6cce/LICENSE ).

**Chọn thay thế:** OpenTofu cho HCL/provider ecosystem với điều kiện kiểm provider/backend; Terraform cần đọc lại license phiên bản định dùng, không suy từ OpenTofu; Pulumi (mục 13) khi nhóm muốn ngôn ngữ lập trình và quản dependency tương ứng; cấu hình cloud nhỏ vẫn có thể dùng công cụ native nếu giữ diff/review/audit. Không chọn chỉ dựa trên cú pháp quen.

<a id="factory-argocd-2026-11-04"></a>

## 4. Argo CD: desired state không đồng nghĩa phục hồi sản phẩm

`argoproj/argo-cd`, Apache-2.0, HEAD `211c2b4fdc82f2ebd0b94c3fbf48779c06d83bad`; hồ sơ gốc mục 13. Đọc `Server.Rollback`, docs automated sync, LICENSE và CI unit/race/integration. Không dựng cluster, không chạy sync/e2e.

`Server.Rollback` kiểm quyền và từ chối khi application đang có automated sync bật: lỗi `rollback cannot be initiated when auto-sync is enabled`. Tài liệu automated sync cũng ghi điều kiện này. Trong hệ GitOps, cần chọn đường phục hồi phù hợp: **revert desired state trong Git và sync lại**, hoặc thao tác rollback có kiểm soát sau khi xử lý chính sách auto-sync. Không ghi runbook “bấm rollback” mà bỏ qua trạng thái controller. [Đường rollback]( https://github.com/argoproj/argo-cd/blob/211c2b4fdc82f2ebd0b94c3fbf48779c06d83bad/server/application/application.go ) · [contract automated sync]( https://github.com/argoproj/argo-cd/blob/211c2b4fdc82f2ebd0b94c3fbf48779c06d83bad/docs/user-guide/auto_sync.md ).

Các tùy chọn prune/self-heal/allow-empty và ApplicationSet làm hành vi khác nhau; phải review manifest thực của ứng dụng. Synced cho biết live state phù hợp desired state theo cách so sánh của Argo CD; Healthy là health assessment được cấu hình, không thay phép thử login/đặt hàng hay bằng chứng restore dữ liệu. Có thể quay image về bản cũ mà schema migration không tương thích; điều kiện này thuộc ứng dụng và backend ở mục 34. [CI]( https://github.com/argoproj/argo-cd/blob/211c2b4fdc82f2ebd0b94c3fbf48779c06d83bad/.github/workflows/ci-build.yaml ) · [license]( https://github.com/argoproj/argo-cd/blob/211c2b4fdc82f2ebd0b94c3fbf48779c06d83bad/LICENSE ).

**Chọn thay thế:** Argo CD khi cần GitOps Kubernetes và mô hình Application; Flux khi nhóm muốn controller/toolkit cùng GitOps (đối chiếu hồ sơ nếu có, chưa đọc mã Flux trong đợt này); CI deploy trực tiếp có audit/rollback cho hệ nhỏ; dịch vụ platform managed khi chấp nhận ràng buộc nhà cung cấp. Không thêm Kubernetes chỉ để dùng một công cụ GitOps.

## 5. Pipeline tham chiếu cho một xưởng nhiều sản phẩm

1. **Golden path tối thiểu:** template repo liên kết owner, runtime/lock, test, docs, release, health/readiness và runbook. Nơi triển khai giữ implementation; kho này giữ tiêu chí so sánh và nguồn.
2. **Dev/CI có cùng đầu vào:** tạo lại môi trường từ nguồn pin; chạy build/test thật và báo số test. Phân biệt retained dependency/cache với process/service phải restart; thay architecture hoặc image phải kiểm lại.
3. **Plan hạ tầng có quyền hẹp:** tạo plan cho đúng môi trường, xử lý 0/1/2 đúng, review policy/cost/resource diff; bảo vệ plan/state và chỉ apply artifact đã duyệt, không sinh plan mới sau approval rồi mặc định tương đương.
4. **Build một lần, promote theo digest:** release bundle gồm source, test/security evidence, artifact digest và config/migration version. Staging/prod nhận cùng artifact; secret/environment là binding riêng có audit, không nhúng vào image.
5. **Deploy và quan sát hành vi:** controller sync/rollout xong phải qua health + functional smoke/SLO tại mục 30/33. Đặt giới hạn blast radius/canary theo rủi ro; ngưỡng do sản phẩm quyết định, không dùng một tỷ lệ chung cho mọi hệ.
6. **Revert/restore và teardown:** diễn tập quay lui app tương thích schema, phục hồi dữ liệu và xóa preview environment theo owner/TTL. Giữ audit artifact trước/sau; secret/volume/tài nguyên dùng chung cần policy riêng để teardown không xóa nhầm.

## 6. Ma trận nghiệm thu và giới hạn

| Cổng | Bằng chứng tối thiểu | Không được coi là pass |
|---|---|---|
| Onboarding | Môi trường mới chạy được build/test/luồng đại diện với dependency pin | Chỉ có container PID, shell attach, port mở hay cache từ máy cũ |
| Plan/apply | Exit đúng nghĩa, plan hash/workspace/state/reviewer, apply log | Chỉ có comment diff hoặc bỏ qua mọi mã lỗi để làm xanh job |
| Deploy | Artifact/config đúng revision, health và functional smoke, provenance theo policy | Chỉ image tag trùng tên, status Synced hoặc một HTTP 200 không kiểm body |
| Recovery | Diễn tập có outcome, RTO/RPO thực đo theo mục tiêu sản phẩm, migration compatibility | Chỉ giữ một image cũ hoặc backup chưa từng restore |
| Chi phí/quyền | Owner, TTL, quota/budget và audit quyền môi trường | Preview chạy vô hạn hoặc dùng production credentials để tiện test |

Ba hồ sơ trên có vai trò khác nhau: spec môi trường, công cụ IaC và controller deployment. Ghép cả ba chỉ khi sản phẩm cần; monolith nhỏ có thể đạt cùng hợp đồng bằng ít công cụ hơn. Chưa có dữ liệu vận hành của xưởng để khẳng định giảm thời gian, chi phí hay lỗi bao nhiêu; các cổng là đề xuất tích hợp cần đo ở repo đích.

<a id="anhkysuai-2026-11-23"></a>

## Đánh giá từ kho Anh Kỹ Sư AI — 23/11/2026

Phần này có **35 hồ sơ hoặc phạm vi đối chiếu** từ [nguồn tuyển chọn](https://anhkysuai.com/kho/). [Bảng đủ 1.295 repo](../data/collections/anhkysuai-kho.json) ghi trạng thái đối chiếu từng link; [danh sách URL](../data/collections/anhkysuai-kho-links.txt) phục vụ tra cứu. Nguồn tuyển chọn giúp phát hiện repo; đánh giá bên dưới dựa trên clone và permalink upstream cùng metadata GitHub ngày 2026-11-23.

Mức `docs-read`/`code-read` chỉ áp dụng phạm vi ghi tại mỗi hồ sơ. Chưa cài, build, chạy test hay benchmark mã upstream. Giấy phép có thể tách theo code, model, nội dung, asset hoặc bản enterprise; con số/tuyên bố của tác giả chưa được tái lập nếu không có ghi chú khác.

<a id="anhkysuai-2026-11-23-fastlane"></a>

### fastlane

**Repo:** [fastlane/fastlane](https://github.com/fastlane/fastlane) · **License:** MIT · **★ 42,500 (GitHub API, 2026-11-23)**

**Mục đích:** Tự động hóa chụp ảnh màn hình, ký và phát hành ứng dụng iOS/Android.

**Giá trị và cơ chế:** README trình bày một bộ công cụ chạy trên máy hoặc CI của dự án; cấu hình CI có ma trận macOS/Xcode/Ruby, phù hợp gom các bước phát hành lặp lại.

**Giới hạn:** Tuyên bố credentials không rời máy không thay việc kiểm từng action và dịch vụ đích. Chưa đọc action phát hành hoặc chạy ký ứng dụng; tương thích phụ thuộc SDK và tài khoản nền tảng.

**Cách tham khảo/tích hợp:** Tách credential theo môi trường, ghim action và giữ bước phê duyệt trước khi phát hành bản sản xuất.

**Thay thế:** codemagic, bitrise, github-actions.

**Bằng chứng:** `docs-read`, ngày 2026-11-23, commit [`1dad6c718459`](https://github.com/fastlane/fastlane/commit/1dad6c7184593f18a4d83a7e8b98325cb992d967). README và các tài liệu/manifest/CI hiện diện, đọc chọn lọc; chưa kiểm implementation. Chưa cài/chạy upstream.

**Nguồn:** [README.md](https://github.com/fastlane/fastlane/blob/1dad6c7184593f18a4d83a7e8b98325cb992d967/README.md) · [LICENSE](https://github.com/fastlane/fastlane/blob/1dad6c7184593f18a4d83a7e8b98325cb992d967/LICENSE) · [metadata GitHub](https://api.github.com/repos/fastlane/fastlane).

<a id="anhkysuai-coollabsio-coolify"></a>

### Coolify

**Đã chuyển (2026-11-23):** hồ sơ này nay nằm ở [mục 36](../36-self-hosting-homelab/README.md#anhkysuai-coollabsio-coolify); catalog con xem [catalog/](../catalog/README.md).

<a id="anhkysuai-pi-hole-pi-hole"></a>

### Pi-hole Core

**Đã chuyển (2026-11-23):** hồ sơ này nay nằm ở [mục 36](../36-self-hosting-homelab/README.md#anhkysuai-pi-hole-pi-hole); catalog con xem [catalog/](../catalog/README.md).

<a id="anhkysuai-acmesh-official-acme.sh"></a>

### acme.sh

**Repo:** [acmesh-official/acme.sh](https://github.com/acmesh-official/acme.sh) · **License:** GPL-3.0 · **Kiểm:** 2026-11-23, `docs-read`, [`5567d7fe7298`](https://github.com/acmesh-official/acme.sh/tree/5567d7fe7298fd37aca53194885ba444c6678669) (commit 2026-11-19). **Sao:** 47,973 tại 2026-11-23 theo [GitHub API](https://api.github.com/repos/acmesh-official/acme.sh).

| Mục | Đánh giá |
|---|---|
| Mục đích | Client ACME bằng shell để cấp, gia hạn và cài chứng chỉ TLS. |
| Giá trị và cơ chế theo tài liệu | README mô tả ECDSA, SAN/wildcard, IPv6 và hook; CI có ShellCheck cùng kiểm định dạng shell. |
| Giới hạn | Quyền DNS API hoặc hook gia hạn có thể ảnh hưởng máy chủ; đọc tài liệu không chứng minh việc renew hoạt động với mọi nhà cung cấp. Chưa cấp hay cài chứng chỉ. |
| Điều kiện tích hợp | Thử CA staging và hook deploy trước; bảo vệ khóa API, kiểm lịch gia hạn và phương án theo dõi hết hạn. |
| Lựa chọn đối chiếu | [Certbot](../32-platform-delivery-engineering/README.md#anhkysuai-certbot-certbot); Lego; [Caddy](../08-awesome-lists-learning/README.md#6c55-container--devops). |

**Phạm vi bằng chứng:** đã clone, đọc trích đoạn tài liệu, giấy phép và các file cấu hình được dẫn dưới đây; chưa chạy mã, build, benchmark hoặc test upstream. `docs-read` không phải kiểm chứng implementation.

**Nguồn tại cùng SHA:** [README.md](https://github.com/acmesh-official/acme.sh/blob/5567d7fe7298fd37aca53194885ba444c6678669/README.md) · [LICENSE.md](https://github.com/acmesh-official/acme.sh/blob/5567d7fe7298fd37aca53194885ba444c6678669/LICENSE.md) · [.github/workflows/shellcheck.yml](https://github.com/acmesh-official/acme.sh/blob/5567d7fe7298fd37aca53194885ba444c6678669/.github/workflows/shellcheck.yml).

<a id="anhkysuai-unitech-pm2"></a>

### PM2

**Repo:** [Unitech/pm2](https://github.com/Unitech/pm2) · **License:** AGPL-3.0 · **Kiểm:** 2026-11-23, `docs-read`, [`7a7fb4e22e9a`](https://github.com/Unitech/pm2/tree/7a7fb4e22e9a26ec79c870ce8daafd2f78b648d1) (commit 2026-11-03). **Sao:** 43,342 tại 2026-11-23 theo [GitHub API](https://api.github.com/repos/Unitech/pm2).

| Mục | Đánh giá |
|---|---|
| Mục đích | Trình quản lý tiến trình cho Node.js/Bun và chương trình chạy lâu dài. |
| Giá trị và cơ chế theo tài liệu | README mô tả restart, reload, cluster/load balancing; manifest nêu runtime và CI chạy bộ kiểm Node/Bun. |
| Giới hạn | LICENSE gốc trỏ đến GNU-AGPL-3.0.txt. Reload không tự bảo đảm không gián đoạn cho mọi ứng dụng; giám sát tiến trình không thay thiết kế lưu bền hay dự phòng máy chủ. |
| Điều kiện tích hợp | Ghim runtime, kiểm graceful shutdown và tài nguyên, cấu hình startup/log rotation; kiểm điều khoản AGPL và tách dịch vụ thương mại nếu sử dụng. |
| Lựa chọn đối chiếu | systemd; Supervisor; [Docker Compose](../32-platform-delivery-engineering/README.md#anhkysuai-docker-compose). |

**Phạm vi bằng chứng:** đã clone, đọc trích đoạn tài liệu, giấy phép và các file cấu hình được dẫn dưới đây; chưa chạy mã, build, benchmark hoặc test upstream. `docs-read` không phải kiểm chứng implementation.

**Nguồn tại cùng SHA:** [README.md](https://github.com/Unitech/pm2/blob/7a7fb4e22e9a26ec79c870ce8daafd2f78b648d1/README.md) · [LICENSE](https://github.com/Unitech/pm2/blob/7a7fb4e22e9a26ec79c870ce8daafd2f78b648d1/LICENSE) · [package.json](https://github.com/Unitech/pm2/blob/7a7fb4e22e9a26ec79c870ce8daafd2f78b648d1/package.json) · [.github/workflows/node.js.yml](https://github.com/Unitech/pm2/blob/7a7fb4e22e9a26ec79c870ce8daafd2f78b648d1/.github/workflows/node.js.yml) · [GNU-AGPL-3.0.txt](https://github.com/Unitech/pm2/blob/7a7fb4e22e9a26ec79c870ce8daafd2f78b648d1/GNU-AGPL-3.0.txt).

<a id="anhkysuai-docker-compose"></a>

### Docker Compose

**Repo:** [docker/compose](https://github.com/docker/compose) · **License:** Apache-2.0 · **Kiểm:** 2026-11-23, `docs-read`, [`469ab94d7232`](https://github.com/docker/compose/tree/469ab94d72326565c6dfdf304a72882115011800) (commit 2026-11-18). **Sao:** 39,135 tại 2026-11-23 theo [GitHub API](https://api.github.com/repos/docker/compose).

| Mục | Đánh giá |
|---|---|
| Mục đích | CLI định nghĩa và chạy ứng dụng nhiều container bằng Compose file. |
| Giá trị và cơ chế theo tài liệu | README cùng go.mod xác định triển khai Go hiện tại; workflow CI gọi các target Make và build artifact, hữu ích làm chuẩn môi trường phát triển tái tạo được. |
| Giới hạn | README lưu ý Swarm không hỗ trợ đầy đủ Compose Specification hiện đại. Một lệnh khởi động không tự giải quyết migration, backup hoặc tính sẵn sàng nhiều máy. |
| Điều kiện tích hợp | Ghim image và phiên bản Compose, khai báo healthcheck/volume/secrets phù hợp; thử khởi động lại và phục hồi dữ liệu của stack trước khi dùng lâu dài. |
| Lựa chọn đối chiếu | Podman Compose; Kubernetes; Nomad. |

**Phạm vi bằng chứng:** đã clone, đọc trích đoạn tài liệu, giấy phép và các file cấu hình được dẫn dưới đây; chưa chạy mã, build, benchmark hoặc test upstream. `docs-read` không phải kiểm chứng implementation.

**Nguồn tại cùng SHA:** [README.md](https://github.com/docker/compose/blob/469ab94d72326565c6dfdf304a72882115011800/README.md) · [LICENSE](https://github.com/docker/compose/blob/469ab94d72326565c6dfdf304a72882115011800/LICENSE) · [go.mod](https://github.com/docker/compose/blob/469ab94d72326565c6dfdf304a72882115011800/go.mod) · [.github/workflows/ci.yml](https://github.com/docker/compose/blob/469ab94d72326565c6dfdf304a72882115011800/.github/workflows/ci.yml).

<a id="anhkysuai-portainer-portainer"></a>

### Portainer Community Edition

**Đã chuyển (2026-11-23):** hồ sơ này nay nằm ở [mục 36](../36-self-hosting-homelab/README.md#anhkysuai-portainer-portainer); catalog con xem [catalog/](../catalog/README.md).

<a id="anhkysuai-adguardteam-adguardhome"></a>

### AdGuard Home

**Đã chuyển (2026-11-23):** hồ sơ này nay nằm ở [mục 36](../36-self-hosting-homelab/README.md#anhkysuai-adguardteam-adguardhome); catalog con xem [catalog/](../catalog/README.md).

<a id="anhkysuai-dokploy-dokploy"></a>

### Dokploy

**Đã chuyển (2026-11-23):** hồ sơ này nay nằm ở [mục 36](../36-self-hosting-homelab/README.md#anhkysuai-dokploy-dokploy); catalog con xem [catalog/](../catalog/README.md).

<a id="anhkysuai-istio-istio"></a>

### Istio

**Repo:** [istio/istio](https://github.com/istio/istio) · **License:** Apache-2.0 · **Kiểm:** 2026-11-23, `docs-read`, [`a49b0c5c91d2`](https://github.com/istio/istio/tree/a49b0c5c91d2bbf077fa224f760a7ce0ec5b65ec) (commit 2026-11-22). **Sao:** 38,534 tại 2026-11-23 theo [GitHub API](https://api.github.com/repos/istio/istio).

| Mục | Đánh giá |
|---|---|
| Mục đích | Service mesh bổ sung điều khiển lưu lượng, xác thực giữa dịch vụ và quan sát. |
| Giá trị và cơ chế theo tài liệu | README trình bày cách phủ lớp mesh lên ứng dụng phân tán và trỏ các repo thành phần; Go manifest giúp xác định phạm vi nền tảng. |
| Giới hạn | Tuyên bố ít thay đổi mã không có nghĩa không phát sinh chi phí vận hành. Chưa kiểm policy, certificate rotation, độ trễ hoặc tính tương thích cluster. |
| Điều kiện tích hợp | Thử một namespace và đường request thực, cấu hình quan sát rồi mới áp chính sách chặt; kiểm rollback và overhead trước khi đưa mesh vào toàn hệ thống. |
| Lựa chọn đối chiếu | Linkerd; [Consul](../34-backend-data-identity-integration/README.md#anhkysuai-hashicorp-consul); [Cilium](../08-awesome-lists-learning/README.md#6c55-container--devops). |

**Phạm vi bằng chứng:** đã clone, đọc trích đoạn tài liệu, giấy phép và các file cấu hình được dẫn dưới đây; chưa chạy mã, build, benchmark hoặc test upstream. `docs-read` không phải kiểm chứng implementation.

**Nguồn tại cùng SHA:** [README.md](https://github.com/istio/istio/blob/a49b0c5c91d2bbf077fa224f760a7ce0ec5b65ec/README.md) · [LICENSE](https://github.com/istio/istio/blob/a49b0c5c91d2bbf077fa224f760a7ce0ec5b65ec/LICENSE) · [go.mod](https://github.com/istio/istio/blob/a49b0c5c91d2bbf077fa224f760a7ce0ec5b65ec/go.mod).

<a id="anhkysuai-icewhaletech-casaos"></a>

### CasaOS

**Repo:** [IceWhaleTech/CasaOS](https://github.com/IceWhaleTech/CasaOS) · **License:** Apache-2.0 · **Kiểm:** 2026-11-23, `docs-read`, [`e099dd6b4982`](https://github.com/IceWhaleTech/CasaOS/tree/e099dd6b4982a264663df2536a55bfea2ae5448a) (commit 2026-11-09). **Sao:** 37,692 tại 2026-11-23 theo [GitHub API](https://api.github.com/repos/IceWhaleTech/CasaOS).

| Mục | Đánh giá |
|---|---|
| Mục đích | Hệ thống personal cloud giúp quản lý ứng dụng Docker, ổ đĩa và tệp bằng giao diện web. |
| Giá trị và cơ chế theo tài liệu | README mô tả nhiều loại phần cứng và kho ứng dụng; manifest có OpenAPI sinh SDK TypeScript/Axios cùng backend Go. |
| Giới hạn | Tầm nhìn personal cloud/AI không đồng nghĩa mọi khả năng đã triển khai. Ứng dụng bên ngoài có giấy phép và vòng đời riêng; chưa kiểm cài đặt trên phần cứng hay restore ổ đĩa. |
| Điều kiện tích hợp | Thử trên máy dành riêng, đọc installer và cấu hình volume; phân biệt backup dữ liệu với việc cài lại app, kiểm quyền truy cập từ mạng ngoài. |
| Lựa chọn đối chiếu | Umbrel; OpenMediaVault; Portainer. |

**Phạm vi bằng chứng:** đã clone, đọc trích đoạn tài liệu, giấy phép và các file cấu hình được dẫn dưới đây; chưa chạy mã, build, benchmark hoặc test upstream. `docs-read` không phải kiểm chứng implementation.

**Nguồn tại cùng SHA:** [README.md](https://github.com/IceWhaleTech/CasaOS/blob/e099dd6b4982a264663df2536a55bfea2ae5448a/README.md) · [LICENSE](https://github.com/IceWhaleTech/CasaOS/blob/e099dd6b4982a264663df2536a55bfea2ae5448a/LICENSE) · [package.json](https://github.com/IceWhaleTech/CasaOS/blob/e099dd6b4982a264663df2536a55bfea2ae5448a/package.json) · [go.mod](https://github.com/IceWhaleTech/CasaOS/blob/e099dd6b4982a264663df2536a55bfea2ae5448a/go.mod) · [.github/workflows/push_test_server.yml](https://github.com/IceWhaleTech/CasaOS/blob/e099dd6b4982a264663df2536a55bfea2ae5448a/.github/workflows/push_test_server.yml).

<a id="anhkysuai-podman-container-tools-podman"></a>

### Podman

**Repo:** [podman-container-tools/podman](https://github.com/podman-container-tools/podman) · **License:** Apache-2.0 · **Kiểm:** 2026-11-23, `docs-read`, [`813b52acd5e9`](https://github.com/podman-container-tools/podman/tree/813b52acd5e9287686185bbe5dd19fdf6e627760) (commit 2026-11-23). **Sao:** 33,363 tại 2026-11-23 theo [GitHub API](https://api.github.com/repos/podman-container-tools/podman).

| Mục | Đánh giá |
|---|---|
| Mục đích | Công cụ quản lý OCI container, image, volume và pod, gồm thư viện libpod. |
| Giá trị và cơ chế theo tài liệu | README phân biệt Linux với máy ảo quản lý trên macOS/Windows; nêu lịch release và phạm vi hỗ trợ phiên bản, hữu ích khi chuẩn hóa môi trường dev. |
| Giới hạn | Khả năng chạy container không tự đồng nhất hoàn toàn với Docker theo mọi workflow. Chưa thử mount, mạng hoặc tương thích daemon/API; cần theo phiên bản còn hỗ trợ. |
| Điều kiện tích hợp | Thử image và Compose hiện có trên môi trường đích, kiểm volume, networking và quyền; chọn release được hỗ trợ và kiểm sao lưu dữ liệu ngoài container. |
| Lựa chọn đối chiếu | Docker Engine; [containerd](../32-platform-delivery-engineering/README.md#anhkysuai-containerd-containerd); nerdctl. |

**Phạm vi bằng chứng:** đã clone, đọc trích đoạn tài liệu, giấy phép và các file cấu hình được dẫn dưới đây; chưa chạy mã, build, benchmark hoặc test upstream. `docs-read` không phải kiểm chứng implementation.

**Nguồn tại cùng SHA:** [README.md](https://github.com/podman-container-tools/podman/blob/813b52acd5e9287686185bbe5dd19fdf6e627760/README.md) · [LICENSE](https://github.com/podman-container-tools/podman/blob/813b52acd5e9287686185bbe5dd19fdf6e627760/LICENSE) · [pyproject.toml](https://github.com/podman-container-tools/podman/blob/813b52acd5e9287686185bbe5dd19fdf6e627760/pyproject.toml) · [go.mod](https://github.com/podman-container-tools/podman/blob/813b52acd5e9287686185bbe5dd19fdf6e627760/go.mod) · [.github/workflows/ci.yml](https://github.com/podman-container-tools/podman/blob/813b52acd5e9287686185bbe5dd19fdf6e627760/.github/workflows/ci.yml).

<a id="anhkysuai-certbot-certbot"></a>

### Certbot

**Repo:** [certbot/certbot](https://github.com/certbot/certbot) · **License:** Apache-2.0; mã nginxparser theo MIT · **Kiểm:** 2026-11-23, `docs-read`, [`9d5c9d44e57d`](https://github.com/certbot/certbot/tree/9d5c9d44e57df4c070287e99338e49029cc45cba) (commit 2026-11-20). **Sao:** 33,346 tại 2026-11-23 theo [GitHub API](https://api.github.com/repos/certbot/certbot).

| Mục | Đánh giá |
|---|---|
| Mục đích | Client ACME của EFF để lấy, gia hạn và tùy chọn cài chứng chỉ HTTPS. |
| Giá trị và cơ chế theo tài liệu | README thực nằm trong certbot/README.rst, mô tả Apache/nginx/webroot/standalone và khóa tạo local; CI điều phối bộ kiểm PR. |
| Giới hạn | Thường cần quyền quản trị trên máy chủ; hosting không cho truy cập máy có thể cần cách khác. Chưa cấp chứng chỉ hay kiểm cấu hình web server sau thay đổi. |
| Điều kiện tích hợp | Dùng hướng dẫn đúng hệ điều hành/web server, thử CA staging và renew; kiểm hook reload, bảo vệ private key và giám sát hết hạn. |
| Lựa chọn đối chiếu | [acme.sh](../32-platform-delivery-engineering/README.md#anhkysuai-acmesh-official-acme.sh); Lego; [Caddy](../08-awesome-lists-learning/README.md#6c55-container--devops). |

**Phạm vi bằng chứng:** đã clone, đọc trích đoạn tài liệu, giấy phép và các file cấu hình được dẫn dưới đây; chưa chạy mã, build, benchmark hoặc test upstream. `docs-read` không phải kiểm chứng implementation.

**Nguồn tại cùng SHA:** [README.rst](https://github.com/certbot/certbot/blob/9d5c9d44e57df4c070287e99338e49029cc45cba/README.rst) · [LICENSE.txt](https://github.com/certbot/certbot/blob/9d5c9d44e57df4c070287e99338e49029cc45cba/LICENSE.txt) · [.github/workflows/pr-test-suite.yml](https://github.com/certbot/certbot/blob/9d5c9d44e57df4c070287e99338e49029cc45cba/.github/workflows/pr-test-suite.yml) · [certbot/README.rst](https://github.com/certbot/certbot/blob/9d5c9d44e57df4c070287e99338e49029cc45cba/certbot/README.rst).

<a id="anhkysuai-kubernetes-minikube"></a>

### minikube

**Repo:** [kubernetes/minikube](https://github.com/kubernetes/minikube) · **License:** Apache-2.0 · **Kiểm:** 2026-11-23, `docs-read`, [`132853137ab6`](https://github.com/kubernetes/minikube/tree/132853137ab61868aa803838398a629faaf4148d) (commit 2026-11-22). **Sao:** 32,261 tại 2026-11-23 theo [GitHub API](https://api.github.com/repos/kubernetes/minikube).

| Mục | Đánh giá |
|---|---|
| Mục đích | Công cụ chạy cluster Kubernetes cục bộ trên macOS, Linux và Windows. |
| Giá trị và cơ chế theo tài liệu | README mô tả profiles, tunnel, NodePort, persistent volume, addon và runtime; Go/CI giúp xây môi trường thử gần với API Kubernetes. |
| Giới hạn | Cluster local không tái hiện đầy đủ topology, storage hay lỗi của production. Tài nguyên và driver máy chủ ảnh hưởng kết quả; chưa khởi tạo cluster thực. |
| Điều kiện tích hợp | Ghim phiên bản Kubernetes và driver, dùng profile riêng cho dự án; kiểm manifest, ingress và volume rồi xác nhận lại trên môi trường triển khai đích. |
| Lựa chọn đối chiếu | kind; k3d; MicroK8s. |

**Phạm vi bằng chứng:** đã clone, đọc trích đoạn tài liệu, giấy phép và các file cấu hình được dẫn dưới đây; chưa chạy mã, build, benchmark hoặc test upstream. `docs-read` không phải kiểm chứng implementation.

**Nguồn tại cùng SHA:** [README.md](https://github.com/kubernetes/minikube/blob/132853137ab61868aa803838398a629faaf4148d/README.md) · [LICENSE](https://github.com/kubernetes/minikube/blob/132853137ab61868aa803838398a629faaf4148d/LICENSE) · [go.mod](https://github.com/kubernetes/minikube/blob/132853137ab61868aa803838398a629faaf4148d/go.mod) · [.github/workflows/test.yml](https://github.com/kubernetes/minikube/blob/132853137ab61868aa803838398a629faaf4148d/.github/workflows/test.yml).

<a id="anhkysuai-dokku-dokku"></a>

### Dokku

**Đã chuyển (2026-11-23):** hồ sơ này nay nằm ở [mục 36](../36-self-hosting-homelab/README.md#anhkysuai-dokku-dokku); catalog con xem [catalog/](../catalog/README.md).

<a id="anhkysuai-abiosoft-colima"></a>

### Colima

**Repo:** [abiosoft/colima](https://github.com/abiosoft/colima) · **License:** MIT · **Kiểm:** 2026-11-23, `docs-read`, [`49dfe87aecc1`](https://github.com/abiosoft/colima/tree/49dfe87aecc1645905d0fb8a0e43ce29e12138f6) (commit 2026-10-02). **Sao:** 31,797 tại 2026-11-23 theo [GitHub API](https://api.github.com/repos/abiosoft/colima).

| Mục | Đánh giá |
|---|---|
| Mục đích | CLI tạo môi trường container trên macOS/Linux với Docker, containerd hoặc Incus. |
| Giá trị và cơ chế theo tài liệu | README mô tả port forwarding, volume, nhiều instance và lựa chọn runtime; Go manifest/CI lint giúp xác định công cụ điều phối môi trường local. |
| Giới hạn | Docker runtime cần Docker client riêng. GPU và behavior volume/network phụ thuộc nền tảng; chưa khởi tạo máy ảo hay kiểm tương thích workflow hiện có. |
| Điều kiện tích hợp | Chọn runtime/profile, giới hạn CPU/RAM/disk và thử mount/port; kiểm kiến trúc image trên Apple Silicon, giữ dữ liệu quan trọng ngoài môi trường có thể xóa. |
| Lựa chọn đối chiếu | Lima; Rancher Desktop; Podman machine. |

**Phạm vi bằng chứng:** đã clone, đọc trích đoạn tài liệu, giấy phép và các file cấu hình được dẫn dưới đây; chưa chạy mã, build, benchmark hoặc test upstream. `docs-read` không phải kiểm chứng implementation.

**Nguồn tại cùng SHA:** [README.md](https://github.com/abiosoft/colima/blob/49dfe87aecc1645905d0fb8a0e43ce29e12138f6/README.md) · [LICENSE](https://github.com/abiosoft/colima/blob/49dfe87aecc1645905d0fb8a0e43ce29e12138f6/LICENSE) · [go.mod](https://github.com/abiosoft/colima/blob/49dfe87aecc1645905d0fb8a0e43ce29e12138f6/go.mod) · [.github/workflows/golang-ci.yml](https://github.com/abiosoft/colima/blob/49dfe87aecc1645905d0fb8a0e43ce29e12138f6/.github/workflows/golang-ci.yml).

<a id="anhkysuai-helm-helm"></a>

### Helm

**Repo:** [helm/helm](https://github.com/helm/helm) · **License:** Apache-2.0 · **Kiểm:** 2026-11-23, `docs-read`, [`e827d8030d3b`](https://github.com/helm/helm/tree/e827d8030d3be68095f00506e295b5b60b7d4353) (commit 2026-11-22). **Sao:** 30,466 tại 2026-11-23 theo [GitHub API](https://api.github.com/repos/helm/helm).

| Mục | Đánh giá |
|---|---|
| Mục đích | Trình quản lý gói Kubernetes dùng chart và template tài nguyên. |
| Giá trị và cơ chế theo tài liệu | README giải thích Chart.yaml, render template, gọi Kubernetes API và quản lý release; nêu v4 là dòng ổn định, v3 có lịch kết thúc hỗ trợ. |
| Giới hạn | Chart từ bên ngoài không tự đáng tin nhờ dùng Helm. Rollback manifest không bảo đảm rollback database hoặc volume; chưa triển khai chart hay kiểm hook. |
| Điều kiện tích hợp | Ghim chart/dependency, xem manifest render và quyền trước khi cài; giữ values/secrets có kiểm soát, thử nâng cấp và phục hồi state trên cluster dev. |
| Lựa chọn đối chiếu | Kustomize; Carvel; manifests Kubernetes thuần. |

**Phạm vi bằng chứng:** đã clone, đọc trích đoạn tài liệu, giấy phép và các file cấu hình được dẫn dưới đây; chưa chạy mã, build, benchmark hoặc test upstream. `docs-read` không phải kiểm chứng implementation.

**Nguồn tại cùng SHA:** [README.md](https://github.com/helm/helm/blob/e827d8030d3be68095f00506e295b5b60b7d4353/README.md) · [LICENSE](https://github.com/helm/helm/blob/e827d8030d3be68095f00506e295b5b60b7d4353/LICENSE) · [go.mod](https://github.com/helm/helm/blob/e827d8030d3be68095f00506e295b5b60b7d4353/go.mod) · [.github/workflows/build-test.yml](https://github.com/helm/helm/blob/e827d8030d3be68095f00506e295b5b60b7d4353/.github/workflows/build-test.yml).

<a id="anhkysuai-community-scripts-proxmoxve"></a>

### Proxmox VE Helper Scripts

**Đã chuyển (2026-11-23):** hồ sơ này nay nằm ở [mục 36](../36-self-hosting-homelab/README.md#anhkysuai-community-scripts-proxmoxve); catalog con xem [catalog/](../catalog/README.md).

<a id="anhkysuai-hashicorp-vagrant"></a>

### Vagrant CLI

**Repo:** [hashicorp/vagrant](https://github.com/hashicorp/vagrant) · **License:** MIT · **Kiểm:** 2026-11-23, `docs-read`, [`747762783149`](https://github.com/hashicorp/vagrant/tree/747762783149cb6fe3bd6480970b5b1e660be5e5) (commit 2026-11-12). **Sao:** 27,238 tại 2026-11-23 theo [GitHub API](https://api.github.com/repos/hashicorp/vagrant).

| Mục | Đánh giá |
|---|---|
| Mục đích | Công cụ mô tả và phân phối môi trường phát triển với máy ảo hoặc provider khác. |
| Giá trị và cơ chế theo tài liệu | README phân biệt rõ HCP Vagrant đang deprecated với CLI không bị ảnh hưởng; LICENSE tại SHA là MIT, CI chạy unit test Ruby. |
| Giới hạn | Box/provider/plugin có nguồn và điều khoản riêng; tính portable cần thử trên kiến trúc máy thật. Không áp nhãn license cũ hoặc tình trạng HCP lên CLI. |
| Điều kiện tích hợp | Ghim box và provider, đọc provisioning script trước khi chạy; thử networking, synced folder và rebuild môi trường, tránh lưu bản duy nhất của dữ liệu trong VM tạm. |
| Lựa chọn đối chiếu | Dev Containers; Lima; Multipass. |

**Phạm vi bằng chứng:** đã clone, đọc trích đoạn tài liệu, giấy phép và các file cấu hình được dẫn dưới đây; chưa chạy mã, build, benchmark hoặc test upstream. `docs-read` không phải kiểm chứng implementation.

**Nguồn tại cùng SHA:** [README.md](https://github.com/hashicorp/vagrant/blob/747762783149cb6fe3bd6480970b5b1e660be5e5/README.md) · [LICENSE](https://github.com/hashicorp/vagrant/blob/747762783149cb6fe3bd6480970b5b1e660be5e5/LICENSE) · [.github/workflows/testing.yml](https://github.com/hashicorp/vagrant/blob/747762783149cb6fe3bd6480970b5b1e660be5e5/.github/workflows/testing.yml).

<a id="anhkysuai-jenkinsci-jenkins"></a>

### Jenkins

**Repo:** [jenkinsci/jenkins](https://github.com/jenkinsci/jenkins) · **License:** MIT · **Kiểm:** 2026-11-23, `docs-read`, [`21431124601c`](https://github.com/jenkinsci/jenkins/tree/21431124601c2f752fba9f093659b098e44b2693) (commit 2026-11-23). **Sao:** 26,804 tại 2026-11-23 theo [GitHub API](https://api.github.com/repos/jenkinsci/jenkins).

| Mục | Đánh giá |
|---|---|
| Mục đích | Máy chủ tự động hóa build, kiểm thử và triển khai với hệ plugin. |
| Giá trị và cơ chế theo tài liệu | README phân biệt release weekly/LTS và các gói WAR/container/native; Maven/frontend manifest cho biết phạm vi core Java và giao diện. |
| Giới hạn | Quyền chạy pipeline và plugin ảnh hưởng trực tiếp credentials/hạ tầng. Workflow đã đọc tạo changelog, chưa xác nhận test core hoặc an toàn plugin ngoài. |
| Điều kiện tích hợp | Chọn LTS và bộ plugin tối thiểu, tách agent build khỏi controller; quản lý secrets, quyền job và backup cấu hình, thử nâng cấp trong staging. |
| Lựa chọn đối chiếu | GitLab CI; Buildkite; Woodpecker CI. |

**Phạm vi bằng chứng:** đã clone, đọc trích đoạn tài liệu, giấy phép và các file cấu hình được dẫn dưới đây; chưa chạy mã, build, benchmark hoặc test upstream. `docs-read` không phải kiểm chứng implementation.

**Nguồn tại cùng SHA:** [README.md](https://github.com/jenkinsci/jenkins/blob/21431124601c2f752fba9f093659b098e44b2693/README.md) · [LICENSE.txt](https://github.com/jenkinsci/jenkins/blob/21431124601c2f752fba9f093659b098e44b2693/LICENSE.txt) · [package.json](https://github.com/jenkinsci/jenkins/blob/21431124601c2f752fba9f093659b098e44b2693/package.json) · [pom.xml](https://github.com/jenkinsci/jenkins/blob/21431124601c2f752fba9f093659b098e44b2693/pom.xml) · [.github/workflows/changelog.yml](https://github.com/jenkinsci/jenkins/blob/21431124601c2f752fba9f093659b098e44b2693/.github/workflows/changelog.yml).

<a id="anhkysuai-openfaas-faas"></a>

### OpenFaaS

**Repo:** [openfaas/faas](https://github.com/openfaas/faas) · **License:** OpenFaaS CE EULA; đóng góp bên thứ ba theo MIT · **Kiểm:** 2026-11-23, `docs-read`, [`eb29c060bda6`](https://github.com/openfaas/faas/tree/eb29c060bda6c2de3df83ca62f7ff6dedca9db23) (commit 2026-10-23). **Sao:** 26,268 tại 2026-11-23 theo [GitHub API](https://api.github.com/repos/openfaas/faas).

| Mục | Đánh giá |
|---|---|
| Mục đích | Nền tảng chạy function và microservice đóng gói OCI trên Kubernetes. |
| Giá trị và cơ chế theo tài liệu | README mô tả endpoint, autoscaling, metrics và CLI/template riêng; Go module cùng workflow build cho thấy repo nền của bộ phân phối. |
| Giới hạn | CE hiện dành cho khám phá cá nhân/hobby, PoC thương mại giới hạn 60 ngày; commercial/production cần edition phù hợp. Không gắn MIT cho toàn repo hoặc suy zero-scale luôn có ở CE. |
| Điều kiện tích hợp | Đối chiếu EULA/edition, thử một function sandbox với timeout và tài nguyên; kiểm cold start, queue, secret và chi phí vận hành trước khi dùng workload thật. |
| Lựa chọn đối chiếu | Knative; Fission; AWS Lambda. |

**Phạm vi bằng chứng:** đã clone, đọc trích đoạn tài liệu, giấy phép và các file cấu hình được dẫn dưới đây; chưa chạy mã, build, benchmark hoặc test upstream. `docs-read` không phải kiểm chứng implementation.

**Nguồn tại cùng SHA:** [README.md](https://github.com/openfaas/faas/blob/eb29c060bda6c2de3df83ca62f7ff6dedca9db23/README.md) · [LICENSE](https://github.com/openfaas/faas/blob/eb29c060bda6c2de3df83ca62f7ff6dedca9db23/LICENSE) · [go.mod](https://github.com/openfaas/faas/blob/eb29c060bda6c2de3df83ca62f7ff6dedca9db23/go.mod) · [.github/workflows/build.yml](https://github.com/openfaas/faas/blob/eb29c060bda6c2de3df83ca62f7ff6dedca9db23/.github/workflows/build.yml) · [EULA.md](https://github.com/openfaas/faas/blob/eb29c060bda6c2de3df83ca62f7ff6dedca9db23/EULA.md).

<a id="anhkysuai-rancher-rancher"></a>

### Rancher

**Repo:** [rancher/rancher](https://github.com/rancher/rancher) · **License:** Apache-2.0 · **Kiểm:** 2026-11-23, `docs-read`, [`b4da0df611cf`](https://github.com/rancher/rancher/tree/b4da0df611cf7ef666d27942f89eaa6d17f6eeac) (commit 2026-11-23). **Sao:** 26,079 tại 2026-11-23 theo [GitHub API](https://api.github.com/repos/rancher/rancher).

| Mục | Đánh giá |
|---|---|
| Mục đích | Nền tảng quản lý môi trường Kubernetes và container cho tổ chức. |
| Giá trị và cơ chế theo tài liệu | README dẫn stable release, support matrix và phân biệt meta-repo đóng gói; Go module và CI unit test hỗ trợ đọc lớp điều phối. |
| Giới hạn | Ví dụ docker privileged là quick start, không phải thiết kế production hoàn chỉnh. Chưa kiểm quản lý nhiều cluster, RBAC, upgrade hoặc agent; hỗ trợ phụ thuộc version matrix. |
| Điều kiện tích hợp | Triển khai thử bằng hướng dẫn đúng release, giới hạn quyền quản trị và bootstrap; kiểm backup, phục hồi control plane và đường nâng cấp cluster trước khi dùng rộng. |
| Lựa chọn đối chiếu | OpenShift; Headlamp; Portainer Business. |

**Phạm vi bằng chứng:** đã clone, đọc trích đoạn tài liệu, giấy phép và các file cấu hình được dẫn dưới đây; chưa chạy mã, build, benchmark hoặc test upstream. `docs-read` không phải kiểm chứng implementation.

**Nguồn tại cùng SHA:** [README.md](https://github.com/rancher/rancher/blob/b4da0df611cf7ef666d27942f89eaa6d17f6eeac/README.md) · [LICENSE](https://github.com/rancher/rancher/blob/b4da0df611cf7ef666d27942f89eaa6d17f6eeac/LICENSE) · [go.mod](https://github.com/rancher/rancher/blob/b4da0df611cf7ef666d27942f89eaa6d17f6eeac/go.mod) · [.github/workflows/unit-test.yml](https://github.com/rancher/rancher/blob/b4da0df611cf7ef666d27942f89eaa6d17f6eeac/.github/workflows/unit-test.yml).

<a id="anhkysuai-pulumi-pulumi"></a>

### Pulumi

**Repo:** [pulumi/pulumi](https://github.com/pulumi/pulumi) · **License:** Apache-2.0 · **Kiểm:** 2026-11-23, `docs-read`, [`5efdf4497592`](https://github.com/pulumi/pulumi/tree/5efdf4497592ab7f1649ff164f720d2d72a8ba00) (commit 2026-11-21). **Sao:** 25,939 tại 2026-11-23 theo [GitHub API](https://api.github.com/repos/pulumi/pulumi).

| Mục | Đánh giá |
|---|---|
| Mục đích | Infrastructure as Code dùng ngôn ngữ lập trình thông thường và Automation API. |
| Giá trị và cơ chế theo tài liệu | README minh họa tạo tài nguyên bằng TypeScript và provider cloud/Kubernetes; workflow CI có build targets và caching cho bộ công cụ nền. |
| Giới hạn | Apache-2.0 của engine không bao phủ mọi provider hay dịch vụ Pulumi Cloud. Code IaC có thể tạo chi phí/thay đổi thật; chưa chạy preview/apply hoặc kiểm state backend. |
| Điều kiện tích hợp | Chọn backend state và provider đã ghim, xem preview với quyền tối thiểu; kiểm secrets, drift, import và recovery state trước khi tự động hóa production. |
| Lựa chọn đối chiếu | [OpenTofu](../32-platform-delivery-engineering/README.md#factory-opentofu-2026-11-04); Terraform; AWS CDK. |

**Phạm vi bằng chứng:** đã clone, đọc trích đoạn tài liệu, giấy phép và các file cấu hình được dẫn dưới đây; chưa chạy mã, build, benchmark hoặc test upstream. `docs-read` không phải kiểm chứng implementation.

**Nguồn tại cùng SHA:** [README.md](https://github.com/pulumi/pulumi/blob/5efdf4497592ab7f1649ff164f720d2d72a8ba00/README.md) · [LICENSE](https://github.com/pulumi/pulumi/blob/5efdf4497592ab7f1649ff164f720d2d72a8ba00/LICENSE) · [.github/workflows/ci.yml](https://github.com/pulumi/pulumi/blob/5efdf4497592ab7f1649ff164f720d2d72a8ba00/.github/workflows/ci.yml).

<a id="anhkysuai-eip-work-kuboard-press"></a>

### Kuboard v4 Documentation

**Repo:** [eip-work/kuboard-press](https://github.com/eip-work/kuboard-press) · **License:** UNLICENSED trong package.json; chưa thấy giấy phép mã nguồn gốc · **Kiểm:** 2026-11-23, `docs-read`, [`e0cf2f199d96`](https://github.com/eip-work/kuboard-press/tree/e0cf2f199d964d8b67d026282e5b5c680bea28ac) (commit 2026-11-23). **Sao:** 25,281 tại 2026-11-23 theo [GitHub API](https://api.github.com/repos/eip-work/kuboard-press).

| Mục | Đánh giá |
|---|---|
| Mục đích | Mã nguồn website tài liệu song ngữ VitePress của Kuboard v4. |
| Giá trị và cơ chế theo tài liệu | README xác nhận đây là docs site, mô tả điều hướng cài đặt, cluster, workload và MCP; package scripts chỉ build/preview tài liệu. |
| Giới hạn | Không phải mã triển khai Kuboard server. File license-install là hướng dẫn kích hoạt sản phẩm, không cấp quyền tái sử dụng repo; package ghi UNLICENSED, thông tin miễn phí không đồng nghĩa nguồn mở. |
| Điều kiện tích hợp | Dùng làm tài liệu tham khảo và đối chiếu tính năng với sản phẩm thực; cần quyền phù hợp trước khi tái phân phối mã/nội dung, chưa kiểm server hay MCP approval. |
| Lựa chọn đối chiếu | Tài liệu Rancher; Headlamp; [K9s](../33-reliability-observability-operations/README.md#anhkysuai-derailed-k9s). |

**Phạm vi bằng chứng:** đã clone, đọc trích đoạn tài liệu, giấy phép và các file cấu hình được dẫn dưới đây; chưa chạy mã, build, benchmark hoặc test upstream. `docs-read` không phải kiểm chứng implementation.

**Nguồn tại cùng SHA:** [README.md](https://github.com/eip-work/kuboard-press/blob/e0cf2f199d964d8b67d026282e5b5c680bea28ac/README.md) · [docs/en/support/license-install.md](https://github.com/eip-work/kuboard-press/blob/e0cf2f199d964d8b67d026282e5b5c680bea28ac/docs/en/support/license-install.md) · [package.json](https://github.com/eip-work/kuboard-press/blob/e0cf2f199d964d8b67d026282e5b5c680bea28ac/package.json).

<a id="anhkysuai-louislam-dockge"></a>

### Dockge

**Đã chuyển (2026-11-23):** hồ sơ này nay nằm ở [mục 36](../36-self-hosting-homelab/README.md#anhkysuai-louislam-dockge); catalog con xem [catalog/](../catalog/README.md).

<a id="anhkysuai-slimtoolkit-slim"></a>

### SlimToolkit

**Repo:** [slimtoolkit/slim](https://github.com/slimtoolkit/slim) · **License:** Apache-2.0 · **Kiểm:** 2026-11-23, `docs-read`, [`976805241c00`](https://github.com/slimtoolkit/slim/tree/976805241c0000c0114b095e384657e0e98ccaaa) (commit 2026-09-19). **Sao:** 23,547 tại 2026-11-23 theo [GitHub API](https://api.github.com/repos/slimtoolkit/slim).

| Mục | Đánh giá |
|---|---|
| Mục đích | Bộ công cụ xem, tối ưu và debug container, trước đây tên DockerSlim. |
| Giá trị và cơ chế theo tài liệu | README liệt kê xray, lint, build, debug, run và registry; phân biệt toolkit mã mở với dịch vụ xử lý vulnerability của Root.io. |
| Giới hạn | Thu nhỏ image không tự bảo đảm an toàn, có thể bỏ tệp chỉ dùng ở nhánh ít chạy. Các mức giảm 30x là tuyên bố upstream, chưa đo với image ứng dụng. |
| Điều kiện tích hợp | Dùng image thử, thực thi đủ hành trình để phát hiện dependency rồi kiểm lại artifact; giữ image gốc, SBOM và đường rollback khi tối ưu pipeline. |
| Lựa chọn đối chiếu | [Distroless](../32-platform-delivery-engineering/README.md#anhkysuai-googlecontainertools-distroless); multi-stage Docker build; Chainguard Images. |

**Phạm vi bằng chứng:** đã clone, đọc trích đoạn tài liệu, giấy phép và các file cấu hình được dẫn dưới đây; chưa chạy mã, build, benchmark hoặc test upstream. `docs-read` không phải kiểm chứng implementation.

**Nguồn tại cùng SHA:** [README.md](https://github.com/slimtoolkit/slim/blob/976805241c0000c0114b095e384657e0e98ccaaa/README.md) · [LICENSE](https://github.com/slimtoolkit/slim/blob/976805241c0000c0114b095e384657e0e98ccaaa/LICENSE) · [go.mod](https://github.com/slimtoolkit/slim/blob/976805241c0000c0114b095e384657e0e98ccaaa/go.mod).

<a id="anhkysuai-googlecontainertools-distroless"></a>

### Distroless

**Repo:** [GoogleContainerTools/distroless](https://github.com/GoogleContainerTools/distroless) · **License:** Apache-2.0 cho repo; package trong image theo giấy phép tương ứng · **Kiểm:** 2026-11-23, `docs-read`, [`130048d94000`](https://github.com/GoogleContainerTools/distroless/tree/130048d94000cec18d16cc44cc561e1e81052304) (commit 2026-11-22). **Sao:** 23,297 tại 2026-11-23 theo [GitHub API](https://api.github.com/repos/GoogleContainerTools/distroless).

| Mục | Đánh giá |
|---|---|
| Mục đích | Bộ image runtime container chỉ giữ ứng dụng và dependency cần thiết. |
| Giá trị và cơ chế theo tài liệu | README nói rõ không có shell/package manager; CI Bazel kiểm lockfile, build và unit test, hữu ích cho chuẩn hóa image cuối của pipeline. |
| Giới hạn | Ít package không bảo đảm không có lỗ hổng; thiếu shell làm cách debug khác đi. Tag deprecated không còn cập nhật, phải đối chiếu support policy đúng runtime. |
| Điều kiện tích hợp | Dùng multi-stage build và ghim digest, kiểm CA/timezone/native library cần thiết; kiểm startup/healthcheck và chuẩn bị phương án debug bên ngoài container. |
| Lựa chọn đối chiếu | Alpine; Wolfi; [SlimToolkit](../32-platform-delivery-engineering/README.md#anhkysuai-slimtoolkit-slim). |

**Phạm vi bằng chứng:** đã clone, đọc trích đoạn tài liệu, giấy phép và các file cấu hình được dẫn dưới đây; chưa chạy mã, build, benchmark hoặc test upstream. `docs-read` không phải kiểm chứng implementation.

**Nguồn tại cùng SHA:** [README.md](https://github.com/GoogleContainerTools/distroless/blob/130048d94000cec18d16cc44cc561e1e81052304/README.md) · [LICENSE](https://github.com/GoogleContainerTools/distroless/blob/130048d94000cec18d16cc44cc561e1e81052304/LICENSE) · [.github/workflows/ci.yaml](https://github.com/GoogleContainerTools/distroless/blob/130048d94000cec18d16cc44cc561e1e81052304/.github/workflows/ci.yaml).

<a id="anhkysuai-netbox-community-netbox"></a>

### NetBox

**Repo:** [netbox-community/netbox](https://github.com/netbox-community/netbox) · **License:** Apache-2.0 · **Kiểm:** 2026-11-23, `docs-read`, [`7d897955c5a3`](https://github.com/netbox-community/netbox/tree/7d897955c5a3185bae6e33a8fa47f5fe2e2375fe) (commit 2026-11-22). **Sao:** 21,926 tại 2026-11-23 theo [GitHub API](https://api.github.com/repos/netbox-community/netbox).

| Mục | Đánh giá |
|---|---|
| Mục đích | Nguồn dữ liệu mô tả trạng thái mong muốn của hạ tầng mạng. |
| Giá trị và cơ chế theo tài liệu | README phân biệt rõ mô hình/documentation với công cụ thao tác node; API cung cấp rack, thiết bị, cáp, IP/VLAN để automation khác sử dụng. |
| Giới hạn | Core không tự discovery hay sửa cấu hình mạng; sản phẩm NetBox Labs là phạm vi khác. Chưa kiểm model dữ liệu, quyền plugin hoặc sync với thiết bị thật. |
| Điều kiện tích hợp | Chuẩn hóa ownership và nguồn nhập dữ liệu, thử API/schema với một site; kiểm quyền thay đổi, audit, backup và quy trình đối soát trạng thái thực. |
| Lựa chọn đối chiếu | Nautobot; phpIPAM; Netdisco. |

**Phạm vi bằng chứng:** đã clone, đọc trích đoạn tài liệu, giấy phép và các file cấu hình được dẫn dưới đây; chưa chạy mã, build, benchmark hoặc test upstream. `docs-read` không phải kiểm chứng implementation.

**Nguồn tại cùng SHA:** [README.md](https://github.com/netbox-community/netbox/blob/7d897955c5a3185bae6e33a8fa47f5fe2e2375fe/README.md) · [LICENSE.txt](https://github.com/netbox-community/netbox/blob/7d897955c5a3185bae6e33a8fa47f5fe2e2375fe/LICENSE.txt) · [pyproject.toml](https://github.com/netbox-community/netbox/blob/7d897955c5a3185bae6e33a8fa47f5fe2e2375fe/pyproject.toml) · [.github/workflows/ci.yml](https://github.com/netbox-community/netbox/blob/7d897955c5a3185bae6e33a8fa47f5fe2e2375fe/.github/workflows/ci.yml).

<a id="anhkysuai-containerd-containerd"></a>

### containerd

**Repo:** [containerd/containerd](https://github.com/containerd/containerd) · **License:** Apache-2.0 · **Kiểm:** 2026-11-23, `docs-read`, [`ce1877a1521b`](https://github.com/containerd/containerd/tree/ce1877a1521be793afe42f8c024d9bc199eb063a) (commit 2026-11-22). **Sao:** 21,527 tại 2026-11-23 theo [GitHub API](https://api.github.com/repos/containerd/containerd).

| Mục | Đánh giá |
|---|---|
| Mục đích | Runtime daemon quản lý image và vòng đời container trên Linux/Windows. |
| Giá trị và cơ chế theo tài liệu | README định vị lớp được nhúng trong hệ lớn, bao gồm transfer/storage/execution/supervision; Go/CI kiểm source và lint giúp xác định ranh giới runtime. |
| Giới hạn | Không phải nền tảng orchestration hoàn chỉnh cho người dùng cuối. Chưa kiểm sandbox, snapshotter, CRI hay chuỗi runtime thấp hơn; daemon thường có quyền quan trọng trên host. |
| Điều kiện tích hợp | Dùng qua nền tảng phù hợp hoặc API đã ghim, chọn snapshotter/runtime theo hệ điều hành; kiểm nâng cấp, image provenance và phục hồi container. |
| Lựa chọn đối chiếu | CRI-O; Docker Engine; [Podman](../32-platform-delivery-engineering/README.md#anhkysuai-podman-container-tools-podman). |

**Phạm vi bằng chứng:** đã clone, đọc trích đoạn tài liệu, giấy phép và các file cấu hình được dẫn dưới đây; chưa chạy mã, build, benchmark hoặc test upstream. `docs-read` không phải kiểm chứng implementation.

**Nguồn tại cùng SHA:** [README.md](https://github.com/containerd/containerd/blob/ce1877a1521be793afe42f8c024d9bc199eb063a/README.md) · [LICENSE](https://github.com/containerd/containerd/blob/ce1877a1521be793afe42f8c024d9bc199eb063a/LICENSE) · [go.mod](https://github.com/containerd/containerd/blob/ce1877a1521be793afe42f8c024d9bc199eb063a/go.mod) · [.github/workflows/ci.yml](https://github.com/containerd/containerd/blob/ce1877a1521be793afe42f8c024d9bc199eb063a/.github/workflows/ci.yml).

<a id="anhkysuai-ahmetb-kubectx"></a>

### kubectx và kubens

**Repo:** [ahmetb/kubectx](https://github.com/ahmetb/kubectx) · **License:** Apache-2.0 · **Kiểm:** 2026-11-23, `docs-read`, [`12ad6fb22e8c`](https://github.com/ahmetb/kubectx/tree/12ad6fb22e8c546ee2b54e7de38aa51c906832f7) (commit 2026-07-26). **Sao:** 20,130 tại 2026-11-23 theo [GitHub API](https://api.github.com/repos/ahmetb/kubectx).

| Mục | Đánh giá |
|---|---|
| Mục đích | CLI chuyển context/namespace Kubernetes nhanh, có tích hợp tìm kiếm tương tác. |
| Giá trị và cơ chế theo tài liệu | README mô tả quay lại context trước, shell một context và read-only shell; go.mod cùng CI unit/build giúp đọc công cụ tiện ích nhỏ. |
| Giới hạn | Read-only shell là tính năng tuyên bố, chưa kiểm implementation và không thay RBAC phía cluster. Chuyển context sai vẫn có thể tác động môi trường khác; chưa thao tác kubeconfig thật. |
| Điều kiện tích hợp | Dùng tên context rõ ràng và quyền Kubernetes ít nhất, thử trên kubeconfig dev; kiểm shell integration và hiển thị context trước khi chạy lệnh thay đổi tài nguyên. |
| Lựa chọn đối chiếu | kubectl config; [K9s](../33-reliability-observability-operations/README.md#anhkysuai-derailed-k9s); kubie. |

**Phạm vi bằng chứng:** đã clone, đọc trích đoạn tài liệu, giấy phép và các file cấu hình được dẫn dưới đây; chưa chạy mã, build, benchmark hoặc test upstream. `docs-read` không phải kiểm chứng implementation.

**Nguồn tại cùng SHA:** [README.md](https://github.com/ahmetb/kubectx/blob/12ad6fb22e8c546ee2b54e7de38aa51c906832f7/README.md) · [LICENSE](https://github.com/ahmetb/kubectx/blob/12ad6fb22e8c546ee2b54e7de38aa51c906832f7/LICENSE) · [go.mod](https://github.com/ahmetb/kubectx/blob/12ad6fb22e8c546ee2b54e7de38aa51c906832f7/go.mod) · [.github/workflows/ci.yml](https://github.com/ahmetb/kubectx/blob/12ad6fb22e8c546ee2b54e7de38aa51c906832f7/.github/workflows/ci.yml).

<a id="anhkysuai-traefik-traefik"></a>

### Traefik

- **Repo:** [traefik/traefik](https://github.com/traefik/traefik).
- **Mục đích:** Reverse proxy và ingress tự cập nhật định tuyến từ hệ điều phối dịch vụ.
- **Điểm đáng dùng:** README mô tả provider Docker, Kubernetes, ECS và file, cập nhật cấu hình không khởi động lại, HTTPS và metrics; manifest Go cùng CI build nhiều nền tảng hỗ trợ đánh giá khả năng phân phối.
- **License:** MIT.
- **Giới hạn:** Quyền đọc Docker socket hoặc API điều phối là quyền nhạy cảm; dashboard và API phải đặt sau kiểm soát truy cập. Chưa chạy thử TLS, failover hoặc tải.
- **Tích hợp:** Triển khai binary/container với provider cần dùng, giới hạn quyền và quản lý chứng chỉ, route bằng cấu hình có phiên bản.
- **Đối chiếu:** [Caddy](../08-awesome-lists-learning/README.md#6c55-container--devops) cho cấu hình HTTPS gọn; NGINX cho proxy phổ biến; Envoy cho dataplane và chính sách nâng cao.
- **Mức kiểm chứng:** `docs-read` — Đọc các phần mô tả và giới hạn trong README, thông báo license, metadata manifest và cấu hình CI khi có; chưa đọc toàn bộ mã triển khai, chưa cài hoặc chạy kiểm thử upstream.
- **Snapshot:** kiểm ngày 2026-11-23; commit `6f79f8c03bf3ab14442c433f194caadd26aed05c` (2026-11-20T14:45:48+01:00); 65,663 sao theo GitHub API ngày 2026-11-23. Sao không đại diện chất lượng.
- **Bằng chứng:** [README.md](https://github.com/traefik/traefik/blob/6f79f8c03bf3ab14442c433f194caadd26aed05c/README.md) · [LICENSE.md](https://github.com/traefik/traefik/blob/6f79f8c03bf3ab14442c433f194caadd26aed05c/LICENSE.md) · [go.mod](https://github.com/traefik/traefik/blob/6f79f8c03bf3ab14442c433f194caadd26aed05c/go.mod) · [.github/workflows/build.yaml](https://github.com/traefik/traefik/blob/6f79f8c03bf3ab14442c433f194caadd26aed05c/.github/workflows/build.yaml) · [GitHub API](https://api.github.com/repos/traefik/traefik).

<a id="anhkysuai-wagoodman-dive"></a>

### dive

- **Repo:** [wagoodman/dive](https://github.com/wagoodman/dive).
- **Mục đích:** Xem layer Docker/OCI image và tìm dung lượng bị lãng phí.
- **Điểm đáng dùng:** README mô tả so sánh file từng layer và chế độ CI không giao diện trả pass/fail theo ngưỡng; tạo được kiểm soát image có thể chạy cùng pipeline.
- **License:** MIT.
- **Giới hạn:** Tác giả gọi sản phẩm beta và chỉ số hiệu quả là ước tính; dung lượng nhỏ không chứng minh image an toàn. Chưa kiểm ngưỡng hay chạy image.
- **Tích hợp:** Ghim image theo digest khi phân tích, xác định ngưỡng wasted space riêng và dùng CI=true cho đầu ra tự động.
- **Đối chiếu:** docker history cho lớp cơ bản; container-diff cho so sánh image; [Trivy](../12-ai-security-guardrails/README.md) cho lỗ hổng, bổ sung thay vì thay thế dive.
- **Mức kiểm chứng:** `docs-read` — Đọc các phần mô tả và giới hạn trong README, thông báo license, metadata manifest và cấu hình CI khi có; chưa đọc toàn bộ mã triển khai, chưa cài hoặc chạy kiểm thử upstream.
- **Snapshot:** kiểm ngày 2026-11-23; commit `75dea9077a4f0c0328cf0084d9b1e32f2f22df87` (2026-11-17T00:03:11-05:00); 54,755 sao theo GitHub API ngày 2026-11-23. Sao không đại diện chất lượng.
- **Bằng chứng:** [README.md](https://github.com/wagoodman/dive/blob/75dea9077a4f0c0328cf0084d9b1e32f2f22df87/README.md) · [LICENSE](https://github.com/wagoodman/dive/blob/75dea9077a4f0c0328cf0084d9b1e32f2f22df87/LICENSE) · [go.mod](https://github.com/wagoodman/dive/blob/75dea9077a4f0c0328cf0084d9b1e32f2f22df87/go.mod) · [.github/workflows/release.yaml](https://github.com/wagoodman/dive/blob/75dea9077a4f0c0328cf0084d9b1e32f2f22df87/.github/workflows/release.yaml) · [GitHub API](https://api.github.com/repos/wagoodman/dive).

<a id="anhkysuai-harness-harness"></a>

### Harness Open Source

- **Repo:** [harness/harness](https://github.com/harness/harness).
- **Mục đích:** Nền tảng tự host code, pipeline DevOps, Gitspaces và artifact registry.
- **Điểm đáng dùng:** README phân biệt main Harness với nhánh drone; hướng dẫn local nhấn mạnh volume giữ cơ sở dữ liệu và repository.
- **License:** Apache-2.0.
- **Giới hạn:** Tương đương đầy đủ pipeline Drone là mục tiêu, chưa được bảo đảm; mô tả Go tối thiểu cũ hơn go.mod 1.26.11 tại SHA.
- **Tích hợp:** Thử ở môi trường riêng có volume và backup, kiểm tra runner isolation cùng secret trước khi nhận repo khách hàng.
- **Đối chiếu:** [Gitea](../08-awesome-lists-learning/README.md#6c526-tự-host--nhà-thông-minh) cho code hosting; GitLab cho nền tảng tích hợp; Woodpecker CI cho pipeline.
- **Mức kiểm chứng:** `docs-read` — Đọc các phần mô tả và giới hạn trong README, thông báo license, metadata manifest và cấu hình CI khi có; chưa đọc toàn bộ mã triển khai, chưa cài hoặc chạy kiểm thử upstream.
- **Snapshot:** kiểm ngày 2026-11-23; commit `5ef62008529c10601c8190869eb688b633542d18` (2026-11-20T17:26:34Z); 38,955 sao theo GitHub API ngày 2026-11-23. Sao không đại diện chất lượng.
- **Bằng chứng:** [README.md](https://github.com/harness/harness/blob/5ef62008529c10601c8190869eb688b633542d18/README.md) · [LICENSE](https://github.com/harness/harness/blob/5ef62008529c10601c8190869eb688b633542d18/LICENSE) · [go.mod](https://github.com/harness/harness/blob/5ef62008529c10601c8190869eb688b633542d18/go.mod) · [.github/workflows/ci-lint.yml](https://github.com/harness/harness/blob/5ef62008529c10601c8190869eb688b633542d18/.github/workflows/ci-lint.yml) · [GitHub API](https://api.github.com/repos/harness/harness).

<a id="anhkysuai-k3s-io-k3s"></a>

### K3s

- **Repo:** [k3s-io/k3s](https://github.com/k3s-io/k3s).
- **Mục đích:** Bản phân phối Kubernetes gọn để triển khai edge, dev và cụm nhỏ.
- **Điểm đáng dùng:** Một launcher ghép containerd, mạng, DNS, ingress; Kine cho backend dữ liệu khác etcd và SQLite là mặc định.
- **License:** Apache-2.0; thành phần đi kèm có thông báo riêng.
- **Giới hạn:** Claim nhẹ và production-ready chưa được đo tại đây; storage local, HA, backup và nâng cấp vẫn cần thiết kế theo cụm.
- **Tích hợp:** Dùng môi trường thử template deploy, chọn rõ datastore/ingress và thử phục hồi trước khi nhận tải thật.
- **Đối chiếu:** kind cho cụm CI; Minikube cho dev; Kubernetes chuẩn cho vận hành đầy đủ.
- **Mức kiểm chứng:** `docs-read` — Đọc các phần mô tả và giới hạn trong README, thông báo license, metadata manifest và cấu hình CI khi có; chưa đọc toàn bộ mã triển khai, chưa cài hoặc chạy kiểm thử upstream.
- **Snapshot:** kiểm ngày 2026-11-23; commit `647ad6706757349803c34d1e33bc3e7384c68544` (2026-11-19T18:17:01+01:00); 34,499 sao theo GitHub API ngày 2026-11-23. Sao không đại diện chất lượng.
- **Bằng chứng:** [README.md](https://github.com/k3s-io/k3s/blob/647ad6706757349803c34d1e33bc3e7384c68544/README.md) · [LICENSE](https://github.com/k3s-io/k3s/blob/647ad6706757349803c34d1e33bc3e7384c68544/LICENSE) · [go.mod](https://github.com/k3s-io/k3s/blob/647ad6706757349803c34d1e33bc3e7384c68544/go.mod) · [.github/workflows/build-k3s.yaml](https://github.com/k3s-io/k3s/blob/647ad6706757349803c34d1e33bc3e7384c68544/.github/workflows/build-k3s.yaml) · [GitHub API](https://api.github.com/repos/k3s-io/k3s).

<a id="anhkysuai-semantic-release-semantic-release"></a>

### semantic-release

- **Repo:** [semantic-release/semantic-release](https://github.com/semantic-release/semantic-release).
- **Mục đích:** Tự động chọn version, tạo release notes và publish package theo commit.
- **Điểm đáng dùng:** Release engine tách @semantic-release/core, plugin và nhánh quyết định kênh phân phối; cấu hình chia sẻ giúp thống nhất nhiều repo.
- **License:** MIT.
- **Giới hạn:** Commit convention sai có thể chọn sai SemVer; pipeline có quyền publish cần bảo vệ nhánh/token, source manifest development không phải số release.
- **Tích hợp:** Bắt đầu bằng dry run và release branch rõ, chỉ cấp quyền publish cho gate đã qua test/review, khóa plugin.
- **Đối chiếu:** Changesets cho changeset có duyệt; [release-please](../13-dev-stack-devops/README.md) cho release PR; [GoReleaser](../13-dev-stack-devops/README.md#goreleaser) cho binary Go.
- **Mức kiểm chứng:** `docs-read` — Đọc các phần mô tả và giới hạn trong README, thông báo license, metadata manifest và cấu hình CI khi có; chưa đọc toàn bộ mã triển khai, chưa cài hoặc chạy kiểm thử upstream.
- **Snapshot:** kiểm ngày 2026-11-23; commit `abd63c0498a4a9de7551c5fa49770282b5dad893` (2026-11-23T08:13:47Z); 24,193 sao theo GitHub API ngày 2026-11-23. Sao không đại diện chất lượng.
- **Bằng chứng:** [README.md](https://github.com/semantic-release/semantic-release/blob/abd63c0498a4a9de7551c5fa49770282b5dad893/README.md) · [LICENSE](https://github.com/semantic-release/semantic-release/blob/abd63c0498a4a9de7551c5fa49770282b5dad893/LICENSE) · [package.json](https://github.com/semantic-release/semantic-release/blob/abd63c0498a4a9de7551c5fa49770282b5dad893/package.json) · [.github/workflows/test.yml](https://github.com/semantic-release/semantic-release/blob/abd63c0498a4a9de7551c5fa49770282b5dad893/.github/workflows/test.yml) · [GitHub API](https://api.github.com/repos/semantic-release/semantic-release).

## 7. Nguồn

- Development Container Specification: [README]( https://github.com/devcontainers/spec/blob/c95ffeed1d059abfe9ffbe79762dc2fa4e7c2421/README.md ), [devcontainer.json reference]( https://github.com/devcontainers/spec/blob/c95ffeed1d059abfe9ffbe79762dc2fa4e7c2421/docs/specs/devcontainerjson-reference.md ), [schema]( https://github.com/devcontainers/spec/blob/c95ffeed1d059abfe9ffbe79762dc2fa4e7c2421/schemas/devContainer.base.schema.json ), `LICENSE` và `LICENSE-CODE` tại SHA §2.
- OpenTofu: LICENSE, `internal/command/plan.go`, `internal/backend/local/backend_local.go`, docs plan/sensitive-state và `.github/workflows/checks.yml` tại SHA §3.
- Argo CD: LICENSE, `server/application/application.go`, `docs/user-guide/auto_sync.md` và `.github/workflows/ci-build.yaml` tại SHA §4.
- Các permalink trong từng hồ sơ là nguồn gốc đọc 4/11/2026. Số sao không được thu thập; trạng thái release/maintenance không suy chỉ từ HEAD. Không có phép đo hay chạy upstream được nhận là của kho.

<a id="chuyen-muc-2026-11-23"></a>

## Hồ sơ chuyển về từ mục khác — 23/11/2026

6 hồ sơ được chuyển khi chia lại catalog theo `data/taxonomy.json`. Nội dung, ngày kiểm và mức bằng chứng giữ nguyên như ở mục gốc.

<a id="chuyen-caddy"></a>

### caddy

`caddyserver/caddy` · License: Apache License 2.0 · ★ 79.146 · docs-read · 2026-11-18

Máy chủ web/nền tảng máy chủ mở rộng viết bằng Go, mặc định dùng TLS và tự động cấp chứng chỉ HTTPS. HTTPS tự động qua ZeroSSL và Let's Encrypt, có CA nội bộ cho tên/IP nội bộ; hỗ trợ HTTP/1.1, HTTP/2 và HTTP/3 mặc định; cấu hình động qua JSON API, Caddyfile và config adapter, kiến trúc module (thư mục modules/ có caddyhttp, caddytls, caddypki). Điều kiện: Build từ mã cần Go 1.26.0 trở lên; bind cổng thấp trên Linux cần setcap cap_net_bind_service. ★ 18/11/2026: 79.146 (GitHub search API), nhóm "Container & DevOps" trong kho-repo của Phan Đông Giang, mục 08 §6c.5

**Hồ sơ gốc:** [mục 08](../08-awesome-lists-learning/README.md#6c55-container--devops) (bảng/đoạn chung, giữ nguyên tại chỗ).

<a id="chuyen-moby"></a>

### moby

`moby/moby` · License: Apache License 2.0 · ★ 72.275 · docs-read · 2026-11-18

Dự án mã nguồn mở do Docker tạo, cung cấp bộ thành phần để lắp ráp hệ thống container; là upstream của Docker Engine. Docker cam kết dùng Moby làm upstream cho sản phẩm Docker; cung cấp module Go github.com/moby/moby/client và api cho Docker Engine API; có badge OpenSSF Scorecard và OpenSSF Best Practices. Điều kiện: Bản phát hành chỉ hỗ trợ theo khả năng (best effort), không hỗ trợ thương mại; module github.com/docker/docker đã ngừng cập nhật từ v29; việc dùng và chuyển giao có thể chịu hạn chế xuất khẩu của Mỹ và các chính phủ khác. ★ 18/11/2026: 72.275 (GitHub search API), nhóm "Container & DevOps" trong kho-repo của Phan Đông Giang, mục 08 §6c.5

**Hồ sơ gốc:** [mục 08](../08-awesome-lists-learning/README.md#6c55-container--devops) (bảng/đoạn chung, giữ nguyên tại chỗ).

<a id="chuyen-ansible"></a>

### ansible

`ansible/ansible` · License: GNU General Public License v3.0 · ★ 71.623 · docs-read · 2026-11-18

Hệ thống tự động hoá hạ tầng IT (ansible-core): quản lý cấu hình, triển khai ứng dụng, cấp phát cloud, thực thi tác vụ ad-hoc và tự động hoá mạng. Không cần agent, dùng SSH sẵn có; điều phối nhiều node, hỗ trợ cập nhật cuốn chiếu không downtime; được Red Hat tài trợ với hơn 5000 người đóng góp. Điều kiện: GPL v3: phân phối bản sửa đổi phải theo điều khoản copyleft. ★ 18/11/2026: 71.623 (GitHub search API), nhóm "Container & DevOps" trong kho-repo của Phan Đông Giang, mục 08 §6c.5

**Hồ sơ gốc:** [mục 08](../08-awesome-lists-learning/README.md#6c55-container--devops) (bảng/đoạn chung, giữ nguyên tại chỗ).

<a id="chuyen-cilium"></a>

### cilium

`cilium/cilium` · License: Apache License 2.0 cho thành phần user space · ★ 25.863 · docs-read · 2026-11-18

Giải pháp mạng, quan sát và bảo mật cho Kubernetes dựa trên eBPF: CNI, cân bằng tải, chính sách mạng L3-L7, service mesh. Dự án tốt nghiệp (graduated) của CNCF; có thể thay thế hoàn toàn kube-proxy bằng hash table eBPF; duy trì 3 nhánh ổn định (v1.18 đến v1.20), ảnh có SBOM định dạng SPDX từ 1.13. Điều kiện: Cần nhân Linux hỗ trợ eBPF; ảnh chỉ cho AMD64 và AArch64; ảnh build từ main/RC không dùng cho production. ★ 18/11/2026: 25.863 (GitHub search API), nhóm "Container & DevOps" trong kho-repo của Phan Đông Giang, mục 08 §6c.5

**Hồ sơ gốc:** [mục 08](../08-awesome-lists-learning/README.md#6c55-container--devops) (bảng/đoạn chung, giữ nguyên tại chỗ).

<a id="chuyen-sealos"></a>

### sealos

`labring/sealos` · License: Sealos Sustainable Use License 1.0 · ★ 18.398 · docs-read · 2026-11-18

Hệ điều hành cloud xây trên Kubernetes, gom cloud IDE (DevBox), cơ sở dữ liệu quản lý, object storage và app store để phát triển, triển khai và vận hành ứng dụng. Cloud IDE DevBox truy cập từ VSCode và Cursor; cơ sở dữ liệu quản lý PostgreSQL, MySQL, MongoDB, Redis cùng object storage tương thích S3; đa tenant theo workspace với RBAC và quota tài nguyên. Điều kiện: Giấy phép cấm dùng để cung cấp dịch vụ cloud (công khai, riêng hay managed) cho bên thứ ba và hạn chế phân phối; đóng góp phải đồng ý CLA và điều khoản đổi giấy phép. ★ 18/11/2026: 18.398 (GitHub search API), nhóm "Container & DevOps" trong kho-repo của Phan Đông Giang, mục 08 §6c.5

**Hồ sơ gốc:** [mục 08](../08-awesome-lists-learning/README.md#6c55-container--devops) (bảng/đoạn chung, giữ nguyên tại chỗ).

<a id="chuyen-kubesphere"></a>

### kubesphere

`kubesphere/kubesphere` · License: Apache License 2.0 kèm điều kiện bổ sung · ★ 17.083 · docs-read · 2026-11-18

Nền tảng container đa thuê bao dùng Kubernetes làm nhân, quản lý ứng dụng cloud-native đa cụm, datacenter và biên qua giao diện web, có kiến trúc mở rộng bằng plugin. Quản lý đa cụm Kubernetes từ một control plane tập trung; tích hợp DevOps (Argo CD, Jenkins), service mesh dựa Istio, App Store cho Helm và biên qua KubeEdge; hỗ trợ cài đặt air-gapped. Điều kiện: Cần cụm Kubernetes; giấy phép v4.x cấm dùng thương mại cho bên thứ ba, SaaS hoặc đổi thương hiệu nếu không có giấy phép thương mại (liên hệ kubesphere@yunify.com). ★ 18/11/2026: 17.083 (GitHub search API), nhóm "Container & DevOps" trong kho-repo của Phan Đông Giang, mục 08 §6c.5

**Hồ sơ gốc:** [mục 08](../08-awesome-lists-learning/README.md#6c55-container--devops) (bảng/đoạn chung, giữ nguyên tại chỗ).

<a id="n2-2026-11-24"></a>

## Nâng trần đợt hai — 23/11/2026

Hồ sơ lập trong đợt nâng trần thứ hai: đọc mã hoặc tài liệu tại commit cố định, chưa chạy upstream; mô tả của trinh sát sai ở nhiều repo nên điều ghi ở đây là điều đã đọc.

<a id="n2-gatekeeper"></a>

### OPA Gatekeeper

| Thuộc tính | Giá trị |
|---|---|
| Repo | https://github.com/open-policy-agent/gatekeeper |
| License | Apache-2.0 |
| Phiên bản đã đọc | `a2bac802bc01a8a1a7639d7b52050ffa79fc785d` (commit 2026-11-20) |
| Kiểm chứng | 2026-11-24; code-read; đã đọc README.md, LICENSE, go.mod, example/templates/k8srequiredlabels_template.yaml, website/docs/gator.md, failing-closed.md, violations.md, pkg/webhook/policy.go (dòng kubebuilder webhook), .github/workflows/test-gator-policy.yaml và unit-test.yaml (đoạn run); chưa chạy upstream |
| Khoảng trống lấp | Policy-as-code admission/runtime (admission controller dùng OPA) |
| Cơ chế đáng học | - Hai CRD: `ConstraintTemplate` chứa Rego và schema tham số, `Constraint` là bản khởi tạo (example/templates/k8srequiredlabels_template.yaml: luật `violation` tính tập nhãn thiếu).<br>- `enforcementAction` mỗi constraint: mặc định `deny`, có `dryrun`, `warn` (website/docs/violations.md) để triển khai chính sách theo từng bước; audit định kỳ (cờ `--audit-interval` mặc định 60 giây trong pkg/audit/manager.go) quét tài nguyên có sẵn.<br>- `gator verify` chạy `Suite` (`test.gatekeeper.sh/v1alpha1`) với các `Case` khẳng định pass/fail; `gator test` thoát theo mã trạng thái (website/docs/gator.md). |
| Tiêu chí và cách kiểm | Kiểm bằng máy: gator verify trong CI, workflow test-gator-policy chạy e2e và unit-test chạy `make native-test`, race, benchmark. Chưa chạy. |
| Giới hạn và rủi ro | Webhook mặc định `failurePolicy=ignore` (kubebuilder marker trong pkg/webhook/policy.go; trang failing-closed.md giải thích): khi webhook sập thì yêu cầu lọt qua, cần chủ động đổi sang `Fail`. Thư viện constraint template đã chuyển sang repo riêng (library/README.md chỉ còn liên kết), nên trinh sát nói có thư viện trong repo là không đúng. Badge OPA v0.60.0 trong README lỗi thời: go.mod dùng opa v1.22.4. Có driver k8scel cho ValidatingAdmissionPolicy (pkg/drivers/k8scel, chưa đọc sâu). |
| So với | `kyverno` (chính sách YAML/CEL, không cần Rego); `open-policy-agent-opa` (engine lõi); `opa-conftest` (kiểm file ngoài cluster). |
| Nguồn | [README](https://github.com/open-policy-agent/gatekeeper/blob/a2bac802bc01a8a1a7639d7b52050ffa79fc785d/README.md) · [LICENSE](https://github.com/open-policy-agent/gatekeeper/blob/a2bac802bc01a8a1a7639d7b52050ffa79fc785d/LICENSE) · [go.mod](https://github.com/open-policy-agent/gatekeeper/blob/a2bac802bc01a8a1a7639d7b52050ffa79fc785d/go.mod) · [k8srequiredlabels_template.yaml](https://github.com/open-policy-agent/gatekeeper/blob/a2bac802bc01a8a1a7639d7b52050ffa79fc785d/example/templates/k8srequiredlabels_template.yaml) · [website/docs/gator.md](https://github.com/open-policy-agent/gatekeeper/blob/a2bac802bc01a8a1a7639d7b52050ffa79fc785d/website/docs/gator.md) · [website/docs/failing-closed.md](https://github.com/open-policy-agent/gatekeeper/blob/a2bac802bc01a8a1a7639d7b52050ffa79fc785d/website/docs/failing-closed.md) · [website/docs/violations.md](https://github.com/open-policy-agent/gatekeeper/blob/a2bac802bc01a8a1a7639d7b52050ffa79fc785d/website/docs/violations.md) · [pkg/webhook/policy.go](https://github.com/open-policy-agent/gatekeeper/blob/a2bac802bc01a8a1a7639d7b52050ffa79fc785d/pkg/webhook/policy.go) · [.github/workflows/test-gator-policy.yaml](https://github.com/open-policy-agent/gatekeeper/blob/a2bac802bc01a8a1a7639d7b52050ffa79fc785d/.github/workflows/test-gator-policy.yaml) · [.github/workflows/unit-test.yaml](https://github.com/open-policy-agent/gatekeeper/blob/a2bac802bc01a8a1a7639d7b52050ffa79fc785d/.github/workflows/unit-test.yaml) |

<a id="n2-changesets"></a>

### Changesets

| Thuộc tính | Giá trị |
|---|---|
| Repo | https://github.com/changesets/changesets |
| License | MIT |
| Phiên bản đã đọc | `4582bbc9b44411be7bc440fec6081e5f794a62e2` (commit 2026-11-23) |
| Kiểm chứng | 2026-11-24; code-read; đã đọc README.md, assemble-release-plan/src/index.ts, changelog-git/src/index.ts, ci.yml; chưa chạy upstream |
| Khoảng trống lấp | Changelog và ghi chú phát hành như tài liệu: nguồn là file khai báo cấp PR, không phải commit message |
| Cơ chế đáng học | - Mỗi PR thêm một file changeset (gói, mức bump, tóm tắt); `assembleReleasePlan` trong `packages/assemble-release-plan/src/index.ts` gộp thành kế hoạch, mỗi gói một release.<br>- Vòng `while` lặp `determineDependents`, `matchFixedConstraint`, `applyLinks` tới khi không còn thay đổi, nên bump lan qua gói phụ thuộc, nhóm `fixed` và `linked`.<br>- Snapshot release: hậu tố từ mẫu có chỗ giữ `{tag}`, `{commit}`, `{datetime}`; mặc định cơ sở `0.0.0` để không chen vào range prerelease thật.<br>- Định dạng changelog cắm được qua `ChangelogFunctions` (`packages/changelog-git/src/index.ts` là bản tối giản). |
| Tiêu chí và cách kiểm | Kiểm bằng máy: kiểm hợp lệ (gói không có trong workspace thì ném lỗi), test vitest có sẵn cạnh mã. CI (`ci.yml`) build, lint workflow bằng zizmor, kiểm khóa workflow, chạy test ma trận Node 22/24/26 và thêm macOS/Windows. Mã thoát của `changeset status` làm cổng bắt buộc có changeset là cách repo lingo.dev dùng trong CI của họ, còn bản thân lệnh chưa đọc đến mã thoát (chưa xác minh). |
| Giới hạn và rủi ro | MIT. Nhánh mặc định là bản phát triển v3, v2 nằm nhánh bảo trì nên cần ghim phiên bản. Mô hình bắt người đóng góp viết changeset (kỷ luật con người, thiếu thì CI mới chặn). Changelog-github gọi API GitHub nên cần token (chưa đọc kỹ). Không thấy telemetry trong mã đã grep nhưng không quét toàn bộ. |
| So với | release-please (sinh từ conventional commits, hồ sơ có sẵn), semantic-release (tự động hóa hoàn toàn từ commit): Changesets đắt giá khi muốn ghi chú viết tay cho người dùng và nhiều gói |
| Nguồn | [LICENSE](https://github.com/changesets/changesets/blob/4582bbc9b44411be7bc440fec6081e5f794a62e2/LICENSE) · [README.md](https://github.com/changesets/changesets/blob/4582bbc9b44411be7bc440fec6081e5f794a62e2/README.md) · [index.ts](https://github.com/changesets/changesets/blob/4582bbc9b44411be7bc440fec6081e5f794a62e2/packages/assemble-release-plan/src/index.ts) · [index.ts](https://github.com/changesets/changesets/blob/4582bbc9b44411be7bc440fec6081e5f794a62e2/packages/changelog-git/src/index.ts) · [ci.yml](https://github.com/changesets/changesets/blob/4582bbc9b44411be7bc440fec6081e5f794a62e2/.github/workflows/ci.yml) |
