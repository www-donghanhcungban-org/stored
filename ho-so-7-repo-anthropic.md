# Hồ sơ chi tiết 7 repo Anthropic đáng lưu

- Ngày lập: 2026-11-27
- Nguồn: đọc trực tiếp trang GitHub và README của từng repo (không dựa vào bài đăng gốc).
- Quy ước: mục ghi **[chưa xác minh]** nghĩa là chưa đọc được nguồn để khẳng định. Số sao/fork là số hiển thị tại thời điểm đọc, không có ngày commit cuối cùng ở bất kỳ repo nào (trang không hiển thị).

## Bảng tổng quan

| # | Repo | Giấy phép | Sao | Fork | Cần API key? | Mức duy trì (theo README) |
|---|------|-----------|-----|------|--------------|---------------------------|
| 1 | claude-code-playground | Apache-2.0 | 831 | 132 | Tùy từng mục | Không phải sản phẩm chính thức, như-là, không nhận đóng góp |
| 2 | skills | Apache-2.0 (nhiều skill) | ~201k | ~23.5k | Không (Claude Code/Claude.ai cần gói trả phí) | Chỉ để minh họa, giáo dục |
| 3 | claude-plugins-official | Apache-2.0 (từng plugin có thể khác) | 48.4k | 5.1k | Tùy plugin | Anthropic quản lý, rất hoạt động (4.895 commit) |
| 4 | launch-your-agent | Apache-2.0 | 1.4k | 273 | Có (API key Anthropic) | Không bảo trì, không nhận đóng góp |
| 5 | knowledge-work-plugins | Apache-2.0 | 37.1k | 4.1k | Cần Cowork hoặc Claude Code | Mã nguồn mở, nhận PR |
| 6 | claude-quickstarts | MIT | 21.3k | 3.5k | Có (Claude API key) | Chưa xác minh |
| 7 | prompt-eng-interactive-tutorial | Chưa xác minh | 39.9k | 4.4k | Chưa xác minh | **Có thể lỗi thời** (dùng Claude 3) |

---

## 1. claude-code-playground

- URL: https://github.com/anthropics/claude-code-playground
- **Mục đích:** Bộ sưu tập cấu hình Claude Code, skill và demo do nhóm DevRel của Anthropic tự dùng. Nội dung theo kiểu "đây là cái chúng tôi đã làm", không phải hướng dẫn thực hành tốt nhất.
- **Lưu ý quan trọng (từ README):** không phải sản phẩm chính thức của Anthropic, cung cấp nguyên trạng, không cam kết còn chạy được, không nhận đóng góp từ bên ngoài (issue/PR có thể bị đóng không xem xét).
- Thống kê: 831 sao, 132 fork, 17 watcher, 10 issue mở, 8 PR mở, 3 commit trên `main`.
- Ngôn ngữ: **[chưa xác minh]** (nội dung hỗn hợp: Markdown, cấu hình, hook, skill, demo).
- **Cấu trúc thư mục cấp cao:** `.github/`, `_template/`, `claude-code/`, `demos/`, `launch-demos/`, `skills/`, cùng các file CLAUDE.md, CONTRIBUTING.md, SECURITY.md, LICENSE...
  - `claude-code/hooks/`: ví dụ hook, mỗi hook một thư mục
  - `claude-code/claude-md/`: file CLAUDE.md thật kèm chú giải
  - `claude-code/settings/`: ví dụ settings.json
  - `claude-code/workflows/`: cách thiết lập cá nhân từ đầu đến cuối
  - `claude-code/mods/`: plugin đổi hành vi hoặc giao diện Claude Code
  - `skills/`: skill tái sử dụng chưa có trong marketplace chính thức
  - `demos/` và `launch-demos/`: demo "khả năng có thể" và demo ra mắt model, kèm prompt và cách thiết lập
- **Cách dùng:** không cài gì ở thư mục gốc. Mở thư mục của từng mục và làm theo phần "Run it" trong README của mục đó. Số lượng và nội dung từng mục **[chưa xác minh]** (chưa mở thư mục con).
- Yêu cầu và chi phí: không nêu ở cấp gốc. Mỗi mục có README riêng.
- Repo liên quan README nhắc: `skills`, `claude-quickstarts`, `claude-agent-sdk-demos`, `claude-cookbooks`, `claude-plugins-official`.
- **Phù hợp với:** người đã dùng Claude Code muốn xem cách đội DevRel cấu hình hook, CLAUDE.md, workflow. Không phải template để fork, ví dụ có thể lỗi thời.

