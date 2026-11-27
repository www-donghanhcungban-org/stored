# Hồ sơ: anthropics/claude-agent-sdk-demos

- Ngày lập: 2026-11-27
- URL: https://github.com/anthropics/claude-agent-sdk-demos
- Nguồn: trang repo, README gốc, README của 8 thư mục demo. **[chưa xác minh]** là chưa đọc được từ nguồn.

## Tổng quan

| Mục | Nội dung |
|---|---|
| Mô tả | "Claude Code SDK Demos" |
| Giấy phép | MIT theo README ("MIT - mã mẫu để minh họa"); huy hiệu giấy phép trên GitHub không hiển thị |
| Thống kê | 2,8k sao, 450 fork, 27 theo dõi, 13 issue mở, 24 PR mở, 69 commit. Ngày commit cuối và ngôn ngữ **[chưa xác minh]** |
| Yêu cầu chung | Bun (hoặc Node.js 18+), khóa API Anthropic |
| Chính sách đóng góp | **[chưa xác minh]** (không thấy `CONTRIBUTING`) |
| Chi phí | Không nêu, ngoài việc cần khóa API (phí theo mức dùng) |

**Cảnh báo (README gốc):** đây là ứng dụng demo, chỉ dùng phát triển cục bộ, **không** triển khai lên sản xuất hay dùng quy mô lớn; cung cấp nguyên trạng. Bắt đầu: `git clone https://github.com/anthropics/claude-agent-sdk-demos.git`, `cd claude-agent-sdk-demos`, vào thư mục demo rồi làm theo README.

**Lưu ý về liên kết:** link "Demo Issues" ở README gốc và đường dẫn clone trong README của `email-agent`, `excel-demo` trỏ tới `anthropics/sdk-demos`, không phải tên repo này. Có thể là liên kết cũ.

## 8 demo

### 1. email-agent (README gốc ghi đang phát triển)
- **Làm gì:** Máy khách email IMAP kiêm trợ lý: hiển thị hộp thư, tìm thư kiểu agent, hỗ trợ AI.
- **Yêu cầu:** Bun hoặc Node.js 18+; khóa API Anthropic; tài khoản email bật IMAP (Gmail cần App Password).
- **Chạy:**
  ```bash
  cp .env.example .env
  bun install   # hoặc npm install
  bun run dev   # hoặc npm run dev; mở http://localhost:3000
  ```
- **Biến:** `ANTHROPIC_API_KEY`, `EMAIL_USER`, `EMAIL_PASSWORD`, `IMAP_HOST`, `IMAP_PORT` (ví dụ `imap.gmail.com`, `993`).
- **Cảnh báo:** chỉ chạy cục bộ trên máy cá nhân; mật khẩu email lưu dạng văn bản thường trong biến môi trường; không có xác thực hay đa người dùng.

### 2. excel-demo
- **Làm gì:** Ứng dụng desktop Electron để AI tạo, phân tích, chỉnh sửa Excel; có ví dụ Python (theo dõi tập luyện, theo dõi ngân sách).
- **Công nghệ:** Electron, React, Node/Bun, Python 3.9+ với openpyxl.
- **Yêu cầu:** Node.js 18+ hoặc Bun; khóa API; Python 3.9+ cho ví dụ Python; LibreOffice (tùy chọn, tính lại công thức).
- **Chạy:**
  ```bash
  npm install   # hoặc bun install
  npm start     # hoặc bun start
  ```
  Ví dụ Python:
  ```bash
  cd agent
  python -m venv .venv
  source .venv/bin/activate
  pip install -r requirements.txt
  python create_workout_tracker.py
  python create_budget_tracker.py
  ```
- **Biến:** `ANTHROPIC_API_KEY` (hoặc ứng dụng hỏi lần đầu).

### 3. hello-world (TypeScript)
- **Làm gì:** Ví dụ nhập môn `query()` và agent có hook `PreToolUse` giới hạn ghi `.js`/`.ts` vào `agent/custom_scripts`.
- **Chạy:**
  ```bash
  npm install @anthropic-ai/claude-agent-sdk typescript @types/node tsx zod
  export ANTHROPIC_API_KEY="your-api-key"
  mkdir -p agent/custom_scripts
  npx tsx hello-world.ts
  ```
