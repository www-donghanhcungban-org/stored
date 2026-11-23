# 31 · Bảo mật chuỗi cung ứng phần mềm và bằng chứng phát hành

> Khép đường từ source và dependency đến artifact được phép chạy: biết thành phần, phát hiện rủi ro, kiểm nguồn gốc và đưa quyết định policy vào CI/deploy. Đây là chuỗi cung ứng phần mềm nói chung; hành vi LLM/tool xem [mục 12](../12-ai-security-guardrails/README.md).

## 1. Trần cần đạt cho xưởng phần mềm

Một repo xanh CI chưa trả lời artifact nào đang chạy, do builder nào tạo, dùng dependency nào, ai phê duyệt ngoại lệ hay bản nào phải thu hồi khi có CVE mới. Xưởng cần gắn source SHA → dependency lock → build identity → artifact digest → SBOM/provenance → policy decision → deployment inventory. Agent có thể đề xuất bản vá; quyền bỏ qua cổng và trust root phải độc lập với tác vụ viết code.

**Ngày đọc:** 2026-11-04. Ba hồ sơ dưới được đọc LICENSE, implementation/callsite và CI tại full SHA. Không cài/chạy upstream, không quét sản phẩm và không tái lập benchmark; số sao để trống. License trong bảng áp dụng code của repo đã đọc, không tự bao phủ dependency, dữ liệu advisory hoặc dịch vụ kết nối.

| Lớp | Công cụ đã có trong kho | Nâng sâu ở mục này |
|---|---|---|
| Secret/SAST | Gitleaks, TruffleHog, Semgrep, CodeQL | Phủ cả history/artifact, baseline có expiry và phát hiện secret phải đi kèm rotation |
| SCA/SBOM | OSV-Scanner, Trivy, Grype, Syft | Gắn SBOM đúng digest; phân biệt scan một lần với theo dõi sau phát hành |
| Provenance/signature | SLSA, cosign | Xác minh builder/issuer/subject/digest và chính sách thực thi, không chỉ có chữ ký |
| Supply-chain workflow | in-toto | Ràng buộc các bước, người ký và artifact materials/products |
| Portfolio/triage | OWASP Dependency-Track | Theo dõi component qua nhiều phiên bản sản phẩm và policy |
| Graph quan hệ | GUAC | Truy vấn phạm vi ảnh hưởng; giữ trust decision riêng với việc ingest |

## 2. Ba hồ sơ đọc mã mới

<a id="factory-2026-11-04-in-toto"></a>

### 2.1 in-toto: layout, người ký và chuỗi materials/products

| Thuộc tính | Kết quả đọc |
|---|---|
| Repo · license · SHA | `in-toto/in-toto` · Apache-2.0 · `e352b43ad7cb8915d84c36d791aa61346152a0a3` |
| Tác giả/quản trị | Dự án in-toto; LICENSE ghi New York University và repository có GOVERNANCE/MAINTAINERS. Đây là Python implementation, không đồng nhất với mọi in-toto attestation consumer |
| Cơ chế | Chủ chuỗi ký layout gồm steps, functionary keys, thresholds, artifact rules và inspections; mỗi bước có link metadata chứa materials/products và chữ ký |
| Enforcement | `in_toto_verify` kiểm layout signatures/expiry, link signatures, thresholds và rules trước khi chạy inspections; CLI trả 1 khi verification thất bại, 2 khi tham số sai |
| Hai bẫy quan trọng | Artifact không bị rule tiêu thụ mặc định được phép; cần terminal `DISALLOW *` khi policy muốn đóng tập. Command alignment là **soft verify**, mismatch chỉ ghi warning trong Python implementation đã đọc, không tự làm verification fail |
| Ranh giới | Chỉ artifact được truyền làm materials/products mới được ghi; không tự quan sát mọi file đã đọc/ghi. Chữ ký không bảo đảm người ký/builder trung thực. Inspections là lệnh thực thi từ layout đã được tin cậy, nên verifier cũng cần scope/quyền nhỏ |
| Tích hợp | Với chuỗi build nhỏ, chốt layout/key custody và rule MATCH giữa từng bước; review negative fixtures thiếu link, sai signer, đổi digest, file phát sinh ngoài policy, layout hết hạn. Command bắt buộc phải được kiểm bằng policy/inspection riêng thay vì tin expected_command |
| CI | `ci.yml` gọi `_test.yml`: tox trên nhiều OS/Python, một nhánh dependency-main là experimental. Chưa chạy các test này tại kho |