## 2. skills

- URL: https://github.com/anthropics/skills
- **Mục đích:** Kho Agent Skills mẫu của Anthropic. Mỗi skill là một thư mục gồm hướng dẫn, script và tài nguyên để Claude nạp khi làm việc chuyên biệt. README ghi các skill này được cung cấp "chỉ để minh họa và giáo dục". Các skill docx, pdf, pptx, xlsx là nền cho tính năng tài liệu của Claude và được chia sẻ như tham chiếu cho skill phức tạp.
- Thống kê: ~201k sao, ~23.5k fork, ~1.2k watcher, 467 issue mở, ~1.1k PR, 64 commit.
- Giấy phép: README nói nhiều skill là Apache 2.0, gồm docx/pdf/pptx/xlsx. Không phải skill nào cũng xác minh được, cần xem LICENSE.txt từng skill.
- **Cấu trúc:** `.claude-plugin/`, `skills/` (mẫu), `spec/` (đặc tả Agent Skills), `template/` (khuôn skill), `THIRD_PARTY_NOTICES.md`.
- **Danh sách skill (19 thư mục):** academy-guide, algorithmic-art, brand-guidelines, canvas-design, claude-api, discernment-nudge, doc-coauthoring, docx, frontend-design, internal-comms, mcp-builder, pdf, pptx, skill-creator, slack-gif-creator, theme-factory, web-artifacts-builder, webapp-testing, xlsx.
  - Đã xác minh: `docx` (tạo, đọc, sửa .docx/.dotx, gồm tracked changes, comment, tìm-thay thế).
  - Các skill còn lại chỉ suy ra từ tên thư mục, **[chưa xác minh]** mục đích chi tiết (đặc biệt academy-guide, discernment-nudge).
- **Định dạng skill:** thư mục chứa `SKILL.md` gồm YAML frontmatter (bắt buộc `name`, `description`) rồi hướng dẫn Markdown. Skill docx còn có `scripts/` và `LICENSE.txt`.
- **Cài đặt và dùng:**
  - Claude Code: `/plugin marketplace add anthropics/skills`, sau đó `/plugin install document-skills@anthropic-agent-skills` hoặc `/plugin install example-skills@anthropic-agent-skills`.
  - Claude.ai: README nói skill mẫu đã có sẵn cho gói trả phí.
  - Claude API: có thể dùng skill dựng sẵn và tải skill tùy chỉnh (hướng dẫn: docs.claude.com/en/api/skills-guide, chưa mở).
- Phụ thuộc của docx: gói npm `docx`, pandoc, LibreOffice, pdftoppm (Poppler). Các skill khác **[chưa xác minh]**.
- Chi phí: README không nêu giá; Claude.ai cần gói trả phí.
- **Phù hợp với:** người làm tài liệu văn phòng và người muốn học cách viết skill riêng. Không phải thư viện ổn định cho sản xuất.

## 3. claude-plugins-official

- URL: https://github.com/anthropics/claude-plugins-official
- **Mục đích:** Thư mục plugin chính thức do Anthropic quản lý cho Claude Code, đồng thời là marketplace `claude-plugins-official`. Topics: claude-code, mcp, skills.
- Thống kê: 48.4k sao, 5.1k fork, 268 watcher, 1.1k issue mở, 226 PR mở, 4.895 commit.
- Giấy phép: Apache-2.0; từng plugin có thể có LICENSE riêng **[chưa kiểm từng plugin]**.
- **Thay đổi đáng chú ý:** plugin bên thứ ba nay nộp qua claude.ai/directory/manage; PR plugin bên thứ ba vào repo này "không được theo dõi". `marketplace.json` đang được rút dần cho plugin bên thứ ba.
- **Cấu trúc:** `.claude-plugin/marketplace.json`, `plugins/` (do Anthropic làm; `example-plugin` là bản tham chiếu), `external_plugins/` (bên thứ ba thêm trước đây, cùng các plugin kênh của Anthropic: Discord, fakechat, iMessage, Telegram).
- **`plugins/` (43 thư mục, chỉ liệt kê tên):** agent-sdk-dev, champion-kit, clangd-lsp, claude-code-setup, claude-for-manufacturing, claude-md-management, claude-security, code-modernization, code-review, code-simplifier, commit-commands, csharp-lsp, cwc-makers, example-plugin, explanatory-output-style, feature-dev, frontend-design, gopls-lsp, hookify, jdtls-lsp, kotlin-lsp, learning-output-style, lua-lsp, math-olympiad, math-proof, mcp-server-dev, mcp-tunnels, php-lsp, playground, plugin-dev, pr-review-toolkit, project-artifact, pyright-lsp, ralph-loop, receipts, ruby-lsp, rust-analyzer-lsp, security-guidance, session-report, skill-creator, swift-lsp, theme-examples, typescript-lsp.
  - Mô tả chỉ xác minh cho một số: agent-sdk-dev (bộ công cụ Agent SDK), champion-kit (hackathon, báo cáo mức độ trưởng thành AI), clangd-lsp (language server C/C++), claude-code-setup (gợi ý hook, skill, MCP, subagent cho codebase), claude-md-management (kiểm tra và bảo trì CLAUDE.md), claude-security (agent tìm và sửa lỗ hổng, GitHub Action review PR). Còn lại **[chưa xác minh]**.
