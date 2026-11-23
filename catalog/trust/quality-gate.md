<!-- File sinh tự động bởi scripts/build_catalog_views.py; sửa data/projects.json hoặc data/taxonomy.json rồi chạy lại. -->

# quality-gate — Đánh giá, an toàn & chất lượng

[← Mục lục catalog](../README.md) · 75 hồ sơ.

## Test unit/integration (`unit-integration`, 15)

| Dự án | Repo | License | ★ | Bằng chứng | Mục | Tóm tắt |
|---|---|---|---|---|---|---|
| [Jest](../../30-software-testing-quality/README.md#anhkysuai-jestjs-jest) | `jestjs/jest` | MIT | 45.486 | đọc tài liệu 2026-11-23 | 30 | Bộ chạy kiểm thử JavaScript với matcher, watch mode và snapshot. |
| [Testify](../../30-software-testing-quality/README.md#anhkysuai-stretchr-testify) | `stretchr/testify` | MIT | 26.261 | đọc mã 2026-11-23 | 30 | Bộ assertion, mock và test suite cho Go. |
| [Mocha](../../30-software-testing-quality/README.md#anhkysuai-mochajs-mocha) | `mochajs/mocha` | MIT | 22.908 | đọc tài liệu 2026-11-23 | 30 | Test framework JavaScript cho Node.js và browser. |
| [jsdom](../../30-software-testing-quality/README.md#anhkysuai-jsdom-jsdom) | `jsdom/jsdom` | MIT; dữ liệu và thuật toán kèm theo có thông báo W3C và Unicode | 21.763 | đọc tài liệu 2026-11-23 | 30 | Mô phỏng nhiều API DOM và HTML trong Node.js để kiểm thử logic giao diện hoặc phân tích trang. |
| [Catch2](../../30-software-testing-quality/README.md#anhkysuai-catchorg-catch2) | `catchorg/Catch2` | BSL-1.0 | 21.590 | đọc tài liệu 2026-11-23 | 30 | Framework unit test C++ với assertion tự nhiên, section chia sẻ setup, macro BDD và microbenchmark cơ bản. |
| [AVA](../../30-software-testing-quality/README.md#anhkysuai-avajs-ava) | `avajs/ava` | MIT | 20.825 | đọc tài liệu 2026-11-23 | 30 | Test runner Node.js với cú pháp ngắn, assertion chi tiết và chạy đồng thời các test độc lập. |
| [keploy](../../30-software-testing-quality/README.md#chuyen-keploy) | `keploy/keploy` | Apache License 2.0 | 19.881 | đọc tài liệu 2026-11-18 | 30 | Công cụ kiểm thử API và tích hợp, ghi lại lưu lượng thật (API, truy vấn DB, sự kiện streaming) bằng eBPF rồi phát lại thành test và mock. |
| [Great Expectations (GX Core)](../../15-ai-for-data/README.md) | `fivetran/great_expectations` | Apache-2.0 | 11.913 | chưa chuẩn hóa | 15 | Unit test cho dữ liệu (Expectation + Checkpoint), v1.24.1; |
| [StrykerJS](../../13-dev-stack-devops/README.md) | `stryker-mutator/stryker-js` | Apache-2.0 | 3.306 | chưa chuẩn hóa | 13 | Mutation testing JS/TS; |
| [Soda Core](../../15-ai-for-data/README.md) | `sodadata/soda-core` | Elastic-2.0 (ELv2; GitHub báo NOASSERTION) | 2.463 | chưa chuẩn hóa | 15 | Data contract YAML, 50+ check, CLI/Python trên Postgres/Snowflake/BigQuery/DuckDB…; |
| [Hypothesis](../../30-software-testing-quality/README.md#hypothesis-factory) | `HypothesisWorks/hypothesis` | MPL-2.0 | — | đọc mã 2026-11-04 | 30 | Property-based Python và thu nhỏ phản ví dụ; |
| [pytest](../../30-software-testing-quality/README.md#pytest-factory) | `pytest-dev/pytest` | MIT | — | đọc mã 2026-11-04 | 30 | Runner Python fixture/parametrization; |
| [Storybook Vitest addon](../../06-ui-ux-design/README.md#storybook-addon-vitest-factory) | `storybookjs/storybook` | MIT | — | đọc mã 2026-11-04 | 06 | Thực thể addon kiểm thử, khác Storybook thư viện; |
| [Testcontainers Python](../../30-software-testing-quality/README.md#testcontainers-python-factory) | `testcontainers/testcontainers-python` | Apache-2.0 | — | đọc mã 2026-11-04 | 30 | Dependency container thật và wait/cleanup; |
| [Vitest](../../30-software-testing-quality/README.md#vitest-factory) | `vitest-dev/vitest` | MIT | — | đọc mã 2026-11-04 | 30 | Runner JS/TS Vite Node/browser; |

## E2E & trình duyệt (`e2e-browser`, 3)

| Dự án | Repo | License | ★ | Bằng chứng | Mục | Tóm tắt |
|---|---|---|---|---|---|---|
| [Playwright](../../11-browser-computer-use-sandbox/README.md#playwright) | `microsoft/playwright` | Apache-2.0 | 99.090 | đọc mã 2026-11-02 | 11 | Runner/library gốc; |
| [Selenium](../../30-software-testing-quality/README.md#anhkysuai-seleniumhq-selenium) | `SeleniumHQ/selenium` | Apache-2.0 | 34.607 | đọc tài liệu 2026-11-23 | 30 | Hạ tầng tự động hóa trình duyệt theo W3C WebDriver. |
| [Appium](../../30-software-testing-quality/README.md#anhkysuai-appium-appium) | `appium/appium` | Apache-2.0 | 22.251 | đọc tài liệu 2026-11-23 | 30 | Framework tự động hóa kiểm thử ứng dụng native, hybrid, mobile web, desktop và thiết bị qua WebDriver. |

## Visual regression & accessibility (`visual-a11y`, 7)

| Dự án | Repo | License | ★ | Bằng chứng | Mục | Tóm tắt |
|---|---|---|---|---|---|---|
| [Responsively App](../../30-software-testing-quality/README.md#anhkysuai-responsively-org-responsively-app) | `responsively-org/responsively-app` | AGPL-3.0 | 25.577 | đọc tài liệu 2026-11-23 | 30 | Browser Electron hiển thị nhiều viewport để kiểm tra responsive. |
| [axe-core](../../06-ui-ux-design/README.md) | `dequelabs/axe-core` | MPL-2.0 | 7.738 | chưa chuẩn hóa | 06 | Engine a11y runtime: 105 luật WCAG 2.0/2.1/2.2 A–AAA + best practice, v4.14.0; |
| [pixelmatch](../../06-ui-ux-design/README.md) | `mapbox/pixelmatch` | ISC | 7.007 | chưa chuẩn hóa | 06 | So ảnh pixel ~600 dòng, không phụ thuộc, OKLab + HyAB, dò khử răng cưa; |
| [VMAF](../../19-agentic-video-media/README.md) | `Netflix/vmaf` | BSD-2-Clause-Patent | 5.578 | chưa chuẩn hóa | 19 | Chỉ số chất lượng video cảm nhận + PSNR/SSIM/MS-SSIM/CIEDE2000/CAMBI; |
| [eslint-plugin-jsx-a11y](../../06-ui-ux-design/README.md) | `jsx-eslint/eslint-plugin-jsx-a11y` | MIT | 3.633 | chưa chuẩn hóa | 06 | 39 luật a11y tĩnh cho JSX; |
| [Argos](../../06-ui-ux-design/README.md) | `argos-ci/argos` | MIT | 656 | chưa chuẩn hóa | 06 | Nền tảng visual testing review ảnh chụp trong PR (Playwright/Storybook/Cypress), so ảnh bằng odiff-bin; |
| [ffmpeg-quality-metrics](../../19-agentic-video-media/README.md) | `slhck/ffmpeg-quality-metrics` | MIT | 561 | chưa chuẩn hóa | 19 | CLI/Python bọc ffmpeg tính PSNR/SSIM/VIF/MSAD/VMAF từng frame + thống kê + GUI; |

## Phân tích tĩnh & lint (`static-analysis`, 19)

| Dự án | Repo | License | ★ | Bằng chứng | Mục | Tóm tắt |
|---|---|---|---|---|---|---|
| [Prettier](../../30-software-testing-quality/README.md#anhkysuai-prettier-prettier) | `prettier/prettier` | MIT | 52.449 | đọc tài liệu 2026-11-23 | 30 | Formatter phân tích cú pháp rồi in lại mã với quy tắc thống nhất. |
| [ruff](../../13-dev-stack-devops/README.md) | `astral-sh/ruff` | MIT | 50.369 | chưa chuẩn hóa | 13 | Linter/formatter Python (Astral); |
| [Black](../../30-software-testing-quality/README.md#anhkysuai-psf-black) | `psf/black` | MIT | 42.210 | đọc tài liệu 2026-11-23 | 30 | Formatter Python theo bộ quy tắc cố định để giảm tranh luận định dạng. |
| [ShellCheck](../../30-software-testing-quality/README.md#anhkysuai-koalaman-shellcheck) | `koalaman/shellcheck` | GPL-3.0 | 40.374 | đọc tài liệu 2026-11-23 | 30 | Phân tích tĩnh script bash/sh để tìm lỗi cú pháp, quoting và portability. |
| [ESLint](../../30-software-testing-quality/README.md#anhkysuai-eslint-eslint) | `eslint/eslint` | MIT | 27.644 | đọc tài liệu 2026-11-23 | 30 | Phân tích mẫu lỗi và quy tắc trong mã JavaScript theo AST. |
| [Biome](../../13-dev-stack-devops/README.md) | `biomejs/biome` | MIT / Apache-2.0 | 26.026 | chưa chuẩn hóa | 13 | Format + lint JS/TS, 500+ rule; |
| [oxlint](../../13-dev-stack-devops/README.md) | `oxc-project/oxc` | MIT | 23.285 | chưa chuẩn hóa | 13 | Linter JS/TS viết bằng Rust; |
| [Mypy](../../30-software-testing-quality/README.md#anhkysuai-python-mypy) | `python/mypy` | MIT cho mypy/mypyc; một số tệp và thành phần có PSF/BSD hoặc thông báo riêng | 20.735 | đọc tài liệu 2026-11-23 | 30 | Bộ kiểm kiểu tĩnh cho Python, cho phép thêm type hint từng phần mà không đổi cách chương trình chạy. |
| [pyright](../../13-dev-stack-devops/README.md) | `microsoft/pyright` | MIT | 15.720 | chưa chuẩn hóa | 13 | Type checker Python; |
| [react-doctor](../../30-software-testing-quality/README.md#chuyen-react-doctor) | `millionco/react-doctor` | Modified MIT License | 15.154 | đọc tài liệu 2026-11-18 | 30 | Công cụ quét tĩnh có tính tất định cho dự án React, báo lỗi về state/effect, hiệu năng, kiến trúc, bảo mật, a11y và khả năng bảo trì. |
| [knip](../../13-dev-stack-devops/README.md) | `webpro-nl/knip` | ISC | 12.560 | chưa chuẩn hóa | 13 | Tìm file/export/dependency chết; |
| [Stylelint](../../06-ui-ux-design/README.md) | `stylelint/stylelint` | MIT | 11.542 | chưa chuẩn hóa | 06 | 154 luật lint CSS (color-no-hex, declaration-property-value-allowed-list, no-unknown-custom-properties) để cấm giá trị ngoài token; |
| [SQLFluff](../../15-ai-for-data/README.md) | `sqlfluff/sqlfluff` | MIT | 10.011 | chưa chuẩn hóa | 15 | Linter + auto-fix SQL, 28 file dialect, templater Jinja/dbt, lõi Rust sqlfluffrs; |
| [zizmor](../../31-software-supply-chain-security/README.md) | `zizmorcore/zizmor` | MIT | 6.856 | chưa chuẩn hóa | 31 | Phân tích tĩnh bảo mật GitHub Actions, 41 audit, SARIF, offline/online; |
| [jscpd](../../13-dev-stack-devops/README.md) | `kucherenko/jscpd` | MIT | 6.472 | chưa chuẩn hóa | 13 | Phát hiện code trùng lặp; |
| [actionlint](../../13-dev-stack-devops/README.md) | `rhysd/actionlint` | MIT | 4.371 | chưa chuẩn hóa | 13 | Lint workflow GitHub Actions: kiểm kiểu ${{ }}, shellcheck/pyflakes; |
| [@shadcn/lint](../../06-ui-ux-design/README.md) | `shadcn-ui/lint` | MIT | 3.291 | chưa chuẩn hóa | 06 | 6 luật ESLint/Oxlint cho design system Tailwind v4, thông báo lỗi viết cho agent; |
| [crapper / dryer / mutator (Uncle Bob)](../../20-claude-plugins-ecosystem/README.md) | `unclebob/crapper` | 0BSD | 171 | chưa chuẩn hóa | 20 | Bộ cổng chất lượng Python của Robert C. |
| [dependency-cruiser](../../29-software-architecture-api-contracts/README.md#dependency-cruiser-architecture-gates) | `sverweij/dependency-cruiser` | MIT | — | đọc mã 2026-11-04 | 29 | Kiểm graph/rule dependency JS/TS; |

## Eval skill/agent (`ai-skill-eval`, 6)

| Dự án | Repo | License | ★ | Bằng chứng | Mục | Tóm tắt |
|---|---|---|---|---|---|---|
| [SkillsBench](../../20-claude-plugins-ecosystem/README.md#xlsx-2026-11-23-skillsbench) | `benchflow-ai/skillsbench` | Apache-2.0 | 1.936 | đọc mã 2026-11-23 | 20 | Benchmark skill của agent: task.md + Docker + oracle + verifier (reward 1/0 từ pytest, phụ thuộc ghim); |
| [agent-skills-eval](../../20-claude-plugins-ecosystem/README.md) | `darkrishabh/agent-skills-eval` | MIT | 809 | chưa chuẩn hóa | 20 | Test runner skill with_skill vs without_skill có judge, báo cáo HTML; |
| [skillgrade](../../20-claude-plugins-ecosystem/README.md) | `mgechev/skillgrade` | MIT | 734 | chưa chuẩn hóa | 20 | Unit test cho skill: eval.yaml, chạy nhiều harness trong Docker, grader tất định/LLM/người, --ci --threshold, JUnit; |
| [NVIDIA SkillEvaluator](../../20-claude-plugins-ecosystem/README.md) | `NVIDIA/SkillEvaluator` | Apache-2.0 | 622 | chưa chuẩn hóa | 20 | Eval skill 3 tầng: chất lượng + scanner, trùng lặp, chạy agent có/không skill; |
| [agnix](../../20-claude-plugins-ecosystem/README.md#factory-skill-admission-2026-11-04) | `agent-sh/agnix` | MIT OR Apache-2.0 | 465 | đọc mã 2026-11-04 | 20 | Linter 757 luật cho CLAUDE.md, SKILL.md, hooks, MCP, plugin của nhiều harness; |
| [Coder Eval](../../20-claude-plugins-ecosystem/README.md) | `UiPath/coder_eval` | Apache-2.0 | 156 | chưa chuẩn hóa | 20 | Eval coding agent trong sandbox, kiểm skill_triggered theo harness, A/B, GitHub Action; |

## Hợp đồng API & schema (`api-contract`, 8)

| Dự án | Repo | License | ★ | Bằng chứng | Mục | Tóm tắt |
|---|---|---|---|---|---|---|
| [Bruno](../../30-software-testing-quality/README.md#anhkysuai-usebruno-bruno) | `usebruno/bruno` | MIT cho code; logo OpenMoji CC-BY-SA-4.0 | 48.512 | đọc tài liệu 2026-11-23 | 30 | API client desktop và CLI lưu collection bằng file cục bộ để quản lý bằng Git. |
| [Zod](../../30-software-testing-quality/README.md#anhkysuai-colinhacks-zod) | `colinhacks/zod` | MIT | 44.394 | đọc mã 2026-11-23 | 30 | Schema validation JavaScript/TypeScript đồng thời suy luận kiểu dữ liệu. |
| [Insomnia](../../30-software-testing-quality/README.md#anhkysuai-kong-insomnia) | `Kong/insomnia` | Apache-2.0 cho mã repo; tính năng dịch vụ theo gói riêng | 40.183 | đọc tài liệu 2026-11-23 | 30 | API client và bộ công cụ thiết kế, chạy thử REST, GraphQL, gRPC và WebSocket. |
| [Pydantic](../../30-software-testing-quality/README.md#anhkysuai-pydantic-pydantic) | `pydantic/pydantic` | MIT | 29.634 | đọc tài liệu 2026-11-23 | 30 | Validation dữ liệu Python qua type hint và model. |
| [Spectral](../../29-software-architecture-api-contracts/README.md) | `stoplightio/spectral` | Apache-2.0 | 3.247 | chưa chuẩn hóa | 29 | Linter JSON/YAML, ruleset sẵn OpenAPI/AsyncAPI/Arazzo v1 (hỗ trợ Arazzo 1.1 chưa xác minh); |
| [OpenTelemetry Weaver](../../07-eval-observability/README.md) | `open-telemetry/weaver` | Apache-2.0 | 521 | chưa chuẩn hóa | 07 | registry check/live-check OTLP so với semconv, GitHub Action fail theo severity; |
| [oasdiff](../../29-software-architecture-api-contracts/README.md#oasdiff-compatibility-gates) | `oasdiff/oasdiff` | Apache-2.0 | — | đọc mã 2026-11-04 | 29 | Breaking diff OpenAPI base/revision; |
| [Schemathesis](../../30-software-testing-quality/README.md#schemathesis-factory) | `schemathesis/schemathesis` | MIT | — | đọc mã 2026-11-04 | 30 | Schema-based OpenAPI/GraphQL/gRPC testing và stateful sequences; |

## Hiệu năng & tải (`perf-load`, 10)

| Dự án | Repo | License | ★ | Bằng chứng | Mục | Tóm tắt |
|---|---|---|---|---|---|---|
| [Lighthouse](../../30-software-testing-quality/README.md#anhkysuai-googlechrome-lighthouse) | `GoogleChrome/lighthouse` | Apache-2.0 | 31.193 | đọc tài liệu 2026-11-23 | 30 | Audit trang web về hiệu năng và các thực hành phát triển. |
| [LeakCanary](../../30-software-testing-quality/README.md#anhkysuai-square-leakcanary) | `square/leakcanary` | Apache-2.0 | 30.009 | đọc tài liệu 2026-11-23 | 30 | Phát hiện rò rỉ bộ nhớ trong ứng dụng Android. |
| [Hyperfine](../../30-software-testing-quality/README.md#anhkysuai-sharkdp-hyperfine) | `sharkdp/hyperfine` | MIT OR Apache-2.0 | 29.338 | đọc tài liệu 2026-11-23 | 30 | Benchmark lệnh qua nhiều lần chạy và xuất thống kê. |
| [Locust](../../30-software-testing-quality/README.md#anhkysuai-locustio-locust) | `locustio/locust` | MIT | 28.307 | đọc tài liệu 2026-11-23 | 30 | Công cụ viết kịch bản kiểm tải bằng Python cho HTTP và giao thức mở rộng. |
| [React Scan](../../30-software-testing-quality/README.md#anhkysuai-aidenybai-react-scan) | `aidenybai/react-scan` | MIT | 21.882 | đọc tài liệu 2026-11-23 | 30 | Công cụ hiển thị component và điểm nóng hiệu năng khi quan sát ứng dụng React đang chạy. |
| [web-vitals](../../30-software-testing-quality/README.md) | `GoogleChrome/web-vitals` | Apache-2.0 | 8.669 | chưa chuẩn hóa | 30 | Thư viện chính thức đo LCP/INP/CLS ở người dùng thật, build attribution chỉ ra nguyên nhân; |
| [Lighthouse CI](../../13-dev-stack-devops/README.md) | `GoogleChrome/lighthouse-ci` | Apache-2.0 | 7.122 | chưa chuẩn hóa | 13 | Commit cuối 26/6/2025 (đứng yên); |
| [Web Quality Skills](../../06-ui-ux-design/README.md) | `addyosmani/web-quality-skills` | MIT | 3.025 | chưa chuẩn hóa | 06 | 6 Agent Skills đo-trước (audit, performance, Core Web Vitals, a11y WCAG 2.2, SEO, best practices); |
| [AIPerf](../../10-local-llm-rag-memory/README.md#aiperf) | `ai-dynamo/aiperf` | Apache-2.0 | 842 | đọc mã 2026-11-02 | 10 | Load generator đo TTFT/ITL/throughput; |
| [Grafana k6](../../30-software-testing-quality/README.md#k6-factory) | `grafana/k6` | AGPL-3.0 | — | đọc mã 2026-11-04 | 30 | Load test runtime Go/JS; |

## Cổng phát hành & review (`release-gate`, 7)

| Dự án | Repo | License | ★ | Bằng chứng | Mục | Tóm tắt |
|---|---|---|---|---|---|---|
| [Renovate](../../13-dev-stack-devops/README.md) | `renovatebot/renovate` | AGPL-3.0 | 22.974 | chưa chuẩn hóa | 13 | Cập nhật dependency 90+ trình quản lý gói; |
| [cz-cli](../../13-dev-stack-devops/README.md#chuyen-cz-cli) | `commitizen/cz-cli` | MIT | 17.503 | đọc tài liệu 2026-11-18 | 13 | Công cụ dòng lệnh nhắc người dùng điền các trường bắt buộc khi commit để thông điệp commit theo quy ước (ví dụ conventional-changelog). |
| [pre-commit](../../13-dev-stack-devops/README.md) | `pre-commit/pre-commit` | MIT | 15.674 | chưa chuẩn hóa | 13 | Hook git đa ngôn ngữ; |
| [reviewdog](../../13-dev-stack-devops/README.md) | `reviewdog/reviewdog` | MIT | 9.712 | chưa chuẩn hóa | 13 | Kết quả linter → comment review PR; |
| [release-please](../../13-dev-stack-devops/README.md) | `googleapis/release-please` | Apache-2.0 | 7.715 | chưa chuẩn hóa | 13 | Conventional commits → changelog + release PR; |
| [OpenSSF Best Practices Badge](../../09-engineering-checklists/README.md) | `ossf/best-practices-badge` | MIT | 1.372 | chưa chuẩn hóa | 09 | App bestpractices.dev: tiêu chí Baseline 1–3 (64 control sinh từ OSPS 2026-08-28) + Metal passing/silver/gold; |
| [Sloth](../../33-reliability-observability-operations/README.md#sloth-slo-generator) | `slok/sloth` | Apache-2.0 | — | đọc mã 2026-11-04 | 33 | SLO-to-Prometheus rules; |