**Nguồn:** [LICENSE](https://github.com/in-toto/in-toto/blob/e352b43ad7cb8915d84c36d791aa61346152a0a3/LICENSE) · [layout/rules README](https://github.com/in-toto/in-toto/blob/e352b43ad7cb8915d84c36d791aa61346152a0a3/README.md) · [verify callsite](https://github.com/in-toto/in-toto/blob/e352b43ad7cb8915d84c36d791aa61346152a0a3/in_toto/verifylib.py) · [CLI outcomes](https://github.com/in-toto/in-toto/blob/e352b43ad7cb8915d84c36d791aa61346152a0a3/in_toto/in_toto_verify.py) · [CI](https://github.com/in-toto/in-toto/blob/e352b43ad7cb8915d84c36d791aa61346152a0a3/.github/workflows/_test.yml).

<a id="factory-2026-11-04-owasp-dependency-track"></a>

### 2.2 OWASP Dependency-Track: SBOM là đầu vào cho quản trị rủi ro liên tục

| Thuộc tính | Kết quả đọc |
|---|---|
| Repo · license · SHA | `DependencyTrack/dependency-track` · Apache-2.0 · `2e3fd965a76bbfdd9e7ec1fb990600cc1f4f11ba` |
| Quản trị/phạm vi | Dự án OWASP, quản lý component theo project/version; frontend và tài liệu là repository riêng. Nguồn đọc là nhánh main hiện có, không tự suy mọi image/tag v4/v5 cùng API |
| Đường gọi | `BomResource` nhận SBOM và trả token theo dõi xử lý; `EventResource` đọc workflow status; `CelPolicyEngine` biên dịch/đánh giá điều kiện policy và tạo policy violations |
| Bẫy CI | Upload HTTP thành công không phải phân tích thành công. Endpoint BOM token cũ nêu rõ `processing=false` còn có thể là token không tồn tại; endpoint cũ deprecated, phải dùng API đúng phiên bản và kiểm terminal status, project/version cùng policy result |
| Vận hành | Có state/database và nguồn advisory ngoài; cần backup/restore, quyền API theo project, khả năng reach feed và tuổi feed. Migration v4/v5 phải đọc tài liệu cutover rồi pin image/digest; không đổi tag latest mà không chủ ý |
| Tích hợp | Upload CycloneDX cho đúng release digest; chờ kết quả có timeout/error rõ; query policy violations đã hoàn tất rồi adapter CI quyết định chặn. Theo dõi lại các bản còn chạy khi advisory thay đổi, không chỉ scan lúc merge |
| CI | `ci-test.yaml` chạy Maven/JDK và có workflow E2E riêng; chưa triển khai server hoặc chạy kiểm tích hợp |

**Nguồn:** [LICENSE](https://github.com/DependencyTrack/dependency-track/blob/2e3fd965a76bbfdd9e7ec1fb990600cc1f4f11ba/LICENSE.txt) · [BOM upload/token](https://github.com/DependencyTrack/dependency-track/blob/2e3fd965a76bbfdd9e7ec1fb990600cc1f4f11ba/apiserver/src/main/java/org/dependencytrack/resources/v1/BomResource.java) · [event status](https://github.com/DependencyTrack/dependency-track/blob/2e3fd965a76bbfdd9e7ec1fb990600cc1f4f11ba/apiserver/src/main/java/org/dependencytrack/resources/v1/EventResource.java) · [policy enforcement](https://github.com/DependencyTrack/dependency-track/blob/2e3fd965a76bbfdd9e7ec1fb990600cc1f4f11ba/apiserver/src/main/java/org/dependencytrack/policy/cel/CelPolicyEngine.java) · [migration contract](https://github.com/DependencyTrack/dependency-track/blob/2e3fd965a76bbfdd9e7ec1fb990600cc1f4f11ba/V5_MIGRATION.md) · [CI](https://github.com/DependencyTrack/dependency-track/blob/2e3fd965a76bbfdd9e7ec1fb990600cc1f4f11ba/.github/workflows/ci-test.yaml).

<a id="factory-2026-11-04-guac"></a>

### 2.3 GUAC: đồ thị phạm vi ảnh hưởng cần nguồn và trạng thái tin cậy

| Thuộc tính | Kết quả đọc |
|---|---|
| Repo · license · SHA | `guacsec/guac` · Apache-2.0 · `a3f0a4df51abcf271221cf9c400de3158d9c20fa` |
| Quản trị/phạm vi | README xác định là dự án OpenSSF incubating; tổng hợp SBOM, vulnerability và provenance thành quan hệ package/source/artifact |
| Cơ chế | Parser CycloneDX/SPDX/SLSA/DSSE đưa dữ liệu vào graph; graph phục vụ câu hỏi package/version/digest nào nằm trong sản phẩm nào và quan hệ nguồn gốc |
| Kiểm đường gọi | `pkg/ingestor/verifier/verifier.go` phân biệt identity đã verify với identity đáng tin. Trong DSSE parser tại SHA này, `GetIdentities` trả mảng rỗng và phần đưa trust information vào graph còn TODO; không diễn giải ingest thành trust decision đầy đủ |
| Rủi ro | README tự nêu có trường hợp phải dùng heuristic nối identifier; thiếu/sai purl/digest có thể làm thiếu hoặc nối nhầm quan hệ. Graph không tự thay việc verify artifact tại deploy |
| Vận hành | README phân biệt in-memory keyvalue với persistent ent/PostgreSQL; backend thử nghiệm/không hỗ trợ không nên được coi tương đương production. Ingestor/collector có thể gọi dịch vụ metadata ngoài; kiểm dữ liệu được gửi theo deployment |
| Tích hợp | Giữ origin, ingest time và evidence digest; truy vấn tác động cho CVE/namespace/version cụ thể; đối chiếu với deployment inventory. Gate release vẫn phải xác minh signer/builder/digest bằng verifier đã chốt trust root |
| CI | `ci.yaml` có Go unit tests/static analysis/lint; chưa chạy graph hay kiểm độ đầy đủ của truy vấn trong đợt này |

**Nguồn:** [LICENSE](https://github.com/guacsec/guac/blob/a3f0a4df51abcf271221cf9c400de3158d9c20fa/LICENSE) · [scope/backends](https://github.com/guacsec/guac/blob/a3f0a4df51abcf271221cf9c400de3158d9c20fa/README.md) · [verifier semantics](https://github.com/guacsec/guac/blob/a3f0a4df51abcf271221cf9c400de3158d9c20fa/pkg/ingestor/verifier/verifier.go) · [DSSE callsite](https://github.com/guacsec/guac/blob/a3f0a4df51abcf271221cf9c400de3158d9c20fa/pkg/ingestor/parser/dsse/parser_dsse.go) · [CycloneDX parser](https://github.com/guacsec/guac/blob/a3f0a4df51abcf271221cf9c400de3158d9c20fa/pkg/ingestor/parser/cyclonedx/parser_cyclonedx.go) · [CI](https://github.com/guacsec/guac/blob/a3f0a4df51abcf271221cf9c400de3158d9c20fa/.github/workflows/ci.yaml).

## 3. So sánh theo quyết định cần đưa ra

| Nhiệm vụ | Baseline nhỏ | Lựa chọn sâu hơn | Điểm không được đánh tráo |
|---|---|---|---|
| Biết thành phần của một image | Syft + SBOM theo digest | Dependency-Track khi nhiều release cần theo dõi | SBOM đầy đủ phụ thuộc cách build/detect; có file SBOM không chứng minh đầy đủ |
| Biết advisory ảnh hưởng gì | Grype / OSV-Scanner / Trivy | Dependency-Track portfolio hoặc GUAC graph | CVE match, exploitability và chấp nhận rủi ro là ba quyết định khác nhau |
| Xác minh artifact được phép dùng | cosign với issuer/subject/digest policy | in-toto khi cần ràng buộc nhiều bước/signer | Chữ ký hợp lệ không chứng minh code sạch hay builder không bị chiếm |
| Đánh giá upstream trước nhận dependency | OpenSSF Scorecard + đọc LICENSE/CI | Review release provenance, maintainer và sandbox build | Điểm Scorecard là tín hiệu, không phải giấy chứng nhận an toàn |
| Chặn policy của xưởng | Script tất định nhỏ/OPA-Conftest | Policy engine theo fleet khi có ownership rõ | Không để chính agent sửa threshold/allowlist để làm check xanh |

**Stack tối thiểu:** khóa dependency và tool → secret scan/SAST/SCA theo scope → build ở runner tách quyền → sinh SBOM/provenance gắn artifact digest → ký từ identity riêng → verify và đánh giá policy trước deploy → lưu inventory + theo dõi advisory sau phát hành. Chỉ thêm Dependency-Track khi có nhu cầu portfolio; chỉ thêm GUAC khi câu hỏi đồ thị liên repo có giá trị đủ bù chi phí vận hành. Không buộc mọi dự án nhỏ dựng đủ mọi dịch vụ.

## 4. Cổng nghiệm thu và bằng chứng phải giao cùng phần mềm

| Cổng | Fixture cố tình sai | Kỳ vọng kiểm được |
|---|---|---|
| Artifact identity | Thay byte artifact sau khi tạo SBOM/ký | Digest mismatch làm fail trước deploy |
| Signer/builder | Chữ ký đúng khóa nhưng issuer/subject/builder ngoài policy | Từ chối; không chỉ kiểm cryptographic validity |
| Supply-chain steps | Thiếu link hoặc sai functionary/threshold, tạo file ngoài rules | in-toto fail; test command mismatch có policy riêng vì native chỉ warning |
| Vulnerability/license | Component vi phạm policy, feed quá cũ hoặc scan timeout | Fail/inconclusive rõ; exception có owner, lý do, scope, expiry |
| Async analysis | Token rác, job thất bại, `processing=false` nhưng thiếu status | Không công nhận pass; so đúng project/version/release |
| Inventory/recall | CVE fixture ảnh hưởng bản cũ đang chạy | Truy ra deployment/owner và có cách rollback/rebuild |
| Secret exposure | Secret giả trong diff/history/artifact | Cổng phát hiện; quy trình incident có revoke/rotate, không chỉ xóa chuỗi khỏi HEAD |

Artifact bàn giao gồm source SHA, lock digest, builder identity, image/package digest, SBOM định dạng/version, provenance/signature bundle, policy version, kết quả checks và ngoại lệ còn hiệu lực. Giới hạn retention, quyền xem và log dữ liệu nhạy cảm phải được ghi theo sản phẩm. Backup/restore catalog và trust roots được diễn tập ở môi trường tích hợp; kho này chưa chứng minh khả năng đó.

## 5. Liên kết toàn xưởng và giới hạn nghiên cứu

- [09 · Checklist](../09-engineering-checklists/README.md): release checklist có owner và bằng chứng, không chỉ dấu tick.
- [11 · Sandbox](../11-browser-computer-use-sandbox/README.md): agent/PR không tin cậy không được cầm secret phát hành.
- [12 · AI Security](../12-ai-security-guardrails/README.md): prompt/tool injection và quyền agent là lớp bổ sung.
- [13 · Dev Stack](../13-dev-stack-devops/README.md): toolchain, build và release tái lập.
- [30 · Kiểm thử](../30-software-testing-quality/README.md): gate phải có test phủ định chứng minh nó bắt được lỗi.
- [32 · Delivery](../32-platform-delivery-engineering/README.md): deployment chỉ nhận digest đã verify; rollout/rollback có kiểm.

Ngày snapshot không phải ngày xác minh mọi hồ sơ cũ được dẫn. Phát hiện về parser/CLI chỉ áp dụng SHA đã đọc; chưa xác minh mọi cấu hình runtime, advisory feed, latency, độ phủ scanner hoặc tình trạng toàn bộ release. Không cộng các lớp thành một điểm an toàn duy nhất.

<a id="anhkysuai-2026-11-23"></a>

## Đánh giá từ kho Anh Kỹ Sư AI — 23/11/2026

Phần này có **1 hồ sơ hoặc phạm vi đối chiếu** từ [nguồn tuyển chọn](https://anhkysuai.com/kho/). [Bảng đủ 1.295 repo](../data/collections/anhkysuai-kho.json) ghi trạng thái đối chiếu từng link; [danh sách URL](../data/collections/anhkysuai-kho-links.txt) phục vụ tra cứu. Nguồn tuyển chọn giúp phát hiện repo; đánh giá bên dưới dựa trên clone và permalink upstream cùng metadata GitHub ngày 2026-11-23.

Mức `docs-read`/`code-read` chỉ áp dụng phạm vi ghi tại mỗi hồ sơ. Chưa cài, build, chạy test hay benchmark mã upstream. Giấy phép có thể tách theo code, model, nội dung, asset hoặc bản enterprise; con số/tuyên bố của tác giả chưa được tái lập nếu không có ghi chú khác.

<a id="anhkysuai-getsops-sops"></a>

### SOPS

**Repo:** [getsops/sops](https://github.com/getsops/sops) · **License:** MPL-2.0 · **Kiểm:** 2026-11-23, `docs-read`, [`9aa10f12bcd8`](https://github.com/getsops/sops/tree/9aa10f12bcd82400b7eb73331dd7a87a93bb17f7) (commit 2026-11-09). **Sao:** 23,807 tại 2026-11-23 theo [GitHub API](https://api.github.com/repos/getsops/sops).

| Mục | Đánh giá |
|---|---|
| Mục đích | Công cụ sửa tệp bí mật đã mã hóa theo YAML, JSON, ENV, INI hoặc binary. |
| Giá trị và cơ chế theo tài liệu | README liệt kê KMS cloud, age và PGP; Go manifest nối từng provider, CI build/test theo OS/architecture giúp đánh giá chuỗi sử dụng CLI. |
| Giới hạn | Mã hóa tệp không thay quản trị khóa, quyền KMS hoặc bảo vệ plaintext trong editor/CI. Chưa kiểm cơ chế cryptography hay recovery khi mất khóa. |
| Điều kiện tích hợp | Thử tệp giả và policy recipient, bảo đảm recovery/rotation trước dùng secrets thật; tránh plaintext trong log, diff, artifact và giới hạn quyền giải mã pipeline. |
| Lựa chọn đối chiếu | age; git-crypt; Sealed Secrets. |

**Phạm vi bằng chứng:** đã clone, đọc trích đoạn tài liệu, giấy phép và các file cấu hình được dẫn dưới đây; chưa chạy mã, build, benchmark hoặc test upstream. `docs-read` không phải kiểm chứng implementation.

**Nguồn tại cùng SHA:** [README.rst](https://github.com/getsops/sops/blob/9aa10f12bcd82400b7eb73331dd7a87a93bb17f7/README.rst) · [LICENSE](https://github.com/getsops/sops/blob/9aa10f12bcd82400b7eb73331dd7a87a93bb17f7/LICENSE) · [go.mod](https://github.com/getsops/sops/blob/9aa10f12bcd82400b7eb73331dd7a87a93bb17f7/go.mod) · [.github/workflows/cli.yml](https://github.com/getsops/sops/blob/9aa10f12bcd82400b7eb73331dd7a87a93bb17f7/.github/workflows/cli.yml).

<a id="chuyen-muc-2026-11-23"></a>

## Hồ sơ chuyển về từ mục khác — 23/11/2026

2 hồ sơ được chuyển khi chia lại catalog theo `data/taxonomy.json`. Nội dung, ngày kiểm và mức bằng chứng giữ nguyên như ở mục gốc.

<a id="chuyen-zizmor"></a>

### zizmor

`zizmorcore/zizmor` · License: MIT · ★ 6.856

Phân tích tĩnh bảo mật GitHub Actions, 41 audit, SARIF, offline/online; bản 1.31.1; ★ 2/11/2026 (GitHub search API), mục 13 §6h

**Hồ sơ gốc:** [mục 13](../13-dev-stack-devops/README.md) (bảng/đoạn chung, giữ nguyên tại chỗ).

<a id="chuyen-infisical"></a>

### infisical

`Infisical/infisical` · License: MIT · ★ 30.570 · docs-read · 2026-11-18

Nền tảng hạ tầng bảo mật mã nguồn mở để quản lý bí mật, chứng chỉ, khoá, truy cập đặc quyền và truy cập của AI agent; có quét lộ bí mật. Hỗ trợ xoay vòng bí mật và bí mật động cho PostgreSQL, MySQL, AWS IAM; có Kubernetes Operator, CLI và SDK cho nhiều ngôn ngữ (Node, Python, Go, Java, .NET, Rust...); tự host được bằng Docker Compose. Điều kiện: Tính năng trong thư mục ee/ cần giấy phép doanh nghiệp Infisical; chạy cục bộ cần Git và Docker; có bản Infisical Cloud trả phí/miễn phí tuỳ gói. ★ 18/11/2026: 30.570 (GitHub search API), nhóm "Bảo mật & Hack" trong kho-repo của Phan Đông Giang, mục 08 §6c.5

**Hồ sơ gốc:** [mục 08](../08-awesome-lists-learning/README.md#6c53-bảo-mật--hack) (bảng/đoạn chung, giữ nguyên tại chỗ).

<a id="chuan-hoa-2026-11-23"></a>

## Chuẩn hóa bằng chứng hồ sơ cũ — 23/11/2026

Các hồ sơ dưới đây có từ trước khi kho ghi mức kiểm. Ngày 2026-11-23 mỗi repo được clone nông tại commit ghi trong bảng, đọc LICENSE, README, manifest và CI (nếu có); không cài, build hay chạy mã upstream. Nhận định cũ ở phần trên giữ nguyên; chỗ nào khác với lần đọc này được ghi trong cột Nhận định. Số sao lấy qua GitHub search API cùng ngày.

<a id="ch-zizmor"></a>

### zizmor

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/zizmorcore/zizmor |
| License | MIT |
| Phiên bản đã đọc | `0af0be985a4cae71ecfaa64ef574a94b35dc722a` (commit 2026-11-22) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE, Cargo.toml, .github/workflows/ci.yml; chưa chạy upstream |
| Bảo trì | active (commit mới nhất 2026-11-22) |
| Nhận định | Công cụ phân tích tĩnh cho CI/CD (GitHub Actions, Dependabot, pre-commit): template injection, lộ credential, quyền thừa, impostor commit; Rust v1.33.1, có fix tự động. |
| Nguồn | [README](https://github.com/zizmorcore/zizmor/blob/0af0be985a4cae71ecfaa64ef574a94b35dc722a/README.md) · [LICENSE](https://github.com/zizmorcore/zizmor/blob/0af0be985a4cae71ecfaa64ef574a94b35dc722a/LICENSE) · [manifest](https://github.com/zizmorcore/zizmor/blob/0af0be985a4cae71ecfaa64ef574a94b35dc722a/Cargo.toml) · [workflow](https://github.com/zizmorcore/zizmor/blob/0af0be985a4cae71ecfaa64ef574a94b35dc722a/.github/workflows/ci.yml) |

<a id="nt-2026-11-23"></a>

## Nâng trần theo khoảng trống — 23/11/2026

Phần này có các hồ sơ mới của đợt nâng trần: mười trinh sát tìm trên internet và GitHub những mảng mà chuyên mục còn thiếu hoặc chỉ có hồ sơ cũ, rồi mỗi repo được clone nông tại một commit cố định, đọc LICENSE, README, ít nhất một file triển khai thật và CI nếu có; không cài hay chạy mã upstream. Mô tả của trinh sát nhiều chỗ sai so với mã thật, và các chỗ đó được sửa ngay trong từng hồ sơ. Số sao lấy sau bằng GitHub search API nên có thể để trống.

<a id="nt-microsoft-sbom-tool"></a>

### SBOM Tool (Microsoft)

| Thuộc tính | Giá trị |
|---|---|
| Repo | https://github.com/microsoft/sbom-tool |
| License | MIT |
| Phiên bản đã đọc | `4d2b44739b4317ff2655b4076292ca2522d376bf` (commit 2026-09-21) |
| Kiểm chứng | 2026-11-23; code-read; đã đọc README.md, LICENSE, docs/feature-overview.md, src/Microsoft.Sbom.Parsers.Spdx30SbomParser/Generator.cs, .github/workflows/codeql-analysis.yml, SECURITY.md; chưa chạy upstream |
| Khoảng trống lấp | Chuỗi cung ứng AI: SBOM theo SPDX (thay cho CycloneDX khi bên nhận yêu cầu SPDX); chưa có AI-BOM hay VEX |
| Cơ chế đáng học | - Phần files duyệt `BuildDropPath`, sinh SPDXID, băm SHA256 và SHA1 cho mỗi file (docs/feature-overview.md).<br>- Phần packages dùng Component Detection quét `BuildComponentPath` theo hệ sinh thái (Cargo, Ruby...), tra giấy phép qua ClearlyDefined.<br>- Parser tách riêng cho SPDX 2.2 và 3.0 (`Microsoft.Sbom.Parsers.Spdx30SbomParser/Generator.cs`), có API NuGet và công cụ dotnet. |
| Tiêu chí và cách kiểm | Kiểm bằng máy: có nhiều dự án test xUnit theo từng module (thư mục `test/`), workflow codeql-analysis.yml (đã đọc, quét C# theo lịch hằng tuần). Pipeline build và release nằm trong `pipelines/` (chưa mở). Không có ngưỡng đạt/hỏng riêng cho nội dung SBOM. |
| Giới hạn và rủi ro | MIT. README mục Telemetry: telemetry ghi ra file JSON cạnh đầu ra, không gửi cho Microsoft (tuyên bố tác giả, chưa xác minh). Tra giấy phép qua ClearlyDefined cần mạng (trong tài liệu). Không nhận đóng góp ngoài; ngôn ngữ .NET, bản trinh sát nêu đúng là thay thế SPDX. |
| So với | Syft (syft, sinh SBOM đa định dạng gồm SPDX và CycloneDX), Trivy (cũng sinh SBOM) |
| Nguồn | [README.md](https://github.com/microsoft/sbom-tool/blob/4d2b44739b4317ff2655b4076292ca2522d376bf/README.md) · [LICENSE](https://github.com/microsoft/sbom-tool/blob/4d2b44739b4317ff2655b4076292ca2522d376bf/LICENSE) · [feature-overview.md](https://github.com/microsoft/sbom-tool/blob/4d2b44739b4317ff2655b4076292ca2522d376bf/docs/feature-overview.md) · [Generator.cs](https://github.com/microsoft/sbom-tool/blob/4d2b44739b4317ff2655b4076292ca2522d376bf/src/Microsoft.Sbom.Parsers.Spdx30SbomParser/Generator.cs) · [codeql-analysis.yml](https://github.com/microsoft/sbom-tool/blob/4d2b44739b4317ff2655b4076292ca2522d376bf/.github/workflows/codeql-analysis.yml) · [SECURITY.md](https://github.com/microsoft/sbom-tool/blob/4d2b44739b4317ff2655b4076292ca2522d376bf/SECURITY.md) |

<a id="nt-gh-actions-lock"></a>

### gh-actions-lock

| Thuộc tính | Giá trị |
|---|---|
| Repo | https://github.com/github/gh-actions-lock |
| License | MIT (LICENSE, Copyright GitHub, Inc.). Không có trọng số |
| Phiên bản đã đọc | `d8e1ae3518e8ae47f38c291c1ebe68c10fcee346` (commit 2026-11-19) |
| Kiểm chứng | 2026-11-23; code-read; đã đọc `README.md`, `LICENSE`, `.github/workflows/actions.lock`, `internal/resolve/ancestry.go`, `internal/config/cooldown.go`, `.github/workflows/verify-lockfile.yml`, `.github/workflows/test.yml`; chưa chạy upstream |
| Khoảng trống lấp | Bảo mật chuỗi cung ứng CI/CD: khóa phụ thuộc trực tiếp và bắc cầu của GitHub Actions vào commit đã xác minh |
| Cơ chế đáng học | - Tiện ích mở rộng `gh`; ghi `.github/workflows/actions.lock` (YAML: workflows liệt kê `uses`, `dependencies` ghi `ref`, `commit` sha1, `owner_id`, `repo_id` và danh sách `uses` bắc cầu), nên `uses:` vẫn có thể là tag.<br>- `internal/resolve/ancestry.go`: kiểm commit đã khóa có phải tổ tiên của commit sống bằng Compare API; không phải thì coi là có thể giả mạo lockfile; ba trạng thái confirmed, not-ancestor, unknown (lỗi tạm thời không bị coi là pass).<br>- Chế độ `--verify` (chỉ đọc, dùng trong CI) và `--verify-local` (ngoại tuyến, chỉ kiểm có phủ), `--relock` để đẩy ref trôi, `--fail-on-warning`.<br>- `internal/config/cooldown.go` đọc khối cooldown của Dependabot cho github-actions và cảnh báo các khóa semver không được hỗ trợ. |
| Tiêu chí và cách kiểm | Kiểm bằng máy: `--verify` thoát khác 0 khi lockfile lệch hoặc pin không còn xác minh được; repo tự dùng `verify-lockfile.yml` (đã mở) và `test.yml` chạy `go vet` và `go test` (đã mở phần grep các lệnh). Kết quả cần mạng và token `gh`. |
| Giới hạn và rủi ro | Giới hạn do tác giả liệt kê: không khóa reusable workflow ở repo khác (#179), không khóa image container, action cục bộ `./` phải xử lý riêng; không hỗ trợ GitHub Enterprise Server. README nhận lockfile đẩy ref trôi về commit cũ hơn không bị phát hiện. Cần `gh` đã đăng nhập; không đọc chi tiết cách runner của GitHub tự kiểm lại khi chạy job (chưa xác minh). |
| So với | harden-runner (hồ sơ có sẵn, giám sát egress lúc chạy, không khóa phụ thuộc), zizmor (lint workflow, bắt unpinned-action), renovate (nâng pin). |
| Nguồn | [README.md](https://github.com/github/gh-actions-lock/blob/d8e1ae3518e8ae47f38c291c1ebe68c10fcee346/README.md) · [LICENSE](https://github.com/github/gh-actions-lock/blob/d8e1ae3518e8ae47f38c291c1ebe68c10fcee346/LICENSE) · [actions.lock](https://github.com/github/gh-actions-lock/blob/d8e1ae3518e8ae47f38c291c1ebe68c10fcee346/.github/workflows/actions.lock) · [ancestry.go](https://github.com/github/gh-actions-lock/blob/d8e1ae3518e8ae47f38c291c1ebe68c10fcee346/internal/resolve/ancestry.go) · [cooldown.go](https://github.com/github/gh-actions-lock/blob/d8e1ae3518e8ae47f38c291c1ebe68c10fcee346/internal/config/cooldown.go) · [verify-lockfile.yml](https://github.com/github/gh-actions-lock/blob/d8e1ae3518e8ae47f38c291c1ebe68c10fcee346/.github/workflows/verify-lockfile.yml) · [test.yml](https://github.com/github/gh-actions-lock/blob/d8e1ae3518e8ae47f38c291c1ebe68c10fcee346/.github/workflows/test.yml) |

<a id="nt-guarddog"></a>

### GuardDog

| Thuộc tính | Giá trị |
|---|---|
| Repo | https://github.com/DataDog/guarddog |
| License | Apache-2.0 (LICENSE, `pyproject.toml`; NOTICE của Datadog; LICENSE-3rdparty.csv liệt kê phụ thuộc). Không có trọng số |
| Phiên bản đã đọc | `5da9538eb05b8c2710db60541ec9732557687f8b` (commit 2026-11-16) |
| Kiểm chứng | 2026-11-23; code-read; đã đọc `README.md`, `LICENSE`, `pyproject.toml`, `guarddog/analyzer/risk_engine.py`, `guarddog/sandbox.py`, `guarddog/analyzer/sourcecode/threat-process-download-exec.yar`, `evals/README.md`, `.github/workflows/nightly-evals.yml`, `.github/workflows/checks.yml`; chưa chạy upstream |
| Khoảng trống lấp | Phát hiện gói độc hại PyPI, npm, Go, Rust, RubyGems, GitHub Actions, VSCode extension trước khi cài (kiểm phụ thuộc agent kéo về) |
| Cơ chế đáng học | - Quy tắc YARA trong `guarddog/analyzer/sourcecode/*.yar` chia hai loại: capability (mã có thể làm gì) và threat (dấu hiệu đáng ngờ), có meta severity, specificity, sophistication, `mitre_tactics`, `path_include`, `max_hits`.<br>- `risk_engine.py` ghép capability với threat cùng file thành rủi ro (khác file thì hạ mức), chấm 0 đến 10 theo bốn nhân tố (mức nghiêm trọng 30%, chuỗi tấn công 20%, độ đặc hiệu 30%, tinh vi 20%) và đối chiếu pha MITRE early/mid/late; có thêm luật metadata (typosquatting, email tác giả, repo không khớp).<br>- `sandbox.py`: giải nén và quét trong sandbox kernel qua `nono-py`, luôn chặn mạng, có giới hạn thời gian giải nén 300 giây.<br>- `evals/`: đo recall trên mẫu độc hại từ bộ dữ liệu của chính Datadog và dương tính giả trên top 1000 gói PyPI/npm, báo precision, recall, F1, MCC theo ngưỡng (mặc định 5.0). |
| Tiêu chí và cách kiểm | Có kiểm bằng máy: workflow `checks.yml` chạy type-check, format, lint, test luật YARA, luật metadata và test lõi; `nightly-evals.yml` chạy eval hằng đêm trên runner lớn và đưa báo cáo lên artifact (đã mở hai workflow). Con số recall/precision cụ thể chưa đọc (chưa chạy). |
| Giới hạn và rủi ro | **Mô tả của trinh sát lệch:** phát hiện bằng YARA (yara-python), không phải Semgrep; không có AI-BOM/SBOM/VEX. Phân tích tĩnh nên bị né bằng obfuscation; kết quả là heuristic, không chứng minh gói sạch. Tải gói từ registry (cần mạng) trước khi quét; mẫu độc hại do chính Datadog tuyển chọn nên recall có thể thiên lệch. Windows chỉ hỗ trợ qua Docker; `nono-py` yêu cầu nền tảng hỗ trợ. |
| So với | safedep-vet (cùng hồ sơ lô này, quét lockfile kèm Threat Intel đám mây), osv-scanner (lỗ hổng đã biết, không bắt mã độc), openssf-scorecard, trivy, zizmor. |
| Nguồn | [README.md](https://github.com/DataDog/guarddog/blob/5da9538eb05b8c2710db60541ec9732557687f8b/README.md) · [LICENSE](https://github.com/DataDog/guarddog/blob/5da9538eb05b8c2710db60541ec9732557687f8b/LICENSE) · [pyproject.toml](https://github.com/DataDog/guarddog/blob/5da9538eb05b8c2710db60541ec9732557687f8b/pyproject.toml) · [risk_engine.py](https://github.com/DataDog/guarddog/blob/5da9538eb05b8c2710db60541ec9732557687f8b/guarddog/analyzer/risk_engine.py) · [sandbox.py](https://github.com/DataDog/guarddog/blob/5da9538eb05b8c2710db60541ec9732557687f8b/guarddog/sandbox.py) · [threat-process-download-exec.yar](https://github.com/DataDog/guarddog/blob/5da9538eb05b8c2710db60541ec9732557687f8b/guarddog/analyzer/sourcecode/threat-process-download-exec.yar) · [README.md](https://github.com/DataDog/guarddog/blob/5da9538eb05b8c2710db60541ec9732557687f8b/evals/README.md) · [nightly-evals.yml](https://github.com/DataDog/guarddog/blob/5da9538eb05b8c2710db60541ec9732557687f8b/.github/workflows/nightly-evals.yml) · [checks.yml](https://github.com/DataDog/guarddog/blob/5da9538eb05b8c2710db60541ec9732557687f8b/.github/workflows/checks.yml) |

<a id="nt-safedep-vet"></a>

### SafeDep vet

| Thuộc tính | Giá trị |
|---|---|
| Repo | https://github.com/safedep/vet |
| License | Apache-2.0 (LICENSE). Không có trọng số. Dữ liệu Threat Intel là dịch vụ SafeDep, điều khoản dịch vụ **(chưa xác minh)** |
| Phiên bản đã đọc | `49fdb4193637d35b0e0d238555e1f3d3aac8490f` (commit 2026-11-22) |
| Kiểm chứng | 2026-11-23; code-read; đã đọc `README.md`, `LICENSE`, `docs/controls.md`, `internal/analytics/analytics.go`, `internal/plugins/controls/agentconfig/suspicious.go`, `.github/workflows/false-positive.yml`, `.github/workflows/ci.yml`; chưa chạy upstream |
| Khoảng trống lấp | Quét chuỗi cung ứng cho phụ thuộc, workflow CI và cấu hình agent AI (kể cả MCP server trong config) |
| Cơ chế đáng học | - Mô hình control (`docs/controls.md`, `internal/plugins/controls/`): hơn 50 control theo họ agent-config, hidden-code, lockfile, malware, reputation, workflow, license, cooldown; mỗi finding có `control_id`, family, severity.<br>- Policy bằng CEL (`vet-policy.yml`): luật `when ... action: fail`, suppression có hạn; `--base-ref` chỉ báo phần PR thay đổi; `--fail-on high` cho mã thoát.<br>- `agentconfig/suspicious.go`: danh sách regex lệnh nguy hiểm trong config agent/editor (tải rồi pipe vào shell, base64 decode, `/dev/tcp`, đọc thư mục khóa); control riêng cho `mcp-server-added`, `agent-hook-command`.<br>- Control workflow `unpinned-action`, `impostor-commit`; tin lockfile của gh-actions-lock khi có (`trust_actions_lock`). |
| Tiêu chí và cách kiểm | Kiểm bằng máy: `ci.yml` chạy test; `false-positive.yml` quét dự án sạch ở commit cố định và fail khi có finding tấn công, chạy khi PR đổi detection, hàng tuần và thủ công, được ghi là chỉ mang tính tham khảo (đã mở đầu hai workflow). Tỷ lệ phát hiện chưa đọc. |
| Giới hạn và rủi ro | Checkout là nhánh `v2` (alpha), v1 mới là bản phát hành ổn định ở `main`, chưa đọc. **Mô tả của trinh sát chưa khớp với v2:** tìm trong `docs/cmd` và mã không thấy lệnh MCP server cho agent coding (có thể ở v1, chưa xác minh); v2 quét config MCP thay vì phục vụ MCP. Telemetry PostHog bật mặc định (`analytics.go`, tắt bằng `VET_DISABLE_TELEMETRY`); README nói gửi định danh gói (hệ sinh thái, tên, phiên bản) tới SafeDep và không gửi mã nguồn; `vet endpoint audit` có thông tin đăng nhập thì gửi kiểm kê máy (công cụ AI, MCP, đường dẫn config, tên thư mục home) lên SafeDep Cloud. Phát hiện malware phụ thuộc dịch vụ của chính hãng. |
| So với | guarddog (cùng lô, quét mã nguồn gói bằng YARA cục bộ), osv-scanner (chỉ lỗ hổng), zizmor (lint workflow sâu hơn), openssf-scorecard, gh-actions-lock (bổ sung: vet đọc lockfile của nó). |
| Nguồn | [README.md](https://github.com/safedep/vet/blob/49fdb4193637d35b0e0d238555e1f3d3aac8490f/README.md) · [LICENSE](https://github.com/safedep/vet/blob/49fdb4193637d35b0e0d238555e1f3d3aac8490f/LICENSE) · [controls.md](https://github.com/safedep/vet/blob/49fdb4193637d35b0e0d238555e1f3d3aac8490f/docs/controls.md) · [analytics.go](https://github.com/safedep/vet/blob/49fdb4193637d35b0e0d238555e1f3d3aac8490f/internal/analytics/analytics.go) · [suspicious.go](https://github.com/safedep/vet/blob/49fdb4193637d35b0e0d238555e1f3d3aac8490f/internal/plugins/controls/agentconfig/suspicious.go) · [false-positive.yml](https://github.com/safedep/vet/blob/49fdb4193637d35b0e0d238555e1f3d3aac8490f/.github/workflows/false-positive.yml) · [ci.yml](https://github.com/safedep/vet/blob/49fdb4193637d35b0e0d238555e1f3d3aac8490f/.github/workflows/ci.yml) |
