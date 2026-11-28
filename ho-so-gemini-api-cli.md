# Hồ sơ: google-gemini/gemini-api-cli

- Ngày lập: 2026-11-27
- URL: https://github.com/google-gemini/gemini-api-cli
- Nguồn: trang repo, README, các thư mục `cmd`, `docs/self-hosted`, `evals/harness-comparison`, `tests/contract`, `LICENSE`, `CONTRIBUTING.md`. Mục ghi **[chưa xác minh]** là chưa đọc được từ nguồn.
- Lưu ý: ảnh chụp màn hình hiển thị 3,8k sao, 275 fork, 18 theo dõi, 7 issue, 43 PR; khi tôi đọc trang thì là 4,2k sao, 302 fork, 21 theo dõi, 9 issue, 45 PR. Số liệu đổi theo thời điểm.

## Tổng quan

| Mục | Nội dung |
|---|---|
| Mô tả (About) | "An (experimental) CLI for the Gemini API" |
| Mục đích (README) | Đưa mô hình Gemini và managed agents cho agent bạn đang dùng. CLI Go không trạng thái (`gemini-api`) cho các agent lập trình có quyền shell (Codex, Claude Code, Antigravity, OpenClaw, Hermes...) gọi Gemini API |
| Giấy phép | Apache-2.0 (bản quyền 2026 Google LLC); tài liệu phi phần mềm theo CC BY 4.0 |
| Ngôn ngữ | Go (cần Go 1.26.10+ cho `main`); TypeScript/Node và Python trong phần evals; script cài đặt shell/PowerShell. Tỷ lệ phần trăm **[chưa xác minh]** |
| Thống kê | 4,2k sao, 302 fork, 21 theo dõi, 9 issue, 45 PR, 225 commit trên `main`. Số nhánh, số tag, ngày commit cuối **[chưa xác minh]** |
| Mức trưởng thành | README ghi **beta**, "có thể có thay đổi phá vỡ giữa các bản phát hành", khuyên ghim phiên bản trong CI |
| Đóng góp | **Không nhận PR bên ngoài** (PR bị đóng không xem xét); phản hồi qua Issues |

## Chức năng

Giúp agent làm các việc sau bằng lệnh shell: tạo văn bản, ảnh, giọng nói, nhạc, video; phân tích tệp; phiên âm; chạy managed agents ở chế độ nền.

### Lệnh (theo bảng trong README)

- **Tạo nội dung:**
  - `generate`: văn bản (model mặc định `gemini-4-hydrogen`), cờ `-m`, `-i/--input`, `--stdin`, `--system`, `--stream=false`, `--body`.
  - `image`: ảnh (`gemini-nano-banana-2.1`), cờ `--out`.
  - `tts`: giọng nói (`gemini-3.8-flash-tts`), cờ `--voice`, `--voice-prompt`, `--style`, `--multi-speaker`, `--out`.
  - `music`: nhạc (`lyria-3.5`).
  - `video`: video (`gemini-omni-1.2-flash`), cờ `--async`.
- **Hiểu nội dung:**
  - `analyze`: PDF, ảnh, âm thanh, video, CSV/văn bản, URL YouTube; `--input` lặp được.
  - `transcribe`: phiên âm (`gemini-3.5-transcribe`), định dạng `md|text|json|srt`.
- **Quản lý:**
  - `agent` (run, status, cancel, delete-interaction, create, list, get, delete).
  - `files` (upload, list, get, generated-files-list, register, delete; lưu trữ 48 giờ).
  - `models`, `voices`, `configure`, `auth`/`whoami`.
  - `install-skill` (xem bên dưới).
- **Nâng cao:** `environments`, `credentials`, `webhooks`, `triggers`.
- **Tiện ích:** `explore`, `version`.
- **Cờ chung/khám phá:** `--help`, `--help-global`, `--usage` (cây lệnh KDL), `--schema` (JSON Schema cho `--body`), `--dry-run`, `--no-interactive`, `--agent-mode`, `--output-format json|toon`, `--jq`, `--stream=false`, `--body`, `--raw-response`, `--background`.
- **Mã thoát:** 0 thành công, 1 lỗi chạy/API, 2 sai cú pháp/xác thực đầu vào, 3 lỗi xác thực.

