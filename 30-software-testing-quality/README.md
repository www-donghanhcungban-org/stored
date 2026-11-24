# 30. Kiểm thử phần mềm và cổng chất lượng cho xưởng phát triển

<a id="testing-factory-2026-11-04"></a>

> Khảo sát 2026-11-04. Chuyên mục bổ sung lớp kiểm thử **hành vi phần mềm** bên cạnh eval LLM ở mục 07, checklist ở mục 09 và hạ tầng CI ở mục 13/32. Đã đọc LICENSE, code/callsite và CI của sáu upstream ghim dưới đây; không cài, build, chạy test hay phát tải vào dịch vụ. Không có kết quả benchmark do kho này thực hiện. Số sao để null vì không thu thập số liệu tin cậy trong đợt này.

## 1. Bài toán và phạm vi còn thiếu

Agent tạo được nhiều code làm tăng nhu cầu có oracle độc lập: **test phải có khả năng bác bỏ lời giải sai**. Một suite xanh chưa đủ nếu không thu được test, chỉ kiểm mock của chính implementation, cập nhật snapshot tự động hoặc bỏ qua integration. Xưởng cần quản từ ID yêu cầu tới test case, bộ dữ liệu, runner và artifact; không dùng một tỷ lệ coverage thay mọi tiêu chí chất lượng.