- **`external_plugins/` (14):** asana, context7, discord, fakechat, firebase, github, gitlab, imessage, laravel-boost, linear, playwright, serena, telegram, terraform.
- **Plugin Telegram (đã đọc README):** nối bot Telegram với Claude Code qua MCP server. Claude có công cụ `reply`, `react` (chỉ emoji Telegram cho phép), `edit_message` (chỉ tin của bot). Tin nhắn DM gửi bot được chuyển vào phiên Claude Code.
  - Yêu cầu: Bun.
  - Các bước: (1) tạo bot qua @BotFather bằng `/newbot` và lấy token; (2) `/plugin install telegram@claude-plugins-official`; (3) `/telegram:configure <token>`; (4) khởi động lại bằng `claude --channels plugin:telegram@claude-plugins-official`; (5) nhắn bot để lấy mã ghép 6 ký tự rồi `/telegram:access pair <code>`; (6) khóa lại bằng `/telegram:access policy allowlist`.
  - Giới hạn: không có lịch sử/tìm kiếm tin nhắn (giới hạn của Bot API). Chính sách mặc định là "pairing", nên nên chuyển sang allowlist.
- **Cài plugin nói chung:** `/plugin install <tên>@claude-plugins-official` hoặc duyệt `/plugin` > Discover.
- **Cấu trúc một plugin:** `.claude-plugin/plugin.json` (bắt buộc), `.mcp.json`, `commands/`, `agents/`, `skills/`, `README.md`.
- **Bảo mật (cảnh báo trong README):** chỉ cài plugin bạn tin tưởng. Anthropic không kiểm soát MCP server, file hay phần mềm trong plugin và không đảm bảo chúng không thay đổi.
- Chi phí: README không nêu. Plugin bọc dịch vụ bên ngoài có thể phát sinh phí riêng **[chưa xác minh]**.
- Chưa xác minh: tổng số plugin trong `marketplace.json` (file ~191k ký tự, chỉ đọc một phần), việc Telegram có mục trong marketplace.
- **Phù hợp với:** người dùng Claude Code muốn plugin chính thức; người viết plugin (xem `example-plugin`).

## 4. launch-your-agent

