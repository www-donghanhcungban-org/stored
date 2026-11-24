<!-- File sinh tự động bởi scripts/build_catalog_views.py; sửa data/projects.json hoặc data/taxonomy.json rồi chạy lại. -->

# quality-mgmt — Kỹ thuật công trình & không gian

[← Mục lục catalog](../README.md) · 8 hồ sơ.

## Hệ thống quản lý chất lượng ISO (đánh giá, CAPA, rủi ro) (`qms-iso`, 2)

| Dự án | Repo | License | ★ | Bằng chứng | Mục | Tóm tắt |
|---|---|---|---|---|---|---|
| [Odoo QMS ISO 9001 (TMC Rosario)](../../38-industrial-quality-manufacturing/README.md#nt-odoo-qms-iso9001) | `jonaesantos/odoo-qms-iso9001` | AGPL-3.0 | 30 | đọc mã 2026-11-23 | 38 | Addon Odoo 14 (34 model) lưu dữ liệu cho ISO 9001: đánh giá nội bộ, phát hiện, hành động kèm kiểm tra hiệu lực, rủi ro 5x5, mục tiêu, xem xét lãnh đạo, tài liệu có phiên… |
| [OpenQMS (Open-Industry-System)](../../38-industrial-quality-manufacturing/README.md#nt-openqms) | `Open-Industry-System/OpenQMS` | MIT | 22 | đọc mã 2026-11-23 | 38 | QMS sản xuất (FastAPI, React, PostgreSQL, Neo4j) nhắm IATF 16949: PFMEA, SPC X-bar R và I-MR kèm tám luật Western Electric và Cp/Cpk, MSA, IQC theo AQL, 8D bằng state ma… |

## SPC, MSA và kiểm soát quá trình (`spc-msa`, 5)

| Dự án | Repo | License | ★ | Bằng chứng | Mục | Tóm tắt |
|---|---|---|---|---|---|---|
| [PowerBI-SPC (WA Health)](../../38-industrial-quality-manufacturing/README.md#nt-aus-doh-powerbi-spc) | `AUS-DOH-Safety-and-Quality/PowerBI-SPC` | GPL-3.0 (LICENSE.md); bản cài từ AppSource kèm EULA.pdf của Microsoft cho Power BI visual | 76 | đọc mã 2026-11-23 | 38 | Visual tùy chỉnh cho Power BI vẽ biểu đồ kiểm soát SPC (run, i, mr, p, p', u, u', c, xbar, s, g, t), chạy hoàn toàn trong Power BI, nguồn gốc là Bộ Y tế Tây Úc (chuẩn y… |
| [pyshewhart](../../38-industrial-quality-manufacturing/README.md#nt-huft-jonathan-pyshewhart) | `huft-jonathan/pyshewhart` | MIT | 34 | đọc mã 2026-11-23 | 38 | Thư viện Python nhỏ (khoảng 1400 dòng) vẽ biểu đồ X-bar và R, X-bar và S, CUSUM, P-attribute bằng matplotlib, hằng số lấy từ Montgomery 2005, kèm kiểm tra luật Western E… |
| [ASPC](../../38-industrial-quality-manufacturing/README.md#n2-aspc) | `M1ndSmith/ASPC` | MIT | 15 | đọc mã 2026-11-23 | 38 | Hệ SPC Python (lõi thuần `spc_core` + FastAPI/CLI + dashboard Next.js + stream Redpanda/MQTT/TimescaleDB) với pipeline Phase I có cổng ok/warn/stop, đóng băng giới hạn c… |
| [Six Sigma in R (skill)](../../38-industrial-quality-manufacturing/README.md#n2-six-sigma-r-skill) | `robustagile/six-sigma-in-r-skill` | Apache-2.0 | 12 | đọc mã 2026-11-23 | 38 | Skill cho Claude Code/Codex sinh mã R cho SPC, Cp/Cpk/Pp/Ppk, DPMO, kiểm định giả thuyết, ANOVA, power. |
| [shewhart-mcp](../../38-industrial-quality-manufacturing/README.md#nt-shewhart-mcp) | `bertanucar/shewhart-mcp` | — | 3 | đọc tài liệu 2026-11-23 | 38 | Repo chỉ là bản giữ tên gói (0.0.1, Pre-Alpha): chưa có máy chủ MCP nào chạy, `__init__.py` chỉ khai báo tuple `PLANNED_TOOLS` (review, control_chart, capability, tolera… |

## Hàn, NDT và hồ sơ chứng nhận (`welding-ndt`, 1)

| Dự án | Repo | License | ★ | Bằng chứng | Mục | Tóm tắt |
|---|---|---|---|---|---|---|
| [WelDX](../../38-industrial-quality-manufacturing/README.md#n2-weldx) | `BAMWelDX/weldx` | BSD-3-Clause | 31 | đọc mã 2026-11-23 | 38 | Định dạng dữ liệu hàn có schema và đơn vị (ASDF), có kiểu rãnh ISO 9692-1; |
