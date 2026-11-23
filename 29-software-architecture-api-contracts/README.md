# 29. Kiến trúc phần mềm, yêu cầu & hợp đồng API

> Bổ sung cho xưởng phát triển phần mềm, khảo sát 2026-11-04. Phạm vi: từ yêu cầu có định danh, quyết định kiến trúc đến kiểm cấu trúc mã và tương thích API. Đây là hồ sơ nghiên cứu; không đặt bộ triển khai hay demo thực thi vào `stored`. Bốn upstream dưới được clone chỉ đọc, đọc LICENSE, implementation, callsite và CI tại full SHA; **code-read**, không cài/chạy/build upstream. Sao để `null`, không dùng mức quan tâm làm thước chất lượng.

## 1. Trần cần đạt và ranh giới với các mục khác

Một xưởng không chỉ sinh code nhanh: phải truy được vì sao có thay đổi, nó thuộc ranh giới nào và khách hàng nào có thể bị hỏng. Tuyến [28](../28-product-discovery-experimentation/README.md) chứng minh nhu cầu/giả thuyết; mục này biến quyết định thành hợp đồng; [30](../30-software-testing-quality/README.md) chứng minh hành vi; [32](../32-platform-delivery-engineering/README.md) và [33](../33-reliability-observability-operations/README.md) giữ bản phát hành vận hành được.

| Lớp | Artifact giữ trong repo tích hợp | Cổng nên có | Giới hạn |
|---|---|---|---|
| Yêu cầu | ID ổn định, tiêu chí nhận, owner, nguồn và trạng thái | Trace không đứt, thay đổi chưa review bị phát hiện | Trace đầy đủ không chứng minh yêu cầu đúng nhu cầu |
| Quyết định kiến trúc | ADR: bối cảnh, lựa chọn, trade-off, điều kiện xem lại | Review quyết định khi constraint đổi | Một mẫu ADR không là oracle tự động |
| Mô hình hệ thống | Context/container, boundary, dependency và deployment view có cùng ID | DSL hợp lệ và review chênh lệch mô hình | Sơ đồ đẹp không chứng minh mã tuân theo |
| Kiến trúc mã | Rule dependency theo module/layer | Import trái ranh giới/cycle làm CI fail | Phân tích tĩnh không phủ dynamic/runtime dependency |
| Hợp đồng API | OpenAPI versioned + compatibility policy + spec của bản đã phát hành | Breaking diff + runtime contract/consumer test | Hai spec khớp không chứng minh server thực thi spec |

Không chọn cả bốn công cụ cho mọi dự án. Một service nhỏ có thể dùng requirements/ADR Markdown, một OpenAPI và vài rule; hệ nhiều đội, khách hàng SDK hoặc chứng cứ truy vết mới cần lớp công cụ dày hơn.

<a id="doorstop-requirements-traceability"></a>

## 2. Doorstop: yêu cầu trong git, link có dấu vết thay đổi

| Thuộc tính | Giá trị |
|---|---|
| Repo/tổ chức | `doorstop-dev/doorstop` — cộng đồng Doorstop |
| License | LGPL-3.0-only; đọc LICENSE.md và SPDX của implementation |
| Phiên bản/phạm vi | `f5f2bef01a99c92210cad2713079f09cc4aed876`, 2026-11-04; `code-read` |
| Vai trò | Yêu cầu/test case dạng YAML, cây document và liên kết có stamp |
| Tích hợp | CLI `doorstop` ở repo đích; review requirements và trace diff cùng thay đổi code |

