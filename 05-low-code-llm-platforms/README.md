# 05 · Low-code / Visual LLM & Automation Platforms

| Dự án | Repo | License | ★ (10/2026) | Định vị | Ghi chú |
|---|---|---|---|---|---|
| **n8n** | n8n-io/n8n | Sustainable Use (fair-code, không OSI) | ~207k | Automation-first, có AI node/agent | Tăng từ 50k lên 200k+ trong ~2 năm |
| **Dify** | langgenius/dify | Apache-2.0 (kèm điều khoản) | ~158k | Nền tảng app LLM production: RAG, agent, workflow, prompt IDE | |
| **Langflow** | langflow-ai/langflow | MIT | ~140–154k | Visual builder trên LangChain/LangGraph, custom Python node | Vượt 100k★ 5/2026 |
| **Flowise** | FlowiseAI/Flowise | Apache-2.0 trừ phần enterprise | ~55k | Drag-drop LangChain | **Đã archive**, hết vòng đời 31/8/2026; xem hồ sơ xác minh 31/10 bên dưới |
| **Activepieces** | activepieces/activepieces | MIT (core) | – | Alternative n8n, MCP-first | |
| **Open WebUI** | open-webui/open-webui | Open WebUI License (BSD-3 + điều khoản giữ thương hiệu, không OSI) | ~154k (12/10/2026) | Giao diện chat tự host cho LLM local; RBAC, RAG, tool MCP/OpenAPI | v0.12.0 (10/10/2026); không được gỡ thương hiệu "Open WebUI" khi quá 50 người dùng/30 ngày |

**Chọn thế nào:** tự động hóa quy trình nhiều SaaS → n8n; app chat/RAG cho doanh nghiệp → Dify; dev Python cần tùy biến → Langflow.

## Bổ sung: chat UI tự host & agent builder (đã xác minh 2026-10-12)

| Repo | ★ (12/10) | License | Hoạt động gần nhất | Vì sao chất lượng | Lưu ý |
|---|---|---|---|---|---|
| **danny-avila/LibreChat** | 45,6k | MIT | v0.8.8 pre-release (1/10/2026) | Chat đa nhà cung cấp tự host: agent, MCP, artifacts, code interpreter sandbox; đa người dùng OAuth2/LDAP | Các bản gần đây đều gắn nhãn pre-release; stack nặng hơn (MongoDB, Meilisearch) **(chưa xác minh)** |
| **lobehub/lobehub** (trước là lobe-chat) | 83,2k | LobeHub Community License (Apache-2.0 + điều kiện, không OSI) | 12/10/2026 | Workspace agent + chat web/desktop; 14,6k commit, phát hành gần như hằng ngày | Phân phối bản phái sinh cần license thương mại; repo đã đổi tên |
| **Mintplex-Labs/anything-llm** | 67,0k | MIT | v1.17.0 (1/10/2026) | App RAG + agent local-first (desktop/Docker), LanceDB tích hợp, 38 nhà cung cấp LLM, agent builder không code, MCP | Telemetry bật mặc định (tắt bằng `DISABLE_TELEMETRY`); đa người dùng chỉ có ở bản Docker |
| **CherryHQ/cherry-studio** | 52,6k | AGPL-3.0 (có license thương mại) | v2.1.6 (11/10/2026) | Client desktop đa LLM, agent, hơn 300 trợ lý dựng sẵn; khoảng 9,5k commit | AGPL; bản Enterprise đóng, trả phí |
| **simstudioai/sim** | 29,8k | Apache-2.0 | v0.9.18 (11/10/2026) | Canvas dựng, triển khai và giám sát workflow agent; hơn 1.000 tích hợp; model local qua Ollama/vLLM | Chat tự host cần API key do Sim cấp; cần từ 12 GB RAM |
| **labring/FastGPT** | 29,8k | FastGPT Open Source License (riêng, không OSI) | v4.17.2 (9/10/2026) | RAG knowledge base + workflow trực quan, khâu xử lý dữ liệu trưởng thành | Không được làm SaaS khi chưa có license thương mại; phải giữ thông báo bản quyền |
| **coze-dev/coze-studio** | 21,7k | Apache-2.0 | commit cuối 29/7/2026 | Bản mở của nền tảng agent/workflow Coze (ByteDance), Go + React, runtime Eino, canvas FlowGram | Hoạt động chậm lại (392 commit); một số tính năng chỉ có ở bản thương mại |

**Nhận xét:** trong nhóm chat UI, chỉ **LibreChat** và **AnythingLLM** dùng MIT thuần; Open WebUI, LobeHub, FastGPT dùng license riêng không OSI, Cherry Studio là AGPL — đọc LICENSE trước khi dựng dịch vụ cho người khác. Chọn nhanh: chat nội bộ nhiều model + đăng nhập doanh nghiệp → LibreChat; RAG tài liệu trên máy cá nhân → AnythingLLM; workflow agent trực quan, license thoáng → Sim. Đã cân nhắc nhưng không thêm: node-red (23,7k★, Apache-2.0, không chuyên LLM), jan (44,9k★, Apache-2.0, thiên về chạy model local — gần mục 10).

## Bổ sung: kiểm ảnh "54 trang làm web, thiết kế, app miễn phí" (AIHubSeek, ảnh người dùng gửi, 2026-10-13)

Ảnh liệt kê 3 cột × 18 công cụ (Build Websites, Generate Designs, Create Apps), tiêu đề "for Free". Tôi kiểm gói miễn phí từng ô ngày 13/10/2026 qua trang giá và bài review; những ô chưa tìm được nguồn chính thức ghi "(chưa xác minh)". Ở đây "miễn phí" nghĩa là có gói dùng mãi không trả tiền, không tính bản dùng thử.

**Các ô đúng (gói free thật, kèm giới hạn thường gặp):**

- **Web:** Wix, WordPress.com, Carrd, Strikingly, Webflow, Jimdo, SITE123, Tilda, Google Sites, Mobirise (app offline miễn phí), Brizy (plugin WordPress free), Dorik (theo trang hãng). Giới hạn chung: tên miền phụ của hãng, có quảng cáo hoặc huy hiệu, ít trang.
- **Thiết kế:** Canva, Adobe Express, Figma (gói Starter), Leonardo.Ai (token hằng ngày), Pixlr, Photopea (có quảng cáo), BeFunky, Visme, Piktochart, Fotor, Vecteezy, Pixabay (ảnh miễn phí theo giấy phép Pixabay).
- **App:** Glide, Adalo, Bubble, Kodular, MIT App Inventor, FlutterFlow, Firebase (gói Spark), Backendless, Softr, Retool, WeWeb, Appsmith (mã nguồn mở Apache-2.0), Draftbit (theo FAQ hãng: 5.000 credit một lần, không nạp lại).

**Các ô sai hoặc cần lưu ý:**

| Cột | Ô | Mức | Thực tế |
|---|---|---|---|
| Web | Squarespace | ❌ | Không có gói free, chỉ dùng thử 14 ngày; muốn xuất bản phải trả tiền |
| Web | Zyro | ❌ | Hostinger đã gộp Zyro vào Hostinger Website Builder (đổi tên 2022, gộp hẳn 12/2023); không có gói free |
| Web | Weebly | ⚠️ | Gói free vẫn còn ở Mỹ, nhưng Square đang dừng Weebly ở 67 quốc gia khác và khuyên người mới dùng Square Online. Ở Việt Nam có còn đăng ký được không: (chưa xác minh) |
| Web | GoDaddy | ⚠️ | Builder nay là Airo; các bài review nói gói free có 50 credit AI/tháng, nhưng mâu thuẫn ở chỗ có được xuất bản hay không (chưa xác minh) |
| Web | Ucraft, Pagecloud, Zyro-cũ | ⚠️ | Không tìm thấy trang giá chính thức hay tin đóng cửa; gói free của Ucraft được mô tả là "rất hạn chế" (chưa xác minh) |
| Thiết kế | Midjourney | ❌ | Không có gói free; gói thấp nhất 10 USD/tháng. Các nguồn mâu thuẫn về lượt dùng thử ~25 ảnh cho tài khoản mới |
| Thiết kế | DALL·E | ❌ | Đã ngừng: OpenAI gỡ dall-e-2/3 khỏi API ngày 12/5/2026 và gỡ DALL·E GPT khỏi ChatGPT ngày 30/8/2026. Thay bằng tạo ảnh trong ChatGPT (bản free có giới hạn lượt) |
| Thiết kế | Crello | ⚠️ | Đổi tên thành VistaCreate từ 10/2021 sau khi Vistaprint mua lại; tên trong ảnh đã cũ 5 năm |
| Thiết kế | Remove.bg | ⚠️ | Bản free chỉ cho tải ảnh xem trước khoảng 0,25 MP và chỉ dùng phi thương mại; ảnh đủ độ phân giải tốn credit |
| Thiết kế | DesignCap, Snappa | ⚠️ | Có gói free nhưng giới hạn lượt tải hoặc gắn watermark (chưa xác minh chi tiết) |
| App | Appy Pie | ❌ | Chỉ thấy dùng thử 7 ngày; người dùng phản ánh gần như không xuất bản được nếu không trả tiền |
| App | Thunkable | ⚠️ | Gói free tối đa 3 project công khai, **không xuất bản lên store**; xuất bản từ gói Builder ~59 USD/tháng |
| App | Zoho Creator | ⚠️ | Các nguồn mâu thuẫn: có trang ghi gói free 1 app, có trang ghi chỉ có dùng thử (chưa xác minh) |
| App | The Things Stack | ⚠️ | Đây là LoRaWAN network server cho thiết bị IoT, không phải công cụ dựng app; xếp sai cột |
| App | Pinecone | ⚠️ | Đây là vector database (có gói Starter free), không phải công cụ dựng app; xếp sai cột |
| App | Firebase, Backendless | ⚠️ | Có free tier thật, nhưng là backend; vẫn phải tự viết app hoặc ghép với một builder khác |

**Tổng:** khoảng 37/54 ô đúng như tiêu đề; 5 ô sai rõ (Squarespace, Zyro, Midjourney, DALL·E, Appy Pie); số còn lại có giới hạn quan trọng, tên đã cũ, hoặc xếp sai cột.

**Dùng ảnh thế nào:** coi là danh sách gợi ý để tự kiểm, không phải bảng "miễn phí". Ba điều cần kiểm trước khi chọn: (1) gói free có cho **xuất bản** không (Thunkable, Adalo, Bubble đều giới hạn ở bước này); (2) có cho **dùng thương mại** không (remove.bg, nhiều kho ảnh); (3) dữ liệu có **xuất ra được** không khi muốn rời nền tảng (FlutterFlow chỉ cho xuất mã ở gói trả phí). Nếu cần tự chủ hoàn toàn: Appsmith (mục này), WordPress tự host, hoặc các nền tảng ở bảng trên.

## Bổ sung: kiểm ảnh "AI Agents A-Z" (`gyoridavid/ai_agents_az`), kho template n8n của một kênh YouTube (ảnh người dùng gửi, 2026-10-25)

> Ảnh là README trên điện thoại, liệt kê "Season 1" từ Episode 1 (prescription agent) đến Episode 10 (n8n best practices). Đã clone đủ lịch sử (110 commit, HEAD `764fac2`), đọc README từng tập và quét **toàn bộ 55 file JSON** (1.551 node) bằng script: loại node, loại credential, host được gọi, chuỗi giống API key. Không import workflow nào vào n8n.

### Hồ sơ nhanh

| Mục | Thông tin (đọc 25/10/2026) |
|---|---|
| Repo | https://github.com/gyoridavid/ai_agents_az · **~3,9k★**, 946 fork (shields) |
| Tác giả | David Gyori: 109/110 commit, 1 commit của người khác. Kênh YouTube "AI Agents A-Z" và cộng đồng trả phí trên Skool |
| License | **Không có file LICENSE** (shields: "not specified"). Về pháp lý mọi quyền thuộc tác giả: import để dùng thì được ngầm hiểu là cho phép, nhưng đóng gói lại hay bán lại thì không có giấy phép |
| Hoạt động | 30/3/2025 → **19/12/2025** (Episode 42). **Đã hơn 10 tháng không commit** |
| Nội dung thật | 33 thư mục tập (1–25, 31, 35, 36, 38–42; thiếu 26–30, 32–34, 37), mỗi tập có README + JSON workflow; thêm 10 file Python (app Modal chạy FLUX/Qwen), 5 mp4 và 5 mp3 mẫu. Repo nặng 112 MB, riêng `episode_9/example_bgvideo.mp4` là 49 MB |

### Kiểm ảnh

- **10 tập trong ảnh đều có thật** và đúng tên. Ảnh chỉ chụp Season 1; README thật kéo tới Episode 42.
- **Phần lớn kho là làm video "faceless" hàng loạt**, không phải "AI agent" theo nghĩa chung. Từ Episode 7 trở đi chủ yếu là YouTube Shorts, truyện kinh dị/trả thù, video ngủ, UGC, influencer ảo trên Instagram, cùng các bài so model sinh ảnh/video (Seedance, Hailuo, Wan 2.2, Veo 3.1, Sora 2, FLUX, Qwen Image, Z-Image).
- Năm tập đầu (đơn thuốc, digest, LinkedIn có duyệt HITL, deep research, viết blog) mới là "agent" đúng nghĩa và là phần đáng học nhất cho mục 03/21.
- **Tên tập không khớp:** README gốc ghi Episode 38 là "Create AI reaction videos with Veo 3.1", nhưng README trong thư mục là "Gemini 3 recreates YouTube shorts", tức là dựng lại video người khác.