- URL: https://github.com/anthropics/launch-your-agent
- **Mục đích:** Một skill của Claude Code (kèm skill `/wrap-up`) giúp người làm kỹ thuật dựng agent trên **Claude Managed Agents (CMA)**. Skill phỏng vấn bạn, chốt phạm vi bản v0, chạy trong tài khoản Anthropic của bạn, chấm theo tiêu chí hoàn thành do bạn định nghĩa, lặp cải tiến, và tùy chọn đặt lịch chạy.
- **Lưu ý quan trọng (từ README):** là "bản triển khai tham chiếu", **không bảo trì, không nhận đóng góp**, mang tính giáo dục, và "tốn token hơn agent làm riêng".
- Thống kê: 1.4k sao, 273 fork, 12 watcher, 2 PR mở, 7 commit. Giấy phép Apache-2.0.
- **Cấu trúc:** `.claude/skills/` (`launch-your-agent/`, `wrap-up/`), `ui/` (trang tổng quan và build sheet mẫu), `CLAUDE.md`, `CONTRIBUTING.md`, `cma-primitives.md`, `LICENSE`, `README.md`. Thư mục `references/` trong skill chưa đọc.
- **Quy trình (SKILL.md v0.3.0):**
  1. Phỏng vấn thành kế hoạch (không cần API key): đưa ví dụ agent, hỏi bạn muốn xây gì, đọc lại bản tóm tắt gồm primitive, danh sách v1/v2, bảng eval nhỏ; sinh thư mục `my-agent/` gồm `agent-overview.html`.
  2. Dựng và chạy: kiểm tra payload, hỏi API key một lần và lưu ở `my-agent/.env` (chmod 600, không bao giờ qua chat), chạy với tiêu chí kết quả và `max_iterations: 3`.
  3. Chấm và lặp: mỗi vòng chỉ đổi một thứ, chạy các ca eval giữ lại.
  4. Đặt lịch (nếu việc lặp lại): triển khai theo cron và múi giờ, có chạy thử thủ công.
  - Mặc định: một agent dùng model Opus mới nhất, kết nối giả (mock) ở v0, đầu ra chỉ là bản nháp. Kết thúc bằng `/wrap-up` tạo trang tổng quan và `NEXT-DIRECTIONS.md`.
- **Cài và chạy:**

  ```bash
  git clone https://github.com/anthropics/launch-your-agent.git
  cd launch-your-agent
  claude
  ```

  Sau đó gõ `/launch-your-agent`.
- Yêu cầu: Claude Code đã đăng nhập; **API key Anthropic của riêng bạn** (tạo ở platform.claude.com); tùy chọn CLI `ant`.
- Chi phí: README ghi "chạy tốn vài cent" và giới hạn bằng `max_iterations: 3`. Giá CMA **[chưa xác minh]**.
- Chưa xác minh: ngày cập nhật, nội dung `cma-primitives.md`, skill `wrap-up`, thư mục `references/`, hai PR đang mở.
- **Phù hợp với:** người làm kỹ thuật, founder muốn học các primitive của CMA (agent, environment, outcome, session, deployment, vault, memory store, skill). Không phù hợp nếu cần sản phẩm sản xuất hoặc có hỗ trợ.

## 5. knowledge-work-plugins

- URL: https://github.com/anthropics/knowledge-work-plugins
- **Mục đích:** Kho plugin mã nguồn mở chủ yếu cho nhân viên tri thức dùng trong **Claude Cowork**, biến Claude thành chuyên gia theo vai trò. Mỗi plugin gồm skill, connector (MCP server), lệnh slash và sub-agent, dạng file "Markdown và JSON, không code, không hạ tầng, không bước build".
- Thống kê: 37.1k sao, 4.1k fork, 233 watcher, 98 issue mở, 79 PR mở, 1.153 commit. Giấy phép Apache-2.0.
- **Thư mục plugin (18):** bio-research, cowork-plugin-management, customer-support, data, design, engineering, enterprise-search, finance, human-resources, legal, marketing, operations, partner-built, pdf-viewer, product-management, productivity, sales, small-business. Bảng trong README chỉ nêu 11; **design, engineering, human-resources, operations, small-business, partner-built, pdf-viewer chưa mở, nội dung chưa xác minh.**
- **Chi tiết các plugin đã đọc:**
  - **productivity:** quản lý việc, lịch, bộ nhớ nơi làm việc; lệnh `/start`, `/update`; giữ `TASKS.md`, `CLAUDE.md`, `memory/`, `dashboard.html`. Connector: Slack, Microsoft 365, Notion, Asana, Linear, Atlassian, monday.com, ClickUp.
  - **sales (v2.0, 36 skill, không có `commands/`):** tìm khách, chuẩn bị cuộc gọi, pipeline, dự báo; gọi theo tên như `/sales:call-summary`. Connector: CRM (HubSpot, Close, Salesforce), email/lịch, ghi âm cuộc gọi (Gong, Fireflies, Zoom, Otter.ai), làm giàu dữ liệu (Clay, ZoomInfo, Apollo...). Salesforce và Microsoft 365 cần quản trị viên bật.
  - **finance:** đóng sổ cuối tháng, kế toán; lệnh `/journal-entry`, `/reconciliation`, `/income-statement`, `/variance-analysis`, `/sox-testing`. Ghi rõ không phải tư vấn tài chính, thuế hay kiểm toán.
  - **legal:** rà soát hợp đồng, phân loại NDA, tuân thủ; lệnh `/review-contract`, `/triage-nda`, `/vendor-check`, `/brief`, `/respond`. Dùng playbook `legal.local.md` do bạn viết. Mặc định theo quan điểm pháp lý Mỹ (Delaware, New York, California), người dùng ngoài Mỹ phải tùy chỉnh. Ghi rõ không phải tư vấn pháp lý.
  - **marketing:** nội dung, chiến dịch, giọng thương hiệu, SEO, báo cáo; lệnh `/draft-content`, `/campaign-plan`, `/brand-review`, `/competitive-brief`, `/performance-report`, `/seo-audit`, `/email-sequence`.
  - Chỉ có tên và connector (chưa mở thư mục): customer-support, product-management, data, enterprise-search, bio-research, cowork-plugin-management.
