<!-- File sinh tự động bởi scripts/build_catalog_views.py; sửa data/projects.json hoặc data/taxonomy.json rồi chạy lại. -->

# Catalog theo nhóm, danh mục và danh mục con

Sinh từ `data/projects.json` (2786 hồ sơ) theo `data/taxonomy.json`. Mỗi dòng dẫn về hồ sơ gốc trong README chuyên mục; số sao và mức bằng chứng chỉ đúng tại ngày ghi trong hồ sơ. Sắp xếp theo ★ giảm dần; ★ để trống là chưa có số tin cậy.

Chọn công cụ theo tác vụ: xem [PLAYBOOK.md](../PLAYBOOK.md) (skill/tính năng đã chắt lọc kèm cách áp dụng) và [GUIDES.md](../GUIDES.md).

## AI agent, skill & điều phối (527)

| Danh mục | Số hồ sơ | Danh mục con |
|---|---|---|
| [coding-agent](ai-agents/coding-agent.md) | 26 | — |
| [coding-tool-commercial](ai-agents/coding-tool-commercial.md) | 6 | — |
| [agent-framework](ai-agents/agent-framework.md) | 51 | — |
| [agent-workspace](ai-agents/agent-workspace.md) | 34 | — |
| [personal-agent](ai-agents/personal-agent.md) | 23 | — |
| [autonomous-agent-history](ai-agents/autonomous-agent-history.md) | 3 | — |
| [pattern-loop](ai-agents/pattern-loop.md) | 15 | — |
| [reasoning-skill](ai-agents/reasoning-skill.md) | 2 | — |
| [context-optimization](ai-agents/context-optimization.md) | 7 | — |
| [agent-memory](ai-agents/agent-memory.md) | 20 | — |
| [harness-pack](ai-agents/harness-pack.md) | 71 | Quy trình coding/TDD/review (16), Điều phối nhiều agent (9), Văn phòng & tài liệu (2), Marketing, bán hàng & kinh doanh (16), Media & sáng tạo (5), Chuyên ngành (20), Tạo/quản lý skill (3) |
| [plugin-marketplace](ai-agents/plugin-marketplace.md) | 17 | — |
| [protocol](ai-agents/protocol.md) | 56 | — |
| [llm-gateway](ai-agents/llm-gateway.md) | 20 | — |
| [prompt](ai-agents/prompt.md) | 31 | — |
| [browser-agent](ai-agents/browser-agent.md) | 43 | — |
| [sandbox](ai-agents/sandbox.md) | 29 | — |
| [remote-access](ai-agents/remote-access.md) | 8 | — |
| [agentic-ui](ai-agents/agentic-ui.md) | 25 | — |
| [codebase-knowledge](ai-agents/codebase-knowledge.md) | 18 | — |
| [spec-driven](ai-agents/spec-driven.md) | 11 | — |
| [code-review](ai-agents/code-review.md) | 11 | — |

## Tự động hóa & quy trình (124)

| Danh mục | Số hồ sơ | Danh mục con |
|---|---|---|
| [workflow-automation](automation/workflow-automation.md) | 58 | — |
| [durable-execution](automation/durable-execution.md) | 15 | — |
| [low-code](automation/low-code.md) | 28 | — |
| [scheduling](automation/scheduling.md) | 10 | — |
| [project-management](automation/project-management.md) | 13 | — |

## Đánh giá, an toàn & chất lượng (345)

| Danh mục | Số hồ sơ | Danh mục con |
|---|---|---|
| [eval-observability](trust/eval-observability.md) | 79 | Eval LLM/agent (27), Tracing & observability LLM (14), Benchmark (20), Giám sát hệ thống (18) |
| [security](trust/security.md) | 102 | Quét lỗ hổng ứng dụng (11), Guardrail & an toàn agent (23), Secret & chuỗi cung ứng (34), Pentest & red team (16), Danh tính & truy cập (9), Quyền riêng tư (9) |
| [policy-as-code](trust/policy-as-code.md) | 11 | — |
| [quality-gate](trust/quality-gate.md) | 123 | Test unit/integration (28), E2E & trình duyệt (6), Visual regression & accessibility (19), Phân tích tĩnh & lint (23), Eval skill/agent (10), Hợp đồng API & schema (14), Hiệu năng & tải (16), Cổng phát hành & review (7) |
| [checklist](trust/checklist.md) | 30 | — |

## Mô hình, dữ liệu & tài liệu (376)

| Danh mục | Số hồ sơ | Danh mục con |
|---|---|---|
| [inference](models-data/inference.md) | 40 | — |
| [rag](models-data/rag.md) | 23 | — |
| [vector-db](models-data/vector-db.md) | 11 | — |
| [model-training](models-data/model-training.md) | 36 | — |
| [data-curation](models-data/data-curation.md) | 18 | — |
| [data](models-data/data.md) | 130 | Cơ sở dữ liệu & lưu trữ (37), BI & dashboard (8), Dataframe, notebook & xử lý (13), Pipeline, ETL & CDC (10), Lineage, metric & ontology (16), Text-to-SQL & agent dữ liệu (14), Thu thập dữ liệu web (6), Tài chính & định lượng (8), Thư viện ML & NLP (6), Thư viện trực quan hóa (4), Tìm kiếm & cache (8) |
| [document-intelligence](models-data/document-intelligence.md) | 25 | — |
| [computer-vision](models-data/computer-vision.md) | 27 | — |
| [image-gen](models-data/image-gen.md) | 12 | — |
| [speech](models-data/speech.md) | 54 | — |

## Thiết kế, giao diện & media (404)

