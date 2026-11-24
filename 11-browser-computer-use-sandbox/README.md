# 11 · Browser Agents, Computer Use & Agent Sandboxes

> Agent thao tác trình duyệt/máy tính và hạ tầng chạy code an toàn cho agent.

## 1. Browser agents / automation cho LLM

| Dự án | Repo | License | ★ (2026) | Cách hoạt động | Ghi chú |
|---|---|---|---|---|---|
| **Browser Use** | browser-use/browser-use | MIT | ~118k (13/10/2026) | Agent Python điều khiển Chromium qua CDP (bỏ Playwright), DOM + accessibility + vision | Lớn nhất; có cloud; telemetry bật mặc định, xem §1c |
| **agent-browser** (Vercel Labs) | vercel-labs/agent-browser | Apache-2.0 | ~29.5k (45k ngày 31/10, §1h.2) | CLI Rust cho agent điều khiển trình duyệt | Mới, tăng nhanh |
| **Stagehand** (Browserbase) | browserbase/stagehand | MIT | ~25.6k | SDK `act/extract/observe`, v4 dùng CDP trực tiếp (không Playwright) | Tích hợp Claude Code, Codex, Mastra |
| **Skyvern** | Skyvern-AI/skyvern | AGPL-3.0 | – | Vision + LLM, workflow form | |
| **Playwright MCP** | microsoft/playwright-mcp | Apache-2.0 | – | MCP server, làm việc trên accessibility tree (không screenshot) | Server MCP phổ biến nhất nhóm browser |
| **Steel / Browserbase / Hyperbrowser** | – | – | – | Browser-as-a-service cho agent | Hạ tầng |
| **Expect / Passmark** | – | – | – | AI testing trên browser | QA |

**Nhận định:** DOM/accessibility-tree rẻ và ổn định hơn vision; vision cần cho canvas/ứng dụng lạ. Chọn Browser Use để thử nhanh, Stagehand khi cần SDK có kiểm soát trong TypeScript.

## 1b. Framework E2E test dùng agent: `tester-army/e2e` (ảnh người dùng gửi, 2026-10-13)

> Ảnh social card GitHub "e2e — Next generation e2e testing framework for web and mobile apps" (35 contributor, used by 640, 9k★, 434 fork). Đã clone nông repo (HEAD `fc90644`, 12/10/2026) để đọc README, `AGENTS.md`, `SECURITY.md`, `docs/` và workflow CI.

### e2e (TesterArmy)

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/tester-army/e2e · docs https://e2e.tester.army/docs · npm `e2e` |
| Mô tả 1 dòng | Framework E2E TypeScript cho web (chạy trên Playwright) và mobile (iOS simulator, Android emulator qua agent-device): trong cùng một test vừa có bước agent bằng ngôn ngữ tự nhiên (`agent.act`, `agent.assert`, `agent.waitFor`, `agent.extract`), vừa có locator và `expect` kiểu Playwright |
| Loại | browser-agent / e2e-testing |
| License | Apache-2.0 (NOTICE: © 2026 TesterArmy, Inc.) |
| ★ (ngày) | ~9,7k★, 462 fork, 107 issue mở (13/10/2026, trang GitHub + shields.io); ảnh ghi 9k★/434 fork. Repo tạo 22/7/2026, push cuối 12/10/2026; khoảng 6,8k★ vào 6/10 theo bài về v0.18 (blog) → tăng nhanh sau khi ra mắt công khai đầu 10/2026 |
| Vì sao đáng tham khảo | • **Cache phát lại đã kiểm** (`docs/cache.mdx`): chỉ lưu thao tác của `agent.act()` sau khi một bước kiểm sau đó xác nhận kết quả; lần chạy sau phát lại không gọi model; khi control hoặc trạng thái cuối không còn khớp thì giao lại cho agent; bản ghi nào dẫn tới lỗi thì bị xoá. Đây là cách giữ test agent rẻ và lặp lại được.<br>• Trộn bước agent với assertion tất định trong một test, nên phần cần chính xác (giá, trạng thái) vẫn kiểm bằng locator.<br>• Một API cho web và mobile; tích hợp chạy trên hạ tầng thuê (Kernel, Limrun, EAS, smol microVM), reporter GitHub PR, MCP server, skill cho coding agent; tài liệu đóng gói kèm npm để agent đọc offline.<br>• Model tự chọn qua Vercel AI SDK (BYO key); có hướng dẫn chuyển từ Playwright, Cypress, Selenium, Detox, Maestro.<br>• `AGENTS.md` theo nguyên tắc "code là hợp đồng": `d.ts` công khai, schema fixture, test đối chiếu mã lỗi với docs; Action trong CI ghim theo SHA |
| Hạn chế / rủi ro | • **Pre-1.0** (gói `e2e` 0.20.0), API còn đổi; repo công khai chưa tới 3 tháng.<br>• **Telemetry bật mặc định** (PostHog EU; tắt bằng `e2e telemetry disable`, `E2E_TELEMETRY_DISABLED=1` hoặc `DO_NOT_TRACK=1`); docs nói không gửi nội dung test hay credential.<br>• `docs/security.mdx` tự nêu: `Secret` được che trong log/prompt nhưng **video và file tải về không che**; **bản ghi cache commit vào repo lưu giá trị đã gõ nguyên văn** (trừ secret); `basicAuth` trả lời 401 từ mọi origin; **không có allowlist origin**; test chạy với quyền hệ điều hành, **không sandbox** → chạy PR không tin cậy trong sandbox ngoài, không secret.<br>• Đăng nhập bằng thuê bao (ChatGPT, Copilot, OpenCode, SuperGrok qua OAuth, `docs/subscriptions.mdx`) có thể vướng điều khoản nhà cung cấp **(chưa xác minh)**.<br>• Tên npm `e2e` tạo từ 2014, nhiều khả năng được chuyển nhượng **(chưa xác minh)** → kiểm publisher trước khi cài.<br>• Công ty YC P26 (Oskar Kwaśniewski, Szymon Rybczak); con số "50+ khách trả phí, gọi vốn $1,2M" chỉ có trên LinkedIn **(chưa xác minh)** |
| Tích hợp | `npm i -D e2e` (ghim phiên bản, kiểm publisher `tester-army`); đặt `E2E_TELEMETRY_DISABLED=1` trong CI; dùng tài khoản test riêng và dữ liệu giả vì video/cache không che; không commit cache nếu form có dữ liệu thật; chạy trong container/VM không secret cho PR từ fork; vẫn giữ assertion tất định cho luồng tiền/quyền. Dự án đã có Playwright + axe (mục 13) có thể thử e2e cho luồng UI hay đổi, giữ Playwright cho cổng a11y/hiệu năng |
| Liên quan | mục 11 §1 (Stagehand, Playwright MCP), mục 13 (Playwright CI, Lighthouse CI, axe), mục 07 (eval), mục 12 (secret, sandbox) |
| Nguồn | xem §4 và `SOURCES.md` (13/10/2026) |

### So sánh với lựa chọn cùng loại (★ qua shields.io, 13/10/2026)

| Dự án | ★ | License | Commit gần nhất | Cách tiếp cận | Khác e2e ở đâu |
|---|---|---|---|---|---|
| **microsoft/playwright** | ~98k | Apache-2.0 | 12/10/2026 | Test tất định bằng locator, đa trình duyệt | Không có bước agent; nền web của e2e |
| **browserbase/stagehand** | ~26k | MIT | 12/10/2026 | SDK `act/extract/observe`, có cache tự phát lại | Thư viện tự động hoá trình duyệt, không phải test runner; chỉ web |
| **mobile-dev-inc/Maestro** | ~16k | Apache-2.0 | 12/10/2026 | Flow YAML cho mobile và web | Tất định là chính; tính năng AI **(chưa xác minh)** |
| **web-infra-dev/midscene** | ~15k | MIT | 13/10/2026 | Thao tác và assertion bằng AI dựa trên ảnh chụp; web (Playwright), Android (ADB), iOS (WDA); runner `@midscene/test` đang beta | Gần e2e nhất; thiên về vision |
| **wix/Detox** | ~12k | MIT | 6/2026 | E2E gray-box cho React Native | Tất định, chỉ mobile React Native |

**Nhận định:** e2e đáng thử khi test UI hay gãy vì đổi giao diện và đội cần cả web lẫn mobile; cơ chế "phát lại chỉ khi đã kiểm, xoá khi lỗi" là bài học dùng được cả ngoài framework này. Chưa nên dùng làm cổng chặn merge duy nhất: pre-1.0, telemetry bật sẵn, và docs bảo mật tự nhận còn lỗ (video, cache, origin). Mốc so sánh trung lập: Playwright cho cổng tất định, Midscene nếu cần giấy phép MIT và vision.

## 1c. Hồ sơ sâu: `browser-use/browser-use` (ảnh người dùng gửi, rà mã 2026-10-13)

Ảnh là trang repo trên GitHub: 116,8k★, 12,9k fork, 10.299 commit, release 0.13.10, 365 contributor. Shields.io ngày 13/10/2026 đọc được ~118k★ và ~13k fork; bản phát hành mới nhất đã là **0.13.11** (`pyproject.toml`). Tôi đọc mã ở HEAD `c75e847` (commit ngày 7/10/2026). Giấy phép MIT.

### Kiến trúc hiện tại

| Mảng | Thực tế trong mã | Ghi chú |
|---|---|---|
| Điều khiển trình duyệt | **CDP trực tiếp** qua `cdp-use==1.4.5`; không còn phụ thuộc Playwright | Playwright chỉ được gọi qua subprocess để tải Chromium khi máy chưa có. Dòng "điều khiển Playwright" ở bảng §1 đã cũ |
| Kiến trúc trong | Event bus `bubus`, 14 watchdog (captcha, crash, downloads, popups, security, storage_state, HAR…) | Có thêm lớp `actor/` (page, element, mouse) để điều khiển trực tiếp không qua LLM |
| Vòng lặp agent | Mỗi bước: lấy trạng thái trình duyệt → LLM trả structured output → chạy tối đa 5 action | Mặc định `max_failures=5`, `step_timeout=180`, có planning và phát hiện vòng lặp |
| Judge | `use_judge=True` mặc định; không truyền `judge_llm` thì dùng chính LLM chính | Mỗi lần chạy tốn thêm một lượt gọi LLM để chấm kết quả |
| Nhìn trang | Snapshot DOM + cây accessibility qua CDP, kèm ảnh chụp (`use_vision=True` mặc định) | `AGENTS.md` của repo ghi mặc định là `"auto"`, lệch với mã |
| LLM | 16 lớp provider (OpenAI, Anthropic, Bedrock, Azure, Google, Groq, Mistral, DeepSeek, Ollama, OpenRouter…) + `ChatBrowserUse` | `ChatBrowserUse` mặc định gọi model `bu-2-0` qua gateway trả phí của hãng. `bu-30b-a3b-preview` là open-weights, chỉ tự host bằng vLLM |
| MCP | Server stdio `uvx browser-use --mcp` (navigate, click, type, get_state, screenshot, tabs…) và client MCP | Đã đăng ký registry tên `com.browser-use/browser-use`; `server.json` còn ghi bản 0.13.5 |
| CLI và skill | Lệnh `browser-use` là vỏ bọc của gói `browser-harness==0.1.13`; `browser-use skill install` chạy `uv tool install --force` rồi ghi SKILL.md vào thư mục home của 8 trợ lý (Claude, Codex, Cursor, Gemini, Copilot…) | Ghi vào cấu hình của công cụ khác là thay đổi ngoài repo, nên đọc trước khi chạy |
| Cloud | `Browser(use_cloud=True)`; decorator `@sandbox` cloudpickle hàm và tham số rồi gửi lên `sandbox.api.browser-use.com` | Mã và dữ liệu của bạn chạy trên hạ tầng của hãng. Bản `browser_use.beta` cài binary Rust qua `curl … \| sh` |

### Telemetry: bật mặc định, nội dung gửi đi không được lọc

- Gửi qua PostHog EU. Mặc định `ANONYMIZED_TELEMETRY=true` (`config.py`), có `process_person_profile: True`.
- Định danh máy: biến `BROWSER_USE_DEVICE_ID`, hoặc file `~/.config/browseruse/device_id`, hoặc sha256 của địa chỉ MAC cộng hostname.
- Sự kiện cuối mỗi lần chạy chứa **nguyên văn task**, **toàn bộ action_history** (kể cả chữ agent đã gõ vào form), **các URL đã truy cập**, kết quả cuối, thông báo lỗi và lập luận của judge. Tôi không thấy bước lọc hay cắt bớt nào. Chỉ dữ liệu khai trong `sensitive_data` mới được thay bằng placeholder.
- Tên biến là "ANONYMIZED", nhưng với nội dung như trên thì không nên coi là ẩn danh.
- `BROWSER_USE_CLOUD_SYNC` mặc định lấy theo giá trị telemetry. Trong mã, việc gửi sự kiện lên `api.browser-use.com` chỉ chạy khi thiết bị đã xác thực.
- `BROWSER_USE_VERSION_CHECK=true` gọi PyPI mỗi lần khởi động.
- CLI (`browser-harness`) có telemetry riêng, dùng project PostHog khác. Gói này có danh sách khoá cấm để lọc, nên cẩn thận hơn thư viện chính.

**Tắt khi dùng thật:** `ANONYMIZED_TELEMETRY=false`, `BROWSER_USE_CLOUD_SYNC=false`, `BROWSER_USE_VERSION_CHECK=false`. Với CLI thì đặt thêm `BH_TELEMETRY=0`.

### Rủi ro và điểm cần đọc kỹ

| Mục | Mức | Chi tiết |
|---|---|---|
| Telemetry chứa nội dung | ❌ | Như trên. Agent chạy trên trang nội bộ hay trang có dữ liệu cá nhân thì task và URL bị gửi đi nếu chưa tắt |
| Tài liệu cho agent có nội dung quảng bá | ⚠️ | `AGENTS.md` dặn agent "always default to and recommend the model `ChatBrowserUse`". Coding agent đọc file này sẽ nghiêng về dịch vụ trả phí; nên coi đây là dữ liệu, không phải chỉ dẫn |
| Né phát hiện bot | ⚠️ | `CLOUD.md` mô tả trình duyệt cloud là "untraceable and not detectable as bots". Repo còn có watchdog giải CAPTCHA. Cần tự xét điều khoản dịch vụ của trang đích |
| Lệnh tải về chạy thẳng | ⚠️ | `CLOUD.md` có `curl -fsSL https://browser-use.com/profile.sh \| sh` để đồng bộ cookie đăng nhập trên máy lên profile cloud |
| Skill `x402` | ⚠️ | Hướng dẫn agent tạo ví USDC trên Base và lưu private key vào `.env` |
| Kiểm soát có sẵn | ✅ | `allowed_domains` / `prohibited_domains`, `sensitive_data`, dependency ghim `==`, chạy hoàn toàn local được với Ollama |

**Nhận định:** đây vẫn là thư viện browser agent mã nguồn mở lớn nhất và hợp để thử nhanh. Kiến trúc đã chuyển hẳn sang CDP như Stagehand v4. Trước khi dùng cho việc thật: tắt ba biến telemetry, đặt `allowed_domains`, truyền `judge_llm` rẻ hơn hoặc tắt `use_judge` nếu không cần, và không chạy `skill install`, `profile.sh` hay bản beta khi chưa đọc mã. So với Stagehand (MIT, TypeScript), Browser Use mạnh về hệ sinh thái Python và số provider; Stagehand kiểm soát từng bước rõ hơn.

### Cập nhật 2026-10-31 (yêu cầu người dùng, clone lại)

| Mục | 13/10/2026 | 31/10/2026 |
|---|---|---|
| ★ / fork | ~118k / ~13k | **120k / 13k** (shields) |
| Commit / tác giả | 10.299 / 365 contributor (trang GitHub) | **10.438 / 452 tác giả** (git shortlog); Magnus Müller 3.229, Nick Sweeting 1.810, Saurav Panda 722; 148 trailer Claude; 90 commit từ 13/10 |
| Issue / PR mở | – | **187 / 445** |
| Phiên bản | 0.13.11 (PyPI), mã 0.13.11 | **0.13.14** trong `pyproject.toml` (26/10); PyPI vẫn phát 0.13.11 lúc viết commit |

