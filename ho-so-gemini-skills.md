# Hồ sơ: google-gemini/gemini-skills

- Ngày lập: 2026-11-27
- URL: https://github.com/google-gemini/gemini-skills
- Nguồn: trang repo, README, thư mục gốc và `skills/`, `SKILL.md` của `gemini-api-cli` và `gemini-api-dev`. Hai skill còn lại chưa mở. **[chưa xác minh]** là chưa đọc được từ nguồn.

## Tổng quan

| Mục | Nội dung |
|---|---|
| Mô tả | "Skills cho Gemini API, SDK và tương tác model/agent" |
| Mục đích | Thư viện skill đưa ngữ cảnh Gemini API cập nhật cho agent lập trình |
| Giấy phép | Apache-2.0 |
| Ngôn ngữ | Không nêu (phần Languages không hiển thị); nội dung có ví dụ SDK Python và TypeScript |
| Thống kê | 4,8k sao, 519 fork, 48 theo dõi, 5 issue, 10 PR, 183 commit. Ngày commit cuối **[chưa xác minh]** |
| Đóng góp | **[chưa xác minh]** (không thấy `CONTRIBUTING`) |
| Chính sách bảo mật | Có liên kết trên trang repo |

**Tuyên bố hiệu quả (do bên phát hành nêu, chưa kiểm chứng):** README cho biết khi dùng skill, mã API đúng đạt 87% với Gemini 3 Flash và 96% với Gemini 3.1 Pro.

**Miễn trừ (README):** không phải sản phẩm được Google hỗ trợ chính thức và không đủ điều kiện nhận thưởng lỗ hổng của chương trình Google Open Source Software Vulnerability Rewards.

## Cấu trúc

`.agents/plugins`, `.claude-plugin`, `.codex-plugin`, `.cursor-plugin`, `skills/`, `LICENSE`, `README.md`, `plugin.json`. Skill `vertex-ai-api-dev` đã chuyển sang `github.com/google/skills` (`skills/cloud/gemini-api`).

## Các skill (4 thư mục trong `skills/`)

- **gemini-api-dev:** xây ứng dụng bằng Gemini API (Interactions và Decisions API): văn bản, chat, streaming, gọi hàm, đầu ra có cấu trúc, ảnh/TTS/giọng nói, Deep Research, managed agents, SDK Python và TypeScript.
- **gemini-api-cli:** gọi Gemini API từ shell bằng CLI `gemini-api` (ảnh, tts, nhạc, video, phân tích, phiên âm, Deep Research, sandbox cho agent). Hồ sơ riêng của CLI: `ho-so-gemini-api-cli.md`.
- **gemini-live-api-dev:** ứng dụng streaming hai chiều thời gian thực bằng Gemini Live API (WebSocket âm thanh/video/văn bản, VAD, gọi hàm). Chỉ biết mô tả, chưa mở `SKILL.md`.
- **gemini-omni-flash-api:** tạo và chỉnh sửa video với Gemini Omni 1.2 Flash qua Interactions API. Chỉ biết mô tả, chưa mở `SKILL.md`.

**Định dạng (đã xác nhận):** mỗi skill là `SKILL.md` có YAML frontmatter `name`, `description` rồi hướng dẫn Markdown. `gemini-api-dev` còn tham chiếu file như `references/migration.md`.

## Cài đặt và dùng (nguyên văn README)

```bash
npx skills add google-gemini/gemini-skills --list
npx skills add google-gemini/gemini-skills --skill gemini-api-dev
npx ctx7 skills install /google-gemini/gemini-skills
npx ctx7 skills install /google-gemini/gemini-skills gemini-api-dev
```

- **Antigravity:** có sẵn; `⚙ → Customizations → Build with Google Plugins`, hoặc `agy plugin install https://github.com/google-gemini/gemini-skills`.
- **Claude Code:**

  ```
  /plugin marketplace add google-gemini/gemini-skills
  /plugin install gemini-skills@gemini-skills
  ```

- **Cursor:** `/add-plugin google-gemini/gemini-skills` (hoặc thư mục plugin của Cursor).
- **OpenAI Codex:**

  ```bash
  codex plugin marketplace add https://github.com/google-gemini/gemini-skills
  codex plugin add gemini-skills@gemini-skills
  ```

- README nêu Antigravity, Claude Code, Cursor, OpenAI Codex, và bất kỳ agent nào qua CLI `skills` của Vercel hoặc CLI Context7. **Gemini CLI không được nhắc tới.**

**Cài thêm cho `gemini-api-cli` (theo `SKILL.md`):** chạy trình cài `curl -fsSL https://raw.githubusercontent.com/google-gemini/gemini-api-cli/main/scripts/install.sh | bash` (đặt `GEMINI_VERSION=<tag>` để ghim phiên bản). Xác thực bằng `export GEMINI_API_KEY="..."` hoặc `gemini-api configure --api-key "..."`; `gemini-api whoami` cho biết nguồn khóa đang dùng. Cảnh báo: biến `GEMINI_API_KEY` đã export sẽ ghi đè khóa trong kho khóa/cấu hình.

## Yêu cầu, chi phí, độ cũ

- **Yêu cầu:** khóa Gemini API (CLI và SDK dùng `GEMINI_API_KEY`); Python cần `google-genai >= 3.2.0` (`pip install -U google-genai`); TypeScript cần `@google/genai >= 3.2.0` (`npm install @google/genai`); Deep Research và Managed Agents cần `v1beta` (theo `SKILL.md`). README không liệt kê điều kiện tiên quyết.
- **Chi phí:** README không nêu. `SKILL.md` ghi interaction được lưu 55 ngày ở gói trả phí và 1 ngày ở gói miễn phí.
- **Độ cũ:** nhiều model/agent gắn nhãn "preview" (ví dụ `antigravity-preview-09-2026`, `deep-research-preview-04-2026`). `SKILL.md` bảo agent tránh các model cũ `gemini-2.5-*`, `gemini-2.0-*`, `gemini-1.5-*`. Các tên model như `gemini-4-hydrogen` lấy nguyên từ repo, chưa đối chiếu với tài liệu của Google.

## Đánh giá

- **Phù hợp:** người dùng Claude Code, Cursor, Codex hoặc Antigravity đang xây ứng dụng với Gemini API/SDK và muốn agent có hướng dẫn API cập nhật; người dùng CLI `gemini-api` trong shell/CI.
- **Lưu ý:** không phải kênh hỗ trợ chính thức của Google; con số 87%/96% do bên phát hành tự báo cáo.
- **Chưa xác minh:** ngôn ngữ, ngày commit cuối, chính sách đóng góp, nội dung hai skill `gemini-live-api-dev` và `gemini-omni-flash-api`, chi phí.