- **Lỗi thường gặp:** `spawn node ENOENT` thì đặt `executable: "node"`.

### 4. hello-world-v2 (TypeScript)
- **Làm gì:** Ví dụ Session API V2 (`unstable_v2_*`): `send()`/`stream()`, nhiều lượt, khôi phục phiên, prompt một lần.
- **Chạy:**
  ```bash
  npm install
  npx tsx v2-examples.ts basic        # hoặc multi-turn, one-shot, resume
  ```
- **Cảnh báo:** API ghi tiền tố `unstable_v2_`, tức chưa ổn định. Yêu cầu và biến môi trường **[chưa xác minh]**.

### 5. research-agent (Python)
- **Làm gì:** Hệ thống nghiên cứu đa agent: agent chính sinh các subagent nghiên cứu, phân tích dữ liệu và viết báo cáo chạy song song; xuất báo cáo PDF và biểu đồ; theo dõi hoạt động subagent bằng hook; có lệnh `/research`, `/competitive-analysis`, `/market-trends`, `/fact-check`, `/summarize`.
- **Yêu cầu:** `uv`, `ANTHROPIC_API_KEY`. Phiên bản Python **[chưa xác minh]**.
- **Chạy:**
  ```bash
  uv sync
  export ANTHROPIC_API_KEY="your-api-key"
  uv run python research_agent/agent.py
  ```

### 6. ask-user-question-previews (TypeScript/React)
- **Làm gì:** Trợ lý thương hiệu, các lựa chọn của `AskUserQuestion` hiển thị thành thẻ xem trước HTML (`previewFormat: "html"`), truyền qua WebSocket bằng `canUseTool`.
- **Công nghệ:** máy chủ HTTP Node với `ws` và `tsx`; React 18 + Vite; DOMPurify; react-markdown.
- **Yêu cầu:** Node.js 18+; khóa API Anthropic hoặc phiên `claude login` có sẵn.
- **Chạy:**
  ```bash
  npm install
  cp .env.example .env   # chỉ khi không dùng claude login
  npm run dev            # mở http://localhost:5173
  ```
- **Ghi chú:** demo một lần; xem trước có thể chậm.

### 7. simple-chatapp (React + Express)
- **Làm gì:** Giao diện chat dùng SDK, phát trực tiếp qua WebSocket.
- **Yêu cầu:** Node.js 18+; `ANTHROPIC_API_KEY`.
- **Chạy:** `npm install`, `npm run dev`; backend http://localhost:3001, frontend http://localhost:5173.
- **Lưu ý khi đưa lên sản xuất (README liệt kê):** cô lập SDK trong container (agent có quyền Bash, hệ thống tệp, web); thay `ChatStore` trong bộ nhớ bằng CSDL (restart là mất chat); lưu bản ghi hội thoại; thêm xác thực (hiện ai cũng truy cập được mọi chat).

### 8. resume-generator
- **Làm gì:** Tạo bản CV một trang `.docx` bằng cách tìm kiếm web về một người được nêu tên (LinkedIn, GitHub, tin tức).
- **Công nghệ:** Node/JavaScript, thư viện `docx`, Claude Agent SDK với WebSearch.
- **Chạy:**
  ```bash
  npm install
  npm start "Person Name"
  ```
- **Đầu ra:** `agent/custom_scripts/resume.docx`.
- **Lưu ý:** công cụ tra cứu thông tin về người thật qua web, nên cân nhắc về quyền riêng tư; README không nêu yêu cầu khóa API hay giấy phép riêng.

## Đánh giá
- **Phù hợp:** người học Claude Agent SDK, chạy demo cục bộ.
- **Không phù hợp:** sản xuất, lưu trữ nhiều người dùng, xử lý thông tin nhạy cảm (đặc biệt `email-agent`).
- **Chưa xác minh:** ngôn ngữ repo, ngày commit cuối, chính sách đóng góp, chi phí từng demo, giấy phép riêng của các demo ngoài `email-agent` và `excel-demo` (README thư mục không nêu), yêu cầu của `hello-world-v2` và `resume-generator`.
