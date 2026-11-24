# 06 · UI/UX, Design Tools & Design-for-AI

> Thư viện component, công cụ thiết kế mở, công cụ AI sinh giao diện, tài nguyên học UI/UX, và lớp "giao diện cho agent".

## 1. Thư viện component & design system (web)

| Thư viện | Repo | ★ · license (31/10/2026) | Commit cuối | Kiểu | Nhận xét |
|---|---|---|---|---|---|
| **shadcn/ui** | shadcn-ui/ui | ~127k · MIT | 31/10/2026 | Copy-paste source (CLI) trên Tailwind | Mặc định cho React+Tailwind; từ 7/2026 cài mới dùng **Base UI**, vẫn hỗ trợ Radix; 27 layout block (§7h) |
| **MUI** | mui/material-ui | ~99k · MIT | 31/10/2026 | Material Design, đầy đủ | An toàn cho enterprise |
| **Radix UI** | radix-ui/primitives | ~19k · MIT | 14/10/2026 | Headless primitives | Chậm lại sau khi WorkOS mua. Trước ghi "19–35k (nguồn lệch)"; shields đọc thẳng từ GitHub ra 19k |
| **Base UI** | mui/base-ui | ~11k · MIT | 30/10/2026 | Headless, từ team Radix + MUI + Floating UI | Lựa chọn khi bắt đầu mới |
| **Mantine** | mantinedev/mantine | ~32k · MIT | 29/10/2026 | "Batteries included", 100+ component | |
| **Vuetify** | vuetifyjs/vuetify | ~41k · MIT | 31/10/2026 | Material 3 cho Vue | `LICENSE.md` ở gốc là symlink tới `packages/vuetify/LICENSE.md` (MIT), nên GitHub không nhận diện được |
| **Headless UI** | tailwindlabs/headlessui | ~29k · MIT | **13/4/2026** | Headless, Tailwind-native | Hơn 6 tháng không commit (release cuối v2.2.10 ngày 7/4/2026); Tailwind Labs về Shopify 9/2026 (§7h) |
| **daisyUI** | saadeghi/daisyui | ~43k · MIT | 13/10/2026 | Plugin component Tailwind | Template đầy đủ bán riêng (§7h) |
| **Storybook** | storybookjs/storybook | ~91k · MIT | 30/10/2026 | Phát triển/test/doc component cô lập | Chuẩn de-facto |

**Design system tham khảo (doanh nghiệp):** Atlassian, GitHub Primer, GitLab Pajamas, Google Material, IBM Carbon, Shopify Polaris (**Polaris React đã bị archive 11/8/2026, đổi tên `Shopify/polaris-react-archive`; Shopify chuyển sang Polaris Web Components từ 1/10/2025**) (bảng so sánh có cột "AI-ready", MCP, `llms.txt`: §7f.3) — xem `klaufel/awesome-design-systems`, designsystemsrepo.com, designsystems.surf.

## 2. Công cụ thiết kế / canvas mã nguồn mở

| Dự án | Repo | License | ★ (31/10/2026) | Commit cuối | Định vị |
|---|---|---|---|---|---|
| **Excalidraw** | excalidraw/excalidraw | MIT | ~135k | 31/10/2026 | Whiteboard phong cách vẽ tay, self-host |
| **Penpot** | penpot/penpot | MPL-2.0 | ~62k | 30/10/2026 | **Thay thế Figma** mã mở, xuất CSS/HTML thật, Docker self-host |
| **tldraw** | tldraw/tldraw | tldraw license (riêng, cần license thương mại tùy trường hợp) | ~51k | 30/10/2026 | Infinite canvas SDK, gần Figma nhất về cảm giác |
| **Onlook** | onlook-dev/onlook | Apache-2.0 | ~27k | **21/7/2026** | Visual editor cho React/Tailwind, "Cursor cho designer"; hơn 3 tháng không commit trên nhánh chính (commit cuối là bản vá IDOR tRPC), dù vẫn có push ở nhánh khác |
| **OpenDesign** | nexu-io/open-design (open-design.ai) | Apache-2.0 | ~105k | 30/10/2026 | "Collaborative AI design agent workspace"; có dịch vụ trả phí. Hồ sơ §7k, **đọc mã §7q.0: telemetry nội dung bật mặc định, agent chạy bỏ kiểm quyền** |
| **FigCraft** | storytold/figcraft | MIT OR Apache-2.0 | ~4k | 31/10/2026 | Dựng lại Figma bằng Rust nhờ agent, alpha, điều khiển được qua CLI/MCP (§7e) |

## 3. AI sinh giao diện (design-to-code / prompt-to-UI)

| Công cụ | Mở? | ★ (31/10/2026) | Ghi chú |
|---|---|---|---|
| **v0.app** (Vercel) | Đóng | – | Rebrand 1/2026, full-stack sandbox, Git, DB connectors; mạnh nhất ở scaffolding frontend |
| **Lovable** | Đóng | – | Prompt → app full-stack (Supabase) |
| **Bolt.new** (StackBlitz) | Core `bolt.diy` mở (MIT) | `stackblitz-labs/bolt.diy` ~20k (shields), commit cuối 10/2026 | WebContainer trong trình duyệt |
| **Google Stitch** | Đóng | – | Sinh UI + màu/typography/spacing tái dùng |
| **MagicPath** | Đóng | – | Layout + hướng thiết kế trên infinite canvas |
| **Subframe** | Đóng | – | Canvas compose React/Tailwind, export code sạch |
| **Figma Make / AI** | Đóng | – | Tích hợp trong Figma |

Danh sách: `narrowin/awesome-generative-ui` (LLM sinh/compose UI động; 144★, CC-BY-4.0, push cuối 26/10/2026), `maxbogo/awesome-ai-tools-for-ui` (1.002★, không ghi license). Số đọc 31/10/2026 (GitHub API).

## 4. "Taste" cho coding agent – chống giao diện AI generic

- **Taste Skill** (`Leonxlnx/taste-skill`, **~98,9k★**, 6,7k fork, MIT, commit cuối 19/10/2026; trước ghi ~46k★ theo listing): mô tả GitHub hiện nay là "art direction, reference images and a browser check", tức đã thêm bước kiểm trên trình duyệt **(chưa đọc mã, chưa xác minh)**; bộ Agent Skills cho Claude Code/Cursor/Codex; cấm các trope "AI slop": purple mesh gradient, hero căn giữa, 3 card giống nhau, font Inter + ảnh stock; 3 "dial" variance/motion/density; v2 đọc brief (loại trang, đối tượng, vibe) trước khi code.
- **Refactoring UI Skill** (`s0xDk/refactoring-ui-skill`, 646★, MIT): áp quy tắc spacing/typography/color/hierarchy từ sách Refactoring UI, kèm `tokens.css` đã kiểm tương phản. Hồ sơ: §7g.4.
- **Frontend-design skill** của Anthropic (trong marketplace Claude Code, Apache-2.0) + Taste làm lớp "quality enforcement". Hồ sơ: §7g.3.
- Chưa có benchmark độc lập chứng minh hiệu quả; bằng chứng chủ yếu là demo & cộng đồng.
- **Thêm từ repo của chủ kho (mục 23, 2026-10-12):** `impeccable` (~83k★ ngày 19/10/2026, hồ sơ mục 20; plugin/skill "taste" được case-study-ft41 ghi trong `ui-ux-intelligence-provider.md`), `nextlevelbuilder/ui-ux-pro-max-skill` (~137k★; 45 file, vendor trong Hermes-Agents; hồ sơ §7g.2), `google-labs-code/design.md` (~28k★, Apache-2.0; file DESIGN.md mô tả hệ thiết kế cho agent; spec + linter, xem §7c), `popular-web-designs` (54 design system tóm tắt). xboss có cổng tĩnh `check:contrast` + `check:ui-ux-guard` và Lighthouse CI chặn merge 4 category — "taste" chỉ bền khi có cổng máy đi kèm.

## 5. Tài nguyên học UI/UX cho developer

| Tài nguyên | Loại | ★ · license (19/10/2026) | Ghi chú |
|---|---|---|---|
| **Refactoring UI** (Wathan & Schoger) | Sách + video (trả phí) | – | Kinh điển cho dev không phải designer; skill dựa trên sách: §7g.4 |
| **Laws of UX** (Jon Yablonski) | Web miễn phí + sách | – | Nguyên lý tâm lý học (Fitts, Hick, Jakob…) |
| `bradtraversy/design-resources-for-developers` | Awesome list | ~67k · MIT, commit cuối 18/10/2026 | Ảnh, font, màu, template, CSS framework |
| `klaufel/awesome-design-systems` | Awesome list | 907 · CC0-1.0, commit cuối 14/9/2026 | Design system hướng dev |
| Design Systems Gallery / designsystems.surf | Thư viện ví dụ | – | Cảm hứng & chuẩn |
| Material Design 3, Apple HIG, Fluent 2 | Guideline chính thức | – | Layout thích ứng: §7h |

## 6. Lớp giao diện cho agent (Agentic UI / Generative UI)

| Dự án | Repo | ★ · license (31/10/2026) | Commit cuối | Vai trò | Ghi chú |
|---|---|---|---|---|---|
| **CopilotKit** | CopilotKit/CopilotKit | ~38k · MIT | 30/10/2026 | Frontend stack cho agent, tác giả **AG-UI** | Gọi vốn $27M 5/2026; nặng & opinionated, như application framework |
| **assistant-ui** | assistant-ui/assistant-ui | ~13k · MIT | 30/10/2026 | Headless React primitives cho chat/agent | Ghép tốt với Vercel AI SDK |
| **Vercel AI SDK** + **AI Elements** | vercel/ai | ~28k · Apache-2.0 | 30/10/2026 | Toolkit streaming, framework-agnostic; AI Elements = component lắp ráp | Gần tầng transport |
| **AG-UI** | ag-ui-protocol/ag-ui | ~17k · MIT | 30/10/2026 | Giao thức sự kiện agent ↔ UI | AWS AgentCore, MS Agent Framework, Oracle A2UI tích hợp |

**Nhận định:** năm 2026 lựa chọn quyết định bởi giao thức (AG-UI) hơn là bộ component.

> **Cách lấy số §1–§6 (rà lại 31/10/2026; lần trước 19/10/2026):** số sao và license từ GitHub search API (`repo:` từng dự án, làm tròn); `bolt.diy` không hiện trong search (là fork) nên lấy shields. **Ngày commit cuối đọc từ `git clone --depth 1` nhánh mặc định**, không dùng `pushed_at` của API vì trường này đổi cả khi push nhánh khác (Onlook: push 21/10 nhưng commit nhánh chính cuối 21/7). Khi GitHub báo license `NOASSERTION` thì giữ license đã đọc trong file LICENSE (Vuetify, tldraw, Vercel AI). Bảng rà toàn bộ 72 repo GitHub của mục: §7p.1.

## 7. Case study: Anatomy – skill vẽ minh họa isometric tương tác (link từ người dùng, 2026-10-12)

| Thuộc tính | Giá trị (đọc 2026-10-12) |
|---|---|
| Repo | https://github.com/wheresryan22/anatomy · release v1.0.0 ngày **10/10/2026** · kèm `wheresryan22/anatomy-figures` (npm `anatomy-figures`, 51–52 máy đã vẽ, 5 theme, React + custom elements, 10★) |
| Mô tả | "An agent skill for creating detailed, interactive isometric illustrations of real-world machines and complex systems… A Claude skill that explains an idea by building it as a real, working object." |
| ★ / forks / commit | **3.8k ★ sau ~2 ngày** · 299 forks · 87 commit · 1 issue · 3 PR mở; 35 commit trong 11–12/10 (gộp PR #20–#39), contributor thứ hai `rudycelekli` (10 fix audit/React/browser) |
| License | MIT ("© 2026 Ryan") |
| Tác giả | Ryan (@wheresryan22, "self-proclaimed misfit"), thành viên org FrameHeadquarters, 106 followers; repo khác: sfinterface-numbers (107★), xq (C, archived) |
| Tương thích | Claude Code, OpenCode, Codex (`$anatomy`); Node 20.10+ (skills CLI cần Node 22), Chrome/Chromium cho bước kiểm tra; **không API key, không `npm install`** |
| Cài | `npx skills add wheresryan22/anatomy -g -a claude-code` → `/anatomy explain how a token bucket rate limiter works, interactive` |

### Cách hoạt động (từ `SKILL.md`)

- **Ý tưởng cốt lõi:** biến khái niệm kỹ thuật thành **một vật thể vật lý thật** mà cơ chế vận hành chính là khái niệm (cache key → ổ khóa pin-tumbler chỉ xoay khi mọi pin khớp; rate limiter → bồn token). Từ chối "hộp xếp chồng trừu tượng". Mọi số trên readout đến từ **cùng một model nhỏ** điều khiển chuyển động.
- **Quy trình 10 bước:** (1) **Size it** – Figure 40–80 part (~30–90 phút), Hero 80–150 part (~2–4 giờ), Epic 6+ giờ; không tự chạy Epic nếu người dùng chưa chọn → (2) **Truth first**: thu thập số liệu/hành vi thật, đặt vào module thuần → (3) Invent the object, một câu "cái gì chuyển động và nghĩa là gì" → (4) Parts list ≥40 part (base, structure, mechanism, controls, lit subject) → (5) camera azimuth 45°/elevation 30°, `fitProjection` → (6) build geometry một lần → (7) **paint back to front** → (8) frame trong card (số hình, tiêu đề, hint, live readout) → (9) motion theo thời gian, tôn trọng reduced-motion, dừng khi offscreen → (10) **verify like a critic**: đọc từng PNG ở zoom 4×.
- **Luật cứng đáng chép lại:** *"Solids, not wireframes."* · *"Every line ends on something: a face, another line or a terminal dot."* · không ống/cáp nào xuyên qua vật khác kể cả giữa chuyển động · *"Shaders never pop or cut off."* · hình chiếm 55–65% card và vẫn đọc được ở 390px.
- **Kit (không phụ thuộc ngoài Node):** `kit/iso-kit.ts` (camera, solids, parts library, SVG renderer), `lathe.mjs` (vật tròn), `tube.mjs` (ống/cáp), `audit.mjs` (chứng minh hình học), `gl.mjs` (WebGL: lửa, nước, plasma), `turn*.mjs` (3D beta), `kit/react/draw.tsx` (server-safe) + `live.tsx`; `references/` 8 guide (craft, kit, motion, react, verify, webgl, walkthrough, 3d) nạp khi cần.
- **Kiểm chứng bằng máy:** `scripts/capture.mjs` (screenshot headless Chrome), `drive.mjs` (chuỗi tương tác), `node build.mjs --audit` phải in "audit passed" khi có ống/vật tròn, `scripts/lines.mjs` phải báo **0 line end**; check 4× ở cả theme sáng/tối; `evals/evals.json` chứa prompt test.
- **Output:** HTML standalone (`pageHtml`), SVG đơn (`figureSvg`), hoặc component React/Next.js; 8 ví dụ (dial-indicator, desk-computer, arcade-cabinet, raptor-engine, ripple-tank, test-rig, spot-plate, turning-dial 3D).
- **Giới hạn tác giả nêu:** không phải chart library; vẽ máy/dụng cụ/đồ nội thất, không vẽ người hay bản đồ chính xác; build chậm có chủ đích; shader cần WebGL; 3D là beta; Codex sandbox có thể chặn browser check (README có hướng dẫn).

### Bối cảnh & so sánh

| Nhóm | Ví dụ | Khác biệt với Anatomy |
|---|---|---|
| Skill sơ đồ "diagram-as-code" | Mermaid skills (design-doc-mermaid ~44k install), Excalidraw skills (~28.7k install, Kroki/CLI export), Garry Tan `diagram` (Mermaid → Excalidraw editable), `diagram-design` (44 loại, branded; xem §7b) | Sơ đồ 2D trừu tượng; Anatomy là **minh họa vật thể 3D-isometric có mô phỏng** |
| Skill thẩm mỹ frontend | Taste Skill (mục 4 ở trên), Refactoring UI skill, `ibelick/ui-skills` (~9.4k★, directory chứa Anatomy cùng animated-sprites, animation-vocabulary, antfu-design, beautiful-shadows) | Anatomy nằm ở nhánh "visual/craft" của cùng hệ sinh thái |
| Motion/video skills | claude-motion-design, awesome-claude-video-skills (mục 19) | Video/animation thay vì SVG tương tác |

### Nhận xét & bài học

1. **Skill kèm kit + audit + eval** là mẫu đáng học: thay vì chỉ prompt, skill mang theo thư viện hình học không phụ thuộc, script kiểm chứng bằng máy (audit hình học, đếm line end, screenshot 4×) và bộ prompt eval. Đây là "evidence or it's a FAIL" (mục 09) áp vào đồ họa.
2. **Sizing trước khi làm** (Figure/Hero/Epic + ước tính thời gian, hỏi người dùng) là cách kiểm soát chi phí token/thời gian rõ ràng, giống gate `[BLOCKER]`/approval ở mục 09 và 19.
3. **"Truth first"**: readout và chuyển động lấy từ một model số nhỏ → tránh minh họa "đẹp nhưng sai"; tái dùng cho dataviz và explainer.
4. **Rủi ro:** dự án 2 ngày tuổi, 1 contributor chính; build 30 phút–6 giờ mỗi hình rất tốn token; phụ thuộc Chrome headless; chưa có đánh giá độc lập (bài ai.sulat.com không truy cập được, 403). Số sao tăng nhanh nhờ bài đăng X ngày 10/10 và lan sang Weibo.
5. Liên hệ: mục 04 (chuẩn Agent Skills, cài qua `skills` CLI), mục 06 §4 (Taste Skill), mục 19 (motion skills), mục 09 (kiểm chứng bằng máy).

**Nguồn:** https://github.com/wheresryan22/anatomy (README, SKILL.md, releases/v1.0.0, commits) · https://github.com/wheresryan22 · https://github.com/wheresryan22/anatomy-figures · https://x.com/wheresryan22/status/2108948624004526516 · https://www.ui-skills.com/skills/wheresryan22/anatomy · https://www.skills.sh/wheresryan22/anatomy/anatomy · https://skillselion.com/guides/best-diagram-skills-for-claude-code · https://aipptskill.com/blog/ai-diagram-skills-guide/ · https://open-design.ai/skills/diagram/ · https://skillselion.com/guides/diagram-design-skill-claude-code-guide

## 7b. Case study: diagram-design — skill vẽ sơ đồ "editorial" theo thương hiệu (ảnh + link người dùng gửi, 2026-10-12)

> Đọc clone đầy đủ (287 commit, HEAD `80c8f28`, plugin 2.6.75) và đối chiếu các con số trong ảnh chụp README.

### 7b.1 Hồ sơ nhanh

| Mục | Thông tin (12/10/2026) |
|---|---|
| Repo | `cathrynlavery/diagram-design` · **~51,8k★**, 3,3k fork, 87 issue + PR mở; tạo 16/4/2026; license **MIT**; trang diagramdesign.dev |
| Mô tả | "An agent skill that draws diagrams as one self-contained HTML + SVG file, in your brand. 44 diagram types. No shadows. No Mermaid slop." |
| Tác giả | Cathryn Lavery (LittleMight; email commit `@bestself.co`, tức BestSelf Co.); tác giả chính 122/287 commit (hai email), bot release 63, tổng 51 tên tác giả. 78/250 commit không merge (~31%) có trailer Claude |
| Host | Claude Code (marketplace `/plugin`), Codex, GitHub Copilot, Factory Droid, Claude Cowork (mirror nội bộ tổ chức), OpenCode, Pi; hoặc `npx skills add cathrynlavery/diagram-design` (chỉ skill, không có lệnh `/export-diagram`, `/import-mermaid`, `/profile`, `/doctor`) |

**Đối chiếu ảnh:** "44 diagram types" **đúng** (44 file `references/type-*.md`); "stars 49k" là số cũ, nay ~51,8k; "version 2.6.74" đã lên 2.6.75 cùng ngày (bot bump mỗi lần merge vào `main`); "Skills 9.3K" là số lượt cài theo skills.sh **(chưa xác minh)**; "CI passing" đúng nghĩa: `ci.yml` chạy trên mọi PR. "#1 Repository Of The Day" là huy hiệu GitHub Trending, không kiểm được ngày.

### 7b.2 Cách hoạt động (đọc `SKILL.md`, 393 dòng, và `references/`)

- **Cổng thương hiệu trước sơ đồ đầu tiên:** nếu token style vẫn mặc định (paper `#f5f5f5`, ink `#2d3142`, accent `#bf4520`), skill **dừng và hỏi** lấy brand từ đâu (URL website, skill có sẵn, thư mục design system, dán token, giữ mặc định, profile đã lưu). Profile lưu ở `~/.diagram-design/profiles/`.
- **Triết lý "xoá trước":** mật độ mục tiêu 4/10, trên 9 node thì tách thành hai sơ đồ, màu nhấn chỉ cho 1–2 node; mục "khi nào **không** dùng" (danh sách → bảng, sơ đồ một hình → viết câu).
- **Output:** một file HTML tự chứa với SVG inline; xuất PNG (cần Playwright trong Python, skill kiểm trước khi chạy) và SVG đứng riêng. Nhập từ `.drawio`, Mermaid, `.excalidraw`.
- **Kiểm bằng máy:** `scripts/` có 30 `verify-*.py` và 39 `test-*.py` (hình học, tương phản màu, a11y, sankey, treemap, waterfall…), fixture "đối nghịch" (`sample-adversarial.mmd`, `waterfall-plausible-wrong.html`); `.maintainer-policy.json` liệt kê cổng local, gồm `claude plugin validate . --strict` ghim phiên bản CLI.
- **Riêng tư:** `PRIVACY.md` nói không server, không analytics, không telemetry; luồng ra ngoài duy nhất là Google Fonts khi mở file (bỏ link thì dùng font hệ thống) và trang web người dùng chỉ định khi lấy brand.

### 7b.3 Đánh giá

- **Điểm mạnh:** đúng mẫu "skill kèm kit + verifier + fixture đối nghịch" như Anatomy (§7), nhưng phạm vi rộng hơn (44 loại, chart lẫn schematic) và đóng gói cho 6+ host với version đồng bộ; luật thẩm mỹ cụ thể đến mức kiểm được.
- **Rủi ro:** (1) phụ thuộc Google Fonts khi xem file (tài liệu nội bộ nhạy cảm nên bỏ link font); (2) PNG cần Playwright + Chromium; (3) bản `npx skills` không tự cập nhật; (4) skill dài (393 dòng + hàng chục reference) nên tốn context mỗi lần nạp, dù reference chỉ nạp khi cần; (5) chưa thấy đánh giá độc lập về chất lượng sơ đồ so với Mermaid.
- **Khi nào dùng:** sơ đồ cho tài liệu đọc lâu, slide, bài viết, cần đúng brand. Với sơ đồ sống trong repo (review được bằng diff, render trên GitHub), Mermaid vẫn tiện hơn.
- **Tích hợp:** MIT, chép/vendor được; giữ `THIRD_PARTY_LICENSES.md` (icon Tabler, MIT). Cấu hình tối thiểu: chạy onboarding một lần cho mỗi dự án, lưu profile; tắt Google Fonts cho tài liệu nội bộ.

**Nguồn §7b:** https://github.com/cathrynlavery/diagram-design (clone đầy đủ, HEAD 80c8f28; README, SKILL.md, references/type-*.md, references/export.md, scripts/, .maintainer-policy.json, .github/workflows/ci.yml, PRIVACY.md, THIRD_PARTY_LICENSES.md) · https://diagramdesign.dev · https://skillselion.com/guides/diagram-design-skill-claude-code-guide

## 7c. Kiểm ảnh: VoltAgent/official-design-md, danh mục DESIGN.md "chính chủ" (ảnh người dùng gửi, 2026-10-13)

> Ảnh là phần đầu README (banner "Official DESIGN.md Collection", huy hiệu "DESIGN.md 7", Discord "138 online"). Đã clone toàn bộ repo (6 commit), tải đủ 11 file được liệt kê, và chạy linter chính thức của Google (`npx @google/design.md@0.4.0 lint`) trên từng file.

### 7c.1 Hồ sơ nhanh

| Mục | Thông tin (đọc 13/10/2026) |
|---|---|
| Repo | `VoltAgent/official-design-md` · ~519★, 47 fork (shields), license **MIT** · chỉ có `README.md` + `LICENSE` |
| Lịch sử | 6 commit, cùng một người (necatiozmen / Necati Özmen): tạo 26/7/2026 với 7 mục → 8 mục ngày 29/8 (thêm Ant Design) → 11 mục ngày 14/9 (Oxide, Juspay, Microsoft FAST); commit cuối 21/9/2026 |
| Mô tả | "The tracker for first-party DESIGN.md adoption… not extracted, not reverse-engineered, not community-made." |
| Chủ list | VoltAgent (framework agent TypeScript). Cùng chủ: `awesome-design-md` (~121k★, 84 DESIGN.md **trích xuất** từ website), `official-mcp-servers` (mục 04 §2c), `awesome-agent-skills`, `awesome-claude-code-subagents` |
| Chuẩn gốc | DESIGN.md do Google Stitch công bố; Google mở bản nháp đặc tả ngày 21/4/2026 tại `google-labs-code/design.md` (~28k★, Apache-2.0, bản 0.4.0 ngày 27/7/2026, trạng thái alpha): YAML front matter chứa token + phần văn xuôi giải thích, kèm CLI `lint`/`diff`/`export` |
| Mô hình kinh doanh | README chèn quảng cáo EveryFeed và hai bộ starter kit trên getdesign.md. Trang getdesign.md/request bán **DESIGN.md riêng** $39 và "Website Starter Kit + DESIGN.md" $249, đều trả một lần (đọc 13/10/2026) |

### 7c.2 Kiểm từng ô trong ảnh

| Ô trong ảnh | Kiểm | Ghi chú |
|---|---|---|
| Tab "MIT license" | ✅ | `LICENSE`: MIT, © 2026 VoltAgent. Chỉ áp cho README; mỗi file được liệt kê thuộc chủ của nó (README tự ghi) |
| Huy hiệu "DESIGN.md 7" | ⚠️ cũ | Ảnh chụp trong khoảng 26/7–29/8/2026; nay huy hiệu ghi **11**, khớp đúng 11 dòng trong mục Collection |
| "138 online" (Discord) | ⚠️ | Huy hiệu sống, đổi theo giờ; không nói gì về chất lượng list |
| "published by companies and projects themselves" | ⚠️ 10/11 | 10/11 file nằm trên domain hoặc repo của chính chủ. Mục **VoltAgent** thì không đúng tinh thần: file trong `VoltAgent/voltagent` (thêm 11/5/2026) tự mô tả là *"Voltagent Inspired… An inspired interpretation of Voltagent's design language"*, giống **88%** theo dòng (difflib) với bản trích xuất `design-md/voltagent/DESIGN.md` mà `awesome-design-md` đăng từ 31/3/2026. Tức là bản trích xuất được đăng lại vào repo chính chủ, cùng một tác giả |
| "not extracted, not reverse-engineered" | ⚠️ | Đúng cho 10 file còn lại theo nội dung đọc được; đúng một ngoại lệ là chính mục của chủ list (ô trên) |
| "If a team ships an official DESIGN.md… it belongs here" | ⚠️ | Không có kiểm tra tự động (không CI, không script). Thêm mục qua issue rồi PR, người duyệt là chủ repo. 11/11 link còn sống (HTTP 200, 13/10/2026) |

**Tổng:** 1✅ / 5⚠️ / 0❌. Không ô nào sai hẳn, nhưng "chính chủ" mới đúng ở mức *đăng trên domain của mình*, chưa phải *chính chủ viết*, và list không kiểm file có đúng spec hay không.

### 7c.3 Linter chính thức chấm 11 file (0.4.0, chạy 13/10/2026)

| File | YAML token? | Lỗi | Cảnh báo | Nhận xét |
|---|---|---|---|---|
| Vercel | có | 0 | 0 | File duy nhất sạch hoàn toàn |
| Ant Design | có | 0 | 19 | 17 token mồ côi; nút chính chữ trắng trên `#1677ff` chỉ đạt 4,10:1 (dưới AA 4,5:1) |
| Mintlify | có | 0 | 43 | Typography viết dạng mảng, linter không nhận; thiếu màu `primary` |
| VoltAgent | có | 0 | 30 | 26 tham chiếu token không trỏ tới đâu |
| Atlassian | có | **29** | 446 | 1.738 dòng; đơn vị `%` không hợp lệ, 203 tham chiếu gãy. Một phần cảnh báo tương phản là dương tính giả (linter tính trên nền trong suốt `#00000000`) |
| Oxide | trong khối code | 0 | 162 | 37 tham chiếu gãy, typography dạng mảng |
| Clerk, Juspay, Microsoft FAST, Nuxt, Resend | **không** | 0 | 1 | "No YAML content found": văn xuôi thuần, linter không có gì để kiểm |

**Đọc bảng:** 6/11 file có token máy đọc được; chỉ 1/11 qua linter sạch. Câu README *"No Figma exports, no JSON schemas, no special tooling… nothing to parse"* lệch với chính spec của Google, vốn đặt token trong YAML và có CLI kiểm. Với agent, file văn xuôi vẫn dùng được làm ngữ cảnh, nhưng không kiểm được tương phản hay tham chiếu bằng máy.

### 7c.4 Dùng thế nào

- **Làm mẫu tham khảo, không chép nguyên:** README bảo "Copy it into your project root", nhưng đó là **hệ thiết kế của thương hiệu khác** (logo, màu, font có thể có quyền riêng). Hợp lý là đọc cách họ cấu trúc file (Vercel cho bản đúng spec, Microsoft FAST và Oxide cho bản dành cho dev của chính design system), rồi viết DESIGN.md cho brand của mình.
- **Muốn file có giá trị kiểm chứng:** viết theo spec của `google-labs-code/design.md` (YAML token + văn xuôi) và chạy `lint` trong CI, cùng kiểu "taste chỉ bền khi có cổng máy" ở §4 và các case study §7, §7b.
- **Phân biệt hai list cùng chủ:** `official-design-md` (11 file, ý định chính chủ) và `awesome-design-md` (84 file trích xuất từ CSS công khai, README tự ghi "We do not claim ownership"). Bản trích xuất hợp cho thử nghiệm; đưa vào sản phẩm thật thì nên tự viết.

**Nguồn §7c:** https://github.com/VoltAgent/official-design-md (clone đầy đủ, HEAD 7236b05) · https://github.com/VoltAgent/awesome-design-md (clone nông, HEAD c7c1bad 12/10/2026; `design-md/voltagent/DESIGN.md`) · https://github.com/VoltAgent/voltagent (lịch sử `DESIGN.md`: bd74d743, 11/5/2026) · https://github.com/google-labs-code/design.md (README, bản 0.4.0) · https://www.npmjs.com/package/@google/design.md · https://blog.google/innovation-and-ai/models-and-research/google-labs/stitch-design-md/ · https://the-decoder.com/googles-open-source-design-md-gives-ai-agents-a-prompt-ready-blueprint-for-brand-consistent-design/ · https://getdesign.md/request · 11 file: ant.design/design.md · atlassian.design/DESIGN.md · clerk.com/design.md · github.com/juspay/blend-design-system (DESIGN.md) · github.com/microsoft/fast (examples/design-system/DESIGN.md) · mintlify.com/design.md · nuxt.com/design.md · github.com/oxidecomputer/design-system (design.md) · resend.com/design.md · vercel.com/design.md · github.com/VoltAgent/voltagent (DESIGN.md)

## 7d. Kiểm ảnh: plugin87/ux-ui-agent-skills ("XIAS"), bộ skill biến Claude thành "Senior Design Architect" (ảnh + tên repo người dùng gửi, 2026-10-13)

> Ảnh là phần đầu README: tagline "Turn Claude into a Senior Design Architect — 15+ years of expertise…", câu "138 brand-grade design systems… any framework and any design system", logo XIAS với ba số 52 · 25 · 14, huy hiệu Trendshift "#10 Repository Of The Day" và chữ phủ tiếng Việt "1.628 lập trình viên đã star". Đã clone toàn bộ repo (144 commit), đếm từng con số, đối chiếu 138 design system với hai kho MIT khác, và tự chạy bộ cổng của repo.

### 7d.1 Hồ sơ nhanh

| Mục | Thông tin (đọc 13/10/2026) |
|---|---|
| Repo | `plugin87/ux-ui-agent-skills` · **1.686★**, 177 fork, 8 issue mở (GitHub search API) · license **MIT** (© 2026 Thientan Soparat) · bản **v2.9.8** (10/10/2026) |
| Tác giả | Thientan Soparat (`plugin87`), 143/144 commit. Tài khoản có từ 2016; các repo khác của cùng người đều nhỏ: `figma-remote-server` (MCP Figma, 5★), `full-stack-design-skills` (10★), `homebrew-tap` |
| Lịch sử | Tạo 16/3/2026 · v1.0.1 (6/6) đóng gói sẵn skill của **Taste Skill** · v1.1.0 (7/6) thêm 138 design system và gỡ skill Taste · v2.9.x tháng 10 thêm hook, máy chủ MCP, brew. Listing agentskill.work ghi 438★ ở bản 2.3.1 (khoảng 22/6/2026), tức sao tăng gấp 4 trong khoảng 3,5 tháng |
| Phân phối | Plugin Claude Code (`.claude-plugin/`), `npx ux-ui-agent-skills init`, brew, máy chủ MCP (`ux-ui-mcp`). `AGENTS.md` cho Codex/Cursor/Copilot/Aider. npm: 7.178 lượt tải từ 1/6 đến 12/10/2026, 3.540 trong 30 ngày gần nhất |
| Bên trong | `CLAUDE.md` 319 dòng (luật + bộ định tuyến yêu cầu) · 25 skill trong `.claude/skills/` · 14 file token DTCG · 11 file spec component · 16 adapter framework · 39 script cổng (Python + Node + Playwright/axe) · 3 hook (preflight, cổng nhanh khi ghi file, chặn dừng lượt khi chưa đo) |

### 7d.2 Kiểm từng ô trong ảnh

| Ô trong ảnh | Kiểm | Ghi chú |
|---|---|---|
| "15+ years of expertise", "Senior Design Architect" | ⚠️ | Không phải kinh nghiệm của ai: đó là câu persona ở dòng 3 `CLAUDE.md` ("You are a Senior Design Architect with 15+ years… at the caliber of Apple, Google, Airbnb, and Stripe"). Persona không đo được; thứ đo được nằm ở cổng (ô "52") |
| "138 brand-grade design systems" | ⚠️ | Đếm đúng **138** thư mục trong `design-systems/library/`. Nhưng **64** tên trùng `VoltAgent/awesome-design-md` (MIT), trong đó **60** file có ≥ 80% dòng trùng nguyên văn với một bản trong lịch sử kho đó (cùng khung 9 mục "Visual Theme & Atmosphere… Agent Prompt Guide"). **51** tên trùng `bergside/awesome-design-skills` (TypeUI, MIT, ~3,1k★): 49/51 giữ nguyên câu mô tả, màu lấy từ token gốc (vd brutalism `#DD614C`), văn được viết lại theo khung trên và mỏng hơn (trung vị 71 dòng so với 154 của cả thư viện). 24 mục còn lại chưa rõ nguồn (chưa xác minh). Repo **không ghi công hay chép bản quyền** của hai kho MIT này ở đâu cả; MIT yêu cầu giữ thông báo bản quyền khi phân phối lại phần đáng kể |
| "any framework and any design system" | ⚠️ | Có 16 adapter (Angular, Vue, Svelte, Flutter, Jetpack Compose, React Native…) cộng React/Next/SwiftUI, nhưng cổng render chỉ chạy trên HTML và component React. Các framework khác là hướng dẫn dạng văn bản, không cổng nào kiểm |
| Logo "52" (cổng khách quan) | ⚠️ 49/52 | Tự chạy `node scripts/accuracy_report.mjs` trên HEAD 62092bd (13/10/2026, Chromium 1194 thay cho Chrome): **49/52**, README ghi "52/52 or it fails". 3 cổng trượt: (1) hook: 3/19 test fail vì hook không nhận ra trình duyệt trong sandbox, do môi trường; (2) harness component: số "65" màu `rgb(157,150,142)` trên nền trắng chỉ đạt **2,92:1** (cần 3:1), không phụ thuộc font nên khả năng cao là lỗi thật; (3) mẫu checkout: tràn +9px ở 280px và hai nút "Place order"/"Back to delivery" bấm không có phản hồi (chưa xác minh có do font hay không). Mô tả repo trên GitHub còn ghi "**50** objective gates", lệch với README |
| Logo "25" (skill chạy được) | ✅ | Đúng 25 `SKILL.md` trong `.claude/skills/` (ví dụ `/design-screen`, `/critique`, `/a11y-audit`, `/data-dashboard`, `/gate`) |
| Logo "14" (file token DTCG) | ✅ | Đúng 14 file trong `tokens/`; `npm test` (validate token, tương phản, spec component, hardcode, tham chiếu theme, emoji, link) qua hết, `npm run test:unit` 49/49 pass |
| Trendshift "#10 Repository Of The Day" | ✅ | Trang trendshift.io/repositories/24406 ghi "#10 on GitHub Trending". Đây là thứ hạng một ngày, không nói gì về chất lượng |
| "1.628 lập trình viên đã star" (chữ phủ tiếng Việt) | ⚠️ cũ | Hôm nay 1.686★. Chữ do người đăng lại thêm vào, không có trên README; số sao không phải số "lập trình viên" |
| "MIT license" | ✅ | `LICENSE` MIT. Xem lưu ý ghi công ở ô "138" |

**Tổng:** 4✅ / 5⚠️ / 0❌. Phần mã của chính tác giả (cổng đo trên trình duyệt thật, hook chặn "báo xong khi chưa đo") là thật và chạy được. Phần "138 design systems" lại chủ yếu là dữ liệu của hai kho MIT khác, đóng gói lại mà không ghi nguồn.

### 7d.3 So với các mục đã có

| | XIAS | Taste Skill (§4) | `awesome-design-md` (§7c) | `ui-ux-pro-max-skill` |
|---|---|---|---|---|
| Bản chất | Luật + token + cổng đo + thư viện DESIGN.md | Luật "taste" chống AI slop | Kho DESIGN.md trích xuất từ website | Kho tra cứu style/palette cho agent |
| Có cổng máy? | Có: 52 cổng (README ghi 34 cổng mở trình duyệt) (axe, tương phản theo trạng thái, phím, vùng chạm, 280px) | Không | Không (linter của Google là công cụ ngoài) | Không (chưa xác minh) |
| Quan hệ | Từng đóng gói Taste Skill (v1.0.1), lấy 60+ file của awesome-design-md | Nguồn gốc ý "slop tells" | Nguồn của ~60 design system trong XIAS | Cùng ngách |

Điểm XIAS hơn hẳn ba bên kia là **cổng đo trên bản render thật** và hook `Stop` buộc agent nói "UNMEASURED" khi chưa đo, đúng tinh thần "taste chỉ bền khi có cổng máy" ở §4.

### 7d.4 Dùng thế nào

- **Lấy phần cổng, không cần cả bộ:** các script `verify_states.mjs` (tương phản theo hover/focus/disabled), `verify_target_size.mjs`, `verify_overflow.mjs` (280px), `axe_audit.mjs`, `lint_intent.mjs` (nút xóa không được mang màu primary) có thể chạy độc lập trên HTML. Lưu ý chúng gọi `chromium.launch({ channel: 'chrome' })`: máy không có Chrome thì phải cài, hoặc nhiều cổng sẽ fail vì môi trường chứ không phải vì giao diện.
- **Không dồn 319 dòng `CLAUDE.md` vào dự án đã có luật riêng:** bộ luật của XIAS (theme đơn, token theo ý định, không emoji) có thể xung đột với design system sẵn có. `npx ux-ui-agent-skills add <phần>` cho phép lấy từng phần.
- **Thư viện 138 design system:** dùng để tham khảo như §7c. Muốn dùng thương mại thì lấy từ nguồn gốc (`awesome-design-md`, `bergside/awesome-design-skills`) để giữ đúng thông báo MIT, và nhớ đó là hệ thiết kế của thương hiệu khác.
- **Tự chạy lại cổng sau khi cài:** README nói 52/52, nhưng bản HEAD chạy trong sandbox còn trượt ít nhất một cổng tương phản thật.

**Rà lại 18/10/2026 (người dùng gửi lại ảnh "PASSED ALL GATES"):** repo **không đổi** — vẫn HEAD `62092bd`, v2.9.8, 144 commit. Chỉ số sao tăng **1.686 → ~2,0k** (218 fork). Ảnh là reference app `examples/` với nhãn "PASSED ALL GATES" (marketing); nhắc lại §7d.2: README/ảnh tuyên bố 52/52 nhưng tự chạy `accuracy_report.mjs` thật ra 49/52, và "138 design systems" phần lớn chép từ hai kho MIT khác không ghi nguồn. Đánh giá giữ nguyên.

**Nguồn §7d:** https://github.com/plugin87/ux-ui-agent-skills (clone đầy đủ, 144 commit, HEAD 62092bd 10/10/2026; README, CLAUDE.md, CHANGELOG.md, LICENSE, package.json, .claude-plugin/plugin.json, design-systems/library/, `git show b89881e:skills-lock.json`; tự chạy `npm test`, `npm run test:unit` 49/49, `node scripts/accuracy_report.mjs` 49/52, 13/10/2026) · GitHub search API 13/10/2026 (1.686★, 177 fork; repo khác của `plugin87`) · https://www.npmjs.com/package/ux-ui-agent-skills (api.npmjs.org: 3.540 lượt/30 ngày, 7.178 từ 1/6/2026) · https://trendshift.io/repositories/24406 · https://agentskill.work/en/skills/plugin87/ux-ui-agent-skills (438★, bản 2.3.1) · https://github.com/VoltAgent/awesome-design-md (clone, lịch sử `design-md/*/DESIGN.md`) · https://github.com/bergside/awesome-design-skills (clone; MIT © Bergside, `skills/*/SKILL.md`, `skills/*/DESIGN.md`) · https://tessl.io/registry/skills/github/bergside/awesome-design-skills/brutalism/evals · https://open-design.ai/systems/brutalism/ · https://github.com/Leonxlnx/taste-skill

## 7e. Case study: FigCraft (`storytold/figcraft`), dựng lại Figma bằng Rust nhờ agent (link người dùng gửi, 2026-10-14)

> Đã clone toàn bộ repo (267 commit), đọc README, `CLAUDE.md`, `ROADMAP.md`, `docs/gaps.md`, mã nhập `.fig`, workflow CI, rồi tự build và chạy test. FigCraft là app mới trong bộ "Crafting Apps" của ArtCraft (danh mục `catalog.rs` của launcher ngày 14/10/2026 có 14 app, gồm cả FigCraft và PrintCraft); kho đã có hai app anh em là FilmCraft ([mục 01](../01-ai-coding-agents/README.md) §3d) và ArtCraft Launcher (mục 01 §3e).

### 7e.1 Hồ sơ nhanh

| Mục | Thông tin (đọc 14/10/2026) |
|---|---|
| Repo | `storytold/figcraft` · **616★**, 264 fork, 40 issue + 21 PR mở (shields) · license **MIT OR Apache-2.0**; tên, logo ArtCraft là thương hiệu riêng, bản fork phải gỡ · bản v0.5.1 (12/10/2026) |
| Định vị | "Interface design; an open-source, clean-room reimplementation of Figma, rebuilt in pure Rust": frame, auto layout, component/variant, vector network, style, variable, prototype, Dev Mode, phiên cộng tác. Chạy native trên macOS/Windows/Linux/FreeBSD và trong trình duyệt (WebAssembly) |
| Tác giả | Brandon Thomas (`echelon`, cựu CEO Storyteller.ai, nhà sáng lập ArtCraft/FakeYou) mở repo ngày **9/10/2026**. Người commit nhiều nhất là `BFlat`/`bflatastic` (210/267). Có 14 tên tác giả, trong đó 9 người ngoài góp qua PR |
| Cách làm | **191/267 commit (72%) ghi "Co-authored-by: Claude"** (Opus 5.5, có commit Sonnet 5.5). `CLAUDE.md` là hướng dẫn cho agent: mỗi phiên đọc `ROADMAP.md` và `docs/gaps.md`, rồi lấy việc ở đầu danh sách. Kế hoạch và ảnh chụp Figma để tham chiếu nằm trong `plan/`, thư mục này bị gitignore, không công khai. ROADMAP ước thời gian theo đơn vị "giờ của một agent Opus 5.5" |
| Quy mô | **204.110 dòng Rust** sau 5 ngày; 16 crate + 4 app (desktop, CLI, server, web); 2.088 hàm `#[test]` |
| Bộ anh em (GitHub search 14/10) | PhotoCraft 59,4k★ · ArtCraft 26,9k★ · PdfCraft 13,2k★ · FilmCraft 12,9k★ · LightCraft 12,2k★ · WordCraft 11,8k★ · VectorCraft 8,7k★ · EffectCraft 6,4k★ · GridCraft, CADCraft, DesignCraft, DeckCraft, SoundCraft · craft-launcher 2,5k★. Phần lớn tạo trong khoảng 30/9–9/10/2026; FigCraft là một trong những repo mới nhất và ít sao nhất |

### 7e.2 Kiểm lời tuyên bố

| Tuyên bố | Kiểm | Ghi chú |
|---|---|---|
| Có test và test thật sự chạy | ✅ | Khác FilmCraft (CI không chạy test), `ci.yml` của FigCraft chạy `cargo clippy -D warnings` + `cargo test --workspace` + kiểm phân tầng (`xtask layers`) + kiểm tài sản + build wasm32 trên mọi PR. Tự chạy `cargo test` cho 4 crate lõi (doc, layout, format, engine) ngày 14/10/2026: **1.092 pass, 0 fail, 2 ignored** |
| "Agent-ready": CLI, kênh JSON, MCP cùng một bộ lệnh | ✅ | Build `figcraft-cli` (release) rồi `render examples/ridgeline-app.figcraft` ra PNG 2639×1117, khớp ảnh trong README; `figcraft-cli commands` liệt kê bộ lệnh (README ghi "400+") |
| "Clean-room… no proprietary code, file formats" | ⚠️ | Không có cách kiểm độc lập: nguồn tham chiếu là `plan/` không công khai. `CLAUDE.md` cấm đọc bundle hay lưu lượng mạng của Figma và cấm dùng icon hay ảnh của họ. Phần đọc `.fig` thì dựa trên định dạng **kiwi**, vốn do đồng sáng lập Figma công bố mã mở. Vì vậy "no proprietary file formats" nên hiểu là không chép mã, chứ không phải không đọc định dạng của Figma |
| Mở được file `.fig` | ⚠️ | README ghi "best effort". `docs/gaps.md` xếp hạng 3: **"Nothing checked against real Figma files"**. Phần xuất `.fig` còn là thử nghiệm |
| "Accessible: screen readers get names, roles…" | ⚠️ | Có AccessKit trong mã, nhưng gaps.md hạng 22 ghi **"Screen readers never run; browser has no accessibility tree"**. README nói mạnh hơn mức đã kiểm |
| "No account, no telemetry, offline" | ✅/⚠️ | Đúng khi không chia sẻ. Bấm Share ▸ Online thì file được đẩy lên server công cộng mặc định `collab.craftapps.dev`, **không mã hóa đầu cuối**, ai có link là sửa được, file tồn tại tới 30 ngày sau lần mở cuối. README tự ghi rõ điều này |
| Mức sẵn sàng | ⚠️ alpha | Tự đánh giá: độ phủ menu/lệnh 100% (211/211, đo bằng `cargo xtask parity`), độ phủ tính năng khoảng 85%, "ready for real work" khoảng 53%. Hai con số sau là ước lượng. Còn cần 155–280 giờ agent nữa mới tới beta; multiplayer chưa có tài khoản; canvas vẽ bằng CPU |

**Tổng:** 3✅ / 5⚠️ / 0❌. Kỷ luật kỹ thuật tốt hơn FilmCraft: CI chặn PR, clippy cấm `unwrap`/`panic`, kiểm phân tầng. Nhưng các con số "parity" vẫn là tự chấm, và tính năng chưa từng được kiểm trên file Figma thật.

### 7e.3 So với các công cụ đã có trong kho

| | FigCraft | Penpot (§2) | Figma |
|---|---|---|---|
| Tuổi / độ chín | 5 ngày, alpha | Nhiều năm, đã dùng production (~61k★) | Sản phẩm thương mại |
| Mô hình | App native + wasm, file `.figcraft` trên máy; server cộng tác tự host được | Web app, self-host bằng Docker, định dạng mở (SVG/CSS) | Cloud, tài khoản |
| Đọc file Figma | Best effort, chưa kiểm trên file thật | Có plugin xuất từ Figma | Gốc |
| Cho agent | CLI + MCP + kênh JSON, mọi thao tác UI là một lệnh | Có API/plugin | MCP chính thức (Dev Mode) |
| License | MIT OR Apache-2.0 | MPL-2.0 | Đóng |

**Trùng tên:** `divikwu/figcraft` (4★) là một **MCP server cho Figma**, không liên quan tới dự án này.

### 7e.4 Dùng thế nào

- **Cho đội cần thay Figma ngay:** vẫn chọn Penpot. FigCraft mới 5 ngày tuổi, chưa kiểm trên file thật, chưa có tài khoản.
- **Cho agent sinh UI:** đây là điểm đáng thử nhất. `figcraft-cli mcp` cho agent dựng frame, component, auto layout rồi render PNG/SVG headless; cả 5 file mẫu trong `examples/` đều được dựng qua bộ lệnh này. Có thể dùng làm "canvas" cho agent thay vì để agent sinh HTML.
- **Không chia sẻ file nhạy cảm qua server mặc định.** Tự chạy `figcraft-server` sau Caddy/nginx, hoặc chia sẻ trong mạng LAN tin cậy.
- **Bài học quy trình** (giống FilmCraft): nhiều phiên agent cùng đọc một danh sách việc xếp hạng (`docs/gaps.md`), mỗi việc kết thúc bằng cập nhật ROADMAP và ước lượng giờ. Khác biệt đáng giá là FigCraft bật CI chặn PR ngay từ ngày đầu.
- **Tải bản build:** chỉ lấy từ release của `storytold/figcraft` hoặc getartcraft.com. Kho đã ghi nhận repo nhái mồi malware cho FilmCraft (mục 01 §3d).

**Nguồn §7e:** https://github.com/storytold/figcraft (clone đầy đủ, 267 commit, HEAD bcedfeb 14/10/2026; README, NOTICE, ATTRIBUTION.md, CLAUDE.md, ROADMAP.md, docs/gaps.md, crates/format/src/fig/mod.rs, .github/workflows/ci.yml; tự chạy 14/10/2026: `cargo test -p figcraft-doc -p figcraft-layout -p figcraft-format -p figcraft-engine` 1.092 pass, `figcraft-cli render` ra PNG) · shields 14/10/2026 (616★, 264 fork, release v0.5.1) · GitHub search API 14/10/2026 (51 repo của `storytold`) · https://github.com/storytold/craft-launcher (`crates/core/src/catalog.rs`, 14/10/2026) · https://getartcraft.com/apps/figcraft · https://petapixel.com/2026/10/07/someone-rebuilt-free-open-source-versions-of-photoshop-premiere-and-lightroom-using-ai/ · https://propakistani.pk/2026/10/09/free-open-source-copies-of-photoshop-premiere-and-lightroom-are-here/ · https://www.tweaktown.com/news/113989/developer-says-software-is-over-after-using-ai-to-recreate-adobes-entire-creative-cloud-suite-for-free/index.html · https://www.it-connect.fr/suite-adobe-rust-claude-opus-artcraft-crafting-apps/ · https://ecosistemastartup.com/artcraft-clona-7-apps-de-adobe-con-claude-opus-5-5/ · https://www.besthub.dev/articles/rewriting-adobe-suite-in-rust-12-open-source-apps-56k-stars-built-for-ai-agents-051d286733fe · https://notes.nicolasdeville.com/apps/artcraft/ · https://glama.ai/mcp/servers/divikwu/figcraft (dự án trùng tên)

## 7f. Zen Design System (Dizai Studio) và design system "AI-ready" (yêu cầu người dùng, 2026-10-16)

> Người dùng hỏi "Zen Design System và các system thiết kế UI/UX khác". Tên này ứng với nhiều dự án; mục này lấy repo mang đúng tên **"Zen Design System"** (`Zen-Design-System/Zen-DS`, của Dizai Studio, Việt Nam) làm chính, liệt kê các dự án trùng tên, rồi so với các design system lớn theo tiêu chí mà Zen lấy làm điểm bán: dùng được với AI agent. Đã clone đầy đủ Zen-DS (HEAD `0e0ff04c` 16/10/2026), cài devDependencies, chạy toàn bộ cổng kiểm của repo và bộ test.

### 7f.1 Trùng tên "Zen"

| Dự án | Là gì | Ghi chú (16/10/2026) |
|---|---|---|
| **`Zen-Design-System/Zen-DS`** | Design system thương mại của **Dizai Studio** (Việt Nam), React 19 + TypeScript, sinh từ thư viện Figma | Mục chính, xem 7f.2 |
| `umami-software/zen` | Design system và bộ component React của **Umami** (analytics mã mở), theo quy ước shadcn, primitive **Base UI**, Tailwind v4 | **MIT**, 58★, 726 commit (721 của Mike Cao, người lập Umami), npm `@umami/react-zen` 0.255.0, ~104 file component, có `SKILL.md` cho agent; tài liệu zen.umami.is |
| `reciprocity/zen-design-system` | Biến, style cho micro-frontend "Zen" của Reciprocity | Dừng từ 11/2020 |
| Zen UI (Flowbase) | Bộ component cho **Webflow**, file Figma bán riêng | Không phải mã mở |
| Zendesk Garden | Design system của Zendesk (`zendeskgarden/react-components`) | Không phải "Zen", hay bị nhầm; Apache-2.0, ~1,1k★ |

### 7f.2 Hồ sơ Zen DS

| Mục | Thông tin (đọc 16/10/2026) |
|---|---|
| Repo | `Zen-Design-System/Zen-DS` · **0★** (shields), 561 commit trong 18 ngày có commit, từ 25/9/2026; Alex Duong 287, commit đồng tác giả Claude 168, `alexduonguiux-hub` 83. Bài LinkedIn có hashtag #zendesignsystem #dizaistudio nhắc đội ngũ Việt Nam; quan hệ giữa các tài khoản và Dizai **chưa xác minh** |
| Nội dung | 67 component có hướng dẫn (đếm bởi `guidelines:check`; Button, input, Table, Dialog, Sidebar, Chat, Chart, app shell…), mỗi component có hướng dẫn Do/Don't và tài liệu props sinh tự động; README ghi **2.179 biến Figma** trên 7 trục chế độ (theme, component theme, density, radius, emphasis, breakpoint, typography), 36 text style, 18 effect style, **1.598 icon**; trang tài liệu "Codebase Platform" và Storybook |
| Lớp cho AI agent | `AGENTS.consumer.md` (đi kèm package, dành cho agent dựng app), `AGENTS.md` (cho agent sửa chính design system), `llms.txt`; **MCP server cục bộ** (`node mcp/server.mjs`, stdio, 11 tool: `list_components`, `get_component`, `get_tokens`, `search_icons`, `list_templates`, `map_figma_component`, `check_spec`, `check_usage`…; không gọi mạng); 8 skill (`zen-component-usage`, `zen-figma-design`, `zen-token-sync`, `zen-responsive-screens`…) |
| Cổng máy | **Usage guard** 205 luật dùng component (có plugin ESLint), kiểm token/text style/icon, đồng bộ hướng dẫn với props, "Figma parity" (`tools/figma-contract`), `verify:package` (đóng gói, cài vào app tạm, type-check, build, kiểm ngân sách kích thước) |
| Giấy phép | **Thương mại, theo số người dùng (seat)**: package `@zen-ds/react` chỉ cài được từ registry riêng `npm.dizai.studio` sau khi đăng nhập tài khoản Zen. Mã nguồn công khai trên GitHub nhưng **không phải mã mở**. `LICENSE.md` (bản 1.0, hiệu lực 8/10/2026) cho phép sửa mã, dùng trong số End Product không giới hạn, cho phép dùng AI agent qua MCP; đầu file ghi **"Draft for legal review… has not yet been reviewed by a lawyer"** |
| npm công khai | `@zen-ds/react@0.1.0` (5/5/2026), ghi **MIT**, maintainer `zen-ds`. Tài liệu của Zen gọi đây là "old public 0.1.0" và cảnh báo thiếu dòng scope trong `.npmrc` thì npm cài nhầm bản này; `npx zen-ds doctor` kiểm điều đó |

**Tự chạy (Node 24.22, `npm ci --ignore-scripts`, 16/10/2026):**

| Lệnh | Kết quả |
|---|---|
| `npx tsc --noEmit -p .` | Sạch |
| `npm run usage:selftest` | 205 luật, mỗi luật bắt được lỗi trong fixture xấu, fixture tốt sạch |
| `npm run usage:check` | Đạt: 464 file, 205 luật, 1 cảnh báo |
| `tokens:check` · `styles:check` · `icons:check` | Đạt, 0 lỗi |
| `guidelines:check` | Hướng dẫn khớp mã: 67 component, 236 union khớp, 85 không phân giải được |
| `node mcp/selftest.mjs` | 11 tool trả lời đúng qua client SDK stdio |
| `npx vitest run` | **1.058 test pass, 24 skip** (70 file) |

**Đánh giá Zen DS:**

- **Điểm mạnh thật, đã kiểm:** tài liệu dành cho agent, MCP cục bộ, và luật dùng component **kiểm bằng máy** (205 luật, có self-test chứng minh mỗi luật bắt được lỗi). Cách này khớp với bài học "skill chỉ khuyên, cổng máy mới chặn" của mục 21 §10c và XIAS (§7d): muốn agent dùng đúng design system thì phải có linter, không chỉ có văn bản hướng dẫn.
- **Rủi ro:** sản phẩm mới khoảng 3 tuần, 0★, chưa có người dùng công khai; mã do một người và agent viết là chính; giấy phép còn là **bản nháp chưa qua luật sư**; phụ thuộc registry riêng và tài khoản của Dizai (mất licence là mất quyền cập nhật). Bản 0.1.0 công khai ghi MIT trong khi bản hiện tại là thương mại: quyền MIT của bản 0.1.0 đã phát hành không tự thu hồi được; muốn dùng hợp pháp bản mới thì phải mua licence.
- **Hợp với ai:** đội ở Việt Nam cần một design system có sẵn Figma + React + lớp cho agent, chấp nhận trả theo seat. Đội cần mã mở thì xem bảng 7f.3.

### 7f.3 Các design system khác, nhìn theo "AI-ready" (shields 16/10/2026)

| Design system | ★ · license | Nền | Lớp cho AI agent (đọc 16/10/2026) |
|---|---|---|---|
| **shadcn/ui** | 126k · MIT | Copy mã vào dự án, Base UI/Radix + Tailwind | MCP server chính thức trong CLI (duyệt, tìm, cài component từ registry), skill, `llms.txt`. Đầy đủ nhất trong nhóm mã mở |
| **Ant Design** | 100k · MIT | Component đầy đủ cho ứng dụng doanh nghiệp | Có MCP theo bài tổng hợp, mức "tài liệu" **(chưa xác minh từ trang chính thức)** |
| **MUI (Material UI)** | 99k · MIT | Material Design | MCP trả tài liệu và ví dụ **(chưa xác minh từ trang chính thức)** |
| **Chakra UI** / **Ark UI** | 41k / 5,4k · MIT | Chakra có style; Ark là headless của cùng đội | MCP có hướng dẫn cho Cursor/VS Code/Claude **(chưa xác minh từ trang chính thức)** |
| **Mantine** | 32k · MIT | Component đầy đủ, hook | Có trong danh sách MCP của bài tổng hợp **(chưa xác minh)** |
| **HeroUI** (tên cũ NextUI) | 31k · Apache-2.0 | React + Tailwind | – |
| **Fluent UI** (Microsoft) | 20k · shields không nhận diện | Fluent 2 | `llms.txt` theo UICentral; không tìm thấy MCP chính thức |
| **Radix Primitives** / **Base UI** | 19k / 11k · MIT | Headless | – |
| **React Spectrum / React Aria** (Adobe) | 16k · Apache-2.0 | Headless + design system Spectrum; mạnh về a11y | – |
| **Material Web** (Google) | 11k · Apache-2.0 | Web component Material 3 | – |
| **Carbon** (IBM) | 9,5k · Apache-2.0 | Web component + React | **Carbon MCP** (public preview, cần IBMid; mã đóng theo bài ngoài) · `llms.txt` |
| **USWDS** | 7,2k | Design system chính phủ Mỹ | – |
| **Polaris** (Shopify) | 6,2k | Đã chuyển sang web component cho app Shopify | – |
| **Primer** (GitHub) | 3,9k · MIT | React + CSS | **`@primer/mcp`** chính thức, stdio cục bộ: token, component, pattern, icon (trang primer.style) |
| **Atlassian Design System** | npm `@atlaskit/*` | React | **`@atlaskit/ads-mcp`** (Early Access) + MCP hosted tại mcp.atlassian.com; Atlassian còn công bố `DESIGN.md` (xem §7c) |
| **GOV.UK Frontend** | 1,5k · MIT | Design system chính phủ Anh, chuẩn a11y | – |
| **Zendesk Garden** | 1,1k · Apache-2.0 | React | – |
| **Zen DS** (Dizai) | 0 · thương mại | React 19 + Figma | MCP cục bộ 11 tool, `AGENTS.consumer.md`, `llms.txt`, **205 luật dùng kiểm bằng máy** |

**Chọn thế nào (cho dự án của chủ kho):**

- **Mặc định cho React + Tailwind:** shadcn/ui (mã nằm trong repo, MCP chính thức, giấy phép MIT). Umami Zen là ví dụ tốt về cách một sản phẩm thật dựng design system riêng trên shadcn + Base UI.
- **Ứng dụng nghiệp vụ nhiều bảng, form:** Ant Design hoặc MUI. Cần a11y chặt (chính phủ, y tế): React Aria/Spectrum hoặc GOV.UK Frontend làm chuẩn tham chiếu.
- **Học cách làm design system "cho agent":** đọc Primer MCP (mã mở, cục bộ) và Zen DS (usage guard có self-test). Hai thứ đáng chép là MCP trả token/component đúng phiên bản đang cài, và linter luật dùng component chạy trong CI, không chỉ trong prompt.
- **Trước khi dùng một design system thương mại** (Zen DS hay bất kỳ): đọc giấy phép bản đã ký, không bản nháp; hỏi rõ chuyện gì xảy ra với End Product khi ngừng trả phí; ghim registry trong `.npmrc` để không cài nhầm package trùng tên trên npm công khai.

**Nguồn §7f:** https://github.com/Zen-Design-System/Zen-DS (clone đầy đủ, HEAD 0e0ff04c; README.md, LICENSE.md, AGENTS.consumer.md, AGENTS.md, .mcp.json, mcp/server.mjs, skills/, package.json; tự chạy tsc, usage/tokens/styles/icons/guidelines check, MCP selftest, vitest) · https://registry.npmjs.org/@zen-ds%2freact (0.1.0, MIT, 5/5/2026) · https://github.com/umami-software/zen · https://zen.umami.is/ · https://registry.npmjs.org/@umami%2freact-zen · https://github.com/reciprocity/zen-design-system · https://webflow.com/libraries/detail/zen-ui · https://vn.linkedin.com/in/tungoc19 · https://primer.style/product/getting-started/foundations/mcp/ · https://carbondesignsystem.com/developing/carbon-mcp/overview/ · https://www.npmjs.com/package/@atlaskit/ads-mcp · https://www.atlassian.com/blog/how-we-build/atlassians-design-md-is-here-what-we-learned-testing-portable-design-context-in-practice · https://state-of-ai-in-design-systems.netlify.app/systems/shadcn-ui · https://uicentral.fyi/blog/ui-component-libraries-with-mcp-servers · https://daily.dev/posts/top-10-best-react-ui-libraries-2026-ai-dx-edition--xtcsp4agl · https://mowgli.ai/blog/mcp-servers-for-ui-design-2026 · shields.io cho số sao các repo trong bảng 7f.3

## 7g. Bốn skill/kho UI đã được nhắc nhưng chưa có hồ sơ (yêu cầu người dùng, 2026-10-18)

> §4 và §7d nhắc tới `ui-ux-pro-max-skill`, `frontend-design` của Anthropic, "Refactoring UI Skill" và `bergside/awesome-design-skills`, nhưng catalog chưa có dòng nào cho chúng. Mục này lập hồ sơ cả bốn: clone repo ngày 18/10/2026, đếm file và dữ liệu thật, tự chạy test hoặc kiểm số liệu khi có thể, rồi đối chiếu với nguồn ngoài.

### 7g.1 Bảng nhanh

| | `ui-ux-pro-max-skill` | `frontend-design` (Anthropic) | Refactoring UI Skill (`s0xDk`) | `bergside/awesome-design-skills` |
|---|---|---|---|---|
| Bản chất | Kho tra cứu (CSV + BM25) sinh "design system" theo loại sản phẩm, kèm 6 skill phụ | 1 prompt ~70 dòng định hướng thẩm mỹ, chống mặc định | 1 skill quy tắc + token CSS lấy từ sách *Refactoring UI* | 67 cặp `SKILL.md` + `DESIGN.md` theo style, kéo về bằng CLI TypeUI |
| ★ · license (18/10/2026) | ~137k · MIT | `anthropics/claude-plugins-official` ~42k · Apache-2.0 | 646 · MIT | ~3,2k · MIT |
| Hoạt động | 277 commit, v2.15.0, commit cuối 14/10/2026 | Plugin 1.1.0, SKILL.md sửa lần cuối 2–3/9/2026 | 2 commit, cùng ngày 27/8/2026 | 49 commit, 9/3 → 28/6/2026 |
| Có cổng máy? | Có validator dữ liệu + 164 unit test của chính repo; **không** đo bản render | Không; chỉ dặn "tự chụp màn hình để phê bình" | Không; token đã kiểm tương phản sẵn | Không; mục "Quality Gates" là văn bản |
| Đã kiểm | `unittest` 164/164 pass, `validate_data.py` OK, chạy thử 1 truy vấn | 3 bản SKILL.md trong 3 repo giống hệt nhau | Tính lại tỉ lệ tương phản light và dark mode: khớp chú thích | 81% dòng là khung chung; 40/67 màu primary không đạt 4,5:1 với chữ trắng |

### 7g.2 `nextlevelbuilder/ui-ux-pro-max-skill`: kho tra cứu lớn nhất, tạo design system bằng tìm kiếm

| Mục | Thông tin (đọc 18/10/2026) |
|---|---|
| Repo | `nextlevelbuilder/ui-ux-pro-max-skill` · trang GitHub **~137k★**, ~14,6k fork · **MIT** (© 2024 Next Level Builder) · tag mới nhất **v2.15.0** · 277 commit, commit đầu 30/11/2025, cuối 14/10/2026 |
| Tác giả | Viet Tran (`viettranx`) 55 commit, "Goon" 30, Clark Cant 17, Duy 15. README có bản tiếng Việt, ảnh demo có giao diện tiếng Việt; tác giả và đội có vẻ ở Việt Nam **(chưa xác minh danh tính)**. Cùng chủ: `3dviz-pro-max`, goclaw.sh, agentkit.best |
| Phân phối | `npx ui-ux-pro-max-cli init --ai <platform>` cho 19 nền tảng (Claude, Cursor, Copilot, Codex, Gemini, Kiro, OpenClaw…). npm `ui-ux-pro-max-cli`: **72.299** lượt tải trong 17/9–16/10/2026 |
| Bên trong | 7 skill trong `.claude/skills/` (`ui-ux-pro-max` 214 dòng, `design` 333, `ui-styling` 336, `design-system` 248, `brand`, `banner-design`, `slides`). Lõi là `scripts/search.py` + `core.py` (**BM25**) chạy trên 13 file CSV. Dữ liệu được nhân bản 3 lần (`src/`, `cli/assets/`, `.claude/skills/`) và `diff` cho thấy giống nhau |

**Đếm lại các con số trên badge** (từ `data/*.csv` và `catalog-summary.json`):

| Badge/README | Đếm thật | Ghi chú |
|---|---|---|
| "79 searchable UI styles" | ✅ 88 dòng, trong đó 79 "searchable" (50 active + 29 supplemental), 9 deprecated | `catalog-summary.json` giải thích đúng |
| "192 reasoning rules", 192 palette, 192 loại sản phẩm | ✅ đúng 192 dòng mỗi file | Mỗi "rule" là một dòng gợi ý theo loại sản phẩm, không phải luật kiểm được |
| 74 font pairing, 119 UX guideline, 25 loại chart, 22 stack | ✅ khớp | Thêm 1.934 Google Fonts, 105 icon chọn lọc |
| Nguồn dữ liệu | ⚠️ `data-provenance.json` chỉ có **51 bản ghi**, phủ 51/192 profile; 31 bản ghi đang "needs-review" | Phần lớn dữ liệu không ghi nguồn gốc từng dòng |

**Tự chạy (Python 3, 18/10/2026):** `python3 -m unittest discover` **164/164 pass**; `validate_data.py` OK (12 file domain, 22 file stack). Thử truy vấn `"fintech mobile banking app" --design-system` thì nhận về pattern **trang landing** ("Contact Sales / Get Quote", logo carousel, Hero → Proof) chứ không phải màn hình app. Accent là tím `#8B5CF6` với ghi chú "Gold trust + purple tech", trong khi mục AVOID của cùng kết quả ghi "AI purple/pink gradients". Checklist còn yêu cầu `cursor-pointer` và hover cho một app mobile. Đây là một truy vấn, chưa đại diện cho cả kho, nhưng cho thấy BM25 khớp theo từ khóa chứ không hiểu ngữ cảnh mobile.

**Đánh giá:**

- **Điểm mạnh:** dữ liệu lớn, có cấu trúc, tra cứu tất định (cùng câu hỏi ra cùng kết quả), có test và validator thật, hỗ trợ nhiều agent nhất trong nhóm. Hợp làm **nguồn gợi ý** palette, font, style khi chưa có brand.
- **Hạn chế:** không có cổng đo trên bản render. Đây là điểm khác chính với Impeccable (mục 20, engine Rust 59 rule tất định) và XIAS (§7d, 52 cổng trình duyệt), như mục 20 đã ghi. Kết quả có thể tự mâu thuẫn như ví dụ trên. Số sao tăng rất nhanh: agentskill.sh ghi 38,3k (3/2026), Skillselion ghi 112k (30/7/2026), trang GitHub ~137k (18/10/2026).
- **Dùng thế nào:** gọi `search.py` để lấy gợi ý, rồi để người hoặc agent chọn lại theo brief. Không dùng nguyên output làm design system. Ghép với một bộ cổng đo (ví dụ script của XIAS) nếu muốn chặn lỗi tương phản. Mục 23 ghi repo này từng được vendor trong Hermes-Agents (45 file).

### 7g.3 `frontend-design` (Anthropic): prompt ngắn, chính chủ, thay đổi theo thời gian

| Mục | Thông tin (đọc 18/10/2026) |
|---|---|
| Vị trí | `anthropics/claude-code/plugins/frontend-design` (plugin 1.1.0), `anthropics/claude-plugins-official/plugins/frontend-design`, `anthropics/skills/skills/frontend-design`. Cả ba `SKILL.md` **giống hệt nhau** (71 dòng) |
| Tác giả | Prithvi Rajasekaran, Alexander Bricken (Anthropic Applied AI, theo `plugin.json`). Bài blog "Improving frontend design through Skills" ngày 12/11/2025 |
| License | `LICENSE.txt` Apache-2.0 trong `anthropics/skills` |
| Cài | `/plugin marketplace add anthropics/claude-code` rồi `/plugin install frontend-design@claude-code-plugins`; hoặc lấy từ marketplace chính thức. Skill do model tự gọi theo mô tả, không phải lệnh `/` |
| Lịch sử | Thêm 11/11/2025; viết lại 9/6, 17/6 (bump 1.1.0) và 2–3/9/2026 |

**Nội dung bản hiện tại:** vai "design lead của studio", buộc xác định chủ đề, người dùng và việc chính của sản phẩm trước khi thiết kế; quy trình hai lượt (lên plan token màu 4–6 hex, font, layout bằng ASCII wireframe, rồi tự so plan với "bản mặc định" và sửa trước khi code); một phần dài về viết nội dung UI (CTA nói rõ hành động, lỗi không xin lỗi, sentence case). Phần đáng chú ý nhất là danh sách **5 cụm "dấu hiệu AI"** cụ thể: nền kem `#F4F1EA` + serif + accent đất nung `#D97757` (skill tự nhận đây là màu của chính Claude), nền gần đen + một accent xanh axit, layout báo giấy, "bộ card SaaS" bóng `rgba(0,0,0,.1)`, và các chi tiết khuôn như eyebrow viết hoa, chuỗi "A · B · C", mũi tên "→" sau nút.

**Đánh giá:**

- **Điểm mạnh:** ngắn (bài blog ước ~400 token cho bản đầu), chính chủ, cập nhật theo chính những gì model hay lặp lại. Bản 9/2026 còn đảo một phần lời khuyên của bản 11/2025: blog gốc khuyên dùng nền gradient nhiều lớp và animation tải trang, bản mới coi "gradient washes as decoration" và fade-up từng section là dấu hiệu AI.
- **Hạn chế:** không có cổng máy, chỉ dặn tự chụp màn hình để phê bình. Bài blog chỉ có ảnh so sánh, **không có benchmark**. Con số "1,1 triệu lượt cài" xuất hiện ở một số trang tổng hợp nhưng không tìm thấy trên trang chính thức **(chưa xác minh)**. Mục tiêu là "khác biệt", nên với sản phẩm đã có brand phải nói rõ ràng buộc trong prompt (skill có ghi "lời của brief luôn thắng").
- **Dùng thế nào:** bật cho trang mới, landing, prototype. Với ứng dụng nghiệp vụ đã có design system thì design system thắng; ghép thêm cổng đo (XIAS) hoặc detector (Impeccable) nếu cần chặn.

### 7g.4 "Refactoring UI Skill": hai repo trùng tên, chọn bản `s0xDk`

`maxbogo/awesome-ai-tools-for-ui` (mục 08) trỏ tới **`s0xDk/refactoring-ui-skill`**. Tìm web còn ra `lovropodobnik/refactoring-ui-skill` (2 commit ngày 8/1/2026, skill 32 dòng + 5 lệnh `/fix-*`, **không có file LICENSE**) và `booklib-ai/skills/refactoring-ui` (chỉ thấy qua trang tổng hợp, chưa xác minh). Hồ sơ dưới đây là bản `s0xDk`.

| Mục | Thông tin (đọc 18/10/2026) |
|---|---|
| Repo | `s0xDk/refactoring-ui-skill` · **646★**, 62 fork · **MIT** (© 2026 s13k) · **2 commit, cùng ngày 27/8/2026** |
| Bên trong | `SKILL.md` 267 dòng (thang spacing, type, weight, màu HSL, 5 mức bóng, line-height, radius; quy trình; 9 "hard rule") · `references/systems.md` (dựng palette), `diagnose.md` (bảng triệu chứng → cách sửa), `techniques.md` · `assets/tokens.css` (token đầy đủ: thang, ramp xám và primary 9 mức, 3 bộ màu accent, lớp semantic `--surface`/`--text-*`/`--action` và khối dark mode) |
| Bản quyền sách | README ghi không chứa chữ hay hình của sách, chỉ ghi chú và CSS tự viết theo ý tưởng của sách |

**Kiểm token (18/10/2026):** tính lại tỉ lệ tương phản theo WCAG từ các giá trị HSL trong `tokens.css`. Light mode khớp chú thích: `grey-400` 2,67:1 (chỉ dùng cho chữ disabled), `grey-500` 3,91:1 (chỉ chữ lớn), `grey-600` 5,60:1, `grey-900` 13,43:1 so với nền `grey-100`; chữ trắng trên `primary-500` 5,81:1, trên `red/yellow/green-500` lần lượt 6,15 / 4,98 / 6,06:1. **Dark mode (kiểm lại 19/10/2026** bằng script đọc khối `@media (prefers-color-scheme: dark)` và giải `var()`, màu làm tròn về 8-bit như trình duyệt): `--text-primary` 11,22:1, `--text-secondary` 9,95:1, `--text-tertiary` 6,05:1 trên nền và 4,81:1 trên `--surface-raised`, chữ trên `--action` 5,19:1, `--border-strong` 5,03 / 3,99:1; đều khớp chú thích trong file. Tính theo 8-bit, các số light mode ở trên lệch tối đa 0,05 (vd primary-500 5,78:1).

**Đánh giá:**

- **Điểm mạnh:** quy tắc cụ thể đến mức kiểm được (không hai bước spacing nào gần nhau dưới ~25%, chữ lớn theo WCAG là 24px hoặc 18,66px đậm chứ không phải 18px, viền chức năng cần 3:1). Token có sẵn và đúng như chú thích. Có bảng chẩn đoán để sửa UI cũ, điều ít skill "taste" làm.
- **Hạn chế:** chỉ 2 commit, một tác giả, chưa có lịch sử bảo trì. Không có cổng máy; luật nằm trong prompt. Thiên về web/CSS, chưa nói tới mobile native.
- **Dùng thế nào:** hợp làm lớp "hệ thống" bên dưới một skill "taste" (frontend-design hoặc Taste Skill): skill này giữ thang giá trị, skill kia quyết định cá tính. Có thể chép thẳng `tokens.css` làm điểm khởi đầu rồi đổi hue.

### 7g.5 `bergside/awesome-design-skills`: 67 style viết bằng một khuôn

| Mục | Thông tin (đọc 18/10/2026) |
|---|---|
| Repo | `bergside/awesome-design-skills` · trang GitHub **~3,2k★**, 327 fork · **MIT** (© 2026 Bergside) · 49 commit, **tất cả của Zoltán Szőgyényi** (đồng sáng lập Themesberg theo blog của Themesberg, công ty làm Flowbite; quan hệ với Bergside chưa xác minh), 9/3 → 28/6/2026 |
| Bên trong | 67 thư mục trong `skills/`, mỗi thư mục có `SKILL.md` (81–101 dòng, trung vị 83) và `DESIGN.md`; `index.json`; ảnh preview |
| Phân phối | CLI **TypeUI** (`npx typeui.sh pull <slug>`, repo `bergside/typeui.sh`), ghi file vào `.claude/`, `.cursor/skills/`…; npm `typeui.sh` 1.297 lượt tải 17/9–16/10/2026. Trang tổng hợp nhắc tới bản Pro trả phí **(chưa xác minh)** |

**Đo chất lượng (18/10/2026):**

- **Khuôn chung chiếm phần lớn:** cả 67 `SKILL.md` có đúng 13 mục giống nhau (Mission, Brand, Style Foundations… Quality Gates), nằm giữa hai dấu `TYPEUI_SH_MANAGED`. Trung bình **81% số dòng** của mỗi file cũng xuất hiện ở ≥90% các file khác. Phần riêng của từng style chủ yếu là một câu mô tả, tên font và vài mã màu.
- **Màu:** 17/67 style dùng cùng primary `#3B82F6` (blue-500 của Tailwind). Nếu đặt chữ trắng trên nền primary (cách phổ biến cho nút), **40/67** style không đạt 4,5:1. Ví dụ `brutalism` `#DD614C` 3,57:1, `bento` `#FAD4C0` 1,38:1. File không quy định màu chữ trên primary, nên đây là rủi ro khi dùng chứ không hẳn là lỗi file.
- **Tên thương hiệu:** có style đặt theo thương hiệu (`claude`, `codex`, `stitch`, `roku`, `sega`, `pacman`, `tetris`, `ant`…) mà không có ghi chú quan hệ hay tuyên bố không liên kết.
- **Liên hệ:** §7d đã ghi 51 style của XIAS lấy mô tả và màu từ kho này mà không ghi công.

**Đánh giá:** hợp làm **danh mục cảm hứng** hoặc khung để tự viết `SKILL.md` theo style. Muốn có giá trị kiểm chứng thì viết DESIGN.md theo spec Google (§7c) và chạy `lint`; với style có primary sáng, thêm token `on-primary` rõ ràng.

### 7g.6 Xếp vào bức tranh chung

| Lớp | Nên dùng | Vì sao |
|---|---|---|
| Thang giá trị, token nền | Refactoring UI Skill (`s0xDk`) | Quy tắc kiểm được, token đúng chú thích |
| Hướng thẩm mỹ, chống "AI slop" | `frontend-design` (chính chủ) hoặc Taste Skill (§4) | Ngắn, danh sách dấu hiệu cụ thể |
| Gợi ý palette/font theo loại sản phẩm | `ui-ux-pro-max-skill` | Kho dữ liệu lớn, tra cứu tất định, nhưng phải chọn lọc lại |
| Khung style có sẵn | `bergside/awesome-design-skills`, `awesome-design-md` (§7c) | Cảm hứng; tự viết lại cho brand |
| Cổng đo bắt lỗi thật | XIAS (§7d), Impeccable (mục 20) | Hai bộ duy nhất trong kho có đo hoặc detector tất định |

Cả bốn mục trên đều **không có benchmark độc lập**, giống nhận xét ở §4. Bài học của §4 vẫn đúng: "taste" chỉ bền khi có cổng máy đi kèm.

**Nguồn §7g:** https://github.com/nextlevelbuilder/ui-ux-pro-max-skill (clone đủ, 277 commit, HEAD 56ea9cf 14/10/2026; README, skill.json, LICENSE, `src/ui-ux-pro-max/data/*.csv`, `catalog-summary.json`, `data-provenance.json`, `scripts/core.py`; tự chạy `unittest` 164/164, `validate_data.py`, `search.py --design-system` 18/10/2026) · trang GitHub 18/10/2026 (~137k★, ~14,6k fork) · api.npmjs.org `ui-ux-pro-max-cli` (72.299, 17/9–16/10/2026) · skillselion.com/best/plugins-for-frontend-design (112k★, dữ liệu 30/7/2026) · agentskill.sh/@nextlevelbuilder/ui-ux-pro-max (38,3k★, 3/2026) · releasealert.dev/github/nextlevelbuilder/ui-ux-pro-max-skill · https://github.com/anthropics/claude-code/tree/main/plugins/frontend-design (README, plugin.json 1.1.0, SKILL.md; git log) · https://github.com/anthropics/claude-plugins-official (trang GitHub ~42,3k★, 18/10/2026; SKILL.md) · https://github.com/anthropics/skills (`skills/frontend-design/SKILL.md`, LICENSE.txt Apache-2.0) · https://claude.com/blog/improving-frontend-design-through-skills (12/11/2025) · wmedia.es/en/tips/claude-code-frontend-design-skill · claudelog.com/faqs/what-is-frontend-design-skill-in-claude-code · https://github.com/s0xDk/refactoring-ui-skill (clone đủ, 2 commit, HEAD 4887214 27/8/2026; SKILL.md, references/, assets/tokens.css, LICENSE; trang GitHub 646★/62 fork 18/10/2026; tính tương phản light mode) · https://github.com/lovropodobnik/refactoring-ui-skill (clone, 2 commit 8/1/2026, không LICENSE) · vibeindex.ai/skills/booklib-ai/skills/refactoring-ui · https://github.com/maxbogo/awesome-ai-tools-for-ui (README dòng 51) · https://github.com/bergside/awesome-design-skills (clone đủ, 49 commit, HEAD f631a09 28/6/2026; README, LICENSE, `skills/*/SKILL.md`; đo trùng dòng và tương phản 18/10/2026; trang GitHub ~3,2k★/327 fork) · api.npmjs.org `typeui.sh` (1.297, 17/9–16/10/2026) · sourcepulse.org/projects/26797192 · hermesatlas.com/projects/bergside/typeui · vibeindex.ai/collection/bergside/awesome-design-skills · themesberg.com/blog/marketplace/2020-year-in-review

## 7h. Layout mẫu cho web, dashboard và mobile (yêu cầu người dùng, 2026-10-18)

> Người dùng hỏi "layout mẫu cho mobile, web, app". Mục này lập hồ sơ các nguồn **page block, template trang và app shell** có mã dùng được, cộng hai bộ hướng dẫn layout chính thức (Material 3, Apple HIG). Đã clone 21 repo ngày 18/10/2026; số commit, ngày commit cuối và license đọc từ bản clone; số block/trang **đếm bằng `git ls-tree`**, không lấy từ README. Số sao là số làm tròn trên trang GitHub cùng ngày.

### 7h.1 Bảng tổng hợp

| Nhóm | Nguồn | ★ · license | Commit cuối · số commit | Layout thực có trong repo | Stack |
|---|---|---|---|---|---|
| Web | **shadcn/ui Blocks** (`shadcn-ui/ui`) | 125,8k · MIT | 16/10/2026 · 2.571 | 27 block trong `registry/new-york-v4/blocks`: 1 dashboard, 16 sidebar, 5 login, 5 signup; thêm ~70 chart và ~32 calendar block | React, Tailwind v4 |
| Web | **HyperUI** (`markmead/hyperui`) | 12,3k · MIT | 10/10/2026 · 825 | 306 mẫu HTML bản sáng (≈560 file kể cả bản tối): marketing 106, application 163, neobrutalism 37; 12 trang template (analytics dashboard, SaaS landing, portfolio, storefront, support inbox) | HTML + Tailwind |
| Web | **Once UI core** (`once-ui-system/core`) | 268 · MIT | 18/10/2026 · 1.207 | 175 file block trong app docs: Hero 14, Features 18, Sidebar 9, Login 5, Dashboard 3, Pricing, FAQ… | Next.js, SCSS |
| Web | **Preline** (`htmlstreamofficial/preline`) | 6,5k · MIT **+ Preline UI Fair Use License** | 21/8/2026 · 142 | Repo chỉ có 29 plugin JS và 5 template HTML; "204 free blocks" của README nằm trên preline.co, không trong repo | HTML, Tailwind, JS |
| Web | **Flowbite** (`themesberg/flowbite`) | 9,4k · MIT (lõi) | 27/6/2026 · 2.789 | Chỉ trang tài liệu component; Blocks "400+ sections" thuộc bản Pro trả phí | Tailwind, JS |
| Web | **daisyUI** (`saadeghi/daisyui`) | 42,6k · MIT | 13/10/2026 · 3.291 | 61 component CSS, không có trang mẫu; template đầy đủ bán ở daisyui.com/store (vd dashboard từ $69) | Plugin Tailwind |
| Web | **Tailwind Plus** (trước là Tailwind UI) | – · thương mại | – | **Ngừng nhận khách mới** từ khi Tailwind Labs về Shopify (9/9/2026); khách cũ giữ quyền dùng | React/Vue/HTML |
| Dashboard | **shadcn-admin** (`satnaing/shadcn-admin`) | 15,8k · MIT | 11/6/2026 · 323 | 31 route: auth 5 (có OTP), lỗi 5, dashboard, tasks, users, chats, apps, settings 5, help center | Vite, React 19, TanStack Router |
| Dashboard | **next-shadcn-dashboard-starter** (`Kiranism/…`) | 7,1k · MIT | 25/8/2026 · 434 | 28 `page.tsx`: overview, CRUD sản phẩm, users, kanban, chat, billing, 4 form, workspaces | Next 16, React 19, Clerk |
| Dashboard | **Tremor Blocks** (`tremorlabs/tremor-blocks`) | 545 · MIT | **22/1/2025 · 3** | 323 file block trong 28 nhóm: page shell 6, KPI card, bảng, form layout, billing, login, onboarding | Next.js, Tailwind |
| Dashboard | **Tremor** (`tremorlabs/tremor`) | 3,7k · Apache-2.0 | **10/10/2025** · 84 | 39 component (8 loại chart, Tracker, BarList), không có trang | React 18, Recharts 2 |
| Dashboard | **TailAdmin free** (`TailAdmin/free-react-tailwind-admin-dashboard`) | 1,3k · MIT | 15/9/2026 · 90 | 18 trang, chỉ 1 dashboard (ecommerce); bản Pro mới có 7 dashboard | Vite, React 19 |
| Dashboard | **Flowbite Admin Dashboard** (`themesberg/flowbite-admin-dashboard`) | 2,9k · MIT | **20/3/2025** · 89 | 17 trang: auth 5, CRUD 2, layout sidebar/stacked, 404/500, pricing, settings | Hugo, HTML |
| Dashboard | **Refine** (`refinedev/refine`) | 35,9k · MIT | 10/9/2026 · 7.607 | Framework CRUD; 281 thư mục examples, 6 `template-*` (antd, mui, mantine, chakra, headless…), app CRM | React + UI kit tùy chọn |
| Mobile RN | **React Native Reusables** (`founded-labs/react-native-reusables`) | 8,7k · MIT | 27/9/2026 · 1.212 | 32 component (bản NativeWind và Uniwind), 7 block auth (mỗi block có bản Clerk) | React Native, Expo |
| Mobile RN | **Tamagui + Bento** (`tamagui/tamagui`, `code/bento`) | 14,3k · MIT | 17/10/2026 · 18.926 | ~70 file Bento: shell 6 (sidebar, top nav, tab bar, drawer), form layout 5, list 10, ecommerce 4; trang Bento nay ghi "Free, forever" | RN + web |
| Mobile RN | **gluestack-ui v3** (`gluestack/gluestack-ui`) | 5,3k · MIT (chỉ trong `packages/gluestack-ui/LICENSE`, gốc repo không có LICENSE) | 2/9/2026 · 16.582 | 61 component, 3 màn showcase, 4 starter kit (Expo, Expo + Uniwind, monorepo, Next) | RN + web, NativeWind |
| Mobile RN | **NativeWind** (`nativewind/nativewind`) | 8,1k · MIT | 16/10/2026 · 3.373 | Không có layout; lớp Tailwind cho RN mà RNR và gluestack dựa vào (v4 ổn định, v5 RC) | RN |
| Flutter | **flutter/samples** | 19,3k · BSD-3 | 8/10/2026 · 1.925 | Mẫu chính thức; liên quan layout: `material_3_demo`, `cupertino_gallery`, `platform_design`, `compass_app`, `navigation_and_routing` | Flutter |
| Flutter | **Best-Flutter-UI-Templates** (`mitesh77/…`) | 22,8k · MIT | 16/12/2025 · 122 | 5 app demo (hotel booking, fitness, course, drawer, intro animation), 52 file dart, không kiến trúc | Flutter |
| Flutter | **Flutter Responsive Admin Panel** (`abuanwar072/…`) | 7,1k · MIT | 28/7/2026 · 65 | 1 layout responsive (side menu + dashboard), 17 file dart | Flutter |
| Hướng dẫn | **Material 3 canonical layouts** | – | – | 3 layout: list-detail (`ListDetailPaneScaffold`), supporting pane (`SupportingPaneScaffold`, 70/30 ở màn rộng), feed (`LazyVerticalGrid` + `GridCells.Adaptive`) | Compose |
| Hướng dẫn | **Apple HIG: Layout** | – | – | Chọn layout theo size class (không theo thiết bị/hướng xoay), tôn trọng safe area, đổi tab bar sang sidebar khi rộng | SwiftUI/UIKit |
| Cảm hứng | **Mobbin** | – · thương mại | – | Thư viện ảnh chụp app thật, không có mã; Pro khoảng $10/tháng trả theo năm **(chưa xác minh từ trang giá, bị chặn)** | – |

### 7h.2 Điều đã kiểm và rủi ro cần biết

- **License không thuần MIT:**
  - Preline dùng hai license song song; phần Fair Use cấm làm "competing products" và cho tác giả quyền chấm dứt (đã đọc `LICENSE` trong clone).
  - Template `once-ui-system/magic-portfolio` là **CC BY-NC 4.0**, cấm dùng thương mại, dù thư viện core là MIT (đã đọc `LICENSE`).
  - Tremor dùng Apache-2.0 cho component nhưng MIT cho repo blocks.
- **Miễn phí trên README, trả phí khi cần trang hoàn chỉnh:** Preline (bản Pro 740 block theo README), Flowbite Blocks, daisyUI store, TailAdmin Pro. Bản miễn phí của các bộ này thường chỉ là component, không phải trang.
- **Ngừng cập nhật:** Tremor Blocks (3 commit, cuối 1/2025), Tremor (10/2025, còn React 18 + Recharts 2), Flowbite Admin Dashboard (3/2025). Vercel mua Tremor 22/1/2025 và mở miễn phí blocks; từ đó gần như không có commit.
- **Tailwind Plus:** Tailwind Labs về Shopify ngày 9/9/2026, ngừng nhận khách mới cho Tailwind Plus; Tailwind CSS vẫn MIT. Nguồn là nhiều bài báo cùng thuật lại bài "Tailwind Labs is joining Shopify" của Adam Wathan; trang tailwindcss.com/plus chỉ hiện form đăng nhập nên **chưa xác minh từ trang chính thức**.
- **Flutter:** gói `flutter_adaptive_scaffold` đã bị đánh dấu discontinued trên pub.dev (0.3.3+1); layout list-detail thích ứng phải tự dựng bằng `LayoutBuilder` / `NavigationRail` **(chưa xác minh có gói thay thế chính thức)**.
- **Breakpoint Material 3:** compact < 600dp, medium 600–839dp, expanded ≥ 840dp, theo tài liệu adaptive của Android; trang m3.material.io trả 404 khi đọc nên **chưa đối chiếu được trên m3**.
- **Apple HIG:** không đưa số margin cố định cho iOS. Số cụ thể có cho tvOS (safe area 60pt trên/dưới, 80pt hai bên) và visionOS (tâm nút cách nhau ≥ 60pt).

### 7h.3 Chọn theo loại sản phẩm

| Cần | Nên lấy | Ghi chú |
|---|---|---|
| Trang marketing / landing | **HyperUI** (106 block marketing, MIT); dự án Next.js thêm **Once UI core** | Tránh Preline nếu không chấp nhận Fair Use; Tailwind Plus không mua được nữa |
| SaaS dashboard | Khung từ **shadcn/ui blocks** (`npx shadcn add dashboard-01`, `sidebar-07`…) + starter **shadcn-admin** (Vite) hoặc **next-shadcn-dashboard-starter** (Next 16) | Tremor Blocks để tham khảo KPI/chart/billing, không làm nền vì đã ngừng; nhiều CRUD thì cân nhắc **Refine** |
| App mobile React Native | **React Native Reusables** (cùng triết lý shadcn) trên NativeWind/Uniwind; cần shell (tab bar, drawer) thì thêm **Tamagui Bento** | gluestack-ui là phương án thay thế nhiều component hơn |
| App mobile Flutter | **flutter/samples** (`material_3_demo`, `cupertino_gallery`, `compass_app`) + Material 3 canonical layouts | Best-Flutter-UI-Templates chỉ để tham khảo giao diện |
| Chuẩn layout thích ứng | **Material 3 canonical layouts** và **Apple HIG: Layout** | Dùng làm quy ước breakpoint và chuyển tab bar ↔ sidebar |
| Cảm hứng màn hình thật | Mobbin | Chỉ là ảnh, không có mã hay license để tái sử dụng |

Liên hệ với các mục khác: layout chỉ là khung; giá trị màu, khoảng cách và "gu" lấy từ design system (§1, §7f) và skill (§7g). Muốn agent dựng trang từ các block này mà không ra giao diện "khuôn", ghép với cổng đo (§7d) hoặc detector (Impeccable, mục 20).

**Nguồn §7h:** clone 18/10/2026 (`git clone --filter=blob:none`, đếm bằng `git ls-tree` trên HEAD): github.com/{shadcn-ui/ui, markmead/hyperui, once-ui-system/core, once-ui-system/magic-portfolio, htmlstreamofficial/preline, themesberg/flowbite, themesberg/flowbite-admin-dashboard, saadeghi/daisyui, satnaing/shadcn-admin, Kiranism/next-shadcn-dashboard-starter, tremorlabs/tremor, tremorlabs/tremor-blocks, TailAdmin/free-react-tailwind-admin-dashboard, refinedev/refine, founded-labs/react-native-reusables, tamagui/tamagui, gluestack/gluestack-ui, nativewind/nativewind, flutter/samples, mitesh77/Best-Flutter-UI-Templates, abuanwar072/Flutter-Responsive-Admin-Panel-or-Dashboard} (README, LICENSE, package.json; số sao từ trang GitHub cùng ngày) · ui.shadcn.com/blocks · blocks.tremor.so · tamagui.dev/bento · daisyui.com/store · pub.dev/packages/flutter_adaptive_scaffold · tailwindcss.com/plus (chỉ form đăng nhập) · cmswire.com/digital-experience/shopify-acquires-tailwind-labs-to-secure-css-framework · vktr.com/digital-experience/shopify-acquires-tailwind-labs-to-secure-css-framework · pulse2.com/shopify-acquires-tailwind-labs-as-tailwind-css-tops-110-million-weekly-installs · witscode.com/blogs/shopify-acquires-tailwind-labs-what-was-announced · developer.android.com/develop/ui/compose/layouts/adaptive/canonical-layouts · m3.material.io/foundations/layout/canonical-layouts/overview (404) · developer.apple.com/design/human-interface-guidelines/layout (đọc qua developer.apple.com/tutorials/data/design/human-interface-guidelines/layout.json) · mobbin.com/pricing (403; giá theo toolradar.com, pricingsaas.com)

## 7i. Kiểm ảnh: miqdadbadjuber/anti-slop ("antislop"), bộ luật lọc "AI slop" cho UI, nội dung và code (ảnh người dùng gửi, 2026-10-19)

> Ảnh là phần đầu README trên trình duyệt: logo "/antislop", huy hiệu Trendshift "#2 Repository Of The Day" và "#13 Repository Of The Week" (JavaScript), các huy hiệu "license MIT", "version v3.2.20", "Skills 29.7K", tiêu đề "Anti Slop: Rules for AI Coding Agents", câu "A filter, not a style guide", và chữ phủ "THIS FREE RULEBOOK" do người đăng lại thêm vào. Đã clone toàn bộ repo (119 commit), đọc 6 skill, tự chạy script kiểm và smoke test của repo, rồi đối chiếu các con số với Trendshift, skills.sh và npm.

### 7i.1 Hồ sơ nhanh

| Mục | Thông tin (đọc 19/10/2026) |
|---|---|
| Repo | `miqdadbadjuber/anti-slop` · trang GitHub **~6,5k★**, 457 fork, 1 issue mở · **MIT** (© 2026 Miqdad Badjuber) · tag mới nhất **v3.2.21** · 119 commit, 7/8 → 16/10/2026 |
| Tác giả | Miqdad Badjuber (Indonesia, 110 follower, 6 repo công khai, đây là repo duy nhất có sao). 95/119 commit từ ba tên/tài khoản của tác giả; Fajar Hidayat 17 commit |
| Phân phối | `npx antislop-ai` (trình cài hỏi skill, phạm vi, agent) · `npx skills add miqdadbadjuber/anti-slop` · plugin cho Claude Code, Codex, Cursor, Antigravity, Kimi, Cline, Oh My Pi, Pi · file đơn `antislop.md` để dán vào chat. npm `antislop-ai`: **9.992** lượt tải 17/9–16/10/2026 |
| Bên trong | 6 skill: `antislop` (lõi, 724 dòng), `antislop-ui` (311), `antislop-copywriting` (372), `antislop-layoutmobile` (170), `antislop-code` (128, chỉ sửa comment), `antislop-human` (150, kèm `contrast-check.py` và MCP tính tương phản). Lõi có **38 luật R-01…R-38** chia 3 tầng: Hard Gate, Purpose-Gate, Quality Locks; cộng 5 chuẩn "Craftsmanship" và "Delivery Gate" trước khi giao |
| Tác động lên máy | Plugin Claude Code tự khởi động MCP `antislop-contrast` (Node gọi Python chạy `contrast-mcp.py`, stdio). Trình cài chép thư mục skill và ghi một khối có dấu `<!-- antislop:start/end -->` vào `CLAUDE.md` hoặc `AGENTS.md`; lưu chế độ ở `~/.config/antislop/settings.json` |

### 7i.2 Kiểm từng ô trong ảnh

| Ô trong ảnh | Kiểm | Ghi chú |
|---|---|---|
| "#2 Repository Of The Day" (Trendshift, JavaScript) | ✅ | Trang trendshift.io/repositories/137042: hạng 12, 6, **2**, 22 các ngày 7–10/10/2026, ngoài ra "not trending". Là thứ hạng một ngày trong nhóm JavaScript |
| "#13 Repository Of The Week" | ✅ | Có huy hiệu Weekly #13, trang không ghi ngày |
| "license MIT" | ✅ | `LICENSE` MIT; npm `antislop-ai` cũng ghi MIT |
| "version v3.2.20" | ⚠️ cũ | Hiện là **v3.2.21** (tag, `package.json`, npm) |
| "Skills 29.7K" | ⚠️ cũ, dễ hiểu sai | skills.sh nay ghi **32,0K**, là **tổng lượt cài của 6 skill** (từ 4,9K đến 6,3K mỗi skill), không phải số người dùng. Các skill có số gần bằng nhau, khớp với việc trình cài chép cả bộ một lần |
| "A filter, not a style guide: no prescribed colors, fonts, or layouts" | ✅ có lưu ý | Luật không chỉ định màu hay font. R-06 nêu tên "danh sách mặc định" (Inter, Geist, Space Grotesk…) nhưng ghi rõ "None are banned", chỉ yêu cầu ghi lý do. Tuy vậy, phần cảnh báo có đánh dấu một số lựa chọn bố cục phổ biến là dấu hiệu slop khi dùng mặc định: bento grid, dải logo "Trusted by", footer 4 cột, thẻ giá "Most Popular", icon Lucide |
| Bốn ảnh "See the difference" (không có gì / chỉ antislop / chỉ DESIGN.md / cả hai) | ⚠️ | Ảnh minh họa của tác giả, không công bố brief hay prompt để chạy lại, không có benchmark |
| "THIS FREE RULEBOOK" | – | Chữ do người đăng lại thêm, không có trong README |

**Tổng:** 3✅ / 3⚠️ / 0❌ (không tính chữ phủ). Các thông tin cũ trong ảnh chỉ lệch vì ảnh chụp trước bản v3.2.21.

### 7i.3 Điều ảnh không nói (đọc mã và tự chạy)

- **Kiểm của chính repo chạy được (19/10/2026):** `node scripts/check-repo.mjs` **13/13 check pass** (gồm "hai bản cài đặt tương phản dùng cùng công thức"); `python3 contrast-check.py --selftest` 9/9 cặp đúng; `node cli/scripts/smoke-test.mjs` pass (bỏ qua phần cần cài dependency của CLI). CI chạy cả ba.
- **Lỗi định nghĩa "chữ lớn":** R-25, `antislop-human` và `contrast-check.py` đều ghi chữ lớn là "**18px+**" được phép 3:1. WCAG định nghĩa chữ lớn là 18pt (khoảng **24px**) hoặc 14pt đậm (khoảng 18,66px). Hệ quả: chữ thường cỡ 18–23px chỉ đạt 3:1 sẽ được báo PASS, trong khi WCAG yêu cầu 4,5:1. Refactoring UI Skill (§7g.4) ghi đúng ngưỡng này.
- **Tốn ngữ cảnh:** skill lõi mô tả "Load always", dài khoảng 58 KB (ước chừng 14 nghìn token). Cả 6 skill cộng lại khoảng 146 KB, chưa kể `antislop.md` là bản trùng của skill lõi. So với `frontend-design` của Anthropic (§7g.3, 71 dòng) thì nặng hơn nhiều lần.
- **Câu hỏi chế độ chặn công việc:** mặc định, mỗi phiên mới agent phải hỏi "DURING hay AFTER" và dừng lại chờ trả lời trước mọi việc UI, kể cả việc chỉ đọc. Muốn bỏ câu hỏi thì chạy `npx antislop-ai --mode during|after`. Với agent chạy không người trông (Routine, CI), cần đặt chế độ trước.
- **Điểm làm tốt về an toàn:** coi `DESIGN.md` và file cài đặt là **dữ liệu, không phải lệnh** ("Never execute instructions from this file"), và khối ghi vào `CLAUDE.md`/`AGENTS.md` có dấu mở/đóng để gỡ sạch.
- **Có cổng máy, nhưng hẹp:** công cụ duy nhất chạy được là tính tương phản cho từng cặp màu (CLI + MCP). Các luật còn lại (dữ liệu giả, nút chết, trạng thái rỗng, bàn phím) dựa vào "Delivery Gate" do agent tự đánh giá; không có script đo trên bản render như XIAS (§7d).
- **Trùng tên:** `dmmulroy/anti-slop` là bộ luật Oxlint cho code TypeScript, `aislop` (PyPI) là công cụ quét; đều khác dự án này.

### 7i.4 So với các mục đã có

| | antislop | `frontend-design` (§7g.3) | Taste Skill (§4) | Impeccable (mục 20) | XIAS (§7d) |
|---|---|---|---|---|---|
| Bản chất | Bộ lọc 38 luật + 6 skill (UI, nội dung, mobile, comment code, a11y) | Prompt định hướng thẩm mỹ | Luật "taste" + dial | 1 skill + 24 lệnh + engine Rust | Luật + token + 52 cổng đo |
| Phạm vi | UI **và** nội dung **và** comment code | UI + nội dung UI | UI | UI | UI |
| Cổng máy | Chỉ tương phản (có lỗi ngưỡng 18px) | Không | Không | 59 rule tất định ở hook | Đo trên trình duyệt thật |
| Chi phí ngữ cảnh | Cao (~14k token lõi) | Thấp (~70 dòng) | Trung bình | Trung bình | Cao (CLAUDE.md 319 dòng) |

Điểm riêng của antislop là **phạm vi**: cùng một bộ luật cho giao diện, văn bản marketing và comment trong code; và cách tách rõ "lọc" (antislop) với "định hướng" (`DESIGN.md`), khớp với cách §7c khuyên viết DESIGN.md riêng cho brand.

### 7i.5 Dùng thế nào

- **Chọn từng phần:** `antislop-copywriting` và `antislop-code` (chỉ sửa comment) đáng thử nhất vì ít bộ khác phủ. Với UI, nếu đã dùng `frontend-design` thì không nên nạp thêm cả lõi 58 KB; lấy danh sách dấu hiệu trong `antislop-ui` làm checklist review là đủ.
- **Sửa ngưỡng chữ lớn** trước khi dùng `contrast-check.py` làm cổng: dùng 24px thường hoặc 18,66px đậm.
- **Đặt chế độ trước** (`npx antislop-ai --mode during`) cho phiên tự động, để agent không dừng lại hỏi.
- **Ghép với cổng đo thật** (XIAS §7d hoặc detector Impeccable) nếu cần chặn lỗi trước khi merge, đúng bài học §4.
- **Không đọc số "Skills 29.7K/32K" là số người dùng:** đó là tổng lượt cài của 6 skill.

**Nguồn §7i:** https://github.com/miqdadbadjuber/anti-slop (clone đủ, 119 commit, HEAD 439a2ef 16/10/2026, tag v3.2.21; README.md, GUIDE.md, ROADMAP.md, LICENSE, package.json, `.claude-plugin/{plugin.json,marketplace.json,contrast-mcp-launcher.mjs}`, `skills/*/SKILL.md`, `skills/antislop-human/{contrast-check.py,contrast-mcp.py}`, `cli/lib/{install,settings}.mjs`, `.github/workflows`; tự chạy 19/10/2026: `check-repo.mjs` 13/13, `contrast-check.py --selftest` 9/9, `smoke-test.mjs` pass) · trang GitHub 19/10/2026 (~6,5k★, 457 fork) · https://github.com/miqdadbadjuber (Indonesia, 110 follower) · https://trendshift.io/repositories/137042 (Daily #2 ngày 9/10/2026, Weekly #13, +6.083★/61 ngày) · https://skills.sh/miqdadbadjuber/anti-slop (32,0K tổng lượt cài, 6 skill) · api.npmjs.org `antislop-ai` (9.992, 17/9–16/10/2026; tạo 15/8/2026) · ssdnodes.com/learn/anti-slop-skill-for-coding-agents · skillsllm.com/skill/miqdadbadjuber-anti-slop · betterstack.com/community/guides/ai/anti-slop-oxlint (dự án trùng tên `dmmulroy/anti-slop`) · pypi.org/project/aislop · https://www.w3.org/TR/WCAG22/#dfn-large-scale (định nghĩa chữ lớn)

### 7i.6 Đọc lại 3/11/2026: ảnh thứ hai là bản v3.2.18 đã cũ

Người dùng gửi thêm một ảnh phần đầu README: logo "/antislop", huy hiệu "license MIT", "version **v3.2.18**", "Skills **19.0K**", "**38 mandatory rules** (R-01 to R-38)", Liveliness Toolkit (ENERGY/RHYTHM/MOTION), Delivery Gate, additive skills. Đối chiếu với clone đủ lịch sử, HEAD `941b1532f9cc8ffde766bca5921d75257c9e5762` (1/11/2026, tag v3.2.25, 139 commit):

| Ô trong ảnh | Kết quả | Hiện tại |
|---|---|---|
| "version v3.2.18" | ⚠️ cũ | v3.2.18 là commit `a56a8a7` ngày 26/9/2026. Sau đó đã có bảy tag nữa, tới v3.2.25 ngày 1/11/2026 |
| "38 mandatory rules (R-01 to R-38)" | ⚠️ cũ | README và `skills/antislop/SKILL.md` nay ghi **40 luật (R-01 đến R-40)**. v3.2.24 (28/10) đưa ngữ nghĩa trợ năng và cơ chế hiệu năng thành luật Hard Gate |
| "Skills 19.0K" | ⚠️ cũ | §7i.2 đã ghi 29,7K rồi 32,0K. Đây vẫn là tổng lượt cài của 6 skill, không phải số người dùng |
| "license MIT" | ✅ | `LICENSE` MIT, © 2026 Miqdad Badjuber |
| Mô tả "filter, not a style guide", `DESIGN.md` cung cấp định hướng (R-37) | ✅ | Không đổi |

**Những gì đã đổi từ 16/10 (`439a2ef..941b153`, 35 file, +1.106/−139 dòng):** sửa trình cài đặt (không ghi con trỏ khi chạy từ thư mục home; gói npm có kèm README và LICENSE; yêu cầu Node 20.12), khai báo capability `skills` cho plugin Cline, đánh dấu Roo là "not planned" vì dự án Roo đã archive, và ghi rõ trong README rằng `DESIGN.md` là bắt buộc. Lõi `skills/antislop/SKILL.md` nay dài 53,7 KB (trước đây khoảng 58 KB). Vẫn là file "load always".

**Vẫn chưa sửa (tự kiểm tại `941b153`):** định nghĩa chữ lớn vẫn ghi "**18px+**" ở `skills/antislop/SKILL.md:289`, `antislop.md:334`, `skills/antislop-human/SKILL.md:26,65` và `contrast-check.py:10`. WCAG định nghĩa chữ lớn là 18pt, tức 24px, hoặc 14pt đậm, tức khoảng 18,66px (xem §7i.3). Câu hỏi "DURING hay AFTER" vẫn là mặc định ở dòng 58–59 của SKILL.md lõi. 8.025★ (3/11/2026, GitHub search API).

**Nguồn §7i.6:** ảnh người dùng gửi 3/11/2026 · clone https://github.com/miqdadbadjuber/anti-slop HEAD `941b1532f9cc8ffde766bca5921d75257c9e5762` (`git log 439a2ef..HEAD`, `git tag`, README.md, LICENSE, `skills/antislop/SKILL.md`, `skills/antislop-human/{SKILL.md,contrast-check.py}`, `antislop.md`) · GitHub search API `user:miqdadbadjuber` 3/11/2026.

## 7j. Hồ sơ: Leonxlnx/taste-skill (Taste Skill) — skill chống "AI slop" có inspector chạy trên trình duyệt thật (bổ sung hồ sơ, clone 2026-10-19)

> §4 và bảng §1–§6 nhắc Taste Skill nhiều lần nhưng chưa có hồ sơ riêng; §7g.5 còn để ngỏ câu "mô tả GitHub mới có browser check (chưa xác minh)". Mục này clone đầy đủ, đọc skill và **tự chạy** để chốt: inspector trên trình duyệt thật là có thật.

### 7j.1 Hồ sơ nhanh

| Mục | Thông tin (đọc 19/10/2026) |
|---|---|
| Repo | `Leonxlnx/taste-skill` · **~98,9k★**, 6,7k fork · **MIT** (© 2026 Leonxlnx) · tag mới nhất **v2.1.2** (19/10/2026) · 239 commit, 19/2 → 19/10/2026 |
| Tác giả | Leonxlnx (Leon Lin). Commit: Leonxlnx 144 + Leon Lin 61 (cùng người), **Cursor Agent 9** → một phần do agent viết. Có trang `tasteskill.dev`, app `tastecode.dev`, nhà tài trợ (React Bits, IMG.LY…) |
| Phân phối | Agent Skills (tương thích Codex/Cursor/Claude, chuẩn `vercel-labs/agent-skills`); `.claude-plugin/`, `.codex-plugin/`, `install.sh`, `skill.sh`. Cũng có **TasteCode** — app desktop đóng gói skill kèm design agent (README ghi free, OSS) |
| Bên trong | 13 thư mục skill. Chính là **`taste-skill`** (`design-taste-frontend`, `SKILL.md` 529 dòng) + `taste-skill-v1` (227), `taste-skill-v2-experimental` (1.229); các biến thể phong cách `brutalist`/`minimalist`/`soft`; `stitch-skill`, `redesign-skill`, `brandkit`, `image-to-code`, `imagegen-frontend-{web,mobile}`, `gpt-tasteskill` |

### 7j.2 Cách hoạt động (đọc `skills/taste-skill/`)

Skill chính không chỉ là lời khuyên; nó có **ba script không phụ thuộc gói ngoài** và một thư viện dữ liệu:

- **`scripts/draw.mjs` (584 dòng)** — "chia bài" hướng thiết kế: theo `--sector` và `--idea`, rút 3 trong **20 hướng** rồi rút tiếp type/palette/hero/section từ thư viện, in ra một "direction sheet". Thư viện (`library/*.json`): 20 directions, 58 heroes, 185 sections, 56 palettes, 44 type, 202 sites, 18 motions — README nói chưng cất từ **một nghiên cứu 247 site** (One Page Love, Awwwards SOTD); thư viện đóng gói 202 (chênh 247 vs 202 là study vs bản đóng gói).
- **`scripts/inspect.mjs` (303 dòng) + `scripts/lib/cdp.mjs`** — **inspector trình duyệt thật**: điều khiển Chrome/Edge/Chromium qua **CDP (DevTools Protocol), không cần Playwright/Puppeteer**, Node 22+. Mở trang ở 1440/768/390px, đo (số dòng tiêu đề, cỡ chữ, font thật đang dùng), ghi `FAIL`/`WARN` và lưu screenshot vào `.taste-skill/inspect/`. Vòng "look-and-fix": agent đọc screenshot, sửa, đo lại.
- **`scripts/lint.mjs` (119 dòng, Node 18+)** — phương án không có Chrome: lint tĩnh "house style" (cấm hairline, v.v.).

**Tự chạy (19/10/2026):** `tests/skill_test.sh` pass; `node --check` cả 5 script OK; `node scripts/draw.mjs --sector saas --idea "…"` in ra direction sheet đầy đủ; `node scripts/lint.mjs` chạy và bắt 6 lỗi hairline trong CSS demo của repo. Tức phần "chia bài" và "lint" chạy được ngay; inspector cần Chrome nên chưa chạy trong sandbox, nhưng mã dùng CDP là thật (chưa chạy end-to-end **tại đây**).

### 7j.3 Vì sao đáng chú ý, và so với các mục đã có

- **Đây là một trong số ít skill "taste" có cổng đo trên bản render thật** — đúng bài học §4. Khác `frontend-design` của Anthropic (§7g.3, chỉ prompt, không cổng) ở chỗ có inspector + vòng screenshot; khác XIAS (§7d) và Impeccable (mục 20) ở chỗ cổng của nó **không cần cài gói** (CDP thuần), nhẹ hơn Playwright.
- **Điểm mạnh riêng:** thư viện hướng thiết kế rút từ nghiên cứu site thật, "chia bài" buộc agent chọn hướng thay vì mặc định; cảnh báo ngay trong skill rằng "bỏ trang trí mà không thêm chất" sẽ ra trang mỏng (một lỗi các skill chống-slop khác hay mắc).
- **Lưu ý:** skill chính 529 dòng + 11 reference + thư viện JSON → tốn ngữ cảnh; có hệ sinh thái thương mại quanh (TasteCode, website, tài trợ) nên đọc README cần tách phần OSS khỏi phần quảng bá. Con số sao nhảy mạnh (kho từng ghi ~46k "theo listing", nay ~98,9k).

### 7j.4 Dùng thế nào

- Lấy cả bộ `taste-skill` nếu muốn cổng đo trên trình duyệt mà không cài Playwright (chỉ cần Chrome/Edge sẵn có + Node 22). Không có Chrome thì `lint.mjs` là mức tối thiểu.
- Đã dùng `frontend-design` rồi thì cân nhắc chỉ mượn `inspect.mjs` + house rules, tránh nạp trùng hai bộ luật lớn.
- Bỏ qua các biến thể `*-experimental` (1.229 dòng) trừ khi cần; dùng bản `taste-skill` ổn định.

**Nguồn §7j:** https://github.com/Leonxlnx/taste-skill (clone đầy đủ, 239 commit, HEAD b9ca2fd 19/10/2026, tag v2.1.2; README.md, LICENSE (MIT), CHANGELOG.md, `skills/taste-skill/SKILL.md` + `references/` + `library/*.json` + `scripts/{draw,inspect,lint,scenes,assets}.mjs` + `scripts/lib/{cdp,probe,rules,app-draw}.mjs`; tự chạy `tests/skill_test.sh`, `node --check`, `draw.mjs`, `lint.mjs` 19/10/2026) · trang GitHub 19/10/2026 (~98,9k★, 6,7k fork) · github.com/Leonxlnx/taste-skill/releases (v2.1.0/2.1.1/2.1.2 18–19/10) · tasteskill.dev · tastecode.dev · github.com/vercel-labs/agent-skills

## 7k. Hồ sơ: nexu-io/open-design (OpenDesign) — "workspace agent thiết kế" local-first, Apache-2.0 (bổ sung hồ sơ, clone 2026-10-19)

> **Đính chính 31/10/2026:** đọc mã sâu ở §7q.0 cho thấy telemetry **nội dung** (prompt, phản hồi) bật mặc định, chẩn đoán tự động tải log `~/.claude`/`~/.codex`, và mọi agent chạy với cờ bỏ kiểm quyền. Nhận định "local-first thật, PRIVACY rõ" bên dưới cần đọc kèm §7q.0.
>
> §2 liệt kê OpenDesign (~102k★) nhưng chưa đọc mã. Mục này clone đầy đủ (blob:none), đọc README, `package.json`, `PRIVACY.md`, `CHANGELOG.md`, catalog design-system và lịch sử commit.

### 7k.1 Hồ sơ nhanh

| Mục | Thông tin (đọc 19/10/2026) |
|---|---|
| Repo | `nexu-io/open-design` (open-design.ai) · **~102k★** trang GitHub, 11,7k fork (aggregator chậm hơn: 76k–91k ở sourcepulse/dev.co, 7–9/2026) · **Apache-2.0** · v0.25.1 · **3.764 commit**, từ **28/4/2026** · monorepo pnpm |
| Nguồn gốc tên | Commit #1 (28/4/2026) đổi tên từ **"Open Claude Design" → "Open Design"**; tự định vị là "bản mã mở thay cho Claude Design" (mer.vin, worldofai). Tức là một **alternative tới một sản phẩm thiết kế của Anthropic**, không phải của Anthropic |
| Tác giả | lefarcen 552, PerishFire 204, Ray Xi 185… + **nhiều bot/agent**: `open-design-crew[bot]` 191, `open-design-bot` 160, `Cursor Agent` 116 → một phần đáng kể do agent/bot viết |
| Là gì | App desktop + web **local-first**: viết brief → agent coding (hoặc OpenDesign Cloud) dựng prototype theo design system của bạn. **Studio**: prototype (preview trực tiếp), slides, sinh ảnh, **HyperFrames** (motion → MP4). Nối coding agent qua **skills/CLI/MCP** + adapter runtime (Claude Code, Codex, DeepSeek Harness/Reasonix, Cursor, Gemini…) |
| Thương mại | **OpenDesign Cloud / Go** trả phí (credit; trang ghi "$8 tháng đầu, tới $120/tháng credit"). Workflow project local chạy được khi không có telemetry |

### 7k.2 Điều đã đọc

- **151 gói design-system** (`design-systems/<slug>/`: `manifest.json` + `DESIGN.md` + `tokens.css` + bản dịch `DESIGN-*.md` nhiều thứ tiếng). Mỗi gói có `source/evidence.md` **ghi trung thực**: "derived from curated OpenDesign bundled fixture… does not claim a fresh crawl of the original upstream brand repository or website". Slug mang tên thương hiệu (Airbnb, Apple, Binance, BMW, Bugatti…) — lưu ý nhãn hiệu như §7d/§7g.5, nhưng ở đây có file provenance kèm, minh bạch hơn.
- **Telemetry (`PRIVACY.md`):** hai lớp — *product analytics* bật mặc định, opt-out qua banner lần chạy đầu và Settings → Privacy; *safety/reliability* luôn bật trong build có telemetry destination (không tắt được bằng toggle chung). **Fork/bản build không có credential telemetry thì không gửi gì.** Minh bạch hơn trường hợp browser-use (mục 11 §1c) vì có trang PRIVACY mô tả rõ và tắt được lớp analytics.
- **Quy mô & nhịp:** 13.557 file, 3.764 commit trong ~6 tháng, release note 0.9.0 khoe "310 PR · 88 contributor · 7 ngày". Tốc độ rất cao, nhiều do agent.

### 7k.3 So sánh và đánh giá

- **So với design tool mở khác (§2):** Penpot/Excalidraw/tldraw là canvas thiết kế; OpenDesign là **workspace điều phối agent** (brief → prototype/slide/ảnh/motion), gần FigCraft (§7e) và các "crafting app" hơn về ý tưởng, nhưng rộng hơn và có tầng Cloud trả phí.
- **Điểm mạnh:** Apache-2.0, local-first thật (dữ liệu + BYOK key ở máy), nhiều adapter agent, catalog design-system có provenance, PRIVACY rõ. Hợp để tham khảo cách **đóng gói design system cho agent** (manifest + DESIGN.md + tokens.css) và cách nối nhiều coding agent qua MCP/CLI/runtime.
- **Rủi ro cần đọc kỹ:** repo **rất lớn, chưa audit mã sâu** (hồ sơ này ở mức README+manifest+privacy); phần lớn giá trị thực nằm sau tầng Cloud trả phí; số sao tăng cực nhanh cho một repo 6 tháng tuổi (kiểm từ trang GitHub trực tiếp, aggregator còn ghi 76–91k); tên "Open(Claude)Design" và slug thương hiệu dễ gây nhầm về liên kết chính chủ.
- **Dùng thế nào:** thử bản OSS local trước khi mua credit; nếu chỉ cần mẫu đóng gói design-system cho agent thì đọc `design-systems/<slug>/` làm tham khảo (giữ evidence/provenance như họ làm); không coi 151 gói thương hiệu là tài sản dùng lại thương mại được mà không kiểm nhãn hiệu.

**Nguồn §7k:** https://github.com/nexu-io/open-design (clone blob:none đầy đủ lịch sử, 3.764 commit, HEAD 88b3d9931 19/10/2026, v0.25.1; đọc README.md, package.json (Apache-2.0, pnpm@10.33.2), PRIVACY.md, CHANGELOG.md (0.9.0), `design-systems/README.md` + `design-systems/airbnb/{manifest.json,source/evidence.md}`; `git log` commit #1 rename "Open Claude Design"→"Open Design") · trang GitHub 19/10/2026 (~102k★, 11,7k fork) · github.com/nexu-io · sourcepulse.org/projects/28859130 · dev.co/ai/frameworks/open-design (76k, 8/7/2026) · mer.vin/2026/05/open-design-explained-local-first-open-source-alternative-to-claude-design · jimmysong.io/ai/open-design

## 7l. Kiểm ảnh: Nutlope/hallmark (Hallmark), skill thiết kế "không trông như AI làm" của Together AI (ảnh README người dùng gửi, clone 2026-10-25)

> Ảnh là README của repo: "A design skill for Claude Code, Codex, Cursor and OpenCode that refuses to look AI-generated", 48 theme, có các chế độ redesign và audit, "Made by Together AI". Mục này clone đầy đủ lịch sử (HEAD `7ec8682`, 22/10/2026) và đọc `skills/hallmark/` (SKILL.md, references, scripts), `eval/`, `.claude-plugin/`, CI. **Không chạy script nào của repo.**

### 7l.1 Hồ sơ nhanh

| Mục | Thông tin (đọc 25/10/2026) |
|---|---|
| Repo | `Nutlope/hallmark` · **~33k★**, 1,7k fork (shields) · **MIT** ("Hallmark contributors") · site usehallmark.com |
| Lịch sử | 297 commit, 27/4 → 22/10/2026. Người viết chính là **Youssef** (282 commit); Hassan El Mghari (Nutlope, Together AI) 12 commit; 3 người khác mỗi người 1. **76 commit có trailer Claude.** Không tag, không release, không CHANGELOG |
| Phiên bản | `2.0.0`, nhưng là **đánh số lại**: trước đó đã lên 2.2 → 2.3 → 2.4.0 rồi đổi về 2.0.0 (commit `45d70b3`, 21/10) |
| Cài | `npx skills add nutlope/hallmark` · plugin marketplace (`.claude-plugin/marketplace.json`) · `node install.mjs` (chép vào `~/.claude/skills`, `~/.agents/skills` và `~/.config/opencode/skills`, **xóa thư mục đích cũ trước khi chép**) |
| Kích thước | Thư mục skill 6,9 MB (48 cặp theme `.md` + ảnh xem trước). SKILL.md 154 dòng (~4,5k token). Một lần build nạp ~120 KB tài liệu tham chiếu (**~30k token**). Repo 64 MB, chủ yếu vì 48 site demo trong `site/themes` (49 MB) |

### 7l.2 Kiểm từng câu trong ảnh

| Câu trong ảnh | Thực tế (đọc mã) | Kiểm |
|---|---|---|
| "forty-eight themes" | Đúng **48** theme trong `references/themes/` + `index.json`. Số theme đã đổi nhiều lần: 12 (27/4) → 22 (1/5) → 56 (1/10) → 49 → 48 (14/10). Bài viết bên ngoài ghi "22 theme" là số cũ | ✅ |
| "deals three themes" | `theme.mjs` chia bài **bằng thuật toán tất định**: chấm độ trùng từ khóa với prompt (từ hiếm nặng hơn), +2 nếu đúng genre, loại các theme của 3 lần gần nhất, phá hòa bằng sha256 của prompt + salt dự án + ngày, rồi lấy theme đứng đầu cùng hai theme khác biệt về nền và trục. Model chọn một trong ba | ✅ |
| "lints the result in a real browser" | `sloplint-render.mjs` dùng `puppeteer-core` điều khiển **Chrome có sẵn trên máy**, chạy headless ở 8 khổ (320 → 1920 px). Người dùng phải tự `npm i -g puppeteer-core` và có Chrome, repo không tự tải trình duyệt. **Thiếu hai thứ đó thì chỉ chạy tầng tĩnh** và ghi "notRun" | ⚠️ tùy chọn |
| Các dấu hiệu "máy làm" (eyebrow, chữ hoa giãn, một chữ tô màu, khung trống, tường ảnh, hero lệch màn hình, form đăng ký email cuối trang, form cảm ơn mà không gửi gì) | Đều có gate tương ứng. Eyebrow, chữ hoa giãn, hero lệch màn hình và form giả ở tầng Floor; chữ tô màu, khung trống, tường ảnh và email cuối trang ở tầng Reflex | ✅ |
| "A fresh-context reviewer gets the last word" | Có prompt `review-hero.md` và `review-finish.md`, chạy bằng **subagent trên Claude Code**. Codex không có subagent nên review **chạy ngay trong luồng** (chỉ ghi lại là đã làm vậy); OpenCode dùng `@general`. Builder tự chấm các bản sửa sau review | ⚠️ chỉ đúng trên Claude Code/OpenCode |
| "Floor never ships (… invented facts …)" | Gate 46a "invented facts" là **7 regex** bắt các câu như "10x faster", "trusted by N", "99.9%", "N+ users", và **chỉ báo WARN, không bao giờ FAIL**. Testimonial, logo khách hàng và số liệu case study không có máy kiểm | ❌ |
| Ba tầng Floor / Reflex / Finish | `gates.md` có 90 dòng gate: 39 Floor, 50 Reflex, 1 Ledger, cộng 26 mục kiểm Finish. Có **45 gate do máy kiểm hoàn toàn**; 9 gate chỉ để model tự chấm. Bảng tier được viết cứng trong `sloplint.mjs` | ✅ |
| Cursor trong danh sách host | `install.mjs` chép vào `~/.agents/skills` mà Cursor đọc được, nhưng **bảng hướng dẫn host trong `flow.md` không có cột Cursor** (chỉ một dòng ghi chú ngắn) | ⚠️ |

**Eval:** thư mục `eval/` là harness nội bộ, không đi kèm skill.

- Tầng B gửi skill làm system prompt tới GLM-5.2 và Kimi K2.7 qua **API Together**, kèm một bản chạy trên Claude với toàn bộ skill.
- Chấm bằng chính `sloplint` cộng một Claude chấm qua ảnh, tức là **tự chấm bài của mình**.
- Chỉ có một lần chạy (23/7/2026, 30 ô): 0 FAIL, điểm chấm 7–8/10.
- Không có nhóm đối chứng **không dùng skill**; kết quả chạy bị gitignore nên không tái lập được, và dùng số gate cũ trước v2. ROADMAP vẫn để ngỏ mục "Measure a build".

### 7l.3 Điều ảnh không nói (đọc mã)

- **Không telemetry, không analytics** trong skill. Không `curl | bash`, không `postinstall`, không hook tự chạy.
- Hook PostToolUse là **tùy chọn**: phải chạy `install-hook.mjs`, script này ghi đè `.claude/settings.json` một cách nguyên tử, và hook chỉ đưa lời khuyên chứ không chặn.
- **Ràng buộc với Together AI** chỉ có hai chỗ:
  - `imagegen.mjs` gọi `api.together.xyz` (FLUX.1.1-pro) **khi có `TOGETHER_API_KEY` và người dùng yêu cầu** sinh ảnh;
  - một dòng "Powered by Together AI" trong SKILL.md.
- **Trang sinh ra gọi bên thứ ba lúc người xem mở trang:**
  - cả 48 theme lấy font từ Google Fonts hoặc Fontshare (7 theme) qua CDN;
  - ảnh mặc định **hotlink từ Wikimedia** (`theme.mjs photos --save` mới tải về máy).
  - Với site châu Âu đây là vấn đề GDPR. Nên tự host font và ảnh trước khi phát hành.
- **License ảnh:** thư viện `photos.json` có 755 ảnh Commons: 547 CC BY-SA, 113 CC BY, 73 CC0, 23 public domain.
  - Ảnh **CC BY-SA đòi ghi nguồn và chia sẻ cùng giấy phép**; skill không nhắc nghĩa vụ này.
  - Repo cũng kèm 122 ảnh Commons trong site demo, có ghi nguồn trên trang.
- Linter **cấm URL Unsplash, Pexels và pravatar**: không cho dùng ảnh stock "đặc trưng AI" hay avatar giả.

### 7l.4 So với các mục đã có

| | Hallmark | Taste Skill (§7j) | antislop (§7i) | `frontend-design` (§7g.3) | UI UX Pro Max (§7g.2) |
|---|---|---|---|---|---|
| Bản chất | Quy trình build trọn trang: chia 3 theme → dựng → lint → review | Luật "taste" + inspector | Bộ lọc 38 luật cho UI, nội dung và comment code | Prompt định hướng thẩm mỹ | Kho tra cứu style/palette |
| Cổng máy | `sloplint` (4,4k dòng) + render qua Puppeteer **nếu có Chrome**; 45 gate máy | Inspector chạy trên trình duyệt thật | Chỉ kiểm tương phản | Không | Không |
| Theme có sẵn | **48** (kèm ảnh xem trước và site demo) | Không, dùng dial | Không | Không | Rất nhiều style |
| Chi phí ngữ cảnh | Cao (~30k token mỗi lần build) | Trung bình | Cao (~14k token) | Thấp | Trung bình |
| Ràng buộc nhà cung cấp | Sinh ảnh qua Together (tùy chọn) | Không | Không | Không | Không |

Điểm riêng của Hallmark: **chọn theme bằng thuật toán tất định**, có loại theme vừa dùng, nên tránh được việc agent lần nào cũng chọn cùng một kiểu. Kèm theo đó là danh sách tell "máy làm" rất cụ thể (eyebrow, chữ hoa giãn, form giả…) được cài thành gate. Phần chặn thật vẫn phụ thuộc Chrome có trên máy và host có subagent.

### 7l.5 Dùng thế nào

- **Hợp:** landing page và trang marketing trên Claude Code, nơi chạy được cả subagent review lẫn Puppeteer. Cài `puppeteer-core` và Chrome trước, không thì mất tầng render.
- **Cẩn thận:**
  - Đừng coi gate 46a là chặn số liệu bịa, vì nó chỉ cảnh báo. Mọi con số và testimonial vẫn cần người kiểm.
  - Tự host font và ảnh; ghi nguồn ảnh CC BY và CC BY-SA.
  - Trên Codex, review không có ngữ cảnh mới; nên mở phiên riêng để review.
- **Dùng lại từng phần:** danh sách tell trong `gates.md` làm checklist review UI (gộp với antislop §7i); ý tưởng chia bài theme tất định trong `theme.mjs` cho agent khỏi lặp style.
- **Không cần** nếu dự án đã có design system riêng (§7f): khi đó dùng chế độ `audit` để chấm, không dùng chế độ build.

**Nguồn §7l:** clone đầy đủ github.com/Nutlope/hallmark 25/10/2026 (blob:none, 297 commit, HEAD 7ec8682 22/10/2026; README.md, ROADMAP.md, LICENSE, package.json, `.claude-plugin/marketplace.json`, `.github/workflows/verify.yml`, `skills/hallmark/{SKILL.md, references/{gates.md, flow.md, fonts.md, imagery.md, themes/*.md, themes/index.json}, scripts/{sloplint.mjs (check46 dòng 2017–2038), sloplint-render.mjs, theme.mjs, install.mjs, install-hook.mjs, lint-hook.mjs, imagegen.mjs, photos.json}}`, `eval/README.md`, git log về số theme và phiên bản) · img.shields.io/github/{stars,forks,license}/Nutlope/hallmark.json 25/10/2026 · usehallmark.com · bên thứ ba: dev.to/terminalchai/hallmark-together-ai-open-sources-an-anti-ai-slop-tool-for-web-design-3nkb · mer.vin/2026/05/hallmark-design-skill-anti-ai-slop-ui-for-claude-code-and-cursor · notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Hallmark · gittrend.io/repo/Nutlope/hallmark · mirror: github.com/xgaisystems/hallmark-Nutlope

## 7m. Kiểm infographic: "12 GitHub repo giúp Claude Code và Codex tạo giao diện đẹp hơn" (ảnh người dùng gửi, 2026-10-29)

> Infographic tiếng Việt liệt kê 12 repo UI/thiết kế cho Claude Code/Codex, mỗi ô một tên hiển thị + mô tả 1 dòng, **không kèm URL/owner**. Đã map từng ô về repo thật và đối chiếu số liệu trực tiếp qua API GitHub (đã xác thực, 29/10/2026). **10/12 đã có hồ sơ trong kho**; 2 ô mới (#07, #12) lập hồ sơ bên dưới. Mô tả trong ảnh khớp repo thật ở cả 12 ô — không có ô nào là "nguồn dựng".

| # | Tên hiển thị (ảnh) | Repo thật | Trong kho |
|---|---|---|---|
| 01 | UI/UX Pro Max Skill | `nextlevelbuilder/ui-ux-pro-max-skill` | §7g.2 |
| 02 | Awesome DESIGN.md | `VoltAgent/awesome-design-md` | §7c |
| 03 | Open Design | `nexu-io/open-design` | §2 |
| 04 | Taste Skill | `Leonxlnx/taste-skill` | §4 / §7j |
| 05 | Impeccable | `impeccable` | §4, mục 20 |
| 06 | React Bits | `DavidHDev/react-bits` | mục 22 |
| 07 | Skills for Designers and Engineers | `emilkowalski/skills` | **mới ↓ §7m.1** |
| 08 | Hallmark | `Nutlope/hallmark` | §7l |
| 09 | Google DESIGN.md | `google-labs-code/design.md` | §7c |
| 10 | GSAP Skills | skill pack GSAP | mục 22 |
| 11 | Scroll World | `scroll-world` (Chase) | mục 22 |
| 12 | Canvas UI | `DavidHDev/canvas-ui` | **mới ↓ §7m.2** |

### 7m.1 `emilkowalski/skills` — "Skills for Designers and Engineers" (mới)

| Thuộc tính | Giá trị |
|---|---|
| Repo | github.com/emilkowalski/skills · **51.327★, 3.001 fork, 2 issue** (29/10/2026, API GitHub) · **MIT** · Markdown · tạo 16/3/2026, push 28/10/2026 · site emilkowal.ski/skill |
| Tác giả | Emil Kowalski — tác giả `sonner` (toast) và `vaul` (drawer), giảng viên animations.dev; nguồn "taste" uy tín thật |
| Nội dung | Bộ Agent Skills về animation, design, code, performance cho "design engineer"; cài `npx skills add emilkowalski/skills`; hỗ trợ Claude Code, Codex, Cursor. Tác giả khuyên bật theo ngữ cảnh (vd khi review animation), không always-on |
| Vì sao đáng tham khảo | Nhỏ gọn (~117 KB), tập trung chi tiết animation/vi tương tác — bổ sung Taste Skill (§4) và Hallmark (§7l) |
| Lưu ý | Aggregator (ecosyste.ms) còn ghi ~5,5k★ — snapshot cũ, lệch ~10× so với API GitHub |
| Liên quan | §4 (taste), §7g, mục 22 (animation) |

### 7m.2 `DavidHDev/canvas-ui` — WebGL phủ lên HTML thật (mới)

| Thuộc tính | Giá trị |
|---|---|
| Repo | github.com/DavidHDev/canvas-ui · **5.166★, 268 fork, 4 issue** (29/10/2026, API GitHub) · **license NOASSERTION** (GitHub không nhận ra license chuẩn → đọc file LICENSE trước khi dùng thương mại; cùng tác giả React Bits vốn MIT+Commons Clause) · TypeScript · tạo 16/7/2026, push 3/10/2026 · site canvasui.dev |
| Tác giả | DavidHDev (David Haz) — cũng là tác giả React Bits (#06 trong ảnh) |
| Nội dung | Thư viện component canvas: dùng API thử nghiệm **html-in-canvas** vẽ DOM thật thành texture rồi phủ shader WebGL (fire, fluid, glass…) mà **vẫn giữ chọn chữ và link**; fallback overlay WebGL khi trình duyệt chưa hỗ trợ (cần Chrome cờ `canvas-draw-element`). Registry **MCP-ready (shadcn MCP)** nên agent duyệt/cài component được. React, Vue, Svelte, vanilla |
| Vì sao đáng tham khảo | Khác thư viện component thường: hiệu ứng WebGL trên nội dung tương tác thật; cầu nối agent ↔ component qua MCP |
| Hạn chế / rủi ro | License phi chuẩn; phụ thuộc API trình duyệt thử nghiệm → chỉ chạy đầy đủ trên Chrome có bật cờ |
| Liên quan | #06 React Bits (mục 22), mục 22 (WebGL/animation) |

**Nguồn §7m:** ảnh infographic người dùng gửi 29/10/2026 · API GitHub (đã xác thực) 29/10/2026: `emilkowalski/skills`, `DavidHDev/canvas-ui` · emilkowal.ski/skill · canvasui.dev · flaviocopes.com/canvas-ui.md · awesome.ecosyste.ms/projects/github.com%2Femilkowalski%2Fskills (snapshot cũ ~5,5k★) · map 10 ô còn lại: §2, §4, §7c, §7g.2, §7j, §7l, mục 20, mục 22.

## 7n. `evondev/evondevKit` — skill `ui-ux` "UI dashboard không còn mùi AI" (bài đăng Facebook người dùng gửi, clone 2026-10-31)

> Ảnh là bài đăng Facebook của tác giả: banner "evondevKit / ui-ux — UI dashboard không còn mùi AI · Open-source UI/UX skill cho coding agents. Đọc codebase, tạo brief, 2–3 wireframes, xây dựng bằng component sẵn có", kèm link website `evondev-uiux.vercel.app/ui-ux` và GitHub, lời "thấy hay cho mình xin stars nhé". Đã clone đủ lịch sử, đọc README/README.vi, `SKILL.md`, `.claude-plugin/`, `TESTS.md`, ba script. **Không cài plugin, không chạy `probe.mjs`.**

### 7n.1 Hồ sơ nhanh

| Mục | Thông tin (đọc 31/10/2026) |
|---|---|
| Repo | github.com/evondev/evondevKit · **432★, 56 fork**, 0 issue/PR mở (shields) · **MIT** (© 2026 Tuấn Trần) · plugin `evon` v0.3.27; tạo 20/9/2026, commit cuối 22/10/2026 |
| Tác giả | **Tuấn Trần (evondev)** — người Việt làm nội dung dạy frontend; một mình viết cả 259 commit, **258/259 có trailer `Co-Authored-By: Claude`**. Nhận ủng hộ qua MoMo |
| Nội dung thật | **Một skill `ui-ux`**: `SKILL.md` 44,5 KB (tiếng Việt), `references/` ~1,2 MB (37 file component như table/kanban/OTP/chart, layout `app.md` 170 KB, `tokens.css`, luật màu/chữ/form/trạng thái, `tailwind-v4-traps.md`, quy trình thiết kế, checklist, ngân sách) + 3 script: `probe.mjs` (~4.700 dòng), `lint-skill.mjs`, `check-update.mjs` |
| Cài | Claude Code: `/plugin marketplace add evondev/evondevKit` → `/plugin install evon@evondevkit`, gọi `/evon:ui-ux`; Cursor/OpenCode/Codex/Antigravity/ZCode/omp: `npx skills add evondev/evondevKit` |
| Trạng thái | README tự ghi **Beta**: hợp UI app nền sáng, "test trên 70 prompt trên dự án thật", chủ yếu prompt tiếng Việt; dark mode đang thử *(70 prompt là tự khai, chưa có bộ eval công khai trong repo)* |

### 7n.2 Kiểm từng câu trong bài đăng

| Câu | Thực tế | Kiểm |
|---|---|---|
| "Open-source UI/UX skill cho coding agents" | Đúng: MIT, một skill, đa host qua `skills` CLI | ✅ |
| "Đọc codebase" | Skill buộc đọc component library, màu/brand của dự án trước khi dựng ("dùng component sẵn có") | ✅ |
| "Tạo brief, 2–3 wireframes" | Luồng mặc định: brief → người dùng duyệt → 2–3 wireframe → chọn → dựng. Có lối tắt "dựng luôn" (bỏ wireframe để tiết kiệm token), "review", "dựng lại giữ brand", "refactor CSS giữ giao diện" | ✅ |
| "Xây dựng bằng component sẵn có" | Đúng với dự án có thư viện component; còn có nhánh "dựng design system trước" (token + 7 component nền) | ✅ |
| "Không còn mùi AI" | Khẩu hiệu. Cơ chế cụ thể: luật cứng ("locked-rules", ngân sách, checklist) + **`probe.mjs` đo bằng Playwright** ở nhiều bề rộng (375–1920, quét mỗi 20px): cuộn ngang, chữ tràn/cắt, tương phản, focus/hover, so bản dựng với wireframe đã chọn. Đây là cổng máy thật, không chỉ prompt | ⚠️ tuyên bố thẩm mỹ, chưa có so sánh độc lập |

### 7n.3 Điều bài đăng không nói (đọc mã)

- **Nặng ngữ cảnh:** riêng `SKILL.md` ~44,5 KB (~11k token) nạp mỗi lần gọi, chưa kể file reference mở theo khối cần dựng. Dòng đầu skill: "Chưa đi hết mục 0 thì KHÔNG viết một dòng code nào" — quy trình chặt, chậm hơn khi chỉ cần sửa nhỏ (README: việc nhỏ hơn một màn hình thì skill làm luôn).
- **Kết nối mạng:** `check-update.mjs` đọc file VERSION trên `raw.githubusercontent.com` tối đa 1 lần/ngày, không gửi gì; tắt bằng `EVONDEVKIT_NO_UPDATE_CHECK=1`. `probe.mjs` chỉ mở URL người dùng đưa (thường localhost); nếu chưa có Playwright thì hướng dẫn cài vào **thư mục tạm**, không cài vào dự án. Không telemetry.
- **Không có CI hay test tự động** (không có `.github/`); `TESTS.md` là danh sách UI cần làm theo bậc, `lint-skill.mjs` kiểm cấu trúc skill nhưng không chạy trong CI.
- **Mới và một người:** 6 tuần tuổi, bus factor 1, phiên bản đổi liên tục (v0.3.x); README khuyên bật auto-update — với team nên ghim phiên bản thay vì auto-update.
- **Tiếng Việt là ngôn ngữ chính** của skill: lợi thế cho đội Việt (mục 18), prompt tiếng Anh "ít test hơn" theo chính README.

### 7n.4 So với các skill UI đã có trong kho

| Skill | ★ | Cách làm | Khác evondevKit |
|---|---|---|---|
| `evondev/evondevKit` | 432 | Quy trình designer (brief → wireframe → dựng) + đo Playwright | Tập trung **dashboard/app**, dùng component dự án, tiếng Việt |
| `Leonxlnx/taste-skill` (§7j) | 106k | Art direction + `draw.mjs`/`inspect.mjs`/`lint.mjs` | Thiên landing/thẩm mỹ chung; có inspector CDP |
| `nextlevelbuilder/ui-ux-pro-max-skill` (§7g.2) | 143k | Kho tra cứu CSV + BM25 sinh design system | Dữ liệu tra cứu, không có quy trình wireframe hay đo trang |
| `Nutlope/hallmark` (§7l) | 43k | Ba script lint, chống "AI slop" | Kiểm sau khi dựng; evondevKit thêm bước chốt bố cục trước |
| `emilkowalski/skills` (§7m.1) | 51k | Animation/vi tương tác | Lớp chi tiết chuyển động, không dựng màn |

**Dùng thế nào:** hợp dự án dashboard/admin có sẵn thư viện component (shadcn, Tailwind v4) và đội quen làm việc bằng tiếng Việt. Đưa link localhost đang chạy để skill đo được. Dùng nhánh "review" trước để xem danh sách lỗi, rồi mới "fix 1, 3". Ghim phiên bản plugin; cân nhắc chi phí token của `SKILL.md` khi dùng cho thay đổi nhỏ. Đây là skill giai đoạn beta của một tác giả; nên thử trên một màn trước khi dùng rộng.

**Nguồn §7n:** bài đăng Facebook tác giả (ảnh người dùng gửi 31/10/2026) · clone đủ lịch sử github.com/evondev/evondevKit 31/10/2026 (259 commit, HEAD 4d02153 22/10/2026; README.md, README.vi.md, LICENSE, TESTS.md, .claude-plugin/{marketplace,plugin}.json, skills/ui-ux/{SKILL.md, VERSION, references/*, scripts/{probe,check-update,lint-skill}.mjs}; đếm trailer bằng git log) · img.shields.io/github/{stars,forks,license,last-commit,v/release,issues,issues-pr}/evondev/evondevKit.json (31/10/2026) · evondev-uiux.vercel.app/ui-ux

### 7n.5 Đọc lại 6/11/2026: v0.6.0, cài được cho sáu công cụ, thêm phân tích sản phẩm và bộ mặt dashboard

> Người dùng gửi ảnh trang giới thiệu (evondev-uiux.vercel.app/ui-ux, mục "Cài xong trong một phút") với các tab Claude Code, Cursor, Codex, OpenCode, Antigravity, ZCode và ba bước: thêm marketplace rồi cài plugin `evon`, gọi `/evon:ui-ux`, cập nhật bằng `/plugin marketplace update evondevkit`. Đối chiếu clone đủ lịch sử, HEAD `69fc1b347dd779f29f13bb4efb42075fb80a1c3a` (5/11/2026): **18 commit sau lần đọc `4d02153`**, plugin từ 0.3.27 lên **0.6.0**, 460★, 62 fork (GitHub search API 6/11/2026). MIT, © Tuấn Trần. **Không cài, không chạy.**

**Cài đặt (khớp ảnh)**

- Claude Code: `/plugin marketplace add evondev/evondevKit` → `/plugin install evon@evondevkit`; gọi `/evon:ui-ux` hoặc chỉ cần viết prompt về giao diện app là skill tự bật; cập nhật `/plugin marketplace update evondevkit` (hoặc bật auto-update trong Marketplaces). README có cả bước gỡ cài đặt.
- Cursor, OpenCode, Codex, Antigravity, omp: `npx skills add evondev/evondevKit` (hoặc `bunx`), chép skill vào `.agents/skills/ui-ux/`; ZCode vào `.zcode/skills/ui-ux/`; `-a` để chọn công cụ, `-g` để dùng chung mọi dự án; cập nhật `npx skills update`. README có bảng cú pháp gọi skill cho từng công cụ.

**Tính năng mới từ 0.3.28 tới 0.6.0 (theo commit và README)**

- **Phân tích sản phẩm trước khi dựng** (0.5.0): một báo cáo gồm brief, các màn chính và cách các sản phẩm cùng loại làm; **soi luồng** (ví dụ onboarding tới việc chính đầu tiên) đếm số bước; sinh `DESIGN.md` cho dự án; `probe --stress` để thử giao diện với dữ liệu khó.
- **Bộ mặt dashboard (P13, 0.4.0)**: các bộ phong cách có tên (Clean, Dark Sidebar, Soft, Night…) đổi font, nền và sidebar mà không đổi bố cục, để các dashboard khác nhau không ra cùng một gương mặt; skill chỉ tự gợi ý những bộ đã có test.
- **Màu nhấn theo ngành (0.4.1)**: gợi ý ba màu nhấn theo ngành, dựa trên đo màu chính của khoảng 60 trang chủ sản phẩm ở 12 ngành; ngành không có quy ước thì không bịa; bảng màu đạt tương phản từ 5:1 với chữ trắng; tránh màu trùng ý nghĩa với nút xóa, success, warning.
- **Trục khung app (0.6.0)**: kiểu điều hướng (Float, Rail có nhãn, Topbar), bề mặt (Không viền, Xếp lớp, Editorial) và bố cục nội dung (Danh sách + chi tiết, Hai panel, Trang hoạt động), chọn theo việc chính của màn.
- Giữ cách làm cũ: wireframe 2–3 phương án trước khi dựng, `probe.mjs` (Playwright) đo tràn, cắt chữ, tương phản ở 375–1920 px; kiểm bản mới tối đa một lần mỗi ngày bằng cách đọc file version trên GitHub (không gửi dữ liệu), tắt bằng biến môi trường.

**Nguồn §7n.5:** ảnh trang giới thiệu người dùng gửi 6/11/2026 · clone https://github.com/evondev/evondevKit HEAD `69fc1b347dd779f29f13bb4efb42075fb80a1c3a`: https://github.com/evondev/evondevKit/blob/69fc1b347dd779f29f13bb4efb42075fb80a1c3a/README.vi.md · https://github.com/evondev/evondevKit/blob/69fc1b347dd779f29f13bb4efb42075fb80a1c3a/.claude-plugin/plugin.json · https://github.com/evondev/evondevKit/blob/69fc1b347dd779f29f13bb4efb42075fb80a1c3a/LICENSE · `git log 4d02153..HEAD` · https://evondev-uiux.vercel.app/ui-ux · GitHub search API 6/11/2026.

### 7n.6 Đọc lại 16/11/2026: v0.9.3 làm tốt cả Mobile App UI, skill landing `evon:landing` đang được audit (bài đăng người dùng gửi)

> Bài đăng của tác giả: landing page trong ảnh là kết quả một prompt của skill đang audit để thêm vào evondevKit; skill hiện làm tốt Dashboard UI và Mobile App UI; lệnh dự kiến `evon:landing: <prompt>`.

| Thuộc tính | Giá trị (16/11/2026) |
|---|---|
| Repo | https://github.com/evondev/evondevKit · **564★, 89 fork** (GitHub search API) · MIT · 355 commit · plugin `evon` **0.9.3** (tag mới nhất v0.9.2) |
| Gọi | `/evon:ui-ux` (Claude Code: `/plugin marketplace add evondev/evondevKit` rồi `/plugin install evon@evondevkit`) |

Điểm mới từ 6/11 (đọc `git log`):

- **App điện thoại thành nhánh đầy đủ (0.9.0–0.9.3)**: `mobile.md` tách theo mục, chín "bộ mặt" app (`clean`, `mono`, `photo`, `playful`, `immersive`, `editorial`…, thêm bộ Brand cho gọi xe, giao hàng, vé), màu nhấn theo ngành; `probe --mobile` đo vùng chạm nhỏ, chữ nhỏ, dòng cuối bị che, sheet thiếu lớp phủ, ô nhập số thiếu `inputmode`, ô thiếu nhãn, màn lỗi chung chung, màn mất nút quay lại.
- **Skill nhẹ token hơn**: `SKILL.md` gọn lại, wireframe tách theo loại màn, checklist từng màn chỉ mở khi cần, `lint-skill.mjs` báo khi file vượt trần kích thước.
- **Thử bằng dự án thật**: mỗi lần sửa luật ghi lại phiên thử (app du lịch, bảo hiểm, AI chat, gọi xe) và kết quả probe.

**Skill landing page (`evon:landing`)**: `NEXT.md` đã chốt hướng làm thành skill thứ hai, tách khỏi `ui-ux` vì luật hai bên khác nhau:

1. Tra 15–20 landing page SaaS đang chạy trước khi viết luật, ghi section, thứ tự, số lần lặp CTA, dạng pricing.
2. Brief hỏi một câu "khách vào trang cần làm gì?" với bốn mục tiêu: đăng ký dùng thử, mua luôn, đặt lịch demo, vào danh sách chờ; mục tiêu quyết định bật section nào.
3. Chín loại section nền (header, hero, social proof, tính năng, cách hoạt động, pricing, FAQ, CTA cuối, footer), mỗi loại 2–3 biến thể; pricing ba dạng.
4. Luật chung: một CTA chính lặp dọc trang cùng chữ cùng đích, một màu nhấn, nhịp dọc theo một thang, chữ hero nói đúng sản phẩm làm được gì cho ai.

**Nguồn §7n.6:** bài đăng người dùng gửi 16/11/2026 · clone https://github.com/evondev/evondevKit HEAD `5a892ceac93d1bb286391663eb01cbd011706886`: https://github.com/evondev/evondevKit/blob/5a892ceac93d1bb286391663eb01cbd011706886/README.vi.md · https://github.com/evondev/evondevKit/blob/5a892ceac93d1bb286391663eb01cbd011706886/NEXT.md · https://github.com/evondev/evondevKit/blob/5a892ceac93d1bb286391663eb01cbd011706886/.claude-plugin/plugin.json · `git log` 6–9/11/2026 · GitHub search API 16/11/2026.

## 7o. Ba skill thiết kế trong ảnh: `/figma-use-motion` (Figma), `/design-critique` và `/design-handoff` (Anthropic) (ảnh người dùng gửi, clone 2026-10-31)

> Ảnh là ba chip lệnh slash trên nền cam, không kèm chữ (sau chip đầu thấy loáng thoáng "…The faded card behind it rises a…", tức một bài viết về hiệu ứng chuyển động). Đã clone `figma/mcp-server-guide`, `anthropics/knowledge-work-plugins` và `openai/plugins`, đọc `SKILL.md` cùng `references/`, `plugin.json`, `.mcp.json`, `CONNECTORS.md` và lịch sử git của từng skill. **Không cài, không gọi Figma MCP.**

### 7o.1 Hồ sơ nhanh

| Skill | Nguồn thật (đọc 31/10/2026) | Nội dung | Cài |
|---|---|---|---|
| `/figma-use-motion` | `figma/mcp-server-guide` · **2.137★, 211 fork** · **không có file LICENSE**, dùng theo Figma Developer Terms · plugin `figma` v2.2.174, **Beta** · skill có từ 24/6/2026, sửa cuối 13/10/2026 | `SKILL.md` 90 dòng + 4 reference (~1.180 dòng: keyframe, easing, custom animation style, text stagger). Dạy agent **tạo/sửa animation ngay trên canvas Figma** qua tool `use_figma` (Plugin API). Phải nạp cùng skill nền `figma-use` | `claude plugin install figma@claude-plugins-official` |
| `/design-critique` | `anthropics/knowledge-work-plugins`, plugin `design` v1.2.0 · **34k★, 3,8k fork**, **Apache-2.0** · tạo 23/2/2026, đổi từ command sang skill 13/3/2026, **không sửa từ đó** | `SKILL.md` 118 dòng, **chỉ là prompt**: 5 khía cạnh (ấn tượng đầu, usability, phân cấp thị giác, nhất quán, accessibility) và mẫu báo cáo có mức 🔴/🟡/🟢 | `claude plugin install design@knowledge-work-plugins` |
| `/design-handoff` | Cùng plugin `design`, cùng ngày tạo và sửa | `SKILL.md` 131 dòng, chỉ là prompt: mẫu spec bàn giao gồm token, component, trạng thái, breakpoint, edge case, **bảng Animation/Motion (ms, easing)**, ghi chú a11y | như trên |

Plugin `design` còn 5 skill khác: `accessibility-review`, `design-system`, `ux-copy`, `research-synthesis`, `user-research`. `.mcp.json` của nó nối sẵn Figma (`mcp.figma.com/mcp`), Slack, Linear, Asana, Atlassian, Notion, Intercom (xem mục 20 §1).

### 7o.2 Điều đọc mã mới thấy

- **Motion trên Figma còn bị khoá theo tài khoản.** `figma-use-motion` dặn: nếu API trả `"<name>" is not a supported API` thì dừng ngay, không thử lại. Bản trong `skills-figquery/` (bản phát cho Cursor) và bản trong `openai/plugins` ghi rõ tên cờ là **`metronome`**; bản chính đã bỏ tên cờ ở lần đồng bộ 13/10/2026. Custom animation style có thể tắt riêng dù keyframe vẫn chạy.
- **Ba bản sao lệch nhau.** Bản `openai/plugins` (đồng bộ cuối 9/7/2026) thiếu `motion-custom-styles.md` và `text-animation.md`; bản figquery cũng khác bản chính. Muốn bản mới nhất thì lấy từ `figma/mcp-server-guide/skills/`.
- **Kiểm chuyển động tốn tiền thật.** `get_screenshot` chỉ chụp trạng thái nghỉ. Muốn thấy chuyển động phải gọi `export_video` (render phía server, ~10 giây tới vài phút), rồi cắt khung bằng `ffmpeg`. Skill hướng dẫn tiết kiệm: 4–6 khung, `fps` 5, rộng 320px. README Figma: tài khoản Starter hoặc ghế View/Collab chỉ được **6 lần gọi tool/tháng**; ghi lên canvas "sẽ thành tính năng trả phí theo lượng dùng", hiện miễn phí trong beta.
- **Skill anh em `figma-implement-motion`** làm chiều ngược lại: đọc `get_motion_context` (keyframe, easing, snippet CSS `@keyframes` và motion.dev) rồi viết code. Hai skill tự phân ranh giới với nhau: sửa trong Figma dùng `figma-use(-motion)`, ra code dùng `implement-motion`.
- **`design-critique` và `design-handoff` không có công cụ đo.** Mục "Color contrast: Pass/fail" và "Touch targets" do model ước lượng từ ảnh hay dữ liệu Figma, không có script tính tỉ lệ tương phản. So với các skill có cổng máy trong kho (Hallmark §7l, evondevKit §7n, taste-skill §7j), đây là khung câu hỏi, không phải bộ kiểm.
- **Bảng motion của `design-handoff` dễ thành số bịa.** Skill bảo điền "Duration (ms) / Easing" nhưng không gọi `get_motion_context`, nên với frame tĩnh model sẽ đoán. Nguyên tắc "Specify everything" của chính skill càng đẩy model điền đủ ô.
- **Đầu ra là văn bản tĩnh**, không nối ngược về file Figma; sửa thiết kế xong phải chạy lại.

### 7o.3 Ghép ba skill thành một luồng

1. `/design-critique <link Figma>` → danh sách ưu tiên; tự đo tương phản bằng công cụ riêng thay vì tin cột Pass/fail.
2. Sửa thiết kế; thêm chuyển động bằng `/figma-use-motion` (nếu tài khoản có quyền motion), kiểm bằng `export_video` ít khung.
3. `/design-handoff <link Figma>` → spec. **Ghi đè bảng Animation/Motion** bằng số từ `get_motion_context`, hoặc giao phần motion cho `figma-implement-motion` sinh code thẳng.

**Nên dùng khi:** đội đã có Figma (ghế Dev/Full trả phí, vì Starter chỉ 6 lần gọi/tháng) và muốn chuẩn hoá mẫu review/bàn giao. Hai skill của Anthropic ngắn, Apache-2.0, dễ fork để thêm bước đo. `figma-use-motion` còn beta, phụ thuộc cờ tính năng và điều khoản riêng của Figma (không phải giấy phép mã mở); không nên dựng quy trình bắt buộc trên nó lúc này. Phần motion trên web viết bằng code xem mục 22 §6.

**Nguồn §7o:** ảnh người dùng gửi 31/10/2026 · clone github.com/figma/mcp-server-guide (88 commit, HEAD f3f264d 28/10/2026; README.md, plugin.json, skills/{figma-use-motion,figma-implement-motion}/**, skills-figquery/figma-use-motion/SKILL.md; `git log -S metronome`) · clone github.com/anthropics/knowledge-work-plugins (1.128 commit, HEAD 2574e29 27/10/2026; design/{.claude-plugin/plugin.json,.mcp.json,CONNECTORS.md,README.md,skills/*/SKILL.md}) · clone github.com/openai/plugins (HEAD 0722921d; plugins/figma/skills/figma-use-motion/**) · GitHub search API 31/10/2026 (sao, fork, license) · tìm web: skills.sh, tessl.io, figma.com/blog/try-these-10-skills-and-show-off-your-own, uxplanet.org (2 bài Medium về plugin design, chỉ đọc tóm tắt)

## 7p. Nâng cấp mục UI/UX: rà lại số liệu và thêm 18 repo mới từ GitHub và web (yêu cầu người dùng, 31/10/2026)

> Hai việc. (1) Đọc lại số sao, license, trạng thái của **72 repo GitHub** đã có trong mục 06 bằng GitHub search API; ngày commit cuối của các bảng §1–§6 lấy từ clone nông. (2) Tìm dự án còn thiếu: 18 truy vấn GitHub (topic `design-system`, `shadcn`, `figma`, `generative-ui`…, và từ khoá "design skill", "design system mcp", "prompt to ui" cho repo tạo sau 1/10/2025), cộng tìm web. Từ ~120 ứng viên chưa có trong kho, chọn **18 repo** gần nhất với chủ đề "làm UI cùng coding agent", clone đủ lịch sử và đọc mã (LICENSE, manifest, skill, script, CI, grep telemetry). **Không chạy script nào của các repo.** Số sao đọc 31/10/2026.

### 7p.1 Rà 72 repo cũ: điều đã đổi

| Repo | Thay đổi (19/10 → 31/10/2026, trừ khi ghi khác) | Hệ quả |
|---|---|---|
| `Shopify/polaris` | **Đã archive 11/8/2026, đổi tên `Shopify/polaris-react-archive`**, README ghi "Deprecated". Shopify chuyển sang **Polaris Web Components** (ra 1/10/2025) | Không chọn Polaris React cho dự án mới. Web components còn thiếu vài component (ví dụ IndexTable, theo diễn đàn Shopify) |
| `tailwindlabs/headlessui` | Commit cuối nhánh chính vẫn **13/4/2026** (release v2.2.10 ngày 7/4) | Hơn 6 tháng đứng yên; muốn headless thì ưu tiên Base UI hoặc React Aria |
| `onlook-dev/onlook` | Commit nhánh chính cuối **21/7/2026** (bản vá IDOR); API báo "push 21/10" là do nhánh khác | Coi như tạm dừng |
| `tremorlabs/tremor`, `tremor-blocks` | Push cuối 10/2025 và 1/2025 | Ngừng phát triển sau khi về Vercel; chọn shadcn charts |
| `themesberg/flowbite-admin-dashboard` | Push cuối 3/2025 | Mẫu cũ, kiểm Tailwind v4 trước khi dùng |
| `wheresryan22/anatomy` | 3,8k (12/10) → **23,3k** | Tăng nhanh nhất mục; hồ sơ §7 vẫn đúng về cơ chế |
| `Nutlope/hallmark` | 33k → **43,9k** | §7l |
| `cathrynlavery/diagram-design` | 51,8k → **63,5k** | §7b |
| `plugin87/ux-ui-agent-skills` | 2k → 3,1k | §7d |
| `storytold/figcraft` | 2,7k → 4k | §7e |
| `miqdadbadjuber/anti-slop` | 6,5k → 7,8k | §7i |
| `ibelick/ui-skills` | 9,4k → 10,4k; GitHub nay nhận MIT | Catalog bổ sung license |

Các repo khác dao động dưới 5%. GitHub báo `NOASSERTION` với Vuetify, tldraw, Vercel AI, Preline, flutter/samples, Fluent UI, USWDS: không phải đổi license; catalog giữ license đã đọc trong file.

### 7p.2 Bảng nhanh 18 repo mới

| Repo | Nhóm | ★ · license | Commit cuối | Một dòng | Cờ |
|---|---|---|---|---|---|
| `meta/astryx` | Design system | 13,8k · MIT | 31/10/2026 | React 19 + StyleX, 107 thư mục component, 7 theme, CLI cho agent, MCP từ xa | 0.x, Beta |
| `shadcn-ui/lint` | Lint design system | 3,3k · MIT | 19/10/2026 | 6 luật ESLint/Oxlint cho Tailwind v4, thông báo lỗi viết cho agent | 6 tuần tuổi |
| `DouyinFE/semi-design` | Design system | 10,4k · MIT (+ notice bên thứ ba) | 26/10/2026 | 86 component (có AI chat), MCP `@douyinfe/semi-mcp`, skill, `DESIGN.md` | Tài liệu agent tiếng Trung |
| `jnsahaj/tweakcn` | Trình sửa theme | 10,5k · Apache-2.0 | 3/9/2026 | Mã nguồn tweakcn.com: chỉnh theme shadcn trực quan | SaaS freemium, PostHog, không CI |
| `GLips/Figma-Context-MCP` | Figma → agent | 16,1k · MIT | 24/6/2026 | MCP "Framelink" rút gọn dữ liệu Figma REST cho agent | **Telemetry bật sẵn** |
| `Manavarya09/design-extract` | Trích design system | 4,4k · MIT | 31/10/2026 | `designlang`: URL → DTCG, Tailwind, shadcn, DESIGN.md (17+ file) | Không đọc robots.txt |
| `dembrandt/dembrandt` | Trích design system | 3,9k · MIT | 22/10/2026 | CLI/MCP/Action: trích token và chặn "drift" trong CI | Có `--stealth` |
| `ZSeven-W/openpencil` | Công cụ vẽ vector | 7k · MIT (+ blob đóng) | 29/10/2026 | Trình vẽ vector viết bằng Rust, MCP, xuất code 8 nền tảng | Thư viện xác thực đóng, ~1,2 triệu dòng |
| `benjitaylor/agentation` | Phản hồi UI cho agent | 5,2k · **PolyForm Shield** | 21/9/2026 | Thanh công cụ React: bấm vào phần tử, ghi chú, gửi agent qua MCP | Không phải mã mở OSI |
| `alchaincyf/huashu-design` | Skill thiết kế | 28,3k · MIT | 31/10/2026 | Một câu → HTML, PPTX sửa được, MP4, infographic; có lint Playwright | Tiếng Trung, tốn token |
| `google-labs-code/stitch-skills` | Skill thiết kế | 8,6k · Apache-2.0 | 17/8/2026 | 16 skill điều khiển Google Stitch MCP, chuyển sang React/RN/shadcn | Cần tài khoản Stitch, dữ liệu lên Google |
| `heydamir/unslop` | Skill thiết kế | 3,4k · CC-BY-4.0 | 29/10/2026 | Kiểm và sửa UI "vibecoded" theo 9 lượt, quay video trước/sau | 4 commit, prompt thuần |
| `Owl-Listener/designer-skills` | Bộ skill | 3,2k · MIT | 5/9/2026 | 111 skill + 34 lệnh nghề thiết kế, 9 plugin | Prompt thuần, kéo 24 plugin từ repo khác |
| `Jakubantalik/transitions.dev` | Skill chuyển động | 6k · **license riêng** | 29/10/2026 | 35 transition CSS + token motion, có quét luật tĩnh | Bán bản Pro, `curl \| bash` |
| `thesysdev/openui` | Generative UI | 14,6k · MIT | 29/10/2026 | Ngôn ngữ "OpenUI Lang" + runtime React/Vue/Svelte/Angular | **Telemetry lúc cài** |
| `tambo-ai/tambo` | Generative UI | 11,2k · MIT + Apache-2.0 | 9/10/2026 | SDK React: component + Zod thành tool cho LLM | **Tambo Cloud đóng 31/10/2026** |
| `CopilotKit/OpenIntelligentUI` | Generative UI (mẫu) | 4,1k · MIT | 13/10/2026 | App mẫu trả lời bằng bảng A2UI hoặc widget HTML trong iframe | Bắt buộc API TypeSafe |
| `JimLiu/baoyu-design` | Skill thiết kế | 5,7k · **hỗn hợp** | 31/10/2026 | Đóng gói lại Artifact types và Claude Design để chạy cục bộ | **Rủi ro sở hữu trí tuệ, không khuyên dùng** |

### 7p.3 Design system và lint "sẵn cho agent"

- **Astryx (Meta).** pnpm monorepo, 5.788 commit, 124 tác giả, 4.511 commit từ 1/5/2026. Có `AGENTS.md` 241 dòng; lệnh CLI ghi một khối hướng dẫn được quản lý vào `AGENTS.md`, `CLAUDE.md`, `GEMINI.md`, `.cursorrules`. MCP **không nằm trong gói npm** mà là dịch vụ `astryx.atmeta.com/mcp` (2 tool `search`, `get`). Lời "dùng cho 13.000 ứng dụng nội bộ trong 8 năm" không kiểm được: lịch sử công khai bắt đầu 9/1/2026. Cần React 19; postinstall chỉ in lời nhắc, không gọi mạng. Cài: `npm install @astryxdesign/core @astryxdesign/theme-neutral @stylexjs/stylex` rồi `npx astryx init`.
- **`@shadcn/lint`.** Đúng 6 luật (`no-restyle`, `no-raw-colors`, `no-arbitrary-values`, `no-inline-styles`, `no-unknown-classes`, `require-static-classes`), mỗi luật một file và một trang docs. Đây là **cổng máy đúng nghĩa cho "taste"**: thay vì dặn agent "dùng token", lint báo lỗi kèm cách sửa. Số liệu "mọi model về 0 lỗi" là eval tự chạy, thư mục kết quả bị gitignore nên không tái lập được. Oxlint chỉ đọc khối script trong `.vue`/`.svelte`. Không telemetry. README trỏ `LICENSE.md` nhưng file tên `LICENSE`.
- **Semi Design (ByteDance).** Thư viện trưởng thành (từ 2021, 467 tag, 10 workflow gồm Cypress, Chromatic, Lighthouse). Lớp agent: MCP 5 tool (skill chỉ mô tả 4), skill `semi-design-guide` tiếng Trung, `DESIGN.md`. MCP tải docs lúc chạy từ unpkg và npm mirror. 626 issue/PR mở. Cài MCP: `claude mcp add semi-mcp -- npx -y @douyinfe/semi-mcp`.
- **tweakcn.** Không phải thư viện mà là mã nguồn một SaaS (Next.js, Neon, Polar, Gemini). Nút "MCP" chỉ sinh cấu hình cho registry MCP của shadcn, không có server riêng. AI sinh theme giới hạn 5 lượt miễn phí; PostHog chỉ bật khi đặt key. Nhịp chậm lại: 2 commit từ 1/8/2026. Dùng tốt nhất qua web, xuất biến CSS.

### 7p.4 Figma, trích design system từ web, công cụ vẽ

- **Figma-Context-MCP (Framelink).** Hai tool `get_figma_data`, `download_figma_images`; rút gọn JSON Figma thành YAML gọn, hợp khi không có ghế Dev để dùng MCP chính chủ (§7o). **PostHog bật mặc định từ v0.10.0 (10/4/2026)**: gửi phiên bản, OS, tên MCP client, số node, thời gian, mã lỗi; README không nói, chỉ CHANGELOG và `--help`. Tắt bằng `--no-telemetry`, `FRAMELINK_TELEMETRY=off` hoặc `DO_NOT_TRACK=1`. `server.json` còn ghi 0.6.4 trong khi gói là 0.13.2. Nhánh chính đứng yên từ 24/6/2026.

**design-extract (`designlang`) và dembrandt** cùng mở URL bằng Playwright rồi xuất token, nhưng khác nhau ở chỗ đáng kể:

| | design-extract | dembrandt |
|---|---|---|
| DESIGN.md | Theo quy ước của design-extractor.com, **không** theo spec Google | Theo **spec `google-labs-code/design.md` 0.4**, test chạy linter thật, có workflow theo dõi spec mới |
| robots.txt | Không đọc | Đọc; trang con bị cấm thì bỏ qua, URL đầu vào chỉ cảnh báo (chặn hẳn với `DEMBRANDT_ENFORCE_ROBOTS=1`) |
| Mạng | `--smart` gửi tóm tắt trang tới Anthropic, OpenAI hoặc Atlas Cloud (nhà tài trợ, mặc định) | `--key`/`--compare <id>` gửi lên dembrandt.com; còn lại chạy offline |
| Khác | 13 bản major trong 5 tháng; có `clone`, `remix` | Có `--stealth` giả vân tay trình duyệt; Action "Drift Gate" chặn lệch token trong CI |

Với kho này, dembrandt là lựa chọn hợp chuẩn hơn (khớp §7c về DESIGN.md). Cả hai đều có thể dùng để sao chép thương hiệu người khác; chỉ nên chạy trên site của mình hoặc site được phép.

- **OpenPencil (`ZSeven-W/openpencil`).** ~1,19 triệu dòng Rust trong 53 crate, viết trong ~8,5 tháng (chuyển từ Electron sang Rust khoảng 5/2026), ~15,7k test, CI clippy `-D warnings`. Có MCP, xuất code React/Vue/Svelte/HTML/Flutter/SwiftUI/Compose/React Native. Lưu ý: **`crates/op-auth-bridge/prebuilt/` chứa thư viện tĩnh đóng, làm rối**, bản phát hành chính thức cần nó, nên bản cài sẵn không hoàn toàn MIT. SSO và relay cộng tác mặc định ở máy chủ `zseven.cn`/`zseven.tech`. **Trùng tên** với `open-pencil/open-pencil` (9,5k★, tạo 27/2/2026, cũng là "Figma thay thế AI-native"). Lời "đầu tiên trên thế giới" không kiểm được.
- **Agentation.** Thanh công cụ React cho phép bấm vào phần tử, khoanh vùng, ghi chú; xuất selector và vị trí cho agent, hoặc đồng bộ qua MCP (9 tool, SQLite cục bộ, cổng 4747). Hợp vòng "người duyệt UI → agent sửa". License **PolyForm Shield** viết lại theo lối riêng, có điều khoản cấm cạnh tranh: được dùng nội bộ, không được dựng sản phẩm cạnh tranh. 22% commit có trailer Claude; không CI. Chế độ cloud tuỳ chọn gửi dữ liệu tới `agentation-mcp-cloud.vercel.app`.

### 7p.5 Skill thiết kế cho agent

- **huashu-design** là skill mạnh nhất trong đợt về **đầu ra thật**: `html2pptx.js` (1.019 dòng) đo style từng phần tử bằng Playwright rồi dựng text box PPTX sửa được; `render-video.js` quay MP4; `design_lint.py` (541 dòng) đo ảnh hỏng, cỡ chữ tối thiểu, **tỉ lệ tương phản WCAG**, lỗi console và phát hiện ba hướng thiết kế chỉ là đổi màu của nhau. Đổi từ "Personal Use License" có giá sang MIT ngày 14/5/2026. `SECURITY.md` liệt kê mọi host mạng và khớp mã; HTML đầu ra vẫn gọi React/Babel/font từ CDN. README tự mâu thuẫn ("không kéo vào Keynote được" và "PPTX sửa được"). Prompt tiếng Trung, mỗi việc luôn sinh 3 hướng, nên tốn token. Cài: `npx skills add alchaincyf/huashu-design`.
- **stitch-skills (Google Labs).** 16 skill trong 3 plugin cho Codex, Claude Code, Cursor. "Validation tự động" thực chất là kiểm AST 2 luật (có interface `*Props`, không có mã màu hex trong `className`); so sánh hình ảnh ở `stitch-loop` là agent tự nhìn. Cần Stitch API key, thiết kế đi lên dịch vụ Google; README ghi "không phải sản phẩm Google hỗ trợ chính thức". Đứng yên từ 17/8/2026.
- **unslop.** `SKILL.md` 233 dòng (~8k token) + ~7k token tham chiếu; 2 script Playwright (chụp trang, dựng video 1080²). Mọi luật (kể cả tương phản 4.5:1) chỉ là lời dặn, không có công cụ đo. Mới 2 ngày tuổi, có quảng cáo dịch vụ "Hire the unslopper". License CC-BY-4.0 (vốn không dành cho phần mềm) buộc ghi công tác giả khi chép hay sửa.
- **designer-skills.** 111 skill nhỏ (0,3–1,8k token mỗi cái) phủ nghiên cứu, design system, chiến lược UX, design ops. CI chỉ kiểm cấu trúc frontmatter. Marketplace kéo thêm 24 plugin từ 4 repo khác qua `git-subdir`, nên con số "273 skill" phụ thuộc repo ngoài. CHANGELOG nói đã gắn tag v1.0.0 nhưng repo không có tag nào. Cài cả bộ sẽ đưa 111 mô tả skill vào ngữ cảnh.
- **transitions.dev.** 35 file transition CSS (README lúc ghi 12, lúc 18; `SKILL.md` ghi 32), có guard `prefers-reduced-motion`. `agent/lib/rules.mjs` là luật tĩnh thật (thời lượng lệch thang, thiếu reduced-motion) nhưng test chỉ chạy khi publish. License riêng: dùng và sửa tự do, **cấm phân phối lại thư viện**; template/theme cần gói trả phí. `npx transitions-refine live --llm` chạy **`curl https://cursor.com/install | bash`**; agent trả phí gửi mã nguồn lên `api.transitions.dev`. Liên quan mục 22 §6.
- **baoyu-design: không khuyên dùng.** `NOTICE.md` tự ghi phần lấy từ Anthropic "not MIT… Anthropic has published no license for it… this project grants none". Repo chứa system prompt của Claude Design (`references/upstream-system-prompt.md`), `provenance.json` cho thấy prompt được trích từ bundle JavaScript phía client, kèm 49 skill dựng sẵn, font icon Anthropicons và editor dựng lại dạng bundle rút gọn 6,3 MB, rồi phát lại lên npm qua 4 gói `dsh-claude-*`. Rủi ro gỡ bỏ và pháp lý cao; mã bundle không kiểm được. Kho chỉ ghi nhận để tránh, không trích nội dung.

### 7p.6 Generative UI: ba cách và một dịch vụ vừa đóng

| | OpenUI (Thesys) | Tambo | OpenIntelligentUI (CopilotKit) |
|---|---|---|---|
| Định dạng | Ngôn ngữ riêng **OpenUI Lang** (dòng lệnh kiểu `root = Card([...])`), spec v1.0 có EBNF và fixture | Không có spec UI: component đăng ký bằng Zod thành tool cho LLM | Bảng **A2UI** + widget HTML/JS do LLM sinh chạy trong iframe |
| Giao thức | Stream qua **AG-UI** (gói langchain), hồ sơ A2UI thử nghiệm | Sự kiện **AG-UI**, client MCP đầy đủ | AG-UI qua CopilotKit |
| Phụ thuộc dịch vụ | Mẫu mặc định gọi `api.thesys.dev`; có mẫu tự host | Client mặc định `api.tambo.co`, **ngừng 31/10/2026**, xoá dữ liệu 30/11 | **Bắt buộc** router Jev của TypeSafe, không có đường lui |
| Telemetry | **`postinstall` của `lang-core` gửi PostHog khi cài**, mọi gói runtime kéo theo; tắt `OPENUI_TELEMETRY_DISABLED=1` hoặc `DO_NOT_TRACK=1` | CLI gửi PostHog; tắt `TAMBO_TELEMETRY_DISABLED` | Gửi `telemetry.copilotkit.ai`; tắt `COPILOTKIT_TELEMETRY_DISABLED=1` |
| Độ chín | 1.076 commit, 60 tác giả, ~143 file test, CI đầy đủ | 5.573 commit, CI đầy đủ, nhưng việc gần nhất là chuẩn bị đóng cloud | 162 commit, không release, dùng bản prerelease CopilotKit |

Nhận định: "chuẩn mở" của OpenUI do một công ty kiểm soát; bảng so sánh "1x so với A2UI 3x" không có dữ liệu trong repo. Tambo vẫn tự host được (Docker + Postgres) nhưng tương lai bảo trì không rõ, không nên chọn cho dự án mới. Với kho này, hướng an toàn vẫn là AG-UI + bộ component (§6) và MCP Apps (mục 04).

### 7p.7 Mẫu chung rút ra

1. **"Agent-ready" đã thành tính năng tiêu chuẩn của design system** (Astryx, Semi, và trước đó Zen DS §7f): `AGENTS.md`, MCP tra cứu component, `DESIGN.md`. Cái phân biệt là có **cổng máy** hay không: `@shadcn/lint`, Drift Gate của dembrandt, `design_lint.py` của huashu đo được; unslop, designer-skills, design-critique (§7o) chỉ dặn.
2. **Telemetry bật sẵn ngày càng phổ biến** ở công cụ cho agent: Framelink MCP (lúc chạy), OpenUI (lúc cài), CopilotKit. Đặt `DO_NOT_TRACK=1` trong môi trường CI/agent chặn được cả ba.
3. **License "gần mở"** nhiều lên: PolyForm Shield (Agentation), license riêng cấm phân phối lại (transitions.dev), CC-BY cho mã (unslop), blob đóng trong repo MIT (OpenPencil). Đọc file LICENSE, đừng tin nhãn GitHub.
4. **Phụ thuộc dịch vụ có thể biến mất**: Tambo Cloud đóng đúng ngày khảo sát. Ưu tiên mẫu tự host được và ghim endpoint.
5. **Sao tăng nhanh không phải tín hiệu chất lượng**: 4 repo trong đợt có dưới 6 tuần tuổi hoặc một người viết gần hết.

**Nguồn §7p:** GitHub search API 31/10/2026 (`repo:` cho 72 repo cũ và 18 repo mới; 18 truy vấn topic/từ khoá) · shields.io cho `stackblitz-labs/bolt.diy` · clone nông nhánh mặc định 20 repo của §1–§6 (ngày commit) · clone `--filter=blob:none` 18 repo mới, đọc: astryx (LICENSE, README, AGENTS.md, packages/cli/{scripts/postinstall.mjs, foundation/agent-docs/agent-docs.mjs}, apps/docsite/src/app/mcp/route.ts), shadcn-ui/lint (packages/lint/src/rules/*, docs/evals.md, SETUP.md), tweakcn (lib/posthog.ts, mcp-dialog.tsx, lib/ai/providers.ts, lib/constants.ts), semi-design (LICENSE, ecosystem/semi-mcp/src/tools/index.ts, ecosystem/semi-ui-skills/SKILL.md, DESIGN.md), Figma-Context-MCP (src/telemetry/client.ts, server.json, CHANGELOG.md), agentation (LICENSE, mcp/src/server/http.ts, skills/*), huashu-design (LICENSE và lịch sử license, SECURITY.md, scripts/{design_lint.py, html2pptx.js, render-video.js}), baoyu-design (LICENSE, NOTICE.md, references/upstream-sync/provenance.json — chỉ đọc đầu file), stitch-skills (react-components/scripts/validate.js, workflows), unslop (SKILL.md, scripts/*), designer-skills (CHANGELOG.md, .claude-plugin/marketplace.json, lint.yml), transitions.dev (LICENSE, agent/lib/rules.mjs, refine/bin/cli.mjs), openui (packages/lang-core/{package.json, src/telemetry/install.ts}, spec/*), tambo (README.md, SELF-HOSTING.md, packages/client/src/tambo-client.ts, các LICENSE/NOTICE), OpenIntelligentUI (apps/agent/src/visualization_router.py, docs/telemetry.md), design-extract (src/formatters/design-md.js, src/classifiers/smart.js), dembrandt (lib/robots.ts, lib/formatters/markdown.ts, smoke.yml), openpencil (crates/op-auth-bridge/{NOTICE, prebuilt/}, op-codegen/src/codegen_targets.rs) · Web: infoq.com/news/2026/10/shopify-web-components, community.shopify.dev/t/is-polaris-shopify-com-going-to-be-shut-down/26216, github.com/Shopify/polaris-react-archive (release notes), releases.sh (Headless UI), infoq.com/news/2026/09/meta-astryx-design-system, opensourceforu.com/2026/06/meta-open-sources-astryx, tambo.co/blog/posts/tambo-is-shutting-down (link trong README, chưa mở)

## 7q. Đọc mã kỹ: open-design, open-pencil, Ionic, Lucide (yêu cầu người dùng, 31/10/2026)

> OpenDesign đã có hồ sơ mức README ở §7k (19/10); open-pencil, Ionic, Lucide là repo lớn còn thiếu sau §7p. Mỗi repo clone đủ lịch sử (blob:none), đọc mã, CI, tài liệu nội bộ; **không cài, không chạy script**. Số sao từ GitHub search API 31/10/2026.

### 7q.0 `nexu-io/open-design`: đọc mã sâu (bổ sung §7k)

| Mục | Thông tin (HEAD `12d970eac`, 30/10/2026) |
|---|---|
| Repo | **105.186★**, 11.992 fork, 572 issue + **759 PR mở** · 3.831 commit trên `main` từ 28/4/2026 · tag mới nhất `open-design-v0.26.1` (22/10) **không nằm trên `main`** (vẫn ghi 0.25.1); tag không ký; CHANGELOG dừng ở 0.9.0 (5/2026); 2.819 nhánh remote |
| Ai viết | 485 tên tác giả; bot `open-design-crew[bot]` 224, `open-design-bot` ~205, `Cursor Agent` 116; 124 commit có trailer Claude, 78 Cursor |
| Kiến trúc | pnpm monorepo: daemon Express 5 + SQLite, web Next.js 16, desktop **Electron 41** (không có Rust/Tauri). ~1,85 triệu dòng TS/TSX (~931k là test); riêng `server.ts` 18.961 dòng. 169 skill, 115 design template, 501 manifest plugin, **152 gói design system** (README ghi 151) |
| Luồng chạy | Web gọi `POST /api/runs` → ghép system prompt (prompt gốc + DESIGN.md + skill + memory) → **spawn CLI agent ngoài** (`shell:false`, cwd là thư mục project) → stream SSE → agent ghi file → xem trong iframe. Có đường BYOK không cần CLI (Anthropic, OpenAI, Azure, Google, Ollama) |

**Phát hiện nặng (đã tự kiểm lại các dòng in đậm trong mã):**

- ❌ **Mọi agent đều chạy với kiểm quyền tắt, gắn cứng trong mã**: Claude Code `--permission-mode bypassPermissions` (`runtimes/defs/claude.ts:116`), Codex `workspace-write` + mạng, và **`danger-full-access` tự động trên Windows/WSL**; Cursor `--force --trust`; Copilot `--allow-all-tools`; Amp `--dangerously-allow-all`; Qwen/Qoder/Trae `--yolo`; Antigravity `--dangerously-skip-permissions`… Brief, file nhập hay skill độc có thể chạy mọi thứ với quyền người dùng.
- ❌ **Telemetry và chia sẻ nội dung mặc định bật**: `applyTelemetryDefaults` đặt `{metrics: true, content: true}` khi chưa có cấu hình (`app-config.ts:732-738`) → prompt, phản hồi, input/output tool gửi về Langfuse qua relay `telemetry.open-design.ai`. Kênh "safety/reliability" gửi PostHog **không kiểm consent và không có công tắc** (khớp PRIVACY.md); README:239 lại nói "consent-gated".
- ❌ **Chẩn đoán tự động tải lên file `*.log` trong `~/.claude`, `~/.codex/log` và thư mục log OpenCode** (`packages/diagnostics/src/agent-logs.ts:120-175`, có bước che bớt), bật mặc định ở bản cài mới; PRIVACY.md không nói rõ việc tải log của CLI bên thứ ba. Mã nguồn relay nằm ở repo riêng.
- ⚠️ **Updater tự viết chỉ so hash lấy từ cùng feed**, không kiểm chữ ký riêng; gói "launcher payload" sau khi giải nén bị **`xattr -dr com.apple.quarantine`** (`updater/payload.ts:159`), tức bỏ qua Gatekeeper cho mã tải về. Bộ cài thì có ký và notarize.
- ⚠️ **API key lưu JSON plaintext** (`app-config.json`, `.od/media-config.json`, file sau không đặt quyền `0o600`); không dùng keychain hay `safeStorage`.
- ⚠️ Daemon bind `127.0.0.1:7456`, từ chối bind ra ngoài khi thiếu `OD_API_TOKEN` (tốt), nhưng **request từ loopback bỏ qua token**, request **không có header Origin được cho qua**, không có allowlist Host chung → có khả năng bị DNS rebinding với route GET **(chưa xác minh khai thác được)**. Docker image đặt `0.0.0.0`.
- ⚠️ **Prompt gốc tự ghi nguồn**: `packages/contracts/src/prompts/official-system.ts` dòng 4: *"Adapted from claude.ai/design's 'expert designer' prompt — same identity, workflow, and content philosophy"*; mặc định màu `#D97757`. Không tìm thấy URL tài sản hay bundle trích từ Anthropic (khác baoyu-design §7p.5), nhưng vẫn là rủi ro điều khoản/sở hữu trí tuệ. Có chế độ "Website Clone" dặn model chép "assets, fonts, and copy faithfully".
- ⚠️ Gói design system mang tên thương hiệu (Stripe, Linear…): `evidence.md` chỉ nói "derived from the curated OpenDesign bundled fixture" (vòng tròn), không có tuyên bố nhãn hiệu; không kèm file font thương mại.
- ⚠️ Dịch vụ model trả phí **AMR là lựa chọn "Officially recommended" mặc định khi onboarding**, trong khi README nói "We don't ship an agent". Bản build từ mã nguồn không có key thì PostHog/relay không gửi, trừ luồng analytics AMR gắn cứng `amr-api.open-design.ai` **(chưa xác minh có gửi ở bản build nguồn)**.
- ✅ Iframe xem trước mặc định không có `allow-same-origin`; cửa sổ Electron `contextIsolation`, `sandbox`, chặn `window.open`; không `eval` trong daemon; CI 55 workflow, ~3.000 file test, Playwright `@critical` và visual.

**Kết luận:** đánh giá §7k ("local-first thật, PRIVACY rõ") cần sửa: lõi chạy cục bộ nhưng **mặc định gửi cả nội dung prompt và log agent ra ngoài**, và mọi agent chạy không kiểm quyền. Nếu dùng: tắt cả hai lớp telemetry trong Settings ngay lần đầu (lớp safety vẫn gửi), chạy trong máy ảo/container riêng không có thư mục `~/.claude`, `~/.codex` thật, không mở brief/skill từ nguồn lạ, ưu tiên đường BYOK; không dùng bản Docker trên mạng chung khi chưa đặt token.

### 7q.1 `open-pencil/open-pencil` (OpenPencil, TypeScript): khác hẳn `ZSeven-W/openpencil` ở §7p.4

| Mục | Thông tin |
|---|---|
| Repo | 9.510★, 1.000 fork, 167 issue/PR mở · tạo 27/2/2026 · **3.404 commit**, HEAD 31/10/2026 · tag mới nhất v0.16.0 (14/10/2026) · openpencil.dev |
| Tác giả | Danila Poyarkov (`dannote`) viết **~89%** commit; 70 tên tổng cộng. Chỉ 19 commit (0,56%) có trailer Claude, nhưng đó là **do quy định**: CONTRIBUTING cấm ghi AI là đồng tác giả, CI chặn, `.claude/settings.json` tắt attribution; việc dùng AI khai trong mẫu PR |
| License | `LICENSE` MIT, nhưng `REUSE.toml` đặt **phần Cloud (`packages/cloud/**`, `src/cloud/**`…) theo Apache-2.0**; có NOTICE cho Kiwi (evanw), luật lint lấy từ `dmmulroy/anti-slop`. **Không có blob nhị phân đóng** (khác ZSeven) |
| Không liên quan ZSeven | 0 commit chung, không trùng tác giả, không nhắc tên nhau; cùng đọc file `.pen` của Pencil.dev nên trùng hướng, không phải fork |

**Kiến trúc.** TypeScript ~587k dòng (trong đó ~259k là test), Vue ~61k, vỏ desktop **Tauri v2** (Rust ~5k dòng). Vẽ bằng **Skia qua `canvaskit-wasm`** trên WebGL, layout bằng Yoga WASM. Định dạng gốc là chính **`.fig` của Figma** (Kiwi + Zstd + ZIP), cũng mở `.pen`, `.jam`, draw.io, Mermaid; xuất SVG, PDF, PPTX, HTML, ảnh, JSX/Tailwind, Storybook. Cộng tác P2P bằng **Yjs qua WebRTC (Trystero)**, báo hiệu qua MQTT công cộng và TURN công cộng `openrelay.metered.ca`.

**Tài liệu nội bộ trung thực hơn README** (như FigCraft §7e): `fig-reader.md` ghi độ trung thực trên toàn bộ corpus "chưa xong"; `export.md` liệt kê lỗ hổng (tên, liên kết style, override); `validation.md` nói chưa có quy trình so hình tự động với Figma; ma trận roadmap ghi prototyping, smart animate, version history "Not modeled".

**AI.** BYOK qua Vercel AI SDK (Anthropic, OpenAI, Google, DeepSeek, OpenRouter, endpoint tương thích); **127 tool** `defineTool`; MCP stdio và HTTP. MCP HTTP làm đúng: bind `127.0.0.1:7600`, **bearer token ngẫu nhiên mặc định**, `eval` tắt trừ khi `OPENPENCIL_MCP_EVAL=1`, giới hạn thư mục bằng `OPENPENCIL_MCP_ROOT` (riêng stdio không áp các giới hạn này, SECURITY.md tự ghi). Gọi Claude Code/Codex/Gemini qua ACP, **không truyền cờ bỏ quyền**; yêu cầu quyền hết giờ thì tự từ chối.

**Rủi ro đọc mã thấy:**

- ❌ **Chat AI trong app desktop bật tool `eval` mặc định**: chạy JavaScript do model viết bằng `new AsyncFunction` ngay trong webview chính, không duyệt, không cô lập; webview đó có quyền Tauri ghi/xoá file `**`, spawn một số tiến trình, `csp: null`. Prompt injection trong file thiết kế hay nội dung web có thể dẫn tới xoá/ghi file **(suy ra từ đọc mã, chưa thử khi chạy)**. Tắt `eval` trong Settings → AI tools khi mở file lạ.
- ⚠️ Đăng nhập ChatGPT **dùng lại client ID OAuth của Codex CLI** và gọi `chatgpt.com/backend-api/codex`: vùng xám điều khoản, có thể hỏng bất kỳ lúc nào.
- ⚠️ Bản build chính thức **gửi ping ẩn danh hằng ngày mặc định** (phiên bản, OS, arch, không ID); thống kê dùng là opt-in. Tắt bằng Settings → Privacy, `OPENPENCIL_TELEMETRY=0` hoặc `DO_NOT_TRACK`. Khớp CHANGELOG.
- ⚠️ CI rất dày (commitlint, oxlint, typecheck, jscpd ngưỡng 0, test 9 nhóm, Cloud e2e 3 backend) nhưng **548 file e2e Playwright của editor không chạy trong workflow nào** tìm được.
- ✅ Cập nhật tự động ký minisign, `requireSignedVersion: true`; bản macOS ký Developer ID và notarize; artifact có attestation. Bản Windows có vẻ chưa ký Authenticode **(chưa xác minh)**.
- Bus factor ~1; 881 commit từ 1/9/2026.

**So sánh nhanh:**

| | open-pencil | ZSeven-W/openpencil (§7p.4) | FigCraft (§7e) | Penpot |
|---|---|---|---|---|
| Ngôn ngữ | TS/Vue + Tauri | Rust | Rust | Clojure(Script) |
| License | MIT + Apache-2.0 (Cloud), sạch | MIT + thư viện xác thực đóng | MIT/Apache-2.0 | MPL-2.0 |
| File Figma | Đọc/ghi `.fig` gốc, chưa trọn vẹn (tự ghi) | Không kiểm | "Best effort" | Qua plugin |
| AI | BYOK, 127 tool, MCP, ACP; **eval bật sẵn** | MCP, ACP | CLI/MCP | Không gốc AI |

**Dùng thế nào:** hợp để đọc/chuyển `.fig`/`.pen` không giao diện qua CLI hoặc MCP (giữ token, eval tắt, đặt `OPENPENCIL_MCP_ROOT` hẹp). Dùng bản web PWA nếu không muốn cấp quyền file của desktop. Luôn giữ file `.fig` gốc. Chưa thay được Figma cho prototype hay lịch sử phiên bản.

### 7q.2 `ionic-team/ionic-framework` (Ionic 9): khỏe, MIT, nhưng do OutSystems nắm

| Mục | Thông tin |
|---|---|
| Repo | **52.734★**, 13.295 fork, 439 issue + 76 PR mở · từ 2013 · 14.820 commit, HEAD 30/10/2026 · **v9.0.10** (v9.0.0 ra 19/8/2026), phát hành vá **mỗi tuần** |
| Ai làm | 12 tháng qua 508 commit: bot ~35% (renovate, release bot), **nhân viên Ionic/OutSystems ~59%** (4–6 người), cộng đồng ~6% |
| License | MIT sạch ("Drifty Co."), không CLA |
| Kinh doanh | Blog Ionic 11/2/2025: **ngừng bán mới mọi sản phẩm thương mại** (Appflow, Identity Vault, Portals…); Appflow chạy tới 31/12/2027; Framework và Capacitor "vẫn miễn phí và mở", là lõi mobile của OutSystems |

**Kiến trúc.** Lõi web components viết bằng **Stencil** (`@stencil/core` ^4.44), bọc cho Angular, React, Vue (kèm router riêng) và SSR Angular; 97 thư mục component (~60–70 component dùng được: datetime, modal, sheet, segment, refresher, item-sliding…). Hai "mode" giao diện **iOS và Material** chọn tự động theo nền tảng (64 file SCSS mỗi mode). Capacitor chỉ là phụ thuộc phát triển, phát hiện lúc chạy. v9 cần Angular 18+, React 18/19, Vue 3.5+, iOS 16+, Capacitor 7+; **`@ionic/react-router` chưa hỗ trợ React Router 7**.

**Cổng chất lượng mạnh:** 424 spec Playwright e2e/screenshot, 213 unit test, **7.436 ảnh chuẩn** so hình, **axe-core** trong 37 file e2e, chạy trên Mobile Chrome/Safari/Firefox; CI chia 20 shard screenshot, bắt buộc check tổng; CodeQL; chạy thử hằng đêm với bản Stencil mới.

**Sẵn cho agent ở mức vừa:** có **`ionicframework.com/docs/llms.txt`** (~46 KB, mỗi trang có bản `.md`) và `core/api.txt` (API công khai, 2.109 dòng); repo **không có** `AGENTS.md`/`CLAUDE.md`, **không có MCP chính chủ** (chỉ bản cộng đồng).

**Telemetry:** framework không gửi gì. **Ionic CLI bật telemetry mặc định**: Google Analytics (mã UA cũ) + POST `api.ionicjs.com/events/metrics` kèm lệnh, đối số, UUID máy, `ionic info`, token nếu đăng nhập; tắt `ionic config set -g telemetry false` (tự bỏ khi CI hoặc không TTY). CLI gần như ngủ (commit cuối 3/2025); dùng Vite/Angular CLI + Capacitor trực tiếp cũng được.

**Đang chuẩn bị:** nhánh `next` (hơn 590 commit) thêm theme "ionic" (58 file SCSS) và phụ thuộc **`outsystems-design-tokens`**; blog v9 hẹn "Modular Ionic" quý 2/2027, tức sắp đổi lớn theo design system của OutSystems.

**Dùng thế nào:** hợp đội web (nhất là Angular) cần một mã cho iOS/Android/PWA qua Capacitor, app nội bộ nhiều form và danh sách. Ghim v9, tắt hoặc bỏ CLI, không dựa vào Appflow/Identity Vault/Portals (thay bằng Capawesome, Capgo, Codemagic). Cho agent đọc `docs/llms.txt` và `core/api.txt`. Không hợp app cần cảm giác native thật hay nhiều animation; so với React Native Reusables, Tamagui, Flutter ở §7h.

### 7q.3 `lucide-icons/lucide`: bộ icon mặc định của shadcn, license thật là ISC + MIT

| Mục | Thông tin |
|---|---|
| Repo | **25.427★**, 1.666 fork, 392 issue/PR mở · fork từ Feather (commit đầu 8/6/2020 "fork") · 3.120 commit, HEAD 30/10/2026 · **v1.66.0** (v1.0.0 ngày 23/3/2026) |
| Nhịp | 779 commit/12 tháng, tăng dần (160 trong 10/2026); **95 bản phát hành/năm**: cron hằng ngày tự tăng minor khi có icon mới (qua bước duyệt) |
| Người phát hành | Chỉ 3 người (`ericfennis`, `karsa-mistmere`, `jguddas`) được chạy release (khoá trong workflow) |
| Nội dung | **2.015 icon** (README còn ghi "1600+"), mỗi icon có JSON tags/categories (43 category); 277 alias tên cũ (274 đánh dấu deprecated, chưa có ngày gỡ); 14 gói (React, Vue, Svelte, Angular, Solid, RN, static, Astro, lab…) |

**License (lý do GitHub báo `NOASSERTION`).** File `LICENSE` gồm **ISC** cho Lucide **cộng toàn văn MIT của Feather (Cole Bemis) áp cho 115 icon gốc Feather**, liệt kê theo tên cũ (vẫn tồn tại qua tên mới hoặc alias). README và badge chỉ ghi "ISC". Dùng gói npm là đủ điều kiện (gói chép `LICENSE` vào); chép SVG thô thì phải kèm `LICENSE`. Ghi trong hồ sơ tuân thủ là **`ISC AND MIT`**. Đã **gỡ toàn bộ icon thương hiệu** (27/11/2025); workflow tự đóng issue xin logo; cần logo thì dùng Simple Icons (CC0).

**Cổng chất lượng.** Prettier + svgo ép thuộc tính gốc (24×24, `stroke-width` 2, đầu nét tròn), ESLint kiểm SVG (chỉ `currentColor`/`none`, không style inline), lint tên file, schema JSON, cspell; cả 2.015 SVG đúng viewBox và nét. Quy tắc hình học (khoảng cách, bo góc, lưới) **chỉ người duyệt**, có comment xem trước tự động; không có so hình pixel. Chuỗi cung ứng tốt: **npm provenance qua OIDC**, publish `--ignore-scripts`, action ghim SHA, `permissions: {}` mặc định. Không gói nào có postinstall, không telemetry (trang docs dùng OpenPanel, dữ liệu ở EU).

**Cho agent.** Có `llms.txt` (vitepress-plugin-llms) nhưng **trang icon bị loại** ("Not working, need investigation"); endpoint công khai `lucide.dev/api/tags`, `/api/icons/[name]`; **không có MCP chính chủ** (bản cộng đồng nhỏ, < 60★). Agent chọn icon tốt nhất qua tags trong `icons/*.json`.

**Điểm cần sửa ở README:** "1600+" (thực 2.015); "ISC" (thực ISC + MIT); ghi chú v1 "giảm 32,3% (11,4 MB → 1 MB)" tự mâu thuẫn (11,4 → 1 là ~91%).

**Tránh "giao diện Lucide mặc định"** (dấu hiệu "AI slop" mà Hallmark §7l, anti-slop §7i nhắc): Phosphor (6 độ đậm, duotone), Material Symbols (trục biến thiên, Apache-2.0), Iconoir (nét 1,5px, MIT), Heroicons solid/mini, Radix Icons (15px). Tabler gần như giống Lucide nên không giúp. Iconify cho phép đổi bộ sau một API (mỗi bộ giữ license riêng; Remix Icon dùng license riêng, cần đọc trước). Nếu giữ Lucide: đổi `strokeWidth` (1,5) và cỡ qua `LucideProvider` của v1.

**Dùng thế nào:** mặc định an toàn về pháp lý, bảo trì tốt; import từng icon, tránh `DynamicIcon` (kéo toàn bộ icon vào bundle); **ghim phiên bản** (phát hành gần như mỗi ngày) và không dùng URL CDN `@latest` như docs gợi ý. Khớp X-Templates `UX-VISUAL-010` (một bộ icon duy nhất).

**Nguồn §7q:** open-design (HEAD 12d970eac; README.md, PRIVACY.md, apps/daemon/DIAGNOSTICS.md, apps/daemon/src/{server.ts, app-config.ts, analytics.ts, daemon-startup.ts, origin-validation.ts, media/config.ts, langfuse-trace.ts, integrations/{telemetry-relay,vela}.ts, runtimes/{registry,agent-process}.ts, runtimes/defs/{claude,codex,cursor-agent,amr}.ts}, packages/contracts/src/prompts/official-system.ts, packages/diagnostics/src/agent-logs.ts, apps/web/src/{analytics/client.ts, analytics/error-tracking.ts, components/FileViewer.tsx}, apps/desktop/src/main/{runtime.ts, updater.ts, updater/payload.ts}, design-systems/{stripe,agentic,linear-app}/*, .github/workflows/{ci,release-stable}.yml, deploy/Dockerfile) · clone `--filter=blob:none` 31/10/2026: open-pencil (HEAD 9da768cf; README.md, LICENSE, REUSE.toml, SECURITY.md, CONTRIBUTING.md, CHANGELOG.md, .claude/settings.json, desktop/{tauri.conf.json, capabilities/default.json, src/credentials.rs, src/system/env.rs}, .github/workflows/{ci,build,app,heavy-tests}.yml, packages/mcp/src/{server.ts, server/lifecycle.ts, transport/origins.ts}, packages/core/src/tools/{analyze/eval/wrap.ts, registry/core.ts}, src/app/ai/{tools/catalog.ts, agents/acp/permission.ts, providers/chatgpt/oauth.ts}, src/app/telemetry/{config,state}.ts, src/app/collab/transport/trystero.ts, packages/docs/development/{roadmap,fig-reader}.md, packages/fig/docs/{export,validation}.md; so sánh lịch sử với ZSeven-W/openpencil) · ionic-framework (HEAD b01d379; LICENSE, README.md, BREAKING.md, lerna.json, core/{package.json, stencil.config.ts, playwright.config.ts, api.txt}, core/src/global/ionic-global.ts, .github/workflows/build.yml, nhánh `next` core/package.json) + ionic-cli (packages/@ionic/cli/src/lib/{telemetry,config,command}.ts) · lucide (HEAD a630cec; LICENSE, README.md, BRAND_LOGOS_STATEMENT.md, icon.schema.json, eslint.config.js, prettier-plugin-lucide-svg.mjs, .github/workflows/{ci,release,linting-icons,lint-code,close-issue-with-banned-phrases}.yml, docs/guide/version-1.md, docs/privacy.md, docs/.vitepress/config.ts) · ionic.io/blog/important-announcement-the-future-of-ionics-commercial-products · ionic.io/blog/announcing-ionic-framework-9 · ionicframework.com/docs/llms.txt (200) · GitHub search API 31/10/2026

## 7r. Quét các repo lớn còn lại liên quan UI/UX (yêu cầu người dùng, 31/10/2026)

> Sau §7p–§7q còn ~100 ứng viên từ các truy vấn GitHub. Bỏ repo lạc chủ đề (Cal.com, Nextcloud, Plausible, DocuSeal, supermemory…), giữ **46 repo** liên quan UI/UX từ ~5k★, chia 4 nhóm. Mỗi repo clone `--filter=blob:none` (đủ lịch sử nhánh mặc định), đọc LICENSE, manifest, CI, grep telemetry, kiểm 2–3 lời README; phiên bản npm đối chiếu `registry.npmjs.org/<gói>/latest`. **Không cài, không chạy script.** Số sao GitHub search API 31/10/2026; "12t/3t" = số commit trong 12 tháng / 3 tháng qua.

### 7r.1 Công cụ và skill thiết kế dùng AI

| Repo | ★ · license | Commit cuối | Là gì | Đánh giá |
|---|---|---|---|---|
| `JCodesMore/ai-website-cloner-template` | 38,3k · MIT | 5/10/2026 | Starter Next.js + một skill `/clone-website` (61 dòng) cho agent dựng lại bất kỳ URL nào | ⚠️ Skill **dặn dùng chữ, font, ảnh, SVG thật của site gốc**; README có mục "Not Intended For" nhưng skill không có bước kiểm ToS/bản quyền/nhãn hiệu. Rủi ro pháp lý dồn cho người dùng |
| `wandb/openui` | 22,7k · Apache-2.0 | 30/6/2026 | App tự host "kiểu v0": mô tả → HTML → React/Svelte/Web Components (FastAPI + LiteLLM/Ollama) | ⚠️ Gần như ngừng (commit chức năng cuối 15/9/2025, 2026 chỉ có Renovate). **Weave tự bật khi có `WANDB_API_KEY` hoặc chỉ cần có mục `api.wandb.ai` trong `~/.netrc`** → prompt có thể bị trace lên W&B không hỏi (`server.py` dòng 584–603) |
| `ConardLi/garden-skills` | 13,4k · MIT (không ghi chủ sở hữu) | 25/10/2026 | 6 skill; `web-design-engineer` 492 dòng (~9k token) + 29 "style recipe" | ⚠️ "Executable browser acceptance harness" thực ra là văn bản; **phát lại dưới MIT một file 73 KB tự nhận là system prompt "Claude Design"** (`dist/prompts/…`), nguồn gốc không rõ (cùng loại rủi ro với baoyu-design §7p.5) |
| `lnkiai/m3e-canvas` | 9,9k · MIT (+ NOTICE Apache-2.0) | 22/10/2026 | Vẽ màn Material 3 Expressive trên trình duyệt, nối thành luồng, xuất prompt cho coding agent | ✅ Tĩnh, không server, link chia sẻ nằm ở fragment URL, có vitest + CI. ⚠️ **API key lưu plaintext trong localStorage**; 7 tuần tuổi, 27% commit trailer Claude |
| `MengTo/threeui` | 7k · MIT | 1/9/2026 | Phần Community của catalog shader/Three.js thương mại ThreeUI, gói `@designcodeio/threeui` | ⚠️ Open-core (nút "Get Pro"), README ghi 50 component nhưng báo cáo đồng bộ ghi 43; demo tải từ threeui.com, CDN, Supabase |
| `twostraws/SwiftUI-Agent-Skill` | 6,4k · MIT | 26/10/2026 | Skill "SwiftUI Pro" của Paul Hudson: viết/duyệt SwiftUI theo API mới, HIG, accessibility | ✅ Gọn (~1,5k token, 12 file tham chiếu nạp theo bước). ⚠️ "Sự thật nền tảng" cứng (iOS 27, Xcode 27.1) sẽ cũ nhanh |
| `kaankiziltug/logo-design-skill` | 5,6k · MIT (trừ thư viện logo) | 20/10/2026 | Quy trình brief → concept → SVG → kiểm → bộ giao; 9 script Python | ⚠️ **Kèm 1.432 SVG logo của công ty thật** (TRADEMARKS.md: MIT không áp dụng, "chỉ để tham khảo"); `render_png.py` cần renderer ngoài dù README nói "không phụ thuộc" |
| `miurla/morphic` | 9,2k · Apache-2.0 | 28/10/2026 | Answer engine kiểu Perplexity, câu trả lời stream một spec JSON thành component (generative UI) | ✅ Trưởng thành (1.889 commit, CI lint/test/build/eval), **mọi telemetry (PostHog, Vercel, Langfuse) chỉ bật qua biến môi trường**. Mẫu tham khảo generative UI tốt hơn các repo §7p.6 |
| `bernaferrari/FigmaToCode` | 5,3k · **GPL-3.0** | 5/8/2026 | Plugin Figma chuyển tất định (không AI) sang HTML/React/Svelte/Tailwind/Flutter/SwiftUI | ✅ `manifest.json` không xin quyền, `networkAccess: none`. ⚠️ GPL nếu fork/nhúng (mã sinh ra thường không bị GPL ràng, **chưa xác minh pháp lý**) |
| `evolus/pencil` | 9,9k · **GPL-2.0** | 22/10/2026 | Công cụ wireframe Electron lâu đời **của Evolus (Việt Nam)**; v4.0.0 (20/10/2026) thêm **MCP server** cho AI vẽ lên canvas | ❌ README nói MCP "chỉ trên loopback 127.0.0.1" nhưng `app/tools/api-server.js` gọi `server.listen(port)` **không truyền host** (nghe mọi interface), `cors origin '*'`, **không xác thực, bật mặc định cổng 1919** **(đọc mã, chưa thử khi chạy)**; Electron 16 (2021, hết hỗ trợ); 530 issue mở; CI chỉ còn AppVeyor Node 6 |
| `ParthJadhav/Tkinter-Designer` | 10,3k · BSD-3-Clause | 16/10/2026 | Đọc Figma qua REST API, sinh mã GUI Tkinter | ⚠️ Gần như đứng từ 2022 (tag cuối v1.0.7 1/2023), CI dùng installer Poetry đã bị gỡ |

**Đáng chú ý cho mục 18:** Pencil là một trong số ít công cụ thiết kế mã mở do đội Việt Nam làm còn được cập nhật; nên báo lỗi MCP cho Evolus, và khi dùng thì tắt MCP (`pencil.mcp.enabled`) hoặc chặn cổng 1919.

### 7r.2 Thư viện React và tiện ích UI

| Repo | ★ · license | 12t / 3t | Bản mới nhất | React 19 | Tài sản cho AI | Đánh giá |
|---|---|---|---|---|---|---|
| `react-bootstrap/react-bootstrap` | 22,6k · MIT | 31 / 19 | 2.10.10 (5/2025); v3 vẫn beta | ✅ | – | ⚠️ Chỉ khi đã dùng Bootstrap; phát hành chậm, một người bảo trì |
| `uber/baseweb` | 9k · MIT | 49 / 9 | 18.2.0 (tag dừng ở v13, 2023) | dải peer mở, chưa kiểm | – | ❌ README: **"limiting our engagement with this repository"**; CI chỉ build, **không chạy test** (dù có 823 file test); khoá vào Styletron |
| `rsuite/rsuite` | 8,7k · MIT | 1.081 / 996 | 6.2.5 | ✅ (CI 18/19) | **MCP `@rsuite/mcp`, skill, `AGENTS.md`** | ✅ Hợp admin nhiều dữ liệu (~120 component); ghim minor vì vừa ra v6, một người chính |
| `grommet/grommet` | 8,4k · Apache-2.0 | 169 / 102 | 2.58.0 | ✅ | `copilot-instructions.md` (cho người đóng góp) | ⚠️ HPE đứng sau, chú trọng a11y (jest-axe, Chromatic), nhưng phụ thuộc styled-components; 494 issue mở |
| `primefaces/primereact` | 8,3k · MIT (các bản cũ) | 63 / 8 | 10.9.9 | ✅ | – | ❌ README: **"no longer under active development… security fixes only"**, chuyển sang PrimeUI (license bản mới chưa rõ); **xoá toàn bộ workflow CI ngày 21/9/2026** |
| `arco-design/arco-design` | 5,8k · MIT | 87 / 10 | 2.66.18 | qua adapter, CI chỉ React 18 | – | ⚠️ Ổn định nhưng chậm, Less, tài liệu Trung trước |
| `cosscom/ui` (coss ui, trước là Origin UI) | 10,8k · MIT (2 dòng copyright nên GitHub báo NOASSERTION) | 279 / 59 | không version (qua registry shadcn) | **bắt buộc** 19.2 + Next 16 | **`AGENTS.md`, `llms.txt`, skill** | ✅ Design system của Cal.com trên **Base UI + Tailwind v4**; chỉ 6 file test |
| `elastic/eui` | 6,4k · **SSPL-1.0 / Elastic License 2.0** | 566 / 196 | 123.3.0 | ❌ (chỉ 17/18) | `AGENTS.md`, `CLAUDE.md` | ❌ Ngoài hệ Elastic: **không phải license OSI** (đổi từ Apache-2.0 ngày 8/7/2021); dù vậy a11y tốt nhất nhóm (46 test Cypress + axe) |
| `react-hook-form/react-hook-form` | 44,9k · MIT | 493 / 240 | 7.91.0 (v8 beta) | ✅ | – | ✅ Chuẩn de facto cho form, 0 phụ thuộc runtime |
| `bvaughn/react-virtualized` | 27,1k · MIT | 11 / 11 | 10.0.0 (18/10/2026, viết lại TS) | chỉ v10 | – | ⚠️ README tự khuyên dự án mới dùng `react-window` (cùng tác giả) hoặc TanStack Virtual |
| `usablica/intro.js` | 23,5k · **AGPL-3.0 + license thương mại** | 104 / 41 | 8.6.0 | không áp dụng | – | ⚠️ Dự án thương mại **phải mua license**; thay bằng driver.js hoặc react-joyride (MIT) |

**Ghi nhận:** hai thư viện của công ty lớn đã rút lui công khai (Base Web của Uber, PrimeReact của PrimeTek) nhưng vẫn còn hàng nghìn sao; sao không nói gì về tình trạng bảo trì. Hai bẫy license: EUI (SSPL/ELv2) và intro.js (AGPL + bản thương mại). Không gói nào trong nhóm có postinstall hay telemetry.

### 7r.3 Vue, Angular và mobile

| Repo | Nền | ★ · license | 12t / 3t | Bản mới nhất | Tài sản cho AI | Đánh giá |
|---|---|---|---|---|---|---|
| `vueComponent/ant-design-vue` | Vue | 21,7k · MIT (3 khối MIT gộp nên GitHub báo NOASSERTION) | 12 / 0 | 4.2.6 (**11/2024**) | – | ❌ Thực tế không bảo trì: 10/12 commit gần nhất là docs/quảng cáo; nhánh `feat/vapor` chưa phát hành. **Workflow bắt mọi PR phải có trailer Co-Authored-By của Claude/Copilot/Cursor/Codex** |
| `tusen-ai/naive-ui` | Vue 3 | 18,6k · MIT | 184 / 52 | 2.45.3 (8/2026) | `AGENTS.md` | ✅ Hợp admin/dashboard Vue; 712 issue mở, phụ thuộc một người chính |
| `unovue/shadcn-vue` | Vue 3.5 + Tailwind v4 | 10,8k · MIT | 284 / 43 | CLI 2.9.0 (28/10/2026) | **`llms.txt`, MCP trong CLI, bộ skill Claude** | ✅ Mặc định cho Vue + Tailwind; sẵn cho agent nhất nhóm |
| `unovue/reka-ui` (trước là Radix Vue) | Vue (headless) | 6,9k · MIT | 455 / 150 | 2.11.0 (5/10/2026) | `CLAUDE.md`, `llms.txt` | ✅ Lớp nền của shadcn-vue và Nuxt UI; nhánh v3 sẽ có thay đổi phá vỡ |
| `NG-ZORRO/ng-zorro-antd` | Angular 22 | 9,2k · MIT | 288 / 60 | 22.1.2 (10/2026) | **`AGENTS.md`, `.claude/`, 7 skill, cấu hình MCP (Angular CLI, ESLint), `llms.txt` + `llms-full.txt`** | ✅ Lựa chọn cho Angular; major phải khớp major Angular |
| `ant-design/ant-design-mobile` | React (mobile web) | 12,1k · MIT | 51 / 9 | 5.43.0 (9/2026) | – | ⚠️ Ổn định cho H5 nhưng chậm lại, toolchain cũ |
| `akveo/react-native-ui-kitten` | React Native | 10,7k · MIT | 193 / 145 | 6.2.1 (10/2026) | `AGENTS.md`, `CLAUDE.md`, MCP thiết bị | ⚠️ **Hồi sinh 2026** (179/193 commit một người), README nói chạy New Architecture RN 0.81 **(chưa xác minh)** |
| `wix/react-native-calendars` | React Native | 10,3k · MIT | 3 / 0 | 1.1314.0 (1/2026) | – | ⚠️ Chuẩn de facto nhưng gần như đứng; tự thử trên New Architecture |
| `necolas/react-native-web` | RN → web | 22,2k · MIT | 77 / 77 | 0.21.4 (10/2026) | – | ⚠️ Nghỉ 11 tháng rồi hồi sinh 25/9/2026 dưới người dẫn mới; **0.22 có thay đổi phá vỡ** — ghim 0.21.x |
| `pure-admin/vue-pure-admin` | Mẫu admin Vue | 20,7k · MIT | 72 / 3 | v7.0.0 (4/2026) | – | ⚠️ 0 test, phụ thuộc rất nặng; dùng bản `pure-admin-thin` |
| `jd-opensource/taro-ui` | Taro (mini-program) | 4,7k · MIT | 108 / 4 | 3.4.2 (9/2026) | `SKILL.md` tiếng Trung | ⚠️ Chỉ khi đã dùng Taro 3; Taro 4 còn thử nghiệm, tài liệu chỉ tiếng Trung |

**Ghi nhận:** ba repo từng bị coi là bỏ (UI Kitten, react-native-web, taro-ui) đã hồi sinh năm 2026 nhưng đều dựa vào một người; ant-design-vue và react-native-calendars thì ngược lại, sao cao nhưng thực tế chỉ còn bảo trì tối thiểu. Các thư viện Vue/Angular đang **cạnh tranh bằng tài sản cho agent** (llms.txt, MCP, skill), giống xu hướng §7p.7.

### 7r.4 Hạ tầng design system, web components, tiện ích và danh sách

| Repo | ★ · license | 12t / 3t | Bản mới nhất | Tài sản cho AI | Đánh giá |
|---|---|---|---|---|---|
| `stenciljs/core` | 13,1k · MIT (đoạn NOTICE thêm vào nên GitHub báo NOASSERTION) | 257 / 77 (nhánh `v5` thêm 451 commit) | 4.45.2; v5.0.0-beta.27 | `CLAUDE.md` (v5) | ⚠️ Trình biên dịch web components dưới Ionic (§7q.2). **CLI v4 bật telemetry mặc định** gửi `api.ionicjs.com` (tắt `npx stencil telemetry off`; bỏ qua khi CI); **v5 gỡ hẳn telemetry**. Một người chính |
| `BuilderIO/mitosis` | 14,5k · MIT | 17 / 4 | 0.14.2 | – | ⚠️ Viết một lần, biên dịch ra ~20 framework; vẫn 0.x, nhịp giảm mạnh (143 → 17 commit/năm), CLI phụ thuộc `gluegun: "latest"` |
| `Tencent/omi` | 13,3k · MIT (bọc trong notice kiểu Tencent) | 15 / 6 | 7.7.14 (tag dừng ở 7.7.0, 2024) | – | ⚠️ Không có CI chạy được; chỉ đáng dùng cùng TDesign; dự án mới chọn Lit hoặc Stencil |
| `chakra-ui/panda` | 6,2k · MIT | 1.094 / 436 | 2.4.0 (lõi v2 viết lại bằng Rust/Oxc) | **`AGENTS.md`, skill, MCP `@pandacss/mcp`, `llms.txt`** | ✅ CSS-in-JS không runtime, CI đầy đủ (cả cargo-deny, clippy); phụ thuộc một người (Segun Adebayo) |
| `chakra-ui/zag` | 5,2k · MIT | 884 / 230 | 1.47.0 | `AGENTS.md`, `CLAUDE.md`, `context7.json`, `llms-*.txt` | ✅ 51 "máy trạng thái" component (dialog, combobox, date-picker…) cho 6 framework; lớp logic của Ark UI, Chakra v3, Skeleton v5; 69 e2e Playwright |
| `primer/css` | 13k · MIT | 179 / 70 (152 là dependabot) | 22.3.3 | – | ⚠️ README: **"This project is in KTLO mode"** (chỉ giữ chạy) từ 25/9/2025; dự án mới dùng Primer React hoặc `@primer/primitives` (vẫn sống) |
| `skeletonlabs/skeleton` | 6,1k · MIT | 313 / 11 | 5.0.1 (8/2026) | `.claude/skills` (cho người đóng góp), llms | ⚠️ Tailwind v4 + Zag; chậm hẳn sau v5.0, PR bảo mật của Renovate chưa merge từ cuối 8/2026 |
| `knadh/oat` | 5,6k · MIT | 273 / 26 | 1.0.1 (31/10/2026) | – | ✅ cho công cụ nhỏ: HTML/CSS ngữ nghĩa ~10 KB, 0 phụ thuộc (Kailash Nadh, CTO Zerodha); **không có test** |
| `golden-layout/golden-layout` | 6,7k · MIT | 9 / 0 | v2.6.0 (**2022**) | – | ❌ cho dự án mới: 4 năm không release, v3 chưa ra |
| `dicebear/dicebear` | 10k · MIT (mã) | 665 (nhánh 11.x) | 10.7.0; 11.0.0-rc.2 | llms | ✅ Avatar tất định, lõi cho 7 ngôn ngữ. ⚠️ **Mỗi style có license riêng**: CC BY 4.0 (adventurer, big-smile, micah, personas… phải ghi công), CC0 (lorelei, notionists, pixel-art…), avataaars/bottts license riêng "free for commercial use" (không phải mã mở). Nhánh mặc định là RC |
| `ekmas/neobrutalism-components` | 5,6k · MIT | 55 / 53 | (registry shadcn) | – | ⚠️ README ghi "no longer maintained" từ 7/2025 tới 11/9/2026 rồi viết lại trên Base UI; không CI, không test |
| `birobirobiro/awesome-shadcn-ui` | 20,7k · MIT | 502 / 208 | – | – | ✅ ~548 mục có cột ngày, CI kiểm link (lychee); 10 link thử: 0 chết, 2 trỏ repo đã archive, 1 đổi tên; có chỗ quảng cáo trả phí |
| `aniftyco/awesome-tailwindcss` | 15,2k · CC0-1.0 | 21 / 4 | – | – | ✅ ~74 link chọn lọc, đã gỡ thư viện không miễn phí; CONTRIBUTING **cấm bài gửi do AI viết và bài trả phí**; 1/10 link chết (`tailwindcss.com/discord`) |

### 7r.5 Mẫu chung rút ra từ 46 repo

1. **Sao không phản ánh bảo trì.** Sáu repo trên 9k★ đang ở chế độ duy trì hoặc rút lui công khai (Base Web, PrimeReact, Primer CSS "KTLO", ant-design-vue, golden-layout, react-native-calendars). Dấu hiệu đọc được ngay: banner trong README, bảng hỗ trợ trong `SECURITY.md`, CI có chạy test hay không, tag có khớp `package.json` hay không.
2. **Bẫy license ẩn sau nhãn GitHub.** `NOASSERTION` thường chỉ là MIT kèm notice (Stencil, Omi, coss ui, ant-design-vue), nhưng cũng có thể là SSPL/ELv2 (EUI) hay AGPL + thương mại (intro.js); và license theo **từng tài sản** (style DiceBear, logo trong logo-design-skill, thư viện Pencil GPL). Luôn đọc file.
3. **Tài sản cho agent thành tiêu chí chọn thư viện**: shadcn-vue, ng-zorro, rsuite, Panda, Zag, coss ui có `llms.txt`/MCP/skill; thư viện cũ hơn thì không. Hợp với X-Templates `UX-DS-019`.
4. **Máy chủ MCP cục bộ của app desktop là bề mặt tấn công mới**: Pencil (nghe mọi interface, CORS `*`, không xác thực, bật mặc định) đối lập với open-pencil (127.0.0.1, token ngẫu nhiên, eval tắt) §7q.1.
5. **Telemetry trong CLI dựng sẵn** (Stencil v4, Ionic CLI) và **trace ngầm** (wandb/openui qua `~/.netrc`) tiếp tục là thứ phải tắt chủ động; bổ sung bảng §2 của [X-TEMPLATES.md](../X-TEMPLATES.md).

**Nguồn §7r:** clone `--filter=blob:none` 46 repo ngày 31/10/2026, đọc qua `git show HEAD:<file>`: LICENSE/NOTICE, `package.json`/`pyproject.toml`, README, workflow CI, các file nêu trong bảng (ví dụ `evolus/pencil` app/tools/api-server.js; `wandb/openui` backend/openui/server.py dòng 584–603; `primefaces/primereact` README.md, SECURITY.md; `uber/baseweb` README.md, .github/workflows/pr-check.yml; `elastic/eui` LICENSE.txt; `usablica/intro.js` license.md; `stenciljs/core` src/cli/telemetry/telemetry.ts, nhánh v5 V5_PLANNING.md; `dicebear/dicebear` nhánh 9.x packages/@dicebear/*/LICENSE; `ConardLi/garden-skills` dist/prompts/; `kaankiziltug/logo-design-skill` TRADEMARKS.md) · `registry.npmjs.org/<gói>/latest` · GitHub search API 31/10/2026.

## 7s. Kiểm ảnh: Stageshow (`benjitaylor/skills`), skill dựng faux product UI của Benji Taylor (ảnh infographic người dùng gửi, clone 2026-11-02)

> Ảnh là infographic của @shannholmberg tiêu đề "The Head of Design at X open-sourced his taste", kèm lệnh `npx skills add benjitaylor/skills --skill stageshow`. Mục này clone repo (`--filter=blob:none`, HEAD `8020574`, 30/10/2026), đọc `stageshow/` (SKILL.md, 15 file `references/`, `kit/`, `scripts/`, LICENSE, NOTICE.md, package.json) và bài giới thiệu benji.org/stageshow. Đã chạy `npm ci --ignore-scripts`, `npm run typecheck` (sạch) và `npm run check:css` (sạch: 81 file CSS, không trùng namespace class). **Chưa chạy dev server và script quay phim**, vì phiên này không cho chạy server từ mã bên ngoài. Vì vậy các kết luận về chất lượng hình ảnh và về bộ dò "jump" là **(chưa xác minh)**.

### 7s.1 Hồ sơ nhanh

| Mục | Thông tin (đọc 2/11/2026) |
|---|---|
| Repo | `benjitaylor/skills` · **622★, 29 fork** (trang GitHub 2/11/2026) · repo chỉ chứa một skill là `stageshow/` |
| License | Không có LICENSE ở gốc repo. `stageshow/LICENSE` là **MIT** (© 2026 Benji Taylor). `NOTICE.md` ghi rõ các phần **không** thuộc MIT: app icon trong `assets/app-icons.ts` là PNG base64 lấy từ app bundle macOS (Mail, Calendar, TestFlight, Slack, Figma, Notion…); logo trong `kit/brands/` theo license riêng (SVGL MIT, payment-icons Apache-2.0, Cryptocurrency Icons CC0, cùng asset chính thức của Linear, Amex, Circle); tên và nhãn hiệu sản phẩm vẫn thuộc chủ sở hữu |
| Lịch sử | **1 commit** ("Add Stageshow", 30/10/2026, tác giả Benji Taylor). Không tag, không release, không CI, không issue tracker có nội dung. Bài giới thiệu đề ngày 31/10/2026 |
| Tác giả | Benji Taylor (@benjitaylor). X thuê làm trưởng thiết kế từ 25/3/2026, theo The Block, PYMNTS và KuCoin; các báo gọi chức danh khác nhau ("head of design" / "design lead"). Trước đó anh dẫn thiết kế ở Base (Coinbase), đồng sáng lập ví Family (Aave mua lại). Là tác giả Agentation (§7p.5, 5,2k★, PolyForm Shield) |
| Kích thước | 363 file, 3,4 MB. SKILL.md 149 dòng (~18,6 KB, ~4,5k token); 15 reference 1.419 dòng (~158 KB, ~40k token nếu đọc hết). `kit/` ~5,5k dòng TS/TSX, `scripts/` ~4k dòng `.mjs`, **69 thư mục ví dụ**, 18 file `teaching/` (9 cặp tsx+css) |
| Stack | React 18, TypeScript, CSS thuần, `lucide-react` 0.468.0. Playground dùng Vite 6. Script quay phim dùng `playwright-core` ~1.48 và **Chrome có sẵn trên máy** (`channel: 'chrome'`, hoặc chỉ định bằng `CHROME_PATH`). `portless` là phụ thuộc tùy chọn, chỉ để dev server có URL tên `stageshow` |
| Cài | `npx skills add benjitaylor/skills --skill stageshow` (CLI `skills` của Vercel, chép thư mục skill vào thư mục skill của agent). Muốn quay phim hay xem ví dụ thì phải `npm install` trong thư mục skill (Node ≥ 20.19) |

### 7s.2 Kiểm từng ô trong ảnh

| Ô trong ảnh | Thực tế (đọc mã) | Kiểm |
|---|---|---|
| Câu "It reads as a real product, simplified to what the viewer needs, framed with intent, and every motion has a cause" | Đúng nguyên văn mục "The one idea" của SKILL.md | ✅ |
| 5 kiểu hỏng: Too much / Too little / Boxed / Flat / Bland | SKILL.md có đủ 5 kiểu, nhưng tên thứ hai là **"Wireframe"** chứ không phải "Too little". Bài giới thiệu dùng "too little" | ✅ (khác tên) |
| 7 bước: Medium, Look, Story, Examples, Screen, Choreograph, Rehearse | Khớp 7 bước của Workflow. Bước 1 trong mã là "Medium and place", bước 4 là "Start from an example" | ✅ |
| "One scene, 4 looks: light, dark, blueprint or minimal" | Sai. `kit/looks.ts` có **4 theme: `light` · `dark` · `blueprint` · `glass`**. `minimal` là một mức **fidelity** (`minimal` / `standard` / `realistic`), là trục riêng. Ngoài ra còn trục palette `accent` / `mono` | ❌ |
| "Your design tokens… read from your design system" | `references/looks.md` hướng dẫn agent **ánh xạ tay** token của sản phẩm sang token của kit. Không có công cụ tự đọc design system | ⚠️ thủ công |
| "Motion the kit handles: avatar flies… numbers roll only the digits that change" | Kit có `Fly`, `Roll`, `Count` cùng `Collapse`, `Swap`, `Connector`, `Follow`, `States`, `Stream`, `Popover`, `Scroll`, `Camera`, `Expand` | ✅ |
| "A camera: push in, pull back" | Có `Camera` trong kit | ✅ |
| Đoạn mã beat 3: `a.click({ at: "share" })`, `a.move({ x: 600, y: 300 })` | Ảnh tự ghi là "his code, shortened". API thật là `click(to?: Target, opts?)` và `set(patch)` trong `kit/act.ts`; mục tiêu đánh dấu bằng `data-target` rồi đo bằng `rect()`, SKILL.md cấm ghi cứng tọa độ. Cú pháp `{ at: … }` trong ảnh là **giả mã**, đừng chép | ⚠️ minh họa |
| "Dozens of gold examples" | Bảng Gold trong SKILL.md có **41 dòng** (vài dòng gộp nhiều ví dụ), 11 dòng "product study" và 5 dòng specimen; tổng cộng 69 thư mục `examples/` | ✅ |
| `scripts/`: "Film, catch jumps, check layout" | Có `film.mjs` (contact sheet, `--gate`, `--states`, `--hover`, `--zoom target:`), `jumps.mjs`, `layout.mjs`, `class-clash.mjs`, `motion-watch.mjs`. `film.mjs` ghi lại hình học **mỗi animation frame** và báo `jump:` / `drift:`; mã thoát 2 khi dữ liệu thu được không đủ ("inconclusive"), tức phân biệt "trượt" với "không đo được" | ✅ (chưa chạy) |
| `playground`: "Bad and good, side by side" | Cặp xấu/tốt nằm ở `teaching/` (đọc kèm `references/teaching.md`); `playground/` là trình xem Vite cho mọi ví dụ, có route `?capture=<tên>` để quay | ⚠️ gộp hai thư mục |
| "Works in Grok Build, Claude Code, Codex and Gemini" | Repo không có nội dung riêng cho host nào; SKILL.md là frontmatter chuẩn Agent Skills. Bài giới thiệu nêu Claude Code, Codex, Gemini; **"Grok Build" chỉ thấy trong ảnh** | ⚠️ Grok (chưa xác minh) |
| Vòng "Compare side by side → Write down what looks off → Update the skill → rerun from scratch" | Bài giới thiệu tả đúng như vậy: một agent mới có skill so với cùng prompt không có skill; tác giả ghi lại chỗ sai chứ không tự sửa output, rồi chạy lại từ đầu. **Repo không có harness eval, dữ liệu so sánh hay kết quả nào** | ⚠️ chỉ có lời kể |
| "732K views, 16.7K bookmarks trong khoảng một ngày" | Số từ bài đăng trên X, không kiểm được từ phiên này | (chưa xác minh) |

### 7s.3 Điều ảnh không nói (đọc mã)

- **Kiểm chứng bằng phim là điểm khác biệt thật.** `references/rehearse.md` định nghĩa một bảng dòng báo "không bao giờ là cố ý" (`framing:`, `cut by the crop:`, `tight stack:`, `tight mark:`, `tight inset:`…). `film.mjs --gate` chỉ in `rehearsal passed` khi tất cả bằng 0. Skill cấm "sửa" một dòng báo bằng cách ẩn phần tử hay gắn `data-crop` / `data-snap`. Ngay sau đó skill tự nói "necessary, not sufficient": qua gate chưa phải là đạt.
- **Người review ngữ cảnh mới chỉ được nhìn hình.** `references/review.md` quy định reviewer chỉ nhận `verify.md`, thư mục ví dụ, URL và các khung hình; **không** nhận kế hoạch hay lý do của người dựng, và không nhận `REHEARSAL.md`. Mọi phát hiện phải trỏ tới một file khung hình cụ thể, và "đoán trước một lỗi" không được tính là phát hiện. Cuối cùng phải nộp `REHEARSAL.md` ghi ví dụ gold đã chép, những gì đã đổi và **những gì chưa kiểm**.
- **Chi phí ngữ cảnh cao.** SKILL.md bắt đọc `craft.md` "in full", rồi `framing.md`, `motion.md`, `rehearse.md`, `verify.md`, `teaching.md` và phần `kit.md` của các part dùng tới; thêm cả mã ví dụ gold sẽ chép. Một lượt dựng thực tế dễ tốn hàng chục nghìn token.
- **Chỉ dành cho React.** Kit là component React kèm CSS riêng. Dự án Vue, Svelte hay HTML tĩnh phải tự chuyển, hoặc dựng trong một đảo React riêng.
- **Phạm vi hẹp và có chủ đích:** chỉ làm minh họa giao diện giả (hero, feature card, bento, demo con trỏ), không dựng UI thật. Các hàm `a.click()` / `a.set()` chỉ vẽ con trỏ và đổi state, không điều khiển trình duyệt.
- **Bảo mật:** không `postinstall`, không telemetry, không gọi mạng lúc chạy (NOTICE ghi playground không tải font hay ảnh từ ngoài; grep `scripts/` và `kit/` không thấy `fetch`, chỉ có `xmlns`). `child_process` chỉ dùng để chạy lại chính `film.mjs` khi dev server reload và để khởi động Vite/portless.
- **Rủi ro nhãn hiệu:** ví dụ mô phỏng Figma, Linear, Slack, Notion, Gmail, Spotify, Office…, kèm app icon thật lấy từ app bundle. Đem lên trang marketing thật thì phải thay bằng sản phẩm của mình. `references/products.md` cũng dặn "borrow the interaction, not another product's identity".
- **Tuổi đời:** mới 1 commit và chưa có lịch sử bảo trì. `lucide-react` ghim cứng `0.468.0`, `playwright-core` `~1.48.2` (mới nhất đã 1.5x), nên cần kiểm Chrome hệ thống có tương thích không.
- Tác giả tự nhận trong bài viết: skill "phản ánh gu của tôi, không trung lập"; vòng đầu "thường tiến một bước lớn" nhưng vẫn cần vài vòng góp ý; bộ kiểm "bắt lỗi chứ không bắt ý tưởng nhạt"; skill không vẽ được minh họa hay ảnh chụp.

### 7s.4 So với các mục đã có

| | Stageshow | Hallmark (§7l) | Taste Skill (§7j) | transitions.dev (§7p.5) | Remotion / HyperFrames skill (mục 22 §2) |
|---|---|---|---|---|---|
| Sản phẩm đầu ra | Minh họa UI giả (ảnh tĩnh hoặc loop) nhúng vào trang | Trọn một trang marketing | Luật thẩm mỹ cho UI thật | Chuyển cảnh và motion UI | Video MP4 |
| Kit kèm theo | **Kit React** (Stage, Window, Phone, Act, 13 primitive motion) + 69 ví dụ | 48 theme | Không | Có thư viện luật | Engine chính thức |
| Cổng máy | Quay phim (contact sheet), dò nhảy hình học từng frame, layout, trùng class; `--gate` | `sloplint` + Puppeteer nếu có Chrome | Inspector trên trình duyệt | Rule CLI | Render |
| Review | Ngữ cảnh mới, **chỉ nhận khung hình** | Ngữ cảnh mới (Claude Code/OpenCode) | Không | Không | Tùy skill |
| License | MIT (trừ icon/logo) | MIT | MIT | License riêng, cấm phân phối lại thư viện | Remotion: công ty ≥ 4 người phải mua license; HyperFrames Apache-2.0 |

Stageshow khác các skill thiết kế khác ở chỗ: (1) chọn "ví dụ gold gần nhất" rồi **chép và sửa**, không viết lại từ đầu; (2) kiểm motion bằng **chuỗi khung hình**, vì một ảnh chụp bỏ qua chuyển động ở giữa; (3) có luật cấm "sửa lỗi bằng cách giấu lỗi".

### 7s.5 Dùng thế nào

- **Hợp:** hero, feature card và bento minh họa sản phẩm trên trang marketing hay docs của dự án React, khi có người để duyệt từng vòng.
- **Cài:** đừng cài vào repo dữ liệu như kho này. Cài vào dự án site, ghim theo commit (`benjitaylor/skills@8020574`), vì CLI `skills` lấy nhánh mặc định. Chép `kit/` vào dự án như hướng dẫn, và giữ `NOTICE.md` cùng license riêng của `kit/brands/`.
- **Trước khi dùng:**
  - xoá app icon và logo không thuộc mình khỏi bản phát hành;
  - đặt `CHROME_PATH` (CI Linux thường không có `channel: 'chrome'`);
  - chạy `npm run typecheck` và `npm run check:css` sau mỗi lần sửa kit.
- **Dùng lại từng phần, kể cả khi không làm faux UI:**
  - quy ước "reviewer chỉ nhận hình, không nhận lý do của người dựng";
  - bảng dòng báo "không bao giờ là cố ý", cùng luật cấm làm cho cổng xanh bằng cách giấu lỗi;
  - `REHEARSAL.md` ghi rõ phần **chưa kiểm**;
  - mã thoát 2 cho kết quả "inconclusive" (giống XT-H-029).
- **Không cần** nếu chỉ cần ảnh chụp sản phẩm thật, hoặc cần video dài: dùng Remotion hay HyperFrames (mục 22).

**Nguồn §7s:** clone github.com/benjitaylor/skills 2/11/2026 (`--filter=blob:none`, 1 commit, HEAD 8020574 30/10/2026; README.md, AGENTS.md, CLAUDE.md, stageshow/{SKILL.md, LICENSE, NOTICE.md, package.json, references/{rehearse,review,looks,…}.md, kit/{looks.ts, act.ts}, scripts/{film,browser,dev}.mjs, assets/app-icons.ts}); chạy `npm ci --ignore-scripts`, `npm run typecheck`, `npm run check:css` (Node 22.23) · github.com/benjitaylor/skills (622★, 29 fork, 2/11/2026) · benji.org/stageshow (31/10/2026) · tác giả: theblock.co/post/395222/elon-musk-taps-benji-taylor, pymnts.com/?p=3595047, kucoin.com/news/flash/x-platform-appoints-benji-taylor-as-head-of-design · tìm web 2/11/2026 không thấy bài review độc lập nào về Stageshow · số view/bookmark trong ảnh lấy từ bài đăng X (chưa xác minh)

## 7t. Nâng trần 2/11/2026: nền móng token/màu/chữ và cổng máy cho frontend (a11y, visual regression, hiệu năng, lint CSS) (yêu cầu người dùng)

> Người dùng yêu cầu "nâng trần cho UI/UX và frontend design". Mục 06 đã có rất nhiều skill "gu" (§4, §7g, §7i, §7j, §7l, §7m, §7s). Đợt này bổ sung hai lớp còn thiếu: **nền móng** (chuẩn token, thang màu, chữ) và **cổng máy** biến "đẹp, dùng được" thành con số. Số sao, license và ngày push đọc bằng GitHub search API ngày 2/11/2026. Clone `--depth 1 --filter=blob:none` 17 repo, đọc LICENSE, README, `package.json`, CI và file chính. **Không cài, không chạy mã của repo nào.**

### 7t.1 Trần hiện tại

- **Gu thì nhiều, thước đo thì ít.** Phần lớn skill §7g–§7s là prompt. Cổng máy đã có đều nằm trong từng skill và chỉ đo đúng skill đó: `sloplint` (§7l), inspector của Taste (§7j), 52 cổng của XIAS có axe (§7d), `film.mjs --gate` (§7s), 6 luật `@shadcn/lint` (§7p.3), Drift Gate của dembrandt (§7p.4). Kho chưa có hồ sơ cho chính các **engine** mà những cổng này dựa vào: axe-core, stylelint, jsx-a11y, so ảnh.
- **Token chưa theo chuẩn.** DESIGN.md (§7c) có YAML token, nhiều skill kèm `tokens.css` riêng, nhưng chưa nối với **DTCG 2025.10**, định dạng token chung mà Figma, Style Dictionary và các công cụ trích token (§7p.4) đang hội tụ về.
- **Màu và chữ dựa vào lời dặn.** Lỗi tương phản lặp lại nhiều lần: Ant Design 4,10:1 (§7c.3), "18px" sai định nghĩa chữ lớn (§7i.3). Chưa có thang màu nào được thiết kế sẵn theo mức tương phản, và chưa có công cụ căn chữ theo metric của font.
- **Chưa có visual regression.** Không mục nào chụp ảnh UI rồi so với bản đã duyệt. Lighthouse CI đã có trong catalog (mục 13) nhưng commit cuối là 26/6/2025.

### 7t.2 Bảng repo và chuẩn mới

| Repo / chuẩn | Lớp | ★ · license (2/11/2026) | Commit cuối | Vì sao nâng trần | Rủi ro |
|---|---|---|---|---|---|
| W3C **WCAG 2.2** (w3.org/TR/WCAG22) | Chuẩn | – · W3C Document License | Rec 10/2023; ISO/IEC 40500:2025 | Thước đo chung cho a11y. Từ 10/2025 WCAG 2.2 cũng là chuẩn ISO, nên dễ được viện dẫn trong luật và hợp đồng | Bản ISO là văn bản 10/2023, không gồm các bản sửa sau đó |
| `design-tokens/community-group` (DTCG) | Chuẩn | 2,2k · W3C Software and Document License | 8/9/2026 | Format, Color và Resolver Module bản **2025.10**, kèm JSON Schema (`schemas/src/2025.10/`) và test-suite có cả ca hợp lệ lẫn ca phải bị từ chối. Dùng để kiểm `tokens.json` tự động | Là báo cáo của Community Group, không phải W3C Recommendation; mã nguồn spec vẫn ghi `specStatus: 'CG-DRAFT'` |
| `vercel-labs/web-interface-guidelines` | Chuẩn (thực hành) | 1,1k · MIT | 5/10/2026 | 130 quy tắc cụ thể (vùng chạm ≥24px, mobile ≥44px; `:focus-visible`; không `transition: all`; URL lưu state…). `command.md` là bản rút gọn MUST/SHOULD/NEVER để agent review code. Cùng nội dung và văn phong với `raunofreiberg/interfaces` (Rauno Freiberg làm ở Vercel), nhưng bản này có license; quan hệ giữa hai repo **(chưa xác minh)** | Chỉ là prompt, không có CI. `install.sh` dùng `curl` tải `command.md` từ `main` mà không ghim phiên bản. **Tự mâu thuẫn**: mục "Mobile input size" gợi ý `maximum-scale=1`, ngay sau đó lại có quy tắc "Never disable browser zoom" |
| `addyosmani/web-quality-skills` | Cổng máy (skill) | 3,0k · MIT | 24/8/2026 | 6 skill (audit, performance, Core Web Vitals, a11y, SEO, best practices) theo hướng **đo trước**: phân biệt dữ liệu thực địa CrUX/RUM với trace lab, dùng Lighthouse qua Chrome DevTools MCP. `analyze.sh` chỉ đọc, xuất JSON | Tự ghi "unofficial". 34 commit, không CI. `analyze.sh` dùng grep HTML nên chỉ là sàng lọc thô. Mỗi SKILL.md 10–14 KB |
| `dequelabs/axe-core` | Cổng máy (a11y runtime) | 7,7k · MPL-2.0 | 21/10/2026 | Engine a11y chuẩn ngành: 105 luật (WCAG 2.0/2.1/2.2 A–AAA và best practice), v4.14.0, CI có test nightly và so sánh hiệu năng. README tự nói chỉ bắt được **trung bình 57%** lỗi WCAG; các ca không chắc chắn trả về `incomplete` để người kiểm | MPL-2.0 là copyleft theo file: sửa file của axe thì phải công bố phần sửa. 43% lỗi còn lại vẫn cần người kiểm |
| `jsx-eslint/eslint-plugin-jsx-a11y` | Cổng máy (a11y tĩnh) | 3,6k · MIT | 3/1/2026 | 39 luật bắt lỗi a11y ngay trong JSX, trước khi render; chạy chung với `@shadcn/lint` (§7p.3) | v6.10.2; peerDeps chỉ tới **ESLint ^9**. PR thêm ESLint 10 chưa được merge (tới 4/2026), có người chuyển sang fork `jsx-a11y-x` **(chưa xác minh)**. Commit cuối cách đây 10 tháng |
| `stylelint/stylelint` | Cổng máy (CSS) | 11,5k · MIT | 29/10/2026 | 154 luật, có `color-no-hex`, `declaration-property-value-allowed-list`, `no-unknown-custom-properties`. Đủ để cấm màu và giá trị ngoài token trong CSS thuần, phần mà `@shadcn/lint` (chỉ Tailwind) không phủ | Nhánh chính đang ở `18.0.0-next.0`; ghim bản stable |
| `style-dictionary/style-dictionary` | Nền móng (token build) | 4,9k · Apache-2.0 | 28/10/2026 | Một nguồn token → CSS, iOS, Android, JS. Bản 5.7 hỗ trợ DTCG (`usesDtcg`, kiểu `duration` 2025.10). 5.7.1 vá một lỗi prototype pollution | Hỗ trợ Resolver Module 2025.10 chưa rõ **(chưa xác minh)**. Cần Node ≥ 22 |
| `radix-ui/colors` | Nền móng (màu) | 1,7k · MIT | 17/12/2025 | 12 bước mỗi thang, mỗi bước có vai trò định sẵn (nền, viền, chữ), kèm cặp sáng/tối và alpha. Là thang màu của Radix Themes | Đứng yên gần 11 tháng (v3.0.0) |
| `evilmartians/harmony` | Nền móng (màu) | 249 · MIT | 24/7/2026 | Thang OKLCH: các màu cùng mức sáng có cùng tương phản, có bản P3; thay thẳng được bảng màu Tailwind | Tính theo **APCA**, mà APCA có license hạn chế (xem dưới). Sao thấp |
| `seek-oss/capsize` | Nền móng (chữ) | 1,7k · MIT | 15/10/2026 | Căn chữ theo cap height bằng metric của font, cắt khoảng trống thừa trên và dưới, nên spacing đo được giữa chữ và khối khác. v4.1.3 | Cần metric đúng của font đang dùng; đổi font thì phải sinh lại |
| `argos-ci/argos` | Cổng máy (visual regression) | 656 · MIT | 30/10/2026 | Nền tảng review ảnh chụp trong PR (Playwright, Storybook, Cypress), so ảnh bằng `odiff-bin` | Mã mở, nhưng tự host cần Postgres, RabbitMQ, Redis, DynamoDB, S3 và GitHub App. Không thấy tài liệu tự host trong repo; thực tế là SaaS **(chưa xác minh bản tự host chạy được)** |
| `mapbox/pixelmatch` | Cổng máy (so ảnh) | 7,0k · ISC | 6/10/2026 | Khoảng 600 dòng, không phụ thuộc. Tính sai khác màu bằng OKLab và HyAB, nhận ra pixel khử răng cưa. v8.0.0. Hợp để tự viết cổng so ảnh trong CI mà không cần SaaS | Chỉ so pixel, không hiểu bố cục. Cần chụp ảnh ổn định (font, animation, dữ liệu giả) |

**Đã xem nhưng không thêm:**

- `raunofreiberg/interfaces` (2,0k★): **không có LICENSE**, commit cuối 6/2023. Dùng bản Vercel ở trên, có MIT.
- `lost-pixel/lost-pixel` (1,7k★): **đã archive**.
- `garris/BackstopJS` (7,2k★, MIT, v6.3.25, kéo theo cả Puppeteer lẫn Playwright) và `reg-viz/reg-suit` (1,3k★, MIT, commit cuối 16/3/2026): phương án so ảnh tự host thay Argos.
- `Myndex/apca-w3` (216★, GitHub báo `NOASSERTION`): LICENSE.md ghi "All Rights Reserved", "Patent(s) pending" và "W3 License for Compliant Code Only" (cấp cho W3 "on a limited basis", chỉ cho nội dung web theo thỏa thuận hợp tác với W3C; ngoài phạm vi đó áp dụng "AGPU v3" — nguyên văn, có lẽ là lỗi gõ của AGPL v3), "Patent(s) pending" và "Limited W3 License". Chỉ được dùng cho nội dung web theo thỏa thuận với W3C; ngoài phạm vi đó thì theo AGPL v3 (văn bản viết nhầm thành "AGPU"); cài đặt sai thuật toán bị coi là vi phạm bản quyền. APCA chưa thuộc WCAG 2.x. **Không nhúng mã APCA vào sản phẩm.** Khi cần cổng hợp chuẩn, đo bằng tỉ lệ tương phản WCAG 2.
- `argyleink/open-props` (5,6k★, MIT) và `fontsource/fontsource` (6,3k★, MIT): hữu ích, nhưng không thêm lớp đo nào mới.
- `GoogleChrome/lighthouse-ci`: đã có ở mục 13 và đứng yên từ 6/2025. `web-quality-skills` thay bằng Lighthouse qua DevTools MCP.

### 7t.3 Stack nâng trần frontend (xếp theo lợi ích/công sức)

1. **Lint tĩnh trong pre-commit và CI (vài giờ).** Dùng `eslint-plugin-jsx-a11y` cùng `@shadcn/lint` (§7p.3) cho JSX/Tailwind, `stylelint` (`color-no-hex`, `declaration-property-value-allowed-list`) cho CSS. Thông báo lỗi chính là "gu" ở dạng máy đọc được: agent sửa theo lỗi chứ không theo lời dặn.
2. **axe-core trong test trình duyệt (1 ngày).** Chạy `@axe-core/playwright` (gói của Deque, **chưa đọc mã**) trên mỗi route và trạng thái chính, chặn PR khi có lỗi `serious`/`critical`. Phần `incomplete` đưa cho người review. Lấy thêm các script trạng thái và vùng chạm của XIAS (§7d.4) để phủ phần axe không đo.
3. **Token theo DTCG (2–3 ngày).** Viết `tokens.json` theo Format 2025.10, kiểm bằng JSON Schema của DTCG trong CI, build bằng Style Dictionary ra biến CSS và theme Tailwind. DESIGN.md (§7c) và `designlang`/dembrandt (§7p.4) đều xuất DTCG, nên token trích từ web và token tự viết dùng chung một đường. Màu lấy từ Radix Colors (vai trò từng bước rõ) hoặc Harmony (OKLCH); lớp chữ dùng Capsize.
4. **Visual regression (1–2 ngày).** Lưu ảnh chụp Storybook hoặc trang mẫu ở các khổ 375, 768, 1440 và 280px (§7d), so bằng pixelmatch (tự host) hoặc Argos (SaaS). Bổ sung cho `film.mjs --gate` của Stageshow (§7s), vốn kiểm chuyển động chứ không kiểm hồi quy giữa hai commit.
5. **Hiệu năng và review cuối (liên tục).** Dùng `web-quality-skills` để agent đo LCP, INP, CLS bằng trace rồi mới sửa. Dùng `command.md` của Vercel cho lượt review UI, sau đó mới tới các skill gu (frontend-design §7g.3, Taste §7j, Hallmark §7l, emilkowalski/skills §7m.1). Thứ tự hợp lý: **cổng máy xanh trước, gu sau**, để skill gu không phải sửa lỗi a11y và người duyệt không phải soi lỗi máy bắt được.

**Nguồn §7t:** GitHub search API 2/11/2026 (`repo:` cho 20 repo) · clone `--depth 1 --filter=blob:none` 2/11/2026: vercel-labs/web-interface-guidelines (HEAD 434b7f9, 5/10/2026; README.md, command.md, AGENTS.md, install.sh, LICENSE; 60 commit từ 9/9/2025), addyosmani/web-quality-skills (afa8da9, 24/8/2026; README.md, skills/*/SKILL.md, skills/web-quality-audit/scripts/analyze.sh, LICENSE; 34 commit), dequelabs/axe-core (6b52b84, 21/10/2026; README.md, LICENSE, package.json, lib/rules/, doc/rule-descriptions.md, .github/workflows/), jsx-eslint/eslint-plugin-jsx-a11y (8f75961, 3/1/2026; package.json, src/rules/), stylelint/stylelint (106c1f0, 29/10/2026; package.json, lib/rules/), design-tokens/community-group (882ebd6, 8/9/2026; README.md, LICENSE.md, technical-reports/, schemas/, test-suite/), style-dictionary/style-dictionary (3815256, 28/10/2026; README.md, package.json, CHANGELOG.md, lib/), radix-ui/colors (dbdb854, 17/12/2025), evilmartians/harmony (6dae4f3, 24/7/2026), seek-oss/capsize (1fcf40a, 15/10/2026), argos-ci/argos (0b85846, 30/10/2026; LICENSE, docker-compose.yml, .env.example, infra/README.md, apps/backend/package.json), mapbox/pixelmatch (ab76f52, 6/10/2026; LICENSE, README.md, index.js), Myndex/apca-w3 (6c5c066, 6/5/2026; LICENSE.md, package.json), garris/BackstopJS (a11d365), reg-viz/reg-suit (5c09c8e), raunofreiberg/interfaces (81f523a, 6/6/2023), argyleink/open-props (f39ab7c) · https://www.w3.org/WAI/news/2025-10-21/wcag22-iso · https://www.w3.org/TR/WCAG22/ · https://www.designtokens.org/TR/2025.10/ · ESLint 10 và jsx-a11y: github.com/jsx-eslint/eslint-plugin-jsx-a11y/pull/1081, github.com/peerigon/configs/issues/213

## 7u. Nâng trần 2/11/2026: quốc tế hóa và kiểm chứng giao diện đa ngôn ngữ (mở rộng cùng ngày)

<a id="i18n-lifecycle-2026-11-02"></a>

> §7t đã phủ token, a11y và so ảnh; phần này xét giao diện còn dùng được sau khi đổi ngôn ngữ, dữ liệu địa phương và độ dài chữ. Đọc code ba repo, LICENSE và CI tại HEAD ghi dưới; metadata GitHub API ngày 2/11/2026. **Không cài/build/chạy** các dự án ngoài; không coi mô tả chức năng là kết quả benchmark.

### 7u.1 Khoảng trống và hồ sơ ba lớp

Một UI vượt qua axe và pixelmatch bằng tiếng Anh vẫn có thể mất dấu tiếng Việt, cắt nút khi chuỗi dài, sai số tiền hoặc đọc sai plural. Mục 18 §5b đã có NFC, cách đặt dấu và parity en/vi; bổ sung ở đây là vòng **extract → dịch → review → compile → render theo locale**, không thay các cổng nội dung tiếng Việt đó.

| Dự án · tác giả/tổ chức | ★ · license (2/11/2026) | HEAD đọc · commit cuối | Cơ chế đã đọc | Điểm phải kiểm khi tích hợp |
|---|---|---|---|---|
| **i18next** · hệ sinh thái i18next/Locize | 8.660 · MIT | `b84e4180d71d271b9ae1f19ebb668224069b435e` · 1/11 | Runtime JS đa framework; `PluralResolver.js` dùng `Intl.PluralRules`; `defaults.js` mặc định `interpolation.escapeValue: true`; CI chạy lint/test/type | Runtime có fallback plural `one/other` khi không tạo được rule. Trang cũ và runtime thiết bị có thể không cùng dữ liệu Intl; fallback dịch làm UI có chữ nhưng không chứng minh đúng locale |
| **Lingui** · cộng đồng Lingui, repo có bản quyền Tomáš Ehrlich/Crowdin | 5.934 · MIT | `cbf16e9825cea76408ce06da02980ba57c8ea6c0` · 2/11 | Extract/macro biến JS/JSX thành ICU MessageFormat, catalog rồi compile; `pseudoLocale` hỗ trợ kéo dài chữ và RTL. CI build và test Node 22/24 trên Linux/Windows | Macro cần build integration phù hợp. **`compile --strict` kiểm thiếu sau khi áp `fallbackLocales`**: xanh vẫn có thể là câu tiếng Anh thay cho tiếng Việt; phải đo completeness của chính catalog đích |
| **Weblate** · cộng đồng Weblate, dịch vụ hosted riêng | 6.149 · **GPL-3.0-or-later** theo README/SPDX, license các phần khác xem `LICENSES/` | `9106f6a31fdeae6fc9e57a3bc1ffc3979824213d` · 2/11 | Nền tảng dịch đồng bộ VCS, glossary, translation memory, check placeholder và workflow reviewer; `docs/workflows.rst` phân biệt suggestion/translated/approved | Review cần bật và cấp quyền đúng theo ngôn ngữ; mặc định bảng workflow không bật review. Dịch máy/memory không tương đương duyệt của người. Tự host có chi phí vận hành và phải xét license khi sửa/phân phối Weblate |

**Phạm vi so sánh:** i18next và Lingui là hai cách triển khai runtime/catalog, không cần dùng cả hai cho một UI. Weblate là lớp cộng tác dịch bên trên file catalog; PO/Gettext của Lingui và JSON của i18next cần cấu hình format khác nhau. Các lựa chọn khác để đối chiếu là FormatJS/react-intl, quy trình PR thuần git và các dịch vụ quản lý bản dịch; chưa đọc mã các lựa chọn đó trong đợt này **(chưa xác minh)**, không gắn nhãn thắng/thua.

### 7u.2 Cổng máy nào chứng minh điều gì

| Câu hỏi | Bằng chứng phù hợp | Giới hạn |
|---|---|---|
| Mọi thông điệp đã được đưa ra catalog? | Diff extract trong CI; đếm chuỗi còn hard-code ở phạm vi đã khai báo | Extract không tìm được mọi chuỗi tạo động/response server; ghi rõ phần loại trừ |
| Catalog tiếng Việt có dịch đủ? | Số message thiếu/fuzzy của **vi trước fallback**, placeholder/plural đúng schema | Build xanh và fallback tiếng Anh không chứng minh hoàn thành dịch |
| UI chịu được ngôn ngữ khác? | Pseudo-locale kéo dài chữ, RTL giả lập; ảnh màn hình thực tế của en/vi và locale mục tiêu | Pseudo-locale không chấm chất lượng dịch; ảnh tĩnh chưa đo đọc màn hình hay hoàn thành tác vụ |
| Ngày, số tiền, timezone và plural đúng? | Fixture theo locale bằng Intl/CLDR; tách timezone dữ liệu và timezone hiển thị | Không ghép chuỗi như “1 + items”; runtime/CLDR khác phiên bản có thể cho kết quả khác |
| Thuật ngữ/dấu/cách xưng hô đúng? | Glossary theo sản phẩm + reviewer bản ngữ + luật ở mục 18 §5b | Check placeholder/ICU không hiểu nghĩa nghiệp vụ |

Chuẩn tham chiếu là **ECMA-402** cho API Intl và **Unicode CLDR/UTS #35** cho quy tắc địa phương; trang ECMA-402 hiện là bản nháp sống nên phải ghi phiên bản engine thực tế. Không suy quy tắc plural ngôn ngữ đích từ tiếng Anh. Với HTML do ứng dụng tự chèn, `escapeValue: false` cần được đánh giá theo đường render; không tắt escape toàn cục chỉ để bản dịch có markup.

### 7u.3 Kiến trúc ghép và cách chọn

Với ứng dụng nhiều framework hoặc JSON catalog sẵn, i18next là ứng viên runtime; ứng dụng muốn extract/macro/ICU và biên dịch message có thể chọn Lingui. Giữ **catalog + source locale + glossary + phiên bản công cụ** trong git, đồng bộ sang Weblate nếu cần nhiều người dịch. Quy trình reviewer chỉ được coi là cổng phát hành khi đã cấu hình quyền/trạng thái cho dự án cụ thể.

Luồng tham chiếu: component/route → extract → bản dịch có placeholder và glossary → review → compile/check thiếu **trước fallback** → Playwright theo locale → axe/so ảnh ở §7t → kiểm nội dung Việt ở mục 18. Đặt date/number/currency formatter ở một lớp chung; xác định rõ locale và timezone của từng màn hình. Font phải có glyph tiếng Việt và test input method, dấu tổ hợp, tên dài trên thiết bị thật.

**Đã đổi từ phần trước:** đây là phần còn thiếu sau việc đo màu/a11y/hiệu năng, không bổ sung thêm skill “gu”. Ba dự án mới không thay các skill thiết kế mà cho chúng điều kiện đạt/trượt khi sinh UI đa ngôn ngữ. **Chưa đo** bundle size, thời gian extract/compile, độ chính xác dịch AI hoặc hỗ trợ trên một thiết bị cụ thể; các thuộc tính đó cần báo cáo của dự án tích hợp.

**Nguồn §7u:** [i18next plural resolver](https://github.com/i18next/i18next/blob/b84e4180d71d271b9ae1f19ebb668224069b435e/src/PluralResolver.js), [defaults](https://github.com/i18next/i18next/blob/b84e4180d71d271b9ae1f19ebb668224069b435e/src/defaults.js), [CI](https://github.com/i18next/i18next/blob/b84e4180d71d271b9ae1f19ebb668224069b435e/.github/workflows/CI.yml), [Lingui compileLocale](https://github.com/lingui/js-lingui/blob/cbf16e9825cea76408ce06da02980ba57c8ea6c0/packages/cli/src/api/compile/compileLocale.ts), [config/pseudoLocale](https://github.com/lingui/js-lingui/blob/cbf16e9825cea76408ce06da02980ba57c8ea6c0/packages/conf/src/types.ts), [CI](https://github.com/lingui/js-lingui/blob/cbf16e9825cea76408ce06da02980ba57c8ea6c0/.github/workflows/main-suite.yml), [Weblate workflows](https://github.com/WeblateOrg/weblate/blob/9106f6a31fdeae6fc9e57a3bc1ffc3979824213d/docs/workflows.rst), [placeholder checks](https://github.com/WeblateOrg/weblate/blob/9106f6a31fdeae6fc9e57a3bc1ffc3979824213d/weblate/checks/placeholders.py), [license](https://github.com/WeblateOrg/weblate/blob/9106f6a31fdeae6fc9e57a3bc1ffc3979824213d/README.rst), [ECMA-402](https://tc39.es/ecma402/), [CLDR number/plural rules](https://www.unicode.org/reports/tr35/tr35-79/tr35-numbers.html), [Lingui pseudolocalization](https://lingui.dev/guides/pseudolocalization). Nguồn web chính thức đọc ngày 2/11/2026; permalink code ghim SHA.

## 7v. Năm trang cảm hứng thiết kế: posts.design, Saaspo, Transitions.dev, Icon Museum, Font in Logo (danh sách người dùng gửi, 2/11/2026)

> Người dùng gửi danh sách 5 link kèm mô tả một dòng (dạng bài tổng hợp "công cụ thiết kế"). Đây là **trang web/dịch vụ**, không phải repo; chỉ `transitions.dev` có mã trên GitHub và đã có hồ sơ ở §7p.5. Kho đọc trang chủ, `llms.txt`, trang FAQ/about (WebFetch 2/11/2026) và nguồn gom (Product Hunt, Awwwards, microsaasexamples); hai trang chặn fetch tự động (403) nên dữ kiện lấy từ nguồn gom, ghi **(chưa xác minh)**.

| Trang | Là gì (đọc 2/11/2026) | Ai làm · giá | Dùng được cho agent? | Quyền và điều kiện |
|---|---|---|---|---|
| **posts.design** | Gallery bài đăng mạng xã hội thật của brand/designer (launch, carousel, OG image, X header), mỗi mục link về bản gốc; "Public preview: 48 of 2218 references"; trang launch ghi số view "500,000+ recorded views" là quan sát có ngày, không phải số live | Không ghi tên người vận hành (liên hệ legal@posts.design) · free 100 credit/tháng, Pro 1.000 credit | **Có, hiếm trong nhóm này:** `llms.txt`, trang `.md` cho mọi path, `GET /api/post-search?q=`, `GET /api/gallery/v2`, **MCP `https://posts.design/mcp`** (Streamable HTTP + OAuth) với tool `search_references`, `get_reference`, `get_video_breakdown`, `get_scene_frames`, Pro: `get_scene_clip`, `list_playbooks`; 1 credit = 1 request | Chỉ để **học timing/cấu trúc/kỹ thuật**, cite nguồn, không tái sử dụng footage/logo/asset; takedown trả lời "within two business days" |
| **Saaspo** (saaspo.com) | Gallery landing page và màn hình SaaS, lọc theo section (pricing table, hero…), cộng đồng gửi, newsletter tuần | Product Hunt: ra 29/11/2023, "free forever" (chưa xác minh, trang chặn fetch); nhiều link vào có `?via=` (affiliate của bên giới thiệu) | Không có API/llms.txt công bố | Ảnh chụp là tài sản của các công ty SaaS; chỉ tham khảo bố cục, không chép asset |
| **Transitions.dev** | Thư viện transition CSS/React "43+ crafted transitions", builder và "agent" motion; mã trên `Jakubantalik/transitions.dev` (hồ sơ §7p.5: 35 file transition lúc đọc 31/10, license riêng cấm phân phối lại thư viện, `refine --llm` chạy `curl cursor.com/install \| bash`, bản Pro gửi mã lên `api.transitions.dev`) | Jakub Antalik · Pro trả phí, một số transition "Pro only" | Có skill/agent nhưng **trả phí và gửi mã ra ngoài** (§7p.5) | Dùng và sửa tự do, **không phân phối lại thư viện**; đọc LICENSE trước khi đóng gói vào template |
| **Icon Museum** (icon.museum) | Gallery app icon iOS tuyển chọn, tìm kiếm, email tuần; nguồn gom ghi "131 iOS icons, macOS coming soon" **(chưa xác minh, trang chỉ trả về title)** | Awwwards ghi tác giả Christo Todorov (chưa xác minh) · chưa thấy giá | Không | Icon là nhãn hiệu của từng app; tham khảo phong cách, không dùng lại |
| **Font in Logo** (fontinlogo.com) | Tra font trong logo nổi tiếng; nhãn trạng thái từng mục: **Verified** (đã đối chiếu nguồn), **The Closest Font** (gần nhất, không phải chính xác), **Based On / Modified**, **Community Suggestion** (chưa xác minh) → mô tả "tìm chính xác font" chỉ đúng với mục Verified | "Made by azwedo.com" (studio template Webflow), "30,000+ active users" tự nhận · "Join for free", có trang Pro | Không có API | Nhiều mục "Promoted" dẫn tới template Webflow của chính Azwedo; link ngoài gắn `ref=fontinlogo`; không ghi chữ "affiliate" |

**Nhận xét:** (1) Trong 5 trang chỉ posts.design được thiết kế cho agent (llms.txt + MCP + API có hạn mức): mẫu "gallery tham khảo có hợp đồng dùng" đáng ghi cho mục 04 (llms.txt) và cho skill thiết kế ở §7j/§7l khi cần tham chiếu thật thay vì trí nhớ model. (2) Mô tả trong danh sách người dùng gửi đúng về chức năng nhưng thổi nhẹ ở hai chỗ: "tìm chính xác font" (chỉ mục Verified), "thư viện hiệu ứng" (có phần trả phí và license cấm phân phối lại). (3) Mọi trang đều là bộ sưu tập tài sản của bên thứ ba: dùng để **học**, không để chép; posts.design nói rõ nhất điều này.

**Nguồn §7v:** WebFetch 2/11/2026: https://posts.design/ · https://posts.design/llms.txt · https://transitions.dev/ · https://fontinlogo.com/ · https://icon.museum/ (chỉ title) · https://saaspo.com và https://www.saaspo.com (403) · WebSearch 2/11/2026: producthunt.com/products/saaspo · awwwards.com/sites/icon-museum · microsaasexamples.com/p/icon-museum · toolfolio.com/tools/icon-museum · hồ sơ `Jakubantalik/transitions.dev` ở §7p.5 (clone 31/10/2026)

## 7w. Kiểm link motionsites.ai: thư viện prompt trả phí, skill Claude miễn phí làm mồi, và các bản dump bị DMCA (link người dùng gửi, 3/11/2026)

> Người dùng gửi link trang chủ. motionsites.ai **không phải repo**: là thư viện prompt trả phí cho Lovable/Bolt/v0/Cursor/Claude. Kho đọc trang chủ, `llms.txt`, `/unlimited`, `/mcp`, `/terms` (WebFetch 3/11/2026), clone repo chính thức `Motionsites-AI/claude-skill`, hai thông báo DMCA trong `github/dmca`, và một review ngoài (stork.ai). Đặt cạnh Hallmark (§7l), Taste Skill (§7j), Stageshow (§7s) và impeccable (mục 20 §3n) vì cùng là "skill để AI làm web đẹp".

### 7w.1 Hồ sơ nhanh

| Mục | Thông tin (3/11/2026) |
|---|---|
| Sản phẩm | "Official Premium AI Website Prompts": prompt hero/landing page, animated background, section, "40+ Lovable Templates", MCP; `llms.txt` chỉ liệt kê trang (Sections, Backgrounds, Gradients, Templates, Pricing, Affiliates), **không có API hay quyền dùng** |
| Ai làm | Footer và Terms (cập nhật 30/9/2026): "Operated by **Viktor Odainyi, sole trader**"; một người, không công ty; có chương trình affiliate |
| Giá (`/unlimited`) | 3 tháng 129 USD (giới hạn "3 prompt copies / Day"), năm 279 USD, trọn đời 399 USD (gạch 759 USD, có đồng hồ đếm ngược), gói lẻ 49 USD cho 2–10 prompt; MCP có trong mọi gói trả phí; tài khoản free mở 3 prompt. Review stork.ai ghi bảng giá khác ($149/năm, $239 trọn đời) đo 1/11/2026 → **giá đổi theo thời điểm**, ghi ngày khi dẫn |
| Quy mô | Trang chủ hiện 36 preview; MCP page ghi "500+ premium prompts"; stork.ai đếm 7/2026 "364 prompts, 159 video background, 40 Lovable templates" và dẫn "1500+" ở một chỗ khác → **không có con số nhất quán** (chưa xác minh) |
| MCP | Endpoint **`https://xgdzyqfalbibzelpdpvr.supabase.co/functions/v1/mcp`** (Supabase Edge Function), `claude mcp add motionsites --scope user --transport http …`, đăng nhập trình duyệt thay API key; trang không ghi tool nào được expose hay dữ liệu gửi đi |
| Terms | Được chép prompt/code vào dự án, sửa, **bán site đã dựng** ("Websites and apps you build with our prompts are yours"); **cấm** bán lại/phân phối lại prompt hoặc code, đăng lại thư viện, chia sẻ tài khoản, cào hay vượt paywall; refund ở trang riêng (review ngoài: "generally non-refundable once delivered") |

### 7w.2 Repo chính thức `Motionsites-AI/claude-skill` (clone 3/11/2026)

| Mục | Thông tin |
|---|---|
| Repo | **1.545★** sau 8 ngày (tạo 26/10/2026, 2 commit cùng ngày, HEAD `faa30d512e3973e58675c72101a7ef42ed37ae83`, author "MotionSites <noreply@motionsites.ai>"); GitHub gắn nhãn **NOASSERTION** |
| License thật | `LICENSE` **hai phần**: (1) SKILL.md, `references/`, `scripts/` theo **MIT** © 2026 MotionSites; (2) `examples/` (40 prompt) và `media/` + video/ảnh được link là **© MotionSites**, được dùng để dựng site kể cả cho khách, **không được bán lại/phân phối lại như một bộ sưu tập** → nhãn NOASSERTION là đúng, phải đọc file |
| Nội dung | Plugin marketplace `motionsites-web-builder` v1.0.0: `SKILL.md` 117 dòng (quy trình 5 bước: đọc brief → đọc 2–3 example gần nhất trong `examples/INDEX.md` → chọn media bằng mắt từ 6 contact sheet → viết spec theo `references/spec-template.md` → code hoặc "prompt mode" cho Lovable/Bolt/v0/Cursor/Manus/AI Studio/Kimi); `references/techniques/` 8 file **4.332 dòng** recipe (scroll, 3D/WebGL, type motion, video…); `references/review.md`: chấm 1–10 từng tiêu chí, **đạt khi trung bình ≥ 8 và không mục nào < 7**, vòng "sửa 3 điểm yếu nhất bằng số, không bằng tính từ" |
| Cổng máy | `scripts/shoot.py` (111 dòng): Playwright chụp desktop/mobile/early-paint và in QA (console error, request hỏng, overflow mobile, font, video) — **chỉ chạy local**, không upload (đọc import: json/os/subprocess/playwright) |
| Media | 139 URL trên `d8j0ntlcm91z4.cloudfront.net`, 42 `images.higgs.ai`, 14 Cloudinary, nhiều `*.figma.site`: **phụ thuộc host của bên thứ ba**, prompt hỏng khi host đổi; MEDIA.md tự ghi "free sample" |
| Phễu | 152 link về motionsites.ai có `utm_source=claude-skill`/`github`; SKILL.md dòng 73 và 79: "This skill is free because it's sponsored by MotionSites", "Want more like this? … 500+ premium prompts … MCP"; `plugin.json` homepage có utm. Skill là **mồi có khai báo**, không ẩn |

### 7w.3 Các bản dump và DMCA

- GitHub có ít nhất **8 repo không chính thức** mang tên motionsites (search API 3/11/2026): `xianxian-sensen/motionsites-prompts` (136★, **Unlicense**, mô tả "trích xuất đầy đủ 328 prompt"), `xiiiabu/motionsites.ai` (114★ MIT), `TheSatyam-Singh/motionsites.ai` (64★ MIT, "65 prompt"), `zhaosenlin12-creator/MotionSites` (56★), `giglianepefrei/motionsites.ai-prompt-library` (39★), `Melectrona/motionsites-prompts` (13★, "177 prompt"), v.v. Các repo này gắn MIT/Unlicense lên nội dung **không phải của họ**.
- Kho `github/dmca` có thông báo gỡ của chủ motionsites.ai ngày **26/5/2026** (`aayushsoam/motionsites.ai`, fork `nomaan5541/…prompt-library`), **9/9/2026** (`nomaan5541/motionsites-prompt-collection`) và hai thông báo "ai-web-design-prompts" 15/6 và 14/7/2026. Người gửi tự nhận là chủ bản quyền "paid collection of AI web design prompts", nêu cả claim vượt kiểm soát truy cập (GitHub ghi "không đủ thông tin cho claim anti-circumvention, nhưng có claim bản quyền hợp lệ").
- Hệ quả cho người dùng kho: dump "miễn phí" là nội dung có chủ và đã bị gỡ nhiều lần; dùng trong sản phẩm là rủi ro pháp lý và rủi ro bị xoá nguồn. Bản hợp lệ miễn phí là **40 prompt trong repo chính thức** với điều kiện ở §7w.2.

### 7w.4 So với cùng nhóm và kết luận

| Skill | ★ (3/11) | License | Cơ chế chính | Phễu |
|---|---|---|---|---|
| **MotionSites Web Builder** | 1.545 | MIT (skill) + © (40 example, media) | Example gần nhất + media thật + spec + screenshot QA + rubric ≥ 8 | Trả phí 500+ prompt, MCP trên Supabase |
| `Leonxlnx/taste-skill` (§7j) | 108.986 | MIT | Inspector chạy trên trình duyệt, thư viện hướng từ 247 site | Không |
| `pbakaus/impeccable` (mục 20 §3n) | 100.786 | Apache-2.0 | Engine Rust 59 luật tất định ở hook | Không |
| `Nutlope/hallmark` (§7l) | 46.248 | MIT | 48 template chống "AI slop", Together AI | Together AI |
| `benjitaylor/skills` Stageshow (§7s) | 622 | MIT (asset riêng) | Kit React Stage/Window/Phone cho faux UI | Không |

- **Điểm hơn:** media thật thay vì "fake image boxes", spec trước khi code, QA bằng ảnh chụp với ngưỡng số; cách viết example có số liệu (font, hex, clamp, easing) là mẫu tốt cho prompt thiết kế.
- **Điểm kém/rủi ro:** giá trị nằm ở prompt và media có chủ; kho ảnh/video trên host bên thứ ba; con số "500+/1500+/364" không khớp; vận hành bởi một người; MCP là hàm Supabase không công bố tool hay dữ liệu gửi; đồng hồ đếm ngược trên trang giá là mẫu bán hàng gây áp lực.
- **Dùng thế nào:** cài skill chính thức khi cần landing page "cinematic" nhanh và chấp nhận media mẫu; giữ 40 example trong dự án, không gom lại phân phối; nếu cần luật tất định thì ghép impeccable/taste-skill; **không** kéo dump từ repo lạ.

**Nguồn §7w:** WebFetch 3/11/2026: https://motionsites.ai · https://motionsites.ai/llms.txt · https://motionsites.ai/unlimited · https://motionsites.ai/mcp · https://motionsites.ai/terms · https://www.stork.ai/en/motionsites-ai · clone `--filter=blob:none` `Motionsites-AI/claude-skill` 3/11/2026 (HEAD `faa30d5`; LICENSE, README.md, `.claude-plugin/`, `SKILL.md`, `examples/INDEX.md`, `media/MEDIA.md`, `references/{review.md,spec-template.md,techniques/*}`, `scripts/shoot.py`; grep host) · GitHub search API 3/11/2026 (`motionsites`, `user:Motionsites-AI`, `repo:` cho 6 repo so sánh; code search `"motionsites.ai"`) · raw.githubusercontent.com/github/dmca/master/2026/05/2026-05-26-motionsites.md · …/2026/09/2026-09-09-motionsites.md · WebSearch 3/11/2026 (x.com/AiMotionSiteS, moge.ai, chatgate.ai, motionsites.org là domain khác chưa rõ liên hệ)

## 7x. Kiểm link mebius.design: chợ UI kit Figma của Keitoto, nhãn “React & Tailwind · MCP Ready” chưa có nội dung đi kèm (link người dùng gửi, 3/11/2026)

> Người dùng gửi https://www.mebius.design. Đã đọc trang chủ, `/license`, `/docs` và một trang sản phẩm (`/resources/aivonic`) bằng WebFetch, cùng mã HTML trang chủ bằng curl. Không tạo tài khoản, không mua, không tải file.

| Thuộc tính | Giá trị (3/11/2026) |
|---|---|
| Là gì | Chợ UI kit: 33 bộ (11 dashboard, 14 mobile app, 8 website), tiêu đề "React & UI Libraries for AI Agents". Mỗi thẻ kit ghi "Figma ready · React & Tailwind · MCP Ready"; nhiều kit hướng sản phẩm AI (AI chat app, AI receptionist) |
| Ai làm | Footer ghi "created by Keitoto" (Keitoto Studio, có cửa hàng trên Gumroad và hồ sơ Contra hướng tới "Web3 and AI SaaS"). Trang không ghi người sáng lập hay địa chỉ. Liên kết mạng xã hội và "Keitoto on UI8" đều là `#` (chưa trỏ đi đâu) |
| Giá | $19 mỗi kit hoặc $259 trọn bộ, trả một lần, được cập nhật miễn phí. Thanh toán qua Polar |
| License | Riêng của Mebius, không phải mã nguồn mở. Được dùng cho dự án cá nhân, thương mại và SaaS có thu phí. **Cấm** bán lại hay chia sẻ file (kể cả bản đã sửa), cấm biến thành UI kit, template, thư viện hay design system, cấm công bố để người dùng cuối trích component, cấm làm app builder hay sản phẩm thiết kế cạnh tranh. Mỗi license cho **một người**; nhóm phải hỏi license tổ chức. **Không nhắc gì tới việc dùng với công cụ AI hay huấn luyện AI**, cũng không nói tới dự án mã nguồn mở |

**Kiểm nhãn trên thẻ kit**

| Nhãn | Kết quả | Căn cứ |
|---|---|---|
| "Figma ready" | ✅ | `/docs` mô tả mỗi lần mua là một file `.zip` trong "My Library", giải nén ra file `.fig`; có hướng dẫn font, variables, auto layout, smart object PSD. Kit Aivonic: `Aivonic.fig` 75,5 MB, 108 màn hình, 33 component, v1.0, cập nhật 28/10/2026 |
| "React & Tailwind" | ⚠️ chưa thấy | Docs không có trang nào về React hay Tailwind, không có gói npm, repo hay registry shadcn. Trang Aivonic chỉ liệt kê file Figma. Có thể ý là "thiết kế theo lối dễ dựng bằng React/Tailwind", nhưng trang không nói rõ **(chưa xác minh khi chưa mua)** |
| "MCP Ready" | ⚠️ không định nghĩa | Không có MCP server, endpoint hay lệnh cài. Trang sản phẩm có một mục điều hướng "Installation & MCP" nhưng không có nội dung đọc được. Nhiều khả năng là file Figma được dựng gọn gàng để đọc qua MCP của Figma (Dev Mode), là tính năng của Figma chứ không phải của Mebius **(suy luận)** |

**Đặt trong bối cảnh**

- Cùng nhóm với các nguồn UI có trả phí mà mục 06 đã đọc (motionsites.ai §7w, Saaspo §7v). Khác biệt so với thư viện mã nguồn mở như shadcn/ui hay HyperUI (§7h) là ở đây bạn mua **file thiết kế**, chưa phải mã.
- ⚠️ Khi đưa kit cho agent dựng giao diện: license cấm "publish" hay để người khác trích component, và không nói gì về AI. Gửi file hoặc ảnh chụp cho dịch vụ AI bên thứ ba là vùng xám; nên hỏi Mebius trước nếu dùng cho sản phẩm thương mại. Không commit file `.fig` hay mã xuất từ kit vào repo công khai.
- Nếu cần thứ thật sự "sẵn cho agent": chọn thư viện có registry máy đọc được (shadcn/ui có registry và MCP server chính thức, §7f, §7h) hoặc kit có kèm mã nguồn và license rõ ràng.

**Nguồn §7x:** https://www.mebius.design · https://www.mebius.design/license · https://www.mebius.design/docs · https://www.mebius.design/resources/aivonic (WebFetch 3/11/2026) · curl trang chủ (grep `MCP`, `/resources/`) · https://keitoto.gumroad.com · https://contra.com/keitotostudio.

## 7y. Nâng trần 4/11/2026: component là hợp đồng có kiểm thử của xưởng phần mềm

<a id="ui-factory-2026-11-04"></a>

**Phạm vi đọc:** mã nguồn, LICENSE và cấu hình CI ghim bên dưới; không cài/chạy Storybook, trình duyệt hay test upstream. Các cổng tích hợp là thiết kế đề xuất cho repo sản phẩm. Số sao không thu thập trong đợt này.

### 7y.1 Khoảng trống sau token, a11y và quốc tế hóa

§7t–§7u đã có thước đo màu, token, ảnh và bản dịch. Để dùng chung trong nhiều dự án, xưởng còn cần một **hợp đồng component**: trạng thái, tương tác, quyền và lỗi đều có ví dụ chạy được. Một ảnh đẹp không chứng minh modal giữ focus, form xử lý lỗi server, hay nút đang tải không gửi đơn hai lần. Story phải phủ loading/empty/error/disabled/permission-denied cùng trạng thái thành công; dùng dữ liệu giả đã khử thông tin khách hàng.

| Lựa chọn | Khi nên chọn | Bằng chứng cần giữ | Giới hạn |
|---|---|---|---|
| Storybook + **@storybook/addon-vitest** | Component của dự án Vite, muốn dùng story làm ca kiểm thử trình duyệt | Danh sách story/test đã chạy, assertion trong play, báo cáo a11y và coverage | Cần tương thích Storybook/Vite/Vitest/browser provider; không thay E2E xuyên backend |
| Playwright ở mục 11 và mục 30 | Luồng route/auth/API của ứng dụng đã ghép | Trace, screenshot/video khi lỗi, assertion nghiệp vụ | Chậm hơn test component; phải kiểm soát đồng hồ, font, mạng và dữ liệu |
| axe-core + jsx-a11y (§7t) | Cổng accessibility động và tĩnh | Violation, incomplete và phần kiểm thủ công | Không tự chứng nhận toàn bộ WCAG hay chất lượng trải nghiệm |
| Argos/pixelmatch (§7t) | Phát hiện thay đổi hình ảnh có người duyệt | Baseline được duyệt theo commit, diff, viewport/locale | Không chấm ý nghĩa nút hoặc đúng/sai nghiệp vụ; không tự cập nhật baseline trong lượt sửa lỗi |

### 7y.2 Đọc mã: addon mới và đường chuyển từ runner cũ

<a id="storybook-addon-vitest-factory"></a>

**Storybook Vitest addon** là thực thể kiểm thử trong cùng upstream storybookjs/storybook, khác hồ sơ thư viện component Storybook ở §1. Đọc nhánh next tại **e4ec60736988a349e8a5d4484ea5a832fde49af8** ngày 2026-11-04: package đang ghi **11.0.0-beta.0**, license MIT. Đây là snapshot phát triển, **không phải khuyến nghị cài beta vào sản phẩm**; khi tích hợp phải chọn bộ phiên bản stable tương thích và kiểm lại migration guide.

Plugin biến story thành test qua vitestTransform, nạp setup-file và project annotations. Đường a11y ở preview phân biệt chế độ **todo** (warning), **error** (failed) và **off**; giá trị khai báo mặc định của addon-a11y là **todo**. Trong lượt Vitest standalone, chỉ khi có violation và mode failed thì matcher làm test thất bại. Vì vậy có addon hoặc có bảng cảnh báo chưa đủ làm cổng phát hành: cấu hình a11y.test thành error cho phạm vi cần chặn, thử một fixture có lỗi để chứng minh pipeline thực sự từ chối. Giữ incomplete cho review riêng.

**Phát hiện cần chuyển đổi:** storybookjs/test-runner tại **5364e386006e31f436813af9205138cfe320be04** ghi rõ **đã kết thúc hỗ trợ chính thức**. MIGRATION.md của Storybook nói package vẫn được phát hành nhưng không tiếp tục nhận fixes/compatibility updates. Mã runner cũ có preVisit/postVisit, coverage instrumentation và telemetry có cờ tắt; đây là thông tin bảo trì cho hệ đang dùng, không thêm runner cũ như lựa chọn mặc định cho dự án mới. Dự án Vite chuyển sang addon-vitest; hệ không tương thích cần thử Playwright/portable stories và xác minh coverage tương đương trước khi bỏ runner cũ.

### 7y.3 Pipeline giao diện cho nhiều sản phẩm

1. **Thiết kế hợp đồng trước:** token DTCG, semantic HTML, API props/events, trạng thái và ma trận quyền/locale; story gắn ID yêu cầu và link về thiết kế đã duyệt.
2. **PR component:** typecheck/lint → test interaction và a11y mode error → so ảnh trên viewport/locale đã chọn. Phải ghi tổng số story hợp lệ/đã chạy/skipped; bộ lọc rỗng không được xem là pass.
3. **Ghép ứng dụng:** E2E cho thao tác quan trọng như đăng nhập, lưu form, thanh toán; có test từ chối quyền phía server. Không suy quyền truy cập backend từ việc ẩn nút UI.
4. **Phát hành design system:** version component/token, changelog breaking changes và kiểm ứng dụng tiêu thụ đại diện trước nâng phiên bản; thêm bài di trú khi đổi props hoặc token.
5. **Nghiệm thu:** người dùng thực hiện tác vụ, kiểm keyboard/screen reader và nội dung tiếng Việt; giữ bằng chứng này cạnh báo cáo máy. Ngưỡng tự động do sản phẩm quy định, không dùng một điểm UI tổng hợp cho mọi tác vụ.

**Nguồn §7y:** [LICENSE](https://github.com/storybookjs/storybook/blob/e4ec60736988a349e8a5d4484ea5a832fde49af8/LICENSE) · [MIGRATION.md](https://github.com/storybookjs/storybook/blob/e4ec60736988a349e8a5d4484ea5a832fde49af8/MIGRATION.md) · [code/addons/vitest/package.json](https://github.com/storybookjs/storybook/blob/e4ec60736988a349e8a5d4484ea5a832fde49af8/code/addons/vitest/package.json) · [code/addons/vitest/src/vitest-plugin/index.ts](https://github.com/storybookjs/storybook/blob/e4ec60736988a349e8a5d4484ea5a832fde49af8/code/addons/vitest/src/vitest-plugin/index.ts) · [code/addons/vitest/src/vitest-plugin/setup-file.ts](https://github.com/storybookjs/storybook/blob/e4ec60736988a349e8a5d4484ea5a832fde49af8/code/addons/vitest/src/vitest-plugin/setup-file.ts) · [code/addons/a11y/src/preview.tsx](https://github.com/storybookjs/storybook/blob/e4ec60736988a349e8a5d4484ea5a832fde49af8/code/addons/a11y/src/preview.tsx) · [.circleci/config.yml](https://github.com/storybookjs/storybook/blob/e4ec60736988a349e8a5d4484ea5a832fde49af8/.circleci/config.yml) · [README.md](https://github.com/storybookjs/test-runner/blob/5364e386006e31f436813af9205138cfe320be04/README.md) · [LICENSE](https://github.com/storybookjs/test-runner/blob/5364e386006e31f436813af9205138cfe320be04/LICENSE) · [src/playwright/transformPlaywright.ts](https://github.com/storybookjs/test-runner/blob/5364e386006e31f436813af9205138cfe320be04/src/playwright/transformPlaywright.ts) · [src/test-storybook.ts](https://github.com/storybookjs/test-runner/blob/5364e386006e31f436813af9205138cfe320be04/src/test-storybook.ts) · [.github/workflows/tests.yml](https://github.com/storybookjs/test-runner/blob/5364e386006e31f436813af9205138cfe320be04/.github/workflows/tests.yml)

## 7z. Kiểm ảnh ba thẻ skill: Emil Kowalski (animation), App Store Screenshots (ra mắt app), gstack (review thiết kế) (ảnh người dùng gửi, đọc mã 7/11/2026)

> Ảnh gồm ba thẻ "SKILL 03/05 Animation – Emil Kowalski ★52.1K (github.com/emilkowalski/skill)", "SKILL 04/05 Ra mắt app – App Store Design ★7.7K (github.com/ParthJadhav/app-store-screenshots)", "SKILL 05/05 Review thiết kế – gstack ★138.3K (github.com/garrytan/gstack)". Đường dẫn đúng của thẻ đầu là `emilkowalski/skills` (có chữ s). Hồ sơ gstack ở mục 20 §3za.

### 7z.1 `emilkowalski/skills` đọc lại (bổ sung §7m.1)

| Thuộc tính | Giá trị (7/11/2026) |
|---|---|
| Repo | https://github.com/emilkowalski/skills · **54.263★, 3.167 fork** (GitHub search API) · MIT · 60 commit |
| Cài | `npx skills@latest add emilkowalski/skills` |
| Thành phần | 17 skill: `emil-design-eng` (skill chính, chủ yếu animation), `animate`, `animate-expo` (React Native/Expo), `review-animations`, `improve-animations`, `find-animation-opportunities`, `remove-animations`, `choreograph`, `animation-performance`, `animation-vocabulary`, `apple-design`, `write-swift`, `pick-ui-library`, `prototype`, `mobile-native`, `break-ui`, `ask-sonner`; thêm `ui-cheatsheet.md` và `performance-cheatsheet.md` |

Điểm mạnh:

- **Kinh nghiệm thật của design engineer** (Vercel, Linear; tác giả Sonner và Vaul) được viết thành luật cụ thể, ví dụ animation xuất hiện dùng `ease-out` chứ không dùng `ease-in`.
- **Đủ vòng animation**: dựng mới (`animate`), tìm chỗ nên có (`find-animation-opportunities`), bỏ chỗ thừa (`remove-animations`), phối nhiều phần tử (`choreograph`), review nghiêm (`review-animations`), audit cả codebase thành kế hoạch tự chứa cho agent khác chạy (`improve-animations`), sửa rớt khung (`animation-performance`).
- **Mở rộng ngoài animation**: thử giao diện bằng dữ liệu xấu nhất (`break-ui`), web có cảm giác native trên điện thoại (`mobile-native`), chọn thư viện đáng tin thay vì để AI tự viết (`pick-ui-library`), làm nhiều phương án có thanh chuyển (`prototype`), nguyên tắc Apple cho web (`apple-design`).

### 7z.2 `ParthJadhav/app-store-screenshots`: skill dựng editor ảnh chụp App Store và Google Play

| Thuộc tính | Giá trị (7/11/2026) |
|---|---|
| Repo | https://github.com/ParthJadhav/app-store-screenshots · **7.834★, 557 fork** (GitHub search API), tạo 7/3/2026 · MIT · 90 commit (Parth Jadhav 71) |
| Cài | `npx skills add ParthJadhav/app-store-screenshots` (thêm `-g` để cài toàn cục, `-a claude-code` cho một agent), hoặc `git clone` vào `~/.claude/skills/app-store-screenshots`; dùng được với Claude Code, Cursor, Windsurf, OpenCode, Codex |
| Thành tích | README ghi 14,1K lượt cài trên skills.sh, Trendshift #10 Repository of the Day, Product Hunt #8; ảnh tạo bằng skill được App Store duyệt cho app Bloom Coffee Shelf Recipe |

Điểm mạnh:

- **Dựng cả một editor, không chỉ một trang tĩnh**: skill scaffold dự án Next.js + shadcn/ui có canvas nối liền (điện thoại, chữ, họa tiết vắt qua nhiều ảnh rồi cắt chính xác từng màn), sidebar màn hình kéo thả, inspector, chọn theme, Style Lab (bốn phong cách cạnh nhau, khóa màu/chữ/bố cục/cảnh), Scene Playground, kính lúp phóng chi tiết.
- **Xuất đúng mọi kích thước bắt buộc** của App Store, Mac App Store và Google Play bằng `html-to-image`, gói zip theo nền tảng, thiết bị, độ phân giải và ngôn ngữ; phủ iPhone, iPad, Apple TV, Apple Watch, CarPlay, Mac, điện thoại và tablet Android, feature graphic.
- **Ảnh là quảng cáo, không phải chụp UI**: 18 phong cách đặt tên có đặc tả riêng (`style-prompts/`) và thư viện tiêu đề (`copy-ideas.md`); hỗ trợ đa ngôn ngữ và bố cục RTL.
- **Lưu dự án theo git**: mọi deck nằm trong `app-store-screenshots.json`, autosave qua `/api/project` có phát hiện bản mới hơn trên đĩa trước khi ghi đè; dự án cũ được migrate tại chỗ, có chế độ isolated giữ nguyên cách xuất cũ.

Dùng: sau khi cài, yêu cầu agent "Build App Store and Google Play screenshots for my app." Skill sẽ hỏi bối cảnh app, ảnh nguồn, nền tảng, ngôn ngữ, phong cách và số slide rồi mới dựng editor. Ảnh nguồn iPhone dễ nhất là chụp từ simulator 6.1 inch.

**Nguồn §7z:** ảnh ba thẻ người dùng gửi 7/11/2026 · clone https://github.com/emilkowalski/skills HEAD `c8a79627b59d72d764d6ab6f2c87c09a48169833`: https://github.com/emilkowalski/skills/blob/c8a79627b59d72d764d6ab6f2c87c09a48169833/README.md · https://github.com/emilkowalski/skills/blob/c8a79627b59d72d764d6ab6f2c87c09a48169833/LICENSE · clone https://github.com/ParthJadhav/app-store-screenshots HEAD `3bdfb8d3dc794bae05f240b2cb9607cd23de40ec`: https://github.com/ParthJadhav/app-store-screenshots/blob/3bdfb8d3dc794bae05f240b2cb9607cd23de40ec/README.md · https://github.com/ParthJadhav/app-store-screenshots/blob/3bdfb8d3dc794bae05f240b2cb9607cd23de40ec/skills/app-store-screenshots/SKILL.md · https://github.com/ParthJadhav/app-store-screenshots/blob/3bdfb8d3dc794bae05f240b2cb9607cd23de40ec/LICENSE · GitHub search API 7/11/2026.

## 7za. Kiểm bài "8 kho UI sẵn dùng": Libraries.dev, Bencho, beUI, Arc UI, BoardUI, Kobra, affectUI, Watermelon UI (bài người dùng gửi, đọc mã 8/11/2026)

> Bài đăng chia 8 kho thành ba nhóm: hiệu ứng và micro-interaction (Libraries.dev, Bencho, beUI Pro), product UI cho dashboard và agent (Arc, BoardUI, Kobra), và component cho agent (affectUI), với Watermelon UI là catalog mở để bắt đầu. Cả 8 đều đưa source vào project và có đường cho coding agent đọc (MCP, `llms.txt`, registry hoặc skill). Sáu kho có repo công khai và đã được đọc mã; Arc UI và Kobra chỉ đọc qua trang chính thức.

### 7za.1 Bảng nhanh

| Kho | Repo hoặc trang | ★ / fork (8/11/2026) | Giấy phép | Thế mạnh | Đường cho agent |
|---|---|---|---|---|---|
| Libraries.dev | `Jakubantalik/Libraries.dev` · libraries.dev | 4.637 / 277 | MIT (thư viện); model `.mfxl` theo license riêng | 7 hiệu ứng React: border beam, thinking orbs, bot avatars, gooey, voice glow, liquid metal, image loader WebGL | Nút *Copy prompt* mỗi trang, skill `libraries-dev` |
| Bencho | `cabralorenzo/bencho` · bencho.dev | 91 / 5 | MIT (bản free); Pro license riêng | 47 block tương tác xếp theo cử chỉ (hover, drag, swipe, slide, press, type, select) + 24 âm thanh giao diện | MCP, *Copy prompt* mỗi block |
| beUI | `starc007/ui-components` · beui.dev | 1.934 / 94 | MIT (core); Pro qua registry riêng | Component motion, block, giao diện AI agent, chart | MCP `mcp.beui.dev`, skill `beui`, `llms.txt`, registry shadcn |
| Arc UI | uiarc.dev (chưa thấy repo công khai) | — | MIT (bản free) | 121 component + 22 block miễn phí cho settings, billing, analytics, sign-in | MCP `uiarc.dev/api/mcp`, `llms.txt`, trang Markdown mỗi item |
| BoardUI | `BoardUI/boardui` · boardui.com | 1.085 / 90 | MIT (bản free) | Design system cho dashboard và giao diện agent, React Aria + Tailwind v4, 400+ token, RTL | MCP qua `npx boardui mcp`, skill, `AGENTS.md`, `llms.txt` |
| Kobra | kobra.systems (chưa thấy repo công khai) | — | Bản free dùng cá nhân; Pro trả một lần | Component có motion riêng, dark mode tinh chỉnh tay, âm thanh tổng hợp, nhóm Generative UI và Agents | `/install.md` cho agent; MCP và skill trong bản Pro |
| affectUI | `flohoeller/affectui` · affectui.com | 523 / 30 | MIT (40 item free) | Component cho việc agent làm: tool call, decision inbox, handoff, approval, trace | MCP `affectui.com/api/mcp`, `llms.txt` |
| Watermelon UI | `WatermelonCorp/watermelon-platform` · ui.watermelon.sh | 184 / 10 | MIT | Catalog mở: animated component, block, dashboard, template | MCP (stdio và hosted), `llms.txt`, `openapi.json`, API catalog, skill `watermelon-ui` |

### 7za.2 Nhóm hiệu ứng và micro-interaction

- **Libraries.dev** (Jakub Antalik, 702 commit): mỗi thư viện là một package npm độc lập, không phụ thuộc runtime (riêng `img-fx` cần `three`), bọc quanh phần tử sẵn có nên giữ nguyên ngữ nghĩa HTML. Cần React 18+. `theme="auto"` tự đọc `data-theme`, class `dark` hoặc `prefers-color-scheme`. Cài: `npm install border-beam` (hoặc `thinking-orbs`, `bot-avatars`, `liquid-gooey`, `voice-glow`, `metal-fx`, `img-fx`) rồi `<BorderBeam><button>…</button></BorderBeam>`. Pro mở Studio để chỉnh sâu và xuất cấu hình.
- **Bencho** (Lorenzo Cabra): mỗi block là một thư mục gồm component, stylesheet và README liệt kê props; props trùng với nút chỉnh trên bencho.dev. `tokens.css` chứa màu sáng và tối. 24 âm thanh tạo bằng Web Audio API nằm gọn trong một file, không có file audio. Dùng: `cp -r blocks/like src/components/like` rồi `npm install framer-motion lucide-react`.
- **beUI** (841 commit, từ 1/2024): React, TypeScript, Tailwind CSS, Motion; component có hành vi bàn phím và reduced-motion, kèm bộ test accessibility (35 file trong `tests/`). Cài: `npx shadcn@latest add @beui/animated-toast-stack`; agent nối MCP `https://mcp.beui.dev/mcp` (không cần key) hoặc `npx skills add starc007/ui-components --skill beui`. Bản Pro thêm section động và template Next.js qua skill `beui-pro`.

### 7za.3 Nhóm product UI cho dashboard và agent

- **Arc UI** (uiarc.dev): component là TSX thuần với CSS modules và token chung cho màu, bo góc, chữ, chuyển động; mỗi trang component có mục bàn phím, screen reader và reduced-motion, bản xem trước chạy đúng source sẽ được cài. Cài: `npx shadcn@latest add https://uiarc.dev/r/arc-foundation.json`; Claude Code: `claude mcp add --transport http arc https://uiarc.dev/api/mcp`. Pro mở thêm 121 component và 118 block.
- **BoardUI**: repo chứa đủ 69 item miễn phí và một app mẫu (chat, dashboard có chart, đăng nhập) dựng từ chính các component đó. Route chat đọc API key phía server, nhận key của Anthropic, OpenAI, Gemini, OpenRouter, Groq, xAI, Vercel AI Gateway và server tương thích OpenAI. Hỗ trợ RTL qua `DirectionProvider`. Cài: `npx boardui@latest add data-table`; nối agent: `claude mcp add boardui -- npx -y boardui@latest mcp`, rồi nói "Install every free BoardUI component".
- **Kobra** (Harsh Singh): khoảng 89 mục chia nhóm Free, Generative UI, Agents (Conversation, Composer, Message, Reasoning Steps, Task List…), Content, Feedback, Form controls, Layout, Navigation, Overlays; React + Tailwind, nhiều mục dựa trên Base UI và Motion. Bản free có 11 component, Figma kit, theme sáng/tối và âm thanh giao diện. Cài: `npx shadcn@latest add @kobra/tabs`.

### 7za.4 Component cho agent và catalog mở

- **affectUI** (`flohoeller`): component cho từng việc agent làm (Tool Call Card, Decision Inbox, Change Summary, Thinking Loader, Progress Tracker) và cho phần còn lại của app; mỗi item có hai kiểu `clean` và classic, motion tôn trọng `prefers-reduced-motion`, React 19. Cài: `npx shadcn@latest add @affectui/reaction-bar` hoặc copy file từ `components/`; MCP: `claude mcp add --transport http affectui https://www.affectui.com/api/mcp`. Agent Tree và Trace Waterfall thuộc Pro.
- **Watermelon UI** (942 commit): mã của cả nền tảng ui.watermelon.sh đều mở (React 19, Vite, Tailwind 4, Motion); nội dung lưu dạng file MDX trong `src/data/contents`. Có MCP server cả stdio (`bun run mcp`) lẫn bản hosted trên Cloudflare, sinh registry shadcn bằng `bun run generate:shadcn-registry`, endpoint `/llms.txt`, `/openapi.json`, `/api/catalog/entries?kind=blocks`; kèm skill `watermelon-ui` và `make-interfaces-feel-better`.

### 7za.5 Chọn theo việc đang thiếu

- Giao diện đã có cấu trúc, thiếu cảm giác sống: Libraries.dev (hiệu ứng AI), Bencho (cử chỉ và âm thanh), beUI (component có motion).
- Dashboard, settings, form: Arc UI, BoardUI.
- Sản phẩm có agent: affectUI (tool call, approval, inbox), BoardUI và Kobra (chat, reasoning), beUI (approval, tool result).
- Bắt đầu miễn phí với catalog mở: Watermelon UI.
- Cách thử: nối MCP hoặc dán *Copy prompt* vào agent, cài một item miễn phí vào codebase rồi mới cân nhắc bản Pro. Liên quan: §7f (design system AI-ready), §7y (component là hợp đồng có kiểm thử), mục 22 (animation).

**Nguồn §7za:** bài đăng người dùng gửi 8/11/2026 · clone `--filter=blob:none`: https://github.com/Jakubantalik/Libraries.dev/blob/9a42e88847dab0ac145733f15cf90535e9cb59ab/README.md · https://github.com/Jakubantalik/Libraries.dev/blob/9a42e88847dab0ac145733f15cf90535e9cb59ab/LICENSE-MODEL.md · https://github.com/cabralorenzo/bencho/blob/c65992417427bb09e661674ffa800bef29adef49/README.md · https://github.com/cabralorenzo/bencho/blob/c65992417427bb09e661674ffa800bef29adef49/LICENSE · https://github.com/starc007/ui-components/blob/7664db5374761439e6582d534311a17aed34d29d/README.md · https://github.com/BoardUI/boardui/blob/ec5c5eb3e29c2441be63b9422cd54f411ef23466/README.md · https://github.com/flohoeller/affectui/blob/7ac87beb0ffaef2dd0305e508b4e3d471f269d84/README.md · https://github.com/WatermelonCorp/watermelon-platform/blob/2a2aeef7533d7df52be294e73628a216238d1b90/README.md · https://uiarc.dev/docs/introduction · https://kobra.systems · https://kobra.systems/pricing · GitHub search API 8/11/2026.

## 7zb. Đọc lại heydamir/unslop: skill biến UI "vibecoded" thành giao diện có chủ đích, 11,4k★ sau 10 ngày (ảnh người dùng gửi, đọc mã 8/11/2026)

> Ảnh là một dòng "unslop: +4,000 ★ … trong 3 ngày". Bổ sung cho dòng `heydamir/unslop` ở §7p.

| Thuộc tính | Giá trị (8/11/2026) |
|---|---|
| Repo | https://github.com/heydamir/unslop · **11.436★, 629 fork** (GitHub search API) · tạo 29/10/2026 · CC BY 4.0 (dùng, sửa, chia sẻ kể cả thương mại khi ghi công tác giả và link về repo) |
| Tác giả | Damir Sokolovsky (@heydamir), người mở loạt "Unslopping" trên X; 12 commit, có đóng góp từ cộng đồng (Codex, snapshot ảnh responsive) |
| Đà tăng sao | Kho này ghi 3.397★ ngày 31/10 và 11.436★ ngày 8/11, tức hơn 8.000★ trong 8 ngày, trung bình khoảng 1.000★ mỗi ngày, khớp với con số +4.000★ trong 3 ngày của ảnh |
| Thành phần | `skills/unslop/SKILL.md` (233 dòng) và 5 file tham chiếu (`signs.md` dấu hiệu slop, `tokens.md`, `effects.md`, `visuals.md`, `refs.md` kèm ảnh mẫu); script `snapshot.mjs` và `story.mjs`; `agents/openai.yaml` cho Codex; hai màn "vibecoded" mẫu trong `examples/` |

Điểm mạnh:

- **Kiểm trước, sửa sau**: liệt kê từng dấu hiệu slop kèm vị trí (gradient tím, glow, nhãn emoji, chữ la hét, khoảng cách lệch), rồi đề xuất hướng trước khi sửa để người dùng lái sớm. Màn đã tốt thì chỉ gợi ý vài chỉnh nhỏ, không thiết kế lại.
- **Hướng đi lấy từ chính sản phẩm**: tính cách, "thế giới", một hai khoảnh khắc mang màu, và một chi tiết đặc trưng.
- **Chín lượt theo thứ tự**: spacing, màu, icon, copy, chữ, layout, chi tiết, hình ảnh, motion; cuối có phần "Do not" và checklist.
- **Hình ảnh thật của sản phẩm** thay cho khối blob bóng loáng; khi hero cần cảnh hoặc vật thể, có thể sinh ảnh qua fal, Replicate, OpenAI images hoặc Higgsfield.
- **Video câu chuyện**: video vuông dưới 10 giây cảnh màn hình tự "unslop", sẵn để đăng (Playwright + ffmpeg); `snapshot.mjs` chụp được trang đang chạy.
- **Chạy trên Claude Code và Codex**, có tên hiển thị và prompt mặc định cho Codex.

Cài và dùng:

```bash
git clone https://github.com/heydamir/unslop
mkdir -p ~/.claude/skills && cp -r unslop/skills/unslop ~/.claude/skills/
```

- Codex: `$skill-installer install https://github.com/heydamir/unslop/tree/main/skills/unslop`, hoặc copy vào `~/.agents/skills/`.
- Muốn chụp trang hoặc làm video: `npm install -D playwright` rồi `npx playwright install chromium`, cần ffmpeg trong PATH.
- Gọi `/unslop this dashboard`, `/unslop the hero of https://example.com` (Codex: `$unslop`). Thử trước trên hai màn mẫu trong `examples/`.
- Cùng nhóm: Taste Skill (§7j), Hallmark (§7l), antislop (§7i), Emil Kowalski (§7z.1).

**Nguồn §7zb:** ảnh người dùng gửi 8/11/2026 · clone https://github.com/heydamir/unslop HEAD `a6f121eee5f29c2f74976b75456feae8b66afb3a`: https://github.com/heydamir/unslop/blob/a6f121eee5f29c2f74976b75456feae8b66afb3a/README.md · https://github.com/heydamir/unslop/blob/a6f121eee5f29c2f74976b75456feae8b66afb3a/skills/unslop/SKILL.md · https://github.com/heydamir/unslop/blob/a6f121eee5f29c2f74976b75456feae8b66afb3a/LICENSE · GitHub search API 31/10 và 8/11/2026.

## 7zc. Hai mươi trang cảm hứng và tài nguyên thiết kế: gallery, từng phần giao diện, chuyển động, làm web bằng AI (danh sách người dùng gửi, đọc 16/11/2026)

> Người dùng gửi danh sách 20 trang chia bốn nhóm. Font In Logo và MotionSites đã có hồ sơ ở §7v và §7w; 18 trang còn lại được đọc trang chủ (và `llms.txt`, trang giá khi có) ngày 16/11/2026. Hai chỗ cần biết khi tra: **Godly (godly.website) nay chuyển hẳn về Recent Design** (recent.design), nên mục 02 và 05 là một trang; **Motion In Design** có địa chỉ `motionin.design`.

### 7zc.1 Cảm hứng tổng hợp

| # | Trang | Có gì | Giá | Cho agent |
|---|---|---|---|---|
| 01 | **Inspora** · inspora.design | Kho thiết kế mới tuyển chọn, lọc Web, Branding, Product, Motion, Illustration, 3D, Print; mục Websites và Logos riêng | Miễn phí | Xem tham khảo |
| 02, 05 | **Recent Design** · recent.design (trước là Godly) | "The best design inspiration on the Internet": Design, Launch Videos, Websites, OG Images, App Screenshots, App Icons, cùng Tools, Skills, Jobs; lọc Web, Interface, Branding, Motion, Illustration, Posters, Print | Miễn phí | Xem tham khảo |
| 03 | **Land-book** · land-book.com | Gallery website cập nhật hằng ngày, duyệt theo loại trang (landing, portfolio, ecommerce, blog), theo section (pricing, value proposition…), nền tảng và màu; thêm OG images, template Webflow/Framer | Miễn phí giới hạn, có gói Pro | `llms.txt` |
| 04 | **Landdding** · landdding.com (Azwedo) | Khoảng 2.700 thiết kế landing page, 40 nhóm, 5 nền tảng template (Webflow, Framer, WordPress, Wix, Squarespace); lọc màu, tag; feed ngày và tuần | Miễn phí; PRO $4/tháng hoặc $48/năm | `llms.txt` |
| 06 | **Motion In Design** · motionin.design | Section web tương tác cao cấp (hero, portfolio wall, product showcase, immersive) dựng bằng React, GSAP, Three.js; có vài section miễn phí | $9/tháng (3 section/tháng), lifetime $99 | Mỗi section là một prompt kèm file spec Markdown, nút *Copy Prompt* để dán vào công cụ AI coding; `llms.txt` |

### 7zc.2 Từng phần của giao diện

| # | Trang | Có gì | Giá | Cho agent |
|---|---|---|---|---|
| 07 | **Navbar Gallery** · navbar.gallery (Christina Liubynska) | Hơn 450 navbar từ site thật, theo loại (static, dropdown, mega menu, sidebar, search bar, announcement, full screen, breadcrumbs), theo style và ngành | Miễn phí | `llms.txt` |
| 08 | **Footer Design** · footer.design (NOOON Studio) | Gallery footer lọc Typographic, Illustrative, Grid, Animated, Cards, Dark, Large Type, Bold… | Miễn phí | `llms.txt` |
| 09 | **CTA Gallery** · cta.gallery | Mẫu CTA theo loại: button, call-to-buy, download, form, modal, newsletter, pricing; lọc theo ngành và chế độ sáng/tối | Miễn phí | Xem tham khảo |
| 10 | **Iconly** · iconly.ai | Nền tảng sinh icon và asset bằng AI (Icon Generator, Vector Studio, Brand Studio), thư viện công khai hơn 11.000 icon trong 10 style, trang riêng cho app và game; icon tạo ra dùng được cả thương mại | Pro $12,50/tháng, Max $25/tháng | REST API, MCP từ xa `https://iconly.ai/mcp`, agent skill |
| 11 | **Refero Styles** · styles.refero.design | Hơn 2.000 design system đọc được bằng AI lấy từ sản phẩm thật: màu, chữ, spacing, component, kèm file `DESIGN.md` cho Cursor, Claude Code, Codex, v0, Lovable | Theo gói Refero | `DESIGN.md`, Refero MCP, skill `referodesign/refero_skill` |

**Refero skill** (`referodesign/refero_skill`, MIT, 353★): một skill bắt agent nghiên cứu trước khi làm giao diện, cộng MCP chỉ đọc để tra style, hơn 150.000 màn hình app thật và hơn 6.000 user flow. Claude Code: `/plugin marketplace add referodesign/refero_skill` rồi `/plugin install refero@refero`; có bản cho Codex, Cursor, Gemini CLI. Tra cứu trực tiếp cần gói Refero trả phí.

### 7zc.3 Chuyển động và hiệu ứng

| # | Trang | Có gì | Giá | Cho agent |
|---|---|---|---|---|
| 12 | **60fps** · 60fps.design | Chi tiết animation và tương tác của app iOS và web: 2.140 shot, 499 app, storyboard, 32 snippet, 108 bộ lọc, glossary | Xem miễn phí; PRO $15/tháng hoặc $150/năm | MCP (gói riêng), snippet |
| 13 | **Scrolltide** · scrolltide.co | 149 template (hero, web 3D, landing), 107 component, 55 shader, 24 section; "copy one, paste it into your AI" để ra Next.js, React, Tailwind, Framer Motion, GSAP, Three.js | Lifetime $299, có template miễn phí; dùng cho cá nhân và khách hàng | Prompt cho Claude, Cursor, v0; MCP chỉ đọc cho Claude Code, Cursor, Codex, VS Code |
| 14 | **Scroll Shaders** · scrollshaders.com | 117 shader WebGL lặp liền mạch trong 11 nhóm (mesh gradient, grain, light & rays, halftone, 3D…), component shader (button, card, border, headline), 77 ảnh tĩnh 6K | $29/tháng, $129/năm, $239 trọn đời; giấy phép thương mại | Copy component React `.tsx` hoặc snippet HTML/JS WebGL2 không cần npm |
| 15 | **OriginKit** · originkit.dev (Vellum AI) | Component có animation miễn phí cho web: interactive, image gallery, text, background, button (Black Hole, Fluid Trail, Coverflow Carousel, Text Morph, Pixel Reveal…), cho React, Next.js, Vite, Framer với CSS, Tailwind hoặc CSS Modules | Miễn phí; lấy code cần API key miễn phí | MCP `https://mcp.originkit.dev/vellumai`; plugin `vellum-ai/originkit` (MIT) với tool browse, get, setup |

### 7zc.4 Làm web bằng AI và tài nguyên

| # | Trang | Có gì | Giá | Cho agent |
|---|---|---|---|---|
| 16 | **MotionSites** · motionsites.ai (hồ sơ §7w) | Thư viện prompt hero và landing page có motion | Gói trả phí | Prompt, MCP trong gói trả phí |
| 17 | **MotionSites Studio** · studio.motionsites.ai | AI website builder: mô tả doanh nghiệp, AI chỉnh một mẫu MotionSites, tạo ảnh và video rồi dựng site; mẫu Portfolio, Ecommerce, SaaS, Agency, Travel, Fashion, 3D | Theo trang | Dựng site bằng lời |
| 18 | **One Prompt Design** · onepromptdesign.com | Prompt AI và tham chiếu hình cho quảng cáo, bài mạng xã hội: posters, images, mockups, gradients, backdrops | Theo trang | Prompt để copy |
| 19 | **Backgrounds Supply** · backgrounds.supply (Kailash) | 1.983 hình nền trong 53 bộ: gradient, wallpaper, nền AI, 36 nền động MP4; ảnh 16:9 tới 4K; 14 công cụ miễn phí như Gradient Lab | $49 một lần, trọn đời; dùng thương mại | File ảnh, video |
| 20 | **Font In Logo** · fontinlogo.com (hồ sơ §7v) | Tra font của logo thương hiệu lớn, có nhãn mức chắc chắn từng mục | Miễn phí | Xem tham khảo |

### 7zc.5 Dùng thế nào

- **Tìm bố cục và cảm hứng chung:** Recent Design, Inspora, Land-book, Landdding; khi cần đúng một phần thì vào Navbar Gallery, Footer Design, CTA Gallery.
- **Đưa thẳng cho coding agent:** Refero Styles (`DESIGN.md` và MCP), OriginKit (MCP, miễn phí), Scrolltide và Motion In Design (prompt kèm spec), Scroll Shaders (copy component React); Iconly qua MCP khi cần icon riêng.
- **Chuyển động:** xem mẫu trên 60fps rồi dùng OriginKit, Scroll Shaders hoặc Scrolltide để dựng; kết hợp skill Emil Kowalski (§7z.1) cho đường cong và thời lượng.
- **Asset:** Backgrounds Supply cho nền, Font In Logo để tìm font gần với thương hiệu tham chiếu.
- Liên quan: §7v (năm trang cảm hứng khác), §7za (8 kho UI sẵn dùng), §7w (MotionSites).

**Nguồn §7zc:** danh sách người dùng gửi 16/11/2026 · WebFetch 16/11/2026: https://www.inspora.design/ · https://godly.website (301 về recent.design) · https://recent.design · https://land-book.com/llms.txt · https://landdding.com · https://landdding.com/pro · https://motionin.design/ · https://www.navbar.gallery · https://www.footer.design · https://www.cta.gallery · https://iconly.ai/ · https://styles.refero.design/ · https://60fps.design/ · https://60fps.design/pro · https://www.scrolltide.co/ · https://scrollshaders.com/ · https://www.originkit.dev/ · https://studio.motionsites.ai/ · https://onepromptdesign.com/ · https://backgrounds.supply/ · clone https://github.com/vellum-ai/originkit/blob/d27526a2e2e728fd2c0c13b28021ade6908211a7/README.md · https://github.com/referodesign/refero_skill/blob/2382e518f90096df607196b9a635da2d1bc142f9/README.md · GitHub search API 16/11/2026.

## 7zd. Sáu công cụ cho designer dùng AI: dream-loop, Hairline, skill Emil Kowalski, skill Meng To, REA, HTML Demo (danh sách người dùng gửi, đọc mã 16/11/2026)

> Người dùng gửi 6 link kèm mô tả. Link `github.com/achimala/dream` không tồn tại; repo đúng là **`achimala/dream-loop`**. Link `fil.design/skills/html-de` là trang **HTML Demo** (`fil.design/skills/html-demo`), mã nằm trong repo `MengTo/Skills`. Skill Emil Kowalski đã có hồ sơ ở §7m.1 và §7z.1.

### 7zd.1 Bảng nhanh

| # | Công cụ | Repo hoặc trang | ★ (16/11/2026) | Giấy phép | Làm gì |
|---|---|---|---|---|---|
| 1 | **dream-loop** | `achimala/dream-loop` | 2.352 | MIT | Skill tạo hình 3D và game đẹp bằng vòng khép kín: sinh ảnh mục tiêu, dựng, critic so ảnh thật với mục tiêu, lặp |
| 2 | **Hairline** | `lucasmarkes/hairline` · hairline.lucasmarkes.com | 3.943 | MIT | 33 hình vẽ nét isometric phản hồi theo con trỏ, SVG không phụ thuộc, cho React và DOM thường |
| 3 | **Skill Emil Kowalski** | `emilkowalski/skills` · emilkowal.ski/skill | (§7z.1) | MIT | 17 skill design engineering về animation, transition, chi tiết tương tác |
| 4 | **Skill Meng To** | `MengTo/Skills` | 7.644 | MIT | 183 skill cho designer và builder: web design, 3D, minh họa, game, workflow, media |
| 5 | **REA** | `morluto/rea` · rea.tools | 463.317 (GitHub search API) | MIT | Một MCP cho agent phân tích ngược app, game, website tới mức binary |
| 6 | **HTML Demo** | fil.design/skills/html-demo · `MengTo/Skills` | (cùng repo Meng To) | MIT (repo) | Skill dựng bản demo app chạy được bằng HTML thay video quay màn hình |

### 7zd.2 Từng công cụ

- **dream-loop** (@anshuc trên X): (1) AI "mơ" ra ảnh mục tiêu chất lượng cao bằng image generation, (2) dựng theo mục tiêu, (3) một AI critic riêng so ảnh chụp thật với mục tiêu và góp ý, (4) lặp tới khi critic hài lòng, (5) có thể mơ mục tiêu mới cao hơn từ trạng thái hiện tại. Cần agent có image generation (sẵn có hoặc qua API như Gemini), đọc được ảnh, nên có subagent; cài Blender khi cần dựng mô hình 3D riêng, qua Blender MCP (§19 §3h) hoặc scripting. Có script `fal-batch.mjs` cho fal và `preview-server.py`; demo trực tiếp dream-loop-demo.anshu.dev. Cài: `npx skills add achimala/dream-loop`.
- **Hairline** (Lucas Marques, v0.5.1): 33 hình nét isometric (ví dụ `Riffle`: khay 8 thẻ, thẻ dưới con trỏ dựng lên, phím mũi tên đi qua từng thẻ), mỗi hình có `intensity` chỉnh độ mạnh phản hồi, tự lấp chiều rộng khung theo tỉ lệ 5:4. Không phụ thuộc, ESM; React 18+ chỉ cần cho bản `/react`. Cài `npm i @lucasmarkes/hairline` hoặc `npx shadcn@latest add https://hairline.lucasmarkes.com/r/hairline.json` (wrapper đọc token theme). Dùng `<Terrain />` trong React hoặc `terrain(el, { play: true })` ở DOM. Có skill vẽ hình mới và `llms.txt`.
- **Skill Emil Kowalski**: xem §7z.1 (17 skill, `npx skills@latest add emilkowalski/skills`).
- **Skill Meng To** (`MengTo/Skills`, 169 commit): 183 file `SKILL.md` chia nhóm `web-design`, `3d`, `illustration` (14 phong cách minh họa SVG), `game-development`, `game-combat`, `ui`, `media`, `workflow`, `codex`. Bốn skill đầu bảng cho quy trình web: biến video quay màn hình thành "super prompt", tách trang HTML thành prompt cho từng section và hiệu ứng, chụp trọn landing page, gom cảm hứng UI hằng ngày thành gói prompt. Định dạng Markdown thuần, dùng được với Codex, Claude Code, Cursor; có `DEMOS.md` liệt kê demo chạy được.
- **REA** (Reverse Engineer Anything): một MCP nối agent tới công cụ phân tích binary native (dùng Hopper, Ghidra, IDA hoặc Kuna có sẵn), app JavaScript và Electron, assembly .NET, APK Android, website (qua kết nối debug trình duyệt cục bộ); phân tích chạy trên máy và kết quả kèm bằng chứng; dựng được môi trường RL từ phiên web đã ghi. Cài: `npx rea-agents setup` (Windows, macOS, Linux). README nhắc chỉ tải từ `morluto/rea`, rea.tools hoặc gói npm `rea-agents`; có `DISCLAIMER.md`, chỉ phân tích phần mềm bạn có quyền.
- **HTML Demo** (Fil, fil.design): dựng một cửa sổ demo sống trên trang web cho thấy app hoạt động qua 3–5 bước, mỗi bước 4–8 giây, sân khấu cố định 1200×750 co giãn sắc nét; mỗi khung là hàm thuần của đồng hồ `t`, con trỏ di chuyển như người thật, tự dừng khi khuất màn hình, có khung cuối cho reduced motion; `shoot.mjs` chụp khung bằng Playwright. Nhập ảnh UI thật, frame từ video docs (ffmpeg) và mã nguồn để chép đúng nhãn, menu, số liệu. Có bản React và JavaScript thuần. Cài Claude Code: tải `https://fil.design/skills/html-demo.zip` giải nén vào `~/.claude/skills`, hoặc `npx degit MengTo/Skills/agent-skills/web-design/html-demo ~/.claude/skills/html-demo`. Fil có 49 skill tải miễn phí (ảnh, video, 3D, web); app Fil hiện chỉ mời.

### 7zd.3 Dùng thế nào

- Dựng hình 3D hay game cần đẹp ngay: dream-loop với Blender MCP và một critic riêng.
- Thêm điểm nhấn tương tác cho landing page: Hairline (hình nét theo con trỏ), cùng nhóm với OriginKit, Scroll Shaders ở §7zc.
- Animation và chi tiết tương tác: skill Emil Kowalski; quy trình từ tham chiếu tới prompt: skill Meng To.
- Học cách một sản phẩm tham khảo được dựng: REA trên app hoặc web bạn có quyền phân tích.
- Trình bày ý tưởng cho khách hàng: HTML Demo thay video quay màn hình.

**Nguồn §7zd:** danh sách người dùng gửi 16/11/2026 · clone `--filter=blob:none` 16/11/2026: https://github.com/achimala/dream-loop/blob/9bddb901f7d071cfefdd21e264267c757177a9df/README.md · https://github.com/lucasmarkes/hairline/blob/034f4bf9902c6adcf3cf39d82f85e6010cb4e094/README.md · https://github.com/MengTo/Skills/blob/3cc93458c4949c39a04e938ea7892a1d6d3d40bf/README.md · https://github.com/morluto/rea/blob/8ffea11ee30d5e0d442a8d14b27e05b0441b9e18/README.md · WebFetch https://hairline.lucasmarkes.com/ · https://rea.tools/ · https://fil.design/skills · https://fil.design/skills/html-demo · GitHub search API 16/11/2026.

## 7ze. Kiểm ảnh bộ skill Figma cho Claude (TELOS Academy): 11 skill từ figma-use tới cc-figma-tokens (ảnh người dùng gửi, đọc mã 16/11/2026)

> Hai ảnh TELOS Academy giới thiệu 11 skill. Danh sách khớp trang [10 Claude Skills for Design](https://www.figma.com/resource-library/claude-skills-for-design/) của Figma; trang này ghi tác giả và link cho từng skill. Ba skill của Figma nằm trong `figma/mcp-server-guide` (đã có hồ sơ ở §7o); `/frontend-design` của Anthropic đã có hồ sơ ở §7g; còn lại là skill cộng đồng, được hồ sơ ở đây.

### 7ze.1 Bảng 11 skill

| Skill | Tác giả | Repo | ★ (16/11/2026) | Làm gì |
|---|---|---|---|---|
| `/figma-use` | Figma | `figma/mcp-server-guide` → `skills/figma-use` | 2.197 (repo) | Cho Claude đọc, đi lại và thao tác trên file Figma: component, layer, variable, frame; nền cho mọi skill Figma khác |
| `/figma-generate-design` | Figma | cùng repo → `skills/figma-generate-design` | | Dựng màn hình, layout, component mới từ thư viện component đã duyệt |
| `/figma-generate-library` | Figma | cùng repo → `skills/figma-generate-library` | | Từ codebase sinh thư viện component Figma tương ứng |
| `/audit-design-system` | Chris Goebel, Edenspiekermann | `edenspiekermann/Skills` | 68 | Rà màn hình hoặc component tìm chỗ lệch design system: thiếu component dùng chung, override cục bộ, token chưa gắn |
| `/apply-design-system` | Chris Goebel, Edenspiekermann | cùng repo | | Gắn lại phần tử lẻ về đúng component và token |
| `/create-voice` | Ian Guisard, Uber | `redongreen/uSpec` | 251 | Sinh đặc tả screen reader cho VoiceOver, TalkBack, ARIA từ component Figma |
| `/rad-spacing` | Nolan Perkins, Rad Collab | `nolanperk/rad-spacing` | 17 | Áp spacing theo cấp bậc bằng biến có sẵn, có quy tắc dự phòng khi thiếu token |
| `/sync-figma-token` | Anish Karthik, Firebender | `firebenders/sync-figma-token-skill` | 27 | So token giữa Figma variables và codebase, báo chỗ lệch |
| `/frontend-design` | Anthropic | `anthropics/claude-code` → `plugins/frontend-design` | (§7g) | Bắt Claude lập brief sáng tạo (mục đích, tông giọng, ràng buộc, điểm nhớ) trước khi tạo UI |
| `/cc-figma-component`, `/cc-figma-tokens` | Nick Villapiano, One North | `nvillapiano/component-contracts-figma` | 34 | Từ file JSON đặc tả (component contract) sinh component set hoặc biến token trong Figma |

### 7ze.2 Điểm mạnh các skill cộng đồng (đọc mã)

- **Edenspiekermann** (3 skill, 165–235 dòng mỗi file): quy trình ba bước rà → sửa từng phát hiện → gắn lại. `audit-design-system` phân loại ba kiểu lệch (thiếu component dùng chung, override cục bộ, token chưa gắn); `fix-design-system-finding` sửa đúng một phát hiện; `apply-design-system` rà rồi nối lại cả màn hình. Repo có sẵn mục `.claude/skills/` nên mở repo trong Claude Code là dùng được lệnh slash.
- **uSpec** (MIT, 67 commit, 13 skill): sinh tài liệu design system cho component từ agent: anatomy, API, cấu trúc, màu, motion, property, voice; plugin Figma "uSpec Extract" chụp component, rồi `create-component-md` sinh cặp `.json` và `.md` làm hợp đồng máy đọc. `create-voice` (891 dòng) viết đặc tả VoiceOver, TalkBack và ARIA cho từng trạng thái.
- **rad-spacing**: xác định độ sâu lồng (trang → section → card → nội dung → phần tử dòng), dùng biến spacing sẵn có trong thư viện theo đúng cách đặt tên đang dùng; nếu chưa có thì tạo bộ `spacing/xs…3xl` (4–48px); mỗi cấp cha lớn hơn cấp con khoảng 1,4 lần rồi làm tròn về bội 8px (hoặc 4px), theo nguyên tắc gần gũi Gestalt.
- **sync-figma-token**: đồng bộ token giữa code và Figma variables với báo cáo lệch nghiêm ngặt, **bắt buộc duyệt trước khi áp**, chỉ áp phần chênh và lưu báo cáo.
- **component-contracts-figma**: một file contract là nguồn chung cho cả code và Figma; `cc-figma-tokens` dựng collection Primitives và Semantic, `cc-figma-component` dựng component set với variant theo contract.

### 7ze.3 Cài và dùng

- Ba skill Figma: cài plugin `figma` từ `figma/mcp-server-guide` (hướng dẫn trong §7o) và nối Figma MCP (`mcp.figma.com/mcp`).
- Skill cộng đồng: chép thư mục skill vào `~/.claude/skills/` hoặc `.claude/skills/` của dự án; Figma còn gom các skill ở trang Community Skills (figma.com/community/skills).
- Bốn repo `edenspiekermann/Skills`, `nolanperk/rad-spacing`, `firebenders/sync-figma-token-skill`, `nvillapiano/component-contracts-figma` chưa kèm file LICENSE; dùng nội bộ thì chép được, muốn phân phối lại thì hỏi tác giả.
- Gợi ý quy trình: `/frontend-design` lập brief → `/figma-generate-design` dựng bằng thư viện có sẵn → `/rad-spacing` chuẩn spacing → `/audit-design-system` rồi `/apply-design-system` → `/sync-figma-token` trước khi bàn giao code → `/create-voice` cho đặc tả screen reader.

**Nguồn §7ze:** ảnh người dùng gửi 16/11/2026 · https://www.figma.com/resource-library/claude-skills-for-design/ (WebFetch 16/11/2026) · clone `--filter=blob:none` 16/11/2026: https://github.com/figma/mcp-server-guide/blob/5f3024c3decd83ff6f0bfb3ef36a2c4cfbff961d/README.md · https://github.com/edenspiekermann/Skills/blob/a49e859329aa99e81e8725bc66767d16e8fc9539/README.md · https://github.com/redongreen/uSpec/blob/1e25e9b8bc2e694689ba0489594f38807a341f14/README.md · https://github.com/nolanperk/rad-spacing/blob/15e911236edca0d6c30d29a24581112ae7635a08/rad-spacing.md · https://github.com/firebenders/sync-figma-token-skill/blob/c017392e2061874124eef61b9f29a7301ad844d1/skills/sync-figma-token/SKILL.md · https://github.com/nvillapiano/component-contracts-figma/blob/14db03bba7727122a7704d46aef1a5f28a2d6dcc/skills/cc-figma-component/SKILL.md · GitHub search API 16/11/2026.

## 7zf. Hồ sơ imskyleen/animate-ui (Animate UI): primitive có animation thay thẳng cho Radix UI, Base UI, React Aria, giữ nguyên component shadcn/ui (ảnh README người dùng gửi, đọc mã 17/11/2026)

> Ảnh là phần đầu README: "Animated drop-in primitives for Radix UI, Base UI and React Aria, built with Motion. Swap the import, keep your shadcn/ui components.", badge 5K sao, license "MIT + Commons Clause", site animate-ui.com.

### 7zf.1 Hồ sơ nhanh

| Thuộc tính | Giá trị (17/11/2026) |
|---|---|
| Repo | https://github.com/imskyleen/animate-ui · **5.063★, 288 fork** (GitHub search API) · tạo 26/3/2025 · site animate-ui.com |
| Tác giả | Elliot Sutton (1.102/1.189 commit) |
| Giấy phép | MIT kèm Commons Clause: dùng trong mọi ứng dụng, website, sản phẩm kể cả thương mại; không bán hoặc phân phối lại chính các component ở dạng gốc |
| Gói | `@animate-ui/react` 2.4.6 (primitive cho Radix UI, Base UI, React Aria), `@animate-ui/vue` 2.4.6 (cho reka-ui/shadcn-vue), `@animate-ui/cli` 2.4.0 (codemod) |
| Kiểm thử | CLI có thư mục `test/` (vitest), thư mục `e2e/` chạy trình duyệt |

### 7zf.2 Điểm mạnh (đọc mã)

- **Đổi một dòng import là có animation**: mỗi primitive giữ **đúng API của thư viện gốc**, chỉ thêm Motion bên trong, nên component shadcn/ui giữ nguyên. Ví dụ `import { Accordion as AccordionPrimitive } from 'radix-ui'` thành `… from '@animate-ui/react/primitives/radix-ui'`.
- **Một lệnh cho cả dự án**: `npx @animate-ui/cli@latest animate all` chạy codemod đổi primitive của mọi component shadcn/ui đã cài; lệnh `migrate` chuyển dần từ bản v1.
- **Phủ ba thư viện headless**: trong `packages/react` có primitive cho Radix UI, Base UI và React Aria; thêm bản Vue cho reka-ui.
- **Ngôn ngữ chuyển động thống nhất**: phần lớn chuyển động dùng spring, mỗi vai trò chuyển động một giá trị token, tween chọn đường cong theo việc phần tử làm; mượn quy tắc thực hành của Emil Kowalski (gốc theo trigger, ease-out khi vào/ra, phản hồi khi nhấn, tôn trọng reduced motion), ghi nguồn MIT trong `NOTICE.md`.
- **Có agent skill đi kèm**: `skills/animate-ui/` (41 file) hướng dẫn agent chọn đường đi (codemod cho shadcn/ui hay đổi import thủ công), danh mục component, token cảm giác chuyển động, công thức tương tác (banner, count badge, expanding card…).

### 7zf.3 Cài và dùng

```bash
npx @animate-ui/cli@latest animate all
```

- Dự án dùng shadcn/ui (React) hoặc shadcn-vue: chạy lệnh trên, rồi kiểm lại UI.
- Component tự viết trên Radix UI, Base UI, React Aria: đổi import sang `@animate-ui/react/primitives/<thư viện>`.
- Agent: chép `skills/animate-ui/` vào thư mục skill để agent tự chọn cách làm.
- Giấy phép cho phép dùng trong sản phẩm thương mại; khi đóng gói lại thành bộ component để bán hoặc phát tán thì cần xin phép tác giả.
- Liên quan: §7za (8 kho UI sẵn dùng), skill Emil Kowalski §7z.1, mục 22 (animation).

**Nguồn §7zf:** ảnh README người dùng gửi 17/11/2026 · clone https://github.com/imskyleen/animate-ui HEAD `9873c628afdcdb030e74dc2930774a2aa473bd39`: https://github.com/imskyleen/animate-ui/blob/9873c628afdcdb030e74dc2930774a2aa473bd39/README.md · https://github.com/imskyleen/animate-ui/blob/9873c628afdcdb030e74dc2930774a2aa473bd39/LICENSE.md · https://github.com/imskyleen/animate-ui/blob/9873c628afdcdb030e74dc2930774a2aa473bd39/skills/animate-ui/SKILL.md · https://github.com/imskyleen/animate-ui/blob/9873c628afdcdb030e74dc2930774a2aa473bd39/skills/animate-ui/NOTICE.md · GitHub search API 17/11/2026.

## 7zg. Hồ sơ penpot/penpot: nền tảng thiết kế mã mở tự host, design token gốc, MCP server chính thức (ảnh README người dùng gửi, đọc mã 19/11/2026)

> **Nguồn:** ảnh trang repo GitHub (README, giấy phép MPL-2.0). Clone nông HEAD `b100a5e` (commit 19/11/2026), đọc README, LICENSE, `CHANGES.md`, `mcp/README.md` và cây `backend/`, `frontend/`, `render-wasm/`, `plugins/`, `docker/`. GitHub search API 19/11/2026: ★ 62.550, fork 4.442, MPL-2.0, tạo 29/12/2015. Bảng §1 có dòng Penpot cũ (~62k, 30/10/2026); hồ sơ này bổ sung chi tiết.

**Làm gì:** nền tảng thiết kế và prototype mã nguồn mở, thay thế Figma, chạy được trên SaaS (design.penpot.app) hoặc tự host bằng Docker, Kubernetes. Thiết kế được lưu dưới dạng mã (SVG, CSS, HTML), nên lập trình viên và AI đọc được trực tiếp.

**Điểm mạnh (đọc mã):**

- **Gần với code:** layout CSS Grid và Flex thật, tab Inspect cho SVG, CSS, HTML dùng ngay; design token gốc làm một nguồn sự thật giữa thiết kế và code, cùng component và variant cho design system.
- **MCP server chính thức** ([`mcp/`](https://github.com/penpot/penpot/blob/b100a5e26f9b0d762ce3edbd00997d4b7f0874fb/mcp/README.md)): LLM truy vấn, sửa và tạo phần tử thiết kế qua Plugin API; server nói với plugin Penpot MCP qua WebSocket. Hỗ trợ luồng thiết kế → code, code → thiết kế.
- **Lập trình được:** hệ plugin (`plugins/`, có tài liệu API và style), webhook, API dùng access token.
- **Kiến trúc mở rộng được:** backend và frontend Clojure/ClojureScript, renderer mới viết bằng Rust biên dịch WebAssembly (`render-wasm/`), dịch vụ exporter và media-processor riêng; `docker/images/` có Dockerfile cho backend, frontend, exporter, mcp, media-processor và `docker-compose.yaml`.
- **Bảo trì chủ động:** CHANGES.md bản 2.21.0 có mục sửa bảo mật kèm GHSA (WebSocket cộng tác không kiểm lại quyền truy cập file sau khi bị thu hồi); Renovate cập nhật phụ thuộc; được công nhận Digital Public Good.

**Cài và dùng:** dùng ngay tại design.penpot.app, hoặc tự host theo hướng dẫn penpot.app/self-host với `docker/images/docker-compose.yaml`. MCP: chạy server trong `mcp/` rồi cài plugin Penpot MCP vào file thiết kế, xem hướng dẫn nhanh help.penpot.app/mcp.

**Điều kiện:** MPL-2.0, giấy phép copyleft theo từng file: sửa file của Penpot thì phải công khai file đó, mã của mình ghép bên cạnh không bị ràng buộc. Penpot Enterprise là gói trả phí cho quản trị nhiều đội. MCP cho LLM viết và chạy đoạn mã tuỳ ý trong môi trường plugin của file đang mở: nên dùng trên file có bản sao lưu và với LLM được tin cậy.

**Dùng khi:** cần công cụ thiết kế tự host, giữ dữ liệu thiết kế trong hạ tầng của mình, hoặc muốn agent đọc và sửa thiết kế qua MCP. Liên quan: §1 (bảng công cụ thiết kế), §7ze (skill Figma cho Claude, so khớp token thiết kế và code).

## 8. Nguồn (mục 1–6)

- https://designrevision.com/blog/best-react-component-libraries · https://designrevision.com/blog/best-tailwind-component-libraries · https://dualite.dev/blogs/best-ui-component-libraries · https://www.uilora.com/blog/uilora/10-best-react-ui-component-libraries-in-2026-ranked-by-a-frontend-team · https://www.techwench.com/best-ui-component-libraries-2026/
- https://www.opensourcealternatives.to/item/penpot · https://openalternative.co/excalidraw · https://www.libhunt.com/compare-penpot-vs-excalidraw · https://storyflow.so/blog/best-excalidraw-alternatives-2026
- https://www.figma.com/resource-library/ai-design-tools/ · https://open-design.ai/blog/best-ai-design-tools/ · https://designtools.fyi/facets/ui-generation · https://github.com/narrowin/awesome-generative-ui · https://dev.to/hadil/24-best-ai-design-tools-for-designers-and-developers-in-2026-i1h
- https://www.tasteskill.dev/ · https://www.x-cmd.com/install/taste-skill/ · https://apito.ai/en/blog/seo/ai-frontend-template-look-taste-skill/ · https://github.com/maxbogo/awesome-ai-tools-for-ui
- https://refactoringui.com/ · https://github.com/klaufel/awesome-design-systems · https://github.com/bradtraversy/design-resources-for-developers · https://designsystemsrepo.com/design-systems/ · https://designsystems.surf/design-systems
- https://github.com/copilotkit/copilotkit · https://github.com/ag-ui-protocol/ag-ui · https://techcrunch.com/2026/05/05/copilotkit-raises-27m-to-help-devs-deploy-app-native-ai-agents/ · https://alatirok.com/best-ai-agent-chat-ui-library/

<a id="anhkysuai-2026-11-23"></a>

## Đánh giá từ kho Anh Kỹ Sư AI — 23/11/2026

Phần này có **74 hồ sơ hoặc phạm vi đối chiếu** từ [nguồn tuyển chọn](https://anhkysuai.com/kho/). [Bảng đủ 1.295 repo](../data/collections/anhkysuai-kho.json) ghi trạng thái đối chiếu từng link; [danh sách URL](../data/collections/anhkysuai-kho-links.txt) phục vụ tra cứu. Nguồn tuyển chọn giúp phát hiện repo; đánh giá bên dưới dựa trên clone và permalink upstream cùng metadata GitHub ngày 2026-11-23.

Mức `docs-read`/`code-read` chỉ áp dụng phạm vi ghi tại mỗi hồ sơ. Chưa cài, build, chạy test hay benchmark mã upstream. Giấy phép có thể tách theo code, model, nội dung, asset hoặc bản enterprise; con số/tuyên bố của tác giả chưa được tái lập nếu không có ghi chú khác.

<a id="anhkysuai-2026-11-23-photocraft"></a>

### PhotoCraft

**Repo:** [storytold/photocraft](https://github.com/storytold/photocraft) · **License:** MIT OR Apache-2.0 · **★ 81,102 (GitHub API, 2026-11-23)**

**Mục đích:** Trình sửa ảnh desktop bằng Rust, làm việc với layer, mask và tài liệu PSD.

**Giá trị và cơ chế:** README và workspace tách engine tài liệu, raster và giao diện; cùng hệ lệnh được mô tả cho UI, CLI và MCP, đáng tham khảo khi muốn AI thao tác ứng dụng native.

**Giới hạn:** Tỷ lệ tương thích PSD và tốc độ GPU là số tác giả công bố; chưa mở tệp thử hay xác minh control channel. Một số codec cần feature riêng.

**Cách tham khảo/tích hợp:** Thử bằng corpus PSD có layer của dự án trước khi dùng làm bộ chuyển đổi; ghim cả revision craft-libs.

**Thay thế:** gimp, krita, [Penpot](../06-ui-ux-design/README.md#7zg-hồ-sơ-penpotpenpot-nền-tảng-thiết-kế-mã-mở-tự-host-design-token-gốc-mcp-server-chính-thức-ảnh-readme-người-dùng-gửi-đọc-mã-19112026).

**Bằng chứng:** `docs-read`, ngày 2026-11-23, commit [`42ade5fc41a6`](https://github.com/storytold/photocraft/commit/42ade5fc41a6669c1bc5c80375ca094488c0de04). README và các tài liệu/manifest/CI hiện diện, đọc chọn lọc; chưa kiểm implementation. Chưa cài/chạy upstream.

**Nguồn:** [README.md](https://github.com/storytold/photocraft/blob/42ade5fc41a6669c1bc5c80375ca094488c0de04/README.md) · [LICENSE-APACHE](https://github.com/storytold/photocraft/blob/42ade5fc41a6669c1bc5c80375ca094488c0de04/LICENSE-APACHE) · [LICENSE-MIT](https://github.com/storytold/photocraft/blob/42ade5fc41a6669c1bc5c80375ca094488c0de04/LICENSE-MIT) · [metadata GitHub](https://api.github.com/repos/storytold/photocraft).

<a id="anhkysuai-2026-11-23-apache-echarts"></a>

### Apache ECharts

**Repo:** [apache/echarts](https://github.com/apache/echarts) · **License:** Apache-2.0; các phần dẫn xuất theo NOTICE/LICENSE · **★ 67,783 (GitHub API, 2026-11-23)**

**Mục đích:** Thư viện JavaScript tạo biểu đồ tương tác cho dashboard và ứng dụng web.

**Giá trị và cơ chế:** README mô tả lớp biểu đồ trên zrender, có gói npm, kiểu TypeScript và quy trình dựng bản phân phối; thích hợp cho bộ biểu đồ cấu hình được.

**Giới hạn:** Chưa chạy render, đo dữ liệu lớn hay kiểm accessibility. LICENSE còn liệt kê mã dẫn xuất và giấy phép liên quan, nên không chỉ giữ nhãn của package.

**Cách tham khảo/tích hợp:** Chọn loại biểu đồ và chỉ nạp thành phần cần dùng; kiểm kích thước bundle, nội dung tooltip và điều kiện attribution.

**Thay thế:** plotly, chartjs, [Recharts](../06-ui-ux-design/README.md#anhkysuai-2026-11-23-recharts).

**Bằng chứng:** `docs-read`, ngày 2026-11-23, commit [`34f4d927eafe`](https://github.com/apache/echarts/commit/34f4d927eafe251f26f63afd3aeefa30f2feba30). README và các tài liệu/manifest/CI hiện diện, đọc chọn lọc; chưa kiểm implementation. Chưa cài/chạy upstream.

**Nguồn:** [README.md](https://github.com/apache/echarts/blob/34f4d927eafe251f26f63afd3aeefa30f2feba30/README.md) · [LICENSE](https://github.com/apache/echarts/blob/34f4d927eafe251f26f63afd3aeefa30f2feba30/LICENSE) · [metadata GitHub](https://api.github.com/repos/apache/echarts).

<a id="anhkysuai-2026-11-23-drawio-desktop"></a>

### draw.io Desktop

**Repo:** [jgraph/drawio-desktop](https://github.com/jgraph/drawio-desktop) · **License:** GPL-3.0-only · **★ 64,111 (GitHub API, 2026-11-23)**

**Mục đích:** Ứng dụng Electron đóng gói trình biên tập sơ đồ draw.io để dùng trên desktop.

**Giá trị và cơ chế:** README phân biệt installer, bản portable và cơ chế cập nhật theo nền tảng; package có bài kiểm Node riêng, phù hợp nhu cầu sơ đồ lưu thành tệp cục bộ.

**Giới hạn:** Tài liệu nói không gửi nội dung sơ đồ nhưng thừa nhận media nhúng từ URL có thể tạo kết nối ngoài. Chưa kiểm lưu lượng hoặc đọc renderer; không coi ứng dụng hoàn toàn ngoại tuyến.

**Cách tham khảo/tích hợp:** Kiểm đường dẫn media/font và cấu hình cập nhật; đánh giá nghĩa vụ GPL nếu sửa và phân phối bản đóng gói.

**Thay thế:** [Excalidraw](https://github.com/excalidraw/excalidraw), [Mermaid](https://github.com/mermaid-js/mermaid), [D2](../16-docs-tools/README.md#anhkysuai-2026-11-23-d2).

**Bằng chứng:** `docs-read`, ngày 2026-11-23, commit [`5e8406789216`](https://github.com/jgraph/drawio-desktop/commit/5e8406789216bed8f043bc503f4927b4034d7a71). README và các tài liệu/manifest/CI hiện diện, đọc chọn lọc; chưa kiểm implementation. Chưa cài/chạy upstream.

**Nguồn:** [README.md](https://github.com/jgraph/drawio-desktop/blob/5e8406789216bed8f043bc503f4927b4034d7a71/README.md) · [LICENSE](https://github.com/jgraph/drawio-desktop/blob/5e8406789216bed8f043bc503f4927b4034d7a71/LICENSE) · [metadata GitHub](https://api.github.com/repos/jgraph/drawio-desktop).

<a id="anhkysuai-2026-11-23-streamlit"></a>

### Streamlit

**Repo:** [streamlit/streamlit](https://github.com/streamlit/streamlit) · **License:** Apache-2.0 · **★ 46,485 (GitHub API, 2026-11-23)**

**Mục đích:** Framework viết ứng dụng dữ liệu và giao diện tương tác bằng Python.

**Giá trị và cơ chế:** README nêu bảng chỉnh sửa, form, chat và streaming trong cùng lớp Python; phù hợp dựng công cụ nội bộ nơi tính toán và quyết định cần xuất hiện cạnh nhau.

**Giới hạn:** Tuyên bố quy mô sử dụng và khả năng enterprise chưa được kiểm độc lập. Chưa thử quản lý session, auth hoặc tải đồng thời; tài liệu hiện thông báo tạm ngừng nhận PR ngoài nhóm duy trì.

**Cách tham khảo/tích hợp:** Tách logic dữ liệu khỏi giao diện, kiểm cache theo người dùng và quyền truy cập trước khi chia sẻ app.

**Thay thế:** [gradio](../08-awesome-lists-learning/README.md#6c513-mô-hình-ai--huấn-luyện), [dash](../08-awesome-lists-learning/README.md#6c527-đồ-họa-3d--sơ-đồ), panel.

**Bằng chứng:** `docs-read`, ngày 2026-11-23, commit [`259fbb652404`](https://github.com/streamlit/streamlit/commit/259fbb652404888bff49b923b8228bd2bd9d4888). README và các tài liệu/manifest/CI hiện diện, đọc chọn lọc; chưa kiểm implementation. Chưa cài/chạy upstream.

**Nguồn:** [README.md](https://github.com/streamlit/streamlit/blob/259fbb652404888bff49b923b8228bd2bd9d4888/README.md) · [LICENSE](https://github.com/streamlit/streamlit/blob/259fbb652404888bff49b923b8228bd2bd9d4888/LICENSE) · [metadata GitHub](https://api.github.com/repos/streamlit/streamlit).

<a id="anhkysuai-2026-11-23-jsoncrack"></a>

### JSON Crack

**Đã chuyển (2026-11-23):** hồ sơ này nay nằm ở [mục 13](../13-dev-stack-devops/README.md#anhkysuai-2026-11-23-jsoncrack); catalog con xem [catalog/](../catalog/README.md).

<a id="anhkysuai-2026-11-23-xyflow"></a>

### xyflow

**Repo:** [xyflow/xyflow](https://github.com/xyflow/xyflow) · **License:** MIT · **★ 39,122 (GitHub API, 2026-11-23)**

**Mục đích:** Các thư viện React, Svelte và Vue để dựng giao diện node và flow tương tác.

**Giá trị và cơ chế:** Monorepo chia packages theo framework và lớp system dùng chung; thuận tiện làm editor workflow với UI tùy biến nhưng giữ một bộ primitive chung.

**Giới hạn:** README phân biệt rõ yêu cầu hỗ trợ trả phí khi bỏ attribution là kỳ vọng của tác giả, không phải điều kiện pháp lý của MIT. Chưa kiểm performance của đồ thị lớn hay accessibility.

**Cách tham khảo/tích hợp:** Dùng đúng package của framework; tách model workflow khỏi vị trí node và xác minh quy tắc kết nối tại backend.

**Thay thế:** rete, drawflow, [Excalidraw](https://github.com/excalidraw/excalidraw).

**Bằng chứng:** `docs-read`, ngày 2026-11-23, commit [`8b95de4602fd`](https://github.com/xyflow/xyflow/commit/8b95de4602fd1fa10243b2fe1b0916aeab551337). README và các tài liệu/manifest/CI hiện diện, đọc chọn lọc; chưa kiểm implementation. Chưa cài/chạy upstream.

**Nguồn:** [README.md](https://github.com/xyflow/xyflow/blob/8b95de4602fd1fa10243b2fe1b0916aeab551337/README.md) · [LICENSE](https://github.com/xyflow/xyflow/blob/8b95de4602fd1fa10243b2fe1b0916aeab551337/LICENSE) · [metadata GitHub](https://api.github.com/repos/xyflow/xyflow).

<a id="anhkysuai-2026-11-23-sharp"></a>

### sharp

**Repo:** [lovell/sharp](https://github.com/lovell/sharp) · **License:** Apache-2.0 · **★ 32,867 (GitHub API, 2026-11-23)**

**Mục đích:** Thư viện Node.js xử lý và chuyển đổi ảnh dựa trên libvips.

**Giá trị và cơ chế:** README và manifest cho thấy API phục vụ resize, xoay, ghép và xuất nhiều định dạng; phù hợp pipeline thumbnail hoặc ảnh web bên máy chủ.

**Giới hạn:** Tuyên bố tốc độ trong README chưa được đo lại. Binary native, phiên bản Node và codec tùy bản dựng ảnh hưởng triển khai; không phải trình biên tập tài liệu nhiều layer.

**Cách tham khảo/tích hợp:** Đo kích thước, thời gian và bộ nhớ với ảnh thực; ghim phiên bản và giới hạn đầu vào trong dịch vụ upload.

**Thay thế:** [ImageMagick](../06-ui-ux-design/README.md#anhkysuai-2026-11-23-imagemagick), pillow, libvips.

**Bằng chứng:** `docs-read`, ngày 2026-11-23, commit [`461a8d56e31e`](https://github.com/lovell/sharp/commit/461a8d56e31e081f0791f4c6265ac2b184a0d4ec). README và các tài liệu/manifest/CI hiện diện, đọc chọn lọc; chưa kiểm implementation. Chưa cài/chạy upstream.

**Nguồn:** [README.md](https://github.com/lovell/sharp/blob/461a8d56e31e081f0791f4c6265ac2b184a0d4ec/README.md) · [LICENSE](https://github.com/lovell/sharp/blob/461a8d56e31e081f0791f4c6265ac2b184a0d4ec/LICENSE) · [metadata GitHub](https://api.github.com/repos/lovell/sharp).

<a id="anhkysuai-2026-11-23-graphite"></a>

### Graphite

**Repo:** [GraphiteEditor/Graphite](https://github.com/GraphiteEditor/Graphite) · **License:** MIT OR Apache-2.0 · **★ 28,014 (GitHub API, 2026-11-23)**

**Mục đích:** Trình thiết kế đồ họa kết hợp chỉnh sửa vector và quy trình node theo thủ tục.

**Giá trị và cơ chế:** README và workspace Rust chia editor, giao diện, lưu trữ/migration; có giá trị tham khảo mô hình tài liệu dùng chung cho thao tác trực tiếp và graph.

**Giới hạn:** Dự án tự ghi alpha; nhiều khả năng motion/VFX được trình bày như hướng phát triển. Chưa mở tài liệu, đo GPU hay xác nhận độ ổn định xuất file.

**Cách tham khảo/tích hợp:** Thử bản ghim với tài sản có thể phục hồi, tập trung học mô hình node và lệnh chỉnh sửa trước dùng sản xuất.

**Thay thế:** inkscape, [Penpot](../06-ui-ux-design/README.md#7zg-hồ-sơ-penpotpenpot-nền-tảng-thiết-kế-mã-mở-tự-host-design-token-gốc-mcp-server-chính-thức-ảnh-readme-người-dùng-gửi-đọc-mã-19112026), krita.

**Bằng chứng:** `docs-read`, ngày 2026-11-23, commit [`615b4050ba4d`](https://github.com/GraphiteEditor/Graphite/commit/615b4050ba4d247712dfd2fca745d87a9bba315f). README và các tài liệu/manifest/CI hiện diện, đọc chọn lọc; chưa kiểm implementation. Chưa cài/chạy upstream.

**Nguồn:** [README.md](https://github.com/GraphiteEditor/Graphite/blob/615b4050ba4d247712dfd2fca745d87a9bba315f/README.md) · [LICENSE-APACHE](https://github.com/GraphiteEditor/Graphite/blob/615b4050ba4d247712dfd2fca745d87a9bba315f/LICENSE-APACHE) · [LICENSE-MIT](https://github.com/GraphiteEditor/Graphite/blob/615b4050ba4d247712dfd2fca745d87a9bba315f/LICENSE-MIT) · [metadata GitHub](https://api.github.com/repos/GraphiteEditor/Graphite).

<a id="anhkysuai-2026-11-23-recharts"></a>

### Recharts

**Repo:** [recharts/recharts](https://github.com/recharts/recharts) · **License:** MIT · **★ 27,739 (GitHub API, 2026-11-23)**

**Mục đích:** Thành phần biểu đồ React dựng từ SVG và các tiện ích D3.

**Giá trị và cơ chế:** README mô tả composable chart components; phù hợp dashboard React cần khai báo trục, tooltip và series bằng JSX.

**Giới hạn:** Không có phép đo render dữ liệu lớn trong lần đánh giá. SVG và cập nhật React có chi phí; README lưu ý đồng bộ phiên bản react-is với React và phân biệt nhánh phát triển/phát hành.

**Cách tham khảo/tích hợp:** Tạo biểu đồ với số điểm thực, kiểm responsive, tooltip và khả năng truy cập trước đưa thành design system.

**Thay thế:** [visx](../06-ui-ux-design/README.md#anhkysuai-2026-11-23-visx), [Apache ECharts](../06-ui-ux-design/README.md#anhkysuai-2026-11-23-apache-echarts), nivo.

**Bằng chứng:** `docs-read`, ngày 2026-11-23, commit [`9f1a412cf6fd`](https://github.com/recharts/recharts/commit/9f1a412cf6fd774175eb2282478e06256d29beeb). README và các tài liệu/manifest/CI hiện diện, đọc chọn lọc; chưa kiểm implementation. Chưa cài/chạy upstream.

**Nguồn:** [README.md](https://github.com/recharts/recharts/blob/9f1a412cf6fd774175eb2282478e06256d29beeb/README.md) · [LICENSE](https://github.com/recharts/recharts/blob/9f1a412cf6fd774175eb2282478e06256d29beeb/LICENSE) · [metadata GitHub](https://api.github.com/repos/recharts/recharts).

<a id="anhkysuai-2026-11-23-chartdb"></a>

### ChartDB

**Repo:** [chartdb/chartdb](https://github.com/chartdb/chartdb) · **License:** AGPL-3.0 · **★ 23,159 (GitHub API, 2026-11-23)**

**Mục đích:** Ứng dụng dựng và chỉnh sửa sơ đồ schema cơ sở dữ liệu trong trình duyệt.

**Giá trị và cơ chế:** README trình bày SmartQuery lấy schema dạng JSON, sơ đồ quan hệ và xuất DDL có hỗ trợ AI; phù hợp tài liệu hóa và trao đổi mô hình dữ liệu.

**Giới hạn:** Dự án ghi public beta; chưa thử import schema hoặc tính đúng DDL sinh ra. AI có thể dùng OpenAI/endpoint tùy chỉnh, nên phải biết metadata được gửi đi đâu.

**Cách tham khảo/tích hợp:** Nhập schema không chứa dữ liệu nghiệp vụ, duyệt DDL bằng công cụ migration và DB thử trước áp dụng.

**Thay thế:** [draw.io Desktop](../06-ui-ux-design/README.md#anhkysuai-2026-11-23-drawio-desktop), dbdiagram, [drawdb](../08-awesome-lists-learning/README.md#6c527-đồ-họa-3d--sơ-đồ).

**Bằng chứng:** `docs-read`, ngày 2026-11-23, commit [`ee95448d154c`](https://github.com/chartdb/chartdb/commit/ee95448d154cfdcf65264c45745f440c0480ef84). README và các tài liệu/manifest/CI hiện diện, đọc chọn lọc; chưa kiểm implementation. Chưa cài/chạy upstream.

**Nguồn:** [README.md](https://github.com/chartdb/chartdb/blob/ee95448d154cfdcf65264c45745f440c0480ef84/README.md) · [LICENSE](https://github.com/chartdb/chartdb/blob/ee95448d154cfdcf65264c45745f440c0480ef84/LICENSE) · [metadata GitHub](https://api.github.com/repos/chartdb/chartdb).

<a id="anhkysuai-2026-11-23-visx"></a>

### visx

**Repo:** [airbnb/visx](https://github.com/airbnb/visx) · **License:** MIT · **★ 21,117 (GitHub API, 2026-11-23)**

**Mục đích:** Các thành phần trực quan hóa cấp thấp kết hợp D3 và React.

**Giá trị và cơ chế:** README có ví dụ dựng bar chart từ scale, shape và group; phù hợp xây biểu đồ riêng theo design system thay vì phụ thuộc một cấu hình chart khép kín.

**Giới hạn:** Nhóm dùng phải tự kết nối trục, tooltip và tương tác; v4 yêu cầu React 18/19. Chưa đo render dữ liệu lớn hoặc kiểm accessibility trên dashboard.

**Cách tham khảo/tích hợp:** Đóng gói thành component nội bộ sau khi chốt scale/format và thử resize với dữ liệu thiếu.

**Thay thế:** [Recharts](../06-ui-ux-design/README.md#anhkysuai-2026-11-23-recharts), [Apache ECharts](../06-ui-ux-design/README.md#anhkysuai-2026-11-23-apache-echarts), nivo.

**Bằng chứng:** `docs-read`, ngày 2026-11-23, commit [`485c0359664e`](https://github.com/airbnb/visx/commit/485c0359664ee8e612992defb16e1f035ed40b23). README và các tài liệu/manifest/CI hiện diện, đọc chọn lọc; chưa kiểm implementation. Chưa cài/chạy upstream.

**Nguồn:** [README.md](https://github.com/airbnb/visx/blob/485c0359664ee8e612992defb16e1f035ed40b23/README.md) · [LICENSE](https://github.com/airbnb/visx/blob/485c0359664ee8e612992defb16e1f035ed40b23/LICENSE) · [metadata GitHub](https://api.github.com/repos/airbnb/visx).

<a id="anhkysuai-2026-11-23-imagemagick"></a>

### ImageMagick

**Repo:** [ImageMagick/ImageMagick](https://github.com/ImageMagick/ImageMagick) · **License:** ImageMagick License · **★ 17,919 (GitHub API, 2026-11-23)**

**Mục đích:** Bộ CLI và API C tạo, chỉnh sửa, ghép và chuyển đổi ảnh bitmap.

**Giá trị và cơ chế:** README mô tả nhiều định dạng và thao tác có thể ghép thành pipeline; hữu ích tự động hóa tài sản, thumbnail và xuất ảnh từ tài liệu.

**Giới hạn:** README yêu cầu thiết kế security policy cho môi trường; delegate/codec thực tế tùy bản dựng. Chưa kiểm file không tin cậy hoặc so sánh chất lượng chuyển đổi. License riêng cho phép dùng thương mại với điều kiện thông báo.

**Cách tham khảo/tích hợp:** Giới hạn định dạng, tài nguyên và delegate; kiểm corpus đầu vào cùng font/color profile trước triển khai.

**Thay thế:** [sharp](../06-ui-ux-design/README.md#anhkysuai-2026-11-23-sharp), libvips, graphicsmagick.

**Bằng chứng:** `docs-read`, ngày 2026-11-23, commit [`3eeefb963328`](https://github.com/ImageMagick/ImageMagick/commit/3eeefb9633286904621822e9721971e266af7288). README và các tài liệu/manifest/CI hiện diện, đọc chọn lọc; chưa kiểm implementation. Chưa cài/chạy upstream.

**Nguồn:** [README.md](https://github.com/ImageMagick/ImageMagick/blob/3eeefb9633286904621822e9721971e266af7288/README.md) · [LICENSE](https://github.com/ImageMagick/ImageMagick/blob/3eeefb9633286904621822e9721971e266af7288/LICENSE) · [metadata GitHub](https://api.github.com/repos/ImageMagick/ImageMagick).

<a id="anhkysuai-chartjs-chart-js"></a>

### Chart.js

- **Repo:** [chartjs/Chart.js](https://github.com/chartjs/Chart.js).
- **Mục đích:** Thư viện biểu đồ JavaScript dựng bằng canvas cho dashboard web.
- **Điểm đáng dùng:** Manifest có đầu ra ESM, CommonJS, bản UMD, kiểu TypeScript và các entry auto/helpers; phù hợp nhúng biểu đồ vào nhiều hệ build.
- **License:** MIT.
- **Giới hạn:** Canvas cần lớp văn bản hoặc bảng dữ liệu bổ sung khi yêu cầu truy cập bằng screen reader; chưa đo hiệu năng, độ chính xác đồ thị hay hành vi trình duyệt.
- **Tích hợp:** Cài chart.js, ghim phiên bản và chọn entry phù hợp hệ module; cung cấp dữ liệu và cấu hình trục rõ ràng.
- **Đối chiếu:** Apache ECharts cho nhiều loại biểu đồ; [D3](../08-awesome-lists-learning/README.md#6c527-đồ-họa-3d--sơ-đồ) cho tùy biến mức thấp; Recharts cho API component React.
- **Mức kiểm chứng:** `docs-read` — Đọc các phần mô tả và giới hạn trong README, thông báo license, metadata manifest và cấu hình CI khi có; chưa đọc toàn bộ mã triển khai, chưa cài hoặc chạy kiểm thử upstream.
- **Snapshot:** kiểm ngày 2026-11-23; commit `ff1bdc38a102e7b9e97756041b1118272ed08564` (2026-11-23T07:08:46+02:00); 67,820 sao theo GitHub API ngày 2026-11-23. Sao không đại diện chất lượng.
- **Bằng chứng:** [README.md](https://github.com/chartjs/Chart.js/blob/ff1bdc38a102e7b9e97756041b1118272ed08564/README.md) · [LICENSE.md](https://github.com/chartjs/Chart.js/blob/ff1bdc38a102e7b9e97756041b1118272ed08564/LICENSE.md) · [package.json](https://github.com/chartjs/Chart.js/blob/ff1bdc38a102e7b9e97756041b1118272ed08564/package.json) · [composer.json](https://github.com/chartjs/Chart.js/blob/ff1bdc38a102e7b9e97756041b1118272ed08564/composer.json) · [.github/workflows/ci.yml](https://github.com/chartjs/Chart.js/blob/ff1bdc38a102e7b9e97756041b1118272ed08564/.github/workflows/ci.yml) · [GitHub API](https://api.github.com/repos/chartjs/Chart.js).

<a id="anhkysuai-ryanoasis-nerd-fonts"></a>

### Nerd Fonts

**Đã chuyển (2026-11-23):** hồ sơ này nay nằm ở [mục 13](../13-dev-stack-devops/README.md#anhkysuai-ryanoasis-nerd-fonts); catalog con xem [catalog/](../catalog/README.md).

<a id="anhkysuai-pmndrs-zustand"></a>

### Zustand

- **Repo:** [pmndrs/zustand](https://github.com/pmndrs/zustand).
- **Mục đích:** Quản lý trạng thái React bằng store và hook với API nhỏ.
- **Điểm đáng dùng:** README mô tả selector theo phần state, cập nhật bất biến và set có merge; manifest tách vanilla, React và middleware, CI chạy types, lint, spec và build.
- **License:** MIT.
- **Giới hạn:** Không suy từ lời tác giả rằng mọi lỗi concurrency đều đã được giải quyết; hydration, state chia sẻ và dữ liệu persist cần kiểm theo ứng dụng.
- **Tích hợp:** Cài zustand, tách store theo miền và dùng selector nhỏ; kiểm vòng đời store khi SSR hoặc nhiều phiên người dùng.
- **Đối chiếu:** Redux Toolkit cho quy ước chặt; Jotai cho atom; React Context cho state đơn giản.
- **Mức kiểm chứng:** `docs-read` — Đọc các phần mô tả và giới hạn trong README, thông báo license, metadata manifest và cấu hình CI khi có; chưa đọc toàn bộ mã triển khai, chưa cài hoặc chạy kiểm thử upstream.
- **Snapshot:** kiểm ngày 2026-11-23; commit `5d66d53be80363b94491868b41325ea058fd16bb` (2026-11-23T09:21:45+09:00); 58,986 sao theo GitHub API ngày 2026-11-23. Sao không đại diện chất lượng.
- **Bằng chứng:** [README.md](https://github.com/pmndrs/zustand/blob/5d66d53be80363b94491868b41325ea058fd16bb/README.md) · [LICENSE](https://github.com/pmndrs/zustand/blob/5d66d53be80363b94491868b41325ea058fd16bb/LICENSE) · [package.json](https://github.com/pmndrs/zustand/blob/5d66d53be80363b94491868b41325ea058fd16bb/package.json) · [.github/workflows/test.yml](https://github.com/pmndrs/zustand/blob/5d66d53be80363b94491868b41325ea058fd16bb/.github/workflows/test.yml) · [GitHub API](https://api.github.com/repos/pmndrs/zustand).

<a id="anhkysuai-h5bp-html5-boilerplate"></a>

### HTML5 Boilerplate

- **Repo:** [h5bp/html5-boilerplate](https://github.com/h5bp/html5-boilerplate).
- **Mục đích:** Bộ khởi đầu HTML/CSS/JavaScript không ép framework.
- **Điểm đáng dùng:** README phân biệt rõ dist được phát hành với Gulp và công cụ chỉ phục vụ xây template; CI kiểm bản archive, giúp tham khảo hợp đồng giữa nguồn và sản phẩm mẫu.
- **License:** MIT.
- **Giới hạn:** Không nên sao chép toàn repo tác giả vào app mới; cấu hình nền không thay kiểm accessibility, bảo mật hay hiệu năng thực tế.
- **Tích hợp:** Lấy package hoặc generator phát hành rồi giữ phần cần dùng; kiểm yêu cầu Node của công cụ đi kèm.
- **Đối chiếu:** Vite template cho app hiện đại; [Astro](../13-dev-stack-devops/README.md) cho nội dung; khung HTML tối giản cho trang nhỏ.
- **Mức kiểm chứng:** `docs-read` — Đọc các phần mô tả và giới hạn trong README, thông báo license, metadata manifest và cấu hình CI khi có; chưa đọc toàn bộ mã triển khai, chưa cài hoặc chạy kiểm thử upstream.
- **Snapshot:** kiểm ngày 2026-11-23; commit `7fa0bd6c9e6818d11a1a7efad56fe715ae56d848` (2026-11-17T12:08:59-05:00); 57,701 sao theo GitHub API ngày 2026-11-23. Sao không đại diện chất lượng.
- **Bằng chứng:** [README.md](https://github.com/h5bp/html5-boilerplate/blob/7fa0bd6c9e6818d11a1a7efad56fe715ae56d848/README.md) · [LICENSE.txt](https://github.com/h5bp/html5-boilerplate/blob/7fa0bd6c9e6818d11a1a7efad56fe715ae56d848/LICENSE.txt) · [package.json](https://github.com/h5bp/html5-boilerplate/blob/7fa0bd6c9e6818d11a1a7efad56fe715ae56d848/package.json) · [.github/workflows/test.yml](https://github.com/h5bp/html5-boilerplate/blob/7fa0bd6c9e6818d11a1a7efad56fe715ae56d848/.github/workflows/test.yml) · [GitHub API](https://api.github.com/repos/h5bp/html5-boilerplate).

<a id="anhkysuai-gatsbyjs-gatsby"></a>

### Gatsby

- **Repo:** [gatsbyjs/gatsby](https://github.com/gatsbyjs/gatsby).
- **Mục đích:** Framework React cho website nội dung, kết hợp nạp dữ liệu và nhiều chế độ render.
- **Điểm đáng dùng:** README nêu source plugin và lớp GraphQL chung, cùng SSG, DSG và SSR theo trang; hữu ích khi dữ liệu tới từ CMS, Markdown và API khác nhau.
- **License:** MIT.
- **Giới hạn:** SSR và DSG cần nền tảng vận hành phù hợp, không thể suy mọi site chỉ cần CDN; claim hiệu năng mặc định chưa được tái lập, plugin cần đánh giá riêng.
- **Tích hợp:** Chọn starter và source plugin tối thiểu, ghim runtime theo manifest và kiểm pipeline build với dữ liệu thật.
- **Đối chiếu:** [Astro](../13-dev-stack-devops/README.md) cho nội dung nhẹ; [Next.js](../13-dev-stack-devops/README.md) cho React full stack; [Hugo](../08-awesome-lists-learning/README.md#6c59-framework-backend) cho sinh tĩnh ít phụ thuộc.
- **Mức kiểm chứng:** `docs-read` — Đọc các phần mô tả và giới hạn trong README, thông báo license, metadata manifest và cấu hình CI khi có; chưa đọc toàn bộ mã triển khai, chưa cài hoặc chạy kiểm thử upstream.
- **Snapshot:** kiểm ngày 2026-11-23; commit `0ac6c88a72c4dfd4d541e3ac43c664343e8e15b6` (2026-11-09T11:28:50-05:00); 55,916 sao theo GitHub API ngày 2026-11-23. Sao không đại diện chất lượng.
- **Bằng chứng:** [README.md](https://github.com/gatsbyjs/gatsby/blob/0ac6c88a72c4dfd4d541e3ac43c664343e8e15b6/README.md) · [LICENSE](https://github.com/gatsbyjs/gatsby/blob/0ac6c88a72c4dfd4d541e3ac43c664343e8e15b6/LICENSE) · [package.json](https://github.com/gatsbyjs/gatsby/blob/0ac6c88a72c4dfd4d541e3ac43c664343e8e15b6/package.json) · [.github/workflows/schedule-stale.yml](https://github.com/gatsbyjs/gatsby/blob/0ac6c88a72c4dfd4d541e3ac43c664343e8e15b6/.github/workflows/schedule-stale.yml) · [GitHub API](https://api.github.com/repos/gatsbyjs/gatsby).

<a id="anhkysuai-chenglou-pretext"></a>

### Pretext

- **Repo:** [chenglou/pretext](https://github.com/chenglou/pretext).
- **Mục đích:** Đo và bố trí văn bản nhiều dòng bằng JavaScript/TypeScript, hỗ trợ render DOM, canvas hoặc SVG.
- **Điểm đáng dùng:** README tách prepare để phân đoạn, đo font bằng canvas khỏi layout chỉ tính trên width cache; có giá trị cho virtualization và UI chat thay vì đo DOM mỗi lần resize.
- **License:** MIT.
- **Giới hạn:** Font và tùy chọn phải đồng bộ với phần render; không được suy mọi ngôn ngữ hay layout chính xác từ claim của tác giả, chưa tái lập benchmark.
- **Tích hợp:** Tái dùng handle prepare cho cùng văn bản/font, chỉ gọi layout khi đổi chiều rộng và kiểm font tải hoàn tất.
- **Đối chiếu:** Đo DOM trực tiếp cho chính xác theo browser; Canvas measureText cho nhu cầu đơn giản; CSS layout khi không cần biết kích thước trước.
- **Mức kiểm chứng:** `docs-read` — Đọc các phần mô tả và giới hạn trong README, thông báo license, metadata manifest và cấu hình CI khi có; chưa đọc toàn bộ mã triển khai, chưa cài hoặc chạy kiểm thử upstream.
- **Snapshot:** kiểm ngày 2026-11-23; commit `6ed1edd294698374ab2fb0d3eb36276527084879` (2026-11-18T17:44:50-08:00); 51,092 sao theo GitHub API ngày 2026-11-23. Sao không đại diện chất lượng.
- **Bằng chứng:** [README.md](https://github.com/chenglou/pretext/blob/6ed1edd294698374ab2fb0d3eb36276527084879/README.md) · [LICENSE](https://github.com/chenglou/pretext/blob/6ed1edd294698374ab2fb0d3eb36276527084879/LICENSE) · [package.json](https://github.com/chenglou/pretext/blob/6ed1edd294698374ab2fb0d3eb36276527084879/package.json) · [.github/workflows/pages.yml](https://github.com/chenglou/pretext/blob/6ed1edd294698374ab2fb0d3eb36276527084879/.github/workflows/pages.yml) · [GitHub API](https://api.github.com/repos/chenglou/pretext).

<a id="anhkysuai-jgthms-bulma"></a>

### Bulma

- **Repo:** [jgthms/bulma](https://github.com/jgthms/bulma).
- **Mục đích:** Framework CSS dựa trên Flexbox, cung cấp lớp giao diện không kèm JavaScript.
- **Điểm đáng dùng:** README tách CSS biên dịch sẵn khỏi Sass để tùy biến; không áp đặt framework logic, phù hợp trang nội dung hoặc dashboard có stack sẵn.
- **License:** MIT.
- **Giới hạn:** Tương tác như menu, modal và accessibility phải được triển khai riêng; không suy tên workflow e2e thành kiểm đầy đủ vì đoạn Cypress đã đọc có phần bị comment.
- **Tích hợp:** Cài bulma hoặc nhập CSS/Sass, quản lý token riêng và kiểm hành vi tương tác trên browser mục tiêu.
- **Đối chiếu:** [Bootstrap](../08-awesome-lists-learning/README.md#6c522-thư-viện-giao-diện--css) cho bộ CSS/JS; [Tailwind CSS](../13-dev-stack-devops/README.md) cho utility; Pico CSS cho giao diện nhẹ.
- **Mức kiểm chứng:** `docs-read` — Đọc các phần mô tả và giới hạn trong README, thông báo license, metadata manifest và cấu hình CI khi có; chưa đọc toàn bộ mã triển khai, chưa cài hoặc chạy kiểm thử upstream.
- **Snapshot:** kiểm ngày 2026-11-23; commit `c5cd04baf0258cfcc77b4e8610488a0d439effa2` (2026-09-21T10:56:01+01:00); 50,036 sao theo GitHub API ngày 2026-11-23. Sao không đại diện chất lượng.
- **Bằng chứng:** [README.md](https://github.com/jgthms/bulma/blob/c5cd04baf0258cfcc77b4e8610488a0d439effa2/README.md) · [LICENSE](https://github.com/jgthms/bulma/blob/c5cd04baf0258cfcc77b4e8610488a0d439effa2/LICENSE) · [package.json](https://github.com/jgthms/bulma/blob/c5cd04baf0258cfcc77b4e8610488a0d439effa2/package.json) · [.github/workflows/main.yml](https://github.com/jgthms/bulma/blob/c5cd04baf0258cfcc77b4e8610488a0d439effa2/.github/workflows/main.yml) · [GitHub API](https://api.github.com/repos/jgthms/bulma).

<a id="anhkysuai-bigskysoftware-htmx"></a>

### htmx

- **Repo:** [bigskysoftware/htmx](https://github.com/bigskysoftware/htmx).
- **Mục đích:** Bổ sung tương tác HTTP và cập nhật từng phần giao diện thông qua thuộc tính HTML.
- **Điểm đáng dùng:** README mô tả hx-post/hx-swap, dependency ít và bộ kiểm theo thuộc tính/core/extension; phù hợp ứng dụng server render muốn giảm JavaScript phía client.
- **License:** 0BSD.
- **Giới hạn:** HTML trả về vẫn cần escape và kiểm quyền; mô hình này không tự thay state phức tạp của SPA. Hiệu năng hay kích thước quảng bá chưa đo lại.
- **Tích hợp:** Dùng package htmx.org, trả fragment HTML có hợp đồng rõ và kiểm lịch sử, lỗi mạng, CSRF.
- **Đối chiếu:** Turbo cho điều hướng HTML; Alpine.js cho tương tác cục bộ; React cho state UI phức tạp.
- **Mức kiểm chứng:** `docs-read` — Đọc các phần mô tả và giới hạn trong README, thông báo license, metadata manifest và cấu hình CI khi có; chưa đọc toàn bộ mã triển khai, chưa cài hoặc chạy kiểm thử upstream.
- **Snapshot:** kiểm ngày 2026-11-23; commit `51c3e67bcedc5568b2a968b079888f13aedf4eb7` (2026-11-18T10:01:49-07:00); 49,655 sao theo GitHub API ngày 2026-11-23. Sao không đại diện chất lượng.
- **Bằng chứng:** [README.md](https://github.com/bigskysoftware/htmx/blob/51c3e67bcedc5568b2a968b079888f13aedf4eb7/README.md) · [LICENSE](https://github.com/bigskysoftware/htmx/blob/51c3e67bcedc5568b2a968b079888f13aedf4eb7/LICENSE) · [package.json](https://github.com/bigskysoftware/htmx/blob/51c3e67bcedc5568b2a968b079888f13aedf4eb7/package.json) · [.github/workflows/ci.yml](https://github.com/bigskysoftware/htmx/blob/51c3e67bcedc5568b2a968b079888f13aedf4eb7/.github/workflows/ci.yml) · [GitHub API](https://api.github.com/repos/bigskysoftware/htmx).

<a id="anhkysuai-microsoft-monaco-editor"></a>

### Monaco Editor

- **Repo:** [microsoft/monaco-editor](https://github.com/microsoft/monaco-editor).
- **Mục đích:** Editor mã nhúng trong trình duyệt, tách model văn bản và view.
- **Điểm đáng dùng:** README giải thích model có URI duy nhất, editor gắn vào DOM và monaco.d.ts là API được version; phù hợp thiết kế editor trong workspace AI.
- **License:** MIT.
- **Giới hạn:** Build AMD bị đánh dấu deprecated; API nội bộ ngoài hợp đồng có thể đổi. Phải dispose model/editor để giải phóng tài nguyên; không mặc nhiên chạy được extension VS Code.
- **Tích hợp:** Dùng ESM, quản lý URI/model theo file và cấu hình worker ngôn ngữ theo bundler.
- **Đối chiếu:** CodeMirror cho editor module; Ace cho editor web lâu đời; VS Code Web khi cần IDE rộng hơn.
- **Mức kiểm chứng:** `docs-read` — Đọc các phần mô tả và giới hạn trong README, thông báo license, metadata manifest và cấu hình CI khi có; chưa đọc toàn bộ mã triển khai, chưa cài hoặc chạy kiểm thử upstream.
- **Snapshot:** kiểm ngày 2026-11-23; commit `ba7a57d4757f03ad92bd62963268faa86b2ff1ab` (2026-11-21T18:11:43+01:00); 47,000 sao theo GitHub API ngày 2026-11-23. Sao không đại diện chất lượng.
- **Bằng chứng:** [README.md](https://github.com/microsoft/monaco-editor/blob/ba7a57d4757f03ad92bd62963268faa86b2ff1ab/README.md) · [LICENSE.txt](https://github.com/microsoft/monaco-editor/blob/ba7a57d4757f03ad92bd62963268faa86b2ff1ab/LICENSE.txt) · [package.json](https://github.com/microsoft/monaco-editor/blob/ba7a57d4757f03ad92bd62963268faa86b2ff1ab/package.json) · [.github/workflows/ci.yml](https://github.com/microsoft/monaco-editor/blob/ba7a57d4757f03ad92bd62963268faa86b2ff1ab/.github/workflows/ci.yml) · [GitHub API](https://api.github.com/repos/microsoft/monaco-editor).

<a id="anhkysuai-leaflet-leaflet"></a>

### Leaflet

- **Repo:** [Leaflet/Leaflet](https://github.com/Leaflet/Leaflet).
- **Mục đích:** Thư viện JavaScript dựng bản đồ tương tác trên web và thiết bị di động.
- **Điểm đáng dùng:** README nêu API và hệ plugin, CI có typecheck/build/test types; manifest snapshot là 2.0.0-beta.5 nên dữ liệu đánh giá gắn đúng nhánh thử nghiệm.
- **License:** BSD-2-Clause.
- **Giới hạn:** License thư viện không cấp quyền tile hoặc dữ liệu bản đồ; cần theo điều khoản nhà cung cấp. Chưa kiểm hiệu năng với nhiều điểm hay plugin.
- **Tích hợp:** Chọn release phù hợp, cấp tile URL/attribution và kiểm tương thích plugin khi chuyển major.
- **Đối chiếu:** MapLibre GL JS cho bản đồ vector; OpenLayers cho GIS phong phú; CesiumJS cho địa cầu 3D.
- **Mức kiểm chứng:** `docs-read` — Đọc các phần mô tả và giới hạn trong README, thông báo license, metadata manifest và cấu hình CI khi có; chưa đọc toàn bộ mã triển khai, chưa cài hoặc chạy kiểm thử upstream.
- **Snapshot:** kiểm ngày 2026-11-23; commit `6d5b3bea118afe0f158c16688abc117b2627848a` (2026-11-22T21:09:20+02:00); 45,972 sao theo GitHub API ngày 2026-11-23. Sao không đại diện chất lượng.
- **Bằng chứng:** [README.md](https://github.com/Leaflet/Leaflet/blob/6d5b3bea118afe0f158c16688abc117b2627848a/README.md) · [LICENSE](https://github.com/Leaflet/Leaflet/blob/6d5b3bea118afe0f158c16688abc117b2627848a/LICENSE) · [package.json](https://github.com/Leaflet/Leaflet/blob/6d5b3bea118afe0f158c16688abc117b2627848a/package.json) · [.github/workflows/main.yml](https://github.com/Leaflet/Leaflet/blob/6d5b3bea118afe0f158c16688abc117b2627848a/.github/workflows/main.yml) · [GitHub API](https://api.github.com/repos/Leaflet/Leaflet).

<a id="anhkysuai-charmbracelet-bubbletea"></a>

### Bubble Tea

- **Repo:** [charmbracelet/bubbletea](https://github.com/charmbracelet/bubbletea).
- **Mục đích:** Framework TUI Go theo mô hình state, event và view.
- **Điểm đáng dùng:** README trình bày Init/Update/View và Cmd cho I/O; module charm.land/bubbletea/v2 giúp tham khảo cách tách cập nhật trạng thái khỏi hiệu ứng bên ngoài.
- **License:** MIT.
- **Giới hạn:** V2 có hướng dẫn nâng cấp riêng; keyboard, clipboard và render phụ thuộc terminal. Chưa chạy để xác minh độ trễ hay mọi client.
- **Tích hợp:** Dùng module v2, giữ Update dễ kiểm và đưa I/O vào command, ghép Bubbles khi cần component.
- **Đối chiếu:** [Textual](../06-ui-ux-design/README.md#anhkysuai-textualize-textual) cho Python; Ratatui cho Rust; [Ink](../06-ui-ux-design/README.md#anhkysuai-vadimdemedes-ink) cho React trong terminal.
- **Mức kiểm chứng:** `docs-read` — Đọc các phần mô tả và giới hạn trong README, thông báo license, metadata manifest và cấu hình CI khi có; chưa đọc toàn bộ mã triển khai, chưa cài hoặc chạy kiểm thử upstream.
- **Snapshot:** kiểm ngày 2026-11-23; commit `585149e50e7c3f1002db5d0fc3912c44bbc6ef92` (2026-11-20T19:01:53+04:00); 45,843 sao theo GitHub API ngày 2026-11-23. Sao không đại diện chất lượng.
- **Bằng chứng:** [README.md](https://github.com/charmbracelet/bubbletea/blob/585149e50e7c3f1002db5d0fc3912c44bbc6ef92/README.md) · [LICENSE](https://github.com/charmbracelet/bubbletea/blob/585149e50e7c3f1002db5d0fc3912c44bbc6ef92/LICENSE) · [go.mod](https://github.com/charmbracelet/bubbletea/blob/585149e50e7c3f1002db5d0fc3912c44bbc6ef92/go.mod) · [.github/workflows/build.yml](https://github.com/charmbracelet/bubbletea/blob/585149e50e7c3f1002db5d0fc3912c44bbc6ef92/.github/workflows/build.yml) · [GitHub API](https://api.github.com/repos/charmbracelet/bubbletea).

<a id="anhkysuai-colorlibhq-adminlte"></a>

### AdminLTE

- **Repo:** [ColorlibHQ/AdminLTE](https://github.com/ColorlibHQ/AdminLTE).
- **Mục đích:** Mẫu bảng quản trị Bootstrap 5.3, JavaScript thuần cho các màn hình vận hành.
- **Điểm đáng dùng:** Tài liệu phân biệt bản HTML cốt lõi với các repo tích hợp React, Vue, Laravel; CI có kiểm tra kiểu và Playwright.
- **License:** MIT; ảnh và thư viện demo có điều khoản riêng.
- **Giới hạn:** Không xem các edition framework là nội dung có sẵn trong repo này; composer mô tả Bootstrap 4 đã lệch README, cần theo bản phân phối đã khóa.
- **Tích hợp:** Tách layout, menu và token màu thành mẫu XTemplates, gắn quyền truy cập và API của sản phẩm riêng.
- **Đối chiếu:** [Tabler](../06-ui-ux-design/README.md#anhkysuai-tabler-tabler) cho dashboard Bootstrap; [shadcn/ui](../06-ui-ux-design/README.md) cho thành phần React; [Ant Design](../06-ui-ux-design/README.md) cho ứng dụng nghiệp vụ.
- **Mức kiểm chứng:** `docs-read` — Đọc các phần mô tả và giới hạn trong README, thông báo license, metadata manifest và cấu hình CI khi có; chưa đọc toàn bộ mã triển khai, chưa cài hoặc chạy kiểm thử upstream.
- **Snapshot:** kiểm ngày 2026-11-23; commit `7cf90cb0a72758c7b9f049d07696d0a81966fdc5` (2026-11-19T19:46:47+02:00); 45,706 sao theo GitHub API ngày 2026-11-23. Sao không đại diện chất lượng.
- **Bằng chứng:** [README.md](https://github.com/ColorlibHQ/AdminLTE/blob/7cf90cb0a72758c7b9f049d07696d0a81966fdc5/README.md) · [LICENSE](https://github.com/ColorlibHQ/AdminLTE/blob/7cf90cb0a72758c7b9f049d07696d0a81966fdc5/LICENSE) · [package.json](https://github.com/ColorlibHQ/AdminLTE/blob/7cf90cb0a72758c7b9f049d07696d0a81966fdc5/package.json) · [composer.json](https://github.com/ColorlibHQ/AdminLTE/blob/7cf90cb0a72758c7b9f049d07696d0a81966fdc5/composer.json) · [.github/workflows/tests.yml](https://github.com/ColorlibHQ/AdminLTE/blob/7cf90cb0a72758c7b9f049d07696d0a81966fdc5/.github/workflows/tests.yml) · [GitHub API](https://api.github.com/repos/ColorlibHQ/AdminLTE).

<a id="anhkysuai-tabler-tabler"></a>

### Tabler

- **Repo:** [tabler/tabler](https://github.com/tabler/tabler).
- **Mục đích:** UI kit dashboard Bootstrap 5 với layout và trang demo sẵn.
- **Điểm đáng dùng:** Sass/CSS custom properties, dark mode, RTL và stylesheet tách phần giúp dựng nhiều biến thể giao diện.
- **License:** MIT cho Tabler; plugin phân phối kèm có license riêng.
- **Giới hạn:** dist/libs có thư viện bên thứ ba: README cảnh báo ApexCharts từ v5 dùng điều khoản riêng, không được xem toàn bundle là MIT.
- **Tích hợp:** Chọn thành phần cần dùng, kiểm kê license từng plugin và tách demo assets trước khi đóng gói mẫu thương mại.
- **Đối chiếu:** [AdminLTE](../06-ui-ux-design/README.md#anhkysuai-colorlibhq-adminlte) cho dashboard Bootstrap; [Ant Design](../06-ui-ux-design/README.md) cho React; [shadcn/ui](../06-ui-ux-design/README.md) cho thành phần tùy biến.
- **Mức kiểm chứng:** `docs-read` — Đọc các phần mô tả và giới hạn trong README, thông báo license, metadata manifest và cấu hình CI khi có; chưa đọc toàn bộ mã triển khai, chưa cài hoặc chạy kiểm thử upstream.
- **Snapshot:** kiểm ngày 2026-11-23; commit `68c81fc9767f679eb3a0f312b79d80435d99e7f7` (2026-11-21T10:42:17+01:00); 42,119 sao theo GitHub API ngày 2026-11-23. Sao không đại diện chất lượng.
- **Bằng chứng:** [README.md](https://github.com/tabler/tabler/blob/68c81fc9767f679eb3a0f312b79d80435d99e7f7/README.md) · [LICENSE](https://github.com/tabler/tabler/blob/68c81fc9767f679eb3a0f312b79d80435d99e7f7/LICENSE) · [package.json](https://github.com/tabler/tabler/blob/68c81fc9767f679eb3a0f312b79d80435d99e7f7/package.json) · [.github/workflows/build.yml](https://github.com/tabler/tabler/blob/68c81fc9767f679eb3a0f312b79d80435d99e7f7/.github/workflows/build.yml) · [GitHub API](https://api.github.com/repos/tabler/tabler).

<a id="anhkysuai-styled-components-styled-components"></a>

### styled-components

- **Repo:** [styled-components/styled-components](https://github.com/styled-components/styled-components).
- **Mục đích:** CSS theo component React với kiểu TypeScript và style phụ thuộc props.
- **Điểm đáng dùng:** README package minh họa transient prop tiền tố $, biến thể component và StyleSheetManager; vendor prefix mặc định tắt và bật bằng plugin.
- **License:** MIT.
- **Giới hạn:** Phải kiểm tra SSR/CSP và browser target; không áp dụng tự động hướng dẫn cũ về prefix cho snapshot này, nguồn bảo trì tập trung ít người.
- **Tích hợp:** Gắn token theme vào component, tránh truyền props nội bộ ra DOM và kiểm tra thứ tự CSS khi streaming SSR.
- **Đối chiếu:** [Tailwind CSS](../13-dev-stack-devops/README.md) cho utility; CSS Modules cho scope tĩnh; Emotion cho CSS-in-JS.
- **Mức kiểm chứng:** `docs-read` — Đọc các phần mô tả và giới hạn trong README, thông báo license, metadata manifest và cấu hình CI khi có; chưa đọc toàn bộ mã triển khai, chưa cài hoặc chạy kiểm thử upstream.
- **Snapshot:** kiểm ngày 2026-11-23; commit `e2aa1c8f6e40b74ae164e7489f68067019d47772` (2026-11-10T00:30:36-05:00); 41,061 sao theo GitHub API ngày 2026-11-23. Sao không đại diện chất lượng.
- **Bằng chứng:** [README.md](https://github.com/styled-components/styled-components/blob/e2aa1c8f6e40b74ae164e7489f68067019d47772/README.md) · [LICENSE](https://github.com/styled-components/styled-components/blob/e2aa1c8f6e40b74ae164e7489f68067019d47772/LICENSE) · [package.json](https://github.com/styled-components/styled-components/blob/e2aa1c8f6e40b74ae164e7489f68067019d47772/package.json) · [.github/workflows/test.yml](https://github.com/styled-components/styled-components/blob/e2aa1c8f6e40b74ae164e7489f68067019d47772/.github/workflows/test.yml) · [packages/styled-components/README.md](https://github.com/styled-components/styled-components/blob/e2aa1c8f6e40b74ae164e7489f68067019d47772/packages/styled-components/README.md) · [packages/styled-components/package.json](https://github.com/styled-components/styled-components/blob/e2aa1c8f6e40b74ae164e7489f68067019d47772/packages/styled-components/package.json) · [GitHub API](https://api.github.com/repos/styled-components/styled-components).

<a id="anhkysuai-phaserjs-phaser"></a>

### Phaser

- **Repo:** [phaserjs/phaser](https://github.com/phaserjs/phaser).
- **Mục đích:** Framework game HTML5 với WebGL/Canvas, dùng JavaScript hoặc TypeScript.
- **Điểm đáng dùng:** README chỉ ra template cho nhiều framework/bundler và khả năng tinh giảm build; gói đọc mang phiên bản 4.2.1.
- **License:** MIT.
- **Giới hạn:** Đóng gói native cần công cụ bên thứ ba; kích thước bundle và tốc độ là công bố tài liệu, chưa đo trên thiết bị mục tiêu. Workflow đã đọc chỉ quản lý thảo luận.
- **Tích hợp:** Dùng cho mẫu game web, tách asset có license riêng và kiểm tra input, âm thanh, bộ nhớ trên mobile.
- **Đối chiếu:** PixiJS cho rendering 2D; [Bevy](../13-dev-stack-devops/README.md#anhkysuai-bevyengine-bevy) cho game Rust; [raylib](../06-ui-ux-design/README.md#anhkysuai-raysan5-raylib) cho thư viện native.
- **Mức kiểm chứng:** `docs-read` — Đọc các phần mô tả và giới hạn trong README, thông báo license, metadata manifest và cấu hình CI khi có; chưa đọc toàn bộ mã triển khai, chưa cài hoặc chạy kiểm thử upstream.
- **Snapshot:** kiểm ngày 2026-11-23; commit `02d8931b626d9764c133cbb3fbf99966c03c757c` (2026-08-21T18:04:38+12:00); 40,774 sao theo GitHub API ngày 2026-11-23. Sao không đại diện chất lượng.
- **Bằng chứng:** [README.md](https://github.com/phaserjs/phaser/blob/02d8931b626d9764c133cbb3fbf99966c03c757c/README.md) · [LICENSE.md](https://github.com/phaserjs/phaser/blob/02d8931b626d9764c133cbb3fbf99966c03c757c/LICENSE.md) · [package.json](https://github.com/phaserjs/phaser/blob/02d8931b626d9764c133cbb3fbf99966c03c757c/package.json) · [.github/workflows/lock-comments.yml](https://github.com/phaserjs/phaser/blob/02d8931b626d9764c133cbb3fbf99966c03c757c/.github/workflows/lock-comments.yml) · [GitHub API](https://api.github.com/repos/phaserjs/phaser).

<a id="anhkysuai-vadimdemedes-ink"></a>

### Ink

- **Repo:** [vadimdemedes/ink](https://github.com/vadimdemedes/ink).
- **Mục đích:** Renderer React cho giao diện terminal.
- **Điểm đáng dùng:** Dùng Yoga để bố trí Flexbox và mô hình component React; manifest bản 8 yêu cầu Node >=22, React >=19.3.
- **License:** MIT.
- **Giới hạn:** README nói đang mô tả phiên bản sắp phát hành; terminal khác trình duyệt về layout, input và accessibility, cần kiểm tra riêng.
- **Tích hợp:** Dùng cho CLI của xưởng phần mềm khi đã có React, bổ sung chế độ không tương tác và đầu ra JSON cho pipeline.
- **Đối chiếu:** [Bubble Tea](../06-ui-ux-design/README.md#anhkysuai-charmbracelet-bubbletea) cho Go; [Textual](../06-ui-ux-design/README.md#anhkysuai-textualize-textual) cho Python; [Rich](../13-dev-stack-devops/README.md#anhkysuai-textualize-rich) cho in thông tin có định dạng.
- **Mức kiểm chứng:** `docs-read` — Đọc các phần mô tả và giới hạn trong README, thông báo license, metadata manifest và cấu hình CI khi có; chưa đọc toàn bộ mã triển khai, chưa cài hoặc chạy kiểm thử upstream.
- **Snapshot:** kiểm ngày 2026-11-23; commit `2a885845648d70564a8722bf06bd38802614740f` (2026-11-22T00:18:44+07:00); 40,317 sao theo GitHub API ngày 2026-11-23. Sao không đại diện chất lượng.
- **Bằng chứng:** [readme.md](https://github.com/vadimdemedes/ink/blob/2a885845648d70564a8722bf06bd38802614740f/readme.md) · [license](https://github.com/vadimdemedes/ink/blob/2a885845648d70564a8722bf06bd38802614740f/license) · [package.json](https://github.com/vadimdemedes/ink/blob/2a885845648d70564a8722bf06bd38802614740f/package.json) · [.github/workflows/test.yml](https://github.com/vadimdemedes/ink/blob/2a885845648d70564a8722bf06bd38802614740f/.github/workflows/test.yml) · [GitHub API](https://api.github.com/repos/vadimdemedes/ink).

<a id="anhkysuai-videojs-video-js"></a>

### Video.js

- **Repo:** [videojs/video.js](https://github.com/videojs/video.js).
- **Mục đích:** Framework media player mô-đun cho Web và React.
- **Điểm đáng dùng:** README tại SHA xác nhận nhánh v10 stable, monorepo có bước chọn package tests theo thay đổi; manifest công cụ yêu cầu Node >=22.22.
- **License:** Apache-2.0.
- **Giới hạn:** Đây là v10, không áp dụng mặc định hướng dẫn/plugin v8; codec, nguồn video và DRM có hỗ trợ/điều khoản riêng.
- **Tích hợp:** Khóa phiên bản player cùng plugin, kiểm tra caption, bàn phím và nguồn stream thực tế trên browser mục tiêu.
- **Đối chiếu:** [Plyr](../06-ui-ux-design/README.md#anhkysuai-sampotts-plyr) cho giao diện media gọn; Shaka Player cho streaming; phần tử video HTML cho nhu cầu cơ bản.
- **Mức kiểm chứng:** `docs-read` — Đọc các phần mô tả và giới hạn trong README, thông báo license, metadata manifest và cấu hình CI khi có; chưa đọc toàn bộ mã triển khai, chưa cài hoặc chạy kiểm thử upstream.
- **Snapshot:** kiểm ngày 2026-11-23; commit `fd24318727bbeba0e0d2a34d5feb161132adaec4` (2026-11-23T12:51:14+11:00); 40,239 sao theo GitHub API ngày 2026-11-23. Sao không đại diện chất lượng.
- **Bằng chứng:** [README.md](https://github.com/videojs/video.js/blob/fd24318727bbeba0e0d2a34d5feb161132adaec4/README.md) · [LICENSE](https://github.com/videojs/video.js/blob/fd24318727bbeba0e0d2a34d5feb161132adaec4/LICENSE) · [package.json](https://github.com/videojs/video.js/blob/fd24318727bbeba0e0d2a34d5feb161132adaec4/package.json) · [.github/workflows/ci.yml](https://github.com/videojs/video.js/blob/fd24318727bbeba0e0d2a34d5feb161132adaec4/.github/workflows/ci.yml) · [GitHub API](https://api.github.com/repos/videojs/video.js).

<a id="anhkysuai-ueberdosis-tiptap"></a>

### Tiptap

- **Repo:** [ueberdosis/tiptap](https://github.com/ueberdosis/tiptap).
- **Mục đích:** Rich-text editor headless dựa trên ProseMirror.
- **Điểm đáng dùng:** Mô hình extension/node cho phép tự dựng UI; Hocuspocus là backend cộng tác Yjs riêng, workflow kiểm tra build và package exports.
- **License:** MIT cho editor mở; Pro Extensions và dịch vụ theo thuê bao.
- **Giới hạn:** Không có toolbar hoàn chỉnh mặc định; bình luận, chuyển đổi và các Pro Extension có điều kiện thuê bao, nội dung nhập cần xử lý an toàn.
- **Tích hợp:** Chốt schema tài liệu và extension tối thiểu, lưu JSON có version rồi kiểm tra paste, undo và cộng tác.
- **Đối chiếu:** Lexical cho editor React; [Slate](../06-ui-ux-design/README.md#anhkysuai-ianstormtaylor-slate) cho mô hình tự thiết kế; [Editor.js](../06-ui-ux-design/README.md#anhkysuai-codex-team-editor-js) cho block JSON.
- **Mức kiểm chứng:** `docs-read` — Đọc các phần mô tả và giới hạn trong README, thông báo license, metadata manifest và cấu hình CI khi có; chưa đọc toàn bộ mã triển khai, chưa cài hoặc chạy kiểm thử upstream.
- **Snapshot:** kiểm ngày 2026-11-23; commit `643792f65e8ea5506fc2591cfd140fc3aec6d29b` (2026-11-22T14:51:33+01:00); 39,117 sao theo GitHub API ngày 2026-11-23. Sao không đại diện chất lượng.
- **Bằng chứng:** [README.md](https://github.com/ueberdosis/tiptap/blob/643792f65e8ea5506fc2591cfd140fc3aec6d29b/README.md) · [LICENSE.md](https://github.com/ueberdosis/tiptap/blob/643792f65e8ea5506fc2591cfd140fc3aec6d29b/LICENSE.md) · [package.json](https://github.com/ueberdosis/tiptap/blob/643792f65e8ea5506fc2591cfd140fc3aec6d29b/package.json) · [.github/workflows/build.yml](https://github.com/ueberdosis/tiptap/blob/643792f65e8ea5506fc2591cfd140fc3aec6d29b/.github/workflows/build.yml) · [GitHub API](https://api.github.com/repos/ueberdosis/tiptap).

<a id="anhkysuai-preactjs-preact"></a>

### Preact

- **Repo:** [preactjs/preact](https://github.com/preactjs/preact).
- **Mục đích:** Thư viện UI Virtual DOM nhỏ với API component quen thuộc React.
- **Điểm đáng dùng:** README giải thích render diff cây và alias preact/compat; CI có kiểm tra kích thước, build/test và benchmark.
- **License:** MIT.
- **Giới hạn:** Tương thích qua compat không bảo đảm mọi thư viện React hoạt động; kích thước 4kB là mô tả tác giả, phụ thuộc bundle ứng dụng.
- **Tích hợp:** Dùng cho widget hoặc trang chú trọng tải nhẹ, thử dependency React và hydration trên bản đã khóa.
- **Đối chiếu:** React cho hệ sinh thái; [Solid](../06-ui-ux-design/README.md#anhkysuai-solidjs-solid) cho fine-grained reactivity; [Svelte](../13-dev-stack-devops/README.md) cho compiler UI.
- **Mức kiểm chứng:** `docs-read` — Đọc các phần mô tả và giới hạn trong README, thông báo license, metadata manifest và cấu hình CI khi có; chưa đọc toàn bộ mã triển khai, chưa cài hoặc chạy kiểm thử upstream.
- **Snapshot:** kiểm ngày 2026-11-23; commit `1fbc07f67bd841315332cac73de8ce1ae3e8b7b5` (2026-11-21T09:15:28+01:00); 39,015 sao theo GitHub API ngày 2026-11-23. Sao không đại diện chất lượng.
- **Bằng chứng:** [README.md](https://github.com/preactjs/preact/blob/1fbc07f67bd841315332cac73de8ce1ae3e8b7b5/README.md) · [LICENSE](https://github.com/preactjs/preact/blob/1fbc07f67bd841315332cac73de8ce1ae3e8b7b5/LICENSE) · [package.json](https://github.com/preactjs/preact/blob/1fbc07f67bd841315332cac73de8ce1ae3e8b7b5/package.json) · [.github/workflows/ci.yml](https://github.com/preactjs/preact/blob/1fbc07f67bd841315332cac73de8ce1ae3e8b7b5/.github/workflows/ci.yml) · [GitHub API](https://api.github.com/repos/preactjs/preact).

<a id="anhkysuai-ant-design-ant-design-pro"></a>

### Ant Design Pro

- **Repo:** [ant-design/ant-design-pro](https://github.com/ant-design/ant-design-pro).
- **Mục đích:** Boilerplate React cho ứng dụng doanh nghiệp có trang, theme và i18n.
- **Điểm đáng dùng:** Snapshot v6 kết hợp React 19, Umi Max 4, Ant Design 6; workflow có lint và tsc, template cung cấp mock API.
- **License:** MIT.
- **Giới hạn:** Lệnh chuyển sang simple version xóa vĩnh viễn nhiều trang/dependency; mock và AI chatbot demo chưa thành backend sản xuất.
- **Tích hợp:** Tách một bản mẫu có version, thay mock bằng hợp đồng API và nối auth/permission trước khi tái sử dụng.
- **Đối chiếu:** [React-admin](../06-ui-ux-design/README.md#anhkysuai-marmelab-react-admin) cho CRUD dữ liệu; [Refine](../06-ui-ux-design/README.md) cho headless admin; [Tabler](../06-ui-ux-design/README.md#anhkysuai-tabler-tabler) cho HTML dashboard.
- **Mức kiểm chứng:** `docs-read` — Đọc các phần mô tả và giới hạn trong README, thông báo license, metadata manifest và cấu hình CI khi có; chưa đọc toàn bộ mã triển khai, chưa cài hoặc chạy kiểm thử upstream.
- **Snapshot:** kiểm ngày 2026-11-23; commit `c70e0d89525933c4dab373143d486c93331392fb` (2026-11-21T00:24:51+08:00); 38,977 sao theo GitHub API ngày 2026-11-23. Sao không đại diện chất lượng.
- **Bằng chứng:** [README.md](https://github.com/ant-design/ant-design-pro/blob/c70e0d89525933c4dab373143d486c93331392fb/README.md) · [LICENSE](https://github.com/ant-design/ant-design-pro/blob/c70e0d89525933c4dab373143d486c93331392fb/LICENSE) · [package.json](https://github.com/ant-design/ant-design-pro/blob/c70e0d89525933c4dab373143d486c93331392fb/package.json) · [.github/workflows/ci.yml](https://github.com/ant-design/ant-design-pro/blob/c70e0d89525933c4dab373143d486c93331392fb/.github/workflows/ci.yml) · [GitHub API](https://api.github.com/repos/ant-design/ant-design-pro).

<a id="anhkysuai-dogfalo-materialize"></a>

### Materialize (Dogfalo)

- **Repo:** [Dogfalo/materialize](https://github.com/Dogfalo/materialize).
- **Mục đích:** CSS framework theo Material Design với bộ component web.
- **Điểm đáng dùng:** README chỉ ra Grunt/BrowserSync cho docs và Jasmine cho component tests; package mang bản 1.0.0.
- **License:** MIT.
- **Giới hạn:** Commit đọc cuối năm 2020 và tài liệu còn Bower/deprecated workflow; cần phân biệt fork hiện đại với đúng repo Dogfalo này.
- **Tích hợp:** Giữ trong kho cho bảo trì dự án cũ, kiểm tra accessibility và dependency trước khi áp vào template mới.
- **Đối chiếu:** [MUI](../06-ui-ux-design/README.md) cho React Material; [Material Web](../06-ui-ux-design/README.md) cho web components; [Bootstrap](../08-awesome-lists-learning/README.md#6c522-thư-viện-giao-diện--css) cho CSS tổng quát.
- **Mức kiểm chứng:** `docs-read` — Đọc các phần mô tả và giới hạn trong README, thông báo license, metadata manifest và cấu hình CI khi có; chưa đọc toàn bộ mã triển khai, chưa cài hoặc chạy kiểm thử upstream.
- **Snapshot:** kiểm ngày 2026-11-23; commit `824e78248b3de81e383445e76ffb04cc3264fe7d` (2020-06-01T09:39:49-07:00); 38,770 sao theo GitHub API ngày 2026-11-23. Sao không đại diện chất lượng.
- **Bằng chứng:** [README.md](https://github.com/Dogfalo/materialize/blob/824e78248b3de81e383445e76ffb04cc3264fe7d/README.md) · [LICENSE](https://github.com/Dogfalo/materialize/blob/824e78248b3de81e383445e76ffb04cc3264fe7d/LICENSE) · [package.json](https://github.com/Dogfalo/materialize/blob/824e78248b3de81e383445e76ffb04cc3264fe7d/package.json) · [GitHub API](https://api.github.com/repos/Dogfalo/materialize).

<a id="anhkysuai-textualize-textual"></a>

### Textual

- **Repo:** [Textualize/textual](https://github.com/Textualize/textual).
- **Mục đích:** Framework Python cho giao diện terminal có thể phục vụ qua trình duyệt.
- **Điểm đáng dùng:** Widget, layout, command palette và dev console riêng hỗ trợ xây app tương tác; async bên dưới nhưng API không bắt buộc mọi mã dùng async.
- **License:** MIT.
- **Giới hạn:** Phục vụ web thêm ranh giới xác thực và kết nối, không chỉ đổi nơi hiển thị; workflow đọc là CodeQL, chưa chạy suite UI.
- **Tích hợp:** Dùng cho bảng điều khiển công cụ nội bộ, xử lý tác vụ chậm ngoài vòng lặp UI và khóa quyền khi mở web.
- **Đối chiếu:** [Rich](../13-dev-stack-devops/README.md#anhkysuai-textualize-rich) cho output tĩnh; [Bubble Tea](../06-ui-ux-design/README.md#anhkysuai-charmbracelet-bubbletea) cho Go TUI; [Ink](../06-ui-ux-design/README.md#anhkysuai-vadimdemedes-ink) cho React terminal.
- **Mức kiểm chứng:** `docs-read` — Đọc các phần mô tả và giới hạn trong README, thông báo license, metadata manifest và cấu hình CI khi có; chưa đọc toàn bộ mã triển khai, chưa cài hoặc chạy kiểm thử upstream.
- **Snapshot:** kiểm ngày 2026-11-23; commit `5e5b7ef58b8c5572c13a3ff9027d756623661495` (2026-10-09T18:24:09+01:00); 37,718 sao theo GitHub API ngày 2026-11-23. Sao không đại diện chất lượng.
- **Bằng chứng:** [README.md](https://github.com/Textualize/textual/blob/5e5b7ef58b8c5572c13a3ff9027d756623661495/README.md) · [LICENSE](https://github.com/Textualize/textual/blob/5e5b7ef58b8c5572c13a3ff9027d756623661495/LICENSE) · [pyproject.toml](https://github.com/Textualize/textual/blob/5e5b7ef58b8c5572c13a3ff9027d756623661495/pyproject.toml) · [.github/workflows/codeql.yml](https://github.com/Textualize/textual/blob/5e5b7ef58b8c5572c13a3ff9027d756623661495/.github/workflows/codeql.yml) · [GitHub API](https://api.github.com/repos/Textualize/textual).

<a id="anhkysuai-solidjs-solid"></a>

### Solid

- **Repo:** [solidjs/solid](https://github.com/solidjs/solid).
- **Mục đích:** UI JavaScript với reactivity chi tiết và JSX biên dịch sang DOM.
- **Điểm đáng dùng:** README snapshot 2.0 mô tả component chạy một lần, tracking theo biểu thức, microtask batching/flush và SSR streaming.
- **License:** MIT.
- **Giới hạn:** API khác Solid 1.x, được giữ ở nhánh riêng; không lấy root package version làm version phát hành hoặc trộn ví dụ cũ.
- **Tích hợp:** Khóa compiler/renderer và major, viết test vòng đời reactive, async boundary cùng hydration cho template.
- **Đối chiếu:** React cho component VDOM; [Svelte](../13-dev-stack-devops/README.md) cho compiler; [Preact](../06-ui-ux-design/README.md#anhkysuai-preactjs-preact) cho runtime nhỏ.
- **Mức kiểm chứng:** `docs-read` — Đọc các phần mô tả và giới hạn trong README, thông báo license, metadata manifest và cấu hình CI khi có; chưa đọc toàn bộ mã triển khai, chưa cài hoặc chạy kiểm thử upstream.
- **Snapshot:** kiểm ngày 2026-11-23; commit `30e7805eb1bbd9e2601d0252558e91d2547e96f4` (2026-11-22T21:46:49-08:00); 36,927 sao theo GitHub API ngày 2026-11-23. Sao không đại diện chất lượng.
- **Bằng chứng:** [README.md](https://github.com/solidjs/solid/blob/30e7805eb1bbd9e2601d0252558e91d2547e96f4/README.md) · [LICENSE](https://github.com/solidjs/solid/blob/30e7805eb1bbd9e2601d0252558e91d2547e96f4/LICENSE) · [package.json](https://github.com/solidjs/solid/blob/30e7805eb1bbd9e2601d0252558e91d2547e96f4/package.json) · [.github/workflows/main-ci.yml](https://github.com/solidjs/solid/blob/30e7805eb1bbd9e2601d0252558e91d2547e96f4/.github/workflows/main-ci.yml) · [GitHub API](https://api.github.com/repos/solidjs/solid).

<a id="anhkysuai-raysan5-raylib"></a>

### raylib

- **Repo:** [raysan5/raylib](https://github.com/raysan5/raylib).
- **Mục đích:** Thư viện C99 cho game, đồ họa và công cụ tương tác.
- **Điểm đáng dùng:** Các module rlgl/raymath, audio và nhiều định dạng asset tạo nền lập trình trực tiếp, không phụ thuộc editor trực quan.
- **License:** Zlib; dependency nhúng có license riêng.
- **Giới hạn:** README ghi mặc định một cửa sổ/một OpenGL context, texture render đảo chiều dọc; dependency được nhúng không đồng nghĩa không có license phụ.
- **Tích hợp:** Làm mẫu render/input nhỏ, kiểm kê src/external và kiểm tra GPU/HTML5 trên target cần phát hành.
- **Đối chiếu:** SDL cho multimedia thấp tầng; [Bevy](../13-dev-stack-devops/README.md#anhkysuai-bevyengine-bevy) cho game ECS; [Phaser](../06-ui-ux-design/README.md#anhkysuai-phaserjs-phaser) cho game web.
- **Mức kiểm chứng:** `docs-read` — Đọc các phần mô tả và giới hạn trong README, thông báo license, metadata manifest và cấu hình CI khi có; chưa đọc toàn bộ mã triển khai, chưa cài hoặc chạy kiểm thử upstream.
- **Snapshot:** kiểm ngày 2026-11-23; commit `4b0c5962dda6ca2b473fe81254e6027c84714b51` (2026-11-22T20:53:27+01:00); 35,770 sao theo GitHub API ngày 2026-11-23. Sao không đại diện chất lượng.
- **Bằng chứng:** [README.md](https://github.com/raysan5/raylib/blob/4b0c5962dda6ca2b473fe81254e6027c84714b51/README.md) · [LICENSE](https://github.com/raysan5/raylib/blob/4b0c5962dda6ca2b473fe81254e6027c84714b51/LICENSE) · [CMakeLists.txt](https://github.com/raysan5/raylib/blob/4b0c5962dda6ca2b473fe81254e6027c84714b51/CMakeLists.txt) · [.github/workflows/build_cmake.yml](https://github.com/raysan5/raylib/blob/4b0c5962dda6ca2b473fe81254e6027c84714b51/.github/workflows/build_cmake.yml) · [GitHub API](https://api.github.com/repos/raysan5/raylib).

<a id="anhkysuai-alvarotrigo-fullpage-js"></a>

### fullPage.js

- **Repo:** [alvarotrigo/fullPage.js](https://github.com/alvarotrigo/fullPage.js).
- **Mục đích:** Tạo trang cuộn từng section toàn màn hình và slide ngang.
- **Điểm đáng dùng:** README mô tả cấu trúc section/slide, callback, media và tùy chọn responsive; package đang ở dòng 4.
- **License:** GPL-3.0 hoặc giấy phép thương mại; extension theo điều khoản riêng.
- **Giới hạn:** licenseKey là bắt buộc theo tài liệu; sản phẩm đóng cần xem giấy phép thương mại. Hành vi cuộn cần kiểm tra bàn phím, reduced-motion và nội dung dài.
- **Tích hợp:** Chỉ dùng khi thiết kế thực sự cần snap toàn trang, kiểm tra giấy phép phân phối template trước khi đóng gói.
- **Đối chiếu:** CSS scroll-snap cho nền web; Swiper cho slider; [GSAP](../19-agentic-video-media/README.md#3h-kiểm-ảnh-ai-video-stack-remotion-skills-blender-và-blender-mcp-faster-whisper-chatterbox-gsap-ảnh-người-dùng-gửi-đọc-mã-8112026) cho điều khiển animation.
- **Mức kiểm chứng:** `docs-read` — Đọc các phần mô tả và giới hạn trong README, thông báo license, metadata manifest và cấu hình CI khi có; chưa đọc toàn bộ mã triển khai, chưa cài hoặc chạy kiểm thử upstream.
- **Snapshot:** kiểm ngày 2026-11-23; commit `49f15effa7b195def295a36f872c28153cf9fb00` (2026-03-04T21:31:23+07:00); 35,353 sao theo GitHub API ngày 2026-11-23. Sao không đại diện chất lượng.
- **Bằng chứng:** [README.md](https://github.com/alvarotrigo/fullPage.js/blob/49f15effa7b195def295a36f872c28153cf9fb00/README.md) · [LICENSE](https://github.com/alvarotrigo/fullPage.js/blob/49f15effa7b195def295a36f872c28153cf9fb00/LICENSE) · [package.json](https://github.com/alvarotrigo/fullPage.js/blob/49f15effa7b195def295a36f872c28153cf9fb00/package.json) · [GitHub API](https://api.github.com/repos/alvarotrigo/fullPage.js).

<a id="anhkysuai-vbenjs-vue-vben-admin"></a>

### Vue Vben Admin

- **Repo:** [vbenjs/vue-vben-admin](https://github.com/vbenjs/vue-vben-admin).
- **Mục đích:** Mẫu quản trị Vue 3, Vite và TypeScript có theme, i18n và route permission.
- **Điểm đáng dùng:** README phân biệt v5 không tương thích bản trước, manifest khóa các dòng Node/pnpm và giao diện dựa trên browser hiện đại.
- **License:** MIT.
- **Giới hạn:** Quyền route ở client không thay authorization server; Tailwind v4 đặt sàn browser, không phù hợp yêu cầu IE.
- **Tích hợp:** Chọn v5 rõ ràng, thay tài khoản demo/mock, nối phân quyền backend và kiểm thử menu theo vai trò.
- **Đối chiếu:** [Ant Design Pro](../06-ui-ux-design/README.md#anhkysuai-ant-design-ant-design-pro) cho React; [Quasar](../06-ui-ux-design/README.md#anhkysuai-quasarframework-quasar) cho Vue đa target; [Refine](../06-ui-ux-design/README.md) cho admin có data provider.
- **Mức kiểm chứng:** `docs-read` — Đọc các phần mô tả và giới hạn trong README, thông báo license, metadata manifest và cấu hình CI khi có; chưa đọc toàn bộ mã triển khai, chưa cài hoặc chạy kiểm thử upstream.
- **Snapshot:** kiểm ngày 2026-11-23; commit `e726bc92780c1023c2393042871470d413ad79dc` (2026-11-19T13:15:40+08:00); 33,845 sao theo GitHub API ngày 2026-11-23. Sao không đại diện chất lượng.
- **Bằng chứng:** [README.md](https://github.com/vbenjs/vue-vben-admin/blob/e726bc92780c1023c2393042871470d413ad79dc/README.md) · [LICENSE](https://github.com/vbenjs/vue-vben-admin/blob/e726bc92780c1023c2393042871470d413ad79dc/LICENSE) · [package.json](https://github.com/vbenjs/vue-vben-admin/blob/e726bc92780c1023c2393042871470d413ad79dc/package.json) · [.github/workflows/ci.yml](https://github.com/vbenjs/vue-vben-admin/blob/e726bc92780c1023c2393042871470d413ad79dc/.github/workflows/ci.yml) · [GitHub API](https://api.github.com/repos/vbenjs/vue-vben-admin).

<a id="anhkysuai-vercel-swr"></a>

### SWR

- **Repo:** [vercel/swr](https://github.com/vercel/swr).
- **Mục đích:** React hooks quản lý lấy dữ liệu và cache theo stale-while-revalidate.
- **Điểm đáng dùng:** Key xác định request, fetcher tùy biến, deduplication, revalidation khi focus/network và optimistic mutation giảm mã lặp.
- **License:** MIT.
- **Giới hạn:** Snapshot là 2.6 beta; cache key phải phân biệt người dùng/quyền truy cập, stale data không phù hợp mọi hành động cần chính xác tức thời.
- **Tích hợp:** Chuẩn hóa fetcher, lỗi và key theo phiên, kiểm tra invalidation sau mutation và đăng xuất.
- **Đối chiếu:** [TanStack Query](../13-dev-stack-devops/README.md) cho server state; RTK Query cho Redux; Apollo Client cho GraphQL.
- **Mức kiểm chứng:** `docs-read` — Đọc các phần mô tả và giới hạn trong README, thông báo license, metadata manifest và cấu hình CI khi có; chưa đọc toàn bộ mã triển khai, chưa cài hoặc chạy kiểm thử upstream.
- **Snapshot:** kiểm ngày 2026-11-23; commit `8148ef012fd5b317d1e8ec2da4b2ca0673f63c0f` (2026-10-16T19:57:57+02:00); 32,495 sao theo GitHub API ngày 2026-11-23. Sao không đại diện chất lượng.
- **Bằng chứng:** [README.md](https://github.com/vercel/swr/blob/8148ef012fd5b317d1e8ec2da4b2ca0673f63c0f/README.md) · [LICENSE](https://github.com/vercel/swr/blob/8148ef012fd5b317d1e8ec2da4b2ca0673f63c0f/LICENSE) · [package.json](https://github.com/vercel/swr/blob/8148ef012fd5b317d1e8ec2da4b2ca0673f63c0f/package.json) · [.github/workflows/test.yml](https://github.com/vercel/swr/blob/8148ef012fd5b317d1e8ec2da4b2ca0673f63c0f/.github/workflows/test.yml) · [GitHub API](https://api.github.com/repos/vercel/swr).

<a id="anhkysuai-emilk-egui"></a>

### egui

- **Repo:** [emilk/egui](https://github.com/emilk/egui).
- **Mục đích:** GUI immediate-mode Rust dùng native, web hoặc nhúng trong engine.
- **Điểm đáng dùng:** eframe cung cấp runtime ứng dụng, epaint và renderer cho textured triangles thuận tiện tích hợp công cụ đồ họa.
- **License:** MIT OR Apache-2.0; font kèm theo có license riêng.
- **Giới hạn:** Accessibility tùy nền tảng, README nêu screen reader web còn thử nghiệm; không suy ra UX native chỉ từ tính portable.
- **Tích hợp:** Dùng bảng điều khiển/editor nội bộ, kiểm tra input, DPI, font và trợ năng theo target.
- **Đối chiếu:** [Iced](../06-ui-ux-design/README.md#anhkysuai-iced-rs-iced) cho Elm-style Rust; [Slint](../06-ui-ux-design/README.md#anhkysuai-slint-ui-slint) cho UI khai báo; Dear ImGui cho công cụ C++.
- **Mức kiểm chứng:** `docs-read` — Đọc các phần mô tả và giới hạn trong README, thông báo license, metadata manifest và cấu hình CI khi có; chưa đọc toàn bộ mã triển khai, chưa cài hoặc chạy kiểm thử upstream.
- **Snapshot:** kiểm ngày 2026-11-23; commit `d33dec58efd165add27acb9cddaf7e457eb5e64f` (2026-11-20T13:52:23Z); 32,444 sao theo GitHub API ngày 2026-11-23. Sao không đại diện chất lượng.
- **Bằng chứng:** [README.md](https://github.com/emilk/egui/blob/d33dec58efd165add27acb9cddaf7e457eb5e64f/README.md) · [LICENSE-APACHE](https://github.com/emilk/egui/blob/d33dec58efd165add27acb9cddaf7e457eb5e64f/LICENSE-APACHE) · [LICENSE-MIT](https://github.com/emilk/egui/blob/d33dec58efd165add27acb9cddaf7e457eb5e64f/LICENSE-MIT) · [Cargo.toml](https://github.com/emilk/egui/blob/d33dec58efd165add27acb9cddaf7e457eb5e64f/Cargo.toml) · [.github/workflows/link_checker.yml](https://github.com/emilk/egui/blob/d33dec58efd165add27acb9cddaf7e457eb5e64f/.github/workflows/link_checker.yml) · [GitHub API](https://api.github.com/repos/emilk/egui).

<a id="anhkysuai-iced-rs-iced"></a>

### Iced

- **Repo:** [iced-rs/iced](https://github.com/iced-rs/iced).
- **Mục đích:** GUI Rust đa nền tảng theo kiến trúc Elm.
- **Điểm đáng dùng:** Tách state, message, view và update; renderer wgpu hoặc tiny-skia cùng task async giúp tổ chức UI có kiểu.
- **License:** MIT.
- **Giới hạn:** README gọi experimental, manifest 0.15.0-dev; API/toolchain có thể đổi và hỗ trợ web/native cần xác nhận riêng.
- **Tích hợp:** Thử màn hình tương tác nhỏ, phân tách cập nhật state với I/O và kiểm thử renderer trên GPU mục tiêu.
- **Đối chiếu:** [egui](../06-ui-ux-design/README.md#anhkysuai-emilk-egui) cho immediate mode; [Slint](../06-ui-ux-design/README.md#anhkysuai-slint-ui-slint) cho UI khai báo; [Dioxus](../13-dev-stack-devops/README.md#anhkysuai-dioxuslabs-dioxus) cho web-style UI.
- **Mức kiểm chứng:** `docs-read` — Đọc các phần mô tả và giới hạn trong README, thông báo license, metadata manifest và cấu hình CI khi có; chưa đọc toàn bộ mã triển khai, chưa cài hoặc chạy kiểm thử upstream.
- **Snapshot:** kiểm ngày 2026-11-23; commit `98bd48fe011efc0ec5819fee0fa7673a7169ff11` (2026-11-19T13:06:00+01:00); 32,110 sao theo GitHub API ngày 2026-11-23. Sao không đại diện chất lượng.
- **Bằng chứng:** [README.md](https://github.com/iced-rs/iced/blob/98bd48fe011efc0ec5819fee0fa7673a7169ff11/README.md) · [LICENSE](https://github.com/iced-rs/iced/blob/98bd48fe011efc0ec5819fee0fa7673a7169ff11/LICENSE) · [Cargo.toml](https://github.com/iced-rs/iced/blob/98bd48fe011efc0ec5819fee0fa7673a7169ff11/Cargo.toml) · [.github/workflows/test.yml](https://github.com/iced-rs/iced/blob/98bd48fe011efc0ec5819fee0fa7673a7169ff11/.github/workflows/test.yml) · [GitHub API](https://api.github.com/repos/iced-rs/iced).

<a id="anhkysuai-codex-team-editor-js"></a>

### Editor.js

- **Repo:** [codex-team/editor.js](https://github.com/codex-team/editor.js).
- **Mục đích:** Editor dạng block lưu dữ liệu JSON thay HTML.
- **Điểm đáng dùng:** Mỗi loại block là plugin, editor.save trả Promise dữ liệu; mô hình thuận tiện render lại trên nhiều kênh.
- **License:** Apache-2.0.
- **Giới hạn:** HEAD 2.32.0-rc.4, roadmap cộng tác còn cập nhật basic tools; JSON vẫn phải validate/sanitize theo từng plugin.
- **Tích hợp:** Khóa schema block và plugin, viết migration dữ liệu và kiểm thử render nội dung không tin cậy.
- **Đối chiếu:** [Tiptap](../06-ui-ux-design/README.md#anhkysuai-ueberdosis-tiptap) cho ProseMirror; Lexical cho editor React; [Slate](../06-ui-ux-design/README.md#anhkysuai-ianstormtaylor-slate) cho mô hình tự tùy biến.
- **Mức kiểm chứng:** `docs-read` — Đọc các phần mô tả và giới hạn trong README, thông báo license, metadata manifest và cấu hình CI khi có; chưa đọc toàn bộ mã triển khai, chưa cài hoặc chạy kiểm thử upstream.
- **Snapshot:** kiểm ngày 2026-11-23; commit `60db62e960480faab1f10f98e96cf4fd3af4a146` (2026-11-18T13:59:20+03:00); 32,007 sao theo GitHub API ngày 2026-11-23. Sao không đại diện chất lượng.
- **Bằng chứng:** [README.md](https://github.com/codex-team/editor.js/blob/60db62e960480faab1f10f98e96cf4fd3af4a146/README.md) · [LICENSE](https://github.com/codex-team/editor.js/blob/60db62e960480faab1f10f98e96cf4fd3af4a146/LICENSE) · [package.json](https://github.com/codex-team/editor.js/blob/60db62e960480faab1f10f98e96cf4fd3af4a146/package.json) · [.github/workflows/eslint.yml](https://github.com/codex-team/editor.js/blob/60db62e960480faab1f10f98e96cf4fd3af4a146/.github/workflows/eslint.yml) · [GitHub API](https://api.github.com/repos/codex-team/editor.js).

<a id="anhkysuai-ianstormtaylor-slate"></a>

### Slate

- **Repo:** [ianstormtaylor/slate](https://github.com/ianstormtaylor/slate).
- **Mục đích:** Framework rich-text editor React cho schema và hành vi tùy biến.
- **Điểm đáng dùng:** Chuỗi plugin bao quanh contenteditable giúp mở rộng logic thay vì giới hạn vào tập định dạng cố định; CI có artifact Playwright.
- **License:** MIT.
- **Giới hạn:** README ghi beta, API chưa chốt và không có lịch 1.0; người dùng phải đảm nhận schema, serialization, paste và lỗi browser.
- **Tích hợp:** Chốt schema tài liệu có version, test IME/selection/undo và paste trước khi dùng làm editor chung của template.
- **Đối chiếu:** [Tiptap](../06-ui-ux-design/README.md#anhkysuai-ueberdosis-tiptap) cho extension ProseMirror; Lexical cho editor React; Quill cho bộ editor sẵn.
- **Mức kiểm chứng:** `docs-read` — Đọc các phần mô tả và giới hạn trong README, thông báo license, metadata manifest và cấu hình CI khi có; chưa đọc toàn bộ mã triển khai, chưa cài hoặc chạy kiểm thử upstream.
- **Snapshot:** kiểm ngày 2026-11-23; commit `7e6e576f30b01a4ed83a9fd233cb1c5a64bf069c` (2026-11-20T12:54:19-07:00); 31,750 sao theo GitHub API ngày 2026-11-23. Sao không đại diện chất lượng.
- **Bằng chứng:** [Readme.md](https://github.com/ianstormtaylor/slate/blob/7e6e576f30b01a4ed83a9fd233cb1c5a64bf069c/Readme.md) · [License.md](https://github.com/ianstormtaylor/slate/blob/7e6e576f30b01a4ed83a9fd233cb1c5a64bf069c/License.md) · [package.json](https://github.com/ianstormtaylor/slate/blob/7e6e576f30b01a4ed83a9fd233cb1c5a64bf069c/package.json) · [.github/workflows/ci.yml](https://github.com/ianstormtaylor/slate/blob/7e6e576f30b01a4ed83a9fd233cb1c5a64bf069c/.github/workflows/ci.yml) · [GitHub API](https://api.github.com/repos/ianstormtaylor/slate).

<a id="anhkysuai-transloadit-uppy"></a>

### Uppy

- **Repo:** [transloadit/uppy](https://github.com/transloadit/uppy).
- **Mục đích:** Bộ tải tệp JavaScript mô-đun với UI sẵn hoặc headless.
- **Điểm đáng dùng:** Plugin tus hỗ trợ tiếp tục upload, Companion lấy tệp remote; tài liệu phân biệt dashboard, headless component và hooks.
- **License:** MIT.
- **Giới hạn:** Kiểm tra file phía client không bảo vệ backend; remote URL/OAuth qua Companion cần cấu hình quyền, giới hạn kích thước và đích tải.
- **Tích hợp:** Dùng endpoint xác thực và validate server, thử mạng đứt cùng resume và kiểm kê plugin thật sự cần.
- **Đối chiếu:** FilePond cho uploader UI; tus-js-client cho giao thức resume; input file HTML cho tải đơn giản.
- **Mức kiểm chứng:** `docs-read` — Đọc các phần mô tả và giới hạn trong README, thông báo license, metadata manifest và cấu hình CI khi có; chưa đọc toàn bộ mã triển khai, chưa cài hoặc chạy kiểm thử upstream.
- **Snapshot:** kiểm ngày 2026-11-23; commit `31a49e492db21f1dd37539ef24010e74be82ed51` (2026-11-23T18:06:42+08:00); 31,087 sao theo GitHub API ngày 2026-11-23. Sao không đại diện chất lượng.
- **Bằng chứng:** [README.md](https://github.com/transloadit/uppy/blob/31a49e492db21f1dd37539ef24010e74be82ed51/README.md) · [LICENSE](https://github.com/transloadit/uppy/blob/31a49e492db21f1dd37539ef24010e74be82ed51/LICENSE) · [package.json](https://github.com/transloadit/uppy/blob/31a49e492db21f1dd37539ef24010e74be82ed51/package.json) · [.github/workflows/ci.yml](https://github.com/transloadit/uppy/blob/31a49e492db21f1dd37539ef24010e74be82ed51/.github/workflows/ci.yml) · [GitHub API](https://api.github.com/repos/transloadit/uppy).

<a id="anhkysuai-layui-layui"></a>

### Layui

- **Repo:** [layui/layui](https://github.com/layui/layui).
- **Mục đích:** Bộ UI HTML/CSS/JavaScript thuần cho trang web nghiệp vụ.
- **Điểm đáng dùng:** README phân biệt dòng 2 đang dùng với main dòng 3; bộ công cụ hướng đến phát triển trực tiếp trong browser.
- **License:** MIT.
- **Giới hạn:** Manifest 3.0.0-alpha.3; README không khuyến nghị production và nói prerelease chưa thuộc phạm vi cập nhật/bulletin an ninh thường lệ.
- **Tích hợp:** Giữ để bảo trì dự án Layui và thử v3 riêng, khóa major cùng tài liệu trước khi đóng gói template.
- **Đối chiếu:** [Bootstrap](../08-awesome-lists-learning/README.md#6c522-thư-viện-giao-diện--css) cho UI thuần; [Element Plus](../06-ui-ux-design/README.md#anhkysuai-element-plus-element-plus) cho Vue; [Ant Design](../06-ui-ux-design/README.md) cho React.
- **Mức kiểm chứng:** `docs-read` — Đọc các phần mô tả và giới hạn trong README, thông báo license, metadata manifest và cấu hình CI khi có; chưa đọc toàn bộ mã triển khai, chưa cài hoặc chạy kiểm thử upstream.
- **Snapshot:** kiểm ngày 2026-11-23; commit `13725717407d23fac11b15b1a1155d26328b6d99` (2026-11-12T16:50:06+08:00); 30,597 sao theo GitHub API ngày 2026-11-23. Sao không đại diện chất lượng.
- **Bằng chứng:** [README.md](https://github.com/layui/layui/blob/13725717407d23fac11b15b1a1155d26328b6d99/README.md) · [LICENSE](https://github.com/layui/layui/blob/13725717407d23fac11b15b1a1155d26328b6d99/LICENSE) · [package.json](https://github.com/layui/layui/blob/13725717407d23fac11b15b1a1155d26328b6d99/package.json) · [.github/workflows/ci.yml](https://github.com/layui/layui/blob/13725717407d23fac11b15b1a1155d26328b6d99/.github/workflows/ci.yml) · [GitHub API](https://api.github.com/repos/layui/layui).

<a id="anhkysuai-sampotts-plyr"></a>

### Plyr

- **Repo:** [sampotts/plyr](https://github.com/sampotts/plyr).
- **Mục đích:** Giao diện media player thống nhất cho HTML5, YouTube và Vimeo.
- **Điểm đáng dùng:** Controls, captions, keyboard, sự kiện chung và integration streaming giúp bảo trì player đang có.
- **License:** MIT.
- **Giới hạn:** README và manifest thông báo deprecated, chỉ cập nhật an ninh; tác giả hướng dự án mới sang Video.js 10.
- **Tích hợp:** Lưu làm tham chiếu bảo trì/migration, kiểm tra caption và plugin hiện dùng rồi chuyển từng nguồn phát sang API đích.
- **Đối chiếu:** Video.js 10 theo hướng upstream; Shaka Player cho adaptive streaming; video HTML cho nhu cầu cơ bản.
- **Mức kiểm chứng:** `docs-read` — Đọc các phần mô tả và giới hạn trong README, thông báo license, metadata manifest và cấu hình CI khi có; chưa đọc toàn bộ mã triển khai, chưa cài hoặc chạy kiểm thử upstream.
- **Snapshot:** kiểm ngày 2026-11-23; commit `b23f9b7d52366d171ed4ec45bd06aedd85954486` (2026-10-21T11:09:32+11:00); 29,983 sao theo GitHub API ngày 2026-11-23. Sao không đại diện chất lượng.
- **Bằng chứng:** [README.md](https://github.com/sampotts/plyr/blob/b23f9b7d52366d171ed4ec45bd06aedd85954486/README.md) · [LICENSE.md](https://github.com/sampotts/plyr/blob/b23f9b7d52366d171ed4ec45bd06aedd85954486/LICENSE.md) · [package.json](https://github.com/sampotts/plyr/blob/b23f9b7d52366d171ed4ec45bd06aedd85954486/package.json) · [.github/workflows/ci.yml](https://github.com/sampotts/plyr/blob/b23f9b7d52366d171ed4ec45bd06aedd85954486/.github/workflows/ci.yml) · [GitHub API](https://api.github.com/repos/sampotts/plyr).

<a id="anhkysuai-pmndrs-react-spring"></a>

### React Spring

- **Repo:** [pmndrs/react-spring](https://github.com/pmndrs/react-spring).
- **Mục đích:** Animation React theo mô hình lò xo cho DOM và react-three-fiber.
- **Điểm đáng dùng:** API khai báo hoặc imperative, spring mặc định và duration/easing tùy chọn giúp mô tả tương tác liên tục.
- **License:** MIT.
- **Giới hạn:** Thông số spring không thay yêu cầu accessibility; toolchain monorepo yêu cầu Node >=26.13.1, không nhầm với yêu cầu app tiêu thụ package.
- **Tích hợp:** Dùng cho chuyển trạng thái có ý nghĩa, tôn trọng reduced-motion và kiểm tra ngắt/đảo animation cùng hiệu năng thiết bị.
- **Đối chiếu:** [Motion](../22-motion-design-animation/README.md) cho React animation; [GSAP](../19-agentic-video-media/README.md#3h-kiểm-ảnh-ai-video-stack-remotion-skills-blender-và-blender-mcp-faster-whisper-chatterbox-gsap-ảnh-người-dùng-gửi-đọc-mã-8112026) cho timeline; CSS transitions cho hiệu ứng đơn giản.
- **Mức kiểm chứng:** `docs-read` — Đọc các phần mô tả và giới hạn trong README, thông báo license, metadata manifest và cấu hình CI khi có; chưa đọc toàn bộ mã triển khai, chưa cài hoặc chạy kiểm thử upstream.
- **Snapshot:** kiểm ngày 2026-11-23; commit `13aacc5a88af35061da375c0259629f1a16a3caa` (2026-11-23T07:55:18Z); 29,325 sao theo GitHub API ngày 2026-11-23. Sao không đại diện chất lượng.
- **Bằng chứng:** [README.md](https://github.com/pmndrs/react-spring/blob/13aacc5a88af35061da375c0259629f1a16a3caa/README.md) · [LICENSE](https://github.com/pmndrs/react-spring/blob/13aacc5a88af35061da375c0259629f1a16a3caa/LICENSE) · [package.json](https://github.com/pmndrs/react-spring/blob/13aacc5a88af35061da375c0259629f1a16a3caa/package.json) · [.github/workflows/tests.yml](https://github.com/pmndrs/react-spring/blob/13aacc5a88af35061da375c0259629f1a16a3caa/.github/workflows/tests.yml) · [GitHub API](https://api.github.com/repos/pmndrs/react-spring).

<a id="anhkysuai-fyne-io-fyne"></a>

### Fyne

- **Repo:** [fyne-io/fyne](https://github.com/fyne-io/fyne).
- **Mục đích:** UI toolkit Go cho desktop và mobile.
- **Điểm đáng dùng:** API app/widget chung và công cụ fyne package/install hỗ trợ tạo binary, demo mobile simulation giúp khảo sát layout.
- **License:** BSD-3-Clause.
- **Giới hạn:** Build cần compiler C và toolchain hệ thống; simulation không thay thiết bị thật và ký gói mobile, lần build đầu có thể tốn thời gian.
- **Tích hợp:** Dùng cho tiện ích Go, kiểm tra font, DPI, input và đóng gói từng OS trước khi chuẩn hóa mẫu.
- **Đối chiếu:** [Wails](../13-dev-stack-devops/README.md#anhkysuai-wailsapp-wails) cho Go với web UI; Gio cho GUI Go; [Flutter](../13-dev-stack-devops/README.md) cho UI đa nền.
- **Mức kiểm chứng:** `docs-read` — Đọc các phần mô tả và giới hạn trong README, thông báo license, metadata manifest và cấu hình CI khi có; chưa đọc toàn bộ mã triển khai, chưa cài hoặc chạy kiểm thử upstream.
- **Snapshot:** kiểm ngày 2026-11-23; commit `653e7928066891434a2ebe9dec4e63823493dce5` (2026-11-21T19:20:30+01:00); 28,859 sao theo GitHub API ngày 2026-11-23. Sao không đại diện chất lượng.
- **Bằng chứng:** [README.md](https://github.com/fyne-io/fyne/blob/653e7928066891434a2ebe9dec4e63823493dce5/README.md) · [LICENSE](https://github.com/fyne-io/fyne/blob/653e7928066891434a2ebe9dec4e63823493dce5/LICENSE) · [go.mod](https://github.com/fyne-io/fyne/blob/653e7928066891434a2ebe9dec4e63823493dce5/go.mod) · [.github/workflows/web_tests.yml](https://github.com/fyne-io/fyne/blob/653e7928066891434a2ebe9dec4e63823493dce5/.github/workflows/web_tests.yml) · [GitHub API](https://api.github.com/repos/fyne-io/fyne).

<a id="anhkysuai-tanstack-table"></a>

### TanStack Table

- **Repo:** [TanStack/table](https://github.com/TanStack/table).
- **Mục đích:** Lõi bảng dữ liệu headless cho nhiều framework.
- **Điểm đáng dùng:** Sorting, filtering, grouping, aggregation và selection tách khỏi markup/style; adapter giúp chia sẻ logic bảng giữa stack.
- **License:** MIT.
- **Giới hạn:** Headless đòi hỏi tự làm UI/a11y; virtualizable không có nghĩa tự cung cấp virtualization. Workflow đọc kiểm skill tài liệu, chưa chạy table tests.
- **Tích hợp:** Tách state bảng và server query, định nghĩa pagination/filter contract rồi kiểm tra bộ dữ liệu lớn và bàn phím.
- **Đối chiếu:** AG Grid cho datagrid đầy đủ; MUI Data Grid cho React; Ant Design Table cho ứng dụng nghiệp vụ.
- **Mức kiểm chứng:** `docs-read` — Đọc các phần mô tả và giới hạn trong README, thông báo license, metadata manifest và cấu hình CI khi có; chưa đọc toàn bộ mã triển khai, chưa cài hoặc chạy kiểm thử upstream.
- **Snapshot:** kiểm ngày 2026-11-23; commit `1cfb2e57cbfecf25e3d4ee1bda32fbd65e4e0327` (2026-11-18T15:03:12-05:00); 28,604 sao theo GitHub API ngày 2026-11-23. Sao không đại diện chất lượng.
- **Bằng chứng:** [README.md](https://github.com/TanStack/table/blob/1cfb2e57cbfecf25e3d4ee1bda32fbd65e4e0327/README.md) · [LICENSE](https://github.com/TanStack/table/blob/1cfb2e57cbfecf25e3d4ee1bda32fbd65e4e0327/LICENSE) · [package.json](https://github.com/TanStack/table/blob/1cfb2e57cbfecf25e3d4ee1bda32fbd65e4e0327/package.json) · [.github/workflows/check-skills.yml](https://github.com/TanStack/table/blob/1cfb2e57cbfecf25e3d4ee1bda32fbd65e4e0327/.github/workflows/check-skills.yml) · [GitHub API](https://api.github.com/repos/TanStack/table).

<a id="anhkysuai-mobxjs-mobx"></a>

### MobX

- **Repo:** [mobxjs/mobx](https://github.com/mobxjs/mobx).
- **Mục đích:** Quản lý state qua observable và dependency tracking tự động.
- **Điểm đáng dùng:** README minh họa observer theo dõi field đọc khi render, action cập nhật observable và truyền thay đổi tới computation liên quan.
- **License:** MIT.
- **Giới hạn:** Tracking ngầm cần hiểu ranh giới async và lifecycle; tuyên bố optimal rendering chưa phải benchmark ứng dụng hoặc bảo đảm không có side effect.
- **Tích hợp:** Tách domain state khỏi UI, quản lý disposal của reaction và viết test mutation/derived state.
- **Đối chiếu:** [Zustand](../06-ui-ux-design/README.md#anhkysuai-pmndrs-zustand) cho store đơn giản; Redux Toolkit cho luồng explicit; Jotai cho atom.
- **Mức kiểm chứng:** `docs-read` — Đọc các phần mô tả và giới hạn trong README, thông báo license, metadata manifest và cấu hình CI khi có; chưa đọc toàn bộ mã triển khai, chưa cài hoặc chạy kiểm thử upstream.
- **Snapshot:** kiểm ngày 2026-11-23; commit `abd3a5879796bcd0f1a23967444a5ff90c99709a` (2026-11-23T14:52:24+07:00); 28,217 sao theo GitHub API ngày 2026-11-23. Sao không đại diện chất lượng.
- **Bằng chứng:** [README.md](https://github.com/mobxjs/mobx/blob/abd3a5879796bcd0f1a23967444a5ff90c99709a/README.md) · [LICENSE](https://github.com/mobxjs/mobx/blob/abd3a5879796bcd0f1a23967444a5ff90c99709a/LICENSE) · [package.json](https://github.com/mobxjs/mobx/blob/abd3a5879796bcd0f1a23967444a5ff90c99709a/package.json) · [.github/workflows/build_and_test.yml](https://github.com/mobxjs/mobx/blob/abd3a5879796bcd0f1a23967444a5ff90c99709a/.github/workflows/build_and_test.yml) · [GitHub API](https://api.github.com/repos/mobxjs/mobx).

<a id="anhkysuai-element-plus-element-plus"></a>

### Element Plus

- **Repo:** [element-plus/element-plus](https://github.com/element-plus/element-plus).
- **Mục đích:** Bộ UI Vue 3 viết TypeScript và Composition API.
- **Điểm đáng dùng:** README cung cấp migration từ Element UI và component playground; workflow đã đọc kiểm tra SSR bằng Chromium/Puppeteer.
- **License:** MIT.
- **Giới hạn:** Migration tool không bảo đảm tương thích hành vi ứng dụng; cần kiểm thử SSR/hydration, locale và accessibility từng component sử dụng.
- **Tích hợp:** Đóng gói theme/token cùng Vue version, chọn import phù hợp và viết smoke test cho form, bảng, dialog.
- **Đối chiếu:** [Naive UI](../06-ui-ux-design/README.md) cho Vue; PrimeVue cho bộ nghiệp vụ; [Vuetify](../06-ui-ux-design/README.md) cho Material Design.
- **Mức kiểm chứng:** `docs-read` — Đọc các phần mô tả và giới hạn trong README, thông báo license, metadata manifest và cấu hình CI khi có; chưa đọc toàn bộ mã triển khai, chưa cài hoặc chạy kiểm thử upstream.
- **Snapshot:** kiểm ngày 2026-11-23; commit `7e6a728c90261c2bc9ff4378f17dca74bcb219d1` (2026-11-23T13:41:50+08:00); 27,872 sao theo GitHub API ngày 2026-11-23. Sao không đại diện chất lượng.
- **Bằng chứng:** [README.md](https://github.com/element-plus/element-plus/blob/7e6a728c90261c2bc9ff4378f17dca74bcb219d1/README.md) · [LICENSE](https://github.com/element-plus/element-plus/blob/7e6a728c90261c2bc9ff4378f17dca74bcb219d1/LICENSE) · [package.json](https://github.com/element-plus/element-plus/blob/7e6a728c90261c2bc9ff4378f17dca74bcb219d1/package.json) · [.github/workflows/test-ssr.yml](https://github.com/element-plus/element-plus/blob/7e6a728c90261c2bc9ff4378f17dca74bcb219d1/.github/workflows/test-ssr.yml) · [GitHub API](https://api.github.com/repos/element-plus/element-plus).

<a id="anhkysuai-mbadolato-iterm2-color-schemes"></a>

### iTerm2 Color Schemes

**Đã chuyển (2026-11-23):** hồ sơ này nay nằm ở [mục 13](../13-dev-stack-devops/README.md#anhkysuai-mbadolato-iterm2-color-schemes); catalog con xem [catalog/](../catalog/README.md).

<a id="anhkysuai-quasarframework-quasar"></a>

### Quasar

- **Repo:** [quasarframework/quasar](https://github.com/quasarframework/quasar).
- **Mục đích:** Framework Vue cho SPA, SSR/SSG, PWA, extension, hybrid mobile và desktop Electron.
- **Điểm đáng dùng:** Cùng hệ component và cấu hình target giảm công việc lặp; workflow ui-tests xây package UI và chuẩn bị kiểm thử.
- **License:** MIT.
- **Giới hạn:** Một codebase không loại bỏ khác biệt runtime native/web; tuyên bố enterprise-ready/accessibility trong README chưa được xác minh bằng thử nghiệm ở đây.
- **Tích hợp:** Chọn target đầu tiên, kiểm tra plugin native và SSR rồi tạo cấu hình build riêng cho từng môi trường.
- **Đối chiếu:** [Nuxt](../13-dev-stack-devops/README.md) cho Vue web; Ionic cho hybrid UI; [Vuetify](../06-ui-ux-design/README.md) cho bộ component Vue.
- **Mức kiểm chứng:** `docs-read` — Đọc các phần mô tả và giới hạn trong README, thông báo license, metadata manifest và cấu hình CI khi có; chưa đọc toàn bộ mã triển khai, chưa cài hoặc chạy kiểm thử upstream.
- **Snapshot:** kiểm ngày 2026-11-23; commit `16637f69c0edb6dd78b73cce4af7c502ff31fc84` (2026-11-21T12:57:53+02:00); 27,198 sao theo GitHub API ngày 2026-11-23. Sao không đại diện chất lượng.
- **Bằng chứng:** [README.md](https://github.com/quasarframework/quasar/blob/16637f69c0edb6dd78b73cce4af7c502ff31fc84/README.md) · [LICENSE](https://github.com/quasarframework/quasar/blob/16637f69c0edb6dd78b73cce4af7c502ff31fc84/LICENSE) · [package.json](https://github.com/quasarframework/quasar/blob/16637f69c0edb6dd78b73cce4af7c502ff31fc84/package.json) · [.github/workflows/ui-tests.yml](https://github.com/quasarframework/quasar/blob/16637f69c0edb6dd78b73cce4af7c502ff31fc84/.github/workflows/ui-tests.yml) · [GitHub API](https://api.github.com/repos/quasarframework/quasar).

<a id="anhkysuai-marmelab-react-admin"></a>

### React-admin

- **Repo:** [marmelab/react-admin](https://github.com/marmelab/react-admin).
- **Mục đích:** Framework React xây ứng dụng quản trị trên REST/GraphQL.
- **Điểm đáng dùng:** Data Provider nối API, Resource khai báo CRUD và controller hooks có thể thay UI; dựa trên MUI và công cụ form/query.
- **License:** MIT cho bản mở; Enterprise Edition theo điều khoản riêng.
- **Giới hạn:** Adapter không tự khớp pagination/filter của mọi API; role ở UI phải đi cùng authorization server, Enterprise không nằm trong quyền MIT chung.
- **Tích hợp:** Làm data/auth provider nhỏ với hợp đồng API cụ thể, kiểm thử optimistic update/undo và phân quyền bản ghi.
- **Đối chiếu:** [Refine](../06-ui-ux-design/README.md) cho admin headless; [Ant Design Pro](../06-ui-ux-design/README.md#anhkysuai-ant-design-ant-design-pro) cho boilerplate; [ToolJet](../05-low-code-llm-platforms/README.md) cho low-code nội bộ.
- **Mức kiểm chứng:** `docs-read` — Đọc các phần mô tả và giới hạn trong README, thông báo license, metadata manifest và cấu hình CI khi có; chưa đọc toàn bộ mã triển khai, chưa cài hoặc chạy kiểm thử upstream.
- **Snapshot:** kiểm ngày 2026-11-23; commit `0c8a5cda6ca68cb115565835af4062c102d62c6a` (2026-11-23T11:08:21+01:00); 27,000 sao theo GitHub API ngày 2026-11-23. Sao không đại diện chất lượng.
- **Bằng chứng:** [README.md](https://github.com/marmelab/react-admin/blob/0c8a5cda6ca68cb115565835af4062c102d62c6a/README.md) · [LICENSE.md](https://github.com/marmelab/react-admin/blob/0c8a5cda6ca68cb115565835af4062c102d62c6a/LICENSE.md) · [package.json](https://github.com/marmelab/react-admin/blob/0c8a5cda6ca68cb115565835af4062c102d62c6a/package.json) · [.github/workflows/test.yml](https://github.com/marmelab/react-admin/blob/0c8a5cda6ca68cb115565835af4062c102d62c6a/.github/workflows/test.yml) · [GitHub API](https://api.github.com/repos/marmelab/react-admin).

<a id="anhkysuai-airbnb-lottie-ios"></a>

### Lottie iOS

- **Repo:** [airbnb/lottie-ios](https://github.com/airbnb/lottie-ios).
- **Mục đích:** Render animation vector bodymovin JSON trên nền tảng Apple.
- **Điểm đáng dùng:** Playback, loop, scrub và thay thuộc tính runtime giúp bàn giao thiết kế thành animation; tài liệu phân biệt lottie-ios nguồn và lottie-spm trỏ XCFramework.
- **License:** Apache-2.0 cho thư viện; animation asset theo license riêng.
- **Giới hạn:** Asset JSON có thể phức tạp dù nhỏ; phải kiểm tra feature exporter, reduced-motion, CPU/GPU và license ảnh/font/animation.
- **Tích hợp:** Khóa thư viện và asset, chọn nguồn hay binary có chủ đích, đo animation trên thiết bị yếu trong màn hình thật.
- **Đối chiếu:** Rive cho animation tương tác; Core Animation cho nền Apple; Lottie Web cho web.
- **Mức kiểm chứng:** `docs-read` — Đọc các phần mô tả và giới hạn trong README, thông báo license, metadata manifest và cấu hình CI khi có; chưa đọc toàn bộ mã triển khai, chưa cài hoặc chạy kiểm thử upstream.
- **Snapshot:** kiểm ngày 2026-11-23; commit `1fb4d7d5b45b0e81239c0c0cab95136a10153762` (2026-10-06T10:02:32-07:00); 26,950 sao theo GitHub API ngày 2026-11-23. Sao không đại diện chất lượng.
- **Bằng chứng:** [README.md](https://github.com/airbnb/lottie-ios/blob/1fb4d7d5b45b0e81239c0c0cab95136a10153762/README.md) · [LICENSE](https://github.com/airbnb/lottie-ios/blob/1fb4d7d5b45b0e81239c0c0cab95136a10153762/LICENSE) · [package.json](https://github.com/airbnb/lottie-ios/blob/1fb4d7d5b45b0e81239c0c0cab95136a10153762/package.json) · [.github/workflows/main.yml](https://github.com/airbnb/lottie-ios/blob/1fb4d7d5b45b0e81239c0c0cab95136a10153762/.github/workflows/main.yml) · [GitHub API](https://api.github.com/repos/airbnb/lottie-ios).

<a id="anhkysuai-select2-select2"></a>

### Select2

- **Repo:** [select2/select2](https://github.com/select2/select2).
- **Mục đích:** Nâng select HTML thành tìm kiếm, multiselect và dữ liệu remote.
- **Điểm đáng dùng:** AJAX/pagination, optgroup lồng và templating hỗ trợ tập dữ liệu lớn; hoạt động như select và có file i18n riêng.
- **License:** MIT.
- **Giới hạn:** Phụ thuộc jQuery; danh sách browser rất cũ trong README không thay xác minh browser hiện tại, custom renderer cần tránh XSS.
- **Tích hợp:** Phù hợp bảo trì form jQuery, xác thực dữ liệu server, giới hạn search và thử bàn phím/screen reader.
- **Đối chiếu:** Tom Select cho vanilla JS; Choices.js cho select không jQuery; React Select cho React.
- **Mức kiểm chứng:** `docs-read` — Đọc các phần mô tả và giới hạn trong README, thông báo license, metadata manifest và cấu hình CI khi có; chưa đọc toàn bộ mã triển khai, chưa cài hoặc chạy kiểm thử upstream.
- **Snapshot:** kiểm ngày 2026-11-23; commit `c9e950c43419563853e5104dd9132b1d3733fe76` (2026-11-23T01:32:28Z); 25,908 sao theo GitHub API ngày 2026-11-23. Sao không đại diện chất lượng.
- **Bằng chứng:** [README.md](https://github.com/select2/select2/blob/c9e950c43419563853e5104dd9132b1d3733fe76/README.md) · [LICENSE.md](https://github.com/select2/select2/blob/c9e950c43419563853e5104dd9132b1d3733fe76/LICENSE.md) · [package.json](https://github.com/select2/select2/blob/c9e950c43419563853e5104dd9132b1d3733fe76/package.json) · [pyproject.toml](https://github.com/select2/select2/blob/c9e950c43419563853e5104dd9132b1d3733fe76/pyproject.toml) · [.github/workflows/main.yml](https://github.com/select2/select2/blob/c9e950c43419563853e5104dd9132b1d3733fe76/.github/workflows/main.yml) · [GitHub API](https://api.github.com/repos/select2/select2).

<a id="anhkysuai-libgdx-libgdx"></a>

### libGDX

- **Repo:** [libgdx/libgdx](https://github.com/libgdx/libgdx).
- **Mục đích:** Framework game Java 2D/3D dựa trên OpenGL/ES cho nhiều nền.
- **Điểm đáng dùng:** Gradle và project setup tách core game khỏi backend target; workflow xây native library và gói phát hành.
- **License:** Apache-2.0; dependency/asset giữ license riêng.
- **Giới hạn:** Không có editor game đầy đủ trong phạm vi README; toolchain iOS/web và thư viện native làm build khác nhau từng nền.
- **Tích hợp:** Dùng mẫu game Java với core thuần, thử input/audio/lifecycle trên target và kiểm kê asset trước phân phối.
- **Đối chiếu:** [Bevy](../13-dev-stack-devops/README.md#anhkysuai-bevyengine-bevy) cho ECS Rust; [raylib](../06-ui-ux-design/README.md#anhkysuai-raysan5-raylib) cho C; [Phaser](../06-ui-ux-design/README.md#anhkysuai-phaserjs-phaser) cho game web.
- **Mức kiểm chứng:** `docs-read` — Đọc các phần mô tả và giới hạn trong README, thông báo license, metadata manifest và cấu hình CI khi có; chưa đọc toàn bộ mã triển khai, chưa cài hoặc chạy kiểm thử upstream.
- **Snapshot:** kiểm ngày 2026-11-23; commit `be635906dc2a437450403bd88b7a40fc8d944354` (2026-11-19T13:58:15Z); 25,551 sao theo GitHub API ngày 2026-11-23. Sao không đại diện chất lượng.
- **Bằng chứng:** [README.md](https://github.com/libgdx/libgdx/blob/be635906dc2a437450403bd88b7a40fc8d944354/README.md) · [LICENSE](https://github.com/libgdx/libgdx/blob/be635906dc2a437450403bd88b7a40fc8d944354/LICENSE) · [build.gradle](https://github.com/libgdx/libgdx/blob/be635906dc2a437450403bd88b7a40fc8d944354/build.gradle) · [.github/workflows/build-publish.yml](https://github.com/libgdx/libgdx/blob/be635906dc2a437450403bd88b7a40fc8d944354/.github/workflows/build-publish.yml) · [GitHub API](https://api.github.com/repos/libgdx/libgdx).

<a id="anhkysuai-angular-components"></a>

### Angular Components

- **Repo:** [angular/components](https://github.com/angular/components).
- **Mục đích:** Bộ Angular Material, CDK, ARIA và wrapper API Google.
- **Điểm đáng dùng:** README phân tách headless directives ARIA, interaction primitive CDK và component Material để chọn đúng mức tùy biến.
- **License:** MIT.
- **Giới hạn:** HEAD 22.4.0-next.0; Google Maps/YouTube là API dịch vụ ngoài, thư viện không thay điều khoản/quota. Accessibility vẫn cần kiểm tra theo ứng dụng.
- **Tích hợp:** Khóa major với Angular, dùng CDK/ARIA cho design system riêng và kiểm thử keyboard/focus của flow thật.
- **Đối chiếu:** PrimeNG cho Angular nghiệp vụ; [NG-ZORRO](../06-ui-ux-design/README.md) cho Ant Design; [Material Web](../06-ui-ux-design/README.md) cho web components.
- **Mức kiểm chứng:** `docs-read` — Đọc các phần mô tả và giới hạn trong README, thông báo license, metadata manifest và cấu hình CI khi có; chưa đọc toàn bộ mã triển khai, chưa cài hoặc chạy kiểm thử upstream.
- **Snapshot:** kiểm ngày 2026-11-23; commit `386c01bf16327d6fe9699eb121337ba90f08c356` (2026-11-23T09:52:49+01:00); 25,049 sao theo GitHub API ngày 2026-11-23. Sao không đại diện chất lượng.
- **Bằng chứng:** [README.md](https://github.com/angular/components/blob/386c01bf16327d6fe9699eb121337ba90f08c356/README.md) · [LICENSE](https://github.com/angular/components/blob/386c01bf16327d6fe9699eb121337ba90f08c356/LICENSE) · [package.json](https://github.com/angular/components/blob/386c01bf16327d6fe9699eb121337ba90f08c356/package.json) · [.github/workflows/ci.yml](https://github.com/angular/components/blob/386c01bf16327d6fe9699eb121337ba90f08c356/.github/workflows/ci.yml) · [GitHub API](https://api.github.com/repos/angular/components).

<a id="anhkysuai-highlightjs-highlight-js"></a>

### Highlight.js

- **Repo:** [highlightjs/highlight.js](https://github.com/highlightjs/highlight.js).
- **Mục đích:** Tô cú pháp mã nguồn trong browser hoặc server bằng JavaScript.
- **Điểm đáng dùng:** Có tự nhận diện ngôn ngữ và import bộ common/định nghĩa riêng, không lệ thuộc framework; CI kiểm build CDN/ESM.
- **License:** BSD-3-Clause.
- **Giới hạn:** Autodetect có thể sai và tốn thời gian cho khối lớn; nội dung mã cần escape đúng, theme/ngôn ngữ bên thứ ba phải kiểm tra riêng.
- **Tích hợp:** Ghi language rõ trong template docs, chỉ bundle ngôn ngữ cần và dùng worker/server rendering nếu khối mã lớn.
- **Đối chiếu:** Shiki cho TextMate theme; Prism cho highlight web; [Tree-sitter](../13-dev-stack-devops/README.md#anhkysuai-tree-sitter-tree-sitter) cho cây cú pháp tăng dần.
- **Mức kiểm chứng:** `docs-read` — Đọc các phần mô tả và giới hạn trong README, thông báo license, metadata manifest và cấu hình CI khi có; chưa đọc toàn bộ mã triển khai, chưa cài hoặc chạy kiểm thử upstream.
- **Snapshot:** kiểm ngày 2026-11-23; commit `35f98874f935d3e4b98dbbbef9895c5fbc7d9b4c` (2026-11-11T08:49:44Z); 25,018 sao theo GitHub API ngày 2026-11-23. Sao không đại diện chất lượng.
- **Bằng chứng:** [README.md](https://github.com/highlightjs/highlight.js/blob/35f98874f935d3e4b98dbbbef9895c5fbc7d9b4c/README.md) · [LICENSE](https://github.com/highlightjs/highlight.js/blob/35f98874f935d3e4b98dbbbef9895c5fbc7d9b4c/LICENSE) · [package.json](https://github.com/highlightjs/highlight.js/blob/35f98874f935d3e4b98dbbbef9895c5fbc7d9b4c/package.json) · [.github/workflows/tests.js.yml](https://github.com/highlightjs/highlight.js/blob/35f98874f935d3e4b98dbbbef9895c5fbc7d9b4c/.github/workflows/tests.js.yml) · [GitHub API](https://api.github.com/repos/highlightjs/highlight.js).

<a id="anhkysuai-slint-ui-slint"></a>

### Slint

- **Repo:** [slint-ui/slint](https://github.com/slint-ui/slint).
- **Mục đích:** GUI khai báo bằng .slint nối logic Rust, C++, JavaScript hoặc Python.
- **Điểm đáng dùng:** Tách UI khỏi nghiệp vụ, live preview và backend từ desktop/mobile tới embedded giúp dùng chung mô hình giao diện.
- **License:** GPL-3.0-only OR Slint Royalty-free 2.0 OR Commercial; docs/examples MIT.
- **Giới hạn:** Royalty-free có nghĩa vụ công bố sử dụng và loại trừ embedded; embedded đóng cần license thương mại theo LICENSE.md. Từng asset vẫn có điều khoản riêng.
- **Tích hợp:** Chọn giấy phép theo kiểu sản phẩm trước, thử renderer/input và ngân sách bộ nhớ trên thiết bị thật.
- **Đối chiếu:** Qt cho toolkit đa nền; [Iced](../06-ui-ux-design/README.md#anhkysuai-iced-rs-iced) cho GUI Rust; [Flutter](../13-dev-stack-devops/README.md) cho UI ứng dụng.
- **Mức kiểm chứng:** `docs-read` — Đọc các phần mô tả và giới hạn trong README, thông báo license, metadata manifest và cấu hình CI khi có; chưa đọc toàn bộ mã triển khai, chưa cài hoặc chạy kiểm thử upstream.
- **Snapshot:** kiểm ngày 2026-11-23; commit `c924c3042473dcbe33837315da93e6aec6f3195d` (2026-11-23T11:15:41+01:00); 24,685 sao theo GitHub API ngày 2026-11-23. Sao không đại diện chất lượng.
- **Bằng chứng:** [README.md](https://github.com/slint-ui/slint/blob/c924c3042473dcbe33837315da93e6aec6f3195d/README.md) · [LICENSE.md](https://github.com/slint-ui/slint/blob/c924c3042473dcbe33837315da93e6aec6f3195d/LICENSE.md) · [package.json](https://github.com/slint-ui/slint/blob/c924c3042473dcbe33837315da93e6aec6f3195d/package.json) · [Cargo.toml](https://github.com/slint-ui/slint/blob/c924c3042473dcbe33837315da93e6aec6f3195d/Cargo.toml) · [.github/workflows/ci.yaml](https://github.com/slint-ui/slint/blob/c924c3042473dcbe33837315da93e6aec6f3195d/.github/workflows/ci.yaml) · [GitHub API](https://api.github.com/repos/slint-ui/slint).

<a id="anhkysuai-charmbracelet-gum"></a>

### Gum

- **Repo:** [charmbracelet/gum](https://github.com/charmbracelet/gum).
- **Mục đích:** Các lệnh giao diện terminal để ghép vào shell script.
- **Điểm đáng dùng:** choose, input, confirm, filter, table và spin nhận cấu hình qua cờ/biến môi trường, trả kết quả stdout để shell kết hợp.
- **License:** MIT.
- **Giới hạn:** UI tương tác cần TTY và đường hủy/lỗi rõ; đầu ra người dùng phải truyền dưới dạng đối số, không nối thành shell code.
- **Tích hợp:** Dùng cho wizard tạo template, giữ chế độ non-interactive có tham số cho CI và kiểm tra mã thoát khi người dùng hủy.
- **Đối chiếu:** [fzf](../08-awesome-lists-learning/README.md#6c58-editor-terminal--dòng-lệnh) cho chọn tương tác; [Bubble Tea](../06-ui-ux-design/README.md#anhkysuai-charmbracelet-bubbletea) cho TUI Go tùy biến; dialog cho shell UI.
- **Mức kiểm chứng:** `docs-read` — Đọc các phần mô tả và giới hạn trong README, thông báo license, metadata manifest và cấu hình CI khi có; chưa đọc toàn bộ mã triển khai, chưa cài hoặc chạy kiểm thử upstream.
- **Snapshot:** kiểm ngày 2026-11-23; commit `b4a8eceee6552a61d683934ff736b998e3d4c80b` (2026-11-20T14:15:18+04:00); 24,647 sao theo GitHub API ngày 2026-11-23. Sao không đại diện chất lượng.
- **Bằng chứng:** [README.md](https://github.com/charmbracelet/gum/blob/b4a8eceee6552a61d683934ff736b998e3d4c80b/README.md) · [LICENSE](https://github.com/charmbracelet/gum/blob/b4a8eceee6552a61d683934ff736b998e3d4c80b/LICENSE) · [go.mod](https://github.com/charmbracelet/gum/blob/b4a8eceee6552a61d683934ff736b998e3d4c80b/go.mod) · [.github/workflows/build.yml](https://github.com/charmbracelet/gum/blob/b4a8eceee6552a61d683934ff736b998e3d4c80b/.github/workflows/build.yml) · [GitHub API](https://api.github.com/repos/charmbracelet/gum).

<a id="anhkysuai-youzan-vant"></a>

### Vant

- **Repo:** [youzan/vant](https://github.com/youzan/vant).
- **Mục đích:** Bộ UI Vue cho ứng dụng web trên mobile.
- **Điểm đáng dùng:** Theme, tree shaking, i18n, SSR và bộ component mobile giúp dựng mẫu nhanh; tài liệu tách dòng Vue 2 với Vue 3 và các repo mini-program.
- **License:** MIT.
- **Giới hạn:** Accessibility còn cải thiện theo README; claim kích thước/coverage chưa đo, Vant Weapp/Taro không phải cùng package web.
- **Tích hợp:** Khóa major theo Vue/Nuxt, kiểm tra touch, bàn phím ảo, safe area và component cần dùng trên thiết bị mục tiêu.
- **Đối chiếu:** Ionic cho mobile web; [Quasar](../06-ui-ux-design/README.md#anhkysuai-quasarframework-quasar) cho Vue đa target; [Element Plus](../06-ui-ux-design/README.md#anhkysuai-element-plus-element-plus) cho ứng dụng desktop web.
- **Mức kiểm chứng:** `docs-read` — Đọc các phần mô tả và giới hạn trong README, thông báo license, metadata manifest và cấu hình CI khi có; chưa đọc toàn bộ mã triển khai, chưa cài hoặc chạy kiểm thử upstream.
- **Snapshot:** kiểm ngày 2026-11-23; commit `7cc499279866e74b117593abf612567d5a2eb28d` (2026-10-26T10:13:10+08:00); 24,430 sao theo GitHub API ngày 2026-11-23. Sao không đại diện chất lượng.
- **Bằng chứng:** [README.md](https://github.com/youzan/vant/blob/7cc499279866e74b117593abf612567d5a2eb28d/README.md) · [LICENSE](https://github.com/youzan/vant/blob/7cc499279866e74b117593abf612567d5a2eb28d/LICENSE) · [package.json](https://github.com/youzan/vant/blob/7cc499279866e74b117593abf612567d5a2eb28d/package.json) · [.github/workflows/test.yml](https://github.com/youzan/vant/blob/7cc499279866e74b117593abf612567d5a2eb28d/.github/workflows/test.yml) · [GitHub API](https://api.github.com/repos/youzan/vant).

<a id="anhkysuai-electron-react-boilerplate-electron-react-boilerplate"></a>

### Electron React Boilerplate

- **Repo:** [electron-react-boilerplate/electron-react-boilerplate](https://github.com/electron-react-boilerplate/electron-react-boilerplate).
- **Mục đích:** Mẫu ứng dụng desktop Electron/React với build và đóng gói sẵn.
- **Điểm đáng dùng:** Tài liệu hiện dùng electron-vite, tách main/preload/renderer và smoke test IPC; native dependencies ở release/app/package.json.
- **License:** MIT.
- **Giới hạn:** Không áp hướng dẫn webpack/DLL cũ; IPC/preload là ranh giới quyền cần kiểm tra, gói cài và cập nhật phải ký/xác minh riêng.
- **Tích hợp:** Khóa Electron/Node, expose API preload tối thiểu và test gói production trên từng OS trước nhân bản template.
- **Đối chiếu:** Electron Forge cho scaffold; [Tauri](../13-dev-stack-devops/README.md) cho WebView/Rust; [Wails](../13-dev-stack-devops/README.md#anhkysuai-wailsapp-wails) cho Go desktop.
- **Mức kiểm chứng:** `docs-read` — Đọc các phần mô tả và giới hạn trong README, thông báo license, metadata manifest và cấu hình CI khi có; chưa đọc toàn bộ mã triển khai, chưa cài hoặc chạy kiểm thử upstream.
- **Snapshot:** kiểm ngày 2026-11-23; commit `e5b8242d8b21a4290c3a1f18ae3b64167e9de04a` (2026-09-15T14:13:26-07:00); 24,249 sao theo GitHub API ngày 2026-11-23. Sao không đại diện chất lượng.
- **Bằng chứng:** [README.md](https://github.com/electron-react-boilerplate/electron-react-boilerplate/blob/e5b8242d8b21a4290c3a1f18ae3b64167e9de04a/README.md) · [LICENSE](https://github.com/electron-react-boilerplate/electron-react-boilerplate/blob/e5b8242d8b21a4290c3a1f18ae3b64167e9de04a/LICENSE) · [package.json](https://github.com/electron-react-boilerplate/electron-react-boilerplate/blob/e5b8242d8b21a4290c3a1f18ae3b64167e9de04a/package.json) · [.github/workflows/test.yml](https://github.com/electron-react-boilerplate/electron-react-boilerplate/blob/e5b8242d8b21a4290c3a1f18ae3b64167e9de04a/.github/workflows/test.yml) · [GitHub API](https://api.github.com/repos/electron-react-boilerplate/electron-react-boilerplate).

<a id="anhkysuai-pure-css-pure"></a>

### Pure CSS

**Repo:** [pure-css/pure](https://github.com/pure-css/pure) · **License:** BSD-3-Clause; thành phần nền có thông báo riêng · **Kiểm:** 2026-11-23, `docs-read`, [`ba73c847bc29`](https://github.com/pure-css/pure/tree/ba73c847bc297fec8489907aff58b4ee3abf59ab) (commit 2026-11-19). **Sao:** 23,717 tại 2026-11-23 theo [GitHub API](https://api.github.com/repos/pure-css/pure).

| Mục | Đánh giá |
|---|---|
| Mục đích | Bộ module CSS nhỏ cho grid, form, button, menu và table responsive. |
| Giá trị và cơ chế theo tài liệu | README mô tả nền Normalize.css, tách core/non-responsive/module build; package 3.1.0 và CI lint/test cho phép chỉ lấy phần giao diện cần dùng. |
| Giới hạn | Kích thước 3.7KB là số upstream, chưa đo bundle tích hợp. CSS cung cấp kiểu dáng, không tự tạo hành vi tương tác hay accessibility của menu/form. |
| Điều kiện tích hợp | Chọn module và breakpoint phù hợp, thử keyboard/focus/contrast với nội dung thật; giữ style tùy chỉnh có phạm vi và kiểm browser mục tiêu trước dùng toàn site. |
| Lựa chọn đối chiếu | [Bootstrap](../08-awesome-lists-learning/README.md#6c522-thư-viện-giao-diện--css); Bulma; Pico CSS. |

**Phạm vi bằng chứng:** đã clone, đọc trích đoạn tài liệu, giấy phép và các file cấu hình được dẫn dưới đây; chưa chạy mã, build, benchmark hoặc test upstream. `docs-read` không phải kiểm chứng implementation.

**Nguồn tại cùng SHA:** [README.md](https://github.com/pure-css/pure/blob/ba73c847bc297fec8489907aff58b4ee3abf59ab/README.md) · [LICENSE](https://github.com/pure-css/pure/blob/ba73c847bc297fec8489907aff58b4ee3abf59ab/LICENSE) · [package.json](https://github.com/pure-css/pure/blob/ba73c847bc297fec8489907aff58b4ee3abf59ab/package.json) · [composer.json](https://github.com/pure-css/pure/blob/ba73c847bc297fec8489907aff58b4ee3abf59ab/composer.json) · [.github/workflows/test.yml](https://github.com/pure-css/pure/blob/ba73c847bc297fec8489907aff58b4ee3abf59ab/.github/workflows/test.yml).

<a id="anhkysuai-svg-svgo"></a>

### SVGO

**Repo:** [svg/svgo](https://github.com/svg/svgo) · **License:** MIT · **Kiểm:** 2026-11-23, `docs-read`, [`31194fb4b3b5`](https://github.com/svg/svgo/tree/31194fb4b3b592d7a65956f8f3b343b9fd6b80a6) (commit 2026-11-07). **Sao:** 22,838 tại 2026-11-23 theo [GitHub API](https://api.github.com/repos/svg/svgo).

| Mục | Đánh giá |
|---|---|
| Mục đích | Tối ưu SVG qua thư viện Node.js hoặc CLI, phù hợp pipeline icon và tài sản giao diện. |
| Giá trị và cơ chế theo tài liệu | README mô tả plugin, preset và cấu hình svgo.config.mjs; manifest 4.1.0 có build bundle, kiểm kiểu và regression script. Có thể chuẩn hóa bước nén asset trước phát hành. |
| Giới hạn | Chưa đo mức giảm dung lượng hoặc kiểm so sánh hình ảnh. Thay đổi metadata, ID và cấu trúc SVG cần thử trên icon có CSS, animation, liên kết và accessibility. |
| Điều kiện tích hợp | Khóa phiên bản, giữ bản gốc và cấu hình plugin trong repo; chạy so sánh hình ảnh cùng kiểm ID được tham chiếu trước khi thay toàn bộ asset. |
| Lựa chọn đối chiếu | SVGOMG; Scour; oxipng. |

**Phạm vi bằng chứng:** đã clone, đọc trích đoạn tài liệu, giấy phép và các file cấu hình được dẫn dưới đây; chưa chạy mã, build, benchmark hoặc test upstream. `docs-read` không phải kiểm chứng implementation.

**Nguồn tại cùng SHA:** [README.md](https://github.com/svg/svgo/blob/31194fb4b3b592d7a65956f8f3b343b9fd6b80a6/README.md) · [LICENSE](https://github.com/svg/svgo/blob/31194fb4b3b592d7a65956f8f3b343b9fd6b80a6/LICENSE) · [package.json](https://github.com/svg/svgo/blob/31194fb4b3b592d7a65956f8f3b343b9fd6b80a6/package.json) · [.github/workflows/ci.yml](https://github.com/svg/svgo/blob/31194fb4b3b592d7a65956f8f3b343b9fd6b80a6/.github/workflows/ci.yml).

<a id="anhkysuai-tabler-tabler-icons"></a>

### Tabler Icons

**Repo:** [tabler/tabler-icons](https://github.com/tabler/tabler-icons) · **License:** MIT · **Kiểm:** 2026-11-23, `docs-read`, [`85e870dbe868`](https://github.com/tabler/tabler-icons/tree/85e870dbe8680c2d6deefd062122d30ef1544a41) (commit 2026-11-16). **Sao:** 22,769 tại 2026-11-23 theo [GitHub API](https://api.github.com/repos/tabler/tabler-icons).

| Mục | Đánh giá |
|---|---|
| Mục đích | Bộ SVG icon outline và filled cho web, có các gói theo framework và định dạng. |
| Giá trị và cơ chế theo tài liệu | README tại SHA kiểm ghi 6.545 icon, lưới 24×24 và nét 2px; cung cấp SVG, sprite, webfont, React và React Native. Manifest và CI có bước validate, optimize và build gói. |
| Giới hạn | Số lượng là số upstream công bố tại snapshot, chưa đếm độc lập. Không suy diễn mọi biểu tượng tự có nhãn truy cập hoặc mọi hình thức import đều tối ưu bundle. |
| Điều kiện tích hợp | Chọn một kiểu nét và tập icon nhất quán; import có chọn lọc, bổ sung nhãn cho nút chỉ có icon và giữ thông báo MIT khi phân phối. |
| Lựa chọn đối chiếu | Lucide; Heroicons; Phosphor Icons. |

**Phạm vi bằng chứng:** đã clone, đọc trích đoạn tài liệu, giấy phép và các file cấu hình được dẫn dưới đây; chưa chạy mã, build, benchmark hoặc test upstream. `docs-read` không phải kiểm chứng implementation.

**Nguồn tại cùng SHA:** [README.md](https://github.com/tabler/tabler-icons/blob/85e870dbe8680c2d6deefd062122d30ef1544a41/README.md) · [LICENSE](https://github.com/tabler/tabler-icons/blob/85e870dbe8680c2d6deefd062122d30ef1544a41/LICENSE) · [package.json](https://github.com/tabler/tabler-icons/blob/85e870dbe8680c2d6deefd062122d30ef1544a41/package.json) · [.github/workflows/build.yml](https://github.com/tabler/tabler-icons/blob/85e870dbe8680c2d6deefd062122d30ef1544a41/.github/workflows/build.yml).

<a id="anhkysuai-react-grid-layout-react-grid-layout"></a>

### React-Grid-Layout

**Repo:** [react-grid-layout/react-grid-layout](https://github.com/react-grid-layout/react-grid-layout) · **License:** MIT · **Kiểm:** 2026-11-23, `docs-read`, [`ec4ab79c9744`](https://github.com/react-grid-layout/react-grid-layout/tree/ec4ab79c97448947b04601c2237b2861d94a0fcb) (commit 2026-11-18). **Sao:** 22,501 tại 2026-11-23 theo [GitHub API](https://api.github.com/repos/react-grid-layout/react-grid-layout).

| Mục | Đánh giá |
|---|---|
| Mục đích | Lưới dashboard React cho phép kéo, đổi kích thước và lưu layout theo breakpoint. |
| Giá trị và cơ chế theo tài liệu | README v2 mô tả bản viết lại TypeScript, hooks đo container và compactor tùy biến; manifest 2.3.0 cùng CI có unit test, build và kiểm ngân sách số phép tính. |
| Giới hạn | API mới thay đổi kiểu và cấu hình; legacy wrapper là lộ trình chuyển đổi do upstream công bố, chưa được kiểm độc lập. width là prop bắt buộc; chưa thử bàn phím, chạm hoặc hiệu năng dashboard lớn. |
| Điều kiện tích hợp | Lưu layout có phiên bản, dùng useContainerWidth hoặc ResizeObserver; thử resize và khôi phục bố cục ở nhiều breakpoint, cung cấp thao tác thay thế cho người không kéo thả. |
| Lựa chọn đối chiếu | GridStack; dnd-kit; CSS Grid. |

**Phạm vi bằng chứng:** đã clone, đọc trích đoạn tài liệu, giấy phép và các file cấu hình được dẫn dưới đây; chưa chạy mã, build, benchmark hoặc test upstream. `docs-read` không phải kiểm chứng implementation.

**Nguồn tại cùng SHA:** [README.md](https://github.com/react-grid-layout/react-grid-layout/blob/ec4ab79c97448947b04601c2237b2861d94a0fcb/README.md) · [LICENSE](https://github.com/react-grid-layout/react-grid-layout/blob/ec4ab79c97448947b04601c2237b2861d94a0fcb/LICENSE) · [package.json](https://github.com/react-grid-layout/react-grid-layout/blob/ec4ab79c97448947b04601c2237b2861d94a0fcb/package.json) · [.github/workflows/test.yml](https://github.com/react-grid-layout/react-grid-layout/blob/ec4ab79c97448947b04601c2237b2861d94a0fcb/.github/workflows/test.yml).

<a id="anhkysuai-palantir-blueprint"></a>

### Blueprint

**Repo:** [palantir/blueprint](https://github.com/palantir/blueprint) · **License:** Apache-2.0 · **Kiểm:** 2026-11-23, `docs-read`, [`75a8495a8c56`](https://github.com/palantir/blueprint/tree/75a8495a8c5654cc5bf6c93c08dc1778cb5a0098) (commit 2026-11-20). **Sao:** 22,228 tại 2026-11-23 theo [GitHub API](https://api.github.com/repos/palantir/blueprint).

| Mục | Đánh giá |
|---|---|
| Mục đích | Bộ component React hướng tới ứng dụng desktop trên trình duyệt với giao diện nhiều dữ liệu. |
| Giá trị và cơ chế theo tài liệu | README tách core, colors, icons, select, datetime và bảng kiểu spreadsheet; có docs app và ví dụ React. Phù hợp console quản trị hoặc công cụ phân tích cần hệ thống thành phần thống nhất. |
| Giới hạn | Upstream nói rõ không ưu tiên mobile. Manifest gốc 0.0.0 là monorepo, không phải bản component; workflow được đọc chỉ tạo bình luận preview nên chưa chứng minh chất lượng kiểm thử UI. |
| Điều kiện tích hợp | Chọn gói thực sự cần, kiểm phiên bản React, theme và tải icon/CSS; thử bảng lớn, bàn phím, độ tương phản và bố cục trên màn hình mục tiêu. |
| Lựa chọn đối chiếu | Ant Design; MUI; Mantine. |

**Phạm vi bằng chứng:** đã clone, đọc trích đoạn tài liệu, giấy phép và các file cấu hình được dẫn dưới đây; chưa chạy mã, build, benchmark hoặc test upstream. `docs-read` không phải kiểm chứng implementation.

**Nguồn tại cùng SHA:** [README.md](https://github.com/palantir/blueprint/blob/75a8495a8c5654cc5bf6c93c08dc1778cb5a0098/README.md) · [LICENSE](https://github.com/palantir/blueprint/blob/75a8495a8c5654cc5bf6c93c08dc1778cb5a0098/LICENSE) · [package.json](https://github.com/palantir/blueprint/blob/75a8495a8c5654cc5bf6c93c08dc1778cb5a0098/package.json) · [.github/workflows/preview-comment.yml](https://github.com/palantir/blueprint/blob/75a8495a8c5654cc5bf6c93c08dc1778cb5a0098/.github/workflows/preview-comment.yml).

<a id="anhkysuai-colorlibhq-gentelella"></a>

### Gentelella

**Repo:** [ColorlibHQ/gentelella](https://github.com/ColorlibHQ/gentelella) · **License:** MIT · **Kiểm:** 2026-11-23, `docs-read`, [`3f9d772dfb21`](https://github.com/ColorlibHQ/gentelella/tree/3f9d772dfb21c7a4cd886222db7e1bd018a5a2f0) (commit 2026-11-17). **Sao:** 21,571 tại 2026-11-23 theo [GitHub API](https://api.github.com/repos/ColorlibHQ/gentelella).

| Mục | Đánh giá |
|---|---|
| Mục đích | Mẫu dashboard quản trị HTML để khởi tạo giao diện SaaS, CRM hoặc công cụ nội bộ. |
| Giá trị và cơ chế theo tài liệu | Snapshot v4.2.2 dùng vanilla JavaScript, SCSS và Vite 8; README mô tả trang mẫu, ECharts, kanban, inbox, theme và PWA. Workflow build/lint rồi xuất GitHub Pages. |
| Giới hạn | Khác nền Bootstrap/jQuery của các bản cũ; số trang và nhãn production-ready là mô tả upstream, chưa kiểm độc lập. UI mẫu không cung cấp sẵn backend, phân quyền hoặc dữ liệu nghiệp vụ. |
| Điều kiện tích hợp | Tách dữ liệu demo, ghép API và xác thực của sản phẩm; kiểm form, accessibility, đường dẫn tài sản và service worker. Khóa bản trước tùy chỉnh theme để dễ nâng cấp. |
| Lựa chọn đối chiếu | Tabler; AdminLTE; CoreUI. |

**Phạm vi bằng chứng:** đã clone, đọc trích đoạn tài liệu, giấy phép và các file cấu hình được dẫn dưới đây; chưa chạy mã, build, benchmark hoặc test upstream. `docs-read` không phải kiểm chứng implementation.

**Nguồn tại cùng SHA:** [README.md](https://github.com/ColorlibHQ/gentelella/blob/3f9d772dfb21c7a4cd886222db7e1bd018a5a2f0/README.md) · [LICENSE.txt](https://github.com/ColorlibHQ/gentelella/blob/3f9d772dfb21c7a4cd886222db7e1bd018a5a2f0/LICENSE.txt) · [package.json](https://github.com/ColorlibHQ/gentelella/blob/3f9d772dfb21c7a4cd886222db7e1bd018a5a2f0/package.json) · [.github/workflows/deploy-pages.yml](https://github.com/ColorlibHQ/gentelella/blob/3f9d772dfb21c7a4cd886222db7e1bd018a5a2f0/.github/workflows/deploy-pages.yml).

<a id="anhkysuai-xtermjs-xterm.js"></a>

### xterm.js

**Repo:** [xtermjs/xterm.js](https://github.com/xtermjs/xterm.js) · **License:** MIT · **Kiểm:** 2026-11-23, `docs-read`, [`eefaadc7787f`](https://github.com/xtermjs/xterm.js/tree/eefaadc7787f5b1c95c22867d02e4074e91f93c9) (commit 2026-11-21). **Sao:** 21,384 tại 2026-11-23 theo [GitHub API](https://api.github.com/repos/xtermjs/xterm.js).

| Mục | Đánh giá |
|---|---|
| Mục đích | Component terminal chạy trong trình duyệt cho IDE web, console máy chủ hoặc công cụ điều khiển từ xa. |
| Giá trị và cơ chế theo tài liệu | README mô tả Unicode/CJK, IME, addon, renderer GPU tùy chọn và chế độ screen reader; gói @xterm/xterm 6.0.0 có build TypeScript cùng CI tạo artifact. |
| Giới hạn | Đây là phần hiển thị terminal, không phải shell hay backend PTY. Chưa thử khả năng tương thích ứng dụng terminal, hiệu năng scrollback hoặc accessibility; quyền chạy lệnh thuộc kiến trúc server. |
| Điều kiện tích hợp | Ghép PTY qua kênh đã xác thực, giới hạn phiên và quyền hệ điều hành; kiểm resize, Unicode, copy/paste, link và mất kết nối, bật chế độ truy cập phù hợp. |
| Lựa chọn đối chiếu | Ghostty; hterm; ttyd. |

**Phạm vi bằng chứng:** đã clone, đọc trích đoạn tài liệu, giấy phép và các file cấu hình được dẫn dưới đây; chưa chạy mã, build, benchmark hoặc test upstream. `docs-read` không phải kiểm chứng implementation.

**Nguồn tại cùng SHA:** [README.md](https://github.com/xtermjs/xterm.js/blob/eefaadc7787f5b1c95c22867d02e4074e91f93c9/README.md) · [LICENSE](https://github.com/xtermjs/xterm.js/blob/eefaadc7787f5b1c95c22867d02e4074e91f93c9/LICENSE) · [package.json](https://github.com/xtermjs/xterm.js/blob/eefaadc7787f5b1c95c22867d02e4074e91f93c9/package.json) · [.github/workflows/ci.yml](https://github.com/xtermjs/xterm.js/blob/eefaadc7787f5b1c95c22867d02e4074e91f93c9/.github/workflows/ci.yml).

<a id="anhkysuai-longbridge-gpui-kit"></a>

### GPUI Kit

**Repo:** [longbridge/gpui-kit](https://github.com/longbridge/gpui-kit) · **License:** Apache-2.0 cho mã; văn bản và minh họa đủ quyền trong docs còn có lựa chọn CC-BY-4.0 · **Kiểm:** 2026-11-23, `docs-read`, [`48e53b11762a`](https://github.com/longbridge/gpui-kit/tree/48e53b11762a7ac37835acca889a924c569ff681) (commit 2026-11-23). **Sao:** 21,217 tại 2026-11-23 theo [GitHub API](https://api.github.com/repos/longbridge/gpui-kit).

| Mục | Đánh giá |
|---|---|
| Mục đích | Framework component desktop Rust trên GPUI, có lớp hành vi nền, giao diện có style và gói ghép ứng dụng. |
| Giá trị và cơ chế theo tài liệu | README phân tách gpui-kit, gpui-base và gpui-component; gói kit khóa GPUI tương ứng, có WASM, AccessKit và runtime extension JavaScript tùy chọn. CI kiểm pin, dependency và tài liệu recipe. |
| Giới hạn | Tuyên bố production-ready và hơn 75 component là từ upstream, chưa chạy ứng dụng. License CC-BY bổ sung chỉ áp dụng tài liệu đủ quyền, không đổi license mã, snippet hoặc tài sản bên thứ ba. |
| Điều kiện tích hợp | Khóa đúng bộ crate và GPUI, làm prototype trên từng hệ điều hành; kiểm input, accessibility, font và đóng gói, chỉ bật runtime extension khi có chính sách quyền phù hợp. |
| Lựa chọn đối chiếu | Slint; Iced; egui. |

**Phạm vi bằng chứng:** đã clone, đọc trích đoạn tài liệu, giấy phép và các file cấu hình được dẫn dưới đây; chưa chạy mã, build, benchmark hoặc test upstream. `docs-read` không phải kiểm chứng implementation.

**Nguồn tại cùng SHA:** [README.md](https://github.com/longbridge/gpui-kit/blob/48e53b11762a7ac37835acca889a924c569ff681/README.md) · [LICENSE-APACHE](https://github.com/longbridge/gpui-kit/blob/48e53b11762a7ac37835acca889a924c569ff681/LICENSE-APACHE) · [LICENSE-DOCS.md](https://github.com/longbridge/gpui-kit/blob/48e53b11762a7ac37835acca889a924c569ff681/LICENSE-DOCS.md) · [Cargo.toml](https://github.com/longbridge/gpui-kit/blob/48e53b11762a7ac37835acca889a924c569ff681/Cargo.toml) · [.github/workflows/ci.yml](https://github.com/longbridge/gpui-kit/blob/48e53b11762a7ac37835acca889a924c569ff681/.github/workflows/ci.yml).

<a id="anhkysuai-basecamp-trix"></a>

### Trix

**Repo:** [basecamp/trix](https://github.com/basecamp/trix) · **License:** MIT · **Kiểm:** 2026-11-23, `docs-read`, [`e2df97a56bcf`](https://github.com/basecamp/trix/tree/e2df97a56bcf1b6689ccd08d0d11a3f96006da8b) (commit 2026-10-09). **Sao:** 20,014 tại 2026-11-23 theo [GitHub API](https://api.github.com/repos/basecamp/trix).

| Mục | Đánh giá |
|---|---|
| Mục đích | Rich text editor cho bài viết, bình luận và tin nhắn, dùng document model nội bộ và xuất HTML. |
| Giá trị và cơ chế theo tài liệu | README mô tả custom element, thao tác chỉnh sửa và attachment; manifest 2.1.19 có build Rollup/Sass, browser test. Ứng dụng tự upload tệp rồi cấp URL bền vững cho attachment. |
| Giới hạn | README cảnh báo HTML không tin cậy đặt trực tiếp trong trix-editor có thể được browser thực thi trước sanitizer. Editor không cung cấp sẵn lưu trữ hoặc chính sách bảo mật tệp; chưa thử trình duyệt/IME. |
| Điều kiện tích hợp | Khởi tạo nội dung qua hidden input đã escape hoặc gán value bằng DOM, kiểm HTML phía server và quyền URL attachment; thử paste, upload lỗi, undo và nội dung dài. |
| Lựa chọn đối chiếu | Tiptap; Lexical; ProseMirror. |

**Phạm vi bằng chứng:** đã clone, đọc trích đoạn tài liệu, giấy phép và các file cấu hình được dẫn dưới đây; chưa chạy mã, build, benchmark hoặc test upstream. `docs-read` không phải kiểm chứng implementation.

**Nguồn tại cùng SHA:** [README.md](https://github.com/basecamp/trix/blob/e2df97a56bcf1b6689ccd08d0d11a3f96006da8b/README.md) · [LICENSE](https://github.com/basecamp/trix/blob/e2df97a56bcf1b6689ccd08d0d11a3f96006da8b/LICENSE) · [package.json](https://github.com/basecamp/trix/blob/e2df97a56bcf1b6689ccd08d0d11a3f96006da8b/package.json) · [.github/workflows/ci.yml](https://github.com/basecamp/trix/blob/e2df97a56bcf1b6689ccd08d0d11a3f96006da8b/.github/workflows/ci.yml).

<a id="anhkysuai-2026-11-23-storytold-artcraft"></a>

### artcraft

**Repo:** [storytold/artcraft](https://github.com/storytold/artcraft) · **License:** MIT OR Apache-2.0 · **★ 42,033 (GitHub API, 2026-11-23)**

**Mục đích:** Môi trường sáng tạo ảnh/video AI có bố cục 2D, dựng cảnh 3D và lựa chọn nhiều mô hình.

**Giá trị:** Chuyển từ prompt đơn thuần sang kiểm soát cảnh, thành phần và góc nhìn; hữu ích tham khảo thiết kế công cụ sáng tạo.

**Giới hạn:** Mã MIT hoặc Apache-2.0 không bao gồm mọi model, tài sản hay dịch vụ được nối; chi phí và quyền đầu ra phải kiểm theo nhà cung cấp.

**Cách tham khảo/tích hợp:** Đối chiếu phạm vi và giấy phép, thử một ca nhỏ có kết quả mong đợi trước khi nhúng vào dự án.

**Lựa chọn để đối chiếu:** [OpenMontageInc/OpenMontage](https://github.com/OpenMontageInc/OpenMontage) · [pixijs/pixijs](https://github.com/pixijs/pixijs). Đây là ứng viên so sánh theo tác vụ; mức phù hợp cần kiểm theo hồ sơ và phiên bản riêng.

**Bằng chứng:** `docs-read`, ngày 2026-11-23, commit [`de571bb2f8351ade6c742d41caea81f11f595801`](https://github.com/storytold/artcraft/commit/de571bb2f8351ade6c742d41caea81f11f595801), ngày commit 2026-11-20. Đã clone và đọc chọn lọc phần giới thiệu, cách dùng, giới hạn, license, metadata manifest và CI hiện diện. Chưa kiểm đầy đủ implementation hoặc chạy upstream; các số đo của tác giả chưa được tái lập.

**Nguồn:** [README.md](https://github.com/storytold/artcraft/blob/de571bb2f8351ade6c742d41caea81f11f595801/README.md) · [LICENSE-APACHE](https://github.com/storytold/artcraft/blob/de571bb2f8351ade6c742d41caea81f11f595801/LICENSE-APACHE) · [LICENSE-MIT](https://github.com/storytold/artcraft/blob/de571bb2f8351ade6c742d41caea81f11f595801/LICENSE-MIT) · [Cargo.toml](https://github.com/storytold/artcraft/blob/de571bb2f8351ade6c742d41caea81f11f595801/Cargo.toml) · [.github/workflows/freebsd.yml](https://github.com/storytold/artcraft/blob/de571bb2f8351ade6c742d41caea81f11f595801/.github/workflows/freebsd.yml) · [metadata GitHub](https://api.github.com/repos/storytold/artcraft).

<a id="anhkysuai-2026-11-23-date-fns-date-fns"></a>

### date-fns

**Repo:** [date-fns/date-fns](https://github.com/date-fns/date-fns) · **License:** MIT (tuyên bố README; từng package kiểm riêng) · **★ 36,661 (GitHub API, 2026-11-23)**

**Mục đích:** Thư viện TypeScript/JavaScript thao tác ngày theo hàm nhỏ, hỗ trợ locale và múi giờ.

**Giá trị:** Dùng native Date và hàm không sửa dữ liệu đầu vào theo tài liệu, thuận tiện chọn chức năng cần thiết.

**Giới hạn:** Không lấy MIT của riêng pkgs/tz để suy toàn bộ; README dự án cũng khai báo MIT. Cần kiểm parsing, DST, locale và múi giờ bằng ví dụ thực của ứng dụng.

**Cách tham khảo/tích hợp:** Ghim phiên bản và kiểm ví dụ nhỏ với framework/trình duyệt đích, gồm accessibility, tải dữ liệu và các trường hợp biên.

**Lựa chọn để đối chiếu:** [iamkun/dayjs](https://github.com/iamkun/dayjs) · [moment/luxon](https://github.com/moment/luxon). Đây là ứng viên so sánh theo tác vụ; mức phù hợp cần kiểm theo hồ sơ và phiên bản riêng.

**Bằng chứng:** `docs-read`, ngày 2026-11-23, commit [`a9739fb3e5384a810e90d7376446f6d84ecc5029`](https://github.com/date-fns/date-fns/commit/a9739fb3e5384a810e90d7376446f6d84ecc5029), ngày commit 2026-10-24. Đã clone và đọc chọn lọc phần giới thiệu, cách dùng, giới hạn, license, metadata manifest và CI hiện diện. Chưa kiểm đầy đủ implementation hoặc chạy upstream; các số đo của tác giả chưa được tái lập.

**Nguồn:** [README.md](https://github.com/date-fns/date-fns/blob/a9739fb3e5384a810e90d7376446f6d84ecc5029/README.md) · [pkgs/tz/LICENSE.md](https://github.com/date-fns/date-fns/blob/a9739fb3e5384a810e90d7376446f6d84ecc5029/pkgs/tz/LICENSE.md) · [package.json](https://github.com/date-fns/date-fns/blob/a9739fb3e5384a810e90d7376446f6d84ecc5029/package.json) · [.github/workflows/tz_tests.yaml](https://github.com/date-fns/date-fns/blob/a9739fb3e5384a810e90d7376446f6d84ecc5029/.github/workflows/tz_tests.yaml) · [metadata GitHub](https://api.github.com/repos/date-fns/date-fns).

<a id="chuyen-muc-2026-11-23"></a>

## Hồ sơ chuyển về từ mục khác — 23/11/2026

10 hồ sơ được chuyển khi chia lại catalog theo `data/taxonomy.json`. Nội dung, ngày kiểm và mức bằng chứng giữ nguyên như ở mục gốc.

<a id="chuyen-handsontable"></a>

### handsontable

`handsontable/handsontable` · License: Giấy phép riêng của Handsoncode · ★ 22.084 · docs-read · 2026-11-18

Thành phần lưới dữ liệu JavaScript giao diện giống bảng tính, dùng với JavaScript/TypeScript, React, Angular, Vue để nhập, sửa, kiểm hợp lệ và xử lý dữ liệu. README liệt kê khoảng 400 công thức dựng sẵn, ảo hoá hàng, lọc, sắp xếp, định dạng có điều kiện; hỗ trợ IME, đa ngôn ngữ, RTL và nhắm WCAG 2.2 AA; có wrapper React, Angular, Vue3 trong thư mục wrappers. Điều kiện: Cần khoá giấy phép (licenseKey); dùng thương mại phải mua giấy phép; bản dùng thử chỉ để đánh giá ngoài production, hết hạn thì lưới bị chặn; dự án phi thương mại phải xin giấy phép miễn phí; đóng góp cần ký CLA. ★ 18/11/2026: 22.084 (GitHub search API), nhóm "Framework Frontend" trong kho-repo của Phan Đông Giang, mục 08 §6c.5

**Hồ sơ gốc:** [mục 08](../08-awesome-lists-learning/README.md#6c510-framework-frontend) (bảng/đoạn chung, giữ nguyên tại chỗ).

<a id="chuyen-react-pdf"></a>

### react-pdf

`diegomura/react-pdf` · License: MIT · ★ 16.858 · docs-read · 2026-11-18

Trình render React để tạo file PDF trên trình duyệt và máy chủ bằng các thành phần Document, Page, View, Text. Render được trong DOM qua PDFViewer và ghi file trên Node qua ReactPDF.render; có StyleSheet kiểu flexbox; monorepo nhiều gói trong packages, phát hành gói @react-pdf/renderer. ★ 18/11/2026: 16.858 (GitHub search API), nhóm "Framework Frontend" trong kho-repo của Phan Đông Giang, mục 08 §6c.5

**Hồ sơ gốc:** [mục 08](../08-awesome-lists-learning/README.md#6c510-framework-frontend) (bảng/đoạn chung, giữ nguyên tại chỗ).

<a id="chuyen-plate"></a>

### plate

`udecode/plate` · License: MIT · ★ 16.712 · docs-read · 2026-11-18

Framework trình soạn thảo văn bản giàu định dạng (rich-text) cho React, kèm các mẫu khởi đầu và tài liệu tại platejs.org. Có mẫu playground có AI và mẫu tối giản; repo chứa gói platejs, plitejs (runtime lõi mô hình tài liệu, giao dịch) và cli; có tài liệu tiếng Trung trong tooling/cn. Điều kiện: Mẫu Notion-like (Potion) có backend nằm ở pro.platejs.org, chưa xác minh điều kiện sử dụng. ★ 18/11/2026: 16.712 (GitHub search API), nhóm "Framework Frontend" trong kho-repo của Phan Đông Giang, mục 08 §6c.5

**Hồ sơ gốc:** [mục 08](../08-awesome-lists-learning/README.md#6c510-framework-frontend) (bảng/đoạn chung, giữ nguyên tại chỗ).

<a id="chuyen-bootstrap"></a>

### bootstrap

`twbs/bootstrap` · License: MIT License · ★ 175.080 · docs-read · 2026-11-18

Framework front-end CSS/JS để dựng giao diện web responsive nhanh. Phát hành qua npm, yarn, Bun, Composer, NuGet; có test JS, coverage và OpenSSF Scorecard trong README; nhánh v5-dev duy trì Bootstrap 5. Điều kiện: Nhánh mặc định đang phát triển Bootstrap 6 (bản 6.0.0-alpha.1); bản ổn định Bootstrap 5 ở nhánh v5-dev. ★ 18/11/2026: 175.080 (GitHub search API), nhóm "Thư viện giao diện & CSS" trong kho-repo của Phan Đông Giang, mục 08 §6c.5

**Hồ sơ gốc:** [mục 08](../08-awesome-lists-learning/README.md#6c522-thư-viện-giao-diện--css) (bảng/đoạn chung, giữ nguyên tại chỗ).

<a id="chuyen-font-awesome"></a>

### Font-Awesome

`FortAwesome/Font-Awesome` · License: Font Awesome Free License · ★ 77.044 · docs-read · 2026-11-18

Bộ icon và toolkit Font Awesome bản Free (phiên bản 7), cung cấp SVG, webfont, CSS/SCSS và gói JS. Bản 7 hiện hành, bản 6 là LTS chỉ vá lỗi nghiêm trọng; có khoảng 2000 icon SVG nhóm solid cùng nhóm regular và brands; phát hành theo SemVer có ghi chú nâng cấp UPGRADING.md. Điều kiện: Bắt buộc ghi công theo CC BY/OFL/MIT (chú thích có sẵn trong file, không được gỡ); chỉ phần Free, bản Pro cần giấy phép trả phí. ★ 18/11/2026: 77.044 (GitHub search API), nhóm "Thư viện giao diện & CSS" trong kho-repo của Phan Đông Giang, mục 08 §6c.5

**Hồ sơ gốc:** [mục 08](../08-awesome-lists-learning/README.md#6c522-thư-viện-giao-diện--css) (bảng/đoạn chung, giữ nguyên tại chỗ).

<a id="chuyen-carbon-app-carbon"></a>

### carbon-app/carbon

`carbon-app/carbon` · License: MIT · ★ 36.148 · docs-read · 2026-11-18

Ứng dụng web (carbon.now.sh) tạo ảnh đẹp từ mã nguồn để chia sẻ, tuỳ chỉnh theme, font, nền. Xuất ảnh PNG và SVG, nhúng snippet qua carbon.now.sh/embed; nhập mã bằng kéo thả file hoặc ID GitHub gist; README có hơn 20 bản dịch. Điều kiện: Lưu snippet cần tạo tài khoản. ★ 18/11/2026: 36.148 (GitHub search API), nhóm "Thư viện giao diện & CSS" trong kho-repo của Phan Đông Giang, mục 08 §6c.5

**Hồ sơ gốc:** [mục 08](../08-awesome-lists-learning/README.md#6c522-thư-viện-giao-diện--css) (bảng/đoạn chung, giữ nguyên tại chỗ).

<a id="chuyen-d3"></a>

### d3

`d3/d3` · License: ISC · ★ 113.955 · docs-read · 2026-11-18

Thư viện JavaScript mã nguồn mở cấp thấp để trực quan hoá dữ liệu trên nền chuẩn web. Phiên bản 7.9.2 trong package.json; tài liệu tại d3js.org và thư viện ví dụ trên Observable; dùng được qua npm hoặc CDN ESM. ★ 18/11/2026: 113.955 (GitHub search API), nhóm "Đồ họa, 3D & Sơ đồ" trong kho-repo của Phan Đông Giang, mục 08 §6c.5

**Hồ sơ gốc:** [mục 08](../08-awesome-lists-learning/README.md#6c527-đồ-họa-3d--sơ-đồ) (bảng/đoạn chung, giữ nguyên tại chỗ).

<a id="chuyen-drawdb"></a>

### drawdb

`drawdb-io/drawdb` · License: GNU AGPL v3 · ★ 40.335 · docs-read · 2026-11-18

Trình soạn sơ đồ quan hệ thực thể (ERD) cơ sở dữ liệu chạy trên trình duyệt, sinh và nhập/xuất script SQL. Dùng không cần tạo tài khoản; xuất/nhập SQL và sinh migration; có Dockerfile và ảnh ghcr.io/drawdb-io/drawdb. Điều kiện: Tính năng chia sẻ cần tự dựng drawdb-server; AGPLv3 buộc công bố mã khi cung cấp bản sửa qua mạng. ★ 18/11/2026: 40.335 (GitHub search API), nhóm "Đồ họa, 3D & Sơ đồ" trong kho-repo của Phan Đông Giang, mục 08 §6c.5

**Hồ sơ gốc:** [mục 08](../08-awesome-lists-learning/README.md#6c527-đồ-họa-3d--sơ-đồ) (bảng/đoạn chung, giữ nguyên tại chỗ).

<a id="chuyen-next-ai-draw-io"></a>

### next-ai-draw-io

`DayuanJiang/next-ai-draw-io` · License: Apache License 2.0 · ★ 37.029 · docs-read · 2026-11-18

Ứng dụng vẽ và sửa sơ đồ draw.io bằng cách trò chuyện với AI; có bản web, desktop và MCP server cho agent. Hỗ trợ 25 nhà cung cấp mô hình kể cả preset tương thích OpenAI; mỗi thay đổi của AI là một phiên bản so sánh, khôi phục, hoàn tác được; xuất .drawio, .png, .svg. Điều kiện: Cần API key nhà cung cấp mô hình AI (mặc định AWS Bedrock); bản demo trực tuyến có giới hạn sử dụng. ★ 18/11/2026: 37.029 (GitHub search API), nhóm "Đồ họa, 3D & Sơ đồ" trong kho-repo của Phan Đông Giang, mục 08 §6c.5

**Hồ sơ gốc:** [mục 08](../08-awesome-lists-learning/README.md#6c527-đồ-họa-3d--sơ-đồ) (bảng/đoạn chung, giữ nguyên tại chỗ).

<a id="chuyen-drawnix"></a>

### drawnix

`plait-board/drawnix` · License: MIT · ★ 15.080 · docs-read · 2026-11-18

Bảng trắng mã nguồn mở tất cả trong một: sơ đồ tư duy, lưu đồ, vẽ tay trên canvas vô hạn, xây trên framework Plait. Chuyển cú pháp Mermaid thành lưu đồ và Markdown thành sơ đồ tư duy; xuất PNG, JPG, JSON và tự lưu vào bộ nhớ trình duyệt; có image Docker để tự host. ★ 18/11/2026: 15.080 (GitHub search API), nhóm "Đồ họa, 3D & Sơ đồ" trong kho-repo của Phan Đông Giang, mục 08 §6c.5

**Hồ sơ gốc:** [mục 08](../08-awesome-lists-learning/README.md#6c527-đồ-họa-3d--sơ-đồ) (bảng/đoạn chung, giữ nguyên tại chỗ).

<a id="chuan-hoa-2026-11-23"></a>

## Chuẩn hóa bằng chứng hồ sơ cũ — 23/11/2026

Các hồ sơ dưới đây có từ trước khi kho ghi mức kiểm. Ngày 2026-11-23 mỗi repo được clone nông tại commit ghi trong bảng, đọc LICENSE, README, manifest và CI (nếu có); không cài, build hay chạy mã upstream. Nhận định cũ ở phần trên giữ nguyên; chỗ nào khác với lần đọc này được ghi trong cột Nhận định. Số sao lấy qua GitHub search API cùng ngày.

<a id="ch-agentation"></a>

### Agentation

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/benjitaylor/agentation |
| License | PolyForm Shield 1.0.0 (văn bản viết lại, không OSI) |
| Phiên bản đã đọc | `0e3236eb1a0f5577852ab7bb5121f5dd46d42f1d` (commit 2026-09-21) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE, package.json; chưa chạy upstream |
| Bảo trì | Ít hoạt động (commit cuối 2026-09-21) |
| Nhận định | Thanh công cụ React để bấm/ghi chú phần tử rồi chuyển cho agent, có MCP server (cổng 4747) và skill. License chặn dùng làm sản phẩm cạnh tranh; không CI. |
| Nguồn | [README.md](https://github.com/benjitaylor/agentation/blob/0e3236eb1a0f5577852ab7bb5121f5dd46d42f1d/README.md) · [LICENSE](https://github.com/benjitaylor/agentation/blob/0e3236eb1a0f5577852ab7bb5121f5dd46d42f1d/LICENSE) · [package.json](https://github.com/benjitaylor/agentation/blob/0e3236eb1a0f5577852ab7bb5121f5dd46d42f1d/package.json) |

<a id="ch-ai-website-cloner-template"></a>

### ai-website-cloner-template

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/JCodesMore/ai-website-cloner-template |
| License | MIT |
| Phiên bản đã đọc | `5426e0e2ec35dbc173a7a18f47a3dfe2a765313e` (commit 2026-11-10) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE, package.json, .github/workflows/ci.yml; chưa chạy upstream |
| Bảo trì | Đang hoạt động (commit cuối 2026-11-10) |
| Nhận định | Starter Next.js + skill cho agent dựng lại website từ URL. Rủi ro pháp lý cao vì clone nội dung/thương hiệu site khác; README quảng bá proxy dân cư. |
| Nguồn | [README.md](https://github.com/JCodesMore/ai-website-cloner-template/blob/5426e0e2ec35dbc173a7a18f47a3dfe2a765313e/README.md) · [LICENSE](https://github.com/JCodesMore/ai-website-cloner-template/blob/5426e0e2ec35dbc173a7a18f47a3dfe2a765313e/LICENSE) · [package.json](https://github.com/JCodesMore/ai-website-cloner-template/blob/5426e0e2ec35dbc173a7a18f47a3dfe2a765313e/package.json) · [.github/workflows/ci.yml](https://github.com/JCodesMore/ai-website-cloner-template/blob/5426e0e2ec35dbc173a7a18f47a3dfe2a765313e/.github/workflows/ci.yml) |

<a id="ch-anatomy"></a>

### Anatomy

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/wheresryan22/anatomy |
| License | MIT |
| Phiên bản đã đọc | `1482e8469b0a9e0d8cc18ea2740a01423d29ae80` (commit 2026-10-18) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE, SKILL.md, .github/workflows/ci.yml; chưa chạy upstream |
| Bảo trì | Đang hoạt động (commit cuối 2026-10-18) |
| Nhận định | Skill vẽ minh họa isometric tương tác (SVG/WebGL/3D) kèm kit không phụ thuộc và audit hình học. Cài bằng giải nén vào thư mục skills; chất lượng hình là tuyên bố của tác giả **(chưa xác minh)**. |
| Nguồn | [README.md](https://github.com/wheresryan22/anatomy/blob/1482e8469b0a9e0d8cc18ea2740a01423d29ae80/README.md) · [LICENSE](https://github.com/wheresryan22/anatomy/blob/1482e8469b0a9e0d8cc18ea2740a01423d29ae80/LICENSE) · [SKILL.md](https://github.com/wheresryan22/anatomy/blob/1482e8469b0a9e0d8cc18ea2740a01423d29ae80/SKILL.md) · [.github/workflows/ci.yml](https://github.com/wheresryan22/anatomy/blob/1482e8469b0a9e0d8cc18ea2740a01423d29ae80/.github/workflows/ci.yml) |

<a id="ch-anatomy-figures"></a>

### anatomy-figures

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/wheresryan22/anatomy-figures |
| License | MIT |
| Phiên bản đã đọc | `d4590e39369d813cd98450f6f6407634a25ad85a` (commit 2026-10-09) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE, package.json, figures.json; chưa chạy upstream |
| Bảo trì | Đang hoạt động (commit cuối 2026-10-09) |
| Nhận định | Gói npm các figure Anatomy dạng React/custom elements, có theme. Chỉ phát hành dist đã build nên khó kiểm mã nguồn. |
| Nguồn | [README.md](https://github.com/wheresryan22/anatomy-figures/blob/d4590e39369d813cd98450f6f6407634a25ad85a/README.md) · [LICENSE](https://github.com/wheresryan22/anatomy-figures/blob/d4590e39369d813cd98450f6f6407634a25ad85a/LICENSE) · [package.json](https://github.com/wheresryan22/anatomy-figures/blob/d4590e39369d813cd98450f6f6407634a25ad85a/package.json) · [figures.json](https://github.com/wheresryan22/anatomy-figures/blob/d4590e39369d813cd98450f6f6407634a25ad85a/figures.json) |

<a id="ch-ant-design"></a>

### Ant Design

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/ant-design/ant-design |
| License | MIT |
| Phiên bản đã đọc | `469bba8a737430015142ad36dd5b7e8e460244ae` (commit 2026-11-23) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE, package.json, .github/workflows/test.yml; chưa chạy upstream |
| Bảo trì | Đang hoạt động (commit cuối 2026-11-23) |
| Nhận định | Thư viện component React cho ứng dụng doanh nghiệp, bảo trì tích cực. Hỗ trợ MCP theo bài tổng hợp vẫn **(chưa xác minh)**. |
| Nguồn | [README.md](https://github.com/ant-design/ant-design/blob/469bba8a737430015142ad36dd5b7e8e460244ae/README.md) · [LICENSE](https://github.com/ant-design/ant-design/blob/469bba8a737430015142ad36dd5b7e8e460244ae/LICENSE) · [package.json](https://github.com/ant-design/ant-design/blob/469bba8a737430015142ad36dd5b7e8e460244ae/package.json) · [.github/workflows/test.yml](https://github.com/ant-design/ant-design/blob/469bba8a737430015142ad36dd5b7e8e460244ae/.github/workflows/test.yml) |

<a id="ch-ant-design-vue"></a>

### ant-design-vue

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/vueComponent/ant-design-vue |
| License | MIT (3 khối MIT gộp) |
| Phiên bản đã đọc | `7483836f0adac76516e527df893c3d84a7cd4005` (commit 2026-07-24) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE, package.json, .github/workflows/ai-co-author.yml; chưa chạy upstream |
| Bảo trì | Ít hoạt động (commit cuối 2026-07-24) |
| Nhận định | Bản Vue của Ant Design. MIT nhưng gần như không phát hành mới từ 11/2024, nên cân nhắc trước khi dùng cho dự án mới. |
| Nguồn | [README.md](https://github.com/vueComponent/ant-design-vue/blob/7483836f0adac76516e527df893c3d84a7cd4005/README.md) · [LICENSE](https://github.com/vueComponent/ant-design-vue/blob/7483836f0adac76516e527df893c3d84a7cd4005/LICENSE) · [package.json](https://github.com/vueComponent/ant-design-vue/blob/7483836f0adac76516e527df893c3d84a7cd4005/package.json) · [.github/workflows/ai-co-author.yml](https://github.com/vueComponent/ant-design-vue/blob/7483836f0adac76516e527df893c3d84a7cd4005/.github/workflows/ai-co-author.yml) |

<a id="ch-antd-mobile"></a>

### antd-mobile

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/ant-design/ant-design-mobile |
| License | MIT |
| Phiên bản đã đọc | `eee5477f8d6221ced8298e3547eb03e0a037a615` (commit 2026-09-14) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE.txt, package.json, .github/workflows/check.yml; chưa chạy upstream |
| Bảo trì | Ít hoạt động (commit cuối 2026-09-14) |
| Nhận định | Thư viện component React cho mobile web (H5). Ổn định nhưng nhịp phát triển chậm, toolchain cũ (gulp/babel). |
| Nguồn | [README.md](https://github.com/ant-design/ant-design-mobile/blob/eee5477f8d6221ced8298e3547eb03e0a037a615/README.md) · [LICENSE.txt](https://github.com/ant-design/ant-design-mobile/blob/eee5477f8d6221ced8298e3547eb03e0a037a615/LICENSE.txt) · [package.json](https://github.com/ant-design/ant-design-mobile/blob/eee5477f8d6221ced8298e3547eb03e0a037a615/package.json) · [.github/workflows/check.yml](https://github.com/ant-design/ant-design-mobile/blob/eee5477f8d6221ced8298e3547eb03e0a037a615/.github/workflows/check.yml) |

<a id="ch-antislop"></a>

### antislop

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/miqdadbadjuber/anti-slop |
| License | MIT |
| Phiên bản đã đọc | `7f6a03df2931c12cb244dc4ab14ee4866b0ac2ba` (commit 2026-11-21) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE, package.json, .github/workflows/ci.yml; chưa chạy upstream |
| Bảo trì | Đang hoạt động (commit cuối 2026-11-21) |
| Nhận định | Bộ luật lọc "AI slop" + skill cho UI, nội dung, code, đóng gói plugin cho nhiều agent. Lõi nạp luôn nên tốn ngữ cảnh; ngưỡng chữ lớn từng lệch WCAG (chưa kiểm lại). |
| Nguồn | [README.md](https://github.com/miqdadbadjuber/anti-slop/blob/7f6a03df2931c12cb244dc4ab14ee4866b0ac2ba/README.md) · [LICENSE](https://github.com/miqdadbadjuber/anti-slop/blob/7f6a03df2931c12cb244dc4ab14ee4866b0ac2ba/LICENSE) · [package.json](https://github.com/miqdadbadjuber/anti-slop/blob/7f6a03df2931c12cb244dc4ab14ee4866b0ac2ba/package.json) · [.github/workflows/ci.yml](https://github.com/miqdadbadjuber/anti-slop/blob/7f6a03df2931c12cb244dc4ab14ee4866b0ac2ba/.github/workflows/ci.yml) |

<a id="ch-apple-hig-layout"></a>

### Apple HIG: Layout

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://developer.apple.com/design/human-interface-guidelines/layout |
| License | Tài liệu của Apple, không có giấy phép mở (khớp catalog) |
| Phiên bản đã đọc | Trang web, không có SHA (đọc 2026-11-23) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc trang HIG Layout (dữ liệu JSON); chưa chạy upstream |
| Bảo trì | Không rõ (tài liệu Apple cập nhật không theo lịch công bố) |
| Nhận định | Hướng dẫn bố cục theo size class, safe area, chuyển tab bar thành sidebar khi màn hình rộng. Không đưa số margin iOS cố định, dùng làm nguyên tắc chứ không làm token. |
| Nguồn | [HIG Layout](https://developer.apple.com/design/human-interface-guidelines/layout) · [JSON trang](https://developer.apple.com/tutorials/data/design/human-interface-guidelines/layout.json) |

<a id="ch-arco-design-react"></a>

### Arco Design (React)

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/arco-design/arco-design |
| License | MIT |
| Phiên bản đã đọc | `84504beeaf68e8dd8a5fba7a74b45f4ca71c76f2` (commit 2026-11-13) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE, package.json, .github/workflows/main.yml; chưa chạy upstream |
| Bảo trì | Hoạt động (commit 13/11/2026) |
| Nhận định | Thư viện React >60 component của ByteDance, theme bằng Less/Design Lab, @arco-design/web-react 2.66.18. peerDependencies react >=16; workflow `main.yml` (pr_check_react18) chỉ cài react@18 để test, nên hỗ trợ React 19 **(chưa xác minh)**. |
| Nguồn | [README](https://github.com/arco-design/arco-design/blob/84504beeaf68e8dd8a5fba7a74b45f4ca71c76f2/README.md) · [LICENSE](https://github.com/arco-design/arco-design/blob/84504beeaf68e8dd8a5fba7a74b45f4ca71c76f2/LICENSE) · [package.json](https://github.com/arco-design/arco-design/blob/84504beeaf68e8dd8a5fba7a74b45f4ca71c76f2/package.json) · [.github/workflows/main.yml](https://github.com/arco-design/arco-design/blob/84504beeaf68e8dd8a5fba7a74b45f4ca71c76f2/.github/workflows/main.yml) |

<a id="ch-argos"></a>

### Argos

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/argos-ci/argos |
| License | MIT |
| Phiên bản đã đọc | `d443632d60cb5cc2c1d1062ab71456d56cd0f8c6` (commit 2026-11-23) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE, package.json, docker-compose.yml, .github/workflows/ci.yml; chưa chạy upstream |
| Bảo trì | Hoạt động (commit 23/11/2026) |
| Nhận định | Nền tảng visual testing mã mở (backend + frontend trong `apps/`). `docker-compose.yml` dev gồm Postgres 18, RabbitMQ 4.2, Redis 6, DynamoDB local; `package.json` khoá Node 26. README không có hướng dẫn tự host; S3/GitHub App **(chưa xác minh)** từ mã. |
| Nguồn | [README](https://github.com/argos-ci/argos/blob/d443632d60cb5cc2c1d1062ab71456d56cd0f8c6/README.md) · [LICENSE](https://github.com/argos-ci/argos/blob/d443632d60cb5cc2c1d1062ab71456d56cd0f8c6/LICENSE) · [package.json](https://github.com/argos-ci/argos/blob/d443632d60cb5cc2c1d1062ab71456d56cd0f8c6/package.json) · [docker-compose.yml](https://github.com/argos-ci/argos/blob/d443632d60cb5cc2c1d1062ab71456d56cd0f8c6/docker-compose.yml) · [.github/workflows/ci.yml](https://github.com/argos-ci/argos/blob/d443632d60cb5cc2c1d1062ab71456d56cd0f8c6/.github/workflows/ci.yml) |

<a id="ch-ark-ui"></a>

### Ark UI

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/chakra-ui/ark |
| License | MIT |
| Phiên bản đã đọc | `831c8ea279431ffb22d793e912eeee4cebee429a` (commit 2026-11-23) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE, package.json, .github/workflows/quality.yml; chưa chạy upstream |
| Bảo trì | Hoạt động (commit 23/11/2026) |
| Nhận định | Headless component dựa trên máy trạng thái Zag.js, cùng API cho React/Solid/Vue/Svelte. Monorepo có thêm `packages/mcp` (MCP server) và `CLAUDE.md`. Tuyên bố WCAG "tested with real assistive technologies" **(chưa xác minh)**. |
| Nguồn | [README](https://github.com/chakra-ui/ark/blob/831c8ea279431ffb22d793e912eeee4cebee429a/README.md) · [LICENSE](https://github.com/chakra-ui/ark/blob/831c8ea279431ffb22d793e912eeee4cebee429a/LICENSE) · [package.json](https://github.com/chakra-ui/ark/blob/831c8ea279431ffb22d793e912eeee4cebee429a/package.json) · [.github/workflows/quality.yml](https://github.com/chakra-ui/ark/blob/831c8ea279431ffb22d793e912eeee4cebee429a/.github/workflows/quality.yml) |

<a id="ch-assistant-ui"></a>

### assistant-ui

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/assistant-ui/assistant-ui |
| License | MIT |
| Phiên bản đã đọc | `8227544705c6045e70545711ee38d09040e1a282` (commit 2026-11-23) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE, package.json; chưa chạy upstream |
| Bảo trì | Hoạt động (commit 23/11/2026), CI dày (codeql, perf-nightly, lighthouse…) |
| Nhận định | Thư viện TypeScript/React dựng UI chat cho agent: primitive Thread/Message/Composer, CLI `assistant-ui create/init`, runtime cho AI SDK/LangGraph/A2A/AG-UI. Có dịch vụ cloud trả phí; README tự nhận "production-grade" **(chưa xác minh)**. |
| Nguồn | [README](https://github.com/assistant-ui/assistant-ui/blob/8227544705c6045e70545711ee38d09040e1a282/README.md) · [LICENSE](https://github.com/assistant-ui/assistant-ui/blob/8227544705c6045e70545711ee38d09040e1a282/LICENSE) · [package.json](https://github.com/assistant-ui/assistant-ui/blob/8227544705c6045e70545711ee38d09040e1a282/package.json) |

<a id="ch-astryx-meta"></a>

### Astryx (Meta)

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/meta/astryx |
| License | MIT |
| Phiên bản đã đọc | `fc0ea5c022af5e20b46e7c6ab74e8bb4c29fc360` (commit 2026-11-23) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE, package.json, packages/core/package.json, .github/workflows/ci.yml; chưa chạy upstream |
| Bảo trì | Hoạt động (commit 23/11/2026), Beta |
| ★ (ngày) | 32.703 ★, 2.567 fork (2026-11-24, nguồn: GitHub search API). Đường tăng: 13,8k (31/10) → 27,2k (13/11, theo ảnh thẻ star-history, **chưa xác minh độc lập**) → 32,451 (23/11); gấp đôi trong khoảng 2 tuần, chưa rõ nguyên nhân |
| Nhận định | Design system React 19 + StyleX của Meta, đang Beta; `@astryx/core` hiện 0.7.18. README tự nhận "150+ component" và dùng cho 13.000+ app nội bộ **(chưa xác minh)**; có CLI, plugin agent (`.claude-plugin`, `plugins/`). |
| Nguồn | [README](https://github.com/meta/astryx/blob/fc0ea5c022af5e20b46e7c6ab74e8bb4c29fc360/README.md) · [LICENSE](https://github.com/meta/astryx/blob/fc0ea5c022af5e20b46e7c6ab74e8bb4c29fc360/LICENSE) · [package.json](https://github.com/meta/astryx/blob/fc0ea5c022af5e20b46e7c6ab74e8bb4c29fc360/package.json) · [packages/core/package.json](https://github.com/meta/astryx/blob/fc0ea5c022af5e20b46e7c6ab74e8bb4c29fc360/packages/core/package.json) · [.github/workflows/ci.yml](https://github.com/meta/astryx/blob/fc0ea5c022af5e20b46e7c6ab74e8bb4c29fc360/.github/workflows/ci.yml) |

<a id="ch-awesome-ai-tools-for-ui"></a>

### awesome-ai-tools-for-ui

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/maxbogo/awesome-ai-tools-for-ui |
| License | Không có file LICENSE |
| Phiên bản đã đọc | `c16e509e4c089abaa5ea50ce8e8d38ac5a03edd2` (commit 2026-11-03) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md; chưa chạy upstream |
| Bảo trì | Có cập nhật (commit 3/11/2026) |
| Nhận định | Danh sách tuyển chọn công cụ AI cho UI (Skills, Apps, MCP/plugin, Design tools); khoảng 70 mục, link gắn utm. Không có file LICENSE nên mặc định không được cấp quyền tái sử dụng nội dung. |
| Nguồn | [README](https://github.com/maxbogo/awesome-ai-tools-for-ui/blob/c16e509e4c089abaa5ea50ce8e8d38ac5a03edd2/README.md) |

<a id="ch-awesome-design-md"></a>

### awesome-design-md

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/VoltAgent/awesome-design-md |
| License | MIT |
| Phiên bản đã đọc | `fcc70284932276d085f01ef9f83edde90b1258cb` (commit 2026-10-28) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE; chưa chạy upstream |
| Bảo trì | Hoạt động (commit 28/10/2026) |
| Nhận định | Bộ DESIGN.md trích từ website thật (thư mục `design-md/` có 84 mục). README dẫn tới getdesign.md để đặt bản riêng. Mức chính xác so với site gốc và quyền dùng nhận diện thương hiệu bên thứ ba **(chưa xác minh)**. |
| Nguồn | [README](https://github.com/VoltAgent/awesome-design-md/blob/fcc70284932276d085f01ef9f83edde90b1258cb/README.md) · [LICENSE](https://github.com/VoltAgent/awesome-design-md/blob/fcc70284932276d085f01ef9f83edde90b1258cb/LICENSE) |

<a id="ch-awesome-design-skills-bergside-typeui"></a>

### awesome-design-skills (Bergside/TypeUI)

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/bergside/awesome-design-skills |
| License | MIT |
| Phiên bản đã đọc | `f631a09b4fcc0166f2e2c1a8c81906ef680c57e8` (commit 2026-06-28) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE; chưa chạy upstream |
| Bảo trì | Ít hoạt động (commit cuối 28/6/2026) |
| Nhận định | Registry 67 style, mỗi style một cặp SKILL.md + DESIGN.md (thư mục `skills/` có 68 mục), kéo bằng `npx typeui.sh pull`. Nội dung khuôn mẫu lặp nhiều và độ tương phản màu kém theo phân tích cũ của kho. |
| Nguồn | [README](https://github.com/bergside/awesome-design-skills/blob/f631a09b4fcc0166f2e2c1a8c81906ef680c57e8/README.md) · [LICENSE](https://github.com/bergside/awesome-design-skills/blob/f631a09b4fcc0166f2e2c1a8c81906ef680c57e8/LICENSE) |

<a id="ch-awesome-shadcn-ui"></a>

### awesome-shadcn-ui

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/birobirobiro/awesome-shadcn-ui |
| License | MIT |
| Phiên bản đã đọc | `3cfe24434664cd9e11d61f40f037aa67cc9a1c0e` (commit 2026-11-23) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE, .github/workflows/link-check.yml; chưa chạy upstream |
| Bảo trì | Hoạt động (commit 23/11/2026) |
| Nhận định | Danh sách tài nguyên shadcn/ui dạng bảng có cột ngày (~600 dòng bảng), workflow kiểm link, thêm ngày và cập nhật sao. README có khối Sponsors trả phí đặt đầu trang. |
| Nguồn | [README](https://github.com/birobirobiro/awesome-shadcn-ui/blob/3cfe24434664cd9e11d61f40f037aa67cc9a1c0e/README.md) · [LICENSE](https://github.com/birobirobiro/awesome-shadcn-ui/blob/3cfe24434664cd9e11d61f40f037aa67cc9a1c0e/LICENSE) · [.github/workflows/link-check.yml](https://github.com/birobirobiro/awesome-shadcn-ui/blob/3cfe24434664cd9e11d61f40f037aa67cc9a1c0e/.github/workflows/link-check.yml) |

<a id="ch-awesome-tailwindcss"></a>

### awesome-tailwindcss

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/aniftyco/awesome-tailwindcss |
| License | CC0-1.0 |
| Phiên bản đã đọc | `3759163f6a6f162f4d5a3dc1950636344ddd87c4` (commit 2026-10-27) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE.md, CONTRIBUTING.md; chưa chạy upstream |
| Bảo trì | Hoạt động (commit 27/10/2026) |
| Nhận định | Danh sách tài nguyên Tailwind CSS có đánh dấu tài nguyên chính thức và mục deprecated. CONTRIBUTING cấm PR do LLM/agent viết. |
| Nguồn | [README](https://github.com/aniftyco/awesome-tailwindcss/blob/3759163f6a6f162f4d5a3dc1950636344ddd87c4/README.md) · [LICENSE](https://github.com/aniftyco/awesome-tailwindcss/blob/3759163f6a6f162f4d5a3dc1950636344ddd87c4/LICENSE.md) · [CONTRIBUTING.md](https://github.com/aniftyco/awesome-tailwindcss/blob/3759163f6a6f162f4d5a3dc1950636344ddd87c4/CONTRIBUTING.md) |

<a id="ch-axe-core"></a>

### axe-core

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/dequelabs/axe-core |
| License | MPL-2.0 |
| Phiên bản đã đọc | `e80f6b797b32b5f9d60ddaa0a7afad6ed864f121` (commit 2026-11-16) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE, LICENSE-3RD-PARTY.txt, package.json, .github/workflows/test.yml, .github/workflows/nightly-tests.yml; chưa chạy upstream |
| Bảo trì | Hoạt động (commit 16/11/2026, nhánh develop) |
| Nhận định | Engine kiểm a11y runtime theo WCAG 2.0–2.2 A–AAA + best practice, nay bản 4.14.1. README: bắt trung bình 57% lỗi WCAG, phần không chắc trả "incomplete" (số liệu của tác giả, **chưa xác minh**). MPL-2.0 copyleft theo file; có LICENSE-3RD-PARTY. |
| Nguồn | [README](https://github.com/dequelabs/axe-core/blob/e80f6b797b32b5f9d60ddaa0a7afad6ed864f121/README.md) · [LICENSE](https://github.com/dequelabs/axe-core/blob/e80f6b797b32b5f9d60ddaa0a7afad6ed864f121/LICENSE) · [LICENSE-3RD-PARTY.txt](https://github.com/dequelabs/axe-core/blob/e80f6b797b32b5f9d60ddaa0a7afad6ed864f121/LICENSE-3RD-PARTY.txt) · [package.json](https://github.com/dequelabs/axe-core/blob/e80f6b797b32b5f9d60ddaa0a7afad6ed864f121/package.json) · [.github/workflows/test.yml](https://github.com/dequelabs/axe-core/blob/e80f6b797b32b5f9d60ddaa0a7afad6ed864f121/.github/workflows/test.yml) · [.github/workflows/nightly-tests.yml](https://github.com/dequelabs/axe-core/blob/e80f6b797b32b5f9d60ddaa0a7afad6ed864f121/.github/workflows/nightly-tests.yml) |

<a id="ch-baoyu-design"></a>

### baoyu-design

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/JimLiu/open-artifact (trước: https://github.com/JimLiu/baoyu-design) |
| License | Apache-2.0 (khác catalog cũ: Hỗn hợp: MIT cho mã tác giả; phần lấy từ Anthropic không có license) |
| Phiên bản đã đọc | `4d6485194733d6eacc18de1b74226bbbe805255a` (commit 2026-11-23) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE, NOTICE, CHANGELOG.md, package.json, Cargo.toml, .github/workflows/publish-npm.yml; chưa chạy upstream |
| Bảo trì | Hoạt động (commit 23/11/2026), đã đổi tên |
| Nhận định | Đã đổi tên thành **Open Artifact** (`JimLiu/open-artifact`; URL cũ chuyển hướng theo README): daemon cục bộ + editor cho slides/design/whiteboard/sheets…, kèm plugin cho nhiều agent. LICENSE nay Apache-2.0, NOTICE chỉ ghi "formerly published as baoyu-design" và không còn tuyên bố phần của Anthropic; việc đã loại bỏ hết tài sản/prompt trích từ Anthropic **(chưa xác minh)**, các bản cũ trên npm vẫn mang rủi ro sở hữu trí tuệ đã ghi. |
| Nguồn | [README](https://github.com/JimLiu/open-artifact/blob/4d6485194733d6eacc18de1b74226bbbe805255a/README.md) · [LICENSE](https://github.com/JimLiu/open-artifact/blob/4d6485194733d6eacc18de1b74226bbbe805255a/LICENSE) · [NOTICE](https://github.com/JimLiu/open-artifact/blob/4d6485194733d6eacc18de1b74226bbbe805255a/NOTICE) · [CHANGELOG.md](https://github.com/JimLiu/open-artifact/blob/4d6485194733d6eacc18de1b74226bbbe805255a/CHANGELOG.md) · [package.json](https://github.com/JimLiu/open-artifact/blob/4d6485194733d6eacc18de1b74226bbbe805255a/package.json) · [Cargo.toml](https://github.com/JimLiu/open-artifact/blob/4d6485194733d6eacc18de1b74226bbbe805255a/Cargo.toml) · [.github/workflows/publish-npm.yml](https://github.com/JimLiu/open-artifact/blob/4d6485194733d6eacc18de1b74226bbbe805255a/.github/workflows/publish-npm.yml) |

<a id="ch-base-ui"></a>

### Base UI

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/mui/base-ui |
| License | MIT |
| Phiên bản đã đọc | `52fac378e79c7eeccb38ae97adb9d33d9650b177` (commit 2026-11-20) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE, package.json, packages/react/package.json, .github/workflows/ci.yml; chưa chạy upstream |
| Bảo trì | Hoạt động (commit 20/11/2026) |
| Nhận định | Thư viện component không style của nhóm Radix/Floating UI/MUI; `@base-ui/react` 1.9.0, peer React 17–19. Repo có AGENTS.md/CLAUDE.md và CI kiểm thử, CodeQL, Scorecards. |
| Nguồn | [README](https://github.com/mui/base-ui/blob/52fac378e79c7eeccb38ae97adb9d33d9650b177/README.md) · [LICENSE](https://github.com/mui/base-ui/blob/52fac378e79c7eeccb38ae97adb9d33d9650b177/LICENSE) · [package.json](https://github.com/mui/base-ui/blob/52fac378e79c7eeccb38ae97adb9d33d9650b177/package.json) · [packages/react/package.json](https://github.com/mui/base-ui/blob/52fac378e79c7eeccb38ae97adb9d33d9650b177/packages/react/package.json) · [.github/workflows/ci.yml](https://github.com/mui/base-ui/blob/52fac378e79c7eeccb38ae97adb9d33d9650b177/.github/workflows/ci.yml) |

<a id="ch-base-web-uber"></a>

### Base Web (Uber)

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/uber/baseweb |
| License | MIT |
| Phiên bản đã đọc | `ed21081e33f7db2770922b4e04d16dcf5bbdfa85` (commit 2026-09-25) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE, package.json, .github/workflows/pr-check.yml; chưa chạy upstream |
| Bảo trì | Ít hoạt động: README "limiting our engagement", commit cuối 25/9/2026 |
| Nhận định | Design system React của Uber (`baseui` 18.2.0) gắn chặt Styletron. README ghi đang hạn chế tham gia, chỉ mirror phát triển nội bộ; `pr-check.yml` chỉ install + build lib, không chạy test. Không nên chọn cho dự án mới. |
| Nguồn | [README](https://github.com/uber/baseweb/blob/ed21081e33f7db2770922b4e04d16dcf5bbdfa85/README.md) · [LICENSE](https://github.com/uber/baseweb/blob/ed21081e33f7db2770922b4e04d16dcf5bbdfa85/LICENSE) · [package.json](https://github.com/uber/baseweb/blob/ed21081e33f7db2770922b4e04d16dcf5bbdfa85/package.json) · [.github/workflows/pr-check.yml](https://github.com/uber/baseweb/blob/ed21081e33f7db2770922b4e04d16dcf5bbdfa85/.github/workflows/pr-check.yml) |

<a id="ch-best-flutter-ui-templates"></a>

### Best-Flutter-UI-Templates

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/mitesh77/Best-Flutter-UI-Templates |
| License | MIT |
| Phiên bản đã đọc | `c85450cb4367742e879ebfae6cda2b7b4da1c3cd` (commit 2025-12-16) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE, best_flutter_ui_templates/pubspec.yaml, .github/workflows/dart.yml; chưa chạy upstream |
| Bảo trì | Ít hoạt động (commit cuối 16/12/2025) |
| Nhận định | Bộ màn hình demo Flutter (hotel booking, fitness, design course, drawer, introduction animation…) trong một app `publish_to: none`. Chỉ là mẫu giao diện, không có kiến trúc state hay test đáng kể. |
| Nguồn | [README](https://github.com/mitesh77/Best-Flutter-UI-Templates/blob/c85450cb4367742e879ebfae6cda2b7b4da1c3cd/README.md) · [LICENSE](https://github.com/mitesh77/Best-Flutter-UI-Templates/blob/c85450cb4367742e879ebfae6cda2b7b4da1c3cd/LICENSE) · [best_flutter_ui_templates/pubspec.yaml](https://github.com/mitesh77/Best-Flutter-UI-Templates/blob/c85450cb4367742e879ebfae6cda2b7b4da1c3cd/best_flutter_ui_templates/pubspec.yaml) · [.github/workflows/dart.yml](https://github.com/mitesh77/Best-Flutter-UI-Templates/blob/c85450cb4367742e879ebfae6cda2b7b4da1c3cd/.github/workflows/dart.yml) |

<a id="ch-bolt-diy"></a>

### bolt.diy

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/stackblitz-labs/bolt.diy |
| License | MIT |
| Phiên bản đã đọc | `72db5ce846faee4a8b66e68f471635367602a77d` (commit 2026-11-21) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE, package.json, .github/workflows/ci.yaml; chưa chạy upstream |
| Bảo trì | Hoạt động (commit 21/11/2026) |
| Nhận định | Workspace AI dựng app full-stack trong trình duyệt, chọn LLM theo prompt (22+ nhà cung cấp), có Docker và app Electron. README lưu ý dùng WebContainers API vốn có điều khoản thương mại riêng cho triển khai doanh nghiệp. |
| Nguồn | [README](https://github.com/stackblitz-labs/bolt.diy/blob/72db5ce846faee4a8b66e68f471635367602a77d/README.md) · [LICENSE](https://github.com/stackblitz-labs/bolt.diy/blob/72db5ce846faee4a8b66e68f471635367602a77d/LICENSE) · [package.json](https://github.com/stackblitz-labs/bolt.diy/blob/72db5ce846faee4a8b66e68f471635367602a77d/package.json) · [.github/workflows/ci.yaml](https://github.com/stackblitz-labs/bolt.diy/blob/72db5ce846faee4a8b66e68f471635367602a77d/.github/workflows/ci.yaml) |

<a id="ch-canvas-ui"></a>

### canvas-ui

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/DavidHDev/canvas-ui |
| License | MIT + Commons Clause (tùy biến) (khác catalog cũ: NOASSERTION) |
| Phiên bản đã đọc | `d5a6778cba7dc72edcc03a133e2841cd1f1e3c8a` (commit 2026-11-21) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE.md, package.json, .github/workflows/ci.yml; chưa chạy upstream |
| Bảo trì | Hoạt động (commit 21/11/2026) |
| Nhận định | Thư viện 38 hiệu ứng canvas (WebGL/WebGPU) cho React/Solid/Preact/Vue/Svelte/vanilla, phân phối kiểu copy qua registry tương thích shadcn; hiệu ứng "Live HTML" dùng API HTML-in-canvas của Chrome, có fallback. LICENSE.md là MIT + Commons Clause: dùng thương mại trong sản phẩm được, nhưng cấm bán/phân phối lại chính component. |
| Nguồn | [README](https://github.com/DavidHDev/canvas-ui/blob/d5a6778cba7dc72edcc03a133e2841cd1f1e3c8a/README.md) · [LICENSE](https://github.com/DavidHDev/canvas-ui/blob/d5a6778cba7dc72edcc03a133e2841cd1f1e3c8a/LICENSE.md) · [package.json](https://github.com/DavidHDev/canvas-ui/blob/d5a6778cba7dc72edcc03a133e2841cd1f1e3c8a/package.json) · [.github/workflows/ci.yml](https://github.com/DavidHDev/canvas-ui/blob/d5a6778cba7dc72edcc03a133e2841cd1f1e3c8a/.github/workflows/ci.yml) |

<a id="ch-capsize"></a>

### Capsize

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/seek-oss/capsize |
| License | MIT |
| Phiên bản đã đọc | `cbfb23088c55be74ffbbe749da2c6e8d3508d2d5` (commit 2026-11-18) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE, packages/core/package.json, .github/workflows/test.yml; chưa chạy upstream |
| Bảo trì | Hoạt động (commit 18/11/2026) |
| Nhận định | Thư viện căn kích thước chữ theo cap height dựa trên metric font, cắt khoảng trống trên/dưới; gói `@capsizecss/core` 4.1.3, kèm metrics/unpack/vanilla-extract. |
| Nguồn | [README](https://github.com/seek-oss/capsize/blob/cbfb23088c55be74ffbbe749da2c6e8d3508d2d5/README.md) · [LICENSE](https://github.com/seek-oss/capsize/blob/cbfb23088c55be74ffbbe749da2c6e8d3508d2d5/LICENSE) · [packages/core/package.json](https://github.com/seek-oss/capsize/blob/cbfb23088c55be74ffbbe749da2c6e8d3508d2d5/packages/core/package.json) · [.github/workflows/test.yml](https://github.com/seek-oss/capsize/blob/cbfb23088c55be74ffbbe749da2c6e8d3508d2d5/.github/workflows/test.yml) |

<a id="ch-carbon"></a>

### Carbon

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/carbon-design-system/carbon |
| License | Apache-2.0 |
| Phiên bản đã đọc | `f8fa9e863f4115798decb2267277418bce36a085` (commit 2026-11-23) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE, package.json, .github/workflows/ci.yml; chưa chạy upstream |
| Bảo trì | Hoạt động (commit 23/11/2026) |
| Nhận định | Monorepo design system IBM: React, web components, Sass, token, icon, pictogram. README/AGENTS.md trong repo không nhắc Carbon MCP hay llms.txt, nên các điểm này vẫn **(chưa xác minh)** từ repo. |
| Nguồn | [README](https://github.com/carbon-design-system/carbon/blob/f8fa9e863f4115798decb2267277418bce36a085/README.md) · [LICENSE](https://github.com/carbon-design-system/carbon/blob/f8fa9e863f4115798decb2267277418bce36a085/LICENSE) · [package.json](https://github.com/carbon-design-system/carbon/blob/f8fa9e863f4115798decb2267277418bce36a085/package.json) · [.github/workflows/ci.yml](https://github.com/carbon-design-system/carbon/blob/f8fa9e863f4115798decb2267277418bce36a085/.github/workflows/ci.yml) |

<a id="ch-chakra-ui"></a>

### Chakra UI

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/chakra-ui/chakra-ui |
| License | MIT |
| Phiên bản đã đọc | `4fca0889be532fced536b77e1dff982001ebc672` (commit 2026-11-19) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE, package.json, apps/mcp/package.json, .github/workflows/quality.yml; chưa chạy upstream |
| Bảo trì | Hoạt động (commit 19/11/2026) |
| Nhận định | Component React có style, hỗ trợ Next.js RSC; `@chakra-ui/react` 3.38.0. Repo có `apps/mcp` (gói `@chakra-ui/react-mcp` 2.1.1) và thư mục `skills/`, nên MCP chính thức có thật; chất lượng tool MCP **(chưa xác minh)**. |
| Nguồn | [README](https://github.com/chakra-ui/chakra-ui/blob/4fca0889be532fced536b77e1dff982001ebc672/README.md) · [LICENSE](https://github.com/chakra-ui/chakra-ui/blob/4fca0889be532fced536b77e1dff982001ebc672/LICENSE) · [package.json](https://github.com/chakra-ui/chakra-ui/blob/4fca0889be532fced536b77e1dff982001ebc672/package.json) · [apps/mcp/package.json](https://github.com/chakra-ui/chakra-ui/blob/4fca0889be532fced536b77e1dff982001ebc672/apps/mcp/package.json) · [.github/workflows/quality.yml](https://github.com/chakra-ui/chakra-ui/blob/4fca0889be532fced536b77e1dff982001ebc672/.github/workflows/quality.yml) |

<a id="ch-copilotkit"></a>

### CopilotKit

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/CopilotKit/CopilotKit |
| License | MIT |
| Phiên bản đã đọc | `544e64f0423533c5ade8346cd7b9da3c0530a6bc` (commit 2026-11-22) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE, package.json; chưa chạy upstream |
| Bảo trì | Hoạt động (commit 22/11/2026) |
| Nhận định | Stack mã mở đưa agent tới người dùng: chat, generative UI, shared state, human-in-the-loop cho React/Angular/Vue/React Native/Slack/Teams; đội tác giả giao thức AG-UI. Lớp "CopilotKit Intelligence" là sản phẩm thương mại; LICENSE gốc và các package con đọc được đều MIT. |
| Nguồn | [README](https://github.com/CopilotKit/CopilotKit/blob/544e64f0423533c5ade8346cd7b9da3c0530a6bc/README.md) · [LICENSE](https://github.com/CopilotKit/CopilotKit/blob/544e64f0423533c5ade8346cd7b9da3c0530a6bc/LICENSE) · [package.json](https://github.com/CopilotKit/CopilotKit/blob/544e64f0423533c5ade8346cd7b9da3c0530a6bc/package.json) |

<a id="ch-coss-ui"></a>

### coss ui

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/cosscom/ui |
| License | MIT |
| Phiên bản đã đọc | `66b96c8463c8e50ca65e543babae5607cf21c92f` (commit 2026-11-23) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE, package.json, packages/ui/package.json, .github/workflows/test.yml; chưa chạy upstream |
| Bảo trì | Hoạt động (commit 23/11/2026) |
| Nhận định | Design system chính thức của Cal.com (trước là Origin UI, `apps/origin` giữ bản cũ). `packages/ui` yêu cầu React ^19.2.6 và Next ^16.3.8; có AGENTS.md và CI test/typecheck. |
| Nguồn | [README](https://github.com/cosscom/ui/blob/66b96c8463c8e50ca65e543babae5607cf21c92f/README.md) · [LICENSE](https://github.com/cosscom/ui/blob/66b96c8463c8e50ca65e543babae5607cf21c92f/LICENSE) · [package.json](https://github.com/cosscom/ui/blob/66b96c8463c8e50ca65e543babae5607cf21c92f/package.json) · [packages/ui/package.json](https://github.com/cosscom/ui/blob/66b96c8463c8e50ca65e543babae5607cf21c92f/packages/ui/package.json) · [.github/workflows/test.yml](https://github.com/cosscom/ui/blob/66b96c8463c8e50ca65e543babae5607cf21c92f/.github/workflows/test.yml) |

<a id="ch-daisyui"></a>

### daisyUI

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/saadeghi/daisyui |
| License | MIT |
| Phiên bản đã đọc | `43bc54e9ea25a0f26d85392c169dae6b9839d6e5` (commit 2026-11-20) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE, packages/daisyui/package.json, .github/workflows/run-tests.yml; chưa chạy upstream |
| Bảo trì | Hoạt động (commit 20/11/2026) |
| Nhận định | Plugin component cho Tailwind CSS, daisyUI 5 (gói 5.8.2); repo có thêm skill và plugin cho Claude/Codex/Cursor. Template đầy đủ bán ở cửa hàng riêng (theo catalog cũ, **chưa xác minh** lại). |
| Nguồn | [README](https://github.com/saadeghi/daisyui/blob/43bc54e9ea25a0f26d85392c169dae6b9839d6e5/README.md) · [LICENSE](https://github.com/saadeghi/daisyui/blob/43bc54e9ea25a0f26d85392c169dae6b9839d6e5/LICENSE) · [packages/daisyui/package.json](https://github.com/saadeghi/daisyui/blob/43bc54e9ea25a0f26d85392c169dae6b9839d6e5/packages/daisyui/package.json) · [.github/workflows/run-tests.yml](https://github.com/saadeghi/daisyui/blob/43bc54e9ea25a0f26d85392c169dae6b9839d6e5/.github/workflows/run-tests.yml) |

<a id="ch-dembrandt"></a>

### dembrandt

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/dembrandt/dembrandt |
| License | MIT |
| Phiên bản đã đọc | `f7edaabbc9e1ac2bee728e2e069f73a0a84b969f` (commit 2026-11-22) |
| Kiểm chứng | 2026-11-23; code-read; đã đọc README.md, LICENSE, package.json, lib/robots.ts, .github/workflows/smoke.yml; chưa chạy upstream |
| Bảo trì | Hoạt động (commit 22/11/2026) |
| Nhận định | CLI/MCP/GitHub Action trích token thiết kế từ website bằng Playwright, xuất W3C token/DESIGN.md và chặn lệch token trong CI; nay v0.41.0. `lib/robots.ts`: lượt chạy "enforcing" từ chối khi robots cấm, lượt người dùng chạy chỉ cảnh báo rồi tiếp tục. |
| Nguồn | [README](https://github.com/dembrandt/dembrandt/blob/f7edaabbc9e1ac2bee728e2e069f73a0a84b969f/README.md) · [LICENSE](https://github.com/dembrandt/dembrandt/blob/f7edaabbc9e1ac2bee728e2e069f73a0a84b969f/LICENSE) · [package.json](https://github.com/dembrandt/dembrandt/blob/f7edaabbc9e1ac2bee728e2e069f73a0a84b969f/package.json) · [lib/robots.ts](https://github.com/dembrandt/dembrandt/blob/f7edaabbc9e1ac2bee728e2e069f73a0a84b969f/lib/robots.ts) · [.github/workflows/smoke.yml](https://github.com/dembrandt/dembrandt/blob/f7edaabbc9e1ac2bee728e2e069f73a0a84b969f/.github/workflows/smoke.yml) |

<a id="ch-design-md-spec-google"></a>

### DESIGN.md spec (Google)

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/google-labs-code/design.md |
| License | Apache-2.0 |
| Phiên bản đã đọc | `db977b3c1d1f309269f43d5d17ae828d54bd6ae3` (commit 2026-11-17) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE, docs/spec.md, packages/cli/package.json, .github/workflows/test.yml; chưa chạy upstream |
| Bảo trì | Hoạt động (commit 17/11/2026) |
| Nhận định | Đặc tả DESIGN.md (token YAML + văn xuôi giải thích) cho agent, `docs/spec.md` ghi version alpha. CLI `@google/design.md` nay 0.4.1 để lint/diff/export. |
| Nguồn | [README](https://github.com/google-labs-code/design.md/blob/db977b3c1d1f309269f43d5d17ae828d54bd6ae3/README.md) · [LICENSE](https://github.com/google-labs-code/design.md/blob/db977b3c1d1f309269f43d5d17ae828d54bd6ae3/LICENSE) · [docs/spec.md](https://github.com/google-labs-code/design.md/blob/db977b3c1d1f309269f43d5d17ae828d54bd6ae3/docs/spec.md) · [packages/cli/package.json](https://github.com/google-labs-code/design.md/blob/db977b3c1d1f309269f43d5d17ae828d54bd6ae3/packages/cli/package.json) · [.github/workflows/test.yml](https://github.com/google-labs-code/design.md/blob/db977b3c1d1f309269f43d5d17ae828d54bd6ae3/.github/workflows/test.yml) |

<a id="ch-design-tokens-community-group-dtcg"></a>

### Design Tokens Community Group (DTCG)

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/design-tokens/community-group |
| License | W3C Software and Document License |
| Phiên bản đã đọc | `882ebd6716abef9a46d8ef5fb12e82009d6cee2e` (commit 2026-09-08) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE.md, technical-reports/format/index.html, .github/workflows/pr.yml; chưa chạy upstream |
| Bảo trì | Ít hoạt động (commit cuối 8/9/2026) |
| Nhận định | Repo của nhóm cộng đồng W3C về design token: technical report Format/Color/Resolver, JSON Schema `schemas/src/2025.10`, test-suite. Nguồn spec ghi `specStatus: CG-DRAFT`, tức báo cáo Community Group, không phải W3C Recommendation. |
| Nguồn | [README](https://github.com/design-tokens/community-group/blob/882ebd6716abef9a46d8ef5fb12e82009d6cee2e/README.md) · [LICENSE](https://github.com/design-tokens/community-group/blob/882ebd6716abef9a46d8ef5fb12e82009d6cee2e/LICENSE.md) · [technical-reports/format/index.html](https://github.com/design-tokens/community-group/blob/882ebd6716abef9a46d8ef5fb12e82009d6cee2e/technical-reports/format/index.html) · [.github/workflows/pr.yml](https://github.com/design-tokens/community-group/blob/882ebd6716abef9a46d8ef5fb12e82009d6cee2e/.github/workflows/pr.yml) |

<a id="ch-designer-skills"></a>

### designer-skills

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/Owl-Listener/designer-skills |
| License | MIT |
| Phiên bản đã đọc | `9a6930cf84a822eb458624bd11c61aac5bbdf224` (commit 2026-09-05) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE, CHANGELOG.md, .github/workflows/lint.yml; chưa chạy upstream |
| Bảo trì | Ít hoạt động (commit cuối 5/9/2026) |
| Nhận định | Bộ skill/lệnh nghề thiết kế dạng prompt cho Claude Code/Gemini CLI, 9 plugin trong repo; README nay quảng bá "273 skill, 76 lệnh, 33 plugin, 5 collection", tức tính cả plugin kéo từ repo khác qua marketplace. Chất lượng skill **(chưa xác minh)**. |
| Nguồn | [README](https://github.com/Owl-Listener/designer-skills/blob/9a6930cf84a822eb458624bd11c61aac5bbdf224/README.md) · [LICENSE](https://github.com/Owl-Listener/designer-skills/blob/9a6930cf84a822eb458624bd11c61aac5bbdf224/LICENSE) · [CHANGELOG.md](https://github.com/Owl-Listener/designer-skills/blob/9a6930cf84a822eb458624bd11c61aac5bbdf224/CHANGELOG.md) · [.github/workflows/lint.yml](https://github.com/Owl-Listener/designer-skills/blob/9a6930cf84a822eb458624bd11c61aac5bbdf224/.github/workflows/lint.yml) |

<a id="ch-designlang-design-extract"></a>

### designlang (design-extract)

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/Manavarya09/design-extract |
| License | MIT |
| Phiên bản đã đọc | `7d37734ef93c57daf358638322ffcb2c45118b3d` (commit 2026-11-18) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE, package.json, .github/workflows/test.yml; chưa chạy upstream |
| Bảo trì | Hoạt động (commit 18/11/2026) |
| Nhận định | CLI `designlang` 13.4.1: dùng trình duyệt headless trích token (DTCG, Tailwind, shadcn, Figma variables, DESIGN.md…) kèm chấm điểm WCAG, drift. README đặt nhà tài trợ (Atlas Cloud, Infistar) lên đầu và quảng bá `--smart` gửi dữ liệu tới API LLM; grep `src/` không thấy xử lý robots.txt. |
| Nguồn | [README](https://github.com/Manavarya09/design-extract/blob/7d37734ef93c57daf358638322ffcb2c45118b3d/README.md) · [LICENSE](https://github.com/Manavarya09/design-extract/blob/7d37734ef93c57daf358638322ffcb2c45118b3d/LICENSE) · [package.json](https://github.com/Manavarya09/design-extract/blob/7d37734ef93c57daf358638322ffcb2c45118b3d/package.json) · [.github/workflows/test.yml](https://github.com/Manavarya09/design-extract/blob/7d37734ef93c57daf358638322ffcb2c45118b3d/.github/workflows/test.yml) |

<a id="ch-diagram-design"></a>

### diagram-design

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/cathrynlavery/diagram-design |
| License | MIT |
| Phiên bản đã đọc | `0eeda75a708f419560d5e032693618bb9954f17b` (commit 2026-11-23) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE, PRIVACY.md, .claude-plugin/plugin.json, .github/workflows/ci.yml; chưa chạy upstream |
| Bảo trì | Hoạt động (commit 2026-11-23, plugin 2.6.174 tự bump) |
| Nhận định | Skill agent vẽ sơ đồ thành một file HTML+SVG tự chứa theo brand; README nay ghi 52 loại sơ đồ (catalog cũ ghi 44), có onboarding brand từ URL, nhập drawio/Mermaid/Excalidraw. PRIVACY.md nói không server/analytics, chỉ tải font từ Google Fonts khi mở file. Chất lượng đầu ra là tuyên bố của tác giả **(chưa xác minh)**. |
| Nguồn | [README.md](https://github.com/cathrynlavery/diagram-design/blob/0eeda75a708f419560d5e032693618bb9954f17b/README.md) · [LICENSE](https://github.com/cathrynlavery/diagram-design/blob/0eeda75a708f419560d5e032693618bb9954f17b/LICENSE) · [PRIVACY.md](https://github.com/cathrynlavery/diagram-design/blob/0eeda75a708f419560d5e032693618bb9954f17b/PRIVACY.md) · [plugin.json](https://github.com/cathrynlavery/diagram-design/blob/0eeda75a708f419560d5e032693618bb9954f17b/.claude-plugin/plugin.json) · [ci.yml](https://github.com/cathrynlavery/diagram-design/blob/0eeda75a708f419560d5e032693618bb9954f17b/.github/workflows/ci.yml) |

<a id="ch-dicebear"></a>

### DiceBear

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/dicebear/dicebear |
| License | MIT cho mã; mỗi style có license riêng (giữ như catalog) |
| Phiên bản đã đọc | `74d2a21337bed581c2aa76926e9ecf7ebf9480ae` (commit 2026-11-21) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE, package.json, src/js/core/package.json, .github/workflows/test.yml; chưa chạy upstream |
| Bảo trì | Hoạt động |
| Nhận định | Thư viện avatar tất định từ seed, bản port JS/PHP/Python/Rust/Go/Dart/C# cam kết SVG giống byte **(chưa xác minh)**. Mã MIT nhưng từng style có license riêng (một số CC BY 4.0 phải ghi công) — đọc trang license trước khi dùng. Nhánh mặc định là 11.x, core đang ở 11.0.0-rc.3. |
| Nguồn | [README.md](https://github.com/dicebear/dicebear/blob/74d2a21337bed581c2aa76926e9ecf7ebf9480ae/README.md) · [LICENSE](https://github.com/dicebear/dicebear/blob/74d2a21337bed581c2aa76926e9ecf7ebf9480ae/LICENSE) · [package.json](https://github.com/dicebear/dicebear/blob/74d2a21337bed581c2aa76926e9ecf7ebf9480ae/package.json) · [package.json](https://github.com/dicebear/dicebear/blob/74d2a21337bed581c2aa76926e9ecf7ebf9480ae/src/js/core/package.json) · [test.yml](https://github.com/dicebear/dicebear/blob/74d2a21337bed581c2aa76926e9ecf7ebf9480ae/.github/workflows/test.yml) |

<a id="ch-elastic-ui-eui"></a>

### Elastic UI (EUI)

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/elastic/eui |
| License | SSPL-1.0 OR Elastic-2.0 (mặc định; vài file theo header khác) — khớp catalog |
| Phiên bản đã đọc | `efc165bfc709ddf3b889a76f905319e3cf158396` (commit 2026-11-23) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE.txt, packages/eui/package.json; chưa chạy upstream |
| Bảo trì | Hoạt động |
| Nhận định | Thư viện React của Elastic, mặc định dual SSPL-1.0/Elastic-2.0 (không phải OSI), một số file theo header riêng. Bản 123.5.0 peer chỉ React 17/18. Chỉ hợp khi làm trong hệ Elastic; contributor ngoài chỉ được mở PR cho issue 'help wanted'. |
| Nguồn | [README.md](https://github.com/elastic/eui/blob/efc165bfc709ddf3b889a76f905319e3cf158396/README.md) · [LICENSE.txt](https://github.com/elastic/eui/blob/efc165bfc709ddf3b889a76f905319e3cf158396/LICENSE.txt) · [package.json](https://github.com/elastic/eui/blob/efc165bfc709ddf3b889a76f905319e3cf158396/packages/eui/package.json) |

<a id="ch-eslint-plugin-jsx-a11y"></a>

### eslint-plugin-jsx-a11y

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/jsx-eslint/eslint-plugin-jsx-a11y |
| License | MIT |
| Phiên bản đã đọc | `8f75961d965e47afb88854d324bd32fafde7acfe` (commit 2026-01-03) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE.md, package.json, .github/workflows/node-4+.yml; chưa chạy upstream |
| Bảo trì | Ít hoạt động (commit cuối 2026-01-03) |
| Nhận định | Plugin ESLint kiểm a11y tĩnh cho JSX, 39 luật. Bản 6.10.2 peer chỉ tới ESLint ^9; nhánh chính đứng từ 3/1/2026 nên dự án dùng ESLint 10 cần kiểm fork hoặc chờ. Chỉ bắt lỗi tĩnh, README khuyên dùng kèm axe. |
| Nguồn | [README.md](https://github.com/jsx-eslint/eslint-plugin-jsx-a11y/blob/8f75961d965e47afb88854d324bd32fafde7acfe/README.md) · [LICENSE.md](https://github.com/jsx-eslint/eslint-plugin-jsx-a11y/blob/8f75961d965e47afb88854d324bd32fafde7acfe/LICENSE.md) · [package.json](https://github.com/jsx-eslint/eslint-plugin-jsx-a11y/blob/8f75961d965e47afb88854d324bd32fafde7acfe/package.json) · [node-4+.yml](https://github.com/jsx-eslint/eslint-plugin-jsx-a11y/blob/8f75961d965e47afb88854d324bd32fafde7acfe/.github/workflows/node-4+.yml) |

<a id="ch-excalidraw"></a>

### Excalidraw

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/excalidraw/excalidraw |
| License | MIT |
| Phiên bản đã đọc | `9c2e462ec23e54c4cf0493328840d6a27191c674` (commit 2026-11-21) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE, package.json, .github/workflows/test.yml; chưa chạy upstream |
| Bảo trì | Hoạt động |
| Nhận định | Whiteboard vẽ tay mã mở, cộng tác và mã hóa đầu-cuối theo README; có gói npm @excalidraw/excalidraw để nhúng và Dockerfile để self-host. Bản Excalidraw+ là dịch vụ trả phí riêng. |
| Nguồn | [README.md](https://github.com/excalidraw/excalidraw/blob/9c2e462ec23e54c4cf0493328840d6a27191c674/README.md) · [LICENSE](https://github.com/excalidraw/excalidraw/blob/9c2e462ec23e54c4cf0493328840d6a27191c674/LICENSE) · [package.json](https://github.com/excalidraw/excalidraw/blob/9c2e462ec23e54c4cf0493328840d6a27191c674/package.json) · [test.yml](https://github.com/excalidraw/excalidraw/blob/9c2e462ec23e54c4cf0493328840d6a27191c674/.github/workflows/test.yml) |

<a id="ch-figcraft"></a>

### FigCraft

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/storytold/figcraft |
| License | MIT OR Apache-2.0 |
| Phiên bản đã đọc | `b828e6c75a3a90fefc0e62f488c013ca4714a5fa` (commit 2026-11-23) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE-MIT, LICENSE-APACHE, Cargo.toml, .github/workflows/ci.yml; chưa chạy upstream |
| Bảo trì | Hoạt động |
| Nhận định | Công cụ thiết kế giao diện kiểu Figma viết bằng Rust (thuộc ArtCraft), chạy native/web, không tài khoản, không telemetry theo README **(chưa xác minh)**. README tự ghi 'early alpha'; mở file .fig chỉ 'best effort' nên chưa thay được Figma cho file thật. |
| Nguồn | [README.md](https://github.com/storytold/figcraft/blob/b828e6c75a3a90fefc0e62f488c013ca4714a5fa/README.md) · [LICENSE-MIT](https://github.com/storytold/figcraft/blob/b828e6c75a3a90fefc0e62f488c013ca4714a5fa/LICENSE-MIT) · [LICENSE-APACHE](https://github.com/storytold/figcraft/blob/b828e6c75a3a90fefc0e62f488c013ca4714a5fa/LICENSE-APACHE) · [Cargo.toml](https://github.com/storytold/figcraft/blob/b828e6c75a3a90fefc0e62f488c013ca4714a5fa/Cargo.toml) · [ci.yml](https://github.com/storytold/figcraft/blob/b828e6c75a3a90fefc0e62f488c013ca4714a5fa/.github/workflows/ci.yml) |

<a id="ch-figmatocode"></a>

### FigmaToCode

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/bernaferrari/FigmaToCode |
| License | GPL-3.0 |
| Phiên bản đã đọc | `f5c4831d5de6cffc19a73fe2823c56b4bb551281` (commit 2026-08-05) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE, manifest.json, package.json, .github/workflows/test.yml; chưa chạy upstream |
| Bảo trì | Ít hoạt động (commit cuối 2026-08-05) |
| Nhận định | Plugin Figma chuyển tất định (không AI) sang HTML/React/Svelte/Tailwind/Flutter/SwiftUI, có xuất starter Vite/Next. manifest.json không xin quyền, chặn mạng. GPL-3.0 ràng khi fork/nhúng plugin; ràng buộc với mã sinh ra **(chưa xác minh pháp lý)**. |
| Nguồn | [README.md](https://github.com/bernaferrari/FigmaToCode/blob/f5c4831d5de6cffc19a73fe2823c56b4bb551281/README.md) · [LICENSE](https://github.com/bernaferrari/FigmaToCode/blob/f5c4831d5de6cffc19a73fe2823c56b4bb551281/LICENSE) · [manifest.json](https://github.com/bernaferrari/FigmaToCode/blob/f5c4831d5de6cffc19a73fe2823c56b4bb551281/manifest.json) · [package.json](https://github.com/bernaferrari/FigmaToCode/blob/f5c4831d5de6cffc19a73fe2823c56b4bb551281/package.json) · [test.yml](https://github.com/bernaferrari/FigmaToCode/blob/f5c4831d5de6cffc19a73fe2823c56b4bb551281/.github/workflows/test.yml) |

<a id="ch-flowbite"></a>

### Flowbite

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/themesberg/flowbite |
| License | MIT |
| Phiên bản đã đọc | `232ebdb33a9e37b31b293b9988d89b862ee121e5` (commit 2026-06-27) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE.md, package.json; chưa chạy upstream |
| Bảo trì | Ít hoạt động (commit cuối 2026-06-27) |
| Nhận định | Thư viện component trên Tailwind, lõi MIT (v4.0.2), có llms.txt trong repo. Blocks 400+ section và Pro là sản phẩm trả phí. Repo không có CI và đứng từ 27/6/2026. |
| Nguồn | [README.md](https://github.com/themesberg/flowbite/blob/232ebdb33a9e37b31b293b9988d89b862ee121e5/README.md) · [LICENSE.md](https://github.com/themesberg/flowbite/blob/232ebdb33a9e37b31b293b9988d89b862ee121e5/LICENSE.md) · [package.json](https://github.com/themesberg/flowbite/blob/232ebdb33a9e37b31b293b9988d89b862ee121e5/package.json) |

<a id="ch-flowbite-admin-dashboard"></a>

### Flowbite Admin Dashboard

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/themesberg/flowbite-admin-dashboard |
| License | MIT |
| Phiên bản đã đọc | `229df7ff25808ab2bbda65f03f2397a05f7b4288` (commit 2025-03-20) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE, package.json; chưa chạy upstream |
| Bảo trì | Ít hoạt động (commit cuối 2025-03-20) |
| Nhận định | Mẫu admin dashboard Hugo + Tailwind v3 + Flowbite. README ghi 15 trang mẫu (catalog đếm file được 17). Đứng từ 3/2025, chưa lên Tailwind v4: chỉ nên làm tham khảo. |
| Nguồn | [README.md](https://github.com/themesberg/flowbite-admin-dashboard/blob/229df7ff25808ab2bbda65f03f2397a05f7b4288/README.md) · [LICENSE](https://github.com/themesberg/flowbite-admin-dashboard/blob/229df7ff25808ab2bbda65f03f2397a05f7b4288/LICENSE) · [package.json](https://github.com/themesberg/flowbite-admin-dashboard/blob/229df7ff25808ab2bbda65f03f2397a05f7b4288/package.json) |

<a id="ch-fluent-ui"></a>

### Fluent UI

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/microsoft/fluentui |
| License | MIT (catalog cũ để trống) |
| Phiên bản đã đọc | `41c06a31611d4a0f6cf7153d71898957e6c497e3` (commit 2026-11-23) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE, package.json, .github/workflows/pr.yml; chưa chạy upstream |
| Bảo trì | Hoạt động |
| Nhận định | Monorepo Fluent UI của Microsoft: React v9 (hướng tới), v8 (trưởng thành), Web Components. Phát triển rất tích cực. Hỗ trợ llms.txt/MCP chưa kiểm trong lần đọc này. |
| Nguồn | [README.md](https://github.com/microsoft/fluentui/blob/41c06a31611d4a0f6cf7153d71898957e6c497e3/README.md) · [LICENSE](https://github.com/microsoft/fluentui/blob/41c06a31611d4a0f6cf7153d71898957e6c497e3/LICENSE) · [package.json](https://github.com/microsoft/fluentui/blob/41c06a31611d4a0f6cf7153d71898957e6c497e3/package.json) · [pr.yml](https://github.com/microsoft/fluentui/blob/41c06a31611d4a0f6cf7153d71898957e6c497e3/.github/workflows/pr.yml) |

<a id="ch-flutter-responsive-admin-panel"></a>

### Flutter Responsive Admin Panel

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/abuanwar072/Flutter-Responsive-Admin-Panel-or-Dashboard |
| License | MIT |
| Phiên bản đã đọc | `a0b5a89c2e6c6a7e4753b36a50b91230156f67b7` (commit 2026-07-28) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE, pubspec.yaml, .github/workflows/run_web.yml; chưa chạy upstream |
| Bảo trì | Ít hoạt động (commit cuối 2026-07-28) |
| Nhận định | Mẫu dashboard Flutter responsive một layout (side menu + dashboard), dùng provider, flutter_svg, google_fonts. Nhỏ (17 file dart), hợp học hoặc khởi đầu, không phải bộ component. |
| Nguồn | [README.md](https://github.com/abuanwar072/Flutter-Responsive-Admin-Panel-or-Dashboard/blob/a0b5a89c2e6c6a7e4753b36a50b91230156f67b7/README.md) · [LICENSE](https://github.com/abuanwar072/Flutter-Responsive-Admin-Panel-or-Dashboard/blob/a0b5a89c2e6c6a7e4753b36a50b91230156f67b7/LICENSE) · [pubspec.yaml](https://github.com/abuanwar072/Flutter-Responsive-Admin-Panel-or-Dashboard/blob/a0b5a89c2e6c6a7e4753b36a50b91230156f67b7/pubspec.yaml) · [run_web.yml](https://github.com/abuanwar072/Flutter-Responsive-Admin-Panel-or-Dashboard/blob/a0b5a89c2e6c6a7e4753b36a50b91230156f67b7/.github/workflows/run_web.yml) |

<a id="ch-flutter-samples"></a>

### flutter/samples

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/flutter/samples |
| License | BSD-3-Clause |
| Phiên bản đã đọc | `a5bccd247163b1017d2eb9320cf3b94a95ccfb5e` (commit 2026-11-17) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE, pubspec.yaml, .github/workflows/main.yml; chưa chạy upstream |
| Bảo trì | Hoạt động |
| Nhận định | Bộ mẫu chính thức của Flutter, CI chạy script kiểm toàn repo. README nói nhóm tạm không thêm mẫu mới, vẫn nhận sửa lỗi. Trạng thái flutter_adaptive_scaffold chưa kiểm lại lần này. |
| Nguồn | [README.md](https://github.com/flutter/samples/blob/a5bccd247163b1017d2eb9320cf3b94a95ccfb5e/README.md) · [LICENSE](https://github.com/flutter/samples/blob/a5bccd247163b1017d2eb9320cf3b94a95ccfb5e/LICENSE) · [pubspec.yaml](https://github.com/flutter/samples/blob/a5bccd247163b1017d2eb9320cf3b94a95ccfb5e/pubspec.yaml) · [main.yml](https://github.com/flutter/samples/blob/a5bccd247163b1017d2eb9320cf3b94a95ccfb5e/.github/workflows/main.yml) |

<a id="ch-framelink-mcp-for-figma-figma-context-mcp"></a>

### Framelink MCP for Figma (Figma-Context-MCP)

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/GLips/Figma-Context-MCP |
| License | MIT |
| Phiên bản đã đọc | `c083d65c7e002923e7cb98f4e3bdafb105e90f6d` (commit 2026-06-24) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE, package.json, server.json, .github/workflows/ci.yml; chưa chạy upstream |
| Bảo trì | Ít hoạt động (commit cuối 2026-06-24) |
| Nhận định | MCP đưa dữ liệu Figma REST rút gọn cho agent. Có module src/telemetry nhưng README không nói (catalog ghi PostHog bật sẵn, tắt bằng --no-telemetry); server.json lệch phiên bản với package.json. Nhánh chính đứng từ 24/6/2026. |
| Nguồn | [README.md](https://github.com/GLips/Figma-Context-MCP/blob/c083d65c7e002923e7cb98f4e3bdafb105e90f6d/README.md) · [LICENSE](https://github.com/GLips/Figma-Context-MCP/blob/c083d65c7e002923e7cb98f4e3bdafb105e90f6d/LICENSE) · [package.json](https://github.com/GLips/Figma-Context-MCP/blob/c083d65c7e002923e7cb98f4e3bdafb105e90f6d/package.json) · [server.json](https://github.com/GLips/Figma-Context-MCP/blob/c083d65c7e002923e7cb98f4e3bdafb105e90f6d/server.json) · [ci.yml](https://github.com/GLips/Figma-Context-MCP/blob/c083d65c7e002923e7cb98f4e3bdafb105e90f6d/.github/workflows/ci.yml) |

<a id="ch-frontend-design-anthropic"></a>

### frontend-design (Anthropic)

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/anthropics/claude-plugins-official |
| License | Apache-2.0 (LICENSE trong thư mục plugin; repo claude-code gốc là độc quyền) |
| Phiên bản đã đọc | `65adb96f26deb662f6a993f74347d0ccd1a61a52` (commit 2026-11-23) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc plugins/frontend-design/LICENSE, plugins/frontend-design/.claude-plugin/plugin.json, plugins/frontend-design/skills/frontend-design/SKILL.md, plugins/frontend-design/skills/frontend-design/LICENSE.txt; chưa chạy upstream |
| Bảo trì | Hoạt động |
| Nhận định | Skill chính chủ ~71 dòng hướng dẫn tránh giao diện mặc định 'AI', nay phát triển ở anthropics/claude-plugins-official (plugin 1.1.1); marketplace của claude-code chỉ trỏ tới. Chỉ là hướng dẫn văn bản, không có cổng kiểm máy. Lưu ý: repo claude-code gốc có LICENSE độc quyền, còn thư mục plugin mang Apache-2.0. |
| Nguồn | [LICENSE](https://github.com/anthropics/claude-plugins-official/blob/65adb96f26deb662f6a993f74347d0ccd1a61a52/plugins/frontend-design/LICENSE) · [plugin.json](https://github.com/anthropics/claude-plugins-official/blob/65adb96f26deb662f6a993f74347d0ccd1a61a52/plugins/frontend-design/.claude-plugin/plugin.json) · [SKILL.md](https://github.com/anthropics/claude-plugins-official/blob/65adb96f26deb662f6a993f74347d0ccd1a61a52/plugins/frontend-design/skills/frontend-design/SKILL.md) · [LICENSE.txt](https://github.com/anthropics/claude-plugins-official/blob/65adb96f26deb662f6a993f74347d0ccd1a61a52/plugins/frontend-design/skills/frontend-design/LICENSE.txt) · [README.md](https://github.com/anthropics/claude-code/blob/50cdc7005318f630144c28217d1dada32e6ba762/plugins/README.md) · [marketplace.json](https://github.com/anthropics/claude-code/blob/50cdc7005318f630144c28217d1dada32e6ba762/.claude-plugin/marketplace.json) |

<a id="ch-garden-skills"></a>

### garden-skills

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/ConardLi/garden-skills |
| License | MIT (không ghi chủ sở hữu) |
| Phiên bản đã đọc | `f2d7adeaf53dcce3d0eb19cbffe8c04f4c636c2a` (commit 2026-11-19) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.ja-JP.md, LICENSE, package.json, .github/workflows/validate-skills.yml; chưa chạy upstream |
| Bảo trì | Hoạt động |
| Nhận định | Bộ 6 skill agent (thiết kế web, video, bài viết, ảnh…). LICENSE MIT không ghi chủ sở hữu. Repo vẫn phát lại file tự nhận là system prompt 'Claude Design' trong dist/prompts, nguồn gốc không rõ — rủi ro bản quyền khi dùng lại. |
| Nguồn | [README.ja-JP.md](https://github.com/ConardLi/garden-skills/blob/f2d7adeaf53dcce3d0eb19cbffe8c04f4c636c2a/README.ja-JP.md) · [LICENSE](https://github.com/ConardLi/garden-skills/blob/f2d7adeaf53dcce3d0eb19cbffe8c04f4c636c2a/LICENSE) · [package.json](https://github.com/ConardLi/garden-skills/blob/f2d7adeaf53dcce3d0eb19cbffe8c04f4c636c2a/package.json) · [validate-skills.yml](https://github.com/ConardLi/garden-skills/blob/f2d7adeaf53dcce3d0eb19cbffe8c04f4c636c2a/.github/workflows/validate-skills.yml) |

<a id="ch-gluestack-ui"></a>

### gluestack-ui

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/gluestack/gluestack-ui |
| License | MIT (chỉ trong packages/gluestack-ui/LICENSE) |
| Phiên bản đã đọc | `b712c8541c85d57becbd1a1b2ba150a369223eb6` (commit 2026-09-02) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, packages/gluestack-ui/LICENSE, packages/gluestack-ui/package.json, .github/workflows/expo-latest.yml; chưa chạy upstream |
| Bảo trì | Ít hoạt động (commit cuối 2026-09-02) |
| Nhận định | Thư viện component copy-paste cho React Native/Expo trên NativeWind; bản hiện tại là v5 (catalog ghi v3). Gốc repo không có LICENSE, chỉ packages/gluestack-ui có MIT. Commit cuối 2/9/2026. |
| Nguồn | [README.md](https://github.com/gluestack/gluestack-ui/blob/b712c8541c85d57becbd1a1b2ba150a369223eb6/README.md) · [LICENSE](https://github.com/gluestack/gluestack-ui/blob/b712c8541c85d57becbd1a1b2ba150a369223eb6/packages/gluestack-ui/LICENSE) · [package.json](https://github.com/gluestack/gluestack-ui/blob/b712c8541c85d57becbd1a1b2ba150a369223eb6/packages/gluestack-ui/package.json) · [expo-latest.yml](https://github.com/gluestack/gluestack-ui/blob/b712c8541c85d57becbd1a1b2ba150a369223eb6/.github/workflows/expo-latest.yml) |

<a id="ch-golden-layout"></a>

### Golden Layout

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/golden-layout/golden-layout |
| License | MIT |
| Phiên bản đã đọc | `b053a23e2d9ea308810559370553a592a0e4bfae` (commit 2026-01-25) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE, package.json, .github/workflows/CI.yml; chưa chạy upstream |
| Bảo trì | Ít hoạt động (commit cuối 2026-01-25, vẫn 2.6.0) |
| Nhận định | Trình quản lý layout docking kéo-thả cho web, có popup window và API lưu/tải layout. Vẫn ở 2.6.0, chỉ có sửa nhỏ; không nên chọn cho dự án mới. |
| Nguồn | [README.md](https://github.com/golden-layout/golden-layout/blob/b053a23e2d9ea308810559370553a592a0e4bfae/README.md) · [LICENSE](https://github.com/golden-layout/golden-layout/blob/b053a23e2d9ea308810559370553a592a0e4bfae/LICENSE) · [package.json](https://github.com/golden-layout/golden-layout/blob/b053a23e2d9ea308810559370553a592a0e4bfae/package.json) · [CI.yml](https://github.com/golden-layout/golden-layout/blob/b053a23e2d9ea308810559370553a592a0e4bfae/.github/workflows/CI.yml) |

<a id="ch-google-stitch"></a>

### Google Stitch

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://stitch.withgoogle.com (chuyển hướng sang https://stitch.google.com/) |
| License | Độc quyền (dịch vụ đóng) |
| Phiên bản đã đọc | Trang web, không có SHA |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc trang chính (title, meta description); chưa chạy upstream |
| Bảo trì | Không rõ (dịch vụ còn trực tuyến) |
| Nhận định | Dịch vụ đóng của Google sinh UI cho app mobile và web bằng AI; trang chủ là ứng dụng web nên chỉ đọc được mô tả. Google công bố chuẩn DESIGN.md gắn với Stitch (xem mục 06 §7c). |
| Nguồn | [Trang chính](https://stitch.google.com/) |

<a id="ch-gov-uk-frontend"></a>

### GOV.UK Frontend

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/alphagov/govuk-frontend |
| License | MIT |
| Phiên bản đã đọc | `d6cb3427cdbb2a4c66095fb209da57843161176a` (commit 2026-11-23) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE.txt, package.json, .github/workflows/tests.yml; chưa chạy upstream |
| Bảo trì | Hoạt động |
| Nhận định | Mã frontend của GOV.UK Design System do GDS duy trì, có workflow test, accessibility và screenshot. Hợp làm chuẩn tham khảo a11y; style gắn nhận diện chính phủ Anh. |
| Nguồn | [README.md](https://github.com/alphagov/govuk-frontend/blob/d6cb3427cdbb2a4c66095fb209da57843161176a/README.md) · [LICENSE.txt](https://github.com/alphagov/govuk-frontend/blob/d6cb3427cdbb2a4c66095fb209da57843161176a/LICENSE.txt) · [package.json](https://github.com/alphagov/govuk-frontend/blob/d6cb3427cdbb2a4c66095fb209da57843161176a/package.json) · [tests.yml](https://github.com/alphagov/govuk-frontend/blob/d6cb3427cdbb2a4c66095fb209da57843161176a/.github/workflows/tests.yml) |

<a id="ch-grommet"></a>

### Grommet

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/grommet/grommet |
| License | Apache-2.0 |
| Phiên bản đã đọc | `b3095d571a1d95fb3ae1a1a2c09c235eb6cb0eb0` (commit 2026-11-20) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE, package.json; chưa chạy upstream |
| Bảo trì | Hoạt động |
| Nhận định | Thư viện React của HPE, chú trọng a11y; bản 2.58.0 hỗ trợ React tới 19 nhưng bắt buộc styled-components. CI chính trên CircleCI/Chromatic. |
| Nguồn | [README.md](https://github.com/grommet/grommet/blob/b3095d571a1d95fb3ae1a1a2c09c235eb6cb0eb0/README.md) · [LICENSE](https://github.com/grommet/grommet/blob/b3095d571a1d95fb3ae1a1a2c09c235eb6cb0eb0/LICENSE) · [package.json](https://github.com/grommet/grommet/blob/b3095d571a1d95fb3ae1a1a2c09c235eb6cb0eb0/package.json) |

<a id="ch-hallmark"></a>

### Hallmark

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/Nutlope/hallmark |
| License | MIT |
| Phiên bản đã đọc | `04977e15f3dfd6ee4b74c887dac3eb52665d6c92` (commit 2026-11-11) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE, package.json, .github/workflows/verify.yml; chưa chạy upstream |
| Bảo trì | Hoạt động |
| Nhận định | Skill thiết kế trang 'không trông như AI làm' cho Claude Code/Codex/Cursor/OpenCode của Together AI; v2 có 50 theme, tầng gate Floor/Reflex và lint trong trình duyệt thật. Số gate và hiệu quả là tuyên bố của tác giả **(chưa xác minh)**; ảnh hotlink cần ghi công. |
| Nguồn | [README.md](https://github.com/Nutlope/hallmark/blob/04977e15f3dfd6ee4b74c887dac3eb52665d6c92/README.md) · [LICENSE](https://github.com/Nutlope/hallmark/blob/04977e15f3dfd6ee4b74c887dac3eb52665d6c92/LICENSE) · [package.json](https://github.com/Nutlope/hallmark/blob/04977e15f3dfd6ee4b74c887dac3eb52665d6c92/package.json) · [verify.yml](https://github.com/Nutlope/hallmark/blob/04977e15f3dfd6ee4b74c887dac3eb52665d6c92/.github/workflows/verify.yml) |

<a id="ch-harmony-evil-martians"></a>

### Harmony (Evil Martians)

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/evilmartians/harmony |
| License | MIT |
| Phiên bản đã đọc | `6dae4f337b7a2f56fb3a8222c3f67760b8d23c84` (commit 2026-07-24) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE, package.json, .github/workflows/tests.yaml; chưa chạy upstream |
| Bảo trì | Ít hoạt động (commit cuối 2026-07-24) |
| Nhận định | Bảng màu OKLCH có tương phản đều theo mức sáng, có bản P3, thay được bảng Tailwind. Dựa trên APCA (license APCA hạn chế, xem mục 06 §7t). |
| Nguồn | [README.md](https://github.com/evilmartians/harmony/blob/6dae4f337b7a2f56fb3a8222c3f67760b8d23c84/README.md) · [LICENSE](https://github.com/evilmartians/harmony/blob/6dae4f337b7a2f56fb3a8222c3f67760b8d23c84/LICENSE) · [package.json](https://github.com/evilmartians/harmony/blob/6dae4f337b7a2f56fb3a8222c3f67760b8d23c84/package.json) · [tests.yaml](https://github.com/evilmartians/harmony/blob/6dae4f337b7a2f56fb3a8222c3f67760b8d23c84/.github/workflows/tests.yaml) |

<a id="ch-headless-ui"></a>

### Headless UI

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/tailwindlabs/headlessui |
| License | MIT |
| Phiên bản đã đọc | `eea57cf46fd6767ed1059012f7073b88eb159fba` (commit 2026-04-13) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE, package.json, .github/workflows/main.yml; chưa chạy upstream |
| Bảo trì | Ít hoạt động (commit cuối 2026-04-13) |
| Nhận định | Component headless, không style, a11y cho React và Vue của Tailwind Labs. Nhánh chính đứng từ 13/4/2026; dự án mới nên cân nhắc Base UI hoặc React Aria. |
| Nguồn | [README.md](https://github.com/tailwindlabs/headlessui/blob/eea57cf46fd6767ed1059012f7073b88eb159fba/README.md) · [LICENSE](https://github.com/tailwindlabs/headlessui/blob/eea57cf46fd6767ed1059012f7073b88eb159fba/LICENSE) · [package.json](https://github.com/tailwindlabs/headlessui/blob/eea57cf46fd6767ed1059012f7073b88eb159fba/package.json) · [main.yml](https://github.com/tailwindlabs/headlessui/blob/eea57cf46fd6767ed1059012f7073b88eb159fba/.github/workflows/main.yml) |

<a id="ch-heroui-ten-cu-nextui"></a>

### HeroUI (tên cũ NextUI)

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/heroui-inc/heroui |
| License | Apache-2.0 |
| Phiên bản đã đọc | `0ef329698a0be930e96588c2a6c2f4717de08081` (commit 2026-11-23) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE, package.json, .github/workflows/QA.yaml; chưa chạy upstream |
| Bảo trì | Hoạt động |
| Nhận định | Thư viện React (tên cũ NextUI), v3 dựa trên React Aria và Tailwind v4, API compound component. Có MCP server và llms.txt cho agent. Nâng từ v2 lên v3 là thay đổi lớn. |
| Nguồn | [README.md](https://github.com/heroui-inc/heroui/blob/0ef329698a0be930e96588c2a6c2f4717de08081/README.md) · [LICENSE](https://github.com/heroui-inc/heroui/blob/0ef329698a0be930e96588c2a6c2f4717de08081/LICENSE) · [package.json](https://github.com/heroui-inc/heroui/blob/0ef329698a0be930e96588c2a6c2f4717de08081/package.json) · [QA.yaml](https://github.com/heroui-inc/heroui/blob/0ef329698a0be930e96588c2a6c2f4717de08081/.github/workflows/QA.yaml) |

<a id="ch-huashu-design"></a>

### huashu-design

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/alchaincyf/huashu-design |
| License | MIT |
| Phiên bản đã đọc | `59065698ad63f87ea1532c126c87f488d4f93fd6` (commit 2026-11-23) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.en.md, LICENSE, package.json; chưa chạy upstream |
| Bảo trì | Hoạt động |
| Nhận định | Skill tiếng Trung biến một câu yêu cầu thành HTML, PPTX, MP4, PDF; scripts có design_lint.py, html2pptx.js, render-video.js. Tốn token, cần Playwright; repo không có CI nên chất lượng script **(chưa xác minh)**. |
| Nguồn | [README.en.md](https://github.com/alchaincyf/huashu-design/blob/59065698ad63f87ea1532c126c87f488d4f93fd6/README.en.md) · [LICENSE](https://github.com/alchaincyf/huashu-design/blob/59065698ad63f87ea1532c126c87f488d4f93fd6/LICENSE) · [package.json](https://github.com/alchaincyf/huashu-design/blob/59065698ad63f87ea1532c126c87f488d4f93fd6/package.json) |

<a id="ch-hyperui"></a>

### HyperUI

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/markmead/hyperui |
| License | MIT |
| Phiên bản đã đọc | `81842332a0e2185c19fc07e19a779c14477e6b16` (commit 2026-11-23) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE, package.json, .github/workflows/ci.yml; chưa chạy upstream |
| Bảo trì | Hoạt động |
| Nhận định | Bộ mẫu HTML + Tailwind copy-paste miễn phí (marketing, app, eCommerce). Không có gói npm; repo là site Astro + playwright. |
| Nguồn | [README.md](https://github.com/markmead/hyperui/blob/81842332a0e2185c19fc07e19a779c14477e6b16/README.md) · [LICENSE](https://github.com/markmead/hyperui/blob/81842332a0e2185c19fc07e19a779c14477e6b16/LICENSE) · [package.json](https://github.com/markmead/hyperui/blob/81842332a0e2185c19fc07e19a779c14477e6b16/package.json) · [ci.yml](https://github.com/markmead/hyperui/blob/81842332a0e2185c19fc07e19a779c14477e6b16/.github/workflows/ci.yml) |

<a id="ch-intro-js"></a>

### Intro.js

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/usablica/intro.js |
| License | AGPL-3.0 + license thương mại |
| Phiên bản đã đọc | `0c5bcfc7598f6cce7b36999f44c9533ef70385e3` (commit 2026-11-20) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, license.md, package.json, .github/workflows/nodejs.yml; chưa chạy upstream |
| Bảo trì | Hoạt động |
| Nhận định | Thư viện tour/onboarding sản phẩm, còn phát hành (8.7.0). Mã AGPL-3.0, dùng thương mại phải mua license; thay bằng driver.js hoặc react-joyride (MIT) nếu cần tránh. |
| Nguồn | [README.md](https://github.com/usablica/intro.js/blob/0c5bcfc7598f6cce7b36999f44c9533ef70385e3/README.md) · [license.md](https://github.com/usablica/intro.js/blob/0c5bcfc7598f6cce7b36999f44c9533ef70385e3/license.md) · [package.json](https://github.com/usablica/intro.js/blob/0c5bcfc7598f6cce7b36999f44c9533ef70385e3/package.json) · [nodejs.yml](https://github.com/usablica/intro.js/blob/0c5bcfc7598f6cce7b36999f44c9533ef70385e3/.github/workflows/nodejs.yml) |

<a id="ch-ionic-framework"></a>

### Ionic Framework

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/ionic-team/ionic-framework |
| License | MIT |
| Phiên bản đã đọc | `2ad93e5500c3d1e46b1d26e934ed41da642b7fbf` (commit 2026-11-20) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE, core/package.json, .github/workflows/build.yml; chưa chạy upstream |
| Bảo trì | Hoạt động |
| Nhận định | Bộ công cụ app đa nền tảng trên Web Components (Stencil) với binding Angular/React/Vue, phát hành đều đặn (9.0.13). Do OutSystems nắm; telemetry của Ionic CLI không kiểm lần này. |
| Nguồn | [README.md](https://github.com/ionic-team/ionic-framework/blob/2ad93e5500c3d1e46b1d26e934ed41da642b7fbf/README.md) · [LICENSE](https://github.com/ionic-team/ionic-framework/blob/2ad93e5500c3d1e46b1d26e934ed41da642b7fbf/LICENSE) · [package.json](https://github.com/ionic-team/ionic-framework/blob/2ad93e5500c3d1e46b1d26e934ed41da642b7fbf/core/package.json) · [build.yml](https://github.com/ionic-team/ionic-framework/blob/2ad93e5500c3d1e46b1d26e934ed41da642b7fbf/.github/workflows/build.yml) |

<a id="ch-logo-design-skill"></a>

### logo-design-skill

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/kaankiziltug/logo-design-skill |
| License | MIT (TRADEMARKS.md loại trừ 1.432 logo thương hiệu) |
| Phiên bản đã đọc | `e9eaddc07895575253d6663320354a708f53e955` (commit 2026-11-13) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE, TRADEMARKS.md; chưa chạy upstream |
| Bảo trì | Hoạt động (commit cuối 2026-11-13) |
| Nhận định | Skill quy trình thiết kế logo kèm script Python và thư viện 1.432 SVG logo thật để tham khảo. TRADEMARKS.md nói rõ MIT không áp dụng cho thư mục logo và chỉ dùng để học, không sao chép; có workflow test. |
| Nguồn | [README.md](https://github.com/kaankiziltug/logo-design-skill/blob/e9eaddc07895575253d6663320354a708f53e955/README.md) · [LICENSE](https://github.com/kaankiziltug/logo-design-skill/blob/e9eaddc07895575253d6663320354a708f53e955/LICENSE) · [TRADEMARKS.md](https://github.com/kaankiziltug/logo-design-skill/blob/e9eaddc07895575253d6663320354a708f53e955/TRADEMARKS.md) |

<a id="ch-lucide"></a>

### Lucide

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/lucide-icons/lucide |
| License | ISC AND MIT (icon gốc Feather) |
| Phiên bản đã đọc | `c26ce5515667640ca2753e095ba319d225fc0d8d` (commit 2026-11-23) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE, package.json; chưa chạy upstream |
| Bảo trì | Hoạt động (commit cuối 2026-11-23) |
| Nhận định | Bộ icon SVG cộng đồng (fork Feather) với nhiều gói framework và CI dày (lint icon, release, preview PR). LICENSE là ISC kèm đoạn MIT cho danh sách icon gốc Feather, nên công cụ quét có thể báo NOASSERTION; có BRAND_LOGOS_STATEMENT.md. |
| Nguồn | [README.md](https://github.com/lucide-icons/lucide/blob/c26ce5515667640ca2753e095ba319d225fc0d8d/README.md) · [LICENSE](https://github.com/lucide-icons/lucide/blob/c26ce5515667640ca2753e095ba319d225fc0d8d/LICENSE) · [package.json](https://github.com/lucide-icons/lucide/blob/c26ce5515667640ca2753e095ba319d225fc0d8d/package.json) |

<a id="ch-m3e-canvas"></a>

### m3e-canvas

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/lnkiai/m3e-canvas |
| License | MIT (+ NOTICE: mã port Apache-2.0 từ material-components-android) |
| Phiên bản đã đọc | `9cbf6eb9ae30cb6c368c4e68742196ef358d7e94` (commit 2026-11-23) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.ja.md, LICENSE, NOTICE, package.json; chưa chạy upstream |
| Bảo trì | Hoạt động (commit cuối 2026-11-23) |
| Nhận định | Canvas trên trình duyệt để dựng màn Material 3 Expressive rồi xuất prompt cho agent; app Next.js tĩnh có CI và deploy. NOTICE ghi phần loading indicator port từ material-components-android (Apache-2.0); việc lưu API key plaintext trong localStorage là nhận định cũ, lần này chưa đọc lại mã. |
| Nguồn | [README.ja.md](https://github.com/lnkiai/m3e-canvas/blob/9cbf6eb9ae30cb6c368c4e68742196ef358d7e94/README.ja.md) · [LICENSE](https://github.com/lnkiai/m3e-canvas/blob/9cbf6eb9ae30cb6c368c4e68742196ef358d7e94/LICENSE) · [NOTICE](https://github.com/lnkiai/m3e-canvas/blob/9cbf6eb9ae30cb6c368c4e68742196ef358d7e94/NOTICE) · [package.json](https://github.com/lnkiai/m3e-canvas/blob/9cbf6eb9ae30cb6c368c4e68742196ef358d7e94/package.json) |

<a id="ch-mantine"></a>

### Mantine

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/mantinedev/mantine |
| License | MIT |
| Phiên bản đã đọc | `8f2ae606f8a37d5971f8315685e7daab44d9fbe2` (commit 2026-11-23) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE, package.json; chưa chạy upstream |
| Bảo trì | Hoạt động (commit cuối 2026-11-23) |
| Nhận định | Thư viện component React lớn, monorepo bản 9.8.2, có AGENTS.md/CLAUDE.md và workflow test/publish. Phù hợp làm nền UI tổng quát; không thấy rủi ro license. |
| Nguồn | [README.md](https://github.com/mantinedev/mantine/blob/8f2ae606f8a37d5971f8315685e7daab44d9fbe2/README.md) · [LICENSE](https://github.com/mantinedev/mantine/blob/8f2ae606f8a37d5971f8315685e7daab44d9fbe2/LICENSE) · [package.json](https://github.com/mantinedev/mantine/blob/8f2ae606f8a37d5971f8315685e7daab44d9fbe2/package.json) |

<a id="ch-material-3-canonical-layouts"></a>

### Material 3 canonical layouts

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://developer.android.com/develop/ui/compose/layouts/adaptive/canonical-layouts |
| License | Không áp dụng (tài liệu web; theo Content License của trang) |
| Phiên bản đã đọc | Trang web, đọc 2026-11-23 (không có SHA) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc https://developer.android.com/develop/ui/compose/layouts/adaptive/canonical-layouts; chưa chạy upstream |
| Bảo trì | Đang cập nhật |
| Nhận định | Trang hướng dẫn chính thức Android về ba layout canonical: list-detail, feed, supporting pane, kèm mẫu Compose (cập nhật 2026-11-10). Ngưỡng breakpoint 600/840dp không nằm trên trang này mà ở trang window size classes được liên kết. |
| Nguồn | [canonical-layouts](https://developer.android.com/develop/ui/compose/layouts/adaptive/canonical-layouts) |

<a id="ch-material-web"></a>

### Material Web

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/material-components/material-web |
| License | Apache-2.0 |
| Phiên bản đã đọc | `a0bab1d9448bbcecab053e6085b8ec621e4cae3e` (commit 2026-11-20) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE, package.json; chưa chạy upstream |
| Bảo trì | README tự ghi chế độ bảo trì (commit cuối 2026-11-20) |
| Nhận định | Web component Material 3 chính chủ Google (@material/web 2.5.0), có release-please và test. README tự ghi MWC đang ở chế độ bảo trì chờ người duy trì mới (discussion #5642), nên không nên chọn làm nền lâu dài dù vẫn có commit nhỏ. |
| Nguồn | [README.md](https://github.com/material-components/material-web/blob/a0bab1d9448bbcecab053e6085b8ec621e4cae3e/README.md) · [LICENSE](https://github.com/material-components/material-web/blob/a0bab1d9448bbcecab053e6085b8ec621e4cae3e/LICENSE) · [package.json](https://github.com/material-components/material-web/blob/a0bab1d9448bbcecab053e6085b8ec621e4cae3e/package.json) |

<a id="ch-mitosis"></a>

### Mitosis

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/BuilderIO/mitosis |
| License | MIT |
| Phiên bản đã đọc | `2de76e9064d9e7916c5309c0a31206383403ae9d` (commit 2026-10-28) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.MD, LICENSE, package.json; chưa chạy upstream |
| Bảo trì | Nhịp thấp (commit cuối 2026-10-28) |
| Nhận định | Viết component một lần rồi biên dịch sang nhiều framework (Builder.io). Commit mới nhất 28/10/2026, khớp nhận định nhịp phát triển đã giảm; nên thử kỹ đầu ra từng framework trước khi dùng. |
| Nguồn | [README.MD](https://github.com/BuilderIO/mitosis/blob/2de76e9064d9e7916c5309c0a31206383403ae9d/README.MD) · [LICENSE](https://github.com/BuilderIO/mitosis/blob/2de76e9064d9e7916c5309c0a31206383403ae9d/LICENSE) · [package.json](https://github.com/BuilderIO/mitosis/blob/2de76e9064d9e7916c5309c0a31206383403ae9d/package.json) |

<a id="ch-mobbin"></a>

### Mobbin

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://mobbin.com |
| License | proprietary |
| Phiên bản đã đọc | Trang web, đọc 2026-11-23 (không có SHA) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc https://mobbin.com, https://mobbin.com/pricing.md; chưa chạy upstream |
| Bảo trì | Đang cập nhật |
| Nhận định | Thư viện ảnh chụp màn hình app/web thật để lấy cảm hứng, không có mã. Trang giá (pricing.md, cập nhật 2026-09-11) xác nhận Pro $10/tháng trả theo năm ($15 theo quý), Pro có MCP, REST API chỉ từ gói Team. |
| Nguồn | [mobbin.com](https://mobbin.com) · [pricing.md](https://mobbin.com/pricing.md) |

<a id="ch-morphic"></a>

### Morphic

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/miurla/morphic |
| License | Apache-2.0 |
| Phiên bản đã đọc | `41c97193f82b8a7bd15dae2cc565ce7a83fe4508` (commit 2026-11-23) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE, package.json; chưa chạy upstream |
| Bảo trì | Hoạt động (commit cuối 2026-11-23) |
| Nhận định | Answer engine kiểu generative UI (Next.js), bản 1.10.0, có Docker, CI lint/test, eval và release. Telemetry/instrumentation cần cấu hình qua biến môi trường (nhận định cũ, lần này chưa đọc lại mã). |
| Nguồn | [README.md](https://github.com/miurla/morphic/blob/41c97193f82b8a7bd15dae2cc565ce7a83fe4508/README.md) · [LICENSE](https://github.com/miurla/morphic/blob/41c97193f82b8a7bd15dae2cc565ce7a83fe4508/LICENSE) · [package.json](https://github.com/miurla/morphic/blob/41c97193f82b8a7bd15dae2cc565ce7a83fe4508/package.json) |

<a id="ch-mui"></a>

### MUI

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/mui/material-ui |
| License | MIT |
| Phiên bản đã đọc | `09da8e5c19cfcee5b89cdb32d8b204e7492b728e` (commit 2026-11-23) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE, package.json; chưa chạy upstream |
| Bảo trì | Hoạt động (commit cuối 2026-11-23) |
| Nhận định | Material UI, thư viện component React phổ biến nhất; nhánh mặc định đang ở 10.0.0-alpha.0, có skills/AGENTS.md và CI rất đầy đủ (CodeQL, scorecards). Lưu ý nhánh chính là alpha v10, bản ổn định cần chọn theo npm. |
| Nguồn | [README.md](https://github.com/mui/material-ui/blob/09da8e5c19cfcee5b89cdb32d8b204e7492b728e/README.md) · [LICENSE](https://github.com/mui/material-ui/blob/09da8e5c19cfcee5b89cdb32d8b204e7492b728e/LICENSE) · [package.json](https://github.com/mui/material-ui/blob/09da8e5c19cfcee5b89cdb32d8b204e7492b728e/package.json) |

<a id="ch-naive-ui"></a>

### Naive UI

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/tusen-ai/naive-ui |
| License | MIT |
| Phiên bản đã đọc | `ce8dc4d8b8b394fbbc7d9f00c2a02c77d8124ecc` (commit 2026-11-14) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE, package.json; chưa chạy upstream |
| Bảo trì | Hoạt động (commit cuối 2026-11-14) |
| Nhận định | Thư viện component Vue 3, bản 2.45.3, có AGENTS.md và workflow Node.js test. Ổn cho dự án Vue; số issue mở cao là nhận định cũ, chưa đếm lại. |
| Nguồn | [README.md](https://github.com/tusen-ai/naive-ui/blob/ce8dc4d8b8b394fbbc7d9f00c2a02c77d8124ecc/README.md) · [LICENSE](https://github.com/tusen-ai/naive-ui/blob/ce8dc4d8b8b394fbbc7d9f00c2a02c77d8124ecc/LICENSE) · [package.json](https://github.com/tusen-ai/naive-ui/blob/ce8dc4d8b8b394fbbc7d9f00c2a02c77d8124ecc/package.json) |

<a id="ch-nativewind"></a>

### NativeWind

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/nativewind/nativewind |
| License | MIT |
| Phiên bản đã đọc | `b56a0289e22a52839b1305e41381697413ae2232` (commit 2026-11-19) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE, package.json; chưa chạy upstream |
| Bảo trì | Hoạt động (commit cuối 2026-11-19) |
| Nhận định | Tailwind cho React Native; nhánh mặc định đã là 5.0.0-preview.4, có CI, release nightly và thư mục skills. Chọn v4 cho sản xuất, v5 còn preview. |
| Nguồn | [README.md](https://github.com/nativewind/nativewind/blob/b56a0289e22a52839b1305e41381697413ae2232/README.md) · [LICENSE](https://github.com/nativewind/nativewind/blob/b56a0289e22a52839b1305e41381697413ae2232/LICENSE) · [package.json](https://github.com/nativewind/nativewind/blob/b56a0289e22a52839b1305e41381697413ae2232/package.json) |

<a id="ch-neobrutalism-components"></a>

### neobrutalism-components

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/ekmas/neobrutalism-components |
| License | MIT |
| Phiên bản đã đọc | `f3c4d42973819ab5cf18697d08d6bd46f384d335` (commit 2026-11-15) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE, package.json; chưa chạy upstream |
| Bảo trì | Hoạt động (commit cuối 2026-11-15) |
| Nhận định | Registry shadcn phong cách neobrutalism; README hiện không còn dòng "no longer maintained" và repo có commit 15/11/2026. Không có thư mục .github/workflows, tức không có CI trên GitHub. |
| Nguồn | [README.md](https://github.com/ekmas/neobrutalism-components/blob/f3c4d42973819ab5cf18697d08d6bd46f384d335/README.md) · [LICENSE](https://github.com/ekmas/neobrutalism-components/blob/f3c4d42973819ab5cf18697d08d6bd46f384d335/LICENSE) · [package.json](https://github.com/ekmas/neobrutalism-components/blob/f3c4d42973819ab5cf18697d08d6bd46f384d335/package.json) |

<a id="ch-next-shadcn-dashboard-starter"></a>

### next-shadcn-dashboard-starter

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/Kiranism/next-shadcn-dashboard-starter |
| License | MIT |
| Phiên bản đã đọc | `89f4e257650905a3a206f8449757f981bb811306` (commit 2026-11-16) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE, package.json; chưa chạy upstream |
| Bảo trì | Hoạt động (commit cuối 2026-11-16) |
| Nhận định | Starter dashboard Next.js + shadcn với nhiều trang mẫu, có Dockerfile, AGENTS.md/CLAUDE.md. Phụ thuộc dịch vụ xác thực bên ngoài (Clerk theo nhận định cũ) nên phải thay nếu muốn tự host trọn. |
| Nguồn | [README.md](https://github.com/Kiranism/next-shadcn-dashboard-starter/blob/89f4e257650905a3a206f8449757f981bb811306/README.md) · [LICENSE](https://github.com/Kiranism/next-shadcn-dashboard-starter/blob/89f4e257650905a3a206f8449757f981bb811306/LICENSE) · [package.json](https://github.com/Kiranism/next-shadcn-dashboard-starter/blob/89f4e257650905a3a206f8449757f981bb811306/package.json) |

<a id="ch-ng-zorro"></a>

### NG-ZORRO

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/NG-ZORRO/ng-zorro-antd |
| License | MIT |
| Phiên bản đã đọc | `d3093bfa34cada0c6429d62d73654aa66fe1f130` (commit 2026-11-21) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README-zh_CN.md, LICENSE, package.json; chưa chạy upstream |
| Bảo trì | Hoạt động (commit cuối 2026-11-21) |
| Nhận định | Ant Design cho Angular (README yêu cầu Angular ^22), có AGENTS.md, .mcp.json và cấu hình cho nhiều agent. CI chính chạy qua azure-pipelines.yml, GitHub Actions chỉ có sync-styles. |
| Nguồn | [README-zh_CN.md](https://github.com/NG-ZORRO/ng-zorro-antd/blob/d3093bfa34cada0c6429d62d73654aa66fe1f130/README-zh_CN.md) · [LICENSE](https://github.com/NG-ZORRO/ng-zorro-antd/blob/d3093bfa34cada0c6429d62d73654aa66fe1f130/LICENSE) · [package.json](https://github.com/NG-ZORRO/ng-zorro-antd/blob/d3093bfa34cada0c6429d62d73654aa66fe1f130/package.json) |

<a id="ch-oat-ui"></a>

### Oat UI

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/knadh/oat |
| License | MIT |
| Phiên bản đã đọc | `9e9338096548347644b5c4c5f800e5af058440fe` (commit 2026-11-01) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE, package.json; chưa chạy upstream |
| Bảo trì | Hoạt động (commit cuối 2026-11-01) |
| Nhận định | Thư viện HTML/CSS ngữ nghĩa nhỏ gọn của Kailash Nadh, không phụ thuộc. Chỉ có workflow publish, không có test; version trong package.json là placeholder, phiên bản thật lấy từ tag. |
| Nguồn | [README.md](https://github.com/knadh/oat/blob/9e9338096548347644b5c4c5f800e5af058440fe/README.md) · [LICENSE](https://github.com/knadh/oat/blob/9e9338096548347644b5c4c5f800e5af058440fe/LICENSE) · [package.json](https://github.com/knadh/oat/blob/9e9338096548347644b5c4c5f800e5af058440fe/package.json) |

<a id="ch-official-design-md-voltagent"></a>

### official-design-md (VoltAgent)

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/VoltAgent/official-design-md |
| License | MIT |
| Phiên bản đã đọc | `7236b0562b219d12b778ef9cc66ac1e3422801ff` (commit 2026-09-21) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE; chưa chạy upstream |
| Bảo trì | Nhịp thấp (commit cuối 2026-09-21) |
| Nhận định | Danh mục DESIGN.md chính chủ của VoltAgent, repo chỉ gồm README và LICENSE. Commit cuối 21/09/2026; giá trị nằm ở các liên kết, cần tự kiểm từng file nguồn. |
| Nguồn | [README.md](https://github.com/VoltAgent/official-design-md/blob/7236b0562b219d12b778ef9cc66ac1e3422801ff/README.md) · [LICENSE](https://github.com/VoltAgent/official-design-md/blob/7236b0562b219d12b778ef9cc66ac1e3422801ff/LICENSE) |

<a id="ch-omi"></a>

### Omi

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/Tencent/omi |
| License | MIT (kèm thành phần bên thứ ba MIT: preact, polyfill) |
| Phiên bản đã đọc | `dd824ab22594fd3c6b8e31cd58a672e3c0f51126` (commit 2026-11-12) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.CN.md, LICENSE; chưa chạy upstream |
| Bảo trì | Hoạt động (commit cuối 2026-11-12) |
| Nhận định | Framework web components của Tencent (monorepo packages/). Không có .github/workflows nên không có CI trên GitHub, khớp nhận định cũ; LICENSE liệt kê thêm preact và polyfill cùng MIT. |
| Nguồn | [README.CN.md](https://github.com/Tencent/omi/blob/dd824ab22594fd3c6b8e31cd58a672e3c0f51126/README.CN.md) · [LICENSE](https://github.com/Tencent/omi/blob/dd824ab22594fd3c6b8e31cd58a672e3c0f51126/LICENSE) |

<a id="ch-once-ui-core"></a>

### Once UI core

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/once-ui-system/core |
| License | MIT |
| Phiên bản đã đọc | `f3a21a577e824c3ac47a3b2c1745db54bca10fac` (commit 2026-11-22) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE.md, package.json; chưa chạy upstream |
| Bảo trì | Hoạt động (commit cuối 2026-11-22) |
| Nhận định | Monorepo Once UI (block/thành phần Next.js), có CI, visual test và release. Cảnh báo CC BY-NC 4.0 thuộc repo riêng magic-portfolio, không nằm trong repo này. |
| Nguồn | [README.md](https://github.com/once-ui-system/core/blob/f3a21a577e824c3ac47a3b2c1745db54bca10fac/README.md) · [LICENSE.md](https://github.com/once-ui-system/core/blob/f3a21a577e824c3ac47a3b2c1745db54bca10fac/LICENSE.md) · [package.json](https://github.com/once-ui-system/core/blob/f3a21a577e824c3ac47a3b2c1745db54bca10fac/package.json) |

<a id="ch-onlook"></a>

### Onlook

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/onlook-dev/onlook |
| License | Apache-2.0 (NOTICE liệt kê phụ thuộc bên thứ ba, có gói độc quyền) |
| Phiên bản đã đọc | `089840c3525faec88e74347bd5f7e06c76c8b3d0` (commit 2026-11-21) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE, NOTICE, package.json; chưa chạy upstream |
| Bảo trì | Hoạt động (commit cuối 2026-11-21) |
| Nhận định | Visual editor cho app React, có CI và hướng dẫn build từ nguồn. NOTICE mới liệt kê phụ thuộc bên thứ ba, gồm cả gói độc quyền @anthropic-ai/claude-agent-sdk (đánh dấu cần rà soát), nên bản phân phối không thuần Apache-2.0. |
| Nguồn | [README.md](https://github.com/onlook-dev/onlook/blob/089840c3525faec88e74347bd5f7e06c76c8b3d0/README.md) · [LICENSE](https://github.com/onlook-dev/onlook/blob/089840c3525faec88e74347bd5f7e06c76c8b3d0/LICENSE) · [NOTICE](https://github.com/onlook-dev/onlook/blob/089840c3525faec88e74347bd5f7e06c76c8b3d0/NOTICE) · [package.json](https://github.com/onlook-dev/onlook/blob/089840c3525faec88e74347bd5f7e06c76c8b3d0/package.json) |

<a id="ch-opendesign"></a>

### OpenDesign

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/nexu-io/open-design |
| License | Apache-2.0 |
| Phiên bản đã đọc | `5fdcc3db1e31bd4fa70f673041b78e87977507c3` (commit 2026-11-23) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE, package.json; chưa chạy upstream |
| Bảo trì | Hoạt động (commit cuối 2026-11-23) |
| Nhận định | Workspace agent thiết kế local-first (bản 0.27.3), có PRIVACY.md, rất nhiều workflow release/CI tự động. Các rủi ro telemetry và cờ bỏ kiểm quyền agent là từ lần đọc mã 31/10/2026, lần này chưa đọc lại mã. |
| Nguồn | [README.md](https://github.com/nexu-io/open-design/blob/5fdcc3db1e31bd4fa70f673041b78e87977507c3/README.md) · [LICENSE](https://github.com/nexu-io/open-design/blob/5fdcc3db1e31bd4fa70f673041b78e87977507c3/LICENSE) · [package.json](https://github.com/nexu-io/open-design/blob/5fdcc3db1e31bd4fa70f673041b78e87977507c3/package.json) |

<a id="ch-openintelligentui-copilotkit"></a>

### OpenIntelligentUI (CopilotKit)

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/CopilotKit/OpenIntelligentUI |
| License | MIT |
| Phiên bản đã đọc | `8391a94c1c3939c679e40ddd7bfc08a9ef690e70` (commit 2026-10-13) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE, package.json; chưa chạy upstream |
| Bảo trì | Nhịp thấp (commit cuối 2026-10-13) |
| Nhận định | App mẫu Next.js + LangGraph trả lời bằng UI sinh động (A2UI/widget iframe), có một workflow CI. Commit cuối 13/10/2026; phụ thuộc router bên thứ ba và telemetry CopilotKit là nhận định cũ, lần này chưa đọc lại mã. |
| Nguồn | [README.md](https://github.com/CopilotKit/OpenIntelligentUI/blob/8391a94c1c3939c679e40ddd7bfc08a9ef690e70/README.md) · [LICENSE](https://github.com/CopilotKit/OpenIntelligentUI/blob/8391a94c1c3939c679e40ddd7bfc08a9ef690e70/LICENSE) · [package.json](https://github.com/CopilotKit/OpenIntelligentUI/blob/8391a94c1c3939c679e40ddd7bfc08a9ef690e70/package.json) |

<a id="ch-openpencil-open-pencil"></a>

### OpenPencil (open-pencil)

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/open-pencil/open-pencil |
| License | MIT + Apache-2.0 (phần Cloud, theo REUSE.toml) |
| Phiên bản đã đọc | `1814dcbd0a493924adc6518e5bd35f25a60a582e` (commit 2026-11-23) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE, REUSE.toml, package.json, Cargo.toml; chưa chạy upstream |
| Bảo trì | Hoạt động (commit cuối 2026-11-23) |
| Nhận định | Trình thiết kế TS/Vue + Tauri đọc/ghi .fig, bản 0.17.0, CI dày. REUSE.toml gán MIT cho toàn repo và Apache-2.0 cho server/portal Cloud, riêng giao thức client giữ MIT. |
| Nguồn | [README.md](https://github.com/open-pencil/open-pencil/blob/1814dcbd0a493924adc6518e5bd35f25a60a582e/README.md) · [LICENSE](https://github.com/open-pencil/open-pencil/blob/1814dcbd0a493924adc6518e5bd35f25a60a582e/LICENSE) · [REUSE.toml](https://github.com/open-pencil/open-pencil/blob/1814dcbd0a493924adc6518e5bd35f25a60a582e/REUSE.toml) · [package.json](https://github.com/open-pencil/open-pencil/blob/1814dcbd0a493924adc6518e5bd35f25a60a582e/package.json) · [Cargo.toml](https://github.com/open-pencil/open-pencil/blob/1814dcbd0a493924adc6518e5bd35f25a60a582e/Cargo.toml) |

<a id="ch-openpencil-zseven-w"></a>

### OpenPencil (ZSeven-W)

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/ZSeven-W/openpencil |
| License | MIT (kèm thư viện xác thực đóng prebuilt) |
| Phiên bản đã đọc | `c939f85cbb7689663e3ea647af47cb5f484583cc` (commit 2026-11-23) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.de.md, LICENSE, Cargo.toml, crates/op-auth-bridge/prebuilt; chưa chạy upstream |
| Bảo trì | Hoạt động (commit cuối 2026-11-23) |
| Nhận định | Trình vẽ vector AI-native bằng Rust (55 crate, bản 0.8.6), nhiều workflow phát hành đa nền tảng. crates/op-auth-bridge/prebuilt vẫn chứa thư viện tĩnh đóng theo từng target, ký bằng RELEASE-MANIFEST.sig, nên bản phát hành không thuần MIT. |
| Nguồn | [README.de.md](https://github.com/ZSeven-W/openpencil/blob/c939f85cbb7689663e3ea647af47cb5f484583cc/README.de.md) · [LICENSE](https://github.com/ZSeven-W/openpencil/blob/c939f85cbb7689663e3ea647af47cb5f484583cc/LICENSE) · [Cargo.toml](https://github.com/ZSeven-W/openpencil/blob/c939f85cbb7689663e3ea647af47cb5f484583cc/Cargo.toml) · [prebuilt](https://github.com/ZSeven-W/openpencil/tree/c939f85cbb7689663e3ea647af47cb5f484583cc/crates/op-auth-bridge/prebuilt) |

<a id="ch-openui-thesys"></a>

### OpenUI (Thesys)

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/thesysdev/openui |
| License | MIT |
| Phiên bản đã đọc | `e9662fe8e096f80e284ca892ea2dd37139d21e91` (commit 2026-11-23) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE, package.json; chưa chạy upstream |
| Bảo trì | Hoạt động (commit cuối 2026-11-23) |
| Nhận định | OpenUI Lang (spec + runtime đa framework) của Thesys, CI build/e2e/release đầy đủ. Telemetry postinstall và mẫu mặc định gọi api.thesys.dev là nhận định cũ, lần này chưa đọc lại mã. |
| Nguồn | [README.md](https://github.com/thesysdev/openui/blob/e9662fe8e096f80e284ca892ea2dd37139d21e91/README.md) · [LICENSE](https://github.com/thesysdev/openui/blob/e9662fe8e096f80e284ca892ea2dd37139d21e91/LICENSE) · [package.json](https://github.com/thesysdev/openui/blob/e9662fe8e096f80e284ca892ea2dd37139d21e91/package.json) |

<a id="ch-openui-w-b"></a>

### OpenUI (W&B)

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/wandb/openui |
| License | Apache-2.0 |
| Phiên bản đã đọc | `42d7ab4ab6650433486dfb12eb3783c393a3e475` (commit 2026-06-30) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE; chưa chạy upstream |
| Bảo trì | Nhịp thấp (commit cuối 2026-06-30) |
| Nhận định | App tự host sinh UI từ mô tả của W&B; commit mới nhất 30/06/2026, chỉ còn workflow docker. Rủi ro Weave tự bật qua WANDB_API_KEY/~/.netrc là nhận định cũ, chưa đọc lại mã. |
| Nguồn | [README.md](https://github.com/wandb/openui/blob/42d7ab4ab6650433486dfb12eb3783c393a3e475/README.md) · [LICENSE](https://github.com/wandb/openui/blob/42d7ab4ab6650433486dfb12eb3783c393a3e475/LICENSE) |

<a id="ch-panda-css"></a>

### Panda CSS

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/chakra-ui/panda |
| License | MIT |
| Phiên bản đã đọc | `af5cf02d63efefeb24b78a52037812b7c88c99cc` (commit 2026-11-21) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE.md, package.json, Cargo.toml; chưa chạy upstream |
| Bảo trì | Hoạt động (commit cuối 2026-11-21) |
| Nhận định | CSS-in-JS không runtime, có crate Rust (Cargo.toml), AGENTS.md, skills và CI quality/rust/release. Phù hợp hệ design token build-time. |
| Nguồn | [README.md](https://github.com/chakra-ui/panda/blob/af5cf02d63efefeb24b78a52037812b7c88c99cc/README.md) · [LICENSE.md](https://github.com/chakra-ui/panda/blob/af5cf02d63efefeb24b78a52037812b7c88c99cc/LICENSE.md) · [package.json](https://github.com/chakra-ui/panda/blob/af5cf02d63efefeb24b78a52037812b7c88c99cc/package.json) · [Cargo.toml](https://github.com/chakra-ui/panda/blob/af5cf02d63efefeb24b78a52037812b7c88c99cc/Cargo.toml) |

<a id="ch-pencil-evolus"></a>

### Pencil (Evolus)

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/evolus/pencil |
| License | GPL-2.0 |
| Phiên bản đã đọc | `3fc5856b60415068259a8916d17a14adcd6ecc7a` (commit 2026-10-22) |
| Kiểm chứng | 2026-11-23; code-read; đã đọc README.md, LICENSE.md, package.json, app/tools/api-server.js; chưa chạy upstream |
| Bảo trì | Hoạt động (HEAD 22/10/2026); không có `.github/workflows` (còn .travis.yml/appveyor.yml) |
| Nhận định | Công cụ wireframe desktop Electron, v4 thêm máy chủ MCP để agent vẽ lên canvas. Rủi ro: mã tại SHA này lắng nghe mọi interface với CORS * và bật mặc định, trái với README ("100% local-first", loopback); chưa thấy lớp xác thực trong api-server.js (chưa đọc hết callsite). Electron 16 đã hết hỗ trợ. |
| Nguồn | [README.md](https://github.com/evolus/pencil/blob/3fc5856b60415068259a8916d17a14adcd6ecc7a/README.md) · [LICENSE.md](https://github.com/evolus/pencil/blob/3fc5856b60415068259a8916d17a14adcd6ecc7a/LICENSE.md) · [package.json](https://github.com/evolus/pencil/blob/3fc5856b60415068259a8916d17a14adcd6ecc7a/package.json) · [app/tools/api-server.js](https://github.com/evolus/pencil/blob/3fc5856b60415068259a8916d17a14adcd6ecc7a/app/tools/api-server.js) |

<a id="ch-pixelmatch"></a>

### pixelmatch

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/mapbox/pixelmatch |
| License | ISC |
| Phiên bản đã đọc | `ab76f526ef951c0ec6284e314a700e161b1800e6` (commit 2026-10-06) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE, package.json, .github/workflows/node.yml; chưa chạy upstream |
| Bảo trì | Hoạt động (commit cuối 6/10/2026) |
| Nhận định | Thư viện so ảnh mức pixel nhỏ, không phụ thuộc, chạy trên typed array (Node và trình duyệt); hợp làm lõi cổng visual regression tự host. Độ chính xác cảm nhận màu là tuyên bố của tác giả **(chưa xác minh)**. |
| Nguồn | [README.md](https://github.com/mapbox/pixelmatch/blob/ab76f526ef951c0ec6284e314a700e161b1800e6/README.md) · [LICENSE](https://github.com/mapbox/pixelmatch/blob/ab76f526ef951c0ec6284e314a700e161b1800e6/LICENSE) · [package.json](https://github.com/mapbox/pixelmatch/blob/ab76f526ef951c0ec6284e314a700e161b1800e6/package.json) · [.github/workflows/node.yml](https://github.com/mapbox/pixelmatch/blob/ab76f526ef951c0ec6284e314a700e161b1800e6/.github/workflows/node.yml) |

<a id="ch-polaris"></a>

### Polaris

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/Shopify/polaris-react-archive |
| License | MIT (catalog cũ ghi null) |
| Phiên bản đã đọc | `3f7954ae42fabf26d63cee68c23ceebfd7ef0972` (commit 2026-09-10) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE.md, package.json; chưa chạy upstream |
| Bảo trì | Archived; README ghi "archived and unmaintained", Polaris React deprecated |
| Nhận định | Monorepo lịch sử của Polaris React (components, tokens, icons, stylelint-polaris). Không dùng cho dự án mới; Shopify hướng sang Polaris Web Components trên shopify.dev. Chỉ còn giá trị tham khảo token/pattern. |
| Nguồn | [README.md](https://github.com/Shopify/polaris-react-archive/blob/3f7954ae42fabf26d63cee68c23ceebfd7ef0972/README.md) · [LICENSE.md](https://github.com/Shopify/polaris-react-archive/blob/3f7954ae42fabf26d63cee68c23ceebfd7ef0972/LICENSE.md) · [package.json](https://github.com/Shopify/polaris-react-archive/blob/3f7954ae42fabf26d63cee68c23ceebfd7ef0972/package.json) |

<a id="ch-preline-ui"></a>

### Preline UI

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/htmlstreamofficial/preline |
| License | MIT + Preline UI Fair Use License |
| Phiên bản đã đọc | `0dfbc35c10360c2608fd134021bc1dbc18d8c8eb` (commit 2026-11-12) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE, package.json; chưa chạy upstream |
| Bảo trì | Hoạt động (HEAD 12/11/2026) |
| Nhận định | Thư viện component Tailwind kèm plugin JS headless; phần lớn block/template nằm trên site, không trong repo. Fair Use License cấm dùng tạo sản phẩm cạnh tranh và cho phép tác giả chấm dứt quyền — không phải MIT thuần, cần rà pháp lý trước khi tích hợp. |
| Nguồn | [README.md](https://github.com/htmlstreamofficial/preline/blob/0dfbc35c10360c2608fd134021bc1dbc18d8c8eb/README.md) · [LICENSE](https://github.com/htmlstreamofficial/preline/blob/0dfbc35c10360c2608fd134021bc1dbc18d8c8eb/LICENSE) · [package.json](https://github.com/htmlstreamofficial/preline/blob/0dfbc35c10360c2608fd134021bc1dbc18d8c8eb/package.json) |

<a id="ch-primer-css"></a>

### Primer CSS

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/primer/css |
| License | MIT |
| Phiên bản đã đọc | `d0cdad70d6c936501e9f8520212e00d0c4589f69` (commit 2026-11-10) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE, package.json, .github/workflows/ci.yml; chưa chạy upstream |
| Bảo trì | KTLO theo README; vẫn có commit (HEAD 10/11/2026) |
| Nhận định | Triển khai CSS của Primer (GitHub), chỉ giữ vận hành (KTLO). Dự án mới nên dùng Primer React hoặc @primer/primitives; dùng tiện ích CSS có sẵn khi cần. |
| Nguồn | [README.md](https://github.com/primer/css/blob/d0cdad70d6c936501e9f8520212e00d0c4589f69/README.md) · [LICENSE](https://github.com/primer/css/blob/d0cdad70d6c936501e9f8520212e00d0c4589f69/LICENSE) · [package.json](https://github.com/primer/css/blob/d0cdad70d6c936501e9f8520212e00d0c4589f69/package.json) · [.github/workflows/ci.yml](https://github.com/primer/css/blob/d0cdad70d6c936501e9f8520212e00d0c4589f69/.github/workflows/ci.yml) |

<a id="ch-primer-react"></a>

### Primer React

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/primer/react |
| License | MIT |
| Phiên bản đã đọc | `2128032dca65a1bd565fe382c2e91c638c6473a4` (commit 2026-11-19) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE, package.json, .github/workflows/ci.yml; chưa chạy upstream |
| Bảo trì | Hoạt động (HEAD 19/11/2026) |
| Nhận định | Bản React của Primer design system, CI dày (VRT, a11y, CodeQL). Có gói MCP trong monorepo; khả năng cụ thể của MCP **(chưa xác minh)** ở lượt này. |
| Nguồn | [README.md](https://github.com/primer/react/blob/2128032dca65a1bd565fe382c2e91c638c6473a4/README.md) · [LICENSE](https://github.com/primer/react/blob/2128032dca65a1bd565fe382c2e91c638c6473a4/LICENSE) · [package.json](https://github.com/primer/react/blob/2128032dca65a1bd565fe382c2e91c638c6473a4/package.json) · [.github/workflows/ci.yml](https://github.com/primer/react/blob/2128032dca65a1bd565fe382c2e91c638c6473a4/.github/workflows/ci.yml) |

<a id="ch-primereact"></a>

### PrimeReact

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/primefaces/primereact |
| License | MIT |
| Phiên bản đã đọc | `5cd9b145ce7d8b498e745002624ba958f307897e` (commit 2026-09-24) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE.md, package.json; chưa chạy upstream |
| Bảo trì | README: không còn phát triển tích cực, chỉ vá bảo mật; chuyển sang PrimeUI |
| Nhận định | Thư viện component React lớn nay chỉ nhận bản vá bảo mật cho các bản MIT; phát triển mới nằm ở PrimeUI với điều khoản license chưa đọc. Tránh cho dự án mới. |
| Nguồn | [README.md](https://github.com/primefaces/primereact/blob/5cd9b145ce7d8b498e745002624ba958f307897e/README.md) · [LICENSE.md](https://github.com/primefaces/primereact/blob/5cd9b145ce7d8b498e745002624ba958f307897e/LICENSE.md) · [package.json](https://github.com/primefaces/primereact/blob/5cd9b145ce7d8b498e745002624ba958f307897e/package.json) |

<a id="ch-radix-colors"></a>

### Radix Colors

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/radix-ui/colors |
| License | MIT |
| Phiên bản đã đọc | `dbdb85470547c7d34b9001f48fddb08ded335979` (commit 2025-12-17) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE, package.json; chưa chạy upstream |
| Bảo trì | Đứng yên: HEAD 17/12/2025 |
| Nhận định | Hệ màu 12 bước có vai trò định sẵn, có sáng/tối và alpha; ổn định nhưng không còn cập nhật gần đây. Hợp làm nền token màu; tính "accessible" là tuyên bố của tác giả **(chưa xác minh)**. |
| Nguồn | [README.md](https://github.com/radix-ui/colors/blob/dbdb85470547c7d34b9001f48fddb08ded335979/README.md) · [LICENSE](https://github.com/radix-ui/colors/blob/dbdb85470547c7d34b9001f48fddb08ded335979/LICENSE) · [package.json](https://github.com/radix-ui/colors/blob/dbdb85470547c7d34b9001f48fddb08ded335979/package.json) |

<a id="ch-radix-ui"></a>

### Radix UI

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/radix-ui/primitives |
| License | MIT |
| Phiên bản đã đọc | `eb3a2b7091293e27df8f9ba906632d8daa3d81a3` (commit 2026-10-14) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE, package.json, .github/workflows/build.yml; chưa chạy upstream |
| Bảo trì | Hoạt động (HEAD 14/10/2026) |
| Nhận định | Thư viện primitive headless cho React, nền của nhiều design system (shadcn/ui cũ). Mức a11y là tuyên bố của tác giả **(chưa xác minh)**; nhịp commit chậm hơn các đối thủ. |
| Nguồn | [README.md](https://github.com/radix-ui/primitives/blob/eb3a2b7091293e27df8f9ba906632d8daa3d81a3/README.md) · [LICENSE](https://github.com/radix-ui/primitives/blob/eb3a2b7091293e27df8f9ba906632d8daa3d81a3/LICENSE) · [package.json](https://github.com/radix-ui/primitives/blob/eb3a2b7091293e27df8f9ba906632d8daa3d81a3/package.json) · [.github/workflows/build.yml](https://github.com/radix-ui/primitives/blob/eb3a2b7091293e27df8f9ba906632d8daa3d81a3/.github/workflows/build.yml) |

<a id="ch-react-bootstrap"></a>

### React Bootstrap

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/react-bootstrap/react-bootstrap |
| License | MIT |
| Phiên bản đã đọc | `d5ebc9cf46b55f9383368c494d7902e707026e20` (commit 2026-11-19) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE, package.json, .github/workflows/ci.yml; chưa chạy upstream |
| Bảo trì | Hoạt động (HEAD 19/11/2026) |
| Nhận định | Component Bootstrap 5 cho React. Bản ổn định là 2.x, v3 vẫn beta trên master; README chưa nói lộ trình v3. Việc một người bảo trì **(chưa xác minh)** ở lượt này. |
| Nguồn | [README.md](https://github.com/react-bootstrap/react-bootstrap/blob/d5ebc9cf46b55f9383368c494d7902e707026e20/README.md) · [LICENSE](https://github.com/react-bootstrap/react-bootstrap/blob/d5ebc9cf46b55f9383368c494d7902e707026e20/LICENSE) · [package.json](https://github.com/react-bootstrap/react-bootstrap/blob/d5ebc9cf46b55f9383368c494d7902e707026e20/package.json) · [.github/workflows/ci.yml](https://github.com/react-bootstrap/react-bootstrap/blob/d5ebc9cf46b55f9383368c494d7902e707026e20/.github/workflows/ci.yml) |

<a id="ch-react-hook-form"></a>

### React Hook Form

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/react-hook-form/react-hook-form |
| License | MIT |
| Phiên bản đã đọc | `074d174816ae4b4e61856925d296f6afb686387d` (commit 2026-11-23) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE, package.json, .github/workflows/build-test.yml; chưa chạy upstream |
| Bảo trì | Hoạt động (HEAD 23/11/2026) |
| Nhận định | Thư viện form React dựa trên input không kiểm soát, hỗ trợ nhiều schema validator. Kích thước nhỏ và không phụ thuộc runtime theo README **(chưa xác minh)**. |
| Nguồn | [README.md](https://github.com/react-hook-form/react-hook-form/blob/074d174816ae4b4e61856925d296f6afb686387d/README.md) · [LICENSE](https://github.com/react-hook-form/react-hook-form/blob/074d174816ae4b4e61856925d296f6afb686387d/LICENSE) · [package.json](https://github.com/react-hook-form/react-hook-form/blob/074d174816ae4b4e61856925d296f6afb686387d/package.json) · [.github/workflows/build-test.yml](https://github.com/react-hook-form/react-hook-form/blob/074d174816ae4b4e61856925d296f6afb686387d/.github/workflows/build-test.yml) |

<a id="ch-react-native-calendars"></a>

### react-native-calendars

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/wix/react-native-calendars |
| License | MIT |
| Phiên bản đã đọc | `808c6e100511f9adf65b1adec5e5830210f27ef4` (commit 2026-01-29) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE, package.json; chưa chạy upstream |
| Bảo trì | Gần như đứng: HEAD 29/1/2026; không có .github/workflows |
| Nhận định | Component lịch thuần JS cho React Native (đánh dấu ngày, kỳ, vuốt). Ít bảo trì; cần tự thử trên New Architecture trước khi dùng. |
| Nguồn | [README.md](https://github.com/wix/react-native-calendars/blob/808c6e100511f9adf65b1adec5e5830210f27ef4/README.md) · [LICENSE](https://github.com/wix/react-native-calendars/blob/808c6e100511f9adf65b1adec5e5830210f27ef4/LICENSE) · [package.json](https://github.com/wix/react-native-calendars/blob/808c6e100511f9adf65b1adec5e5830210f27ef4/package.json) |

<a id="ch-react-native-reusables"></a>

### React Native Reusables

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/founded-labs/react-native-reusables |
| License | MIT |
| Phiên bản đã đọc | `7df9e76c65c6f866a0865aa2697635c162d3484f` (commit 2026-11-17) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE, package.json; chưa chạy upstream |
| Bảo trì | Hoạt động (HEAD 17/11/2026) |
| Nhận định | Bộ component kiểu shadcn cho React Native (copy-code). Số component/block cụ thể theo catalog cũ **(chưa xác minh)** ở lượt này; không có CI workflow trong repo. |
| Nguồn | [README.md](https://github.com/founded-labs/react-native-reusables/blob/7df9e76c65c6f866a0865aa2697635c162d3484f/README.md) · [LICENSE](https://github.com/founded-labs/react-native-reusables/blob/7df9e76c65c6f866a0865aa2697635c162d3484f/LICENSE) · [package.json](https://github.com/founded-labs/react-native-reusables/blob/7df9e76c65c6f866a0865aa2697635c162d3484f/package.json) |

<a id="ch-react-native-web"></a>

### react-native-web

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/necolas/react-native-web |
| License | MIT |
| Phiên bản đã đọc | `2ba89609cc24edc1cd4d63db651dfd4e56393081` (commit 2026-11-23) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE, package.json, .github/workflows/tests.yml; chưa chạy upstream |
| Bảo trì | Hoạt động (HEAD 23/11/2026) |
| Nhận định | Lớp chạy component React Native trên web (monorepo). Nên ghim phiên bản vì nhánh 0.22 có thay đổi phá vỡ theo catalog cũ **(chưa xác minh)** ở lượt này. |
| Nguồn | [README.md](https://github.com/necolas/react-native-web/blob/2ba89609cc24edc1cd4d63db651dfd4e56393081/README.md) · [LICENSE](https://github.com/necolas/react-native-web/blob/2ba89609cc24edc1cd4d63db651dfd4e56393081/LICENSE) · [package.json](https://github.com/necolas/react-native-web/blob/2ba89609cc24edc1cd4d63db651dfd4e56393081/package.json) · [.github/workflows/tests.yml](https://github.com/necolas/react-native-web/blob/2ba89609cc24edc1cd4d63db651dfd4e56393081/.github/workflows/tests.yml) |

<a id="ch-react-spectrum-react-aria"></a>

### React Spectrum / React Aria

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/adobe/react-spectrum |
| License | Apache-2.0 |
| Phiên bản đã đọc | `6be3466d87cc628ee69461230c1b5f4e3b64c6e3` (commit 2026-11-21) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE, package.json, .github/workflows/nightly.yaml; chưa chạy upstream |
| Bảo trì | Hoạt động (HEAD 21/11/2026); nightly.yaml chỉ là deploy thủ công, kiểm thử không thấy trong GitHub Actions |
| Nhận định | Bộ thư viện của Adobe: React Aria (hook/component không style) mạnh về a11y và i18n, cộng React Spectrum có style. Các tuyên bố a11y/hơn 30 ngôn ngữ **(chưa xác minh)**. |
| Nguồn | [README.md](https://github.com/adobe/react-spectrum/blob/6be3466d87cc628ee69461230c1b5f4e3b64c6e3/README.md) · [LICENSE](https://github.com/adobe/react-spectrum/blob/6be3466d87cc628ee69461230c1b5f4e3b64c6e3/LICENSE) · [package.json](https://github.com/adobe/react-spectrum/blob/6be3466d87cc628ee69461230c1b5f4e3b64c6e3/package.json) · [.github/workflows/nightly.yaml](https://github.com/adobe/react-spectrum/blob/6be3466d87cc628ee69461230c1b5f4e3b64c6e3/.github/workflows/nightly.yaml) |

<a id="ch-react-suite-rsuite"></a>

### React Suite (rsuite)

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/rsuite/rsuite |
| License | MIT |
| Phiên bản đã đọc | `71175b9adbb9c840b6c4a4fe0a62cb607ebf2fac` (commit 2026-10-25) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE, package.json, .github/workflows/nodejs-ci.yml; chưa chạy upstream |
| Bảo trì | Hoạt động (HEAD 25/10/2026) |
| Nhận định | Bộ component React cho ứng dụng nhiều dữ liệu, có SSR. CI đa trình duyệt; MCP/skill theo catalog cũ **(chưa xác minh)** ở lượt này. |
| Nguồn | [README.md](https://github.com/rsuite/rsuite/blob/71175b9adbb9c840b6c4a4fe0a62cb607ebf2fac/README.md) · [LICENSE](https://github.com/rsuite/rsuite/blob/71175b9adbb9c840b6c4a4fe0a62cb607ebf2fac/LICENSE) · [package.json](https://github.com/rsuite/rsuite/blob/71175b9adbb9c840b6c4a4fe0a62cb607ebf2fac/package.json) · [.github/workflows/nodejs-ci.yml](https://github.com/rsuite/rsuite/blob/71175b9adbb9c840b6c4a4fe0a62cb607ebf2fac/.github/workflows/nodejs-ci.yml) |

<a id="ch-react-virtualized"></a>

### react-virtualized

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/bvaughn/react-virtualized |
| License | MIT |
| Phiên bản đã đọc | `3f50a3f9c127051c99e11974710ee6cdd7272cd2` (commit 2026-11-14) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE, package.json, .github/workflows/vitest.yml; chưa chạy upstream |
| Bảo trì | Hoạt động (HEAD 14/11/2026) |
| Nhận định | Component render danh sách/bảng lớn bằng windowing, v10 viết lại TypeScript. README gợi ý cân nhắc react-window cho dự án mới. |
| Nguồn | [README.md](https://github.com/bvaughn/react-virtualized/blob/3f50a3f9c127051c99e11974710ee6cdd7272cd2/README.md) · [LICENSE](https://github.com/bvaughn/react-virtualized/blob/3f50a3f9c127051c99e11974710ee6cdd7272cd2/LICENSE) · [package.json](https://github.com/bvaughn/react-virtualized/blob/3f50a3f9c127051c99e11974710ee6cdd7272cd2/package.json) · [.github/workflows/vitest.yml](https://github.com/bvaughn/react-virtualized/blob/3f50a3f9c127051c99e11974710ee6cdd7272cd2/.github/workflows/vitest.yml) |

<a id="ch-refactoring-ui-skill"></a>

### Refactoring UI Skill

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/s0xDk/refactoring-ui-skill |
| License | MIT (kèm điều khoản: không bao gồm sách Refactoring UI) |
| Phiên bản đã đọc | `48872143abb0a8feb6d9bf58e222afbd800210b0` (commit 2026-08-27) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE; chưa chạy upstream |
| Bảo trì | Đứng: chỉ có commit 27/8/2026 |
| Nhận định | Skill Claude Code đưa quy tắc sách Refactoring UI (thang spacing/type/màu/bóng, bảng chẩn đoán) kèm tokens.css. Việc "đối chiếu từng trang với sách" là tuyên bố tác giả **(chưa xác minh)**. |
| Nguồn | [README.md](https://github.com/s0xDk/refactoring-ui-skill/blob/48872143abb0a8feb6d9bf58e222afbd800210b0/README.md) · [LICENSE](https://github.com/s0xDk/refactoring-ui-skill/blob/48872143abb0a8feb6d9bf58e222afbd800210b0/LICENSE) |

<a id="ch-refine"></a>

### Refine

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/refinedev/refine |
| License | MIT |
| Phiên bản đã đọc | `2352eb5b6539e2f39ad9aef652279ad1dcf2c467` (commit 2026-09-10) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE, package.json, .github/workflows/pull-request.yml; chưa chạy upstream |
| Bảo trì | HEAD nhánh mặc định 10/9/2026; chưa đủ dữ liệu kết luận nhịp bảo trì |
| Nhận định | Framework headless cho admin/dashboard/CRUD, tích hợp nhiều UI kit. Hơn 2 tháng không commit trên main tại thời điểm kiểm; nên xem lại nhịp phát hành trước khi chọn. |
| Nguồn | [README.md](https://github.com/refinedev/refine/blob/2352eb5b6539e2f39ad9aef652279ad1dcf2c467/README.md) · [LICENSE](https://github.com/refinedev/refine/blob/2352eb5b6539e2f39ad9aef652279ad1dcf2c467/LICENSE) · [package.json](https://github.com/refinedev/refine/blob/2352eb5b6539e2f39ad9aef652279ad1dcf2c467/package.json) · [.github/workflows/pull-request.yml](https://github.com/refinedev/refine/blob/2352eb5b6539e2f39ad9aef652279ad1dcf2c467/.github/workflows/pull-request.yml) |

<a id="ch-reka-ui"></a>

### Reka UI

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/unovue/reka-ui |
| License | MIT |
| Phiên bản đã đọc | `e4687cd0f745ca18f28235b69cfa35a7415553f8` (commit 2026-11-23) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE, package.json, .github/workflows/build.yaml; chưa chạy upstream |
| Bảo trì | Hoạt động (nhánh mặc định v2, HEAD 23/11/2026) |
| Nhận định | Thư viện primitive headless cho Vue (trước là Radix Vue), nền của shadcn-vue và Nuxt UI. Tài liệu cho agent có sẵn; chất lượng a11y **(chưa xác minh)**. |
| Nguồn | [README.md](https://github.com/unovue/reka-ui/blob/e4687cd0f745ca18f28235b69cfa35a7415553f8/README.md) · [LICENSE](https://github.com/unovue/reka-ui/blob/e4687cd0f745ca18f28235b69cfa35a7415553f8/LICENSE) · [package.json](https://github.com/unovue/reka-ui/blob/e4687cd0f745ca18f28235b69cfa35a7415553f8/package.json) · [.github/workflows/build.yaml](https://github.com/unovue/reka-ui/blob/e4687cd0f745ca18f28235b69cfa35a7415553f8/.github/workflows/build.yaml) |

<a id="ch-semi-design"></a>

### Semi Design

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/DouyinFE/semi-design |
| License | MIT (LICENSE kèm notice license bên thứ ba) |
| Phiên bản đã đọc | `57dd0c16c10a43d72171c0982c6af04ffb350836` (commit 2026-11-23) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE, package.json, .github/workflows/test.yml; chưa chạy upstream |
| Bảo trì | Hoạt động (HEAD 23/11/2026) |
| Nhận định | Design system React của ByteDance với nhiều component và D2C từ Figma. Có gói MCP trong repo; hành vi tải docs lúc chạy theo catalog cũ **(chưa xác minh)** ở lượt này. |
| Nguồn | [README.md](https://github.com/DouyinFE/semi-design/blob/57dd0c16c10a43d72171c0982c6af04ffb350836/README.md) · [LICENSE](https://github.com/DouyinFE/semi-design/blob/57dd0c16c10a43d72171c0982c6af04ffb350836/LICENSE) · [package.json](https://github.com/DouyinFE/semi-design/blob/57dd0c16c10a43d72171c0982c6af04ffb350836/package.json) · [.github/workflows/test.yml](https://github.com/DouyinFE/semi-design/blob/57dd0c16c10a43d72171c0982c6af04ffb350836/.github/workflows/test.yml) |

<a id="ch-shadcn-admin"></a>

### shadcn-admin

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/satnaing/shadcn-admin |
| License | MIT |
| Phiên bản đã đọc | `e16c87f213a5ba5e45964e9b67c792105ec74d26` (commit 2026-06-11) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE, package.json, .github/workflows/ci.yml; chưa chạy upstream |
| Bảo trì | Đứng từ HEAD 11/6/2026 |
| Nhận định | Giao diện admin Vite + React dựng trên shadcn, có RTL và một số component đã chỉnh. Tác giả không coi là template; cập nhật component qua CLI cần merge tay với các file đã sửa. |
| Nguồn | [README.md](https://github.com/satnaing/shadcn-admin/blob/e16c87f213a5ba5e45964e9b67c792105ec74d26/README.md) · [LICENSE](https://github.com/satnaing/shadcn-admin/blob/e16c87f213a5ba5e45964e9b67c792105ec74d26/LICENSE) · [package.json](https://github.com/satnaing/shadcn-admin/blob/e16c87f213a5ba5e45964e9b67c792105ec74d26/package.json) · [.github/workflows/ci.yml](https://github.com/satnaing/shadcn-admin/blob/e16c87f213a5ba5e45964e9b67c792105ec74d26/.github/workflows/ci.yml) |

<a id="ch-shadcn-lint"></a>

### @shadcn/lint

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/shadcn-ui/lint |
| License | MIT |
| Phiên bản đã đọc | `529de36e185297a46ed5ef7049eb2965272d102e` (commit 2026-11-02) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE, package.json, .github/workflows/ci.yml; chưa chạy upstream |
| Bảo trì | Hoạt động (HEAD 2/11/2026) |
| Nhận định | Linter viết thông báo lỗi cho agent, kiểm luật design system Tailwind. Kết quả eval không commit nên hiệu quả với agent **(chưa xác minh)**. |
| Nguồn | [README.md](https://github.com/shadcn-ui/lint/blob/529de36e185297a46ed5ef7049eb2965272d102e/README.md) · [LICENSE](https://github.com/shadcn-ui/lint/blob/529de36e185297a46ed5ef7049eb2965272d102e/LICENSE) · [package.json](https://github.com/shadcn-ui/lint/blob/529de36e185297a46ed5ef7049eb2965272d102e/package.json) · [.github/workflows/ci.yml](https://github.com/shadcn-ui/lint/blob/529de36e185297a46ed5ef7049eb2965272d102e/.github/workflows/ci.yml) |

<a id="ch-shadcn-ui"></a>

### shadcn/ui

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/shadcn-ui/ui |
| License | MIT |
| Phiên bản đã đọc | `055aa6b7837b1808456a24beb4c97a677864aa82` (commit 2026-11-23) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE.md, package.json, .github/workflows/test.yml; chưa chạy upstream |
| Bảo trì | Hoạt động (HEAD 23/11/2026) |
| Nhận định | Bộ component copy-code cho React, dùng làm nền tự xây thư viện. Số layout block/chart và mặc định Base UI theo catalog cũ **(chưa xác minh)** ở lượt này. |
| Nguồn | [README.md](https://github.com/shadcn-ui/ui/blob/055aa6b7837b1808456a24beb4c97a677864aa82/README.md) · [LICENSE.md](https://github.com/shadcn-ui/ui/blob/055aa6b7837b1808456a24beb4c97a677864aa82/LICENSE.md) · [package.json](https://github.com/shadcn-ui/ui/blob/055aa6b7837b1808456a24beb4c97a677864aa82/package.json) · [.github/workflows/test.yml](https://github.com/shadcn-ui/ui/blob/055aa6b7837b1808456a24beb4c97a677864aa82/.github/workflows/test.yml) |

<a id="ch-shadcn-vue"></a>

### shadcn-vue

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/unovue/shadcn-vue |
| License | MIT |
| Phiên bản đã đọc | `d1bf1b3a2d1a824b19f32d7253a28a43797b8253` (commit 2026-11-03) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE, package.json, .github/workflows/test.yaml; chưa chạy upstream |
| Bảo trì | Hoạt động (nhánh mặc định dev, HEAD 3/11/2026) |
| Nhận định | Bản Vue của shadcn/ui trên Reka UI. MCP trong CLI và bộ skill theo catalog cũ **(chưa xác minh)** ở lượt này. |
| Nguồn | [README.md](https://github.com/unovue/shadcn-vue/blob/d1bf1b3a2d1a824b19f32d7253a28a43797b8253/README.md) · [LICENSE](https://github.com/unovue/shadcn-vue/blob/d1bf1b3a2d1a824b19f32d7253a28a43797b8253/LICENSE) · [package.json](https://github.com/unovue/shadcn-vue/blob/d1bf1b3a2d1a824b19f32d7253a28a43797b8253/package.json) · [.github/workflows/test.yaml](https://github.com/unovue/shadcn-vue/blob/d1bf1b3a2d1a824b19f32d7253a28a43797b8253/.github/workflows/test.yaml) |

<a id="ch-skeleton"></a>

### Skeleton

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/skeletonlabs/skeleton |
| License | MIT |
| Phiên bản đã đọc | `011910c49939628b883c745994657ede4460143c` (commit 2026-11-23) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE, package.json, .github/workflows/code-quality.yml; chưa chạy upstream |
| Bảo trì | Có commit mới (HEAD 23/11/2026) |
| Nhận định | Design system dựa trên Tailwind với component cho nhiều framework. Trạng thái PR bảo mật Renovate theo catalog cũ **(chưa xác minh)** ở lượt này. |
| Nguồn | [README.md](https://github.com/skeletonlabs/skeleton/blob/011910c49939628b883c745994657ede4460143c/README.md) · [LICENSE](https://github.com/skeletonlabs/skeleton/blob/011910c49939628b883c745994657ede4460143c/LICENSE) · [package.json](https://github.com/skeletonlabs/skeleton/blob/011910c49939628b883c745994657ede4460143c/package.json) · [.github/workflows/code-quality.yml](https://github.com/skeletonlabs/skeleton/blob/011910c49939628b883c745994657ede4460143c/.github/workflows/code-quality.yml) |

<a id="ch-stageshow"></a>

### Stageshow

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/benjitaylor/skills |
| License | MIT (stageshow/LICENSE); app icon trong assets/app-icons.ts và logo trong kit/brands theo license/điều khoản riêng (NOTICE.md) |
| Phiên bản đã đọc | `299140fafd08df55a9c234e610c3f64af3f45531` (commit 2026-11-04) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc stageshow/README.md, stageshow/LICENSE, stageshow/NOTICE.md, stageshow/package.json; chưa chạy upstream |
| Bảo trì | Mới: HEAD 4/11/2026; không có CI workflow |
| Nhận định | Skill + kit React dựng minh họa sản phẩm và chuyển động, kèm script quay phim kiểm khung hình. Asset thương hiệu/icon không thuộc MIT; không có CI. Hiệu quả cổng --gate **(chưa xác minh)**. |
| Nguồn | [stageshow/README.md](https://github.com/benjitaylor/skills/blob/299140fafd08df55a9c234e610c3f64af3f45531/stageshow/README.md) · [stageshow/LICENSE](https://github.com/benjitaylor/skills/blob/299140fafd08df55a9c234e610c3f64af3f45531/stageshow/LICENSE) · [stageshow/NOTICE.md](https://github.com/benjitaylor/skills/blob/299140fafd08df55a9c234e610c3f64af3f45531/stageshow/NOTICE.md) · [stageshow/package.json](https://github.com/benjitaylor/skills/blob/299140fafd08df55a9c234e610c3f64af3f45531/stageshow/package.json) |

<a id="ch-stencil"></a>

### Stencil

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/stenciljs/core |
| License | MIT |
| Phiên bản đã đọc | `42307820e1e5ae4bc03bf881c28a0e6ba95167d7` (commit 2026-11-19) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc readme.md, LICENSE, package.json, .github/workflows/main.yml; chưa chạy upstream |
| Bảo trì | Hoạt động (HEAD 19/11/2026) |
| Nhận định | Trình biên dịch web component (nền Ionic). Telemetry mặc định của CLI v4 theo catalog cũ **(chưa xác minh)** ở lượt này; nên tắt khi dùng trong CI. |
| Nguồn | [readme.md](https://github.com/stenciljs/core/blob/42307820e1e5ae4bc03bf881c28a0e6ba95167d7/readme.md) · [LICENSE](https://github.com/stenciljs/core/blob/42307820e1e5ae4bc03bf881c28a0e6ba95167d7/LICENSE) · [package.json](https://github.com/stenciljs/core/blob/42307820e1e5ae4bc03bf881c28a0e6ba95167d7/package.json) · [.github/workflows/main.yml](https://github.com/stenciljs/core/blob/42307820e1e5ae4bc03bf881c28a0e6ba95167d7/.github/workflows/main.yml) |

<a id="ch-stitch-skills-google-labs"></a>

### stitch-skills (Google Labs)

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/google-labs-code/stitch-skills |
| License | Apache-2.0 |
| Phiên bản đã đọc | `62fdcd679747aca0792e5dd6591b10ddfad56825` (commit 2026-11-20) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE, .github/workflows/validate-skills.yml; chưa chạy upstream |
| Bảo trì | active (đang hoạt động) |
| Nhận định | Bộ 16 skill/3 plugin cho Google Stitch MCP, cài qua marketplace Codex/Claude Code. Cần Stitch API key và gửi dữ liệu thiết kế lên Google; không phải sản phẩm Google hỗ trợ chính thức. Repo hoạt động lại (commit 20/11/2026). |
| Nguồn | [README.md](https://github.com/google-labs-code/stitch-skills/blob/62fdcd679747aca0792e5dd6591b10ddfad56825/README.md) · [LICENSE](https://github.com/google-labs-code/stitch-skills/blob/62fdcd679747aca0792e5dd6591b10ddfad56825/LICENSE) · [validate-skills.yml](https://github.com/google-labs-code/stitch-skills/blob/62fdcd679747aca0792e5dd6591b10ddfad56825/.github/workflows/validate-skills.yml) |

<a id="ch-storybook"></a>

### Storybook

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/storybookjs/storybook |
| License | MIT |
| Phiên bản đã đọc | `d38b4c5c771bc15b8e139d1e352bcc207734d709` (commit 2026-11-23) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE, package.json; chưa chạy upstream |
| Bảo trì | active (đang hoạt động) |
| Nhận định | Workshop dựng và test component UI cô lập, hỗ trợ nhiều framework. README nay thêm mục AI (prompt cho agent, MCP) — mức hữu ích cho agent **(chưa xác minh)**. |
| Nguồn | [README.md](https://github.com/storybookjs/storybook/blob/d38b4c5c771bc15b8e139d1e352bcc207734d709/README.md) · [LICENSE](https://github.com/storybookjs/storybook/blob/d38b4c5c771bc15b8e139d1e352bcc207734d709/LICENSE) · [package.json](https://github.com/storybookjs/storybook/blob/d38b4c5c771bc15b8e139d1e352bcc207734d709/package.json) |

<a id="ch-style-dictionary"></a>

### Style Dictionary

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/style-dictionary/style-dictionary |
| License | Apache-2.0 |
| Phiên bản đã đọc | `795233d9bee6a7b5787d685d75d626df3399d24d` (commit 2026-11-03) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE, package.json, CHANGELOG.md; chưa chạy upstream |
| Bảo trì | active (đang hoạt động) |
| Nhận định | Build design token sang CSS/iOS/Android/JS từ một nguồn; hỗ trợ cú pháp DTCG 2025.10. Bản 5.8.0 có thay đổi breaking nhỏ về tên format `sketch/palette` — ghim phiên bản khi nâng cấp. |
| Nguồn | [README.md](https://github.com/style-dictionary/style-dictionary/blob/795233d9bee6a7b5787d685d75d626df3399d24d/README.md) · [LICENSE](https://github.com/style-dictionary/style-dictionary/blob/795233d9bee6a7b5787d685d75d626df3399d24d/LICENSE) · [package.json](https://github.com/style-dictionary/style-dictionary/blob/795233d9bee6a7b5787d685d75d626df3399d24d/package.json) · [CHANGELOG.md](https://github.com/style-dictionary/style-dictionary/blob/795233d9bee6a7b5787d685d75d626df3399d24d/CHANGELOG.md) |

<a id="ch-stylelint"></a>

### Stylelint

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/stylelint/stylelint |
| License | MIT |
| Phiên bản đã đọc | `39f029d687cf2e667a43bc7005c1a16e8c36930d` (commit 2026-11-20) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE, package.json, CHANGELOG.md; chưa chạy upstream |
| Bảo trì | active (đang hoạt động) |
| Nhận định | Linter CSS với ~150 luật dựng sẵn (vd. color-no-hex, declaration-property-value-allowed-list) để cấm giá trị ngoài token. Bản 18.x yêu cầu Node 22.22+; 18.1.0 sửa autofix nhiều lượt. |
| Nguồn | [README.md](https://github.com/stylelint/stylelint/blob/39f029d687cf2e667a43bc7005c1a16e8c36930d/README.md) · [LICENSE](https://github.com/stylelint/stylelint/blob/39f029d687cf2e667a43bc7005c1a16e8c36930d/LICENSE) · [package.json](https://github.com/stylelint/stylelint/blob/39f029d687cf2e667a43bc7005c1a16e8c36930d/package.json) · [CHANGELOG.md](https://github.com/stylelint/stylelint/blob/39f029d687cf2e667a43bc7005c1a16e8c36930d/CHANGELOG.md) |

<a id="ch-swiftui-agent-skill"></a>

### SwiftUI Agent Skill

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/twostraws/SwiftUI-Agent-Skill |
| License | MIT |
| Phiên bản đã đọc | `f2920b63995263f57b3e198674e89a602efba6d2` (commit 2026-10-26) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE, swiftui-pro/SKILL.md; chưa chạy upstream |
| Bảo trì | active (đang hoạt động) |
| Nhận định | Skill SwiftUI Pro của Paul Hudson: SKILL.md ngắn nạp 12 file tham chiếu theo chủ đề (API, a11y, hiệu năng…). Chứa các sự thật nền tảng ghi cứng (iOS 27) nên cần cập nhật theo năm; không có CI. |
| Nguồn | [README.md](https://github.com/twostraws/SwiftUI-Agent-Skill/blob/f2920b63995263f57b3e198674e89a602efba6d2/README.md) · [LICENSE](https://github.com/twostraws/SwiftUI-Agent-Skill/blob/f2920b63995263f57b3e198674e89a602efba6d2/LICENSE) · [SKILL.md](https://github.com/twostraws/SwiftUI-Agent-Skill/blob/f2920b63995263f57b3e198674e89a602efba6d2/swiftui-pro/SKILL.md) |

<a id="ch-tailadmin-react-free"></a>

### TailAdmin React (free)

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/TailAdmin/free-react-tailwind-admin-dashboard |
| License | MIT |
| Phiên bản đã đọc | `486ed748b21e032a4432effeca4ef3684fa223d3` (commit 2026-11-17) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE.md, package.json; chưa chạy upstream |
| Bảo trì | active (đang hoạt động) |
| Nhận định | Mẫu admin React 19 + Tailwind v4 miễn phí, một dashboard ecommerce; README đẩy sang bản Pro trả phí. Không có CI/test. |
| Nguồn | [README.md](https://github.com/TailAdmin/free-react-tailwind-admin-dashboard/blob/486ed748b21e032a4432effeca4ef3684fa223d3/README.md) · [LICENSE.md](https://github.com/TailAdmin/free-react-tailwind-admin-dashboard/blob/486ed748b21e032a4432effeca4ef3684fa223d3/LICENSE.md) · [package.json](https://github.com/TailAdmin/free-react-tailwind-admin-dashboard/blob/486ed748b21e032a4432effeca4ef3684fa223d3/package.json) |

<a id="ch-tailwind-plus"></a>

### Tailwind Plus

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://tailwindcss.com/plus |
| License | proprietary |
| Phiên bản đã đọc | trang web đọc ngày 2026-11-23 (không có SHA) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc https://tailwindcss.com/blog/tailwind-is-joining-shopify, https://tailwindcss.com/plus; chưa chạy upstream |
| Bảo trì | unknown (chưa rõ) |
| Nhận định | Bộ UI block/template trả phí của Tailwind Labs (trước là Tailwind UI). Đã đóng bán cho khách mới từ 9/2026; chỉ còn ý nghĩa tham khảo với người đã mua. |
| Nguồn | [tailwindcss.com/blog/tailwind-is-joining-shopify](https://tailwindcss.com/blog/tailwind-is-joining-shopify) · [tailwindcss.com/plus](https://tailwindcss.com/plus) |

<a id="ch-tamagui-bento"></a>

### Tamagui (Bento)

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/tamagui/tamagui |
| License | MIT |
| Phiên bản đã đọc | `1d5e750ec5a17c97843613d86c916bad44ec900e` (commit 2026-11-15) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE, package.json, code/bento/package.json; chưa chạy upstream |
| Bảo trì | active (đang hoạt động) |
| Nhận định | Thư viện style + UI kit dùng chung React/React Native với compiler tối ưu. Bento (component/màn hình copy-paste) nay có nguồn MIT trong repo; monorepo lớn, build bằng bun/turbo. |
| Nguồn | [README.md](https://github.com/tamagui/tamagui/blob/1d5e750ec5a17c97843613d86c916bad44ec900e/README.md) · [LICENSE](https://github.com/tamagui/tamagui/blob/1d5e750ec5a17c97843613d86c916bad44ec900e/LICENSE) · [package.json](https://github.com/tamagui/tamagui/blob/1d5e750ec5a17c97843613d86c916bad44ec900e/package.json) · [package.json](https://github.com/tamagui/tamagui/blob/1d5e750ec5a17c97843613d86c916bad44ec900e/code/bento/package.json) |

<a id="ch-tambo"></a>

### Tambo

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/tambo-ai/tambo |
| License | MIT + Apache-2.0 (apps/api, apps/web, packages/backend) |
| Phiên bản đã đọc | `6e2c1bff3b68a00c094b6d876788cc8f33f7bb02` (commit 2026-10-09) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE, apps/api/LICENSE, packages/backend/LICENSE, apps/web/LICENSE; chưa chạy upstream |
| Bảo trì | low-activity (ít hoạt động) |
| Nhận định | SDK React biến component + schema Zod thành tool cho agent, có backend tự host bằng Docker. Cloud đã đóng nên phải tự host; nhóm đã chuyển sang sản phẩm khác, rủi ro ngừng phát triển. |
| Nguồn | [README.md](https://github.com/tambo-ai/tambo/blob/6e2c1bff3b68a00c094b6d876788cc8f33f7bb02/README.md) · [LICENSE](https://github.com/tambo-ai/tambo/blob/6e2c1bff3b68a00c094b6d876788cc8f33f7bb02/LICENSE) · [LICENSE](https://github.com/tambo-ai/tambo/blob/6e2c1bff3b68a00c094b6d876788cc8f33f7bb02/apps/api/LICENSE) · [LICENSE](https://github.com/tambo-ai/tambo/blob/6e2c1bff3b68a00c094b6d876788cc8f33f7bb02/packages/backend/LICENSE) · [LICENSE](https://github.com/tambo-ai/tambo/blob/6e2c1bff3b68a00c094b6d876788cc8f33f7bb02/apps/web/LICENSE) |

<a id="ch-taro-ui"></a>

### Taro UI

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/jd-opensource/taro-ui |
| License | MIT |
| Phiên bản đã đọc | `d0653307e44015ebf6de382f0a31dab4c9756e15` (commit 2026-09-25) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE, package.json, docs/MAINTENANCE.md, packages/taro-ui/package.json; chưa chạy upstream |
| Bảo trì | active (đang hoạt động) |
| Nhận định | Bộ UI đa nền (mini-program, H5, RN) cho Taro 3; có ví dụ chạy Taro 4 nhưng gói chính vẫn khai Taro 3.x. Tài liệu chủ yếu tiếng Trung. |
| Nguồn | [README.md](https://github.com/jd-opensource/taro-ui/blob/d0653307e44015ebf6de382f0a31dab4c9756e15/README.md) · [LICENSE](https://github.com/jd-opensource/taro-ui/blob/d0653307e44015ebf6de382f0a31dab4c9756e15/LICENSE) · [package.json](https://github.com/jd-opensource/taro-ui/blob/d0653307e44015ebf6de382f0a31dab4c9756e15/package.json) · [MAINTENANCE.md](https://github.com/jd-opensource/taro-ui/blob/d0653307e44015ebf6de382f0a31dab4c9756e15/docs/MAINTENANCE.md) · [package.json](https://github.com/jd-opensource/taro-ui/blob/d0653307e44015ebf6de382f0a31dab4c9756e15/packages/taro-ui/package.json) |

<a id="ch-taste-skill"></a>

### Taste Skill

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/Leonxlnx/taste-skill |
| License | MIT |
| Phiên bản đã đọc | `6c0b5c78f5d31776e2210305abaa210cdc0030bf` (commit 2026-11-22) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE, .github/workflows/check-skills.yml; chưa chạy upstream |
| Bảo trì | active (đang hoạt động) |
| Nhận định | Skill chống giao diện "AI slop" cho trang web công ty: chia palette/font/layout, cổng kết thúc (Stop hook) và trình kiểm render ở 5 độ rộng màn hình. Repo đã tách còn 1 skill; các con số cũ về 13 skill không còn đúng. |
| Nguồn | [README.md](https://github.com/Leonxlnx/taste-skill/blob/6c0b5c78f5d31776e2210305abaa210cdc0030bf/README.md) · [LICENSE](https://github.com/Leonxlnx/taste-skill/blob/6c0b5c78f5d31776e2210305abaa210cdc0030bf/LICENSE) · [check-skills.yml](https://github.com/Leonxlnx/taste-skill/blob/6c0b5c78f5d31776e2210305abaa210cdc0030bf/.github/workflows/check-skills.yml) |

<a id="ch-threeui-community"></a>

### ThreeUI Community

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/MengTo/threeui |
| License | MIT (tài sản/font có file license riêng) |
| Phiên bản đã đọc | `68802d5428071ada5c20db8094b1649e6bb770ed` (commit 2026-09-01) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE, ASSET-LICENSES.md, package.json; chưa chạy upstream |
| Bảo trì | low-activity (ít hoạt động) |
| Nhận định | Catalog shader/Three.js bản cộng đồng (bỏ Pro/Beta) dạng open-core. Tài sản và font có license riêng, cần đọc trước khi dùng; Pro tải qua CLI có xác thực. |
| Nguồn | [README.md](https://github.com/MengTo/threeui/blob/68802d5428071ada5c20db8094b1649e6bb770ed/README.md) · [LICENSE](https://github.com/MengTo/threeui/blob/68802d5428071ada5c20db8094b1649e6bb770ed/LICENSE) · [ASSET-LICENSES.md](https://github.com/MengTo/threeui/blob/68802d5428071ada5c20db8094b1649e6bb770ed/ASSET-LICENSES.md) · [package.json](https://github.com/MengTo/threeui/blob/68802d5428071ada5c20db8094b1649e6bb770ed/package.json) |

<a id="ch-tkinter-designer"></a>

### Tkinter-Designer

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/ParthJadhav/Tkinter-Designer |
| License | BSD-3-Clause |
| Phiên bản đã đọc | `61ce0665ce68e255fd8bead3c14aac6c877bfa05` (commit 2026-10-16) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE, pyproject.toml, .github/workflows/build.yml; chưa chạy upstream |
| Bảo trì | low-activity (ít hoạt động) |
| Nhận định | Sinh mã GUI Tkinter từ file Figma qua REST API. Phát triển gần như dừng, CI lỗi thời; chỉ đáng tham khảo ý tưởng design-to-code. |
| Nguồn | [README.md](https://github.com/ParthJadhav/Tkinter-Designer/blob/61ce0665ce68e255fd8bead3c14aac6c877bfa05/README.md) · [LICENSE](https://github.com/ParthJadhav/Tkinter-Designer/blob/61ce0665ce68e255fd8bead3c14aac6c877bfa05/LICENSE) · [pyproject.toml](https://github.com/ParthJadhav/Tkinter-Designer/blob/61ce0665ce68e255fd8bead3c14aac6c877bfa05/pyproject.toml) · [build.yml](https://github.com/ParthJadhav/Tkinter-Designer/blob/61ce0665ce68e255fd8bead3c14aac6c877bfa05/.github/workflows/build.yml) |

<a id="ch-tldraw"></a>

### tldraw

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/tldraw/tldraw |
| License | tldraw license |
| Phiên bản đã đọc | `4aaf272ac8a245e4c875feb668cd9884c475a299` (commit 2026-11-23) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE.md, package.json; chưa chạy upstream |
| Bảo trì | active (đang hoạt động) |
| Nhận định | SDK canvas vô hạn cho React (shape/tool tùy biến, sync multiplayer, primitive cho LLM). Không phải OSS tự do: dùng production cần license key trả phí. |
| Nguồn | [README.md](https://github.com/tldraw/tldraw/blob/4aaf272ac8a245e4c875feb668cd9884c475a299/README.md) · [LICENSE.md](https://github.com/tldraw/tldraw/blob/4aaf272ac8a245e4c875feb668cd9884c475a299/LICENSE.md) · [package.json](https://github.com/tldraw/tldraw/blob/4aaf272ac8a245e4c875feb668cd9884c475a299/package.json) |

<a id="ch-transitions-dev"></a>

### transitions.dev

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/Jakubantalik/transitions.dev |
| License | License riêng (cấm phân phối lại thư viện; tooling MIT) |
| Phiên bản đã đọc | `add5b467b13be16664d10fd888330ce2f3288b07` (commit 2026-11-19) |
| Kiểm chứng | 2026-11-23; code-read; đã đọc README.md, LICENSE, package.json, refine/bin/cli.mjs; chưa chạy upstream |
| Bảo trì | active (đang hoạt động) |
| Nhận định | Bộ transition CSS copy-paste kèm skill agent và luật tĩnh (agent/lib/rules.mjs). Rủi ro: `refine` tải và chạy script cài Cursor từ mạng; license cấm phân phối lại; mô hình trả phí Pro. |
| Nguồn | [README.md](https://github.com/Jakubantalik/transitions.dev/blob/add5b467b13be16664d10fd888330ce2f3288b07/README.md) · [LICENSE](https://github.com/Jakubantalik/transitions.dev/blob/add5b467b13be16664d10fd888330ce2f3288b07/LICENSE) · [package.json](https://github.com/Jakubantalik/transitions.dev/blob/add5b467b13be16664d10fd888330ce2f3288b07/package.json) · [cli.mjs](https://github.com/Jakubantalik/transitions.dev/blob/add5b467b13be16664d10fd888330ce2f3288b07/refine/bin/cli.mjs) |

<a id="ch-tremor"></a>

### Tremor

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/tremorlabs/tremor |
| License | Apache-2.0 |
| Phiên bản đã đọc | `ca4d588f47820ff3d514d37fa4ee08a4222dec11` (commit 2025-10-10) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE, package.json; chưa chạy upstream |
| Bảo trì | low-activity (ít hoạt động) |
| Nhận định | Component chart/dashboard copy-paste trên Tailwind + Radix. Đứng từ 10/2025, còn React 18/Recharts 2; nên ưu tiên shadcn charts. |
| Nguồn | [README.md](https://github.com/tremorlabs/tremor/blob/ca4d588f47820ff3d514d37fa4ee08a4222dec11/README.md) · [LICENSE](https://github.com/tremorlabs/tremor/blob/ca4d588f47820ff3d514d37fa4ee08a4222dec11/LICENSE) · [package.json](https://github.com/tremorlabs/tremor/blob/ca4d588f47820ff3d514d37fa4ee08a4222dec11/package.json) |

<a id="ch-tremor-blocks"></a>

### Tremor Blocks

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/tremorlabs/tremor-blocks |
| License | MIT |
| Phiên bản đã đọc | `b319e8d3d3678a4f60f4802f7e85bc1abc52d598` (commit 2025-01-22) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE.md, package.json; chưa chạy upstream |
| Bảo trì | low-activity (ít hoạt động) |
| Nhận định | Kho 323 block dashboard (KPI, bảng, billing, login…) trên Next.js + Tailwind. Ngừng cập nhật từ 1/2025; README không có tài liệu thực. |
| Nguồn | [README.md](https://github.com/tremorlabs/tremor-blocks/blob/b319e8d3d3678a4f60f4802f7e85bc1abc52d598/README.md) · [LICENSE.md](https://github.com/tremorlabs/tremor-blocks/blob/b319e8d3d3678a4f60f4802f7e85bc1abc52d598/LICENSE.md) · [package.json](https://github.com/tremorlabs/tremor-blocks/blob/b319e8d3d3678a4f60f4802f7e85bc1abc52d598/package.json) |

<a id="ch-tweakcn"></a>

### tweakcn

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/jnsahaj/tweakcn |
| License | Apache-2.0 |
| Phiên bản đã đọc | `a3b47b37cba97dd637de517aab52c45ec0f83456` (commit 2026-09-03) |
| Kiểm chứng | 2026-11-23; code-read; đã đọc README.md, LICENSE, package.json, lib/ai/providers.ts, lib/constants.ts; chưa chạy upstream |
| Bảo trì | low-activity (ít hoạt động) |
| Nhận định | Mã nguồn SaaS chỉnh theme shadcn/Tailwind trực quan; AI theme qua Gemini với 5 lượt miễn phí rồi trả phí. Không CI, ít commit gần đây. |
| Nguồn | [README.md](https://github.com/jnsahaj/tweakcn/blob/a3b47b37cba97dd637de517aab52c45ec0f83456/README.md) · [LICENSE](https://github.com/jnsahaj/tweakcn/blob/a3b47b37cba97dd637de517aab52c45ec0f83456/LICENSE) · [package.json](https://github.com/jnsahaj/tweakcn/blob/a3b47b37cba97dd637de517aab52c45ec0f83456/package.json) · [providers.ts](https://github.com/jnsahaj/tweakcn/blob/a3b47b37cba97dd637de517aab52c45ec0f83456/lib/ai/providers.ts) · [constants.ts](https://github.com/jnsahaj/tweakcn/blob/a3b47b37cba97dd637de517aab52c45ec0f83456/lib/constants.ts) |

<a id="ch-ui-kitten"></a>

### UI Kitten

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/akveo/react-native-ui-kitten |
| License | MIT |
| Phiên bản đã đọc | `e73dce62f946e39c946ba4006dbd6c082d393161` (commit 2026-10-06) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE.txt, package.json, src/components/package.json; chưa chạy upstream |
| Bảo trì | active (đang hoạt động) |
| Nhận định | Thư viện UI React Native trên Eva Design System, 30+ component, theme runtime. Bản 6 tuyên bố chạy New Architecture **(chưa xác minh)**; phần lớn công sức từ một người duy trì. |
| Nguồn | [README.md](https://github.com/akveo/react-native-ui-kitten/blob/e73dce62f946e39c946ba4006dbd6c082d393161/README.md) · [LICENSE.txt](https://github.com/akveo/react-native-ui-kitten/blob/e73dce62f946e39c946ba4006dbd6c082d393161/LICENSE.txt) · [package.json](https://github.com/akveo/react-native-ui-kitten/blob/e73dce62f946e39c946ba4006dbd6c082d393161/package.json) · [package.json](https://github.com/akveo/react-native-ui-kitten/blob/e73dce62f946e39c946ba4006dbd6c082d393161/src/components/package.json) |

<a id="ch-ui-skills"></a>

### ui-skills

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/ibelick/ui-skills |
| License | MIT |
| Phiên bản đã đọc | `7ef0076fce1dfa39dd2bc43b7dc13add6eda8a41` (commit 2026-11-21) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE, package.json; chưa chạy upstream |
| Bảo trì | active (đang hoạt động) |
| Nhận định | Registry skill UI/visual/motion cho agent, kèm CLI và MCP tới ui-skills.com. Phần lớn nội dung nằm ở dịch vụ web, repo chỉ chứa một phần skill. |
| Nguồn | [README.md](https://github.com/ibelick/ui-skills/blob/7ef0076fce1dfa39dd2bc43b7dc13add6eda8a41/README.md) · [LICENSE](https://github.com/ibelick/ui-skills/blob/7ef0076fce1dfa39dd2bc43b7dc13add6eda8a41/LICENSE) · [package.json](https://github.com/ibelick/ui-skills/blob/7ef0076fce1dfa39dd2bc43b7dc13add6eda8a41/package.json) |

<a id="ch-ui-ux-pro-max"></a>

### UI UX Pro Max

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/nextlevelbuilder/ui-ux-pro-max-skill |
| License | MIT |
| Phiên bản đã đọc | `7e935ad920b390035e0e139bce555d091d14c70b` (commit 2026-11-23) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE, src/ui-ux-pro-max/data/colors.csv, src/ui-ux-pro-max/data/typography.csv; chưa chạy upstream |
| Bảo trì | active (đang hoạt động) |
| Nhận định | Kho CSV tra cứu + BM25 sinh design system theo loại sản phẩm, có CLI cho nhiều agent. Không đo render thật; số liệu tăng dần qua các bản. |
| Nguồn | [README.md](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill/blob/7e935ad920b390035e0e139bce555d091d14c70b/README.md) · [LICENSE](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill/blob/7e935ad920b390035e0e139bce555d091d14c70b/LICENSE) · [colors.csv](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill/blob/7e935ad920b390035e0e139bce555d091d14c70b/src/ui-ux-pro-max/data/colors.csv) · [typography.csv](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill/blob/7e935ad920b390035e0e139bce555d091d14c70b/src/ui-ux-pro-max/data/typography.csv) |

<a id="ch-uswds"></a>

### USWDS

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/uswds/uswds |
| License | CC0-1.0 (phần GSA) + Apache-2.0 (Material Icons) + OFL-1.1 (font) (khác catalog cũ: None) |
| Phiên bản đã đọc | `029d6d792241b3b4107a630590a27ee951a152b5` (commit 2026-10-09) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE.md, package.json; chưa chạy upstream |
| Bảo trì | active (đang hoạt động) |
| Nhận định | Design system chính phủ Mỹ: component HTML/Sass/JS kèm hướng dẫn. Chỉ nhánh 3.x được bảo trì; license nhiều phần cần ghi đúng khi tái dùng icon/font. |
| Nguồn | [README.md](https://github.com/uswds/uswds/blob/029d6d792241b3b4107a630590a27ee951a152b5/README.md) · [LICENSE.md](https://github.com/uswds/uswds/blob/029d6d792241b3b4107a630590a27ee951a152b5/LICENSE.md) · [package.json](https://github.com/uswds/uswds/blob/029d6d792241b3b4107a630590a27ee951a152b5/package.json) |

<a id="ch-ux-ui-agent-skills-xias"></a>

### UX/UI Agent Skills (XIAS)

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/plugin87/ux-ui-agent-skills |
| License | MIT |
| Phiên bản đã đọc | `d0ee2fa38edea5eba0b3d3a4a43f6b7e9ab923a6` (commit 2026-11-18) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE, package.json, CHANGELOG.md; chưa chạy upstream |
| Bảo trì | active (đang hoạt động) |
| Nhận định | Doctrine thiết kế + token cho agent kèm 52 cổng đo trên trình duyệt thật và hook. Các con số 26 skill/2.144 design system là tuyên bố của tác giả **(chưa xác minh)**; nguồn gốc dữ liệu design system cần kiểm lại. |
| Nguồn | [README.md](https://github.com/plugin87/ux-ui-agent-skills/blob/d0ee2fa38edea5eba0b3d3a4a43f6b7e9ab923a6/README.md) · [LICENSE](https://github.com/plugin87/ux-ui-agent-skills/blob/d0ee2fa38edea5eba0b3d3a4a43f6b7e9ab923a6/LICENSE) · [package.json](https://github.com/plugin87/ux-ui-agent-skills/blob/d0ee2fa38edea5eba0b3d3a4a43f6b7e9ab923a6/package.json) · [CHANGELOG.md](https://github.com/plugin87/ux-ui-agent-skills/blob/d0ee2fa38edea5eba0b3d3a4a43f6b7e9ab923a6/CHANGELOG.md) |

<a id="ch-v0-app"></a>

### v0.app

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://v0.app |
| License | proprietary |
| Phiên bản đã đọc | trang web đọc ngày 2026-11-23 (không có SHA) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc https://v0.app; chưa chạy upstream |
| Bảo trì | active (đang hoạt động) |
| Nhận định | Dịch vụ đóng của Vercel sinh ứng dụng web full-stack từ prompt, mạnh ở scaffolding frontend. Phụ thuộc nền tảng Vercel, không tự host. |
| Nguồn | [v0.app](https://v0.app) |

<a id="ch-vercel-ai-sdk"></a>

### Vercel AI SDK

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/vercel/ai |
| License | Apache-2.0 |
| Phiên bản đã đọc | `fac1d6a5882903594278edef0d58859d25c80ae8` (commit 2026-11-22) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE, packages/ai/README.md, packages/ai/package.json; chưa chạy upstream |
| Bảo trì | active (đang hoạt động) |
| Nhận định | Toolkit TypeScript trung lập nhà cung cấp cho ứng dụng/agent AI (React, Svelte, Vue…). Mặc định định tuyến qua Vercel AI Gateway; AI Elements là repo riêng. |
| Nguồn | [README.md](https://github.com/vercel/ai/blob/fac1d6a5882903594278edef0d58859d25c80ae8/README.md) · [LICENSE](https://github.com/vercel/ai/blob/fac1d6a5882903594278edef0d58859d25c80ae8/LICENSE) · [README.md](https://github.com/vercel/ai/blob/fac1d6a5882903594278edef0d58859d25c80ae8/packages/ai/README.md) · [package.json](https://github.com/vercel/ai/blob/fac1d6a5882903594278edef0d58859d25c80ae8/packages/ai/package.json) |

<a id="ch-vue-pure-admin"></a>

### vue-pure-admin

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/pure-admin/vue-pure-admin |
| License | MIT |
| Phiên bản đã đọc | `fae75ad1cd52d11a7279931ef5bba2b80e363c7b` (commit 2026-10-12) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.en-US.md, LICENSE, package.json; chưa chạy upstream |
| Bảo trì | active (đang hoạt động) |
| Nhận định | Mẫu admin Vue 3 đầy đủ, nhiều phụ thuộc nặng, không có test. Nên bắt đầu từ bản pure-admin-thin. |
| Nguồn | [README.en-US.md](https://github.com/pure-admin/vue-pure-admin/blob/fae75ad1cd52d11a7279931ef5bba2b80e363c7b/README.en-US.md) · [LICENSE](https://github.com/pure-admin/vue-pure-admin/blob/fae75ad1cd52d11a7279931ef5bba2b80e363c7b/LICENSE) · [package.json](https://github.com/pure-admin/vue-pure-admin/blob/fae75ad1cd52d11a7279931ef5bba2b80e363c7b/package.json) |

<a id="ch-vuetify"></a>

### Vuetify

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/vuetifyjs/vuetify |
| License | MIT |
| Phiên bản đã đọc | `e8963a2b544e5b99759e20f9cd43d9f957a78c1b` (commit 2026-11-23) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE.md, package.json, packages/vuetify/package.json; chưa chạy upstream |
| Bảo trì | active (đang hoạt động) |
| Nhận định | Thư viện component Material cho Vue, nay ở 4.x. Vuetify 2 đã EOL, không còn vá bảo mật. |
| Nguồn | [README.md](https://github.com/vuetifyjs/vuetify/blob/e8963a2b544e5b99759e20f9cd43d9f957a78c1b/README.md) · [LICENSE.md](https://github.com/vuetifyjs/vuetify/blob/e8963a2b544e5b99759e20f9cd43d9f957a78c1b/LICENSE.md) · [package.json](https://github.com/vuetifyjs/vuetify/blob/e8963a2b544e5b99759e20f9cd43d9f957a78c1b/package.json) · [package.json](https://github.com/vuetifyjs/vuetify/blob/e8963a2b544e5b99759e20f9cd43d9f957a78c1b/packages/vuetify/package.json) |

<a id="ch-wcag-2-2"></a>

### WCAG 2.2

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://www.w3.org/TR/WCAG22/ |
| License | W3C Document License |
| Phiên bản đã đọc | trang web đọc ngày 2026-11-23 (không có SHA) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc https://www.w3.org/TR/WCAG22/; chưa chạy upstream |
| Bảo trì | active (đang hoạt động) |
| Nhận định | Chuẩn tiếp cận W3C, thước đo cho axe-core, jsx-a11y. Bản TR hiện hành là Rec 12/12/2024. |
| Nguồn | [www.w3.org/TR/WCAG22/](https://www.w3.org/TR/WCAG22/) |

<a id="ch-web-interface-guidelines-vercel"></a>

### Web Interface Guidelines (Vercel)

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/vercel-labs/web-interface-guidelines |
| License | MIT |
| Phiên bản đã đọc | `434b7f91364665f2f733b310ec54809bf8f37937` (commit 2026-10-05) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE, command.md, install.sh; chưa chạy upstream |
| Bảo trì | active (đang hoạt động) |
| Nhận định | Danh sách quy tắc UI (tương tác, focus, vùng chạm, zoom, URL là state…) kèm command.md cho agent review và install.sh. Tự mâu thuẫn nhẹ: README gợi ý `maximum-scale=1` ngay cạnh luật "Never disable browser zoom". install.sh tải command.md từ nhánh main, không ghim; repo không có .github. |
| Nguồn | [README.md](https://github.com/vercel-labs/web-interface-guidelines/blob/434b7f91364665f2f733b310ec54809bf8f37937/README.md) · [LICENSE](https://github.com/vercel-labs/web-interface-guidelines/blob/434b7f91364665f2f733b310ec54809bf8f37937/LICENSE) |

<a id="ch-web-quality-skills"></a>

### Web Quality Skills

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/addyosmani/web-quality-skills |
| License | MIT |
| Phiên bản đã đọc | `afa8da942115f2961fdbfa80807ea0b232ff6c00` (commit 2026-08-24) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE, skills/*/scripts/analyze.sh (đầu file); chưa chạy upstream |
| Bảo trì | low-activity (commit cuối cách hơn 2 tháng) |
| Nhận định | Bộ 6 Agent Skills đo-trước (audit, performance, Core Web Vitals, a11y, SEO, best practices), tự ghi là không chính thức; có analyze.sh chỉ đọc xuất JSON. Không có workflow CI; commit cuối 24/8/2026. |
| Nguồn | [README.md](https://github.com/addyosmani/web-quality-skills/blob/afa8da942115f2961fdbfa80807ea0b232ff6c00/README.md) · [LICENSE](https://github.com/addyosmani/web-quality-skills/blob/afa8da942115f2961fdbfa80807ea0b232ff6c00/LICENSE) · [gemini-extension.json](https://github.com/addyosmani/web-quality-skills/blob/afa8da942115f2961fdbfa80807ea0b232ff6c00/gemini-extension.json) |

<a id="ch-zag"></a>

### Zag

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/chakra-ui/zag |
| License | MIT |
| Phiên bản đã đọc | `cb967cd6678242c7455d3a35d4e2b6209306eb03` (commit 2026-11-22) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE, packages/core/package.json; chưa chạy upstream |
| Bảo trì | active (đang hoạt động) |
| Nhận định | Máy trạng thái component headless cho React/Vue/Solid/Svelte (thêm adapter Preact/vanilla); có AGENTS.md, CLAUDE.md, context7.json. Rất hoạt động (commit 22/11/2026), phiên bản core 1.49.0. |
| Nguồn | [README.md](https://github.com/chakra-ui/zag/blob/cb967cd6678242c7455d3a35d4e2b6209306eb03/README.md) · [LICENSE](https://github.com/chakra-ui/zag/blob/cb967cd6678242c7455d3a35d4e2b6209306eb03/LICENSE) · [package.json](https://github.com/chakra-ui/zag/blob/cb967cd6678242c7455d3a35d4e2b6209306eb03/packages/core/package.json) |

<a id="ch-zen-design-system-dizai-studio"></a>

### Zen Design System (Dizai Studio)

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/Zen-Design-System/Zen-DS |
| License | Commercial (Dizai Studio Commercial Licence Agreement v1.0, hiệu lực 2026-10-08; tự ghi bản nháp chưa qua luật sư) |
| Phiên bản đã đọc | `f81c4ff08f0622c00c951e16a833158da6c7648c` (commit 2026-11-20) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE.md, package.json, .github/workflows/ci.yml (đầu file); chưa chạy upstream |
| Bảo trì | active (đang hoạt động) |
| Nhận định | Design system thương mại (React 19 + token/icon sinh từ Figma), kèm MCP cục bộ, AGENTS.consumer.md, llms.txt. `@zen-ds/react` cấp phép theo seat qua registry riêng npm.dizai.studio; giấy phép còn là bản nháp. Phiên bản 0.3.0. |
| Nguồn | [README.md](https://github.com/Zen-Design-System/Zen-DS/blob/f81c4ff08f0622c00c951e16a833158da6c7648c/README.md) · [LICENSE.md](https://github.com/Zen-Design-System/Zen-DS/blob/f81c4ff08f0622c00c951e16a833158da6c7648c/LICENSE.md) · [package.json](https://github.com/Zen-Design-System/Zen-DS/blob/f81c4ff08f0622c00c951e16a833158da6c7648c/package.json) · [ci.yml](https://github.com/Zen-Design-System/Zen-DS/blob/f81c4ff08f0622c00c951e16a833158da6c7648c/.github/workflows/ci.yml) |

<a id="ch-zen-umami"></a>

### Zen (Umami)

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/umami-software/zen |
| License | MIT |
| Phiên bản đã đọc | `e200ca20c43a338c272f33cf61a781076c69f63e` (commit 2026-11-22) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE, SKILL.md, packages/react-zen/package.json; chưa chạy upstream |
| Bảo trì | active (đang hoạt động) |
| Nhận định | Design system/React component của Umami: quy ước shadcn, primitive Base UI, Tailwind. Có SKILL.md hướng dẫn dùng @umami/react-zen cho agent; gói react-zen 0.255.0. |
| Nguồn | [README.md](https://github.com/umami-software/zen/blob/e200ca20c43a338c272f33cf61a781076c69f63e/README.md) · [LICENSE](https://github.com/umami-software/zen/blob/e200ca20c43a338c272f33cf61a781076c69f63e/LICENSE) · [package.json](https://github.com/umami-software/zen/blob/e200ca20c43a338c272f33cf61a781076c69f63e/packages/react-zen/package.json) · [SKILL.md](https://github.com/umami-software/zen/blob/e200ca20c43a338c272f33cf61a781076c69f63e/SKILL.md) |

<a id="ch-zendesk-garden"></a>

### Zendesk Garden

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/zendeskgarden/react-components |
| License | Apache-2.0 |
| Phiên bản đã đọc | `60faa730776976016b86f1e3f90d00b0c0d43b22` (commit 2026-11-18) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE.md, package.json; chưa chạy upstream |
| Bảo trì | active (đang hoạt động) |
| Nhận định | Design system React của Zendesk; nhánh hiện tại là v10 (10.0.0-next.4, release candidate) gộp mọi component vào một gói, v9 (các gói @zendeskgarden/react-*) vẫn là bản ổn định. API v10 còn có thể đổi. |
| Nguồn | [README.md](https://github.com/zendeskgarden/react-components/blob/60faa730776976016b86f1e3f90d00b0c0d43b22/README.md) · [LICENSE.md](https://github.com/zendeskgarden/react-components/blob/60faa730776976016b86f1e3f90d00b0c0d43b22/LICENSE.md) · [package.json](https://github.com/zendeskgarden/react-components/blob/60faa730776976016b86f1e3f90d00b0c0d43b22/package.json) |

<a id="bo-sung-lovable-2026-11-23"></a>

### Lovable — đối chiếu nguồn chính thức 23/11/2026

Trang chính thức mô tả tạo ứng dụng và website qua hội thoại, với giao diện, dữ liệu và logic. Đây là mô tả của nhà cung cấp; chưa thử sản phẩm, đánh giá bảo mật hay xác minh chi phí.

Nguồn: [https://lovable.dev/build](https://lovable.dev/build).

<a id="ux-2026-11-23"></a>

## Nghiên cứu bổ sung UX — 23/11/2026

Phần này có **39 hồ sơ** skill và công cụ cho thiết kế UX/UI mà kho chưa có, thuộc bảy mảng kho còn mỏng: nghiên cứu người dùng, kiểm thử khả dụng bằng agent, đo hành vi, design review và critique, accessibility (kiểm WCAG, trình đọc màn hình, màu), bộ luật theo nền tảng, design system cho agent và UI sinh động (Generative UI). Mỗi repo được clone nông tại một commit cố định, đọc LICENSE, README, ít nhất một skill hoặc agent thật và CI nếu có; không cài hay chạy mã upstream. Cột Kiểm chứng ghi đúng phạm vi đã đọc. Số sao sẽ được bổ sung ở bước sau nên có thể để trống.

<a id="ux-tinytroupe"></a>

### TinyTroupe

| Thuộc tính | Giá trị |
|---|---|
| Repo | https://github.com/microsoft/TinyTroupe |
| License | MIT (Microsoft Corporation) |
| Phiên bản đã đọc | `7ce8be378a37ee73f9745d6781452712318afa04` (commit 2026-10-23) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, RESPONSIBLE_AI_FAQ.md, LICENSE, tinytroupe/config.ini, .github/workflows/core-tests.yml; chưa chạy upstream |
| Mảng UX | nghiên cứu người dùng giả lập: persona, focus group, phỏng vấn, chấm phương án; không điều khiển giao diện thật |
| Cơ chế đáng học | - Persona khai báo bằng JSON và fragment tái dùng; `TinyPersonFactory` lấy mẫu quần thể theo kế hoạch (README, tinytroupe/factory).<br>- `Proposition` do LLM chấm (persona_adherence, self_consistency, fluency) có thể bật để kiểm/sửa hành động của agent (tinytroupe/config.ini mục ActionGenerator; tinytroupe/validation/propositions.py, chỉ đọc lướt).<br>- `SimulationExperimentEmpiricalValidator` so phân phối trả lời mô phỏng với CSV khảo sát thật bằng t-test hoặc KS-test (README mục Empirical Validation).<br>- `InPlaceExperimentRunner` chạy A/B trong một file (tuyên bố trong README). |
| Tiêu chí và cách đo | Không có ngưỡng đạt/trượt cho UX. Kiểm chất lượng hành động mặc định TẮT: config.ini đặt `ENABLE_QUALITY_CHECKS=False` (công tắc tổng) dù `ENABLE_QUALITY_CHECK_FOR_PERSONA_ADHERENCE=True`. Kiểm bám persona do model chấm. Có bộ test pytest chạy trong CI cần OPENAI_API_KEY (core-tests.yml), chưa chạy. Ví dụ đối chiếu khảo sát thật là notebook minh họa, không phải benchmark độ khớp tổng quát (chưa xác minh). |
| Giới hạn và rủi ro | **Độ tin cậy do tác giả thừa nhận** (RESPONSIBLE_AI_FAQ.md): "TinyTroupe HAS NOT being shown to match real human behavior", mọi khả năng khớp "remains mere research or experimental investigation"; đánh giá chỉ đúng "to the extent that the demonstrations show"; mục đích là bổ sung chứ không thay thế insight người; KHÔNG dành cho quyết định hệ trọng hay chính sách. README mở đầu bằng cảnh báo WORK IN PROGRESS và Legal Disclaimer: đầu ra có thể không thực tế, sai thực tế hoặc có hại, người dùng chịu trách nhiệm kiểm.<br>Phụ thuộc API LLM bên ngoài (mặc định gpt-5-mini theo README; đổi model có thể đổi hành vi, README tự cảnh báo phải kiểm lại). Dữ liệu persona và prompt rời máy sang nhà cung cấp, trừ khi dùng Ollama (hỗ trợ thử nghiệm). API còn đổi thường xuyên. Không chứa bộ kiểm khả dụng hay a11y. |
| So với | uxagent (cùng loại giả lập người dùng nhưng UXAgent lái trình duyệt thật); last30days-skill và gpt-researcher (nghiên cứu từ nguồn thật, không giả lập người) |
| Nguồn | [README.md](https://github.com/microsoft/TinyTroupe/blob/7ce8be378a37ee73f9745d6781452712318afa04/README.md) · [RESPONSIBLE_AI_FAQ.md](https://github.com/microsoft/TinyTroupe/blob/7ce8be378a37ee73f9745d6781452712318afa04/RESPONSIBLE_AI_FAQ.md) · [LICENSE](https://github.com/microsoft/TinyTroupe/blob/7ce8be378a37ee73f9745d6781452712318afa04/LICENSE) · [config.ini](https://github.com/microsoft/TinyTroupe/blob/7ce8be378a37ee73f9745d6781452712318afa04/tinytroupe/config.ini) · [core-tests.yml](https://github.com/microsoft/TinyTroupe/blob/7ce8be378a37ee73f9745d6781452712318afa04/.github/workflows/core-tests.yml) |

<a id="ux-uxagent"></a>

### UXAgent

| Thuộc tính | Giá trị |
|---|---|
| Repo | https://github.com/neuhai/UXAgent |
| License | Không có file LICENSE; README (badge) và `pyproject.toml` (`license = "MIT"`) tự khai MIT (chưa xác minh bằng văn bản giấy phép) |
| Phiên bản đã đọc | `4d3b1f1c1fef93c5e2ea7d104153ea164ba1acbd` (commit 2025-11-05) |
| Kiểm chứng | 2026-11-23; code-read; đã đọc README.md, pyproject.toml, conf/base.yaml, src/simulated_web_agent/agent/agent.py, src/simulated_web_agent/agent/shop_prompts/action.txt, src/simulated_web_agent/agent/shop_prompts/reflect.txt, src/simulated_web_agent/agent/shop_prompts/wonder.txt, src/simulated_web_agent/agent/shop_prompts/memory_importance.txt, src/simulated_web_agent/main/survey.py; chưa chạy upstream |
| Mảng UX | kiểm thử khả dụng giả lập trên web thật: persona, nhiệm vụ mua sắm, SUS, memory trace |
| Cơ chế đáng học | - Vòng agent perceive → plan → act → feedback, thêm reflect và wonder (suy nghĩ ngẫu nhiên) để tạo hành vi giống người; README gọi là dual-system (agent.py, shop_prompts/*.txt).<br>- Memory stream có độ quan trọng do LLM chấm 1–10 (memory_importance.txt, memory.py), truy xuất theo `kind_weight` khi act.<br>- `runConfig.yaml` khai báo total_personas, concurrency, demographics có trọng số, example_persona, questionnaire (README, conf/).<br>- `survey.py` đưa memory_trace.json + bảng hỏi cho model để sinh câu trả lời SUS sau phiên. |
| Tiêu chí và cách đo | Không có rubric tự động hay ngưỡng đạt/trượt: điểm SUS và hành vi do LLM sinh ra. Đánh giá trong bài báo là nghiên cứu với 16 nhà nghiên cứu UX (độ hữu ích M=1.29, tin cậy dữ liệu M=0.57 SD=0.85 ở một chỗ và M=0.63 SD=0.81 ở chỗ khác trong cùng bài, thang -2..+2). Repo không có test hay CI (không thấy thư mục tests/workflows). Không thấy phép đối chiếu với hành vi người thật trong các đoạn đã đọc. |
| Giới hạn và rủi ro | **Độ tin cậy do tác giả/bài báo thừa nhận** (arXiv 2504.09407v3, đọc bản PDF): người tham gia đánh giá có "mixed feeling" về việc dữ liệu có đại diện người thật; P6: "Some behaviors are abnormal—not what real users would do"; khi hỏi LLM agent có thay được người thật không, đa số không đồng ý (M=-0.57, SD=1.16); P1 lo nhà nghiên cứu "overtrust". Mục 5.3 viết: dữ liệu LLM nên là "supplementary rather than definitive", "cannot fully replicate the complexity of real human behavior", cảnh báo rủi ro dùng dữ liệu giả thay nghiên cứu thật và rủi ro riêng tư/y tế; mục 5.2: "not substitutes for human data". Mục 5.4 nêu giới hạn số người tham gia ít. Kết luận bài chỉ nói giúp phát hiện lỗi thiết kế nghiên cứu và có cái nhìn sớm, không tuyên bố khớp người thật.<br>Quan sát mã (chưa chạy): trong `act()` của agent.py, `inputs` và `selects` đều được gán từ `env["clickable_elements"]` giống `clickables`, nên danh sách đích hợp lệ không phân biệt loại phần tử. Mã dùng Playwright duyệt site thật, ví dụ mặc định trỏ Amazon và có `--wait-for-login`: rủi ro thao tác tài khoản thật. HTML trang, persona và memory gửi tới LLM (Anthropic/OpenAI/AWS Bedrock theo README). Thiếu file LICENSE. |
| So với | tinytroupe (cùng giả lập người dùng, không lái UI); e2e-testerarmy và stagehand (agent trình duyệt không có persona); evondevkit-ui-ux (skill đánh giá UX do model chấm) |
| Nguồn | [README.md](https://github.com/neuhai/UXAgent/blob/4d3b1f1c1fef93c5e2ea7d104153ea164ba1acbd/README.md) · [pyproject.toml](https://github.com/neuhai/UXAgent/blob/4d3b1f1c1fef93c5e2ea7d104153ea164ba1acbd/pyproject.toml) · [base.yaml](https://github.com/neuhai/UXAgent/blob/4d3b1f1c1fef93c5e2ea7d104153ea164ba1acbd/conf/base.yaml) · [agent.py](https://github.com/neuhai/UXAgent/blob/4d3b1f1c1fef93c5e2ea7d104153ea164ba1acbd/src/simulated_web_agent/agent/agent.py) · [action.txt](https://github.com/neuhai/UXAgent/blob/4d3b1f1c1fef93c5e2ea7d104153ea164ba1acbd/src/simulated_web_agent/agent/shop_prompts/action.txt) · [reflect.txt](https://github.com/neuhai/UXAgent/blob/4d3b1f1c1fef93c5e2ea7d104153ea164ba1acbd/src/simulated_web_agent/agent/shop_prompts/reflect.txt) · [wonder.txt](https://github.com/neuhai/UXAgent/blob/4d3b1f1c1fef93c5e2ea7d104153ea164ba1acbd/src/simulated_web_agent/agent/shop_prompts/wonder.txt) · [memory_importance.txt](https://github.com/neuhai/UXAgent/blob/4d3b1f1c1fef93c5e2ea7d104153ea164ba1acbd/src/simulated_web_agent/agent/shop_prompts/memory_importance.txt) · [survey.py](https://github.com/neuhai/UXAgent/blob/4d3b1f1c1fef93c5e2ea7d104153ea164ba1acbd/src/simulated_web_agent/main/survey.py) · [bài báo](https://arxiv.org/abs/2504.09407) |

<a id="ux-cookiy-user-research-skill"></a>

### Cookiy User Research Skill

| Thuộc tính | Giá trị |
|---|---|
| Repo | https://github.com/cookiy-ai/user-research-skill |
| License | MIT (Cookiy AI) cho nội dung repo; dịch vụ Cookiy AI là sản phẩm thương mại riêng, không nằm trong license này |
| Phiên bản đã đọc | `4aa62a47150e17b00bcade08f340aeb7755fd2c0` (commit 2026-11-12) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE, SKILL.md, references/cookiy/cookiy.md, references/cookiy/cookiy-qual.md, references/cookiy/cookiy-study-synthetic-user.md, references/cookiy/cookiy-billing.md, references/synthesize-research-report/synthesize-research-report.md, references/synthesize-research-report/phases/phase4-synthesis.md, references/qualitative-research-planner/qualitative-research-planner.md, .github/workflows/release-skill.yml; chưa chạy upstream |
| Mảng UX | nghiên cứu người dùng: lập kế hoạch, phỏng vấn/khảo sát, tổng hợp phát hiện, persona từ dữ liệu |
| Cơ chế đáng học | - SKILL.md là bộ định tuyến theo ý định (Route A lập kế hoạch, B tổng hợp, C Cookiy), hỏi một câu làm rõ khi mơ hồ.<br>- Pipeline tổng hợp 5 pha cố định, mỗi pha một sub-agent, đọc tóm tắt pha trước; chọn khung ưu tiên theo loại mục tiêu (bảng trong synthesize-research-report.md).<br>- Cổng chất lượng mỗi pha: mỗi theme/phát hiện phải có mặt trong ít nhất 2 buổi phỏng vấn, mỗi phát hiện có 1 trích dẫn chính và 2 trích dẫn phụ, ghi mức tin cậy Cao/Vừa/Thấp (phase3-themes.md, phase4-synthesis.md, phase5-report.md).<br>- Sau khi chạy xong cho link phát lại video/bản ghi để người dùng tự kiểm dữ liệu là người thật hay tổng hợp (cookiy-qual.md). |
| Tiêu chí và cách đo | Tiêu chí là checklist trong văn bản (≥2 nguồn mỗi phát hiện, mốc 5–8 phát hiện chính, mức tin cậy), do model tự đối chiếu, không có script hay eval. Repo không có test; workflow release-skill.yml chỉ đóng gói zip và cập nhật bản `latest`. |
| Giới hạn và rủi ro | Tuyên bố của tác giả (chưa xác minh): "world's first agentic AI user researcher", "900K+ views", thời gian có người trả lời đầu tiên khoảng 30 phút.<br>Skill có mục "Cookiy Suggestions" bảo agent chủ động mời người dùng chạy nghiên cứu trên Cookiy sau mỗi bước: thiên lệch bán hàng. Mọi thao tác nền tảng (tuyển người, phỏng vấn tổng hợp, báo cáo) tốn tiền từ ví, có nạp tự động bằng thẻ đã lưu (cookiy-billing.md).<br>Dữ liệu nghiên cứu đi qua s-api.cookiy.ai; README hướng dẫn bật egress mạng, đề xuất "All domains" hoặc thêm domain đó; đăng nhập bằng token dán lại cho agent. Workflow đẩy ép (force) tag `latest` mỗi lần push main nên zip tải về không ghim phiên bản.<br>Người dùng tổng hợp được giới thiệu là "faster, cheaper, good for piloting" mà không có đánh giá độ khớp với người thật. |
| So với | pm-skills (bộ skill PM có phần khám phá); academic-research-skills (pipeline tổng hợp nghiên cứu); tinytroupe và uxagent (người dùng giả lập, có thừa nhận giới hạn rõ hơn) |
| Nguồn | [README.md](https://github.com/cookiy-ai/user-research-skill/blob/4aa62a47150e17b00bcade08f340aeb7755fd2c0/README.md) · [LICENSE](https://github.com/cookiy-ai/user-research-skill/blob/4aa62a47150e17b00bcade08f340aeb7755fd2c0/LICENSE) · [SKILL.md](https://github.com/cookiy-ai/user-research-skill/blob/4aa62a47150e17b00bcade08f340aeb7755fd2c0/SKILL.md) · [cookiy.md](https://github.com/cookiy-ai/user-research-skill/blob/4aa62a47150e17b00bcade08f340aeb7755fd2c0/references/cookiy/cookiy.md) · [cookiy-qual.md](https://github.com/cookiy-ai/user-research-skill/blob/4aa62a47150e17b00bcade08f340aeb7755fd2c0/references/cookiy/cookiy-qual.md) · [cookiy-study-synthetic-user.md](https://github.com/cookiy-ai/user-research-skill/blob/4aa62a47150e17b00bcade08f340aeb7755fd2c0/references/cookiy/cookiy-study-synthetic-user.md) · [cookiy-billing.md](https://github.com/cookiy-ai/user-research-skill/blob/4aa62a47150e17b00bcade08f340aeb7755fd2c0/references/cookiy/cookiy-billing.md) · [synthesize-research-report.md](https://github.com/cookiy-ai/user-research-skill/blob/4aa62a47150e17b00bcade08f340aeb7755fd2c0/references/synthesize-research-report/synthesize-research-report.md) · [phase4-synthesis.md](https://github.com/cookiy-ai/user-research-skill/blob/4aa62a47150e17b00bcade08f340aeb7755fd2c0/references/synthesize-research-report/phases/phase4-synthesis.md) · [qualitative-research-planner.md](https://github.com/cookiy-ai/user-research-skill/blob/4aa62a47150e17b00bcade08f340aeb7755fd2c0/references/qualitative-research-planner/qualitative-research-planner.md) · [release-skill.yml](https://github.com/cookiy-ai/user-research-skill/blob/4aa62a47150e17b00bcade08f340aeb7755fd2c0/.github/workflows/release-skill.yml) |

<a id="ux-retentioneering"></a>

### Retentioneering

| Thuộc tính | Giá trị |
|---|---|
| Repo | https://github.com/retentioneering/retentioneering-tools |
| License | Apache-2.0 (LICENSE, NOTICE); COMMERCIAL.md mô tả mô hình open-core: dịch vụ thương mại (hosted, agent-to-agent, recipe pack cao cấp) không thuộc license này; tên và logo là nhãn hiệu |
| Phiên bản đã đọc | `289c003591d224bcd036d0e7d5c1b2d7acf7e6c1` (commit 2026-11-14) |
| Kiểm chứng | 2026-11-23; code-read; đã đọc README.md, LICENSE, COMMERCIAL.md, NOTICE, src/retentioneering/_tracking.py, .agents/skills/retentioneering-product-analytics/SKILL.md, .agents/skills/retentioneering-product-analytics/references/gotchas-and-validation.md, .github/workflows/ci.yml; chưa chạy upstream |
| Mảng UX | đo hành vi: đường đi, phễu, phân khúc, so sánh trước/sau; phục vụ chẩn đoán luồng UX bằng dữ liệu |
| Cơ chế đáng học | - SKILL.md bắt buộc chạy `scripts/inspect_event_log.py` để profile dữ liệu và đề xuất schema TRƯỚC khi chọn phương pháp; báo lại ánh xạ cột, số lượng, khoảng thời gian, cờ đỏ.<br>- Chọn công thức nhỏ nhất trong 10 mẫu R1–R10 (analysis-recipes.md); mỗi phần trăm phải nêu mẫu số, lọc dân số phải ghi số lượng, chú thích hình lấy số từ các hàm `*_data` không đồ họa.<br>- Đầu ra tách Quan sát / Diễn giải / Giải thích thay thế / Giả thuyết sản phẩm / Hạn chế; lưu `recipe()` để tái lập từ dữ liệu thô.<br>- Diff mode của transition graph và step matrix so hai phân khúc (đoạn cắt theo khoảng thời gian, phễu đạt/không đạt). |
| Tiêu chí và cách đo | Kiểm bằng danh sách: gotchas G1–G10 (API), checklist B1–B10 (tính toàn vẹn), mục C "self-checks worth automating" (do model và người tự áp dụng). Không có ngưỡng thống kê cố định trong skill. CI ci.yml chạy lint, test JS và pytest trên Python 3.11–3.13 (đã mở workflow, chưa chạy). Chưa thấy eval kiểm skill có làm agent phân tích đúng hơn. |
| Giới hạn và rủi ro | **Telemetry mặc định bật** (`_tracking.py`): gửi sự kiện tới PostHog (eu.i.posthog.com) kèm khóa dự án nhúng sẵn; distinct_id băm từ /etc/machine-id hoặc địa chỉ MAC, hoặc UUID lưu ở ~/.retentioneering/config.json; thuộc tính gồm phiên bản thư viện, OS, phiên bản Python, môi trường (colab/vscode/jupyter/script), hash đường dẫn script và lệnh, TÊN tham số (không gửi giá trị) và loại lỗi. README khẳng định không gửi tên sự kiện/định danh/nội dung đường đi; mã đã đọc khớp với phần tên tham số, nhưng chưa chạy để xác nhận. Tắt bằng biến môi trường RETENTIONEERING_NO_TRACK, secret Colab hoặc file cấu hình; chú thích trong mã nói tiến trình CI/offline cũng không gửi, nhưng hàm kiểm opt-out đã đọc không có nhánh CI.<br>Không đo UX định tính; cần dữ liệu sự kiện có sẵn. MCP server còn beta. Tương quan đường đi không phải nhân quả (skill tự nhắc). Open-core: tính năng nâng cao nằm ngoài license. |
| So với | posthog (nền tảng analytics đầy đủ, có replay); openreplay (session replay tự host); umami (analytics nhẹ không có đường đi chi tiết) |
| Nguồn | [README.md](https://github.com/retentioneering/retentioneering-tools/blob/289c003591d224bcd036d0e7d5c1b2d7acf7e6c1/README.md) · [LICENSE](https://github.com/retentioneering/retentioneering-tools/blob/289c003591d224bcd036d0e7d5c1b2d7acf7e6c1/LICENSE) · [COMMERCIAL.md](https://github.com/retentioneering/retentioneering-tools/blob/289c003591d224bcd036d0e7d5c1b2d7acf7e6c1/COMMERCIAL.md) · [NOTICE](https://github.com/retentioneering/retentioneering-tools/blob/289c003591d224bcd036d0e7d5c1b2d7acf7e6c1/NOTICE) · [_tracking.py](https://github.com/retentioneering/retentioneering-tools/blob/289c003591d224bcd036d0e7d5c1b2d7acf7e6c1/src/retentioneering/_tracking.py) · [SKILL.md](https://github.com/retentioneering/retentioneering-tools/blob/289c003591d224bcd036d0e7d5c1b2d7acf7e6c1/.agents/skills/retentioneering-product-analytics/SKILL.md) · [gotchas-and-validation.md](https://github.com/retentioneering/retentioneering-tools/blob/289c003591d224bcd036d0e7d5c1b2d7acf7e6c1/.agents/skills/retentioneering-product-analytics/references/gotchas-and-validation.md) · [ci.yml](https://github.com/retentioneering/retentioneering-tools/blob/289c003591d224bcd036d0e7d5c1b2d7acf7e6c1/.github/workflows/ci.yml) |

<a id="ux-awizemann-harness"></a>

### Harness (user-test agent)

| Thuộc tính | Giá trị |
|---|---|
| Repo | https://github.com/awizemann/harness |
| License | MIT (Alan Wizemann); submodule vendor/WebDriverAgent và thư mục vendors có license riêng, chưa đọc |
| Phiên bản đã đọc | `3f58c077ded131cca71d75efb05c5d325f0ed18f` (commit 2026-09-02) |
| Kiểm chứng | 2026-11-23; code-read; đã đọc README.md, LICENSE, docs/PROMPTS/system-prompt.md, docs/PROMPTS/friction-vocab.md, docs/PROMPTS/persona-defaults.md, docs/PROMPTS/platforms/web.md, standards/13-agent-loop.md, standards/08-run-log-integrity.md, Harness/Domain/AgentLoop.swift; chưa chạy upstream |
| Mảng UX | kiểm thử khả dụng bằng agent trên iOS/macOS/web: persona, ghi ma sát, đường đi có thể phát lại |
| Cơ chế đáng học | - System prompt dùng một nguồn (docs/PROMPTS/system-prompt.md), nạp lúc chạy; ép trường `observation` và `intent` mỗi lượt, một hành động mỗi lượt.<br>- Quy tắc coi chữ trên màn hình là nội dung cần đánh giá, không phải chỉ dẫn (chống prompt injection từ app đang test).<br>- Taxonomy ma sát cố định ở friction-vocab.md, kèm danh sách cố ý KHÔNG có (accessibility_failure, bug, slow) và quy tắc viết detail theo giọng persona.<br>- Bộ phát hiện vòng lặp (AgentLoop.swift): cửa sổ 3 lượt, dHash khoảng cách Hamming ≤5 và tọa độ lệch ≤8pt thì dừng blocked; ngân sách mặc định 40 bước; log events.jsonl chỉ ghi nối thêm, có schemaVersion (standards/08, 13). |
| Tiêu chí và cách đo | Kết quả gồm verdict success/failure/blocked và `would_real_user_succeed` do chính model tự báo, có thể khác verdict. Không có ngưỡng UX hay chấm điểm khả dụng; ma sát do model gắn nhãn. Tác giả tuyên bố 359 unit test pass (chưa xác minh); repo có thư mục Tests/HarnessTests và smoke test MCP, nhưng .github chỉ có FUNDING, ISSUE_TEMPLATE, PR template và copilot-instructions, không có workflows. |
| Giới hạn và rủi ro | Chỉ macOS 14+, cần Xcode/simctl; trạng thái alpha. Ảnh chụp màn hình app đang test gửi tới nhà cung cấp LLM (có client Claude, OpenAI, Gemini, Ollama; Ollama chạy cục bộ). Phiên web có thể tiêm cookie và localStorage để đăng nhập (`session_state`) và xuất lại: rủi ro lộ thông tin phiên.<br>Persona và đánh giá hoàn toàn do model sinh, không đối chiếu với người thật; tác giả cũng không tuyên bố độ khớp. Không có nhãn lỗi accessibility theo thiết kế. |
| So với | e2e-testerarmy và stagehand (agent trình duyệt, không có persona hay taxonomy ma sát); playwright-mcp (điều khiển trình duyệt qua MCP); uxagent (giả lập người dùng trên web) |
| Nguồn | [README.md](https://github.com/awizemann/harness/blob/3f58c077ded131cca71d75efb05c5d325f0ed18f/README.md) · [LICENSE](https://github.com/awizemann/harness/blob/3f58c077ded131cca71d75efb05c5d325f0ed18f/LICENSE) · [system-prompt.md](https://github.com/awizemann/harness/blob/3f58c077ded131cca71d75efb05c5d325f0ed18f/docs/PROMPTS/system-prompt.md) · [friction-vocab.md](https://github.com/awizemann/harness/blob/3f58c077ded131cca71d75efb05c5d325f0ed18f/docs/PROMPTS/friction-vocab.md) · [persona-defaults.md](https://github.com/awizemann/harness/blob/3f58c077ded131cca71d75efb05c5d325f0ed18f/docs/PROMPTS/persona-defaults.md) · [web.md](https://github.com/awizemann/harness/blob/3f58c077ded131cca71d75efb05c5d325f0ed18f/docs/PROMPTS/platforms/web.md) · [13-agent-loop.md](https://github.com/awizemann/harness/blob/3f58c077ded131cca71d75efb05c5d325f0ed18f/standards/13-agent-loop.md) · [08-run-log-integrity.md](https://github.com/awizemann/harness/blob/3f58c077ded131cca71d75efb05c5d325f0ed18f/standards/08-run-log-integrity.md) · [AgentLoop.swift](https://github.com/awizemann/harness/blob/3f58c077ded131cca71d75efb05c5d325f0ed18f/Harness/Domain/AgentLoop.swift) |

<a id="ux-product-engineer-skills"></a>

### Product Engineer Skills

| Thuộc tính | Giá trị |
|---|---|
| Repo | https://github.com/Trystan-SA/product-engineer-skills |
| License | MIT (Trystan Sarrade) |
| Phiên bản đã đọc | `5e0534c97f29b82a5e2077000eb1cb8732f03296` (commit 2026-11-22) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE, plugin.json, skills/happy-path-audit/SKILL.md, skills/flow-test/SKILL.md, skills/usability-test-plan/SKILL.md, tools/check_skills.py, .github/workflows/validate.yml; chưa chạy upstream |
| Mảng UX | đo chi phí luồng, ngân sách UX trong CI, kế hoạch test khả dụng, review UX theo PR, adoption/A-B test |
| Cơ chế đáng học | - happy-path-audit: bảng từng bước với toán tử KLM (K 0,28s; P 1,1s; BB 0,1s; H 0,4s; M 1,35s), tổng click/trường/màn hình, đề xuất rút gọn xếp theo tiết kiệm/công sức; tự nói KLM chỉ để so sánh phiên bản, không hứa thời gian cho người dùng.<br>- flow-test: fixture `UxMeter` đếm sự kiện click/input thật trong trang bằng listener pha capture, `expectWithin({clicks, fields, navigations})` làm UX regression fail CI.<br>- usability-test-plan: tình huống nhiệm vụ không dùng nhãn giao diện, Single Ease Question 1–7, ghi riêng hành vi và lời nói, "hành vi thắng" khi mâu thuẫn; cảnh báo 5 người không đủ để báo phần trăm.<br>- tools/check_skills.py: frontmatter chỉ trường di động, name khớp thư mục, description ≤1024 ký tự, không dùng tên công cụ riêng của một agent. |
| Tiêu chí và cách đo | Có ngưỡng đo bằng máy ở flow-test (ngân sách click/trường/điều hướng, test fail khi vượt) nhưng ngân sách do người đặt từ lần đo. Phần còn lại là quy trình văn bản. CI validate.yml (đã đọc) chạy check_skills.py, unittest cho script thống kê, `claude plugin validate --strict` và cài thử bằng Codex; không có eval chất lượng đầu ra của từng skill. Script sample_size.py và readout.py chưa đọc. |
| Giới hạn và rủi ro | Repo vừa đổi mục tiêu (trước là claude-design-system-prompt, nay chỉ còn ở tag v1-design-prompt theo README) và cập nhật liên tục (commit 1 ngày trước ngày kiểm). KLM giả định chuyên gia không lỗi, tác giả đã ghi giới hạn. UxMeter không đếm click do JS của app tạo ra và chọn `<select>` cần cộng tay.<br>Skill yêu cầu agent đọc mã thật và có thể thêm công cụ test; skill nói sẽ hỏi trước khi thêm dependency (tuyên bố, chưa xác minh). |
| So với | pm-skills (skill PM, nhiều khung ra quyết định); playwright (nền test E2E); evondevkit-ui-ux và ui-ux-pro-max (skill UI/UX nghiêng về thiết kế hình ảnh) |
| Nguồn | [README.md](https://github.com/Trystan-SA/product-engineer-skills/blob/5e0534c97f29b82a5e2077000eb1cb8732f03296/README.md) · [LICENSE](https://github.com/Trystan-SA/product-engineer-skills/blob/5e0534c97f29b82a5e2077000eb1cb8732f03296/LICENSE) · [plugin.json](https://github.com/Trystan-SA/product-engineer-skills/blob/5e0534c97f29b82a5e2077000eb1cb8732f03296/plugin.json) · [SKILL.md](https://github.com/Trystan-SA/product-engineer-skills/blob/5e0534c97f29b82a5e2077000eb1cb8732f03296/skills/happy-path-audit/SKILL.md) · [SKILL.md](https://github.com/Trystan-SA/product-engineer-skills/blob/5e0534c97f29b82a5e2077000eb1cb8732f03296/skills/flow-test/SKILL.md) · [SKILL.md](https://github.com/Trystan-SA/product-engineer-skills/blob/5e0534c97f29b82a5e2077000eb1cb8732f03296/skills/usability-test-plan/SKILL.md) · [check_skills.py](https://github.com/Trystan-SA/product-engineer-skills/blob/5e0534c97f29b82a5e2077000eb1cb8732f03296/tools/check_skills.py) · [validate.yml](https://github.com/Trystan-SA/product-engineer-skills/blob/5e0534c97f29b82a5e2077000eb1cb8732f03296/.github/workflows/validate.yml) |

<a id="ux-testzeus-hercules"></a>

### TestZeus Hercules

| Thuộc tính | Giá trị |
|---|---|
| Repo | https://github.com/test-zeus-ai/testzeus-hercules |
| License | AGPL-3.0-only (copyleft mạng); vendor axe-core 4.10.3 theo MPL-2.0 và phông OFL-1.1 (THIRD_PARTY_NOTICES.md) |
| Phiên bản đã đọc | `f67e5daaa963f8e19b52bd15e391f5264c420fe9` (commit 2026-11-23) |
| Kiểm chứng | 2026-11-23; code-read; đã đọc README.md, LICENSE, THIRD_PARTY_NOTICES.md, docs/guide/quality-checks.md, testzeus_hercules/quality/checks.py, testzeus_hercules/explore/oracles.py, bench/README.md, .github/workflows/ci.yml; chưa chạy upstream |
| Mảng UX | kiểm thử luồng, accessibility (WCAG 2.0–2.2 A/AA), layout, visual regression, explore phát hiện lỗi |
| Cơ chế đáng học | - Quality step trong ngôn ngữ tự nhiên: model đọc một lần thành payload có cấu trúc `{kind: a11y\|visual\|layout, fail_on}`, phần kiểm chạy bằng mã (quality-checks.md).<br>- checks.py: tương phản, tên truy cập, kích thước vùng chạm tối thiểu `MIN_TARGET_PX = 24.0`, ảnh thiếu alt, kiểm tab bàn phím; axe-core đóng gói chạy offline.<br>- Mỗi finding nêu selector và giá trị sửa (màu gần nhất đạt tương phản, kích thước vùng chạm, aria-label), áp vào trang thật rồi kiểm lại mới đặt `verified: true`.<br>- explore/oracles.py: oracle ba tầng code (lỗi console/mạng, hành động không đổi gì), invariant (lời hứa kiểm bằng mã) và judged (model cho hai xác suất: sai thật hay chỉ là sở thích thiết kế, loại sau chỉ thành ghi chú UX). |
| Tiêu chí và cách đo | Mức `fail_on` critical/serious/moderate/minor (mặc định serious); visual: baseline mới tạo ra là unverified và tính như fail. Có bench cục bộ 30 kịch bản (21 dương, 9 âm) đo accuracy, false pass, false fail, p95 thời gian và độ chính xác theo tag (bench/README.md); thư mục results nằm ngoài git nên số liệu cụ thể chưa có và chưa xác minh. CI ci.yml (đã mở phần đầu) chạy lint và test offline, bỏ test live cần model/khóa. |
| Giới hạn và rủi ro | AGPL-3.0-only: dùng làm dịch vụ mạng buộc công khai mã nguồn bản sửa; không thể mang thẳng mã vào skill MIT/Apache. Không có chế độ không model: cần model cục bộ hoặc OpenRouter/OpenAI-compatible. Chính sách egress: `hybrid` gửi văn bản trang (và ảnh khi không chắc) ra ngoài; `local` không gửi gì.<br>Telemetry PostHog ẩn danh bật theo README (phiên bản, tên cài đặt, số run và kết quả, loại agent, tên lớp lỗi, id cài đặt ngẫu nhiên; không gửi nội dung/URL/bí mật theo tuyên bố, chưa xác minh); tắt bằng `--no-telemetry`, HERCULES_TELEMETRY=0 hoặc DO_NOT_TRACK=1, luôn tắt khi egress `local`. Repo cập nhật ngay ngày kiểm (v2.0.1, viết lại từ v1), API còn đổi. |
| So với | axe-core và eslint-plugin-jsx-a11y (kiểm a11y tất định, không cần model); playwright và playwright-mcp (hạ tầng điều khiển); e2e-testerarmy (agent test E2E) |
| Nguồn | [README.md](https://github.com/test-zeus-ai/testzeus-hercules/blob/f67e5daaa963f8e19b52bd15e391f5264c420fe9/README.md) · [LICENSE](https://github.com/test-zeus-ai/testzeus-hercules/blob/f67e5daaa963f8e19b52bd15e391f5264c420fe9/LICENSE) · [THIRD_PARTY_NOTICES.md](https://github.com/test-zeus-ai/testzeus-hercules/blob/f67e5daaa963f8e19b52bd15e391f5264c420fe9/THIRD_PARTY_NOTICES.md) · [quality-checks.md](https://github.com/test-zeus-ai/testzeus-hercules/blob/f67e5daaa963f8e19b52bd15e391f5264c420fe9/docs/guide/quality-checks.md) · [checks.py](https://github.com/test-zeus-ai/testzeus-hercules/blob/f67e5daaa963f8e19b52bd15e391f5264c420fe9/testzeus_hercules/quality/checks.py) · [oracles.py](https://github.com/test-zeus-ai/testzeus-hercules/blob/f67e5daaa963f8e19b52bd15e391f5264c420fe9/testzeus_hercules/explore/oracles.py) · [README.md](https://github.com/test-zeus-ai/testzeus-hercules/blob/f67e5daaa963f8e19b52bd15e391f5264c420fe9/bench/README.md) · [ci.yml](https://github.com/test-zeus-ai/testzeus-hercules/blob/f67e5daaa963f8e19b52bd15e391f5264c420fe9/.github/workflows/ci.yml) |

<a id="ux-webqa-agent"></a>

### WebQA Agent

| Thuộc tính | Giá trị |
|---|---|
| Repo | https://github.com/MigoXLab/webqa-agent |
| License | Apache-2.0 cho repo; skill `ui-audit` ghi `author: Tommy Geoco`, `license: MIT` trong frontmatter, không có file LICENSE riêng trong thư mục đó (nguồn gốc/giấy phép MIT chưa xác minh) |
| Phiên bản đã đọc | `aa156d4ab8b2a4658b13eb33073c686be843d3e4` (commit 2026-07-02) |
| Kiểm chứng | 2026-11-23; code-read; đã đọc README.md, LICENSE, skills/webqa/SKILL.md, skills/webqa/references/mini-agent.md, skills/webqa/references/setup.md, webqa_agent/executor/flash/skills/ui-audit/SKILL.md, webqa_agent/executor/gen/agents/status_determination.py, tests/test_status_determination.py, .github/workflows/workflow.yml; chưa chạy upstream |
| Mảng UX | design review/UI audit do model chấm, kiểm thử luồng, an toàn cơ bản (nuclei-scan), hiệu năng; đầu vào là URL |
| Cơ chế đáng học | - ui-audit/SKILL.md: quy trình chụp ảnh, lấy accessibility snapshot, nạp `00-core-framework` rồi tải từng tham chiếu theo nhu cầu; mục bắt buộc Visual Hierarchy, Visual Style, Accessibility, mục theo ngữ cảnh Navigation/Forms/Onboarding; đầu ra JSON mỗi check có `status: pass\|warn\|fail` và `priority_fixes` có `framework_reference`.<br>- 22 file tham chiếu đánh số (checklist, patterns, defects) nạp theo yêu cầu thay vì đưa hết vào prompt.<br>- status_determination.py: `apply_safety_guard` buộc kết quả `failed` nếu có CRITICAL hoặc HARD_FAIL dù LLM nói khác; `verdict_fallback` tất định khi thiếu STATUS; có test (test_status_determination.py).<br>- skills/webqa/SKILL.md: "Do not treat execution completion as test success", pass/fail chỉ lấy từ báo cáo. |
| Tiêu chí và cách đo | UI audit chỉ có nhãn pass/warn/fail do model chấm, không có ngưỡng số hay kiểm tất định (khác Hercules). Test pytest có trong repo (tests/, chưa chạy). Workflow duy nhất đã mở là workflow.yml chỉ build và đẩy PyPI khi có tag, không chạy test; chưa thấy eval cho chất lượng UI audit. |
| Giới hạn và rủi ro | Skill công khai `webqa` gọi MCP tới nền tảng WebQA qua `WEBQA_API_URL` và `WEBQA_API_KEY` (setup.md): URL, task và cookie đăng nhập có thể rời máy tới nền tảng; tài liệu cho phép truyền cookie cho test đã đăng nhập.<br>Skill ui-audit có tác giả và license MIT khác repo mẹ nhưng không kèm giấy phép tại chỗ; bộ tham chiếu có phát biểu kiểu "15%+ of users have some disability" không dẫn nguồn. Prompt và README chủ yếu tiếng Trung/Anh, README có khối SEO và tuyên bố marketing như "fully automated", "second-scale" (chưa xác minh). |
| So với | testzeus-hercules (kiểm a11y bằng mã); e2e-testerarmy và stagehand (agent trình duyệt); googlechrome-lighthouse (kiểm tất định hiệu năng/a11y); evondevkit-ui-ux (rubric UX do model chấm) |
| Nguồn | [README.md](https://github.com/MigoXLab/webqa-agent/blob/aa156d4ab8b2a4658b13eb33073c686be843d3e4/README.md) · [LICENSE](https://github.com/MigoXLab/webqa-agent/blob/aa156d4ab8b2a4658b13eb33073c686be843d3e4/LICENSE) · [SKILL.md](https://github.com/MigoXLab/webqa-agent/blob/aa156d4ab8b2a4658b13eb33073c686be843d3e4/skills/webqa/SKILL.md) · [mini-agent.md](https://github.com/MigoXLab/webqa-agent/blob/aa156d4ab8b2a4658b13eb33073c686be843d3e4/skills/webqa/references/mini-agent.md) · [setup.md](https://github.com/MigoXLab/webqa-agent/blob/aa156d4ab8b2a4658b13eb33073c686be843d3e4/skills/webqa/references/setup.md) · [SKILL.md](https://github.com/MigoXLab/webqa-agent/blob/aa156d4ab8b2a4658b13eb33073c686be843d3e4/webqa_agent/executor/flash/skills/ui-audit/SKILL.md) · [status_determination.py](https://github.com/MigoXLab/webqa-agent/blob/aa156d4ab8b2a4658b13eb33073c686be843d3e4/webqa_agent/executor/gen/agents/status_determination.py) · [test_status_determination.py](https://github.com/MigoXLab/webqa-agent/blob/aa156d4ab8b2a4658b13eb33073c686be843d3e4/tests/test_status_determination.py) · [workflow.yml](https://github.com/MigoXLab/webqa-agent/blob/aa156d4ab8b2a4658b13eb33073c686be843d3e4/.github/workflows/workflow.yml) |

<a id="ux-rrweb"></a>

### rrweb

| Thuộc tính | Giá trị |
|---|---|
| Repo | https://github.com/rrweb-io/rrweb |
| License | MIT (Contributors của rrweb) |
| Phiên bản đã đọc | `d6926830927706b96d6c018d77d40a945c187342` (commit 2026-11-15) |
| Kiểm chứng | 2026-11-23; code-read; đã đọc README.md, LICENSE, guide.md, CONTEXT.md, docs/adr/0001-require-sandboxed-browser-rebuilds.md, docs/design/index.md, packages/rrweb/src/record/index.ts; chưa chạy upstream |
| Mảng UX | đo hành vi: session replay, tái hiện tương tác để xem vấn đề thật của người dùng |
| Cơ chế đáng học | - Ba lớp: rrweb-snapshot (tuần tự hóa DOM thành cấu trúc có id và dựng lại), record (đột biến + tương tác), replay/rrweb-player (guide.md, docs/design).<br>- Tùy chọn riêng tư: `blockClass` (thay bằng khối giữ kích thước), `ignoreClass`, `maskTextClass`, `maskInputOptions` (mặc định chỉ `{ password: true }`), `maskAllInputs` mặc định false (guide.md; xác nhận ở packages/rrweb/src/record/index.ts).<br>- Mô hình bảo mật replay: dữ liệu replay coi là không tin cậy, `rebuild()` từ chối tài liệu không được sandbox theo mặc định, an toàn dựa vào iframe sandbox chứ không lọc DOM (CONTEXT.md, ADR 0001).<br>- Hệ plugin console/network và tùy chọn checkout để giữ N sự kiện cuối quanh lỗi. |
| Tiêu chí và cách đo | Không có rubric UX; đây là lớp thu thập dữ liệu, không diễn giải. Có bộ test lớn (packages/rrweb/test gồm integration, record, replay, benchmark) và workflow ci-cd.yml chạy test với Chromium và WebKit; tôi chỉ grep các bước run, chưa đọc trọn workflow và chưa chạy gì. |
| Giới hạn và rủi ro | Mặc định riêng tư yếu: chỉ mật khẩu được che; văn bản trang và nhiều input được ghi, nên PII lọt vào bản ghi nếu không cấu hình `maskTextSelector`/`maskAllInputs`. Nội dung ghi là DOM của người dùng thật, cần đồng ý và chính sách lưu trữ. README quảng bá rrweb cloud (dịch vụ thương mại) và roadmap "token efficient AI session replay format" mới là kế hoạch (chưa xác minh).<br>Không có phân tích sẵn (heatmap, phễu, phát hiện rage-click): phải tự xây. Replay bản ghi không tin cậy vô hiệu hóa script nên có thể không giống hệt trang gốc. |
| So với | openreplay (nền tảng replay tự host hoàn chỉnh); posthog (analytics có replay); retentioneering (phân tích đường đi từ nhật ký sự kiện) |
| Nguồn | [README.md](https://github.com/rrweb-io/rrweb/blob/d6926830927706b96d6c018d77d40a945c187342/README.md) · [LICENSE](https://github.com/rrweb-io/rrweb/blob/d6926830927706b96d6c018d77d40a945c187342/LICENSE) · [guide.md](https://github.com/rrweb-io/rrweb/blob/d6926830927706b96d6c018d77d40a945c187342/guide.md) · [CONTEXT.md](https://github.com/rrweb-io/rrweb/blob/d6926830927706b96d6c018d77d40a945c187342/CONTEXT.md) · [0001-require-sandboxed-browser-rebuilds.md](https://github.com/rrweb-io/rrweb/blob/d6926830927706b96d6c018d77d40a945c187342/docs/adr/0001-require-sandboxed-browser-rebuilds.md) · [index.md](https://github.com/rrweb-io/rrweb/blob/d6926830927706b96d6c018d77d40a945c187342/docs/design/index.md) · [index.ts](https://github.com/rrweb-io/rrweb/blob/d6926830927706b96d6c018d77d40a945c187342/packages/rrweb/src/record/index.ts) |

<a id="ux-wireflow"></a>

### Wireflow

| Thuộc tính | Giá trị |
|---|---|
| Repo | https://github.com/vanila-io/wireflow |
| License | MIT (Copyright 2017–2019 The Vanila Team; README nói đây là bản dựng lại của wireflow.co) |
| Phiên bản đã đọc | `8080d2ffed17b4119f505699fb53cd1375da3fec` (commit 2026-11-18) |
| Kiểm chứng | 2026-11-23; code-read; đã đọc README.md, LICENSE, AGENTS.md, lib/ai/prompt.ts, lib/ai/key-crypto.ts, lib/diagram/rules.ts, lib/env.ts, app/layout.tsx; chưa chạy upstream |
| Mảng UX | vẽ luồng người dùng/wireflow, sơ đồ màn hình, ước lượng khối lượng; không mô phỏng hay đo |
| Cơ chế đáng học | - `lib/ai/prompt.ts`: system prompt ổn định (để cache), sơ đồ đi kèm từng tin nhắn dưới thẻ `<diagram>`, bắt buộc dùng id mẫu trong catalog, "never invent one", luật bố cục (mũi tên ra đáy và vào đỉnh nên luồng đọc từ trên xuống, cách nhau khoảng 300px).<br>- `lib/diagram/rules.ts` (`enforceRules`): mọi ghi, đọc từ lưu trữ hoặc file đều qua một biên: id duy nhất, cạnh nối hai nút tồn tại, nhóm không chứa chính nó, chỉ giữ trường biết trước (chặn `__proto__`), trả số mục bị bỏ.<br>- `lib/ai/key-crypto.ts`: khóa API mã hóa AES-GCM bằng khóa thiết bị WebCrypto không xuất được, lưu IndexedDB; tác giả nêu rõ nó không chống được mã chạy trong trang hay extension.<br>- Lỗi của công cụ AI trả về sơ đồ mới để model tự sửa lô thay đổi (prompt.ts). |
| Tiêu chí và cách đo | Không có tiêu chí UX; chỉ có luật cấu trúc sơ đồ kiểm bằng mã. Có vitest (tests/unit, gồm ai-diagram, rules) và 24 spec Playwright e2e trong e2e/; chưa chạy. Repo không có thư mục .github/workflows nên không thấy CI. |
| Giới hạn và rủi ro | Sơ đồ chỉ là ảnh mẫu, nhãn và mũi tên: không có trạng thái, nhánh điều kiện, trạng thái lỗi/rỗng hay kiểm accessibility; không import/export chuẩn ngoài JSON riêng và ảnh. Lưu tối đa ~5MB theo localStorage, ảnh riêng nằm trong file.<br>Trợ lý AI gọi thẳng api.anthropic.com từ trình duyệt bằng `dangerouslyAllowBrowser: true` với khóa người dùng, gửi nhãn, vị trí, ghi chú và ước lượng (không gửi ảnh riêng); khóa nhớ mặc định trên thiết bị, lịch sử chat lưu không mã hóa (README). **Analytics:** README nói "Analytics load only when configured", nhưng `lib/env.ts` cho `rybbitScript()` rơi về `DEFAULT_RYBBIT` (rybbit-d367d4.automatio.run) và `app/layout.tsx` luôn chèn thẻ script đó; AGENTS.md cũng nêu đây là property mặc định của site. Đọc mã, chưa chạy để thấy yêu cầu mạng. |
| So với | excalidraw và tldraw (canvas vẽ tự do, không có mẫu wireframe), drawio-desktop (sơ đồ tổng quát), xyflow (thư viện nền), diagram-design (skill vẽ sơ đồ cho agent) |
| Nguồn | [README.md](https://github.com/vanila-io/wireflow/blob/8080d2ffed17b4119f505699fb53cd1375da3fec/README.md) · [LICENSE](https://github.com/vanila-io/wireflow/blob/8080d2ffed17b4119f505699fb53cd1375da3fec/LICENSE) · [AGENTS.md](https://github.com/vanila-io/wireflow/blob/8080d2ffed17b4119f505699fb53cd1375da3fec/AGENTS.md) · [prompt.ts](https://github.com/vanila-io/wireflow/blob/8080d2ffed17b4119f505699fb53cd1375da3fec/lib/ai/prompt.ts) · [key-crypto.ts](https://github.com/vanila-io/wireflow/blob/8080d2ffed17b4119f505699fb53cd1375da3fec/lib/ai/key-crypto.ts) · [rules.ts](https://github.com/vanila-io/wireflow/blob/8080d2ffed17b4119f505699fb53cd1375da3fec/lib/diagram/rules.ts) · [env.ts](https://github.com/vanila-io/wireflow/blob/8080d2ffed17b4119f505699fb53cd1375da3fec/lib/env.ts) · [layout.tsx](https://github.com/vanila-io/wireflow/blob/8080d2ffed17b4119f505699fb53cd1375da3fec/app/layout.tsx) |

<a id="ux-oneredoak-design-review"></a>

### OneRedOak claude-code-workflows (design-review)

| Thuộc tính | Giá trị |
|---|---|
| Repo | https://github.com/OneRedOak/claude-code-workflows |
| License | MIT (Copyright 2025 Patrick Ellis) |
| Phiên bản đã đọc | `29a34c725313c7621f426f838ed31cf482473fb4` (commit 2026-10-08) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc LICENSE, README.md, design-review/README.md, design-review/design-review-agent.md, design-review/design-review-slash-command.md, design-review/design-review-claude-md-snippet.md, design-review/design-principles-example.md, guides/orchestration-layer/templates/review-triage.md, code-review/claude-code-review.yml; chưa chạy upstream |
| Mảng UX | design review bằng trình duyệt thật (Playwright MCP), responsive, a11y WCAG 2.1 AA, triage mức nghiêm trọng |
| Cơ chế đáng học | - `design-review/design-review-agent.md`: subagent 8 pha (Phase 0 chuẩn bị, 1 luồng tương tác, 2 responsive 1440/768/375, 3 visual polish, 4 a11y, 5 robustness, 6 code health, 7 nội dung và console); nguyên tắc "Live Environment First": trải nghiệm chạy thật trước, đọc code sau.<br>- `design-review-agent.md` mục Communication Principles: "Problems Over Prescriptions" (mô tả vấn đề và tác động, không ra lệnh sửa pixel), mọi phát hiện kèm ảnh chụp, mở đầu bằng điều làm tốt; ma trận [Blocker]/[High-Priority]/[Medium-Priority]/[Nitpick] (nit gắn tiền tố "Nit:").<br>- `design-review-slash-command.md` nhúng `git status/diff/log` bằng cú pháp `!` làm ngữ cảnh rồi ép phản hồi cuối chỉ là báo cáo markdown; `design-review-claude-md-snippet.md` thêm vòng "Quick Visual Check" ngay sau khi sửa front-end (chụp full page 1440px + đọc console) và chỉ gọi agent đầy đủ cho thay đổi lớn.<br>- `guides/orchestration-layer/templates/review-triage.md` (phần review code, không riêng UI): bảng độ tin cậy theo nguồn phát hiện + quyết định Act/Skip có hồi đáp/Skip không hồi đáp, ghi manifest mọi quyết định kể cả bỏ qua; mẫu đáng mượn để xử lý phát hiện không chắc chắn. |
| Tiêu chí và cách đo | Không có rubric điểm số hay ngưỡng chạy máy: tiêu chí là danh sách việc cần kiểm trong prompt và checklist `design-principles-example.md` (kiểu "S-Tier SaaS dashboard"; ngưỡng duy nhất nêu rõ là tương phản 4,5:1 và line-height 1,5-1,7 ở dạng gợi ý). Mức nghiêm trọng do model gán, không có hiệu chuẩn; không có eval, test hay fixture. Không có cơ chế riêng cho kết quả không nhất quán giữa các lần chạy (không lặp, không biểu quyết, không baseline ảnh); chỉ có mẫu triage review code ở `review-triage.md`. |
| Giới hạn và rủi ro | Cần preview chạy được và Playwright MCP (agent khai báo cả Edit/Write/Bash nên không read-only, khác agent chỉ-đọc). `model: sonnet` cố định trong frontmatter. Slash command tham chiếu `../context/design-principles.md` và `style-guide.md` không có trong repo (người dùng phải tự tạo). Checklist mẫu thiên về SaaS dashboard kiểu Stripe/Linear nên khó dùng nguyên cho thể loại khác. Tuyên bố "world-class", "objective" là của tác giả **(chưa xác minh)**; không thấy dữ liệu hiệu quả. Ảnh chụp và diff đi qua nhà cung cấp model của người dùng. |
| So với | taste-skill (cũng chụp 3 viewport nhưng có inspector đo bằng máy); evondevkit-ui-ux (probe Playwright đo tràn/cắt chữ/tương phản); gstack (/plan-design-review chấm 0-10) |
| Nguồn | [LICENSE](https://github.com/OneRedOak/claude-code-workflows/blob/29a34c725313c7621f426f838ed31cf482473fb4/LICENSE) · [README](https://github.com/OneRedOak/claude-code-workflows/blob/29a34c725313c7621f426f838ed31cf482473fb4/README.md) · [Design-review README](https://github.com/OneRedOak/claude-code-workflows/blob/29a34c725313c7621f426f838ed31cf482473fb4/design-review/README.md) · [Agent design-review](https://github.com/OneRedOak/claude-code-workflows/blob/29a34c725313c7621f426f838ed31cf482473fb4/design-review/design-review-agent.md) · [Slash command](https://github.com/OneRedOak/claude-code-workflows/blob/29a34c725313c7621f426f838ed31cf482473fb4/design-review/design-review-slash-command.md) · [Snippet CLAUDE.md](https://github.com/OneRedOak/claude-code-workflows/blob/29a34c725313c7621f426f838ed31cf482473fb4/design-review/design-review-claude-md-snippet.md) · [Nguyên tắc mẫu](https://github.com/OneRedOak/claude-code-workflows/blob/29a34c725313c7621f426f838ed31cf482473fb4/design-review/design-principles-example.md) · [Triage mẫu](https://github.com/OneRedOak/claude-code-workflows/blob/29a34c725313c7621f426f838ed31cf482473fb4/guides/orchestration-layer/templates/review-triage.md) · [Workflow code-review (chỉ để đối chiếu: không có workflow design-review)](https://github.com/OneRedOak/claude-code-workflows/blob/29a34c725313c7621f426f838ed31cf482473fb4/code-review/claude-code-review.yml) |

<a id="ux-happyhands"></a>

### HappyHands

| Thuộc tính | Giá trị |
|---|---|
| Repo | https://github.com/ShuaiMXu/happyhands |
| License | MIT (Copyright 2026 HappyHands contributors; kèm vendor MIT/Apache-2.0 trong THIRD_PARTY_NOTICES.md) |
| Phiên bản đã đọc | `b5feef42df4a7fc12845e019d2fd564e0a413673` (commit 2026-11-23) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc LICENSE, README.md, AGENTS.md, THIRD_PARTY_NOTICES.md, docs/finding-admission-policy.md, docs/skill-regression-gates.md, docs/review-outcomes-and-cost.md, docs/counter-evidence-review-2026-10-21.md, skills/review-product/SKILL.md, examples/capture-plan.example.json, diagnosis.schema.json, regression/cases.json, .github/workflows/checks.yml; chưa chạy upstream |
| Mảng UX | design review có bằng chứng (chụp nhiều breakpoint, diagnose, repair, review độc lập), quality gate cho agent |
| Cơ chế đáng học | - `docs/finding-admission-policy.md` + `diagnosis.schema.json`: lỗi chỉ vào danh sách chính thức khi có `findingBasis` gồm observed/expected/whyWrong/reproduction/alternativesChecked/skillRefs; category chỉ gồm functional, accessibility, layout-break, explicit-contract; Harness kiểm đoạn trích/dòng/chương của skill được dẫn; ý kiến thẩm mỹ, đoán mò và "model tự tin cao" không đủ.<br>- `examples/capture-plan.example.json`: kế hoạch chụp khai báo `configurations` (desktop 1280x800, phone 390x844) x `states` (có `actions` như click/wait-for); ảnh gốc được băm và gắn với nguồn, so sánh trước/sau chỉ chạy khi ảnh khớp cấu hình/trạng thái (`skills/review-product/SKILL.md`).<br>- `docs/review-outcomes-and-cost.md`: mỗi lần gọi model đặt chỗ/ghi sổ dưới khóa run, trần `--max-model-calls`, `--max-total-calls`, ngưỡng token quan sát; kết quả batch thô lưu bất biến theo hash để `--resume-review` không "rút thăm lại" (reroll) trả phí; thiếu usage thì tính là unknown, không phải 0; lỗi mơ hồ phải đối soát bằng biên nhận.<br>- `docs/counter-evidence-review-2026-10-21.md`: khi model báo fail nhưng có phản chứng (ảnh thao tác + số đo), người nộp bằng chứng mới gắn với ảnh gốc để yêu cầu tái duyệt; báo cáo cũ giữ nguyên byte trong chuỗi cha, review mới phải trả lời từng finding cũ, không đủ bằng chứng thì không được pass. |
| Tiêu chí và cách đo | Phần tất định có kiểm bằng máy: `regression/cases.json` (28 ca tổng hợp ở commit này, docs/skill-regression-gates.md vẫn ghi 14 ca nên tài liệu lệch file: 23 ca skill, 4 ca score, 1 ca priority; phủ phát hiện, ưu tiên, kế hoạch sửa, visual QA, hiệu chuẩn điểm, pattern/state/brand) chạy bằng `pnpm regression` với so baseline giữa các báo cáo; ca đổi hợp đồng hoặc đầu ra bị chặn để rà. Điểm Experience Score chỉ do rubric evaluator có phiên bản tính (kiểm dimension/weight/phủ bằng chứng), không do model tự đặt. Mức nghiêm trọng là điểm ưu tiên số (impact, confidence, effort) và việc có `supported` do người xác nhận vẫn xếp trước phép tính. Chất lượng chẩn đoán của model KHÔNG có eval: tài liệu tự nói báo cáo ghi "model review was not run" và các mục còn mở (so sánh đa model, review `claude-code` thật, gọi API thật). CI `checks.yml` đã mở: Ubuntu + Windows x Node 22/24 chạy `test:unit` + `regression`; test trình duyệt không chạy trên CI. |
| Giới hạn và rủi ro | Cài skill qua tgz release (`npx --package=<URL tgz> happyhands install`), cần Node 22.15+, Git, Chrome/Edge và tài khoản model; bước nhìn ảnh gửi mã nguồn chọn lọc và ảnh lên dịch vụ model đã cấu hình (README nói rõ). Worktree chỉ là biện pháp quy trình, không phải sandbox bảo mật (tác giả). Nhiều tài liệu và quy tắc nội bộ viết tiếng Trung, quy tắc UI của HappyHands không áp cho dự án bị review. Số liệu xác minh "đã chạy trên macOS/Chrome/Codex, cài lạnh Windows" là tuyên bố của tác giả **(chưa xác minh)**. Phụ thuộc skill vendor (OJO MIT, Taste MIT, Impeccable Apache-2.0) được nhúng nên cần giữ NOTICE khi mượn. Mức độ phức tạp cao: chỉ nên mượn từng cơ chế (admission policy, ledger chi phí), không mang cả harness. |
| So với | taste-skill và evondevkit-ui-ux (probe/inspector đo ở nhiều viewport); argos (so ảnh PR); gstack (/qa trình duyệt thật, /plan-design-review) |
| Nguồn | [LICENSE](https://github.com/ShuaiMXu/happyhands/blob/b5feef42df4a7fc12845e019d2fd564e0a413673/LICENSE) · [README](https://github.com/ShuaiMXu/happyhands/blob/b5feef42df4a7fc12845e019d2fd564e0a413673/README.md) · [AGENTS.md](https://github.com/ShuaiMXu/happyhands/blob/b5feef42df4a7fc12845e019d2fd564e0a413673/AGENTS.md) · [Third-party notices](https://github.com/ShuaiMXu/happyhands/blob/b5feef42df4a7fc12845e019d2fd564e0a413673/THIRD_PARTY_NOTICES.md) · [Finding admission policy](https://github.com/ShuaiMXu/happyhands/blob/b5feef42df4a7fc12845e019d2fd564e0a413673/docs/finding-admission-policy.md) · [Skill regression gates](https://github.com/ShuaiMXu/happyhands/blob/b5feef42df4a7fc12845e019d2fd564e0a413673/docs/skill-regression-gates.md) · [Review outcomes and cost](https://github.com/ShuaiMXu/happyhands/blob/b5feef42df4a7fc12845e019d2fd564e0a413673/docs/review-outcomes-and-cost.md) · [Counter-evidence review](https://github.com/ShuaiMXu/happyhands/blob/b5feef42df4a7fc12845e019d2fd564e0a413673/docs/counter-evidence-review-2026-10-21.md) · [review-product SKILL.md](https://github.com/ShuaiMXu/happyhands/blob/b5feef42df4a7fc12845e019d2fd564e0a413673/skills/review-product/SKILL.md) · [Mẫu kế hoạch chụp](https://github.com/ShuaiMXu/happyhands/blob/b5feef42df4a7fc12845e019d2fd564e0a413673/examples/capture-plan.example.json) · [diagnosis.schema.json](https://github.com/ShuaiMXu/happyhands/blob/b5feef42df4a7fc12845e019d2fd564e0a413673/diagnosis.schema.json) · [regression/cases.json](https://github.com/ShuaiMXu/happyhands/blob/b5feef42df4a7fc12845e019d2fd564e0a413673/regression/cases.json) · [Workflow checks.yml](https://github.com/ShuaiMXu/happyhands/blob/b5feef42df4a7fc12845e019d2fd564e0a413673/.github/workflows/checks.yml) |

<a id="ux-julianoczkowski-designer-skills"></a>

### Designer Skills (Julian Oczkowski)

| Thuộc tính | Giá trị |
|---|---|
| Repo | https://github.com/julianoczkowski/designer-skills |
| License | Apache-2.0 (Copyright 2026 Julian Oczkowski) |
| Phiên bản đã đọc | `c259656c76d9758d7ead46b0d2f125cbe84f8665` (commit 2026-07-06) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc LICENSE, README.md, SECURITY.md, design-review/SKILL.md, .claude-plugin/plugin.json; chưa chạy upstream |
| Mảng UX | design review dựa trên brief, chụp responsive, quy trình thiết kế từ brief tới review |
| Cơ chế đáng học | - `design-review/SKILL.md` Bước 3 là "bắt buộc, không được bỏ": thứ tự công cụ Playwright MCP, rồi Cursor IDE Browser, rồi (cuối cùng) hỏi người dùng đưa ảnh 1280/768/375 + dark mode, và không được làm review tiếp khi chưa có ảnh.<br>- Quy ước lưu trữ: `.design/<feature-slug>/screenshots/review-<page>-<state>-<width>.png` cạnh `DESIGN_BRIEF.md`, báo cáo trích dẫn tên ảnh để truy vết; chụp `fullPage: true`, thêm trạng thái hover/focus/lỗi/empty và dark mode.<br>- Review đối chiếu với `DESIGN_BRIEF.md` (triết lý thẩm mỹ đã chọn) thay vì tiêu chuẩn chung; checklist 9 nhóm (hierarchy, consistency, aesthetic fidelity, component, states, responsive, a11y, typography, dark mode, mobile-first) và mục "What Works Well" bắt buộc trong mẫu báo cáo.<br>- Có `design-flow` điều phối chuỗi skill với vòng lặp iterate về grill-me; chỉ chạy review khi người dùng yêu cầu, không tự động. |
| Tiêu chí và cách đo | Rubric chỉ định tính: tương phản AA 4,5:1 / 3:1, vùng chạm tối thiểu 44x44px, dòng 45-75 ký tự, body mobile >= 16px, line-height 1,4-1,6; không kiểm bằng máy, không có điểm số. Mức nghiêm trọng 3 bậc Must fix/Should fix/Could improve do model gán, định nghĩa một dòng mỗi bậc. Không có eval, fixture, CI (không có thư mục .github). Không có cơ chế cho kết quả không nhất quán giữa các lần chạy. |
| Giới hạn và rủi ro | Plugin cài từ nhánh main nên luôn theo commit mới nhất, không ghim bản (README ghi "Installs track the latest commit on main"). Không có kiểm tra nào cho việc model thật sự chụp đủ viewport; ép bằng văn bản "CRITICAL". Dùng cùng tên `designer-skills` với repo Owl-Listener đã có trong kho nên dễ nhầm id/catalog. SECURITY.md chỉ là quy trình báo lỗi. Tên công cụ MCP (`plugin-playwright-playwright`) phụ thuộc môi trường. |
| So với | designer-skills (Owl-Listener, cùng tên khác repo); ui-ux của evondevKit (brief rồi wireframe, có probe đo); taste-skill |
| Nguồn | [LICENSE](https://github.com/julianoczkowski/designer-skills/blob/c259656c76d9758d7ead46b0d2f125cbe84f8665/LICENSE) · [README](https://github.com/julianoczkowski/designer-skills/blob/c259656c76d9758d7ead46b0d2f125cbe84f8665/README.md) · [SECURITY.md](https://github.com/julianoczkowski/designer-skills/blob/c259656c76d9758d7ead46b0d2f125cbe84f8665/SECURITY.md) · [design-review/SKILL.md](https://github.com/julianoczkowski/designer-skills/blob/c259656c76d9758d7ead46b0d2f125cbe84f8665/design-review/SKILL.md) · [plugin.json](https://github.com/julianoczkowski/designer-skills/blob/c259656c76d9758d7ead46b0d2f125cbe84f8665/.claude-plugin/plugin.json) |

<a id="ux-ui-craft"></a>

### UI Craft

| Thuộc tính | Giá trị |
|---|---|
| Repo | https://github.com/educlopez/ui-craft |
| License | MIT (Copyright 2026 Eduardo Calvo) |
| Phiên bản đã đọc | `c1e556ed843b5aad057678f9a152fbcf756eb62c` (commit 2026-11-16) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc LICENSE, README.md, PRIVACY.md, commands/critique.md, commands/heuristic.md, agents/design-reviewer.md, skills/ui-craft/SKILL.md, skills/ui-craft/references/heuristics.md, evals/README.md, hooks/hooks.json, .github/workflows/validate.yml; chưa chạy upstream |
| Mảng UX | critique/audit giao diện, chấm điểm heuristic, anti-slop, enforce bằng gate tất định |
| Cơ chế đáng học | - `commands/critique.md` Bước 0 bắt buộc chụp trước khi review: Playwright MCP full-page ở 1280x800, 768x1024, 375x812 (+dark mode), rồi DevTools/Chrome MCP, rồi browser khác, cuối cùng hỏi người dùng; nếu người dùng từ chối ảnh thì chạy "code-only" và phải ghi nhãn `[CODE-ONLY REVIEW - visual issues not assessed]` ở đầu báo cáo.<br>- `agents/design-reviewer.md`: agent đối nghịch chỉ đọc (tools chỉ Read/Grep/Glob) chạy song song với `a11y-auditor`, trả bảng Critical/Warning/Suggestion kèm `file:line`; "nếu sạch thì trả bảng rỗng, không bịa phát hiện"; yêu cầu sửa bị từ chối và ghi thành finding Critical.<br>- `commands/critique.md` + `skills/ui-craft/SKILL.md`: ngưỡng gắn cờ theo knob CRAFT_LEVEL (3 chỉ Critical của anti-slop; 5-7 Critical+Major; 9+ mọi thứ kể cả Minor), kết thúc bằng Craft Report (Checked/Passed/Changed/Left alone/Verdict).<br>- `evals/README.md`: UICraftScore = 100 - 8 x critical - 4 x major - 1 x warn (anti_slop) - 2 x finding (token) - 8/4 (a11y), clamp 0-100, hạng A>=90..F<60; baselines theo dải điểm cho fixture slop/designer cộng bất biến tách `min(designer) > max(slop)`. |
| Tiêu chí và cách đo | Hai thang tách bạch. Tất định: `scripts/eval.mjs` + `evals/quality/*` (công thức ở trên, 5 luật a11y tĩnh bằng regex, baseline dải điểm, exit code 0/1/2), có test node:test; CI `validate.yml` (đã mở) chạy `pnpm verify` trên Ubuntu/Node 20 cộng Go và MCP. Do model chấm: `/heuristic` chấm Nielsen 10 mục thang 1-5 (1 chặn người dùng ... 5 tốt nhất), 6 luật thiết kế PASS/FAIL, UsabilityScore = round(((mean-1)/4) x 100) - 5 x số luật trượt, tối đa 5 phát hiện xếp theo impact `blocks-conversion > adds-friction > reduces-trust > minor-polish`; luôn nhãn judged, không được gate CI, không lấy trung bình với điểm tất định. Eval mô tả (description optimizer, craft-quality prompts) là thủ công hoặc ngoài CI. Chưa mở mã `score.mjs`/`detect.mjs`. |
| Giới hạn và rủi ro | Cài bằng `curl ... \| bash` hoặc `irm ... \| iex` từ ui-craft.smoothui.dev (có kiểm checksum theo README) và hook PostToolUse chạy `detect.mjs hook-run` sau mỗi Edit/Write, nên cần rà trước khi bật. PRIVACY.md: không backend lưu dữ liệu, nhưng `npx` MCP kéo gói từ npm; detector có chế độ quét URL (puppeteer/fetch). Dải baseline +-10 điểm "để hấp thụ đổi trọng số" nghĩa là điểm không so được giữa phiên bản luật. Anti-slop "purple gradient, bounce easing, glassmorphism" là quan điểm thẩm mỹ của tác giả, không phải chuẩn **(chưa xác minh)**. Không có thử nghiệm độ lặp lại của điểm judged giữa các lần chạy. |
| So với | antislop (38 luật chống AI slop); hallmark (sloplint gate 90, render Puppeteer); web-quality-skills; taste-skill |
| Nguồn | [LICENSE](https://github.com/educlopez/ui-craft/blob/c1e556ed843b5aad057678f9a152fbcf756eb62c/LICENSE) · [README](https://github.com/educlopez/ui-craft/blob/c1e556ed843b5aad057678f9a152fbcf756eb62c/README.md) · [PRIVACY.md](https://github.com/educlopez/ui-craft/blob/c1e556ed843b5aad057678f9a152fbcf756eb62c/PRIVACY.md) · [/critique](https://github.com/educlopez/ui-craft/blob/c1e556ed843b5aad057678f9a152fbcf756eb62c/commands/critique.md) · [/heuristic](https://github.com/educlopez/ui-craft/blob/c1e556ed843b5aad057678f9a152fbcf756eb62c/commands/heuristic.md) · [design-reviewer agent](https://github.com/educlopez/ui-craft/blob/c1e556ed843b5aad057678f9a152fbcf756eb62c/agents/design-reviewer.md) · [SKILL.md](https://github.com/educlopez/ui-craft/blob/c1e556ed843b5aad057678f9a152fbcf756eb62c/skills/ui-craft/SKILL.md) · [heuristics.md](https://github.com/educlopez/ui-craft/blob/c1e556ed843b5aad057678f9a152fbcf756eb62c/skills/ui-craft/references/heuristics.md) · [evals/README](https://github.com/educlopez/ui-craft/blob/c1e556ed843b5aad057678f9a152fbcf756eb62c/evals/README.md) · [hooks.json](https://github.com/educlopez/ui-craft/blob/c1e556ed843b5aad057678f9a152fbcf756eb62c/hooks/hooks.json) · [Workflow validate.yml](https://github.com/educlopez/ui-craft/blob/c1e556ed843b5aad057678f9a152fbcf756eb62c/.github/workflows/validate.yml) |

<a id="ux-shadscan"></a>

### Shadscan

| Thuộc tính | Giá trị |
|---|---|
| Repo | https://github.com/TheOrcDev/shadscan |
| License | MIT (Copyright 2026 TheOrcDev) |
| Phiên bản đã đọc | `dafe99045f444c7cc4981fb17fb6365ef269888b` (commit 2026-09-30) |
| Kiểm chứng | 2026-11-23; code-read; đã đọc LICENSE.md, packages/cli/LICENSE, README.md, AGENTS.md, docs/rules.md, docs/cli-contract.md, docs/web-scanner.md, packages/cli/src/overflow-check/evaluate.ts, packages/cli/src/overflow-check/browser-measure.ts, .github/workflows/quality.yml; chưa chạy upstream |
| Mảng UX | audit giao diện tất định, rubric 62 luật, kiểm tràn ngang đa viewport, handoff cho agent |
| Cơ chế đáng học | - `docs/rules.md` (sinh bằng script, CI `docs:check` bắt lệch): mỗi luật có Confidence (high/medium/low), điểm thô khi áp dụng hoặc Advisory, và adapter áp dụng; luật không áp dụng bị loại khỏi mẫu số; điểm thô chuẩn hóa trong từng hạng mục có trọng số.<br>- `README.md`/`docs/cli-contract.md`: báo cáo tách Fixes (lỗi tin cậy cao có bằng chứng), Decisions (lựa chọn sản phẩm cần làm hoặc ghi miễn trừ), Advisories, Not applicable; `--prompt` xuất kế hoạch sửa dán thẳng cho agent; `--fail-under N` thoát mã khác 0, tìm thấy lỗi không tự làm fail.<br>- `overflow-check/browser-measure.ts` + `evaluate.ts`: hàm đo chạy trong trang (không closure để Playwright serialize), giới hạn số phần tử/culprit, sắp xếp culprit tất định (overflowPx, depth, order, descriptor) và làm sạch ký tự điều khiển; viewport cố định 320x820 và 1440x1000; chỉ cần 1 CSS px tràn là critical, trang trình duyệt cô lập, route thêm tối đa 10.<br>- `docs/cli-contract.md`: quy ước exit code (0 xong, 1 lỗi tràn hoặc lỗi trình duyệt/đối số), JSON báo cáo có phiên bản schema. |
| Tiêu chí và cách đo | Hoàn toàn tất định, không gọi model: điểm = chuẩn hóa điểm luật theo hạng mục (Foundation 20, Interaction 20, States, Accessibility 20, Forms 10, Polish 10 theo ví dụ README). Kiểm tràn ngang là nhị phân (>0px là critical) và không cộng vào điểm/luật. Mức nghiêm trọng thực chất là độ tin cậy luật cộng điểm thô, không phải thang severity UX. Có test CLI/e2e và CI `quality.yml` (đã mở: format, lint, `docs:check`, audit phụ thuộc, typecheck, test CLI và API). Tính nhất quán giữa các lần chạy là thiết kế (thứ tự tất định) nhưng chưa chạy để xác nhận. |
| Giới hạn và rủi ro | Chỉ hiểu mã React/shadcn: không đánh giá thẩm mỹ, thứ bậc, copy; luật như Cmd+K command menu và hotkey đổi theme là quan điểm sản phẩm, nên điểm cao không đồng nghĩa UX tốt (tuyên bố "deterministic UI audit" của tác giả đúng về tính lặp lại chứ không về chất lượng UX). Có dịch vụ hosted /scan quét repo GitHub công khai qua shadscan.com (Neon, rate limit, tùy chọn API), tách khỏi CLI vốn không upload mã. Luôn pin phiên bản CLI trong CI vì lệnh không pin lấy bản mới nhất. Chế độ --check-ui chạy JavaScript của trang đích; --apply có thể khởi chạy agent cài sẵn, cần cân nhắc quyền. Có "roast" mặc định trong báo cáo (tắt bằng --no-roast). |
| So với | axe-core (a11y runtime, luật có `incomplete`); eslint-plugin-jsx-a11y; web-quality-skills; antislop |
| Nguồn | [LICENSE gốc](https://github.com/TheOrcDev/shadscan/blob/dafe99045f444c7cc4981fb17fb6365ef269888b/LICENSE.md) · [LICENSE của packages/cli](https://github.com/TheOrcDev/shadscan/blob/dafe99045f444c7cc4981fb17fb6365ef269888b/packages/cli/LICENSE) · [README](https://github.com/TheOrcDev/shadscan/blob/dafe99045f444c7cc4981fb17fb6365ef269888b/README.md) · [AGENTS.md](https://github.com/TheOrcDev/shadscan/blob/dafe99045f444c7cc4981fb17fb6365ef269888b/AGENTS.md) · [Danh mục luật](https://github.com/TheOrcDev/shadscan/blob/dafe99045f444c7cc4981fb17fb6365ef269888b/docs/rules.md) · [CLI contract](https://github.com/TheOrcDev/shadscan/blob/dafe99045f444c7cc4981fb17fb6365ef269888b/docs/cli-contract.md) · [Web scanner](https://github.com/TheOrcDev/shadscan/blob/dafe99045f444c7cc4981fb17fb6365ef269888b/docs/web-scanner.md) · [evaluate.ts](https://github.com/TheOrcDev/shadscan/blob/dafe99045f444c7cc4981fb17fb6365ef269888b/packages/cli/src/overflow-check/evaluate.ts) · [browser-measure.ts](https://github.com/TheOrcDev/shadscan/blob/dafe99045f444c7cc4981fb17fb6365ef269888b/packages/cli/src/overflow-check/browser-measure.ts) · [Workflow quality.yml](https://github.com/TheOrcDev/shadscan/blob/dafe99045f444c7cc4981fb17fb6365ef269888b/.github/workflows/quality.yml) |

<a id="ux-squirrelscan"></a>

### squirrelscan

| Thuộc tính | Giá trị |
|---|---|
| Repo | https://github.com/squirrelscan/squirrelscan |
| License | MIT (Copyright 2026 squirrelscan; tên và logo theo TRADEMARKS.md) |
| Phiên bản đã đọc | `1892d157092f40505b00bd86e80f30c8a939bf08` (commit 2026-11-24) |
| Kiểm chứng | 2026-11-23; code-read; đã đọc LICENSE, README.md, TRADEMARKS.md, docs/guides/read-your-report.mdx, docs/guides/ci.mdx, docs/faq.mdx, packages/rules/src/content/color-sprawl.ts, benchmarks/2026-11-component-findings-eval.md, .github/workflows/ci.yml; chưa chạy upstream |
| Mảng UX | audit site toàn cục (nhất quán, a11y, mobile, hiệu năng), điểm và xếp hạng sửa cho agent |
| Cơ chế đáng học | - `packages/rules/src/content/color-sprawl.ts`: thu mọi literal màu từ `<style>`/`style=`, quy sang OKLab, gom cụm theo khoảng cách 0,02 (xấp xỉ một JND); cụm có nhiều literal là trùng lặp gần giống, màu chỉ một trang dùng là outlier; vế phải của `--token: màu` không tính (đó là định nghĩa thang); ngưỡng sàn (>=10 trang, >=5 trang có màu, tối đa 6 màu thừa) để không phán khi thiếu chuẩn của site.<br>- `docs/guides/read-your-report.mdx`: điểm 0-100 có hạng A>=90..F<60, trọng số theo luật, luật bị bỏ qua không tính; issue gắn severity (critical/high/medium/low) và effort (Quick win/Moderate/Significant); báo cáo nói rõ phần không kiểm (vd 912/1412 link ngoài chưa kiểm).<br>- `docs/guides/ci.mdx`: cổng `--fail-on "score<90,severity>=error,score:perf<80"`; build không fail vì điểm tụt so với lần trước mà chỉ theo ngưỡng tuyệt đối.<br>- `benchmarks/2026-11-component-findings-eval.md`: eval trước/sau trên 14 site tổng hợp (60 trang) với nhãn tay, đo "incorrect merges" và "missed merges", ghi rõ không replay DOM lịch sử nên không khẳng định gì cho corpus thật. |
| Tiêu chí và cách đo | Tất định: điểm và nhóm điểm là trọng số của check đã chạy; ngưỡng CI do người dùng đặt bằng `--fail-on`. Mức severity có trong báo cáo nhưng một số issue chưa có. Có benchmark/eval nhãn tay cho phần gộp component (số liệu trên fixture tổng hợp, tác giả nói rõ phạm vi) và CI `ci.yml` (đã mở phần đầu: Bun, `NO_TELEMETRY=1`, classify theo đường dẫn); chưa mở mã tính điểm. Không có kiểm ảnh chụp/thị giác. |
| Giới hạn và rủi ro | Telemetry bật mặc định: gửi tên sự kiện, phiên bản CLI, install ID ngẫu nhiên (kèm user ID sau `auth login`), chuyển tiếp PostHog; tắt bằng `NO_TELEMETRY`, `DO_NOT_TRACK=1` hoặc `audit --offline` (docs/faq.mdx). Cài bằng `curl \| bash`, lệnh "dán vào agent" bảo agent tải và làm theo hướng dẫn từ URL ngoài (rủi ro prompt injection nếu nguồn đổi). Tính năng cloud (render trình duyệt, AI summary, MCP hosted) cần đăng nhập, gửi nội dung site và dùng tín dụng; MIT cho phần mã nhưng tên thương hiệu bị hạn chế. Mặc định `respect_robots=false`. "350+ luật" là số liệu của tác giả **(chưa xác minh từng luật)**. Skill agent nằm ở repo riêng squirrelscan/skills, không đọc ở đây. |
| So với | web-quality-skills (audit trước-đo, Lighthouse); axe-core; antislop |
| Nguồn | [LICENSE](https://github.com/squirrelscan/squirrelscan/blob/1892d157092f40505b00bd86e80f30c8a939bf08/LICENSE) · [README](https://github.com/squirrelscan/squirrelscan/blob/1892d157092f40505b00bd86e80f30c8a939bf08/README.md) · [TRADEMARKS.md](https://github.com/squirrelscan/squirrelscan/blob/1892d157092f40505b00bd86e80f30c8a939bf08/TRADEMARKS.md) · [Đọc báo cáo](https://github.com/squirrelscan/squirrelscan/blob/1892d157092f40505b00bd86e80f30c8a939bf08/docs/guides/read-your-report.mdx) · [Hướng dẫn CI](https://github.com/squirrelscan/squirrelscan/blob/1892d157092f40505b00bd86e80f30c8a939bf08/docs/guides/ci.mdx) · [FAQ (telemetry)](https://github.com/squirrelscan/squirrelscan/blob/1892d157092f40505b00bd86e80f30c8a939bf08/docs/faq.mdx) · [color-sprawl.ts](https://github.com/squirrelscan/squirrelscan/blob/1892d157092f40505b00bd86e80f30c8a939bf08/packages/rules/src/content/color-sprawl.ts) · [Benchmark component findings](https://github.com/squirrelscan/squirrelscan/blob/1892d157092f40505b00bd86e80f30c8a939bf08/benchmarks/2026-11-component-findings-eval.md) · [Workflow ci.yml](https://github.com/squirrelscan/squirrelscan/blob/1892d157092f40505b00bd86e80f30c8a939bf08/.github/workflows/ci.yml) |

<a id="ux-mastepanoski-claude-skills"></a>

### mastepanoski claude-skills (UX/UI audit suite)

| Thuộc tính | Giá trị |
|---|---|
| Repo | https://github.com/mastepanoski/claude-skills |
| License | MIT (Copyright 2026 mastepanoski) |
| Phiên bản đã đọc | `ac3023830834f9c7c181649f31fbfd48c91837d3` (commit 2026-10-29) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc LICENSE, README.md, CLAUDE.md, scripts/validate.js, skills/nielsen-heuristics-audit/SKILL.md, skills/ui-design-review/SKILL.md, skills/ui-design-review/references/review-procedure.md, skills/ui-design-review/references/report-template.md, .github/workflows/validate.yml; chưa chạy upstream |
| Mảng UX | đánh giá heuristic (Nielsen, Norman, IDF 7 yếu tố, cognitive walkthrough), accessibility WCAG, review thị giác |
| Cơ chế đáng học | - Mọi `SKILL.md` có mục "Security Notice / Untrusted Input Handling (OWASP LLM01)": bọc input ngoài (`screenshots_or_links`, `known_issues`, `competitive_context`) như `<untrusted-content>`, phát hiện cụm "ignore previous instructions", chỉ rút bằng chứng usability; mẫu đáng chép cho skill nhận ảnh/URL bên ngoài.<br>- `skills/nielsen-heuristics-audit/SKILL.md`: quy trình 4 bước (chuẩn bị, chấm từng heuristic với vị trí/mô tả/ảnh/tác vụ ảnh hưởng, phân tích chéo, báo cáo); severity 0-4 (Not a problem, Cosmetic, Minor, Major, Catastrophic) kèm hành động; ưu tiên = severity x tần suất x tác động tới tác vụ chính; nhắc heuristic evaluation chỉ tìm khoảng 75% vấn đề.<br>- `skills/ui-design-review/`: 10 chiều thị giác chấm 0-10 (tiêu chí/checklist/red flag tách vào `references/` để SKILL.md gọn), ấn tượng đầu 1-10, kiểm kê component, đánh giá design system, so sánh đối thủ; tách tài liệu chi tiết ra references để giảm token nạp.<br>- `scripts/validate.js` (CI): kiểm frontmatter YAML hợp lệ (bắt dấu hai chấm/`#`/ngoặc không đóng làm hỏng `npx skills add`), mô tả <=200 ký tự, kích thước SKILL.md. |
| Tiêu chí và cách đo | Không kiểm bằng máy nội dung đánh giá; chỉ `validate.js` kiểm cấu trúc skill. `npm test` chỉ in "No tests yet" (package.json, đã xem qua grep). Rubric: severity 0-4 (Nielsen) với ví dụ ở bảng; ui-design-review chấm 0-10 mỗi chiều, quy điểm tổng thành hạng A+..F. Mâu thuẫn quan sát được: `review-procedure.md` ghi "Quality rating: 1-5" và đánh giá tổng 3/5, `report-template.md` ghi "Visual Design Score: X/100" nhưng ví dụ lại "4/10", trong khi SKILL.md định nghĩa tổng = trung bình 10 chiều (thang 0-10) nhưng bảng hạng dùng 90-100/80-89 (thang 100). Không có eval, không xử lý kết quả không nhất quán giữa các lần chạy, không có giao thức chụp ảnh (ảnh do người dùng cung cấp hoặc URL). |
| Giới hạn và rủi ro | Thang điểm không thống nhất như trên khiến điểm do model xuất ra không so sánh được giữa lần chạy. Không có cơ chế chụp màn hình hay đo, nên đánh giá thị giác dựa vào ảnh người dùng đưa; phát hiện "không thấy ảnh" có thể bị model bịa. Khẳng định "industry-standard", "battle-tested" là của tác giả **(chưa xác minh)**. Cài bằng `npx skills add` (CLAUDE.md cảnh báo không chạy ở gốc repo vì CLI ghi đè `skills/` bằng symlink). Skill mô phỏng chuyên gia, chính tác giả khuyên xác nhận bằng người dùng thật. Nhóm skill governance/AI security (GDPR, ISO 42001, OWASP) ngoài trọng tâm UX. |
| So với | web-interface-guidelines-vercel (checklist UI cho agent review); antislop; web-quality-skills (a11y WCAG 2.2) |
| Nguồn | [LICENSE](https://github.com/mastepanoski/claude-skills/blob/ac3023830834f9c7c181649f31fbfd48c91837d3/LICENSE) · [README](https://github.com/mastepanoski/claude-skills/blob/ac3023830834f9c7c181649f31fbfd48c91837d3/README.md) · [CLAUDE.md](https://github.com/mastepanoski/claude-skills/blob/ac3023830834f9c7c181649f31fbfd48c91837d3/CLAUDE.md) · [validate.js](https://github.com/mastepanoski/claude-skills/blob/ac3023830834f9c7c181649f31fbfd48c91837d3/scripts/validate.js) · [nielsen-heuristics-audit/SKILL.md](https://github.com/mastepanoski/claude-skills/blob/ac3023830834f9c7c181649f31fbfd48c91837d3/skills/nielsen-heuristics-audit/SKILL.md) · [ui-design-review/SKILL.md](https://github.com/mastepanoski/claude-skills/blob/ac3023830834f9c7c181649f31fbfd48c91837d3/skills/ui-design-review/SKILL.md) · [review-procedure.md](https://github.com/mastepanoski/claude-skills/blob/ac3023830834f9c7c181649f31fbfd48c91837d3/skills/ui-design-review/references/review-procedure.md) · [report-template.md](https://github.com/mastepanoski/claude-skills/blob/ac3023830834f9c7c181649f31fbfd48c91837d3/skills/ui-design-review/references/report-template.md) · [Workflow validate.yml](https://github.com/mastepanoski/claude-skills/blob/ac3023830834f9c7c181649f31fbfd48c91837d3/.github/workflows/validate.yml) |

<a id="ux-ux-skill"></a>

### ux-skill (uxskill)

| Thuộc tính | Giá trị |
|---|---|
| Repo | https://github.com/Laith0003/ux-skill |
| License | MIT (Copyright 2026 Laith Aljunaidy; NOTICE ghi một phần từ taste-skill, MIT) |
| Phiên bản đã đọc | `b0a3aff443776a1e3a08d62a18ca390ec4d451b1` (commit 2026-11-12) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc LICENSE, NOTICE, README.md, PRIVACY.md, commands/ux-polish.md, commands/ux-critique.md, `engine/evaluator/__init__.py`, engine/evaluator/core.py, engine/rulepack/decisions/reflow-at-320.md, data/anti-patterns.json, .github/workflows/test.yml; chưa chạy upstream |
| Mảng UX | design system cho agent, linter/evaluator tất định, vòng polish tự động, critique và audit |
| Cơ chế đáng học | - `commands/ux-polish.md` + `engine/evaluator/`: vòng `uxskill evolve` mỗi lượt chạy linter 0-100 và evaluator 7 trục (linter, hierarchy, layout, spacing, readability, tone, uniqueness), áp 6 bước polish idempotent, rồi dừng khi `target_hit` (điểm 90), `plateau` (delta < 5), `max_rounds` (mặc định 3) hoặc `gate_failed` (< 65, cần `--force` mới ghi); file gốc không bị chạm trừ khi `--fix`/`--loop-only` và cây git sạch.<br>- `data/anti-patterns.json`: 171 mục có `severity`, `detection` (regex/phạm vi), `why`, `fix`; mã Python chạy offline, "no LLM", cùng input cho cùng điểm (tuyên bố trong docstring).<br>- `commands/ux-critique.md` tách hẳn ý kiến thiết kế (tối đa 500 từ, 3 thắng, 3 thua, 1 nước đi chiến lược, cấm severity/WCAG) khỏi `/ux-audit` có severity và `/ux-a11y`; mỗi lệnh có phạm vi và bảng "không dùng khi".<br>- `engine/rulepack/decisions/reflow-at-320.md`: sổ quyết định cho từng luật (context/decision/why/consequences) gắn WCAG 1.4.10 (tầng tablet phải trên 320px, cột phone tối thiểu 44px): mẫu để lưu lý do ngưỡng. |
| Tiêu chí và cách đo | Chủ yếu tất định: linter regex trên HTML/CSS đã parse, evaluator 7 trục (mean các trục, ngưỡng 65 tự chấp nhận, 90 mục tiêu), gate WCAG cho màu (4,5:1 chữ, 3:1 phi văn bản, 7:1 high contrast). Chưa đọc mã cụ thể của từng trục ngoài docstring và đầu `core.py`. CI `test.yml` (đã mở): pytest Python 3.10-3.13, kiểm JSON trong data/, quét emoji. README ghi "13101 tests passing" và "strongest UX plugin": số liệu tự công bố **(chưa xác minh)**. Không có eval người/chất lượng, không có giao thức chụp ảnh nhiều breakpoint ở các lệnh review đã đọc (nhận URL/ảnh/file); phát hiện reflow/ngang chủ yếu qua gate lúc sinh. |
| Giới hạn và rủi ro | Quy mô rất lớn (17 IDE installer, 160 brand spec, 17 ngôn ngữ README) nên khó mượn nguyên; điểm tất định đo phù hợp với "luật của chính engine" chứ không chứng minh UI tốt. Có sự không khớp: PRIVACY.md nói landing page không có analytics và không Google Analytics, nhưng CI buộc mọi `docs/*.html` mang thẻ GA4 (`ensure-ga.py --check`) và `docs/index.html` có gtag G-Z371T0DBW5 (quan sát trong repo; chưa rõ docs/ có phải site đã nói). Plugin tự khẳng định không có telemetry, mạng bằng không **(chưa xác minh)**. Sự phụ thuộc/kế thừa từ taste-skill phải giữ NOTICE. Một số lệnh cho phép Bash(python3/uxskill) và WebFetch. Các lệnh critique mang tính ý kiến, nên không lặp lại được giữa các lần chạy. |
| So với | taste-skill (đồng nguồn dials, inspector đo 3 viewport); antislop; hallmark (gate điểm 90); emilkowalski-skills |
| Nguồn | [LICENSE](https://github.com/Laith0003/ux-skill/blob/b0a3aff443776a1e3a08d62a18ca390ec4d451b1/LICENSE) · [NOTICE](https://github.com/Laith0003/ux-skill/blob/b0a3aff443776a1e3a08d62a18ca390ec4d451b1/NOTICE) · [README](https://github.com/Laith0003/ux-skill/blob/b0a3aff443776a1e3a08d62a18ca390ec4d451b1/README.md) · [PRIVACY.md](https://github.com/Laith0003/ux-skill/blob/b0a3aff443776a1e3a08d62a18ca390ec4d451b1/PRIVACY.md) · [/ux-polish](https://github.com/Laith0003/ux-skill/blob/b0a3aff443776a1e3a08d62a18ca390ec4d451b1/commands/ux-polish.md) · [/ux-critique](https://github.com/Laith0003/ux-skill/blob/b0a3aff443776a1e3a08d62a18ca390ec4d451b1/commands/ux-critique.md) · [evaluator/\_\_init\_\_.py](https://github.com/Laith0003/ux-skill/blob/b0a3aff443776a1e3a08d62a18ca390ec4d451b1/engine/evaluator/__init__.py) · [evaluator/core.py](https://github.com/Laith0003/ux-skill/blob/b0a3aff443776a1e3a08d62a18ca390ec4d451b1/engine/evaluator/core.py) · [reflow-at-320.md](https://github.com/Laith0003/ux-skill/blob/b0a3aff443776a1e3a08d62a18ca390ec4d451b1/engine/rulepack/decisions/reflow-at-320.md) · [anti-patterns.json](https://github.com/Laith0003/ux-skill/blob/b0a3aff443776a1e3a08d62a18ca390ec4d451b1/data/anti-patterns.json) · [Workflow test.yml](https://github.com/Laith0003/ux-skill/blob/b0a3aff443776a1e3a08d62a18ca390ec4d451b1/.github/workflows/test.yml) |

<a id="ux-gnurio-refactoring-ui-plugin"></a>

### Refactoring UI Skills (gnurio)

| Thuộc tính | Giá trị |
|---|---|
| Repo | https://github.com/gnurio/refactoring-ui-plugin |
| License | All rights reserved (Copyright 2026 George Nurijanian); không phải license mở |
| Phiên bản đã đọc | `00781eab1dde7fdb720d63f8d6c8148bf5835a31` (commit 2026-04-27) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc LICENSE, README.md, SKILL.md, skills.json, skills/meta-refactor-ui/SKILL.md, skills/09-manage-color-contrast/SKILL.md, tests/validate-skills.sh, tests/skill-schema.test.js; chưa chạy upstream |
| Mảng UX | đánh giá thị giác theo nguyên tắc sách Refactoring UI, quy trình skill nguyên tử |
| Cơ chế đáng học | - `skills/meta-refactor-ui/SKILL.md`: orchestrator 4 pha (nạp `skills.json`, chạy tuần tự 10 skill, gom FAIL theo severity Critical/High/Medium/Low và khử trùng, xuất JSON `overall_score: PASS \| NEEDS_WORK \| FAIL` + `violations` + `priority_fixes` + `skill_breakdown`); hai chế độ Quick Scan (chỉ FAIL) và Deep Analysis.<br>- Mỗi `skills/NN-*/SKILL.md` có khung cố định: Purpose, Type, Input/Output, Decision Criteria PASS/FAIL, Common Failure Modes, Prerequisites/Dependencies, ví dụ đánh giá (xem `09-manage-color-contrast/SKILL.md`).<br>- `skills.json` làm registry có `prerequisites`, `dependencies`, `test_cases`; `tests/skill-schema.test.js` và `validate-skills.sh` kiểm schema và sự tồn tại thư mục.<br>- Adapter `adapters/platform-adapter.js` (chỉ xem phần đầu) phát hiện nền tảng Claude/Codex/Cursor qua biến môi trường để map tên công cụ. |
| Tiêu chí và cách đo | Tiêu chí là ngưỡng con số trong từng skill (ví dụ contrast 4,5:1 chữ thường, 3:1 chữ lớn/UI, focus 3:1). Kiểm bằng máy chỉ ở mức cấu trúc skill (schema, thư mục), không chấm nội dung. `skills.json` tuyên bố "expert_agreement 97%", "cases_validated 29", `last_validated 2024-04-26` với nguồn "NotebookLM": số liệu tự công bố, không có dữ liệu kèm theo **(chưa xác minh)**; ngày 2024 cũng đi trước ngày repo (2026). Lỗi dữ kiện nhỏ: skill contrast ghi #666666 là 5,9:1 còn tính lại được 5,74:1 (các ví dụ khác như #757575 = 4,61:1 và #888 = 3,54:1 đúng). Không có CI, không có eval, không xử lý nhất quán giữa các lần chạy. |
| Giới hạn và rủi ro | LICENSE "All rights reserved" ngăn sao chép, sửa hay phân phối lại; chỉ có thể tham khảo ý tưởng, không nhúng nội dung. `skills.json` trỏ tới các file `references/*.md` không tồn tại trong cây (không thấy thư mục references nào), nên các tham chiếu bị treo. Chỉ 1 thư mục ví dụ (visual-hierarchy). Phụ thuộc tên và nội dung sách Refactoring UI (bản quyền Tailwind Labs) mà không có điều khoản giới hạn như hồ sơ s0xDk. Đứng một commit 27/4/2026 ở độ sâu clone 1, chưa đánh giá lịch sử. |
| So với | Refactoring UI Skill (s0xDk): MIT kèm điều khoản không bao gồm sách, README + tokens.css (thang spacing/type/màu HSL/bóng, 9 hard rule, bảng chẩn đoán, tương phản đã được tính lại); gnurio khác ở chỗ PASS/FAIL theo 10 skill + orchestrator JSON, không có tokens, license đóng. Kết luận so sánh: mượn cơ chế từ s0xDk (MIT) an toàn hơn; gnurio chỉ đáng tham khảo cách tách skill nguyên tử |
| Nguồn | [LICENSE](https://github.com/gnurio/refactoring-ui-plugin/blob/00781eab1dde7fdb720d63f8d6c8148bf5835a31/LICENSE) · [README](https://github.com/gnurio/refactoring-ui-plugin/blob/00781eab1dde7fdb720d63f8d6c8148bf5835a31/README.md) · [SKILL.md](https://github.com/gnurio/refactoring-ui-plugin/blob/00781eab1dde7fdb720d63f8d6c8148bf5835a31/SKILL.md) · [skills.json](https://github.com/gnurio/refactoring-ui-plugin/blob/00781eab1dde7fdb720d63f8d6c8148bf5835a31/skills.json) · [meta-refactor-ui/SKILL.md](https://github.com/gnurio/refactoring-ui-plugin/blob/00781eab1dde7fdb720d63f8d6c8148bf5835a31/skills/meta-refactor-ui/SKILL.md) · [09-manage-color-contrast/SKILL.md](https://github.com/gnurio/refactoring-ui-plugin/blob/00781eab1dde7fdb720d63f8d6c8148bf5835a31/skills/09-manage-color-contrast/SKILL.md) · [validate-skills.sh](https://github.com/gnurio/refactoring-ui-plugin/blob/00781eab1dde7fdb720d63f8d6c8148bf5835a31/tests/validate-skills.sh) · [skill-schema.test.js](https://github.com/gnurio/refactoring-ui-plugin/blob/00781eab1dde7fdb720d63f8d6c8148bf5835a31/tests/skill-schema.test.js) |

<a id="ux-accessibility-agents-community-access"></a>

### Accessibility Agents (Community-Access)

| Thuộc tính | Giá trị |
|---|---|
| Repo | https://github.com/Community-Access/accessibility-agents |
| License | MIT (LICENSE gốc, © 2026 Taylor Arndt; mỗi SKILL.md khai `license: MIT`; `mcp-server/` có LICENSE riêng, chưa đọc) |
| Phiên bản đã đọc | `a538edc9edfb98cdd8bae96d6b79542874b478f7` (commit 2026-11-07) |
| Kiểm chứng | 2026-11-23; code-read; đã đọc README.md, LICENSE, AGENTS.md, PRIVACY.md, skills/accessibility-lead/SKILL.md, skills/a11y-core/SKILL.md, skills/contrast-master/SKILL.md, hooks/guard.mjs, scripts/audit-recall.mjs, budgets.json, .github/workflows/a11y-pr-gate.yml, .github/workflows/verify.yml, example/README.md; chưa chạy upstream |
| Mảng UX | accessibility (WCAG 2.2 AA) cho code web, tài liệu Office/PDF/ePub, markdown; design system token (`design-system-auditor`) |
| Cơ chế đáng học | - `skills/accessibility-lead/SKILL.md`: router phân loại thay đổi, gọi specialist song song bằng mẫu prompt cố định, bắt trả JSON và từ chối phản hồi dạng văn xuôi; Critical/Serious nghĩa là không ship<br>- `hooks/guard.mjs`: một script cho 5 client (detect/gate/mark/persist/finalize), exit code 2 chặn Edit/Write vào file UI (kể cả `sed -i`, redirect) đến khi lead hoàn tất; tự mô tả là rào chắn, không phải sandbox<br>- `skills/a11y-core/SKILL.md` + `scripts/render-report.mjs`: bảy mục báo cáo bắt buộc (điểm /100, hạng A-F, delta so với lần trước), câu chốt rằng kiểm tự động chỉ thấy một phần rào cản<br>- `scripts/audit-recall.mjs` + `example/index.html`: trang cố tình lỗi có chú thích ISSUE, bỏ chú thích rồi chấm xem audit tìm lại bao nhiêu lỗi (khớp theo gần dòng và từ khóa)<br>- `budgets.json` + `measure-context.mjs`: trần token luôn-bật (README nói khoảng 1.100 token, chưa xác minh) |
| Tiêu chí và cách đo | WCAG 2.2 AA là mặc định (AGENTS.md, README, decision-matrix có 2.4.11, 2.5.8, 3.3.8); `references/sources.md` còn dẫn cả đặc tả WCAG 2.1. Contrast: chữ 4.5:1, chữ lớn 3:1, phi văn bản 3:1 (`contrast-master`, 'bắt buộc'). Máy kiểm được: axe-core, quét Playwright, markdown/Office/PDF scanner qua MCP; còn lại model chấm theo checklist và có trường `confidence` high/medium/low. Báo cáo kết thúc bằng bước 'xác nhận bằng screen reader và bàn phím thủ công', nhưng không có trạng thái 'chưa kiểm' riêng cho từng tiêu chí như bộ của masuP9. Có `audit-recall` (eval một fixture) và `npm run verify`; chưa thấy eval nhiều trang hay so baseline. |
| Giới hạn và rủi ro | Hook chạy `node` tại máy người dùng và có hạn chế đã tự nêu (không thấy đường dẫn tạo từ biến). Tool `glow_*` gửi file đã chọn tới dịch vụ bên thứ ba letitglow.app/mcp (PRIVACY.md). Cổng `a11y-pr-gate.yml` là grep regex (ví dụ `<img` thiếu alt), mới đọc đoạn đầu workflow. PRIVACY.md khẳng định không telemetry (chưa xác minh bằng mã). Kho lớn (746 file), dễ nặng khi mang nguyên gói. 'Verified live' về hook trong guard.mjs chỉ là lời tác giả. |
| So với | axe-core (`axe-core`), eslint-plugin-jsx-a11y (`eslint-plugin-jsx-a11y`), WCAG 2.2 (`wcag-2-2`), a11y-specialist-skills (hồ sơ cùng lô) |
| Nguồn | [README.md](https://github.com/Community-Access/accessibility-agents/blob/a538edc9edfb98cdd8bae96d6b79542874b478f7/README.md) · [LICENSE](https://github.com/Community-Access/accessibility-agents/blob/a538edc9edfb98cdd8bae96d6b79542874b478f7/LICENSE) · [AGENTS.md](https://github.com/Community-Access/accessibility-agents/blob/a538edc9edfb98cdd8bae96d6b79542874b478f7/AGENTS.md) · [PRIVACY.md](https://github.com/Community-Access/accessibility-agents/blob/a538edc9edfb98cdd8bae96d6b79542874b478f7/PRIVACY.md) · [SKILL.md](https://github.com/Community-Access/accessibility-agents/blob/a538edc9edfb98cdd8bae96d6b79542874b478f7/skills/accessibility-lead/SKILL.md) · [SKILL.md](https://github.com/Community-Access/accessibility-agents/blob/a538edc9edfb98cdd8bae96d6b79542874b478f7/skills/a11y-core/SKILL.md) · [SKILL.md](https://github.com/Community-Access/accessibility-agents/blob/a538edc9edfb98cdd8bae96d6b79542874b478f7/skills/contrast-master/SKILL.md) · [guard.mjs](https://github.com/Community-Access/accessibility-agents/blob/a538edc9edfb98cdd8bae96d6b79542874b478f7/hooks/guard.mjs) · [audit-recall.mjs](https://github.com/Community-Access/accessibility-agents/blob/a538edc9edfb98cdd8bae96d6b79542874b478f7/scripts/audit-recall.mjs) · [budgets.json](https://github.com/Community-Access/accessibility-agents/blob/a538edc9edfb98cdd8bae96d6b79542874b478f7/budgets.json) · [a11y-pr-gate.yml](https://github.com/Community-Access/accessibility-agents/blob/a538edc9edfb98cdd8bae96d6b79542874b478f7/.github/workflows/a11y-pr-gate.yml) · [verify.yml](https://github.com/Community-Access/accessibility-agents/blob/a538edc9edfb98cdd8bae96d6b79542874b478f7/.github/workflows/verify.yml) · [README.md](https://github.com/Community-Access/accessibility-agents/blob/a538edc9edfb98cdd8bae96d6b79542874b478f7/example/README.md) |

<a id="ux-a11y-specialist-skills"></a>

### a11y-specialist-skills (masuP9)

| Thuộc tính | Giá trị |
|---|---|
| Repo | https://github.com/masup9/a11y-specialist-skills |
| License | MIT (LICENSE gốc © 2025 masuP9; `packages/a11y-audit/package.json` khai MIT) |
| Phiên bản đã đọc | `b44bfb728800932265c4c89db570a8f7706123ca` (commit 2026-11-11) |
| Kiểm chứng | 2026-11-23; code-read; đã đọc README.md, LICENSE, skills/auditing-wcag/SKILL.md, skills/auditing-wcag/references/manual-checks.md, skills/a11y-knowledge/references/criteria/1.4.3.md, packages/a11y-audit/package.json, .github/workflows/ci.yml; chưa chạy upstream |
| Mảng UX | accessibility: đánh giá WCAG 2.2 A/AA có hệ thống, review lỗi, lập kế hoạch audit và cải thiện, hướng dẫn khi implement |
| Cơ chế đáng học | - `skills/auditing-wcag/SKILL.md`: scope contract (mức A/AA, trang, môi trường, có cho phép thao tác gây tác dụng phụ hay không) quyết định tham số `--checks`; allowlist riêng các check không thao tác trang<br>- `@a11y-skills/audit` (packages/a11y-audit): check tự viết cho reflow 320px, text spacing, target size, focus indicator, keyboard trap, non-text contrast...; exit code 0/1/2; CI chạy smoke test và CLI trên fixture HTML<br>- `skills/a11y-knowledge/references/criteria/<số>.md`: mỗi tiêu chí có bằng chứng đánh số (ví dụ 1.4.3-E01), ghi rõ 'Judgment lines', điều kiện và giới hạn, ngày kiểm nguồn W3C; mục 'do not assert' buộc để NT<br>- `references/manual-checks.md` + `output-format.md` + `coverage-matrix.md`: bảng tiêu chí cần người, bằng chứng yêu cầu, luật Fail; báo cáo phủ mọi tiêu chí A/AA |
| Tiêu chí và cách đo | Mặc định WCAG 2.2 AA (README, SKILL.md; có thể chọn A). Phân tách rõ: Pass/Fail chỉ khi có bằng chứng, thiếu thì NT; axe 'passes' chỉ là bằng chứng trong phạm vi luật chứ không phải Pass cho cả tiêu chí. Phần cần người: 1.4.4, 1.4.10, 1.4.12 (cần xem ảnh), thời gian, nhấp nháy, nội dung (alt, nhãn, heading). Screen reader và tổ hợp AT x trình duyệt ghi rõ là ngoài phạm vi. Contrast 1.4.3 dùng axe `color-contrast`, repo không có check riêng cho 1.4.3; ngưỡng 4.5:1/3:1 theo W3C. Eval: ci.yml chạy lint, build, smoke test Playwright và CLI smoke (kỳ vọng exit 1 trên fixture lỗi); không thấy đo recall/precision của skill trên site thật. |
| Giới hạn và rủi ro | CLI chạy qua `npx -y @a11y-skills/audit` (tải gói từ npm khi chạy, allowed-tools cho phép) là rủi ro chuỗi cung ứng nếu không ghim. Các check có tác dụng phụ (nhấn phím, rê chuột) cần xác nhận phạm vi; tác giả đã tách allowlist. Kho giàu nội dung song ngữ Anh/Nhật nên nặng (780 file). Số liệu 'axe-core 4.14.0' trong kho tri thức là tuyên bố tác giả (chưa xác minh). |
| So với | UI-agent a11y của Community-Access (hồ sơ cùng lô), axe-core (`axe-core`), WCAG 2.2 (`wcag-2-2`) |
| Nguồn | [README.md](https://github.com/masup9/a11y-specialist-skills/blob/b44bfb728800932265c4c89db570a8f7706123ca/README.md) · [LICENSE](https://github.com/masup9/a11y-specialist-skills/blob/b44bfb728800932265c4c89db570a8f7706123ca/LICENSE) · [SKILL.md](https://github.com/masup9/a11y-specialist-skills/blob/b44bfb728800932265c4c89db570a8f7706123ca/skills/auditing-wcag/SKILL.md) · [manual-checks.md](https://github.com/masup9/a11y-specialist-skills/blob/b44bfb728800932265c4c89db570a8f7706123ca/skills/auditing-wcag/references/manual-checks.md) · [1.4.3.md](https://github.com/masup9/a11y-specialist-skills/blob/b44bfb728800932265c4c89db570a8f7706123ca/skills/a11y-knowledge/references/criteria/1.4.3.md) · [package.json](https://github.com/masup9/a11y-specialist-skills/blob/b44bfb728800932265c4c89db570a8f7706123ca/packages/a11y-audit/package.json) · [ci.yml](https://github.com/masup9/a11y-specialist-skills/blob/b44bfb728800932265c4c89db570a8f7706123ca/.github/workflows/ci.yml) |

<a id="ux-aipex-wcag22-a11y-audit"></a>

### AIPex: skill wcag22-a11y-audit

| Thuộc tính | Giá trị |
|---|---|
| Repo | https://github.com/AIPexStudio/AIPex |
| License | MIT (LICENSE gốc, © 2024 AIPex; README cũng có badge MIT) |
| Phiên bản đã đọc | `4173fa865fed46aa4dd7af19f39a2ecace634116` (commit 2026-08-26) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE, packages/browser-runtime/src/skill/built-in/wcag22-a11y-audit/SKILL.md, packages/browser-runtime/src/skill/lib/services/skill-manager.ts, packages/browser-runtime/src/skill/built-in/ux-audit-walkthrough/SKILL.md; chưa chạy upstream |
| Mảng UX | accessibility: audit trang trực tiếp trong trình duyệt do agent điều khiển (cây accessibility, bàn phím, ảnh chụp) |
| Cơ chế đáng học | - `SKILL.md` mục 'Tool Usage Strategy': thứ tự ưu tiên cây accessibility, rồi ảnh chụp + LLM, rồi thao tác bàn phím; mỗi tiêu chí nói tool nào là chính<br>- Mẫu báo cáo cố định: Pass/Fail/Partial/Needs Verification, bảng phủ trạng thái (default/hover/focus/disabled) cho 1.4.11, ngoặc `[[screenshot:N]]` để xuất ZIP kèm ảnh bằng `download_current_chat_report_zip`<br>- Mục 'Threat Context & Privacy Notes': nhắc ảnh và dump cây có thể chứa PII, không đưa dữ liệu thô vào báo cáo<br>- `skill-manager.ts`: skill được nhúng bằng `?raw` và ghi vào ZenFS khi khởi tạo; cùng nơi nạp `ux-audit-walkthrough` (đánh giá heuristic tương tác) |
| Tiêu chí và cách đo | Tuyên bố WCAG 2.2 nhưng chỉ 8 tiêu chí, không có 2.4.11, 2.5.8, 3.3.8 hay tiêu chí nào mới. Không phân loại rõ máy/người: 1.1.1, 2.1.1, 4.1.2 đọc từ cây (cấu trúc, có tính tất định); 1.4.3, 1.4.11, 2.4.7 do model xem ảnh (ước lượng, luôn kèm 'cần xác minh bằng WebAIM/axe'); 2.1.1 và 2.1.2 là phép thử tương tác bằng phím. Ngưỡng nêu rõ: chữ thường 4.5:1, chữ lớn ≥24px hoặc ≥18.66px đậm 3:1, phi văn bản 3:1. Không có script đo tỉ lệ tương phản, không eval, không thấy test cho skill này (chưa mở CI). |
| Giới hạn và rủi ro | Contrast do LLM nhìn ảnh nên dễ sai cả hai chiều; skill chỉ 'khuyến nghị' công cụ xác nhận chứ không buộc. Ảnh chụp trang có thể gửi tới nhà cung cấp model do người dùng chọn (BYOK), nên README 'dữ liệu không rời máy' chưa xác minh với đường gọi LLM. Phần còn lại của sản phẩm là trợ lý tự động hóa trình duyệt (quyền rộng trên tab), nằm ngoài phạm vi hồ sơ. Không đọc workflow CI. |
| So với | a11y-specialist-skills (hồ sơ cùng lô), Playwright MCP (`playwright-mcp`), axe-core (`axe-core`) |
| Nguồn | [README.md](https://github.com/AIPexStudio/AIPex/blob/4173fa865fed46aa4dd7af19f39a2ecace634116/README.md) · [LICENSE](https://github.com/AIPexStudio/AIPex/blob/4173fa865fed46aa4dd7af19f39a2ecace634116/LICENSE) · [SKILL.md](https://github.com/AIPexStudio/AIPex/blob/4173fa865fed46aa4dd7af19f39a2ecace634116/packages/browser-runtime/src/skill/built-in/wcag22-a11y-audit/SKILL.md) · [skill-manager.ts](https://github.com/AIPexStudio/AIPex/blob/4173fa865fed46aa4dd7af19f39a2ecace634116/packages/browser-runtime/src/skill/lib/services/skill-manager.ts) · [SKILL.md](https://github.com/AIPexStudio/AIPex/blob/4173fa865fed46aa4dd7af19f39a2ecace634116/packages/browser-runtime/src/skill/built-in/ux-audit-walkthrough/SKILL.md) |

<a id="ux-pa11y"></a>

### Pa11y

| Thuộc tính | Giá trị |
|---|---|
| Repo | https://github.com/pa11y/pa11y |
| License | LGPL-3.0-only (LICENSE là văn bản LGPL v3; package.json khai `LGPL-3.0-only`) |
| Phiên bản đã đọc | `5c3b4182f752cd145849f5b0fafd5cbbaa4f3da6` (commit 2026-11-01) |
| Kiểm chứng | 2026-11-23; code-read; đã đọc README.md, LICENSE, package.json, lib/runners/axe.js, lib/runners/htmlcs.js, .github/workflows/tests.yml; chưa chạy upstream |
| Mảng UX | accessibility: quét tự động cổng CI cho trang đã render (không phải đánh giá thiết kế) |
| Cơ chế đáng học | - `lib/runners/axe.js`: `createAxeRunOnlyTags` khóa runOnly vào wcag2a/wcag21a (+wcag2aa/wcag21aa khi chuẩn ≠ WCAG2A) + best-practice; `incomplete` của axe thành issue có `needsFurtherReview`<br>- `lib/runners/htmlcs.js` + README: runner mặc định HTML_CodeSniffer, `--add-rule` thêm luật WCAG 2.1; có thể chạy cả hai runner cùng lúc<br>- Mã thoát 0/1/2 và `--level`, `--threshold`, `--ignore`, `--root-element`, `--hide-elements`: cổng tất định, dễ gắn CI<br>- Runner tùy biến là module CommonJS (README): chỗ cắm cho kiểm tra riêng |
| Tiêu chí và cách đo | Mặc định WCAG 2.1 AA trên thực tế: chuẩn nhận `WCAG2A\|AA\|AAA` (AAA chỉ htmlcs), axe không được bật tag `wcag22*` (suy từ mã, chưa chạy) nên các luật WCAG 2.2 của axe không chạy qua pa11y; README ghi 'WCAG 2.1 rules' cho add-rule. Máy kiểm hết: không có khái niệm kiểm tay ngoài việc hạ mức 'needs review' của axe và dòng notice/warning của htmlcs. Ngưỡng là số lỗi theo mức (mặc định chỉ `error` làm thất bại). Không eval chất lượng phát hiện; CI (tests.yml) chạy lint và test trên 3 hệ điều hành, Node 22-26. |
| Giới hạn và rủi ro | LGPL-3.0: dùng như CLI hoặc phụ thuộc thường không buộc mở mã sản phẩm, nhưng sửa/nhúng lại mã pa11y có điều kiện riêng (không phải kết luận pháp lý, cần đọc kỹ). Tải Chromium qua Puppeteer; quét URL do người dùng đưa nên cần cẩn trọng với trang nội bộ. Không kiểm screen reader, focus order, nghĩa của alt. README tự nhắc kiểm tự động chỉ bổ trợ kiểm tay (xem pa11y-ci). |
| So với | axe-core (`axe-core`), Lighthouse CI (`lighthouse-ci`), eslint-plugin-jsx-a11y (`eslint-plugin-jsx-a11y`) |
| Nguồn | [README.md](https://github.com/pa11y/pa11y/blob/5c3b4182f752cd145849f5b0fafd5cbbaa4f3da6/README.md) · [LICENSE](https://github.com/pa11y/pa11y/blob/5c3b4182f752cd145849f5b0fafd5cbbaa4f3da6/LICENSE) · [package.json](https://github.com/pa11y/pa11y/blob/5c3b4182f752cd145849f5b0fafd5cbbaa4f3da6/package.json) · [axe.js](https://github.com/pa11y/pa11y/blob/5c3b4182f752cd145849f5b0fafd5cbbaa4f3da6/lib/runners/axe.js) · [htmlcs.js](https://github.com/pa11y/pa11y/blob/5c3b4182f752cd145849f5b0fafd5cbbaa4f3da6/lib/runners/htmlcs.js) · [tests.yml](https://github.com/pa11y/pa11y/blob/5c3b4182f752cd145849f5b0fafd5cbbaa4f3da6/.github/workflows/tests.yml) |

<a id="ux-pa11y-ci"></a>

### Pa11y CI

| Thuộc tính | Giá trị |
|---|---|
| Repo | https://github.com/pa11y/pa11y-ci |
| License | LGPL-3.0-only (LICENSE là văn bản LGPL v3; package.json khai `LGPL-3.0-only`) |
| Phiên bản đã đọc | `05f4dbbf58d1e53391cddb02ddbc067c45ca465b` (commit 2026-11-01) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE, package.json, .github/workflows/tests.yml, .github/workflows/publish.yml; chưa chạy upstream |
| Mảng UX | accessibility: cổng CI quét hàng loạt trang, chạy lại để phát hiện hồi quy |
| Cơ chế đáng học | - README mục 'Exit codes and thresholds': 0 đạt, 1 lỗi kỹ thuật, 2 có trang vượt ngưỡng; ngưỡng mặc định 0<br>- Cấu hình hai tầng: tùy chọn theo trang (`runners`, `ignore`, `actions`, `screenCapture`, `threshold`) và tùy chọn cả lần chạy (`concurrency`, `reporters`)<br>- `--sitemap`, `--sitemap-find/replace/exclude`: lấy trang từ sitemap và đổi host sang môi trường staging<br>- Phụ thuộc `pa11y ^10.0.0` (package.json) nên chuẩn và runner là của Pa11y |
| Tiêu chí và cách đo | Chuẩn và phiên bản WCAG thừa hưởng từ `pa11y` (WCAG2A/AA/AAA, với axe chỉ đến tag 2.1; xem hồ sơ Pa11y); repo này không đặt thêm. Hoàn toàn kiểm bằng máy; README ghi thẳng 'automated checks complement manual testing and testing with assistive technologies', không có luồng kiểm tay. Ngưỡng là số lỗi/trang và số lỗi toàn run. Không eval; CI chỉ lint/test. Chưa mở `lib/pa11y-ci.js` nên cơ chế chạy song song và gom kết quả chỉ biết qua README. |
| Giới hạn và rủi ro | LGPL-3.0-only như Pa11y. Chạy trình duyệt headless trên URL tùy ý; sitemap-index được tải đệ quy nên cần giới hạn nguồn. Publish workflow dùng `id-token: write` để phát hành npm (đã đọc). Thiếu bất kỳ phát hiện nào về kiểm màn hình đọc, thứ tự focus hoặc chất lượng nội dung. |
| So với | Pa11y (hồ sơ cùng lô), Lighthouse CI (`lighthouse-ci`), Argos (`argos`) |
| Nguồn | [README.md](https://github.com/pa11y/pa11y-ci/blob/05f4dbbf58d1e53391cddb02ddbc067c45ca465b/README.md) · [LICENSE](https://github.com/pa11y/pa11y-ci/blob/05f4dbbf58d1e53391cddb02ddbc067c45ca465b/LICENSE) · [package.json](https://github.com/pa11y/pa11y-ci/blob/05f4dbbf58d1e53391cddb02ddbc067c45ca465b/package.json) · [tests.yml](https://github.com/pa11y/pa11y-ci/blob/05f4dbbf58d1e53391cddb02ddbc067c45ca465b/.github/workflows/tests.yml) · [publish.yml](https://github.com/pa11y/pa11y-ci/blob/05f4dbbf58d1e53391cddb02ddbc067c45ca465b/.github/workflows/publish.yml) |

<a id="ux-guidepup"></a>

### Guidepup

| Thuộc tính | Giá trị |
|---|---|
| Repo | https://github.com/guidepup/guidepup |
| License | MIT (LICENSE gốc, © 2023 Craig Morten; package.json khai MIT) |
| Phiên bản đã đọc | `77fc318b78e95384fb1b03dd0b9e923b64e9cf27` (commit 2026-11-08) |
| Kiểm chứng | 2026-11-23; code-read; đã đọc README.md, LICENSE, package.json, src/BaseScreenReader.ts, src/navigateUntil.ts, src/macOS/VoiceOver/VoiceOver.ts, .github/workflows/playwright-nvda.yml, examples/playwright-voiceover/tests/headerNavigation.ts; chưa chạy upstream |
| Mảng UX | accessibility: phần 'cần trình đọc màn hình' mà máy quét tĩnh không làm được, ở dạng test tự động |
| Cơ chế đáng học | - `src/BaseScreenReader.ts` + `IScreenReader`: giao diện chung (start/stop, điều hướng theo heading/link/landmark, `perform(keyboardCommand)`, `capture`) cho 3 triển khai `windows/NVDA`, `linux/Orca`, `macOS/VoiceOver`<br>- `src/navigateUntil.ts`: lặp bước điều hướng cho đến khi lời đọc khớp chuỗi/regex/hàm, lỗi nếu quá `maxNavigationAttempts` (mặc định 10)<br>- Nhật ký lời đọc (`spokenPhraseLog`, `itemTextLog`) là thứ test khẳng định; ví dụ `examples/playwright-voiceover` kết hợp Playwright mở trang rồi VoiceOver duyệt<br>- `.github/workflows/playwright-nvda.yml`: ma trận windows-2022/2025 x chromium/firefox chạy NVDA thật sau `@guidepup/setup` |
| Tiêu chí và cách đo | Không gắn WCAG 2.1 hay 2.2; công cụ khẳng định hành vi đọc của AT, người viết tự quyết tiêu chí (ví dụ heading có được đọc, nút có tên). Chỉ chạy được trên máy có screen reader thật, nên là phần 'cần người/AT' được tự động hóa chứ không thay người nghe. CI của repo chạy NVDA/VoiceOver/Orca thật trên runner; không có số liệu độ ổn định hay so sánh giữa screen reader. Ví dụ dùng `delay(500)` giữa bước cho thấy test nhạy với thời gian. |
| Giới hạn và rủi ro | Cần `npx @guidepup/setup setup` thay đổi máy (chưa đọc repo setup, chưa xác minh chính xác đổi gì) và cài tài sản screen reader; chỉ nên chạy trên máy ảo/CI. Ép dùng VoiceOver/NVDA nên phụ thuộc phiên bản hệ điều hành (README liệt kê macOS, Windows Server, Ubuntu 26.04+). Lời đọc khác nhau theo phiên bản, ngôn ngữ, cấu hình nên test dễ giòn. Không thấy telemetry trong `src` (chỉ grep). |
| So với | axe-core (`axe-core`), Playwright MCP (`playwright-mcp`), Pa11y (hồ sơ cùng lô) |
| Nguồn | [README.md](https://github.com/guidepup/guidepup/blob/77fc318b78e95384fb1b03dd0b9e923b64e9cf27/README.md) · [LICENSE](https://github.com/guidepup/guidepup/blob/77fc318b78e95384fb1b03dd0b9e923b64e9cf27/LICENSE) · [package.json](https://github.com/guidepup/guidepup/blob/77fc318b78e95384fb1b03dd0b9e923b64e9cf27/package.json) · [BaseScreenReader.ts](https://github.com/guidepup/guidepup/blob/77fc318b78e95384fb1b03dd0b9e923b64e9cf27/src/BaseScreenReader.ts) · [navigateUntil.ts](https://github.com/guidepup/guidepup/blob/77fc318b78e95384fb1b03dd0b9e923b64e9cf27/src/navigateUntil.ts) · [VoiceOver.ts](https://github.com/guidepup/guidepup/blob/77fc318b78e95384fb1b03dd0b9e923b64e9cf27/src/macOS/VoiceOver/VoiceOver.ts) · [playwright-nvda.yml](https://github.com/guidepup/guidepup/blob/77fc318b78e95384fb1b03dd0b9e923b64e9cf27/.github/workflows/playwright-nvda.yml) · [headerNavigation.ts](https://github.com/guidepup/guidepup/blob/77fc318b78e95384fb1b03dd0b9e923b64e9cf27/examples/playwright-voiceover/tests/headerNavigation.ts) |

<a id="ux-happo"></a>

### Happo (client)

| Thuộc tính | Giá trị |
|---|---|
| Repo | https://github.com/happo/happo |
| License | Không có file LICENSE ở gốc (package.json và badge README khai MIT, chưa đối chiếu được file nguồn) |
| Phiên bản đã đọc | `16cd2c4bf0fc73251c3da85a8b6d61da6341c5be` (commit 2026-10-07) |
| Kiểm chứng | 2026-11-23; code-read; đã đọc README.md, package.json, AGENTS.md, src/config/configSchema.ts, src/config/index.ts, src/cli/telemetry.ts, src/browser/takeDOMSnapshot.ts, .github/workflows/test.yaml; chưa chạy upstream |
| Mảng UX | accessibility + visual regression: cổng 'không thêm lỗi a11y mới' trên PR, kèm diff hình ảnh |
| Cơ chế đáng học | - `src/config/configSchema.ts`: `targets` gồm trình duyệt và loại `accessibility`; `blockApproval.renderErrors` và `accessibilityViolations`<br>- `src/browser/takeDOMSnapshot.ts`: tuần tự hóa DOM, CSS (kể cả constructed stylesheets) và URL tài sản để dựng lại ở máy chủ<br>- README: bật `blockApproval` trong một PR để vừa sửa vừa bật mà không ảnh hưởng nhánh khác<br>- `.github/workflows/test.yaml`: dogfood bằng `orchestrate-happo` trên nhiều dự án mẫu (Storybook v8-10, Cypress, Playwright) |
| Tiêu chí và cách đo | Không nêu phiên bản WCAG hay bộ luật trong repo (kiểm a11y xử lý ở happo.io, không có trong mã đã đọc). Tiêu chí là 'vi phạm a11y mới so với baseline' và 'lỗi render', do máy chủ tính; không có phần kiểm tay. Không có eval công khai về độ chính xác. Test của repo chạy unit và nhiều tích hợp trên Ubuntu và Windows, cần khóa API. |
| Giới hạn và rủi ro | Dữ liệu rời máy: DOM, CSS và tài sản trang được tải lên happo.io (endpoint mặc định `https://happo.io`); cần cân nhắc với UI nội bộ. `telemetry.ts` gửi lỗi tới Sentry (tên lỗi, message, stack, CI, Node, nền tảng); tắt bằng `HAPPO_DISABLE_TELEMETRY`. Dịch vụ thương mại cần API key; license không có file gốc và repo ngừng cập nhật (chưa xác minh trạng thái hỗ trợ lâu dài). |
| So với | Argos (`argos`), Lighthouse CI (`lighthouse-ci`), Responsively App (`responsively-org-responsively-app`) |
| Nguồn | [README.md](https://github.com/happo/happo/blob/16cd2c4bf0fc73251c3da85a8b6d61da6341c5be/README.md) · [package.json](https://github.com/happo/happo/blob/16cd2c4bf0fc73251c3da85a8b6d61da6341c5be/package.json) · [AGENTS.md](https://github.com/happo/happo/blob/16cd2c4bf0fc73251c3da85a8b6d61da6341c5be/AGENTS.md) · [configSchema.ts](https://github.com/happo/happo/blob/16cd2c4bf0fc73251c3da85a8b6d61da6341c5be/src/config/configSchema.ts) · [index.ts](https://github.com/happo/happo/blob/16cd2c4bf0fc73251c3da85a8b6d61da6341c5be/src/config/index.ts) · [telemetry.ts](https://github.com/happo/happo/blob/16cd2c4bf0fc73251c3da85a8b6d61da6341c5be/src/cli/telemetry.ts) · [takeDOMSnapshot.ts](https://github.com/happo/happo/blob/16cd2c4bf0fc73251c3da85a8b6d61da6341c5be/src/browser/takeDOMSnapshot.ts) · [test.yaml](https://github.com/happo/happo/blob/16cd2c4bf0fc73251c3da85a8b6d61da6341c5be/.github/workflows/test.yaml) |

<a id="ux-color-expert-skill"></a>

### color-expert (meodai)

| Thuộc tính | Giá trị |
|---|---|
| Repo | https://github.com/meodai/skill.color-expert |
| License | CC-BY-4.0 cho phần gốc (LICENSE); `THIRD_PARTY_NOTICES.md` nói các file `references/` dựa trên nguồn ngoài và không được cấp lại license |
| Phiên bản đã đọc | `5bf7c7704d56bccc6aeea38c36bcf449abe56a6c` (commit 2026-10-21) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE, THIRD_PARTY_NOTICES.md, SKILL.md, SECURITY.md, evals/TRIGGERING.md, evals/trigger-evals.json, evals/task-prompts.md; chưa chạy upstream |
| Mảng UX | khoa học màu và độ tương phản cho design system, dataviz, theme sáng/tối; không phải audit WCAG |
| Cơ chế đáng học | - `SKILL.md` mục 'How to Use': 5 chế độ (dự án cụ thể, design system/ramp, nghệ thuật tạo sinh, câu hỏi chung, xây công cụ) với thứ tự ưu tiên; 'đưa nhiều hướng với đánh đổi trước khi chốt một'<br>- Token graph tham chiếu, ngữ nghĩa, thành phần; quy tắc suy dẫn như `bestContrastWith(surface)` và `mostVivid(... minContrast: 4.5)` để màu chữ tự tính lại<br>- Chart: đặt viền và đòi 3:1 giữa fill và viền thay vì 3:1 giữa mọi cặp fill; kiểm thang tuần tự bằng đạo hàm cảm nhận phẳng, cả trong thang xám<br>- `evals/TRIGGERING.md` + `trigger-evals.json`: quy tắc trigger viết ra (có `kind`, `why`) để tranh luận ranh giới; `task-prompts.md` là rubric định tính |
| Tiêu chí và cách đo | Không gắn WCAG 2.1 hay 2.2 (công thức contrast giống nhau): nói 'xác minh mọi cặp chữ/nền bằng APCA hoặc WCAG ở sáng và tối', nêu 3:1/4.5:1/7:1 và APCA 60/75/90; nhắc thang xám 'không phải bằng chứng a11y'. Skill không có script kiểm tỉ lệ, nên model phải gọi công cụ ngoài (Huetone, Leonardo, Color Buddy...). Eval chỉ là dữ liệu trigger (30 ca) và đề định tính, repo không có runner đã đọc. Bảng tỉ lệ cặp màu đạt chuẩn (WCAG 4.5:1 ~11,98%, APCA 90 ~0,08%) là số của tác giả (chưa xác minh). |
| Giới hạn và rủi ro | File lớn tốn token khi kích hoạt; description rộng có thể bật skill không cần. Nhiều `references/` là transcript, scrape website, tóm tắt bài (huevaluechroma.com...), có nguy cơ bản quyền khi phân phối lại dù repo ghi CC-BY-4.0 cho phần gốc. Có chỉ dẫn mang tính quan điểm ('không bao giờ gợi ý coolors.co'). SECURITY.md nói chỉ là nội dung đọc, không chạy mã (tuyên bố). |
| So với | Radix Colors (`radix-colors`), UI UX Pro Max (`ui-ux-pro-max`), Taste Skill (`taste-skill`) |
| Nguồn | [README.md](https://github.com/meodai/skill.color-expert/blob/5bf7c7704d56bccc6aeea38c36bcf449abe56a6c/README.md) · [LICENSE](https://github.com/meodai/skill.color-expert/blob/5bf7c7704d56bccc6aeea38c36bcf449abe56a6c/LICENSE) · [THIRD_PARTY_NOTICES.md](https://github.com/meodai/skill.color-expert/blob/5bf7c7704d56bccc6aeea38c36bcf449abe56a6c/THIRD_PARTY_NOTICES.md) · [SKILL.md](https://github.com/meodai/skill.color-expert/blob/5bf7c7704d56bccc6aeea38c36bcf449abe56a6c/SKILL.md) · [SECURITY.md](https://github.com/meodai/skill.color-expert/blob/5bf7c7704d56bccc6aeea38c36bcf449abe56a6c/SECURITY.md) · [TRIGGERING.md](https://github.com/meodai/skill.color-expert/blob/5bf7c7704d56bccc6aeea38c36bcf449abe56a6c/evals/TRIGGERING.md) · [trigger-evals.json](https://github.com/meodai/skill.color-expert/blob/5bf7c7704d56bccc6aeea38c36bcf449abe56a6c/evals/trigger-evals.json) · [task-prompts.md](https://github.com/meodai/skill.color-expert/blob/5bf7c7704d56bccc6aeea38c36bcf449abe56a6c/evals/task-prompts.md) |

<a id="ux-platform-design-skills"></a>

### Platform Design Skills (ehmo)

| Thuộc tính | Giá trị |
|---|---|
| Repo | https://github.com/ehmo/platform-design-skills |
| License | MIT (LICENSE gốc, dòng bản quyền 'Copyright (c) 2026' không ghi tên); repo còn kèm `Apple_HIG.pdf` 2,4 MB chép từ trang Apple, không thuộc phạm vi MIT) |
| Phiên bản đã đọc | `dc2be825d8b439caea78e9eaa8fb3ac23b0ff3e9` (commit 2026-03-18) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE, CLAUDE.md, skills/ios/SKILL.md, skills/ios/rules/_sections.md, skills/ios/metadata.json, skills/web/SKILL.md, skills/android/SKILL.md; chưa chạy upstream |
| Mảng UX | bộ luật theo nền tảng (Apple HIG, Material 3, Web) cho review và sinh UI; a11y là một mục trong từng bộ |
| Cơ chế đáng học | - `skills/<nền tảng>/SKILL.md`: frontmatter `name`/`description` có câu kích hoạt, rồi các nhóm (Layout, Navigation, Typography, Color, Accessibility, Gestures, Components...) mỗi nhóm có Impact CRITICAL/HIGH<br>- Mẫu luật: 'Rule 1.1: tối thiểu 44pt', code đúng/sai, kèm mục 'Anti-Patterns' (ví dụ hamburger menu, font cố định, chỉ dùng màu) và checklist cuối<br>- `rules/_sections.md` + `metadata.json` (nguồn Apple, phiên bản, ngày): mục lục và nguồn tham chiếu cho từng skill<br>- Skill Android dùng ID luật R1.3, R6.7 và tách 'dynamic color là mặc định, màu tùy biến là dự phòng' |
| Tiêu chí và cách đo | Skill web nói dựa trên WCAG 2.2 (mức A/AA, vài luật AAA ghi chú) và nêu 2.5.8 24px AA, 2.5.5 44px AAA đúng; nhưng viết '2.4.11 (AA)' và '2.4.12 (AAA)' cho focus và cho rằng 2.2 'bắt buộc' vùng viền 2px, trong khi 2.4.11 là Focus Not Obscured (Minimum), 2.4.12 bản Enhanced, còn focus appearance là 2.4.13 (AAA). Skill Android nêu contrast 4.5:1/3:1. Tuyệt đại đa số là ngưỡng viết tay (44pt, 48dp, 24px), không phân biệt máy kiểm được hay cần người/screen reader, không có script hay eval và repo không có workflow CI. |
| Giới hạn và rủi ro | Chép nội dung Apple HIG (PDF 2,4 MB) vào repo MIT: quyền sử dụng nội dung của Apple không do MIT cấp, cần cân nhắc khi vendor. Luật có thể lỗi thời so với HIG/M3 mới (metadata ghi 'February 2026'); gán số tiêu chí WCAG sai ở skill web. Dòng bản quyền không có tên chủ sở hữu. Không có cơ chế phát hiện luật nào được áp dụng trong output. |
| So với | Apple HIG: Layout (`apple-hig-layout`), Material 3 canonical layouts (`material-3-canonical-layouts`), UI UX Pro Max (`ui-ux-pro-max`) |
| Nguồn | [README.md](https://github.com/ehmo/platform-design-skills/blob/dc2be825d8b439caea78e9eaa8fb3ac23b0ff3e9/README.md) · [LICENSE](https://github.com/ehmo/platform-design-skills/blob/dc2be825d8b439caea78e9eaa8fb3ac23b0ff3e9/LICENSE) · [CLAUDE.md](https://github.com/ehmo/platform-design-skills/blob/dc2be825d8b439caea78e9eaa8fb3ac23b0ff3e9/CLAUDE.md) · [SKILL.md](https://github.com/ehmo/platform-design-skills/blob/dc2be825d8b439caea78e9eaa8fb3ac23b0ff3e9/skills/ios/SKILL.md) · [_sections.md](https://github.com/ehmo/platform-design-skills/blob/dc2be825d8b439caea78e9eaa8fb3ac23b0ff3e9/skills/ios/rules/_sections.md) · [metadata.json](https://github.com/ehmo/platform-design-skills/blob/dc2be825d8b439caea78e9eaa8fb3ac23b0ff3e9/skills/ios/metadata.json) · [SKILL.md](https://github.com/ehmo/platform-design-skills/blob/dc2be825d8b439caea78e9eaa8fb3ac23b0ff3e9/skills/web/SKILL.md) · [SKILL.md](https://github.com/ehmo/platform-design-skills/blob/dc2be825d8b439caea78e9eaa8fb3ac23b0ff3e9/skills/android/SKILL.md) |

<a id="ux-material-design-3-ui-skill"></a>

### Material Design 3 UI Skill (skydashnet)

| Thuộc tính | Giá trị |
|---|---|
| Repo | https://github.com/skydashnet/material-design-3-ui-skill |
| License | MIT (LICENSE gốc, © 2026 'Material Design 3 UI Skill contributors') |
| Phiên bản đã đọc | `82783f76de4a5b08a60421cae935cf8de7ca1ee8` (commit 2026-10-01) |
| Kiểm chứng | 2026-11-23; code-read; đã đọc README.md, LICENSE, SKILL.md, references/accessibility.md, references/color-system.md, tests/README.md, tests/validate_skill.py, tests/cases/04-form-validation.md, .github/workflows/validate.yml, install.sh, CHANGELOG.md; chưa chạy upstream |
| Mảng UX | design system cho agent (Material 3/Expressive) + design review có rubric; a11y là tham chiếu bắt buộc trước khi duyệt |
| Cơ chế đáng học | - `SKILL.md`: luồng user goal -> IA -> thích ứng -> token ngữ nghĩa -> thành phần -> trạng thái -> a11y -> motion -> Expressive -> audit; bảng 'Need -> Read' để nạp dần (progressive disclosure)<br>- Self-audit 8 hạng mục chấm 0/1/2; cấm duyệt khi 0 ở component semantics, states & feedback, accessibility; 'đừng nâng điểm cho vừa lòng người dùng'<br>- `tests/validate_skill.py` + `validate.yml`: kiểm frontmatter, tên/phiên bản, mọi `references/*.md` được nhắc đều tồn tại, manifest `skill-files.txt`, cùng `bash -n` cho script cài<br>- `tests/cases/*.md`: 6 ca (Expected decisions, Failure signals) như case 04 form: nhãn thường trực, lỗi không chỉ bằng màu, giữ dữ liệu khi lỗi |
| Tiêu chí và cách đo | `references/accessibility.md` bắt buộc đọc trước khi duyệt: target 48dp, contrast 4.5:1/3:1 ('planning targets'), tên cho icon, focus, bàn phím, co chữ, reduced motion; chỉ nói 'WCAG-aligned', không nêu 2.1 hay 2.2, và grep chỉ thấy đúng một lần chữ WCAG. Không tách phần máy kiểm được khỏi phần cần kiểm tay hay screen reader. CI chỉ kiểm tính toàn vẹn của gói bằng script tĩnh, không đánh giá chất lượng thiết kế do model sinh; ca hành vi để chấm thủ công hoặc tự dựng. |
| Giới hạn và rủi ro | `install.sh`/`install.ps1` được quảng bá bằng `curl \| bash` từ nhánh `main` (REF mặc định `main`, không ghim SHA) rồi ghi vào thư mục toàn cục của 7 agent, có `rm -rf` thư mục đích; cần đọc script trước khi chạy. Tuyên bố 'hardened' trong CHANGELOG chưa xác minh (chỉ xem lệnh chính). Skill thiên về nguyên tắc, không có token/giá trị M3 cụ thể nên phải xác minh số liệu với m3.material.io. |
| So với | Material 3 canonical layouts (`material-3-canonical-layouts`), Material Web (`material-web`), Platform Design Skills (hồ sơ cùng lô) |
| Nguồn | [README.md](https://github.com/skydashnet/material-design-3-ui-skill/blob/82783f76de4a5b08a60421cae935cf8de7ca1ee8/README.md) · [LICENSE](https://github.com/skydashnet/material-design-3-ui-skill/blob/82783f76de4a5b08a60421cae935cf8de7ca1ee8/LICENSE) · [SKILL.md](https://github.com/skydashnet/material-design-3-ui-skill/blob/82783f76de4a5b08a60421cae935cf8de7ca1ee8/SKILL.md) · [accessibility.md](https://github.com/skydashnet/material-design-3-ui-skill/blob/82783f76de4a5b08a60421cae935cf8de7ca1ee8/references/accessibility.md) · [color-system.md](https://github.com/skydashnet/material-design-3-ui-skill/blob/82783f76de4a5b08a60421cae935cf8de7ca1ee8/references/color-system.md) · [README.md](https://github.com/skydashnet/material-design-3-ui-skill/blob/82783f76de4a5b08a60421cae935cf8de7ca1ee8/tests/README.md) · [validate_skill.py](https://github.com/skydashnet/material-design-3-ui-skill/blob/82783f76de4a5b08a60421cae935cf8de7ca1ee8/tests/validate_skill.py) · [04-form-validation.md](https://github.com/skydashnet/material-design-3-ui-skill/blob/82783f76de4a5b08a60421cae935cf8de7ca1ee8/tests/cases/04-form-validation.md) · [validate.yml](https://github.com/skydashnet/material-design-3-ui-skill/blob/82783f76de4a5b08a60421cae935cf8de7ca1ee8/.github/workflows/validate.yml) · [install.sh](https://github.com/skydashnet/material-design-3-ui-skill/blob/82783f76de4a5b08a60421cae935cf8de7ca1ee8/install.sh) · [CHANGELOG.md](https://github.com/skydashnet/material-design-3-ui-skill/blob/82783f76de4a5b08a60421cae935cf8de7ca1ee8/CHANGELOG.md) |

<a id="ux-ui-design-brain"></a>

### UI Design Brain

| Thuộc tính | Giá trị |
|---|---|
| Repo | https://github.com/carmahhawwari/ui-design-brain |
| License | MIT |
| Phiên bản đã đọc | `38f04c5a1dee55d99c686a16643cef4e2ce0f7a2` (commit 2026-02-27) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, SKILL.md, components.md (mục Modal, 60 mục), LICENSE.txt; repo không có workflow CI; chưa chạy upstream |
| Mảng UX | đưa bộ tri thức component cho agent / design system knowledge pack |
| Cơ chế đáng học | - `SKILL.md`: 4 bước (nhận diện component -> áp best practice -> chọn 1 trong 5 hướng thiết kế -> sinh code React+Tailwind), bảng tra nhanh 15 component và danh sách anti-pattern (rainbow badge, modal trong modal, spinner cho layout dự đoán được...).<br>- `components.md` (1262 dòng): 60 mục theo mẫu cố định 'Also known as / mô tả / Best practices / Common layouts' (ví dụ Modal: trap focus, X+Cancel+Escape, trả focus về trigger), giúp agent khớp yêu cầu mơ hồ với đúng component qua bí danh.<br>- Ngưỡng định lượng nằm thẳng trong văn bản: lưới 8 px, chữ thân tối thiểu 14 px, touch target 44 px, toast 4-6 s, skeleton hiện sau 300 ms, mobile test 375/768/1440. |
| Tiêu chí và cách đo | Không có rubric chấm điểm hay lệnh kiểm. Các số trên là chỉ dẫn cho model tự tuân thủ, không có máy kiểm, không có eval hay so sánh có/không skill. Mục 'How it differs from frontend-design skills' trong README là tuyên bố của tác giả (chưa xác minh). |
| Giới hạn và rủi ro | Không có CI, test, hay cơ chế chống lệch: hệ thiết kế chỉ là văn bản, không có token hay lint. README ghi 'sourced from component.gallery' nhưng không kèm điều kiện sử dụng lại dữ liệu đó; license MIT chỉ phủ phần của repo (chưa kiểm điều khoản nguồn dữ liệu). Quy tắc thẩm mỹ cố định ('no Inter/Roboto', 'one strong color moment') áp cho mọi dự án, dễ ghi đè design system riêng. |
| So với | ui-skills, frontend-design-anthropic, ui-ux-pro-max (cùng nhóm skill tri thức/triết lý UI); awesome-shadcn-ui nếu chỉ cần danh mục component |
| Nguồn | [README.md](https://github.com/carmahhawwari/ui-design-brain/blob/38f04c5a1dee55d99c686a16643cef4e2ce0f7a2/README.md) · [SKILL.md](https://github.com/carmahhawwari/ui-design-brain/blob/38f04c5a1dee55d99c686a16643cef4e2ce0f7a2/SKILL.md) · [components.md](https://github.com/carmahhawwari/ui-design-brain/blob/38f04c5a1dee55d99c686a16643cef4e2ce0f7a2/components.md) · [LICENSE.txt](https://github.com/carmahhawwari/ui-design-brain/blob/38f04c5a1dee55d99c686a16643cef4e2ce0f7a2/LICENSE.txt) |

<a id="ux-oh-my-design"></a>

### oh-my-design (OmD)

| Thuộc tính | Giá trị |
|---|---|
| Repo | https://github.com/kwakseongjae/oh-my-design |
| License | MIT (mã nguồn); các DESIGN.md và tài sản trong kho mô tả thiết kế của công ty khác, ghi 'thuộc về công ty đó, đăng lại cho mục đích tham khảo' |
| Phiên bản đã đọc | `10be2098e9796b7f4510afefb8ec96034db04b4b` (commit 2026-11-23) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE, AGENTS.md, package.json, docs/guide/design-md.md, 3 SKILL.md (omd-apply, omd-sync, omd-slop-audit), slop-gates.md, reference-quality.json, design-md/toss/DESIGN.md, LICENSE-NOTE.md của tving, README benchmark và workflow quality.yml; chưa chạy upstream |
| Mảng UX | đưa hệ thiết kế/brief cho agent (DESIGN.md + shim) và chống lệch khỏi hệ (cổng slop, drift shim) |
| Cơ chế đáng học | - `skills/omd-sync/SKILL.md`: giữ 3 shim (`CLAUDE.md`, `AGENTS.md`, `.cursor/rules/omd-design.mdc`) bằng khối có hash `<!-- omd:start v=1 hash=... -->`; thứ tự ưu tiên 'sửa tay đang chờ > DESIGN.md/graph đã nhận > mặc định của agent'; phát hiện drift khi DESIGN.md đổi mà shim cũ.<br>- `docs/guide/design-md.md`: DESIGN.md Core v2 gồm 7 mục neo cố định, không frontmatter, dán vào chat thường vẫn dùng được như brief; mỗi quyết định có id `D-<nguyên tắc>-<n>` và token mang id đó (cổng GS7 trượt token không có quyết định, GS8 trượt component dựng mới khi đã có preset).<br>- `skills/omd-autopilot/references/slop-gates.md`: danh sách cổng có/không đánh số (G1...G28+), phần máy kiểm được ghi rõ bằng grep (`transition: all`, hex ngoài token, `<select`, `100vh` hero...) và yêu cầu ghi log grep vào critique.md; `omd-slop-audit` tách 3 trục SLOP / QUALITY / FYI để không gọi lỗi a11y là 'vị AI'.<br>- `omd-apply/SKILL.md`: bảng định tuyến yêu cầu -> chuyên gia (a11y, microcopy, persona, critic...) và work packet có `protected_contract` (số lượng control, chuyển trạng thái, giá trị cần giữ) cùng ngân sách thời gian; chuyên gia chỉ tư vấn, agent chính sở hữu việc sửa và kiểm. |
| Tiêu chí và cách đo | Hai lớp. (1) Cổng slop: câu hỏi có/không, một 'có' là không ship; phần máy kiểm nằm ở grep thủ công do agent chạy, không thấy trình chạy tự động trong các file đã đọc. (2) `data/reference-quality.json`: 622 mục, 455 verified_v2, 86 partial, 81 legacy_snapshot, có ngày kiểm lại và evidence_coverage. UI-Resolve Bench (`benchmarks/ui-resolve-bench/README.md`) tự mô tả là bản nháp nội bộ v0.2, 3 fixture phát triển, chưa đủ để so sánh nhân quả hay gọi 'best UI skill'; một pilot đầu bị đánh dấu invalid vì sai kích hoạt. Workflow `quality.yml` (đã mở) chạy lint, npm test, build, check-counts, check dữ liệu tham chiếu; không chạy benchmark UI. |
| Giới hạn và rủi ro | Phạm vi quá rộng (hơn 30 skill, 20 agent, 622 DESIGN.md) nên khó mang một phần mà không kéo cả hệ. Kho DESIGN.md là giá trị đo từ site công ty khác; `design-md/tving/assets/_reference/LICENSE-NOTE.md` ghi rõ 'tham khảo, không phân phối lại' cho logo/ảnh chụp, nên dùng lại cần xét từng mục. Tuyên bố 'giá trị không xác nhận được thì để trống' chưa kiểm độc lập (chưa xác minh). Chưa đọc mã CLI/installer nên chưa biết nó ghi những file nào ngoài shim. `omd doctor` có đặt DISABLE_TELEMETRY/DO_NOT_TRACK cho tiến trình con (src/cli/doctor.ts), chưa thấy telemetry riêng của OmD nhưng chưa rà toàn bộ. |
| So với | design-md-spec-google (định dạng DESIGN.md gốc), awesome-design-md và official-design-md-voltagent (kho DESIGN.md), hallmark (cổng slop đánh số), ui-ux-pro-max |
| Nguồn | [README.md](https://github.com/kwakseongjae/oh-my-design/blob/10be2098e9796b7f4510afefb8ec96034db04b4b/README.md) · [LICENSE](https://github.com/kwakseongjae/oh-my-design/blob/10be2098e9796b7f4510afefb8ec96034db04b4b/LICENSE) · [AGENTS.md](https://github.com/kwakseongjae/oh-my-design/blob/10be2098e9796b7f4510afefb8ec96034db04b4b/AGENTS.md) · [package.json](https://github.com/kwakseongjae/oh-my-design/blob/10be2098e9796b7f4510afefb8ec96034db04b4b/package.json) · [design-md.md](https://github.com/kwakseongjae/oh-my-design/blob/10be2098e9796b7f4510afefb8ec96034db04b4b/docs/guide/design-md.md) · [SKILL.md](https://github.com/kwakseongjae/oh-my-design/blob/10be2098e9796b7f4510afefb8ec96034db04b4b/skills/omd-apply/SKILL.md) · [SKILL.md](https://github.com/kwakseongjae/oh-my-design/blob/10be2098e9796b7f4510afefb8ec96034db04b4b/skills/omd-sync/SKILL.md) · [SKILL.md](https://github.com/kwakseongjae/oh-my-design/blob/10be2098e9796b7f4510afefb8ec96034db04b4b/skills/omd-slop-audit/SKILL.md) · [slop-gates.md](https://github.com/kwakseongjae/oh-my-design/blob/10be2098e9796b7f4510afefb8ec96034db04b4b/skills/omd-autopilot/references/slop-gates.md) · [reference-quality.json](https://github.com/kwakseongjae/oh-my-design/blob/10be2098e9796b7f4510afefb8ec96034db04b4b/data/reference-quality.json) · [DESIGN.md](https://github.com/kwakseongjae/oh-my-design/blob/10be2098e9796b7f4510afefb8ec96034db04b4b/design-md/toss/DESIGN.md) · [LICENSE-NOTE.md](https://github.com/kwakseongjae/oh-my-design/blob/10be2098e9796b7f4510afefb8ec96034db04b4b/design-md/tving/assets/_reference/LICENSE-NOTE.md) · [README.md](https://github.com/kwakseongjae/oh-my-design/blob/10be2098e9796b7f4510afefb8ec96034db04b4b/benchmarks/ui-resolve-bench/README.md) · [quality.yml](https://github.com/kwakseongjae/oh-my-design/blob/10be2098e9796b7f4510afefb8ec96034db04b4b/.github/workflows/quality.yml) |

<a id="ux-design-how"></a>

### design.how (design-system-skills)

| Thuộc tính | Giá trị |
|---|---|
| Repo | https://github.com/arla6ka/design.how |
| License | MIT |
| Phiên bản đã đọc | `1ce5304466db2ba47a7a7524603e86df77c702bd` (commit 2026-11-17) |
| Kiểm chứng | 2026-11-23; code-read; đã đọc README.md, LICENSE, marketplace.json, 4 SKILL.md/criteria (design-system-boss, ui-review, build-design-system), check-system.mjs, capture-guard.mjs (phần đầu), taste.md, evals/run.mjs (phần đầu), README Quartz; không có .github; chưa chạy upstream |
| Mảng UX | đưa hệ thiết kế cho agent (hệ + skill đi kèm cài một lệnh) và chống lệch (check-system, ratchet allowlist) |
| Cơ chế đáng học | - `skills/design-system-boss/SKILL.md`: router đọc app, khớp 1 playbook, chép nguyên bước vào `.design-system/state.md`; bước bỏ phải ghi `skipped (<lý do>)`; ghi `roles.md` tách người viết khỏi người kiểm ('the writer never grades itself'); danh sách 'Never ship' (không commit trên nhánh gốc, không migrate khi chỉ nói 'fix it').<br>- `skills/build-design-system/scripts/check-system.mjs` (Node, không phụ thuộc): đọc cả thẻ JSX, có `--self-test`, allowlist chỉ co không phình (`--shrink-allowlist`), quy tắc chỉ tính khi đã thấy trượt trên mẫu cài (plant) trong phiên; mỗi điều cấm trong taste.md đi kèm một rule kiểm trong cùng thay đổi.<br>- `capture-guard.mjs` + `capture.mjs`: chụp màn hình thật ở 390 và 1280 sau một guard chặn mọi request ghi (`prove --writes` chạy khô trước khi mở trình duyệt), lưu cả accessibility tree để so before/after bằng `pixdiff.mjs` ở tolerance 0.<br>- `skills/ui-review/references/criteria.md`: 13 tiêu chí + mức blocking/should-fix/note; tiêu chí 13 (phản hồi dưới 100 ms qua Event Timing API) bắt buộc đo, ảnh chụp không đủ làm bằng chứng; finding phải có vị trí tìm lại được, vd `button 'Save changes' (settings-1280.png)`; finding dựa gu bị loại sang 'Left out'. |
| Tiêu chí và cách đo | Mã máy: check-system.mjs (rule có test tự thân + exit code 0/1/2), capture-guard (quyết định read/deny, thất bại nếu một write lọt), pixdiff. Do model chấm: 13 tiêu chí ui-review, panel nhiều reviewer thì gộp và loại nitpick. `evals/run.mjs` (đã mở phần mô tả) có `--lint` (frontmatter, độ dài 40-150 dòng, link, cấm em dash, từ trong glossary `_Avoid_`), `--triggers` (hỏi host skill nào kích hoạt cho từng prompt) và `--case` in ca sự cố để chạy tay; file tự nói nó chỉ chứng minh cụm quy tắc đã được viết ra, không chứng minh agent tuân theo. 18 ca sự cố trong evals/incidents/. |
| Giới hạn và rủi ro | Không có workflow CI. Playwright/Chromium bắt buộc cho chụp; make-font và make-logo kéo thêm Python (fonttools, potrace...) nên không cần cho mảng UX. Phần nhiều giá trị nằm ở các quy ước thẩm mỹ cá nhân của tác giả (taste.md: cấm chữ hoa, dấu chấm giữa, em dash, emoji, gradient là mặc định có thể thay). Số liệu 'migration' và chất lượng đầu ra của 4 hệ (Quartz...) là tuyên bố tác giả (chưa xác minh). License repo là MIT; riêng skill font/logo nói tạo font OFL và không chép đường nét, chưa kiểm sâu. |
| So với | designer-skills, design-dna, edenspiekermann-figma-ds-skills và component-contracts-figma (skill hệ thiết kế/Figma), shadcn-lint (cổng token bằng lint), ui-ux-pro-max |
| Nguồn | [README.md](https://github.com/arla6ka/design.how/blob/1ce5304466db2ba47a7a7524603e86df77c702bd/README.md) · [LICENSE](https://github.com/arla6ka/design.how/blob/1ce5304466db2ba47a7a7524603e86df77c702bd/LICENSE) · [marketplace.json](https://github.com/arla6ka/design.how/blob/1ce5304466db2ba47a7a7524603e86df77c702bd/.claude-plugin/marketplace.json) · [SKILL.md](https://github.com/arla6ka/design.how/blob/1ce5304466db2ba47a7a7524603e86df77c702bd/skills/design-system-boss/SKILL.md) · [SKILL.md](https://github.com/arla6ka/design.how/blob/1ce5304466db2ba47a7a7524603e86df77c702bd/skills/ui-review/SKILL.md) · [criteria.md](https://github.com/arla6ka/design.how/blob/1ce5304466db2ba47a7a7524603e86df77c702bd/skills/ui-review/references/criteria.md) · [SKILL.md](https://github.com/arla6ka/design.how/blob/1ce5304466db2ba47a7a7524603e86df77c702bd/skills/build-design-system/SKILL.md) · [check-system.mjs](https://github.com/arla6ka/design.how/blob/1ce5304466db2ba47a7a7524603e86df77c702bd/skills/build-design-system/scripts/check-system.mjs) · [capture-guard.mjs](https://github.com/arla6ka/design.how/blob/1ce5304466db2ba47a7a7524603e86df77c702bd/skills/build-design-system/scripts/capture-guard.mjs) · [taste.md](https://github.com/arla6ka/design.how/blob/1ce5304466db2ba47a7a7524603e86df77c702bd/skills/build-design-system/references/taste.md) · [run.mjs](https://github.com/arla6ka/design.how/blob/1ce5304466db2ba47a7a7524603e86df77c702bd/evals/run.mjs) · [README.md](https://github.com/arla6ka/design.how/blob/1ce5304466db2ba47a7a7524603e86df77c702bd/systems/quartz/README.md) |

<a id="ux-tinte"></a>

### Tinte

| Thuộc tính | Giá trị |
|---|---|
| Repo | https://github.com/Railly/tinte |
| License | MIT |
| Phiên bản đã đọc | `b30e72b9eafc2d3f4dcb53c15dfd9afdcdc144fa` (commit 2026-11-17) |
| Kiểm chứng | 2026-11-23; code-read; đã đọc README.md, LICENSE, CLAUDE.md, tinte.config.json, skills/tinte/SKILL.md, lint.ts, build.ts (từng đoạn), from.ts (đầu file), landing.md (đầu file), release.yml; chưa chạy upstream |
| Mảng UX | đưa định danh thiết kế cho agent (trích định danh từ trang, biên dịch thành skill + token) và chống lệch (lint màu) |
| Cơ chế đáng học | - `packages/cli/src/commands/build.ts`: `renderSkill` điền các slot `{{brand_name}} {{tokens_css_url}} {{type_scale}} {{voice_words}} {{brand_dos_donts}}` vào `assets/templates/landing.md`, chèn ghi chú 'inverted primary' khi cần, xuất `plugin.json` + `skills/<tên>-design/SKILL.md` + `references/tokens.css`; `bestContrast` chọn màu chữ trên nền token.<br>- `packages/cli/src/commands/lint.ts`: quét .tsx/.ts/.jsx/.js/.css/.html, 3 loại vi phạm (hex, rgb/hsl, lớp palette Tailwind như `bg-blue-500`), bỏ qua `tokens.css` và dòng có `tinte-ignore`, thoát 0/1/2, có `--json`.<br>- `tinte from`: `--emit-script` in script chụp style của trang sống, `--normalize` biến kết quả thành danh tính nháp (schema lỏng có ngưỡng chroma 0.09, top 10 màu theo diện tích); `tinte build` mới là cổng schema chặt.<br>- Template `landing.md`: thứ tự ưu tiên 6 mức khi yêu cầu xung đột (giữ sự kiện/giá, giữ khung dự án, rồi mới đến nhận diện), 'màu cứng là lỗi chứ không phải đường tắt', 'nếu không token nào hợp thì đổi bố cục, không đổi bảng màu'. |
| Tiêu chí và cách đo | Máy kiểm: `tinte lint` (regex theo dòng, không hiểu CSS cascade hay giá trị tính toán), có test (`lint.test.ts`, `build.test.ts`, `from.test.ts`). Do model: các quy tắc bố cục/giọng văn trong template. Không thấy eval đo agent có bám token hơn nhờ skill hay không. Workflow `release.yml` (đã mở) chỉ chạy bun test, build và publish npm khi version đổi; không có CI cho PR. |
| Giới hạn và rủi ro | Lint theo dòng bằng regex: bỏ sót màu qua biến JS, `currentColor`, tên màu CSS; dòng có `tinte-ignore` bị miễn. Skill `tinte` hướng dẫn `curl` ảnh thiết kế tới `ray.tinte.dev` (có chế độ AI gọi model) nên ảnh rời máy; và gọi API `tinte.dev` để cài preset (chưa xác minh bảo mật phía dịch vụ). Mục tiêu 13 token màu cố định kiểu Flexoki có thể không vừa hệ nhiều màu ngữ nghĩa. Template hiện là landing page, loại giao diện khác cần tự viết. |
| So với | tweakcn và designlang-design-extract/dembrandt (rút token từ trang), style-dictionary và design-tokens-community-group-dtcg (chuẩn token), shadcn-lint (lint token) |
| Nguồn | [README.md](https://github.com/Railly/tinte/blob/b30e72b9eafc2d3f4dcb53c15dfd9afdcdc144fa/README.md) · [LICENSE](https://github.com/Railly/tinte/blob/b30e72b9eafc2d3f4dcb53c15dfd9afdcdc144fa/LICENSE) · [CLAUDE.md](https://github.com/Railly/tinte/blob/b30e72b9eafc2d3f4dcb53c15dfd9afdcdc144fa/CLAUDE.md) · [tinte.config.json](https://github.com/Railly/tinte/blob/b30e72b9eafc2d3f4dcb53c15dfd9afdcdc144fa/tinte.config.json) · [SKILL.md](https://github.com/Railly/tinte/blob/b30e72b9eafc2d3f4dcb53c15dfd9afdcdc144fa/skills/tinte/SKILL.md) · [lint.ts](https://github.com/Railly/tinte/blob/b30e72b9eafc2d3f4dcb53c15dfd9afdcdc144fa/packages/cli/src/commands/lint.ts) · [build.ts](https://github.com/Railly/tinte/blob/b30e72b9eafc2d3f4dcb53c15dfd9afdcdc144fa/packages/cli/src/commands/build.ts) · [from.ts](https://github.com/Railly/tinte/blob/b30e72b9eafc2d3f4dcb53c15dfd9afdcdc144fa/packages/cli/src/commands/from.ts) · [landing.md](https://github.com/Railly/tinte/blob/b30e72b9eafc2d3f4dcb53c15dfd9afdcdc144fa/packages/cli/assets/templates/landing.md) · [release.yml](https://github.com/Railly/tinte/blob/b30e72b9eafc2d3f4dcb53c15dfd9afdcdc144fa/.github/workflows/release.yml) |

<a id="ux-craft-design-skills"></a>

### craft (diego3g)

| Thuộc tính | Giá trị |
|---|---|
| Repo | https://github.com/diego3g/craft |
| License | MIT |
| Phiên bản đã đọc | `a61231f83f6c299663858a25369681643aa14a6e` (commit 2026-11-23) |
| Kiểm chứng | 2026-11-23; code-read; đã đọc README.md, LICENSE, package.json, hooks (2 file), checks.mjs (đầu file), check-privacy.mjs (đầu file), craft/SKILL.md, craft-critique/SKILL.md, tests/scenarios/craft-critique/green.md; không có .github; chưa chạy upstream |
| Mảng UX | đưa brief thiết kế cho agent (DESIGN.md + hook SessionStart) và chống lệch (mã thắng brief, craft-sync, critique tự kiểm) |
| Cơ chế đáng học | - `hooks/session-start` + `hooks/hooks.json`: hook SessionStart (matcher `startup\|clear\|compact`) nhồi nội dung skill định tuyến `using-craft` vào ngữ cảnh mỗi phiên, bọc `<EXTREMELY_IMPORTANT>`; ý tưởng mượn từ obra/superpowers (README ghi MIT). Agent không có hook thì dán bảng định tuyến vào AGENTS.md.<br>- `skills/craft/SKILL.md`: đọc DESIGN.md (thiếu thì bắt buộc chạy craft-setup), chốt phạm vi bằng lời, với mỗi màn hình: craft-states (liệt kê trạng thái) -> tùy chọn craft-explore -> vẽ chỉ bằng thành phần/token của hệ -> craft-critique chế độ self-check; kết thúc ghi quyết định vào DESIGN.md. Có bảng 'Common mistakes' kiểu suy nghĩ-biện hộ/thực tế.<br>- `skills/craft-critique/SKILL.md`: render trước rồi mới nhận xét ('đọc HTML chưa đủ, người dùng thấy pixel'), 8 nhóm quy tắc, xếp theo tác động (chặn/làm chậm/trông cẩu thả), 3 chế độ review (chỉ báo cáo, không sửa) / refine / self-check; nếu hệ của dự án khác mặc định thì dự án thắng và chỉ ghi chú một lần.<br>- `scripts/checks.mjs` + `npm run check`: kiểm frontmatter, giới hạn 250 dòng/skill, link, và không để tên công cụ (mcp__..., get_jsx, write_html...) ngoài thư mục adapter, để skill không dính một công cụ thiết kế. |
| Tiêu chí và cách đo | Máy: `npm test` (test cho validator và hook) và `npm run check` (định dạng skill, link, tên công cụ). Không có CI GitHub trong repo. Chất lượng đầu ra do model chấm; bằng chứng là `tests/scenarios/<skill>/{baseline,green}.md` chạy kịch bản có/không có skill, ví dụ critique bắt đủ 6 lỗi gieo sẵn (nút loading đổi bề rộng, 3 primary, hover = selected, badge tương phản 2.2:1...). Đây là bản ghi tay của tác giả, nhiều lần không render được do sandbox, và vài chạy thất bại được ghi lại; coi là bằng chứng sơ bộ (chưa xác minh độc lập). |
| Giới hạn và rủi ro | Adapter Figma và đăng nhập OAuth của Penpot được README ghi là chưa kiểm trong chạy thật. Phụ thuộc hook SessionStart nên chỉ Claude Code/Cursor tự áp, agent khác phải dán tay. `scripts/check-privacy.mjs` là cổng cá nhân của tác giả (denylist và màu trùng token riêng), vô dụng với người khác. Hook nhồi một khối lớn vào mỗi phiên (chi phí ngữ cảnh). Các quy tắc thẩm mỹ chỉ là mặc định có thể bị hệ dự án ghi đè. |
| So với | designer-skills và huashu-design (bộ skill thiết kế nhiều bước), hallmark, ui-ux-pro-max |
| Nguồn | [README.md](https://github.com/diego3g/craft/blob/a61231f83f6c299663858a25369681643aa14a6e/README.md) · [LICENSE](https://github.com/diego3g/craft/blob/a61231f83f6c299663858a25369681643aa14a6e/LICENSE) · [package.json](https://github.com/diego3g/craft/blob/a61231f83f6c299663858a25369681643aa14a6e/package.json) · [hooks.json](https://github.com/diego3g/craft/blob/a61231f83f6c299663858a25369681643aa14a6e/hooks/hooks.json) · [session-start](https://github.com/diego3g/craft/blob/a61231f83f6c299663858a25369681643aa14a6e/hooks/session-start) · [checks.mjs](https://github.com/diego3g/craft/blob/a61231f83f6c299663858a25369681643aa14a6e/scripts/checks.mjs) · [check-privacy.mjs](https://github.com/diego3g/craft/blob/a61231f83f6c299663858a25369681643aa14a6e/scripts/check-privacy.mjs) · [SKILL.md](https://github.com/diego3g/craft/blob/a61231f83f6c299663858a25369681643aa14a6e/skills/craft/SKILL.md) · [SKILL.md](https://github.com/diego3g/craft/blob/a61231f83f6c299663858a25369681643aa14a6e/skills/craft-critique/SKILL.md) · [green.md](https://github.com/diego3g/craft/blob/a61231f83f6c299663858a25369681643aa14a6e/tests/scenarios/craft-critique/green.md) |

<a id="ux-json-render"></a>

### json-render (Vercel Labs)

| Thuộc tính | Giá trị |
|---|---|
| Repo | https://github.com/vercel-labs/json-render |
| License | Apache-2.0 |
| Phiên bản đã đọc | `372ae4f487d02bd2f591e94a84527de40f3938df` (commit 2026-11-23) |
| Kiểm chứng | 2026-11-23; code-read; đã đọc README.md, LICENSE, spec-validator.ts, actions.ts (phần đầu), server.ts, renderer.tsx (đoạn executeAction), shadcn catalog.ts (href), skills/core/SKILL.md (đầu file), ci.yml; chưa chạy upstream |
| Mảng UX | UI sinh động mức declarative (giữa controlled và open-ended); danh mục component được phép; MCP Apps |
| Cơ chế đáng học | - `packages/core` (`defineCatalog`, `schema.ts`, `prompt.ts`): catalog (Zod props + mô tả + actions) là nguồn duy nhất cho prompt, schema và kiểu; `catalog.validate()` được gọi trong tool MCP trước khi trả spec.<br>- `packages/core/src/spec-validator.ts`: `validateSpec` trả mã lỗi máy đọc (missing_root, root_not_found, missing_child, visible_in_props, on_in_props, orphaned_element...), nhắm các lỗi hay gặp của model.<br>- Hành động và dữ liệu động: `actions.ts` định nghĩa binding {action, params, confirm, onSuccess, onError}; `react/src/renderer.tsx` chỉ chạy action có trong map, tên lạ thì `console.warn('Unknown action')`; biểu thức giá trị chỉ là `$state/$bindState/$cond/$item` (không có eval).<br>- `packages/mcp/src/server.ts`: đăng ký tool + resource `ui://` mime `text/html;profile=mcp-app` qua `@modelcontextprotocol/ext-apps`, spec chạy trong iframe do host sandbox. `skills/core/SKILL.md` cũng có API thử nghiệm `experimental_composeSpec` để model chọn từ danh sách ứng viên có sẵn (gọi mô hình qua AI Gateway). |
| Tiêu chí và cách đo | Đo bằng máy ở mức cấu trúc: schema Zod + `validateSpec`; repo có nhiều test đơn vị (spec-validator.test.ts, props.test.ts...) và workflow `ci.yml` (đã mở) chạy version-sync, lint, build, test, kiểm mô hình Swift sinh tự động và fixture tương thích React/Swift (Linux và macOS). Không có eval chất lượng thẩm mỹ hay độ trung thực của model; 'Guardrailed/Predictable' trong README là tuyên bố của tác giả, đúng với ràng buộc cấu trúc chứ không đảm bảo đầu ra tốt hoặc an toàn. |
| Giới hạn và rủi ro | Catalog `Link` của gói shadcn có `href: z.string()` (catalog.ts) và component render `<a href={props.href ?? '#'}>`, chưa thấy ràng buộc scheme ở các file đã đọc nên người dùng nên tự giới hạn (chưa xác minh renderer có lọc `javascript:`). `server.ts` đặt CSP `resourceDomains` và `connectDomains` là `https:` (mọi host https) nên iframe MCP có thể kéo/gửi dữ liệu tới bất kỳ máy chủ https nào; nên siết lại. API `experimental_*` gọi dịch vụ model ngoài bằng `AI_GATEWAY_API_KEY` (dữ liệu rời máy). Là thư viện nên giới hạn bảo mật phụ thuộc cách đặt catalog và action của người tích hợp. Rất nhiều gói (khoảng 35) nên bề mặt bảo trì lớn. |
| So với | a2ui (giao thức declarative, json-render dùng catalog riêng chứ không theo A2UI), openui-thesys, tambo, copilotkit (controlled/MCP Apps) |
| Nguồn | [README.md](https://github.com/vercel-labs/json-render/blob/372ae4f487d02bd2f591e94a84527de40f3938df/README.md) · [LICENSE](https://github.com/vercel-labs/json-render/blob/372ae4f487d02bd2f591e94a84527de40f3938df/LICENSE) · [spec-validator.ts](https://github.com/vercel-labs/json-render/blob/372ae4f487d02bd2f591e94a84527de40f3938df/packages/core/src/spec-validator.ts) · [actions.ts](https://github.com/vercel-labs/json-render/blob/372ae4f487d02bd2f591e94a84527de40f3938df/packages/core/src/actions.ts) · [server.ts](https://github.com/vercel-labs/json-render/blob/372ae4f487d02bd2f591e94a84527de40f3938df/packages/mcp/src/server.ts) · [renderer.tsx](https://github.com/vercel-labs/json-render/blob/372ae4f487d02bd2f591e94a84527de40f3938df/packages/react/src/renderer.tsx) · [catalog.ts](https://github.com/vercel-labs/json-render/blob/372ae4f487d02bd2f591e94a84527de40f3938df/packages/shadcn/src/catalog.ts) · [SKILL.md](https://github.com/vercel-labs/json-render/blob/372ae4f487d02bd2f591e94a84527de40f3938df/skills/core/SKILL.md) · [ci.yml](https://github.com/vercel-labs/json-render/blob/372ae4f487d02bd2f591e94a84527de40f3938df/.github/workflows/ci.yml) |

<a id="ux-copilotkit-generative-ui"></a>

### CopilotKit/generative-ui (hướng dẫn ba kiểu)

| Thuộc tính | Giá trị |
|---|---|
| Repo | https://github.com/CopilotKit/generative-ui |
| License | không có file LICENSE |
| Phiên bản đã đọc | `12aa81e3deeb9c6c15c7863b67a3f8f63144e383` (commit 2026-03-21) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md; repo chỉ có README và tài sản ảnh/PDF, không có LICENSE và không có .github; chưa chạy upstream |
| Mảng UX | UI sinh động: ba mức kiểm soát (controlled / declarative / open-ended) và giao thức (AG-UI, A2UI, MCP Apps) |
| Cơ chế đáng học | - README, mục 'The 3 Types': controlled = bạn dựng sẵn component, agent chọn cái nào và đưa dữ liệu (ví dụ `useFrontendTool` có `render` theo trạng thái inProgress/executing/complete); declarative = agent trả cấu trúc (A2UI JSONL gồm `surfaceUpdate`, `dataModelUpdate`, `beginRendering`); open-ended = agent trả cả bề mặt (HTML/iframe), renderer chỉ là khung chứa.<br>- README nêu thẳng đánh đổi của open-ended: rủi ro bảo mật/hiệu năng khi render nội dung tùy ý, kiểu dáng không nhất quán, kém di động ngoài web; và xếp AG-UI làm lớp tương tác hai chiều bên dưới cả ba kiểu (cũng là nơi README tự gán AG-UI vừa là 'kiểu controlled' vừa là lớp runtime chung, nên khái niệm hơi chồng).<br>- Ví dụ MCP Apps: `MCPAppsMiddleware` từ `@ag-ui/mcp-apps-middleware` nối agent với máy chủ MCP (Excalidraw); ví dụ `useComponent` với `widgetRenderer` nhận `{title, description, html}` và nói render 'trong iframe sandbox' (chi tiết sandbox nằm ở repo OpenGenerativeUI, chưa đọc). |
| Tiêu chí và cách đo | Không có rubric hay máy kiểm: đây là tài liệu khái niệm cộng đoạn mã minh họa, một số đánh dấu 'illustrative' (Open-JSON-UI). Không chạy được trong repo này vì không có mã dự án. Không có eval so sánh ba mức. |
| Giới hạn và rủi ro | Là bài viết của nhà bán sản phẩm; nội dung phụ thuộc CopilotKit/AG-UI và nhiều liên kết ra ngoài (blog, video) chưa đọc. Không có file LICENSE nên không rõ quyền dùng lại văn bản/ảnh/PDF (license: null). Mã trong README chỉ là đoạn minh họa, không phải bản đã kiểm. Phần sandbox/bảo mật của open-ended chỉ được nhắc ở mức cảnh báo, không có cấu hình cụ thể. |
| So với | ag-ui, a2ui, copilotkit (hồ sơ sản phẩm), awesome-generative-ui (danh mục) |
| Nguồn | [README.md](https://github.com/CopilotKit/generative-ui/blob/12aa81e3deeb9c6c15c7863b67a3f8f63144e383/README.md) |

<a id="ux-agenui"></a>

### AGenUI

| Thuộc tính | Giá trị |
|---|---|
| Repo | https://github.com/AGenUI/AGenUI |
| License | Apache-2.0 (mã AGenUI); NOTICE liệt kê thành phần bên thứ ba LGPL v2.1 (iksemel, sax) |
| Phiên bản đã đọc | `02462d09ff4a6c9d4914654cd6162f2ce2a7bdad` (commit 2026-11-23) |
| Kiểm chứng | 2026-11-23; code-read; đã đọc README.md, LICENSE, NOTICE, a2ui-generation/SKILL.md, validate_a2ui.py (đầu file và phần kiểm URL), component-catalog.md (mục Web), ci-android.yml, pages-privacy.yml; chưa chạy upstream |
| Mảng UX | UI sinh động mức declarative (A2UI) trên native; danh mục component; allowlist; kiểm bằng script |
| Cơ chế đáng học | - Catalog + allowlist: `skills/a2ui-generation/SKILL.md` cấm bịa tên component (Container, Stack, Badge... phải đổi sang Card/Column/Text có style) và `validate_a2ui.py` có `ALLOWED_COMPONENTS` và `ALLOWED_COMMON_STYLE_KEYS` làm bộ lọc cứng; `agenui_catalog.json` là schema catalog tự chứa dùng trong đàm phán `supportedCatalogIds`.<br>- Cổng thẻ cứng trong SKILL.md: mục chính ≤ 3, không List mẫu động, không ảnh hero rộng hết cỡ, thân ≤ 2 đoạn, tổng chiều cao ≤ 2/3 màn hình, Row tối đa 3 con, CTA và nhóm tag phải ở hàng riêng; thẻ tra cứu giữ cấu trúc Tiêu đề -> 1-3 thuộc tính -> tóm tắt ≤ 2 dòng -> tag -> CTA.<br>- Quy trình có vòng kiểm: nêu lý do bố cục -> bản nháp -> ít nhất một lần cải thiện rõ ràng -> ghi file -> chạy `validate_a2ui.py` tới khi qua -> review thiết kế bằng model -> chạy lại script; ngoại lệ theo yêu cầu người dùng đi qua `overrides.json` phạm vi tối thiểu. Thứ tự bắt buộc `updateComponents` rồi `updateDataModel`.<br>- Phân tách an toàn bố cục/dữ liệu: component dùng `{"path": ...}` ràng buộc dữ liệu và template dùng đường dẫn tương đối; hành động chỉ qua `Button + action` thật, cấm nút giả. |
| Tiêu chí và cách đo | Mã máy: `validate_a2ui.py` (trả danh sách lỗi; chạy cả kiểm URL ảnh/media có tồn tại) và test C++/tích hợp trong tests/; CI (ci-android.yml đã mở) chỉ build Android khi đổi các đường dẫn liên quan, các workflow ios/harmony chưa mở. Do model chấm: review thiết kế theo `reference/design-review.md`. Không có eval đo chất lượng thiết kế giữa các model; README khuyên tự thử nhiều model. 'Giữ 120 fps' là tuyên bố của tác giả (chưa xác minh). |
| Giới hạn và rủi ro | `validate_a2ui.py::_check_url_reachable` dùng `urlopen` GET tới mọi URL do model sinh trong dữ liệu (kèm Range), nghĩa là chạy skill trên máy dev có thể gọi tới URL tùy ý, kể cả mạng nội bộ nếu model xuất ra (rủi ro SSRF phía công cụ phát triển). Component `Web` nhận `source` là URL hoặc chuỗi HTML và `RichText` render HTML, cần siết ở app chủ (chưa đọc triển khai native nên chưa xác minh có sandbox). NOTICE liệt kê thành phần LGPL v2.1 có mã nguồn đặt trong repo nên người nhúng cần xét điều kiện LGPL. Dự án tự ghi 'đang phát triển nhanh'; khó dùng nếu mục tiêu là web. |
| So với | a2ui (đặc tả gốc), json-render (cùng mức declarative nhưng catalog riêng, đa nền web), openui-thesys |
| Nguồn | [README.md](https://github.com/AGenUI/AGenUI/blob/02462d09ff4a6c9d4914654cd6162f2ce2a7bdad/README.md) · [LICENSE](https://github.com/AGenUI/AGenUI/blob/02462d09ff4a6c9d4914654cd6162f2ce2a7bdad/LICENSE) · [NOTICE](https://github.com/AGenUI/AGenUI/blob/02462d09ff4a6c9d4914654cd6162f2ce2a7bdad/NOTICE) · [SKILL.md](https://github.com/AGenUI/AGenUI/blob/02462d09ff4a6c9d4914654cd6162f2ce2a7bdad/skills/a2ui-generation/SKILL.md) · [validate_a2ui.py](https://github.com/AGenUI/AGenUI/blob/02462d09ff4a6c9d4914654cd6162f2ce2a7bdad/skills/a2ui-generation/scripts/validate_a2ui.py) · [component-catalog.md](https://github.com/AGenUI/AGenUI/blob/02462d09ff4a6c9d4914654cd6162f2ce2a7bdad/skills/a2ui-generation/reference/component-catalog.md) · [ci-android.yml](https://github.com/AGenUI/AGenUI/blob/02462d09ff4a6c9d4914654cd6162f2ce2a7bdad/.github/workflows/ci-android.yml) · [pages-privacy.yml](https://github.com/AGenUI/AGenUI/blob/02462d09ff4a6c9d4914654cd6162f2ce2a7bdad/.github/workflows/pages-privacy.yml) |

<a id="ux-pi-generative-ui"></a>

### pi-generative-ui

| Thuộc tính | Giá trị |
|---|---|
| Repo | https://github.com/Michaelliv/pi-generative-ui |
| License | không có file LICENSE |
| Phiên bản đã đọc | `d1abf2cb38fbf54c4b91d06677c700193d495887` (commit 2026-06-04) |
| Kiểm chứng | 2026-11-23; code-read; đã đọc README.md, package.json, CHANGELOG.md, index.ts, rpc.ts, session.ts (đầu file), morph.ts, CORE.md (đầu file), test.yml; không có LICENSE; chưa chạy upstream |
| Mảng UX | UI sinh động mức open-ended (HTML/JS do model sinh, render trong cửa sổ WebView) và rủi ro sandbox |
| Cơ chế đáng học | - `.pi/extensions/generative-ui/index.ts`: bắt các sự kiện stream `toolcall_start/delta/end` của tool `show_widget` để mở `WidgetSession` sớm và đẩy HTML từng phần (debounce 150 ms, `session.ts`); tool resolve ngay khi HTML cuối đến, cửa sổ vẫn mở cho người dùng.<br>- `runtime/morph.ts`: morphdom cập nhật DOM giữ danh tính, script nằm chờ rồi `runScripts` chạy tuần tự đúng một lần ở chunk cuối (script ngoài phải load xong mới chạy script nội tuyến sau nó, tránh ReferenceError với Chart.js/D3).<br>- `rpc.ts` + giao thức JSON có kiểu: widget chỉ gọi được các RPC đã đăng ký (svg.copy/svg.save); mọi tin nhắn không đúng giao thức bị bỏ, widget là display-only, agent không nhận lại click hay input.<br>- `claude-guidelines/CORE.md` và 5 module (interactive, chart, mockup, art, diagram, tổng cỡ khoảng 72K): luật thiết kế 'flat, compact, văn bản ra ngoài tool', ngân sách độ phức tạp cứng (phụ đề hộp ≤ 5 từ, ≤ 2 dải màu, ≤ 4 hộp ngang), thiết kế an toàn khi stream (style inline trước, script cuối, tránh gradient/blur). |
| Tiêu chí và cách đo | Không có rubric chấm giao diện. Kiểm máy chỉ cho hạ tầng: vitest (giao thức, RPC, phiên, shim nền tảng) và `test.yml` (đã mở) typecheck, build bundle, kiểm bundle commit khớp mã nguồn trên macOS/Linux/Windows x Node 20/22; test tích hợp thật chỉ chạy trên macOS. Không có eval cho chất lượng widget hay độ an toàn. |
| Giới hạn và rủi ro | Không thấy sandbox hay CSP trong mã (grep Content-Security-Policy/sandbox cho kết quả rỗng trên ts/mjs/json; shell HTML trong `build.mjs` chỉ có charset và viewport): HTML/JS do model sinh chạy với toàn quyền trình duyệt trong WebView và tải script từ mọi URL, nên prompt injection có thể kéo mã ngoài hoặc gọi mạng; dòng 'CSP-enforced' trong guidelines không phản ánh repo này. License: không có LICENSE, chỉ README/package.json ghi MIT; hơn nữa hướng dẫn sao nguyên văn từ công cụ của Anthropic (trích qua xuất hội thoại) nên quyền phân phối lại văn bản đó chưa rõ. Cài đặt biên dịch binary native khi postinstall. Phụ thuộc framework `pi` còn mới (phiên bản 0.3.0 'unreleased' trong CHANGELOG). |
| So với | copilotkit (mức open-ended qua MCP Apps/useComponent), a2ui (mức declarative để so), tambo; về luật thiết kế widget có thể đối chiếu frontend-design-anthropic |
| Nguồn | [README.md](https://github.com/Michaelliv/pi-generative-ui/blob/d1abf2cb38fbf54c4b91d06677c700193d495887/README.md) · [package.json](https://github.com/Michaelliv/pi-generative-ui/blob/d1abf2cb38fbf54c4b91d06677c700193d495887/package.json) · [CHANGELOG.md](https://github.com/Michaelliv/pi-generative-ui/blob/d1abf2cb38fbf54c4b91d06677c700193d495887/CHANGELOG.md) · [index.ts](https://github.com/Michaelliv/pi-generative-ui/blob/d1abf2cb38fbf54c4b91d06677c700193d495887/.pi/extensions/generative-ui/index.ts) · [rpc.ts](https://github.com/Michaelliv/pi-generative-ui/blob/d1abf2cb38fbf54c4b91d06677c700193d495887/.pi/extensions/generative-ui/rpc.ts) · [session.ts](https://github.com/Michaelliv/pi-generative-ui/blob/d1abf2cb38fbf54c4b91d06677c700193d495887/.pi/extensions/generative-ui/session.ts) · [morph.ts](https://github.com/Michaelliv/pi-generative-ui/blob/d1abf2cb38fbf54c4b91d06677c700193d495887/.pi/extensions/generative-ui/runtime/morph.ts) · [CORE.md](https://github.com/Michaelliv/pi-generative-ui/blob/d1abf2cb38fbf54c4b91d06677c700193d495887/.pi/extensions/generative-ui/claude-guidelines/CORE.md) · [test.yml](https://github.com/Michaelliv/pi-generative-ui/blob/d1abf2cb38fbf54c4b91d06677c700193d495887/.github/workflows/test.yml) |

<a id="ux-shadcn-chatbot-kit"></a>

### shadcn-chatbot-kit (Blazity)

| Thuộc tính | Giá trị |
|---|---|
| Repo | https://github.com/Blazity/shadcn-chatbot-kit |
| License | MIT |
| Phiên bản đã đọc | `fe32b9241dacbfe7b7149c7914812d35139a693f` (commit 2026-02-27) |
| Kiểm chứng | 2026-11-23; code-read; đã đọc README.md, LICENSE.md, chat-message.tsx, markdown-renderer.tsx (đầu file), apps/www/package.json (grep phụ thuộc), code-check.yml; chưa chạy upstream |
| Mảng UX | giao diện chat/agent chrome (controlled), hiển thị trạng thái tool; không phải UI sinh động |
| Cơ chế đáng học | - `apps/www/registry/default/ui/chat-message.tsx`: nhận `parts` (text, reasoning, tool-invocation) hoặc `toolInvocations` kiểu cũ, ba trạng thái tool (`partial-call`, `call`, `result`) và biến thể animation (none/slide/scale/fade) bằng `cva`; chỉ định nghĩa hiển thị, quyền gọi tool nằm ở backend.<br>- `markdown-renderer.tsx`: `react-markdown` + `remark-gfm`, highlight bằng shiki, mặc định react-markdown không render HTML thô nên nội dung model xuất ra đi qua Markdown (chưa kiểm cấu hình runtime).<br>- Phân phối bằng registry của shadcn (`registry/default/ui`), người dùng sở hữu mã và chỉnh bằng biến CSS; có trang theme customizer. |
| Tiêu chí và cách đo | Không có rubric thiết kế hay a11y tự động trong phần đã đọc. Workflow `code-check.yml` (đã mở) chạy pnpm lint và format check khi PR (Node 18); không thấy test component hay kiểm a11y. Danh sách 'Features' trong README là tuyên bố của tác giả. |
| Giới hạn và rủi ro | Bám `ai` 4.3.x và kiểu `toolInvocations`; AI SDK sau đó đổi mô hình message-part nên cần chuyển đổi khi nâng cấp (chưa kiểm). Một số tính năng ghi WIP. Không giải quyết sandbox hay danh mục component cho UI do model sinh. Chưa thấy chống chèn nội dung đặc biệt ngoài mặc định của react-markdown. Site docs `apps/www` có `analytics.tsx` (chưa mở), không thuộc phần component cài về. |
| So với | assistant-ui và vercel-ai-sdk (hạ tầng chat), shadcn-ui (nền component), tambo (UI sinh động ở mức component dựng sẵn) |
| Nguồn | [README.md](https://github.com/Blazity/shadcn-chatbot-kit/blob/fe32b9241dacbfe7b7149c7914812d35139a693f/README.md) · [LICENSE.md](https://github.com/Blazity/shadcn-chatbot-kit/blob/fe32b9241dacbfe7b7149c7914812d35139a693f/LICENSE.md) · [chat-message.tsx](https://github.com/Blazity/shadcn-chatbot-kit/blob/fe32b9241dacbfe7b7149c7914812d35139a693f/apps/www/registry/default/ui/chat-message.tsx) · [markdown-renderer.tsx](https://github.com/Blazity/shadcn-chatbot-kit/blob/fe32b9241dacbfe7b7149c7914812d35139a693f/apps/www/registry/default/ui/markdown-renderer.tsx) · [package.json](https://github.com/Blazity/shadcn-chatbot-kit/blob/fe32b9241dacbfe7b7149c7914812d35139a693f/apps/www/package.json) · [code-check.yml](https://github.com/Blazity/shadcn-chatbot-kit/blob/fe32b9241dacbfe7b7149c7914812d35139a693f/.github/workflows/code-check.yml) |

<a id="n2-2026-11-24"></a>

## Nâng trần đợt hai — 23/11/2026

Hồ sơ lập trong đợt nâng trần thứ hai: đọc mã hoặc tài liệu tại commit cố định, chưa chạy upstream; mô tả của trinh sát sai ở nhiều repo nên điều ghi ở đây là điều đã đọc.

<a id="n2-signoff-ui"></a>

### signoff-ui

| Thuộc tính | Giá trị |
|---|---|
| Repo | https://github.com/dgesteves/signoff-ui |
| License | MIT |
| Phiên bản đã đọc | `de69d2ce5e0d928443c6eb9582cb36ab78366938` (commit 2026-11-16) |
| Kiểm chứng | 2026-11-24; code-read; đã đọc README, LICENSE, SECURITY.md, lib/policy.ts, lib/risk.ts, vitest.config.ts và ci.yml; chưa chạy upstream |
| Khoảng trống lấp | UI người-trong-vòng cho agent: duyệt diff nhiều file và duyệt lệnh, trả kết quả để agent hành động (AI SDK, AG-UI, ACP) |
| Cơ chế đáng học | (1) Quy tắc duyệt có phạm vi: allow-once, allow-session, allow-always, deny-once, deny-always; luật deny thắng luật allow (`lib/policy.ts`). (2) Glob của luật allow dừng ở toán tử shell, nên `npm test*` cho `npm test -- --watch` nhưng không cho `npm test && rm -rf ~`; luật deny tách từng lệnh trong dòng shell, kể cả trong dấu nháy (`lib/policy.ts`). (3) Mức rủi ro từ chú thích MCP: destructive thành high, readOnly thành low, không đoán khi thiếu gợi ý, và nêu rõ đó chỉ là gợi ý không được dùng để tự duyệt (`lib/risk.ts`). |
| Tiêu chí và cách kiểm | CI (đã mở) chạy format, lint không cảnh báo, typecheck, vitest với ngưỡng phủ statements 92, branches 87, functions 92, lines 94, ngân sách kích thước bundle, perf diff trên Chrome, axe a11y hai chủ đề, audit phụ thuộc mức moderate, smoke Next.js, assistant-ui, CopilotKit. 106 file trong thư mục test. Chưa chạy lại. |
| Giới hạn và rủi ro | Phiên bản 0.14.1 nên API còn đổi. Yêu cầu Node 24 trở lên và pnpm; thành phần React nên cần Tailwind hoặc CSS đi kèm. Số sao do trinh sát ghi (16) chưa kiểm. Chỉ là lớp giao diện, hiệu lực chặn hành động phụ thuộc việc server của người dùng thực sự dừng chờ phản hồi. SECURITY.md liệt kê duyệt gửi không do người dùng bấm là lỗ hổng. |
| So với | CopilotKit, assistant-ui (kit chat, chỉ diff từng file, không trả kết quả duyệt), json-render |
| Nguồn | [README.md](https://github.com/dgesteves/signoff-ui/blob/de69d2ce5e0d928443c6eb9582cb36ab78366938/README.md) · [LICENSE](https://github.com/dgesteves/signoff-ui/blob/de69d2ce5e0d928443c6eb9582cb36ab78366938/LICENSE) · [SECURITY.md](https://github.com/dgesteves/signoff-ui/blob/de69d2ce5e0d928443c6eb9582cb36ab78366938/SECURITY.md) · [policy.ts](https://github.com/dgesteves/signoff-ui/blob/de69d2ce5e0d928443c6eb9582cb36ab78366938/packages/signoff-ui/src/lib/policy.ts) · [risk.ts](https://github.com/dgesteves/signoff-ui/blob/de69d2ce5e0d928443c6eb9582cb36ab78366938/packages/signoff-ui/src/lib/risk.ts) · [vitest.config.ts](https://github.com/dgesteves/signoff-ui/blob/de69d2ce5e0d928443c6eb9582cb36ab78366938/packages/signoff-ui/vitest.config.ts) · [ci.yml](https://github.com/dgesteves/signoff-ui/blob/de69d2ce5e0d928443c6eb9582cb36ab78366938/.github/workflows/ci.yml) |

<a id="n2-lingo-dev"></a>

### Lingo.dev

| Thuộc tính | Giá trị |
|---|---|
| Repo | https://github.com/lingodotdev/lingo.dev |
| License | Apache-2.0 |
| Phiên bản đã đọc | `b3fba7d0272d139176064a9162a834bdace0712a` (commit 2026-11-20) |
| Kiểm chứng | 2026-11-24; code-read; đã đọc readme.md, packages/cli/package.json, lockfile.ts, observability.ts, settings.ts, pr-check.yml, i18n.json, i18n.lock; chưa chạy upstream |
| Khoảng trống lấp | Bản địa hóa tài liệu (i18n/l10n) và đồng bộ bản dịch |
| Cơ chế đáng học | - `lockfile.ts` băm MD5 từng giá trị nguồn theo mẫu đường dẫn; `extractUpdatedData` chỉ chọn khóa có checksum lệch, nên chỉ dịch lại phần đổi.<br>- `i18n.json` mô tả locale nguồn, đích và bucket kèm `lockedKeys` và `ignoredKeys` (xem `packages/cli/i18n.json`).<br>- Chính repo tự dùng: `pr-check.yml` chạy build, test và `pnpm changeset status --since origin/main` để bắt buộc có changeset.<br>- Readme mô tả lớp glossary, rules, brand voice, AI reviewer (GEMBA, BERTScore) là tính năng nền tảng đám mây (chưa xác minh trong mã, phần này không nằm trong packages đã mở). |
| Tiêu chí và cách kiểm | Không có chấm điểm chất lượng thuật ngữ tiếng Việt nào trong repo đã đọc; điểm chặn duy nhất kiểm được bằng máy là checksum khóa và test spec cạnh mã. Chất lượng dịch phụ thuộc mô hình phía dịch vụ (chưa xác minh). Cần tự kiểm thuật ngữ tiếng Việt bằng glossary riêng. |
| Giới hạn và rủi ro | Apache-2.0 cho mã. Telemetry: `observability.ts` gửi sự kiện tới PostHog (eu.i.posthog.com) kèm email khi đã đăng nhập, ID tổ chức git hoặc ID máy; tắt bằng DO_NOT_TRACK=1. Dịch cần LINGO_API_KEY tới api.lingo.dev nên nội dung nguồn rời máy. Repo đang chuyển trọng tâm sang nền tảng nên bề mặt CLI có thể đổi (cờ deprecated trong settings.ts). |
| So với | Weblate (tự host, quản lý dịch có người), i18next (thư viện runtime, không dịch tự động), kiss-translator: Lingo.dev là lớp dịch tự động chạy trong CI |
| Nguồn | [LICENSE.md](https://github.com/lingodotdev/lingo.dev/blob/b3fba7d0272d139176064a9162a834bdace0712a/LICENSE.md) · [readme.md](https://github.com/lingodotdev/lingo.dev/blob/b3fba7d0272d139176064a9162a834bdace0712a/readme.md) · [package.json](https://github.com/lingodotdev/lingo.dev/blob/b3fba7d0272d139176064a9162a834bdace0712a/packages/cli/package.json) · [lockfile.ts](https://github.com/lingodotdev/lingo.dev/blob/b3fba7d0272d139176064a9162a834bdace0712a/packages/cli/src/cli/utils/lockfile.ts) · [observability.ts](https://github.com/lingodotdev/lingo.dev/blob/b3fba7d0272d139176064a9162a834bdace0712a/packages/cli/src/cli/utils/observability.ts) · [settings.ts](https://github.com/lingodotdev/lingo.dev/blob/b3fba7d0272d139176064a9162a834bdace0712a/packages/cli/src/cli/utils/settings.ts) · [pr-check.yml](https://github.com/lingodotdev/lingo.dev/blob/b3fba7d0272d139176064a9162a834bdace0712a/.github/workflows/pr-check.yml) |
