# 28 · Product Discovery, UX Research & Experimentation

Từ vấn đề người dùng đến quyết định sản phẩm có bằng chứng. Ngày đọc **2026-11-02**: đã đọc README/LICENSE, workflow kiểm và các file triển khai dẫn trong hồ sơ; **chưa triển khai dịch vụ, bắt gói SDK hoặc chạy thí nghiệm người dùng**.

## 1. Chuỗi quyết định trước khi chọn công cụ

| Câu hỏi | Phương pháp / công cụ | Bằng chứng cần giữ |
|---|---|---|
| Người dùng đang gặp khó ở đâu? | Phỏng vấn, quan sát công việc, khảo sát có mục tiêu | Tuyển mẫu, consent, ghi nhận ẩn danh, phân biệt quan sát với diễn giải |
| Giải pháp có dễ dùng? | Prototype + usability test theo tác vụ | Completion, lỗi, thời gian, hỗ trợ cần dùng; người dùng đích và người khuyết tật |
| Hành vi thực tế thế nào? | PostHog/funnel/cohort; replay khi cần | Event dictionary, mẫu số, identity, phiên bản tracking, tỷ lệ thiếu event |
| Thay đổi có tạo tác động? | GrowthBook/experiment engine + assignment/exposure log | Hypothesis, randomization unit, sample size/MDE, guardrails, SRM |
| Phát hành có kiểm soát? | Unleash/feature flags | Rollout, kill switch, owner/expiry, rollback đã diễn tập |
| Vì sao người dùng bỏ cuộc? | Formbricks + replay đã che dữ liệu | Ngữ cảnh khảo sát, selection bias, giới hạn capture và retention |

[Mục 06](../06-ui-ux-design/README.md) kiểm chất lượng UI; [07](../07-eval-observability/README.md) kiểm AI; mục này kiểm **người dùng có hoàn thành công việc tốt hơn không**. Chỉ số model tốt hơn chưa đủ để kết luận sản phẩm tốt hơn.

## 2. Hồ sơ công cụ

### PostHog

