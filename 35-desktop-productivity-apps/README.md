# 35. Ứng dụng desktop, tiện ích hệ thống & năng suất cá nhân

Ứng dụng người dùng cuối chạy trên máy cá nhân: tiện ích macOS/Windows/Linux, quản lý file và media, đọc sách, ghi chú và knowledge base cá nhân. Trước khi cài, kiểm quyền hệ thống app yêu cầu (accessibility, full disk, mạng), nguồn phát hành có ký số hay không, và dữ liệu đồng bộ đi đâu.

Mục được lập ngày 2026-11-23 khi chia lại catalog; hồ sơ bên dưới chuyển nguyên văn từ mục cũ, neo cũ vẫn giữ một đoạn dẫn sang đây. Bảng tổng hợp theo danh mục con: [catalog/](../catalog/README.md).

<a id="chuyen-muc-2026-11-23"></a>

## Hồ sơ chuyển về từ mục khác — 23/11/2026

54 hồ sơ được chuyển khi chia lại catalog theo `data/taxonomy.json`. Nội dung, ngày kiểm và mức bằng chứng giữ nguyên như ở mục gốc.

<a id="chuyen-brewui"></a>

### BrewUI

`Homebrew/BrewUI` · License: AGPL-3.0 · ★ 2.769

GUI chính thức của Homebrew (SwiftUI, macOS 26+), cask homebrew-app, ra cùng Homebrew 7.0.0; hiện lệnh brew thật, hàng đợi lệnh tuần tự, zsh cô lập (cấu hình qua brew.env); không telemetry riêng; 455/1.201 commit có trailer Claude, AGENTS.md mẫu; v0.6.0, ★ 14/10/2026; ★ 31/10/2026: 2.769 (GitHub API)

**Hồ sơ gốc:** [mục 13](../13-dev-stack-devops/README.md) (bảng/đoạn chung, giữ nguyên tại chỗ).

<a id="chuyen-applite"></a>

### Applite

`milanvarady/Applite` · License: MIT · ★ 7.104

GUI Homebrew cho cask/app trên macOS; thay thế BrewUI trên macOS cũ; ★ 14/10/2026; ★ 31/10/2026: 7.104 (GitHub API)

**Hồ sơ gốc:** [mục 13](../13-dev-stack-devops/README.md) (bảng/đoạn chung, giữ nguyên tại chỗ).

<a id="chuyen-cork"></a>

### Cork

`buresdv/Cork` · License: provisional (không OSI) · ★ 4.717

GUI Homebrew; mã công khai nhưng license tạm "provided as-is", bản build bán trả phí (chưa xác minh); ★ 14/10/2026; ★ 31/10/2026: 4.717 (GitHub API)

**Hồ sơ gốc:** [mục 13](../13-dev-stack-devops/README.md) (bảng/đoạn chung, giữ nguyên tại chỗ).

<a id="chuyen-cleanmylinux"></a>

### CleanMyLinux

`Better-Linux/CleanMyLinux` · License: MIT · ★ 10

App dọn dẹp Linux desktop (Tauri v2+Rust+React19), gỡ app + cập nhật đa package manager, có ml/ phân loại app. RỦI RO (đọc mã): helper pkexec /usr/bin/cleanmylinux-helper = exec "$@", gọi qua pkexec sh -c => primitive chạy lệnh root tùy ý; allow_active auth_self_keep cache => sau 1 lần auth mọi tiến trình user active chạy được root. beta, 1 tác giả. ★ slide 18/10/2026; mục 13 §6e; ★ 31/10/2026: 10 (GitHub API)

**Hồ sơ gốc:** [mục 13](../13-dev-stack-devops/README.md) (bảng/đoạn chung, giữ nguyên tại chỗ).

<a id="chuyen-nextai-translator"></a>

### nextai-translator

`nextai-translator/nextai-translator` · License: AGPL-3.0 · ★ 25.067 · docs-read · 2026-11-18

Ứng dụng dịch, trau chuốt và tóm tắt văn bản bằng LLM, có tiện ích trình duyệt (Chrome, Firefox) và app desktop Windows/macOS/Linux; trước đây tên openai-translator. Ba chế độ dịch, trau chuốt, tóm tắt cho 55 ngôn ngữ, có streaming và TTS; chạy cả tiện ích trình duyệt lẫn desktop (Tauri) đa nền tảng; hỗ trợ dịch ảnh chụp màn hình và sổ từ vựng. Điều kiện: Cần khoá API OpenAI hoặc Azure OpenAI (hoặc nhà cung cấp LLM khác, README quảng bá TeamoRouter); đổi tên do cảnh báo nhãn hiệu từ OpenAI; app desktop chưa ký nên Windows/macOS cảnh báo khi cài. ★ 18/11/2026: 25.067 (GitHub search API), nhóm "Editor, Terminal & Dòng lệnh" trong kho-repo của Phan Đông Giang, mục 08 §6c.5

