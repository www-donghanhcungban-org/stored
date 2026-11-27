# Hồ sơ chi tiết từng dự án trong `anthropics/claude-quickstarts`

- Ngày lập: 2026-11-27
- Nguồn: README của từng thư mục dự án (raw.githubusercontent.com, nhánh `main`). Cả 18 README đọc được, không có lỗi 404.
- Chưa đọc: các file `skill.md`, `CLAUDE.md`, `.env.example`, file YAML agent/environment mà README nhắc tới. Mục nào bị thiếu thì ghi "không nêu".
- Không README nào nêu giá cụ thể, trừ `daily-brief`, `knowledge-wiki` và trần chi phí của `sentry-autofix`.
- `managed-agents/README.md` chỉ là danh mục, không có yêu cầu chung. Danh mục còn liệt kê `assistant-ui/` và `self-hosted-sandboxes/` mà README gốc của repo không đếm trong 18 dự án; hai thư mục này chưa đọc.

## Bảng tóm tắt

| Dự án | Công nghệ | Cần gì ngoài API key | Mức rủi ro/lưu ý chính |
|---|---|---|---|
| customer-support-agent | Next.js, TypeScript | AWS Bedrock + knowledge base | Prototype, không dành cho sản xuất |
| financial-data-analyst | Next.js 14, Recharts | Node 20+ | README clone nhầm repo |
| computer-use-demo | Python, Docker, Streamlit | Docker | Prompt injection, chạy trong VM/container |
| computer-use-best-practices | Python (macOS) | macOS, Python 3.11+ | Điều khiển chuột/bàn phím thật |
| browser-use-demo | Python, Docker, Playwright | Docker Compose | Không dùng cho sản xuất |
| browser-toolset | Python + TypeScript, CDP | Chromium | Không phải code sản xuất |
| computer-toolset | Python + TypeScript, VNC | Máy chủ VNC | Chỉ dùng desktop dùng-một-lần |
| autonomous-coding | Python, Agent SDK | Claude Code CLI | Chạy nhiều giờ |
| managed-agents/chat-sdk | TypeScript, Hono, React | Node 22.9+ | `getUser` tin mọi người gọi |
| managed-agents/copilot-kit-ag-ui | Node, Express, Vite | Node 22+, `ant` CLI | Endpoint chat không có xác thực |
| managed-agents/daily-brief | Shell, YAML | Slack app, GitHub PAT | Có ước tính chi phí |
| managed-agents/knowledge-wiki | Python 3.11+, Jupyter | `EDGAR_USER_AGENT` | ~$16 một lượt chạy `core` |
| managed-agents/linear | Bun, TypeScript | Quyền admin Linear, tunnel | Cài đầu tiên chiếm quyền sở hữu |
| managed-agents/mcp-server-typescript | Bun, TypeScript | Agent có sẵn | Token HTTP chạy được mọi agent |
| managed-agents/roadtrip-planner | Next.js | Khóa NPS và Windy | Không có tài khoản người dùng |
| managed-agents/sentry | Python (`uv`) | Tài khoản Sentry | Tổ chức bật SSO có thể lỗi |
| managed-agents/sentry-autofix | TypeScript, Node 22.9+ | GitHub ruleset, Sentry | Trần $10/phiên |
| managed-agents/slack | Bun, TypeScript | Slack app, tunnel | Phải chạy server trước khi lưu URL |

---

## Nhóm 1: ứng dụng kiểu truyền thống

### 1. customer-support-agent
- **Làm gì:** Giao diện chat hỗ trợ khách hàng chạy bằng Claude, truy xuất qua Amazon Bedrock Knowledge Bases. Có hiển thị suy nghĩ/debug, nguồn tri thức, phát hiện tâm trạng người dùng để chuyển cho nhân viên, giao diện shadcn/ui.
- **Công nghệ:** Next.js (App Router, suy ra từ file), TypeScript, shadcn/ui, `@anthropic-ai/sdk` v1.x.
- **Yêu cầu:** Node.js 20+; API key Anthropic; tài khoản AWS có Bedrock, IAM user với `AmazonBedrockFullAccess`, một knowledge base (ví dụ dùng Titan Text Embeddings 2).
- **Chạy:**
  ```bash
  npm install
  npm run dev   # mở http://localhost:3000
  ```
- **Biến môi trường** (`.env.local`): `ANTHROPIC_API_KEY`, `BAWS_ACCESS_KEY_ID`, `BAWS_SECRET_ACCESS_KEY` (tiền tố B vì Amplify không cho khóa bắt đầu bằng AWS). Có nhắc thêm `KNOWLEDGE_BASE_ID`, `NEXT_PUBLIC_INCLUDE_LEFT_SIDEBAR`, `NEXT_PUBLIC_INCLUDE_RIGHT_SIDEBAR`.
- **Cấu hình trong code:** ID knowledge base và danh sách model nằm trong `ChatArea.tsx` (ví dụ mặc định `claude-haiku-4-5-20251001`).
- **Triển khai:** AWS Amplify, có build YAML riêng; service role cũng cần `AmazonBedrockFullAccess`.
- **Lưu ý:** README nói đây là prototype, "as-is", không dành cho sản xuất; khuyên chính sách IAM rộng (`AmazonBedrockFullAccess`), không đề xuất chính sách hẹp hơn; bước build Amplify ghi secret vào `.env`. README đánh số bước lặp (5, 5, 8, 8) và nhắc `.env.local` ở chỗ này nhưng `.env` ở chỗ khác.

