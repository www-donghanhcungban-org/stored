# 04 · Protocols & Standards cho hệ sinh thái Agent

> Các giao thức/định dạng mở giúp agent nói chuyện với tool, với agent khác, với UI và với hướng dẫn của dự án.

## 1. Bản đồ giao thức

| Lớp | Giao thức | Chủ quản | Mốc | Vai trò |
|---|---|---|---|---|
| Agent ↔ Tool/Data | **MCP** (Model Context Protocol) | Anthropic → Agentic AI Foundation (AAIF, Linux Foundation, 12/2025) | 11/2024 ra mắt; >10k server production (2026) | Chuẩn kết nối tool, resource, prompt |
| Agent ↔ Agent | **A2A** (Agent2Agent) | Google → Linux Foundation (6/2025) | v1.0 3/2026, v1.0.1 5/2026; >150 tổ chức (4/2026) | Task state, long-running, agent card; có nguồn nói chuyển vào AAIF 20/8/2026 **(chưa xác minh)** |
| Agent ↔ UI | **AG-UI** (Agent-User Interaction) | CopilotKit | 2025–2026; AWS AgentCore, MS Agent Framework, Oracle Agent Spec/A2UI tích hợp | Stream sự kiện agent → frontend, generative UI |
| Agent ↔ Kỹ năng | **Agent Skills / SKILL.md** | Anthropic → chuẩn mở agentskills.io (18/12/2025) | Ra mắt 16/10/2025; OpenAI, Microsoft hỗ trợ trong ~48h; ~40 sản phẩm (Copilot, VS Code, Gemini CLI, Cursor 2.4) | Gói hướng dẫn + script tải theo nhu cầu |
| Agent ↔ Dự án | **AGENTS.md** | OpenAI → Agentic AI Foundation (Linux Foundation), repo `agentsmd/agents.md` | 2025; hơn 60k dự án (12/10/2026) | File hướng dẫn chung cho nhiều tool |
| Editor ↔ Coding agent | **ACP** (Agent Client Protocol) | Zed → `agentclientprotocol/` | Schema v1.25.0 (9/10/2026) | Một giao thức để editor (Zed, JetBrains, Neovim, Emacs) gọi coding agent bất kỳ |
| (legacy) | `.cursorrules` → `.cursor/rules/*.mdc` | Cursor | – | Đã lỗi thời; chuyển sang skills/AGENTS.md |

## 2. MCP chi tiết

- **Repo chính:** `modelcontextprotocol/servers` (~91,2k★, 12/10/2026) – 7 reference server: Everything, Fetch, Filesystem, Git, Memory, Sequential Thinking, Time; README nay ghi "not production-ready", bỏ mục Official Integrations và trỏ sang MCP Registry.
- **SDK/framework:** `prefecthq/fastmcp` (~23k★, Python), SDK chính thức TS/Python/Java/C#/Kotlin.
- **Server phổ biến nhất (theo nhiều roundup):** GitHub, Context7 (docs), Playwright (browser), Filesystem/Fetch, Tavily (search).
- **Danh sách:** `punkpeye/awesome-mcp-servers` (96,2k★), `VoltAgent/official-mcp-servers` (chỉ server chính chủ, xem §2c), `wong2/awesome-mcp-servers` (ngừng nhận PR), `sadekxD/Awesome-MCP`.
- **Rủi ro:** prompt injection qua tool output, quyền truy cập quá rộng → cần allowlist và sandbox.
- **Đóng gói & tính năng ít dùng (từ repo của chủ kho, mục 23):** `.mcpb` — manifest đóng gói MCP server một-click cho Claude Desktop (Dhcb-Tools `tools/mcpb/manifest.json`); **MCP prompts + completion** và WebMCP declarations (`@modelcontextprotocol/server` 2.0.0-beta, REA `docs/mcp-prompts.md`); MCP Streamable HTTP với `Mcp-Session-Id` (ai-gateway). Mẫu thiết kế: "MCP tool là agent-computer interface" — ít tool, tên tham số tra được (`parameters_of`), không đoán; cho model local chỉ lộ ≤8 tool (`--group`).

## 2b. Repo chính thức & SDK đã xác minh (2026-10-12)

| Repo | ★ (12/10) | License | Phát hành / hoạt động gần nhất | Vai trò & điểm chất lượng | Lưu ý |
|---|---|---|---|---|---|
| **modelcontextprotocol/python-sdk** | 24,6k | MIT | v2.3.0 (2/10/2026), commit 12/10 | SDK Python chính thức cho MCP server/client: stdio, Streamable HTTP, SSE; có hướng dẫn chuyển lên v2 | v2 có thay đổi phá vỡ; bỏ Python 3.10 từ 12/10/2026 |
| **modelcontextprotocol/typescript-sdk** | 13,6k | Apache-2.0 (code mới) / MIT (code cũ) | 2.3.1 (5/10/2026) | Hiện thực spec 2026-07-28; tách gói server/client, middleware Express/Fastify/Hono | v2 tách gói; v1.x chỉ còn sửa lỗi và bảo mật |
| **modelcontextprotocol/inspector** | 11,1k | đang chuyển MIT → Apache-2.0 | 2.10.1 (8/10/2026) | Công cụ test MCP server dạng UI và CLI (dùng được trong CI và vòng phản hồi của agent); secret lưu vào keychain hệ điều hành | Không có keychain thì `secrets.json` không mã hoá; v1 chỉ còn vá bảo mật |
| **modelcontextprotocol/registry** | 7,3k | Apache-2.0 (một phần đang chuyển MIT/CC-BY-4.0) | tag v1.8.1 (6/8/2026) | Registry chính thức của cộng đồng cho MCP server, do MCP Registry WG (Stacklok, PulseMCP…) vận hành; API đóng băng ở v0.1 từ 10/2025 | README vẫn ghi "preview", dữ liệu có thể bị reset; chưa GA |
| **modelcontextprotocol/ext-apps** | 2,9k | Apache-2.0 | 2.0.3, commit 25/9/2026 | Extension chính thức **MCP Apps**: spec + SDK nhúng UI vào host (ChatGPT, Claude, VS Code, Goose, Postman); spec 2026-01-26 ổn định | Mức hỗ trợ khác nhau giữa các host; thay thế `MCP-UI-Org/mcp-ui` (5,2k★) |
| **agentclientprotocol/agent-client-protocol** (ACP của Zed) | 4,4k | Apache-2.0 | Schema v1.25.0 (9/10/2026) | Giao thức nối editor bất kỳ với coding agent bất kỳ; client: Zed, JetBrains, Neovim, Emacs, extension VS Code; SDK 5 ngôn ngữ | Trùng tên với ACP của IBM (đã archive); schema v2 còn alpha |
| **agentsmd/agents.md** | 24,9k | MIT | commit 10/9/2026 | Định dạng mở AGENTS.md, hơn 60k dự án dùng; do Agentic AI Foundation (Linux Foundation) quản; Codex, Cursor, Copilot hỗ trợ | Là quy ước, không phải schema; repo chủ yếu là website (38 commit) |

**Nhận xét:**

- **Hai giao thức "ACP" khác nhau:** Agent **Client** Protocol (Zed, nay ở `agentclientprotocol/`, nối editor với coding agent, đang hoạt động; Jupyter AI ở mục 15 dùng giao thức này) và Agent **Communication** Protocol (IBM, `i-am-bee/acp`, **archive 27/8/2025, đã nhập vào A2A**). Bảng §1 và §3 đã sửa theo.
- MCP TypeScript SDK v2 đã nhắm spec 2026-07-28; REA đang dùng `@modelcontextprotocol/server` 2.0.0-beta (§2) nên cân nhắc lên 2.3.x ổn định.
- AGNTCY ("Internet of Agents", Linux Foundation) không có repo chủ lực, mọi repo dưới 400★ — chưa đáng theo dõi.

## 2c. Danh mục MCP server "chính thức": VoltAgent/official-mcp-servers (ảnh người dùng gửi, 2026-10-12)

| Mục | Thông tin (12/10/2026) |
|---|---|
| Repo | `VoltAgent/official-mcp-servers` · 302★, 45 fork, MIT, tạo 1/10/2026, 26 commit |
| Lời hứa | "A curated directory of 280+ official MCP servers from the companies behind the products. No unofficial forks, no abandoned projects." |
| Thực tế | README có **297 mục** trong 14 nhóm (badge "286" là số gõ tay; badge "Last update today" chỉ là ngày commit cuối, không nói gì về các server); 202 mục là repo GitHub, 95 mục chỉ trỏ tới docs hoặc endpoint hosted |
| Cơ chế kiểm | **Không có kiểm tra tự động** (repo không có `.github/`); README tự ghi "curated, not audited"; CONTRIBUTING nhận cả "a widely used open source project", nên "official" không tuyệt đối |
| Chủ list | VoltAgent (framework agent TypeScript, `VoltAgent/voltagent` 10,8k★); list có cả MCP server của chính họ. Cùng chủ: awesome-design-md (120k★), awesome-agent-skills (36k★), awesome-claude-code-subagents (26k★) |

**Kiểm 201 repo GitHub trong list** (metadata ecosyste.ms, trạng thái archive xác nhận trực tiếp trên GitHub):

- **11 repo đã archive (5,5%)**: `PostHog/mcp`, `semgrep/mcp`, `browserbase/mcp-server-browserbase`, `elevenlabs/elevenlabs-mcp`, `tinybirdco/mcp-tinybird`, `e2b-dev/mcp-server`, `axiomhq/mcp-server-axiom`, oxylabs-mcp, `box-community/mcp-server-box`, `chargebee/agentkit`, `incident-io/incidentio-mcp-golang` — phần lớn vì hãng đã chuyển sang **server hosted (remote MCP)** hoặc gộp vào monorepo.
- **Khoảng 21 repo không push hơn 6 tháng** (15 repo chắc chắn, 6 repo **chưa xác minh**), ví dụ `langfuse/mcp-server-langfuse` (2/2025), `JetBrains/mcp-jetbrains` (README ghi "Deprecated… no longer maintained").
- **Không chính chủ hoặc trái luật của list:** `ahujasid/blender-mcp` (nay chuyển hướng sang `ahujasid/mcp-for-blender`) tự ghi "third-party… not made by Blender"; `google/mcp` tự ghi "not an officially supported Google product"; 4 repo gần như 0★ (Invompt, Desearch, bestax, BulkPublish) được merge ngay tuần đầu dù luật cấm "brand new projects".

**Bối cảnh các danh mục khác:** `punkpeye/awesome-mcp-servers` 96,2k★ (~4.200 dòng, không lọc chính chủ); `modelcontextprotocol/servers` 91,2k★ — README **đã bỏ mục "Official Integrations"**, chỉ còn 7 reference server ghi "not production-ready" và trỏ sang MCP Registry (§2b); `wong2/awesome-mcp-servers` 4,4k★ ngừng nhận PR (chuyển sang mcpservers.org); Glama ghi 97.619 server, Smithery 26.257+ server. List của VoltAgent lấp đúng khoảng trống "server chính chủ" mà repo chính thức đã bỏ.

**Cách dùng:** coi là điểm khởi đầu tìm server của chính hãng, nhưng trước khi cài vẫn tự kiểm 3 điều: (1) repo không archive và còn commit; (2) owner đúng là hãng; (3) hãng đã có bản hosted (remote MCP) thay cho repo local chưa — xu hướng 2026 là server local bị archive để chuyển sang endpoint hosted. Tra metadata ở MCP Registry chính thức khi có.

## 3. MCP vs A2A

| | MCP | A2A |
|---|---|---|
| Kết nối | Agent ↔ tool/data | Agent ↔ agent |
| Trạng thái | Phần lớn stateless | Task state tường minh, long-running |
| Khi dùng | Hầu hết ứng dụng, bắt đầu từ đây | Multi-agent vượt ranh giới tổ chức |
| Bổ sung | ACP (IBM) — đã archive 27/8/2025 và nhập vào A2A; ANP | |

## 4. SKILL.md vs AGENTS.md vs CLAUDE.md vs .cursorrules

- **SKILL.md**: YAML frontmatter (name, description) + hướng dẫn + file đính kèm; nạp "progressive disclosure" khi tác vụ khớp. Đặt tại `.claude/skills/`, `.agents/skills/`, `.cursor/skills/`, `.codex/skills/`.
- **AGENTS.md**: hướng dẫn luôn-nạp cho toàn repo, trung lập tool. Khuyến nghị cho team đa tool; skills là lớp bổ sung "gọi được".
- **CLAUDE.md**: tương đương AGENTS.md trong Claude Code (hỗ trợ import, phân cấp thư mục).
- **.cursorrules**: legacy; chuyển đổi = thêm frontmatter + đưa vào thư mục skills/rules.
- **Bộ file cho đa harness** (quan sát trong 19 repo của chủ kho, 2026-10-12): `CLAUDE.md` dùng `@import` để trỏ về AGENTS.md; bridge mỏng `GEMINI.md`, `.clinerules`, `.windsurfrules`, `.cursor/rules/*.mdc`, `.github/copilot-instructions.md` chỉ chứa một dòng "đọc AGENTS.md"; **Antigravity** dùng `.agents/rules/*.md`, `.agents/workflows/*.md`, `.agents/mcp_config.json` và `.agents/skills/`; Hermes Agent đọc SKILL.md có `metadata.hermes`; Codex đọc `AGENTS.md` + `.codex/skills/`. Bẫy thật: `next dev` ghi đè `AGENTS.md` (case-study-ft41) → giữ bản gốc trong `docs/` và kiểm bằng script.
- **Danh sách:** `VoltAgent/awesome-agent-skills` (1000+ skills), `spencerpauly/awesome-cursor-skills`, `PatrickJS/awesome-cursorrules`.

## 4b. Nâng cấp 31/10/2026: rà repo lớn

> Hai việc. (1) Đọc lại số sao, license, ngày push của mọi repo mục 04 trong catalog bằng GitHub search API (31/10/2026). (2) Tìm repo lớn còn thiếu: 8 truy vấn (topic `mcp`, `a2a`, `mcp-gateway`; từ khoá "model context protocol", "agent protocol", "agent skills specification", "a2ui"; repo tạo sau 1/10/2025). Lọc trùng với toàn catalog, chọn **6 repo** gần chủ đề "giao thức và chuẩn" nhất, clone `--filter=blob:none` đủ lịch sử, đọc LICENSE, manifest, cấu trúc, CI, file nguồn chính và grep telemetry. **Không cài, không chạy script nào.**

### 4b.1 Repo cũ: điều đã đổi

| Repo | Thay đổi (12/10 → 31/10/2026) | Hệ quả |
|---|---|---|
| **Spec MCP** (bản `2026-07-28`) | Changelog chính thức: **bỏ `Mcp-Session-Id` và phiên ở tầng giao thức**, bỏ bắt tay `initialize`, thêm `server/discover`, mỗi request mang version và capability trong `_meta`; bỏ `ping`, `logging/setLevel`; tasks chuyển thành extension | Dòng "MCP Streamable HTTP với `Mcp-Session-Id` (ai-gateway)" ở §2 đã lỗi thời theo spec mới; server/gateway tự viết cần lộ trình sang stateless. Chi tiết ở 4b.3 |
| `prefecthq/fastmcp` | ~23k → **28,3k** (+23%) | Tăng nhanh nhất mục; vẫn là framework Python phổ biến nhất |
| `a2aproject/A2A` | Bảng §1 chưa có số → **26,4k**, push 30/10 | Catalog bổ sung số sao |
| `ag-ui-protocol/ag-ui` | **16,9k**, push 30/10 | Lần đầu ghi số trong README |
| `modelcontextprotocol/servers` | 91,2k → 91,7k; GitHub báo `NOASSERTION` | Không phải đổi license: cả tổ chức đang chuyển MIT → Apache-2.0 (code) và CC-BY-4.0 (docs), file LICENSE là văn bản chuyển tiếp nên GitHub không nhận dạng được. Tương tự `typescript-sdk`, `inspector`, `registry`, `ext-apps` |
| `agentsmd/agents.md` | 24,9k → 25,2k; **commit cuối vẫn 10/9/2026** | Bảy tuần không commit; là quy ước ổn định nên chưa đáng lo, nhưng đừng chờ thay đổi từ repo này |
| `VoltAgent/official-mcp-servers` | 302 → **405** (+34%) | §2c vẫn đúng về cơ chế |
| `VoltAgent/awesome-agent-skills` · `punkpeye/awesome-mcp-servers` | Chưa có số → **36,7k** · 96,2k → 97,1k | Catalog bổ sung số sao |
| SDK, inspector, registry, ACP | Dao động dưới 3% | Không đổi nhận định |

### 4b.2 Bảng nhanh 6 repo mới

| Repo | Nhóm | ★ · license | Commit cuối | Một dòng | Cờ |
|---|---|---|---|---|---|
| `modelcontextprotocol/modelcontextprotocol` | Spec MCP | 9,6k · đang chuyển MIT → Apache-2.0 (`NOASSERTION`) | 31/10/2026 | Nguồn gốc spec + schema TS/JSON, 6 bản (2024-11-05 → 2026-07-28 + draft), 48 SEP | README vẫn ghi MIT |
| `agentskills/agentskills` | Spec Agent Skills | 26,8k · Apache-2.0 (docs CC-BY-4.0) | 9/8/2026 | Spec SKILL.md + thư viện kiểm `skills-ref` | Không CI; 12 tuần đứng yên |
| `a2ui-project/a2ui` | Chuẩn Agent → UI | 16,9k · Apache-2.0 | 30/10/2026 | JSON khai báo UI, renderer Lit/Angular/Flutter/Swift/Kotlin, bộ conformance | Vẫn "public preview"; trước là `google/A2UI` |
| `github/github-mcp-server` | MCP server chính chủ | 34,1k · MIT | 28/10/2026 | Server GitHub chính thức (Go), bản hosted `api.githubcopilot.com/mcp/` | Ghi được vào repo nếu không bật `--read-only` |
| `mcp-use/mcp-use` | Framework MCP | 10,8k · MIT | 30/10/2026 | SDK Python/TS dựng MCP server, MCP Apps, agent client | **Telemetry gửi cả câu hỏi và câu trả lời** |
| `agentgateway/agentgateway` | Gateway MCP/A2A | 5,8k · Apache-2.0 | 30/10/2026 | Proxy Rust cho MCP, A2A, LLM; dự án LF Projects do Solo.io dẫn | Hạ tầng nặng (Kubernetes, CEL) |

### 4b.3 Hồ sơ từng repo