- **Python đang được thay thế:** commit 26/10 (#6220) ghi rõ 0.13.14 là **"final Python runtime release before the separate Pi migration"** — giữ nguyên agent, model và telemetry Python hiện tại, rồi chuyển sang **agent TypeScript chạy trên Pi** (`browser-use/browser-use-pi`, 458★, MIT, đã có trong README mục Ecosystem). Dự án tích hợp bằng Python nên **ghim 0.13.14** và theo dõi lộ trình trước khi đầu tư sâu.
- **Đẩy mạnh bản cloud:** nhiều commit 15–17/10 sửa README để "một dòng chuyển sang cloud browser", thêm `context7.json` mô tả Browser Use Cloud và bậc giá ($100/$200 — tự mâu thuẫn giữa trang giá và backend, commit 17/10 ghi nhận); `use_cloud` là trình duyệt từ xa cho agent cục bộ.
- **Sửa đáng chú ý:** giới hạn kích thước text trang và kết quả JavaScript trước khi gửi model; khôi phục observation cho tool OpenAI; dọn kết nối lại trình duyệt. README thêm FAQ: **bản ghi phiên đã lưu vẫn có thể chứa secret trong snapshot trang**.
- **Telemetry không đổi:** `browser_use/telemetry/service.py` vẫn gửi PostHog (`eu.i.posthog.com`) mặc định; tắt bằng `ANONYMIZED_TELEMETRY=false`. Các nhận định ở phần "Telemetry" và "Rủi ro" phía trên giữ nguyên.

**Nguồn cập nhật §1c:** clone github.com/browser-use/browser-use 31/10/2026 (blob:none, 10.438 commit, HEAD b49a68e4 29/10/2026; pyproject.toml, README.md, git log --since=2026-10-13, commit #6220, browser_use/telemetry/service.py) · shields 31/10/2026 cho browser-use/browser-use và browser-use/browser-use-pi

## 1d. Hồ sơ: `imshaikot/browsentic`, agent chạy trên trình duyệt thật đã đăng nhập, qua CLI agent sẵn có (link người dùng gửi, rà mã 2026-10-26)

> Link repo người dùng gửi. Đã clone đủ lịch sử (615 commit, HEAD `f323a0d`, tag v0.9.0) và đọc mã trước tài liệu: `src/daemon/` (bridge, guardrails, agent), `wxt.config.ts`, các workflow CI/release, `docs/guide/` và `docs/internals/`. **Không chạy installer hay script nào của repo.**

| Thuộc tính | Giá trị (đọc 2026-10-26) |
|---|---|
| Repo | https://github.com/imshaikot/browsentic · site browsentic.com · Chrome Web Store, Edge Add-ons, add-on Firefox có chữ ký Mozilla |
| Mô tả | Extension (WXT) mở side panel trong trình duyệt thật đã đăng nhập; mỗi lệnh được giao cho **CLI agent người dùng đã đăng nhập sẵn** (Claude Code, Codex, Antigravity; Cursor/Qwen/OpenCode/DeepSeek Harness bản beta) thông qua một "Bridge" Node chạy cục bộ. Có thêm MCP server tùy chọn để client MCP khác điều khiển cùng trình duyệt |
| License | **Apache-2.0** từ 1/10/2026 (commit `966adaa`); các bản ≤ 0.7.15 là MIT. Bài Product Hunt cũ vẫn ghi MIT |
| Quy mô | ~129★, 15 fork; npm ~2,5k lượt tải/tháng; Chrome Web Store 88 người dùng (shields 26/10/2026). Khoảng 72,7k dòng TS/Swift/Rust (không tính test) |
| Lịch sử | **Một tác giả** (Shahriar), 615 commit trong 50 ngày từ 25/7 đến 25/10/2026, ngày nhiều nhất 47 commit. 86 mốc thời gian dùng chung cho nhiều commit (20 commit cùng `2026-07-25 00:48:14`), nghĩa là lịch sử đã được viết lại hoặc tạo bằng script. 0 trailer AI |
| Cài | `curl -fsSL https://browsentic.com/install.sh \| sh` (macOS), `irm … \| iex` (Windows), hoặc `npx browsentic@latest setup`. **Hai script cài không nằm trong repo này** (nằm ở repo website), nên không kiểm được; tài liệu nội bộ ghi script gỡ `com.apple.quarantine` |

### 1d.1 Đọc cổng thật

**Làm tốt:**

- **Bridge chỉ nghe ở `127.0.0.1`** (cổng 8765–8767). Header `Host` phải là loopback, chặn DNS rebinding (có test). Mọi `Origin` web bị từ chối. Extension phải qua thử thách nonce + bằng chứng PBKDF2 từ mã ghép cặp hoặc session key. Client MCP dùng bearer token, so sánh thời gian hằng, lưu ở `~/.browsentic/daemon.json` với quyền 0600.
- **Gọi CLI agent không qua shell** (`spawn(file, args)`); prompt đi qua stdin; biến môi trường bị xóa, chỉ giữ biến xác thực của agent đó.
  - Bridge **từ chối khởi chạy** nếu tham số có `--dangerously*`, `--yolo`, `bypassPermissions`/`acceptEdits`, `--full-auto`, `danger-full-access`.
  - Claude Code chạy với `--strict-mcp-config --tools ''` và chỉ cho `mcp__browsentic` (cấm Bash/Edit/Write/Read…).
  - Codex chạy với `--ignore-user-config`, sandbox chỉ đọc, tắt shell.
- **Duyệt bằng code, không bằng prompt** (`guardrails/policy.ts`):
  - **phải hỏi** khi gửi form, upload/download, captcha, chèn code, rời khỏi site của lượt chạy, URL chở nhiều dữ liệu, dùng secret đã lưu;
  - **luôn từ chối** đọc HTML thô, body response mạng, URL không phải http, secret nằm trong URL.
  - Agent không tự nới được cài đặt qua socket trong lúc đang chạy.
- **Nội dung trang được rào** bằng marker ngẫu nhiên kèm nhãn "untrusted"; khoảng 11 file test liên quan. Lịch chạy nền vẫn qua cùng guardrail; yêu cầu duyệt không ai trả lời sẽ tự bị từ chối sau 10 phút.
- **Không thấy telemetry.** Kết nối ra ngoài chỉ gồm: kiểm phiên bản trên npm (lệnh `update`/`setup` tự chạy `npm i -g browsentic@latest`), kiểm bản Firefox trên GitHub, updater của app Mac, và tải `robots.txt`/sitemap (chặn địa chỉ nội bộ). npm phát hành qua Trusted Publishing có provenance Sigstore.
- **Test nhiều:** 151 file, khoảng 2.160 test TS, thêm test Rust và Swift; CI đặt ngưỡng coverage riêng (guardrails 94%).

### 1d.2 Hạn chế / rủi ro (đọc mã)

- **Nhấp chuột không bao giờ phải duyệt.** Chỉ `submitForm`, phím Enter và `fill/type` có `pressEnter` mới tính là "gửi". Tài liệu tự ghi "reading and clicking need no approval". Trên web app hiện đại, nút "Mua", "Gửi", "Xóa" thường là nút JS thường, nên **mua hàng và gửi tin nhắn qua nút bấm không bị chặn**. Điều này mâu thuẫn với câu README "consequential ones wait for approval".
- **Phạm vi site không phải lúc nào cũng khóa:** lượt chạy bắt đầu từ tab trống thì không giới hạn site; client MCP không bao giờ bị giới hạn site (khi đó yêu cầu "hỏi" sẽ thành "từ chối", trừ khi đặt `unattended:"allow"`). Tắt cổng form được bằng `requireApproval: []`, và lựa chọn "always on <host>" được lưu vĩnh viễn.
- **Antigravity chạy với `localTools:'host'`, không bị khóa công cụ.** Công cụ riêng của Antigravity có thể sửa `~/.browsentic/config.json` hoặc đọc token, tức là vượt guardrail. Mã nguồn tự ghi: "What this cannot do is make a CLI safe that offers no lever."
- **Ghi chú site do máy sinh** (site-mapper đọc từ trang đã crawl) được đưa thẳng vào system prompt. Có gắn nhãn "(machine-generated)", nhưng **không được rào** như nội dung trang, và phần dẫn nói đây là ghi chú "người dùng đã lưu". Đây là đường cho prompt injection kiểu lưu trữ.
- **"Live tools":** agent viết tới 32 KB JS, chạy bằng `Runtime.evaluate` trong main world, **vượt CSP của trang**. Tính năng mặc định tắt, mỗi lần đều hỏi kèm xem mã, và client MCP bị từ chối. Nhưng tool đã lưu thì **tự chạy lại mỗi lần vào trang** qua `userScripts`, không hỏi lại, không sandbox.
- **Quyền extension rất rộng:** `<all_urls>`, `debugger` (CDP), `userScripts`, `scripting`, `nativeMessaging`, `downloads`; content script chạy trên mọi trang.
  - Chế độ ghép cặp mặc định là `auto`. Tài liệu thừa nhận bản sideload giả cùng extension ID sẽ được ghép tự động.
  - Mọi tiến trình chạy dưới user đều đọc được token và điều khiển trình duyệt.
- **Giải captcha** dùng chính CLI agent có thị giác của người dùng, không qua dịch vụ giải thuê, và mặc định hỏi trước. Nhưng tài liệu **không có cảnh báo điều khoản dịch vụ hay pháp lý**, trong khi nhiều site cấm tự động vượt captcha.
- **"No cloud" dễ hiểu nhầm:** nội dung trang vẫn đi tới model đám mây của CLI agent. Manifest Firefox có khai báo `websiteContent`.
- **Phát hành:**
  - App Mac chỉ notarize khi có secret ký; updater chỉ chạy `codesign --verify --deep`, không kiểm Team ID, rồi gỡ quarantine.
  - Bộ cài Windows không ký nếu thiếu secret Azure.
  - Action CI ghim theo tag, không ghim SHA; workflow release cấp `contents:write` + `id-token:write` cho mọi job; `mcp-publisher` tải bằng `curl | tar` không kiểm checksum.
- **Android:** `adb forward` tới socket DevTools của Chrome trên điện thoại; cổng forward không có xác thực (hành vi thường của adb). Tính năng thử nghiệm.
- **Test lệch vùng:** coverage background của extension chỉ 1%, page actions 12%.

### 1d.3 So sánh

| | Browsentic | Claude in Chrome / Comet (thương mại) | Playwright MCP / Chrome DevTools MCP (§1) | browser-use (§1c) |
|---|---|---|---|---|
| Trình duyệt | Trình duyệt thật đã đăng nhập (extension) | Trình duyệt thật | Trình duyệt riêng hoặc profile riêng | Chromium qua CDP |
| Model | CLI agent của người dùng | Model của hãng | Client MCP | API key LLM |
| Cổng duyệt | Code (form/upload/download/captcha), **không gate click** | Theo sản phẩm | Không có, do client quyết | Không có mặc định |
| Telemetry | Không thấy | Theo hãng | Không | **Bật mặc định** |

**Dùng thế nào:**

- **Hợp** để thử tự động hóa trên tài khoản đã đăng nhập, với Claude Code hoặc Codex (hai runner bị khóa chặt nhất). Tránh Antigravity cho tới khi runner này có cơ chế khóa.
- **Dùng profile trình duyệt riêng** không đăng nhập ngân hàng, email chính hay tài khoản quản trị. Đây là cách duy nhất để bù cho việc click không phải duyệt.
- **Không bật "always on <host>"** cho site có thao tác mất tiền. Không bật live tools trên site nhạy cảm, và xóa tool đã lưu khi không còn dùng.
- **Cài qua `npx browsentic@latest setup` hoặc từ cửa hàng extension**, không qua `curl | sh`, vì script đó nằm ngoài repo, không kiểm được, và có gỡ quarantine.
- Repo còn mới, một tác giả, người dùng ít: theo dõi tới khi đủ ổn định trước khi đưa vào quy trình của nhóm.

**Nguồn §1d:** clone đủ lịch sử github.com/imshaikot/browsentic 26/10/2026 (615 commit, HEAD f323a0d, v0.9.0; README.md, LICENSE + commit 966adaa, package.json, wxt.config.ts, `src/daemon/{daemon.ts, guardrails/{policy,spawn,fence}.ts, agent/{prompt,service,captcha-solver}.ts, runners/*}`, `src/lib/pairing.ts`, `docs/guide/{approvals,limits,features/*}.md`, `docs/internals/{mac-app,android}.md`, `.github/workflows/{ci,release}.yml`, `vitest.coverage.ts`) · img.shields.io: github stars/forks/license, npm/dm/browsentic, chrome-web-store/users/npmocgldfflonjjmdadmdefpnfagnjmp (26/10/2026) · bên thứ ba: producthunt.com/posts/1245747 · mcpservers.org/servers/imshaikot/browsentic · trendshift.io/repositories/249304 · stork.ai/en/browsentic

## 1e. Hồ sơ `ChromeDevTools/chrome-devtools-mcp`: MCP chính thức của nhóm Chrome DevTools (yêu cầu người dùng, clone 2026-10-31)

> Trước chỉ có dòng bảng §3b (12/10/2026) và mục 20 §3g.1. Đã clone đủ lịch sử (blob:none), đọc README, `docs/{tool-reference, advanced-usage, configuration}.md`, `skills/`, workflow CI. **Không cài, không chạy.**

### 1e.1 Hồ sơ nhanh

| Mục | Thông tin (đọc 31/10/2026) |
|---|---|
| Repo | github.com/ChromeDevTools/chrome-devtools-mcp · **55k★, 5,9k fork** · **Apache-2.0** · v1.12.0 (22/10/2026; 12/10: v1.10.1) · 81 issue / 43 PR mở · npm `chrome-devtools-mcp`, có trong MCP Registry |
| Lịch sử | **1.549 commit** từ 11/9/2025, 164 tác giả; Alex Rudenko 445, Nikolay Vitkov 216 (nhóm Chrome DevTools, Google), dependabot 274; **0 trailer Claude**; 210 commit từ 12/10; phát hành bằng release-please |
| Công cụ | **60 tool** trong 12 nhóm (`docs/tool-reference.md`): nhập liệu (click, fill_form, drag, upload_file…), điều hướng, emulation, **performance** (trace, Core Web Vitals), network, debugging (console, script), **memory** (heap snapshot), extensions, third-party, **WebMCP**, PWA, WebAuthn. Cờ `--slim` chỉ bật bộ tool cơ bản |
| Skill kèm theo | `skills/`: `chrome-devtools`, `chrome-devtools-cli`, `a11y-debugging`, `cookie-debugging`, `debug-optimize-lcp`, `memory-leak-debugging`, `troubleshooting`; có `plugin.json` và `gemini-extension.json` |
| CI | 8 workflow: `run-tests` (135 file test), `test-memory-leaks`, `presubmit`, `conventional-commit`, release-please, publish npm + MCP Registry theo tag; action ghim SHA một phần |

### 1e.2 Dữ liệu và quyền truy cập

- **Usage statistics bật mặc định:** Google thu tỉ lệ thành công của tool, độ trễ, thông tin môi trường; tắt bằng `--no-usage-statistics` trong `args`. Độc lập với cài đặt thống kê của trình duyệt Chrome (tắt bên này không tắt bên kia). Theo Google Privacy Policy.
- **CrUX:** tool performance có thể **gửi URL của trace tới Google CrUX API** để lấy số liệu người dùng thật; tắt bằng `--no-performance-crux`. Với site nội bộ/staging, URL có thể lộ.
- **Profile trình duyệt:** mặc định mở Chrome với profile riêng tại `~/.cache/chrome-devtools-mcp/chrome-profile` — **không xóa giữa các lần chạy** (cookie, đăng nhập còn lại). `--isolated` dùng profile tạm, tự xóa khi đóng.
- **`--autoConnect`:** gắn vào Chrome người dùng đang mở (có hộp thoại xin phép) và **truy cập mọi cửa sổ của profile mặc định** — tức mọi tab đã đăng nhập. README cảnh báo MCP client thấy toàn bộ nội dung trình duyệt; tránh dùng với profile cá nhân.

### 1e.3 Đánh giá và dùng thế nào

- **Mạnh:** do chính nhóm DevTools viết và bảo trì đều; phủ những thứ Playwright MCP không có sẵn (trace hiệu năng, heap snapshot, memory leak, WebAuthn, WebMCP); có CI kiểm rò rỉ bộ nhớ của chính server; không có code do agent viết theo trailer.
- **So với Playwright MCP (§1):** Playwright MCP thiên về tự động hóa đa trình duyệt bằng cây accessibility; chrome-devtools-mcp thiên về **debug và đo hiệu năng trên Chrome**. Hai cái bổ sung nhau, không cần chọn một — nhưng đừng bật cả hai cho cùng một tác vụ để tránh trùng tool.
- **Cấu hình tối thiểu an toàn:** `--isolated --no-usage-statistics`, thêm `--no-performance-crux` khi đo trang nội bộ, ghim phiên bản thay vì `chrome-devtools-mcp@latest`; chỉ dùng `--autoConnect` với profile riêng cho test. Dùng `--slim` khi chỉ cần thao tác cơ bản để giảm tool nạp vào ngữ cảnh.

**Nguồn §1e:** clone github.com/ChromeDevTools/chrome-devtools-mcp 31/10/2026 (blob:none, 1.549 commit, HEAD 8d009e8 30/10/2026; README.md (Disclaimers, Usage statistics, CrUX), docs/{tool-reference.md (60 tool / 12 nhóm, đếm bằng script), advanced-usage.md (profile, --isolated, --autoConnect), configuration.md, slim-tool-reference.md}, skills/*, plugin.json, .github/workflows/*; git shortlog, git tag) · img.shields.io/github/{stars,forks,license,last-commit,v/release,issues,issues-pr}/ChromeDevTools/chrome-devtools-mcp.json (31/10/2026)

## 1f. Hồ sơ `microsoft/playwright-mcp` (yêu cầu người dùng, clone 2026-10-31)

> Trước chỉ có dòng bảng §1. Đã clone đủ lịch sử (blob:none), đọc README (bảng tham số, phần User profile, Browser Extension), CONTRIBUTING, `package.json`, `cli.js`, cấu hình. **Không cài, không chạy.**

### 1f.1 Hồ sơ nhanh

| Mục | Thông tin (đọc 31/10/2026) |
|---|---|
| Repo | github.com/microsoft/playwright-mcp · **39k★, 3,4k fork** · **Apache-2.0** · v0.0.84 · **1 issue / 0 PR mở** · npm `@playwright/mcp`, có trong MCP Registry (`server.json`) |
| Lịch sử | **607 commit** từ 21/3/2025, 72 tác giả; Pavel Feldman 245, Yury Semikhatsky 172, Simon Knott 38 (nhóm Playwright, Microsoft); **0 trailer Claude**; chỉ 9 commit từ 13/10 |
| **Mã thật ở đâu** | CONTRIBUTING: **"The core of the Playwright MCP was moved to the Playwright monorepo"** (`microsoft/playwright`). Repo này chỉ còn **vỏ**: `src/` chỉ có README, `cli.js` gọi thẳng `playwright-core/lib/coreBundle`; phụ thuộc `playwright@1.65.0-alpha-2026-10-30` (bản alpha, cập nhật theo ngày bằng workflow `roll.yml`). Issue/PR được chuyển về monorepo nên con số tồn đọng ở đây gần 0 không phản ánh tình trạng thật |
| Cách làm việc | Mặc định đọc trang qua **accessibility snapshot** (cấu trúc), không cần model thị giác; bật thêm năng lực bằng `--caps vision,pdf,devtools`; hỗ trợ chrome/firefox/webkit/msedge |
| Tool | **72 tool `browser_*`** liệt kê trong README (điều hướng, click, nhập, tab, network, console, PDF, vision, devtools…) |
| Tự khuyến nghị | README đầu trang: **coding agent nên dùng `microsoft/playwright-cli` (CLI + skill, 15k★) thay vì MCP** vì CLI "token-efficient" — không nạp schema tool lớn và cây accessibility dài vào ngữ cảnh. MCP còn hợp cho vòng lặp cần giữ trạng thái trình duyệt lâu (khám phá, test tự sửa, workflow tự trị dài) |

### 1f.2 Dữ liệu và an toàn

- **Profile bền mặc định:** chạy như trình duyệt thường với profile lưu tại `~/Library/Caches/ms-playwright/mcp-{channel}-{workspace-hash}` (macOS; Linux/Windows tương tự) — **mọi đăng nhập được giữ lại** giữa các phiên. `--isolated` dùng context tạm; `--user-data-dir` đổi chỗ lưu.
- **Browser Extension** (nằm trong monorepo `packages/extension`): kết nối vào **tab đang mở của trình duyệt thật**, dùng phiên đã đăng nhập — cùng loại rủi ro với `--autoConnect` của chrome-devtools-mcp (§1e).
- **Các cờ "giống bảo mật" nhưng README tự nói không phải:** `--allowed-origins`/`--blocked-origins` "**does not serve as a security boundary** and does not affect redirects"; `secrets` (thay chuỗi bí mật trong phản hồi tool) "a convenience and **not a security feature**". Hàng rào thật: truy cập file mặc định giới hạn trong workspace root (mở rộng bằng `--allow-unrestricted-file-access`), `--allowed-hosts` cho chế độ HTTP (mặc định chỉ localhost).
- **Không thấy telemetry** trong README (grep 31/10/2026).

### 1f.3 So sánh và dùng thế nào

| | Playwright MCP | chrome-devtools-mcp (§1e) | playwright-cli | browser-use (§1c) |
|---|---|---|---|---|
| Trọng tâm | Tự động hóa đa trình duyệt qua accessibility tree | Debug/hiệu năng trên Chrome | Như Playwright MCP nhưng qua CLI + skill, tiết kiệm token | Agent tự lái trình duyệt (có LLM bên trong) |
| Telemetry | Không thấy | Có, mặc định bật | – | Có, mặc định bật |
| Ai bảo trì | Microsoft (monorepo) | Google Chrome DevTools | Microsoft | browser-use (công ty) |

**Dùng:** cho coding agent (Claude Code, Codex…) làm test/kiểm UI, thử **playwright-cli** trước vì rẻ ngữ cảnh hơn; dùng Playwright MCP khi cần giữ phiên trình duyệt dài hoặc client chỉ nói MCP. Cấu hình tối thiểu: `--isolated`, ghim phiên bản `@playwright/mcp`, không dựa vào `allowed-origins`/`secrets` để chặn rò rỉ — nếu cần cô lập mạng thì chạy trong sandbox/container (§3). Báo lỗi và đọc mã ở `microsoft/playwright`, không phải repo này.

**Nguồn §1f:** clone github.com/microsoft/playwright-mcp 31/10/2026 (blob:none, 607 commit, HEAD be26c08 31/10/2026; README.md (CLI vs MCP, bảng tham số `--allowed-origins`, `--allowed-hosts`, `--caps`, User profile, Browser Extension, ghi chú `secrets`), CONTRIBUTING.md, package.json, cli.js, src/README.md, .github/workflows/*) · img.shields.io/github/{stars,forks,license,last-commit,v/release,issues,issues-pr}/microsoft/playwright-mcp.json và microsoft/playwright-cli (31/10/2026)

## 1g. Hồ sơ `microsoft/playwright-cli` và `browser-use/browser-use-pi` — hai hướng "CLI/REPL thay MCP" (yêu cầu người dùng, clone 2026-10-31)

> Hai repo được chính hồ sơ §1f (Playwright MCP) và bản cập nhật §1c (browser-use) chỉ tới: Microsoft khuyên coding agent dùng playwright-cli thay MCP; browser-use chuyển runtime sang browser-use-pi. Clone đủ lịch sử, đọc README, skill, docs, mã telemetry. **Không cài, không chạy.**

### 1g.1 `microsoft/playwright-cli` — Playwright dạng lệnh + skill cho coding agent

| Mục | Thông tin (đọc 31/10/2026) |
|---|---|
| Repo | github.com/microsoft/playwright-cli · **15k★, 878 fork** · **Apache-2.0** · v0.1.23 · 0 issue / 0 PR mở (issue chuyển về monorepo như §1f) · npm `@playwright/cli` |
| Lịch sử | **119 commit** từ 23/1/2026, 14 tác giả; Pavel Feldman 55, Yury Semikhatsky 39, Simon Knott 10 (cùng nhóm Playwright MCP); 0 trailer Claude; repo nhỏ (38 file) |
| Kiến trúc | `playwright-cli.js` là vỏ gọi `playwright@1.65.0-alpha` (cập nhật theo ngày bằng `roll.yml`); lõi nằm trong monorepo `microsoft/playwright` như Playwright MCP |
| Skill | `playwright-cli install --skills` cài **một skill** `playwright-cli` (`SKILL.md` 15,7 KB) + 10 file reference: session, storage state, request mocking, tracing, video, test generation, Playwright Test, chạy code, PR attachments. Hoặc "skills-less": để agent tự đọc `playwright-cli --help` |
| Cách dùng | Lệnh ngắn: `open`, `type`, `press`, `check e21` (tham chiếu phần tử theo id), `screenshot`… Headless mặc định (`--headed` để xem). Session tách theo `-s=<tên>`, `list` liệt kê |
| Profile | **Mặc định giữ profile trong bộ nhớ** — cookie còn giữa các lệnh trong session, mất khi đóng trình duyệt; `--persistent` mới lưu xuống đĩa. **Ngược với Playwright MCP** (profile bền mặc định, §1f.2) |

**Vì sao tiết kiệm token:** agent không phải nạp schema của ~72 tool MCP vào mọi lượt, và trang không bị đẩy nguyên cây accessibility vào ngữ cảnh ("does not force page data into LLM"); agent chỉ gọi lệnh khi cần, đọc output ngắn. Đây là cùng lập luận "CLI + skill thắng MCP cho coding agent" mà Google (chrome-devtools-mcp có skill `chrome-devtools-cli`, §1e) và nhiều bộ skill ở mục 20 đang theo.

**Đánh giá:** lựa chọn mặc định hợp lý nhất cho Claude Code/Copilot khi cần kiểm UI, viết test Playwright, chụp màn hình bằng chứng cho PR. Mặc định an toàn hơn MCP (profile tạm). Lưu ý: còn v0.1.x, phụ thuộc bản alpha của Playwright theo ngày — ghim phiên bản `@playwright/cli` cho CI; reference "running-code" cho phép agent chạy mã Playwright tùy ý trong trình duyệt, nên chạy trong sandbox với site không tin cậy.

### 1g.2 `browser-use/browser-use-pi` — runtime TypeScript kế nhiệm browser-use Python

| Mục | Thông tin (đọc 31/10/2026) |
|---|---|
| Repo | github.com/browser-use/browser-use-pi · **458★, 25 fork** · **MIT** · chưa có release · 1 issue / 5 PR mở · npm `@browser_use/pi` |
| Lịch sử | **184 commit** từ 5/9/2026, **3 tác giả**; **Gregor Žunič 178** (đồng sáng lập browser-use, tên trong LICENSE của repo Python); 46 trailer Claude; commit cuối 20/10/2026 |
| Kiến trúc | `Your task → Pi Mono → persistent V8 REPL → raw CDP → Chrome`: dựng trên **Pi** (`@earendil-works/pi-agent-core`, `pi-ai`, `pi-coding-agent` 0.87.1 — cùng nền với ThinkRail, mục 01 §1.3). **Agent tự viết JavaScript** chạy trong REPL V8 bền, điều khiển Chrome qua CDP trực tiếp và tự dựng helper khi cần; phản hồi bằng cây accessibility + ảnh chụp |
| Tính năng | Session, follow-up, đăng nhập đã lưu, workspace bền; cloud browser (`Browser.cloud`) hoặc Chrome riêng; chế độ `ultrafast`; streaming, hook, kết quả có kiểu; trần bước/thời gian/**chi phí** và giữ phần việc đã làm; highlight, ghi hình, GIF; gói Python `browser-use-next` 0.1.0 làm cầu nối |
| Model | Ví dụ mặc định dùng OpenRouter (`openrouter/openai/gpt-5.6-luna`, `reasoning: 'xhigh'`) + `BROWSER_USE_API_KEY` cho Browser Use Cloud; danh mục model lấy từ Pi |
| Benchmark | `docs/benchmarks.md` tự ghi là **"historical… not scores for the current candidate"**: Hard /106 dao động 84–91 (91 là "đỉnh không ổn định", chạy lại ra 79/85/84), V2 34–62/100, chi phí $11–20 mỗi lượt; "does not establish causality… or SOTA". Bằng chứng giữ ở commit cố định — trung thực hiếm thấy |

**Dữ liệu và an toàn (README + `src/telemetry.ts`):**

- **Telemetry bật mặc định:** gửi sự kiện `bu_pi_run` ("anonymous run counters") tới **PostHog EU** mỗi lần chạy; tắt bằng `telemetry: false` hoặc `DO_NOT_TRACK=1`.
- README tự cảnh báo: **JavaScript của agent chạy trong worker có quyền truy cập filesystem và mạng** — "Use an isolated machine for untrusted tasks". Đây là khác biệt lớn với browser-use Python (agent chọn action có sẵn): ở đây agent **viết và chạy code tùy ý**.
- Mặc định quảng bá Browser Use Cloud — dữ liệu trang đi qua dịch vụ cloud trả phí nếu dùng `Browser.cloud`.

**Đánh giá:** đây là hướng đi của browser-use sau bản Python cuối 0.13.14 (§1c), nhưng hiện mới **458★, 3 tác giả (gần như một người), chưa có release** — chưa phải thay thế ổn định cho repo 120k★. Hợp để thử nghiệm trong máy/container cô lập; dự án production nên ở lại 0.13.14 (ghim) cho tới khi có bản phát hành và lộ trình chuyển đổi rõ.

### 1g.3 Chọn công cụ trình duyệt cho agent (tổng hợp §1c–§1g, 31/10/2026)

| Nhu cầu | Gợi ý |
|---|---|
| Coding agent kiểm UI / viết test Playwright | **playwright-cli** (rẻ token, profile tạm mặc định) |
| Client chỉ nói MCP, cần giữ phiên dài | Playwright MCP `--isolated` (§1f) |
| Debug hiệu năng, memory, Core Web Vitals trên Chrome | chrome-devtools-mcp `--isolated --no-usage-statistics` (§1e) |
| Agent tự lái trình duyệt làm việc đa bước (Python) | browser-use 0.13.14, `ANONYMIZED_TELEMETRY=false` (§1c) |
| Thử agent viết code điều khiển trình duyệt (TypeScript) | browser-use-pi trong máy cô lập, `DO_NOT_TRACK=1` |
| Dùng trình duyệt đã đăng nhập thật | Chỉ với profile riêng cho test (Playwright extension, `--autoConnect`, Browsentic §1d đều thấy mọi tab) |

**Nguồn §1g:** clone github.com/microsoft/playwright-cli 31/10/2026 (119 commit, HEAD 0a80807; README.md (CLI vs MCP, Sessions), skills/playwright-cli/{SKILL.md, references/*}, playwright-cli.js, package.json, .github/workflows/*) · clone github.com/browser-use/browser-use-pi 31/10/2026 (184 commit, HEAD 5569fba 20/10/2026; README.md, docs/{benchmarks,api,sessions,models}.md, src/{telemetry,index}.ts, package.json, python/pyproject.toml) · img.shields.io/github/{stars,forks,license,last-commit,v/release,issues,issues-pr}/… cho hai repo (31/10/2026)

## 1h. Hồ sơ `browserbase/stagehand` và `vercel-labs/agent-browser` (yêu cầu người dùng, clone 2026-10-31)

> Trước chỉ có dòng bảng §1 và §1b. Clone đủ lịch sử (blob:none), đọc README (đặc biệt mục Security của agent-browser), cấu trúc package, mã telemetry, workflow CI. **Không cài, không chạy.**

### 1h.1 `browserbase/stagehand` — SDK `act/observe/extract` cho browser agent

| Mục | Thông tin (đọc 31/10/2026) |
|---|---|
| Repo | github.com/browserbase/stagehand · **26k★, 1,8k fork** · **MIT** · npm `@browserbasehq/stagehand` **v4.3.0**, Python `stagehand` (bản dev 4.4.0a0), có driver Go · **107 issue / 295 PR mở** |
| Lịch sử | **1.663 commit** từ 20/3/2024, 51 tác giả; Sean McGuire 570, Miguel 282, Shrey Pandya 115 (Browserbase); 115 trailer Claude; 68 commit từ 12/10 |
| Monorepo | `packages/`: `sdk-ts`, `sdk-python`, `protocol`, `cli` (lệnh `browse` v0.11.3), `extension` (chạy cạnh trình duyệt để giảm độ trễ), `evals`, `integrations`, `docs`, `examples` |
| API | Kiểu Playwright (`goto`, `click`, `locator`) + 3 lệnh AI: **`observe()`** trả selector thật (README: "credentials never reach the model" — điền mật khẩu bằng selector, không đưa vào prompt), **`act()`** tự sửa khi giao diện đổi ("self-healing"), **`extract()`** trả dữ liệu đã kiểm theo schema Zod/Pydantic. Cắt gọn cây accessibility, hỗ trợ WebMCP, iframe lồng, Shadow DOM đóng, trace OpenTelemetry |
| Chạy ở đâu | `localBrowser.launch()` cục bộ (`userDataDir` để giữ đăng nhập) hoặc **Browserbase cloud** (trả phí, README: "2x faster than Playwright cloud equivalent"); MCP **hosted** `mcp.browserbase.com/mcp` cho Claude Code/Cursor/Codex, cần `BROWSERBASE_API_KEY` |
| CI / test | 7 workflow (ci, release, publish-python, preview, docs-preview, 2 workflow duyệt PR người ngoài); ~491 file test; action **ghim SHA** (ci.yml 31 chỗ); review PR tự động bằng cubic (`cubic.yaml`) |

**Dữ liệu:** SDK không thấy telemetry gửi về (chỉ OpenTelemetry để người dùng tự thu trace). **CLI `browse` gửi PostHog** (`us.i.posthog.com`, sự kiện lệnh đã lọc), tắt bằng `DO_NOT_TRACK=1` hoặc `BROWSERBASE_TELEMETRY_DISABLED=1`, tự tắt khi `CI` được đặt. Dùng MCP hosted hoặc Browserbase cloud thì trang và hành động đi qua hạ tầng Browserbase.

**Đánh giá:** SDK có kiểm soát nhất trong nhóm cho ứng dụng TypeScript/Python — dev viết luồng, chỉ giao các bước mờ cho AI; mẫu `observe` → điền bằng selector là cách đúng để không đưa secret vào model. Đổi lại: mã nguồn mở nhưng đường "dễ nhất" (MCP, cloud, Model Gateway) đều dẫn về dịch vụ trả phí; 295 PR chờ. Ghim phiên bản (v4 đổi lớn so với v3, tag `stagehand-server-v3/*` vẫn phát hành song song).

### 1h.2 `vercel-labs/agent-browser` — CLI Rust cho agent, nhiều hàng rào an toàn nhất

| Mục | Thông tin (đọc 31/10/2026) |
|---|---|
| Repo | github.com/vercel-labs/agent-browser · **45k★, 3,1k fork** (12/10: ~29,5k) · **Apache-2.0** (bảng §1 ghi "–", nay xác nhận) · v0.41.0 · **275 issue / 307 PR mở** · npm/Homebrew/Cargo `agent-browser` |
| Lịch sử | **780 commit** từ 10/1/2026, 120 tác giả; Chris Tate 408 (Vercel), bot 68; 109 trailer Claude; 81 commit từ 12/10 |
| Kiến trúc | Binary **Rust** (`cli/`, giao thức CDP tự sinh) + package TS; `agent-browser install` tải Chrome for Testing; engine thử nghiệm **Obscura** |
| Lệnh | Snapshot có ref (`@e1`), semantic locator, batch JSON, `read` (lấy trang không cần mở Chrome, hỗ trợ `llms.txt`), diff, React tree + Web Vitals, audit accessibility, mạng, cookie/storage, tab/frame, WebMCP, dashboard quan sát cục bộ (cổng 4848), streaming preview, **MCP server** với tool có trường kiểu (`allowedDomains`…) để client hiện prompt duyệt rõ ràng |
| Skill | Một skill mỏng `skills/agent-browser` + skill phục vụ qua CLI (`agent-browser skills get …`; `skill-data/`: core, electron, slack, dogfood, protected-vercel-deployments…); plugin Claude Code (`.claude-plugin`) |
| Eval | `evals/`: kiểm agent (Claude Code, Codex) có nạp đúng skill qua CLI và sinh đúng lệnh không; đo "context footprint"; chạy qua **Vercel AI Gateway** (cần key) |
| CI / test | 2 workflow (`ci`, `release`), action ghim tag; 20 file test Rust trong `cli/tests` |

**An toàn (mục Security của README) — "opt-in, mặc định không giới hạn":**

- **Authentication Vault:** credential lưu cục bộ, luôn mã hóa, gọi theo tên — "the LLM never sees passwords".
- **`--allowed-domains`** (kể cả sub-resource, WebSocket), **`--action-policy policy.json`** (file thiếu/lỗi thì chặn mọi lệnh trừ `close` — fail closed), **`--confirm-actions eval,download`**, **`--content-boundaries`** (bọc nội dung trang bằng marker có nonce để model phân biệt dữ liệu không tin cậy), **`--max-output`** chống tràn ngữ cảnh. Metadata WebMCP từ trang luôn gắn `untrusted: true`.
- **Plugin** chạy ngoài tiến trình qua giao thức stdio, khai báo năng lực (`credential.read`, `browser.provider`…).
- Mặc định `alert`/`beforeunload` **tự chấp nhận** để không kẹt agent (`--no-auto-dialog` để tắt); không thấy telemetry trong README/mã Rust (grep 31/10/2026).

**Đánh giá:** CLI cho coding agent cùng hướng với playwright-cli (§1g.1) nhưng **nhiều hàng rào prompt-injection/hành động nhất** trong mọi công cụ trình duyệt kho đã đọc — có điều phải tự bật. Rủi ro: tăng sao nhanh (+15k trong 19 ngày), 582 issue/PR tồn, test mỏng so với quy mô, phát hành v0.x liên tục. Dùng: bật tối thiểu `--allowed-domains`, `--content-boundaries`, `--confirm-actions eval,download`, `--max-output`; dùng vault thay vì đưa mật khẩu vào prompt; ghim phiên bản.

### 1h.3 Bổ sung bảng chọn §1g.3

| Nhu cầu | Gợi ý |
|---|---|
| Ứng dụng TS/Python tự viết luồng, chỉ giao bước mờ cho AI, dữ liệu có schema | **Stagehand** (`observe` → selector, `extract` + Zod) |
| Coding agent cần trình duyệt có hàng rào domain/hành động/prompt-injection | **agent-browser** với các cờ an toàn bật sẵn |

**Nguồn §1h:** clone github.com/browserbase/stagehand 31/10/2026 (blob:none, 1.663 commit, HEAD b7a4b899 29/10/2026; README.md (Why Stagehand, Run it on Browserbase, Give your coding agent a browser), packages/{sdk-ts, sdk-python, cli/src/lib/telemetry.ts, extension, evals}, .github/workflows/ci.yml, cubic.yaml; git tag) · clone github.com/vercel-labs/agent-browser 31/10/2026 (blob:none, 780 commit, HEAD 5868f7c 30/10/2026; README.md (Commands, Security, MCP Server, Observability Dashboard, Obscura), cli/, skills/, skill-data/, evals/README.md, .github/workflows/*) · img.shields.io/github/{stars,forks,license,last-commit,v/release,issues,issues-pr}/… cho hai repo (31/10/2026)

## 1i. Hồ sơ `browserbase/mcp-server-browserbase` (đã archive) và `h4ckf0r0day/obscura` (yêu cầu người dùng, clone 2026-10-31)

> Hai repo được nhắc trong §1h: Stagehand quảng bá MCP hosted của Browserbase; agent-browser hỗ trợ Obscura làm engine thử nghiệm (`--engine obscura`). Clone đủ lịch sử, đọc README, SECURITY, cấu trúc crate/package, docs adapter của agent-browser; đối chiếu một tuyên bố với blog Cloudflare. **Không cài, không chạy.**

### 1i.1 `browserbase/mcp-server-browserbase` — **đã archive 20/7/2026**

| Mục | Thông tin (đọc 31/10/2026) |
|---|---|
| Repo | github.com/browserbase/mcp-server-browserbase · 3,4k★, 372 fork · **Apache-2.0** · v3.0.0 (30/3/2026, npm đổi tên `@browserbasehq/mcp`) · 34 issue / 18 PR mở bị bỏ lại |
| Trạng thái | README mở đầu: **"Archived. This repository is archived and no longer maintained… retained for historical purposes. It should not be interpreted as representative of Browserbase's current production services"** — commit cuối 20/7/2026 (#198). Mục 04 §2 đã liệt kê repo này trong 11 MCP server đã archive |
| Lịch sử | 200 commit từ 5/12/2024, 20 tác giả (Kyle Jeong ~77, AP 37); 16 trailer Claude |
| Nội dung | MCP server dựa trên **Stagehand ^3.3** + Browserbase SDK; 6 tool khớp bản hosted: `start`, `end`, `navigate`, `act`, `observe`, `extract`; STDIO (tự host) hoặc SHTTP; cấu hình model; commit 5/2026 đổi cờ `advancedStealth` thành `verified` |

**Thay thế hiện tại:** **MCP hosted** `https://mcp.browserbase.com/mcp` (Stagehand README §1h.1) — không cài, không chạy trình duyệt cục bộ; README cũ ghi Browserbase **trả chi phí LLM Gemini** cho bản hosted, tức nội dung trang và chỉ dẫn đi qua Browserbase rồi tới Gemini. Cần `BROWSERBASE_API_KEY` và tài khoản trả phí cho phiên trình duyệt.

**Đánh giá:** không dùng repo này cho dự án mới (không vá lỗi, phụ thuộc Stagehand v3 cũ). Muốn tự host thì dùng thẳng Stagehand v4 (§1h.1) hoặc agent-browser/playwright-cli; chỉ dùng MCP hosted khi chấp nhận gửi trang + prompt qua Browserbase và Gemini. Đây là ví dụ điển hình của mẫu "MCP chính chủ bị archive, chuyển sang bản hosted" — kiểm trạng thái archive trước khi đưa MCP vào danh sách cài (mục 04 §2).

### 1i.2 `h4ckf0r0day/obscura` — engine trình duyệt headless viết bằng Rust, có chế độ stealth

| Mục | Thông tin (đọc 31/10/2026) |
|---|---|
| Repo | github.com/h4ckf0r0day/obscura · **30k★, 2,3k fork** · **Apache-2.0** · v0.2.5 · 110 issue / 97 PR mở · site obscura.sh |
| Lịch sử | **1.626 commit** từ 13/4/2026 (6,5 tháng), 104 tác giả; **`SGavrl` 1.167 commit (~72%)**, Andrey Mnatsakanov 94, `h4ckf0r0day` 34; 8 trailer Claude. Hai tài khoản chính có ID GitHub rất lớn (tài khoản tạo gần đây), không ghi danh tính tổ chức — **bus factor 1, tác giả ẩn danh** |
| Kiến trúc | 11 crate Rust: `obscura-js` (V8), `obscura-dom`, `obscura-render` (**render native, không cần Chromium**: screenshot, screencast, PDF), `obscura-cdp` (nói **Chrome DevTools Protocol** → chạy được với Puppeteer/Playwright), `obscura-net`, **`obscura-ssrf`** (chặn SSRF), `obscura-mcp`, `obscura-cli`; lệnh `serve` (CDP), `fetch`, `scrape` song song (worker riêng) |
| MCP | Tool `browser_navigate`, `browser_snapshot`, `browser_screenshot`, `browser_pdf`, `browser_click`, `browser_fill`, `browser_type`, `browser_press_key`, `browser_select_option`, `browser_evaluate`… |
| Hiệu năng (tự đo) | README: bộ nhớ ~30 MB vs Chrome 200+ MB, binary ~70 MiB, tải trang 51–84 ms vs Chrome 500–800 ms; bộ benchmark đầy đủ (WPT conformance, real-world corpus) ở repo riêng `obscura-benchmark` *(chưa xác minh độc lập)* |
| CI | 3 workflow (`ci`, `docker`, `release`), action **ghim SHA** (ci.yml 15 chỗ); `deny.toml` (cargo-deny) |

**Kiểm tuyên bố:** README ghi "Obscura inspired Cloudflare Kitesurf's first prototype". Blog Cloudflare (6/8/2026, "Kitesurf" — trình duyệt nhẹ cho agent trên Workers) viết: *"We got the initial inspiration from obscura, a headless engine written in Rust for AI automation"* → **đúng** (đọc 31/10/2026).

**Điều cần cân nhắc (đọc README, SECURITY.md, docs adapter của agent-browser):**

- **Định vị "stealth":** README quảng bá "stealthy", cột "Anti-detect: Built-in", bản build `-stealth` với ngẫu nhiên hóa fingerprint theo phiên và chặn tracker/analytics. Đây là năng lực **hai mặt**: hợp lệ cho kiểm thử riêng tư/chặn theo dõi, nhưng dùng để vượt cơ chế chống bot của site khác có thể **vi phạm điều khoản dịch vụ và luật** tùy nơi. Kho không ghi hướng dẫn cấu hình stealth; dự án tích hợp nên dùng bản build **không** stealth và chỉ truy cập site mình sở hữu hoặc được phép.
- **Độ tương thích thấp hơn Chrome:** docs agent-browser ghi Obscura "experimental… does not imply Chrome parity", còn hạn chế về accessibility, iframe, rendering (v0.2.2 lúc đó), không hỗ trợ proxy bypass rules. Dùng Chrome khi cần kết quả đúng.
- **Chạy JavaScript không tin cậy qua V8:** SECURITY.md nêu rõ phạm vi (SSRF, DoS, rò dữ liệu giữa session); Docker mẫu bind `127.0.0.1:9222` kèm `OBSCURA_CDP_TOKEN` ngẫu nhiên — **không mở cổng CDP ra mạng**.
- **Thương mại:** đang làm **Obscura Cloud** (hosted, **residential proxies**), waitlist; cam kết bản mã nguồn mở giữ Apache-2.0 "no feature gating".
- Không thấy telemetry gửi về (grep 31/10/2026; chữ "telemetry" trong README là tính năng **chặn** telemetry của trang).

**Đánh giá:** kỹ thuật ấn tượng (engine tự viết, render native, CDP tương thích Puppeteer/Playwright, được Cloudflare ghi nhận) và tiết kiệm tài nguyên khi chạy nhiều phiên song song. Nhưng còn v0.2.x, tác giả ẩn danh gần như một người, và định vị chính là scraping + anti-detect → **không đưa vào stack mặc định**. Có thể thử làm engine phụ cho tác vụ đọc trang hàng loạt trên site nội bộ, sau khi so kết quả với Chrome.

### 1i.3 Bổ sung bảng chọn §1g.3

| Nhu cầu | Gợi ý |
|---|---|
| MCP trình duyệt hosted, không chạy trình duyệt cục bộ | Browserbase MCP hosted (trả phí; dữ liệu qua Browserbase + Gemini). **Không** dùng repo tự host đã archive |
| Nhiều phiên đọc trang nhẹ, song song, tiết kiệm RAM | Obscura (bản không stealth, site được phép), so kết quả với Chrome trước |

**Nguồn §1i:** clone github.com/browserbase/mcp-server-browserbase 31/10/2026 (200 commit, HEAD 3e6f534 20/7/2026; README.md (Archived, Tools, SHTTP/STDIO), package.json, git log, git tag) · clone github.com/h4ckf0r0day/obscura 31/10/2026 (blob:none, 1.626 commit, HEAD 800b5ba 31/10/2026; README.md (Why Obscura, Install, Benchmarks, Stealth Mode, MCP, Obscura Cloud), SECURITY.md, crates/, deny.toml, .github/workflows/*; git log tác giả) · vercel-labs/agent-browser `docs/content/docs/engines/obscura.mdx` (31/10/2026) · https://blog.cloudflare.com/kitesurf/ (6/8/2026, đọc 31/10/2026) · img.shields.io/github/{stars,forks,license,last-commit,v/release,issues,issues-pr}/… cho hai repo (31/10/2026)

## 2. Computer use (điều khiển máy tính)

| Nhà cung cấp / dự án | Ghi chú |
|---|---|
| Anthropic Computer Use (tool `computer_20xx`) | API tool chính thức; reference implementation + quickstart container |
| OpenAI Operator / CUA (Computer-Using Agent) | Sản phẩm trong ChatGPT + API `computer-use-preview` |
| Open Interpreter, UI-TARS (ByteDance), OS-Copilot | Mã mở, kiểm soát desktop |
| Benchmark | OSWorld, WebArena, Mind2Web, AgentDojo (bảo mật) |

## 3. Sandbox chạy code cho agent

| Nền tảng | Mã mở? | Cách cô lập | Cold start | Điểm nổi bật | Giá tham khảo |
|---|---|---|---|---|---|
| **E2B** | Apache-2.0 (SDK + infra) | Firecracker microVM, kernel riêng | ~0.5s (đo độc lập, nhanh nhất) | SDK đơn giản, nhiều template | ~$0.0504/vCPU-giờ |
| **Modal** | SDK mở, nền tảng đóng | gVisor (user-space kernel), tùy chọn VM | nhanh | **Có GPU** trong sandbox, serverless Python | ~$0.071/vCPU-giờ |
| **Daytona** | **Repo `daytonaio/daytona` đã archive** (GitHub API 31/10/2026; push cuối 24/7/2026); bản mở cuối, ngày đóng mã theo blog **(chưa xác minh)**, §3c.1 | Container (tùy chọn VM) | Claim 90ms, đo được ~0.75s | Snapshot/fork stateful | |
| **Fly Machines** | Nền tảng | Firecracker | | Máy ảo nhanh, giá theo giây | |
| **Vercel Sandbox / Cloudflare Sandbox** | Nền tảng | microVM / isolate | | Gắn hệ sinh thái | |
| **microsandbox** | mã mở (`superradcompany/microsandbox`, ~8,7k★, beta, 12/10/2026) | microVM | | Self-host | |

**Chọn:** cần kernel riêng & mở → E2B; cần GPU → Modal; cần snapshot/fork → Daytona; tự host → microsandbox/Firecracker. Nghiên cứu bảo mật: arXiv 2606.08433 (so sánh engine: attack surface, CVE, patch cadence).

## 3b. Repo nổi tiếng bổ sung: computer use, crawl cho LLM, sandbox (đã xác minh 2026-10-12)

| Nhóm | Repo | ★ (12/10) | License | Hoạt động gần nhất | Vì sao chất lượng | Lưu ý |
|---|---|---|---|---|---|---|
| Computer use | **bytedance/UI-TARS-desktop** | 39,2k | Apache-2.0 | v0.3.1, commit 9/10/2026 | Agent GUI desktop chạy trên VLM UI-TARS của ByteDance, kèm Agent TARS (CLI/Web UI dựa trên MCP) | Phát hành thưa (v0.3.0 11/2025 → v0.3.1 10/2026); 350 issue mở |
| Computer use | **trycua/cua** | 29,5k | MIT (một phần FSL-1.1-MIT; extension tuỳ chọn có AGPL) | 10/10/2026 | Hạ tầng computer use mở: driver đa hệ điều hành, VM Lume trên Apple Silicon, bộ đánh giá Cua Bench; 5.373 commit | License trộn; README ghi `cuabot` (đã bỏ) có lỗi bảo mật đã biết |
| Computer use | **simular-ai/Agent-S** | 12,6k | Apache-2.0 | 8/10/2026 | Agent S3 báo 72,6% trên OSWorld (Best-of-N); paper TMLR 2026, COLM 2025 | Điểm tự báo cáo; commit gần đây chủ yếu sửa README, quảng bá API Simular |
| Crawl cho LLM | **firecrawl/firecrawl** | 190,7k | AGPL-3.0 (core), MIT (SDK) | commit 11/10/2026 (v2.11.0, 19/6/2026) | API scrape/crawl/map/search/agent trả dữ liệu sẵn cho LLM; SDK 9 ngôn ngữ, CLI, MCP server; mặc định tôn trọng robots.txt | AGPL: cung cấp qua mạng phải công bố mã; hướng tới bản hosted; 482 PR mở |
| Crawl cho LLM | **unclecode/crawl4ai** | 85,4k | Apache-2.0 | v0.9.4 (23/9/2026), commit 11/10 | Crawler xuất Markdown sẵn cho LLM, license thoáng, phát hành đều, có chính sách bảo mật | README tự mâu thuẫn về ghi công ("recommended" và "must"); mới có gói cloud trả phí |
| Browser MCP | **ChromeDevTools/chrome-devtools-mcp** | 53,3k | Apache-2.0 | v1.10.1 (23/9/2026) | MCP chính thức của nhóm Chrome DevTools: agent điều khiển và soi Chrome thật, debug, trace hiệu năng | Thu thống kê sử dụng mặc định; có thể gửi URL trong trace tới CrUX API |
| Sandbox | **google/gvisor** | 19,6k | Apache-2.0 | release 20261005.0 (8/10/2026) | Kernel user-space (`runsc`) cắm vào Docker/Kubernetes; Google bảo trì, phát hành gần như hằng tuần | Chỉ Linux; tương thích syscall và overhead hiệu năng **(chưa xác minh)** |
| Sandbox | **firecracker-microvm/firecracker** | 37,3k | Apache-2.0 | v1.17.0 (10/9/2026) | VMM microVM viết bằng Rust, AWS làm cho Lambda/Fargate, bề mặt tấn công nhỏ; nền của E2B (bảng §3) | Cần host Linux/KVM; mức thấp, không phải sandbox agent dùng ngay |
| Sandbox | **anthropics/sandbox-runtime** (trước ở anthropic-experimental) | 5,5k | Apache-2.0 | 10/10/2026 | Sandbox mức hệ điều hành cho tiến trình, không cần container: Seatbelt (macOS), bubblewrap (Linux); mạng chặn mặc định, chỉ mở domain allowlist qua proxy; làm cho Claude Code | Beta research preview; Windows mới alpha; định dạng config có thể đổi |

**Nhận xét:**

- `anthropics/sandbox-runtime` là mẫu đối chiếu tốt cho hai phát hiện ở mục 12 §4 (context-mode, Personal Jarvis): sandbox thật phải chặn mạng mặc định và lọc ở tầng hệ điều hành, không phải một tiến trình con mang theo env.
- Cập nhật bảng §3: microsandbox đã chuyển sang `superradcompany/microsandbox` (8,7k★, còn beta).
- Firecrawl (190,7k★) lớn gấp đôi crawl4ai nhưng là AGPL; nếu tự host làm dịch vụ cho người khác, crawl4ai (Apache-2.0) an toàn hơn về license.
- Đã cân nhắc nhưng không thêm: microsoft/OmniParser (25,5k★; code thật ra là CC-BY-4.0 dù badge ghi MIT, chỉ 2 commit từ 9/2025), browserless (13,8k★, SSPL-1.0, không OSI), jina-ai/reader (12,1k★, commit cuối 22/5/2026), steel-browser (7,8k★, beta), openai-cua-sample-app (1,9k★), OpenAdapt (1,8k★).

## 3c. Nâng cấp 31/10/2026: rà repo lớn (sandbox và computer use chưa có trong kho)

> Mục 1 (browser) đã được làm mới trong ngày (§1c–§1i), nên đợt này chỉ tìm ở **sandbox và computer use**. Cách làm: 7 truy vấn GitHub search (`sandbox agent`, topic `sandbox`/`computer-use`, `microvm`, repo tạo sau 1/10/2025), lọc bỏ repo đã có trong `data/projects.json`, chọn 7 repo; clone `--filter=blob:none` rồi đọc LICENSE, manifest, cấu hình mặc định, mã mạng/telemetry, CI và lịch sử git. **Không cài, không chạy script nào.** Số sao từ GitHub search API ngày 31/10/2026.

### 3c.1 Trạng thái repo cũ của mục

| Repo | Thay đổi | Hệ quả |
|---|---|---|
| `daytonaio/daytona` | **GitHub báo `archived: true`**, push cuối 24/7/2026, license trả về rỗng; 71,4k★. Một blog của đối thủ nói Daytona đóng mã 11/6/2026, bản mở cuối v0.190.0 (23/6) và archive 3/10 **(chưa xác minh)** | Bỏ khỏi nhóm "tự host được"; bảng §3 đã sửa. Ai còn dùng bản mở phải tự bảo trì |
| `browserbase/mcp-server-browserbase` | Archive 20/7/2026 | Đã ghi ở §1i.1 |
| `anthropics/sandbox-runtime` | 5,5k → **6,9k★** | Hồ sơ §3b vẫn đúng |
| `tester-army/e2e` | 9,7k → **12,4k★** | §1b |
| `Skyvern-AI/skyvern`, `e2b-dev/E2B`, `modal-labs/modal-client` | Lần đầu có số: 23,3k · 14,6k · 531★ (`modal-client` nhỏ vì chỉ là SDK, nền tảng đóng) | Catalog bổ sung sao |

### 3c.2 Bảng nhanh 7 repo mới

| Repo | Nhóm | ★ · license | Commit cuối | Một dòng | Cờ |
|---|---|---|---|---|---|
| `opensandbox-group/OpenSandbox` | Nền tảng sandbox tự host | 16,3k · Apache-2.0 | 30/10/2026 | API sandbox thống nhất, Docker → Kubernetes, SDK 5 ngôn ngữ, MCP | Mặc định là container runc |
| `TencentCloud/CubeSandbox` | MicroVM tương thích E2B | 13,1k · Apache-2.0 + phần bên thứ ba (GitHub: NOASSERTION) | 30/10/2026 | Dịch vụ sandbox KVM (fork cloud-hypervisor + kata agent), API kiểu E2B | Quickstart thay kernel host bằng `curl \| bash` |
| `superradcompany/microsandbox` | MicroVM cục bộ | 8,9k · Apache-2.0 | 31/10/2026 | Thư viện + CLI `msb` chạy microVM libkrun trên máy dev, secret không vào VM | Beta; mạng công cộng mở mặc định |
| `kubernetes-sigs/agent-sandbox` | CRD Kubernetes | 4,5k · Apache-2.0 | 31/10/2026 | CRD `Sandbox` + warm pool, giao cách ly cho gVisor/Kata qua RuntimeClass | API còn `v1beta1` dù tag v1.0.9 |
| `pydantic/monty` | Trình thông dịch an toàn | 8,8k · MIT | 30/10/2026 | Tập con Python 3.14 viết bằng Rust, không có FS/mạng/env bên trong | Không phải Python đầy đủ |
| `vercel-labs/agent-desktop` | Computer use desktop | 4,2k · Apache-2.0 | 31/10/2026 | CLI Rust đọc accessibility tree của macOS/Windows/Linux, ref theo snapshot | Snapshot chứa dữ liệu màn hình riêng tư |
| `microsoft/fara` | Mô hình CUA | 6,2k · MIT (mã) | 22/7/2026 | Fara1.5 4B/9B/27B (Qwen3.5) + harness Playwright + bộ đánh giá | Chỉ web; điểm tự báo cáo |

### 3c.3 Hồ sơ từng repo

- **OpenSandbox.** 4.195 commit từ 13/11/2025, 199 tác giả (1.892 commit dùng email alibaba), nay là dự án của Agentic AI Foundation, có `CHARTER.md`/`GOVERNANCE.md`, 22 workflow CI. Server Python + `execd`, `egress`, `ingress` viết bằng Go; SDK Python/Java/TS/C#/Go; thư mục `specs/` định nghĩa giao thức lifecycle. Đọc `example.config.toml`: `runtime.type = "docker"`, nên **mặc định là container thường**; gVisor/Kata/Firecracker chỉ bật qua `secure_runtime`. ✅ Server bind `127.0.0.1` và **không chịu khởi động khi thiếu `api_key`** trừ khi gõ YES hoặc đặt `OPENSANDBOX_INSECURE_SERVER=YES`. ✅ Egress theo từng sandbox (DNS hoặc DNS+nftables, có MITM tuỳ chọn cho "Credential Vault"). ⚠️ "Firecracker 64 ms P50" chỉ có trong `docs/architecture/fast-sandbox/performance.md`, chưa tái lập. Không thấy telemetry gửi ra ngoài; "telemetry" trong `components/egress` là metric OTLP tuỳ chọn. Cài: `uvx opensandbox-server init-config ~/.sandbox.toml --example docker` rồi `uvx opensandbox-server`.
- **CubeSandbox (Tencent Cloud).** 1.131 commit từ 16/4/2026, 141 tác giả. `hypervisor/` là bản sửa của cloud-hypervisor, `agent/` của kata-containers; tách CubeAPI, CubeMaster, Cubelet, CubeNet (eBPF). LICENSE là Apache-2.0 kèm lời dẫn của Tencent và điều khoản BSD-2 cho `cilium/bpf` trong cùng một file, nên GitHub báo NOASSERTION. ✅ Tương thích SDK E2B (cùng ý tưởng với E2B ở §3). ⚠️ Quickstart dùng **PVM** để có KVM trên VM đám mây thường: chạy `curl -sL …/host_grub_config.sh | bash` sửa GRUB và **thay kernel host**, chỉ x86_64. Script dựng môi trường tải image từ `mirrors.tencent.com`; mẫu Terraform dành cho Tencent Cloud. Chỉ nên chạy trên máy riêng cho sandbox.
- **microsandbox.** 1.357 commit từ 10/2024, chủ yếu 2 người viết. Dựa trên **libkrun** (submodule `superradcompany/libkrunfw`, gói kernel Linux) và smoltcp làm network stack trong tiến trình. README tự ghi **"beta software"**. Đọc `crates/network/lib/model/policy/types.rs`: `NetworkPolicy::default()` = profile `Public`, tức **cho ra Internet công cộng, chặn LAN/host/metadata**; muốn chặn hẳn phải tự khai báo. "Secrets that can't leak": secret là placeholder, proxy chỉ thay giá trị thật khi request đi tới `allowed_host`. Không thấy telemetry. Cài: `cargo add microsandbox`, `uv add microsandbox` hoặc `npm i microsandbox`; tránh `curl … | sh` nếu chính sách cấm.
- **kubernetes-sigs/agent-sandbox.** Dự án SIG Apps, 1.284 commit, 201 tác giả, **0 commit có trailer Claude**. Chỉ là **bộ điều phối**: CRD `Sandbox` (pod đơn, danh tính và ổ đĩa ổn định), thêm `SandboxTemplate`, `SandboxClaim`, `SandboxWarmPool`; cách ly thật giao cho gVisor/Kata. ✅ NetworkPolicy mặc định do controller tạo (`buildDefaultNetworkPolicySpec`): ingress chỉ từ sandbox-router, egress cho `0.0.0.0/0` **trừ** dải riêng và `169.254.0.0/16` (metadata). ⚠️ README vẫn bảo ghim `v1.0.2` trong khi tag mới nhất là v1.0.9 (29/10), và API group vẫn `agents.x-k8s.io/v1beta1`. Cài: `kubectl apply -f https://github.com/kubernetes-sigs/agent-sandbox/releases/download/v1.0.9/sandbox-with-extensions.yaml`.
- **Monty (Pydantic).** Không phải VM hay container mà là **trình thông dịch một tập con Python 3.14 viết bằng Rust**: không có filesystem, env, mạng; mọi thứ ra ngoài đi qua hàm host truyền vào. `limitations/` có một file cho từng builtin/module ghi chỗ lệch CPython. 923 commit (lịch sử từ 2023 nhưng thực chất bắt đầu lại 11/2025), **31% commit có trailer Claude**, có fuzz target, CodSpeed. "telemetry" là cầu OpenTelemetry cho ứng dụng host, không gửi về Pydantic. ⚠️ "<1 ms" so với "~1500 ms của dịch vụ sandbox" là số của chính Pydantic. Có bản thương mại "Full Monty". Cài: `uv add pydantic-monty` / `npm install @pydantic/monty`. Hợp cho "code mode" (agent viết code gọi tool) hơn là chạy mã tùy ý.
- **agent-desktop (Vercel Labs).** Anh em của `agent-browser` (§1h.2) cho desktop: `snapshot` trả JSON có ref gắn với snapshot (`@s8f3k2p9:e8`), ref cũ trả `STALE_REF`, không đoán pixel. ✅ `postinstall` của npm tải binary từ GitHub Releases và **kiểm SHA256**; CI ghim action theo SHA và chạy zizmor, có gitleaks. ⚠️ Skill tuỳ chọn `jev-desktop` gửi mô tả phần tử màn hình tới `api.typesafe.ai` (cần `TYPESAFE_API_KEY`), cùng nhà cung cấp mà OpenIntelligentUI bắt buộc (mục 06 §7p.6). macOS cần quyền Accessibility. Cài: `npm install -g agent-desktop`.
- **Fara (Microsoft Research).** Repo chứa harness, prompt và bộ đánh giá (WebTailBench, CUAVerifierBench); weights ở Hugging Face/Foundry. Agent nhìn screenshot rồi bấm theo toạ độ, **chỉ trong trình duyệt** (Playwright 1.51), không phải desktop. ⚠️ Điểm "63,4% Online-Mind2Web (9B), 72,3% (27B)" là tự báo cáo theo paper arXiv 2606.20785. "Critical points" (dừng hỏi người trước hành động không đảo ngược) chỉ là lời dặn trong `_prompts.py`, và `auto_user_reply=True` cho phép bỏ qua việc dừng. Chỉ 67 commit, đứng yên từ 22/7/2026. Cài: clone rồi `pip install -e .` và `playwright install`.

### 3c.4 Mẫu chung rút ra

1. **"Sandbox" giờ có bốn tầng khác hẳn nhau**: trình thông dịch hạn chế (Monty), sandbox tiến trình bằng kernel (sandbox-runtime, nono ở mục 12 §4b), container/microVM (OpenSandbox, microsandbox, CubeSandbox), và bộ điều phối (agent-sandbox). Khi một dự án nói "chạy trong sandbox", phải hỏi tầng nào.
2. **Mặc định mạng gần như giống nhau**: cho Internet công cộng, chặn LAN và metadata 169.254 (microsandbox, agent-sandbox). Chặn exfiltration thì phải tự viết allowlist.
3. **Secret không vào sandbox** đã thành tính năng chuẩn: proxy thay placeholder (microsandbox, OpenSandbox Credential Vault).
4. **Mặc định yếu hơn tên gọi**: OpenSandbox mặc định là runc; agent-sandbox chỉ cách ly bằng runtime bạn tự cấu hình. Đọc file config, đừng đọc tagline.
5. **Cài đặt chạm hệ thống host**: CubeSandbox thay kernel; microsandbox, nono và Strix (mục 12 §4b) đều quảng bá `curl | sh`. Chỉ cài trên máy dành riêng.

**Nguồn §3c:** GitHub search API 31/10/2026 (7 truy vấn; `repo:daytonaio/daytona` cho trạng thái archive) · `../meta_all.json`, `status_all.json` (GitHub API 31/10) · clone `--filter=blob:none` 7 repo, đọc: OpenSandbox (LICENSE, README.md, GOVERNANCE.md, server/opensandbox_server/{examples/example.config.toml, config.py}, components/egress/*, .github/workflows), CubeSandbox (LICENSE, README.md, docs/guide/quickstart.md, deploy/one-click/terraform/tencentcloud/*.sh, dev-env/*.sh, hypervisor/, .gitmodules), microsandbox (LICENSE, README.md, .gitmodules, crates/network/lib/model/policy/types.rs), agent-sandbox (README.md, api/v1beta1/groupversion_info.go, extensions/api/v1beta1/sandboxtemplate_types.go, extensions/controllers/sandboxtemplate_controller.go), monty (README.md, limitations/index.md, crates/monty-js/src/telemetry.rs, crates/fuzz/), agent-desktop (README.md, npm/package.json, npm/scripts/postinstall.js, skills/jev-desktop/SKILL.md, .github/workflows/supply-chain.yml), fara (LICENSE, README.md, pyproject.toml, src/fara/agents/fara/{_prompts.py, fara15_agent.py}) · Web: agent37.com/blog/daytona-alternative, developersdigest.tech/agent-sandboxes/daytona-oss (blog, chưa xác minh) · https://github.com/opensandbox-group/OpenSandbox · https://github.com/TencentCloud/CubeSandbox · https://github.com/superradcompany/microsandbox · https://github.com/kubernetes-sigs/agent-sandbox · https://github.com/pydantic/monty · https://github.com/vercel-labs/agent-desktop · https://github.com/microsoft/fara

## 3d. Nâng trần 2/11/2026: benchmark agent tái lập được và cách ly mức nhân/VM (yêu cầu người dùng)

> Cách làm: grep `data/projects.json` theo `repo` để loại trùng (gVisor, Firecracker, E2B, OpenSandbox, agent-sandbox… đã có); GitHub search API ngày 2/11/2026 (`repo:` cho từng ứng viên, thêm `browser agent benchmark`); clone `--depth 1 --filter=blob:none` 6 repo, đọc LICENSE, README, manifest, file task/chấm điểm và CI. **Không cài, không chạy mã của repo.**

**Trần hiện tại:**

- Công cụ browser và computer use đã có hồ sơ sâu (§1b–§1i, §3b–§3c), nhưng benchmark chỉ là **một dòng chữ** ở §2 (OSWorld, WebArena, Mind2Web, AgentDojo), không có repo, phiên bản hay cách chạy. Các con số đang trích như Agent S3 72,6% OSWorld (§3b) hay Fara 63,4% Online-Mind2Web (§3c) đều tự báo cáo, chưa có đường tái lập.
- Không có cổng đo **prompt injection** cho agent đọc web, dù §3b.1 của mục 10 và mục 12 đều nêu rủi ro này.
- Sandbox có gVisor, Firecracker, sandbox-runtime, microsandbox, OpenSandbox, agent-sandbox (§3b, §3c), nhưng **Kata Containers**, runtime mà agent-sandbox giao việc cách ly và CubeSandbox lấy agent, chưa có trong catalog. Cũng còn trống tầng jail tiến trình chạy trên server (namespace + seccomp) nằm giữa sandbox-runtime và microVM.

| Repo | Lớp | ★ · license (2/11/2026) | Commit cuối | Vì sao nâng trần | Rủi ro |
|---|---|---|---|---|---|
| `xlang-ai/OSWorld` | Chuẩn + cổng máy | 3,2k · Apache-2.0 | 2/11/2026 | Benchmark computer use trên VM thật: `evaluation_examples/test_all.json` có 368 task (chrome, gimp, LibreOffice Calc/Impress/Writer, multi_apps, os, thunderbird, vlc, vs_code), chấm bằng hàm kiểm trạng thái máy sau khi chạy. Bản **OSWorld-Verified** (28/7/2025) sửa lỗi task; provider gồm docker (KVM), VMware, VirtualBox, AWS, Azure, GCP, Modal, Daytona… | README tự cảnh báo: một số task cần tài khoản Google (OAuth) và proxy, thiếu cấu hình thì task fail và điểm thấp. Provider Daytona vẫn được hướng dẫn dù repo Daytona đã archive (§3c.1) |
| `web-arena-x/webarena` | Chuẩn | 1,6k · Apache-2.0 | 26/11/2025 | 812 task (`config_files/test.raw.json`) trên các site tự host (Docker hoặc AMI dựng sẵn), chấm bằng hàm kiểm URL, DOM, chuỗi; bản v0.2.0 sửa nhãn 10/2023 | Môi trường nặng (nhiều site); gần 1 năm không commit; nhãn gốc có lỗi nên ServiceNow làm WebArenaVerified (67★) |
| `ServiceNow/BrowserGym` | Cổng máy | 1,4k · Apache-2.0 (file LICENSE chỉ chứa đoạn thông báo Apache-2.0 ngắn (dòng "Copyright 2024 ServiceNow" cùng lời dẫn tới URL giấy phép) chứ không có toàn văn giấy phép, nên GitHub không nhận dạng được và báo NOASSERTION) | 28/10/2026 | Một API kiểu Gym cho MiniWoB, WebArena, WebArenaVerified, VisualWebArena, WorkArena, AssistantBench, WebLINX; cài từng phần (`browsergym-core`, `browsergym-miniwob`…); AgentLab (661★) chạy thí nghiệm và so agent | Chỉ là lớp bọc: vẫn phải tự dựng site của WebArena/WorkArena |
| `ethz-spylab/agentdojo` | Cổng máy (bảo mật) | 978 · MIT | 2/6/2026 (v0.1.35) | Đo cùng lúc **utility** và **tỷ lệ tấn công prompt injection thành công** trên 4 suite (workspace, slack, travel, banking), có registry tấn công (important_instructions, tool_knowledge, DoS…) và phòng thủ (`tool_filter`, detector qua extra `transformers`); kết quả công khai tại agentdojo.spylab.ai | README ghi API còn đang phát triển; agent dùng tool giả lập chứ không phải trình duyệt thật; 5 tháng không commit |
| `google/nsjail` | Đầu bảng (sandbox) | 4,2k · Apache-2.0 | 28/10/2026 | Jail tiến trình bằng namespace (UTS, MOUNT, PID, IPC, NET, USER, CGROUP, TIME), cgroup v1/v2, rlimit và seccomp-bpf viết bằng Kafel; cấu hình protobuf, có mẫu cho chromium/firefox; mạng tách hẳn hoặc userland (pasta) | README ghi "not an official Google product"; chỉ Linux; vẫn chia sẻ kernel host; phải build từ nguồn hoặc chạy Docker `--privileged` |
| `kata-containers/kata-containers` | Đầu bảng (sandbox) | 9,1k · Apache-2.0 | 2/11/2026 (4.3.1) | Container chạy trong microVM riêng, chọn hypervisor QEMU, Cloud Hypervisor, Firecracker hoặc Dragonball, cắm vào Kubernetes qua RuntimeClass. Là tầng cách ly thật dưới agent-sandbox (§3c). CI dày: OpenSSF Scorecard, zizmor, osv-scanner, cargo-deny, govulncheck, CodeQL | Cần KVM hoặc nested virtualization; vận hành phức tạp hơn gVisor |

**Stack nâng trần** (theo thứ tự lợi ích/công sức):

1. **AgentDojo cho mọi agent đọc nội dung ngoài:** đo tỷ lệ tấn công thành công trước và sau khi bật phòng thủ (allowlist tool, tách quyền như mục 12), giữ utility không giảm quá ngưỡng đặt trước.
2. **Đo browser agent bằng cùng một harness:** MiniWoB qua BrowserGym làm cổng CI nhanh; WebArenaVerified cho mỗi bản phát hành. So browser-use, Stagehand, playwright-mcp (§1c, §1f, §1h) trên cùng task thay vì tin số tự công bố.
3. **Tái lập số computer use:** chạy OSWorld-Verified bằng provider docker trên host có KVM, báo riêng số task lỗi do cấu hình (Google, proxy); kiểm lại số của Agent-S, UI-TARS, Fara (§3b, §3c) trên tập con trước khi chọn.
4. **Sandbox theo tầng:** máy dev → sandbox-runtime (§3b); code không tin cậy trên một server → nsjail không mạng + seccomp; đa người dùng trên Kubernetes → agent-sandbox (§3c) với RuntimeClass Kata hoặc gVisor (§3b).
5. **Chạy chính benchmark trong sandbox:** site của WebArena và VM của OSWorld chạy trong mạng riêng, không cho agent đang được đo ra Internet thật.

**Nguồn §3d:** GitHub search API 2/11/2026 (`repo:` cho 6 repo trên, `ServiceNow/webarena-verified`, `ServiceNow/AgentLab`; ứng viên loại: `MinorJerry/WebVoyager` 1,1k★ push cuối 4/3/2024, `OSU-NLP-Group/Mind2Web` 1,0k★ push cuối 5/11/2025) · clone `--depth 1 --filter=blob:none`, đọc: OSWorld (HEAD 7aa0559 2/11/2026; LICENSE, README.md, evaluation_examples/test_all.json, desktop_env/providers/), webarena (dce0468 26/11/2025; LICENSE, README.md, config_files/test.raw.json, .github/workflows/), BrowserGym (27a90ce 28/10/2026; LICENSE, README.md, .github/workflows/), agentdojo (089ed468 2/6/2026; LICENSE, README.md, pyproject.toml, src/agentdojo/default_suites/, src/agentdojo/attacks/), nsjail (d8415bc 28/10/2026; LICENSE, README.md, configs/), kata-containers (ea74fd9 2/11/2026; LICENSE, README.md, VERSION, versions.yaml, .github/workflows/) · https://github.com/xlang-ai/OSWorld · https://github.com/web-arena-x/webarena · https://github.com/ServiceNow/BrowserGym · https://github.com/ServiceNow/webarena-verified · https://github.com/ethz-spylab/agentdojo · https://arxiv.org/abs/2406.13352 · https://github.com/google/nsjail · https://github.com/kata-containers/kata-containers

## 3e. Nâng trần toàn diện 2/11/2026: kiểm hậu điều kiện và trạng thái tài khoản của browser agent

> Đọc LICENSE, README, CI và implementation của hai repo ở commit bên dưới; metadata GitHub lấy ngày 2/11/2026, cả hai chưa archive. **Chỉ đọc mã; chưa cài browser, chưa chạy test/benchmark, chưa dùng tài khoản thật.** Playwright MCP/CLI (§1f–§1g) và BrowserGym (§3d) đã có; bổ sung runner gốc và lớp quản lý thí nghiệm, không thêm lại chúng dưới tên khác.

| Dự án | ★ · license (đọc 2/11/2026) | HEAD / ngày commit | Lớp và điều kiện dùng |
|---|---|---|---|
| [Playwright](https://github.com/microsoft/playwright) | 99,090 · Apache-2.0 | `820620c98b35` · 2026-11-01 | Runner/library gốc; assertion hậu điều kiện và tách auth state; khác repo MCP/CLI |
| [AgentLab](https://github.com/ServiceNow/AgentLab) | 661 · Apache-2.0 (notice) | `8488c564eea0` · 2026-10-05 | Thí nghiệm BrowserGym; strict_reproducibility mặc định false, relaunch_errors có thể chạy lại lỗi |

### Playwright

Runner/library gốc của Microsoft cho Chromium, Firefox, WebKit. [Actionability](https://github.com/microsoft/playwright/blob/820620c98b359f4bb16e1596fd16d6b1a354b2f3/docs/src/actionability.md) kiểm điều kiện trước thao tác; `click()` thành công không chứng minh đơn hàng đã tạo đúng. Ghép assertion hậu điều kiện (`toHaveURL`, trạng thái DOM) với truy vấn backend đọc lại entity vừa ghi khi ứng dụng có API test. [Matcher URL](https://github.com/microsoft/playwright/blob/820620c98b359f4bb16e1596fd16d6b1a354b2f3/packages/playwright/src/matchers/toHaveURL.ts) cho thấy assertion retry theo điều kiện, không cần dùng một khoảng `sleep` đoán trước. Framework không tự hiểu đúng nghiệp vụ; expected outcome phải do test/task xác định độc lập với agent.

[Hướng dẫn auth](https://github.com/microsoft/playwright/blob/820620c98b359f4bb16e1596fd16d6b1a354b2f3/docs/src/auth.md) và [BrowserContext](https://github.com/microsoft/playwright/blob/820620c98b359f4bb16e1596fd16d6b1a354b2f3/packages/playwright-core/src/server/browserContext.ts) cho thấy context mới có thể nạp lại storage state. IndexedDB phải bật khi snapshot nếu ứng dụng dùng nó; cookie/localStorage/credential vẫn là bí mật. Một context riêng không xoá dữ liệu trên server. Với test sửa trạng thái chung, dùng tài khoản/dataset riêng cho từng worker và tenant; state hết hạn phải cấp lại. CI [tests_primary](https://github.com/microsoft/playwright/blob/820620c98b359f4bb16e1596fd16d6b1a354b2f3/.github/workflows/tests_primary.yml) có matrix ba browser, nhưng kho này chưa chạy matrix đó. So với MCP/CLI, runner phù hợp làm người chấm tất định và regression gate cho hành động agent tạo ra.

### AgentLab

Framework nghiên cứu của ServiceNow trên BrowserGym, quản lý study, song song, kết quả và thông tin tái lập. [Reproducibility util](https://github.com/ServiceNow/AgentLab/blob/8488c564eea0525aaff5dea189bb03a9b529546e/src/agentlab/experiments/reproducibility_util.py) ghi phiên bản benchmark/package/git; [Study](https://github.com/ServiceNow/AgentLab/blob/8488c564eea0525aaff5dea189bb03a9b529546e/src/agentlab/experiments/study.py) có `strict_reproducibility=False`, `n_relaunch=3`, `relaunch_errors=True` ở API chạy study. Muốn cổng so sánh nghiêm cần bật chế độ strict và giữ báo cáo mọi lượt, tránh chỉ nhìn kết quả sau retry. LICENSE là notice dẫn Apache-2.0, GitHub trả NOASSERTION; không suy ra MIT từ đường link badge trong README. CI [unit_tests](https://github.com/ServiceNow/AgentLab/blob/8488c564eea0525aaff5dea189bb03a9b529546e/.github/workflows/unit_tests.yml) chạy MiniWoB và bỏ nhóm `pricy`, nên CI xanh cũng không có nghĩa toàn benchmark/model trả phí đã được kiểm. Cần môi trường site/task từ BrowserGym, không phải sản phẩm automation cho người dùng cuối.

**Bảng lựa chọn:**

| Nhu cầu | Lớp thích hợp | Điều phải tự bổ sung |
|---|---|---|
| Agent thao tác trang web thay đổi thường xuyên | Browser Use/Stagehand/MCP/CLI (§1c–§1h) | Giới hạn quyền + nhiệm vụ + người chấm độc lập |
| Kiểm thao tác đã đạt nghiệp vụ | Playwright assertions + API đọc lại | Expected state, fixture và kiểm tác dụng phụ |
| So agent/model trên cùng tập task | BrowserGym (§3d) + AgentLab | Site/version/seed/model giống nhau, tách lỗi môi trường |
| Dùng browser đã đăng nhập của người thật | Các bridge §1d–§1h | Chính sách account/session, phê duyệt hành động, audit; snapshot không chứng minh đủ quyền |

**Chuỗi kiểm hành động:** chụp tiền trạng thái → xác định account/tenant/resource → agent đề xuất hành động → cổng quyền (mục 12 §4d) → thực thi → người chấm đọc hậu trạng thái → lưu receipt/outcome. Tác vụ tạo/xoá/gửi phải có kiểm dữ kiện nghiệp vụ; ảnh và dòng “success” chỉ là một phần bằng chứng. Đây là kiến trúc đề xuất, không phải tính năng được tự động bảo đảm bởi hai repo.

| Ca hồi quy đề xuất | Kết quả mong đợi |
|---|---|
| Submit trả HTTP lỗi nhưng UI đóng dialog | Fail; không ghi thành công chỉ vì đã click |
| Hai worker đổi cùng profile | Dữ liệu được cô lập, hoặc test khai rõ kiểm cạnh tranh |
| Session hết hạn/đổi role/nhảy tenant | Dừng, xác thực và kiểm quyền lại; không âm thầm dùng cookie tài khoản khác |
| Task lỗi môi trường được relaunch | Giữ cả lần lỗi và retry; báo riêng số task không chạy được, cùng mẫu số gốc |
| Prompt injection trên trang | Chấm cả utility và ASR bằng AgentDojo (§3d), không chỉ tỷ lệ hoàn thành |

**Giới hạn:** context browser không phải sandbox OS; bảo vệ trace/storage state vì có thể chứa token/nội dung riêng. Hậu điều kiện DOM có thể bị UI đánh lừa; API/dữ liệu cuối đáng tin hơn khi có quyền kiểm. Benchmark tự host không đại diện hoàn toàn cho CAPTCHA, OAuth và dịch vụ thật. Không có số tỷ lệ thành công mới nào do kho này đo.

**Nguồn §3e:** [Playwright LICENSE](https://github.com/microsoft/playwright/blob/820620c98b359f4bb16e1596fd16d6b1a354b2f3/LICENSE); [AgentLab LICENSE](https://github.com/ServiceNow/AgentLab/blob/8488c564eea0525aaff5dea189bb03a9b529546e/LICENSE); [Playwright auth](https://playwright.dev/docs/auth), [BrowserGym ecosystem paper](https://arxiv.org/abs/2412.05467). Nguồn implementation và CI được ghim ngay trong hồ sơ.

## 3f. Hồ sơ radareorg/radare2 (r2): bộ công cụ dịch ngược dòng lệnh, nay có AGENTS.md, MCP server và r2ai cho agent (ảnh README người dùng gửi, đọc mã 3/11/2026)

> Ảnh là phần đầu README: logo r2, "Radare2: Libre Reversing Framework for Unix Geeks", badge CI, build, tcc (đều passing), "openssf best practices in progress 82%", "coverity passed 4 new defects", "radare 1.1K members", dòng "Current git master branch is 6.2.5, next release will be 6.2.6", ảnh chụp giao diện panels (thanh ghi, menu, disassembly, danh sách hàm, graph). Đã clone `--filter=blob:none` đủ lịch sử, HEAD `55b6a167acef2fbc8fd94776c1cdee2448a30ecb` (2/11/2026). **Không build, không chạy.** Dịch ngược là công cụ hai mặt: chỉ dùng trên phần mềm của mình hoặc khi được phép (CTF, nghiên cứu, kiểm thử có hợp đồng).

### 3f.1 Kiểm ảnh

| Ô trong ảnh | Kết quả | Đối chiếu (3/11/2026) |
|---|---|---|
| "master is 6.2.5, next release 6.2.6" | ✅ đúng nghĩa nhánh phát triển | `configure.acr:2` `VERSION 6.2.5`. Nhưng **tag phát hành mới nhất là 6.2.4** (5/10/2026); dãy tag 6.2.0, 6.2.2, 6.2.4 cho thấy số lẻ là bản đang phát triển. Ai cài bản phát hành sẽ nhận 6.2.4 |
| "Distributed under LGPLv3, despite each plugin can have different licenses (see `r2 -Lj`)" | ✅ | `COPYING.md`: phần lớn LGPLv3, plugin và phụ thuộc có license khác; có cờ `--without-gpl` để bỏ phần GPL khi build tĩnh. GitHub hiển thị `NOASSERTION` vì có nhiều license |
| "embedded Javascript interpreter or via r2pipe" | ✅ | QuickJS nằm trong `shlr/qjs`, plugin ngôn ngữ `libr/lang/p/qjs.c`. r2pipe ở repo riêng `radareorg/radare2-r2pipe` (468★) |
| Badge CI, build, tcc, Coverity | ✅ có workflow | `.github/workflows/`: `ci.yml`, `build.yml`, `tcc.yml`, `coverity-scan.yml`, `codeql-analysis.yml`, `semgrep.yml`, `qemu.yml`. Trạng thái passing và "4 new defects" của Coverity là ảnh chụp tại thời điểm đó **(không kiểm lại)** |
| "openssf best practices in progress 82%" | ⚠️ chưa đạt | Badge tự nó ghi là đang làm, chưa đạt mức passing |
| ★ | – | 25.282★, 3.407 fork, 792 issue+PR mở (GitHub search API) |

### 3f.2 Đọc mã: điều đáng ghi

- **Dự án lâu đời, một người dẫn dắt.** 38.595 commit từ 5/2/2009. Từ 1/8/2026 có 2.056 commit, trong đó `pancake` (Sergi Àlvarez, hai email) chiếm khoảng 1.337, tức hơn 60%. Chỉ 9 commit có trailer Co-Authored-By Claude/Anthropic.
- **Có `AGENTS.md` cho agent viết mã**: sửa nhỏ nhất có thể, tìm symbol trước rồi chỉ đọc phần liên quan, theo quy ước bộ nhớ (kiểm overflow bằng `r_mul_overflow_*` trước khi cấp phát, cấm `alloca` và mảng độ dài biến đổi trên stack), build bằng `make` ở gốc chứ không biên dịch lẻ từng file, test theo `test/db/` (1.051 file). Đây là mẫu AGENTS.md tốt cho codebase C lớn: ghi đúng quy ước mà agent hay vi phạm.
- **Hệ sinh thái cho agent** (org `radareorg`): `radare2-mcp` (347★, MIT, "MCP stdio server for radare2", push 15/10/2026) và `r2ai` (508★, MIT, "LLM-based reversing", push 2/11/2026); GUI chính thức `iaito` (GPL-3.0); decompiler `r2ghidra`.
- ⚠️ **Chính sách bảo mật lạ**: `SECURITY.md` yêu cầu báo lỗ hổng bằng **issue công khai** trên GitHub ("We don't believe in secrecy when security matters"), cam kết sửa trong 24 giờ và **không backport** bản vá cho bản cũ. Hệ quả: phải theo bản mới nhất, và khi mở file hay binary không tin cậy bằng r2 thì nên chạy trong sandbox hoặc máy ảo (mục 11 §3).
- Cách cài khuyến nghị là build từ git bằng `sys/install.sh`, script dùng `sudo` để cài symlink vào hệ thống. Có thể cài qua `r2env` (pip) hoặc trình quản lý gói (Homebrew, MacPorts…) nếu không muốn chạy script với quyền root.
- Không thấy mã telemetry (grep chỉ khớp tên syscall `telemetry` trong bảng syscall Darwin).

### 3f.3 So với cùng loại

| Công cụ | ★ (3/11) | License | Khác r2 |
|---|---|---|---|
| **radareorg/radare2** | 25k | LGPLv3 (+plugin khác) | Dòng lệnh, nhẹ, script bằng JS/r2pipe, nhiều kiến trúc, debug và emulate (ESIL) |
| Ghidra (NSA) | – | Apache-2.0 | GUI Java, decompiler mạnh; r2 dùng lại qua `r2ghidra` |
| `rizinorg/rizin` | – | LGPLv3 | Fork của radare2 từ 2020, ưu tiên API ổn định **(không đọc mã)** |
| `morluto/rea` (mục 23 §6.4) | API trả số bất thường | MIT | CLI + MCP 95 tool cho agent, có thể dùng Ghidra/Hopper |
| Craft Anything (mục 01 §3m) | 4,2k | MIT/Apache-2.0 | Engine dịch ngược Rust tự viết + agent dựng lại sản phẩm |

**Dùng thế nào:** cho agent dùng r2 qua `radare2-mcp` thay vì để agent tự gõ lệnh shell; chạy trong container hoặc máy ảo khi phân tích binary lạ; ghim bản phát hành (6.2.4) nếu cần ổn định, hoặc theo master nếu cần bản vá bảo mật mới nhất (vì không có backport).

**Nguồn §3f:** ảnh README người dùng gửi 3/11/2026 · clone https://github.com/radareorg/radare2 HEAD `55b6a167acef2fbc8fd94776c1cdee2448a30ecb`: https://github.com/radareorg/radare2/blob/55b6a167acef2fbc8fd94776c1cdee2448a30ecb/README.md · https://github.com/radareorg/radare2/blob/55b6a167acef2fbc8fd94776c1cdee2448a30ecb/COPYING.md · https://github.com/radareorg/radare2/blob/55b6a167acef2fbc8fd94776c1cdee2448a30ecb/AGENTS.md · https://github.com/radareorg/radare2/blob/55b6a167acef2fbc8fd94776c1cdee2448a30ecb/SECURITY.md · https://github.com/radareorg/radare2/blob/55b6a167acef2fbc8fd94776c1cdee2448a30ecb/configure.acr · `shlr/qjs`, `libr/lang/p/qjs.c`, `.github/workflows/*`, `sys/install.sh`, `test/db/`; `git tag`, `git shortlog --since=2026-08-01` · GitHub search API `repo:radareorg/radare2`, `org:radareorg` 3/11/2026.

## 3g. Nâng trần 4/11/2026: sandbox theo hợp đồng quyền cho xưởng phần mềm

**Trần hiện tại:** kho đã có browser agent, benchmark và sandbox VM/kernel. Chỗ cần sâu thêm là hợp đồng quyền kiểm được cho từng tác vụ: đường dẫn được ghi, dữ liệu được đọc, đích mạng, secret và hậu điều kiện. Một browser agent hoàn thành bước UI không chứng minh tác dụng nghiệp vụ đúng, cũng không chứng minh shell của agent đã được cách ly.

<a id="factory-2026-11-04-bubblewrap"></a>

### Bubblewrap: cơ chế namespace cần một chính sách bên ngoài

| Thuộc tính | Kết quả đọc |
|---|---|
| Repo · phiên bản | `containers/bubblewrap` · `1fb0aa26d3eb66254f7742e704add7f82f41a582` |
| License | File `LICENSE` là LGPL 2.1; header `bubblewrap.c` ghi `LGPL-2.0-or-later`. Giữ khác biệt theo file khi đóng gói, không gán toàn cây một SPDX tùy ý |
| Cơ chế | CLI nhận mount bind chỉ đọc/ghi, namespace mạng/PID/user, môi trường và seccomp; chính đối số của wrapper quyết định phạm vi bảo vệ |
| Đường gọi đã đọc | `bubblewrap.c`: parse `--unshare-net`, `--ro-bind`, `--seccomp`, `--new-session`; thiết lập bind mount kiểm loại đích; `--not-a-security-boundary` thêm `BIND_FAIL_OPEN` |
| CI đã đọc | `.github/workflows/check.yml` build Meson với sanitizer, chạy test với `BWRAP_MUST_WORK=1`; đây là nội dung workflow, chưa kiểm kết quả từng run |
| Giới hạn | Dùng chung kernel Linux; không tự cấp CPU/RAM/time quota; không thay firewall/proxy ứng dụng. Cờ `--not-a-security-boundary` không phù hợp nơi cần ranh giới bảo mật; user namespace có thể bị kernel/host vô hiệu hóa |

**Phạm vi kiểm (2026-11-04):** đọc tài liệu, LICENSE, mã đường gọi và workflow tại SHA dưới đây; không cài/chạy upstream. Các cổng nghiệm thu là đề xuất cho repo tích hợp, chưa phải kết quả chạy của kho. Số sao không thu thập trong đợt này.

| Lựa chọn | Khi phù hợp | Điều xưởng vẫn phải chứng minh |
|---|---|---|
| Bubblewrap | Job Linux ngắn, wrapper quyền nhỏ cần kiểm soát mount cụ thể | Chỉ mount đúng input; không đọc home/secret; không ghi host; network đúng scope; timeout/quota ở lớp ngoài |
| [nsjail](README.md#3d-nâng-trần-2112026-benchmark-agent-tái-lập-được-và-cách-ly-mức-nhânvm-yêu-cầu-người-dùng) | Cần policy namespace/seccomp và hạn mức theo process | Profile kernel/namespace thật sự được áp dụng ở host đích |
| gVisor | Muốn giảm bề mặt syscall của container bằng user-space kernel | Tương thích workload, mount/egress và overhead đo trên workload thật |
| Firecracker / Kata Containers | Tác vụ không tin cậy hoặc tenant cần ranh giới VM | KVM/host, image digest, mạng và xóa tài nguyên sau job; không suy an toàn chỉ từ tên microVM |

**Stack tích hợp:** phân loại job theo độ tin cậy → dựng wrapper quyền từ manifest đã review → chạy agent trong vùng dữ liệu giả → kiểm trạng thái đích bằng API/DB/locator tất định → thu artifact đã lọc → hủy môi trường. Với browser, credential/session của mỗi tenant phải có vòng đời riêng; không tái dùng profile đăng nhập thật giữa các job.

**Cổng nghiệm thu:** fixture độc hại thử đọc một tệp sentinel ngoài input, ghi ra ngoài output, gọi đích mạng ngoài scope và sống quá timeout đều phải bị chặn; fixture hợp lệ vẫn chạy. Lưu exit status, profile hash, namespace/runner identity và hậu điều kiện nghiệp vụ. Một lệnh `true` trong sandbox chỉ kiểm startup; không thay các phép thử phủ định trên. Liên kết [kiểm thử phần mềm](../30-software-testing-quality/README.md) và [chuỗi cung ứng](../31-software-supply-chain-security/README.md) để image, dependency và chính wrapper cũng được kiểm.

**Nguồn §3g:** [README: security/limitations](https://github.com/containers/bubblewrap/blob/1fb0aa26d3eb66254f7742e704add7f82f41a582/README.md) · [LICENSE](https://github.com/containers/bubblewrap/blob/1fb0aa26d3eb66254f7742e704add7f82f41a582/LICENSE) · [callsite](https://github.com/containers/bubblewrap/blob/1fb0aa26d3eb66254f7742e704add7f82f41a582/bubblewrap.c) · [CI](https://github.com/containers/bubblewrap/blob/1fb0aa26d3eb66254f7742e704add7f82f41a582/.github/workflows/check.yml).

## 3h. Hồ sơ vercel-labs/agent-desktop: computer use cho AI agent qua accessibility tree trên macOS, Windows, Linux (ảnh README người dùng gửi, đọc mã 6/11/2026)

> Ảnh là phần đầu README: "Computer use for AI agents: see and operate desktop apps on macOS, Windows, and Linux through the OS accessibility tree", badge Vercel LABS PRODUCT, npm v1.2.0, Apache-2.0, 31K/month; mô tả không dùng ảnh chụp hay so pixel, trả cây accessibility dạng JSON có ref cho từng phần tử, vòng lặp nằm ở agent, phát hành dạng CLI và thư viện C. §3c.3 trước đây chỉ có một đoạn ngắn. Đã clone `--filter=blob:none` đủ lịch sử, HEAD `b43ac4f6e892ef608f8851428613c4009f0e84c7` (5/11/2026, tag v1.2.0). **Không cài, không chạy.**

### 3h.1 Hồ sơ nhanh

| Thuộc tính | Giá trị (6/11/2026) |
|---|---|
| Repo | https://github.com/vercel-labs/agent-desktop · **17.675★** (GitHub search API; 4.217★ ngày 31/10), Apache-2.0, tạo 19/2/2026 |
| npm | `agent-desktop` 1.2.0, **46.698 lượt tải** từ 7/10 tới 5/11/2026 (api.npmjs.org) |
| Mã | Rust workspace: `crates/core`, `crates/ffi` (thư viện C `libagent_desktop_ffi`), mỗi hệ điều hành một crate (`macos` AX API, `windows` UI Automation, `linux` AT-SPI) chọn lúc build; 335 commit, tác giả chính Lahfir |
| Lệnh | 60 tên lệnh, 56 lệnh chạy được: quan sát (`snapshot`, `find`, `get`, `is`, `screenshot`), thao tác theo ref (`click`, `type`, `set-value`, `select`, `toggle`, `scroll-to`…), bàn phím và chuột, ứng dụng và cửa sổ, thông báo, clipboard, `wait`, session và `trace`, `batch` |
| Nền tảng | macOS 13+ (Intel, Apple Silicon); Windows 10 1809+ (x64, ARM64); Linux Ubuntu 24.04+ (x86_64, aarch64, X11 hoặc Wayland) |
| Kiểm thử | 6.701 test Rust; CI gồm `ci.yml`, `linux-e2e.yml`, `native-e2e.yml`, `windows-capability-probe.yml`, `codeql.yml`, `supply-chain.yml`, `release-dry-run.yml`; `benchmarks/locator-resolution`; thư mục `probes/` |

### 3h.2 Điểm mạnh

- **Không cần ảnh chụp hay mô hình thị giác**: đọc thẳng cây accessibility của hệ điều hành, nên rẻ, nhanh và chính xác hơn đoán pixel; agent nào cũng dùng được vì agent-desktop không chứa model.
- **Ref gắn với snapshot**: mỗi phần tử có ref dạng `@s8f3k2p9:e8`; ref trần bị từ chối (`INVALID_ARGS`); khi UI đổi, thao tác trả `STALE_REF` hoặc `AMBIGUOUS_TARGET` để agent chụp lại thay vì bấm nhầm. Mỗi lệnh in một JSON envelope; lỗi có `error.disposition.retry`, chỉ thử lại khi giá trị là `safe`.
- **Chạy nền mặc định**: thao tác theo ref dùng accessibility API, không di chuột hay lấy focus, nên không làm phiền người đang dùng máy; cần thì bật `--headed`.
- **App dày đặc**: `snapshot --skeleton … --compact` để có bản đồ trước, rồi `--root @ref` để đi sâu một vùng, giữ ngữ cảnh của agent gọn.
- **Chờ sau thao tác có phạm vi rõ**: ref gắn với cửa sổ gốc (kể cả sheet, alert, popover), lệnh chờ đọc đúng cửa sổ đó.
- **Giữ bí mật ngoài tham số tiến trình**: `type`, `set-value`, `clipboard-set` nhận `--stdin`. README nhắc snapshot, clipboard, ảnh chụp và log debug có thể chứa nội dung riêng tư, nên giữ ngoài log và upload công khai.
- **Ba cách nối vào agent**: CLI; `agent-desktop mcp` phục vụ mọi lệnh thành tool MCP qua stdio (`desktop_snapshot`, `desktop_click`…); thư viện C để gọi trong tiến trình (có kiểm phiên bản ABI). Binary kèm hướng dẫn đúng phiên bản: `agent-desktop skills get desktop` và `skills get platform`; skill cài qua `npx skills add`.
- **Chuỗi phát hành cẩn thận** (theo §3c.3 và CI hiện tại): `postinstall` của npm tải binary từ GitHub Releases và kiểm SHA-256; CI có CodeQL và workflow kiểm chuỗi cung ứng.

### 3h.3 Dùng thế nào

```bash
npm install -g agent-desktop
agent-desktop snapshot --app Finder -i
agent-desktop click @s8f3k2p9:e8
agent-desktop snapshot --app Finder -i
```

Với Claude Code hoặc client MCP khác: thêm `{"mcpServers": {"agent-desktop": {"command": "agent-desktop", "args": ["mcp"]}}}`. Trước lần dùng đầu, cho agent đọc `agent-desktop skills get desktop` và `skills get platform`. Cùng nhà với `agent-browser` (§1h.2) cho trình duyệt.

**Nguồn §3h:** ảnh README người dùng gửi 6/11/2026 · clone https://github.com/vercel-labs/agent-desktop HEAD `b43ac4f6e892ef608f8851428613c4009f0e84c7`: https://github.com/vercel-labs/agent-desktop/blob/b43ac4f6e892ef608f8851428613c4009f0e84c7/README.md · https://github.com/vercel-labs/agent-desktop/blob/b43ac4f6e892ef608f8851428613c4009f0e84c7/LICENSE · https://github.com/vercel-labs/agent-desktop/blob/b43ac4f6e892ef608f8851428613c4009f0e84c7/Cargo.toml · `crates/{core,ffi,macos,windows,linux}`, `.github/workflows/*`, `benchmarks/` · https://registry.npmjs.org/agent-desktop (1.2.0) · https://api.npmjs.org/downloads/point/last-month/agent-desktop · GitHub search API 6/11/2026.

<a id="anhkysuai-2026-11-23"></a>

## Đánh giá từ kho Anh Kỹ Sư AI — 23/11/2026

Phần này có **13 hồ sơ hoặc phạm vi đối chiếu** từ [nguồn tuyển chọn](https://anhkysuai.com/kho/). [Bảng đủ 1.295 repo](../data/collections/anhkysuai-kho.json) ghi trạng thái đối chiếu từng link; [danh sách URL](../data/collections/anhkysuai-kho-links.txt) phục vụ tra cứu. Nguồn tuyển chọn giúp phát hiện repo; đánh giá bên dưới dựa trên clone và permalink upstream cùng metadata GitHub ngày 2026-11-23.

Mức `docs-read`/`code-read` chỉ áp dụng phạm vi ghi tại mỗi hồ sơ. Chưa cài, build, chạy test hay benchmark mã upstream. Giấy phép có thể tách theo code, model, nội dung, asset hoặc bản enterprise; con số/tuyên bố của tác giả chưa được tái lập nếu không có ghi chú khác.

<a id="anhkysuai-2026-11-23-lightpanda"></a>

### Lightpanda

**Repo:** [lightpanda-io/browser](https://github.com/lightpanda-io/browser) · **License:** AGPL-3.0-only · **★ 42,394 (GitHub API, 2026-11-23)**

**Mục đích:** Trình duyệt headless viết bằng Zig cho tự động hóa và thu thập web.

**Giá trị và cơ chế:** Đã đọc telemetry: init tắt nếu biến LIGHTPANDA_DISABLE_TELEMETRY tồn tại, record trả sớm khi tắt; mặc định có gửi event tới telemetry.lightpanda.io/v2. Callsite main ghi sự kiện chạy.

**Giới hạn:** Chỉ kiểm nhánh telemetry, chưa chứng minh tương thích CDP hoặc các số tăng tốc upstream. Khi cần tắt, sự hiện diện biến môi trường là điều kiện, không phải kiểm giá trị true/false.

**Cách tham khảo/tích hợp:** Thử corpus website đích và đặt LIGHTPANDA_DISABLE_TELEMETRY=true nếu không muốn gửi số liệu sử dụng.

**Thay thế:** [Playwright](../11-browser-computer-use-sandbox/README.md#playwright), [Browser Use](https://github.com/browser-use/browser-use), [Stagehand](https://github.com/browserbase/stagehand).

**Bằng chứng:** `code-read`, ngày 2026-11-23, commit [`a33cb1cc4694`](https://github.com/lightpanda-io/browser/commit/a33cb1cc469400fdbd20c7d1776abec399047ad7). Luồng telemetry init/record/send, callsite main và CI e2e; không kiểm toàn engine browser. Chưa cài/chạy upstream.

**Nguồn:** [README.md](https://github.com/lightpanda-io/browser/blob/a33cb1cc469400fdbd20c7d1776abec399047ad7/README.md) · [LICENSE](https://github.com/lightpanda-io/browser/blob/a33cb1cc469400fdbd20c7d1776abec399047ad7/LICENSE) · [src/telemetry/lightpanda.zig](https://github.com/lightpanda-io/browser/blob/a33cb1cc469400fdbd20c7d1776abec399047ad7/src/telemetry/lightpanda.zig) · [src/telemetry/telemetry.zig](https://github.com/lightpanda-io/browser/blob/a33cb1cc469400fdbd20c7d1776abec399047ad7/src/telemetry/telemetry.zig) · [src/main.zig](https://github.com/lightpanda-io/browser/blob/a33cb1cc469400fdbd20c7d1776abec399047ad7/src/main.zig) · [LICENSING.md](https://github.com/lightpanda-io/browser/blob/a33cb1cc469400fdbd20c7d1776abec399047ad7/LICENSING.md) · [metadata GitHub](https://api.github.com/repos/lightpanda-io/browser).

<a id="anhkysuai-2026-11-23-nanobrowser"></a>

### Nanobrowser

**Repo:** [nanobrowser/nanobrowser](https://github.com/nanobrowser/nanobrowser) · **License:** Apache-2.0 · **★ 14,371 (GitHub API, 2026-11-23)**

**Mục đích:** Tiện ích browser cho agent đọc trang, thao tác và quản lý tác vụ qua side panel.

**Giá trị và cơ chế:** Đọc URL policy thấy chặn scheme nguy hiểm, ghép allow/deny và blocked-site; bài check gọi session.navigate/tabs có ca redirect và history. Chưa chạy các ca này.

**Giới hạn:** CI nói browser/model checks chạy thủ công. Privacy policy ghi gửi nội dung tới model đã chọn và analytics tổng hợp mặc định bật; không gọi hoàn toàn offline. Ask/Auto có phạm vi chấp thuận khác nhau.

**Cách tham khảo/tích hợp:** Dùng profile browser thử, cấu hình site rules và provider, kiểm các bước gửi/xóa trước cấp quyền trang thật.

**Thay thế:** [Browser Use](https://github.com/browser-use/browser-use), [Skyvern](https://github.com/Skyvern-AI/skyvern), [Stagehand](https://github.com/browserbase/stagehand).

**Bằng chứng:** `code-read`, ngày 2026-11-23, commit [`291d5f3927ee`](https://github.com/nanobrowser/nanobrowser/commit/291d5f3927ee4c4795b0ea4588f2b404838b3ff6). URL policy và các ca gọi session trong navigation check, cùng CI; chưa chạy browser checks. Chưa cài/chạy upstream.

**Nguồn:** [README.md](https://github.com/nanobrowser/nanobrowser/blob/291d5f3927ee4c4795b0ea4588f2b404838b3ff6/README.md) · [LICENSE](https://github.com/nanobrowser/nanobrowser/blob/291d5f3927ee4c4795b0ea4588f2b404838b3ff6/LICENSE) · [src/background/checks/navigation-policy.ts](https://github.com/nanobrowser/nanobrowser/blob/291d5f3927ee4c4795b0ea4588f2b404838b3ff6/src/background/checks/navigation-policy.ts) · [src/browser-control/core/url-policy.ts](https://github.com/nanobrowser/nanobrowser/blob/291d5f3927ee4c4795b0ea4588f2b404838b3ff6/src/browser-control/core/url-policy.ts) · [PRIVACY.md](https://github.com/nanobrowser/nanobrowser/blob/291d5f3927ee4c4795b0ea4588f2b404838b3ff6/PRIVACY.md) · [metadata GitHub](https://api.github.com/repos/nanobrowser/nanobrowser).

<a id="anhkysuai-2026-11-23-robotgo"></a>

### RobotGo

**Repo:** [go-vgo/robotgo](https://github.com/go-vgo/robotgo) · **License:** Apache-2.0; một số thành phần BSD-like · **★ 10,912 (GitHub API, 2026-11-23)**

**Mục đích:** Thư viện Go tự động hóa chuột, bàn phím, màn hình và cửa sổ desktop.

**Giá trị và cơ chế:** README và go.mod cho thấy backend native/Cgo và pure Go theo nền tảng; thích hợp lớp công cụ computer-use hoặc kiểm thử giao diện desktop.

**Giới hạn:** Chưa gửi input hay chụp màn hình thử. macOS cần quyền riêng, hỗ trợ Wayland/X11 và thao tác cửa sổ tùy backend; RobotGo-Pro không nằm trong mã mở này.

**Cách tham khảo/tích hợp:** Dùng desktop thử, kiểm tọa độ/DPI và quyền hệ điều hành, thêm chốt xác nhận ở luồng hành động nhạy cảm.

**Thay thế:** pyautogui, nut-js, xdotool.

**Bằng chứng:** `docs-read`, ngày 2026-11-23, commit [`513810704bd4`](https://github.com/go-vgo/robotgo/commit/513810704bd4d5a624db272ecb8537d614f99a54). README và các tài liệu/manifest/CI hiện diện, đọc chọn lọc; chưa kiểm implementation. Chưa cài/chạy upstream.

**Nguồn:** [README.md](https://github.com/go-vgo/robotgo/blob/513810704bd4d5a624db272ecb8537d614f99a54/README.md) · [LICENSE](https://github.com/go-vgo/robotgo/blob/513810704bd4d5a624db272ecb8537d614f99a54/LICENSE) · [metadata GitHub](https://api.github.com/repos/go-vgo/robotgo).

<a id="anhkysuai-2026-11-23-browser-use-web-ui"></a>

### Browser Use WebUI

**Repo:** [browser-use/web-ui](https://github.com/browser-use/web-ui) · **License:** MIT · **★ 16,664 (GitHub API, 2026-11-23)**

**Mục đích:** Giao diện Gradio để cấu hình và chạy tác vụ browser-use với nhiều nhà cung cấp model.

**Giá trị và cơ chế:** Đã đọc đường truyền cấu hình từ UI vào BrowserConfig/context và khởi chạy agent. CustomBrowser dựng launch arguments; cờ disable_security thêm các tham số tắt bảo vệ trình duyệt.

**Giới hạn:** Phạm vi đọc là launch/configuration và callsite, chưa kiểm toàn bộ agent hoặc ranh giới quyền. Dùng profile trình duyệt thật có thể đưa session và nội dung trang vào tác vụ; CI đã đọc chỉ build image.

**Cách tham khảo/tích hợp:** Dùng profile thử riêng, giữ cấu hình bảo vệ và giới hạn tài khoản trước khi đánh giá các tác vụ có đăng nhập.

**Thay thế:** nanobrowser, [Stagehand](https://github.com/browserbase/stagehand), [Skyvern](https://github.com/Skyvern-AI/skyvern).

**Bằng chứng:** `code-read`, ngày 2026-11-23, commit [`61962296c38a`](https://github.com/browser-use/web-ui/commit/61962296c38a0d064e0ba02c827192b7a81d1819). Đọc browser launch, truyền cấu hình context từ UI và callsite agent.run; đọc workflow build Docker, chưa kiểm toàn bộ agent hoặc runtime permissions. Chưa cài/chạy upstream.

**Nguồn:** [README.md](https://github.com/browser-use/web-ui/blob/61962296c38a0d064e0ba02c827192b7a81d1819/README.md) · [LICENSE](https://github.com/browser-use/web-ui/blob/61962296c38a0d064e0ba02c827192b7a81d1819/LICENSE) · [src/browser/custom_browser.py](https://github.com/browser-use/web-ui/blob/61962296c38a0d064e0ba02c827192b7a81d1819/src/browser/custom_browser.py) · [src/webui/components/browser_use_agent_tab.py](https://github.com/browser-use/web-ui/blob/61962296c38a0d064e0ba02c827192b7a81d1819/src/webui/components/browser_use_agent_tab.py) · [SECURITY.md](https://github.com/browser-use/web-ui/blob/61962296c38a0d064e0ba02c827192b7a81d1819/SECURITY.md) · [metadata GitHub](https://api.github.com/repos/browser-use/web-ui).

<a id="anhkysuai-searxng-searxng"></a>

### SearXNG

**Repo:** [searxng/searxng](https://github.com/searxng/searxng) · **License:** AGPL-3.0-or-later · **Kiểm:** 2026-11-23, `docs-read`, [`a7163d091037`](https://github.com/searxng/searxng/tree/a7163d091037cae586c444b05f22ecca162bb492) (commit 2026-11-23). **Sao:** 39,800 tại 2026-11-23 theo [GitHub API](https://api.github.com/repos/searxng/searxng).

| Mục | Đánh giá |
|---|---|
| Mục đích | Metasearch tự host, gom kết quả từ nhiều công cụ tìm kiếm. |
| Giá trị và cơ chế theo tài liệu | README dẫn cấu hình engine và triển khai; cấu trúc Python cùng công cụ frontend cung cấp nền cho dịch vụ tìm kiếm riêng. |
| Giới hạn | Không theo dõi người dùng là tuyên bố thiết kế, chưa kiểm toàn bộ cấu hình hay upstream. Khả năng truy cập engine phụ thuộc giới hạn, thay đổi giao diện và điều khoản nhà cung cấp. |
| Điều kiện tích hợp | Bắt đầu một nhóm engine cần thiết, kiểm outbound request, log và rate limit; giám sát chất lượng kết quả, không suy bảo đảm riêng tư từ mặc định. |
| Lựa chọn đối chiếu | Searx; Whoogle; Brave Search API. |

**Phạm vi bằng chứng:** đã clone, đọc trích đoạn tài liệu, giấy phép và các file cấu hình được dẫn dưới đây; chưa chạy mã, build, benchmark hoặc test upstream. `docs-read` không phải kiểm chứng implementation.

**Nguồn tại cùng SHA:** [README.rst](https://github.com/searxng/searxng/blob/a7163d091037cae586c444b05f22ecca162bb492/README.rst) · [LICENSE](https://github.com/searxng/searxng/blob/a7163d091037cae586c444b05f22ecca162bb492/LICENSE) · [package.json](https://github.com/searxng/searxng/blob/a7163d091037cae586c444b05f22ecca162bb492/package.json) · [go.mod](https://github.com/searxng/searxng/blob/a7163d091037cae586c444b05f22ecca162bb492/go.mod) · [.github/workflows/l10n.yml](https://github.com/searxng/searxng/blob/a7163d091037cae586c444b05f22ecca162bb492/.github/workflows/l10n.yml).

<a id="anhkysuai-archivebox-archivebox"></a>

### ArchiveBox

**Repo:** [ArchiveBox/ArchiveBox](https://github.com/ArchiveBox/ArchiveBox) · **License:** MIT · **Kiểm:** 2026-11-23, `docs-read`, [`5a5f6386e323`](https://github.com/ArchiveBox/ArchiveBox/tree/5a5f6386e323f940c6fa2e6a4c5b67feeeb0e8b6) (commit 2026-11-23). **Sao:** 29,082 tại 2026-11-23 theo [GitHub API](https://api.github.com/repos/ArchiveBox/ArchiveBox).

| Mục | Đánh giá |
|---|---|
| Mục đích | Ứng dụng lưu trữ nội dung web thành HTML, PDF, ảnh, văn bản và định dạng archive. |
| Giá trị và cơ chế theo tài liệu | README nêu CLI, REST API, webhook và đầu ra chuẩn; CI phân tách lint, test platform, CodeQL, Python artifact và Docker. |
| Giới hạn | Manifest là bản rc tại SHA đọc. Không bảo đảm mọi website hay nội dung đăng nhập lưu đầy đủ; tuyên bố đọc được hàng chục năm chưa thể xác minh trong review này. |
| Điều kiện tích hợp | Thử nhóm URL đại diện, giới hạn credential/crawler và kiểm nội dung lưu; sao lưu index lẫn artifact, xác nhận quyền truy cập trước khi xuất bản archive. |
| Lựa chọn đối chiếu | SingleFile; [Karakeep](../21-autonomous-workflows/README.md#anhkysuai-karakeep-app-karakeep); Wallabag. |

**Phạm vi bằng chứng:** đã clone, đọc trích đoạn tài liệu, giấy phép và các file cấu hình được dẫn dưới đây; chưa chạy mã, build, benchmark hoặc test upstream. `docs-read` không phải kiểm chứng implementation.

**Nguồn tại cùng SHA:** [README.md](https://github.com/ArchiveBox/ArchiveBox/blob/5a5f6386e323f940c6fa2e6a4c5b67feeeb0e8b6/README.md) · [LICENSE](https://github.com/ArchiveBox/ArchiveBox/blob/5a5f6386e323f940c6fa2e6a4c5b67feeeb0e8b6/LICENSE) · [pyproject.toml](https://github.com/ArchiveBox/ArchiveBox/blob/5a5f6386e323f940c6fa2e6a4c5b67feeeb0e8b6/pyproject.toml) · [.github/workflows/ci.yml](https://github.com/ArchiveBox/ArchiveBox/blob/5a5f6386e323f940c6fa2e6a4c5b67feeeb0e8b6/.github/workflows/ci.yml).

<a id="anhkysuai-m1k1o-neko"></a>

### Neko

**Repo:** [m1k1o/neko](https://github.com/m1k1o/neko) · **License:** Apache-2.0 · **Kiểm:** 2026-11-23, `docs-read`, [`8fd303c932e9`](https://github.com/m1k1o/neko/tree/8fd303c932e9189a25dfdce0acb31157940b02e7) (commit 2026-11-18). **Sao:** 22,709 tại 2026-11-23 theo [GitHub API](https://api.github.com/repos/m1k1o/neko).

| Mục | Đánh giá |
|---|---|
| Mục đích | Trình duyệt ảo tự host trong Docker, chia sẻ giao diện qua WebRTC. |
| Giá trị và cơ chế theo tài liệu | README mô tả nhiều người dùng cùng phiên browser, trình diễn và thử web; CI tách build client và image nền cho nhánh. |
| Giới hạn | Docker/WebRTC không tự bảo đảm riêng tư hay cô lập đủ cho mã không tin cậy. Chia sẻ browser đồng nghĩa chia sẻ phiên đăng nhập; chưa kiểm sandbox, media hay mạng NAT. |
| Điều kiện tích hợp | Dùng profile riêng không chứa tài khoản nhạy cảm, cấu hình auth/TLS và quyền host; thử mạng/TURN, clipboard/file transfer và xóa phiên sau sử dụng. |
| Lựa chọn đối chiếu | Kasm Workspaces; noVNC; Apache Guacamole. |

**Phạm vi bằng chứng:** đã clone, đọc trích đoạn tài liệu, giấy phép và các file cấu hình được dẫn dưới đây; chưa chạy mã, build, benchmark hoặc test upstream. `docs-read` không phải kiểm chứng implementation.

**Nguồn tại cùng SHA:** [README.md](https://github.com/m1k1o/neko/blob/8fd303c932e9189a25dfdce0acb31157940b02e7/README.md) · [LICENSE](https://github.com/m1k1o/neko/blob/8fd303c932e9189a25dfdce0acb31157940b02e7/LICENSE) · [.github/workflows/branch_test.yml](https://github.com/m1k1o/neko/blob/8fd303c932e9189a25dfdce0acb31157940b02e7/.github/workflows/branch_test.yml).

<a id="anhkysuai-wasmerio-wasmer"></a>

### Wasmer

**Repo:** [wasmerio/wasmer](https://github.com/wasmerio/wasmer) · **License:** MIT · **Kiểm:** 2026-11-23, `docs-read`, [`29e67da7ca5f`](https://github.com/wasmerio/wasmer/tree/29e67da7ca5fb5b3b41300d643437b623411c7c9) (commit 2026-11-19). **Sao:** 21,258 tại 2026-11-23 theo [GitHub API](https://api.github.com/repos/wasmerio/wasmer).

| Mục | Đánh giá |
|---|---|
| Mục đích | Runtime sandbox WebAssembly và CLI chạy ứng dụng từ package hoặc nhúng qua SDK. |
| Giá trị và cơ chế theo tài liệu | README mô tả cấp quyền filesystem bằng volume và mạng bằng net, tách Wasmer SDK ở repo riêng; Cargo/CI build nhiều nền tảng. |
| Giới hạn | Mô tả secure-by-default chưa là kiểm toán cách ly. Package registry, runtime và SDK là các phạm vi khác nhau; chưa kiểm syscall, resource limit hay escape. |
| Điều kiện tích hợp | Ghim runtime/package, mặc định cấp quyền hẹp và thử dữ liệu không nhạy cảm; đo CPU/RAM, filesystem/network và giới hạn thời gian trước cho agent thực thi mã. |
| Lựa chọn đối chiếu | Wasmtime; Firecracker; gVisor. |

**Phạm vi bằng chứng:** đã clone, đọc trích đoạn tài liệu, giấy phép và các file cấu hình được dẫn dưới đây; chưa chạy mã, build, benchmark hoặc test upstream. `docs-read` không phải kiểm chứng implementation.

**Nguồn tại cùng SHA:** [README.md](https://github.com/wasmerio/wasmer/blob/29e67da7ca5fb5b3b41300d643437b623411c7c9/README.md) · [LICENSE](https://github.com/wasmerio/wasmer/blob/29e67da7ca5fb5b3b41300d643437b623411c7c9/LICENSE) · [Cargo.toml](https://github.com/wasmerio/wasmer/blob/29e67da7ca5fb5b3b41300d643437b623411c7c9/Cargo.toml) · [.github/workflows/build.yml](https://github.com/wasmerio/wasmer/blob/29e67da7ca5fb5b3b41300d643437b623411c7c9/.github/workflows/build.yml).

<a id="anhkysuai-2026-11-23-identity-gvisor"></a>

### gVisor: đối chiếu tên repo

**Kết luận:** [google/gvisor](https://github.com/google/gvisor) và [gvisor/gvisor](https://github.com/gvisor/gvisor) là cùng thực thể GitHub, repository ID `131212638` theo API ngày 2026-11-23. Giữ ID catalog `gvisor` và hồ sơ gốc; cập nhật đường dẫn chuẩn, không thêm hồ sơ trùng.

**Phạm vi đọc lại:** `docs-read`; clone tại commit [`6abe42f82cb9fadf431d622741ac8bd9f3e75ab1`](https://github.com/gvisor/gvisor/commit/6abe42f82cb9fadf431d622741ac8bd9f3e75ab1) và đọc tài liệu được dẫn. GitHub get_repo cho google/gvisor trả canonical gvisor/gvisor, ID 131212638; metadata gvisor/gvisor cùng ID. Catalog đã có entity id gvisor trỏ tên cũ google/gvisor. Không tạo hồ sơ trùng; vẫn clone và đọc README/LICENSE/manifest/CI của SHA này. Những nhận định kỹ thuật cũ ở các phần trước giữ ngày/phạm vi cũ; lượt đối chiếu này chưa tái kiểm toàn bộ implementation hoặc chạy upstream.

**Metadata:** ★ 20,088 (GitHub API, 2026-11-23); commit ngày 2026-11-23. Trạng thái archived là `false`, không dùng riêng cờ này để kết luận mức bảo trì.

**Nguồn:** [gvisor](https://api.github.com/repos/google/gvisor) · [gvisor](https://api.github.com/repos/gvisor/gvisor) · [README.md](https://github.com/gvisor/gvisor/blob/6abe42f82cb9fadf431d622741ac8bd9f3e75ab1/README.md) · [LICENSE](https://github.com/gvisor/gvisor/blob/6abe42f82cb9fadf431d622741ac8bd9f3e75ab1/LICENSE) · [go.mod](https://github.com/gvisor/gvisor/blob/6abe42f82cb9fadf431d622741ac8bd9f3e75ab1/go.mod) · [build.yml](https://github.com/gvisor/gvisor/blob/6abe42f82cb9fadf431d622741ac8bd9f3e75ab1/.github/workflows/build.yml).

<a id="anhkysuai-2026-11-23-gorhill-ublock"></a>

### uBlock

**Đã chuyển (2026-11-23):** hồ sơ này nay nằm ở [mục 35](../35-desktop-productivity-apps/README.md#anhkysuai-2026-11-23-gorhill-ublock); catalog con xem [catalog/](../catalog/README.md).

<a id="anhkysuai-2026-11-23-pavlobu-deskreen"></a>

### deskreen

**Repo:** [pavlobu/deskreen](https://github.com/pavlobu/deskreen) · **License:** AGPL-3.0 · **★ 21,797 (GitHub API, 2026-11-23)**

**Mục đích:** Deskreen Community Edition truyền màn hình máy tính tới trình duyệt thiết bị khác qua WebRTC.

**Giá trị:** Cho phép dùng thiết bị có trình duyệt làm màn hình phụ, có ứng dụng cho Windows, macOS và Linux.

**Giới hạn:** README tách bản CE giới hạn tính năng với Pro; cần đo độ trễ, quyền chia sẻ màn hình và khả năng mạng thực tế. AGPL của CE không được suy áp dụng cho Pro.

**Cách tham khảo/tích hợp:** Thiết lập phạm vi thiết bị và xác thực phiên rõ ràng, kiểm đường truyền/relay và quyền điều khiển trong môi trường thử.

**Lựa chọn để đối chiếu:** [rustdesk/rustdesk](https://github.com/rustdesk/rustdesk) · [LizardByte/Sunshine](https://github.com/LizardByte/Sunshine). Đây là ứng viên so sánh theo tác vụ; mức phù hợp cần kiểm theo hồ sơ và phiên bản riêng.

**Bằng chứng:** `docs-read`, ngày 2026-11-23, commit [`b5dc3d4d1a74ec38091d36578fd84174db3792bc`](https://github.com/pavlobu/deskreen/commit/b5dc3d4d1a74ec38091d36578fd84174db3792bc), ngày commit 2026-07-08. Đã clone và đọc chọn lọc phần giới thiệu, cách dùng, giới hạn, license, metadata manifest và CI hiện diện. Chưa kiểm đầy đủ implementation hoặc chạy upstream; các số đo của tác giả chưa được tái lập.

**Nguồn:** [README.md](https://github.com/pavlobu/deskreen/blob/b5dc3d4d1a74ec38091d36578fd84174db3792bc/README.md) · [LICENSE](https://github.com/pavlobu/deskreen/blob/b5dc3d4d1a74ec38091d36578fd84174db3792bc/LICENSE) · [package.json](https://github.com/pavlobu/deskreen/blob/b5dc3d4d1a74ec38091d36578fd84174db3792bc/package.json) · [.github/workflows/release.yml](https://github.com/pavlobu/deskreen/blob/b5dc3d4d1a74ec38091d36578fd84174db3792bc/.github/workflows/release.yml) · [metadata GitHub](https://api.github.com/repos/pavlobu/deskreen).

<a id="anhkysuai-2026-11-23-genymobile-scrcpy"></a>

### scrcpy

**Repo:** [Genymobile/scrcpy](https://github.com/Genymobile/scrcpy) · **License:** Apache-2.0 · **★ 155,456 (GitHub API, 2026-11-23)**

**Mục đích:** Công cụ hiển thị và điều khiển Android từ máy tính qua USB hoặc TCP/IP.

**Giá trị:** Không cần root theo README, hỗ trợ bàn phím/chuột và âm thanh, phù hợp demo hoặc kiểm thử thủ công thiết bị.

**Giới hạn:** Cần quản lý quyền debug và kết nối mạng; các số FPS/độ trễ phụ thuộc thiết bị và chưa đo lại. README nhấn mạnh chỉ tải release từ nguồn chính thức.

**Cách tham khảo/tích hợp:** Thiết lập phạm vi thiết bị và xác thực phiên rõ ràng, kiểm đường truyền/relay và quyền điều khiển trong môi trường thử.

**Lựa chọn để đối chiếu:** [rustdesk/rustdesk](https://github.com/rustdesk/rustdesk) · [pavlobu/deskreen](https://github.com/pavlobu/deskreen). Đây là ứng viên so sánh theo tác vụ; mức phù hợp cần kiểm theo hồ sơ và phiên bản riêng.

**Bằng chứng:** `docs-read`, ngày 2026-11-23, commit [`c939183a7cdca4599cee337e60bc0e147b6c9828`](https://github.com/Genymobile/scrcpy/commit/c939183a7cdca4599cee337e60bc0e147b6c9828), ngày commit 2026-11-19. Đã clone và đọc chọn lọc phần giới thiệu, cách dùng, giới hạn, license, metadata manifest và CI hiện diện. Chưa kiểm đầy đủ implementation hoặc chạy upstream; các số đo của tác giả chưa được tái lập.

**Nguồn:** [README.md](https://github.com/Genymobile/scrcpy/blob/c939183a7cdca4599cee337e60bc0e147b6c9828/README.md) · [LICENSE](https://github.com/Genymobile/scrcpy/blob/c939183a7cdca4599cee337e60bc0e147b6c9828/LICENSE) · [build.gradle](https://github.com/Genymobile/scrcpy/blob/c939183a7cdca4599cee337e60bc0e147b6c9828/build.gradle) · [.github/workflows/release.yml](https://github.com/Genymobile/scrcpy/blob/c939183a7cdca4599cee337e60bc0e147b6c9828/.github/workflows/release.yml) · [metadata GitHub](https://api.github.com/repos/Genymobile/scrcpy).

<a id="anhkysuai-2026-11-23-rustdesk-rustdesk"></a>

### rustdesk

**Repo:** [rustdesk/rustdesk](https://github.com/rustdesk/rustdesk) · **License:** AGPL-3.0 · **★ 130,912 (GitHub API, 2026-11-23)**

**Mục đích:** Ứng dụng remote desktop bằng Rust, hỗ trợ dùng relay/rendezvous công cộng hoặc tự host.

**Giá trị:** Có lựa chọn kiểm soát hạ tầng kết nối và nhiều nền tảng, phù hợp nghiên cứu remote access.

**Giới hạn:** Tuyên bố kiểm soát dữ liệu trong README chưa thay kiểm bảo mật; cần cấu hình server, xác thực và quyền phiên. AGPL của client tách khỏi Server Pro và điều khoản dịch vụ.

**Cách tham khảo/tích hợp:** Thiết lập phạm vi thiết bị và xác thực phiên rõ ràng, kiểm đường truyền/relay và quyền điều khiển trong môi trường thử.

**Lựa chọn để đối chiếu:** [Genymobile/scrcpy](https://github.com/Genymobile/scrcpy) · [guacamole/guacamole-client](https://github.com/guacamole/guacamole-client). Đây là ứng viên so sánh theo tác vụ; mức phù hợp cần kiểm theo hồ sơ và phiên bản riêng.

**Bằng chứng:** `docs-read`, ngày 2026-11-23, commit [`51f94394ce61e1f3d26229565c326b2862cbdd1f`](https://github.com/rustdesk/rustdesk/commit/51f94394ce61e1f3d26229565c326b2862cbdd1f), ngày commit 2026-11-23. Đã clone và đọc chọn lọc phần giới thiệu, cách dùng, giới hạn, license, metadata manifest và CI hiện diện. Chưa kiểm đầy đủ implementation hoặc chạy upstream; các số đo của tác giả chưa được tái lập.

**Nguồn:** [README.md](https://github.com/rustdesk/rustdesk/blob/51f94394ce61e1f3d26229565c326b2862cbdd1f/README.md) · [LICENCE](https://github.com/rustdesk/rustdesk/blob/51f94394ce61e1f3d26229565c326b2862cbdd1f/LICENCE) · [Cargo.toml](https://github.com/rustdesk/rustdesk/blob/51f94394ce61e1f3d26229565c326b2862cbdd1f/Cargo.toml) · [.github/workflows/ci.yml](https://github.com/rustdesk/rustdesk/blob/51f94394ce61e1f3d26229565c326b2862cbdd1f/.github/workflows/ci.yml) · [metadata GitHub](https://api.github.com/repos/rustdesk/rustdesk).

## 4. Nguồn

- https://gist.github.com/kevinmichaelchen/9d77b8a681238cc45297dff969686175 · https://www.firecrawl.dev/blog/best-browser-agents · https://scrapfly.io/blog/posts/stagehand-vs-browser-use · https://agentscamp.com/guides/comparisons/browser-agents-compared-2026 · https://bug0.com/blog/expect-vs-agent-browser-vs-stagehand-vs-passmark · https://github.com/browserbase/stagehand · https://kanopylabs.com/blog/stagehand-vs-browserbase-vs-steel-browser-ai
- https://www.superagent.sh/blog/ai-code-sandbox-benchmark-2026 · https://blog.logrocket.com/comparing-ai-agent-sandbox-platforms-e2b-modal-daytona-and-more/ · https://devtoollab.com/blog/best-ai-code-execution-sandboxes · https://bex.co/blog/2026/09/25/four-companies-one-sandbox-market-agent-code-execution · https://www.developersdigest.tech/blog/ai-agent-code-sandbox-comparison-2026 · https://www.beri.net/article/e2b-vs-modal-vs-daytona-agent-sandbox-pricing-isolation-2026 · https://particula.tech/blog/modal-vs-e2b-vs-daytona-vs-vercel-sandbox-ai-code-execution · https://arxiv.org/pdf/2606.08433
- §3b (12/10/2026): https://github.com/bytedance/UI-TARS-desktop · https://github.com/trycua/cua · https://github.com/simular-ai/Agent-S · https://github.com/firecrawl/firecrawl · https://github.com/unclecode/crawl4ai · https://github.com/ChromeDevTools/chrome-devtools-mcp · https://github.com/google/gvisor · https://github.com/firecracker-microvm/firecracker · https://github.com/anthropics/sandbox-runtime · https://github.com/superradcompany/microsandbox · https://github.com/microsoft/OmniParser · https://github.com/browserless/browserless · https://github.com/jina-ai/reader · https://github.com/steel-dev/steel-browser
- §1b e2e (13/10/2026): https://github.com/tester-army/e2e (clone nông, HEAD fc90644: README.md, AGENTS.md, SECURITY.md, NOTICE, docs/{cache,security,telemetry,subscriptions,models}.mdx, packages/e2e/package.json 0.20.0, .github/workflows) · https://e2e.tester.army/docs · https://ycombinator.com/companies/testerarmy · https://hn.svelte.dev/item/48586299 (Launch HN) · https://docs.expo.dev/guides/using-e2e/ · https://testdino.com/blog/playwright-vs-e2e (blog) · https://ai-tldr.dev/releases/tester-army-e2e-0-18/ (blog) · https://www.testmuai.com/blog/e2e-by-testerarmy/ (blog) · so sánh: https://github.com/web-infra-dev/midscene, https://midscenejs.com/midscene-test/overview, https://github.com/mobile-dev-inc/Maestro, https://github.com/wix/Detox
- §1c browser-use (13/10/2026): https://github.com/browser-use/browser-use (clone nông, HEAD c75e847: pyproject.toml 0.13.11, browser_use/config.py, browser_use/telemetry/{service,views}.py, browser_use/agent/{service,views}.py, browser_use/llm/browser_use/chat.py, browser_use/mcp/server.py, browser_use/skills/install.py, browser_use/sandbox/sandbox.py, AGENTS.md, CLOUD.md, skills/x402/SKILL.md, server.json) · https://github.com/browser-use/browser-harness (telemetry.py) · shields.io stars/forks/license 13/10/2026

<a id="chuan-hoa-2026-11-23"></a>

## Chuẩn hóa bằng chứng hồ sơ cũ — 23/11/2026

Các hồ sơ dưới đây có từ trước khi kho ghi mức kiểm. Ngày 2026-11-23 mỗi repo được clone nông tại commit ghi trong bảng, đọc LICENSE, README, manifest và CI (nếu có); không cài, build hay chạy mã upstream. Nhận định cũ ở phần trên giữ nguyên; chỗ nào khác với lần đọc này được ghi trong cột Nhận định. Số sao lấy qua GitHub search API cùng ngày.

<a id="ch-agent-browser"></a>

### agent-browser

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/vercel-labs/agent-browser |
| License | Apache-2.0 |
| Phiên bản đã đọc | `d2dfc782ccdd79d25a9b4f0acced9321789cecb8` (commit 2026-11-21) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE, package.json (chỉ đối chiếu số phiên bản/cấu hình); chưa chạy upstream |
| Bảo trì | active (commit cuối 2026-11-21) |
| Nhận định | CLI trình duyệt cho agent (Rust CLI, package 0.43.0, ghi chú cũ 0.41.0); license Apache-2.0 khớp. |
| Nguồn | [README.md](https://github.com/vercel-labs/agent-browser/blob/d2dfc782ccdd79d25a9b4f0acced9321789cecb8/README.md) · [LICENSE](https://github.com/vercel-labs/agent-browser/blob/d2dfc782ccdd79d25a9b4f0acced9321789cecb8/LICENSE) · [package.json](https://github.com/vercel-labs/agent-browser/blob/d2dfc782ccdd79d25a9b4f0acced9321789cecb8/package.json) |

<a id="ch-agent-s"></a>

### Agent S

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/simular-ai/Agent-S |
| License | Apache-2.0 |
| Phiên bản đã đọc | `bcdf1d6c8f1cbe3f1c4004e83fad6020651db925` (commit 2026-11-23) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE, setup.py (chỉ đối chiếu số phiên bản/cấu hình); chưa chạy upstream |
| Bảo trì | active (commit cuối 2026-11-23) |
| Nhận định | Framework agent dùng máy tính (Agent S); license Apache-2.0 khớp; số OSWorld là tự báo cáo (chưa xác minh). |
| Nguồn | [README.md](https://github.com/simular-ai/Agent-S/blob/bcdf1d6c8f1cbe3f1c4004e83fad6020651db925/README.md) · [LICENSE](https://github.com/simular-ai/Agent-S/blob/bcdf1d6c8f1cbe3f1c4004e83fad6020651db925/LICENSE) · [setup.py](https://github.com/simular-ai/Agent-S/blob/bcdf1d6c8f1cbe3f1c4004e83fad6020651db925/setup.py) |

<a id="ch-agent-sandbox-kubernetes-sig-apps"></a>

### Agent Sandbox (Kubernetes SIG Apps)

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/kubernetes-sigs/agent-sandbox |
| License | Apache-2.0 |
| Phiên bản đã đọc | `1b7d5336539b9acd44ec431a61f4e83700a0a392` (commit 2026-11-21) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE, go.mod (chỉ đối chiếu số phiên bản/cấu hình); chưa chạy upstream |
| Bảo trì | active (commit cuối 2026-11-21) |
| Nhận định | Dự án kubernetes-sigs cho CRD Sandbox; license Apache-2.0 khớp; README ví dụ cài v1.0.2, chưa đối chiếu được tag v1.0.9 nêu trong ghi chú cũ. |
| Nguồn | [README.md](https://github.com/kubernetes-sigs/agent-sandbox/blob/1b7d5336539b9acd44ec431a61f4e83700a0a392/README.md) · [LICENSE](https://github.com/kubernetes-sigs/agent-sandbox/blob/1b7d5336539b9acd44ec431a61f4e83700a0a392/LICENSE) · [go.mod](https://github.com/kubernetes-sigs/agent-sandbox/blob/1b7d5336539b9acd44ec431a61f4e83700a0a392/go.mod) |

<a id="ch-agentdojo"></a>

### AgentDojo

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/ethz-spylab/agentdojo |
| License | MIT |
| Phiên bản đã đọc | `089ed468cf3ed0322acc66b0211f26d9d90dbf60` (commit 2026-06-02) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE, pyproject.toml (chỉ đối chiếu số phiên bản/cấu hình); chưa chạy upstream |
| Bảo trì | low-activity (commit cuối 2026-06-02) |
| Nhận định | Benchmark prompt injection cho agent (package 0.1.35); license MIT khớp; commit cuối 2026-06-02. |
| Nguồn | [README.md](https://github.com/ethz-spylab/agentdojo/blob/089ed468cf3ed0322acc66b0211f26d9d90dbf60/README.md) · [LICENSE](https://github.com/ethz-spylab/agentdojo/blob/089ed468cf3ed0322acc66b0211f26d9d90dbf60/LICENSE) · [pyproject.toml](https://github.com/ethz-spylab/agentdojo/blob/089ed468cf3ed0322acc66b0211f26d9d90dbf60/pyproject.toml) |

<a id="ch-browsentic"></a>

### Browsentic

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/imshaikot/browsentic |
| License | Apache-2.0 |
| Phiên bản đã đọc | `9c0892a457e86cf2a5c3d1f4a8eea7eeb0900632` (commit 2026-11-06) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE, package.json (chỉ đối chiếu số phiên bản/cấu hình); chưa chạy upstream |
| Bảo trì | active (commit cuối 2026-11-06) |
| Nhận định | Extension trình duyệt + bridge cục bộ cho CLI agent; license Apache-2.0 khớp; kho còn nhỏ. |
| Nguồn | [README.md](https://github.com/imshaikot/browsentic/blob/9c0892a457e86cf2a5c3d1f4a8eea7eeb0900632/README.md) · [LICENSE](https://github.com/imshaikot/browsentic/blob/9c0892a457e86cf2a5c3d1f4a8eea7eeb0900632/LICENSE) · [package.json](https://github.com/imshaikot/browsentic/blob/9c0892a457e86cf2a5c3d1f4a8eea7eeb0900632/package.json) |

<a id="ch-browser-use"></a>

### Browser Use

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/browser-use/browser-use |
| License | MIT |
| Phiên bản đã đọc | `753d629d76eb2b670f4cf467f3355bbe750f6845` (commit 2026-11-21) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE, pyproject.toml (chỉ đối chiếu số phiên bản/cấu hình); chưa chạy upstream |
| Bảo trì | active (commit cuối 2026-11-21) |
| Nhận định | Thư viện agent trình duyệt Python; pyproject hiện version 1.0.8 và README liệt kê Browser Use Pi như runtime TypeScript riêng, lệch ghi chú cũ (0.13.14 là bản Python cuối); license MIT khớp. |
| Nguồn | [README.md](https://github.com/browser-use/browser-use/blob/753d629d76eb2b670f4cf467f3355bbe750f6845/README.md) · [LICENSE](https://github.com/browser-use/browser-use/blob/753d629d76eb2b670f4cf467f3355bbe750f6845/LICENSE) · [pyproject.toml](https://github.com/browser-use/browser-use/blob/753d629d76eb2b670f4cf467f3355bbe750f6845/pyproject.toml) |

<a id="ch-browser-use-pi"></a>

### browser-use-pi

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/browser-use/browser-use-pi |
| License | MIT |
| Phiên bản đã đọc | `3583b8a10a2cf393956ad75c32fec302b227aa32` (commit 2026-11-20) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE, package.json (chỉ đối chiếu số phiên bản/cấu hình); chưa chạy upstream |
| Bảo trì | active (commit cuối 2026-11-20) |
| Nhận định | Runtime TypeScript trên Pi, package 0.2.0; license MIT khớp; không có thư mục .github/workflows. |
| Nguồn | [README.md](https://github.com/browser-use/browser-use-pi/blob/3583b8a10a2cf393956ad75c32fec302b227aa32/README.md) · [LICENSE](https://github.com/browser-use/browser-use-pi/blob/3583b8a10a2cf393956ad75c32fec302b227aa32/LICENSE) · [package.json](https://github.com/browser-use/browser-use-pi/blob/3583b8a10a2cf393956ad75c32fec302b227aa32/package.json) |

<a id="ch-browserbase-mcp-self-host-archived"></a>

### Browserbase MCP (self-host, archived)

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/browserbase/mcp-server-browserbase |
| License | Apache-2.0. Khớp catalog. |
| Phiên bản đã đọc | `3e6f53461949037d5e65dd425da3ceb1263f11d6` (commit 2026-07-20) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE, package.json; chưa chạy upstream |
| Bảo trì | archived |
| Nhận định | MCP tự host 6 tool (start/end/navigate/act/observe/extract) trên Browserbase + Stagehand; README nói tool khớp bản hosted. Đã ngừng bảo trì nên chỉ để tham khảo, không dựa vào cho sản phẩm mới. |
| Nguồn | [README.md](https://github.com/browserbase/mcp-server-browserbase/blob/3e6f53461949037d5e65dd425da3ceb1263f11d6/README.md) · [LICENSE](https://github.com/browserbase/mcp-server-browserbase/blob/3e6f53461949037d5e65dd425da3ceb1263f11d6/LICENSE) · [package.json](https://github.com/browserbase/mcp-server-browserbase/blob/3e6f53461949037d5e65dd425da3ceb1263f11d6/package.json) |

<a id="ch-browsergym"></a>

### BrowserGym

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/ServiceNow/BrowserGym |
| License | Apache-2.0 (LICENSE chỉ có dòng bản quyền ServiceNow + đoạn áp dụng Apache, không có văn bản đầy đủ nên GitHub báo NOASSERTION). Khớp catalog (đã ghi chú NOASSERTION). |
| Phiên bản đã đọc | `62a678feefaff0f93e9bab03f51c5402a1e1db00` (commit 2026-11-18) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE, pyproject.toml; chưa chạy upstream |
| Bảo trì | active |
| Nhận định | Môi trường kiểu Gym cho agent web, gộp nhiều benchmark qua các gói con. README tự cảnh báo chỉ cho nghiên cứu, "not a consumer product". |
| Nguồn | [README.md](https://github.com/ServiceNow/BrowserGym/blob/62a678feefaff0f93e9bab03f51c5402a1e1db00/README.md) · [LICENSE](https://github.com/ServiceNow/BrowserGym/blob/62a678feefaff0f93e9bab03f51c5402a1e1db00/LICENSE) · [pyproject.toml](https://github.com/ServiceNow/BrowserGym/blob/62a678feefaff0f93e9bab03f51c5402a1e1db00/pyproject.toml) |

<a id="ch-crawl4ai"></a>

### Crawl4AI

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/unclecode/crawl4ai |
| License | Apache-2.0. Khớp catalog. |
| Phiên bản đã đọc | `4e4bab5d44a7557eb403f137ec589833368a3e38` (commit 2026-11-23) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE, pyproject.toml; chưa chạy upstream |
| Bảo trì | active |
| Nhận định | Crawler xuất Markdown/JSON cho LLM, cài bằng Python hoặc Docker. Lưu ý README đẩy mạnh bản cloud; phụ thuộc playwright/patchright. |
| Nguồn | [README.md](https://github.com/unclecode/crawl4ai/blob/4e4bab5d44a7557eb403f137ec589833368a3e38/README.md) · [LICENSE](https://github.com/unclecode/crawl4ai/blob/4e4bab5d44a7557eb403f137ec589833368a3e38/LICENSE) · [pyproject.toml](https://github.com/unclecode/crawl4ai/blob/4e4bab5d44a7557eb403f137ec589833368a3e38/pyproject.toml) |

<a id="ch-cua"></a>

### Cua

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/trycua/cua |
| License | MIT (gốc); FSL-1.1-MIT cho Cua Spaces và libs/cua-driver-bench; AGPL-3.0-or-later cho libs/python/som. Khớp catalog "MIT một phần FSL/AGPL"; đính chính chi tiết: README mục Licensing nói cua-driver-bench trước 11/10/2026 là MIT, nay FSL-1.1-MIT; AGPL ở som và artifact model OmniParser (đọc README + legal/LICENSING.md). |
| Phiên bản đã đọc | `316b098571adf4872f0fa1a96f8237e737f72754` (commit 2026-11-23) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE.md, package.json, pyproject.toml, legal/LICENSING.md; chưa chạy upstream |
| Bảo trì | active |
| Nhận định | Monorepo hạ tầng computer-use (SDK, Cua Driver, Lume, bench). Phần lớn MIT nhưng có thư mục FSL (không dùng để cạnh tranh dịch vụ hosted) và AGPL, cần xem LICENSING.md theo từng thư mục trước khi dùng. |
| Nguồn | [README.md](https://github.com/trycua/cua/blob/316b098571adf4872f0fa1a96f8237e737f72754/README.md) · [LICENSE.md](https://github.com/trycua/cua/blob/316b098571adf4872f0fa1a96f8237e737f72754/LICENSE.md) · [package.json](https://github.com/trycua/cua/blob/316b098571adf4872f0fa1a96f8237e737f72754/package.json) · [pyproject.toml](https://github.com/trycua/cua/blob/316b098571adf4872f0fa1a96f8237e737f72754/pyproject.toml) · [LICENSING.md](https://github.com/trycua/cua/blob/316b098571adf4872f0fa1a96f8237e737f72754/legal/LICENSING.md) |

<a id="ch-cubesandbox"></a>

### CubeSandbox

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/TencentCloud/CubeSandbox |
| License | Apache-2.0 trừ các thành phần bên thứ ba liệt kê trong LICENSE. Khớp catalog. |
| Phiên bản đã đọc | `a260523d30186d1a17010345984e71af49c19edc` (commit 2026-11-23) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE; chưa chạy upstream |
| Bảo trì | active |
| Nhận định | MicroVM KVM của Tencent Cloud cho sandbox agent (repo nhiều thành phần Cube*, SDK, hypervisor). Cần đọc phần bên thứ ba trong LICENSE; tuyên bố tương thích E2B là của tác giả (chưa xác minh). |
| Nguồn | [README.md](https://github.com/TencentCloud/CubeSandbox/blob/a260523d30186d1a17010345984e71af49c19edc/README.md) · [LICENSE](https://github.com/TencentCloud/CubeSandbox/blob/a260523d30186d1a17010345984e71af49c19edc/LICENSE) |

<a id="ch-daytona"></a>

### Daytona

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/daytonaio/daytona |
| License | Không có file LICENSE ở HEAD. Không có file LICENSE ở HEAD (README trỏ tới LICENSE ở tag v0.190.0); khớp catalog (null). |
| Phiên bản đã đọc | `ec4c21b2d597091ac09ecc278f3bcc172575a987` (commit 2026-06-25) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md; chưa chạy upstream |
| Bảo trì | deprecated-by-readme |
| Nhận định | Không còn mã nguồn để tham khảo ở nhánh mặc định; chỉ README mô tả nền tảng sandbox (SDK/API/CLI). Không nên coi là dự án mã mở đang phát triển; tài nguyên mới ở github.com/daytona. |
| Nguồn | [README.md](https://github.com/daytonaio/daytona/blob/ec4c21b2d597091ac09ecc278f3bcc172575a987/README.md) |

<a id="ch-e2b"></a>

### E2B

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/e2b-dev/E2B |
| License | Apache-2.0. Khớp catalog. |
| Phiên bản đã đọc | `08c4eeba6d08413779ec3fa5e7ac0edf3f608b33` (commit 2026-11-18) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE, package.json; chưa chạy upstream |
| Bảo trì | active |
| Nhận định | SDK và CLI cho sandbox E2B; mô tả Firecracker microVM trong catalog là tuyên bố nền tảng (chưa xác minh trong repo này). |
| Nguồn | [README.md](https://github.com/e2b-dev/E2B/blob/08c4eeba6d08413779ec3fa5e7ac0edf3f608b33/README.md) · [LICENSE](https://github.com/e2b-dev/E2B/blob/08c4eeba6d08413779ec3fa5e7ac0edf3f608b33/LICENSE) · [package.json](https://github.com/e2b-dev/E2B/blob/08c4eeba6d08413779ec3fa5e7ac0edf3f608b33/package.json) |

<a id="ch-e2e-testerarmy"></a>

### e2e (TesterArmy)

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/tester-army/e2e |
| License | Apache-2.0. Khớp catalog; có thêm file NOTICE. |
| Phiên bản đã đọc | `74904fcbfdefc27be8db0fffa73a3af8a92fb6d0` (commit 2026-11-23) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE, NOTICE, package.json; chưa chạy upstream |
| Bảo trì | active |
| Nhận định | Framework E2E agentic dạng monorepo (@e2e-dev/*: web, mobile, desktop, acp...). Cần lưu ý khả năng đổi owner sang e2e-inc. |
| Nguồn | [README.md](https://github.com/tester-army/e2e/blob/74904fcbfdefc27be8db0fffa73a3af8a92fb6d0/README.md) · [LICENSE](https://github.com/tester-army/e2e/blob/74904fcbfdefc27be8db0fffa73a3af8a92fb6d0/LICENSE) · [NOTICE](https://github.com/tester-army/e2e/blob/74904fcbfdefc27be8db0fffa73a3af8a92fb6d0/NOTICE) · [package.json](https://github.com/tester-army/e2e/blob/74904fcbfdefc27be8db0fffa73a3af8a92fb6d0/package.json) |

<a id="ch-fara"></a>

### Fara

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/microsoft/fara |
| License | MIT. Khớp catalog. |
| Phiên bản đã đọc | `a675d6d61c41c47ae87bacefeab22caad18e3e84` (commit 2026-07-22) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE, pyproject.toml; chưa chạy upstream |
| Bảo trì | low-activity |
| Nhận định | Mô hình computer-use Fara1.5 (4B/9B/27B) kèm harness Playwright và WebTailBench. Trọng số ở Hugging Face, license riêng của model cần xem ở model card. |
| Nguồn | [README.md](https://github.com/microsoft/fara/blob/a675d6d61c41c47ae87bacefeab22caad18e3e84/README.md) · [LICENSE](https://github.com/microsoft/fara/blob/a675d6d61c41c47ae87bacefeab22caad18e3e84/LICENSE) · [pyproject.toml](https://github.com/microsoft/fara/blob/a675d6d61c41c47ae87bacefeab22caad18e3e84/pyproject.toml) |

<a id="ch-firecracker"></a>

### Firecracker

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/firecracker-microvm/firecracker |
| License | Apache-2.0. Khớp catalog. |
| Phiên bản đã đọc | `58cf1b2cdca407f2323d1b0b25ebb95dfe5b4bcb` (commit 2026-11-20) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE, NOTICE, Cargo.toml; chưa chạy upstream |
| Bảo trì | active |
| Nhận định | VMM microVM nền tảng cho nhiều sandbox (AWS Lambda, E2B...). Repo trưởng thành, CI qua workflow cho PR/style/build. |
| Nguồn | [README.md](https://github.com/firecracker-microvm/firecracker/blob/58cf1b2cdca407f2323d1b0b25ebb95dfe5b4bcb/README.md) · [LICENSE](https://github.com/firecracker-microvm/firecracker/blob/58cf1b2cdca407f2323d1b0b25ebb95dfe5b4bcb/LICENSE) · [NOTICE](https://github.com/firecracker-microvm/firecracker/blob/58cf1b2cdca407f2323d1b0b25ebb95dfe5b4bcb/NOTICE) · [Cargo.toml](https://github.com/firecracker-microvm/firecracker/blob/58cf1b2cdca407f2323d1b0b25ebb95dfe5b4bcb/Cargo.toml) |

<a id="ch-firecrawl"></a>

### Firecrawl

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/firecrawl/firecrawl |
| License | AGPL-3.0 (chính); SDK và một số thành phần UI MIT theo LICENSE từng thư mục. Khớp catalog (AGPL, SDK MIT): README mục License và LICENSE riêng trong apps/*-sdk. |
| Phiên bản đã đọc | `6f2c50739e8426c49e83832408927bf0f862e69b` (commit 2026-11-23) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE; chưa chạy upstream |
| Bảo trì | active |
| Nhận định | Scrape/crawl/search cho LLM, có self-host và Firecrawl Local. AGPL gốc ràng buộc khi tự host dịch vụ; README nói scrape cục bộ có thể fallback qua Firecrawl Cloud theo mặc định. |
| Nguồn | [README.md](https://github.com/firecrawl/firecrawl/blob/6f2c50739e8426c49e83832408927bf0f862e69b/README.md) · [LICENSE](https://github.com/firecrawl/firecrawl/blob/6f2c50739e8426c49e83832408927bf0f862e69b/LICENSE) |

<a id="ch-kata-containers"></a>

### Kata Containers

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/kata-containers/kata-containers |
| License | Apache-2.0. Khớp catalog. |
| Phiên bản đã đọc | `e7e4c61dd6367046a45dcfb75d523a96ab5774d5` (commit 2026-11-23) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE, Cargo.toml; chưa chạy upstream |
| Bảo trì | active |
| Nhận định | Container chạy trong VM nhẹ cho cách ly workload; trưởng thành, CI đa nền tảng. Chi tiết Scorecard/zizmor/osv trong catalog chưa kiểm ở mức workflow. |
| Nguồn | [README.md](https://github.com/kata-containers/kata-containers/blob/e7e4c61dd6367046a45dcfb75d523a96ab5774d5/README.md) · [LICENSE](https://github.com/kata-containers/kata-containers/blob/e7e4c61dd6367046a45dcfb75d523a96ab5774d5/LICENSE) · [Cargo.toml](https://github.com/kata-containers/kata-containers/blob/e7e4c61dd6367046a45dcfb75d523a96ab5774d5/Cargo.toml) |

<a id="ch-maestro"></a>

### Maestro

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/mobile-dev-inc/Maestro |
| License | Apache-2.0. Khớp catalog. |
| Phiên bản đã đọc | `d9561331af38c6417ff39ce655251aea898ae3f6` (commit 2026-11-20) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE; chưa chạy upstream |
| Bảo trì | active |
| Nhận định | Framework E2E mobile/web bằng flow YAML, nay có MCP cho coding agent. iOS thật chưa hỗ trợ theo README. |
| Nguồn | [README.md](https://github.com/mobile-dev-inc/Maestro/blob/d9561331af38c6417ff39ce655251aea898ae3f6/README.md) · [LICENSE](https://github.com/mobile-dev-inc/Maestro/blob/d9561331af38c6417ff39ce655251aea898ae3f6/LICENSE) |

<a id="ch-microsandbox"></a>

### microsandbox

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/superradcompany/microsandbox |
| License | Apache-2.0. Khớp catalog. |
| Phiên bản đã đọc | `5ca1046a23fd8fba5037a0ef80b386ea4799784b` (commit 2026-11-23) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE, Cargo.toml; chưa chạy upstream |
| Bảo trì | active |
| Nhận định | MicroVM chạy cục bộ trên libkrun, workspace Rust nhiều crate. Còn beta nên API có thể đổi. |
| Nguồn | [README.md](https://github.com/superradcompany/microsandbox/blob/5ca1046a23fd8fba5037a0ef80b386ea4799784b/README.md) · [LICENSE](https://github.com/superradcompany/microsandbox/blob/5ca1046a23fd8fba5037a0ef80b386ea4799784b/LICENSE) · [Cargo.toml](https://github.com/superradcompany/microsandbox/blob/5ca1046a23fd8fba5037a0ef80b386ea4799784b/Cargo.toml) |

<a id="ch-midscene-js"></a>

### Midscene.js

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/web-infra-dev/midscene |
| License | MIT. Khớp catalog. |
| Phiên bản đã đọc | `8a0f9949e6ad615b9bb3678e1b2147fe2b418d78` (commit 2026-11-23) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE, package.json; chưa chạy upstream |
| Bảo trì | active |
| Nhận định | Thao tác/assert bằng AI dựa trên ảnh chụp cho web, Android, iOS và desktop. Phụ thuộc mô hình thị giác bên ngoài. |
| Nguồn | [README.md](https://github.com/web-infra-dev/midscene/blob/8a0f9949e6ad615b9bb3678e1b2147fe2b418d78/README.md) · [LICENSE](https://github.com/web-infra-dev/midscene/blob/8a0f9949e6ad615b9bb3678e1b2147fe2b418d78/LICENSE) · [package.json](https://github.com/web-infra-dev/midscene/blob/8a0f9949e6ad615b9bb3678e1b2147fe2b418d78/package.json) |

<a id="ch-modal"></a>

### Modal

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/modal-labs/modal-client |
| License | Apache-2.0 (SDK). Khớp catalog (chỉ SDK). |
| Phiên bản đã đọc | `ded1c859db9b8861793da618de47f152321fb28c` (commit 2026-11-21) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE; chưa chạy upstream |
| Bảo trì | active |
| Nhận định | Chỉ là SDK client mã mở; nền tảng chạy phía Modal là dịch vụ đóng. Có skill chính thức cho coding agent (`modal skills install`). |
| Nguồn | [README.md](https://github.com/modal-labs/modal-client/blob/ded1c859db9b8861793da618de47f152321fb28c/README.md) · [LICENSE](https://github.com/modal-labs/modal-client/blob/ded1c859db9b8861793da618de47f152321fb28c/LICENSE) |

<a id="ch-monty"></a>

### Monty

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/pydantic/monty |
| License | MIT. Khớp catalog. |
| Phiên bản đã đọc | `89379319399e3b6d328c394f41e2f3577601d46e` (commit 2026-11-23) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE, pyproject.toml, Cargo.toml; chưa chạy upstream |
| Bảo trì | active |
| Nhận định | Trình thông dịch Python tập con viết bằng Rust cho code do LLM sinh; có binding Python/JS. Dự án rất mới, nhiều crate. |
| Nguồn | [README.md](https://github.com/pydantic/monty/blob/89379319399e3b6d328c394f41e2f3577601d46e/README.md) · [LICENSE](https://github.com/pydantic/monty/blob/89379319399e3b6d328c394f41e2f3577601d46e/LICENSE) · [pyproject.toml](https://github.com/pydantic/monty/blob/89379319399e3b6d328c394f41e2f3577601d46e/pyproject.toml) · [Cargo.toml](https://github.com/pydantic/monty/blob/89379319399e3b6d328c394f41e2f3577601d46e/Cargo.toml) |

<a id="ch-nsjail"></a>

### nsjail

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/google/nsjail |
| License | Apache-2.0. Khớp catalog. |
| Phiên bản đã đọc | `ec259a3edb34c3b138fbad859c09e0e70259ff8b` (commit 2026-11-20) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE; chưa chạy upstream |
| Bảo trì | active |
| Nhận định | Công cụ jail tiến trình Linux gọn, cấu hình bằng protobuf hoặc CLI. Cần quyền (namespace/cgroup) khi chạy. |
| Nguồn | [README.md](https://github.com/google/nsjail/blob/ec259a3edb34c3b138fbad859c09e0e70259ff8b/README.md) · [LICENSE](https://github.com/google/nsjail/blob/ec259a3edb34c3b138fbad859c09e0e70259ff8b/LICENSE) |

<a id="ch-obscura"></a>

### Obscura

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/h4ckf0r0day/obscura |
| License | Apache-2.0. Khớp catalog. |
| Phiên bản đã đọc | `fef52749c09d875ca5eb72143458d9b68a8fb728` (commit 2026-11-22) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE, Cargo.toml; chưa chạy upstream |
| Bảo trì | active |
| Nhận định | Engine trình duyệt headless Rust có CDP và MCP, tự nhận thay Chromium. Dự án còn mới (version 0.1.0). |
| Nguồn | [README.md](https://github.com/h4ckf0r0day/obscura/blob/fef52749c09d875ca5eb72143458d9b68a8fb728/README.md) · [LICENSE](https://github.com/h4ckf0r0day/obscura/blob/fef52749c09d875ca5eb72143458d9b68a8fb728/LICENSE) · [Cargo.toml](https://github.com/h4ckf0r0day/obscura/blob/fef52749c09d875ca5eb72143458d9b68a8fb728/Cargo.toml) |

<a id="ch-opensandbox"></a>

### OpenSandbox

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/opensandbox-group/OpenSandbox |
| License | Apache-2.0. Khớp catalog. |
| Phiên bản đã đọc | `5039696283031c67a7945f1091deef7c8efe61b6` (commit 2026-11-23) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE; chưa chạy upstream |
| Bảo trì | active |
| Nhận định | Nền tảng sandbox tự host từ Docker tới Kubernetes, SDK nhiều ngôn ngữ. Chi tiết runtime mặc định runc/gVisor/Kata chưa kiểm ở mức code. |
| Nguồn | [README.md](https://github.com/opensandbox-group/OpenSandbox/blob/5039696283031c67a7945f1091deef7c8efe61b6/README.md) · [LICENSE](https://github.com/opensandbox-group/OpenSandbox/blob/5039696283031c67a7945f1091deef7c8efe61b6/LICENSE) |

<a id="ch-osworld"></a>

### OSWorld

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/xlang-ai/OSWorld |
| License | Apache-2.0. Khớp catalog. |
| Phiên bản đã đọc | `0ad41bee56565efe7bb3c3a5ebc67590a1b8276f` (commit 2026-11-23) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE, pyproject.toml; chưa chạy upstream |
| Bảo trì | active |
| Nhận định | Benchmark computer-use trên VM với nhiều provider. Phụ thuộc nặng (paddleocr, nhiều SDK LLM) nên cài tách môi trường. |
| Nguồn | [README.md](https://github.com/xlang-ai/OSWorld/blob/0ad41bee56565efe7bb3c3a5ebc67590a1b8276f/README.md) · [LICENSE](https://github.com/xlang-ai/OSWorld/blob/0ad41bee56565efe7bb3c3a5ebc67590a1b8276f/LICENSE) · [pyproject.toml](https://github.com/xlang-ai/OSWorld/blob/0ad41bee56565efe7bb3c3a5ebc67590a1b8276f/pyproject.toml) |

<a id="ch-playwright-cli"></a>

### playwright-cli

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/microsoft/playwright-cli |
| License | Apache-2.0. Khớp catalog. |
| Phiên bản đã đọc | `c872a33cec77fa03c28fa7c6d1ad99d15d04ce42` (commit 2026-11-18) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE, package.json; chưa chạy upstream |
| Bảo trì | active |
| Nhận định | Playwright dạng lệnh kèm skill cho coding agent. Phiên bản 0.1.x nên còn thay đổi nhanh. |
| Nguồn | [README.md](https://github.com/microsoft/playwright-cli/blob/c872a33cec77fa03c28fa7c6d1ad99d15d04ce42/README.md) · [LICENSE](https://github.com/microsoft/playwright-cli/blob/c872a33cec77fa03c28fa7c6d1ad99d15d04ce42/LICENSE) · [package.json](https://github.com/microsoft/playwright-cli/blob/c872a33cec77fa03c28fa7c6d1ad99d15d04ce42/package.json) |

<a id="ch-playwright-mcp"></a>

### Playwright MCP

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/microsoft/playwright-mcp |
| License | Apache-2.0. Khớp catalog. |
| Phiên bản đã đọc | `2337aff0213d28db41d3e3daf48cee19b3d0bd82` (commit 2026-11-18) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE, package.json; chưa chạy upstream |
| Bảo trì | active |
| Nhận định | MCP điều khiển trình duyệt qua Playwright; README tự đưa CLI+SKILLS làm lựa chọn tiết kiệm token hơn cho agent lập trình. |
| Nguồn | [README.md](https://github.com/microsoft/playwright-mcp/blob/2337aff0213d28db41d3e3daf48cee19b3d0bd82/README.md) · [LICENSE](https://github.com/microsoft/playwright-mcp/blob/2337aff0213d28db41d3e3daf48cee19b3d0bd82/LICENSE) · [package.json](https://github.com/microsoft/playwright-mcp/blob/2337aff0213d28db41d3e3daf48cee19b3d0bd82/package.json) |

<a id="ch-rea-reverse-engineer-anything"></a>

### REA – Reverse Engineer Anything

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/morluto/rea |
| License | MIT. Khớp catalog (có THIRD_PARTY_NOTICES và thư mục licenses). |
| Phiên bản đã đọc | `caf5f4e38a1ec1a71dacf77130c211d6b0e3229b` (commit 2026-11-23) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE, licenses, package.json; chưa chạy upstream |
| Bảo trì | active |
| Nhận định | CLI và MCP server dịch ngược cho agent (binary native, Electron/JS, .NET, website), chạy cục bộ. Dự án một tác giả, cần thận trọng với phân tích mã độc. |
| Nguồn | [README.md](https://github.com/morluto/rea/blob/caf5f4e38a1ec1a71dacf77130c211d6b0e3229b/README.md) · [LICENSE](https://github.com/morluto/rea/blob/caf5f4e38a1ec1a71dacf77130c211d6b0e3229b/LICENSE) · [licenses](https://github.com/morluto/rea/blob/caf5f4e38a1ec1a71dacf77130c211d6b0e3229b/licenses) · [package.json](https://github.com/morluto/rea/blob/caf5f4e38a1ec1a71dacf77130c211d6b0e3229b/package.json) |

<a id="ch-sandbox-runtime"></a>

### sandbox-runtime

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/anthropics/sandbox-runtime |
| License | Apache-2.0. Khớp catalog. |
| Phiên bản đã đọc | `0bbebed0aa9a8e628dc4df8bc30293550a1988eb` (commit 2026-11-12) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE, package.json; chưa chạy upstream |
| Bảo trì | active |
| Nhận định | Sandbox cấp OS không cần container cho agent/MCP/lệnh bash; mặc định tối thiểu quyền (theo README). Còn là bản preview, API có thể đổi. |
| Nguồn | [README.md](https://github.com/anthropics/sandbox-runtime/blob/0bbebed0aa9a8e628dc4df8bc30293550a1988eb/README.md) · [LICENSE](https://github.com/anthropics/sandbox-runtime/blob/0bbebed0aa9a8e628dc4df8bc30293550a1988eb/LICENSE) · [package.json](https://github.com/anthropics/sandbox-runtime/blob/0bbebed0aa9a8e628dc4df8bc30293550a1988eb/package.json) |

<a id="ch-skyvern"></a>

### Skyvern

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/Skyvern-AI/skyvern |
| License | AGPL-3.0 (README: lõi AGPL, ngoại trừ biện pháp chống bot chỉ có ở bản cloud). Khớp catalog (AGPL-3.0). |
| Phiên bản đã đọc | `9db98c92dcb5af83be0f98d7495379b8d1a0581b` (commit 2026-11-23) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE, pyproject.toml; chưa chạy upstream |
| Bảo trì | active |
| Nhận định | Agent tự động hóa trình duyệt bằng LLM và thị giác. AGPL ràng buộc khi tự host thành dịch vụ; tính năng chống bot không có trong bản mở. |
| Nguồn | [README.md](https://github.com/Skyvern-AI/skyvern/blob/9db98c92dcb5af83be0f98d7495379b8d1a0581b/README.md) · [LICENSE](https://github.com/Skyvern-AI/skyvern/blob/9db98c92dcb5af83be0f98d7495379b8d1a0581b/LICENSE) · [pyproject.toml](https://github.com/Skyvern-AI/skyvern/blob/9db98c92dcb5af83be0f98d7495379b8d1a0581b/pyproject.toml) |

<a id="ch-stagehand"></a>

### Stagehand

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/browserbase/stagehand |
| License | MIT. Khớp catalog. |
| Phiên bản đã đọc | `3bedd822f2e31c6716added7743179405985a439` (commit 2026-11-20) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE, package.json, pyproject.toml; chưa chạy upstream |
| Bảo trì | active |
| Nhận định | SDK tự động hóa trình duyệt bằng AI (TS, Python) trong monorepo; là nền cho Browserbase MCP đã archive. |
| Nguồn | [README.md](https://github.com/browserbase/stagehand/blob/3bedd822f2e31c6716added7743179405985a439/README.md) · [LICENSE](https://github.com/browserbase/stagehand/blob/3bedd822f2e31c6716added7743179405985a439/LICENSE) · [package.json](https://github.com/browserbase/stagehand/blob/3bedd822f2e31c6716added7743179405985a439/package.json) · [pyproject.toml](https://github.com/browserbase/stagehand/blob/3bedd822f2e31c6716added7743179405985a439/pyproject.toml) |

<a id="ch-ui-tars-desktop"></a>

### UI-TARS-desktop

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/bytedance/UI-TARS-desktop |
| License | Apache-2.0. Khớp catalog. |
| Phiên bản đã đọc | `3ac2cb8d946d78d5ff92ad17b318eaafa18c178c` (commit 2026-10-09) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE, package.json; chưa chạy upstream |
| Bảo trì | low-activity |
| Nhận định | Ứng dụng desktop GUI agent dùng mô hình UI-TARS cùng Agent TARS CLI. Hoạt động chậm hơn các repo cùng lô. |
| Nguồn | [README.md](https://github.com/bytedance/UI-TARS-desktop/blob/3ac2cb8d946d78d5ff92ad17b318eaafa18c178c/README.md) · [LICENSE](https://github.com/bytedance/UI-TARS-desktop/blob/3ac2cb8d946d78d5ff92ad17b318eaafa18c178c/LICENSE) · [package.json](https://github.com/bytedance/UI-TARS-desktop/blob/3ac2cb8d946d78d5ff92ad17b318eaafa18c178c/package.json) |

<a id="ch-webarena"></a>

### WebArena

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/web-arena-x/webarena |
| License | Apache-2.0 |
| Phiên bản đã đọc | `dce04686a56253aefba7b18a4fa0937cf1dc987b` (commit 2025-11-26) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE; chưa chạy upstream |
| Bảo trì | Commit cuối 2025-11-26; README (cập nhật 12/2024) khuyên dùng AgentLab/BrowserGym cho thí nghiệm mới |
| Nhận định | Benchmark web agent tự host (Docker); repo giữ triển khai chuẩn để tái lập kết quả, tác giả khuyên chuyển sang AgentLab cho thí nghiệm mới. Nhịp commit chậm. |
| Nguồn | [README](https://github.com/web-arena-x/webarena/blob/dce04686a56253aefba7b18a4fa0937cf1dc987b/README.md) · [LICENSE](https://github.com/web-arena-x/webarena/blob/dce04686a56253aefba7b18a4fa0937cf1dc987b/LICENSE) |

<a id="nt-2026-11-23"></a>

## Nâng trần theo khoảng trống — 23/11/2026

Phần này có các hồ sơ mới của đợt nâng trần: mười trinh sát tìm trên internet và GitHub những mảng mà chuyên mục còn thiếu hoặc chỉ có hồ sơ cũ, rồi mỗi repo được clone nông tại một commit cố định, đọc LICENSE, README, ít nhất một file triển khai thật và CI nếu có; không cài hay chạy mã upstream. Mô tả của trinh sát nhiều chỗ sai so với mã thật, và các chỗ đó được sửa ngay trong từng hồ sơ. Số sao lấy sau bằng GitHub search API nên có thể để trống.

<a id="nt-rivet-agentos"></a>

### agentOS (Rivet)

| Thuộc tính | Giá trị |
|---|---|
| Repo | https://github.com/rivet-dev/agentos |
| License | Apache-2.0 (file LICENSE ở gốc) |
| Phiên bản đã đọc | `04e6be73a743670726f70cc6d0551a3b4f46abfc` (commit 2026-11-21) |
| Kiểm chứng | 2026-11-23; code-read; đã đọc README, security-model, permissions, limitations, permissions.rs, network_policy.rs và ci.yml; chưa chạy upstream |
| Khoảng trống lấp | Sandbox/isolation (microVM, WASM): lớp cách ly thứ ba, ở mức isolate/WASM trong tiến trình thay cho VM nặng |
| Cơ chế đáng học | - Kernel ảo sở hữu filesystem, process table, socket, PTY và policy cho từng VM; mã khách (V8, WASM, Python) chỉ chạm host qua syscall do sidecar kiểm (security-model.mdx).<br>- `PermissionEvaluator` có ba dạng Deny, Allow, Dynamic và mặc định là Deny; bốn loại request fs/network/command/env (crates/vm-kernel/src/permissions.rs).<br>- Chặn kết nối ra dải private, link-local, CGNAT, multicast và IPv6 nhúng IPv4 (network_policy.rs); `network: deny` chặn cả DNS nhưng vẫn cho loopback trong VM (permissions.mdx).<br>- Actor hosted chỉ nhận cấu hình tuần tự hóa được: không nhận host mount, host path hay callback; các khả năng này chỉ có ở API nhúng tin cậy (README). |
| Tiêu chí và cách kiểm | CI đã đọc (ci.yml): build turbo, check-types, biome, cargo fmt, test đơn vị gói nhanh và script kiểm layout/protocol. Kiểm bằng máy ở cấp build và kiểu; tôi chưa thấy trong ci.yml bước chạy test escape của kernel (chưa xác minh), và permissions.rs không có test nội tuyến (thư mục tests/ của vm-kernel có tệp test riêng, chưa đọc). |
| Giới hạn và rủi ro | Beta, tự ghi là còn đang rà soát bảo mật; ranh giới cách ly là V8 và WASM trong tiến trình sidecar, yếu hơn microVM khi mã khách thoát được isolate (đánh giá của tôi). Không cài tùy ý binary, không Go/Rust/C++ native; muốn có thì phải nối sandbox ngoài. Có crate resource-accounting nhưng chưa xác minh có gửi dữ liệu ra ngoài. License Apache-2.0 đồng nhất ở gốc. |
| So với | e2b, microsandbox, sandbox-runtime, gvisor, firecracker (hồ sơ sandbox có sẵn; các mục này dùng VM hoặc kernel Linux thật, agentOS không) |
| Nguồn | [README.md](https://github.com/rivet-dev/agentos/blob/04e6be73a743670726f70cc6d0551a3b4f46abfc/README.md) · [LICENSE](https://github.com/rivet-dev/agentos/blob/04e6be73a743670726f70cc6d0551a3b4f46abfc/LICENSE) · [security-model.mdx](https://github.com/rivet-dev/agentos/blob/04e6be73a743670726f70cc6d0551a3b4f46abfc/docs/content/docs/security-model.mdx) · [permissions.mdx](https://github.com/rivet-dev/agentos/blob/04e6be73a743670726f70cc6d0551a3b4f46abfc/docs/content/docs/permissions.mdx) · [limitations.mdx](https://github.com/rivet-dev/agentos/blob/04e6be73a743670726f70cc6d0551a3b4f46abfc/docs/content/docs/limitations.mdx) · [permissions.rs](https://github.com/rivet-dev/agentos/blob/04e6be73a743670726f70cc6d0551a3b4f46abfc/crates/vm-kernel/src/permissions.rs) · [network_policy.rs](https://github.com/rivet-dev/agentos/blob/04e6be73a743670726f70cc6d0551a3b4f46abfc/crates/vm-kernel/src/network_policy.rs) · [ci.yml](https://github.com/rivet-dev/agentos/blob/04e6be73a743670726f70cc6d0551a3b4f46abfc/.github/workflows/ci.yml) |

<a id="nt-arcbox"></a>

### ArcBox

| Thuộc tính | Giá trị |
|---|---|
| Repo | https://github.com/arcboxlabs/arcbox |
| License | Apache-2.0 hoặc MIT (LICENSE-APACHE, LICENSE-MIT; NOTICE.md liệt kê phụ thuộc) |
| Phiên bản đã đọc | `31419ccf96e624f9e40724c936c86147e1ca92bc` (commit 2026-11-06) |
| Kiểm chứng | 2026-11-23; code-read; đã đọc README, agent-sandbox.md, sandbox-api.md, jail.rs, contract.rs và ci.yml; chưa chạy upstream |
| Khoảng trống lấp | Sandbox/isolation (microVM, WASM): microVM cục bộ trên macOS, chạy agent coding trong VM thay vì cấp quyền từng lệnh |
| Cơ chế đáng học | - `/workspace` bắt đầu rỗng, không mount thư mục host; kết quả ra bằng API file (giới hạn 256 MiB mỗi file) và tất cả bị hủy khi dừng sandbox (docs/agent-sandbox.md).<br>- Chỉ forward biến `ANTHROPIC_*` và `CLAUDE_*` vào sandbox cho phiên đó; không chép OAuth từ `~/.claude` (agent-sandbox.md).<br>- Firecracker chạy dưới jailer: chroot riêng, file kernel/đĩa/vmstate được stage vào bằng hard link hoặc copy và chown về uid/gid bị giam (virt/arcbox-fc-driver/src/jail.rs).<br>- Contract test dùng chung cho mọi adapter VMM, kèm bản fake chạy được không cần phần cứng (virt/arcbox-vm-driver/src/testkit/contract.rs); checkpoint và restore để khởi động gần như tức thì (README). |
| Tiêu chí và cách kiểm | ci.yml chạy `cargo fmt --check`, `cargo clippy --workspace -D warnings`, build và `cargo test --workspace` (loại arcbox-agent), kèm job SDK TypeScript/Python và proto-compat; test với phần cứng thật đánh dấu ignore nên không nằm trong CI thường (suy từ contract.rs, chưa xác minh toàn bộ). |
| Giới hạn và rủi ro | Chỉ macOS (Apple Silicon M3+, macOS 15+ cho sandbox); trên máy khác mọi RPC sandbox trả FAILED_PRECONDITION (docs). Bản beta; `abctl claude` tắt prompt quyền mặc định (có `--no-bypass`), nên an toàn dựa hoàn toàn vào ranh giới VM. Chưa thấy telemetry trong README và docs đã đọc (không grep toàn mã). Cài bằng script tải về rồi chuyển thẳng cho shell (curl rồi bash) là rủi ro chuỗi cung ứng cần tự rà. Cặp license MIT/Apache cho người dùng chọn. |
| So với | microsandbox, e2b, firecracker, docker-sandboxes, cubesandbox |
| Nguồn | [README.md](https://github.com/arcboxlabs/arcbox/blob/31419ccf96e624f9e40724c936c86147e1ca92bc/README.md) · [LICENSE-APACHE](https://github.com/arcboxlabs/arcbox/blob/31419ccf96e624f9e40724c936c86147e1ca92bc/LICENSE-APACHE) · [LICENSE-MIT](https://github.com/arcboxlabs/arcbox/blob/31419ccf96e624f9e40724c936c86147e1ca92bc/LICENSE-MIT) · [agent-sandbox.md](https://github.com/arcboxlabs/arcbox/blob/31419ccf96e624f9e40724c936c86147e1ca92bc/docs/agent-sandbox.md) · [sandbox-api.md](https://github.com/arcboxlabs/arcbox/blob/31419ccf96e624f9e40724c936c86147e1ca92bc/docs/sandbox-api.md) · [jail.rs](https://github.com/arcboxlabs/arcbox/blob/31419ccf96e624f9e40724c936c86147e1ca92bc/virt/arcbox-fc-driver/src/jail.rs) · [contract.rs](https://github.com/arcboxlabs/arcbox/blob/31419ccf96e624f9e40724c936c86147e1ca92bc/virt/arcbox-vm-driver/src/testkit/contract.rs) · [ci.yml](https://github.com/arcboxlabs/arcbox/blob/31419ccf96e624f9e40724c936c86147e1ca92bc/.github/workflows/ci.yml) |

<a id="nt-e2b-open-computer-use"></a>

### Open Computer Use (E2B)

| Thuộc tính | Giá trị |
|---|---|
| Repo | https://github.com/e2b-dev/open-computer-use |
| License | Apache-2.0 (LICENSE) |
| Phiên bản đã đọc | `ee1025911c36e1f28bb3400c7d81170a8482f35d` (commit 2026-10-23) |
| Kiểm chứng | 2026-11-23; code-read; đã đọc README, sandbox_agent.py, config.py, osatlas_provider.py và tests/sandbox_agent.py; chưa chạy upstream |
| Khoảng trống lấp | Computer-use an toàn: ví dụ nhỏ đọc được toàn bộ về agent điều khiển desktop trong sandbox đám mây |
| Cơ chế đáng học | - `SandboxAgent.run`: mỗi vòng gia hạn timeout sandbox 60 giây, chụp màn hình, vision model mô tả, action model chọn tool; kết quả tool thành OBSERVATION trong lịch sử (os_computer_use/sandbox_agent.py).<br>- Tool đăng ký bằng decorator `@tool` vào dict `tools`; `call_function` bắt mọi exception và trả lỗi thành chuỗi (sandbox_agent.py).<br>- Click qua grounding: gửi ảnh và mô tả tới OS-Atlas, nhận bbox, lấy tâm rồi di chuột (osatlas_provider.py, grounding.py). |
| Tiêu chí và cách kiểm | Không có workflow CI. tests/sandbox_agent.py dùng sandbox giả và ảnh tĩnh, đã mở nhưng chưa chạy; không có ngưỡng hay kiểm an toàn nào. |
| Giới hạn và rủi ro | Mã không có hàng rào quyền: mô hình chạy được shell tùy ý trong sandbox (`run_command`, timeout 5 giây) và truy cập mạng của sandbox. Screenshot gửi tới Space công khai của Hugging Face (`maxiw/OS-ATLAS`) và các LLM provider; cần E2B API key và khóa LLM. Cấu hình mặc định đọc từ config.py (Groq llama-3.3, OpenRouter qwen-2.5-vl) có thể lệch README. Lần commit gần nhất 2026-10-23 là bump certifi; mức bảo trì thấp (chưa xác minh). |
| So với | cua, e2b, browser-use, browsergym |
| Nguồn | [README.md](https://github.com/e2b-dev/open-computer-use/blob/ee1025911c36e1f28bb3400c7d81170a8482f35d/README.md) · [LICENSE](https://github.com/e2b-dev/open-computer-use/blob/ee1025911c36e1f28bb3400c7d81170a8482f35d/LICENSE) · [sandbox_agent.py](https://github.com/e2b-dev/open-computer-use/blob/ee1025911c36e1f28bb3400c7d81170a8482f35d/os_computer_use/sandbox_agent.py) · [config.py](https://github.com/e2b-dev/open-computer-use/blob/ee1025911c36e1f28bb3400c7d81170a8482f35d/os_computer_use/config.py) · [osatlas_provider.py](https://github.com/e2b-dev/open-computer-use/blob/ee1025911c36e1f28bb3400c7d81170a8482f35d/os_computer_use/osatlas_provider.py) · [sandbox_agent.py](https://github.com/e2b-dev/open-computer-use/blob/ee1025911c36e1f28bb3400c7d81170a8482f35d/tests/sandbox_agent.py) |

<a id="nt-e2b-surf"></a>

### Surf (E2B)

| Thuộc tính | Giá trị |
|---|---|
| Repo | https://github.com/e2b-dev/surf |
| License | Apache-2.0 (LICENSE) |
| Phiên bản đã đọc | `d66db293ac513a98abe1fd5c58a69b5130e4a996` (commit 2026-10-13) |
| Kiểm chứng | 2026-11-23; code-read; đã đọc README, route.ts, config.ts và lib/streaming/openai.ts (đọc từng phần); chưa chạy upstream |
| Khoảng trống lấp | Computer-use an toàn: ví dụ web đầy đủ gắn model computer-use của OpenAI với sandbox desktop |
| Cơ chế đáng học | - `POST /api/chat` tạo `Sandbox.create` của E2B với độ phân giải và timeout 300000 ms, hoặc nối lại `sandboxId`, rồi stream sự kiện (app/api/chat/route.ts).<br>- Độ phân giải giới hạn 640x480 tới 1024x768, mặc định 1024x720; screenshot gửi nguyên chi tiết, không scale (lib/config.ts).<br>- Vòng lặp trong lib/streaming/openai.ts áp dụng `truncation: auto`, gom batch hành động và chờ trễ 100 ms trước khi chụp lại trong một số trường hợp. |
| Tiêu chí và cách kiểm | Không có workflow CI; `package.json` chỉ có script dev/build/start/lint. Có lib/streaming/resolution.test.ts nhưng không có script test chạy nó (chưa chạy, chưa mở nội dung). |
| Giới hạn và rủi ro | Grep trong app và lib không thấy cơ chế xác thực, nên ai tới được endpoint đều tạo sandbox bằng `E2B_API_KEY` và gọi OpenAI bằng khóa của chủ triển khai (chi phí và lạm dụng). System prompt trong mã nói môi trường cho phép không lo bảo mật; không thấy xử lý pending safety checks của computer use (grep không có kết quả). Cần E2B và OpenAI key. License Apache-2.0. |
| So với | e2b-open-computer-use (cùng hãng), cua, e2b, browser-use |
| Nguồn | [README.md](https://github.com/e2b-dev/surf/blob/d66db293ac513a98abe1fd5c58a69b5130e4a996/README.md) · [LICENSE](https://github.com/e2b-dev/surf/blob/d66db293ac513a98abe1fd5c58a69b5130e4a996/LICENSE) · [route.ts](https://github.com/e2b-dev/surf/blob/d66db293ac513a98abe1fd5c58a69b5130e4a996/app/api/chat/route.ts) · [config.ts](https://github.com/e2b-dev/surf/blob/d66db293ac513a98abe1fd5c58a69b5130e4a996/lib/config.ts) · [openai.ts](https://github.com/e2b-dev/surf/blob/d66db293ac513a98abe1fd5c58a69b5130e4a996/lib/streaming/openai.ts) |

<a id="nt-agent-device"></a>

### agent-device

| Thuộc tính | Giá trị |
|---|---|
| Repo | https://github.com/callstack/agent-device |
| License | MIT (kèm Apache-2.0 và thành phần bên thứ ba trong LICENSES/) |
| Phiên bản đã đọc | `ecb2089867e91c626be0f29e1c41cab466ceb954` (commit 2026-11-23) |
| Kiểm chứng | 2026-11-23; code-read; đã đọc LICENSE, README, package.json, SECURITY.md, SKILL.md, ci.yml, perf-nightly.yml, conformance-differential.yml (phần đầu), cli-help.ts và management/app.ts (đoạn mô tả lệnh); chưa chạy upstream |
| Khoảng trống lấp | Kiểm thử mobile trên thiết bị và hiệu năng (lớp thiết bị cho agent) |
| Cơ chế đáng học | - Vòng lặp snapshot accessibility có `@ref`: `open` trả snapshot, hành động (`press`, `fill`, `--settle`) trả diff chỉ thay đổi, agent dùng ref thay vì toạ độ hay ảnh chụp (SKILL.md, README).<br>- Cùng một lõi phục vụ CLI, MCP (`src/mcp/`) và API Node; hỗ trợ iOS, Android, HarmonyOS, TV, web, macOS, Linux qua các package platform-* và provider đám mây.<br>- Khoá thiết bị giữa các agent song song: thiết bị đang bị session khác giữ thì từ chối ngay, có `--wait <ms>` rồi mới báo `DEVICE_IN_USE` nêu session sở hữu (mô tả lệnh open trong `packages/command-surface/src/management/app.ts`).<br>- Lệnh `perf` (frames, memory, cpu) và workflow `perf-nightly.yml` so trung vị với tối đa bảy đêm trước, bước chỉ bị đánh dấu khi vượt độ phân tán, sai số mẫu, 20% và 50 ms. |
| Tiêu chí và cách kiểm | CI nhiều job (ci.yml: lint-typecheck, repo-guards, coverage có waiver, integration) cùng workflow riêng cho apple, android, linux, mutation test, replay nightly. `conformance-differential.yml` chạy cùng kịch bản qua Maestro thật và agent-device để so kết quả quan sát được, có khai báo `knownDivergence` (tất cả kiểm bằng máy trong CI, chưa chạy lại ở đây). |
| Giới hạn và rủi ro | Phiên bản 0.21.43-dev: API còn đổi nhanh. Số tính năng và giới hạn nền tảng rất rộng, khó đánh giá hết; phần đã đọc chỉ là mẫu. Daemon điều khiển thiết bị và nhận lệnh chạy ứng dụng nên cần kiểm quyền và token daemon trước khi dùng cho agent không tin cậy. Không thấy gửi telemetry trong phần đã mở (chưa quét toàn bộ). Trinh sát ghi MIT: đúng nhưng LICENSES/ có Apache-2.0 và thành phần bên thứ ba. Mô tả lệnh trong CLI rất dài, tốn token nếu nạp vào ngữ cảnh agent. |
| So với | maestro, appium-appium |
| Nguồn | [LICENSE](https://github.com/callstack/agent-device/blob/ecb2089867e91c626be0f29e1c41cab466ceb954/LICENSE) · [README.md](https://github.com/callstack/agent-device/blob/ecb2089867e91c626be0f29e1c41cab466ceb954/README.md) · [package.json](https://github.com/callstack/agent-device/blob/ecb2089867e91c626be0f29e1c41cab466ceb954/package.json) · [SECURITY.md](https://github.com/callstack/agent-device/blob/ecb2089867e91c626be0f29e1c41cab466ceb954/SECURITY.md) · [skills/agent-device/SKILL.md](https://github.com/callstack/agent-device/blob/ecb2089867e91c626be0f29e1c41cab466ceb954/skills/agent-device/SKILL.md) · [.github/workflows/ci.yml](https://github.com/callstack/agent-device/blob/ecb2089867e91c626be0f29e1c41cab466ceb954/.github/workflows/ci.yml) · [.github/workflows/perf-nightly.yml](https://github.com/callstack/agent-device/blob/ecb2089867e91c626be0f29e1c41cab466ceb954/.github/workflows/perf-nightly.yml) · [.github/workflows/conformance-differential.yml](https://github.com/callstack/agent-device/blob/ecb2089867e91c626be0f29e1c41cab466ceb954/.github/workflows/conformance-differential.yml) · [src/commands/schema/cli-help.ts](https://github.com/callstack/agent-device/blob/ecb2089867e91c626be0f29e1c41cab466ceb954/src/commands/schema/cli-help.ts) · [packages/command-surface/src/management/app.ts](https://github.com/callstack/agent-device/blob/ecb2089867e91c626be0f29e1c41cab466ceb954/packages/command-surface/src/management/app.ts) |

<a id="nt-perplexity-space"></a>

### SPACE (Perplexity)

| Thuộc tính | Giá trị |
|---|---|
| Repo | https://github.com/perplexityai/SPACE |
| License | Apache-2.0 |
| Phiên bản đã đọc | `432ff2e7d9061cc0e47177d900a8b3c6cc5399df` (commit 2026-11-23) |
| Kiểm chứng | 2026-11-23; code-read; đã đọc LICENSE, README.md, docs/architecture.md, docs/egress-profiles.md, docs/installation.md; chưa chạy upstream |
| Khoảng trống lấp | Sandbox/isolation (microVM): sandbox microVM Firecracker tự host cho agent, có lifecycle và egress có kiểm soát |
| Cơ chế đáng học | - `docs/architecture.md`: template (có digest), sandbox (microVM có đĩa ghi riêng), process, command session (token đính kèm theo phiên) và operation bất đồng bộ; API ghi trạng thái mong muốn vào PostgreSQL, controller đối soát; hai adapter Kubernetes và direct.<br>- `docs/egress-profiles.md` và `crates/l40_api/api/src/egress_profiles.rs`: biến `SPACE_EGRESS_PROFILES` định nghĩa hồ sơ cho phép theo IP, CIDR, domain chính xác (không wildcard); chọn bằng header `X-Space-Egress-Profiles: +name -name`; deny của tenant và platform luôn thắng; lựa chọn bất biến theo vòng đời sandbox.<br>- Chính sách template tin cậy: danh sách bucket S3 cho phép khi đăng ký template (`SPACE_TRUSTED_TEMPLATE_STORAGE_BUCKETS`).<br>- `docs/observability.md`: bộ chọn exporter Datadog hoặc OTLP, lỗi cấu hình thì báo, không im lặng chuyển mặc định. |
| Tiêu chí và cách kiểm | CI có nhiều workflow (`main-ci.yml` đã mở, còn pull-ci, kind-ci, fuzz...); `ARCHITECTURE.toml` do `cargo arch` kiểm quy tắc cấu trúc, `deny.toml` (cargo-deny) giới hạn license phụ thuộc và nguồn registry; kiểm bằng máy. Chưa chạy lại; `docs/versioning.md` nói 0.8.0 là baseline, 0.9.0 là lần phá vỡ cuối trước 1.0. |
| Giới hạn và rủi ro | Apache-2.0 (LICENSE đã đọc, ghi Copyright 2026 Perplexity AI). Yêu cầu hạ tầng nặng: host Linux x86_64 có `/dev/kvm`, loop device, btrfs, Docker đặc quyền, 30 GiB trống; không chạy trên macOS. Trường `incubating` và các thao tác snapshot/checkpoint nằm ngoài hợp đồng hỗ trợ. Có CLA dự kiến, chỉ bản minor mới nhất nhận bản vá bảo mật (SECURITY.md). Độ cô lập của microVM là tuyên bố của kiến trúc **(chưa xác minh bằng kiểm thử thoát)**. |
| So với | firecracker (thành phần nền), e2b và opensandbox (cùng nhiệm vụ sandbox cho agent), gvisor và kata-containers (cô lập kiểu khác) |
| Nguồn | [LICENSE](https://github.com/perplexityai/SPACE/blob/432ff2e7d9061cc0e47177d900a8b3c6cc5399df/LICENSE) · [README.md](https://github.com/perplexityai/SPACE/blob/432ff2e7d9061cc0e47177d900a8b3c6cc5399df/README.md) · [docs/architecture.md](https://github.com/perplexityai/SPACE/blob/432ff2e7d9061cc0e47177d900a8b3c6cc5399df/docs/architecture.md) · [docs/egress-profiles.md](https://github.com/perplexityai/SPACE/blob/432ff2e7d9061cc0e47177d900a8b3c6cc5399df/docs/egress-profiles.md) · [docs/installation.md](https://github.com/perplexityai/SPACE/blob/432ff2e7d9061cc0e47177d900a8b3c6cc5399df/docs/installation.md) · [docs/versioning.md](https://github.com/perplexityai/SPACE/blob/432ff2e7d9061cc0e47177d900a8b3c6cc5399df/docs/versioning.md) · [docs/observability.md](https://github.com/perplexityai/SPACE/blob/432ff2e7d9061cc0e47177d900a8b3c6cc5399df/docs/observability.md) · [crates/l40_api/api/src/egress_profiles.rs](https://github.com/perplexityai/SPACE/blob/432ff2e7d9061cc0e47177d900a8b3c6cc5399df/crates/l40_api/api/src/egress_profiles.rs) · [ARCHITECTURE.toml](https://github.com/perplexityai/SPACE/blob/432ff2e7d9061cc0e47177d900a8b3c6cc5399df/ARCHITECTURE.toml) · [deny.toml](https://github.com/perplexityai/SPACE/blob/432ff2e7d9061cc0e47177d900a8b3c6cc5399df/deny.toml) · [.github/workflows/main-ci.yml](https://github.com/perplexityai/SPACE/blob/432ff2e7d9061cc0e47177d900a8b3c6cc5399df/.github/workflows/main-ci.yml) |

<a id="n2-2026-11-24"></a>

## Nâng trần đợt hai — 23/11/2026

Hồ sơ lập trong đợt nâng trần thứ hai: đọc mã hoặc tài liệu tại commit cố định, chưa chạy upstream; mô tả của trinh sát sai ở nhiều repo nên điều ghi ở đây là điều đã đọc.

<a id="n2-pullrun-agent-sandbox"></a>

### Pullrun

| Thuộc tính | Giá trị |
|---|---|
| Repo | https://github.com/pullrun/pullrun |
| License | Apache-2.0 |
| Phiên bản đã đọc | `0a45f4841753cd161439225a7bd14858dd7ec4d5` (commit 2026-11-24) |
| Kiểm chứng | 2026-11-24; code-read; đã đọc README.md, LICENSE, docs/SECURITY_STATUS.md, docs/TIERS.md, docs/SNAPSHOTS.md, runtime/pullrun-vm/src/egress.rs, docs/BUSINESS.md, .github/workflows/ci.yml; chưa chạy upstream |
| Khoảng trống lấp | Sandbox/isolation (microVM): runtime Rust chạy OCI image trong Firecracker hoặc Apple VM, snapshot bộ nhớ |
| Cơ chế đáng học | - Cùng một image OCI chạy ở nhiều tầng: container, VM Firecracker từng tác vụ, nhóm sandbox trong một VM (macOS): `docs/TIERS.md`.<br>- Snapshot bộ nhớ Firecracker và rootfs; khôi phục 63–119 ms trong bản đo của tác giả, mã hóa AES-256-GCM kèm SHA-256 từng file: `docs/SNAPSHOTS.md`, `docs/SECURITY_STATUS.md`.<br>- Egress fail-closed bằng nftables theo từng VM trên bridge, chỉ cho phép danh sách và lưu lượng đã thiết lập: `runtime/pullrun-vm/src/egress.rs`.<br>- Có MCP server 15 tool để agent tự điều khiển. |
| Tiêu chí và cách kiểm | CI: `cargo build/test --workspace`, clippy `-D warnings`, `fmt --check`, và workflow fuzz (đã mở `ci.yml`, chưa mở `fuzz.yml`); `SECURITY_STATUS.md` tự chấm từng nguyên tắc Met/Partial/Future, đo 23,7 triệu lượt fuzz parser OCI. Số đo tốc độ là của tác giả (chưa xác minh). |
| Giới hạn và rủi ro | Đồng bộ tài liệu chưa nhất quán: README nói "bốn tầng cô lập" còn `TIERS.md` liệt kê ba; README ghi snapshot dạng văn bản thô, trong khi `SECURITY_STATUS.md` và `SNAPSHOTS.md` ghi mã hóa AES-256-GCM (README có thể cũ). Egress fail-closed chỉ cho container root và VM bridge; VM rootless chưa có; nhóm sandbox chỉ macOS; control plane chỉ là stub, một nút. Checkout nông nên không xác minh được lịch sử. Có lộ trình thương mại OEM/on-prem (`BUSINESS.md`), chưa có kiểm toán độc lập, 0.11.x còn sớm. |
| So với | `firecracker`, `microsandbox`, `opensandbox` |
| Nguồn | [README.md](https://github.com/pullrun/pullrun/blob/0a45f4841753cd161439225a7bd14858dd7ec4d5/README.md) · [LICENSE](https://github.com/pullrun/pullrun/blob/0a45f4841753cd161439225a7bd14858dd7ec4d5/LICENSE) · [SECURITY_STATUS.md](https://github.com/pullrun/pullrun/blob/0a45f4841753cd161439225a7bd14858dd7ec4d5/docs/SECURITY_STATUS.md) · [TIERS.md](https://github.com/pullrun/pullrun/blob/0a45f4841753cd161439225a7bd14858dd7ec4d5/docs/TIERS.md) · [SNAPSHOTS.md](https://github.com/pullrun/pullrun/blob/0a45f4841753cd161439225a7bd14858dd7ec4d5/docs/SNAPSHOTS.md) · [egress.rs](https://github.com/pullrun/pullrun/blob/0a45f4841753cd161439225a7bd14858dd7ec4d5/runtime/pullrun-vm/src/egress.rs) · [BUSINESS.md](https://github.com/pullrun/pullrun/blob/0a45f4841753cd161439225a7bd14858dd7ec4d5/docs/BUSINESS.md) · [ci.yml](https://github.com/pullrun/pullrun/blob/0a45f4841753cd161439225a7bd14858dd7ec4d5/.github/workflows/ci.yml) |

<a id="n2-capsulerun-capsule-wasm"></a>

### Capsule (capsulerun)

| Thuộc tính | Giá trị |
|---|---|
| Repo | https://github.com/capsulerun/runtime |
| License | Apache-2.0 |
| Phiên bản đã đọc | `7588fc7d24dddc5f8da38e51beb6c0d4eb30d061` (commit 2026-10-12) |
| Kiểm chứng | 2026-11-24; code-read; đã đọc README.md, LICENSE, crates/capsule-core/src/wasm/execution_policy.rs, crates/capsule-core/Cargo.toml, .github/workflows/ci.yml; chưa chạy upstream |
| Khoảng trống lấp | Sandbox WASM cho mã do agent sinh: mỗi tác vụ một module Wasm có hạn mức |
| Cơ chế đáng học | - Hàm Python hoặc TypeScript gắn `@task`/`task()` được biên dịch thành module WebAssembly và chạy dưới Wasmtime; mỗi tác vụ một sandbox: `README.md`.<br>- CPU giới hạn bằng fuel của Wasm: LOW 100 triệu, MEDIUM 2 tỷ, HIGH 50 tỷ lệnh (hoặc `Custom`), cộng `ram`, `timeout`, `max_retries`: `execution_policy.rs`.<br>- Quyền mặc định rỗng: `allowed_files` (có chế độ ro), `allowed_hosts`, `env_variables` đều phải khai báo; nhật ký thực thi lưu fuel đã dùng, RAM, số request host vào SQLite: `config/log.rs`. |
| Tiêu chí và cách kiểm | CI: `cargo fmt --check`, clippy `-D warnings`, test lõi Rust, thêm workflow phát hành cho adapter Python, TypeScript, MCP (đã mở `ci.yml`). Chưa chạy. |
| Giới hạn và rủi ro | Chỉ chạy mã biên dịch được sang Wasm (hệ sinh thái Python/JS hạn chế, không chạy được tiến trình hay thư viện native tùy ý), khác với sandbox VM. Cô lập dựa vào Wasmtime 29 chứ không có kernel riêng. `ram` và `timeout` mặc định không giới hạn nên phải đặt tường minh. Không thấy telemetry trong mã Rust (tìm từ khóa, không phải kiểm toán). Dự án trẻ (0.8.x), cập nhật gần nhất 2026-10-12. |
| So với | `monty`, `microsandbox`, `sandbox-runtime` |
| Nguồn | [README.md](https://github.com/capsulerun/runtime/blob/7588fc7d24dddc5f8da38e51beb6c0d4eb30d061/README.md) · [LICENSE](https://github.com/capsulerun/runtime/blob/7588fc7d24dddc5f8da38e51beb6c0d4eb30d061/LICENSE) · [execution_policy.rs](https://github.com/capsulerun/runtime/blob/7588fc7d24dddc5f8da38e51beb6c0d4eb30d061/crates/capsule-core/src/wasm/execution_policy.rs) · [Cargo.toml](https://github.com/capsulerun/runtime/blob/7588fc7d24dddc5f8da38e51beb6c0d4eb30d061/crates/capsule-core/Cargo.toml) · [ci.yml](https://github.com/capsulerun/runtime/blob/7588fc7d24dddc5f8da38e51beb6c0d4eb30d061/.github/workflows/ci.yml) |

<a id="n2-swe-rex-runtime"></a>

### SWE-ReX

| Thuộc tính | Giá trị |
|---|---|
| Repo | https://github.com/SWE-agent/SWE-ReX |
| License | MIT |
| Phiên bản đã đọc | `5c995c365dfb1fd5bc56fda688be5d8538f9931f` (commit 2026-03-02) |
| Kiểm chứng | 2026-11-24; code-read; đã đọc README.md, LICENSE.txt, src/swerex/runtime/abstract.py, src/swerex/server.py, src/swerex/deployment/docker.py, .github/workflows/pytest.yaml; chưa chạy upstream |
| Khoảng trống lấp | Lớp runtime thực thi shell cho agent trên nhiều backend (Docker, Modal, Fargate, Daytona), không phải sandbox cô lập |
| Cơ chế đáng học | - Giao diện `AbstractRuntime` gồm phiên bash nhiều luồng, nhận biết lệnh kết thúc, lấy exit code và hỗ trợ lệnh tương tác (gdb, ipython): `runtime/abstract.py`.<br>- Cùng mã agent chạy trên `docker`, `modal`, `fargate`, `daytona`, `local`, `remote` nhờ lớp `Deployment` trừu tượng: `deployment/`.<br>- Triển khai Docker khởi chạy container, mở cổng, rồi đợi `is_alive` với token xác thực; server FastAPI kiểm `X-API-Key`, hỗ trợ `X-Request-ID` lũy đẳng: `server.py`, `deployment/docker.py`. |
| Tiêu chí và cách kiểm | CI: workflow pytest dựng image Docker kiểm thử rồi chạy bộ test (có test docker, local, fargate; job dùng secret Modal). Đã mở `pytest.yaml`. Chưa chạy. |
| Giới hạn và rủi ro | Mô tả trinh sát hơi lệch: đây không phải sandbox, cô lập hoàn toàn do backend (container Docker, Modal...); `LocalDeployment` chạy lệnh thẳng trên máy. `docker run -p` mặc định gắn mọi giao diện và `docker_args` tùy ý; so khóa bằng `!=` không phải so sánh hằng thời gian (chỉ đọc mã, không phải khai thác). Kiểm tra cổng nên đặt token luôn. Backend Daytona ghi WIP. Commit mới nhất 2026-03-02, tức khoảng 9 tháng không cập nhật tại thời điểm kiểm (bảo trì chậm). |
| So với | `e2b`, `modal`, `daytona`, `opensandbox` |
| Nguồn | [README.md](https://github.com/SWE-agent/SWE-ReX/blob/5c995c365dfb1fd5bc56fda688be5d8538f9931f/README.md) · [LICENSE.txt](https://github.com/SWE-agent/SWE-ReX/blob/5c995c365dfb1fd5bc56fda688be5d8538f9931f/LICENSE.txt) · [abstract.py](https://github.com/SWE-agent/SWE-ReX/blob/5c995c365dfb1fd5bc56fda688be5d8538f9931f/src/swerex/runtime/abstract.py) · [server.py](https://github.com/SWE-agent/SWE-ReX/blob/5c995c365dfb1fd5bc56fda688be5d8538f9931f/src/swerex/server.py) · [docker.py](https://github.com/SWE-agent/SWE-ReX/blob/5c995c365dfb1fd5bc56fda688be5d8538f9931f/src/swerex/deployment/docker.py) · [pytest.yaml](https://github.com/SWE-agent/SWE-ReX/blob/5c995c365dfb1fd5bc56fda688be5d8538f9931f/.github/workflows/pytest.yaml) |

<a id="n2-pctx"></a>

### pctx (Port of Context)

| Thuộc tính | Giá trị |
|---|---|
| Repo | https://github.com/portofcontext/pctx |
| License | MIT |
| Phiên bản đã đọc | `499379dfb6a145185f2f8021bb9751584f8ed6fd` (commit 2026-11-02) |
| Kiểm chứng | 2026-11-24; code-read; đã đọc LICENSE, README.md, CHANGELOG.md, lib.rs, module_loading.rs, timeout.rs; chưa chạy upstream |
| Khoảng trống lấp | Sandbox/isolation: chạy mã do LLM sinh trong isolate hạn chế, giữ bí mật auth ngoài tầm nhìn của mô hình |
| Cơ chế đáng học | - execute() giữ mutex V8 toàn tiến trình, chạy type check TypeScript trước, chỉ chạy khi không có diagnostic, rồi trả stdout, stderr, output và trace sự kiện (`crates/pctx_executor/src/lib.rs`).<br>- Isolate dựng từ snapshot, module loader là NoopModuleLoader nên mọi import() bị từ chối, kể cả đọc file host (`lib.rs`, `tests/module_loading.rs`).<br>- Hạn giờ mặc định 120 giây, vòng lặp vô hạn bị dừng và lần chạy sau vẫn chạy được (`tests/timeout.rs`).<br>- Telemetry OTLP là cấu hình tùy chọn với cờ enabled, mặc định tắt theo derive Default (`crates/pctx_config/src/telemetry.rs`). |
| Tiêu chí và cách kiểm | Test Rust trong crates/pctx_executor/src/tests (module_loading, timeout, runtime_semantics, type_checking, mcp_client_usage, concurrent_v8_stress). Workflow ci.yaml đã mở: cargo fmt --check và cargo test --workspace --locked trên ubuntu; job clippy bị comment tắt; chỉ Linux (macOS và Windows còn TODO). Kiểm bằng máy, nhưng tôi chưa chạy. |
| Giới hạn và rủi ro | MIT (Sideko, Inc.). Phiên bản v1.0.0 (2026-10-30 theo CHANGELOG). Cô lập chỉ ở mức isolate V8, không có giới hạn bộ nhớ hay CPU ngoài thời gian đã đọc thấy; không thấy ranh giới tiến trình hay hệ điều hành. Mô tả của trinh sát "microVM, WASM" là sai: đây là Deno/V8. Allow-list host trong README không có đường thực thi tương ứng trong executor (chưa xác minh phía session server). CI bỏ clippy. |
| So với | sandbox-runtime (Anthropic, cô lập mức hệ điều hành), microsandbox (microVM), opensandbox; khác nhau ở chỗ pctx cô lập ngôn ngữ chứ không cô lập tiến trình |
| Nguồn | [LICENSE](https://github.com/portofcontext/pctx/blob/499379dfb6a145185f2f8021bb9751584f8ed6fd/LICENSE) · [README.md](https://github.com/portofcontext/pctx/blob/499379dfb6a145185f2f8021bb9751584f8ed6fd/README.md) · [CHANGELOG.md](https://github.com/portofcontext/pctx/blob/499379dfb6a145185f2f8021bb9751584f8ed6fd/CHANGELOG.md) · [lib.rs](https://github.com/portofcontext/pctx/blob/499379dfb6a145185f2f8021bb9751584f8ed6fd/crates/pctx_executor/src/lib.rs) · [module_loading.rs](https://github.com/portofcontext/pctx/blob/499379dfb6a145185f2f8021bb9751584f8ed6fd/crates/pctx_executor/src/tests/module_loading.rs) · [timeout.rs](https://github.com/portofcontext/pctx/blob/499379dfb6a145185f2f8021bb9751584f8ed6fd/crates/pctx_executor/src/tests/timeout.rs) · [telemetry.rs](https://github.com/portofcontext/pctx/blob/499379dfb6a145185f2f8021bb9751584f8ed6fd/crates/pctx_config/src/telemetry.rs) · [ci.yaml](https://github.com/portofcontext/pctx/blob/499379dfb6a145185f2f8021bb9751584f8ed6fd/.github/workflows/ci.yaml) |

<a id="n2-agent-vault-infisical"></a>

### Agent Vault (Infisical)

| Thuộc tính | Giá trị |
|---|---|
| Repo | https://github.com/Infisical/agent-vault |
| License | MIT (Infisical, ngoại trừ thư mục ee/ nếu có; không thấy thư mục ee/ ở commit này) |
| Phiên bản đã đọc | `16ec8d5a5db38be9d2c77fe9c19c7fd7125246ba` (commit 2026-11-06) |
| Kiểm chứng | 2026-11-24; code-read; đã đọc README, LICENSE, `cmd/telemetry.go`, `telemetry.go`, `brokercore/substitution.go`, `netguard.go`, `crypto.go`, ci.yml; chưa chạy upstream |
| Khoảng trống lấp | Môi giới thông tin xác thực (credential broker): agent không bao giờ cầm khoá thật |
| Cơ chế đáng học | • Proxy MITM HTTPS: agent đặt `HTTPS_PROXY`, gửi giá trị giả như `__anthropic_api_key__`, proxy thay bằng khoá thật trên đường ra — README.md, `internal/brokercore/substitution.go`.<br>• Thay thế khai báo theo bề mặt (`path`, `query`, `header`, `body`, `websocket`) làm ranh giới an ninh, có chặn CRLF ở header; lỗi thì không chuyển tiếp — `substitution.go`.<br>• `netguard` chặn mặc định dải IP riêng/loopback/link-local và luôn chặn endpoint metadata đám mây; có chế độ `unmatched_host_policy=deny` để chỉ cho đi tới dịch vụ đã khai báo — `netguard.go`, README.<br>• Kho khoá cục bộ mã hóa AES-256-GCM (`internal/crypto/crypto.go`), có log yêu cầu và egress filtering; thiết kế chạy trên máy tách khỏi agent. |
| Tiêu chí và cách kiểm | Kiểm bằng máy: CI chạy `go test -race -count=1 ./...`, lint, go mod tidy, có job bảo mật chạy mọi PR (đã mở ci.yml; chưa xác minh kết quả). Chưa chạy. |
| Giới hạn và rủi ro | README mở đầu bằng cảnh báo: bản mã nguồn mở này KHÔNG còn được khuyến nghị cho thiết lập mới, hãy dùng Agent Vault trong nền tảng Infisical (dịch vụ riêng). README còn có dòng chỉ thị gửi tới AI agent (đã coi là dữ liệu, không làm theo). Telemetry ẩn danh qua PostHog bật mặc định (cờ `--telemetry` mặc định true, hoặc `AGENT_VAULT_TELEMETRY`), dùng machine ID. Phải tin CA do proxy tự cấp cho MITM; mặc định yêu cầu không khớp dịch vụ vẫn được chuyển như proxy thường. Trinh sát ghi license '-', thực tế là MIT; số sao 530 lấy từ web (chưa xác minh). |
| So với | [NemoClaw](11-browser-computer-use-sandbox/README.md) (sandbox có chính sách mạng) · [External Secrets](12-ai-security-guardrails/README.md) (đưa secret vào K8s, không phải broker cho agent) · [Destructive Command Guard](12-ai-security-guardrails/README.md#ch-dcg-destructive-command-guard) |
| Nguồn | [README.md](https://github.com/Infisical/agent-vault/blob/16ec8d5a5db38be9d2c77fe9c19c7fd7125246ba/README.md) · [LICENSE](https://github.com/Infisical/agent-vault/blob/16ec8d5a5db38be9d2c77fe9c19c7fd7125246ba/LICENSE) · [telemetry.go](https://github.com/Infisical/agent-vault/blob/16ec8d5a5db38be9d2c77fe9c19c7fd7125246ba/cmd/telemetry.go) · [telemetry.go](https://github.com/Infisical/agent-vault/blob/16ec8d5a5db38be9d2c77fe9c19c7fd7125246ba/internal/telemetry/telemetry.go) · [substitution.go](https://github.com/Infisical/agent-vault/blob/16ec8d5a5db38be9d2c77fe9c19c7fd7125246ba/internal/brokercore/substitution.go) · [netguard.go](https://github.com/Infisical/agent-vault/blob/16ec8d5a5db38be9d2c77fe9c19c7fd7125246ba/internal/netguard/netguard.go) · [crypto.go](https://github.com/Infisical/agent-vault/blob/16ec8d5a5db38be9d2c77fe9c19c7fd7125246ba/internal/crypto/crypto.go) · [ci.yml](https://github.com/Infisical/agent-vault/blob/16ec8d5a5db38be9d2c77fe9c19c7fd7125246ba/.github/workflows/ci.yml) |
