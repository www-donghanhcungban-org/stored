# 36. Tự host & homelab

Ứng dụng và nền tảng tự vận hành trên server riêng hoặc máy nhà: PaaS/bảng điều khiển, ứng dụng ảnh/file/mật khẩu, DNS chặn quảng cáo, giám sát uptime. Tự host chuyển trách nhiệm sao lưu, cập nhật bảo mật, chứng chỉ và phơi cổng ra Internet về phía người vận hành.

Mục được lập ngày 2026-11-23 khi chia lại catalog; hồ sơ bên dưới chuyển nguyên văn từ mục cũ, neo cũ vẫn giữ một đoạn dẫn sang đây. Bảng tổng hợp theo danh mục con: [catalog/](../catalog/README.md).

<a id="chuyen-muc-2026-11-23"></a>

## Hồ sơ chuyển về từ mục khác — 23/11/2026

38 hồ sơ được chuyển khi chia lại catalog theo `data/taxonomy.json`. Nội dung, ngày kiểm và mức bằng chứng giữ nguyên như ở mục gốc.

<a id="chuyen-libretranslate"></a>

### LibreTranslate

`LibreTranslate/LibreTranslate` · License: GNU Affero General Public License v3 · ★ 17.783 · docs-read · 2026-11-18

API dịch máy mã nguồn mở, tự host hoàn toàn, không phụ thuộc dịch vụ độc quyền như Google hay Azure. Động cơ dịch dựa trên thư viện mã nguồn mở Argos Translate; Có sẵn docker-compose (kể cả bản CUDA) và manifest k8s.yaml để tự triển khai; Có CI chạy test, phát hành gói PyPI và Docker image (theo badge workflow trong README), phiên bản hiện tại 1.9.6. Điều kiện: AGPL-3.0: cung cấp qua mạng bản đã sửa phải công khai mã nguồn; dùng tên/logo LibreTranslate cho bản sửa đổi hoặc trong tên miền cần xin phép bằng văn bản theo TRADEMARK.md. ★ 18/11/2026: 17.783 (GitHub search API), nhóm "API & Dịch vụ dữ liệu" trong kho-repo của Phan Đông Giang, mục 08 §6c.5