### 2. financial-data-analyst
- **Làm gì:** Chat Next.js để Claude phân tích dữ liệu tài chính tải lên và vẽ biểu đồ (đường, cột, nhiều cột, vùng, vùng chồng, tròn). Chấp nhận file văn bản/code, PDF có chữ (PDF quét không hỗ trợ), ảnh.
- **Công nghệ:** Next.js 14, React, TailwindCSS, shadcn/ui, Recharts, PDF.js; API route chạy Edge Runtime; `@anthropic-ai/sdk` v1.x.
- **Yêu cầu:** Node.js 20+, Claude API key.
- **Chạy:**
  ```bash
  git clone https://github.com/anthropics/anthropic-quickstarts.git
  cd anthropic-quickstarts/financial-data-analyst
  npm install
  # tạo .env.local với ANTHROPIC_API_KEY=...
  npm run dev   # http://localhost:3000
  ```
- **Lưu ý:** URL clone trong README trỏ tới `anthropics/anthropic-quickstarts`, không phải `claude-quickstarts`; bạn nên clone từ repo thật rồi `cd` vào thư mục này. README nhắc model "Claude Haiku 4.5 & Claude Sonnet 5.5", không nêu model ID trong code. Không có cảnh báo bảo mật hay chi phí.

## Nhóm 2: computer use và browser use

### 3. computer-use-demo
- **Làm gì:** Tham chiếu computer use: desktop Linux trong Docker (X11 + VNC/noVNC), vòng lặp agent bằng Claude API, Bedrock hoặc Vertex, các công cụ computer use do Anthropic định nghĩa, giao diện Streamlit.
- **Model:** mặc định `claude-opus-4-8` (adaptive thinking); hỗ trợ nhiều model khác, kể cả Opus 4.7/4.6, Sonnet 4.6 và các model cũ hơn.
- **Yêu cầu:** Docker; API key Claude, hoặc AWS có Bedrock, hoặc Google Cloud có Vertex.
- **Chạy (Claude API):**
  ```bash
  export ANTHROPIC_API_KEY=%your_api_key%
  docker run \
      -e ANTHROPIC_API_KEY=$ANTHROPIC_API_KEY \
      -v $HOME/.anthropic:/home/computeruse/.anthropic \
      -p 5900:5900 -p 8501:8501 -p 6080:6080 -p 8080:8080 \
      -it ghcr.io/anthropics/anthropic-quickstarts:computer-use-demo-latest
  ```
  Bedrock dùng `-e API_PROVIDER=bedrock` cộng thông tin AWS; Vertex dùng `docker build . -t computer-use-demo`, `gcloud auth application-default login`, `-e API_PROVIDER=vertex`.
- **Truy cập:** http://localhost:8080 (UI gộp), :8501 (Streamlit), :6080/vnc.html (desktop), `vnc://localhost:5900`.
- **Biến môi trường:** `ANTHROPIC_API_KEY`, `API_PROVIDER`, `AWS_PROFILE`, `AWS_REGION`, `AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`, `AWS_SESSION_TOKEN`, `VERTEX_REGION`/`CLOUD_ML_REGION`, `VERTEX_PROJECT_ID`/`ANTHROPIC_VERTEX_PROJECT_ID`, `GOOGLE_APPLICATION_CREDENTIALS`, `WIDTH`, `HEIGHT`.
- **Phát triển:** `./setup.sh`, build `docker build . -t computer-use-demo:local`, mount thư mục `computer_use_demo` để sửa trực tiếp.
- **Kích thước màn hình:** nên dùng XGA (1024x768) trở xuống.
- **Cảnh báo (chi tiết nhất nhóm):** tính năng beta có rủi ro riêng; chạy trong VM/container ít quyền, không dùng dữ liệu nhạy cảm, đặt danh sách domain cho phép, người xác nhận hành động quan trọng; mô hình có thể làm theo chỉ dẫn trong nội dung trang/ảnh (prompt injection); phải báo rủi ro cho người dùng cuối. Vòng lặp agent chạy bên trong container được điều khiển, chỉ một phiên mỗi lần, cần reset giữa các phiên. API beta có thể đổi.

### 4. computer-use-best-practices
- **Làm gì:** Tham chiếu computer use trên **macOS**, chạy cục bộ không Docker. Mô hình điều khiển chuột, bàn phím, màn hình thật. Có công cụ trình duyệt Playwright, công cụ batch (`computer_batch`/`browser_batch`), `bash`/`python` trong sandbox `sandbox-exec`, ghi quỹ đạo vào `runs/<timestamp>/`, trình xem quỹ đạo Streamlit, demo FastAPI. Dùng để đọc và sửa, không phải thư viện.
- **Yêu cầu:** chỉ macOS; Python 3.11+ (python3 hệ thống 3.9 không dùng được); API key; cấp quyền Screen Recording và Accessibility cho terminal rồi khởi động lại hẳn; macOS 15+ hiện hộp thoại private window picker lần đầu và khoảng mỗi tháng. Tùy chọn `uv`. Vertex/Bedrock cần `pip install "anthropic[vertex]"` hoặc `"anthropic[bedrock]"`.
- **Cài:**
  ```bash
  python3.13 -m venv .venv
  source .venv/bin/activate
  python -m pip install --upgrade pip
  python -m pip install -r requirements.txt
  python -m playwright install chromium
  ```
- **Chạy:**
  ```bash
  python -m computer_use "open TextEdit and type hello world"
  python -m streamlit run dev_ui/trajectory_viewer/app.py
  python -m pytest
  ```
  Chỉ trình duyệt: `CU_ENABLE_COMPUTER_USE_TOOLS=false python -m computer_use "..."`.
