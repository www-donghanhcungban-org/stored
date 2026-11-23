<!-- File sinh tự động bởi scripts/build_catalog_views.py; sửa data/projects.json hoặc data/taxonomy.json rồi chạy lại. -->

# manufacturing — Kỹ thuật công trình & không gian

[← Mục lục catalog](../README.md) · 5 hồ sơ.

## MES/ERP cho xưởng sản xuất (`mes-erp`, 4)

| Dự án | Repo | License | ★ | Bằng chứng | Mục | Tóm tắt |
|---|---|---|---|---|---|---|
| [Carbon (crbnos)](../../38-industrial-quality-manufacturing/README.md#nt-crbnos-carbon) | `crbnos/carbon` | AGPL-3.0-only cho phần lõi; packages/ee và file có ".ee." trong tên theo Carbon Commercial License (cần giấy phép thương mại để chạy hoặc sửa); MIT cho packages/form, Apache-2.0 cho Gantt | 2.858 | đọc mã 2026-11-23 | 38 | ERP, MRP, MES và QMS trên một CSDL Postgres (monorepo TypeScript, tự host bằng Docker). |
| [OCA manufacture (Odoo MRP addons)](../../38-industrial-quality-manufacturing/README.md#nt-oca-manufacture) | `OCA/manufacture` | AGPL-3.0 (LICENSE gốc); module riêng AGPL-3 hoặc LGPL-3 | 285 | đọc mã 2026-11-23 | 38 | Bộ 31 addon của Odoo Community Association cho phân hệ sản xuất (MRP) của Odoo, nhánh mặc định 19.0 (chưa kiểm các nhánh phiên bản khác dù trinh sát nói nhiều phiên bản). |
| [OpenMES](../../38-industrial-quality-manufacturing/README.md#nt-mes-open-openmes) | `Mes-Open/OpenMes` | AGPL-3.0 cho lõi; AFL-3.0 cho thư mục modules (chỉ file có dòng thông báo AFL); có thêm giấy phép thương mại song song qua CLA | 206 | đọc mã 2026-11-23 | 38 | MES tự host (Laravel, Livewire, PostgreSQL) cho xưởng nhỏ: lệnh sản xuất, lịch kéo thả, Andon/issue, OEE, kiểm chất lượng theo mẫu, truy vết lô và serial, kết nối MQTT/M… |
| [FactorySemantics MES](../../38-industrial-quality-manufacturing/README.md#nt-factorysemantics-mes) | `factorysemantics/factorysemantics-mes` | Apache-2.0 | 20 | đọc mã 2026-11-23 | 38 | MES module quanh kernel (Python 3.12+, FastAPI, SQLite hoặc PostgreSQL): lệnh sản xuất, OPC UA, OEE, chất lượng kèm SPC, hiệu chuẩn, bảo trì, lập lịch, truy xuất theo se… |

## Bảo trì thiết bị (CMMS) (`maintenance-cmms`, 1)

| Dự án | Repo | License | ★ | Bằng chứng | Mục | Tóm tắt |
|---|---|---|---|---|---|---|
| [OCA maintenance (Odoo 19)](../../38-industrial-quality-manufacturing/README.md#nt-oca-maintenance) | `OCA/maintenance` | AGPL-3.0 (repo; vài module LGPL-3.0) | 120 | đọc mã 2026-11-23 | 38 | 22 addon bảo trì thiết bị cho Odoo 19: kế hoạch bảo trì định kỳ, phân cấp thiết bị, trạng thái, phiếu bảo trì gắn mua hàng, timesheet. |
