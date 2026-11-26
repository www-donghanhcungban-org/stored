# 33 · Reliability, Observability & Operations: phần mềm chạy được, phát hiện hỏng và phục hồi được

> Phạm vi nghiên cứu **2026-11-04**: đọc mã, LICENSE, CI và đường gọi được dẫn tại SHA cố định; không cài/chạy upstream, không phát sinh sự cố hay đo RTO/RPO. Đây là hồ sơ chọn và tích hợp công cụ cho xưởng phần mềm, không phải bộ runbook đã được thử trên production.

## 1. Vì sao xưởng cần một mục vận hành riêng

[Mục 07](../07-eval-observability/README.md) đánh giá ứng dụng LLM; [mục 13](../13-dev-stack-devops/README.md) giữ dev stack; [mục 32](../32-platform-delivery-engineering/README.md) lo hạ tầng/phát hành. Mục này giữ hợp đồng **sau khi phát hành**: điều gì là thành công đối với người dùng, ai nhận cảnh báo, dữ liệu đi đâu, khi nào dừng rollout, và khôi phục thế nào. App vừa trả HTTP 200 chưa chứng minh nghiệp vụ đúng, queue không kẹt hay backup dùng được.

| Năng lực xưởng | Artifact tối thiểu ở dự án nhận | Cổng có thể làm thất bại |
|---|---|---|
| Biết ai chịu trách nhiệm | Service owner, dependency map, on-call/runbook, độ quan trọng | Service không có người xử lý/đường escalation; runbook không có quyền và điều kiện thực thi |
| Đo tác vụ người dùng | SLI query, numerator/denominator, latency boundary, window, exclusions | Query sai sample; drop telemetry tạo tỷ lệ đẹp; tenant/route quan trọng biến mất |
| Quyết định SLO | Objective và error-budget policy được chủ sản phẩm/ops chấp nhận | Metric không đại diện hành trình người dùng; mục tiêu đặt sau khi xem kết quả |
| Thu telemetry có giới hạn | Schema, allowlist/redaction, retention, access, cardinality/cost budget | Canary secret/PII tới exporter; queue/drop hoặc metric cardinality vượt ngân sách |
| Phát hiện và xử lý sự cố | Alert rule fixtures, routing/ack, timeline incident, escalation | Alert tạo đúng nhưng không đến nơi/không được nhận; silence không hết hạn |
| Phục hồi | Backup ID, restore receipt, RPO/RTO mục tiêu/đo được, kết quả nghiệp vụ | Snapshot tồn tại nhưng key/quyền/dependency không khôi phục được |

Không có một bộ công cụ bắt buộc cho mọi xưởng: service nhỏ có thể bắt đầu từ metrics có chủ sở hữu, log có cấu trúc và restore drill. Chỉ thêm tracing/SLO operator/chaos khi chúng giải một failure mode đã xác định.

## 2. Chọn công cụ theo quyết định cần đưa ra