### Ví dụ (từ README)

```bash
gemini-api generate "Hello from my agent" --dry-run
gemini-api image "A friendly robot mascot for a developer tool" --out ./assets/
gemini-api analyze --input before.png --input after.png "Summarize the visual design changes"
gemini-api transcribe --input interview.mp4 --format srt --out interview.srt
gemini-api agent run "<prompt>" --agent deep-research-preview-04-2026 --background --jq '.id'
gemini-api agent status "$INTERACTION_ID" --stream=false --output-format json
gemini-api agent cancel "$INTERACTION_ID"
gemini-api models list --all
```

## Cài đặt

```bash
# macOS/Linux
curl -fsSL https://raw.githubusercontent.com/google-gemini/gemini-api-cli/main/scripts/install.sh | bash
```

```powershell
# Windows PowerShell
iwr -useb https://raw.githubusercontent.com/google-gemini/gemini-api-cli/main/scripts/install.ps1 | iex
```

```bash
# Go (dùng @main cho bản phát triển; cần Go 1.26.10+)
go install github.com/google-gemini/gemini-api-cli/cmd/gemini-api@latest
```

Hoặc tải gói dựng sẵn từ GitHub Releases rồi đặt `gemini-api` vào PATH. Lưu ý: các lệnh `curl | bash` và `iwr | iex` chạy script từ xa, nên đọc script trước khi chạy.

## Xác thực

- Tạo khóa ở Google AI Studio, đặt `export GEMINI_API_KEY="YOUR_API_KEY"`.
- Lưu lâu dài (tùy chọn): `gemini-api configure --api-key "..."` hoặc `gemini-api configure --interactive`; lưu vào kho khóa HĐH (macOS Keychain, Linux Secret Service, Windows Credential Manager) hoặc `~/.config/gemini-api/config.yaml`. Kiểm tra bằng `gemini-api whoami`. Có thêm `auth login`, `auth whoami`, `auth logout`.
- Biến môi trường được nêu: `GEMINI_API_KEY`, `GEMINI_CLI_AGENT_MODE=1` (như `--agent-mode`), `GEMINI_ENVIRONMENT_KEY` (worker tự lưu trữ), `GOOGLE_GEMINI_BASE_URL`, `EVAL_GEMINI_API_KEY`, `GEMINI_CONFIG_DIR`, `XDG_CONFIG_HOME`. Danh sách đầy đủ **[chưa xác minh]** (xem bằng `--usage`).

## Tính năng `install-skill`

Cài skill `gemini-api-cli` (nhúng sẵn trong file nhị phân; nguồn ở `github.com/google-gemini/gemini-skills`, `skills/gemini-api-cli`) để agent biết dùng CLI.

- Chế độ tương tác hỏi cài cho agent nào (README nêu Antigravity, Gemini CLI, Claude Code, Codex, Cursor "và nhiều hơn") và cài trong dự án hay thư mục home.
- Không tương tác: `--agent <danh sách>` (hoặc `all`), `--global`, `--dry-run` để xem trước.
- Agent không nạp được skill thì README cho một đoạn văn bản để dán vào `AGENTS.md` / `CLAUDE.md` / `.cursorrules`.
- Danh sách agent hỗ trợ đầy đủ **[chưa xác minh]**.

## Cấu trúc repo

