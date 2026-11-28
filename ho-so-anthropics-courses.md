# Hồ sơ: anthropics/courses

- Ngày lập: 2026-11-28
- URL: https://github.com/anthropics/courses
- Nguồn: trang repo, README gốc (nhánh `master`), README của cả 5 khóa. Chưa mở các notebook và file LICENSE. **[chưa xác minh]** là chưa đọc được từ nguồn.

## Tổng quan

| Mục | Nội dung |
|---|---|
| **Trạng thái** | **Đã lưu trữ (archived) bởi chủ sở hữu ngày 15/09/2026, chỉ đọc.** Không còn commit, issue hay PR mới |
| Mục đích | "Các khóa học giáo dục của Anthropic"; README nói hiện có 5 khóa, nên học theo thứ tự 1 đến 5 |
| Giấy phép | Có file LICENSE ở gốc nhưng loại giấy phép **[chưa xác minh]** |
| Định dạng | Jupyter notebook (theo README từng khóa) |
| Thống kê | 23,2k sao, 2,6k fork, 260 theo dõi, 44 issue, 51 PR, 59 commit trên `master`. Ngày commit cuối **[chưa xác minh]** |
| Đóng góp | Không nêu; repo đã chỉ đọc |

## 5 khóa

### 1. anthropic_api_fundamentals
Cơ bản về Claude SDK: lấy khóa API, tham số model, prompt đa phương thức, streaming. Sáu bài notebook: `01_getting_started` (lấy khóa API, yêu cầu đơn giản), `02_messages_format`, `03_models` (so sánh họ model Claude), `04_parameters`, `05_Streaming`, `06_vision`.

### 2. prompt_engineering_interactive_tutorial
Kỹ thuật viết prompt từng bước, mỗi bài có bài tập và "Example Playground". Có bản Google Sheets dùng Claude for Sheets (README khuyên dùng vì dễ hơn). Đây là cùng khóa với repo `prompt-eng-interactive-tutorial` trong bài đăng gốc.
- Cơ bản: 1 Cấu trúc prompt, 2 Rõ ràng và trực tiếp, 3 Gán vai trò.
- Trung cấp: 4 Tách dữ liệu khỏi chỉ dẫn, 5 Định dạng đầu ra và nói thay Claude, 6 Tư duy từng bước, 7 Dùng ví dụ.
- Nâng cao: 8 Tránh ảo giác, 9 Prompt phức tạp (chatbot, pháp lý, bài tập tài chính và lập trình).
- Phụ lục: chuỗi prompt, dùng công cụ, tìm kiếm và truy xuất.
- Có đáp án dạng Google Sheets và bản AWS Workshop (chưa mở).

### 3. real_world_prompting
Dành cho lập trình viên có kinh nghiệm đã học khóa 2 (README "rất khuyến nghị"). Năm notebook: `01_prompting_recap`, `02_medical_prompt`, `03_prompt_engineering`, `04_call_summarizer`, `05_customer_support_ai`. Có bản Google Vertex (nhánh `vertex`, chưa mở).

### 4. prompt_evaluations
Chín bài: 01 Evaluations 101; 02 đánh giá do người chấm với Workbench của Anthropic; 03 đánh giá chấm bằng code; 04 đánh giá phân loại chấm bằng code; 05 giới thiệu promptfoo; 06 đánh giá phân loại bằng promptfoo; 07 bộ chấm tùy chỉnh bằng promptfoo; 08 đánh giá do model chấm bằng promptfoo; 09 đánh giá do model chấm tùy chỉnh bằng promptfoo.

### 5. tool_use
Sáu bài: 01 tổng quan; 02 công cụ đơn giản đầu tiên; 03 ép đầu ra JSON bằng tool use; 04 quy trình tool use hoàn chỉnh; 05 chọn công cụ (tool choice); 06 chatbot nhiều công cụ.

## Cài đặt, yêu cầu, chi phí
- **Lệnh cài đặt:** README gốc và README các khóa đã đọc không có lệnh cài. Có thể nằm trong notebook (chưa mở) **[chưa xác minh]**.
- **Khóa API:** khóa 1 chắc chắn cần (bài đầu là lấy khóa). Khóa 2 dùng Claude qua API hoặc tiện ích Claude for Sheets. Các khóa còn lại không nêu rõ. Chi tiết dùng promptfoo và Workbench **[chưa xác minh]**.
- **Chi phí:** không nêu giá. README nói các khóa "thường dùng model rẻ nhất, Claude 3 Haiku, để giảm chi phí cho học viên", và có thể dùng model khác.

## Độ cũ
- Repo đã lưu trữ, tài liệu và tên model (Claude 3 Haiku/Sonnet/Opus) cũ. Link tài liệu trỏ tới `docs.anthropic.com`. Nên coi tên model, ID model và liên kết là có khả năng không còn đúng.
- Điều này cũng áp dụng cho `prompt-eng-interactive-tutorial` trong bài đăng gốc: repo đó có thể cũng không còn được cập nhật.

## Đánh giá
- **Phù hợp:** người học theo giáo trình có thứ tự, từ API cơ bản, viết prompt, đánh giá prompt đến tool use, và chấp nhận phải tự đổi tên model.
- **Không phù hợp:** ai cần tài liệu mới theo model hiện hành.
- **Chưa xác minh:** loại giấy phép, ngày commit cuối, lệnh cài đặt, nội dung notebook, yêu cầu khóa API của các khóa 3 đến 5.