**Hồ sơ gốc:** [mục 08](../08-awesome-lists-learning/README.md#6c52-api--dịch-vụ-dữ-liệu) (bảng/đoạn chung, giữ nguyên tại chỗ).

<a id="chuyen-open-seo"></a>

### open-seo

`every-app/open-seo` · License: MIT · ★ 28.117 · docs-read · 2026-11-18

Công cụ SEO mã nguồn mở thay thế Semrush/Ahrefs (nghiên cứu từ khoá, theo dõi thứ hạng, backlink, audit site) kèm MCP server và skill cho AI agent. Có MCP server và Agent Skills cho Claude Code, Codex, ChatGPT; tự host bằng Docker (Compose) hoặc Cloudflare, có tài liệu riêng cho từng cách; trả theo mức dùng thay vì thuê bao. Điều kiện: Cần khoá API DataForSEO trả phí (hoặc tài khoản treg); bản hosted có thuê bao 10 USD/tháng và cộng 28% phí DataForSEO; tự host qua EveryApp cần gói Cloudflare 5 USD/tháng. ★ 18/11/2026: 28.117 (GitHub search API), nhóm "Editor, Terminal & Dòng lệnh" trong kho-repo của Phan Đông Giang, mục 08 §6c.5

**Hồ sơ gốc:** [mục 08](../08-awesome-lists-learning/README.md#6c58-editor-terminal--dòng-lệnh) (bảng/đoạn chung, giữ nguyên tại chỗ).

<a id="chuyen-uptime-kuma"></a>

### uptime-kuma

`louislam/uptime-kuma` · License: MIT · ★ 94.567 · docs-read · 2026-11-18

Công cụ giám sát uptime tự host, dễ dùng, theo dõi HTTP(s), TCP, ping, DNS, WebSocket, container Docker và có trang trạng thái. Thông báo qua Telegram, Discord, Slack, email và hơn 90 dịch vụ; chu kỳ kiểm tra 20 giây, nhiều trang trạng thái gắn tên miền riêng; hỗ trợ 2FA, proxy, thông tin chứng chỉ. Điều kiện: Không hỗ trợ hệ thống file NFS; không hỗ trợ FreeBSD/OpenBSD/NetBSD, Replit/Heroku; README cảnh báo uptimekuma.co không phải trang chính thức. ★ 18/11/2026: 94.567 (GitHub search API), nhóm "Giám sát, CSDL & Phân tích" trong kho-repo của Phan Đông Giang, mục 08 §6c.5

**Hồ sơ gốc:** [mục 08](../08-awesome-lists-learning/README.md#6c511-giám-sát-csdl--phân-tích) (bảng/đoạn chung, giữ nguyên tại chỗ).

<a id="chuyen-trendradar"></a>

### TrendRadar

`sansan0/TrendRadar` · License: GPL-3.0 · ★ 63.705 · docs-read · 2026-11-18

Trợ lý theo dõi tin nóng: gom bảng xếp hạng thịnh hành từ nhiều nền tảng (Trung Quốc) và RSS, lọc theo từ khoá, phân tích bằng AI và đẩy thông báo qua nhiều kênh. Mặc định theo dõi 11 nền tảng như Zhihu, Weibo và hỗ trợ RSS; đẩy qua WeCom, Feishu, DingTalk, Telegram, Email, ntfy, Bark, Slack, webhook; có MCP server và triển khai qua GitHub Actions, Docker hoặc chạy cục bộ. Điều kiện: Dữ liệu nền tảng lấy qua API của dự án newsnow (có thể tự host); phân tích AI cần khoá API mô hình (mặc định DeepSeek); tài liệu chủ yếu tiếng Trung; tác giả nói đây là chia sẻ mã nguồn mở, không phải sản phẩm thương mại. ★ 18/11/2026: 63.705 (GitHub search API), nhóm "Năng suất, Ghi chú & Việc làm" trong kho-repo của Phan Đông Giang, mục 08 §6c.5

**Hồ sơ gốc:** [mục 08](../08-awesome-lists-learning/README.md#6c515-năng-suất-ghi-chú--việc-làm) (bảng/đoạn chung, giữ nguyên tại chỗ).

<a id="chuyen-paperless-ngx"></a>

### paperless-ngx

`paperless-ngx/paperless-ngx` · License: GPL-3.0 · ★ 48.232 · docs-read · 2026-11-18

Hệ thống quản lý tài liệu tự host, biến giấy tờ quét thành kho lưu trữ trực tuyến tìm kiếm được. Kế nhiệm chính thức của Paperless và Paperless-ng; triển khai bằng docker compose với script cài đặt sẵn; có bản demo công khai và bản dịch điều phối qua Crowdin. Điều kiện: Dữ liệu lưu dạng rõ, không mã hoá: dự án khuyến cáo không chạy trên máy chủ không tin cậy, tự chịu rủi ro, nên chạy trên máy chủ tại nhà có sao lưu. ★ 18/11/2026: 48.232 (GitHub search API), nhóm "Năng suất, Ghi chú & Việc làm" trong kho-repo của Phan Đông Giang, mục 08 §6c.5

**Hồ sơ gốc:** [mục 08](../08-awesome-lists-learning/README.md#6c515-năng-suất-ghi-chú--việc-làm) (bảng/đoạn chung, giữ nguyên tại chỗ).

<a id="chuyen-reactive-resume"></a>

### reactive-resume

`reactive-resume/reactive-resume` · License: MIT · ★ 45.869 · docs-read · 2026-11-18

Trình tạo CV và thư xin việc miễn phí, mã nguồn mở, có kiểm tra CV và theo dõi hồ sơ ứng tuyển, dùng bản host sẵn hoặc tự host. 18 mẫu CV, xem trước PDF trực tiếp, xuất PDF, Word, Markdown, JSON; nhập từ JSON Resume, LinkedIn, PDF, Word; có REST API, MCP server và tự host qua Docker, Vercel, Cloudflare Workers. Điều kiện: Tính năng AI cần nhà cung cấp do người dùng kết nối (có thể phát sinh chi phí); nhập Word cần nhà cung cấp AI. ★ 18/11/2026: 45.869 (GitHub search API), nhóm "Năng suất, Ghi chú & Việc làm" trong kho-repo của Phan Đông Giang, mục 08 §6c.5

**Hồ sơ gốc:** [mục 08](../08-awesome-lists-learning/README.md#6c515-năng-suất-ghi-chú--việc-làm) (bảng/đoạn chung, giữ nguyên tại chỗ).

<a id="chuyen-open-notebook"></a>

### open-notebook

`lfnovo/open-notebook` · License: MIT · ★ 42.052 · docs-read · 2026-11-18

Phương án mã nguồn mở, tự host thay cho Google NotebookLM: tổ chức tài liệu đa phương tiện, tìm kiếm và trò chuyện với AI trên nội dung nghiên cứu, tạo podcast nhiều giọng. Hỗ trợ hơn 20 nhà cung cấp mô hình kể cả chạy cục bộ qua Ollama, LM Studio; tìm kiếm toàn văn và vector; có REST API và triển khai bằng Docker Compose với SurrealDB. Điều kiện: Cần Docker và khoá API của nhà cung cấp AI hoặc máy chủ mô hình cục bộ (Ollama); phải đặt OPEN_NOTEBOOK_ENCRYPTION_KEY trong .env. ★ 18/11/2026: 42.052 (GitHub search API), nhóm "Năng suất, Ghi chú & Việc làm" trong kho-repo của Phan Đông Giang, mục 08 §6c.5

**Hồ sơ gốc:** [mục 08](../08-awesome-lists-learning/README.md#6c515-năng-suất-ghi-chú--việc-làm) (bảng/đoạn chung, giữ nguyên tại chỗ).

<a id="chuyen-outline"></a>

### outline

`outline/outline` · License: Business Source License 1.1 · ★ 41.292 · docs-read · 2026-11-18

Cơ sở tri thức (wiki) cộng tác nhanh cho nhóm, viết bằng React và Node.js; có bản hosted tại getoutline.com hoặc tự host. Có image container chính thức outlinewiki/outline trên Docker Hub; test bằng Vitest, migration bằng Sequelize; có tài liệu kiến trúc docs/ARCHITECTURE.md. Điều kiện: BSL 1.1: không được cung cấp Outline như dịch vụ tài liệu thương mại cho bên thứ ba; dự án yêu cầu không gửi PR do AI tạo và phải thảo luận qua issue trước khi gửi PR. ★ 18/11/2026: 41.292 (GitHub search API), nhóm "Năng suất, Ghi chú & Việc làm" trong kho-repo của Phan Đông Giang, mục 08 §6c.5

**Hồ sơ gốc:** [mục 08](../08-awesome-lists-learning/README.md#6c515-năng-suất-ghi-chú--việc-làm) (bảng/đoạn chung, giữ nguyên tại chỗ).

<a id="chuyen-docmost"></a>

### docmost

`docmost/docmost` · License: AGPL-3.0 cho phần lõi · ★ 22.367 · docs-read · 2026-11-18

Phần mềm wiki và tài liệu cộng tác mã nguồn mở, tự host được. Cộng tác thời gian thực, lịch sử trang, quản lý quyền theo space và nhóm; vẽ sơ đồ bằng Draw.io, Excalidraw và Mermaid; giao diện hơn 10 ngôn ngữ. Điều kiện: Lõi AGPL-3.0; tính năng Enterprise cần giấy phép Enterprise riêng. ★ 18/11/2026: 22.367 (GitHub search API), nhóm "Năng suất, Ghi chú & Việc làm" trong kho-repo của Phan Đông Giang, mục 08 §6c.5

**Hồ sơ gốc:** [mục 08](../08-awesome-lists-learning/README.md#6c515-năng-suất-ghi-chú--việc-làm) (bảng/đoạn chung, giữ nguyên tại chỗ).

<a id="chuyen-docuseal"></a>

### docuseal

`docusealco/docuseal` · License: AGPL-3.0 kèm điều khoản bổ sung mục 7(b) · ★ 19.082 · docs-read · 2026-11-18

Nền tảng mã nguồn mở để tạo biểu mẫu PDF, điền và ký điện tử tài liệu trực tuyến, có API và webhook để tích hợp. Trình dựng trường biểu mẫu PDF kiểu WYSIWYG với 12 loại trường và nhiều người ký mỗi tài liệu; tự động ký điện tử PDF và xác minh chữ ký; chạy một lệnh Docker, mặc định SQLite, hỗ trợ PostgreSQL/MySQL qua DATABASE_URL. Điều kiện: AGPL-3.0 và bắt buộc giữ ghi công DocuSeal trong UI; một số tính năng (white-label, SSO/SAML, nhắc tự động, xác minh SMS, gửi hàng loạt, nhúng form) chỉ có ở bản Pro trả phí; gửi email cần cấu hình SMTP. ★ 18/11/2026: 19.082 (GitHub search API), nhóm "Năng suất, Ghi chú & Việc làm" trong kho-repo của Phan Đông Giang, mục 08 §6c.5

**Hồ sơ gốc:** [mục 08](../08-awesome-lists-learning/README.md#6c515-năng-suất-ghi-chú--việc-làm) (bảng/đoạn chung, giữ nguyên tại chỗ).

<a id="chuyen-docs"></a>

### docs

`suitenumerique/docs` · License: MIT · ★ 16.995 · docs-read · 2026-11-18

Trình soạn thảo cộng tác thời gian thực mã nguồn mở (La Suite Docs của chính phủ Pháp), thay thế Notion/Google Docs, hỗ trợ tự host. Cộng tác thời gian thực với con trỏ, bình luận và phân quyền chi tiết, có soạn thảo ngoại tuyến; nhập .docx/.md và xuất .docx/.odt/.pdf; tự host qua Kubernetes, Docker Compose, Nix hoặc YunoHost. Điều kiện: Gói BlockNote XL theo GPL cho một số tính năng nâng cao; tính năng AI tuỳ chọn cần URL và API key của nhà cung cấp; lưu trữ cần dịch vụ tương thích S3. ★ 18/11/2026: 16.995 (GitHub search API), nhóm "Năng suất, Ghi chú & Việc làm" trong kho-repo của Phan Đông Giang, mục 08 §6c.5

**Hồ sơ gốc:** [mục 08](../08-awesome-lists-learning/README.md#6c515-năng-suất-ghi-chú--việc-làm) (bảng/đoạn chung, giữ nguyên tại chỗ).

<a id="chuyen-omnivore"></a>

### omnivore

`omnivore-app/omnivore` · License: AGPL-3.0 · ★ 16.420 · docs-read · 2026-11-18

Ứng dụng đọc-để-sau (read-it-later) mã nguồn mở, lưu bài viết, PDF, newsletter để đọc, tô sáng và ghi chú; hiện chỉ chạy dạng tự host. Có tô sáng, ghi chú, tìm kiếm, nhãn và hỗ trợ ngoại tuyến; có ứng dụng iOS, Android, tiện ích trình duyệt Chrome, Safari, Firefox, Edge và client RSS; có plugin Logseq và Obsidian. Điều kiện: Dịch vụ cloud đã ngừng từ tháng 11/2024, chỉ còn tự host; AGPL-3.0 copyleft khi phục vụ qua mạng. ★ 18/11/2026: 16.420 (GitHub search API), nhóm "Năng suất, Ghi chú & Việc làm" trong kho-repo của Phan Đông Giang, mục 08 §6c.5

**Hồ sơ gốc:** [mục 08](../08-awesome-lists-learning/README.md#6c515-năng-suất-ghi-chú--việc-làm) (bảng/đoạn chung, giữ nguyên tại chỗ).

<a id="chuyen-documenso"></a>

### documenso

`documenso/documenso` · License: AGPL-3.0 · ★ 15.813 · docs-read · 2026-11-18

Nền tảng ký tài liệu điện tử mã nguồn mở, thay thế DocuSign, có thể tự host. Tự host được bằng Docker hoặc Docker Compose theo tài liệu chính thức; stack TypeScript, React Router v7, Hono, Prisma, tRPC; ký PDF bằng @libpdf/core. Điều kiện: AGPL-3.0 buộc công khai mã sửa đổi khi cung cấp qua mạng; tính năng trong packages/ee cần gói Enterprise trả phí để dùng production; không nhận PR từ bên ngoài. ★ 18/11/2026: 15.813 (GitHub search API), nhóm "Năng suất, Ghi chú & Việc làm" trong kho-repo của Phan Đông Giang, mục 08 §6c.5

**Hồ sơ gốc:** [mục 08](../08-awesome-lists-learning/README.md#6c515-năng-suất-ghi-chú--việc-làm) (bảng/đoạn chung, giữ nguyên tại chỗ).

<a id="chuyen-trek"></a>

### TREK

`liketrek/TREK` · License: AGPL-3.0 · ★ 15.737 · docs-read · 2026-11-18

Ứng dụng lập kế hoạch du lịch tự host: lên lịch trình cộng tác thời gian thực trên bản đồ, tour đi bộ/đạp xe, đặt chỗ, chia chi phí, nhật ký và trợ lý AI. Bản đồ Leaflet/MapLibre với OpenFreeMap, không cần token; dự báo thời tiết 16 ngày từ Open-Meteo, không cần khoá; triển khai bằng Docker, Docker Compose, Helm, TrueNAS SCALE. Điều kiện: Cần ENCRYPTION_KEY; Google Places/Amap cần khoá API; tên và logo TREK chịu chính sách thương hiệu riêng; dữ liệu ranh giới CC BY 4.0 phải ghi nguồn. ★ 18/11/2026: 15.737 (GitHub search API), nhóm "Năng suất, Ghi chú & Việc làm" trong kho-repo của Phan Đông Giang, mục 08 §6c.5

**Hồ sơ gốc:** [mục 08](../08-awesome-lists-learning/README.md#6c515-năng-suất-ghi-chú--việc-làm) (bảng/đoạn chung, giữ nguyên tại chỗ).

<a id="chuyen-awesome-selfhosted"></a>

### awesome-selfhosted

`awesome-selfhosted/awesome-selfhosted` · License: CC-BY-SA-3.0 · ★ 338.129 · docs-read · 2026-11-18

Danh sách các dịch vụ mạng và ứng dụng web phần mềm tự do có thể tự host trên máy chủ riêng, chia theo hạng mục. Khoảng 1277 mục liệt kê trong README chia theo nhiều hạng mục (Analytics, Backup, Automation…); có kiểm tra tự động link chết và dự án không còn bảo trì; phần mềm không tự do tách riêng ở non-free.md, có bản HTML tại awesome-selfhosted.net. Điều kiện: Nội dung theo CC-BY-SA-3.0 (ghi công, chia sẻ tương tự). ★ 18/11/2026: 338.129 (GitHub search API), nhóm "Tự host & Nhà thông minh" trong kho-repo của Phan Đông Giang, mục 08 §6c.5

**Hồ sơ gốc:** [mục 08](../08-awesome-lists-learning/README.md#6c526-tự-host--nhà-thông-minh) (bảng/đoạn chung, giữ nguyên tại chỗ).

<a id="chuyen-immich"></a>

### immich

`immich-app/immich` · License: GNU AGPL v3 · ★ 119.489 · docs-read · 2026-11-18

Giải pháp tự host quản lý ảnh và video hiệu năng cao, có ứng dụng web và di động. Sao lưu tự động và nền từ di động, chống trùng lặp, hỗ trợ ảnh raw, LivePhoto/MotionPhoto; tìm kiếm theo metadata, vật thể, khuôn mặt và CLIP, nhận diện và gom nhóm khuôn mặt; hỗ trợ nhiều người dùng, OAuth, chia sẻ công khai và đối tác, có các file docker compose kèm cấu hình tăng tốc phần cứng. Điều kiện: Giấy phép AGPLv3; README khuyến cáo luôn theo kế hoạch sao lưu 3-2-1 cho ảnh và video. ★ 18/11/2026: 119.489 (GitHub search API), nhóm "Tự host & Nhà thông minh" trong kho-repo của Phan Đông Giang, mục 08 §6c.5

**Hồ sơ gốc:** [mục 08](../08-awesome-lists-learning/README.md#6c526-tự-host--nhà-thông-minh) (bảng/đoạn chung, giữ nguyên tại chỗ).

<a id="chuyen-core"></a>

### core

`home-assistant/core` · License: Apache License 2.0 · ★ 92.443 · docs-read · 2026-11-18

Nền tảng tự động hoá nhà ở mã nguồn mở ưu tiên điều khiển cục bộ và quyền riêng tư, chạy được trên Raspberry Pi hoặc máy chủ cục bộ. Kiến trúc mô-đun với khoảng 1569 thư mục tích hợp trong homeassistant/components; thuộc Open Home Foundation và có cộng đồng toàn cầu; có demo trực tuyến và tài liệu kiến trúc, hướng dẫn tạo tích hợp riêng. Điều kiện: Đóng góp mã cần ký CLA (có file CLA.md). ★ 18/11/2026: 92.443 (GitHub search API), nhóm "Tự host & Nhà thông minh" trong kho-repo của Phan Đông Giang, mục 08 §6c.5

**Hồ sơ gốc:** [mục 08](../08-awesome-lists-learning/README.md#6c526-tự-host--nhà-thông-minh) (bảng/đoạn chung, giữ nguyên tại chỗ).

<a id="chuyen-gitea"></a>

### gitea

`go-gitea/gitea` · License: MIT · ★ 59.145 · docs-read · 2026-11-18

Dịch vụ phát triển phần mềm tự host trọn gói: Git hosting, review mã, issue, kanban, wiki, registry gói và CI/CD tương thích GitHub Actions. Viết bằng Go, chạy trên Linux, macOS, FreeBSD/OpenBSD, Windows với nhiều kiến trúc (amd64, ARM, RISC-V 64, PowerPC); có ảnh Docker chính thức và bản demo demo.gitea.com; có go-sdk, CLI gt và action runner chính thức. ★ 18/11/2026: 59.145 (GitHub search API), nhóm "Tự host & Nhà thông minh" trong kho-repo của Phan Đông Giang, mục 08 §6c.5

**Hồ sơ gốc:** [mục 08](../08-awesome-lists-learning/README.md#6c526-tự-host--nhà-thông-minh) (bảng/đoạn chung, giữ nguyên tại chỗ).

<a id="chuyen-1panel"></a>

### 1Panel

`1Panel-dev/1Panel` · License: GNU GPL v3 · ★ 37.464 · docs-read · 2026-11-18

Bảng điều khiển quản trị máy chủ Linux qua web kèm nền tảng quản lý AI: giám sát, tệp, cơ sở dữ liệu, container, website, sao lưu. Kho ứng dụng tích hợp cài một chạm (README nêu 165+ ứng dụng); cấu hình tên miền và SSL một chạm cho website như WordPress, Halo; sao lưu/khôi phục một chạm tích hợp nhiều kho lưu trữ đám mây. Điều kiện: Chỉ chạy trên Linux; một số tính năng (đa node, chống sửa website, AI Gateway…) chỉ có ở bản Pro/Ent trả phí; cài đặt bằng script tải từ mạng chạy quyền root. ★ 18/11/2026: 37.464 (GitHub search API), nhóm "Tự host & Nhà thông minh" trong kho-repo của Phan Đông Giang, mục 08 §6c.5

**Hồ sơ gốc:** [mục 08](../08-awesome-lists-learning/README.md#6c526-tự-host--nhà-thông-minh) (bảng/đoạn chung, giữ nguyên tại chỗ).

<a id="chuyen-dashy"></a>

### dashy

`lissy93/dashy` · License: MIT · ★ 27.015 · docs-read · 2026-11-18

Trang chủ/dashboard tự host cho homelab, tập hợp liên kết ứng dụng kèm widget và giám sát trạng thái. Cấu hình bằng một tệp YAML hoặc qua giao diện; giám sát trạng thái thời gian thực, widget, nhiều trang, xác thực đa người dùng có SSO; hơn 30 ngôn ngữ dịch bởi người. ★ 18/11/2026: 27.015 (GitHub search API), nhóm "Tự host & Nhà thông minh" trong kho-repo của Phan Đông Giang, mục 08 §6c.5

**Hồ sơ gốc:** [mục 08](../08-awesome-lists-learning/README.md#6c526-tự-host--nhà-thông-minh) (bảng/đoạn chung, giữ nguyên tại chỗ).

<a id="chuyen-seafile"></a>

### seafile

`haiwen/seafile` · License: GPL v2 kèm ngoại lệ cho phép liên kết với OpenSSL · ★ 15.468 · docs-read · 2026-11-18

Repo daemon client đồng bộ của Seafile, hệ thống lưu trữ đám mây mã nguồn mở có mã hoá thư viện và cộng tác nhóm. Đồng bộ chọn lọc, chỉ truyền phần thay đổi và tiếp tục được khi gián đoạn; mã hoá thư viện bằng mật khẩu người dùng, mã hoá phía client khi đồng bộ desktop; xử lý xung đột dựa trên lịch sử thay vì dấu thời gian. Điều kiện: Repo này chỉ là daemon client; server, web UI và app di động nằm ở repo riêng với giấy phép khác; khách hàng Pro liên hệ qua email. ★ 18/11/2026: 15.468 (GitHub search API), nhóm "Tự host & Nhà thông minh" trong kho-repo của Phan Đông Giang, mục 08 §6c.5

**Hồ sơ gốc:** [mục 08](../08-awesome-lists-learning/README.md#6c526-tự-host--nhà-thông-minh) (bảng/đoạn chung, giữ nguyên tại chỗ).

<a id="anhkysuai-dani-garcia-vaultwarden"></a>

### Vaultwarden

**Repo:** [dani-garcia/vaultwarden](https://github.com/dani-garcia/vaultwarden) · **License:** AGPL-3.0-only · **Kiểm:** 2026-11-23, `docs-read`, [`6f7a7f70347e`](https://github.com/dani-garcia/vaultwarden/tree/6f7a7f70347e0cdde9d3506342ff04b22a9c78ce) (commit 2026-11-23). **Sao:** 71,206 tại 2026-11-23 theo [GitHub API](https://api.github.com/repos/dani-garcia/vaultwarden).

| Mục | Đánh giá |
|---|---|
| Mục đích | Máy chủ Rust tương thích API và client Bitwarden để tự lưu kho mật khẩu. |
| Giá trị và cơ chế theo tài liệu | README mô tả vault cá nhân, tổ chức, chia sẻ và nhiều cách xác thực; Cargo tách các backend SQLite, MySQL, PostgreSQL bằng feature. |
| Giới hạn | Đây là triển khai độc lập với Bitwarden. Web vault cần HTTPS; dữ liệu mật khẩu và bản sao lưu đòi hỏi kiểm soát vận hành. Chưa kiểm toán mật mã hay tương thích mọi client. |
| Điều kiện tích hợp | Ưu tiên container chính thức của dự án, volume bền và reverse proxy HTTPS; kiểm nghĩa vụ AGPL trước khi sửa và cung cấp dịch vụ. |
| Lựa chọn đối chiếu | Bitwarden; KeePassXC; Passbolt. |

**Phạm vi bằng chứng:** đã clone, đọc trích đoạn tài liệu, giấy phép và các file cấu hình được dẫn dưới đây; chưa chạy mã, build, benchmark hoặc test upstream. `docs-read` không phải kiểm chứng implementation.

**Nguồn tại cùng SHA:** [README.md](https://github.com/dani-garcia/vaultwarden/blob/6f7a7f70347e0cdde9d3506342ff04b22a9c78ce/README.md) · [LICENSE.txt](https://github.com/dani-garcia/vaultwarden/blob/6f7a7f70347e0cdde9d3506342ff04b22a9c78ce/LICENSE.txt) · [Cargo.toml](https://github.com/dani-garcia/vaultwarden/blob/6f7a7f70347e0cdde9d3506342ff04b22a9c78ce/Cargo.toml) · [.github/workflows/build.yml](https://github.com/dani-garcia/vaultwarden/blob/6f7a7f70347e0cdde9d3506342ff04b22a9c78ce/.github/workflows/build.yml).

<a id="anhkysuai-coollabsio-coolify"></a>

### Coolify

**Repo:** [coollabsio/coolify](https://github.com/coollabsio/coolify) · **License:** Apache-2.0 · **Kiểm:** 2026-11-23, `docs-read`, [`619e9a78d0d1`](https://github.com/coollabsio/coolify/tree/619e9a78d0d1d66e085e151c0e41cd5d9a083576) (commit 2026-11-23). **Sao:** 66,375 tại 2026-11-23 theo [GitHub API](https://api.github.com/repos/coollabsio/coolify).

| Mục | Đánh giá |
|---|---|
| Mục đích | Nền tảng triển khai ứng dụng, cơ sở dữ liệu và dịch vụ trên máy chủ tự quản lý qua SSH. |
| Giá trị và cơ chế theo tài liệu | Tài liệu gom Git, Dockerfile/Compose, proxy HTTPS, preview và rollback trong một bảng điều khiển; cấu trúc Laravel/Composer giúp đọc được tầng điều phối. |
| Giới hạn | Quyền SSH và bí mật triển khai có phạm vi ảnh hưởng lớn. Khả năng rollback, cách cô lập mạng và phục hồi dữ liệu mới được đọc từ tài liệu, chưa thử trên hệ thống thật. |
| Điều kiện tích hợp | Đọc script cài trước khi dùng; triển khai thử trên máy chủ riêng, giới hạn quyền và kiểm quy trình backup/restore của từng dịch vụ. |
| Lựa chọn đối chiếu | [Dokploy](../32-platform-delivery-engineering/README.md#anhkysuai-dokploy-dokploy); [Dokku](../32-platform-delivery-engineering/README.md#anhkysuai-dokku-dokku); CapRover. |

**Phạm vi bằng chứng:** đã clone, đọc trích đoạn tài liệu, giấy phép và các file cấu hình được dẫn dưới đây; chưa chạy mã, build, benchmark hoặc test upstream. `docs-read` không phải kiểm chứng implementation.

**Nguồn tại cùng SHA:** [README.md](https://github.com/coollabsio/coolify/blob/619e9a78d0d1d66e085e151c0e41cd5d9a083576/README.md) · [LICENSE](https://github.com/coollabsio/coolify/blob/619e9a78d0d1d66e085e151c0e41cd5d9a083576/LICENSE) · [package.json](https://github.com/coollabsio/coolify/blob/619e9a78d0d1d66e085e151c0e41cd5d9a083576/package.json) · [composer.json](https://github.com/coollabsio/coolify/blob/619e9a78d0d1d66e085e151c0e41cd5d9a083576/composer.json) · [.github/workflows/build.yaml](https://github.com/coollabsio/coolify/blob/619e9a78d0d1d66e085e151c0e41cd5d9a083576/.github/workflows/build.yaml).

<a id="anhkysuai-pi-hole-pi-hole"></a>

### Pi-hole Core

**Repo:** [pi-hole/pi-hole](https://github.com/pi-hole/pi-hole) · **License:** EUPL-1.2 · **Kiểm:** 2026-11-23, `docs-read`, [`f7c0220e63e7`](https://github.com/pi-hole/pi-hole/tree/f7c0220e63e753c664a1ec08d42d6b647b86005d) (commit 2026-11-11). **Sao:** 62,184 tại 2026-11-23 theo [GitHub API](https://api.github.com/repos/pi-hole/pi-hole).

| Mục | Đánh giá |
|---|---|
| Mục đích | DNS sinkhole chặn tên miền không mong muốn cho cả mạng, có thể kiêm DHCP. |
| Giá trị và cơ chế theo tài liệu | Có CLI shell và BATS/ShellCheck trong CI; việc cấu hình DNS tại router cho phép áp chính sách cho nhiều thiết bị. |
| Giới hạn | Chặn theo DNS không đồng nghĩa chặn mọi nội dung quảng cáo; độ phủ phụ thuộc đường DNS thiết bị dùng. LICENSE ghi ngoại lệ lịch sử trước phiên bản 3.0. |
| Điều kiện tích hợp | Đọc installer trước khi chạy; thử cấu hình DNS và phương án khôi phục, tránh tạo hai máy chủ DHCP cùng mạng. |
| Lựa chọn đối chiếu | [AdGuard Home](../32-platform-delivery-engineering/README.md#anhkysuai-adguardteam-adguardhome); Technitium DNS; NextDNS. |

**Phạm vi bằng chứng:** đã clone, đọc trích đoạn tài liệu, giấy phép và các file cấu hình được dẫn dưới đây; chưa chạy mã, build, benchmark hoặc test upstream. `docs-read` không phải kiểm chứng implementation.

**Nguồn tại cùng SHA:** [README.md](https://github.com/pi-hole/pi-hole/blob/f7c0220e63e753c664a1ec08d42d6b647b86005d/README.md) · [LICENSE](https://github.com/pi-hole/pi-hole/blob/f7c0220e63e753c664a1ec08d42d6b647b86005d/LICENSE) · [.github/workflows/test.yml](https://github.com/pi-hole/pi-hole/blob/f7c0220e63e753c664a1ec08d42d6b647b86005d/.github/workflows/test.yml).

<a id="anhkysuai-photoprism-photoprism"></a>

### PhotoPrism

**Repo:** [photoprism/photoprism](https://github.com/photoprism/photoprism) · **License:** AGPL-3.0; điều khoản bổ sung về nhãn hiệu và tài sản thương hiệu · **Kiểm:** 2026-11-23, `docs-read`, [`3d2c27ec7bf2`](https://github.com/photoprism/photoprism/tree/3d2c27ec7bf2fd150aaf9669a4a94773a4c96934) (commit 2026-11-23). **Sao:** 40,471 tại 2026-11-23 theo [GitHub API](https://api.github.com/repos/photoprism/photoprism).

| Mục | Đánh giá |
|---|---|
| Mục đích | Ứng dụng tự host để quản lý, duyệt, tìm và gắn nhãn ảnh/video. |
| Giá trị và cơ chế theo tài liệu | README mô tả thư viện media và giao diện web; manifest Go/frontend và workflow CodeQL cung cấp điểm kiểm nền tảng. |
| Giới hạn | LICENSE có điều khoản bổ sung về nhãn hiệu, không chỉ nhãn AGPL của bộ dò. Nhận diện và quyền riêng tư chưa được đo/kiểm; cần dự trù dung lượng gốc, thumbnail và cơ sở dữ liệu. |
| Điều kiện tích hợp | Nhập bộ ảnh thử, kiểm metadata, quyền truy cập và restore; tách sao lưu ảnh gốc khỏi index, đọc điều khoản thương hiệu trước khi phân phối bản đổi tên. |
| Lựa chọn đối chiếu | [Immich](../08-awesome-lists-learning/README.md#6c526-tự-host--nhà-thông-minh); LibrePhotos; Nextcloud Photos. |

**Phạm vi bằng chứng:** đã clone, đọc trích đoạn tài liệu, giấy phép và các file cấu hình được dẫn dưới đây; chưa chạy mã, build, benchmark hoặc test upstream. `docs-read` không phải kiểm chứng implementation.

**Nguồn tại cùng SHA:** [README.md](https://github.com/photoprism/photoprism/blob/3d2c27ec7bf2fd150aaf9669a4a94773a4c96934/README.md) · [LICENSE](https://github.com/photoprism/photoprism/blob/3d2c27ec7bf2fd150aaf9669a4a94773a4c96934/LICENSE) · [package.json](https://github.com/photoprism/photoprism/blob/3d2c27ec7bf2fd150aaf9669a4a94773a4c96934/package.json) · [go.mod](https://github.com/photoprism/photoprism/blob/3d2c27ec7bf2fd150aaf9669a4a94773a4c96934/go.mod) · [.github/workflows/codeql-analysis.yml](https://github.com/photoprism/photoprism/blob/3d2c27ec7bf2fd150aaf9669a4a94773a4c96934/.github/workflows/codeql-analysis.yml).

<a id="anhkysuai-portainer-portainer"></a>

### Portainer Community Edition

**Repo:** [portainer/portainer](https://github.com/portainer/portainer) · **License:** Zlib · **Kiểm:** 2026-11-23, `docs-read`, [`08a5576af343`](https://github.com/portainer/portainer/tree/08a5576af343fe330ae57f9a9d16b5085df37097) (commit 2026-11-20). **Sao:** 38,893 tại 2026-11-23 theo [GitHub API](https://api.github.com/repos/portainer/portainer).

| Mục | Đánh giá |
|---|---|
| Mục đích | Giao diện quản lý container cho Docker, Swarm, Podman, Kubernetes và ACI. |
| Giá trị và cơ chế theo tài liệu | README phân biệt CE với Business Edition; manifest Go/frontend và script Vitest/typecheck cho thấy cách phát triển giao diện quản trị. |
| Giới hạn | README tại SHA này định vị CE cho homelab/học tập, không hỗ trợ production hay cam kết SLA. Giấy phép Zlib cho phép dùng thương mại nhưng không tạo cam kết hỗ trợ đó. |
| Điều kiện tích hợp | Dùng CE trong môi trường thử, giới hạn quyền truy cập Docker/Kubernetes; nếu vận hành doanh nghiệp, đối chiếu yêu cầu RBAC/audit/SSO và edition phù hợp. |
| Lựa chọn đối chiếu | [Rancher](../32-platform-delivery-engineering/README.md#anhkysuai-rancher-rancher); [Dockge](../32-platform-delivery-engineering/README.md#anhkysuai-louislam-dockge); Headlamp. |

**Phạm vi bằng chứng:** đã clone, đọc trích đoạn tài liệu, giấy phép và các file cấu hình được dẫn dưới đây; chưa chạy mã, build, benchmark hoặc test upstream. `docs-read` không phải kiểm chứng implementation.

**Nguồn tại cùng SHA:** [README.md](https://github.com/portainer/portainer/blob/08a5576af343fe330ae57f9a9d16b5085df37097/README.md) · [LICENSE](https://github.com/portainer/portainer/blob/08a5576af343fe330ae57f9a9d16b5085df37097/LICENSE) · [package.json](https://github.com/portainer/portainer/blob/08a5576af343fe330ae57f9a9d16b5085df37097/package.json) · [go.mod](https://github.com/portainer/portainer/blob/08a5576af343fe330ae57f9a9d16b5085df37097/go.mod).

<a id="anhkysuai-adguardteam-adguardhome"></a>

### AdGuard Home

**Repo:** [AdguardTeam/AdGuardHome](https://github.com/AdguardTeam/AdGuardHome) · **License:** GPL-3.0 · **Kiểm:** 2026-11-23, `docs-read`, [`69ee3d389910`](https://github.com/AdguardTeam/AdGuardHome/tree/69ee3d389910d5d30701cbe867280cf1809853ac) (commit 2026-11-20). **Sao:** 38,749 tại 2026-11-23 theo [GitHub API](https://api.github.com/repos/AdguardTeam/AdGuardHome).

| Mục | Đánh giá |
|---|---|
| Mục đích | Máy chủ DNS tự host chặn tên miền quảng cáo và theo dõi trên mạng. |
| Giá trị và cơ chế theo tài liệu | README giải thích cơ chế chuyển hướng tên miền, API và khác biệt với DNS công cộng; go.mod cho thấy các thư viện DNS proxy và bộ lọc. |
| Giới hạn | DNS filtering không bảo đảm chặn nội dung cùng tên miền hoặc thiết bị dùng DNS khác. Chưa kiểm danh sách lọc, độ trễ hay bảo vệ log truy vấn. |
| Điều kiện tích hợp | Thử với một nhóm thiết bị, chọn upstream tin cậy và chính sách log; chuẩn bị DNS dự phòng, tránh làm mất phân giải tên của cả mạng. |
| Lựa chọn đối chiếu | Pi-hole; Technitium DNS; Blocky. |

**Phạm vi bằng chứng:** đã clone, đọc trích đoạn tài liệu, giấy phép và các file cấu hình được dẫn dưới đây; chưa chạy mã, build, benchmark hoặc test upstream. `docs-read` không phải kiểm chứng implementation.

**Nguồn tại cùng SHA:** [README.md](https://github.com/AdguardTeam/AdGuardHome/blob/69ee3d389910d5d30701cbe867280cf1809853ac/README.md) · [LICENSE.txt](https://github.com/AdguardTeam/AdGuardHome/blob/69ee3d389910d5d30701cbe867280cf1809853ac/LICENSE.txt) · [go.mod](https://github.com/AdguardTeam/AdGuardHome/blob/69ee3d389910d5d30701cbe867280cf1809853ac/go.mod) · [.github/workflows/build.yaml](https://github.com/AdguardTeam/AdGuardHome/blob/69ee3d389910d5d30701cbe867280cf1809853ac/.github/workflows/build.yaml).

<a id="anhkysuai-dokploy-dokploy"></a>

### Dokploy

**Repo:** [Dokploy/dokploy](https://github.com/Dokploy/dokploy) · **License:** Apache-2.0 ngoài proprietary; proprietary theo DSAL-1.0 · **Kiểm:** 2026-11-23, `docs-read`, [`3b13bcde8dca`](https://github.com/Dokploy/dokploy/tree/3b13bcde8dca8b4ec0e4d48445b2aa1b0c183449) (commit 2026-11-20). **Sao:** 38,652 tại 2026-11-23 theo [GitHub API](https://api.github.com/repos/Dokploy/dokploy).

| Mục | Đánh giá |
|---|---|
| Mục đích | PaaS tự host để triển khai ứng dụng, cơ sở dữ liệu và Docker Compose. |
| Giá trị và cơ chế theo tài liệu | README kết hợp Traefik, nhiều máy chủ, backup và CLI/API; workflow upgrade integration tạo cặp phiên bản để kiểm đường nâng cấp. |
| Giới hạn | LICENSE tách proprietary sang DSAL đòi thỏa thuận thương mại cho production. Có workflow nâng cấp chưa chứng minh mọi stack nâng cấp an toàn; quyền quản trị máy chủ cần giới hạn. |
| Điều kiện tích hợp | Thử ứng dụng và database có backup phục hồi được; chốt phần Apache/DSAL sử dụng, quyền SSH, bí mật và đường rollback trước khi triển khai rộng. |
| Lựa chọn đối chiếu | [Coolify](../32-platform-delivery-engineering/README.md#anhkysuai-coollabsio-coolify); [Dokku](../32-platform-delivery-engineering/README.md#anhkysuai-dokku-dokku); CapRover. |

**Phạm vi bằng chứng:** đã clone, đọc trích đoạn tài liệu, giấy phép và các file cấu hình được dẫn dưới đây; chưa chạy mã, build, benchmark hoặc test upstream. `docs-read` không phải kiểm chứng implementation.

**Nguồn tại cùng SHA:** [README.md](https://github.com/Dokploy/dokploy/blob/3b13bcde8dca8b4ec0e4d48445b2aa1b0c183449/README.md) · [LICENSE.MD](https://github.com/Dokploy/dokploy/blob/3b13bcde8dca8b4ec0e4d48445b2aa1b0c183449/LICENSE.MD) · [LICENSE_PROPRIETARY.md](https://github.com/Dokploy/dokploy/blob/3b13bcde8dca8b4ec0e4d48445b2aa1b0c183449/LICENSE_PROPRIETARY.md) · [package.json](https://github.com/Dokploy/dokploy/blob/3b13bcde8dca8b4ec0e4d48445b2aa1b0c183449/package.json) · [.github/workflows/upgrade-integration-test.yml](https://github.com/Dokploy/dokploy/blob/3b13bcde8dca8b4ec0e4d48445b2aa1b0c183449/.github/workflows/upgrade-integration-test.yml).

<a id="anhkysuai-nextcloud-server"></a>

### Nextcloud Server

**Repo:** [nextcloud/server](https://github.com/nextcloud/server) · **License:** AGPL-3.0-or-later; thành phần bên thứ ba theo SPDX riêng · **Kiểm:** 2026-11-23, `docs-read`, [`0ff6535942dd`](https://github.com/nextcloud/server/tree/0ff6535942ddf0a2ab38c215c3d0ff78aa6f43f7) (commit 2026-11-23). **Sao:** 37,615 tại 2026-11-23 theo [GitHub API](https://api.github.com/repos/nextcloud/server).

| Mục | Đánh giá |
|---|---|
| Mục đích | Máy chủ lưu, đồng bộ và chia sẻ tệp với hệ sinh thái ứng dụng cộng tác. |
| Giá trị và cơ chế theo tài liệu | README nối files, contacts, calendar và các app riêng; Composer/Node cùng CI frontend giúp xác định ranh giới server và phần mở rộng. |
| Giới hạn | Các ứng dụng trong App Store không nằm hết trong phạm vi review. Tuyên bố mã hóa/an toàn chưa được kiểm; tính bảo mật phụ thuộc cách cấu hình và vận hành server. |
| Điều kiện tích hợp | Dùng bản phát hành phù hợp PHP/database, thử chia sẻ và ACL bằng tài khoản khác nhau; kiểm backup cả dữ liệu lẫn database và quy trình nâng cấp app. |
| Lựa chọn đối chiếu | [Seafile](../08-awesome-lists-learning/README.md#6c526-tự-host--nhà-thông-minh); ownCloud; [Syncthing](../08-awesome-lists-learning/README.md#6c526-tự-host--nhà-thông-minh). |

**Phạm vi bằng chứng:** đã clone, đọc trích đoạn tài liệu, giấy phép và các file cấu hình được dẫn dưới đây; chưa chạy mã, build, benchmark hoặc test upstream. `docs-read` không phải kiểm chứng implementation.

**Nguồn tại cùng SHA:** [README.md](https://github.com/nextcloud/server/blob/0ff6535942ddf0a2ab38c215c3d0ff78aa6f43f7/README.md) · [COPYING](https://github.com/nextcloud/server/blob/0ff6535942ddf0a2ab38c215c3d0ff78aa6f43f7/COPYING) · [COPYING-README](https://github.com/nextcloud/server/blob/0ff6535942ddf0a2ab38c215c3d0ff78aa6f43f7/COPYING-README) · [package.json](https://github.com/nextcloud/server/blob/0ff6535942ddf0a2ab38c215c3d0ff78aa6f43f7/package.json) · [composer.json](https://github.com/nextcloud/server/blob/0ff6535942ddf0a2ab38c215c3d0ff78aa6f43f7/composer.json) · [.github/workflows/node-test.yml](https://github.com/nextcloud/server/blob/0ff6535942ddf0a2ab38c215c3d0ff78aa6f43f7/.github/workflows/node-test.yml).

<a id="anhkysuai-dokku-dokku"></a>

### Dokku

**Repo:** [dokku/dokku](https://github.com/dokku/dokku) · **License:** MIT · **Kiểm:** 2026-11-23, `docs-read`, [`5112d90e44e1`](https://github.com/dokku/dokku/tree/5112d90e44e17ff90b89452cd4c2fc972881974c) (commit 2026-11-22). **Sao:** 32,233 tại 2026-11-23 theo [GitHub API](https://api.github.com/repos/dokku/dokku).

| Mục | Đánh giá |
|---|---|
| Mục đích | PaaS dùng Docker để quản lý vòng đời ứng dụng trên máy chủ tự quản. |
| Giá trị và cơ chế theo tài liệu | README định vị như Heroku nhỏ gọn; cấu trúc plugin, tài liệu và workflow build package cung cấp nền cho triển khai đơn giản bằng CLI. |
| Giới hạn | Tính nhỏ gọn không bảo đảm HA hay phục hồi dữ liệu. Plugin và backend build có phạm vi riêng; chưa cài máy chủ hoặc kiểm deployment/rollback. |
| Điều kiện tích hợp | Thử một ứng dụng stateless, cấu hình domain/HTTPS và biến môi trường; kiểm quyền SSH, volume/database backup và đường nâng cấp plugin. |
| Lựa chọn đối chiếu | [Coolify](../32-platform-delivery-engineering/README.md#anhkysuai-coollabsio-coolify); [Dokploy](../32-platform-delivery-engineering/README.md#anhkysuai-dokploy-dokploy); CapRover. |

**Phạm vi bằng chứng:** đã clone, đọc trích đoạn tài liệu, giấy phép và các file cấu hình được dẫn dưới đây; chưa chạy mã, build, benchmark hoặc test upstream. `docs-read` không phải kiểm chứng implementation.

**Nguồn tại cùng SHA:** [README.md](https://github.com/dokku/dokku/blob/5112d90e44e17ff90b89452cd4c2fc972881974c/README.md) · [LICENSE](https://github.com/dokku/dokku/blob/5112d90e44e17ff90b89452cd4c2fc972881974c/LICENSE) · [.github/workflows/ci.yml](https://github.com/dokku/dokku/blob/5112d90e44e17ff90b89452cd4c2fc972881974c/.github/workflows/ci.yml).

<a id="anhkysuai-community-scripts-proxmoxve"></a>

### Proxmox VE Helper Scripts

**Repo:** [community-scripts/ProxmoxVE](https://github.com/community-scripts/ProxmoxVE) · **License:** MIT · **Kiểm:** 2026-11-23, `docs-read`, [`ffd23fd306e2`](https://github.com/community-scripts/ProxmoxVE/tree/ffd23fd306e2a6415160a3965b1b3ca8d5960529) (commit 2026-11-23). **Sao:** 30,167 tại 2026-11-23 theo [GitHub API](https://api.github.com/repos/community-scripts/ProxmoxVE).

| Mục | Đánh giá |
|---|---|
| Mục đích | Bộ script cộng đồng cài ứng dụng vào container hoặc VM trên Proxmox VE. |
| Giá trị và cơ chế theo tài liệu | README phân tách script mô tả ứng dụng với shared engine ở repo core, hỗ trợ đường chạy Incus riêng; CI gọi kiểm script dùng chung. |
| Giới hạn | Lệnh mẫu chạy bằng root trên host và nạp engine ngoài; chỉ review repo này chưa bao phủ toàn chuỗi tải/cài. Chưa thực thi script hoặc xác minh app cuối cùng. |
| Điều kiện tích hợp | Đọc và ghim script lẫn core, thử trên host/VM không chứa dữ liệu chính; kiểm tài nguyên, mạng, storage và cách khôi phục trước khi dùng tiện ích cài nhanh. |
| Lựa chọn đối chiếu | [Ansible](../08-awesome-lists-learning/README.md#6c55-container--devops); Terraform/OpenTofu; cấu hình Proxmox thủ công. |

**Phạm vi bằng chứng:** đã clone, đọc trích đoạn tài liệu, giấy phép và các file cấu hình được dẫn dưới đây; chưa chạy mã, build, benchmark hoặc test upstream. `docs-read` không phải kiểm chứng implementation.

**Nguồn tại cùng SHA:** [README.md](https://github.com/community-scripts/ProxmoxVE/blob/ffd23fd306e2a6415160a3965b1b3ca8d5960529/README.md) · [LICENSE](https://github.com/community-scripts/ProxmoxVE/blob/ffd23fd306e2a6415160a3965b1b3ca8d5960529/LICENSE) · [.github/workflows/pr-script-test.yml](https://github.com/community-scripts/ProxmoxVE/blob/ffd23fd306e2a6415160a3965b1b3ca8d5960529/.github/workflows/pr-script-test.yml).

<a id="anhkysuai-requarks-wiki"></a>

### Wiki.js

**Repo:** [requarks/wiki](https://github.com/requarks/wiki) · **License:** AGPL-3.0 · **Kiểm:** 2026-11-23, `docs-read`, [`d05ff15437ed`](https://github.com/requarks/wiki/tree/d05ff15437ed3452f1132862ef928fa9a6bf0ecd) (commit 2026-11-23). **Sao:** 29,362 tại 2026-11-23 theo [GitHub API](https://api.github.com/repos/requarks/wiki).

| Mục | Đánh giá |
|---|---|
| Mục đích | Ứng dụng wiki tự host cho tài liệu và kiến thức của nhóm. |
| Giá trị và cơ chế theo tài liệu | README tập trung liên kết yêu cầu, cài đặt, changelog và tài liệu; workflow build/publish cho thấy quy trình tạo artifact và draft release. |
| Giới hạn | README gốc ít mô tả cơ chế quyền và storage; chưa đọc backend hay thử editor, search, import/export. Không suy mọi tính năng trên website đã có trong nhánh đã clone. |
| Điều kiện tích hợp | Chọn release, kiểm tài liệu tương ứng và yêu cầu database; thử quyền đọc/sửa, sao lưu và xuất nội dung trước khi nhập kho tri thức. |
| Lựa chọn đối chiếu | BookStack; [Outline](../08-awesome-lists-learning/README.md#6c515-năng-suất-ghi-chú--việc-làm); XWiki. |

**Phạm vi bằng chứng:** đã clone, đọc trích đoạn tài liệu, giấy phép và các file cấu hình được dẫn dưới đây; chưa chạy mã, build, benchmark hoặc test upstream. `docs-read` không phải kiểm chứng implementation.

**Nguồn tại cùng SHA:** [README.md](https://github.com/requarks/wiki/blob/d05ff15437ed3452f1132862ef928fa9a6bf0ecd/README.md) · [LICENSE](https://github.com/requarks/wiki/blob/d05ff15437ed3452f1132862ef928fa9a6bf0ecd/LICENSE) · [.github/workflows/build.yml](https://github.com/requarks/wiki/blob/d05ff15437ed3452f1132862ef928fa9a6bf0ecd/.github/workflows/build.yml).

<a id="anhkysuai-cloudreve-cloudreve"></a>

### Cloudreve

**Repo:** [cloudreve/cloudreve](https://github.com/cloudreve/cloudreve) · **License:** GPL-3.0 · **Kiểm:** 2026-11-23, `docs-read`, [`6193d04f4a95`](https://github.com/cloudreve/cloudreve/tree/6193d04f4a95a770c63fa2a29b7b335f09a6612e) (commit 2026-11-23). **Sao:** 29,002 tại 2026-11-23 theo [GitHub API](https://api.github.com/repos/cloudreve/cloudreve).

| Mục | Đánh giá |
|---|---|
| Mục đích | Hệ quản lý và chia sẻ tệp tự host nối nhiều nhà cung cấp lưu trữ. |
| Giá trị và cơ chế theo tài liệu | README mô tả truyền thẳng client-storage, WebDAV, upload tiếp tục, nhóm người dùng và liên kết hết hạn; go.mod xác định adapter/provider. |
| Giới hạn | Độ tương thích từng provider, preview và download nền chưa được kiểm. Liên kết chia sẻ, credential storage và node tải ngoài mở rộng phạm vi dữ liệu phải bảo vệ. |
| Điều kiện tích hợp | Thử một backend với file lớn/ngắt mạng, kiểm ACL và expiry bằng tài khoản khác; backup metadata, quản lý khóa provider và rà luồng WebDAV trước khi dùng. |
| Lựa chọn đối chiếu | Nextcloud; [Seafile](../08-awesome-lists-learning/README.md#6c526-tự-host--nhà-thông-minh); File Browser. |

**Phạm vi bằng chứng:** đã clone, đọc trích đoạn tài liệu, giấy phép và các file cấu hình được dẫn dưới đây; chưa chạy mã, build, benchmark hoặc test upstream. `docs-read` không phải kiểm chứng implementation.

**Nguồn tại cùng SHA:** [README.md](https://github.com/cloudreve/cloudreve/blob/6193d04f4a95a770c63fa2a29b7b335f09a6612e/README.md) · [LICENSE](https://github.com/cloudreve/cloudreve/blob/6193d04f4a95a770c63fa2a29b7b335f09a6612e/LICENSE) · [go.mod](https://github.com/cloudreve/cloudreve/blob/6193d04f4a95a770c63fa2a29b7b335f09a6612e/go.mod).

<a id="anhkysuai-navidrome-navidrome"></a>

### Navidrome

**Repo:** [navidrome/navidrome](https://github.com/navidrome/navidrome) · **License:** GPL-3.0 · **Kiểm:** 2026-11-23, `docs-read`, [`06df4a5661dc`](https://github.com/navidrome/navidrome/tree/06df4a5661dc7aea82d15deb75684854743149d0) (commit 2026-11-22). **Sao:** 24,909 tại 2026-11-23 theo [GitHub API](https://api.github.com/repos/navidrome/navidrome).

| Mục | Đánh giá |
|---|---|
| Mục đích | Máy chủ thư viện nhạc cá nhân và streaming qua trình duyệt/client. |
| Giá trị và cơ chế theo tài liệu | README tách bản release khỏi master có thể không ổn định; Go manifest cho biết các thư viện tag/media, hỗ trợ đánh giá ứng dụng lưu trữ tự quản. |
| Giới hạn | Không phải kho nhạc có quyền phân phối sẵn. Chưa thử codec, scan metadata hoặc stream trên mobile; workflow đã đọc chỉ quản lý nhãn review, không chứng minh test chức năng. |
| Điều kiện tích hợp | Dùng release với thư viện mẫu, kiểm tagging, transcoding và quyền tài khoản; sao lưu nhạc gốc lẫn database, chỉ mở ra mạng ngoài sau cấu hình HTTPS. |
| Lựa chọn đối chiếu | Jellyfin; Airsonic-Advanced; Ampache. |

**Phạm vi bằng chứng:** đã clone, đọc trích đoạn tài liệu, giấy phép và các file cấu hình được dẫn dưới đây; chưa chạy mã, build, benchmark hoặc test upstream. `docs-read` không phải kiểm chứng implementation.

**Nguồn tại cùng SHA:** [README.md](https://github.com/navidrome/navidrome/blob/06df4a5661dc7aea82d15deb75684854743149d0/README.md) · [LICENSE](https://github.com/navidrome/navidrome/blob/06df4a5661dc7aea82d15deb75684854743149d0/LICENSE) · [go.mod](https://github.com/navidrome/navidrome/blob/06df4a5661dc7aea82d15deb75684854743149d0/go.mod) · [.github/workflows/review-attestation-label.yml](https://github.com/navidrome/navidrome/blob/06df4a5661dc7aea82d15deb75684854743149d0/.github/workflows/review-attestation-label.yml).

<a id="anhkysuai-louislam-dockge"></a>

### Dockge

**Repo:** [louislam/dockge](https://github.com/louislam/dockge) · **License:** MIT · **Kiểm:** 2026-11-23, `docs-read`, [`0329dabb5003`](https://github.com/louislam/dockge/tree/0329dabb5003f206d4fd9f7403a6af26d7138497) (commit 2026-10-23). **Sao:** 24,884 tại 2026-11-23 theo [GitHub API](https://api.github.com/repos/louislam/dockge).

| Mục | Đánh giá |
|---|---|
| Mục đích | Giao diện quản lý các stack compose.yaml và nhiều Docker host. |
| Giá trị và cơ chế theo tài liệu | README nhấn mạnh compose file vẫn nằm trên đĩa và dùng được bằng CLI thường; có terminal thời gian thực, manifest/CI lint, typecheck và build frontend. |
| Giới hạn | Quyền terminal/engine có ảnh hưởng lớn đến host; kiểm TypeScript không thay test thao tác runtime. Windows được README ghi chưa hỗ trợ, dù CI có bước liên quan Windows. |
| Điều kiện tích hợp | Thử với stack dev, bảo vệ dashboard và quyền Docker socket; giữ compose trong version control, kiểm backup volume và hành vi cập nhật image. |
| Lựa chọn đối chiếu | Portainer; Docker Compose CLI; Dockhand. |

**Phạm vi bằng chứng:** đã clone, đọc trích đoạn tài liệu, giấy phép và các file cấu hình được dẫn dưới đây; chưa chạy mã, build, benchmark hoặc test upstream. `docs-read` không phải kiểm chứng implementation.

**Nguồn tại cùng SHA:** [README.md](https://github.com/louislam/dockge/blob/0329dabb5003f206d4fd9f7403a6af26d7138497/README.md) · [LICENSE](https://github.com/louislam/dockge/blob/0329dabb5003f206d4fd9f7403a6af26d7138497/LICENSE) · [package.json](https://github.com/louislam/dockge/blob/0329dabb5003f206d4fd9f7403a6af26d7138497/package.json) · [.github/workflows/ci.yml](https://github.com/louislam/dockge/blob/0329dabb5003f206d4fd9f7403a6af26d7138497/.github/workflows/ci.yml).

<a id="anhkysuai-2026-11-23-monicahq-monica"></a>

### monica

**Repo:** [monicahq/monica](https://github.com/monicahq/monica) · **License:** AGPL-3.0 · **★ 25,827 (GitHub API, 2026-11-23)**

**Mục đích:** Ứng dụng quản lý quan hệ cá nhân để ghi thông tin, sự kiện và tương tác với người quen.

**Giá trị:** Mô hình PRM phù hợp tham khảo tổ chức dữ liệu quan hệ và nhắc việc theo ngữ cảnh cá nhân.

**Giới hạn:** Nhánh được clone là beta; README trỏ bản ổn định sang nhánh 4.x. Dữ liệu quan hệ có tính riêng tư, cần kiểm quyền truy cập, sao lưu và xuất dữ liệu trước sử dụng.

**Cách tham khảo/tích hợp:** Đọc cấu hình triển khai, giới hạn license và hợp đồng dữ liệu; thử auth, migration, backup/restore với dữ liệu mẫu trước tích hợp.

**Lựa chọn để đối chiếu:** [monicahq/chandler](https://github.com/monicahq/chandler) · [twentyhq/twenty](https://github.com/twentyhq/twenty). Đây là ứng viên so sánh theo tác vụ; mức phù hợp cần kiểm theo hồ sơ và phiên bản riêng.

**Bằng chứng:** `docs-read`, ngày 2026-11-23, commit [`dab74273acc5c9e0ba713a9f7c2c71c24ab16993`](https://github.com/monicahq/monica/commit/dab74273acc5c9e0ba713a9f7c2c71c24ab16993), ngày commit 2026-10-28. Đã clone và đọc chọn lọc phần giới thiệu, cách dùng, giới hạn, license, metadata manifest và CI hiện diện. Chưa kiểm đầy đủ implementation hoặc chạy upstream; các số đo của tác giả chưa được tái lập.

**Nguồn:** [README.md](https://github.com/monicahq/monica/blob/dab74273acc5c9e0ba713a9f7c2c71c24ab16993/README.md) · [LICENSE.md](https://github.com/monicahq/monica/blob/dab74273acc5c9e0ba713a9f7c2c71c24ab16993/LICENSE.md) · [package.json](https://github.com/monicahq/monica/blob/dab74273acc5c9e0ba713a9f7c2c71c24ab16993/package.json) · [composer.json](https://github.com/monicahq/monica/blob/dab74273acc5c9e0ba713a9f7c2c71c24ab16993/composer.json) · [.github/workflows/tests.yml](https://github.com/monicahq/monica/blob/dab74273acc5c9e0ba713a9f7c2c71c24ab16993/.github/workflows/tests.yml) · [metadata GitHub](https://api.github.com/repos/monicahq/monica).

<a id="anhkysuai-2026-11-23-firefly-iii-firefly-iii"></a>

### firefly-iii

**Repo:** [firefly-iii/firefly-iii](https://github.com/firefly-iii/firefly-iii) · **License:** AGPL-3.0 · **★ 25,320 (GitHub API, 2026-11-23)**

**Mục đích:** Ứng dụng tự host quản lý thu chi cá nhân, ngân sách, nhãn và báo cáo.

**Giá trị:** Tham khảo mô hình giao dịch và phân loại chi tiêu; hệ sinh thái có công cụ nhập dữ liệu được giới thiệu trong README.

**Giới hạn:** Chưa xác minh đối soát số liệu hoặc cơ chế bảo vệ dữ liệu tài chính bằng chạy thử; tích hợp nguồn nhập cần kiểm định dạng, tiền tệ, sao lưu và quyền truy cập.

**Cách tham khảo/tích hợp:** Đọc cấu hình triển khai, giới hạn license và hợp đồng dữ liệu; thử auth, migration, backup/restore với dữ liệu mẫu trước tích hợp.

**Lựa chọn để đối chiếu:** [actualbudget/actual](https://github.com/actualbudget/actual) · [maybe-finance/maybe](https://github.com/maybe-finance/maybe). Đây là ứng viên so sánh theo tác vụ; mức phù hợp cần kiểm theo hồ sơ và phiên bản riêng.

**Bằng chứng:** `docs-read`, ngày 2026-11-23, commit [`e1a90bf8ee7499524039b331179e40431b3c84af`](https://github.com/firefly-iii/firefly-iii/commit/e1a90bf8ee7499524039b331179e40431b3c84af), ngày commit 2026-11-14. Đã clone và đọc chọn lọc phần giới thiệu, cách dùng, giới hạn, license, metadata manifest và CI hiện diện. Chưa kiểm đầy đủ implementation hoặc chạy upstream; các số đo của tác giả chưa được tái lập.

**Nguồn:** [readme.md](https://github.com/firefly-iii/firefly-iii/blob/e1a90bf8ee7499524039b331179e40431b3c84af/readme.md) · [COPYING](https://github.com/firefly-iii/firefly-iii/blob/e1a90bf8ee7499524039b331179e40431b3c84af/COPYING) · [LICENSE](https://github.com/firefly-iii/firefly-iii/blob/e1a90bf8ee7499524039b331179e40431b3c84af/LICENSE) · [package.json](https://github.com/firefly-iii/firefly-iii/blob/e1a90bf8ee7499524039b331179e40431b3c84af/package.json) · [composer.json](https://github.com/firefly-iii/firefly-iii/blob/e1a90bf8ee7499524039b331179e40431b3c84af/composer.json) · [.github/workflows/lock.yml](https://github.com/firefly-iii/firefly-iii/blob/e1a90bf8ee7499524039b331179e40431b3c84af/.github/workflows/lock.yml) · [metadata GitHub](https://api.github.com/repos/firefly-iii/firefly-iii).

<a id="anhkysuai-2026-11-23-arendst-tasmota"></a>

### Tasmota

**Repo:** [arendst/Tasmota](https://github.com/arendst/Tasmota) · **License:** GPL-3.0 · **★ 25,013 (GitHub API, 2026-11-23)**

**Mục đích:** Firmware thay thế cho thiết bị ESP8266/ESP32, điều khiển cục bộ qua MQTT, HTTP và các giao thức thiết bị.

**Giá trị:** Quy tắc, timer và OTA được tài liệu hóa, hữu ích cho nghiên cứu tự động hóa IoT giảm phụ thuộc cloud.

**Giới hạn:** README cảnh báo cập nhật có thể thất bại và cần khôi phục qua serial; phải xác định đúng bo mạch, sao lưu cấu hình và thử trên thiết bị dễ tiếp cận trước.

**Cách tham khảo/tích hợp:** Ghim phiên bản, xác định quyền cần cấp và thử quy trình trong môi trường riêng; kiểm kết quả và đường khôi phục trước dùng với tài nguyên thật.

**Lựa chọn để đối chiếu:** [esphome/esphome](https://github.com/esphome/esphome) · [home-assistant/core](https://github.com/home-assistant/core). Đây là ứng viên so sánh theo tác vụ; mức phù hợp cần kiểm theo hồ sơ và phiên bản riêng.

**Bằng chứng:** `docs-read`, ngày 2026-11-23, commit [`016be6317eb963777ae1879b9f59a76cca9e83e9`](https://github.com/arendst/Tasmota/commit/016be6317eb963777ae1879b9f59a76cca9e83e9), ngày commit 2026-11-22. Đã clone và đọc chọn lọc phần giới thiệu, cách dùng, giới hạn, license, metadata manifest và CI hiện diện. Chưa kiểm đầy đủ implementation hoặc chạy upstream; các số đo của tác giả chưa được tái lập.

**Nguồn:** [README.md](https://github.com/arendst/Tasmota/blob/016be6317eb963777ae1879b9f59a76cca9e83e9/README.md) · [LICENSE.txt](https://github.com/arendst/Tasmota/blob/016be6317eb963777ae1879b9f59a76cca9e83e9/LICENSE.txt) · [.github/workflows/Tasmota_build_devel.yml](https://github.com/arendst/Tasmota/blob/016be6317eb963777ae1879b9f59a76cca9e83e9/.github/workflows/Tasmota_build_devel.yml) · [metadata GitHub](https://api.github.com/repos/arendst/Tasmota).

<a id="nt-2026-11-23"></a>

## Nâng trần theo khoảng trống — 23/11/2026

Phần này có các hồ sơ mới của đợt nâng trần: mười trinh sát tìm trên internet và GitHub những mảng mà chuyên mục còn thiếu hoặc chỉ có hồ sơ cũ, rồi mỗi repo được clone nông tại một commit cố định, đọc LICENSE, README, ít nhất một file triển khai thật và CI nếu có; không cài hay chạy mã upstream. Mô tả của trinh sát nhiều chỗ sai so với mã thật, và các chỗ đó được sửa ngay trong từng hồ sơ. Số sao lấy sau bằng GitHub search API nên có thể để trống.

<a id="nt-external-secrets"></a>

### External Secrets Operator

| Thuộc tính | Giá trị |
|---|---|
| Repo | https://github.com/external-secrets/external-secrets |
| License | Apache-2.0 |
| Phiên bản đã đọc | `9f8b5837188cf1e394b8e1f2dc0e9d63afe2aa68` (commit 2026-11-23) |
| Kiểm chứng | 2026-11-23; code-read; đã đọc README.md, LICENSE, AGENTS.md, apis/externalsecrets/v1/externalsecret_types.go, apis/externalsecrets/v1/generic_store.go, .github/workflows/zizmor.yml; chưa chạy upstream |
| Khoảng trống lấp | Bí mật và quyền cho workload: giữ bí mật ngoài repo và prompt, kéo từ kho ngoài vào cụm lúc chạy |
| Cơ chế đáng học | - CRD trong `apis/externalsecrets/v1`: `ExternalSecret` khai refreshInterval, creationPolicy, deletionPolicy; `ClusterSecretStore` dùng chung toàn cụm (`generic_store.go`).<br>- Mỗi provider là module Go riêng trong `providers/v1/*` (42 thư mục); `generators/v1` có password, uuid, sshkey, sts, vault, webhook, github...<br>- Có webhook xác thực CRD và certcontroller quản chứng chỉ webhook (AGENTS.md). |
| Tiêu chí và cách kiểm | Kiểm bằng máy: AGENTS.md yêu cầu `make test && make check-diff` trước PR; workflow zizmor.yml (đã đọc) quét lỗi bảo mật của chính các workflow Actions, dùng harden-runner và pin SHA; có e2e theo nhà cung cấp, scorecard, dependency-review (chỉ thấy tên). |
| Giới hạn và rủi ro | Apache-2.0. Repo nhiều module go.mod, nặng. Tin cậy phụ thuộc cấu hình ClusterSecretStore (phạm vi namespace) và quyền của operator, đọc bí mật từ kho ngoài bằng thông tin xác thực của chính nó. Không thấy telemetry trong phần đã đọc. |
| So với | OpenBao (kho bí mật gốc, ESO chỉ là cầu nối), Infisical, SOPS |
| Nguồn | [README.md](https://github.com/external-secrets/external-secrets/blob/9f8b5837188cf1e394b8e1f2dc0e9d63afe2aa68/README.md) · [LICENSE](https://github.com/external-secrets/external-secrets/blob/9f8b5837188cf1e394b8e1f2dc0e9d63afe2aa68/LICENSE) · [AGENTS.md](https://github.com/external-secrets/external-secrets/blob/9f8b5837188cf1e394b8e1f2dc0e9d63afe2aa68/AGENTS.md) · [externalsecret_types.go](https://github.com/external-secrets/external-secrets/blob/9f8b5837188cf1e394b8e1f2dc0e9d63afe2aa68/apis/externalsecrets/v1/externalsecret_types.go) · [generic_store.go](https://github.com/external-secrets/external-secrets/blob/9f8b5837188cf1e394b8e1f2dc0e9d63afe2aa68/apis/externalsecrets/v1/generic_store.go) · [zizmor.yml](https://github.com/external-secrets/external-secrets/blob/9f8b5837188cf1e394b8e1f2dc0e9d63afe2aa68/.github/workflows/zizmor.yml) |