- **Biến:** `ANTHROPIC_API_KEY` (bắt buộc), `CU_CONFIG`, `CU_<FIELD>` (ví dụ `CU_ENABLE_BROWSER_USE_TOOLS`, `CU_JPEG_QUALITY`, `CU_BROWSER_VIEWPORT`, `CU_USE_HOSTED_COMPUTER_TOOL`, `CU_ENABLE_ADVISOR_TOOL`).
- **Cờ:** `--model {claude-haiku-4-5,claude-sonnet-4-6,claude-opus-4-6,claude-opus-4-7}`, `--thinking {off,low,medium,high,max}`, `--max-iters N`, `--skip-preflight`.
- **Điểm nổi bật:** định nghĩa công cụ tường minh, đổi cỡ ảnh chụp theo tài liệu API, cắt tỉa ảnh biết cache, prompt caching, advisor tool (thử nghiệm, tắt mặc định), tự nén phía server (bật mặc định, chỉ Sonnet/Opus), toolset `computer_toolset_20260801` (chỉ API gốc).
- **Cảnh báo:** chỉ để học; chạy ngoài VM bị "khuyên mạnh là không nên", không có biện pháp chống ảnh chụp lộ dữ liệu nhạy cảm; nên dùng VM macOS dùng-một-lần (UTM, Parallels). Bộ phân loại prompt-injection chỉ chạy với công cụ computer do Anthropic định nghĩa, schema tường minh ở đây không qua bộ phân loại.
- **Chi phí:** mỗi ảnh chụp khoảng 1.500 token đầu vào; cache đọc khoảng 10% giá đầu vào; advisor tính phí riêng. Không có số đô la.

### 5. browser-use-demo
- **Làm gì:** Claude điều khiển Chromium không giao diện qua công cụ `browser` dùng Playwright (nhắm theo `ref` của DOM, đọc trang, nhập form, chạy JavaScript, chụp ảnh), chat Streamlit.
- **Công nghệ:** Python (Streamlit, Playwright, Chromium) trong Docker với XVFB, VNC, noVNC.
- **Yêu cầu:** Docker và Docker Compose; API key.
- **Chạy:**
  ```bash
  git clone https://github.com/anthropics/claude-quickstarts.git
  cd claude-quickstarts/browser-use-demo
  cp .env.example .env   # thêm ANTHROPIC_API_KEY
  docker-compose up --build
  docker-compose up --build --watch   # chế độ phát triển
  ```
- **Truy cập:** http://localhost:8080 (UI), http://localhost:6080 (noVNC), localhost:5900 (VNC). Màn hình 1920x1080.
- **Cảnh báo:** chạy trong VM/container ít quyền, không đưa dữ liệu nhạy cảm hay đăng nhập, cân nhắc danh sách domain cho phép, người xác nhận hành động quan trọng, rủi ro prompt injection, không dùng cho sản xuất. Google search gặp CAPTCHA, nên nêu rõ tên trang trong lời nhắc. Model mặc định không nêu.

### 6. browser-toolset
- **Làm gì:** Ví dụ CDP tối giản cho toolset trình duyệt `browser_toolset_20260801`, bản Python và TypeScript. Mô hình gọi từng thao tác như một công cụ, trình điều khiển chạy trong một tab Chromium. Cài 5 công cụ: `navigate`, `read_page`, `left_click`, `get_page_text`, `wait`, cộng `browser_state`. Ghi rõ "không phải code sản xuất".
- **Yêu cầu:** `ANTHROPIC_API_KEY`; `anthropic` 2.0+ hoặc `@anthropic-ai/sdk` 1.0+; Python 3.10+ hoặc Node 20+; Chromium (đặt `CHROME_PATH` hoặc có `google-chrome`/`chromium` trong PATH). Chromium snap của Ubuntu không mở được profile dưới `/tmp`, cần bản `.deb` hoặc không-snap.
- **Cài và chạy:**
  ```bash
  cd browser-toolset/python
  python -m venv .venv && source .venv/bin/activate
  pip install -r requirements.txt
  python run.py "Open example.com and tell me the heading"
  ```
  ```bash
  cd browser-toolset/typescript
  npm install
  npm run start -- "Open example.com and tell me the heading"
  ```
  Chạy không cần mô hình (không cần API key): `python exercise.py` hoặc `npm run exercise`.
- **Biến:** `ANTHROPIC_API_KEY` (cho `run`), `ALLOWED_DOMAINS` (mặc định `example.com,iana.org`; đặt rỗng thì không host nào được vào), `HEADLESS=0` để xem trình duyệt, `CHROME_PATH`, `MODEL`.
- **Lỗ hổng đã biết (README liệt kê):** không có ảnh chụp, cuộn, gõ, nhập form, tab, tải lên/xuống, chạy JS, click có phím bổ trợ; không chặn request nên chuyển hướng và tài nguyên con có thể tới host mà chính sách URL từ chối; hộp thoại có thể làm treo trình điều khiển; Ctrl-C để lại profile tạm của bản TypeScript.
- **Bảo mật:** dùng profile trình duyệt dùng-một-lần trong sandbox có kiểm soát đầu ra; đọc hướng dẫn "Running a browser toolset safely" của SDK.

