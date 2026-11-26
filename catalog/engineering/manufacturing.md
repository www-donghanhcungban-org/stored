<!-- File sinh tự động bởi scripts/build_catalog_views.py; sửa data/projects.json hoặc data/taxonomy.json rồi chạy lại. -->

# manufacturing — Kỹ thuật công trình & không gian

[← Mục lục catalog](../README.md) · 11 hồ sơ.

## MES/ERP cho xưởng sản xuất (`mes-erp`, 7)

| Dự án | Repo | License | ★ | Bằng chứng | Mục | Tóm tắt |
|---|---|---|---|---|---|---|
| [Carbon (crbnos)](../../38-industrial-quality-manufacturing/README.md#nt-crbnos-carbon) | `crbnos/carbon` | AGPL-3.0-only cho phần lõi; packages/ee và file có ".ee." trong tên theo Carbon Commercial License (cần giấy phép thương mại để chạy hoặc sửa); MIT cho packages/form, Apache-2.0 cho Gantt | 2.858 | đọc mã 2026-11-23 | 38 | ERP, MRP, MES và QMS trên một CSDL Postgres (monorepo TypeScript, tự host bằng Docker). |
| [node-opcua](../../38-industrial-quality-manufacturing/README.md#n2-node-opcua) | `node-opcua/node-opcua` | MIT | 1.673 | đọc mã 2026-11-23 | 38 | Thư viện OPC UA TypeScript đầy đủ, MIT, bảo mật chứng chỉ; |
| [qcadoo MES](../../38-industrial-quality-manufacturing/README.md#n2-qcadoo-mes) | `qcadoo/mes` | AGPL-3.0-or-later (README và header LICENSE.txt; không có văn bản AGPL đầy đủ) | 954 | đọc mã 2026-11-23 | 38 | MES Java kiểu plugin với máy trạng thái AOP và đếm sản lượng; |
| [OCA manufacture (Odoo MRP addons)](../../38-industrial-quality-manufacturing/README.md#nt-oca-manufacture) | `OCA/manufacture` | AGPL-3.0 (LICENSE gốc); module riêng AGPL-3 hoặc LGPL-3 | 285 | đọc mã 2026-11-23 | 38 | Bộ 31 addon của Odoo Community Association cho phân hệ sản xuất (MRP) của Odoo, nhánh mặc định 19.0 (chưa kiểm các nhánh phiên bản khác dù trinh sát nói nhiều phiên bản). |
| [OpenMES](../../38-industrial-quality-manufacturing/README.md#nt-mes-open-openmes) | `Mes-Open/OpenMes` | AGPL-3.0 cho lõi; AFL-3.0 cho thư mục modules (chỉ file có dòng thông báo AFL); có thêm giấy phép thương mại song song qua CLA | 206 | đọc mã 2026-11-23 | 38 | MES tự host (Laravel, Livewire, PostgreSQL) cho xưởng nhỏ: lệnh sản xuất, lịch kéo thả, Andon/issue, OEE, kiểm chất lượng theo mẫu, truy vết lô và serial, kết nối MQTT/M… |
| [FasTnT EPCIS (bản .NET 5)](../../38-industrial-quality-manufacturing/README.md#n2-fastnt-epcis) | `FasTnT/epcis` | Apache-2.0 | 25 | đọc mã 2026-11-23 | 38 | Kho sự kiện GS1 EPCIS 1.2 viết bằng C# (.NET 5) lưu PostgreSQL: nhận sự kiện qua XML, truy vấn SOAP (SimpleEventQuery, master data), đăng ký nhận kết quả. |
| [FactorySemantics MES](../../38-industrial-quality-manufacturing/README.md#nt-factorysemantics-mes) | `factorysemantics/factorysemantics-mes` | Apache-2.0 | 20 | đọc mã 2026-11-23 | 38 | MES module quanh kernel (Python 3.12+, FastAPI, SQLite hoặc PostgreSQL): lệnh sản xuất, OPC UA, OEE, chất lượng kèm SPC, hiệu chuẩn, bảo trì, lập lịch, truy xuất theo se… |

## Bảo trì thiết bị (CMMS) (`maintenance-cmms`, 4)

| Dự án | Repo | License | ★ | Bằng chứng | Mục | Tóm tắt |
|---|---|---|---|---|---|---|
| [Atlas CMMS (Grashjs)](../../38-industrial-quality-manufacturing/README.md#n2-atlas-cmms) | `Grashjs/cmms` | AGPL-3.0 (song song giấy phép thương mại) | 875 | đọc mã 2026-11-23 | 38 | CMMS độc lập Spring Boot với lịch PM Quartz và cơ chế giới hạn theo giấy phép (entitlement qua Keygen); |
| [OCA maintenance (Odoo 19)](../../38-industrial-quality-manufacturing/README.md#nt-oca-maintenance) | `OCA/maintenance` | AGPL-3.0 (repo; vài module LGPL-3.0) | 120 | đọc mã 2026-11-23 | 38 | 22 addon bảo trì thiết bị cho Odoo 19: kế hoạch bảo trì định kỳ, phân cấp thiết bị, trạng thái, phiếu bảo trì gắn mua hàng, timesheet. |
| [Liberu Maintenance](../../38-industrial-quality-manufacturing/README.md#n2-liberu-maintenance) | `liberusoftware/project-maintenance-laravel-filament` | MIT | 75 | đọc mã 2026-11-23 | 38 | Ứng dụng Laravel 13/Filament 5 lắp từ nhiều module Composer độc lập (tài sản, lệnh công việc, bảo trì phòng ngừa, kho, mua sắm, kiểm tra, lập lịch, báo cáo, cổng khách…)… |
| [CMMS-OEE-Software](../../38-industrial-quality-manufacturing/README.md#n2-cmms-oee-software) | `opensourceoeesoftware/CMMS-OEE-Software` | AGPL-3.0 | 6 | đọc mã 2026-11-23 | 38 | Ứng dụng Django + React + PostgreSQL gộp tính OEE (từ sự kiện máy run/stop/fault/failure/break và báo cáo sản lượng/phế phẩm) với CMMS đơn giản (tài sản, kế hoạch bảo tr… |