| Thuộc tính | Giá trị |
|---|---|
| Repo | [PostHog/posthog](https://github.com/PostHog/posthog) |
| Snapshot | 40,593★, chưa archive (GitHub API, 2026-11-02); HEAD `1df14a1b82c7` ngày 2026-11-02 |
| License | MIT (core); proprietary (ee); [file thật](https://github.com/PostHog/posthog/blob/1df14a1b82c7a24e0a4a0d19b7c708c9e76ee9a5/LICENSE) |
| Bằng chứng | [Triển khai/đặc tả](https://github.com/PostHog/posthog/blob/1df14a1b82c7a24e0a4a0d19b7c708c9e76ee9a5/products/feature_flags/backend/models/feature_flag.py); [CI tại cùng commit](https://github.com/PostHog/posthog/tree/1df14a1b82c7a24e0a4a0d19b7c708c9e76ee9a5/.github/workflows); đọc mã/đặc tả, chưa chạy |

Nền tảng analytics/replay/flags/experiments. Model feature flag có validation cho variants và eligibility; kết hợp hành vi và thử nghiệm, nhưng không thay thiết kế nghiên cứu hay metric contract.

**Tích hợp và giới hạn:** README chỉ hướng tự host hobby và không bảo đảm hỗ trợ deployment mở. LICENSE loại ee; kiểm feature/tài nguyên theo edition. SDK/capture endpoint/retention cần audit riêng; không suy self-host thành mọi dữ liệu không rời mạng.

### GrowthBook

| Thuộc tính | Giá trị |
|---|---|
| Repo | [growthbook/growthbook](https://github.com/growthbook/growthbook) |
| Snapshot | 8,556★, chưa archive (GitHub API, 2026-11-02); HEAD `0553a68def70` ngày 2026-10-30 |
| License | MIT (core); GrowthBook Enterprise License (enterprise dirs); [file thật](https://github.com/growthbook/growthbook/blob/0553a68def700abbcaaca8f5096da913f197804c/LICENSE) |
| Bằng chứng | [Triển khai/đặc tả](https://github.com/growthbook/growthbook/blob/0553a68def700abbcaaca8f5096da913f197804c/packages/sdk-js/src/GrowthBook.ts); [CI tại cùng commit](https://github.com/growthbook/growthbook/tree/0553a68def700abbcaaca8f5096da913f197804c/.github/workflows); đọc mã/đặc tả, chưa chạy |

SDK có trackingCallback/onFeatureUsage và state assignment; code trả sớm khi thiếu callback. Do đó chọn biến thể và ghi exposure thành công là hai việc phải kiểm riêng. CI có test thống kê và backend/frontend.

**Tích hợp và giới hạn:** SDK + event/warehouse/analysis; kiểm stable subject ID, sticky assignment và callback dedupe. Một flag được bật không chứng minh tác động có ý nghĩa; enterprise backend/frontend/shared là license riêng.

### Formbricks

| Thuộc tính | Giá trị |
|---|---|
| Repo | [formbricks/formbricks](https://github.com/formbricks/formbricks) |
| Snapshot | 13,211★, chưa archive (GitHub API, 2026-11-02); HEAD `76b05fb98dd8` ngày 2026-11-02 |
| License | AGPL-3.0 (core); MIT (SDKs); proprietary (ee); [file thật](https://github.com/formbricks/formbricks/blob/76b05fb98dd870000d820ad8a27527e483dcfbb0/LICENSE) |
| Bằng chứng | [Triển khai/đặc tả](https://github.com/formbricks/formbricks/blob/76b05fb98dd870000d820ad8a27527e483dcfbb0/apps/web/lib/response/service.ts); [CI tại cùng commit](https://github.com/formbricks/formbricks/tree/76b05fb98dd870000d820ad8a27527e483dcfbb0/.github/workflows); đọc mã/đặc tả, chưa chạy |

Khảo sát link/web/in-app phục vụ phản hồi có ngữ cảnh. Service response giữ status finished, language, contact/meta và file upload; phân tích cần tách đáp án hoàn thành, bỏ dở và selection bias.

**Tích hợp và giới hạn:** SDK/API/export nối kho dữ liệu; hạn chế PII/file upload, consent và retention. LICENSE tách core, SDK và ee; không suy nhãn AGPL toàn repo hay mọi feature tự host đều miễn phí.

### OpenReplay

| Thuộc tính | Giá trị |
|---|---|
| Repo | [openreplay/openreplay](https://github.com/openreplay/openreplay) |
| Snapshot | 13,087★, chưa archive (GitHub API, 2026-11-02); HEAD `9f1dcebfa5bd` ngày 2026-10-30 |
| License | AGPL-3.0 (default); MIT (một số thư mục); proprietary (ee); [file thật](https://github.com/openreplay/openreplay/blob/9f1dcebfa5bd98967c902b77b8fe7ed120ab5b2b/LICENSE) |
| Bằng chứng | [Triển khai/đặc tả](https://github.com/openreplay/openreplay/blob/9f1dcebfa5bd98967c902b77b8fe7ed120ab5b2b/tracker/tracker/src/main/app/sanitizer.ts); [CI tại cùng commit](https://github.com/openreplay/openreplay/tree/9f1dcebfa5bd98967c902b77b8fe7ed120ab5b2b/.github/workflows); đọc mã/đặc tả, chưa chạy |

Session replay có sanitizer cho DOM. Mã default privateMode=false, obscureTextEmails=true và obscureTextNumbers=false; cơ chế masking tồn tại không đồng nghĩa mọi nội dung mặc định đã che.

**Tích hợp và giới hạn:** Bật private mode/masking có kiểm bằng dữ liệu giả; xét input, DOM/shadow DOM, URL/network/plugin và quyền xem replay. LICENSE nhiều lớp; chưa bắt gói hay đánh giá capture end-to-end.

### Unleash

| Thuộc tính | Giá trị |
|---|---|
| Repo | [Unleash/unleash](https://github.com/Unleash/unleash) |
| Snapshot | 13,924★, chưa archive (GitHub API, 2026-11-02); HEAD `92cf79aad5d1` ngày 2026-11-02 |
| License | AGPL-3.0; [file thật](https://github.com/Unleash/unleash/blob/92cf79aad5d18e04cf72909e31f9b35a7840c355/LICENSE) |
| Bằng chứng | [Triển khai/đặc tả](https://github.com/Unleash/unleash/blob/92cf79aad5d18e04cf72909e31f9b35a7840c355/src/lib/features/playground/feature-evaluator/strategy/unknown-strategy.ts); [CI tại cùng commit](https://github.com/Unleash/unleash/tree/92cf79aad5d18e04cf72909e31f9b35a7840c355/.github/workflows); đọc mã/đặc tả, chưa chạy |

Feature management/rollout có SDK và strategy evaluation. Playground báo incomplete/unknown với custom strategy không thể đánh giá offline; trạng thái này không được đổi thành passed.

**Tích hợp và giới hạn:** SDK/server flag evaluation cần identity/context consistent, fallback khi mất server và kill switch. Server AGPL; edition Enterprise và license SDK kiểm riêng. Flag là cơ chế rollout, không thay authorization hoặc bằng chứng nhân quả.

## 3. Chuẩn phương pháp và cổng quyết định

Hướng dẫn gốc [GOV.UK: lập kế hoạch nghiên cứu](https://www.gov.uk/service-manual/user-research/plan-user-research-for-your-service) yêu cầu nghiên cứu theo người dùng/tác vụ thực tế. [Đo thành công dịch vụ](https://www.gov.uk/service-manual/measuring-success/measuring-the-success-of-your-service) kết hợp metric với nghiên cứu định tính. Đây là hướng dẫn phương pháp, không phải một chứng nhận tự động cho sản phẩm.

[Microsoft Research: trước thí nghiệm](https://www.microsoft.com/en-us/research/articles/patterns-of-trustworthy-experimentation-pre-experiment-stage/) và [sau thí nghiệm](https://www.microsoft.com/en-us/research/articles/patterns-of-trustworthy-experimentation-post-experiment-stage/) là nguồn cho data quality/guardrails và kiểm SRM. Phần vận dụng dưới đây là tiêu chí đề xuất của kho:

1. **Trước thu dữ liệu:** nêu quyết định cần đưa ra, phân khúc người dùng, metric chính và guardrails; chọn đúng đơn vị randomization (user/account/team). Phân tích power/MDE trước; lưu chính sách dừng và phương pháp thống kê, không nhìn p-value mỗi ngày bằng kiểm fixed-horizon rồi tự dừng khi xanh.
2. **Tracking contract:** định nghĩa event/schema/version, timestamp, event ID chống gửi trùng, subject ID và trạng thái consent. Assignment khác exposure; log việc người dùng thật sự được thấy treatment. Không gửi prompt/tài liệu/PII mặc định để làm analytics.
3. **Kiểm instrumentation:** event test, join rate, missing/duplicate event, A/A và SRM theo phương pháp đã chọn. Khác mẫu số hoặc attribution window thì không so trực tiếp hai dashboard.
4. **Khi chạy:** theo dõi crash/latency/chi phí/hỗ trợ và metric gây hại theo phân khúc; feature flag có đường tắt và kill switch. Kiểm tenant isolation và quyền xem replay, thời hạn retention/xóa dữ liệu.
5. **Khi kết luận:** báo effect size, khoảng bất định, cỡ mẫu, dữ liệu loại bỏ, ảnh hưởng guardrail và kết quả chưa đủ lực thống kê. Không có ý nghĩa thống kê không chứng minh hai phương án tương đương.
6. **Với AI:** giữ offline task eval + safety ở [07](../07-eval-observability/README.md)/[12](../12-ai-security-guardrails/README.md), bổ sung task completion/acceptance, tỷ lệ sửa tay, time-to-value, retention theo cohort, chi phí mỗi tác vụ được chấp nhận. Tách thay model khỏi thay UI khi cần biết nguyên nhân.

## 4. Stack ghép và giới hạn lựa chọn

- **Nhóm nhỏ, chưa có traffic đủ:** nghiên cứu định tính + usability + event tối thiểu; có thể dùng Formbricks. Không cần triển khai tất cả nền tảng để bắt đầu.
- **Đã có warehouse/event tốt:** GrowthBook + SDK/exposure callback + dữ liệu hiện có; test consistency giữa server/client và assignment sau login.
- **Cần điều tra hành trình:** PostHog hoặc OpenReplay tùy nhu cầu; kiểm masking bằng dữ liệu giả trước capture thật. Self-host chỉ là vị trí triển khai, chưa chứng minh mọi SDK/integration giữ dữ liệu trong mạng.
- **Cần rollout tin cậy:** Unleash + owner/expiry + kill switch; flag không thay transaction hoặc authorization. Nối với [13](../13-dev-stack-devops/README.md), [15](../15-ai-for-data/README.md), [21](../21-autonomous-workflows/README.md).

<a id="factory-2026-11-04"></a>

## 5. Nâng trần 4/11/2026: hợp đồng thử nghiệm độc lập nhà cung cấp và đo giá trị của xưởng

**Trần hiện tại:** §3 đã có A/A, SRM, exposure và metric. Khoảng thiếu là cách đưa chúng vào hợp đồng phát hành: tách flag evaluation, exposure và phân tích; đo đầu ra được khách hàng chấp nhận, không chỉ số code/PR do agent tạo. Phần metric/gate là thiết kế đề xuất, chưa chạy A/B hoặc đo ROI tại kho này.

| Lựa chọn | Khi hợp | Cần nối thêm | Giới hạn |
|---|---|---|---|
| PostHog ở §2 | Analytics/replay/flags trong cùng nền tảng | Event dictionary, consent, masking, phân quyền/retention | Tự host không tự chứng minh SDK/integration không gửi dữ liệu ngoài |
| GrowthBook ở §2 | Experiment gắn warehouse và assignment/exposure | Callback, metric model, audit query, unit randomization | Callback có trong mã chưa chứng minh event tới kho dữ liệu |
| Unleash ở §2 | Quản trị flag/rollout có owner và kill switch | Analytics/experiment engine độc lập | Flag không thay authorization hoặc bằng chứng nhân quả |
| OpenFeature + flagd dưới đây | Cần giao diện evaluation và daemon có thể thay provider | Cấu hình flag, SDK provider, exposure pipeline, phân tích thống kê | Không phải toàn bộ nền tảng A/B và không tự giải SRM/power |

<a id="flagd"></a>

### flagd: bucketing có hợp đồng, chưa phải kết luận thử nghiệm

| Thuộc tính | Giá trị |
|---|---|
| Repo / SHA / license | [open-feature/flagd](https://github.com/open-feature/flagd), `902555686f8bb1a89fe40c4b532e78c4e098110d`, Apache-2.0 |
| Kiểm chứng 2026-11-04 | `code-read`: evaluator JSON/fractional, LICENSE/README và `build.yaml`; chưa chạy daemon/provider hoặc kiểm tương đương SDK |
| Cơ chế đã đọc | `fractional.go` phân biệt explicit hashing input với nhánh implicit; nhánh implicit dùng `[flagKey, targetingKey]`, từ chối missing/null/non-string/empty `targetingKey`. Do đó không ghi "mọi rollout đều bắt buộc targetingKey": input explicit là đường khác. |
| CI | `build.yaml` chạy `make test` và có lane FIPS; không suy nhãn FIPS trong workflow thành chứng nhận hệ triển khai hoặc mọi bản phân phối. |
| Tích hợp | Ghim daemon/provider/schema/flag version và context; lập fixture assignment cho cùng subject qua client/server, login, restart, đổi rule. Định nghĩa fallback khi mất nguồn hoặc lỗi evaluation; ghi reason/error cùng exposure, không chỉ giá trị boolean. |
| Giới hạn | Percentage rollout không tự là randomization đúng ở cấp account/team; thay key hoặc rule có thể đổi tập nhận. Cần phân tích thống kê và pipeline exposure riêng. Không dùng feature flag làm cổng quyền truy cập dữ liệu. |

**Hợp đồng từ khám phá đến phát hành:**

1. Chọn một tác vụ khách hàng và quyết định cụ thể: tỷ lệ hoàn thành được chấp nhận, thời gian/chi phí tới đầu ra, defect escape/rework; giữ cả phân khúc và guardrail. Với xưởng nội bộ, số dòng code/PR/agent chạy là activity, không tự là giá trị.
2. Trước xây lớn, phỏng vấn/quan sát hoặc prototype theo §1–§3; đối chiếu lựa chọn nhỏ, quy trình thủ công và baseline hiện có. Nếu traffic thấp hoặc đơn vị là cả khách hàng, ưu tiên usability/cohort có giới hạn thay vì A/B thiếu lực.
3. Đóng băng metric contract: numerator/denominator, window, assignment unit, consent, exposure, query/version, exclusion và phương pháp dừng. Chi phí/tác vụ đạt cần tính cả sửa tay/review/retry, không chỉ tiền token của lần gọi thành công.
4. Trước rollout, chạy fixture event, A/A và SRM theo phương pháp đã chọn; kiểm dữ liệu trùng/thiếu, context thay sau login, cross-tenant leakage và fallback. Một evaluation thành công nhưng chưa có exposure hợp lệ không được tính vào mẫu đã thấy treatment.
5. Phát hành theo flag với owner/expiry, guardrail latency/crash/chi phí và kill switch diễn tập; kết nối [32](../32-platform-delivery-engineering/README.md) và [33](../33-reliability-observability-operations/README.md). Hết thời hạn phải có quyết định giữ/bỏ/đo thêm và dọn flag theo quy trình.
6. Báo effect size/khoảng bất định theo phân khúc, tác động guardrail, mẫu bị loại và chi phí trên đầu ra được chấp nhận. Không kết luận "không khác" khi phép thử thiếu lực; không dùng traffic bên trong xưởng thay người dùng đích.

**Đã đổi so với đợt trước:** bổ sung lớp provider/daemon và kiểm assignment, tách nó khỏi exposure/experiment engine; đưa outcome economics vào nghiệm thu phần mềm. **Nguồn §5:** [README.md](https://github.com/open-feature/flagd/blob/902555686f8bb1a89fe40c4b532e78c4e098110d/README.md) · [LICENSE](https://github.com/open-feature/flagd/blob/902555686f8bb1a89fe40c4b532e78c4e098110d/LICENSE) · [core/pkg/evaluator/fractional.go](https://github.com/open-feature/flagd/blob/902555686f8bb1a89fe40c4b532e78c4e098110d/core/pkg/evaluator/fractional.go) · [core/pkg/evaluator/json.go](https://github.com/open-feature/flagd/blob/902555686f8bb1a89fe40c4b532e78c4e098110d/core/pkg/evaluator/json.go) · [.github/workflows/build.yaml](https://github.com/open-feature/flagd/blob/902555686f8bb1a89fe40c4b532e78c4e098110d/.github/workflows/build.yaml); phương pháp nghiên cứu/SRM tiếp tục dùng nguồn gốc đã dẫn ở §3.

<a id="anhkysuai-2026-11-23"></a>

## Đánh giá từ kho Anh Kỹ Sư AI — 23/11/2026

Phần này có **4 hồ sơ hoặc phạm vi đối chiếu** từ [nguồn tuyển chọn](https://anhkysuai.com/kho/). [Bảng đủ 1.295 repo](../data/collections/anhkysuai-kho.json) ghi trạng thái đối chiếu từng link; [danh sách URL](../data/collections/anhkysuai-kho-links.txt) phục vụ tra cứu. Nguồn tuyển chọn giúp phát hiện repo; đánh giá bên dưới dựa trên clone và permalink upstream cùng metadata GitHub ngày 2026-11-23.

Mức `docs-read`/`code-read` chỉ áp dụng phạm vi ghi tại mỗi hồ sơ. Chưa cài, build, chạy test hay benchmark mã upstream. Giấy phép có thể tách theo code, model, nội dung, asset hoặc bản enterprise; con số/tuyên bố của tác giả chưa được tái lập nếu không có ghi chú khác.

<a id="anhkysuai-2026-11-23-umami"></a>

### Umami

**Repo:** [umami-software/umami](https://github.com/umami-software/umami) · **License:** MIT · **★ 40,308 (GitHub API, 2026-11-23)**

**Mục đích:** Nền tảng web/product analytics có thể tự host.

**Giá trị và cơ chế:** Tài liệu cài đặt dùng Node.js, PostgreSQL và APP_SECRET; build tạo schema và tài khoản ban đầu, phù hợp tham khảo kiến trúc analytics nằm trong hạ tầng sản phẩm.

**Giới hạn:** Chưa kiểm payload tracker, recorder hoặc chính sách lưu dữ liệu. README yêu cầu đổi mật khẩu tài khoản ban đầu; CI đặt SKIP_DB_CHECK nên build pass không tự chứng minh kết nối dữ liệu thực tế.

**Cách tham khảo/tích hợp:** Thiết lập secret riêng, giới hạn quyền DB và xác định rõ sự kiện nào được thu thập trước khi gắn tracker.

**Thay thế:** plausible, [PostHog](../28-product-discovery-experimentation/README.md#posthog), matomo.

**Bằng chứng:** `docs-read`, ngày 2026-11-23, commit [`aad2c4cedd5c`](https://github.com/umami-software/umami/commit/aad2c4cedd5c0b3bc4d361843830a0bb47cf79c4). README và các tài liệu/manifest/CI hiện diện, đọc chọn lọc; chưa kiểm implementation. Chưa cài/chạy upstream.

**Nguồn:** [README.md](https://github.com/umami-software/umami/blob/aad2c4cedd5c0b3bc4d361843830a0bb47cf79c4/README.md) · [LICENSE](https://github.com/umami-software/umami/blob/aad2c4cedd5c0b3bc4d361843830a0bb47cf79c4/LICENSE) · [metadata GitHub](https://api.github.com/repos/umami-software/umami).

<a id="anhkysuai-2026-11-23-plausible-analytics"></a>

### Plausible Analytics

**Repo:** [plausible/analytics](https://github.com/plausible/analytics) · **License:** AGPL-3.0 · **★ 29,915 (GitHub API, 2026-11-23)**

**Mục đích:** Phân tích truy cập website với dashboard và bản Community tự lưu trữ.

**Giá trị và cơ chế:** README nhấn mạnh tracker tối giản, sự kiện và báo cáo dễ vận hành; đáng tham khảo thiết kế analytics tập trung chỉ số thiết yếu.

**Giới hạn:** Mô tả không cookie và tuân thủ riêng tư là tuyên bố upstream, chưa kiểm tra lưu lượng hay cơ sở pháp lý. Cloud và Community có phạm vi tính năng riêng; cần vận hành kho dữ liệu.

**Cách tham khảo/tích hợp:** Xác định sự kiện cần đo, kiểm dữ liệu thực gửi đi và lưu lượng trước thay hệ analytics hiện có.

**Thay thế:** [Umami](../28-product-discovery-experimentation/README.md#anhkysuai-2026-11-23-umami), [PostHog](../28-product-discovery-experimentation/README.md#posthog), matomo.

**Bằng chứng:** `docs-read`, ngày 2026-11-23, commit [`418da46de5e0`](https://github.com/plausible/analytics/commit/418da46de5e09c6b1113772d1f15d375527130b3). README và các tài liệu/manifest/CI hiện diện, đọc chọn lọc; chưa kiểm implementation. Chưa cài/chạy upstream.

**Nguồn:** [README.md](https://github.com/plausible/analytics/blob/418da46de5e09c6b1113772d1f15d375527130b3/README.md) · [LICENSE.md](https://github.com/plausible/analytics/blob/418da46de5e09c6b1113772d1f15d375527130b3/LICENSE.md) · [metadata GitHub](https://api.github.com/repos/plausible/analytics).

<a id="anhkysuai-makeplane-plane"></a>

### Plane

**Repo:** [makeplane/plane](https://github.com/makeplane/plane) · **License:** AGPL-3.0-only · **Kiểm:** 2026-11-23, `docs-read`, [`57a876da1d83`](https://github.com/makeplane/plane/tree/57a876da1d83ce3309543464325a44e90b2f5c96) (commit 2026-11-23). **Sao:** 63,008 tại 2026-11-23 theo [GitHub API](https://api.github.com/repos/makeplane/plane).

| Mục | Đánh giá |
|---|---|
| Mục đích | Công cụ quản lý công việc, chu kỳ phát triển, module, trang ghi chú và lộ trình sản phẩm. |
| Giá trị và cơ chế theo tài liệu | README trình bày cách nối work item, cycles và views; monorepo có cổng lint/typecheck và workflow build Community Edition. |
| Giới hạn | Tính năng phân tích và AI trong trang là tuyên bố tài liệu, chưa chạy kiểm. Tự host còn cần quản lý dữ liệu, tệp tải lên và nâng cấp; AGPL áp dụng cho mã trong phạm vi đã đọc. |
| Điều kiện tích hợp | Dùng môi trường thử theo Docker hoặc Kubernetes được tài liệu chỉ dẫn; kiểm migration, phân quyền và xuất dữ liệu trước khi đưa công việc thật vào. |
| Lựa chọn đối chiếu | OpenProject; Taiga; Huly. |

**Phạm vi bằng chứng:** đã clone, đọc trích đoạn tài liệu, giấy phép và các file cấu hình được dẫn dưới đây; chưa chạy mã, build, benchmark hoặc test upstream. `docs-read` không phải kiểm chứng implementation.

**Nguồn tại cùng SHA:** [README.md](https://github.com/makeplane/plane/blob/57a876da1d83ce3309543464325a44e90b2f5c96/README.md) · [COPYRIGHT.txt](https://github.com/makeplane/plane/blob/57a876da1d83ce3309543464325a44e90b2f5c96/COPYRIGHT.txt) · [COPYRIGHT_CHECK.md](https://github.com/makeplane/plane/blob/57a876da1d83ce3309543464325a44e90b2f5c96/COPYRIGHT_CHECK.md) · [LICENSE.txt](https://github.com/makeplane/plane/blob/57a876da1d83ce3309543464325a44e90b2f5c96/LICENSE.txt) · [package.json](https://github.com/makeplane/plane/blob/57a876da1d83ce3309543464325a44e90b2f5c96/package.json) · [.github/workflows/build-branch.yml](https://github.com/makeplane/plane/blob/57a876da1d83ce3309543464325a44e90b2f5c96/.github/workflows/build-branch.yml).

<a id="anhkysuai-dubinc-dub.link"></a>

### Dub Links

**Repo:** [dubinc/dub.link](https://github.com/dubinc/dub.link) · **License:** AGPL-3.0; thư mục ee theo giấy phép riêng · **Kiểm:** 2026-11-23, `docs-read`, [`6b463b4bdd9e`](https://github.com/dubinc/dub.link/tree/6b463b4bdd9ed2fd9aa416f67b5b77d317b1471e) (commit 2026-10-26). **Sao:** 25,217 tại 2026-11-23 theo [GitHub API](https://api.github.com/repos/dubinc/dub.link).

| Mục | Đánh giá |
|---|---|
| Mục đích | Nền tảng link ngắn, attribution và theo dõi chuyển đổi. |
| Giá trị và cơ chế theo tài liệu | README liệt kê Next.js/Prisma, Redis/analytics/database và nhiều dịch vụ ngoài; CI có public API tests, hữu ích để xem cấu trúc tích hợp tăng trưởng sản phẩm. |
| Giới hạn | LICENSE tách hai nhánh thư mục ee; không gắn AGPL cho toàn monorepo. Số click trong mô tả không được đo lại; self-host còn phụ thuộc cấu hình dịch vụ/credentials. |
| Điều kiện tích hợp | Thử domain/link và event conversion trên dữ liệu giả, kiểm privacy/retention và chống lạm dụng redirect; đối chiếu CE/EE và chi phí backend trước triển khai. |
| Lựa chọn đối chiếu | Shlink; YOURLS; Kutt. |

**Phạm vi bằng chứng:** đã clone, đọc trích đoạn tài liệu, giấy phép và các file cấu hình được dẫn dưới đây; chưa chạy mã, build, benchmark hoặc test upstream. `docs-read` không phải kiểm chứng implementation.

**Nguồn tại cùng SHA:** [README.md](https://github.com/dubinc/dub.link/blob/6b463b4bdd9ed2fd9aa416f67b5b77d317b1471e/README.md) · [LICENSE.md](https://github.com/dubinc/dub.link/blob/6b463b4bdd9ed2fd9aa416f67b5b77d317b1471e/LICENSE.md) · [package.json](https://github.com/dubinc/dub.link/blob/6b463b4bdd9ed2fd9aa416f67b5b77d317b1471e/package.json) · [.github/workflows/e2e.yaml](https://github.com/dubinc/dub.link/blob/6b463b4bdd9ed2fd9aa416f67b5b77d317b1471e/.github/workflows/e2e.yaml).

## Nguồn

Các permalink trong từng hồ sơ cố định đúng phiên bản đã đọc; số sao/trạng thái archive là snapshot GitHub API ngày 2026-11-02. Không chạy mã, huấn luyện model hoặc tái lập kết quả của upstream.

<a id="nt-2026-11-23"></a>

## Nâng trần theo khoảng trống — 23/11/2026

Phần này có các hồ sơ mới của đợt nâng trần: mười trinh sát tìm trên internet và GitHub những mảng mà chuyên mục còn thiếu hoặc chỉ có hồ sơ cũ, rồi mỗi repo được clone nông tại một commit cố định, đọc LICENSE, README, ít nhất một file triển khai thật và CI nếu có; không cài hay chạy mã upstream. Mô tả của trinh sát nhiều chỗ sai so với mã thật, và các chỗ đó được sửa ngay trong từng hồ sơ. Số sao lấy sau bằng GitHub search API nên có thể để trống.

<a id="nt-go-feature-flag"></a>

### GO Feature Flag

| Thuộc tính | Giá trị |
|---|---|
| Repo | https://github.com/thomaspoignant/go-feature-flag |
| License | MIT |
| Phiên bản đã đọc | `df297b611c6e816a8f4ae88d4c2eb100bd8f728a` (commit 2026-11-23) |
| Kiểm chứng | 2026-11-23; code-read; đã đọc LICENSE, README.md, modules/core/utils/hash.go, modules/core/flag/internal_flag.go, modules/core/flag/rule.go; chưa chạy upstream |
| Khoảng trống lấp | Feature flag an toàn: chuẩn OpenFeature và cấu hình theo ngữ cảnh |
| Cơ chế đáng học | - `modules/core/utils/hash.go`: `BuildHash` = FNV-1a(tên cờ + bucketing key) chia dư theo `maxPercentage`, nên cùng người dùng luôn rơi vào cùng nhóm và không cấp phát chuỗi.<br>- `modules/core/flag/internal_flag.go`: `selectVariation` duyệt các rule theo thứ tự, rule đầu khớp thắng, sau đó đến default rule; lỗi `errRuleNotApply` thì sang rule kế; kết quả có cờ `cacheable`.<br>- `rule.go`: progressive rollout và percentage dùng cùng hàm băm; `BucketingKey` tùy chỉnh được.<br>- Retriever, exporter và notifier là các gói thay thế được (`retriever/`, `exporter/`, `notifier/`). |
| Tiêu chí và cách kiểm | CI `ci.yml` chạy build, lint, `make test`, coverage, benchmark, kiểm swagger sinh lại, `make vuln-check-relayproxy`, build WASM và `make provider-tests` (dựng 2 relay proxy rồi chạy test tích hợp provider các ngôn ngữ). Có fuzz test cho `InternalFlag`. Kiểm bằng máy; chưa chạy. |
| Giới hạn và rủi ro | MIT (LICENSE; examples/demo cũng MIT). Dữ liệu rời máy chỉ khi cấu hình exporter/notifier (S3, Kafka, webhook, Slack); bật xuất dữ liệu đánh giá cần cân nhắc dữ liệu người dùng trong evaluation context. Relay proxy mặc định cần cấu hình API key để không mở. Một maintainer chính (chưa xác minh số liệu đóng góp). |
| So với | Unleash (server có UI, mục 28), flagd (provider OpenFeature gọn), OpenFeature spec (chuẩn, hồ sơ đợt này) |
| Nguồn | [LICENSE](https://github.com/thomaspoignant/go-feature-flag/blob/df297b611c6e816a8f4ae88d4c2eb100bd8f728a/LICENSE) · [README.md](https://github.com/thomaspoignant/go-feature-flag/blob/df297b611c6e816a8f4ae88d4c2eb100bd8f728a/README.md) · [hash.go](https://github.com/thomaspoignant/go-feature-flag/blob/df297b611c6e816a8f4ae88d4c2eb100bd8f728a/modules/core/utils/hash.go) · [internal_flag.go](https://github.com/thomaspoignant/go-feature-flag/blob/df297b611c6e816a8f4ae88d4c2eb100bd8f728a/modules/core/flag/internal_flag.go) · [rule.go](https://github.com/thomaspoignant/go-feature-flag/blob/df297b611c6e816a8f4ae88d4c2eb100bd8f728a/modules/core/flag/rule.go) · [integration_tests.sh](https://github.com/thomaspoignant/go-feature-flag/blob/df297b611c6e816a8f4ae88d4c2eb100bd8f728a/openfeature/provider_tests/integration_tests.sh) · [ci.yml](https://github.com/thomaspoignant/go-feature-flag/blob/df297b611c6e816a8f4ae88d4c2eb100bd8f728a/.github/workflows/ci.yml) |

<a id="nt-openfeature-spec"></a>

### OpenFeature Specification

| Thuộc tính | Giá trị |
|---|---|
| Repo | https://github.com/open-feature/spec |
| License | Apache-2.0 |
| Phiên bản đã đọc | `b489ba9134ee081cecaf18a28b544ddabc1b25f7` (commit 2026-11-15) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc LICENSE, README.md, version.txt, specification/sections/02-providers.md, specification/assets/provider-tck/README.md; chưa chạy upstream |
| Khoảng trống lấp | Feature flag an toàn: chuẩn OpenFeature và cấu hình theo ngữ cảnh |
| Cơ chế đáng học | - Yêu cầu đánh số (ví dụ 2.1.1) trong `specification/sections/01..06-*.md`; `tools/specification_parser` sinh `specification.json` và CI kiểm JSON được sinh lại cùng lint từ khóa RFC 2119 (`pr-checks.yaml`).<br>- `specification/assets/provider-tck/`: 6 file gherkin (evaluation, errors, events, lifecycle, metadata, reason), `flags/canonical-flags.json`, `openapi/control-api.yaml` phải đi cùng nhau; flag mẫu thiết kế để bắt lỗi (giá trị falsy, `missing-flag` phải vắng, số nguyên 2^53-1).<br>- Cơ chế khả năng: thẻ như `@events`, `@stale`, `@targeting`; provider khai báo thẻ hỗ trợ, scenario chưa khai báo bị báo skipped kèm lý do, không bao giờ pass.<br>- Mô-đun Go `provider-tck` chỉ nhúng các artifact bằng `embed.FS`. |
| Tiêu chí và cách kiểm | Kiểm bằng máy ở hai tầng: spec (parser + lint + ToC trong CI) và provider (gherkin chạy bằng suite ở repo khác, ví dụ test provider của go-feature-flag). Repo này tự nó không có runner TCK, nên không tự kiểm provider nào. Chưa chạy. |
| Giới hạn và rủi ro | Apache-2.0. Đây là đặc tả, không phải triển khai: SDK không tự đánh giá cờ (README). TCK ghi rõ là thử nghiệm, tập scenario là tập con đại diện, từ vựng có thể đổi, và việc không khai báo một thẻ không phải vi phạm đặc tả. Mô tả trinh sát đúng về 0.1.0 ngày 2026-10-16 nhưng làm TCK nghe như đã hoàn chỉnh. |
| So với | flagd (triển khai tham chiếu, mục 28), Unleash, GO Feature Flag (provider OpenFeature, hồ sơ đợt này) |
| Nguồn | [LICENSE](https://github.com/open-feature/spec/blob/b489ba9134ee081cecaf18a28b544ddabc1b25f7/LICENSE) · [README.md](https://github.com/open-feature/spec/blob/b489ba9134ee081cecaf18a28b544ddabc1b25f7/README.md) · [version.txt](https://github.com/open-feature/spec/blob/b489ba9134ee081cecaf18a28b544ddabc1b25f7/version.txt) · [02-providers.md](https://github.com/open-feature/spec/blob/b489ba9134ee081cecaf18a28b544ddabc1b25f7/specification/sections/02-providers.md) · [README.md](https://github.com/open-feature/spec/blob/b489ba9134ee081cecaf18a28b544ddabc1b25f7/specification/assets/provider-tck/README.md) · [evaluation.feature](https://github.com/open-feature/spec/blob/b489ba9134ee081cecaf18a28b544ddabc1b25f7/specification/assets/provider-tck/gherkin/evaluation.feature) · [CHANGELOG.md](https://github.com/open-feature/spec/blob/b489ba9134ee081cecaf18a28b544ddabc1b25f7/specification/assets/provider-tck/CHANGELOG.md) · [pr-checks.yaml](https://github.com/open-feature/spec/blob/b489ba9134ee081cecaf18a28b544ddabc1b25f7/.github/workflows/pr-checks.yaml) |