### 7. computer-toolset
- **Làm gì:** Ví dụ VNC tối giản cho toolset máy tính `computer_toolset_20260801` (Python và TypeScript). Trình điều khiển cài 10 công cụ: screenshot, left_click, right_click, double_click, triple_click, mouse_move, scroll, type, key, wait. Ghi rõ "không phải code sản xuất".
- **Yêu cầu:** `ANTHROPIC_API_KEY` (cho `run`); `anthropic` 2.0+ hoặc `@anthropic-ai/sdk` 1.0+; Python 3.10+ hoặc Node 20+; máy chủ VNC không mật khẩu, màn hình không quá 1920×1200 (gợi ý `apt install tigervnc-standalone-server`).
- **Chạy:**
  ```bash
  Xvnc :1 -geometry 1280x800 -depth 24 -SecurityTypes None -localhost -rfbport 5900 &
  DISPLAY=:1 xterm -geometry 160x50 &
  ```
  ```bash
  cd computer-toolset/python
  python -m venv .venv && source .venv/bin/activate
  pip install -r requirements.txt
  python run.py "Open a terminal, run date, and tell me today's date and time zone"
  ```
  Bản TypeScript: `npm install` rồi `npm run start -- "..."`. Chạy không cần mô hình: `python exercise.py` hoặc `npm run exercise`.
- **Biến:** `ANTHROPIC_API_KEY`, `VNC_HOST` (mặc định `127.0.0.1`), `VNC_PORT` (mặc định `5900`), `MODEL` (mặc định `claude-sonnet-5-5`).
- **Đặc điểm:** trước mỗi thao tác khác chụp màn hình, `run` hỏi xác nhận `y`. Không có: zoom, kéo thả, middle_click, hold_key, VNC có mật khẩu, RFB cũ hơn 3.7, co dãn, đổi cỡ màn hình, giới hạn cho `wait`, tự kết nối lại.
- **Cảnh báo:** nội dung trên màn hình điều khiển hành động tiếp theo của mô hình và terminal đang focus chạy bất cứ thứ gì mô hình gõ, nên chỉ dùng desktop dùng-một-lần trong sandbox. VNC không mật khẩu nên giữ ở localhost; từ container chỉ publish ra loopback (`-p 127.0.0.1:5900:5900`).

## Nhóm 3: agent tự trị

### 8. autonomous-coding
- **Làm gì:** Khung chạy lập trình tự trị lâu dài bằng Claude Agent SDK, mô hình hai agent: phiên khởi tạo đọc `app_spec.txt`, viết `feature_list.json` gồm 200 test case, dựng dự án và khởi tạo git; các phiên lập trình sau đó làm từng tính năng và đánh dấu đạt.
- **Công nghệ:** Python, Claude Code CLI (npm), Claude Agent SDK.
- **Yêu cầu:** Claude Code CLI bản mới nhất, phụ thuộc Python từ `requirements.txt`, `ANTHROPIC_API_KEY`. Phiên bản Node và Python không nêu.
- **Chạy:**
  ```bash
  npm install -g @anthropic-ai/claude-code
  pip install -r requirements.txt
  export ANTHROPIC_API_KEY='your-api-key-here'
  python autonomous_agent_demo.py --project-dir ./my_project
  python autonomous_agent_demo.py --project-dir ./my_project --max-iterations 3   # thử giới hạn
  ```
- **Tùy chọn:** `--project-dir` (mặc định `./autonomous_demo_project`), `--max-iterations` (mặc định không giới hạn), `--model` (mặc định `claude-sonnet-4-5-20250929`).
- **Điểm nổi bật:** ngữ cảnh mới mỗi phiên, tiến độ lưu trong `feature_list.json` và git, tự tiếp tục sau 3 giây, Ctrl+C để tạm dừng và chạy lại cùng lệnh để tiếp tục. Phòng thủ nhiều lớp: sandbox cấp HĐH cho Bash, file giới hạn trong thư mục dự án, allowlist lệnh Bash (`ALLOWED_COMMANDS` trong `security.py`).
- **Cảnh báo:** README ghi "demo này chạy rất lâu": mỗi vòng 5 đến 15 phút, build đủ 200 tính năng cần "nhiều giờ"; phiên đầu có vẻ treo khi đang viết 200 tính năng là bình thường. Có thể giảm xuống 20–50 tính năng. Chi phí đô la không nêu. Giấy phép ghi "Internal Anthropic use" (khác với MIT của repo gốc, nên cần kiểm tra trước khi tái sử dụng).

## Nhóm 4: Managed Agents

> Hầu hết dự án dưới đây dùng `ant` CLI 2.0+ (`brew install anthropics/tap/ant`), `ant apply` để tạo agent/environment và lưu ID vào `claude-lock.json`, và đều có lệnh dẫn dắt `claude "walk me through setting this up"`. Riêng `sentry-autofix` ghi `ant` CLI 1.34+.

### 9. managed-agents/chat-sdk
- **Làm gì:** Nhà phân tích nghiên cứu trong cửa sổ chat trình duyệt. Vercel Chat SDK lo bề mặt chat; mỗi hội thoại ứng với một phiên Managed Agents bền vững; lệnh gọi công cụ hiện thành vệt có thể gập. Máy chủ không lưu trạng thái, ID hội thoại chính là ID phiên.
- **Công nghệ:** TypeScript/Node, Hono, React (`useChat`), esbuild.
- **Yêu cầu:** Node 22.9+; `ANTHROPIC_API_KEY` hoặc `ant auth login`. Phát token trực tiếp (`event_deltas`) bị chặn theo tổ chức trong đợt cập nhật 2026-07-01; không có thì trả lời hiện nguyên khối.
- **Chạy:**
  ```bash
  cd managed-agents/chat-sdk
  npm install
  cp .env.example .env
  npm run setup   # một lần; tạo agent và environment, dán ID in ra vào .env
  npm run dev     # http://localhost:3000
  ```
  `npm run update-agent` đẩy chỉnh sửa từ `setup/agent-config.ts`. Không chạy lại `npm run setup` để sửa (sẽ tạo agent trùng).