Cùng upstream đã có hồ sơ thì dẫn về đó: [Playwright](../11-browser-computer-use-sandbox/README.md), [StrykerJS](../13-dev-stack-devops/README.md), [axe-core/visual regression](../06-ui-ux-design/README.md#ui-factory-2026-11-04). Phần này thêm runner unit/property/integration/schema/load, không nhân bản catalog các thực thể đã có.

## 2. So sánh công cụ theo lớp lỗi

| Công cụ | Lớp và khác biệt | License đã đọc | Khi chọn | Giới hạn phải giữ |
|---|---|---|---|---|
| **Vitest** | Runner JS/TS theo Vite, Node/browser, coverage/reporters | MIT | Frontend/full-stack JS/TS đã dùng Vite; ghép Storybook addon-vitest | Browser Mode không tự là E2E toàn hệ; phải kiểm runtime và dependency theo phiên bản |
| **pytest** | Runner Python, fixture/parametrization/plugin, mã thoát phân loại | MIT | Backend Python, CLI và integration; giữ test nhỏ trước | Plugin/hook có thể thay hành vi; fixture không thay dữ liệu đại diện |
| **Hypothesis** | Sinh input theo strategy, tìm và thu nhỏ phản ví dụ | MPL-2.0 | Invariant, serialization, parser, tính tiền, state machine | Sinh dữ liệu tốt không tự sinh oracle đúng; không thay kiểm yêu cầu |
| **Testcontainers Python** | Dependency thật sống ngắn, lifecycle/wait strategy | Apache-2.0 | Postgres/Redis/queue khi mock hoặc SQLite khác production | Cần Docker/OCI daemon, image và tài nguyên; không phải sandbox chạy code không tin cậy |
| **Schemathesis** | Sinh request từ schema, kiểm response và chuỗi thao tác | MIT | Kiểm OpenAPI/GraphQL/gRPC có schema và môi trường thử | Gửi request thật có thể tạo/sửa/xóa dữ liệu; schema sai hoặc thiếu assertion nghiệp vụ vẫn bỏ sót lỗi |
| **Grafana k6** | Workload JS chạy trên Go runtime, đo metric và threshold | AGPL-3.0 | Load/soak và hồi quy latency/error theo workload | Không dùng toàn bộ API Node; license sửa/nhúng/phân phối cần xét đúng phạm vi; load generator cũng có giới hạn tài nguyên |

Đây là các lớp bổ sung nhau. Không cần cài tất cả cho mọi repo: Python không bắt buộc Vitest; ứng dụng nhỏ có thể dùng unit + vài integration/E2E đại diện trước khi thêm mutation hoặc load phân tán. Ngưỡng do rủi ro và SLO của sản phẩm quyết định.

## 3. Hồ sơ code-read tại phiên bản cụ thể

### 3.1 Vitest: runner và ca không thu được test

<a id="vitest-factory"></a>

Repo vitest-dev/vitest; SHA **289caab9cf9e9440e2a0be2d8783f7bd0f489a8b**, HEAD 2026-11-03. LICENSE MIT. Mã test-run.ts xác định thất bại khi module không ok/pending; khi không có module thì phụ thuộc **passWithNoTests**. Logger mô tả trường hợp cấu hình đó cho thoát 0 dù không có file test. Vì vậy CI phải kiểm **tập test dự kiến và số test đã chạy**, không bật passWithNoTests chỉ để làm pipeline xanh. Dùng chế độ run cho CI, reporter machine-readable và coverage theo vùng code quan trọng; giữ skipped/todo riêng. CI upstream có lint/typecheck và ma trận kiểm; chưa xác minh một lượt CI gần nhất hay tính tương thích của app cụ thể.

**Tích hợp đề xuất:** unit thuần cho logic → component/browser theo môi trường cần thiết → report JUnit/JSON và coverage của chính artifact ứng viên. Giữ snapshot có reviewer; không để agent tự duyệt snapshot mới do chính bản sửa tạo ra.

**Nguồn:** [LICENSE](https://github.com/vitest-dev/vitest/blob/289caab9cf9e9440e2a0be2d8783f7bd0f489a8b/LICENSE) · [packages/vitest/src/node/test-run.ts](https://github.com/vitest-dev/vitest/blob/289caab9cf9e9440e2a0be2d8783f7bd0f489a8b/packages/vitest/src/node/test-run.ts) · [packages/vitest/src/node/logger.ts](https://github.com/vitest-dev/vitest/blob/289caab9cf9e9440e2a0be2d8783f7bd0f489a8b/packages/vitest/src/node/logger.ts) · [.github/workflows/ci.yml](https://github.com/vitest-dev/vitest/blob/289caab9cf9e9440e2a0be2d8783f7bd0f489a8b/.github/workflows/ci.yml)

### 3.2 pytest: mã thoát và fixture có phạm vi

<a id="pytest-factory"></a>

Repo pytest-dev/pytest; SHA **8b005ed7f972987033ec34dc1e68b0635fb8142b**, HEAD 2026-11-02; MIT. _main thực hiện collection rồi runtestloop, trả TESTS_FAILED khi có failure và **NO_TESTS_COLLECTED = 5** khi không thu được test. Không dùng shell pipeline làm mất mã thoát, cũng không biến exit 5 thành thành công cho suite bắt buộc. Enum còn phân biệt interruption, internal/usage error; báo các kết quả đó như lỗi chạy kiểm, không như ứng dụng vượt qua test.

Fixture có scope và cleanup giúp quản dữ liệu/transaction/dependency theo vòng đời; người viết phải chọn phạm vi phù hợp, tránh session fixture làm test phụ thuộc thứ tự. Test plugin và cấu hình của sản phẩm trước khi áp kỳ vọng mã thoát cho mọi runner bọc ngoài. CI của pytest xây package và kiểm ma trận Python/OS; đó là bằng chứng có cơ chế kiểm upstream, chưa chứng minh fixture của xưởng đúng.

**Nguồn:** [LICENSE](https://github.com/pytest-dev/pytest/blob/8b005ed7f972987033ec34dc1e68b0635fb8142b/LICENSE) · [pytest config](https://github.com/pytest-dev/pytest/blob/8b005ed7f972987033ec34dc1e68b0635fb8142b/src/_pytest/config/__init__.py) · [src/_pytest/main.py](https://github.com/pytest-dev/pytest/blob/8b005ed7f972987033ec34dc1e68b0635fb8142b/src/_pytest/main.py) · [src/_pytest/fixtures.py](https://github.com/pytest-dev/pytest/blob/8b005ed7f972987033ec34dc1e68b0635fb8142b/src/_pytest/fixtures.py) · [.github/workflows/test.yml](https://github.com/pytest-dev/pytest/blob/8b005ed7f972987033ec34dc1e68b0635fb8142b/.github/workflows/test.yml)

### 3.3 Hypothesis: invariant và phản ví dụ giữ lại

<a id="hypothesis-factory"></a>

Repo HypothesisWorks/hypothesis; SHA **535f94db57d2248d4c0f799f319563c5c7fbbdbb**, HEAD 2026-11-03; MPL-2.0 theo LICENSE.txt, phần bên thứ ba có ghi chú riêng. Đọc settings, database và tutorial replay: example database lưu các trường hợp hữu ích để chạy lại; **không phải bản đặc tả đầy đủ của mọi lỗi đã biết**. Tài liệu khuyên dùng example rõ ràng cho regression quan trọng thay vì chỉ dựa cache. Ghim phiên bản Hypothesis, giữ phản ví dụ tối giản dưới dạng fixture/assertion và report settings/seed khi có; không hứa cùng seed tái tạo mọi bản sau nâng dependency.

Ví dụ thuộc tính phù hợp: decode(encode(x)) giữ dữ liệu theo miền đã khai báo; tổng tiền phân bổ bảo toàn theo quy tắc làm tròn; thao tác bị từ chối không đổi trạng thái. Phải nêu miền input và invariant nghiệp vụ độc lập với implementation; test cùng một hàm viết lại bằng công thức sai giống nhau vẫn có thể xanh. Settings về deadline/max_examples/derandomize cần chọn theo suite; timeout không phải assertion tính đúng đắn.

**Nguồn:** [LICENSE.txt](https://github.com/HypothesisWorks/hypothesis/blob/535f94db57d2248d4c0f799f319563c5c7fbbdbb/LICENSE.txt) · [hypothesis/src/hypothesis/_settings.py](https://github.com/HypothesisWorks/hypothesis/blob/535f94db57d2248d4c0f799f319563c5c7fbbdbb/hypothesis/src/hypothesis/_settings.py) · [hypothesis/src/hypothesis/database.py](https://github.com/HypothesisWorks/hypothesis/blob/535f94db57d2248d4c0f799f319563c5c7fbbdbb/hypothesis/src/hypothesis/database.py) · [hypothesis/docs/tutorial/replaying-failures.rst](https://github.com/HypothesisWorks/hypothesis/blob/535f94db57d2248d4c0f799f319563c5c7fbbdbb/hypothesis/docs/tutorial/replaying-failures.rst) · [.github/workflows/main.yml](https://github.com/HypothesisWorks/hypothesis/blob/535f94db57d2248d4c0f799f319563c5c7fbbdbb/.github/workflows/main.yml)

### 3.4 Testcontainers Python: integration với dependency thật

<a id="testcontainers-python-factory"></a>

Repo testcontainers/testcontainers-python; SHA **6146aa1170f415fcc825ed9bddc4eacbeb937a12**, HEAD 2026-10-07; Apache-2.0. Container.start khởi tạo Ryuk khi được bật, tạo container và gọi wait strategy; context manager có cleanup khi khởi động lỗi. PostgresContainer kiểm readiness qua truy vấn psql, mạnh hơn chỉ thấy PID/port. **Readiness của DB chưa chứng minh migration và nghiệp vụ ứng dụng đúng**: suite phải áp migration, ghi/đọc/query ranh giới và test transaction riêng.

Snapshot đọc cho thấy testcontainers.postgres đã deprecated, module mới là **testcontainers.community.postgres**; constructor PostgresContainer mặc định image **postgres:latest**. Khi tích hợp phải ghim image version/digest theo DB được hỗ trợ; không chép default latest rồi gọi môi trường tái lập. Ryuk có volume mapping Docker socket và quyền tùy cấu hình; chỉ dùng trong runner CI có phạm vi phù hợp, không coi nó là chỗ cô lập agent khỏi host. Chưa chạy Docker hay kiểm tương thích rootless/remote daemon.

**Nguồn:** [LICENSE.txt](https://github.com/testcontainers/testcontainers-python/blob/6146aa1170f415fcc825ed9bddc4eacbeb937a12/LICENSE.txt) · [src/testcontainers/core/container.py](https://github.com/testcontainers/testcontainers-python/blob/6146aa1170f415fcc825ed9bddc4eacbeb937a12/src/testcontainers/core/container.py) · [src/testcontainers/postgres.py](https://github.com/testcontainers/testcontainers-python/blob/6146aa1170f415fcc825ed9bddc4eacbeb937a12/src/testcontainers/postgres.py) · [Postgres community module](https://github.com/testcontainers/testcontainers-python/blob/6146aa1170f415fcc825ed9bddc4eacbeb937a12/src/testcontainers/community/postgres/__init__.py) · [.github/workflows/ci-core.yml](https://github.com/testcontainers/testcontainers-python/blob/6146aa1170f415fcc825ed9bddc4eacbeb937a12/.github/workflows/ci-core.yml)

### 3.5 Schemathesis: schema là nguồn sinh test, vẫn cần oracle nghiệp vụ

<a id="schemathesis-factory"></a>

Repo schemathesis/schemathesis; SHA **8033ef464ac7d1d12b527a6de5952defad2760d0**, HEAD 2026-11-04; MIT. README mô tả OpenAPI/GraphQL/gRPC và stateful sequences; đường checks.py chạy registry check, có hook/custom checks, not_a_server_error và max_response_time. Đọc thêm OpenAPI checks để phân biệt response-schema/status/content-type conformance với một assertion nghiệp vụ tự viết.

Giá trị: tạo dữ liệu biên và chuỗi request khó viết tay, lưu report/reproducer cho bug; bổ sung contract lint/diff ở mục 29. Giới hạn: schema cho phép một câu trả lời sai về tiền/quyền thì conformance vẫn có thể qua. Bộ ca hai principal/tenant và thay đổi trạng thái cần có kỳ vọng độc lập. README cảnh báo request tạo/sửa/xóa dữ liệu: dùng môi trường thử với tenant/dataset dùng xong được, giới hạn tốc độ và credential tối thiểu. Không quét production từ một ví dụ quickstart. Đợt này chưa xác minh tính năng BOLA/coverage toàn diện hay chạy request thật.

**Nguồn:** [LICENSE](https://github.com/schemathesis/schemathesis/blob/8033ef464ac7d1d12b527a6de5952defad2760d0/LICENSE) · [README.md](https://github.com/schemathesis/schemathesis/blob/8033ef464ac7d1d12b527a6de5952defad2760d0/README.md) · [src/schemathesis/checks.py](https://github.com/schemathesis/schemathesis/blob/8033ef464ac7d1d12b527a6de5952defad2760d0/src/schemathesis/checks.py) · [src/schemathesis/specs/openapi/checks.py](https://github.com/schemathesis/schemathesis/blob/8033ef464ac7d1d12b527a6de5952defad2760d0/src/schemathesis/specs/openapi/checks.py) · [.github/workflows/build.yml](https://github.com/schemathesis/schemathesis/blob/8033ef464ac7d1d12b527a6de5952defad2760d0/.github/workflows/build.yml) · [.github/workflows/test-hypothesis.yml](https://github.com/schemathesis/schemathesis/blob/8033ef464ac7d1d12b527a6de5952defad2760d0/.github/workflows/test-hypothesis.yml)

### 3.6 k6: check thất bại và threshold làm CI thất bại là hai việc khác

<a id="k6-factory"></a>

Repo grafana/k6; SHA **48d8dbbc12be13c42ab63a40b2221223b6e7cb4d**, HEAD 2026-11-03; AGPL-3.0 theo README/LICENSE.md. Hàm Check trả boolean và phát metric checks; **một check trả false không tự quyết định mã thoát của cả lượt chạy**. Đường run.go tính threshold cuối lượt và gắn ThresholdsHaveFailed khi vượt ngưỡng. Vì vậy muốn CI chặn khi check lỗi, phải đặt threshold phù hợp trên checks và các metric latency/error; chỉ in “checks failed” chưa là hợp đồng exit status.

Khai báo workload theo tốc độ đến/concurrency, tỷ lệ thao tác, kích thước payload/dữ liệu, warmup/cache và thời gian; báo p50/p95/p99 cùng số mẫu, lỗi và dropped iterations khi có. Ngưỡng như p95 < 500 ms chỉ là ví dụ nếu chưa có SLO được chủ sản phẩm chấp nhận; không biến thành chuẩn cho mọi dịch vụ. Giữ chức năng đúng dưới tải và giới hạn của generator bên cạnh throughput. Chưa chạy load hay xác minh hiệu năng của dịch vụ nào.

**Nguồn:** [LICENSE.md](https://github.com/grafana/k6/blob/48d8dbbc12be13c42ab63a40b2221223b6e7cb4d/LICENSE.md) · [README.md](https://github.com/grafana/k6/blob/48d8dbbc12be13c42ab63a40b2221223b6e7cb4d/README.md) · [internal/js/modules/k6/k6.go](https://github.com/grafana/k6/blob/48d8dbbc12be13c42ab63a40b2221223b6e7cb4d/internal/js/modules/k6/k6.go) · [internal/cmd/run.go](https://github.com/grafana/k6/blob/48d8dbbc12be13c42ab63a40b2221223b6e7cb4d/internal/cmd/run.go) · [metrics/thresholds.go](https://github.com/grafana/k6/blob/48d8dbbc12be13c42ab63a40b2221223b6e7cb4d/metrics/thresholds.go) · [.github/workflows/test.yml](https://github.com/grafana/k6/blob/48d8dbbc12be13c42ab63a40b2221223b6e7cb4d/.github/workflows/test.yml)

## 4. Pipeline kiểm theo rủi ro và bằng chứng

| Tầng | Artifact/kiểm chứng | Điều kiện cổng cần nêu | Phần vẫn cần kiểm khác |
|---|---|---|---|
| Static/type/build | Source + compiler/lint + artifact build | Đúng target, không che lỗi/allow-failure | Code biên dịch chưa chứng minh đúng hành vi |
| Unit/property | Requirement ID, fixture, assertion, phản ví dụ | Suite bắt được lỗi đã biết; test counts/skips rõ | Mock không thay transaction hoặc dependency thật |
| Integration | Dependency image digest, migration, dữ liệu thử, report | Đường ghi/đọc thực, transaction và lỗi dependency | Chưa bao phủ browser/khả năng dùng hoặc tải |
| API/schema/contract | Schema version, request/response/reproducer | Conformance + assertion quyền/nghiệp vụ | Schema không tự mô tả đủ mọi ràng buộc domain |
| Component/E2E/a11y | Story/route, persona/locale, trace/ảnh | Luồng critical và ca từ chối quyền chạy thật | Test tự động chưa chứng nhận accessibility toàn bộ |
| Mutation | Mutant/survivor, thời gian và phạm vi thay đổi | Survivor quan trọng được phân tích, không chỉ tăng coverage | Equivalent mutant và timeout cần phân loại |
| Load/soak/resilience | Workload, p95/p99/error, tài nguyên, recovery | Threshold có mã thoát + chức năng đúng trong điều kiện đã khai báo | Không suy khả năng chịu tải production từ máy/tải khác |

**Giữ một lỗi cố ý làm đối chứng:** ví dụ bỏ kiểm tra quyền, làm sai làm tròn hoặc bỏ một migration trong fixture riêng; cổng liên quan phải từ chối. Đây là kiểm hiệu lực của cổng, không yêu cầu sửa/xóa code production để làm demo. Agent viết code có thể đề xuất test, nhưng reviewer/requirement oracle cần độc lập với cùng giả định sai của implementation.

## 5. Độ tin cậy của suite, flakiness và dữ liệu thử

- **Không đánh đổi lỗi lấy xanh:** retry phải được ghi riêng first-attempt fail/retry-pass; quarantine có chủ, lý do và hạn xử lý, không biến thành bỏ qua vô thời hạn.
- **Đúng lần chạy:** report mang commit/build/config, suite/target, thời điểm, số executed/passed/failed/skipped/expected-failure. Artifact cũ hay suite không có test không đủ nghiệm thu.
- **Test data:** synthetic hoặc đã khử thông tin; seed/reset rõ, tenant tách biệt, clock/timezone được kiểm soát. Không sao chép dữ liệu khách hàng vào report CI công khai.
- **Coverage đúng nghĩa:** line/branch coverage cho biết code được thực thi; mutation và phản ví dụ giúp tìm assertion yếu; cả hai vẫn không thay thiếu yêu cầu. So sánh theo vùng thay đổi/rủi ro thay vì một con số toàn repo.
- **Snapshot có người duyệt:** diff hiển thị đúng phiên bản, font/browser/viewport/locale; ngưỡng so ảnh không được tăng chỉ để bỏ lỗi mới.
- **Ngân sách kiểm:** PR chạy bộ critical/unit và integration đại diện; suite sâu/load/resilience theo lịch hoặc trước release. Bản đồ chọn suite phải kiểm được để thay đổi nhạy cảm không lọt khỏi cổng bắt buộc.

## 6. Nối vào xưởng phát triển phần mềm

1. Product/BA chốt acceptance IDs và tác vụ critical → kiến trúc/API ở mục 29 xác định invariant và ranh giới.
2. Developer dùng unit/property ở vòng nhanh; QA/reviewer kiểm test có oracle độc lập và bổ sung ca âm.
3. Integration dùng dependency thật; API/schema và E2E kiểm sản phẩm đã ghép; eval LLM ở mục 07 tách khỏi test tất định.
4. Pipeline mục 32 lưu cùng artifact được test và phát hành; checklist mục 09 đối chiếu evidence thay lời tự khai.
5. SLO/incident mục 33 và migration/data mục 34 bổ sung phục hồi; lỗi thật được chuyển thành regression có version.

**Còn chưa xác minh:** chưa thực thi sáu công cụ, chưa chạy benchmark tương đối, chưa kiểm hết plugin/extension hoặc bản phát hành stable tương thích cho từng stack. Các ngưỡng và thiết kế pipeline ở đây là đề xuất kiến trúc; việc chọn/cài/chạy thuộc repo sản phẩm.

<a id="anhkysuai-2026-11-23"></a>

## Đánh giá từ kho Anh Kỹ Sư AI — 23/11/2026

Phần này có **23 hồ sơ hoặc phạm vi đối chiếu** từ [nguồn tuyển chọn](https://anhkysuai.com/kho/). [Bảng đủ 1.295 repo](../data/collections/anhkysuai-kho.json) ghi trạng thái đối chiếu từng link; [danh sách URL](../data/collections/anhkysuai-kho-links.txt) phục vụ tra cứu. Nguồn tuyển chọn giúp phát hiện repo; đánh giá bên dưới dựa trên clone và permalink upstream cùng metadata GitHub ngày 2026-11-23.

Mức `docs-read`/`code-read` chỉ áp dụng phạm vi ghi tại mỗi hồ sơ. Chưa cài, build, chạy test hay benchmark mã upstream. Giấy phép có thể tách theo code, model, nội dung, asset hoặc bản enterprise; con số/tuyên bố của tác giả chưa được tái lập nếu không có ghi chú khác.

<a id="anhkysuai-prettier-prettier"></a>

### Prettier

- **Repo:** [prettier/prettier](https://github.com/prettier/prettier).
- **Mục đích:** Formatter phân tích cú pháp rồi in lại mã với quy tắc thống nhất.
- **Điểm đáng dùng:** README mô tả cùng một formatter chạy khi lưu file, hook hoặc CI; manifest snapshot là bản 3.11.0-dev và yêu cầu Node >=22, nên không nhầm HEAD với release ổn định.
- **License:** MIT.
- **Giới hạn:** Format không chứng minh đúng logic; plugin và phiên bản khác nhau có thể tạo diff lớn. Chưa chạy kiểm tính bảo toàn ngữ nghĩa.
- **Tích hợp:** Ghim release, dùng --check trong CI và cấu hình editor dùng cùng phiên bản repo.
- **Đối chiếu:** [Biome](../13-dev-stack-devops/README.md) cho format/lint tích hợp; dprint cho nhiều formatter plugin; [ESLint](../30-software-testing-quality/README.md#anhkysuai-eslint-eslint) cho quy tắc lỗi mã bổ sung.
- **Mức kiểm chứng:** `docs-read` — Đọc các phần mô tả và giới hạn trong README, thông báo license, metadata manifest và cấu hình CI khi có; chưa đọc toàn bộ mã triển khai, chưa cài hoặc chạy kiểm thử upstream.
- **Snapshot:** kiểm ngày 2026-11-23; commit `7f583a828439022323342279911efe585d5d9981` (2026-11-23T17:44:58+08:00); 52,449 sao theo GitHub API ngày 2026-11-23. Sao không đại diện chất lượng.
- **Bằng chứng:** [README.md](https://github.com/prettier/prettier/blob/7f583a828439022323342279911efe585d5d9981/README.md) · [LICENSE](https://github.com/prettier/prettier/blob/7f583a828439022323342279911efe585d5d9981/LICENSE) · [package.json](https://github.com/prettier/prettier/blob/7f583a828439022323342279911efe585d5d9981/package.json) · [.github/workflows/_build.yml](https://github.com/prettier/prettier/blob/7f583a828439022323342279911efe585d5d9981/.github/workflows/_build.yml) · [GitHub API](https://api.github.com/repos/prettier/prettier).

<a id="anhkysuai-usebruno-bruno"></a>

### Bruno

- **Repo:** [usebruno/bruno](https://github.com/usebruno/bruno).
- **Mục đích:** API client desktop và CLI lưu collection bằng file cục bộ để quản lý bằng Git.
- **Điểm đáng dùng:** README snapshot dùng OpenCollection YAML và cung cấp CLI/container chạy collection trong CI; phù hợp chuyển ví dụ request thành artifact kiểm có phiên bản.
- **License:** MIT cho code; logo OpenMoji CC-BY-SA-4.0.
- **Giới hạn:** Có bản thương mại riêng; offline-only nói về lưu trữ collection, request vẫn gửi dữ liệu tới endpoint. Phải tách secret khỏi file được commit.
- **Tích hợp:** Lưu collection trong repo, truyền biến môi trường khi chạy CLI và kiểm exit code cùng assertion.
- **Đối chiếu:** Postman cho cộng tác dịch vụ; [Insomnia](../30-software-testing-quality/README.md#anhkysuai-kong-insomnia) cho API client; curl và test HTTP cho bộ kiểm nhỏ.
- **Mức kiểm chứng:** `docs-read` — Đọc các phần mô tả và giới hạn trong README, thông báo license, metadata manifest và cấu hình CI khi có; chưa đọc toàn bộ mã triển khai, chưa cài hoặc chạy kiểm thử upstream.
- **Snapshot:** kiểm ngày 2026-11-23; commit `2f65423c22a3005cab1a6c64bd5e0e010a500672` (2026-11-23T14:52:06+05:30); 48,512 sao theo GitHub API ngày 2026-11-23. Sao không đại diện chất lượng.
- **Bằng chứng:** [readme.md](https://github.com/usebruno/bruno/blob/2f65423c22a3005cab1a6c64bd5e0e010a500672/readme.md) · [license.md](https://github.com/usebruno/bruno/blob/2f65423c22a3005cab1a6c64bd5e0e010a500672/license.md) · [package.json](https://github.com/usebruno/bruno/blob/2f65423c22a3005cab1a6c64bd5e0e010a500672/package.json) · [.github/workflows/lint-checks.yml](https://github.com/usebruno/bruno/blob/2f65423c22a3005cab1a6c64bd5e0e010a500672/.github/workflows/lint-checks.yml) · [GitHub API](https://api.github.com/repos/usebruno/bruno).

<a id="anhkysuai-jestjs-jest"></a>

### Jest

- **Repo:** [jestjs/jest](https://github.com/jestjs/jest).
- **Mục đích:** Bộ chạy kiểm thử JavaScript với matcher, watch mode và snapshot.
- **Điểm đáng dùng:** README hướng dẫn cấu hình Babel, TypeScript và các bundler; watch chọn bài kiểm tra liên quan thay đổi, CI xây dựng JavaScript theo ma trận Node.
- **License:** MIT.
- **Giới hạn:** Snapshot cần được người duyệt đánh giá; transpile TypeScript không đồng nghĩa kiểm tra kiểu hay kiểm thử trình duyệt thật.
- **Tích hợp:** Dùng cho unit test của template, khóa môi trường Node và thêm tsc, kiểm thử trình duyệt khi có UI.
- **Đối chiếu:** [Vitest](../30-software-testing-quality/README.md#vitest-factory) cho dự án Vite; Mocha cho runner linh hoạt; [Playwright](../11-browser-computer-use-sandbox/README.md#playwright) cho luồng trình duyệt.
- **Mức kiểm chứng:** `docs-read` — Đọc các phần mô tả và giới hạn trong README, thông báo license, metadata manifest và cấu hình CI khi có; chưa đọc toàn bộ mã triển khai, chưa cài hoặc chạy kiểm thử upstream.
- **Snapshot:** kiểm ngày 2026-11-23; commit `aa88f7cf0bfc7a3a2efbfcab97914886b22d4454` (2026-11-11T09:33:55+09:00); 45,486 sao theo GitHub API ngày 2026-11-23. Sao không đại diện chất lượng.
- **Bằng chứng:** [README.md](https://github.com/jestjs/jest/blob/aa88f7cf0bfc7a3a2efbfcab97914886b22d4454/README.md) · [LICENSE](https://github.com/jestjs/jest/blob/aa88f7cf0bfc7a3a2efbfcab97914886b22d4454/LICENSE) · [package.json](https://github.com/jestjs/jest/blob/aa88f7cf0bfc7a3a2efbfcab97914886b22d4454/package.json) · [.github/workflows/test.yml](https://github.com/jestjs/jest/blob/aa88f7cf0bfc7a3a2efbfcab97914886b22d4454/.github/workflows/test.yml) · [GitHub API](https://api.github.com/repos/jestjs/jest).

<a id="anhkysuai-colinhacks-zod"></a>

### Zod

- **Repo:** [colinhacks/zod](https://github.com/colinhacks/zod).
- **Mục đích:** Schema validation JavaScript/TypeScript đồng thời suy luận kiểu dữ liệu.
- **Điểm đáng dùng:** Mã classic gọi core._safeParse; core chạy schema._zod.run, tách nhánh success và tạo error lười qua getter, rồi bỏ tham chiếu raw issues. Test lỗi kiểm tra custom map và refinement.
- **License:** MIT.
- **Giới hạn:** safeParse đồng bộ vẫn ném ZodAsyncError nếu schema trả Promise; phải dùng bản async. AOT/CSP và benchmark mới chỉ đọc tài liệu, chưa xác minh thực thi.
- **Tích hợp:** Đặt schema tại biên API, cấu hình và đầu vào template; kiểm thử dữ liệu sai và dùng refinement không có tác dụng phụ.
- **Đối chiếu:** Valibot cho schema mô-đun; Joi cho validation Node; Ajv cho JSON Schema.
- **Mức kiểm chứng:** `code-read` — Đọc classic/parse.ts, nhánh parse/safeParse và tạo lỗi trong core/parse.ts, các test lỗi tương ứng và workflow test; chưa kiểm tra compiler AOT hoặc mọi schema, chưa chạy test.
- **Snapshot:** kiểm ngày 2026-11-23; commit `d40c329910436e528d3c26cb1b9179e05abebf05` (2026-11-22T12:47:41-08:00); 44,394 sao theo GitHub API ngày 2026-11-23. Sao không đại diện chất lượng.
- **Bằng chứng:** [README.md](https://github.com/colinhacks/zod/blob/d40c329910436e528d3c26cb1b9179e05abebf05/README.md) · [LICENSE](https://github.com/colinhacks/zod/blob/d40c329910436e528d3c26cb1b9179e05abebf05/LICENSE) · [package.json](https://github.com/colinhacks/zod/blob/d40c329910436e528d3c26cb1b9179e05abebf05/package.json) · [.github/workflows/test.yml](https://github.com/colinhacks/zod/blob/d40c329910436e528d3c26cb1b9179e05abebf05/.github/workflows/test.yml) · [packages/zod/README.md](https://github.com/colinhacks/zod/blob/d40c329910436e528d3c26cb1b9179e05abebf05/packages/zod/README.md) · [packages/zod/package.json](https://github.com/colinhacks/zod/blob/d40c329910436e528d3c26cb1b9179e05abebf05/packages/zod/package.json) · [packages/zod/src/v4/classic/parse.ts](https://github.com/colinhacks/zod/blob/d40c329910436e528d3c26cb1b9179e05abebf05/packages/zod/src/v4/classic/parse.ts) · [packages/zod/src/v4/core/parse.ts](https://github.com/colinhacks/zod/blob/d40c329910436e528d3c26cb1b9179e05abebf05/packages/zod/src/v4/core/parse.ts) · [packages/zod/src/v4/classic/tests/error.test.ts](https://github.com/colinhacks/zod/blob/d40c329910436e528d3c26cb1b9179e05abebf05/packages/zod/src/v4/classic/tests/error.test.ts) · [GitHub API](https://api.github.com/repos/colinhacks/zod).

<a id="anhkysuai-psf-black"></a>

### Black

- **Repo:** [psf/black](https://github.com/psf/black).
- **Mục đích:** Formatter Python theo bộ quy tắc cố định để giảm tranh luận định dạng.
- **Điểm đáng dùng:** README nêu kiểm tra AST tương đương sau định dạng và tùy chọn --fast bỏ bước này; pyproject yêu cầu Python >=3.11.
- **License:** MIT.
- **Giới hạn:** Định dạng không chứng minh đúng nghiệp vụ; tùy chọn style ít, thay phiên bản có thể tạo diff lớn.
- **Tích hợp:** Khóa phiên bản và cấu hình pyproject, áp dụng lần chuẩn hóa riêng rồi dùng check trong CI.
- **Đối chiếu:** Ruff formatter cho bộ công cụ gọn; autopep8 cho chỉnh phong cách; [Prettier](../30-software-testing-quality/README.md#anhkysuai-prettier-prettier) cho mã web.
- **Mức kiểm chứng:** `docs-read` — Đọc các phần mô tả và giới hạn trong README, thông báo license, metadata manifest và cấu hình CI khi có; chưa đọc toàn bộ mã triển khai, chưa cài hoặc chạy kiểm thử upstream.
- **Snapshot:** kiểm ngày 2026-11-23; commit `a12e95913f5181f357f210207ea2c37f6b970174` (2026-11-19T22:55:03-07:00); 42,210 sao theo GitHub API ngày 2026-11-23. Sao không đại diện chất lượng.
- **Bằng chứng:** [README.md](https://github.com/psf/black/blob/a12e95913f5181f357f210207ea2c37f6b970174/README.md) · [LICENSE](https://github.com/psf/black/blob/a12e95913f5181f357f210207ea2c37f6b970174/LICENSE) · [pyproject.toml](https://github.com/psf/black/blob/a12e95913f5181f357f210207ea2c37f6b970174/pyproject.toml) · [.github/workflows/test.yml](https://github.com/psf/black/blob/a12e95913f5181f357f210207ea2c37f6b970174/.github/workflows/test.yml) · [GitHub API](https://api.github.com/repos/psf/black).

<a id="anhkysuai-koalaman-shellcheck"></a>

### ShellCheck

- **Repo:** [koalaman/shellcheck](https://github.com/koalaman/shellcheck).
- **Mục đích:** Phân tích tĩnh script bash/sh để tìm lỗi cú pháp, quoting và portability.
- **Điểm đáng dùng:** Chẩn đoán có mã SC và exit code tích hợp editor/CI; README phân biệt công cụ với formatter.
- **License:** GPL-3.0.
- **Giới hạn:** Không chứng minh lệnh chạy an toàn với mọi đầu vào hay điều kiện hệ thống; suppression cần lý do và vẫn phải thử script thực tế.
- **Tích hợp:** Gắn vào gate template shell, khai báo đúng dialect và kiểm thử các đường lỗi có tác dụng ghi.
- **Đối chiếu:** shfmt cho định dạng; [Semgrep](../12-ai-security-guardrails/README.md) cho rule tùy chỉnh; Bats cho hành vi shell.
- **Mức kiểm chứng:** `docs-read` — Đọc các phần mô tả và giới hạn trong README, thông báo license, metadata manifest và cấu hình CI khi có; chưa đọc toàn bộ mã triển khai, chưa cài hoặc chạy kiểm thử upstream.
- **Snapshot:** kiểm ngày 2026-11-23; commit `70f8c60a55cfd4a682196e6d84588dd5adf5d402` (2026-11-20T20:28:16-08:00); 40,374 sao theo GitHub API ngày 2026-11-23. Sao không đại diện chất lượng.
- **Bằng chứng:** [README.md](https://github.com/koalaman/shellcheck/blob/70f8c60a55cfd4a682196e6d84588dd5adf5d402/README.md) · [LICENSE](https://github.com/koalaman/shellcheck/blob/70f8c60a55cfd4a682196e6d84588dd5adf5d402/LICENSE) · [.github/workflows/build.yml](https://github.com/koalaman/shellcheck/blob/70f8c60a55cfd4a682196e6d84588dd5adf5d402/.github/workflows/build.yml) · [GitHub API](https://api.github.com/repos/koalaman/shellcheck).

<a id="anhkysuai-kong-insomnia"></a>

### Insomnia

- **Repo:** [Kong/insomnia](https://github.com/Kong/insomnia).
- **Mục đích:** API client và bộ công cụ thiết kế, chạy thử REST, GraphQL, gRPC và WebSocket.
- **Điểm đáng dùng:** Tài liệu phân biệt Local Vault, Git Sync, Cloud Sync và Private Environments; CLI hỗ trợ lint và test trong CI.
- **License:** Apache-2.0 cho mã repo; tính năng dịch vụ theo gói riêng.
- **Giới hạn:** Các mức cộng tác/Git Sync có điều kiện gói; lưu local không có nghĩa request không truyền dữ liệu ra API, cần quản lý secret.
- **Tích hợp:** Chuẩn hóa collection cho template API, chọn storage rõ ràng và dùng biến môi trường bí mật ngoài repo.
- **Đối chiếu:** [Bruno](../30-software-testing-quality/README.md#anhkysuai-usebruno-bruno) cho collection trong Git; [Hoppscotch](../08-awesome-lists-learning/README.md#6c52-api--dịch-vụ-dữ-liệu) cho API client web; Postman cho dịch vụ cộng tác.
- **Mức kiểm chứng:** `docs-read` — Đọc các phần mô tả và giới hạn trong README, thông báo license, metadata manifest và cấu hình CI khi có; chưa đọc toàn bộ mã triển khai, chưa cài hoặc chạy kiểm thử upstream.
- **Snapshot:** kiểm ngày 2026-11-23; commit `cd6f713e216f77ad59883d5c6ec64445d08564d0` (2026-11-23T09:03:00Z); 40,183 sao theo GitHub API ngày 2026-11-23. Sao không đại diện chất lượng.
- **Bằng chứng:** [README.md](https://github.com/Kong/insomnia/blob/cd6f713e216f77ad59883d5c6ec64445d08564d0/README.md) · [LICENSE](https://github.com/Kong/insomnia/blob/cd6f713e216f77ad59883d5c6ec64445d08564d0/LICENSE) · [package.json](https://github.com/Kong/insomnia/blob/cd6f713e216f77ad59883d5c6ec64445d08564d0/package.json) · [.github/workflows/test.yml](https://github.com/Kong/insomnia/blob/cd6f713e216f77ad59883d5c6ec64445d08564d0/.github/workflows/test.yml) · [GitHub API](https://api.github.com/repos/Kong/insomnia).

<a id="anhkysuai-seleniumhq-selenium"></a>

### Selenium

- **Repo:** [SeleniumHQ/selenium](https://github.com/SeleniumHQ/selenium).
- **Mục đích:** Hạ tầng tự động hóa trình duyệt theo W3C WebDriver.
- **Điểm đáng dùng:** API độc lập nền tảng/ngôn ngữ giúp kiểm tra browser thật; repo có nhiều binding và build Bazel, CI lint workflow/shell.
- **License:** Apache-2.0.
- **Giới hạn:** README chủ yếu hướng dẫn phát triển Selenium, không phải quy trình test ứng dụng hoàn chỉnh; cần quản lý driver/browser và các chờ trạng thái.
- **Tích hợp:** Dùng cho ma trận browser và hệ ngôn ngữ đã có, viết locator ổn định và giữ trace/log lỗi.
- **Đối chiếu:** [Playwright](../11-browser-computer-use-sandbox/README.md#playwright) cho E2E hiện đại; Cypress cho test web; [Puppeteer](../08-awesome-lists-learning/README.md#6c520-thu-thập-dữ-liệu--trình-duyệt-tự-động) cho điều khiển Chromium.
- **Mức kiểm chứng:** `docs-read` — Đọc các phần mô tả và giới hạn trong README, thông báo license, metadata manifest và cấu hình CI khi có; chưa đọc toàn bộ mã triển khai, chưa cài hoặc chạy kiểm thử upstream.
- **Snapshot:** kiểm ngày 2026-11-23; commit `4748ffdef0ff152221f1eb5b2a32e4fae757a57c` (2026-11-23T09:22:34Z); 34,607 sao theo GitHub API ngày 2026-11-23. Sao không đại diện chất lượng.
- **Bằng chứng:** [README.md](https://github.com/SeleniumHQ/selenium/blob/4748ffdef0ff152221f1eb5b2a32e4fae757a57c/README.md) · [LICENSE](https://github.com/SeleniumHQ/selenium/blob/4748ffdef0ff152221f1eb5b2a32e4fae757a57c/LICENSE) · [package.json](https://github.com/SeleniumHQ/selenium/blob/4748ffdef0ff152221f1eb5b2a32e4fae757a57c/package.json) · [.github/workflows/ci.yml](https://github.com/SeleniumHQ/selenium/blob/4748ffdef0ff152221f1eb5b2a32e4fae757a57c/.github/workflows/ci.yml) · [GitHub API](https://api.github.com/repos/SeleniumHQ/selenium).

<a id="anhkysuai-googlechrome-lighthouse"></a>

### Lighthouse

- **Repo:** [GoogleChrome/lighthouse](https://github.com/GoogleChrome/lighthouse).
- **Mục đích:** Audit trang web về hiệu năng và các thực hành phát triển.
- **Điểm đáng dùng:** CLI/module tách gather và audit, xuất report HTML hoặc định dạng máy; package yêu cầu Node >=22.19.
- **License:** Apache-2.0.
- **Giới hạn:** Điểm phòng thử phụ thuộc máy, mạng và throttling; không thay dữ liệu người dùng thật hoặc kiểm tra accessibility thủ công.
- **Tích hợp:** Dùng baseline cố định cho template, so regression qua nhiều lần và giữ report kèm cấu hình browser.
- **Đối chiếu:** WebPageTest cho phân tích tải; [Playwright](../11-browser-computer-use-sandbox/README.md#playwright) cho hành vi; [axe-core](../06-ui-ux-design/README.md) cho quy tắc accessibility.
- **Mức kiểm chứng:** `docs-read` — Đọc các phần mô tả và giới hạn trong README, thông báo license, metadata manifest và cấu hình CI khi có; chưa đọc toàn bộ mã triển khai, chưa cài hoặc chạy kiểm thử upstream.
- **Snapshot:** kiểm ngày 2026-11-23; commit `f482542ae0c5f05bcd1831906e7e4b4b1857ca4b` (2026-11-19T22:31:07-08:00); 31,193 sao theo GitHub API ngày 2026-11-23. Sao không đại diện chất lượng.
- **Bằng chứng:** [readme.md](https://github.com/GoogleChrome/lighthouse/blob/f482542ae0c5f05bcd1831906e7e4b4b1857ca4b/readme.md) · [LICENSE](https://github.com/GoogleChrome/lighthouse/blob/f482542ae0c5f05bcd1831906e7e4b4b1857ca4b/LICENSE) · [package.json](https://github.com/GoogleChrome/lighthouse/blob/f482542ae0c5f05bcd1831906e7e4b4b1857ca4b/package.json) · [.github/workflows/ci.yml](https://github.com/GoogleChrome/lighthouse/blob/f482542ae0c5f05bcd1831906e7e4b4b1857ca4b/.github/workflows/ci.yml) · [GitHub API](https://api.github.com/repos/GoogleChrome/lighthouse).

<a id="anhkysuai-square-leakcanary"></a>

### LeakCanary

- **Repo:** [square/leakcanary](https://github.com/square/leakcanary).
- **Mục đích:** Phát hiện rò rỉ bộ nhớ trong ứng dụng Android.
- **Điểm đáng dùng:** Tài liệu fundamentals giải thích ObjectWatcher giữ weak reference theo lifecycle, dump heap rồi Shark tìm trace và nhóm theo fingerprint.
- **License:** Apache-2.0.
- **Giới hạn:** Đối tượng retained ban đầu chỉ là nghi ngờ; dump heap làm dừng app tạm thời và có thể chứa dữ liệu nhạy cảm. Chưa chạy emulator.
- **Tích hợp:** Gắn vào build debug và test vòng đời activity/fragment, hạn chế chia sẻ heap dump và xác minh nguyên nhân trước sửa.
- **Đối chiếu:** Android Studio Memory Profiler cho phân tích thủ công; Perfetto cho tracing; Android lint cho lỗi tĩnh.
- **Mức kiểm chứng:** `docs-read` — Đọc các phần mô tả và giới hạn trong README, thông báo license, metadata manifest và cấu hình CI khi có; chưa đọc toàn bộ mã triển khai, chưa cài hoặc chạy kiểm thử upstream.
- **Snapshot:** kiểm ngày 2026-11-23; commit `eb60b0be53732aa016c79b7774b497770ad1e4f3` (2026-10-21T17:19:52+02:00); 30,009 sao theo GitHub API ngày 2026-11-23. Sao không đại diện chất lượng.
- **Bằng chứng:** [README.md](https://github.com/square/leakcanary/blob/eb60b0be53732aa016c79b7774b497770ad1e4f3/README.md) · [LICENSE.txt](https://github.com/square/leakcanary/blob/eb60b0be53732aa016c79b7774b497770ad1e4f3/LICENSE.txt) · [.github/workflows/main.yml](https://github.com/square/leakcanary/blob/eb60b0be53732aa016c79b7774b497770ad1e4f3/.github/workflows/main.yml) · [docs/fundamentals-how-leakcanary-works.md](https://github.com/square/leakcanary/blob/eb60b0be53732aa016c79b7774b497770ad1e4f3/docs/fundamentals-how-leakcanary-works.md) · [GitHub API](https://api.github.com/repos/square/leakcanary).

<a id="anhkysuai-pydantic-pydantic"></a>

### Pydantic

- **Repo:** [pydantic/pydantic](https://github.com/pydantic/pydantic).
- **Mục đích:** Validation dữ liệu Python qua type hint và model.
- **Điểm đáng dùng:** README phân biệt v1/v2 và module v1 hỗ trợ migration dần; manifest hiện yêu cầu Python >=3.11, CI build core nhiều target.
- **License:** MIT.
- **Giới hạn:** Validation/coercion không thay quy tắc nghiệp vụ hoặc authorization; Logfire quảng bá trong README là sản phẩm riêng.
- **Tích hợp:** Dùng tại biên API/config, đặt chính sách strict và trường dư rõ ràng, test dữ liệu sai cùng migration v1/v2.
- **Đối chiếu:** msgspec cho cấu trúc dữ liệu nhanh; Marshmallow cho serialization; JSON Schema cho hợp đồng đa ngôn ngữ.
- **Mức kiểm chứng:** `docs-read` — Đọc các phần mô tả và giới hạn trong README, thông báo license, metadata manifest và cấu hình CI khi có; chưa đọc toàn bộ mã triển khai, chưa cài hoặc chạy kiểm thử upstream.
- **Snapshot:** kiểm ngày 2026-11-23; commit `bcadb56a3808ebfba332a868d8fcc4b684f055cc` (2026-11-23T11:01:36+01:00); 29,634 sao theo GitHub API ngày 2026-11-23. Sao không đại diện chất lượng.
- **Bằng chứng:** [README.md](https://github.com/pydantic/pydantic/blob/bcadb56a3808ebfba332a868d8fcc4b684f055cc/README.md) · [LICENSE](https://github.com/pydantic/pydantic/blob/bcadb56a3808ebfba332a868d8fcc4b684f055cc/LICENSE) · [pyproject.toml](https://github.com/pydantic/pydantic/blob/bcadb56a3808ebfba332a868d8fcc4b684f055cc/pyproject.toml) · [.github/workflows/ci.yml](https://github.com/pydantic/pydantic/blob/bcadb56a3808ebfba332a868d8fcc4b684f055cc/.github/workflows/ci.yml) · [GitHub API](https://api.github.com/repos/pydantic/pydantic).

<a id="anhkysuai-sharkdp-hyperfine"></a>

### Hyperfine

- **Repo:** [sharkdp/hyperfine](https://github.com/sharkdp/hyperfine).
- **Mục đích:** Benchmark lệnh qua nhiều lần chạy và xuất thống kê.
- **Điểm đáng dùng:** Warmup, prepare, phát hiện outlier, quét tham số và JSON/CSV giúp so build tool; README bản đọc nói mặc định chạy trực tiếp, -S bật shell.
- **License:** MIT OR Apache-2.0.
- **Giới hạn:** Kết quả phụ thuộc cache/nhiễu hệ thống; lệnh sẽ được chạy lặp nên phải giới hạn tác dụng phụ và giữ dữ liệu thử cố định.
- **Tích hợp:** Benchmark tác vụ build trong workspace riêng, ghi máy/toolchain và tách cold/warm run để so template công bằng.
- **Đối chiếu:** Criterion cho benchmark Rust; pytest-benchmark cho Python; time cho đo sơ bộ.
- **Mức kiểm chứng:** `docs-read` — Đọc các phần mô tả và giới hạn trong README, thông báo license, metadata manifest và cấu hình CI khi có; chưa đọc toàn bộ mã triển khai, chưa cài hoặc chạy kiểm thử upstream.
- **Snapshot:** kiểm ngày 2026-11-23; commit `c5161524980522320c7d3425e714cc0965a869a5` (2026-10-12T10:33:47+02:00); 29,338 sao theo GitHub API ngày 2026-11-23. Sao không đại diện chất lượng.
- **Bằng chứng:** [README.md](https://github.com/sharkdp/hyperfine/blob/c5161524980522320c7d3425e714cc0965a869a5/README.md) · [LICENSE-APACHE](https://github.com/sharkdp/hyperfine/blob/c5161524980522320c7d3425e714cc0965a869a5/LICENSE-APACHE) · [LICENSE-MIT](https://github.com/sharkdp/hyperfine/blob/c5161524980522320c7d3425e714cc0965a869a5/LICENSE-MIT) · [pyproject.toml](https://github.com/sharkdp/hyperfine/blob/c5161524980522320c7d3425e714cc0965a869a5/pyproject.toml) · [Cargo.toml](https://github.com/sharkdp/hyperfine/blob/c5161524980522320c7d3425e714cc0965a869a5/Cargo.toml) · [.github/workflows/CICD.yml](https://github.com/sharkdp/hyperfine/blob/c5161524980522320c7d3425e714cc0965a869a5/.github/workflows/CICD.yml) · [GitHub API](https://api.github.com/repos/sharkdp/hyperfine).

<a id="anhkysuai-eslint-eslint"></a>

### ESLint

- **Repo:** [eslint/eslint](https://github.com/eslint/eslint).
- **Mục đích:** Phân tích mẫu lỗi và quy tắc trong mã JavaScript theo AST.
- **Điểm đáng dùng:** Espree parser và rule plugin, mức off/warn/error gắn với exit code; snapshot dùng eslint.config.js và dòng Node hiện hành.
- **License:** MIT.
- **Giới hạn:** TypeScript/cú pháp thử nghiệm cần parser/plugin phù hợp; lint không thay test, warn mặc định không làm thất bại exit code.
- **Tích hợp:** Chốt bộ rule theo template, đặt gate lỗi có ý nghĩa và kiểm tra diff khi áp auto-fix.
- **Đối chiếu:** [Biome](../13-dev-stack-devops/README.md) cho lint/format tích hợp; [Oxlint](../13-dev-stack-devops/README.md) cho lint nhanh; [Semgrep](../12-ai-security-guardrails/README.md) cho rule đa ngôn ngữ.
- **Mức kiểm chứng:** `docs-read` — Đọc các phần mô tả và giới hạn trong README, thông báo license, metadata manifest và cấu hình CI khi có; chưa đọc toàn bộ mã triển khai, chưa cài hoặc chạy kiểm thử upstream.
- **Snapshot:** kiểm ngày 2026-11-23; commit `5716b3fdc07a60f83b4812c4faa745dd05948367` (2026-11-23T09:51:24+01:00); 27,644 sao theo GitHub API ngày 2026-11-23. Sao không đại diện chất lượng.
- **Bằng chứng:** [README.md](https://github.com/eslint/eslint/blob/5716b3fdc07a60f83b4812c4faa745dd05948367/README.md) · [LICENSE](https://github.com/eslint/eslint/blob/5716b3fdc07a60f83b4812c4faa745dd05948367/LICENSE) · [package.json](https://github.com/eslint/eslint/blob/5716b3fdc07a60f83b4812c4faa745dd05948367/package.json) · [.github/workflows/ci.yml](https://github.com/eslint/eslint/blob/5716b3fdc07a60f83b4812c4faa745dd05948367/.github/workflows/ci.yml) · [GitHub API](https://api.github.com/repos/eslint/eslint).

<a id="anhkysuai-stretchr-testify"></a>

### Testify

- **Repo:** [stretchr/testify](https://github.com/stretchr/testify).
- **Mục đích:** Bộ assertion, mock và test suite cho Go.
- **Điểm đáng dùng:** require.Equal gọi Helper rồi assert.Equal; khi thất bại gọi TestingT.FailNow. TestEqual dùng MockT kiểm tra nhánh thất bại; CI khai báo race test trên stable, oldstable và Go cũ.
- **License:** MIT.
- **Giới hạn:** require phải chạy trong goroutine của test; mock chỉ chứng minh kỳ vọng đã khai báo, không thay integration test. Dòng v1 không nhận breaking change.
- **Tích hợp:** Dùng assertion cho hành vi quan trọng, ưu tiên fake/interface nhỏ và chạy race detector cho test concurrent.
- **Đối chiếu:** testing chuẩn Go cho dependency tối thiểu; go-cmp cho diff giá trị; Gomega cho matcher.
- **Mức kiểm chứng:** `code-read` — Đọc interface TestingT, wrapper require.Equal/Contains/Condition, callsite TestEqual với MockT và CI go test -race; chưa audit toàn bộ assert/mock/suite, chưa chạy test.
- **Snapshot:** kiểm ngày 2026-11-23; commit `87a7b9d57689f6579db2da795ab8deeab29cb724` (2026-09-24T16:59:34+02:00); 26,261 sao theo GitHub API ngày 2026-11-23. Sao không đại diện chất lượng.
- **Bằng chứng:** [README.md](https://github.com/stretchr/testify/blob/87a7b9d57689f6579db2da795ab8deeab29cb724/README.md) · [LICENSE](https://github.com/stretchr/testify/blob/87a7b9d57689f6579db2da795ab8deeab29cb724/LICENSE) · [go.mod](https://github.com/stretchr/testify/blob/87a7b9d57689f6579db2da795ab8deeab29cb724/go.mod) · [.github/workflows/main.yml](https://github.com/stretchr/testify/blob/87a7b9d57689f6579db2da795ab8deeab29cb724/.github/workflows/main.yml) · [require/requirements.go](https://github.com/stretchr/testify/blob/87a7b9d57689f6579db2da795ab8deeab29cb724/require/requirements.go) · [require/doc.go](https://github.com/stretchr/testify/blob/87a7b9d57689f6579db2da795ab8deeab29cb724/require/doc.go) · [require/require.go](https://github.com/stretchr/testify/blob/87a7b9d57689f6579db2da795ab8deeab29cb724/require/require.go) · [require/requirements_test.go](https://github.com/stretchr/testify/blob/87a7b9d57689f6579db2da795ab8deeab29cb724/require/requirements_test.go) · [GitHub API](https://api.github.com/repos/stretchr/testify).

<a id="anhkysuai-responsively-org-responsively-app"></a>

### Responsively App

- **Repo:** [responsively-org/responsively-app](https://github.com/responsively-org/responsively-app).
- **Mục đích:** Browser Electron hiển thị nhiều viewport để kiểm tra responsive.
- **Điểm đáng dùng:** Mirrored interactions, inspector chung, screenshot từng thiết bị và MCP tích hợp hỗ trợ vòng kiểm tra UI.
- **License:** AGPL-3.0.
- **Giới hạn:** Viewport profile không mô phỏng đầy đủ thiết bị thật hoặc engine Safari; claim nhanh 5 lần chưa đo, MCP cần phạm vi truy cập rõ.
- **Tích hợp:** Dùng kiểm tra layout của template với dev server, vẫn có bước browser/device thật cho font, touch và accessibility.
- **Đối chiếu:** [Playwright](../11-browser-computer-use-sandbox/README.md#playwright) cho viewport tự động; Chrome DevTools cho kiểm tra thủ công; BrowserStack cho thiết bị/browser hosted.
- **Mức kiểm chứng:** `docs-read` — Đọc các phần mô tả và giới hạn trong README, thông báo license, metadata manifest và cấu hình CI khi có; chưa đọc toàn bộ mã triển khai, chưa cài hoặc chạy kiểm thử upstream.
- **Snapshot:** kiểm ngày 2026-11-23; commit `048d018de294791dab42e628269844dfb6471a0a` (2026-11-23T08:56:55+05:30); 25,577 sao theo GitHub API ngày 2026-11-23. Sao không đại diện chất lượng.
- **Bằng chứng:** [README.md](https://github.com/responsively-org/responsively-app/blob/048d018de294791dab42e628269844dfb6471a0a/README.md) · [LICENSE](https://github.com/responsively-org/responsively-app/blob/048d018de294791dab42e628269844dfb6471a0a/LICENSE) · [.github/workflows/test.yml](https://github.com/responsively-org/responsively-app/blob/048d018de294791dab42e628269844dfb6471a0a/.github/workflows/test.yml) · [GitHub API](https://api.github.com/repos/responsively-org/responsively-app).

<a id="anhkysuai-mochajs-mocha"></a>

### Mocha

**Repo:** [mochajs/mocha](https://github.com/mochajs/mocha) · **License:** MIT · **Kiểm:** 2026-11-23, `docs-read`, [`93e7234e5a9f`](https://github.com/mochajs/mocha/tree/93e7234e5a9f4223181bbef5385312e848b98f1d) (commit 2026-11-22). **Sao:** 22,908 tại 2026-11-23 theo [GitHub API](https://api.github.com/repos/mochajs/mocha).

| Mục | Đánh giá |
|---|---|
| Mục đích | Test framework JavaScript cho Node.js và browser. |
| Giá trị và cơ chế theo tài liệu | Manifest 12.0.3 nêu dải Node hỗ trợ, build Rollup và cổng lint; README dẫn documentation/release history để chọn API phù hợp. |
| Giới hạn | Workflow chọn được chỉ gắn nhãn CLA, không xác nhận suite runtime; chưa chạy test upstream. Framework test không tự cung cấp coverage hay assertion đúng cho nghiệp vụ. |
| Điều kiện tích hợp | Chọn assertion/mocking/coverage theo dự án, ghim runtime và xử lý async/timeouts rõ; kiểm lỗi setup/teardown và flaky test trước đưa vào cổng CI bắt buộc. |
| Lựa chọn đối chiếu | [Vitest](../30-software-testing-quality/README.md#vitest-factory); Jest; Node test runner. |

**Phạm vi bằng chứng:** đã clone, đọc trích đoạn tài liệu, giấy phép và các file cấu hình được dẫn dưới đây; chưa chạy mã, build, benchmark hoặc test upstream. `docs-read` không phải kiểm chứng implementation.

**Nguồn tại cùng SHA:** [README.md](https://github.com/mochajs/mocha/blob/93e7234e5a9f4223181bbef5385312e848b98f1d/README.md) · [LICENSE](https://github.com/mochajs/mocha/blob/93e7234e5a9f4223181bbef5385312e848b98f1d/LICENSE) · [package.json](https://github.com/mochajs/mocha/blob/93e7234e5a9f4223181bbef5385312e848b98f1d/package.json) · [.github/workflows/cla.yml](https://github.com/mochajs/mocha/blob/93e7234e5a9f4223181bbef5385312e848b98f1d/.github/workflows/cla.yml).

<a id="anhkysuai-appium-appium"></a>

### Appium

**Repo:** [appium/appium](https://github.com/appium/appium) · **License:** Apache-2.0 · **Kiểm:** 2026-11-23, `docs-read`, [`e86206265639`](https://github.com/appium/appium/tree/e86206265639ce207bc5f5b30a587c2ca1146800) (commit 2026-11-22). **Sao:** 22,251 tại 2026-11-23 theo [GitHub API](https://api.github.com/repos/appium/appium).

| Mục | Đánh giá |
|---|---|
| Mục đích | Framework tự động hóa kiểm thử ứng dụng native, hybrid, mobile web, desktop và thiết bị qua WebDriver. |
| Giá trị và cơ chế theo tài liệu | Kiến trúc README tách driver theo nền tảng, client theo ngôn ngữ và plugin mở rộng; CI có phát hiện gói e2e và smoke test. Phù hợp xây lớp kiểm thử hành trình trên thiết bị. |
| Giới hạn | Upstream chỉ hỗ trợ phiên bản Appium mới nhất theo README; driver, SDK và hệ điều hành có yêu cầu riêng. Manifest monorepo 0.0.0 không phải phiên bản sản phẩm; Node/npm tối thiểu khá mới. |
| Điều kiện tích hợp | Chọn driver và thiết bị mục tiêu, khóa bản tương thích, cô lập tài khoản thử nghiệm; thiết kế chờ theo trạng thái và thu log/screenshot để giảm test chập chờn. |
| Lựa chọn đối chiếu | Maestro; Detox; [Playwright](../11-browser-computer-use-sandbox/README.md#playwright). |

**Phạm vi bằng chứng:** đã clone, đọc trích đoạn tài liệu, giấy phép và các file cấu hình được dẫn dưới đây; chưa chạy mã, build, benchmark hoặc test upstream. `docs-read` không phải kiểm chứng implementation.

**Nguồn tại cùng SHA:** [README.md](https://github.com/appium/appium/blob/e86206265639ce207bc5f5b30a587c2ca1146800/README.md) · [LICENSE](https://github.com/appium/appium/blob/e86206265639ce207bc5f5b30a587c2ca1146800/LICENSE) · [package.json](https://github.com/appium/appium/blob/e86206265639ce207bc5f5b30a587c2ca1146800/package.json) · [.github/workflows/build.yml](https://github.com/appium/appium/blob/e86206265639ce207bc5f5b30a587c2ca1146800/.github/workflows/build.yml).

<a id="anhkysuai-aidenybai-react-scan"></a>

### React Scan

**Repo:** [aidenybai/react-scan](https://github.com/aidenybai/react-scan) · **License:** MIT · **Kiểm:** 2026-11-23, `docs-read`, [`0fb31862b697`](https://github.com/aidenybai/react-scan/tree/0fb31862b697ef3ed2d8ed6990878a35a4ca8a75) (commit 2026-08-16). **Sao:** 21,882 tại 2026-11-23 theo [GitHub API](https://api.github.com/repos/aidenybai/react-scan).

| Mục | Đánh giá |
|---|---|
| Mục đích | Công cụ hiển thị component và điểm nóng hiệu năng khi quan sát ứng dụng React đang chạy. |
| Giá trị và cơ chế theo tài liệu | README mô tả toolbar và cài qua script hoặc gói phát triển; monorepo có extension, Vite plugin, Playwright và kiểm kiểu. Hữu ích để tìm vùng cần đo sâu khi UI render nhiều. |
| Giới hạn | README hiện khuyên dùng React Doctor cho kiểm tra tĩnh qua agent nhưng vẫn cho dùng React Scan. Highlight không chứng minh nguyên nhân hoặc mức cải thiện; chưa đo overhead và tính tương thích React. |
| Điều kiện tích hợp | Bật trong môi trường phát triển có kiểm soát, khóa phiên bản script và so với React Profiler; chỉ sửa sau khi tái hiện tác vụ chậm và đo trước/sau. |
| Lựa chọn đối chiếu | React DevTools; React Doctor; why-did-you-render. |

**Phạm vi bằng chứng:** đã clone, đọc trích đoạn tài liệu, giấy phép và các file cấu hình được dẫn dưới đây; chưa chạy mã, build, benchmark hoặc test upstream. `docs-read` không phải kiểm chứng implementation.

**Nguồn tại cùng SHA:** [README.md](https://github.com/aidenybai/react-scan/blob/0fb31862b697ef3ed2d8ed6990878a35a4ca8a75/README.md) · [LICENSE](https://github.com/aidenybai/react-scan/blob/0fb31862b697ef3ed2d8ed6990878a35a4ca8a75/LICENSE) · [package.json](https://github.com/aidenybai/react-scan/blob/0fb31862b697ef3ed2d8ed6990878a35a4ca8a75/package.json) · [.github/workflows/build-extension.yml](https://github.com/aidenybai/react-scan/blob/0fb31862b697ef3ed2d8ed6990878a35a4ca8a75/.github/workflows/build-extension.yml).

<a id="anhkysuai-jsdom-jsdom"></a>

### jsdom

**Repo:** [jsdom/jsdom](https://github.com/jsdom/jsdom) · **License:** MIT; dữ liệu và thuật toán kèm theo có thông báo W3C và Unicode · **Kiểm:** 2026-11-23, `docs-read`, [`f15f030b0076`](https://github.com/jsdom/jsdom/tree/f15f030b00766c502ea858011c35df34f88b77df) (commit 2026-11-21). **Sao:** 21,763 tại 2026-11-23 theo [GitHub API](https://api.github.com/repos/jsdom/jsdom).

| Mục | Đánh giá |
|---|---|
| Mục đích | Mô phỏng nhiều API DOM và HTML trong Node.js để kiểm thử logic giao diện hoặc phân tích trang. |
| Giá trị và cơ chế theo tài liệu | README minh họa JSDOM tạo window/document và tùy chọn tài nguyên; manifest 31.0.1 có quy trình sinh dữ liệu, CI kiểm Node engine và các biến thể canvas. |
| Giới hạn | Không thực hiện layout/rendering và không hỗ trợ navigation đầy đủ. README cảnh báo runScripts dangerously với nội dung không tin cậy có thể tiếp cận môi trường Node; không coi đây là sandbox bảo mật. |
| Điều kiện tích hợp | Dùng cho test DOM không phụ thuộc hình học, giữ thực thi script tắt với HTML lạ; chuyển test bố cục hoặc điều hướng sang browser thật và khóa Node theo engines. |
| Lựa chọn đối chiếu | Happy DOM; LinkeDOM; [Playwright](../11-browser-computer-use-sandbox/README.md#playwright). |

**Phạm vi bằng chứng:** đã clone, đọc trích đoạn tài liệu, giấy phép và các file cấu hình được dẫn dưới đây; chưa chạy mã, build, benchmark hoặc test upstream. `docs-read` không phải kiểm chứng implementation.

**Nguồn tại cùng SHA:** [README.md](https://github.com/jsdom/jsdom/blob/f15f030b00766c502ea858011c35df34f88b77df/README.md) · [LICENSE.txt](https://github.com/jsdom/jsdom/blob/f15f030b00766c502ea858011c35df34f88b77df/LICENSE.txt) · [package.json](https://github.com/jsdom/jsdom/blob/f15f030b00766c502ea858011c35df34f88b77df/package.json) · [.github/workflows/ci.yml](https://github.com/jsdom/jsdom/blob/f15f030b00766c502ea858011c35df34f88b77df/.github/workflows/ci.yml).

<a id="anhkysuai-catchorg-catch2"></a>

### Catch2

**Repo:** [catchorg/Catch2](https://github.com/catchorg/Catch2) · **License:** BSL-1.0 · **Kiểm:** 2026-11-23, `docs-read`, [`36c1bc3ef209`](https://github.com/catchorg/Catch2/tree/36c1bc3ef209a649741f36d9913d63451e8d07b5) (commit 2026-11-15). **Sao:** 21,590 tại 2026-11-23 theo [GitHub API](https://api.github.com/repos/catchorg/Catch2).

| Mục | Đánh giá |
|---|---|
| Mục đích | Framework unit test C++ với assertion tự nhiên, section chia sẻ setup, macro BDD và microbenchmark cơ bản. |
| Giá trị và cơ chế theo tài liệu | README có ví dụ TEST_CASE, REQUIRE và BENCHMARK; CMake yêu cầu tối thiểu 3.16, workflow macOS configure/build rồi ctest. Phù hợp bổ sung kiểm tra thư viện hoặc thành phần C++. |
| Giới hạn | Nhánh devel phát triển v3, không còn là thư viện một header; tài liệu chuyển đổi từ v2 vẫn đang được cập nhật theo README. Không coi microbenchmark là đánh giá hiệu năng hệ thống. |
| Điều kiện tích hợp | Khóa bản release, tích hợp target CMake và test discovery; kiểm chuẩn C++, compiler và lựa chọn linking, tách test đơn vị với benchmark nhạy cảm tài nguyên. |
| Lựa chọn đối chiếu | GoogleTest; doctest; Boost.Test. |

**Phạm vi bằng chứng:** đã clone, đọc trích đoạn tài liệu, giấy phép và các file cấu hình được dẫn dưới đây; chưa chạy mã, build, benchmark hoặc test upstream. `docs-read` không phải kiểm chứng implementation.

**Nguồn tại cùng SHA:** [README.md](https://github.com/catchorg/Catch2/blob/36c1bc3ef209a649741f36d9913d63451e8d07b5/README.md) · [LICENSE.txt](https://github.com/catchorg/Catch2/blob/36c1bc3ef209a649741f36d9913d63451e8d07b5/LICENSE.txt) · [CMakeLists.txt](https://github.com/catchorg/Catch2/blob/36c1bc3ef209a649741f36d9913d63451e8d07b5/CMakeLists.txt) · [.github/workflows/mac-builds.yml](https://github.com/catchorg/Catch2/blob/36c1bc3ef209a649741f36d9913d63451e8d07b5/.github/workflows/mac-builds.yml).

<a id="anhkysuai-avajs-ava"></a>

### AVA

**Repo:** [avajs/ava](https://github.com/avajs/ava) · **License:** MIT · **Kiểm:** 2026-11-23, `docs-read`, [`ce2839c13857`](https://github.com/avajs/ava/tree/ce2839c13857ab43f3e0bde9799d706e15914a54) (commit 2026-11-15). **Sao:** 20,825 tại 2026-11-23 theo [GitHub API](https://api.github.com/repos/avajs/ava).

| Mục | Đánh giá |
|---|---|
| Mục đích | Test runner Node.js với cú pháp ngắn, assertion chi tiết và chạy đồng thời các test độc lập. |
| Giá trị và cơ chế theo tài liệu | README mô tả không dùng global ngầm, môi trường tách cho từng file, hỗ trợ Promise và async; manifest 8.4.0 cùng CI có các bản Node và kiểm TypeScript. |
| Giới hạn | Thread isolation không tách database, port hoặc filesystem dùng chung. Chạy song song có thể làm test phụ thuộc thứ tự bộc lộ lỗi; snapshot yêu cầu Node mới theo engines, chưa chạy suite. |
| Điều kiện tích hợp | Dùng fixture riêng mỗi test, quản lý timeout và cleanup, chọn serial cho tài nguyên bắt buộc dùng chung; đưa test vào CI với báo cáo thất bại dễ tái hiện. |
| Lựa chọn đối chiếu | [Vitest](../30-software-testing-quality/README.md#vitest-factory); [Mocha](../30-software-testing-quality/README.md#anhkysuai-mochajs-mocha); Node.js test runner. |

**Phạm vi bằng chứng:** đã clone, đọc trích đoạn tài liệu, giấy phép và các file cấu hình được dẫn dưới đây; chưa chạy mã, build, benchmark hoặc test upstream. `docs-read` không phải kiểm chứng implementation.

**Nguồn tại cùng SHA:** [readme.md](https://github.com/avajs/ava/blob/ce2839c13857ab43f3e0bde9799d706e15914a54/readme.md) · [license](https://github.com/avajs/ava/blob/ce2839c13857ab43f3e0bde9799d706e15914a54/license) · [package.json](https://github.com/avajs/ava/blob/ce2839c13857ab43f3e0bde9799d706e15914a54/package.json) · [.github/workflows/ci.yml](https://github.com/avajs/ava/blob/ce2839c13857ab43f3e0bde9799d706e15914a54/.github/workflows/ci.yml).

<a id="anhkysuai-python-mypy"></a>

### Mypy

**Repo:** [python/mypy](https://github.com/python/mypy) · **License:** MIT cho mypy/mypyc; một số tệp và thành phần có PSF/BSD hoặc thông báo riêng · **Kiểm:** 2026-11-23, `docs-read`, [`1572a18848d1`](https://github.com/python/mypy/tree/1572a18848d181f5cd91877aa3ab4e1644b14f20) (commit 2026-11-20). **Sao:** 20,735 tại 2026-11-23 theo [GitHub API](https://api.github.com/repos/python/mypy).

| Mục | Đánh giá |
|---|---|
| Mục đích | Bộ kiểm kiểu tĩnh cho Python, cho phép thêm type hint từng phần mà không đổi cách chương trình chạy. |
| Giá trị và cơ chế theo tài liệu | README minh họa phát hiện phép toán sai kiểu, gradual typing, generics và structural subtyping; có daemon tăng tốc kiểm lặp. CI liệt kê nhiều bản Python, Windows và biến thể mypyc. |
| Giới hạn | Độ bao phủ phụ thuộc annotation, stub và cấu hình; code dynamic hoặc Any có thể làm giảm kiểm tra. Type check không chứng minh hành vi runtime hoặc thay unit test; chưa chạy mypy trên codebase mẫu. |
| Điều kiện tích hợp | Bắt đầu từ module biên, khóa phiên bản/stub và Python target, tăng mức nghiêm dần trong CI; xử lý ignore có lý do và giữ test hành vi. |
| Lựa chọn đối chiếu | Pyright; ty; Pyre. |

**Phạm vi bằng chứng:** đã clone, đọc trích đoạn tài liệu, giấy phép và các file cấu hình được dẫn dưới đây; chưa chạy mã, build, benchmark hoặc test upstream. `docs-read` không phải kiểm chứng implementation.

**Nguồn tại cùng SHA:** [README.md](https://github.com/python/mypy/blob/1572a18848d181f5cd91877aa3ab4e1644b14f20/README.md) · [LICENSE](https://github.com/python/mypy/blob/1572a18848d181f5cd91877aa3ab4e1644b14f20/LICENSE) · [pyproject.toml](https://github.com/python/mypy/blob/1572a18848d181f5cd91877aa3ab4e1644b14f20/pyproject.toml) · [.github/workflows/test.yml](https://github.com/python/mypy/blob/1572a18848d181f5cd91877aa3ab4e1644b14f20/.github/workflows/test.yml).

<a id="anhkysuai-2026-11-23-typicode-json-server"></a>

### json-server

**Repo:** [typicode/json-server](https://github.com/typicode/json-server) · **License:** MIT · **★ 75,753 (GitHub API, 2026-11-23)**

**Mục đích:** Công cụ dựng REST API giả từ dữ liệu JSON/JSON5 để phát triển giao diện và prototype.

**Giá trị:** Hỗ trợ route và truy vấn giúp làm việc khi backend thật chưa sẵn sàng.

**Giới hạn:** SHA hiện tại là 1.0.0-beta.15, README cảnh báo breaking changes và trỏ stable v0.17.4; API giả không chứng minh hành vi xác thực, giao dịch hay tải của backend thật.

**Cách tham khảo/tích hợp:** Đọc cấu hình triển khai, giới hạn license và hợp đồng dữ liệu; thử auth, migration, backup/restore với dữ liệu mẫu trước tích hợp.

**Lựa chọn để đối chiếu:** [mswjs/msw](https://github.com/mswjs/msw) · [stoplightio/prism](https://github.com/stoplightio/prism). Đây là ứng viên so sánh theo tác vụ; mức phù hợp cần kiểm theo hồ sơ và phiên bản riêng.

**Bằng chứng:** `docs-read`, ngày 2026-11-23, commit [`89a34a44b7a6a5311dc84f3b8a1b8b45c0905aea`](https://github.com/typicode/json-server/commit/89a34a44b7a6a5311dc84f3b8a1b8b45c0905aea), ngày commit 2026-03-23. Đã clone và đọc chọn lọc phần giới thiệu, cách dùng, giới hạn, license, metadata manifest và CI hiện diện. Chưa kiểm đầy đủ implementation hoặc chạy upstream; các số đo của tác giả chưa được tái lập.

**Nguồn:** [README.md](https://github.com/typicode/json-server/blob/89a34a44b7a6a5311dc84f3b8a1b8b45c0905aea/README.md) · [LICENSE](https://github.com/typicode/json-server/blob/89a34a44b7a6a5311dc84f3b8a1b8b45c0905aea/LICENSE) · [package.json](https://github.com/typicode/json-server/blob/89a34a44b7a6a5311dc84f3b8a1b8b45c0905aea/package.json) · [.github/workflows/node.js.yml](https://github.com/typicode/json-server/blob/89a34a44b7a6a5311dc84f3b8a1b8b45c0905aea/.github/workflows/node.js.yml) · [metadata GitHub](https://api.github.com/repos/typicode/json-server).

<a id="chuyen-muc-2026-11-23"></a>

## Hồ sơ chuyển về từ mục khác — 23/11/2026

4 hồ sơ được chuyển khi chia lại catalog theo `data/taxonomy.json`. Nội dung, ngày kiểm và mức bằng chứng giữ nguyên như ở mục gốc.

<a id="chuyen-web-vitals"></a>

### web-vitals

`GoogleChrome/web-vitals` · License: Apache-2.0 · ★ 8.669

Thư viện chính thức đo LCP/INP/CLS ở người dùng thật, build attribution chỉ ra nguyên nhân; v6.2.3; dùng đo tác động của animation; commit cuối 16/10/2026; ★ 2/11/2026 (GitHub search API), mục 22 §9g

**Hồ sơ gốc:** [mục 22](../22-motion-design-animation/README.md) (bảng/đoạn chung, giữ nguyên tại chỗ).

<a id="chuyen-keploy"></a>

### keploy

`keploy/keploy` · License: Apache License 2.0 · ★ 19.881 · docs-read · 2026-11-18

Công cụ kiểm thử API và tích hợp, ghi lại lưu lượng thật (API, truy vấn DB, sự kiện streaming) bằng eBPF rồi phát lại thành test và mock. Không cần sửa code hay SDK, độc lập ngôn ngữ; mock được Postgres, MySQL, MongoDB, Kafka, RabbitMQ; tích hợp CI/CD và đóng băng thời gian để phát lại tất định. Điều kiện: Một số phụ thuộc giao thức không mã nguồn mở theo README; một số tính năng (console, mock registry, mở rộng bằng AI) thuộc nền tảng keploy.io (chưa xác minh phạm vi miễn phí). ★ 18/11/2026: 19.881 (GitHub search API), nhóm "Container & DevOps" trong kho-repo của Phan Đông Giang, mục 08 §6c.5

**Hồ sơ gốc:** [mục 08](../08-awesome-lists-learning/README.md#6c55-container--devops) (bảng/đoạn chung, giữ nguyên tại chỗ).

<a id="chuyen-react-doctor"></a>

### react-doctor

`millionco/react-doctor` · License: Modified MIT License · ★ 15.154 · docs-read · 2026-11-18

Công cụ quét tĩnh có tính tất định cho dự án React, báo lỗi về state/effect, hiệu năng, kiến trúc, bảo mật, a11y và khả năng bảo trì. Hỗ trợ Next.js, Vite, Astro, TanStack, React Native, Expo; có lệnh cài skill cho agent và lệnh cài quét CI cho từng PR; có plugin eslint và oxlint trong packages. Điều kiện: CLI thu thập báo cáo crash và dữ liệu sử dụng ẩn danh (tắt bằng --no-telemetry); giấy phép cấm dùng làm dữ liệu huấn luyện AI hoặc bán dạng SaaS khi chưa được phép. ★ 18/11/2026: 15.154 (GitHub search API), nhóm "Framework Frontend" trong kho-repo của Phan Đông Giang, mục 08 §6c.5

**Hồ sơ gốc:** [mục 08](../08-awesome-lists-learning/README.md#6c510-framework-frontend) (bảng/đoạn chung, giữ nguyên tại chỗ).

<a id="anhkysuai-locustio-locust"></a>

### Locust

**Repo:** [locustio/locust](https://github.com/locustio/locust) · **License:** MIT · **Kiểm:** 2026-11-23, `docs-read`, [`85d6d65da7d1`](https://github.com/locustio/locust/tree/85d6d65da7d12f07fc1001192e52c4ede286528f) (commit 2026-11-16). **Sao:** 28,307 tại 2026-11-23 theo [GitHub API](https://api.github.com/repos/locustio/locust).

| Mục | Đánh giá |
|---|---|
| Mục đích | Công cụ viết kịch bản kiểm tải bằng Python cho HTTP và giao thức mở rộng. |
| Giá trị và cơ chế theo tài liệu | README mô tả greenlet theo người dùng, CLI/WebUI và xuất throughput/latency/errors; Python/Node manifests cùng CI thể hiện engine và frontend. |
| Giới hạn | Kết quả phụ thuộc mô hình hành vi, máy tạo tải và dữ liệu kiểm. Chưa chạy tải hoặc xác minh giới hạn throughput; vòng lặp benchmark không tự mô phỏng người dùng thật. |
| Điều kiện tích hợp | Viết hành trình có thời gian chờ và kiểm response, chạy trong môi trường được phép; tách bottleneck load generator và theo dõi percentile/error trước khi kết luận sức tải. |
| Lựa chọn đối chiếu | k6; JMeter; Gatling. |

**Phạm vi bằng chứng:** đã clone, đọc trích đoạn tài liệu, giấy phép và các file cấu hình được dẫn dưới đây; chưa chạy mã, build, benchmark hoặc test upstream. `docs-read` không phải kiểm chứng implementation.

**Nguồn tại cùng SHA:** [README.md](https://github.com/locustio/locust/blob/85d6d65da7d12f07fc1001192e52c4ede286528f/README.md) · [LICENSE](https://github.com/locustio/locust/blob/85d6d65da7d12f07fc1001192e52c4ede286528f/LICENSE) · [package.json](https://github.com/locustio/locust/blob/85d6d65da7d12f07fc1001192e52c4ede286528f/package.json) · [pyproject.toml](https://github.com/locustio/locust/blob/85d6d65da7d12f07fc1001192e52c4ede286528f/pyproject.toml) · [.github/workflows/tests.yml](https://github.com/locustio/locust/blob/85d6d65da7d12f07fc1001192e52c4ede286528f/.github/workflows/tests.yml).

<a id="chuan-hoa-2026-11-23"></a>

## Chuẩn hóa bằng chứng hồ sơ cũ — 23/11/2026

Các hồ sơ dưới đây có từ trước khi kho ghi mức kiểm. Ngày 2026-11-23 mỗi repo được clone nông tại commit ghi trong bảng, đọc LICENSE, README, manifest và CI (nếu có); không cài, build hay chạy mã upstream. Nhận định cũ ở phần trên giữ nguyên; chỗ nào khác với lần đọc này được ghi trong cột Nhận định. Số sao lấy qua GitHub search API cùng ngày.

<a id="ch-web-vitals"></a>

### web-vitals

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/GoogleChrome/web-vitals |
| License | Apache-2.0 |
| Phiên bản đã đọc | `94b3b4bced9d63b4ff6bfb8290bf1f505daa00bb` (commit 2026-11-09) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE, package.json, .github/workflows/tests.yml; chưa chạy upstream |
| Bảo trì | active (commit mới nhất 2026-11-09) |
| Nhận định | Thư viện JS đo Core Web Vitals và gửi lên analytics, có bản attribution; package v6.2.3. Giới hạn: số đo phụ thuộc hỗ trợ API của trình duyệt. |
| Nguồn | [README](https://github.com/GoogleChrome/web-vitals/blob/94b3b4bced9d63b4ff6bfb8290bf1f505daa00bb/README.md) · [LICENSE](https://github.com/GoogleChrome/web-vitals/blob/94b3b4bced9d63b4ff6bfb8290bf1f505daa00bb/LICENSE) · [manifest](https://github.com/GoogleChrome/web-vitals/blob/94b3b4bced9d63b4ff6bfb8290bf1f505daa00bb/package.json) · [workflow](https://github.com/GoogleChrome/web-vitals/blob/94b3b4bced9d63b4ff6bfb8290bf1f505daa00bb/.github/workflows/tests.yml) |

<a id="nt-2026-11-23"></a>

## Nâng trần theo khoảng trống — 23/11/2026

Phần này có các hồ sơ mới của đợt nâng trần: mười trinh sát tìm trên internet và GitHub những mảng mà chuyên mục còn thiếu hoặc chỉ có hồ sơ cũ, rồi mỗi repo được clone nông tại một commit cố định, đọc LICENSE, README, ít nhất một file triển khai thật và CI nếu có; không cài hay chạy mã upstream. Mô tả của trinh sát nhiều chỗ sai so với mã thật, và các chỗ đó được sửa ngay trong từng hồ sơ. Số sao lấy sau bằng GitHub search API nên có thể để trống.

<a id="nt-vegeta"></a>

### Vegeta

| Thuộc tính | Giá trị |
|---|---|
| Repo | https://github.com/tsenart/vegeta |
| License | MIT |
| Phiên bản đã đọc | `a5dcbf48acd83383d3687c3634ce067a54b06983` (commit 2026-11-19) |
| Kiểm chứng | 2026-11-23; code-read; đã đọc LICENSE, README, go.mod, ci.yml, lib/attack.go, lib/pacer.go, lib/metrics.go (chỉ liệt kê tên test, chưa mở file test); chưa chạy upstream |
| Khoảng trống lấp | Kiểm thử tải (HTTP, tốc độ cố định) |
| Cơ chế đáng học | - Tải theo tốc độ yêu cầu cố định chứ không theo số kết nối: `ConstantPacer` trong `lib/pacer.go` tính số hit kỳ vọng theo thời gian trôi qua và gửi bù ngay khi chạy trễ; ngoài ra có `SinePacer` và `LinearPacer` cho tải dao động hoặc tăng dần.<br>- Giao diện `Pacer` (Pace, Rate) tách chính sách tải khỏi bộ tấn công, nên nhúng làm thư viện Go và tự viết pacer riêng được (`lib/attack.go`, `lib/pacer.go`).<br>- Số worker khởi đầu là 10 và tự nở thêm tới `MaxWorkers` để giữ tốc độ; độ trễ đo từ lúc ghi timestamp trong vùng khóa của `Attack` đến khi trả về, nên không gộp thời gian chờ hàng đợi nội bộ vào mẫu đã gửi.<br>- Báo cáo trong `lib/metrics.go`: p50/p90/p95/p99, max, tỷ lệ thành công và histogram mã trạng thái; phân vị lấy bằng t-digest (xấp xỉ, không chính xác tuyệt đối). |
| Tiêu chí và cách kiểm | Không có ngưỡng đạt/trượt tích hợp; `go vet` và `go test -race ./...` chạy trong CI (đã mở ci.yml), kèm kiểm định dạng bằng goimports. Có test cho pacer và metrics, có fuzz target trong `lib/`. Muốn làm cổng CI phải tự đọc báo cáo JSON và so ngưỡng bằng script. |
| Giới hạn và rủi ro | Chỉ HTTP/HTTPS; không kịch bản nhiều bước hay logic người dùng như k6 hoặc Locust. Xuất báo cáo bằng t-digest nên phân vị là xấp xỉ. Trinh sát ghi MIT: đúng (LICENSE MIT, 2013-2023 Tomás Senart). Không thấy telemetry trong phần đã đọc (chưa quét toàn bộ). Commit mới nhất 2026-11-19 nên còn bảo trì; go.mod yêu cầu Go 1.22. |
| So với | grafana-k6, locustio-locust, oha (cùng lô) |
| Nguồn | [LICENSE](https://github.com/tsenart/vegeta/blob/a5dcbf48acd83383d3687c3634ce067a54b06983/LICENSE) · [README.md](https://github.com/tsenart/vegeta/blob/a5dcbf48acd83383d3687c3634ce067a54b06983/README.md) · [go.mod](https://github.com/tsenart/vegeta/blob/a5dcbf48acd83383d3687c3634ce067a54b06983/go.mod) · [.github/workflows/ci.yml](https://github.com/tsenart/vegeta/blob/a5dcbf48acd83383d3687c3634ce067a54b06983/.github/workflows/ci.yml) · [lib/attack.go](https://github.com/tsenart/vegeta/blob/a5dcbf48acd83383d3687c3634ce067a54b06983/lib/attack.go) · [lib/pacer.go](https://github.com/tsenart/vegeta/blob/a5dcbf48acd83383d3687c3634ce067a54b06983/lib/pacer.go) · [lib/metrics.go](https://github.com/tsenart/vegeta/blob/a5dcbf48acd83383d3687c3634ce067a54b06983/lib/metrics.go) |

<a id="nt-oha"></a>

### oha

| Thuộc tính | Giá trị |
|---|---|
| Repo | https://github.com/hatoo/oha |
| License | MIT |
| Phiên bản đã đọc | `780c4e6e23ea8297e68fc7a042a8b1b0413741d9` (commit 2026-11-18) |
| Kiểm chứng | 2026-11-23; code-read; đã đọc LICENSE, README, Cargo.toml, CI.yml, src/cli.rs, src/client.rs, src/histogram.rs, src/db.rs; chưa chạy upstream |
| Khoảng trống lấp | Kiểm thử tải (HTTP, có TUI) |
| Cơ chế đáng học | - Sinh tải HTTP bằng Rust, hiển thị TUI thời gian thực (ratatui); chế độ `--no-tui` không đặt `-q` hay burst dùng đường chạy nhanh hơn vì bỏ gom dữ liệu thời gian thực (README).<br>- Cờ `--latency-correction` đặt `start_latency_correction` trong `src/client.rs` để tính độ trễ từ thời điểm lẽ ra phải gửi, nhằm tránh coordinated omission; chỉ có hiệu lực khi đặt `-q` hoặc `--burst-delay` (theo README và mô tả cờ trong `src/cli.rs`).<br>- Ghi kết quả từng yêu cầu vào SQLite qua `--db-url` (`src/db.rs`, rusqlite) để phân tích sau.<br>- Hỗ trợ HTTP/1, HTTP/2, tuỳ chọn HTTP/3 và vsock qua feature flag trong `Cargo.toml`. |
| Tiêu chí và cách kiểm | CI (CI.yml đã mở) chạy `cargo test` trên ubuntu, windows, macos với ba tổ hợp feature (mặc định rustls, native-tls, http3) cùng job rustfmt; có test tích hợp trong `tests/` và test đơn vị trong `src/histogram.rs`. Không có ngưỡng đạt/trượt cho mục tiêu được đo; đây là công cụ đo, không phải cổng. |
| Giới hạn và rủi ro | Histogram tự dựng với số bin cố định, không phải HDR. Latency correction mặc định tắt. Không kịch bản nhiều bước. Trinh sát ghi MIT: đúng (LICENSE và Cargo.toml). Phần đã đọc không thấy telemetry. Edition 2024 và rust-version 1.88 nên cần toolchain mới để tự build. Có bảo trì (commit 2026-11-18). |
| So với | vegeta (cùng lô), grafana-k6, locustio-locust |
| Nguồn | [LICENSE](https://github.com/hatoo/oha/blob/780c4e6e23ea8297e68fc7a042a8b1b0413741d9/LICENSE) · [README.md](https://github.com/hatoo/oha/blob/780c4e6e23ea8297e68fc7a042a8b1b0413741d9/README.md) · [Cargo.toml](https://github.com/hatoo/oha/blob/780c4e6e23ea8297e68fc7a042a8b1b0413741d9/Cargo.toml) · [.github/workflows/CI.yml](https://github.com/hatoo/oha/blob/780c4e6e23ea8297e68fc7a042a8b1b0413741d9/.github/workflows/CI.yml) · [src/cli.rs](https://github.com/hatoo/oha/blob/780c4e6e23ea8297e68fc7a042a8b1b0413741d9/src/cli.rs) · [src/client.rs](https://github.com/hatoo/oha/blob/780c4e6e23ea8297e68fc7a042a8b1b0413741d9/src/client.rs) · [src/histogram.rs](https://github.com/hatoo/oha/blob/780c4e6e23ea8297e68fc7a042a8b1b0413741d9/src/histogram.rs) · [src/db.rs](https://github.com/hatoo/oha/blob/780c4e6e23ea8297e68fc7a042a8b1b0413741d9/src/db.rs) |

<a id="nt-google-oss-fuzz"></a>

### OSS-Fuzz

| Thuộc tính | Giá trị |
|---|---|
| Repo | https://github.com/google/oss-fuzz |
| License | Apache-2.0 |
| Phiên bản đã đọc | `0a47116786dffb1fff93b2bfb48c7b4ae8463903` (commit 2026-11-23) |
| Kiểm chứng | 2026-11-23; code-read; đã đọc README.md, LICENSE, AGENTS.md, docs/getting-started/accepting_new_projects.md, docs/getting-started/bug_disclosure_guidelines.md, projects/zlib/build.sh, projects/zlib/project.yaml, infra/constants.py, .github/workflows/presubmit.yml; chưa chạy upstream |
| Khoảng trống lấp | Fuzz, mutation, chaos/resilience: nền cho việc dựng fuzz harness và cấu hình sanitizer |
| Cơ chế đáng học | - `projects/<tên>/` gồm `Dockerfile`, `build.sh`, `project.yaml`; ví dụ zlib khai libfuzzer, afl, honggfuzz, ba sanitizer (address, memory, undefined), hai kiến trúc.<br>- `build.sh` biên dịch từng `*_fuzzer.c(c)` với `$LIB_FUZZING_ENGINE` và đóng seed corpus; bỏ `make check` khi sanitizer là memory.<br>- `infra/helper.py` có `build_fuzzers`, `check_build`, `run_fuzzer`, `reproduce`; `infra/constants.py` liệt kê engine libfuzzer, afl, honggfuzz, centipede, none, wycheproof.<br>- Quy trình công bố lỗi 90 ngày kèm 14 ngày gia hạn (bug_disclosure_guidelines.md). |
| Tiêu chí và cách kiểm | Điều kiện nhận: dự án mở có nhiều người dùng hoặc là hạ tầng quan trọng, email liên hệ là committer gắn tài khoản Google. Kiểm bằng máy: presubmit.yml (đã đọc) chạy lint/test hạ tầng, `check_build` xác nhận fuzzer chạy được. Kết quả fuzz thật nằm ở dịch vụ ClusterFuzz phía Google, không thấy trong repo. |
| Giới hạn và rủi ro | Apache-2.0. Báo cáo lỗi tự động gửi tới liên hệ chính và công khai sau hạn; dự án nhận vào là cho Google chạy mã build của dự án trên hạ tầng của họ. Hỗ trợ x86_64 và i386, ngôn ngữ C/C++, Rust, Go, Python, JVM, JavaScript, Lua. Repo chứa hơn 1400 thư mục dự án, rất nặng nếu clone đầy đủ. Mô tả trinh sát đặt vào unit-integration là gần đúng nhưng đây là hạ tầng fuzz, không phải test unit. |
| So với | Chưa có hồ sơ fuzz tương đương trong kho; gần nhất về vai trò cổng chất lượng là Semgrep và Trivy (quét tĩnh, không động) |
| Nguồn | [README.md](https://github.com/google/oss-fuzz/blob/0a47116786dffb1fff93b2bfb48c7b4ae8463903/README.md) · [LICENSE](https://github.com/google/oss-fuzz/blob/0a47116786dffb1fff93b2bfb48c7b4ae8463903/LICENSE) · [AGENTS.md](https://github.com/google/oss-fuzz/blob/0a47116786dffb1fff93b2bfb48c7b4ae8463903/AGENTS.md) · [accepting_new_projects.md](https://github.com/google/oss-fuzz/blob/0a47116786dffb1fff93b2bfb48c7b4ae8463903/docs/getting-started/accepting_new_projects.md) · [bug_disclosure_guidelines.md](https://github.com/google/oss-fuzz/blob/0a47116786dffb1fff93b2bfb48c7b4ae8463903/docs/getting-started/bug_disclosure_guidelines.md) · [build.sh](https://github.com/google/oss-fuzz/blob/0a47116786dffb1fff93b2bfb48c7b4ae8463903/projects/zlib/build.sh) · [project.yaml](https://github.com/google/oss-fuzz/blob/0a47116786dffb1fff93b2bfb48c7b4ae8463903/projects/zlib/project.yaml) · [constants.py](https://github.com/google/oss-fuzz/blob/0a47116786dffb1fff93b2bfb48c7b4ae8463903/infra/constants.py) · [presubmit.yml](https://github.com/google/oss-fuzz/blob/0a47116786dffb1fff93b2bfb48c7b4ae8463903/.github/workflows/presubmit.yml) |

<a id="nt-shopify-toxiproxy"></a>

### Toxiproxy

| Thuộc tính | Giá trị |
|---|---|
| Repo | https://github.com/Shopify/toxiproxy |
| License | MIT |
| Phiên bản đã đọc | `49299d8838525126e09c85ebe0ba89940a3261e5` (commit 2026-10-14) |
| Kiểm chứng | 2026-11-23; code-read; đã đọc README.md, LICENSE, CREATING_TOXICS.md, toxics/latency.go, toxics/reset_peer.go, .github/workflows/test.yml, .github/workflows/analysis.yml; chưa chạy upstream |
| Khoảng trống lấp | Fuzz, mutation, chaos/resilience: gây lỗi mạng có kiểm soát cho test tích hợp |
| Cơ chế đáng học | - Mỗi toxic hiện thực giao diện `Toxic { Pipe(*ToxicStub) }` (CREATING_TOXICS.md); `toxics/latency.go` trì hoãn bằng latency cộng trừ jitter, tính bù thời gian chunk đã chờ.<br>- `toxics/reset_peer.go` đặt SetLinger 0 để gửi RST thay vì đóng êm, mô phỏng đứt kết nối đột ngột.<br>- Tham số `toxicity` quyết định phần trăm kết nối bị ảnh hưởng, cho kiểm thử ngẫu nhiên.<br>- Đặt tên proxy theo `<app>_<env>_<datastore>_<shard>` và dùng chung một Toxiproxy (README FAQ). |
| Tiêu chí và cách kiểm | Không có ngưỡng đạt/hỏng riêng, kết quả do test của ứng dụng quyết định. Repo tự kiểm: test.yml chạy `make test` và `make bench` trên Go 1.27; analysis.yml chạy golangci-lint, shellcheck, yamllint và quét lỗ hổng theo lịch hằng tuần (đã mở cả hai). Mỗi toxic có file test riêng. |
| Giới hạn và rủi ro | MIT. README ghi API không xác thực mặc định và có thể tạo proxy tới upstream bất kỳ, có tùy chọn token (`--auth-token`); image Docker bind API ở 0.0.0.0 nên phải cô lập mạng. Cổng tạm thời trùng dải ephemeral gây lỗi ngắt quãng. Tuyên bố độ trễ dưới 100µs và khoảng 1000MB/s là số của tác giả (chưa xác minh). |
| So với | Chưa có công cụ chaos mạng nào trong kho; về cổng chất lượng test tích hợp có thể đối chiếu các hồ sơ quality-gate cùng nhóm |
| Nguồn | [README.md](https://github.com/Shopify/toxiproxy/blob/49299d8838525126e09c85ebe0ba89940a3261e5/README.md) · [LICENSE](https://github.com/Shopify/toxiproxy/blob/49299d8838525126e09c85ebe0ba89940a3261e5/LICENSE) · [CREATING_TOXICS.md](https://github.com/Shopify/toxiproxy/blob/49299d8838525126e09c85ebe0ba89940a3261e5/CREATING_TOXICS.md) · [latency.go](https://github.com/Shopify/toxiproxy/blob/49299d8838525126e09c85ebe0ba89940a3261e5/toxics/latency.go) · [reset_peer.go](https://github.com/Shopify/toxiproxy/blob/49299d8838525126e09c85ebe0ba89940a3261e5/toxics/reset_peer.go) · [test.yml](https://github.com/Shopify/toxiproxy/blob/49299d8838525126e09c85ebe0ba89940a3261e5/.github/workflows/test.yml) · [analysis.yml](https://github.com/Shopify/toxiproxy/blob/49299d8838525126e09c85ebe0ba89940a3261e5/.github/workflows/analysis.yml) |

<a id="nt-tapflow"></a>

### tapflow

| Thuộc tính | Giá trị |
|---|---|
| Repo | https://github.com/jo-duchan/tapflow |
| License | MIT (LICENSE). NOTICE nêu thành phần dẫn xuất/đóng gói theo Apache-2.0 (baguette, scrcpy-server, tinyh264, emulator_controller.proto) và danh sách nhãn từ simslim (MIT). Không có trọng số |
| Phiên bản đã đọc | `a09d6eeb78f1a0cef9bc80c37d0551c3d15b91ee` (commit 2026-11-24) |
| Kiểm chứng | 2026-11-23; code-read; đã đọc `README.md`, `LICENSE`, `NOTICE`, `packages/flow-runner/src/schema.ts`, `packages/relay/src/middleware/auth.ts`, `docs/reference/performance.md`, `.github/workflows/ci.yml`; chưa chạy upstream |
| Khoảng trống lấp | Kiểm thử mobile trên máy mô phỏng: stream iOS Simulator/Android emulator qua trình duyệt, tự host cho cả nhóm |
| Cơ chế đáng học | - Ba phần: relay tự host (phục vụ dashboard), agent macOS kết nối ra ngoài tới relay, dashboard trình duyệt; iOS chèn cảm ứng không qua WebDriverAgent.<br>- `packages/flow-runner/src/schema.ts`: flow YAML gồm các bước tapOn, assertVisible, scroll, swipe, setOrientation, clearState...; selector theo text/id/label/role; `inputSecret` đưa giá trị khi chạy, không ghi vào flow hay log; replay không gọi LLM (đang đánh dấu thử nghiệm).<br>- `relay/src/middleware/auth.ts`: JWT 7 ngày gắn với dấu vân tay mật khẩu (`pwv`) nên đổi mật khẩu thu hồi mọi phiên; chỉ localhost được vào không xác thực, agent từ máy khác dùng token phạm vi `agent`.<br>- Có MCP server và endpoint chụp màn hình REST cho CI và agent. |
| Tiêu chí và cách kiểm | Kiểm bằng máy: CI Node 22 và 24 (lint, test) và job `test-swift` riêng trên macOS (đã mở ci.yml); `docs/reference/performance.md` ghi đo độ trễ giải mã trên LAN (p50 khoảng 11 đến 17 ms) kèm cách tái lập, là số của tác giả **(chưa xác minh)**. |
| Giới hạn và rủi ro | **Mô tả của trinh sát lệch:** là máy mô phỏng/emulator chạy trên Mac của bạn, không phải thiết bị thật, và không đo hiệu năng ứng dụng, chỉ đo độ trễ luồng hình. Agent chỉ chạy trên macOS 26/27 với Xcode 26/27; relay là ranh giới tin cậy, ai tới được relay là điều khiển được thiết bị và xem bản dựng. Dự án mới (v0.x, MIT 2026), phụ thuộc cấu hình bảo mật triển khai. |
| So với | maestro (hồ sơ có sẵn, chạy flow YAML trên thiết bị/giả lập), appium-appium (điều khiển chuẩn WebDriver), genymobile-scrcpy (nguồn của luồng Android), docker-android. |
| Nguồn | [README.md](https://github.com/jo-duchan/tapflow/blob/a09d6eeb78f1a0cef9bc80c37d0551c3d15b91ee/README.md) · [LICENSE](https://github.com/jo-duchan/tapflow/blob/a09d6eeb78f1a0cef9bc80c37d0551c3d15b91ee/LICENSE) · [NOTICE](https://github.com/jo-duchan/tapflow/blob/a09d6eeb78f1a0cef9bc80c37d0551c3d15b91ee/NOTICE) · [schema.ts](https://github.com/jo-duchan/tapflow/blob/a09d6eeb78f1a0cef9bc80c37d0551c3d15b91ee/packages/flow-runner/src/schema.ts) · [auth.ts](https://github.com/jo-duchan/tapflow/blob/a09d6eeb78f1a0cef9bc80c37d0551c3d15b91ee/packages/relay/src/middleware/auth.ts) · [performance.md](https://github.com/jo-duchan/tapflow/blob/a09d6eeb78f1a0cef9bc80c37d0551c3d15b91ee/docs/reference/performance.md) · [ci.yml](https://github.com/jo-duchan/tapflow/blob/a09d6eeb78f1a0cef9bc80c37d0551c3d15b91ee/.github/workflows/ci.yml) |

<a id="n2-2026-11-24"></a>

## Nâng trần đợt hai — 23/11/2026

Hồ sơ lập trong đợt nâng trần thứ hai: đọc mã hoặc tài liệu tại commit cố định, chưa chạy upstream; mô tả của trinh sát sai ở nhiều repo nên điều ghi ở đây là điều đã đọc.

<a id="n2-flashlight"></a>

### Flashlight

| Thuộc tính | Giá trị |
|---|---|
| Repo | https://github.com/bamlab/flashlight |
| License | MIT |
| Phiên bản đã đọc | `5eeee8a8a8f64c06c707a214e2b572084201c64d` (commit 2026-11-17) |
| Kiểm chứng | 2026-11-24; code-read; đã đọc README, LICENSE, getScore.ts, cppProfiler.ts, tests.yml; chưa chạy upstream |
| Khoảng trống lấp | Kiểm thử mobile trên thiết bị và hiệu năng |
| Cơ chế đáng học | - Điểm = trung bình điểm CPU (`-0.3167*x+116`, kẹp 0..100) và điểm FPS (`fps*100/refreshRate`), nhân (1 - tỉ lệ thời gian thread CPU cao) — `core/reporter/src/reporting/getScore.ts`.<br>- Đo bằng bộ đếm chạy trên thiết bị: nhị phân C++ trả chuỗi cpu/ram/atrace/timestamp được `parseCppMeasure` tách theo `=SEPARATOR=` — `platforms/android/src/commands/cppProfiler.ts`.<br>- `flashlight test` lặp nhiều iteration và ghi trạng thái FAILURE của từng vòng; plugin `appium-helper`, `aws-device-farm` cho test tự động trên cloud (chỉ thấy tên thư mục). |
| Tiêu chí và cách kiểm | Điểm là số liên tục, không có ngưỡng đỗ/trượt tích hợp trong phần đã đọc (cờ ngưỡng chưa thấy ở `bin.ts`, chưa xác minh). Có test Jest chạy trong CI macOS (`yarn test`); không có benchmark độ chính xác của điểm. |
| Giới hạn và rủi ro | MIT (BAM, 2022). Hệ số công thức CPU là hằng số nội suy từ 3 điểm, không chuẩn hoá theo thiết bị. Đo qua adb nên cần máy thật hoặc emulator; điểm phụ thuộc thiết bị. Chế độ upload ở app.flashlight.dev đưa APK ra ngoài máy (chưa xác minh điều khoản). Telemetry: không thấy trong phần đã đọc. |
| So với | lighthouse-ci và googlechrome-lighthouse (web), maestro (luồng UI mobile) |
| Nguồn | [README.md](https://github.com/bamlab/flashlight/blob/5eeee8a8a8f64c06c707a214e2b572084201c64d/README.md) · [LICENSE](https://github.com/bamlab/flashlight/blob/5eeee8a8a8f64c06c707a214e2b572084201c64d/LICENSE) · [getScore.ts](https://github.com/bamlab/flashlight/blob/5eeee8a8a8f64c06c707a214e2b572084201c64d/packages/core/reporter/src/reporting/getScore.ts) · [cppProfiler.ts](https://github.com/bamlab/flashlight/blob/5eeee8a8a8f64c06c707a214e2b572084201c64d/packages/platforms/android/src/commands/cppProfiler.ts) · [tests.yml](https://github.com/bamlab/flashlight/blob/5eeee8a8a8f64c06c707a214e2b572084201c64d/.github/workflows/tests.yml) |

<a id="n2-patrol"></a>

### Patrol

| Thuộc tính | Giá trị |
|---|---|
| Repo | https://github.com/leancodepl/patrol |
| License | Apache-2.0 |
| Phiên bản đã đọc | `afd136cfd7f27458a5987b96f52711b3434a6f92` (commit 2026-11-10) |
| Kiểm chứng | 2026-11-24; code-read; đã đọc README, LICENSE, Automator.kt, analytics.dart, patrol_command_runner.dart, SKILL.md, patrol_mcp README, 2 workflow; chưa chạy upstream |
| Khoảng trống lấp | Kiểm thử mobile trên thiết bị và hiệu năng |
| Cơ chế đáng học | - `Automator.kt` bọc UiAutomator: `tap`, `tapOnNotification`, `allowPermissionWhileUsingApp/Once`, `denyPermission`, `enableWifi` (`svc wifi enable`) — thao tác ngoài cây widget Flutter.<br>- Hợp đồng giữa app Dart và máy chủ native sinh từ `schema.dart` bằng `patrol_gen` (thư mục `gen_from_schema`, chưa đọc nội dung).<br>- `packages/patrol_mcp` cho agent chạy/quản lý test; `skills/patrol-write-test/SKILL.md` quy định thứ tự viết test, khoá widget và chạy thường xuyên; workflow `check-skills.yaml` chạy `tool/check_skills.sh` kiểm skill. |
| Tiêu chí và cách kiểm | Test E2E chạy trên ma trận API 32 đến 36 của emulator và máy thật theo lịch 12 giờ/lần (`test-android-emulator.yaml`), kèm workflow iOS, macOS, web. Kiểm bằng máy; đã mở workflow Android, chưa mở các workflow còn lại. |
| Giới hạn và rủi ro | Apache-2.0 (mỗi gói con có LICENSE riêng, đọc LICENSE gốc và patrol_mcp, cùng nội dung Apache). CLI gửi dữ liệu dùng ẩn danh tới Google Analytics (`https://www.google-analytics.com/mp/collect`) mặc định bật; tắt bằng `PATROL_ANALYTICS_ENABLED=false`; `sendCommand` chỉ gửi khi đã có `clientId` trong file cấu hình (tạo ở lần chạy đầu), rồi dùng `envAnalyticsEnabled ?? config.enabled ?? true`; getter `enabled` trả false khi chạy CI (chưa chạy nên chưa xác nhận hành vi thực). Chỉ Flutter. Có dịch vụ trả phí của LeanCode bên cạnh bản mở. |
| So với | maestro (flow YAML đa nền tảng), flutter (integration_test gốc), appium-appium |
| Nguồn | [README.md](https://github.com/leancodepl/patrol/blob/afd136cfd7f27458a5987b96f52711b3434a6f92/README.md) · [LICENSE](https://github.com/leancodepl/patrol/blob/afd136cfd7f27458a5987b96f52711b3434a6f92/LICENSE) · [Automator.kt](https://github.com/leancodepl/patrol/blob/afd136cfd7f27458a5987b96f52711b3434a6f92/packages/patrol/android/src/main/kotlin/pl/leancode/patrol/Automator.kt) · [analytics.dart](https://github.com/leancodepl/patrol/blob/afd136cfd7f27458a5987b96f52711b3434a6f92/packages/patrol_cli/lib/src/analytics/analytics.dart) · [patrol_command_runner.dart](https://github.com/leancodepl/patrol/blob/afd136cfd7f27458a5987b96f52711b3434a6f92/packages/patrol_cli/lib/src/runner/patrol_command_runner.dart) · [SKILL.md](https://github.com/leancodepl/patrol/blob/afd136cfd7f27458a5987b96f52711b3434a6f92/skills/patrol-write-test/SKILL.md) · [README.md](https://github.com/leancodepl/patrol/blob/afd136cfd7f27458a5987b96f52711b3434a6f92/packages/patrol_mcp/README.md) · [test-android-emulator.yaml](https://github.com/leancodepl/patrol/blob/afd136cfd7f27458a5987b96f52711b3434a6f92/.github/workflows/test-android-emulator.yaml) · [check-skills.yaml](https://github.com/leancodepl/patrol/blob/afd136cfd7f27458a5987b96f52711b3434a6f92/.github/workflows/check-skills.yaml) |

<a id="n2-maestro-runner"></a>

### maestro-runner

| Thuộc tính | Giá trị |
|---|---|
| Repo | https://github.com/devicelab-dev/maestro-runner |
| License | Apache-2.0 (mã nguồn); driver APK/iOS agent của DeviceLab là proprietary |
| Phiên bản đã đọc | `35748752544f9ac021156400e087e78e31cf9cda` (commit 2026-11-23) |
| Kiểm chứng | 2026-11-24; code-read; đã đọc README, LICENSE, LICENSE-BINARIES.md, telemetry.go, appium.go, retry.go, ci.yml; chưa chạy upstream |
| Khoảng trống lấp | Kiểm thử mobile trên thiết bị và hiệu năng |
| Cơ chế đáng học | - `pkg/executor/retry.go` (`flowRetries`) chạy lại flow thất bại trong cùng run, giữ driver và agent, báo cáo ghi từng lần thử, thay cho vòng lặp ngoài đọc report.json.<br>- Pha trộn driver: `--driver devicelab` dùng agent riêng, còn lại UIAutomator2/WDA/Appium; `pkg/validator` kiểm flow trước khi chạy (chỉ thấy tên).<br>- Telemetry thiết kế dè dặt: chỉ đếm, băm một chiều danh sách file flow, `pkg/telemetry/appium.go` chỉ gửi tên nhà cung cấp cloud từ danh sách cố định, không gửi host. |
| Tiêu chí và cách kiểm | CI chạy `go test -race -timeout 25m` kèm coverage, `make fmt-check`, golangci-lint v2.13.2 (ghim), có `DO_NOT_TRACK=1` để test không gửi telemetry. Con số '~5x nhanh hơn, 14x ít bộ nhớ hơn Maestro' và '78% issue hàng đầu' là tuyên bố của tác giả (chưa xác minh); có `benchmarks/speed-baseline.json` chưa đọc. |
| Giới hạn và rủi ro | Mã Apache-2.0 nhưng `drivers/LICENSE-BINARIES.md` nói rõ agent Android/iOS của DeviceLab là proprietary: dùng miễn phí cùng maestro-runner, không được sửa, không phân phối riêng; WDA và UIAutomator2 giữ license upstream. Telemetry bật mặc định (endpoint open.devicelab.dev), tắt bằng `MAESTRO_RUNNER_NO_TELEMETRY=1` hoặc `DO_NOT_TRACK=1`. Dự án mới, phụ thuộc một nhà cung cấp; cú pháp flow bám Maestro nên lệch phiên bản có thể gây khác biệt (chưa xác minh). |
| So với | maestro (bản gốc Kotlin/JVM), appium-appium |
| Nguồn | [README.md](https://github.com/devicelab-dev/maestro-runner/blob/35748752544f9ac021156400e087e78e31cf9cda/README.md) · [LICENSE](https://github.com/devicelab-dev/maestro-runner/blob/35748752544f9ac021156400e087e78e31cf9cda/LICENSE) · [LICENSE-BINARIES.md](https://github.com/devicelab-dev/maestro-runner/blob/35748752544f9ac021156400e087e78e31cf9cda/drivers/LICENSE-BINARIES.md) · [telemetry.go](https://github.com/devicelab-dev/maestro-runner/blob/35748752544f9ac021156400e087e78e31cf9cda/pkg/telemetry/telemetry.go) · [appium.go](https://github.com/devicelab-dev/maestro-runner/blob/35748752544f9ac021156400e087e78e31cf9cda/pkg/telemetry/appium.go) · [retry.go](https://github.com/devicelab-dev/maestro-runner/blob/35748752544f9ac021156400e087e78e31cf9cda/pkg/executor/retry.go) · [ci.yml](https://github.com/devicelab-dev/maestro-runner/blob/35748752544f9ac021156400e087e78e31cf9cda/.github/workflows/ci.yml) |

<a id="n2-artillery"></a>

### Artillery

| Thuộc tính | Giá trị |
|---|---|
| Repo | https://github.com/artilleryio/artillery |
| License | MPL-2.0 (đa số); BUSL-1.1 cho module Azure |
| Phiên bản đã đọc | `664806bb60218c06c4fc34f49fdb8854de83b000` (commit 2026-10-20) |
| Kiểm chứng | 2026-11-24; code-read; đã đọc README, LICENSE.txt, LICENSE-BSL.txt, telemetry.ts, az/aci.ts, ensure plugin.ts và README, run-tests.yml; chưa chạy upstream |
| Khoảng trống lấp | Kiểm thử tải |
| Cơ chế đáng học | - `artillery-plugin-ensure` (`plugin.ts`) đánh giá điều kiện biểu thức (`filtrex`) trên chỉ số tổng hợp, thất bại thì đặt `global.artillery.suggestedExitCode = 1`; chỉ chạy ở luồng chính, bỏ qua worker.<br>- Chạy phân tán không cần hạ tầng riêng: nền tảng `lib/platform/aws-lambda`, `aws-ecs`, `az`; worker đặt `ARTILLERY_DISABLE_ENSURE` để cổng chỉ chấm một lần.<br>- Tách engine và plugin thành gói riêng: `artillery-engine-playwright`, `artillery-plugin-expect`, `apdex`, `publish-metrics`, `slack`. |
| Tiêu chí và cách kiểm | Cổng: điều kiện `ensure` trong script, mã thoát khác 0 khi trượt (theo README plugin và `plugin.ts`). CI: typecheck, ma trận test theo gói (`run-tests.yml`), job AWS riêng; chưa mở các workflow còn lại. |
| Giới hạn và rủi ro | README nêu: phần lớn mã là MPL-2.0 (copyleft theo tệp), module Azure (`platform/az/aci.ts`, `aqs-queue-consumer.ts` mang `SPDX-License-Identifier: BUSL-1.1`) chỉ dùng cho đánh giá hoặc phi sản xuất, sản xuất cần giấy phép thương mại, đổi sang MPL-2.0 sau 4 năm. Telemetry ẩn danh gửi tới us.i.posthog.com mặc định (tắt bằng `ARTILLERY_DISABLE_TELEMETRY`; có khoá PostHog trong mã). Lần push gần nhất 2026-10-20, chậm hơn các repo cùng lô. Mô tả trinh sát ghi MPL-2.0 là chưa đủ. |
| So với | grafana-k6, locustio-locust (cùng nhóm tải); gatling (hồ sơ này) |
| Nguồn | [README.md](https://github.com/artilleryio/artillery/blob/664806bb60218c06c4fc34f49fdb8854de83b000/README.md) · [LICENSE.txt](https://github.com/artilleryio/artillery/blob/664806bb60218c06c4fc34f49fdb8854de83b000/LICENSE.txt) · [LICENSE-BSL.txt](https://github.com/artilleryio/artillery/blob/664806bb60218c06c4fc34f49fdb8854de83b000/LICENSE-BSL.txt) · [telemetry.ts](https://github.com/artilleryio/artillery/blob/664806bb60218c06c4fc34f49fdb8854de83b000/packages/artillery/lib/telemetry.ts) · [aci.ts](https://github.com/artilleryio/artillery/blob/664806bb60218c06c4fc34f49fdb8854de83b000/packages/artillery/lib/platform/az/aci.ts) · [plugin.ts](https://github.com/artilleryio/artillery/blob/664806bb60218c06c4fc34f49fdb8854de83b000/packages/artillery-plugin-ensure/plugin.ts) · [README.md](https://github.com/artilleryio/artillery/blob/664806bb60218c06c4fc34f49fdb8854de83b000/packages/artillery-plugin-ensure/README.md) · [run-tests.yml](https://github.com/artilleryio/artillery/blob/664806bb60218c06c4fc34f49fdb8854de83b000/.github/workflows/run-tests.yml) |

<a id="n2-gatling"></a>

### Gatling

| Thuộc tính | Giá trị |
|---|---|
| Repo | https://github.com/gatling/gatling |
| License | Apache-2.0 (Community); gRPC/MQTT/GraphQL/JDBC dưới Gatling Enterprise Component License |
| Phiên bản đã đọc | `7ed10232bbbdc6ac15932a5ea4c28b170c68ad32` (commit 2026-11-23) |
| Kiểm chứng | 2026-11-24; code-read; đã đọc README, LICENSE.txt, AssertionBuilders.scala, RunResultProcessor.scala, StatusCode.scala, build.yml; chưa chạy upstream |
| Khoảng trống lấp | Kiểm thử tải |
| Cơ chế đáng học | - `AssertionBuilders.scala` dựng assertion có kiểu: min/max/mean/stdDev/percentile, đếm/phần trăm request lỗi, `requestsPerSec`; so sánh `lt/lte/gt/gte/between/around/deviatesAround/is/in`.<br>- `RunResultProcessor.runStatus` in từng assertion (kết quả và giá trị thực), gộp bằng AND, trả `StatusCode.AssertionsFailed` (mã 2, `StatusCode.scala`) khi trượt; `Gatling.scala` gọi `sys.exit`.<br>- Cùng một mô phỏng chạy qua plugin Maven, Gradle, sbt hoặc npm; kho chia module `gatling-core`, `-http`, `-jms`, `-redis`, `-recorder`, `-charts`. |
| Tiêu chí và cách kiểm | Cổng là assertion trong mô phỏng, trượt thì mã thoát 2 (theo `StatusCode.scala`). CI `build.yml` dựng bằng sbt trên JDK 25, action ghim theo SHA; chưa mở workflow release. |
| Giới hạn và rủi ro | Apache-2.0 cho mã Community (LICENSE.txt), nhưng README nói gRPC, MQTT, GraphQL, JDBC là phụ thuộc riêng dưới Gatling Enterprise Component License, Community bị giới hạn 5 người dùng đồng thời và 5 phút; báo cáo dùng Highcharts theo giấy phép Highsoft riêng. Mô tả trinh sát (Apache-2.0) thiếu các ngoại lệ này. Số '300.000 công ty, 30 triệu lượt tải' là tuyên bố tác giả (chưa xác minh). Phần tính năng doanh nghiệp (chạy phân tán, so sánh run) không nằm trong repo. |
| So với | grafana-k6 (script JS, Go), locustio-locust (Python), artillery (hồ sơ này) |
| Nguồn | [README.md](https://github.com/gatling/gatling/blob/7ed10232bbbdc6ac15932a5ea4c28b170c68ad32/README.md) · [LICENSE.txt](https://github.com/gatling/gatling/blob/7ed10232bbbdc6ac15932a5ea4c28b170c68ad32/LICENSE.txt) · [AssertionBuilders.scala](https://github.com/gatling/gatling/blob/7ed10232bbbdc6ac15932a5ea4c28b170c68ad32/gatling-core/src/main/scala/io/gatling/core/assertion/AssertionBuilders.scala) · [RunResultProcessor.scala](https://github.com/gatling/gatling/blob/7ed10232bbbdc6ac15932a5ea4c28b170c68ad32/gatling-app/src/main/scala/io/gatling/app/RunResultProcessor.scala) · [StatusCode.scala](https://github.com/gatling/gatling/blob/7ed10232bbbdc6ac15932a5ea4c28b170c68ad32/gatling-app/src/main/scala/io/gatling/app/cli/StatusCode.scala) · [build.yml](https://github.com/gatling/gatling/blob/7ed10232bbbdc6ac15932a5ea4c28b170c68ad32/.github/workflows/build.yml) |

<a id="n2-atheris"></a>

### Atheris

| Thuộc tính | Giá trị |
|---|---|
| Repo | https://github.com/google/atheris |
| License | Apache-2.0 |
| Phiên bản đã đọc | `e36da74cf42b5834c4e31d7cabb58d796695d29f` (commit 2026-06-17) |
| Kiểm chứng | 2026-11-24; code-read; đã đọc README.md, LICENSE, hooking.md, src/instrument_bytecode.py (đầu file), src/function_hooks.py (danh sách hàm), example_fuzzers/fuzzing_example.py, run_tests.sh, .github/workflows/builds.yaml; chưa chạy upstream |
| Khoảng trống lấp | Fuzz, mutation, chaos/resilience (fuzzer Python theo coverage) |
| Cơ chế đáng học | - Dựa trên libFuzzer; `atheris.instrument_imports()`, `@atheris.instrument_func` hoặc instrument toàn bộ để chèn đo coverage vào bytecode Python (src/instrument_bytecode.py) và cả extension native.<br>- Hàm vào `TestOneInput(data)` gọi mã cần thử; ngoại lệ không bắt được tính là lỗi (README). Hook so sánh, nhánh, phương thức `str` và biểu thức chính quy (src/function_hooks.py sinh chuỗi khớp regex) giúp fuzzer vượt điều kiện so sánh.<br>- Hỗ trợ custom mutator/crossover và protobuf (contrib/libprotobuf_mutator) cho fuzz có cấu trúc; có `FuzzedDataProvider`. |
| Tiêu chí và cách kiểm | Không có ngưỡng điểm: tiêu chí là phát hiện crash hay ngoại lệ trong thời gian chạy; README nói tích hợp OSS-Fuzz. CI chạy ruff, pytype và `run_tests.sh` (chạy từng `*_test.py`). |
| Giới hạn và rủi ro | Hỗ trợ Linux và macOS, Python 3.11-3.14 theo README, không có Windows. Cần clang/libFuzzer khớp khi fuzz native. Commit cuối 2026-06-17, cách ngày kiểm khoảng 5 tháng; phải chú ý tương thích bản Python mới vì cơ chế phụ thuộc bytecode. Fuzz chạy mã mục tiêu nên cần cô lập. |
| So với | `hypothesis` (property-based, thuần Python); `google-oss-fuzz` (hạ tầng chạy fuzz liên tục, Atheris là một engine). |
| Nguồn | [README](https://github.com/google/atheris/blob/e36da74cf42b5834c4e31d7cabb58d796695d29f/README.md) · [LICENSE](https://github.com/google/atheris/blob/e36da74cf42b5834c4e31d7cabb58d796695d29f/LICENSE) · [hooking.md](https://github.com/google/atheris/blob/e36da74cf42b5834c4e31d7cabb58d796695d29f/hooking.md) · [src/instrument_bytecode.py](https://github.com/google/atheris/blob/e36da74cf42b5834c4e31d7cabb58d796695d29f/src/instrument_bytecode.py) · [src/function_hooks.py](https://github.com/google/atheris/blob/e36da74cf42b5834c4e31d7cabb58d796695d29f/src/function_hooks.py) · [example_fuzzers/fuzzing_example.py](https://github.com/google/atheris/blob/e36da74cf42b5834c4e31d7cabb58d796695d29f/example_fuzzers/fuzzing_example.py) · [run_tests.sh](https://github.com/google/atheris/blob/e36da74cf42b5834c4e31d7cabb58d796695d29f/run_tests.sh) · [.github/workflows/builds.yaml](https://github.com/google/atheris/blob/e36da74cf42b5834c4e31d7cabb58d796695d29f/.github/workflows/builds.yaml) |

<a id="n2-mutmut"></a>

### mutmut

| Thuộc tính | Giá trị |
|---|---|
| Repo | https://github.com/boxed/mutmut |
| License | BSD-3-Clause |
| Phiên bản đã đọc | `2c034f20539ed7f460ea749db036e60a23f06b19` (commit 2026-11-19) |
| Kiểm chứng | 2026-11-24; code-read; đã đọc README.rst, LICENSE, ARCHITECTURE.rst, pyproject.toml (dòng version/license), src/mutmut/configuration.py, mutation/mutators.py, mutation/trampoline.py, `__main__.py` (đoạn export_cicd_stats, thoát mã), .github/workflows/tests.yml (đoạn đầu); chưa chạy upstream |
| Khoảng trống lấp | Fuzz, mutation, chaos/resilience (mutation testing Python) |
| Cơ chế đáng học | - Các bước của `mutmut run` (ARCHITECTURE.rst): sinh thư mục `mutants/`, thu thống kê test nào chạm mutant nào, chạy test sạch, chạy bước ép lỗi để chắc cơ chế mutant có hiệu lực, rồi từng mutant chạy trong tiến trình fork riêng.<br>- Mutant nằm trong cùng file mã, chọn bằng trạng thái tiến trình và biến môi trường `MUTANT_UNDER_TEST` (mutation/trampoline.py); nhờ đó chỉ chạy test có chạm tới mutant.<br>- Các toán tử trong mutation/mutators.py: số, chuỗi, lambda, bỏ đối số, đổi phép toán, đổi từ khóa, `if` biểu thức, `match`; cấu hình `do_not_mutate`, `mutate_only_covered_lines`, `type_check_command`. |
| Tiêu chí và cách kiểm | Kết quả lưu trong `.meta`; `mutmut export-cicd-stats` ghi `mutants/mutmut-cicd-stats.json` (killed, survived, total, no_tests, timeout...) để chặn PR; không thấy ngưỡng điểm hay mã thoát theo mutant sống sót trong mã đã đọc, ngưỡng do CI tự so. CI chạy pre-commit và pytest trên Python 3.10-3.15. |
| Giới hạn và rủi ro | Cần hệ có `fork` (Windows phải qua WSL, README). README nói không mutate mã ngoài hàm trong bản 3+ (muốn thế dùng mutmut 2). Chạy test nhiều lần nên tốn thời gian; test có tác dụng phụ ngoài có thể bị mutant kích hoạt. License BSD-3-Clause, không telemetry trong phần đã đọc. |
| So với | `strykerjs` (mutation JS); `cargo-mutants` (Rust); `hypothesis` (bổ sung cho test). |
| Nguồn | [README.rst](https://github.com/boxed/mutmut/blob/2c034f20539ed7f460ea749db036e60a23f06b19/README.rst) · [LICENSE](https://github.com/boxed/mutmut/blob/2c034f20539ed7f460ea749db036e60a23f06b19/LICENSE) · [ARCHITECTURE.rst](https://github.com/boxed/mutmut/blob/2c034f20539ed7f460ea749db036e60a23f06b19/ARCHITECTURE.rst) · [pyproject.toml](https://github.com/boxed/mutmut/blob/2c034f20539ed7f460ea749db036e60a23f06b19/pyproject.toml) · [src/mutmut/configuration.py](https://github.com/boxed/mutmut/blob/2c034f20539ed7f460ea749db036e60a23f06b19/src/mutmut/configuration.py) · [src/mutmut/mutation/mutators.py](https://github.com/boxed/mutmut/blob/2c034f20539ed7f460ea749db036e60a23f06b19/src/mutmut/mutation/mutators.py) · [src/mutmut/mutation/trampoline.py](https://github.com/boxed/mutmut/blob/2c034f20539ed7f460ea749db036e60a23f06b19/src/mutmut/mutation/trampoline.py) · [`src/mutmut/__main__.py`](https:`//github.com/boxed/mutmut/blob/2c034f20539ed7f460ea749db036e60a23f06b19/src/mutmut/__main__.py`) · [.github/workflows/tests.yml](https://github.com/boxed/mutmut/blob/2c034f20539ed7f460ea749db036e60a23f06b19/.github/workflows/tests.yml) |

<a id="n2-cargo-mutants"></a>

### cargo-mutants

| Thuộc tính | Giá trị |
|---|---|
| Repo | https://github.com/sourcefrog/cargo-mutants |
| License | MIT |
| Phiên bản đã đọc | `6c720ae82a1784b84cfa06066f7b0d59ed1798d0` (commit 2026-10-19) |
| Kiểm chứng | 2026-11-24; code-read; đã đọc README.md, LICENSE, Cargo.toml, src/exit_code.rs, book/src/exit-codes.md, how-it-works.md, mutants.md, ci.md, cautions.md, mutants-out.md, .github/workflows/tests.yml (các bước run); chưa chạy upstream |
| Khoảng trống lấp | Fuzz, mutation, chaos/resilience (mutation testing Rust) |
| Cơ chế đáng học | - Phân tích mã bằng `syn`, sinh mutant theo kiểu trả về (thay thân hàm bằng giá trị đoán), toán tử nhị phân, một ngôi, nhánh match, điều kiện match, trường struct (book/src/mutants.md); áp dụng bằng sửa văn bản để giữ nguyên định dạng.<br>- Chạy trong bản sao cây mã: kiểm baseline `cargo test`, với mỗi mutant `cargo test --no-run` (không biên dịch được thì bỏ), rồi `cargo test` (book/src/how-it-works.md).<br>- `--in-diff` chỉ thử mutant trong diff của PR; `--iterate`, `--shard`, `--jobs`, hỗ trợ nextest; kết quả máy đọc nằm ở `mutants.out` (mutants.json, outcomes.json, missed.txt). |
| Tiêu chí và cách kiểm | Mã thoát cho CI định nghĩa trong src/exit_code.rs: 0 mọi mutant bị bắt, 2 có mutant sống sót, 3 timeout, 4 baseline hỏng, 5 và 6 lỗi diff, 70 lỗi nội bộ; không cần shell tự so điểm. CI repo chạy cargo fmt, test, build nhiều target (tests.yml). |
| Giới hạn và rủi ro | Chỉ phủ kiểu mutant nêu trong tài liệu, hàm `unsafe`, hàm test và hàm có `#[mutants::skip]` bị loại; mutant tương đương gây dương tính giả. Rủi ro tác dụng phụ của test: tài liệu cautions.md khuyên chạy trong môi trường cô lập, nhất là khi dùng `--in-place`. Bảo trì tích cực (v27.1.0, MSRV Rust 1.88). Giới hạn Rust nên chỉ hợp với dự án Rust. |
| So với | `mutmut` (Python); `strykerjs` (JS); `hypothesis` (property-based). |
| Nguồn | [README](https://github.com/sourcefrog/cargo-mutants/blob/6c720ae82a1784b84cfa06066f7b0d59ed1798d0/README.md) · [LICENSE](https://github.com/sourcefrog/cargo-mutants/blob/6c720ae82a1784b84cfa06066f7b0d59ed1798d0/LICENSE) · [Cargo.toml](https://github.com/sourcefrog/cargo-mutants/blob/6c720ae82a1784b84cfa06066f7b0d59ed1798d0/Cargo.toml) · [src/exit_code.rs](https://github.com/sourcefrog/cargo-mutants/blob/6c720ae82a1784b84cfa06066f7b0d59ed1798d0/src/exit_code.rs) · [book/src/exit-codes.md](https://github.com/sourcefrog/cargo-mutants/blob/6c720ae82a1784b84cfa06066f7b0d59ed1798d0/book/src/exit-codes.md) · [book/src/how-it-works.md](https://github.com/sourcefrog/cargo-mutants/blob/6c720ae82a1784b84cfa06066f7b0d59ed1798d0/book/src/how-it-works.md) · [book/src/mutants.md](https://github.com/sourcefrog/cargo-mutants/blob/6c720ae82a1784b84cfa06066f7b0d59ed1798d0/book/src/mutants.md) · [book/src/ci.md](https://github.com/sourcefrog/cargo-mutants/blob/6c720ae82a1784b84cfa06066f7b0d59ed1798d0/book/src/ci.md) · [book/src/cautions.md](https://github.com/sourcefrog/cargo-mutants/blob/6c720ae82a1784b84cfa06066f7b0d59ed1798d0/book/src/cautions.md) · [book/src/mutants-out.md](https://github.com/sourcefrog/cargo-mutants/blob/6c720ae82a1784b84cfa06066f7b0d59ed1798d0/book/src/mutants-out.md) · [.github/workflows/tests.yml](https://github.com/sourcefrog/cargo-mutants/blob/6c720ae82a1784b84cfa06066f7b0d59ed1798d0/.github/workflows/tests.yml) |

<a id="n2-msw"></a>

### Mock Service Worker

| Thuộc tính | Giá trị |
|---|---|
| Repo | https://github.com/mswjs/msw |
| License | MIT |
| Phiên bản đã đọc | `b3df8504adc30538e9634a46b7303a850a817928` (commit 2026-11-18) |
| Kiểm chứng | 2026-11-24; code-read; đã đọc README.md, LICENSE.md, package.json, src/core/shared-options.ts, src/core/experimental/on-unhandled-frame.ts, test/memory/2735-memory-leak.memory.test.ts, decisions/jest-support.md, .github/workflows/ci.yml, .github/workflows/smoke-test.yml; chưa chạy upstream |
| Khoảng trống lấp | Mock API và kiểm thử cho frontend; chặn gọi mạng ngoài ý muốn |
| Cơ chế đáng học | - Tuỳ chọn `onUnhandledFrame: 'bypass' \| 'warn' \| 'error'` hoặc callback có `defaults` (`src/core/shared-options.ts`, `on-unhandled-frame.ts`); `server.listen({onUnhandledFrame: 'error'})` làm test hỏng khi có request chưa mock.<br>- Test bộ nhớ riêng (`test:memory`): bắn 5000 request, đo số listener và khẳng định delta dưới 5% (`test/memory/2735-memory-leak.memory.test.ts`).<br>- Thư mục `decisions/` ghi quyết định thiết kế (không hỗ trợ Jest chính thức, cách phát hành, phiên bản TypeScript).<br>- Dự án Playwright, test module Node/browser và `smoke-test.sh` chạy ví dụ sau CI (`ci.yml`, `smoke-test.yml`). |
| Tiêu chí và cách kiểm | CI (ci.yml): ma trận Node 22/24/26, `oxlint`, build, vitest, Playwright; smoke-test ví dụ chạy sau khi CI trên main thành công. Kiểm bằng máy đầy đủ; không có ngưỡng coverage hoặc kích thước đã thấy. |
| Giới hạn và rủi ro | MIT. Không hỗ trợ chính thức Jest, Deno, Bun (decisions/jest-support.md). Yêu cầu Node 22.12+. Bản 3.0.7; API đổi tên so với v2 (onUnhandledRequest thành onUnhandledFrame, theo mã đọc), cẩn thận khi theo tài liệu cũ. |
| So với | `playwright`, `shopify-toxiproxy`, `hypothesis` |
| Nguồn | [README.md](https://github.com/mswjs/msw/blob/b3df8504adc30538e9634a46b7303a850a817928/README.md) · [LICENSE.md](https://github.com/mswjs/msw/blob/b3df8504adc30538e9634a46b7303a850a817928/LICENSE.md) · [package.json](https://github.com/mswjs/msw/blob/b3df8504adc30538e9634a46b7303a850a817928/package.json) · [shared-options.ts](https://github.com/mswjs/msw/blob/b3df8504adc30538e9634a46b7303a850a817928/src/core/shared-options.ts) · [on-unhandled-frame.ts](https://github.com/mswjs/msw/blob/b3df8504adc30538e9634a46b7303a850a817928/src/core/experimental/on-unhandled-frame.ts) · [2735-memory-leak.memory.test.ts](https://github.com/mswjs/msw/blob/b3df8504adc30538e9634a46b7303a850a817928/test/memory/2735-memory-leak.memory.test.ts) · [jest-support.md](https://github.com/mswjs/msw/blob/b3df8504adc30538e9634a46b7303a850a817928/decisions/jest-support.md) · [ci.yml](https://github.com/mswjs/msw/blob/b3df8504adc30538e9634a46b7303a850a817928/.github/workflows/ci.yml) · [smoke-test.yml](https://github.com/mswjs/msw/blob/b3df8504adc30538e9634a46b7303a850a817928/.github/workflows/smoke-test.yml) |

<a id="n2-detox"></a>

### Detox

| Thuộc tính | Giá trị |
|---|---|
| Repo | https://github.com/wix/Detox |
| License | MIT |
| Phiên bản đã đọc | `667efcb6e7dda59b390f1707ceeb546414869a97` (commit 2026-11-02) |
| Kiểm chứng | 2026-11-24; code-read; đã đọc README.md, detox/LICENSE, docs/articles/how-detox-works.md, docs/articles/design-principles.md, detox/jest.config.js, detox/src/pilot/DetoxPilot.js, docs/pilot/testing-with-pilot.md, .github/workflows/rapid-test.yml, .github/workflows/release-checks.yml; chưa chạy upstream |
| Khoảng trống lấp | Phát hành mobile: kiểm thử E2E trên thiết bị |
| Cơ chế đáng học | - Đồng bộ tự động: Detox theo dõi request, main queue, layout, timer, animation, JS thread, bridge rồi mới chạy bước kế (`docs/articles/how-detox-works.md`).<br>- Kiến trúc hai phần: app có mã native Detox và test chạy trên Node, nói chuyện qua websocket qua một server trung gian (`detox/src/client`, `server`).<br>- Pilot: viết bước bằng ngôn ngữ tự nhiên qua LLM, bọc `@wix-pilot/core` với driver Detox (`detox/src/pilot/DetoxPilot.js`); tài liệu ghi rõ đang phát triển.<br>- Ngưỡng coverage toàn cục 100% cho statements/branches/functions/lines với `jest --coverage` (`detox/jest.config.js`). |
| Tiêu chí và cách kiểm | Workflow rapid-test: lint mã nguồn và dự án test, test kiểu, unit, integration, generation test, trên Linux và Windows (đã mở). Không tìm thấy ktlint/detekt trong gradle/yml/json (đã grep), nên mô tả "lint Kotlin" của trinh sát chưa đúng. E2E trên thiết bị thật nằm ngoài rapid-test (chưa xác minh). |
| Giới hạn và rủi ro | MIT. Pilot cần khoá LLM và gửi nội dung màn hình/bước đến nhà cung cấp mô hình (suy ra từ thiết kế, chưa xác minh). Cần Xcode/Android SDK, build native; bản 20.51.4. Chỉ phù hợp app có thể gắn mã native Detox (chủ yếu React Native). |
| So với | `maestro`, `appium-appium`, `playwright` |
| Nguồn | [README.md](https://github.com/wix/Detox/blob/667efcb6e7dda59b390f1707ceeb546414869a97/README.md) · [LICENSE](https://github.com/wix/Detox/blob/667efcb6e7dda59b390f1707ceeb546414869a97/detox/LICENSE) · [how-detox-works.md](https://github.com/wix/Detox/blob/667efcb6e7dda59b390f1707ceeb546414869a97/docs/articles/how-detox-works.md) · [design-principles.md](https://github.com/wix/Detox/blob/667efcb6e7dda59b390f1707ceeb546414869a97/docs/articles/design-principles.md) · [jest.config.js](https://github.com/wix/Detox/blob/667efcb6e7dda59b390f1707ceeb546414869a97/detox/jest.config.js) · [DetoxPilot.js](https://github.com/wix/Detox/blob/667efcb6e7dda59b390f1707ceeb546414869a97/detox/src/pilot/DetoxPilot.js) · [testing-with-pilot.md](https://github.com/wix/Detox/blob/667efcb6e7dda59b390f1707ceeb546414869a97/docs/pilot/testing-with-pilot.md) · [rapid-test.yml](https://github.com/wix/Detox/blob/667efcb6e7dda59b390f1707ceeb546414869a97/.github/workflows/rapid-test.yml) · [release-checks.yml](https://github.com/wix/Detox/blob/667efcb6e7dda59b390f1707ceeb546414869a97/.github/workflows/release-checks.yml) |

<a id="n2-aflplusplus"></a>

### AFL++

| Thuộc tính | Giá trị |
|---|---|
| Repo | https://github.com/AFLplusplus/AFLplusplus |
| License | AGPL-3.0-or-later (cả repo); nhiều file riêng Apache-2.0 theo SPDX; có giấy phép thương mại tuỳ chọn |
| Phiên bản đã đọc | `d798677805de81b50aa8f45beb0342ae1617b9d8` (commit 2026-11-15) |
| Kiểm chứng | 2026-11-24; code-read; đã đọc README.md, LICENSE, LICENSING.md, instrumentation/README.cmplog.md, src/afl-fuzz.c, src/afl-main.c, instrumentation/afl-compiler-rt.o.c, test/test-basic.sh, .github/workflows/ci.yml; chưa chạy upstream |
| Khoảng trống lấp | Fuzz coverage-guided cho C/C++ và nhị phân; kiểm thử thuộc tính mức hệ thống |
| Cơ chế đáng học | - Instrumentation bằng pass LLVM/GCC chèn bộ đếm cạnh; runtime nhẹ ở `instrumentation/afl-compiler-rt.o.c` (Apache-2.0).<br>- CmpLog: build thêm một bản có `AFL_LLVM_CMPLOG`, ghi toán hạng so sánh vào bộ nhớ chung cho mutator input-to-state (`instrumentation/README.cmplog.md`).<br>- Chế độ persistent, custom mutator, QEMU/Frida/Nyx/Unicorn cho nhị phân không có mã nguồn (thư mục gốc, README).<br>- Test hồi quy bằng shell: biên dịch ca thử với các cờ `AFL_*` rồi so bản đồ cạnh `afl-showmap` (`test/test-basic.sh`). |
| Tiêu chí và cách kiểm | CI chạy build qua nhiều bản LLVM (14 đến 21), chạy `make tests` có ASAN, kiểm định dạng code (đã mở ci.yml; workflow khác chỉ biết tên). Không có ngưỡng; fuzz không chứng minh vắng lỗi. |
| Giới hạn và rủi ro | LICENSE là AGPL-3.0. LICENSING.md và SPDX từng file: `afl-fuzz.c` và `afl-compiler-rt.o.c` ghi Apache-2.0, còn `afl-main.c`, `hashmap.c`, `afl-fuzz-mopt-adaptive.c` ghi AGPL, đếm 15 file AGPL và 129 file Apache ở thời điểm đọc, README nói bản nhị phân `afl-fuzz` là AGPL vì liên kết các file AGPL. Runtime liên kết vào mục tiêu là Apache-2.0 (tuyên bố tác giả). Nhúng/đổi và cung cấp qua mạng cần nghĩa vụ mã nguồn AGPL. Cần quyền cấu hình hệ thống (`afl-system-config`) để chạy nhanh. |
| So với | `google-oss-fuzz`, `hypothesis`, `shopify-toxiproxy` |
| Nguồn | [README.md](https://github.com/AFLplusplus/AFLplusplus/blob/d798677805de81b50aa8f45beb0342ae1617b9d8/README.md) · [LICENSE](https://github.com/AFLplusplus/AFLplusplus/blob/d798677805de81b50aa8f45beb0342ae1617b9d8/LICENSE) · [LICENSING.md](https://github.com/AFLplusplus/AFLplusplus/blob/d798677805de81b50aa8f45beb0342ae1617b9d8/LICENSING.md) · [README.cmplog.md](https://github.com/AFLplusplus/AFLplusplus/blob/d798677805de81b50aa8f45beb0342ae1617b9d8/instrumentation/README.cmplog.md) · [afl-fuzz.c](https://github.com/AFLplusplus/AFLplusplus/blob/d798677805de81b50aa8f45beb0342ae1617b9d8/src/afl-fuzz.c) · [afl-main.c](https://github.com/AFLplusplus/AFLplusplus/blob/d798677805de81b50aa8f45beb0342ae1617b9d8/src/afl-main.c) · [afl-compiler-rt.o.c](https://github.com/AFLplusplus/AFLplusplus/blob/d798677805de81b50aa8f45beb0342ae1617b9d8/instrumentation/afl-compiler-rt.o.c) · [test-basic.sh](https://github.com/AFLplusplus/AFLplusplus/blob/d798677805de81b50aa8f45beb0342ae1617b9d8/test/test-basic.sh) · [ci.yml](https://github.com/AFLplusplus/AFLplusplus/blob/d798677805de81b50aa8f45beb0342ae1617b9d8/.github/workflows/ci.yml) |

<a id="n2-chaostoolkit"></a>

### Chaos Toolkit

| Thuộc tính | Giá trị |
|---|---|
| Repo | https://github.com/chaostoolkit/chaostoolkit |
| License | Apache-2.0 |
| Phiên bản đã đọc | `2ff559be6b378f83f0e9ddf951e577eb1e97cdcd` (commit 2026-10-05) |
| Kiểm chứng | 2026-11-24; code-read; đã đọc README.md, LICENSE, pyproject.toml, CHANGELOG.md, chaostoolkit/check.py, chaostoolkit/commands/root.py, chaostoolkit/skills/chaostoolkit-experiment/SKILL.md, chaostoolkit/skills/chaostoolkit-network-faults/SKILL.md, tests/fixtures/check-file-exists.json, .github/workflows/build.yaml; chưa chạy upstream |
| Khoảng trống lấp | Chaos/lỗi giả lập có giả thuyết trạng thái ổn định máy kiểm được |
| Cơ chế đáng học | - Tài liệu thí nghiệm gồm `steady-state-hypothesis` (probe với `tolerance`), `method`, `rollbacks`; provider kiểu `python` hoặc `process` (`tests/fixtures/check-file-exists.json`).<br>- Khai báo phụ thuộc Python trong thí nghiệm (`runtime.python.dependencies`), chạy trong môi trường `uv` tách, không sửa cài đặt hiện có (README, `commands/root.py`).<br>- Skill agent `chaostoolkit-experiment`: bắt hỏi câu có thể bị bác bỏ, steady state từ dữ liệu thật như SLO, không đụng production nếu người dùng chưa gọi tên và duyệt kế hoạch (`SKILL.md`, CHANGELOG 1.21.4).<br>- Skill `chaostoolkit-network-faults`: mọi lỗi mạng qua `fault`/`faultlib` (cần Python 3.14+), cấm `tc`, `iptables`, toxiproxy. |
| Tiêu chí và cách kiểm | CI build.yaml: `pdm lock --check`, lint, `pytest` trên Python 3.12-3.14, Ubuntu và macOS (đã mở). Thí nghiệm tự nó cho kết quả đạt/lệch giả thuyết, có exit code theo journal (chưa kiểm chi tiết mã thoát). |
| Giới hạn và rủi ro | Apache-2.0. Phone-home: `check_newer_version` gửi phiên bản hiện tại và tên lệnh tới `releases.chaostoolkit.org` mỗi lần chạy (timeout 2 giây), tắt bằng `--no-version-check` (`check.py`, `root.py`). Provider `process` chạy lệnh tuỳ ý: thí nghiệm là mã, phải review. Tần suất phát hành thấp (1.21.4 ngày 2026-10-05). Hệ sinh thái nằm ở extension riêng, chưa đọc. |
| So với | `shopify-toxiproxy`, `hypothesis` |
| Nguồn | [README.md](https://github.com/chaostoolkit/chaostoolkit/blob/2ff559be6b378f83f0e9ddf951e577eb1e97cdcd/README.md) · [LICENSE](https://github.com/chaostoolkit/chaostoolkit/blob/2ff559be6b378f83f0e9ddf951e577eb1e97cdcd/LICENSE) · [pyproject.toml](https://github.com/chaostoolkit/chaostoolkit/blob/2ff559be6b378f83f0e9ddf951e577eb1e97cdcd/pyproject.toml) · [CHANGELOG.md](https://github.com/chaostoolkit/chaostoolkit/blob/2ff559be6b378f83f0e9ddf951e577eb1e97cdcd/CHANGELOG.md) · [check.py](https://github.com/chaostoolkit/chaostoolkit/blob/2ff559be6b378f83f0e9ddf951e577eb1e97cdcd/chaostoolkit/check.py) · [root.py](https://github.com/chaostoolkit/chaostoolkit/blob/2ff559be6b378f83f0e9ddf951e577eb1e97cdcd/chaostoolkit/commands/root.py) · [SKILL.md](https://github.com/chaostoolkit/chaostoolkit/blob/2ff559be6b378f83f0e9ddf951e577eb1e97cdcd/chaostoolkit/skills/chaostoolkit-experiment/SKILL.md) · [SKILL.md](https://github.com/chaostoolkit/chaostoolkit/blob/2ff559be6b378f83f0e9ddf951e577eb1e97cdcd/chaostoolkit/skills/chaostoolkit-network-faults/SKILL.md) · [check-file-exists.json](https://github.com/chaostoolkit/chaostoolkit/blob/2ff559be6b378f83f0e9ddf951e577eb1e97cdcd/tests/fixtures/check-file-exists.json) · [build.yaml](https://github.com/chaostoolkit/chaostoolkit/blob/2ff559be6b378f83f0e9ddf951e577eb1e97cdcd/.github/workflows/build.yaml) |

<a id="n2-stryker-net"></a>

### Stryker.NET

| Thuộc tính | Giá trị |
|---|---|
| Repo | https://github.com/stryker-mutator/stryker-net |
| License | Apache-2.0 |
| Phiên bản đã đọc | `8072f0c5cdbb64b35989102ebd45ffdb23f60eba` (commit 2026-11-23) |
| Kiểm chứng | 2026-11-24; code-read; đã đọc README.md, LICENSE, AGENTS.md, src/Stryker.Core/Stryker.Core/Mutators/BinaryExpressionMutator.cs, src/Stryker.Configuration/Options/Inputs/ThresholdBreakInput.cs, src/Stryker.Configuration/ExitCodes.cs, .github/workflows/stryker-on-stryker.yaml, .github/workflows/unit-test.yaml, .github/skills/run-stryker/SKILL.md; chưa chạy upstream |
| Khoảng trống lấp | Kiểm thử mutation cho hệ sinh thái .NET (không phải JVM) |
| Cơ chế đáng học | - `src/Stryker.Core/Stryker.Core/Mutators/` có 26 mutator (ví dụ `BinaryExpressionMutator.cs` ánh xạ `SyntaxKind` sang các `SyntaxKind` thay thế theo nhóm Arithmetic, Equality, Logical, Bitwise; bỏ qua phép cộng chuỗi).<br>- `src/Stryker.Core/Stryker.Core/MutantFilters/` gồm lọc theo mã sinh tự động, khối bỏ qua, pattern file, `SinceMutantFilter` và `BaselineMutantFilter`.<br>- `src/Stryker.Core/Stryker.Core/Reporters/` có báo cáo HTML, JSON, markdown, GitLab quality và dashboard.<br>- `.github/skills/run-stryker/SKILL.md` là skill hướng dẫn agent chạy Stryker từ terminal. |
| Tiêu chí và cách kiểm | `ThresholdHighInput` mặc định 80, `ThresholdLowInput` mặc định 60, `ThresholdBreakInput` mặc định 0 (break phải không lớn hơn low). Điểm dưới break làm tiến trình thoát mã 2 (`ExitCodes.BreakThresholdViolated`). CI: `unit-test.yaml` chạy trên ba hệ điều hành, `integration-test.yaml` theo ma trận, `stryker-on-stryker.yaml` chạy Stryker trên chính từng dự án mỗi đêm. Kiểm bằng máy. |
| Giới hạn và rủi ro | Mặc định break bằng 0 nên cổng không chặn gì nếu chưa đặt ngưỡng. Mutation chậm trên solution lớn. Báo cáo lên Stryker Dashboard (https://dashboard.stryker-mutator.io) là tùy chọn, dữ liệu rời máy chỉ khi bật reporter dashboard. README ghi phiên bản .NET tối thiểu cũ (dotnet core 1.1) nhưng tested chỉ tới 3.1 (README lạc hậu so với CI dùng .NET 10; chưa xác minh phạm vi hỗ trợ thật). Bảo trì tích cực. |
| So với | `strykerjs` (cùng họ, cho JS/TS; cũng đã có trong kho); khác ngôn ngữ nên cơ chế mutator khác (Roslyn so với AST JS). |
| Nguồn | [README.md](https://github.com/stryker-mutator/stryker-net/blob/8072f0c5cdbb64b35989102ebd45ffdb23f60eba/README.md) · [LICENSE](https://github.com/stryker-mutator/stryker-net/blob/8072f0c5cdbb64b35989102ebd45ffdb23f60eba/LICENSE) · [AGENTS.md](https://github.com/stryker-mutator/stryker-net/blob/8072f0c5cdbb64b35989102ebd45ffdb23f60eba/AGENTS.md) · [BinaryExpressionMutator.cs](https://github.com/stryker-mutator/stryker-net/blob/8072f0c5cdbb64b35989102ebd45ffdb23f60eba/src/Stryker.Core/Stryker.Core/Mutators/BinaryExpressionMutator.cs) · [ThresholdBreakInput.cs](https://github.com/stryker-mutator/stryker-net/blob/8072f0c5cdbb64b35989102ebd45ffdb23f60eba/src/Stryker.Configuration/Options/Inputs/ThresholdBreakInput.cs) · [ExitCodes.cs](https://github.com/stryker-mutator/stryker-net/blob/8072f0c5cdbb64b35989102ebd45ffdb23f60eba/src/Stryker.Configuration/ExitCodes.cs) · [stryker-on-stryker.yaml](https://github.com/stryker-mutator/stryker-net/blob/8072f0c5cdbb64b35989102ebd45ffdb23f60eba/.github/workflows/stryker-on-stryker.yaml) · [unit-test.yaml](https://github.com/stryker-mutator/stryker-net/blob/8072f0c5cdbb64b35989102ebd45ffdb23f60eba/.github/workflows/unit-test.yaml) · [SKILL.md](https://github.com/stryker-mutator/stryker-net/blob/8072f0c5cdbb64b35989102ebd45ffdb23f60eba/.github/skills/run-stryker/SKILL.md) |
