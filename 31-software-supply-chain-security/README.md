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

<a id="n2-2026-11-24"></a>

## Nâng trần đợt hai — 23/11/2026

Hồ sơ lập trong đợt nâng trần thứ hai: đọc mã hoặc tài liệu tại commit cố định, chưa chạy upstream; mô tả của trinh sát sai ở nhiều repo nên điều ghi ở đây là điều đã đọc.

<a id="n2-step-security-secure-repo"></a>

### Secure-Repo (StepSecurity)

| Thuộc tính | Giá trị |
|---|---|
| Repo | https://github.com/step-security/secure-repo |
| License | AGPL-3.0 (LICENSE) |
| Phiên bản đã đọc | `f16799fed9809f97f21efa979d4ba9c726cf8e89` (commit 2026-11-05) |
| Kiểm chứng | 2026-11-24; code-read; đã đọc LICENSE, README, main.go, permissions.go, action-security.yml của checkout và test.yml; chưa chạy upstream |
| Khoảng trống lấp | Bảo mật chuỗi cung ứng CI/CD: tự sửa workflow GitHub Actions (quyền GITHUB_TOKEN tối thiểu, ghim SHA, thêm Harden-Runner) |
| Cơ chế đáng học | - Cơ sở tri thức theo từng action (`knowledge-base/actions/<owner>/<action>/action-security.yml`, hơn 1000 mục): ghi quyền token cần (kèm lý do) và endpoint ra ngoài; công cụ cộng quyền của mọi step để ra `permissions` tối thiểu (`remediation/workflow/permissions/permissions.go`).<br>- Từ chối sửa khi không chắc: các mã KnownIssue-1..8 (step `run` dùng token, action cục bộ, action thiếu trong kho tri thức, docker action, reusable workflow, job đã có permissions).<br>- Các bộ sửa tách thư mục: `pin` (ghim action và ảnh Docker theo digest), `hardenrunner`, `dependabot`, `permissions`, `maintainedactions`, `runnerlabel`; thêm CodeQL, dependency review, Scorecard từ `workflow-templates`.<br>- Tự áp dụng cho chính mình: workflow `test.yml` có `permissions` tối thiểu, Harden-Runner với allowed-endpoints và action ghim SHA. |
| Tiêu chí và cách kiểm | CI `test.yml` đã mở: chạy test Go (Go 1.27.3) với Harden-Runner; có workflow kb-test, kbanalysis, scorecards, codeql (chưa mở). Nhiều bộ sửa có file `_test.go` cạnh (permissions, pin, hardenrunner...). Kiểm bằng máy ở mức test đơn vị với workflow mẫu trong `testfiles/`. |
| Giới hạn và rủi ro | AGPL-3.0, nên chạy hộ dịch vụ cho người khác kích hoạt nghĩa vụ công bố mã. Dạng sản phẩm là dịch vụ AWS Lambda (`main.go` dùng `lambda.StartHandler`), dùng chủ yếu qua bản host app.stepsecurity.io (README: đăng nhập GitHub, không cần cài app); tự host cần CloudFormation ở tài khoản AWS. Dùng PAT cho workflow tạo PR (`automatePR.yml`). Độ phủ phụ thuộc kho tri thức, action ngoài kho thì bị bỏ qua. Không phải CLI chạy cục bộ nhẹ nhàng như tên gợi ý. |
| So với | Harden-Runner (cùng hãng, bổ trợ: một bên sửa tĩnh, một bên giám sát runtime), zizmor, actionlint, OpenSSF Scorecard, gh-actions-lock. |
| Nguồn | [LICENSE](https://github.com/step-security/secure-repo/blob/f16799fed9809f97f21efa979d4ba9c726cf8e89/LICENSE) · [README.md](https://github.com/step-security/secure-repo/blob/f16799fed9809f97f21efa979d4ba9c726cf8e89/README.md) · [main.go](https://github.com/step-security/secure-repo/blob/f16799fed9809f97f21efa979d4ba9c726cf8e89/main.go) · [remediation/workflow/permissions/permissions.go](https://github.com/step-security/secure-repo/blob/f16799fed9809f97f21efa979d4ba9c726cf8e89/remediation/workflow/permissions/permissions.go) · [knowledge-base/actions/actions/checkout/action-security.yml](https://github.com/step-security/secure-repo/blob/f16799fed9809f97f21efa979d4ba9c726cf8e89/knowledge-base/actions/actions/checkout/action-security.yml) · [.github/workflows/test.yml](https://github.com/step-security/secure-repo/blob/f16799fed9809f97f21efa979d4ba9c726cf8e89/.github/workflows/test.yml) |

<a id="n2-cicd-sensor"></a>

### cicd-sensor

| Thuộc tính | Giá trị |
|---|---|
| Repo | https://github.com/cicd-sensor/cicd-sensor |
| License | Apache-2.0 (LICENSE) |
| Phiên bản đã đọc | `932bdc4c4886b001f31be4587b81f0480104fe38` (commit 2026-11-18) |
| Kiểm chứng | 2026-11-24; code-read; đã đọc LICENSE, README, rules/README.md, hai file luật, redaction.go, ci.yaml và ba trang user-guide; chưa chạy upstream |
| Khoảng trống lấp | Bảo mật chuỗi cung ứng CI/CD: cảm biến eBPF runtime (kiểu EDR) cho GitHub Actions và GitLab CI |
| Cơ chế đáng học | - Phát hiện theo tổ tiên tiến trình và tương quan tín hiệu, ví dụ đọc thông tin xác thực từ tiến trình con của `npm install`; luật khai báo YAML với điều kiện CEL (`rules/*.yaml`, `docs/user-guide/rule-cel-conditions.md`).<br>- Nhóm luật gốc theo giai đoạn tấn công (credential-access, execution, exfiltration, persistence, tracking-escape, ioc) kèm mô tả What/Why/Notes và thừa nhận giới hạn (ví dụ luật DNS Telegram không chứng minh có upload).<br>- Hành động mỗi luật là `detect`, `collect` hoặc `terminate`, đổi bằng `override_action`; `monitor_mode` hạ `terminate` xuống `detect` (`docs/user-guide/rule-modifiers.md`).<br>- Che dữ liệu nhạy cảm trong argv (`internal/jobevent/redaction.go`: cờ và chuỗi như token, secret, ghp_) trước khi ghi log; bộ luật gốc phát hành dạng OCI có chữ ký Sigstore và bị chặn nếu không qua validate (`rules/README.md`, `manager.md`). |
| Tiêu chí và cách kiểm | CI `ci.yaml` đã mở: gofmt, `go vet`, `make test` với action ghim SHA; có `make rules-test`, `rules-validate`, `rules-bundle-validate` và test cho luật (`rules/*_test.go`) chạy trước khi phát hành bundle luật. Có workflow thử trên nhiều kernel (`bpf-cross-kernel.yaml`, chưa mở). |
| Giới hạn và rủi ro | README tự ghi "Pre-release: Active development" (bản action v0.0.41). Cần kernel 5.15+ (amd64) hoặc 6.1+ (arm64) có BTF và fentry; không chạy trên `ubuntu-slim` và một số runner của bên thứ ba (docs github-hosted). Mặc định tải báo cáo HTML và attestation lên artifact của job; xuất log ra S3/GCS/Azure/Pub/Sub qua Manager tự host, còn trỏ tới Manager của bên thứ ba (ví dụ Takumi Runner) thì log rời sang bên đó (README nêu rõ). Chặn mạng chỉ "một phần" (kill tiến trình, dừng job), không phải tường lửa; bảng so sánh với Harden-Runner là tuyên bố của tác giả (chưa xác minh, dữ liệu 05/2026). Clone nông nên không đánh giá được lịch sử. |
| So với | Harden-Runner (egress allowlist, bản miễn phí là SaaS), Falco (runtime chung, không riêng CI), OpenSSF Scorecard (tĩnh, không phải runtime). |
| Nguồn | [LICENSE](https://github.com/cicd-sensor/cicd-sensor/blob/932bdc4c4886b001f31be4587b81f0480104fe38/LICENSE) · [README.md](https://github.com/cicd-sensor/cicd-sensor/blob/932bdc4c4886b001f31be4587b81f0480104fe38/README.md) · [rules/README.md](https://github.com/cicd-sensor/cicd-sensor/blob/932bdc4c4886b001f31be4587b81f0480104fe38/rules/README.md) · [rules/generic-credential-access.yaml](https://github.com/cicd-sensor/cicd-sensor/blob/932bdc4c4886b001f31be4587b81f0480104fe38/rules/generic-credential-access.yaml) · [rules/generic-exfiltration.yaml](https://github.com/cicd-sensor/cicd-sensor/blob/932bdc4c4886b001f31be4587b81f0480104fe38/rules/generic-exfiltration.yaml) · [internal/jobevent/redaction.go](https://github.com/cicd-sensor/cicd-sensor/blob/932bdc4c4886b001f31be4587b81f0480104fe38/internal/jobevent/redaction.go) · [.github/workflows/ci.yaml](https://github.com/cicd-sensor/cicd-sensor/blob/932bdc4c4886b001f31be4587b81f0480104fe38/.github/workflows/ci.yaml) · [docs/user-guide/github-hosted.md](https://github.com/cicd-sensor/cicd-sensor/blob/932bdc4c4886b001f31be4587b81f0480104fe38/docs/user-guide/github-hosted.md) · [docs/user-guide/manager.md](https://github.com/cicd-sensor/cicd-sensor/blob/932bdc4c4886b001f31be4587b81f0480104fe38/docs/user-guide/manager.md) · [docs/user-guide/rule-modifiers.md](https://github.com/cicd-sensor/cicd-sensor/blob/932bdc4c4886b001f31be4587b81f0480104fe38/docs/user-guide/rule-modifiers.md) |

<a id="n2-zanadir"></a>

### zanadir

| Thuộc tính | Giá trị |
|---|---|
| Repo | https://github.com/MustacheCase/zanadir |
| License | MIT (LICENSE, © MustacheCase) |
| Phiên bản đã đọc | `5cd1565070c9160433532084c74b6092c93ced67` (commit 2026-11-23) |
| Kiểm chứng | 2026-11-24; code-read; đã đọc LICENSE, README, grading.go, hai file test grading và TestAndBuild.yml; chưa chạy upstream |
| Khoảng trống lấp | Bảo mật chuỗi cung ứng CI/CD: đọc pipeline, báo kiểm tra bảo mật còn thiếu hoặc không thể chặn build |
| Cơ chế đáng học | - Chấm từng nhóm kiểm soát (13 nhóm) thành `enforcing`, `partial`, `advisory`, `unknown` thay vì chỉ "có/không" (`grading/grading.go`): scanner có `continue-on-error`, lệnh nuốt lỗi bằng toán tử OR của shell kèm `true`, chỉ chạy khi push, hoặc `trivy` không có `--exit-code 1` bị xếp advisory.<br>- Kiểm tra trigger có chặn thay đổi thật không (`gradeTriggers`, `coversDefaultBranch`) và với `--required-checks` chỉ tính enforcing khi branch protection bắt buộc check đó.<br>- Đọc 6 hệ CI (GitHub Actions, GitLab CI, CircleCI, Bitbucket, Azure Pipelines, Jenkins) từ thư mục hoặc từ GitHub (`--repo`); xuất table, JSON, SARIF, Markdown; `zanadir fix` in cấu hình gợi ý.<br>- Test đầu-cuối theo từng hệ CI với pipeline mẫu và kết quả mong đợi (`grading/github_test.go`, `azure_test.go`), gồm cả ca "cờ của lệnh bên cạnh không làm mạnh/yếu". |
| Tiêu chí và cách kiểm | Cổng CLI: `--fail-on` (nhóm thiếu công cụ) và `--fail-on-weakened` (nhóm bị làm yếu) trả mã lỗi để chặn PR (README). CI `TestAndBuild.yml` đã mở, có Codecov; có workflow tự quét mình (ZanadirScan, SBOM, Scorecard, SecretsScan... chưa mở). Kiểm bằng máy là test đơn vị; độ chính xác ngoài các mẫu test chưa xác minh. |
| Giới hạn và rủi ro | MIT, bản phát hành có attestation và checksum (README, chưa xác minh bản phát hành thật). Việc phát hiện dựa trên danh mục tên công cụ và quy tắc cờ nên ca lạ (script tự viết, wrapper) có thể ra `unknown` hoặc sai; cảnh báo "covered" hay "weakened" là suy luận tĩnh, không chứng minh scanner chạy được. Chế độ `--repo` gọi api.github.com. Số liệu "State of CI security 2026" trong README là tuyên bố tác giả (chưa xác minh). Có cả plugin, MCP server, bản WebAssembly (chưa mở). |
| So với | OpenSSF Scorecard, zizmor, actionlint, Harden-Runner. Khác Scorecard ở chỗ chấm hiệu lực chặn build, không chỉ sự hiện diện. |
| Nguồn | [LICENSE](https://github.com/MustacheCase/zanadir/blob/5cd1565070c9160433532084c74b6092c93ced67/LICENSE) · [README.md](https://github.com/MustacheCase/zanadir/blob/5cd1565070c9160433532084c74b6092c93ced67/README.md) · [grading/grading.go](https://github.com/MustacheCase/zanadir/blob/5cd1565070c9160433532084c74b6092c93ced67/grading/grading.go) · [grading/azure_test.go](https://github.com/MustacheCase/zanadir/blob/5cd1565070c9160433532084c74b6092c93ced67/grading/azure_test.go) · [grading/github_test.go](https://github.com/MustacheCase/zanadir/blob/5cd1565070c9160433532084c74b6092c93ced67/grading/github_test.go) · [.github/workflows/TestAndBuild.yml](https://github.com/MustacheCase/zanadir/blob/5cd1565070c9160433532084c74b6092c93ced67/.github/workflows/TestAndBuild.yml) |

<a id="n2-shai-hulud-2-detector"></a>

### Shai-Hulud 2.0 Detector

| Thuộc tính | Giá trị |
|---|---|
| Repo | https://github.com/gensecaihq/Shai-Hulud-2.0-Detector |
| License | MIT (LICENSE, © gensecaihq) |
| Phiên bản đã đọc | `d96885a17a1b9ce40bb669c6fa34bbdf75fe2c17` (commit 2026-08-09) |
| Kiểm chứng | 2026-11-24; code-read; đã đọc LICENSE, README, action.yml, compromised-packages.json, src/scanner.ts, ci.yml và update-ioc-database.yml; chưa chạy upstream |
| Khoảng trống lấp | Bảo mật chuỗi cung ứng CI/CD: ví dụ ứng phó sự cố worm npm (Shai-Hulud 2.0 và ChainDrop) bằng IOC tĩnh |
| Cơ chế đáng học | - GitHub Action và CLI quét lockfile, `node_modules`, script vòng đời và workflow để tìm gói trong danh sách thỏa hiệp (`compromised-packages.json`: 1241 gói kèm phiên bản bị ảnh hưởng và mức nghiêm trọng) và IOC tệp/băm.<br>- Phân mức theo ngữ cảnh: script `preinstall` có `curl`/`wget`/`fetch` hoặc `node setup.mjs` là critical, ngoài hook vòng đời là high (`src/scanner.ts` quanh dòng 1300); kèm sha256 nội dung làm bằng chứng.<br>- Cổng thất bại cấu hình được: `fail-on-critical` (mặc định true), `fail-on-high`, `fail-on-any`; xuất text, JSON hoặc SARIF; allowlist chống báo nhầm (`action.yml`).<br>- Danh sách IOC gom từ nhiều nguồn (DataDog, Wiz, Socket, StepSecurity, Koi...) và workflow `update-ioc-database.yml` chạy hằng ngày. |
| Tiêu chí và cách kiểm | CI đã mở: build, kiểm dist, chạy chính action trên mẫu. Có vitest (`scanner.pnpm.test.ts`, chưa chạy). Phần kiểm `dist` chỉ cảnh báo, không chặn khi `dist/index.js` lệch nguồn. |
| Giới hạn và rủi ro | Trinh sát ghi pushed 2026-11-23 nhưng commit trên nhánh mặc định là 2026-08-09 và `lastUpdated` của danh sách IOC cũng 2026-08-09, dù workflow cập nhật hằng ngày: dữ liệu IOC có thể đã cũ so với hôm nay (2026-11-24); chưa xác minh nhánh khác. Phát hiện chỉ theo danh sách tĩnh và regex nên không bắt được biến thể mới; phạm vi tuyên bố "protect" quá rộng. Tác giả (gensecaihq) là tổ chức nhỏ, độ tin cậy dữ liệu cộng đồng phụ thuộc báo cáo gói (README tự nói). Repo commit cả `dist/` đã build, người dùng khó kiểm bản build. Không thấy telemetry trong phần đã đọc. |
| So với | OSV-Scanner, GUAC, Gitleaks. OSV-Scanner dùng cơ sở dữ liệu lỗ hổng công khai và cập nhật liên tục; repo này là bộ IOC theo một chiến dịch. |
| Nguồn | [LICENSE](https://github.com/gensecaihq/Shai-Hulud-2.0-Detector/blob/d96885a17a1b9ce40bb669c6fa34bbdf75fe2c17/LICENSE) · [README.md](https://github.com/gensecaihq/Shai-Hulud-2.0-Detector/blob/d96885a17a1b9ce40bb669c6fa34bbdf75fe2c17/README.md) · [action.yml](https://github.com/gensecaihq/Shai-Hulud-2.0-Detector/blob/d96885a17a1b9ce40bb669c6fa34bbdf75fe2c17/action.yml) · [compromised-packages.json](https://github.com/gensecaihq/Shai-Hulud-2.0-Detector/blob/d96885a17a1b9ce40bb669c6fa34bbdf75fe2c17/compromised-packages.json) · [src/scanner.ts](https://github.com/gensecaihq/Shai-Hulud-2.0-Detector/blob/d96885a17a1b9ce40bb669c6fa34bbdf75fe2c17/src/scanner.ts) · [.github/workflows/ci.yml](https://github.com/gensecaihq/Shai-Hulud-2.0-Detector/blob/d96885a17a1b9ce40bb669c6fa34bbdf75fe2c17/.github/workflows/ci.yml) · [.github/workflows/update-ioc-database.yml](https://github.com/gensecaihq/Shai-Hulud-2.0-Detector/blob/d96885a17a1b9ce40bb669c6fa34bbdf75fe2c17/.github/workflows/update-ioc-database.yml) |

<a id="n2-checkov"></a>

### Checkov

| Thuộc tính | Giá trị |
|---|---|
| Repo | https://github.com/bridgecrewio/checkov |
| License | Apache-2.0 |
| Phiên bản đã đọc | `2f107f8613830f773b23fa21104b7ac2885c2581` (commit 2026-11-23) |
| Kiểm chứng | 2026-11-24; code-read; đã đọc README, LICENSE, version.py, AMICopyIsEncrypted.py, ACMWildcardDomainName.yaml, ext_argument_parser.py, pr-test.yml; chưa chạy upstream |
| Khoảng trống lấp | SAST/DAST/IaC scan |
| Cơ chế đáng học | - Check theo resource là lớp Python: `BaseResourceValueCheck` với `id` (CKV_AWS_235), `supported_resources`, `get_inspected_key` — `terraform/checks/resource/aws/AMICopyIsEncrypted.py`; thư mục aws có 366 file.<br>- Check đồ thị khai báo YAML (`graph_checks/aws/ACMWildcardDomainName.yaml`, CKV2_AWS_71) với `cond_type`, `operator` (`not_contains`, `not_exists`) và `and`/`or`, cho quan hệ giữa nhiều resource.<br>- Cờ điều khiển cổng: `--check`, `--skip-check`, `--soft-fail`, `--hard-fail-on` theo mức độ, `--external-checks-dir` cho check tuỳ biến — `common/util/ext_argument_parser.py`. |
| Tiêu chí và cách kiểm | Mã thoát do cờ soft-fail/hard-fail-on (đọc mô tả cờ, chưa chạy); `main.py` gộp mã thoát nhiều runner. CI PR: pre-commit, danger, cfn-lint; đã mở một phần `pr-test.yml`, chưa mở workflow build/coverage. Độ chính xác (dương tính giả) của từng check chưa xác minh. |
| Giới hạn và rủi ro | Apache-2.0. `--external-checks-dir` chạy mã Python từ thư mục chỉ định (mô tả cờ cảnh báo), nên không dùng với thư mục không tin cậy. Truyền API key Prisma Cloud thì kết quả có thể rời máy (chưa xác minh luồng); `--skip-download` bỏ tải dữ liệu. Phiên bản 3.4.7. README có quảng bá sản phẩm thương mại cùng nhà. Kích thước rất lớn nên khó audit toàn bộ. |
| So với | opa-conftest (policy Rego), zizmor (riêng GitHub Actions), trivy (có quét misconfig) |
| Nguồn | [README.md](https://github.com/bridgecrewio/checkov/blob/2f107f8613830f773b23fa21104b7ac2885c2581/README.md) · [LICENSE](https://github.com/bridgecrewio/checkov/blob/2f107f8613830f773b23fa21104b7ac2885c2581/LICENSE) · [version.py](https://github.com/bridgecrewio/checkov/blob/2f107f8613830f773b23fa21104b7ac2885c2581/checkov/version.py) · [AMICopyIsEncrypted.py](https://github.com/bridgecrewio/checkov/blob/2f107f8613830f773b23fa21104b7ac2885c2581/checkov/terraform/checks/resource/aws/AMICopyIsEncrypted.py) · [ACMWildcardDomainName.yaml](https://github.com/bridgecrewio/checkov/blob/2f107f8613830f773b23fa21104b7ac2885c2581/checkov/terraform/checks/graph_checks/aws/ACMWildcardDomainName.yaml) · [ext_argument_parser.py](https://github.com/bridgecrewio/checkov/blob/2f107f8613830f773b23fa21104b7ac2885c2581/checkov/common/util/ext_argument_parser.py) · [pr-test.yml](https://github.com/bridgecrewio/checkov/blob/2f107f8613830f773b23fa21104b7ac2885c2581/.github/workflows/pr-test.yml) |

<a id="n2-cdxgen"></a>

### cdxgen (CycloneDX Generator)

| Thuộc tính | Giá trị |
|---|---|
| Repo | https://github.com/cdxgen/cdxgen |
| License | Apache-2.0 |
| Phiên bản đã đọc | `fdb08696f73dc5e344cfb39409ed0ecfbd72ff1e` (commit 2026-11-24) |
| Kiểm chứng | 2026-11-24; code-read; đã đọc README, LICENSE, SECURITY.md, AI-DECLARATION.md, SKILL.md, PERMISSIONS.md, aiCollector.js, package.json, nodejs.yml; chưa chạy upstream |
| Khoảng trống lấp | Chuỗi cung ứng AI: AI-BOM/SBOM/VEX |
| Cơ chế đáng học | - `--dry-run` chỉ đọc: chặn ghi, tiến trình con, thư mục tạm, clone, nộp từ xa và in bảng hoạt động; `cdxgen-secure` đặt cài phụ thuộc luôn tắt (`bin/cdxgen-secure.js`, `docs/PERMISSIONS.md`).<br>- `lib/inventory/aiCollector.js` (kèm `aiInventory.js`, `aiModelVariants.js`, `parsers/gguf.js`, `onnx.js`, `safetensors.js`) đọc metadata mô hình có giới hạn (`boundedFile.js`) và làm sạch URL/thuộc tính trước khi đưa vào BOM (`propertySanitizer.js`).<br>- `SKILL.md` và `agent-plugin/` đóng gói cách agent gọi cdxgen với cờ an toàn (dry-run trước, không tự cài). |
| Tiêu chí và cách kiểm | Mã thoát không đọc cụ thể. CI `nodejs.yml` chạy quick-tests, golden-tests, unit-tests là check bắt buộc trên nhánh chính; test dùng khung `poku` (nhiều file `*.poku.js`). Chất lượng phát hiện AI-BOM chưa kiểm trên mẫu thật. |
| Giới hạn và rủi ro | Apache-2.0. Khi không ở secure mode, cdxgen có thể chạy mvn, gradle, npm install... của dự án quét, tức thực thi mã dự án (SECURITY.md coi là hành vi mong đợi nếu cho phép). `AI-DECLARATION.md` ghi: từ 04/2026 phần lớn thay đổi do AI viết, hợp nhất tự động khi check qua, chỉ thay đổi rủi ro cao do người rà. Dự án rất lớn nên khó audit đầy đủ. Telemetry: không thấy trong phần đã đọc (chưa xác minh toàn repo). |
| So với | syft (SBOM đã có), microsoft-sbom-tool, trivy; cisco-aibom và vexctl (cùng lô) |
| Nguồn | [README.md](https://github.com/cdxgen/cdxgen/blob/fdb08696f73dc5e344cfb39409ed0ecfbd72ff1e/README.md) · [LICENSE](https://github.com/cdxgen/cdxgen/blob/fdb08696f73dc5e344cfb39409ed0ecfbd72ff1e/LICENSE) · [SECURITY.md](https://github.com/cdxgen/cdxgen/blob/fdb08696f73dc5e344cfb39409ed0ecfbd72ff1e/SECURITY.md) · [AI-DECLARATION.md](https://github.com/cdxgen/cdxgen/blob/fdb08696f73dc5e344cfb39409ed0ecfbd72ff1e/AI-DECLARATION.md) · [SKILL.md](https://github.com/cdxgen/cdxgen/blob/fdb08696f73dc5e344cfb39409ed0ecfbd72ff1e/SKILL.md) · [PERMISSIONS.md](https://github.com/cdxgen/cdxgen/blob/fdb08696f73dc5e344cfb39409ed0ecfbd72ff1e/docs/PERMISSIONS.md) · [aiCollector.js](https://github.com/cdxgen/cdxgen/blob/fdb08696f73dc5e344cfb39409ed0ecfbd72ff1e/lib/inventory/aiCollector.js) · [package.json](https://github.com/cdxgen/cdxgen/blob/fdb08696f73dc5e344cfb39409ed0ecfbd72ff1e/package.json) · [nodejs.yml](https://github.com/cdxgen/cdxgen/blob/fdb08696f73dc5e344cfb39409ed0ecfbd72ff1e/.github/workflows/nodejs.yml) |

<a id="n2-cisco-aibom"></a>

### Cisco AI BOM

| Thuộc tính | Giá trị |
|---|---|
| Repo | https://github.com/cisco-ai-defense/aibom |
| License | Apache-2.0 |
| Phiên bản đã đọc | `93ea541da490cc81394efa536fec9ab4de5c3e1e` (commit 2026-11-04) |
| Kiểm chứng | 2026-11-24; code-read; đã đọc README, LICENSE, policy.py, pyproject.toml, unit-tests.yml; chưa chạy upstream |
| Khoảng trống lấp | Chuỗi cung ứng AI: AI-BOM/SBOM/VEX |
| Cơ chế đáng học | - `aibom/src/aibom/policy.py`: bảy luật (`no_hardcoded_keys`, `require_pinned_models`, `max_risk_score`, `blocked_models`, `require_guardrail_for`, `require_observability_for`, `max_unresolved_agentic`), mức `severity` và `fail_on`; vi phạm đạt ngưỡng thì trượt.<br>- Phát hiện ba tầng: AST bằng LibCST cho Python, tree-sitter cho ngôn ngữ khác, rồi agent LLM (LangChain/Deep Agents) loại dương tính giả (README, `agentic/`).<br>- Tích hợp ngoài tuỳ chọn: tra OSV.dev cho CVE phụ thuộc, POST báo cáo (`report_sender.py`, `--post-url`), telemetry Galileo (opt-in) cho chất lượng agent. |
| Tiêu chí và cách kiểm | Policy: README nói exit code 1 khi trượt; code `load_policy` chỉ nhận các khoá luật nêu trên. Theo mã đọc, ví dụ README (`required_fields`, `blocked_types`, `required_types`, và `rules` kiểu `name/field/operator`) không khớp: khoá lạ bị bỏ qua ở dạng phẳng, còn mục `rules` thiếu `rule` sẽ ném ValueError (chưa chạy). CI chạy `pytest` ma trận Python 3.11 đến 3.13; có 103 mục trong `aibom/tests` (chưa chạy). |
| Giới hạn và rủi ro | Apache-2.0 (header Cisco 2026). Dùng chế độ agentic thì mã/đoạn phát hiện gửi tới nhà cung cấp LLM bạn chọn (khoá `--llm-api-key`); OSV.dev nhận tên và phiên bản phụ thuộc; `--post-url` gửi cả báo cáo. 119 sao, cộng đồng nhỏ, phiên bản 1.10.1. Phát hiện phi-Python yếu hơn (README tự nói). Một số tính năng gắn dịch vụ Cisco AI Defense (khoá API riêng). |
| So với | skill-scanner-cisco và cisco-mcp-scanner (cùng tổ chức), cdxgen (AI-BOM trong BOM chuẩn) |
| Nguồn | [README.md](https://github.com/cisco-ai-defense/aibom/blob/93ea541da490cc81394efa536fec9ab4de5c3e1e/README.md) · [LICENSE](https://github.com/cisco-ai-defense/aibom/blob/93ea541da490cc81394efa536fec9ab4de5c3e1e/LICENSE) · [policy.py](https://github.com/cisco-ai-defense/aibom/blob/93ea541da490cc81394efa536fec9ab4de5c3e1e/aibom/src/aibom/policy.py) · [pyproject.toml](https://github.com/cisco-ai-defense/aibom/blob/93ea541da490cc81394efa536fec9ab4de5c3e1e/aibom/pyproject.toml) · [unit-tests.yml](https://github.com/cisco-ai-defense/aibom/blob/93ea541da490cc81394efa536fec9ab4de5c3e1e/.github/workflows/unit-tests.yml) |

<a id="n2-vexctl"></a>

### vexctl

| Thuộc tính | Giá trị |
|---|---|
| Repo | https://github.com/openvex/vexctl |
| License | Apache-2.0 |
| Phiên bản đã đọc | `fefc350c2da2523caa7361cc3c43a064b6ddeee5` (commit 2026-11-23) |
| Kiểm chứng | 2026-11-24; code-read; đã đọc README, LICENSE, go.mod, ctl.go, implementation.go, filter.go, ci-build-test.yaml; chưa chạy upstream |
| Khoảng trống lấp | Chuỗi cung ứng AI: AI-BOM/SBOM/VEX |
| Cơ chế đáng học | - `ApplySingleVEX` (`pkg/ctl/implementation.go`) sắp xếp statement theo thời gian, lập chỉ mục theo mã lỗ hổng (CVE, GHSA, RUSTSEC, RHSA, SNYK, PRISMA, GO) và xoá kết quả SARIF có statement `not_affected` hoặc `fixed`.<br>- `vexctl filter` nhận SARIF (hoặc stdin `-`) và VEX/CSAF/CycloneDX, có tuỳ chọn `--product` cho CSAF — `internal/cmd/filter.go`.<br>- `vexctl validate` kiểm tài liệu OpenVEX, thoát khác 0 nếu có lỗi (README); `attest` ký bằng sigstore; binary phát hành có sigstore bundle để xác minh bằng cosign. |
| Tiêu chí và cách kiểm | Có test Go (`*_test.go`) và CI build/test cho PR, action ghim theo SHA; mã thoát `validate` theo README. Chưa xác minh phủ test của logic lọc. |
| Giới hạn và rủi ro | Apache-2.0. Theo `ApplySingleVEX` (đọc mã), kết quả bị loại chỉ dựa vào mã lỗ hổng và trạng thái, không so sản phẩm với SARIF, nên VEX viết cho sản phẩm khác có thể làm biến mất cảnh báo thật; tài liệu VEX phải được tin cậy và kiểm nguồn (chưa chạy để xác nhận). Chỉ lọc kết quả SARIF dạng CVE/GHSA...; phụ thuộc go-vex bản pre-release. Không thấy telemetry. Số sao 222 là của trinh sát. |
| So với | grype và trivy (nguồn cảnh báo cần lọc), syft và cdxgen (sinh SBOM) |
| Nguồn | [README.md](https://github.com/openvex/vexctl/blob/fefc350c2da2523caa7361cc3c43a064b6ddeee5/README.md) · [LICENSE](https://github.com/openvex/vexctl/blob/fefc350c2da2523caa7361cc3c43a064b6ddeee5/LICENSE) · [go.mod](https://github.com/openvex/vexctl/blob/fefc350c2da2523caa7361cc3c43a064b6ddeee5/go.mod) · [ctl.go](https://github.com/openvex/vexctl/blob/fefc350c2da2523caa7361cc3c43a064b6ddeee5/pkg/ctl/ctl.go) · [implementation.go](https://github.com/openvex/vexctl/blob/fefc350c2da2523caa7361cc3c43a064b6ddeee5/pkg/ctl/implementation.go) · [filter.go](https://github.com/openvex/vexctl/blob/fefc350c2da2523caa7361cc3c43a064b6ddeee5/internal/cmd/filter.go) · [ci-build-test.yaml](https://github.com/openvex/vexctl/blob/fefc350c2da2523caa7361cc3c43a064b6ddeee5/.github/workflows/ci-build-test.yaml) |

<a id="n2-openvex-spec"></a>

### OpenVEX Specification

| Thuộc tính | Giá trị |
|---|---|
| Repo | https://github.com/openvex/spec |
| License | CC0-1.0 (LICENSE); governance/4._License.md nêu Community Specification License 1.0 cho đặc tả |
| Phiên bản đã đọc | `93139bd2c65390b504e47f82f11c50451289f93a` (commit 2026-10-30) |
| Kiểm chứng | 2026-11-24; docs-read; đã đọc README.md, LICENSE, OPENVEX-SPEC.md, openvex_json_schema.json, governance/4._License.md, ATTESTING.md (đầu file); chưa chạy upstream |
| Khoảng trống lấp | Chuỗi cung ứng AI: AI-BOM/SBOM/VEX (định dạng VEX tách khỏi SBOM) |
| Cơ chế đáng học | - Statement gồm vulnerability, products, status (`not_affected`, `affected`, `fixed`, `under_investigation`) và nhãn justification cố định cho `not_affected` (OPENVEX-SPEC.md §Status Justifications: 5 nhãn như `component_not_present`, `vulnerable_code_not_in_execute_path`).<br>- `openvex_json_schema.json` (draft 2020-12) mã hóa luật bằng if/then: `not_affected` buộc có `justification` hoặc `impact_statement`, `affected` buộc có `action_statement`; document bắt buộc `@context`, `@id`, `author`, `timestamp`, `version`, `statements`.<br>- Quy tắc kế thừa dữ liệu khi VEX nhúng trong tài liệu khác (§Data Inheritance) và hướng nhúng vào attestation in-toto (ATTESTING.md): mẫu để gắn VEX vào chuỗi bằng chứng. |
| Tiêu chí và cách kiểm | Kiểm bằng máy được qua JSON Schema (vi phạm if/then bị từ chối); repo không có test hay CI (không có thư mục .github). Phần dùng làm cổng VEX phải do dự án đích tự viết trên schema này. |
| Giới hạn và rủi ro | Đặc tả vẫn ghi là draft (README), v0.2.0; không có thư viện trong repo này (thư viện Go nằm repo khác, chưa đọc). Licence không đồng nhất: LICENSE là CC0-1.0 nhưng governance nói đặc tả theo Community Specification License 1.0 và khi xung đột thì license đó thắng; cần đối chiếu trước khi trích nguyên văn. Nhãn justification dễ bị lạm dụng, chính spec thừa nhận vài nhãn khó chứng minh. |
| So với | `cosign`, `slsa` (cùng họ chứng thực chuỗi cung ứng, nhưng không có định dạng VEX); `owasp-dependency-track` và `grype` là bên tiêu thụ VEX; `microsoft-sbom-tool` (SBOM, không phải VEX). |
| Nguồn | [README](https://github.com/openvex/spec/blob/93139bd2c65390b504e47f82f11c50451289f93a/README.md) · [LICENSE](https://github.com/openvex/spec/blob/93139bd2c65390b504e47f82f11c50451289f93a/LICENSE) · [OPENVEX-SPEC.md](https://github.com/openvex/spec/blob/93139bd2c65390b504e47f82f11c50451289f93a/OPENVEX-SPEC.md) · [JSON Schema](https://github.com/openvex/spec/blob/93139bd2c65390b504e47f82f11c50451289f93a/openvex_json_schema.json) · [governance/4._License.md](https://github.com/openvex/spec/blob/93139bd2c65390b504e47f82f11c50451289f93a/governance/4._License.md) · [ATTESTING.md](https://github.com/openvex/spec/blob/93139bd2c65390b504e47f82f11c50451289f93a/ATTESTING.md) |

<a id="n2-sbomqs"></a>

### sbomqs

| Thuộc tính | Giá trị |
|---|---|
| Repo | https://github.com/interlynk-io/sbomqs |
| License | Apache-2.0 |
| Phiên bản đã đọc | `613d55c2db5a3d4d12f74a2a6d582299d996dd24` (commit 2026-11-23) |
| Kiểm chứng | 2026-11-24; code-read; đã đọc README.md, LICENSE, docs/guides/policy.md, docs/commands/score.md, docs/reference/quality-checks.md, pkg/scorer/ntia.go, pkg/share/share.go, cmd/policy.go, Makefile (target test/ci), .github/workflows/ci.yml (đoạn đầu); chưa chạy upstream |
| Khoảng trống lấp | Chuỗi cung ứng AI: AI-BOM/SBOM/VEX (chấm điểm chất lượng SBOM) |
| Cơ chế đáng học | - `sbomqs score` chấm 0-10 theo nhóm kiểm (NTIA, Structural, Semantic, Quality, Sharing, BSI); mỗi kiểm là hàm đếm tỷ lệ thành phần đạt, ví dụ `compWithSupplierCheck` trong `pkg/scorer/ntia.go` trả `đếm có supplier / tổng * 10` và đánh dấu bỏ qua khi không có thành phần.<br>- `sbomqs compliance` đối chiếu theo chuẩn (BSI TR-03183-2 v1.1/2.0/2.1, FSCT v3, OpenChain Telco, NTIA) theo README.<br>- `sbomqs policy`: file YAML gồm `type` (whitelist, blacklist, required), `rules`, `action` (fail, warn, pass), mức `comp` hay `doc`; vi phạm làm lệnh thoát mã 1 (cmd/policy.go bắt `ErrPolicyViolation` rồi `os.Exit(1)`). |
| Tiêu chí và cách kiểm | Cổng thật dựa trên exit code của `policy`; lệnh `score` tự nó không có ngưỡng, tài liệu hướng dẫn tự viết shell so điểm (docs/commands/score.md: `score < 7.0` thì `exit 1`). Dải điểm mô tả: 9-10 xuất sắc, dưới 5 là thất bại. CI repo chạy `make ci` và `make test` (go test -race) trên 3 hệ điều hành. |
| Giới hạn và rủi ro | Lệnh `share` gửi báo cáo điểm tới https://sbombenchmark.dev (pkg/share/share.go, HTTP POST), tức dữ liệu rời máy khi người dùng chủ động gọi; các lệnh còn lại chưa thấy gọi mạng trong phần đã đọc (chưa rà toàn mã). Hệ thống hãng Interlynk (README quảng bá gói free tier và demo.interlynk.io) là dịch vụ riêng, ngoài phạm vi license Apache. Điểm số do tác giả định nghĩa, không phải chuẩn; số khẳng định về ENISA/white paper trong README là trích dẫn của tác giả (chưa xác minh). |
| So với | `microsoft-sbom-tool` (sinh SBOM, không chấm); `owasp-dependency-track` (quản lý SBOM); `openssf-scorecard` (chấm repo, cùng ý tưởng điểm số máy đọc). |
| Nguồn | [README](https://github.com/interlynk-io/sbomqs/blob/613d55c2db5a3d4d12f74a2a6d582299d996dd24/README.md) · [LICENSE](https://github.com/interlynk-io/sbomqs/blob/613d55c2db5a3d4d12f74a2a6d582299d996dd24/LICENSE) · [docs/guides/policy.md](https://github.com/interlynk-io/sbomqs/blob/613d55c2db5a3d4d12f74a2a6d582299d996dd24/docs/guides/policy.md) · [docs/commands/score.md](https://github.com/interlynk-io/sbomqs/blob/613d55c2db5a3d4d12f74a2a6d582299d996dd24/docs/commands/score.md) · [docs/reference/quality-checks.md](https://github.com/interlynk-io/sbomqs/blob/613d55c2db5a3d4d12f74a2a6d582299d996dd24/docs/reference/quality-checks.md) · [pkg/scorer/ntia.go](https://github.com/interlynk-io/sbomqs/blob/613d55c2db5a3d4d12f74a2a6d582299d996dd24/pkg/scorer/ntia.go) · [pkg/share/share.go](https://github.com/interlynk-io/sbomqs/blob/613d55c2db5a3d4d12f74a2a6d582299d996dd24/pkg/share/share.go) · [cmd/policy.go](https://github.com/interlynk-io/sbomqs/blob/613d55c2db5a3d4d12f74a2a6d582299d996dd24/cmd/policy.go) · [Makefile](https://github.com/interlynk-io/sbomqs/blob/613d55c2db5a3d4d12f74a2a6d582299d996dd24/Makefile) · [.github/workflows/ci.yml](https://github.com/interlynk-io/sbomqs/blob/613d55c2db5a3d4d12f74a2a6d582299d996dd24/.github/workflows/ci.yml) |

<a id="n2-slsa-verifier"></a>

### SLSA Verifier

| Thuộc tính | Giá trị |
|---|---|
| Repo | https://github.com/slsa-framework/slsa-verifier |
| License | Apache-2.0 |
| Phiên bản đã đọc | `46099781eca1b8e91884770f40476631b033e0e8` (commit 2026-08-06) |
| Kiểm chứng | 2026-11-24; code-read; đã đọc README.md, LICENSE, verifiers/verifier.go, verifiers/internal/gha/provenance.go, Makefile (target regression-test), .github/workflows/pre-submit.cli.yml (đoạn đầu); chưa chạy upstream |
| Khoảng trống lấp | Chuỗi cung ứng AI: AI-BOM/SBOM/VEX (kiểm provenance của artifact) |
| Cơ chế đáng học | - `verifiers/verifier.go` chọn verifier theo builder ID (GHA mặc định, GCB, VSA); `VerifyArtifact`/`VerifyImage` trả provenance đã xác minh cùng builder tin cậy.<br>- `gha/provenance.go`: `VerifyProvenanceSignature` đối chiếu bản ghi Rekor (có chứng chỉ nhúng thì tra trực tiếp, không thì tìm theo digest); `VerifyProvenance` so builder ID khớp tuyệt đối hoặc theo tiền tố đường dẫn (BYOB), rồi `VerifyProvenanceCommonOptions` kiểm digest, `--source-uri`, nhánh, tag, input workflow.<br>- Cờ `--print-provenance` in provenance đã xác minh để chuyển vào policy engine khác (README). |
| Tiêu chí và cách kiểm | Thoát mã khác 0 khi xác minh lỗi (cli/slsa-verifier/main.go có `os.Exit(1)`, chỉ thấy qua grep, chưa đọc cả file) (chưa xác minh đầy đủ). Có bộ regression với dữ liệu mẫu `cli/slsa-verifier/testdata` và workflow pre-submit chạy `make regression-test`, lịch e2e hằng tuần. |
| Giới hạn và rủi ro | README mở đầu ghi dự án không còn được bảo trì tích cực và khuyên dùng GitHub artifact attestations với `gh attestation verify`; trinh sát không nêu điều này. Chỉ hỗ trợ builder GitHub và Google Cloud Build, `--source-uri` chỉ nhận URI GitHub. Cần mạng tới Rekor/TUF khi xác minh. |
| So với | `cosign` (ký và xác minh chữ ký); `slsa` (khung và mức SLSA); `in-toto` (định dạng attestation). |
| Nguồn | [README](https://github.com/slsa-framework/slsa-verifier/blob/46099781eca1b8e91884770f40476631b033e0e8/README.md) · [LICENSE](https://github.com/slsa-framework/slsa-verifier/blob/46099781eca1b8e91884770f40476631b033e0e8/LICENSE) · [verifiers/verifier.go](https://github.com/slsa-framework/slsa-verifier/blob/46099781eca1b8e91884770f40476631b033e0e8/verifiers/verifier.go) · [verifiers/internal/gha/provenance.go](https://github.com/slsa-framework/slsa-verifier/blob/46099781eca1b8e91884770f40476631b033e0e8/verifiers/internal/gha/provenance.go) · [.github/workflows/pre-submit.cli.yml](https://github.com/slsa-framework/slsa-verifier/blob/46099781eca1b8e91884770f40476631b033e0e8/.github/workflows/pre-submit.cli.yml) · [Makefile](https://github.com/slsa-framework/slsa-verifier/blob/46099781eca1b8e91884770f40476631b033e0e8/Makefile) |

<a id="n2-allstar"></a>

### Allstar

| Thuộc tính | Giá trị |
|---|---|
| Repo | https://github.com/ossf/allstar |
| License | Apache-2.0 |
| Phiên bản đã đọc | `9e77102569fbc1ddc6a71687267ab26a1bd3044f` (commit 2026-11-23) |
| Kiểm chứng | 2026-11-24; code-read; đã đọc README.md, LICENSE, pkg/policydef/policydef.go, pkg/enforce/enforce.go, pkg/policies/branch/branch.go (phần kiểu cấu hình), .github/workflows/pr.yaml (đoạn đầu); chưa chạy upstream |
| Khoảng trống lấp | Policy-as-code admission/runtime (chính sách cho cài đặt repo GitHub) |
| Cơ chế đáng học | - `pkg/policydef/policydef.go` định nghĩa interface `Policy` gồm `IsEnabled`, `Check`, `Fix`, `GetAction`; mỗi chính sách (branch, binary, codeowners, outside, scorecard, secretscanning, security, workflow, admin) là một gói trong `pkg/policies/`.<br>- `pkg/enforce/enforce.go` `handlePolicyFailure` xử lý hành động `log`, `issue` (mở issue, nhắc lại sau 24 giờ theo README), `fix` (gọi `Fix` sửa cài đặt repo); `email` chỉ ghi cảnh báo chưa cài, `block` và `rpc` README ghi là đề xuất chưa làm.<br>- Cấu hình YAML ở repo `.allstar` của tổ chức, có opt-in/opt-out và cấu hình riêng từng repo (README); ví dụ `branch_protection.yaml` với `requireApproval`, `approvalCount`, `enforceOnAdmins`. |
| Tiêu chí và cách kiểm | Kiểm bằng cách đọc cài đặt GitHub qua API rồi so với cấu hình; kết quả `Pass` hay không do từng chính sách trả về. CI repo chạy golangci-lint, `go build`, `go test`, `go vet` và `deadcode` (pr.yaml). Thao tác ngưỡng cụ thể thuộc từng chính sách, chỉ đọc phần kiểu cấu hình của branch. |
| Giới hạn và rủi ro | README mở đầu: app Allstar do OpenSSF lưu trữ đã bị ngưng; trinh sát mô tả như GitHub App dùng chung nên sai. Muốn dùng phải tự tạo GitHub App rồi chạy dạng Action hoặc daemon, cần quyền ghi cài đặt repo nếu bật `fix`. Hành động `block` chưa có nên không chặn merge trực tiếp. |
| So với | `openssf-scorecard` (nguồn điểm mà chính sách `scorecard` dùng); `opa-conftest` và `open-policy-agent-opa` (policy-as-code tổng quát, không gắn GitHub). |
| Nguồn | [README](https://github.com/ossf/allstar/blob/9e77102569fbc1ddc6a71687267ab26a1bd3044f/README.md) · [LICENSE](https://github.com/ossf/allstar/blob/9e77102569fbc1ddc6a71687267ab26a1bd3044f/LICENSE) · [pkg/policydef/policydef.go](https://github.com/ossf/allstar/blob/9e77102569fbc1ddc6a71687267ab26a1bd3044f/pkg/policydef/policydef.go) · [pkg/enforce/enforce.go](https://github.com/ossf/allstar/blob/9e77102569fbc1ddc6a71687267ab26a1bd3044f/pkg/enforce/enforce.go) · [pkg/policies/branch/branch.go](https://github.com/ossf/allstar/blob/9e77102569fbc1ddc6a71687267ab26a1bd3044f/pkg/policies/branch/branch.go) · [.github/workflows/pr.yaml](https://github.com/ossf/allstar/blob/9e77102569fbc1ddc6a71687267ab26a1bd3044f/.github/workflows/pr.yaml) |

<a id="n2-kyverno"></a>

### Kyverno

| Thuộc tính | Giá trị |
|---|---|
| Repo | https://github.com/kyverno/kyverno |
| License | Apache-2.0 |
| Phiên bản đã đọc | `cb73f9dc7a3f59c9f48178549e3c214b5a2b4b0c` (commit 2026-11-23) |
| Kiểm chứng | 2026-11-24; code-read; đã đọc README.md, LICENSE, pkg/engine/AGENTS.md, pkg/image/AGENTS.md (tài liệu tác giả, đối chiếu với cây thư mục), pkg/image/verifiers/ivpol/cosign/verifier.go và opts.go, test/cli/test-image-validating-policy/explain/json-policy.yaml, .github/workflows/check-unit-tests.yaml (đoạn đầu); chưa chạy upstream |
| Khoảng trống lấp | Policy-as-code admission/runtime (policy engine K8s, kiểm chữ ký ảnh) |
| Cơ chế đáng học | - Ở commit này chính sách mới là CEL, nhóm API `policies.kyverno.io` (CRD trong config/crds/policies.kyverno.io: ValidatingPolicy, MutatingPolicy, GeneratingPolicy, DeletingPolicy, ImageValidatingPolicy và bản Namespaced). Mô tả trinh sát về YAML với `verifyImages` đã lỗi thời. Theo `pkg/engine/AGENTS.md` engine cũ `kyverno.io/v1` đã xóa; cây thư mục không còn `pkg/cosign` hay `verifiers/cpol`, nhưng config/crds/kyverno vẫn còn CRD ClusterPolicy, nên trạng thái chuyển tiếp.<br>- `ImageValidatingPolicy` khai `matchImageReferences`, `attestors` (cosign key hoặc keyless, notary), `images` và `validations` bằng CEL (mẫu json-policy.yaml); verifier ở `pkg/image/verifiers/ivpol/cosign/verifier.go` có `VerifyImageSignature` và `VerifyAttestationSignature`, hỗ trợ bundle Sigstore.<br>- `opts.go` dùng TUF để lấy trusted root, có khóa mutex riêng quanh TUF; AGENTS.md của tác giả nói xác minh thất bại thì đóng (không có nhánh bỏ qua), các điểm này chỉ đối chiếu một phần với opts.go (chưa xác minh toàn bộ). |
| Tiêu chí và cách kiểm | CLI `kyverno apply`/`test` chạy chính sách ngoại tuyến với bộ ca trong test/cli (nhiều thư mục theo loại chính sách, gồm `test-legacy-policies`); CI có check-unit-tests chạy `make test-unit` cùng nhiều workflow khác (lint, codegen, e2e-gate; chỉ mở check-unit-tests). Chưa chạy. |
| Giới hạn và rủi ro | Mở rộng lớn nên cần học khái niệm mới (CEL, nhiều CRD); tài liệu cũ về ClusterPolicy có thể không còn đúng với nhánh này. Chạy như admission webhook nên là điểm lỗi vận hành (chưa đọc cấu hình failurePolicy). README tự nêu giới hạn: không vá lỗi của Kubernetes và chỉ thực thi chính sách người dùng viết. Có CLAUDE.md và AGENTS.md trong repo, coi là nội dung đọc. |
| So với | `open-policy-agent-opa` (Rego, mục đích chung); `opa-conftest` (kiểm file cấu hình); `cedar` (chính sách phân quyền); `cosign` (công cụ ký mà verifier dựa vào). |
| Nguồn | [README](https://github.com/kyverno/kyverno/blob/cb73f9dc7a3f59c9f48178549e3c214b5a2b4b0c/README.md) · [LICENSE](https://github.com/kyverno/kyverno/blob/cb73f9dc7a3f59c9f48178549e3c214b5a2b4b0c/LICENSE) · [pkg/engine/AGENTS.md](https://github.com/kyverno/kyverno/blob/cb73f9dc7a3f59c9f48178549e3c214b5a2b4b0c/pkg/engine/AGENTS.md) · [pkg/image/AGENTS.md](https://github.com/kyverno/kyverno/blob/cb73f9dc7a3f59c9f48178549e3c214b5a2b4b0c/pkg/image/AGENTS.md) · [pkg/image/verifiers/ivpol/cosign/verifier.go](https://github.com/kyverno/kyverno/blob/cb73f9dc7a3f59c9f48178549e3c214b5a2b4b0c/pkg/image/verifiers/ivpol/cosign/verifier.go) · [pkg/image/verifiers/ivpol/cosign/opts.go](https://github.com/kyverno/kyverno/blob/cb73f9dc7a3f59c9f48178549e3c214b5a2b4b0c/pkg/image/verifiers/ivpol/cosign/opts.go) · [json-policy.yaml (mẫu ImageValidatingPolicy)](https://github.com/kyverno/kyverno/blob/cb73f9dc7a3f59c9f48178549e3c214b5a2b4b0c/test/cli/test-image-validating-policy/explain/json-policy.yaml) · [.github/workflows/check-unit-tests.yaml](https://github.com/kyverno/kyverno/blob/cb73f9dc7a3f59c9f48178549e3c214b5a2b4b0c/.github/workflows/check-unit-tests.yaml) |

<a id="n2-pitloom"></a>

### Pitloom

| Thuộc tính | Giá trị |
|---|---|
| Repo | https://github.com/bact/pitloom |
| License | Apache-2.0 |
| Phiên bản đã đọc | `ef5be3b2dec4d942ee965fb8bc6dbf774dff47e5` (commit 2026-11-23) |
| Kiểm chứng | 2026-11-24; code-read; đã đọc README, LICENSE, pyproject, docs/cli.md, docs/agent-skills.md, `_gguf_bounds.py`, workflow test và fuzz; chưa chạy upstream |
| Khoảng trống lấp | Chuỗi cung ứng AI: sinh SBOM/AIBOM cho dự án Python và file mô hình |
| Cơ chế đáng học | • Sinh SBOM chuẩn SPDX 3 (không phải CycloneDX) cho dự án (`loom project`), wheel (`loom wheel`), môi trường (`loom env`) và file mô hình (`loom model`) — README.md.<br>• Đọc metadata mô hình GGUF, ONNX, Safetensors, PyTorch, fastText mà không nạp trọng số; reader GGUF có giới hạn cứng (số cặp, tensor, mảng) và coi file lạ là không tin cậy — `_gguf_bounds.py`, cờ `--trust-model-files`.<br>• Nhúng SBOM vào wheel qua hook Hatchling theo PEP 770 (`.dist-info/sboms`) và có GitHub Action cùng 3 skill (`sbom-generate`, `sbom-enrich`, `sbom-validate`) — `docs/agent-skills.md`.<br>• Chế độ `--offline` cấm truy cập mạng; repo từ xa là không tin cậy nên cấu hình `[tool.pitloom]` của chính nó bị bỏ qua — `docs/cli.md`. |
| Tiêu chí và cách kiểm | Kiểm bằng máy: có thể validate SPDX 3 (extra `validate`, schema/SHACL); CI test chạy trên nhiều hệ điều hành khi gắn nhãn, fuzz chạy thủ công (`workflow_dispatch`, mặc định 300 giây mỗi target), thêm workflow pip-audit, scorecard, bandit (tên file). Chưa chạy. |
| Giới hạn và rủi ro | Rất mới và ít người dùng (8 sao theo trinh sát, bản 0.24.0), một tác giả chính (cũng là người liên quan SPDX). Cần cài thêm gói ngoài (`licenseid`, extra `ai` kéo fasttext-community, fickling, gguf…) nên bề mặt phụ thuộc lớn. Chưa xác minh chất lượng SBOM so với công cụ khác. Tài liệu CC0-1.0, mã Apache-2.0, fixture mô hình có license riêng. |
| So với | [Microsoft SBOM Tool](31-software-supply-chain-security/README.md#nt-microsoft-sbom-tool) · [Syft](31-software-supply-chain-security/README.md) · [ModelScan](12-ai-security-guardrails/README.md) |
| Nguồn | [README.md](https://github.com/bact/pitloom/blob/ef5be3b2dec4d942ee965fb8bc6dbf774dff47e5/README.md) · [LICENSE](https://github.com/bact/pitloom/blob/ef5be3b2dec4d942ee965fb8bc6dbf774dff47e5/LICENSE) · [pyproject.toml](https://github.com/bact/pitloom/blob/ef5be3b2dec4d942ee965fb8bc6dbf774dff47e5/pyproject.toml) · [cli.md](https://github.com/bact/pitloom/blob/ef5be3b2dec4d942ee965fb8bc6dbf774dff47e5/docs/cli.md) · [agent-skills.md](https://github.com/bact/pitloom/blob/ef5be3b2dec4d942ee965fb8bc6dbf774dff47e5/docs/agent-skills.md) · [_gguf_bounds.py](https://github.com/bact/pitloom/blob/ef5be3b2dec4d942ee965fb8bc6dbf774dff47e5/src/pitloom/extract/ai_model/_gguf_bounds.py) · [test.yml](https://github.com/bact/pitloom/blob/ef5be3b2dec4d942ee965fb8bc6dbf774dff47e5/.github/workflows/test.yml) · [fuzz.yml](https://github.com/bact/pitloom/blob/ef5be3b2dec4d942ee965fb8bc6dbf774dff47e5/.github/workflows/fuzz.yml) |

<a id="n2-jadx"></a>

### JADX

| Thuộc tính | Giá trị |
|---|---|
| Repo | https://github.com/skylot/jadx |
| License | Apache-2.0 |
| Phiên bản đã đọc | `d6c683fc940c4687387f8ae9188c7b8eecc91c85` (commit 2026-11-23) |
| Kiểm chứng | 2026-11-24; code-read; đã đọc README.md, LICENSE, NOTICE, SECURITY.md, Jadx.java; chưa chạy upstream |
| Khoảng trống lấp | Phân tích ngược Android: lấy mã Java và tài nguyên từ APK/AAB làm đầu vào cho review và quét tĩnh |
| Cơ chế đáng học | • `jadx-core/.../Jadx.java`: danh sách pass tuần tự (PrepareAccessFlags, DeobfuscatorVisitor, UsageInfoVisitor, BlockSplitter, SSATransform, TypeInferenceVisitor, RegionMakerVisitor, ...) quyết định chất lượng mã sinh ra; CLI chọn `-m` (auto, restructure, simple hoặc fallback) và `--show-bad-code`.<br>• Khử làm rối: `--deobf` đổi tên ngắn hơn 3 hoặc dài hơn 64 ký tự (`--deobf-min/--deobf-max`), đọc/ghi ánh xạ `.jobf`, nhập ánh xạ Tiny/Enigma qua `--mappings-path`.<br>• Xuất dự án Gradle (`-e`, `--export-gradle-type`) và đầu ra `json`, tiện nối vào chuỗi quét tự động.<br>• Plugin (`jadx plugins`), plugin tools tải từ GitHub (`GithubTools` dùng api.github.com). |
| Tiêu chí và cách kiểm | Kiểm bằng máy: hơn 700 file Java trong `jadx-core/src/test` (lấy `TestBreakInLoop` làm ví dụ: biên dịch lớp mẫu, giải mã, khẳng định mã Java sinh ra chứa `for (int i = 0; ...)`, `break;`), nhưng kiểm hồi quy theo mẫu mã chứ không có ngưỡng tỉ lệ giải mã. CI `build-test.yml` (đã đọc) chạy `./gradlew build dist distWin` trên ubuntu và windows, JDK 25 để build, mục tiêu Java 11. Chưa chạy; chất lượng giải mã trên APK thật bị làm rối: (chưa xác minh), README thừa nhận lỗi. |
| Giới hạn và rủi ro | Apache-2.0 (LICENSE; NOTICE nêu mã lấy từ AOSP `dx` và thư viện bên thứ ba như JCommander, cùng Apache-2.0). Giải mã có thể sai hoặc thiếu (README); không dùng đầu ra làm bằng chứng pháp lý/an toàn cuối. GUI mặc định `checkForUpdates = true`, gọi api.github.com kiểm bản mới (`JadxUpdate.kt`); trình quản lý plugin cũng tải từ GitHub: cần tắt/chặn mạng khi phân tích mẫu độc. Chạy phần mềm trên mẫu không tin cậy (parser Dex/XML/ZIP) cần cô lập; chỉ kiểm SECURITY.md (quy trình báo lỗi ba ngày làm việc), chưa audit parser. Bảo trì tích cực (commit 2026-11-23). |
| So với | ghidra (đảo ngược đa kiến trúc, trọng tâm native, có decompiler C); radare2 (khung dòng lệnh, native); mobsf (gọi jadx rồi chạy luật quét tĩnh) |
| Nguồn | [README.md](https://github.com/skylot/jadx/blob/d6c683fc940c4687387f8ae9188c7b8eecc91c85/README.md) · [LICENSE](https://github.com/skylot/jadx/blob/d6c683fc940c4687387f8ae9188c7b8eecc91c85/LICENSE) · [NOTICE](https://github.com/skylot/jadx/blob/d6c683fc940c4687387f8ae9188c7b8eecc91c85/NOTICE) · [SECURITY.md](https://github.com/skylot/jadx/blob/d6c683fc940c4687387f8ae9188c7b8eecc91c85/SECURITY.md) · [Jadx.java](https://github.com/skylot/jadx/blob/d6c683fc940c4687387f8ae9188c7b8eecc91c85/jadx-core/src/main/java/jadx/core/Jadx.java) · [TestBreakInLoop.java](https://github.com/skylot/jadx/blob/d6c683fc940c4687387f8ae9188c7b8eecc91c85/jadx-core/src/test/java/jadx/tests/integration/loops/TestBreakInLoop.java) · [JadxUpdate.kt](https://github.com/skylot/jadx/blob/d6c683fc940c4687387f8ae9188c7b8eecc91c85/jadx-gui/src/main/java/jadx/gui/update/JadxUpdate.kt) · [JadxSettingsData.java](https://github.com/skylot/jadx/blob/d6c683fc940c4687387f8ae9188c7b8eecc91c85/jadx-gui/src/main/java/jadx/gui/settings/JadxSettingsData.java) · [build-test.yml](https://github.com/skylot/jadx/blob/d6c683fc940c4687387f8ae9188c7b8eecc91c85/.github/workflows/build-test.yml) |

<a id="n2-mobsf"></a>

### MobSF

| Thuộc tính | Giá trị |
|---|---|
| Repo | https://github.com/MobSF/Mobile-Security-Framework-MobSF |
| License | GPL-3.0-only |
| Phiên bản đã đọc | `fa87c37892b264cf76bed8c358cc2d5d5323c8c2` (commit 2026-11-17) |
| Kiểm chứng | 2026-11-24; code-read; đã đọc README.md, LICENSE, settings.py, android_rules.yaml, android_apis.yaml; chưa chạy upstream |
| Khoảng trống lấp | Cổng bảo mật ứng dụng mobile: quét tĩnh APK/IPA, ánh xạ phát hiện sang CWE/OWASP Mobile/MASVS, có API cho pipeline |
| Cơ chế đáng học | • `android_rules.yaml` (54 luật `- id:` theo đếm grep) và `android_apis.yaml`: mỗi luật có `type` (Regex, RegexOr...), `pattern`, `severity` và `metadata` (cvss, cwe, owasp-mobile, masvs).<br>• `common/appsec.py::calculate_security_score` và `common_fields`: gom phát hiện theo mức high/warning/secure/info thành điểm trong 10 đến 100 và bảng AppSec.<br>• `api_static_analysis.py` cung cấp `api_upload`, `api_scan`, `api_recent_scans`, `api_tasks`... để nối vào CI; xác thực bằng khóa API (cấu hình trong settings, chưa đọc chi tiết middleware).<br>• `tests_network_limits.py`: giới hạn số URL và thời hạn cho các yêu cầu mạng do nội dung ứng dụng kích hoạt (assetlinks, Firebase) để tránh quét bị lợi dụng. |
| Tiêu chí và cách kiểm | Kiểm bằng máy nhưng không có cổng đạt/trượt chuẩn sẵn: điểm số là chỉ số, CI phải tự đọc JSON và đặt ngưỡng. CI `mobsf-test.yml` (đã đọc) chạy lint (tox) và test đơn vị trên ubuntu-22.04, macOS, Windows với Python 3.12 và 3.13, JDK 21; chưa chạy. Độ phủ MASVS/MASTG thực tế: chỉ biết nhãn trong luật, không chứng minh phủ đủ danh mục (chưa xác minh); nhãn dạng `storage-7`, `code-2` chưa đối chiếu phiên bản MASVS. |
| Giới hạn và rủi ro | GPL-3.0-only (LICENSE): nhúng/phân phối lại mã MobSF kéo theo nghĩa vụ copyleft; dùng như dịch vụ nội bộ thường ổn nhưng cần đánh giá. Thư mục `LICENSES/` liệt kê license từng thành phần đi kèm (androguard, jadx, frida, apksigner, dữ liệu IP2Location LITE...), có mục điều khoản riêng. Quét tĩnh VẪN gọi ra ngoài theo nội dung ứng dụng: Firebase Remote Config bằng khóa API trích từ APK (`firebase.py`), assetlinks của các domain trong manifest, cập nhật DB Maltrail/Trackers, kiểm kết nối Google/Baidu; VirusTotal chỉ khi đặt `MOBSF_VT_API_KEY` và `MOBSF_VT_UPLOAD=1` sẽ tải mẫu lên. `MOBSF_DISABLE_AUTHENTICATION` mặc định 0 nhưng `ALLOWED_HOSTS` chứa `*`: không phơi ra Internet. Phân tích động cần thiết bị/emulator root và tải Frida server từ GitHub. |
| So với | semgrep (luật mã tổng quát, không có ngữ cảnh Android); trivy và osv-scanner (SBOM và lỗ hổng phụ thuộc); jadx (bộ giải mã mà MobSF dùng); maestro (kiểm thử giao diện mobile, khác nhiệm vụ) |
| Nguồn | [README.md](https://github.com/MobSF/Mobile-Security-Framework-MobSF/blob/fa87c37892b264cf76bed8c358cc2d5d5323c8c2/README.md) · [LICENSE](https://github.com/MobSF/Mobile-Security-Framework-MobSF/blob/fa87c37892b264cf76bed8c358cc2d5d5323c8c2/LICENSE) · [settings.py](https://github.com/MobSF/Mobile-Security-Framework-MobSF/blob/fa87c37892b264cf76bed8c358cc2d5d5323c8c2/mobsf/MobSF/settings.py) · [android_rules.yaml](https://github.com/MobSF/Mobile-Security-Framework-MobSF/blob/fa87c37892b264cf76bed8c358cc2d5d5323c8c2/mobsf/StaticAnalyzer/views/android/rules/android_rules.yaml) · [android_apis.yaml](https://github.com/MobSF/Mobile-Security-Framework-MobSF/blob/fa87c37892b264cf76bed8c358cc2d5d5323c8c2/mobsf/StaticAnalyzer/views/android/rules/android_apis.yaml) · [appsec.py](https://github.com/MobSF/Mobile-Security-Framework-MobSF/blob/fa87c37892b264cf76bed8c358cc2d5d5323c8c2/mobsf/StaticAnalyzer/views/common/appsec.py) · [firebase.py](https://github.com/MobSF/Mobile-Security-Framework-MobSF/blob/fa87c37892b264cf76bed8c358cc2d5d5323c8c2/mobsf/StaticAnalyzer/views/common/firebase.py) · [tests_network_limits.py](https://github.com/MobSF/Mobile-Security-Framework-MobSF/blob/fa87c37892b264cf76bed8c358cc2d5d5323c8c2/mobsf/StaticAnalyzer/tests_network_limits.py) · [api_static_analysis.py](https://github.com/MobSF/Mobile-Security-Framework-MobSF/blob/fa87c37892b264cf76bed8c358cc2d5d5323c8c2/mobsf/MobSF/views/api/api_static_analysis.py) · [mobsf-test.yml](https://github.com/MobSF/Mobile-Security-Framework-MobSF/blob/fa87c37892b264cf76bed8c358cc2d5d5323c8c2/.github/workflows/mobsf-test.yml) · [jadx.txt](https://github.com/MobSF/Mobile-Security-Framework-MobSF/blob/fa87c37892b264cf76bed8c358cc2d5d5323c8c2/LICENSES/jadx.txt) |

<a id="n2-scancode-toolkit"></a>

### ScanCode Toolkit

| Thuộc tính | Giá trị |
|---|---|
| Repo | https://github.com/aboutcode-org/scancode-toolkit |
| License | Apache-2.0 AND CC-BY-4.0 (mã Apache-2.0, dữ liệu luật/rule CC-BY-4.0; kèm thành phần bên thứ ba) |
| Phiên bản đã đọc | `2b07b4d71b426bc78e350c80c7b0a90e7280319e` (commit 2026-11-23) |
| Kiểm chứng | 2026-11-24; code-read; đã đọc README.rst, NOTICE, pyproject.toml, src/licensedcode/index.py, src/licensedcode/match_hash.py, src/licensedcode/plugin_license_policy.py, azure-pipelines.yml, .github/workflows/zizmor.yml; chưa chạy upstream |
| Khoảng trống lấp | Tuân thủ giấy phép và nguồn gốc mã (license/provenance) |
| Cơ chế đáng học | - `src/licensedcode/index.py` dựng danh sách matcher theo thứ tự: tra SPDX-License-Identifier, khớp Aho-Corasick chính xác, rồi khớp chuỗi gần đúng (`seq`) chỉ khi bật approximate; dừng khi không còn đoạn có thể khớp.<br>- `src/licensedcode/match_hash.py` băm SHA-1 dãy token để khớp cả khối văn bản một lần.<br>- `src/licensedcode/data/licenses` (2743 file) và `data/rules` (hơn 36 nghìn file) là dữ liệu có phiên bản kèm metadata, tách khỏi mã.<br>- `src/licensedcode/plugin_license_policy.py` áp file chính sách YAML (nhãn, màu theo license key) lên từng tệp sau khi quét. |
| Tiêu chí và cách kiểm | Có bộ test lớn (README tuyên bố hơn 30.000 test, chưa xác minh con số); `azure-pipelines.yml` chạy pytest chia nhóm licensedcode, datadriven và validate trên nhiều hệ điều hành, Python 3.14 cho job lõi. Workflow `zizmor.yml` quét bảo mật GitHub Actions. Kiểm bằng máy, nhưng ngưỡng độ chính xác không công bố thành số trong các file đã đọc. Plugin chính sách chỉ gắn nhãn, không tự làm hỏng build. |
| Giới hạn và rủi ro | Giấy phép kép (mã Apache-2.0, dữ liệu CC-BY-4.0) và nhiều thành phần bên thứ ba copyleft nhúng kèm, nên khi nhúng dữ liệu rule vào sản phẩm phải giữ ghi công. Nặng (cài qua `configure`, nhiều phụ thuộc native). Kết quả là phát hiện văn bản giấy phép, không phải tư vấn pháp lý. Không thấy telemetry trong `src/scancode` qua grep (chưa đọc toàn bộ). Bảo trì rất tích cực (push 2026-11-23). |
| So với | `trivy` và `osv-scanner` (quét lỗ hổng, không chuyên về giấy phép); `syft` (SBOM, nhận diện package nhưng không khớp văn bản giấy phép); `owasp-dependency-track` (quản lý thành phần theo SBOM). |
| Nguồn | [README.rst](https://github.com/aboutcode-org/scancode-toolkit/blob/2b07b4d71b426bc78e350c80c7b0a90e7280319e/README.rst) · [NOTICE](https://github.com/aboutcode-org/scancode-toolkit/blob/2b07b4d71b426bc78e350c80c7b0a90e7280319e/NOTICE) · [pyproject.toml](https://github.com/aboutcode-org/scancode-toolkit/blob/2b07b4d71b426bc78e350c80c7b0a90e7280319e/pyproject.toml) · [index.py](https://github.com/aboutcode-org/scancode-toolkit/blob/2b07b4d71b426bc78e350c80c7b0a90e7280319e/src/licensedcode/index.py) · [match_hash.py](https://github.com/aboutcode-org/scancode-toolkit/blob/2b07b4d71b426bc78e350c80c7b0a90e7280319e/src/licensedcode/match_hash.py) · [plugin_license_policy.py](https://github.com/aboutcode-org/scancode-toolkit/blob/2b07b4d71b426bc78e350c80c7b0a90e7280319e/src/licensedcode/plugin_license_policy.py) · [azure-pipelines.yml](https://github.com/aboutcode-org/scancode-toolkit/blob/2b07b4d71b426bc78e350c80c7b0a90e7280319e/azure-pipelines.yml) · [zizmor.yml](https://github.com/aboutcode-org/scancode-toolkit/blob/2b07b4d71b426bc78e350c80c7b0a90e7280319e/.github/workflows/zizmor.yml) |

<a id="n2-cve-bin-tool"></a>

### CVE Binary Tool

| Thuộc tính | Giá trị |
|---|---|
| Repo | https://github.com/ossf/cve-bin-tool |
| License | GPL-3.0-or-later (LICENSE.md là GPL-3.0; header file ghi GPL-3.0-or-later) |
| Phiên bản đã đọc | `09539e71596c6777e4b73209e9271d2cce2f764a` (commit 2026-11-23) |
| Kiểm chứng | 2026-11-24; code-read; đã đọc README.md, LICENSE.md, AGENTS.md, cve_bin_tool/checkers/openssl.py, cve_bin_tool/vex_manager/generate.py, cve_bin_tool/util.py, cve_bin_tool/cli.py, TRIAGE.json, .github/workflows/testing.yml; chưa chạy upstream |
| Khoảng trống lấp | Quản lý lỗ hổng sau SBOM (SCA vận hành, triage, ưu tiên) |
| Cơ chế đáng học | - `cve_bin_tool/checkers/*.py` (460 file; ví dụ `openssl.py`) khai báo `CONTAINS_PATTERNS`, `FILENAME_PATTERNS`, `VERSION_PATTERNS` và `VENDOR_PRODUCT` để nhận diện thành phần trong nhị phân.<br>- `cve_bin_tool/util.py` định nghĩa enum `Remarks` (NewFound, Unexplored, Confirmed, Mitigated, FalsePositive, NotAffected) làm trạng thái triage.<br>- `cve_bin_tool/vex_manager/generate.py` ánh xạ `Remarks` sang `analysis_state` của CycloneDX, CSAF và OpenVEX.<br>- `cve_bin_tool/data_sources/` có nguồn NVD, OSV, Red Hat, GitLab, Curl và EPSS để xếp ưu tiên; `TRIAGE.json` là mẫu CycloneDX VEX. |
| Tiêu chí và cách kiểm | `--severity` đặt ngưỡng CVSS tối thiểu để báo cáo; README ghi chế độ `-q` thoát với mã bằng số tệp có CVE (cli.py dòng 1344-1348 trả mã 1 khi có CVE), dùng được làm cổng CI. `AGENTS.md` yêu cầu checker mới có gói test thật trong `test/condensed-downloads/` từ ít nhất hai nguồn phân phối. Workflow `testing.yml` có job tài liệu và test; còn có fuzzing, CodeQL, Scorecard, dependency-review (chỉ thấy tên file, chưa mở hết). |
| Giới hạn và rủi ro | GPL-3.0 (copyleft mạnh) nếu liên kết mã. Dữ liệu CVE tải từ nhiều nguồn ngoài mỗi ngày một lần (cần mạng, nên có khóa NVD để tránh giới hạn tốc độ). Nhận diện bằng regex chuỗi nên có dương tính giả và âm tính giả với nhị phân bị strip hoặc biên dịch tĩnh; phạm vi do AGENTS.md giới hạn ở phát hiện phiên bản từ nhị phân. Không thấy telemetry trong mã Python (grep chỉ khớp file js đóng gói). Bảo trì tích cực. |
| So với | `grype` (quét SBOM/ảnh, thiên về package manager hơn nhị phân thuần); `osv-scanner`; `trivy`; `owasp-dependency-track` (quản trị VEX và triage theo dự án, có máy chủ). |
| Nguồn | [README.md](https://github.com/ossf/cve-bin-tool/blob/09539e71596c6777e4b73209e9271d2cce2f764a/README.md) · [LICENSE.md](https://github.com/ossf/cve-bin-tool/blob/09539e71596c6777e4b73209e9271d2cce2f764a/LICENSE.md) · [AGENTS.md](https://github.com/ossf/cve-bin-tool/blob/09539e71596c6777e4b73209e9271d2cce2f764a/AGENTS.md) · [openssl.py](https://github.com/ossf/cve-bin-tool/blob/09539e71596c6777e4b73209e9271d2cce2f764a/cve_bin_tool/checkers/openssl.py) · [generate.py](https://github.com/ossf/cve-bin-tool/blob/09539e71596c6777e4b73209e9271d2cce2f764a/cve_bin_tool/vex_manager/generate.py) · [util.py](https://github.com/ossf/cve-bin-tool/blob/09539e71596c6777e4b73209e9271d2cce2f764a/cve_bin_tool/util.py) · [cli.py](https://github.com/ossf/cve-bin-tool/blob/09539e71596c6777e4b73209e9271d2cce2f764a/cve_bin_tool/cli.py) · [TRIAGE.json](https://github.com/ossf/cve-bin-tool/blob/09539e71596c6777e4b73209e9271d2cce2f764a/TRIAGE.json) · [testing.yml](https://github.com/ossf/cve-bin-tool/blob/09539e71596c6777e4b73209e9271d2cce2f764a/.github/workflows/testing.yml) |