- **`modelcontextprotocol/modelcontextprotocol` (spec).** 4.932 commit từ 24/9/2024, 472 tác giả, 977 commit từ 1/5/2026; 6,2% commit có trailer Claude. Schema viết TypeScript trước (`schema/2026-07-28/schema.ts`, 3.197 dòng) rồi xuất JSON Schema. Có quy trình SEP thật: 48 file trong `seps/`, workflow `sep-lifecycle.yml`, `sep-reminder.yml`. `AI_POLICY.md` **bắt buộc khai báo** mọi trợ giúp AI trong PR/issue. Bản `2026-07-28` là đổi lớn nhất từ khi ra mắt: stateless, `subscriptions/listen` thay GET/SSE, mẫu **MRTR** (`input_required`) thay request từ server (sampling, elicitation), mọi kết quả list có `ttlMs`/`cacheScope`, `tools/list` nên trả theo thứ tự cố định để tăng cache hit, client **MUST** kiểm `iss` (RFC 9207). Mâu thuẫn: README ghi "licensed under the MIT License" ❌, LICENSE ghi đang chuyển sang Apache-2.0. Không phải phần mềm để cài; đọc tại modelcontextprotocol.io/specification.
- **`agentskills/agentskills`.** 145 commit, 44 tác giả, Jonathan Hefner (Anthropic) 91 commit; 39% commit có trailer Claude. Gồm spec (`docs/specification.mdx`), hướng dẫn viết và **eval skill** (`evaluating-skills.mdx`, `optimizing-descriptions.mdx`), và `skills-ref` (Python): `validator.py` kiểm đúng các giới hạn spec ghi (name ≤ 64 ký tự, chữ thường, không `--`, khớp tên thư mục; description ≤ 1024; compatibility ≤ 500; chỉ 6 trường frontmatter) ✅. Lệch nhỏ: validator nhận chữ Unicode (i18n), spec ghi "lowercase letters, numbers, and hyphens" ⚠️. README `skills-ref` tự ghi "demonstration purposes only". Repo không có `.github/`, tức **không CI**; test có nhưng không ai chạy tự động. Commit cuối 9/8/2026 chỉ thêm OpenClaw, Hermes Agent vào danh sách client. Kiểm skill: `uvx --from git+https://github.com/agentskills/agentskills#subdirectory=skills-ref skills-ref validate <thư-mục>` **(lệnh suy từ pyproject, chưa chạy)**.
- **`a2ui-project/a2ui`.** 1.696 commit từ 26/9/2025, 110 tác giả, 706 commit từ email `google.com`; không commit nào có trailer Claude (repo dùng `.gemini/`). Spec có 4 bản `v0_8`, `v0_9`, `v0_9_1`, `v1_0` (RC); README ghi bản production là 0.9.1 và "Early stage public preview". Lời "agent chỉ được yêu cầu component có trong catalog tin cậy" có cơ chế thật: `conformance/core/catalog.yaml` và `validator_v*.yaml` định nghĩa bộ test chung cho mọi SDK ✅. Điểm cần canh: **catalog MCP** (`catalogs/mcp/`) cho phép payload UI gọi `callMcpTool` theo tên tool, và component `McpApp` nhúng MCP App vào surface — tức UI do agent sinh có thể kích hoạt tool; host phải tự lọc tool nào được gọi. 19 workflow CI (conformance, eval, kiểm spec). Liên quan AG-UI §1 và mục 06 §7p.6.
- **`github/github-mcp-server`.** 1.200 commit, 194 tác giả, Go; bản v2.0.3 (21/10/2026). Kiểm soát quyền làm tốt: `--toolsets`, `--tools`, `--exclude-tools`, `--read-only` (ưu tiên hơn `--tools`) ✅; **lockdown mode** chỉ trả nội dung public do người có quyền push viết, README tự nói rõ là "best-effort content filter… not an authorization boundary" và miễn trừ `github-actions[bot]`, `copilot`. Chế độ HTTP: `--listen-host` để trống thì **nghe trên mọi interface**; header `X-MCP-Lockdown` chỉ bật thêm được, không tắt được lockdown do người vận hành đặt. Không thấy telemetry trong mã. Cài: `claude mcp add github -e GITHUB_PERSONAL_ACCESS_TOKEN=$GITHUB_PAT -- docker run -i --rm -e GITHUB_PERSONAL_ACCESS_TOKEN ghcr.io/github/github-mcp-server` (thêm `-e GITHUB_READ_ONLY=1` hoặc cờ `--read-only` cho agent không cần ghi).
- **`mcp-use/mcp-use`.** 1.693 commit, 68 tác giả; SDK Python và TypeScript (client, agent, server, inspector, MCP Apps). **Telemetry bật mặc định, gửi tới PostHog EU (`eu.i.posthog.com`, key viết cứng) và Scarf.** `telemetry/events.py` và `telemetry.py` cho thấy sự kiện `mcp_agent_execution` mang **nguyên văn `query` và `response`** của agent, cùng tên tool, model; docs tự ghi "Query and response content" nhưng vẫn gọi là "anonymized" ❌. Tắt bằng `MCP_USE_ANONYMIZED_TELEMETRY=false` (Python không đọc `DO_NOT_TRACK`). Ngoài telemetry, repo hoạt động tốt (CI conformance, e2e inspector, eval SDK). Cài: `pip install mcp-use` hoặc `npm install --save-dev @mcp-use/client`, nhớ đặt biến tắt telemetry trước.
- **`agentgateway/agentgateway`.** 3.180 commit từ 18/3/2025, 307 tác giả, 2.022 commit từ email `solo.io`; `CHARTER.md` xác nhận là "a Series of LF Projects". Rust (15 crate) + controller Go cho Kubernetes Gateway API; proxy MCP, A2A và LLM với RBAC qua CEL, JWT/OAuth, rate limit, guardrail, OpenTelemetry. File `analytics.go` chỉ là lệnh xem log request cục bộ (token, chi phí, TTFT), không gửi ra ngoài ✅. Lời "the first complete connectivity solution" không kiểm được. Bản v1.7.0 (27/10/2026); quickstart chỉ có trên agentgateway.dev **(chưa đọc)**. Chưa kiểm hỗ trợ spec MCP 2026-07-28.

### 4b.4 Mẫu chung rút ra

1. **Chuẩn đã có "cổng máy" đi kèm:** MCP có schema JSON + SEP lifecycle, Agent Skills có `skills-ref validate`, A2UI có bộ conformance YAML dùng chung cho mọi SDK. Dự án dùng chuẩn nên chạy validator chính thức trong CI thay vì tự viết.
2. **MCP đang bỏ trạng thái phiên.** Ai đã dựa vào `Mcp-Session-Id`, SSE resumable hay request từ server (sampling/elicitation) phải chuyển sang handle tường minh và MRTR.
3. **Lọc nội dung chống prompt injection không phải ranh giới quyền:** github-mcp-server nói thẳng điều này về lockdown mode; vẫn cần `--read-only` và token tối thiểu.
4. **Telemetry trong SDK giao thức là rủi ro dữ liệu thật:** mcp-use gửi nguyên văn hội thoại. Đặt biến tắt riêng của từng SDK, đừng chỉ dựa vào `DO_NOT_TRACK`.
5. **License đang chuyển tiếp làm GitHub báo `NOASSERTION`** (cả tổ chức modelcontextprotocol): đọc file LICENSE, đừng đọc nhãn.

**Nguồn §4b (31/10/2026):** GitHub search API (`repo:` cho repo cũ, 8 truy vấn topic/từ khoá) · clone `--filter=blob:none`: modelcontextprotocol/modelcontextprotocol (README.md, LICENSE, AI_POLICY.md, GOVERNANCE.md, `docs/specification/2026-07-28/changelog.mdx`, `schema/*`, `seps/`, `.github/workflows/`), agentskills/agentskills (README.md, `docs/specification.mdx`, `skills-ref/src/skills_ref/validator.py`, `skills-ref/README.md`, `.claude/hooks/session-start.sh`), a2ui-project/a2ui (README.md, `specification/`, `conformance/core/catalog.yaml`, `catalogs/mcp/README.md`, workflows), github/github-mcp-server (README.md mục Toolsets và Lockdown Mode, `cmd/github-mcp-server/main.go`, tag v2.0.3), mcp-use/mcp-use (`libraries/python/mcp_use/telemetry/{telemetry,events}.py`, `libraries/typescript/packages/client/src/telemetry/telemetry.ts`, `docs/python/development/telemetry.mdx`, `libraries/python/mcp_use/agents/mcpagent.py`), agentgateway/agentgateway (README.md, CHARTER.md, `crates/`, `controller/pkg/cli/standalone/analytics.go`) · https://modelcontextprotocol.io/specification · https://github.com/a2ui-project/a2ui · https://agentgateway.dev

## 4c. Nâng trần 2/11/2026: bộ conformance, inspector có eval, chuẩn đóng gói và scanner cho MCP/A2A (yêu cầu người dùng)

> Tìm repo **chưa có trong catalog** ở ba lớp: chuẩn, cổng máy, đầu bảng. GitHub search API 2/11/2026 (`repo:` cho từng repo, 6 truy vấn từ khoá). Clone `--depth 1 --filter=blob:none`, đọc LICENSE, README, manifest, CI, file chính. **Không cài, không chạy.**

**Trần hiện tại:**

- Mục đã có spec (§4b `modelcontextprotocol/modelcontextprotocol`, `agentskills/agentskills`, A2UI), SDK, inspector chính thức, registry (§2b) và một validator nhẹ (`skills-ref`, §4b.3). Tức là đủ để **viết** server, chưa đủ để **chứng minh** server/client đúng spec.
- Chưa có bộ test conformance nào cho MCP hay A2A, nên "hỗ trợ spec 2026-07-28" (§4b.3, agentgateway) vẫn là lời tự nhận.
- Chưa có lớp đóng gói chuẩn (`.mcpb` chỉ được nhắc qua repo của chủ kho, §2) và chưa có scanner bảo mật cho MCP trong mục này (scanner nằm ở mục 12).

| Repo | Lớp | ★ · license (2/11/2026) | Commit cuối | Vì sao nâng trần | Rủi ro |
|---|---|---|---|---|---|
| `modelcontextprotocol/conformance` | Cổng máy (chính thức) | 140 · MIT → Apache-2.0 đang chuyển (`NOASSERTION`; `package.json` vẫn ghi MIT) | HEAD `c37eec8` 1/10/2026 (nhánh khác push 2/11) | Bộ test chính thức cho **cả client và server**: 81 file scenario, kiểm từng message JSON-RPC trên dây với JSON Schema của spec (`wire-schema-valid`); `--requirements 2026-07-28` chạy đúng tập bắt buộc của một bản spec, đóng băng lúc phát hành; `tier-check` chấm SDK theo SEP-1730; có GitHub Action (`action.yml`) và file baseline lỗi đã biết | Bản `0.2.0-alpha.12`, ít sao; scenario tăng nhanh nên chỉ tin `--requirements`, không tin "chạy tất cả" |
| `a2aproject/a2a-tck` | Cổng máy (chính thức) | 57 · Apache-2.0 | 22/10/2026 | TCK cho A2A trên 3 transport (gRPC, JSON-RPC, HTTP+JSON); MUST là lỗi cứng, SHOULD là `xfail`; sinh SUT từ kịch bản Gherkin cho a2a-java/python/jakarta | Rất ít sao; README còn trỏ link spec cũ `google.github.io/A2A` |
| `a2aproject/a2a-inspector` | Cổng máy (thủ công) | 506 · Apache-2.0 | 29/10/2026 | Một binary Go có UI: kiểm agent card v1.0/v0.3 theo spec, ghi và validate từng request/response | Không phải test tự động cho CI; Docker mẫu đã bind `127.0.0.1` ✅ |
| `MCPJam/inspector` | Đầu bảng | 2,3k · Apache-2.0 **trừ phần eval** (`NOASSERTION`) | 2/11/2026 | Inspector + eval chéo 16 cấu hình client (ChatGPT, Claude, Cursor…), OAuth debugger, CLI chạy conformance/e2e/eval trong CI | `server/services` (và `server/routes/mcp/evals.ts` nếu có) dùng **MCPJam EE License** (văn bản giấy phép nằm ở `server/evals/LICENSE`): chạy production cần subscription, dev/test thì được. Telemetry PostHog/Axiom có chính sách "chặt nhất thắng", `DO_NOT_TRACK=1` (hoặc `true`) chỉ tắt telemetry phía server (analytics, báo lỗi Sentry, log Axiom); bản browser phát hành trên npm vẫn gửi usage event lên PostHog, muốn tắt phải build từ source với `VITE_DISABLE_POSTHOG_LOCAL=true` (app desktop dùng `MCPJAM_TELEMETRY_DISABLED=1`) |
| `modelcontextprotocol/mcpb` | Chuẩn đóng gói | 2,2k · MIT → Apache-2.0 đang chuyển | HEAD 22/4/2026 | Spec + JSON Schema manifest (v0.1 → v0.4) và CLI `mcpb init/validate/pack/sign/verify`; tên cũ DXT; Claude Code nhận `.mcpb` trong `mcpServers` của plugin (docs plugins-reference, mục 20 §3v) | Hơn 6 tháng không commit trên `main`; chữ ký tự ký chỉ cảnh báo, không chặn |
| `cisco-ai-defense/mcp-scanner` | Cổng máy (bảo mật) | 1,1k · Apache-2.0 | 28/10/2026 | Quét tool MCP bằng YARA (offline), LLM judge, API Cisco AI Defense; thêm "readiness" tĩnh (timeout, retry), quét gói PyPI/npm trong Docker; có CodeQL, plugin Claude Code | `--stdio-command` **khởi chạy server** để quét; analyzer API gửi mô tả tool lên Cisco; LLM analyzer cần key |

**Stack nâng trần** (lợi ích/công sức giảm dần):

1. Server MCP tự viết: thêm job CI `npx @modelcontextprotocol/conformance server --url … --requirements 2026-07-28 --expected-failures conformance-baseline.yml` (hoặc dùng `action.yml`). Đây là cổng duy nhất biến lộ trình stateless ở §4b.3 thành đo được.
2. Trước khi cài server ngoài (§2c): `mcp-scanner --analyzers yara` (không cần key, không gửi dữ liệu) trên server đã sandbox; kết hợp checklist 3 điểm của §2c và OWASP MCP Top 10 (mục 12).
3. Kiểm tay bằng inspector chính thức (§2b); khi cần đo tool trên nhiều client thì dùng MCPJam, nhưng giữ phần eval trong phạm vi dev/test vì license EE.
4. Phát hành server local: đóng gói `.mcpb` và chạy `mcpb validate` trong CI; ký bằng chứng chỉ thật, đừng dừng ở `--self-signed`.
5. Agent A2A: `a2a-tck` mức MUST trong CI, `a2a-inspector` để soi agent card.
6. Skill: tiếp tục `skills-ref validate` (§4b.3); lint và eval skill chi tiết hơn xem mục 20 §3v.

**Nguồn §4c:** GitHub search API 2/11/2026 (`repo:` từng repo; truy vấn "mcp conformance", "skill validator agent skills", "claude plugin validate") · clone `--depth 1 --filter=blob:none` 2/11/2026: modelcontextprotocol/conformance (LICENSE, README.md, SDK_INTEGRATION.md, package.json, action.yml, `requirements/`, `src/scenarios/`), MCPJam/inspector (LICENSE, `mcpjam-inspector/server/evals/LICENSE`, README.md, `mcpjam-inspector/shared/telemetry-privacy.ts`, `server/utils/__tests__/analytics.test.ts`, workflows), modelcontextprotocol/mcpb (LICENSE, README.md, CLI.md, `schemas/`, package.json), cisco-ai-defense/mcp-scanner (LICENSE, README.md, workflows, `claude-code-plugin/`), a2aproject/a2a-tck (LICENSE, README.md), a2aproject/a2a-inspector (README.md) · https://github.com/modelcontextprotocol/conformance · https://github.com/a2aproject/a2a-tck · https://github.com/a2aproject/a2a-inspector · https://github.com/MCPJam/inspector · https://github.com/modelcontextprotocol/mcpb · https://github.com/cisco-ai-defense/mcp-scanner

<a id="core-protocol-boundaries"></a>

## 4d. Nâng trần 2/11/2026: phiên bản wire và ranh giới uỷ quyền MCP (mở rộng cùng ngày)

> Mở rộng chiều sâu trong cùng đợt 2/11/2026, không phải công bố các repo vừa ra mắt. Hai repo dưới đã có trong catalog: đọc lại LICENSE, CI và nhánh mặc định bằng clone chỉ đọc; SHA đối chiếu GitHub API. Mức bằng chứng **code-read**; không chạy/build repo ngoài, hiệu năng và hành vi thực tế **(chưa xác minh)**. Số sao/trạng thái đọc 2026-11-02; ngày commit tính theo UTC, tách khỏi `pushed_at`.

| Repo đã có | ★ · license (2026-11-02) | HEAD nhánh mặc định | Vai trò đọc sâu |
|---|---|---|---|
| `modelcontextprotocol/python-sdk` | 24.736 · MIT | 2026-10-27 · `d7845c07` | Conformance/version baseline và bảo vệ transport |
| `agentgateway/agentgateway` | 5.872 · Apache-2.0 | 2026-10-30 · `084992d6` | JWT/CEL theo tool. prompt. resource và đường gọi |

**Trần còn thiếu:** §4c đã có bộ conformance/scanner. Cần tách **đúng giao thức**, **xác thực danh tính** và **được quyền thao tác tài nguyên**: một server pass JSON-RPC/schema vẫn có thể cho người dùng đọc dữ liệu tenant khác.

### MCP Python SDK: ghim spec, harness và baseline cùng nhau