- **Cài và dùng:**
  - Cowork: cài từ claude.com/plugins.
  - Claude Code:

    ```bash
    claude plugin marketplace add anthropics/knowledge-work-plugins
    claude plugin install sales@knowledge-work-plugins
    ```

  - Sau khi cài, skill tự kích hoạt khi liên quan; lệnh dạng `/sales:call-prep`, `/data:write-query`, `/finance:reconciliation`.
  - Tùy biến: sửa `.mcp.json` để đổi connector, thêm ngữ cảnh công ty vào file skill.
- Yêu cầu: Cowork hoặc Claude Code, cộng tài khoản các công cụ bạn muốn nối. Yêu cầu gói và chi phí **[chưa xác minh]**.
- **Phù hợp với:** nhân viên bán hàng, marketing, tài chính, pháp lý, sản phẩm, hỗ trợ, dữ liệu; đội muốn tùy biến theo quy trình riêng. Kết quả tài chính và pháp lý cần chuyên gia kiểm tra.

## 6. claude-quickstarts

- URL: https://github.com/anthropics/claude-quickstarts
- **Mục đích:** "Bộ sưu tập dự án giúp lập trình viên bắt đầu nhanh với ứng dụng triển khai được bằng Claude API". Mỗi dự án có README riêng.
- Thống kê: 21.3k sao, 3.5k fork, 185 watcher, 136 issue mở, 123 PR mở, 118 commit. Giấy phép MIT (chưa mở file LICENSE).
- **18 dự án (ngăn xếp công nghệ chỉ ghi khi README nêu):**
  1. customer-support-agent: hệ thống hỗ trợ có truy cập cơ sở kiến thức.
  2. financial-data-analyst: chat phân tích dữ liệu tài chính, có biểu đồ tương tác.
  3. computer-use-demo: môi trường đóng gói để Claude điều khiển máy tính.
  4. computer-use-best-practices: tham chiếu native-macOS cho agent computer use, khuyên chạy trong VM (prompt caching, cắt tỉa ảnh, nén phía server, shell sandbox, ghi quỹ đạo).
  5. browser-use-demo: tự động hóa trình duyệt với công cụ Playwright tùy chỉnh.
  6. browser-toolset: ví dụ tối giản Chrome DevTools Protocol (Python và TypeScript, "không phải code sản xuất").
  7. computer-toolset: ví dụ tối giản VNC/RFB (Python và TypeScript, "không phải code sản xuất").
  8. autonomous-coding: mô hình hai agent (khởi tạo và lập trình) xây ứng dụng qua nhiều phiên, lưu tiến độ bằng git, dùng Claude Agent SDK.
  9–18. Nhóm `managed-agents/`: chat-sdk (chat trình duyệt, mỗi hội thoại một session), copilot-kit-ag-ui (trợ lý tài chính cá nhân), daily-brief (agent đặt lịch đọc Slack/GitHub PR rồi đăng bản tin lên Slack), knowledge-wiki (wiki phòng deal từ hồ sơ SEC EDGAR), linear (agent được @mention trong Linear), mcp-server-typescript (MCP server bọc Sessions API, TypeScript), roadtrip-planner (lập lộ trình công viên quốc gia, Next.js), sentry (phân loại lỗi Sentry theo cron), sentry-autofix (webhook mở PR sửa lỗi, có trần chi phí mỗi session), slack (bot Slack, cầu nối webhook không có CSDL).
  - Ngôn ngữ các dự án còn lại **[chưa xác minh]**.