### Điều ảnh không nói (quét JSON)

- **Không lộ secret:** không chuỗi nào giống API key (OpenAI, Google, Replicate, Slack, fal) trong file hiện tại, kể cả commit "Remove pinned data".
- **Node:** 1.225 node `n8n-nodes-base` + 282 node `@n8n/n8n-nodes-langchain`; không có community node (các node lạ là workflow ComfyUI đi kèm).
- **Credential cần chuẩn bị:** HTTP header/bearer (111 chỗ, gọi API trả phí trực tiếp), OpenAI (32), Supabase (23), Ollama (16), Gmail (11), YouTube (10), OpenRouter (9), Facebook Graph (8)…
- **Dịch vụ ngoài:** fal.ai (24 lần gọi `queue.fal.run`), Modal, Together, MiniMax, ElevenLabs, Cloudflare Workers AI. Sora 2/Veo đi qua **kie.ai**, một bên bán lại API không chính thức.
- **"Free" trong tên tập thường là:** dùng tín dụng dùng thử, chạy GPU của mình (ComfyUI, Colab), hoặc gói free có giới hạn.

**Phụ thuộc vào máy chủ của tác giả:**

- Nhiều tập cần container `gyoridavid/ai-agents-no-code-tools` (6,4k lượt pull) và `gyoridavid/narrated-story-creator` (5,7k lượt pull) trên Docker Hub. **Hai image này không có repo mã nguồn công khai** (GitHub trả "repo not found"), nên khó kiểm bên trong làm gì. Image cập nhật lần cuối 9/2025 và 5/2025.
- Chỉ `gyoridavid/short-video-maker` (~1,4k★, MIT) là có mã: Kokoro TTS (chỉ tiếng Anh) + whisper.cpp + video nền từ Pexels + **Remotion**. Công ty trên 3 người phải mua license Remotion (mục 22 §2.2). Repo này dừng từ 6/2025.
- Hai workflow còn hard-code IP mạng LAN của tác giả (`192.168.68.60:8000`); Episode 19 trỏ thẳng tới endpoint Modal riêng của tác giả. Import xong phải đổi các địa chỉ này.

**License model:** các tập FLUX.1 Kontext [dev] và FLUX.1 [dev] dùng trọng số theo **FLUX Non-Commercial License**, không dùng cho kênh kiếm tiền được; muốn dùng thương mại thì chọn FLUX.1 Schnell, tương tự cảnh báo FLUX.2 ở mục 19 §1e. File Modal ghim commit diffusers và revision model, là điểm tốt.

**Phễu thương mại:** README mỗi tập dẫn tới Skool trả phí ("premium versions of the workflows… with the hosted GPU media server"; 77 link) và có link affiliate n8n (24 tập). Bản trong repo là bản miễn phí; bản "premium" nằm sau cộng đồng trả phí.

**Rủi ro nội dung:**

- Episode 36 tạo "bodycam footage" giả bằng Sora 2; Episode 38 dựng lại Shorts của người khác; Episode 21 là "10 niche faceless kiếm tiền trong một tháng".
- Không workflow nào gắn nhãn nội dung AI. YouTube và TikTok đều yêu cầu khai báo nội dung tổng hợp trông như thật.
- Kiểu nội dung sản xuất hàng loạt dễ bị coi là "inauthentic/repetitious content" khi xét kiếm tiền **(chi tiết chính sách chưa xác minh trong đợt này)**.

### So sánh & dùng thế nào

| | ai_agents_az | `enescingoz/awesome-n8n-templates` | Thư viện chính thức n8n.io/workflows | OpenMontage / skill video (mục 19, 22) |
|---|---|---|---|---|
| Bản chất | ~55 workflow của một kênh, kèm video hướng dẫn | Danh sách workflow cộng đồng gom từ nhiều nguồn **(chưa clone)** | Template do n8n và cộng đồng đăng, có trang mô tả | Agent viết code dựng video |
| License | Không có | Xem từng mục | Theo điều khoản n8n | Tùy repo |
| Cập nhật | Dừng 12/2025 | **(chưa kiểm)** | Liên tục | Liên tục |

- **Đáng lấy:** Episode 3 (đăng LinkedIn có bước duyệt người, HITL qua Gmail) và Episode 4–5 (deep research → viết blog) là mẫu tốt để học cấu trúc agent trong n8n. Episode 10 (best practices) chỉ là video, thư mục không có workflow.
- **Trước khi import:**
  - Xem từng node HTTP: gửi gì, tới đâu, dùng credential nào.
  - Thay IP LAN và endpoint Modal của tác giả.
  - Đặt hạn mức chi tiêu trên fal/kie/OpenAI, vì vòng lặp tạo video gọi API trả phí nhiều lần.
- **Không nên:** chạy image Docker không có mã nguồn trên máy có dữ liệu thật (nếu cần thì chạy trong VM riêng); đóng gói lại workflow để bán, vì repo không có license; dùng FLUX [dev] cho kênh thương mại.
- n8n tự nó là fair-code (Sustainable Use License): dùng nội bộ thì được, bán dịch vụ host n8n cho khách thì phải xem lại điều khoản (bảng đầu mục này).

**Nguồn:** clone đủ lịch sử github.com/gyoridavid/ai_agents_az 25/10/2026 (110 commit, HEAD 764fac2 19/12/2025; README.md, `episode_*/README.md`, quét 55 file JSON bằng script, `episode_19/flux_kontext_dev_modal.py`, `episode_16/guide-start-server.md`, commit "Remove pinned data from workflow") · github.com/gyoridavid/short-video-maker (clone nông; README, LICENSE MIT, package.json `@remotion/*` ^4.0.286) · hub.docker.com/v2/repositories/gyoridavid/{ai-agents-no-code-tools,narrated-story-creator,short-video-maker} (lượt pull, ngày cập nhật) · img.shields.io/github/{stars,forks,license,last-commit}/gyoridavid/… 25/10/2026 · bên thứ ba: osrepos.com/repo/gyoridavid-ai_agents_az · sourcepulse.org/projects/11055697 · growwstacks.com/blog/free-n8n-automation-templates-goldmine

## Nâng cấp 31/10/2026: rà repo lớn, Flowise đã archive

> Ba việc. (1) Đọc lại số sao, license, ngày push của mọi repo mục 05 trong catalog bằng GitHub search API (31/10/2026). (2) **Điều tra Flowise**: clone đủ lịch sử, đọc commit cuối, `SECURITY.md`, LICENSE, thông báo chính thức và tìm fork cộng đồng. (3) Tìm repo lớn còn thiếu bằng 9 truy vấn (topic `low-code`, `no-code`, `workflow-automation`; từ khoá "visual agent builder", "llm app builder", "agent builder" tạo sau 1/10/2025). Chọn **5 repo**, clone `--filter=blob:none`, đọc LICENSE, manifest, cấu trúc, CI, grep telemetry. **Không cài, không chạy script nào.**

### Flowise: vì sao archive và thay bằng gì

| Mục | Thông tin (đọc 31/10/2026) |
|---|---|
| Trạng thái | `FlowiseAI/Flowise` **archived**, 55,5k★, 25,1k fork; push cuối 13/8/2026. Dòng "Trạng thái chưa rõ" ở bảng đầu mục đã có câu trả lời |
| Mốc | **29/7/2026** đóng băng code, tag cuối `flowise@3.1.4` cùng ngày; **3/8** `SECURITY.md` đổi thành "PRODUCT SUNSET… no longer accepting new security vulnerability reports" (commit của nhân viên Workday); **13/8** commit cuối thêm "Flowise has been archived" vào README rồi archive; **31/8** hết vòng đời, nhóm lõi rời Discord/GitHub. Trang flowiseai.com/sunset ghi ngày archive là 10/8, lệch 3 ngày với GitHub |
| Lý do chính thức | Discussion #6727 và trang sunset: lập trình viên chuyển sang coding agent (Claude Code, OpenClaw) cho việc phức tạp; "The typical rigid workflow low code approach quickly hits the limit when it comes to complexity" |
| Ai quyết | Flowise thuộc Workday (mua khoảng 8/2025 theo tin báo chí, **chưa xác minh** từ thông cáo của Workday). Từ 11/2025 có 200 commit từ email `workday.com`, nhiều hơn email `flowiseai.com` (160) |
| Thay thế chính thức | **Không có.** Nhóm chỉ khuyên fork; code "Apache 2.0 licensed… is yours to keep building on". Không nêu ngày tắt Flowise Cloud hay cách xuất dữ liệu (một blog nói 30/11/2026, **chưa xác minh**) |
| License | `LICENSE.md` là Apache-2.0 **trừ** `packages/server/src/enterprise/` và các file ghi bản quyền riêng (FlowiseAI Commercial License), nên GitHub báo `NOASSERTION`. Fork phải bỏ hoặc thay phần enterprise |
| Fork cộng đồng | `Perruer/keelflow` (43★, tạo 24/9/2026, Apache-2.0 only, tự gọi là "security-maintained continuation"); `davobene/migrateflows` (4★, MIT) chuyển flow Flowise sang n8n. Chưa có fork nào đủ lớn |
| Rủi ro nếu còn chạy | Không còn nhận báo lỗi bảo mật. Đã có repo khai thác công khai cho **CVE-2026-58057** (RCE trên Windows qua MCP stdio, `CerberusMrXi/Flowise-CVE-2026-58057-exploit`, tạo 23/7/2026); chưa kiểm bản 3.1.4 đã vá hay chưa |

**Nên chuyển sang đâu:** canvas LangChain gần nhất là **Langflow** (MIT, 156,2k★); app LLM/RAG có giao diện quản trị → **Dify**; tự động hoá nhiều SaaS → **n8n** (fair-code); muốn để coding agent dựng workflow thay vì kéo thả → **n8n-mcp** (bảng dưới). Nếu buộc giữ Flowise: chạy sau VPN, không bật node MCP stdio, và tự theo dõi CVE.

### Repo cũ: điều đã đổi

| Repo | Thay đổi (12/10 → 31/10/2026) | Hệ quả |
|---|---|---|
| `FlowiseAI/Flowise` | **Archived 13/8/2026** | Xem trên; catalog ghi archived |
| `danny-avila/LibreChat` | **Đã chuyển sang `LibreChat-AI/LibreChat`**, 45,6k → 46,6k, push 31/10 | Link cũ còn chuyển hướng; catalog cần đổi trường `repo` |
| `coze-dev/coze-studio` | 21,7k → 21,8k; **push cuối vẫn 29/7/2026** | Hơn 3 tháng không commit trên nhánh chính; coi như tạm dừng. Canvas FlowGram của nó vẫn sống (bảng dưới) |
| `gyoridavid/ai_agents_az` | Vẫn dừng từ 19/12/2025 | Đúng như hồ sơ 25/10 |
| `activepieces/activepieces` | Bảng đầu ghi "–" → **25,3k**, push 31/10; GitHub báo `NOASSERTION` (MIT core + phần EE) | Bổ sung số |
| n8n · Dify · Langflow · Open WebUI | 207k → 209,2k · 158k → 160,1k · ~140–154k → 156,2k · 154k → 157,4k | Không đổi nhận định. n8n, Dify, Open WebUI, LobeHub, FastGPT đều hiện `NOASSERTION` vì license riêng (đúng như bảng đầu) |
| LobeHub, AnythingLLM, Cherry Studio, Sim, FastGPT | Tăng 0,5–1,5% | Không đổi |

### Bảng nhanh 5 repo mới

| Repo | Nhóm | ★ · license | Commit cuối | Một dòng | Cờ |
|---|---|---|---|---|---|
| `czlonkowski/n8n-mcp` | Coding agent → n8n | 23,2k · MIT | 27/10/2026 | MCP server cho agent tra node n8n, kiểm và sửa workflow | **Telemetry mặc định thu workflow để làm dataset ML** |
| `ToolJet/ToolJet` | Nền tảng internal tool + AI | 41,2k · AGPL-3.0 (EE riêng) | 30/10/2026 | Dựng admin/dashboard bằng prompt hoặc qua MCP | Quickstart dùng image **EE**; submodule EE riêng tư |
| `Budibase/budibase` | Nền tảng app + agent | 28,4k · GPL-3.0 / MPL-2.0 / BSL | 29/10/2026 | App nội bộ, automation, agent AI có phân quyền theo người dùng | 3 license trong một repo; analytics bật trong compose |
| `iflytek/astron-agent` | Nền tảng agentic workflow | 9,0k · Apache-2.0 | 28/10/2026 | Workflow agent + RPA + MCP của iFlytek, Java/Python/Go | Mật khẩu mặc định yếu; gắn hệ sinh thái iFlytek |
| `bytedance/flowgram.ai` | Framework canvas workflow | 8,5k · MIT | 22/10/2026 | Thư viện canvas, form node, biến, runtime để tự dựng "Dify của riêng mình" | Bản Desktop chưa ký số |

