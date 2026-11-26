# 38. Chất lượng và sản xuất công nghiệp

Mục lập ngày 23/11/2026 cho nhà máy chế tạo thiết bị áp lực và bình chứa khí (chai LPG, chai khí công nghiệp, bình amoniac) và các xưởng sản xuất vừa và nhỏ: hệ thống quản lý chất lượng ISO 9001/14001/45001 (đánh giá nội bộ, CAPA, rủi ro, mục tiêu), kiểm soát quá trình thống kê, quản lý quy trình hàn và chứng chỉ, kiểm tra không phá hủy, hiệu chuẩn, truy xuất nguồn gốc theo lô và serial, MES/ERP nhẹ và bảo trì thiết bị.

Mục này được tạo vì kho trước đó gần như không có công cụ nào cho mảng này (chỉ có ERP và quản lý tài liệu chung). **Lưu ý về giới hạn:** các chuẩn ISO và ASME bán có phí nên mọi nhận định ở cấp điều khoản chỉ dựa trên tóm tắt công khai và ghi "(chưa xác minh điều khoản)"; trạng thái hiệu lực của chuẩn cần kiểm trên trang chính thức của tổ chức ban hành trước khi dựa vào. Một số mảng (quy trình hàn WPS/PQR, hiệu chuẩn thiết bị đo, kiểm tra không phá hủy) chưa tìm được công cụ mã mở đạt chất lượng: đó là khoảng trống cần tự xây hoặc mua, không phải thiếu sót của việc tìm kiếm.

Bảng tổng hợp theo danh mục con: [catalog/engineering/](../catalog/README.md).

<a id="nt-2026-11-23"></a>

## Nâng trần theo khoảng trống — 23/11/2026

Phần này có các hồ sơ mới của đợt nâng trần: mười trinh sát tìm trên internet và GitHub những mảng mà chuyên mục còn thiếu hoặc chỉ có hồ sơ cũ, rồi mỗi repo được clone nông tại một commit cố định, đọc LICENSE, README, ít nhất một file triển khai thật và CI nếu có; không cài hay chạy mã upstream. Mô tả của trinh sát nhiều chỗ sai so với mã thật, và các chỗ đó được sửa ngay trong từng hồ sơ. Số sao lấy sau bằng GitHub search API nên có thể để trống.

<a id="nt-crbnos-carbon"></a>

### Carbon (crbnos)