| Nhiệm vụ | Lựa chọn đã đọc | So với lựa chọn khác | Điều kiện vận hành |
|---|---|---|---|
| Chuẩn hoá/giới hạn telemetry trước exporter | OpenTelemetry Collector Contrib, phạm vi redaction processor | OTel SDK tại source giảm dữ liệu từ đầu; filter/transform processor phục vụ policy khác, không tự có cùng semantics | Distribution phải chứa component, pipeline phải thực sự tham chiếu processor đúng thứ tự |
| Generate SLO rules theo GitOps/CI | Sloth | Pyrra nếu cần UI/budget view; rule Prometheus viết tay nếu số SLO rất nhỏ | Pin generator/plugins; validate, rule tests rồi rollout; YAML hợp lệ không chứng minh SLI đúng |
| SLO UI + operator/FS backend | Pyrra | Sloth ưu tiên compilation/CLI; Prometheus/Grafana dùng trực tiếp nếu chưa cần operator | RBAC, rule discovery và query backend phải khớp; kiểm cardinality khi grouping |
| Backup file/object | [restic ở mục 09](../09-engineering-checklists/README.md#operations-recovery-cost-evidence) | Snapshot của storage/DB hoặc Velero theo môi trường | Metadata check khác đọc payload và khác restore ứng dụng; bảo vệ key và retention |
| Backup Kubernetes resource/PV | [Velero ở mục 09](../09-engineering-checklists/README.md#operations-recovery-cost-evidence) | Backup native DB cho tính nhất quán nghiệp vụ | Restore cả service dependency và kiểm record/transaction; không chỉ đếm pod Running |

## 3. Hồ sơ đọc mã

<a id="otel-collector-egress"></a>

### 3.1 OpenTelemetry Collector Contrib: telemetry egress có policy cụ thể

| Thuộc tính | Giá trị |
|---|---|
| Repo / tổ chức | [open-telemetry/opentelemetry-collector-contrib](https://github.com/open-telemetry/opentelemetry-collector-contrib), dự án OpenTelemetry |
| Phiên bản / license | `970f597792f2e60786e480dad4598b1078ba5627` · Apache-2.0 · đọc 2026-11-04 |
| Phạm vi `code-read` | `processor/redactionprocessor`: config → factory cho traces/logs/metrics → `processAttrs` và xử lý log body; đọc metadata/CI |
| Cơ chế | Allowlist loại key không được phép trước value masking; `ignored_keys`/`ignored_key_patterns` được giữ và bỏ qua xử lý; `allowed_values` có ưu tiên cho phép so với mask. Factory gắn các hàm xử lý vào pipeline khi processor được cấu hình. |
| Độ ổn định component | `metadata.yaml`: traces beta, logs/metrics alpha ở SHA đã đọc; mức ổn định của Collector nói chung không áp tự động cho mọi processor. |
| Giá trị cho xưởng | Tập trung egress policy, giữ cùng schema/allowlist ở nhiều dịch vụ, có thể thử canary PII và contract fixtures trước khi đổi config. |
| Rủi ro / dữ liệu rời máy | Exporter quyết định đích; telemetry vẫn có thể chứa nội dung nghiệp vụ. Bật `allow_all_keys`, thêm ignore quá rộng hoặc policy không bao phủ kiểu dữ liệu làm thay đổi bảo vệ. Regex không phải bằng chứng đã ẩn danh mọi PII. |
| Tích hợp | Pin distribution/version và config; kiểm component có trong binary; đặt redaction trước exporter và thử cả resource/scope/span/log body/metric attributes. `summary: debug` có thể lộ tên key; quyết định rõ summary/retention, không bật vì nghĩ chỉ là diagnostic vô hại. |
| Giới hạn | Chưa audit tất cả receiver/exporter, bảo vệ mạng/auth hay mọi loại payload. Không suy default allowlist của một processor bảo vệ pipeline chưa cài nó. |

**Bằng chứng:** [LICENSE](https://github.com/open-telemetry/opentelemetry-collector-contrib/blob/970f597792f2e60786e480dad4598b1078ba5627/LICENSE) · [processor/redactionprocessor/README.md](https://github.com/open-telemetry/opentelemetry-collector-contrib/blob/970f597792f2e60786e480dad4598b1078ba5627/processor/redactionprocessor/README.md) · [processor/redactionprocessor/config.go](https://github.com/open-telemetry/opentelemetry-collector-contrib/blob/970f597792f2e60786e480dad4598b1078ba5627/processor/redactionprocessor/config.go) · [processor/redactionprocessor/processor.go](https://github.com/open-telemetry/opentelemetry-collector-contrib/blob/970f597792f2e60786e480dad4598b1078ba5627/processor/redactionprocessor/processor.go) · [processor/redactionprocessor/factory.go](https://github.com/open-telemetry/opentelemetry-collector-contrib/blob/970f597792f2e60786e480dad4598b1078ba5627/processor/redactionprocessor/factory.go) · [processor/redactionprocessor/metadata.yaml](https://github.com/open-telemetry/opentelemetry-collector-contrib/blob/970f597792f2e60786e480dad4598b1078ba5627/processor/redactionprocessor/metadata.yaml) · [.github/workflows/build-and-test.yml](https://github.com/open-telemetry/opentelemetry-collector-contrib/blob/970f597792f2e60786e480dad4598b1078ba5627/.github/workflows/build-and-test.yml).

<a id="sloth-slo-generator"></a>

### 3.2 Sloth: SLO là source, Prometheus rule là artifact sinh ra

| Thuộc tính | Giá trị |
|---|---|
| Repo / tác giả | [slok/sloth](https://github.com/slok/sloth), cộng đồng Sloth; không suy bảo đảm hỗ trợ thương mại |
| Phiên bản / license | `dfab41f326c042e75f9cf7262ef66d19a755cb54` · Apache-2.0 · đọc 2026-11-04 |
| Cơ chế | CLI `generate` đi vào generator, sinh recording rules/metadata và multiwindow multi-burn alerts. `validate` gọi generator, kiểm spec và SLO trùng ID; trả lỗi khi validation fail. Không chỉ parse YAML. |
| Default cần biết | CLI dùng SLO period mặc định `30d`; có flag tắt recording/alert/default plugins và thêm plugin. Config được chọn mới là hợp đồng thật, không suy mọi mode có cùng cổng. |
| Giá trị cho xưởng | Review mục tiêu/SLI như code, tạo artifact nhất quán giữa service, giảm copy-paste PromQL và drift giữa dashboard/alert. |
| CI đã đọc | Unit/check, CLI integration và Kubernetes integration; workflow không được tự chạy ở kho này. |
| Rủi ro | Generator hợp lệ vẫn có thể dùng sai denominator hoặc loại bỏ nhóm lỗi; plugin mở rộng có quyền thực thi/biến đổi trong môi trường CI và phải được review/pin. Các objective 99.x chỉ là ví dụ, không phải SLA mẫu. |
| Tích hợp | Lưu source SLO và phiên bản generator/plugins; validate → generate → kiểm rules bằng Prometheus tooling/fixtures → diff artifact → rollout → kiểm alert routing/ack. Negative fixture phải làm cổng đỏ. |
| Thay thế | Pyrra nếu cần operator/UI; rule viết tay khi ít service; dịch vụ SLO managed khi chấp nhận data flow/cost và khóa nền tảng. |

**Bằng chứng:** [LICENSE](https://github.com/slok/sloth/blob/dfab41f326c042e75f9cf7262ef66d19a755cb54/LICENSE) · [README.md](https://github.com/slok/sloth/blob/dfab41f326c042e75f9cf7262ef66d19a755cb54/README.md) · [cmd/sloth/commands/generate.go](https://github.com/slok/sloth/blob/dfab41f326c042e75f9cf7262ef66d19a755cb54/cmd/sloth/commands/generate.go) · [cmd/sloth/commands/validate.go](https://github.com/slok/sloth/blob/dfab41f326c042e75f9cf7262ef66d19a755cb54/cmd/sloth/commands/validate.go) · [internal/app/generate/generate.go](https://github.com/slok/sloth/blob/dfab41f326c042e75f9cf7262ef66d19a755cb54/internal/app/generate/generate.go) · [internal/plugin/slo/core/alert_rules_v1/plugin.go](https://github.com/slok/sloth/blob/dfab41f326c042e75f9cf7262ef66d19a755cb54/internal/plugin/slo/core/alert_rules_v1/plugin.go) · [.github/workflows/ci.yaml](https://github.com/slok/sloth/blob/dfab41f326c042e75f9cf7262ef66d19a755cb54/.github/workflows/ci.yaml).

<a id="pyrra-slo-operations"></a>

### 3.3 Pyrra: SLO có UI và vòng reconcile, vẫn phải kiểm đích thật

| Thuộc tính | Giá trị |
|---|---|
| Repo / tổ chức | [pyrra-dev/pyrra](https://github.com/pyrra-dev/pyrra), cộng đồng Pyrra |
| Phiên bản / license | `a71aef6f7dd9e2774662211a805af5ab54445216` · Apache-2.0 · đọc 2026-11-04 |
| Cơ chế | `slo/rules.go` tạo burn-rate recording/alert rules từ Objective. Kubernetes reconciler tạo/cập nhật `PrometheusRule`, hoặc ConfigMap/Mimir theo mode; README còn có filesystem backend cho ngoài Kubernetes. |
| Giá trị | UI xem objective, error budget và burn rate; đưa SLO cho người vận hành/sản phẩm thay vì chỉ giữ PromQL trong repo. |
| Giới hạn đường gọi | Có lựa chọn tắt alerting/burnrates; controller cập nhật resource không chứng minh Prometheus đã discover/evaluate rule hay notification đến on-call. |
| CI | Workflow Go dùng version từ `go.mod`, gọi `make test`/`make pyrra`; không lấy biến môi trường cũ trong workflow làm version runtime thật. Chưa chạy test hoặc UI. |
| Dữ liệu / quyền | Query Prometheus/backend, cấp quyền reconcile tài nguyên; grouping tạo thêm series. Không thu user ID/raw URL làm label chỉ để drill-down dễ hơn. |
| Tích hợp | Service owner định nghĩa indicator/target/window; kiểm grouping/label routing, RBAC tối thiểu và namespace; sau reconcile kiểm rule được evaluate và alert tới kênh thử, có ack và auto-resolve. |
| Thay thế | Sloth cho compile rules; Prometheus + Grafana/alert rules trực tiếp nếu quy mô nhỏ; managed SLO khi chấp nhận provider. Không cần chạy hai generator cho cùng SLO. |

**Bằng chứng:** [LICENSE](https://github.com/pyrra-dev/pyrra/blob/a71aef6f7dd9e2774662211a805af5ab54445216/LICENSE) · [README.md](https://github.com/pyrra-dev/pyrra/blob/a71aef6f7dd9e2774662211a805af5ab54445216/README.md) · [slo/rules.go](https://github.com/pyrra-dev/pyrra/blob/a71aef6f7dd9e2774662211a805af5ab54445216/slo/rules.go) · [kubernetes/controllers/servicelevelobjective.go](https://github.com/pyrra-dev/pyrra/blob/a71aef6f7dd9e2774662211a805af5ab54445216/kubernetes/controllers/servicelevelobjective.go) · [.github/workflows/go.yaml](https://github.com/pyrra-dev/pyrra/blob/a71aef6f7dd9e2774662211a805af5ab54445216/.github/workflows/go.yaml).

## 4. Đường vận hành có thể kiểm lại

1. **Trước release:** chốt SLI/SLO theo hành trình người dùng, owner, dependency map, RPO/RTO và action khi error budget cạn. Đo đúng/thời gian/chi phí tách nhau; model response quality ở mục 07 bổ sung cho service SLO.
2. **Trước export:** fixture chứa canary secret, PII dạng string/số/nested, label cardinality và payload quá lớn. Kiểm ở **đích nhận thử** sau toàn bộ pipeline; chỉ unit test regex không phủ mapping/exporter. Lưu input/output/config hash và mẫu đã che.
3. **Trước đổi alert:** compiler + PromQL/rule fixtures có healthy, fast burn, slow burn, thiếu traffic và thiếu series. Quy định khi data thiếu là unknown hay incident; không tự coi mẫu rỗng là 100% thành công. Lưu số fixture, kỳ vọng và số alert phát sinh.
4. **Trong rollout:** đối chiếu canary/control bằng các metric đã chọn; log lý do tiếp tục/dừng. Rollback binary không tự đảo schema/data migration hoặc side effect đã commit; nối [mục 32](../32-platform-delivery-engineering/README.md) và [21](../21-autonomous-workflows/README.md).
5. **Khi incident:** alert phải có owner, runbook, customer impact, deploy/dataset/model revision; diễn tập nhận thông báo/ack/escalation và khôi phục dịch vụ. Viết timeline, điều gì chưa biết, action có người chịu trách nhiệm; không dùng số MTTR nhỏ để che sự cố bỏ sót.
6. **Sau restore:** khôi phục ở môi trường tách biệt với production, có khoá/quyền/dependency cần thiết; kiểm record nghiệp vụ, referential integrity, queue/outbox và tenant isolation. Ghi RPO/RTO **đo được**, backup ID và thời điểm cắt dữ liệu; không suy từ lịch backup hoặc pod Running.

Chaos/fault injection bắt đầu từ một giả thuyết và phạm vi nhỏ: worker chết, provider timeout, telemetry exporter nghẽn hay storage mất quyền. Có abort condition, owner và đường khôi phục; thử ở môi trường phù hợp rủi ro. Đợt nghiên cứu này chưa chạy chaos, kiểm alert routing, tải telemetry hay restore drill nên không gọi bất cứ stack nào “production-ready”.

## 5. Nguồn và giới hạn khảo sát

Nguồn ghim SHA trong §3 là source/LICENSE/CI chính thức đã đọc; so sánh Restic/Velero dẫn hồ sơ có bằng chứng ở mục 09, không tạo thực thể trùng. Không dùng sao làm điểm chất lượng. API GitHub trực tiếp bị proxy từ chối ở lượt đọc này, nên không bổ sung số sao hay kết luận archived/bảo trì từ việc clone thành công. Benchmark, hiệu quả alert và khả năng chịu tải ngoài phạm vi chưa được xác minh.

<a id="anhkysuai-2026-11-23"></a>

## Đánh giá từ kho Anh Kỹ Sư AI — 23/11/2026

Phần này có **10 hồ sơ hoặc phạm vi đối chiếu** từ [nguồn tuyển chọn](https://anhkysuai.com/kho/). [Bảng đủ 1.295 repo](../data/collections/anhkysuai-kho.json) ghi trạng thái đối chiếu từng link; [danh sách URL](../data/collections/anhkysuai-kho-links.txt) phục vụ tra cứu. Nguồn tuyển chọn giúp phát hiện repo; đánh giá bên dưới dựa trên clone và permalink upstream cùng metadata GitHub ngày 2026-11-23.

Mức `docs-read`/`code-read` chỉ áp dụng phạm vi ghi tại mỗi hồ sơ. Chưa cài, build, chạy test hay benchmark mã upstream. Giấy phép có thể tách theo code, model, nội dung, asset hoặc bản enterprise; con số/tuyên bố của tác giả chưa được tái lập nếu không có ghi chú khác.

<a id="anhkysuai-getsentry-sentry"></a>

### Sentry

**Repo:** [getsentry/sentry](https://github.com/getsentry/sentry) · **License:** FSL-1.1-Apache-2.0 · **Kiểm:** 2026-11-23, `docs-read`, [`17d485c4264e`](https://github.com/getsentry/sentry/tree/17d485c4264efceab71313e4176022a525e1da59) (commit 2026-11-23). **Sao:** 45,868 tại 2026-11-23 theo [GitHub API](https://api.github.com/repos/getsentry/sentry).

| Mục | Đánh giá |
|---|---|
| Mục đích | Nền tảng thu thập lỗi và ngữ cảnh debug của ứng dụng. |
| Giá trị và cơ chế theo tài liệu | README gắn SDK với việc phát hiện, truy vết và sửa vấn đề; monorepo Python/TypeScript và workflow lint cho thấy nhiều thành phần vận hành. |
| Giới hạn | LICENSE hiện tại là FSL, không phải Apache-2.0 hiện hành cho mọi mã. Khả năng giảm thời gian xử lý lỗi và chi phí self-host chưa đo; dữ liệu sự kiện có thể chứa thông tin nhạy cảm. |
| Điều kiện tích hợp | Kiểm giới hạn sử dụng FSL, bắt đầu một dịch vụ với sampling và lọc dữ liệu; đánh giá lưu trữ, cảnh báo, retention trước khi mở rộng. |
| Lựa chọn đối chiếu | GlitchTip; OpenTelemetry + Grafana; Bugsink. |

**Phạm vi bằng chứng:** đã clone, đọc trích đoạn tài liệu, giấy phép và các file cấu hình được dẫn dưới đây; chưa chạy mã, build, benchmark hoặc test upstream. `docs-read` không phải kiểm chứng implementation.

**Nguồn tại cùng SHA:** [README.md](https://github.com/getsentry/sentry/blob/17d485c4264efceab71313e4176022a525e1da59/README.md) · [LICENSE.md](https://github.com/getsentry/sentry/blob/17d485c4264efceab71313e4176022a525e1da59/LICENSE.md) · [package.json](https://github.com/getsentry/sentry/blob/17d485c4264efceab71313e4176022a525e1da59/package.json) · [pyproject.toml](https://github.com/getsentry/sentry/blob/17d485c4264efceab71313e4176022a525e1da59/pyproject.toml) · [.github/workflows/decision-model-lint.yml](https://github.com/getsentry/sentry/blob/17d485c4264efceab71313e4176022a525e1da59/.github/workflows/decision-model-lint.yml).

<a id="anhkysuai-glanceapp-glance"></a>

### Glance

**Repo:** [glanceapp/glance](https://github.com/glanceapp/glance) · **License:** AGPL-3.0 · **Kiểm:** 2026-11-23, `docs-read`, [`53aec7f392ca`](https://github.com/glanceapp/glance/tree/53aec7f392ca72143870dcb45526ec7c80a68f32) (commit 2026-11-07). **Sao:** 38,351 tại 2026-11-23 theo [GitHub API](https://api.github.com/repos/glanceapp/glance).

| Mục | Đánh giá |
|---|---|
| Mục đích | Dashboard tự host gom feed, lịch, thời tiết, thông tin máy chủ và widget tùy chỉnh. |
| Giá trị và cơ chế theo tài liệu | README cung cấp cấu hình YAML theo trang/cột/widget; Go binary và workflow GoReleaser là cách đóng gói dễ kiểm soát cho dashboard cá nhân. |
| Giới hạn | Các con số kích thước, thời gian tải và bộ nhớ trong README chưa được tái lập. Widget phụ thuộc API bên ngoài; nội dung màn hình có thể lộ thông tin nội bộ. |
| Điều kiện tích hợp | Bắt đầu ít widget, ghim cấu hình và hạn chế truy cập bảng điều khiển; kiểm cache, lỗi upstream và quyền của nguồn dữ liệu. |
| Lựa chọn đối chiếu | [Homepage](../33-reliability-observability-operations/README.md#anhkysuai-gethomepage-homepage); [Dashy](../08-awesome-lists-learning/README.md#6c526-tự-host--nhà-thông-minh); Heimdall. |

**Phạm vi bằng chứng:** đã clone, đọc trích đoạn tài liệu, giấy phép và các file cấu hình được dẫn dưới đây; chưa chạy mã, build, benchmark hoặc test upstream. `docs-read` không phải kiểm chứng implementation.

**Nguồn tại cùng SHA:** [README.md](https://github.com/glanceapp/glance/blob/53aec7f392ca72143870dcb45526ec7c80a68f32/README.md) · [LICENSE](https://github.com/glanceapp/glance/blob/53aec7f392ca72143870dcb45526ec7c80a68f32/LICENSE) · [go.mod](https://github.com/glanceapp/glance/blob/53aec7f392ca72143870dcb45526ec7c80a68f32/go.mod) · [.github/workflows/release.yaml](https://github.com/glanceapp/glance/blob/53aec7f392ca72143870dcb45526ec7c80a68f32/.github/workflows/release.yaml).

<a id="anhkysuai-alibaba-arthas"></a>

### Arthas

**Repo:** [alibaba/arthas](https://github.com/alibaba/arthas) · **License:** Apache-2.0 · **Kiểm:** 2026-11-23, `docs-read`, [`1712334ef34f`](https://github.com/alibaba/arthas/tree/1712334ef34f70c3dc72f3241818c3729770639b) (commit 2026-11-23). **Sao:** 37,630 tại 2026-11-23 theo [GitHub API](https://api.github.com/repos/alibaba/arthas).

| Mục | Đánh giá |
|---|---|
| Mục đích | Công cụ chẩn đoán Java đang chạy để tìm vấn đề mà không cần sửa mã ứng dụng. |
| Giá trị và cơ chế theo tài liệu | README giải thích tình huống lỗi khó tái hiện; CI Maven có các bước verify trên nhiều môi trường, hỗ trợ dùng như công cụ điều tra JVM. |
| Giới hạn | Khẳng định không dừng JVM không bảo đảm mọi lệnh không gây overhead. Quyền attach và quan sát có thể tiếp cận dữ liệu nhạy cảm; chưa gắn vào tiến trình thực. |
| Điều kiện tích hợp | Thử trước trên JVM staging, giới hạn người dùng và thời gian phiên chẩn đoán; chọn lệnh có phạm vi nhỏ và theo dõi tác động tài nguyên. |
| Lựa chọn đối chiếu | Java Flight Recorder; async-profiler; VisualVM. |

**Phạm vi bằng chứng:** đã clone, đọc trích đoạn tài liệu, giấy phép và các file cấu hình được dẫn dưới đây; chưa chạy mã, build, benchmark hoặc test upstream. `docs-read` không phải kiểm chứng implementation.

**Nguồn tại cùng SHA:** [README.md](https://github.com/alibaba/arthas/blob/1712334ef34f70c3dc72f3241818c3729770639b/README.md) · [LICENSE](https://github.com/alibaba/arthas/blob/1712334ef34f70c3dc72f3241818c3729770639b/LICENSE) · [pom.xml](https://github.com/alibaba/arthas/blob/1712334ef34f70c3dc72f3241818c3729770639b/pom.xml) · [.github/workflows/test.yaml](https://github.com/alibaba/arthas/blob/1712334ef34f70c3dc72f3241818c3729770639b/.github/workflows/test.yaml).

<a id="anhkysuai-derailed-k9s"></a>

### K9s

**Repo:** [derailed/k9s](https://github.com/derailed/k9s) · **License:** Apache-2.0 · **Kiểm:** 2026-11-23, `docs-read`, [`c732946a6da3`](https://github.com/derailed/k9s/tree/c732946a6da348ad1b4fdabd6b9bd0f8cd2d3804) (commit 2026-11-21). **Sao:** 35,035 tại 2026-11-23 theo [GitHub API](https://api.github.com/repos/derailed/k9s).

| Mục | Đánh giá |
|---|---|
| Mục đích | Giao diện terminal để quan sát và thao tác tài nguyên Kubernetes. |
| Giá trị và cơ chế theo tài liệu | README mô tả theo dõi thay đổi liên tục, điều hướng pods/logs/deployments; Go manifest và workflow make test cung cấp cơ sở đọc công cụ vận hành. |
| Giới hạn | UI nhanh cũng làm thao tác nhầm context nguy hiểm hơn. Quyền thực tế phụ thuộc kubeconfig/RBAC; chưa kết nối cluster hay kiểm các plugin/lệnh mở rộng. |
| Điều kiện tích hợp | Dùng tài khoản chỉ đọc khi quan sát, hiển thị rõ context/namespace và thử trên cluster dev; kiểm plugin trước khi cho phép chạy lệnh có quyền cao. |
| Lựa chọn đối chiếu | kubectl; Headlamp; Lens. |

**Phạm vi bằng chứng:** đã clone, đọc trích đoạn tài liệu, giấy phép và các file cấu hình được dẫn dưới đây; chưa chạy mã, build, benchmark hoặc test upstream. `docs-read` không phải kiểm chứng implementation.

**Nguồn tại cùng SHA:** [README.md](https://github.com/derailed/k9s/blob/c732946a6da348ad1b4fdabd6b9bd0f8cd2d3804/README.md) · [COPYING](https://github.com/derailed/k9s/blob/c732946a6da348ad1b4fdabd6b9bd0f8cd2d3804/COPYING) · [LICENSE](https://github.com/derailed/k9s/blob/c732946a6da348ad1b4fdabd6b9bd0f8cd2d3804/LICENSE) · [go.mod](https://github.com/derailed/k9s/blob/c732946a6da348ad1b4fdabd6b9bd0f8cd2d3804/go.mod) · [.github/workflows/test.yml](https://github.com/derailed/k9s/blob/c732946a6da348ad1b4fdabd6b9bd0f8cd2d3804/.github/workflows/test.yml).

<a id="anhkysuai-nicolargo-glances"></a>

### Glances

**Repo:** [nicolargo/glances](https://github.com/nicolargo/glances) · **License:** LGPL-3.0 · **Kiểm:** 2026-11-23, `docs-read`, [`f94244c60881`](https://github.com/nicolargo/glances/tree/f94244c6088133f18c4dc0e445b44cda840a4500) (commit 2026-11-23). **Sao:** 34,005 tại 2026-11-23 theo [GitHub API](https://api.github.com/repos/nicolargo/glances).

| Mục | Đánh giá |
|---|---|
| Mục đích | Công cụ Python quan sát hệ thống bằng terminal, WebUI và REST API. |
| Giá trị và cơ chế theo tài liệu | README mô tả kiến trúc plugin/export và API v5; CI tách quality, test, web UI, build và kiểm bảo mật thành workflow riêng. |
| Giới hạn | README nói API không có mật khẩu mặc định dù bind localhost; mở toàn interface cần thêm kiểm soát. Client/server v5 phải cùng dòng; chưa đo overhead hay kiểm sensor mọi hệ điều hành. |
| Điều kiện tích hợp | Bắt đầu local, chọn plugin cần thiết và đặt xác thực trước khi truy cập từ xa; hạn chế lộ chỉ số tiến trình và kiểm exporter/retention. |
| Lựa chọn đối chiếu | [Beszel](../33-reliability-observability-operations/README.md#anhkysuai-henrygd-beszel); [Netdata](../08-awesome-lists-learning/README.md#6c511-giám-sát-csdl--phân-tích); btop. |

**Phạm vi bằng chứng:** đã clone, đọc trích đoạn tài liệu, giấy phép và các file cấu hình được dẫn dưới đây; chưa chạy mã, build, benchmark hoặc test upstream. `docs-read` không phải kiểm chứng implementation.

**Nguồn tại cùng SHA:** [README.rst](https://github.com/nicolargo/glances/blob/f94244c6088133f18c4dc0e445b44cda840a4500/README.rst) · [COPYING](https://github.com/nicolargo/glances/blob/f94244c6088133f18c4dc0e445b44cda840a4500/COPYING) · [pyproject.toml](https://github.com/nicolargo/glances/blob/f94244c6088133f18c4dc0e445b44cda840a4500/pyproject.toml) · [.github/workflows/ci.yml](https://github.com/nicolargo/glances/blob/f94244c6088133f18c4dc0e445b44cda840a4500/.github/workflows/ci.yml).

<a id="anhkysuai-gethomepage-homepage"></a>

### Homepage

**Repo:** [gethomepage/homepage](https://github.com/gethomepage/homepage) · **License:** GPL-3.0 · **Kiểm:** 2026-11-23, `docs-read`, [`a1e3a5fd26d6`](https://github.com/gethomepage/homepage/tree/a1e3a5fd26d6f55aaccdf1be000913eddba666fc) (commit 2026-11-19). **Sao:** 33,788 tại 2026-11-23 theo [GitHub API](https://api.github.com/repos/gethomepage/homepage).

| Mục | Đánh giá |
|---|---|
| Mục đích | Dashboard ứng dụng tự host với bookmarks, widget và phát hiện dịch vụ từ Docker label. |
| Giá trị và cơ chế theo tài liệu | README mô tả backend proxy API để giữ khóa khỏi frontend; manifest Next.js và CI Vitest shard cho thấy cách tổ chức giao diện và kiểm. |
| Giới hạn | Proxy không tự chứng minh an toàn cho mọi endpoint hay quyền Docker socket. Các tích hợp phụ thuộc API riêng; chưa kiểm truy cập trái phép hoặc chất lượng widget. |
| Điều kiện tích hợp | Chỉ kết nối dịch vụ cần thiết, kiểm quyền socket/API và giới hạn truy cập dashboard; lưu cấu hình YAML có kiểm soát và tránh public dữ liệu vận hành. |
| Lựa chọn đối chiếu | [Glance](../33-reliability-observability-operations/README.md#anhkysuai-glanceapp-glance); [Dashy](../08-awesome-lists-learning/README.md#6c526-tự-host--nhà-thông-minh); Heimdall. |

**Phạm vi bằng chứng:** đã clone, đọc trích đoạn tài liệu, giấy phép và các file cấu hình được dẫn dưới đây; chưa chạy mã, build, benchmark hoặc test upstream. `docs-read` không phải kiểm chứng implementation.

**Nguồn tại cùng SHA:** [README.md](https://github.com/gethomepage/homepage/blob/a1e3a5fd26d6f55aaccdf1be000913eddba666fc/README.md) · [LICENSE](https://github.com/gethomepage/homepage/blob/a1e3a5fd26d6f55aaccdf1be000913eddba666fc/LICENSE) · [package.json](https://github.com/gethomepage/homepage/blob/a1e3a5fd26d6f55aaccdf1be000913eddba666fc/package.json) · [pyproject.toml](https://github.com/gethomepage/homepage/blob/a1e3a5fd26d6f55aaccdf1be000913eddba666fc/pyproject.toml) · [.github/workflows/test.yml](https://github.com/gethomepage/homepage/blob/a1e3a5fd26d6f55aaccdf1be000913eddba666fc/.github/workflows/test.yml).

<a id="anhkysuai-locustio-locust"></a>

### Locust

**Đã chuyển (2026-11-23):** hồ sơ này nay nằm ở [mục 30](../30-software-testing-quality/README.md#anhkysuai-locustio-locust); catalog con xem [catalog/](../catalog/README.md).

<a id="anhkysuai-henrygd-beszel"></a>

### Beszel

**Repo:** [henrygd/beszel](https://github.com/henrygd/beszel) · **License:** MIT · **Kiểm:** 2026-11-23, `docs-read`, [`6702f013f8ce`](https://github.com/henrygd/beszel/tree/6702f013f8ceed0c48d95c1988a58b6d970b5022) (commit 2026-11-20). **Sao:** 27,564 tại 2026-11-23 theo [GitHub API](https://api.github.com/repos/henrygd/beszel).

| Mục | Đánh giá |
|---|---|
| Mục đích | Hệ thống giám sát máy chủ với lịch sử, Docker stats và cảnh báo. |
| Giá trị và cơ chế theo tài liệu | README phân tách hub dựa PocketBase với agent, mô tả OAuth/OIDC, nhiều người dùng và backup; workflow govulncheck bổ sung cổng kiểm dependency. |
| Giới hạn | Nhẹ và dễ cài là mục tiêu upstream, chưa đo overhead. Quyền agent, socket Docker và chia sẻ hệ thống cần kiểm; có scan không thay kiểm an toàn toàn triển khai. |
| Điều kiện tích hợp | Gắn thử một agent, giới hạn truy cập hub và bật xác thực; kiểm alert, retention và restore backup trước khi dùng theo dõi đội máy chủ. |
| Lựa chọn đối chiếu | [Glances](../33-reliability-observability-operations/README.md#anhkysuai-nicolargo-glances); [Netdata](../08-awesome-lists-learning/README.md#6c511-giám-sát-csdl--phân-tích); Prometheus + Grafana. |

**Phạm vi bằng chứng:** đã clone, đọc trích đoạn tài liệu, giấy phép và các file cấu hình được dẫn dưới đây; chưa chạy mã, build, benchmark hoặc test upstream. `docs-read` không phải kiểm chứng implementation.

**Nguồn tại cùng SHA:** [readme.md](https://github.com/henrygd/beszel/blob/6702f013f8ceed0c48d95c1988a58b6d970b5022/readme.md) · [LICENSE](https://github.com/henrygd/beszel/blob/6702f013f8ceed0c48d95c1988a58b6d970b5022/LICENSE) · [go.mod](https://github.com/henrygd/beszel/blob/6702f013f8ceed0c48d95c1988a58b6d970b5022/go.mod) · [.github/workflows/vulncheck.yml](https://github.com/henrygd/beszel/blob/6702f013f8ceed0c48d95c1988a58b6d970b5022/.github/workflows/vulncheck.yml).

<a id="anhkysuai-alibaba-sentinel"></a>

### Sentinel

**Repo:** [alibaba/Sentinel](https://github.com/alibaba/Sentinel) · **License:** Apache-2.0 · **Kiểm:** 2026-11-23, `docs-read`, [`a3f40ba8e900`](https://github.com/alibaba/Sentinel/tree/a3f40ba8e900c8489bd520274739f17235a7721c) (commit 2026-05-27). **Sao:** 23,141 tại 2026-11-23 theo [GitHub API](https://api.github.com/repos/alibaba/Sentinel).

| Mục | Đánh giá |
|---|---|
| Mục đích | Component kiểm soát lưu lượng, giới hạn đồng thời, circuit breaking và bảo vệ quá tải. |
| Giá trị và cơ chế theo tài liệu | README mô tả adapter Spring Cloud/gRPC/Dubbo/Quarkus; Maven CI kiểm cả có/không Spring 6, hỗ trợ đọc lớp resilience của dịch vụ Java. |
| Giới hạn | Kinh nghiệm upstream ở hệ lớn không chứng minh ngưỡng phù hợp ứng dụng mới. Rule sai có thể từ chối người dùng hợp lệ; chưa thử overload, fail-open/fail-closed hay cluster rule. |
| Điều kiện tích hợp | Bắt đầu bằng quan sát và rule bảo thủ, thử burst/timeout/cascade failure; quản lý quyền đổi rule, rollback và version adapter theo runtime. |
| Lựa chọn đối chiếu | Resilience4j; Envoy; Bucket4j. |

**Phạm vi bằng chứng:** đã clone, đọc trích đoạn tài liệu, giấy phép và các file cấu hình được dẫn dưới đây; chưa chạy mã, build, benchmark hoặc test upstream. `docs-read` không phải kiểm chứng implementation.

**Nguồn tại cùng SHA:** [README.md](https://github.com/alibaba/Sentinel/blob/a3f40ba8e900c8489bd520274739f17235a7721c/README.md) · [LICENSE](https://github.com/alibaba/Sentinel/blob/a3f40ba8e900c8489bd520274739f17235a7721c/LICENSE) · [pom.xml](https://github.com/alibaba/Sentinel/blob/a3f40ba8e900c8489bd520274739f17235a7721c/pom.xml) · [.github/workflows/ci.yml](https://github.com/alibaba/Sentinel/blob/a3f40ba8e900c8489bd520274739f17235a7721c/.github/workflows/ci.yml).

<a id="anhkysuai-allinurl-goaccess"></a>

### GoAccess

**Repo:** [allinurl/goaccess](https://github.com/allinurl/goaccess) · **License:** MIT · **Kiểm:** 2026-11-23, `docs-read`, [`33995aa31c8d`](https://github.com/allinurl/goaccess/tree/33995aa31c8d3cbd9490309fa363dcc4239ee9a8) (commit 2026-11-20). **Sao:** 21,150 tại 2026-11-23 theo [GitHub API](https://api.github.com/repos/allinurl/goaccess).

| Mục | Đánh giá |
|---|---|
| Mục đích | Công cụ phân tích access log web, hiển thị terminal hoặc dashboard HTML thời gian thực. |
| Giá trị và cơ chế theo tài liệu | README mô tả chọn log format, response time và xác thực WebSocket/JWT; CI C build/test trên nhiều cấu hình hỗ trợ đọc chuỗi đóng gói. |
| Giới hạn | Chỉ thấy những gì có trong log, không thay tracing hay analytics client. Các mốc cập nhật thời gian thực chưa đo; log có thể chứa IP, URL/token nhạy cảm. |
| Điều kiện tích hợp | Dùng log mẫu đúng format/timezone, kiểm proxy IP và bộ lọc; bảo vệ HTML/WebSocket, đặt retention và che trường nhạy cảm trước khi chia sẻ báo cáo. |
| Lựa chọn đối chiếu | Grafana Loki; Matomo; AWStats. |

**Phạm vi bằng chứng:** đã clone, đọc trích đoạn tài liệu, giấy phép và các file cấu hình được dẫn dưới đây; chưa chạy mã, build, benchmark hoặc test upstream. `docs-read` không phải kiểm chứng implementation.

**Nguồn tại cùng SHA:** [README.md](https://github.com/allinurl/goaccess/blob/33995aa31c8d3cbd9490309fa363dcc4239ee9a8/README.md) · [COPYING](https://github.com/allinurl/goaccess/blob/33995aa31c8d3cbd9490309fa363dcc4239ee9a8/COPYING) · [.github/workflows/build-test.yml](https://github.com/allinurl/goaccess/blob/33995aa31c8d3cbd9490309fa363dcc4239ee9a8/.github/workflows/build-test.yml).

<a id="chuyen-muc-2026-11-23"></a>

## Hồ sơ chuyển về từ mục khác — 23/11/2026

10 hồ sơ được chuyển khi chia lại catalog theo `data/taxonomy.json`. Nội dung, ngày kiểm và mức bằng chứng giữ nguyên như ở mục gốc.

<a id="chuyen-netdata"></a>

### netdata

`netdata/netdata` · License: GPL-3.0 · ★ 81.458 · docs-read · 2026-11-18

Nền tảng quan sát full-stack thu thập metric theo từng giây, log, trace, luồng mạng, có cảnh báo và học máy, chạy trên Linux, macOS, FreeBSD, Windows, Kubernetes. Hơn 800 tích hợp gồm OpenTelemetry, SNMP, NetFlow/IPFIX/sFlow, IPMI; Agent có máy chủ MCP tích hợp; mở rộng từ một nút tới hàng trăm nghìn nút qua kiến trúc Parent. Điều kiện: Telemetry ẩn danh bật mặc định (tắt bằng --disable-telemetry hoặc file opt-out); giao diện UI mã đóng giấy phép NCUL1; tính năng Cloud (SSO, RBAC, truy cập từ xa) cần tài khoản Netdata Cloud. ★ 18/11/2026: 81.458 (GitHub search API), nhóm "Giám sát, CSDL & Phân tích" trong kho-repo của Phan Đông Giang, mục 08 §6c.5

**Hồ sơ gốc:** [mục 08](../08-awesome-lists-learning/README.md#6c511-giám-sát-csdl--phân-tích) (bảng/đoạn chung, giữ nguyên tại chỗ).

<a id="chuyen-grafana"></a>

### grafana

`grafana/grafana` · License: AGPL-3.0-only · ★ 77.975 · docs-read · 2026-11-18

Nền tảng giám sát và quan sát mã nguồn mở để truy vấn, trực quan hoá, cảnh báo trên metric và log từ nhiều nguồn dữ liệu. Dashboard động với biến template, trộn nhiều nguồn dữ liệu trong một biểu đồ; cảnh báo gửi tới Slack, PagerDuty, OpsGenie; có bản demo trực tiếp tại play.grafana.org. Điều kiện: AGPL-3.0: cung cấp bản sửa đổi qua mạng phải công bố mã nguồn. ★ 18/11/2026: 77.975 (GitHub search API), nhóm "Giám sát, CSDL & Phân tích" trong kho-repo của Phan Đông Giang, mục 08 §6c.5

**Hồ sơ gốc:** [mục 08](../08-awesome-lists-learning/README.md#6c511-giám-sát-csdl--phân-tích) (bảng/đoạn chung, giữ nguyên tại chỗ).

<a id="chuyen-signoz"></a>

### signoz

`SigNoz/signoz` · License: MIT · ★ 32.673 · docs-read · 2026-11-18

Nền tảng observability mã nguồn mở dựa trên OpenTelemetry, gộp logs, metrics, traces, cảnh báo và dashboard một chỗ. Gộp APM, quản lý log, metrics, distributed tracing và cảnh báo trong một sản phẩm; truy vấn bằng Query Builder, PromQL hoặc ClickHouse SQL; tự host bằng Docker, Kubernetes hoặc Linux. Điều kiện: Mã trong ee/ cần giấy phép SigNoz Enterprise để dùng production; trợ lý Noz chỉ có trên SigNoz Cloud (README). ★ 18/11/2026: 32.673 (GitHub search API), nhóm "Giám sát, CSDL & Phân tích" trong kho-repo của Phan Đông Giang, mục 08 §6c.5

**Hồ sơ gốc:** [mục 08](../08-awesome-lists-learning/README.md#6c511-giám-sát-csdl--phân-tích) (bảng/đoạn chung, giữ nguyên tại chỗ).

<a id="chuyen-skywalking"></a>

### skywalking

`apache/skywalking` · License: Apache License 2.0 · ★ 25.010 · docs-read · 2026-11-18

Hệ thống APM cho microservice và kiến trúc cloud native: distributed tracing, giám sát và chẩn đoán hệ phân tán. Có agent cho Java, .Net Core, PHP, NodeJS, Golang, Lua, Rust, C++, Python và JavaScript phía client; agent Rover dùng eBPF để giám sát Kubernetes; nhận dữ liệu từ Zipkin, OpenTelemetry, Prometheus, Zabbix, Fluentd. ★ 18/11/2026: 25.010 (GitHub search API), nhóm "Giám sát, CSDL & Phân tích" trong kho-repo của Phan Đông Giang, mục 08 §6c.5

**Hồ sơ gốc:** [mục 08](../08-awesome-lists-learning/README.md#6c511-giám-sát-csdl--phân-tích) (bảng/đoạn chung, giữ nguyên tại chỗ).

<a id="chuyen-jaeger"></a>

### jaeger

`jaegertracing/jaeger` · License: Apache License 2.0 · ★ 23.422 · docs-read · 2026-11-18

Nền tảng distributed tracing do Uber tạo và tặng CNCF, nhận trace qua OTLP và có giao diện truy vấn. Dự án CNCF đã graduated (10/2019); Jaeger v2 dựa trên thành phần OpenTelemetry Collector; có chính sách bảo đảm tương thích cấu hình với thời gian ân hạn ít nhất 3 tháng. ★ 18/11/2026: 23.422 (GitHub search API), nhóm "Giám sát, CSDL & Phân tích" trong kho-repo của Phan Đông Giang, mục 08 §6c.5

**Hồ sơ gốc:** [mục 08](../08-awesome-lists-learning/README.md#6c511-giám-sát-csdl--phân-tích) (bảng/đoạn chung, giữ nguyên tại chỗ).

<a id="chuyen-openobserve"></a>

### openobserve

`openobserve/openobserve` · License: GNU Affero General Public License v3.0 · ★ 23.096 · docs-read · 2026-11-18

Nền tảng observability cloud native viết bằng Rust cho logs, metrics, traces, RUM và quan sát AI/LLM, định vị thay Datadog, Splunk, Elasticsearch. Triển khai một binary duy nhất; lưu trữ cột Parquet trên S3 (README nêu chi phí lưu trữ thấp hơn 140 lần so với Elasticsearch); truy vấn bằng SQL và PromQL, gốc OpenTelemetry. Điều kiện: AGPL-3.0 (copyleft cả khi cung cấp qua mạng); có Enterprise Edition riêng (điều khoản chưa xác minh). ★ 18/11/2026: 23.096 (GitHub search API), nhóm "Giám sát, CSDL & Phân tích" trong kho-repo của Phan Đông Giang, mục 08 §6c.5

**Hồ sơ gốc:** [mục 08](../08-awesome-lists-learning/README.md#6c511-giám-sát-csdl--phân-tích) (bảng/đoạn chung, giữ nguyên tại chỗ).

<a id="chuyen-vector"></a>

### vector

`vectordotdev/vector` · License: Mozilla Public License 2.0 · ★ 22.895 · docs-read · 2026-11-18

Pipeline dữ liệu observability hiệu năng cao viết bằng Rust, chạy như agent hoặc aggregator để thu, biến đổi và định tuyến logs và metrics. Viết bằng Rust với mục tiêu thiết kế chính là độ tin cậy; có ngôn ngữ biến đổi VRL và lệnh vector validate, vector test, vector top, vector tap; do nhóm Community Open Source Engineering của Datadog duy trì. ★ 18/11/2026: 22.895 (GitHub search API), nhóm "Giám sát, CSDL & Phân tích" trong kho-repo của Phan Đông Giang, mục 08 §6c.5

**Hồ sơ gốc:** [mục 08](../08-awesome-lists-learning/README.md#6c511-giám-sát-csdl--phân-tích) (bảng/đoạn chung, giữ nguyên tại chỗ).

<a id="chuyen-kibana"></a>

### kibana

`elastic/kibana` · License: Mặc định ba giấy phép AGPL-3.0-only · ★ 21.382 · docs-read · 2026-11-18

Giao diện để truy vấn, phân tích, trực quan hoá và quản lý dữ liệu lưu trong Elasticsearch. Là giao diện chính thức của Elastic Stack; README có bảng tương thích phiên bản Kibana–Elasticsearch rõ ràng; có bản tải sẵn và bản hosted trên Elastic Cloud. Điều kiện: Cần Elasticsearch cùng phiên bản major; mã x-pack chỉ theo Elastic License 2.0. ★ 18/11/2026: 21.382 (GitHub search API), nhóm "Giám sát, CSDL & Phân tích" trong kho-repo của Phan Đông Giang, mục 08 §6c.5

**Hồ sơ gốc:** [mục 08](../08-awesome-lists-learning/README.md#6c511-giám-sát-csdl--phân-tích) (bảng/đoạn chung, giữ nguyên tại chỗ).

<a id="chuyen-victoriametrics"></a>

### VictoriaMetrics

`VictoriaMetrics/VictoriaMetrics` · License: Apache-2.0 · ★ 18.126 · docs-read · 2026-11-18

Cơ sở dữ liệu chuỗi thời gian và giải pháp giám sát nhanh, tiết kiệm, mở rộng được; dùng làm lưu trữ dài hạn hoặc thay thế Prometheus/Graphite trong Grafana. Hỗ trợ PromQL và MetricsQL; nhận dữ liệu qua Prometheus remote write, InfluxDB line protocol, Graphite, OpenTSDB, DataDog, NewRelic, OpenTelemetry; có bản single-node và cluster cùng bộ công cụ vmagent, vmalert, vmauth, vmbackup. Điều kiện: Tính năng Enterprise và bản LTS cần giấy phép thương mại. ★ 18/11/2026: 18.126 (GitHub search API), nhóm "Giám sát, CSDL & Phân tích" trong kho-repo của Phan Đông Giang, mục 08 §6c.5

**Hồ sơ gốc:** [mục 08](../08-awesome-lists-learning/README.md#6c511-giám-sát-csdl--phân-tích) (bảng/đoạn chung, giữ nguyên tại chỗ).

<a id="chuyen-zipkin"></a>

### zipkin

`openzipkin/zipkin` · License: Apache-2.0 · ★ 17.475 · docs-read · 2026-11-18

Hệ thống truy vết phân tán, thu thập và tra cứu dữ liệu thời gian để gỡ lỗi độ trễ trong kiến trúc dịch vụ, kèm giao diện web và sơ đồ phụ thuộc. Nhận dữ liệu qua HTTP, Kafka, gRPC, RabbitMQ, ActiveMQ, Pulsar; lưu trong bộ nhớ, Cassandra hoặc Elasticsearch; có bản slim, ảnh Docker và công thức Homebrew. Điều kiện: Máy chủ cần JRE 17+; ứng dụng phải được gắn thư viện instrumentation. ★ 18/11/2026: 17.475 (GitHub search API), nhóm "Giám sát, CSDL & Phân tích" trong kho-repo của Phan Đông Giang, mục 08 §6c.5

**Hồ sơ gốc:** [mục 08](../08-awesome-lists-learning/README.md#6c511-giám-sát-csdl--phân-tích) (bảng/đoạn chung, giữ nguyên tại chỗ).

<a id="nt-2026-11-23"></a>

## Nâng trần theo khoảng trống — 23/11/2026

Phần này có các hồ sơ mới của đợt nâng trần: mười trinh sát tìm trên internet và GitHub những mảng mà chuyên mục còn thiếu hoặc chỉ có hồ sơ cũ, rồi mỗi repo được clone nông tại một commit cố định, đọc LICENSE, README, ít nhất một file triển khai thật và CI nếu có; không cài hay chạy mã upstream. Mô tả của trinh sát nhiều chỗ sai so với mã thật, và các chỗ đó được sửa ngay trong từng hồ sơ. Số sao lấy sau bằng GitHub search API nên có thể để trống.

<a id="nt-culiops-skills"></a>

### CuliOps skills

| Thuộc tính | Giá trị |
|---|---|
| Repo | https://github.com/culiops/culiops-skills |
| License | MIT |
| Phiên bản đã đọc | `40d9310d51a6b43d6d78bb0928193b705bd1910a` (commit 2026-11-20) |
| Kiểm chứng | 2026-11-23; code-read; đã đọc LICENSE, README.md, skills/sre-investigate/SKILL.md, .claude-plugin/plugin.json, CHANGELOG.md; chưa chạy upstream |
| Khoảng trống lấp | Skill vận hành SRE/incident/runbook: điều tra sự cố chỉ đọc có nhãn bằng chứng và sổ truy vấn |
| Cơ chế đáng học | - `skills/sre-investigate/SKILL.md` (400 dòng): Iron Law "quan sát, không tác động", mỗi nguyên nhân và mỗi mắt xích mang đúng một nhãn, nhãn không mạnh hơn mắt xích yếu nhất, "disprove first" (chạy truy vấn bác bỏ trước).<br>- Lệnh chạy theo đợt: in đầy đủ lệnh rồi chạy; AccessDenied/401/403 ghi thành khoảng trống kèm cách sửa, không đi vòng; thông tin thật chỉ trỏ bằng tên biến môi trường; mọi giờ theo UTC.<br>- Quy trình 7 pha, 0 đến 6 (truy cập và intake, phạm vi/tác động, tương quan thay đổi, giả thuyết, bằng chứng bằng worker riêng ở chế độ Deep, kết luận, ghi nhận); sổ `ledger.md` ghi ID truy vấn dạng `W<đợt>-Q<n>`.<br>- Văn bản trong log, ticket, PR là dữ liệu không tin cậy: không chạy lệnh hay mở URL nằm trong đó. |
| Tiêu chí và cách kiểm | Chỉ có fixture mô phỏng: `tests/fixtures/sre-investigate/*` (9 tình huống như injection-in-logs, k8s-crashloop-configmap), mỗi ca có world giả và `DRY-RUN-NOTES.md` chấm tay theo các dòng MUST/MUST-NOT. Fixture injection-in-logs ghi 5 đạt, 3 trượt cho lượt baseline không có skill (đã mở). Không có CI, không có script chạy tự động, không đo độ đúng RCA trên sự cố thật. |
| Giới hạn và rủi ro | MIT (LICENSE đã đọc). Cần AWS CLI, kubectl, helm, gh; skill khuyến nghị quyền chỉ đọc (ReadOnlyAccess, ClusterRole view) nhưng cảnh báo rồi vẫn chạy khi thấy credential có quyền ghi (Constraint 7), nên an toàn dựa vào cấu hình của người dùng. Truy vấn CloudWatch Logs Insights, X-Ray tính tiền theo lượng quét. Tích hợp "Culibox" chưa có (SKILL.md ghi chưa sẵn sàng). Bản 0.20.0, chỉ AWS và Kubernetes; GCP và Azure đã bị gỡ ở v0.11.0. Bản clone nông chỉ có một commit nên không đánh giá được lịch sử bảo trì. |
| So với | google-sre-workbook (tri thức SRE dạng checklist, không phải skill chạy được), kubernetes và các skill vận hành khác ở mục 33 |
| Nguồn | [LICENSE](https://github.com/culiops/culiops-skills/blob/40d9310d51a6b43d6d78bb0928193b705bd1910a/LICENSE) · [README.md](https://github.com/culiops/culiops-skills/blob/40d9310d51a6b43d6d78bb0928193b705bd1910a/README.md) · [skills/sre-investigate/SKILL.md](https://github.com/culiops/culiops-skills/blob/40d9310d51a6b43d6d78bb0928193b705bd1910a/skills/sre-investigate/SKILL.md) · [.claude-plugin/plugin.json](https://github.com/culiops/culiops-skills/blob/40d9310d51a6b43d6d78bb0928193b705bd1910a/.claude-plugin/plugin.json) · [CHANGELOG.md](https://github.com/culiops/culiops-skills/blob/40d9310d51a6b43d6d78bb0928193b705bd1910a/CHANGELOG.md) · [tests/fixtures/sre-investigate/injection-in-logs/DRY-RUN-NOTES.md](https://github.com/culiops/culiops-skills/blob/40d9310d51a6b43d6d78bb0928193b705bd1910a/tests/fixtures/sre-investigate/injection-in-logs/DRY-RUN-NOTES.md) |

<a id="n2-2026-11-24"></a>

## Nâng trần đợt hai — 23/11/2026

Hồ sơ lập trong đợt nâng trần thứ hai: đọc mã hoặc tài liệu tại commit cố định, chưa chạy upstream; mô tả của trinh sát sai ở nhiều repo nên điều ghi ở đây là điều đã đọc.

<a id="n2-dress-rehearsal"></a>

### dress-rehearsal

| Thuộc tính | Giá trị |
|---|---|
| Repo | https://github.com/ruinosus/dress-rehearsal |
| License | MIT (ruinosus, 2026); `npm/LICENSE` cho gói npm |
| Phiên bản đã đọc | `20d277084312e5c7d79a522dacb028a2c34c359a` (commit 2026-11-01) |
| Kiểm chứng | 2026-11-24; code-read; đã đọc LICENSE, README, CHANGELOG, SKILL.md, src/drill.ts, src/review.ts, src/play.ts, tools/check.mjs, một drill mẫu, một grader eval, npm/package.json; chưa chạy upstream |
| Khoảng trống lấp | Skill vận hành SRE/incident/runbook (diễn tập runbook) |
| Cơ chế đáng học | - `src/drill.ts` (`readDrill`): báo lỗi có số dòng cho cảnh dẫn tới id không tồn tại, cảnh kẹt không có lối ra, vai trò lạ, đồng hồ sai; không có kết thúc nào tới được từ điểm bắt đầu thì lỗi `noEnd`.<br>- `src/review.ts` (`reviewDrill`): cảnh không ai tới, cảnh không còn đường tới kết thúc, lựa chọn cần quyền mà không vai trò nào có, không lựa chọn nào báo người bị ảnh hưởng, 'escalate' không có người nhận.<br>- `SKILL.md`: mục `gaps` là sản phẩm thật (những gì runbook thiếu), tình huống và số liệu là hư cấu nhưng hệ thống/người của đội thì không được bịa.<br>- `src/play.ts` tính đồng hồ, tổn thất và debrief (Markdown và CSV cải tiến) thành hàm thuần để test chơi trọn ván. |
| Tiêu chí và cách kiểm | `tools/check.mjs` chạy các check `checks/*.check.ts`, build từng ví dụ ra HTML và kịch bản, xác nhận file hỏng báo đúng dòng, trang game không tải gì từ internet và (khi có trình duyệt) chơi hết ván trong trình duyệt headless. Thư mục `evals/` có prompt và grader (ví dụ `no-build.md`: câu hỏi thường không được gọi `build.mjs`). Repo không có workflow CI (không thấy `.github/workflows`), nên check chạy cục bộ, và tôi chưa chạy. |
| Giới hạn và rủi ro | Repo đã chuyển nơi ở (README trỏ sang house-lights) nên có thể không còn cập nhật; cần Node 18+ và agent chạy mã. Hậu quả từng lựa chọn trong drill là phỏng đoán của agent từ runbook, không phải mô phỏng hệ thống thật. Hai ví dụ đều hư cấu. 0 sao. |
| So với | culiops-skills, claude-code-game-studios, academic-research-skills |
| Nguồn | [README.md](https://github.com/ruinosus/dress-rehearsal/blob/20d277084312e5c7d79a522dacb028a2c34c359a/README.md) · [LICENSE](https://github.com/ruinosus/dress-rehearsal/blob/20d277084312e5c7d79a522dacb028a2c34c359a/LICENSE) · [CHANGELOG.md](https://github.com/ruinosus/dress-rehearsal/blob/20d277084312e5c7d79a522dacb028a2c34c359a/CHANGELOG.md) · [SKILL.md](https://github.com/ruinosus/dress-rehearsal/blob/20d277084312e5c7d79a522dacb028a2c34c359a/skills/dress-rehearsal/SKILL.md) · [drill.ts](https://github.com/ruinosus/dress-rehearsal/blob/20d277084312e5c7d79a522dacb028a2c34c359a/src/drill.ts) · [review.ts](https://github.com/ruinosus/dress-rehearsal/blob/20d277084312e5c7d79a522dacb028a2c34c359a/src/review.ts) · [play.ts](https://github.com/ruinosus/dress-rehearsal/blob/20d277084312e5c7d79a522dacb028a2c34c359a/src/play.ts) · [check.mjs](https://github.com/ruinosus/dress-rehearsal/blob/20d277084312e5c7d79a522dacb028a2c34c359a/tools/check.mjs) · [database-disk.drill.yaml](https://github.com/ruinosus/dress-rehearsal/blob/20d277084312e5c7d79a522dacb028a2c34c359a/docs/examples/database-disk.drill.yaml) · [no-build.md](https://github.com/ruinosus/dress-rehearsal/blob/20d277084312e5c7d79a522dacb028a2c34c359a/evals/not-a-drill-en/graders/no-build.md) · [package.json](https://github.com/ruinosus/dress-rehearsal/blob/20d277084312e5c7d79a522dacb028a2c34c359a/npm/package.json) |

<a id="n2-chaos-mesh"></a>

### Chaos Mesh

| Thuộc tính | Giá trị |
|---|---|
| Repo | https://github.com/chaos-mesh/chaos-mesh |
| License | Apache-2.0 |
| Phiên bản đã đọc | `fdb9684b50c268b89c8007270f567df788913494` (commit 2026-11-22) |
| Kiểm chứng | 2026-11-24; code-read; đã đọc README.md, LICENSE, api/v1alpha1/podchaos_types.go, statuscheck_types.go, workflow_types.go, schedule_types.go, controllers/README.md, helm/chaos-mesh/values.yaml, .github/workflows/ci.yml (các bước run); chưa chạy upstream |
| Khoảng trống lấp | Fuzz, mutation, chaos/resilience (chaos engineering cho Kubernetes) |
| Cơ chế đáng học | - Mỗi loại lỗi là một CRD; `PodChaosSpec` có action `pod-kill`, `pod-failure`, `container-kill`, `duration`, `gracePeriod`; README liệt kê thêm mạng, DNS, HTTP, I/O, thời gian, stress, kernel, JVM, máy vật lý và lỗi cloud AWS, Azure, GCP.<br>- `StatusCheck` (api/v1alpha1/statuscheck_types.go) kiểm sức khỏe ứng dụng bằng HTTP với `mode` (Synchronous hoặc Continuous), `intervalSeconds` mặc định 10, `failureThreshold` mặc định 3, `successThreshold` mặc định 1; trong `Workflow`, `abortWithStatusCheck` hủy workflow khi vượt ngưỡng lỗi.<br>- `Schedule` có `concurrencyPolicy` (Forbid hoặc Allow) và `startingDeadlineSeconds`; `Workflow` điều phối tuần tự hay song song. Chaos Daemon chạy DaemonSet để thực hiện thao tác đặc quyền ở node. |
| Tiêu chí và cách kiểm | Điều kiện dừng thử nghiệm là ngưỡng StatusCheck nêu trên; phần còn lại là kết quả điều kiện CRD. Kiểm máy: CI (ci.yml) chạy `make check`, `make test` hoặc `make test-pr` trong dev-env, kiểm sinh protobuf và Helm chart, cùng `pnpm build` và `pnpm test` cho dashboard; có workflow e2e riêng (chưa mở e2e_test.yml). Chưa chạy. |
| Giới hạn và rủi ro | Chaos Daemon đặc quyền: helm values đặt `privileged: true` kèm capability SYS_PTRACE, NET_ADMIN, NET_RAW, và DaemonSet dùng `hostPID: true`; cần tách cluster thử nghiệm và quyền RBAC chặt (có `enableFilterNamespace` mặc định false). Mở rộng quy mô lỗi sai có thể gây sự cố thật. README nói đây là dự án CNCF incubating (tuyên bố của tác giả, chưa xác minh). Không thấy telemetry trong phần đã đọc, chưa rà toàn mã. Có CLAUDE.md và AGENTS.md trong repo, coi là nội dung đọc. |
| So với | `shopify-toxiproxy` (proxy lỗi mạng cho test, nhẹ hơn nhiều, không cần Kubernetes); `google-oss-fuzz` (fuzz, khác lớp lỗi). |
| Nguồn | [README](https://github.com/chaos-mesh/chaos-mesh/blob/fdb9684b50c268b89c8007270f567df788913494/README.md) · [LICENSE](https://github.com/chaos-mesh/chaos-mesh/blob/fdb9684b50c268b89c8007270f567df788913494/LICENSE) · [api/v1alpha1/podchaos_types.go](https://github.com/chaos-mesh/chaos-mesh/blob/fdb9684b50c268b89c8007270f567df788913494/api/v1alpha1/podchaos_types.go) · [api/v1alpha1/statuscheck_types.go](https://github.com/chaos-mesh/chaos-mesh/blob/fdb9684b50c268b89c8007270f567df788913494/api/v1alpha1/statuscheck_types.go) · [api/v1alpha1/workflow_types.go](https://github.com/chaos-mesh/chaos-mesh/blob/fdb9684b50c268b89c8007270f567df788913494/api/v1alpha1/workflow_types.go) · [api/v1alpha1/schedule_types.go](https://github.com/chaos-mesh/chaos-mesh/blob/fdb9684b50c268b89c8007270f567df788913494/api/v1alpha1/schedule_types.go) · [controllers/README.md](https://github.com/chaos-mesh/chaos-mesh/blob/fdb9684b50c268b89c8007270f567df788913494/controllers/README.md) · [helm/chaos-mesh/values.yaml](https://github.com/chaos-mesh/chaos-mesh/blob/fdb9684b50c268b89c8007270f567df788913494/helm/chaos-mesh/values.yaml) · [.github/workflows/ci.yml](https://github.com/chaos-mesh/chaos-mesh/blob/fdb9684b50c268b89c8007270f567df788913494/.github/workflows/ci.yml) |

<a id="n2-litmuschaos"></a>

### LitmusChaos

| Thuộc tính | Giá trị |
|---|---|
| Repo | https://github.com/litmuschaos/litmus |
| License | Apache-2.0 |
| Phiên bản đã đọc | `97a397fb2e3cb3e3ab41e9bd301b9143da547b6f` (commit 2026-10-27) |
| Kiểm chứng | 2026-11-24; docs-read; đã đọc README, LICENSE, NOTICE, tiêu chí trưởng thành thí nghiệm, schema probe của chaoscenter, workflow cifuzz và e2e; chưa chạy upstream |
| Khoảng trống lấp | Chaos/resilience: chủ động gây lỗi có kiểm soát trên Kubernetes và chấm điểm khả năng chịu lỗi (khoảng trống Fuzz, mutation, chaos của kho) |
| Cơ chế đáng học | • Chaos là tài nguyên Kubernetes: ChaosExperiment (mẫu cài đặt của một lỗi), ChaosEngine (gắn lỗi vào workload, kèm giả thuyết trạng thái ổn định), ChaosResult (kết quả) — README.md.<br>• Probe là phép kiểm giả thuyết ổn định: có loại HTTP, lệnh, Prometheus, k8s; mỗi probe có timeout, interval, retry, attempt và cờ `stop_on_failure`; chaoscenter lưu `average_success_percentage` mỗi probe — `probe/schema.go`.<br>• Mỗi lần chạy có `resiliency_score` (điểm khả năng chịu lỗi) lưu theo run và theo experiment — `chaos_experiment_run/schema.go` (đọc qua grep, không mở trọn).<br>• Thang trưởng thành Alpha/Beta/GA cho thí nghiệm (phải có tiêu chí vào/ra, hoàn tác sạch, không để rác, chạy được trên 2 rồi 4 nền k8s) — `CHAOS_EXPERIMENT_MATURITY.md`; dùng được làm checklist viết một thí nghiệm chaos. |
| Tiêu chí và cách kiểm | Ngưỡng cụ thể nằm ở cấu hình từng probe và thang trưởng thành; test của chính repo: CIFuzz (oss-fuzz, sanitizer address, 120 giây, chỉ khi PR chạm authentication, graphql, subscriber) và workflow e2e kích bằng comment `/run-e2e` trên PR. Đã mở hai workflow; chưa xác minh kết quả chạy. |
| Giới hạn và rủi ro | Phải chạy trên Kubernetes cùng control plane (GraphQL, MongoDB, auth) — nặng so với công cụ thư viện; thư mục `chaos-engineering/` chỉ có `.gitkeep` nên mã lỗi cụ thể nằm ở repo khác (chưa xác minh repo nào, README nhắc ChaosHub ở repo community-charts). Apache-2.0, NOTICE nói có thành phần bên thứ ba theo license riêng (xem báo cáo FOSSA). Quét từ khóa telemetry và analytics trong mã server không thấy gửi số liệu (grep, chưa chứng minh phủ hết). Dự án CNCF, đẩy mã gần đây (10/2026). |
| So với | [Toxiproxy](30-software-testing-quality/README.md#nt-shopify-toxiproxy) (chèn lỗi mạng ở mức proxy, nhẹ hơn nhiều) · [Grafana k6](30-software-testing-quality/README.md) (tải, không phải chaos) · [OSS-Fuzz](30-software-testing-quality/README.md#nt-google-oss-fuzz) (fuzz mã, khác tầng) |
| Nguồn | [README.md](https://github.com/litmuschaos/litmus/blob/97a397fb2e3cb3e3ab41e9bd301b9143da547b6f/README.md) · [LICENSE](https://github.com/litmuschaos/litmus/blob/97a397fb2e3cb3e3ab41e9bd301b9143da547b6f/LICENSE) · [NOTICE.md](https://github.com/litmuschaos/litmus/blob/97a397fb2e3cb3e3ab41e9bd301b9143da547b6f/NOTICE.md) · [CHAOS_EXPERIMENT_MATURITY.md](https://github.com/litmuschaos/litmus/blob/97a397fb2e3cb3e3ab41e9bd301b9143da547b6f/CHAOS_EXPERIMENT_MATURITY.md) · [schema.go](https://github.com/litmuschaos/litmus/blob/97a397fb2e3cb3e3ab41e9bd301b9143da547b6f/chaoscenter/graphql/server/pkg/database/mongodb/probe/schema.go) · [cifuzz.yml](https://github.com/litmuschaos/litmus/blob/97a397fb2e3cb3e3ab41e9bd301b9143da547b6f/.github/workflows/cifuzz.yml) · [e2e.yml](https://github.com/litmuschaos/litmus/blob/97a397fb2e3cb3e3ab41e9bd301b9143da547b6f/.github/workflows/e2e.yml) |

<a id="n2-dash0-agent-skills"></a>

### Dash0 OpenTelemetry skills

| Thuộc tính | Giá trị |
|---|---|
| Repo | https://github.com/dash0hq/agent-skills |
| License | Apache-2.0 |
| Phiên bản đã đọc | `7bb506b71536fea51f08afa509bf198b42bae8b7` (commit 2026-11-23) |
| Kiểm chứng | 2026-11-24; code-read; đã đọc README, LICENSE, plugin.json, skills/otel-ottl/SKILL.md, evals/custom/README.md và evals-pr.yml; chưa chạy upstream |
| Khoảng trống lấp | Skill dạy agent gắn OpenTelemetry vào ứng dụng, có eval chấm bằng telemetry thật; không phải quan sát hay phát lại phiên agent như trinh sát ghi |
| Cơ chế đáng học | (1) Bốn skill vendor-neutral: otel-instrumentation, otel-collector, otel-ottl, otel-semantic-conventions, kèm thư mục `rules/` tách theo chủ đề (`skills/*/SKILL.md`). (2) Harness eval chạy Claude Code headless trên ứng dụng mẫu, thu telemetry OTLP qua relay và sink, kết luận bằng khẳng định tất định, không dùng LLM làm giám khảo (`evals/custom/README.md`). (3) Lớp lỗi của verdict tách `infra` (thử lại tối đa 3 lần) khỏi `agent-noskill`, `agent-build`, `agent-telemetry`. |
| Tiêu chí và cách kiểm | Mọi khối mã trong `skills/` được trích và kiểm tất định; cổng `evals-gate` đặt đúng một tên job cho branch protection và thất bại khi job bị bỏ qua mà chưa chọn 0 kịch bản (đọc trong `evals-pr.yml`). Khoá API chỉ nằm ở environment secret `evals`, PR từ fork và Dependabot không chạy agent. Chưa chạy lại eval, kết quả tự công bố (chưa xác minh). |
| Giới hạn và rủi ro | Cần ANTHROPIC_API_KEY, Docker và CLI Claude Code cố định phiên bản để chạy eval cục bộ. Skill là văn bản, không mã chạy; gói npm ship nguyên thư mục skills. Tác giả là hãng quan sát nên ví dụ có thể thiên về Dash0 (chưa xác minh mức độ). Số sao do trinh sát ghi (102) chưa tự kiểm. |
| So với | OpenTelemetry Collector Contrib (thành phần được dạy), OpenTelemetry Weaver (kiểm quy ước ngữ nghĩa), CulIOps skills (skill vận hành khác) |
| Nguồn | [README.md](https://github.com/dash0hq/agent-skills/blob/7bb506b71536fea51f08afa509bf198b42bae8b7/README.md) · [LICENSE](https://github.com/dash0hq/agent-skills/blob/7bb506b71536fea51f08afa509bf198b42bae8b7/LICENSE) · [plugin.json](https://github.com/dash0hq/agent-skills/blob/7bb506b71536fea51f08afa509bf198b42bae8b7/plugin.json) · [SKILL.md](https://github.com/dash0hq/agent-skills/blob/7bb506b71536fea51f08afa509bf198b42bae8b7/skills/otel-ottl/SKILL.md) · [README.md](https://github.com/dash0hq/agent-skills/blob/7bb506b71536fea51f08afa509bf198b42bae8b7/evals/custom/README.md) · [evals-pr.yml](https://github.com/dash0hq/agent-skills/blob/7bb506b71536fea51f08afa509bf198b42bae8b7/.github/workflows/evals-pr.yml) |

<a id="n2-healthchecks"></a>

### Healthchecks

| Thuộc tính | Giá trị |
|---|---|
| Repo | https://github.com/healthchecks/healthchecks |
| License | BSD-3-Clause |
| Phiên bản đã đọc | `c1039ad23395162c5e2f17d324d8ccdaa60a1d14` (commit 2026-11-23) |
| Kiểm chứng | 2026-11-24; code-read; đã đọc README.md, hc/api/models.py, sendalerts.py, urls.py, settings.py, tests.yml, LICENSE; chưa chạy upstream |
| Khoảng trống lấp | Giám sát job định kỳ (dead-man's switch, SLO cho cron) tự host được |
| Cơ chế đáng học | - `Check.get_grace_start`, `going_down_after`, `get_status` tính thời điểm down từ `last_ping`, lịch và `grace`; có `last_start` để bắt job chạy quá lâu (`hc/api/models.py`).<br>- `sendalerts.handle_going_down`: chọn check có `alert_after` quá hạn, tính lại trạng thái, cập nhật nguyên tử, chỉ tạo `Flip` khi đúng một dòng được cập nhật.<br>- Ping qua HTTP hoặc email (`hc/api/management/commands/smtpd.py`), lưu thân ping tối đa `PING_BODY_LIMIT` (mặc định 10000 byte).<br>- Notification chạy trong ThreadPoolExecutor và có thống kê statsd. |
| Tiêu chí và cách kiểm | CI `tests.yml` chạy `python manage.py test` trên ma trận 4 cơ sở dữ liệu (sqlite, postgres, mysql, mariadb) và Python 3.12–3.15; thêm workflow coverage và mypy. Khoảng 441 hàm test trong `hc/api/tests` (đếm bằng grep). |
| Giới hạn và rủi ro | - BSD-3-Clause; bản hosted healthchecks.io tính phí, code payments nằm trong cùng repo.<br>- Mặc định `DEBUG=True` và `REGISTRATION_OPEN=True` trong `settings.py`: triển khai thật phải đổi.<br>- Cần `SECRET_KEY` thật, cơ sở dữ liệu và SMTP; ngoài ra có tích hợp gửi tới dịch vụ bên thứ ba do người dùng cấu hình.<br>- Chỉ cảnh báo khi job im lặng; không đảm bảo job chạy đúng kết quả nếu ping được gọi sai chỗ. |
| So với | uptime-kuma (giám sát uptime chủ động, khác mô hình ping thụ động), celery-celery (lập lịch), bullmq (scheduler, không giám sát) |
| Nguồn | [README.md](https://github.com/healthchecks/healthchecks/blob/c1039ad23395162c5e2f17d324d8ccdaa60a1d14/README.md) · [LICENSE](https://github.com/healthchecks/healthchecks/blob/c1039ad23395162c5e2f17d324d8ccdaa60a1d14/LICENSE) · [models.py](https://github.com/healthchecks/healthchecks/blob/c1039ad23395162c5e2f17d324d8ccdaa60a1d14/hc/api/models.py) · [sendalerts.py](https://github.com/healthchecks/healthchecks/blob/c1039ad23395162c5e2f17d324d8ccdaa60a1d14/hc/api/management/commands/sendalerts.py) · [urls.py](https://github.com/healthchecks/healthchecks/blob/c1039ad23395162c5e2f17d324d8ccdaa60a1d14/hc/api/urls.py) · [settings.py](https://github.com/healthchecks/healthchecks/blob/c1039ad23395162c5e2f17d324d8ccdaa60a1d14/hc/settings.py) · [tests.yml](https://github.com/healthchecks/healthchecks/blob/c1039ad23395162c5e2f17d324d8ccdaa60a1d14/.github/workflows/tests.yml) |

<a id="n2-stackstorm-st2"></a>

### StackStorm (st2)

| Thuộc tính | Giá trị |
|---|---|
| Repo | https://github.com/StackStorm/st2 |
| License | Apache-2.0 |
| Phiên bản đã đọc | `bb348ad74781e15a177b39a4d5e701fa395fa460` (commit 2026-11-20) |
| Kiểm chứng | 2026-11-24; code-read; đã đọc README.md, LICENSE, st2reactor/st2reactor/rules/filter.py, contrib/examples/rules/notify_inquiry.yaml, .github/workflows/ci.yaml, CHANGELOG.rst; chưa chạy upstream |
| Khoảng trống lấp | Runbook automation và remediation theo sự kiện (ITOps): sensor, trigger, rule, action, kèm cổng duyệt người (Inquiry) |
| Cơ chế đáng học | - Rule = trigger + criteria + action: `RuleFilter.filter()` trong `st2reactor/st2reactor/rules/filter.py` duyệt từng tiêu chí, render pattern bằng Jinja rồi gọi toán tử trong `st2common/st2common/operators.py` (equals, iequals, regex, match_wildcard, timediff_lt/gt, inside, exists, search lồng điều kiện); mọi lỗi render/so khớp tạo `RuleEnforcementDB` với `failure_reason` thay vì nuốt lỗi.<br>- Loại rule `standard` và `backstop` (`st2common/constants/rules.py`): backstop dùng làm lưới đỡ khi không rule nào khớp.<br>- Inquiry (`st2common/st2common/services/inquiry.py`): action chờ phản hồi người, kiểm quyền theo `roles` và `users`, kiểm phản hồi theo schema; ví dụ rule `contrib/examples/rules/notify_inquiry.yaml` đẩy thông báo Slack khi có Inquiry chờ duyệt (mẫu đang `enabled: false`).<br>- Có `garbage_collection/` dọn trigger instance, execution, inquiry, trace theo TTL (đọc tên file). |
| Tiêu chí và cách kiểm | CI `.github/workflows/ci.yaml` chạy lint và test trên ma trận Python 3.10/3.11/3.12 (push master, PR, cron hằng đêm); đã mở file. Test unit/integration nằm ở `st2tests` và từng gói; kết quả chưa chạy lại. Rule có công cụ thử `st2reactor/rules/tester.py` (chỉ đọc tên). |
| Giới hạn và rủi ro | Apache-2.0 sạch. Vận hành nặng (nhiều dịch vụ nền, cài bằng script `install.sh` tải từ stackstorm.com, nội dung README, chưa xác minh). Không thấy telemetry khi grep thô trong `st2common`; chưa xác minh toàn bộ. Badge Python trong README lỗi thời. Mô tả trinh sát đúng nhưng Inquiry/ChatOps là phần phụ, lõi là rule engine. |
| So với | kestra, windmill, n8n, huginn |
| Nguồn | [README.md](https://github.com/StackStorm/st2/blob/bb348ad74781e15a177b39a4d5e701fa395fa460/README.md) · [LICENSE](https://github.com/StackStorm/st2/blob/bb348ad74781e15a177b39a4d5e701fa395fa460/LICENSE) · [filter.py](https://github.com/StackStorm/st2/blob/bb348ad74781e15a177b39a4d5e701fa395fa460/st2reactor/st2reactor/rules/filter.py) · [notify_inquiry.yaml](https://github.com/StackStorm/st2/blob/bb348ad74781e15a177b39a4d5e701fa395fa460/contrib/examples/rules/notify_inquiry.yaml) · [ci.yaml](https://github.com/StackStorm/st2/blob/bb348ad74781e15a177b39a4d5e701fa395fa460/.github/workflows/ci.yaml) · [CHANGELOG.rst](https://github.com/StackStorm/st2/blob/bb348ad74781e15a177b39a4d5e701fa395fa460/CHANGELOG.rst) |

<a id="n2-prometheus"></a>

### Prometheus

| Thuộc tính | Giá trị |
|---|---|
| Repo | https://github.com/prometheus/prometheus |
| License | Apache-2.0 |
| Phiên bản đã đọc | `a5022ef622b4718c3dda1291c1e641fbed44c607` (commit 2026-11-23) |
| Kiểm chứng | 2026-11-24; code-read; đã đọc README.md, LICENSE, AGENTS.md, cmd/promtool/unittest.go, cmd/promtool/testdata/unittest.yml, cmd/promtool/main.go, .github/workflows/ci.yml, .github/workflows/fuzzing.yml; chưa chạy upstream |
| Khoảng trống lấp | Quan sát hệ thống: metric và cảnh báo; rule kiểm được bằng máy |
| Cơ chế đáng học | - Unit test cho rule: file YAML khai `input_series` (cú pháp `1+1x2`, `stale`, `_`), `promql_expr_test` và `alert_rule_test`; `cmd/promtool/unittest.go` nạp rule, dựng bộ nhớ giả, chạy đúng `eval_time`, so kết quả, hỗ trợ `--diff`, `--run` và xuất JUnit XML (`unittest.go`, `testdata/unittest.yml`).<br>- Lint rule/cấu hình bằng cờ `--lint=all\|duplicate-rules\|none` và `--lint-fatal` (exit code 3 khi có vấn đề lint) tách biệt với exit code lỗi cú pháp (`cmd/promtool/main.go`).<br>- Fuzz parser và chunk bằng Go native fuzz trong CI, mỗi mục 4 phút, đẩy artifact crash khi hỏng (`.github/workflows/fuzzing.yml`).<br>- AGENTS.md ghi quy ước PR (tiêu đề `area: mô tả`) cho agent, rút từ review thật. |
| Tiêu chí và cách kiểm | Test rule chạy bằng máy (`promtool test rules`), CI Go có ma trận race/386/dedupelabels/LTS, kiểm `git diff --exit-code` sau sinh proto, workflow fuzzing, govulncheck, scorecards, zizmor (đã mở ci.yml và fuzzing.yml; các workflow khác chỉ biết tên file). Ngưỡng alert do người viết rule tự đặt; Prometheus không đề xuất ngưỡng. |
| Giới hạn và rủi ro | Apache-2.0, không thấy telemetry trong README (chưa dò mã). Bảo trì rất sôi động (commit 2026-11-23, VERSION 3.16.0). Lint mặc định hẹp (chỉ duplicate-rules). Lưu trữ đơn nút, không bền vững dài hạn khi mất đĩa; trinh sát gợi ý category devops/ci-cd-release là chưa đúng, đây là giám sát. |
| So với | `grafana`, `opencost`, `vector`, `getsentry-sentry` |
| Nguồn | [README.md](https://github.com/prometheus/prometheus/blob/a5022ef622b4718c3dda1291c1e641fbed44c607/README.md) · [LICENSE](https://github.com/prometheus/prometheus/blob/a5022ef622b4718c3dda1291c1e641fbed44c607/LICENSE) · [AGENTS.md](https://github.com/prometheus/prometheus/blob/a5022ef622b4718c3dda1291c1e641fbed44c607/AGENTS.md) · [unittest.go](https://github.com/prometheus/prometheus/blob/a5022ef622b4718c3dda1291c1e641fbed44c607/cmd/promtool/unittest.go) · [unittest.yml](https://github.com/prometheus/prometheus/blob/a5022ef622b4718c3dda1291c1e641fbed44c607/cmd/promtool/testdata/unittest.yml) · [main.go](https://github.com/prometheus/prometheus/blob/a5022ef622b4718c3dda1291c1e641fbed44c607/cmd/promtool/main.go) · [ci.yml](https://github.com/prometheus/prometheus/blob/a5022ef622b4718c3dda1291c1e641fbed44c607/.github/workflows/ci.yml) · [fuzzing.yml](https://github.com/prometheus/prometheus/blob/a5022ef622b4718c3dda1291c1e641fbed44c607/.github/workflows/fuzzing.yml) |

<a id="n2-infracost"></a>

### Infracost

| Thuộc tính | Giá trị |
|---|---|
| Repo | https://github.com/infracost/infracost |
| License | Apache-2.0 |
| Phiên bản đã đọc | `b8c2bd6e345b30c2c88c36431bed78cfc13885a5` (commit 2026-11-20) |
| Kiểm chứng | 2026-11-24; code-read; đã đọc README.md, LICENSE, AGENTS.md, infracost-example.yml, internal/resources/aws/s3_bucket.go, internal/config/config.go, .github/workflows/go.yml; chưa chạy upstream |
| Khoảng trống lấp | GitOps và FinOps: ước tính chi phí hạ tầng ngay trong PR |
| Cơ chế đáng học | - Mỗi loại tài nguyên là một struct Go có 3 nhóm tham số: bắt buộc, tuỳ chọn, `infracost_usage` (khai báo mức dùng như số object tag); `UsageSchema()` công bố khoá và mặc định (`internal/resources/aws/s3_bucket.go`).<br>- File cấu hình dự án + file usage tách giả định mức dùng khỏi mã hạ tầng (`infracost-example.yml`, `infracost-usage-example.yml`).<br>- Đầu ra nhiều định dạng (table, json, markdown, html, slack) và lệnh `comment` cho GitHub/GitLab/Bitbucket/Azure Repos (`internal/output`, `cmd/infracost/comment_*.go`).<br>- Giá lấy từ API giá của hãng, không nhúng bảng giá trong mã (`internal/config/config.go`, `pricing.api.infracost.io`). |
| Tiêu chí và cách kiểm | CI go.yml chạy golangci-lint, kiểm định dạng Terraform, `make test_shared_int`, benchmark parser (đã mở). Không có ngưỡng chi phí chặn merge trong mã đã đọc; chính sách ngân sách/tag nằm ở Infracost Cloud (tuyên bố trong README, chưa xác minh). |
| Giới hạn và rủi ro | Apache-2.0 nhưng AGENTS.md ghi rõ repo EOL, không nhận PR/issue; phải có `INFRACOST_API_KEY` và mã gửi sự kiện (`AddEvent`, `EventsDisabled`) tới API của hãng, tắt được trong cấu hình (chưa kiểm chi tiết). Cloud/SaaS là phần có phí. README mô tả 1.100+ tài nguyên là tuyên bố tác giả (chưa xác minh). |
| So với | `opencost` (chi phí Kubernetes thực tế), `terraform`, `opentofu` |
| Nguồn | [README.md](https://github.com/infracost/infracost/blob/b8c2bd6e345b30c2c88c36431bed78cfc13885a5/README.md) · [LICENSE](https://github.com/infracost/infracost/blob/b8c2bd6e345b30c2c88c36431bed78cfc13885a5/LICENSE) · [AGENTS.md](https://github.com/infracost/infracost/blob/b8c2bd6e345b30c2c88c36431bed78cfc13885a5/AGENTS.md) · [infracost-example.yml](https://github.com/infracost/infracost/blob/b8c2bd6e345b30c2c88c36431bed78cfc13885a5/infracost-example.yml) · [s3_bucket.go](https://github.com/infracost/infracost/blob/b8c2bd6e345b30c2c88c36431bed78cfc13885a5/internal/resources/aws/s3_bucket.go) · [config.go](https://github.com/infracost/infracost/blob/b8c2bd6e345b30c2c88c36431bed78cfc13885a5/internal/config/config.go) · [go.yml](https://github.com/infracost/infracost/blob/b8c2bd6e345b30c2c88c36431bed78cfc13885a5/.github/workflows/go.yml) |
