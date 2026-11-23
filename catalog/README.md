<!-- File sinh tự động bởi scripts/build_catalog_views.py; sửa data/projects.json hoặc data/taxonomy.json rồi chạy lại. -->

# Catalog theo nhóm, danh mục và danh mục con

Sinh từ `data/projects.json` (2330 hồ sơ) theo `data/taxonomy.json`. Mỗi dòng dẫn về hồ sơ gốc trong README chuyên mục; số sao và mức bằng chứng chỉ đúng tại ngày ghi trong hồ sơ. Sắp xếp theo ★ giảm dần; ★ để trống là chưa có số tin cậy.

Chọn công cụ theo tác vụ: xem [PLAYBOOK.md](../PLAYBOOK.md) (skill/tính năng đã chắt lọc kèm cách áp dụng) và [GUIDES.md](../GUIDES.md).

## AI agent, skill & điều phối (460)

| Danh mục | Số hồ sơ | Danh mục con |
|---|---|---|
| [coding-agent](ai-agents/coding-agent.md) | 26 | — |
| [coding-tool-commercial](ai-agents/coding-tool-commercial.md) | 6 | — |
| [agent-framework](ai-agents/agent-framework.md) | 46 | — |
| [agent-workspace](ai-agents/agent-workspace.md) | 33 | — |
| [personal-agent](ai-agents/personal-agent.md) | 23 | — |
| [autonomous-agent-history](ai-agents/autonomous-agent-history.md) | 3 | — |
| [pattern-loop](ai-agents/pattern-loop.md) | 15 | — |
| [reasoning-skill](ai-agents/reasoning-skill.md) | 2 | — |
| [context-optimization](ai-agents/context-optimization.md) | 6 | — |
| [agent-memory](ai-agents/agent-memory.md) | 19 | — |
| [harness-pack](ai-agents/harness-pack.md) | 52 | Quy trình coding/TDD/review (15), Điều phối nhiều agent (9), Văn phòng & tài liệu (0), Marketing, bán hàng & kinh doanh (16), Media & sáng tạo (2), Chuyên ngành (7), Tạo/quản lý skill (3) |
| [plugin-marketplace](ai-agents/plugin-marketplace.md) | 13 | — |
| [protocol](ai-agents/protocol.md) | 46 | — |
| [llm-gateway](ai-agents/llm-gateway.md) | 18 | — |
| [prompt](ai-agents/prompt.md) | 30 | — |
| [browser-agent](ai-agents/browser-agent.md) | 41 | — |
| [sandbox](ai-agents/sandbox.md) | 21 | — |
| [remote-access](ai-agents/remote-access.md) | 6 | — |
| [agentic-ui](ai-agents/agentic-ui.md) | 24 | — |
| [codebase-knowledge](ai-agents/codebase-knowledge.md) | 18 | — |
| [spec-driven](ai-agents/spec-driven.md) | 7 | — |
| [code-review](ai-agents/code-review.md) | 5 | — |

## Tự động hóa & quy trình (92)

| Danh mục | Số hồ sơ | Danh mục con |
|---|---|---|
| [workflow-automation](automation/workflow-automation.md) | 36 | — |
| [durable-execution](automation/durable-execution.md) | 15 | — |
| [low-code](automation/low-code.md) | 27 | — |
| [scheduling](automation/scheduling.md) | 5 | — |
| [project-management](automation/project-management.md) | 9 | — |

## Đánh giá, an toàn & chất lượng (251)

| Danh mục | Số hồ sơ | Danh mục con |
|---|---|---|
| [eval-observability](trust/eval-observability.md) | 68 | Eval LLM/agent (23), Tracing & observability LLM (13), Benchmark (15), Giám sát hệ thống (17) |
| [security](trust/security.md) | 62 | Quét lỗ hổng ứng dụng (5), Guardrail & an toàn agent (13), Secret & chuỗi cung ứng (17), Pentest & red team (16), Danh tính & truy cập (7), Quyền riêng tư (4) |
| [policy-as-code](trust/policy-as-code.md) | 4 | — |
| [quality-gate](trust/quality-gate.md) | 88 | Test unit/integration (15), E2E & trình duyệt (6), Visual regression & accessibility (15), Phân tích tĩnh & lint (21), Eval skill/agent (6), Hợp đồng API & schema (8), Hiệu năng & tải (10), Cổng phát hành & review (7) |
| [checklist](trust/checklist.md) | 29 | — |

## Mô hình, dữ liệu & tài liệu (321)

| Danh mục | Số hồ sơ | Danh mục con |
|---|---|---|
| [inference](models-data/inference.md) | 33 | — |
| [rag](models-data/rag.md) | 22 | — |
| [vector-db](models-data/vector-db.md) | 9 | — |
| [model-training](models-data/model-training.md) | 34 | — |
| [data-curation](models-data/data-curation.md) | 12 | — |
| [data](models-data/data.md) | 109 | Cơ sở dữ liệu & lưu trữ (30), BI & dashboard (5), Dataframe, notebook & xử lý (10), Pipeline, ETL & CDC (7), Lineage, metric & ontology (12), Text-to-SQL & agent dữ liệu (14), Thu thập dữ liệu web (6), Tài chính & định lượng (8), Thư viện ML & NLP (5), Thư viện trực quan hóa (4), Tìm kiếm & cache (8) |
| [document-intelligence](models-data/document-intelligence.md) | 17 | — |
| [computer-vision](models-data/computer-vision.md) | 25 | — |
| [image-gen](models-data/image-gen.md) | 11 | — |
| [speech](models-data/speech.md) | 49 | — |