- `.github/workflows/`: CI (gồm workflow `harness-eval`).
- `cmd/`: `gemini-api` (CLI) và `gendocs` (mục đích không nêu ngoài tên).
- `internal/`: **[chưa xác minh]**.
- `scripts/`: `install.sh`, `install.ps1`.
- `docs/self-hosted/`: hướng dẫn môi trường tự lưu trữ.
- `evals/harness-comparison/`: bộ đánh giá so sánh harness.
- `tests/contract/`: 26 file kiểm thử hợp đồng bằng Go (ví dụ `cli_contract_test.go`, `exitcodes_test.go`, `install_skill_test.go`, `dryrun_everywhere_test.go`, `readme_examples_test.go`, `error_taxonomy_test.go`).
- Gốc: `README.md`, `USAGE.md` (chưa đọc), `CONTRIBUTING.md`, `LICENSE`, `.goreleaser.yaml`, `go.mod`, `go.sum`. **Không có `SECURITY.md`** trên `main` dù thanh bên GitHub có nhãn "Security policy" (đó là liên kết chung của GitHub).

## Môi trường tự lưu trữ (`docs/self-hosted`)

Cho phép agent phía máy chủ Gemini API chạy công cụ tích hợp (`execute_bash`, đọc/ghi/sửa tệp, `list_dir`, `grep_search`, `find_by_name`) trong hạ tầng của bạn, chỉ dùng HTTPS đi ra.

- Hai chế độ: `environments connect` (một worker) và `environments poll` + `environments serve` (mặt phẳng điều khiển giữ khóa, worker sandbox chỉ nhận token thuê).
- Thư mục con: `local/` (không an toàn để mở ra máy chủ), `containers/` (Docker, Podman), `agent-substrate/` (Kubernetes), `providers/` (Vercel, Daytona, E2B, Modal, Fly.io, Cloud Run, Cloudflare).
- **Cảnh báo:** luôn cô lập `execute_bash` trong container, microVM hoặc VM. Tài liệu ghi các mẫu là "bản triển khai tham chiếu, không phải sản phẩm Google được hỗ trợ chính thức".

## Evals (`evals/harness-comparison`)

Đo harness CLI nào giúp agent lập trình gọi đúng API với ít lượt nhất, so CLI sinh tự động (Speakeasy, chính là CLI này) với CLI viết tay tham chiếu. Dùng máy chủ giả lập Gemini Interactions API, trình điều khiển Antigravity SDK (Python), công cụ duy nhất `run_command`. Bảy kịch bản: create/list/get/delete-agent, run-agent-background, interaction-status, cancel-interaction.

- Chạy: `npm install`, `npm run setup`, `npm run eval`; cần `EVAL_GEMINI_API_KEY`. Mỗi lượt chạy đủ là 22 phiên agent thật, **tốn token**.
- Chạy trên mọi PR qua `.github/workflows/harness-eval.yaml` (bỏ qua với PR từ fork).

## Yêu cầu, chi phí, bảo mật

- **Yêu cầu:** khóa Gemini API từ AI Studio; agent có quyền shell; Go 1.26.10+ chỉ khi build từ mã nguồn; PowerShell cho trình cài Windows.
- **Chi phí/gói miễn phí:** **[chưa xác minh]** (README không nêu). Evals tốn token thật. Tệp tải lên giữ 48 giờ. Interaction được lưu phía máy chủ trừ khi đặt `"store": false`.
- **Bảo mật:** `--dry-run` in yêu cầu với thông tin xác thực đã che, không gọi mạng và không đọc kho khóa. CLI không giữ trạng thái hội thoại cục bộ. Khi gửi báo lỗi, không đưa `GEMINI_API_KEY`.

## Đánh giá

- **Phù hợp:** người chạy agent lập trình (Claude Code, Codex...) muốn gọi mô hình Gemini, tạo media, phân tích tệp hoặc chạy managed agents nền từ shell.
- **Không phù hợp:** pipeline sản xuất cần API ổn định (đang beta), hoặc người muốn đóng góp mã (không nhận PR).
- **Lưu ý tên model:** các tên như `gemini-4-hydrogen`, `gemini-omni-1.2-flash`, `lyria-3.5` lấy nguyên từ README; chưa kiểm chứng chúng có khả dụng hay không.
- **Chưa xác minh:** số nhánh/tag, ngày commit cuối, tỷ lệ ngôn ngữ, nội dung `USAGE.md` và `internal/`, mục đích `gendocs`, giá và hạn mức miễn phí.