**Hồ sơ gốc:** [mục 08](../08-awesome-lists-learning/README.md#6c58-editor-terminal--dòng-lệnh) (bảng/đoạn chung, giữ nguyên tại chỗ).

<a id="chuyen-voyager"></a>

### voyager

`voyager-crew/voyager` · License: GPL-3.0 · ★ 20.655 · docs-read · 2026-11-18

Tiện ích trình duyệt bổ sung thư mục, dòng thời gian, xuất hội thoại và chép công thức cho Gemini, AI Studio, ChatGPT, Claude, DeepSeek và Kimi; mỗi tính năng là plugin JSON. Plugin là JSON thuần, không chạy mã, gỡ sạch khi tắt; phát hành trên Chrome Web Store, Edge Add-ons và Firefox Add-ons; README có 10 bản ngôn ngữ. Điều kiện: Dự án độc lập, không liên kết với Google, Anthropic, OpenAI hay Moonshot AI; trên Gemini for Enterprise chỉ chạy thư viện prompt; copyleft GPL-3.0. ★ 18/11/2026: 20.655 (GitHub search API), nhóm "Editor, Terminal & Dòng lệnh" trong kho-repo của Phan Đông Giang, mục 08 §6c.5

**Hồ sơ gốc:** [mục 08](../08-awesome-lists-learning/README.md#6c58-editor-terminal--dòng-lệnh) (bảng/đoạn chung, giữ nguyên tại chỗ).

<a id="chuyen-worldmonitor"></a>

### worldmonitor

`koala73/worldmonitor` · License: AGPL-3.0-only · ★ 90.854 · docs-read · 2026-11-18

Bảng điều khiển tình báo toàn cầu thời gian thực: tổng hợp tin bằng AI, theo dõi địa chính trị, hạ tầng, tài chính trên bản đồ 3D/2D, có web, desktop, terminal, CLI và SDK. Tự host toàn bộ stack bằng Docker (dashboard, Redis, AIS relay); chạy AI cục bộ với Ollama không cần khoá API; app desktop Tauri 2 cho Windows, macOS, Linux và dashboard terminal qua npx. Điều kiện: AGPL-3.0 buộc công bố mã khi chạy dịch vụ mạng; không được trình bày bản fork như trang chính thức (thương hiệu World Monitor); một số nguồn dữ liệu cần thông tin xác thực riêng (.env.example); Node.js 24. ★ 18/11/2026: 90.854 (GitHub search API), nhóm "Năng suất, Ghi chú & Việc làm" trong kho-repo của Phan Đông Giang, mục 08 §6c.5

**Hồ sơ gốc:** [mục 08](../08-awesome-lists-learning/README.md#6c515-năng-suất-ghi-chú--việc-làm) (bảng/đoạn chung, giữ nguyên tại chỗ).

<a id="chuyen-appflowy"></a>

### AppFlowy

`AppFlowy-IO/AppFlowy` · License: AGPL-3.0 · ★ 79.108 · docs-read · 2026-11-18

Không gian làm việc kiểu Notion mã nguồn mở có AI, giữ quyền kiểm soát dữ liệu; ứng dụng desktop và di động. Viết bằng Flutter và Rust (thư mục frontend/appflowy_flutter và frontend/rust-lib); có bản cho macOS, Windows, Linux, iOS và Android; có hướng dẫn tự host. Điều kiện: AGPL-3.0: phân phối hoặc cung cấp qua mạng bản sửa đổi phải công bố mã nguồn; Android cần bản 10 trở lên, không hỗ trợ ARMv7. ★ 18/11/2026: 79.108 (GitHub search API), nhóm "Năng suất, Ghi chú & Việc làm" trong kho-repo của Phan Đông Giang, mục 08 §6c.5

**Hồ sơ gốc:** [mục 08](../08-awesome-lists-learning/README.md#6c515-năng-suất-ghi-chú--việc-làm) (bảng/đoạn chung, giữ nguyên tại chỗ).

<a id="chuyen-affine"></a>

### AFFiNE

`toeverything/AFFiNE` · License: Hỗn hợp · ★ 74.618 · docs-read · 2026-11-18

Không gian làm việc tất cả trong một, local-first, gộp tài liệu, bảng trắng (canvas) và cơ sở dữ liệu, thay thế Notion và Miro. Tài liệu và bảng trắng hợp nhất trên canvas edgeless dựa trên BlockSuite; local-first kèm đồng bộ và cộng tác thời gian thực; có ứng dụng web, Electron, iOS và Android trong packages/frontend/apps. Điều kiện: Phần backend theo giấy phép EE: dùng production cần thuê bao AFFiNE EE (phần thuộc bản Community thì không); đóng góp cần ký CLA. ★ 18/11/2026: 74.618 (GitHub search API), nhóm "Năng suất, Ghi chú & Việc làm" trong kho-repo của Phan Đông Giang, mục 08 §6c.5

**Hồ sơ gốc:** [mục 08](../08-awesome-lists-learning/README.md#6c515-năng-suất-ghi-chú--việc-làm) (bảng/đoạn chung, giữ nguyên tại chỗ).

<a id="chuyen-memos"></a>

### memos

`usememos/memos` · License: MIT · ★ 64.528 · docs-read · 2026-11-18

Ứng dụng ghi chú nhanh tự host, sắp xếp ghi chú Markdown theo dòng thời gian cá nhân, tự chọn riêng tư hay chia sẻ. Chạy bằng một lệnh Docker, toàn bộ dữ liệu nằm trong một thư mục ~/.memos; backend Go kèm web frontend; có API, MCP server, Web Clipper và bot Telegram. ★ 18/11/2026: 64.528 (GitHub search API), nhóm "Năng suất, Ghi chú & Việc làm" trong kho-repo của Phan Đông Giang, mục 08 §6c.5

**Hồ sơ gốc:** [mục 08](../08-awesome-lists-learning/README.md#6c515-năng-suất-ghi-chú--việc-làm) (bảng/đoạn chung, giữ nguyên tại chỗ).

<a id="chuyen-joplin"></a>

### joplin

`laurent22/joplin` · License: AGPL-3.0-or-later mặc định · ★ 57.228 · docs-read · 2026-11-18

Ứng dụng ghi chú và việc cần làm mã nguồn mở, offline-first, ghi chú Markdown sắp theo sổ, đồng bộ có mã hoá đầu cuối. Có bản Windows, Linux, macOS, Android, iOS và Web Clipper cho Firefox/Chrome; đồng bộ mã hoá đầu cuối qua Nextcloud, Dropbox, OneDrive, Joplin Cloud; nhập từ Evernote, tìm kiếm toàn văn, hỗ trợ plugin và theme. Điều kiện: Joplin Server chỉ được dùng phi thương mại cá nhân trừ khi có cho phép bằng văn bản; không dùng logo/biểu tượng khi chưa xin phép. ★ 18/11/2026: 57.228 (GitHub search API), nhóm "Năng suất, Ghi chú & Việc làm" trong kho-repo của Phan Đông Giang, mục 08 §6c.5

**Hồ sơ gốc:** [mục 08](../08-awesome-lists-learning/README.md#6c515-năng-suất-ghi-chú--việc-làm) (bảng/đoạn chung, giữ nguyên tại chỗ).

<a id="chuyen-siyuan"></a>

### siyuan

`siyuan-note/siyuan` · License: AGPL-3.0 · ★ 47.272 · docs-read · 2026-11-18

Hệ thống quản lý tri thức cá nhân ưu tiên riêng tư, tham chiếu cấp khối và soạn Markdown WYSIWYG. Tham chiếu khối hai chiều, nhúng truy vấn SQL, cơ sở dữ liệu dạng bảng và flashcard lặp lại ngắt quãng; xuất Markdown, PDF, Word, HTML; có ứng dụng Android/iOS/HarmonyOS và image Docker b3log/siyuan. Điều kiện: Một số tính năng chỉ dành cho thành viên trả phí; AI dùng OpenAI API cần khoá; chạy Docker cần đặt accessAuthCode. ★ 18/11/2026: 47.272 (GitHub search API), nhóm "Năng suất, Ghi chú & Việc làm" trong kho-repo của Phan Đông Giang, mục 08 §6c.5

**Hồ sơ gốc:** [mục 08](../08-awesome-lists-learning/README.md#6c515-năng-suất-ghi-chú--việc-làm) (bảng/đoạn chung, giữ nguyên tại chỗ).

<a id="chuyen-logseq"></a>

### logseq

`logseq/logseq` · License: AGPL-3.0 · ★ 45.639 · docs-read · 2026-11-18

Nền tảng quản lý tri thức và cộng tác ưu tiên quyền riêng tư, mã nguồn mở; ghi chú dạng khối, hỗ trợ Markdown và Org-mode, có bản desktop, web và mobile. Có plugin API với tài liệu tại plugins-doc.logseq.com; hỗ trợ chú thích PDF và quản lý công việc; có ứng dụng mobile (thư mục android, ios trong repo). Điều kiện: Giấy phép AGPL-3.0 (copyleft mạnh, áp dụng cả khi cung cấp qua mạng); README nói bản DB đang beta, mobile mới và RTC đang alpha, có thể mất dữ liệu nên cần sao lưu. ★ 18/11/2026: 45.639 (GitHub search API), nhóm "Năng suất, Ghi chú & Việc làm" trong kho-repo của Phan Đông Giang, mục 08 §6c.5

**Hồ sơ gốc:** [mục 08](../08-awesome-lists-learning/README.md#6c515-năng-suất-ghi-chú--việc-làm) (bảng/đoạn chung, giữ nguyên tại chỗ).

<a id="chuyen-trilium"></a>

### Trilium

`TriliumNext/Trilium` · License: AGPL-3.0 · ★ 38.981 · docs-read · 2026-11-18

Ứng dụng ghi chú phân cấp đa nền tảng, mã nguồn mở, hướng tới xây dựng cơ sở tri thức cá nhân lớn; có bản desktop và máy chủ đồng bộ tự host. Mã hoá ghi chú theo từng ghi chú, đồng bộ qua máy chủ tự host và có REST API (ETAPI); hỗ trợ canvas Excalidraw, mind map, bản đồ quan hệ, scripting; README nói mở rộng tốt tới hơn 100 000 ghi chú. Điều kiện: Giấy phép AGPL-3.0; giao diện web chỉ hỗ trợ bản mới nhất của Chrome và Firefox; chưa có app mobile chính thức (dùng giao diện web mobile). ★ 18/11/2026: 38.981 (GitHub search API), nhóm "Năng suất, Ghi chú & Việc làm" trong kho-repo của Phan Đông Giang, mục 08 §6c.5

**Hồ sơ gốc:** [mục 08](../08-awesome-lists-learning/README.md#6c515-năng-suất-ghi-chú--việc-làm) (bảng/đoạn chung, giữ nguyên tại chỗ).

<a id="chuyen-super-productivity"></a>

### super-productivity

`super-productivity/super-productivity` · License: MIT · ★ 23.776 · docs-read · 2026-11-18

Ứng dụng to-do, theo dõi thời gian và lập kế hoạch ngày cho công việc cá nhân, ưu tiên offline và quyền riêng tư. Tích hợp Jira, GitHub, GitLab, Linear và nhiều công cụ khác; đồng bộ qua SuperSync mã hoá đầu cuối (tự host được), Dropbox hoặc WebDAV; chạy trên Linux, macOS, Windows, Android, iOS và trình duyệt. Điều kiện: Bản web có một số giới hạn so với bản desktop. ★ 18/11/2026: 23.776 (GitHub search API), nhóm "Năng suất, Ghi chú & Việc làm" trong kho-repo của Phan Đông Giang, mục 08 §6c.5

**Hồ sơ gốc:** [mục 08](../08-awesome-lists-learning/README.md#6c515-năng-suất-ghi-chú--việc-làm) (bảng/đoạn chung, giữ nguyên tại chỗ).

<a id="chuyen-activitywatch"></a>

### activitywatch

`ActivityWatch/activitywatch` · License: MPL-2.0 · ★ 19.697 · docs-read · 2026-11-18

Trình theo dõi thời gian sử dụng máy tính mã nguồn mở, ghi lại ứng dụng, cửa sổ, tab trình duyệt và trạng thái AFK, lưu dữ liệu cục bộ trên máy người dùng. Dữ liệu lưu cục bộ, người dùng kiểm soát; kiến trúc module gồm server (Python và Rust) cùng các watcher tách riêng làm submodule; có DOI Zenodo để trích dẫn trong nghiên cứu. ★ 18/11/2026: 19.697 (GitHub search API), nhóm "Năng suất, Ghi chú & Việc làm" trong kho-repo của Phan Đông Giang, mục 08 §6c.5

**Hồ sơ gốc:** [mục 08](../08-awesome-lists-learning/README.md#6c515-năng-suất-ghi-chú--việc-làm) (bảng/đoạn chung, giữ nguyên tại chỗ).

<a id="chuyen-xournalpp"></a>

### xournalpp

`xournalpp/xournalpp` · License: GPL-2.0 · ★ 15.687 · docs-read · 2026-11-18

Phần mềm ghi chú viết tay viết bằng C++, hỗ trợ bút cảm ứng lực và chú thích lên PDF. Hỗ trợ bút cảm ứng lực (Wacom, Huion, XP Pen); chú thích lên PDF, xuất SVG/PNG/PDF từ GUI và dòng lệnh; plugin bằng Lua và hỗ trợ LaTeX. Điều kiện: Tính năng LaTeX cần cài LaTeX riêng. ★ 18/11/2026: 15.687 (GitHub search API), nhóm "Năng suất, Ghi chú & Việc làm" trong kho-repo của Phan Đông Giang, mục 08 §6c.5

**Hồ sơ gốc:** [mục 08](../08-awesome-lists-learning/README.md#6c515-năng-suất-ghi-chú--việc-làm) (bảng/đoạn chung, giữ nguyên tại chỗ).

<a id="chuyen-notesnook"></a>

### notesnook

`streetwriters/notesnook` · License: GPL-3.0 · ★ 14.952 · docs-read · 2026-11-18

Ứng dụng ghi chú mã hoá đầu-cuối, thay thế Evernote, có bản web, desktop và di động. Mã hoá mọi thứ trên thiết bị bằng XChaCha20-Poly1305 và Argon2; monorepo gồm client web (React), desktop (Electron), mobile (React Native) và web clipper; có công cụ Vericrypt để tự kiểm chứng mã hoá. Điều kiện: Đồng bộ cần tài khoản có email; dịch vụ chịu chính sách bảo mật và điều khoản của Notesnook. ★ 18/11/2026: 14.952 (GitHub search API), nhóm "Năng suất, Ghi chú & Việc làm" trong kho-repo của Phan Đông Giang, mục 08 §6c.5

**Hồ sơ gốc:** [mục 08](../08-awesome-lists-learning/README.md#6c515-năng-suất-ghi-chú--việc-làm) (bảng/đoạn chung, giữ nguyên tại chỗ).

<a id="chuyen-horizon"></a>

### Horizon

`Thysrael/Horizon` · License: MIT · ★ 14.539 · docs-read · 2026-11-18

Radar tin tức dùng AI: gom tin từ RSS, Hacker News, Reddit, Telegram, X, GitHub…, chấm điểm, lọc trùng và tạo bản tin hằng ngày tiếng Anh và tiếng Trung. Profile cấu hình tiêu chí chấm điểm và đầu ra riêng cho từng loại nội dung; phát bản tin qua Markdown, Pages, email, WeChat và webhook; có MCP và Agent Skill để trợ lý AI điều khiển. Điều kiện: Cần khoá API mô hình (OpenAI, Gemini…) qua biến môi trường, hoặc đăng nhập ChatGPT cho thuê bao đủ điều kiện. ★ 18/11/2026: 14.539 (GitHub search API), nhóm "Năng suất, Ghi chú & Việc làm" trong kho-repo của Phan Đông Giang, mục 08 §6c.5

**Hồ sơ gốc:** [mục 08](../08-awesome-lists-learning/README.md#6c515-năng-suất-ghi-chú--việc-làm) (bảng/đoạn chung, giữ nguyên tại chỗ).

<a id="anhkysuai-niri-wm-niri"></a>

### Niri

- **Repo:** [niri-wm/niri](https://github.com/niri-wm/niri).
- **Mục đích:** Wayland compositor xếp cửa sổ thành dải cột cuộn ngang.
- **Điểm đáng dùng:** Mỗi màn hình có dải/workspace riêng; README mô tả giữ bố cục qua tháo màn hình, screencast và che cửa sổ nhạy cảm.
- **License:** GPL-3.0-or-later.
- **Giới hạn:** Không phải desktop environment hoàn chỉnh; cần shell, portal và công cụ phụ, CI test đọc loại trừ visual tests ở bước build.
- **Tích hợp:** Thử như cấu hình workstation tùy chọn, kiểm tra đa màn hình, screen sharing và accessibility trước khi dùng hằng ngày.
- **Đối chiếu:** Sway cho tiling Wayland; Hyprland cho compositor động; GNOME cho desktop tích hợp.
- **Mức kiểm chứng:** `docs-read` — Đọc các phần mô tả và giới hạn trong README, thông báo license, metadata manifest và cấu hình CI khi có; chưa đọc toàn bộ mã triển khai, chưa cài hoặc chạy kiểm thử upstream.
- **Snapshot:** kiểm ngày 2026-11-23; commit `02ee0585b9da359cb30aa2a13a6023a6e471cc23` (2026-11-23T09:35:25+03:00); 29,212 sao theo GitHub API ngày 2026-11-23. Sao không đại diện chất lượng.
- **Bằng chứng:** [README.md](https://github.com/niri-wm/niri/blob/02ee0585b9da359cb30aa2a13a6023a6e471cc23/README.md) · [LICENSE](https://github.com/niri-wm/niri/blob/02ee0585b9da359cb30aa2a13a6023a6e471cc23/LICENSE) · [Cargo.toml](https://github.com/niri-wm/niri/blob/02ee0585b9da359cb30aa2a13a6023a6e471cc23/Cargo.toml) · [.github/workflows/ci.yml](https://github.com/niri-wm/niri/blob/02ee0585b9da359cb30aa2a13a6023a6e471cc23/.github/workflows/ci.yml) · [GitHub API](https://api.github.com/repos/niri-wm/niri).

<a id="anhkysuai-devolutions-unigetui"></a>

### UniGetUI

- **Repo:** [Devolutions/UniGetUI](https://github.com/Devolutions/UniGetUI).
- **Mục đích:** GUI tập trung cho nhiều package manager, ưu tiên Windows và có bản đa nền.
- **Điểm đáng dùng:** Giao diện tìm/cài/nâng/gỡ qua WinGet, Scoop, Chocolatey và manager khác; README nêu chủ quản Devolutions và nguồn chính thức.
- **License:** MIT; package được cài có license riêng.
- **Giới hạn:** GUI không xác thực chất lượng mọi package upstream; README cảnh báo tên miền giả, package manager và publisher cần kiểm tra riêng.
- **Tích hợp:** Dùng cho quản lý workstation, xuất danh sách gói có version và duyệt nguồn trước thao tác cài hàng loạt.
- **Đối chiếu:** WinGet CLI cho Windows; [Homebrew](../13-dev-stack-devops/README.md#anhkysuai-homebrew-brew) cho macOS/Linux; Chocolatey cho quản lý package Windows.
- **Mức kiểm chứng:** `docs-read` — Đọc các phần mô tả và giới hạn trong README, thông báo license, metadata manifest và cấu hình CI khi có; chưa đọc toàn bộ mã triển khai, chưa cài hoặc chạy kiểm thử upstream.
- **Snapshot:** kiểm ngày 2026-11-23; commit `bb42035d57d7c3bd9ff7254b94f713129e040b4c` (2026-11-20T14:40:43-05:00); 27,211 sao theo GitHub API ngày 2026-11-23. Sao không đại diện chất lượng.
- **Bằng chứng:** [README.md](https://github.com/Devolutions/UniGetUI/blob/bb42035d57d7c3bd9ff7254b94f713129e040b4c/README.md) · [LICENSE](https://github.com/Devolutions/UniGetUI/blob/bb42035d57d7c3bd9ff7254b94f713129e040b4c/LICENSE) · [.github/workflows/dotnet-test.yml](https://github.com/Devolutions/UniGetUI/blob/bb42035d57d7c3bd9ff7254b94f713129e040b4c/.github/workflows/dotnet-test.yml) · [GitHub API](https://api.github.com/repos/Devolutions/UniGetUI).

<a id="anhkysuai-nikitabobko-aerospace"></a>

### AeroSpace

**Repo:** [nikitabobko/AeroSpace](https://github.com/nikitabobko/AeroSpace) · **License:** MIT · **Kiểm:** 2026-11-23, `docs-read`, [`6ed6af62429e`](https://github.com/nikitabobko/AeroSpace/tree/6ed6af62429e8aaec4d3d6516184945e19728fa4) (commit 2026-11-13). **Sao:** 23,926 tại 2026-11-23 theo [GitHub API](https://api.github.com/repos/nikitabobko/AeroSpace).

| Mục | Đánh giá |
|---|---|
| Mục đích | Trình quản lý cửa sổ dạng tiling kiểu i3 cho macOS. |
| Giá trị và cơ chế theo tài liệu | README mô tả cây bố cục, workspace tự mô phỏng, CLI/config text và không cần tắt SIP; CI build Swift debug/release và chạy test. |
| Giới hạn | README đặt nhãn beta. Workspace mô phỏng có hành vi khác Spaces gốc; chưa thử app đặc biệt, accessibility permission hoặc nhiều màn hình thực tế. |
| Điều kiện tích hợp | Thử cấu hình phím với vài ứng dụng, giữ cách thoát/tắt nhanh; kiểm màn hình ngoài, floating exception và nâng cấp macOS trước dùng làm môi trường hằng ngày. |
| Lựa chọn đối chiếu | yabai; Amethyst; Rectangle. |

**Phạm vi bằng chứng:** đã clone, đọc trích đoạn tài liệu, giấy phép và các file cấu hình được dẫn dưới đây; chưa chạy mã, build, benchmark hoặc test upstream. `docs-read` không phải kiểm chứng implementation.

**Nguồn tại cùng SHA:** [README.md](https://github.com/nikitabobko/AeroSpace/blob/6ed6af62429e8aaec4d3d6516184945e19728fa4/README.md) · [LICENSE.txt](https://github.com/nikitabobko/AeroSpace/blob/6ed6af62429e8aaec4d3d6516184945e19728fa4/LICENSE.txt) · [.github/workflows/build.yml](https://github.com/nikitabobko/AeroSpace/blob/6ed6af62429e8aaec4d3d6516184945e19728fa4/.github/workflows/build.yml).

<a id="anhkysuai-winboat-org-winboat"></a>

### WinBoat

**Repo:** [winboat-org/winboat](https://github.com/winboat-org/winboat) · **License:** MIT cho ứng dụng; Windows và phần mềm khách có giấy phép riêng · **Kiểm:** 2026-11-23, `docs-read`, [`b9a2df2cc33b`](https://github.com/winboat-org/winboat/tree/b9a2df2cc33b2a5e2dc95b3f0472d832f44e86d3) (commit 2026-09-10). **Sao:** 23,435 tại 2026-11-23 theo [GitHub API](https://api.github.com/repos/winboat-org/winboat).

| Mục | Đánh giá |
|---|---|
| Mục đích | Ứng dụng Electron giúp chạy cửa sổ phần mềm Windows trong desktop Linux. |
| Giá trị và cơ chế theo tài liệu | README giải thích Windows VM nằm trong Docker/Podman, guest server và FreeRDP RemoteApp; manifest Bun/Electron và workflow build xác định các thành phần. |
| Giới hạn | README ghi beta; không bảo đảm mọi app Windows hoạt động. Home directory được mount sang Windows nên phải kiểm phạm vi chia sẻ; MIT không cấp quyền hệ điều hành khách. |
| Điều kiện tích hợp | Thử VM với dữ liệu riêng, kiểm CPU/RAM/virtualization và ứng dụng mục tiêu; giới hạn mount, chuẩn bị backup và đối chiếu giấy phép Windows trước dùng lâu dài. |
| Lựa chọn đối chiếu | Wine; Bottles; virt-manager. |

**Phạm vi bằng chứng:** đã clone, đọc trích đoạn tài liệu, giấy phép và các file cấu hình được dẫn dưới đây; chưa chạy mã, build, benchmark hoặc test upstream. `docs-read` không phải kiểm chứng implementation.

**Nguồn tại cùng SHA:** [README.md](https://github.com/winboat-org/winboat/blob/b9a2df2cc33b2a5e2dc95b3f0472d832f44e86d3/README.md) · [LICENSE](https://github.com/winboat-org/winboat/blob/b9a2df2cc33b2a5e2dc95b3f0472d832f44e86d3/LICENSE) · [package.json](https://github.com/winboat-org/winboat/blob/b9a2df2cc33b2a5e2dc95b3f0472d832f44e86d3/package.json) · [.github/workflows/release.yml](https://github.com/winboat-org/winboat/blob/b9a2df2cc33b2a5e2dc95b3f0472d832f44e86d3/.github/workflows/release.yml).

<a id="anhkysuai-2026-11-23-tw93-mole"></a>

### Mole

**Repo:** [tw93/Mole](https://github.com/tw93/Mole) · **License:** GPL-3.0 · **★ 75,916 (GitHub API, 2026-11-23)**

**Mục đích:** CLI macOS để dọn cache, gỡ ứng dụng, phân tích dung lượng và theo dõi hệ thống.

**Giá trị:** Gom các thao tác bảo trì vào cùng giao diện dòng lệnh; README tách rõ CLI trong repo với ứng dụng native thương mại.

**Giới hạn:** Thao tác dọn/xóa có thể tác động dữ liệu máy; bản native Mac/Windows không được suy là cùng giấy phép với CLI GPL-3.0.

**Cách tham khảo/tích hợp:** Tham khảo thiết kế dry-run và xác nhận trước khi xóa; kiểm từng đường dẫn trong môi trường thử trước khi tích hợp với agent.

**Lựa chọn để đối chiếu:** [qarmin/czkawka](https://github.com/qarmin/czkawka) · [rclone/rclone](https://github.com/rclone/rclone). Đây là ứng viên so sánh theo tác vụ; mức phù hợp cần kiểm theo hồ sơ và phiên bản riêng.

**Bằng chứng:** `docs-read`, ngày 2026-11-23, commit [`15af96cb100d6ff72ad9ee20d3a81f3bb8ffb3b0`](https://github.com/tw93/Mole/commit/15af96cb100d6ff72ad9ee20d3a81f3bb8ffb3b0), ngày commit 2026-11-23. Đã clone và đọc chọn lọc phần giới thiệu, cách dùng, giới hạn, license, metadata manifest và CI hiện diện. Chưa kiểm đầy đủ implementation hoặc chạy upstream; các số đo của tác giả chưa được tái lập.

**Nguồn:** [README.md](https://github.com/tw93/Mole/blob/15af96cb100d6ff72ad9ee20d3a81f3bb8ffb3b0/README.md) · [LICENSE](https://github.com/tw93/Mole/blob/15af96cb100d6ff72ad9ee20d3a81f3bb8ffb3b0/LICENSE) · [go.mod](https://github.com/tw93/Mole/blob/15af96cb100d6ff72ad9ee20d3a81f3bb8ffb3b0/go.mod) · [.github/workflows/test.yml](https://github.com/tw93/Mole/blob/15af96cb100d6ff72ad9ee20d3a81f3bb8ffb3b0/.github/workflows/test.yml) · [metadata GitHub](https://api.github.com/repos/tw93/Mole).

<a id="anhkysuai-2026-11-23-gorhill-ublock"></a>

### uBlock

**Repo:** [gorhill/uBlock](https://github.com/gorhill/uBlock) · **License:** GPL-3.0 · **★ 69,588 (GitHub API, 2026-11-23)**

**Mục đích:** uBlock Origin: tiện ích trình duyệt chặn nội dung theo các bộ lọc và quy tắc.

**Giá trị:** Tham khảo cơ chế lọc nhiều nguồn và cho phép người dùng tinh chỉnh quy tắc; phạm vi trình duyệt được trình bày riêng trong README.

**Giới hạn:** README ghi Chrome Web Store đã gỡ bản này ngày 31/8/2026; khả năng cài phụ thuộc trình duyệt và kênh phân phối, không suy mọi Chromium còn hỗ trợ như nhau.

**Cách tham khảo/tích hợp:** Đối chiếu môi trường đích và quyền của tiện ích; kiểm tác động lên website cần dùng trước khi thêm bộ lọc.

**Lựa chọn để đối chiếu:** [AdguardTeam/AdGuardHome](https://github.com/AdguardTeam/AdGuardHome) · [pi-hole/pi-hole](https://github.com/pi-hole/pi-hole). Đây là ứng viên so sánh theo tác vụ; mức phù hợp cần kiểm theo hồ sơ và phiên bản riêng.

**Bằng chứng:** `docs-read`, ngày 2026-11-23, commit [`515aad2643a6112ece4d0703453f85d0810fcb78`](https://github.com/gorhill/uBlock/commit/515aad2643a6112ece4d0703453f85d0810fcb78), ngày commit 2026-11-22. Đã clone và đọc chọn lọc phần giới thiệu, cách dùng, giới hạn, license, metadata manifest và CI hiện diện. Chưa kiểm đầy đủ implementation hoặc chạy upstream; các số đo của tác giả chưa được tái lập.

**Nguồn:** [README.md](https://github.com/gorhill/uBlock/blob/515aad2643a6112ece4d0703453f85d0810fcb78/README.md) · [LICENSE.txt](https://github.com/gorhill/uBlock/blob/515aad2643a6112ece4d0703453f85d0810fcb78/LICENSE.txt) · [package.json](https://github.com/gorhill/uBlock/blob/515aad2643a6112ece4d0703453f85d0810fcb78/package.json) · [.github/workflows/main.yml](https://github.com/gorhill/uBlock/blob/515aad2643a6112ece4d0703453f85d0810fcb78/.github/workflows/main.yml) · [metadata GitHub](https://api.github.com/repos/gorhill/uBlock).

<a id="anhkysuai-2026-11-23-alistgo-alist"></a>

### alist

**Repo:** [AlistGo/alist](https://github.com/AlistGo/alist) · **License:** AGPL-3.0 · **★ 50,480 (GitHub API, 2026-11-23)**

**Mục đích:** Dịch vụ liệt kê tệp và WebDAV gom nhiều backend lưu trữ, dùng Go/Gin và SolidJS.

**Giá trị:** Có preview, upload và nhiều adapter cloud, phù hợp tham khảo cách thống nhất truy cập tệp qua một giao diện.

**Giới hạn:** AGPL-3.0; dịch vụ nắm credential và quyền dữ liệu của các backend, còn proxy/preview có thể tạo đường truyền dữ liệu bổ sung.

**Cách tham khảo/tích hợp:** Thử bằng tài khoản ít quyền, kiểm từng adapter và đường tải/preview; tách dịch vụ lưu trữ khỏi quyền tùy ý của agent.

**Lựa chọn để đối chiếu:** [rclone/rclone](https://github.com/rclone/rclone) · [nextcloud/server](https://github.com/nextcloud/server). Đây là ứng viên so sánh theo tác vụ; mức phù hợp cần kiểm theo hồ sơ và phiên bản riêng.

**Bằng chứng:** `docs-read`, ngày 2026-11-23, commit [`92e745360766cce32564f94a468cb576f577d27e`](https://github.com/AlistGo/alist/commit/92e745360766cce32564f94a468cb576f577d27e), ngày commit 2026-10-21. Đã clone và đọc chọn lọc phần giới thiệu, cách dùng, giới hạn, license, metadata manifest và CI hiện diện. Chưa kiểm đầy đủ implementation hoặc chạy upstream; các số đo của tác giả chưa được tái lập.

**Nguồn:** [README.md](https://github.com/AlistGo/alist/blob/92e745360766cce32564f94a468cb576f577d27e/README.md) · [LICENSE](https://github.com/AlistGo/alist/blob/92e745360766cce32564f94a468cb576f577d27e/LICENSE) · [go.mod](https://github.com/AlistGo/alist/blob/92e745360766cce32564f94a468cb576f577d27e/go.mod) · [.github/workflows/build.yml](https://github.com/AlistGo/alist/blob/92e745360766cce32564f94a468cb576f577d27e/.github/workflows/build.yml) · [metadata GitHub](https://api.github.com/repos/AlistGo/alist).

<a id="anhkysuai-2026-11-23-iina-iina"></a>

### iina

**Repo:** [iina/iina](https://github.com/iina/iina) · **License:** GPL-3.0 · **★ 47,238 (GitHub API, 2026-11-23)**

**Mục đích:** Trình phát media native macOS xây trên mpv, hỗ trợ phụ đề, playlist và plugin.

**Giá trị:** Tham khảo cách bọc bộ giải mã mạnh bằng giao diện phù hợp hệ điều hành và mở rộng qua plugin.

**Giới hạn:** Phạm vi chính là macOS; khả năng phát codec phụ thuộc mpv và thư viện đi cùng, không suy từ README thành kết quả đã thử.

**Cách tham khảo/tích hợp:** Dùng bản phát hành phù hợp hệ điều hành, kiểm quyền ứng dụng và thao tác với dữ liệu mẫu; giữ khả năng khôi phục trước tác vụ ghi/xóa.

**Lựa chọn để đối chiếu:** [mpv-player/mpv](https://github.com/mpv-player/mpv) · [videolan/vlc](https://github.com/videolan/vlc). Đây là ứng viên so sánh theo tác vụ; mức phù hợp cần kiểm theo hồ sơ và phiên bản riêng.

**Bằng chứng:** `docs-read`, ngày 2026-11-23, commit [`d71bb5c0feca2dbd9871a97f9091ad44d1079c1d`](https://github.com/iina/iina/commit/d71bb5c0feca2dbd9871a97f9091ad44d1079c1d), ngày commit 2026-11-22. Đã clone và đọc chọn lọc phần giới thiệu, cách dùng, giới hạn, license, metadata manifest và CI hiện diện. Chưa kiểm đầy đủ implementation hoặc chạy upstream; các số đo của tác giả chưa được tái lập.

**Nguồn:** [README.md](https://github.com/iina/iina/blob/d71bb5c0feca2dbd9871a97f9091ad44d1079c1d/README.md) · [LICENSE](https://github.com/iina/iina/blob/d71bb5c0feca2dbd9871a97f9091ad44d1079c1d/LICENSE) · [.github/workflows/ci.yml](https://github.com/iina/iina/blob/d71bb5c0feca2dbd9871a97f9091ad44d1079c1d/.github/workflows/ci.yml) · [metadata GitHub](https://api.github.com/repos/iina/iina).

<a id="anhkysuai-2026-11-23-heyputer-puter"></a>

### puter

**Repo:** [HeyPuter/puter](https://github.com/HeyPuter/puter) · **License:** AGPL-3.0 · **★ 44,233 (GitHub API, 2026-11-23)**

**Mục đích:** Môi trường desktop trong trình duyệt và nền tảng ứng dụng có lưu trữ, API và khả năng tự host.

**Giá trị:** Có giá trị tham khảo cho giao diện gom ứng dụng, quản lý tệp và dịch vụ dùng chung của nhiều app.

**Giới hạn:** AGPL-3.0; tự host mã không tự cấp quyền sử dụng dịch vụ AI/cloud bên ngoài. Các tuyên bố miễn phí và đầy đủ tính năng cần kiểm theo deployment.

**Cách tham khảo/tích hợp:** Dùng bản phát hành phù hợp hệ điều hành, kiểm quyền ứng dụng và thao tác với dữ liệu mẫu; giữ khả năng khôi phục trước tác vụ ghi/xóa.

**Lựa chọn để đối chiếu:** [spacedriveapp/spacedrive](https://github.com/spacedriveapp/spacedrive) · [nextcloud/server](https://github.com/nextcloud/server). Đây là ứng viên so sánh theo tác vụ; mức phù hợp cần kiểm theo hồ sơ và phiên bản riêng.

**Bằng chứng:** `docs-read`, ngày 2026-11-23, commit [`0a5328bb2481cd2d4411d68f8bff055580c784e9`](https://github.com/HeyPuter/puter/commit/0a5328bb2481cd2d4411d68f8bff055580c784e9), ngày commit 2026-11-22. Đã clone và đọc chọn lọc phần giới thiệu, cách dùng, giới hạn, license, metadata manifest và CI hiện diện. Chưa kiểm đầy đủ implementation hoặc chạy upstream; các số đo của tác giả chưa được tái lập.

**Nguồn:** [README.md](https://github.com/HeyPuter/puter/blob/0a5328bb2481cd2d4411d68f8bff055580c784e9/README.md) · [LICENSE.txt](https://github.com/HeyPuter/puter/blob/0a5328bb2481cd2d4411d68f8bff055580c784e9/LICENSE.txt) · [package.json](https://github.com/HeyPuter/puter/blob/0a5328bb2481cd2d4411d68f8bff055580c784e9/package.json) · [.github/workflows/docs-build.yml](https://github.com/HeyPuter/puter/blob/0a5328bb2481cd2d4411d68f8bff055580c784e9/.github/workflows/docs-build.yml) · [metadata GitHub](https://api.github.com/repos/HeyPuter/puter).

<a id="anhkysuai-2026-11-23-schollz-croc"></a>

### croc

**Repo:** [schollz/croc](https://github.com/schollz/croc) · **License:** MIT · **★ 41,000 (GitHub API, 2026-11-23)**

**Mục đích:** CLI truyền tệp/thư mục giữa máy, hỗ trợ kết nối trực tiếp và relay dự phòng.

**Giá trị:** Phù hợp tham khảo luồng ghép phiên bằng mã, truyền đa nền tảng và tiếp tục phiên bị ngắt.

**Giới hạn:** Chưa kiểm giao thức mã hóa hoặc thử truyền; cần phân biệt vai trò relay, code phrase và các tùy chọn ghi đè/tạm lưu.

**Cách tham khảo/tích hợp:** Dùng bản phát hành phù hợp hệ điều hành, kiểm quyền ứng dụng và thao tác với dữ liệu mẫu; giữ khả năng khôi phục trước tác vụ ghi/xóa.

**Lựa chọn để đối chiếu:** [rclone/rclone](https://github.com/rclone/rclone) · [syncthing/syncthing](https://github.com/syncthing/syncthing). Đây là ứng viên so sánh theo tác vụ; mức phù hợp cần kiểm theo hồ sơ và phiên bản riêng.

**Bằng chứng:** `docs-read`, ngày 2026-11-23, commit [`d77d59a8931d67460574f7603b9446470d475070`](https://github.com/schollz/croc/commit/d77d59a8931d67460574f7603b9446470d475070), ngày commit 2026-11-21. Đã clone và đọc chọn lọc phần giới thiệu, cách dùng, giới hạn, license, metadata manifest và CI hiện diện. Chưa kiểm đầy đủ implementation hoặc chạy upstream; các số đo của tác giả chưa được tái lập.

**Nguồn:** [README.md](https://github.com/schollz/croc/blob/d77d59a8931d67460574f7603b9446470d475070/README.md) · [LICENSE](https://github.com/schollz/croc/blob/d77d59a8931d67460574f7603b9446470d475070/LICENSE) · [go.mod](https://github.com/schollz/croc/blob/d77d59a8931d67460574f7603b9446470d475070/go.mod) · [.github/workflows/ci.yml](https://github.com/schollz/croc/blob/d77d59a8931d67460574f7603b9446470d475070/.github/workflows/ci.yml) · [metadata GitHub](https://api.github.com/repos/schollz/croc).

<a id="anhkysuai-2026-11-23-spacedriveapp-spacedrive"></a>

### spacedrive

**Repo:** [spacedriveapp/spacedrive](https://github.com/spacedriveapp/spacedrive) · **License:** Apache-2.0 · **★ 39,580 (GitHub API, 2026-11-23)**

**Mục đích:** Trình quản lý tệp đa nguồn với lớp filesystem phân tán viết bằng Rust.

**Giá trị:** Mô hình index nguồn, lịch sử và API dùng chung đáng tham khảo cho kho dữ liệu dài hạn và app desktop.

**Giới hạn:** README tại SHA đọc ghi beta2.0 dự kiến27/11/2026, beta đầu hỗ trợ macOS/Linux; không ghi phiên bản tương lai là đã phát hành hoặc bảo đảm Windows.

**Cách tham khảo/tích hợp:** Dùng bản phát hành phù hợp hệ điều hành, kiểm quyền ứng dụng và thao tác với dữ liệu mẫu; giữ khả năng khôi phục trước tác vụ ghi/xóa.

**Lựa chọn để đối chiếu:** [HeyPuter/puter](https://github.com/HeyPuter/puter) · [rclone/rclone](https://github.com/rclone/rclone). Đây là ứng viên so sánh theo tác vụ; mức phù hợp cần kiểm theo hồ sơ và phiên bản riêng.

**Bằng chứng:** `docs-read`, ngày 2026-11-23, commit [`30576ad1e5567b26dacdd0a68083ad77f714e960`](https://github.com/spacedriveapp/spacedrive/commit/30576ad1e5567b26dacdd0a68083ad77f714e960), ngày commit 2026-11-22. Đã clone và đọc chọn lọc phần giới thiệu, cách dùng, giới hạn, license, metadata manifest và CI hiện diện. Chưa kiểm đầy đủ implementation hoặc chạy upstream; các số đo của tác giả chưa được tái lập.

**Nguồn:** [README.md](https://github.com/spacedriveapp/spacedrive/blob/30576ad1e5567b26dacdd0a68083ad77f714e960/README.md) · [LICENSE](https://github.com/spacedriveapp/spacedrive/blob/30576ad1e5567b26dacdd0a68083ad77f714e960/LICENSE) · [package.json](https://github.com/spacedriveapp/spacedrive/blob/30576ad1e5567b26dacdd0a68083ad77f714e960/package.json) · [Cargo.toml](https://github.com/spacedriveapp/spacedrive/blob/30576ad1e5567b26dacdd0a68083ad77f714e960/Cargo.toml) · [.github/workflows/ci.yml](https://github.com/spacedriveapp/spacedrive/blob/30576ad1e5567b26dacdd0a68083ad77f714e960/.github/workflows/ci.yml) · [metadata GitHub](https://api.github.com/repos/spacedriveapp/spacedrive).

<a id="anhkysuai-2026-11-23-pbatard-rufus"></a>

### rufus

**Repo:** [pbatard/rufus](https://github.com/pbatard/rufus) · **License:** GPL-3.0 · **★ 38,468 (GitHub API, 2026-11-23)**

**Mục đích:** Tiện ích Windows định dạng và tạo USB khởi động từ nhiều loại ảnh hệ điều hành.

**Giá trị:** Tham khảo luồng chọn thiết bị, định dạng và chuẩn BIOS/UEFI trong một công cụ có phạm vi rõ.

**Giới hạn:** Thao tác ghi thiết bị có thể xóa dữ liệu; chưa chạy hoặc kiểm khả năng boot của bất kỳ ảnh nào trong đợt này.

**Cách tham khảo/tích hợp:** Dùng bản phát hành phù hợp hệ điều hành, kiểm quyền ứng dụng và thao tác với dữ liệu mẫu; giữ khả năng khôi phục trước tác vụ ghi/xóa.

**Lựa chọn để đối chiếu:** [ventoy/Ventoy](https://github.com/ventoy/Ventoy) · [balena-io/etcher](https://github.com/balena-io/etcher). Đây là ứng viên so sánh theo tác vụ; mức phù hợp cần kiểm theo hồ sơ và phiên bản riêng.

**Bằng chứng:** `docs-read`, ngày 2026-11-23, commit [`bed2c33669048a432c7135441d8cbcae72fd315f`](https://github.com/pbatard/rufus/commit/bed2c33669048a432c7135441d8cbcae72fd315f), ngày commit 2026-11-17. Đã clone và đọc chọn lọc phần giới thiệu, cách dùng, giới hạn, license, metadata manifest và CI hiện diện. Chưa kiểm đầy đủ implementation hoặc chạy upstream; các số đo của tác giả chưa được tái lập.

**Nguồn:** [README.md](https://github.com/pbatard/rufus/blob/bed2c33669048a432c7135441d8cbcae72fd315f/README.md) · [LICENSE.txt](https://github.com/pbatard/rufus/blob/bed2c33669048a432c7135441d8cbcae72fd315f/LICENSE.txt) · [.github/workflows/lock.yml](https://github.com/pbatard/rufus/blob/bed2c33669048a432c7135441d8cbcae72fd315f/.github/workflows/lock.yml) · [metadata GitHub](https://api.github.com/repos/pbatard/rufus).

<a id="anhkysuai-2026-11-23-permissionlesstech-bitchat"></a>

### bitchat

**Repo:** [permissionlesstech/bitchat](https://github.com/permissionlesstech/bitchat) · **License:** Unlicense · **★ 37,198 (GitHub API, 2026-11-23)**

**Mục đích:** Ứng dụng nhắn tin dùng Bluetooth mesh khi offline và Nostr khi có Internet.

**Giá trị:** Tham khảo thiết kế hai lớp truyền và định tuyến tin trực tiếp trong ứng dụng không dựa trên tài khoản số điện thoại.

**Giới hạn:** Chưa audit mật mã, quyền thiết bị hoặc rò rỉ metadata; nhãn phi tập trung không chứng minh ẩn danh. README yêu cầu kiểm nguồn của bản biên dịch.

**Cách tham khảo/tích hợp:** Dùng bản phát hành phù hợp hệ điều hành, kiểm quyền ứng dụng và thao tác với dữ liệu mẫu; giữ khả năng khôi phục trước tác vụ ghi/xóa.

**Lựa chọn để đối chiếu:** [zulip/zulip](https://github.com/zulip/zulip) · [matrix-org/synapse](https://github.com/matrix-org/synapse). Đây là ứng viên so sánh theo tác vụ; mức phù hợp cần kiểm theo hồ sơ và phiên bản riêng.

**Bằng chứng:** `docs-read`, ngày 2026-11-23, commit [`04995f68e470a18d1fc99f86fa326c2a87bab4f2`](https://github.com/permissionlesstech/bitchat/commit/04995f68e470a18d1fc99f86fa326c2a87bab4f2), ngày commit 2026-10-25. Đã clone và đọc chọn lọc phần giới thiệu, cách dùng, giới hạn, license, metadata manifest và CI hiện diện. Chưa kiểm đầy đủ implementation hoặc chạy upstream; các số đo của tác giả chưa được tái lập.

**Nguồn:** [README.md](https://github.com/permissionlesstech/bitchat/blob/04995f68e470a18d1fc99f86fa326c2a87bab4f2/README.md) · [LICENSE](https://github.com/permissionlesstech/bitchat/blob/04995f68e470a18d1fc99f86fa326c2a87bab4f2/LICENSE) · [.github/workflows/swift-tests.yml](https://github.com/permissionlesstech/bitchat/blob/04995f68e470a18d1fc99f86fa326c2a87bab4f2/.github/workflows/swift-tests.yml) · [metadata GitHub](https://api.github.com/repos/permissionlesstech/bitchat).

<a id="anhkysuai-2026-11-23-vorssaint-vorssaint-utils"></a>

### vorssaint-utils

**Repo:** [vorssaint/vorssaint-utils](https://github.com/vorssaint/vorssaint-utils) · **License:** GPL-3.0 · **★ 35,826 (GitHub API, 2026-11-23)**

**Mục đích:** Bộ tiện ích thanh menu macOS cho âm thanh, cửa sổ, clipboard, tệp và theo dõi hệ thống.

**Giá trị:** Thiết kế bật riêng từng tính năng giúp tham khảo cách gom nhiều tiện ích mà giữ lựa chọn của người dùng.

**Giới hạn:** Tuyên bố không telemetry mới được đọc từ README, chưa kiểm đường mạng; tên/logo có chính sách riêng ngoài GPL-3.0-or-later.

**Cách tham khảo/tích hợp:** Dùng bản phát hành phù hợp hệ điều hành, kiểm quyền ứng dụng và thao tác với dữ liệu mẫu; giữ khả năng khôi phục trước tác vụ ghi/xóa.

**Lựa chọn để đối chiếu:** [MonitorControl/MonitorControl](https://github.com/MonitorControl/MonitorControl) · [tw93/Mole](https://github.com/tw93/Mole). Đây là ứng viên so sánh theo tác vụ; mức phù hợp cần kiểm theo hồ sơ và phiên bản riêng.

**Bằng chứng:** `docs-read`, ngày 2026-11-23, commit [`21682edaac2958577267ab7d0940a7b2d1662eb7`](https://github.com/vorssaint/vorssaint-utils/commit/21682edaac2958577267ab7d0940a7b2d1662eb7), ngày commit 2026-11-23. Đã clone và đọc chọn lọc phần giới thiệu, cách dùng, giới hạn, license, metadata manifest và CI hiện diện. Chưa kiểm đầy đủ implementation hoặc chạy upstream; các số đo của tác giả chưa được tái lập.

**Nguồn:** [README.md](https://github.com/vorssaint/vorssaint-utils/blob/21682edaac2958577267ab7d0940a7b2d1662eb7/README.md) · [LICENSE](https://github.com/vorssaint/vorssaint-utils/blob/21682edaac2958577267ab7d0940a7b2d1662eb7/LICENSE) · [.github/workflows/ci.yml](https://github.com/vorssaint/vorssaint-utils/blob/21682edaac2958577267ab7d0940a7b2d1662eb7/.github/workflows/ci.yml) · [metadata GitHub](https://api.github.com/repos/vorssaint/vorssaint-utils).

<a id="anhkysuai-2026-11-23-qarmin-czkawka"></a>

### czkawka

**Repo:** [qarmin/czkawka](https://github.com/qarmin/czkawka) · **License:** MIT / GPL-3.0-only theo ứng dụng; CC BY-4.0 cho ảnh/âm thanh · **★ 35,440 (GitHub API, 2026-11-23)**

**Mục đích:** Bộ công cụ tìm tệp trùng, thư mục rỗng và ảnh tương tự với core Rust cùng nhiều frontend.

**Giá trị:** Tách core khỏi GUI/CLI và hỗ trợ các kiểu tìm khác nhau, hữu ích tham khảo thiết kế công cụ dọn dữ liệu.

**Giới hạn:** README khuyên chuyển GTK GUI sang Krokiet; MIT cho một số thành phần, GPL-3.0-only cho Krokiet/Cedinia và CC BY4.0 cho media. Chưa chạy hay kiểm an toàn xóa.

**Cách tham khảo/tích hợp:** Dùng bản phát hành phù hợp hệ điều hành, kiểm quyền ứng dụng và thao tác với dữ liệu mẫu; giữ khả năng khôi phục trước tác vụ ghi/xóa.

**Lựa chọn để đối chiếu:** [tw93/Mole](https://github.com/tw93/Mole) · [rclone/rclone](https://github.com/rclone/rclone). Đây là ứng viên so sánh theo tác vụ; mức phù hợp cần kiểm theo hồ sơ và phiên bản riêng.

**Bằng chứng:** `docs-read`, ngày 2026-11-23, commit [`1cdc6a4373b6a626c3a306e455b79576357a0b41`](https://github.com/qarmin/czkawka/commit/1cdc6a4373b6a626c3a306e455b79576357a0b41), ngày commit 2026-11-15. Đã clone và đọc chọn lọc phần giới thiệu, cách dùng, giới hạn, license, metadata manifest và CI hiện diện. Chưa kiểm đầy đủ implementation hoặc chạy upstream; các số đo của tác giả chưa được tái lập.

**Nguồn:** [README.md](https://github.com/qarmin/czkawka/blob/1cdc6a4373b6a626c3a306e455b79576357a0b41/README.md) · [LICENSE_CC_BY_4_ICONS](https://github.com/qarmin/czkawka/blob/1cdc6a4373b6a626c3a306e455b79576357a0b41/LICENSE_CC_BY_4_ICONS) · [LICENSE_MIT_EVERYTHING_OUTSIDE_ANY_CARGO_APP_LIBRARY](https://github.com/qarmin/czkawka/blob/1cdc6a4373b6a626c3a306e455b79576357a0b41/LICENSE_MIT_EVERYTHING_OUTSIDE_ANY_CARGO_APP_LIBRARY) · [Cargo.toml](https://github.com/qarmin/czkawka/blob/1cdc6a4373b6a626c3a306e455b79576357a0b41/Cargo.toml) · [.github/workflows/mac.yml](https://github.com/qarmin/czkawka/blob/1cdc6a4373b6a626c3a306e455b79576357a0b41/.github/workflows/mac.yml) · [metadata GitHub](https://api.github.com/repos/qarmin/czkawka).

<a id="anhkysuai-2026-11-23-monitorcontrol-monitorcontrol"></a>

### MonitorControl

**Repo:** [MonitorControl/MonitorControl](https://github.com/MonitorControl/MonitorControl) · **License:** MIT · **★ 34,803 (GitHub API, 2026-11-23)**

**Mục đích:** Ứng dụng macOS điều chỉnh độ sáng, âm lượng và tương phản màn hình từ menu hoặc phím.

**Giá trị:** Phân biệt DDC, giao thức Apple và làm tối bằng phần mềm, hữu ích tham khảo lớp adapter phần cứng.

**Giới hạn:** Khả năng điều khiển phụ thuộc màn hình, cáp và giao thức; chưa thử trên phần cứng thật.

**Cách tham khảo/tích hợp:** Dùng bản phát hành phù hợp hệ điều hành, kiểm quyền ứng dụng và thao tác với dữ liệu mẫu; giữ khả năng khôi phục trước tác vụ ghi/xóa.

**Lựa chọn để đối chiếu:** [vorssaint/vorssaint-utils](https://github.com/vorssaint/vorssaint-utils) · [jordanbaird/Ice](https://github.com/jordanbaird/Ice). Đây là ứng viên so sánh theo tác vụ; mức phù hợp cần kiểm theo hồ sơ và phiên bản riêng.

**Bằng chứng:** `docs-read`, ngày 2026-11-23, commit [`7cfe64500d19cbbcbf82121a91c826f658a403bd`](https://github.com/MonitorControl/MonitorControl/commit/7cfe64500d19cbbcbf82121a91c826f658a403bd), ngày commit 2026-10-14. Đã clone và đọc chọn lọc phần giới thiệu, cách dùng, giới hạn, license, metadata manifest và CI hiện diện. Chưa kiểm đầy đủ implementation hoặc chạy upstream; các số đo của tác giả chưa được tái lập.

**Nguồn:** [README.md](https://github.com/MonitorControl/MonitorControl/blob/7cfe64500d19cbbcbf82121a91c826f658a403bd/README.md) · [License.txt](https://github.com/MonitorControl/MonitorControl/blob/7cfe64500d19cbbcbf82121a91c826f658a403bd/License.txt) · [metadata GitHub](https://api.github.com/repos/MonitorControl/MonitorControl).

<a id="anhkysuai-2026-11-23-chubin-wttr.in"></a>

### wttr.in

**Repo:** [chubin/wttr.in](https://github.com/chubin/wttr.in) · **License:** Apache-2.0 · **★ 30,812 (GitHub API, 2026-11-23)**

**Mục đích:** Dịch vụ dự báo thời tiết hướng terminal, có nhiều dạng đầu ra như văn bản, hình và JSON.

**Giá trị:** Một API biểu diễn thông tin theo client phù hợp để tham khảo UX dòng lệnh và định dạng đáp ứng.

**Giới hạn:** Dữ liệu dự báo đến từ nguồn bên ngoài; không đánh giá độ đúng thời tiết hoặc SLA của dịch vụ công cộng.

**Cách tham khảo/tích hợp:** Dùng bản phát hành phù hợp hệ điều hành, kiểm quyền ứng dụng và thao tác với dữ liệu mẫu; giữ khả năng khôi phục trước tác vụ ghi/xóa.

**Lựa chọn để đối chiếu:** [open-meteo/open-meteo](https://github.com/open-meteo/open-meteo) · [public-apis/public-apis](https://github.com/public-apis/public-apis). Đây là ứng viên so sánh theo tác vụ; mức phù hợp cần kiểm theo hồ sơ và phiên bản riêng.

**Bằng chứng:** `docs-read`, ngày 2026-11-23, commit [`3873fd294bb6fadfcf6e4391e0f0666bf827fcf5`](https://github.com/chubin/wttr.in/commit/3873fd294bb6fadfcf6e4391e0f0666bf827fcf5), ngày commit 2026-11-22. Đã clone và đọc chọn lọc phần giới thiệu, cách dùng, giới hạn, license, metadata manifest và CI hiện diện. Chưa kiểm đầy đủ implementation hoặc chạy upstream; các số đo của tác giả chưa được tái lập.

**Nguồn:** [README.md](https://github.com/chubin/wttr.in/blob/3873fd294bb6fadfcf6e4391e0f0666bf827fcf5/README.md) · [LICENSE](https://github.com/chubin/wttr.in/blob/3873fd294bb6fadfcf6e4391e0f0666bf827fcf5/LICENSE) · [go.mod](https://github.com/chubin/wttr.in/blob/3873fd294bb6fadfcf6e4391e0f0666bf827fcf5/go.mod) · [.github/workflows/makefile.yml](https://github.com/chubin/wttr.in/blob/3873fd294bb6fadfcf6e4391e0f0666bf827fcf5/.github/workflows/makefile.yml) · [metadata GitHub](https://api.github.com/repos/chubin/wttr.in).

<a id="anhkysuai-2026-11-23-ente-ente"></a>

### ente

**Repo:** [ente/ente](https://github.com/ente/ente) · **License:** AGPL-3.0 · **★ 30,410 (GitHub API, 2026-11-23)**

**Mục đích:** Nền tảng lưu trữ và ứng dụng có mã hóa đầu-cuối cho ảnh, xác thực và tài liệu.

**Giá trị:** Monorepo nhiều client cho phép tham khảo cách chia dịch vụ lưu trữ và trải nghiệm đa nền tảng.

**Giới hạn:** Tuyên bố E2EE được đọc từ tài liệu, chưa audit mật mã hoặc luồng khôi phục khóa; AGPL-3.0 và phụ thuộc hạ tầng cần xem khi tự host.

**Cách tham khảo/tích hợp:** Dùng bản phát hành phù hợp hệ điều hành, kiểm quyền ứng dụng và thao tác với dữ liệu mẫu; giữ khả năng khôi phục trước tác vụ ghi/xóa.

**Lựa chọn để đối chiếu:** [immich-app/immich](https://github.com/immich-app/immich) · [nextcloud/server](https://github.com/nextcloud/server). Đây là ứng viên so sánh theo tác vụ; mức phù hợp cần kiểm theo hồ sơ và phiên bản riêng.

**Bằng chứng:** `docs-read`, ngày 2026-11-23, commit [`6ace5d36ec91d96caf3f17d08cb41a945741c301`](https://github.com/ente/ente/commit/6ace5d36ec91d96caf3f17d08cb41a945741c301), ngày commit 2026-11-23. Đã clone và đọc chọn lọc phần giới thiệu, cách dùng, giới hạn, license, metadata manifest và CI hiện diện. Chưa kiểm đầy đủ implementation hoặc chạy upstream; các số đo của tác giả chưa được tái lập.

**Nguồn:** [README.md](https://github.com/ente/ente/blob/6ace5d36ec91d96caf3f17d08cb41a945741c301/README.md) · [LICENSE](https://github.com/ente/ente/blob/6ace5d36ec91d96caf3f17d08cb41a945741c301/LICENSE) · [.github/workflows/ci.yml](https://github.com/ente/ente/blob/6ace5d36ec91d96caf3f17d08cb41a945741c301/.github/workflows/ci.yml) · [metadata GitHub](https://api.github.com/repos/ente/ente).

<a id="anhkysuai-2026-11-23-jordanbaird-ice"></a>

### Ice

**Repo:** [jordanbaird/Ice](https://github.com/jordanbaird/Ice) · **License:** GPL-3.0 · **★ 30,088 (GitHub API, 2026-11-23)**

**Mục đích:** Ứng dụng macOS để sắp xếp, ẩn và hiện các biểu tượng trên menu bar.

**Giá trị:** README tách rõ tính năng đã có và roadmap, giúp đối chiếu nhu cầu quản lý menu bar cụ thể.

**Giới hạn:** README còn mô tả active development nhưng commit được clone từ năm 2025; không suy trạng thái bảo trì hiện tại chỉ từ câu quảng bá. Cần thử quyền hệ thống và phiên bản macOS đích.

**Cách tham khảo/tích hợp:** Dùng bản phát hành phù hợp hệ điều hành, kiểm quyền ứng dụng và thao tác với dữ liệu mẫu; giữ khả năng khôi phục trước tác vụ ghi/xóa.

**Lựa chọn để đối chiếu:** [dwarvesf/hidden](https://github.com/dwarvesf/hidden) · [MonitorControl/MonitorControl](https://github.com/MonitorControl/MonitorControl). Đây là ứng viên so sánh theo tác vụ; mức phù hợp cần kiểm theo hồ sơ và phiên bản riêng.

**Bằng chứng:** `docs-read`, ngày 2026-11-23, commit [`11edd39115f3f43a83ae114b5348df6a0e1741cf`](https://github.com/jordanbaird/Ice/commit/11edd39115f3f43a83ae114b5348df6a0e1741cf), ngày commit 2025-09-20. Đã clone và đọc chọn lọc phần giới thiệu, cách dùng, giới hạn, license, metadata manifest và CI hiện diện. Chưa kiểm đầy đủ implementation hoặc chạy upstream; các số đo của tác giả chưa được tái lập.

**Nguồn:** [README.md](https://github.com/jordanbaird/Ice/blob/11edd39115f3f43a83ae114b5348df6a0e1741cf/README.md) · [LICENSE](https://github.com/jordanbaird/Ice/blob/11edd39115f3f43a83ae114b5348df6a0e1741cf/LICENSE) · [.github/workflows/lint.yml](https://github.com/jordanbaird/Ice/blob/11edd39115f3f43a83ae114b5348df6a0e1741cf/.github/workflows/lint.yml) · [metadata GitHub](https://api.github.com/repos/jordanbaird/Ice).

<a id="anhkysuai-2026-11-23-nickemanarin-screentogif"></a>

### ScreenToGif

**Repo:** [NickeManarin/ScreenToGif](https://github.com/NickeManarin/ScreenToGif) · **License:** MS-PL · **★ 27,984 (GitHub API, 2026-11-23)**

**Mục đích:** Ứng dụng Windows ghi vùng màn hình, chỉnh từng khung và xuất GIF hoặc video.

**Giá trị:** Hợp làm hình minh họa thao tác và tái hiện lỗi ngắn; quy trình ghi và chỉnh sửa nằm trong cùng công cụ.

**Giới hạn:** README yêu cầu .NET 9 Desktop Runtime hoặc mới hơn; cần kiểm khả năng chạy trên máy đích và tránh ghi lộ dữ liệu trong vùng màn hình.

**Cách tham khảo/tích hợp:** Dùng bản phát hành phù hợp hệ điều hành, kiểm quyền ứng dụng và thao tác với dữ liệu mẫu; giữ khả năng khôi phục trước tác vụ ghi/xóa.

**Lựa chọn để đối chiếu:** [ShareX/ShareX](https://github.com/ShareX/ShareX) · [obsproject/obs-studio](https://github.com/obsproject/obs-studio). Đây là ứng viên so sánh theo tác vụ; mức phù hợp cần kiểm theo hồ sơ và phiên bản riêng.

**Bằng chứng:** `docs-read`, ngày 2026-11-23, commit [`a4d0a67c2131cd048ceec86cd40afc2f1a06f2fd`](https://github.com/NickeManarin/ScreenToGif/commit/a4d0a67c2131cd048ceec86cd40afc2f1a06f2fd), ngày commit 2026-07-28. Đã clone và đọc chọn lọc phần giới thiệu, cách dùng, giới hạn, license, metadata manifest và CI hiện diện. Chưa kiểm đầy đủ implementation hoặc chạy upstream; các số đo của tác giả chưa được tái lập.

**Nguồn:** [README.md](https://github.com/NickeManarin/ScreenToGif/blob/a4d0a67c2131cd048ceec86cd40afc2f1a06f2fd/README.md) · [LICENSE.txt](https://github.com/NickeManarin/ScreenToGif/blob/a4d0a67c2131cd048ceec86cd40afc2f1a06f2fd/LICENSE.txt) · [.github/workflows/discord-releases.yml](https://github.com/NickeManarin/ScreenToGif/blob/a4d0a67c2131cd048ceec86cd40afc2f1a06f2fd/.github/workflows/discord-releases.yml) · [metadata GitHub](https://api.github.com/repos/NickeManarin/ScreenToGif).

<a id="anhkysuai-2026-11-23-gopeedlab-gopeed"></a>

### gopeed

**Repo:** [GopeedLab/gopeed](https://github.com/GopeedLab/gopeed) · **License:** GPL-3.0 · **★ 27,904 (GitHub API, 2026-11-23)**

**Mục đích:** Trình quản lý tải đa nền tảng viết bằng Go và Flutter, hỗ trợ HTTP, torrent, magnet và ed2k.

**Giá trị:** REST API, CLI và extension JavaScript được tài liệu hóa, phù hợp nghiên cứu quy trình tải có hàng đợi và tự động hóa.

**Giới hạn:** Tuyên bố tốc độ chưa được đo ở lượt này; extension và giao diện web tự host mở thêm bề mặt quyền truy cập, cần kiểm trước khi cấp đường dẫn và tài khoản tải.

**Cách tham khảo/tích hợp:** Dùng bản phát hành phù hợp hệ điều hành, kiểm quyền ứng dụng và thao tác với dữ liệu mẫu; giữ khả năng khôi phục trước tác vụ ghi/xóa.

**Lựa chọn để đối chiếu:** [aria2/aria2](https://github.com/aria2/aria2) · [rclone/rclone](https://github.com/rclone/rclone). Đây là ứng viên so sánh theo tác vụ; mức phù hợp cần kiểm theo hồ sơ và phiên bản riêng.

**Bằng chứng:** `docs-read`, ngày 2026-11-23, commit [`996685c8478ac055f4842746682b1db2a8b810f8`](https://github.com/GopeedLab/gopeed/commit/996685c8478ac055f4842746682b1db2a8b810f8), ngày commit 2026-11-22. Đã clone và đọc chọn lọc phần giới thiệu, cách dùng, giới hạn, license, metadata manifest và CI hiện diện. Chưa kiểm đầy đủ implementation hoặc chạy upstream; các số đo của tác giả chưa được tái lập.

**Nguồn:** [README.md](https://github.com/GopeedLab/gopeed/blob/996685c8478ac055f4842746682b1db2a8b810f8/README.md) · [LICENSE](https://github.com/GopeedLab/gopeed/blob/996685c8478ac055f4842746682b1db2a8b810f8/LICENSE) · [go.mod](https://github.com/GopeedLab/gopeed/blob/996685c8478ac055f4842746682b1db2a8b810f8/go.mod) · [.github/workflows/test.yml](https://github.com/GopeedLab/gopeed/blob/996685c8478ac055f4842746682b1db2a8b810f8/.github/workflows/test.yml) · [metadata GitHub](https://api.github.com/repos/GopeedLab/gopeed).

<a id="anhkysuai-2026-11-23-molunerfinn-picgo"></a>

### PicGo

**Repo:** [Molunerfinn/PicGo](https://github.com/Molunerfinn/PicGo) · **License:** MIT · **★ 27,514 (GitHub API, 2026-11-23)**

**Mục đích:** Ứng dụng tải ảnh lên dịch vụ lưu trữ và chép link cho trình soạn thảo, hỗ trợ hệ plugin.

**Giá trị:** Có thể giảm thao tác khi viết tài liệu với nhiều ảnh và nhiều định dạng liên kết.

**Giới hạn:** Bản hiện tại đặt PicGo Cloud làm mặc định cho cài mới; nhà cung cấp, plugin và token lưu trữ có điều khoản/quyền riêng. Không suy MIT của ứng dụng bao gồm dịch vụ cloud.

**Cách tham khảo/tích hợp:** Dùng bản phát hành phù hợp hệ điều hành, kiểm quyền ứng dụng và thao tác với dữ liệu mẫu; giữ khả năng khôi phục trước tác vụ ghi/xóa.

**Lựa chọn để đối chiếu:** [ShareX/ShareX](https://github.com/ShareX/ShareX) · [rclone/rclone](https://github.com/rclone/rclone). Đây là ứng viên so sánh theo tác vụ; mức phù hợp cần kiểm theo hồ sơ và phiên bản riêng.

**Bằng chứng:** `docs-read`, ngày 2026-11-23, commit [`bf4069bd3bdbec9b33d43e37df6bc91265415d47`](https://github.com/Molunerfinn/PicGo/commit/bf4069bd3bdbec9b33d43e37df6bc91265415d47), ngày commit 2026-11-17. Đã clone và đọc chọn lọc phần giới thiệu, cách dùng, giới hạn, license, metadata manifest và CI hiện diện. Chưa kiểm đầy đủ implementation hoặc chạy upstream; các số đo của tác giả chưa được tái lập.

**Nguồn:** [README.md](https://github.com/Molunerfinn/PicGo/blob/bf4069bd3bdbec9b33d43e37df6bc91265415d47/README.md) · [LICENSE](https://github.com/Molunerfinn/PicGo/blob/bf4069bd3bdbec9b33d43e37df6bc91265415d47/LICENSE) · [package.json](https://github.com/Molunerfinn/PicGo/blob/bf4069bd3bdbec9b33d43e37df6bc91265415d47/package.json) · [.github/workflows/ci-check.yml](https://github.com/Molunerfinn/PicGo/blob/bf4069bd3bdbec9b33d43e37df6bc91265415d47/.github/workflows/ci-check.yml) · [metadata GitHub](https://api.github.com/repos/Molunerfinn/PicGo).

<a id="anhkysuai-2026-11-23-kovidgoyal-calibre"></a>

### calibre

**Repo:** [kovidgoyal/calibre](https://github.com/kovidgoyal/calibre) · **License:** GPL-3.0 · **★ 26,497 (GitHub API, 2026-11-23)**

**Mục đích:** Bộ quản lý ebook đa nền tảng để tổ chức thư viện, đọc, chuyển đổi và chỉnh sửa sách.

**Giá trị:** Bao quát nhiều bước xử lý ebook và tương tác thiết bị đọc; phù hợp tham khảo luồng metadata và chuyển đổi định dạng.

**Giới hạn:** COPYRIGHT liệt kê nhiều thành phần có giấy phép riêng; chuyển đổi cần kiểm kết quả bố cục và quyền của từng ebook. Lượt đọc này chưa chạy bộ chuyển đổi.

**Cách tham khảo/tích hợp:** Dùng bản phát hành phù hợp hệ điều hành, kiểm quyền ứng dụng và thao tác với dữ liệu mẫu; giữ khả năng khôi phục trước tác vụ ghi/xóa.

**Lựa chọn để đối chiếu:** [readest/readest](https://github.com/readest/readest) · [koreader/koreader](https://github.com/koreader/koreader). Đây là ứng viên so sánh theo tác vụ; mức phù hợp cần kiểm theo hồ sơ và phiên bản riêng.

**Bằng chứng:** `docs-read`, ngày 2026-11-23, commit [`443ecd46162912147ac991fa84b563930cbfa1cf`](https://github.com/kovidgoyal/calibre/commit/443ecd46162912147ac991fa84b563930cbfa1cf), ngày commit 2026-11-23. Đã clone và đọc chọn lọc phần giới thiệu, cách dùng, giới hạn, license, metadata manifest và CI hiện diện. Chưa kiểm đầy đủ implementation hoặc chạy upstream; các số đo của tác giả chưa được tái lập.

**Nguồn:** [README.md](https://github.com/kovidgoyal/calibre/blob/443ecd46162912147ac991fa84b563930cbfa1cf/README.md) · [COPYRIGHT](https://github.com/kovidgoyal/calibre/blob/443ecd46162912147ac991fa84b563930cbfa1cf/COPYRIGHT) · [LICENSE](https://github.com/kovidgoyal/calibre/blob/443ecd46162912147ac991fa84b563930cbfa1cf/LICENSE) · [LICENSE.rtf](https://github.com/kovidgoyal/calibre/blob/443ecd46162912147ac991fa84b563930cbfa1cf/LICENSE.rtf) · [pyproject.toml](https://github.com/kovidgoyal/calibre/blob/443ecd46162912147ac991fa84b563930cbfa1cf/pyproject.toml) · [.github/workflows/ci.yml](https://github.com/kovidgoyal/calibre/blob/443ecd46162912147ac991fa84b563930cbfa1cf/.github/workflows/ci.yml) · [metadata GitHub](https://api.github.com/repos/kovidgoyal/calibre).

<a id="anhkysuai-2026-11-23-aprilnea-openlogi"></a>

### OpenLogi

**Repo:** [AprilNEA/OpenLogi](https://github.com/AprilNEA/OpenLogi) · **License:** MIT OR Apache-2.0 (mã); tài sản thương hiệu riêng · **★ 26,065 (GitHub API, 2026-11-23)**

**Mục đích:** Ứng dụng Rust cấu hình thiết bị Logitech qua HID++, có giao diện native và API tự động hóa JSON.

**Giá trị:** Hỗ trợ cấu hình TOML và cả GUI/CLI, phù hợp nghiên cứu điều khiển ngoại vi trên nhiều hệ điều hành.

**Giới hạn:** README ghi chưa ổn định; danh sách thiết bị và quyền hệ thống cần kiểm riêng. Mã MIT OR Apache-2.0, nhưng logo/icon trong design là all rights reserved.

**Cách tham khảo/tích hợp:** Dùng bản phát hành phù hợp hệ điều hành, kiểm quyền ứng dụng và thao tác với dữ liệu mẫu; giữ khả năng khôi phục trước tác vụ ghi/xóa.

**Lựa chọn để đối chiếu:** [pwr-Solaar/Solaar](https://github.com/pwr-Solaar/Solaar) · [PixlOne/logiops](https://github.com/PixlOne/logiops). Đây là ứng viên so sánh theo tác vụ; mức phù hợp cần kiểm theo hồ sơ và phiên bản riêng.

**Bằng chứng:** `docs-read`, ngày 2026-11-23, commit [`da245558a4cafef5271480cc10e633c901f62a82`](https://github.com/AprilNEA/OpenLogi/commit/da245558a4cafef5271480cc10e633c901f62a82), ngày commit 2026-11-23. Đã clone và đọc chọn lọc phần giới thiệu, cách dùng, giới hạn, license, metadata manifest và CI hiện diện. Chưa kiểm đầy đủ implementation hoặc chạy upstream; các số đo của tác giả chưa được tái lập.

**Nguồn:** [README.md](https://github.com/AprilNEA/OpenLogi/blob/da245558a4cafef5271480cc10e633c901f62a82/README.md) · [LICENSE-APACHE](https://github.com/AprilNEA/OpenLogi/blob/da245558a4cafef5271480cc10e633c901f62a82/LICENSE-APACHE) · [LICENSE-MIT](https://github.com/AprilNEA/OpenLogi/blob/da245558a4cafef5271480cc10e633c901f62a82/LICENSE-MIT) · [Cargo.toml](https://github.com/AprilNEA/OpenLogi/blob/da245558a4cafef5271480cc10e633c901f62a82/Cargo.toml) · [.github/workflows/ci.yml](https://github.com/AprilNEA/OpenLogi/blob/da245558a4cafef5271480cc10e633c901f62a82/.github/workflows/ci.yml) · [metadata GitHub](https://api.github.com/repos/AprilNEA/OpenLogi).

<a id="anhkysuai-2026-11-23-ayangweb-bongocat"></a>

### BongoCat

**Repo:** [ayangweb/BongoCat](https://github.com/ayangweb/BongoCat) · **License:** Apache-2.0 · **★ 24,760 (GitHub API, 2026-11-23)**

**Mục đích:** Thú cưng desktop Live2D phản ứng với phím, chuột và gamepad trên Windows/macOS.

**Giá trị:** Hỗ trợ thay model và hiển thị phản hồi thao tác, phù hợp làm overlay hoặc tham khảo tương tác desktop.

**Giới hạn:** Tuyên bố offline/không thu dữ liệu mới được đọc trong tài liệu; quyền model Live2D và quyền theo dõi input cần xem riêng với từng bản phân phối.

**Cách tham khảo/tích hợp:** Dùng bản phát hành phù hợp hệ điều hành, kiểm quyền ứng dụng và thao tác với dữ liệu mẫu; giữ khả năng khôi phục trước tác vụ ghi/xóa.

**Lựa chọn để đối chiếu:** [MMmmmoko/Bongo-Cat-Mver](https://github.com/MMmmmoko/Bongo-Cat-Mver) · [MagicMirrorOrg/MagicMirror](https://github.com/MagicMirrorOrg/MagicMirror). Đây là ứng viên so sánh theo tác vụ; mức phù hợp cần kiểm theo hồ sơ và phiên bản riêng.

**Bằng chứng:** `docs-read`, ngày 2026-11-23, commit [`47a73ed1765b13fdd674ec356d51b5b16a6b5a5b`](https://github.com/ayangweb/BongoCat/commit/47a73ed1765b13fdd674ec356d51b5b16a6b5a5b), ngày commit 2026-10-28. Đã clone và đọc chọn lọc phần giới thiệu, cách dùng, giới hạn, license, metadata manifest và CI hiện diện. Chưa kiểm đầy đủ implementation hoặc chạy upstream; các số đo của tác giả chưa được tái lập.

**Nguồn:** [README.md](https://github.com/ayangweb/BongoCat/blob/47a73ed1765b13fdd674ec356d51b5b16a6b5a5b/README.md) · [LICENSE](https://github.com/ayangweb/BongoCat/blob/47a73ed1765b13fdd674ec356d51b5b16a6b5a5b/LICENSE) · [Cargo.toml](https://github.com/ayangweb/BongoCat/blob/47a73ed1765b13fdd674ec356d51b5b16a6b5a5b/Cargo.toml) · [.github/workflows/verify.yml](https://github.com/ayangweb/BongoCat/blob/47a73ed1765b13fdd674ec356d51b5b16a6b5a5b/.github/workflows/verify.yml) · [metadata GitHub](https://api.github.com/repos/ayangweb/BongoCat).

<a id="anhkysuai-2026-11-23-magicmirrororg-magicmirror"></a>

### MagicMirror

**Repo:** [MagicMirrorOrg/MagicMirror](https://github.com/MagicMirrorOrg/MagicMirror) · **License:** MIT · **★ 24,241 (GitHub API, 2026-11-23)**

**Mục đích:** Nền tảng gương thông minh dạng mô-đun sử dụng Electron và hệ module mở rộng.

**Giá trị:** Cho phép tổ chức các khối thông tin thành dashboard cá nhân; cách phân tách module hữu ích cho màn hình thông tin tại chỗ.

**Giới hạn:** Mỗi module ngoài có nguồn dữ liệu, token và giấy phép riêng; cần kiểm tài nguyên thiết bị và tránh hiển thị dữ liệu cá nhân ở không gian công cộng.

**Cách tham khảo/tích hợp:** Dùng bản phát hành phù hợp hệ điều hành, kiểm quyền ứng dụng và thao tác với dữ liệu mẫu; giữ khả năng khôi phục trước tác vụ ghi/xóa.

**Lựa chọn để đối chiếu:** [gethomepage/homepage](https://github.com/gethomepage/homepage) · [lissy93/dashy](https://github.com/lissy93/dashy). Đây là ứng viên so sánh theo tác vụ; mức phù hợp cần kiểm theo hồ sơ và phiên bản riêng.

**Bằng chứng:** `docs-read`, ngày 2026-11-23, commit [`f138f5b690ceab6450f55c852ac81d268363f563`](https://github.com/MagicMirrorOrg/MagicMirror/commit/f138f5b690ceab6450f55c852ac81d268363f563), ngày commit 2026-10-01. Đã clone và đọc chọn lọc phần giới thiệu, cách dùng, giới hạn, license, metadata manifest và CI hiện diện. Chưa kiểm đầy đủ implementation hoặc chạy upstream; các số đo của tác giả chưa được tái lập.

**Nguồn:** [README.md](https://github.com/MagicMirrorOrg/MagicMirror/blob/f138f5b690ceab6450f55c852ac81d268363f563/README.md) · [LICENSE.md](https://github.com/MagicMirrorOrg/MagicMirror/blob/f138f5b690ceab6450f55c852ac81d268363f563/LICENSE.md) · [package.json](https://github.com/MagicMirrorOrg/MagicMirror/blob/f138f5b690ceab6450f55c852ac81d268363f563/package.json) · [.github/workflows/spellcheck.yaml](https://github.com/MagicMirrorOrg/MagicMirror/blob/f138f5b690ceab6450f55c852ac81d268363f563/.github/workflows/spellcheck.yaml) · [metadata GitHub](https://api.github.com/repos/MagicMirrorOrg/MagicMirror).

<a id="anhkysuai-2026-11-23-caldis-mos"></a>

### Mos

**Repo:** [Caldis/Mos](https://github.com/Caldis/Mos) · **License:** CC-BY-NC-4.0 · **★ 21,981 (GitHub API, 2026-11-23)**

**Mục đích:** Tiện ích macOS làm mượt cuộn chuột, đổi hướng theo trục và tùy chỉnh nút theo ứng dụng.

**Giá trị:** Cấu hình riêng từng app giúp giải quyết sự khác biệt giữa chuột truyền thống và trackpad.

**Giới hạn:** Cần quyền Accessibility để đọc/ghi sự kiện; LICENSE là CC BY-NC 4.0 và README yêu cầu không đưa lên App Store, nên không gắn nhãn nguồn mở thương mại tự do.

**Cách tham khảo/tích hợp:** Dùng bản phát hành phù hợp hệ điều hành, kiểm quyền ứng dụng và thao tác với dữ liệu mẫu; giữ khả năng khôi phục trước tác vụ ghi/xóa.

**Lựa chọn để đối chiếu:** [AprilNEA/OpenLogi](https://github.com/AprilNEA/OpenLogi) · [linearmouse/linearmouse](https://github.com/linearmouse/linearmouse). Đây là ứng viên so sánh theo tác vụ; mức phù hợp cần kiểm theo hồ sơ và phiên bản riêng.

**Bằng chứng:** `docs-read`, ngày 2026-11-23, commit [`b95fee8985240261627f9e86d31398734885eeb0`](https://github.com/Caldis/Mos/commit/b95fee8985240261627f9e86d31398734885eeb0), ngày commit 2026-11-23. Đã clone và đọc chọn lọc phần giới thiệu, cách dùng, giới hạn, license, metadata manifest và CI hiện diện. Chưa kiểm đầy đủ implementation hoặc chạy upstream; các số đo của tác giả chưa được tái lập.

**Nguồn:** [README.md](https://github.com/Caldis/Mos/blob/b95fee8985240261627f9e86d31398734885eeb0/README.md) · [LICENSE](https://github.com/Caldis/Mos/blob/b95fee8985240261627f9e86d31398734885eeb0/LICENSE) · [.github/workflows/pages.yml](https://github.com/Caldis/Mos/blob/b95fee8985240261627f9e86d31398734885eeb0/.github/workflows/pages.yml) · [metadata GitHub](https://api.github.com/repos/Caldis/Mos).

<a id="anhkysuai-2026-11-23-komi-store-komi-store"></a>

### komi-store

**Repo:** [komi-store/komi-store](https://github.com/komi-store/komi-store) · **License:** Apache-2.0 · **★ 22,082 (GitHub API, 2026-11-23)**

**Mục đích:** Kho ứng dụng đa nền tảng tìm và cài bản phát hành từ GitHub, Codeberg và Forgejo/Gitea.

**Giá trị:** Giảm thao tác tìm release giữa nhiều forge; có giá trị tham khảo catalog ứng dụng đa nguồn.

**Giới hạn:** README ghi bản macOS chưa notarize; đánh giá này không khuyến nghị bỏ kiểm tra hệ điều hành. Tính tin cậy vẫn phụ thuộc nguồn release, chữ ký và quyền từng ứng dụng.

**Cách tham khảo/tích hợp:** Dùng bản phát hành phù hợp hệ điều hành, kiểm quyền ứng dụng và thao tác với dữ liệu mẫu; giữ khả năng khôi phục trước tác vụ ghi/xóa.

**Lựa chọn để đối chiếu:** [ImranR98/Obtainium](https://github.com/ImranR98/Obtainium) · [marticliment/UniGetUI](https://github.com/marticliment/UniGetUI). Đây là ứng viên so sánh theo tác vụ; mức phù hợp cần kiểm theo hồ sơ và phiên bản riêng.

**Bằng chứng:** `docs-read`, ngày 2026-11-23, commit [`19eb74474f5f45a63cca45fc1dc9b8f7314687f0`](https://github.com/komi-store/komi-store/commit/19eb74474f5f45a63cca45fc1dc9b8f7314687f0), ngày commit 2026-10-25. Đã clone và đọc chọn lọc phần giới thiệu, cách dùng, giới hạn, license, metadata manifest và CI hiện diện. Chưa kiểm đầy đủ implementation hoặc chạy upstream; các số đo của tác giả chưa được tái lập.

**Nguồn:** [README.md](https://github.com/komi-store/komi-store/blob/19eb74474f5f45a63cca45fc1dc9b8f7314687f0/README.md) · [LICENSE](https://github.com/komi-store/komi-store/blob/19eb74474f5f45a63cca45fc1dc9b8f7314687f0/LICENSE) · [.github/workflows/pr-checks.yml](https://github.com/komi-store/komi-store/blob/19eb74474f5f45a63cca45fc1dc9b8f7314687f0/.github/workflows/pr-checks.yml) · [metadata GitHub](https://api.github.com/repos/komi-store/komi-store).

<a id="anhkysuai-2026-11-23-imranr98-obtainium"></a>

### Obtainium

**Repo:** [ImranR98/Obtainium](https://github.com/ImranR98/Obtainium) · **License:** GPL-3.0 · **★ 21,828 (GitHub API, 2026-11-23)**

**Mục đích:** Ứng dụng Android theo dõi, cài và cập nhật phần mềm trực tiếp từ trang phát hành gốc.

**Giá trị:** Có cấu hình nguồn cộng đồng và deep link, phù hợp người muốn quản lý ứng dụng từ nhiều nguồn phát hành.

**Giới hạn:** README nêu một số nguồn phải scrape web và dễ hỏng khi trang đổi; cấu hình cộng đồng không thay thế kiểm chữ ký, nhà phát hành và quyền của APK.

**Cách tham khảo/tích hợp:** Dùng bản phát hành phù hợp hệ điều hành, kiểm quyền ứng dụng và thao tác với dữ liệu mẫu; giữ khả năng khôi phục trước tác vụ ghi/xóa.

**Lựa chọn để đối chiếu:** [komi-store/komi-store](https://github.com/komi-store/komi-store) · [f-droid/fdroidclient](https://github.com/f-droid/fdroidclient). Đây là ứng viên so sánh theo tác vụ; mức phù hợp cần kiểm theo hồ sơ và phiên bản riêng.

**Bằng chứng:** `docs-read`, ngày 2026-11-23, commit [`42575039fa6b501d442ed8485c40e1150928e85a`](https://github.com/ImranR98/Obtainium/commit/42575039fa6b501d442ed8485c40e1150928e85a), ngày commit 2026-11-23. Đã clone và đọc chọn lọc phần giới thiệu, cách dùng, giới hạn, license, metadata manifest và CI hiện diện. Chưa kiểm đầy đủ implementation hoặc chạy upstream; các số đo của tác giả chưa được tái lập.

**Nguồn:** [README.md](https://github.com/ImranR98/Obtainium/blob/42575039fa6b501d442ed8485c40e1150928e85a/README.md) · [LICENSE.txt](https://github.com/ImranR98/Obtainium/blob/42575039fa6b501d442ed8485c40e1150928e85a/LICENSE.txt) · [.github/workflows/release.yml](https://github.com/ImranR98/Obtainium/blob/42575039fa6b501d442ed8485c40e1150928e85a/.github/workflows/release.yml) · [metadata GitHub](https://api.github.com/repos/ImranR98/Obtainium).

<a id="anhkysuai-2026-11-23-videolan-vlc"></a>

### vlc

**Repo:** [videolan/vlc](https://github.com/videolan/vlc) · **License:** GPL-2.0-or-later (player); LGPL-2.1-or-later (libVLC) · **★ 20,558 (GitHub API, 2026-11-23)**

**Mục đích:** VLC media player và engine libVLC cho phát, chuyển đổi và xử lý luồng đa phương tiện.

**Giá trị:** Nhiều nền tảng và khả năng nhúng libVLC tạo giá trị tham khảo cho ứng dụng media.

**Giới hạn:** README tách GPL-2.0-or-later của player và LGPL của engine; COPYING.LIB là LGPL 2.1, một số nền tảng chịu GPLv3 do phụ thuộc. Cần kiểm đúng thành phần và build.

**Cách tham khảo/tích hợp:** Dùng bản phát hành phù hợp hệ điều hành, kiểm quyền ứng dụng và thao tác với dữ liệu mẫu; giữ khả năng khôi phục trước tác vụ ghi/xóa.

**Lựa chọn để đối chiếu:** [mpv-player/mpv](https://github.com/mpv-player/mpv) · [iina/iina](https://github.com/iina/iina). Đây là ứng viên so sánh theo tác vụ; mức phù hợp cần kiểm theo hồ sơ và phiên bản riêng.

**Bằng chứng:** `docs-read`, ngày 2026-11-23, commit [`391a3bf87302769a3e45143b8a2f9961be45db0e`](https://github.com/videolan/vlc/commit/391a3bf87302769a3e45143b8a2f9961be45db0e), ngày commit 2026-11-22. Đã clone và đọc chọn lọc phần giới thiệu, cách dùng, giới hạn, license, metadata manifest và CI hiện diện. Chưa kiểm đầy đủ implementation hoặc chạy upstream; các số đo của tác giả chưa được tái lập.

**Nguồn:** [README.md](https://github.com/videolan/vlc/blob/391a3bf87302769a3e45143b8a2f9961be45db0e/README.md) · [COPYING](https://github.com/videolan/vlc/blob/391a3bf87302769a3e45143b8a2f9961be45db0e/COPYING) · [COPYING.LIB](https://github.com/videolan/vlc/blob/391a3bf87302769a3e45143b8a2f9961be45db0e/COPYING.LIB) · [Cargo.toml](https://github.com/videolan/vlc/blob/391a3bf87302769a3e45143b8a2f9961be45db0e/Cargo.toml) · [metadata GitHub](https://api.github.com/repos/videolan/vlc).

<a id="anhkysuai-2026-11-23-files-community-files"></a>

### Files

**Repo:** [files-community/Files](https://github.com/files-community/Files) · **License:** MIT và MPL-2.0 theo thành phần; kiểm header từng tệp · **★ 46,764 (GitHub API, 2026-11-23)**

**Mục đích:** Trình quản lý tệp cho Windows với đa nhiệm, tag và tích hợp hệ thống.

**Giá trị:** Có thể tham khảo UX thao tác tệp và quy trình cộng đồng phát triển ứng dụng desktop.

**Giới hạn:** Repo có LICENSE-MIT và LICENSE-MPL; chưa có căn cứ coi cả hai là lựa chọn OR cho mọi tệp. Cần đọc header phần được nhúng và thử tác vụ sao chép/xóa trên dữ liệu mẫu.

**Cách tham khảo/tích hợp:** Dùng bản phát hành phù hợp hệ điều hành, kiểm quyền ứng dụng và thao tác với dữ liệu mẫu; giữ khả năng khôi phục trước tác vụ ghi/xóa.

**Lựa chọn để đối chiếu:** [spacedriveapp/spacedrive](https://github.com/spacedriveapp/spacedrive) · [sxyazi/yazi](https://github.com/sxyazi/yazi). Đây là ứng viên so sánh theo tác vụ; mức phù hợp cần kiểm theo hồ sơ và phiên bản riêng.

**Bằng chứng:** `docs-read`, ngày 2026-11-23, commit [`802ee6831f6882880c5d0613ddab67bd17d3965f`](https://github.com/files-community/Files/commit/802ee6831f6882880c5d0613ddab67bd17d3965f), ngày commit 2026-11-22. Đã clone và đọc chọn lọc phần giới thiệu, cách dùng, giới hạn, license, metadata manifest và CI hiện diện. Chưa kiểm đầy đủ implementation hoặc chạy upstream; các số đo của tác giả chưa được tái lập.

**Nguồn:** [.github/README.md](https://github.com/files-community/Files/blob/802ee6831f6882880c5d0613ddab67bd17d3965f/.github/README.md) · [LICENSE-MIT](https://github.com/files-community/Files/blob/802ee6831f6882880c5d0613ddab67bd17d3965f/LICENSE-MIT) · [LICENSE-MPL](https://github.com/files-community/Files/blob/802ee6831f6882880c5d0613ddab67bd17d3965f/LICENSE-MPL) · [.github/workflows/ci.yml](https://github.com/files-community/Files/blob/802ee6831f6882880c5d0613ddab67bd17d3965f/.github/workflows/ci.yml) · [.github/CONTRIBUTING.md](https://github.com/files-community/Files/blob/802ee6831f6882880c5d0613ddab67bd17d3965f/.github/CONTRIBUTING.md) · [metadata GitHub](https://api.github.com/repos/files-community/Files).

<a id="anhkysuai-2026-11-23-sharex-sharex"></a>

### ShareX

**Repo:** [ShareX/ShareX](https://github.com/ShareX/ShareX) · **License:** GPL-3.0 · **★ 41,321 (GitHub API, 2026-11-23)**

**Mục đích:** Ứng dụng Windows chụp/quay màn hình, chỉnh ảnh, tải tệp và nối workflow bằng phím tắt.

**Giá trị:** Tự động hóa chuỗi capture → sửa → lưu/upload hữu ích cho hỗ trợ, tài liệu và tái hiện lỗi.

**Giới hạn:** Tự upload có thể đưa ảnh hoặc clipboard lên nhà cung cấp ngoài; cần kiểm đích tải, token, vùng chụp và license dịch vụ. Chưa thử workflow thực tế trong lượt này.

**Cách tham khảo/tích hợp:** Dùng bản phát hành phù hợp hệ điều hành, kiểm quyền ứng dụng và thao tác với dữ liệu mẫu; giữ khả năng khôi phục trước tác vụ ghi/xóa.

**Lựa chọn để đối chiếu:** [NickeManarin/ScreenToGif](https://github.com/NickeManarin/ScreenToGif) · [Molunerfinn/PicGo](https://github.com/Molunerfinn/PicGo). Đây là ứng viên so sánh theo tác vụ; mức phù hợp cần kiểm theo hồ sơ và phiên bản riêng.

**Bằng chứng:** `docs-read`, ngày 2026-11-23, commit [`099bcb60a1c4af514f8b8b936a870492744e98fd`](https://github.com/ShareX/ShareX/commit/099bcb60a1c4af514f8b8b936a870492744e98fd), ngày commit 2026-11-22. Đã clone và đọc chọn lọc phần giới thiệu, cách dùng, giới hạn, license, metadata manifest và CI hiện diện. Chưa kiểm đầy đủ implementation hoặc chạy upstream; các số đo của tác giả chưa được tái lập.

**Nguồn:** [README.md](https://github.com/ShareX/ShareX/blob/099bcb60a1c4af514f8b8b936a870492744e98fd/README.md) · [LICENSE.txt](https://github.com/ShareX/ShareX/blob/099bcb60a1c4af514f8b8b936a870492744e98fd/LICENSE.txt) · [.github/workflows/build.yml](https://github.com/ShareX/ShareX/blob/099bcb60a1c4af514f8b8b936a870492744e98fd/.github/workflows/build.yml) · [metadata GitHub](https://api.github.com/repos/ShareX/ShareX).

<a id="anhkysuai-2026-11-23-koreader-koreader"></a>

### koreader

**Repo:** [koreader/koreader](https://github.com/koreader/koreader) · **License:** AGPL-3.0 · **★ 31,280 (GitHub API, 2026-11-23)**

**Mục đích:** Ứng dụng đọc tài liệu tối ưu thiết bị e-ink, hỗ trợ nhiều định dạng và nền tảng.

**Giá trị:** Có tùy chỉnh dàn trang và reflow PDF/DjVu, phù hợp nghiên cứu trải nghiệm đọc trên thiết bị tài nguyên hạn chế.

**Giới hạn:** Cài đặt phụ thuộc model/firmware thiết bị; cần kiểm font, chú thích và quyền sách. AGPL của ứng dụng tách khỏi quyền tài liệu và thư viện phụ thuộc.

**Cách tham khảo/tích hợp:** Dùng bản phát hành phù hợp hệ điều hành, kiểm quyền ứng dụng và thao tác với dữ liệu mẫu; giữ khả năng khôi phục trước tác vụ ghi/xóa.

**Lựa chọn để đối chiếu:** [readest/readest](https://github.com/readest/readest) · [koodo-reader/koodo-reader](https://github.com/koodo-reader/koodo-reader). Đây là ứng viên so sánh theo tác vụ; mức phù hợp cần kiểm theo hồ sơ và phiên bản riêng.

**Bằng chứng:** `docs-read`, ngày 2026-11-23, commit [`1294bb3d377c51fdd0b7ef250620aee2ca08927c`](https://github.com/koreader/koreader/commit/1294bb3d377c51fdd0b7ef250620aee2ca08927c), ngày commit 2026-11-21. Đã clone và đọc chọn lọc phần giới thiệu, cách dùng, giới hạn, license, metadata manifest và CI hiện diện. Chưa kiểm đầy đủ implementation hoặc chạy upstream; các số đo của tác giả chưa được tái lập.

**Nguồn:** [README.md](https://github.com/koreader/koreader/blob/1294bb3d377c51fdd0b7ef250620aee2ca08927c/README.md) · [COPYING](https://github.com/koreader/koreader/blob/1294bb3d377c51fdd0b7ef250620aee2ca08927c/COPYING) · [.github/workflows/build.yml](https://github.com/koreader/koreader/blob/1294bb3d377c51fdd0b7ef250620aee2ca08927c/.github/workflows/build.yml) · [metadata GitHub](https://api.github.com/repos/koreader/koreader).

<a id="anhkysuai-2026-11-23-koodo-reader-koodo-reader"></a>

### koodo-reader

**Repo:** [koodo-reader/koodo-reader](https://github.com/koodo-reader/koodo-reader) · **License:** AGPL-3.0 · **★ 28,951 (GitHub API, 2026-11-23)**

**Mục đích:** Trình đọc và quản lý ebook đa nền tảng với đồng bộ, sao lưu và plugin.

**Giá trị:** Danh sách định dạng rộng, hỗ trợ cả tài liệu và truyện tranh trong cùng thư viện.

**Giới hạn:** Cần kiểm độ bảo toàn layout/annotation khi chuyển đổi và điều khoản dịch vụ sync; hỗ trợ Mobipocket/Kindle được README giới hạn DRM-free, không suy đọc được mọi sách.

**Cách tham khảo/tích hợp:** Dùng bản phát hành phù hợp hệ điều hành, kiểm quyền ứng dụng và thao tác với dữ liệu mẫu; giữ khả năng khôi phục trước tác vụ ghi/xóa.

**Lựa chọn để đối chiếu:** [kovidgoyal/calibre](https://github.com/kovidgoyal/calibre) · [readest/readest](https://github.com/readest/readest). Đây là ứng viên so sánh theo tác vụ; mức phù hợp cần kiểm theo hồ sơ và phiên bản riêng.

**Bằng chứng:** `docs-read`, ngày 2026-11-23, commit [`bb4ec25af94e3e023d773714467d8d6f5cc7b065`](https://github.com/koodo-reader/koodo-reader/commit/bb4ec25af94e3e023d773714467d8d6f5cc7b065), ngày commit 2026-11-23. Đã clone và đọc chọn lọc phần giới thiệu, cách dùng, giới hạn, license, metadata manifest và CI hiện diện. Chưa kiểm đầy đủ implementation hoặc chạy upstream; các số đo của tác giả chưa được tái lập.

**Nguồn:** [README.md](https://github.com/koodo-reader/koodo-reader/blob/bb4ec25af94e3e023d773714467d8d6f5cc7b065/README.md) · [LICENSE](https://github.com/koodo-reader/koodo-reader/blob/bb4ec25af94e3e023d773714467d8d6f5cc7b065/LICENSE) · [package.json](https://github.com/koodo-reader/koodo-reader/blob/bb4ec25af94e3e023d773714467d8d6f5cc7b065/package.json) · [.github/workflows/upload.yml](https://github.com/koodo-reader/koodo-reader/blob/bb4ec25af94e3e023d773714467d8d6f5cc7b065/.github/workflows/upload.yml) · [metadata GitHub](https://api.github.com/repos/koodo-reader/koodo-reader).

<a id="anhkysuai-2026-11-23-readest-readest"></a>

### readest

**Repo:** [readest/readest](https://github.com/readest/readest) · **License:** AGPL-3.0 · **★ 26,598 (GitHub API, 2026-11-23)**

**Mục đích:** Trình đọc ebook đa nền tảng dựa trên Tauri/Next.js, phát triển từ ý tưởng Foliate.

**Giá trị:** Hướng tới trải nghiệm đọc sâu với nhiều định dạng và khả năng chạy cả web lẫn native.

**Giới hạn:** README tách tính năng dự kiến và hiện có; Windows cần WebView2, Linux có giới hạn compositor. Cần kiểm dữ liệu đồng bộ, font và license engine/tài liệu đi kèm.

**Cách tham khảo/tích hợp:** Dùng bản phát hành phù hợp hệ điều hành, kiểm quyền ứng dụng và thao tác với dữ liệu mẫu; giữ khả năng khôi phục trước tác vụ ghi/xóa.

**Lựa chọn để đối chiếu:** [koreader/koreader](https://github.com/koreader/koreader) · [koodo-reader/koodo-reader](https://github.com/koodo-reader/koodo-reader). Đây là ứng viên so sánh theo tác vụ; mức phù hợp cần kiểm theo hồ sơ và phiên bản riêng.

**Bằng chứng:** `docs-read`, ngày 2026-11-23, commit [`0856099ee905f91bbe7fcf6b84cba767851f7935`](https://github.com/readest/readest/commit/0856099ee905f91bbe7fcf6b84cba767851f7935), ngày commit 2026-11-23. Đã clone và đọc chọn lọc phần giới thiệu, cách dùng, giới hạn, license, metadata manifest và CI hiện diện. Chưa kiểm đầy đủ implementation hoặc chạy upstream; các số đo của tác giả chưa được tái lập.

**Nguồn:** [README.md](https://github.com/readest/readest/blob/0856099ee905f91bbe7fcf6b84cba767851f7935/README.md) · [LICENSE](https://github.com/readest/readest/blob/0856099ee905f91bbe7fcf6b84cba767851f7935/LICENSE) · [package.json](https://github.com/readest/readest/blob/0856099ee905f91bbe7fcf6b84cba767851f7935/package.json) · [Cargo.toml](https://github.com/readest/readest/blob/0856099ee905f91bbe7fcf6b84cba767851f7935/Cargo.toml) · [.github/workflows/nix-build.yml](https://github.com/readest/readest/blob/0856099ee905f91bbe7fcf6b84cba767851f7935/.github/workflows/nix-build.yml) · [metadata GitHub](https://api.github.com/repos/readest/readest).

<a id="chuan-hoa-2026-11-23"></a>

## Chuẩn hóa bằng chứng hồ sơ cũ — 23/11/2026

Các hồ sơ dưới đây có từ trước khi kho ghi mức kiểm. Ngày 2026-11-23 mỗi repo được clone nông tại commit ghi trong bảng, đọc LICENSE, README, manifest và CI (nếu có); không cài, build hay chạy mã upstream. Nhận định cũ ở phần trên giữ nguyên; chỗ nào khác với lần đọc này được ghi trong cột Nhận định. Số sao lấy qua GitHub search API cùng ngày.

<a id="ch-applite"></a>

### Applite

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/milanvarady/Applite |
| License | MIT |
| Phiên bản đã đọc | `cf9712ae57a23628f4946389192959eb7079c6be` (commit 2026-09-12) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE.txt, Applite.xcodeproj/project.pbxproj; chưa chạy upstream |
| Bảo trì | active (commit mới nhất 2026-09-12) |
| Nhận định | App macOS native làm "app store" cho Homebrew Cask (SwiftUI). README có mục "Development and AI" (chưa đọc chi tiết). Chỉ chạy trên macOS, phụ thuộc Homebrew. |
| Nguồn | [README](https://github.com/milanvarady/Applite/blob/cf9712ae57a23628f4946389192959eb7079c6be/README.md) · [LICENSE](https://github.com/milanvarady/Applite/blob/cf9712ae57a23628f4946389192959eb7079c6be/LICENSE.txt) · [manifest](https://github.com/milanvarady/Applite/blob/cf9712ae57a23628f4946389192959eb7079c6be/Applite.xcodeproj/project.pbxproj) |

<a id="ch-brewui"></a>

### BrewUI

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/Homebrew/BrewUI |
| License | AGPL-3.0 |
| Phiên bản đã đọc | `4390497f1a09deaf100bea9a93afb11a37b606c5` (commit 2026-11-20) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE, Package.swift, .github/workflows/build.yml; chưa chạy upstream |
| Bảo trì | active (commit mới nhất 2026-11-20) |
| Nhận định | GUI chính thức của Homebrew cho macOS (SwiftUI, Swift 6.2, yêu cầu macOS 26): đọc từ brew CLI và Homebrew JSON API, công khai thao tác brew. AGPL-3.0 hạn chế dùng lại mã trong sản phẩm đóng. |
| Nguồn | [README](https://github.com/Homebrew/BrewUI/blob/4390497f1a09deaf100bea9a93afb11a37b606c5/README.md) · [LICENSE](https://github.com/Homebrew/BrewUI/blob/4390497f1a09deaf100bea9a93afb11a37b606c5/LICENSE) · [manifest](https://github.com/Homebrew/BrewUI/blob/4390497f1a09deaf100bea9a93afb11a37b606c5/Package.swift) · [workflow](https://github.com/Homebrew/BrewUI/blob/4390497f1a09deaf100bea9a93afb11a37b606c5/.github/workflows/build.yml) |

<a id="ch-cleanmylinux"></a>

### CleanMyLinux

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/Better-Linux/CleanMyLinux |
| License | MIT |
| Phiên bản đã đọc | `02de64d1168e06820a4e280971b49175bdc31307` (commit 2026-05-25) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE, package.json, .github/workflows/ci.yml; chưa chạy upstream |
| Bảo trì | low-activity (commit mới nhất 2026-05-25) |
| Nhận định | App dọn dẹp và quản lý ứng dụng cho Linux desktop (Tauri + Vite), bản 1.0.0-beta.2; hỗ trợ Ubuntu 22.04+, Debian 12+, Fedora 40+; Arch chưa kiểm. Commit mới nhất 2026-05-25. |
| Nguồn | [README](https://github.com/Better-Linux/CleanMyLinux/blob/02de64d1168e06820a4e280971b49175bdc31307/README.md) · [LICENSE](https://github.com/Better-Linux/CleanMyLinux/blob/02de64d1168e06820a4e280971b49175bdc31307/LICENSE) · [manifest](https://github.com/Better-Linux/CleanMyLinux/blob/02de64d1168e06820a4e280971b49175bdc31307/package.json) · [workflow](https://github.com/Better-Linux/CleanMyLinux/blob/02de64d1168e06820a4e280971b49175bdc31307/.github/workflows/ci.yml) |

<a id="ch-cork"></a>

### Cork

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/buresdv/Cork |
| License | Provisional custom license (dựa trên Commons Clause, source-available, không OSI) |
| Phiên bản đã đọc | `aee5584a348b629da9fd52386b89ad5fdd4998a1` (commit 2026-11-22) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE.md, Project.swift, .github/workflows/tuist-test.yml; chưa chạy upstream |
| Bảo trì | active (commit mới nhất 2026-11-22) |
| Nhận định | GUI Homebrew viết SwiftUI (macOS 14+, Tuist). Mã xem được nhưng giấy phép tạm cấm bán lại, biên dịch ngoài mục đích cá nhân và dựng sản phẩm cạnh tranh; README nói không dùng AI viết mã. Không phải mã mở. |
| Nguồn | [README](https://github.com/buresdv/Cork/blob/aee5584a348b629da9fd52386b89ad5fdd4998a1/README.md) · [LICENSE](https://github.com/buresdv/Cork/blob/aee5584a348b629da9fd52386b89ad5fdd4998a1/LICENSE.md) · [manifest](https://github.com/buresdv/Cork/blob/aee5584a348b629da9fd52386b89ad5fdd4998a1/Project.swift) · [workflow](https://github.com/buresdv/Cork/blob/aee5584a348b629da9fd52386b89ad5fdd4998a1/.github/workflows/tuist-test.yml) |