- **Biến:** `ANTHROPIC_API_KEY`, `CLAUDE_AGENT_ID`, `CLAUDE_ENVIRONMENT_ID`, `PORT` (3000), `HOST` (127.0.0.1), `QUICKSTART_MODEL`.
- **Cảnh báo:** hàm `getUser` mẫu trong `src/bot.ts` tin mọi người gọi, vì vậy mặc định chỉ bind loopback; phải thay bằng tra cứu phiên thật trước khi đặt `HOST=0.0.0.0`. Triển khai dùng một tiến trình sống lâu; route `/api/chat` mở suốt lượt nên timeout serverless vài giây là vấn đề.

### 10. managed-agents/copilot-kit-ag-ui
- **Làm gì:** Chat trợ lý tài chính cá nhân; Anthropic lưu trữ vòng lặp agent và container, CopilotKit dựng chat, trả lời phát từng token, agent vẽ biểu đồ tương tác nội tuyến (lịch trả nợ, tăng trưởng, ngân sách, so sánh kịch bản).
- **Công nghệ:** monorepo Node (npm workspaces): `runtime` (Express, :8787) và `web` (Vite, :5173); adapter `@ag-ui/claude-managed-agents`.
- **Yêu cầu:** Node 22+, `ant` CLI 2.0+, tín dụng Anthropic có bản beta Managed Agents; tổ chức giữ dữ liệu 30 ngày (`claude-fable-5` không dùng được khi zero data retention).
- **Chạy:**
  ```bash
  npm install
  ant apply agents environments   # một lần
  npm run dev                     # mở http://localhost:5173
  ```
  Khác: `npm run build`, `npm start`, `npm run typecheck`.
- **Biến:** `ANTHROPIC_API_KEY`, `ANTHROPIC_ENVIRONMENT_ID`/`ANTHROPIC_AGENT_ID`/`ANTHROPIC_AGENT_VERSION` (mặc định đọc từ `claude-lock.json`; đặt thiếu một phần gây lỗi khởi động), `PORT` (8787), `ALLOWED_ORIGINS`, `VITE_COPILOT_RUNTIME_URL`.
- **Cảnh báo:** endpoint chat không xác thực; mỗi tin nhắn tiêu tín dụng API nên cần đặt `ALLOWED_ORIGINS`, giữ URL riêng tư hoặc thêm xác thực. Container không có mạng ra ngoài; `web_fetch` tắt có chủ ý (đường prompt injection), `web_search` vẫn bật. Mỗi lượt giới hạn 5 phút. Bản đồ thread→phiên nằm trong bộ nhớ nên khởi động lại là phiên mới ("ổn cho demo, không cho sản xuất").

### 11. managed-agents/daily-brief
- **Làm gì:** Mỗi sáng ngày làm việc đọc kênh Slack và PR GitHub, chọn điều bạn nên xử lý và đăng một bản tin ngắn lên Slack. Chạy như một triển khai theo lịch (cron) của Managed Agents, không cần server.
- **Công nghệ:** tài nguyên YAML/Markdown áp dụng bằng `ant apply`; script shell (`bash`, `jq`, `curl`); Slack qua `curl`, GitHub qua MCP server.
- **Yêu cầu:** `ant` CLI 2.0+, `jq`; Slack app tạo từ manifest (token bot `xoxb-...`, quyền `channels:history`, `chat:write`; phải mời bot vào từng kênh nguồn và kênh đích); GitHub fine-grained PAT chỉ đọc (Contents, Pull requests).
- **Chạy:**
  ```bash
  cp .env.example .env        # điền hai token
  agents/setup.sh
  cp preferences.example.md preferences.md
  scripts/seed-preferences.sh preferences.md
  scripts/run.sh
  ant beta:deployments unpause --deployment-id <depl_ id do setup in ra>
  ```
  Dọn: `scripts/teardown.sh`; đặt lại trạng thái: `scripts/reset-state.sh`.
- **Điểm nổi bật:** dấu mốc theo từng nguồn nên chạy trễ không mất gì; sổ cái chống lặp; nguồn không đọc được thì báo là không đọc được thay vì "ngày yên tĩnh"; chỉ chuyển dấu mốc sau khi Slack xác nhận `"ok": true`. Lịch bắt đầu ở trạng thái tạm dừng.
- **Bảo mật:** agent đọc văn bản người khác viết nên có thể bị tiêm chỉ dẫn; token GitHub chỉ đọc là kiểm soát chính; quy tắc "chỉ đăng vào kênh đích" chỉ là quy tắc trong prompt, giới hạn thật là bot có mặt ở kênh nào. Mạng sandbox chỉ cho `slack.com` và MCP server GitHub; `web_search`/`web_fetch` tắt. Kênh riêng cần thêm `groups:history`.
- **Chi phí:** ngày bận (2 kênh, 2 repo, ~140 tin, 25 PR) khoảng $1,50 trên Opus 5 hoặc $1,00 trên Sonnet 5 (đo trước đây; model mặc định nay là Sonnet 5.5 nên cần kiểm lại); lượt đọc-không-được-gì $0,15–0,30. Trần mỗi lượt trong `deployment.md`: `amount: "500"` (cent) = $5; chạm trần thì dừng, trông như kênh im lặng.

