# 02 · Agent Frameworks & LLM Orchestration

> **Cập nhật 24/11/2026:** `microsoft/agent-framework` đã được loại khỏi catalog vì chưa kiểm được repo tại commit xác định. Tài liệu Microsoft Learn vẫn được giữ như nguồn tham khảo; các nhận định cũ không chứng minh trạng thái repo hiện tại.

> Thư viện để xây agent/multi-agent và ứng dụng LLM. Số sao ước lượng 8–10/2026.

## 1. Bảng tổng hợp

| Framework | Repo | Ngôn ngữ | ★ (ước lượng) | Mô hình tư duy | Khi nào dùng |
|---|---|---|---|---|---|
| **LangChain** | langchain-ai/langchain | Py/TS | ~130k | Chuỗi, tool, retriever; hệ sinh thái lớn nhất | Prototype nhanh, nhiều tích hợp |
| **LangGraph** | langchain-ai/langgraph | Py/TS | ~40k · **34.5M tải/tháng** | Đồ thị trạng thái (state graph), checkpoint, human-in-the-loop | Agent production cần kiểm soát luồng, durable |
| **AutoGen → Microsoft Agent Framework** | microsoft/autogen · microsoft/agent-framework | Py/.NET | ~60k (AutoGen, maintenance) | Hội thoại đa agent; hợp nhất AutoGen + Semantic Kernel, GA 1.0 4/2026 | Doanh nghiệp .NET/Azure |
| **CrewAI** | crewAIInc/crewAI | Py | ~57k · 5.2M tải/tháng | Vai trò (role) + nhiệm vụ + crew | Đội agent theo vai trò, dễ lên |
| **OpenAI Agents SDK** | openai/openai-agents-python | Py/TS | ~29k · 10.3M tải/tháng | Agents, handoffs, guardrails, tracing | Dùng OpenAI/Responses API |
| **LlamaIndex** | run-llama/llama_index | Py/TS | ~48k | Data framework (RAG), workflows | RAG trên dữ liệu doanh nghiệp |
| **Semantic Kernel** | microsoft/semantic-kernel | .NET/Py/Java | ~28k | Plugins, planners | Đang hợp vào Agent Framework |
| **smolagents** | huggingface/smolagents | Py | ~26k | Code-agent tối giản (agent viết Python để hành động) | Nhẹ, HF ecosystem |
| **Haystack** | deepset-ai/haystack | Py | ~20k | Pipeline component hóa | RAG/search production |
| **PydanticAI** | pydantic/pydantic-ai | Py | ~16k | Typed, dependency injection, validation | Team ưa type-safety |
| **Google ADK** | google/adk-python | Py/Java | – | Agent Development Kit, A2A native | Gemini/Vertex |
| **Mastra** | mastra-ai/mastra | TS | – | Agent framework TS, workflows, evals | Next.js/TS stack |
| **OpenClaw** | openclaw/openclaw | TS | **~390k** | Trợ lý cá nhân tự host, nối Discord/Slack/Telegram/WhatsApp, skills module | Agent cá nhân; tác giả Peter Steinberger gia nhập OpenAI 2/2026, dự án về foundation độc lập |
| **Hermes Agent** | NousResearch/hermes-agent | Py | – | Agent mã mở chạy CLI/TUI/Electron + gateway Telegram/Discord/Slack/WhatsApp + ACP cho IDE; skills tự học, memory, `delegate_task` (≤10 con, **không lồng**), kanban, cron, webhook, plugin model-provider | Chủ kho dùng thật (mục 23 §5): provider Antigravity/`claude -p`/Codex CLI, 112 skill; docs `llms.txt` |
| **MetaGPT** | FoundationAgents/MetaGPT | Py | ~70,8k (trang GitHub 12/10/2026) | "Công ty phần mềm" đa vai trò: SOP → PRD/design/code; MGX | Khung "công ty AI" đầu tiên |
| **ChatDev** | OpenBMB/ChatDev | Py | ~34,5k (12/10/2026) | Chat-chain giữa các vai trò CEO/CTO/dev/tester | Nghiên cứu, nhỏ gọn |
| **DeerFlow** | bytedance/deer-flow | Py/TS | ~83,7k (12/10/2026) | Deep research đa agent trên LangGraph, planner + coordinator | X-Agents đối chiếu (mục 23 §3.1) |
| **AG2** (ex-AutoGen fork) | ag2ai/ag2 | Py | – | Fork cộng đồng của AutoGen 0.2 | Tách khỏi Microsoft 11/2024 |
| **CAMEL** | camel-ai/camel | Py | ~13k (nt.) | Role-playing agent, data gen, OWL | Học thuật |
| **agency-swarm** | VRSEN/agency-swarm | Py | – | Agency = agent có vai trò + luồng giao tiếp định nghĩa sẵn | Trên OpenAI Assistants/Agents SDK |
| **gpt-pilot** | Pythagora-io/gpt-pilot | Py/TS | ~33,6k (12/10/2026) | Dev AI theo bước, hỏi người khi kẹt | **Ngừng bảo trì**; cảnh báo mã độc trong `core/telemetry/` (8/2025–6/2026) **(chưa xác minh)** |
| **ruflo** (claude-flow) | ruvnet/ruflo | TS | – | Swarm orchestration cho Claude Code, hive-mind, MCP tools | Nhiều tuyên bố hiệu năng **chưa kiểm chứng** |
| **Paperclip** | paperclipai/paperclip | TS | ~100,5k (12/10/2026) | "Quản lý agent như nhân viên": org chart, budget, heartbeat; `npx paperclipai onboard` | Lớn nhất họ "công ty AI" 2026 |
| **OpenOPC** | HKUDS/OpenOPC | Py | ~1,8k (12/10/2026) | "One-person company": tự dựng org chart, uỷ việc cho Claude Code/Codex/Cursor | Mới, mỏng |
| **OpenCompany** (ex-MachinaOS) | zeenie-ai/OpenCompany | Py + TS | ~995 (12/10/2026) | App desktop/self-host: nhân viên AI = lead + specialist trên canvas, trigger email/chat/lịch, Temporal, 86 SKILL.md | Xem §4; theo dõi, chưa khuyến nghị production |

## 2. Phân tích

- **Sao ≠ dùng thật**: AutoGen nhiều sao nhất nhưng ở chế độ bảo trì; LangGraph ít sao hơn nhưng dẫn đầu mọi chỉ số adoption.
- **Hợp nhất**: Microsoft gom AutoGen + Semantic Kernel; LangChain tách phần agent sang LangGraph; OpenAI tự làm SDK → xu hướng "mỗi nhà cung cấp model có SDK agent riêng + 1–2 framework trung lập".
- **Chuẩn chung thay framework**: MCP (tool), A2A (agent-agent), AG-UI (UI) khiến việc chọn framework ít "khóa chặt" hơn trước.
- **"Công ty AI" là một họ riêng** (MetaGPT, ChatDev, gpt-pilot, agency-swarm, DeerFlow; so sánh trong `X-Agents/docs/reports/2026-10-10-doi-chieu-12-repo-co-che.md`): điểm chung là vai trò + SOP + artifact trung gian; bài học từ X-Agents (mục 23 §3.1) là **model quyết định, code hành động** — mọi trường "đã làm" do code điền, không tin lời khai của model.
- **Hermes Agent** là framework agent cá nhân gần OpenClaw nhất nhưng mở hơn về provider (plugin model-provider, CLI thuê bao làm backend) — xem mục 23 §5.
- **Tiêu chí chọn**: (1) kiểm soát luồng & durable execution (LangGraph), (2) tốc độ lên demo (CrewAI), (3) type-safety (PydanticAI), (4) hệ sinh thái cloud (ADK/Agent Framework), (5) khối lượng phụ thuộc (smolagents).

## 4. Case study: zeenie-ai/OpenCompany – "nhân viên AI" đóng gói thành sản phẩm (link từ người dùng, 2026-10-12)

### Hồ sơ nhanh

| Mục | Giá trị (đọc 2026-10-12, clone nông commit `a09c079`) |
|---|---|
| Repo | zeenie-ai/OpenCompany (tên cũ **MachinaOS**, đổi ~7/2026); npm `@zeenie-ai/opencompany` 0.2.1 (12/9/2026) |
| Tác giả | Zeenie AI (tài khoản cá nhân, 5 repo); gần như toàn bộ commit của `trohitg`, trailer `Co-Authored-By: Claude`; everydev.ai nói 1 nhân sự ở Bengaluru **(chưa xác minh)** |
| License / quy mô | MIT; 995★ · 151 fork · 1.556 commit; commit cuối 11/10/2026; ~183k dòng Python + ~91k dòng TS; 386 file test; `CLAUDE.md` 359 KB (2.835 dòng) |
| Stack | FastAPI + WebSocket, React 19 + React Flow + Tailwind 4, Electron, bun, uv/Python 3.12, SQLite mặc định, **Temporal** nhúng; 14 provider LLM (Anthropic, OpenAI, Gemini, Ollama, LM Studio…) |
| Xu hướng sao | +671/90 ngày (reporank) — ổn định, không viral; **0 thread HN/Reddit** tìm được |

### Cơ chế đáng học