- [CI conformance](https://github.com/modelcontextprotocol/python-sdk/blob/d7845c073a2b9ba5ab2817ecf93d3e45ef24cd14/.github/workflows/conformance.yml) ghim `@modelcontextprotocol/conformance@0.2.0-alpha.11`, chạy wire `2025-11-25`, `2026-07-28` và mặc định; có baseline riêng cho từng wire. Bản baseline 2026-07-28 tại SHA này có `client: []`, `server: []`. Đây là **đọc cấu hình**, chưa xác minh artifact/kết quả CI; khi so SDK phải ghi đúng bộ requirements và baseline, không chỉ badge xanh.
- [`MCPServer`](https://github.com/modelcontextprotocol/python-sdk/blob/d7845c073a2b9ba5ab2817ecf93d3e45ef24cd14/src/mcp/server/mcpserver/server.py#L1162) tự bật DNS-rebinding protection cho localhost trong đường SSE được đọc; [`TransportSecurityMiddleware`](https://github.com/modelcontextprotocol/python-sdk/blob/d7845c073a2b9ba5ab2817ecf93d3e45ef24cd14/src/mcp/server/transport_security.py#L48) khi không nhận settings lại dùng protection tắt. Không suy từ giá trị mặc định của model settings ra mọi entrypoint; reverse proxy/host khác phải cấu hình Host/Origin allowlist rõ và thử request giả.
- Auth đòi token verifier khi bật; [bearer middleware](https://github.com/modelcontextprotocol/python-sdk/blob/d7845c073a2b9ba5ab2817ecf93d3e45ef24cd14/src/mcp/server/auth/middleware/bearer_auth.py) và auth settings là phần phải kiểm với issuer/resource URL thực tế. MCP authorization spec cấm kiểu nhận token sai audience rồi chuyển thẳng xuống API. Credential cho upstream là một ranh giới riêng.

### agentgateway: có engine policy chưa có nghĩa đã có policy

- [`McpAuthorizationSet::validate`](https://github.com/agentgateway/agentgateway/blob/084992d6091d671cf845e9cd40b16fed41c1511d/crates/agentgateway/src/mcp/rbac.rs#L54) trả `true` nếu **không có rule**. Vì vậy cài gateway rồi cấu hình JWT chưa tự giới hạn từng tool. Phải thêm policy cho tool/prompt/resource và kiểm người dùng không được phép cả khi list và khi gọi trực tiếp tên đã biết.
- [JWT config](https://github.com/agentgateway/agentgateway/blob/084992d6091d671cf845e9cd40b16fed41c1511d/crates/agentgateway/src/http/jwt.rs#L166) yêu cầu issuer; audience chỉ được ép khi danh sách cấu hình không rỗng. Có mode `Permissive` cho phép request thiếu/sai JWT. Đây là tuỳ chọn chức năng, không phải lỗi tự thân; cấu hình triển khai cần chọn mode và audience đúng với mức tin cậy.
- [Ví dụ MCP authorization](https://github.com/agentgateway/agentgateway/blob/084992d6091d671cf845e9cd40b16fed41c1511d/examples/mcp-authorization/config.yaml) minh hoạ CEL theo `jwt.sub` và `mcp.tool.name`, nhưng có CORS `*` và backend token passthrough. Không chép nguyên ví dụ thành cấu hình production: phải kiểm audience/credential flow tới upstream, origin được phép và network không cho bypass gateway. [CI](https://github.com/agentgateway/agentgateway/blob/084992d6091d671cf845e9cd40b16fed41c1511d/.github/workflows/pull_request.yml) có proxy test/lint đa OS, chưa thay kiểm chính sách nghiệp vụ của người tích hợp.

**Ma trận chọn cổng kiểm**

| Muốn chứng minh | Cổng phù hợp | Chưa chứng minh được |
|---|---|---|
| Message/transport đúng một bản spec | Conformance §4c, ghim harness + requirements | User được phép truy cập dữ liệu nào |
| Token đúng issuer/audience/thời hạn | SDK verifier hoặc gateway JWT với cấu hình thực | Quyền trên tool/resource của tenant |
| Người A không gọi được tool của B | CEL/tool policy + test deny list/call | Nội dung retrieved không có prompt injection |
| Không bypass chính sách | Backend chỉ nhận traffic gateway/credential hợp lệ | Model luôn dùng tool theo mục đích mong muốn |
| Đổi spec/SDK không âm thầm mất tính năng | Ma trận host × transport × spec + baseline diff | Hành vi của host/model chưa nằm trong test |

**Cách ghép:** server nhỏ dùng SDK và auth rõ trước; thêm gateway khi có nhiều upstream, policy/trace tập trung. Khóa đường trực tiếp tới upstream, cấp credential theo audience và phạm vi; chạy conformance cùng negative tests auth, expiry, wrong audience, cross-tenant, gọi tool không có trong list. ghép scanner §4c và guardrail mục 12 cho rủi ro nội dung. Các negative test nêu trên là tiêu chí đánh giá, **(chưa xác minh)** bằng chạy thật trong đợt này.

**Nguồn phần mở rộng:** [1](https://github.com/modelcontextprotocol/python-sdk/blob/d7845c073a2b9ba5ab2817ecf93d3e45ef24cd14/LICENSE) · [2](https://github.com/modelcontextprotocol/python-sdk/blob/d7845c073a2b9ba5ab2817ecf93d3e45ef24cd14/.github/workflows/conformance.yml) · [3](https://github.com/modelcontextprotocol/python-sdk/blob/d7845c073a2b9ba5ab2817ecf93d3e45ef24cd14/.github/actions/conformance/expected-failures.2026-07-28.yml) · [4](https://github.com/modelcontextprotocol/python-sdk/blob/d7845c073a2b9ba5ab2817ecf93d3e45ef24cd14/src/mcp/server/mcpserver/server.py) · [5](https://github.com/modelcontextprotocol/python-sdk/blob/d7845c073a2b9ba5ab2817ecf93d3e45ef24cd14/src/mcp/server/transport_security.py) · [6](https://github.com/modelcontextprotocol/python-sdk/blob/d7845c073a2b9ba5ab2817ecf93d3e45ef24cd14/src/mcp/server/auth/middleware/bearer_auth.py) · [7](https://github.com/agentgateway/agentgateway/blob/084992d6091d671cf845e9cd40b16fed41c1511d/LICENSE) · [8](https://github.com/agentgateway/agentgateway/blob/084992d6091d671cf845e9cd40b16fed41c1511d/crates/agentgateway/src/mcp/rbac.rs) · [9](https://github.com/agentgateway/agentgateway/blob/084992d6091d671cf845e9cd40b16fed41c1511d/crates/agentgateway/src/http/jwt.rs) · [10](https://github.com/agentgateway/agentgateway/blob/084992d6091d671cf845e9cd40b16fed41c1511d/examples/mcp-authorization/config.yaml) · [11](https://github.com/agentgateway/agentgateway/blob/084992d6091d671cf845e9cd40b16fed41c1511d/.github/workflows/pull_request.yml) · [12](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization/security-considerations)

## 4e. Kiểm ảnh "Codex Project Structure" (Ananya Ghosh Chowdhury): bản đồ file cấu hình dự án của OpenAI Codex, đối chiếu mã nguồn (ảnh người dùng gửi, 3/11/2026)

> Ảnh là cây thư mục `your-repo/` gồm `AGENTS.md`, `AGENTS.override.md`, `.agents/skills/deploy/{SKILL.md,scripts/}` và `.codex/{config.toml [mcp_servers.*], agents/*.toml, rules/default.rules, hooks.json, hooks/pre_tool_use.py, environments/environment.toml}`, mỗi nhánh có một hộp giải thích. Tác giả ghi trên ảnh: Ananya Ghosh Chowdhury (@ananyaghoshchowdhury). Đối chiếu với `openai/codex` (Apache-2.0, 132.944★) tại `ac91c14443c11c4279a9305099354e443c6fa7d4` (clone nông 3/11/2026). Docs trong repo (`docs/agents_md.md`, `docs/skills.md`…) chỉ trỏ ra developers.openai.com, nên phần lớn kiểm bằng mã Rust trong `codex-rs/`. **Không chạy Codex.**

| Hộp trong ảnh | Kết quả | Đối chiếu |
|---|---|---|
| **AGENTS.md**: gộp từ gốc tới thư mục hiện tại, file gần hơn thắng; `AGENTS.override.md` thay thế trong thư mục của nó; trần 32 KiB qua `project_doc_max_bytes` | ✅ | `core/src/agents_md.rs:45` `LOCAL_AGENTS_MD_FILENAME = "AGENTS.override.md"`; `config/src/config_toml.rs:77` `DEFAULT_PROJECT_DOC_MAX_BYTES = 32 * 1024`. Thứ tự gộp chưa đọc từng dòng |
| **skills/** trong `.agents/` (không phải `.codex/`); quét từ thư mục hiện tại lên gốc repo; lúc khởi động chỉ nạp name + description; gọi bằng `$deploy` | ✅ phần thư mục | `ext/skills/src/host_roots.rs:27` `AGENTS_DIR_NAME = ".agents"`; cũng có `~/.agents/skills` (`guardian-v2/.../trusted_skills.rs:22`). Cách nạp tiến dần và cú pháp `$tên` theo docs, chưa đọc mã **(chưa xác minh)** |
| **config.toml**: lớp dự án đè `~/.codex/config.toml`; `.codex/` lồng nhau thì gần nhất thắng; bị bỏ qua ở dự án không tin cậy | ✅ | Comment ở `config/src/loader/mod.rs:133–135`: cwd → các thư mục cha → gốc git tìm `./.codex/config.toml`, "loaded but disabled when untrusted" |
| **MCP servers**: STDIO hoặc streamable HTTP; không có `.mcp.json`, server là bảng trong `config.toml`; `codex mcp add`, `codex mcp login` (OAuth) | ✅ | `McpServerTransportConfig::{Stdio, StreamableHttp}`; `cli/src/mcp_cmd.rs:79` `Login(LoginArgs)` |
| **agents/**: mỗi subagent tùy biến là một file TOML; cần name, description, `developer_instructions`; có model, reasoning effort, sandbox riêng; có sẵn default, worker, explorer | ✅ | `agent-roles/src/agent_role_config.rs` kiểm `developer_instructions` không được rỗng; `core/src/agent/role.rs` có `DEFAULT_ROLE_NAME = "default"`, `"explorer"`, `"worker"` |
| **rules/**: `prefix_rule()` viết bằng Starlark theo tiền tố lệnh; kiểm lệnh chạy ngoài sandbox; allow/prompt/forbidden, mức chặt nhất thắng; thử bằng `codex execpolicy check` | ✅ | `execpolicy/src/decision.rs` (`Allow`, `Prompt`, `Forbidden`); `policy.rs:494` lấy `.max()` các quyết định khớp, tức chặt nhất thắng; có `execpolicy/src/execpolicycheck.rs` và lệnh `Execpolicy` trong `cli/src/main.rs:198` |
| **hooks.json**: script cho **12** sự kiện vòng đời; hoặc bảng `[hooks]` trong config.toml; exit code 2 để chặn tool call; phải được duyệt và tin cậy trong `/hooks` | ⚠️ số sự kiện | Tại HEAD có **14** sự kiện: PreModelRequest, PostModelRequest, PreToolUse, PermissionRequest, PostToolUse, PreCompact, PostCompact, SessionStart, SessionEnd, UserPromptSubmit, SubagentStart, SubagentStop, Stop, Interrupt (`app-server-protocol/src/protocol/v2/hook.rs:19`). Exit 2 đúng: `hooks/src/events/{post_tool_use,permission_request}.rs` xử lý `Some(2)` khi handler có quyền tác động. Handler có 4 loại (Command, McpTool, Prompt, Agent), ảnh chỉ nói script |
| Hộp cuối, tiêu đề "**Tokenomics**": môi trường local cho app ChatGPT desktop; setup script chạy với mỗi worktree mới; Actions (Run, Test) trên thanh trên cùng; commit để chia sẻ | ⚠️ sai tiêu đề | Nội dung nói về **local environments** (`.codex/environments/environment.toml`), không liên quan token. App desktop không có mã nguồn mở. Docs chính thức (developers.openai.com/codex/app/local-environments) xác nhận setup script chạy khi tạo worktree, actions nằm trên thanh trên cùng, file commit được. Schema file chỉ thấy trên trang skill cộng đồng **(chưa xác minh)** |

**So với Claude Code (để ai dùng cả hai biết file nào tương ứng):** `AGENTS.md` ↔ `CLAUDE.md` (Claude Code đọc AGENTS.md qua `@import`, §4); `.agents/skills/` ↔ `.claude/skills/` (cùng định dạng SKILL.md); `.codex/config.toml [mcp_servers]` ↔ `.mcp.json`; `.codex/agents/*.toml` ↔ `.claude/agents/*.md`; `.codex/rules/*.rules` (Starlark) ↔ `permissions` trong `.claude/settings.json`; `.codex/hooks.json` ↔ `hooks` trong `settings.json` (Claude Code cũng chặn bằng exit code 2). Khác biệt đáng chú ý: Codex **tắt toàn bộ cấu hình dự án** khi thư mục chưa được tin cậy, và hook dự án phải được duyệt trong `/hooks`. Đây là lớp chặn hữu ích khi clone repo lạ có `.codex/` độc hại.

**Dùng thế nào:** ảnh đúng khoảng 6/8 hộp và là bản đồ nhanh tốt. Trước khi dựa vào số liệu cụ thể (số sự kiện hook, giá trị mặc định), hãy kiểm lại docs chính thức hoặc mã, vì Codex đổi nhanh (hai sự kiện model-request và Interrupt không có trong ảnh).

**Nguồn §4e:** ảnh người dùng gửi 3/11/2026 · clone `--depth 1` https://github.com/openai/codex HEAD `ac91c14443c11c4279a9305099354e443c6fa7d4`: https://github.com/openai/codex/blob/ac91c14443c11c4279a9305099354e443c6fa7d4/codex-rs/core/src/agents_md.rs · https://github.com/openai/codex/blob/ac91c14443c11c4279a9305099354e443c6fa7d4/codex-rs/config/src/config_toml.rs · https://github.com/openai/codex/blob/ac91c14443c11c4279a9305099354e443c6fa7d4/codex-rs/config/src/loader/mod.rs · https://github.com/openai/codex/blob/ac91c14443c11c4279a9305099354e443c6fa7d4/codex-rs/ext/skills/src/host_roots.rs · https://github.com/openai/codex/blob/ac91c14443c11c4279a9305099354e443c6fa7d4/codex-rs/agent-roles/src/agent_role_config.rs · https://github.com/openai/codex/blob/ac91c14443c11c4279a9305099354e443c6fa7d4/codex-rs/core/src/agent/role.rs · https://github.com/openai/codex/blob/ac91c14443c11c4279a9305099354e443c6fa7d4/codex-rs/execpolicy/src/decision.rs · https://github.com/openai/codex/blob/ac91c14443c11c4279a9305099354e443c6fa7d4/codex-rs/execpolicy/src/policy.rs · https://github.com/openai/codex/blob/ac91c14443c11c4279a9305099354e443c6fa7d4/codex-rs/cli/src/mcp_cmd.rs · https://github.com/openai/codex/blob/ac91c14443c11c4279a9305099354e443c6fa7d4/codex-rs/app-server-protocol/src/protocol/v2/hook.rs · https://github.com/openai/codex/blob/ac91c14443c11c4279a9305099354e443c6fa7d4/codex-rs/hooks/src/events/post_tool_use.rs · https://developers.openai.com/codex/app/local-environments · GitHub search API `repo:openai/codex` 3/11/2026.

<a id="factory-protocol-conformance-evidence-2026-11-04"></a>

## 4f. Nâng trần 4/11/2026: phiên bản conformance, mẫu số và license là một phần hợp đồng tích hợp

> Đọc lại MCP Conformance (nhóm Model Context Protocol), `c37eec888e1c6ff140af79987a40008548b7cc5f`, ngày 2026-11-04; **code-read**, không chạy client/server hay bộ test upstream; không cập nhật sao. Nối §4c–§4d; không suy trạng thái chuẩn đã final từ tên một thư mục hay một revision của harness.

**Trần còn thiếu:** có test conformance chưa trả lời “phiên bản wire nào, test nào được tính, có bao nhiêu skipped/expected failures, chứng minh quyền của ứng dụng tới đâu?”. Xưởng phải lưu toàn bộ hợp đồng kiểm này để lần nâng SDK không đổi nghĩa pass âm thầm.

### MCP Conformance: frozen requirements khác toàn bộ suite hiện tại

- [README](https://github.com/modelcontextprotocol/conformance/blob/c37eec888e1c6ff140af79987a40008548b7cc5f/README.md) phân `--suite`, `--spec-version` và `--requirements <revision>`. Requirements đóng băng danh sách cho revision, cố định wire version và thay lựa chọn suite/scenario; harness còn có scenario ngoài phần chấm. Một scenario có ở cả hai revision phải được chạy cho từng wire; pass một phiên bản không suy sang phiên bản khác.
- [Loader requirements](https://github.com/modelcontextprotocol/conformance/blob/c37eec888e1c6ff140af79987a40008548b7cc5f/src/requirements.ts) chỉ nhận các role client/server, chặn khai báo authorization-server vào requirement set. [`requirementsExitCode`](https://github.com/modelcontextprotocol/conformance/blob/c37eec888e1c6ff140af79987a40008548b7cc5f/src/index.ts) lọc scenario được chấm; lỗi ở `not_scored` vẫn báo nhưng không làm exit code của conformance thất bại. Do đó giữ **scored, not-scored, skipped và baseline expected-failure** riêng trong artifact; một tỷ lệ pass không đại diện mọi scenario.
- [Requirement set cụ thể](https://github.com/modelcontextprotocol/conformance/blob/c37eec888e1c6ff140af79987a40008548b7cc5f/requirements/2026-07-28.yaml) cùng bản harness là bằng chứng tái kiểm. Những revision/nhãn draft trong upstream cần được đối chiếu đặc tả đang triển khai trước tích hợp; không tự chuyển production sang draft vì nó xuất hiện trong `list`.
- [LICENSE thực](https://github.com/modelcontextprotocol/conformance/blob/c37eec888e1c6ff140af79987a40008548b7cc5f/LICENSE) ghi quá trình **MIT → Apache-2.0**: đóng góp chưa có đồng ý chuyển vẫn theo MIT; đóng góp code/spec mới theo Apache-2.0; tài liệu trừ specification theo CC-BY-4.0. Không gán nguyên cây là “MIT thuần” hoặc “Apache-2.0 thuần”; kiểm notice khi đóng gói lại.

| Lớp | Công cụ/nguồn so sánh | Phạm vi đúng |
|---|---|---|
| Wire interoperability MCP | MCP Conformance + requirement revision | Message/schema/lifecycle và scenario cụ thể |
| A2A | A2A TCK/Inspector (§4c) | Giao thức A2A; không thay MCP tests |
| Kiểm bề mặt tool | Cisco MCP Scanner (§4c) | Tín hiệu policy/phân tích theo khả năng scanner, không là bằng chứng nghiệp vụ |
| API nghiệp vụ/tenant | OpenAPI + oasdiff (mục 29), test runtime (mục 30/34) | AuthZ, ownership, compatibility và side effect của ứng dụng |

**Chuỗi nâng SDK cho xưởng:** (1) inventory client/server, transport, wire revision và extension sử dụng; (2) ghim SDK, harness SHA, requirements file, exception baseline; (3) chạy role/transport thực sự cần và negative fixture để biết bộ chấm bắt lỗi; (4) lưu checks.json với passed/failed/skipped/not-scored/expected-failure và version; (5) kiểm độc lập access token audience, tenant, quyền từng tool và hành động lặp; (6) thử rollback về SDK/config trước. Harness không tự chứng minh một người dùng có quyền đọc một hồ sơ trong sản phẩm.

**Cổng nhận đề xuất:** không giảm số scenario required ngoài thay đổi revision có duyệt; không biến failure thành baseline chỉ để xanh; mọi exception có phạm vi/owner/hạn xem lại; quyền ứng dụng có ca từ chối truy cập chéo tenant. Đây là tiêu chí tích hợp, chưa chạy trong đợt đọc mã.

**Nguồn kiểm cấu hình:** [CI](https://github.com/modelcontextprotocol/conformance/blob/c37eec888e1c6ff140af79987a40008548b7cc5f/.github/workflows/ci.yml) · [Expected failures](https://github.com/modelcontextprotocol/conformance/blob/c37eec888e1c6ff140af79987a40008548b7cc5f/src/expected-failures.ts). CI chạy kiểm/build/test harness; không chứng nhận một deployment của xưởng.

## 4g. Hồ sơ `ag-ui-protocol/ag-ui`: AG-UI 1.0, giao thức sự kiện nối agent với giao diện người dùng (ảnh thẻ GitHub người dùng gửi, đọc mã 19/11/2026)

> **Nguồn:** ảnh thẻ GitHub (182 contributor, 21k sao, 2k fork). Clone nông HEAD `3416b86` (commit 17/11/2026), đọc README, LICENSE, `DEPRECATIONS.md`, `spec/README.md`, `spec/1.0/schema.json` và cây `sdks/`, `integrations/`, `middlewares/`. GitHub search API 19/11/2026: ★ 20.574, fork 2.118, MIT, tạo 7/5/2025. Mục §1 và §4b.1 có dòng AG-UI cũ (16,9k, 31/10/2026); hồ sơ này thay cho chúng.

**Làm gì:** giao thức mở, dựa trên sự kiện, chuẩn hoá cách agent nói chuyện với ứng dụng người dùng. Agent là một HTTP endpoint nhận `RunAgentInput` và stream sự kiện về (SSE hoặc wire nhị phân); client không đổi khi đổi framework agent phía sau. Trong bộ ba giao thức: MCP cho agent dùng tool, A2A cho agent nói với agent, AG-UI cho agent đến người dùng. A2UI, MCP Apps là spec mô tả giao diện agent muốn hiện; AG-UI là giao thức runtime chở chúng.

**Điểm mạnh (đọc mã):**

- **Spec 1.0 đóng băng, có máy kiểm:** bản 1.0 phát hành 17/9/2026, hợp đồng là [`spec/1.0/schema.json`](https://github.com/ag-ui-protocol/ag-ui/blob/3416b86da4b3288e87f827c7f2759a7fa18b5231/spec/1.0/schema.json) (JSON Schema, mọi object đóng bằng `unevaluatedProperties: false`) với 31 loại sự kiện: tin nhắn, tool call, state snapshot/delta (JSON Patch), messages snapshot, activity, run/step, reasoning (kể cả giá trị mã hoá), subagent. `spec/harness/` có test conformance, fixture chấp nhận/từ chối, `proto-freeze.txt` là sổ số hiệu wire nhị phân chỉ được thêm.
- **SDK sinh từ schema:** TypeScript (`@ag-ui/client`), Python (`ag-ui-protocol`), .NET (`AGUI.Client`) sinh tất định bởi `spec/generator/`; SDK cộng đồng Kotlin, Go, Java, Dart, Rust, Ruby, C++, Swift. Nguyên tắc "object chính xác, bên nhận dễ tính": bên nhận bỏ trường lạ kèm cảnh báo thay vì từ chối stream.
- **Lộ trình ngừng dùng rõ ràng:** [`DEPRECATIONS.md`](https://github.com/ag-ui-protocol/ag-ui/blob/3416b86da4b3288e87f827c7f2759a7fa18b5231/DEPRECATIONS.md) liệt kê từng dạng cũ (vd `THINKING_*` → `REASONING_*`, phần `binary` → phần media có `source`), shim nằm ở đâu và ngày hết hạn chung 17/9/2027 (12 tháng sau 1.0); middleware tương thích theo phiên bản peer.
- **Tích hợp rộng:** 22 thư mục tích hợp trong `integrations/` (LangGraph, CrewAI, Microsoft Agent Framework, Google ADK, AWS Strands, Mastra, Pydantic AI, LlamaIndex, Agno, AG2, Claude Agent SDK, Claude Managed Agents, OpenAI Agents, Vercel AI SDK, watsonx…), 6 middleware (MCP, MCP Apps, A2A, A2UI, throttle sự kiện), mỗi framework có demo ở Dojo; Amazon Bedrock AgentCore hỗ trợ AG-UI trong runtime.
- **Khối tính năng map vào sự kiện:** streaming chat có huỷ và chạy tiếp, generative UI, shared state, frontend tool, human-in-the-loop bằng kết quả `interrupt`, hiển thị reasoning.

**Cài và dùng:**

```sh
npx create-ag-ui-app@latest            # dựng app CopilotKit/Next.js hoặc client terminal nối framework agent đã chọn
pip install ag-ui-protocol             # SDK Python cho phía agent
npm install @ag-ui/client              # SDK TypeScript cho phía client
```

README có ví dụ 30 dòng: server FastAPI phát `RUN_STARTED`, `TEXT_MESSAGE_*`, `RUN_FINISHED` và client `HttpAgent` in chuỗi stream, không cần khoá API.

**Điều kiện:** MIT. Python 3.9+ cho SDK Python, Node.js 20+ cho client mẫu. Template của `create-ag-ui-app` gọi OpenAI nên cần `OPENAI_API_KEY`. Giao thức do CopilotKit khởi xướng; client giao diện có sẵn chủ yếu là CopilotKit (React, Angular, Vue, React Native). Peer nói phiên bản trước 1.0 chỉ được hỗ trợ qua shim tới 17/9/2027.

**Dùng khi:** cần đưa agent vào giao diện người dùng (web, mobile, Slack/Teams, terminal) mà không viết giao thức stream riêng cho từng framework; cần shared state hai chiều, tool chạy phía app hoặc duyệt của người giữa lượt chạy. Liên quan: §1 (bản đồ giao thức), §4b.3 (A2UI), §4c (bộ conformance của MCP/A2A), mục 06 §7p (OpenUI, Tambo dùng sự kiện AG-UI).

<a id="ag-ui-reread-2026-11-26"></a>

### 4g.1. Đọc lại 26/11/2026: kiểm ảnh README và các bản vá bảo mật tích hợp

> Ảnh người dùng gửi là phần đầu README (huy hiệu npm v1.0.5, 8,1M lượt tải/tuần, PyPI v1.0.0, nút "Talk to the team", huy hiệu "#1 Repository Of The Day"). Đối chiếu với clone `blob:none` tại [`ed94ca4`](https://github.com/ag-ui-protocol/ag-ui/tree/ed94ca4a3240527d3ef20fd0f0cc63501f44e469) (commit 23/11/2026), 43 commit kể từ `3416b86`. Số liệu đọc 26/11/2026: GitHub search API ★ 21.802, fork 2.190, MIT, không archive; npm API `@ag-ui/core` 1.0.5 và 8.048.263 lượt tải tuần 19–25/11 (`@ag-ui/client` 2.530.482); PyPI `ag-ui-protocol` 1.0.0. Mức `code-read` cho các changelog và commit nêu dưới, không chạy mã.

**Ảnh khớp với repo**, và phần đầu README không đổi so với bản 19/11. Ba điểm cần đọc đúng:

- **8,1M lượt tải/tuần** là của `@ag-ui/core`, gói kiểu dữ liệu mà các SDK và framework khác kéo theo. Con số này gồm cả tải gián tiếp qua dependency và CI, nên không phải số dự án dùng AG-UI. Gói client chỉ có 2,5M.
- **"#1 Repository Of The Day"** là huy hiệu động của Trendshift (bên thứ ba), không phải xếp hạng của GitHub. Huy hiệu này đã có từ bản README 19/11.
- **"Talk to the team"** dẫn tới trang [Production support](https://docs.ag-ui.com/talk-to-us): dịch vụ tư vấn kiến trúc và triển khai có trả phí, không bắt buộc. Giao thức và SDK vẫn là MIT. SECURITY.md cho thấy CopilotKit giữ kênh báo lỗi bảo mật.

**Phát hiện mới: năm bản vá bảo mật ở lớp tích hợp, gộp ngày 21/11/2026.** Năm commit "Merge commit from fork" của maintainer Jordan Ritter là kiểu gộp từ fork riêng của GitHub Security Advisory. Changelog ghi rõ lỗi:

| Gói (bản vá) | Lỗi trước bản vá | Cách sửa |
|---|---|---|
| `ag_ui_adk` (Python, 0.14.0; ghi [GHSA-jhvp-j8pf-5vh5](https://github.com/ag-ui-protocol/ag-ui/blob/ed94ca4a3240527d3ef20fd0f0cc63501f44e469/integrations/adk-middleware/python/CHANGELOG.md)) | `dependencies` dùng để xác thực chỉ áp cho route agent. `/agents/state` vẫn mở, nên người chưa đăng nhập đọc được state và lịch sử tin nhắn của thread. State dạng mảng cặp `[key, value]` lọt qua kiểm scope `app:`/`user:`, cho phép client ghi state toàn app. | Áp `dependencies` cho cả `/capabilities` và `/agents/state`. Trả 422 khi state không phải object. Header của request thắng `state.headers` do client gửi. Tài liệu đổi sang lấy user ID từ request thay vì context của client. |
| `ag-ui-openai-agents` ([0.2.0](https://github.com/ag-ui-protocol/ag-ui/blob/ed94ca4a3240527d3ef20fd0f0cc63501f44e469/integrations/openai-agents/python/CHANGELOG.md)) | Client tự thêm một tool call vào lịch sử của mình (tool bất kỳ, đối số bất kỳ) rồi duyệt nó trong `resume`, và server chạy tool đó trước cả lượt gọi model. Client cũng sửa được đối số của lệnh đang chờ duyệt hoặc gửi lại để chạy hai lần. | Mỗi lệnh tạm dừng có token HMAC gắn thread, call id, tên tool và đối số; token dùng một lần và có hạn. Cần biến `AG_UI_OPENAI_AGENTS_APPROVAL_SECRET` ≥ 32 byte. **Chạy nhiều worker thì phải dùng store `ConsumedTokens` chung (vd Redis)**, nếu không thì gửi lại vào worker khác vẫn chạy tool. |
| `ag-ui-langgraph` (Python 0.0.48) và `@ag-ui/langgraph` ([TS 0.0.47](https://github.com/ag-ui-protocol/ag-ui/blob/ed94ca4a3240527d3ef20fd0f0cc63501f44e469/integrations/langgraph/typescript/CHANGELOG.md)) | `forwardedProps` của client lái được run: `node_name` để bỏ qua node duyệt quyền, `config` ghi đè `assistantConfig`, `command.goto/update`, `checkpoint`, `durability`. Chế độ continue chạy tiếp với input đã đổi mà không qua lại node kiểm. | Allowlist `forwardedProps` (chỉ còn `streamSubgraphs`, `durability`), `command` chỉ nhận `resume`. Continue chỉ đi từ node mà lịch sử thread cho thấy đã chạy cuối. Input đổi thì mở run mới để cổng kiểm chạy lại. Đây là **breaking change**, cần kiểm lại luồng continue. |

OSV.dev chưa có mục nào cho các gói này khi tra ngày 26/11/2026, và API advisory của repo không mở cho phiên này. Vì vậy chỉ GHSA-jhvp-j8pf-5vh5 có mã trong changelog; ba advisory còn lại **(chưa xác minh)** đã công bố hay chưa.

**Bài học khi tích hợp:** spec 1.0 không đổi, nhưng cả ba lỗi đều cùng một kiểu: adapter tin những gì client gửi trong `RunAgentInput` (`state`, `forwardedProps`, lịch sử tin nhắn có tool call). Với AG-UI, client là bên không tin được. Danh tính lấy từ request đã xác thực; mọi trường client gửi qua allowlist; quyết định duyệt (human-in-the-loop) phải gắn với lệnh do chính server tạm dừng. Ai dùng các adapter ADK, OpenAI Agents, LangGraph cần nâng lên bản trên. Cùng đợt có PR #3303 siết quy trình phát hành: nhánh release do bot giữ, `required-checks.yml` gate theo vùng thay đổi, bỏ workflow tự duyệt PR cộng đồng.

<a id="awesome-mcp-servers-reread-2026-11-21"></a>

## 4h. Kiểm ảnh trang repo `punkpeye/awesome-mcp-servers` (ảnh người dùng gửi, đọc 21/11/2026)

> Ảnh chụp trang GitHub: 97,8k★, 20,2k fork, 15.249 commit, 3.940 contributor, commit gần nhất `5fb385c` (14 giờ trước), MIT. Đối chiếu với clone `blob:none` tại `5fb385c3c56a004eacad6a21cb446205c787926b` (commit 16/11/2026) và GitHub search API 21/11/2026. Mức `docs-read`; không kiểm từng server trong danh sách.

| Ô trong ảnh | Kết quả | Ghi chú |
|---|---|---|
| 15.249 commit, HEAD `5fb385c` | ✅ khớp | Đúng với clone (`git rev-list --count`: 15.249) |
| 97,8k★ / 20,2k fork | ✅ → nay **98.334★ / 20.539 fork** | Ảnh cũ vài ngày; GitHub search API 21/11/2026 |
| MIT | ✅ | LICENSE trong repo |
| 3.940 contributor | chưa kiểm | Số do GitHub hiển thị, không kiểm lại bằng API |
| "A collection of MCP servers" | ✅ | Mô tả repo |

**Cấu trúc và đặc điểm (đọc `README.md`, `CONTRIBUTING.md`, workflow):**

- `README.md` 5.450 dòng, **4.982 dòng mục server**, 10 mục `##`; thêm bản dịch (fa, ja, ko, pt-BR, th, zh, zh-TW). Khoảng **521** dòng gắn 🎖️ (server chính chủ). Không có mã thực thi nào của danh sách ngoài workflow.
- **Phạm vi:** chỉ server có **repo GitHub công khai tự cài/chạy**; server chỉ-từ-xa (URL hosted) thuộc `awesome-remote-mcp-servers`. Dùng bảng này cùng `modelcontextprotocol/servers` (mục này) và `VoltAgent/official-mcp-servers` (§2c) để chọn.
- **Một người chi phối:** Frank Fiegel (`punkpeye`) **6.252/15.249 commit (~41%)**; người kế tiếp 96 commit. Bus factor cao, nhưng nhiều contributor chỉ thêm một dòng.
- **Gắn với doanh nghiệp của chủ repo (glama.ai):** README có banner quảng cáo ("ray.run", liên kết `glama.ai/advertise` đánh dấu *Ad*), huy hiệu Discord/subreddit của Glama, và khoảng **3.699 dòng gắn huy hiệu điểm của Glama** (`glama.ai/mcp/servers/.../badges/score.svg`). Workflow `check-glama.yml` bắt PR phải có liên kết Glama. Đây không phải sai, nhưng nghĩa là **thứ hạng/điểm hiển thị là của dịch vụ thương mại**, và danh sách hướng người dùng về Glama.
- **Đường tắt cho agent:** `CONTRIBUTING.md` ghi PR của agent tự động được **merge nhanh** nếu thêm `🤖🤖🤖` vào tiêu đề. Nghĩa là có thể tin ít hơn vào việc mỗi mục đã được người đọc kiểm. Workflow dùng `pull_request_target` (quyền ghi PR/issue); tôi chỉ đọc đầu file, **không đánh giá an toàn** của workflow.

**Dùng thế nào:** coi đây là **mục lục để tìm ứng viên**, không phải bảo chứng. Trước khi cài một server từ danh sách, đọc mã/quyền của chính repo đó (xem mẫu kiểm MCP ở các mục trên): danh sách không kiểm license, quyền ghi hay telemetry của từng server. Với nhu cầu chỉ server chính chủ, dùng `VoltAgent/official-mcp-servers` hoặc registry chính thức.

**Nguồn §4h:** clone github.com/punkpeye/awesome-mcp-servers 21/11/2026 (blob:none, 15.249 commit, HEAD 5fb385c; `README.md`, `CONTRIBUTING.md`, `LICENSE`, `.github/workflows/check-glama.yml`, `git shortlog`) · GitHub search API (số sao/fork) 21/11/2026 · ảnh trang repo do người dùng cung cấp

<a id="anhkysuai-2026-11-23"></a>

## Đánh giá từ kho Anh Kỹ Sư AI — 23/11/2026

Phần này có **4 hồ sơ hoặc phạm vi đối chiếu** từ [nguồn tuyển chọn](https://anhkysuai.com/kho/). [Bảng đủ 1.295 repo](../data/collections/anhkysuai-kho.json) ghi trạng thái đối chiếu từng link; [danh sách URL](../data/collections/anhkysuai-kho-links.txt) phục vụ tra cứu. Nguồn tuyển chọn giúp phát hiện repo; đánh giá bên dưới dựa trên clone và permalink upstream cùng metadata GitHub ngày 2026-11-23.

Mức `docs-read`/`code-read` chỉ áp dụng phạm vi ghi tại mỗi hồ sơ. Chưa cài, build, chạy test hay benchmark mã upstream. Giấy phép có thể tách theo code, model, nội dung, asset hoặc bản enterprise; con số/tuyên bố của tác giả chưa được tái lập nếu không có ghi chú khác.

<a id="anhkysuai-2026-11-23-apache-apisix"></a>

### Apache APISIX

**Repo:** [apache/apisix](https://github.com/apache/apisix) · **License:** Apache-2.0; kèm notices thành phần thứ ba · **★ 17,361 (GitHub API, 2026-11-23)**

**Mục đích:** API gateway động cho định tuyến, kiểm soát lưu lượng và các API mô hình AI.

**Giá trị và cơ chế:** README mô tả lớp NGINX/OpenResty, plugin xác thực, canary, circuit breaker và observability; phù hợp điểm vào chung cho dịch vụ truyền thống lẫn LLM.

**Giới hạn:** Chưa đọc triển khai plugin hoặc đo benchmark. Gateway không tự giải quyết quyền dữ liệu trong ứng dụng; cấu hình plugin, upstream và control plane quyết định vận hành.

**Cách tham khảo/tích hợp:** Dùng route thử với retry/rate limit rõ ràng, đo streaming và xử lý lỗi trước chuyển lưu lượng thật.

**Thay thế:** [kong](../08-awesome-lists-learning/README.md#6c55-container--devops), [LiteLLM](https://github.com/BerriAI/litellm), envoy.

**Bằng chứng:** `docs-read`, ngày 2026-11-23, commit [`bd310c5782e4`](https://github.com/apache/apisix/commit/bd310c5782e46fed758582a184fe387cf5df8d39). README và các tài liệu/manifest/CI hiện diện, đọc chọn lọc; chưa kiểm implementation. Chưa cài/chạy upstream.

**Nguồn:** [README.md](https://github.com/apache/apisix/blob/bd310c5782e46fed758582a184fe387cf5df8d39/README.md) · [LICENSE](https://github.com/apache/apisix/blob/bd310c5782e46fed758582a184fe387cf5df8d39/LICENSE) · [metadata GitHub](https://api.github.com/repos/apache/apisix).

<a id="anhkysuai-2026-11-23-dsh-our-free-model"></a>

### dsh-our-free-model

**Repo:** [Ebony-Vinyl/dsh-our-free-model](https://github.com/Ebony-Vinyl/dsh-our-free-model) · **License:** MIT và notices thành phần; Qoder auth WASM chưa rõ quyền phân phối · **★ 84,542 (GitHub API, 2026-11-23)**

**Mục đích:** Plugin và proxy local tập hợp nhiều đường truy cập mô hình qua gateway/nhà cung cấp.

**Giá trị và cơ chế:** README mô tả catalog cập nhật từ upstream, kiểm khả dụng theo mạng và chuyển tiếp API tương thích OpenAI; hữu ích tham khảo quản lý provider và chẩn đoán lỗi route.

**Giới hạn:** LICENSE tự ghi Qoder auth WASM chưa xác định cơ sở phân phối; không gọi cả gói MIT. Cam kết miễn phí/không giới hạn chưa kiểm; README thừa nhận quota, chặn vùng và upstream có thể lưu prompt.

**Cách tham khảo/tích hợp:** Đánh giá adapter với tài khoản được phép, tránh nội dung bí mật và kiểm điều khoản từng upstream trước dùng.

**Thay thế:** [LiteLLM](https://github.com/BerriAI/litellm), [CLIProxyAPI](../04-protocols-standards/README.md#anhkysuai-2026-11-23-cliproxyapi), [one-api](https://github.com/songquanpeng/one-api).

**Bằng chứng:** `docs-read`, ngày 2026-11-23, commit [`f111941c46bb`](https://github.com/Ebony-Vinyl/dsh-our-free-model/commit/f111941c46bb6789b236d858ed85edbe41c89bfc). README và các tài liệu/manifest/CI hiện diện, đọc chọn lọc; chưa kiểm implementation. Chưa cài/chạy upstream.

**Nguồn:** [README.md](https://github.com/Ebony-Vinyl/dsh-our-free-model/blob/f111941c46bb6789b236d858ed85edbe41c89bfc/README.md) · [LICENSE](https://github.com/Ebony-Vinyl/dsh-our-free-model/blob/f111941c46bb6789b236d858ed85edbe41c89bfc/LICENSE) · [metadata GitHub](https://api.github.com/repos/Ebony-Vinyl/dsh-our-free-model).

<a id="anhkysuai-2026-11-23-gpt4free"></a>

### GPT4Free

**Repo:** [xtekky/gpt4free](https://github.com/xtekky/gpt4free) · **License:** GPL-3.0 · **★ 67,099 (GitHub API, 2026-11-23)**

**Mục đích:** Tập hợp adapter nhiều nhà cung cấp LLM/media với GUI và REST API tương thích OpenAI.

**Giá trị và cơ chế:** README mô tả client Python/JavaScript, chế độ synchronous/async và Docker; hữu ích tham khảo chuẩn hóa bề mặt provider cho thử nghiệm.

**Giới hạn:** Tên gpt4free không bảo đảm quyền truy cập, miễn phí hoặc ổn định; provider có thể cần token và đổi giao diện. Chưa kiểm đường truyền, đăng nhập hay toàn adapter. README yêu cầu auth/HTTPS khi đưa server ra mạng.

**Cách tham khảo/tích hợp:** Chỉ cấu hình provider được phép sử dụng, lưu lỗi/quota rõ ràng và tách thử nghiệm khỏi dịch vụ sản xuất.

**Thay thế:** [LiteLLM](https://github.com/BerriAI/litellm), [CLIProxyAPI](../04-protocols-standards/README.md#anhkysuai-2026-11-23-cliproxyapi), openrouter.

**Bằng chứng:** `docs-read`, ngày 2026-11-23, commit [`9059e300bdd7`](https://github.com/xtekky/gpt4free/commit/9059e300bdd71a02973107805933cd882040de4b). README và các tài liệu/manifest/CI hiện diện, đọc chọn lọc; chưa kiểm implementation. Chưa cài/chạy upstream.

**Nguồn:** [README.md](https://github.com/xtekky/gpt4free/blob/9059e300bdd71a02973107805933cd882040de4b/README.md) · [LICENSE](https://github.com/xtekky/gpt4free/blob/9059e300bdd71a02973107805933cd882040de4b/LICENSE) · [metadata GitHub](https://api.github.com/repos/xtekky/gpt4free).

<a id="anhkysuai-2026-11-23-cliproxyapi"></a>

### CLIProxyAPI

**Repo:** [router-for-me/CLIProxyAPI](https://github.com/router-for-me/CLIProxyAPI) · **License:** MIT · **★ 59,282 (GitHub API, 2026-11-23)**

**Mục đích:** Proxy Go đưa nhiều provider/CLI account về API tương thích OpenAI, Gemini hoặc Claude.

**Giá trị và cơ chế:** README và go.mod thể hiện adapter giao thức, model alias và các dự án quản lý liên quan; hữu ích tham khảo cách đồng nhất nhiều bề mặt API cho client.

**Giới hạn:** Chưa đọc adapter xác thực hoặc xác minh mọi endpoint đang hoạt động. Điều khoản tài khoản và quota upstream độc lập MIT; workflow được xem chỉ build/cross-build, không xác nhận tính tương đương giao thức.

**Cách tham khảo/tích hợp:** Dùng credential được phép, kiểm streaming/tool-call và thông báo lỗi theo từng provider trước thay endpoint.

**Thay thế:** [LiteLLM](https://github.com/BerriAI/litellm), [one-api](https://github.com/songquanpeng/one-api), apisix.

**Bằng chứng:** `docs-read`, ngày 2026-11-23, commit [`6eb8554f0ede`](https://github.com/router-for-me/CLIProxyAPI/commit/6eb8554f0ede597b2aa3e508ffb3f111d3c2b9e6). README và các tài liệu/manifest/CI hiện diện, đọc chọn lọc; chưa kiểm implementation. Chưa cài/chạy upstream.

**Nguồn:** [README.md](https://github.com/router-for-me/CLIProxyAPI/blob/6eb8554f0ede597b2aa3e508ffb3f111d3c2b9e6/README.md) · [LICENSE](https://github.com/router-for-me/CLIProxyAPI/blob/6eb8554f0ede597b2aa3e508ffb3f111d3c2b9e6/LICENSE) · [metadata GitHub](https://api.github.com/repos/router-for-me/CLIProxyAPI).

## 5. Nguồn

- https://en.wikipedia.org/wiki/Model_Context_Protocol · https://github.com/wong2/awesome-mcp-servers · https://github.com/sadekxD/Awesome-MCP · https://uibakery.io/blog/best-mcp-servers
- https://www.mintmcp.com/blog/a2a-vs-mcp · https://crystl.dev/blog/agent-communication-protocols/ · https://stellagent.ai/insights/a2a-protocol-google-agent-to-agent · https://www.flowhunt.io/blog/agentic-ai-foundation-a2a-mcp-standards/ · https://techiehub.blog/what-is-the-a2a-protocol/
- https://github.com/ag-ui-protocol/ag-ui · https://blogs.oracle.com/ai-and-datascience/announcing-agent-spec-for-a2ui-copilotkit-ag-ui · https://aws.amazon.com/blogs/machine-learning/build-generative-ui-for-ai-agents-on-amazon-bedrock-agentcore-with-the-ag-ui-protocol/ · https://learn.microsoft.com/en-us/agent-framework/integrations/ag-ui/
- https://blog.buildbetter.ai/agents-md-vs-cursorrules-vs-claude-skills-2026-comparison/ · https://meshlaunch.com/en/blog/2026-cursor-agent-skills-complete-guide.html · https://codersera.com/blog/agents-md-vs-claude-md-vs-cursor-rules-comparison-2026/ · https://dev.to/creeta/one-skillmd-replaces-claudemd-agentsmd-and-cursorrules-5a70
- §2b (12/10/2026): https://github.com/modelcontextprotocol/python-sdk · https://github.com/modelcontextprotocol/typescript-sdk · https://github.com/modelcontextprotocol/inspector · https://github.com/modelcontextprotocol/registry · https://github.com/modelcontextprotocol/ext-apps · https://github.com/MCP-UI-Org/mcp-ui · https://github.com/agentclientprotocol/agent-client-protocol · https://agentclientprotocol.com/get-started/clients · https://github.com/agentsmd/agents.md · https://agents.md/ · https://github.com/i-am-bee/acp · https://github.com/agntcy
- §2c (12/10/2026): https://github.com/VoltAgent/official-mcp-servers · https://raw.githubusercontent.com/VoltAgent/official-mcp-servers/main/CONTRIBUTING.md · https://repos.ecosyste.ms/api/v1/hosts/GitHub/repositories/VoltAgent%2Fofficial-mcp-servers · https://github.com/orgs/VoltAgent/repositories · https://github.com/VoltAgent/voltagent · https://github.com/PostHog/mcp · https://github.com/semgrep/mcp · https://github.com/browserbase/mcp-server-browserbase · https://github.com/elevenlabs/elevenlabs-mcp · https://github.com/JetBrains/mcp-jetbrains · https://github.com/langfuse/mcp-server-langfuse · https://github.com/ahujasid/mcp-for-blender · https://github.com/google/mcp · https://github.com/modelcontextprotocol/servers · https://github.com/punkpeye/awesome-mcp-servers · https://github.com/wong2/awesome-mcp-servers · https://glama.ai/mcp/servers · https://smithery.ai

<a id="chuan-hoa-2026-11-23"></a>

## Chuẩn hóa bằng chứng hồ sơ cũ — 23/11/2026

Các hồ sơ dưới đây có từ trước khi kho ghi mức kiểm. Ngày 2026-11-23 mỗi repo được clone nông tại commit ghi trong bảng, đọc LICENSE, README, manifest và CI (nếu có); không cài, build hay chạy mã upstream. Nhận định cũ ở phần trên giữ nguyên; chỗ nào khác với lần đọc này được ghi trong cột Nhận định. Số sao lấy qua GitHub search API cùng ngày.

<a id="ch-a2a"></a>

### A2A

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/a2aproject/A2A |
| License | Apache-2.0 |
| Phiên bản đã đọc | `5f931b8a25fe66789f987ec4a55fc16ee9fe41ee` (commit 2026-11-18) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE, CHANGELOG.md, GOVERNANCE.md; chưa chạy upstream |
| Bảo trì | active |
| Nhận định | Repo đặc tả A2A (giao tiếp agent ↔ agent giữa các hệ thống "opaque"): spec, ADR, docs mkdocs, CI kiểm link/chính tả. Bản hiện hành v1.0.1; v1.0 đổi tên/gộp cấu hình push notification nên client v0.3 cần nâng cấp. |
| Nguồn | [README.md](https://github.com/a2aproject/A2A/blob/5f931b8a25fe66789f987ec4a55fc16ee9fe41ee/README.md) · [LICENSE](https://github.com/a2aproject/A2A/blob/5f931b8a25fe66789f987ec4a55fc16ee9fe41ee/LICENSE) · [CHANGELOG.md](https://github.com/a2aproject/A2A/blob/5f931b8a25fe66789f987ec4a55fc16ee9fe41ee/CHANGELOG.md) · [GOVERNANCE.md](https://github.com/a2aproject/A2A/blob/5f931b8a25fe66789f987ec4a55fc16ee9fe41ee/GOVERNANCE.md) |

<a id="ch-a2a-inspector"></a>

### A2A Inspector

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/a2aproject/a2a-inspector |
| License | Apache-2.0 |
| Phiên bản đã đọc | `832545784c9dd4928af1337e80e5293bc282b6ae` (commit 2026-11-16) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE, go.mod; chưa chạy upstream |
| Bảo trì | active |
| Nhận định | Công cụ debug thủ công cho agent A2A qua JSON-RPC, HTTP+JSON, gRPC; mặc định bind 127.0.0.1 với token theo lần chạy. Lưu ý: host agent tự bật khi có `GOOGLE_API_KEY`/`GEMINI_API_KEY`, trên instance dùng chung thì mọi người dùng chạy trên khóa của operator. Không phải bộ test cho CI. |
| Nguồn | [README.md](https://github.com/a2aproject/a2a-inspector/blob/832545784c9dd4928af1337e80e5293bc282b6ae/README.md) · [LICENSE](https://github.com/a2aproject/a2a-inspector/blob/832545784c9dd4928af1337e80e5293bc282b6ae/LICENSE) · [go.mod](https://github.com/a2aproject/a2a-inspector/blob/832545784c9dd4928af1337e80e5293bc282b6ae/go.mod) |

<a id="ch-a2a-tck"></a>

### A2A TCK

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/a2aproject/a2a-tck |
| License | Apache-2.0 |
| Phiên bản đã đọc | `5e6f37c2d38eb3d7684686243c34d365c83df49b` (commit 2026-11-18) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE, pyproject.toml; chưa chạy upstream |
| Bảo trì | active |
| Nhận định | Bộ test tương thích A2A dựa trên pytest, chạy `run_tck.py --sut-host` vào agent đang chạy, lọc theo transport hoặc mức RFC 2119, xuất báo cáo vào `reports/`. Dùng được làm cổng CI cho bản cài A2A; còn ít người dùng. |
| Nguồn | [README.md](https://github.com/a2aproject/a2a-tck/blob/5e6f37c2d38eb3d7684686243c34d365c83df49b/README.md) · [LICENSE](https://github.com/a2aproject/a2a-tck/blob/5e6f37c2d38eb3d7684686243c34d365c83df49b/LICENSE) · [pyproject.toml](https://github.com/a2aproject/a2a-tck/blob/5e6f37c2d38eb3d7684686243c34d365c83df49b/pyproject.toml) |

<a id="ch-a2ui"></a>

### A2UI

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/a2ui-project/a2ui |
| License | Apache-2.0 |
| Phiên bản đã đọc | `5ff1b05f02d39f969b52a942e78e864ef3ac01fa` (commit 2026-11-20) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE, specification/versions.json, package.json; chưa chạy upstream |
| Bảo trì | active |
| Nhận định | Framework UI sinh động cho agent: UI biểu diễn bằng dữ liệu JSON theo schema thay vì mã, renderer gốc cho web/Flutter/SwiftUI/Compose, SDK agent nhiều ngôn ngữ và thư mục `conformance/`. Ranh giới an toàn dựa vào catalog component phía host; host vẫn phải lọc hành động gọi tool. |
| Nguồn | [README.md](https://github.com/a2ui-project/a2ui/blob/5ff1b05f02d39f969b52a942e78e864ef3ac01fa/README.md) · [LICENSE](https://github.com/a2ui-project/a2ui/blob/5ff1b05f02d39f969b52a942e78e864ef3ac01fa/LICENSE) · [versions.json](https://github.com/a2ui-project/a2ui/blob/5ff1b05f02d39f969b52a942e78e864ef3ac01fa/specification/versions.json) · [package.json](https://github.com/a2ui-project/a2ui/blob/5ff1b05f02d39f969b52a942e78e864ef3ac01fa/package.json) |

<a id="ch-agent-client-protocol"></a>

### Agent Client Protocol

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/agentclientprotocol/agent-client-protocol |
| License | Apache-2.0 |
| Phiên bản đã đọc | `5bba73da3d72eb83ef0ace43ca7346d0864a2446` (commit 2026-11-23) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE, MAINTAINERS.md, package.json; chưa chạy upstream |
| Bảo trì | active |
| Nhận định | Repo chứa crate Rust `agent-client-protocol-schema` và JSON Schema của ACP; SDK chính thức Kotlin, Java, Python, Rust, TypeScript ở repo riêng. README nhấn mạnh tương thích wire xác định bằng `protocolVersion` trong `initialize`, không theo số phiên bản crate/schema. |
| Nguồn | [README.md](https://github.com/agentclientprotocol/agent-client-protocol/blob/5bba73da3d72eb83ef0ace43ca7346d0864a2446/README.md) · [LICENSE](https://github.com/agentclientprotocol/agent-client-protocol/blob/5bba73da3d72eb83ef0ace43ca7346d0864a2446/LICENSE) · [MAINTAINERS.md](https://github.com/agentclientprotocol/agent-client-protocol/blob/5bba73da3d72eb83ef0ace43ca7346d0864a2446/MAINTAINERS.md) · [package.json](https://github.com/agentclientprotocol/agent-client-protocol/blob/5bba73da3d72eb83ef0ace43ca7346d0864a2446/package.json) |

<a id="ch-agent-skills-spec"></a>

### Agent Skills spec

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://agentskills.io (repo nguồn: https://github.com/agentskills/agentskills) |
| License | Chuẩn mở; trang không nêu license cụ thể |
| Phiên bản đã đọc | Trang web tại ngày 2026-11-23 (không có SHA) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc trang chủ và /specification; chưa chạy upstream |
| Bảo trì | active (có Discord chính thức, trang cập nhật) |
| Nhận định | Một skill là thư mục có `SKILL.md` (YAML frontmatter + Markdown) cùng `scripts/`, `references/`, `assets/` tùy chọn; agent nạp theo ba bước discovery → activation → execution để tiết kiệm context. Trang ghi chuẩn do Anthropic phát triển rồi mở; mốc 18/12/2025 **(chưa xác minh)** trên trang. `allowed-tools` vẫn là trường thử nghiệm. |
| Nguồn | [Trang chủ](https://agentskills.io/home) · [Specification](https://agentskills.io/specification) |

<a id="ch-agents-md"></a>

### AGENTS.md

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/agentsmd/agents.md |
| License | MIT |
| Phiên bản đã đọc | `d001185d792eb6402a58e4cbef1c228b309ec25d` (commit 2026-09-10) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE, package.json, components/AboutSection.tsx; chưa chạy upstream |
| Bảo trì | active |
| Nhận định | Repo của định dạng AGENTS.md và trang Next.js agents.md: chỉ là quy ước một file Markdown hướng dẫn agent, không có schema bắt buộc hay công cụ kiểm. Con số 60k dự án dùng là lời trang **(chưa xác minh)**. Commit cuối 10/9/2026, ít thay đổi vì định dạng đơn giản. |
| Nguồn | [README.md](https://github.com/agentsmd/agents.md/blob/d001185d792eb6402a58e4cbef1c228b309ec25d/README.md) · [LICENSE](https://github.com/agentsmd/agents.md/blob/d001185d792eb6402a58e4cbef1c228b309ec25d/LICENSE) · [package.json](https://github.com/agentsmd/agents.md/blob/d001185d792eb6402a58e4cbef1c228b309ec25d/package.json) · [AboutSection.tsx](https://github.com/agentsmd/agents.md/blob/d001185d792eb6402a58e4cbef1c228b309ec25d/components/AboutSection.tsx) |

<a id="ch-awesome-agent-skills"></a>

### awesome-agent-skills

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/VoltAgent/awesome-agent-skills |
| License | MIT (catalog cũ để trống) |
| Phiên bản đã đọc | `20c57162c790d59d35e47c1538dc534c5c59e60d` (commit 2026-11-15) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE; chưa chạy upstream |
| Bảo trì | active |
| Nhận định | Danh sách skill chính chủ và cộng đồng, chia theo tổ chức phát hành, có bảng đường dẫn cài cho nhiều agent. Không có CI kiểm link hay nội dung; nhãn "hand-picked" là tuyên bố của người duy trì **(chưa xác minh)**. Skill bên thứ ba có thể kèm script, cần đọc trước khi cài. |
| Nguồn | [README.md](https://github.com/VoltAgent/awesome-agent-skills/blob/20c57162c790d59d35e47c1538dc534c5c59e60d/README.md) · [LICENSE](https://github.com/VoltAgent/awesome-agent-skills/blob/20c57162c790d59d35e47c1538dc534c5c59e60d/LICENSE) |

<a id="ch-awesome-mcp-servers-punkpeye"></a>

### awesome-mcp-servers (punkpeye)

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/punkpeye/awesome-mcp-servers |
| License | MIT |
| Phiên bản đã đọc | `9dbadb400a592289ec0f0dd97ee44632840c3c2b` (commit 2026-11-22) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE, .github/workflows/check-glama.yml; chưa chạy upstream |
| Bảo trì | active |
| Nhận định | Danh sách MCP server lớn nhất (khoảng 5.000 dòng mục, 8 bản dịch). Cổng PR duy nhất là badge điểm của Glama (dịch vụ liên quan tới người duy trì), nên danh sách nghiêng về khối lượng hơn chọn lọc; nhãn chính chủ không được xác minh. |
| Nguồn | [README.md](https://github.com/punkpeye/awesome-mcp-servers/blob/9dbadb400a592289ec0f0dd97ee44632840c3c2b/README.md) · [LICENSE](https://github.com/punkpeye/awesome-mcp-servers/blob/9dbadb400a592289ec0f0dd97ee44632840c3c2b/LICENSE) · [check-glama.yml](https://github.com/punkpeye/awesome-mcp-servers/blob/9dbadb400a592289ec0f0dd97ee44632840c3c2b/.github/workflows/check-glama.yml) |

<a id="ch-cisco-mcp-scanner"></a>

### Cisco MCP Scanner

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/cisco-ai-defense/mcp-scanner |
| License | Apache-2.0 |
| Phiên bản đã đọc | `8c3cae130a12afb7b3abfe9c8a4e2a5e2b103735` (commit 2026-11-19) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE, pyproject.toml; chưa chạy upstream |
| Bảo trì | active |
| Nhận định | Quét tool/prompt/resource của MCP server bằng nhiều engine dùng riêng hoặc kết hợp, có chế độ tĩnh cho CI và REST API. Chú ý: chế độ `stdio` chạy chính server cần quét trên máy, VirusTotal và AI Defense gửi dữ liệu ra dịch vụ ngoài khi bật. Độ phủ phát hiện là tuyên bố của Cisco **(chưa xác minh)**. |
| Nguồn | [README.md](https://github.com/cisco-ai-defense/mcp-scanner/blob/8c3cae130a12afb7b3abfe9c8a4e2a5e2b103735/README.md) · [LICENSE](https://github.com/cisco-ai-defense/mcp-scanner/blob/8c3cae130a12afb7b3abfe9c8a4e2a5e2b103735/LICENSE) · [pyproject.toml](https://github.com/cisco-ai-defense/mcp-scanner/blob/8c3cae130a12afb7b3abfe9c8a4e2a5e2b103735/pyproject.toml) |

<a id="ch-fastmcp"></a>

### FastMCP

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/prefecthq/fastmcp |
| License | Apache-2.0 |
| Phiên bản đã đọc | `33c7401f7e4fa716b1d5731e9f6105d711c3ac43` (commit 2026-11-23) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE, pyproject.toml; chưa chạy upstream |
| Bảo trì | active |
| Nhận định | Framework Python sinh schema và validation từ hàm, quản lý transport, auth, vòng đời; FastMCP 1.0 đã nhập vào SDK Python chính thức năm 2024. Các con số "1 triệu lượt tải/ngày", "70% MCP server" là tuyên bố của README **(chưa xác minh)**. |
| Nguồn | [README.md](https://github.com/prefecthq/fastmcp/blob/33c7401f7e4fa716b1d5731e9f6105d711c3ac43/README.md) · [LICENSE](https://github.com/prefecthq/fastmcp/blob/33c7401f7e4fa716b1d5731e9f6105d711c3ac43/LICENSE) · [pyproject.toml](https://github.com/prefecthq/fastmcp/blob/33c7401f7e4fa716b1d5731e9f6105d711c3ac43/pyproject.toml) |

<a id="ch-github-mcp-server"></a>

### GitHub MCP Server

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/github/github-mcp-server |
| License | MIT |
| Phiên bản đã đọc | `9a72d8d38fec18c207cd924b33aa0eb3e186252c` (commit 2026-11-20) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE, go.mod, server.json; chưa chạy upstream |
| Bảo trì | active |
| Nhận định | MCP server chính chủ (Go) cho repo, issue, PR, Actions, bảo mật; có bản hosted và bản local, giới hạn bằng `--toolsets`, read-only, exclude-tools. Lockdown chỉ giảm prompt injection từ nội dung công khai, quyền thật vẫn do token quyết định. |
| Nguồn | [README.md](https://github.com/github/github-mcp-server/blob/9a72d8d38fec18c207cd924b33aa0eb3e186252c/README.md) · [LICENSE](https://github.com/github/github-mcp-server/blob/9a72d8d38fec18c207cd924b33aa0eb3e186252c/LICENSE) · [go.mod](https://github.com/github/github-mcp-server/blob/9a72d8d38fec18c207cd924b33aa0eb3e186252c/go.mod) · [server.json](https://github.com/github/github-mcp-server/blob/9a72d8d38fec18c207cd924b33aa0eb3e186252c/server.json) |

<a id="ch-mcp-apps-ext-apps"></a>

### MCP Apps (ext-apps)

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/modelcontextprotocol/ext-apps |
| License | MIT → Apache-2.0 (đang chuyển; tài liệu CC-BY-4.0); package.json ghi MIT. Khác catalog cũ (Apache-2.0) |
| Phiên bản đã đọc | `ea3e9d0e624a20bc1c51310292f09d9b8ed17161` (commit 2026-11-10) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE, package.json; chưa chạy upstream |
| Bảo trì | active |
| Nhận định | Extension UI chính thức của MCP: spec 2026-01-26 (và bản draft) cùng SDK để tool trả UI tương tác hiển thị trong host. Repo không có host được hỗ trợ ngoài ví dụ `basic-host`; MCP-UI là framework client hiện thực chuẩn này, nên ghi "thay mcp-ui" trong catalog cũ là không chính xác. |
| Nguồn | [README.md](https://github.com/modelcontextprotocol/ext-apps/blob/ea3e9d0e624a20bc1c51310292f09d9b8ed17161/README.md) · [LICENSE](https://github.com/modelcontextprotocol/ext-apps/blob/ea3e9d0e624a20bc1c51310292f09d9b8ed17161/LICENSE) · [package.json](https://github.com/modelcontextprotocol/ext-apps/blob/ea3e9d0e624a20bc1c51310292f09d9b8ed17161/package.json) |

<a id="ch-mcp-bundles-mcpb"></a>

### MCP Bundles (MCPB)

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/modelcontextprotocol/mcpb |
| License | MIT → Apache-2.0 (đang chuyển; tài liệu CC-BY-4.0) |
| Phiên bản đã đọc | `70fe3b34cd6dff1b3bba046638edc72a6467a4fb` (commit 2026-04-22) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE, CLI.md, package.json; chưa chạy upstream |
| Bảo trì | low-activity (main đứng từ 2026-04-22) |
| Nhận định | Định dạng zip `.mcpb` chứa MCP server cục bộ và `manifest.json`, kèm CLI đóng gói, ký và mã nạp bundle mà Claude desktop dùng. Main đứng yên 7 tháng tính tới ngày kiểm. |
| Nguồn | [README.md](https://github.com/modelcontextprotocol/mcpb/blob/70fe3b34cd6dff1b3bba046638edc72a6467a4fb/README.md) · [LICENSE](https://github.com/modelcontextprotocol/mcpb/blob/70fe3b34cd6dff1b3bba046638edc72a6467a4fb/LICENSE) · [CLI.md](https://github.com/modelcontextprotocol/mcpb/blob/70fe3b34cd6dff1b3bba046638edc72a6467a4fb/CLI.md) · [package.json](https://github.com/modelcontextprotocol/mcpb/blob/70fe3b34cd6dff1b3bba046638edc72a6467a4fb/package.json) |

<a id="ch-mcp-inspector"></a>

### MCP Inspector

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/modelcontextprotocol/inspector |
| License | MIT → Apache-2.0 (đang chuyển; tài liệu CC-BY-4.0) |
| Phiên bản đã đọc | `eb54b447e5377a7a18acaea9602fced5cb4c5b9f` (commit 2026-11-18) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE, package.json; chưa chạy upstream |
| Bảo trì | active |
| Nhận định | Công cụ kiểm MCP server qua web UI, CLI (hợp cho CI), TUI. Rủi ro thực tế: trên Linux headless/container token OAuth và biến `env:` của stdio có thể nằm plaintext trên đĩa nếu không cấu hình khóa. |
| Nguồn | [README.md](https://github.com/modelcontextprotocol/inspector/blob/eb54b447e5377a7a18acaea9602fced5cb4c5b9f/README.md) · [LICENSE](https://github.com/modelcontextprotocol/inspector/blob/eb54b447e5377a7a18acaea9602fced5cb4c5b9f/LICENSE) · [package.json](https://github.com/modelcontextprotocol/inspector/blob/eb54b447e5377a7a18acaea9602fced5cb4c5b9f/package.json) |

<a id="ch-mcp-registry"></a>

### MCP Registry

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/modelcontextprotocol/registry |
| License | MIT → Apache-2.0 (đang chuyển; tài liệu CC-BY-4.0). Khác catalog cũ (Apache-2.0) |
| Phiên bản đã đọc | `9b093df6b9f196875626dac9f6060b03c732e799` (commit 2026-11-23) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE, go.mod; chưa chạy upstream |
| Bảo trì | active |
| Nhận định | Registry chính thức (Go, PostgreSQL) liệt kê MCP server như một app store, do working group nhiều công ty duy trì. Vẫn là preview nên có thể breaking change hoặc reset dữ liệu; registry chỉ lưu metadata, không kiểm an toàn server. |
| Nguồn | [README.md](https://github.com/modelcontextprotocol/registry/blob/9b093df6b9f196875626dac9f6060b03c732e799/README.md) · [LICENSE](https://github.com/modelcontextprotocol/registry/blob/9b093df6b9f196875626dac9f6060b03c732e799/LICENSE) · [go.mod](https://github.com/modelcontextprotocol/registry/blob/9b093df6b9f196875626dac9f6060b03c732e799/go.mod) |

<a id="ch-mcp-servers-reference"></a>

### MCP servers (reference)

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/modelcontextprotocol/servers |
| License | MIT → Apache-2.0 (đang chuyển; tài liệu CC-BY-4.0). Khác catalog cũ (MIT) |
| Phiên bản đã đọc | `c799c8552b0f27b7a33a7b9233773da144dddcf5` (commit 2026-11-18) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE; chưa chạy upstream |
| Bảo trì | active |
| Nhận định | Bảy server mẫu để minh họa SDK, README tự cảnh báo không dành cho production; các server cũ đã chuyển sang `servers-archived`. Danh sách server cộng đồng nay nằm ở Registry. |
| Nguồn | [README.md](https://github.com/modelcontextprotocol/servers/blob/c799c8552b0f27b7a33a7b9233773da144dddcf5/README.md) · [LICENSE](https://github.com/modelcontextprotocol/servers/blob/c799c8552b0f27b7a33a7b9233773da144dddcf5/LICENSE) |

<a id="ch-mcp-specification"></a>

### MCP Specification

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/modelcontextprotocol/modelcontextprotocol |
| License | MIT → Apache-2.0 (đang chuyển; tài liệu CC-BY-4.0) |
| Phiên bản đã đọc | `1c5f400671ba9ac6d558de907b815be4d2c37548` (commit 2026-11-23) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE, AI_POLICY.md; chưa chạy upstream |
| Bảo trì | active |
| Nhận định | Nguồn của spec, schema TypeScript/JSON và tài liệu modelcontextprotocol.io. Chỉ thành viên tổ chức được mở PR, thay đổi spec đi qua working group và SEP. Mâu thuẫn nhỏ: README ghi MIT, LICENSE ghi chuyển sang Apache-2.0. |
| Nguồn | [README.md](https://github.com/modelcontextprotocol/modelcontextprotocol/blob/1c5f400671ba9ac6d558de907b815be4d2c37548/README.md) · [LICENSE](https://github.com/modelcontextprotocol/modelcontextprotocol/blob/1c5f400671ba9ac6d558de907b815be4d2c37548/LICENSE) · [AI_POLICY.md](https://github.com/modelcontextprotocol/modelcontextprotocol/blob/1c5f400671ba9ac6d558de907b815be4d2c37548/AI_POLICY.md) |

<a id="ch-mcp-typescript-sdk"></a>

### MCP TypeScript SDK

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/modelcontextprotocol/typescript-sdk |
| License | MIT → Apache-2.0 (đang chuyển; tài liệu CC-BY-4.0) |
| Phiên bản đã đọc | `5ee54ee30ddc00a914a3d981880f87fdce0e6246` (commit 2026-11-18) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE, packages/server/package.json; chưa chạy upstream |
| Bảo trì | active |
| Nhận định | SDK chính thức chạy trên Node, Bun, Deno, có middleware Express/Fastify/Hono và codemod nâng cấp v1 → v2. Người ngoài chỉ được mở một PR cùng lúc. |
| Nguồn | [README.md](https://github.com/modelcontextprotocol/typescript-sdk/blob/5ee54ee30ddc00a914a3d981880f87fdce0e6246/README.md) · [LICENSE](https://github.com/modelcontextprotocol/typescript-sdk/blob/5ee54ee30ddc00a914a3d981880f87fdce0e6246/LICENSE) · [package.json](https://github.com/modelcontextprotocol/typescript-sdk/blob/5ee54ee30ddc00a914a3d981880f87fdce0e6246/packages/server/package.json) |

<a id="ch-mcp-use"></a>

### mcp-use

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/mcp-use/mcp-use |
| License | MIT |
| Phiên bản đã đọc | `8ff4b865e0e5712c66d5077e93392807daca9354` (commit 2026-11-19) |
| Kiểm chứng | 2026-11-23; code-read; đã đọc README.md, LICENSE, libraries/python/mcp_use/telemetry/telemetry.py, libraries/python/mcp_use/telemetry/events.py, libraries/typescript/packages/client/src/telemetry/telemetry.ts, libraries/typescript/packages/client/src/telemetry/events.ts, .github/workflows/close-python-prs.yml; chưa chạy upstream |
| Bảo trì | active (TypeScript); Python chỉ nhận sửa lỗi có tái hiện |
| Nhận định | Framework TypeScript dựng MCP server, MCP Apps, inspector và agent client; thư viện Python vẫn phát hành nhưng ưu tiên thấp. Rủi ro dữ liệu: agent Python gửi nội dung hội thoại lên PostHog nếu không tắt biến môi trường. |
| Nguồn | [README.md](https://github.com/mcp-use/mcp-use/blob/8ff4b865e0e5712c66d5077e93392807daca9354/README.md) · [LICENSE](https://github.com/mcp-use/mcp-use/blob/8ff4b865e0e5712c66d5077e93392807daca9354/LICENSE) · [telemetry.py](https://github.com/mcp-use/mcp-use/blob/8ff4b865e0e5712c66d5077e93392807daca9354/libraries/python/mcp_use/telemetry/telemetry.py) · [events.py](https://github.com/mcp-use/mcp-use/blob/8ff4b865e0e5712c66d5077e93392807daca9354/libraries/python/mcp_use/telemetry/events.py) · [telemetry.ts](https://github.com/mcp-use/mcp-use/blob/8ff4b865e0e5712c66d5077e93392807daca9354/libraries/typescript/packages/client/src/telemetry/telemetry.ts) · [events.ts](https://github.com/mcp-use/mcp-use/blob/8ff4b865e0e5712c66d5077e93392807daca9354/libraries/typescript/packages/client/src/telemetry/events.ts) · [close-python-prs.yml](https://github.com/mcp-use/mcp-use/blob/8ff4b865e0e5712c66d5077e93392807daca9354/.github/workflows/close-python-prs.yml) |

<a id="ch-mcpjam-inspector"></a>

### MCPJam Inspector

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/MCPJam/inspector |
| License | Apache-2.0; phần eval (`mcpjam-inspector/server/services`, `server/evals`) theo MCPJam EE License; LICENSE gốc vẫn ghi đường dẫn cũ `/server/services` |
| Phiên bản đã đọc | `0ec2456f1ebd5dff92a212f5faaead6224196551` (commit 2026-11-23) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE, mcpjam-inspector/server/evals/LICENSE, mcpjam-inspector/package.json, mcpjam-inspector/docs/server-error-reporting.md; chưa chạy upstream |
| Bảo trì | active |
| Nhận định | Inspector và nền tảng eval cho MCP server: playground đa client, OAuth debugger, CLI cho CI, bản hosted app.mcpjam.com. Rủi ro license: phần eval theo EE License và đường dẫn carve-out trong LICENSE đã lệch sau khi tái cấu trúc repo. Lời "bản browser vẫn gửi usage event khi DO_NOT_TRACK=1" từ lần kiểm trước chưa đọc lại lần này **(chưa xác minh)**. |
| Nguồn | [README.md](https://github.com/MCPJam/inspector/blob/0ec2456f1ebd5dff92a212f5faaead6224196551/README.md) · [LICENSE](https://github.com/MCPJam/inspector/blob/0ec2456f1ebd5dff92a212f5faaead6224196551/LICENSE) · [LICENSE](https://github.com/MCPJam/inspector/blob/0ec2456f1ebd5dff92a212f5faaead6224196551/mcpjam-inspector/server/evals/LICENSE) · [package.json](https://github.com/MCPJam/inspector/blob/0ec2456f1ebd5dff92a212f5faaead6224196551/mcpjam-inspector/package.json) · [server-error-reporting.md](https://github.com/MCPJam/inspector/blob/0ec2456f1ebd5dff92a212f5faaead6224196551/mcpjam-inspector/docs/server-error-reporting.md) |

<a id="ch-official-mcp-servers-voltagent"></a>

### official-mcp-servers (VoltAgent)

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/VoltAgent/official-mcp-servers |
| License | MIT |
| Phiên bản đã đọc | `e71f99b3e8c5283ca729c9716cd0b4cbbb7098e3` (commit 2026-11-19) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE; chưa chạy upstream |
| Bảo trì | active |
| Nhận định | Danh mục MCP server chính chủ chia theo lĩnh vực, ưu tiên server của chính hãng sản phẩm, link docs của nhà cung cấp khi không có repo. Không có kiểm tự động link hay trạng thái archive, nên mục có thể lỗi thời; "chỉ server tin được" là tuyên bố của người duy trì **(chưa xác minh)**. |
| Nguồn | [README.md](https://github.com/VoltAgent/official-mcp-servers/blob/e71f99b3e8c5283ca729c9716cd0b4cbbb7098e3/README.md) · [LICENSE](https://github.com/VoltAgent/official-mcp-servers/blob/e71f99b3e8c5283ca729c9716cd0b4cbbb7098e3/LICENSE) |

<a id="nt-2026-11-23"></a>

## Nâng trần theo khoảng trống — 23/11/2026

Phần này có các hồ sơ mới của đợt nâng trần: mười trinh sát tìm trên internet và GitHub những mảng mà chuyên mục còn thiếu hoặc chỉ có hồ sơ cũ, rồi mỗi repo được clone nông tại một commit cố định, đọc LICENSE, README, ít nhất một file triển khai thật và CI nếu có; không cài hay chạy mã upstream. Mô tả của trinh sát nhiều chỗ sai so với mã thật, và các chỗ đó được sửa ngay trong từng hồ sơ. Số sao lấy sau bằng GitHub search API nên có thể để trống.

<a id="nt-archestra"></a>

### Archestra

| Thuộc tính | Giá trị |
|---|---|
| Repo | https://github.com/archestra-ai/archestra |
| License | LICENSE.md điều phối song license: AGPL-3.0-only (mặc định, LICENSE_AGPL) và LicenseRef-Archestra-Enterprise (LICENSE_ENTERPRISE) cho file/vùng đánh dấu; Dagger SDK vendor MIT |
| Phiên bản đã đọc | `47d935ff4f6435d3f6a843b036a6f786cbc27d97` (commit 2026-11-23) |
| Kiểm chứng | 2026-11-23; code-read; đã đọc README, LICENSE.md, LICENSE_ENTERPRISE, guardrails/index.md, openappa-architecture.md, enterprise-tier.ts, guardrails-policy.ts, config.ts và on-pull-requests.yml; chưa chạy upstream |
| Khoảng trống lấp | MCP gateway/registry/bảo mật: gateway kèm guardrail theo phiên chống lethal trifecta |
| Cơ chế đáng học | - Mỗi phiên qua LLM proxy mang nhãn (trust, audience) chỉ chặt thêm; mỗi tool khai báo `delta` và `requires`, gọi không đủ nhãn thì bị chặn kèm các remedy: duyệt người, sanitizer, `attest-schema`, chấp nhận hạ nhãn (docs/pages/agents/guardrails/index.md).<br>- Danh tính thực thi lấy từ metadata client, không từ tham số do model viết; kết quả tool ngoài coi là không tin cậy (docs/openappa-architecture.md).<br>- Chính sách lưu theo revision trong PostgreSQL với kiểm expectedRevision và khóa giao dịch (models/guardrails-policy.ts).<br>- MCP gateway dùng OAuth và On-Behalf-Of để tool chạy với danh nghĩa người dùng (README, chưa đọc mã triển khai phần này). |
| Tiêu chí và cách kiểm | Có workflow on-pull-requests.yml với license-check (`pnpm license-check --ci`), test đơn vị backend, e2e, openappa-native-tests, helm lint; tôi chỉ đọc danh sách job và vài bước, chưa đọc từng job. Hiệu quả chặn của guardrail chưa tự kiểm. |
| Giới hạn và rủi ro | License song song: LICENSE.md quy định thứ tự (header SPDX, vùng snippet, đường dẫn `ee/` hoặc `*.ee.*`, mặc định AGPL); tôi đếm 483 file trong platform/backend/src mang header Enterprise. AGPL có điều khoản mạng; Enterprise cấm sao chép, phân phối, và điều khoản Small Team Clause dưới 30 người dùng toàn công ty (chưa đọc hết điều khoản). Guardrail mặc định tắt (`guardrails_deployment.enabled`) và ghi beta. Analytics (PostHog) và báo lỗi (Sentry) mặc định bật trên image production, tắt bằng `ARCHESTRA_ANALYTICS=disabled` hoặc khi kích hoạt license Enterprise (config.ts, docs cấu hình). Chạy cần mount docker.sock trong quickstart. |
| So với | agentgateway, cisco-mcp-scanner, agent-scan, portkey-gateway |
| Nguồn | [README.md](https://github.com/archestra-ai/archestra/blob/47d935ff4f6435d3f6a843b036a6f786cbc27d97/README.md) · [LICENSE.md](https://github.com/archestra-ai/archestra/blob/47d935ff4f6435d3f6a843b036a6f786cbc27d97/LICENSE.md) · [LICENSE_ENTERPRISE](https://github.com/archestra-ai/archestra/blob/47d935ff4f6435d3f6a843b036a6f786cbc27d97/LICENSE_ENTERPRISE) · [openappa-architecture.md](https://github.com/archestra-ai/archestra/blob/47d935ff4f6435d3f6a843b036a6f786cbc27d97/docs/openappa-architecture.md) · [index.md](https://github.com/archestra-ai/archestra/blob/47d935ff4f6435d3f6a843b036a6f786cbc27d97/docs/pages/agents/guardrails/index.md) · [enterprise-tier.ts](https://github.com/archestra-ai/archestra/blob/47d935ff4f6435d3f6a843b036a6f786cbc27d97/platform/backend/src/enterprise-tier.ts) · [guardrails-policy.ts](https://github.com/archestra-ai/archestra/blob/47d935ff4f6435d3f6a843b036a6f786cbc27d97/platform/backend/src/models/guardrails-policy.ts) · [config.ts](https://github.com/archestra-ai/archestra/blob/47d935ff4f6435d3f6a843b036a6f786cbc27d97/platform/backend/src/config.ts) · [on-pull-requests.yml](https://github.com/archestra-ai/archestra/blob/47d935ff4f6435d3f6a843b036a6f786cbc27d97/.github/workflows/on-pull-requests.yml) |

<a id="nt-mcphub"></a>

### MCPHub

| Thuộc tính | Giá trị |
|---|---|
| Repo | https://github.com/samanhappy/mcphub |
| License | Apache-2.0 (LICENSE) |
| Phiên bản đã đọc | `73217631986397af317b09a61985f4c685155a85` (commit 2026-11-23) |
| Kiểm chứng | 2026-11-23; code-read; đã đọc README, toolPolicy.ts, toolPolicyService.ts, authorizationService.ts, mcpTools.ts (callsite), User.ts và ci.yml; chưa chạy upstream |
| Khoảng trống lấp | MCP gateway/registry/bảo mật: một endpoint cho nhiều MCP server, kèm phân quyền theo người và theo khóa |
| Cơ chế đáng học | - `evaluateToolPolicy`: deny khớp thì chặn; nếu có rule allow áp dụng cho chủ thể mà không rule nào khớp thì chặn; nếu không có rule áp dụng thì cho phép (src/utils/toolPolicy.ts).<br>- Callsite thật: `mcpTools.ts` gọi `getToolPolicy` rồi `policy.authorize(serverName, toolName)` khi gọi tool; smart routing và OpenAPI cũng lọc theo cùng policy (grep callsite).<br>- Quyền dùng server (discover, invoke) tách khỏi quyền đọc cấu hình, dùng chung luật visibility (authorizationService.ts).<br>- Mật khẩu admin: lấy từ `ADMIN_PASSWORD`, nếu không thì sinh ngẫu nhiên và in log; chỉ ở NODE_ENV=development mới là `admin123` (src/models/User.ts). |
| Tiêu chí và cách kiểm | ci.yml chạy `pnpm docs:validate`, lint, build backend, typecheck frontend và `pnpm test:ci` (đã đọc); có test toolCallGuard. Tôi chưa đọc nội dung các test đó. |
| Giới hạn và rủi ro | Mặc định mở: người dùng chưa có luật thì mọi tool được phép (toolPolicy.ts); phải tự viết luật deny/allow. Phiên bản package ghi `dev`. Có chế độ hosted và client tới dịch vụ ngoài (cloudService, market) nhưng tôi chưa đọc xem dữ liệu nào rời máy. Rủi ro chung của gateway gộp: một token mở nhiều server, cần kiểm scope. README mô tả smart routing dùng embedding (chưa xác minh nhà cung cấp embedding mặc định). |
| So với | agentgateway, archestra, fastmcp, cisco-mcp-scanner |
| Nguồn | [README.md](https://github.com/samanhappy/mcphub/blob/73217631986397af317b09a61985f4c685155a85/README.md) · [LICENSE](https://github.com/samanhappy/mcphub/blob/73217631986397af317b09a61985f4c685155a85/LICENSE) · [toolPolicy.ts](https://github.com/samanhappy/mcphub/blob/73217631986397af317b09a61985f4c685155a85/src/utils/toolPolicy.ts) · [toolPolicyService.ts](https://github.com/samanhappy/mcphub/blob/73217631986397af317b09a61985f4c685155a85/src/services/toolPolicyService.ts) · [authorizationService.ts](https://github.com/samanhappy/mcphub/blob/73217631986397af317b09a61985f4c685155a85/src/services/authorizationService.ts) · [mcpTools.ts](https://github.com/samanhappy/mcphub/blob/73217631986397af317b09a61985f4c685155a85/src/services/mcpTools.ts) · [User.ts](https://github.com/samanhappy/mcphub/blob/73217631986397af317b09a61985f4c685155a85/src/models/User.ts) · [ci.yml](https://github.com/samanhappy/mcphub/blob/73217631986397af317b09a61985f4c685155a85/.github/workflows/ci.yml) |

<a id="nt-a2a-python"></a>

### A2A Python SDK

| Thuộc tính | Giá trị |
|---|---|
| Repo | https://github.com/a2aproject/a2a-python |
| License | Apache-2.0 (LICENSE) |
| Phiên bản đã đọc | `eaa71bcaffaae8b6cb3606b797ece4f7ae0dd554` (commit 2026-11-23) |
| Kiểm chứng | 2026-11-23; code-read; đã đọc README, agent_executor.py, auth/user.py, pyproject.toml, run-tck.yaml và unit-tests.yml; chưa chạy upstream |
| Khoảng trống lấp | A2A và interop: SDK phía triển khai còn thiếu cạnh a2a, a2a-tck, a2a-inspector đã có |
| Cơ chế đáng học | - `AgentExecutor.execute/cancel`: framework bảo đảm không gọi đồng thời cho một request, exception thành TASK_STATE_ERROR, executor phát TaskStatusUpdateEvent tới trạng thái cuối hoặc bị gián đoạn (agent_execution/agent_executor.py).<br>- Hai mô hình auth-required: trong băng (execute trả về, framework gọi lại khi có phản hồi) và ngoài băng (giữ execute chờ nhà cung cấp xác thực) (agent_executor.py).<br>- Tách transport, task store (in-memory, SQL), push notification store; compat 0.3 nằm trong `src/a2a/compat`.<br>- `a2a.auth.user.User` trừu tượng (is_authenticated, user_name) cho tích hợp middleware của ứng dụng. |
| Tiêu chí và cách kiểm | run-tck.yaml chạy a2a-tck bản 0.3.0.beta3 trên Python 3.10 và 3.13 với SUT cục bộ; unit-tests.yml chạy pytest kèm `--cov-fail-under=88` (đã mở đọc). Chuẩn do TCK quyết định, tôi chưa chạy. |
| Giới hạn và rủi ro | Cần chọn đúng phiên bản: README nói spec 1.0 và có hướng dẫn nâng từ 0.3 lên 1.0, các mẫu a2a-samples ghim a2a-sdk từ >=0.3.0 đến >=1.1.0 nên không đồng đều. TCK ghim beta, không phải bản chính thức (theo tên biến). Việc ủy quyền theo skill hay theo task không có trong SDK. License Apache-2.0. |
| So với | a2a (chuẩn), a2a-tck, a2a-inspector, fastmcp (SDK phía MCP) |
| Nguồn | [README.md](https://github.com/a2aproject/a2a-python/blob/eaa71bcaffaae8b6cb3606b797ece4f7ae0dd554/README.md) · [LICENSE](https://github.com/a2aproject/a2a-python/blob/eaa71bcaffaae8b6cb3606b797ece4f7ae0dd554/LICENSE) · [agent_executor.py](https://github.com/a2aproject/a2a-python/blob/eaa71bcaffaae8b6cb3606b797ece4f7ae0dd554/src/a2a/server/agent_execution/agent_executor.py) · [user.py](https://github.com/a2aproject/a2a-python/blob/eaa71bcaffaae8b6cb3606b797ece4f7ae0dd554/src/a2a/auth/user.py) · [pyproject.toml](https://github.com/a2aproject/a2a-python/blob/eaa71bcaffaae8b6cb3606b797ece4f7ae0dd554/pyproject.toml) · [run-tck.yaml](https://github.com/a2aproject/a2a-python/blob/eaa71bcaffaae8b6cb3606b797ece4f7ae0dd554/.github/workflows/run-tck.yaml) · [unit-tests.yml](https://github.com/a2aproject/a2a-python/blob/eaa71bcaffaae8b6cb3606b797ece4f7ae0dd554/.github/workflows/unit-tests.yml) |

<a id="nt-a2a-samples"></a>

### A2A Samples

| Thuộc tính | Giá trị |
|---|---|
| Repo | https://github.com/a2aproject/a2a-samples |
| License | Apache-2.0 (LICENSE) |
| Phiên bản đã đọc | `b7a2a689ff3a86e756386aa488e3f7b02a355590` (commit 2026-11-23) |
| Kiểm chứng | 2026-11-23; code-read; đã đọc README, sign_and_verify_agent_card/`__main__`.py, headless_agent_auth/oauth2_middleware.py, pyproject.toml và linter.yaml; chưa chạy upstream |
| Khoảng trống lấp | A2A và interop: ví dụ chạy được nhiều framework và mẫu bảo mật cho agent card |
| Cơ chế đáng học | - Ký agent card: sinh cặp khóa EC P-256, xuất `public_keys.json`, dùng `create_agent_card_signer` của SDK (sign_and_verify_agent_card/`__main__`.py).<br>- Middleware Starlette đọc `security` trong AgentCard, lấy scope của yêu cầu đầu tiên, xác thực bearer token qua Auth0 (`verify_access_token`, domain và audience từ biến môi trường) (headless_agent_auth/oauth2_middleware.py).<br>- Tách extension A2A thành thư mục riêng: agp, secure-passport (có test_secure_passport.py), timestamp, traceability. |
| Tiêu chí và cách kiểm | Workflow duy nhất là linter.yaml (Super-Linter slim, nhiều linter Python tắt, chỉ lint file đổi). Không có test chung cho mẫu; chỉ vài extension có test riêng (agp, secure-passport; chưa đọc). |
| Giới hạn và rủi ro | Mã mẫu, không phải thư viện: sample auth tự ghi chú chỉ minh họa (scheme trong `security_schemes` không được xác thực), middleware cho qua khi agent card không khai security. Ghim a2a-sdk không đồng đều (>=0.3.0, >=1.0.0a1, >=1.1.0), nên nhiều mẫu có thể chưa chạy với SDK 1.x (chưa kiểm). Khóa ký sinh mới mỗi lần chạy, chỉ phù hợp demo. |
| So với | a2a-python (SDK), a2a-inspector, a2a-tck |
| Nguồn | [README.md](https://github.com/a2aproject/a2a-samples/blob/b7a2a689ff3a86e756386aa488e3f7b02a355590/README.md) · [LICENSE](https://github.com/a2aproject/a2a-samples/blob/b7a2a689ff3a86e756386aa488e3f7b02a355590/LICENSE) · [\_\_main\_\_.py](https://github.com/a2aproject/a2a-samples/blob/b7a2a689ff3a86e756386aa488e3f7b02a355590/samples/python/agents/sign_and_verify_agent_card/`__main__`.py) · [oauth2_middleware.py](https://github.com/a2aproject/a2a-samples/blob/b7a2a689ff3a86e756386aa488e3f7b02a355590/samples/python/agents/headless_agent_auth/oauth2_middleware.py) · [pyproject.toml](https://github.com/a2aproject/a2a-samples/blob/b7a2a689ff3a86e756386aa488e3f7b02a355590/samples/python/pyproject.toml) · [linter.yaml](https://github.com/a2aproject/a2a-samples/blob/b7a2a689ff3a86e756386aa488e3f7b02a355590/.github/workflows/linter.yaml) |

<a id="n2-2026-11-24"></a>

## Nâng trần đợt hai — 23/11/2026

Hồ sơ lập trong đợt nâng trần thứ hai: đọc mã hoặc tài liệu tại commit cố định, chưa chạy upstream; mô tả của trinh sát sai ở nhiều repo nên điều ghi ở đây là điều đã đọc.

<a id="n2-mcp-gateway-registry-agentic-community"></a>

### MCP Gateway & Registry (agentic-community)

| Thuộc tính | Giá trị |
|---|---|
| Repo | https://github.com/agentic-community/mcp-gateway-registry |
| License | Apache-2.0 |
| Phiên bản đã đọc | `3b37ee2941ac5bbab23e012ea4d1885a69a4ea3e` (commit 2026-11-23) |
| Kiểm chứng | 2026-11-24; code-read; đã đọc README.md, LICENSE, auth_server/egress_obo.py, registry/core/config.py, .env.example, .github/workflows/registry-test.yml, terraform/telemetry-collector/README.md; chưa chạy upstream |
| Khoảng trống lấp | MCP gateway, registry và bảo mật: mặt phẳng điều khiển tự host cho MCP server, agent và skill |
| Cơ chế đáng học | - Tách data plane (nginx reverse proxy, TLS, xác thực) khỏi control plane (dịch vụ FastAPI giữ kho đăng ký, mô hình quyền, nhật ký kiểm toán): `README.md`.<br>- Egress OBO: trao đổi lại token đăng nhập của người dùng thành token có audience là app của MCP server (RFC 8693 hoặc jwt-bearer của Entra), trao đổi theo từng request, không cache chéo người dùng, và từ chối token nếu chính gateway cũng chấp nhận nó: `auth_server/egress_obo.py`.<br>- Kho đăng ký không chỉ cho MCP server mà cả agent (A2A), skill và thực thể tùy ý, tìm theo ngôn ngữ tự nhiên; có `AGENTS.md`/`CLAUDE.md` và skill cài đặt trong `.claude/skills/`. |
| Tiêu chí và cách kiểm | CI nhiều workflow riêng cho từng thành phần (registry-test chạy bộ test đầy đủ kèm coverage trên Python 3.14 với MongoDB 8.2, auth-server-test, helm-test, lua-test, terraform-test). Đã mở `registry-test.yml`, chưa thấy ngưỡng coverage cứng trong file này. Kiểm bằng máy có, kết quả chưa chạy lại. |
| Giới hạn và rủi ro | Telemetry **bật mặc định**: `telemetry_enabled` mặc định `True` (ping khởi động) cộng heartbeat 24 giờ, tắt bằng `MCP_TELEMETRY_DISABLED=1` hoặc chỉ heartbeat bằng `MCP_TELEMETRY_OPT_OUT=1`; điểm thu là Lambda và DocumentDB do dự án vận hành (`terraform/telemetry-collector`). Tác giả nói ẩn danh, không IP (chưa xác minh phía thu). Bề mặt rất lớn (Keycloak, MongoDB, nhiều IdP, Terraform AWS) nên chi phí vận hành cao; README ghi 350 dòng tối đa do CI cưỡng chế (chưa xác minh). |
| So với | `agentgateway` (data plane Rust), `mcp-registry` (registry chuẩn), `litellm` |
| Nguồn | [README.md](https://github.com/agentic-community/mcp-gateway-registry/blob/3b37ee2941ac5bbab23e012ea4d1885a69a4ea3e/README.md) · [LICENSE](https://github.com/agentic-community/mcp-gateway-registry/blob/3b37ee2941ac5bbab23e012ea4d1885a69a4ea3e/LICENSE) · [egress_obo.py](https://github.com/agentic-community/mcp-gateway-registry/blob/3b37ee2941ac5bbab23e012ea4d1885a69a4ea3e/auth_server/egress_obo.py) · [config.py](https://github.com/agentic-community/mcp-gateway-registry/blob/3b37ee2941ac5bbab23e012ea4d1885a69a4ea3e/registry/core/config.py) · [.env.example](https://github.com/agentic-community/mcp-gateway-registry/blob/3b37ee2941ac5bbab23e012ea4d1885a69a4ea3e/.env.example) · [registry-test.yml](https://github.com/agentic-community/mcp-gateway-registry/blob/3b37ee2941ac5bbab23e012ea4d1885a69a4ea3e/.github/workflows/registry-test.yml) · [README.md](https://github.com/agentic-community/mcp-gateway-registry/blob/3b37ee2941ac5bbab23e012ea4d1885a69a4ea3e/terraform/telemetry-collector/README.md) |

<a id="n2-docker-mcp-gateway-cli"></a>

### Docker MCP Gateway

| Thuộc tính | Giá trị |
|---|---|
| Repo | https://github.com/docker/mcp-gateway |
| License | MIT |
| Phiên bản đã đọc | `4b5180c5ba8e1b456c53b36b7f90f17964131a16` (commit 2026-11-19) |
| Kiểm chứng | 2026-11-24; code-read; đã đọc README.md, LICENSE, docs/security.md, pkg/interceptors/block_secrets.go, pkg/secretsscan/rules.go, pkg/gateway/clientpool.go, docs/telemetry/README.md, .github/workflows/ci.yml; chưa chạy upstream |
| Khoảng trống lấp | MCP gateway bảo mật: chạy MCP server trong container cô lập, chặn secret ở tool call |
| Cơ chế đáng học | - Mỗi MCP server chạy bằng `docker run --rm -i --init --security-opt no-new-privileges` kèm giới hạn `--cpus`/`--memory`: `pkg/gateway/clientpool.go`.<br>- Middleware `block-secrets` (bật mặc định) quét tham số tool call và nội dung text trả về bằng bộ rule sao chép từ Trivy, chặn nếu thấy khóa: `pkg/interceptors/block_secrets.go`, `pkg/secretsscan/rules.go`.<br>- `docs/security.md` nêu mô hình tin cậy rõ: transport HTTP đòi Bearer token mặc định, URL từ xa chỉ chấp nhận HTTPS công khai (chặn loopback, link-local, metadata), bind mount mặc định chỉ đọc và phải nằm trong danh sách cho phép, xác minh chữ ký image `mcp/` mặc định bật.<br>- Hồ sơ (profile) gom server, đẩy/kéo qua OCI registry; ghi đè tên tool trùng bị từ chối. |
| Tiêu chí và cách kiểm | CI chạy lint trên ba nền, `make test` trên Linux, build ba nền (đã mở `ci.yml`); có test Go cho interceptor, secretsscan, clientpool. Quét secret là regex theo từ khóa nên không thay cho kiểm soát egress. Chưa chạy. |
| Giới hạn và rủi ro | Mặc định không chặn egress mạng (`--block-network` và `allowHosts` là tùy chọn, theo chính `docs/security.md`). Telemetry OpenTelemetry nối vào collector cục bộ của Docker Desktop qua unix socket; khi không có cấu hình thì không xuất (theo `docs/telemetry/README.md`, chưa xác minh điểm đến cuối). Gắn chặt Docker Desktop 4.59+ hoặc cờ `DOCKER_MCP_IN_CONTAINER`; catalog và việc quét malware ở hệ thống riêng của Docker, ngoài repo. |
| So với | `agentgateway`, `mcp-registry`, `docker-sandboxes` |
| Nguồn | [README.md](https://github.com/docker/mcp-gateway/blob/4b5180c5ba8e1b456c53b36b7f90f17964131a16/README.md) · [LICENSE](https://github.com/docker/mcp-gateway/blob/4b5180c5ba8e1b456c53b36b7f90f17964131a16/LICENSE) · [security.md](https://github.com/docker/mcp-gateway/blob/4b5180c5ba8e1b456c53b36b7f90f17964131a16/docs/security.md) · [block_secrets.go](https://github.com/docker/mcp-gateway/blob/4b5180c5ba8e1b456c53b36b7f90f17964131a16/pkg/interceptors/block_secrets.go) · [rules.go](https://github.com/docker/mcp-gateway/blob/4b5180c5ba8e1b456c53b36b7f90f17964131a16/pkg/secretsscan/rules.go) · [clientpool.go](https://github.com/docker/mcp-gateway/blob/4b5180c5ba8e1b456c53b36b7f90f17964131a16/pkg/gateway/clientpool.go) · [README.md](https://github.com/docker/mcp-gateway/blob/4b5180c5ba8e1b456c53b36b7f90f17964131a16/docs/telemetry/README.md) · [ci.yml](https://github.com/docker/mcp-gateway/blob/4b5180c5ba8e1b456c53b36b7f90f17964131a16/.github/workflows/ci.yml) |

<a id="n2-microsoft-mcp-gateway-k8s"></a>

### Microsoft MCP Gateway

| Thuộc tính | Giá trị |
|---|---|
| Repo | https://github.com/microsoft/mcp-gateway |
| License | MIT |
| Phiên bản đã đọc | `0d24d9952de17563f231b7b0501ed595a98f7de9` (commit 2026-11-20) |
| Kiểm chứng | 2026-11-24; code-read; đã đọc README.md, LICENSE, dotnet/Microsoft.McpGateway.Management/src/Authorization/SimplePermissionProvider.cs, dotnet/Microsoft.McpGateway.Management/src/Authorization/BuiltinToolAuthorizer.cs, dotnet/Microsoft.McpGateway.Management/src/Contracts/ResourcePermission.cs, .github/workflows/main.yml; chưa chạy upstream |
| Khoảng trống lấp | MCP gateway trên Kubernetes: định tuyến không trạng thái và quản lý vòng đời server |
| Cơ chế đáng học | - Adapter (một MCP server) và Tool được quản lý qua API CRUD; Deployment Manager tạo workload trên Kubernetes, định tuyến `/adapters/{name}/mcp` và một tool router chung `/mcp`: `README.md`.<br>- Mô hình quyền gọn: đọc cho người tạo, vai trò trong `requiredRoles` hoặc `mcp.admin`; ghi chỉ cho người tạo hoặc `mcp.admin`; đóng khi rỗng: `SimplePermissionProvider.cs`, `ResourcePermission.cs`.<br>- Tool dựng sẵn `builtin:bash`, `builtin:read_file`, `builtin:write_file` bị vô hiệu cho mọi người gọi kể cả admin (README), còn `BuiltinToolAuthorizer` ghi fail-closed: cũng là ví dụ gỡ năng lực nguy hiểm thay vì chỉ gác quyền.<br>- Phiên bản này bỏ phiên giao vận cũ, chỉ nhận máy khách MCP `2026-07-28`, định tuyến từng request độc lập. |
| Tiêu chí và cách kiểm | CI: build Release và `dotnet test` trên .NET 8 cho toàn solution, thêm job test mcp-proxy (đã mở `main.yml`). Có test cho authorizer, executor, deployment manager. Chưa chạy. |
| Giới hạn và rủi ro | README ghi đây là thay đổi phá vỡ, không tương thích ngược, nên máy khách cũ không dùng được. Xác thực gắn Entra ID; lưu trữ Cosmos hoặc Redis; phần Agent và Session là bản xem trước (Preview) dựa trên Foundry. Quyền chỉ ở mức vai trò đơn giản, không có chính sách theo tool hay kiểm tra nội dung. License MIT, tác giả là Microsoft nhưng đây là mẫu gateway, mức hỗ trợ (chưa xác minh). |
| So với | `agentgateway`, `mcp-registry`, `kong` |
| Nguồn | [README.md](https://github.com/microsoft/mcp-gateway/blob/0d24d9952de17563f231b7b0501ed595a98f7de9/README.md) · [LICENSE](https://github.com/microsoft/mcp-gateway/blob/0d24d9952de17563f231b7b0501ed595a98f7de9/LICENSE) · [SimplePermissionProvider.cs](https://github.com/microsoft/mcp-gateway/blob/0d24d9952de17563f231b7b0501ed595a98f7de9/dotnet/Microsoft.McpGateway.Management/src/Authorization/SimplePermissionProvider.cs) · [BuiltinToolAuthorizer.cs](https://github.com/microsoft/mcp-gateway/blob/0d24d9952de17563f231b7b0501ed595a98f7de9/dotnet/Microsoft.McpGateway.Management/src/Authorization/BuiltinToolAuthorizer.cs) · [ResourcePermission.cs](https://github.com/microsoft/mcp-gateway/blob/0d24d9952de17563f231b7b0501ed595a98f7de9/dotnet/Microsoft.McpGateway.Management/src/Contracts/ResourcePermission.cs) · [main.yml](https://github.com/microsoft/mcp-gateway/blob/0d24d9952de17563f231b7b0501ed595a98f7de9/.github/workflows/main.yml) |

<a id="n2-kuadrant-mcp-gateway-envoy"></a>

### Kuadrant MCP Gateway

| Thuộc tính | Giá trị |
|---|---|
| Repo | https://github.com/Kuadrant/mcp-gateway |
| License | Apache-2.0 |
| Phiên bản đã đọc | `e98a736d59f2b22f2ce2d7201faf5bf5d43cd6cb` (commit 2026-11-23) |
| Kiểm chứng | 2026-11-24; code-read; đã đọc README.md, LICENSE, VISION.md, docs/design/security-architecture.md, docs/design/guardrails/README.md, internal/guardrails/checker.go, .github/workflows/tests.yaml; chưa chạy upstream |
| Khoảng trống lấp | MCP gateway cloud-native dựa trên Envoy ext_proc và Gateway API, có guardrail và RBAC theo tool |
| Cơ chế đáng học | - Router chạy như ext_proc của Envoy: đọc thân JSON-RPC để lấy method và tên tool, bỏ tiền tố tool, gắn header định tuyến; broker gom tool từ nhiều server: `docs/design/security-architecture.md`.<br>- RBAC theo tool: AuthPolicy (Authorino) khớp claim JWT với header `x-mcp-toolname`/`x-mcp-servername` rồi ký header `x-mcp-authorized` bằng ECDSA; broker kiểm chữ ký, header chưa ký hoặc bị sửa bị từ chối.<br>- Guardrails: lớp dịch `tools/call` (cả request và response) sang kiểm tra của NeMo Guardrails, mặc định fail-closed, `failMode: allow` tùy chọn theo server; timeout 8 giây, dial 1 giây: `internal/guardrails/checker.go`.<br>- Đứng ngoài phạm vi có chủ ý: không biến đổi nội dung tool, không tự ánh xạ OpenAPI sang MCP (`VISION.md`). |
| Tiêu chí và cách kiểm | CI có workflow unit test (`make test-unit`, kiểm e2e biên dịch được), e2e nightly và theo yêu cầu, conformance, performance-benchmark, helm-install-test, ratchet cho ghim action (đã mở `tests.yaml`, chưa mở các workflow khác). Chưa chạy. |
| Giới hạn và rủi ro | Sao thấp hơn nhiều gateway khác (lượng người dùng nhỏ, hướng nền tảng). Ghi thẳng rằng header `Authorization` gốc được chuyển nguyên tới upstream MCP server (theo `security-architecture.md`) nên server upstream phải đáng tin. Phụ thuộc Istio/Envoy, Authorino, Keycloak; không vận hành server guardrail hộ. Tác giả nói sẽ nhường chỗ cho chuẩn Envoy/Gateway API khi chín (`VISION.md`, tuyên bố). |
| So với | `agentgateway`, `kong`, `mcp-registry` |
| Nguồn | [README.md](https://github.com/Kuadrant/mcp-gateway/blob/e98a736d59f2b22f2ce2d7201faf5bf5d43cd6cb/README.md) · [LICENSE](https://github.com/Kuadrant/mcp-gateway/blob/e98a736d59f2b22f2ce2d7201faf5bf5d43cd6cb/LICENSE) · [VISION.md](https://github.com/Kuadrant/mcp-gateway/blob/e98a736d59f2b22f2ce2d7201faf5bf5d43cd6cb/VISION.md) · [security-architecture.md](https://github.com/Kuadrant/mcp-gateway/blob/e98a736d59f2b22f2ce2d7201faf5bf5d43cd6cb/docs/design/security-architecture.md) · [README.md](https://github.com/Kuadrant/mcp-gateway/blob/e98a736d59f2b22f2ce2d7201faf5bf5d43cd6cb/docs/design/guardrails/README.md) · [checker.go](https://github.com/Kuadrant/mcp-gateway/blob/e98a736d59f2b22f2ce2d7201faf5bf5d43cd6cb/internal/guardrails/checker.go) · [tests.yaml](https://github.com/Kuadrant/mcp-gateway/blob/e98a736d59f2b22f2ce2d7201faf5bf5d43cd6cb/.github/workflows/tests.yaml) |

<a id="n2-azure-ai-gateway-labs"></a>

### AI Gateway Labs (Azure API Management)

| Thuộc tính | Giá trị |
|---|---|
| Repo | https://github.com/Azure-Samples/AI-Gateway |
| License | MIT |
| Phiên bản đã đọc | `98c242510ba53f4e83e5f4f19595907c8e0b36bc` (commit 2026-11-05) |
| Kiểm chứng | 2026-11-24; code-read; đã đọc README.md, LICENSE.md, AGENTS.md, labs/token-rate-limiting/policy.xml, labs/semantic-caching/policy.xml, labs/mcp-client-authorization/README.MD, .github/workflows/nbchecks.py, .github/workflows/nbchecks.yaml; chưa chạy upstream |
| Khoảng trống lấp | AI gateway mẫu trên Azure API Management: giới hạn token, cache ngữ nghĩa, MCP và agent |
| Cơ chế đáng học | - Khoảng 50 lab (Jupyter + Bicep + policy APIM), mỗi lab một khả năng: giới hạn token, cache ngữ nghĩa, cân bằng tải backend pool, an toàn nội dung, MCP, A2A, đăng ký MCP: `AGENTS.md`, `labs/`.<br>- Giới hạn token chỉ là một dòng policy `llm-token-limit` (đếm theo subscription, tokens-per-minute): `labs/token-rate-limiting/policy.xml`.<br>- Cache ngữ nghĩa bằng `azure-openai-semantic-cache-lookup` với `score-threshold="0.8"` và lưu 120 giây ở Redis: `labs/semantic-caching/policy.xml`.<br>- Lab MCP client authorization cho APIM vừa là OAuth client (tới Entra ID) vừa là authorization server cho máy khách MCP. |
| Tiêu chí và cách kiểm | Chỉ một kiểm máy: `nbchecks.py` thất bại nếu notebook còn output lưu sẵn. Không có test hành vi cho policy; các lab cần tài khoản Azure thật nên không tái hiện cục bộ. Chưa chạy. |
| Giới hạn và rủi ro | Là mẫu thử nghiệm của Microsoft, chính `AGENTS.md` gọi là experimental; lab MCP authorization tự ghi chưa khuyến nghị dùng production do đặc tả đổi nhanh. Khóa chặt vào Azure APIM (không chạy ở nơi khác), tạo tài nguyên tính phí nên phải chạy bước dọn dẹp. Không phải sản phẩm gateway dùng ngay mà là kho công thức policy. |
| So với | `litellm`, `portkey-gateway`, `kong` |
| Nguồn | [README.md](https://github.com/Azure-Samples/AI-Gateway/blob/98c242510ba53f4e83e5f4f19595907c8e0b36bc/README.md) · [LICENSE.md](https://github.com/Azure-Samples/AI-Gateway/blob/98c242510ba53f4e83e5f4f19595907c8e0b36bc/LICENSE.md) · [AGENTS.md](https://github.com/Azure-Samples/AI-Gateway/blob/98c242510ba53f4e83e5f4f19595907c8e0b36bc/AGENTS.md) · [policy.xml](https://github.com/Azure-Samples/AI-Gateway/blob/98c242510ba53f4e83e5f4f19595907c8e0b36bc/labs/token-rate-limiting/policy.xml) · [policy.xml](https://github.com/Azure-Samples/AI-Gateway/blob/98c242510ba53f4e83e5f4f19595907c8e0b36bc/labs/semantic-caching/policy.xml) · [README.MD](https://github.com/Azure-Samples/AI-Gateway/blob/98c242510ba53f4e83e5f4f19595907c8e0b36bc/labs/mcp-client-authorization/README.MD) · [nbchecks.py](https://github.com/Azure-Samples/AI-Gateway/blob/98c242510ba53f4e83e5f4f19595907c8e0b36bc/.github/workflows/nbchecks.py) · [nbchecks.yaml](https://github.com/Azure-Samples/AI-Gateway/blob/98c242510ba53f4e83e5f4f19595907c8e0b36bc/.github/workflows/nbchecks.yaml) |

<a id="n2-agent-passport-system-aps"></a>

### Agent Passport System (APS)

| Thuộc tính | Giá trị |
|---|---|
| Repo | https://github.com/agent-passport-system/agent-passport-system |
| License | Apache-2.0 |
| Phiên bản đã đọc | `638ac267b15d290ae5dbbd79ecdd2b5af7170512` (commit 2026-11-22) |
| Kiểm chứng | 2026-11-24; code-read; đã đọc README.md, LICENSE, PRIVACY.md, REUSE.toml, src/core/delegation.ts, package.json, .github/workflows/tests.yml; chưa chạy upstream |
| Khoảng trống lấp | Agent định danh và ủy quyền: giao thức hộ chiếu, ủy quyền thu hẹp dần và biên nhận hành động có chữ ký |
| Cơ chế đáng học | - Ủy quyền chỉ được thu hẹp: `subDelegate` từ chối phạm vi con không nằm trong phạm vi cha (`scopeCovers`), ràng buộc đơn vị chi tiêu và thời hạn không được nới: `src/core/delegation.ts`.<br>- Chuỗi 3 chữ ký cho hành động: agent ký ý định, engine chính sách ký đánh giá, agent ký biên nhận thực thi; thu hồi lan tỏa theo chuỗi (README).<br>- Cổng thương mại 5 bước (hộ chiếu hợp lệ, phạm vi, hạn mức, danh sách người bán, tính lũy đẳng); xác minh biên nhận ngay trên trình duyệt.<br>- Triển khai chéo TypeScript, Python, Go, Rust, đối chiếu bằng bộ conformance và fixture; ghi trạng thái từng module (Canonical, Production-Extension, Experimental). |
| Tiêu chí và cách kiểm | Rất nhiều test: `npm test` liệt kê hàng trăm file (test tính chất, đối kháng, vector chéo ngôn ngữ), cộng typecheck fixtures; có workflow conformance, cross-impl JCS, scorecard, CodeQL, fuzz; README ghi coverage 97% dòng (chưa xác minh). Đã mở `tests.yml`, chưa mở các workflow khác. |
| Giới hạn và rủi ro | Gateway thực thi đã tách khỏi gói này sang `@aeoess/gateway` (kho khác), nên repo chỉ chứa nguyên thủy; `delegation.ts` cho biết các hàm trạng thái ném lỗi chỉ sang `DelegationStore`. Bề mặt tính năng rất rộng (thương mại, dữ liệu, hành vi, thanh toán) và nhiều phần Experimental nên khó đánh giá; một tác giả chính, IETF draft cá nhân (`draft-pidlisnyi-aps-03`) chưa phải chuẩn. License: Apache-2.0, riêng danh sách từ vựng dùng CC-BY-3.0 và MIT, bản thảo IETF dưới Trust TLP (theo `REUSE.toml`). `PRIVACY.md` nói không telemetry. |
| So với | `a2a`, `agent-client-protocol`, `mcp-registry` |
| Nguồn | [README.md](https://github.com/agent-passport-system/agent-passport-system/blob/638ac267b15d290ae5dbbd79ecdd2b5af7170512/README.md) · [LICENSE](https://github.com/agent-passport-system/agent-passport-system/blob/638ac267b15d290ae5dbbd79ecdd2b5af7170512/LICENSE) · [PRIVACY.md](https://github.com/agent-passport-system/agent-passport-system/blob/638ac267b15d290ae5dbbd79ecdd2b5af7170512/PRIVACY.md) · [REUSE.toml](https://github.com/agent-passport-system/agent-passport-system/blob/638ac267b15d290ae5dbbd79ecdd2b5af7170512/REUSE.toml) · [delegation.ts](https://github.com/agent-passport-system/agent-passport-system/blob/638ac267b15d290ae5dbbd79ecdd2b5af7170512/src/core/delegation.ts) · [package.json](https://github.com/agent-passport-system/agent-passport-system/blob/638ac267b15d290ae5dbbd79ecdd2b5af7170512/package.json) · [tests.yml](https://github.com/agent-passport-system/agent-passport-system/blob/638ac267b15d290ae5dbbd79ecdd2b5af7170512/.github/workflows/tests.yml) |

<a id="n2-toolhive"></a>

### ToolHive

| Thuộc tính | Giá trị |
|---|---|
| Repo | https://github.com/stacklok/toolhive |
| License | Apache-2.0 |
| Phiên bản đã đọc | `ae8b232db4282180e9c5decf08a68062ea12622a` (commit 2026-11-23) |
| Kiểm chứng | 2026-11-24; code-read; đã đọc README.md, LICENSE, docs/authz.md, pkg/authz/tool_filter.go, pkg/authz/authorizers/cedar/core.go, pkg/runner/middleware.go, pkg/usagemetrics/collector.go, pkg/sentry/sentry.go, .github/workflows/lint.yml; chưa chạy upstream |
| Khoảng trống lấp | Cổng gateway và proxy cho MCP có kiểm soát chính sách |
| Cơ chế đáng học | - `docs/authz.md` mô tả giao diện `Authorizer` có đăng ký factory; có hai loại `cedarv1` và `httpv1`.<br>- `pkg/authz/authorizers/cedar/core.go` dùng cedar-go, chính sách dạng `permit(principal, action == Action::"call_tool", resource == Tool::"weather")`.<br>- `pkg/authz/tool_filter.go` lọc danh sách tool theo quyền, truyền annotation (ví dụ readOnlyHint) vào ngữ cảnh Cedar.<br>- Phân tích MCP từ chối JSON-RPC lỗi, gộp, mơ hồ trước khi phân quyền (docs/authz.md). |
| Tiêu chí và cách kiểm | Có nhiều test đơn vị và tích hợp trong `pkg/authz` (ví dụ `case_smuggling_test.go`, `resource_uri_test.go`); CI có lint (golangci-lint), e2e, operator-ci, kiểm API tương thích, kiểm license header (chỉ đọc `lint.yml`, các workflow khác chỉ biết tên). Phân quyền được kiểm bằng máy; hiệu quả cô lập container chưa được kiểm trong phiên này. |
| Giới hạn và rủi ro | Usage metrics mặc định BẬT (`pkg/usagemetrics/collector.go`): tắt khi CI, khi cấu hình `disable_usage_metrics` hoặc biến môi trường; endpoint mặc định https://updates.stacklok.com/api/v1/toolcount, nội dung gửi chưa xác minh. Sentry chỉ chạy khi có DSN cấu hình. README ghi enforcement chỉ có "khi cấu hình nguồn xác thực", tức mặc định không buộc danh tính. Tuyên bố tiết kiệm token tới 85% (chưa xác minh). Có bản Stacklok Enterprise trả phí tách riêng. Phát hành nhanh (VERSION 0.68.0), API còn đổi. |
| So với | `agentgateway` (gateway MCP/agent, cùng nhóm); `cisco-mcp-scanner` (quét máy chủ MCP, không chạy runtime); `portkey-gateway` (gateway LLM). |
| Nguồn | [README.md](https://github.com/stacklok/toolhive/blob/ae8b232db4282180e9c5decf08a68062ea12622a/README.md) · [LICENSE](https://github.com/stacklok/toolhive/blob/ae8b232db4282180e9c5decf08a68062ea12622a/LICENSE) · [authz.md](https://github.com/stacklok/toolhive/blob/ae8b232db4282180e9c5decf08a68062ea12622a/docs/authz.md) · [tool_filter.go](https://github.com/stacklok/toolhive/blob/ae8b232db4282180e9c5decf08a68062ea12622a/pkg/authz/tool_filter.go) · [core.go](https://github.com/stacklok/toolhive/blob/ae8b232db4282180e9c5decf08a68062ea12622a/pkg/authz/authorizers/cedar/core.go) · [middleware.go](https://github.com/stacklok/toolhive/blob/ae8b232db4282180e9c5decf08a68062ea12622a/pkg/runner/middleware.go) · [collector.go](https://github.com/stacklok/toolhive/blob/ae8b232db4282180e9c5decf08a68062ea12622a/pkg/usagemetrics/collector.go) · [sentry.go](https://github.com/stacklok/toolhive/blob/ae8b232db4282180e9c5decf08a68062ea12622a/pkg/sentry/sentry.go) · [lint.yml](https://github.com/stacklok/toolhive/blob/ae8b232db4282180e9c5decf08a68062ea12622a/.github/workflows/lint.yml) |