### 12. managed-agents/knowledge-wiki
- **Làm gì:** Đọc một kho tài liệu một lần thành "wiki tri thức" (markdown trong memory store) bằng một lượt workflow động (trích xuất, giải quyết thực thể, phân tích, sắp xếp). Sau đó agent trả lời chỉ-đọc, mỗi dữ kiện có nhãn nguồn `[source | as-of]`, mâu thuẫn được giữ nguyên. Ví dụ: thương vụ Squarespace / Permira 2024 từ hồ sơ SEC EDGAR công khai (tải trực tiếp). Notebook chính: `distill_documents_into_knowledge_wiki.ipynb`.
- **Yêu cầu:** Python 3.11+, `anthropic` SDK 2.0+, Jupyter, quyền beta Managed Agents (mặc định bật cho tổ chức API), `EDGAR_USER_AGENT` có thông tin liên hệ của bạn.
- **Chạy:**
  ```bash
  pip install -r requirements.txt
  export EDGAR_USER_AGENT="your-name your-email"
  python3 fetch_data_room.py --tier=core
  jupyter lab distill_documents_into_knowledge_wiki.ipynb
  ```
  Tùy chọn: `fetch_real_deck.py`, `make_analyst_docx.py`.
- **Cấp độ dữ liệu:** `quickstart` (8 hồ sơ ngắn), `core` (8 hồ sơ, 2,8 MB, lượt đã ghi), `mini` (26), `standard` (37), `full` (42).
- **Biến:** `EDGAR_USER_AGENT`, `ANTHROPIC_API_KEY` (hoặc `ant auth login`, hoặc Workload Identity Federation), `COOKBOOK_DOCS`, `COOKBOOK_RECORDS_DIR`.
- **Bảo mật và giới hạn:** file Office từ phía đối tác là không tin cậy, nên chuyển đổi trong container; mỗi file memory store tối đa 100 KB; nhiều agent ghi chung trang có thể đè nhau (README thừa nhận khoảng 5% dòng ở trang thực thể bận nhất bị mất).
- **Chi phí:** lượt `core` đã ghi mất 23 phút, khoảng $16 theo giá niêm yết; chi phí build trung bình quanh $19. Haiku 5.5 cho agent đọc, Sonnet 5.5 cho agent chính. Với tier khác, notebook in ước tính và dừng nếu vượt ngân sách.
- **Tuyên bố hiệu quả của README (số liệu tự báo cáo, chưa kiểm):** model nhỏ trả lời trong khoảng một điểm so với model lớn tìm trong tài liệu gốc, với khoảng 1/15 giá mỗi câu trả lời; "hoàn vốn" sau khoảng 240 câu hỏi.

### 13. managed-agents/linear
- **Làm gì:** @mention hoặc giao issue Linear cho một Managed Agent và nhận câu trả lời dưới dạng bình luận. Cầu nối không lưu trạng thái: `metadata` của phiên (`linear_session_id`, `linear_org_id`) là trạng thái định tuyến duy nhất.
- **Công nghệ:** Bun/TypeScript, `@anthropic-ai/sdk` >= 1.0.0, Linear OAuth app (`actor=app`), tunnel HTTPS công khai (ví dụ ngrok).
- **Yêu cầu:** Bun (phiên bản không nêu), `ant` CLI 2.0+, tunnel, quyền admin workspace Linear, xác thực Anthropic.
- **Chạy:**
  ```bash
  cd managed-agents/linear
  bun install
  ant auth login
  ant apply agents environments
  cp .env.example .env   # rồi theo checklist trong skill.md cho phần Linear và webhook
  bun run dev
  ```
- **Luồng:** @mention → `/linear-webhook` → `sessions.create` → phiên chạy tới idle → `session.status_idled` → `/managed-agents/webhook` → trả lời đăng thành hoạt động agent trong Linear.
- **Cảnh báo bảo mật:** `/oauth/authorize` không có đăng nhập phía trước; workspace Linear **cài đầu tiên sẽ sở hữu cầu nối**, các lần cài khác bị từ chối và thu hồi. Nên đặt `LINEAR_ALLOWED_ORG_IDS` trong `.env`. Mỗi lần mention từ workspace đã cài chạy một phiên trên thông tin Anthropic của người vận hành. Nội dung issue là đầu vào không tin cậy. Tên biến OAuth của Linear không có trong README (xem `.env.example`).

### 14. managed-agents/mcp-server-typescript
- **Làm gì:** MCP server mỏng bọc Sessions API của Managed Agents để Claude Desktop, Claude Code hoặc claude.ai bắt đầu và trò chuyện với các agent sẵn có như công cụ. Có 9 công cụ: `list_agents`, `get_agent`, `create_session`, `send_message`, `interrupt`, `get_session`, `list_events`, `archive_session`, `wait_for_idle` (phát SSE tới khi idle và trả văn bản trả lời).
- **Công nghệ:** TypeScript/Bun, `@anthropic-ai/sdk` >= 1.0.0; truyền tải stdio và Streamable HTTP; có Dockerfile cho Fly, Railway, Render, Cloud Run.
- **Yêu cầu:** Bun, `ant` CLI 2.0+, xác thực Anthropic. **Không tạo agent**; cần có ít nhất một agent trong workspace (nếu chưa, chạy `./agents/setup.sh` ở `../slack` hoặc `../chat-sdk`).
- **Chạy (stdio):**
  ```bash
  cd managed-agents/mcp-server-typescript
  bun install
  ant auth login
  printf 'CLAUDE_ENVIRONMENT_ID=%s\n' \
    "$(ant beta:environments create --transform id --raw-output < environment.yaml)" >> .env
  claude mcp add managed-agents -- bun --env-file="$PWD/.env" run "$PWD/src/server.ts"
  ```
- **Biến:** `ANTHROPIC_API_KEY`, `CLAUDE_ENVIRONMENT_ID`, `ALLOWED_AGENT_IDS` (khuyến nghị), `ALLOWED_HOSTS` (bắt buộc trước khi dùng `HOST` khác loopback), `HOST`.
- **Cảnh báo bảo mật:** token bearer HTTP cho phép người giữ nó liệt kê, đọc và chạy **mọi agent trong workspace**, tiền tính vào thông tin Anthropic của server. Đặt `ALLOWED_AGENT_IDS` trước khi triển khai; server từ chối khởi động trên `HOST` khác khi chưa đặt `ALLOWED_HOSTS`.