- **Cách làm chung:** clone repo, vào thư mục dự án, cài phụ thuộc, đặt API key làm biến môi trường, chạy. Lệnh cụ thể nằm trong README từng dự án, **chưa đọc**.
- Yêu cầu: Claude API key (đăng ký ở console.anthropic.com). Một số dự án cần thêm macOS hoặc VM, container, trình duyệt Chromium, hoặc tài khoản Slack, Linear, Sentry, GitHub **[chưa xác minh từng dự án]**.
- Chi phí: README không nêu giá; tính theo mức dùng API.
- **Phù hợp với:** lập trình viên đã có API key cần điểm xuất phát chạy được. Dự án computer use cần thận trọng về an toàn.

## 7. prompt-eng-interactive-tutorial

- URL: https://github.com/anthropics/prompt-eng-interactive-tutorial
- **Mục đích:** Khóa học từng bước về cách viết prompt tối ưu cho Claude: cấu trúc prompt tốt, nhận biết lỗi thường gặp và sửa kiểu "80/20", hiểu điểm mạnh yếu của Claude, tự dựng prompt cho các ca dùng phổ biến.
- Thống kê: 39.9k sao, 4.4k fork, 385 watcher, 43 issue mở, 26 PR mở, 9 commit, nhánh mặc định `master`. Giấy phép: **[chưa xác minh]** (trang About không hiển thị).
- **Nội dung:** 9 chương có bài tập và 1 phụ lục, nên học theo thứ tự.
  - Cơ bản: Ch1 Cấu trúc prompt cơ bản; Ch2 Rõ ràng và trực tiếp; Ch3 Gán vai trò.
  - Trung cấp: Ch4 Tách dữ liệu khỏi chỉ dẫn; Ch5 Định dạng đầu ra và nói thay Claude; Ch6 Tư duy từng bước; Ch7 Dùng ví dụ.
  - Nâng cao: Ch8 Tránh ảo giác; Ch9 Prompt phức tạp theo ngành (chatbot, pháp lý, tài chính, lập trình).
  - Phụ lục: Chuỗi prompt, dùng công cụ, tìm kiếm và truy xuất.
  - Mỗi bài có "Example Playground"; đáp án nằm trong Google Sheet.
- **Định dạng:** README mô tả bản chạy trên Google Sheets với tiện ích Claude for Sheets (dễ dùng hơn). Repo có thư mục `AmazonBedrock` và `Anthropic 1P` (chưa mở, định dạng notebook **[chưa xác minh]**).
- Yêu cầu, cách cài, chi phí: **[chưa xác minh]** (README không nêu).
- **Cảnh báo lỗi thời:** README dùng "Claude 3 Haiku" và nhắc Claude 3 Sonnet/Opus. Với thời điểm hiện tại, tên model, ID và giá trong khóa học nhiều khả năng không còn đúng.
- **Phù hợp với:** người mới đến trung cấp muốn bài tập có hướng dẫn. Người cần tra cứu nhanh có thể thấy chậm.

---

## Đối chiếu với bài đăng gốc

- Bài viết nói Skills dành cho "Word, PDF, PowerPoint, Excel": đúng (docx, pdf, pptx, xlsx), nhưng repo còn nhiều skill khác (thiết kế, MCP, kiểm thử web...).
- Bài viết mô tả **Launch Your Agent** là "Claude hỏi muốn tự động hóa gì, chạy thử, đặt lịch": đúng, nhưng thiếu hai điều: nó cần API key riêng và dựng agent trên Managed Agents; repo ghi rõ là không bảo trì.
- Bài viết mô tả **Playground** là "cấu hình, skill, demo để tham khảo": đúng, nhưng README nhấn mạnh đây không phải sản phẩm chính thức và không đảm bảo còn chạy.
- Bài viết dùng đúng cả 7 URL và cả 7 repo đều tồn tại, công khai.
- Bài viết nhắc plugin Telegram nằm ở repo plugin chính thức: đúng, nằm ở `external_plugins/telegram`.
- Về chi phí, bài viết cảnh báo API có thể phát sinh phí: phù hợp (quickstarts, launch-your-agent cần API key).

## Chưa kiểm chứng (toàn bộ hồ sơ)

- Ngày commit cuối của cả 7 repo.
- README riêng của từng mục/dự án con ở playground, quickstarts và nhiều plugin.
- Giá và gói Cowork, Claude Code, Managed Agents.
- Giấy phép repo số 7.