## Thiết kế, giao diện & media (371)

| Danh mục | Số hồ sơ | Danh mục con |
|---|---|---|
| [ui-library](design-media/ui-library.md) | 106 | Component React (15), Component Vue/Svelte/Angular/khác (13), Design system chính thức của tổ chức (22), Primitive headless & accessibility (7), Component có animation (9), CSS framework (6), Biểu đồ & bản đồ (6), Editor & nhập liệu phong phú (8), Icon, font & tài sản (7), TUI & GUI native (10), Media player & upload (3) |
| [design-tool](design-media/design-tool.md) | 58 | Canvas & editor thiết kế (15), Design-to-code & MCP thiết kế (10), Gallery cảm hứng (13), Token, màu & chữ (8), Minh họa & sơ đồ (12) |
| [design-skill](design-media/design-skill.md) | 55 | — |
| [layout-template](design-media/layout-template.md) | 20 | — |
| [ai-ui-generator](design-media/ai-ui-generator.md) | 8 | — |
| [animation-library](design-media/animation-library.md) | 24 | — |
| [motion-design](design-media/motion-design.md) | 33 | — |
| [video-engine](design-media/video-engine.md) | 26 | — |
| [agentic-video](design-media/agentic-video.md) | 41 | — |

## Kỹ thuật phần mềm & vận hành (428)

| Danh mục | Số hồ sơ | Danh mục con |
|---|---|---|
| [frontend](software/frontend.md) | 82 | Framework UI (23), Build, bundler & monorepo (9), State & data fetching (6), CSS & styling (6), Ngôn ngữ & runtime JS/TS (4), App desktop/đa nền tảng (6), Game engine & đồ họa (4), Thư viện tiện ích (22), Template & starter (2) |
| [backend](software/backend.md) | 122 | Web framework (26), BaaS & nền tảng backend (6), Xác thực & danh tính (5), API, RPC & client (20), ORM, migration & công cụ CSDL (5), CMS & thương mại điện tử (11), Ứng dụng doanh nghiệp (ERP/CRM) (11), Ngôn ngữ & runtime (14), Microservice, cấu hình & service mesh (9), Ứng dụng tự host (8), Realtime, bot & nhắn tin (7) |
| [mobile](software/mobile.md) | 26 | — |
| [devops](software/devops.md) | 162 | Container & Kubernetes (17), IaC & quản lý cấu hình (5), CI/CD & phát hành (7), PaaS tự host & bảng điều khiển server (7), Mạng, proxy, DNS & chứng chỉ (8), Sao lưu, chi phí & vận hành hạ tầng (6), Terminal, shell & công cụ dòng lệnh (43), Editor & IDE (16), Môi trường dev & quản lý toolchain (26), Hệ điều hành & công cụ hệ thống (17), Ứng dụng tự host (ảnh, git, file...) (9), Bảo mật CI & chuỗi cung ứng (1) |
| [localization](software/localization.md) | 7 | — |
| [reverse-engineering](software/reverse-engineering.md) | 7 | — |
| [app-launcher](software/app-launcher.md) | 5 | — |
| [feature-management](software/feature-management.md) | 2 | — |
| [product-analytics](software/product-analytics.md) | 8 | — |
| [product-research](software/product-research.md) | 7 | — |

## Học tập, tài liệu & tri thức (340)

| Danh mục | Số hồ sơ | Danh mục con |
|---|---|---|
| [learning](knowledge/learning.md) | 141 | Khóa học LLM/GenAI & deep learning (35), Khóa học/hướng dẫn agent & Claude Code (15), Nền tảng khoa học máy tính (14), Học ngôn ngữ lập trình (20), Phỏng vấn & thuật toán (20), Thiết kế hệ thống & kiến trúc (6), Dự án mẫu & cookbook (13), Tham chiếu thiết kế UI/UX (3), Học bảo mật (2), Lộ trình, sách & tài liệu tổng hợp (13) |
| [awesome-list](knowledge/awesome-list.md) | 84 | Skill, plugin & agent (15), MCP server (3), Thiết kế & UI (12), Hệ sinh thái ngôn ngữ/framework (13), Dữ liệu & ML (10), DevOps & sysadmin (5), Bảo mật (4), Marketing & tăng trưởng (4), Tài nguyên chung & xếp hạng (18) |
| [docs](knowledge/docs.md) | 82 | Site tài liệu (17), Kiểm tài liệu (lint, link, chính tả) (6), Tài liệu cho agent (llms.txt, context) (5), Sơ đồ & hình vẽ (5), Slide & trình chiếu (7), Ghi chú & knowledge base (14), Office, bảng tính & PDF (8), Soạn thảo & xuất bản (Markdown, Typst) (11), Ứng dụng năng suất (9) |
| [vietnam](knowledge/vietnam.md) | 18 | — |
| [own-repo](knowledge/own-repo.md) | 15 | — |

## Kỹ thuật công trình & không gian (37)

| Danh mục | Số hồ sơ | Danh mục con |
|---|---|---|
| [cad-bim](engineering/cad-bim.md) | 19 | — |
| [geospatial](engineering/geospatial.md) | 14 | — |
| [simulation](engineering/simulation.md) | 4 | — |

## Ứng dụng người dùng cuối (30)

| Danh mục | Số hồ sơ | Danh mục con |
|---|---|---|
| [desktop-utility](end-user/desktop-utility.md) | 30 | — |
