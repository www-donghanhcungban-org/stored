<!-- File sinh tự động bởi scripts/build_catalog_views.py; sửa data/projects.json hoặc data/taxonomy.json rồi chạy lại. -->

# quality-gate — Đánh giá, an toàn & chất lượng

[← Mục lục catalog](../README.md) · 97 hồ sơ.

## Test unit/integration (`unit-integration`, 17)

| Dự án | Repo | License | ★ | Bằng chứng | Mục | Tóm tắt |
|---|---|---|---|---|---|---|
| [Jest](../../30-software-testing-quality/README.md#anhkysuai-jestjs-jest) | `jestjs/jest` | MIT | 45.486 | đọc tài liệu 2026-11-23 | 30 | Bộ chạy kiểm thử JavaScript với matcher, watch mode và snapshot. |
| [Testify](../../30-software-testing-quality/README.md#anhkysuai-stretchr-testify) | `stretchr/testify` | MIT | 26.261 | đọc mã 2026-11-23 | 30 | Bộ assertion, mock và test suite cho Go. |
| [Mocha](../../30-software-testing-quality/README.md#anhkysuai-mochajs-mocha) | `mochajs/mocha` | MIT | 22.908 | đọc tài liệu 2026-11-23 | 30 | Test framework JavaScript cho Node.js và browser. |
| [jsdom](../../30-software-testing-quality/README.md#anhkysuai-jsdom-jsdom) | `jsdom/jsdom` | MIT; dữ liệu và thuật toán kèm theo có thông báo W3C và Unicode | 21.763 | đọc tài liệu 2026-11-23 | 30 | Mô phỏng nhiều API DOM và HTML trong Node.js để kiểm thử logic giao diện hoặc phân tích trang. |
| [Catch2](../../30-software-testing-quality/README.md#anhkysuai-catchorg-catch2) | `catchorg/Catch2` | BSL-1.0 | 21.590 | đọc tài liệu 2026-11-23 | 30 | Framework unit test C++ với assertion tự nhiên, section chia sẻ setup, macro BDD và microbenchmark cơ bản. |
| [AVA](../../30-software-testing-quality/README.md#anhkysuai-avajs-ava) | `avajs/ava` | MIT | 20.825 | đọc tài liệu 2026-11-23 | 30 | Test runner Node.js với cú pháp ngắn, assertion chi tiết và chạy đồng thời các test độc lập. |
| [keploy](../../30-software-testing-quality/README.md#chuyen-keploy) | `keploy/keploy` | Apache License 2.0 | 19.881 | đọc tài liệu 2026-11-18 | 30 | Công cụ kiểm thử API và tích hợp, ghi lại lưu lượng thật (API, truy vấn DB, sự kiện streaming) bằng eBPF rồi phát lại thành test và mock. |
| [OSS-Fuzz](../../30-software-testing-quality/README.md#nt-google-oss-fuzz) | `google/oss-fuzz` | Apache-2.0 | 12.982 | đọc mã 2026-11-23 | 30 | Dịch vụ fuzz liên tục do Google vận hành cho dự án mã nguồn mở được nhận, cũng là kho định dạng chuẩn: mỗi dự án có Dockerfile, build.sh và project.yaml (engine, sanitiz… |
| [Toxiproxy](../../30-software-testing-quality/README.md#nt-shopify-toxiproxy) | `Shopify/toxiproxy` | MIT | 12.543 | đọc mã 2026-11-23 | 30 | Proxy TCP viết bằng Go để mô phỏng lỗi mạng trong test tích hợp: tạo proxy qua API HTTP hoặc client rồi gắn các toxic (latency, bandwidth, timeout, reset_peer, slicer, l… |
| [Great Expectations (GX Core)](../../15-ai-for-data/README.md#ch-great-expectations-gx-core) | `fivetran/great_expectations` | Apache-2.0 | 11.945 | đọc tài liệu 2026-11-23 | 15 | Unit test cho dữ liệu (Expectation + Checkpoint), v1.24.1; |
| [StrykerJS](../../13-dev-stack-devops/README.md#ch-strykerjs) | `stryker-mutator/stryker-js` | Apache-2.0 | 3.306 | đọc tài liệu 2026-11-23 | 13 | Mutation testing JS/TS; |
| [Soda Core](../../15-ai-for-data/README.md#ch-soda-core) | `sodadata/soda-core` | Elastic-2.0 (ELv2; pyproject khai "Proprietary") | 2.463 | đọc tài liệu 2026-11-23 | 15 | Data contract YAML, 50+ check, CLI/Python trên Postgres/Snowflake/BigQuery/DuckDB…; |
| [Hypothesis](../../30-software-testing-quality/README.md#hypothesis-factory) | `HypothesisWorks/hypothesis` | MPL-2.0 | — | đọc mã 2026-11-04 | 30 | Property-based Python và thu nhỏ phản ví dụ; |
| [pytest](../../30-software-testing-quality/README.md#pytest-factory) | `pytest-dev/pytest` | MIT | — | đọc mã 2026-11-04 | 30 | Runner Python fixture/parametrization; |
| [Storybook Vitest addon](../../06-ui-ux-design/README.md#storybook-addon-vitest-factory) | `storybookjs/storybook` | MIT | — | đọc mã 2026-11-04 | 06 | Thực thể addon kiểm thử, khác Storybook thư viện; |
| [Testcontainers Python](../../30-software-testing-quality/README.md#testcontainers-python-factory) | `testcontainers/testcontainers-python` | Apache-2.0 | — | đọc mã 2026-11-04 | 30 | Dependency container thật và wait/cleanup; |
| [Vitest](../../30-software-testing-quality/README.md#vitest-factory) | `vitest-dev/vitest` | MIT | — | đọc mã 2026-11-04 | 30 | Runner JS/TS Vite Node/browser; |

## E2E & trình duyệt (`e2e-browser`, 6)

| Dự án | Repo | License | ★ | Bằng chứng | Mục | Tóm tắt |
|---|---|---|---|---|---|---|
| [Playwright](../../11-browser-computer-use-sandbox/README.md#playwright) | `microsoft/playwright` | Apache-2.0 | 99.090 | đọc mã 2026-11-02 | 11 | Runner/library gốc; |
| [Selenium](../../30-software-testing-quality/README.md#anhkysuai-seleniumhq-selenium) | `SeleniumHQ/selenium` | Apache-2.0 | 34.607 | đọc tài liệu 2026-11-23 | 30 | Hạ tầng tự động hóa trình duyệt theo W3C WebDriver. |
| [Appium](../../30-software-testing-quality/README.md#anhkysuai-appium-appium) | `appium/appium` | Apache-2.0 | 22.251 | đọc tài liệu 2026-11-23 | 30 | Framework tự động hóa kiểm thử ứng dụng native, hybrid, mobile web, desktop và thiết bị qua WebDriver. |
| [TestZeus Hercules](../../06-ui-ux-design/README.md#ux-testzeus-hercules) | `test-zeus-ai/testzeus-hercules` | AGPL-3.0-only | 1.231 | đọc mã 2026-11-23 | 06 | Engine QA mã nguồn mở: viết bước kiểm thử bằng ngôn ngữ tự nhiên, model đọc bước và quyết định, mã thực hiện hành động và kiểm kết quả trong Chromium thật, có CLI, UI cụ… |
| [Harness (user-test agent)](../../06-ui-ux-design/README.md#ux-awizemann-harness) | `awizemann/harness` | MIT | 366 | đọc mã 2026-11-23 | 06 | Ứng dụng macOS (alpha) cho agent LLM đóng vai người dùng thật với persona và mục tiêu, lái iOS Simulator, app macOS hoặc web (WKWebView) qua ảnh chụp màn hình có đánh số… |
| [WebQA Agent](../../06-ui-ux-design/README.md#ux-webqa-agent) | `MigoXLab/webqa-agent` | Apache-2.0 | 240 | đọc mã 2026-11-23 | 06 | Agent kiểm thử web đa phương thức với ba chế độ (Flash qua chrome-devtools-mcp, Standard Generate, Run YAML) và MCP server cho Cursor/Claude Code. |

## Visual regression & accessibility (`visual-a11y`, 15)

| Dự án | Repo | License | ★ | Bằng chứng | Mục | Tóm tắt |
|---|---|---|---|---|---|---|
| [Responsively App](../../30-software-testing-quality/README.md#anhkysuai-responsively-org-responsively-app) | `responsively-org/responsively-app` | AGPL-3.0 | 25.577 | đọc tài liệu 2026-11-23 | 30 | Browser Electron hiển thị nhiều viewport để kiểm tra responsive. |
| [axe-core](../../06-ui-ux-design/README.md#ch-axe-core) | `dequelabs/axe-core` | MPL-2.0 | 7.874 | đọc tài liệu 2026-11-23 | 06 | Engine a11y runtime: 105 luật WCAG 2.0/2.1/2.2 A–AAA + best practice, v4.14.0; |
| [pixelmatch](../../06-ui-ux-design/README.md#ch-pixelmatch) | `mapbox/pixelmatch` | ISC | 7.028 | đọc tài liệu 2026-11-23 | 06 | So ảnh pixel ~600 dòng, không phụ thuộc, OKLab + HyAB, dò khử răng cưa; |
| [VMAF](../../19-agentic-video-media/README.md#ch-vmaf) | `Netflix/vmaf` | BSD-2-Clause-Patent | 5.655 | đọc tài liệu 2026-11-23 | 19 | Chỉ số chất lượng video cảm nhận + PSNR/SSIM/MS-SSIM/CIEDE2000/CAMBI; |
| [Pa11y](../../06-ui-ux-design/README.md#ux-pa11y) | `pa11y/pa11y` | LGPL-3.0-only | 4.603 | đọc mã 2026-11-23 | 06 | CLI/thư viện Node chạy Chromium (Puppeteer) rồi áp HTML_CodeSniffer (mặc định) và/hoặc axe-core lên trang, in lỗi dạng error/warning/notice và thoát mã 2 nếu có lỗi vượt… |
| [eslint-plugin-jsx-a11y](../../06-ui-ux-design/README.md#ch-eslint-plugin-jsx-a11y) | `jsx-eslint/eslint-plugin-jsx-a11y` | MIT | 3.631 | đọc tài liệu 2026-11-23 | 06 | 39 luật a11y tĩnh cho JSX; |
| [AIPex: skill wcag22-a11y-audit](../../06-ui-ux-design/README.md#ux-aipex-wcag22-a11y-audit) | `AIPexStudio/AIPex` | MIT | 1.284 | đọc tài liệu 2026-11-23 | 06 | Skill tích hợp sẵn của tiện ích trình duyệt AIPex: audit trang đang mở theo 8 tiêu chí (1.1.1, 1.4.3, 1.4.11, 2.1.1, 2.1.2, 2.4.3, 2.4.7, 4.1.2), mỗi tiêu chí có bước ki… |
| [Argos](../../06-ui-ux-design/README.md#ch-argos) | `argos-ci/argos` | MIT | 666 | đọc tài liệu 2026-11-23 | 06 | Nền tảng visual testing review ảnh chụp trong PR (Playwright/Storybook/Cypress), so ảnh bằng odiff-bin; |
| [Pa11y CI](../../06-ui-ux-design/README.md#ux-pa11y-ci) | `pa11y/pa11y-ci` | LGPL-3.0-only | 649 | đọc tài liệu 2026-11-23 | 06 | Bộ chạy Pa11y trên danh sách URL, file cục bộ (glob) hoặc sitemap, dùng một trình duyệt chung, in kết quả cuối và JSON để chặn CI. |
| [Guidepup](../../06-ui-ux-design/README.md#ux-guidepup) | `guidepup/guidepup` | MIT | 604 | đọc mã 2026-11-23 | 06 | Thư viện TypeScript điều khiển screen reader thật (NVDA trên Windows, Orca trên Linux, VoiceOver trên macOS) qua một API chung (`next`, `nextHeading`, `act`, `spokenPhra… |
| [ffmpeg-quality-metrics](../../19-agentic-video-media/README.md#ch-ffmpeg-quality-metrics) | `slhck/ffmpeg-quality-metrics` | MIT | 566 | đọc tài liệu 2026-11-23 | 19 | CLI/Python bọc ffmpeg tính PSNR/SSIM/VIF/MSAD/VMAF từng frame + thống kê + GUI; |
| [HappyHands](../../06-ui-ux-design/README.md#ux-happyhands) | `ShuaiMXu/happyhands` | MIT (Copyright 2026 HappyHands contributors; kèm vendor MIT/Apache-2.0 trong THIRD_PARTY_NOTICES.md) | 537 | đọc tài liệu 2026-11-23 | 06 | Harness cục bộ cho coding agent: chụp trang thật ở nhiều viewport/trạng thái, chẩn đoán, sửa trong git worktree cô lập, chụp lại và nhờ reviewer độc lập chấm trên bằng c… |
| [Happo (client)](../../06-ui-ux-design/README.md#ux-happo) | `happo/happo` | — | 515 | đọc mã 2026-11-23 | 06 | Thư viện/CLI client của dịch vụ happo.io: chụp snapshot DOM và tài sản (Storybook, Cypress, Playwright, custom), tải lên SaaS để so ảnh trên Chrome/Firefox/Safari/iOS và… |
| [Accessibility Agents (Community-Access)](../../06-ui-ux-design/README.md#ux-accessibility-agents-community-access) | `Community-Access/accessibility-agents` | MIT | 456 | đọc mã 2026-11-23 | 06 | Gói 113 skill WCAG 2.2 AA (6 router + chuyên gia + kb-\*) chạy trên nhiều client, kèm hook chặn sửa file UI cho đến khi `accessibility-lead` hoàn tất và MCP server 39 too… |
| [a11y-specialist-skills (masuP9)](../../06-ui-ux-design/README.md#ux-a11y-specialist-skills) | `masup9/a11y-specialist-skills` | MIT | 61 | đọc mã 2026-11-23 | 06 | Sáu skill WCAG 2.2 A/AA cho Claude Code và Codex, nổi bật là `auditing-wcag`: quy trình 6 bước gán Pass/Fail/NT/NA cho từng tiêu chí kèm bằng chứng, chạy CLI `@a11y-skil… |

## Phân tích tĩnh & lint (`static-analysis`, 22)

| Dự án | Repo | License | ★ | Bằng chứng | Mục | Tóm tắt |
|---|---|---|---|---|---|---|
| [Prettier](../../30-software-testing-quality/README.md#anhkysuai-prettier-prettier) | `prettier/prettier` | MIT | 52.449 | đọc tài liệu 2026-11-23 | 30 | Formatter phân tích cú pháp rồi in lại mã với quy tắc thống nhất. |
| [ruff](../../13-dev-stack-devops/README.md#ch-ruff) | `astral-sh/ruff` | MIT | 50.369 | đọc tài liệu 2026-11-23 | 13 | Linter/formatter Python (Astral); |
| [Black](../../30-software-testing-quality/README.md#anhkysuai-psf-black) | `psf/black` | MIT | 42.210 | đọc tài liệu 2026-11-23 | 30 | Formatter Python theo bộ quy tắc cố định để giảm tranh luận định dạng. |
| [ShellCheck](../../30-software-testing-quality/README.md#anhkysuai-koalaman-shellcheck) | `koalaman/shellcheck` | GPL-3.0 | 40.374 | đọc tài liệu 2026-11-23 | 30 | Phân tích tĩnh script bash/sh để tìm lỗi cú pháp, quoting và portability. |
| [ESLint](../../30-software-testing-quality/README.md#anhkysuai-eslint-eslint) | `eslint/eslint` | MIT | 27.644 | đọc tài liệu 2026-11-23 | 30 | Phân tích mẫu lỗi và quy tắc trong mã JavaScript theo AST. |
| [Biome](../../13-dev-stack-devops/README.md#ch-biome) | `biomejs/biome` | MIT OR Apache-2.0 (hai file LICENSE-MIT và LICENSE-APACHE) | 26.026 | đọc tài liệu 2026-11-23 | 13 | Format + lint JS/TS, 500+ rule; |
| [oxlint](../../13-dev-stack-devops/README.md#ch-oxlint) | `oxc-project/oxc` | MIT | 23.285 | đọc tài liệu 2026-11-23 | 13 | Linter JS/TS viết bằng Rust; |
| [Mypy](../../30-software-testing-quality/README.md#anhkysuai-python-mypy) | `python/mypy` | MIT cho mypy/mypyc; một số tệp và thành phần có PSF/BSD hoặc thông báo riêng | 20.735 | đọc tài liệu 2026-11-23 | 30 | Bộ kiểm kiểu tĩnh cho Python, cho phép thêm type hint từng phần mà không đổi cách chương trình chạy. |
| [pyright](../../13-dev-stack-devops/README.md#ch-pyright) | `microsoft/pyright` | MIT | 15.720 | đọc tài liệu 2026-11-23 | 13 | Type checker Python; |
| [react-doctor](../../30-software-testing-quality/README.md#chuyen-react-doctor) | `millionco/react-doctor` | Modified MIT License | 15.154 | đọc tài liệu 2026-11-18 | 30 | Công cụ quét tĩnh có tính tất định cho dự án React, báo lỗi về state/effect, hiệu năng, kiến trúc, bảo mật, a11y và khả năng bảo trì. |
| [knip](../../13-dev-stack-devops/README.md#ch-knip) | `webpro-nl/knip` | ISC | 12.560 | đọc tài liệu 2026-11-23 | 13 | Tìm file/export/dependency chết; |
| [Stylelint](../../06-ui-ux-design/README.md#ch-stylelint) | `stylelint/stylelint` | MIT | 11.557 | đọc tài liệu 2026-11-23 | 06 | 154 luật lint CSS (color-no-hex, declaration-property-value-allowed-list, no-unknown-custom-properties) để cấm giá trị ngoài token; |
| [SQLFluff](../../15-ai-for-data/README.md#ch-sqlfluff) | `sqlfluff/sqlfluff` | MIT | 10.035 | đọc tài liệu 2026-11-23 | 15 | Linter + auto-fix SQL, 28 file dialect, templater Jinja/dbt, lõi Rust sqlfluffrs; |
| [zizmor](../../31-software-supply-chain-security/README.md#ch-zizmor) | `zizmorcore/zizmor` | MIT | 7.126 | đọc tài liệu 2026-11-23 | 31 | Phân tích tĩnh bảo mật GitHub Actions, 41 audit, SARIF, offline/online; |
| [jscpd](../../13-dev-stack-devops/README.md#ch-jscpd) | `kucherenko/jscpd` | MIT | 6.472 | đọc tài liệu 2026-11-23 | 13 | Phát hiện code trùng lặp; |
| [actionlint](../../13-dev-stack-devops/README.md#ch-actionlint) | `rhysd/actionlint` | MIT | 4.371 | đọc tài liệu 2026-11-23 | 13 | Lint workflow GitHub Actions: kiểm kiểu ${{ }}, shellcheck/pyflakes; |
| [@shadcn/lint](../../06-ui-ux-design/README.md#ch-shadcn-lint) | `shadcn-ui/lint` | MIT | 3.455 | đọc tài liệu 2026-11-23 | 06 | 6 luật ESLint/Oxlint cho design system Tailwind v4, thông báo lỗi viết cho agent; |
| [Shadscan](../../06-ui-ux-design/README.md#ux-shadscan) | `TheOrcDev/shadscan` | MIT (Copyright 2026 TheOrcDev) | 562 | đọc mã 2026-11-23 | 06 | CLI audit tĩnh tất định cho app React/shadcn: 62 luật, 6 hạng mục, điểm 0-100 và chia báo cáo thành Fixes/Decisions/Advisories/Not applicable, kèm lệnh --check-ui đo trà… |
| [squirrelscan](../../06-ui-ux-design/README.md#ux-squirrelscan) | `squirrelscan/squirrelscan` | MIT (Copyright 2026 squirrelscan; tên và logo theo TRADEMARKS.md) | 334 | đọc mã 2026-11-23 | 06 | CLI/Bun audit website 350+ luật trong 22 nhóm (SEO, a11y 63 luật, mobile, content, performance, security, agent experience...), điểm 0-100 theo trọng số luật và xuất báo… |
| [crapper / dryer / mutator (Uncle Bob)](../../20-claude-plugins-ecosystem/README.md#ch-crapper-dryer-mutator-uncle-bob) | `unclebob/crapper` | 0BSD | 243 | đọc tài liệu 2026-11-23 | 20 | Bộ cổng chất lượng Python của Robert C. |
| [driftlint](../../20-claude-plugins-ecosystem/README.md#nt-driftlint) | `alifurkangokce/driftlint` | MIT | 61 | đọc mã 2026-11-23 | 20 | CLI Node/TypeScript (không phụ thuộc runtime) tìm điều CLAUDE.md, AGENTS.md, skill, rule Cursor khẳng định mà mã không còn ủng hộ: đường dẫn chết, lệnh npm/make đã xóa,… |
| [dependency-cruiser](../../29-software-architecture-api-contracts/README.md#dependency-cruiser-architecture-gates) | `sverweij/dependency-cruiser` | MIT | — | đọc mã 2026-11-04 | 29 | Kiểm graph/rule dependency JS/TS; |

## Eval skill/agent (`ai-skill-eval`, 6)

| Dự án | Repo | License | ★ | Bằng chứng | Mục | Tóm tắt |
|---|---|---|---|---|---|---|
| [NVIDIA SkillEvaluator](../../20-claude-plugins-ecosystem/README.md#ch-nvidia-skillevaluator) | `NVIDIA/SkillEvaluator` | Apache-2.0 | 4.442 | đọc tài liệu 2026-11-23 | 20 | Eval skill 3 tầng: chất lượng + scanner, trùng lặp, chạy agent có/không skill; |
| [SkillsBench](../../20-claude-plugins-ecosystem/README.md#xlsx-2026-11-23-skillsbench) | `benchflow-ai/skillsbench` | Apache-2.0 | 1.936 | đọc mã 2026-11-23 | 20 | Benchmark skill của agent: task.md + Docker + oracle + verifier (reward 1/0 từ pytest, phụ thuộc ghim); |
| [agent-skills-eval](../../20-claude-plugins-ecosystem/README.md#ch-agent-skills-eval) | `darkrishabh/agent-skills-eval` | MIT | 821 | đọc tài liệu 2026-11-23 | 20 | Test runner skill with_skill vs without_skill có judge, báo cáo HTML; |
| [skillgrade](../../20-claude-plugins-ecosystem/README.md#ch-skillgrade) | `mgechev/skillgrade` | MIT | 737 | đọc tài liệu 2026-11-23 | 20 | Unit test cho skill: eval.yaml, chạy nhiều harness trong Docker, grader tất định/LLM/người, --ci --threshold, JUnit; |
| [agnix](../../20-claude-plugins-ecosystem/README.md#factory-skill-admission-2026-11-04) | `agent-sh/agnix` | MIT OR Apache-2.0 | 465 | đọc mã 2026-11-04 | 20 | Linter 757 luật cho CLAUDE.md, SKILL.md, hooks, MCP, plugin của nhiều harness; |
| [Coder Eval](../../20-claude-plugins-ecosystem/README.md#ch-coder-eval) | `UiPath/coder_eval` | Apache-2.0 | 159 | đọc tài liệu 2026-11-23 | 20 | Eval coding agent trong sandbox, kiểm skill_triggered theo harness, A/B, GitHub Action; |

## Hợp đồng API & schema (`api-contract`, 11)

| Dự án | Repo | License | ★ | Bằng chứng | Mục | Tóm tắt |
|---|---|---|---|---|---|---|
| [Bruno](../../30-software-testing-quality/README.md#anhkysuai-usebruno-bruno) | `usebruno/bruno` | MIT cho code; logo OpenMoji CC-BY-SA-4.0 | 48.512 | đọc tài liệu 2026-11-23 | 30 | API client desktop và CLI lưu collection bằng file cục bộ để quản lý bằng Git. |
| [Zod](../../30-software-testing-quality/README.md#anhkysuai-colinhacks-zod) | `colinhacks/zod` | MIT | 44.394 | đọc mã 2026-11-23 | 30 | Schema validation JavaScript/TypeScript đồng thời suy luận kiểu dữ liệu. |
| [Insomnia](../../30-software-testing-quality/README.md#anhkysuai-kong-insomnia) | `Kong/insomnia` | Apache-2.0 cho mã repo; tính năng dịch vụ theo gói riêng | 40.183 | đọc tài liệu 2026-11-23 | 30 | API client và bộ công cụ thiết kế, chạy thử REST, GraphQL, gRPC và WebSocket. |
| [Pydantic](../../30-software-testing-quality/README.md#anhkysuai-pydantic-pydantic) | `pydantic/pydantic` | MIT | 29.634 | đọc tài liệu 2026-11-23 | 30 | Validation dữ liệu Python qua type hint và model. |
| [Spectral](../../29-software-architecture-api-contracts/README.md#ch-spectral) | `stoplightio/spectral` | Apache-2.0 | 3.263 | đọc tài liệu 2026-11-23 | 29 | Linter JSON/YAML, ruleset sẵn OpenAPI/AsyncAPI/Arazzo v1 (hỗ trợ Arazzo 1.1 chưa xác minh); |
| [Microcks](../../29-software-architecture-api-contracts/README.md#nt-microcks) | `microcks/microcks` | Apache-2.0 | 2.093 | đọc mã 2026-11-23 | 29 | Nền tảng mock và test hợp đồng đa giao thức từ cùng một tài sản đặc tả. |
| [vacuum (OpenAPI, AsyncAPI, Arazzo linter)](../../29-software-architecture-api-contracts/README.md#nt-vacuum) | `daveshanley/vacuum` | MIT | 1.149 | đọc mã 2026-11-23 | 29 | Linter Go rất nhanh cho OpenAPI, AsyncAPI, JSON Schema và Arazzo; |
| [Data Contract CLI](../../15-ai-for-data/README.md#nt-datacontract-cli) | `datacontract/datacontract-cli` | MIT | 1.116 | đọc mã 2026-11-23 | 15 | CLI Python MIT lint và test dữ liệu thật theo Open Data Contract Standard, có `ci --fail-on` và xuất JUnit. |
| [OpenTelemetry Weaver](../../07-eval-observability/README.md#ch-opentelemetry-weaver) | `open-telemetry/weaver` | Apache-2.0 | 537 | đọc tài liệu 2026-11-23 | 07 | registry check/live-check OTLP so với semconv, GitHub Action fail theo severity; |
| [oasdiff](../../29-software-architecture-api-contracts/README.md#oasdiff-compatibility-gates) | `oasdiff/oasdiff` | Apache-2.0 | — | đọc mã 2026-11-04 | 29 | Breaking diff OpenAPI base/revision; |
| [Schemathesis](../../30-software-testing-quality/README.md#schemathesis-factory) | `schemathesis/schemathesis` | MIT | — | đọc mã 2026-11-04 | 30 | Schema-based OpenAPI/GraphQL/gRPC testing và stateful sequences; |

## Hiệu năng & tải (`perf-load`, 13)

| Dự án | Repo | License | ★ | Bằng chứng | Mục | Tóm tắt |
|---|---|---|---|---|---|---|
| [Lighthouse](../../30-software-testing-quality/README.md#anhkysuai-googlechrome-lighthouse) | `GoogleChrome/lighthouse` | Apache-2.0 | 31.193 | đọc tài liệu 2026-11-23 | 30 | Audit trang web về hiệu năng và các thực hành phát triển. |
| [LeakCanary](../../30-software-testing-quality/README.md#anhkysuai-square-leakcanary) | `square/leakcanary` | Apache-2.0 | 30.009 | đọc tài liệu 2026-11-23 | 30 | Phát hiện rò rỉ bộ nhớ trong ứng dụng Android. |
| [Hyperfine](../../30-software-testing-quality/README.md#anhkysuai-sharkdp-hyperfine) | `sharkdp/hyperfine` | MIT OR Apache-2.0 | 29.338 | đọc tài liệu 2026-11-23 | 30 | Benchmark lệnh qua nhiều lần chạy và xuất thống kê. |
| [Locust](../../30-software-testing-quality/README.md#anhkysuai-locustio-locust) | `locustio/locust` | MIT | 28.307 | đọc tài liệu 2026-11-23 | 30 | Công cụ viết kịch bản kiểm tải bằng Python cho HTTP và giao thức mở rộng. |
| [Vegeta](../../30-software-testing-quality/README.md#nt-vegeta) | `tsenart/vegeta` | MIT | 25.256 | đọc mã 2026-11-23 | 30 | Công cụ tải HTTP bằng Go, điều khiển theo tốc độ cố định, dùng được như dòng lệnh hoặc thư viện. |
| [React Scan](../../30-software-testing-quality/README.md#anhkysuai-aidenybai-react-scan) | `aidenybai/react-scan` | MIT | 21.882 | đọc tài liệu 2026-11-23 | 30 | Công cụ hiển thị component và điểm nóng hiệu năng khi quan sát ứng dụng React đang chạy. |
| [oha](../../30-software-testing-quality/README.md#nt-oha) | `hatoo/oha` | MIT | 10.722 | đọc mã 2026-11-23 | 30 | Bộ sinh tải HTTP Rust có TUI, đọc nhanh, ghi kết quả vào SQLite. |
| [web-vitals](../../30-software-testing-quality/README.md#ch-web-vitals) | `GoogleChrome/web-vitals` | Apache-2.0 | 8.700 | đọc tài liệu 2026-11-23 | 30 | Thư viện chính thức đo LCP/INP/CLS ở người dùng thật, build attribution chỉ ra nguyên nhân; |
| [Lighthouse CI](../../13-dev-stack-devops/README.md#ch-lighthouse-ci) | `GoogleChrome/lighthouse-ci` | Apache-2.0 | 7.122 | đọc tài liệu 2026-11-23 | 13 | Commit cuối 26/6/2025 (đứng yên); |
| [Web Quality Skills](../../06-ui-ux-design/README.md#ch-web-quality-skills) | `addyosmani/web-quality-skills` | MIT | 3.122 | đọc tài liệu 2026-11-23 | 06 | 6 Agent Skills đo-trước (audit, performance, Core Web Vitals, a11y WCAG 2.2, SEO, best practices); |
| [GuideLLM](../../10-local-llm-rag-memory/README.md#nt-guidellm) | `vllm-project/guidellm` | Apache-2.0 | 1.804 | đọc mã 2026-11-23 | 10 | Công cụ benchmark tải cho endpoint LLM, ra phân phối TTFT/ITL và tìm mức tải an toàn theo SLO. |
| [AIPerf](../../10-local-llm-rag-memory/README.md#aiperf) | `ai-dynamo/aiperf` | Apache-2.0 | 842 | đọc mã 2026-11-02 | 10 | Load generator đo TTFT/ITL/throughput; |
| [Grafana k6](../../30-software-testing-quality/README.md#k6-factory) | `grafana/k6` | AGPL-3.0 | — | đọc mã 2026-11-04 | 30 | Load test runtime Go/JS; |

## Cổng phát hành & review (`release-gate`, 7)

| Dự án | Repo | License | ★ | Bằng chứng | Mục | Tóm tắt |
|---|---|---|---|---|---|---|
| [Renovate](../../13-dev-stack-devops/README.md#ch-renovate) | `renovatebot/renovate` | AGPL-3.0 | 22.974 | đọc tài liệu 2026-11-23 | 13 | Cập nhật dependency 90+ trình quản lý gói; |
| [cz-cli](../../13-dev-stack-devops/README.md#chuyen-cz-cli) | `commitizen/cz-cli` | MIT | 17.503 | đọc tài liệu 2026-11-18 | 13 | Công cụ dòng lệnh nhắc người dùng điền các trường bắt buộc khi commit để thông điệp commit theo quy ước (ví dụ conventional-changelog). |
| [pre-commit](../../13-dev-stack-devops/README.md#ch-pre-commit) | `pre-commit/pre-commit` | MIT | 15.674 | đọc tài liệu 2026-11-23 | 13 | Hook git đa ngôn ngữ; |
| [reviewdog](../../13-dev-stack-devops/README.md#ch-reviewdog) | `reviewdog/reviewdog` | MIT | 9.712 | đọc tài liệu 2026-11-23 | 13 | Kết quả linter → comment review PR; |
| [release-please](../../13-dev-stack-devops/README.md#ch-release-please) | `googleapis/release-please` | Apache-2.0 | 7.715 | đọc tài liệu 2026-11-23 | 13 | Conventional commits → changelog + release PR; |
| [OpenSSF Best Practices Badge](../../09-engineering-checklists/README.md#ch-openssf-best-practices-badge) | `ossf/best-practices-badge` | MIT | 1.377 | đọc tài liệu 2026-11-23 | 09 | App bestpractices.dev: tiêu chí Baseline 1–3 (64 control sinh từ OSPS 2026-08-28) + Metal passing/silver/gold; |
| [Sloth](../../33-reliability-observability-operations/README.md#sloth-slo-generator) | `slok/sloth` | Apache-2.0 | — | đọc mã 2026-11-04 | 33 | SLO-to-Prometheus rules; |