- **Một nhân viên = một workflow**: chủ mô tả việc bằng lời → LLM soạn bản thiết lập (app, giờ làm, quy tắc hỏi trước) → "Hire" tạo workflow chạy nền với trigger Gmail/Telegram/WhatsApp/Stripe/webhook/cron.
- **Topology là ranh giới uỷ quyền** (`docs-internal/agent_teams.md`): lead (`ai_employee`/`orchestrator_agent`) chỉ giao việc cho specialist nối trực tiếp vào handle `input-teammates`, tối đa 2 tầng, không trùng loại specialist trong một đội; mỗi tool node có đúng một agent sở hữu.
- **Task Manager** gắn cố định vào lead: giao việc chỉ qua `assign_task(mission, context, acceptance_criteria, assignee)`; specialist nộp, lead review và trả lại nếu chưa đạt rồi mới báo chủ. Các tool `delegate_to_*` **bị ẩn khỏi model**, lead chỉ thấy roster một dòng/teammate.
- **Context ≠ Memory** (RFC-0002): context = hội thoại backend sở hữu, khoá `(workflow, generation, agent)`, mọi lần kích hoạt nối tiếp cùng hội thoại; memory = tool `simpleMemory` gọi tường minh, người dùng sửa được. Thiết kế journal/epoch/hash-chain trong RFC bị thay bằng store phẳng sau ~2 tháng — "đơn giản thắng".
- **Compaction** tự động ở 0,8 cửa sổ ngữ cảnh thành tóm tắt 5 phần ("lấy cảm hứng từ Claude Code") kèm đếm token và tính chi phí theo `pricing.json`.
- **Skill = SKILL.md** (chuẩn Agent Skills, 86 file/21 domain, ví dụ `employee/chase-late-payments` với 3 mức nhắc nợ, cấm đe doạ/tự giảm giá); "self-improving" = memory + sửa skill + thêm tool có duyệt, **không retrain**.
- **Plugin**: class kế thừa `ActionNode/TriggerNode/ToolNode` với `Params`/`Output` Pydantic dùng chung cho form UI + tool schema LLM + REST spec; restart là có node mới, không sửa frontend. Approval gate "ask first" cho gửi/chi tiền kèm 5 giây undo. CLI agent (Claude Code/Codex/Gemini) chạy qua subprocess — gãy khi CLI đổi flag (issue #132–134).

### Mâu thuẫn & rủi ro

- README "78 skills" nhưng đếm được **86**; "140+ tools" vs docs "110+ nodes" vs mã 171 plugin; README hứa 6 "nhân viên" nhưng chỉ ship 3 template + 4 starter; website kể 6 vai khác và dashboard "$27,342/day" không có bằng chứng; website bán gói Pro/Max trong khi README nói "No subscription".
- `.env` **commit sẵn SECRET_KEY/JWT_SECRET_KEY dev**; binary desktop chưa ký; không SECURITY.md; agent có quyền email/thanh toán/shell trên máy người dùng.
- Bus-factor 1; issue 10/10/2026: job kẹt "working" khi model local không gọi `assign_task` (#145), Gmail trigger giao mission rỗng (#143). cloudnews.tech (4/2026): "còn xa mới plug-and-play".
- Trùng tên với `tinyhumansai/opencompany` (Rust, GPL-3.0, 298★) — dự án khác, vài directory gộp nhầm.

### Bài học cho kho

- Họ "công ty AI" 2026 tách làm hai: *thư viện cho dev* (MetaGPT, ChatDev, CrewAI, agency-swarm) và *sản phẩm end-user chạy nền* (Paperclip, OpenCompany, OpenOPC). OpenCompany là mẫu hiếm có installer 3 OS + Docker 1 container, docs nội bộ 300 file và 3 RFC ở dự án một người.
- Ba pattern đưa sang mục 03: topology = ranh giới uỷ quyền, ẩn tool uỷ quyền khỏi model (chỉ đưa roster), tách context/memory. Cùng ý với X-Agents "model quyết định, code hành động" (mục 23).
- Trạng thái: **theo dõi, chưa khuyến nghị production**; nếu thử: Docker, đổi secret `.env`, dùng model cloud; xem lại sau 3–6 tháng (contributor thứ hai, SECURITY.md, bản ký số).

## 4b. Case study: Munder Difflin (HarnessMD) – "văn phòng" agent CLI có avatar (link từ người dùng, 2026-10-12)

> Nguồn: https://github.com/harnessmd/munder-difflin. Đã clone đầy đủ lịch sử (1.394 commit): README, `HIVE.md`, `TELEMETRY.md`, `SECURITY.md`, `LICENSE`/`LICENSE-ASSETS`, `src/shared/agentProvider.ts`, `src/main/analytics.ts`, `test/`. Cùng với đó là trang GitHub, trendshift và Product Hunt.

### Hồ sơ nhanh

| Mục | Giá trị (đọc 2026-10-12) |
|---|---|
| Repo | `HarnessMD/munder-difflin`, nhưng README, link release và lệnh clone vẫn trỏ `chaitanyagiri/munder-difflin` → đã chuyển sang org mới. Site harnessmd.com, munderdiffl.in. Tên nhại "Dunder Mifflin" (*The Office*), agent điều phối tên "Michael" |
| Tác giả | Chaitanya Giri: 1.053/1.394 commit (2 email); có 4 người khác góp 27–56 commit |
| Tuổi / phiên bản | Commit đầu 31/5/2026; v0.5.3 "pre-release"; badge #1 Repository of the Day trên trendshift, #5 Product of the Day trên Product Hunt |
| Quy mô | Electron + React + TypeScript + Pixi.js + xterm.js + node-pty; ~66,8k dòng TS trong `src/`; 131 file test |
| License / mô hình | Code MIT; art asset tách riêng (`LICENSE-ASSETS`). **Open-core**: bản Pro US$150/năm (giảm theo sức mua, thấp nhất ~US$100) có sidebar Tasks/Inbox/Automations, ghi âm cuộc họp "Stapler"… |
| Số liệu | **8,7k★**, 1,2k fork, 34 watcher, 114 issue + 125 PR mở |
| Lịch sử commit | **75 commit `seo-engine: day N AM/PM…`**: một agent viết bài SEO/blog theo lịch rồi commit thẳng vào repo sản phẩm (thư mục `blog/`, `seo/`) |

### Cơ chế

- **Mỗi terminal là một agent:** chạy CLI thật (`claude`, `codex`, `agy`, `grok`, `kimi`, `qwen`, `opencode`, `crush`, `pi`, `copilot`, Cursor hoặc lệnh tuỳ ý) trong PTY. Dùng subscription có sẵn, chịu giới hạn theo giờ của từng gói; hỗ trợ thêm BYOK và model local (Ollama, LM Studio, vLLM). Mỗi agent tuỳ chọn một git worktree riêng.
- **"Hive" = repo git chứa file thuần:** agent ghi vào `outbox/`, router giao vào `inbox/` của người nhận; blackboard `board.md` chỉ có một người ghi; `tasks.json` là sổ giao việc; event log chỉ ghi thêm. **Chỉ harness commit git** (single-committer), nhờ vậy tránh lỗi hỏng `index.lock` khi nhiều agent cùng ghi. Chỉ request/query/propose mới bắt buộc trả lời; có trần số bước chuyển để hai agent không đá qua đá lại mãi.
- **GOD agent (Michael):** người dùng chỉ nói chuyện với Michael; Michael phân việc, tự xử việc thường, chỉ đẩy việc "critical" (chi tiền, thao tác phá huỷ, đổi phạm vi) vào hàng chờ duyệt. Ngoài ra có **circuit breaker** steer → constrain → stop khi agent lặp, bão lỗi hoặc vượt ngân sách token; chi phí thật đọc từ transcript; span OTel.
- **Memory:** markdown của từng agent được gom thành "palace" chung có tìm kiếm ngữ nghĩa và cơ chế nén. README gọi đây là "fastest memory layer in the world" nhưng không có benchmark **(chưa xác minh)**.
- **Phụ:** dictation toàn hệ thống (Whisper chạy local), avatar trên sàn văn phòng 2D, IDE Monaco, kanban có ticket key, kích hoạt qua Slack/webhook, catalog 227 skill.

### Đọc cổng thật

| Tuyên bố | Code / docs | Nhận xét |
|---|---|---|
| "Autonomy with a leash: spend, scope and destructive operations come back to you" | `HIVE.md`: "Its escalation policy (what counts as 'critical') lives in its **system prompt** and is the primary control surface — tune the prompt, not the code" | Cổng duyệt là **phán đoán của LLM**, không phải code. Prompt injection hoặc model nhầm thì thao tác phá huỷ vẫn chạy. Khác với cổng máy (mục 23) và khác với cách OpenCompany giới hạn bằng topology (§4) |
| Chế độ auto của từng agent | `agentProvider.ts`: Claude Code và Grok chạy với `--permission-mode bypassPermissions`, Cursor với `--dangerously-skip-permissions`, Gemini với `--yolo`. Riêng **Codex đã được sửa** từ `--dangerously-bypass-approvals-and-sandbox` sang `-a never -s workspace-write` + `--add-dir` (comment giải thích, có test `auto-mode-sandbox.test.cjs`) | Ngoài Codex, ở chế độ auto **không agent nào có sandbox hay cổng hỏi**; an toàn chỉ còn dựa vào lời dặn trong prompt của Michael. Nên chạy trong VM/container (mục 11) hoặc dùng Codex |
| Telemetry "anonymous" | `TELEMETRY.md` + `analytics.ts`: PostHog, **bật sẵn (opt-out)**, allowlist sự kiện (`app_launched`, `agent_spawned`, `message_sent` chỉ đếm, không có nội dung), `$ip: null`, tôn trọng `DO_NOT_TRACK`; key chỉ chèn vào bản build chính thức | Minh bạch hơn mức trung bình: tài liệu là hợp đồng và allowlist được thực thi bằng code. Nhưng mặc định vẫn là bật |
| "Free, open source" | Lõi MIT; nhiều tính năng điều hành (sidebar Pro, Stapler) nằm trong bản Pro trả phí | Open-core, giống context-mode (mục 03 §8b) |

### Đánh giá

- **Đáng học:** (1) **hive bằng file + một người commit duy nhất**: giao tiếp giữa agent đọc được, diff được, không cần message broker; (2) chặn trả lời qua lại bằng loại thông điệp + trần số bước; (3) circuit breaker có 3 nấc thay vì kill ngay; (4) `TELEMETRY.md` là hợp đồng có allowlist trong code; (5) sửa Codex từ "bypass toàn bộ" sang "sandbox + `--add-dir`" là ví dụ đúng về giữ sandbox khi cần ghi thêm thư mục.
- **Rủi ro:** cổng "critical" là LLM; bypass permission mặc định cho các CLI ngoài Codex; pre-release (0.5.x) nhưng có tới 125 PR mở; repo vừa đổi chủ; commit SEO tự động làm loãng lịch sử; chưa có đánh giá độc lập về chất lượng phối hợp nhiều agent.
- **So sánh:** cùng họ "công ty/văn phòng AI" với OpenCompany (§4), Paperclip, OpenOPC, và cùng nhóm ADE ở mục 01 §1.3 (Personal Jarvis, T3 Code, Claude Squad). Điểm khác biệt là dồn mọi CLI về **một** agent điều phối bằng giọng nói/chat và hiển thị như một văn phòng.

## 4c. Nâng cấp 31/10/2026: rà repo lớn

> Hai việc. (1) Đọc lại sao, license, trạng thái của các repo mục 02 bằng GitHub search API (31/10/2026). (2) Tìm framework lớn còn thiếu: 5 truy vấn (`agent framework`, topic `ai-agents`, `multi-agent`, `agent sdk`, `agent harness`, repo tạo sau 1/10/2025), lọc bỏ repo đã có trong `data/projects.json`. Chọn **7 repo**, clone `--filter=blob:none` (lịch sử) và `--depth 1` (đọc/grep mã): LICENSE, manifest, cấu trúc gốc, file nguồn chính, CI, grep telemetry/host mạng; đếm commit, tác giả, trailer `Co-Authored-By: Claude`. **Không cài, không chạy script nào của repo.**

### 4c.1 Repo cũ: điều đã đổi

| Repo | Thay đổi (bảng §1 → 31/10/2026) | Hệ quả |
|---|---|---|
| `FoundationAgents/MetaGPT` | **Push cuối 21/1/2026** (hơn 9 tháng); 71,1k★ | Coi như ngừng phát triển; chỉ đọc để học mẫu SOP, không chọn cho dự án mới |
| `Pythagora-io/gpt-pilot` | Push cuối 18/6/2026; GitHub báo `NOASSERTION` | Khớp ghi chú "ngừng bảo trì" ở §1 |
| `HKUDS/OpenOPC` | **Không còn trong kết quả search API** (meta_all không có) | Có thể đã đổi tên, chuyển private hoặc xoá **(chưa xác minh)**; tạm không dùng URL cũ |
| `NousResearch/hermes-agent` | "–" → **259,2k★**, MIT | Lớn thứ hai trong bảng sau OpenClaw (393,6k) |
| `ruvnet/ruflo` | "–" → 80,4k★, MIT | Số sao lớn nhưng tuyên bố hiệu năng vẫn **chưa kiểm chứng** |
| `langchain-ai/langchain` / `langgraph` | ~130k → 148,8k★ / ~40k → 44,2k★ | |
| `deepset-ai/haystack` | ~20k → 26,9k★ | Tăng mạnh nhất nhóm RAG |
| `pydantic/pydantic-ai` | ~16k → 21k★ | |
| `google/adk-python` | "–" → 22,1k★ | Bổ sung số |
| `mastra-ai/mastra` | "–" → 29,2k★; GitHub báo `NOASSERTION` | GitHub không nhận diện được license; catalog ghi Apache-2.0, cần đọc lại LICENSE trước khi nhúng **(chưa đọc lại đợt này)** |
| `microsoft/agent-framework` | "–" → 14,4k★ | Bổ sung số |
| `microsoft/autogen` | 61,7k★; GitHub nhận **CC-BY-4.0** | Nhiều khả năng do file `LICENSE` là license tài liệu, mã theo `LICENSE-CODE` (MIT) **(chưa đọc lại đợt này)**. Catalog giữ MIT |
| `camel-ai/camel` · `ag2ai/ag2` · `VRSEN/agency-swarm` | ~13k → 18k★ · "–" → 5k★ · "–" → 4,6k★ | |
| `paperclipai/paperclip` · `bytedance/deer-flow` · `crewAIInc/crewAI` | 100,5k → 109,5k · 83,7k → 84,8k · ~57k → 60,4k★ | |

### 4c.2 Bảng nhanh 7 repo mới

| Repo | Nhóm | ★ · license | Commit cuối | Một dòng | Cờ |
|---|---|---|---|---|---|
| `HKUDS/nanobot` | Agent cá nhân | 49,7k · MIT | 31/10/2026 | Agent cá nhân tự host, WebUI/TUI/chat app, memory "Dream", cron, SDK + API kiểu OpenAI | "Siêu nhẹ" nhưng ~188k dòng Python; `restrict_to_workspace` mặc định tắt |
| `agentscope-ai/agentscope` | Framework | 35k · Apache-2.0 | 31/10/2026 | AgentScope 2.0 (Alibaba): middleware, permission engine, SOP, A2A, realtime voice | Lịch sử viết lại từ 8/2025 |
| `nanocoai/nanoclaw` | Agent cá nhân | 31,1k · MIT | 26/10/2026 | "OpenClaw thu nhỏ": mỗi agent một container, chạy trên Claude Agent SDK | **PostHog lúc setup bật sẵn**; 43% commit có trailer Claude |
| `langchain-ai/deepagents` | Agent harness | 30,8k · MIT | 31/10/2026 | Harness "đủ pin" trên LangGraph: subagent, filesystem, nén ngữ cảnh, skills, HITL | `recursion_limit` 9.999 |
| `strands-agents/harness-sdk` | Framework + harness | 9k · Apache-2.0 | 30/10/2026 | Monorepo Strands (AWS) Python/TS: SDK vòng lặp + `create_harness()` | Mặc định Bedrock Claude Sonnet 4.6 |
| `anthropics/claude-agent-sdk-python` | SDK | 8,4k · MIT (+ điều khoản thương mại) | 31/10/2026 | SDK Python chạy Claude Code CLI làm vòng lặp agent | **Wheel nhúng CLI Claude Code mã đóng** |
| `vercel/eve` | Framework | 5,8k · Apache-2.0 | 31/10/2026 | Agent "filesystem-first": `instructions.md`, `tools/`, `skills/`, `channels/`, `schedules/` | 1.0.0-rc.1; telemetry CLI bật sẵn; gắn hạ tầng Vercel |

### 4c.3 Hồ sơ từng repo

- **deepagents** (LangChain). 4.546 commit từ 27/7/2025, 177 tác giả, phiên bản `deepagents` 0.7.32. Lõi là `create_deep_agent()` trong `graph.py` ghép chuỗi middleware: subagent (đồng bộ và async), filesystem kèm quyền (`FilesystemPermission`), summarization, memory, skills, prompt caching; thư mục `middleware/` còn có `_message_eviction`, `_blob_offload` (đẩy output tool ra đĩa). ✅ README "context management: summarize + offload to disk" khớp middleware thật. Đáng học nhất là **`RubricMiddleware`** (tuỳ chọn, không nằm trong graph mặc định): khi model định dừng, một grader sub-agent chấm transcript theo rubric; `needs_revision` thì đưa phản hồi lại và lặp tiếp, dừng ở `satisfied`/`failed` hoặc `max_iterations`. Đây là mẫu evaluator–optimizer đóng gói sẵn (mục 03 §1). ⚠️ Graph đặt `recursion_limit = 9_999`, nên trần vòng lặp thật nằm ở middleware/người gọi. Mạng: thư viện chỉ gọi model; `deepagents-code` (CLI kèm theo) tự bật trace LangSmith khi lưu key qua `/auth`, tắt bằng `DEEPAGENTS_CODE_LANGSMITH_TRACING=false`. Cài: `uv add deepagents`.
- **AgentScope 2.0** (Alibaba/Tongyi). Repo tạo 1/2024 nhưng lịch sử hiện tại bắt đầu 15/8/2025 (viết lại cho 2.0), 828 commit, 191 tác giả, `__version__` 2.0.12dev, cần Python ≥ 3.11. Có `permission/` (engine + rule + decision), `sop/` (chạy việc nhiều bước theo quy trình chuẩn), `pipeline/` (`TeamPipeline` leader giao việc), `realtime/`, A2A. Tracing OpenTelemetry nằm trong middleware, không thấy endpoint thu thập mặc định. Host mặc định nghiêng về Aliyun Bailian/DashScope. Cài: `pip install agentscope`.
- **Claude Agent SDK (Python)**. 952 commit từ 11/6/2025, **26,7% có trailer Claude**, phát hành tự động (bot GitHub Actions đứng đầu). ❌ Điều README không nói ở đầu: **wheel nhúng sẵn CLI Claude Code** (`_cli_version.py` = 2.1.316) là phần mềm mã đóng; LICENSE MIT chỉ phủ phần SDK, và README §"License and terms" đặt toàn bộ việc dùng dưới **Commercial Terms** của Anthropic. ⚠️ Bẫy quyền: `allowed_tools` chỉ là danh sách **tự duyệt**, không giới hạn tool; muốn chặn phải dùng `disallowed_tools` (README tự ghi). Script build `download_cli.py` tải `install.sh` và chỉ kiểm shebang, không kiểm hash. Cài: `pip install claude-agent-sdk`.
- **Strands harness-sdk** (AWS). Repo `sdk-python` cũ (tạo 14/5/2025) nay là monorepo `harness-sdk`: `strands-py`, `strands-ts`, `harness-py`, `harness-ts`, CLI, MCP server, site docs, `team/` (tenets, quyết định). 3.187 commit, 365 tác giả, 56 workflow. ✅ README "lifecycle controls (turn limits, token budgets, cancellation)" có trong SDK. ✅ Telemetry đúng mực: `harness-py/telemetry.py` **chỉ bật exporter OTel khi đặt `OTEL_TRACES_EXPORTER`**, cố ý không theo mặc định `otlp` của spec để tránh âm thầm dựng exporter. Mặc định model `global.anthropic.claude-sonnet-4-6` trên Bedrock (cần tài khoản AWS). Cài: `pip install strands-harness` hoặc `pip install strands-agents`.
- **nanobot** (HKU Data Intelligence Lab). 5.171 commit từ 1/2/2026, 543 tác giả, v0.4.0. ⚠️ Tự gọi "ultra-lightweight" nhưng gói `nanobot/` có 445 file, ~188k dòng Python, kèm cả một bộ cập nhật tự động (~20 module `update_*`). ⚠️ `restrict_to_workspace` mặc định `False`: shell và file tool không bị giới hạn trong workspace trừ khi bật. Không thấy telemetry trong mã Python. Kênh: Telegram, Discord, Slack, WeChat, Feishu, email, Linear. Cài: `pip install nanobot-ai` (Python ≥ 3.11).
- **NanoClaw**. 3.052 commit từ 31/1/2026, 196 tác giả, **43,1% commit có trailer Claude** (cao nhất đợt). Ý tưởng: thay vì OpenClaw (~500k dòng, bảo mật ở tầng ứng dụng), mỗi agent chạy trong **container Linux riêng**, chỉ thấy thư mục được mount, khoá API đi qua Agent Vault của OneCLI (agent không giữ khoá thô). ⚠️ "Một tiến trình, vài file nguồn" không khớp: `src/` có 242 file TS, ~37,7k dòng (không tính test). ⚠️ `setup/lib/diagnostics.sh` gửi sự kiện cài đặt tới PostHog (`us.i.posthog.com`, khoá nhúng sẵn) với install-id lưu ở `data/install-id`; README có nói, tắt bằng `NANOCLAW_NO_DIAGNOSTICS=1`. Khi một bước cài lỗi, script **tự gọi Claude Code để sửa**, nên cần giám sát lần cài đầu. Cài: `git clone https://github.com/nanocoai/nanoclaw.git && cd nanoclaw && bash nanoclaw.sh`.
- **eve** (Vercel). 2.360 commit từ 16/6/2026, 77 tác giả, `eve@1.0.0-rc.1`. Agent khai báo bằng thư mục: `instructions.md` bắt buộc, `tools/*.ts`, `skills/*.md`, `channels/`, `schedules/`; gói npm kèm toàn bộ docs để coding agent đọc tại `node_modules/eve/docs`. Phụ thuộc chặt hệ Vercel (`@vercel/sandbox`, `@vercel/queue`, `@vercel/oidc`, AI Gateway). ⚠️ CLI telemetry **bật sẵn** gửi `telemetry.vercel.com/api/eve-cli/v1/events`, tắt bằng `eve telemetry disable` hoặc `EVE_TELEMETRY_DISABLED=1`; **không đọc `DO_NOT_TRACK`**. Có gói `eve-self-modification` (agent tự sửa mình), nên khoá quyền ghi khi chạy production. Cài: `npx eve@latest init my-agent`.

### 4c.4 Mẫu chung rút ra

1. **"Harness" thay chữ "framework"**: deepagents ("batteries-included agent harness"), Strands đổi tên repo thành `harness-sdk` và thêm `create_harness()`, Claude Agent SDK bọc nguyên Claude Code. Xu hướng là bán một agent đã lắp sẵn với mặc định tốt, kèm lối thoát để thay từng phần.
2. **Thư mục là giao diện viết agent**: eve (`agent/` theo quy ước), nanobot/NanoClaw (`CLAUDE.md` và memory theo từng nhóm), deepagents (skills, memory trên backend file). Hợp với hướng "trạng thái bền trong file" của mục 03 §6.
3. **Cách ly bằng container thay cho allowlist** (NanoClaw) là câu trả lời trực tiếp cho rủi ro "agent cá nhân có quyền shell" của OpenClaw/nanobot; nanobot vẫn để `restrict_to_workspace` tắt.
4. **Telemetry: Strands là mẫu tốt** (tắt đến khi người dùng bật bằng biến chuẩn OTel). eve, NanoClaw, deepagents-code bật sẵn; chỉ một phần tôn trọng `DO_NOT_TRACK`.
5. **"Nhẹ" là lời quảng cáo, không phải số đo**: nanobot ~188k dòng, NanoClaw ~38k dòng. Đếm dòng trước khi tin.

**Nguồn §4c:** GitHub search API 31/10/2026 (5 truy vấn + `user:HKUDS`) · `meta_all.json`/`status_all.json` (GitHub API 31/10/2026) · clone `--filter=blob:none` và `--depth 1` 7 repo, đọc: deepagents (README.md, LICENSE, `libs/deepagents/pyproject.toml`, `deepagents/graph.py`, `deepagents/middleware/{rubric,summarization,subagents,permissions}.py`, `libs/code/DEVELOPMENT.md`, `deepagents_code/config.py`) · agentscope (README.md, LICENSE, pyproject.toml, `src/agentscope/{_version.py, permission/, sop/, middleware/_tracing/}`) · claude-agent-sdk-python (README.md, LICENSE, pyproject.toml, `src/claude_agent_sdk/_cli_version.py`, `scripts/download_cli.py`) · harness-sdk (README.md, LICENSE.APACHE, NOTICE, `harness-py/src/strands_harness/telemetry.py`, `strands-py/src/strands/models/bedrock.py`) · nanobot (README.md, LICENSE, `nanobot/config/schema.py`, `nanobot/config/loader.py`) · nanoclaw (README.md, README_zh.md, LICENSE, nanoclaw.sh, `setup/lib/diagnostics.sh`, `src/`) · eve (README.md, LICENSE, `packages/eve/package.json`, `packages/eve/src/cli/telemetry/{index,flush,preference}.ts`) · https://github.com/HKUDS/OpenOPC (không tìm thấy qua search API)

## 4d. Nâng trần 2/11/2026: chuẩn trace OTel GenAI và benchmark gọi tool độc lập framework (yêu cầu người dùng)

> Đọc lại §1–§4c và catalog; grep `repo` trong `data/projects.json` trước khi thêm. Sao/license/ngày bằng GitHub search API 2/11/2026; clone `--depth 1 --filter=blob:none` (BFCL clone sparse thư mục `berkeley-function-call-leaderboard/`), chỉ đọc. **Không cài, không chạy.**

**Trần hiện tại**

- §1–§2 so framework bằng mô hình tư duy, số sao, tải/tháng; §4c ghi telemetry từng repo (Strands chỉ bật OTel khi đặt `OTEL_TRACES_EXPORTER`, AgentScope có tracing OTel). Nhưng **chưa có chuẩn chung** để trace của LangGraph, CrewAI, OpenAI Agents SDK, Strands… so được với nhau.
- Chưa có cổng máy đo **năng lực gọi tool** của tổ hợp model + framework; mục 07 có τ²-bench (tool–agent–user) nhưng thiếu benchmark gọi hàm/đa lượt và benchmark môi trường (OS, DB, web).
- Hệ quả: đổi framework hay model chỉ dựa vào cảm nhận, không có baseline đo được.

**Bảng repo mới**

| Repo | Lớp | ★ · license (2/11/2026) | Commit cuối | Vì sao nâng trần | Rủi ro |
|---|---|---|---|---|---|
| `open-telemetry/semantic-conventions-genai` | Chuẩn | 506 · Apache-2.0 | 2/11/2026 (`16f3130`) | Repo riêng (tạo 5/5/2026) cho GenAI semconv, tách khỏi `semantic-conventions` (trang cũ ghi "Moved"). Định nghĩa span agent: `create_agent`, `invoke_agent`, `invoke_workflow`, `plan`, `execute_tool`, cùng `mcp.md`, `a2a.md`, metric token; `reference/` có kịch bản cho từng thư viện chạy trên mock server và **conformance runner** dùng OTel Weaver để kiểm thuộc tính | Mọi thuộc tính `gen_ai.*` vẫn **Development**; README ghi "Schema URL: TODO", CHANGELOG chưa có bản phát hành; tên thuộc tính có thể đổi |
| `Arize-ai/openinference` | Chuẩn (thực dụng) + instrumentation | 1.299 · Apache-2.0 | 1/11/2026 (`5c68f3a`) | Spec bổ sung trên OTel với `openinference.span.kind` (AGENT, CHAIN, TOOL, GUARDRAIL, EVALUATOR…) và gói instrumentation sẵn cho ~38 thư viện Python (LangChain, CrewAI, OpenAI Agents, Strands, Google ADK, Agent Framework, Claude Agent SDK, PydanticAI, smolagents, MCP…), JS/Java/Go; có gói `openinference-genai` (JS) và `annotations.md` ánh xạ sang sự kiện `gen_ai.evaluation.result` | Là chuẩn của một vendor (Arize, xem Phoenix ở mục 07), chồng lấn với OTel GenAI; cần chọn một quy ước chính cho pipeline |
| `ShishirPatil/gorilla` (BFCL) | Cổng máy | 13.062 · Apache-2.0 | push 17/10/2026; HEAD nhánh mặc định 23/3/2026 (`6ea5797`) | Berkeley Function Calling Leaderboard: chấm gọi hàm bằng AST và thực thi, đa lượt, V4 thêm agentic (web search, memory, độ nhạy định dạng); trọng số V4 dồn 40% cho agentic vì các tác vụ single-turn đang tiến gần mức bão hòa; gói `bfcl_eval`, cờ `--partial-eval` | CHANGELOG dừng ở 10/2025; hạng mục web search cần SerpAPI; đo model + prompt format, **không** đo framework trực tiếp, phải bọc handler |
| `THUDM/AgentBench` | Cổng máy (môi trường) | 3.806 · Apache-2.0 | 9/2/2026 (`d1e4a10`) | Bản "AgentBench FC" (10/2025) dùng prompt function-calling, đóng container 5 môi trường: alfworld, DB (MySQL), knowledge graph, OS, WebShop; một lệnh `docker compose` dựng controller AgentRL + worker | Nặng (Freebase cho KG, Redis, nhiều image); đứng yên ~9 tháng; bản cũ ở tag `v0.1`/`v0.2` |

> Cùng đợt 2/11/2026, mục 07 (phần "Nâng trần 2/11/2026: chuẩn trace GenAI…") cũng hồ sơ hoá `semantic-conventions-genai` và `openinference` từ góc quan sát/eval; catalog chỉ giữ một dòng cho mỗi repo, mục này nhìn từ góc chọn framework.

**Stack nâng trần**

1. **Một quy ước trace cho mọi framework**: bật instrumentation OpenInference cho framework đang dùng (§1) và xuất OTLP sang Phoenix/Langfuse (mục 07); đặt mục tiêu chuyển dần sang tên `gen_ai.*` khi semconv ổn định. Mẫu "chỉ bật khi đặt biến OTel" của Strands (§4c) là mặc định nên giữ.
2. **Cổng thuộc tính trace**: chạy conformance runner của `semantic-conventions-genai` (hoặc test riêng kiểm `invoke_agent`/`execute_tool` có đủ `gen_ai.operation.name`, `gen_ai.provider.name`) trong CI để trace không âm thầm mất trường khi nâng framework.
3. **Baseline gọi tool trước khi đổi model**: chạy BFCL (`--partial-eval` trên hạng mục multi-turn + agentic) cho model ứng viên; so cùng prompt format framework dùng (V4 đo độ nhạy định dạng).
4. **Kiểm framework trong môi trường thật**: với agent thao tác OS/DB, dùng các task container của AgentBench FC làm smoke test; với agent hội thoại, dùng τ²-bench (mục 07).
5. **Ghi kết quả vào hồ sơ framework**: mỗi lựa chọn ở §2 "Tiêu chí chọn" kèm số đo BFCL/AgentBench và trace mẫu theo quy ước ở bước 1.

**Nguồn §4d:** GitHub search API 2/11/2026 (`repo:` cho 4 repo trên và `open-telemetry/semantic-conventions`; `tau2-bench`, `inspect_ai`, `openllmetry`, `phoenix` đã có ở mục 07) · clone 2/11/2026, đọc: semantic-conventions-genai (README.md, LICENSE, CHANGELOG.md, `docs/gen-ai/{README,gen-ai-agent-spans,mcp,a2a}.md`, `reference/README.md`) · `open-telemetry/semantic-conventions` (`docs/gen-ai/README.md`, trang "Moved") · openinference (LICENSE, `spec/{semantic_conventions,annotations}.md`, cây `python/instrumentation/`, `js/packages/`) · gorilla (`berkeley-function-call-leaderboard/{README.md,CHANGELOG.md,pyproject.toml}`, LICENSE) · AgentBench (README.md, LICENSE, cây thư mục) · https://github.com/open-telemetry/semantic-conventions-genai · https://opentelemetry.io/docs/specs/semconv/gen-ai/ · https://github.com/Arize-ai/openinference · https://gorilla.cs.berkeley.edu/leaderboard.html · https://github.com/THUDM/AgentBench

<a id="core-framework-semantics"></a>

## 4e. Nâng trần 2/11/2026: checkpoint, retry và giới hạn có ngữ nghĩa rõ (mở rộng cùng ngày)

> Mở rộng chiều sâu trong cùng đợt 2/11/2026, không phải công bố các repo vừa ra mắt. Hai repo dưới đã có trong catalog: đọc lại LICENSE, CI và nhánh mặc định bằng clone chỉ đọc; SHA đối chiếu GitHub API. Mức bằng chứng **code-read**; không chạy/build repo ngoài, hiệu năng và hành vi thực tế **(chưa xác minh)**. Số sao/trạng thái đọc 2026-11-02; ngày commit tính theo UTC, tách khỏi `pushed_at`.

| Repo đã có | ★ · license (2026-11-02) | HEAD nhánh mặc định | Vai trò đọc sâu |
|---|---|---|---|
| `langchain-ai/langgraph` | 44.327 · MIT | 2026-11-02 · `ee3c043b` | Checkpoint/HITL và điểm có thể thực thi lại |
| `pydantic/pydantic-ai` | 20.996 · MIT | 2026-11-02 · `129c94ef` | Hợp đồng output/tool và các loại ngân sách |

**Trần còn thiếu:** §4d đã chuẩn hoá trace và benchmark tool; §2 vẫn chủ yếu chọn framework theo kiểu đồ thị/type safety. Với hệ chạy thật, cần biết **bước nào bị chạy lại, điều gì đã được lưu và giới hạn đếm cái gì**.

### LangGraph: durable phụ thuộc checkpointer và ranh giới node

- [`InMemorySaver`](https://github.com/langchain-ai/langgraph/blob/ee3c043bddcc514012885167dd5916b15d6e4731/libs/checkpoint/langgraph/checkpoint/memory/__init__.py#L34) tự ghi chỉ hợp debugging/testing và khuyên PostgresSaver cho production. State trong RAM không sống qua việc mất tiến trình; chọn framework “có checkpoint” chưa đủ.
- [`Pregel.stream`](https://github.com/langchain-ai/langgraph/blob/ee3c043bddcc514012885167dd5916b15d6e4731/libs/langgraph/langgraph/pregel/main.py#L2794) có `sync` (lưu trước bước tiếp), `async` (lưu song song, mặc định), `exit` (lưu khi thoát); mã cảnh báo **`durability` không có tác dụng nếu thiếu checkpointer**. Trade-off là độ trễ lưu và cửa sổ mất tiến trình, cần đo với backend thật.
- [`interrupt()`](https://github.com/langchain-ai/langgraph/blob/ee3c043bddcc514012885167dd5916b15d6e4731/libs/langgraph/langgraph/types.py#L918) resume bằng **chạy lại node từ đầu**; nhiều interrupt khớp theo thứ tự. Side effect trước interrupt phải idempotent hoặc tách riêng vào task/node có ranh giới ghi nhận. Không thể suy ra “đúng một lần” cho thanh toán/email chỉ từ checkpoint.

### PydanticAI: output có kiểu và budget là hai hợp đồng riêng

- [`UsageLimits`](https://github.com/pydantic/pydantic-ai/blob/129c94ef2940565af3bc9f638196fcc994d1ed4d/pydantic_ai_slim/pydantic_ai/usage.py#L536) mặc định `request_limit=50`, nhưng đếm **response được commit vào history**, không phải tất cả HTTP/provider retry hoặc các attempt fallback. `tool_calls_limit` đếm tool thành công; cần giới hạn cả lượt model và timeout để chặn vòng lỗi.
- Token usage lấy từ provider và thường kiểm **sau response**; `count_tokens_before_request=True` có thể kiểm trước với provider hỗ trợ nhưng thêm overhead. `cost_limit` không thay request/token cap khi bảng giá hoặc usage thiếu; muốn trần chi phí cứng còn cần cổng quota/billing bên ngoài.
- Output validation/`ModelRetry` trong [`_agent_graph.py`](https://github.com/pydantic/pydantic-ai/blob/129c94ef2940565af3bc9f638196fcc994d1ed4d/pydantic_ai_slim/pydantic_ai/_agent_graph.py#L847) có ngân sách retry riêng. Output đúng schema chưa chứng minh nội dung đúng; vẫn ghép eval §4d và mục 07. [CI](https://github.com/pydantic/pydantic-ai/blob/129c94ef2940565af3bc9f638196fcc994d1ed4d/.github/workflows/ci.yml) là bằng chứng kiểm thư viện, chưa phải kiểm yêu cầu của ứng dụng tích hợp.

**Ma trận chọn theo failure semantics**

| Điều kiện | Lựa chọn phù hợp | Phần người tích hợp phải chứng minh |
|---|---|---|
| Có nhiều trạng thái, cần dừng chờ người | LangGraph + persistent checkpointer | Restart/resume không mất state; `thread_id` cách ly đúng tenant |
| Tool/output cần kiểu và DI rõ | PydanticAI | Validation thất bại có trần; test sai schema, tool lỗi và usage thiếu |
| Luồng dài có side effect bên ngoài | Framework + runtime mục 21 | Idempotency key/outbox; kill–resume không gửi/trừ tiền lặp |
| Nhiều agent/subagent dùng chung budget | Usage chia sẻ có chủ ý | Child không tự nới cap; đối soát provider usage với số đếm framework |
| Mục tiêu đổi backend quan sát | OTel/OpenInference §4d | Weaver kiểm trace; không bật ghi prompt nhạy cảm theo mặc định |

**Cách ghép:** bắt đầu một framework và một backend checkpoint; thiết kế schema state/output; đặt request/token/tool/time cap; ghép adapter durable khi thật sự cần, giữ side effect có receipt; kiểm fault injection ở các điểm trước/sau checkpoint và interrupt. Chạy cùng tập task §4d và trace chung; chọn theo kết quả + ngữ nghĩa khôi phục, không theo bảng sao. Những ca fault injection này là **tiêu chí đánh giá đề xuất**, chưa được chạy trong đợt đọc kho.

**Nguồn phần mở rộng:** [1](https://github.com/langchain-ai/langgraph/blob/ee3c043bddcc514012885167dd5916b15d6e4731/LICENSE) · [2](https://github.com/langchain-ai/langgraph/blob/ee3c043bddcc514012885167dd5916b15d6e4731/libs/langgraph/langgraph/pregel/main.py) · [3](https://github.com/langchain-ai/langgraph/blob/ee3c043bddcc514012885167dd5916b15d6e4731/libs/langgraph/langgraph/types.py) · [4](https://github.com/langchain-ai/langgraph/blob/ee3c043bddcc514012885167dd5916b15d6e4731/libs/checkpoint/langgraph/checkpoint/memory/__init__.py) · [5](https://github.com/langchain-ai/langgraph/blob/ee3c043bddcc514012885167dd5916b15d6e4731/.github/workflows/_test_langgraph.yml) · [6](https://github.com/pydantic/pydantic-ai/blob/129c94ef2940565af3bc9f638196fcc994d1ed4d/LICENSE) · [7](https://github.com/pydantic/pydantic-ai/blob/129c94ef2940565af3bc9f638196fcc994d1ed4d/pydantic_ai_slim/pydantic_ai/usage.py) · [8](https://github.com/pydantic/pydantic-ai/blob/129c94ef2940565af3bc9f638196fcc994d1ed4d/pydantic_ai_slim/pydantic_ai/_agent_graph.py) · [9](https://github.com/pydantic/pydantic-ai/blob/129c94ef2940565af3bc9f638196fcc994d1ed4d/.github/workflows/ci.yml) · [10](https://docs.langchain.com/oss/python/langgraph/interrupts) · [11](https://pydantic.dev/docs/ai/api/pydantic-ai/usage/)

## 4f. Hồ sơ `blogminhquy/javis-os`: trợ lý tự host "thuê model, giữ não" chạy trên CLI thuê bao (link người dùng gửi, clone 2/11/2026)

> Người dùng gửi link. Clone `--filter=blob:none` đủ lịch sử ngày 2/11/2026 (HEAD `94b597415a370064cd33a7013b8eddc8dcbf5a7b`, v0.440.0, commit lúc 17:02 +07 cùng ngày); đọc LICENSE, README, ARCHITECTURE.md, SECURITY.md, CLAUDE.md (prompt kernel), `install.sh`, `requirements.txt`, `server/main.py` (các đoạn PROVIDER_DEFS, host, bypass), `server/claude_sdk_engine.py`, `server/mcp_hub.py`, `update.sh`, 4 workflow CI; không chạy mã. Cùng nhóm "trợ lý cá nhân tự host" với OpenClaw/Hermes/nanobot ở §1 và §4c.

### 4f.1 Hồ sơ nhanh

| Mục | Thông tin (2/11/2026) |
|---|---|
| Repo | `blogminhquy/javis-os` · **MIT** (© 2026 Nguyễn Minh Quý) · **537★ · 205 fork · 8 issue mở** (GitHub search API) · homepage javisos.com · topics `agent-os`, `harness`, `mcp`, `telegrambot` |
| Tác giả | Nguyễn Minh Quý (`blogminhquy`, minhquy.vn): người làm kinh doanh online/marketing ở VN, không phải tổ chức; 5 repo khác đều nhỏ (`javis-store` index skill/pack, `javis-zalo` CLI + MCP Zalo, bộ cài Telegram↔Claude Code) |
| Lịch sử | Tạo **28/6/2026** ("Jarvis OS — AI operating layer"); **1.531 commit trong 4 tháng** (~12/ngày), **936 PR** (tác giả tự mở và merge từng bản, số PR trùng số phiên bản 0.x), 141 PR trong 8 ngày cuối; 59 PR từ người ngoài (nhiều nhất `hwangrin`), 33 issue (chỉ 4 trước 1/10 → cộng đồng mới bùng từ tháng 10) |
| Ai viết | 1.289 commit ký tên tác giả, **216 commit author "Claude"**, **4.116 trailer `Co-Authored-By: Claude`** trên 1.531 commit: gần như toàn bộ mã do agent viết dưới điều phối của tác giả; CHANGELOG hai thứ tiếng |
| Quy mô | `server/*.py` **227.024 dòng**, riêng `server/main.py` **29.548 dòng**; dashboard JS thuần 201 file; `tests/` **1.017 file .py**; `docs/` 503 file, README 12 ngôn ngữ; mã và comment tiếng Việt không dấu (có `docs/dev/GLOSSARY.md`) |
| Phát hành | File `VERSION` 0.440.0 nhưng chỉ **4 tag git** (v0.64.x); cập nhật bằng `update.sh` = `git pull --ff-only` + pip, hoặc trang Updates trong dashboard (`server/updater.py`); image `ghcr.io`; từ 0.439.0 có installer Windows .exe / macOS .dmg, **ký mã tắt mặc định** cho tới khi chủ repo thêm secret |
| CI | `ci.yml`: pytest chia 2 shard, fetch thêm 8 commit cũ để chạy test "quay về" theo phiên bản; `docker-publish.yml`; `desktop-installers.yml`; `translations.yml` (`tools/check_translations.py`) |

### 4f.2 Nó là gì (đối chiếu mã, không chỉ README)

- **"Thuê model, giữ não."** Một server FastAPI + WebSocket `/ws`; mỗi lượt chat là job phía server (`chat_runtime.ChatRuntime`) nên đóng tab không hủy. Prompt = `CLAUDE.md` gốc (prompt kernel ~ vai "trợ lý business & life") + `memory/MEMORY.md` + skill index + khối kênh. Mọi thứ người dùng tích lũy là **file markdown trong thư mục "brain"** (Obsidian đọc được), hội thoại trong SQLite FTS5, mỗi lượt "học" là một commit git có thể hoàn tác, brain đồng bộ lên repo GitHub riêng.
- **14 "brain" đúng như README** (đếm `PROVIDER_DEFS`): 4 CLI thuê bao (`claude` qua Claude Agent SDK, `codex`, Grok Build `grok`, Antigravity CLI `agy`) có shell/web/subagent, và 10 engine API (OpenRouter, Anthropic, OpenAI, Gemini, Groq, DeepSeek, Ollama cloud/local, endpoint OpenAI-/Anthropic-compatible) chỉ có tool qua MCP Hub. `ARCHITECTURE.md` vẫn ghi "12 providers" (tài liệu cũ hơn mã). `CLAUDE.md` ghi Gemini CLI bị gỡ ở 0.50.0 vì Google cắt gói cá nhân 18/6/2026 **(chưa xác minh)**.
- **MCP Hub (`server/mcp_hub.py`) là lớp cứng:** gộp tool từ mọi connection, quyền 3 mức `readonly/safe/full` kiểm trong code (`mcp_catalog.effective_perm`), **audit log** `mcp_audit.jsonl` (xoay ở 5 MB), rate limit; bot khách hàng (Zalo/Messenger) chạy engine trong **thư mục trống, không MCP, không tool ghi** để prompt injection từ khách không có gì để làm.
- **Việc nền:** Tasks (Kanban + nhắc + thói quen, 0.422–0.428), loops `Javis/loops/*.md`, self-learning `learn.py`, "team" nhiều agent có bước chờ duyệt (`team_gate.py`, PreToolUse hook **fail-closed** từ 0.207.0). Kênh: Telegram, Zalo (bot + cá nhân), Slack, WhatsApp, Messenger (0.434), CLI; 0.440.0 thêm "Javis Gate" cho chat ngoài (ChatGPT) gọi vào qua MCP OAuth (issue #971 đang mở vì ChatGPT từ chối OAuth tùy chỉnh).
- **Plugin người dùng = Python thật chạy trong process server**, bật mặc định từ 0.161.0; tắt bằng `JAVIS_ENABLE_USER_PLUGINS=false`. SECURITY.md tự khai "AI brain with full rights on the machine it is installed on".

### 4f.3 Đọc cổng thật

| Điểm | Mức | Chi tiết |
|---|---|---|
| Bind và đăng nhập | ✅ | `JAVIS_HOST` mặc định `127.0.0.1` (main.py:28790, script start); cổng đăng nhập + TOTP (`totp.py`) + API token theo scope; tự vá PYSEC-2026-161 (Host header bẻ `url.path`) ở 0.59.16 trước khi nâng Starlette |
| Ghim phụ thuộc có lý do | ✅ | `requirements.txt` ghim `fastapi==0.141.1`, `starlette`, `claude-agent-sdk==0.2.116` và **ghi từng advisory đã soi** (7 PYSEC, cái nào chạm, cái nào không); Dockerfile ghim `node:22.23.4` theo bản vá Brotli RCE 21/10/2026 và có `ANNOUNCEMENTS.json` cảnh báo người dùng |
| Quyền của engine Claude | ⚠️ | `claude_sdk_engine.py`: có `allowed_tools` → `permission_mode="default"` + `can_use_tool` gate **DENY mọi tool ngoài danh sách**, không nạp settings máy; **không có** `allowed_tools` → `permission_mode="bypassPermissions"` ("parity --dangerously-skip-permissions") và nạp settings user/project/local. Phiên chat chính của chủ máy đi nhánh nào tùy cấu hình "mode" (suggest/auto/full) → đọc kỹ trước khi mở Javis ra Internet |
| Installer | ⚠️ | `install.sh` tự `apt/dnf install`, cài Node (NodeSource `curl \| bash`), `npm i -g @anthropic-ai/claude-code`, và **`curl -fsSL … \| bash`** cho `agy` (antigravity.google) và `grok` (x.ai) — là installer chính thức của hai hãng nhưng vẫn là mẫu kho cảnh báo (mục 12); `.env` chmod 600 |
| Cập nhật | ⚠️ | `git pull --ff-only` từ `main`, không tag/ký; "Updates page" tự cập nhật → người dùng chạy đúng HEAD của tác giả, không có bước xem diff. Ghim commit nếu dùng cho việc thật |
| Dữ liệu rời máy | ✅/⚠️ | Không thấy telemetry hay gọi về javisos.com (chỉ `BRAND_SOURCE` ghi vào metadata PNG sinh ra); request chỉ đi tới provider đã chọn. Nhưng STT/TTS, học nền và loop 24/7 đều gửi nội dung brain tới provider đó; CLI thuê bao chạy nền liên tục có **rủi ro ToS** (blog bên ngoài cũng cảnh báo khoá tài khoản; kho chưa thấy case thật) |
| Tốc độ thay đổi | ⚠️ | 12 commit/ngày, main.py gần 30k dòng, test 1.017 file nhưng không có coverage công bố; audit độc lập gần như không theo kịp. 34 PR ngoài đang mở (0 merged của người ngoài ở Game Studios là chuyện khác; ở đây 59 PR ngoài có merge) |
| Minh bạch thương mại | ⚠️ | README có 3 link Hostinger kèm `REFERRALCODE` không ghi là affiliate; phần "Support" là donate. javisos.com không bán gói; blog bên thứ ba (dochidung.com) bán khóa học/tư vấn quanh sản phẩm |

### 4f.4 So với cùng nhóm (sao GitHub search API 2/11/2026)

| Repo | ★ | Khác biệt so với Javis OS |
|---|---|---|
| `openclaw/openclaw` (§1) | 393.719 | TypeScript, kênh chat là trung tâm, hệ skill lớn; không có khái niệm "brain = thư mục markdown + git" và Zalo/POS VN |
| `NousResearch/hermes-agent` (§1, §4c) | 259.719 | Cùng ý "CLI thuê bao làm backend" qua plugin provider (chủ kho có `Plugin-4-Hermes`, mục 23 §5); Hermes là framework cho dev, Javis là sản phẩm đóng gói cho chủ shop |
| `HKUDS/nanobot` (§4c) | 49.763 | Cũng tự gọi "nhẹ" mà ~188k dòng Python; `restrict_to_workspace` tắt mặc định — cùng bẫy quyền như nhánh bypass của Javis |
| `nanocoai/nanoclaw` (§4c) | 31.073 | **Mỗi agent một container**, khoá API trong vault OneCLI: mẫu cô lập mà Javis chưa có (plugin Python chạy trong process) |
| `open-jarvis/OpenJarvis` (mục 01) | 12.949 | Stanford, local-first, đo năng lượng/chi phí; nghiên cứu hơn là sản phẩm |
| `Dodaios/Dodaios` (mục 01) | 316 | Agent OS desktop nhiều pane, cùng vấn đề `approval_mode=bypass` mặc định |

**Khi nào dùng:** chủ doanh nghiệp nhỏ ở VN đã có gói Claude/ChatGPT, muốn trợ lý tiếng Việt nối Zalo/Pancake/Meta Ads, dữ liệu nằm trên máy mình và đọc được bằng Obsidian. **Điều kiện tối thiểu:** giữ bind `127.0.0.1` sau reverse proxy TLS; bật TOTP; `JAVIS_ENABLE_USER_PLUGINS=false` trừ khi tự viết plugin; cấu hình allowlist tool thay vì nhánh bypass; ghim commit thay vì "Updates page"; chạy trong Docker với volume riêng; đọc điều khoản gói thuê bao trước khi bật loop nền 24/7. **Không nên** coi SECURITY.md "full rights on the machine" là cảnh báo hình thức.

**Nguồn §4f:** clone `--filter=blob:none` 2/11/2026 (HEAD `94b5974`; `git log` thống kê tác giả/trailer, `git tag`, `git rev-list --count`); LICENSE, README.md, ARCHITECTURE.md, SECURITY.md, CLAUDE.md, VERSION, CHANGELOG.md, `install.sh`, `update.sh`, `requirements.txt`, Dockerfile, `ANNOUNCEMENTS.json`, `server/main.py` (PROVIDER_DEFS :1766, host :28790, bypass :2170), `server/claude_sdk_engine.py` (:531, :878–890, :900), `server/mcp_hub.py` (:44, :107, :248, :1399), `server/image_gen.py` (:239), `.github/workflows/{ci,docker-publish,desktop-installers,translations}.yml` · GitHub search API 2/11/2026 (repo, user, issues, PR) · https://javisos.com (đọc 2/11/2026) · https://dochidung.com/javis-os-la-gi-huong-dan-toan-dien/ (blog bên thứ ba, có bán khóa học) · WebSearch 2/11/2026 (javisos.vn, Threads meta.ai, ~207 fork cùng tên)

## 4g. Hồ sơ `andrewyng/openworker` (OpenWorker): "đồng nghiệp AI" desktop giao việc xong, quản trị bằng kiến trúc, sandbox NVIDIA OpenShell (ảnh README người dùng gửi, clone 2/11/2026)

> Ảnh là README trên GitHub: "OpenWorker", huy hiệu Trendshift "#1 Repository Of The Day", "Beta", "Governed by design", "NVIDIA OpenShell sandbox", nút tải macOS "signed & notarized · auto-updates" và Windows "not yet code-signed". Clone `--filter=blob:none` đủ lịch sử 2/11/2026 (HEAD `5e3d7261f203bbd94a91fa10856d29aad0bfaeae`, v0.3.4, commit cùng ngày); đọc LICENSE, README, SECURITY.md, `pyproject.toml`, `docs/openshell.md`, `coworker/cloud.py`, `coworker/config.py`, `coworker/sandbox/providers/openshell_policy.py`, `surfaces/gui/src-tauri/tauri.conf.json`, 3 workflow CI; không chạy mã. Đặt cạnh Javis OS (§4f) vì cùng là "trợ lý tự host, model thay được" nhưng khác hẳn về cách đặt hàng rào.

### 4g.1 Hồ sơ nhanh

| Mục | Thông tin (2/11/2026) |
|---|---|
| Repo | `andrewyng/openworker` · **MIT** (© 2024 Andrew Ng) · **18.866★ · 2.678 fork · 375 mở** (GitHub search API; README không nêu tên Andrew Ng, chỉ owner tài khoản) · homepage openworker.com · tạo 20/7/2026, công bố 23/7/2026 (web) |
| Ai viết | 972 commit, **82 tác giả email**; đứng đầu Rohit C Prasad (367 + 184 commit dưới hai tên), Devika Verma (248); chỉ 26 trailer Co-Authored-By; **215 PR người ngoài đã merge** trên 552 PR; 272 issue (202 còn mở) → dự án nhóm có cộng đồng thật, khác hẳn Javis OS (một người) |
| Quy mô | Python 498 file (`coworker/` 277: sandbox 42, personas 37, connectors 32, providers 27, teams 15), TypeScript/TSX 336 file (`surfaces/gui`, **Tauri 2** + React), `tests/` 244 file .py; CI `ci.yml` chạy `pytest --cov=coworker` + `tsc --noEmit` + `npm test`; `release.yml` ký và notarize macOS khi có secret `APPLE_*`, Windows chưa ký (đúng như ảnh); `image.yml` |
| Phát hành | 11 tag (v0.3.2…v0.3.4); Tauri updater với `pubkey` minisign và endpoint `download.openworker.com/latest.json` → tự cập nhật có chữ ký, khác `git pull` của Javis |
| Model | "Bring your own key": OpenAI, Azure, Anthropic, Gemini, Ark (BytePlus/Volcengine), GLM, DeepSeek, Kimi, Qwen, MiniMax, Mistral, xAI, Upstage, Cohere, Together, Fireworks, OpenRouter, Ollama…; nền `aisuite>=0.2.0` (thư viện của Andrew Ng); không có đường "CLI thuê bao" kiểu Javis/Hermes |

### 4g.2 "Governed by design" đối chiếu mã

| Tuyên bố README | Trong mã | Mức |
|---|---|---|
| "Hard floors: human-only, always; no mode lowers them" | `coworker/server/manager.py` giữ `human_only` trên từng pending call (:6496–6519), floor MCP tách khỏi verdict đọc của catalog (:2132–2136); SECURITY.md coi **bypass floor/approval gate qua prompt injection hoặc MCP tool độc** là lỗi mức cao, trong phạm vi báo cáo | ✅ |
| "Approval-gated by default, auto-approve optional" | `config.py`: `auto_approve: bool = False`, `auto_approve_shadow = False`, `auto_approve_plan_approval = False`; inbox approver cho session/team/plan (`manager.py` :1637–1907); unattended run "never self-approve", chờ trong inbox | ✅ mặc định đóng |
| "Audit trail với provenance" | `coworker/audit.py`; `docs/openshell.md` ghi mức enforcement vào từng tool-call event | ✅ (chưa đọc schema) |
| "Sandbox NVIDIA OpenShell" | `coworker/sandbox/` 42 file: `providers/openshell_policy.py` dịch "thư mục của session + user id + allowlist mạng" thành policy OpenShell; **refuse thay vì chạy mở khi OpenShell không dùng được**; profile "open" (mọi host) không viết được vì OpenShell 0.1 từ chối `*`; "secrets are absent, not denied": sandbox không chứa key, API token của chính OpenWorker cũng ở ngoài. Mặc định app chạy lệnh trực tiếp, bật sandbox theo từng máy; Mac cần Docker Desktop, có thêm `docs/macos-sandbox.md` và `windows-sandbox.md` | ✅ nhưng **opt-in** |
| "Your data leaves your machine only through the model and integrations you choose" | `coworker/cloud.py`: telemetry "một câu: loại coworker và thời điểm", **default-on cho người đã đăng nhập tài khoản cloud tùy chọn**, có opt-out; không gửi prompt/output/đường dẫn; tài khoản cloud chỉ broker OAuth (`api.openworker.com`, `machines.openworker.com`); Slack relay qua websocket. PostHog trong mã là **connector** đọc dữ liệu người dùng, không phải telemetry của app | ⚠️ ghi rõ "default-on khi đăng nhập" |
| "Security coworkers ship first" | `coworker/personas/` 37 file; README: security review dùng scanner tất định (semgrep) rồi model triage; incident triage; cần tự kiểm chất lượng tìm lỗi (kho chưa chạy) | (chưa xác minh) |

### 4g.3 So với Javis OS (§4f) và nhóm

| Tiêu chí | OpenWorker | Javis OS |
|---|---|---|
| Hàng rào | Floor human-only trong code, approval mặc định, sandbox container per agent, cập nhật ký minisign | Allowlist tool → gate DENY, nhưng không allowlist → `bypassPermissions`; plugin Python trong process; `git pull` |
| Ai làm | 82 contributor, 215 PR ngoài merge | 1 người + agent, 59 PR ngoài |
| Model | API key (18+ provider) + Ollama | 4 CLI thuê bao + 10 API |
| "Não" | Conversations + memory trong app; không phải thư mục markdown | Thư mục markdown Obsidian + git undo |
| Kênh | Slack (@mention mở session trên desktop), automation lịch, remote machines SSH | Telegram/Zalo/Messenger/WhatsApp, Zalo cá nhân, POS VN |
| Nền tảng | macOS ký+notarize, Windows chưa ký, Linux chưa có bundle (issue #787) | Linux/macOS/Windows script, Docker, .exe/.dmg chưa ký |

- **Đáng học nhất:** (1) tách "floor" (không mode nào hạ được) khỏi "ladder" (duyệt một lần → luật → allowlist cấu hình); (2) sandbox mà **từ chối chạy** khi không dựng được, thay vì âm thầm chạy mở (ngược với nhánh bypass của Javis và `restrict_to_workspace` tắt của nanobot §4c); (3) tuyên bố bảo mật đi kèm SECURITY.md nhận lỗi bypass do prompt injection vào phạm vi.
- **Rủi ro:** beta 0.3.x, 202 issue mở; sandbox opt-in nên mặc định vẫn chạy lệnh trên máy; telemetry default-on khi đăng nhập; Windows chưa ký; tài khoản cloud tùy chọn là dịch vụ của chính dự án (OAuth broker), cần đọc chính sách khi dùng connector Slack/Gmail.
- **Dùng thế nào:** bật OpenShell cho máy dùng thật, giữ `auto_approve=false`, tắt telemetry nếu đăng nhập, ghim tag; với Linux chờ bundle chính thức hoặc chạy headless (`docs/headless.md`).

**Nguồn §4g:** ảnh README người dùng gửi 2/11/2026 · clone `--filter=blob:none` 2/11/2026 (HEAD `5e3d726`; `git log` tác giả/trailer, `git tag`); LICENSE, README.md (:5–21, :65–90), SECURITY.md, `pyproject.toml`, `docs/openshell.md`, `docs/approval-guidance.md`, `coworker/cloud.py` (:278–305), `coworker/config.py` (:83–99), `coworker/server/manager.py` (:1637–1907, :2132, :6496–6519), `coworker/sandbox/providers/openshell_policy.py`, `surfaces/gui/src-tauri/tauri.conf.json` (:47–52), `.github/workflows/{ci,release,image}.yml` · GitHub search API 2/11/2026 (repo, issues, PR, `is:pr is:merged -author:andrewyng`) · https://openworker.com (WebFetch 2/11/2026) · WebSearch 2/11/2026: marktechpost.com (23/7/2026) · mer.vin · note.com/ai_driven (đọc mã) · theaiagentindex.com

<a id="factory-framework-guardrail-boundaries-2026-11-04"></a>

## 4h. Nâng trần 4/11/2026: kiểm đúng ranh giới guardrail và handoff trước khi chọn framework

> Đọc sâu hồ sơ OpenAI Agents SDK Python (OpenAI), MIT; `23e9996ac146109bdcd9b871e3564f70dc13aae1`; 2026-11-04. Mức **code-read**, không chạy SDK hay gọi model; không cập nhật sao. Giữ phạm vi §4e cho LangGraph/PydanticAI, không nâng mức bằng chứng của các hồ sơ đó chỉ vì được so trong bảng.

**Trần còn thiếu:** checkpoint/retry ở §4e xử lý sống lại sau lỗi; xưởng còn phải biết cổng kiểm nào chạy **trước hành động**, cổng nào chỉ xét đầu vào ban đầu/đầu ra cuối, và đường nào không đi qua cổng. Từ “guardrail” không xác định những ranh giới này.

### OpenAI Agents SDK: guardrail agent và guardrail tool có phạm vi khác nhau

- [`InputGuardrail`](https://github.com/openai/openai-agents-python/blob/23e9996ac146109bdcd9b871e3564f70dc13aae1/src/agents/guardrail.py) mặc định `run_in_parallel=True`. [Runner](https://github.com/openai/openai-agents-python/blob/23e9996ac146109bdcd9b871e3564f70dc13aae1/src/agents/run.py) chia guardrail tuần tự và song song; [tài liệu gốc](https://github.com/openai/openai-agents-python/blob/23e9996ac146109bdcd9b871e3564f70dc13aae1/docs/guardrails.md) nói rõ ở chế độ song song, model có thể đã dùng token và thực thi tool trước khi bị huỷ. Với kiểm điều kiện bắt buộc trước hành động, dùng chế độ blocking và cổng ngay tại side effect; output guardrail không hoàn tác việc đã gửi.
- Input guardrail cấp agent chỉ áp dụng cho agent đầu chuỗi, output guardrail cho agent tạo đầu ra cuối. **Handoff không tự biến guardrail đầu chuỗi thành kiểm mỗi tool của mọi specialist.** Đặc tả công việc phải ghi từng ranh giới cần xét quyền/tenant/args.
- [Pipeline function-tool](https://github.com/openai/openai-agents-python/blob/23e9996ac146109bdcd9b871e3564f70dc13aae1/src/agents/run_internal/tool_execution.py) có kiểm input/output của function tool và kiểm approval. Tài liệu hiện tại nêu tool guardrails áp dụng pipeline `FunctionTool` (kể cả local MCP có cấu hình guardrail), không áp dụng trực tiếp cho handoff, hosted tools hay các built-in execution tools được liệt kê trong docs. Phải kiểm adapter cụ thể; không tuyên bố “mọi tool đều được guardrail” từ việc đã gắn một decorator.
- Với tool cần approval, input guardrail mặc định chạy sau approval và trước thực thi; tuỳ chọn `pre_approval_tool_input_guardrails=True` cho phép kiểm trước khi tạo interruption và vẫn kiểm lại sau khi được duyệt. Quyết định quyền nên gắn với invocation/args hiện tại, không chỉ tên tool.

| Nhu cầu | Điểm xuất phát | Điều người tích hợp cần thêm |
|---|---|---|
| Điều phối handoff và function tool rõ | OpenAI Agents SDK | Ma trận tool → pipeline → guardrail → principal → side effect |
| State graph, interrupt/resume | LangGraph (§4e) | Persistent checkpointer; idempotency và replay test |
| Output/tool có kiểu và giới hạn usage | PydanticAI (§4e) | Eval nội dung, timeout và quota bên ngoài |
| Workflow hữu hạn, ít nhánh | Hàm/queue/state machine tất định | Không thêm vòng agent nếu rule thường giải được |

**Chuỗi tích hợp:** (1) liệt kê tool thật theo đường thực thi, dữ liệu ra provider và quyền tối thiểu; (2) xác định precondition nào phải chặn trước call, condition nào xét sau; (3) giữ canary function tool có receipt để thử input bị từ chối, handoff, timeout và approval với args đổi; (4) kết hợp checkpoint mục 21 với idempotency của side effect, log trace có redaction; (5) chạy cùng dataset và tiêu chí nhiệm vụ ở mục 07/30 trước khi đổi framework.

**Nghiệm thu đề xuất:** input bị từ chối ở chế độ blocking không khởi chạy hành động; mỗi tool ghi principal/tenant và args đã kiểm; hủy run không được báo đã hoàn tác side effect; mọi exception/blocked/budget-exhausted có trạng thái riêng. Đây là yêu cầu kiểm của dự án tích hợp, **(chưa xác minh)** bằng thực nghiệm trong đợt đọc này.

**Nguồn phạm vi:** [LICENSE](https://github.com/openai/openai-agents-python/blob/23e9996ac146109bdcd9b871e3564f70dc13aae1/LICENSE) · [CI tests](https://github.com/openai/openai-agents-python/blob/23e9996ac146109bdcd9b871e3564f70dc13aae1/.github/workflows/tests.yml). SDK MIT không cấp quyền sử dụng model hay bỏ nghĩa vụ dữ liệu của dịch vụ tích hợp.

<a id="anhkysuai-2026-11-23"></a>

## Đánh giá từ kho Anh Kỹ Sư AI — 23/11/2026

Phần này có **7 hồ sơ hoặc phạm vi đối chiếu** từ [nguồn tuyển chọn](https://anhkysuai.com/kho/). [Bảng đủ 1.295 repo](../data/collections/anhkysuai-kho.json) ghi trạng thái đối chiếu từng link; [danh sách URL](../data/collections/anhkysuai-kho-links.txt) phục vụ tra cứu. Nguồn tuyển chọn giúp phát hiện repo; đánh giá bên dưới dựa trên clone và permalink upstream cùng metadata GitHub ngày 2026-11-23.

Mức `docs-read`/`code-read` chỉ áp dụng phạm vi ghi tại mỗi hồ sơ. Chưa cài, build, chạy test hay benchmark mã upstream. Giấy phép có thể tách theo code, model, nội dung, asset hoặc bản enterprise; con số/tuyên bố của tác giả chưa được tái lập nếu không có ghi chú khác.

<a id="anhkysuai-2026-11-23-zeroclaw"></a>

### ZeroClaw

**Repo:** [zeroclaw-labs/zeroclaw](https://github.com/zeroclaw-labs/zeroclaw) · **License:** MIT OR Apache-2.0 · **★ 33,583 (GitHub API, 2026-11-23)**

**Mục đích:** Agent cá nhân bằng Rust với nhiều kênh nhắn tin, mô hình và công cụ hệ thống.

**Giá trị và cơ chế:** Đã đọc đường chạy shell: kiểm chính sách/đường dẫn trước tạo tiến trình, xác nhận loại shell, bọc sandbox rồi thiết lập môi trường. Autonomy mặc định là Supervised; chính sách yêu cầu cờ approved cho lệnh rủi ro theo cấu hình.

**Giới hạn:** Đây là kiểm tra một luồng shell; chưa kiểm chứng nguồn quyết định approved, mọi adapter hay cách ly toàn hệ thống. Constructor shell có NoopSandbox nếu không được thay.

**Cách tham khảo/tích hợp:** Tham khảo phân lớp policy–runtime–tool, thử cấu hình sandbox và chấp thuận trên workspace dùng thử.

**Thay thế:** [OpenClaw](https://github.com/openclaw/openclaw), [nanobot](https://github.com/HKUDS/nanobot), picoclaw.

**Bằng chứng:** `code-read`, ngày 2026-11-23, commit [`b503bc5758fa`](https://github.com/zeroclaw-labs/zeroclaw/commit/b503bc5758fa0ae45fee68b6b674d6277e5f8a7b). Hàm kiểm chính sách shell và callsite trước spawn, autonomy mặc định, các mục liên quan trong CI; không kiểm mọi sandbox/adapter. Chưa cài/chạy upstream.

**Nguồn:** [README.md](https://github.com/zeroclaw-labs/zeroclaw/blob/b503bc5758fa0ae45fee68b6b674d6277e5f8a7b/README.md) · [LICENSE-APACHE](https://github.com/zeroclaw-labs/zeroclaw/blob/b503bc5758fa0ae45fee68b6b674d6277e5f8a7b/LICENSE-APACHE) · [LICENSE-MIT](https://github.com/zeroclaw-labs/zeroclaw/blob/b503bc5758fa0ae45fee68b6b674d6277e5f8a7b/LICENSE-MIT) · [crates/zeroclaw-runtime/src/security/policy.rs](https://github.com/zeroclaw-labs/zeroclaw/blob/b503bc5758fa0ae45fee68b6b674d6277e5f8a7b/crates/zeroclaw-runtime/src/security/policy.rs) · [crates/zeroclaw-runtime/src/tools/shell.rs](https://github.com/zeroclaw-labs/zeroclaw/blob/b503bc5758fa0ae45fee68b6b674d6277e5f8a7b/crates/zeroclaw-runtime/src/tools/shell.rs) · [crates/zeroclaw-config/src/autonomy.rs](https://github.com/zeroclaw-labs/zeroclaw/blob/b503bc5758fa0ae45fee68b6b674d6277e5f8a7b/crates/zeroclaw-config/src/autonomy.rs) · [crates/zeroclaw-config/src/policy.rs](https://github.com/zeroclaw-labs/zeroclaw/blob/b503bc5758fa0ae45fee68b6b674d6277e5f8a7b/crates/zeroclaw-config/src/policy.rs) · [metadata GitHub](https://api.github.com/repos/zeroclaw-labs/zeroclaw).

<a id="anhkysuai-2026-11-23-qm"></a>

### QM

**Repo:** [yc-software/qm](https://github.com/yc-software/qm) · **License:** MIT · **★ 15,762 (GitHub API, 2026-11-23)**

**Mục đích:** Agent cho nhóm dùng qua Slack/web với workspace, lịch chạy và bộ nhớ theo người/phòng.

**Giá trị và cơ chế:** Đã đọc classifier: mode observe ghi nhận bất đồng bộ và cho đi tiếp; enforce chờ kết quả, phân biệt dữ liệu chưa được screen. SECURITY.md giải thích principal/scope và giới hạn operator.

**Giới hạn:** Đây là phần classifier, chưa chứng minh cách ly toàn nền tảng. Upstream tự ghi experimental, command policy có thể vượt qua và browser runner không đi qua một số cổng core; screening mặc định tắt theo README.

**Cách tham khảo/tích hợp:** Tham khảo mô hình scope, thử trong một tổ chức nội bộ và kiểm tuyến gọi tool/bộ nhớ theo quyền.

**Thay thế:** [OpenClaw](https://github.com/openclaw/openclaw), [Letta](https://github.com/letta-ai/letta), [Octop](../02-agent-frameworks/README.md#anhkysuai-2026-11-23-octop).

**Bằng chứng:** `code-read`, ngày 2026-11-23, commit [`6f84bffaf85b`](https://github.com/yc-software/qm/commit/6f84bffaf85bbed72425e3888430a8d1611c0eda). createSecurityClassifier, mode observe/enforce và security model; chưa kiểm toàn tuyến effect/authorization. Chưa cài/chạy upstream.

**Nguồn:** [README.md](https://github.com/yc-software/qm/blob/6f84bffaf85bbed72425e3888430a8d1611c0eda/README.md) · [LICENSE](https://github.com/yc-software/qm/blob/6f84bffaf85bbed72425e3888430a8d1611c0eda/LICENSE) · [SECURITY.md](https://github.com/yc-software/qm/blob/6f84bffaf85bbed72425e3888430a8d1611c0eda/SECURITY.md) · [src/core/orchestrator/security-screen.ts](https://github.com/yc-software/qm/blob/6f84bffaf85bbed72425e3888430a8d1611c0eda/src/core/orchestrator/security-screen.ts) · [metadata GitHub](https://api.github.com/repos/yc-software/qm).

<a id="anhkysuai-2026-11-23-genericagent"></a>

### GenericAgent

**Repo:** [lsdefine/GenericAgent](https://github.com/lsdefine/GenericAgent) · **License:** MIT · **★ 14,440 (GitHub API, 2026-11-23)**

**Mục đích:** Framework agent tối giản thao tác terminal, file và trình duyệt trên máy cá nhân.

**Giá trị và cơ chế:** Đã đọc vòng lặp: gọi model, parse tool_calls, dispatch sang do_<tool>, thu kết quả và dừng theo StepOutcome/max_turns. Bash/PowerShell được ánh xạ về code_run, hooks bao quanh mỗi bước.

**Giới hạn:** Chỉ kiểm loop/dispatch, chưa kiểm mọi tool, ghi nhớ hay cơ chế tự sinh skill. Không thấy workflow GitHub CI trong tree đã lấy. Tuyên bố tự xây repo và tự tiến hóa là lời tác giả.

**Cách tham khảo/tích hợp:** Tham khảo vòng điều phối, chạy về sau trong môi trường tách biệt với tool allowlist và dữ liệu thử.

**Thay thế:** [smolagents](https://github.com/huggingface/smolagents), [nanobot](https://github.com/HKUDS/nanobot), [Open Interpreter](https://github.com/openinterpreter/open-interpreter).

**Bằng chứng:** `docs-read`, ngày 2026-11-23, commit [`a0521ab4f92b`](https://github.com/lsdefine/GenericAgent/commit/a0521ab4f92b4f3b57d5b1f070ff4296c9062e03). Vòng agent_runner_loop, dispatch và cấu trúc agentmain; tree không có GitHub Actions workflow, chưa kiểm toàn bộ tools. Chưa cài/chạy upstream.

**Nguồn:** [README.md](https://github.com/lsdefine/GenericAgent/blob/a0521ab4f92b4f3b57d5b1f070ff4296c9062e03/README.md) · [LICENSE](https://github.com/lsdefine/GenericAgent/blob/a0521ab4f92b4f3b57d5b1f070ff4296c9062e03/LICENSE) · [agent_loop.py](https://github.com/lsdefine/GenericAgent/blob/a0521ab4f92b4f3b57d5b1f070ff4296c9062e03/agent_loop.py) · [agentmain.py](https://github.com/lsdefine/GenericAgent/blob/a0521ab4f92b4f3b57d5b1f070ff4296c9062e03/agentmain.py) · [metadata GitHub](https://api.github.com/repos/lsdefine/GenericAgent).

<a id="anhkysuai-2026-11-23-octop"></a>

### Octop

**Repo:** [TencentCloud/Octop](https://github.com/TencentCloud/Octop) · **License:** MIT · **★ 12,410 (GitHub API, 2026-11-23)**

**Mục đích:** Trợ lý AI tự lưu trữ đa người dùng/agent, kết nối web, IM, MCP và ACP.

**Giá trị và cơ chế:** Đã đọc middleware: tuyến /api ngoài allowlist gọi authenticate_request, cache người dùng trên request; khi chưa có user, setup-lockdown trả 503 cho API ngoài setup/health. Đây là lớp vào API đã xem.

**Giới hạn:** Chưa chứng minh cách ly tool, WebSocket hay toàn allowlist; backend model/connector vẫn có thể gửi dữ liệu ngoài máy. AgentTeams và manifest hiện là beta, không coi nhãn self-hosted thành bảo đảm riêng tư.

**Cách tham khảo/tích hợp:** Thử setup, phân quyền và kênh IM trên tổ chức dùng thử trước nối tài khoản nghiệp vụ.

**Thay thế:** [OpenClaw](https://github.com/openclaw/openclaw), [QM](../02-agent-frameworks/README.md#anhkysuai-2026-11-23-qm), [Letta](https://github.com/letta-ai/letta).

**Bằng chứng:** `code-read`, ngày 2026-11-23, commit [`30f4aecd2e14`](https://github.com/TencentCloud/Octop/commit/30f4aecd2e14e7eeee639b8c6c33c9f404463df8). Middleware JWT và setup-lockdown, cùng CI; chưa kiểm mọi route và tenant boundary. Chưa cài/chạy upstream.

**Nguồn:** [README.md](https://github.com/TencentCloud/Octop/blob/30f4aecd2e14e7eeee639b8c6c33c9f404463df8/README.md) · [LICENSE](https://github.com/TencentCloud/Octop/blob/30f4aecd2e14e7eeee639b8c6c33c9f404463df8/LICENSE) · [src/octop/api/middleware/jwt_auth.py](https://github.com/TencentCloud/Octop/blob/30f4aecd2e14e7eeee639b8c6c33c9f404463df8/src/octop/api/middleware/jwt_auth.py) · [src/octop/api/middleware/setup_lockdown.py](https://github.com/TencentCloud/Octop/blob/30f4aecd2e14e7eeee639b8c6c33c9f404463df8/src/octop/api/middleware/setup_lockdown.py) · [metadata GitHub](https://api.github.com/repos/TencentCloud/Octop).

<a id="anhkysuai-2026-11-23-agenticseek"></a>

### AgenticSeek

**Repo:** [Fosowl/agenticSeek](https://github.com/Fosowl/agenticSeek) · **License:** GPL-3.0 · **★ 27,691 (GitHub API, 2026-11-23)**

**Mục đích:** Trợ lý tự vận hành kết hợp tìm kiếm, duyệt web và công cụ lập trình với lựa chọn model cục bộ hoặc nhà cung cấp ngoài.

**Giá trị và cơ chế:** Đã đọc router: kết hợp classifier và BART zero-shot, ước lượng độ phức tạp rồi chọn planner hoặc agent chuyên biệt; browser agent khai báo công cụ tìm kiếm riêng.

**Giới hạn:** README gọi safe_mode là lọc best-effort, không phải sandbox. Docker vẫn đọc/ghi WORK_DIR và có mạng; chưa kiểm toàn bộ tác vụ. Tree không có CI liên quan nên giữ docs-read.

**Cách tham khảo/tích hợp:** Thử trong môi trường riêng, giới hạn thư mục và tài khoản; xác minh cấu hình provider trước khi đưa dữ liệu thực vào.

**Thay thế:** OpenManus, [OpenClaw](https://github.com/openclaw/openclaw), GenericAgent.

**Bằng chứng:** `docs-read`, ngày 2026-11-23, commit [`8f705be8ca62`](https://github.com/Fosowl/agenticSeek/commit/8f705be8ca625e9549389f188b1e37f700d3ed34). Đọc routing/classifier, phần khởi tạo browser agent và các đoạn security trong README; không thấy GitHub Actions workflow nên giữ docs-read, chưa kiểm toàn bộ thực thi công cụ. Chưa cài/chạy upstream.

**Nguồn:** [README.md](https://github.com/Fosowl/agenticSeek/blob/8f705be8ca625e9549389f188b1e37f700d3ed34/README.md) · [LICENSE](https://github.com/Fosowl/agenticSeek/blob/8f705be8ca625e9549389f188b1e37f700d3ed34/LICENSE) · [sources/router.py](https://github.com/Fosowl/agenticSeek/blob/8f705be8ca625e9549389f188b1e37f700d3ed34/sources/router.py) · [sources/agents/browser_agent.py](https://github.com/Fosowl/agenticSeek/blob/8f705be8ca625e9549389f188b1e37f700d3ed34/sources/agents/browser_agent.py) · [SECURITY.md](https://github.com/Fosowl/agenticSeek/blob/8f705be8ca625e9549389f188b1e37f700d3ed34/SECURITY.md) · [metadata GitHub](https://api.github.com/repos/Fosowl/agenticSeek).

<a id="anhkysuai-2026-11-23-rasa-open-source"></a>

### Rasa Open Source

**Repo:** [RasaHQ/rasa](https://github.com/RasaHQ/rasa) · **License:** Apache-2.0 · **★ 21,401 (GitHub API, 2026-11-23)**

**Mục đích:** Xây dựng trợ lý hội thoại với NLU, quản lý hội thoại và các kết nối kênh giao tiếp.

**Giá trị và cơ chế:** Manifest và README của nhánh nguồn này mô tả Rasa 3.x; phù hợp học pipeline intent/entity và điều phối phản hồi có cấu hình.

**Giới hạn:** README ghi dự án ở chế độ maintenance. Hello Rasa/CALM được dẫn sang sản phẩm mới, không nên gán mọi tính năng mới cho repo này; chưa kiểm runtime hoặc migration.

**Cách tham khảo/tích hợp:** Đối chiếu yêu cầu hỗ trợ và dependency, thử một flow hội thoại hoàn chỉnh rồi quyết định tiếp tục Rasa 3.x hay chuyển nền tảng.

**Thay thế:** [botpress](../08-awesome-lists-learning/README.md#6c516-nền-tảng-ai-rag--workflow), [LangGraph](../02-agent-frameworks/README.md#core-framework-semantics), Dialogflow.

**Bằng chứng:** `docs-read`, ngày 2026-11-23, commit [`60a3cff9c081`](https://github.com/RasaHQ/rasa/commit/60a3cff9c08183760355b07bd60f5223d8916d6b). README và các tài liệu/manifest/CI hiện diện, đọc chọn lọc; chưa kiểm implementation. Chưa cài/chạy upstream.

**Nguồn:** [README.md](https://github.com/RasaHQ/rasa/blob/60a3cff9c08183760355b07bd60f5223d8916d6b/README.md) · [LICENSE.txt](https://github.com/RasaHQ/rasa/blob/60a3cff9c08183760355b07bd60f5223d8916d6b/LICENSE.txt) · [metadata GitHub](https://api.github.com/repos/RasaHQ/rasa).

<a id="anhkysuai-2026-11-23-leon"></a>

### Leon

**Repo:** [leon-ai/leon](https://github.com/leon-ai/leon) · **License:** MIT · **★ 17,706 (GitHub API, 2026-11-23)**

**Mục đích:** Trợ lý cá nhân tự host với hệ thống kỹ năng, giao tiếp và lựa chọn model.

**Giá trị và cơ chế:** README và manifest cho thấy hướng Leon 2.0 alpha, mô tả server, giao diện web và các thành phần phục vụ thực thi kỹ năng.

**Giới hạn:** Nhánh develop là bản đang xây dựng, chưa phải bản 2.0 phát hành; một số tài liệu công khai còn thuộc phiên bản trước. Chưa kiểm implementation hoặc độ ổn định.

**Cách tham khảo/tích hợp:** Ghim commit và đối chiếu tài liệu cùng phiên bản, thử kỹ năng ít quyền trong môi trường riêng trước khi kết nối dữ liệu cá nhân.

**Thay thế:** [OpenClaw](https://github.com/openclaw/openclaw), Octop, GenericAgent.

**Bằng chứng:** `docs-read`, ngày 2026-11-23, commit [`cddd7020b327`](https://github.com/leon-ai/leon/commit/cddd7020b32709148d5810d88f8b2096302e9fe9). README và các tài liệu/manifest/CI hiện diện, đọc chọn lọc; chưa kiểm implementation. Chưa cài/chạy upstream.

**Nguồn:** [README.md](https://github.com/leon-ai/leon/blob/cddd7020b32709148d5810d88f8b2096302e9fe9/README.md) · [LICENSE.md](https://github.com/leon-ai/leon/blob/cddd7020b32709148d5810d88f8b2096302e9fe9/LICENSE.md) · [metadata GitHub](https://api.github.com/repos/leon-ai/leon).

## 5. Nguồn

- https://www.firecrawl.dev/blog/best-open-source-agent-frameworks
- https://dreaming.press/posts/ai-agent-frameworks-github-ranked-by-stars-2026.html
- https://unifiedplatforms.com/blogs/web-development/agentic-ai-frameworks-compared/
- https://the-agent-report.com/2026/07/ai-agent-frameworks-comparison-2026-langgraph-crewai-autogen/
- https://pickaxe.co/post/top-ai-agent-frameworks · https://pickaxe.co/post/crewai-vs-langgraph-vs-autogen
- https://www.langchain.com/resources/ai-agent-frameworks
- https://cordum.io/blog/langchain-vs-llamaindex-vs-semantic-kernel · https://uvik.net/blog/python-ai-agent-frameworks/
- https://github.com/NousResearch/hermes-agent · https://github.com/FoundationAgents/MetaGPT · https://github.com/OpenBMB/ChatDev · https://github.com/bytedance/deer-flow · https://github.com/ag2ai/ag2 · https://github.com/camel-ai/camel · https://github.com/VRSEN/agency-swarm · https://github.com/Pythagora-io/gpt-pilot · https://github.com/ruvnet/ruflo (đọc qua docs nội bộ của X-Agents/Hermes-Agents, 2026-10-12)
- OpenCompany (đọc 2026-10-12): https://github.com/zeenie-ai/OpenCompany (README, CONTRIBUTING, CLAUDE.md, LICENSE, releases, issues #128 #129 #132–134 #143 #145, `docs-internal/{agent_teams,employee_teams,normal_mode,memory_compaction,agent_context_flow}.md`, RFC-0001..0003, `server/nodes/README.md`, `server/skills/**/SKILL.md`, `client/src/features/home/hire/starters.json`) · https://opencompany.sh · https://docs.opencompany.sh · https://reporank.net/en/repo/zeenie-ai-opencompany.html · https://www.opensourcealternatives.to/item/opencompany · https://cloudnews.tech/machinaos-wants-to-bring-the-ai-personal-assistant-from-the-cloud-to-your-own-server/ · https://www.everydev.ai/developers/zeenie-ai (chưa xác minh) · https://github.com/paperclipai/paperclip · https://github.com/HKUDS/OpenOPC · https://github.com/tinyhumansai/opencompany (trùng tên)
- https://github.com/openclaw/openclaw · https://www.digitalocean.com/resources/articles/what-is-openclaw · https://www.freecodecamp.org/news/how-to-build-and-secure-a-personal-ai-agent-with-openclaw/
- Munder Difflin (2026-10-12): https://github.com/harnessmd/munder-difflin (clone đầy đủ; README, HIVE.md, TELEMETRY.md, src/shared/agentProvider.ts, src/main/analytics.ts) · https://github.com/chaitanyagiri/munder-difflin (URL cũ) · https://trendshift.io/repositories/46562 · https://www.producthunt.com/products/munder-difflin · https://harnessmd.com · https://munderdiffl.in

<a id="chuan-hoa-2026-11-23"></a>

## Chuẩn hóa bằng chứng hồ sơ cũ — 23/11/2026

Các hồ sơ dưới đây có từ trước khi kho ghi mức kiểm. Ngày 2026-11-23 mỗi repo được clone nông tại commit ghi trong bảng, đọc LICENSE, README, manifest và CI (nếu có); không cài, build hay chạy mã upstream. Nhận định cũ ở phần trên giữ nguyên; chỗ nào khác với lần đọc này được ghi trong cột Nhận định. Số sao lấy qua GitHub search API cùng ngày.

<a id="ch-ag2"></a>

### AG2

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/ag2ai/ag2 |
| License | Apache-2.0 |
| Phiên bản đã đọc | `db7194e8e26705381d9d23c402ba2bc5cadc67fa` (commit 2026-11-22) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE, pyproject.toml, workflows; chưa chạy upstream |
| Bảo trì | Hoạt động, commit 2026-11-22 |
| Nhận định | Khởi nguồn là fork cộng đồng AutoGen 0.2 (11/2024) nhưng nay là framework agent viết lại, Python ≥3.11, có middleware/memory policy. Mã dùng `autogen` cũ phải chuyển sang `ag2-classic`; độ ổn định API mới **(chưa xác minh)**. |
| Nguồn | [README.md](https://github.com/ag2ai/ag2/blob/db7194e8e26705381d9d23c402ba2bc5cadc67fa/README.md) · [LICENSE](https://github.com/ag2ai/ag2/blob/db7194e8e26705381d9d23c402ba2bc5cadc67fa/LICENSE) · [pyproject.toml](https://github.com/ag2ai/ag2/blob/db7194e8e26705381d9d23c402ba2bc5cadc67fa/pyproject.toml) · [workflows](https://github.com/ag2ai/ag2/tree/db7194e8e26705381d9d23c402ba2bc5cadc67fa/.github/workflows) |

<a id="ch-agency-swarm"></a>

### agency-swarm

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/VRSEN/agency-swarm |
| License | MIT |
| Phiên bản đã đọc | `016189784354b4298ed25de752d22013ee5b5511` (commit 2026-11-16) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE, pyproject.toml, package.json, workflows; chưa chạy upstream |
| Bảo trì | Hoạt động, commit 2026-11-16 |
| Nhận định | Framework "agency": agent có vai trò, luồng giao tiếp có hướng khai báo trên `Agency`, tool kiểu Pydantic. Phụ thuộc OpenAI Agents SDK; nhãn "production-ready" và coverage 92% là tuyên bố README **(chưa xác minh)**. |
| Nguồn | [README.md](https://github.com/VRSEN/agency-swarm/blob/016189784354b4298ed25de752d22013ee5b5511/README.md) · [LICENSE](https://github.com/VRSEN/agency-swarm/blob/016189784354b4298ed25de752d22013ee5b5511/LICENSE) · [pyproject.toml](https://github.com/VRSEN/agency-swarm/blob/016189784354b4298ed25de752d22013ee5b5511/pyproject.toml) · [package.json](https://github.com/VRSEN/agency-swarm/blob/016189784354b4298ed25de752d22013ee5b5511/package.json) · [workflows](https://github.com/VRSEN/agency-swarm/tree/016189784354b4298ed25de752d22013ee5b5511/.github/workflows) |

<a id="ch-agentbench"></a>

### AgentBench

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/THUDM/AgentBench |
| License | Apache-2.0 |
| Phiên bản đã đọc | `d1e4a10db08c87075c78972e48ecc182be03e2d5` (commit 2026-02-09) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE, workflows; chưa chạy upstream |
| Bảo trì | Commit cuối 2026-02-09, ít hoạt động |
| Nhận định | Benchmark agent nhiều môi trường, bản FC dùng prompt function-calling, dựng bằng Docker Compose; bản cũ ở tag v0.1/v0.2. Nặng về hạ tầng và không có commit mới từ 2/2026. |
| Nguồn | [README.md](https://github.com/THUDM/AgentBench/blob/d1e4a10db08c87075c78972e48ecc182be03e2d5/README.md) · [LICENSE](https://github.com/THUDM/AgentBench/blob/d1e4a10db08c87075c78972e48ecc182be03e2d5/LICENSE) · [workflows](https://github.com/THUDM/AgentBench/tree/d1e4a10db08c87075c78972e48ecc182be03e2d5/.github/workflows) |

<a id="ch-agentscope-2-0"></a>

### AgentScope 2.0

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/agentscope-ai/agentscope |
| License | Apache-2.0 |
| Phiên bản đã đọc | `f25a15bd3a1b902abe03e977c91e722379d8e31e` (commit 2026-11-23) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE, pyproject.toml, workflows; chưa chạy upstream |
| Bảo trì | Hoạt động, commit 2026-11-23 |
| Nhận định | Nền tảng đa agent của Alibaba, tài liệu song ngữ, CI đầy đủ (unittest, pre-commit, publish). Danh sách tính năng 2.0 theo hồ sơ cũ **(chưa xác minh đợt này)**. |
| Nguồn | [README.md](https://github.com/agentscope-ai/agentscope/blob/f25a15bd3a1b902abe03e977c91e722379d8e31e/README.md) · [LICENSE](https://github.com/agentscope-ai/agentscope/blob/f25a15bd3a1b902abe03e977c91e722379d8e31e/LICENSE) · [pyproject.toml](https://github.com/agentscope-ai/agentscope/blob/f25a15bd3a1b902abe03e977c91e722379d8e31e/pyproject.toml) · [workflows](https://github.com/agentscope-ai/agentscope/tree/f25a15bd3a1b902abe03e977c91e722379d8e31e/.github/workflows) |

<a id="ch-autogen"></a>

### AutoGen

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/microsoft/autogen |
| License | MIT (mã, LICENSE-CODE) + CC-BY-4.0 (tài liệu, LICENSE) (catalog cũ: MIT) |
| Phiên bản đã đọc | `8390985108cb1e3881f5f7297765758d8ad2540c` (commit 2026-11-12) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE, LICENSE-CODE, workflows; chưa chạy upstream |
| Bảo trì | README ghi archived, không còn bảo trì; commit cuối 2026-11-12 |
| Nhận định | Framework đa agent tiên phong của Microsoft Research (Python + .NET). README cảnh báo dùng repo archive có rủi ro bảo mật; dự án mới nên dùng Microsoft Agent Framework. |
| Nguồn | [README.md](https://github.com/microsoft/autogen/blob/8390985108cb1e3881f5f7297765758d8ad2540c/README.md) · [LICENSE](https://github.com/microsoft/autogen/blob/8390985108cb1e3881f5f7297765758d8ad2540c/LICENSE) · [LICENSE-CODE](https://github.com/microsoft/autogen/blob/8390985108cb1e3881f5f7297765758d8ad2540c/LICENSE-CODE) · [workflows](https://github.com/microsoft/autogen/tree/8390985108cb1e3881f5f7297765758d8ad2540c/.github/workflows) |

<a id="ch-berkeley-function-calling-leaderboard-gorilla"></a>

### Berkeley Function Calling Leaderboard (gorilla)

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/ShishirPatil/gorilla |
| License | Apache-2.0 |
| Phiên bản đã đọc | `6ea57973c7a6097fd7c5915698c54c17c5b1b6c8` (commit 2026-03-23) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE, workflows; chưa chạy upstream |
| Bảo trì | Commit cuối 2026-03-23, ít hoạt động |
| Nhận định | Monorepo Gorilla gồm BFCL, GoEx, RAFT, OpenFunctions; BFCL chấm gọi hàm AST/thực thi, multi-turn, agentic, phát hành gói `bfcl_eval` qua workflow PyPI. Hoạt động thưa từ 2026. |
| Nguồn | [README.md](https://github.com/ShishirPatil/gorilla/blob/6ea57973c7a6097fd7c5915698c54c17c5b1b6c8/README.md) · [LICENSE](https://github.com/ShishirPatil/gorilla/blob/6ea57973c7a6097fd7c5915698c54c17c5b1b6c8/LICENSE) · [workflows](https://github.com/ShishirPatil/gorilla/tree/6ea57973c7a6097fd7c5915698c54c17c5b1b6c8/.github/workflows) |

<a id="ch-camel"></a>

### CAMEL

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/camel-ai/camel |
| License | Apache-2.0 |
| Phiên bản đã đọc | `c9f270d06b80d408809ff4553557a7f5ec4aef64` (commit 2026-11-23) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.ja.md, LICENSE, pyproject.toml, workflows; chưa chạy upstream |
| Bảo trì | Hoạt động, commit 2026-11-23 |
| Nhận định | Framework agent nhập vai/sinh dữ liệu đa agent của CAMEL-AI, kèm apps và services. CI rộng (pytest, CodeQL, scorecard); tuyên bố quy mô cộng đồng **(chưa xác minh)**. |
| Nguồn | [README.ja.md](https://github.com/camel-ai/camel/blob/c9f270d06b80d408809ff4553557a7f5ec4aef64/README.ja.md) · [LICENSE](https://github.com/camel-ai/camel/blob/c9f270d06b80d408809ff4553557a7f5ec4aef64/LICENSE) · [pyproject.toml](https://github.com/camel-ai/camel/blob/c9f270d06b80d408809ff4553557a7f5ec4aef64/pyproject.toml) · [workflows](https://github.com/camel-ai/camel/tree/c9f270d06b80d408809ff4553557a7f5ec4aef64/.github/workflows) |

<a id="ch-chatdev"></a>

### ChatDev

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/OpenBMB/ChatDev |
| License | Apache-2.0 |
| Phiên bản đã đọc | `464a681ba7bda869db97a50c5fa707c9a0fb57a0` (commit 2026-10-30) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README-zh.md, LICENSE, pyproject.toml, package.json, workflows; chưa chạy upstream |
| Bảo trì | Hoạt động, commit 2026-10-30 |
| Nhận định | DevAll điều phối workflow đa agent qua cấu hình (frontend + server Python 3.12), không còn chỉ là "công ty phần mềm ảo". Hồ sơ so sánh dựa trên 1.0 cần ghi rõ nhánh `chatdev1.0`. |
| Nguồn | [README-zh.md](https://github.com/OpenBMB/ChatDev/blob/464a681ba7bda869db97a50c5fa707c9a0fb57a0/README-zh.md) · [LICENSE](https://github.com/OpenBMB/ChatDev/blob/464a681ba7bda869db97a50c5fa707c9a0fb57a0/LICENSE) · [pyproject.toml](https://github.com/OpenBMB/ChatDev/blob/464a681ba7bda869db97a50c5fa707c9a0fb57a0/pyproject.toml) · [package.json](https://github.com/OpenBMB/ChatDev/blob/464a681ba7bda869db97a50c5fa707c9a0fb57a0/package.json) · [workflows](https://github.com/OpenBMB/ChatDev/tree/464a681ba7bda869db97a50c5fa707c9a0fb57a0/.github/workflows) |

<a id="ch-claude-agent-sdk-python"></a>

### Claude Agent SDK (Python)

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/anthropics/claude-agent-sdk-python |
| License | MIT (+ Anthropic Commercial Terms; CLI nhúng mã đóng) |
| Phiên bản đã đọc | `3184360393a92ca8a6ec7bbbdee571afd1ce1c56` (commit 2026-11-20) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE, pyproject.toml, workflows; chưa chạy upstream |
| Bảo trì | Hoạt động, commit 2026-11-20 |
| Nhận định | SDK Python bọc Claude Code CLI làm vòng lặp agent (`query`, client hai chiều, tool/hook). Phụ thuộc CLI mã đóng; ngữ nghĩa `allowed_tools` theo hồ sơ cũ **(chưa xác minh đợt này)**. |
| Nguồn | [README.md](https://github.com/anthropics/claude-agent-sdk-python/blob/3184360393a92ca8a6ec7bbbdee571afd1ce1c56/README.md) · [LICENSE](https://github.com/anthropics/claude-agent-sdk-python/blob/3184360393a92ca8a6ec7bbbdee571afd1ce1c56/LICENSE) · [pyproject.toml](https://github.com/anthropics/claude-agent-sdk-python/blob/3184360393a92ca8a6ec7bbbdee571afd1ce1c56/pyproject.toml) · [workflows](https://github.com/anthropics/claude-agent-sdk-python/tree/3184360393a92ca8a6ec7bbbdee571afd1ce1c56/.github/workflows) |

<a id="ch-crewai"></a>

### CrewAI

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/crewAIInc/crewAI |
| License | MIT |
| Phiên bản đã đọc | `6a5b80c4551a562004f342f46c8d1470627f535f` (commit 2026-11-23) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE, pyproject.toml, workflows; chưa chạy upstream |
| Bảo trì | Hoạt động, commit 2026-11-23 |
| Nhận định | Framework điều phối "crew" agent theo vai trò, kèm Flows; có bản cloud thương mại song song. Tuyên bố hiệu năng/marketing trong README **(chưa xác minh)**. |
| Nguồn | [README.md](https://github.com/crewAIInc/crewAI/blob/6a5b80c4551a562004f342f46c8d1470627f535f/README.md) · [LICENSE](https://github.com/crewAIInc/crewAI/blob/6a5b80c4551a562004f342f46c8d1470627f535f/LICENSE) · [pyproject.toml](https://github.com/crewAIInc/crewAI/blob/6a5b80c4551a562004f342f46c8d1470627f535f/pyproject.toml) · [workflows](https://github.com/crewAIInc/crewAI/tree/6a5b80c4551a562004f342f46c8d1470627f535f/.github/workflows) |

<a id="ch-deerflow"></a>

### DeerFlow

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/bytedance/deer-flow |
| License | MIT |
| Phiên bản đã đọc | `fc0d4bd7bc2602b4ff0abdc8600545b23b620ef9` (commit 2026-11-23) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE, workflows; chưa chạy upstream |
| Bảo trì | Hoạt động, commit 2026-11-23 |
| Nhận định | Harness đa agent của ByteDance cho research/coding dài hơi, nhiều workflow CI (backend, frontend, e2e). README quảng bá model Volcengine; khả năng "làm hầu hết mọi việc" **(chưa xác minh)**. |
| Nguồn | [README.md](https://github.com/bytedance/deer-flow/blob/fc0d4bd7bc2602b4ff0abdc8600545b23b620ef9/README.md) · [LICENSE](https://github.com/bytedance/deer-flow/blob/fc0d4bd7bc2602b4ff0abdc8600545b23b620ef9/LICENSE) · [workflows](https://github.com/bytedance/deer-flow/tree/fc0d4bd7bc2602b4ff0abdc8600545b23b620ef9/.github/workflows) |

<a id="ch-eve"></a>

### eve

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/vercel/eve |
| License | Apache-2.0 |
| Phiên bản đã đọc | `e254c0ff805dbe126fefc011defe23f057fefacf` (commit 2026-11-22) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE, package.json, workflows; chưa chạy upstream |
| Bảo trì | Hoạt động, commit 2026-11-22 |
| Nhận định | Framework agent của Vercel, cấu trúc `agent/` theo thư mục (instructions, tools, skills…), nhắm triển khai trên Vercel. Telemetry bật sẵn, không đọc DO_NOT_TRACK theo hồ sơ cũ **(chưa xác minh đợt này)**. |
| Nguồn | [README.md](https://github.com/vercel/eve/blob/e254c0ff805dbe126fefc011defe23f057fefacf/README.md) · [LICENSE](https://github.com/vercel/eve/blob/e254c0ff805dbe126fefc011defe23f057fefacf/LICENSE) · [package.json](https://github.com/vercel/eve/blob/e254c0ff805dbe126fefc011defe23f057fefacf/package.json) · [workflows](https://github.com/vercel/eve/tree/e254c0ff805dbe126fefc011defe23f057fefacf/.github/workflows) |

<a id="ch-google-adk"></a>

### Google ADK

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/google/adk-python |
| License | Apache-2.0 |
| Phiên bản đã đọc | `4d9e2c75f92305b335f8e66f8b4a8ea99f13017f` (commit 2026-11-22) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE, pyproject.toml, workflows; chưa chạy upstream |
| Bảo trì | Hoạt động, commit 2026-11-22 |
| Nhận định | Bộ công cụ code-first của Google để xây, đánh giá, triển khai agent; có ADK Web và repo recipes riêng. Tích hợp A2A **(chưa xác minh đợt này)**. |
| Nguồn | [README.md](https://github.com/google/adk-python/blob/4d9e2c75f92305b335f8e66f8b4a8ea99f13017f/README.md) · [LICENSE](https://github.com/google/adk-python/blob/4d9e2c75f92305b335f8e66f8b4a8ea99f13017f/LICENSE) · [pyproject.toml](https://github.com/google/adk-python/blob/4d9e2c75f92305b335f8e66f8b4a8ea99f13017f/pyproject.toml) · [workflows](https://github.com/google/adk-python/tree/4d9e2c75f92305b335f8e66f8b4a8ea99f13017f/.github/workflows) |

<a id="ch-gpt-pilot"></a>

### gpt-pilot

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/Pythagora-io/gpt-pilot |
| License | FSL-1.1-MIT (Functional Source License, chuyển MIT sau thời hạn) (catalog cũ: MIT) |
| Phiên bản đã đọc | `9b763fdaf0020c7d8abacc7b58b2b09e57494623` (commit 2026-06-12) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE, pyproject.toml, workflows; chưa chạy upstream |
| Bảo trì | README ghi không còn bảo trì; commit cuối 2026-06-12 |
| Nhận định | Agent dev AI theo bước của Pythagora, đã ngừng bảo trì. README hướng dẫn ai đã chạy từ nguồn trong khoảng 8/2025–6/2026 phải xoay vòng mọi credential; không nên dùng, chỉ tham khảo như bài học chuỗi cung ứng. |
| Nguồn | [README.md](https://github.com/Pythagora-io/gpt-pilot/blob/9b763fdaf0020c7d8abacc7b58b2b09e57494623/README.md) · [LICENSE](https://github.com/Pythagora-io/gpt-pilot/blob/9b763fdaf0020c7d8abacc7b58b2b09e57494623/LICENSE) · [pyproject.toml](https://github.com/Pythagora-io/gpt-pilot/blob/9b763fdaf0020c7d8abacc7b58b2b09e57494623/pyproject.toml) · [workflows](https://github.com/Pythagora-io/gpt-pilot/tree/9b763fdaf0020c7d8abacc7b58b2b09e57494623/.github/workflows) |

<a id="ch-haystack"></a>

### Haystack

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/deepset-ai/haystack |
| License | Apache-2.0 |
| Phiên bản đã đọc | `9b38a55242d3aaa3020ad63f2d5b2731cdc03a2a` (commit 2026-11-23) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE, pyproject.toml, workflows; chưa chạy upstream |
| Bảo trì | Hoạt động, commit 2026-11-23 |
| Nhận định | Framework LLM ghép component thành pipeline/agent (RAG, converter, vector DB), CI dày (tests, CodeQL, fuzz). Ghi chú cũ trống nội dung nay bổ sung mô tả. |
| Nguồn | [README.md](https://github.com/deepset-ai/haystack/blob/9b38a55242d3aaa3020ad63f2d5b2731cdc03a2a/README.md) · [LICENSE](https://github.com/deepset-ai/haystack/blob/9b38a55242d3aaa3020ad63f2d5b2731cdc03a2a/LICENSE) · [pyproject.toml](https://github.com/deepset-ai/haystack/blob/9b38a55242d3aaa3020ad63f2d5b2731cdc03a2a/pyproject.toml) · [workflows](https://github.com/deepset-ai/haystack/tree/9b38a55242d3aaa3020ad63f2d5b2731cdc03a2a/.github/workflows) |

<a id="ch-hermes-agent"></a>

### Hermes Agent

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/NousResearch/hermes-agent |
| License | MIT (catalog cũ: –) |
| Phiên bản đã đọc | `45665879083359efe1fc5134ddd2f5dffd804139` (commit 2026-11-23) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.es.md, LICENSE, package.json, workflows; chưa chạy upstream |
| Bảo trì | Hoạt động, commit 2026-11-23 |
| Nhận định | Agent cá nhân mã mở chạy CLI/TUI/desktop với gateway nhắn tin, tự tạo skill từ kinh nghiệm. Giới hạn `delegate_task` và cơ chế gateway theo docs nội bộ **(chưa xác minh)**. |
| Nguồn | [README.es.md](https://github.com/NousResearch/hermes-agent/blob/45665879083359efe1fc5134ddd2f5dffd804139/README.es.md) · [LICENSE](https://github.com/NousResearch/hermes-agent/blob/45665879083359efe1fc5134ddd2f5dffd804139/LICENSE) · [package.json](https://github.com/NousResearch/hermes-agent/blob/45665879083359efe1fc5134ddd2f5dffd804139/package.json) · [workflows](https://github.com/NousResearch/hermes-agent/tree/45665879083359efe1fc5134ddd2f5dffd804139/.github/workflows) |

<a id="ch-langchain"></a>

### LangChain

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/langchain-ai/langchain |
| License | MIT |
| Phiên bản đã đọc | `4af34be7bee448ef32ea4f100b61e6df09a74cf6` (commit 2026-11-22) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE, workflows; chưa chạy upstream |
| Bảo trì | Hoạt động, commit 2026-11-22 |
| Nhận định | Framework xây agent và ứng dụng LLM với nhiều tích hợp bên thứ ba; hệ sinh thái lớn (LangGraph, LangSmith). Ghi chú cũ trống nội dung nay bổ sung mô tả. |
| Nguồn | [README.md](https://github.com/langchain-ai/langchain/blob/4af34be7bee448ef32ea4f100b61e6df09a74cf6/README.md) · [LICENSE](https://github.com/langchain-ai/langchain/blob/4af34be7bee448ef32ea4f100b61e6df09a74cf6/LICENSE) · [workflows](https://github.com/langchain-ai/langchain/tree/4af34be7bee448ef32ea4f100b61e6df09a74cf6/.github/workflows) |

<a id="ch-llamaindex"></a>

### LlamaIndex

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/run-llama/llama_index |
| License | MIT |
| Phiên bản đã đọc | `99d7433f6f71888951379ccca9294e272442c832` (commit 2026-11-13) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE, pyproject.toml, workflows; chưa chạy upstream |
| Bảo trì | Hoạt động (trọng tâm công ty chuyển sang LlamaParse); commit 2026-11-13 |
| Nhận định | Framework RAG/agent trên dữ liệu (core + integrations). Vẫn có commit (2026-11-13) nhưng README báo dịch ưu tiên sang LlamaParse — rủi ro chậm phát triển dài hạn. |
| Nguồn | [README.md](https://github.com/run-llama/llama_index/blob/99d7433f6f71888951379ccca9294e272442c832/README.md) · [LICENSE](https://github.com/run-llama/llama_index/blob/99d7433f6f71888951379ccca9294e272442c832/LICENSE) · [pyproject.toml](https://github.com/run-llama/llama_index/blob/99d7433f6f71888951379ccca9294e272442c832/pyproject.toml) · [workflows](https://github.com/run-llama/llama_index/tree/99d7433f6f71888951379ccca9294e272442c832/.github/workflows) |

<a id="ch-mastra"></a>

### Mastra

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/mastra-ai/mastra |
| License | Apache-2.0 + Mastra Enterprise License cho thư mục `ee/` (catalog cũ: Apache-2.0) |
| Phiên bản đã đọc | `3fe2318cba624a0e48cff0ec5c8503bfa0a4804b` (commit 2026-11-23) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE.md, package.json, workflows; chưa chạy upstream |
| Bảo trì | Hoạt động, commit 2026-11-23 |
| Nhận định | Framework agent/workflow TypeScript (model routing, workflow đồ thị, human-in-the-loop, MCP). Khi nhúng cần tránh hoặc mua license cho mã `ee/`. |
| Nguồn | [README.md](https://github.com/mastra-ai/mastra/blob/3fe2318cba624a0e48cff0ec5c8503bfa0a4804b/README.md) · [LICENSE.md](https://github.com/mastra-ai/mastra/blob/3fe2318cba624a0e48cff0ec5c8503bfa0a4804b/LICENSE.md) · [package.json](https://github.com/mastra-ai/mastra/blob/3fe2318cba624a0e48cff0ec5c8503bfa0a4804b/package.json) · [workflows](https://github.com/mastra-ai/mastra/tree/3fe2318cba624a0e48cff0ec5c8503bfa0a4804b/.github/workflows) |

<a id="ch-metagpt"></a>

### MetaGPT

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/FoundationAgents/MetaGPT |
| License | MIT |
| Phiên bản đã đọc | `11cdf466d042aece04fc6cfd13b28e1a70341b1f` (commit 2026-01-21) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE, danh sách .github/workflows; chưa chạy upstream |
| Bảo trì | Ít hoạt động: commit HEAD 2026-01-21 (~10 tháng); README chỉ có tin tới 3/2025, trọng tâm chuyển sang sản phẩm MGX |
| Nhận định | Khung đa agent mô phỏng công ty phần mềm (PM/kiến trúc sư/kỹ sư) theo SOP, `Code = SOP(Team)`; đáng đọc để học mẫu SOP/vai trò. HEAD đứng yên từ 1/2026 nên không hợp cho dự án mới. |
| Nguồn | [README](https://github.com/FoundationAgents/MetaGPT/blob/11cdf466d042aece04fc6cfd13b28e1a70341b1f/README.md) · [LICENSE](https://github.com/FoundationAgents/MetaGPT/blob/11cdf466d042aece04fc6cfd13b28e1a70341b1f/LICENSE) · [workflows](https://github.com/FoundationAgents/MetaGPT/tree/11cdf466d042aece04fc6cfd13b28e1a70341b1f/.github/workflows) |

<a id="ch-munder-difflin"></a>

### Munder Difflin

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/HarnessMD/munder-difflin |
| License | MIT (mã nguồn); asset pixel-art LimeZu theo license riêng, cần ghi công (LICENSE-ASSETS) |
| Phiên bản đã đọc | `d86ab7acd2c5b817a4ec80d897a44a1db7e8062e` (commit 2026-11-23) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE, LICENSE-ASSETS, package.json, danh sách .github/workflows; chưa chạy upstream |
| Bảo trì | Hoạt động: commit 2026-11-23; package.json 0.6.0 |
| Nhận định | App desktop Electron chạy 'văn phòng' agent qua CLI thật của từng nhà cung cấp, Michael làm điều phối, dữ liệu là file cục bộ. README gọi bản này là 'Classic' MIT, phát hành dạng mã nguồn tự build; các tuyên bố về 12 engine là **(chưa xác minh)**. |
| Nguồn | [README](https://github.com/HarnessMD/munder-difflin/blob/d86ab7acd2c5b817a4ec80d897a44a1db7e8062e/README.md) · [LICENSE](https://github.com/HarnessMD/munder-difflin/blob/d86ab7acd2c5b817a4ec80d897a44a1db7e8062e/LICENSE) · [LICENSE-ASSETS](https://github.com/HarnessMD/munder-difflin/blob/d86ab7acd2c5b817a4ec80d897a44a1db7e8062e/LICENSE-ASSETS) · [package.json](https://github.com/HarnessMD/munder-difflin/blob/d86ab7acd2c5b817a4ec80d897a44a1db7e8062e/package.json) · [workflows](https://github.com/HarnessMD/munder-difflin/tree/d86ab7acd2c5b817a4ec80d897a44a1db7e8062e/.github/workflows) |

<a id="ch-nanobot"></a>

### nanobot

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/HKUDS/nanobot |
| License | MIT |
| Phiên bản đã đọc | `37c2af8ffc86c5adf0a9e42732e26722d8a4260b` (commit 2026-11-23) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE, pyproject.toml, danh sách .github/workflows; chưa chạy upstream |
| Bảo trì | Hoạt động: commit 2026-11-23; pyproject 0.4.2 (Alpha) |
| Nhận định | Framework trợ lý AI cá nhân tự host (Python ≥3.11, gói `nanobot-ai`), có WebUI/TUI và kênh chat. Nhãn 'lightweight' là tự mô tả; mặc định workspace/sandbox chưa đọc lại ở lượt này **(chưa xác minh)**. |
| Nguồn | [README](https://github.com/HKUDS/nanobot/blob/37c2af8ffc86c5adf0a9e42732e26722d8a4260b/README.md) · [LICENSE](https://github.com/HKUDS/nanobot/blob/37c2af8ffc86c5adf0a9e42732e26722d8a4260b/LICENSE) · [pyproject.toml](https://github.com/HKUDS/nanobot/blob/37c2af8ffc86c5adf0a9e42732e26722d8a4260b/pyproject.toml) · [workflows](https://github.com/HKUDS/nanobot/tree/37c2af8ffc86c5adf0a9e42732e26722d8a4260b/.github/workflows) |

<a id="ch-nanoclaw"></a>

### NanoClaw

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/nanocoai/nanoclaw |
| License | MIT |
| Phiên bản đã đọc | `53099d281f894521049e3930ee9e56d0dad7c1cf` (commit 2026-11-22) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE, package.json, danh sách .github/workflows; chưa chạy upstream |
| Bảo trì | Hoạt động: commit 2026-11-22; package.json 2026.11.0 |
| Nhận định | Trợ lý AI chạy mỗi agent trong container Linux riêng, tự định vị là bản gọn của OpenClaw; mới thêm luồng Slack mỗi agent một app qua tài khoản NanoClaw. Tuyên bố cách ly OS-level là của tác giả **(chưa xác minh)**. |
| Nguồn | [README](https://github.com/nanocoai/nanoclaw/blob/53099d281f894521049e3930ee9e56d0dad7c1cf/README.md) · [LICENSE](https://github.com/nanocoai/nanoclaw/blob/53099d281f894521049e3930ee9e56d0dad7c1cf/LICENSE) · [package.json](https://github.com/nanocoai/nanoclaw/blob/53099d281f894521049e3930ee9e56d0dad7c1cf/package.json) · [workflows](https://github.com/nanocoai/nanoclaw/tree/53099d281f894521049e3930ee9e56d0dad7c1cf/.github/workflows) |

<a id="ch-openclaw"></a>

### OpenClaw

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/openclaw/openclaw |
| License | MIT |
| Phiên bản đã đọc | `1601f86def0c0c1cb15feec3b45f6151a9e09e9f` (commit 2026-11-23) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE, package.json, danh sách .github/workflows; chưa chạy upstream |
| Bảo trì | Hoạt động: commit 2026-11-23; package.json 2026.11.7; CI rất lớn |
| Nhận định | Trợ lý AI tự host nối vào 20+ kênh chat và app native, do OpenClaw Foundation (501(c)(3)) quản lý. README nói mặc định chỉ gửi kiểm tra phiên bản hằng ngày, thống kê ẩn danh là opt-in **(chưa xác minh)**. |
| Nguồn | [README](https://github.com/openclaw/openclaw/blob/1601f86def0c0c1cb15feec3b45f6151a9e09e9f/README.md) · [LICENSE](https://github.com/openclaw/openclaw/blob/1601f86def0c0c1cb15feec3b45f6151a9e09e9f/LICENSE) · [package.json](https://github.com/openclaw/openclaw/blob/1601f86def0c0c1cb15feec3b45f6151a9e09e9f/package.json) · [workflows](https://github.com/openclaw/openclaw/tree/1601f86def0c0c1cb15feec3b45f6151a9e09e9f/.github/workflows) |

<a id="ch-opencompany-ex-machinaos"></a>

### OpenCompany (ex-MachinaOS)

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/zeenie-ai/OpenCompany |
| License | MIT |
| Phiên bản đã đọc | `cfb06d6cf6daa32e0605f17f4ccf796ecefdca04` (commit 2026-11-23) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE, package.json, pyproject.toml, danh sách .github/workflows; chưa chạy upstream |
| Bảo trì | Hoạt động: commit 2026-11-23; npm `@zeenie-ai/opencompany` 0.3.2 |
| Nhận định | Hệ điều hành 'nhân viên AI' tự host: Chat Employee + Orchestrator giao việc cho các vai trò, có quyền truy cập trình duyệt/app/máy. Quyền truy cập rộng là rủi ro chính; các nhận định cũ (secret dev commit sẵn, bus-factor) chưa đọc lại ở lượt này. |
| Nguồn | [README](https://github.com/zeenie-ai/OpenCompany/blob/cfb06d6cf6daa32e0605f17f4ccf796ecefdca04/README.md) · [LICENSE](https://github.com/zeenie-ai/OpenCompany/blob/cfb06d6cf6daa32e0605f17f4ccf796ecefdca04/LICENSE) · [package.json](https://github.com/zeenie-ai/OpenCompany/blob/cfb06d6cf6daa32e0605f17f4ccf796ecefdca04/package.json) · [pyproject.toml](https://github.com/zeenie-ai/OpenCompany/blob/cfb06d6cf6daa32e0605f17f4ccf796ecefdca04/pyproject.toml) · [workflows](https://github.com/zeenie-ai/OpenCompany/tree/cfb06d6cf6daa32e0605f17f4ccf796ecefdca04/.github/workflows) |

<a id="ch-openopc"></a>

### OpenOPC

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/HKUDS/OpenOPC |
| License | MIT |
| Phiên bản đã đọc | `9824f41f18d31801b97ce87f58c7151b5c080047` (commit 2026-11-23) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE, pyproject.toml, danh sách .github/workflows; chưa chạy upstream |
| Bảo trì | Hoạt động: commit 2026-11-23; repo vẫn truy cập được |
| Nhận định | Repo vẫn tồn tại nhưng sản phẩm đã đổi tên thành **AutoSwarm** (pyproject `autoswarm` 2.0.0.dev0): điều phối nhiều agent khác nhau, chia sẻ context, có app desktop. Các tuyên bố phối hợp/song song là của tác giả **(chưa xác minh)**. |
| Nguồn | [README](https://github.com/HKUDS/OpenOPC/blob/9824f41f18d31801b97ce87f58c7151b5c080047/README.md) · [LICENSE](https://github.com/HKUDS/OpenOPC/blob/9824f41f18d31801b97ce87f58c7151b5c080047/LICENSE) · [pyproject.toml](https://github.com/HKUDS/OpenOPC/blob/9824f41f18d31801b97ce87f58c7151b5c080047/pyproject.toml) · [workflows](https://github.com/HKUDS/OpenOPC/tree/9824f41f18d31801b97ce87f58c7151b5c080047/.github/workflows) |

<a id="ch-paperclip"></a>

### Paperclip

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/paperclipai/paperclip |
| License | MIT |
| Phiên bản đã đọc | `78b10a43ce751c2e16a15593f40cb134d9ca2c03` (commit 2026-11-23) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE, package.json, danh sách .github/workflows; chưa chạy upstream |
| Bảo trì | Hoạt động: commit 2026-11-23 (nhánh master); CI nhiều workflow |
| Nhận định | Server Node.js + UI React điều phối đội agent như một công ty (org chart, ngân sách, governance), nối nhiều harness/agent qua adapter. Tuyên bố 'tổ chức AI tự trị' là định vị marketing **(chưa xác minh)**. |
| Nguồn | [README](https://github.com/paperclipai/paperclip/blob/78b10a43ce751c2e16a15593f40cb134d9ca2c03/README.md) · [LICENSE](https://github.com/paperclipai/paperclip/blob/78b10a43ce751c2e16a15593f40cb134d9ca2c03/LICENSE) · [package.json](https://github.com/paperclipai/paperclip/blob/78b10a43ce751c2e16a15593f40cb134d9ca2c03/package.json) · [workflows](https://github.com/paperclipai/paperclip/tree/78b10a43ce751c2e16a15593f40cb134d9ca2c03/.github/workflows) |

<a id="ch-ruflo-claude-flow"></a>

### ruflo (claude-flow)

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/ruvnet/ruflo |
| License | MIT |
| Phiên bản đã đọc | `326687da9b6a442303818249bbd80444a1414cca` (commit 2026-11-22) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE, package.json, Cargo.toml, danh sách .github/workflows; chưa chạy upstream |
| Bảo trì | Hoạt động: commit 2026-11-22; package.json `claude-flow` 3.80.1 |
| Nhận định | Nay tự gọi là 'agent meta-harness cho Claude Code và Codex': `npx ruflo init` cài agent, hook, memory, MCP server và daemon vào dự án (98 agent, 60+ lệnh theo README). Bề mặt cài đặt lớn; tuyên bố hiệu năng vẫn **(chưa xác minh)**. |
| Nguồn | [README](https://github.com/ruvnet/ruflo/blob/326687da9b6a442303818249bbd80444a1414cca/README.md) · [LICENSE](https://github.com/ruvnet/ruflo/blob/326687da9b6a442303818249bbd80444a1414cca/LICENSE) · [package.json](https://github.com/ruvnet/ruflo/blob/326687da9b6a442303818249bbd80444a1414cca/package.json) · [Cargo.toml](https://github.com/ruvnet/ruflo/blob/326687da9b6a442303818249bbd80444a1414cca/Cargo.toml) · [workflows](https://github.com/ruvnet/ruflo/tree/326687da9b6a442303818249bbd80444a1414cca/.github/workflows) |

<a id="ch-semantic-kernel"></a>

### Semantic Kernel

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/microsoft/semantic-kernel |
| License | MIT |
| Phiên bản đã đọc | `aa46eddff989c13fba70c15e0ae8715b75f3fe8d` (commit 2026-11-20) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE, danh sách .github/workflows; chưa chạy upstream |
| Bảo trì | README ghi Semantic Kernel nay là Microsoft Agent Framework (kế nhiệm, MAF 1.0); repo vẫn có commit 2026-11-20 |
| Nhận định | SDK agent đa ngôn ngữ (.NET/Python/Java) của Microsoft. README đặt khung IMPORTANT chỉ sang Microsoft Agent Framework làm kế nhiệm và có hướng dẫn migration; dự án mới nên xem MAF. |
| Nguồn | [README](https://github.com/microsoft/semantic-kernel/blob/aa46eddff989c13fba70c15e0ae8715b75f3fe8d/README.md) · [LICENSE](https://github.com/microsoft/semantic-kernel/blob/aa46eddff989c13fba70c15e0ae8715b75f3fe8d/LICENSE) · [workflows](https://github.com/microsoft/semantic-kernel/tree/aa46eddff989c13fba70c15e0ae8715b75f3fe8d/.github/workflows) |

<a id="ch-smolagents"></a>

### smolagents

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/huggingface/smolagents |
| License | Apache-2.0 |
| Phiên bản đã đọc | `5107d3aec21d26ed808aabd95d93a63d4244226f` (commit 2026-11-23) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE, pyproject.toml, danh sách .github/workflows; chưa chạy upstream |
| Bảo trì | Hoạt động: commit 2026-11-23; pyproject 1.27.0.dev0 |
| Nhận định | Thư viện agent tối giản của Hugging Face, trọng tâm CodeAgent viết hành động bằng code, chạy sandbox qua Blaxel/E2B/Modal/Docker. Tuyên bố logic ~1.000 dòng là của tác giả **(chưa xác minh)**. |
| Nguồn | [README](https://github.com/huggingface/smolagents/blob/5107d3aec21d26ed808aabd95d93a63d4244226f/README.md) · [LICENSE](https://github.com/huggingface/smolagents/blob/5107d3aec21d26ed808aabd95d93a63d4244226f/LICENSE) · [pyproject.toml](https://github.com/huggingface/smolagents/blob/5107d3aec21d26ed808aabd95d93a63d4244226f/pyproject.toml) · [workflows](https://github.com/huggingface/smolagents/tree/5107d3aec21d26ed808aabd95d93a63d4244226f/.github/workflows) |

<a id="ch-strands-agents-harness-sdk"></a>

### Strands Agents harness-sdk

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/strands-agents/harness-sdk |
| License | Apache-2.0 (file LICENSE.APACHE ở gốc) |
| Phiên bản đã đọc | `d8e5c03c51526fece0d1cb5158c23c2413d77624` (commit 2026-11-23) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE.APACHE, package.json, pyproject.toml, danh sách .github/workflows; chưa chạy upstream |
| Bảo trì | Hoạt động: commit 2026-11-23; CI nhiều workflow cho từng gói |
| Nhận định | Monorepo SDK Strands (Python/TypeScript) + harness, CLI và MCP server; chạy trong tiến trình, không control plane hosted. Mặc định Bedrock và cấu hình OTel theo hồ sơ cũ chưa đọc lại ở lượt này. |
| Nguồn | [README](https://github.com/strands-agents/harness-sdk/blob/d8e5c03c51526fece0d1cb5158c23c2413d77624/README.md) · [LICENSE.APACHE](https://github.com/strands-agents/harness-sdk/blob/d8e5c03c51526fece0d1cb5158c23c2413d77624/LICENSE.APACHE) · [package.json](https://github.com/strands-agents/harness-sdk/blob/d8e5c03c51526fece0d1cb5158c23c2413d77624/package.json) · [pyproject.toml](https://github.com/strands-agents/harness-sdk/blob/d8e5c03c51526fece0d1cb5158c23c2413d77624/pyproject.toml) · [workflows](https://github.com/strands-agents/harness-sdk/tree/d8e5c03c51526fece0d1cb5158c23c2413d77624/.github/workflows) |

<a id="ch-voltagent"></a>

### VoltAgent

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/VoltAgent/voltagent |
| License | MIT |
| Phiên bản đã đọc | `e9fc599f6059afcd88b34f2bfc50d0d1d6a0877c` (commit 2026-11-06) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENCE, package.json, danh sách .github/workflows; chưa chạy upstream |
| Bảo trì | Hoạt động: commit 2026-11-06 |
| Nhận định | Framework agent TypeScript mã nguồn mở (memory, RAG, guardrail, tool, MCP, workflow, supervisor/sub-agent) đi kèm VoltOps Console (cloud/self-host) cho observability. Phần console là sản phẩm riêng; ranh giới license của nó chưa kiểm. |
| Nguồn | [README](https://github.com/VoltAgent/voltagent/blob/e9fc599f6059afcd88b34f2bfc50d0d1d6a0877c/README.md) · [LICENCE](https://github.com/VoltAgent/voltagent/blob/e9fc599f6059afcd88b34f2bfc50d0d1d6a0877c/LICENCE) · [package.json](https://github.com/VoltAgent/voltagent/blob/e9fc599f6059afcd88b34f2bfc50d0d1d6a0877c/package.json) · [workflows](https://github.com/VoltAgent/voltagent/tree/e9fc599f6059afcd88b34f2bfc50d0d1d6a0877c/.github/workflows) |

### Microsoft Agent Framework — tài liệu chính thức 23/11/2026

Theo [Microsoft Learn](https://learn.microsoft.com/en-us/agent-framework/overview/), Agent Framework kế thừa AutoGen và Semantic Kernel, bổ sung workflow điều phối. Chỉ đọc tài liệu sản phẩm; chưa truy cập được repo tại commit xác định, chưa kiểm license hoặc mã, chưa nâng mức xác minh của repo.