| Thuộc tính | Giá trị |
|---|---|
| Repo | https://github.com/crbnos/carbon |
| License | AGPL-3.0-only cho phần lõi; thư mục `packages/ee` và mọi file có ".ee." trong tên theo Carbon Commercial License (chạy, thử, sửa đều cần giấy phép thương mại); MIT cho `packages/form`, Apache-2.0 cho Gantt. Tên và logo Carbon không được dùng. Trinh sát ghi NOASSERTION vì GitHub không gộp được các tầng này |
| Phiên bản đã đọc | `e128c2082eb0485f9762fb316f851ec45d059fb0` (commit 2026-11-23) |
| Kiểm chứng | 2026-11-23; code-read; đã đọc README, LICENSE các tầng, mô hình và dịch vụ quality, bảng lấy mẫu, mẫu quy trình, workflow check.yml; chưa chạy upstream |
| Khoảng trống lấp | MES/ERP mã mở cho xưởng vừa và nhỏ, có QMS tích hợp (không phải module rời) |
| Cơ chế đáng học | - Mô hình nonconformance trong `quality.models.ts`: trạng thái Registered, In Progress, Closed; yêu cầu phê duyệt MRB; nguồn Internal hoặc External; liên kết tới dòng PO, lô nhận, job operation, thực thể truy vết, phiếu kiểm.<br>- Quyết định xử lý lô kiểm (Accept, Reject, Partial) trong `packages/database/src/quality-disposition.ts`: Reject coi cả lô không phù hợp (chú thích dẫn ISO 9001:2015 mục 8.7), từ chối Partial khi chưa lấy mẫu đủ hoặc không mẫu nào đạt, kèm các bước lật trạng thái đơn vị và ghi hủy.<br>- `samplingStandards.ts` là hàm thuần: mã chữ theo cỡ lô và mức kiểm (S1 đến S4, I đến III), mức AQL chuẩn, mức độ Normal/Tightened/Reduced, cho ANSI Z1.4 và ISO 2859-1; có `samplingStandards.test.ts`.<br>- Dụng cụ đo có trạng thái Pending, In-Calibration, Out-of-Calibration; bộ chọn dụng cụ ở màn kiểm MES gắn nhãn Out-of-Calibration (đã đọc phần hiển thị, chưa thấy đoạn chặn cứng trong phần đã mở).<br>- `quality-document-templates.ts` chứa bộ mẫu quy trình QMS (Control of Documents, Internal Auditing, Control of NCP, Corrective and Preventive Action, Calibration Procedure, Risk and Opportunity Management...) viết theo AS9100D. |
| Tiêu chí và cách kiểm | Chuẩn nhắm tới: AS9100D (thư viện mẫu quy trình trong `quality-document-templates.ts`) và ISO 9001:2015 mục 8.7 (xử lý đầu ra không phù hợp); lấy mẫu theo ISO 2859-1/ANSI Z1.4. Không thấy IATF 16949 (grep thư viện mẫu cho 0 kết quả) và không thấy chức năng cho ISO 14001/45001. Hỗ trợ quy trình là có thật cho NCR, kiểm nhập, hiệu chuẩn, rủi ro, truy vết; nhưng không có ánh xạ điều khoản tự động, không có tuyên bố chứng nhận. Máy kiểm: CI `check.yml` chạy biome, kiểm conformance, lingui, vitest (đã mở workflow); chưa chạy. |
| Giới hạn và rủi ro | Open-core: file ee cấm chạy khi chưa có giấy phép, API key và MCP khi tự host cần giấy phép thương mại (README). Tuyên bố "Hard tech unicorns build on Carbon" và các so sánh với NetSuite/SAP là marketing **(chưa xác minh)**. Stack nặng (Supabase, Postgres RLS, Rust crates, SST); PostHog, Stripe, email, AI là tùy chọn qua `.env`. Mẫu quy trình AS9100D là văn bản mẫu, tổ chức phải tự rà trước khi dùng cho đánh giá chứng nhận. Chuẩn ISO trả phí nên mọi nhận định ở cấp điều khoản chưa xác minh điều khoản. |
| So với | Odoo Community (`odoo-odoo`) và ERPNext (`frappe-erpnext`) là ERP tổng quát có module chất lượng/sản xuất; Carbon hẹp hơn nhưng sát xưởng chế tạo (traveler, FAI, MRB). Cùng đợt: OpenMES (MES nhẹ, chưa có hồ sơ trong kho). |
| Nguồn | [README](https://github.com/crbnos/carbon/blob/e128c2082eb0485f9762fb316f851ec45d059fb0/README.md) · [LICENSE](https://github.com/crbnos/carbon/blob/e128c2082eb0485f9762fb316f851ec45d059fb0/LICENSE) · [ee/LICENSE](https://github.com/crbnos/carbon/blob/e128c2082eb0485f9762fb316f851ec45d059fb0/packages/ee/LICENSE) · [quality.models](https://github.com/crbnos/carbon/blob/e128c2082eb0485f9762fb316f851ec45d059fb0/apps/erp/app/modules/quality/quality.models.ts) · [samplingStandards](https://github.com/crbnos/carbon/blob/e128c2082eb0485f9762fb316f851ec45d059fb0/apps/erp/app/modules/quality/samplingStandards.ts) · [sampling test](https://github.com/crbnos/carbon/blob/e128c2082eb0485f9762fb316f851ec45d059fb0/apps/erp/app/modules/quality/samplingStandards.test.ts) · [quality-disposition](https://github.com/crbnos/carbon/blob/e128c2082eb0485f9762fb316f851ec45d059fb0/packages/database/src/quality-disposition.ts) · [mẫu quy trình](https://github.com/crbnos/carbon/blob/e128c2082eb0485f9762fb316f851ec45d059fb0/apps/erp/app/modules/quality/quality-document-templates.ts) · [gauge picker](https://github.com/crbnos/carbon/blob/e128c2082eb0485f9762fb316f851ec45d059fb0/apps/mes/app/components/Inspection/InspectionGaugePicker.tsx) · [check.yml](https://github.com/crbnos/carbon/blob/e128c2082eb0485f9762fb316f851ec45d059fb0/.github/workflows/check.yml) |

<a id="nt-mes-open-openmes"></a>

### OpenMES

| Thuộc tính | Giá trị |
|---|---|
| Repo | https://github.com/Mes-Open/OpenMes |
| License | AGPL-3.0 cho lõi; AFL-3.0 cho `modules/` (chỉ file mang dòng "Licensed under the Academic Free License version 3.0"; thư mục này được ghi là đã lỗi thời); bản thương mại song song nhờ CLA |
| Phiên bản đã đọc | `faccc52a543382922aa8b7d9d79b89e6a30b28d3` (commit 2026-11-19) |
| Kiểm chứng | 2026-11-23; code-read; đã đọc README, LICENSE, LICENSING.md, docs/telemetry.md, AuditLog.php, migration audit_logs, QualityCheck.php, IssueActionService.php, LotWhereUsedService.php, tests.yml; chưa chạy upstream |
| Khoảng trống lấp | MES/ERP mã mở nhẹ cho xưởng vừa và nhỏ |
| Cơ chế đáng học | - `AuditLog.php` ghi trước/sau trạng thái, người dùng, IP; sự kiện `updating` và `deleting` của Eloquent ném lỗi để cấm sửa/xóa bản ghi.<br>- `IssueActionService.php`: hành động khắc phục/phòng ngừa gắn vào Issue với vòng đời OPEN, IN_PROGRESS, DONE, VERIFIED; đóng Issue bị chặn cho đến khi mọi hành động được VERIFIED (theo chú thích mã, chưa mở `IssueService`).<br>- `LotWhereUsedService.php`: tra ngược lô nguyên liệu sang đơn vị serial, báo rõ độ chính xác (unit, batch hoặc none) thay vì giả định chính xác.<br>- Mô hình QualityCheck, QualityCheckSample, QualityCheckTemplate cho kiểm theo mẫu trên lô và pallet; usage reporting có tài liệu ranh giới và test (`TelemetryPayloadTest`) theo docs. |
| Tiêu chí và cách kiểm | Chuẩn nhắm tới: README tuyên bố "ISO 9001, AS9100 compatible audit trail" và "OWASP Top 10 compliant" (chưa xác minh). Trong mã chỉ thấy nhật ký thay đổi, Issue với hành động khắc phục, kiểm theo mẫu và truy vết; không thấy ánh xạ điều khoản ISO 9001/AS9100, không IATF 16949, không ISO 14001. Tức là gọi tên chuẩn ở mức tương thích dấu vết, chưa phải bộ quy trình QMS. CI `tests.yml` chạy `npm test` và `php artisan test --stop-on-failure` (đã mở workflow); chưa chạy. |
| Giới hạn và rủi ro | Tuyên bố "Immutable audit logs - PostgreSQL-enforced" không khớp mã: migration `create_audit_logs_table` không có trigger hay REVOKE, grep toàn thư mục database không thấy trigger nào cho bảng này; tính bất biến chỉ nằm ở model Eloquent nên truy vấn thô hoặc quản trị CSDL vẫn sửa được. Usage reporting bật mặc định khi cài mới (tắt bằng `OPENMES_TELEMETRY=false` hoặc `--no-telemetry`); tài liệu nói chỉ gửi phiên bản, tính năng bật, dải kích thước, lớp lỗi và vị trí, không gửi dữ liệu nhập; chưa xác minh bằng chạy. AGPL mục 13 áp cho bản sửa chạy qua mạng. Cần CLA để đóng góp. |
| So với | Carbon (`crbnos-carbon`, cùng đợt) rộng hơn và có QMS sâu hơn nhưng open-core; ERPNext (`frappe-erpnext`) và Odoo Community (`odoo-odoo`) là ERP tổng quát có module sản xuất. |
| Nguồn | [README](https://github.com/Mes-Open/OpenMes/blob/faccc52a543382922aa8b7d9d79b89e6a30b28d3/README.md) · [LICENSE](https://github.com/Mes-Open/OpenMes/blob/faccc52a543382922aa8b7d9d79b89e6a30b28d3/LICENSE) · [LICENSING](https://github.com/Mes-Open/OpenMes/blob/faccc52a543382922aa8b7d9d79b89e6a30b28d3/LICENSING.md) · [telemetry](https://github.com/Mes-Open/OpenMes/blob/faccc52a543382922aa8b7d9d79b89e6a30b28d3/docs/telemetry.md) · [AuditLog](https://github.com/Mes-Open/OpenMes/blob/faccc52a543382922aa8b7d9d79b89e6a30b28d3/backend/app/Models/AuditLog.php) · [migration audit_logs](https://github.com/Mes-Open/OpenMes/blob/faccc52a543382922aa8b7d9d79b89e6a30b28d3/backend/database/migrations/2026_02_16_210143_create_audit_logs_table.php) · [QualityCheck](https://github.com/Mes-Open/OpenMes/blob/faccc52a543382922aa8b7d9d79b89e6a30b28d3/backend/app/Models/QualityCheck.php) · [IssueActionService](https://github.com/Mes-Open/OpenMes/blob/faccc52a543382922aa8b7d9d79b89e6a30b28d3/backend/app/Services/Quality/IssueActionService.php) · [LotWhereUsedService](https://github.com/Mes-Open/OpenMes/blob/faccc52a543382922aa8b7d9d79b89e6a30b28d3/backend/app/Services/Traceability/LotWhereUsedService.php) · [tests.yml](https://github.com/Mes-Open/OpenMes/blob/faccc52a543382922aa8b7d9d79b89e6a30b28d3/.github/workflows/tests.yml) |

<a id="nt-aus-doh-powerbi-spc"></a>

### PowerBI-SPC (WA Health)

| Thuộc tính | Giá trị |
|---|---|
| Repo | https://github.com/AUS-DOH-Safety-and-Quality/PowerBI-SPC |
| License | GPL-3.0 (LICENSE.md đã mở); `EULA.pdf` là điều khoản chuẩn Power BI custom visual cho bản tải từ Office Store, nêu việc truyền thông tin thiết bị cho dịch vụ Internet của nền tảng |
| Phiên bản đã đọc | `b821ee8b843277d9174877bc1aba37ef90885320` (commit 2026-11-12) |
| Kiểm chứng | 2026-11-23; code-read; đã đọc README, LICENSE.md, privacy-policy.md, package.json, pbiviz.json, `Limit Calculations/i.ts`, `Settings Model/outliersSettings.ts`, test_visual.yml; chưa chạy upstream |
| Khoảng trống lấp | SPC (kiểm soát quá trình thống kê); không có Cp/Cpk |
| Cơ chế đáng học | - `src/Limit Calculations/*.ts` mỗi loại biểu đồ một file; `i.ts` lấy đường tâm là trung bình, sigma bằng trung bình khoảng di động chia 1.128 và có tùy chọn bỏ điểm ngoại lai khi tính giới hạn.<br>- `outliersSettings.ts`: shift (mặc định 7 điểm, điểm nằm đúng đường tâm không đếm cũng không ngắt), trend, hai trên ba điểm vượt giới hạn cảnh báo, điểm thiên văn; từng quy tắc tắt theo mặc định.<br>- Biểu tượng kết luận kiểu NHS (cải thiện, suy giảm, biến thiên chung) từ `Outlier Flagging/variationIconsToDraw.ts` (chỉ đọc tên file); cho phép tái lập đường giới hạn theo mốc (docs/RebaselineLimits.md, chưa mở). |
| Tiêu chí và cách kiểm | Chuẩn nhắm tới: không viện dẫn ISO 9001 hay IATF 16949; biểu tượng kết luận lấy kiểu NHS (tên file trong src), thư mục docs có trang PlotTheDots (chưa mở). Hỗ trợ SPC có thật cho biểu đồ kiểm soát nhưng IATF 16949 và AIAG SPC cần Cp/Cpk, MSA, không có ở đây. Máy kiểm: thư mục `test` có vitest (regressions, rebaselines, tooltips, validation...), `npm test` chạy `vitest --run`; workflow `test_visual.yml` gọi workflow tái sử dụng của repo powerbi-visuals-core (đã mở file gọi, chưa đọc workflow đích). |
| Giới hạn và rủi ro | Phụ thuộc Power BI (dữ liệu và chạy nằm trong nền tảng Microsoft); `powerbi-visuals-core` được ghim vào một fork GitHub ở commit 610c763, nên chuỗi cung ứng phụ thuộc repo khác. Chính sách riêng tư của repo nói visual không truyền dữ liệu ra ngoài Power BI, chưa xác minh bằng kiểm lưu lượng. |
| So với | pyshewhart (`huft-jonathan-pyshewhart`, cùng đợt) là thư viện Python mã MIT chạy không cần Power BI nhưng chỉ có 4 loại biểu đồ; trong kho chưa có hồ sơ SPC khác. |
| Nguồn | [README](https://github.com/AUS-DOH-Safety-and-Quality/PowerBI-SPC/blob/b821ee8b843277d9174877bc1aba37ef90885320/README.md) · [LICENSE](https://github.com/AUS-DOH-Safety-and-Quality/PowerBI-SPC/blob/b821ee8b843277d9174877bc1aba37ef90885320/LICENSE.md) · [privacy-policy](https://github.com/AUS-DOH-Safety-and-Quality/PowerBI-SPC/blob/b821ee8b843277d9174877bc1aba37ef90885320/privacy-policy.md) · [package.json](https://github.com/AUS-DOH-Safety-and-Quality/PowerBI-SPC/blob/b821ee8b843277d9174877bc1aba37ef90885320/package.json) · [pbiviz.json](https://github.com/AUS-DOH-Safety-and-Quality/PowerBI-SPC/blob/b821ee8b843277d9174877bc1aba37ef90885320/pbiviz.json) · [i.ts](https://github.com/AUS-DOH-Safety-and-Quality/PowerBI-SPC/blob/b821ee8b843277d9174877bc1aba37ef90885320/src/Limit%20Calculations/i.ts) · [outliersSettings](https://github.com/AUS-DOH-Safety-and-Quality/PowerBI-SPC/blob/b821ee8b843277d9174877bc1aba37ef90885320/src/Settings%20Model/outliersSettings.ts) · [test_visual.yml](https://github.com/AUS-DOH-Safety-and-Quality/PowerBI-SPC/blob/b821ee8b843277d9174877bc1aba37ef90885320/.github/workflows/test_visual.yml) |

<a id="nt-huft-jonathan-pyshewhart"></a>

### pyshewhart

| Thuộc tính | Giá trị |
|---|---|
| Repo | https://github.com/huft-jonathan/pyshewhart |
| License | MIT (LICENSE đã mở) |
| Phiên bản đã đọc | `3c398648548fc90a090665d8ec6b242b5d672fe7` (commit 2026-07-19) |
| Kiểm chứng | 2026-11-23; code-read; đã đọc README, LICENSE, CHANGELOG, setup.py, constants.py, control_charts.py, test_smoke.py, noxfile.py; chưa chạy upstream |
| Khoảng trống lấp | SPC và Cp/Cpk: có biểu đồ kiểm soát và luật Western Electric, không có Cp/Cpk |
| Cơ chế đáng học | - `constants.py` giữ bảng hằng số biểu đồ kiểm soát (A, A2, A3, d2, d3, D1 đến D4...) theo cỡ mẫu, trích từ Montgomery (2005), Statistical Quality Control, ấn bản 5.<br>- `control_charts.py` có lớp `XbarRControlChart`, `XbarSControlChart`, `CUSUMControlChart`, `PAttributeControlChart`; hàm `_western_electric_rules` định nghĩa ba luật hai trên ba, bốn trên năm, tám liên tiếp.<br>- Nhập từ danh sách, CSV hoặc console script; thời gian dạng datetime, timedelta, chuỗi, Unix timestamp hoặc giây. |
| Tiêu chí và cách kiểm | Chỉ có smoke test: `tests/test_smoke.py` tự nhận là không kiểm tính đúng của thống kê hay hình ảnh, chỉ kiểm không ném ngoại lệ; `noxfile.py` chạy ma trận Python 3.8 đến 3.14 với phụ thuộc cũ nhất và mới nhất (đã đọc phần đầu). Không có workflow CI trong repo. Chưa chạy. |
| Giới hạn và rủi ro | Nghi lỗi logic luật Western Electric: so sánh `len(ooti) > m` (control_charts.py) khiến luật tám liên tiếp (m=8, n=8) không thể xảy ra, hai trên ba chỉ bắt khi cả ba, bốn trên năm chỉ bắt khi cả năm; đây là kết luận từ đọc mã, cần test với dữ liệu có đáp án trước khi tin cảnh báo. Hằng số bảng chỉ tới cỡ mẫu 25 đến 27. Không có Cp/Cpk, giới hạn quy cách hay MSA nên không đáp ứng IATF 16949 hay AIAG SPC; hiển thị bằng matplotlib, không có lưu vết kiểm toán. Commit cuối 2026-07-19 (sửa tương thích matplotlib), chủ yếu một tác giả. |
| So với | PowerBI-SPC (`aus-doh-powerbi-spc`, cùng đợt) có nhiều loại biểu đồ hơn và quy tắc kiểu NHS nhưng cần Power BI; kho chưa có hồ sơ SPC khác. |
| Nguồn | [README](https://github.com/huft-jonathan/pyshewhart/blob/3c398648548fc90a090665d8ec6b242b5d672fe7/README.md) · [LICENSE](https://github.com/huft-jonathan/pyshewhart/blob/3c398648548fc90a090665d8ec6b242b5d672fe7/LICENSE) · [CHANGELOG](https://github.com/huft-jonathan/pyshewhart/blob/3c398648548fc90a090665d8ec6b242b5d672fe7/CHANGELOG.md) · [setup.py](https://github.com/huft-jonathan/pyshewhart/blob/3c398648548fc90a090665d8ec6b242b5d672fe7/setup.py) · [constants.py](https://github.com/huft-jonathan/pyshewhart/blob/3c398648548fc90a090665d8ec6b242b5d672fe7/pyshewhart/constants.py) · [control_charts.py](https://github.com/huft-jonathan/pyshewhart/blob/3c398648548fc90a090665d8ec6b242b5d672fe7/pyshewhart/control_charts.py) · [test_smoke](https://github.com/huft-jonathan/pyshewhart/blob/3c398648548fc90a090665d8ec6b242b5d672fe7/tests/test_smoke.py) · [noxfile](https://github.com/huft-jonathan/pyshewhart/blob/3c398648548fc90a090665d8ec6b242b5d672fe7/noxfile.py) |

<a id="nt-odoo-qms-iso9001"></a>

### Odoo QMS ISO 9001 (TMC Rosario)

| Thuộc tính | Giá trị |
|---|---|
| Repo | https://github.com/jonaesantos/odoo-qms-iso9001 |
| License | AGPL-3.0 |
| Phiên bản đã đọc | `2e95782d1139c96b1c6e166630ed8659cf4475b9` (commit 2021-12-15) |
| Kiểm chứng | 2026-11-23; code-read; đã đọc README.md, LICENSE, qms/`__manifest__`.py và các model audit/action/finding/effectiveness_check/hazard/goal cùng qms_groups.xml; chưa chạy upstream |
| Khoảng trống lấp | QMS ISO 9001 mã mở (đánh giá nội bộ, CAPA, rủi ro, mục tiêu): chỉ ISO 9001, không phải 14001 hay 45001 |
| Cơ chế đáng học | • Mô hình ISO 9001 theo bản ghi: qms.audit (hệ thống chọn ISO 9001:2015 hoặc 2008, dòng kiểm tra, đánh giá, đóng audit) gắn với finding, quy trình và đối tượng quan tâm (audit.py, finding.py).<br>• CAPA là qms.action có loại tức thời, khắc phục, cải tiến, phòng ngừa theo rủi ro; mỗi action có qms.effectiveness_check, ràng buộc không đóng kiểm tra nếu thiếu ngày kiểm (action.py, effectiveness_check.py).<br>• Rủi ro: ma trận xác suất x tác động 1-5, bốn mức đánh giá (1-3, 4-8, 9-14, 15-25) cùng chiến lược chấp nhận, tránh, chuyển, giảm (hazard.py).<br>• Phân quyền ba nhóm User, Manager, Read Only (qms_groups.xml); giai đoạn của finding là bản ghi cấu hình được, có kanban state (finding.py). |
| Tiêu chí và cách kiểm | Không có test, không có workflow CI, không có kiểm bằng máy nào trong repo. Ngưỡng duy nhất là bảng điểm rủi ro trong hazard.py và ràng buộc ngày kiểm hiệu lực; không có kiểm hạn hiệu chuẩn hay lịch audit tự động. |
| Giới hạn và rủi ro | Đã đọc thấy: (1) Audit.button_close ghi state done trong khi `_states_` chỉ có open và closed; (2) Hazard.`_compute_result_and_evaluation` nhân hai giá trị Selection kiểu chuỗi và không lặp qua self; (3) Goal.`_compute_last_measurement_date` và result lấy phần tử [0] không kiểm rỗng. Cả ba là đọc mã, chưa chạy. Odoo 14 đã hết vòng đời, repo không còn commit từ 2021; AGPL-3.0 buộc công bố mã khi phục vụ qua mạng; một phần mã dẫn xuất từ OCA management-system (Savoir-faire Linux), cần giữ ghi công. Không hỗ trợ ISO 14001 hay 45001; mọi liên hệ với điều khoản ISO là (chưa xác minh điều khoản). |
| So với | OpenQMS (cùng đợt: ngược lại, có logic và CI nhưng nhắm IATF 16949); FactorySemantics MES (cùng đợt); odoo-odoo trong kho (nền Odoo). |
| Nguồn | [README.md](https://github.com/jonaesantos/odoo-qms-iso9001/blob/2e95782d1139c96b1c6e166630ed8659cf4475b9/README.md) · [LICENSE](https://github.com/jonaesantos/odoo-qms-iso9001/blob/2e95782d1139c96b1c6e166630ed8659cf4475b9/LICENSE) · [\_\_manifest\_\_.py](https://github.com/jonaesantos/odoo-qms-iso9001/blob/2e95782d1139c96b1c6e166630ed8659cf4475b9/qms/`__manifest__`.py) · [audit.py](https://github.com/jonaesantos/odoo-qms-iso9001/blob/2e95782d1139c96b1c6e166630ed8659cf4475b9/qms/models/audit.py) · [action.py](https://github.com/jonaesantos/odoo-qms-iso9001/blob/2e95782d1139c96b1c6e166630ed8659cf4475b9/qms/models/action.py) · [finding.py](https://github.com/jonaesantos/odoo-qms-iso9001/blob/2e95782d1139c96b1c6e166630ed8659cf4475b9/qms/models/finding.py) · [effectiveness_check.py](https://github.com/jonaesantos/odoo-qms-iso9001/blob/2e95782d1139c96b1c6e166630ed8659cf4475b9/qms/models/effectiveness_check.py) · [hazard.py](https://github.com/jonaesantos/odoo-qms-iso9001/blob/2e95782d1139c96b1c6e166630ed8659cf4475b9/qms/models/hazard.py) · [goal.py](https://github.com/jonaesantos/odoo-qms-iso9001/blob/2e95782d1139c96b1c6e166630ed8659cf4475b9/qms/models/goal.py) · [qms_groups.xml](https://github.com/jonaesantos/odoo-qms-iso9001/blob/2e95782d1139c96b1c6e166630ed8659cf4475b9/qms/security/qms_groups.xml) |

<a id="nt-openqms"></a>

### OpenQMS (Open-Industry-System)

| Thuộc tính | Giá trị |
|---|---|
| Repo | https://github.com/Open-Industry-System/OpenQMS |
| License | MIT |
| Phiên bản đã đọc | `48f591a37d7332753179e10f75830dcb5f073037` (commit 2026-11-23) |
| Kiểm chứng | 2026-11-23; code-read; đã đọc README.md, LICENSE, spc_calculation_engine.py, gauge_service.py, models/gauge.py, eightd_state.py, test.yml và r5-model-egress.md; chưa chạy upstream |
| Khoảng trống lấp | QMS cho nhà máy chế tạo: nhắm IATF 16949 (FMEA, SPC, MSA, 8D, PPAP), có kèm đánh giá nội bộ và xem xét lãnh đạo |
| Cơ chế đáng học | • SPC engine thuần tính toán: hằng số A2, D3, D4, d2 cho n từ 2 đến 10, tám luật Western Electric có bật tắt từng luật, Cp/Cpk/Pp/Ppk/Cm/PPM (spc_calculation_engine.py).<br>• 8D là máy trạng thái D1 đến D6, D7 phòng ngừa, cổng D8 chờ duyệt rồi lưu trữ; chỉ cho phép chuyển theo bảng EIGHTD_TRANSITIONS và có nhánh quay lui D4 về D3, D6 về D5 (eightd_state.py).<br>• Sổ thiết bị đo: chu kỳ hiệu chuẩn, next_calibration_date, bản ghi hiệu chuẩn có số chứng chỉ, log audit mỗi lần ghi; validate_gauge_for_use từ chối thiết bị không active hoặc quá hạn và được gọi từ grr_service, stability_service, control_plan_service (gauge_service.py, models/gauge.py).<br>• AI agent đề xuất bước D5 chỉ qua mô hình được duyệt, ràng buộc địa chỉ, HMAC cấu hình, đề xuất lưu chờ duyệt rồi người mới nhận (r5-model-egress.md; mặc định tắt). |
| Tiêu chí và cách kiểm | Máy tính bằng hàm có hằng số tra bảng; CI test.yml chạy test_schema.py, test_spc_engine.py và pytest chia shard trên PostgreSQL 15 cùng job kiểm SDK; backend/tests có 157 file. Ngưỡng Cpk cứng trong mã: từ 1.67 là tốt, từ 1.33 là đạt, từ 1.0 là cảnh báo, dưới 1.0 gợi ý dừng sản xuất. Không chạy lại test ở đây. |
| Giới hạn và rủi ro | Cp/Cpk tính bằng độ lệch chuẩn mẫu của toàn bộ giá trị (nhãn là ngắn hạn) nên gần với Ppk; ngưỡng và lời khuyên cứng, tiếng Trung. Nhắm IATF 16949 chứ không phải ISO 9001: README viết là hỗ trợ quy trình liên quan IATF, và tuyên bố mục xem xét lãnh đạo theo ISO 9001 9.3 chưa được xác minh bằng mã (chưa xác minh điều khoản); không thấy 14001 hay 45001. Hiệu chuẩn chỉ là sổ và cổng quá hạn, không có độ không đảm bảo, chuẩn tham chiếu hay truy xuất đo lường. Repo trẻ, README có tài khoản demo và mật khẩu mẫu (chỉ dùng phát triển), môi trường demo công khai ghi được; cần 4 GB RAM trở lên; LLM và embedding là tùy chọn, bật thì dữ liệu rời máy tới nhà cung cấp đã duyệt. MIT, bản quyền ghi tên OpenQMS. |
| So với | Odoo QMS ISO 9001 (cùng đợt: chỉ khung dữ liệu); FactorySemantics MES (cùng đợt: nhẹ hơn, SPC và gauge nhưng không có 8D, FMEA); frappe-erpnext trong kho (ERP có module chất lượng, chưa đối chiếu). |
| Nguồn | [README.md](https://github.com/Open-Industry-System/OpenQMS/blob/48f591a37d7332753179e10f75830dcb5f073037/README.md) · [LICENSE](https://github.com/Open-Industry-System/OpenQMS/blob/48f591a37d7332753179e10f75830dcb5f073037/LICENSE) · [spc_calculation_engine.py](https://github.com/Open-Industry-System/OpenQMS/blob/48f591a37d7332753179e10f75830dcb5f073037/backend/app/services/spc_calculation_engine.py) · [gauge_service.py](https://github.com/Open-Industry-System/OpenQMS/blob/48f591a37d7332753179e10f75830dcb5f073037/backend/app/services/gauge_service.py) · [gauge.py](https://github.com/Open-Industry-System/OpenQMS/blob/48f591a37d7332753179e10f75830dcb5f073037/backend/app/models/gauge.py) · [eightd_state.py](https://github.com/Open-Industry-System/OpenQMS/blob/48f591a37d7332753179e10f75830dcb5f073037/backend/app/state_machines/eightd_state.py) · [test.yml](https://github.com/Open-Industry-System/OpenQMS/blob/48f591a37d7332753179e10f75830dcb5f073037/.github/workflows/test.yml) · [r5-model-egress.md](https://github.com/Open-Industry-System/OpenQMS/blob/48f591a37d7332753179e10f75830dcb5f073037/docs/development/r5-model-egress.md) |

<a id="nt-oca-maintenance"></a>

### OCA maintenance (Odoo 19)

| Thuộc tính | Giá trị |
|---|---|
| Repo | https://github.com/OCA/maintenance |
| License | AGPL-3.0 (repo; vài module LGPL-3.0) |
| Phiên bản đã đọc | `0216cccccad104a1ef1cef48988b26210410d793` (commit 2026-11-20) |
| Kiểm chứng | 2026-11-23; code-read; đã đọc README.md, LICENSE, test.yml, các file model của maintenance_equipment_certification và maintenance_plan.py; chưa chạy upstream |
| Khoảng trống lấp | Bảo trì thiết bị (CMMS) trong Odoo; gần hiệu chuẩn chỉ ở mức lịch bảo trì và nhắc hạn chứng chỉ, chưa phải ISO/IEC 17025 |
| Cơ chế đáng học | • maintenance.equipment.certificate: số chứng chỉ, ngày, renewal_date, tệp; cron `_cron_notify_expiring_certificates` đếm số lần đã nhắc so với quy tắc days_before, gửi mail cho kỹ thuật viên hoặc chủ thiết bị, thiếu người nhận thì tạo activity (maintenance_equipment_certificate.py, certificate_reminder_rule.py).<br>• maintenance.plan: interval cùng bước ngày, tuần, tháng, năm; next_maintenance_date tính từ phiếu mở gần nhất, hoặc phiếu cuối cộng chu kỳ, hoặc từ ngày bắt đầu; ràng buộc duy nhất cho cặp thiết bị và loại bảo trì (maintenance_plan.py).<br>• Mỗi addon một việc, nhỏ và ghép được, có manifest khai license riêng và nhóm quyền cơ sở (base_maintenance_group). |
| Tiêu chí và cách kiểm | CI test.yml chạy kiểm phụ thuộc chưa phát hành, test trên container Odoo 19 và OCB 19 với PostgreSQL 13, và manifestoo check-licenses; có pre-commit riêng; maintenance_plan có tests/. Chưa mở các file test, chưa chạy. |
| Giới hạn và rủi ro | Không có hiệu chuẩn thật: không as-found, as-left, độ không đảm bảo, chuẩn tham chiếu; chứng chỉ quá hạn không khóa thiết bị (trong file đã đọc). License lẫn: repo AGPL-3.0 nhưng maintenance_equipment_hierarchy và maintenance_equipment_status là LGPL-3.0, phải đọc manifest từng module. Chỉ dùng được trong Odoo 19, bám nhịp phát hành của Odoo; AGPL buộc công bố mã khi phục vụ qua mạng. Bảo trì tích cực theo commit gần nhất, nhưng không đo. |
| So với | OpenQMS (cùng đợt: có sổ thiết bị đo và cổng quá hạn hiệu chuẩn); FactorySemantics MES (cùng đợt: gauge có as-found); odoo-odoo trong kho (nền). |
| Nguồn | [README.md](https://github.com/OCA/maintenance/blob/0216cccccad104a1ef1cef48988b26210410d793/README.md) · [LICENSE](https://github.com/OCA/maintenance/blob/0216cccccad104a1ef1cef48988b26210410d793/LICENSE) · [test.yml](https://github.com/OCA/maintenance/blob/0216cccccad104a1ef1cef48988b26210410d793/.github/workflows/test.yml) · [\_\_manifest\_\_.py](https://github.com/OCA/maintenance/blob/0216cccccad104a1ef1cef48988b26210410d793/maintenance_equipment_certification/`__manifest__`.py) · [maintenance_equipment_certificate.py](https://github.com/OCA/maintenance/blob/0216cccccad104a1ef1cef48988b26210410d793/maintenance_equipment_certification/models/maintenance_equipment_certificate.py) · [certificate_reminder_rule.py](https://github.com/OCA/maintenance/blob/0216cccccad104a1ef1cef48988b26210410d793/maintenance_equipment_certification/models/certificate_reminder_rule.py) · [maintenance_equipment.py](https://github.com/OCA/maintenance/blob/0216cccccad104a1ef1cef48988b26210410d793/maintenance_equipment_certification/models/maintenance_equipment.py) · [maintenance_plan.py](https://github.com/OCA/maintenance/blob/0216cccccad104a1ef1cef48988b26210410d793/maintenance_plan/models/maintenance_plan.py) |

<a id="nt-factorysemantics-mes"></a>

### FactorySemantics MES

| Thuộc tính | Giá trị |
|---|---|
| Repo | https://github.com/factorysemantics/factorysemantics-mes |
| License | Apache-2.0 |
| Phiên bản đã đọc | `664c5500cc640e022638f0786dc349f36c1b98c7` (commit 2026-11-23) |
| Kiểm chứng | 2026-11-23; code-read; đã đọc README.md, LICENSE, CHANGELOG.md, CLAUDE.md (chỉ coi là nội dung), pyproject.toml, ci.yml, domain/gauges.py, domain/serialization.py, services/gauges.py, services/spc.py, services/quality.py và đầu services/assistant.py; chưa chạy upstream |
| Khoảng trống lấp | MES và ERP mã mở nhẹ cho xưởng vừa và nhỏ, tích hợp sẵn chất lượng, hiệu chuẩn, truy xuất; chưa kiểm chứng ngoài mô phỏng |
| Cơ chế đáng học | • Hiệu chuẩn có ngữ nghĩa: CalibrationResult gồm pass, fail_as_found, adjusted; fail_as_found chuyển thiết bị sang out_of_service và trả danh sách số đo nghi ngờ từ lần hiệu chuẩn tốt trước (services/gauges.py, domain/gauges.py).<br>• Quyết định có chủ ý: số đọc từ thiết bị quá hạn hoặc ngưng dùng không bị từ chối mà ghi tên thiết bị để lần ra bằng gauges impact; mã thiết bị lạ thì bị từ chối (services/quality.py).<br>• SPC: loại biểu đồ theo kế hoạch lấy mẫu (X-bar R khi lấy n mẫu một lần, I-MR khi lấy từng chiếc, p chart cho đếm lỗi), bốn luật Western Electric cộng luật khoảng di động, ngưỡng Cpk cấu hình, mỗi tín hiệu ghi một lần theo window_key (services/spc.py).<br>• Truy xuất theo serial: SerialUnit sinh bởi lệnh ở máy, chứa trong đơn vị khác (chai trong thùng, thùng trên pallet), UnitStatus có quarantined (domain/serialization.py). |
| Tiêu chí và cách kiểm | CI ci.yml chạy ruff, kiểm gói skill và pytest trên Ubuntu và Windows với Python 3.12 và 3.13, cộng job PostgreSQL thật; tests/ có khoảng 300 file kể cả test cho SPC, gauge, serial. Ngưỡng Cpk mặc định trong mã là 1.33 đạt và 1.0 giới hạn, đổi được bằng cấu hình. Chưa chạy. |
| Giới hạn và rủi ro | Pre-alpha 0.5.0, một người duy trì (theo README và pyproject), số liệu chỉ từ mô phỏng nên không dùng làm bằng chứng sản xuất. Không có đánh giá nội bộ, CAPA 8D, FMEA hay xem xét lãnh đạo nên không thay QMS ISO 9001 hay IATF 16949; ISA-95, ISO 22400, PackML là tuyên bố tác giả (chưa xác minh điều khoản). Hiệu chuẩn chỉ có sổ, kết quả và danh sách ảnh hưởng, không có độ không đảm bảo. Trợ lý sàn xưởng gọi mô hình qua urllib (đã đọc đầu file, đích chưa kiểm) và có lớp thương mại tách riêng; chưa kiểm dữ liệu rời máy. Apache-2.0, đóng góp theo DCO. |
| So với | OpenQMS (cùng đợt: QMS đầy đủ FMEA, 8D, PPAP nhưng nặng, nhắm IATF); frappe-erpnext trong kho (ERP có sản xuất); odoo-odoo trong kho; OCA maintenance (cùng đợt: CMMS trong Odoo). |
| Nguồn | [README.md](https://github.com/factorysemantics/factorysemantics-mes/blob/664c5500cc640e022638f0786dc349f36c1b98c7/README.md) · [LICENSE](https://github.com/factorysemantics/factorysemantics-mes/blob/664c5500cc640e022638f0786dc349f36c1b98c7/LICENSE) · [CHANGELOG.md](https://github.com/factorysemantics/factorysemantics-mes/blob/664c5500cc640e022638f0786dc349f36c1b98c7/CHANGELOG.md) · [CLAUDE.md](https://github.com/factorysemantics/factorysemantics-mes/blob/664c5500cc640e022638f0786dc349f36c1b98c7/CLAUDE.md) · [pyproject.toml](https://github.com/factorysemantics/factorysemantics-mes/blob/664c5500cc640e022638f0786dc349f36c1b98c7/pyproject.toml) · [ci.yml](https://github.com/factorysemantics/factorysemantics-mes/blob/664c5500cc640e022638f0786dc349f36c1b98c7/.github/workflows/ci.yml) · [gauges.py](https://github.com/factorysemantics/factorysemantics-mes/blob/664c5500cc640e022638f0786dc349f36c1b98c7/src/fsmes/domain/gauges.py) · [serialization.py](https://github.com/factorysemantics/factorysemantics-mes/blob/664c5500cc640e022638f0786dc349f36c1b98c7/src/fsmes/domain/serialization.py) · [gauges.py](https://github.com/factorysemantics/factorysemantics-mes/blob/664c5500cc640e022638f0786dc349f36c1b98c7/src/fsmes/services/gauges.py) · [spc.py](https://github.com/factorysemantics/factorysemantics-mes/blob/664c5500cc640e022638f0786dc349f36c1b98c7/src/fsmes/services/spc.py) · [quality.py](https://github.com/factorysemantics/factorysemantics-mes/blob/664c5500cc640e022638f0786dc349f36c1b98c7/src/fsmes/services/quality.py) · [assistant.py](https://github.com/factorysemantics/factorysemantics-mes/blob/664c5500cc640e022638f0786dc349f36c1b98c7/src/fsmes/services/assistant.py) |

<a id="nt-shewhart-mcp"></a>

### shewhart-mcp

| Thuộc tính | Giá trị |
|---|---|
| Repo | https://github.com/bertanucar/shewhart-mcp |
| License | Không có file LICENSE (README và pyproject khai MIT, chưa xác minh) |
| Phiên bản đã đọc | `e08494ac970d0e304cb8ca1937b3b11179423a5b` (commit 2026-06-12) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, pyproject.toml, shewhart_mcp/`__init__`.py, .github/workflows/release.yml; chưa chạy upstream |
| Khoảng trống lấp | SPC (kiểm soát quá trình thống kê) và Cp/Cpk: mẫu nối thư viện SPC vào agent qua MCP, nhưng mới ở giai đoạn giữ chỗ |
| Cơ chế đáng học | - `README.md`: lý lẽ thiết kế (agent diễn giải, mã đã kiểm chứng tính), bảng sáu công cụ dự kiến gồm biểu đồ I-MR, Xbar-R/S, p/np/c/u, Laney, EWMA, CUSUM, Cp/Cpk/Pp/Ppk có khoảng tin cậy, khoảng dung sai Howe và Wilks, đóng băng giới hạn kiểm soát.<br>- Dự kiến mỗi kết quả kèm provenance (phiên bản thư viện, hash đầu vào, thời điểm) **(kế hoạch, chưa có mã)**.<br>- `pyproject.toml`: phụ thuộc vào thư viện `shewhart>=0.1.0` (repo khác, chưa đọc), Python 3.10 trở lên.<br>- Chưa có mã triển khai nào để học; chỉ có khung gói và workflow phát hành. |
| Tiêu chí và cách kiểm | Không có test và không có mã tính toán. `release.yml` (đã mở) chỉ build và đẩy gói lên PyPI khi có tag `v*` bằng OIDC. Tuyên bố "đối chiếu với giá trị tham chiếu NIST trong CI" không có CI nào thực hiện trong repo này **(chưa xác minh)**; nếu có thì ở repo thư viện `shewhart`. |
| Giới hạn và rủi ro | Không có file LICENSE trong repo (license ghi null); README và `pyproject.toml` ghi MIT nên chỉ là khai báo của tác giả, chưa thể coi là giấy phép có hiệu lực **(chưa xác minh)**, và `open_source: true` ở đây chỉ phản ánh khai báo đó. Gói chưa có chức năng, một tác giả, không hoạt động từ 6/2026. Nếu cần SPC cho agent, đọc và đánh giá repo `shewhart` thay vì repo này. |
| So với | Chưa có hồ sơ SPC cùng loại trong kho; so với mục 38 chưa có công cụ SPC khác để đối chiếu |
| Nguồn | [README.md](https://github.com/bertanucar/shewhart-mcp/blob/e08494ac970d0e304cb8ca1937b3b11179423a5b/README.md) · [pyproject.toml](https://github.com/bertanucar/shewhart-mcp/blob/e08494ac970d0e304cb8ca1937b3b11179423a5b/pyproject.toml) · [shewhart\_mcp/`\_\_init\_\_`.py](https://github.com/bertanucar/shewhart-mcp/blob/e08494ac970d0e304cb8ca1937b3b11179423a5b/shewhart_mcp/`__init__`.py) · [.github/workflows/release.yml](https://github.com/bertanucar/shewhart-mcp/blob/e08494ac970d0e304cb8ca1937b3b11179423a5b/.github/workflows/release.yml) |

<a id="nt-oca-manufacture"></a>

### OCA manufacture (Odoo MRP addons)

| Thuộc tính | Giá trị |
|---|---|
| Repo | https://github.com/OCA/manufacture |
| License | AGPL-3.0 (LICENSE gốc); module riêng AGPL-3 hoặc LGPL-3 |
| Phiên bản đã đọc | `b07b1b852a196fffd3ab7bd656cb359c489c5aed` (commit 2026-11-23) |
| Kiểm chứng | 2026-11-23; code-read; đã đọc LICENSE, README.md, mrp_multi_level/`__manifest__`.py, mrp_multi_level/wizards/mrp_multi_level.py, quality_control_oca/`__manifest__`.py; chưa chạy upstream |
| Khoảng trống lấp | MES/ERP mã mở nhẹ cho xưởng vừa và nhỏ: addon MRP và kiểm soát chất lượng trên Odoo Community |
| Cơ chế đáng học | - `mrp_multi_level`: tính nhu cầu theo thứ tự mã cấp thấp nhất (`_low_level_code_calculation` trong `wizards/mrp_multi_level.py`), khởi tạo từ tồn, dự báo, đơn mua, rồi tạo `mrp.planned.order` để xác nhận thành PO hoặc MO; có cron hằng ngày (`data/mrp_multi_level_cron.xml`), khai báo `Production/Stable`.<br>- `quality_control_oca/models/qc_inspection.py`: `qc.inspection` có trạng thái plan, draft, ready, waiting supervisor approval, success, failed; mỗi dòng đạt khi giá trị định lượng nằm trong khoảng `min_value` đến `max_value` (so sau quy đổi đơn vị) hoặc đáp án định tính đánh dấu `ok`; cả phiếu đạt khi mọi dòng đạt.<br>- `mrp_production_unique_lot`, `mrp_lot_number_propagation`, `mrp_bom_tracking` hỗ trợ truy vết lô và nhật ký thay đổi BoM. |
| Tiêu chí và cách kiểm | CI `test.yml` (đã mở): chạy trên ảnh OCA với Odoo 19.0 và OCB 19.0, `manifestoo check-licenses`, `check-dev-status`, `oca_run_tests` kèm coverage; có test trong mrp_multi_level (33 hàm `test_`) và quality_control_oca (10 hàm `test_`). Kiểm bằng máy nhưng chỉ khi chạy trong hạ tầng OCA; chưa chạy lại ở đây. Không có kiểm SPC hay biểu đồ kiểm soát. |
| Giới hạn và rủi ro | LICENSE gốc là AGPL-3.0; README nói mỗi module có thể có license khác: 24 module khai `AGPL-3`, 7 module khai `LGPL-3` (mrp_bom_tracking, mrp_multi_level, mrp_multi_level_estimate, mrp_subcontracting_purchase_link, mrp_subcontracting_resupply_status, mrp_warehouse_calendar, mrp_workorder_sequence), theo `__manifest__.py`. AGPL ràng buộc khi cung cấp dịch vụ qua mạng. Phụ thuộc Odoo và đổi phiên bản Odoo thì phải chọn nhánh khác. Số sao của trinh sát để trống nên chưa xác minh. Không có MES thật (ghi nhận máy, OEE), chỉ lệnh sản xuất và workorder. |
| So với | odoo-odoo và frappe-erpnext (ERP đầy đủ cùng họ), các hồ sơ quality-mgmt khác ở mục 38 |
| Nguồn | [LICENSE](https://github.com/OCA/manufacture/blob/b07b1b852a196fffd3ab7bd656cb359c489c5aed/LICENSE) · [README.md](https://github.com/OCA/manufacture/blob/b07b1b852a196fffd3ab7bd656cb359c489c5aed/README.md) · [mrp\_multi\_level/`\_\_manifest\_\_`.py](https://github.com/OCA/manufacture/blob/b07b1b852a196fffd3ab7bd656cb359c489c5aed/mrp_multi_level/`__manifest__`.py) · [mrp_multi_level/wizards/mrp_multi_level.py](https://github.com/OCA/manufacture/blob/b07b1b852a196fffd3ab7bd656cb359c489c5aed/mrp_multi_level/wizards/mrp_multi_level.py) · [quality\_control\_oca/`\_\_manifest\_\_`.py](https://github.com/OCA/manufacture/blob/b07b1b852a196fffd3ab7bd656cb359c489c5aed/quality_control_oca/`__manifest__`.py) · [quality_control_oca/models/qc_inspection.py](https://github.com/OCA/manufacture/blob/b07b1b852a196fffd3ab7bd656cb359c489c5aed/quality_control_oca/models/qc_inspection.py) · [.github/workflows/test.yml](https://github.com/OCA/manufacture/blob/b07b1b852a196fffd3ab7bd656cb359c489c5aed/.github/workflows/test.yml) |

<a id="n2-2026-11-24"></a>

## Nâng trần đợt hai — 23/11/2026

Hồ sơ lập trong đợt nâng trần thứ hai: đọc mã hoặc tài liệu tại commit cố định, chưa chạy upstream; mô tả của trinh sát sai ở nhiều repo nên điều ghi ở đây là điều đã đọc.

<a id="n2-atlas-cmms"></a>

### Atlas CMMS (Grashjs)

| Thuộc tính | Giá trị |
|---|---|
| Repo | https://github.com/Grashjs/cmms |
| License | AGPL-3.0 (song song giấy phép thương mại) |
| Phiên bản đã đọc | `a3c7ce38adedeb90ac13c280e8ccad6622ff2a42` (commit 2026-11-21) |
| Kiểm chứng | 2026-11-24; code-read; đã đọc README.MD, LICENSE, COMMERCIAL_LICENSE.MD, PreventiveMaintenanceService.java, LicenseService.java, LicenseEntitlement.java, PlanFeatures.java, Consts.java, main-ci.yml; chưa chạy upstream |
| Khoảng trống lấp | CMMS tự host: lệnh công việc, tài sản, bảo trì phòng ngừa |
| Cơ chế đáng học | - Mô hình dữ liệu Spring/JPA đầy đủ cho CMMS: `WorkOrder`, `Asset`, `PreventiveMaintenance`, `Schedule`, `Meter`, `WorkOrderMeterTrigger`, `Part`, `PurchaseOrder`, `Request`, `Workflow` (thư mục `model/`).<br>- `PreventiveMaintenanceService.java`: bảo trì phòng ngừa lên lịch bằng Quartz (`Scheduler`), kiểm quyền theo vai trò (`PermissionEntity`) và tính năng theo gói (`PlanFeatures`); lịch có tần suất, kiểu lặp, ngày trong tuần, độ trễ hạn.<br>- Kích hoạt theo đồng hồ đo: `WorkOrderMeterTrigger` và entitlement `CONDITION_BASED_PM` (chưa mở thân của trigger).<br>- Giới hạn bản miễn phí đặt trong `Consts.usageBasedFreeLimits`: 5 người dùng, 50 tài sản, 100 phụ tùng, 10 địa điểm, 10 lịch PM, 30 lệnh công việc đang mở, 10 đồng hồ đo, 10 checklist. |
| Tiêu chí và cách kiểm | Có test Maven (`mvn test` trong `main-ci.yml`, đã mở) và một job smoke test tự host xây image Docker; thư mục `api/src/test` có test controller, tích hợp, aspect. Kiểm bằng máy; chưa chạy. Chưa đọc nội dung test. |
| Giới hạn và rủi ro | Dual license: AGPL-3.0 hoặc giấy phép thương mại của INTELLOOP LLC (chọn một). Bản tự host bị giới hạn theo `usageBasedFreeLimits` trừ khi có khóa: `LicenseService` gọi `api.keygen.sh` để xác thực khóa (cache 12 giờ, tối đa 20 yêu cầu mỗi ngày) hoặc đọc file giấy phép; nhiều tính năng (SSO, workflow, webhook, vai trò tùy chỉnh, PM theo điều kiện, lịch PM) là entitlement trả phí. Thực tế bản mã mở bị giới hạn so với README (tuyên bố tính năng đầy đủ). Có Firebase/Google Maps/mobile (chưa đọc). 'Hoạt động đến 2026-11' đúng với ngày commit; chất lượng chưa kiểm. |
| So với | OCA maintenance (`oca-maintenance`) là module bảo trì trong Odoo; ERPNext (`frappe-erpnext`) có module bảo trì trong ERP; OpenMES (`mes-open-openmes`) thiên về sản xuất hơn là bảo trì. |
| Nguồn | [README](https://github.com/Grashjs/cmms/blob/a3c7ce38adedeb90ac13c280e8ccad6622ff2a42/README.MD) · [LICENSE](https://github.com/Grashjs/cmms/blob/a3c7ce38adedeb90ac13c280e8ccad6622ff2a42/LICENSE) · [COMMERCIAL_LICENSE](https://github.com/Grashjs/cmms/blob/a3c7ce38adedeb90ac13c280e8ccad6622ff2a42/COMMERCIAL_LICENSE.MD) · [PreventiveMaintenanceService](https://github.com/Grashjs/cmms/blob/a3c7ce38adedeb90ac13c280e8ccad6622ff2a42/api/src/main/java/com/grash/service/PreventiveMaintenanceService.java) · [LicenseService](https://github.com/Grashjs/cmms/blob/a3c7ce38adedeb90ac13c280e8ccad6622ff2a42/api/src/main/java/com/grash/service/LicenseService.java) · [LicenseEntitlement](https://github.com/Grashjs/cmms/blob/a3c7ce38adedeb90ac13c280e8ccad6622ff2a42/api/src/main/java/com/grash/dto/license/LicenseEntitlement.java) · [PlanFeatures](https://github.com/Grashjs/cmms/blob/a3c7ce38adedeb90ac13c280e8ccad6622ff2a42/api/src/main/java/com/grash/model/enums/PlanFeatures.java) · [Consts](https://github.com/Grashjs/cmms/blob/a3c7ce38adedeb90ac13c280e8ccad6622ff2a42/api/src/main/java/com/grash/utils/Consts.java) · [main-ci.yml](https://github.com/Grashjs/cmms/blob/a3c7ce38adedeb90ac13c280e8ccad6622ff2a42/.github/workflows/main-ci.yml) |

<a id="n2-qcadoo-mes"></a>

### qcadoo MES

| Thuộc tính | Giá trị |
|---|---|
| Repo | https://github.com/qcadoo/mes |
| License | AGPL-3.0-or-later (README và header LICENSE.txt; không có văn bản AGPL đầy đủ) |
| Phiên bản đã đọc | `625afad7a8adaaa65b5b8b7bd7867af21aafc960` (commit 2026-11-20) |
| Kiểm chứng | 2026-11-24; code-read; đã đọc README, LICENSE.txt, pom.xml, RunForStateTransitionAspect.java, ProductionTrackingStateStringValues.java, StoppageService.java, help.properties; chưa chạy upstream |
| Khoảng trống lấp | MES/ERP sản xuất nhẹ cho nhà máy vừa và nhỏ (lệnh sản xuất, công nghệ, đếm sản lượng, dừng máy) |
| Cơ chế đáng học | - Kiến trúc plugin Maven (56 thư mục trong `mes-plugins/`): orders, technologies, production-counting, stoppage, material-flow, deliveries, cost-calculation, production-scheduling, wage-groups, cmms-machine-parts...<br>- Máy trạng thái dùng AOP: annotation `@RunForStateTransition` và `RunForStateTransitionAspect` chỉ chạy listener khi cặp (trạng thái nguồn, đích) khớp, hỗ trợ ký tự đại diện `*`.<br>- Phiếu đếm sản lượng (`ProductionTracking`) có vòng đời 01draft, 02accepted, 03declined, 04corrected, 05pending.<br>- `StoppageService` mở danh sách dừng máy lọc theo số lệnh sản xuất. |
| Tiêu chí và cách kiểm | Không thấy workflow GitHub Actions hay Travis trong repo; commit gần nhất là merge `dev` do tài khoản `jenkins` (CI nằm ngoài kho, chưa xác minh). Có 214 file nằm trong thư mục `src/test`; chưa đọc test. Không có ngưỡng độ phủ. |
| Giới hạn và rủi ro | License: GitHub báo NOASSERTION vì `LICENSE.txt` (21 dòng) chỉ chứa phần header 'AGPL phiên bản 3 hoặc mới hơn', không có văn bản AGPL đầy đủ; README ghi AGPLv3. Bản cộng đồng bị cắt so với bản thương mại: không có REST API, Gantt lập kế hoạch, module bảo trì, tích hợp SCADA (theo README, chưa xác minh). Mô tả của trinh sát về OEE không có cơ sở trong mã đã đọc: không có plugin OEE trong `mes-plugins/`, chỉ có đường dẫn tài liệu `oee.*` trong `help.properties`. Phụ thuộc framework qcadoo từ super-pom (không nằm trong repo); Java 1.8, phiên bản `1.5-SNAPSHOT`: công nghệ cũ. |
| So với | OpenMES (`mes-open-openmes`) hiện đại hơn (Laravel) với audit log và truy vết lô; Odoo Community (`odoo-odoo`) và ERPNext (`frappe-erpnext`) có module sản xuất; OCA manufacture (`oca-manufacture`). |
| Nguồn | [README](https://github.com/qcadoo/mes/blob/625afad7a8adaaa65b5b8b7bd7867af21aafc960/README.md) · [LICENSE.txt](https://github.com/qcadoo/mes/blob/625afad7a8adaaa65b5b8b7bd7867af21aafc960/LICENSE.txt) · [pom.xml](https://github.com/qcadoo/mes/blob/625afad7a8adaaa65b5b8b7bd7867af21aafc960/pom.xml) · [RunForStateTransitionAspect](https://github.com/qcadoo/mes/blob/625afad7a8adaaa65b5b8b7bd7867af21aafc960/mes-plugins/mes-plugins-states/src/main/java/com/qcadoo/mes/states/aop/RunForStateTransitionAspect.java) · [ProductionTrackingStateStringValues](https://github.com/qcadoo/mes/blob/625afad7a8adaaa65b5b8b7bd7867af21aafc960/mes-plugins/mes-plugins-production-counting/src/main/java/com/qcadoo/mes/productionCounting/states/constants/ProductionTrackingStateStringValues.java) · [StoppageService](https://github.com/qcadoo/mes/blob/625afad7a8adaaa65b5b8b7bd7867af21aafc960/mes-plugins/mes-plugins-stoppage/src/main/java/com/qcadoo/mes/stoppage/StoppageService.java) · [help.properties](https://github.com/qcadoo/mes/blob/625afad7a8adaaa65b5b8b7bd7867af21aafc960/mes-plugins/mes-plugins-technologies/src/main/resources/help.properties) |

<a id="n2-node-opcua"></a>

### node-opcua

| Thuộc tính | Giá trị |
|---|---|
| Repo | https://github.com/node-opcua/node-opcua |
| License | MIT |
| Phiên bản đã đọc | `86c0da2bc582a06e6a8f8531905b6da1ea376c8f` (commit 2026-11-23) |
| Kiểm chứng | 2026-11-24; code-read; đã đọc README, LICENSE, supported_features.md, certificate_manager.ts, security_policy.ts, workflow.yml; chưa chạy upstream |
| Khoảng trống lấp | Kết nối dữ liệu thiết bị và PLC qua chuẩn mở OPC UA |
| Cơ chế đáng học | - Hiện thực OPC UA đầy đủ bằng TypeScript: client, server, discovery; 134 gói con trong `packages/`, tất cả mã nguồn đọc được ghi MIT (125 gói node-opcua* có `license: MIT`).<br>- `security_policy.ts` liệt kê chính sách bảo mật gồm Basic256Sha256, Aes128_Sha256_RsaOaep, Aes256_Sha256_RsaPss...; `supported_features.md` kê dịch vụ và profile đã hỗ trợ, chưa hỗ trợ (HistoryRead/Update một phần, AddNodes chưa có).<br>- `OPCUACertificateManager` quản lý kho chứng chỉ tin cậy theo thư mục trusted/rejected; `automaticallyAcceptUnknownCertificate` mặc định false (`!!options...`).<br>- Có bộ sinh nodeset từ XML và kiểm drift trong CI (`pnpm run generate` rồi `git diff`). |
| Tiêu chí và cách kiểm | CI `workflow.yml` (đã mở) có job kiểm file sinh không lệch nguồn, kiểm nhất quán phiên bản workspace, test đơn vị, và matrix nhiều phiên bản Node (24.x, job riêng Node 26); báo độ phủ lên Coveralls. Kiểm bằng máy; chưa chạy. Tính tuân thủ CTT còn nằm trong lộ trình (README: 'Compliance testing and certification (CTT)'). |
| Giới hạn và rủi ro | Mô tả của trinh sát sai ở điểm MTConnect và UNS: không thấy MTConnect hay Sparkplug trong repo; đây là thư viện OPC UA thuần. PubSub và GDS được ghi là 'commercial module' (không có trong repo). Hỗ trợ dài hạn, CVE sớm và bản build chứng nhận là gói trả phí của Sterfive. Yêu cầu Node.js từ 22.13. Redundancy, session-less transaction chưa có. Chưa kiểm hiệu năng hoặc độ bền ngoài CI. Không thu telemetry ở các file đã đọc (chưa quét toàn repo). |
| So với | Node-RED (`node-red`) là công cụ luồng, có thể dùng node OPC UA dựa trên chính node-opcua; không có hồ sơ OPC UA nào khác trong kho nên đây là khoảng trống giao thức công nghiệp. |
| Nguồn | [README](https://github.com/node-opcua/node-opcua/blob/86c0da2bc582a06e6a8f8531905b6da1ea376c8f/README.md) · [LICENSE](https://github.com/node-opcua/node-opcua/blob/86c0da2bc582a06e6a8f8531905b6da1ea376c8f/LICENSE) · [supported_features](https://github.com/node-opcua/node-opcua/blob/86c0da2bc582a06e6a8f8531905b6da1ea376c8f/supported_features.md) · [certificate_manager.ts](https://github.com/node-opcua/node-opcua/blob/86c0da2bc582a06e6a8f8531905b6da1ea376c8f/packages/node-opcua-certificate-manager/source/certificate_manager.ts) · [security_policy.ts](https://github.com/node-opcua/node-opcua/blob/86c0da2bc582a06e6a8f8531905b6da1ea376c8f/packages/node-opcua-secure-channel/source/security_policy.ts) · [workflow.yml](https://github.com/node-opcua/node-opcua/blob/86c0da2bc582a06e6a8f8531905b6da1ea376c8f/.github/workflows/workflow.yml) |

<a id="n2-weldx"></a>

### WelDX

| Thuộc tính | Giá trị |
|---|---|
| Repo | https://github.com/BAMWelDX/weldx |
| License | BSD-3-Clause |
| Phiên bản đã đọc | `2d9fa832b632b8e5bffb8ddd5fee00af2c41056e` (commit 2026-11-09) |
| Kiểm chứng | 2026-11-24; code-read; đã đọc README, LICENSE, pyproject.toml, iso_9692_1.py, hai schema YAML (shielding_gas_for_procedure, GMAW), pytest.yml, pytest_asdf.yml; chưa chạy upstream |
| Khoảng trống lấp | Dữ liệu hàn có cấu trúc làm nền cho WPS/PQR và bản ghi thông số hàn |
| Cơ chế đáng học | - Định dạng ASDF có schema: 74 file YAML trong `weldx/schemas/weldx.bam.de/weldx/` (process, groove, equipment, measurement, core/time_series, units...), đăng ký qua entry point `asdf.extensions` trong `pyproject.toml`.<br>- `weldx/welding/groove/iso_9692_1.py`: 12 kiểu rãnh hàn theo ISO 9692-1 (I, V, VV, U, HV, DV...) dưới dạng dataclass với đại lượng có đơn vị (pint), tính `cross_sect_area` và hình học `to_profile`.<br>- Schema `aws/process/shielding_gas_for_procedure` mô tả khí bảo vệ, lưu lượng, khí lót và khí đuôi (đặt trong thư mục `aws`, gần ngôn ngữ quy trình hàn); schema `process/GMAW` kèm ví dụ xung CLOOS với dòng, tần số xung theo chuỗi thời gian có đơn vị.<br>- Đo đạc: chuỗi đo, thiết bị, nguồn sai số và biến đổi tọa độ được ghi cùng nhau để truy xuất. |
| Tiêu chí và cách kiểm | Hai workflow đã mở: `pytest.yml` chạy ma trận môi trường Python 3.10-3.14 và `test-min-deps` (theo pixi, cron hàng tuần) kèm Codecov; `pytest_asdf.yml` kiểm schema với asdf 3, 4, 5 và kiểm manifest không lệch. pytest cấu hình `--doctest-modules`. Kiểm bằng máy; chưa chạy. |
| Giới hạn và rủi ro | BSD-3-Clause. Không phải công cụ WPS/PQR: không có mô hình hồ sơ đánh giá quy trình theo ISO 15614 hay ISO 15609, chỉ có một số schema giống thông số quy trình (khí bảo vệ, GMAW). Schema phiên bản 0.1.x, manifest 0.1.0 đến 0.1.2: định dạng còn đang phát triển. Quy mô cộng đồng nhỏ. Chỉ chạy trong hệ Python (asdf, xarray, pint), không có công cụ cho người viết WPS không lập trình. README nói dự án đang phát triển tích cực. |
| So với | Kho chưa có hồ sơ hàn nào khác; gần nhất là nhóm chất lượng (`odoo-qms-iso9001`, `openqms`) nhưng đó là QMS tổng quát chứ không phải dữ liệu hàn. |
| Nguồn | [README](https://github.com/BAMWelDX/weldx/blob/2d9fa832b632b8e5bffb8ddd5fee00af2c41056e/README.md) · [LICENSE](https://github.com/BAMWelDX/weldx/blob/2d9fa832b632b8e5bffb8ddd5fee00af2c41056e/LICENSE) · [pyproject.toml](https://github.com/BAMWelDX/weldx/blob/2d9fa832b632b8e5bffb8ddd5fee00af2c41056e/pyproject.toml) · [iso_9692_1.py](https://github.com/BAMWelDX/weldx/blob/2d9fa832b632b8e5bffb8ddd5fee00af2c41056e/weldx/welding/groove/iso_9692_1.py) · [shielding_gas_for_procedure](https://github.com/BAMWelDX/weldx/blob/2d9fa832b632b8e5bffb8ddd5fee00af2c41056e/weldx/schemas/weldx.bam.de/weldx/aws/process/shielding_gas_for_procedure-0.1.0.yaml) · [GMAW](https://github.com/BAMWelDX/weldx/blob/2d9fa832b632b8e5bffb8ddd5fee00af2c41056e/weldx/schemas/weldx.bam.de/weldx/process/GMAW-0.1.0.yaml) · [pytest.yml](https://github.com/BAMWelDX/weldx/blob/2d9fa832b632b8e5bffb8ddd5fee00af2c41056e/.github/workflows/pytest.yml) · [pytest_asdf.yml](https://github.com/BAMWelDX/weldx/blob/2d9fa832b632b8e5bffb8ddd5fee00af2c41056e/.github/workflows/pytest_asdf.yml) |

<a id="n2-aspc"></a>

### ASPC

| Thuộc tính | Giá trị |
|---|---|
| Repo | https://github.com/M1ndSmith/ASPC |
| License | MIT (© 2025 Samad El-joaydi; pyproject cũng khai MIT) |
| Phiên bản đã đọc | `590f69ef76b9aac698aceec49da82200728a7378` (commit 2026-08-13) |
| Kiểm chứng | 2026-11-24; code-read; đã đọc README, LICENSE, pyproject.toml, spc_core/pipeline.py, spc_core/msa.py, docs/overview/benchmarking.md, .github/workflows/ci.yml; chưa chạy upstream |
| Khoảng trống lấp | Biểu đồ kiểm soát SPC nhúng vào bảng giám sát và công cụ BI; thêm MSA có cổng go-live |
| Cơ chế đáng học | - `spc_core/pipeline.py` `establish()`: chuỗi cổng MSA → tự tương quan → chuẩn tính → đa đỉnh (STOP) → biến đổi/Wheeler → biểu đồ → cổng đóng băng; có STOP thì không đóng băng giới hạn Phase I<br>- `phase1_checklist()` cùng file: 10 mục go-live (MSA, chuẩn tính, ACF, outlier, dữ liệu thiếu, tối thiểu 25 điểm/nhóm con, giới hạn đã đóng băng có hash phiên bản…)<br>- `spc_core/msa.py`: Gage R&R ANOVA/range, bias, linearity, stability; `ndc_gate` (NDC ≥ 5) và `gage_resolution_gate` (độ phân giải ≤ dung sai/10) |
| Tiêu chí và cách kiểm | %GRR dưới 10 tốt, 10–30 có điều kiện, trên 30 không đạt (theo AIAG MSA-4, `_acceptability`); tối thiểu 25 điểm Phase I. CI (`ci.yml`) chạy ruff, mypy `spc_core`, pytest (bỏ integration), báo cáo resilience, bộ 28 kiểm tra công thức `benchmarks/accuracy.py` (chặn) và kiểm không còn stub; ma trận combinatorial để `continue-on-error`. Kiểm bằng máy, nhưng tôi chưa chạy. |
| Giới hạn và rủi ro | MIT, không thấy telemetry trong phần đã đọc; webhook ký gửi cảnh báo ra URL do người dùng cấu hình. Stack đầy đủ nặng (TimescaleDB, Redis, Redpanda, Mosquitto). Tác giả tự nêu: độ chính xác là khớp công thức, không phải tương đương Minitab/JMP; cổng MSA và valid_range tùy chọn, thiếu thì chỉ cảnh báo. Mô tả của trinh sát (nhúng vào bảng giám sát/BI) chỉ đúng một phần: có dashboard Next.js riêng và Grafana tùy chọn, không phải plugin BI; chưa xác minh tính đúng của số liệu thống kê ngoài test của tác giả. |
| So với | aus-doh-powerbi-spc (SPC trong Power BI), shewhart-mcp, pyshewhart |
| Nguồn | [README.md](https://github.com/M1ndSmith/ASPC/blob/590f69ef76b9aac698aceec49da82200728a7378/README.md) · [LICENSE](https://github.com/M1ndSmith/ASPC/blob/590f69ef76b9aac698aceec49da82200728a7378/LICENSE) · [pyproject.toml](https://github.com/M1ndSmith/ASPC/blob/590f69ef76b9aac698aceec49da82200728a7378/pyproject.toml) · [pipeline.py](https://github.com/M1ndSmith/ASPC/blob/590f69ef76b9aac698aceec49da82200728a7378/spc_core/pipeline.py) · [msa.py](https://github.com/M1ndSmith/ASPC/blob/590f69ef76b9aac698aceec49da82200728a7378/spc_core/msa.py) · [benchmarking.md](https://github.com/M1ndSmith/ASPC/blob/590f69ef76b9aac698aceec49da82200728a7378/docs/overview/benchmarking.md) · [ci.yml](https://github.com/M1ndSmith/ASPC/blob/590f69ef76b9aac698aceec49da82200728a7378/.github/workflows/ci.yml) |

<a id="n2-six-sigma-r-skill"></a>

### Six Sigma in R (skill)

| Thuộc tính | Giá trị |
|---|---|
| Repo | https://github.com/robustagile/six-sigma-in-r-skill |
| License | Apache-2.0 |
| Phiên bản đã đọc | `2343167b4557dc0ab66e8a32d28a396954f7fbb0` (commit 2026-04-17) |
| Kiểm chứng | 2026-11-24; code-read; đã đọc README, LICENSE, SKILL.md, references/control_charts.md, evals/evals.json; chưa chạy upstream |
| Khoảng trống lấp | Kỹ năng agent cho Six Sigma/Cp-Cpk (không có MSA) |
| Cơ chế đáng học | - `skills/six-sigma-r/SKILL.md`: hỏi một lần script hay function, file hay inline; bảng ánh xạ cách diễn đạt của người dùng sang 12 file `references/`; quy ước: base R, hằng số đặt ở đầu file, in kết luận chứ không chỉ số<br>- `references/control_charts.md`: bảng hằng số SPC n=2..10 (A2, D3, D4, d2, A3, B3, B4, c4), kẹp LCL ≥ 0 cho P/NP/C/U<br>- `evals/evals.json`: 5 prompt kèm đầu ra kỳ vọng để so có/không skill (không có kịch bản chạy trong repo) |
| Tiêu chí và cách kiểm | Chỉ có `evals/evals.json` (prompt và mô tả đầu ra kỳ vọng); không có test tự động hay CI (không có thư mục .github). Số liệu đánh giá (30/30 so 30/30; 36/36 so 34/36 với Claude Opus 4.7) nằm trong README và thư mục `eval-workspace/` mà repo không chứa (chưa xác minh). |
| Giới hạn và rủi ro | Apache-2.0, không telemetry (chỉ là văn bản hướng dẫn). Rủi ro nội dung: mã R do agent sinh ra cần người dùng kiểm; không có MSA nên không thay được công cụ kiểu ASPC. Repo mới (v1.0.0, 17/04/2026), 12 sao, một tác giả. Bảng hằng số do tác giả chép, tôi chưa đối chiếu với bảng chuẩn. |
| So với | shewhart-mcp (công cụ SPC qua MCP), pyshewhart; cùng kiểu skill nghề với các gói trong `20-claude-plugins-ecosystem` |
| Nguồn | [README.md](https://github.com/robustagile/six-sigma-in-r-skill/blob/2343167b4557dc0ab66e8a32d28a396954f7fbb0/README.md) · [LICENSE](https://github.com/robustagile/six-sigma-in-r-skill/blob/2343167b4557dc0ab66e8a32d28a396954f7fbb0/LICENSE) · [SKILL.md](https://github.com/robustagile/six-sigma-in-r-skill/blob/2343167b4557dc0ab66e8a32d28a396954f7fbb0/skills/six-sigma-r/SKILL.md) · [control_charts.md](https://github.com/robustagile/six-sigma-in-r-skill/blob/2343167b4557dc0ab66e8a32d28a396954f7fbb0/skills/six-sigma-r/references/control_charts.md) · [evals.json](https://github.com/robustagile/six-sigma-in-r-skill/blob/2343167b4557dc0ab66e8a32d28a396954f7fbb0/evals/evals.json) |

<a id="n2-industrial-calibration"></a>

### Industrial Calibration

| Thuộc tính | Giá trị |
|---|---|
| Repo | https://github.com/ros-industrial/industrial_calibration |
| License | Apache-2.0 (LICENSE và `package.xml`) |
| Phiên bản đã đọc | `c275104eef312ec5a5e07d4e228d6e9e1038f1e4` (commit 2026-09-08) |
| Kiểm chứng | 2026-11-24; code-read; đã đọc README, LICENSE, package.xml, analysis/src/statistics.cpp, optimizations/src/covariance_analysis.cpp, test/camera_intrinsic_calibration_validation_utest.cpp, docs/page_primer.dox, ubuntu.yml, CHANGELOG.rst; chưa chạy upstream |
| Khoảng trống lấp | Hiệu chuẩn hệ đo công nghiệp bằng thuật toán camera-robot (không phải quản lý thiết bị đo) |
| Cơ chế đáng học | - `optimizations/src/covariance_analysis.cpp`: `computeCovarianceResults` đổi ma trận hiệp phương sai thành độ lệch chuẩn từng tham số và hệ số tương quan có tên, để nhận ra tham số không phân biệt được<br>- `analysis/src/statistics.cpp`: trung bình quaternion bằng SVD và độ lệch góc, dùng cho phân tích nhiễu và lặp lại<br>- `analysis/src` còn có `noise_qualification.cpp`, `homography_analysis.cpp` và `camera_intrinsic_calibration_analysis.cpp` (kiểm tra sai số sau hiệu chuẩn bằng cách đo lệch giữa bảng mục tiêu ảo với bảng thật) |
| Tiêu chí và cách kiểm | Test gtest trong `test/` (`*_utest.cpp`: nội tại, tay-mắt, đa camera tĩnh, DH, hiệp phương sai, nhiễu, PnP); ví dụ `camera_intrinsic_calibration_validation_utest.cpp` dùng `EXPECT_LT(pos_error.first + 2·pos_error.second, threshold)` (trung bình + 2 sigma dưới ngưỡng). CI `ubuntu.yml` build bằng colcon trên focal/jammy/noble, bật clang-tidy và chạy test (đã mở workflow; kết quả chưa xem). |
| Giới hạn và rủi ro | Apache-2.0, không thấy telemetry. Cần ROS/PCL/Ceres/OpenCV (build trên Ubuntu qua colcon) nên nặng để mang vào dự án ngoài ROS. Lân cận chủ đề: không quản lý chu kỳ hiệu chuẩn thiết bị đo hay truy xuất đơn vị chuẩn. Bảo trì tích cực (commit 09/2026, CHANGELOG 1.2.0 ngày 02/10/2025). Phân loại `simulation` của trinh sát không hợp, đặt vào computer-vision. |
| So với | opencv (thư viện thị giác máy tính nền), kornia; không có hồ sơ hiệu chuẩn tay-mắt nào khác trong kho |
| Nguồn | [README.md](https://github.com/ros-industrial/industrial_calibration/blob/c275104eef312ec5a5e07d4e228d6e9e1038f1e4/README.md) · [LICENSE](https://github.com/ros-industrial/industrial_calibration/blob/c275104eef312ec5a5e07d4e228d6e9e1038f1e4/LICENSE) · [package.xml](https://github.com/ros-industrial/industrial_calibration/blob/c275104eef312ec5a5e07d4e228d6e9e1038f1e4/package.xml) · [statistics.cpp](https://github.com/ros-industrial/industrial_calibration/blob/c275104eef312ec5a5e07d4e228d6e9e1038f1e4/analysis/src/statistics.cpp) · [covariance_analysis.cpp](https://github.com/ros-industrial/industrial_calibration/blob/c275104eef312ec5a5e07d4e228d6e9e1038f1e4/optimizations/src/covariance_analysis.cpp) · [camera_intrinsic_calibration_validation_utest.cpp](https://github.com/ros-industrial/industrial_calibration/blob/c275104eef312ec5a5e07d4e228d6e9e1038f1e4/test/camera_intrinsic_calibration_validation_utest.cpp) · [page_primer.dox](https://github.com/ros-industrial/industrial_calibration/blob/c275104eef312ec5a5e07d4e228d6e9e1038f1e4/docs/page_primer.dox) · [ubuntu.yml](https://github.com/ros-industrial/industrial_calibration/blob/c275104eef312ec5a5e07d4e228d6e9e1038f1e4/.github/workflows/ubuntu.yml) · [CHANGELOG.rst](https://github.com/ros-industrial/industrial_calibration/blob/c275104eef312ec5a5e07d4e228d6e9e1038f1e4/CHANGELOG.rst) |

<a id="n2-fastnt-epcis"></a>

### FasTnT EPCIS (bản .NET 5)

| Thuộc tính | Giá trị |
|---|---|
| Repo | https://github.com/FasTnT/epcis |
| License | Apache-2.0 |
| Phiên bản đã đọc | `18e1b71069c3363cad2401c74ce980525360c1ef` (commit 2022-03-18) |
| Kiểm chứng | 2026-11-24; code-read; đã đọc README, LICENSE, dotnetcore.yml, SimpleEventQuery.cs, EventFetcher.cs, WhenCapturingAnEvent.cs; chưa chạy upstream |
| Khoảng trống lấp | Truy xuất sự kiện chuỗi cung ứng EPCIS (serial/lô) cho chai khí |
| Cơ chế đáng học | - `src/FasTnT.Domain/Queries/SimpleEventQuery.cs`: bảng tên tham số chuẩn EPCIS (EQ_*, WD_*, orderBy, eventCountLimit…) cộng nhóm tham số theo regex, mỗi cái gắn một bộ lọc<br>- `src/FasTnT.Data.PostgreSql/Query/EventFetcher.cs`: dịch bộ lọc thành điều kiện SQL qua Dapper, ví dụ lọc EPC bằng `LIKE ANY` kèm loại EPC<br>- README liệt kê Capture, Poll, Subscribe/Unsubscribe, callback; tài liệu chuẩn GS1 và bộ Postman/SoapUI kèm theo trong `documents/` |
| Tiêu chí và cách kiểm | Workflow `dotnetcore.yml` (chạy khi push): build Release, dựng PostgreSQL, chạy unit test và integration test có coverage rồi gửi Codecov (đã mở workflow, tôi chưa chạy). Test tích hợp là mẫu đạt/không đạt theo từng điểm cuối (Capture, Poll, Subscribe, sai thông tin xác thực); không thấy kiểm tra tuân thủ EPCIS Conformance bằng máy. |
| Giới hạn và rủi ro | Apache-2.0. Repo gần như ngừng: commit cuối 2022-03-18; .NET 5 đã hết hỗ trợ; chỉ EPCIS 1.2 (không có 2.0/REST/JSON-LD); đây là nhánh cũ dùng Dapper, bản mới là epcis-ef-core (chưa kiểm). Mặc định HTTP Basic admin:P@ssw0rd theo README và test, phải đổi trước khi dùng. Mô tả trinh sát nêu bản fork hỗ trợ 1.2 và 2.0: không phải repo này. |
| So với | mes-open-openmes, factorysemantics-mes; kho chưa có repo EPCIS nào khác |
| Nguồn | [README.md](https://github.com/FasTnT/epcis/blob/18e1b71069c3363cad2401c74ce980525360c1ef/README.md) · [LICENSE](https://github.com/FasTnT/epcis/blob/18e1b71069c3363cad2401c74ce980525360c1ef/LICENSE) · [dotnetcore.yml](https://github.com/FasTnT/epcis/blob/18e1b71069c3363cad2401c74ce980525360c1ef/.github/workflows/dotnetcore.yml) · [SimpleEventQuery.cs](https://github.com/FasTnT/epcis/blob/18e1b71069c3363cad2401c74ce980525360c1ef/src/FasTnT.Domain/Queries/SimpleEventQuery.cs) · [EventFetcher.cs](https://github.com/FasTnT/epcis/blob/18e1b71069c3363cad2401c74ce980525360c1ef/src/FasTnT.Data.PostgreSql/Query/EventFetcher.cs) · [WhenCapturingAnEvent.cs](https://github.com/FasTnT/epcis/blob/18e1b71069c3363cad2401c74ce980525360c1ef/test/FasTnT.IntegrationTests/API/EpcisEndpoints/v1.2/XML/Capture/WhenCapturingAnEvent.cs) |

<a id="n2-liberu-maintenance"></a>

### Liberu Maintenance

| Thuộc tính | Giá trị |
|---|---|
| Repo | https://github.com/liberusoftware/project-maintenance-laravel-filament |
| License | MIT (© 2026 Liberu Software) |
| Phiên bản đã đọc | `f95e98993cf8dfe99f55d90f3f092610657748cc` (commit 2026-11-21) |
| Kiểm chứng | 2026-11-24; code-read; đã đọc README, LICENSE.md, SECURITY.md, tests.yml, preventative-maintenance module.json, GenerateWorkOrderFromPlan.php, CheckDueMaintenanceCommand.php; chưa chạy upstream |
| Khoảng trống lấp | Bảo trì CMMS có lệnh công việc, tài sản, bảo trì phòng ngừa tự host |
| Cơ chế đáng học | - `GenerateWorkOrderFromPlan.php`: kế hoạch bảo trì sinh lệnh công việc trong một giao dịch DB; từ chối kế hoạch không hoạt động và trả lại lệnh đang mở thay vì sinh trùng (lũy đẳng)<br>- `CheckDueMaintenanceCommand.php` (`maintenance:check-due --days=7`): gửi thông báo quá hạn và sắp đến hạn cho người được giao<br>- `modules/*/module.json` + `tests/Architecture/ModuleBoundariesTest.php`: manifest từng năng lực, phụ thuộc theo hướng, kiểm ranh giới giữa module; tài sản có đồng hồ đo và đọc cảm biến (`module-maintenance-assets`) |
| Tiêu chí và cách kiểm | `tests.yml`: `composer validate --strict`, `composer audit --locked`, Pint, PHPStan, `php artisan test` có coverage, rồi `scripts/verify-coverage` ép 100 phần trăm phạm vi release, gửi Codecov (đã mở workflow). Theo chú thích trong workflow, ngưỡng đó chỉ đo thư mục `app/` của host; mỗi module tự có cổng riêng, tôi không kiểm từng module. Không rõ có KPI bảo trì (MTBF/MTTR) hay không (chưa xác minh). |
| Giới hạn và rủi ro | MIT; không thấy telemetry trong phần đọc, nhưng stack có Telescope, Pulse, Horizon, Octane, Reverb, tích hợp analytics Google/Meta (module `analytics-google`, `analytics-meta`) cần rà khi tự host. Repo kéo theo mã module đã commit sẵn (1.9 nghìn file) và các file chỉ dẫn agent (AGENTS.md, CLAUDE.md, GEMINI.md) chỉ là nội dung, không áp dụng. Tên 'project-maintenance' và README là nền tảng chung chứ không riêng cho nhà máy; không có MES/OEE. |
| So với | oca-maintenance (module bảo trì Odoo), frappe-erpnext; cùng nhóm bảo trì CMMS với CMMS-OEE-Software (lô này) |
| Nguồn | [README.md](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/f95e98993cf8dfe99f55d90f3f092610657748cc/README.md) · [LICENSE.md](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/f95e98993cf8dfe99f55d90f3f092610657748cc/LICENSE.md) · [SECURITY.md](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/f95e98993cf8dfe99f55d90f3f092610657748cc/SECURITY.md) · [tests.yml](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/f95e98993cf8dfe99f55d90f3f092610657748cc/.github/workflows/tests.yml) · [module.json](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/f95e98993cf8dfe99f55d90f3f092610657748cc/modules/module-maintenance-preventative-maintenance/module.json) · [GenerateWorkOrderFromPlan.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/f95e98993cf8dfe99f55d90f3f092610657748cc/modules/module-maintenance-preventative-maintenance/src/Actions/GenerateWorkOrderFromPlan.php) · [CheckDueMaintenanceCommand.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/f95e98993cf8dfe99f55d90f3f092610657748cc/modules/module-maintenance-preventative-maintenance/src/Console/CheckDueMaintenanceCommand.php) |

<a id="n2-cmms-oee-software"></a>

### CMMS-OEE-Software

| Thuộc tính | Giá trị |
|---|---|
| Repo | https://github.com/opensourceoeesoftware/CMMS-OEE-Software |
| License | AGPL-3.0 (bản GNU Affero v3) |
| Phiên bản đã đọc | `ad0631c99e4d890855ef45b11a17792ce91ee4d3` (commit 2026-02-21) |
| Kiểm chứng | 2026-11-24; code-read; đã đọc README, LICENSE, push.yaml, backend/state/util.py, backend/db/models.py, backend/apiv1/tests.py; chưa chạy upstream |
| Khoảng trống lấp | MES/OEE nhẹ cho nhà máy chế tạo vừa và nhỏ |
| Cơ chế đáng học | - `backend/state/util.py` `calculate_oee`: ghép cặp sự kiện bắt đầu/tiếp tục (run–stop, fault–resume fault, failure, break in/out), cộng thời gian, tính Availability = run_time / planned_production_time, Performance = thời gian lý tưởng / run_time, Quality = (tổng − phế phẩm) / tổng, kẹp mỗi hệ số tối đa 1, OEE = tích × 100<br>- `backend/db/models.py`: `MaintenancePlan` (loại Planned/UnPlanned, ưu tiên, trạng thái, chi phí ước tính) gắn `Asset`; tín hiệu `post_save` đồng bộ trạng thái tài sản với trạng thái kế hoạch<br>- `backend/state/consumers.py` và routing: kênh WebSocket (Redis) cho dữ liệu trực tiếp |
| Tiêu chí và cách kiểm | Không có kiểm tra đúng đắn của OEE: 4 file `tests.py` đều chỉ là bản giả (đã đọc `apiv1/tests.py`; độ dài mỗi file 12–15 dòng). CI `push.yaml` (đã mở) dựng docker-compose rồi chạy `manage.py test`, nên xanh chỉ chứng minh dựng được; workflow còn tải Docker bằng `curl get.docker.com` và dùng khoá `pull_requests` (không phải khoá hợp lệ của GitHub, chưa xác minh tác dụng). |
| Giới hạn và rủi ro | AGPL-3.0: tự host nội bộ ít vướng, nhưng cung cấp dịch vụ qua mạng thì phải công bố mã nguồn bản sửa. README mời dùng tài khoản demo công khai (demo_user) và mẫu `.env` có `SECRET_KEY='django-insecure'`, DEBUG=True: không dùng nguyên trạng cho sản xuất. Trong `calculate_oee`, `planned_production_time = run − break_in + failure` rồi `run_time = planned − fault − failure` làm số failure triệt tiêu: có thể sai định nghĩa Availability (chưa xác minh bằng chạy). Bảo trì thưa: commit cuối 02/2026. |
| So với | oca-maintenance, mes-open-openmes, Liberu Maintenance (lô này) |
| Nguồn | [README.md](https://github.com/opensourceoeesoftware/CMMS-OEE-Software/blob/ad0631c99e4d890855ef45b11a17792ce91ee4d3/README.md) · [LICENSE](https://github.com/opensourceoeesoftware/CMMS-OEE-Software/blob/ad0631c99e4d890855ef45b11a17792ce91ee4d3/LICENSE) · [push.yaml](https://github.com/opensourceoeesoftware/CMMS-OEE-Software/blob/ad0631c99e4d890855ef45b11a17792ce91ee4d3/.github/workflows/push.yaml) · [util.py](https://github.com/opensourceoeesoftware/CMMS-OEE-Software/blob/ad0631c99e4d890855ef45b11a17792ce91ee4d3/backend/state/util.py) · [models.py](https://github.com/opensourceoeesoftware/CMMS-OEE-Software/blob/ad0631c99e4d890855ef45b11a17792ce91ee4d3/backend/db/models.py) · [tests.py](https://github.com/opensourceoeesoftware/CMMS-OEE-Software/blob/ad0631c99e4d890855ef45b11a17792ce91ee4d3/backend/apiv1/tests.py) |