### 15. managed-agents/roadtrip-planner
- **Làm gì:** App chat Next.js dựng trực tiếp trên phiên Managed Agent để lập lộ trình quanh các công viên quốc gia Mỹ, không dùng framework chat và không có CSDL (nhật ký sự kiện của phiên là danh sách tin nhắn). Trình diễn bốn tính năng: phát trực tiếp bằng `event_deltas`, thông tin xác thực trong vault với `injection_location` theo từng khóa, `agent_with_overrides` đổi model theo phiên, và agent điều phối đa agent nhờ agent kiểm duyệt (Opus) phê bình lộ trình.
- **Yêu cầu:** Node 20+, `ant` CLI 2.0+, `jq`, tổ chức có quyền Managed Agents; khóa API NPS (miễn phí, gửi email ngay) và khóa Windy Point Forecast (gói miễn phí).
- **Chạy:**
  ```bash
  cd managed-agents/roadtrip-planner
  npm install
  ant auth login
  cp .env.example .env   # điền NATIONAL_PARK_SERVICE_API_KEY và WINDY_API_KEY
  ./agents/setup.sh
  npm run dev            # http://localhost:3000
  ```
  `./agents/teardown.sh` lưu trữ mọi thứ và xóa `claude-lock.json`.
- **Cách tiêm khóa:** NPS → host `developer.nps.gov`, tiêm vào header (`X-Api-Key`); Windy → host `api.windy.com`, tiêm vào body (`"key": ...`).
- **Bảo mật:** không có tài khoản người dùng, cookie gắn một trình duyệt với một phiên, nên chạy ở localhost; mọi route kiểm tra quyền sở hữu phiên, `src/proxy.ts` kiểm tra `Host`/`Origin`/`Sec-Fetch-Site` chống POST chéo trang và DNS rebinding. Phải thêm xác thực thật trước khi mở ra ngoài. Giữ allowlist host của thông tin xác thực chính xác, không dùng ký tự đại diện.
- **Chi phí:** không nêu; chỉ biết agent tự giới hạn khoảng năm lệnh curl mỗi câu hỏi.

### 16. managed-agents/sentry
- **Làm gì:** Agent theo lịch dùng MCP server Sentry (mcp.sentry.dev) để xếp hạng issue chưa giải quyết trong 24 giờ qua, nhờ Seer phân tích gốc rễ khi có, rồi viết báo cáo một trang `TRIAGE_REPORT.md`. Lịch mặc định `0 9 * * 1-5` (ngày làm việc, 9 giờ sáng giờ Đông Mỹ). Không có tiến trình nào chạy trên máy bạn.
- **Công nghệ:** Managed Agents, Sentry MCP, Python (`uv`, file `.py`; ngôn ngữ suy ra từ file), `anthropic` >= 2.0.0.
- **Yêu cầu:** Claude Code, `uv`, `ant` CLI 2.0+, `jq`, tài khoản Sentry có quyền vào tổ chức/dự án.
- **Chạy:**
  ```bash
  cd managed-agents/sentry
  ./start.sh                  # có hướng dẫn
  # hoặc thủ công:
  ant auth login
  uv sync
  ./agents/setup.sh --org <org-slug> --project <project-slug>
  uv run python deploy.py     # đặt lịch
  uv run python run_now.py    # chạy tay, tải báo cáo về reports/<session_id>/
  ```
- **Điểm nổi bật:** chỉ đọc; allowlist bốn công cụ MCP (`search_issues`, `search_events`, `get_sentry_resource`, `analyze_issue_with_seer`); phân loại issue mới/hồi quy/leo thang/đang diễn ra và xếp theo số người dùng bị ảnh hưởng; nếu Seer không có thì nói rõ và dùng giả thuyết có nhãn.
- **Lưu ý:** ở màn hình phê duyệt Sentry chỉ để "Inspect Issues & Events" và "Seer", bỏ "Triage Issues" và "Manage Projects & Teams". Sau khi `ant apply` xuất bản phiên bản agent mới, kiểm tra trên Console rằng bốn công cụ vẫn là "always allow", nếu rơi về `always_ask` thì lượt chạy theo lịch bị treo.
- **Hạn chế đã biết:** tổ chức bật SSO bắt buộc hoặc từ chối token OAuth gắn với người dùng sẽ lỗi `mcp_authentication_failed_error` hoặc 403 (vault chỉ gửi `Authorization: Bearer`, còn server cần `Sentry-Bearer` cho token tổ chức). README chỉ tới bản cũ (`git show 97c825e:managed-agents/sentry/README.md`) dùng sentry-cli và token tổ chức làm cách tạm. Trần chi phí và giá: không nêu.