### Hồ sơ từng repo

- **n8n-mcp.** 1.336 commit từ 7/6/2025, 39 tác giả nhưng gần như một người (Romuald Członkowski, ~1.230 commit dưới hai tên); **60% commit có trailer Claude**. Bản v2.99.2 (27/10/2026), ghim `n8n-workflow` 2.44.2. Có 7 tool tra cứu (không cần n8n) và 21 tool quản lý (cần `N8N_API_URL`, `N8N_API_KEY`); README hướng dẫn `DISABLED_TOOLS=…` để tắt hẳn tool ghi/xoá và tool credential ✅. **Telemetry bật mặc định** gửi `https://telemetry.n8n-mcp.com`: ID cài đặt băm từ hostname/home dir, tên tool, **workflow đã làm sạch** (giữ node, kết nối, tham số không nhạy cảm) và **câu `intent` người dùng gõ**; `PRIVACY.md` v2 (28/9/2026) nói thẳng mục đích "build datasets and machine learning models". Làm sạch chạy trên máy (`workflow-sanitizer.ts`, `intent-sanitizer.ts`) ✅, nhưng **không đọc `DO_NOT_TRACK`**; tắt bằng `npx n8n-mcp telemetry disable` hoặc `N8N_MCP_TELEMETRY_DISABLED=true`. Đi kèm `czlonkowski/n8n-skills` (6,6k★, MIT). Cài: `npx n8n-mcp` (stdio) sau khi tắt telemetry.
- **ToolJet.** 19.373 commit từ 3/2021, 760 tác giả. LICENSE là **AGPL-3.0**, nhưng `frontend/ee` và `server/ee` là submodule trỏ tới `ToolJet/ee-frontend`, `ToolJet/ee-server` **không truy cập công khai được**; lệnh Docker trong README chạy `tooljet/try:ee-lts-latest`, tức bản EE chứ không phải bản CE ⚠️. MCP server và plugin cho Claude Code/Codex đang beta. `.env.example`: `CHECK_FOR_UPDATES=true` và telemetry gửi về "ToolJet hub" mỗi 24 giờ, **bật mặc định**, tắt bằng `DISABLE_TOOLJET_TELEMETRY=true`. CI dày (Cypress, CodeQL, grype, license-compliance). Có kênh LTS (`v3.20.252-lts`) tách khỏi kênh beta.
- **Budibase.** 61.333 commit từ 3/2019, 211 tác giả. `LICENSE` là hướng dẫn: server/builder/worker **GPL-3.0**, client/bbui/sdk/string-templates **MPL-2.0** (để app dựng ra không bị GPL), `packages/pro` **BSL** (đổi sang GPLv3 sau 4 năm) dù `package.json` ghi `UNLICENSED`; kèm `SQS_LICENSE` của bên thứ ba. Agent AI: `packages/server/src/ai/tools/authorization.ts` lọc kết quả tool theo quyền của **người đang dùng** ("Tool is not available in this security context") ✅ — mẫu tốt cho agent nội bộ. Analytics: `hosting/docker-compose.yaml` đặt `ENABLE_ANALYTICS: "true"`, image đơn có sẵn token PostHog mặc định trong `runner.sh`. Bản v3.50.0 (15/10/2026).
- **Astron Agent (iFlytek).** 3.264 commit từ 22/9/2025, 125 tác giả. Apache-2.0 + NOTICE; README nhấn "no commercial restrictions" ✅ (khác FastGPT, Dify). Gồm `core/` (agent, workflow, knowledge, memory, plugin, tenant), `console/`, Casdoor cho đăng nhập, tuỳ chọn RPA (`iflytek/astron-rpa`). `.env.example` có **mật khẩu mặc định yếu** (`spark123`, `root123`, Redis `123`, MinIO `minioadmin123`); endpoint bot mặc định trỏ Spark của iFlytek (`spark-api-open.xf-yun.com`). Có workflow `claim-issue-reward.yml` trả thưởng cho người đóng issue. Bản v1.1.2 (1/9/2026). Cài: `cd docker/astronAgent && cp .env.example .env` (đổi hết mật khẩu) rồi `docker compose -f docker-compose-with-auth.yaml up -d`.
- **FlowGram (ByteDance).** 779 commit từ 2/2025, 45 tác giả, MIT. Không phải sản phẩm mà là **bộ khung để tự dựng nền tảng workflow**: `canvas-engine`, `node-engine`, `variable-engine`, `runtime`, `materials` (node LLM, Condition, Code); là canvas của Coze Studio. Mới thêm FlowGram Desktop (10/2026) xuất workflow ra HTTP và MCP, README tự ghi "Preview installers are unsigned". Không thấy telemetry. Hợp khi muốn nhúng canvas vào sản phẩm riêng thay cho Flowise.

### Mẫu chung rút ra

1. **"Low-code bị coding agent nuốt" đã thành lý do đóng cửa chính thức** (Flowise). Hướng sống sót của nhóm này là mở MCP để agent dựng thay người kéo thả: n8n-mcp, ToolJet MCP, FlowGram Desktop xuất MCP.
2. **Sản phẩm bị mua lại có thể đóng nhanh:** từ đóng băng tới hết vòng đời chỉ 33 ngày, không có đường chuyển đổi dữ liệu. Khi chọn nền tảng, ưu tiên định dạng flow xuất được và license cho phép fork (Apache/MIT không kèm thư mục thương mại).
3. **Telemetry ngày càng thu nội dung, không chỉ số đếm:** n8n-mcp thu workflow và câu lệnh để huấn luyện mô hình; ToolJet, Budibase bật analytics mặc định ở bản tự host.
4. **"Open source" nhiều tầng:** ToolJet (AGPL + EE riêng tư), Budibase (GPL + MPL + BSL), Flowise (Apache + thư mục thương mại). Đọc LICENSE từng thư mục và kiểm image Docker mặc định là CE hay EE.

**Nguồn (31/10/2026):** GitHub search API (`repo:` cho repo cũ, 9 truy vấn; `flowise` tạo sau 1/7/2026; `keelflow`) · clone `--filter=blob:none` FlowiseAI/Flowise (README.md, SECURITY.md, LICENSE.md, `packages/server/src/enterprise/LICENSE.md`, `git log` email theo domain, commit ba4c6509 và 9291856d, tag `flowise@3.1.4`) · https://github.com/FlowiseAI/Flowise/discussions/6727 · https://flowiseai.com/sunset · bên thứ ba: https://landing.elest.io/flowise-alternatives · https://byteiota.com/flowise-shutdown-august-31-migrate-your-ai-pipelines-now/ · https://dev.to/nodles/best-flowise-alternatives-in-2026-after-the-workday-acquisition-4834 · https://github.com/Perruer/keelflow · clone repo mới: n8n-mcp (README.md, PRIVACY.md, LICENSE, package.json, `src/telemetry/{config-manager,ingest-client,telemetry-types}.ts`), ToolJet (LICENSE, README.md, .gitmodules, .env.example, workflows), Budibase (LICENSE, `packages/*/package.json`, `packages/pro/license.md`, `packages/server/src/ai/tools/authorization.ts`, `packages/backend-core/src/configs/configs.ts`, `hosting/docker-compose.yaml`, `hosting/single/runner.sh`), astron-agent (README.md, LICENSE, NOTICE, `docker/astronAgent/{.env.example,docker-compose.yaml}`, workflows), flowgram.ai (README.md, LICENSE, `packages/`, `apps/`)

## Nâng trần 2/11/2026: workflow thành tài liệu có chuẩn, lint và test được (yêu cầu người dùng)

> Cách làm: grep `data/projects.json` theo `repo` (Windmill, Kestra, Temporal, Activepieces, Conductor đã ở mục 21 nên không thêm); GitHub search API 2/11/2026; clone `--depth 1 --filter=blob:none`, đọc LICENSE, README, schema, bộ test conformance, file cấu hình mặc định. **Không cài, không chạy.**

**Trần hiện tại:**

- Mục chỉ so **nền tảng với nền tảng** (n8n, Dify, Langflow, FastGPT…); flow nằm trong định dạng riêng của từng sản phẩm. Vụ Flowise (§ Nâng cấp 31/10) cho thấy hệ quả: đóng cửa 33 ngày, không có đường chuyển dữ liệu.
- Mẫu chung 31/10 đã khuyên "ưu tiên định dạng flow xuất được" nhưng **chưa chỉ ra chuẩn nào** để xuất sang.
- Chưa có **cổng máy** cho flow: không lint, không test hồi quy, không kiểm khi agent (n8n-mcp) sửa flow.

| Repo | Lớp | ★ · license (2/11/2026) | Commit cuối | Vì sao nâng trần | Rủi ro |
|---|---|---|---|---|---|
| `open-workflow-specification/specification` (trước là `serverlessworkflow/specification`) | Chuẩn | 947 · Apache-2.0 | 2/11/2026 | DSL workflow trung lập nhà cung cấp của cộng đồng CNCF; YAML có schema (`schema/workflow.yaml`, ví dụ ghi `dsl: '1.0.4'`), gọi HTTP/gRPC/OpenAPI/AsyncAPI, sự kiện CloudEvents, timeout, xử lý lỗi, lịch CRON. Có **CTK** (`ctk/features/*.feature`, Gherkin) để kiểm runtime có đúng chuẩn | **Đã đổi tên** từ Serverless Workflow; tìm theo tên cũ trên GitHub search không ra. Runtime chủ yếu hệ Java (SonataFlow, Quarkus Flow, SDK Java) và vài dự án nhỏ; các nền tảng ở bảng đầu mục **không** xuất ra DSL này |
| `OAI/Arazzo-Specification` | Chuẩn | 487 · Apache-2.0 | 28/10/2026 | Chuẩn của OpenAPI Initiative mô tả **chuỗi gọi API** (bước, phụ thuộc, điều kiện thành công, output) dạng máy đọc; bản hiện hành **1.1.0** thêm nguồn AsyncAPI. Hợp làm "hợp đồng" cho flow tích hợp nhiều SaaS mà agent đọc và chạy được | Chỉ mô tả gọi API, không có node LLM hay human-in-the-loop; công cụ hỗ trợ 1.1.0 còn ít (README liệt kê vài parser/validator của bên thứ ba) |
| `cloudevents/spec` | Chuẩn | 5,9k · Apache-2.0 | 22/10/2026 | Định dạng sự kiện chung cho trigger/webhook, có binding HTTP, Kafka, MQTT…; Open Workflow dùng nó cho sự kiện | Nhánh chính đang là `1.0.3-wip`; chỉ chuẩn hoá phong bì, không chuẩn hoá nội dung |
| `stoplightio/spectral` | Cổng máy | 3,2k · Apache-2.0 | 30/10/2026 | Linter JSON/YAML theo ruleset; có sẵn `spectral:oas`, `spectral:asyncapi`, **`spectral:arazzo`** (Arazzo v1) và cho viết rule riêng. Dùng để chặn PR khi file flow/API sai schema hoặc phạm quy ước (CLI v6.17.0) | Ruleset Arazzo ghi "v1", hỗ trợ 1.1.0 **chưa xác minh**; không hiểu JSON riêng của n8n/Dify trừ khi tự viết rule |
| `node-red/node-red` | Đầu bảng | 23,8k · Apache-2.0 | 26/10/2026 | Công cụ low-code lâu đời còn sống (OpenJS Foundation, v5.0.9). Flow là **một file `flows.json`**, credential mã hoá riêng, có chế độ Projects quản flow bằng git; kèm `node-red/node-red-node-test-helper` (65★, Apache-2.0, commit 12/1/2026) để **unit test node/flow** | Không có lớp agent/RAG mạnh như Dify. `settings.js`: mặc định mã hoá credential bằng khoá tự sinh; đã đặt `credentialSecret` thì **không được đổi**, đổi là mất credential. Test helper nhịp chậm |

**Stack nâng trần** (lợi ích/công sức giảm dần):

1. **Flow là file trong git:** xuất workflow n8n/Dify/Langflow ra JSON/YAML, commit cùng code, bỏ dữ liệu ghim (n8n "pinned data", § kiểm ảnh AI Agents A-Z) và không để credential trong file; Node-RED thì bật Projects và đặt `credentialSecret` một lần, giữ trong kho secret.
2. **Hợp đồng API bằng Arazzo:** với flow chủ yếu gọi SaaS, viết mô tả Arazzo cạnh flow; chạy `spectral lint` (`extends: ["spectral:oas", "spectral:arazzo"]`) trong CI.
3. **Cổng khi agent sửa flow:** n8n-mcp (§ Nâng cấp 31/10) có tool kiểm workflow; đặt bước kiểm đó cùng Spectral làm required check trước khi deploy flow do agent sinh.
4. **Test hồi quy flow:** Node-RED dùng test helper; n8n/Dify gọi webhook/API của flow bằng Promptfoo (mục 07) với assertion tất định trên output.
5. **Đường thoát khỏi nền tảng:** flow quan trọng, chạy lâu thì mô tả lại bằng Open Workflow DSL hoặc chuyển sang engine durable ở mục 21 (Temporal, Kestra, Windmill). Phát sự kiện theo CloudEvents để đổi nền tảng không phải sửa nơi phát.