[README](https://github.com/doorstop-dev/doorstop/blob/f5f2bef01a99c92210cad2713079f09cc4aed876/README.md) mô tả item YAML có ID, link, validate và publish. [`Item.cleared`/`reviewed`](https://github.com/doorstop-dev/doorstop/blob/f5f2bef01a99c92210cad2713079f09cc4aed876/doorstop/core/item.py) so stamp của parent/link và nội dung để biết review không còn trùng bản hiện tại. Cơ chế này hữu ích khi yêu cầu gốc đổi: downstream phải xem lại, thay vì mặc định test case cũ vẫn hợp.

**Giới hạn quyết định:** [`ItemValidator`](https://github.com/doorstop-dev/doorstop/blob/f5f2bef01a99c92210cad2713079f09cc4aed876/doorstop/core/validators/item_validator.py) bỏ qua item inactive; một số tình huống `needs initial review` là info, `unreviewed changes`/suspect là warning. Mặc định `validate=True` không đồng nghĩa không còn warning. [CLI options](https://github.com/doorstop-dev/doorstop/blob/f5f2bef01a99c92210cad2713079f09cc4aed876/doorstop/cli/main.py) có `--warn-all`, `--error-all`, `--no-reformat`; nếu tổ chức muốn review/trace là điều kiện bắt buộc cần định nghĩa severity và dùng profile kiểm tương ứng, không tắt review/suspect cho qua. Stamp là dấu toàn vẹn nội dung, không là chữ ký người đã duyệt hay chứng cứ test đã chạy.

**Ghép vào xưởng:** định danh requirement → acceptance case → test/artifact thực thi; reviewer chịu trách nhiệm tính đúng của link; bật cổng được kiểm bằng fixture đứt link/thay parent/chưa review; lưu log và trạng thái inactive có giải thích. So với Markdown+ADR, Doorstop thêm trace/stamp; so với hệ ALM thương mại, cần tự đánh giá SSO, audit, phân quyền và workflow phê duyệt — **(chưa xác minh)** những khả năng ALM đó trong đợt này.

**Bằng chứng:** [LICENSE](https://github.com/doorstop-dev/doorstop/blob/f5f2bef01a99c92210cad2713079f09cc4aed876/LICENSE.md) · [Call validate](https://github.com/doorstop-dev/doorstop/blob/f5f2bef01a99c92210cad2713079f09cc4aed876/doorstop/cli/commands.py) · [CI đa OS/Python](https://github.com/doorstop-dev/doorstop/blob/f5f2bef01a99c92210cad2713079f09cc4aed876/.github/workflows/_common.yml). LGPL của công cụ không tự quyết định license tài liệu yêu cầu do người dùng viết; phân phối/nhúng thư viện cần xem nghĩa vụ tương ứng.

<a id="structurizr-model-code-boundary"></a>

## 3. Structurizr: một mô hình tạo nhiều view, vẫn cần kiểm mã riêng

| Thuộc tính | Giá trị |
|---|---|
| Repo/tác giả | `structurizr/structurizr` — Simon Brown, tác giả C4 |
| License | Apache-2.0 cho cây đã đọc; không suy sang dịch vụ thương mại |
| Phiên bản/phạm vi | `e3a736a90194d3ac692ad7b5c1c7a48287355347`, 2026-11-04; `code-read` |
| Vai trò | DSL/model cho context/container và nhiều view từ cùng mô hình |
| Tích hợp | Workspace DSL/JSON trong repo thiết kế, validate bằng toolchain ghim phiên bản |

[README monorepo](https://github.com/structurizr/structurizr/blob/e3a736a90194d3ac692ad7b5c1c7a48287355347/README.md) giới thiệu reference implementation C4 và đường `local`/playground. Không dùng đường dẫn `structurizr/dsl` như repo hiện hành: thao tác Git tới đường đó trả `Repository not found` trong phiên; mã DSL đọc được nằm trong monorepo này. Kết quả truy cập không tự xác định nguyên nhân archive/xoá/đổi quyền của repo cũ.

[`ValidateCommand`](https://github.com/structurizr/structurizr/blob/e3a736a90194d3ac692ad7b5c1c7a48287355347/structurizr-application/src/main/java/com/structurizr/command/ValidateCommand.java) load workspace, round-trip JSON để kích hoạt validation và tải themes để kiểm truy cập. Vì vậy `validate` không chỉ là parser offline nếu workspace dùng tài nguyên mạng; cũng **không kiểm rằng import/dependency trong code ứng với sơ đồ**. [DSL parser](https://github.com/structurizr/structurizr/blob/e3a736a90194d3ac692ad7b5c1c7a48287355347/structurizr-dsl/src/main/java/com/structurizr/dsl/StructurizrDslParser.java) có `setRestricted` tắt nhóm tính năng như plugin/script/filesystem. Không mặc định coi DSL từ nguồn lạ là dữ liệu thụ động; host/CLI có bật chế độ nào cần kiểm riêng, chưa thử runtime trong đợt này.

**Ghép vào xưởng:** lưu mô hình + ADR gắn ID boundary; review diff views theo thay đổi hệ thống; dùng parser/validator đúng phiên bản và giới hạn tài nguyên tham chiếu; ghép dependency-cruiser/ArchUnit hoặc kiểm phù hợp ngôn ngữ để chặn drift mã. So với Mermaid/PlantUML, giá trị ở shared semantic model nhiều view; so với bản đồ lấy từ source, đây là kiến trúc khai báo cần người giữ đúng.

**Bằng chứng:** [LICENSE](https://github.com/structurizr/structurizr/blob/e3a736a90194d3ac692ad7b5c1c7a48287355347/LICENSE) · [CI JDK21/Maven](https://github.com/structurizr/structurizr/blob/e3a736a90194d3ac692ad7b5c1c7a48287355347/.github/workflows/maven.yml). CI hiện loại nhóm `IntegrationTest`; không gọi “mọi integration đã được test” từ việc job build tồn tại.

<a id="dependency-cruiser-architecture-gates"></a>

## 4. dependency-cruiser: biến luật dependency JS/TS thành cổng

| Thuộc tính | Giá trị |
|---|---|
| Repo/tác giả | `sverweij/dependency-cruiser` — Sander Verweij |
| License | MIT |
| Phiên bản/phạm vi | `e6517db02e169f3db5c838bb1565ebd0fefeb452`, 2026-11-04; `code-read` |
| Vai trò | Graph dependency + rule forbidden/required theo cấu trúc JS/TS |
| Tích hợp | Dev dependency ghim lockfile, config rule được review cùng kiến trúc |

[README](https://github.com/sverweij/dependency-cruiser/blob/e6517db02e169f3db5c838bb1565ebd0fefeb452/README.md) minh hoạ chặn import từ production sang test và phát hiện dependency/cycle. Dùng quy tắc thể hiện boundary thật — ví dụ domain không import UI/DB adapter, package không vượt public entry point — thay vì chỉ xuất một đồ thị rồi gọi là kiểm kiến trúc.

**Bẫy cổng:** [CLI callsite](https://github.com/sverweij/dependency-cruiser/blob/e6517db02e169f3db5c838bb1565ebd0fefeb452/src/cli/index.mjs) trả exit code từ reporter. [JSON reporter](https://github.com/sverweij/dependency-cruiser/blob/e6517db02e169f3db5c838bb1565ebd0fefeb452/src/report/json.mjs) đặt `exitCode: 0`, trong khi [Error reporter](https://github.com/sverweij/dependency-cruiser/blob/e6517db02e169f3db5c838bb1565ebd0fefeb452/src/report/error.mjs) dùng `summary.advisedExitCode` (fallback `summary.error`). Vì vậy chạy `--output-type json` rồi thấy lệnh thành công chưa chứng minh không vi phạm. Dùng reporter `err` làm gate, giữ JSON/graph làm artifact riêng hoặc có consumer kiểm summary rõ. Không áp kết luận này sang mọi reporter.

**Ghép vào xưởng:** bắt đầu vài rule error quan trọng; fixture cố tình import trái lớp/cycle phải làm gate fail, fixture hợp lệ phải pass; kiểm alias/tsconfig và phạm vi include/exclude; baseline nợ cũ phải có owner và không được tăng âm thầm. Static graph không thể bao phủ mọi dependency được tạo động, network call hay cấu hình runtime; nối mô hình Structurizr và test tích hợp. ArchUnit phù hợp Java, kiểm kiến trúc riêng từng ngôn ngữ hoặc rule monorepo có sẵn là lựa chọn thay thế; không thêm dependency-cruiser chỉ để có graph nếu pipeline hiện tại đã chặn đủ boundary.

**Bằng chứng:** [LICENSE](https://github.com/sverweij/dependency-cruiser/blob/e6517db02e169f3db5c838bb1565ebd0fefeb452/LICENSE) · [Rule defaults](https://github.com/sverweij/dependency-cruiser/blob/e6517db02e169f3db5c838bb1565ebd0fefeb452/src/cli/init-config/config-template.mjs) · [CI tự kiểm dependency/test](https://github.com/sverweij/dependency-cruiser/blob/e6517db02e169f3db5c838bb1565ebd0fefeb452/.github/workflows/ci.yml). Nhiều rule khởi tạo là warning; severity phải phù hợp hợp đồng của đội.

<a id="oasdiff-compatibility-gates"></a>

## 5. oasdiff: tương thích API là quyết định release, không chỉ là báo cáo diff

| Thuộc tính | Giá trị |
|---|---|
| Repo/nhóm | `oasdiff/oasdiff` — nhóm oasdiff |
| License | Apache-2.0 |
| Phiên bản/phạm vi | `aa8a46f666d73479c542cd089037cc4989b6e42d`, 2026-11-04; `code-read` |
| Vai trò | So OpenAPI base/revision, phân loại thay đổi và breaking changes |
| Tích hợp | CLI/binary hoặc container đã ghim digest tại pipeline API |

[Tài liệu compatibility](https://github.com/oasdiff/oasdiff/blob/aa8a46f666d73479c542cd089037cc4989b6e42d/docs/BREAKING-CHANGES.md) phân biệt contract với server có thể chấp nhận dữ liệu rộng hơn. Thêm field request bắt buộc có thể phá client ngay khi server tự bù default; spec dùng cho SDK/gateway/validator cũng là khách hàng của thay đổi. Cần chọn policy theo API công bố, không suy từ vài request nội bộ vẫn trả 200.

[Command breaking](https://github.com/oasdiff/oasdiff/blob/aa8a46f666d73479c542cd089037cc4989b6e42d/internal/breaking_changes.go) mặc định `--fail-on` rỗng; [Callsite severity/exit](https://github.com/oasdiff/oasdiff/blob/aa8a46f666d73479c542cd089037cc4989b6e42d/internal/changelog.go) chỉ bật điều kiện fail khi được cấu hình. Cổng mẫu ở repo đích là `oasdiff breaking --fail-on ERR base.yaml revision.yaml`; nếu policy chặn cả warning, chọn `WARN` có chủ ý. Một lệnh chỉ in breaking changes có thể thoát 0. Base phải là spec **của bản đã phát hành/consumer đang dùng**, không tự so với một file đã bị ghi đè trong cùng PR.

**Giới hạn:** spec diff không gọi server, không biết authorization thực, logic idempotency hay dữ liệu production. Ghép Spectral (mục 05) để lint quy ước, Schemathesis và consumer/integration tests (mục 30) cho runtime; AsyncAPI/Protobuf/GraphQL cần bộ compatibility đúng định dạng, không ép vào OpenAPI. Ignore/severity override là thay đổi policy cần review, không là cách làm check xanh.

**Bằng chứng:** [LICENSE](https://github.com/oasdiff/oasdiff/blob/aa8a46f666d73479c542cd089037cc4989b6e42d/LICENSE) · [Fixture exit-code](https://github.com/oasdiff/oasdiff/blob/aa8a46f666d73479c542cd089037cc4989b6e42d/internal/breaking_files_test.go) · [CI Go đa OS](https://github.com/oasdiff/oasdiff/blob/aa8a46f666d73479c542cd089037cc4989b6e42d/.github/workflows/go.yml). Test nguồn củng cố ngữ nghĩa intended nhưng chưa được chạy lại trong phiên này.

## 6. Chuỗi áp dụng cho xưởng và cổng nghiệm thu

1. **Chọn phạm vi tối thiểu:** requirement ID + acceptance examples; ghi constraint bảo mật, dữ liệu, latency, chi phí và owner. Dùng Markdown trước; thêm Doorstop khi trace/version ảnh hưởng đáng kể.
2. **Chốt quyết định:** ADR nêu 2–4 phương án và vì sao chọn; vẽ context/container/boundary trong mô hình có ID. Thiết kế API/data ownership trước khi chia task cho nhiều coding agent.
3. **Biến boundary thành rule:** dependency-cruiser hoặc công cụ đúng ngôn ngữ chặn import trái lớp. Giữ fixture tốt/xấu chứng minh cổng có tác dụng, không chỉ kiểm file config tồn tại.
4. **Chốt compatibility:** spec phát hành có version/hash; lint + breaking diff + test runtime/consumer trước release. Thử thêm required field, xoá operation, đổi auth requirement để kiểm cổng bắt điều dự án coi là breaking.
5. **Truy vết artifact:** requirement → ADR/boundary → change/PR → test run → artifact digest → release/rollback. Link ID không được tự gán trạng thái “đã kiểm” nếu chỉ có file test mà chưa có run.
6. **Đánh giá drift:** khi requirement/API/dependency thay đổi, review lại downstream và giữ exception có owner/hạn xem lại. Đo defect lọt qua boundary, compatibility incident và thời gian tìm nguyên nhân; không đo bằng số sơ đồ hay số dòng requirement.

**Đầu ra đủ dùng:** một thay đổi mẫu đi qua toàn chuỗi, một ca cố tình vi phạm từng cổng bị bắt, một ca hợp lệ được nhận, và hồ sơ rõ phần chưa được kiểm. Đây là mục tiêu áp dụng ở dự án của xưởng, không phải tuyên bố `stored` đã dựng hay benchmark các công cụ đó.

## 7. Nguồn chuẩn và tuyến đọc chéo

- Nguồn gốc từng claim nằm ở permalink full SHA ngay trong hồ sơ; tham khảo mô hình gốc [C4](https://c4model.com/) và đặc tả [OpenAPI](https://spec.openapis.org/oas/latest.html) để chọn đúng phiên bản trước tích hợp. Hai trang chuẩn là đường tra cứu bổ sung, không được dùng để nâng mức kiểm vượt các file đã đọc ở đây.
- [Mục 04](../04-protocols-standards/README.md): phiên bản wire/conformance cho MCP/A2A; khác compatibility của API nghiệp vụ.
- [Mục 09](../09-engineering-checklists/README.md): checklist quyết định; [mục 13](../13-dev-stack-devops/README.md): toolchain; [mục 23](../23-own-repos-lessons/README.md): bài học repo chủ kho.
- [Mục 28](../28-product-discovery-experimentation/README.md): nhu cầu và phép đo sản phẩm; mục 30/34 bổ sung nghiệm thu runtime và data/identity.

<a id="anhkysuai-2026-11-23"></a>

## Đánh giá từ kho Anh Kỹ Sư AI — 23/11/2026

Phần này có **2 hồ sơ hoặc phạm vi đối chiếu** từ [nguồn tuyển chọn](https://anhkysuai.com/kho/). [Bảng đủ 1.295 repo](../data/collections/anhkysuai-kho.json) ghi trạng thái đối chiếu từng link; [danh sách URL](../data/collections/anhkysuai-kho-links.txt) phục vụ tra cứu. Nguồn tuyển chọn giúp phát hiện repo; đánh giá bên dưới dựa trên clone và permalink upstream cùng metadata GitHub ngày 2026-11-23.

Mức `docs-read`/`code-read` chỉ áp dụng phạm vi ghi tại mỗi hồ sơ. Chưa cài, build, chạy test hay benchmark mã upstream. Giấy phép có thể tách theo code, model, nội dung, asset hoặc bản enterprise; con số/tuyên bố của tác giả chưa được tái lập nếu không có ghi chú khác.

<a id="anhkysuai-2026-11-23-microsoft-api-guidelines"></a>

### api-guidelines

**Repo:** [microsoft/api-guidelines](https://github.com/microsoft/api-guidelines) · **License:** CC-BY-4.0 · **★ 23,353 (GitHub API, 2026-11-23)**

**Mục đích:** Hướng dẫn thiết kế REST API của Microsoft, có nhánh hướng dẫn riêng cho Azure và Microsoft Graph.

**Giá trị:** Tham khảo cách thống nhất quy ước API và tách yêu cầu chung khỏi bối cảnh dịch vụ cụ thể.

**Giới hạn:** Đây là tài liệu định hướng của một tổ chức; cần chọn quy tắc phù hợp với hệ thống đang xây, không áp nguyên bộ Azure/Graph cho mọi API.

**Cách tham khảo/tích hợp:** Chọn quy tắc phù hợp bối cảnh API, chuyển thành hợp đồng có ví dụ và kiểm tương thích trước áp dụng cho dịch vụ.

**Lựa chọn để đối chiếu:** [zalando/restful-api-guidelines](https://github.com/zalando/restful-api-guidelines) · [microsoft/cloud-design-patterns](https://github.com/microsoft/cloud-design-patterns). Đây là ứng viên so sánh theo tác vụ; mức phù hợp cần kiểm theo hồ sơ và phiên bản riêng.

**Bằng chứng:** `docs-read`, ngày 2026-11-23, commit [`1c58ca7f1eb51768cb4e21facd6ce0154ee4db64`](https://github.com/microsoft/api-guidelines/commit/1c58ca7f1eb51768cb4e21facd6ce0154ee4db64), ngày commit 2026-10-30. Đã clone và đọc chọn lọc phần giới thiệu, cách dùng, giới hạn, license, metadata manifest và CI hiện diện. Chưa kiểm đầy đủ implementation hoặc chạy upstream; các số đo của tác giả chưa được tái lập.

**Nguồn:** [README.md](https://github.com/microsoft/api-guidelines/blob/1c58ca7f1eb51768cb4e21facd6ce0154ee4db64/README.md) · [license.txt](https://github.com/microsoft/api-guidelines/blob/1c58ca7f1eb51768cb4e21facd6ce0154ee4db64/license.txt) · [metadata GitHub](https://api.github.com/repos/microsoft/api-guidelines).

<a id="anhkysuai-2026-11-23-googlecloudplatform-microservices-demo"></a>

### microservices-demo

**Repo:** [GoogleCloudPlatform/microservices-demo](https://github.com/GoogleCloudPlatform/microservices-demo) · **License:** Apache-2.0 · **★ 21,208 (GitHub API, 2026-11-23)**

**Mục đích:** Online Boutique: ứng dụng thương mại điện tử mẫu minh họa microservices trên Kubernetes.

**Giá trị:** Có thể học cách nối nhiều dịch vụ, gRPC và quan sát hệ thống qua một luồng mua hàng giả lập.

**Giới hạn:** Đây là demo và nhiều hướng dẫn gắn sản phẩm Google Cloud; cần đánh giá chi phí, tài khoản, dữ liệu và cấu hình triển khai riêng trước dùng ngoài môi trường học.

**Cách tham khảo/tích hợp:** Chọn bài theo mục tiêu, thực hành lại trên môi trường riêng và kiểm bằng bài chuyển giao; khi dùng lại nội dung phải đối chiếu giấy phép đúng phạm vi.

**Lựa chọn để đối chiếu:** [docker/awesome-compose](https://github.com/docker/awesome-compose) · [microsoft/eShop](https://github.com/microsoft/eShop). Đây là ứng viên so sánh theo tác vụ; mức phù hợp cần kiểm theo hồ sơ và phiên bản riêng.

**Bằng chứng:** `docs-read`, ngày 2026-11-23, commit [`c7cb6d5bfd6ea3aed768634ebbcb98cb7a523712`](https://github.com/GoogleCloudPlatform/microservices-demo/commit/c7cb6d5bfd6ea3aed768634ebbcb98cb7a523712), ngày commit 2026-10-27. Đã clone và đọc chọn lọc phần giới thiệu, cách dùng, giới hạn, license, metadata manifest và CI hiện diện. Chưa kiểm đầy đủ implementation hoặc chạy upstream; các số đo của tác giả chưa được tái lập.

**Nguồn:** [README.md](https://github.com/GoogleCloudPlatform/microservices-demo/blob/c7cb6d5bfd6ea3aed768634ebbcb98cb7a523712/README.md) · [LICENSE](https://github.com/GoogleCloudPlatform/microservices-demo/blob/c7cb6d5bfd6ea3aed768634ebbcb98cb7a523712/LICENSE) · [.github/workflows/ci-pr.yaml](https://github.com/GoogleCloudPlatform/microservices-demo/blob/c7cb6d5bfd6ea3aed768634ebbcb98cb7a523712/.github/workflows/ci-pr.yaml) · [metadata GitHub](https://api.github.com/repos/GoogleCloudPlatform/microservices-demo).

<a id="chuyen-muc-2026-11-23"></a>

## Hồ sơ chuyển về từ mục khác — 23/11/2026

1 hồ sơ được chuyển khi chia lại catalog theo `data/taxonomy.json`. Nội dung, ngày kiểm và mức bằng chứng giữ nguyên như ở mục gốc.

<a id="chuyen-spectral"></a>

### Spectral

`stoplightio/spectral` · License: Apache-2.0 · ★ 3.247

Linter JSON/YAML, ruleset sẵn OpenAPI/AsyncAPI/Arazzo v1 (hỗ trợ Arazzo 1.1 chưa xác minh); CLI 6.17.0; ★ 2/11/2026 (GitHub search API), mục 05 §Nâng trần 2/11

**Hồ sơ gốc:** [mục 05](../05-low-code-llm-platforms/README.md) (bảng/đoạn chung, giữ nguyên tại chỗ).

<a id="chuan-hoa-2026-11-23"></a>

## Chuẩn hóa bằng chứng hồ sơ cũ — 23/11/2026

Các hồ sơ dưới đây có từ trước khi kho ghi mức kiểm. Ngày 2026-11-23 mỗi repo được clone nông tại commit ghi trong bảng, đọc LICENSE, README, manifest và CI (nếu có); không cài, build hay chạy mã upstream. Nhận định cũ ở phần trên giữ nguyên; chỗ nào khác với lần đọc này được ghi trong cột Nhận định. Số sao lấy qua GitHub search API cùng ngày.

<a id="ch-spectral"></a>

### Spectral

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/stoplightio/spectral |
| License | Apache-2.0 |
| Phiên bản đã đọc | `16aae2b6f4448e9bf1a5bbb093601149f0ae0ac2` (commit 2026-11-13) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE, package.json, .github/workflows/commit.yml; chưa chạy upstream |
| Bảo trì | active (commit mới nhất 2026-11-13) |
| Nhận định | Linter JSON/YAML theo ruleset tùy chỉnh, có ruleset dựng sẵn cho OpenAPI v2/3.0/3.1/3.2, AsyncAPI, Arazzo v1; monorepo yarn. |
| Nguồn | [README](https://github.com/stoplightio/spectral/blob/16aae2b6f4448e9bf1a5bbb093601149f0ae0ac2/README.md) · [LICENSE](https://github.com/stoplightio/spectral/blob/16aae2b6f4448e9bf1a5bbb093601149f0ae0ac2/LICENSE) · [manifest](https://github.com/stoplightio/spectral/blob/16aae2b6f4448e9bf1a5bbb093601149f0ae0ac2/package.json) · [workflow](https://github.com/stoplightio/spectral/blob/16aae2b6f4448e9bf1a5bbb093601149f0ae0ac2/.github/workflows/commit.yml) |

<a id="nt-2026-11-23"></a>

## Nâng trần theo khoảng trống — 23/11/2026

Phần này có các hồ sơ mới của đợt nâng trần: mười trinh sát tìm trên internet và GitHub những mảng mà chuyên mục còn thiếu hoặc chỉ có hồ sơ cũ, rồi mỗi repo được clone nông tại một commit cố định, đọc LICENSE, README, ít nhất một file triển khai thật và CI nếu có; không cài hay chạy mã upstream. Mô tả của trinh sát nhiều chỗ sai so với mã thật, và các chỗ đó được sửa ngay trong từng hồ sơ. Số sao lấy sau bằng GitHub search API nên có thể để trống.

<a id="nt-asyncapi-spec"></a>

### AsyncAPI Specification

| Thuộc tính | Giá trị |
|---|---|
| Repo | https://github.com/asyncapi/spec |
| License | Apache-2.0 |
| Phiên bản đã đọc | `41662743fe64189858f4076f27d2b1d9da6b3093` (commit 2026-10-27) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc LICENSE, NOTICE, spec/asyncapi.md (đầu file và mục Operation), embedded-examples-validation.js, ba workflow validate-examples, validate-embedded-examples, lint; chưa chạy upstream |
| Khoảng trống lấp | API design và kiểm hợp đồng (nửa event-driven: AsyncAPI) |
| Cơ chế đáng học | - Mô hình tách `channels` (nơi thông điệp đi qua), `operations` (action `send` hoặc `receive` trên channel) và `messages`, nên một tài liệu mô tả ứng dụng theo góc nhìn của chính nó (spec/asyncapi.md, mục Operation Object).<br>- Request-reply là phần của đặc tả: Operation Reply Object và Reply Address Object; kèm security scheme, traits và bindings theo giao thức (Kafka, MQTT, AMQP, WebSocket...).<br>- Ví dụ trong đặc tả được kiểm bằng máy: chú thích `asyncapi-example-tester` trước mỗi khối mã, script `embedded-examples-validation.js` phân tích bằng `@asyncapi/parser`.<br>- Thư mục `examples/` chứa tài liệu mẫu (Streetlights Kafka/MQTT, RPC, request-reply). |
| Tiêu chí và cách kiểm | CI (đã mở) kiểm ba thứ: `asyncapi validate` cho mọi file YAML trong examples (trừ social-media/common), kiểm ví dụ nhúng trong asyncapi.md bằng parser, và markdownlint cho asyncapi.md. Repo này không chứa JSON Schema hay bộ test conformance cho công cụ; schema nằm ở repo khác (chưa xác minh vì chưa mở). |
| Giới hạn và rủi ro | Đây là đặc tả chữ, không phải công cụ: cần parser, CLI hoặc generator khác để dùng. Nhánh đã đọc ghi phiên bản 3.1.0, nhiều hệ sinh thái vẫn dùng 2.6 hoặc 3.0 (chưa xác minh mức hỗ trợ của từng công cụ). Giữ ý rằng tài liệu AsyncAPI mô tả chứ không ép hợp đồng lúc chạy. Phần dùng ví dụ trong workflow `pull_request_target` là chi tiết CI của upstream, không ảnh hưởng người dùng. Trinh sát ghi Apache-2.0: đúng. |
| So với | openapitools-openapi-generator và spectral (phía OpenAPI), faststream (cùng lô) |
| Nguồn | [LICENSE](https://github.com/asyncapi/spec/blob/41662743fe64189858f4076f27d2b1d9da6b3093/LICENSE) · [NOTICE](https://github.com/asyncapi/spec/blob/41662743fe64189858f4076f27d2b1d9da6b3093/NOTICE) · [spec/asyncapi.md](https://github.com/asyncapi/spec/blob/41662743fe64189858f4076f27d2b1d9da6b3093/spec/asyncapi.md) · [scripts/validation/embedded-examples-validation.js](https://github.com/asyncapi/spec/blob/41662743fe64189858f4076f27d2b1d9da6b3093/scripts/validation/embedded-examples-validation.js) · [.github/workflows/validate-examples.yml](https://github.com/asyncapi/spec/blob/41662743fe64189858f4076f27d2b1d9da6b3093/.github/workflows/validate-examples.yml) · [.github/workflows/validate-embedded-examples.yml](https://github.com/asyncapi/spec/blob/41662743fe64189858f4076f27d2b1d9da6b3093/.github/workflows/validate-embedded-examples.yml) · [.github/workflows/lint.yml](https://github.com/asyncapi/spec/blob/41662743fe64189858f4076f27d2b1d9da6b3093/.github/workflows/lint.yml) |

<a id="nt-eventcatalog"></a>

### EventCatalog

| Thuộc tính | Giá trị |
|---|---|
| Repo | https://github.com/event-catalog/eventcatalog |
| License | BUSL-1.1 cho packages/core (chuyển MIT sau 4 năm); sdk, linter, fitness, cli, visualiser, exporters, connectors MIT |
| Phiên bản đã đọc | `ae660c8d15a78bc11e8e20eda72b181e6b528730` (commit 2026-11-23) |
| Kiểm chứng | 2026-11-23; code-read; đã đọc LICENSE, README, AGENTS.md, packages/core/package.json, LICENSE của sdk, linter/src/rules.ts, fitness/README.md, analytics/telemetry.ts và analytics.js, verify-build.yml; chưa chạy upstream |
| Khoảng trống lấp | Kiến trúc event-driven: catalog tài liệu domain, service, message, schema |
| Cơ chế đáng học | - Catalog là thư mục Markdown và frontmatter mô tả domain, service, event, command, query, channel, flow; công cụ dựng site Astro/React có trực quan hoá quan hệ (README, AGENTS.md).<br>- `@eventcatalog/linter` có registry quy tắc (`packages/linter/src/rules.ts`): schema/required-fields, valid-semver, unknown-field... mỗi quy tắc có mức mặc định error hoặc warn.<br>- `@eventcatalog/fitness`: viết fitness function kiểu kiến trúc bằng TypeScript (`defineFitnessFunction`, ví dụ mọi event phải có owner), chạy qua `eventcatalog fitness check`; README nói rõ chỉ kiểm kiến trúc được tài liệu hoá, không kiểm hệ thống đang chạy.<br>- `@eventcatalog/sdk` (MIT) đọc ghi catalog bằng mã; có máy chủ MCP và `llms.txt` tuỳ chọn. |
| Tiêu chí và cách kiểm | verify-build.yml (đã mở) chạy `pnpm test:ci`, `pnpm run check`, đóng gói các package, cài vào catalog ví dụ rồi `eventcatalog generate` và `build`, kiểm SSR smoke và kích thước build. Chưa chạy lại; fitness và linter là kiểm bằng máy khi người dùng đưa vào CI. |
| Giới hạn và rủi ro | License: trinh sát ghi NOASSERTION, thực tế là Business Source License 1.1 tuỳ biến cho `packages/core` (bản 5.0 trở lên), không phải mã nguồn mở theo OSI, nên `open_source` đặt false. Dùng sản xuất miễn phí chỉ khi thuộc nhóm Free Use: cá nhân dùng riêng, tổ chức doanh thu dưới 10 triệu USD và vốn huy động dưới 10 triệu USD, tài liệu hoá dự án mã nguồn mở công khai, trường học, hoặc trong 60 ngày đánh giá; dùng trong CI cho catalog nội bộ và cho AI agent cũng tính là dùng sản xuất; Hosted Offering bị hạn chế. Change License MIT sau 4 năm kể từ bản phát hành đầu của dòng phiên bản. Telemetry bật mặc định cho `dev` và `build` (gửi lệnh, mã catalog, số lượng tài nguyên, hash nội dung và cờ tính năng tới dịch vụ phân tích); tắt bằng `telemetry: false`, `EVENTCATALOG_TELEMETRY_DISABLED` hoặc `DO_NOT_TRACK`; có thêm phân tích tuỳ chọn cho EventCatalog Cloud. Cần đọc LICENSE đầy đủ và FAQ của tác giả trước khi dùng trong công ty. |
| So với | structurizr, backstage-techdocs, asyncapi-spec và faststream (cùng lô) |
| Nguồn | [LICENSE](https://github.com/event-catalog/eventcatalog/blob/ae660c8d15a78bc11e8e20eda72b181e6b528730/LICENSE) · [README.md](https://github.com/event-catalog/eventcatalog/blob/ae660c8d15a78bc11e8e20eda72b181e6b528730/README.md) · [AGENTS.md](https://github.com/event-catalog/eventcatalog/blob/ae660c8d15a78bc11e8e20eda72b181e6b528730/AGENTS.md) · [packages/core/package.json](https://github.com/event-catalog/eventcatalog/blob/ae660c8d15a78bc11e8e20eda72b181e6b528730/packages/core/package.json) · [packages/sdk/LICENSE](https://github.com/event-catalog/eventcatalog/blob/ae660c8d15a78bc11e8e20eda72b181e6b528730/packages/sdk/LICENSE) · [packages/linter/src/rules.ts](https://github.com/event-catalog/eventcatalog/blob/ae660c8d15a78bc11e8e20eda72b181e6b528730/packages/linter/src/rules.ts) · [packages/fitness/README.md](https://github.com/event-catalog/eventcatalog/blob/ae660c8d15a78bc11e8e20eda72b181e6b528730/packages/fitness/README.md) · [packages/core/src/analytics/telemetry.ts](https://github.com/event-catalog/eventcatalog/blob/ae660c8d15a78bc11e8e20eda72b181e6b528730/packages/core/src/analytics/telemetry.ts) · [packages/core/src/analytics/analytics.js](https://github.com/event-catalog/eventcatalog/blob/ae660c8d15a78bc11e8e20eda72b181e6b528730/packages/core/src/analytics/analytics.js) · [.github/workflows/verify-build.yml](https://github.com/event-catalog/eventcatalog/blob/ae660c8d15a78bc11e8e20eda72b181e6b528730/.github/workflows/verify-build.yml) |

<a id="nt-vacuum"></a>

### vacuum (OpenAPI, AsyncAPI, Arazzo linter)

| Thuộc tính | Giá trị |
|---|---|
| Repo | https://github.com/daveshanley/vacuum |
| License | MIT |
| Phiên bản đã đọc | `5954963af688f1a7095e7df09acec0ca8c46a2b8` (commit 2026-11-21) |
| Kiểm chứng | 2026-11-23; code-read; đã đọc LICENSE, README.md, ARAZZO.md, cmd/exit_codes.go, cmd/update_check.go, rulesets/arazzo_rules.go, .github/workflows/build.yaml; chưa chạy upstream |
| Khoảng trống lấp | Đặc tả workflow API (Arazzo) và cổng kiểm máy cho hợp đồng API |
| Cơ chế đáng học | - Linter Go một binary cho OpenAPI, AsyncAPI, JSON Schema và Arazzo 1.0/1.1; tự nhận dạng tài liệu Arazzo và chọn ruleset `arazzo-recommended` (`ARAZZO.md`).<br>- `rulesets/arazzo_rules.go` gói kết quả của `libopenapi-validator` thành các rule thường (structure, duplicate-id, reference, parameter, expression, selector, dependency chu trình, input schema, source type) với vị trí và JSONPath; chỉ validate, không thực thi workflow.<br>- Mã thoát cố định cho CI trong `cmd/exit_codes.go`: 0 sạch, 1 có vi phạm tới ngưỡng, 2 lỗi đầu vào/công cụ; cờ `--fail-severity` chọn ngưỡng (error, warn, info, hint, none). |
| Tiêu chí và cách kiểm | Cổng kiểm bằng mã thoát và ngưỡng severity, tất định, chạy offline (README). `build.yaml` chạy `go test` với coverage và build, dùng `-tags html_report_ui`, kiểm `go mod tidy` sạch; mình chưa chạy. |
| Giới hạn và rủi ro | MIT (dòng bản quyền 2022-2023 trong LICENSE nhưng header file 2026, không ảnh hưởng điều khoản). Có kiểm tra bản cập nhật qua mạng (`cmd/update_check.go`, cache cục bộ); mình không đọc kỹ điều kiện tắt, nên cần kiểm trước khi chạy trong môi trường cô lập. Arazzo mặc định cho phép tra cứu nguồn qua file và HTTP(S) (ARAZZO.md), cần cân nhắc khi lint tài liệu không tin cậy. Khoảng trống trinh sát nêu có "Serverless Workflow" nhưng mình không thấy hỗ trợ nó trong các file đã đọc: chỉ Arazzo, OpenAPI, AsyncAPI, JSON Schema. |
| So với | spectral, arazzo-specification, schemathesis |
| Nguồn | [LICENSE](https://github.com/daveshanley/vacuum/blob/5954963af688f1a7095e7df09acec0ca8c46a2b8/LICENSE) · [README.md](https://github.com/daveshanley/vacuum/blob/5954963af688f1a7095e7df09acec0ca8c46a2b8/README.md) · [ARAZZO.md](https://github.com/daveshanley/vacuum/blob/5954963af688f1a7095e7df09acec0ca8c46a2b8/ARAZZO.md) · [exit_codes.go](https://github.com/daveshanley/vacuum/blob/5954963af688f1a7095e7df09acec0ca8c46a2b8/cmd/exit_codes.go) · [update_check.go](https://github.com/daveshanley/vacuum/blob/5954963af688f1a7095e7df09acec0ca8c46a2b8/cmd/update_check.go) · [arazzo_rules.go](https://github.com/daveshanley/vacuum/blob/5954963af688f1a7095e7df09acec0ca8c46a2b8/rulesets/arazzo_rules.go) · [build.yaml](https://github.com/daveshanley/vacuum/blob/5954963af688f1a7095e7df09acec0ca8c46a2b8/.github/workflows/build.yaml) |

<a id="nt-microcks"></a>

### Microcks

| Thuộc tính | Giá trị |
|---|---|
| Repo | https://github.com/microcks/microcks |
| License | Apache-2.0 (LICENSE). Không có trọng số |
| Phiên bản đã đọc | `1c38f795e1a9c45024faa0f527c4986931ff47f3` (commit 2026-11-13) |
| Kiểm chứng | 2026-11-23; code-read; đã đọc `README.md`, `LICENSE`, `ARCHITECTURE.md`, `commons/model/src/main/java/io/github/microcks/domain/TestRunnerType.java`, `webapp/src/main/java/io/github/microcks/util/openapi/OpenAPITestRunner.java`, `.github/workflows/api-check.yml`, `.github/workflows/build-verify.yml`, `AI-POLICY.md`; chưa chạy upstream |
| Khoảng trống lấp | Kiểm hợp đồng API: mock và test conformance từ OpenAPI, AsyncAPI, gRPC, GraphQL, Postman, SoapUI |
| Cơ chế đáng học | - Một tài sản (spec/collection) sinh cả mock sống và bộ test; `TestRunnerType` có HTTP, SOAP_HTTP, SOAP_UI, POSTMAN, OPEN_API_SCHEMA, ASYNC_API_SCHEMA, GRPC_PROTOBUF, GRAPHQL_SCHEMA.<br>- `OpenAPITestRunner.java`: gọi endpoint thật, so mã trạng thái và content-type với phản hồi mẫu khi `validateResponseCode`, rồi kiểm thân JSON theo JSON Schema của spec; lỗi vào `lastValidationErrors`, kết quả SUCCESS hoặc FAILURE.<br>- Kiến trúc (`ARCHITECTURE.md`): Spring Boot, MongoDB, Keycloak, Angular, các minion bất đồng bộ cho Kafka và giao thức tin nhắn.<br>- CLI/GitHub Action để nhúng vào CI nằm repo khác, không đọc trong lô này. |
| Tiêu chí và cách kiểm | Mỗi test trả cổng nhị phân SUCCESS/FAILURE theo runner; workflow `api-check.yml` chạy hằng ngày bộ test API với ảnh uber (JVM và native) và `build-verify.yml` build với JDK 25 (đã mở đầu hai file). Cổng conformance trong CI của người dùng cần CLI ở repo microcks-cli **(chưa xác minh)**. |
| Giới hạn và rủi ro | Mô tả của trinh sát hơi lệch: repo này là máy chủ/nền tảng; phần CI gate là CLI và action ở repo khác. Triển khai nặng (Java, MongoDB, Keycloak, tùy chọn Kafka). Có dòng chính sách dùng AI khi đóng góp (`AI-POLICY.md`) và `AICopilotRunnerService` sinh mẫu bằng AI **(chưa xác minh hành vi)**. Có badge CNCF Landscape trong README; bảo trì hoạt động (commit 2026-11-13). |
| So với | schemathesis (hồ sơ có sẵn, sinh ca kiểm tự động từ OpenAPI, không mock), spectral (lint spec, không gọi API), openapitools-openapi-generator (sinh code/stub). |
| Nguồn | [README.md](https://github.com/microcks/microcks/blob/1c38f795e1a9c45024faa0f527c4986931ff47f3/README.md) · [LICENSE](https://github.com/microcks/microcks/blob/1c38f795e1a9c45024faa0f527c4986931ff47f3/LICENSE) · [ARCHITECTURE.md](https://github.com/microcks/microcks/blob/1c38f795e1a9c45024faa0f527c4986931ff47f3/ARCHITECTURE.md) · [TestRunnerType.java](https://github.com/microcks/microcks/blob/1c38f795e1a9c45024faa0f527c4986931ff47f3/commons/model/src/main/java/io/github/microcks/domain/TestRunnerType.java) · [OpenAPITestRunner.java](https://github.com/microcks/microcks/blob/1c38f795e1a9c45024faa0f527c4986931ff47f3/webapp/src/main/java/io/github/microcks/util/openapi/OpenAPITestRunner.java) · [api-check.yml](https://github.com/microcks/microcks/blob/1c38f795e1a9c45024faa0f527c4986931ff47f3/.github/workflows/api-check.yml) · [build-verify.yml](https://github.com/microcks/microcks/blob/1c38f795e1a9c45024faa0f527c4986931ff47f3/.github/workflows/build-verify.yml) · [AI-POLICY.md](https://github.com/microcks/microcks/blob/1c38f795e1a9c45024faa0f527c4986931ff47f3/AI-POLICY.md) |