### 17. managed-agents/sentry-autofix
- **Làm gì:** Lỗi Sentry mới kích hoạt một phiên Managed Agents: đọc stack trace và RCA của Seer, viết test thất bại trong bản sao repo của bạn, sửa lỗi và mở PR có nội dung `Fixes SHOP-1A`. Người duyệt và merge; Sentry giải quyết issue khi có bản phát hành chứa commit merge. Host khoảng 600 dòng TypeScript, không lưu trạng thái. `demo-app/` là dịch vụ checkout Express có lỗi cố ý (giỏ hàng không có mã giảm giá trả 500).
- **Yêu cầu:** Claude Code, Node 22.9+, `ant` CLI 1.34+, `jq`, tổ chức Sentry (Seer là add-on trả phí; không có Seer thì agent làm từ stack trace và nói rõ trong PR), repo GitHub có **ruleset** yêu cầu PR ở nhánh mặc định (quy tắc bảo vệ nhánh cổ điển không được chấp nhận), token GitHub fine-grained giới hạn một repo (Contents và Pull requests: đọc/ghi, tắt Workflows). Với webhook: Sentry internal integration đăng ký resource `issue`, webhook trỏ tới tunnel vào cổng 3000, Client Secret đặt vào `SENTRY_CLIENT_SECRET`.
- **Chạy:**
  ```bash
  cd managed-agents/sentry-autofix
  ./start.sh                          # có hướng dẫn
  # hoặc thủ công:
  ant auth login
  npm install
  ./agents/setup.sh
  $EDITOR .env                        # GITHUB_REPO_URL, GITHUB_TOKEN, SENTRY_CLIENT_SECRET
  npm run fix -- SHOP-1A              # sửa một issue theo short ID, không cần webhook
  npm run dev                         # nghe http://localhost:3000/webhooks/sentry
  ```
- **Biến:** `ANTHROPIC_API_KEY`, `GITHUB_REPO_URL`, `GITHUB_TOKEN`, `SENTRY_CLIENT_SECRET`, `AUTOFIX_MAX_USD` (mặc định $10), `AUTOFIX_MAX_ACTIVE` (mặc định 3), `HOST` (mặc định loopback), `GITHUB_BASE_BRANCH` (vai trò không nêu rõ).
- **Điểm nổi bật:** webhook gửi lại không khởi động bản sửa thứ hai; `open_pull_request` là công cụ tùy chỉnh do host trả lời bằng token GitHub của chính host; thông tin xác thực được tiêm qua git proxy và MCP proxy, phiên dùng được nhưng không đọc được. Chỉ bật năm công cụ Sentry theo allowlist, nên agent không giải quyết hay giao lại issue được. Đăng nhập Sentry yêu cầu ba scope `org:read`, `project:write`, `event:write`.
- **Bảo mật:** shell chạy không cần duyệt từng lệnh vì phiên webhook không có người duyệt; bốn kiểm soát giới hạn tác hại của chỉ dẫn bị tiêm: ruleset PR bắt buộc (server thoát ngay khi khởi động nếu không có), kiểm tra PR phía host, cô lập thông tin xác thực, hạn chế đầu ra (chỉ GitHub, kho gói, MCP server Sentry; công cụ web tắt). Host từ chối tiêu đề/nội dung PR sẽ đóng issue khác, và nhánh sửa file dưới `.github/`. `GET /` liệt kê các bản sửa không cần xác thực; chỉ lộ `/webhooks/sentry` qua tunnel.
- **Chi phí:** trần cứng mỗi phiên `AUTOFIX_MAX_USD` (phiên chạm trần sẽ tạm dừng); `AUTOFIX_MAX_ACTIVE` giới hạn đồng thời, issue thừa bị ghi log và bỏ qua. Seer là add-on trả phí. Cùng hạn chế SSO như dự án `sentry`.

### 18. managed-agents/slack
- **Làm gì:** @mention một Managed Agent trong Slack và nhận trả lời ngay trong thread. Cầu nối không trạng thái, `metadata` của phiên (`slack_channel`, `slack_thread_ts`) là trạng thái định tuyến duy nhất, không CSDL.
- **Luồng:** @mention → `/slack/events` → `sessions.create` kèm metadata (trả 204) → khi phiên phát `session.status_idled` thì webhook `/managed-agents/webhook` đọc metadata và gọi `chat.postMessage`.
- **Công nghệ:** Bun/TypeScript (suy ra từ file `.ts`), `@anthropic-ai/sdk` >= 1.0.0.
- **Yêu cầu:** Bun, `ant` CLI 2.0+, tunnel HTTPS công khai (ví dụ ngrok), xác thực Anthropic, Slack app (phạm vi quyền và các bước nằm trong `skill.md`, chưa đọc).
- **Chạy:**
  ```bash
  cd managed-agents/slack
  bun install
  ant auth login
  ant apply agents environments
  cp .env.example .env   # rồi theo checklist trong skill.md cho phần Slack và webhook
  bun run dev
  ```
- **Lưu ý:** Slack kiểm tra Request URL ngay khi lưu, nên **server phải chạy trước**. Xác minh chữ ký Slack và xử lý `url_verification`; dùng `beta.webhooks.unwrap` để xác minh webhook Anthropic. Tên các biến Slack signing secret, bot token và webhook secret không có trong README. Không có cảnh báo bảo mật hay chi phí khác.

---

## Điểm cần biết khi chọn dự án

- Mọi dự án Managed Agents cần quyền beta Managed Agents và `ant` CLI; các dự án `copilot-kit-ag-ui`, `chat-sdk` và `knowledge-wiki` có yêu cầu phiên bản riêng (Node 22+, Node 22.9+, Python 3.11+).
- Một số dự án (`copilot-kit-ag-ui`, `chat-sdk`, `roadtrip-planner`) không có xác thực người dùng; không đưa ra internet khi chưa thêm.
- Dự án computer use và browser use đều khuyến cáo VM/container dùng-một-lần và coi nội dung trang/màn hình là không tin cậy.
- Các README có vài điểm không nhất quán đã ghi chú ở trên (clone nhầm repo ở `financial-data-analyst`, đánh số bước ở `customer-support-agent`, giấy phép "Internal Anthropic use" ở `autonomous-coding`).
- Chưa kiểm chứng bằng cách chạy: toàn bộ lệnh ở đây lấy từ README, chưa chạy thử.