**Nguồn §Nâng trần 2/11/2026:** GitHub search API 2/11/2026 (`repo:` gộp; `open workflow specification in:name`) · `data/projects.json` (grep `repo`) · clone `--depth 1 --filter=blob:none`: serverlessworkflow/specification → open-workflow-specification/specification (HEAD 2108908, 2/11/2026; LICENSE, README.md, `schema/`, `ctk/README.md`, `ctk/features/`, `examples/`), OAI/Arazzo-Specification (HEAD e9ee1c4, 28/10/2026; README.md, `versions/1.1.0.md`), cloudevents/spec (HEAD 1025510, 22/10/2026; `cloudevents/spec.md`), stoplightio/spectral (HEAD 0b4889e, 30/10/2026; README.md, `docs/getting-started/{1-concepts,3-rulesets,6-arazzo}.md`, `packages/cli/package.json`), node-red/node-red (HEAD 22d019c, 26/10/2026; LICENSE, package.json, `packages/node_modules/node-red/settings.js`) · https://github.com/open-workflow-specification/specification · https://github.com/OAI/Arazzo-Specification · https://github.com/cloudevents/spec · https://github.com/stoplightio/spectral · https://github.com/node-red/node-red · https://github.com/node-red/node-red-node-test-helper

## Nâng trần 2/11/2026 (mở rộng): kiểm đường rời nền tảng bằng dữ liệu và kết quả chạy

<a id="platform-portability-2026-11-02"></a>

> Bổ sung chiều sâu trong cùng ngày với phần chuẩn/lint ở trên, không phải đợt phát hành mới. Đọc mã ba repo: Node-RED, FlowGram và Prompt flow; GitHub API cho metadata ngày 2/11/2026. Chỉ clone/read LICENSE, CI, schema và file chính; **không cài, không chạy flow hoặc trình chuyển đổi**.

### Trần hiện tại và ba hồ sơ đối chiếu

Phần chuẩn/lint đã có Open Workflow DSL, Arazzo và Spectral. Nhưng **xuất được JSON không chứng minh chạy tương đương trên runtime khác**: còn phiên bản node, credential, mã Python/JS tùy chỉnh, thứ tự sự kiện và side effect. Cần đánh giá đường rời nền tảng bằng một flow cụ thể cùng bộ dữ liệu và kết quả kỳ vọng.

| Repo · tổ chức | ★ · license (2/11/2026) | HEAD đọc · commit cuối | Cơ chế đọc được | Giới hạn khi chọn |
|---|---|---|---|---|
| **Node-RED** · OpenJS Foundation, dự án từ IBM | 23.805 · Apache-2.0 | `22d019c4eccac31d95f3b6167c7334de72ef02a6` · 26/10 | `settings.js` khai `flows.json`, còn Projects quản git; workflow CI gọi `npm run test`. Runtime và định dạng node có cùng hệ sinh thái nên hợp workflow thiết bị/tích hợp đã có node phù hợp | Projects **tắt mặc định**. Flow, gói node và credential không phải một file duy nhất; clone git thiếu secret không khôi phục được toàn dịch vụ |
| **FlowGram** · ByteDance, canvas của Coze Studio | 8.549 · MIT | `f644642123ba05e0207594c582d4f42337af2a1c` · 2/11 | `WorkflowSchema` có `nodes/edges/groups/globalVariable`; interface node LLM/code nằm riêng. CI build/lint/typecheck/test coverage và E2E Playwright | Đây là SDK để tự làm sản phẩm; type TypeScript của FlowGram **không phải** chuẩn trung lập Open Workflow. Mang canvas sang app khác vẫn cần cùng registry node/runtime hoặc adapter do mình viết |
| **Prompt flow** · Microsoft | 11.260 · MIT | `33a68c9d3cf349d7fdfad1f41969af27543c0406` · 19/10 | `flow.dag.yaml` tách graph khỏi Python/prompt; repo có hướng dẫn audit → rebuild → parity → vận hành khi chuyển sang Microsoft Agent Framework | README chính thức **không khuyến nghị phát triển mới**; Prompt flow trong Foundry/Azure ML nghỉ ngày **20/4/2027**, runtime image ngừng cập nhật kể cả bảo mật. Repo chưa archive không chứng minh dịch vụ còn được duy trì |

**Đọc sâu đường di chuyển.** Prompt flow là case study cho rủi ro vòng đời, không phải lựa chọn mặc định mới: `migration-guide/PromptFlow-to-MAF/workflow_loader.py` nạp module workflow Python bằng `exec_module`; nó không phải bộ chuyển đổi tự động an toàn cho graph bất kỳ. Phải giữ prompt, schema input/output, connection alias và bộ parity từ ứng dụng cũ. FlowGram có schema rõ để tự dựng adapter; Node-RED có runtime/node ổn định để xuất–nhập trong cùng nền tảng. **Chưa kiểm** chuyển đổi chéo ba hệ thống hoặc khả năng giữ nguyên side effect.

**Đã đổi từ hồ sơ trước:** bảng Flowise ở đầu mục từng ghi “trạng thái chưa rõ”; kết luận xác minh 31/10 bên dưới là **đã archive**, nay sửa hàng đầu cho nhất quán. Với FlowGram, HEAD 2/11 thêm hướng dẫn cài Desktop; điều đó không nâng JSON riêng thành chuẩn chung. Prompt flow được thêm vì lịch nghỉ đã công bố trước ngày khảo sát.

### Ma trận lựa chọn và tiêu chí đo

| Nhu cầu | Hướng phù hợp | Điều phải kiểm trên một flow mẫu |
|---|---|---|
| Workflow SaaS hoặc thiết bị có node cộng đồng sẵn | n8n/Node-RED; so license và node cụ thể | Import vào môi trường sạch; tỷ lệ node/credential khôi phục được; lỗi retry có nhân đôi side effect không |
| Nhúng canvas vào sản phẩm riêng | FlowGram; so với canvas có sẵn của nền tảng app | Graph round-trip giữ ID/schema; node chưa biết phải báo lỗi; version runtime/registry khớp |
| Thoát Prompt flow đang chạy | Microsoft Agent Framework ở mục 02, theo migration guide chính thức | Output parity trên ca thường/lỗi/timeout; latency, số gọi model/tool, tổng phí và kết quả side effect |
| Cần trung lập nhà cung cấp | Arazzo cho chuỗi API; Open Workflow DSL cho runtime hỗ trợ | Không suy từ schema pass ra runtime tương thích; kiểm conformance và mapping từng node thực sự dùng |

Không đặt ngưỡng chung “100% portable” cho mọi flow. Một hồ sơ tích hợp đủ bằng chứng nên ghi **số ca parity đạt/tổng**, phần node chưa hỗ trợ, và cách xử lý secret; số sao không đo các thuộc tính này.

### Kiến trúc ghép và điều kiện tích hợp

Một gói flow có thể di chuyển gồm **graph có phiên bản + mã node được ghim dependency + prompt/schema + bộ test + tham chiếu secret**. Flow là lớp điều phối; tích hợp SaaS quan trọng đặt sau hợp đồng API/Arazzo, tác vụ chạy lâu giao engine durable mục 21, hành động do model sinh giữ sandbox/quyền ở mục 11/12. Test output bằng công cụ mục 07 và kiểm trạng thái đích để phát hiện chạy lặp.

Khi đánh giá nền tảng, thử xuất gói, nhập vào một instance sạch cùng phiên bản, rồi mới thử adapter sang runtime khác. Đọc giấy phép của node/plugin bên thứ ba riêng với license core; MIT của FlowGram/Prompt flow và Apache của Node-RED không cấp quyền cho dịch vụ SaaS hoặc model được gọi. Bản đánh giá này chưa chạy bài thử khôi phục nên chưa tuyên bố thời gian di chuyển hay mức tương đương thực tế.

