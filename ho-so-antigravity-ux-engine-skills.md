# Hồ sơ: agent-nau/Antigravity-UX-Engine-Skills

- Ngày lập: 2026-11-28
- URL: https://github.com/agent-nau/Antigravity-UX-Engine-Skills
- Nguồn: trang repo, README, LICENSE. **Không đọc được** `SKILL.md` của cả 5 skill (HTTP 404). **[chưa xác minh]** là chưa đọc được từ nguồn.
- Bối cảnh: repo này xuất hiện khi tìm plugin `ux-engine` trong ảnh chụp màn hình (`/plugin install ux-engine`, "8 skills, 4 commands"). **Đây không phải plugin đó.** Hồ sơ này chỉ mô tả repo được ghi là lấy cảm hứng từ nó.

## Tổng quan

| Mục | Nội dung |
|---|---|
| Mô tả (About) | "Antigravity skills inspired by Design Motion's UX Engine plugin for Claude Code" |
| Tiêu đề README | "Antigravity UX Engine Skills", khẩu hiệu "Production-grade UI/UX engineering skills for Google Antigravity" |
| Giấy phép | MIT, "Copyright (c) 2026 agent-nau" |
| Thống kê | 1 sao, 0 fork, 0 theo dõi, 2 commit trên `main`, không có release hay package. Ngày commit cuối, số issue/PR, người đóng góp, ngôn ngữ **[chưa xác minh]** |
| Nền tảng đích | Google Antigravity (đường dẫn `.gemini/`), **không phải Claude Code** |
| Yêu cầu | README không nêu |

## Quan hệ với bản gốc

- Dòng About là chỗ duy nhất nhắc "Design Motion" và "UX Engine plugin for Claude Code". README, LICENSE đều không nhắc, không có link, không ghi ghi công.
- Không rõ có mã nào sao chép từ bản gốc hay không **[chưa xác minh]**.
- README liệt kê 5 skill; bản gốc theo ảnh có 8 skill và 4 lệnh. Hai bản khác nhau.

## Nội dung README

- **Cấu trúc README:** Overview; The Anti-Slop Manifesto (bảng "chung chung" so với "chuẩn"); Architecture (sơ đồ mermaid 5 skill dẫn tới giao diện chuẩn sản xuất); The 5 Core Skills; Before & After Showcase (ví dụ React `MetricCard` bằng TSX); Quickstart & Installation; Usage Workflows; Repository Structure; Contributing; License.
- **Huy hiệu:** License MIT, Google Antigravity, "Zero AI Slop", "WCAG AA Compliant", PRs Welcome.
- **Tuyên bố tiếp thị (chưa kiểm chứng):** phần mềm "mượt 60fps", chữ "đạt chứng nhận WCAG 2.1 AA", Antigravity "tự nạp" skill khi yêu cầu khớp.

### 5 skill (chỉ theo mô tả trong README)

| Lệnh | Mô tả trong README |
|---|---|
| `/audit` | Kiểm tra UX và khả năng truy cập 12 điểm; mức độ Critical/Warning/Improvement, tọa độ dòng, bản vá dán được. Ví dụ: `/audit inspect the checkout modal in src/components/CheckoutModal.tsx` |
| `/design-system` | Token, bố cục đáp ứng (breakpoint dưới 640px), đủ các trạng thái, đọc `DESIGN.md` |
| `/motion` | Đường cong `cubic-bezier`, chỉ hoạt họa `transform`/`opacity`, dưới 200ms, bọc `prefers-reduced-motion` |
| `/restyle` | Chẩn đoán bốn trục (kiểu chữ, màu, khoảng cách, hoàn thiện), kết quả trước/sau |
| `/unslop` | Bỏ gradient và glassmorphism, chuẩn hóa bo góc, tăng tương phản |

Với cả 5 skill, frontmatter, các bước, script và mọi lệnh shell/mạng mà skill bảo agent chạy đều **[chưa xác minh]**. README không mô tả skill nào gọi shell, `curl`, mạng hay thông tin xác thực.

### Quy ước `DESIGN.md`

Tạo `DESIGN.md` ở gốc dự án với màu thương hiệu, thang chữ, token bo góc; README nói skill "tự đọc và áp dụng". Định dạng của `DESIGN.md` không được nêu.

## Cài đặt (nguyên văn README)

```bash
# A. Theo workspace (khuyến nghị)
mkdir -p .gemini/skills
git clone https://github.com/agent-nau/Antigravity-UX-Engine-Skills.git .gemini/skills/ux-engine
```

```bash
# B. Toàn cục, macOS/Linux
git clone https://github.com/agent-nau/Antigravity-UX-Engine-Skills.git ~/.gemini/antigravity/skills/ux-engine
```

```powershell
# B. Toàn cục, Windows PowerShell
git clone https://github.com/agent-nau/Antigravity-UX-Engine-Skills.git "$HOME\.gemini\antigravity\skills\ux-engine"
```

Đây chỉ là `git clone` nhánh mặc định, không ghim phiên bản, không có checksum. Cách B ghi vào thư mục home, ngoài dự án.

## Cấu trúc repo: mâu thuẫn cần lưu ý

- Mục "Repository Structure" trong README liệt kê các thư mục `audit/`, `design-system/`, `motion/`, `restyle/`, `unslop/`, mỗi thư mục có `SKILL.md`.
- Nhưng danh sách file thật ở gốc repo chỉ có `.gitignore`, `LICENSE`, `README.md`, và cả 5 URL `…/main/<skill>/SKILL.md` đều trả **404**.
- Vì vậy các skill có thể không tồn tại trên `main` (hoặc nằm ở nhánh khác), **[chưa xác minh]**. Nếu đúng thì repo hiện chỉ có README, tức là clone về sẽ không có skill nào chạy được.
- Lưu ý: một lần đọc trước đó của tôi ghi cấu trúc có các thư mục skill, đó là lấy từ README chứ không phải từ danh sách file thật; bản hồ sơ này sửa lại.

## Đóng góp

Fork, nhánh, PR theo README; không có `CONTRIBUTING`.

## Đánh giá

- **Rủi ro:** repo rất mới (1 sao, 2 commit), cài bằng `git clone` không ghim, chưa đọc được nội dung skill nên không thể khẳng định an toàn. Cách B ghi vào thư mục home.
- **Phù hợp:** người dùng Google Antigravity muốn thử bộ quy tắc giao diện; không dùng được trực tiếp với Claude Code vì lệnh và đường dẫn dành cho Antigravity.
- **Chưa xác minh:** nội dung 5 `SKILL.md` (có tồn tại không), ngày commit cuối, ngôn ngữ, số issue/PR, mối quan hệ mã nguồn với plugin gốc của Design Motion, và mọi con số hiệu năng/chứng nhận trong README.
