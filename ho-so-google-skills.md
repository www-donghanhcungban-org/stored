# Hồ sơ: google/skills

- Ngày lập: 2026-11-28
- URL: https://github.com/google/skills
- Nguồn: trang repo, README, danh sách `skills/` và `skills/cloud`, `SKILL.md` của `gemini-api` và `gcloud`, `CONTRIBUTING.md`. Nội dung các trang đọc qua bản trích xuất của mô hình, không phải file thô. **[chưa xác minh]** là chưa đọc được từ nguồn.

## Tổng quan

| Mục | Nội dung |
|---|---|
| Mục đích | "Agent Skills cho các sản phẩm và công nghệ của Google", gồm Google Cloud. Skill là thư mục có `SKILL.md` theo chuẩn agentskills.io |
| Giấy phép | Apache-2.0 (README: được sao chép, sửa, phân phối theo giấy phép này) |
| Thống kê | 24,9k sao, 2,1k fork, 153 theo dõi, 45 issue mở, 1 PR mở, 670 commit trên `main`. Ngày commit cuối và ngôn ngữ **[chưa xác minh]** |
| Đóng góp | **Không nhận PR hay đóng góp mã bên ngoài.** Chấp nhận báo lỗi/sai sót và đề nghị skill mới qua Issues; khuyến khích fork và remix. Skill do các nhóm Google viết qua chương trình Agent Skills nội bộ |
| Miễn trừ "không phải sản phẩm chính thức" | Không thấy trong README và CONTRIBUTING (khác với `gemini-skills`) |

## Cấu trúc

- Gốc: `.agents/plugins`, `.claude-plugin`, `.github/workflows`, `plugins`, `skills`, `.gitmodules`, `index.json`, `CONTRIBUTING.md`, `LICENSE`, `README.md`, `lychee.toml`. Có liên kết quy tắc ứng xử và chính sách bảo mật (nội dung chưa đọc).
- `skills/`: `ads`, `analytics`, `cloud`, `developers`, `identity`, `platform-devices/litert-google-tensor`.
- `skills/cloud/`: khoảng 150 thư mục skill; danh sách hiển thị bị cắt ở `gke-ai-troubleshooting-tpu-vbar-oom` nên tổng số chưa xác minh.
- README còn nhóm theo loại: đa sản phẩm, AI/ML, hạ tầng, cơ sở dữ liệu, công cụ phát triển, phát triển ứng dụng, quản lý, Well-Architected, bảo mật, lưu trữ web, quảng cáo... Có liên kết tới các repo skill khác (`android/skills`, `dart-lang/skills`, `flutter/skills`, `googlemaps/agent-skills`...).

## Định dạng skill (đã xác nhận ở 2 file)

`SKILL.md` có YAML frontmatter gồm `name`, khối `metadata` (`version`, `category`), `description`, tùy chọn `compatibility`; thân là Markdown với bảng định tuyến tới các file `references/*.md`.

## Skill mẫu

- **gemini-api** (v1.0.4, loại AiAndMachineLearning): Gemini trên nền tảng Gemini (trước là Vertex AI) bằng Google Gen AI SDK cho Python, TS/JS, Go, Java, C#. Bảo agent tránh SDK và họ model đã lỗi thời. Yêu cầu: thông tin xác thực Google Cloud, bật thanh toán, bật `aiplatform.googleapis.com`, vai trò `roles/aiplatform.user`, ADC qua `gcloud auth application-default login`. Cài: `pip install "google-genai>=2.33.0,<3"`.
- **gcloud** (v1.0.4, loại CloudInfrastructureAndServices): skill rào chắn khi agent dùng CLI `gcloud`. Bắt buộc `gcloud help <lệnh>` để xác thực trước khi chạy, thêm `--quiet`, `--project`, và `--limit`/`--filter`/`--format` cho lệnh liệt kê. Danh sách cấm: mọi thay đổi IAM, bật API khi chưa được duyệt, `gcloud * delete`, `gcloud billing *`, `gcloud organizations *`, `gcloud kms *`, `gcloud infra-manager deployments apply`.
- Khác (theo danh sách README): `cloud-run-basics`, `bigquery-basics`, `gke-basics`, `google-cloud-recipe-auth` (xác thực và phân quyền), `secops-triage` (phân loại cảnh báo bảo mật), `google-cloud-waf-security`, `google-ads-api-quickstart`, `google-analytics-data-api-basics`.

## Cài đặt (nguyên văn README)

```bash
npx skills add google/skills     # chọn skill, agent đích, phạm vi project hoặc global
npx skills update
```

Plugin:

```bash
claude plugin marketplace add google/skills
claude plugin install <plugin>@google-plugins
```

```bash
codex plugin marketplace add google/skills   # rồi cài từ trình duyệt /plugins
agy plugin install https://github.com/google/skills/<plugin-path>
```

Cần Node.js (npm/npx). README không liệt kê agent mà `npx skills` hỗ trợ; bảng plugin nêu Claude Code, Codex, Antigravity CLI.

## Yêu cầu, chi phí, bảo mật

- **Yêu cầu:** Node.js để cài; riêng `gemini-api` cần dự án Google Cloud có thanh toán, API và ADC như trên.
- **Chi phí:** README không nêu; `SKILL.md` chỉ chỉ tới giá Google Cloud.
- **Bảo mật:** README không có hướng dẫn bảo mật; file chính sách bảo mật chưa đọc. Skill `gcloud` có rào chắn riêng ở trên, nhưng vẫn do agent thực thi lệnh nên nên kiểm tra quyền của tài khoản dùng.

## Đánh giá

- **Phù hợp:** người dùng agent lập trình (Claude Code, Codex, Antigravity) làm việc với Google Cloud, Gemini, Ads, Analytics muốn hướng dẫn cập nhật dạng skill.
- **Liên quan hồ sơ khác:** skill `gemini-api` ở đây là nơi `google-gemini/gemini-skills` nói đã chuyển `vertex-ai-api-dev` sang (xem `ho-so-gemini-skills.md`).
- **Chưa xác minh:** ngôn ngữ, ngày commit cuối, tổng số skill chính xác, nội dung issue/PR đang mở, chính sách bảo mật, hỗ trợ agent của `npx skills`.