**Nguồn phần mở rộng:** [Node-RED settings](https://github.com/node-red/node-red/blob/22d019c4eccac31d95f3b6167c7334de72ef02a6/packages/node_modules/node-red/settings.js), [CI](https://github.com/node-red/node-red/blob/22d019c4eccac31d95f3b6167c7334de72ef02a6/.github/workflows/tests.yml), [FlowGram schema](https://github.com/bytedance/flowgram.ai/blob/f644642123ba05e0207594c582d4f42337af2a1c/packages/runtime/interface/src/schema/workflow.ts), [CI](https://github.com/bytedance/flowgram.ai/blob/f644642123ba05e0207594c582d4f42337af2a1c/.github/workflows/ci.yml), [Prompt flow notice](https://github.com/microsoft/promptflow/blob/33a68c9d3cf349d7fdfad1f41969af27543c0406/README.md), [migration loader](https://github.com/microsoft/promptflow/blob/33a68c9d3cf349d7fdfad1f41969af27543c0406/migration-guide/PromptFlow-to-MAF/workflow_loader.py), [Microsoft Learn: audit/rebuild/parity](https://learn.microsoft.com/en-us/azure/machine-learning/prompt-flow/how-to-migrate-prompt-flow-to-agent-framework?view=azureml-api-2). Các link code ghim commit; trang Learn là tài liệu chính thức sống, đọc 2/11/2026.

<a id="factory-lowcode-runtime-boundaries-2026-11-04"></a>

## Nâng trần 4/11/2026: low-code cho xưởng phải tách mặt quản trị, endpoint nghiệp vụ và bí mật khôi phục

> Đọc sâu Node-RED (OpenJS Foundation và contributors), Apache-2.0, `22d019c4eccac31d95f3b6167c7334de72ef02a6` ngày 2026-11-04; **code-read**. Không cài/chạy Node-RED; không cập nhật sao. SHA đọc lại không đổi so với phạm vi portability 2/11: đây là kiểm thêm đường bảo vệ runtime, không phải tuyên bố có bản phát hành mới.

**Trần còn thiếu:** phần portability đã yêu cầu mang đủ graph/dependencies/credentials. Khi dùng low-code làm xưởng, endpoint người dùng gọi và editor/admin API là hai ranh giới riêng; restore flow thành công cũng chưa chứng minh credential giải mã được hoặc tenant bị cách ly đúng.

### Node-RED: `adminAuth` không bảo vệ thay `httpNodeAuth`

- [Settings mặc định](https://github.com/node-red/node-red/blob/22d019c4eccac31d95f3b6167c7334de72ef02a6/packages/node_modules/node-red/settings.js) để `adminAuth`, `httpNodeAuth`, HTTPS và `uiHost` ở dạng ví dụ comment; mô tả UI mặc định nhận kết nối mọi IPv4 interface. Không công bố editor ra mạng chỉ vì “self-hosted”. Đây là default file tại SHA đã đọc; deployment/reverse proxy có thể thay đổi, cần kiểm cấu hình hiệu lực.
- [`needsPermission`](https://github.com/node-red/node-red/blob/22d019c4eccac31d95f3b6167c7334de72ef02a6/packages/node_modules/@node-red/editor-api/lib/auth/index.js) đi tiếp nếu không cấu hình `adminAuth`; [Bootstrap HTTP](https://github.com/node-red/node-red/blob/22d019c4eccac31d95f3b6167c7334de72ef02a6/packages/node_modules/node-red/red.js) gắn `httpNodeAuth` riêng tại `httpNodeRoot`. Bật auth cho editor không tự bảo vệ HTTP In endpoint; cổng authZ theo dữ liệu/người dùng vẫn do app hoặc gateway đảm trách.
- [Credential storage](https://github.com/node-red/node-red/blob/22d019c4eccac31d95f3b6167c7334de72ef02a6/packages/node_modules/@node-red/runtime/lib/nodes/credentials.js) có key hệ thống/người dùng/project, với nhánh tắt mã hoá khi cấu hình `false`. Backup chỉ flow JSON không đủ; phải biết key nào được dùng và thử restore với credential thật qua kho bí mật phù hợp. Không đưa giá trị secret vào flow export, catalog hoặc log.

| Lựa chọn | Vai trò hợp lý | Đường phải nghiệm thu |
|---|---|---|
| Node-RED | Flow sự kiện/integration, service nhỏ với node có sẵn | Hai mặt auth, node dependency, key restore và duplicate event |
| n8n (hồ sơ đầu mục) | Automation theo connector | License, credential binding, retry/idempotency và workspace boundary |
| Dify/Flowise (hồ sơ tương ứng) | Luồng LLM/RAG có UI | Prompt/dataset/model revision, export parity và provider data flow |
| Service/queue tất định | API trọng yếu có hợp đồng, test và owner rõ | Unit/integration/contract test; chi phí bảo trì có thể thấp hơn nền tảng |

**Chuỗi tích hợp:** (1) chốt workflow nào đáng dùng low-code, vẽ admin plane/data plane; (2) tách principal quản trị với principal nghiệp vụ, giới hạn mạng và cài node/plugin được review; (3) version flow cùng runtime/node/config manifest, tách secret reference; (4) dùng fixture để replay event, kiểm retry/timeout/idempotency và lỗi upstream; (5) restore sang instance sạch, kiểm giải mã credential, expected output và quyền; (6) đối chiếu trace/receipt với source version trước nhận bản phát hành.

**Cổng xưởng đề xuất:** anonymous không mở editor/admin; endpoint nghiệp vụ từ chối caller thiếu quyền dù admin đã đăng nhập ở nơi khác; backup/restore có receipt thành công; sự kiện trùng không tạo side effect trùng; tắt một node bắt buộc phải làm smoke test thất bại rõ. Nội dung này là ma trận kiểm đề xuất ở repo triển khai, **(chưa xác minh)** bằng cách chạy Node-RED trong `stored`.

**Nguồn:** [LICENSE](https://github.com/node-red/node-red/blob/22d019c4eccac31d95f3b6167c7334de72ef02a6/LICENSE) · [CI Node 22/24](https://github.com/node-red/node-red/blob/22d019c4eccac31d95f3b6167c7334de72ef02a6/.github/workflows/tests.yml). Nối mục 29 cho hợp đồng API, mục 30 cho test, mục 33 cho khôi phục và mục 34 cho identity/data.

## Nguồn

- https://www.knowlee.ai/blog/dify-alternatives-2026 · https://toolhalla.ai/blog/dify-vs-flowise-vs-langflow-2026 · https://www.jahanzaib.ai/blog/flowise-vs-dify-vs-n8n-ai-agents · https://rapidclaw.dev/blog/low-code-ai-agent-platforms-compared-2026 · https://makerstack.co/reviews/langflow-review/ · https://enterprisedna.co/directories/compare/dify-vs-flowise-vs-langflow/
- Bổ sung (12/10/2026): https://github.com/open-webui/open-webui · https://github.com/danny-avila/LibreChat · https://github.com/lobehub/lobehub · https://github.com/Mintplex-Labs/anything-llm · https://github.com/CherryHQ/cherry-studio · https://github.com/simstudioai/sim · https://github.com/labring/FastGPT · https://github.com/coze-dev/coze-studio · https://github.com/node-red/node-red · https://github.com/janhq/jan

<a id="xlsx-2026-11-23"></a>

## Đánh giá bổ sung từ bảng "Top 100 GitHub AI Skills" — 23/11/2026

Phần này có **2 hồ sơ** từ bảng xlsx người dùng gửi ngày 2026-11-23; đọc bằng `git clone --depth 1`, không cài hay chạy mã upstream. Lúc đọc, REST API của GitHub bị chặn nên trong hồ sơ ★ và `pushed_at` ghi **(chưa xác minh)**; số sao lấy lại cùng ngày qua GitHub search API nằm trong `data/projects.json` và [catalog/](../catalog/README.md), `pushed_at` vẫn chưa xác minh.

<a id="xlsx-2026-11-23-n8n-skills-czlonkowski"></a>

### n8n-skills (czlonkowski)

**Repo:** [czlonkowski/n8n-skills](https://github.com/czlonkowski/n8n-skills) · **License:** MIT (Copyright 2025 Romuald Członkowski); phần hook điều chỉnh từ `n8n-io/skills` (Apache-2.0, có `NOTICES` + `NOTICES-APACHE-2.0.txt`) · **★ 6.700 (GitHub search API, 2026-11-23)**

**Mục đích:** Bộ 14 skill + 1 skill router (`using-n8n-mcp-skills`) và lớp hook dạy coding agent dựng, kiểm, vận hành workflow n8n qua MCP server `n8n-mcp` (cùng tác giả, đã có hồ sơ ở mục 05).

**Giá trị và cơ chế:** Thư mục thật có đúng 15 thư mục `skills/` (khớp README "14 + router"). `hooks/hooks.json` gắn `SessionStart` (nạp skill router, tự xóa dấu "đã nhắc" khi `clear`/`compact`), 7 `PreToolUse` (`get_node`, `n8n_create_workflow`, `n8n_update_*`, `validate_workflow`, `n8n_test_workflow`, `n8n_instances`, `n8n_manage_credentials`) và 1 `PostToolUse` sau `validate_workflow`. Các hook chỉ chèn `additionalContext` nhắc skill, không chặn lệnh (README: "fails open"). `create-workflow.sh` còn quét payload tìm node Code/HTTP Request thiếu ghi chú `Why Code:`/`Why HTTP:`. Có 68 file JSON dưới `evaluations/` (phần lớn là hỏi đáp một lượt) và `evaluations/build-tasks/` (5 ca dựng workflow, `score.py` chấm JSON: loại node, trần phân trang, ghi chú Why, nối dây; chạy tay, mỗi lần là phiên agent tính phí, không chạy trong CI). Skill `n8n-self-hosting` kèm `assets/` (docker-compose single/queue, Caddyfile, `.env` mẫu) với mặc định an toàn ghi trong README: khóa mã hóa tường minh, không mở cổng nội bộ, tắt telemetry n8n.

**Giới hạn:** Không có `.github/` nên không có CI; `build.sh` chỉ dựng zip và so version hai manifest (`plugin.json` và `.claude-plugin/plugin.json` đều 1.38.0 khi đọc). `mcp.json` ở gốc trỏ `streamable-http` tới `https://api.n8n-mcp.com/mcp` (dịch vụ hosted của tác giả, không phải server tự lưu trữ); `.mcp.json.example` mới là bản `npx n8n-mcp` chạy cục bộ. Dùng bản hosted là gửi cấu trúc workflow tới bên thứ ba; telemetry của `n8n-mcp` xem hồ sơ n8n-MCP. Hook là shell, cần `jq` để đầy đủ (không có `jq` chỉ còn nhắc một lần). Gần như một tác giả (88 + 14 commit trên 107; 1 commit tên Claude), 107 commit từ 2025-10-20. README quảng bá dịch vụ tư vấn AiAdvisors (chỉ ở README). Chưa chạy hook, eval hay `n8n-mcp`.

**Cách tham khảo/tích hợp:** Mẫu "skill + hook nhắc đúng lúc + eval build-task chấm bằng script" đáng chép cho bộ skill riêng; ghim SHA khi cài plugin, dùng `.mcp.json.example` (stdio, cục bộ) thay vì endpoint hosted khi workflow chứa dữ liệu khách hàng, và đọc `hooks/` trước khi bật. Ghép với [n8n-MCP](../05-low-code-llm-platforms/README.md) (server) và mục 20 về vòng đời skill.

**Thay thế:** [n8n-MCP](../05-low-code-llm-platforms/README.md) (server, không phải skill), [tmolavi/n8n-agent-skills](#xlsx-2026-11-23-n8n-agent-skills-tmolavi) (16 skill, trung lập server, 1 tháng tuổi), `n8n-io/skills` (Apache-2.0, bản chính thức của n8n GmbH theo NOTICES của hai repo; chưa đọc, chưa xác minh số sao).

**Bằng chứng:** `code-read`, ngày 2026-11-23, commit [`ecdeca6f760b`](https://github.com/czlonkowski/n8n-skills/commit/ecdeca6f760b56bb1b11c0a7c961f11b69cb87d5) (2026-11-18). Đọc LICENSE, NOTICES, 2 manifest, `mcp.json`, `hooks.json`, `session-start.sh`, `create-workflow.sh`, `build.sh`, SKILL.md `n8n-self-hosting`, README build-tasks. Chưa chạy mã, chưa đọc từng SKILL còn lại.

**Nguồn:** [README.md](https://github.com/czlonkowski/n8n-skills/blob/ecdeca6f760b56bb1b11c0a7c961f11b69cb87d5/README.md) · [LICENSE](https://github.com/czlonkowski/n8n-skills/blob/ecdeca6f760b56bb1b11c0a7c961f11b69cb87d5/LICENSE) · [NOTICES](https://github.com/czlonkowski/n8n-skills/blob/ecdeca6f760b56bb1b11c0a7c961f11b69cb87d5/NOTICES) · [hooks.json](https://github.com/czlonkowski/n8n-skills/blob/ecdeca6f760b56bb1b11c0a7c961f11b69cb87d5/hooks/hooks.json) · [mcp.json](https://github.com/czlonkowski/n8n-skills/blob/ecdeca6f760b56bb1b11c0a7c961f11b69cb87d5/mcp.json) · [plugin.json](https://github.com/czlonkowski/n8n-skills/blob/ecdeca6f760b56bb1b11c0a7c961f11b69cb87d5/.claude-plugin/plugin.json) · [build-tasks](https://github.com/czlonkowski/n8n-skills/blob/ecdeca6f760b56bb1b11c0a7c961f11b69cb87d5/evaluations/build-tasks/README.md) · [metadata GitHub](https://api.github.com/search/repositories?q=repo:czlonkowski/n8n-skills).

<a id="xlsx-2026-11-23-n8n-agent-skills-tmolavi"></a>

### n8n-agent-skills (tmolavi)

**Repo:** [tmolavi/n8n-agent-skills](https://github.com/tmolavi/n8n-agent-skills) · **License:** MIT (Copyright 2026 Taghi Molavi) · **★ 2 (GitHub search API, 2026-11-23)**

**Mục đích:** Bộ 16 skill n8n "trung lập server MCP" (router, lifecycle, MCP tooling, expressions, node, code, loop, agent, lỗi, credential, sub-workflow, binary, data table, debug, SEO/GEO, production ops) kèm manifest Claude Code/Codex, plugin OpenCode và cấu hình MCP mẫu.

**Giá trị và cơ chế:** `skills/` có đúng 16 thư mục, khớp README. Hook (`SessionStart` + 4 `PreToolUse` gate + `PostToolUse` nhắc) chỉ chèn nhắc nhở; `side-effects-gate.sh` nhắc hỏi người dùng trước khi `test_workflow`/`execute_workflow` có thể gây tác dụng phụ thật (Slack, DB, thanh toán). `configs/mcp.multi.example.json` gom ví dụ cho server chính thức và các server cộng đồng. `.claude-plugin/plugin.json` khai `userConfig` (URL n8n) và MCP `${user_config.n8n_url}/mcp-server/http`.

**Giới hạn:** Repo mới (2026-08-27), 2 commit, 2 sao, một tác giả; không có `.github/workflows` (không CI). `scripts/validate-skills.sh` chỉ kiểm có `name:`/`description:` và **cảnh báo khi thiếu link `molavi.pro`**; cả 16 SKILL.md đều chứa link quảng bá tác giả, mọi hook nhắc đều in `Repo/Author` vào ngữ cảnh agent, và skill `n8n-ai-seo-geo-automation` đẩy sang công cụ riêng của tác giả (`geo-scope`, `mcp-geo-server`). `NOTICE` ghi cảm hứng từ `n8n-io/skills` (Apache-2.0) và `n8n-mcp` nhưng không có file giấy phép Apache kèm theo như repo czlonkowski (mức sao chép chưa so, chưa xác minh). Tên tác giả hiện hai dạng (Taghi/Taqi Molavi). Chưa chạy hook hay installer; `scripts/install.sh` ghi đè thư mục skill đích (`rm -rf` rồi `cp -R`), nên dùng `--dry-run` trước.

**Cách tham khảo/tích hợp:** Chỉ nên lấy ý tưởng bảng chọn server MCP (`n8n-mcp-tooling/references/SERVER_MATRIX.md`) hoặc đọc làm đối chiếu; nếu dùng thật, tách link/quảng bá khỏi hook và ghim SHA. Với dự án nghiêm túc ưu tiên bộ czlonkowski hoặc `n8n-io/skills`.

**Thay thế:** [n8n-skills (czlonkowski)](#xlsx-2026-11-23-n8n-skills-czlonkowski), [n8n-MCP](../05-low-code-llm-platforms/README.md), `n8n-io/skills` (chưa đọc).

**Bằng chứng:** `code-read`, ngày 2026-11-23, commit [`868436013817`](https://github.com/tmolavi/n8n-agent-skills/commit/868436013817a5f62a917aa6c6cb93881945c9be) (2026-09-18). Đọc LICENSE, NOTICE, package.json, plugin.json, hooks.json, `side-effects-gate.sh`, `validate-skills.sh`, `install.sh` (đầu file), CHANGELOG, SECURITY, SKILL credentials và SEO/GEO. Chưa chạy mã.

**Nguồn:** [README.md](https://github.com/tmolavi/n8n-agent-skills/blob/868436013817a5f62a917aa6c6cb93881945c9be/README.md) · [LICENSE](https://github.com/tmolavi/n8n-agent-skills/blob/868436013817a5f62a917aa6c6cb93881945c9be/LICENSE) · [NOTICE](https://github.com/tmolavi/n8n-agent-skills/blob/868436013817a5f62a917aa6c6cb93881945c9be/NOTICE) · [hooks.json](https://github.com/tmolavi/n8n-agent-skills/blob/868436013817a5f62a917aa6c6cb93881945c9be/hooks/hooks.json) · [validate-skills.sh](https://github.com/tmolavi/n8n-agent-skills/blob/868436013817a5f62a917aa6c6cb93881945c9be/scripts/validate-skills.sh) · [side-effects-gate.sh](https://github.com/tmolavi/n8n-agent-skills/blob/868436013817a5f62a917aa6c6cb93881945c9be/hooks/pre-tool-use/side-effects-gate.sh) · [plugin.json](https://github.com/tmolavi/n8n-agent-skills/blob/868436013817a5f62a917aa6c6cb93881945c9be/.claude-plugin/plugin.json) · [metadata GitHub](https://api.github.com/search/repositories?q=repo:tmolavi/n8n-agent-skills).

<a id="chuan-hoa-2026-11-23"></a>

## Chuẩn hóa bằng chứng hồ sơ cũ — 23/11/2026

Các hồ sơ dưới đây có từ trước khi kho ghi mức kiểm. Ngày 2026-11-23 mỗi repo được clone nông tại commit ghi trong bảng, đọc LICENSE, README, manifest và CI (nếu có); không cài, build hay chạy mã upstream. Nhận định cũ ở phần trên giữ nguyên; chỗ nào khác với lần đọc này được ghi trong cột Nhận định. Số sao lấy qua GitHub search API cùng ngày.

<a id="ch-ai-agents-a-z-n8n-templates"></a>

### AI Agents A-Z (n8n templates)

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/gyoridavid/ai_agents_az |
| License | Không có file LICENSE (khớp catalog) |
| Phiên bản đã đọc | `764fac221bf6f1dba94d016e2e4e0d450e3cba51` (commit 2025-12-19) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md; chưa chạy upstream |
| Bảo trì | Ít hoạt động (commit cuối 2025-12-19) |
| Nhận định | Kho template n8n đi kèm video YouTube (agent, video faceless qua dịch vụ trả phí bên thứ ba). Tham khảo cấu trúc workflow được; không có LICENSE nên không có quyền tái sử dụng rõ ràng, đã ngừng cập nhật từ 12/2025. |
| Nguồn | [README.md](https://github.com/gyoridavid/ai_agents_az/blob/764fac221bf6f1dba94d016e2e4e0d450e3cba51/README.md) |

<a id="ch-anythingllm"></a>

### AnythingLLM

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/Mintplex-Labs/anything-llm |
| License | MIT |
| Phiên bản đã đọc | `472b1e3f4715c6ccd38a099aecd4651a449188aa` (commit 2026-11-20) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE, package.json, .github/workflows/run-tests.yaml; chưa chạy upstream |
| Bảo trì | Đang hoạt động (commit cuối 2026-11-20) |
| Nhận định | App RAG + agent local-first (desktop/Docker) gồm server, collector, frontend, embed, browser-extension. Telemetry bật mặc định theo catalog cũ (chưa xác minh lại trong lần đọc này). |
| Nguồn | [README.md](https://github.com/Mintplex-Labs/anything-llm/blob/472b1e3f4715c6ccd38a099aecd4651a449188aa/README.md) · [LICENSE](https://github.com/Mintplex-Labs/anything-llm/blob/472b1e3f4715c6ccd38a099aecd4651a449188aa/LICENSE) · [package.json](https://github.com/Mintplex-Labs/anything-llm/blob/472b1e3f4715c6ccd38a099aecd4651a449188aa/package.json) · [.github/workflows/run-tests.yaml](https://github.com/Mintplex-Labs/anything-llm/blob/472b1e3f4715c6ccd38a099aecd4651a449188aa/.github/workflows/run-tests.yaml) |

<a id="ch-arazzo-specification"></a>

### Arazzo Specification

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/OAI/Arazzo-Specification |
| License | Apache-2.0 |
| Phiên bản đã đọc | `12f619ecd85e79fb67ce0610b85926ca3cfd9c79` (commit 2026-11-09) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE, package.json, .github/workflows/schema-tests.yaml; chưa chạy upstream |
| Bảo trì | Đang hoạt động (commit cuối 2026-11-09) |
| Nhận định | Chuẩn OpenAPI Initiative mô tả chuỗi gọi API (workflow, bước, điều kiện) dạng máy đọc; repo chứa spec theo phiên bản, schema và ví dụ, CI kiểm schema và markdown. |
| Nguồn | [README.md](https://github.com/OAI/Arazzo-Specification/blob/12f619ecd85e79fb67ce0610b85926ca3cfd9c79/README.md) · [LICENSE](https://github.com/OAI/Arazzo-Specification/blob/12f619ecd85e79fb67ce0610b85926ca3cfd9c79/LICENSE) · [package.json](https://github.com/OAI/Arazzo-Specification/blob/12f619ecd85e79fb67ce0610b85926ca3cfd9c79/package.json) · [.github/workflows/schema-tests.yaml](https://github.com/OAI/Arazzo-Specification/blob/12f619ecd85e79fb67ce0610b85926ca3cfd9c79/.github/workflows/schema-tests.yaml) |

<a id="ch-astron-agent"></a>

### Astron Agent

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/iflytek/astron-agent |
| License | Apache-2.0 |
| Phiên bản đã đọc | `831e7b1628cdf8f117dfe0d2249c9fb05cabb4be` (commit 2026-11-03) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE, Makefile, .github/workflows/ci.yml; chưa chạy upstream |
| Bảo trì | Đang hoạt động (commit cuối 2026-11-03) |
| Nhận định | Nền tảng agentic workflow + RPA + MCP của iFlytek, đa ngôn ngữ (console/core), triển khai Docker/Helm. Rủi ro mật khẩu mặc định yếu và endpoint mặc định của iFlytek theo catalog cũ (chưa xác minh lại). |
| Nguồn | [README.md](https://github.com/iflytek/astron-agent/blob/831e7b1628cdf8f117dfe0d2249c9fb05cabb4be/README.md) · [LICENSE](https://github.com/iflytek/astron-agent/blob/831e7b1628cdf8f117dfe0d2249c9fb05cabb4be/LICENSE) · [Makefile](https://github.com/iflytek/astron-agent/blob/831e7b1628cdf8f117dfe0d2249c9fb05cabb4be/Makefile) · [.github/workflows/ci.yml](https://github.com/iflytek/astron-agent/blob/831e7b1628cdf8f117dfe0d2249c9fb05cabb4be/.github/workflows/ci.yml) |

<a id="ch-budibase"></a>

### Budibase

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/Budibase/budibase |
| License | GPL-3.0 / MPL-2.0 / BSL (packages/pro), kèm SQS_LICENSE bên thứ ba |
| Phiên bản đã đọc | `f29a398e324efa0fcc766851aad1f5810e39ccfb` (commit 2026-11-23) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE, package.json, .github/workflows/budibase_ci.yml; chưa chạy upstream |
| Bảo trì | Đang hoạt động (commit cuối 2026-11-23) |
| Nhận định | Nền tảng app nội bộ + automation + agent AI, monorepo nhiều license. Phải đọc license từng package trước khi tái sử dụng; packages/pro là BSL nên không gỡ kiểm license khi chạy production. |
| Nguồn | [README.md](https://github.com/Budibase/budibase/blob/f29a398e324efa0fcc766851aad1f5810e39ccfb/README.md) · [LICENSE](https://github.com/Budibase/budibase/blob/f29a398e324efa0fcc766851aad1f5810e39ccfb/LICENSE) · [package.json](https://github.com/Budibase/budibase/blob/f29a398e324efa0fcc766851aad1f5810e39ccfb/package.json) · [.github/workflows/budibase_ci.yml](https://github.com/Budibase/budibase/blob/f29a398e324efa0fcc766851aad1f5810e39ccfb/.github/workflows/budibase_ci.yml) |

<a id="ch-cherry-studio"></a>

### Cherry Studio

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/CherryHQ/cherry-studio |
| License | AGPL-3.0 |
| Phiên bản đã đọc | `cc24ac0445071fc848f678dc9e975efeac4faea0` (commit 2026-11-23) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE, package.json, .github/workflows/ci.yml; chưa chạy upstream |
| Bảo trì | Đang hoạt động (commit cuối 2026-11-23) |
| Nhận định | Client desktop (Electron) đa nhà cung cấp LLM, có agent và trợ lý dựng sẵn. AGPL ràng buộc khi phân phối bản sửa; bản Enterprise đóng theo catalog cũ (chưa xác minh). |
| Nguồn | [README.md](https://github.com/CherryHQ/cherry-studio/blob/cc24ac0445071fc848f678dc9e975efeac4faea0/README.md) · [LICENSE](https://github.com/CherryHQ/cherry-studio/blob/cc24ac0445071fc848f678dc9e975efeac4faea0/LICENSE) · [package.json](https://github.com/CherryHQ/cherry-studio/blob/cc24ac0445071fc848f678dc9e975efeac4faea0/package.json) · [.github/workflows/ci.yml](https://github.com/CherryHQ/cherry-studio/blob/cc24ac0445071fc848f678dc9e975efeac4faea0/.github/workflows/ci.yml) |

<a id="ch-coze-studio"></a>

### Coze Studio

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/coze-dev/coze-studio |
| License | Apache-2.0 (file LICENSE-APACHE) |
| Phiên bản đã đọc | `fefb05ff27be1da939612fbf9faf5db62583b8ae` (commit 2026-07-29) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE-APACHE, rush.json, .github/workflows/ci.yml; chưa chạy upstream |
| Bảo trì | Ít hoạt động (commit cuối 2026-07-29) |
| Nhận định | Bản mở của nền tảng agent/workflow Coze (ByteDance), backend Go + frontend monorepo Rush, triển khai Docker/Helm. Hoạt động gần như dừng từ 7/2026 nên rủi ro bảo trì cao. |
| Nguồn | [README.md](https://github.com/coze-dev/coze-studio/blob/fefb05ff27be1da939612fbf9faf5db62583b8ae/README.md) · [LICENSE-APACHE](https://github.com/coze-dev/coze-studio/blob/fefb05ff27be1da939612fbf9faf5db62583b8ae/LICENSE-APACHE) · [rush.json](https://github.com/coze-dev/coze-studio/blob/fefb05ff27be1da939612fbf9faf5db62583b8ae/rush.json) · [.github/workflows/ci.yml](https://github.com/coze-dev/coze-studio/blob/fefb05ff27be1da939612fbf9faf5db62583b8ae/.github/workflows/ci.yml) |

<a id="ch-dify"></a>

### Dify

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/langgenius/dify |
| License | Apache-2.0 sửa đổi (thêm điều kiện multi-tenant/thương hiệu) |
| Phiên bản đã đọc | `e62d1e37a523dc1ce42c56b7100380022291c598` (commit 2026-11-23) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE, package.json, .github/workflows/main-ci.yml; chưa chạy upstream |
| Bảo trì | Đang hoạt động (commit cuối 2026-11-23) |
| Nhận định | Nền tảng LLM app/workflow/RAG lớn (api Python, web, CLI, dify-agent). License không phải Apache thuần: chạy SaaS nhiều tenant hoặc gỡ thương hiệu cần license thương mại. |
| Nguồn | [README.md](https://github.com/langgenius/dify/blob/e62d1e37a523dc1ce42c56b7100380022291c598/README.md) · [LICENSE](https://github.com/langgenius/dify/blob/e62d1e37a523dc1ce42c56b7100380022291c598/LICENSE) · [package.json](https://github.com/langgenius/dify/blob/e62d1e37a523dc1ce42c56b7100380022291c598/package.json) · [.github/workflows/main-ci.yml](https://github.com/langgenius/dify/blob/e62d1e37a523dc1ce42c56b7100380022291c598/.github/workflows/main-ci.yml) |

<a id="ch-fastgpt"></a>

### FastGPT

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/labring/FastGPT |
| License | FastGPT Open Source License (Apache-2.0 + điều kiện) |
| Phiên bản đã đọc | `9aea02765a34642e0ed1dcb88f0168bf9e607211` (commit 2026-11-23) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE, package.json, .github/workflows/test-fastgpt.yaml; chưa chạy upstream |
| Bảo trì | Đang hoạt động (commit cuối 2026-11-23) |
| Nhận định | Nền tảng RAG + workflow (monorepo pnpm, sandbox code/browser, MCP server). License riêng không OSI: cung cấp dịch vụ nhiều tenant hoặc gỡ thương hiệu cần license thương mại theo LICENSE. |
| Nguồn | [README.md](https://github.com/labring/FastGPT/blob/9aea02765a34642e0ed1dcb88f0168bf9e607211/README.md) · [LICENSE](https://github.com/labring/FastGPT/blob/9aea02765a34642e0ed1dcb88f0168bf9e607211/LICENSE) · [package.json](https://github.com/labring/FastGPT/blob/9aea02765a34642e0ed1dcb88f0168bf9e607211/package.json) · [.github/workflows/test-fastgpt.yaml](https://github.com/labring/FastGPT/blob/9aea02765a34642e0ed1dcb88f0168bf9e607211/.github/workflows/test-fastgpt.yaml) |

<a id="ch-flowise"></a>

### Flowise

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/FlowiseAI/Flowise |
| License | Apache-2.0 trừ thư mục enterprise (thương mại); catalog JSON chỉ ghi Apache-2.0 |
| Phiên bản đã đọc | `9291856d1ea4a4ceea9f8fef8ce14f4f6c81e8eb` (commit 2026-08-13) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE.md, package.json, .github/workflows/main.yml; chưa chạy upstream |
| Bảo trì | Đã archive (commit cuối 2026-08-13) |
| Nhận định | Builder kéo-thả LangChain/agentflow, bản cuối 3.1.4. Đã archive nên không nhận bản vá; phần enterprise không thuộc Apache-2.0. Không nên chọn cho dự án mới. |
| Nguồn | [README.md](https://github.com/FlowiseAI/Flowise/blob/9291856d1ea4a4ceea9f8fef8ce14f4f6c81e8eb/README.md) · [LICENSE.md](https://github.com/FlowiseAI/Flowise/blob/9291856d1ea4a4ceea9f8fef8ce14f4f6c81e8eb/LICENSE.md) · [package.json](https://github.com/FlowiseAI/Flowise/blob/9291856d1ea4a4ceea9f8fef8ce14f4f6c81e8eb/package.json) · [.github/workflows/main.yml](https://github.com/FlowiseAI/Flowise/blob/9291856d1ea4a4ceea9f8fef8ce14f4f6c81e8eb/.github/workflows/main.yml) |

<a id="ch-langflow"></a>

### Langflow

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/langflow-ai/langflow |
| License | MIT |
| Phiên bản đã đọc | `21381e5b2964fb4c714dc91fcd5187d4cfc2a67f` (commit 2026-11-17) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE, pyproject.toml, .github/workflows/ci.yml; chưa chạy upstream |
| Bảo trì | Đang hoạt động (commit cuối 2026-11-17) |
| Nhận định | Builder visual cho agent/RAG bằng Python, CI rất dày. Điểm đáng chú ý: bản phát hành mặc định tắt auto-login, phải đặt mật khẩu superuser trước khi chạy. |
| Nguồn | [README.md](https://github.com/langflow-ai/langflow/blob/21381e5b2964fb4c714dc91fcd5187d4cfc2a67f/README.md) · [LICENSE](https://github.com/langflow-ai/langflow/blob/21381e5b2964fb4c714dc91fcd5187d4cfc2a67f/LICENSE) · [pyproject.toml](https://github.com/langflow-ai/langflow/blob/21381e5b2964fb4c714dc91fcd5187d4cfc2a67f/pyproject.toml) · [.github/workflows/ci.yml](https://github.com/langflow-ai/langflow/blob/21381e5b2964fb4c714dc91fcd5187d4cfc2a67f/.github/workflows/ci.yml) |

<a id="ch-librechat"></a>

### LibreChat

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/LibreChat-AI/LibreChat |
| License | MIT |
| Phiên bản đã đọc | `4700c44eb77c142b4f9f8b87476924f22890eb39` (commit 2026-11-19) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE, package.json, .github/workflows/backend-review.yml; chưa chạy upstream |
| Bảo trì | Đang hoạt động (commit cuối 2026-11-19) |
| Nhận định | Chat UI tự host đa nhà cung cấp, agent, MCP, OAuth2/LDAP; MIT thuần. Repo đã chuyển sang org LibreChat-AI, cần cập nhật link cũ danny-avila trong catalog. |
| Nguồn | [README.md](https://github.com/LibreChat-AI/LibreChat/blob/4700c44eb77c142b4f9f8b87476924f22890eb39/README.md) · [LICENSE](https://github.com/LibreChat-AI/LibreChat/blob/4700c44eb77c142b4f9f8b87476924f22890eb39/LICENSE) · [package.json](https://github.com/LibreChat-AI/LibreChat/blob/4700c44eb77c142b4f9f8b87476924f22890eb39/package.json) · [.github/workflows/backend-review.yml](https://github.com/LibreChat-AI/LibreChat/blob/4700c44eb77c142b4f9f8b87476924f22890eb39/.github/workflows/backend-review.yml) |

<a id="ch-lobehub"></a>

### LobeHub

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/lobehub/lobehub |
| License | LobeHub Community License (package.json ghi MIT, mâu thuẫn) |
| Phiên bản đã đọc | `18ff6aead33b35bfb8b6a4566ffa66578f81041e` (commit 2026-11-23) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE, package.json, .github/workflows/test.yml; chưa chạy upstream |
| Bảo trì | Đang hoạt động (commit cuối 2026-11-23) |
| Nhận định | Workspace agent + chat web/desktop, phát hành rất dày (v2.3.4). License riêng không OSI; trường license MIT trong package.json gây hiểu nhầm, căn cứ vào file LICENSE. |
| Nguồn | [README.md](https://github.com/lobehub/lobehub/blob/18ff6aead33b35bfb8b6a4566ffa66578f81041e/README.md) · [LICENSE](https://github.com/lobehub/lobehub/blob/18ff6aead33b35bfb8b6a4566ffa66578f81041e/LICENSE) · [package.json](https://github.com/lobehub/lobehub/blob/18ff6aead33b35bfb8b6a4566ffa66578f81041e/package.json) · [.github/workflows/test.yml](https://github.com/lobehub/lobehub/blob/18ff6aead33b35bfb8b6a4566ffa66578f81041e/.github/workflows/test.yml) |

<a id="ch-n8n"></a>

### n8n

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/n8n-io/n8n |
| License | Sustainable Use + Enterprise (.ee) — khớp catalog, bổ sung phần EE |
| Phiên bản đã đọc | `dc913a32da41ea52e1aa6c82e79e767569ce0ef3` (commit 2026-11-23) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE.md, LICENSE_EE.md, package.json, .github/workflows/ci-master.yml; chưa chạy upstream |
| Bảo trì | Đang hoạt động (commit cuối 2026-11-23) |
| Nhận định | Nền tảng workflow automation có node AI/agent. Không phải mã mở OSI: cấm cung cấp lại như dịch vụ thương mại; tính năng .ee cần license Enterprise. |
| Nguồn | [README.md](https://github.com/n8n-io/n8n/blob/dc913a32da41ea52e1aa6c82e79e767569ce0ef3/README.md) · [LICENSE.md](https://github.com/n8n-io/n8n/blob/dc913a32da41ea52e1aa6c82e79e767569ce0ef3/LICENSE.md) · [LICENSE_EE.md](https://github.com/n8n-io/n8n/blob/dc913a32da41ea52e1aa6c82e79e767569ce0ef3/LICENSE_EE.md) · [package.json](https://github.com/n8n-io/n8n/blob/dc913a32da41ea52e1aa6c82e79e767569ce0ef3/package.json) · [.github/workflows/ci-master.yml](https://github.com/n8n-io/n8n/blob/dc913a32da41ea52e1aa6c82e79e767569ce0ef3/.github/workflows/ci-master.yml) |

<a id="ch-n8n-mcp"></a>

### n8n-MCP

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/czlonkowski/n8n-mcp |
| License | MIT |
| Phiên bản đã đọc | `a816db89fd6180f9b2b56c1935ea8078c8d27104` (commit 2026-11-19) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE, package.json, .github/workflows/test.yml; chưa chạy upstream |
| Bảo trì | Đang hoạt động (commit cuối 2026-11-19) |
| Nhận định | MCP server cho coding agent tra cứu node và quản lý workflow n8n. Telemetry mặc định gửi workflow đã làm sạch theo catalog cũ (chưa xác minh lại lần này). |
| Nguồn | [README.md](https://github.com/czlonkowski/n8n-mcp/blob/a816db89fd6180f9b2b56c1935ea8078c8d27104/README.md) · [LICENSE](https://github.com/czlonkowski/n8n-mcp/blob/a816db89fd6180f9b2b56c1935ea8078c8d27104/LICENSE) · [package.json](https://github.com/czlonkowski/n8n-mcp/blob/a816db89fd6180f9b2b56c1935ea8078c8d27104/package.json) · [.github/workflows/test.yml](https://github.com/czlonkowski/n8n-mcp/blob/a816db89fd6180f9b2b56c1935ea8078c8d27104/.github/workflows/test.yml) |

<a id="ch-open-webui"></a>

### Open WebUI

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/open-webui/open-webui |
| License | Open WebUI License (BSD-3 + branding), kèm LICENSE_HISTORY |
| Phiên bản đã đọc | `0666e59d26a4d056e0bacee41742486badd71cf8` (commit 2026-11-17) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE, LICENSE_HISTORY, LICENSE_NOTICE, package.json, .github/workflows/backend.yaml; chưa chạy upstream |
| Bảo trì | Đang hoạt động (commit cuối 2026-11-17) |
| Nhận định | Chat UI tự host phổ biến (SvelteKit + backend Python). Không được gỡ branding ngoài các ngoại lệ trong LICENSE; repo đa license theo thời điểm đóng góp. |
| Nguồn | [README.md](https://github.com/open-webui/open-webui/blob/0666e59d26a4d056e0bacee41742486badd71cf8/README.md) · [LICENSE](https://github.com/open-webui/open-webui/blob/0666e59d26a4d056e0bacee41742486badd71cf8/LICENSE) · [LICENSE_HISTORY](https://github.com/open-webui/open-webui/blob/0666e59d26a4d056e0bacee41742486badd71cf8/LICENSE_HISTORY) · [LICENSE_NOTICE](https://github.com/open-webui/open-webui/blob/0666e59d26a4d056e0bacee41742486badd71cf8/LICENSE_NOTICE) · [package.json](https://github.com/open-webui/open-webui/blob/0666e59d26a4d056e0bacee41742486badd71cf8/package.json) · [.github/workflows/backend.yaml](https://github.com/open-webui/open-webui/blob/0666e59d26a4d056e0bacee41742486badd71cf8/.github/workflows/backend.yaml) |

<a id="ch-open-workflow-specification"></a>

### Open Workflow Specification

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/open-workflow-specification/specification |
| License | Apache-2.0 |
| Phiên bản đã đọc | `09ad1deea8a8bb9d34bfded261b14c054dcf92c7` (commit 2026-11-12) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE, .github/workflows/schema-check.yaml; chưa chạy upstream |
| Bảo trì | Đang hoạt động (commit cuối 2026-11-12) |
| Nhận định | DSL workflow trung lập nhà cung cấp (trước là Serverless Workflow, CNCF) với schema YAML và bộ test tuân thủ (ctk). Hữu ích làm tham chiếu định dạng workflow. |
| Nguồn | [README.md](https://github.com/open-workflow-specification/specification/blob/09ad1deea8a8bb9d34bfded261b14c054dcf92c7/README.md) · [LICENSE](https://github.com/open-workflow-specification/specification/blob/09ad1deea8a8bb9d34bfded261b14c054dcf92c7/LICENSE) · [.github/workflows/schema-check.yaml](https://github.com/open-workflow-specification/specification/blob/09ad1deea8a8bb9d34bfded261b14c054dcf92c7/.github/workflows/schema-check.yaml) |

<a id="ch-sim"></a>

### Sim

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/simstudioai/sim |
| License | Apache-2.0 |
| Phiên bản đã đọc | `1814ccd70e21906216bca2a08f95d6a2841db406` (commit 2026-11-22) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE, package.json, .github/workflows/ci.yml; chưa chạy upstream |
| Bảo trì | Đang hoạt động (commit cuối 2026-11-22) |
| Nhận định | Canvas dựng và triển khai workflow agent, hỗ trợ model local qua Ollama. Số tích hợp 1.000+ là tuyên bố của tác giả **(chưa xác minh)**. |
| Nguồn | [README.md](https://github.com/simstudioai/sim/blob/1814ccd70e21906216bca2a08f95d6a2841db406/README.md) · [LICENSE](https://github.com/simstudioai/sim/blob/1814ccd70e21906216bca2a08f95d6a2841db406/LICENSE) · [package.json](https://github.com/simstudioai/sim/blob/1814ccd70e21906216bca2a08f95d6a2841db406/package.json) · [.github/workflows/ci.yml](https://github.com/simstudioai/sim/blob/1814ccd70e21906216bca2a08f95d6a2841db406/.github/workflows/ci.yml) |

<a id="ch-tooljet"></a>

### ToolJet

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/ToolJet/ToolJet |
| License | AGPL-3.0; EE là submodule riêng |
| Phiên bản đã đọc | `e921d9a9558cb065cfbb1db733fbc7e6a7fd5683` (commit 2026-11-23) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE, .gitmodules, .github/workflows/ci.yml; chưa chạy upstream |
| Bảo trì | Đang hoạt động (commit cuối 2026-11-23) |
| Nhận định | Nền tảng internal tool dựng bằng prompt/MCP. Bản mở AGPL nhưng phần EE là submodule riêng, quickstart dùng image EE theo catalog cũ. |
| Nguồn | [README.md](https://github.com/ToolJet/ToolJet/blob/e921d9a9558cb065cfbb1db733fbc7e6a7fd5683/README.md) · [LICENSE](https://github.com/ToolJet/ToolJet/blob/e921d9a9558cb065cfbb1db733fbc7e6a7fd5683/LICENSE) · [.gitmodules](https://github.com/ToolJet/ToolJet/blob/e921d9a9558cb065cfbb1db733fbc7e6a7fd5683/.gitmodules) · [.github/workflows/ci.yml](https://github.com/ToolJet/ToolJet/blob/e921d9a9558cb065cfbb1db733fbc7e6a7fd5683/.github/workflows/ci.yml) |

<a id="nt-2026-11-23"></a>

## Nâng trần theo khoảng trống — 23/11/2026

Phần này có các hồ sơ mới của đợt nâng trần: mười trinh sát tìm trên internet và GitHub những mảng mà chuyên mục còn thiếu hoặc chỉ có hồ sơ cũ, rồi mỗi repo được clone nông tại một commit cố định, đọc LICENSE, README, ít nhất một file triển khai thật và CI nếu có; không cài hay chạy mã upstream. Mô tả của trinh sát nhiều chỗ sai so với mã thật, và các chỗ đó được sửa ngay trong từng hồ sơ. Số sao lấy sau bằng GitHub search API nên có thể để trống.

<a id="nt-workflowbuilder"></a>

### Workflow Builder (Synergy Codes)

| Thuộc tính | Giá trị |
|---|---|
| Repo | https://github.com/synergycodes/workflowbuilder |
| License | Apache-2.0 (LICENSE gốc và từng gói ui, sdk, temporal, mcp-server) |
| Phiên bản đã đọc | `9b6e3b01066967b94346aa66db0cd4b75dc78d05` (commit 2026-11-23) |
| Kiểm chứng | 2026-11-23; code-read; đã đọc LICENSE, README.md, packages/temporal/src/workflow/durable-pause.decision-log.md, packages/temporal/src/workflow/verdict-validation.ts, apps/backend/README.md, .github/workflows/pr-check.yml; chưa chạy upstream |
| Khoảng trống lấp | Human-in-the-loop và phê duyệt (trình dựng workflow nhúng cộng thực thi bền trên Temporal) |
| Cơ chế đáng học | - Editor React (`packages/sdk`, `packages/ui`) xuất workflow JSON; backend và plugin Temporal chạy một workflow tổng quát cho mọi sơ đồ, mỗi node một Activity (`packages/temporal`).<br>- Bước chờ người: node trả `{ waiting: true }`, workflow đợi bằng Temporal Update `resolveNode` chứ không dùng signal, để quyết định đến muộn nhận câu trả lời đồng bộ thay vì mất im lặng (`durable-pause.decision-log.md`).<br>- `verdict-validation.ts` chỉ kiểm tính toàn vẹn của engine: verdict sai định dạng, node lạ, đã có verdict (first-write-wins) hoặc node không đang chờ đều bị từ chối trước khi vào lịch sử. |
| Tiêu chí và cách kiểm | Có test determinism/replay cho execution-core và lịch sử replay ghim (decision log nêu thư mục `test/replay/`; mình chưa mở). `pr-check.yml` kiểm format, lint, test của các gói đã phát hành và cổng air-gap cho Dockerfile; mình chỉ đọc phần đầu, chưa chạy. |
| Giới hạn và rủi ro | Backend không có xác thực thật: `AllowAllAuthPort` bắt buộc đặt `WB_AUTH_PORT=allow-all` mới chạy, không có cô lập tenant; README cảnh báo không mở ra mạng chung, và compose deploy ai-studio publish cổng 8080 trên mọi interface. Tuyên bố của README về "approve with corrections" chỉ đúng một nửa: apps/backend/README.md ghi các chỉnh sửa (`edits`) được lưu nhưng chưa được áp vào bước sau (follow-up decision-settled-values). Chưa thấy phê duyệt nhiều cấp có sẵn: node phê duyệt là từng bước riêng, ghép nhiều cấp là việc của người dùng; trinh sát ghi "nhiều cấp" là chưa xác minh. Cần Temporal và Postgres tự vận hành. |
| So với | temporal, n8n, langgraph |
| Nguồn | [LICENSE](https://github.com/synergycodes/workflowbuilder/blob/9b6e3b01066967b94346aa66db0cd4b75dc78d05/LICENSE) · [README.md](https://github.com/synergycodes/workflowbuilder/blob/9b6e3b01066967b94346aa66db0cd4b75dc78d05/README.md) · [durable-pause.decision-log.md](https://github.com/synergycodes/workflowbuilder/blob/9b6e3b01066967b94346aa66db0cd4b75dc78d05/packages/temporal/src/workflow/durable-pause.decision-log.md) · [verdict-validation.ts](https://github.com/synergycodes/workflowbuilder/blob/9b6e3b01066967b94346aa66db0cd4b75dc78d05/packages/temporal/src/workflow/verdict-validation.ts) · [README.md](https://github.com/synergycodes/workflowbuilder/blob/9b6e3b01066967b94346aa66db0cd4b75dc78d05/apps/backend/README.md) · [pr-check.yml](https://github.com/synergycodes/workflowbuilder/blob/9b6e3b01066967b94346aa66db0cd4b75dc78d05/.github/workflows/pr-check.yml) |

<a id="n2-2026-11-24"></a>

## Nâng trần đợt hai — 23/11/2026

Hồ sơ lập trong đợt nâng trần thứ hai: đọc mã hoặc tài liệu tại commit cố định, chưa chạy upstream; mô tả của trinh sát sai ở nhiều repo nên điều ghi ở đây là điều đã đọc.

<a id="n2-speakeasy-api-openapi"></a>

### Speakeasy OpenAPI (Go)

| Thuộc tính | Giá trị |
|---|---|
| Repo | https://github.com/speakeasy-api/openapi |
| License | MIT |
| Phiên bản đã đọc | `c9d1c24238dc7dbff4bd3a7d25955e096ea3382c` (commit 2026-11-19) |
| Kiểm chứng | 2026-11-24; code-read; đã đọc arazzo/arazzo.go, arazzo/linter/rules/dependency_cycle.go, arazzo/linter/README.md, workflow ci.yaml; chưa chạy upstream |
| Khoảng trống lấp | Đặc tả workflow API (Arazzo) và công cụ: bộ phân tích, kiểm hợp lệ và lint Arazzo 1.0/1.1 bằng Go |
| Cơ chế đáng học | • `arazzo.Validate` (arazzo/arazzo.go) kiểm phiên bản được hỗ trợ, tên sourceDescription và workflowId không trùng, `$self` hợp lệ, rồi `validateReferences` trả danh sách lỗi có vị trí trong cây YAML.<br>• Linter Arazzo tách luật ngữ nghĩa khỏi kiểm schema: ví dụ `semantic-dependency-cycle` (dependency_cycle.go) dựng đồ thị dependsOn của workflow và step rồi báo chu trình; còn có luật bước không chạy tới, output/input không dùng, retry-after, nguồn không HTTPS.<br>• CLI `openapi arazzo` có validate, lint (kèm `--fix` và `--dry-run`), graph (xuất Mermaid hoặc DOT), bootstrap từ OpenAPI và upgrade lên 1.1; cùng engine linter dùng cho OpenAPI, Overlay, AsyncAPI. |
| Tiêu chí và cách kiểm | Luật lint có mức nghiêm trọng mặc định (chu trình dependsOn là error) và cấu hình ruleset; CI chạy fmt-check, mod-check, lint, kiểm ví dụ cập nhật, rồi test có cờ race trên ubuntu và windows kèm coverage. Kiểm bằng máy, nhưng chỉ kiểm tài liệu, không gọi API thật. |
| Giới hạn và rủi ro | Không có bộ thực thi: đây là thư viện phân tích và kiểm, không chạy workflow (trinh sát ghi chung chung là bộ công cụ có validate, đúng nhưng không nên hiểu là engine). MIT, không thấy telemetry trong CLI (tìm theo từ khóa, chưa quét toàn bộ). Do Speakeasy duy trì và dùng cho sản phẩm SDK của họ nên lộ trình có thể theo nhu cầu thương mại; số sao 279 do trinh sát ghi (chưa xác minh). |
| So với | arazzo-specification (đặc tả gốc), jentic-arazzo-engine (bộ chạy), open-workflow-specification, spectral (lint OpenAPI), openapitools-openapi-generator |
| Nguồn | [LICENSE](https://github.com/speakeasy-api/openapi/blob/c9d1c24238dc7dbff4bd3a7d25955e096ea3382c/LICENSE) · [README.md](https://github.com/speakeasy-api/openapi/blob/c9d1c24238dc7dbff4bd3a7d25955e096ea3382c/README.md) · [arazzo.go](https://github.com/speakeasy-api/openapi/blob/c9d1c24238dc7dbff4bd3a7d25955e096ea3382c/arazzo/arazzo.go) · [dependency_cycle.go](https://github.com/speakeasy-api/openapi/blob/c9d1c24238dc7dbff4bd3a7d25955e096ea3382c/arazzo/linter/rules/dependency_cycle.go) · [README.md](https://github.com/speakeasy-api/openapi/blob/c9d1c24238dc7dbff4bd3a7d25955e096ea3382c/arazzo/linter/README.md) · [ci.yaml](https://github.com/speakeasy-api/openapi/blob/c9d1c24238dc7dbff4bd3a7d25955e096ea3382c/.github/workflows/ci.yaml) |

<a id="n2-jentic-arazzo-engine"></a>

### Jentic Arazzo Engine

| Thuộc tính | Giá trị |
|---|---|
| Repo | https://github.com/jentic/arazzo-engine |
| License | Apache-2.0 |
| Phiên bản đã đọc | `ba7f19e5d40693a433f48df41a914789584ec293` (commit 2026-06-12) |
| Kiểm chứng | 2026-11-24; code-read; đã đọc runner/README.md, runner/arazzo_runner/executor/action_handler.py, runner.py, success_criteria.py, generator/arazzo_validator.py, workflow arazzo-engine.yml; chưa chạy upstream |
| Khoảng trống lấp | Đặc tả workflow API (Arazzo): bộ chạy workflow và bộ sinh workflow từ OpenAPI |
| Cơ chế đáng học | • Runner (runner/arazzo_runner) thực thi workflow Arazzo: `ArazzoRunner.execute_workflow`, ánh xạ biến môi trường cho xác thực API key, OAuth2 client-credentials/password, HTTP basic/bearer; một số luồng (authorization code, OpenID) ghi rõ chưa hỗ trợ.<br>• `SuccessCriteriaChecker` (executor/success_criteria.py): không khai successCriteria thì mặc định mã 2xx; `ActionHandler` chọn hành động goto, end, retry theo onSuccess/onFailure.<br>• Generator dùng LLM qua litellm để đề xuất chuỗi gọi từ OpenAPI rồi kiểm bằng schema Arazzo 1.0.1 đóng gói sẵn (arazzo_validator.py). |
| Tiêu chí và cách kiểm | Runner có bộ test pytest lớn (thư mục tests với fixture, mock HTTP) và CI chia theo runner/generator, Python 3.11 đến 3.13, kèm phân tích tĩnh. Generator chỉ kiểm bằng schema, không chạy thử workflow sinh ra. |
| Giới hạn và rủi ro | Runner ghi Beta. Điểm lệch tuyên bố: trong runner chỉ thấy `retryLimit` được đọc rồi trả về trong kết quả (action_handler.py), còn runner.py chỉ chuyển `retry_after` và đặt bước về PENDING, tìm toàn runner không thấy chỗ đếm số lần hay ngủ chờ (có thể do lớp gọi ngoài chịu trách nhiệm, chưa xác minh). Generator gửi mô tả OpenAPI tới nhà cung cấp LLM do người dùng chọn. Push cuối 2026-06-12, cũ hơn các repo cùng lô; Apache-2.0 cho cả runner và generator. |
| So với | arazzo-specification, speakeasy-api-openapi (chỉ kiểm, không chạy), kestra, windmill |
| Nguồn | [LICENSE](https://github.com/jentic/arazzo-engine/blob/ba7f19e5d40693a433f48df41a914789584ec293/LICENSE) · [README.md](https://github.com/jentic/arazzo-engine/blob/ba7f19e5d40693a433f48df41a914789584ec293/README.md) · [README.md](https://github.com/jentic/arazzo-engine/blob/ba7f19e5d40693a433f48df41a914789584ec293/runner/README.md) · [pyproject.toml](https://github.com/jentic/arazzo-engine/blob/ba7f19e5d40693a433f48df41a914789584ec293/runner/pyproject.toml) · [action_handler.py](https://github.com/jentic/arazzo-engine/blob/ba7f19e5d40693a433f48df41a914789584ec293/runner/arazzo_runner/executor/action_handler.py) · [runner.py](https://github.com/jentic/arazzo-engine/blob/ba7f19e5d40693a433f48df41a914789584ec293/runner/arazzo_runner/runner.py) · [pyproject.toml](https://github.com/jentic/arazzo-engine/blob/ba7f19e5d40693a433f48df41a914789584ec293/generator/pyproject.toml) · [arazzo_validator.py](https://github.com/jentic/arazzo-engine/blob/ba7f19e5d40693a433f48df41a914789584ec293/generator/arazzo_generator/validator/arazzo_validator.py) · [arazzo-engine.yml](https://github.com/jentic/arazzo-engine/blob/ba7f19e5d40693a433f48df41a914789584ec293/.github/workflows/arazzo-engine.yml) |
