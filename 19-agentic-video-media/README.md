# 19 · Agentic Video & Media Production

> Hệ thống để coding agent sản xuất video/media đầu-cuối, model sinh video mở, và làn sóng "video/motion skills" cho Claude Code. Mục này mở ra từ link người dùng gửi (`calesthio/OpenMontage`, 2026-10-12). Liên quan: mục 14 (TTS, VLM, ComfyUI), mục 04 (skills), mục 11 (sandbox).

---

## 1. calesthio/OpenMontage ⭐ (link từ người dùng)

### 1.1 Hồ sơ nhanh

| Thuộc tính | Giá trị (đọc 2026-10-12) |
|---|---|
| Repo | https://github.com/calesthio/OpenMontage · site openmontage.video · X @calesthioailabs |
| Mô tả | "World's first open-source, agentic video production system. 12 production pipelines, 100+ tools, 700+ agent skill and production-knowledge files. Turn your AI coding assistant into a full video production studio." |
| ★ / forks / watchers | **67.1k ★** · 8.5k forks · 370 watchers · 455 commit · 113 issue mở · 284 PR (một aggregator ghi 355 issue/70 PR mở – số liệu lệch) |
| License | **AGPL-3.0** |
| Ngôn ngữ | Python 3.10+ (tools, state), JS/React (Remotion composer), HTML/GSAP (HyperFrames), YAML (pipeline manifest), Markdown (skills); cần FFmpeg, Node 18+ (22+ cho HyperFrames) |
| Tác giả | `calesthio` – bio "Building open source AI Assisted and Agentic Tools", **Microsoft, Seattle**; 1.3k followers; repo khác: Crucix (12.1k★, agent giám sát nguồn dữ liệu), generative-media-skills (199★), Resonant, PhantomReach; sponsor: Bloome, Atlas Cloud |
| Lịch sử | #1 GitHub Trending "Repository of the Day"; bài viết đầu tiên ~6/2026; cadence: dồn dập 14–22/8/2026 (17 merge trong ngày 22/8), sau đó thưa (26/8, 6/9, 3/10 – refresh provider, thêm HeyGen Avatar); fix CVE-2026-67213 ngày 20/8 |

### 1.2 Kiến trúc "agent là orchestrator" (điểm đáng học nhất)

- **Không có code orchestrator.** `AGENTS.md` chỉ là stub bắt agent đọc `AGENT_GUIDE.md` → `PROJECT_CONTEXT.md`. Python chỉ cung cấp tool + persistence; mọi quyết định sáng tạo/review nằm trong file hướng dẫn. *"The intelligence is in the skills, not in improvised code."*
- **Pipeline cố định:** `research → proposal → script → scene_plan → assets → edit → compose`; mỗi stage có một **director skill** (Markdown) và sinh đúng một artifact (brief, script, scene plan, asset manifest, edit decisions, render report) phải validate qua **20+ JSON Schema**. *"Every video production request MUST go through the pipeline system. No exceptions."*
- **Approval gate theo stage:** manifest khai `human_approval_default`; stage gated dừng ở trạng thái `awaiting_human` và agent **phải kết thúc lượt**; "Approval is per-gate"; pre-authorize cả run phải được log như quyết định `approval_policy`. Stage `assets` luôn gated để người xem cảnh trước khi compose.
- **Ba lớp tri thức:** L1 `tools/` (cái gì tồn tại, giá bao nhiêu) → L2 `skills/` (OpenMontage muốn dùng tool thế nào) → L3 `.agents/skills/` (kỹ thuật theo vendor; **bắt buộc đọc trước khi gọi tool sinh**). Đọc source chỉ để debug/audit.
- **Tool registry runtime:** agent gọi `capability_catalog()`, `provider_catalog()` thay vì danh sách cứng; selector (`tts_selector`, `image_selector`, `video_selector`) chọn theo ưu tiên người dùng → sẵn có → thứ tự khám phá; README nói chấm 7 chiều (task fit, quality, control, reliability, cost, latency, continuity) và log cả phương án bị loại. *"Silent runtime swap is forbidden."*
- **State:** `projects/<id>/` với `checkpoint_<stage>.json`, bản cũ vào `history/`; `decision_log` chỉ **append**, không sửa.
- **Ngân sách:** `tools/cost_tracker.py`; ước tính chi phí ở proposal; mặc định trần $10/tổng, hỏi lại trên $0.50/hành động; call trả phí phải nêu tool/provider/model/lý do trước; chạy mẫu trước batch.
- **Quality:** reviewer meta-skill sau mỗi stage (tối đa 2 vòng; critical/suggestion/nitpick); pre-compose validation, post-render check bằng ffprobe/frame extraction/audio analysis; "slideshow-risk check" chặn output "animated PowerPoint"; *"Still-image fallback is forbidden"* khi yêu cầu có chuyển động.
- **Anti-pattern nêu rõ:** bỏ qua pipeline bằng script ad-hoc, gọi tool sinh mà chưa đọc L3, đổi provider/render path không xin phép, giấu đường degrade, hardcode provider/key, sinh asset trước khi plan được duyệt.
- **Backlot:** bảng điều khiển local (`python -m backlot open`) hiện tiến độ, gate, chi tiêu.

### 1.3 Pipeline & provider

11 pipeline trong README (About nói 12): Animated Explainer, Animation, Avatar Spokesperson, Cinematic, Clip Factory, Documentary Montage (ghép footage mở từ Archive.org/NASA/Wikimedia), Hybrid, Localization & Dub, Podcast Repurpose, Screen Demo, Talking Head (+ character animation). Provider: FLUX, Kling, Veo, Runway, WAN 2.2 (qua ComfyUI), HeyGen Avatar; TTS ElevenLabs/OpenAI/Google/**Piper (free)**; nhạc Suno/ElevenLabs; stock Pexels/Pixabay/Unsplash. **Zero-key path** hoàn toàn miễn phí.

### 1.4 Đánh giá từ bên ngoài

| Nguồn | Nội dung |
|---|---|
| pinggy.io (26/6/2026) | Free tier chạy end-to-end, explainer 60s mất ~10–15 phút; chi phí ví dụ: Ghibli-style 12 ảnh FLUX ~$0.15, history 70s OpenAI TTS ~$0.02, ad 4 ảnh ~$0.69. Điểm yếu: setup nặng (Python+Node+FFmpeg+SDK), chưa có Docker, pipeline cao cấp phụ thuộc API trả phí |
| knightli.com (22/6/2026) | Hướng dẫn cài; lỗi thường gặp: venv, `npm ERR_INVALID_ARG_TYPE` (fix `npx --yes npm install`), PowerShell policy, 401/429, GPU/CUDA; khuyên `make demo` 15–30s trước; "không phải one-prompt video generator" |
| dev.to/andrew-ooo | Piper kém ElevenLabs; footage archive giới hạn thẩm mỹ public-domain; **model agent quyết định chất lượng** (model mạnh chọn pipeline/script tốt hơn rõ rệt); phí agent ~$3–7 cho video 60s trên model top; AGPL: dùng nội bộ/consulting ok, SaaS phải mở mã sửa đổi |
| hysenlabs, opensourcealternatives.to, explainx | AGPL là caveat chính; "fast-moving, cần hardening trước production"; số liệu tool/skill lệch giữa nguồn (52 vs 100+ tool; 400+ vs 700+ skill) |
| Thảo luận cộng đồng | OpenMAIC (THU) bàn dùng OpenMontage làm MCP service cho nội dung học tập; OpenViking (Volcengine) RFC dùng làm benchmark context |

### 1.5 Nhận xét & cách tận dụng

- **Giá trị cốt lõi:** không phải model video mà là **mẫu kiến trúc "skills-as-orchestrator"** ở quy mô lớn: pipeline manifest + director skill + schema + gate + decision log + cost tracker. Đây là bản mở rộng tự nhiên của SKILL.md (mục 04) và evaluator pattern (mục 03) sang domain sáng tạo nhiều bước, nhiều provider.
- **Bài học tái dùng cho bất kỳ agent workflow nào:** (1) artifact chuẩn hóa + schema mỗi stage; (2) gate theo stage với trạng thái `awaiting_human` và agent phải dừng lượt; (3) registry runtime thay danh sách cứng; (4) ba lớp tri thức tách "cái gì/như thế nào/kỹ thuật vendor"; (5) append-only decision log; (6) reviewer meta-skill có giới hạn vòng.
- **Rủi ro:** AGPL với SaaS; dự án trẻ, nhiều issue mở, cadence commit chậm từ 9/2026; setup phức tạp (chưa Docker); chất lượng phụ thuộc model agent và provider trả phí; marketing numbers chưa nhất quán.
- **Gợi ý:** chạy zero-key path trong sandbox (mục 11) để học kiến trúc; nếu dùng thương mại, kiểm tra AGPL; so sánh với `generative-media-skills` (cùng tác giả, nhẹ hơn) nếu chỉ cần sinh ảnh/âm thanh.

---

### 1.6 Cập nhật 2026-10-31: kiểm ảnh README người dùng gửi và clone lại

Ảnh là phần đầu README: tab "README · Contributing · AGPL-3.0 license", mascot **"Monty the Clapper — the official mascot of OpenMontage"**, dòng "The first open-source, agentic video production system", nút website openmontage.video, các link mục lục, badge `license AGPLv3` và khung **"GitHub Trending #1 Repository Of The Day"**.

| Ý trong ảnh | Thực tế (clone 31/10/2026) | Kiểm |
|---|---|---|
| License AGPL-3.0 | File `LICENSE` là GNU AGPL v3 | ✅ — nhắc lại: dùng trong dịch vụ mạng phải công bố mã sửa đổi |
| "The first open-source, agentic video production system" | Khẩu hiệu tự nhận; mục 19 có các hệ tương tự (OpenCreator §1b, mục 22) ra đời gần cùng thời | ⚠️ tuyên bố marketing |
| "#1 Repository Of The Day" | Badge là **file SVG tự lưu trong repo** (`.github/assets/repo-of-the-day-light.svg`), không phải badge động từ dịch vụ bên ngoài; §1.1 đã ghi nhận sự kiện trending này | ⚠️ không tự kiểm được qua badge |
| Mascot Monty | Đúng (`assets/monty-*.svg`) | ✅ |

| Mục | 12/10/2026 (§1.1) | 31/10/2026 |
|---|---|---|
| ★ / fork | 67,1k / 8,5k | **74k / 9,7k** (shields) |
| Commit | 455 | **500** từ 29/3/2026, 80 tác giả (calesthio ~320, 2 tên); 43 trailer Claude; 22 commit từ 13/10 |
| Issue / PR mở | 113 / 284 | **114 / 304** |
| Quy mô (đếm bằng script) | "12 pipeline, 100+ tool, 700+ file skill" (README) | `pipeline_defs/` **13** file, `tools/` **195** file Python, `skills/` **157** file `.md` (con số "700+" của README gộp cả file tri thức khác) |
| CI | – | **1 workflow** (`ci.yml`) |

- **Vá bảo mật qua advisory riêng (28/10):** "Merge commit from fork" sửa `tools/video/showcase_card.py` + `video_compose.py` và thêm 231 dòng `tests/tools/test_showcase_card_security.py` (kiểm thuộc tính `force_style` thật) — dấu hiệu một lỗ hổng chèn tham số vào phụ đề/khung hình được báo riêng *(chưa thấy GHSA công khai, chưa xác minh chi tiết)*. Cập nhật lên commit sau 28/10 nếu dùng `showcase_card`.
- **Backlot** (`python -m backlot open`, có từ 1/7/2026): bảng storyboard cục bộ chỉ đọc, hiển thị pipeline, kịch bản, scene plan, chi phí; commit 24/10 **từ chối request có Host header không tin cậy** (chống DNS rebinding). **Ink Theater** (30/6/2026): engine "moving art" mực đen tất định, ghi rõ cảm hứng từ skill 小黑/Xiaohei (MIT).
- Đợt 23–24/10 là loạt sửa cache, audio/video, phụ đề RTL, cập nhật provider (Gemini TTS, ElevenLabs, Google); 16/10 gỡ mục Sponsors khỏi README.
- Nhận định §1.5 giữ nguyên.

**Nguồn §1.6:** ảnh README người dùng gửi 31/10/2026 · clone github.com/calesthio/OpenMontage 31/10/2026 (blob:none, 500 commit, HEAD 195eab2 28/10/2026; README.md, LICENSE, backlot/README.md, ink-theater/README.md, pipeline_defs/, tools/, skills/, .github/workflows/ci.yml; git show của commit "Merge commit from fork" 28/10) · img.shields.io/github/{stars,forks,license,last-commit,issues,issues-pr}/calesthio/OpenMontage.json (31/10/2026)

## 1b. krillinai/OpenCreator, tên cũ KrillinAI (ảnh README người dùng gửi, 2026-10-13)

### 1b.1 Hồ sơ nhanh

| Thuộc tính | Giá trị (đọc 2026-10-13) |
|---|---|
| Repo | https://github.com/krillinai/OpenCreator (link cũ `krillinai/KrillinAI` chuyển hướng về đây) · site open-creator.ai |
| Mô tả (About) | "Formerly KrillinAI. Open-source AI workspace for creators, powered by Codex. Create videos, images, voice, avatars, translations, and edits with Agents in one place." |
| ★ / fork | **~13k ★ · ~1,4k fork** (shields 13/10/2026; ảnh chụp ghi 11.5k/1.1k là số cũ) · 28 issue mở · 5 PR mở · bản phát hành v3.2.6 |
| License | **Apache-2.0** từ 21/9/2026. Trước đó GPL-3.0: `LICENSE` gốc tạo 27/12/2024 là GPLv3; `runtime/krillinai/LICENSE` đổi GPLv3 → Apache ở commit bfbf59a ngày 29/9/2026 |
| Tên gọi | KrillinAI → KlicStudio (khoảng 2025) → KrillinAI (đổi lại 12/9/2025) → OpenCreator (9/2026) |
| Lịch sử | Commit đầu 17/12/2024; 936 commit; 358 commit từ 1/8/2026 (đọc git 13/10/2026). Huy hiệu Trendshift "#1 Repository of the Day" có thật, trang Trendshift không ghi ngày (chưa xác minh ngày) |
| Ngôn ngữ | TypeScript ~82%, Go ~9% (ảnh chụp; Go là `runtime/krillinai`, lõi dịch video cũ) |

### 1b.2 Kiến trúc (đọc README + mã)

- **Không tự viết vòng lặp agent.** Dùng **Codex CLI** (app-server) làm động cơ; OpenCreator thêm daemon cục bộ, giao diện web và vỏ desktop. Chạy tác vụ thật cần đăng nhập ChatGPT hoặc API key (Codex hoặc nhà cung cấp tương thích OpenAI).
- **Ba lớp:** `apps/web` (React 18 + Vite) → `apps/daemon` (Fastify, Runtime API + SSE, SQLite, lịch chạy, duyệt quyền, bộ nhớ) → Codex + bộ công cụ media (FFmpeg, yt-dlp, Whisper, dịch vụ AI). `apps/desktop` là Electron nạp lại đúng bản web.
- **Một máy trạng thái cho hai giao diện:** thao tác trên workspace và lệnh trong hội thoại cùng đẩy sự kiện vào một máy trạng thái; mỗi lần sửa tạo phiên bản mới, không ghi đè.
- **Daemon chỉ nghe loopback:** `server.listen({ host: '127.0.0.1', port: 0 })` (`apps/daemon/src/main.ts`), token tạm in ra stdout một lần.
- **Skills:** 7 skill trong `skills/` điều khiển CLI KrillinAI (phụ đề, TTS, render ngang/dọc, ảnh bìa, kiểm kế hoạch pipeline). Mặc định dùng `$CODEX_HOME` chung, nên đổi skill/MCP ở đây là đổi cấu hình Codex toàn máy.
- **CI:** `pnpm audit --audit-level high`, test daemon/desktop/web, actionlint cho workflow phát hành.

### 1b.3 Kiểm ảnh README

| Ô trong ảnh | Kết luận |
|---|---|
| "Formerly KrillinAI" | ✅ Đúng; còn một tên trung gian là KlicStudio |
| "Open-source" | ⚠️ Mã Apache-2.0, nhưng tài khoản, gói đăng ký, tín dụng và "official model services" đi qua gateway `open-creator.ai` (mặc định trong `OPENCREATOR_GATEWAY_ORIGIN`, thanh toán Stripe). Tự cấu hình key riêng vẫn dùng được |
| "powered by Codex" | ✅ Đúng như mã: Codex là nguồn sự thật cho vòng lặp agent, Skills, MCP |
| "videos, images, voice, avatars, translations, and edits" | ⚠️ Digital Avatar và Auto Clips đang ghi "In development"; 10 công cụ còn lại ✅ Available |
| 11.5k★ · 1.1k fork | ⚠️ Số cũ; nay ~13k / ~1,4k |
| "#1 Repository of the Day" | ✅ Huy hiệu Trendshift #1 có thật; ngày đạt chưa xác minh |
| 14 ngôn ngữ README | ✅ 13 bản dịch trong `docs/<lang>/` + tiếng Anh |
| Ngôn ngữ mã TS/Go | ✅ Khớp cấu trúc repo |

**Tổng: 5✅ / 3⚠️ / 0❌.** Ảnh không sai ô nào; điều đáng biết nằm ngoài ảnh (mục dưới).

### 1b.4 Điều ảnh không nói

- **Telemetry bật mặc định ở bản desktop chính thức.** `apps/desktop/src/main/telemetry.ts` gửi mỗi 6 giờ `install_id`, số lần mở, phút hoạt động, phiên bản, hệ điều hành, kiến trúc tới `https://admin.clawee.work/api/v1/public/desktop-usage`; `telemetryEnabled: true` trong `settings-store.ts`. Có công tắc tắt trong Cài đặt, mô tả nói rõ máy chủ ghi IP và không gửi nội dung dự án/file/hội thoại. README không nhắc. Quan hệ giữa domain `clawee.work` và dự án: chưa xác minh. Bản build từ nguồn không gửi (endpoint rỗng khi không phải bản chính thức).
- **Đổi giấy phép GPL-3.0 → Apache-2.0 trên mã có 22 email tác giả khác nhau** (commit trước 8/2026). Repo không có CLA/DCO trong `CONTRIBUTING.md`. Đổi từ GPL sang giấy phép dễ dãi hơn thường cần đồng ý của người giữ bản quyền; repo không ghi đã xin (chưa xác minh). Ai phân phối lại phần mã cũ nên để ý.
- **Trình tải video** nhận YouTube, TikTok, Douyin, Instagram… qua yt-dlp, có thể cần cookie nền tảng. Đây là công cụ, rủi ro điều khoản dịch vụ và bản quyền nằm ở người dùng.
- **Đánh giá bên ngoài:** chưa thấy bài dùng thử độc lập. Bài aiindigo.com ("deep dive") đọc như quảng bá; bản mirror SourceForge vẫn ghi GPLv3 (ảnh chụp cũ).

### 1b.5 Nhận xét & cách tận dụng

- **So với OpenMontage (§1):** OpenMontage để agent làm orchestrator qua skill + schema + gate; OpenCreator đặt **máy trạng thái trong daemon** và cho agent (Codex) cùng giao diện trực quan đẩy sự kiện vào đó. Mẫu đáng học: một nguồn sự thật cho cả UI lẫn hội thoại, mỗi lần sửa là một phiên bản.
- **Thế mạnh thật:** dịch phụ đề + lồng tiếng (14 ngôn ngữ nguồn, 101 ngôn ngữ đích theo README) có từ thời KrillinAI; giấy phép Apache-2.0 nay thoáng hơn AGPL của OpenMontage.
- **Rủi ro:** phụ thuộc Codex CLI và tài khoản OpenAI/nhà cung cấp; telemetry mặc định bật; nguồn gốc giấy phép phần mã cũ; dự án đổi tên ba lần, tốc độ thay đổi cao (358 commit trong ~2,5 tháng).
- **Gợi ý:** chạy bản web từ nguồn (`pnpm web:dev`, không gửi telemetry) với `CODEX_HOME` riêng để khỏi đụng cấu hình Codex chung; nếu dùng desktop, tắt "Send anonymous usage data".

---

## 1c. saturndec/waoowaoo (nay là waooAI/waoowaoo): từ "studio phim ngắn AI" thành workspace ảnh/video (link người dùng, 2026-10-13)

> Người dùng gửi `saturndec/waoowaoo`. Repo đã chuyển sang tổ chức `waooAI/waoowaoo` (link cũ vẫn chuyển hướng; shields trả cùng số cho cả hai). Đã clone toàn bộ repo (27 commit, HEAD `dfec20e` 21/9/2026), đọc README các bản, `LICENSE` qua `git log`, `docs/INSTALL.md`, `docker-compose.yml`, `Dockerfile.codex-runtime`, `package.json`. Chưa chạy test vì cần MySQL, Redis và Temporal.

### 1c.1 Hồ sơ nhanh

| Mục | Thông tin (đọc 13/10/2026) |
|---|---|
| Repo | `waooAI/waoowaoo` (tên cũ `saturndec/waoowaoo`) · ~15k★, ~3,2k fork · ~140 issue mở, **0 PR mở** · release ổn định mới nhất v0.4.1 (3/4/2026); tag `v0.5.0-beta.1` (5/9/2026); commit cuối 21/9/2026 |
| Tác giả | "saturn" (`saturndec`, ~23 commit) và bot `waoowaoo-publisher` (4 commit). Mã được đẩy theo từng đợt phát hành, không có lịch sử phát triển chi tiết. Đội ngũ có bản web thương mại (waitlist tại waoowaoo.com) |
| Đóng góp | README: nhóm lõi tự làm, PR từ ngoài chỉ để tham khảo, **không merge trực tiếp** |
| Stack (v0.5) | Next.js 16 + React 19, MySQL + Prisma, **Temporal** (durable execution), Redis, MinIO riêng, NextAuth, Caddy (HTTPS cục bộ cổng 1443) |
| Model | Bản preview chỉ mở cấu hình **OpenRouter**: GPT Image 2, các bản Nano Banana, Seedance, MiniMax H3/H3 Max. Người dùng tự trả phí qua key OpenRouter của mình |

### 1c.2 Hai sản phẩm khác nhau dưới cùng một tên

| | v0.3.0 → v0.4.1 (3–4/2026) | v0.5.0-beta.1 (9/2026) |
|---|---|---|
| Mô tả | "waoowaoo AI 影视 Studio": công cụ làm **phim ngắn/truyện tranh động** từ tiểu thuyết: phân tích kịch bản, sinh nhân vật và cảnh nhất quán, dựng phân cảnh thành video, lồng tiếng nhiều vai | "AI creative workspace for images and videos": Assistant bên phải + canvas để quản lý tài liệu tham chiếu, sinh ảnh/video, tinh chỉnh thành phiên bản mới |
| Lồng tiếng / nhạc | Có | **Chưa có** trong bản preview |
| Người làm | README ghi "hiện chỉ mình tôi phát triển" | "waoowaoo team", nhóm lõi |
| Giấy phép | Không có file `LICENSE` tới 27/4/2026, sau đó **CC BY-NC-SA 4.0** (giấy phép nội dung, cấm thương mại) | **Elastic License 2.0**: dùng cá nhân/nội bộ, sửa và phân phối được; cấm cung cấp thành dịch vụ cho bên thứ ba. README tự ghi "source-available, not OSI-approved open source" |

Bản v0.5 thay đổi gần như toàn bộ mã (2.372 file, +147k / −191k dòng so với bản trước). Phần lớn bài giới thiệu bên ngoài (sourcepulse, addrom, skillsllm) và nhiều bản sao vẫn mô tả sản phẩm cũ. Bản sao trên Gitee còn ghi MIT, **sai** với cả hai giấy phép thật.

### 1c.3 Điều cần biết trước khi cài (đọc mã)

- **Container của app được gắn Docker socket** (`/var/run/docker.sock`) để tự khởi container Assistant cho từng dự án. Quyền này tương đương quyền root trên máy host; `docs/INSTALL.md` cũng chỉ ghi "use a trusted local installation". Chỉ nên cài trên máy hoặc VM riêng.
- **Assistant chạy OpenAI Codex CLI 0.146** trong container riêng (sandbox bubblewrap, giới hạn mặc định 2 CPU, 2 GB RAM, 256 tiến trình, tự tắt sau 15 phút rảnh).
- **HTTPS cục bộ bằng CA riêng của Caddy**: quy trình cài yêu cầu tin `root.crt` trên máy. Phần này làm cẩn thận: prompt cài đặt bắt agent hỏi rồi mới tin chứng chỉ, không xuất `root.key`, không bỏ kiểm TLS.
- **Cài kiểu "nhắn coding agent tự cài"**, ghim image theo digest bất biến của release. Prompt cài cũng cấm agent chạy tác vụ AI trả phí khi chưa được đồng ý và cấm hỏi key trong chat. Đây là mẫu prompt cài đặt đáng tham khảo.
- **Có hai bản**: self-hosted (repo này, `BILLING_MODE=OFF`) và bản cloud có tính tiền (script test nhắc thư mục `ee/` không có trong repo).
- **Bản preview**: README cảnh báo còn lỗi; dữ liệu giữa các bản beta trước đây không tương thích, phải xóa dữ liệu cũ khi nâng cấp.

### 1c.4 So sánh & dùng thế nào

| Dự án (shields 13/10/2026) | ★ · license | Khác waoowaoo |
|---|---|---|
| OpenMontage (§1) | ~68k · AGPL-3.0 | Agent điều phối pipeline video, mã mở OSI |
| OpenCreator (§1b) | ~13k · Apache-2.0 | Workspace sáng tạo trên Codex CLI, mạnh về dịch/lồng tiếng |
| `HBAI-Ltd/Toonflow-app` | ~17k · MIT theo GitHub (một trang tổng hợp ghi AGPL, chưa xác minh) | Gần với waoowaoo bản cũ nhất: tiểu thuyết → kịch bản → ảnh/video phim ngắn |
| `xuanyustudio/LocalMiniDrama` | ~2k · MIT | Phim ngắn/truyện tranh động chạy offline, SQLite, hỗ trợ Ollama |

- **Muốn đúng sản phẩm "tiểu thuyết → phim ngắn"** như phần lớn bài viết mô tả: đó là v0.4.1 (CC BY-NC-SA, cấm thương mại) hoặc Toonflow/LocalMiniDrama. Bản waoowaoo hiện tại đã đổi hướng thành workspace ảnh/video chung.
- **Không nên** dùng waoowaoo làm nền cho dịch vụ bán cho khách (ELv2 cấm), cũng không nên gửi PR với hy vọng được merge.
- **Đáng mượn:** prompt cài đặt cho agent (ghim digest, hỏi trước khi tin chứng chỉ và trước khi tốn tiền), và việc tách Assistant thành container có hạn mức tài nguyên.

**Nguồn §1c:** https://github.com/waooAI/waoowaoo (clone đầy đủ, HEAD dfec20e; README.md, README_en.md, README_zh.md, bản README ở v0.4.1 `531de26`, LICENSE ở `8bc8eb3` và `41ec33d`, docs/INSTALL.md, docker-compose.yml, Dockerfile.codex-runtime, package.json) · https://github.com/saturndec/waoowaoo · https://www.waoowaoo.com/ · https://trendshift.io/repositories/22585 · https://www.sourcepulse.org/projects/25569794 · https://addrom.com/waoowaoo-ai-studio-self-hosted-ai-agent-platform-for-short-drama-and-film-video-production/ · https://skillsllm.com/skill/waoowaoo · https://gitee.com/chees_cn/waoowaoo · https://gittrend.io/repo/waooAI/waoowaoo · https://awesome.ecosyste.ms/projects/github.com%2FwaooAI%2Fwaoowaoo · https://www.elastic.co/licensing/elastic-license · https://github.com/HBAI-Ltd/Toonflow-app · https://github.com/xuanyustudio/LocalMiniDrama · https://www.sourcepulse.org/projects/23907340 · https://www.sourcepulse.org/projects/28710401

## 1d. Kiểm ảnh: topviewai/topview-3d-builder, dựng cảnh 3D cho agent trước khi sinh video (ảnh người dùng gửi, 2026-10-16)

> Ảnh là đầu README trên GitHub: logo tím, tiêu đề "Let AI build your 3D scenes", câu "From an idea, to a 3D scene built by your agent, to a real animated video. Free, runs locally, no sign-up.", bốn huy hiệu (license Apache 2.0 · python >=3.11 · node >=20.6 · runs 100% local), dải link Quick Start | Examples | Tutorial | 3D Builder | Topview.ai | Issues, và video `3D-BUILDER-hero-9MB.mp4` (1:42) cảnh hành lang với các ma-nơ-canh màu. Đã clone toàn bộ repo (69 commit, HEAD `a0671f9` 16/10/2026), đọc README, `NOTICE`, `.mcp.json`, ba manifest plugin, skill `topview-3d-cli` và các file tham chiếu, `agent/pyproject.toml`; chạy test Python; cài bản phát hành từ PyPI rồi tự dựng và render một cảnh.

### 1d.1 Hồ sơ nhanh

| Mục | Thông tin (đọc 16/10/2026) |
|---|---|
| Repo | `topviewai/topview-3d-builder` · **68★, 24 fork**, 2 PR mở, chưa có GitHub Release (tag `v0.1.3`…`v0.1.7`) · commit đầu 24/9/2026 với tên "Scene3D by TopView", công bố mã mở 15/10/2026 (X, dev.to) |
| Chủ | **Topview** (topview.ai), dịch vụ sinh video/ảnh AI trả phí theo credit. Người commit: Albert 30, 郭益雄 27, 3 người khác 4 commit mỗi người |
| Giấy phép | Mã, schema, tài liệu: **Apache-2.0**. Tài sản dựng sẵn trong `builtin-assets/` (nhân vật, tư thế, ảnh bìa): **CC BY 4.0**, phải ghi "Scene3D built-in assets © Topview, CC BY 4.0". Font editor: OFL 1.1 |
| Thành phần | CLI Python `topview-3d-cli` (PyPI, chỉ phụ thuộc `jsonschema`) điều khiển renderer Node/three.js chạy trong Chromium headless; Studio (editor web cục bộ, ~555 file); skill cho Claude Code, Codex, Cursor |
| Phạm vi bản này | 4 ma-nơ-canh (Child, Youth, Female, Man), 121 tư thế **tĩnh**, 5 khối hình cơ bản, camera tĩnh và keyframe vị trí. Skill tự ghi: **không có thư viện chuyển động**, không hứa hẹn dáng đi hay hoạt ảnh cơ thể |

### 1d.2 Kiểm từng ô trong ảnh

| Ô trong ảnh | Kiểm | Ghi chú |
|---|---|---|
| "Free, runs locally, no sign-up" | ⚠️ | Đúng với phần **dựng và render**: tự chạy bản 0.1.7, dựng cảnh hai nhân vật + camera và render một khung 640×360 trong khoảng 2 giây, không cần tài khoản; lời gọi mạng duy nhất trong CLI là tới Studio ở `localhost`. Nhưng câu này gộp cả bước "to a real animated video", mà bước đó cần một dịch vụ sinh video. Video ví dụ trong README ghi "rendered by Topview.ai" |
| license Apache 2.0 | ✅ | Đúng với mã. Tài sản dựng sẵn là CC BY 4.0, phải ghi công khi dùng |
| python >=3.11 | ✅ | `requires-python = ">=3.11"` |
| node >=20.6 | ⚠️ | README và bài dev.to ghi 20.6+, nhưng `editor/package.json` khai `engines.node >=18.0.0`. Đã chạy được với Node 24.22 |
| runs 100% local | ⚠️ | Lõi đúng, **plugin thì không**: `.mcp.json` ở gốc repo khai máy chủ MCP từ xa `https://mcp-3d.topview.ai` (OAuth). Manifest Codex trỏ thẳng tới file này, marketplace Codex đặt `"authentication": "ON_INSTALL"`. Manifest Claude không khai, nhưng Claude Code **tự nạp `.mcp.json` ở gốc plugin** (docs plugins-reference: "loads `.mcp.json` at the plugin root first"). Cài plugin vào Claude Code vì thế cũng đăng ký máy chủ `topview-3d`. Nó chỉ chạy được khi người dùng đồng ý OAuth, không âm thầm gửi dữ liệu. Bài dev.to không nhắc tới máy chủ MCP này |
| Link Quick Start · Examples · Tutorial · 3D Builder · Topview.ai · Issues | ⚠️ | Quick Start và Issues trỏ đúng chỗ. **Examples gãy**: neo `#see-what-you-can-make` không có heading tương ứng (mục gần nhất là `### Example`). 3/6 link dẫn về topview.ai (tutorial, trang sản phẩm, trang chủ) |
| Video hero 1:42 | ⚠️ | Phần dựng cảnh khớp sản phẩm; phần video thật cuối cùng do Topview sinh, không phải do công cụ mã mở này tạo |

**Tổng:** 2✅ / 5⚠️ / 0❌. Không có ô sai hẳn. Ngoài link Examples gãy, các ⚠️ có chung một gốc: ảnh gộp phần mã mở chạy cục bộ (dựng, kiểm, render khung tham chiếu) với bước sinh video trả phí của Topview.

### 1d.3 Điều ảnh không nói (đọc mã và tự chạy)

- **Bước sinh video là phễu về Topview, nhưng có thứ tự và cổng đồng ý.** `references/generate.md` buộc agent dùng trước dịch vụ người dùng đã nêu hoặc công cụ đã cài trên máy. Chỉ khi không có gì, agent mới **tự đăng ký** máy chủ MCP `https://mcp-browser.topview.ai` vào cấu hình host (với Cursor là gộp vào `~/.cursor/mcp.json` cấp người dùng, sao lưu trước, không in file), rồi để người dùng tự hoàn tất OAuth. Agent bị cấm hỏi mật khẩu, cookie hay token. Commit `58b06ab` (14/10) mới thêm việc tự kết nối này.
- **Một lần đồng ý sinh là chạy hết vòng đó.** Skill viết: sau khi người dùng cho phép một "generation round", agent upload khung tham chiếu, gửi, chờ, nhận kết quả **mà không hỏi lại**, chỉ báo dịch vụ, nội dung upload và chi phí. Sửa cảnh 3D thì phải hỏi lại cho vòng mới. Đây là một ngân sách đồng ý theo vòng; nếu dùng với credit thật, nên tự đặt trần chi phí.
- **Skill ở HEAD ghim một phiên bản chưa có trên PyPI.** Commit `24c2374` (15/10) ghim `topview-3d-cli==0.1.8` ở skill và cả ba plugin, nhưng PyPI (đọc 16/10/2026) mới tới **0.1.7** (0.1.3 cũng không có). Làm đúng bước 1 của skill (`uvx --python 3.12 topview-3d-cli@0.1.8 doctor --json`) sẽ lỗi cài đặt. Phần hướng dẫn xử lý lỗi của skill giả định lỗi do mirror cũ, không xét trường hợp bản chưa phát hành.
- **Test:** `pytest` thư mục test của CLI (cài từ mã nguồn): **214 pass, 28 skip** (cần editor đã build), **1 fail** (`test_node_batch_state_reports_primitive_sizes`, `ERR_MODULE_NOT_FOUND`). Test này cần editor đã build nhưng thiếu điều kiện skip như 28 test kia, nên là lỗi môi trường chứ không phải lỗi logic.
- **Chạy thật bản 0.1.7:** `doctor` báo đủ (Python, Node, runtime đóng gói, 4 nhân vật, 121 tư thế, 5 khối); `browser ensure` tận dụng Chromium sẵn có; `project init` → `node batch` (2 nhân vật + 1 camera) → `render` ra `frame-0.png` cùng sha256 kiểm được. Khung hình là ma-nơ-canh trên lưới, đúng mục tiêu "tham chiếu dàn cảnh", không phải ảnh thành phẩm.
- **Thiết kế đáng học:** cảnh là tệp JSON (`.topview-3d/`) sửa bằng lệnh có `expectedSceneSequence` (khoá lạc quan, lệnh dựa trên trạng thái cũ thì bị từ chối); `node batch --dry-run` và `evaluate` kiểm số (chạm đất, va chạm, khoảng cách, khung hình) **trước** khi render; mỗi lần render ghi `documentSha256` và đánh dấu bản render cũ là `stale`. Đây là cùng ý "kiểm bằng máy trước khi tiêu credit" mà OpenMontage (§1) làm ở mức pipeline.

### 1d.4 So sánh & dùng thế nào

| Dự án (shields 16/10/2026) | ★ · license | Khác topview-3d-builder |
|---|---|---|
| `ahujasid/blender-mcp` | ~31k · MIT | Agent điều khiển Blender đầy đủ qua MCP: mạnh hơn nhiều về mô hình, vật liệu, hoạt ảnh, nhưng phải cài Blender. Repo của chủ kho `design-os-3d-blender` dùng hướng này (mục 23 §6.1; mục 14) |
| `earthtojake/text-to-cad` | ~21k · MIT | Cùng mẫu "plugin cho coding agent + CLI + viewer cục bộ", nhưng cho CAD cơ khí (mục 20 §3e) |
| Higgsfield 3D Jutsu, Spline AI Agent, Topview 3D Builder bản web | dịch vụ trả phí | Prompt → cảnh 3D chỉnh được → video, chạy trên cloud; bản web của Topview tính phí mỗi lần dựng cảnh (trang Topview, chưa xác minh giá) |
| `topviewai/skill` | ~40 · Apache-2.0 | Skill khác của cùng hãng, gọi dịch vụ Topview qua MCP để sinh media; không phải công cụ cục bộ |

- **Dùng được ngay cho:** dựng phân cảnh tham chiếu (vị trí nhân vật, hướng nhìn, góc máy, chuyển động camera) rồi đưa khung hình vào **bất kỳ** model video nào có nhận ảnh tham chiếu. Phần này mã mở thật và chạy cục bộ.
- **Trước khi cài plugin:** hiểu rằng plugin đăng ký sẵn một máy chủ MCP từ xa của Topview. Nếu chỉ cần phần cục bộ, cài CLI từ PyPI (`pip install topview-3d-cli==0.1.7`, bản đã kiểm ở đây) và chép riêng skill, bỏ `.mcp.json`. Ghim phiên bản có thật trên PyPI.
- **Không trông đợi** hoạt ảnh nhân vật: bản này chỉ có tư thế tĩnh và keyframe vị trí. "Real animated video" là việc của model video phía sau.
- **Rủi ro dự án:** repo 3 tuần tuổi, 68★, do một công ty có sản phẩm trả phí phát triển; phần cục bộ có lợi ích thật nhưng vai trò chính là kênh dẫn tới dịch vụ sinh video của Topview.

**Nguồn §1d:** https://github.com/topviewai/topview-3d-builder (clone đầy đủ, HEAD a0671f9; README.md, NOTICE, LICENSE, builtin-assets/LICENSE, .mcp.json, .claude-plugin/{plugin,marketplace}.json, .codex-plugin/plugin.json, .agents/plugins/marketplace.json, skills/topview-3d-cli/SKILL.md, references/{generate,doctor-browser,camera,checks,add-character}.md, agent/pyproject.toml, agent/topview_3d_cli/local_studio.py, editor/package.json) · https://pypi.org/pypi/topview-3d-cli/json (đọc 16/10/2026: bản mới nhất 0.1.7) · https://code.claude.com/docs/en/plugins-reference (`.mcp.json` ở gốc plugin được nạp trước) · https://dev.to/topviewai/from-one-prompt-to-an-editable-3d-scene-we-open-sourced-a-local-first-agent-workflow-npa (15/10/2026) · https://x.com/TopviewAIhq/status/2110615678805774657 · https://www.topview.ai/3d-builder · https://github.com/topviewai/skill · https://github.com/ahujasid/blender-mcp · https://github.com/earthtojake/text-to-cad · https://docs.spline.design/spline-ai/ai-agent · https://higgsfield.ai/blog/higgsfield-3d-jutsu

## 1e. Kiểm bài "10 kho mã nguồn cực kỳ mạnh mẽ mà bạn không nên bỏ qua" (bài người dùng gửi, 2026-10-19)

> Bài liệt kê 10 repo cho quy trình sáng tạo nội dung: kịch bản → ảnh → giọng → nhạc → dựng video → Shorts → podcast → đăng bài. Đã clone cả 10 (blob:none, đủ lịch sử), đọc README/LICENSE/package.json, lấy số sao + license qua shields ngày 19/10/2026. Link mục 2 trong bài bị cắt ("ScrapeCre…"); repo đúng là `ScrapeCreators/social-media-research-skills`.

### 1e.1 Bảng kiểm

| # | Repo | ★ · license (19/10/2026) | Commit cuối · số commit | Kiểm | Điều bài không nói |
|---|---|---|---|---|---|
| 1 | `krillinai/OpenCreator` | ~14k · Apache-2.0 | 19/10/2026 · 983 | ✅ | Đã có hồ sơ §1b: dùng Codex CLI làm động cơ; tài khoản, tín dụng và "official model service" là dịch vụ trả phí |
| 2 | `ScrapeCreators/social-media-research-skills` | ~4,2k · MIT | **26/8/2026 · 7** | ⚠️ | **Bắt buộc `SCRAPECREATORS_API_KEY`** (dịch vụ thu thập dữ liệu trả phí của chính tác giả); 13 skill là lớp prompt trên API đó. Chỉ 7 commit |
| 3 | `LearningCircuit/local-deep-research` | ~9,3k · MIT | 19/10/2026 · **8.382** · v1.10.7 | ✅ | Web + tài liệu cá nhân, model local và cloud đúng như bài. Có CodeQL, Semgrep, OpenSSF Scorecard. Huy hiệu "SimpleQA ~95%" là **tự đo** trên dataset của dự án |
| 4 | `black-forest-labs/flux2` | ~2,8k · Apache-2.0 (mã) | **12/3/2026 · 12** | ✅ có lưu ý | Đúng: **Klein 4B và 4B Base** trọng số Apache-2.0, ~8 GB VRAM. Nhưng **Klein 9B, 9B KV, 9B Base và FLUX.2 [dev] dùng FLUX Non-Commercial License** → làm thumbnail/quảng cáo thương mại chỉ được với bản 4B. Repo là mã inference, ít commit |
| 5 | `hexgrad/kokoro` | ~9,5k · Apache-2.0 | **6/8/2025 · 71** | ✅ | 82M tham số, trọng số Apache. Thư viện đã **14 tháng không commit**; không clone giọng (mục 14) |
| 6 | `ace-step/ACE-Step-1.5` | ~14k · MIT (mã) | 29/8/2026 · 1.410 · v0.1.8 | ✅ | Chạy local < 4 GB VRAM theo README (bản XL 4B cần ≥ 12 GB). "Chất lượng giữa Suno v4.5 và v5" là **tự nhận**. License trọng số trên Hugging Face **(chưa xác minh)** |
| 7 | `YILS-LIN/short-video-factory` | ~5,8k · **AGPL-3.0** | 16/10/2026 · 145 · v1.3.0 | ⚠️ | **AGPL-3.0**: nhúng vào dịch vụ phải mở mã. App **Electron 22** (hết hỗ trợ từ 2/2024). TTS chỉ có **EdgeTTS** (gọi dịch vụ đọc online của Microsoft Edge qua thư viện không chính thức); LLM qua API tương thích OpenAI. README tiếng Trung |
| 8 | `Anil-matcha/AI-Youtube-Shorts-Generator` | ~5,5k · MIT | 11/10/2026 · 29 | ⚠️ | Chế độ mặc định `--mode api` dùng **MuAPI** (dịch vụ trả phí theo clip, README quảng bá nhiều lần). `--mode local` chạy được bằng yt-dlp + faster-whisper + OpenCV, nhưng **vẫn cần API key OpenAI hoặc Gemini** cho bước chọn đoạn |
| 9 | `souzatharsis/podcastfy` | ~6,7k · Apache-2.0 | **4/5/2026** · 399 · v0.4.0 | ✅ | 100+ LLM (có local), TTS OpenAI/Google/ElevenLabs/Edge. Đã 5 tháng không commit |
| 10 | `langchain-ai/social-media-agent` | ~2,9k · MIT | 19/10/2026 · 1.058 | ✅ có lưu ý | URL → nháp X/LinkedIn, có duyệt (HITL) và lên lịch đúng như bài. Cần **Anthropic API + LangSmith + FireCrawl + Arcade** (Arcade lo đăng nhập và đăng bài), tùy chọn Supabase/Slack. Là ví dụ tham chiếu của LangGraph, không phải sản phẩm |

**Tổng:** 7✅ / 3⚠️ / 0❌. Mọi repo đều tồn tại và làm đúng việc bài mô tả. Điểm bài bỏ qua là **chi phí và ràng buộc**: 4/10 repo cần dịch vụ trả phí hoặc API key bên thứ ba để chạy được (mục 2, 8, 10, và OpenCreator ở mức tài khoản), 1 repo AGPL, và 4/6 biến thể FLUX.2 là non-commercial.

### 1e.2 Ghép thành quy trình, và chọn bản nào

| Bước | Lựa chọn trong bài | Mở hoàn toàn / chạy local? | So với kho |
|---|---|---|---|
| Nghiên cứu chủ đề | Local Deep Research | ✅ (local model + SearXNG) | Repo trưởng thành nhất trong danh sách |
| Nghiên cứu mạng xã hội | Social Media Research Skills | ❌ cần API ScrapeCreators | Chỉ là skill trên API trả phí |
| Ảnh | FLUX.2 [klein] 4B | ✅ (Apache, ~8 GB VRAM) | Chạy qua ComfyUI (mục 14) tiện hơn dùng repo inference trực tiếp |
| Giọng | Kokoro | ✅ (Apache, CPU được) | Không clone giọng; cần giọng riêng thì xem mục 14 (Chatterbox, Fish Audio) và mục 18 (TTS tiếng Việt) |
| Nhạc | ACE-Step 1.5 | ✅ (MIT mã; trọng số chưa xác minh) | |
| Dựng video ngắn | Short Video Factory | ⚠️ AGPL, Electron cũ, EdgeTTS | OpenMontage (§1) và các skill motion (mục 22) hợp hơn nếu dựng bằng agent |
| Cắt Shorts từ video dài | AI YouTube Shorts Generator | ⚠️ local mode vẫn cần LLM API | |
| Podcast | Podcastfy | ✅ nếu chọn LLM local + Edge/OpenAI TTS | |
| Đăng bài | Social Media Agent | ❌ cần 4 dịch vụ ngoài | Mẫu học cách làm HITL với LangGraph (mục 02, 21) |

**Dùng thế nào:** một quy trình **chạy local toàn bộ và dùng thương mại được** gồm Local Deep Research + FLUX.2 Klein 4B + Kokoro + ACE-Step 1.5 (kiểm license trọng số trước) + Podcastfy với LLM local. Các mục còn lại hoặc gắn với dịch vụ trả phí của tác giả (2, 8), hoặc cần nhiều API bên ngoài (10), hoặc có ràng buộc license/bảo trì (7). Trước khi nhúng vào sản phẩm: đọc license trọng số trên Hugging Face (FLUX.2, ACE-Step), và tránh AGPL nếu không muốn mở mã.

### 1e.3 Bản infographic "Nhà máy nội dung AI" (người dùng gửi, 2026-10-20)

Ảnh dạng cây thư mục VS Code (`ai-content-factory.md`) liệt kê **đúng 10 repo của §1e**, chia 6 nhóm: 01 Nghiên cứu & ý tưởng (Social Media Research Skills, Local Deep Research) · 02 Không gian sáng tạo (OpenCreator) · 03 Hình ảnh (FLUX.2) · 04 Giọng đọc & âm nhạc (Kokoro, ACE-Step 1.5) · 05 Video & podcast (Short Video Factory, AI YouTube Shorts Generator, Podcastfy) · 06 Phân phối nội dung (Social Media Agent). Mô tả từng dòng khớp bảng 1e.1; ảnh ghi đủ tên `ScrapeCreators/social-media-research-skills` (bài gốc bị cắt link).

- **Kiểm lại 20/10/2026:** số sao, license và release không đổi so với 1e.1 (shields: Social Media Research Skills ~4,3k, Local Deep Research ~9,4k, còn lại như cũ). Short Video Factory có thêm commit `a9516c1` (19/10, bỏ đường lùi phụ đề FFmpeg, dùng engine phụ đề riêng) nhưng vẫn v1.3.0, AGPL-3.0, `electron ^22.3.27`.
- **Điều ảnh vẫn không nói:** dòng cuối có nhắc "chọn theo nhu cầu, phần cứng & ngân sách", nhưng không ghi repo nào cần dịch vụ trả phí hay license nào hạn chế. Các lưu ý ⚠️ ở 1e.1 và bộ chạy local ở 1e.2 vẫn giữ nguyên.

**Nguồn §1e:** clone 19/10/2026 (blob:none, đủ lịch sử; README.md, LICENSE, package.json): github.com/{krillinai/OpenCreator, ScrapeCreators/social-media-research-skills, LearningCircuit/local-deep-research, black-forest-labs/flux2 (bảng model + model_licenses/LICENSE-FLUX-NON-COMMERICAL), hexgrad/kokoro, ace-step/ACE-Step-1.5, YILS-LIN/short-video-factory (package.json electron ^22.3.27), Anil-matcha/AI-Youtube-Shorts-Generator, souzatharsis/podcastfy, langchain-ai/social-media-agent} · img.shields.io/github/{stars,license}/… 19/10/2026 · skillselion.com/marketplace/ScrapeCreators/social-media-research-skills · skills-hub.ai/sources/social-media-research-skills · bfl.ai/blog/flux2-klein-towards-interactive-visual-intelligence · huggingface.co/hexgrad/Kokoro-82M · huggingface.co/ACE-Step/Ace-Step1.5

## 1f. Kiểm bài "Tự làm video AI xây kênh, chỉ cần 1 tài khoản AI": bộ 4 repo của CuongIT (ảnh người dùng gửi, 2026-10-21)

> Bài Facebook của CuongIT (GitHub `Cuongyd196`, 105 follower) giới thiệu "3 repo GitHub đã có sẵn các skill + ứng dụng CIT Voice Studio". Theo bài, người dùng chỉ cần thêm một gói AI (ChatGPT Plus, Claude Pro hoặc Google AI Pro) và một agent desktop (Codex, Claude Code hoặc Antigravity), rồi mở thư mục repo và làm theo README. Đã clone đủ lịch sử cả 4 repo, đọc README, SKILL.md, package.json, mã TTS và LICENSE, đọc số sao/fork qua shields ngày 21/10/2026. **Không cài và không chạy script nào của các repo.**

### 1f.1 Hồ sơ nhanh

| Repo | ★ · fork (21/10/2026) | Commit · thời gian | Engine | License thật | Kiểm |
|---|---|---|---|---|---|
| `Cuongyd196/auto-compare-video` | 220 · 125 | 21 · 24/7 → 24/9/2026 | HyperFrames 0.7.58 (ghim) + GSAP | MIT (có file) | ⚠️ |
| `Cuongyd196/remotion-cuongit-template` | 208 · 123 | 14 · 22/1 → 16/10/2026 | Remotion 4.0.407 (ghim) | **Không có file LICENSE**. Badge ghi MIT, `package.json` ghi `UNLICENSED` | ❌ license |
| `Cuongyd196/auto-video-gen` | 184 · 112 | 11 · 13/7 → 28/9/2026 | HyperFrames ^0.4.34 | MIT, nhưng là bản sao `hoquanghai/Auto-Create-Video` và file LICENSE đã thay tên tác giả gốc | ⚠️ |
| `Cuongyd196/cit-voice-studio` | 119 · 48 | 35 · 23/9 → 3/10/2026, tag 1.0.0–1.0.3 | App đóng mã (PyInstaller, FastAPI, ONNX Runtime) chạy VieNeu-TTS v3 Turbo | README ghi Apache-2.0, nhưng repo **không có mã nguồn và không có file LICENSE** | ⚠️ |

Số sao trong ảnh (215/206/181/112) lệch nhẹ so với bảng vì ảnh chụp sớm hơn.

**Điểm chung của 3 repo video:**

- Mỗi repo là **template kèm một skill**: `create-video`, `remotion-topic-explainer`, `create-news-video`.
- Skill được chép thành hai bản: `.claude/skills/` cho Claude Code và `.agents/skills/` cho Antigravity (Codex cũng đọc được `.agents/skills`). Không có bản riêng cho Gemini.
- Kịch bản do **chính agent viết**, trong mã không có lệnh gọi LLM API nào. Vế "chỉ cần 1 tài khoản AI" vì vậy là đúng.
- Không repo nào có CI. Chỉ auto-video-gen có test (60 case vitest, thừa hưởng từ bản gốc).
- Tất cả do một tác giả làm, dưới vài danh tính git; mỗi repo có 0–3 commit mang trailer Claude.

### 1f.2 Điều bài không nói (đọc mã)

#### auto-compare-video: video "A vs B" khoảng 20 giây, hai nhân vật robot

**Luồng chạy:**

1. Agent viết 8 câu thoại.
2. `generate-vo.mjs` gọi TTS cho từng câu, đo độ dài bằng `ffprobe` rồi ghi `durations.json`.
3. Agent **chép tay** các số đo vào đối tượng `VO` và các thẻ `<audio>` trong `index.html`.
4. `hyperframes render` xuất video. Lúc render không bước nào đọc `durations.json`.

**Lỗi lệch tiếng đã xảy ra trong repo:**

- Video mẫu `thien-thach-vs-sao-bang` được tạo lại giọng bằng Edge TTS ở commit `1dbc29d`.
- Clip mới dài 1,8–3,0 giây mỗi câu, tổng khoảng 20 giây.
- `index.html` vẫn giữ số đo Vbee cũ (1,0–2,0 giây, comment còn ghi "Real Vbee"), nên phụ đề và nhân vật chạy lệch với tiếng.
- Miệng robot chỉ lắc theo nhịp cố định 0,22 giây chứ không bám âm thanh.

**Không có bước kiểm chứng nội dung.** Agent tự viết phần so sánh, và README/skill không yêu cầu ghi nguồn. Khi bật `AUTO_CREATE_VIDEO=1`, quy trình đi thẳng từ chọn chủ đề đến chốt kịch bản mà không dừng cho người duyệt. Với kênh "chia sẻ kiến thức", đây là rủi ro lớn nhất của repo.

**Lặt vặt:**

- `package.json` của mỗi video có script `prepublish`, mà npm vẫn chạy khi `npm install` cục bộ. Script này gọi `sync-channel.mjs` để sửa `index.html` theo `.env`.
- `npx --yes` tự tải HyperFrames mà không hỏi.
- README dùng link affiliate Vbee.
- README nói font Be Vietnam Pro được nhúng sẵn, thực tế font này và GSAP được tải từ Google Fonts/jsDelivr lúc render.
- Provider mặc định không khớp giữa các nơi: `.env.example` ghi `edge`, README tiếng Anh ghi `vieneu`, skill ghi code lùi về `vbee` nhưng code thật lùi về `vieneu`.

#### remotion-cuongit-template: video giải thích 9:16 dài 40–60 giây

**Phần agent viết và phần dùng lại được:**

- Agent viết gần như mọi thứ: kịch bản, script sinh audio, toàn bộ thư mục `src/<Topic>/` và chỗ sửa trong `Root.tsx`.
- Phần dùng lại thật chỉ có:
  - `scripts/generate-tts.ts`: gọi Edge TTS hoặc CIT Voice Studio, đo độ dài từ header MP3/WAV, ghi `manifest.json`;
  - hai component `BrandHeader` và `SubtitleBox`.
- Phụ đề được chia đều 6 từ một khúc theo thời lượng cảnh, không có timestamp từng từ.

**License:**

- Repo không có file LICENSE, nên về pháp lý mọi quyền vẫn thuộc tác giả. Badge MIT không có giá trị, và `package.json` còn ghi `UNLICENSED`.
- README có nhắc Remotion "cần company license trong một số trường hợp" nhưng không nói ngưỡng: Remotion miễn phí cho cá nhân và công ty tối đa 3 người, công ty lớn hơn phải mua license (mục 22 §2.2).

**Font Segoe UI bị commit vào repo:** hai file `public/fonts/SegoeUI-{Regular,Bold}.ttf` (bản 5.65).

- Bảng name của font ghi "© 2022 Microsoft Corporation… Microsoft supplied font": chỉ được dùng theo điều khoản của sản phẩm Microsoft đi kèm, nên **không được phân phối lại**.
- Trước khi dùng, thay bằng một font OFL như Be Vietnam Pro hoặc Inter.

**Lặt vặt:**

- Ba file manifest lộ đường dẫn trên máy tác giả (`D:\cuongit\...`).
- `DockerExplainer` hard-code tên kênh "CƯỜNG IT" và `durationInFrames=1280`, trái với chính skill của repo.

#### auto-video-gen: URL tin tức hoặc GitHub → video 9:16

**Là bản sao của `hoquanghai/Auto-Create-Video`** (322★, MIT, 34 commit từ 29/4 đến 2/5/2026, có CI test và typecheck):

- 54/64 file trùng đường dẫn và 31 file giống hệt từng byte, kể cả `docs/superpowers/` ghi ngày 2026-04-29.
- Lịch sử mở đầu bằng commit `#Init` ngày 13/7/2026, không giữ commit gốc.
- README có ghi rõ đây là "bản fork… toàn bộ công sức thiết kế pipeline gốc thuộc về tác giả gốc".
- Nhưng file `LICENSE` đã đổi dòng copyright từ "Ho Quang Hai" thành "CuongIT". MIT yêu cầu giữ nguyên thông báo bản quyền gốc, nên đúng ra phải **thêm** dòng mới chứ không thay.
- Phần bổ sung thật của bản này: provider Vbee, hai theme `dark-neon`/`light-pro`, kiến trúc TTS dạng module kèm Edge TTS.

**Nội dung và bản quyền:**

- Agent tự lấy bài bằng WebFetch, viết `script.json` (schema Zod, tối đa 8 cảnh) rồi chạy pipeline.
- Code tải **og:image của bài báo** làm nền video, tức dùng lại ảnh có bản quyền của báo. Repo không có lời nhắc bản quyền nào.

**README lệch so với code:**

- "5 phút" chỉ là một câu trong README; bản gốc ghi "60 giây" ở tiêu đề và "~5 phút" ở bảng so sánh.
- Thư viện SFX không có sẵn trong repo: phải chạy `sfx:download` (cào myinstants.com) rồi `sfx:filter`.
- README ghi "SFX/BGM" nhưng pipeline không có BGM.
- Danh sách template, đường dẫn output và con số 60 FPS trong README không khớp code. Thực tế có 6 loại cảnh (`hook`, `comparison`, `stat-hero`, `feature-list`, `callout`, `outro`), render 30 fps, file ra là `video.mp4`.

**Đã kiểm `.claude/settings.json` đi kèm repo:** file chỉ cho phép sẵn vài lệnh đọc (curl GitHub API, `gh repo view`), là dấu vết phiên làm việc của tác giả. Không nguy hiểm.

#### cit-voice-studio: app TTS tiếng Việt

**Repo không có mã nguồn.** Toàn bộ repo là 5 file tài liệu (README, PRIVACY, DIEU-KHOAN, THIRD-PARTY-NOTICES và một ảnh), và README tự nói mã nguồn không công khai, chỉ phát hành bộ cài. Mọi điều dưới đây vì vậy là lời tác giả, **không kiểm được bằng mã**.

**Bộ cài:** bản v1.0.3 gồm .exe cho Windows (~363 MB), .deb (~463 MB) và .dmg (~427–447 MB), kèm mirror Google Drive.

**Công nghệ và model (theo file notices):**

- Python đóng gói bằng PyInstaller, chạy FastAPI/Uvicorn và ONNX Runtime; giao diện React hiển thị trong pywebview.
- Model mặc định là **VieNeu-TTS v3 Turbo** (ONNX int8) cùng MOSS Audio Tokenizer Nano, cả hai đều Apache-2.0 theo notices.
- Tùy chọn Supertonic 3 cho 31 ngôn ngữ khác, giấy phép OpenRAIL-M có điều khoản hạn chế sử dụng.
- ASR Zipformer tiếng Việt dùng để kiểm câu đồng ý khi clone giọng.
- Không có trọng số non-commercial (như F5-TTS-Vietnamese, viXTTS), nên theo lời README thì dùng thương mại được.

**Clone giọng có cổng đồng ý:**

- Người dùng phải ghi âm trực tiếp câu cam kết khoảng 8 giây; app không clone từ file có sẵn.
- Có điều khoản cấm mạo danh, và file xuất ra mang metadata "AI-generated".
- Đây là thiết kế đáng học (mục 14).

**API HTTP ở `127.0.0.1:8001`** (`/api/tts/generate`, `/stream`, `/voices`…): đây là cổng 3 repo video gọi tới qua provider `vieneu`/`cit`.

- Ở chế độ localhost, API **không xác thực**, nên mọi tiến trình trên máy đều gọi được.
- Chế độ LAN dùng header `X-API-Key` trên HTTP thường, không mã hóa.

**Bộ cài không ký số và không công bố checksum.** Đây là điểm đáng ngại nhất trong cả bộ, vì README hướng dẫn:

- bỏ qua cảnh báo SmartScreen;
- chạy `xattr -dr com.apple.quarantine` trên macOS;
- tắt Smart App Control của Windows 11, dù tự thừa nhận có thể không bật lại được.

**README mâu thuẫn với chính tài liệu của nó:**

- README nói "không cần Internet sau khi cài", nhưng lần clone giọng đầu tiên tải ASR ~77 MB, các bản FP32/Nano/Supertonic/GPU phải tải thêm, và bật GPU kéo gói PyPI/PyTorch không ghim phiên bản.
- README ghi Apache-2.0 cho một binary đóng mã mà repo không có file LICENSE hay NOTICE.

### 1f.3 Bài nói đúng gì, thiếu gì

| Claim của bài | Thực tế |
|---|---|
| "3 repo đã có sẵn các skill" | ✅ Mỗi repo có một skill, chép thành hai bản (Claude Code và Antigravity/Codex). Không có bản riêng cho Gemini |
| "chỉ cần 1 tài khoản AI" | ✅ cho phần viết kịch bản. ⚠️ cho phần giọng: Edge TTS miễn phí nhưng là dịch vụ đọc online không chính thức của Microsoft, văn bản bị gửi lên Microsoft, và thư viện `edge-tts-universal` dùng giấy phép **AGPL-3.0** (cả 3 repo đều kéo). Vbee, ElevenLabs và LucyLab trả phí. CIT Voice Studio cần máy 8–16 GB RAM |
| "chia sẻ miễn phí" | ⚠️ Miễn phí để dùng, nhưng: 1 repo không có license (về pháp lý không được phép tái sử dụng), 1 repo commit font Microsoft, 1 repo là bản sao đã đổi copyright, còn app giọng đóng mã |
| "mở thư mục bằng công cụ AI rồi làm theo readme.md" | ✅ Cách dùng này đúng. Nhưng README lệch code ở nhiều chỗ (template, fps, đường dẫn, provider mặc định), nên agent đọc skill và code sẽ chính xác hơn đọc README |
| (không nói) license Remotion | Công ty trên 3 người phải mua license Remotion |
| (không nói) kiểm chứng nội dung | Không repo nào có bước kiểm nguồn hay fact-check, và auto-video-gen dùng lại ảnh của báo |

**Tổng:** cả 4 repo tồn tại và làm đúng việc mô tả, ở mức "template + skill cho agent". Bộ này hợp để **học cách đóng gói quy trình làm video thành skill**, chưa hợp để nhúng nguyên vào sản phẩm hay kênh thương mại.

### 1f.4 Dùng thế nào

**Bài học cấu trúc:** tách phần "agent viết nội dung" khỏi phần "script tất định đo, ghép và render". Đây cũng là mẫu của OpenMontage (§1) và của skill HyperFrames (mục 22). Lỗi lệch tiếng của auto-compare-video cho thấy: **để code đọc `durations.json` lúc dựng**, đừng để agent chép số bằng tay (cùng tinh thần "cổng máy" ở mục 23).

**Nếu dùng từng repo:**

- **auto-video-gen:**
  - Dùng thẳng bản gốc `hoquanghai/Auto-Create-Video` (có CI); chỉ chọn bản của CuongIT khi cần Vbee hoặc hai theme mới.
  - Sửa `LICENSE` để giữ cả hai dòng copyright.
  - Bỏ nền og:image, hoặc chỉ dùng ảnh mình có quyền.
- **remotion-cuongit-template:**
  - Chờ tác giả thêm LICENSE hoặc xin phép trước khi tái sử dụng.
  - Xóa font Segoe UI.
  - Mua license Remotion nếu công ty trên 3 người.
  - Hoặc dựng lại từ `remotion-dev/skills` (mục 22 §2.3).
- **auto-compare-video:**
  - Thêm bước ghi nguồn tham khảo và người duyệt trước khi render.
  - Sửa lại thời gian trong video mẫu.
- **Giọng đọc:**
  - Cần mã mở thì dùng thẳng `pnnbao97/VieNeu-TTS` (Apache-2.0, mục 18) thay cho CIT Voice Studio.
  - Nếu dùng app, tải từ GitHub Releases (không dùng mirror Drive), đừng tắt Smart App Control cho toàn máy, và giữ API ở localhost.

**Thay thế cùng loại:** OpenMontage (§1), Short Video Factory (§1e, AGPL), workflow `/faceless-explainer` của HyperFrames (mục 22), MoneyPrinterTurbo (§3).

**Nguồn §1f:** clone đủ lịch sử 21/10/2026: github.com/Cuongyd196/auto-compare-video (HEAD 50b1f34; CLAUDE.md, AGENTS.md, `.claude/skills/create-video/`, `videos/*/{package.json,index.html,generate-vo.mjs,assets/vo/durations.json}`, commit 1dbc29d, LICENSE) · github.com/Cuongyd196/remotion-cuongit-template (HEAD 3af5eac; package.json, src/Root.tsx, scripts/generate-tts.ts, public/fonts/SegoeUI-*.ttf (đọc bảng name), `.claude/skills/remotion-topic-explainer/`, docs/cit-voice-studio.md) · github.com/Cuongyd196/auto-video-gen (HEAD 86cda98; README.md, README.full.md, README.en.md, LICENSE, package.json, package-lock.json (`edge-tts-universal` 1.4.0 AGPL-3.0), src/pipeline.ts, src/render/script-schema.ts, `.claude/settings.json`, `.claude/skills/create-news-video/`) · github.com/Cuongyd196/cit-voice-studio (HEAD 0b0b995; README.md, PRIVACY.md, DIEU-KHOAN.md, THIRD-PARTY-NOTICES.md) · github.com/hoquanghai/Auto-Create-Video (clone 21/10/2026, 34 commit, so sánh từng file với auto-video-gen) · img.shields.io/github/{stars,forks,license,followers}/… 21/10/2026 · github.com/Cuongyd196 (profile "CuongIT") · github.com/vu05051995/auto-compare-video (fork, 0★) · github.com/dongphuongman/hyframe-video, github.com/ptit9x/auto-generate-short-videos (biến thể cùng họ, 0★) · remotion.pro/license

## 2. Làn sóng "video / motion skills" cho Claude Code (trendshift topic ai-video, 10/2026)

| Repo | Số hiển thị (★?) | Ghi chú |
|---|---|---|
| zhuyansen/awesome-claude-video-skills | ~55k **(sai — thực tế 1.359★ ngày 31/10/2026, GitHub API)** | Danh sách skill video cho Claude |
| allenv0/SCM | ~47k **(sai — 516★ ngày 31/10)** | |
| howseen-ai/claude-motion-design | ~45k **(sai — thực tế 450★ ngày 12/10, xem mục 22)** | Motion design bằng skill; Playwright + ffmpeg |
| guanmo-ai/awesome-ai-motion · gongnyang/awesome-ai-motion | ~30k · ~10.5k **(sai — 479 · 297★ ngày 31/10)** | |
| joeseesun/opus-video-prompts · zhuyansen/awesome-opus-5.5-video | ~27.5k · ~15.6k **(sai — 866 · 284★ ngày 31/10)** | Prompt video cho Claude Opus |
| adunext/adu-motion-video · unclejobs-ai/motion-video-skill | ~24k · ~11.6k **(sai — 655 · 131★ ngày 31/10)** | |
| FavioVazquez/showtime · Remocn/remocn-studio | ~23k · ~16k **(sai — 310 · 211★ ngày 31/10)** | |
| ferndesk/no-slop-motion | ~0.9k **(thực tế 92★ ngày 31/10)** | Chống "motion slop" (so với Taste Skill, mục 06) |

**Đính chính 31/10/2026:** đọc lại cả 12 repo trong bảng bằng GitHub search API: **mọi số ★ ở cột giữa đều sai, phóng đại 10–90 lần** (tổng thật ≈5,9k★ so với ≈306k ghi trong bảng). Số đúng ghi trong ngoặc; chi tiết ở §3b.

**Nhận định:** số liệu chỉ từ một trang aggregator và tăng rất nhanh → cần xác minh từng repo (đã kiểm: claude-motion-design thực tế 450★, tức bảng này có thể lệch ~100 lần — **không dùng các số ★ ở bảng này**; 16 repo motion/video đã xác minh ở mục 22); nhưng xu hướng rõ: *video/motion được đóng gói thành skill cho coding agent* thay vì app riêng. OpenMontage là bản "full pipeline" của xu hướng này.

## 3. Model & công cụ video mở liên quan

| Dự án | ★ (ước lượng) | Ghi chú |
|---|---|---|
| Remotion | 63,4k (12/10/2026) | Video bằng React; engine compose của OpenMontage (license riêng cho công ty ≥4 người; chi tiết mục 22) |
| Open-Sora 2.0 | ~24k | Nhiều sao nhất nhóm model; 11B |
| CogVideoX-1.5 | ~12.5k | Apache-2.0, 16GB VRAM |
| HunyuanVideo (Tencent) | ~11.9k | 60–80GB VRAM, license cộng đồng |
| Wan 2.1/2.2 | – | Model text/image-to-video mở; OpenMontage bundle workflow ComfyUI |
| OpenShorts, MoneyPrinterTurbo, ShortGPT | – | Tự động hóa video ngắn |
| codebase-video (plugin Claude Code) | – | Biến codebase thành video thuyết minh, agent khác verify claim |
| vimax-agnes | – | Pipeline idea → story → scene → video, free tier |
| FRAMEWORKERS (arXiv 2608.29814), *Agentic Artifact Creation* (2608.28122) | – | Nghiên cứu multi-agent cho sản xuất video |
| LTX-2 (Lightricks), Wan 2.2 | – | X-Studio chọn cho "xưởng video" (mục 23 §3.2): render cache SHA-256, MotionSpec, `qc.py` kiểm LUFS/độ dài/khung; nghiên cứu `RESEARCH-VIDEO-FACTORIES.md` so sánh video factory mở |
| codebase-video, vimax-agnes, MoneyPrinterTurbo | – | Xem thêm "video factory" trong X-Studio docs |

## 3b. Nâng cấp 31/10/2026: rà repo lớn

> Hai việc. (1) Đọc lại số sao, license, ngày push của **22 repo** mục 19 đã có trong catalog (GitHub API 31/10/2026) và 12 repo trong bảng §2. (2) Tìm repo lớn còn thiếu: 10 truy vấn GitHub search (`video agent`, `short video`, `video editing ai`, `podcast ai`, `comfyui video`, topic `ai-video`, `video-generation`, repo tạo sau 1/10/2025…). Từ ~110 ứng viên chưa có trong kho, chọn **6 repo** gần nhất với "agent sản xuất video", clone `--filter=blob:none` và đọc file thật (LICENSE, manifest, SKILL, script, CI, grep telemetry và host mạng). Repo kiểu "video bằng code" (HTML/Remotion) đưa sang mục 22 §9e. **Không cài, không chạy script nào.** Số sao đọc 31/10/2026.

### 3b.1 Repo cũ: điều đã đổi

| Repo | Thay đổi (đến 31/10/2026) | Hệ quả |
|---|---|---|
| `zhuyansen/awesome-claude-video-skills` | Catalog cũ ghi **55k★: sai**, thực tế **1.359★** (tạo 27/9/2026) | Đã sửa bảng §2. Số gốc lấy từ aggregator, đúng loại lỗi WORKFLOW đã cảnh báo |
| 11 repo còn lại của bảng §2 | Thực tế 92–866★, bảng ghi 0,9k–47k | Bảng §2 chỉ còn giá trị làm danh sách tên; mọi số ★ cũ đã gạch |
| `hpcaitech/Open-Sora` | ★ ~24k → **29,9k**, nhưng push cuối **9/4/2026** | Gần 7 tháng không commit; coi là model tham khảo, không phải dự án đang chạy |
| `zai-org/CogVideo` | 13,2k★, push cuối **4/11/2025** | Gần 1 năm đứng yên; Wan 2.2 (`Wan-Video/Wan2.2`, 18,3k★, Apache-2.0, push 21/9/2026) là lựa chọn mở mới hơn **(chưa thêm vào catalog)** |
| `remotion-dev/remotion` (§3) | 63,4k (12/10) → **69,4k** | Không đổi license (GitHub báo NOASSERTION vì license riêng) |
| `Tencent-Hunyuan/HunyuanVideo` | ~11,9k → **12,7k**; GitHub báo NOASSERTION | Vẫn là "Tencent Community License", giữ nguyên ghi chú |
| `calesthio/OpenMontage` (§1) | **73,9k★**, push 28/10/2026 | Vẫn hoạt động; hồ sơ §1 giữ nguyên |
| `calesthio/Crucix` | 12,2k★, push cuối 20/5/2026 | 5 tháng đứng yên |
| `souzatharsis/podcastfy` | 6,8k★, push cuối 4/5/2026 | Gần 6 tháng đứng yên |

Không repo nào của mục 19 bị archive. `MoneyPrinterTurbo` được nhắc ở §3 từ trước nhưng chưa có trong catalog; nay thêm (bảng dưới).

### 3b.2 Bảng nhanh 6 repo mới

| Repo | Nhóm | ★ · license | Commit cuối | Một dòng | Cờ |
|---|---|---|---|---|---|
| `harry0703/MoneyPrinterTurbo` | Pipeline video ngắn | 136,9k · MIT | 31/10/2026 | Chủ đề → kịch bản, footage stock, TTS, phụ đề, nhạc → MP4; WebUI, API, CLI, skill cho agent | README dày quảng cáo tài trợ; skill dặn agent "không hỏi xác nhận" |
| `browser-use/video-use` | Skill dựng footage | 30,3k · MIT | 8/10/2026 | Claude Code cắt footage thô theo transcript từng từ, chấm màu, phụ đề, overlay | Âm thanh gửi ElevenLabs; không CI |
| `ATH-MaaS/Pixelle-Video` | Pipeline video ngắn | 29,6k · Apache-2.0 | 14/6/2026 | Chủ đề → ảnh/video AI (ComfyUI/RunningHub/API) → MP4, có digital human | **Đứng yên 4,5 tháng**, không test |
| `hypit-ai/hypit` | Agent "clone video viral" | 27,1k · **Apache-2.0 có điều kiện** | 29/10/2026 | Ngôn ngữ SVML + 86 gói TS; agent phân tích video mẫu rồi dựng biến thể | Cấm SaaS/bán lại; không có lời nào về đồng ý hay deepfake |
| `bradautomates/claude-video` | Skill "xem video" | 19,6k · MIT | 25/9/2026 | `/watch`: URL/file → khung hình có mốc thời gian + transcript cho agent | Engine Gemini gửi video lên Google |
| `HKUDS/ViMax` | Đa agent sinh phim | 12,8k · MIT | 30/9/2026 | Ý tưởng/kịch bản/tiểu thuyết → nhân vật, storyboard, keyframe → video (Veo, Seedance…) | Đi qua proxy `yunwu.ai`; tốn API |

### 3b.3 Hồ sơ từng repo

- **MoneyPrinterTurbo.** Python 3.11 (Streamlit + FastAPI), 1.220 commit, 174 tác giả, **538 commit từ 1/8/2026**, tag v1.3.9; 35 commit có trailer Claude. CI thật: `ci.yml` chạy ruff + pytest (251 file `test_*.py`) trên nhiều bản Python, `security.yml` chạy Trivy (action ghim SHA). Bản 2026 đã thành "hub nhà cung cấp": 35 module trong `app/services/` (Seedance, MiniMax, Pexels, ElevenLabs, upload-post.com để đăng mạng xã hội…). Đáng chú ý: provider `claude_code` gọi CLI `claude` trong container (`Dockerfile.claude` ghim `@anthropic-ai/claude-code@2.1.260`) để **dùng thuê bao Claude thay API key**; tương tự có OAuth ChatGPT/Codex và Kimi Code. Kiểm điều khoản nhà cung cấp trước khi dùng kiểu này cho dịch vụ nhiều người. `version_checker.py` gọi `api.github.com` để báo bản mới; không thấy telemetry. `docs/skill/SKILL.md` dặn agent **"Do not ask for confirmation before installing"** và tải `mpt_agent.py` từ nhánh `main` không ghim. README ✅ đúng là có đủ 4 đường WebUI/API/CLI/agent; ⚠️ phần đầu README là ~10 khối quảng cáo có link affiliate. Cài: `python -m pip install mpt` (gói PyPI tên `mpt`) hoặc `docker compose -f docker-compose.release.yml up`.
- **video-use (Browser Use).** 23 commit, 8 tác giả, chưa có tag; 10/23 commit có trailer Claude. Ý chính: **LLM không xem video mà đọc nó**: transcript từng từ (ElevenLabs Scribe) gộp thành `takes_packed.md` ~12KB, chỉ gọi ảnh `timeline_view` (filmstrip + sóng âm) ở điểm quyết định. ✅ `helpers/render.py` (801 dòng) có thật: fade 30ms, loudnorm −14 LUFS. ⚠️ "Self-evaluates at every cut boundary" chỉ là lời dặn trong `SKILL.md` bước 7 (tối đa 3 vòng), không có mã kiểm tự động. ⚠️ Không có Whisper cục bộ: mọi âm thanh đi lên `api.elevenlabs.io`. Không CI (3 file test). Có cloud "video-use.com" đang waitlist. Cài: clone rồi `ln -sfn ~/Developer/video-use ~/.claude/skills/video-use`, `uv sync`.
- **Pixelle-Video.** Gốc của AIDC-AI (Alibaba), nay nằm ở `ATH-MaaS` (README vẫn trỏ `AIDC-AI/Pixelle-Video`). 377 commit, 21 tác giả, tag v0.1.15. 29 workflow ComfyUI (Flux, Qwen-Image, Wan 2.1/2.2, LTX-2, Index-TTS…) cho bản tự host hoặc RunningHub (cloud). NOTICE liệt kê license bên thứ ba. ⚠️ **Không có file test**, CI chỉ build docs. Commit cuối 14/6/2026: coi như tạm dừng. Không thấy telemetry. Cài: bản Windows trọn gói ở Releases, hoặc `uv run` theo README.
- **hypit.** Monorepo TypeScript 86 gói (`compiler`, `timeline`, `seedance`, `whisperx`, `yt-dlp`, `volcengine-matting`…), 1.496 commit trong 3 tháng (tạo 30/7/2026), 28 tác giả, tag v0.3.1. Skill `skills/hypit/` dạy agent "đọc" video mẫu tới từng mốc thời gian rồi dựng lại bằng SVML. **License không phải Apache-2.0 thuần**: cấm vận hành dịch vụ nhiều tenant, cấm bán lại, cấm gỡ logo; người đóng góp đồng ý cho công ty đổi license (GitHub báo NOASSERTION). ⚠️ Mô tả GitHub nhắc "swap the face", nhưng README, docs và skill không có chữ nào về đồng ý của người trong video, deepfake hay bản quyền video mẫu. "1 command, 100 variants, 100M views" là khẩu hiệu. Điểm tốt: workflow phân tích issue bằng LLM chỉ chạy tay, quyền đọc, action ghim SHA. Cài: `npx skills add hypit-ai/hypit -g`.
- **claude-video (`/watch`).** 33 commit, 1 tác giả, **31/33 commit có trailer Claude**, tag v0.3.2; plugin cho Claude Code và Codex, CI chạy 16 file test. Hai engine: `local` (ffmpeg + yt-dlp, transcript bằng WhisperX cục bộ, Groq hoặc OpenAI) và **Gemini** (gửi cả video lên `generativelanguage.googleapis.com`). README tự ghi không chạy trong Cowork/Claude Chat. Hook `SessionStart` chỉ kiểm thiết lập, timeout 5 giây, không gọi mạng. Cài: `/plugin marketplace add bradautomates/claude-video` rồi cài `watch`.
- **ViMax (HKU Data Intelligence Lab).** Python 3.12, 395 commit, 17 tác giả, v1.2.0 (20/7/2026), có báo cáo kỹ thuật arXiv 2606.07649. Có agent thật cho từng vai (`screenwriter`, `storyboard_artist`, `character_portraits_generator`, `best_image_selector`…), pipeline idea2video, script2video, novel2movie, Web UI và vòng "Agent Loop" có nén ngữ cảnh. 25 file test nhưng **không có CI**. Nhà cung cấp mặc định đi qua `yunwu.ai` (proxy API bên thứ ba) cho Veo, Seedance, Nano Banana; có đường OpenRouter, Google, MiniMax trực tiếp. "telemetry" trong `tool_executor.py` chỉ ghi log cục bộ. Cài: `uv sync` rồi `python main_idea2video.py` với `configs/*.yaml`.

### 3b.4 Mẫu chung rút ra

1. **"Đọc" video thay vì "xem"**: video-use (transcript từng từ + ảnh timeline khi cần), claude-video (khung hình có mốc + transcript), hypit (đọc video mẫu theo mốc thời gian). Cách này rẻ hơn hàng trăm lần so với đưa toàn bộ khung hình cho model.
2. **Skill tự cài đặt cho agent đang thành chuẩn**, kèm rủi ro chuỗi cung ứng: MoneyPrinterTurbo tải helper từ `main` và dặn không hỏi xác nhận; video-use bảo agent tự clone và đăng ký skill. Nên ghim commit/tag và giữ bước xác nhận.
3. **Dữ liệu người dùng rời máy theo mặc định**: ElevenLabs (video-use), Gemini (claude-video), RunningHub/yunwu (Pixelle, ViMax). Chọn đường cục bộ khi footage nhạy cảm.
4. **License "gần mở" và rủi ro nội dung**: hypit (Apache-2.0 + điều kiện), cộng thêm việc clone video viral, đổi mặt mà không có cơ chế đồng ý. Kiểm LICENSE và quyền với video mẫu trước khi dùng thương mại.
5. **Số sao từ aggregator không dùng được**: bảng §2 sai 10–90 lần; hai repo lớn (Pixelle-Video, Open-Sora) có sao cao nhưng đã đứng yên nhiều tháng.

**Nguồn §3b:** GitHub search API 31/10/2026 (`repo:` cho 13 repo mới/ứng viên và 12 repo bảng §2; 10 truy vấn từ khoá/topic) · `meta_all.json`/`status_all.json` (GitHub API 31/10/2026) · clone `--filter=blob:none` ngày 31/10/2026, đọc: MoneyPrinterTurbo (HEAD 1cebc65; LICENSE, README-en.md, pyproject.toml, Dockerfile.claude, app/services/{llm.py, chatgpt_auth.py, kimi_code_oauth.py, version_checker.py, upload_post.py}, docs/skill/SKILL.md, .github/workflows/{ci.yml, security.yml}) · video-use (HEAD 43cfc56; LICENSE, README.md, SKILL.md, pyproject.toml, helpers/{render.py, transcribe.py}, skills/manim-video/scripts/setup.sh) · Pixelle-Video (HEAD 848b054; LICENSE, NOTICE, README_EN.md, workflows/, .github/workflows/docs.yml) · hypit (HEAD 0762c6be; LICENSE, README.md, package.json, skills/hypit/{SKILL.md, references/creation/reference-video.md}, .github/workflows/repository-analysis.yml) · claude-video (HEAD 03ceb42; LICENSE, README.md, hooks/{hooks.json, scripts/check-setup.sh}, skills/watch/scripts/{gemini.py, whisper.py, setup.py}) · ViMax (HEAD fd4b72e; LICENSE, readme.md, agents/, tools/, agent_runtime/tool_executor.py, tests/) · github.com/{harry0703/MoneyPrinterTurbo, browser-use/video-use, ATH-MaaS/Pixelle-Video, hypit-ai/hypit, bradautomates/claude-video, HKUDS/ViMax} · arxiv.org/abs/2606.07649 (link trong README ViMax, chưa mở)

## 3c. Đọc mã kỹ: Wan-Video/Wan2.2 và palmier-io/palmier-pro (yêu cầu người dùng, 1/11/2026)

> Hai repo lớn còn thiếu sau §3b: Wan2.2 là model video mở mà §3, §3b và mục 23 đều nhắc nhưng chưa có hồ sơ; Palmier Pro là trình dựng video macOS mở MCP cho agent. Clone `--filter=blob:none` ngày 1/11/2026, đọc mã, lịch sử git, model card Hugging Face; **không cài, không chạy script hay model nào**. Số sao từ GitHub search API 1/11/2026.

### 3c.1 `Wan-Video/Wan2.2`: model mở tốt, mã suy luận đã đứng yên

| Mục | Thông tin (HEAD `1ea34ff`, 21/9/2026) |
|---|---|
| Repo | **18.293★**, 2.396 fork, 328 issue/PR mở · tạo 28/7/2025 · **53 commit**, không tag, không release |
| Hoạt động thật | Commit cuối chạm mã `.py` là **20/9/2025** (`2677bea`, sửa tương thích SAM-2). 9 commit sau đó (11/2025 đến 21/9/2026) chỉ sửa README, thêm mục "Community Works". "Push 21/9/2026" là README, không phải mã |
| Ai viết | Nhóm Wan của Alibaba: `WanX-Video` (`wanx.ai@alibabacloud.com`) 14, Shiwei Zhang 12, kelseyee 6, các email `@alibaba-inc.com`. **0 commit có trailer Claude** |
| License mã | `LICENSE.txt` Apache-2.0 thuần, không NOTICE, `pyproject.toml` trỏ cùng file |
| License trọng số | Model card Hugging Face của T2V-A14B, TI2V-5B, S2V-14B, Animate-14B đều ghi `apache-2.0`, **không gated** (HF API 1/11/2026). README §License thêm một đoạn cấm dùng gây hại, tung tin sai, nhắm nhóm dễ tổn thương; Apache-2.0 không có điều khoản hạn chế mục đích, nên đoạn này là lời dặn, không phải điều kiện license |
| Lượt tải 30 ngày (HF) | Animate-14B 214k · S2V-14B 44k · TI2V-5B 19,5k · T2V-A14B 3,6k. Phần lớn người dùng đi qua bản Diffusers/ComfyUI đóng gói lại, không qua repo này |

**Kiến trúc.** Python ~19,1k dòng, 87 file mã. Một lối vào `generate.py` với 5 task: `t2v-A14B`, `i2v-A14B`, `ti2v-5B`, `s2v-14B` (giọng nói → video), `animate-14B` (diễn hoạt và **thay nhân vật** trong video). Dòng A14B là **MoE hai chuyên gia ~14B** (tổng 27B, 14B hoạt động mỗi bước): chuyên gia nhiễu cao dựng bố cục, chuyên gia nhiễu thấp làm chi tiết, đổi tại ngưỡng `boundary = 0.875` (`wan/configs/wan_t2v_A14B.py:36`); khi offload, chuyên gia không dùng bị đẩy về CPU (`wan/text2video.py:169-196`). TI2V-5B là model dày dùng VAE mới nén 4×16×16 (`wan/modules/vae2_2.py`); A14B vẫn dùng VAE của Wan2.1 (`vae2_1.py`). Chạy nhiều GPU bằng FSDP + Ulysses (`wan/distributed/`).

**Phần cứng: README so với mã.**

| README nói | Mã thật |
|---|---|
| A14B một GPU "cần ít nhất 80GB VRAM", kèm `--offload_model True --convert_model_dtype` | Khớp. `offload_model` tự bật khi chạy 1 GPU (`generate.py:322-323`). Repo **không có lượng tử hoá, FP8 hay offload theo lớp**; README tự chỉ sang DiffSynth-Studio, LightX2V cho máy nhỏ |
| TI2V-5B chạy trên GPU 24GB (RTX 4090) với `--t5_cpu`, "720P 5 giây dưới 9 phút" | Khớp về cờ; con số thời gian là bảng ảnh `assets/comp_effic.png`, không có script đo kèm theo **(chưa xác minh)** |
| (không nói rõ) | `flash_attn` là phụ thuộc bắt buộc trong `requirements.txt` và `pyproject.toml`, tức cần CUDA và build được FlashAttention; FA3 dùng nếu có (`wan/modules/attention.py:5-11`). Không có đường Mac/CPU chính thức |

**Mở rộng prompt (prompt extend).** Tắt mặc định (`--use_prompt_extend` `store_true`, `generate.py:170-173`); phương pháp mặc định là **`local_qwen`**, tải `Qwen/Qwen2.5-14B-Instruct` hoặc `Qwen2.5-VL-7B-Instruct` từ Hugging Face (`wan/utils/prompt_extend.py:263-294`). Chọn `dashscope` thì gọi **DashScope của Alibaba Cloud** với `qwen-plus` (văn bản) hoặc `qwen-vl-max` (kèm ảnh), key lấy từ `DASH_API_KEY`, endpoint mặc định **`dashscope.aliyuncs.com` (vùng Trung Quốc)** trừ khi đặt `DASH_API_URL` (`prompt_extend.py:137-151`). Ở task I2V, **ảnh đầu vào được gửi lên DashScope** cùng prompt (`prompt_extend.py:215-240`). Gói `dashscope` luôn được cài dù không dùng.

**Phát hiện khi đọc mã:**

- ❌ **`--enable_tts` (S2V) tự `git clone` CosyVoice từ nhánh `main` có submodule, không ghim commit, vào thư mục hiện tại**, tải model `CosyVoice2-0.5B` từ ModelScope, rồi thêm vào `sys.path` và import (`wan/speech2video.py:697-707`, `wan/utils/utils.py:228-238`). Đây là mã bên thứ ba chạy lúc runtime mà người dùng không thấy bước cài. Ngược lại, `requirements_animate.txt` ghim SAM-2 theo commit (tốt).
- ⚠️ `torch.load` không có `weights_only` ở 5 chỗ (`t5.py:496`, `vae2_1.py:614`, `vae2_2.py:883`, `animate/clip.py:519`, `animate.py:188` cho LoRA) trong khi `torch>=2.4` được chấp nhận: với torch < 2.6, file `.pth` lạ có thể chạy mã pickle. Chỉ nạp checkpoint từ `Wan-AI` chính chủ.
- ⚠️ **Không có watermark, bộ lọc NSFW hay C2PA trong mã** (grep `watermark|nsfw|safety` rỗng). Animate-14B thay được người trong video bằng nhân vật từ một ảnh; README không nói gì về đồng ý của người bị thay. Trách nhiệm dồn hết cho người dùng.
- ⚠️ **Không CI, không unit test**: không có `.github/`; `tests/test.sh` (91 dòng) chỉ là lệnh chạy thử cần đủ trọng số và nhiều GPU; `Makefile` chỉ có `format`.
- ✅ Prompt extend cục bộ là mặc định; không có telemetry; script chỉ ghi file ra thư mục hiện tại.

**Wan2.1 và các bản sau.** `Wan-Video/Wan2.1` 17.349★, push cuối 5/3/2026, cùng Apache-2.0; Wan2.2 dùng lại VAE và T5 của 2.1. **Wan 2.5 và 2.6 chỉ có qua API Alibaba Cloud (wan.video, Model Studio), không phát hành trọng số**; các nguồn bên thứ ba nhắc thêm 2.7 cũng đóng, và issue hỏi "2.5 có mở không" từ 9/2025 không được trả lời **(theo nguồn bên thứ ba, chưa xác minh từ Alibaba)**. Tức Wan2.2 nhiều khả năng là bản mở cuối của dòng Wan.

**Dùng thế nào:** model mở Apache-2.0 sạch nhất trong nhóm (so với HunyuanVideo license cộng đồng, Open-Sora và CogVideo đã đứng yên ở §3b). Nhưng repo này là **bản phát hành tham chiếu đã đóng băng**; dùng qua Diffusers (`Wan-AI/Wan2.2-*-Diffusers`), ComfyUI, DiffSynth-Studio hay LightX2V để có lượng tử hoá và bảo trì. Nếu chạy trực tiếp: `git clone https://github.com/Wan-Video/Wan2.2.git && cd Wan2.2 && pip install -r requirements.txt` rồi `huggingface-cli download Wan-AI/Wan2.2-TI2V-5B --local-dir ./Wan2.2-TI2V-5B`; dùng torch ≥ 2.6, không bật `--enable_tts` (tự cài CosyVoice ghim commit nếu cần), không dùng `dashscope` với ảnh nhạy cảm, tự gắn watermark/nhãn "AI-generated" ở khâu hậu kỳ.

### 3c.2 `palmier-io/palmier-pro`: GPL trên GitHub, nhưng phần mềm đang phát hành đã đóng

| Mục | Thông tin (HEAD `5b806b3`, 29/10/2026) |
|---|---|
| Repo | **14.669★**, 1.152 fork, 100 issue/PR mở · tạo 7/4/2026 · **1.095 commit** · 91 tag, mới nhất v0.12.0 (appcast 29/10/2026) · Palmier, Inc. (YC S24) |
| Ai viết | Harrison Tin `@palmier.io` **1.007 commit (92%)**, Marcos Rico Peng 52, người ngoài ~36. Trailer: **Cursor 144**, Claude 37 (~3,4%) |
| License | `LICENSE` GPL-3.0 (GitHub hiển thị GPL-3.0), **nhưng README dòng 1-2: bản phát hành đến v0.7.6 và mã đến tag `last-gpl-source` (24/8/2026) là GPLv3; các bản sau là độc quyền, không công bố mã**. `BINARY_LICENSE.md` cấm sao chép, sửa, phân phối lại, dịch ngược |
| Trạng thái mã | `main` = `last-gpl-source` + commit `eba39db` "Retire public source development" (28/8/2026: xoá `ci.yml`, CONTRIBUTING, FAQ, `release.sh`) + 6 commit chỉ cập nhật `appcast.xml`. **Không nhận đóng góp nữa** |

**Kiến trúc (bản GPL cuối).** Swift 6.2, SwiftUI + AppKit, AVFoundation, kernel Metal CoreImage; 540 file nguồn, **~88,4k dòng Swift**; chỉ macOS 26 trên Apple Silicon. `AGENTS.md:3` tự ghi "Non-sandboxed Developer ID app" (entitlements không có App Sandbox). Phụ thuộc: MCP `swift-sdk` 0.12.0, Sparkle, Clerk (đăng nhập), Convex (backend), Sentry và PostHog (chỉ khi bật trait `ProductionTelemetry`), MLX + speech-swift (trait `BundledSpeech`, phiên âm và khử ồn cục bộ). Model tìm kiếm SigLIP2 CoreML tải từ `huggingface.co/palmier-io` (`Search/SearchIndexConfig.swift:6`).

**AI và agent.**

- **Agent trong app**: hai đường, qua tài khoản Palmier (`PalmierClient`, trừ credit) hoặc **BYOK Anthropic/OpenAI** gọi thẳng `api.anthropic.com`/`api.openai.com`, key lưu **macOS Keychain** (`Utilities/KeychainStore.swift`, `Settings/AgentPane.swift:20`).
- **Sinh ảnh/video** (Seedance, Kling, Nano Banana…) đi qua **backend Convex đóng của Palmier**, cần đăng nhập Clerk và credit; file tham chiếu được tải lên backend (`Generation/GenerationBackend.swift`, `uploadReference`). Bản tự build từ mã không có URL backend (khoá Clerk/Convex chỉ tiêm lúc đóng gói), nên chỉ còn trình dựng + agent BYOK.
- **54 tool** (`Agent/Tools/ToolDefinitions.swift`): timeline, clip, phụ đề, màu, multicam, cắt theo transcript (`remove_words`, `remove_silence`), `generate_video/image/audio`, `import_media`, `export_project`. **Không có tool shell hay chạy mã**, không spawn CLI agent (khác OpenDesign §06 7q.0). Mô tả tool rất kỹ (frame nửa mở, ripple, chỉ số từ ổn định), đáng học khi thiết kế MCP cho NLE.
- ⚠️ `generate_video` tự ghi "Costs real money and is not undoable" nhưng **không có bước xác nhận**, chỉ chặn khi hết credit. `send_feedback` gửi báo cáo về Palmier **"there is no user confirmation step"** (`ToolDefinitions.swift:1155-1156`), chỉ dặn model diễn đạt lại, không chép nội dung người dùng.

**MCP cục bộ.** HTTP `127.0.0.1:19789/mcp`, **bật mặc định** (`Agent/MCP/MCPService.swift:9-20`), bind loopback (`MCPHTTPServer.swift:45-46`), có `OriginValidator.localhost` + kiểm Content-Type và phiên bản giao thức (`MCPHTTPServer.swift:204`) nên trang web lạ khó gọi; **nhưng không có token**: mọi tiến trình cục bộ đều gọi được toàn bộ tool, kể cả sinh video tốn tiền, nhập file từ đường dẫn bất kỳ và xuất đè ra đường dẫn tuyệt đối bất kỳ có đuôi media (`ToolExecutor+Export.swift:241-260`). Có `.mcpb` cho Claude Desktop (shim Node stdio → HTTP, `mcpb/server/index.js`).

**Telemetry (chỉ bản chính thức).** Sentry và PostHog chỉ biên dịch khi bật `ProductionTelemetry`, DSN/token tiêm lúc đóng gói (`scripts/bundle.sh:101-112`); bản tự build không gửi gì. Ở bản chính thức, **cả hai mặc định bật**, tắt trong Settings (`Telemetry/Telemetry.swift:19-23`, `Analytics.swift:84-88`); không đọc `DO_NOT_TRACK`. Sentry nhận **email và họ tên** tài khoản (`Account/AccountService.swift:213-217`), trace 10%, bật log. PostHog có allowlist thuộc tính (tốt), nhưng sự kiện xuất video gửi **`timeline_snapshot`** (cấu trúc track/clip, tỉ lệ clip AI) kèm **tên file media và tên file xuất** (chỉ basename, `Export/ExportTimelineAnalyticsSnapshot.swift:98-200`).

**Cập nhật.** Sparkle 2 có **chữ ký EdDSA** (`SUPublicEDKey`), tự kiểm (`SUEnableAutomaticChecks`), feed `raw.githubusercontent.com/palmier-io/palmier-pro/main/appcast.xml` (`Resources/Info.plist:55-60`); bản DMG ký Developer ID và notarize (`release.sh` cũ). Hệ quả với GPL: **bản v0.7.6 hay bản tự build từ `last-gpl-source` vẫn trỏ cùng feed và cùng khoá, nên Sparkle sẽ đề nghị cập nhật lên bản độc quyền v0.12.0**. Muốn giữ bản GPL phải xoá `SUFeedURL` hoặc tắt kiểm tự động trước khi build.

**Kiểm README so với mã:**

| README nói | Kết quả |
|---|---|
| "Built from scratch with Swift" | ✅ Swift thuần, không Electron |
| MCP server cho Claude/Codex/Cursor tại `127.0.0.1:19789` | ✅ Có, loopback; ⚠️ không token, bật mặc định |
| "Built-in Generative AI" (Seedance, Kling, Nano Banana Pro) | ⚠️ Qua backend Palmier đóng, cần tài khoản và credit; bản build từ mã không có |
| GPLv3 / "source code remains available" | ⚠️ Đúng với bản ≤ v0.7.6; bản đang tải từ nút Download là độc quyền; badge GitHub vẫn ghi GPL-3.0 |
| (FAQ cũ) mở mã "to improve the product with the community" | ❌ Đóng nguồn 4,5 tháng sau khi mở; người ngoài đóng góp ~36 commit theo GPLv3 **không có CLA** (`CONTRIBUTING.md:37` bản cũ); việc dùng lại mã đó trong bản độc quyền cần viết lại hoặc xin phép **(chưa xác minh họ xử lý thế nào)** |

**Cổng chất lượng.** 198 file test, ~1.640 hàm test/`@Test` (Agent, Timeline, Export, Rendering…); CI cũ chạy `swift test` trên `macos-26` và kiểm bản dịch, **đã xoá ngày 28/8/2026**, nên hiện không còn cổng nào trên mã công khai.

**Dùng thế nào:** coi Palmier Pro là **freeware độc quyền có MCP**, không phải dự án mã mở đang sống. Dùng bản DMG nếu cần trình dựng macOS cho agent: tắt telemetry và analytics trong Settings, tắt MCP khi không dùng, chỉ cho agent tin cậy kết nối, đặt hạn mức credit. Muốn học hoặc fork: `git clone https://github.com/palmier-io/palmier-pro.git && git checkout last-gpl-source`, bỏ `SUFeedURL`, `swift build` (macOS 26, Apple Silicon); phần sinh AI phải tự thay backend. So với lựa chọn mở thật: video-use, OpenMontage (§1, AGPL), Remotion (mục 22).

### 3c.3 Rút ra

1. **"Push gần đây" không phải "mã còn sống"**: Wan2.2 push 21/9/2026 nhưng mã đứng từ 9/2025; Palmier push 29/10/2026 nhưng chỉ là appcast cho bản đóng. Đo bằng commit cuối chạm mã nguồn.
2. **Badge license trên GitHub có thể nói sai về thứ người dùng thật sự tải**: Palmier ghi GPL-3.0 trong khi nút Download phát bản độc quyền, và updater đưa người dùng bản GPL sang bản đóng.
3. **Model mở không kèm biện pháp an toàn**: Wan2.2 không watermark, không lọc, có model thay người; khâu gắn nhãn AI phải nằm ở pipeline của mình.
4. **Tự tải mã lúc chạy** (CosyVoice từ `main`) là cùng loại rủi ro chuỗi cung ứng đã thấy ở §3b mẫu 2.

**Nguồn §3c:** GitHub search API 1/11/2026 (`repo:Wan-Video/Wan2.2`, `repo:Wan-Video/Wan2.1`, `repo:palmier-io/palmier-pro`) · Hugging Face API `api/models/Wan-AI/{Wan2.2-T2V-A14B, Wan2.2-TI2V-5B, Wan2.2-S2V-14B, Wan2.2-Animate-14B}` (1/11/2026) · clone `--filter=blob:none` 1/11/2026, đọc Wan2.2 (HEAD 1ea34ff; LICENSE.txt, README.md, pyproject.toml, requirements*.txt, Makefile, generate.py, tests/{README.md, test.sh}, wan/utils/{prompt_extend.py, utils.py}, wan/speech2video.py, wan/text2video.py, wan/configs/wan_t2v_A14B.py, wan/modules/{attention.py, t5.py, vae2_1.py, vae2_2.py}, wan/animate.py) · palmier-pro (HEAD 5b806b3; LICENSE, BINARY_LICENSE.md, README.md, AGENTS.md, Package.swift, Package.resolved, appcast.xml, scripts/{bundle.sh, PalmierPro.entitlements}, `git show last-gpl-source:{.github/workflows/ci.yml, scripts/release.sh, CONTRIBUTING.md, FAQ.md}`, Sources/PalmierPro/{Agent/MCP/*, Agent/Clients/BYOKClient.swift, Agent/Tools/{ToolDefinitions.swift, ToolExecutor+Export.swift, ToolExecutor+Import.swift, ToolExecutor+Generate.swift}, Generation/GenerationBackend.swift, Backend/BackendConfig.swift, Telemetry/{Telemetry.swift, Analytics.swift}, Account/AccountService.swift, Export/ExportTimelineAnalyticsSnapshot.swift, Resources/Info.plist}, mcpb/) · https://github.com/Wan-Video/Wan2.2 · https://huggingface.co/Wan-AI · https://github.com/palmier-io/palmier-pro · https://howaiworks.ai/models/wan · https://vivideo.ai/ai-models/wan-video (Wan 2.5/2.6 đóng, nguồn bên thứ ba)

## 3d. Nâng trần 2/11/2026: nguồn gốc nội dung (C2PA, watermark) và đo chất lượng video (VMAF, VBench, loudness) (yêu cầu người dùng)

> Mục 19 có nhiều pipeline sinh video (§1–§3c), nhưng chưa có chuẩn nào để **ghi nhãn đầu ra** và chưa có thước đo khách quan cho **chất lượng hình và tiếng**. Số liệu đọc bằng GitHub search API ngày 2/11/2026. Clone `--depth 1 --filter=blob:none` 6 repo, đọc LICENSE, README, Cargo/pyproject và file chính. **Không cài, không chạy.** Chuẩn ngoài GitHub tra web ngày 2/11/2026.

### 3d.1 Trần hiện tại

- Mọi pipeline (OpenMontage, MoneyPrinterTurbo, ViMax, hypit…) đều dừng ở file MP4. §3c.3 ghi "khâu gắn nhãn AI phải nằm ở pipeline của mình" (Wan2.2 không watermark), nhưng kho chưa nói gắn **bằng gì**.
- QC hiện là kiểm tra thủ công hoặc kiểm tra đơn giản: contact sheet, độ dài, LUFS trong `qc.py` của X-Studio (§3, mục 23). Chưa có chỉ số cảm nhận cho bước nén/xuất, cũng chưa có benchmark cho model sinh video.
- Thêm một rủi ro: các repo **gỡ watermark** đang rất nhiều sao (`guillaumemeyer/watermarks-remover` 25,9k★, `wiltodelta/remove-ai-watermarks` 6,3k★, tra 2/11/2026). Chỉ gắn metadata thì không đủ.

### 3d.2 Bảng repo và chuẩn mới

| Repo / chuẩn | Lớp | ★ · license (2/11/2026) | Commit cuối | Vì sao nâng trần | Rủi ro |
|---|---|---|---|---|---|
| `c2pa-org/specifications` (**C2PA 2.3**) | Chuẩn | 213 · CC-BY-4.0 | 28/10/2026 | Chuẩn Content Credentials: manifest ký số ghi nguồn gốc và chỉnh sửa, gắn vào ảnh, video, âm thanh. Bản 2.3 có PDF đề ngày 5/1/2026 (theo bài tổng hợp, bản này thêm hỗ trợ livestream, ký từng segment CMAF **(chưa xác minh)**). Repo có `softbinding-alg-list` gồm 32 thuật toán watermark/fingerprint được đăng ký, trong đó có VideoSeal, PixelSeal, AudioSeal | Repo chỉ dựng trang tài liệu; mã nguồn spec nằm ở các repo khác. Metadata bị mất khi nền tảng mạng xã hội nén lại hoặc khi bị gỡ có chủ ý |
| `contentauth/c2pa-rs` | Đầu bảng (SDK) | 438 · MIT OR Apache-2.0 (GitHub báo `NOASSERTION`) | 2/11/2026 | SDK Rust chính thức của Content Authenticity Initiative: đọc, ký, kiểm manifest; có C FFI và hỗ trợ CAWG identity. `c2patool` nay là repo riêng (`contentauth/c2patool`) | Vẫn 0.x, API đổi nhanh. Ký thật cần chứng thư nằm trong trust list. Không có chứng thư hợp lệ thì manifest chỉ là "tự khai" |
| `facebookresearch/videoseal` | Đầu bảng (watermark) | 817 · MIT (cả model) | 2/7/2026 | Watermark ẩn cho ảnh và video (VideoSeal, PixelSeal, ChunkySeal), kèm WmForger để thử tấn công. Có id soft-binding C2PA, nên manifest mất thì vẫn tra lại được | 4 tháng không commit. Watermark ẩn vẫn có thể bị tấn công gỡ (chính repo có công cụ tấn công) |
| `Netflix/vmaf` | Cổng máy (chất lượng nén) | 5,6k · BSD-2-Clause-Patent (GitHub báo `NOASSERTION`) | 30/10/2026 | Chỉ số cảm nhận chuẩn ngành, kèm PSNR, SSIM, MS-SSIM, CIEDE2000 và CAMBI (dò banding). Bộ model **VMAF v1** (6/2026) có bản 1080p, Phone và 4K; bản HDR ra 26/10/2026; có thể gọi từ ffmpeg (`libvmaf`) | **Cần video tham chiếu**: đo bản xuất so với bản master, không đo được chất lượng video AI tự sinh. Model v1 khuyên đo ở 10-bit |
| `slhck/ffmpeg-quality-metrics` | Cổng máy (CLI) | 561 · MIT | 25/10/2026 | Bọc ffmpeg để tính PSNR, SSIM, VIF, MSAD, VMAF theo từng frame, kèm thống kê và GUI; v3.13.0. Cách nhanh nhất để đưa VMAF vào CI | Cần ffmpeg build có `libvmaf` |
| `Vchitect/VBench` | Chuẩn đo (video sinh) | 1,8k · Apache-2.0 | 21/8/2026 | Benchmark cho model sinh video: VBench có 16 chiều T2V, VBench-2.0 thêm 18 chiều (vật lý, chuyển động người, suy luận thường thức), có bản I2V và video dài; điểm được đối chiếu với đánh giá của người. Từ 5/2025 chấm được video tự sinh | Nặng (nhiều model con). Nên dùng để chọn model (Wan2.2, HunyuanVideo, CogVideo ở §3), không chạy mỗi lần render |
| **EBU R 128** / ITU-R BS.1770 | Chuẩn (âm thanh) | – | – | Đo loudness thống nhất: phát sóng −23 LUFS (±1 LU), true peak −1 dBTP. `ffmpeg -af loudnorm` mặc định theo R128 | Các nền tảng streaming dùng mục tiêu khác (Spotify chọn −11/−14/−19 LUFS; mục 22 đang master −14 LUFS). Ghi rõ mục tiêu theo nơi đăng |

### 3d.3 Stack nâng trần

1. **Cổng loudness và kỹ thuật (vài giờ).** Đưa `loudnorm` 2 lượt cùng kiểm độ dài, fps, khung hình đen hoặc đứng vào bước QC của mọi pipeline. Mở rộng `qc.py` (mục 23) và áp cho đầu ra của OpenMontage (§1), MoneyPrinterTurbo (§3b).
2. **VMAF cho bước xuất (nửa ngày).** Render master bằng Remotion hoặc HyperFrames (mục 22), rồi so mỗi bản nén cho từng nền tảng với master bằng `ffmpeg-quality-metrics`. Chặn khi VMAF (model Phone cho video dọc) dưới ngưỡng tự đặt, hoặc khi CAMBI báo banding.
3. **Ký Content Credentials (1–2 ngày).** Dùng `c2pa-rs` hoặc `c2patool` để ký manifest ghi model và công cụ đã dùng (Wan2.2, TTS…), cờ "AI-generated" và các asset nguồn. Phải ký sau bước nén cuối, nếu không manifest sẽ mất.
4. **Watermark ẩn làm lớp dự phòng (1 ngày).** Chèn VideoSeal vào hình, AudioSeal (mục 14 §5d) vào tiếng, khai id soft-binding trong manifest. Như vậy khi metadata bị gỡ vẫn tra lại được nguồn.
5. **Chọn model bằng VBench (khi đổi model).** Chạy các chiều liên quan (ổn định chủ thể, độ mượt chuyển động, bám prompt) trên bộ prompt của dự án trước khi đổi model sinh video.

**Nguồn §3d:** GitHub search API 2/11/2026 (`repo:` cho 6 repo; truy vấn `c2pa`, `vmaf`, `video generation benchmark`, `watermark audio video`) · clone `--depth 1 --filter=blob:none` 2/11/2026: c2pa-org/specifications (HEAD 66ee450, 28/10/2026; README.md, LICENSE, softbinding-alg-list/softbinding-algorithm-list.json), contentauth/c2pa-rs (35866a0, 2/11/2026; README.md, LICENSE-APACHE, LICENSE-MIT, sdk/Cargo.toml), facebookresearch/videoseal (870ca7f, 2/7/2026; README.md, LICENSE), Netflix/vmaf (4611e47, 30/10/2026; README.md, LICENSE, resource/doc/models_v1.md), slhck/ffmpeg-quality-metrics (e4aafcb, 25/10/2026; README.md, LICENSE.md, pyproject.toml), Vchitect/VBench (fd18b3d, 21/8/2026; README.md, LICENSE) · Web 2/11/2026: https://spec.c2pa.org/specifications/specifications/2.3/specs/_attachments/C2PA_Specification.pdf · https://softwareseni.com/c2pa-adoption-in-2026-hardware-platforms-and-verification-reality (bài tổng hợp) · https://en.wikipedia.org/wiki/EBU_R_128 · https://ibc.org/trends/ebu-tackles-loudness-in-streaming-with-r128-update/6830.article

## 3e. Reproducible media pipelines

> Mở rộng ngày 2/11/2026. §3d đã có C2PA/VMAF/loudness; phần này nối **kế hoạch dựng → timeline → asset → bản xuất** để kiểm sai thời gian, thiếu nguồn và khả năng dựng lại. Chỉ đọc LICENSE/CI/mã tại commit ghim, chưa render hay đo A/V sync.

| Repo | ★ · license (2/11/2026) | Commit đọc | Cơ chế đáng học | Giới hạn / điều kiện |
|---|---|---|---|---|
| [AcademySoftwareFoundation/OpenTimelineIO](https://github.com/AcademySoftwareFoundation/OpenTimelineIO/tree/80c5ff30938e4adffe9c94f419b1055856cee9f5) | 2,052 · Apache-2.0 | 2026-10-30 · `80c5ff3` | OTIO: clip/track/gap/transition, RationalTime và media reference | Mô hình trao đổi timeline; không nhúng media và không phải renderer; effects/adapter có thể mất thông tin |
| [Breakthrough/PySceneDetect](https://github.com/Breakthrough/PySceneDetect/tree/c5ce29c73751e77139e838bd9ce9ab66a8e71a23) | 5,315 · BSD-3-Clause | 2026-11-02 · `c5ce29c` | Dò cut/transition, ContentDetector và AdaptiveDetector; xuất scene list | Đo biến đổi khung hình, không hiểu câu chuyện; cần tự kiểm false cut do pan/flash và miss cut |

### 3e.1 Hồ sơ và điều kiện trao đổi

**OpenTimelineIO (Academy Software Foundation):** [RationalTime](https://github.com/AcademySoftwareFoundation/OpenTimelineIO/blob/80c5ff30938e4adffe9c94f419b1055856cee9f5/src/opentime/rationalTime.h) lưu giá trị và rate, còn [ExternalReference](https://github.com/AcademySoftwareFoundation/OpenTimelineIO/blob/80c5ff30938e4adffe9c94f419b1055856cee9f5/src/opentimelineio/externalReference.h) trỏ `target_url` và `available_range`. [Tài liệu timeline](https://opentimelineio.readthedocs.io/en/latest/tutorials/otio-timeline-structure.html) ghi rõ OTIO cho phép `source_range` vượt `available_range` và không tự xác minh; effects là hành vi phụ thuộc ứng dụng. Vì vậy “file OTIO đọc được” chưa chứng minh render đúng hay đủ footage. Khi đổi editor, test round-trip duration/source range/track và effect được hỗ trợ; các effect mất nghĩa phải bake hoặc báo mất mát rõ.

**PySceneDetect (Brandon Castellano và cộng đồng):** [AdaptiveDetector](https://github.com/Breakthrough/PySceneDetect/blob/c5ce29c73751e77139e838bd9ce9ab66a8e71a23/scenedetect/detectors/adaptive_detector.py) lấy content score rồi so rolling average, giúp giảm một số false positive khi camera chuyển động; [docs chính thức](https://www.scenedetect.com/docs/head/api/detectors.html) mô tả threshold. So với ffmpeg scene filter và cut viết tay trong Remotion/HyperFrames, công cụ này tạo candidate scene list từ footage có sẵn; cần đối chiếu shot list hoặc nhãn người, không dùng số cut làm điểm “video hay”.

### 3e.2 Chọn theo đầu vào

| Trường hợp | Cách tiếp cận | Cổng quyết định |
|---|---|---|
| Video-as-code cần dựng lại từng frame | Remotion/HyperFrames + manifest asset + bản renderer ghim | Thời gian/frame rate, font, asset hash, renderer/config, seed nếu có; seed một mình không bảo đảm GPU sinh ảnh/video tất định |
| Footage dài cần cắt/phân đoạn | PySceneDetect + người duyệt shot list | Miss/false cuts trên mẫu có nhãn; không cắt phụ âm đầu/cuối hoặc cắt sai điểm nhấn |
| Chuyển timeline giữa editor | OTIO + adapter đã kiểm | Asset relink, `source_range`/handles, timebase, transitions/effects và audio ownership |
| Video dùng thương mại | Cổng quyền asset trước render | Nguồn, license code/weights/ảnh/font/nhạc, attribution và quyền giọng; C2PA không tự cấp quyền sử dụng |

### 3e.3 Stack kiểm bản xuất

1. **Asset manifest:** mỗi ảnh/footage/font/nhạc/giọng có URL gốc, hash, license, ngày tải và biến đổi; tài sản không rõ quyền vào trạng thái chưa duyệt, không trộn vào thư mục “free”.
2. **Timeline có hợp đồng:** ghim fps/timebase, resolution, color space, audio sample rate và duration; nội dung thoại/caption/shot tham chiếu cùng ID. Chọn rational time để tránh cộng số giây làm tròn qua nhiều cảnh.
3. **Preflight:** asset tồn tại, source range đủ cả handles, font tải xong, audio stream đúng, caption nằm trong duration/safe area; lỗi thiếu asset phải đỏ trước render tốn tiền.
4. **Render và A/V sync:** lưu phiên bản engine/encoder, lệnh và log; kiểm timestamp đầu/cuối, duration, audio/caption tại các mốc và đoạn chuyển cảnh. Không đo đồng bộ môi chỉ bằng duration container.
5. **Hai cổng độc lập:** dùng VMAF/loudness (§3d) cho chất lượng kỹ thuật của bản encode so master; dùng reviewer người/chuỗi frame và script có nguồn cho nội dung, sự thật và tính nhất quán. VMAF cao không chứng minh nội dung AI đúng.
6. **Publish bundle:** lưu manifest, timeline, bản master, bản phát hành và kết quả kiểm liên kết bằng hash; ký C2PA khi có đường phát hành hỗ trợ, ghi rõ trust policy. C2PA chứng minh chuỗi khai báo/provenance theo chính sách kiểm, không chứng minh mọi mệnh đề trong video là thật.

**Nguồn §3e:** GitHub metadata/HEAD, LICENSE/README/CI và các file mã permalink trên (2/11/2026); tài liệu OTIO, PySceneDetect; chuẩn và cổng đo ở §3d. Chưa kiểm round-trip adapter hay chạy renderer tại đây.

## 3f. Hồ sơ higgsfield-ai/skills: 9 skill gọi CLI đóng của Higgsfield để sinh ảnh, video, brand kit và train “Soul” khuôn mặt (ảnh README người dùng gửi, đọc mã 3/11/2026)

> Ảnh là phần đầu README: "Higgsfield AI Skills", badge license MIT, version 0.14.0, skills 9, Discord; ba cách cài (`npx skills add higgsfield-ai/skills`, `gh skill install higgsfield-ai/skills`, Claude Code `/plugin marketplace add higgsfield-ai/skills` + `/plugin install higgsfield@higgsfield`) và "Setup script". Đã clone đủ lịch sử `higgsfield-ai/skills` (HEAD `4d0757471a704dac8729ea3c2ef0f3f330e0d9b6`, 27/10/2026, 108 commit) và `higgsfield-ai/cli` (HEAD `fd21e7cb550b5835cc00c6b4abfea0c02fe77ff2`, 44 commit). **Không cài, không chạy, không đăng nhập.**

### 3f.1 Kiểm ảnh

| Ô trong ảnh | Kết quả | Đối chiếu (3/11/2026) |
|---|---|---|
| license MIT | ✅ | `LICENSE` MIT (repo skills). Lưu ý: MIT chỉ áp cho file skill; dịch vụ Higgsfield là thương mại, có trả phí |
| version 0.14.0 | ✅ | `VERSION` 0.14.0; frontmatter mỗi `SKILL.md` cũng ghi 0.14.0 |
| skills 9 | ✅ | 9 thư mục: `generate`, `soul-id`, `product-photoshoot`, `brandkit`, `marketplace-cards`, `websites`, `faceless-video`, `video-explainer` (README ghi là "compatibility entry", tức bản trùng của faceless-video), `youtube-thumbnail`. Thực chất là 8 skill riêng |
| "Each method handles the Higgsfield CLI install and auth as part of skill setup" | ⚠️ | Đúng: skill tự cài CLI. Nhưng **CLI không có mã nguồn**: repo `higgsfield-ai/cli` (694★) chỉ chứa `install.sh`, README, `MODELS.md` và LICENSE MIT. `install.sh` tải binary từ GitHub Releases, kiểm SHA-256 với `checksums.txt` **cùng release** (chống file hỏng, không chứng minh nguồn gốc), ghi vào `/usr/local/bin` bằng sudo hoặc `--prefix` |
| ★ | – | 1.869★, 348 fork, tạo 9/4/2026, push cuối 27/10/2026 (GitHub search API). Org còn có `higgsfield-ai/higgsfield` (6.279★, Apache-2.0, framework điều phối GPU, khác hẳn sản phẩm này) |

### 3f.2 Đọc mã: điều đáng ghi

- **Skill chỉ là lớp mỏng trên một dịch vụ trả phí.** Mọi việc sinh nội dung đều qua `higgsfield <lệnh>`, đăng nhập bằng `higgsfield auth login` (OAuth trên trình duyệt) và trừ credit. `generate` gọi hơn 30 model (Veo 3.1, Kling 3.0, Seedance 2.5, Flux 2, GPT Image 2.5…); `websites` tạo và deploy site React lên Cloudflare Workers **trên hạ tầng của Higgsfield**. Ảnh, video, ảnh khuôn mặt và mã site của bạn đều đi tới dịch vụ đó.
- ⚠️ **Cài CLI không hỏi ở một số skill.** `higgsfield-soul-id/SKILL.md` bước 0: "If `higgsfield` is not on `$PATH`, install it" bằng `curl … install.sh | sh`. Trong khi đó `higgsfield-brandkit/SKILL.md` ghi "install it only after permission" và "Never install system packages without the user…". Hai skill cùng repo có hai chuẩn khác nhau.
- ⚠️ **Train khuôn mặt mà không có bước đồng ý.** `soul-id` train "a personalized model on a person's face" từ ảnh người dùng đưa vào, sau đó dùng cho ảnh và video (kể cả `youtube-thumbnail` "identity-preserving"). Skill không có câu nào yêu cầu xác nhận ảnh là của chính người dùng hoặc đã được người trong ảnh đồng ý. Phần "Safety" duy nhất (`generate/references/prompt-engineering.md`) chỉ nói model sẽ từ chối "real public figures", nội dung tình dục và thương hiệu, tức là dựa vào bộ lọc phía server. Ảnh khuôn mặt là dữ liệu sinh trắc học: ở Việt Nam, Luật 91/2025 + NĐ 356/2025 có quy định riêng cho dữ liệu sinh trắc học theo tóm tắt của EY (mục 18 §4e), số điều **chưa xác minh**; ở EU là dữ liệu đặc biệt theo GDPR Điều 9.
- **Cổng chất lượng**: workflow `validate-skills.yml` kiểm frontmatter và cấu trúc skill (cài `pyyaml`); có `evals/scenarios.md` mô tả kịch bản đánh giá nhưng không thấy harness tự chạy. Không thấy mã telemetry trong repo skill (CLI đóng nên không kiểm được).
- Hỗ trợ nhiều agent: `.claude-plugin/`, `.codex-plugin/`, `.cursor-plugin/`, `agents/openai.yaml`; có `INSTALL_FOR_AGENTS.md` viết sẵn để agent tự cài.

### 3f.3 So với cùng loại và cách dùng

- Cùng dạng "skill gói một dịch vụ sinh media trả phí" như các skill video ở mục 19 §1 và mục 22. Khác với pipeline mở như Remotion hay HyperFrames (mục 22), nơi mã render chạy trên máy bạn.
- Nếu dùng: cài CLI thủ công với `--tag` cụ thể thay vì để skill tự cài `main`; chỉ train Soul bằng ảnh của chính bạn hoặc người đã đồng ý bằng văn bản; đọc điều khoản dữ liệu của Higgsfield trước khi tải ảnh khuôn mặt hay mã nguồn site lên; với nội dung phát hành, gắn nhãn nội dung do AI tạo (Luật AI 134/2025 + NĐ 142/2026, mục 18 §4e checklist 07).

**Nguồn §3f:** ảnh README người dùng gửi 3/11/2026 · clone https://github.com/higgsfield-ai/skills HEAD `4d0757471a704dac8729ea3c2ef0f3f330e0d9b6`: https://github.com/higgsfield-ai/skills/blob/4d0757471a704dac8729ea3c2ef0f3f330e0d9b6/README.md · https://github.com/higgsfield-ai/skills/blob/4d0757471a704dac8729ea3c2ef0f3f330e0d9b6/INSTALL_FOR_AGENTS.md · https://github.com/higgsfield-ai/skills/blob/4d0757471a704dac8729ea3c2ef0f3f330e0d9b6/VERSION · https://github.com/higgsfield-ai/skills/blob/4d0757471a704dac8729ea3c2ef0f3f330e0d9b6/higgsfield-soul-id/SKILL.md · https://github.com/higgsfield-ai/skills/blob/4d0757471a704dac8729ea3c2ef0f3f330e0d9b6/higgsfield-brandkit/SKILL.md · https://github.com/higgsfield-ai/skills/blob/4d0757471a704dac8729ea3c2ef0f3f330e0d9b6/higgsfield-generate/references/prompt-engineering.md · `.github/workflows/validate-skills.yml` · clone https://github.com/higgsfield-ai/cli HEAD `fd21e7cb550b5835cc00c6b4abfea0c02fe77ff2` (`install.sh`, README.md, LICENSE) · GitHub search API `repo:higgsfield-ai/skills`, `org:higgsfield-ai` 3/11/2026.

<a id="factory-media-release-2026-11-04"></a>

## 3g. Nâng trần 4/11/2026: media phát hành cần quyền sử dụng, provenance và cổng đọc báo cáo

**Trần và khoảng trống.** §3d có C2PA/watermark/chất lượng; §3e đã nối manifest asset, timeline và render. Xưởng cần thêm hợp đồng cho video demo, tài liệu đào tạo, bản ghi kiểm thử và nội dung ra mắt: **ai được phép dùng asset, artifact nào đã phát hành, verifier đã chấp nhận theo trust policy nào**. Lệnh xuất JSON chạy xong không tự tương đương chính sách nội dung đã pass.

### 3g.1 c2patool và SDK: phân biệt đọc báo cáo với chấp nhận trust

`contentauth/c2patool` là CLI riêng của Content Authenticity Initiative/Adobe và cộng đồng, dual license MIT hoặc Apache-2.0; HEAD `e02c55ce02664c1ce41dc6b3c6901d7bc9336e54` đọc 4/11/2026. `reader_from_args` đi qua `read_asset` để mở file hoặc manifest ngoài, rồi `print_reader` chọn JSON/detailed/CR JSON. Nhánh đọc thông thường trả thành công khi đọc và in report được; phần `print_reader` đã đọc **không tự áp chính sách “chỉ Trusted mới được phát hành”**. Nhánh `fragment` riêng có đếm `ValidationState::Invalid` và trả lỗi khi có file thất bại. Cấu hình trust có thể bật `verify_trust`; điều đó vẫn khác chính sách phát hành bắt buộc trạng thái Trusted. Không được suy ngữ nghĩa mã thoát của hai nhánh là một. [Callsite CLI]( https://github.com/contentauth/c2patool/blob/e02c55ce02664c1ce41dc6b3c6901d7bc9336e54/src/main.rs ) · [license MIT]( https://github.com/contentauth/c2patool/blob/e02c55ce02664c1ce41dc6b3c6901d7bc9336e54/LICENSE-MIT ) · [license Apache]( https://github.com/contentauth/c2patool/blob/e02c55ce02664c1ce41dc6b3c6901d7bc9336e54/LICENSE-APACHE ) · [CI đa nền tảng]( https://github.com/contentauth/c2patool/blob/e02c55ce02664c1ce41dc6b3c6901d7bc9336e54/.github/workflows/ci.yml ).

Đọc lại SDK `contentauth/c2pa-rs` ở HEAD `e23bcaf586661103cdbfdff91aa59fb547e4463d`: `ValidationState` tách **Invalid**, **Valid** (có signature-validated/inside-validity và không có failure ngoài nhóm SDK dung thứ) và **Trusted** (valid, có signing-credential-trusted và không còn active/ingredient failure). `Reader.validation_state()` trả kết quả validation, còn JSON là hình thức trình bày. Policy của dự án phải xử lý manifest thiếu, chữ ký sai, không đủ trust và lỗi tải tài nguyên theo các trạng thái riêng; không gọi tất cả là “fake”. [State và điều kiện tính]( https://github.com/contentauth/c2pa-rs/blob/e23bcaf586661103cdbfdff91aa59fb547e4463d/sdk/src/validation_results.rs ) · [Reader callsite]( https://github.com/contentauth/c2pa-rs/blob/e23bcaf586661103cdbfdff91aa59fb547e4463d/sdk/src/reader.rs ). Đây là đọc mã, chưa ký asset hay diễn tập trust store.

### 3g.2 Chọn công cụ theo câu hỏi

| Câu hỏi | Cách làm | Giới hạn phải giữ |
|---|---|---|
| Manifest/chữ ký/provenance có hợp lệ theo policy? | c2patool cho báo cáo; c2pa-rs khi cần tích hợp decision trong ứng dụng | Cần trust list/version/cert/timestamp policy; provenance không xác nhận mọi câu nói trong video đúng |
| Nội dung có watermark từ hệ thống của mình? | VideoSeal (§3d) hoặc watermark phù hợp nguồn | Có/không phát hiện watermark không chứng minh quyền asset, độ thật hay tác giả của mọi nội dung |
| Encode có giữ chất lượng bản master? | VMAF/ffmpeg-quality-metrics (§3d) | Metric có tham chiếu, không kiểm sự thật, license, phụ đề hay lỗi sản phẩm trong demo |
| Bản dựng có tái kiểm được và relink đủ asset? | OTIO/PySceneDetect + render manifest (§3e); dựng code ở mục 22 | Timeline đọc được không chứng minh effect tương thích; seed không bảo đảm render GPU/model tất định |

### 3g.3 Luồng phát hành media cho xưởng

1. Gắn video với release/build sản phẩm và script có nguồn; demo chức năng phải ghi rõ dữ liệu mẫu và trạng thái thực tế, không trộn màn hình mô phỏng vào bằng chứng E2E.
2. Manifest quyền ghi nguồn, hash, license code/model/asset/font/nhạc, điều kiện attribution, chấp thuận giọng/hình theo phạm vi. Việc mô hình cho tải ảnh không tự cấp quyền với tài sản bên trong.
3. Preflight timeline/audio/caption như §3e; chặn thiếu asset và dùng font không có quyền trước render tốn tiền. Tách bản master khỏi encode dành cho từng kênh.
4. Lưu báo cáo kỹ thuật và provenance cho **đúng hash bản phát hành**. Nếu policy yêu cầu trusted C2PA, verifier phải đọc state/status chứ không chỉ nhìn exit 0 hay thấy trường manifest.
5. Bộ ca âm ở dự án đích gồm asset bị sửa sau ký, thiếu manifest, signer không nằm trong policy, report không đọc được và transcoding làm mất metadata. Ghi expected behavior theo kênh phát hành; thiếu C2PA có thể là unsupported/unknown, không tự là giả mạo.
6. Lưu master, release media, manifest/report, trust-list revision và script; nội dung lỗi có đường gỡ/thay bản và kiểm lại các nơi đã phân phối. Tiêu chí hoàn thành gồm cả quyền, chức năng được mô tả và chất lượng bản xuất.

**Đã nâng sâu:** CLI/report trở thành đầu vào của quyết định phát hành có trust policy. Không tuyên bố đã có pipeline ký/trust hay benchmark media chạy tại kho này.

**Nguồn §3g:** các permalink CLI/SDK/LICENSE/CI trên; chuẩn C2PA và đối chiếu metric/timeline §3d–§3e. Không cài CLI, không chạy model hay xuất bản media.

## 3h. Kiểm ảnh "AI Video Stack": Remotion Skills, Blender và Blender MCP, faster-whisper, Chatterbox, GSAP (ảnh người dùng gửi, đọc mã 8/11/2026)

> Ảnh ghép 5 thẻ đầu (#01–#05) của loạt "AI Video Stack" 14 công cụ (NGUYEN TAT KIEM.COM), thẻ thứ 5 ghi "+10" cho phần còn lại. Mỗi thẻ ghép một video ngắn với trang GitHub của repo. Người dùng gửi thêm danh sách đủ 14 công cụ; #06–#14 ở §3h.4. Mười hai repo đã có trong catalog (mục 11, 14, 20, 22) và được đọc lại ở đây; Blender và yt-dlp là hồ sơ mới.

### 3h.1 Bảng nhanh

| # | Vai trò trong stack | Repo | ★ / fork (8/11/2026) | Giấy phép |
|---|---|---|---|---|
| 01 | Hướng dẫn agent dựng video bằng React | `remotion-dev/skills` | 6.553 / 716 | Repo skill không kèm file license; Remotion theo license riêng của Remotion |
| 02 | Dựng hình 3D, rigging, render | `blender/blender` (mirror chính thức) | 21.750 / 3.535 | GPL-3.0 |
| 02b | Cho Claude điều khiển Blender (thẻ ghi "Blender MCP") | `ahujasid/mcp-for-blender` (tên cũ `blender-mcp`) | 33.578 | MIT |
| 03 | Tạo phụ đề từ lời dẫn | `SYSTRAN/faster-whisper` | 26.577 / 2.222 | MIT |
| 04 | Tạo giọng đọc từ văn bản | `resemble-ai/chatterbox` | 27.660 / 3.722 | MIT |
| 05 | Chuyển động UI và chữ theo timeline | `greensock/GSAP` | 30.295 / 2.354 | GSAP Standard "no charge" License |

### 3h.2 Từng công cụ

- **Remotion Skills** (95 commit, tạo 19/1/2026): 13 skill chính thức, gom dưới `/remotion-best-practices`: `/remotion-create`, `/remotion-markup` (composition, animation, layout, chữ, media, hiệu ứng, âm thanh, font, timing), `/remotion-studio`, `/remotion-render`, `/remotion-maps` (Cesium, Mapbox, MapLibre, MapTiler), `/remotion-captions` (phiên âm, nhập SRT, hiển thị phụ đề), `/remotion-saas`, `/remotion-interactivity`, `/remotion-docs`, `/remotion-license`, `/remotion-upgrade`, `/remotion-multimedia`. Mỗi skill có `agents/openai.yaml` cho Codex. Cài: `npx skills add remotion-dev/skills` hoặc `gh skill install remotion-dev/skills`; khi tạo dự án mới bằng `bun create video` cũng được hỏi có thêm skill. Thẻ trong ảnh ghi "12 rules" là cấu trúc `rules/*.md` trước đây; nay đã tách thành các skill con.
- **Blender**: bộ công cụ 3D mở phủ trọn quy trình: modeling, rigging, animation, simulation, render, compositing, motion tracking và dựng video. Repo GitHub là mirror chính thức; review code và bug tracker ở projects.blender.org.
- **MCP for Blender** (266 commit): addon `addon.py` mở socket server trong Blender; MCP server cho agent viết Python Blender trực tiếp (`execute_blender_code`), tự nhìn lại kết quả (`look`: viewport, camera, nhiều góc, dải khung hình), đọc tóm tắt cảnh (`get_scene_info`), lấy tài sản từ Poly Haven, Sketchfab, Poly Pizza và sinh model 3D qua Meshy, Tripo, Hyper3D Rodin, Hunyuan3D (`generate_3d`); có công cụ tắt telemetry. Cài một lệnh `curl -LsSf https://www.mcp-for-blender.com/install.sh | sh` (Windows: `install.ps1`) hoặc `uvx mcp-for-blender setup`; tự tìm Claude Desktop, Claude Code, Codex, Cursor, VS Code, Windsurf, OpenCode, Antigravity. Cấu hình cũ `uvx blender-mcp` vẫn chạy. Có thư mục `tests/` lớn (tương thích phiên bản, bảo mật import).
- **faster-whisper** (276 commit, v1.2.1): Whisper chạy trên CTranslate2, nhanh tới 4 lần bản gốc với cùng độ chính xác và ít bộ nhớ hơn. Benchmark trong README: 13 phút audio, large-v2 trên GPU mất 1m03s (fp16), 16s với `batch_size=8` int8; small trên CPU 1m42s int8. Có `BatchedInferencePipeline`, timestamp từng từ (hợp cho phụ đề karaoke), lọc VAD, Distil-Whisper. Cài: `pip install faster-whisper`; GPU cần CUDA 12 và cuDNN 9.
- **Chatterbox** (43 commit, v0.1.2): họ model TTS mở: Turbo 350M (tiếng Anh, độ trễ thấp, tag `[laugh]`, `[cough]`), Nano 110M (chạy CPU), Multilingual V3 500M (23+ ngôn ngữ, clone giọng xuyên ngôn ngữ), Single Language Pack 6 bản tinh chỉnh. Mọi file sinh ra có watermark PerTh không nghe thấy, kèm script kiểm watermark. Từ 8/2026 Resemble AI giữ repo ở dạng lưu trữ công khai theo MIT; mã và model vẫn dùng được. Cài: `pip install chatterbox-tts` (thử trên Python 3.11).
- **GSAP** (v3.15.1): thư viện animation JavaScript không phụ thuộc, chạy mọi framework, animate CSS, SVG, canvas, WebGL; miễn phí hoàn toàn cả các plugin như SplitText, MorphSVG, ScrollTrigger nhờ Webflow tài trợ. Cài: `npm install gsap` hoặc CDN jsDelivr. Timeline của GSAP là nền cho HyperFrames và nhiều pipeline video HTML ở mục 22.

### 3h.4 Công cụ #06–#14 (danh sách đầy đủ người dùng gửi thêm)

| # | Vai trò | Repo | ★ / fork (8/11/2026) | Giấy phép |
|---|---|---|---|---|
| 06 | Claude điều khiển cảnh Blender | `ahujasid/mcp-for-blender` (§3h.2) | 33.578 | MIT |
| 07 | Agent tự xem kết quả render và sửa trước khi xuất | `ChromeDevTools/chrome-devtools-mcp` | 54.937 / 5.236 | Apache-2.0 |
| 08 | Encode, kiểm tra, xuất MP4 | `FFmpeg/FFmpeg` (mirror) | 66.719 / 14.541 | LGPL-2.1+ / GPL tùy cấu hình build |
| 09 | Ghép và render video bằng React | `remotion-dev/remotion` | 71.540 / 5.932 | Remotion License (miễn phí cho cá nhân và công ty nhỏ, công ty lớn mua Company License) |
| 10 | Hoàn thiện, phê bình, kiểm thiết kế | `pbakaus/impeccable` | 105.650 / 6.277 | Apache-2.0 |
| 11 | Render 3D bằng GPU trên trình duyệt | `mrdoob/three.js` | 117.839 / 36.905 | MIT |
| 12 | Pipeline sinh ảnh và video | `Comfy-Org/ComfyUI` | 145.616 / 17.335 | GPL-3.0 |
| 13 | Lấy clip và audio tham chiếu từ web | `yt-dlp/yt-dlp` | 206.055 / 18.102 | Unlicense |
| 14 | Viết HTML thành video, thiết kế cho agent | `heygen-com/hyperframes` | 80.641 / 7.442 | Apache-2.0 |

- **Chrome DevTools MCP**: agent điều khiển và soi Chrome thật qua MCP hoặc CLI: chụp màn hình, đọc console có stack trace theo source map, phân tích request mạng, ghi trace hiệu năng; Puppeteer tự chờ kết quả thao tác. Với video HTML, agent mở trang, chụp khung và sửa trước khi render. Cấu hình: `"command": "npx", "args": ["-y", "chrome-devtools-mcp@latest"]`; thêm `--no-usage-statistics` để tắt thống kê sử dụng.
- **FFmpeg**: bộ thư viện `libavcodec`, `libavformat`, `libavfilter`, `libswscale`, `libswresample` và công cụ `ffmpeg`, `ffprobe` xử lý audio, video, phụ đề; `ffprobe` dùng để kiểm thông số file trước khi giao.
- **Remotion**: làm video bằng agent, bằng editor tương tác hoặc bằng code; dựng thư viện asset động cho tổ chức, render hàng loạt trên hạ tầng riêng, đóng gói thành ứng dụng; tài liệu hơn 1.200 trang. Bắt đầu: `npx create-video@latest`.
- **Impeccable**: "từ vựng thiết kế" cho coding agent: `polish`, `bolder` để lái, `critique` chấm theo heuristic khả dụng và xếp thứ tự sửa, `audit` kiểm accessibility, hiệu năng, theming, responsive; 62 luật tất định bắt dấu hiệu AI slop, không cần LLM hay API key. Cài: `npx impeccable install`, rồi `/impeccable init`.
- **three.js**: thư viện 3D nhẹ, đa trình duyệt, renderer WebGL và WebGPU; repo có `llms.txt` cho agent. Cài: `npm install three`.
- **ComfyUI**: engine sinh ảnh, video bằng đồ thị node, hỗ trợ sẵn các model mở mới nhất, kiểm soát từng tham số; có `openapi.yaml` và `AGENTS.md`.
- **yt-dlp**: tải audio và video từ hàng nghìn trang (`supportedsites.md`), nhánh nâng cấp của youtube-dl; ghép luồng hình và tiếng nhờ ffmpeg (dự án có bản build FFmpeg riêng). Cài: `python -m pip install -U "yt-dlp[default]"`. Chỉ dùng cho nội dung bạn có quyền sử dụng (§3g).
- **HyperFrames**: biến HTML, CSS, media và animation tua được thành MP4 tất định; dùng qua CLI, skill cho agent hoặc Studio. Claude Code: `claude plugin marketplace add heygen-com/hyperframes` rồi `claude plugin install hyperframes@hyperframes`; agent khác: `npx skills add heygen-com/hyperframes`.

### 3h.3 Ghép thành một stack video

1. Viết kịch bản, rồi tạo giọng đọc bằng Chatterbox.
2. Chạy faster-whisper với timestamp từng từ để có phụ đề khớp giọng.
3. Dựng hình bằng Remotion (React) có Remotion Skills dẫn agent, hoặc HTML + GSAP timeline.
4. Cảnh 3D: agent điều khiển Blender qua MCP for Blender rồi render cảnh.
5. Lấy clip, audio tham chiếu bằng yt-dlp; sinh ảnh, video bổ trợ bằng ComfyUI; cảnh 3D trên web bằng three.js.
6. Agent mở trang qua Chrome DevTools MCP để xem từng khung và sửa; rà thiết kế bằng Impeccable.
7. Render bằng `/remotion-render` hoặc HyperFrames, gắn phụ đề bằng `/remotion-captions`, kiểm và encode MP4 bằng `ffprobe`/`ffmpeg`.

Liên quan: mục 22 (motion, HyperFrames, Lemo-Opuscar §9k), mục 14 (giọng nói), mục 27 (3D).

**Nguồn §3h:** ảnh người dùng gửi 8/11/2026 · clone `--filter=blob:none`: https://github.com/remotion-dev/skills/blob/a2824c67f8b4585c294a8101db9f9f0ad3c643f8/README.md · https://github.com/blender/blender/blob/9c4fc4363b03d30e576d76b86420b929f1e18465/README.md · https://github.com/blender/blender/blob/9c4fc4363b03d30e576d76b86420b929f1e18465/COPYING · https://github.com/ahujasid/mcp-for-blender/blob/2e4b0bc294694b1570d76ed01be657c22e6d02a0/README.md · https://github.com/ahujasid/mcp-for-blender/blob/2e4b0bc294694b1570d76ed01be657c22e6d02a0/LICENSE · https://github.com/SYSTRAN/faster-whisper/blob/846467d436117e44d54ad74f555d85c75834edb0/README.md · https://github.com/SYSTRAN/faster-whisper/blob/846467d436117e44d54ad74f555d85c75834edb0/LICENSE · https://github.com/resemble-ai/chatterbox/blob/ab55923c27757c90cfcc407baa57dc25a7d25217/README.md · https://github.com/resemble-ai/chatterbox/blob/ab55923c27757c90cfcc407baa57dc25a7d25217/LICENSE · https://github.com/greensock/GSAP/blob/5e6c35ff8eedea12d4f229129def635277d8b0f2/README.md · https://github.com/greensock/GSAP/blob/5e6c35ff8eedea12d4f229129def635277d8b0f2/package.json · danh sách 14 công cụ người dùng gửi thêm, clone `--depth 1 --sparse`: https://github.com/ChromeDevTools/chrome-devtools-mcp/blob/0b37364dc0a88a804c6d73d3335e776adc7f33c4/README.md · https://github.com/FFmpeg/FFmpeg/blob/2bf291526e50480d2c355b4c6c8dd04863212aa1/README.md · https://github.com/remotion-dev/remotion/blob/5dee2b6b14f7f0cebb040b7d92b0097b6be582a9/README.md · https://github.com/pbakaus/impeccable/blob/924bbd194d02e5e15a227e75b5901fb0d7a4ecad/README.md · https://github.com/mrdoob/three.js/blob/f2b6a71bdd088d9da387fcc62802323341099b92/README.md · https://github.com/Comfy-Org/ComfyUI/blob/bdb0816a292d221efeb6ec4ae41bcdff3f91fc86/README.md · https://github.com/yt-dlp/yt-dlp/blob/412e7f0a4b0588fe884a02b344ac66a06538475b/README.md · https://github.com/heygen-com/hyperframes/blob/adf14d7324109694614955f32ba6cf2b97ad79d2/README.md · https://github.com/remotion-dev/remotion/blob/5dee2b6b14f7f0cebb040b7d92b0097b6be582a9/LICENSE.md · GitHub search API 8/11/2026.

<a id="anhkysuai-2026-11-23"></a>

## Đánh giá từ kho Anh Kỹ Sư AI — 23/11/2026

Phần này có **10 hồ sơ hoặc phạm vi đối chiếu** từ [nguồn tuyển chọn](https://anhkysuai.com/kho/). [Bảng đủ 1.295 repo](../data/collections/anhkysuai-kho.json) ghi trạng thái đối chiếu từng link; [danh sách URL](../data/collections/anhkysuai-kho-links.txt) phục vụ tra cứu. Nguồn tuyển chọn giúp phát hiện repo; đánh giá bên dưới dựa trên clone và permalink upstream cùng metadata GitHub ngày 2026-11-23.

Mức `docs-read`/`code-read` chỉ áp dụng phạm vi ghi tại mỗi hồ sơ. Chưa cài, build, chạy test hay benchmark mã upstream. Giấy phép có thể tách theo code, model, nội dung, asset hoặc bản enterprise; con số/tuyên bố của tác giả chưa được tái lập nếu không có ghi chú khác.

<a id="anhkysuai-2026-11-23-identity-openmontage"></a>

### OpenMontage: đối chiếu tên repo

**Kết luận:** [calesthio/OpenMontage](https://github.com/calesthio/OpenMontage) và [OpenMontageInc/OpenMontage](https://github.com/OpenMontageInc/OpenMontage) là cùng thực thể GitHub, repository ID `1195360525` theo API ngày 2026-11-23. Giữ ID catalog `openmontage` và hồ sơ gốc; cập nhật đường dẫn chuẩn, không thêm hồ sơ trùng.

**Phạm vi đọc lại:** `docs-read`; clone tại commit [`2e003e65fa99a0f329478a2c1cdcf26bc481933a`](https://github.com/OpenMontageInc/OpenMontage/commit/2e003e65fa99a0f329478a2c1cdcf26bc481933a) và đọc tài liệu được dẫn. Đã có hồ sơ openmontage tại calesthio/OpenMontage. GitHub get_repo URL cũ trả canonical OpenMontageInc/OpenMontage, stable repository ID 1195360525 trùng metadata URL mới; git ls-remote hai URL cũng cùng HEAD. Không tạo hồ sơ trùng. Những nhận định kỹ thuật cũ ở các phần trước giữ ngày/phạm vi cũ; lượt đối chiếu này chưa tái kiểm toàn bộ implementation hoặc chạy upstream.

**Metadata:** ★ 82,544 (GitHub API, 2026-11-23); commit ngày 2026-11-15. Trạng thái archived là `false`, không dùng riêng cờ này để kết luận mức bảo trì.

**Nguồn:** [README.md](https://github.com/OpenMontageInc/OpenMontage/blob/2e003e65fa99a0f329478a2c1cdcf26bc481933a/README.md) · [LICENSE](https://github.com/OpenMontageInc/OpenMontage/blob/2e003e65fa99a0f329478a2c1cdcf26bc481933a/LICENSE) · [ci.yml](https://github.com/OpenMontageInc/OpenMontage/blob/2e003e65fa99a0f329478a2c1cdcf26bc481933a/.github/workflows/ci.yml) · [OpenMontage](https://api.github.com/repos/OpenMontageInc/OpenMontage) · [OpenMontage](https://api.github.com/repos/calesthio/OpenMontage).

<a id="anhkysuai-2026-11-23-mpv"></a>

### mpv

**Repo:** [mpv-player/mpv](https://github.com/mpv-player/mpv) · **License:** GPL-2.0-or-later mặc định; LGPL-2.1-or-later theo cấu hình build · **★ 38,265 (GitHub API, 2026-11-23)**

**Mục đích:** Trình phát audio/video dòng lệnh hỗ trợ nhiều định dạng và phụ đề.

**Giá trị và cơ chế:** README mô tả yêu cầu CPU/GPU và quyền điều khiển playback; Copyright giải thích ranh giới GPL/LGPL, hữu ích khi chọn thành phần phát media cho ứng dụng.

**Giới hạn:** Hardware decoding không mặc định bật theo tài liệu; chưa đo playback hay kiểm môi trường nhúng. License nhị phân còn phụ thuộc cờ build và thư viện liên kết.

**Cách tham khảo/tích hợp:** Ghim bản build và lựa chọn codec, kiểm phụ đề/màu/âm thanh trên bộ media thực tế trước khi nhúng.

**Thay thế:** vlc, [FFmpeg](../19-agentic-video-media/README.md#3h-kiểm-ảnh-ai-video-stack-remotion-skills-blender-và-blender-mcp-faster-whisper-chatterbox-gsap-ảnh-người-dùng-gửi-đọc-mã-8112026), gstreamer.

**Bằng chứng:** `docs-read`, ngày 2026-11-23, commit [`1eb941fdb974`](https://github.com/mpv-player/mpv/commit/1eb941fdb974fe25dc0ac68a33652c145ff41f9d). README và các tài liệu/manifest/CI hiện diện, đọc chọn lọc; chưa kiểm implementation. Chưa cài/chạy upstream.

**Nguồn:** [README.md](https://github.com/mpv-player/mpv/blob/1eb941fdb974fe25dc0ac68a33652c145ff41f9d/README.md) · [Copyright](https://github.com/mpv-player/mpv/blob/1eb941fdb974fe25dc0ac68a33652c145ff41f9d/Copyright) · [LICENSE.GPL](https://github.com/mpv-player/mpv/blob/1eb941fdb974fe25dc0ac68a33652c145ff41f9d/LICENSE.GPL) · [LICENSE.LGPL](https://github.com/mpv-player/mpv/blob/1eb941fdb974fe25dc0ac68a33652c145ff41f9d/LICENSE.LGPL) · [metadata GitHub](https://api.github.com/repos/mpv-player/mpv).

<a id="anhkysuai-2026-11-23-mediamtx"></a>

### MediaMTX

**Repo:** [bluenviron/mediamtx](https://github.com/bluenviron/mediamtx) · **License:** MIT · **★ 20,751 (GitHub API, 2026-11-23)**

**Mục đích:** Server/proxy media cho phát, đọc, ghi và phát lại luồng video/audio thời gian thực.

**Giá trị và cơ chế:** README mô tả định tuyến giữa RTSP, RTMP, WebRTC, HLS và nhiều giao thức, đường stream riêng, reload cấu hình và xác thực nội bộ/HTTP/JWT.

**Giới hạn:** Đổi giao thức không tự bảo đảm chuyển codec phù hợp mọi client; chưa đo latency hay throughput. Chứng chỉ, NAT và xác thực cần cấu hình theo môi trường.

**Cách tham khảo/tích hợp:** Dựng một nguồn thử và hai kiểu client, kiểm reconnect/ghi hình trước mở thêm stream.

**Thay thế:** srs, ovenmediaengine, mistserver.

**Bằng chứng:** `docs-read`, ngày 2026-11-23, commit [`8c10ac7dbc46`](https://github.com/bluenviron/mediamtx/commit/8c10ac7dbc466e87a8fe6cac3ecbefc36daaf426). README và các tài liệu/manifest/CI hiện diện, đọc chọn lọc; chưa kiểm implementation. Chưa cài/chạy upstream.

**Nguồn:** [README.md](https://github.com/bluenviron/mediamtx/blob/8c10ac7dbc466e87a8fe6cac3ecbefc36daaf426/README.md) · [LICENSE](https://github.com/bluenviron/mediamtx/blob/8c10ac7dbc466e87a8fe6cac3ecbefc36daaf426/LICENSE) · [metadata GitHub](https://api.github.com/repos/bluenviron/mediamtx).

<a id="anhkysuai-2026-11-23-ffmpeg.wasm"></a>

### ffmpeg.wasm

**Repo:** [ffmpegwasm/ffmpeg.wasm](https://github.com/ffmpegwasm/ffmpeg.wasm) · **License:** MIT cho wrapper; FFmpeg/core và codec theo license bản dựng · **★ 17,984 (GitHub API, 2026-11-23)**

**Mục đích:** Mang các thao tác FFmpeg vào trình duyệt thông qua WebAssembly và JavaScript.

**Giá trị và cơ chế:** README và workspace tách wrapper với core đơn/đa luồng; phù hợp xử lý media phía client khi không muốn tải file lên server.

**Giới hạn:** Chưa chuyển đổi file hoặc đo RAM; core và các thư viện codec có license riêng. Cấu hình phục vụ test dùng COOP/COEP, cần xem điều kiện worker đa luồng. HEAD được lấy không chứng minh bản phát hành còn cập nhật.

**Cách tham khảo/tích hợp:** Thử định dạng và dung lượng thực, ghim core cùng wrapper, bố trí thông báo tiến độ/hủy tác vụ.

**Thay thế:** [FFmpeg](../19-agentic-video-media/README.md#3h-kiểm-ảnh-ai-video-stack-remotion-skills-blender-và-blender-mcp-faster-whisper-chatterbox-gsap-ảnh-người-dùng-gửi-đọc-mã-8112026), webcodecs, [MediaMTX](../19-agentic-video-media/README.md#anhkysuai-2026-11-23-mediamtx).

**Bằng chứng:** `docs-read`, ngày 2026-11-23, commit [`f876f907c7e9`](https://github.com/ffmpegwasm/ffmpeg.wasm/commit/f876f907c7e9b9bf51d4ed0b913a855a63ae63fc). README và các tài liệu/manifest/CI hiện diện, đọc chọn lọc; chưa kiểm implementation. Chưa cài/chạy upstream.

**Nguồn:** [README.md](https://github.com/ffmpegwasm/ffmpeg.wasm/blob/f876f907c7e9b9bf51d4ed0b913a855a63ae63fc/README.md) · [LICENSE](https://github.com/ffmpegwasm/ffmpeg.wasm/blob/f876f907c7e9b9bf51d4ed0b913a855a63ae63fc/LICENSE) · [apps/website/docs/faq.md](https://github.com/ffmpegwasm/ffmpeg.wasm/blob/f876f907c7e9b9bf51d4ed0b913a855a63ae63fc/apps/website/docs/faq.md) · [metadata GitHub](https://api.github.com/repos/ffmpegwasm/ffmpeg.wasm).

<a id="anhkysuai-2026-11-23-obs-studio"></a>

### OBS Studio

**Repo:** [obsproject/obs-studio](https://github.com/obsproject/obs-studio) · **License:** GPL-2.0-or-later · **★ 80,076 (GitHub API, 2026-11-23)**

**Mục đích:** Ứng dụng thu, phối trộn, mã hóa, ghi hình và phát trực tiếp video.

**Giá trị và cơ chế:** README cùng CMake tách frontend Qt, scripting và các thành phần media; phù hợp tham khảo ứng dụng desktop ghép nhiều nguồn hình/âm thanh.

**Giới hạn:** Chưa ghi hoặc stream thử, không đánh giá chất lượng encoder và tải GPU. License plugin/codec và hỗ trợ capture khác theo nền tảng; workflow được xem là kiểm format, không chứng minh build toàn ứng dụng.

**Cách tham khảo/tích hợp:** Tạo scene thử và đo dropped frames/âm thanh đồng bộ theo cấu hình encoder, giữ profile cho từng máy.

**Thay thế:** [Cap](../19-agentic-video-media/README.md#anhkysuai-2026-11-23-cap), [Screenity](../19-agentic-video-media/README.md#anhkysuai-2026-11-23-screenity), [FFmpeg](../19-agentic-video-media/README.md#3h-kiểm-ảnh-ai-video-stack-remotion-skills-blender-và-blender-mcp-faster-whisper-chatterbox-gsap-ảnh-người-dùng-gửi-đọc-mã-8112026).

**Bằng chứng:** `docs-read`, ngày 2026-11-23, commit [`0c790bd0151f`](https://github.com/obsproject/obs-studio/commit/0c790bd0151fb9f574867e025ecf57e6eedc58e2). README và các tài liệu/manifest/CI hiện diện, đọc chọn lọc; chưa kiểm implementation. Chưa cài/chạy upstream.

**Nguồn:** [README.rst](https://github.com/obsproject/obs-studio/blob/0c790bd0151fb9f574867e025ecf57e6eedc58e2/README.rst) · [COPYING](https://github.com/obsproject/obs-studio/blob/0c790bd0151fb9f574867e025ecf57e6eedc58e2/COPYING) · [metadata GitHub](https://api.github.com/repos/obsproject/obs-studio).

<a id="anhkysuai-2026-11-23-losslesscut"></a>

### LosslessCut

**Repo:** [mifi/lossless-cut](https://github.com/mifi/lossless-cut) · **License:** GPL-2.0 · **★ 46,341 (GitHub API, 2026-11-23)**

**Mục đích:** GUI desktop dùng FFmpeg để cắt, ghép và remux video/audio mà hạn chế mã hóa lại.

**Giá trị và cơ chế:** README mô tả gần như sao chép trực tiếp stream, quản lý segment, track và metadata; phù hợp rough cut nhanh và giữ chất lượng nguồn.

**Giới hạn:** Chưa kiểm độ chính xác điểm cắt, đồng bộ audio hay codec trên file thật. Ghép yêu cầu codec tương thích; lossless không đồng nghĩa mọi ranh giới cắt đều tự do như encode lại.

**Cách tham khảo/tích hợp:** Dùng bản sao, kiểm đầu/cuối từng segment trong player đích và giữ EDL/marker để tái dựng quyết định cắt.

**Thay thế:** avidemux, [shotcut](../08-awesome-lists-learning/README.md#6c57-dựng-video--slide-tự-động), [FFmpeg](../19-agentic-video-media/README.md#3h-kiểm-ảnh-ai-video-stack-remotion-skills-blender-và-blender-mcp-faster-whisper-chatterbox-gsap-ảnh-người-dùng-gửi-đọc-mã-8112026).

**Bằng chứng:** `docs-read`, ngày 2026-11-23, commit [`8f95118fb021`](https://github.com/mifi/lossless-cut/commit/8f95118fb021a6fb95761f2807e760b92482af05). README và các tài liệu/manifest/CI hiện diện, đọc chọn lọc; chưa kiểm implementation. Chưa cài/chạy upstream.

**Nguồn:** [README.md](https://github.com/mifi/lossless-cut/blob/8f95118fb021a6fb95761f2807e760b92482af05/README.md) · [LICENSE](https://github.com/mifi/lossless-cut/blob/8f95118fb021a6fb95761f2807e760b92482af05/LICENSE) · [metadata GitHub](https://api.github.com/repos/mifi/lossless-cut).

<a id="anhkysuai-2026-11-23-cap"></a>

### Cap

**Repo:** [CapSoftware/Cap](https://github.com/CapSoftware/Cap) · **License:** AGPL-3.0, ngoại trừ `cap-camera*` và `scap-*` theo MIT · **★ 25,458 (GitHub API, 2026-11-23)**

**Mục đích:** Quay màn hình, chỉnh sửa và chia sẻ video qua ứng dụng desktop và dịch vụ web.

**Giá trị và cơ chế:** Tài liệu phân biệt Studio xử lý bản ghi cục bộ và Instant tải lên trong lúc quay; cấu trúc hỗ trợ tự host và lưu trữ tương thích S3.

**Giới hạn:** Không thể gọi mọi chế độ là offline. LICENSE tách phạm vi AGPL/MIT; chưa kiểm luồng upload, quyền truy cập link hay chi phí các dịch vụ tùy chọn.

**Cách tham khảo/tích hợp:** Chọn chế độ ghi phù hợp, cấu hình storage và chính sách chia sẻ, rồi thử quyền xem/xóa với tài khoản riêng.

**Thay thế:** [OBS Studio](../19-agentic-video-media/README.md#anhkysuai-2026-11-23-obs-studio), [Screenity](../19-agentic-video-media/README.md#anhkysuai-2026-11-23-screenity), Loom.

**Bằng chứng:** `docs-read`, ngày 2026-11-23, commit [`f6e70ac50ed9`](https://github.com/CapSoftware/Cap/commit/f6e70ac50ed9de70b6134b704834c7af67205985). README và các tài liệu/manifest/CI hiện diện, đọc chọn lọc; chưa kiểm implementation. Chưa cài/chạy upstream.

**Nguồn:** [README.md](https://github.com/CapSoftware/Cap/blob/f6e70ac50ed9de70b6134b704834c7af67205985/README.md) · [LICENSE](https://github.com/CapSoftware/Cap/blob/f6e70ac50ed9de70b6134b704834c7af67205985/LICENSE) · [metadata GitHub](https://api.github.com/repos/CapSoftware/Cap).

<a id="anhkysuai-2026-11-23-video2x"></a>

### Video2X

**Repo:** [k4yt3x/video2x](https://github.com/k4yt3x/video2x) · **License:** AGPL-3.0; thư viện và models bên thứ ba có điều khoản riêng · **★ 22,853 (GitHub API, 2026-11-23)**

**Mục đích:** Tăng độ phân giải video và nội suy khung hình với các backend xử lý ảnh.

**Giá trị và cơ chế:** Snapshot dùng C++ và cấu hình cho các backend NCNN/Vulkan như Real-ESRGAN, Real-CUGAN, Anime4K và RIFE; phù hợp khảo sát chuỗi xử lý video.

**Giới hạn:** Chưa chạy GPU hoặc đo artefact, tốc độ và đồng bộ audio. Giấy phép chương trình không bao trùm mọi model; binary dựng sẵn có yêu cầu phần cứng riêng.

**Cách tham khảo/tích hợp:** Thử một đoạn video ngắn, so sánh frame và audio, ghi rõ backend/weights trước khi xử lý theo lô.

**Thay thế:** Upscayl, [Real-ESRGAN](../14-voice-multimodal/README.md#anhkysuai-2026-11-23-real-esrgan), [Anime4K](../19-agentic-video-media/README.md#anhkysuai-2026-11-23-anime4k).

**Bằng chứng:** `docs-read`, ngày 2026-11-23, commit [`7db9c18d6278`](https://github.com/k4yt3x/video2x/commit/7db9c18d6278bbad9c3eda0e4e4ae210f9a688eb). README và các tài liệu/manifest/CI hiện diện, đọc chọn lọc; chưa kiểm implementation. Chưa cài/chạy upstream.

**Nguồn:** [README.md](https://github.com/k4yt3x/video2x/blob/7db9c18d6278bbad9c3eda0e4e4ae210f9a688eb/README.md) · [LICENSE](https://github.com/k4yt3x/video2x/blob/7db9c18d6278bbad9c3eda0e4e4ae210f9a688eb/LICENSE) · [metadata GitHub](https://api.github.com/repos/k4yt3x/video2x).

<a id="anhkysuai-2026-11-23-anime4k"></a>

### Anime4K

**Repo:** [bloc97/Anime4K](https://github.com/bloc97/Anime4K) · **License:** MIT cho mã; hình minh họa giữ quyền của chủ sở hữu · **★ 21,659 (GitHub API, 2026-11-23)**

**Mục đích:** Upscale và làm sạch hình anime theo hướng xử lý thời gian thực bằng shader.

**Giá trị và cơ chế:** README nêu phạm vi tối ưu là nguồn anime 1080p và cung cấp preset tích hợp trình phát; phù hợp thử cải thiện hiển thị khi xem.

**Giới hạn:** Tác giả phân biệt rõ với phục hồi nguồn 720p, DVD hoặc nội dung suy giảm mạnh. Chưa đo tốc độ hay so sánh chất lượng; license mã không bao gồm ảnh minh họa.

**Cách tham khảo/tích hợp:** Chọn preset theo nguồn và GPU, so sánh cảnh nhiều nét hoặc phụ đề để phát hiện viền giả và mất chi tiết.

**Thay thế:** [Real-ESRGAN](../14-voice-multimodal/README.md#anhkysuai-2026-11-23-real-esrgan), waifu2x, [Video2X](../19-agentic-video-media/README.md#anhkysuai-2026-11-23-video2x).

**Bằng chứng:** `docs-read`, ngày 2026-11-23, commit [`7684e9586f8d`](https://github.com/bloc97/Anime4K/commit/7684e9586f8dcc738af08a1cdceb024cc184f426). README và các tài liệu/manifest/CI hiện diện, đọc chọn lọc; chưa kiểm implementation. Chưa cài/chạy upstream.

**Nguồn:** [README.md](https://github.com/bloc97/Anime4K/blob/7684e9586f8dcc738af08a1cdceb024cc184f426/README.md) · [LICENSE](https://github.com/bloc97/Anime4K/blob/7684e9586f8dcc738af08a1cdceb024cc184f426/LICENSE) · [metadata GitHub](https://api.github.com/repos/bloc97/Anime4K).

<a id="anhkysuai-2026-11-23-screenity"></a>

### Screenity

**Repo:** [alyssaxuu/screenity](https://github.com/alyssaxuu/screenity) · **License:** GPL-3.0 (nhánh MV3 hiện tại) · **★ 19,009 (GitHub API, 2026-11-23)**

**Mục đích:** Quay màn hình trong trình duyệt, chú thích trong lúc ghi và chỉnh sửa bản ghi.

**Giá trị và cơ chế:** README mô tả extension Manifest V3 cùng lưu trữ/xuất video; tích hợp Google Drive cần cấu hình OAuth của bản triển khai.

**Giới hạn:** Phiên bản hiện tại đã chuyển từ MIT cũ sang GPL-3.0. Screenity Pro là dịch vụ riêng; chưa kiểm permissions, hiệu năng ghi hay luồng tải dữ liệu.

**Cách tham khảo/tích hợp:** Kiểm quyền extension, chính sách lưu video và OAuth trên tài khoản thử trước khi phân phối nội bộ.

**Thay thế:** [OBS Studio](../19-agentic-video-media/README.md#anhkysuai-2026-11-23-obs-studio), [Cap](../19-agentic-video-media/README.md#anhkysuai-2026-11-23-cap), Loom.

**Bằng chứng:** `docs-read`, ngày 2026-11-23, commit [`45562d130fcf`](https://github.com/alyssaxuu/screenity/commit/45562d130fcf745683ac34651e1a5389340f8301). README và các tài liệu/manifest/CI hiện diện, đọc chọn lọc; chưa kiểm implementation. Chưa cài/chạy upstream.

**Nguồn:** [README.md](https://github.com/alyssaxuu/screenity/blob/45562d130fcf745683ac34651e1a5389340f8301/README.md) · [LICENSE](https://github.com/alyssaxuu/screenity/blob/45562d130fcf745683ac34651e1a5389340f8301/LICENSE) · [metadata GitHub](https://api.github.com/repos/alyssaxuu/screenity).

## 4. Nguồn

- https://github.com/calesthio/OpenMontage (README, AGENTS.md, AGENT_GUIDE.md, commits) · https://github.com/calesthio · https://openmontage.video
- https://pinggy.io/blog/openmontage_agentic_video_production/ · https://knightli.com/en/2026/06/22/openmontage-ai-video-production-guide/ · https://dev.to/andrew-ooo/openmontage-review-open-source-agentic-video-production-296l · https://hysenlabs.com/projects/calesthio-openmontage · https://www.opensourcealternatives.to/item/openmontage · https://explainx.ai/blog/openmontage-agentic-video-production-claude-code-2026 · https://www.visionstory.ai/open-source/openmontage · https://tosea.ai/blog/openmontage-agentic-video-production-guide · https://www.blog.brightcoding.dev/2026/10/10/calesthioopenmontage-agentic-video-production-from-natural-language
- §1b OpenCreator (13/10/2026): https://github.com/krillinai/OpenCreator (clone đầy đủ, 936 commit, HEAD 2b80bca 13/10/2026; README, LICENSE, CONTRIBUTING.md, `apps/desktop/src/main/telemetry.ts`, `settings-store.ts`, `apps/daemon/src/main.ts`, `startup.ts`, `.github/workflows/ci.yml`, commit afe6aa4/4d29f87/bfbf59a/406dec8) · https://trendshift.io/repositories/13360 · https://sourceforge.net/projects/krillinai.mirror/ · https://aiindigo.com/blog/krillinai-deep-dive-technical-review · https://tessl.io/registry/skills/github/krillinai/KrillinAI/krillinai-tts/review
- https://github.com/THU-MAIC/OpenMAIC/discussions/346 · https://github.com/volcengine/OpenViking/discussions/1083
- https://trendshift.io/topics/ai-video · https://www.atlascloud.ai/blog/tips/github-ai-video-generator-skill-directory-free-tools-vs-paid-apis-2026 · https://agenticvideos.org/ · https://arxiv.org/pdf/2608.29814 · https://arxiv.org/pdf/2608.28122

<a id="xlsx-2026-11-23"></a>

## Đánh giá bổ sung từ bảng "Top 100 GitHub AI Skills" — 23/11/2026

Phần này có **12 hồ sơ** từ bảng xlsx người dùng gửi ngày 2026-11-23; đọc bằng `git clone --depth 1`, không cài hay chạy mã upstream. Lúc đọc, REST API của GitHub bị chặn nên trong hồ sơ ★ và `pushed_at` ghi **(chưa xác minh)**; số sao lấy lại cùng ngày qua GitHub search API nằm trong `data/projects.json` và [catalog/](../catalog/README.md), `pushed_at` vẫn chưa xác minh.

<a id="xlsx-2026-11-23-fal-ai-skills"></a>

### fal-ai-community/skills (bộ skill chính thức cho fal.ai)

**Repo:** [fal-ai-community/skills](https://github.com/fal-ai-community/skills) · **License:** MIT (LICENSE, © 2026 fal.ai; chỉ áp cho file skill, các model fal chạy trả phí theo endpoint) · **★ (chưa xác minh; GitHub API bị chặn ngày 2026-11-23)**

**Mục đích:** thư viện **36 skill** (đếm thư mục `skills/*/SKILL.md`; README ghi "36-skill library", không phải khoảng 15) dạy agent chọn endpoint fal.ai, viết prompt theo họ model và nối nhiều lệnh để ra ảnh, video, âm thanh, 3D. Đường chạy mặc định là CLI `genmedia` (`models`, `schema`, `run`, `status`, `upload`, `pricing`); phần lớn skill là lớp tri thức, không gọi API trực tiếp.

**Giá trị và cơ chế:** (1) tách lớp rõ: `genmedia` và `model-routing` (lõi), ba skill ô dù (`fal-models-catalog`, `fal-prompting`, `fal-recipes` với `references/` theo modality/họ model/use case), skill sản xuất, và 5 skill "kết quả trọn gói" có `assets/plan.json` cho bộ chạy có thể tiếp tục (`genmedia/scripts/run_plan.py`, chỉ dùng thư viện chuẩn Python + `subprocess`). (2) Quy tắc cứng trong `genmedia/SKILL.md`: luôn `--json`, không bịa endpoint ID, xem schema trước khi truyền tham số, tải file bằng `--download`. (3) CI kiểm chéo: `validate.yml` chạy trên ubuntu/macos/windows, `build-skills-index.py --check` (sinh `skills/index.json`) và `unittest`; `docs/public-access-audit.json` ghi 102 schema endpoint công khai được GET ẩn danh ngày 2026-11-06. (4) Phân phối nhiều nền: plugin Claude (`.claude-plugin`), Gemini, OpenClaw, MCP Registry (workflow `publish-mcp-registry.yml` chỉ chạy tay, phải gõ đúng chuỗi xác nhận).

**Danh sách 36 skill theo nhóm:**

| Nhóm | Skill |
|---|---|
| Lõi | `genmedia`, `model-routing`, `fal-media` (dùng khi host có MCP fal) |
| Ô dù tri thức | `fal-models-catalog`, `fal-prompting`, `fal-recipes` |
| Sản xuất ảnh/video | `character-design`, `character-sheet`, `cinematography`, `commercial`, `branded-graphics`, `storytelling`, `ugc`, `marketing`, `fal-shot-craft`, `h3-cinematic-prompter`, `fal-script-writer`, `fal-video-generation`, `fal-audio-generation`, `photo-editing` |
| Kết quả trọn gói | `product-ad-campaign`, `game-asset-production`, `storyboard-to-short-film`, `ecommerce-product-photography`, `localize-and-repurpose` |
| Quy trình/dọc | `fal-workflow`, `genmedia-workflow` (cũ), `fan-cam`, `fal-gamedev`, `fal-redesign`, `fal-regenerate-3d`, `fal-video-production`, `video-compositing`, `fal-motion-graphics`, `reels-creator`, `wrap-it-up` |

**Giới hạn:** (1) `genmedia/SKILL.md` hướng dẫn cài CLI bằng `curl https://genmedia.sh/install -fsS | bash` rồi `genmedia setup --api-key "$FAL_KEY"`; CLI là repo khác (`fal-ai-community/genmedia-cli`, chưa đọc), nên không biết nó làm gì ngoài lời mô tả. (2) Mọi prompt, ảnh tham chiếu (`genmedia upload` đưa file lên CDN của fal) và kết quả đi qua fal.ai; ảnh người thật dùng cho `fan-cam`, `ugc`, `character-*` là dữ liệu cá nhân. (3) Chi phí theo endpoint (`genmedia pricing` có sẵn nhưng skill không đặt trần chi tiêu, chưa tìm thấy ngưỡng dừng trong phần đã đọc). (4) Một vài skill cần renderer cục bộ (`reels-creator`, `video-compositing`: "requires local rendering dependencies"). (5) Bản `distribution/openclaw/.mcp.json` trỏ `https://mcp.fal.ai/mcp-relay` dùng OAuth: dữ liệu qua máy chủ trung gian của fal. (6) README ghi nhiều kênh phát hành còn "pending"; HEAD đọc chỉ có 1 commit trong clone nông nên chưa đánh giá được nhịp bảo trì.

**Cách tham khảo/tích hợp:** học cấu trúc ô dù + kết quả trọn gói + kiểm chỉ mục bằng CI, hơn là lấy từng skill. Nếu dùng: cài CLI thủ công và ghim bản, đặt hạn mức chi tiêu ở tài khoản fal, đọc `docs/public-access-audit.json` trước khi tin endpoint, và không tải ảnh người thật lên khi chưa có đồng ý.

**Thay thế:** [higgsfield-ai/skills](../19-agentic-video-media/README.md#3f-hồ-sơ-higgsfield-aiskills-9-skill-gọi-cli-đóng-của-higgsfield-để-sinh-ảnh-video-brand-kit-và-train-soul-khuôn-mặt-ảnh-readme-người-dùng-gửi-đọc-mã-3112026) (skill gói một dịch vụ khác, CLI đóng), [calesthio/generative-media-skills](../19-agentic-video-media/README.md) (id `generative-media-skills`), [OpenMontage](../19-agentic-video-media/README.md#anhkysuai-2026-11-23-identity-openmontage) (pipeline nhiều provider, mã mở).

**Bằng chứng:** `code-read`, ngày 2026-11-23, commit [`ca79376d624d`](https://github.com/fal-ai-community/skills/commit/ca79376d624d244e601f9182fa80b5bf66efec9c) (2026-11-06). Đã đọc README, LICENSE, `validate.yml`, `publish-mcp-registry.yml` (đầu), `genmedia/SKILL.md`, frontmatter của cả 36 SKILL.md, `genmedia/scripts/run_plan.py` (chỉ import), `docs/public-access-audit.json`, `.claude-plugin/plugin.json`, `distribution/openclaw/.mcp.json`. Chưa đọc `references/`, `scripts/build-*.py`, `tests/`, CLI `genmedia`; chưa cài, chưa chạy, chưa gọi API.

**Nguồn:** [README.md](https://github.com/fal-ai-community/skills/blob/ca79376d624d244e601f9182fa80b5bf66efec9c/README.md) · [LICENSE](https://github.com/fal-ai-community/skills/blob/ca79376d624d244e601f9182fa80b5bf66efec9c/LICENSE) · [.github/workflows/validate.yml](https://github.com/fal-ai-community/skills/blob/ca79376d624d244e601f9182fa80b5bf66efec9c/.github/workflows/validate.yml) · [.github/workflows/publish-mcp-registry.yml](https://github.com/fal-ai-community/skills/blob/ca79376d624d244e601f9182fa80b5bf66efec9c/.github/workflows/publish-mcp-registry.yml) · [skills/genmedia/SKILL.md](https://github.com/fal-ai-community/skills/blob/ca79376d624d244e601f9182fa80b5bf66efec9c/skills/genmedia/SKILL.md) · [skills/genmedia/scripts/run_plan.py](https://github.com/fal-ai-community/skills/blob/ca79376d624d244e601f9182fa80b5bf66efec9c/skills/genmedia/scripts/run_plan.py) · [docs/public-access-audit.json](https://github.com/fal-ai-community/skills/blob/ca79376d624d244e601f9182fa80b5bf66efec9c/docs/public-access-audit.json) · [distribution/openclaw/.mcp.json](https://github.com/fal-ai-community/skills/blob/ca79376d624d244e601f9182fa80b5bf66efec9c/distribution/openclaw/.mcp.json) · [metadata GitHub](https://api.github.com/repos/fal-ai-community/skills) (không đọc được, 403).

<a id="xlsx-2026-11-23-super-video-maker-skill"></a>

### bomx/super-video-maker-skill

**Repo:** [bomx/super-video-maker-skill](https://github.com/bomx/super-video-maker-skill) (README clone từ `Bomx/super-video-maker-skill`) · **License:** **không có file LICENSE và README không nêu license** (mặc định bảo lưu mọi quyền, không phải mã mở) · **★ (chưa xác minh; GitHub API bị chặn ngày 2026-11-23)**

**Mục đích:** skill "sản xuất video trọn gói" của Distribb: biến ý tưởng/link/kịch bản thành video bằng avatar HeyGen, ảnh OpenAI, b-roll Seedance 2.5 qua fal.ai (Replicate là phương án cũ), ghi màn hình, Remotion hoặc HyperFrames, FFmpeg, phụ đề Whisper, nhạc ElevenLabs. Định dạng chủ lực là "Avatar Explainer" kèm 17 recipe JSON (`recipes/*.json`).

**Giá trị và cơ chế:** khác phần lớn skill video ở chỗ có đủ lớp kiểm: `tools/ffmpeg_qc.py`, `broll_layout_qc.py`, `ad_quality_gate.py`, `tests/test_video_recipes.py` kiểm schema recipe; 6.343 dòng Python trong `tools/` và `workflows/` (HeyGen client, Seedance qua fal, ghi màn hình bằng Playwright/Xvfb, ghép demo). Có tài liệu quyết định tốt: `SEEDANCE_AVATAR_ROI.md` kết luận avatar "NO-GO" làm mặc định vì chiếm khoảng 90% chi phí mỗi video mà không giúp mục tiêu AI-answer-engine (số liệu tự công bố trong file, chưa tái lập). `SKILL.md` yêu cầu ảnh gốc người thật phải "licensed/user-provided" trước khi tạo nhân vật hư cấu.

**Giới hạn:** (1) **không license** nên không thể nhúng hay phân phối lại hợp pháp, chỉ nên tham khảo. (2) `SKILL.md` khai 5 biến môi trường bắt buộc (HeyGen, fal, OpenAI, ElevenLabs...) và `.env.example` còn có `REPLICATE_API_TOKEN`, `AWS_*`: nhiều khóa trả phí, nhiều nơi nhận dữ liệu. (3) **`tools/demo_video_composer.py` hàm `upload_to_s3` đặt `ACL: public-read`** và bucket mặc định `aiagentassets` nếu không đặt `AWS_S3_BUCKET`: video/phụ đề demo có thể thành công khai trên bucket của tác giả hoặc của bạn nếu cấu hình sai. Đây là đọc mã tĩnh, chưa chạy. (4) Không có CI (`.github/` vắng), kiểm chỉ có test cục bộ. (5) `agent_browser_recorder.py` cho agent điều khiển trình duyệt để quay "bằng chứng": rủi ro lộ phiên đăng nhập trên màn hình quay (chưa đọc kỹ cách xử lý cookie). (6) Một nhân vật "hư cấu" dựng từ ảnh người thật: cần đồng ý/quyền ảnh.

**Cách tham khảo/tích hợp:** chỉ lấy ý tưởng: recipe JSON có schema, cổng QC trước khi xuất, và phép tính ROI cho avatar. Không chạy `demo_video_composer.py` với AWS thật khi chưa đổi ACL và bucket; không dán nhiều khóa vào một `.env` dùng chung. Muốn dùng mã thì hỏi tác giả về license.

**Thay thế:** [browser-use/video-use](../19-agentic-video-media/README.md) (id `video-use`, MIT, dựng footage thô), [OpenMontage](../19-agentic-video-media/README.md#anhkysuai-2026-11-23-identity-openmontage), [heygen-com/skills](../19-agentic-video-media/README.md#xlsx-2026-11-23-heygen-skills) (chính thức, MIT).

**Bằng chứng:** `code-read`, ngày 2026-11-23, commit [`3fec4aa66a1d`](https://github.com/bomx/super-video-maker-skill/commit/3fec4aa66a1d4f8b249746eabc372547f67bba5c) (2026-08-09). Đã đọc README, SKILL.md (đầu và phần liên quan), `.env.example`, `SEEDANCE_AVATAR_ROI.md` (đầu), `tools/demo_video_composer.py` (hàm upload), grep endpoint trong `tools/*.py`. Chưa đọc `heygen_client.py`, `ugc_ad_runner.py`, workflows; chưa cài hay chạy.

**Nguồn:** [README.md](https://github.com/bomx/super-video-maker-skill/blob/3fec4aa66a1d4f8b249746eabc372547f67bba5c/README.md) · [SKILL.md](https://github.com/bomx/super-video-maker-skill/blob/3fec4aa66a1d4f8b249746eabc372547f67bba5c/SKILL.md) · [.env.example](https://github.com/bomx/super-video-maker-skill/blob/3fec4aa66a1d4f8b249746eabc372547f67bba5c/.env.example) · [tools/demo_video_composer.py](https://github.com/bomx/super-video-maker-skill/blob/3fec4aa66a1d4f8b249746eabc372547f67bba5c/tools/demo_video_composer.py) · [SEEDANCE_AVATAR_ROI.md](https://github.com/bomx/super-video-maker-skill/blob/3fec4aa66a1d4f8b249746eabc372547f67bba5c/SEEDANCE_AVATAR_ROI.md) · [tests/test_video_recipes.py](https://github.com/bomx/super-video-maker-skill/blob/3fec4aa66a1d4f8b249746eabc372547f67bba5c/tests/test_video_recipes.py) · [metadata GitHub](https://api.github.com/repos/bomx/super-video-maker-skill) (không đọc được, 403).

<a id="xlsx-2026-11-23-visual-skills"></a>

### smixs/visual-skills

**Repo:** [smixs/visual-skills](https://github.com/smixs/visual-skills) · **License:** **CC BY 4.0** (LICENSE + NOTICE; bắt buộc ghi công Serge Shima khi dùng/chuyển thể; CC không dành cho phần mềm nhưng ở đây áp cho văn bản skill) · **★ (chưa xác minh; GitHub API bị chặn ngày 2026-11-23)**

**Mục đích:** hai skill chỉ gồm văn bản: `video` (viết prompt video AI theo vai đạo diễn/biên kịch/dựng phim cho Seedance 2.5, Kling, Veo, Runway, Luma, Pika, Sora) và `image` (prompt ảnh cho Nano Banana, GPT Image, kèm storyboard/keyframe). Có bản README tiếng Nga.

**Giá trị và cơ chế:** `video/SKILL.md` chỉ 106 dòng và **cố ý mỏng**: ép đọc `references/dramaturgy.md` trước, rồi `universal-rules.md`, rồi một file model; đầu ra phải qua "dramaturgy check" 6 điểm và kiểm 3 chi tiết mỗi cảnh trước khi trả. Công thức cảnh `desire + obstacle + geometry + gaze + rhythm`, danh sách từ cấm ("cinematic", "epic", "stunning"...). `video/references/seedance-25.md` ghi theo hướng dẫn chính thức của ByteDance ngày 31/7/2026 (tác giả khai; chưa đối chiếu nguồn ByteDance). `NOTICE` ghi rõ nguồn chuyển thể: `agentara/skills` (MIT), viết lại, không chép.

**Giới hạn:** không có mã, test, CI (`.github/` vắng) nên không có cổng máy; chất lượng chỉ đo bằng đọc. Nội dung gắn với phiên bản model giữa năm 2026 và sẽ lỗi thời nhanh. Không gọi API nào, không có dữ liệu rời máy (chỉ cài qua `npx skills add` từ skills.sh, README nêu). CC BY 4.0 buộc ghi công trong sản phẩm phái sinh, khác hẳn MIT của đa số skill cùng nhóm.

**Cách tham khảo/tích hợp:** dùng làm lớp viết prompt đứng trước một skill chạy model (fal, Higgsfield, HeyGen). Khi nhúng hoặc sửa nội dung, giữ dòng ghi công và NOTICE. Trước khi tin cú pháp model, kiểm lại với tài liệu hiện hành của từng hãng.

**Thay thế:** [fal-ai-community/skills](../19-agentic-video-media/README.md#xlsx-2026-11-23-fal-ai-skills) (`fal-prompting`, `fal-shot-craft`, cùng ý nhưng gắn endpoint fal, MIT), [higgsfield-ai/skills](../19-agentic-video-media/README.md#3f-hồ-sơ-higgsfield-aiskills-9-skill-gọi-cli-đóng-của-higgsfield-để-sinh-ảnh-video-brand-kit-và-train-soul-khuôn-mặt-ảnh-readme-người-dùng-gửi-đọc-mã-3112026), [OpenMontage](../19-agentic-video-media/README.md#anhkysuai-2026-11-23-identity-openmontage).

**Bằng chứng:** `code-read`, ngày 2026-11-23, commit [`61a60d317f0f`](https://github.com/smixs/visual-skills/commit/61a60d317f0fa0c3dc98902e58a7cb178838ae3f) (2026-11-06). Đọc README, LICENSE (đầu), NOTICE, `plugin.json`, `video/SKILL.md` (đầu và cuối), dòng đếm của `image/SKILL.md`; chưa đọc từng file trong `references/` (60 file trong repo). Chưa thử đầu ra prompt trên model thật.

**Nguồn:** [README.md](https://github.com/smixs/visual-skills/blob/61a60d317f0fa0c3dc98902e58a7cb178838ae3f/README.md) · [LICENSE](https://github.com/smixs/visual-skills/blob/61a60d317f0fa0c3dc98902e58a7cb178838ae3f/LICENSE) · [NOTICE](https://github.com/smixs/visual-skills/blob/61a60d317f0fa0c3dc98902e58a7cb178838ae3f/NOTICE) · [.claude-plugin/plugin.json](https://github.com/smixs/visual-skills/blob/61a60d317f0fa0c3dc98902e58a7cb178838ae3f/.claude-plugin/plugin.json) · [video/SKILL.md](https://github.com/smixs/visual-skills/blob/61a60d317f0fa0c3dc98902e58a7cb178838ae3f/video/SKILL.md) · [image/SKILL.md](https://github.com/smixs/visual-skills/blob/61a60d317f0fa0c3dc98902e58a7cb178838ae3f/image/SKILL.md) · [metadata GitHub](https://api.github.com/repos/smixs/visual-skills) (không đọc được, 403).

<a id="xlsx-2026-11-23-heygen-skills"></a>

### heygen-com/skills

**Repo:** [heygen-com/skills](https://github.com/heygen-com/skills) · **License:** MIT (LICENSE, © 2026 HeyGen; chỉ áp cho file skill, dịch vụ HeyGen thương mại, trừ credit gói) · **★ (chưa xác minh; GitHub API bị chặn ngày 2026-11-23)**

**Mục đích:** 3 skill chính thức của HeyGen: `heygen-avatar` (tạo avatar bền vững: mặt + giọng, mặc định từ mô tả; ảnh thật hoặc video "digital twin" là tùy chọn), `heygen-video` (tạo video có avatar), `heygen-translate` (dịch/lồng tiếng video). Chạy qua HeyGen CLI (`HEYGEN_API_KEY`) hoặc MCP từ xa `https://mcp.heygen.com/mcp/v1/` (OAuth, dùng credit gói).

**Giá trị và cơ chế:** (1) hai đường giao vận có thứ tự ưu tiên rõ: có `HEYGEN_API_KEY` thì dùng CLI, không thì dò MCP. (2) `heygen-video/references/` có `prompt-craft`, `frame-check`, `motion-vocabulary`, `official-prompt-guide`, `troubleshooting`: tri thức viết prompt cho video avatar. (3) Quy trình phát hành chuẩn: `release-please`, `CHANGELOG.md`, `VERSION` 3.2.0; `validate-skills.yml` kiểm skill **cài sạch qua `gh skill install`** (gói tự chứa), `publish.yml` đẩy lên ClawHub khi gắn tag `v*`. (4) Gắn nhãn đa nền: `.claude-plugin`, `.codex-plugin`, `.cursor-plugin`, `INSTALL_FOR_AGENTS.md` cho agent tự cài.

**Giới hạn:** (1) Cài CLI bằng `curl -fsSL https://static.heygen.ai/cli/install.sh | bash` (README và `INSTALL_FOR_AGENTS.md`); CLI ở repo khác `heygen-com/heygen-cli`, chưa đọc. (2) **Có tín hiệu rời máy mặc định**: skill yêu cầu agent chạy `heygen feedback --rating ... --comment ...` "once per task" (CLI mode), và `heygen-video/scripts/update-check.sh` gọi `raw.githubusercontent.com/.../VERSION` định kỳ; tắt feedback bằng `HEYGEN_NO_ANALYTICS` hoặc `heygen config set analytics false`. Nội dung `--comment` do agent tự viết: có thể chứa chi tiết tác vụ (chưa kiểm). Tương phản với `liveavatar-agent-skills` (cùng hãng) nơi feedback chỉ gửi sau khi người dùng đồng ý. (3) `heygen-avatar` nhận ảnh/video người thật để tạo avatar (`create_photo_avatar`, digital twin); trong `SKILL.md` và `references/avatar-creation.md` không thấy từ "consent" hay bước xác nhận quyền ảnh, chỉ yêu cầu ảnh rõ mặt. Ảnh khuôn mặt là dữ liệu sinh trắc học (xem mục 18 §4e, số điều luật VN chưa xác minh). (4) HEAD là 2026-07-14 trong khi CHANGELOG mới nhất là 3.2.0 ngày 2026-05-13: có commit sau bản phát hành cuối. (5) Mặc định "Target = the agent": skill chủ động tạo danh tính avatar cho agent.

**Cách tham khảo/tích hợp:** nếu cần video avatar chính chủ, đây là đường chính thức hơn các skill bên thứ ba. Cài CLI thủ công và ghim phiên bản, đặt `HEYGEN_NO_ANALYTICS=1` nếu không muốn gửi tín hiệu, chỉ dùng ảnh của chính mình hoặc người đã đồng ý bằng văn bản, gắn nhãn nội dung AI khi phát hành (mục 18 §4e). Học cách kiểm "cài sạch qua `gh skill`" trong CI.

**Thay thế:** [higgsfield-ai/skills](../19-agentic-video-media/README.md#3f-hồ-sơ-higgsfield-aiskills-9-skill-gọi-cli-đóng-của-higgsfield-để-sinh-ảnh-video-brand-kit-và-train-soul-khuôn-mặt-ảnh-readme-người-dùng-gửi-đọc-mã-3112026) (CLI đóng, train khuôn mặt), [bomx/super-video-maker-skill](../19-agentic-video-media/README.md#xlsx-2026-11-23-super-video-maker-skill) (dùng HeyGen làm một provider, không license), [HyperFrames](../22-motion-design-animation/README.md) (cũng của HeyGen nhưng là engine render mở, Apache-2.0, chạy cục bộ).

**Bằng chứng:** `code-read`, ngày 2026-11-23, commit [`1bd5e4d33a02`](https://github.com/heygen-com/skills/commit/1bd5e4d33a028dfed3abf504c5e3dd644fb9ea8a) (2026-07-14). Đọc README, LICENSE, VERSION, CHANGELOG (đầu), `validate-skills.yml` (đầu), `publish.yml` (đầu), `.mcp.json`, `heygen-avatar/SKILL.md` (frontmatter + phần feedback), `avatar-creation.md` (đầu), `update-check.sh` (đầu). Chưa đọc `heygen-video/SKILL.md` toàn bộ, `heygen-translate`, `setup`; chưa cài, chưa đăng nhập, chưa gọi API.

**Nguồn:** [README.md](https://github.com/heygen-com/skills/blob/1bd5e4d33a028dfed3abf504c5e3dd644fb9ea8a/README.md) · [LICENSE](https://github.com/heygen-com/skills/blob/1bd5e4d33a028dfed3abf504c5e3dd644fb9ea8a/LICENSE) · [CHANGELOG.md](https://github.com/heygen-com/skills/blob/1bd5e4d33a028dfed3abf504c5e3dd644fb9ea8a/CHANGELOG.md) · [.github/workflows/validate-skills.yml](https://github.com/heygen-com/skills/blob/1bd5e4d33a028dfed3abf504c5e3dd644fb9ea8a/.github/workflows/validate-skills.yml) · [.mcp.json](https://github.com/heygen-com/skills/blob/1bd5e4d33a028dfed3abf504c5e3dd644fb9ea8a/.mcp.json) · [heygen-avatar/SKILL.md](https://github.com/heygen-com/skills/blob/1bd5e4d33a028dfed3abf504c5e3dd644fb9ea8a/heygen-avatar/SKILL.md) · [heygen-avatar/references/avatar-creation.md](https://github.com/heygen-com/skills/blob/1bd5e4d33a028dfed3abf504c5e3dd644fb9ea8a/heygen-avatar/references/avatar-creation.md) · [heygen-video/scripts/update-check.sh](https://github.com/heygen-com/skills/blob/1bd5e4d33a028dfed3abf504c5e3dd644fb9ea8a/heygen-video/scripts/update-check.sh) · [metadata GitHub](https://api.github.com/repos/heygen-com/skills) (không đọc được, 403).

<a id="xlsx-2026-11-23-runway-studio-skills"></a>

### runway-studio-skills

**Repo:** [runwayml/runway-studio-skills](https://github.com/runwayml/runway-studio-skills) · **License:** MIT (LICENSE ghi `Copyright (c) 2026`, không nêu tên chủ sở hữu) · **★ chưa xác minh (GitHub API không truy cập được trong phiên, 2026-11-23)**

**Mục đích:** Skill đơn lẻ cho agent gọi Runway API sinh video, ảnh, âm thanh (quảng cáo sản phẩm, TTS, lồng tiếng) bằng bốn script Python chạy qua `uv run`.

**Giá trị và cơ chế:** Một `SKILL.md` + `COOKBOOK.md` (công thức quảng cáo sản phẩm) + năm script (`generate_video.py` tự định tuyến text/image/video-to-video và character performance, `generate_image.py`, `generate_audio.py`, `get_task.py`, `runway_helpers.py`). `CLAUDE.md` dặn agent không hardcode khóa, không đọc lại file media vào hội thoại, tải kết quả ngay vì URL đầu ra hết hạn sau 24–48 giờ. Ảnh cục bộ được tải lên bằng `uploads.create_ephemeral` rồi dùng URI `runway://`.

**Giới hạn:** Trả phí theo credit Runway và cần `RUNWAYML_API_SECRET`; đọc mã thấy `poll_task` lặp `while True` mỗi 5 giây, không có hạn chót tổng. Repo 12 file, một commit khi clone nông (2026-04-20), không có CI, không có test; danh sách model cứng trong README/SKILL có thể lỗi thời so với API. Repo `runwayml/skills` (hồ sơ kế bên) ghi trong CHANGELOG rằng các skill cũ đã bị gỡ khỏi gói đó, nhưng không có tuyên bố nào cho biết repo này bị thay thế (chưa xác minh trạng thái bảo trì).

**Cách tham khảo/tích hợp:** Chỉ dùng làm mẫu cấu trúc skill gọi API sinh media. Trước khi dùng thật: đặt khóa trong secret manager, thêm timeout tổng cho vòng poll, đặt trần credit, và kiểm tên model với tài liệu Runway hiện hành.

**Thay thế:** [runwayml/skills](#xlsx-2026-11-23-runwayml-skills), [higgsfield-skills](../19-agentic-video-media/README.md#3f-hồ-sơ-higgsfield-aiskills-9-skill-gọi-cli-đóng-của-higgsfield-để-sinh-ảnh-video-brand-kit-và-train-soul-khuôn-mặt-ảnh-readme-người-dùng-gửi-đọc-mã-3112026), generative-media-skills, [ComfyUI](../19-agentic-video-media/README.md#3h-kiểm-ảnh-ai-video-stack-remotion-skills-blender-và-blender-mcp-faster-whisper-chatterbox-gsap-ảnh-người-dùng-gửi-đọc-mã-8112026).

**Bằng chứng:** `code-read`, ngày 2026-11-23, commit [`c1c0348fda3a`](https://github.com/runwayml/runway-studio-skills/commit/c1c0348fda3acf4ef864393b6485afb4600eedda) (commit ngày 2026-04-20). Đã đọc README, SKILL.md, CLAUDE.md, COOKBOOK.md, package.json, LICENSE, `scripts/runway_helpers.py` (khóa, poll, tải, upload) và đếm cấu trúc 12 file tại commit này; không có thư mục CI. Chưa cài `uv`, chưa gọi Runway API, chưa chạy script nào; chưa đọc đủ `generate_*.py` từng nhánh tham số.

**Nguồn:** [README.md](https://github.com/runwayml/runway-studio-skills/blob/c1c0348fda3acf4ef864393b6485afb4600eedda/README.md) · [SKILL.md](https://github.com/runwayml/runway-studio-skills/blob/c1c0348fda3acf4ef864393b6485afb4600eedda/SKILL.md) · [CLAUDE.md](https://github.com/runwayml/runway-studio-skills/blob/c1c0348fda3acf4ef864393b6485afb4600eedda/CLAUDE.md) · [scripts/runway_helpers.py](https://github.com/runwayml/runway-studio-skills/blob/c1c0348fda3acf4ef864393b6485afb4600eedda/scripts/runway_helpers.py) · [LICENSE](https://github.com/runwayml/runway-studio-skills/blob/c1c0348fda3acf4ef864393b6485afb4600eedda/LICENSE) · metadata GitHub: chưa xác minh (API trả 403 trong phiên).

<a id="xlsx-2026-11-23-runwayml-skills"></a>

### Runway Dev (runwayml/skills)

**Repo:** [runwayml/skills](https://github.com/runwayml/skills) · **License:** MIT (RunwayML, Inc.) · **★ chưa xác minh (GitHub API không truy cập được trong phiên, 2026-11-23)**

**Mục đích:** Plugin chính thức của Runway (`runway-api`, tên hiển thị Runway Dev, phiên bản 4.0.1): MCP của Developer Portal cộng bảy skill hướng dẫn agent tích hợp Runway API vào ứng dụng bằng SDK.

**Giá trị và cơ chế:** Khác repo script ở trên: không sinh media thay người dùng mà dạy agent **viết code tích hợp**. Gồm `runway-dev` (nền), `-setup`, `-models`, `-model-routers`, `-characters`, `-recipes`, `-workflows`. Quy tắc đáng học: khóa API chỉ ở server; đọc `docs.dev.runwayml.com/ai-context.md` trước khi chọn model thay vì nhớ; coi tài liệu và kết quả MCP là dữ liệu không tin cậy; dùng wait helper của SDK thay vòng poll tự viết; **bản Claude (`claude/`) cấm chạy sinh media tính phí**, chỉ kiểm bằng typecheck/test mock. Một manifest cho Claude Code, Codex và Cursor; MCP `https://dev.runwayml.com/mcp` (bản Claude dùng `/mcp/claude`, bỏ công cụ `create_avatar`).

**Giới hạn:** Phụ thuộc dịch vụ MCP và tài khoản Runway (OAuth qua trình duyệt); khóa SDK vẫn do người dùng tạo. Thư mục `claude/` nhân bản bảy skill nên có nguy cơ lệch so với `skills/` (CI chạy `build:plugin` và `validate:plugin` nhưng chưa đọc rõ cơ chế so khớp). README ghi listing `claude-plugins-official` do Anthropic quản lý và có thể ghim phiên bản khác. CHANGELOG 4.0.0 ghi các skill và helper cũ không còn được phát hành.

**Cách tham khảo/tích hợp:** Cài bằng `claude plugin marketplace add runwayml/skills` rồi `claude plugin install runway-api@runway-dev`. Ghim phiên bản/commit, tự thực hiện bước đăng nhập OAuth, giữ `RUNWAYML_API_SECRET` ở server; dùng mẫu 'tài liệu và MCP là dữ liệu không tin cậy' cho skill tích hợp API khác.

**Thay thế:** [runway-studio-skills](#xlsx-2026-11-23-runway-studio-skills), [higgsfield-skills](../19-agentic-video-media/README.md#3f-hồ-sơ-higgsfield-aiskills-9-skill-gọi-cli-đóng-của-higgsfield-để-sinh-ảnh-video-brand-kit-và-train-soul-khuôn-mặt-ảnh-readme-người-dùng-gửi-đọc-mã-3112026), elevenlabs-skills (mục 22), stripe-ai (mục 20, cùng kiểu plugin hãng + MCP).

**Bằng chứng:** `code-read`, ngày 2026-11-23, commit [`6e98d3f35407`](https://github.com/runwayml/skills/commit/6e98d3f3540705331acd748d75427f4bd7c90ce1) (commit ngày 2026-10-30). Đã đọc README, CHANGELOG, `plugin.json`, `.claude-plugin/marketplace.json`, `claude/.mcp.json`, `.mcp.json`, hai SKILL.md (`runway-dev`, `runway-dev-setup`) và workflow CI `dev-plugin.yml`, LICENSE tại commit này. Chưa chạy `npm ci`/test/build plugin, chưa kết nối MCP, chưa kiểm hai cây skill có giống nhau không.

**Nguồn:** [README.md](https://github.com/runwayml/skills/blob/6e98d3f3540705331acd748d75427f4bd7c90ce1/README.md) · [CHANGELOG.md](https://github.com/runwayml/skills/blob/6e98d3f3540705331acd748d75427f4bd7c90ce1/CHANGELOG.md) · [plugin.json](https://github.com/runwayml/skills/blob/6e98d3f3540705331acd748d75427f4bd7c90ce1/plugin.json) · [claude/skills/runway-dev/SKILL.md](https://github.com/runwayml/skills/blob/6e98d3f3540705331acd748d75427f4bd7c90ce1/claude/skills/runway-dev/SKILL.md) · [claude/.mcp.json](https://github.com/runwayml/skills/blob/6e98d3f3540705331acd748d75427f4bd7c90ce1/claude/.mcp.json) · [.github/workflows/dev-plugin.yml](https://github.com/runwayml/skills/blob/6e98d3f3540705331acd748d75427f4bd7c90ce1/.github/workflows/dev-plugin.yml) · [LICENSE](https://github.com/runwayml/skills/blob/6e98d3f3540705331acd748d75427f4bd7c90ce1/LICENSE) · metadata GitHub: chưa xác minh (API trả 403 trong phiên).

<a id="xlsx-2026-11-23-ffmpeg-skill-kajisho5"></a>

### ffmpeg-skill (kajisho5)

**Repo:** [kajisho5/ffmpeg-skill](https://github.com/kajisho5/ffmpeg-skill) · **License:** MIT (Copyright (c) 2026 kajisho5) · **★ chưa xác minh (GitHub API không truy cập được trong phiên, 2026-11-23)**

**Mục đích:** Skill + bộ 42 công cụ Python (chỉ thư viện chuẩn) bọc `ffmpeg`/`ffprobe` cho agent chỉnh sửa video/audio cục bộ, kèm MCP server và hợp đồng công cụ đọc được bằng máy (v4.7.0).

**Giá trị và cơ chế:** Quy trình cố định probe → sửa không mất dữ liệu nếu được → kiểm → verify; công cụ nhận tham số có kiểu (`--aspect 9:16 --fit pad`) thay vì để agent tự ghép lệnh. `input_schema` của mỗi tool **sinh từ chính parser `argparse`** lúc chạy và CI báo lỗi nếu lệch; từ chối ghi đè nguồn nếu thiếu `--overwrite`; MCP mặc định chỉ liệt kê 12 tool lõi ('stable'), 30 tool còn lại 'beta'. PRIVACY.md nói không telemetry, không dùng mạng; ngoại lệ là engine Whisper do người dùng tự cài có thể tải model. CI chạy ma trận Ubuntu/macOS/Windows, Python 3.10/3.13, FFmpeg 6.1/7.1/8/9, kèm CodeQL, OpenSSF Scorecard, ClusterFuzzLite, dependabot.

**Giới hạn:** Rất lớn so với đối thủ (498 file tracked, khoảng 27 nghìn dòng Python ở `scripts/`), nên chi phí đọc và rà trước khi nhúng cao; README tự gọi 30/42 tool là beta. Cần FFmpeg 6.1+ và Python 3.10+. Ảnh/clip demo do Veo sinh (README tự ghi). Hệ sinh thái riêng của tác giả (nhiều repo `*-skill`) gợi ý rủi ro phụ thuộc một người. `.claude/settings.json` của repo bật marketplace trailofbits cho phát triển (chỉ ảnh hưởng người clone repo để làm việc trong đó). Huy hiệu Trendshift/npm/Scorecard là tuyên bố trong README, chưa kiểm độc lập.

**Cách tham khảo/tích hợp:** `npx ffmpeg-skill` hoặc cài plugin; ghim phiên bản, chạy `doctor` để biết FFmpeg có codec cần, đặt `FFMPEG_SKILL_MCP_TOOLS` để thu nhỏ danh sách tool. Dùng `--dry-run --json` trước các bước ghi và không bỏ cờ bảo vệ nguồn.

**Thay thế:** [n0an/ffmpeg-skill](#xlsx-2026-11-23-ffmpeg-skill-n0an), [FFmpeg](../19-agentic-video-media/README.md#3h-kiểm-ảnh-ai-video-stack-remotion-skills-blender-và-blender-mcp-faster-whisper-chatterbox-gsap-ảnh-người-dùng-gửi-đọc-mã-8112026), video-use (mục 19), [ffmpeg.wasm](#anhkysuai-2026-11-23-ffmpeg.wasm).

**Bằng chứng:** `code-read`, ngày 2026-11-23, commit [`c559cb5fcbfb`](https://github.com/kajisho5/ffmpeg-skill/commit/c559cb5fcbfbb37b8a48165b0c49e6bdfa674883) (commit ngày 2026-11-22). Đã đọc README, SKILL.md, `.claude-plugin/plugin.json`, `package.json`, PRIVACY.md, `.claude/settings.json`, `.github/workflows/ci.yml`, LICENSE, danh sách `scripts/` và `bin/install.js` (chỉ `spawnSync` tới python/ffmpeg) tại commit này; grep `scripts/_contract.py`, `_review.py` không thấy `urllib`/`requests`/`socket` ngoài một comment. Chưa chạy bộ test (24 mục trong `tests/`), chưa chạy công cụ nào, chưa kiểm FFmpeg/codec; chưa đọc từng script trong 42 tool.

**Nguồn:** [README.md](https://github.com/kajisho5/ffmpeg-skill/blob/c559cb5fcbfbb37b8a48165b0c49e6bdfa674883/README.md) · [SKILL.md](https://github.com/kajisho5/ffmpeg-skill/blob/c559cb5fcbfbb37b8a48165b0c49e6bdfa674883/SKILL.md) · [PRIVACY.md](https://github.com/kajisho5/ffmpeg-skill/blob/c559cb5fcbfbb37b8a48165b0c49e6bdfa674883/PRIVACY.md) · [scripts/_contract.py](https://github.com/kajisho5/ffmpeg-skill/blob/c559cb5fcbfbb37b8a48165b0c49e6bdfa674883/scripts/_contract.py) · [.github/workflows/ci.yml](https://github.com/kajisho5/ffmpeg-skill/blob/c559cb5fcbfbb37b8a48165b0c49e6bdfa674883/.github/workflows/ci.yml) · [LICENSE](https://github.com/kajisho5/ffmpeg-skill/blob/c559cb5fcbfbb37b8a48165b0c49e6bdfa674883/LICENSE) · metadata GitHub: chưa xác minh (API trả 403 trong phiên).

<a id="xlsx-2026-11-23-ffmpeg-skill-n0an"></a>

### ffmpeg-skill (n0an, FFmpeg Recipes)

**Repo:** [n0an/ffmpeg-skill](https://github.com/n0an/ffmpeg-skill) · **License:** MIT (Copyright (c) 2026 Anton Novoselov) · **★ chưa xác minh (GitHub API không truy cập được trong phiên, 2026-11-23)**

**Mục đích:** Skill thuần tài liệu (SKILL.md 87 dòng + 6 file tham chiếu, khoảng 750 dòng) gom công thức FFmpeg đã chọn lọc để agent ráp lệnh thay vì nhớ từ trí nhớ (v1.0.0).

**Giá trị và cơ chế:** Không có mã thực thi: quy tắc cốt lõi nằm trong SKILL.md (không dùng `-c copy` khi có filter; seek đầu ra để cắt chính xác; mặc định libx264 `-crf 18 -pix_fmt yuv420p +faststart`; thẻ `hvc1` cho HEVC trên Apple; đặt lại timestamp sau `trim`), kèm mẫu đầu ra (lệnh một dòng + giải thích cờ + caveat). Tham chiếu tải theo nhu cầu (glossary, simple/advanced editing, audio, asset generation, encoding). Có manifest cho Claude Code, Gemini extension và `agents/openai.yaml` (Codex).

**Giới hạn:** Chỉ là cheatsheet: không kiểm tra đầu ra, không dò năng lực FFmpeg cục bộ, không bảo vệ file nguồn; mọi lệnh do agent chạy qua shell của chính nó. Mặc định `-preset veryslow` rất chậm cho file dài. Một tác giả, một commit đọc được (2026-09-08, clone nông); không có CI (chỉ 13 file). Công thức chưa được chạy lại trong phiên này.

**Cách tham khảo/tích hợp:** `npx skills add https://github.com/n0an/ffmpeg-skill --skill ffmpeg`. Phù hợp làm lớp tri thức nhẹ khi dự án đã có sandbox chạy FFmpeg; cần thêm bước probe/verify của dự án chủ.

**Thay thế:** [kajisho5/ffmpeg-skill](#xlsx-2026-11-23-ffmpeg-skill-kajisho5), [SkillsBench](../20-claude-plugins-ecosystem/README.md#xlsx-2026-11-23-skillsbench) (skill mẫu cắt/nối), [FFmpeg](../19-agentic-video-media/README.md#3h-kiểm-ảnh-ai-video-stack-remotion-skills-blender-và-blender-mcp-faster-whisper-chatterbox-gsap-ảnh-người-dùng-gửi-đọc-mã-8112026).

**Bằng chứng:** `docs-read`, ngày 2026-11-23, commit [`aec7706a3602`](https://github.com/n0an/ffmpeg-skill/commit/aec7706a3602134bfc606cc8a85eb010dfaa22ad) (commit ngày 2026-09-08). Đã đọc README, SKILL.md, `.claude-plugin/plugin.json`, `agents/openai.yaml`, LICENSE và đếm dòng các file tham chiếu tại commit này; không đọc từng công thức trong 6 file tham chiếu, không có mã để đọc. Chưa chạy lệnh nào.

**Nguồn:** [README.md](https://github.com/n0an/ffmpeg-skill/blob/aec7706a3602134bfc606cc8a85eb010dfaa22ad/README.md) · [ffmpeg/SKILL.md](https://github.com/n0an/ffmpeg-skill/blob/aec7706a3602134bfc606cc8a85eb010dfaa22ad/ffmpeg/SKILL.md) · [ffmpeg/references/glossary.md](https://github.com/n0an/ffmpeg-skill/blob/aec7706a3602134bfc606cc8a85eb010dfaa22ad/ffmpeg/references/glossary.md) · [.claude-plugin/plugin.json](https://github.com/n0an/ffmpeg-skill/blob/aec7706a3602134bfc606cc8a85eb010dfaa22ad/.claude-plugin/plugin.json) · [LICENSE](https://github.com/n0an/ffmpeg-skill/blob/aec7706a3602134bfc606cc8a85eb010dfaa22ad/LICENSE) · metadata GitHub: chưa xác minh (API trả 403 trong phiên).

<a id="xlsx-2026-11-23-comfyui-agent-skill-mie"></a>

### comfyui-agent-skill (MieMieeeee)

**Repo:** [MieMieeeee/comfyui-agent-skill](https://github.com/MieMieeeee/comfyui-agent-skill) · **License:** Apache-2.0 (LICENSE gốc); thư mục vendored `scripts/comfy_api_simplified/` mang LICENSE MIT riêng (VENDORING.md ghi Copyright 2024 deimos-deimos) · **★ chưa xác minh (GitHub API không truy cập được trong phiên, 2026-11-23)**

**Mục đích:** Skill + CLI Python (gói PyPI `comfyui-agent-skill-mie`, bản 0.1.14) để agent chạy workflow ComfyUI **đã đăng ký** (ảnh, sửa ảnh, video LTX, nhạc, TTS, matting, LivePortrait, clone giọng) trên máy chủ ComfyUI cục bộ hoặc tự dựng đáng tin.

**Giá trị và cơ chế:** Hợp đồng ổn định thay cho JSON workflow tự do: mỗi workflow có `*.config.json` đã duyệt (12 workflow 'stable'), CLI trả JSON có mã lỗi (`SERVER_UNAVAILABLE`, `NO_OUTPUT`...), có chế độ `--submit`/poll, `check` và `doctor` kiểm máy chủ và node/model trước khi chạy lâu. SKILL.md nói rõ **không chạy JSON workflow chưa duyệt**; workflow của người dùng chỉ được nhập vào registry riêng sau khi xem config. CHANGELOG ghi các bản vá cụ thể: timeout HTTP 10s/60s cho mọi lệnh `requests` (0.1.13), chặn đường dẫn đầu ra kiểu Windows/`..` (0.1.12), hỗ trợ đầu ra 3D (0.1.14).

**Giới hạn:** README tự dặn không trỏ vào endpoint ComfyUI công cộng không tin cậy; không cài ComfyUI hay model, phần cứng GPU và custom node là việc của người dùng. Repo vendoring một phần `comfy_api_simplified` (sửa cục bộ `api.py`, phải áp lại khi đồng bộ). Bản 0.1.x, một tác giả; có `docs/internal/` (kế hoạch, findings) lẫn trong repo. Tên mẫu trong catalog dễ nhầm với ComfyUI gốc và các MCP/skill ComfyUI khác. Chưa đọc mã executor, nên các tuyên bố an toàn (registry, kiểm đường dẫn) chưa kiểm ở mức mã.

**Cách tham khảo/tích hợp:** `pipx install comfyui-agent-skill-mie`, chạy `check`/`doctor` với máy chủ ComfyUI nội bộ; giữ máy chủ sau mạng tin cậy, ghim phiên bản gói và kiểm license model của từng workflow (model thường có license riêng, không thuộc Apache-2.0 của skill).

**Thay thế:** [ComfyUI](../19-agentic-video-media/README.md#3h-kiểm-ảnh-ai-video-stack-remotion-skills-blender-và-blender-mcp-faster-whisper-chatterbox-gsap-ảnh-người-dùng-gửi-đọc-mã-8112026), Pixelle-Video (mục 19), generative-media-skills (mục 19, API đám mây), [higgsfield-skills](../19-agentic-video-media/README.md#3f-hồ-sơ-higgsfield-aiskills-9-skill-gọi-cli-đóng-của-higgsfield-để-sinh-ảnh-video-brand-kit-và-train-soul-khuôn-mặt-ảnh-readme-người-dùng-gửi-đọc-mã-3112026).

**Bằng chứng:** `docs-read`, ngày 2026-11-23, commit [`b42d1076a7ae`](https://github.com/MieMieeeee/comfyui-agent-skill/commit/b42d1076a7ae4ea8084fe6580080aaaeb0610eeb) (commit ngày 2026-10-13). Đã đọc README, SKILL.md (phần mô tả và phạm vi sử dụng), VENDORING.md, CHANGELOG.md (0.1.11–0.1.14), `pyproject.toml`, workflow `ci.yml` (ma trận Ubuntu/Windows, Python 3.10/3.11, pytest), danh sách file và LICENSE tại commit này. Chưa đọc mã trong `scripts/comfyui/`, chưa chạy test, chưa kết nối ComfyUI; chưa kiểm bản PyPI khớp repo.

**Nguồn:** [README.md](https://github.com/MieMieeeee/comfyui-agent-skill/blob/b42d1076a7ae4ea8084fe6580080aaaeb0610eeb/README.md) · [SKILL.md](https://github.com/MieMieeeee/comfyui-agent-skill/blob/b42d1076a7ae4ea8084fe6580080aaaeb0610eeb/SKILL.md) · [VENDORING.md](https://github.com/MieMieeeee/comfyui-agent-skill/blob/b42d1076a7ae4ea8084fe6580080aaaeb0610eeb/VENDORING.md) · [CHANGELOG.md](https://github.com/MieMieeeee/comfyui-agent-skill/blob/b42d1076a7ae4ea8084fe6580080aaaeb0610eeb/CHANGELOG.md) · [.github/workflows/ci.yml](https://github.com/MieMieeeee/comfyui-agent-skill/blob/b42d1076a7ae4ea8084fe6580080aaaeb0610eeb/.github/workflows/ci.yml) · [LICENSE](https://github.com/MieMieeeee/comfyui-agent-skill/blob/b42d1076a7ae4ea8084fe6580080aaaeb0610eeb/LICENSE) · metadata GitHub: chưa xác minh (API trả 403 trong phiên).

<a id="xlsx-2026-11-23-youtube-agent-skill"></a>

### youtube-agent-skill (Jake Schincariol)

**Repo:** [Jakeschincariol/youtube-agent-skill](https://github.com/Jakeschincariol/youtube-agent-skill) · **License:** MIT (Copyright (c) 2026 Jake Schincariol) · **★ chưa xác minh (GitHub API không truy cập được trong phiên, 2026-11-23)**

**Mục đích:** Bộ 11 skill Claude cho người làm kênh YouTube (script, tiêu đề + thumbnail, EDL từ transcript, retention, chapters, Shorts, SEO, bình luận, kế hoạch tuần, audit) kèm 6 công cụ Python không phụ thuộc thư viện (v1.0.0).

**Giá trị và cơ chế:** Điểm khác biệt là phần kiểm bằng mã nhỏ: `hookscore.py` (bảng 5 thuộc tính cho hook, 21 công thức trong `hooks.json`), `title.py` (lint tiêu đề và thumbnail như một cặp), `deadair.py` (EDL từ SRT), `chapters.py` (kiểm luật chapter của YouTube), `retention.py` (đọc CSV retention), `swipe.py` (xếp hạng video theo bội số so với median của chính kênh, cần tối thiểu 4 video mỗi kênh). README ghi giới hạn thẳng: hookscore là heuristic hiệu chỉnh trên 74 hook, phân biệt hook tệ/thật tốt nhưng gần như không phân biệt hit/miss của cùng một người sáng tạo. Mọi skill kết thúc bằng khối để người dùng tự đăng, không tự xuất bản.

**Giới hạn:** Hiệu chỉnh trên 74 hook, năm kênh (tuyên bố của tác giả, chưa tái lập). `/yt-viral` cần người dùng tự thu thập dữ liệu (ví dụ `yt-dlp --flat-playlist`); xếp hạng dựa trên tiêu đề, không giải thích vì sao video thành công. Tệp `voice.md` do người dùng viết quyết định chất lượng. Không CI, không test (repo 24 file, mã Python tổng cộng khoảng 535 dòng). Một tác giả; chưa kiểm mã từng script bằng chạy thật.

**Cách tham khảo/tích hợp:** Sao chép `skills/yt-*` vào `~/.claude/skills/` hoặc `/plugin marketplace add Jakeschincariol/youtube-agent-skill`; điền `templates/voice.md`. Không cần khóa API nên rủi ro bí mật thấp; kết quả `swipe.py` chỉ phản ánh dữ liệu đầu vào người dùng đưa.

**Thay thế:** [claude-youtube](#xlsx-2026-11-23-claude-youtube), ai-youtube-shorts-generator (mục 19), last30days-skill (mục 08), social-media-research-skills (mục 19).

**Bằng chứng:** `docs-read`, ngày 2026-11-23, commit [`a2feb2104981`](https://github.com/Jakeschincariol/youtube-agent-skill/commit/a2feb2104981a375ffd4f87ee04f4f5344ac43c6) (commit ngày 2026-09-16). Đã đọc README, LICENSE, `plugin.json`, SKILL.md của `yt-viral`, đầu file và import của sáu script (grep không thấy `urlopen`/`requests`/`socket`/`subprocess` trong các script) tại commit này. Không có thư mục `.github`. Chưa chạy script nào, chưa đọc đủ logic chấm điểm; số 74 hook/21 công thức chưa kiểm.

**Nguồn:** [README.md](https://github.com/Jakeschincariol/youtube-agent-skill/blob/a2feb2104981a375ffd4f87ee04f4f5344ac43c6/README.md) · [skills/yt-viral/SKILL.md](https://github.com/Jakeschincariol/youtube-agent-skill/blob/a2feb2104981a375ffd4f87ee04f4f5344ac43c6/skills/yt-viral/SKILL.md) · [skills/yt-script/hookscore.py](https://github.com/Jakeschincariol/youtube-agent-skill/blob/a2feb2104981a375ffd4f87ee04f4f5344ac43c6/skills/yt-script/hookscore.py) · [skills/yt-viral/swipe.py](https://github.com/Jakeschincariol/youtube-agent-skill/blob/a2feb2104981a375ffd4f87ee04f4f5344ac43c6/skills/yt-viral/swipe.py) · [.claude-plugin/plugin.json](https://github.com/Jakeschincariol/youtube-agent-skill/blob/a2feb2104981a375ffd4f87ee04f4f5344ac43c6/.claude-plugin/plugin.json) · [LICENSE](https://github.com/Jakeschincariol/youtube-agent-skill/blob/a2feb2104981a375ffd4f87ee04f4f5344ac43c6/LICENSE) · metadata GitHub: chưa xác minh (API trả 403 trong phiên).

<a id="xlsx-2026-11-23-claude-youtube"></a>

### claude-youtube (AgriciDaniel)

**Repo:** [AgriciDaniel/claude-youtube](https://github.com/AgriciDaniel/claude-youtube) · **License:** MIT (Copyright (c) 2025 Daniel Agrici) · **★ chưa xác minh (GitHub API không truy cập được trong phiên, 2026-11-23)**

**Mục đích:** Skill 'cố vấn tăng trưởng YouTube' cho Claude Code: orchestrator `SKILL.md` điều tới 14 sub-skill (audit, SEO, script, hook, thumbnail, strategy, calendar, shorts, analyze, repurpose, monetize, competitor, metadata, ideate), 9 hướng dẫn tham chiếu, 9 mẫu theo loại kênh và 6 script Python gọi YouTube Data/Analytics API (bản 0.1.0, README ghi Beta).

**Giá trị và cơ chế:** Cấu trúc 3 lớp rõ (router + sub-skill + references, tải theo nhu cầu); script tách riêng xác thực khóa API/OAuth (`youtube_auth.py`), bộ đếm quota 10.000 đơn vị/ngày (`quota_tracker.py`) và lấy transcript qua `yt-dlp` nếu có. Cùng tác giả với claude-seo nên dùng chung mô hình orchestrator/sub-skill.

**Giới hạn:** Phần lớn là lời khuyên dạng markdown (README ghi hơn 5.300 dòng) với benchmark, tỷ lệ CTR/RPM nêu trong guide không kèm nguồn kiểm được (chưa xác minh). Cần khóa YouTube Data API hoặc OAuth client secrets cho dữ liệu thật; token OAuth lưu ở `~/.claude/.tmp/youtube_oauth_token.json` (đọc từ mã `youtube_auth.py`). `SKILL.md` khai báo công cụ rộng (Bash, WebSearch, Write, Agent). Cài đặt khuyến nghị dùng `curl | bash`; `install.sh` đọc được chỉ clone nông và chép file vào `~/.claude/skills/youtube`. Không có CI; commit cuối 2026-04-10, bản 0.1.0 (Beta), nên có thể đã tụt so với thay đổi chính sách YouTube.

**Cách tham khảo/tích hợp:** Cài bằng cách tự đọc rồi chép `skills/claude-youtube/` vào `~/.claude/skills/youtube` thay vì pipe vào shell; nếu cần dữ liệu riêng, tạo OAuth client riêng với phạm vi chỉ đọc và bảo vệ token. Kiểm lại các con số benchmark trước khi đưa vào quyết định.

**Thay thế:** [youtube-agent-skill](#xlsx-2026-11-23-youtube-agent-skill), [claude-seo](../20-claude-plugins-ecosystem/README.md#3z-hồ-sơ-agricidanielclaude-seo-claude-seo-plugin-audit-seo-và-geo-cho-claude-code-26-skill--19-agent--1077-test-ảnh-readme-người-dùng-gửi-đọc-mã-5112026), ai-youtube-shorts-generator (mục 19), [BrowserAct youtube-api-skill](#xlsx-2026-11-23-browser-act-youtube-api-skill).

**Bằng chứng:** `code-read`, ngày 2026-11-23, commit [`84c3fa680520`](https://github.com/AgriciDaniel/claude-youtube/commit/84c3fa6805200632fadb4fe2795ef265511271c7) (commit ngày 2026-04-10). Đã đọc README, SKILL.md (router), `plugin.json`, `install.sh`, SECURITY.md, `execution/utils/youtube_auth.py` (khóa từ `YOUTUBE_API_KEY` hoặc `~/.claude/youtube-credentials.json`, đường dẫn token OAuth), đầu `quota_tracker.py` và `fetch_transcript.py`, LICENSE tại commit này. Không có `.github/workflows`. Chưa đọc đủ bốn script `fetch_*`/`search_*`, chưa chạy script, chưa kiểm số benchmark trong guide.

**Nguồn:** [README.md](https://github.com/AgriciDaniel/claude-youtube/blob/84c3fa6805200632fadb4fe2795ef265511271c7/README.md) · [skills/claude-youtube/SKILL.md](https://github.com/AgriciDaniel/claude-youtube/blob/84c3fa6805200632fadb4fe2795ef265511271c7/skills/claude-youtube/SKILL.md) · [skills/claude-youtube/execution/utils/youtube_auth.py](https://github.com/AgriciDaniel/claude-youtube/blob/84c3fa6805200632fadb4fe2795ef265511271c7/skills/claude-youtube/execution/utils/youtube_auth.py) · [install.sh](https://github.com/AgriciDaniel/claude-youtube/blob/84c3fa6805200632fadb4fe2795ef265511271c7/install.sh) · [SECURITY.md](https://github.com/AgriciDaniel/claude-youtube/blob/84c3fa6805200632fadb4fe2795ef265511271c7/SECURITY.md) · [LICENSE](https://github.com/AgriciDaniel/claude-youtube/blob/84c3fa6805200632fadb4fe2795ef265511271c7/LICENSE) · metadata GitHub: chưa xác minh (API trả 403 trong phiên).

<a id="xlsx-2026-11-23-browser-act-youtube-api-skill"></a>

### BrowserAct youtube-api-skill (browser-act/skills)

**Repo:** [browser-act/skills](https://github.com/browser-act/skills) · **License:** MIT (Copyright (c) 2026 BrowserAct); dịch vụ BrowserAct đám mây là sản phẩm riêng, điều khoản riêng · **★ chưa xác minh (GitHub API không truy cập được trong phiên, 2026-11-23)**

**Mục đích:** Phạm vi đọc: `solutions/video-platforms/youtube-api-skill`, một skill gọi workflow-template của dịch vụ BrowserAct để lấy số liệu video/kênh YouTube theo từ khóa và bộ lọc ngày tải lên. Repo `browser-act/skills` chứa 103 SKILL.md: skill CLI trình duyệt `browser-act`, `browser-act-skill-forge` và thư mục `solutions/` (thương mại điện tử, lead generation, social listening, video-platforms...).

**Giá trị và cơ chế:** Một script `youtube_api.py` (106 dòng): đọc `BROWSERACT_API_KEY` từ môi trường, POST `run-task-by-template` tới `api.browseract.com/v2/workflow` với template ID cố định, poll trạng thái mỗi 10 giây tối đa 300 giây rồi in kết quả (tiêu đề, kênh, subscriber, view, like, comment, thời lượng). SKILL.md quy định agent không làm gì khác trước khi người dùng cung cấp khóa, chỉ retry một lần và không retry khi 'Invalid authorization'. Có timeout tổng và timeout từng request, khác nhiều skill gọi API khác.

**Giới hạn:** Không thay YouTube Data API: dữ liệu do dịch vụ đám mây của bên thứ ba cào về, **từ khóa tìm kiếm gửi sang BrowserAct**, tính phí theo tài khoản BrowserAct (chưa xác minh giá), khóa API bắt buộc. Việc cào trang YouTube có thể mâu thuẫn điều khoản dịch vụ của YouTube (chưa xác minh, cần rà pháp lý của dự án chủ). Các tuyên bố 'không hallucination', 'không CAPTCHA', 'rẻ hơn AI thuần' trong SKILL.md là quảng cáo của nhà cung cấp, chưa kiểm. Mã trong repo chỉ là client; logic cào nằm trong template đóng ở phía dịch vụ nên không đọc được. CI của repo chỉ đồng bộ thư mục sang repo plugin và hoạt động cộng đồng, không kiểm skill.

**Cách tham khảo/tích hợp:** Nếu chỉ cần số liệu YouTube hợp lệ, ưu tiên YouTube Data API chính thức. Dùng skill này khi chấp nhận phụ thuộc BrowserAct: lưu khóa trong secret manager, ghim commit, kiểm điều khoản và chi phí, không gửi từ khóa nhạy cảm. Skill CLI `browser-act` cài `uv tool install browser-act-cli` (tải gói PyPI ngoài), cần xem xét riêng.

**Thay thế:** [yt-dlp](../19-agentic-video-media/README.md#3h-kiểm-ảnh-ai-video-stack-remotion-skills-blender-và-blender-mcp-faster-whisper-chatterbox-gsap-ảnh-người-dùng-gửi-đọc-mã-8112026), [claude-youtube](#xlsx-2026-11-23-claude-youtube) (YouTube Data API trực tiếp), social-media-research-skills (mục 19), last30days-skill (mục 08).

**Bằng chứng:** `code-read`, ngày 2026-11-23, commit [`593316aa0f8c`](https://github.com/browser-act/skills/commit/593316aa0f8ccd88bdf745c92b24a50641701973) (commit ngày 2026-11-04). Đã đọc README repo, `solutions/video-platforms/youtube-api-skill/SKILL.md` và toàn bộ `scripts/youtube_api.py`, đầu `browser-act/SKILL.md` (metadata quyền, cài đặt), `docs/installation.md`, workflow `sync-browser-act.yml`, LICENSE tại commit này. Chỉ phạm vi skill YouTube này; chưa đọc 100+ skill còn lại, chưa gọi API BrowserAct, chưa chạy script; template phía dịch vụ không truy cập được.

**Nguồn:** [solutions/video-platforms/youtube-api-skill/SKILL.md](https://github.com/browser-act/skills/blob/593316aa0f8ccd88bdf745c92b24a50641701973/solutions/video-platforms/youtube-api-skill/SKILL.md) · [solutions/video-platforms/youtube-api-skill/scripts/youtube_api.py](https://github.com/browser-act/skills/blob/593316aa0f8ccd88bdf745c92b24a50641701973/solutions/video-platforms/youtube-api-skill/scripts/youtube_api.py) · [browser-act/SKILL.md](https://github.com/browser-act/skills/blob/593316aa0f8ccd88bdf745c92b24a50641701973/browser-act/SKILL.md) · [README.md](https://github.com/browser-act/skills/blob/593316aa0f8ccd88bdf745c92b24a50641701973/README.md) · [.github/workflows/sync-browser-act.yml](https://github.com/browser-act/skills/blob/593316aa0f8ccd88bdf745c92b24a50641701973/.github/workflows/sync-browser-act.yml) · [LICENSE](https://github.com/browser-act/skills/blob/593316aa0f8ccd88bdf745c92b24a50641701973/LICENSE) · metadata GitHub: chưa xác minh (API trả 403 trong phiên).

<a id="chuan-hoa-2026-11-23"></a>

## Chuẩn hóa bằng chứng hồ sơ cũ — 23/11/2026

Các hồ sơ dưới đây có từ trước khi kho ghi mức kiểm. Ngày 2026-11-23 mỗi repo được clone nông tại commit ghi trong bảng, đọc LICENSE, README, manifest và CI (nếu có); không cài, build hay chạy mã upstream. Nhận định cũ ở phần trên giữ nguyên; chỗ nào khác với lần đọc này được ghi trong cột Nhận định. Số sao lấy qua GitHub search API cùng ngày.

<a id="ch-ai-youtube-shorts-generator"></a>

### AI YouTube Shorts Generator

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/Anil-matcha/AI-Youtube-Shorts-Generator |
| License | MIT |
| Phiên bản đã đọc | `8c9ac3103a137e53669aeebfc2af8dbdd810c35a` (commit 2026-11-21) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README, LICENSE, requirements.txt; chưa chạy upstream |
| Bảo trì | commit 21/11/2026; không có workflow CI; chỉ thấy requirements.txt tối thiểu (requests, python-dotenv) |
| Nhận định | CLI đổi video YouTube dài thành các Shorts 9:16: LLM chọn đoạn nổi bật, Whisper phiên âm, cắt khung dọc. Mã tách module `shorts_generator/` (downloader, transcriber, highlights, clipper, muapi). Giới hạn: mặc định phụ thuộc dịch vụ MuAPI trả phí; tuyên bố "miễn phí, không giới hạn" của README chỉ đúng khi tự chịu chi phí API **(chưa xác minh)**; không có test/CI. |
| Nguồn | [README.md](https://github.com/Anil-matcha/AI-Youtube-Shorts-Generator/blob/8c9ac3103a137e53669aeebfc2af8dbdd810c35a/README.md) · [LICENSE](https://github.com/Anil-matcha/AI-Youtube-Shorts-Generator/blob/8c9ac3103a137e53669aeebfc2af8dbdd810c35a/LICENSE) · [requirements.txt](https://github.com/Anil-matcha/AI-Youtube-Shorts-Generator/blob/8c9ac3103a137e53669aeebfc2af8dbdd810c35a/requirements.txt) |

<a id="ch-auto-compare-video"></a>

### auto-compare-video

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/Cuongyd196/auto-compare-video |
| License | MIT |
| Phiên bản đã đọc | `50b1f34a7b1fdf309695ca4391bb8fd805d05b24` (commit 2026-09-24) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.EN.md (bản dịch tiếng Anh của README.md tiếng Việt; phần License cũng đối chiếu README.md), LICENSE; chưa chạy upstream |
| Bảo trì | commit 24/9/2026; không có workflow CI; không có package.json ở gốc (mỗi video là một thư mục con) |
| Nhận định | Mẫu video ngắn "A vs B" với bố cục cố định 3 phần (hai thẻ minh họa, phụ đề chạy, robot MC 2D), dựng bằng HyperFrames, hướng dẫn qua skill cho Claude Code. Điểm tham khảo: DESIGN.md chuẩn hóa bố cục để agent chỉ thay nội dung. Giới hạn: không có bước kiểm chứng nội dung hay CI; lỗi lệch tiếng ở video mẫu trong ghi chú cũ là quan sát riêng của kho **(chưa tái kiểm ở lần này)**. |
| Nguồn | [README.EN.md](https://github.com/Cuongyd196/auto-compare-video/blob/50b1f34a7b1fdf309695ca4391bb8fd805d05b24/README.EN.md) · [LICENSE](https://github.com/Cuongyd196/auto-compare-video/blob/50b1f34a7b1fdf309695ca4391bb8fd805d05b24/LICENSE) |

<a id="ch-auto-create-video"></a>

### Auto-Create-Video

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/hoquanghai/Auto-Create-Video |
| License | MIT |
| Phiên bản đã đọc | `8c2e04337ca7fb574692c5830dafde35ac2017cd` (commit 2026-05-02) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README, LICENSE, package.json, test.yml, typecheck.yml; chưa chạy upstream |
| Bảo trì | commit cuối 2/5/2026 (~6,5 tháng); có CI test.yml (npm ci, vitest) và typecheck.yml (tsc --noEmit) |
| Nhận định | Pipeline TypeScript biến bài báo công nghệ tiếng Việt (URL/txt) thành video 9:16 bằng Claude Code skill + HyperFrames + GSAP, TTS LucyLab/ElevenLabs. Có vitest và typecheck chạy trên CI. Giới hạn: phụ thuộc khóa TTS trả phí, đã đứng yên từ đầu tháng 5; tuyên bố "60 giây, chi phí ~0,1 USD" của README **(chưa xác minh)**. |
| Nguồn | [README.md](https://github.com/hoquanghai/Auto-Create-Video/blob/8c2e04337ca7fb574692c5830dafde35ac2017cd/README.md) · [LICENSE](https://github.com/hoquanghai/Auto-Create-Video/blob/8c2e04337ca7fb574692c5830dafde35ac2017cd/LICENSE) · [package.json](https://github.com/hoquanghai/Auto-Create-Video/blob/8c2e04337ca7fb574692c5830dafde35ac2017cd/package.json) · [test.yml](https://github.com/hoquanghai/Auto-Create-Video/blob/8c2e04337ca7fb574692c5830dafde35ac2017cd/.github/workflows/test.yml) · [typecheck.yml](https://github.com/hoquanghai/Auto-Create-Video/blob/8c2e04337ca7fb574692c5830dafde35ac2017cd/.github/workflows/typecheck.yml) |

<a id="ch-auto-video-gen-cuongit"></a>

### auto-video-gen (CuongIT)

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/Cuongyd196/auto-video-gen |
| License | MIT |
| Phiên bản đã đọc | `86cda98a59b1126bd5e95b6839e87ee67b9fd396` (commit 2026-09-28) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.en.md (bản dịch tiếng Anh của README.md tiếng Việt; phần License đối chiếu README.md), LICENSE; chưa chạy upstream |
| Bảo trì | commit 28/9/2026; không có workflow CI |
| Nhận định | Biến bài viết tiếng Việt hoặc URL repo GitHub thành video 9:16 (HyperFrames + GSAP + TTS), cùng cây thư mục và pipeline với Auto-Create-Video của hoquanghai, thêm Vbee và theme. Giới hạn: không có workflow CI; cần xem kỹ quyền dùng ảnh/og:image của báo khi đăng. |
| Nguồn | [README.en.md](https://github.com/Cuongyd196/auto-video-gen/blob/86cda98a59b1126bd5e95b6839e87ee67b9fd396/README.en.md) · [LICENSE](https://github.com/Cuongyd196/auto-video-gen/blob/86cda98a59b1126bd5e95b6839e87ee67b9fd396/LICENSE) |

<a id="ch-awesome-claude-video-skills"></a>

### awesome-claude-video-skills

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/zhuyansen/awesome-claude-video-skills |
| License | CC0-1.0 (khác catalog cũ) |
| Phiên bản đã đọc | `93fc8b8485a845d55b6d36c6c40f74f960642130` (commit 2026-11-22) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README, LICENSE; chưa chạy upstream |
| Bảo trì | commit 22/11/2026 ("Daily update"), danh sách tự cập nhật hằng ngày |
| Nhận định | Danh sách tuyển chọn ~540 repo/skill giúp agent làm video (HyperFrames, Remotion, motion graphics...), kèm điểm an toàn do Agent Skills Hub chấm và mục "đã chạy thử 16 repo". Hữu ích để dò nhanh hệ sinh thái; xếp hạng và điểm an toàn là của nhà duy trì **(chưa xác minh)**. |
| Nguồn | [README.md](https://github.com/zhuyansen/awesome-claude-video-skills/blob/93fc8b8485a845d55b6d36c6c40f74f960642130/README.md) · [LICENSE](https://github.com/zhuyansen/awesome-claude-video-skills/blob/93fc8b8485a845d55b6d36c6c40f74f960642130/LICENSE) |

<a id="ch-c2pa-specifications"></a>

### C2PA Specifications

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/c2pa-org/specifications |
| License | CC-BY-4.0 |
| Phiên bản đã đọc | `05dbf10bbd362c0f5ec1d2108f6745dfe9cb8669` (commit 2026-11-16) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README, LICENSE, publish.yml; chưa chạy upstream |
| Bảo trì | commit 16/11/2026; workflow publish.yml đẩy site lên GitHub Pages |
| Nhận định | Kho nguồn site đặc tả C2PA (xác thực nguồn gốc nội dung) dựng bằng Antora, có danh sách thuật toán soft-binding. README chủ yếu hướng dẫn build site; nội dung đặc tả nằm trong `docs/` và trên site spec.c2pa.org, chưa đọc nội dung đặc tả trong lần này. |
| Nguồn | [README.md](https://github.com/c2pa-org/specifications/blob/05dbf10bbd362c0f5ec1d2108f6745dfe9cb8669/README.md) · [LICENSE](https://github.com/c2pa-org/specifications/blob/05dbf10bbd362c0f5ec1d2108f6745dfe9cb8669/LICENSE) · [publish.yml](https://github.com/c2pa-org/specifications/blob/05dbf10bbd362c0f5ec1d2108f6745dfe9cb8669/.github/workflows/publish.yml) |

<a id="ch-cit-voice-studio"></a>

### CIT Voice Studio

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/Cuongyd196/cit-voice-studio |
| License | Apache-2.0 (khác catalog cũ) |
| Phiên bản đã đọc | `6fc8d14985b157a629392faa83c8db418d2af5ab` (commit 2026-11-12) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README (tiếng Việt, phần giới thiệu và license), LICENSE; chưa chạy upstream |
| Bảo trì | commit 12/11/2026; có ci.yml, build-linux.yml, build-macos.yml (chưa mở) |
| Nhận định | Ứng dụng TTS tiếng Việt chạy cục bộ (25 giọng, nhân bản giọng, lồng tiếng theo .srt, API cục bộ cổng 8001, bản desktop). Mã mở Apache-2.0 nhưng mô hình đi kèm có license riêng (OpenRAIL-M) cần kiểm khi dùng thương mại; chất lượng "ngang mô hình lớn hơn nhiều lần" là lời nhà cung cấp **(chưa xác minh)**. |
| Nguồn | [README.md](https://github.com/Cuongyd196/cit-voice-studio/blob/6fc8d14985b157a629392faa83c8db418d2af5ab/README.md) · [LICENSE](https://github.com/Cuongyd196/cit-voice-studio/blob/6fc8d14985b157a629392faa83c8db418d2af5ab/LICENSE) |

<a id="ch-claude-video-watch"></a>

### claude-video (/watch)

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/bradautomates/claude-video |
| License | MIT |
| Phiên bản đã đọc | `03ceb42f7fa2c4439aca01752118044baabffb8f` (commit 2026-09-25) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README, LICENSE, tests.yml, release.yml; chưa chạy upstream |
| Bảo trì | commit 25/9/2026 (release 0.3.2); có tests.yml (ma trận Ubuntu/macOS/Windows) và release.yml |
| Nhận định | Skill/plugin "/watch": biến URL hoặc file video thành khung hình có mốc thời gian + transcript (ưu tiên phụ đề gốc, tùy chọn WhisperX cục bộ hoặc Groq/OpenAI). Có test đa hệ điều hành và quy trình release; dùng Groq/OpenAI thì dữ liệu rời máy. |
| Nguồn | [README.md](https://github.com/bradautomates/claude-video/blob/03ceb42f7fa2c4439aca01752118044baabffb8f/README.md) · [LICENSE](https://github.com/bradautomates/claude-video/blob/03ceb42f7fa2c4439aca01752118044baabffb8f/LICENSE) · [tests.yml](https://github.com/bradautomates/claude-video/blob/03ceb42f7fa2c4439aca01752118044baabffb8f/.github/workflows/tests.yml) · [release.yml](https://github.com/bradautomates/claude-video/blob/03ceb42f7fa2c4439aca01752118044baabffb8f/.github/workflows/release.yml) |

<a id="ch-cogvideox"></a>

### CogVideoX

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/zai-org/CogVideo |
| License | Apache-2.0 (code); mô hình CogVideoX-5B theo CogVideoX LICENSE riêng (khác catalog cũ) |
| Phiên bản đã đọc | `7a1af7154511e0ce4e4be8d62faa8c5e5a3532d2` (commit 2025-11-04) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README, LICENSE, MODEL_LICENSE; chưa chạy upstream |
| Bảo trì | commit cuối 4/11/2025 ("update readme", ~1 năm); mục tin README dừng ở đầu 2025; không có CI |
| Nhận định | Mã suy luận/tinh chỉnh (diffusers, SAT, LoRA) cho họ mô hình sinh video CogVideoX, kèm CLI demo và DDIM inversion. Giới hạn: license mô hình khác code, repo đứng yên khoảng một năm và README chỉ sang CogKit; cần GPU lớn. |
| Nguồn | [README.md](https://github.com/zai-org/CogVideo/blob/7a1af7154511e0ce4e4be8d62faa8c5e5a3532d2/README.md) · [LICENSE](https://github.com/zai-org/CogVideo/blob/7a1af7154511e0ce4e4be8d62faa8c5e5a3532d2/LICENSE) · [MODEL_LICENSE](https://github.com/zai-org/CogVideo/blob/7a1af7154511e0ce4e4be8d62faa8c5e5a3532d2/MODEL_LICENSE) |

<a id="ch-crucix"></a>

### Crucix

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/calesthio/Crucix |
| License | AGPL-3.0 (khác catalog cũ) |
| Phiên bản đã đọc | `3db7068817e0c815df353fa0f19657c85142789d` (commit 2026-05-19) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README, LICENSE, package.json; chưa chạy upstream |
| Bảo trì | commit cuối 19/5/2026 (~6 tháng); có docker-publish.yml; package.json v2.0.0 |
| Nhận định | Ứng dụng Node tự chạy gom 27 nguồn dữ liệu mở (cháy vệ tinh, chuyến bay, bức xạ, thị trường, xung đột...) mỗi 15 phút lên bảng điều khiển kiểu "Jarvis", có thể nối LLM để cảnh báo qua Telegram/Discord. Rủi ro: AGPL-3.0 buộc mở mã khi cung cấp qua mạng; "không telemetry" là tuyên bố của tác giả **(chưa xác minh)**; không liên quan trực tiếp tới dựng video. |
| Nguồn | [README.md](https://github.com/calesthio/Crucix/blob/3db7068817e0c815df353fa0f19657c85142789d/README.md) · [LICENSE](https://github.com/calesthio/Crucix/blob/3db7068817e0c815df353fa0f19657c85142789d/LICENSE) · [package.json](https://github.com/calesthio/Crucix/blob/3db7068817e0c815df353fa0f19657c85142789d/package.json) |

<a id="ch-ebu-r-128-itu-r-bs-1770"></a>

### EBU R 128 / ITU-R BS.1770

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://tech.ebu.ch/publications/r128 (trang 403 với curl; đã đọc PDF https://tech.ebu.ch/docs/r/r128.pdf) |
| License | Không có file license; tài liệu khuyến nghị của EBU (EBU Recommendation) |
| Phiên bản đã đọc | EBU R 128-2023 (v5, tháng 11/2023); không áp dụng SHA |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc r128.pdf; chưa chạy upstream |
| Bảo trì | Chưa rõ (bản sửa đổi gần nhất đọc được là 11/2023) |
| Nhận định | Khuyến nghị chuẩn hóa loudness theo chương trình ở -23,0 LUFS (dung sai ±0,5 LU, ±1,0 LU cho chương trình trực tiếp) và true peak không quá -1 dBTP, đo bằng máy đo theo ITU-R BS.1770 và EBU Tech 3341. Đây là mục tiêu cho phát sóng, các nền tảng streaming dùng mục tiêu khác. |
| Nguồn | [R 128 PDF](https://tech.ebu.ch/docs/r/r128.pdf) |

<a id="ch-ffmpeg-quality-metrics"></a>

### ffmpeg-quality-metrics

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/slhck/ffmpeg-quality-metrics |
| License | MIT |
| Phiên bản đã đọc | `e4aafcb575fb9feeb36c960ef38e997278d6c817` (commit 2026-10-25) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README, LICENSE.md, pyproject.toml; chưa chạy upstream |
| Bảo trì | commit 25/10/2026; có python-package.yml, docker-push.yml, auto-update-ffmpeg.yml (chưa mở); pyproject v3.13.0 |
| Nhận định | Công cụ Python gọi FFmpeg tính PSNR, SSIM, VIF, MSAD, VMAF theo từng khung và thống kê toàn video, có GUI xem kết quả trên trình duyệt. Dùng tốt làm bước đo chất lượng sau khi sinh/nén video; chạy cần FFmpeg bản mới. |
| Nguồn | [README.md](https://github.com/slhck/ffmpeg-quality-metrics/blob/e4aafcb575fb9feeb36c960ef38e997278d6c817/README.md) · [LICENSE.md](https://github.com/slhck/ffmpeg-quality-metrics/blob/e4aafcb575fb9feeb36c960ef38e997278d6c817/LICENSE.md) · [pyproject.toml](https://github.com/slhck/ffmpeg-quality-metrics/blob/e4aafcb575fb9feeb36c960ef38e997278d6c817/pyproject.toml) |

<a id="ch-generative-media-skills"></a>

### generative-media-skills

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/calesthio/generative-media-skills |
| License | MIT (khác catalog cũ) |
| Phiên bản đã đọc | `8c85352d5d75d4dcbe58480bd138e37b9742bab1` (commit 2026-07-14) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README, LICENSE; chưa chạy upstream |
| Bảo trì | commit 14/7/2026 (~4 tháng); không có workflow CI; có thư mục tests/ |
| Nhận định | Bộ 150+ skill chia 25 nhóm cho agent làm ảnh, video, âm thanh, giọng, nhạc, 3D, avatar, kèm kiểm tra kỹ thuật; có file hướng dẫn riêng cho nhiều host (CLAUDE.md, GEMINI.md, OPENCLAW.md...). Số lượng và mức "research-backed" là tuyên bố của tác giả **(chưa xác minh)**. |
| Nguồn | [README.md](https://github.com/calesthio/generative-media-skills/blob/8c85352d5d75d4dcbe58480bd138e37b9742bab1/README.md) · [LICENSE](https://github.com/calesthio/generative-media-skills/blob/8c85352d5d75d4dcbe58480bd138e37b9742bab1/LICENSE) |

<a id="ch-hunyuanvideo"></a>

### HunyuanVideo

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/Tencent-Hunyuan/HunyuanVideo |
| License | Tencent Hunyuan Community License (không áp dụng tại EU, UK, Hàn Quốc) |
| Phiên bản đã đọc | `4eda9cb44c3be82a6b9c4261897cb6bd3cfb084e` (commit 2026-10-08) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README, LICENSE.txt, Notice; chưa chạy upstream |
| Bảo trì | commit 8/10/2026 chỉ chỉnh tài liệu cài đặt; mục tin README dừng ở 11/2025 và hướng sang HunyuanVideo-1.5; không có CI |
| Nhận định | Mã mô hình, trọng số và suy luận của HunyuanVideo gốc (PyTorch, gradio_server.py, sample_video.py). Giới hạn: license cộng đồng có hạn chế lãnh thổ, repo gần như chỉ còn sửa tài liệu và đã có bản kế nhiệm 1.5; cần GPU rất lớn. |
| Nguồn | [README.md](https://github.com/Tencent-Hunyuan/HunyuanVideo/blob/4eda9cb44c3be82a6b9c4261897cb6bd3cfb084e/README.md) · [LICENSE.txt](https://github.com/Tencent-Hunyuan/HunyuanVideo/blob/4eda9cb44c3be82a6b9c4261897cb6bd3cfb084e/LICENSE.txt) · [Notice](https://github.com/Tencent-Hunyuan/HunyuanVideo/blob/4eda9cb44c3be82a6b9c4261897cb6bd3cfb084e/Notice) |

<a id="ch-hypit"></a>

### Hypit

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/hypit-ai/hypit |
| License | Hypit Open Source License (Apache-2.0 sửa đổi, cấm SaaS/bán lại) |
| Phiên bản đã đọc | `9a6f688c39829857d50dc596fa1218565585a9da` (commit 2026-11-16) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README, LICENSE, package.json; chưa chạy upstream |
| Bảo trì | commit 16/11/2026, nhiều workflow (ci.yml, publish-npm.yml...; chưa mở); package.json v0.3.3 |
| Nhận định | Hệ thống cho agent dựng video bằng ngôn ngữ SVML (mốc theo từ thay vì theo giây), cài qua `npx skills add`, có thể nhân bản video mẫu thành workflow hoặc dựng từ mô tả. Không phải Apache-2.0 thuần nên cần đọc kỹ điều kiện thương mại; README không bàn về đồng ý/deepfake khi clone video. |
| Nguồn | [README.md](https://github.com/hypit-ai/hypit/blob/9a6f688c39829857d50dc596fa1218565585a9da/README.md) · [LICENSE](https://github.com/hypit-ai/hypit/blob/9a6f688c39829857d50dc596fa1218565585a9da/LICENSE) · [package.json](https://github.com/hypit-ai/hypit/blob/9a6f688c39829857d50dc596fa1218565585a9da/package.json) |

<a id="ch-localminidrama"></a>

### LocalMiniDrama

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/xuanyustudio/LocalMiniDrama |
| License | MIT |
| Phiên bản đã đọc | `2335879a40f4349003217c957798401f2cb7910b` (commit 2026-11-22) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README, LICENSE, release.yml; chưa chạy upstream |
| Bảo trì | commit 22/11/2026; release.yml build bộ cài (chưa đọc hết); CHANGELOG, README nêu v1.2.9 |
| Nhận định | Ứng dụng desktop/web làm phim ngắn AI: kịch bản, nhân vật, cảnh, storyboard đến ghép video, hỗ trợ nhiều nhà cung cấp (Tongyi, Volcengine, Kling, Gemini, Vidu...), có chế độ canvas. README tiếng Trung; "dữ liệu không lên mây" áp dụng cho dữ liệu app, còn API model bên thứ ba vẫn nhận nội dung gửi đi. |
| Nguồn | [README.md](https://github.com/xuanyustudio/LocalMiniDrama/blob/2335879a40f4349003217c957798401f2cb7910b/README.md) · [LICENSE](https://github.com/xuanyustudio/LocalMiniDrama/blob/2335879a40f4349003217c957798401f2cb7910b/LICENSE) · [release.yml](https://github.com/xuanyustudio/LocalMiniDrama/blob/2335879a40f4349003217c957798401f2cb7910b/.github/workflows/release.yml) |

<a id="ch-moneyprinterturbo"></a>

### MoneyPrinterTurbo

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/harry0703/MoneyPrinterTurbo |
| License | MIT |
| Phiên bản đã đọc | `3482168e8958a73c48656634c750a5ce459224df` (commit 2026-11-23) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README (tiếng Trung), LICENSE, pyproject.toml, ci.yml, security.yml; chưa chạy upstream |
| Bảo trì | commit 23/11/2026 (release v1.3.11); CI thật ci.yml (pytest trên Python 3.11/3.13, Redis), security.yml (Trivy), docker-ghcr.yml |
| Nhận định | Pipeline Python (WebUI, API, CLI) tạo video ngắn từ chủ đề: viết kịch bản bằng LLM, lấy footage, TTS, phụ đề, nhạc rồi xuất MP4. Điểm đáng tham khảo: có test và CI bảo mật. Rủi ro: phụ thuộc nhiều dịch vụ bên thứ ba và khóa API; README quảng cáo tài trợ. |
| Nguồn | [README.md](https://github.com/harry0703/MoneyPrinterTurbo/blob/3482168e8958a73c48656634c750a5ce459224df/README.md) · [LICENSE](https://github.com/harry0703/MoneyPrinterTurbo/blob/3482168e8958a73c48656634c750a5ce459224df/LICENSE) · [pyproject.toml](https://github.com/harry0703/MoneyPrinterTurbo/blob/3482168e8958a73c48656634c750a5ce459224df/pyproject.toml) · [ci.yml](https://github.com/harry0703/MoneyPrinterTurbo/blob/3482168e8958a73c48656634c750a5ce459224df/.github/workflows/ci.yml) · [security.yml](https://github.com/harry0703/MoneyPrinterTurbo/blob/3482168e8958a73c48656634c750a5ce459224df/.github/workflows/security.yml) |

<a id="ch-open-sora"></a>

### Open-Sora

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/hpcaitech/Open-Sora |
| License | Apache-2.0 |
| Phiên bản đã đọc | `7ad6a96a135feb81f755c84fb391818718f6beb2` (commit 2026-04-09) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README, LICENSE, close_issue.yaml; chưa chạy upstream |
| Bảo trì | commit cuối 9/4/2026 (~7,5 tháng, sửa README); workflow chỉ đóng issue cũ và github_page |
| Nhận định | Mã và checkpoint mô hình sinh video Open-Sora (1.3 và 2.0 11B), có cấu hình huấn luyện/suy luận và gradio demo. Giới hạn: repo đứng yên nhiều tháng, cần GPU lớn; kết quả so sánh VBench trong README là tuyên bố của tác giả **(chưa xác minh)**. |
| Nguồn | [README.md](https://github.com/hpcaitech/Open-Sora/blob/7ad6a96a135feb81f755c84fb391818718f6beb2/README.md) · [LICENSE](https://github.com/hpcaitech/Open-Sora/blob/7ad6a96a135feb81f755c84fb391818718f6beb2/LICENSE) · [close_issue.yaml](https://github.com/hpcaitech/Open-Sora/blob/7ad6a96a135feb81f755c84fb391818718f6beb2/.github/workflows/close_issue.yaml) |

<a id="ch-opencreator-ten-cu-krillinai"></a>

### OpenCreator (tên cũ KrillinAI)

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/krillinai/OpenCreator |
| License | Apache-2.0 |
| Phiên bản đã đọc | `55a9db9c0643ab18717e0f2259b03c32867d33c1` (commit 2026-11-23) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README, LICENSE; chưa chạy upstream |
| Bảo trì | commit 23/11/2026 (chuẩn bị v3.3.4); có ci.yml, desktop-release.yml |
| Nhận định | Không gian làm việc cục bộ cho sáng tạo và lập trình dùng Codex CLI làm động cơ agent, gồm Runtime, giao diện trực quan và bản Desktop; có công cụ dịch/tải video, sinh ảnh/video, giọng đọc, viết bài. Phụ thuộc Codex CLI; khẩu hiệu "hệ sản xuất video agentic mã mở đầu tiên" là tuyên bố tiếp thị **(chưa xác minh)**. |
| Nguồn | [README.md](https://github.com/krillinai/OpenCreator/blob/55a9db9c0643ab18717e0f2259b03c32867d33c1/README.md) · [LICENSE](https://github.com/krillinai/OpenCreator/blob/55a9db9c0643ab18717e0f2259b03c32867d33c1/LICENSE) |

<a id="ch-palmier-pro"></a>

### Palmier Pro

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/palmier-io/palmier-pro |
| License | GPL-3.0 (mã nguồn đã công bố đến v0.7.6); bản nhị phân sau đó độc quyền (BINARY_LICENSE.md) |
| Phiên bản đã đọc | `7a140c15ca628a8aa67bb5aaae7c6994474f73b9` (commit 2026-11-20) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README, LICENSE, BINARY_LICENSE.md; chưa chạy upstream |
| Bảo trì | commit 20/11/2026 (xuất bản appcast v1.0.0-beta.4); repo nay chủ yếu lưu mã lịch sử và phát hành bản nhị phân |
| Nhận định | Trình dựng video native cho macOS (Swift, Apple Silicon, macOS 26) có sinh AI và MCP để agent thao tác timeline. Điểm cần lưu ý: GPL-3.0 chỉ phủ phần mã lịch sử, phần mềm đang phát hành là đóng nên không thể audit hay fork bản mới. |
| Nguồn | [README.md](https://github.com/palmier-io/palmier-pro/blob/7a140c15ca628a8aa67bb5aaae7c6994474f73b9/README.md) · [LICENSE](https://github.com/palmier-io/palmier-pro/blob/7a140c15ca628a8aa67bb5aaae7c6994474f73b9/LICENSE) · [BINARY_LICENSE.md](https://github.com/palmier-io/palmier-pro/blob/7a140c15ca628a8aa67bb5aaae7c6994474f73b9/BINARY_LICENSE.md) |

<a id="ch-pixelle-video"></a>

### Pixelle-Video

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/ATH-MaaS/Pixelle-Video |
| License | Apache-2.0 |
| Phiên bản đã đọc | `848b054e4fae40dabc62ec58e960b573e83793ac` (commit 2026-06-14) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README (tiếng Trung), LICENSE, NOTICE, docs.yml; chưa chạy upstream |
| Bảo trì | commit cuối 14/6/2026 (~5 tháng); chỉ có docs.yml (deploy mkdocs), không CI test |
| Nhận định | Pipeline Python/Streamlit/FastAPI nhập chủ đề rồi sinh kịch bản, ảnh/video AI (ComfyUI, RunningHub hoặc API trực tiếp), TTS, BGM và ghép MP4, có digital human và dịch chuyển động. Giới hạn: không test, đứng yên từ giữa tháng 6, dữ liệu có thể gửi tới RunningHub/API bên thứ ba. |
| Nguồn | [README.md](https://github.com/ATH-MaaS/Pixelle-Video/blob/848b054e4fae40dabc62ec58e960b573e83793ac/README.md) · [LICENSE](https://github.com/ATH-MaaS/Pixelle-Video/blob/848b054e4fae40dabc62ec58e960b573e83793ac/LICENSE) · [NOTICE](https://github.com/ATH-MaaS/Pixelle-Video/blob/848b054e4fae40dabc62ec58e960b573e83793ac/NOTICE) · [docs.yml](https://github.com/ATH-MaaS/Pixelle-Video/blob/848b054e4fae40dabc62ec58e960b573e83793ac/.github/workflows/docs.yml) |

<a id="ch-podcastfy"></a>

### Podcastfy

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/souzatharsis/podcastfy |
| License | Apache-2.0 |
| Phiên bản đã đọc | `053b54a0917e35edb2808049499292361ccaae7b` (commit 2026-05-04) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README, LICENSE, pyproject.toml; chưa chạy upstream |
| Bảo trì | commit cuối 4/5/2026 (~6,5 tháng); có python-app.yml, docker-publish.yml, draft-pdf.yml (chưa mở); pyproject v0.4.3 |
| Nhận định | Gói Python sinh đoạn hội thoại âm thanh (kiểu podcast) từ web, PDF, ảnh, YouTube hoặc chủ đề, có CLI, API và Docker. Phụ thuộc LLM/TTS bên thứ ba; mã ít cập nhật từ giữa năm. |
| Nguồn | [README.md](https://github.com/souzatharsis/podcastfy/blob/053b54a0917e35edb2808049499292361ccaae7b/README.md) · [LICENSE](https://github.com/souzatharsis/podcastfy/blob/053b54a0917e35edb2808049499292361ccaae7b/LICENSE) · [pyproject.toml](https://github.com/souzatharsis/podcastfy/blob/053b54a0917e35edb2808049499292361ccaae7b/pyproject.toml) |

<a id="ch-remotion-cuongit-template"></a>

### remotion-cuongit-template

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/Cuongyd196/remotion-cuongit-template |
| License | MIT (khác catalog cũ) |
| Phiên bản đã đọc | `206b4b73ba6b04fab802ad8a2ee1381461bd0892` (commit 2026-11-07) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README (tiếng Việt), LICENSE; chưa chạy upstream |
| Bảo trì | commit 7/11/2026; không có workflow CI |
| Nhận định | Mẫu Remotion kèm bốn skill cho agent tạo video dọc 9:16 về công nghệ (giải thích chủ đề, giới thiệu repo GitHub, so sánh, từ nội dung có sẵn). Mã MIT nhưng Remotion và các tài nguyên giọng/âm thanh có điều khoản riêng; không có CI. |
| Nguồn | [README.md](https://github.com/Cuongyd196/remotion-cuongit-template/blob/206b4b73ba6b04fab802ad8a2ee1381461bd0892/README.md) · [LICENSE](https://github.com/Cuongyd196/remotion-cuongit-template/blob/206b4b73ba6b04fab802ad8a2ee1381461bd0892/LICENSE) |

<a id="ch-short-video-factory"></a>

### Short Video Factory

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/YILS-LIN/short-video-factory |
| License | AGPL-3.0 |
| Phiên bản đã đọc | `4e58116fd98cac2526e134237b57db8f01aed79f` (commit 2026-11-20) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README (tiếng Trung), LICENSE, package.json; chưa chạy upstream |
| Bảo trì | commit 20/11/2026 (release v1.4.1); có build.yml (chưa mở) |
| Nhận định | Ứng dụng Electron desktop tạo video ngắn: LLM (API tương thích OpenAI) viết lời, TTS (EdgeTTS), tự cắt ghép, phụ đề, xử lý hàng loạt. Rủi ro: AGPL-3.0 buộc mở mã khi nhúng thành dịch vụ; README tuyên bố chạy "hoàn toàn cục bộ" nhưng LLM/TTS gọi dịch vụ ngoài **(chưa xác minh)**. |
| Nguồn | [README.md](https://github.com/YILS-LIN/short-video-factory/blob/4e58116fd98cac2526e134237b57db8f01aed79f/README.md) · [LICENSE](https://github.com/YILS-LIN/short-video-factory/blob/4e58116fd98cac2526e134237b57db8f01aed79f/LICENSE) · [package.json](https://github.com/YILS-LIN/short-video-factory/blob/4e58116fd98cac2526e134237b57db8f01aed79f/package.json) |

<a id="ch-social-media-agent-langchain"></a>

### Social Media Agent (LangChain)

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/langchain-ai/social-media-agent |
| License | MIT |
| Phiên bản đã đọc | `bc27973c9c11f5c4929d78f26cb9ed200ab017f2` (commit 2026-11-17) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README, LICENSE; chưa chạy upstream |
| Bảo trì | commit 17/11/2026; có ci.yml, unit-tests.yml, integration-tests.yml (chưa mở) |
| Nhận định | Agent LangGraph (TypeScript) soạn và đăng bài mạng xã hội: nạp nội dung từ URL, tạo bài, người dùng duyệt trước khi đăng; có chế độ quickstart và chế độ đầy đủ (Slack, ảnh). Cần nhiều khóa API (LLM, LangSmith, Firecrawl, đăng nhập mạng xã hội). |
| Nguồn | [README.md](https://github.com/langchain-ai/social-media-agent/blob/bc27973c9c11f5c4929d78f26cb9ed200ab017f2/README.md) · [LICENSE](https://github.com/langchain-ai/social-media-agent/blob/bc27973c9c11f5c4929d78f26cb9ed200ab017f2/LICENSE) |

<a id="ch-social-media-research-skills"></a>

### Social Media Research Skills

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/ScrapeCreators/social-media-research-skills |
| License | MIT |
| Phiên bản đã đọc | `64ba7b4dea71e130d2712ffb6c1c1024b3b7c4b2` (commit 2026-08-26) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README, LICENSE; chưa chạy upstream |
| Bảo trì | commit 26/8/2026 (~3 tháng, gộp PR thêm LICENSE MIT); không có CI |
| Nhận định | Bộ skill cho agent nghiên cứu mạng xã hội (bài nổi bật, bình luận, transcript, phân tích đối thủ, thư viện quảng cáo) trên nhiều nền tảng, cài bằng `npx skills add`. Cần khóa SCRAPECREATORS_API_KEY của dịch vụ trả phí; mã skill MIT nhưng dữ liệu đi qua một bên thứ ba thương mại. |
| Nguồn | [README.md](https://github.com/ScrapeCreators/social-media-research-skills/blob/64ba7b4dea71e130d2712ffb6c1c1024b3b7c4b2/README.md) · [LICENSE](https://github.com/ScrapeCreators/social-media-research-skills/blob/64ba7b4dea71e130d2712ffb6c1c1024b3b7c4b2/LICENSE) |

<a id="ch-toonflow"></a>

### Toonflow

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/HBAI-Ltd/Toonflow-app |
| License | MIT |
| Phiên bản đã đọc | `eecf51547af47eb504822186bd3f2dee369125ff` (commit 2026-11-20) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README (tiếng Trung), LICENSE; chưa chạy upstream |
| Bảo trì | commit 20/11/2026; có release.yml, signPath.yml, debug.yml (chưa mở) |
| Nhận định | Studio phim ngắn/hoạt hình AI mã mở: canvas vô hạn, tiền kỳ 3D (white-model), sinh video theo từng shot, bản desktop (Electrobun) và Docker. README tiếng Trung, có nhiều khối tài trợ; số lượt xem phim ngắn là tuyên bố của tác giả **(chưa xác minh)**. |
| Nguồn | [README.md](https://github.com/HBAI-Ltd/Toonflow-app/blob/eecf51547af47eb504822186bd3f2dee369125ff/README.md) · [LICENSE](https://github.com/HBAI-Ltd/Toonflow-app/blob/eecf51547af47eb504822186bd3f2dee369125ff/LICENSE) |

<a id="ch-topview-3d-builder"></a>

### Topview 3D Builder

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/topviewai/topview-3d-builder |
| License | Apache-2.0 |
| Phiên bản đã đọc | `631c08c8fd352b4ff83df33aa9a74a4563f4674b` (commit 2026-10-17) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE; chưa chạy upstream |
| Bảo trì | Commit 17/10/2026, repo mới; hai workflow (ci.yml, release.yml) có trong cây nhưng chưa mở. |
| Nhận định | Plugin/CLI để agent dựng cảnh 3D cục bộ làm tham chiếu trước khi sinh video; cấu trúc có `.mcp.json`, `.claude-plugin`, `.codex-plugin`, `.cursor-plugin`. README quảng bá "runs 100% local"; việc bước sinh video dẫn về Topview trả phí là ghi chú cũ của catalog, chưa kiểm lại **(chưa xác minh)**. |
| Nguồn | [README.md](https://github.com/topviewai/topview-3d-builder/blob/631c08c8fd352b4ff83df33aa9a74a4563f4674b/README.md) · [LICENSE](https://github.com/topviewai/topview-3d-builder/blob/631c08c8fd352b4ff83df33aa9a74a4563f4674b/LICENSE) |

<a id="ch-vbench"></a>

### VBench

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/Vchitect/VBench |
| License | Apache-2.0 |
| Phiên bản đã đọc | `fd18b3d055cb0fc6f066ca90fe2c3c8cbb698490` (commit 2026-08-21) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE, setup.py; chưa chạy upstream |
| Bảo trì | Commit cuối 21/8/2026 (~3 tháng trước ngày kiểm). |
| Nhận định | Bộ benchmark đánh giá model sinh video theo nhiều chiều (T2V, I2V, video dài, VBench-2.0); đáng tham khảo làm khung chấm. Nặng: cần GPU/CUDA và nhiều checkpoint (theo setup.py/README). |
| Nguồn | [README.md](https://github.com/Vchitect/VBench/blob/fd18b3d055cb0fc6f066ca90fe2c3c8cbb698490/README.md) · [LICENSE](https://github.com/Vchitect/VBench/blob/fd18b3d055cb0fc6f066ca90fe2c3c8cbb698490/LICENSE) · [setup.py](https://github.com/Vchitect/VBench/blob/fd18b3d055cb0fc6f066ca90fe2c3c8cbb698490/setup.py) |

<a id="ch-video-use"></a>

### video-use

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/browser-use/video-use |
| License | MIT |
| Phiên bản đã đọc | `43cfc566833548093455c9d4a46bd69913b7e552` (commit 2026-10-08) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE, pyproject.toml; chưa chạy upstream |
| Bảo trì | Commit 8/10/2026; repo không có thư mục .github/workflows. |
| Nhận định | Skill Claude Code dựng video từ footage thô qua transcript từng từ và ảnh timeline, xuất bằng ffmpeg. README tự nhận self-evaluate ở mỗi điểm cắt **(chưa xác minh)**. Phụ thuộc dịch vụ ElevenLabs trả phí và có định hướng sang bản cloud. |
| Nguồn | [README.md](https://github.com/browser-use/video-use/blob/43cfc566833548093455c9d4a46bd69913b7e552/README.md) · [LICENSE](https://github.com/browser-use/video-use/blob/43cfc566833548093455c9d4a46bd69913b7e552/LICENSE) · [pyproject.toml](https://github.com/browser-use/video-use/blob/43cfc566833548093455c9d4a46bd69913b7e552/pyproject.toml) |

<a id="ch-videoseal"></a>

### VideoSeal

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/facebookresearch/videoseal |
| License | MIT |
| Phiên bản đã đọc | `f12875a9b5e711e0c6e2dc3a22aca18231ce4a1a` (commit 2026-11-10) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE, pyproject.toml; chưa chạy upstream |
| Bảo trì | Commit 10/11/2026 (gần ngày kiểm). |
| Nhận định | Bộ watermark ẩn cho ảnh/video của Meta (VideoSeal, PixelSeal, ChunkySeal) kèm WmForger để thử tấn công giả mạo. Đáng tham khảo cho nhúng/phát hiện nguồn gốc; độ bền thực tế **(chưa xác minh)**, chỉ là số liệu của tác giả. |
| Nguồn | [README.md](https://github.com/facebookresearch/videoseal/blob/f12875a9b5e711e0c6e2dc3a22aca18231ce4a1a/README.md) · [LICENSE](https://github.com/facebookresearch/videoseal/blob/f12875a9b5e711e0c6e2dc3a22aca18231ce4a1a/LICENSE) · [pyproject.toml](https://github.com/facebookresearch/videoseal/blob/f12875a9b5e711e0c6e2dc3a22aca18231ce4a1a/pyproject.toml) |

<a id="ch-vimax"></a>

### ViMax

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/HKUDS/ViMax |
| License | MIT |
| Phiên bản đã đọc | `fd4b72e7731be6e5f88486206d25ea59849b0285` (commit 2026-09-30) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc readme.md, LICENSE, pyproject.toml; chưa chạy upstream |
| Bảo trì | Commit 30/9/2026; repo có thư mục tests, workflow chưa kiểm. |
| Nhận định | Khung đa agent (biên kịch, storyboard, nhân vật, dựng) đi từ ý tưởng/kịch bản/tiểu thuyết đến video, có Web UI và TUI. Cần khóa API của nhà cung cấp mô hình ngoài; chất lượng đầu ra **(chưa xác minh)**. |
| Nguồn | [readme.md](https://github.com/HKUDS/ViMax/blob/fd4b72e7731be6e5f88486206d25ea59849b0285/readme.md) · [LICENSE](https://github.com/HKUDS/ViMax/blob/fd4b72e7731be6e5f88486206d25ea59849b0285/LICENSE) · [pyproject.toml](https://github.com/HKUDS/ViMax/blob/fd4b72e7731be6e5f88486206d25ea59849b0285/pyproject.toml) |

<a id="ch-vmaf"></a>

### VMAF

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/Netflix/vmaf |
| License | BSD-2-Clause-Patent |
| Phiên bản đã đọc | `cf677baaa039723876fff8c2677164f25102e684` (commit 2026-11-16) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE; chưa chạy upstream |
| Bảo trì | Commit 16/11/2026; README ghi HDR model 26/10/2026 và VMAF v1 (6/2026). |
| Nhận định | Chỉ số chất lượng video cảm nhận của Netflix, thư viện C `libvmaf` cùng wrapper Python để huấn luyện/kiểm model. Là chỉ số full-reference: cần bản gốc để so, nên hợp đo bản mã hóa so với master hơn là chấm video AI tự sinh. |
| Nguồn | [README.md](https://github.com/Netflix/vmaf/blob/cf677baaa039723876fff8c2677164f25102e684/README.md) · [LICENSE](https://github.com/Netflix/vmaf/blob/cf677baaa039723876fff8c2677164f25102e684/LICENSE) |

<a id="ch-wan2-2"></a>

### Wan2.2

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/Wan-Video/Wan2.2 |
| License | Apache-2.0 |
| Phiên bản đã đọc | `1ea34ff48f87168174e12956e200b1d908b1c5ff` (commit 2026-09-21) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc LICENSE.txt, README.md, pyproject.toml; chưa chạy upstream |
| Bảo trì | Commit 21/9/2026 (~2 tháng); README nêu bản Wan2.2-Animate từ 19/9/2025, không có thư mục .github trong cây. |
| Nhận định | Model video mở của Alibaba (T2V/I2V MoE, TI2V-5B, S2V, Animate) kèm mã suy luận `generate.py`. Cần GPU lớn; trọng số tải từ HF/ModelScope, repo không chứa trọng số. |
| Nguồn | [LICENSE.txt](https://github.com/Wan-Video/Wan2.2/blob/1ea34ff48f87168174e12956e200b1d908b1c5ff/LICENSE.txt) · [README.md](https://github.com/Wan-Video/Wan2.2/blob/1ea34ff48f87168174e12956e200b1d908b1c5ff/README.md) · [pyproject.toml](https://github.com/Wan-Video/Wan2.2/blob/1ea34ff48f87168174e12956e200b1d908b1c5ff/pyproject.toml) |

<a id="ch-waoowaoo-ten-cu-saturndec-waoowaoo"></a>

### waoowaoo (tên cũ saturndec/waoowaoo)

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/waooAI/waoowaoo |
| License | Elastic-2.0 |
| Phiên bản đã đọc | `dfec20e32298ed675050329e4a41477024148399` (commit 2026-09-21) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE, package.json; chưa chạy upstream |
| Bảo trì | Commit 21/9/2026, package.json 0.5.0-beta.1; README ghi "Preview release". |
| Nhận định | Workspace ảnh/video AI có Assistant, canvas và cấu hình OpenRouter; từ bản 0.5 viết lại so với bản "phim ngắn từ tiểu thuyết" cũ. ELv2 cấm cung cấp dịch vụ hosted/managed cho bên thứ ba, không dùng làm nền cho dịch vụ bán lại. |
| Nguồn | [README.md](https://github.com/waooAI/waoowaoo/blob/dfec20e32298ed675050329e4a41477024148399/README.md) · [LICENSE](https://github.com/waooAI/waoowaoo/blob/dfec20e32298ed675050329e4a41477024148399/LICENSE) · [package.json](https://github.com/waooAI/waoowaoo/blob/dfec20e32298ed675050329e4a41477024148399/package.json) |

<a id="nt-2026-11-23"></a>

## Nâng trần theo khoảng trống — 23/11/2026

Phần này có các hồ sơ mới của đợt nâng trần: mười trinh sát tìm trên internet và GitHub những mảng mà chuyên mục còn thiếu hoặc chỉ có hồ sơ cũ, rồi mỗi repo được clone nông tại một commit cố định, đọc LICENSE, README, ít nhất một file triển khai thật và CI nếu có; không cài hay chạy mã upstream. Mô tả của trinh sát nhiều chỗ sai so với mã thật, và các chỗ đó được sửa ngay trong từng hồ sơ. Số sao lấy sau bằng GitHub search API nên có thể để trống.

<a id="nt-smartsub"></a>

### SmartSub

| Thuộc tính | Giá trị |
|---|---|
| Repo | https://github.com/buxuku/SmartSub |
| License | MIT |
| Phiên bản đã đọc | `a03d73c79a5a21513092996a9ad715ee68e57368` (commit 2026-11-19) |
| Kiểm chứng | 2026-11-23; code-read; đã đọc README_EN.md, alignment.ts, automation/server.ts, catalog.ts, ci.yml, crash-diagnostics.yml; chưa chạy upstream |
| Khoảng trống lấp | Phụ đề và dịch phụ đề tiếng Việt (và lồng tiếng) |
| Cơ chế đáng học | - `main/helpers/dubbing/alignment.ts`: tính khe thời gian cho từng cue (mượn khoảng lặng chỉ khi được duyệt), ước lượng độ dài giọng đọc rồi quyết định tăng tốc hoặc cắt; ngưỡng quá dài 1.15 khai báo ở `types/dubbing.ts`.<br>- `main/automation/server.ts`: máy chủ HTTP cục bộ chỉ nhận Host 127.0.0.1, từ chối request có header Origin, token Bearer ngẫu nhiên 32 byte so sánh `timingSafeEqual`, giới hạn body 8 MB, kết quả qua `redact()`.<br>- `automation/catalog.ts`: danh mục thao tác định nghĩa bằng zod, dùng chung cho MCP và CLI (`smartsub`), có `requestId` chống trùng và `tasks.wait`. |
| Tiêu chí và cách kiểm | CI `ci.yml` chạy kiểm khớp khóa i18n, typecheck, nhiều bộ test (pro-baseline, engines, GPU, stdio, addon, speech-review, translate-parser) trên ubuntu-22.04; có workflow riêng cho GPU Windows, đường dẫn không-ASCII, ffmpeg-compat (chỉ ghi tên, chưa mở hết). Kiểm bằng máy, nhưng chất lượng dịch/lồng tiếng không có ngưỡng tự động đã đọc. |
| Giới hạn và rủi ro | MIT. Nhiều dịch vụ dịch/LLM/TTS đám mây: văn bản phụ đề rời máy khi dùng; README có mục tài trợ quảng cáo API trung gian. Crash reporter đặt `uploadToServer: false` (chỉ dòng trong crashReporting.ts, chưa mở cả file). Số liệu "111 công cụ", "20 dịch vụ dịch" là tuyên bố tác giả **(chưa xác minh)**. Phụ thuộc addon/native tải về runtime (CUDA, whisper addon): rủi ro chuỗi cung ứng cần kiểm riêng. Danh sách ngôn ngữ có "vi" (locale en/common.json) nhưng chất lượng ASR/TTS tiếng Việt **(chưa xác minh)**. |
| So với | pyvideotrans, VideoLingo (cùng nhóm dịch/lồng tiếng), FunASR (động cơ nhận dạng) |
| Nguồn | [README_EN.md](https://github.com/buxuku/SmartSub/blob/a03d73c79a5a21513092996a9ad715ee68e57368/README_EN.md) · [LICENSE](https://github.com/buxuku/SmartSub/blob/a03d73c79a5a21513092996a9ad715ee68e57368/LICENSE) · [package.json](https://github.com/buxuku/SmartSub/blob/a03d73c79a5a21513092996a9ad715ee68e57368/package.json) · [ci.yml](https://github.com/buxuku/SmartSub/blob/a03d73c79a5a21513092996a9ad715ee68e57368/.github/workflows/ci.yml) · [crash-diagnostics.yml](https://github.com/buxuku/SmartSub/blob/a03d73c79a5a21513092996a9ad715ee68e57368/.github/workflows/crash-diagnostics.yml) · [alignment.ts](https://github.com/buxuku/SmartSub/blob/a03d73c79a5a21513092996a9ad715ee68e57368/main/helpers/dubbing/alignment.ts) · [server.ts](https://github.com/buxuku/SmartSub/blob/a03d73c79a5a21513092996a9ad715ee68e57368/main/automation/server.ts) · [catalog.ts](https://github.com/buxuku/SmartSub/blob/a03d73c79a5a21513092996a9ad715ee68e57368/automation/catalog.ts) |

<a id="nt-youdub-desktop"></a>

### YouDub Desktop

| Thuộc tính | Giá trị |
|---|---|
| Repo | https://github.com/liuzhao1225/YouDub-Desktop |
| License | Apache-2.0 |
| Phiên bản đã đọc | `b82cb0aebe7e89cc0dd0db215764657f06cb0d05` (commit 2026-11-23) |
| Kiểm chứng | 2026-11-23; code-read; đã đọc README.en.md, docs/workflows.md, dag.py, segments.py, tts.py, resources.json, ci.yml; chưa chạy upstream |
| Khoảng trống lấp | Lồng tiếng và bản địa hóa video |
| Cơ chế đáng học | - `backend/app/server/dag.py` (`TaskRunner`): lập lịch DAG, một khe GPU (`Semaphore(1)`), trạng thái chờ xác nhận của người, sổ đăng ký artifact và kế hoạch chạy lại.<br>- `docs/workflows.md`: tác vụ lưu bản chụp đồ thị và cấu hình; sửa kết quả tạo task phái sinh, xem trước phần tái dùng; không có song song/vòng lặp ở phiên bản này.<br>- `backend/app/v1/tts.py`: mỗi câu dịch lấy audio câu gốc làm tham chiếu giọng, ánh xạ một-một; kiểm ngôn ngữ nguồn/đích thuộc `LANGUAGES`.<br>- `backend/requirements/resources.json`: khai báo nhóm phụ thuộc và model theo nhà cung cấp, chỉ chuẩn bị tài nguyên cho workflow được chọn. |
| Tiêu chí và cách kiểm | CI `ci.yml`: job backend cài ffmpeg, dựng venv và chạy pytest qua `scripts/test-backend.mjs` (thư mục backend/tests có test cho asr, tts, mix, export...); job web kiểm frontend; action ghim theo SHA. Kiểm bằng máy; chất lượng giọng/dịch không có ngưỡng tự động đã đọc. |
| Giới hạn và rủi ro | Apache-2.0 cho mã; model (Whisper, Demucs, VoxCPM2, Qwen forced aligner) có license riêng, chưa kiểm từng cái **(chưa xác minh)**; thư mục submodule demucs trỏ repo facebookresearch/demucs, không được clone ở đây. `LANGUAGES = ("en","zh","ja")` trong segments.py: không có tiếng Việt. README và release trỏ tên cũ YouDub-webui (repo đã đổi tên). Nhân bản giọng người nói gốc cần cân nhắc quyền và deepfake. Cần GPU và tải nhiều model; README hướng dẫn mặc định dùng mirror npm Trung Quốc. |
| So với | VideoLingo, pyvideotrans, FunASR (chỉ khâu nhận dạng) |
| Nguồn | [README.en.md](https://github.com/liuzhao1225/YouDub-Desktop/blob/b82cb0aebe7e89cc0dd0db215764657f06cb0d05/README.en.md) · [LICENSE](https://github.com/liuzhao1225/YouDub-Desktop/blob/b82cb0aebe7e89cc0dd0db215764657f06cb0d05/LICENSE) · [THIRD_PARTY_NOTICES.md](https://github.com/liuzhao1225/YouDub-Desktop/blob/b82cb0aebe7e89cc0dd0db215764657f06cb0d05/THIRD_PARTY_NOTICES.md) · [workflows.md](https://github.com/liuzhao1225/YouDub-Desktop/blob/b82cb0aebe7e89cc0dd0db215764657f06cb0d05/docs/workflows.md) · [dag.py](https://github.com/liuzhao1225/YouDub-Desktop/blob/b82cb0aebe7e89cc0dd0db215764657f06cb0d05/backend/app/server/dag.py) · [segments.py](https://github.com/liuzhao1225/YouDub-Desktop/blob/b82cb0aebe7e89cc0dd0db215764657f06cb0d05/backend/app/v1/segments.py) · [tts.py](https://github.com/liuzhao1225/YouDub-Desktop/blob/b82cb0aebe7e89cc0dd0db215764657f06cb0d05/backend/app/v1/tts.py) · [resources.json](https://github.com/liuzhao1225/YouDub-Desktop/blob/b82cb0aebe7e89cc0dd0db215764657f06cb0d05/backend/requirements/resources.json) · [.gitmodules](https://github.com/liuzhao1225/YouDub-Desktop/blob/b82cb0aebe7e89cc0dd0db215764657f06cb0d05/.gitmodules) · [ci.yml](https://github.com/liuzhao1225/YouDub-Desktop/blob/b82cb0aebe7e89cc0dd0db215764657f06cb0d05/.github/workflows/ci.yml) |

<a id="nt-freecut"></a>

### FreeCut

| Thuộc tính | Giá trị |
|---|---|
| Repo | https://github.com/walterlow/freecut |
| License | MIT |
| Phiên bản đã đọc | `5ceeeb388eef5423640b7db157706274bf1b8165` (commit 2026-10-29) |
| Kiểm chứng | 2026-11-23; code-read; đã đọc README.md, package.json, ci.yml, frame-oracle.mjs, server.mjs; chưa chạy upstream |
| Khoảng trống lấp | Trình dựng video trong trình duyệt (WebCodecs, tất định) |
| Cơ chế đáng học | - `headless/frame-oracle.mjs`: dựng dự án fixture giàu hiệu ứng qua `POST /frame`, in `frame=N sha256=...` cho 5 khung; chạy hai lần phải ra cùng hash; `--ablate` bỏ từng thành phần để chứng minh thành phần đó có tác động lên hash.<br>- `headless/serve.mjs` / `server.mjs`: dịch vụ render cục bộ (mặc định 127.0.0.1:8787, hàng đợi có giới hạn, timeout render 30 phút) kèm kiểm tra bảo mật HTTP và test hợp đồng trong `headless/*.test.mjs`.<br>- `package.json`: xuất media bằng `mediabunny` 1.54.0 và các encoder AAC/AC3/MP3/ProRes; tách ranh giới feature bằng các script check trong CI. |
| Tiêu chí và cách kiểm | CI `ci.yml`: kiểm ranh giới feature/layer, quét mã chết (fallow), `vp run check`, unit test có sàn coverage, build, rồi bộ test headless "portable" với ffmpeg. Kiểm bằng máy. Chính `frame-oracle.mjs` ghi rõ không phải golden của CI vì hash phụ thuộc GPU. |
| Giới hạn và rủi ro | MIT. "Tất định" chỉ đúng trong cùng một máy/GPU khi chạy hai lần, theo ghi chú trong frame-oracle.mjs; không có bằng chứng bit-exact giữa GPU. Cần WebGPU/WebCodecs, ProRes/codec tùy trình duyệt. Mô hình AI cục bộ (Parakeet, Kokoro, MusicGen, VLM) tải về lúc chạy, license từng model chưa kiểm **(chưa xác minh)**. Phiên bản `0.0.0`, lịch sử tính năng dài nhưng chưa có bản phát hành ổn định đã đọc. Không thấy mã telemetry trong lần grep mã nguồn (chưa quét sâu). |
| So với | Remotion, mediabunny, ffmpeg.wasm |
| Nguồn | [README.md](https://github.com/walterlow/freecut/blob/5ceeeb388eef5423640b7db157706274bf1b8165/README.md) · [LICENSE](https://github.com/walterlow/freecut/blob/5ceeeb388eef5423640b7db157706274bf1b8165/LICENSE) · [package.json](https://github.com/walterlow/freecut/blob/5ceeeb388eef5423640b7db157706274bf1b8165/package.json) · [ci.yml](https://github.com/walterlow/freecut/blob/5ceeeb388eef5423640b7db157706274bf1b8165/.github/workflows/ci.yml) · [frame-oracle.mjs](https://github.com/walterlow/freecut/blob/5ceeeb388eef5423640b7db157706274bf1b8165/headless/frame-oracle.mjs) · [server.mjs](https://github.com/walterlow/freecut/blob/5ceeeb388eef5423640b7db157706274bf1b8165/headless/server.mjs) |

<a id="nt-ffmetrics"></a>

### FFMetrics

| Thuộc tính | Giá trị |
|---|---|
| Repo | https://github.com/fifonik/FFMetrics |
| License | Không có file LICENSE |
| Phiên bản đã đọc | `6ec04ee493d178199de1f71c7f357814024898f7` (commit 2026-05-13) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, TODO.md (repo không có mã nguồn); chưa chạy upstream |
| Khoảng trống lấp | Cổng chất lượng video tất định (VMAF/PSNR/SSIM; loudness và timecode không có) |
| Cơ chế đáng học | - README liệt kê PSNR, SSIM, VMAF, XPSNR; chọn model VMAF tự động theo thông tin media tham chiếu, hỗ trợ model built-in, json hoặc pkl.<br>- Chạy không giao diện qua cờ: `-metric=...`, `-run`, `-exit`, `-auto-save-results-file`, `-log-frames`, `-project=<file.ffmproj>`; đây là cách dùng như bước trong pipeline Windows.<br>- Trích khung "xấu" ra PNG và lưu số liệu từng khung ra CSV để lọc ngưỡng ở bước khác. |
| Tiêu chí và cách kiểm | Không có ngưỡng đạt/trượt, không test, không CI trong repo (không có thư mục .github). Mọi khẳng định là mô tả của tác giả **(chưa xác minh)**; chưa tải bản phát hành nhị phân. |
| Giới hạn và rủi ro | Không có file LICENSE và không có mã nguồn: mặc định mọi quyền được bảo lưu, không nên coi là mã nguồn mở (trinh sát ghi license "-" là đúng). Chỉ Windows, cần ffmpeg ngoài (VMAF cần bản build có libvmaf). Lời hứa "không theo dõi, không quảng cáo" là tuyên bố tác giả **(chưa xác minh)**. Bảo trì: commit mới nhất 2026-05-13, chỉ README. |
| So với | ffmpeg-quality-metrics (CLI/Python, cùng việc), VMAF của Netflix, ffmpeg |
| Nguồn | [README.md](https://github.com/fifonik/FFMetrics/blob/6ec04ee493d178199de1f71c7f357814024898f7/README.md) · [TODO.md](https://github.com/fifonik/FFMetrics/blob/6ec04ee493d178199de1f71c7f357814024898f7/TODO.md) |

<a id="nt-ai-video-editor"></a>

### Timeline Studio (ai-video-editor)

| Thuộc tính | Giá trị |
|---|---|
| Repo | https://github.com/MartinDelophy/ai-video-editor |
| License | MIT (chỉ phạm vi mã gốc; model và dữ liệu có license riêng) |
| Phiên bản đã đọc | `087e2f78dbc0ef2c1843daa82236367cb274b9ff` (commit 2026-11-22) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, MODEL_LICENSES.md, docs/webmcp.md, SKILL.md, package.json, ci.yml; chưa chạy upstream |
| Khoảng trống lấp | Trình dựng video trong trình duyệt (WebCodecs, tất định); người và agent cùng sửa một timeline |
| Cơ chế đáng học | - `docs/webmcp.md`: bảng công cụ `timeline_project_inspect`, `timeline_edit_preview` (cần `stateToken`, chưa đổi timeline), `timeline_edit_apply` (áp đúng `previewId` thành một giao dịch hoàn tác được), `timeline_export_prepare/start/inspect/cancel`.<br>- `skills/edit-timeline-studio/SKILL.md`: ưu tiên xử lý file `.timeline` cục bộ qua lớp lệnh có revision, bắt buộc `timeline_project_diff` trước `apply`, và cấm tuyên bố tất định nếu chỉ tự động hóa UI.<br>- `MODEL_LICENSES.md`: tách rõ license mã và trọng số model, ghi mirror/ghim revision/checksum không làm đổi license. |
| Tiêu chí và cách kiểm | CI `ci.yml`: chặn commit trọng số model vào `public/models/`, giới hạn 20 MiB mỗi file, rồi eslint, typecheck (web và host) và build; không thấy bước unit test trong CI và `package.json` không có script `test` (đã grep). Chưa chạy gì. |
| Giới hạn và rủi ro | MIT chỉ cho mã gốc; MODEL_LICENSES.md nói rõ trọng số face-swap (MobileFaceSwap, ArcFace, SCRFD) là research, không cấp quyền thương mại, nên không dùng tính năng đó cho sản phẩm thương mại khi chưa xác minh. Mô hình tải từ mirror Hugging Face/ModelScope lúc chạy. README quảng bá bản Anna (lưu cloud) và nhóm WeChat; bản local khác bản cloud về dữ liệu rời máy. Tính năng deep synthesis có cảnh báo sử dụng có trách nhiệm. Tuyên bố "deterministic offline export" **(chưa xác minh)** vì không đọc mã xuất. Tên sản phẩm là Timeline Studio, khác tên repo. |
| So với | OpenTimelineIO (định dạng trao đổi), Remotion (dựng bằng mã), mediabunny |
| Nguồn | [README.md](https://github.com/MartinDelophy/ai-video-editor/blob/087e2f78dbc0ef2c1843daa82236367cb274b9ff/README.md) · [LICENSE](https://github.com/MartinDelophy/ai-video-editor/blob/087e2f78dbc0ef2c1843daa82236367cb274b9ff/LICENSE) · [MODEL_LICENSES.md](https://github.com/MartinDelophy/ai-video-editor/blob/087e2f78dbc0ef2c1843daa82236367cb274b9ff/MODEL_LICENSES.md) · [webmcp.md](https://github.com/MartinDelophy/ai-video-editor/blob/087e2f78dbc0ef2c1843daa82236367cb274b9ff/docs/webmcp.md) · [SKILL.md](https://github.com/MartinDelophy/ai-video-editor/blob/087e2f78dbc0ef2c1843daa82236367cb274b9ff/skills/edit-timeline-studio/SKILL.md) · [package.json](https://github.com/MartinDelophy/ai-video-editor/blob/087e2f78dbc0ef2c1843daa82236367cb274b9ff/package.json) · [ci.yml](https://github.com/MartinDelophy/ai-video-editor/blob/087e2f78dbc0ef2c1843daa82236367cb274b9ff/.github/workflows/ci.yml) |

<a id="nt-libebur128"></a>

### libebur128

| Thuộc tính | Giá trị |
|---|---|
| Repo | https://github.com/jiixyj/libebur128 |
| License | MIT |
| Phiên bản đã đọc | `1f3fc73c9526c462405613e4fedca5d0f9fad9fc` (commit 2026-11-19) |
| Kiểm chứng | 2026-11-23; code-read; đã đọc ebur128.h, ebur128.c, test ebu_files và true_peak, check_coverage_thresholds.py, build.yml, README.md; chưa chạy upstream |
| Khoảng trống lấp | Cổng chất lượng video tất định (loudness) |
| Cơ chế đáng học | - `ebur128/ebur128.c`: cổng tuyệt đối -70 LUFS dùng histogram 1000 ngăn, cổng tương đối -10 LU (`relative_gate = -10.0`), hiệu chỉnh 0.691 theo BS.1770.<br>- `ebur128/ebur128.h`: các chế độ đo (`ebur128_loudness_global`, `ebur128_loudness_range`, peak) và định nghĩa kênh theo BS.1770-4.<br>- Lõi tách `ebur128_loudness_global_multiple` để gộp nhiều luồng; v1.2.4 sửa lỗi ngưỡng tương đối bị tính từ state cuối cùng (README). |
| Tiêu chí và cách kiểm | Test `ebur128-test.ebu_files.cpp`: dung sai integrated 0.1 LU, LRA 1.0 LU, true peak không vượt giá trị chuẩn quá 0.2 dB; test malloc-fail; `check_coverage_thresholds.py` mặc định yêu cầu 100% dòng, 85% nhánh, 100% hàm. CI `build.yml` chạy ubuntu x86 và ARM, macOS 15, Windows 2022 với sanitizer và coverage 32-bit. Kiểm bằng máy; cách lấy bộ file EBU của CMake chưa kiểm. |
| Giới hạn và rủi ro | MIT, tác giả Jan Kokemüller. Chỉ là thư viện: muốn làm cổng loudness phải tự viết lớp đọc audio và ngưỡng (ví dụ -23 LUFS/-14 LUFS) bên ngoài. Công cụ dòng lệnh là repo khác (loudness-scanner). Bản 1.2.6; commit mới nhất 2026-11-19 là còn bảo trì. Tuyên bố tuân thủ chuẩn dựa trên test của tác giả, chưa chạy lại. |
| So với | ffmpeg (bộ lọc ebur128 dùng cùng phép đo), ffmpeg-quality-metrics, VMAF |
| Nguồn | [README.md](https://github.com/jiixyj/libebur128/blob/1f3fc73c9526c462405613e4fedca5d0f9fad9fc/README.md) · [COPYING](https://github.com/jiixyj/libebur128/blob/1f3fc73c9526c462405613e4fedca5d0f9fad9fc/COPYING) · [ebur128.h](https://github.com/jiixyj/libebur128/blob/1f3fc73c9526c462405613e4fedca5d0f9fad9fc/ebur128/ebur128.h) · [ebur128.c](https://github.com/jiixyj/libebur128/blob/1f3fc73c9526c462405613e4fedca5d0f9fad9fc/ebur128/ebur128.c) · [ebur128-test.ebu_files.cpp](https://github.com/jiixyj/libebur128/blob/1f3fc73c9526c462405613e4fedca5d0f9fad9fc/ebur128/ebur128-test.ebu_files.cpp) · [ebur128-test.true_peak.cpp](https://github.com/jiixyj/libebur128/blob/1f3fc73c9526c462405613e4fedca5d0f9fad9fc/ebur128/ebur128-test.true_peak.cpp) · [check_coverage_thresholds.py](https://github.com/jiixyj/libebur128/blob/1f3fc73c9526c462405613e4fedca5d0f9fad9fc/tools/check_coverage_thresholds.py) · [build.yml](https://github.com/jiixyj/libebur128/blob/1f3fc73c9526c462405613e4fedca5d0f9fad9fc/.github/workflows/build.yml) |

<a id="nt-letsseal"></a>

### Let's Seal (SEAL)

| Thuộc tính | Giá trị |
|---|---|
| Repo | https://github.com/letsseal/letsseal |
| License | Apache-2.0 |
| Phiên bản đã đọc | `daff1706f70ce81d040f1e9bb2a1f4d41c15f64b` (commit 2026-08-18) |
| Kiểm chứng | 2026-11-23; code-read; đã đọc README.md, SPEC.md, CONFORMANCE.md, spec/verify.py, signing-service/c2pa_seal.py, requirements.txt, ci.yml; chưa chạy upstream |
| Khoảng trống lấp | Provenance và C2PA cho media |
| Cơ chế đáng học | - `signing-service/c2pa_seal.py`: ký manifest C2PA bằng callback signer với khóa tổ chức; dùng `c2pa.opened` trên ingredient `parentOf` vì c2pa 0.37 đòi `digitalSourceType` cho `c2pa.created`; seal cũ vẫn xác minh được (test_c2pa.py).<br>- `spec/verify.py`: trình xác minh tham chiếu dùng pyhanko và `openssl`, ghim root đã công bố (hoặc `--root`), tùy chọn `--check-revocation`; thời gian kiểm bằng `ots verify`.<br>- `SPEC.md` + `CONFORMANCE.md`: mỗi yêu cầu đánh số C-n truy về mục spec; thư mục `spec/vectors/` có ca hợp lệ, bị sửa, root lạ, thu hồi. |
| Tiêu chí và cách kiểm | CI `ci.yml`: web (typecheck, test, build, kiểm migration), signing service (khóa requirements, dựng CA tạm, seal, validate, tamper-check). Có vector tuân thủ để bên thứ ba tự kiểm. Kiểm bằng máy; chưa chạy lại. |
| Giới hạn và rủi ro | Apache-2.0. SPEC ghi rõ chưa có rà soát bên thứ ba hay cơ quan chuẩn; không phải chuẩn C2PA hay trust list của Adobe, nên trình đọc C2PA phổ thông có thể không nhận signer (suy luận từ SPEC, chưa thử). Niêm phong ảnh/video qua API cloud khiến byte media đến máy ký (c2pa_seal.py ghi rõ); chỉ CAdES tách rời là chỉ gửi digest. Phụ thuộc dịch vụ cloud letsseal.org, root CA tự vận hành, và neo Bitcoin cho thời gian; chứng minh danh tính pháp lý bị loại trừ. Dự án còn mới (CPS v1.0). |
| So với | C2PA specifications, c2pa-rs (Content Credentials SDK), c2patool, cosign |
| Nguồn | [README.md](https://github.com/letsseal/letsseal/blob/daff1706f70ce81d040f1e9bb2a1f4d41c15f64b/README.md) · [LICENSE](https://github.com/letsseal/letsseal/blob/daff1706f70ce81d040f1e9bb2a1f4d41c15f64b/LICENSE) · [NOTICE](https://github.com/letsseal/letsseal/blob/daff1706f70ce81d040f1e9bb2a1f4d41c15f64b/NOTICE) · [SPEC.md](https://github.com/letsseal/letsseal/blob/daff1706f70ce81d040f1e9bb2a1f4d41c15f64b/SPEC.md) · [CONFORMANCE.md](https://github.com/letsseal/letsseal/blob/daff1706f70ce81d040f1e9bb2a1f4d41c15f64b/CONFORMANCE.md) · [verify.py](https://github.com/letsseal/letsseal/blob/daff1706f70ce81d040f1e9bb2a1f4d41c15f64b/spec/verify.py) · [c2pa_seal.py](https://github.com/letsseal/letsseal/blob/daff1706f70ce81d040f1e9bb2a1f4d41c15f64b/signing-service/c2pa_seal.py) · [requirements.txt](https://github.com/letsseal/letsseal/blob/daff1706f70ce81d040f1e9bb2a1f4d41c15f64b/signing-service/requirements.txt) · [ci.yml](https://github.com/letsseal/letsseal/blob/daff1706f70ce81d040f1e9bb2a1f4d41c15f64b/.github/workflows/ci.yml) |

<a id="nt-raven-otio-viewer"></a>

### Raven (OTIO viewer)

| Thuộc tính | Giá trị |
|---|---|
| Repo | https://github.com/OpenTimelineIO/raven |
| License | Apache-2.0 |
| Phiên bản đã đọc | `e6dfe8bd4c159e380aa2480e4184527a2de7ec7d` (commit 2026-09-23) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, editing.h, pyproject.toml, build.yaml (README và header, chưa đọc timeline.cpp/app.cpp); chưa chạy upstream |
| Khoảng trống lấp | Timeline trao đổi và timecode (OpenTimelineIO) |
| Cơ chế đáng học | - README: mục tiêu thay `otioview`, build CMake trên macOS/Windows/Linux, WASM bằng Emscripten, gói Python `opentimelineio-raven` qua scikit-build-core.<br>- `editing.h`: các thao tác sửa `ReplaceObject`, `DeleteSelectedObject`, `AddMarkerAtPlayhead`, `AddTrack`, `FlattenTrackDown`, màu item.<br>- `app.cpp` (đã grep): timecode dùng `RationalTime::to_timecode` với `drop_frame_mode` và tùy chọn "Snap to Frames". |
| Tiêu chí và cách kiểm | Không có test; workflow `build.yaml` chỉ build trên Linux/macOS/Windows rồi `ls` và `file raven`. Không có kiểm timecode tự động, nên không thay được cổng kiểm timeline. |
| Giới hạn và rủi ro | Apache-2.0. Phiên bản 0.1.0, README tự ghi "experimental" và liệt kê thiếu: nhiều lựa chọn, copy/paste, undo/redo, adapter, tính năng của otiotool. Cần clone `--recursive` (OpenTimelineIO, imgui, glfw, minizip-ng...); ZIP không build được. Bản WASM thiếu hộp thoại mở/lưu file. File mẫu Netflix theo CC BY 4.0. Hiệu năng với timeline lớn (JSON inspector làm tăng thời gian nạp) theo README **(chưa xác minh)**. |
| So với | OpenTimelineIO (thư viện lõi), Blender (editor có timeline riêng) |
| Nguồn | [README.md](https://github.com/OpenTimelineIO/raven/blob/e6dfe8bd4c159e380aa2480e4184527a2de7ec7d/README.md) · [LICENSE.txt](https://github.com/OpenTimelineIO/raven/blob/e6dfe8bd4c159e380aa2480e4184527a2de7ec7d/LICENSE.txt) · [VERSION.txt](https://github.com/OpenTimelineIO/raven/blob/e6dfe8bd4c159e380aa2480e4184527a2de7ec7d/VERSION.txt) · [pyproject.toml](https://github.com/OpenTimelineIO/raven/blob/e6dfe8bd4c159e380aa2480e4184527a2de7ec7d/pyproject.toml) · [editing.h](https://github.com/OpenTimelineIO/raven/blob/e6dfe8bd4c159e380aa2480e4184527a2de7ec7d/editing.h) · [.gitmodules](https://github.com/OpenTimelineIO/raven/blob/e6dfe8bd4c159e380aa2480e4184527a2de7ec7d/.gitmodules) · [build.yaml](https://github.com/OpenTimelineIO/raven/blob/e6dfe8bd4c159e380aa2480e4184527a2de7ec7d/.github/workflows/build.yaml) |

<a id="nt-montage-ai"></a>

### Montage AI

| Thuộc tính | Giá trị |
|---|---|
| Repo | https://github.com/mfahsold/montage-ai |
| License | PolyForm Noncommercial 1.0.0 |
| Phiên bản đã đọc | `2e9dc03bfd0c320cf30f2762791bcccfd1d12b06` (commit 2026-03-10) |
| Kiểm chứng | 2026-11-23; code-read; đã đọc LICENSE, NOTICE, pyproject.toml, README.md, src/montage_ai/export/otio_builder.py, src/montage_ai/text_editor.py, scripts/ci.sh, Jenkinsfile, tests/test_otio_export.py; chưa chạy upstream |
| Khoảng trống lấp | Timeline trao đổi và timecode (xuất OpenTimelineIO, EDL, FCP XML, AAF) |
| Cơ chế đáng học | - `export/otio_builder.py` dựng timeline OpenTimelineIO từ `EditingParameters` và danh sách clip rồi xuất qua adapter: `cmx_3600` (EDL), `otio_json`, `fcp_xml`, `aaf`; marker nhịp và ghi chú hiệu ứng nằm trong metadata `montage_ai` của clip.<br>- `text_editor.py`: cắt theo transcript (Word, Segment, EditRegion), loại từ đệm, khoảng lặng, đoạn độ tin cậy thấp bằng các hàm như `remove_filler_words`, `remove_silence`, `remove_low_confidence`.<br>- Kho có Jenkinsfile gọi `scripts/ci.sh` chạy pytest, không dùng GitHub Actions. |
| Tiêu chí và cách kiểm | Có test cho OTIO (`tests/test_otio_export.py` kiểm tên timeline, số track, metadata clip). Mình chưa chạy; chưa thấy kiểm vòng tròn nhập lại OTIO vào NLE thật. fps mặc định cố định 30 trong `OTIOBuilder`, cần truyền đúng fps nguồn. |
| Giới hạn và rủi ro | License là PolyForm Noncommercial 1.0.0 (cả LICENSE lẫn `pyproject.toml`): chỉ dùng phi thương mại, không sublicense, nên không phải mã nguồn mở theo OSI; trinh sát ghi NOASSERTION là sai so với LICENSE thực. Gốc kho có rất nhiều file báo cáo (SESSION_SUMMARY, DEPLOYMENT_READINESS...) do agent sinh ra nên độ tin cậy tài liệu thấp hơn mã (nhận xét chủ quan). Phụ thuộc FFmpeg (LGPL), OpenCV; yêu cầu 16 GB RAM khuyến nghị. |
| So với | opentimelineio, video-use, auto-create-video |
| Nguồn | [LICENSE](https://github.com/mfahsold/montage-ai/blob/2e9dc03bfd0c320cf30f2762791bcccfd1d12b06/LICENSE) · [NOTICE](https://github.com/mfahsold/montage-ai/blob/2e9dc03bfd0c320cf30f2762791bcccfd1d12b06/NOTICE) · [pyproject.toml](https://github.com/mfahsold/montage-ai/blob/2e9dc03bfd0c320cf30f2762791bcccfd1d12b06/pyproject.toml) · [README.md](https://github.com/mfahsold/montage-ai/blob/2e9dc03bfd0c320cf30f2762791bcccfd1d12b06/README.md) · [otio_builder.py](https://github.com/mfahsold/montage-ai/blob/2e9dc03bfd0c320cf30f2762791bcccfd1d12b06/src/montage_ai/export/otio_builder.py) · [text_editor.py](https://github.com/mfahsold/montage-ai/blob/2e9dc03bfd0c320cf30f2762791bcccfd1d12b06/src/montage_ai/text_editor.py) · [ci.sh](https://github.com/mfahsold/montage-ai/blob/2e9dc03bfd0c320cf30f2762791bcccfd1d12b06/scripts/ci.sh) · [Jenkinsfile](https://github.com/mfahsold/montage-ai/blob/2e9dc03bfd0c320cf30f2762791bcccfd1d12b06/Jenkinsfile) · [test_otio_export.py](https://github.com/mfahsold/montage-ai/blob/2e9dc03bfd0c320cf30f2762791bcccfd1d12b06/tests/test_otio_export.py) |

<a id="nt-media-os"></a>

### Media OS for Claude Code

| Thuộc tính | Giá trị |
|---|---|
| Repo | https://github.com/damionrashford/media-os |
| License | MIT |
| Phiên bản đã đọc | `5014c1e8b23fd3e18d49926d9aa147d15a3aa08e` (commit 2026-05-17) |
| Kiểm chứng | 2026-11-23; code-read; đã đọc LICENSE, README.md, .github/workflows/validate.yml, hooks/hooks.json, hooks/scripts/pre-ffmpeg-validate.py, bin/mosafe, skills/ffmpeg-streaming/SKILL.md, skills/ffmpeg-quality/SKILL.md, skills/ffmpeg-transcode/SKILL.md; chưa chạy upstream |
| Khoảng trống lấp | Tham chiếu skill FFmpeg và media: HLS/DASH, HDR, kiểm chất lượng (VMAF) |
| Cơ chế đáng học | - Plugin Claude Code gồm skill, mode định tuyến, agent chuyên biệt, hook vòng đời và ba CLI `moprobe`, `moqc`, `mosafe` (`hooks/hooks.json`, `bin/`); router nạp file mode trước khi tạo agent.<br>- Hook PreToolUse trên Bash (`hooks/scripts/pre-ffmpeg-validate.py`) quét chuỗi lệnh ffmpeg tìm lỗi kinh điển: input trùng output, `-y` ghi đè, MP4 thiếu `-movflags +faststart`, HLS thiếu `-sc_threshold 0`, TS sang MP4 thiếu `aac_adtstoasc`, CRF cùng bitrate; trả `ask` thay vì chặn cứng.<br>- Các SKILL.md (ví dụ `ffmpeg-streaming`, `ffmpeg-quality`) là công thức theo bước: bảng chọn giao thức, VMAF/PSNR/SSIM và quét CRF theo mục tiêu VMAF. |
| Tiêu chí và cách kiểm | `validate.yml` chỉ kiểm cấu trúc: JSON hợp lệ, version khớp, frontmatter từng SKILL.md, không có README trong thư mục skill, không có đường dẫn /Users, CLI có quyền thực thi, số lượng khớp thực tế. Không thấy test chạy thử các script hay lệnh ffmpeg; chất lượng công thức là chưa xác minh. Validator hook dựa trên khớp chuỗi sau `shlex.split`, không phải parser ffmpeg. |
| Giới hạn và rủi ro | MIT. Số liệu bị lệch: README ghi 96 skill tool và 13 workflow (109), nhưng thư mục `skills/` có 110 thư mục (97 không phải workflow); trinh sát ghi 96 là theo README. Chưa thấy skill riêng cho AVIF, AV1 chỉ xuất hiện trong bảng của `ffmpeg-transcode`; tuyên bố "AV1, AVIF" của trinh sát chưa được xác nhận. Hook SessionStart ghi cache cục bộ (`session-start-capabilities.py`); mình không thấy gọi mạng trong hook và bin (grep), nhưng skill hướng dẫn dùng nhiều công cụ ngoài (yt-dlp, mô hình AI). README cam kết lọc model theo license nhưng mình không kiểm. |
| So với | ffmpeg-skill-kajisho5, ffmpeg-skill-n0an, ffmpeg-quality-metrics |
| Nguồn | [LICENSE](https://github.com/damionrashford/media-os/blob/5014c1e8b23fd3e18d49926d9aa147d15a3aa08e/LICENSE) · [README.md](https://github.com/damionrashford/media-os/blob/5014c1e8b23fd3e18d49926d9aa147d15a3aa08e/README.md) · [validate.yml](https://github.com/damionrashford/media-os/blob/5014c1e8b23fd3e18d49926d9aa147d15a3aa08e/.github/workflows/validate.yml) · [hooks.json](https://github.com/damionrashford/media-os/blob/5014c1e8b23fd3e18d49926d9aa147d15a3aa08e/hooks/hooks.json) · [pre-ffmpeg-validate.py](https://github.com/damionrashford/media-os/blob/5014c1e8b23fd3e18d49926d9aa147d15a3aa08e/hooks/scripts/pre-ffmpeg-validate.py) · [mosafe](https://github.com/damionrashford/media-os/blob/5014c1e8b23fd3e18d49926d9aa147d15a3aa08e/bin/mosafe) · [SKILL.md](https://github.com/damionrashford/media-os/blob/5014c1e8b23fd3e18d49926d9aa147d15a3aa08e/skills/ffmpeg-streaming/SKILL.md) · [SKILL.md](https://github.com/damionrashford/media-os/blob/5014c1e8b23fd3e18d49926d9aa147d15a3aa08e/skills/ffmpeg-quality/SKILL.md) · [SKILL.md](https://github.com/damionrashford/media-os/blob/5014c1e8b23fd3e18d49926d9aa147d15a3aa08e/skills/ffmpeg-transcode/SKILL.md) |

<a id="nt-c2pa-mcp"></a>

### c2pa-mcp (Content Credentials MCP)

| Thuộc tính | Giá trị |
|---|---|
| Repo | https://github.com/contentauth/c2pa-mcp |
| License | MIT OR Apache-2.0 (hai file LICENSE-MIT và LICENSE-APACHE) |
| Phiên bản đã đọc | `ef521f06dc3900fcc5afdc8ad9fe846011c44f0d` (commit 2026-03-27) |
| Kiểm chứng | 2026-11-23; code-read; đã đọc LICENSE-MIT, LICENSE-APACHE, Cargo.toml, README.md, src/reader.rs, src/main.rs, src/mcp.rs, src/settings.json, .github/workflows/release.yml; chưa chạy upstream |
| Khoảng trống lấp | Provenance và C2PA cho media (cầu nối agent với SDK c2pa-rs) |
| Cơ chế đáng học | - Server MCP stdio nhỏ (khoảng 500 dòng Rust trong `src/`) với hai tool `read_credentials_file` và `read_credentials_url`, trả JSON `success`, `hasCredentials`, `manifestData` (`src/mcp.rs`).<br>- Khi khởi động tải bốn danh sách tin cậy (C2PA trust list, TSA, và hai danh sách ITL) từ raw.githubusercontent.com ghép thành PEM rồi nạp vào `c2pa::Context` (`src/main.rs`, `src/reader.rs`); nếu tải hỏng thì chạy tiếp mà không có trust anchor.<br>- Cấu hình `verify_after_reading` và `remote_manifest_fetch` đều bật trong `src/settings.json`. |
| Tiêu chí và cách kiểm | Chỉ có một unit test (đọc file rỗng trả `has_credentials=false`); workflow duy nhất là `release.yml` (build ma trận khi gắn tag) và mình không thấy bước chạy test trong phần đã đọc. Không có kiểm chứng tự động chữ ký trên mẫu thật trong repo; mình chưa chạy. |
| Giới hạn và rủi ro | Cả hai tool đọc đường dẫn hoặc URL do agent cung cấp: file đọc được bất kỳ đường dẫn nào (không allowlist), URL chỉ kiểm tiền tố http/https và timeout 60 giây, không giới hạn kích thước hay chặn địa chỉ nội bộ (rủi ro SSRF nếu agent bị tiêm lệnh); `remote_manifest_fetch` có thể kéo thêm manifest từ xa. Không có trust anchor khi tải danh sách lỗi: kết quả xác thực kém tin cậy hơn nhưng vẫn trả thành công. Cài bằng `curl \| sh` từ nhánh main. Dự án mới (v0.2.2), ít sao. |
| So với | c2pa-rs-cai-rust-sdk, c2patool, c2pa-specifications |
| Nguồn | [LICENSE-MIT](https://github.com/contentauth/c2pa-mcp/blob/ef521f06dc3900fcc5afdc8ad9fe846011c44f0d/LICENSE-MIT) · [LICENSE-APACHE](https://github.com/contentauth/c2pa-mcp/blob/ef521f06dc3900fcc5afdc8ad9fe846011c44f0d/LICENSE-APACHE) · [Cargo.toml](https://github.com/contentauth/c2pa-mcp/blob/ef521f06dc3900fcc5afdc8ad9fe846011c44f0d/Cargo.toml) · [README.md](https://github.com/contentauth/c2pa-mcp/blob/ef521f06dc3900fcc5afdc8ad9fe846011c44f0d/README.md) · [reader.rs](https://github.com/contentauth/c2pa-mcp/blob/ef521f06dc3900fcc5afdc8ad9fe846011c44f0d/src/reader.rs) · [main.rs](https://github.com/contentauth/c2pa-mcp/blob/ef521f06dc3900fcc5afdc8ad9fe846011c44f0d/src/main.rs) · [mcp.rs](https://github.com/contentauth/c2pa-mcp/blob/ef521f06dc3900fcc5afdc8ad9fe846011c44f0d/src/mcp.rs) · [settings.json](https://github.com/contentauth/c2pa-mcp/blob/ef521f06dc3900fcc5afdc8ad9fe846011c44f0d/src/settings.json) · [release.yml](https://github.com/contentauth/c2pa-mcp/blob/ef521f06dc3900fcc5afdc8ad9fe846011c44f0d/.github/workflows/release.yml) |

<a id="dr-2026-11-24"></a>

## Bổ sung drama-skills — 23/11/2026

Hồ sơ lập từ ảnh người dùng gửi; đọc mã tại commit cố định, chưa chạy.

<a id="dr-drama-skills"></a>

### drama-skills (bộ skill phim ngắn AI)

| Thuộc tính | Giá trị |
|---|---|
| Repo | https://github.com/zenstory-ai/drama-skills |
| License | MIT (một file LICENSE ở gốc, ghi "drama-skills contributors") |
| Phiên bản đã đọc | `7fed9dfcd33c5a3134ff1b51709dd826488b5aab` (commit 2026-11-22, release v0.13.0); ★ 4.850 theo GitHub API ngày 2026-11-24 (infographic của dự án ghi 4.389, là số cũ hơn) |
| Kiểm chứng | 2026-11-24; code-read; đã đọc LICENSE, README_EN.md, pyproject.toml, `skills/short-drama-produce/scripts/production_tool.py` (đoạn xác nhận và so khớp đầu vào), `provider_adapters.py` (đoạn gọi HTTP và đọc biến môi trường) và `skills/short-drama/scripts/dashboard_server.py` (đoạn bind và kiểm tra yêu cầu); chưa chạy mã, chưa đọc skill dựng phim (Remotion), thư mục `evaluations/` và `tests/` |
| Khoảng trống lấp | Bộ 12 skill cho quy trình phim ngắn AI (phân tích truyện, kịch bản, thiết lập hình ảnh, storyboard, prompt ảnh/video, sản xuất, dựng, duyệt); chỉ tham khảo cho phòng KT-AT-CL, không dùng trực tiếp cho công việc chất lượng chai khí |
| Cơ chế đáng học | - Thư mục `skills/` có đúng 12 skill; 7 skill có script Python (`short-drama`, `-edit`, `-write`, `-produce`, `-develop`, `-breakdown`, `-novel-analyze`), 5 skill chỉ là tài liệu, khớp với README.<br>- **Cổng xác nhận gắn với dấu vân tay của job**: `production_tool.py` sinh chuỗi `CONFIRM <job_id> <12 ký tự đầu của fingerprint>`; `confirm_job` từ chối nếu chuỗi không khớp, và khi chạy lại mà đầu vào đã đổi (so băm SHA-256 của file hoặc đoạn nguồn) thì báo `ConfirmationRequiredError: job inputs changed; prepare and confirm again`. Đây là mẫu đáng tham khảo cho cổng "đã xác nhận đủ dữ liệu rồi mới gửi mail tự động" của báo cáo chất lượng: xác nhận không dùng lại được khi dữ liệu nguồn đã đổi.<br>- Dashboard cục bộ (`dashboard_server.py`) mặc định bind `127.0.0.1`, từ chối host không phải loopback, sinh token truy cập ngẫu nhiên mỗi lần chạy (`secrets.token_urlsafe(32)`), tiền tố API ngẫu nhiên, kiểm header `Origin` và so token bằng `hmac.compare_digest`.<br>- Khóa API không nằm trong mã: nhà cung cấp (OpenAI, Seedance qua Volcengine, MiniMax) được gọi bằng `urllib` với địa chỉ gốc và tên mô hình lấy từ biến môi trường hoặc tham số, thiếu thì báo lỗi. |
| Tiêu chí và cách kiểm | Có thư mục `tests/` (33 file) và `evaluations/`, chưa đọc nội dung và chưa chạy. Cổng xác nhận có thể kiểm bằng cách: tạo job, đổi một file đầu vào, chạy lại và mong đợi lỗi `job inputs changed`. |
| Giới hạn và rủi ro | (1) Kịch bản, ảnh tham chiếu và prompt được gửi tới nhà cung cấp bên thứ ba, trong đó có dịch vụ đặt tại Trung Quốc (Volcengine); không dùng với nội dung nội bộ hoặc nhạy cảm. (2) Cổng xác nhận chặn việc gọi API trả phí, còn các cảnh báo trong `_preview_warnings` chỉ là nhắc nhở ("soft gate"), không chặn; không suy ra toàn bộ quy trình đều bị chặn. (3) Cài bằng `npx skills add zenstory-ai/drama-skills -y -g` qua một trình cài đặt bên thứ ba, chưa đọc trình đó. (4) Các số liệu của dự án ("hơn một nghìn dự án", "gần 80.000 dòng GUI") chỉ là tuyên bố trong README. (5) Chưa đọc phần dựng phim (Remotion) và render, nên chưa biết nó tải gì lúc chạy. |
| So với | awesome-short-drama-skills (danh sách tuyển chọn, chưa đọc), short-drama-skills của YvonneMovingon (chưa đọc) |
| Nguồn | [LICENSE](https://github.com/zenstory-ai/drama-skills/blob/7fed9dfcd33c5a3134ff1b51709dd826488b5aab/LICENSE) · [README_EN.md](https://github.com/zenstory-ai/drama-skills/blob/7fed9dfcd33c5a3134ff1b51709dd826488b5aab/README_EN.md) · [pyproject.toml](https://github.com/zenstory-ai/drama-skills/blob/7fed9dfcd33c5a3134ff1b51709dd826488b5aab/pyproject.toml) · [skills/short-drama-produce/scripts/production_tool.py](https://github.com/zenstory-ai/drama-skills/blob/7fed9dfcd33c5a3134ff1b51709dd826488b5aab/skills/short-drama-produce/scripts/production_tool.py) · [skills/short-drama-produce/scripts/provider_adapters.py](https://github.com/zenstory-ai/drama-skills/blob/7fed9dfcd33c5a3134ff1b51709dd826488b5aab/skills/short-drama-produce/scripts/provider_adapters.py) · [skills/short-drama/scripts/dashboard_server.py](https://github.com/zenstory-ai/drama-skills/blob/7fed9dfcd33c5a3134ff1b51709dd826488b5aab/skills/short-drama/scripts/dashboard_server.py) · [metadata GitHub](https://api.github.com/repos/zenstory-ai/drama-skills) |

<a id="n2-2026-11-24"></a>

## Nâng trần đợt hai — 23/11/2026

Hồ sơ lập trong đợt nâng trần thứ hai: đọc mã hoặc tài liệu tại commit cố định, chưa chạy upstream; mô tả của trinh sát sai ở nhiều repo nên điều ghi ở đây là điều đã đọc.

<a id="n2-ebur128-rust"></a>

### ebur128 (Rust)

| Thuộc tính | Giá trị |
|---|---|
| Repo | https://github.com/sdroege/ebur128 |
| License | MIT |
| Phiên bản đã đọc | `241d390ce4d64036f03d8a242b59c1c16689d74f` (commit 2026-10-27) |
| Kiểm chứng | 2026-11-24; code-read; đã đọc README.md, LICENSE, Cargo.toml, CHANGELOG.md, tests/reference_tests.rs, src/ebur128.rs, .github/workflows/ebur128.yml; chưa chạy upstream |
| Khoảng trống lấp | Cổng chất lượng video tất định (loudness, VMAF, timecode): đo loudness EBU R128 làm cổng tất định trong pipeline |
| Cơ chế đáng học | • Bản Rust của libebur128: chế độ M, S, I, LRA, sample peak và true peak chọn bằng cờ `Mode` (`src/ebur128.rs`), API `loudness_global`, `loudness_range`, `true_peak`.<br>• Test tham chiếu (`tests/reference_tests.rs`) chạy các file thuộc bộ EBU Loudness Test Set (TECH 3341/3342) và so với giá trị chuẩn với dung sai tuyệt đối 0,1 LU cho loudness toàn cục.<br>• Có `capi` tương thích ABI libebur128 qua cargo-c và bản test C kiểm với valgrind (`capi-test/`). |
| Tiêu chí và cách kiểm | CI (`ebur128.yml`): rustfmt, clippy với `-D warnings`, test tham chiếu EBU trên stable, beta, nightly (tải bộ mẫu từ bản sao GitHub, kiểm SHA-256 trước khi giải nén), test so với libebur128 bản C và quickcheck, build MSRV Rust 1.60, valgrind cho C API. Ngưỡng đạt là dung sai EBU của bộ test (0,1 LU cho loudness toàn cục); CHANGELOG 0.1.11 ghi đã sửa chênh lệch cuối bit giữa nền tảng không SSE2 và x86, tức tác giả quan tâm tới tính tái lập. |
| Giới hạn và rủi ro | MIT, tác giả Jan Kokemüller và Sebastian Dröge. Thư viện đo chứ không phải CLI: muốn làm cổng phải tự viết lớp bọc đọc audio, đặt ngưỡng (ví dụ -23 LUFS) và xử lý lỗi. Nhận đầu vào dạng mẫu chưa giải mã, không đọc container video. Workflow dùng action cũ (`actions-rs/*`, `actions/checkout@v2`) không ghim SHA. Mô tả trinh sát đúng; số sao 135 chưa xác minh. Không telemetry (thư viện thuần tính toán). |
| So với | libebur128 (bản C gốc, cùng chức năng), vmaf, ffmpeg-quality-metrics (cổng chất lượng hình, bổ sung cho âm thanh) |
| Nguồn | [README.md](https://github.com/sdroege/ebur128/blob/241d390ce4d64036f03d8a242b59c1c16689d74f/README.md) · [LICENSE](https://github.com/sdroege/ebur128/blob/241d390ce4d64036f03d8a242b59c1c16689d74f/LICENSE) · [Cargo.toml](https://github.com/sdroege/ebur128/blob/241d390ce4d64036f03d8a242b59c1c16689d74f/Cargo.toml) · [CHANGELOG.md](https://github.com/sdroege/ebur128/blob/241d390ce4d64036f03d8a242b59c1c16689d74f/CHANGELOG.md) · [reference_tests.rs](https://github.com/sdroege/ebur128/blob/241d390ce4d64036f03d8a242b59c1c16689d74f/tests/reference_tests.rs) · [ebur128.rs](https://github.com/sdroege/ebur128/blob/241d390ce4d64036f03d8a242b59c1c16689d74f/src/ebur128.rs) · [ebur128.yml](https://github.com/sdroege/ebur128/blob/241d390ce4d64036f03d8a242b59c1c16689d74f/.github/workflows/ebur128.yml) |

<a id="n2-video-quality-metrics-vqm"></a>

### Video Quality Metrics (VQM)

| Thuộc tính | Giá trị |
|---|---|
| Repo | https://github.com/CrypticSignal/video-quality-metrics |
| License | MIT |
| Phiên bản đã đọc | `acbd775b94acd125afd97d1de708743f0315bfe4` (commit 2026-11-08) |
| Kiểm chứng | 2026-11-24; code-read; đã đọc README.md, LICENSE, main.py, ffmpeg_tasks.py, metrics.py, tests.py; chưa chạy upstream |
| Khoảng trống lấp | Cổng chất lượng video tất định: so VMAF, PSNR, SSIM giữa các giá trị tham số encoder |
| Cơ chế đáng học | - ffmpeg_tasks.py dựng một filtergraph FFmpeg duy nhất: đặt lại PTS, ép khung hình tham chiếu và bản nén cùng độ phân giải (scale bicubic) rồi gọi bộ lọc libvmaf kèm PSNR và float_ssim; hai đầu vào dùng cùng tùy chọn tốc độ khung để ghép khung theo thứ tự.<br>- main.py có reason_to_recalculate: chỉ dùng lại file điểm JSON đã lưu khi file còn mới hơn bản transcode và settings lưu kèm trùng settings hiện tại.<br>- metrics.py đọc log JSON per-frame của libvmaf, tính trung bình, xuất report.html một file có đồ thị. |
| Tiêu chí và cách kiểm | Không có ngưỡng đạt/trượt hay mã thoát theo điểm trong các file đã đọc: công cụ báo cáo và tô xanh giá trị cao nhất, người dùng tự quyết (chưa xác minh toàn mã). Kiểm bằng máy: tests.py (unittest, gồm test đầu cuối chạy main.py trên ForBiggerFun.mp4) và CI dùng ruff format/check; CI cài FFmpeg có libvmaf và kiểm bộ lọc tồn tại, nếu thiếu thì test e2e bị bỏ qua chứ không đỏ khi chạy local. |
| Giới hạn và rủi ro | License MIT. Không thấy telemetry trong file đã đọc (chưa xác minh toàn mã). Cần FFmpeg có libvmaf; CI tải bản BtbN latest không ghim phiên bản. PSNR và SSIM chỉ trên kênh Y; mô hình VMAF dành cho SDR (có cảnh báo khi HDR). Bản VMAF 4K và HD dùng file model kèm trong repo. |
| So với | VMAF, ffmpeg-quality-metrics |
| Nguồn | [README.md](https://github.com/CrypticSignal/video-quality-metrics/blob/acbd775b94acd125afd97d1de708743f0315bfe4/README.md) · [LICENSE](https://github.com/CrypticSignal/video-quality-metrics/blob/acbd775b94acd125afd97d1de708743f0315bfe4/LICENSE) · [main.py](https://github.com/CrypticSignal/video-quality-metrics/blob/acbd775b94acd125afd97d1de708743f0315bfe4/main.py) · [ffmpeg_tasks.py](https://github.com/CrypticSignal/video-quality-metrics/blob/acbd775b94acd125afd97d1de708743f0315bfe4/ffmpeg_tasks.py) · [metrics.py](https://github.com/CrypticSignal/video-quality-metrics/blob/acbd775b94acd125afd97d1de708743f0315bfe4/metrics.py) · [tests.py](https://github.com/CrypticSignal/video-quality-metrics/blob/acbd775b94acd125afd97d1de708743f0315bfe4/tests.py) · [requirements.txt](https://github.com/CrypticSignal/video-quality-metrics/blob/acbd775b94acd125afd97d1de708743f0315bfe4/requirements.txt) · [tests.yml](https://github.com/CrypticSignal/video-quality-metrics/blob/acbd775b94acd125afd97d1de708743f0315bfe4/.github/workflows/tests.yml) |

<a id="n2-vmafx"></a>

### VMAFx

| Thuộc tính | Giá trị |
|---|---|
| Repo | https://github.com/vidiko/vmafx |
| License | EUPL-1.2 (mã do fork viết) + BSD-2-Clause-Patent (mã kế thừa Netflix) + giấy phép riêng từng file |
| Phiên bản đã đọc | `6da90915748d2d4e4cf5881b33635edaea285a13` (commit 2026-11-23) |
| Kiểm chứng | 2026-11-24; code-read; đã đọc README.md, LICENSE, NOTICE, REUSE.toml, docs/licensing.md, AGENTS.md; chưa chạy upstream |
| Khoảng trống lấp | Cổng chất lượng video tất định: VMAF kèm hợp đồng tương đương số học giữa CPU, GPU và SIMD |
| Cơ chế đáng học | - Fork của Netflix/vmaf thêm backend CUDA, SYCL, HIP, Metal và đường SIMD; README coi ba cặp tham chiếu Netflix là cổng CI bắt buộc.<br>- scripts/ci/cross_backend_parity_gate.py chạy binary vmaf một lần cho mỗi backend, so metric từng khung với dung sai riêng từng đặc trưng (FEATURE_TOLERANCE, mặc định 5e-5 tức places=4; cặp song sinh chính xác là EXACT_TWINS; FP16 là 1e-2), xuất JSON và Markdown, mã thoát 0/1/2.<br>- Workflow tests-and-quality-gates.yml có job Netflix CPU Golden chạy pytest trên ca vmaf_runner và có bước kế hoạch tác động CI (plan-ci-impact.py) để bỏ qua cổng nặng kèm lý do ghi lại.<br>- mcp-server/vmaf-mcp có tool-contract.json liệt kê công cụ MCP (score, compare_models, describe_worst_frames). |
| Tiêu chí và cách kiểm | Dung sai theo đặc trưng đặt trong mã và mỗi lần siết phải qua ADR; thông điệp trong file nói rõ không sửa assertion vàng của Netflix. Kiểm bằng máy: golden pytest, cổng parity theo ma trận (feature, cặp backend), 55 workflow (sanitizer, fuzz, scorecard, REUSE, supply-chain...). Tuyên bố điểm khớp từng byte với Netflix chưa được tự chạy lại (chưa xác minh). |
| Giới hạn và rủi ro | Mô tả của trinh sát (VMAF tăng tốc GPU/SIMD, còn rất mới) đúng một phần: đây là fork có 1472 file ADR và harness agent dày (AGENTS.md, .claude, .agents), nhiều phần do agent sinh, cần kiểm độc lập. License lẫn: mã mới EUPL-1.2 (copyleft, nghĩa vụ cung cấp mã nguồn khi phân phối libvmaf), mã Netflix giữ BSD-2-Clause-Patent; docs/licensing.md nói bản libvmaf phân phối liên kết cả hai nên chịu EUPL-1.2; muốn giấy phép dễ dãi thì dùng Netflix/vmaf gốc. Bản fork có 7 sao (số của trinh sát), phát hành v1.0.0-rc.3. Chưa đọc telemetry của máy chủ MCP/K8s (chưa xác minh). |
| So với | VMAF, ffmpeg-quality-metrics |
| Nguồn | [README.md](https://github.com/vidiko/vmafx/blob/6da90915748d2d4e4cf5881b33635edaea285a13/README.md) · [LICENSE](https://github.com/vidiko/vmafx/blob/6da90915748d2d4e4cf5881b33635edaea285a13/LICENSE) · [NOTICE](https://github.com/vidiko/vmafx/blob/6da90915748d2d4e4cf5881b33635edaea285a13/NOTICE) · [REUSE.toml](https://github.com/vidiko/vmafx/blob/6da90915748d2d4e4cf5881b33635edaea285a13/REUSE.toml) · [licensing.md](https://github.com/vidiko/vmafx/blob/6da90915748d2d4e4cf5881b33635edaea285a13/docs/licensing.md) · [AGENTS.md](https://github.com/vidiko/vmafx/blob/6da90915748d2d4e4cf5881b33635edaea285a13/AGENTS.md) · [tests-and-quality-gates.yml](https://github.com/vidiko/vmafx/blob/6da90915748d2d4e4cf5881b33635edaea285a13/.github/workflows/tests-and-quality-gates.yml) · [cross_backend_parity_gate.py](https://github.com/vidiko/vmafx/blob/6da90915748d2d4e4cf5881b33635edaea285a13/scripts/ci/cross_backend_parity_gate.py) · [tool-contract.json](https://github.com/vidiko/vmafx/blob/6da90915748d2d4e4cf5881b33635edaea285a13/mcp-server/vmaf-mcp/tool-contract.json) |

<a id="n2-otio-aaf-adapter"></a>

### OpenTimelineIO AAF Adapter

| Thuộc tính | Giá trị |
|---|---|
| Repo | https://github.com/OpenTimelineIO/otio-aaf-adapter |
| License | Apache-2.0 |
| Phiên bản đã đọc | `47886982d67c00573ad4a565ae51ad0e73f4caff` (commit 2026-09-21) |
| Kiểm chứng | 2026-11-24; code-read; đã đọc README.md, LICENSE.txt, pyproject.toml, .github/workflows/ci.yaml, src/otio_aaf_adapter/plugin_manifest.json, src/otio_aaf_adapter/adapters/advanced_authoring_format.py; chưa chạy upstream |
| Khoảng trống lấp | Trao đổi timeline và timecode (OpenTimelineIO) với Avid qua định dạng AAF |
| Cơ chế đáng học | - Plugin OTIO tên AAF đăng ký bằng plugin_manifest.json và entry point opentimelineio.plugins; đọc/ghi qua pyaaf2 trong advanced_authoring_format.py (hơn 2000 dòng) và aaf_writer.py.<br>- Timecode: _get_mob_start_tc lấy TC bắt đầu từ track timecode của mob rồi gán vào global_start_time; test có mẫu 29,97 fps và drop-frame (2997fps-DFTC.aaf, kỳ vọng 05:00:00;00 ở 30000/1001).<br>- Bốn hook (otio_aaf_pre/post_read/write_transcribe) trong hooks.py cho phép nhúng xử lý riêng quanh quá trình chuyển đổi. |
| Tiêu chí và cách kiểm | tests/test_aaf_adapter.py (khoảng 70 test, mẫu AAF thật trong tests/sample_data); CI chạy flake8, dựng wheel/sdist, rồi ma trận ubuntu, windows-2022, macos-15 với OTIO main và 0.18.1 và Python 3.9 đến 3.12 (Codecov chỉ một ô). Bảng tính năng trong README tự khai: chưa có hiệu ứng, tốc độ phức tạp, CDL, chuỗi ảnh (chưa xác minh bằng chạy). |
| Giới hạn và rủi ro | License Apache-2.0 (LICENSE.txt; README trỏ nhầm LICENSE.md). Commit gần nhất trên nhánh mặc định là 2026-09-21, ngày push 2026-10-22 của trinh sát thuộc nhánh khác. Đang tách khỏi OTIO lõi nên API có thể đổi; CI cài OTIO main từ git. Classifier liệt kê Python 3.7 và 3.8 dù requires-python lớn hơn 3.9. Phụ thuộc pyaaf2 do bên thứ ba bảo trì. |
| So với | OpenTimelineIO |
| Nguồn | [README.md](https://github.com/OpenTimelineIO/otio-aaf-adapter/blob/47886982d67c00573ad4a565ae51ad0e73f4caff/README.md) · [LICENSE.txt](https://github.com/OpenTimelineIO/otio-aaf-adapter/blob/47886982d67c00573ad4a565ae51ad0e73f4caff/LICENSE.txt) · [pyproject.toml](https://github.com/OpenTimelineIO/otio-aaf-adapter/blob/47886982d67c00573ad4a565ae51ad0e73f4caff/pyproject.toml) · [ci.yaml](https://github.com/OpenTimelineIO/otio-aaf-adapter/blob/47886982d67c00573ad4a565ae51ad0e73f4caff/.github/workflows/ci.yaml) · [plugin_manifest.json](https://github.com/OpenTimelineIO/otio-aaf-adapter/blob/47886982d67c00573ad4a565ae51ad0e73f4caff/src/otio_aaf_adapter/plugin_manifest.json) · [advanced_authoring_format.py](https://github.com/OpenTimelineIO/otio-aaf-adapter/blob/47886982d67c00573ad4a565ae51ad0e73f4caff/src/otio_aaf_adapter/adapters/advanced_authoring_format.py) · [hooks.py](https://github.com/OpenTimelineIO/otio-aaf-adapter/blob/47886982d67c00573ad4a565ae51ad0e73f4caff/src/otio_aaf_adapter/adapters/aaf_adapter/hooks.py) · [test_aaf_adapter.py](https://github.com/OpenTimelineIO/otio-aaf-adapter/blob/47886982d67c00573ad4a565ae51ad0e73f4caff/tests/test_aaf_adapter.py) |

<a id="n2-otio-js-bindings"></a>

### OpenTimelineIO JS Bindings

| Thuộc tính | Giá trị |
|---|---|
| Repo | https://github.com/JeanChristopheMorinPerso/OpenTimelineIO-JS-Bindings |
| License | Apache-2.0 |
| Phiên bản đã đọc | `6f222d68ca1844c6b2598ec21589a07ece5bf915` (commit 2026-11-22) |
| Kiểm chứng | 2026-11-24; code-read; đã đọc README.md, LICENSE, package.json, .gitmodules, src/CMakeLists.txt, src/opentime/bindings.cpp; chưa chạy upstream |
| Khoảng trống lấp | Trao đổi timeline và timecode (OpenTimelineIO) cho JavaScript và trình duyệt |
| Cơ chế đáng học | - Biên dịch lõi C++ của OpenTimelineIO (submodule deps/OpenTimelineIO) sang WebAssembly bằng Emscripten/embind, xuất module MODULARIZE (src/CMakeLists.txt); src/opentime/bindings.cpp mở RationalTime, to_timecode, to_nearest_timecode.<br>- Vòng đời đối tượng chia sẻ giữa JS và retainer của OTIO: người dùng phải gọi delete() trên mọi handle trả về.<br>- Test Jest (tests/rationaltime.test.js và tests/opentimelineio) chạy trên bản build trong install/; README ghi test hồi quy Marker.2 chạy dạng expected failure. |
| Tiêu chí và cách kiểm | CI tests.yaml build Release và Debug bằng emscripten, cài và chạy pnpm test, kèm job coverage C++. Đo bằng máy nhưng chỉ các API đã bind; mức bao phủ so với OTIO Python nằm ở scripts/api-coverage (chưa đọc). |
| Giới hạn và rủi ro | Mô tả trinh sát hơi sai: repo nằm dưới tài khoản cá nhân của một maintainer, không thuộc tổ chức OpenTimelineIO, và README tự nói còn đang làm dở (work in progress). package.json ghi version 0.15.0 trong khi submodule ghim OTIO main 0.19 phát triển; chưa thấy bằng chứng phát hành npm (chưa xác minh). Clone nông không nạp submodule nên mã C++ upstream chưa đọc. Phải tự quản lý bộ nhớ bằng delete(), dễ rò rỉ. License Apache-2.0. |
| So với | OpenTimelineIO, Mediabunny |
| Nguồn | [README.md](https://github.com/JeanChristopheMorinPerso/OpenTimelineIO-JS-Bindings/blob/6f222d68ca1844c6b2598ec21589a07ece5bf915/README.md) · [LICENSE](https://github.com/JeanChristopheMorinPerso/OpenTimelineIO-JS-Bindings/blob/6f222d68ca1844c6b2598ec21589a07ece5bf915/LICENSE) · [package.json](https://github.com/JeanChristopheMorinPerso/OpenTimelineIO-JS-Bindings/blob/6f222d68ca1844c6b2598ec21589a07ece5bf915/package.json) · [.gitmodules](https://github.com/JeanChristopheMorinPerso/OpenTimelineIO-JS-Bindings/blob/6f222d68ca1844c6b2598ec21589a07ece5bf915/.gitmodules) · [CMakeLists.txt](https://github.com/JeanChristopheMorinPerso/OpenTimelineIO-JS-Bindings/blob/6f222d68ca1844c6b2598ec21589a07ece5bf915/src/CMakeLists.txt) · [bindings.cpp](https://github.com/JeanChristopheMorinPerso/OpenTimelineIO-JS-Bindings/blob/6f222d68ca1844c6b2598ec21589a07ece5bf915/src/opentime/bindings.cpp) · [rationaltime.test.js](https://github.com/JeanChristopheMorinPerso/OpenTimelineIO-JS-Bindings/blob/6f222d68ca1844c6b2598ec21589a07ece5bf915/tests/rationaltime.test.js) · [tests.yaml](https://github.com/JeanChristopheMorinPerso/OpenTimelineIO-JS-Bindings/blob/6f222d68ca1844c6b2598ec21589a07ece5bf915/.github/workflows/tests.yaml) |

<a id="n2-timecode-agent"></a>

### timecode:agent (video-agent)

| Thuộc tính | Giá trị |
|---|---|
| Repo | https://github.com/mupozg823/timecode-agent |
| License | MIT |
| Phiên bản đã đọc | `02f7c5a9ce1c09b4ba49177d2a4dc8e9ee1bbc03` (commit 2026-08-07) |
| Kiểm chứng | 2026-11-24; code-read; đã đọc README.md, LICENSE, SECURITY.md, CONTRIBUTING.md, pyproject.toml, .github/workflows/ci.yml; chưa chạy upstream |
| Khoảng trống lấp | Bằng chứng video có dấu thời gian cho coding agent, xuất EDL, FCPXML, OTIO |
| Cơ chế đáng học | - Hai sổ ghi nối đuôi tách biệt: checkpoints.jsonl (khẳng định hiểu video) và sequences.jsonl (quyết định dựng); docs/ARCHITECTURE.md phân P0 đo vật lý, P1 nhận thức học máy, P2 khẳng định ngữ nghĩa, P3 quyết định dựng.<br>- export.py xuất edl, otio, fcpxml, xmeml, srt, md; với edl/otio/fcpxml có Receipt sidecar (schema tca-receipt-v1, artifact_sha256 và revision bằng chứng, không dấu thời gian nên tất định).<br>- decoded_timing.py chặn xuất NLE khi video biến thiên fps hoặc không đều cadence giải mã (_require_cfr_handoff), chỉ cho xuất văn bản.<br>- benchmarks/run_bench.py biến phần tất định thành cổng hồi quy trên ba video Blender CC-BY. |
| Tiêu chí và cách kiểm | Đã thấy: validate_export_request từ chối tổ hợp tùy chọn sai; benchmarks/run_bench.py đối chiếu golden-public.json. Tuyên bố README về cổng nhịp beat (p90 lệch nhỏ hơn hoặc bằng 40 ms) chưa mở boundary_eval.py để kiểm (chưa xác minh). |
| Giới hạn và rủi ro | Phát hiện chính: README có huy hiệu CI test, typecheck, package-smoke và CONTRIBUTING.md bảo chạy uv run pytest, nhưng cây git không có thư mục tests nào (0 file) và ci.yml chỉ có job package-smoke (dựng wheel, chạy va --version); tuyên bố có test/typecheck là quá mức ở commit này. Một người bảo trì, alpha; yêu cầu Python 3.12 đúng; tải mô hình whisper/sherpa lần đầu và gọi yt-dlp tới mạng khi ingest URL (có tùy chọn cookies trình duyệt, cần thận trọng). License MIT. |
| So với | video-use, claude-video (/watch), OpenTimelineIO |
| Nguồn | [README.md](https://github.com/mupozg823/timecode-agent/blob/02f7c5a9ce1c09b4ba49177d2a4dc8e9ee1bbc03/README.md) · [LICENSE](https://github.com/mupozg823/timecode-agent/blob/02f7c5a9ce1c09b4ba49177d2a4dc8e9ee1bbc03/LICENSE) · [SECURITY.md](https://github.com/mupozg823/timecode-agent/blob/02f7c5a9ce1c09b4ba49177d2a4dc8e9ee1bbc03/SECURITY.md) · [CONTRIBUTING.md](https://github.com/mupozg823/timecode-agent/blob/02f7c5a9ce1c09b4ba49177d2a4dc8e9ee1bbc03/CONTRIBUTING.md) · [pyproject.toml](https://github.com/mupozg823/timecode-agent/blob/02f7c5a9ce1c09b4ba49177d2a4dc8e9ee1bbc03/pyproject.toml) · [ci.yml](https://github.com/mupozg823/timecode-agent/blob/02f7c5a9ce1c09b4ba49177d2a4dc8e9ee1bbc03/.github/workflows/ci.yml) · [ARCHITECTURE.md](https://github.com/mupozg823/timecode-agent/blob/02f7c5a9ce1c09b4ba49177d2a4dc8e9ee1bbc03/docs/ARCHITECTURE.md) · [export.py](https://github.com/mupozg823/timecode-agent/blob/02f7c5a9ce1c09b4ba49177d2a4dc8e9ee1bbc03/src/video_agent/export.py) · [decoded_timing.py](https://github.com/mupozg823/timecode-agent/blob/02f7c5a9ce1c09b4ba49177d2a4dc8e9ee1bbc03/src/video_agent/decoded_timing.py) · [run_bench.py](https://github.com/mupozg823/timecode-agent/blob/02f7c5a9ce1c09b4ba49177d2a4dc8e9ee1bbc03/benchmarks/run_bench.py) |

<a id="n2-vietsub-studio"></a>

### VietSub Studio

| Thuộc tính | Giá trị |
|---|---|
| Repo | https://github.com/qvinh8726/VietSub-Studio |
| License | MIT |
| Phiên bản đã đọc | `d9a8367d88bf9a7a82e5a4cfc30771260e171477` (commit 2026-11-20) |
| Kiểm chứng | 2026-11-24; code-read; đã đọc README.md, LICENSE, requirements.txt, app.py, vietsub/editor/subtitles.py, vietsub/editor/compat_signer.py; chưa chạy upstream |
| Khoảng trống lấp | Phụ đề và dịch phụ đề tiếng Việt: OCR chữ cứng trong video, dịch, dựng lại |
| Cơ chế đáng học | - app.py (hơn 8000 dòng) điều phối VideOCR cho OCR theo vùng crop, hợp nhất các khối SRT gần nhau cùng chữ (write_merged_videocr_srt) và cắt đoạn dài (45 phút) để OCR/dịch từng khúc.<br>- Dịch qua Gemini Notebook, DeepSeek, OpenRouter hoặc API tương thích OpenAI; từ chối SRT thiếu, dính khối hoặc sai cấu trúc, khôi phục số thứ tự và timecode từ bản gốc.<br>- vietsub/editor/subtitles.py đổi SRT sang ASS an toàn (không thực thi định dạng HTML) để libass ghi cứng vào video. |
| Tiêu chí và cách kiểm | Tests: hơn 30 file unittest và test frontend Node; CI Windows chạy py_compile, unittest, kiểm cú pháp JS, rồi job desktop-ui chạy các script QA Playwright theo từng giai đoạn. Không có chỉ số chất lượng bản dịch: README nói rõ kiểm cấu trúc SRT không thay việc đọc lại nội dung. |
| Giới hạn và rủi ro | Mô tả trinh sát (quy trình OCR phụ đề và dịch, chỉ làm mẫu) thiếu phạm vi: đây là bộ công cụ ba workspace chỉ cho Windows, còn tải video từ Douyin, Kuaishou, Xiaohongshu, TikTok, tạo TTS và tự đăng lên nền tảng (Publish Hub), dính điều khoản từng nền tảng và quyền nội dung. compat_signer.py tự khai là cài lại độc lập một ứng viên thuật toán ký từ repo bên thứ ba cho TTS CapCut, không chắc là thuật toán chính thức, nên rủi ro điều khoản và gãy bất kỳ lúc nào. Văn bản SRT, nội dung TTS đi tới nhà cung cấp bên ngoài; khóa API dùng DPAPI. License MIT; 3 sao, một tác giả. |
| So với | VideoCaptioner, Pixelle-Video |
| Nguồn | [README.md](https://github.com/qvinh8726/VietSub-Studio/blob/d9a8367d88bf9a7a82e5a4cfc30771260e171477/README.md) · [LICENSE](https://github.com/qvinh8726/VietSub-Studio/blob/d9a8367d88bf9a7a82e5a4cfc30771260e171477/LICENSE) · [requirements.txt](https://github.com/qvinh8726/VietSub-Studio/blob/d9a8367d88bf9a7a82e5a4cfc30771260e171477/requirements.txt) · [app.py](https://github.com/qvinh8726/VietSub-Studio/blob/d9a8367d88bf9a7a82e5a4cfc30771260e171477/app.py) · [subtitles.py](https://github.com/qvinh8726/VietSub-Studio/blob/d9a8367d88bf9a7a82e5a4cfc30771260e171477/vietsub/editor/subtitles.py) · [compat_signer.py](https://github.com/qvinh8726/VietSub-Studio/blob/d9a8367d88bf9a7a82e5a4cfc30771260e171477/vietsub/editor/compat_signer.py) · [tests.yml](https://github.com/qvinh8726/VietSub-Studio/blob/d9a8367d88bf9a7a82e5a4cfc30771260e171477/.github/workflows/tests.yml) |

<a id="n2-ltx-2"></a>

### LTX-2

| Thuộc tính | Giá trị |
|---|---|
| Repo | https://github.com/Lightricks/LTX-2 |
| License | Apache-2.0 cho mã; trọng số theo giấy phép riêng LTX-2 Community License (LTX-2.3) và LTX-2.x Community License (LTX-2.5) |
| Phiên bản đã đọc | `daa6b16fc7f0f1628f2c9e36a303e3312b333cc6` (commit 2026-11-19) |
| Kiểm chứng | 2026-11-24; code-read; đã đọc README.md, LICENSE, LICENSE-2_x, CHANGELOG.md, `marking/__init__.py`, t2v_lora.yaml, wandb_logger.py, captioning.py; chưa chạy upstream |
| Khoảng trống lấp | Vận hành pipeline video cục bộ: chạy mô hình mở, huấn luyện LoRA, quản lý checkpoint và VRAM |
| Cơ chế đáng học | - Ghép gói pipeline theo tác vụ (`packages/ltx-pipelines/src/ltx_pipelines/`: `distilled.py`, `ti2vid_two_stages_hq.py`, `retake.py`, `ic_lora.py`, `dubit.py`...) có cờ `--quantization fp8-cast --offload` khi thiếu VRAM.<br>- Trainer cấu hình bằng YAML (`ltx-trainer/configs/t2v_lora.yaml`): chiến lược `flexible`, LoRA rank 32, tiền xử lý latent/điều kiện/âm thanh rồi mới huấn luyện, nhiều cấu hình mẫu cho inpainting/outpainting/extend.<br>- Gói đánh dấu `marking/` nạp Videoseal/AudioSeal từ thư mục pack bắt buộc đủ 5 file, import không cần extra.<br>- `captioning.py` gọi máy chủ vLLM cục bộ (127.0.0.1:8001) hoặc Gemini để dựng caption. |
| Tiêu chí và cách kiểm | Không thấy `.github/workflows` hay thư mục test ở mức tìm kiếm cấp 1 đến 4 của repo, nên không có cổng CI công khai; CHANGELOG ghi từng bản sửa lỗi (1.6.2 ngày 2026-11-12). Chất lượng sinh và điểm benchmark là tuyên bố của tác giả (chưa xác minh). Chưa tải trọng số hay chạy. |
| Giới hạn và rủi ro | Giấy phép trọng số LTX-2.x: doanh nghiệp doanh thu từ 10 triệu USD phải có giấy phép thương mại trả phí, kèm Acceptable Use Policy (Attachment A) cập nhật được và điều khoản trọng tài; LTX-2.3 theo LICENSE-2 riêng. Encoder văn bản Gemma giữ giấy phép Google. Yêu cầu GPU lớn (khoảng 66 GiB tải về). W&B tắt mặc định (`enabled: false`); `hf auth login` cần token Hugging Face. |
| So với | Wan2.2 (wan2-2), HunyuanVideo, CogVideoX (hồ sơ agentic-video có sẵn), ComfyUI (điều phối node, khác một mô hình đơn) |
| Nguồn | [LICENSE](https://github.com/Lightricks/LTX-2/blob/daa6b16fc7f0f1628f2c9e36a303e3312b333cc6/LICENSE) · [LICENSE-2_x](https://github.com/Lightricks/LTX-2/blob/daa6b16fc7f0f1628f2c9e36a303e3312b333cc6/LICENSE-2_x) · [README.md](https://github.com/Lightricks/LTX-2/blob/daa6b16fc7f0f1628f2c9e36a303e3312b333cc6/README.md) · [CHANGELOG.md](https://github.com/Lightricks/LTX-2/blob/daa6b16fc7f0f1628f2c9e36a303e3312b333cc6/CHANGELOG.md) · [`__init__.py`](https:`//github.com/Lightricks/LTX-2/blob/daa6b16fc7f0f1628f2c9e36a303e3312b333cc6/packages/ltx-pipelines/src/ltx_pipelines/marking/__init__.py`) · [t2v_lora.yaml](https://github.com/Lightricks/LTX-2/blob/daa6b16fc7f0f1628f2c9e36a303e3312b333cc6/packages/ltx-trainer/configs/t2v_lora.yaml) · [wandb_logger.py](https://github.com/Lightricks/LTX-2/blob/daa6b16fc7f0f1628f2c9e36a303e3312b333cc6/packages/ltx-trainer/src/ltx_trainer/wandb_logger.py) · [captioning.py](https://github.com/Lightricks/LTX-2/blob/daa6b16fc7f0f1628f2c9e36a303e3312b333cc6/packages/ltx-trainer/src/ltx_trainer/captioning.py) |

<a id="n2-jellyfish"></a>

### Jellyfish

| Thuộc tính | Giá trị |
|---|---|
| Repo | https://github.com/Forget-C/Jellyfish |
| License | Apache-2.0 (thư mục .agents/skills dùng MIT của tác giả khác) |
| Phiên bản đã đọc | `b1d8add653a97ebe89c2eb8cc7b712af800b8f3c` (commit 2026-11-23) |
| Kiểm chứng | 2026-11-24; code-read; đã đọc LICENSE, README.md, AGENTS_OVERVIEW.md, consistency_checker_agent.py, identity_references.py, automatic_checks.py, backend-tests.yml, commit-messages.yml; chưa chạy upstream |
| Khoảng trống lấp | Nhất quán nhân vật/phong cách trong xưởng phim ngắn (không phải huấn luyện LoRA) |
| Cơ chế đáng học | - `identity_references.py`: ràng buộc mỗi nhóm tham chiếu danh tính phải ứng với đúng một nhân vật/vật thể và một nguồn ảnh duy nhất, vi phạm thì `ValueError` từ chối nhận.<br>- `generation_canvas/automatic_checks.py`: đóng băng kế hoạch kiểm tự động khi nhận lệnh sinh, ước lượng số lần gọi, chỉ đẩy việc kiểm khi tác vụ sinh hoàn tất đủ đầu ra; thư mục cùng cấp có `check_duration.py`, `check_reference_media.py`, `check_rhythm.py`...<br>- `chains/agents/consistency_checker_agent.py`: agent LLM chỉ kiểm lỗi chữ và mâu thuẫn trong kịch bản, xuất JSON có `classification` (mâu thuẫn, mơ hồ, tùy chọn) và đoạn trích định vị.<br>- Trung tâm tác vụ bất đồng bộ cho văn bản, ảnh, video, có hủy và xem lỗi. |
| Tiêu chí và cách kiểm | Workflow `backend-tests.yml` chạy preflight môi trường rồi `uv run pytest -q`; `commit-messages.yml` kiểm tiêu đề commit bằng test Node. Có bộ test backend lớn (cả server trình duyệt cho canvas). Đã mở hai workflow này; chưa chạy test, các workflow khác chỉ biết tên. |
| Giới hạn và rủi ro | Apache-2.0; thư mục skill của agent mã hóa (.agents/skills) là MIT tác giả khác. Triển khai cần MySQL 9 và khóa nhà cung cấp mô hình ảnh/video trả phí nên prompt và ảnh tham chiếu rời máy tới nhà cung cấp. Tài liệu và prompt chủ yếu tiếng Trung; mã còn trẻ nên API có thể đổi. Không đọc phần lưu trữ file hay xác thực. |
| So với | short-video-factory, pixelle-video, ai-video-editor (hồ sơ agentic-video có sẵn, thiên về dựng tự động hơn là canvas kiểm tham chiếu) |
| Nguồn | [LICENSE](https://github.com/Forget-C/Jellyfish/blob/b1d8add653a97ebe89c2eb8cc7b712af800b8f3c/LICENSE) · [LICENSE](https://github.com/Forget-C/Jellyfish/blob/b1d8add653a97ebe89c2eb8cc7b712af800b8f3c/.agents/skills/LICENSE) · [README.md](https://github.com/Forget-C/Jellyfish/blob/b1d8add653a97ebe89c2eb8cc7b712af800b8f3c/README.md) · [AGENTS_OVERVIEW.md](https://github.com/Forget-C/Jellyfish/blob/b1d8add653a97ebe89c2eb8cc7b712af800b8f3c/backend/AGENTS_OVERVIEW.md) · [consistency_checker_agent.py](https://github.com/Forget-C/Jellyfish/blob/b1d8add653a97ebe89c2eb8cc7b712af800b8f3c/backend/app/chains/agents/consistency_checker_agent.py) · [identity_references.py](https://github.com/Forget-C/Jellyfish/blob/b1d8add653a97ebe89c2eb8cc7b712af800b8f3c/backend/app/services/directing/identity_references.py) · [automatic_checks.py](https://github.com/Forget-C/Jellyfish/blob/b1d8add653a97ebe89c2eb8cc7b712af800b8f3c/backend/app/services/generation_canvas/automatic_checks.py) · [backend-tests.yml](https://github.com/Forget-C/Jellyfish/blob/b1d8add653a97ebe89c2eb8cc7b712af800b8f3c/.github/workflows/backend-tests.yml) · [commit-messages.yml](https://github.com/Forget-C/Jellyfish/blob/b1d8add653a97ebe89c2eb8cc7b712af800b8f3c/.github/workflows/commit-messages.yml) |

<a id="n2-duix-avatar"></a>

### Duix Avatar

| Thuộc tính | Giá trị |
|---|---|
| Repo | https://github.com/duixcom/Duix-Avatar |
| License | Duix.com Community License (tùy biến, GitHub báo NOASSERTION); không phải OSI, ngưỡng 1.000 MAU, buộc ghi nhãn |
| Phiên bản đã đọc | `1328feb5871448c8fa3d0e45b3bbc87e7c1d458a` (commit 2026-04-21) |
| Kiểm chứng | 2026-11-24; code-read; đã đọc LICENSE, README, compose, `video.js`, `f2f.js`, `config.js`; chưa chạy upstream |
| Khoảng trống lấp | Mặt/miệng và avatar nói (lip-sync, talking head) |
| Cơ chế đáng học | - Ứng dụng khách Electron chỉ làm điều phối: `src/main/api/f2f.js` gọi `POST /easy/submit` và `GET /easy/query?code=` tới container sinh video ở cổng 8383; `src/main/config/config.js` trỏ TTS tới cổng 18180.<br>- `src/main/service/video.js` quản lý hàng đợi tác vụ trong cơ sở dữ liệu cục bộ (trạng thái `draft`, `waiting`, hiển thị tiến độ `vị trí / tổng số hàng chờ`), tách khâu tạo giọng (`voice.js`) khỏi khâu ghép hình.<br>- `deploy/docker-compose*.yml` đóng gói ba dịch vụ (fun-asr, fish-speech-ziming, duix.avatar) với biến thể lite chỉ còn dịch vụ sinh video; có biến thể riêng cho Linux và GPU dòng 50. |
| Tiêu chí và cách kiểm | Không có workflow CI (`.github` không tồn tại) và không thấy thư mục test trong cấp 1–2; kiểm bằng máy: không có. Cách dùng thật là chạy compose rồi gọi API cục bộ; yêu cầu nêu trong README: GPU NVIDIA, ổ D còn hơn 30 GB, ổ C hơn 100 GB, tải khoảng 70 GB lần đầu (tuyên bố của tác giả, chưa xác minh). |
| Giới hạn và rủi ro | License: LICENSE của repo là thỏa thuận cộng đồng Duix.com, không phải OSI; cấp quyền dùng/sửa/phân phối nhưng buộc ghi "Built with DUIX.COM", kèm Notice, đặt tên "DUIX.COM" ở đầu tên mô hình AI huấn luyện từ tài liệu này, và cho Duix quyền vĩnh viễn dùng các ca/ứng dụng bạn tạo (mục 5c). Mục 2 yêu cầu xin giấy phép thương mại khi trên 1.000 MAU, trong khi bảng README ghi ngưỡng 100.000 người dùng hoặc doanh thu trên 10 triệu USD: hai nguồn lệch nhau, cần coi LICENSE là nguồn ràng buộc. Hai file PDF thỏa thuận cho mô hình có trong repo nhưng chưa đọc nội dung (chưa xác minh). Trọng số nằm trong image `guiji2025/*` trên Docker Hub, không kiểm được trong repo. Compose dùng `privileged: true`; `dev-app-update.yml` còn URL mẫu example.com nên cập nhật tự động chưa cấu hình; mã dev còn IP nội bộ cứng. Không đọc mã Python của container, nên chất lượng lip-sync chưa xác minh. Mô tả của trinh sát (NOASSERTION) đúng ở mặt GitHub, nhưng bỏ sót điều kiện thương mại. |
| So với | HyperFrames (dựng video bằng HTML), LiveAvatar Agent Skills và HeyGen Skills (avatar qua dịch vụ trả phí, không chạy cục bộ). |
| Nguồn | [LICENSE](https://github.com/duixcom/Duix-Avatar/blob/1328feb5871448c8fa3d0e45b3bbc87e7c1d458a/LICENSE) · [README.md](https://github.com/duixcom/Duix-Avatar/blob/1328feb5871448c8fa3d0e45b3bbc87e7c1d458a/README.md) · [docker-compose-lite.yml](https://github.com/duixcom/Duix-Avatar/blob/1328feb5871448c8fa3d0e45b3bbc87e7c1d458a/deploy/docker-compose-lite.yml) · [docker-compose.yml](https://github.com/duixcom/Duix-Avatar/blob/1328feb5871448c8fa3d0e45b3bbc87e7c1d458a/deploy/docker-compose.yml) · [video.js](https://github.com/duixcom/Duix-Avatar/blob/1328feb5871448c8fa3d0e45b3bbc87e7c1d458a/src/main/service/video.js) · [f2f.js](https://github.com/duixcom/Duix-Avatar/blob/1328feb5871448c8fa3d0e45b3bbc87e7c1d458a/src/main/api/f2f.js) · [config.js](https://github.com/duixcom/Duix-Avatar/blob/1328feb5871448c8fa3d0e45b3bbc87e7c1d458a/src/main/config/config.js) · [dev-app-update.yml](https://github.com/duixcom/Duix-Avatar/blob/1328feb5871448c8fa3d0e45b3bbc87e7c1d458a/dev-app-update.yml) |

<a id="n2-gpac"></a>

### GPAC (MP4Box, packager DASH/HLS/CMAF)

| Thuộc tính | Giá trị |
|---|---|
| Repo | https://github.com/gpac/gpac |
| License | LGPL-2.1-or-later; phần lớn mã có thêm bản thương mại riêng |
| Phiên bản đã đọc | `ca91126ce7766871bec9a053f5245f720b7236eb` (commit 2026-11-23) |
| Kiểm chứng | 2026-11-24; code-read; đã đọc LICENSE (COPYING), README, AGENTS.md, THREAT_MODEL, SECURITY, `dasher.c` (phần enum và đuôi tệp), unittests/README, hai workflow; chưa chạy upstream |
| Khoảng trống lấp | Đóng gói và phát trực tuyến (HLS/DASH/CMAF, packager) |
| Cơ chế đáng học | - `src/filters/dasher.c` là bộ lọc phân đoạn: một pipeline sinh cả `mpd` và `m3u8` (nhánh `force_ext`, `segext`), enum `DasherCMAFMode` (`cmfc`, `cmf2`) và hỗ trợ khóa mặc định CENC (`DasherDefaultKIDInjection`).<br>- Kiến trúc bộ lọc: PID/gói tin nối các filter trong `src/filter_core/`; `src/media_tools/` giữ nhập, MPD (`mpd.c`, `m3u8.c`) và `dash_segmenter.c`; `applications/mp4box/` là CLI kiểm/đóng gói ISOBMFF.<br>- `THREAT_MODEL.md` và `SECURITY.md` mô tả bề mặt tấn công (tệp, manifest từ xa, SVG có script) và khuyên chạy xử lý media không tin cậy trong sandbox riêng. |
| Tiêu chí và cách kiểm | Test: `unittests/` (bật bằng `configure --unittests`, chạy trong `make`) bổ sung cho `testsuite/` là submodule riêng; thư mục đó rỗng trong bản clone nên không đọc được kịch bản và ngưỡng. Workflow `master.yml` dựng image Docker và đẩy lên Docker Hub; `testbuilds.yml` dựng FreeBSD rồi chạy `gpac -h`. Badge README trỏ buildbot/tests.gpac.io (chưa xác minh, không mở). Không thấy cổng kiểm tuân thủ DASH/HLS trong CI GitHub. |
| Giới hạn và rủi ro | License: LGPL-2.1 hoặc mới hơn, nên nhúng tĩnh vào sản phẩm đóng cần cân nhắc; README nói phần lớn mã có bản thương mại (Motion Spell). SECURITY.md yêu cầu báo lỗi công khai qua issue và chỉ coi là lỗ hổng khi có tác động an ninh rõ, không dùng GitHub Security Advisories; dự án tự nhận không phải sandbox, và là parser C xử lý định dạng phức tạp nên cần cô lập khi nhận tệp từ ngoài. Có thể gọi mạng khi nhận URL/manifest. Mô tả của trinh sát (LGPL-2.1, MP4Box/DASH/HLS/CMAF) khớp với repo; "bộ kiểm cấu trúc ISOBMFF" chỉ chứng minh qua việc có công cụ kiểm của MP4Box, chưa đọc ngưỡng cụ thể (chưa xác minh). |
| So với | FFmpeg (muxer/segmenter HLS, DASH ít tuân thủ chuẩn hơn theo tuyên bố chung, chưa đối chiếu ở đây), MediaMTX (server phát luồng, không đóng gói file), Mediabunny (đóng gói trong trình duyệt). |
| Nguồn | [COPYING](https://github.com/gpac/gpac/blob/ca91126ce7766871bec9a053f5245f720b7236eb/COPYING) · [README.md](https://github.com/gpac/gpac/blob/ca91126ce7766871bec9a053f5245f720b7236eb/README.md) · [AGENTS.md](https://github.com/gpac/gpac/blob/ca91126ce7766871bec9a053f5245f720b7236eb/AGENTS.md) · [THREAT_MODEL.md](https://github.com/gpac/gpac/blob/ca91126ce7766871bec9a053f5245f720b7236eb/THREAT_MODEL.md) · [SECURITY.md](https://github.com/gpac/gpac/blob/ca91126ce7766871bec9a053f5245f720b7236eb/SECURITY.md) · [dasher.c](https://github.com/gpac/gpac/blob/ca91126ce7766871bec9a053f5245f720b7236eb/src/filters/dasher.c) · [README.md](https://github.com/gpac/gpac/blob/ca91126ce7766871bec9a053f5245f720b7236eb/unittests/README.md) · [master.yml](https://github.com/gpac/gpac/blob/ca91126ce7766871bec9a053f5245f720b7236eb/.github/workflows/master.yml) · [testbuilds.yml](https://github.com/gpac/gpac/blob/ca91126ce7766871bec9a053f5245f720b7236eb/.github/workflows/testbuilds.yml) · [.gitmodules](https://github.com/gpac/gpac/blob/ca91126ce7766871bec9a053f5245f720b7236eb/.gitmodules) |

<a id="n2-mediaconch"></a>

### MediaConch (hồ sơ thiết kế và chính sách)

| Thuộc tính | Giá trị |
|---|---|
| Repo | https://github.com/MediaArea/MediaConch |
| License | GPL-3.0-or-later hoặc MPL-2.0-or-later (mã trong `SourceCode/`); CC BY-SA 4.0 (tài sản theo README); không có LICENSE ở gốc repo |
| Phiên bản đã đọc | `d2a4b62ffbaf5475c5c3e82b3e6fc9883a6be592` (commit 2021-09-29) |
| Kiểm chứng | 2026-11-24; docs-read; đã đọc README, License.html, readme và registry của ImplementationChecks, XSL kiểm EBML (đầu và các nhánh ICID), mẫu PolicyChecks, Demo/README; chưa chạy upstream |
| Khoảng trống lấp | Kiểm định file media (container/codec conformance, MediaInfo/MediaConch) |
| Cơ chế đáng học | - Sổ đăng ký check (`ImplementationCheckRegistry.md`): mỗi kiểm tra có CCID duy nhất, phiên bản, authority, định dạng đích và quan hệ phân cấp; ICID ví dụ `EBML-VER-COH`, `EBML-ELEMENT-VALID-PARENT`.<br>- `MetadataDevelopment/ImplementationChecks/implementationCheckEBML.xsl` (và Matroska/WebM) hiện thực từng ICID bằng XSLT trên đầu ra trace của MediaInfo; `PolicyCheckSampleOutput.xml` cho thấy một policy gồm các `check` có `expected`, `value` và `outcome` là pass hoặc fail kèm `reason`.<br>- Demo (`Demo/README.md`) cho ví dụ chính sách: định dạng Matroska, video FFV1, tỉ lệ khung hình 4:3, tốc độ 25 fps, chạy trên tệp mẫu `.mkv`. |
| Tiêu chí và cách kiểm | Kết quả mỗi check là pass/fail có lý do trong XML; policy là biểu thức XPath/so sánh trên trường MediaInfo. Kiểm bằng máy khi chạy MediaConch, nhưng repo này không có CI hay test tự động và chưa chạy upstream; registry còn nhiều mục TODO (hợp nhất ICID, bỏ csv, FFV1 chưa chuẩn hóa ICID). |
| Giới hạn và rủi ro | Repo ở trạng thái lưu trữ về mặt thực tế (commit cuối 2021-09-29, không có `.github`), không thay cho bản phát hành MediaConch mới; dùng cho thiết kế, không để dựng cổng CI. Mô tả trinh sát về chức năng đúng nhưng sao, license, ngày chưa xác minh được điền: license thật theo `SourceCode/License.html` là GPL-3.0+/MPL-2.0+, README ghi tài sản mở là CC BY-SA 4.0 và thư viện bên thứ ba có license riêng; ở thư mục gốc không có LICENSE. Tương thích copyleft khi nhúng cần đọc từng thư mục. Phải lấy mã hiện hành ở repo khác, chưa đọc ở đây. |
| So với | VMAF (đo chất lượng cảm nhận, không đo tuân thủ cấu trúc), FFMetrics (giao diện đo bằng FFmpeg), Pa11y (kiểm theo chính sách nhưng cho web, cùng ý tưởng cổng bằng quy tắc). |
| Nguồn | [README.md](https://github.com/MediaArea/MediaConch/blob/d2a4b62ffbaf5475c5c3e82b3e6fc9883a6be592/README.md) · [License.html](https://github.com/MediaArea/MediaConch/blob/d2a4b62ffbaf5475c5c3e82b3e6fc9883a6be592/SourceCode/License.html) · [readme.md](https://github.com/MediaArea/MediaConch/blob/d2a4b62ffbaf5475c5c3e82b3e6fc9883a6be592/MetadataDevelopment/ImplementationChecks/readme.md) · [ImplementationCheckRegistry.md](https://github.com/MediaArea/MediaConch/blob/d2a4b62ffbaf5475c5c3e82b3e6fc9883a6be592/MetadataDevelopment/ImplementationChecks/ImplementationCheckRegistry.md) · [implementationCheckEBML.xsl](https://github.com/MediaArea/MediaConch/blob/d2a4b62ffbaf5475c5c3e82b3e6fc9883a6be592/MetadataDevelopment/ImplementationChecks/implementationCheckEBML.xsl) · [PolicyCheckSampleOutput.xml](https://github.com/MediaArea/MediaConch/blob/d2a4b62ffbaf5475c5c3e82b3e6fc9883a6be592/MetadataDevelopment/PolicyChecks/PolicyCheckSampleOutput.xml) · [README.md](https://github.com/MediaArea/MediaConch/blob/d2a4b62ffbaf5475c5c3e82b3e6fc9883a6be592/Demo/README.md) |

<a id="n2-remove-ai-watermarks"></a>

### remove-ai-watermarks

| Thuộc tính | Giá trị |
|---|---|
| Repo | https://github.com/wiltodelta/remove-ai-watermarks |
| License | Apache-2.0 |
| Phiên bản đã đọc | `442187775afb7721b0e3cdc04be998d06d4849e1` (commit 2026-11-23) |
| Kiểm chứng | 2026-11-24; code-read; đã đọc LICENSE, README, `legal-and-safety.md`, `known-limitations.md`, `external-benchmark-licensing.md`, `gemini_engine.py` (đầu tệp, bản đồ alpha), `pyproject.toml` (phiên bản/license), workflow test; chưa chạy upstream |
| Khoảng trống lấp | Nhãn AI và minh bạch nội dung sinh ra (EU AI Act, watermark, tấn công gỡ nhãn) |
| Cơ chế đáng học | - `src/remove_ai_watermarks/gemini_engine.py`: gỡ sparkle Gemini bằng bản đồ alpha tính từ ảnh nền chụp mẫu 48 và 96 px (`gemini_bg_48.png`, `gemini_bg_96.png`), phát hiện theo nhiều tỉ lệ rồi tái dựng (`reverse=True`) và inpaint chung; lệnh `identify` chỉ đọc tín hiệu.<br>- `docs/known-limitations.md`: bảng từng đường xử lý (`metadata`, `visible`, `invisible`, `all`, `text`) ghi rõ phần bị gỡ, phần còn lại và cách kiểm phần còn lại; không lệnh nào cho kết luận "sạch".<br>- `docs/legal-and-safety.md`: ranh giới phạm vi (không nhắm xem trước ảnh stock, Nightshade/Glaze), bảng điều khoản pháp lý theo quốc gia kiểm 2026-09-23; `external-benchmark-licensing.md` ghi bộ ETI không có license nên không dùng được. |
| Tiêu chí và cách kiểm | CI `test.yml` chạy ruff, quét lockfile (`uv-secure`), kiểm snapshot đăng ký C2PA soft-binding và pytest ma trận Python 3.11 trên ba hệ điều hành; thư mục `tests/` có hàng trăm tệp (257 mục, chưa đọc từng test). Hiệu quả gỡ watermark ẩn (SynthID, VideoSeal) là tuyên bố của tác giả (chưa xác minh); tài liệu giới hạn nói không có bộ giải mã cục bộ xác nhận SynthID đã mất. |
| Giới hạn và rủi ro | Dùng sai mục đích có thể vi phạm quy định gỡ nhãn AI (tài liệu nêu Trung Quốc cấm cả cung cấp công cụ); không dùng để gỡ nhãn của nội dung không phải của mình. Tính năng tái sinh cần GPU CUDA/MPS và tải mô hình từ Hugging Face khi chạy lần đầu (`huggingface_hub`), nên có dữ liệu mạng ra vào ở bước tải. README quảng bá dịch vụ lưu trữ trả phí raiw.cc của tác giả. Một người duy trì, phát hành rất nhanh (0.74.0), phụ thuộc rất nhiều extras. Mô tả trinh sát (Apache-2.0, 6.490 sao) khớp ở license; số sao không kiểm lại. Khi mang cơ chế vào dự án khác: chỉ dùng phần `identify` và `known-limitations` để lập bộ test độ bền, chạy trong sandbox, không phát hành bản gỡ nhãn. |
| So với | c2patool và c2pa-rs (ký/đọc C2PA, phía bảo vệ chứ không tấn công), HyperFrames (không liên quan watermark, cùng nhóm media). |
| Nguồn | [LICENSE](https://github.com/wiltodelta/remove-ai-watermarks/blob/442187775afb7721b0e3cdc04be998d06d4849e1/LICENSE) · [README.md](https://github.com/wiltodelta/remove-ai-watermarks/blob/442187775afb7721b0e3cdc04be998d06d4849e1/README.md) · [legal-and-safety.md](https://github.com/wiltodelta/remove-ai-watermarks/blob/442187775afb7721b0e3cdc04be998d06d4849e1/docs/legal-and-safety.md) · [known-limitations.md](https://github.com/wiltodelta/remove-ai-watermarks/blob/442187775afb7721b0e3cdc04be998d06d4849e1/docs/known-limitations.md) · [external-benchmark-licensing.md](https://github.com/wiltodelta/remove-ai-watermarks/blob/442187775afb7721b0e3cdc04be998d06d4849e1/docs/external-benchmark-licensing.md) · [gemini_engine.py](https://github.com/wiltodelta/remove-ai-watermarks/blob/442187775afb7721b0e3cdc04be998d06d4849e1/src/remove_ai_watermarks/gemini_engine.py) · [pyproject.toml](https://github.com/wiltodelta/remove-ai-watermarks/blob/442187775afb7721b0e3cdc04be998d06d4849e1/pyproject.toml) · [test.yml](https://github.com/wiltodelta/remove-ai-watermarks/blob/442187775afb7721b0e3cdc04be998d06d4849e1/.github/workflows/test.yml) |