| Danh mục | Số hồ sơ | Danh mục con |
|---|---|---|
| [ui-library](design-media/ui-library.md) | 106 | Component React (15), Component Vue/Svelte/Angular/khác (13), Design system chính thức của tổ chức (22), Primitive headless & accessibility (7), Component có animation (9), CSS framework (6), Biểu đồ & bản đồ (6), Editor & nhập liệu phong phú (8), Icon, font & tài sản (7), TUI & GUI native (10), Media player & upload (3) |
| [design-tool](design-media/design-tool.md) | 58 | Canvas & editor thiết kế (15), Design-to-code & MCP thiết kế (10), Gallery cảm hứng (13), Token, màu & chữ (8), Minh họa & sơ đồ (12) |
| [design-skill](design-media/design-skill.md) | 56 | — |
| [layout-template](design-media/layout-template.md) | 20 | — |
| [ai-ui-generator](design-media/ai-ui-generator.md) | 8 | — |
| [animation-library](design-media/animation-library.md) | 28 | — |
| [motion-design](design-media/motion-design.md) | 34 | — |
| [video-engine](design-media/video-engine.md) | 39 | — |
| [agentic-video](design-media/agentic-video.md) | 55 | — |

## Kỹ thuật phần mềm & vận hành (502)

| Danh mục | Số hồ sơ | Danh mục con |
|---|---|---|
| [frontend](software/frontend.md) | 90 | Framework UI (23), Build, bundler & monorepo (9), State & data fetching (9), CSS & styling (6), Ngôn ngữ & runtime JS/TS (4), App desktop/đa nền tảng (6), Game engine & đồ họa (4), Thư viện tiện ích (24), Template & starter (5) |
| [backend](software/backend.md) | 159 | Web framework (30), BaaS & nền tảng backend (6), Xác thực & danh tính (20), API, RPC & client (22), ORM, migration & công cụ CSDL (7), CMS & thương mại điện tử (16), Ứng dụng doanh nghiệp (ERP/CRM) (12), Ngôn ngữ & runtime (14), Microservice, cấu hình & service mesh (13), Ứng dụng tự host (8), Realtime, bot & nhắn tin (11) |
| [mobile](software/mobile.md) | 39 | — |
| [devops](software/devops.md) | 169 | Container & Kubernetes (17), IaC & quản lý cấu hình (5), CI/CD & phát hành (8), PaaS tự host & bảng điều khiển server (7), Mạng, proxy, DNS & chứng chỉ (8), Sao lưu, chi phí & vận hành hạ tầng (7), Terminal, shell & công cụ dòng lệnh (43), Editor & IDE (16), Môi trường dev & quản lý toolchain (26), Hệ điều hành & công cụ hệ thống (17), Ứng dụng tự host (ảnh, git, file...) (9), Bảo mật CI & chuỗi cung ứng (6) |
| [localization](software/localization.md) | 9 | — |
| [reverse-engineering](software/reverse-engineering.md) | 8 | — |
| [app-launcher](software/app-launcher.md) | 5 | — |
| [feature-management](software/feature-management.md) | 6 | — |
| [product-analytics](software/product-analytics.md) | 10 | — |
| [product-research](software/product-research.md) | 7 | — |

## Học tập, tài liệu & tri thức (398)

| Danh mục | Số hồ sơ | Danh mục con |
|---|---|---|
| [learning](knowledge/learning.md) | 167 | Khóa học LLM/GenAI & deep learning (36), Khóa học/hướng dẫn agent & Claude Code (15), Nền tảng khoa học máy tính (17), Học ngôn ngữ lập trình (29), Phỏng vấn & thuật toán (25), Thiết kế hệ thống & kiến trúc (6), Dự án mẫu & cookbook (15), Tham chiếu thiết kế UI/UX (3), Học bảo mật (7), Lộ trình, sách & tài liệu tổng hợp (14) |
| [awesome-list](knowledge/awesome-list.md) | 85 | Skill, plugin & agent (15), MCP server (3), Thiết kế & UI (12), Hệ sinh thái ngôn ngữ/framework (13), Dữ liệu & ML (10), DevOps & sysadmin (5), Bảo mật (4), Marketing & tăng trưởng (4), Tài nguyên chung & xếp hạng (19) |
| [docs](knowledge/docs.md) | 104 | Site tài liệu (21), Kiểm tài liệu (lint, link, chính tả) (10), Tài liệu cho agent (llms.txt, context) (6), Sơ đồ & hình vẽ (5), Slide & trình chiếu (7), Ghi chú & knowledge base (21), Office, bảng tính & PDF (11), Soạn thảo & xuất bản (Markdown, Typst) (11), Ứng dụng năng suất (12) |
| [vietnam](knowledge/vietnam.md) | 27 | — |
| [own-repo](knowledge/own-repo.md) | 15 | — |

## Kỹ thuật công trình & không gian (73)

| Danh mục | Số hồ sơ | Danh mục con |
|---|---|---|
| [cad-bim](engineering/cad-bim.md) | 23 | — |
| [geospatial](engineering/geospatial.md) | 22 | — |
| [simulation](engineering/simulation.md) | 9 | — |
| [quality-mgmt](engineering/quality-mgmt.md) | 8 | Hệ thống quản lý chất lượng ISO (đánh giá, CAPA, rủi ro) (2), SPC, MSA và kiểm soát quá trình (5), Hàn, NDT và hồ sơ chứng nhận (1), Hiệu chuẩn và truy xuất nguồn gốc (0) |
| [manufacturing](engineering/manufacturing.md) | 11 | MES/ERP cho xưởng sản xuất (7), Bảo trì thiết bị (CMMS) (4) |

## Ứng dụng người dùng cuối (37)

| Danh mục | Số hồ sơ | Danh mục con |
|---|---|---|
| [desktop-utility](end-user/desktop-utility.md) | 37 | — |
