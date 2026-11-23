# 13 · Dev Stack: Frontend · Backend · Mobile · DevOps · Spec-driven · AI Code Review

> Nền tảng kỹ thuật "cổ điển" mà agent/AI tooling đứng trên. Số sao ước lượng 2026 (nguồn lệch).

## 1. Frontend

| Framework | Repo | ★ | Ghi chú |
|---|---|---|---|
| React | facebook/react | ~251k (11/10/2026) | React 19; nền của Next.js, shadcn/ui |
| Vue | vuejs/core | ~54,9k (31/10/2026; số ~208k cũ là lỗi dữ liệu, §6g.1) | Vue 3.5; Nuxt |
| Next.js | vercel/next.js | ~125–138k | App Router, Server Actions; 59% dev dùng (State of JS 2025) |
| Angular | angular/angular | ~95k | Angular 18+ |
| Svelte | sveltejs/svelte | ~78k | Svelte 5 runes; SvelteKit |
| Nuxt | nuxt/nuxt | ~54k | |
| Astro | withastro/astro | ~63,6k (31/10/2026) | Islands, content-first |
| SolidJS | solidjs/solid | ~32k | |
| Vite | vitejs/vite | ~83k (13/10/2026) | Build tool mặc định của hệ sinh thái; Rolldown; v8.3 |
| TanStack (Query/Router/Start) | TanStack/* | Query ~50k (13/10/2026) | Full-stack TS mới nổi; Query có adapter React/Vue/Solid/Svelte/Angular/Preact |
| Tailwind CSS | tailwindlabs/tailwindcss | ~98k (13/10/2026) | Utility-first CSS, v4.3 (cấu hình CSS-first); kiểm ảnh ở §6c |

## 2. Backend

| Framework | Repo | ★ | Ghi chú |
|---|---|---|---|
| FastAPI | fastapi/fastapi | ~100k | Mặc định cho API AI/Python |
| NestJS | nestjs/nest | ~76.8k (10/2026) | TS enterprise |
| Django | django/django | – | Python full-stack; Django 5 |
| Spring Boot | spring-projects/spring-boot | – | Spring Boot 4, Java enterprise |
| Hono | honojs/hono | ~32.5k | Edge-first, 1.5M tải/tuần, tăng nhanh nhất Node |
| Express / Fastify | expressjs/express · fastify/fastify | – | Express 5; Fastify hiệu năng |
| Bun / Deno | oven-sh/bun · denoland/deno | – | Runtime thay Node |
| Go (Gin, Fiber), Rust (Axum, Actix) | – | – | Hiệu năng cao |

## 3. Mobile / cross-platform

| Framework | Chia sẻ | Phù hợp |
|---|---|---|
| **Flutter** | UI + logic (Dart) | UI tùy biến, mobile + web + desktop |
| **React Native + Expo** | UI + logic (TS) | Team có sẵn React; New Architecture bỏ bridge |
| **Kotlin Multiplatform (+ Compose MP)** | Logic (UI native hoặc Compose) | Enterprise/fintech có kỹ năng Kotlin |
| .NET MAUI | UI + logic (C#) | Hệ sinh thái Microsoft |
| Capacitor/Ionic, Tauri Mobile | Web → native | Web team |

## 4. DevOps / Platform

| Lĩnh vực | Công cụ | Ghi chú |
|---|---|---|
| Container | Docker, Podman | |
| Orchestration | **Kubernetes** (CNCF graduated) | Baseline |
| IaC | **Terraform** (BSL) vs **OpenTofu** (MPL, fork cộng đồng), Pulumi, Crossplane | OpenTofu tăng do lo lock-in |
| GitOps / CD | **Argo CD** (CNCF graduated, phổ biến nhất), Flux | |
| CI | **GitHub Actions**, GitLab CI, Dagger (pipeline as code), Buildkite | |
| Observability | Prometheus, Grafana, OpenTelemetry, Loki | |
| Dev env | Dev Containers, Nix, mise | Quan trọng cho agent chạy test/lint |
| Danh sách | `bregman-arie/devops-exercises`, CNCF Landscape | |

### 4b. "Quality gate stack" quan sát trong 19 repo của chủ kho (mục 23, 2026-10-12)

| Lớp | Công cụ / mẫu | Repo |
|---|---|---|
| Bảo vệ nhánh | **GitHub rulesets** dưới dạng code (`.github/rulesets/main.json`), job `quality`/`quality-gate` gom mọi cổng làm required check duy nhất | case-study-ft41, Dhcb-Tools, Sales-Hunter |
| Dependency | Dependabot **gom nhóm đa hệ sinh thái** + **WIP cap** (giới hạn PR bot mở cùng lúc); `scheduled-audit.yml` pip-audit hằng tuần; `dotnet list package --vulnerable` | case-study-ft41, Sales-Hunter, Dhcb-Tools |
| Policy | OPA/conftest, `pr-policy.yml` (PR `feat` phải link spec "Approved for implementation"; tự xin Copilot review qua `pulls.requestReviewers`) | qlkh, xboss |
| Web | Playwright CI 4 worker + cache browser; **Lighthouse CI** chặn merge 4 category; `@axe-core/playwright` | Xgold, xboss |
| Release | release-please (conventional commits → changelog + tag), Keep a Changelog + commitlint/husky/lint-staged, nhãn `no-changelog` cho PR bot | REA, xboss, Sales-Hunter |
| Chất lượng mã | **oxlint** (lint Rust nhanh), **knip** (code/dep chết), **jscpd** (trùng lặp), fast-check (property test), TypeDoc; Python: **uv**, **ruff**, **pyright**, pip-audit, hatchling, pre-commit, import-linter | REA, Sales-Hunter, qlkh |
| Cổng tĩnh tự viết | 17+ `check:*` (route-perms, db-params, lib-layers, migrations, coverage ratchet, hex-hardcode, contrast, progress-freshness); fitness function AST; mutation test ~150 dòng | xboss, qlkh |
| Tài liệu tươi | `check-progress-freshness.ts` / `check_status_freshness.py` (SHA ghi trong PROGRESS/STATUS phải là tổ tiên HEAD; PROGRESS đổi cùng code); `validate_repo.py` hợp đồng repo (file bắt buộc, link md, config theo schema) | xboss, Sales-Hunter |
| Supply chain | hash-locked tool (`ci/tool-checksums.txt`), Action pin SHA, syft SBOM, gitleaks, CodeQL, concurrency group theo SHA | qlkh, X-Scanner, Dhcb-Tools |

**Stack frontend ghi nhận (10/2026):** Next.js 16 App Router + React 19 + TypeScript 6 (strict) + Tailwind 4; Postgres raw SQL hoặc Supabase; node:test thay vitest (xboss ADR-0002) — chọn theo nguyên tắc "ít phụ thuộc, agent chạy test được ngay".

### 4c. Thông số các repo trong quality gate stack (đã xác minh 2026-10-12)

| Repo | ★ (12/10) | License | Phát hành / hoạt động gần nhất | Vì sao chất lượng | Lưu ý |
|---|---|---|---|---|---|
| **astral-sh/uv** | 90,6k | Apache-2.0 + MIT | 0.13.0 (9/10/2026) | Quản lý gói/dự án Python viết bằng Rust; README đo nhanh hơn pip 10–100 lần | Vẫn 0.x; OpenAI công bố mua Astral (19/3/2026) |
| **astral-sh/ruff** | 50,0k | MIT | 0.17.0 (9/10/2026) | Linter + formatter Python, hơn 900 rule; FastAPI, pandas, SciPy, transformers, Airflow dùng | Không kiểm kiểu; rule có thể đổi giữa các bản 0.x |
| **microsoft/pyright** | 15,7k | MIT | 1.1.414 (9/9/2026), commit 9/10 | Type checker Python theo chuẩn, Microsoft bảo trì, CLI + VS Code | Cần Node; một số tính năng IDE chỉ có trong Pylance |
| **biomejs/biome** | 25,9k | MIT / Apache-2.0 | CLI v2.5.15 (30/9/2026), commit 12/10 | Formatter + linter JS/TS/JSON/CSS/GraphQL, hơn 500 rule, tương thích Prettier 97%, không cần Node | Chưa ngang hoàn toàn ESLint/Prettier, chuyển config cần cẩn thận |
| **oxc-project/oxc** (oxlint) | 23,0k | MIT | oxlint v1.87.0 (5/10/2026) | Bộ công cụ JS nhanh (parser, oxlint, oxfmt); Preact, Shopify, ByteDance dùng oxlint | Phát hành rất dày |
| **webpro-nl/knip** | 12,4k | ISC | 6.41.0 (9/10/2026) | Tìm file, dependency, export không dùng trong JS/TS; có `@knip/mcp` và language server; chỉ 11 issue mở | Framework cần cấu hình plugin (vd. chạy typegen của react-router trước) |
| **kucherenko/jscpd** | 6,4k | MIT | v5.4.1 (9/10/2026) | Phát hiện code trùng lặp cho 224 định dạng; reporter SARIF/AI, GitHub Action, MCP server; engine Rust | Phát hiện trùng lặp ngữ nghĩa (Type-4) còn thử nghiệm |
| **renovatebot/renovate** | 22,7k | AGPL-3.0 | 44.151.5 (12/10/2026) | Tự động cập nhật dependency cho hơn 90 trình quản lý gói trên GitHub, GitLab, Bitbucket, Azure DevOps, Gitea, Forgejo | AGPL; khoảng 1k issue mở |
| **pre-commit/pre-commit** | 15,6k | MIT | v4.6.2 (10/8/2026), commit 9/10 | Framework hook git đa ngôn ngữ, ghim phiên bản hook theo repo; có pre-commit.ci; chỉ 18 issue mở | Hook local bỏ qua được bằng `--no-verify` → luôn chạy lại trong CI |
| **googleapis/release-please** | 7,6k | Apache-2.0 | v17.11.2 (24/8/2026) | Conventional commits → changelog + tag (REA, xboss dùng) | — |
| **reviewdog/reviewdog** | 9,7k | MIT | commit 11/10/2026 | Biến kết quả linter bất kỳ thành comment review trên PR | Bản phát hành cuối v0.21.2 (18/9, nhiều khả năng năm 2025) |
| **stryker-mutator/stryker-js** | 3,2k | Apache-2.0 | v10.0.0 (14/8/2026) | Mutation testing chuẩn cho JS/TS; thay script tự viết ở §4b khi repo lớn | — |
| **GoogleChrome/lighthouse-ci** | 7,1k | Apache-2.0 | **commit cuối 26/6/2025** | Chặn merge theo điểm Lighthouse (Xgold, xboss dùng) | **Đứng yên hơn 15 tháng** — vẫn chạy được nhưng cần theo dõi phương án thay |

**Nhận xét:**

- Phần lớn stack trong §4b được bảo trì rất tích cực (có bản phát hành trong 10/2026). Ngoại lệ đáng chú ý: **Lighthouse CI không commit từ 6/2025**, trong khi hai repo của chủ kho đang dùng nó làm cổng chặn merge.
- uv và ruff giờ thuộc OpenAI (thương vụ Astral công bố 19/3/2026); license vẫn MIT/Apache nên rủi ro thấp, nhưng nên theo dõi.
- Repo JS/TS mới: biome (format + lint) hoặc oxlint, cộng knip và jscpd. Python: uv + ruff + pyright. Cả hai: pre-commit ở máy **và** chạy lại trong CI; Renovate hoặc Dependabot gom nhóm.
- `alibaba/open-code-review` (§6) nay có 46,4k★, v1.12.13 (8/10/2026); mới mở mã giữa 2026, chỉ có benchmark tự công bố, và theo chính số liệu đó recall thấp hơn Claude Code.

## 5. Spec-driven development (SDD) cho AI coding

| Công cụ | Repo / nhà cung cấp | License | Cách tiếp cận | Nhận xét |
|---|---|---|---|---|
| **GitHub Spec Kit** | github/spec-kit | MIT | CLI + template: `specify → plan → tasks → implement`, chạy trên agent có sẵn (Copilot, Claude Code, Cursor, Gemini CLI) | Trung lập nhất; còn breaking changes |
| **AWS Kiro** | kiro.dev | Proprietary | IDE fork VS Code, spec-first từ đầu, hooks | Lock-in AWS |
| **BMAD-METHOD** | bmad-code-org/BMAD-METHOD | MIT | Agent theo vai trò (analyst, PM, architect, dev) mô phỏng team | Opinionated về quy trình |
| **OpenSpec** | Fission-AI/OpenSpec | MIT | Spec thay đổi (change proposals) nhẹ | |
| Tessl, intentdocs, codemyspec | – | – | Thương mại | |

**Liên hệ mục 03:** spec là "hợp đồng" để chạy nhiều agent song song và là tiêu chí dừng cho loop.

### 5a. Hồ sơ github/spec-kit: từ bộ template SDD thành khung quy trình có extension, preset, workflow và bundle (ảnh trang repo người dùng gửi, đọc mã 3/11/2026)

> Ảnh ghép hai phần: trang repo (`github/spec-kit`, 102 issue, 125 PR, 13k fork, 145k★, commit cuối `7370e59` của Quratulain-bilal "3 days ago", About "Toolkit to help you get started with SDD or any other process!", topic ai/copilot/development/engineering/prd/spec/spec-driven, MIT) và đầu README ("Build with a spec, fix a bug, or assess an idea — with your coding agent", badge release **v1.2.5**, 145k★, MIT, docs GitHub Pages). Đã clone `--filter=blob:none` đủ lịch sử, HEAD `ba8363f8ab56b2da456a81299cfdbfee1ef7b871` (2/11/2026). **Không cài, không chạy.** Dòng bảng §5 ở trên là ghi chép từ 10/2026; hồ sơ này thay cho nó.

**Kiểm ảnh**

| Ô trong ảnh | Kết quả | Đối chiếu (3/11/2026) |
|---|---|---|
| 145k★, 13k fork | ✅ | 145.528★, 13.055 fork (GitHub search API) |
| 102 issue + 125 PR | ✅ gần đúng | API trả 214 issue+PR mở; ảnh cộng lại là 227, khác nhau do thời điểm chụp |
| "release v1.2.5" | ⚠️ cũ | v1.2.5 ra 28/10/2026; **v1.2.6** ra 2/11/2026 (PyPI cũng 1.2.6). `pyproject.toml` ở HEAD đã là `1.2.7.dev0` |
| "MIT" | ✅ | `LICENSE` MIT, "Copyright GitHub, Inc." |
| Câu "SDD or any other process" | ✅ | README nay chia **ba quy trình**: SDD nằm trong lõi, còn bug fixing và idea assessment là extension đi kèm (bundle `bugfix`, `assess`), cộng cơ chế để tự làm quy trình riêng |

**Đã đổi so với dòng §5 (ghi 10/2026)**

- Không còn chỉ là `specify → plan → tasks → implement` với 4 agent. `integrations/catalog.json` có **43 integration**. Có thêm 5 lớp mở rộng: extension (5 chính thức, **186 cộng đồng**), preset (42 cộng đồng), workflow (có overlay và step package), bundle theo vai trò, và catalog riêng của tổ chức, hỗ trợ cả air-gapped. README tự nói: "Catalog listings are not audits or endorsements, so review community source code before installing".
- Cài bằng `uv tool install specify-cli` từ PyPI (Python ≥ 3.11). Trước đây README hướng dẫn cài `--from git+https://github.com/github/spec-kit.git`; lệnh này bị bỏ trong đợt tinh gọn README 5/2026 (`707e929`) rồi 9/2026 (`3affdb2`).
- Dự án lớn nhanh: 2.329 commit từ 21/8/2025. Manfred Riem 424, bot 249, Den Delimarsky khoảng 286 (2 tên); **869 dòng trailer Co-Authored-By Claude**.

**Cổng và chuỗi phát hành (đọc mã)**

- `publish-pypi.yml` build bằng `uv build`, rồi `uv publish` trong environment `pypi` với `id-token: write` (trusted publishing OIDC). Action ghim theo **SHA**. Tuy vậy PyPI **không có provenance** cho `specify_cli-1.2.6-py3-none-any.whl` (API integrity của PyPI trả "No provenance available"). Muốn kiểm nguồn gốc thì phải đối chiếu với release trên GitHub.
- CI có `test.yml` (Python 3.11 và 3.12 từ #5220), `lint.yml`, `codeql.yml`, `security.yml`, `extension-version-guard.yml`. Repo cũng tự dùng **GitHub Agentic Workflows** (cặp `*.md` + `*.lock.yml`) để agent đánh giá bug, PR và feature, và để duyệt đề xuất thêm extension, preset, bundle cộng đồng, có danh sách `trusted-users` (xem gh-aw ở mục 21).
- Grep `telemetry|posthog|analytics` trong `src/` chỉ thấy comment về handler sự kiện; **không thấy mã gửi telemetry**.

**Rủi ro và cách dùng**

- Extension, preset và workflow cộng đồng có thể chạy lệnh shell và hook theo vòng đời agent. Hãy đọc mã trước khi cài, hoặc dựng catalog riêng chỉ gồm thành phần đã duyệt (tính năng có sẵn).
- Ghim phiên bản (`uv tool install specify-cli==1.2.6`). Nhịp phát hành vài ngày một bản; CHANGELOG và `docs/upgrade` là nơi xem thay đổi phá vỡ tương thích.
- Spec Kit "sở hữu quy trình" giống BMAD hay GSD. Nếu chỉ cần skill nhỏ, xem phản đề ở mục 20 §3c (mattpocock/skills). OpenSpec gọn hơn cho thay đổi nhỏ; Kiro khoá vào IDE của AWS.

**Nguồn §5a:** ảnh người dùng gửi 3/11/2026 · clone https://github.com/github/spec-kit HEAD `ba8363f8ab56b2da456a81299cfdbfee1ef7b871` (README.md, LICENSE, pyproject.toml, `integrations/catalog.json`, `extensions/catalog{,.community}.json`, `presets/catalog.community.json`, `workflows/`, `bundles/`, `.github/workflows/{publish-pypi,test}.yml` và các `*.lock.yml`; `git tag`, `git shortlog`, `git log -S git+https`) · https://pypi.org/pypi/specify-cli/json (1.2.6, 78 bản) · PyPI integrity API (không có provenance cho 1.2.6) · GitHub search API `repo:github/spec-kit` 3/11/2026.

## 6. AI code review

| Công cụ | Giá | Thế mạnh | Hạn chế |
|---|---|---|---|
| **CodeRabbit** | $24 / $48 dev/tháng; free public repo | All-rounder ít nhiễu; hỗ trợ 4 Git host | |
| **Greptile** | – | Bắt lỗi cross-file tốt (82% một benchmark) | Nhiều false positive; GitHub-first; benchmark Macroscope cho thấp hơn |
| **Qodo** (CodiumAI) | Qodo Merge mở, self-host (bản mã mở nay là `The-PR-Agent/pr-agent`, MIT, cộng đồng giữ, §6g.1) | F1 cao nhất trong 8 tool (2/2026); sinh test | |
| **GitHub Copilot Code Review** | Theo Copilot; usage-based private repo từ 6/2026 | Ít ma sát | Nông hơn |
| **Claude Code Review / `/code-review`** | Theo gói Claude | Chạy trong CLI/CI, GitHub Action | |
| Bito, Macroscope | – | | |
| **alibaba/open-code-review** (`ocr`) | Mở, Apache-2.0, Go; `ocr delegate` không cần API key | **Luật review theo glob đường dẫn** (`rule.json`, first-match-wins); xboss sinh rule từ mảnh markdown + test khớp file→rule; dhcb dùng | CI chỉ góp ý, không chặn |
| Santa Method / Council (skill ECC) | Theo gói model | 2 reviewer độc lập cùng rubric, cả hai phải pass | Xem mục 07 |

## 6b. Kiểm ảnh "CRM System Architecture" (#codepathindia, ảnh người dùng gửi, 2026-10-13)

Ảnh vẽ một CRM theo kiểu microservices. Client (web, mobile, nhân viên sales, cổng tự phục vụ của khách) đi qua CDN và load balancer, rồi API Gateway (Kong/NGINX/AWS) có IAM (Keycloak/Auth0). Phía sau là 6 service viết bằng Go/Echo: User, Contact, Opportunity, Task, Communication, Report & Analytics. Tầng dữ liệu gồm PostgreSQL, Redis, S3 và ClickHouse. Tích hợp ngoài: SendGrid/SES, Twilio, Stripe/Razorpay, Google Calendar. Hạ tầng chạy Docker và Kubernetes (HPA, EBS/EFS); quan sát bằng Prometheus, Grafana, ELK/OpenSearch, Jaeger. CI/CD dùng GitHub Actions/Jenkins, IaC dùng Terraform.

| Ô trong ảnh | Đánh giá | Ghi chú |
|---|---|---|
| CDN + LB, API Gateway (routing, rate limit, auth), IAM có RBAC/SSO | ✅ | Đúng vai trò từng lớp. Rate limit đặt ở gateway là hợp lý |
| 6 service tách theo miền (contact, opportunity, task…) | ⚠️ | Cách chia hợp lý về mặt miền. Nhưng với một CRM của một công ty, 6 service + Kubernetes là chi phí vận hành lớn; modular monolith tách đúng theo các miền này rồi mới tách dần thường rẻ hơn nhiều |
| Mỗi service ghi "PostgreSQL", tầng dữ liệu chỉ có một "PostgreSQL (Primary DB)" | ⚠️ | Ảnh không nói rõ database riêng cho từng service hay dùng chung. Dùng chung một schema thì các service dính nhau qua bảng, mất lợi ích chính của microservices |
| Không có message broker | ❌ | Các mũi tên đều là gọi trực tiếp. CRM cần sự kiện bất đồng bộ (lead mới → gửi email, đổi stage → cập nhật báo cáo, webhook ra ngoài). Thiếu Kafka/RabbitMQ/NATS hoặc ít nhất outbox pattern, và Communication Service dựa vào Redis thì dễ mất tin khi Redis không bật persistence |
| ClickHouse cho báo cáo | ⚠️ | Hợp lý cho analytics. Nhưng ảnh thiếu đường đưa dữ liệu từ PostgreSQL sang (CDC như Debezium, hoặc ETL); không có nó thì báo cáo sai hoặc chậm |
| "Load Balancer (Service Mesh)" có circuit breaker | ⚠️ | Gộp hai khái niệm khác nhau. Service mesh (Istio/Linkerd) lo mTLS, retry, circuit breaker giữa các service; LB ở rìa là chuyện khác |
| Persistent Volumes EBS/EFS | ⚠️ | Service Go nên stateless; volume chỉ cần nếu tự chạy DB trong cluster, mà khi đó nên dùng dịch vụ quản lý (RDS…) và có backup/PITR |
| Prometheus + Grafana + ELK/OpenSearch + Jaeger | ✅ | Bộ quan sát chuẩn. Ngày nay nên thu traces/metrics/logs qua OpenTelemetry rồi đẩy vào các backend này |
| CI/CD: Code Push → Build → Test → Build Image → Deploy | ⚠️ | Thiếu quét bảo mật (SAST, quét image, quét bí mật), migration DB, và môi trường staging trước production |
| Không có trong ảnh | ❌ | Tìm kiếm khách hàng/full-text (OpenSearch chỉ được vẽ cho log), audit log, backup và khôi phục, quản lý bí mật (Vault/Secrets Manager), multi-tenant nếu bán SaaS, đồng ý/xoá dữ liệu cá nhân (GDPR, Nghị định 13/2023 ở Việt Nam) |

**Tổng:** 2 ✅, 6 ⚠️, 2 ❌. Ảnh dùng được làm **bản đồ thuật ngữ** cho người mới (các lớp trong một hệ thống SaaS điển hình), không dùng được làm bản thiết kế: không có gì riêng của CRM ngoài tên service, và thiếu đúng phần khó nhất là luồng sự kiện giữa các service.

**Nếu cần CRM thật, xem mã nguồn mở trước khi tự dựng** (★ qua shields.io, 13/10/2026):

| Repo | ★ | Giấy phép | Stack | Ghi chú |
|---|---|---|---|---|
| twentyhq/twenty | ~58k | Phần lớn AGPL-3.0; một số file `@license Enterprise` là thương mại; SDK/CLI/UI là MIT | TypeScript, NestJS, PostgreSQL, Redis | CRM hiện đại, tự host được; dự án sôi động (commit hôm qua) |
| krayin/laravel-crm | ~24k | MIT | PHP Laravel | Giấy phép thoáng nhất trong nhóm |
| odoo/odoo | ~55k | LGPL-3.0 (bản Community) | Python | ERP đầy đủ, CRM là một module; Enterprise là bản trả phí |
| salesagility/SuiteCRM | ~5,8k | AGPL-3.0 | PHP | Kế thừa SugarCRM; lâu đời |
| frappe/crm | ~3,8k | AGPL-3.0 | Python (Frappe), Vue | Gọn, đi cùng hệ Frappe/ERPNext |
| espocrm/espocrm | ~3,5k | AGPL-3.0 | PHP | Nhẹ, dễ tuỳ biến |

Đọc kỹ các repo này cho thấy chúng đều là **monolith** (một ứng dụng + PostgreSQL/MySQL + job queue), không phải 6 microservice như ảnh.

## 6c. Kiểm ảnh "5 GitHub Repositories Every Frontend Developer Should Know" (codingwithparvez, ảnh người dùng gửi, 2026-10-13)

Ảnh giới thiệu 5 repo, mỗi repo kèm thẻ, "Why it's useful", một đoạn mã và ảnh minh họa. Số liệu kiểm bằng shields.io và `npm view` ngày 13/10/2026.

| Ô trong ảnh | Kết luận |
|---|---|
| ① **shadcn-ui/ui**: "Customizable UI components", thẻ React/TypeScript, "Add accessible components and own the code in your project", `import { Button } from "@/components/ui/button"` | ✅ Đúng mô hình copy mã vào dự án; đường dẫn import đúng mặc định CLI. ~125k★, MIT, CLI `shadcn` 4.21.4. Tính "accessible" đến từ primitive bên dưới (Base UI mặc định từ 7/2026, trước là Radix, xem mục 06) |
| ② **TanStack/query**: thẻ React, `const { data, isLoading } = useQuery({ queryKey, queryFn })` | ⚠️ Thẻ chỉ ghi React, trong khi thư viện có adapter Vue, Solid, Svelte, Angular, Preact (`@tanstack/*-query` đều có trên npm). `isLoading` vẫn chạy ở v5 nhưng tài liệu hiện chỉ dạy `isPending` rồi `isError`. ~50k★, MIT, `@tanstack/react-query` 5.104.2 |
| ③ **storybookjs/storybook**: thẻ React, `import type { Meta, StoryObj } from "@storybook/react"` + `satisfies Meta<typeof Button>` | ⚠️ Tài liệu Storybook 10.6 bảo import từ gói **framework** (`@storybook/react-vite`, `@storybook/nextjs`…), không phải gói renderer `@storybook/react`. Thẻ React thiếu Vue/Angular/Svelte/Web Components. `satisfies` đúng. ~91k★, MIT, v10.6.2 |
| ④ **vitejs/vite**: `npm create vite@latest my-app` → `npm install` → `npm run dev`; màn hình "VITE v5.x ready in 320 ms", "Network: http://192.168.1.5:5173" | ⚠️ Lệnh đúng (create-vite 9.2.1 còn có cờ `--immediate` cài và chạy luôn). Màn hình cũ: bản hiện tại là **8.3.4**, và mặc định Vite in "Network: use `--host` to expose"; dòng địa chỉ LAN chỉ có khi chạy với `--host` (đọc mã `vite` 8.3.4). ~83k★, MIT |
| ⑤ **tailwindlabs/tailwindcss**: "Utility-first CSS", JSX `className="min-h-screen bg-gray-950 text-white flex items-center justify-center"` | ✅ Mọi class có trong Tailwind 4.3.3. ~98k★, MIT |

**Tổng: 2✅ / 3⚠️ / 0❌.**

**Dùng ảnh thế nào:** danh sách đúng là 5 công cụ phổ biến, cả 5 đều MIT và còn hoạt động (commit trong ngày). Ba lỗi đều là lỗi "chụp lúc cũ hoặc chỉ nhìn React": sửa nhãn thành đa framework, đổi `isLoading` → `isPending`, import Storybook từ gói framework, cập nhật màn hình Vite. Tiêu đề "every frontend developer" thực ra là "dev React + Vite"; không có công cụ test (Vitest, Playwright) hay lint (ESLint, Biome) nào, xem §1 và §4b. Không tìm được bài gốc của codingwithparvez.

**Nguồn của mục:** shields.io 13/10/2026 (5 repo: sao, license, commit cuối, release) · `npm view` 13/10/2026 (shadcn, @tanstack/{react,vue,svelte,solid,angular-query-experimental,preact}-query, storybook, @storybook/{react,react-vite,vue3-vite,angular,sveltekit,web-components-vite}, vite, create-vite, tailwindcss) · https://storybook.js.org/docs/writing-stories · https://tanstack.com/query/latest/docs/framework/react/guides/queries · mã `vite` 8.3.4 (`dist/node/chunks/node.js`, chuỗi "--host … to expose") và README `create-vite` 9.2.1.

## 6d. Homebrew/BrewUI: GUI chính thức của Homebrew cho macOS (link người dùng gửi, 2026-10-14)

> Đã clone toàn bộ repo (1.201 commit, HEAD `7bc5efa` 13/10/2026, tag v0.6.0) và đọc README, `ARCHITECTURE.md`, `AGENTS.md` (`CLAUDE.md` là symlink tới nó), `Package.swift`, `.github/workflows/`, PR template, `Sources/`. Đối chiếu bài BleepingComputer, dev.to và trang GitHub.

### 6d.1 Hồ sơ nhanh

| Mục | Thông tin (đọc 14/10/2026) |
|---|---|
| Repo | `Homebrew/BrewUI` · ~2,5k★, 80 fork, 2 issue + 2 PR mở · **AGPL-3.0** · About: "Homebrew's official macOS GUI" |
| Tuổi và nhịp | Commit đầu 2/3/2026; đỉnh 334 commit tháng 5, 235 commit tháng 9; 15 tag, v0.4.2 (15/9) → v0.6.0 (13/10/2026) |
| Tác giả | Graeme Arthur 875/1.201 commit; Mike McQuaid (trưởng dự án Homebrew) 67; BrewTestBot 102, dependabot 51; Ruoyu Zhong, Patrick Linnane là maintainer Homebrew |
| Ra mắt | "Phát hành đầy đủ" cùng **Homebrew 7.0.0 (13/9/2026)**, bản kèm lệnh `brew vulns` quét lỗ hổng qua OSV.dev (BleepingComputer 14/9/2026) |
| Cài | `brew install --cask homebrew-app`; app ký và notarize trong `release.yml` |
| Yêu cầu | **macOS 26 Tahoe trở lên** (`Package.swift`: `.macOS("26.0")`), Swift 6.2; Homebrew phải cài sẵn ở prefix mặc định (`/opt/homebrew` hoặc `/usr/local`) |
| Quy mô | 222 file Swift / ~20k dòng nguồn, 181 file test / ~24k dòng test (test nhiều hơn mã) |

### 6d.2 Kiến trúc và cổng chất lượng (đọc mã)

- **Không giấu Homebrew.** Mọi thao tác hiện lệnh `brew` copy được và giữ toàn bộ output trong console. Dữ liệu lấy từ `brew` CLI và JSON API formulae.brew.sh. App không sửa nội bộ Homebrew và chưa hỗ trợ prefix hay tap tuỳ chỉnh.
- **Clean Architecture + MVVM** chia 21 module SwiftPM: `BrewCore`, `BrewCLI` (chạy tiến trình), `BrewNetworking`, `BrewRepositories`, các `BrewFeature*` (Discover, Installed, Services, Doctor, Config, Console, SelfUpgrade). Feature không import feature khác.
- **Một hàng đợi lệnh.** Actor `SerialBrewCommandCenter` chạy tuần tự mọi lệnh làm thay đổi hệ thống và gộp lệnh trùng. Huỷ lệnh sẽ dừng cả process group.
- **Môi trường shell cô lập.** Luôn chạy `/bin/zsh --no-rcs --no-global-rcs` với PATH tối thiểu. Tham số đi qua argv nguyên văn, không nội suy chuỗi shell. Hệ quả: alias và biến export trong shell **không có tác dụng**, cấu hình phải đặt trong `brew.env`.
- **Tự nâng cấp** qua helper riêng: đợi app thoát, chạy upgrade, ghi kết quả, mở lại app. App từ chối nâng cấp khi đang có lệnh chạy.
- **Cổng máy:** pre-commit chạy SwiftFormat, SwiftLint strict và `BrewUILint` (luật lint riêng của dự án). CI có `pr_build_test` (`scripts/test`, `scripts/test-ui` trên runner `macos-26`), `swift_quality`, `licenses`, `actionlint`, `e2e`. Test UI tất định, không gọi Homebrew thật. Test e2e cài rồi gỡ gói `hello` thật.

### 6d.3 Điều đáng chú ý

- **Repo của một tổ chức lớn viết chủ yếu cùng AI, và nói rõ.** 455 trailer `Co-Authored-By` là model Claude (Opus 5, Opus 4.7/4.8, Sonnet 4.6) trên 1.201 commit. PR template có mục bắt buộc "AI assistance" và yêu cầu tách phần người tự kiểm với phần AI kiểm.
- **`AGENTS.md` (50 KB) là mẫu đáng học.** Có thứ tự ưu tiên chỉ dẫn (người dùng > `AGENTS.md` gần nhất > gốc) và quy định "web-search giá trị có phiên bản (runner, SDK, action) thay vì đoán theo dữ liệu huấn luyện". Agent phải chạy `scripts/test` trước mỗi commit. Bug sửa theo red-green TDD. Cấm dùng `scripts/test-e2e` trừ khi được yêu cầu. Cấm tắt test để qua CI. Cấm file nhớ phiên hay rule riêng cho từng tool. Khớp với khung drop-in của chủ kho (mục 23) và quy ước AGENTS.md (mục 04).
- **Không telemetry riêng của app** (grep `Sources/` không thấy SDK analytics). "Analytics" trong mã là số lượt cài công khai từ API Homebrew để xếp hạng trong Discover. Báo crash không tự gửi đi: app đọc báo cáo macOS ghi trong `~/Library/Logs/DiagnosticReports` rồi mở trang `issues/new` điền sẵn cho người dùng tự nộp. Lưu ý: chính `brew` vẫn gửi analytics theo mặc định của Homebrew. Muốn tắt thì đặt `HOMEBREW_NO_ANALYTICS=1` trong `~/.homebrew/brew.env`, vì app bỏ qua biến export của shell.
- **Tên dễ nhầm:** `mckaymic/Brewui` là app khác không liên quan. Bài Medium tả BrewUI như một phần của Homebrew, nhưng thực ra BrewUI là cask riêng (`homebrew-app`).
- **Thông tin cũ:** bài dev.to viết lúc dự án mới bắt đầu, nói "chưa tải về được". Nay đã có cask và bản v0.6.0.

### 6d.4 So sánh và dùng thế nào

| GUI Homebrew | ★ (14/10/2026, shields) | License | Ghi chú |
|---|---|---|---|
| **Homebrew/BrewUI** | ~2,5k | AGPL-3.0 | Chính chủ, cần macOS 26, hiện lệnh thật, dịch vụ chỉ đọc |
| `milanvarady/Applite` | ~7,1k | MIT | Tập trung cask/app, commit cuối 9/2026 |
| `buresdv/Cork` | ~4,7k | **"provisional license", không phải OSI** | Bản build sẵn bán trả phí (chưa xác minh giá) |
| `brunophilipe/Cakebrew` | ~5k | GPL-3.0 | **Đứng yên từ 3/2021** |

- **Cho người không quen Terminal** (đội văn phòng, thiết kế) trên macOS 26: BrewUI là lựa chọn an toàn nhất vì chính chủ, không giấu lệnh và không có telemetry riêng. Máy chạy macOS cũ hơn chỉ còn Applite.
- **Tái dùng mã:** AGPL-3.0 kèm điều khoản dùng qua mạng. Nhúng hay sửa để phát hành thì phải công bố mã. Học kiến trúc (hàng đợi lệnh tuần tự, shell cô lập, helper tự nâng cấp) thì không vướng.
- **Cho agent của chủ kho:** đáng mượn ba quy ước từ `AGENTS.md`: thứ tự ưu tiên chỉ dẫn, "tra web cho mọi giá trị có phiên bản" và mục AI assistance trong PR template.

**Nguồn §6d:** https://github.com/Homebrew/BrewUI (clone đầy đủ, HEAD 7bc5efa 13/10/2026; README.md, ARCHITECTURE.md, AGENTS.md, Package.swift, .github/workflows/{pr_build_test,release,build}.yml, .github/PULL_REQUEST_TEMPLATE.md, Sources/BrewCrashReporting/, Sources/BrewNetworking/, Tools/BrewUILint/; git log/tag) · trang GitHub và shields 14/10/2026 · https://github.com/Homebrew/BrewUI/releases · https://www.bleepingcomputer.com/news/security/homebrew-700-gets-built-in-gui-better-security-controls/ · https://dev.to/arshtechpro/brewui-a-first-look-at-homebrews-official-macos-gui-3fk2 · https://medium.com/@kanishks772/homebrew-just-got-a-gui-after-10-years-the-terminal-finally-has-a-window-64e73307752b · https://runany.dev/blog/brewui/ · https://www.opensourcealternatives.to/item/brewui · https://github.com/mckaymic/Brewui · https://github.com/milanvarady/Applite · https://github.com/buresdv/Cork · https://github.com/brunophilipe/Cakebrew · https://docs.brew.sh/Analytics

## 6e. Better-Linux/CleanMyLinux — app dọn dẹp Linux desktop (Tauri/Rust), có lỗ leo thang quyền đáng lưu ý (ảnh "4 repos worth bookmarking", 2026-10-18)

> Một trong 4 repo của slide Chris Porter (tác giả `Better-Linux` / PRAS Samin). Đã clone đầy đủ (HEAD `02de64d`, 25/5/2026, v1.0.0-beta.2), đọc README, `app.toml`, policy PolicyKit và mã Rust gọi helper.

| Thuộc tính | Giá trị (18/10/2026) |
|---|---|
| Repo / URL | https://github.com/Better-Linux/CleanMyLinux · slide: 8★/1 fork |
| Mô tả 1 dòng | App desktop "CleanMyMac cho Linux": gỡ ứng dụng an toàn, cập nhật đa trình quản lý gói (APT/Pacman/DNF/Flatpak/Snap), dọn rác, theo dõi app lâu không dùng |
| Loại | devops / desktop tool (GUI) |
| License | **MIT** (© 2026 Better Linux) |
| Stack | **Tauri v2 + Rust + React 19 + Bun**; GUI chạy quyền user thường, tác vụ admin qua **PolicyKit (pkexec)**; có thư mục `ml/` (app_classifier, progress_model) để lọc "app người dùng" khỏi thư viện hệ thống |
| Vì sao đáng tham khảo | • Hiếm có app dọn dẹp Linux desktop có GUI thống nhất nhiều trình quản lý gói; kiến trúc Tauri (Rust core + web UI) gọn.<br>• Có `docs/architecture.md`, CHANGELOG, SECURITY.md, CI, bảng distro/GLIBC hỗ trợ rõ ràng. |
| Hạn chế / rủi ro | • **⚠️ Lỗ leo thang quyền (đọc mã):** policy `config/com.betterlinux.cleanmylinux.policy` đăng ký đích pkexec là `/usr/bin/cleanmylinux-helper`, mà helper (`scripts/cleanmylinux-helper.sh`) chỉ là `exec "$@"`. Mã Rust gọi `pkexec /usr/bin/cleanmylinux-helper sh -c <lệnh>` (`src-tauri/src/system_info/ops.rs`). Đây là **primitive chạy lệnh tùy ý với quyền root**: với `allow_active = auth_self_keep`, sau một lần xác thực mật khẩu được cache, bất kỳ tiến trình nào của user active (kể cả mã độc) đều có thể gọi helper để chạy lệnh root. Một helper "exec mọi thứ" làm mất ý nghĩa của việc giới hạn action PolicyKit.<br>• Mới (beta), một tác giả, 8★; tên "premium" nhưng mã mở MIT.<br>• Binary dựng sẵn cần GLIBC ≥ 2.39. |
| Tích hợp | Nếu dùng/đóng gói: nên thu hẹp helper thành **danh sách lệnh cho phép** (không `exec "$@"`), hoặc tách từng action PolicyKit theo tác vụ, thay vì một đích exec vạn năng. Trước khi cài bản binary, cân nhắc build từ nguồn và đọc lại helper. |
| Liên quan | mục 13 §6d (BrewUI, GUI cho package manager), mục 12 §4 (nguyên tắc: allowlist tham số, review cho hành động quyền cao), mục 11 (sandbox) |
| Nguồn | clone 18/10/2026 (README, app.toml, config/*.policy, scripts/cleanmylinux-helper.sh, src-tauri/src/system_info/{ops,sudo}.rs); slide "4 GitHub repos worth bookmarking" |

## 6f. Case study: thsangyk-oss/sremote — terminal + remote desktop tự host qua Tailscale, không có lớp auth ứng dụng (link người dùng gửi, clone 2026-10-19)

**Kết luận:** một công cụ "mở lại phiên terminal/desktop của máy trạm từ trình duyệt hay điện thoại", gọn và trung thực về phạm vi, hợp để tiếp tục một phiên coding agent đang chạy. Nhưng toàn bộ an toàn **chỉ dựa vào ranh giới mạng Tailscale**: không có mật khẩu, token hay bất kỳ xác thực ứng dụng nào. Ai ở trên cùng tailnet (hoặc localhost) đều có shell toàn quyền, điều khiển chuột/bàn phím và đọc/ghi toàn bộ ổ đĩa của máy host. Cài bằng `irm … | iex` và tự nâng quyền admin. Repo mới, 2★, một phần code do agent Devin viết, chưa có file LICENSE.

### 6f.1 Hồ sơ nhanh

| Mục | Thông tin (đọc 19/10/2026) |
|---|---|
| Repo | `thsangyk-oss/sremote` · **~2★, 2 fork** · 53 commit, 25/9 → 19/10/2026 · tag mới nhất **v1.14.1** (README nói APK kèm v1.11.3) · **không có file LICENSE**; `package.json` ghi `"license":"ISC"`, trường `author` để trống |
| Tác giả | `thsangyk-oss` (16 repo công khai). README có QR **VietQR·MB** "Ủng hộ tác giả cốc cafe mua token" → tác giả Việt Nam **(chưa xác minh danh tính)**. Commit: `thsangyk-oss` 44, **`Devin` (agent AI) 6**, `thsangyk` 3 |
| Là gì | Máy chủ Node (`server.js` 1.091 dòng, cổng 2209; deps `node-pty`, `ws`, `@xterm/*`) + `agent/` (session broker giữ PTY sống trong tiến trình riêng; `screen-pro/ScreenPro.cs` 673 dòng chụp màn hình DXGI trên Windows; tray C#) + `public/` (web UI xterm.js, `app.js` 2.612 dòng) + `android/` (client Java thuần, không AndroidX) |
| Chức năng | Phiên terminal **sống xuyên thiết bị** (PTY sống trong broker, sống sót đóng tab/mất wifi/restart app); remote desktop (chuột, bàn phím, clipboard, đa màn hình, "trackpad mode" cho điện thoại); file explorer toàn máy (upload tới 4 GB, tự zip thư mục, giải nén, xem trước code/ảnh/video); git diff |
| Nền tảng | Host Windows/Linux/macOS; client trình duyệt + app Android |

### 6f.2 Mô hình bảo mật: chỉ có một lớp, là mạng

- **Lớp duy nhất:** `isAllowedRemote()` (server.js) chỉ cho `127.0.0.1`/`::1`, dải Tailscale `100.64.0.0/10` và ULA tailnet `fd7a:115c:a1e0:`; mọi địa chỉ khác bị **403** trước khi vào app, cho cả HTTP và WebSocket. README ghi đúng điều này ("Private by design").
- **Không có lớp thứ hai:** không mật khẩu, không token, không phiên đăng nhập. Khi đã qua được lớp IP, mọi route đều mở. Nghĩa là **bất kỳ thiết bị nào trên cùng tailnet** (hoặc bất kỳ tiến trình nào trên chính máy host, qua localhost) đều: mở shell mới, gõ lệnh vào phiên đang chạy, điều khiển desktop, và duyệt/tải/ghi file bất kỳ đâu trên máy.
- **"Jail" chỉ cho API file, không cho terminal:** các route `/api/files|file|fileop` có kiểm `jail()` chặn ra ngoài thư mục gốc (403 "outside jail"), nhưng terminal là shell đầy đủ nên giới hạn này không áng gì với người đã vào được.
- **Máy chủ `listen(PORT, "0.0.0.0")`:** lắng nghe trên mọi interface rồi lọc bằng IP ở tầng ứng dụng. An toàn chỉ còn đúng khi (a) Tailscale ACL thực sự giới hạn ai vào được tailnet, và (b) không có ai/cái gì không tin cậy chạy trên chính máy host. README có hướng dẫn thêm firewall giới hạn cổng 2209 vào riêng interface Tailscale — nên làm, vì nó là lớp phòng thủ thứ hai mà mặc định không có.

Đây **không phải lỗ hổng giấu kín** — mô hình "tin toàn bộ tailnet" là lựa chọn thiết kế, và README nói rõ chỉ tailnet vào được. Điều cần người đọc kho nắm: tailnet của bạn thường gồm nhiều thiết bị, và Tailscale cho phép chia sẻ node cho người khác; trên sremote, mọi nút được chia sẻ đều ngang bằng chủ máy. Không có "chế độ chỉ xem" hay phân quyền.

### 6f.3 Cài đặt và quyền

- **`irm … | iex`:** cách cài khuyến nghị là tải `install.ps1` từ `raw.githubusercontent.com` rồi chạy thẳng (`fix-state.ps1`, `elevate.ps1` cũng vậy). Đây là mẫu "chạy script từ xa không kiểm" — rủi ro chuỗi cung ứng như mọi `curl|sh`/`irm|iex`: tin tưởng repo + CDN tại thời điểm chạy. Nên tải script về đọc rồi mới chạy.
- **Tự nâng quyền admin:** cài từ shell elevated thì tác vụ autostart tự elevate, và **mọi phiên terminal kế thừa token admin** của chuỗi task → tray → server → PTY (README mục elevate). Đặt `$env:SREMOTE_LIMITED=1` để không elevate. Hệ quả: nếu đã bật, một phiên mở từ điện thoại là shell admin.
- Cài sẵn rule firewall qua `install.bat`/installer elevated.

### 6f.4 So với lựa chọn cùng loại

| | sremote | ttyd | sshx | wetty |
|---|---|---|---|---|
| Bản chất | Terminal + remote desktop + file, phiên bền, app phone | Chia sẻ 1 terminal qua web, 1 binary C | Terminal cộng tác, hạ tầng tác giả | SSH client trong trình duyệt |
| License | **chưa có file** (package.json ghi ISC) | MIT | — | MIT |
| Auth ứng dụng | **Không** (chỉ lọc IP tailnet) | Basic Auth tùy chọn (`-c user:pass`), ghi mặc định tắt | Link bí mật/khóa | Tùy chọn, + proxy |
| Phiên sống sau mất kết nối | Có (PTY trong broker) | Không | Có | Không (là SSH) |
| Điểm mạnh riêng | Remote desktop + file + app Android trong một | Nhẹ, chín, có auth | Cộng tác nhiều người | Dựa trên SSH sẵn có |

sremote thêm nhiều thứ ttyd không có (phiên bền, desktop, file, app phone), nhưng **bỏ hẳn lớp auth ứng dụng** mà ttyd có tùy chọn. Với ai chỉ cần terminal web có mật khẩu, ttyd + Tailscale vẫn an toàn hơn theo lớp.

### 6f.5 Dùng thế nào

- **Hợp khi:** một người, một tailnet riêng chỉ gồm thiết bị của chính mình, muốn tiếp tục phiên build/dev/coding-agent từ điện thoại. Đúng ca dùng README mô tả.
- **Không nên:** đặt trên tailnet chia sẻ nhiều người; dựa vào sremote như lớp an toàn khi host chạy cả tiến trình không tin cậy (localhost luôn vào được); để chế độ elevate nếu không cần shell admin.
- **Nếu dùng, tối thiểu:** thêm firewall giới hạn cổng 2209 vào riêng interface Tailscale (README có lệnh); siết Tailscale ACL để chỉ thiết bị của bạn thấy được node; đọc `install.ps1` trước khi `iex`; cân nhắc `SREMOTE_LIMITED=1`.
- **Trưởng thành:** repo 2★, 3 tuần tuổi, một phần do agent viết, chưa có LICENSE (dùng lại/nhúng chưa có cơ sở pháp lý rõ). Xem là công cụ cá nhân đang phát triển, không phải sản phẩm đã kiểm.

**Nguồn §6f:** https://github.com/thsangyk-oss/sremote (clone đầy đủ, 53 commit, HEAD `ce9e17c` 19/10/2026, tag v1.14.1; đọc README.md, AGENTS.md, package.json, server.js (`isAllowedRemote`, các route `/api/*`, `listen`), install.ps1, elevate.ps1, agent/screen-pro/ScreenPro.cs, public/app.js; không có file LICENSE) · https://github.com/thsangyk-oss (16 repo) · ttyd: github.com/tsl0922/ttyd (MIT) · besthub.dev/articles/three-open-source-web-terminal-tools · selfhostyourself.com/tags/ssh-client-web

## 6g. Nâng cấp 31/10/2026: rà repo lớn

> Cách làm: 7 truy vấn GitHub search (repo >40k★ theo TypeScript/Go/Rust push sau 1/9/2026, `code review ai`, `spec-driven development`, `devops agent kubernetes`, topic `developer-tools` tạo sau 1/10/2025), lọc bỏ repo đã có trong `data/projects.json`, chọn 7 repo. Repo lớn (Bun, Supabase, Tauri, act, PocketBase) clone `--filter=tree:0` và chỉ đọc file đích; repo nhỏ clone `--filter=blob:none`. **Không cài, không chạy gì.** Số sao từ GitHub search API ngày 31/10/2026.

### 6g.1 Trạng thái repo cũ của mục

| Repo | Thay đổi | Hệ quả |
|---|---|---|
| `vuejs/core` | Catalog từng ghi **~208k★ là lỗi dữ liệu**; số thật **54,9k** (GitHub API 31/10/2026) | Đã sửa bảng §1. Vue vẫn là framework lớn, nhưng không lớn hơn React |
| `withastro/astro` | 45,5k → **63,6k★**; GitHub báo license NOASSERTION (file vẫn MIT theo lần đọc trước, chưa đọc lại) | Sửa bảng §1 |
| `qodo-ai/pr-agent` | Repo nay ở **`The-PR-Agent/pr-agent`** (13,8k★, commit 31/10/2026). README: Qodo đã **tặng dự án cho cộng đồng**, "not the Qodo offering"; file LICENSE hiện là **MIT** (©2026 The PR Agent), catalog đang ghi AGPL-3.0 | Sửa link; catalog cần đổi license thành MIT. Qodo Merge thương mại nay là "Qodo 2.0" |
| `vercel/next.js`, `angular/angular`, `sveltejs/svelte`, `nuxt/nuxt` | Bảng §1 ghi số cũ; nay 143k · 101k · 88,5k · 61k★ | Thứ tự không đổi |
| `hashicorp/terraform`, `bmad-code-org/BMAD-METHOD`, `JetBrains/kotlin` | GitHub báo NOASSERTION/không nhận license | Giữ license đã đọc trong file (Terraform BUSL-1.1) |

### 6g.2 Bảng nhanh 7 repo mới

| Repo | Nhóm | ★ · license | Commit cuối | Một dòng | Cờ |
|---|---|---|---|---|---|
| `supabase/supabase` | Backend (BaaS) | 114,4k · Apache-2.0 | 31/10/2026 | Postgres + Auth + Storage + Realtime + Studio, tự host bằng Docker | `.env.example` chứa secret mẫu |
| `tauri-apps/tauri` | Desktop/mobile | 112,4k · MIT/Apache-2.0 | 31/10/2026 | App desktop/mobile nhỏ nhẹ với frontend web + lõi Rust | v3 đang alpha |
| `oven-sh/bun` | Runtime JS | 96,5k · MIT + LGPL tĩnh (GitHub: NOASSERTION) | 31/10/2026 | Runtime, bundler, test runner, package manager | **Đã viết lại bằng Rust (5/2026)**, thuộc Anthropic |
| `nektos/act` | DevOps/CI | 72,5k · MIT | 31/10/2026 | Chạy GitHub Actions cục bộ trong Docker | **5 lỗ Critical thoát container**, vá trong v0.2.94 |
| `pocketbase/pocketbase` | Backend 1 file | 61,6k · MIT | 26/10/2026 | Backend Go: SQLite, auth, file, realtime, admin UI | **Archive, rời GitHub** |
| `tirth8205/code-review-graph` | AI code review | 32,5k · MIT | 15/10/2026 | Đồ thị mã Tree-sitter trong SQLite, cấp "blast radius" qua MCP | Cài ghi cấu hình vào ~20 công cụ |
| `buildermethods/agent-os` | Spec-driven | 5,6k · MIT | 7/10/2026 | Lệnh/prompt để rút chuẩn mã từ codebase và viết spec | 22 file, docs ở web riêng |

### 6g.3 Hồ sơ từng repo

- **Bun.** Anthropic mua Bun 2/12/2025 (theo tin báo chí). Git log có commit **"Rewrite Bun in Rust (#30412)" của Jarred Sumner ngày 14/5/2026**; báo chí nói phần lớn do Claude viết trong ~11 ngày, nhà sáng lập Zig chê là "unreviewed" (các con số dòng mã, chi phí **chưa xác minh**). Tag `bun-v1.4.0` ngày 19/8/2026, mới nhất `bun-v1.4.4` (22/10). `CLAUDE.md` nay ghi "written primarily in Rust with C++"; 729 commit (3,9%) có trailer Claude, bot `robobun` 3.091 commit. `LICENSE.md`: Bun là MIT nhưng **link tĩnh JavaScriptCore/WebKit (LGPL-2)** và tinycc (LGPL-2.1), nên GitHub báo NOASSERTION; phân phối binary Bun phải tôn trọng điều khoản relink của LGPL. Crate `src/analytics` tôn trọng `DO_NOT_TRACK`. Cài: `npm install -g bun` hoặc `curl -fsSL https://bun.com/install | bash`. Với dự án dùng Bun làm runtime production: theo dõi độ ổn định sau đợt viết lại.
- **act.** `SECURITY_AUDIT.md` (10/2026) công khai kết quả audit: **5 lỗi Critical** (GHSA-7x4h, -v5hg, -hf9j, -3m58, -45wq) cho phép workflow qua `container.options`/`volumes:` bỏ CapDrop/seccomp, mount thư mục host, đọc file host, dùng PID/IPC host; thêm path traversal ở `uses:` và `.actrc` của project ghi đè hardening. Bản vá thêm chính sách `--container-options-policy` và allowlist `.actrc` (cờ có trong `cmd/root.go` ở HEAD = tag v0.2.94, 31/10/2026). Hệ quả: **chạy `act` trên repo lạ trước v0.2.94 tương đương chạy mã không tin cậy trên host**. Đáng chú ý: 61 commit từ 8/2026 có tác giả "Cursor Agent". Cài: `brew install act`; checksum ở `checksums.txt` của release.
- **PocketBase.** Commit cuối 26/10/2026 thêm dòng "The repo has moved to https://ganigeorgiev.com/pocketbase/pocketbase", repo đã archive. CHANGELOG v0.40.6: lệnh `update` từ nay tải bản mới từ `ganigeorgiev.com` "(there is nothing there yet)". 2.514/2.570 commit của một người. ⚠️ Kênh cập nhật chuyển từ GitHub Releases sang domain cá nhân: ghim phiên bản, kiểm checksum, đừng bật tự cập nhật. `go.mod` vẫn là `github.com/pocketbase/pocketbase`, đường import tương lai **chưa xác minh**.
- **Supabase.** 39.562 commit, 2.156 tác giả. Self-host qua `docker/` với tag riêng `self-hosted/v*` (mới nhất v0.8.3, 16/10/2026) và nhiều biến thể compose (Kong, Envoy, Caddy, Nginx, PG15/17). ✅ `docker/setup.sh` **tự sinh secret và khoá API bất đối xứng**. ⚠️ `docker/.env.example` vẫn chứa `JWT_SECRET`, `DASHBOARD_PASSWORD=this_password_is_insecure…`, `SECRET_KEY_BASE` mẫu: nếu copy thẳng file này thì instance dùng secret công khai. `.mcp.json` ở gốc trỏ tới MCP hosted `mcp.supabase.com`. Có `AGENTS.md`/`CLAUDE.md`, zizmor cho workflow.
- **Tauri.** 6.391 commit, 634 tác giả, dual license MIT/Apache-2.0 (có `LICENSE.spdx`). Bản ổn định v2.12.5 (21/10/2026); **v3 đang alpha** (alpha đầu 12/9, alpha.5 ngày 14/10). `SECURITY.md` yêu cầu báo lỗi qua private advisory. Gần như không có commit AI (2 trailer). Là lựa chọn nhẹ hơn Electron khi agent cần dựng app desktop (BrewUI §6d, CleanMyLinux §6e đã dùng).
- **code-review-graph.** Python, 1.270 commit từ 26/2/2026, 885 của một người, **35% có trailer Claude**. Tree-sitter → đồ thị node/edge trong SQLite, trả "blast radius" và tập file tối thiểu cần review qua MCP; có GitHub Action và extension VS Code. ⚠️ "65× ít token hơn" so token của cả codebase với token của một câu trả lời đồ thị, không đo chất lượng review. ⚠️ `code-review-graph install` tự dò và **ghi MCP entry, hook, skill vào file rules của tới ~20 công cụ** (Claude Code, Cursor, Codex…); có `uninstall --dry-run`. Cài: `pipx install code-review-graph`, rồi `install --platform claude-code` để chỉ đụng một công cụ.
- **Agent OS.** Chỉ 22 file: lệnh trong `commands/agent-os`, `profiles/`, 3 script bash cài vào project. Bốn bước: rút chuẩn từ codebase, tiêm chuẩn theo việc, shape spec, đánh chỉ mục. Tài liệu và cách cài nằm ở buildermethods.com (kèm gói Pro trả phí). 110/132 commit của một người, v3.0.0 (20/1/2026). Nhẹ hơn spec-kit/OpenSpec (§5), hợp khi chỉ cần "standards file" cho agent.

### 6g.4 Mẫu chung rút ra

1. **Hạ tầng dev cốt lõi đang được viết bởi agent**: Bun viết lại bằng Rust phần lớn nhờ Claude, act nhận vá bảo mật từ "Cursor Agent", code-review-graph 35% commit có trailer Claude. Khi chọn dependency, xem thêm tỉ lệ commit agent và mức review.
2. **Audit công khai trong repo** (act `SECURITY_AUDIT.md`: công cụ quét, GHSA, commit vá, mặc định an toàn và cách tắt) là mẫu đáng chép cho template.
3. **Kênh phân phối có thể đổi chủ**: PocketBase rời GitHub sang domain cá nhân, PR-Agent đổi org và license, Daytona (mục 11 §3c.1) đóng mã. Ghim phiên bản và nguồn tải.
4. **File mẫu chứa secret** (Supabase `.env.example`) vẫn phổ biến; script sinh secret phải là đường mặc định.
5. **Số catalog phải đọc từ API, không chép bài tổng hợp**: lỗi Vue ~208k đã nằm cả trong README §1 lẫn catalog.

**Nguồn §6g:** GitHub search API 31/10/2026 (7 truy vấn; `pr-agent in:name`) · `../meta_all.json`, `status_all.json` (GitHub API 31/10) · clone `--filter=tree:0`: bun (LICENSE.md, README.md, CLAUDE.md, src/analytics/lib.rs, git log #30412, tag bun-v1.4.0), act (README.md, SECURITY_AUDIT.md, VERIFICATION, cmd/root.go, tag v0.2.94), pocketbase (README.md, CHANGELOG.md, go.mod, LICENSE.md, commit 7f2773e), supabase (LICENSE, .mcp.json, docker/{.env.example, setup.sh}), tauri (SECURITY.md, LICENSE.spdx, tag tauri-v2.12.5/v3.0.0-alpha.5) · clone `--filter=blob:none`: code-review-graph (LICENSE, README.md, docs/, code_review_graph/), agent-os (LICENSE, README.md, scripts/, commands/), The-PR-Agent/pr-agent (LICENSE, README.md) · Web: simonwillison.net/2026/jul/8/rewriting-bun-in-rust, devclass.com/devops/2026/07/15/zig-creator-calls-buns-claude-rust-rewrite-unreviewed-slop, i-programmer.info (Bun 1.4) — báo chí/blog · https://github.com/oven-sh/bun · https://github.com/nektos/act · https://github.com/pocketbase/pocketbase · https://github.com/supabase/supabase · https://github.com/tauri-apps/tauri · https://github.com/tirth8205/code-review-graph · https://github.com/buildermethods/agent-os · https://github.com/The-PR-Agent/pr-agent

## 6h. Nâng trần 2/11/2026: chuẩn SLSA, lint bảo mật GitHub Actions, quét lỗ hổng theo SBOM và giám sát runner (yêu cầu người dùng)

> Cách làm: grep `data/projects.json` theo `repo` (Renovate, pre-commit, Dagger ở mục này; syft, gitleaks, trufflehog, osv-scanner, Trivy, cosign, Scorecard ở mục 12 nên không thêm); GitHub search API 2/11/2026; clone `--depth 1 --filter=blob:none`, đọc LICENSE, README, docs, danh sách audit, `action.yml`. **Không cài, không chạy.**

**Trần hiện tại:**

- §4b/§4c có quality gate cho **mã** (lint, type, mutation, Lighthouse) và vài mẩu supply chain (pin SHA, hash-locked tool, syft, gitleaks); thiếu **chuẩn đích** để biết "đủ" là mức nào.
- **Chính file workflow CI không được lint bảo mật**: chưa có công cụ bắt template injection, `pull_request_target` nguy hiểm, quyền `GITHUB_TOKEN` thừa, Action không pin. Vụ Trivy (mục 12 §3d) và act (§6g) cho thấy CI là bề mặt tấn công chính.
- Có SBOM (syft) nhưng chưa có bước **quét SBOM đó** và chưa có **giám sát lúc runner chạy** (egress, file bị sửa).

| Repo / chuẩn | Lớp | ★ · license (2/11/2026) | Commit cuối | Vì sao nâng trần | Rủi ro |
|---|---|---|---|---|---|
| `slsa-framework/slsa` | Chuẩn | 2,0k · Community Specification License 1.0 (GitHub: NOASSERTION) | 28/10/2026 | Đặc tả SLSA của OpenSSF. **v1.2 được duyệt 24/11/2025** (`www/_data/versions.yml`: `current: v1.2`, blog announce-slsa-v1.2), gồm Build track và **Source track** mới; bản nháp đang làm thêm Dependency track, Build Environment track, "Verified Properties". Cho đích đo được: Build L1 (có provenance) → L2 (nền tảng ký) → L3 (build cách ly) | Là đặc tả, cần công cụ khác để đạt (GitHub artifact attestations, slsa-github-generator, cosign). Các track mới ngoài Build/Source còn ở bản nháp |
| `zizmorcore/zizmor` | Cổng máy | 6,9k · MIT | 2/11/2026 | Phân tích tĩnh bảo mật GitHub Actions, viết bằng Rust; 41 audit (`template-injection`, `dangerous-triggers`, `excessive-permissions`, `unpinned-uses`, `impostor-commit`, `cache-poisoning`, `known-vulnerable-actions`, `dependabot-cooldown`…); chế độ offline/online, xuất SARIF để hiện trên Code Scanning. Giskard và Supabase đã dùng (mục 07, §6g) | Bản 1.31.1, nhánh chính đang 1.32.0-rc; audit online cần `GH_TOKEN`. Chỉ cho GitHub Actions |
| `rhysd/actionlint` | Cổng máy | 4,4k · MIT | 19/4/2026 (push 16/7) | Lint **đúng cú pháp/kiểu** cho workflow: kiểm kiểu biểu thức `${{ }}`, gọi shellcheck và pyflakes cho `run:`, cảnh báo input không tin cậy dùng thẳng trong script. Bổ sung cho zizmor (zizmor thiên về bảo mật) | Nhịp chậm lại (commit cuối 4/2026); một người bảo trì chính |
| `anchore/grype` | Cổng máy | 13,2k · Apache-2.0 | 30/10/2026 | Quét lỗ hổng cho image, filesystem và **SBOM của syft** (`grype sbom:./sbom.json`); xếp ưu tiên theo **EPSS, KEV**, lọc bằng OpenVEX. Ghép thẳng với syft đã có ở §4b | Trùng phần lớn với osv-scanner/Trivy (mục 12); chọn một làm cổng chính để tránh nhiễu |
| `step-security/harden-runner` | Cổng máy (runtime) | 1,3k · Apache-2.0 | 27/10/2026 | Agent giám sát runner GitHub Actions: ghi egress, file bị sửa, process; chế độ `egress-policy: block` với allowlist domain. README liệt kê vụ đã bắt được: tj-actions/changed-files (CVE-2025-30066), Trivy v0.69.4, axios npm, nx. Mã action kiểm checksum agent (`src/checksum.ts`) | **Bản free chỉ cho repo public trên runner GitHub-hosted**; repo private hay self-hosted phải trả phí. Gửi telemetry về API StepSecurity, chỉ tắt được (`disable-telemetry`) khi đã ở chế độ block |

**Stack nâng trần** (lợi ích/công sức giảm dần):

1. **Lint workflow ở mọi PR:** `actionlint` (đúng) + `zizmor --format=sarif` (an toàn) làm required check trong job `quality-gate` của §4b; sửa theo audit `unpinned-uses` khớp luôn quy tắc "Action pin SHA" đã có.
2. **Quyền tối thiểu cho CI:** `permissions: {}` ở đầu workflow, mở theo job; bỏ `pull_request_target` có checkout mã PR. zizmor `excessive-permissions`/`dangerous-triggers` giữ quy tắc này khỏi trôi.
3. **SBOM → quét → chặn:** syft sinh SBOM (§4b) → `grype sbom:` với ngưỡng mức nghiêm trọng, ưu tiên mục có KEV/EPSS cao; Renovate (§4c) mở PR vá, đặt độ trễ để tránh bản độc vừa phát hành (zizmor có audit `dependabot-cooldown` cho Dependabot).
4. **Đặt đích SLSA:** tối thiểu Build L2 (provenance do nền tảng ký, vd. GitHub artifact attestations hoặc cosign mục 12 §3d), đích L3 cho artifact phát hành; theo Source track v1.2 thì rulesets-as-code (§4b) là bằng chứng phía mã nguồn.
5. **Giám sát runner:** repo public dùng harden-runner `egress-policy: audit` vài tuần rồi chuyển `block`; repo private cân nhắc chi phí hoặc tự giới hạn egress ở runner self-hosted. Chấm lại tổng thể bằng OpenSSF Scorecard (mục 12 §3d).

**Nguồn §6h:** GitHub search API 2/11/2026 (`repo:` gộp) · `data/projects.json` (grep `repo`) · clone `--depth 1 --filter=blob:none`: slsa-framework/slsa (HEAD 4d3f9d4, 28/10/2026; LICENSE.md, `spec/whats-new.md`, `spec/` danh sách track, `www/_data/versions.yml`, `www/_posts/`), zizmorcore/zizmor (HEAD fbf8d0c, 2/11/2026; LICENSE, Cargo.toml, `docs/{usage,release-notes}.md`, `crates/zizmor/src/audit/`), rhysd/actionlint (HEAD 011a6d1, 19/4/2026; LICENSE.txt, README.md), anchore/grype (HEAD cb4a51d, 30/10/2026; LICENSE, README.md), step-security/harden-runner (HEAD 46b06ce, 27/10/2026; LICENSE, README.md, action.yml, `src/checksum.ts`, `src/bravo-config.ts`) · https://github.com/slsa-framework/slsa · https://slsa.dev/spec/v1.2/ · https://github.com/zizmorcore/zizmor · https://github.com/rhysd/actionlint · https://github.com/anchore/grype · https://github.com/step-security/harden-runner

## 6i. Nâng trần toàn diện 2/11/2026: môi trường dev, build và release tái lập

> Metadata GitHub đọc 2/11/2026, ba repo chưa archive; clone nông và đọc LICENSE, CI, lock/config và implementation. **Chỉ đọc mã, không cài Nix/devenv, không build, không phát hành.** Phân biệt môi trường khai báo, artifact tái lập và provenance có chữ ký: ba loại bằng chứng bổ sung nhau.

**Trần hiện tại:** §4c có quality gates/toolchain, §6g có Dagger, §6h có SLSA/scan/runner hardening. Chưa có hồ sơ đủ sâu về môi trường dev ghim đầu vào và pipeline đưa *đúng artifact đã kiểm* tới người dùng. [Định nghĩa Reproducible Builds](https://reproducible-builds.org/docs/definition/) yêu cầu tạo lại artifact giống từng bit dưới điều kiện đã công bố; có lockfile hoặc provenance chưa tự chứng minh điều đó.

| Dự án | ★ · license (đọc 2/11/2026) | HEAD / ngày commit | Lớp và điều kiện dùng |
|---|---|---|---|
| [Nix](https://github.com/NixOS/nix) | 17,960 · LGPL-2.1 | `b64c28c2134f` · 2026-11-02 | Package/build manager Unix; pin inputs và sandbox, vẫn cần build lại so hash để chứng minh tái lập |
| [devenv](https://github.com/cachix/devenv) | 7,794 · Apache-2.0 | `0d6c556e5f86` · 2026-10-28 | Môi trường dev khai báo trên Nix với lock/packages/services/tests; không tự cách ly tác dụng phụ service |
| [GoReleaser](https://github.com/goreleaser/goreleaser) | 16,131 · MIT | `3d5c3a2efe15` · 2026-11-01 | Release pipeline đa nền tảng; phân biệt bản OSS và Pro trong chính cấu hình upstream |

### Nix

Package/build manager của cộng đồng Nix, LGPL v2.1 theo [COPYING](https://github.com/NixOS/nix/blob/b64c28c2134f5b6e4900e423ec281a2985e57086/COPYING). Inputs/derivation và store giúp ghim toolchain, chia sẻ cache và build trong môi trường kiểm soát. [Build command](https://github.com/NixOS/nix/blob/b64c28c2134f5b6e4900e423ec281a2985e57086/src/nix/build.cc) có `--rebuild` đi qua `bmCheck`; [Build goal](https://github.com/NixOS/nix/blob/b64c28c2134f5b6e4900e423ec281a2985e57086/src/libstore/build/derivation-building-goal.cc) có đường kiểm output đã tồn tại. Khi cần chứng minh tái lập, buộc build lại và đối chiếu output, không chỉ tải lại cùng binary cache. Cần ghim Nix/nixpkgs/input lock, platform, flags và trạng thái sandbox. Timestamp, đường dẫn, mạng, CPU/tool nondeterminism vẫn có thể làm output khác; Nix không bảo đảm mọi package tái lập. Không cần chuyển cả hệ điều hành sang NixOS để dùng Nix; Linux/macOS có khác biệt sandbox, Windows thường qua WSL.

### devenv

Lớp khai báo môi trường dev trên Nix của Cachix: package/ngôn ngữ, service, task và hook trong cấu hình, dependency pin ở lock. [Test module](https://github.com/cachix/devenv/blob/0d6c556e5f862c14a75a543e2ee4fdb7acc005ad/src/modules/tests.nix) nối `enterTest` với lifecycle/readiness của process; [CI test](https://github.com/cachix/devenv/blob/0d6c556e5f862c14a75a543e2ee4fdb7acc005ad/.github/workflows/test.yml) thực sự gọi `devenv test`. Giá trị là dùng cùng định nghĩa dev/CI, so với Dagger thiên pipeline container. Shell hook và service vẫn chạy mã, DB state/secret vẫn phải quản lý riêng; lock không làm database fixture bất biến. Với nhiều agent/worktree, tách cổng/service data và định danh môi trường trước khi chạy song song. Các tính năng giao diện/cloud không phải điều kiện để dùng bản Apache-2.0 này.

### GoReleaser

Release engineering đa nền tảng, mã trong repo MIT; có bản Pro thương mại. [Cấu hình tự phát hành](https://github.com/goreleaser/goreleaser/blob/3d5c3a2efe1544b8f7d24a8c2ed10dab45b89a61/.goreleaser.yaml) mở bằng `pro: true`, nên sao chép toàn bộ file không bảo đảm chạy với bản OSS. Trong cấu hình có `-trimpath`, timestamp theo commit, checksum/SBOM/signing; [Checksum pipe](https://github.com/goreleaser/goreleaser/blob/3d5c3a2efe1544b8f7d24a8c2ed10dab45b89a61/internal/pipe/checksums/checksums.go) triển khai băm và sắp thứ tự danh sách. [Release verification](https://github.com/goreleaser/goreleaser/blob/3d5c3a2efe1544b8f7d24a8c2ed10dab45b89a61/.github/workflows/release.yml) tải artifact, kiểm checksum, cosign identity/issuer và GitHub attestation: đây là mẫu kiểm ở phía người nhận đáng học. Dùng GoReleaser đóng gói binary đã qua kiểm, ghim edition/version và tách quyền build với publish. Phải tự kiểm artifact đa kiến trúc/installer; chữ ký đúng không chứng minh ứng dụng đúng hay build tái lập.

**Kiến trúc tham khảo:** source commit + input lock → môi trường Nix/devenv hoặc Dagger hiện có → lint/test/eval → build candidate → rebuild độc lập → so artifact → SBOM/provenance/signature → publish chính candidate ấy. Khi signing/notarization tạo byte biến động, công bố rõ artifact được so và lớp ký ngoài thay vì tuyên bố cả gói giống bit. Devcontainer/container có thể là lựa chọn đủ dùng nếu team chỉ cần môi trường đồng nhất; Nix phù hợp khi cần biểu diễn/ghim dependency sâu hơn.

| Cổng tại dự án tích hợp | Đạt khi | Không thay được bởi |
|---|---|---|
| Môi trường dev/CI | Checkout mới vào môi trường đã ghim, cùng lệnh kiểm chạy được | README ghi “works on my machine” |
| Input closure | Toolchain, dependency, image và nguồn tải đều có phiên bản/hash; thay lock được review | Chỉ ghim package manager |
| Tái lập artifact | Hai build sạch có cùng điều kiện công bố cho cùng hash; khác thì giữ diff/báo cáo | Hai lần tải cùng cache |
| Nguồn gốc artifact | Verify chữ ký/issuer/identity/source commit ở phía nhận | Chỉ sinh provenance rồi không kiểm |
| Phát hành | Hash artifact kiểm thử khớp artifact phát hành; rollback/version có kiểm | Rebuild lại lúc publish mà không đối chiếu |

**Đối chiếu ba cột:** đã có và sâu hơn: gate mã/supply chain (§4c/§6h); đã có nhưng mỏng hơn: môi trường dev nhất quán và liên kết build–release; mới: hồ sơ Nix/devenv/GoReleaser với cổng tái lập và xác minh phía nhận. Không khuyến nghị dùng cùng lúc mọi build system; chọn một đường có bằng chứng và chi phí vận hành phù hợp.

**Nguồn §6i:** [CI Nix](https://github.com/NixOS/nix/blob/b64c28c2134f5b6e4900e423ec281a2985e57086/.github/workflows/ci.yml); [devenv LICENSE](https://github.com/cachix/devenv/blob/0d6c556e5f862c14a75a543e2ee4fdb7acc005ad/LICENSE), [devenv lock](https://github.com/cachix/devenv/blob/0d6c556e5f862c14a75a543e2ee4fdb7acc005ad/devenv.lock); [GoReleaser LICENSE](https://github.com/goreleaser/goreleaser/blob/3d5c3a2efe1544b8f7d24a8c2ed10dab45b89a61/LICENSE.md), [GoReleaser build CI](https://github.com/goreleaser/goreleaser/blob/3d5c3a2efe1544b8f7d24a8c2ed10dab45b89a61/.github/workflows/build.yml); [Nix how it works](https://nixos.org/guides/how-nix-works/), [devenv basics](https://devenv.sh/basics/), [GoReleaser Go build](https://goreleaser.com/customization/builds/builders/go/), [định nghĩa tái lập](https://reproducible-builds.org/docs/definition/).

## 6j. Nâng sâu 4/11/2026: hợp đồng toolchain và lệnh chuẩn của xưởng

**Trần hiện tại:** mục này đã có môi trường tái lập, IaC, release và lint. Lớp còn thiếu là cách cùng một repository chỉ ra toolchain và lệnh chuẩn cho người, IDE, coding agent và CI; cập nhật môi trường phải đi qua diff review được. Triển khai nền tảng/rollback xem [mục 32](../32-platform-delivery-engineering/README.md), còn chứng thực build xem [mục 31](../31-software-supply-chain-security/README.md).

<a id="factory-2026-11-04-mise"></a>

### mise: khóa toolchain, không thay lockfile dependency của ứng dụng

| Thuộc tính | Kết quả đọc |
|---|---|
| Repo · license · SHA | `jdx/mise` · MIT · `02d59ef93faf219319cccac23249501e8763e2da` |
| Cơ chế đã đọc | `mise.toml` khai báo tools/tasks/env; `mise lock` ghi version cùng URL/checksum khi backend cung cấp; `mise install --locked` yêu cầu dùng dữ liệu lock theo phạm vi cấu hình |
| Đường gọi | `src/cli/install.rs` truyền `ResolveOptions.use_locked_version` và trạng thái `Settings.locked`; `src/cli/lock.rs` có trust check và từ chối khóa phiên bản không xác minh được khi truy vấn version thất bại |
| Ranh giới | Lock tool không khóa package của app: vẫn giữ npm/uv/Cargo lock. Download checksum còn phụ thuộc backend/platform; lock có version nhưng thiếu digest không đồng nghĩa byte-for-byte reproducible |
| Cấu hình thực thi | Template `exec`, hook, env directives và postinstall có thể chạy mã. Trust là quyết định cho phép config, không phải sandbox hay kiểm duyệt tool upstream; phải review trước khi trust |
| CI | `test.yml` tách luồng trusted/untrusted rồi gọi `test-impl.yml`; không suy việc này thành mọi task của người dùng được cách ly |

**Phạm vi kiểm (2026-11-04):** đọc tài liệu, LICENSE, mã đường gọi và workflow tại SHA dưới đây; không cài/chạy upstream. Các cổng nghiệm thu là đề xuất cho repo tích hợp, chưa phải kết quả chạy của kho. Số sao không thu thập trong đợt này.

| Lựa chọn | Giá trị chính | Chọn khi |
|---|---|---|
| mise | Tool versions + task/env ở nhiều hệ sinh thái | Đội cần điểm vào gọn cho runtime/linter/codegen; kiểm đủ platform và backend |
| Nix | Mô tả build/dev shell và store theo đầu vào | Cần khóa cả dependency hệ thống và chấp nhận học mô hình Nix; đánh giá impurity/network riêng |
| devenv | Trải nghiệm môi trường dev dựa trên Nix | Cần dịch vụ dev và shell tiện dụng trên nền Nix |
| Dev Containers | Cấu hình môi trường IDE/container | Cần host/IDE thống nhất; image/features vẫn phải pin và kiểm provenance |

**Stack cho xưởng:** khóa bootstrap của tool manager → review `mise.toml` và task graph → tạo lock cho từng platform dùng thật → install locked → cài dependency app bằng frozen lock → chạy cùng task lint/test/build ở local và CI. Tách task cần secret khỏi PR không tin cậy; ghi tool versions, lock digest và target vào báo cáo.

**Cổng nghiệm thu:** máy sạch và runner mới chạy cùng entrypoint cho kết quả chức năng tương đương; lock không đủ platform/backend phải làm fail rõ thay vì âm thầm chọn latest. Thử thay cấu hình, artifact digest và quyền mạng để chứng minh cổng phát hiện sai lệch. Build thành công chỉ là một lớp; kiểm test count, artifact checksum, SBOM và deployment smoke ở các mục 30–32. Cache hit không được bỏ qua xác minh input.

**Nguồn §6j:** [LICENSE](https://github.com/jdx/mise/blob/02d59ef93faf219319cccac23249501e8763e2da/LICENSE) · [lock contract](https://github.com/jdx/mise/blob/02d59ef93faf219319cccac23249501e8763e2da/docs/dev-tools/mise-lock.md) · [trust/security](https://github.com/jdx/mise/blob/02d59ef93faf219319cccac23249501e8763e2da/docs/security.md) · [install callsite](https://github.com/jdx/mise/blob/02d59ef93faf219319cccac23249501e8763e2da/src/cli/install.rs) · [lock implementation](https://github.com/jdx/mise/blob/02d59ef93faf219319cccac23249501e8763e2da/src/cli/lock.rs) · [CI](https://github.com/jdx/mise/blob/02d59ef93faf219319cccac23249501e8763e2da/.github/workflows/test.yml).

<a id="anhkysuai-2026-11-23"></a>

## Đánh giá từ kho Anh Kỹ Sư AI — 23/11/2026

Phần này có **167 hồ sơ hoặc phạm vi đối chiếu** từ [nguồn tuyển chọn](https://anhkysuai.com/kho/). [Bảng đủ 1.295 repo](../data/collections/anhkysuai-kho.json) ghi trạng thái đối chiếu từng link; [danh sách URL](../data/collections/anhkysuai-kho-links.txt) phục vụ tra cứu. Nguồn tuyển chọn giúp phát hiện repo; đánh giá bên dưới dựa trên clone và permalink upstream cùng metadata GitHub ngày 2026-11-23.

Mức `docs-read`/`code-read` chỉ áp dụng phạm vi ghi tại mỗi hồ sơ. Chưa cài, build, chạy test hay benchmark mã upstream. Giấy phép có thể tách theo code, model, nội dung, asset hoặc bản enterprise; con số/tuyên bố của tác giả chưa được tái lập nếu không có ghi chú khác.

<a id="anhkysuai-2026-11-23-formatjs"></a>

### FormatJS

**Repo:** [formatjs/formatjs](https://github.com/formatjs/formatjs) · **License:** BSD-3-Clause cho react-intl; MIT cho CLI; theo từng package · **★ 14,755 (GitHub API, 2026-11-23)**

**Mục đích:** Hệ thư viện định dạng thông điệp, số/ngày và quốc tế hóa cho nhiều runtime.

**Giá trị và cơ chế:** README phân phối JS/TS, Rust, Python và React Native; React Intl cùng CLI hỗ trợ đưa thông điệp và Intl API vào pipeline ứng dụng.

**Giới hạn:** Không có một license duy nhất cho toàn monorepo: đã đọc react-intl BSD-3-Clause và CLI MIT. Chưa kiểm mọi package, locale hay tương thích runtime; đây không phải dịch vụ dịch tự động.

**Cách tham khảo/tích hợp:** Chọn package đúng framework, tách catalog bản dịch và kiểm số nhiều/ngày/tiền tệ theo locale mục tiêu.

**Thay thế:** [i18next](../06-ui-ux-design/README.md#i18n-lifecycle-2026-11-02), [Lingui](../06-ui-ux-design/README.md#i18n-lifecycle-2026-11-02), fluent.

**Bằng chứng:** `docs-read`, ngày 2026-11-23, commit [`e6c25c2dba0b`](https://github.com/formatjs/formatjs/commit/e6c25c2dba0bbe72fa74f46b8014693d0d549719). README và các tài liệu/manifest/CI hiện diện, đọc chọn lọc; chưa kiểm implementation. Chưa cài/chạy upstream.

**Nguồn:** [README.md](https://github.com/formatjs/formatjs/blob/e6c25c2dba0bbe72fa74f46b8014693d0d549719/README.md) · [packages/cli/LICENSE.md](https://github.com/formatjs/formatjs/blob/e6c25c2dba0bbe72fa74f46b8014693d0d549719/packages/cli/LICENSE.md) · [Cargo.toml](https://github.com/formatjs/formatjs/blob/e6c25c2dba0bbe72fa74f46b8014693d0d549719/Cargo.toml) · [packages/react-intl/LICENSE.md](https://github.com/formatjs/formatjs/blob/e6c25c2dba0bbe72fa74f46b8014693d0d549719/packages/react-intl/LICENSE.md) · [metadata GitHub](https://api.github.com/repos/formatjs/formatjs).

<a id="anhkysuai-2026-11-23-kiss-translator"></a>

### KISS Translator

**Repo:** [fishjar/kiss-translator](https://github.com/fishjar/kiss-translator) · **License:** GPL-3.0 · **★ 13,495 (GitHub API, 2026-11-23)**

**Mục đích:** Tiện ích và userscript dịch song ngữ webpage, lựa chọn văn bản và phụ đề.

**Giá trị và cơ chế:** README tách dịch vụ theo năng lực, plugin API, đối chiếu nhiều bản dịch và model local; thích hợp tham khảo giao diện đọc song ngữ với provider tùy chọn.

**Giới hạn:** Tính năng mới như file/local AI chỉ có ở extension, không tự có trong userscript. Chưa kiểm quyền mạng hay chất lượng tiếng Việt; provider cloud nhận nội dung và weights local có điều kiện riêng.

**Cách tham khảo/tích hợp:** Chọn engine theo ngôn ngữ, giới hạn site và kiểm bố cục bản gốc/bản dịch trên trang thực.

**Thay thế:** immersive-translate, easydict, [Translate for Zotero](../16-docs-tools/README.md#anhkysuai-2026-11-23-zotero-pdf-translate).

**Bằng chứng:** `docs-read`, ngày 2026-11-23, commit [`8696ab9e9b2f`](https://github.com/fishjar/kiss-translator/commit/8696ab9e9b2f6f4d90960e7c1d3c1bf0aa989a20). README và các tài liệu/manifest/CI hiện diện, đọc chọn lọc; chưa kiểm implementation. Chưa cài/chạy upstream.

**Nguồn:** [README.md](https://github.com/fishjar/kiss-translator/blob/8696ab9e9b2f6f4d90960e7c1d3c1bf0aa989a20/README.md) · [LICENSE](https://github.com/fishjar/kiss-translator/blob/8696ab9e9b2f6f4d90960e7c1d3c1bf0aa989a20/LICENSE) · [metadata GitHub](https://api.github.com/repos/fishjar/kiss-translator).

<a id="anhkysuai-2026-11-23-identity-react"></a>

### React: đối chiếu tên repo

**Kết luận:** [facebook/react](https://github.com/facebook/react) và [react/react](https://github.com/react/react) là cùng thực thể GitHub, repository ID `10270250` theo API ngày 2026-11-23. Giữ ID catalog `react` và hồ sơ gốc; cập nhật đường dẫn chuẩn, không thêm hồ sơ trùng.

**Phạm vi đọc lại:** `docs-read`; clone tại commit [`33e52451f2ab39e0a4d186256b2b4d55277e6041`](https://github.com/react/react/commit/33e52451f2ab39e0a4d186256b2b4d55277e6041) và đọc tài liệu được dẫn. GitHub get_repo cho facebook/react chuyển tới react/react, cùng repository ID 10270250; catalog đã có hồ sơ react. Không tạo thực thể thứ hai. Những nhận định kỹ thuật cũ ở các phần trước giữ ngày/phạm vi cũ; lượt đối chiếu này chưa tái kiểm toàn bộ implementation hoặc chạy upstream.

**Metadata:** ★ 252,940 (GitHub API, 2026-11-23); commit ngày 2026-11-21. Trạng thái archived là `false`, không dùng riêng cờ này để kết luận mức bảo trì.

**Nguồn:** [README.md](https://github.com/react/react/blob/33e52451f2ab39e0a4d186256b2b4d55277e6041/README.md) · [LICENSE](https://github.com/react/react/blob/33e52451f2ab39e0a4d186256b2b4d55277e6041/LICENSE) · [package.json](https://github.com/react/react/blob/33e52451f2ab39e0a4d186256b2b4d55277e6041/package.json) · [runtime_fuzz_tests.yml](https://github.com/react/react/blob/33e52451f2ab39e0a4d186256b2b4d55277e6041/.github/workflows/runtime_fuzz_tests.yml) · [react](https://api.github.com/repos/react/react) · [react](https://api.github.com/repos/facebook/react).

<a id="anhkysuai-2026-11-23-identity-react-native"></a>

### React Native: đối chiếu tên repo

**Kết luận:** [facebook/react-native](https://github.com/facebook/react-native) và [react/react-native](https://github.com/react/react-native) là cùng thực thể GitHub, repository ID `29028775` theo API ngày 2026-11-23. Giữ ID catalog `react-native` và hồ sơ gốc; cập nhật đường dẫn chuẩn, không thêm hồ sơ trùng.

**Phạm vi đọc lại:** `docs-read`; clone tại commit [`3f00329b50fd2e8d3fb6bc29fc87e2f38db6ac2a`](https://github.com/react/react-native/commit/3f00329b50fd2e8d3fb6bc29fc87e2f38db6ac2a) và đọc tài liệu được dẫn. GitHub get_repo cho facebook/react-native chuyển tới react/react-native, cùng repository ID 29028775; catalog đã có hồ sơ react-native. Không tạo thực thể thứ hai. Những nhận định kỹ thuật cũ ở các phần trước giữ ngày/phạm vi cũ; lượt đối chiếu này chưa tái kiểm toàn bộ implementation hoặc chạy upstream.

**Metadata:** ★ 126,999 (GitHub API, 2026-11-23); commit ngày 2026-11-22. Trạng thái archived là `false`, không dùng riêng cờ này để kết luận mức bảo trì.

**Nguồn:** [README.md](https://github.com/react/react-native/blob/3f00329b50fd2e8d3fb6bc29fc87e2f38db6ac2a/README.md) · [LICENSE](https://github.com/react/react-native/blob/3f00329b50fd2e8d3fb6bc29fc87e2f38db6ac2a/LICENSE) · [package.json](https://github.com/react/react-native/blob/3f00329b50fd2e8d3fb6bc29fc87e2f38db6ac2a/package.json) · [test-all.yml](https://github.com/react/react-native/blob/3f00329b50fd2e8d3fb6bc29fc87e2f38db6ac2a/.github/workflows/test-all.yml) · [react-native](https://api.github.com/repos/react/react-native) · [react-native](https://api.github.com/repos/facebook/react-native).

<a id="anhkysuai-burntsushi-ripgrep"></a>

### ripgrep

- **Repo:** [BurntSushi/ripgrep](https://github.com/BurntSushi/ripgrep).
- **Mục đích:** CLI tìm biểu thức chính quy trong cây thư mục, dùng được trên Windows, macOS và Linux.
- **Điểm đáng dùng:** README nêu cơ chế mặc định tôn trọng gitignore, bỏ file ẩn và nhị phân; Cargo chia riêng matcher, searcher, printer và ignore, hữu ích làm lớp tìm kiếm tất định cho agent.
- **License:** MIT OR Unlicense.
- **Giới hạn:** Một truy vấn không thấy kết quả chưa chứng minh mã không tồn tại vì bộ lọc mặc định; dùng cờ mở rộng có chủ đích. Không tái lập bảng benchmark của tác giả.
- **Tích hợp:** Dùng binary rg, ghi rõ cờ, thư mục gốc và phạm vi bỏ qua khi đưa kết quả cho agent.
- **Đối chiếu:** git grep cho file đã theo dõi; GNU grep cho tính sẵn có; The Silver Searcher cho tìm kiếm code.
- **Mức kiểm chứng:** `docs-read` — Đọc các phần mô tả và giới hạn trong README, thông báo license, metadata manifest và cấu hình CI khi có; chưa đọc toàn bộ mã triển khai, chưa cài hoặc chạy kiểm thử upstream.
- **Snapshot:** kiểm ngày 2026-11-23; commit `4a51093f78bfbef86d89275f4916fd6b6039fe9e` (2026-11-22T18:03:56-05:00); 70,184 sao theo GitHub API ngày 2026-11-23. Sao không đại diện chất lượng.
- **Bằng chứng:** [README.md](https://github.com/BurntSushi/ripgrep/blob/4a51093f78bfbef86d89275f4916fd6b6039fe9e/README.md) · [COPYING](https://github.com/BurntSushi/ripgrep/blob/4a51093f78bfbef86d89275f4916fd6b6039fe9e/COPYING) · [LICENSE-MIT](https://github.com/BurntSushi/ripgrep/blob/4a51093f78bfbef86d89275f4916fd6b6039fe9e/LICENSE-MIT) · [Cargo.toml](https://github.com/BurntSushi/ripgrep/blob/4a51093f78bfbef86d89275f4916fd6b6039fe9e/Cargo.toml) · [.github/workflows/ci.yml](https://github.com/BurntSushi/ripgrep/blob/4a51093f78bfbef86d89275f4916fd6b6039fe9e/.github/workflows/ci.yml) · [GitHub API](https://api.github.com/repos/BurntSushi/ripgrep).

<a id="anhkysuai-alacritty-alacritty"></a>

### Alacritty

- **Repo:** [alacritty/alacritty](https://github.com/alacritty/alacritty).
- **Mục đích:** Terminal dùng OpenGL, chạy trên BSD, Linux, macOS và Windows.
- **Điểm đáng dùng:** Workspace tách terminal core khỏi lớp ứng dụng và cấu hình; CI có kiểm tra core không dùng default features, giúp tham khảo cách chia engine với giao diện.
- **License:** Apache-2.0; thành phần MIT theo thông báo riêng.
- **Giới hạn:** README vẫn tự ghi beta; cần OpenGL ES 2.0, Windows cần ConPTY. Tốc độ được tác giả công bố, chưa benchmark trong đợt này. Manifest alacritty và alacritty_terminal ghi Apache-2.0; không coi hai LICENSE ở root là quyền lựa chọn MIT cho toàn repo.
- **Tích hợp:** Dùng binary phát hành hoặc gói hệ thống; cấu hình bằng TOML và ghép với multiplexer bên ngoài nếu cần.
- **Đối chiếu:** [WezTerm](../13-dev-stack-devops/README.md#anhkysuai-wezterm-wezterm) cho nhiều chức năng tích hợp; [kitty](../13-dev-stack-devops/README.md#anhkysuai-kovidgoyal-kitty) cho hệ terminal phong phú; Windows Terminal cho môi trường Windows.
- **Mức kiểm chứng:** `docs-read` — Đọc các phần mô tả và giới hạn trong README, thông báo license, metadata manifest và cấu hình CI khi có; chưa đọc toàn bộ mã triển khai, chưa cài hoặc chạy kiểm thử upstream.
- **Snapshot:** kiểm ngày 2026-11-23; commit `791efff6d74c66bee390c259e322626ca93aadb6` (2026-11-18T16:50:57+01:00); 66,272 sao theo GitHub API ngày 2026-11-23. Sao không đại diện chất lượng.
- **Bằng chứng:** [README.md](https://github.com/alacritty/alacritty/blob/791efff6d74c66bee390c259e322626ca93aadb6/README.md) · [LICENSE-APACHE](https://github.com/alacritty/alacritty/blob/791efff6d74c66bee390c259e322626ca93aadb6/LICENSE-APACHE) · [LICENSE-MIT](https://github.com/alacritty/alacritty/blob/791efff6d74c66bee390c259e322626ca93aadb6/LICENSE-MIT) · [Cargo.toml](https://github.com/alacritty/alacritty/blob/791efff6d74c66bee390c259e322626ca93aadb6/Cargo.toml) · [.github/workflows/ci.yml](https://github.com/alacritty/alacritty/blob/791efff6d74c66bee390c259e322626ca93aadb6/.github/workflows/ci.yml) · [alacritty/Cargo.toml](https://github.com/alacritty/alacritty/blob/791efff6d74c66bee390c259e322626ca93aadb6/alacritty/Cargo.toml) · [alacritty_terminal/Cargo.toml](https://github.com/alacritty/alacritty/blob/791efff6d74c66bee390c259e322626ca93aadb6/alacritty_terminal/Cargo.toml) · [GitHub API](https://api.github.com/repos/alacritty/alacritty).

<a id="anhkysuai-webpack-webpack"></a>

### webpack

- **Repo:** [webpack/webpack](https://github.com/webpack/webpack).
- **Mục đích:** Bundler JavaScript và tài nguyên web với hệ loader, plugin và chia chunk.
- **Điểm đáng dùng:** README mô tả ghép ESM/CommonJS/AMD và tải chunk bất đồng bộ; cấu trúc lib, schemas, hot cùng entry CLI thể hiện vai trò compiler có thể mở rộng.
- **License:** MIT.
- **Giới hạn:** Cấu hình loader và plugin làm tăng diện tích phụ thuộc; phải kiểm bundle thật theo ứng dụng, chưa xác minh hiệu năng hoặc tree shaking trong phiên này.
- **Tích hợp:** Cài webpack ở devDependencies, ghim loader/plugin và lưu cấu hình build trong repo sản phẩm.
- **Đối chiếu:** [Vite](../13-dev-stack-devops/README.md) cho vòng lặp phát triển; [esbuild](../13-dev-stack-devops/README.md#anhkysuai-evanw-esbuild) cho build gọn; Rollup cho đóng gói thư viện.
- **Mức kiểm chứng:** `docs-read` — Đọc các phần mô tả và giới hạn trong README, thông báo license, metadata manifest và cấu hình CI khi có; chưa đọc toàn bộ mã triển khai, chưa cài hoặc chạy kiểm thử upstream.
- **Snapshot:** kiểm ngày 2026-11-23; commit `bd75318efdf58618fcc4167f654d6f8824a0858b` (2026-11-23T11:32:56+03:00); 66,023 sao theo GitHub API ngày 2026-11-23. Sao không đại diện chất lượng.
- **Bằng chứng:** [README.md](https://github.com/webpack/webpack/blob/bd75318efdf58618fcc4167f654d6f8824a0858b/README.md) · [LICENSE](https://github.com/webpack/webpack/blob/bd75318efdf58618fcc4167f654d6f8824a0858b/LICENSE) · [package.json](https://github.com/webpack/webpack/blob/bd75318efdf58618fcc4167f654d6f8824a0858b/package.json) · [.github/workflows/test.yml](https://github.com/webpack/webpack/blob/bd75318efdf58618fcc4167f654d6f8824a0858b/.github/workflows/test.yml) · [GitHub API](https://api.github.com/repos/webpack/webpack).

<a id="anhkysuai-termux-termux-app"></a>

### Termux app

- **Repo:** [termux/termux-app](https://github.com/termux/termux-app).
- **Mục đích:** Ứng dụng terminal và môi trường Linux trên Android; repo này chứa giao diện và terminal emulator.
- **Điểm đáng dùng:** README tách app khỏi kho gói termux-packages và liệt kê plugin API/Boot/Tasker; workflow chạy kiểm Gradle, hữu ích làm ví dụ shell tích hợp trên thiết bị di động.
- **License:** GPL-3.0-only; thành phần terminal có ngoại lệ Apache-2.0.
- **Giới hạn:** Android 12 trở lên có thể diệt tiến trình; app và plugin phải cùng nguồn ký. GPL và các ngoại lệ thành phần cần được giữ riêng khi tái phân phối.
- **Tích hợp:** Cài từ nguồn phát hành chính thức thống nhất, kiểm phiên bản Android và không trộn APK có chữ ký khác nhau.
- **Đối chiếu:** Android shell qua ADB cho bảo trì; UserLAnd cho distro Linux; terminal SSH khi công việc chạy trên máy chủ.
- **Mức kiểm chứng:** `docs-read` — Đọc các phần mô tả và giới hạn trong README, thông báo license, metadata manifest và cấu hình CI khi có; chưa đọc toàn bộ mã triển khai, chưa cài hoặc chạy kiểm thử upstream.
- **Snapshot:** kiểm ngày 2026-11-23; commit `8629e632fcb95da272221be327db653fb24befe9` (2026-09-26T10:11:43+05:00); 65,516 sao theo GitHub API ngày 2026-11-23. Sao không đại diện chất lượng.
- **Bằng chứng:** [README.md](https://github.com/termux/termux-app/blob/8629e632fcb95da272221be327db653fb24befe9/README.md) · [LICENSE.md](https://github.com/termux/termux-app/blob/8629e632fcb95da272221be327db653fb24befe9/LICENSE.md) · [build.gradle](https://github.com/termux/termux-app/blob/8629e632fcb95da272221be327db653fb24befe9/build.gradle) · [.github/workflows/run_tests.yml](https://github.com/termux/termux-app/blob/8629e632fcb95da272221be327db653fb24befe9/.github/workflows/run_tests.yml) · [GitHub API](https://api.github.com/repos/termux/termux-app).

<a id="anhkysuai-git-git"></a>

### Git

- **Repo:** [git/git](https://github.com/git/git).
- **Mục đích:** Hệ quản lý phiên bản phân tán cho lịch sử mã, nhánh và thay đổi.
- **Điểm đáng dùng:** README phân biệt lệnh cấp cao với truy cập nội bộ, dẫn tài liệu từng lệnh và quy trình gửi patch; COPYING chỉ định GPLv2 cụ thể, không mặc nhiên GPLv3.
- **License:** GPL-2.0-only; một số thành phần tương thích có điều khoản riêng.
- **Giới hạn:** Git là hạ tầng lịch sử, không thay review, kiểm thử hay backup ngoài thiết bị; nhúng hoặc phân phối mã nguồn cần xét GPL và license thành phần.
- **Tích hợp:** Dùng CLI với commit SHA, worktree và diff để đóng phạm vi công việc của agent; lưu remote và nhánh rõ ràng.
- **Đối chiếu:** Mercurial cho VCS phân tán; Fossil cho bộ công cụ tích hợp; Jujutsu cho giao diện quản lý thay đổi trên Git.
- **Mức kiểm chứng:** `docs-read` — Đọc các phần mô tả và giới hạn trong README, thông báo license, metadata manifest và cấu hình CI khi có; chưa đọc toàn bộ mã triển khai, chưa cài hoặc chạy kiểm thử upstream.
- **Snapshot:** kiểm ngày 2026-11-23; commit `f7de81456940dd6f3274e461149bba12965de609` (2026-11-19T09:11:33-08:00); 64,479 sao theo GitHub API ngày 2026-11-23. Sao không đại diện chất lượng.
- **Bằng chứng:** [README.md](https://github.com/git/git/blob/f7de81456940dd6f3274e461149bba12965de609/README.md) · [COPYING](https://github.com/git/git/blob/f7de81456940dd6f3274e461149bba12965de609/COPYING) · [Cargo.toml](https://github.com/git/git/blob/f7de81456940dd6f3274e461149bba12965de609/Cargo.toml) · [.github/workflows/check-style.yml](https://github.com/git/git/blob/f7de81456940dd6f3274e461149bba12965de609/.github/workflows/check-style.yml) · [GitHub API](https://api.github.com/repos/git/git).

<a id="anhkysuai-sharkdp-bat"></a>

### bat

- **Repo:** [sharkdp/bat](https://github.com/sharkdp/bat).
- **Mục đích:** Trình đọc file trên terminal có tô cú pháp, số dòng và dấu thay đổi Git.
- **Điểm đáng dùng:** README nêu tự chọn pager khi tương tác và chuyển sang nội dung thuần khi pipe; Cargo tách tính năng ứng dụng và tích hợp Git, hữu ích cho công cụ xem mã của agent.
- **License:** MIT OR Apache-2.0.
- **Giới hạn:** Màu, pager và ký tự điều khiển có thể làm hỏng đầu ra dùng cho máy; không nên coi bản render là nội dung byte gốc.
- **Tích hợp:** Dùng --paging=never hoặc đầu ra thuần cho pipeline, chỉ bật màu ở preview tương tác như fzf.
- **Đối chiếu:** cat cho byte thuần; less cho xem file dài; [delta](../13-dev-stack-devops/README.md#anhkysuai-dandavison-delta) cho diff Git.
- **Mức kiểm chứng:** `docs-read` — Đọc các phần mô tả và giới hạn trong README, thông báo license, metadata manifest và cấu hình CI khi có; chưa đọc toàn bộ mã triển khai, chưa cài hoặc chạy kiểm thử upstream.
- **Snapshot:** kiểm ngày 2026-11-23; commit `4bd5c5b602950ea8fe62ea16d851d6a26eccfb76` (2026-11-22T22:49:47+02:00); 61,377 sao theo GitHub API ngày 2026-11-23. Sao không đại diện chất lượng.
- **Bằng chứng:** [README.md](https://github.com/sharkdp/bat/blob/4bd5c5b602950ea8fe62ea16d851d6a26eccfb76/README.md) · [LICENSE-APACHE](https://github.com/sharkdp/bat/blob/4bd5c5b602950ea8fe62ea16d851d6a26eccfb76/LICENSE-APACHE) · [LICENSE-MIT](https://github.com/sharkdp/bat/blob/4bd5c5b602950ea8fe62ea16d851d6a26eccfb76/LICENSE-MIT) · [Cargo.toml](https://github.com/sharkdp/bat/blob/4bd5c5b602950ea8fe62ea16d851d6a26eccfb76/Cargo.toml) · [.github/workflows/CICD.yml](https://github.com/sharkdp/bat/blob/4bd5c5b602950ea8fe62ea16d851d6a26eccfb76/.github/workflows/CICD.yml) · [GitHub API](https://api.github.com/repos/sharkdp/bat).

<a id="anhkysuai-starship-starship"></a>

### Starship

- **Repo:** [starship/starship](https://github.com/starship/starship).
- **Mục đích:** Prompt có cấu hình dùng chung cho nhiều shell và hệ điều hành.
- **Điểm đáng dùng:** README tách binary khỏi bước tích hợp vào shell, yêu cầu Nerd Font để hiển thị glyph; manifest Rust và tài liệu preset phù hợp chuẩn hóa trải nghiệm terminal của đội.
- **License:** ISC.
- **Giới hạn:** Thông tin prompt có thể tốn thời gian khi kiểm repo lớn hoặc gọi công cụ ngoài; tốc độ quảng bá chưa được đo lại. Font và shell cần tương thích.
- **Tích hợp:** Cài binary từ nguồn chính thức, khởi tạo trong cấu hình shell và bật những module cần dùng.
- **Đối chiếu:** Oh My Posh cho cấu hình đa nền tảng; Powerlevel10k cho zsh; prompt shell tối giản khi ưu tiên ít phụ thuộc.
- **Mức kiểm chứng:** `docs-read` — Đọc các phần mô tả và giới hạn trong README, thông báo license, metadata manifest và cấu hình CI khi có; chưa đọc toàn bộ mã triển khai, chưa cài hoặc chạy kiểm thử upstream.
- **Snapshot:** kiểm ngày 2026-11-23; commit `9eb8412bcee3fa35e597b37e0566afb8f9c05217` (2026-11-23T08:07:12Z); 60,872 sao theo GitHub API ngày 2026-11-23. Sao không đại diện chất lượng.
- **Bằng chứng:** [README.md](https://github.com/starship/starship/blob/9eb8412bcee3fa35e597b37e0566afb8f9c05217/README.md) · [LICENSE](https://github.com/starship/starship/blob/9eb8412bcee3fa35e597b37e0566afb8f9c05217/LICENSE) · [Cargo.toml](https://github.com/starship/starship/blob/9eb8412bcee3fa35e597b37e0566afb8f9c05217/Cargo.toml) · [.github/workflows/spell-check.yml](https://github.com/starship/starship/blob/9eb8412bcee3fa35e597b37e0566afb8f9c05217/.github/workflows/spell-check.yml) · [GitHub API](https://api.github.com/repos/starship/starship).

<a id="anhkysuai-textualize-rich"></a>

### Rich

- **Repo:** [Textualize/rich](https://github.com/Textualize/rich).
- **Mục đích:** Thư viện Python hiển thị bảng, tiến độ, Markdown, cú pháp và traceback trên terminal.
- **Điểm đáng dùng:** README mô tả đầu ra nhiều nền tảng và Jupyter; pyproject là nguồn yêu cầu runtime đáng tin hơn lời giới thiệu: Python >=3.10 trong snapshot này.
- **License:** MIT.
- **Giới hạn:** README còn nói Python 3.8 trong khi manifest đòi >=3.10; nên theo manifest. Khả năng màu phụ thuộc terminal; traceback có thể lộ dữ liệu nếu ghi log không lọc.
- **Tích hợp:** Cài rich trong môi trường dự án, dùng output thuần cho consumer máy và cấu hình việc hiển thị biến trong traceback.
- **Đối chiếu:** Click cho CLI và màu cơ bản; [Textual](../06-ui-ux-design/README.md#anhkysuai-textualize-textual) cho TUI tương tác; tabulate cho bảng nhỏ.
- **Mức kiểm chứng:** `docs-read` — Đọc các phần mô tả và giới hạn trong README, thông báo license, metadata manifest và cấu hình CI khi có; chưa đọc toàn bộ mã triển khai, chưa cài hoặc chạy kiểm thử upstream.
- **Snapshot:** kiểm ngày 2026-11-23; commit `3a109ccdffe5b2d0e30684a304fbd388e99ce57b` (2026-11-07T11:26:07Z); 57,853 sao theo GitHub API ngày 2026-11-23. Sao không đại diện chất lượng.
- **Bằng chứng:** [README.md](https://github.com/Textualize/rich/blob/3a109ccdffe5b2d0e30684a304fbd388e99ce57b/README.md) · [LICENSE](https://github.com/Textualize/rich/blob/3a109ccdffe5b2d0e30684a304fbd388e99ce57b/LICENSE) · [pyproject.toml](https://github.com/Textualize/rich/blob/3a109ccdffe5b2d0e30684a304fbd388e99ce57b/pyproject.toml) · [.github/workflows/codeql.yml](https://github.com/Textualize/rich/blob/3a109ccdffe5b2d0e30684a304fbd388e99ce57b/.github/workflows/codeql.yml) · [GitHub API](https://api.github.com/repos/Textualize/rich).

<a id="anhkysuai-powershell-powershell"></a>

### PowerShell

- **Repo:** [PowerShell/PowerShell](https://github.com/PowerShell/PowerShell).
- **Mục đích:** Shell, ngôn ngữ script và hệ cmdlet đa nền tảng, xử lý dữ liệu có cấu trúc.
- **Điểm đáng dùng:** README mô tả pipeline đối tượng và JSON/CSV/XML, đồng thời phân biệt nhánh PowerShell 7+ với Windows PowerShell 5.1; phù hợp điều phối công cụ Windows trong worker.
- **License:** MIT.
- **Giới hạn:** Module và API hệ điều hành không hoàn toàn giống giữa Windows, Linux, macOS; không suy script 5.1 tương thích 7+. Chưa chạy script upstream.
- **Tích hợp:** Dùng pwsh với phiên bản và module ghim, tránh ghép chuỗi lệnh từ dữ liệu chưa tin cậy, truyền tham số có cấu trúc.
- **Đối chiếu:** Bash cho shell POSIX; Python cho logic phức tạp; [Nushell](../13-dev-stack-devops/README.md#anhkysuai-nushell-nushell) cho pipeline dữ liệu.
- **Mức kiểm chứng:** `docs-read` — Đọc các phần mô tả và giới hạn trong README, thông báo license, metadata manifest và cấu hình CI khi có; chưa đọc toàn bộ mã triển khai, chưa cài hoặc chạy kiểm thử upstream.
- **Snapshot:** kiểm ngày 2026-11-23; commit `ba2221aed027041b6620c5fe1c0675567f14452a` (2026-11-19T12:32:38-08:00); 56,276 sao theo GitHub API ngày 2026-11-23. Sao không đại diện chất lượng.
- **Bằng chứng:** [README.md](https://github.com/PowerShell/PowerShell/blob/ba2221aed027041b6620c5fe1c0675567f14452a/README.md) · [LICENSE.txt](https://github.com/PowerShell/PowerShell/blob/ba2221aed027041b6620c5fe1c0675567f14452a/LICENSE.txt) · [.github/workflows/linux-ci.yml](https://github.com/PowerShell/PowerShell/blob/ba2221aed027041b6620c5fe1c0675567f14452a/.github/workflows/linux-ci.yml) · [GitHub API](https://api.github.com/repos/PowerShell/PowerShell).

<a id="anhkysuai-expo-expo"></a>

### Expo

- **Repo:** [expo/expo](https://github.com/expo/expo).
- **Mục đích:** Nền tảng React Native cho ứng dụng Android, iOS và web.
- **Điểm đáng dùng:** Monorepo có SDK, Modules API, Go app, CLI, Router, templates và docs; README giải thích các thư mục, giúp phân biệt runtime nguồn mở với dịch vụ EAS được host.
- **License:** MIT cho mã Expo; phụ thuộc có giấy phép riêng.
- **Giới hạn:** EAS là dịch vụ riêng; quyền module native, ký ứng dụng và yêu cầu build của từng nền tảng vẫn cần quản lý. CI đã đọc bỏ qua một số build/e2e với draft PR.
- **Tích hợp:** Khởi tạo bằng template được phát hành, ghim SDK và kiểm tương thích module native trước nâng cấp.
- **Đối chiếu:** [React Native](../13-dev-stack-devops/README.md) thuần cho kiểm soát native; [Flutter](../13-dev-stack-devops/README.md) cho hệ widget riêng; Capacitor cho ứng dụng web đóng gói.
- **Mức kiểm chứng:** `docs-read` — Đọc các phần mô tả và giới hạn trong README, thông báo license, metadata manifest và cấu hình CI khi có; chưa đọc toàn bộ mã triển khai, chưa cài hoặc chạy kiểm thử upstream.
- **Snapshot:** kiểm ngày 2026-11-23; commit `f0efd93b378e1147026a09d3b80324a5590f3e58` (2026-11-23T10:52:49+01:00); 53,736 sao theo GitHub API ngày 2026-11-23. Sao không đại diện chất lượng.
- **Bằng chứng:** [README.md](https://github.com/expo/expo/blob/f0efd93b378e1147026a09d3b80324a5590f3e58/README.md) · [LICENSE](https://github.com/expo/expo/blob/f0efd93b378e1147026a09d3b80324a5590f3e58/LICENSE) · [package.json](https://github.com/expo/expo/blob/f0efd93b378e1147026a09d3b80324a5590f3e58/package.json) · [.github/workflows/test-suite.yml](https://github.com/expo/expo/blob/f0efd93b378e1147026a09d3b80324a5590f3e58/.github/workflows/test-suite.yml) · [GitHub API](https://api.github.com/repos/expo/expo).

<a id="anhkysuai-definitelytyped-definitelytyped"></a>

### DefinitelyTyped

- **Repo:** [DefinitelyTyped/DefinitelyTyped](https://github.com/DefinitelyTyped/DefinitelyTyped).
- **Mục đích:** Kho khai báo kiểu TypeScript cho các thư viện JavaScript chưa tự cung cấp type.
- **Điểm đáng dùng:** README mô tả package @types và monorepo pnpm có kiểm type/lint; hữu ích tách hợp đồng tĩnh của thư viện khỏi runtime.
- **License:** MIT; copyright theo từng contributor/file khai báo.
- **Giới hạn:** Declaration có thể lệch phiên bản thực thi và không xác thực dữ liệu khi chạy; cần khớp major version và bổ sung kiểm runtime ở biên dữ liệu.
- **Tích hợp:** Cài đúng @types/package ở devDependencies nếu thư viện chưa có type; kiểm tsc trong CI.
- **Đối chiếu:** Type gốc từ package khi có; JSDoc cho dự án JS; declaration cục bộ có test cho API riêng.
- **Mức kiểm chứng:** `docs-read` — Đọc các phần mô tả và giới hạn trong README, thông báo license, metadata manifest và cấu hình CI khi có; chưa đọc toàn bộ mã triển khai, chưa cài hoặc chạy kiểm thử upstream.
- **Snapshot:** kiểm ngày 2026-11-23; commit `90f69d78cc09a977ad9422249941e3c3e4244dbc` (2026-11-23T08:21:55Z); 51,485 sao theo GitHub API ngày 2026-11-23. Sao không đại diện chất lượng.
- **Bằng chứng:** [README.md](https://github.com/DefinitelyTyped/DefinitelyTyped/blob/90f69d78cc09a977ad9422249941e3c3e4244dbc/README.md) · [LICENSE](https://github.com/DefinitelyTyped/DefinitelyTyped/blob/90f69d78cc09a977ad9422249941e3c3e4244dbc/LICENSE) · [package.json](https://github.com/DefinitelyTyped/DefinitelyTyped/blob/90f69d78cc09a977ad9422249941e3c3e4244dbc/package.json) · [.github/workflows/CI.yml](https://github.com/DefinitelyTyped/DefinitelyTyped/blob/90f69d78cc09a977ad9422249941e3c3e4244dbc/.github/workflows/CI.yml) · [GitHub API](https://api.github.com/repos/DefinitelyTyped/DefinitelyTyped).

<a id="anhkysuai-homebrew-brew"></a>

### Homebrew

- **Repo:** [Homebrew/brew](https://github.com/Homebrew/brew).
- **Mục đích:** Trình quản lý gói và môi trường công cụ, có formula, cask và bundle.
- **Điểm đáng dùng:** README tách metadata gói, brew doctor, strict audit và hướng dẫn đóng góp; workflow có style/typecheck, hỗ trợ tham khảo cách kiểm công thức phân phối phần mềm.
- **License:** BSD-2-Clause cho code; tài liệu theo CC BY.
- **Giới hạn:** License Homebrew không thay license gói; README có analytics tổng hợp cần đọc chính sách/cấu hình trước triển khai. Tap bên ngoài là nguồn tin cậy riêng.
- **Tích hợp:** Quản lý danh sách phụ thuộc bằng Brewfile, ưu tiên tap chính thức và giữ cách nâng cấp phù hợp máy.
- **Đối chiếu:** [Nix](../13-dev-stack-devops/README.md#nix) cho môi trường khai báo; apt/dnf cho Linux hệ thống; Scoop hoặc winget cho Windows.
- **Mức kiểm chứng:** `docs-read` — Đọc các phần mô tả và giới hạn trong README, thông báo license, metadata manifest và cấu hình CI khi có; chưa đọc toàn bộ mã triển khai, chưa cài hoặc chạy kiểm thử upstream.
- **Snapshot:** kiểm ngày 2026-11-23; commit `7ef183d10e7d6e5620d7124b744b1dfbf69fc108` (2026-11-23T09:18:37Z); 50,411 sao theo GitHub API ngày 2026-11-23. Sao không đại diện chất lượng.
- **Bằng chứng:** [README.md](https://github.com/Homebrew/brew/blob/7ef183d10e7d6e5620d7124b744b1dfbf69fc108/README.md) · [LICENSE.txt](https://github.com/Homebrew/brew/blob/7ef183d10e7d6e5620d7124b744b1dfbf69fc108/LICENSE.txt) · [.github/workflows/tests.yml](https://github.com/Homebrew/brew/blob/7ef183d10e7d6e5620d7124b744b1dfbf69fc108/.github/workflows/tests.yml) · [GitHub API](https://api.github.com/repos/Homebrew/brew).

<a id="anhkysuai-bevyengine-bevy"></a>

### Bevy

- **Repo:** [bevyengine/bevy](https://github.com/bevyengine/bevy).
- **Mục đích:** Game engine Rust theo kiến trúc dữ liệu và Entity Component System.
- **Điểm đáng dùng:** README nhấn mạnh plugin/module và xử lý song song; Cargo snapshot là 0.20.0-dev, CI có build và test, phù hợp tham khảo ECS cho mô phỏng tương tác.
- **License:** MIT OR Apache-2.0; ngoại lệ theo crate/asset.
- **Giới hạn:** Tác giả cảnh báo API thay đổi thường xuyên và thiếu một số tính năng/tài liệu; cần ghim release, không coi HEAD dev là API ổn định.
- **Tích hợp:** Chọn release và plugin tương thích, làm thử nghiệm nhỏ trước khi gắn pipeline asset hoặc renderer vào sản phẩm.
- **Đối chiếu:** [Godot](../08-awesome-lists-learning/README.md#6c528-ứng-dụng-đa-nền-tảng--game) cho editor tích hợp; Unity cho hệ thương mại lớn; [raylib](../06-ui-ux-design/README.md#anhkysuai-raysan5-raylib) cho lớp đồ họa nhỏ.
- **Mức kiểm chứng:** `docs-read` — Đọc các phần mô tả và giới hạn trong README, thông báo license, metadata manifest và cấu hình CI khi có; chưa đọc toàn bộ mã triển khai, chưa cài hoặc chạy kiểm thử upstream.
- **Snapshot:** kiểm ngày 2026-11-23; commit `ea068131982105dca960341ee8fe72b902db57b4` (2026-11-22T19:35:07Z); 49,954 sao theo GitHub API ngày 2026-11-23. Sao không đại diện chất lượng.
- **Bằng chứng:** [README.md](https://github.com/bevyengine/bevy/blob/ea068131982105dca960341ee8fe72b902db57b4/README.md) · [LICENSE-APACHE](https://github.com/bevyengine/bevy/blob/ea068131982105dca960341ee8fe72b902db57b4/LICENSE-APACHE) · [LICENSE-MIT](https://github.com/bevyengine/bevy/blob/ea068131982105dca960341ee8fe72b902db57b4/LICENSE-MIT) · [Cargo.toml](https://github.com/bevyengine/bevy/blob/ea068131982105dca960341ee8fe72b902db57b4/Cargo.toml) · [.github/workflows/ci.yml](https://github.com/bevyengine/bevy/blob/ea068131982105dca960341ee8fe72b902db57b4/.github/workflows/ci.yml) · [GitHub API](https://api.github.com/repos/bevyengine/bevy).

<a id="anhkysuai-julialang-julia"></a>

### Julia

**Đã chuyển (2026-11-23):** hồ sơ này nay nằm ở [mục 37](../37-programming-languages-runtimes/README.md#anhkysuai-julialang-julia); catalog con xem [catalog/](../catalog/README.md).

<a id="anhkysuai-cli-cli"></a>

### GitHub CLI

- **Repo:** [cli/cli](https://github.com/cli/cli).
- **Mục đích:** Công cụ gh đưa tác vụ GitHub vào terminal và tự động hóa.
- **Điểm đáng dùng:** README mô tả cài đặt trên runner/Codespaces và xác minh binary, manifest Go xác định upstream github.com/cli/cli/v2; khác với các repo cũng tên cli của Google Workspace hay Lark.
- **License:** MIT.
- **Giới hạn:** Hành động ghi chạy dưới quyền token/tài khoản; phiên bản có sẵn trên runner thay đổi, nên ghim khi cần tái lập. Extension là nguồn thực thi riêng.
- **Tích hợp:** Dùng gh với repo và scope quyền rõ ràng, lấy JSON cho script, kiểm trạng thái sau thao tác.
- **Đối chiếu:** GitHub REST/GraphQL cho tích hợp riêng; giao diện web cho tác vụ tương tác; [Git](../13-dev-stack-devops/README.md#anhkysuai-git-git) thuần cho lịch sử mã.
- **Mức kiểm chứng:** `docs-read` — Đọc các phần mô tả và giới hạn trong README, thông báo license, metadata manifest và cấu hình CI khi có; chưa đọc toàn bộ mã triển khai, chưa cài hoặc chạy kiểm thử upstream.
- **Snapshot:** kiểm ngày 2026-11-23; commit `de06af2c2ea536d5722fda35dc2001565f9b9f64` (2026-11-20T13:14:15Z); 47,162 sao theo GitHub API ngày 2026-11-23. Sao không đại diện chất lượng.
- **Bằng chứng:** [README.md](https://github.com/cli/cli/blob/de06af2c2ea536d5722fda35dc2001565f9b9f64/README.md) · [LICENSE](https://github.com/cli/cli/blob/de06af2c2ea536d5722fda35dc2001565f9b9f64/LICENSE) · [go.mod](https://github.com/cli/cli/blob/de06af2c2ea536d5722fda35dc2001565f9b9f64/go.mod) · [.github/workflows/govulncheck.yml](https://github.com/cli/cli/blob/de06af2c2ea536d5722fda35dc2001565f9b9f64/.github/workflows/govulncheck.yml) · [GitHub API](https://api.github.com/repos/cli/cli).

<a id="anhkysuai-helix-editor-helix"></a>

### Helix

- **Repo:** [helix-editor/helix](https://github.com/helix-editor/helix).
- **Mục đích:** Editor terminal dạng modal với mô hình lựa chọn văn bản và nhiều selection.
- **Điểm đáng dùng:** README mô tả LSP và tree-sitter tích hợp, Cargo xác định MPL-2.0, workflow có cargo check/test; phù hợp tham khảo editor ít cần lắp plugin cơ bản.
- **License:** MPL-2.0.
- **Giới hạn:** Hỗ trợ indent phụ thuộc query của từng ngôn ngữ; mô hình thao tác khác Vim cần học lại. Chưa đo đáp ứng hay kiểm grammar thực tế.
- **Tích hợp:** Cài release, cấu hình language server và kiểm runtime queries cho ngôn ngữ sử dụng.
- **Đối chiếu:** [Neovim](../08-awesome-lists-learning/README.md#6c58-editor-terminal--dòng-lệnh) cho plugin rộng; Kakoune cho mô hình selection; [VS Code](../08-awesome-lists-learning/README.md#6c58-editor-terminal--dòng-lệnh) cho IDE đồ họa.
- **Mức kiểm chứng:** `docs-read` — Đọc các phần mô tả và giới hạn trong README, thông báo license, metadata manifest và cấu hình CI khi có; chưa đọc toàn bộ mã triển khai, chưa cài hoặc chạy kiểm thử upstream.
- **Snapshot:** kiểm ngày 2026-11-23; commit `1a3fdfda6dfdda4567af6093a6249bb2bb422fc6` (2026-11-20T20:15:14+09:00); 46,977 sao theo GitHub API ngày 2026-11-23. Sao không đại diện chất lượng.
- **Bằng chứng:** [README.md](https://github.com/helix-editor/helix/blob/1a3fdfda6dfdda4567af6093a6249bb2bb422fc6/README.md) · [LICENSE](https://github.com/helix-editor/helix/blob/1a3fdfda6dfdda4567af6093a6249bb2bb422fc6/LICENSE) · [Cargo.toml](https://github.com/helix-editor/helix/blob/1a3fdfda6dfdda4567af6093a6249bb2bb422fc6/Cargo.toml) · [.github/workflows/build.yml](https://github.com/helix-editor/helix/blob/1a3fdfda6dfdda4567af6093a6249bb2bb422fc6/.github/workflows/build.yml) · [GitHub API](https://api.github.com/repos/helix-editor/helix).

<a id="anhkysuai-google-zx"></a>

### zx

- **Repo:** [google/zx](https://github.com/google/zx).
- **Mục đích:** Viết script điều phối shell bằng JavaScript/TypeScript với wrapper child_process.
- **Điểm đáng dùng:** README nêu escape tham số và hỗ trợ Bash/PowerShell cùng nhiều runtime; phù hợp tác vụ có JSON, điều kiện và gọi công cụ ngoài phức tạp hơn shell ngắn.
- **License:** Apache-2.0.
- **Giới hạn:** Không phải sản phẩm được Google hỗ trợ chính thức; wrapper không biến lệnh shell thành an toàn nếu cố ghép chuỗi. Chưa kiểm portability trên từng hệ.
- **Tích hợp:** Ghim zx/runtime, truyền tham số theo API thay vì nối chuỗi và kiểm exit code, timeout.
- **Đối chiếu:** Python subprocess cho dữ liệu và tiến trình; Bash cho script ngắn; [PowerShell](../13-dev-stack-devops/README.md#anhkysuai-powershell-powershell) cho object pipeline.
- **Mức kiểm chứng:** `docs-read` — Đọc các phần mô tả và giới hạn trong README, thông báo license, metadata manifest và cấu hình CI khi có; chưa đọc toàn bộ mã triển khai, chưa cài hoặc chạy kiểm thử upstream.
- **Snapshot:** kiểm ngày 2026-11-23; commit `3b04a6ae3e34b1a7ee6b925f1efcceb901f0d8a5` (2026-11-05T14:24:02+03:00); 45,865 sao theo GitHub API ngày 2026-11-23. Sao không đại diện chất lượng.
- **Bằng chứng:** [README.md](https://github.com/google/zx/blob/3b04a6ae3e34b1a7ee6b925f1efcceb901f0d8a5/README.md) · [LICENSE](https://github.com/google/zx/blob/3b04a6ae3e34b1a7ee6b925f1efcceb901f0d8a5/LICENSE) · [package.json](https://github.com/google/zx/blob/3b04a6ae3e34b1a7ee6b925f1efcceb901f0d8a5/package.json) · [.github/workflows/test.yml](https://github.com/google/zx/blob/3b04a6ae3e34b1a7ee6b925f1efcceb901f0d8a5/.github/workflows/test.yml) · [GitHub API](https://api.github.com/repos/google/zx).

<a id="anhkysuai-pyenv-pyenv"></a>

### pyenv

- **Repo:** [pyenv/pyenv](https://github.com/pyenv/pyenv).
- **Mục đích:** Chuyển phiên bản Python theo người dùng, thư mục dự án hoặc biến môi trường.
- **Điểm đáng dùng:** Shim trong PATH chọn bản Python; công cụ viết bằng shell nên không cần một Python sẵn có để khởi động quản lý phiên bản.
- **License:** MIT.
- **Giới hạn:** Không quản lý virtualenv mặc định; biên dịch Python cần thư viện hệ thống và thiết lập shell chính xác.
- **Tích hợp:** Ghi .python-version trong mẫu Python, dùng virtualenv hoặc uv cho môi trường và dependency.
- **Đối chiếu:** [uv](../13-dev-stack-devops/README.md) cho quản lý dự án Python; [asdf](../13-dev-stack-devops/README.md#anhkysuai-asdf-vm-asdf) cho nhiều runtime; [mise](../13-dev-stack-devops/README.md#factory-2026-11-04-mise) cho môi trường phát triển.
- **Mức kiểm chứng:** `docs-read` — Đọc các phần mô tả và giới hạn trong README, thông báo license, metadata manifest và cấu hình CI khi có; chưa đọc toàn bộ mã triển khai, chưa cài hoặc chạy kiểm thử upstream.
- **Snapshot:** kiểm ngày 2026-11-23; commit `fc6046ccd0721c0ea258e11c9320515cee13f4d7` (2026-11-20T08:33:41+03:00); 45,183 sao theo GitHub API ngày 2026-11-23. Sao không đại diện chất lượng.
- **Bằng chứng:** [README.md](https://github.com/pyenv/pyenv/blob/fc6046ccd0721c0ea258e11c9320515cee13f4d7/README.md) · [LICENSE](https://github.com/pyenv/pyenv/blob/fc6046ccd0721c0ea258e11c9320515cee13f4d7/LICENSE) · [.github/workflows/build.yml](https://github.com/pyenv/pyenv/blob/fc6046ccd0721c0ea258e11c9320515cee13f4d7/.github/workflows/build.yml) · [GitHub API](https://api.github.com/repos/pyenv/pyenv).

<a id="anhkysuai-sharkdp-fd"></a>

### fd

- **Repo:** [sharkdp/fd](https://github.com/sharkdp/fd).
- **Mục đích:** Tìm đường dẫn bằng regex hoặc glob với giao diện dòng lệnh ngắn.
- **Điểm đáng dùng:** Tài liệu mô tả duyệt thư mục song song, smart case và bỏ qua .gitignore; Cargo xác nhận tên gói fd-find và hai lựa chọn license.
- **License:** MIT OR Apache-2.0.
- **Giới hạn:** Mặc định bỏ tệp ẩn và tệp bị ignore nên không dùng kết quả rỗng để khẳng định tệp không tồn tại; không thay hết khả năng find.
- **Tích hợp:** Dùng khám phá nguồn cho công cụ template, đặt rõ quy tắc ignore và cách truyền tên tệp cho lệnh sau.
- **Đối chiếu:** [ripgrep](../13-dev-stack-devops/README.md#anhkysuai-burntsushi-ripgrep) cho tìm nội dung; find cho điều kiện filesystem; [fzf](../08-awesome-lists-learning/README.md#6c58-editor-terminal--dòng-lệnh) cho chọn tương tác.
- **Mức kiểm chứng:** `docs-read` — Đọc các phần mô tả và giới hạn trong README, thông báo license, metadata manifest và cấu hình CI khi có; chưa đọc toàn bộ mã triển khai, chưa cài hoặc chạy kiểm thử upstream.
- **Snapshot:** kiểm ngày 2026-11-23; commit `f8d4e0e7de6e502b80b6d77f169e5b4a20f6742d` (2026-11-21T00:41:11-07:00); 45,169 sao theo GitHub API ngày 2026-11-23. Sao không đại diện chất lượng.
- **Bằng chứng:** [README.md](https://github.com/sharkdp/fd/blob/f8d4e0e7de6e502b80b6d77f169e5b4a20f6742d/README.md) · [LICENSE-APACHE](https://github.com/sharkdp/fd/blob/f8d4e0e7de6e502b80b6d77f169e5b4a20f6742d/LICENSE-APACHE) · [LICENSE-MIT](https://github.com/sharkdp/fd/blob/f8d4e0e7de6e502b80b6d77f169e5b4a20f6742d/LICENSE-MIT) · [Cargo.toml](https://github.com/sharkdp/fd/blob/f8d4e0e7de6e502b80b6d77f169e5b4a20f6742d/Cargo.toml) · [.github/workflows/CICD.yml](https://github.com/sharkdp/fd/blob/f8d4e0e7de6e502b80b6d77f169e5b4a20f6742d/.github/workflows/CICD.yml) · [GitHub API](https://api.github.com/repos/sharkdp/fd).

<a id="anhkysuai-spf13-cobra"></a>

### Cobra

- **Repo:** [spf13/cobra](https://github.com/spf13/cobra).
- **Mục đích:** Thư viện Go xây CLI có cây lệnh và cờ.
- **Điểm đáng dùng:** Command, args và flags là cấu trúc chính; hỗ trợ cờ kế thừa, alias, trợ giúp, completion và sinh trang man.
- **License:** Apache-2.0.
- **Giới hạn:** Chỉ tổ chức giao diện lệnh; kiểm tra đầu vào, hủy tác vụ và tính lặp an toàn vẫn do ứng dụng thiết kế.
- **Tích hợp:** Dùng dựng CLI tạo dự án với subcommand rõ, kiểm thử lỗi tham số và mã thoát trước khi nối tác vụ có ghi dữ liệu.
- **Đối chiếu:** Typer cho Python; Commander.js cho Node; clap cho Rust.
- **Mức kiểm chứng:** `docs-read` — Đọc các phần mô tả và giới hạn trong README, thông báo license, metadata manifest và cấu hình CI khi có; chưa đọc toàn bộ mã triển khai, chưa cài hoặc chạy kiểm thử upstream.
- **Snapshot:** kiểm ngày 2026-11-23; commit `adbc8813901bba65827259daa8e22ff94ec1f30e` (2026-07-10T20:43:07-04:00); 44,825 sao theo GitHub API ngày 2026-11-23. Sao không đại diện chất lượng.
- **Bằng chứng:** [README.md](https://github.com/spf13/cobra/blob/adbc8813901bba65827259daa8e22ff94ec1f30e/README.md) · [LICENSE.txt](https://github.com/spf13/cobra/blob/adbc8813901bba65827259daa8e22ff94ec1f30e/LICENSE.txt) · [go.mod](https://github.com/spf13/cobra/blob/adbc8813901bba65827259daa8e22ff94ec1f30e/go.mod) · [.github/workflows/test.yml](https://github.com/spf13/cobra/blob/adbc8813901bba65827259daa8e22ff94ec1f30e/.github/workflows/test.yml) · [GitHub API](https://api.github.com/repos/spf13/cobra).

<a id="anhkysuai-meteor-meteor"></a>

### Meteor

- **Repo:** [meteor/meteor](https://github.com/meteor/meteor).
- **Mục đích:** Môi trường JavaScript tích hợp công cụ phát triển và core package cho ứng dụng nhiều nền tảng.
- **Điểm đáng dùng:** README đưa tutorial React, Blaze, Vue, Svelte, Solid; workflow E2E kiểm kê nhóm kiểm thử trước khi tạo ma trận.
- **License:** MIT.
- **Giới hạn:** Galaxy là dịch vụ triển khai riêng, không suy ra mọi tính năng hosted nằm trong repo; phải đánh giá chi phí phụ thuộc hệ sinh thái Meteor.
- **Tích hợp:** Thử một mẫu CRUD nhỏ và kiểm tra lựa chọn package, build, deploy của chính template trước khi chuẩn hóa.
- **Đối chiếu:** [Next.js](../13-dev-stack-devops/README.md) cho React; [Nuxt](../13-dev-stack-devops/README.md) cho Vue; SvelteKit cho Svelte.
- **Mức kiểm chứng:** `docs-read` — Đọc các phần mô tả và giới hạn trong README, thông báo license, metadata manifest và cấu hình CI khi có; chưa đọc toàn bộ mã triển khai, chưa cài hoặc chạy kiểm thử upstream.
- **Snapshot:** kiểm ngày 2026-11-23; commit `b377f35db21e0f77971fa982f5603a76c08542d8` (2026-11-18T15:35:28+01:00); 44,791 sao theo GitHub API ngày 2026-11-23. Sao không đại diện chất lượng.
- **Bằng chứng:** [README.md](https://github.com/meteor/meteor/blob/b377f35db21e0f77971fa982f5603a76c08542d8/README.md) · [LICENSE](https://github.com/meteor/meteor/blob/b377f35db21e0f77971fa982f5603a76c08542d8/LICENSE) · [package.json](https://github.com/meteor/meteor/blob/b377f35db21e0f77971fa982f5603a76c08542d8/package.json) · [.github/workflows/e2e-tests.yml](https://github.com/meteor/meteor/blob/b377f35db21e0f77971fa982f5603a76c08542d8/.github/workflows/e2e-tests.yml) · [GitHub API](https://api.github.com/repos/meteor/meteor).

<a id="anhkysuai-babel-babel"></a>

### Babel

- **Repo:** [babel/babel](https://github.com/babel/babel).
- **Mục đích:** Biên dịch cú pháp JavaScript mới sang mục tiêu thực thi được lựa chọn.
- **Điểm đáng dùng:** Monorepo chia thành nhiều package compiler; README minh họa biến đổi cú pháp, manifest tại SHA mang phiên bản 8.1.3.
- **License:** MIT.
- **Giới hạn:** Biến đổi cú pháp không tự bảo đảm mọi API runtime tồn tại; plugin/preset và hỗ trợ trình duyệt cần khóa tương thích.
- **Tích hợp:** Dùng khi template cần transform cụ thể, ghi rõ target và chính sách polyfill rồi kiểm thử bundle đầu ra.
- **Đối chiếu:** [SWC](../13-dev-stack-devops/README.md#anhkysuai-swc-project-swc) cho compiler Rust; [esbuild](../13-dev-stack-devops/README.md#anhkysuai-evanw-esbuild) cho build tích hợp; TypeScript compiler cho kiểm tra kiểu và emit.
- **Mức kiểm chứng:** `docs-read` — Đọc các phần mô tả và giới hạn trong README, thông báo license, metadata manifest và cấu hình CI khi có; chưa đọc toàn bộ mã triển khai, chưa cài hoặc chạy kiểm thử upstream.
- **Snapshot:** kiểm ngày 2026-11-23; commit `5122561237cfbbc78b356a24e96eea9bdc558fd2` (2026-11-22T03:59:32Z); 44,078 sao theo GitHub API ngày 2026-11-23. Sao không đại diện chất lượng.
- **Bằng chứng:** [README.md](https://github.com/babel/babel/blob/5122561237cfbbc78b356a24e96eea9bdc558fd2/README.md) · [LICENSE](https://github.com/babel/babel/blob/5122561237cfbbc78b356a24e96eea9bdc558fd2/LICENSE) · [package.json](https://github.com/babel/babel/blob/5122561237cfbbc78b356a24e96eea9bdc558fd2/package.json) · [.github/workflows/ci.yml](https://github.com/babel/babel/blob/5122561237cfbbc78b356a24e96eea9bdc558fd2/.github/workflows/ci.yml) · [GitHub API](https://api.github.com/repos/babel/babel).

<a id="anhkysuai-parcel-bundler-parcel"></a>

### Parcel

- **Repo:** [parcel-bundler/parcel](https://github.com/parcel-bundler/parcel).
- **Mục đích:** Build tool web tích hợp xử lý mã, CSS, hình ảnh, font và dev server.
- **Điểm đáng dùng:** README v3 mô tả lõi Rust và plugin native/JavaScript, tối ưu tài nguyên theo target; workflow có kiểm tra TypeScript và Rust đa hệ điều hành.
- **License:** MIT.
- **Giới hạn:** HEAD được ghi rõ v3 alpha; v2 nằm ở nhánh riêng. Không lấy hứa hẹn zero-config hay tốc độ làm kết quả đo cho dự án.
- **Tích hợp:** Chọn bản ổn định hoặc thử nghiệm v3 có chủ đích, đo bundle và kiểm tra từng plugin cần thiết trước khi chốt template.
- **Đối chiếu:** [Vite](../13-dev-stack-devops/README.md) cho dev server; [webpack](../13-dev-stack-devops/README.md#anhkysuai-webpack-webpack) cho cấu hình sâu; [esbuild](../13-dev-stack-devops/README.md#anhkysuai-evanw-esbuild) cho pipeline gọn.
- **Mức kiểm chứng:** `docs-read` — Đọc các phần mô tả và giới hạn trong README, thông báo license, metadata manifest và cấu hình CI khi có; chưa đọc toàn bộ mã triển khai, chưa cài hoặc chạy kiểm thử upstream.
- **Snapshot:** kiểm ngày 2026-11-23; commit `63a71c9c3d1499127a9f8ba3b8602ae80456b4af` (2026-11-22T14:45:14-08:00); 44,034 sao theo GitHub API ngày 2026-11-23. Sao không đại diện chất lượng.
- **Bằng chứng:** [README.md](https://github.com/parcel-bundler/parcel/blob/63a71c9c3d1499127a9f8ba3b8602ae80456b4af/README.md) · [LICENSE](https://github.com/parcel-bundler/parcel/blob/63a71c9c3d1499127a9f8ba3b8602ae80456b4af/LICENSE) · [package.json](https://github.com/parcel-bundler/parcel/blob/63a71c9c3d1499127a9f8ba3b8602ae80456b4af/package.json) · [Cargo.toml](https://github.com/parcel-bundler/parcel/blob/63a71c9c3d1499127a9f8ba3b8602ae80456b4af/Cargo.toml) · [.github/workflows/v3.yml](https://github.com/parcel-bundler/parcel/blob/63a71c9c3d1499127a9f8ba3b8602ae80456b4af/.github/workflows/v3.yml) · [GitHub API](https://api.github.com/repos/parcel-bundler/parcel).

<a id="anhkysuai-alamofire-alamofire"></a>

### Alamofire

- **Repo:** [Alamofire/Alamofire](https://github.com/Alamofire/Alamofire).
- **Mục đích:** Thư viện HTTP Swift cho ứng dụng trên nền tảng Apple.
- **Điểm đáng dùng:** API bao phủ encode, upload/download, response validation, adapter/retry và Swift concurrency; CI có ma trận Xcode/Swift.
- **License:** MIT.
- **Giới hạn:** Retry có thể lặp thao tác ghi; pinning cần kế hoạch thay chứng chỉ, log cURL phải che token. Chưa chạy kiểm thử mạng hoặc thiết bị.
- **Tích hợp:** Bọc Session theo môi trường, giới hạn retry theo tính idempotent và viết fixture cho lỗi xác thực, timeout.
- **Đối chiếu:** URLSession cho API hệ thống; [OkHttp](../34-backend-data-identity-integration/README.md#anhkysuai-lysine-dev-okhttp) cho Android/JVM; [Requests](../34-backend-data-identity-integration/README.md#anhkysuai-psf-requests) cho Python.
- **Mức kiểm chứng:** `docs-read` — Đọc các phần mô tả và giới hạn trong README, thông báo license, metadata manifest và cấu hình CI khi có; chưa đọc toàn bộ mã triển khai, chưa cài hoặc chạy kiểm thử upstream.
- **Snapshot:** kiểm ngày 2026-11-23; commit `dea4bab91767a971d6e112bc955c6a82295589b7` (2026-11-13T22:41:37-05:00); 42,397 sao theo GitHub API ngày 2026-11-23. Sao không đại diện chất lượng.
- **Bằng chứng:** [README.md](https://github.com/Alamofire/Alamofire/blob/dea4bab91767a971d6e112bc955c6a82295589b7/README.md) · [LICENSE](https://github.com/Alamofire/Alamofire/blob/dea4bab91767a971d6e112bc955c6a82295589b7/LICENSE) · [.github/workflows/ci.yml](https://github.com/Alamofire/Alamofire/blob/dea4bab91767a971d6e112bc955c6a82295589b7/.github/workflows/ci.yml) · [GitHub API](https://api.github.com/repos/Alamofire/Alamofire).

<a id="anhkysuai-dcloudio-uni-app"></a>

### uni-app

- **Repo:** [dcloudio/uni-app](https://github.com/dcloudio/uni-app).
- **Mục đích:** Framework Vue phát triển web, ứng dụng và mini-program nhiều nền tảng.
- **Điểm đáng dùng:** README phân biệt uni-app cũ và nhánh chính uni-app x; UTS hướng đến Kotlin, Swift, ArkTS hoặc JavaScript tùy target.
- **License:** Apache-2.0 cho mã repo; license.md dẫn điều khoản DCloud riêng cần kiểm tra.
- **Giới hạn:** Không đánh đồng nhánh x với vue2/vue3; benchmark native là công bố tác giả chưa tái hiện. Hệ công cụ và dịch vụ DCloud có điều khoản ngoài LICENSE mã.
- **Tích hợp:** Chọn target và nhánh trước, làm mẫu tính năng native thiết yếu trên thiết bị thật và kiểm tra giấy phép phần đóng gói.
- **Đối chiếu:** Expo/React Native cho mobile; [Flutter](../13-dev-stack-devops/README.md) cho UI đa nền tảng; [Taro](../13-dev-stack-devops/README.md#anhkysuai-nervjs-taro) cho mini-program.
- **Mức kiểm chứng:** `docs-read` — Đọc các phần mô tả và giới hạn trong README, thông báo license, metadata manifest và cấu hình CI khi có; chưa đọc toàn bộ mã triển khai, chưa cài hoặc chạy kiểm thử upstream.
- **Snapshot:** kiểm ngày 2026-11-23; commit `67f1cbbee193ff44c1a9a9a1ed80faade6e562ae` (2026-11-23T16:48:24+08:00); 41,699 sao theo GitHub API ngày 2026-11-23. Sao không đại diện chất lượng.
- **Bằng chứng:** [README.md](https://github.com/dcloudio/uni-app/blob/67f1cbbee193ff44c1a9a9a1ed80faade6e562ae/README.md) · [LICENSE](https://github.com/dcloudio/uni-app/blob/67f1cbbee193ff44c1a9a9a1ed80faade6e562ae/LICENSE) · [license.md](https://github.com/dcloudio/uni-app/blob/67f1cbbee193ff44c1a9a9a1ed80faade6e562ae/license.md) · [package.json](https://github.com/dcloudio/uni-app/blob/67f1cbbee193ff44c1a9a9a1ed80faade6e562ae/package.json) · [GitHub API](https://api.github.com/repos/dcloudio/uni-app).

<a id="anhkysuai-nwjs-nw-js"></a>

### NW.js

- **Repo:** [nwjs/nw.js](https://github.com/nwjs/nw.js).
- **Mục đích:** Runtime desktop ghép Chromium và Node.js để đóng gói ứng dụng HTML/JavaScript.
- **Điểm đáng dùng:** Cho phép gọi module Node từ DOM; README giải thích SDK build và cấu trúc package của ứng dụng.
- **License:** MIT cho mã repo; Chromium/Node và binary có thông báo riêng.
- **Giới hạn:** Nội dung web có thể tiếp cận quyền Node nên nguồn nội dung và phân quyền là điểm cần kiểm tra; bản binary không chỉ có license MIT.
- **Tích hợp:** Dùng nội dung được kiểm soát, khóa runtime và lập quy trình cập nhật Chromium, ký gói và rà soát license phụ thuộc.
- **Đối chiếu:** [Electron](../08-awesome-lists-learning/README.md#6c528-ứng-dụng-đa-nền-tảng--game) cho hệ sinh thái desktop JS; [Tauri](../13-dev-stack-devops/README.md) cho WebView hệ thống; [Wails](../13-dev-stack-devops/README.md#anhkysuai-wailsapp-wails) cho backend Go.
- **Mức kiểm chứng:** `docs-read` — Đọc các phần mô tả và giới hạn trong README, thông báo license, metadata manifest và cấu hình CI khi có; chưa đọc toàn bộ mã triển khai, chưa cài hoặc chạy kiểm thử upstream.
- **Snapshot:** kiểm ngày 2026-11-23; commit `47a32c0e6639fb0b19ec07b8a603dcadfdfea167` (2026-11-12T14:47:23-07:00); 41,141 sao theo GitHub API ngày 2026-11-23. Sao không đại diện chất lượng.
- **Bằng chứng:** [README.md](https://github.com/nwjs/nw.js/blob/47a32c0e6639fb0b19ec07b8a603dcadfdfea167/README.md) · [LICENSE](https://github.com/nwjs/nw.js/blob/47a32c0e6639fb0b19ec07b8a603dcadfdfea167/LICENSE) · [GitHub API](https://api.github.com/repos/nwjs/nw.js).

<a id="anhkysuai-nushell-nushell"></a>

### Nushell

- **Repo:** [nushell/nushell](https://github.com/nushell/nushell).
- **Mục đích:** Shell truyền bảng và giá trị có cấu trúc qua pipeline.
- **Điểm đáng dùng:** Đầu ra lệnh có thể là bảng thay vì chuỗi thô; triết lý pipeline phù hợp xử lý JSON và dữ liệu công cụ phát triển.
- **License:** MIT.
- **Giới hạn:** README cảnh báo một số lệnh chưa ổn định và thiết kế còn đổi; cú pháp không tương thích trực tiếp script POSIX.
- **Tích hợp:** Thử trong tác vụ đọc dữ liệu và báo cáo, khóa phiên bản cho automation và chuyển đổi rõ tại ranh giới lệnh ngoài.
- **Đối chiếu:** [PowerShell](../13-dev-stack-devops/README.md#anhkysuai-powershell-powershell) cho pipeline đối tượng; jq cho JSON; [fish](../13-dev-stack-devops/README.md#anhkysuai-fish-shell-fish-shell) cho shell tương tác.
- **Mức kiểm chứng:** `docs-read` — Đọc các phần mô tả và giới hạn trong README, thông báo license, metadata manifest và cấu hình CI khi có; chưa đọc toàn bộ mã triển khai, chưa cài hoặc chạy kiểm thử upstream.
- **Snapshot:** kiểm ngày 2026-11-23; commit `3dbf0506045e21baf875e868e7bd5bc2822ef946` (2026-11-22T18:23:07-06:00); 41,077 sao theo GitHub API ngày 2026-11-23. Sao không đại diện chất lượng.
- **Bằng chứng:** [README.md](https://github.com/nushell/nushell/blob/3dbf0506045e21baf875e868e7bd5bc2822ef946/README.md) · [LICENSE](https://github.com/nushell/nushell/blob/3dbf0506045e21baf875e868e7bd5bc2822ef946/LICENSE) · [Cargo.toml](https://github.com/nushell/nushell/blob/3dbf0506045e21baf875e868e7bd5bc2822ef946/Cargo.toml) · [.github/workflows/ci.yml](https://github.com/nushell/nushell/blob/3dbf0506045e21baf875e868e7bd5bc2822ef946/.github/workflows/ci.yml) · [GitHub API](https://api.github.com/repos/nushell/nushell).

<a id="anhkysuai-ajeetdsouza-zoxide"></a>

### zoxide

- **Repo:** [ajeetdsouza/zoxide](https://github.com/ajeetdsouza/zoxide).
- **Mục đích:** Điều hướng thư mục bằng lịch sử sử dụng thay cho gõ đường dẫn dài.
- **Điểm đáng dùng:** README mô tả ghi nhớ thư mục thường dùng, tích hợp nhiều shell; CI có lint và test, Cargo yêu cầu Rust 1.88 nếu tự build.
- **License:** MIT.
- **Giới hạn:** Kết quả phụ thuộc lịch sử máy nên không phù hợp làm đường dẫn quyết định trong CI tái lập.
- **Tích hợp:** Dùng làm tiện ích cá nhân cho workspace nhiều repo, giữ automation dùng đường dẫn xác định.
- **Đối chiếu:** [fzf](../08-awesome-lists-learning/README.md#6c58-editor-terminal--dòng-lệnh) cho chọn thư mục; [fd](../13-dev-stack-devops/README.md#anhkysuai-sharkdp-fd) cho tìm đường dẫn; autojump cho điều hướng theo lịch sử.
- **Mức kiểm chứng:** `docs-read` — Đọc các phần mô tả và giới hạn trong README, thông báo license, metadata manifest và cấu hình CI khi có; chưa đọc toàn bộ mã triển khai, chưa cài hoặc chạy kiểm thử upstream.
- **Snapshot:** kiểm ngày 2026-11-23; commit `daf56a372ad33604aac986bbd44e5663b602cb42` (2026-11-22T03:22:21+05:30); 40,710 sao theo GitHub API ngày 2026-11-23. Sao không đại diện chất lượng.
- **Bằng chứng:** [README.md](https://github.com/ajeetdsouza/zoxide/blob/daf56a372ad33604aac986bbd44e5663b602cb42/README.md) · [LICENSE](https://github.com/ajeetdsouza/zoxide/blob/daf56a372ad33604aac986bbd44e5663b602cb42/LICENSE) · [Cargo.toml](https://github.com/ajeetdsouza/zoxide/blob/daf56a372ad33604aac986bbd44e5663b602cb42/Cargo.toml) · [.github/workflows/ci.yml](https://github.com/ajeetdsouza/zoxide/blob/daf56a372ad33604aac986bbd44e5663b602cb42/.github/workflows/ci.yml) · [GitHub API](https://api.github.com/repos/ajeetdsouza/zoxide).

<a id="anhkysuai-evanw-esbuild"></a>

### esbuild

- **Repo:** [evanw/esbuild](https://github.com/evanw/esbuild).
- **Mục đích:** Bundler/compiler JavaScript, TypeScript, JSX và CSS.
- **Điểm đáng dùng:** CLI, JavaScript và Go API cùng tree shaking, minify, sourcemap, watch và plugin giúp ghép pipeline nhỏ.
- **License:** MIT.
- **Giới hạn:** README tập trung tốc độ nhưng chưa đo tại đây; cần kiểm tra type riêng và xác minh plugin phù hợp khi build phức tạp.
- **Tích hợp:** Dùng cho build thư viện hoặc công cụ template, chốt target, external dependency và kiểm thử artifact sau bundle.
- **Đối chiếu:** [Vite](../13-dev-stack-devops/README.md) cho quy trình ứng dụng; [webpack](../13-dev-stack-devops/README.md#anhkysuai-webpack-webpack) cho loader/plugin rộng; [SWC](../13-dev-stack-devops/README.md#anhkysuai-swc-project-swc) cho compiler Rust.
- **Mức kiểm chứng:** `docs-read` — Đọc các phần mô tả và giới hạn trong README, thông báo license, metadata manifest và cấu hình CI khi có; chưa đọc toàn bộ mã triển khai, chưa cài hoặc chạy kiểm thử upstream.
- **Snapshot:** kiểm ngày 2026-11-23; commit `f6058f8364fe7ab91ca57a83e02577ed74c9cae4` (2026-08-09T13:17:12-04:00); 40,171 sao theo GitHub API ngày 2026-11-23. Sao không đại diện chất lượng.
- **Bằng chứng:** [README.md](https://github.com/evanw/esbuild/blob/f6058f8364fe7ab91ca57a83e02577ed74c9cae4/README.md) · [LICENSE.md](https://github.com/evanw/esbuild/blob/f6058f8364fe7ab91ca57a83e02577ed74c9cae4/LICENSE.md) · [go.mod](https://github.com/evanw/esbuild/blob/f6058f8364fe7ab91ca57a83e02577ed74c9cae4/go.mod) · [.github/workflows/ci.yml](https://github.com/evanw/esbuild/blob/f6058f8364fe7ab91ca57a83e02577ed74c9cae4/.github/workflows/ci.yml) · [GitHub API](https://api.github.com/repos/evanw/esbuild).

<a id="anhkysuai-dioxuslabs-dioxus"></a>

### Dioxus

- **Repo:** [DioxusLabs/dioxus](https://github.com/DioxusLabs/dioxus).
- **Mục đích:** Framework Rust xây UI web, desktop và mobile bằng một mô hình component.
- **Điểm đáng dùng:** Signals, server functions tích hợp axum và CLI bundle tạo chuỗi phát triển thống nhất; tài liệu phân biệt WebView với renderer native.
- **License:** MIT OR Apache-2.0.
- **Giới hạn:** Manifest tại SHA là 0.8 alpha; hotpatch và renderer WGPU được ghi thử nghiệm, không suy ra mọi target đạt cùng độ hoàn thiện.
- **Tích hợp:** Chọn một target cho mẫu thử, kiểm tra bridge native và SSR rồi khóa bộ phiên bản CLI/runtime.
- **Đối chiếu:** Leptos cho web Rust; [Yew](../13-dev-stack-devops/README.md#anhkysuai-yewstack-yew) cho Wasm component; [Tauri](../13-dev-stack-devops/README.md) cho desktop WebView.
- **Mức kiểm chứng:** `docs-read` — Đọc các phần mô tả và giới hạn trong README, thông báo license, metadata manifest và cấu hình CI khi có; chưa đọc toàn bộ mã triển khai, chưa cài hoặc chạy kiểm thử upstream.
- **Snapshot:** kiểm ngày 2026-11-23; commit `0a7242a2a72b08975584bf8ecb05076a5ee0b9c7` (2026-11-22T00:02:35Z); 39,883 sao theo GitHub API ngày 2026-11-23. Sao không đại diện chất lượng.
- **Bằng chứng:** [README.md](https://github.com/DioxusLabs/dioxus/blob/0a7242a2a72b08975584bf8ecb05076a5ee0b9c7/README.md) · [LICENSE-APACHE](https://github.com/DioxusLabs/dioxus/blob/0a7242a2a72b08975584bf8ecb05076a5ee0b9c7/LICENSE-APACHE) · [LICENSE-MIT](https://github.com/DioxusLabs/dioxus/blob/0a7242a2a72b08975584bf8ecb05076a5ee0b9c7/LICENSE-MIT) · [Cargo.toml](https://github.com/DioxusLabs/dioxus/blob/0a7242a2a72b08975584bf8ecb05076a5ee0b9c7/Cargo.toml) · [.github/workflows/main.yml](https://github.com/DioxusLabs/dioxus/blob/0a7242a2a72b08975584bf8ecb05076a5ee0b9c7/.github/workflows/main.yml) · [GitHub API](https://api.github.com/repos/DioxusLabs/dioxus).

<a id="anhkysuai-lapce-lapce"></a>

### Lapce

- **Repo:** [lapce/lapce](https://github.com/lapce/lapce).
- **Mục đích:** Code editor Rust dùng Floem/wgpu với LSP, terminal và remote development.
- **Điểm đáng dùng:** README nêu Rope Science cho cấu trúc văn bản, plugin biên dịch WASI và chế độ Vim tùy chọn.
- **License:** Apache-2.0.
- **Giới hạn:** Không giả định tương thích extension VS Code; ngôn ngữ, GPU và môi trường remote cần kiểm thử thực tế, build cần Rust 1.98 theo manifest.
- **Tích hợp:** Thử trên workspace và language server đang dùng trước khi chọn làm môi trường chuẩn cho xưởng.
- **Đối chiếu:** [VS Code](../08-awesome-lists-learning/README.md#6c58-editor-terminal--dòng-lệnh) cho extension rộng; [Zed](../08-awesome-lists-learning/README.md#6c58-editor-terminal--dòng-lệnh) cho editor native; [Helix](../13-dev-stack-devops/README.md#anhkysuai-helix-editor-helix) cho terminal LSP.
- **Mức kiểm chứng:** `docs-read` — Đọc các phần mô tả và giới hạn trong README, thông báo license, metadata manifest và cấu hình CI khi có; chưa đọc toàn bộ mã triển khai, chưa cài hoặc chạy kiểm thử upstream.
- **Snapshot:** kiểm ngày 2026-11-23; commit `9e8317c84e9540ac0b09689dd9f9d4fafe44ac00` (2026-11-18T14:40:26+01:00); 39,104 sao theo GitHub API ngày 2026-11-23. Sao không đại diện chất lượng.
- **Bằng chứng:** [README.md](https://github.com/lapce/lapce/blob/9e8317c84e9540ac0b09689dd9f9d4fafe44ac00/README.md) · [LICENSE](https://github.com/lapce/lapce/blob/9e8317c84e9540ac0b09689dd9f9d4fafe44ac00/LICENSE) · [Cargo.toml](https://github.com/lapce/lapce/blob/9e8317c84e9540ac0b09689dd9f9d4fafe44ac00/Cargo.toml) · [.github/workflows/ci.yml](https://github.com/lapce/lapce/blob/9e8317c84e9540ac0b09689dd9f9d4fafe44ac00/.github/workflows/ci.yml) · [GitHub API](https://api.github.com/repos/lapce/lapce).

<a id="anhkysuai-servo-servo"></a>

### Servo

- **Repo:** [servo/servo](https://github.com/servo/servo).
- **Mục đích:** Engine trình duyệt viết Rust, phục vụ nghiên cứu và nhúng nền web.
- **Điểm đáng dùng:** README liệt kê host Linux/macOS/Windows/Android/OpenHarmony cùng bootstrap/mach build; Cargo mô tả workspace engine.
- **License:** MPL-2.0; phần đặc tả WHATWG BSD-3-Clause.
- **Giới hạn:** Tác giả gọi đây là prototype; không suy ra độ tương thích web hay mô hình bảo mật tương đương browser ổn định, build có nhiều dependency hệ thống.
- **Tích hợp:** Dùng làm tham khảo hoặc thử nhúng giới hạn, chạy tập trang và chuẩn web cần thiết trước quyết định sản phẩm.
- **Đối chiếu:** Chromium cho engine phổ biến; WebKit cho nền Apple; Ladybird cho hướng engine độc lập.
- **Mức kiểm chứng:** `docs-read` — Đọc các phần mô tả và giới hạn trong README, thông báo license, metadata manifest và cấu hình CI khi có; chưa đọc toàn bộ mã triển khai, chưa cài hoặc chạy kiểm thử upstream.
- **Snapshot:** kiểm ngày 2026-11-23; commit `2e22bffd4692a39290fe1cb8646e4424c0c8be80` (2026-11-23T06:30:40Z); 38,596 sao theo GitHub API ngày 2026-11-23. Sao không đại diện chất lượng.
- **Bằng chứng:** [README.md](https://github.com/servo/servo/blob/2e22bffd4692a39290fe1cb8646e4424c0c8be80/README.md) · [LICENSE](https://github.com/servo/servo/blob/2e22bffd4692a39290fe1cb8646e4424c0c8be80/LICENSE) · [LICENSE_WHATWG_SPECS](https://github.com/servo/servo/blob/2e22bffd4692a39290fe1cb8646e4424c0c8be80/LICENSE_WHATWG_SPECS) · [pyproject.toml](https://github.com/servo/servo/blob/2e22bffd4692a39290fe1cb8646e4424c0c8be80/pyproject.toml) · [Cargo.toml](https://github.com/servo/servo/blob/2e22bffd4692a39290fe1cb8646e4424c0c8be80/Cargo.toml) · [.github/workflows/try.yml](https://github.com/servo/servo/blob/2e22bffd4692a39290fe1cb8646e4424c0c8be80/.github/workflows/try.yml) · [GitHub API](https://api.github.com/repos/servo/servo).

<a id="anhkysuai-vlang-v"></a>

### V

**Đã chuyển (2026-11-23):** hồ sơ này nay nằm ở [mục 37](../37-programming-languages-runtimes/README.md#anhkysuai-vlang-v); catalog con xem [catalog/](../catalog/README.md).

<a id="anhkysuai-nervjs-taro"></a>

### Taro

- **Repo:** [NervJS/taro](https://github.com/NervJS/taro).
- **Mục đích:** Biên dịch ứng dụng React/Vue/Nerv sang nhiều nền mini-program, Web và React Native.
- **Điểm đáng dùng:** README có ma trận UI library theo framework/major Taro, hướng dẫn migration; manifest snapshot 4.3.3.
- **License:** MIT.
- **Giới hạn:** API và khả năng nền tảng khác nhau, một nguồn mã không loại bỏ kiểm thử từng target; UI package phải khớp major.
- **Tích hợp:** Chọn nền cần phát hành, tách adapter riêng và làm mẫu luồng quyền, điều hướng, thanh toán thực tế.
- **Đối chiếu:** [uni-app](../13-dev-stack-devops/README.md#anhkysuai-dcloudio-uni-app) cho Vue đa nền; [Expo](../13-dev-stack-devops/README.md#anhkysuai-expo-expo) cho React Native; [Flutter](../13-dev-stack-devops/README.md) cho UI đa nền.
- **Mức kiểm chứng:** `docs-read` — Đọc các phần mô tả và giới hạn trong README, thông báo license, metadata manifest và cấu hình CI khi có; chưa đọc toàn bộ mã triển khai, chưa cài hoặc chạy kiểm thử upstream.
- **Snapshot:** kiểm ngày 2026-11-23; commit `99683d13bf1f57ba02dceabdb4690034b4469b0a` (2026-11-23T15:52:34+08:00); 37,768 sao theo GitHub API ngày 2026-11-23. Sao không đại diện chất lượng.
- **Bằng chứng:** [README.md](https://github.com/NervJS/taro/blob/99683d13bf1f57ba02dceabdb4690034b4469b0a/README.md) · [LICENSE](https://github.com/NervJS/taro/blob/99683d13bf1f57ba02dceabdb4690034b4469b0a/LICENSE) · [package.json](https://github.com/NervJS/taro/blob/99683d13bf1f57ba02dceabdb4690034b4469b0a/package.json) · [Cargo.toml](https://github.com/NervJS/taro/blob/99683d13bf1f57ba02dceabdb4690034b4469b0a/Cargo.toml) · [.github/workflows/build-rust-wasm.yml](https://github.com/NervJS/taro/blob/99683d13bf1f57ba02dceabdb4690034b4469b0a/.github/workflows/build-rust-wasm.yml) · [GitHub API](https://api.github.com/repos/NervJS/taro).

<a id="anhkysuai-wailsapp-wails"></a>

### Wails

- **Repo:** [wailsapp/wails](https://github.com/wailsapp/wails).
- **Mục đích:** Đóng gói backend Go và frontend web thành ứng dụng desktop.
- **Điểm đáng dùng:** Tự sinh TypeScript binding cho struct/method, dùng engine render hệ thống và hỗ trợ dialog/menu native.
- **License:** MIT.
- **Giới hạn:** README có cả v2 và v3 stable, trong khi workflow thu thập là Build + Test v2; không lấy CI một major chứng minh major khác.
- **Tích hợp:** Chọn major rõ, kiểm tra binding được expose và WebView từng OS rồi thiết kế ký gói/cập nhật.
- **Đối chiếu:** [Tauri](../13-dev-stack-devops/README.md) cho backend Rust; [Electron](../08-awesome-lists-learning/README.md#6c528-ứng-dụng-đa-nền-tảng--game) cho runtime Chromium; [NW.js](../13-dev-stack-devops/README.md#anhkysuai-nwjs-nw-js) cho Node trong DOM.
- **Mức kiểm chứng:** `docs-read` — Đọc các phần mô tả và giới hạn trong README, thông báo license, metadata manifest và cấu hình CI khi có; chưa đọc toàn bộ mã triển khai, chưa cài hoặc chạy kiểm thử upstream.
- **Snapshot:** kiểm ngày 2026-11-23; commit `1569f2490daa24dd1b88154c699374fbc377af2f` (2026-11-23T00:18:46Z); 37,180 sao theo GitHub API ngày 2026-11-23. Sao không đại diện chất lượng.
- **Bằng chứng:** [README.md](https://github.com/wailsapp/wails/blob/1569f2490daa24dd1b88154c699374fbc377af2f/README.md) · [LICENSE](https://github.com/wailsapp/wails/blob/1569f2490daa24dd1b88154c699374fbc377af2f/LICENSE) · [.github/workflows/build-and-test.yml](https://github.com/wailsapp/wails/blob/1569f2490daa24dd1b88154c699374fbc377af2f/.github/workflows/build-and-test.yml) · [GitHub API](https://api.github.com/repos/wailsapp/wails).

<a id="anhkysuai-pnpm-pnpm"></a>

### pnpm

- **Repo:** [pnpm/pnpm](https://github.com/pnpm/pnpm).
- **Mục đích:** Quản lý package JavaScript với content-addressable store và workspace.
- **Điểm đáng dùng:** README mô tả hard-link/reflink tái dùng file, quyền truy cập dependency nghiêm theo manifest và lockfile xác định.
- **License:** MIT; pnpr/ là PolyForm Shield 1.0.0 source-available.
- **Giới hạn:** Monorepo không hoàn toàn MIT vì pnpr/ có hạn chế riêng; pacquet là Rust port thử nghiệm, hiệu năng chưa đo tại đây.
- **Tích hợp:** Khóa packageManager/lockfile, dùng cài đặt frozen trong CI và kiểm tra script dependency cùng license phần được đóng gói.
- **Đối chiếu:** npm cho chuẩn Node; Yarn cho workspace; [Bun](../13-dev-stack-devops/README.md) cho runtime và package manager.
- **Mức kiểm chứng:** `docs-read` — Đọc các phần mô tả và giới hạn trong README, thông báo license, metadata manifest và cấu hình CI khi có; chưa đọc toàn bộ mã triển khai, chưa cài hoặc chạy kiểm thử upstream.
- **Snapshot:** kiểm ngày 2026-11-23; commit `a6d032bb5fcb03ec251ecacda5cc6f2030f136e9` (2026-11-23T02:25:03+01:00); 37,156 sao theo GitHub API ngày 2026-11-23. Sao không đại diện chất lượng.
- **Bằng chứng:** [README.md](https://github.com/pnpm/pnpm/blob/a6d032bb5fcb03ec251ecacda5cc6f2030f136e9/README.md) · [LICENSE](https://github.com/pnpm/pnpm/blob/a6d032bb5fcb03ec251ecacda5cc6f2030f136e9/LICENSE) · [package.json](https://github.com/pnpm/pnpm/blob/a6d032bb5fcb03ec251ecacda5cc6f2030f136e9/package.json) · [Cargo.toml](https://github.com/pnpm/pnpm/blob/a6d032bb5fcb03ec251ecacda5cc6f2030f136e9/Cargo.toml) · [.github/workflows/ci.yml](https://github.com/pnpm/pnpm/blob/a6d032bb5fcb03ec251ecacda5cc6f2030f136e9/.github/workflows/ci.yml) · [pnpr/LICENSE.md](https://github.com/pnpm/pnpm/blob/a6d032bb5fcb03ec251ecacda5cc6f2030f136e9/pnpr/LICENSE.md) · [GitHub API](https://api.github.com/repos/pnpm/pnpm).

<a id="anhkysuai-zellij-org-zellij"></a>

### Zellij

- **Repo:** [zellij-org/zellij](https://github.com/zellij-org/zellij).
- **Mục đích:** Workspace terminal nhiều pane, session và bố cục cấu hình được.
- **Điểm đáng dùng:** Plugin WebAssembly, pane nổi/xếp chồng, cộng tác và web client là các khả năng được tài liệu mô tả; có workflow E2E.
- **License:** MIT.
- **Giới hạn:** README cảnh báo main là prerelease và có thể làm hỏng cache; web client/cộng tác đòi hỏi kiểm soát quyền vào terminal.
- **Tích hợp:** Khóa release để tạo layout công cụ của nhóm, thử khôi phục session và cấu hình truy cập trước khi dùng chung.
- **Đối chiếu:** tmux cho multiplexer; [WezTerm](../13-dev-stack-devops/README.md#anhkysuai-wezterm-wezterm) cho terminal tích hợp; [Kitty](../13-dev-stack-devops/README.md#anhkysuai-kovidgoyal-kitty) cho GPU terminal.
- **Mức kiểm chứng:** `docs-read` — Đọc các phần mô tả và giới hạn trong README, thông báo license, metadata manifest và cấu hình CI khi có; chưa đọc toàn bộ mã triển khai, chưa cài hoặc chạy kiểm thử upstream.
- **Snapshot:** kiểm ngày 2026-11-23; commit `c01b6fa3dce5c56ac8e75b68dfcfa26e550111b7` (2026-11-23T09:37:02+01:00); 36,194 sao theo GitHub API ngày 2026-11-23. Sao không đại diện chất lượng.
- **Bằng chứng:** [README.md](https://github.com/zellij-org/zellij/blob/c01b6fa3dce5c56ac8e75b68dfcfa26e550111b7/README.md) · [LICENSE.md](https://github.com/zellij-org/zellij/blob/c01b6fa3dce5c56ac8e75b68dfcfa26e550111b7/LICENSE.md) · [Cargo.toml](https://github.com/zellij-org/zellij/blob/c01b6fa3dce5c56ac8e75b68dfcfa26e550111b7/Cargo.toml) · [.github/workflows/e2e.yml](https://github.com/zellij-org/zellij/blob/c01b6fa3dce5c56ac8e75b68dfcfa26e550111b7/.github/workflows/e2e.yml) · [GitHub API](https://api.github.com/repos/zellij-org/zellij).

<a id="anhkysuai-kovidgoyal-kitty"></a>

### Kitty

- **Repo:** [kovidgoyal/kitty](https://github.com/kovidgoyal/kitty).
- **Mục đích:** Terminal dùng GPU cho Linux, macOS và BSD.
- **Điểm đáng dùng:** docs/index.rst mô tả graphics/keyboard protocol, tab/split, session và Python kittens; CI xây với nhiều Python/compiler/sanitizer.
- **License:** GPL-3.0-only.
- **Giới hạn:** README root là AsciiDoc nên đã đọc thêm đúng tài liệu, không suy tính năng từ README của thư mục gen; remote-control cần giới hạn quyền.
- **Tích hợp:** Thử trên GPU, font và shell của nhóm, lưu cấu hình session và chỉ bật điều khiển từ ngoài khi cần.
- **Đối chiếu:** [WezTerm](../13-dev-stack-devops/README.md#anhkysuai-wezterm-wezterm) cho terminal/multiplexer; [Alacritty](../13-dev-stack-devops/README.md#anhkysuai-alacritty-alacritty) cho terminal gọn; [Zellij](../13-dev-stack-devops/README.md#anhkysuai-zellij-org-zellij) cho workspace terminal.
- **Mức kiểm chứng:** `docs-read` — Đọc các phần mô tả và giới hạn trong README, thông báo license, metadata manifest và cấu hình CI khi có; chưa đọc toàn bộ mã triển khai, chưa cài hoặc chạy kiểm thử upstream.
- **Snapshot:** kiểm ngày 2026-11-23; commit `1dadc7931b7ccfa1b05d2fbe044e1c094e766862` (2026-11-23T11:11:26+05:30); 35,806 sao theo GitHub API ngày 2026-11-23. Sao không đại diện chất lượng.
- **Bằng chứng:** [gen/README.rst](https://github.com/kovidgoyal/kitty/blob/1dadc7931b7ccfa1b05d2fbe044e1c094e766862/gen/README.rst) · [LICENSE](https://github.com/kovidgoyal/kitty/blob/1dadc7931b7ccfa1b05d2fbe044e1c094e766862/LICENSE) · [pyproject.toml](https://github.com/kovidgoyal/kitty/blob/1dadc7931b7ccfa1b05d2fbe044e1c094e766862/pyproject.toml) · [go.mod](https://github.com/kovidgoyal/kitty/blob/1dadc7931b7ccfa1b05d2fbe044e1c094e766862/go.mod) · [.github/workflows/ci.yml](https://github.com/kovidgoyal/kitty/blob/1dadc7931b7ccfa1b05d2fbe044e1c094e766862/.github/workflows/ci.yml) · [README.asciidoc](https://github.com/kovidgoyal/kitty/blob/1dadc7931b7ccfa1b05d2fbe044e1c094e766862/README.asciidoc) · [docs/index.rst](https://github.com/kovidgoyal/kitty/blob/1dadc7931b7ccfa1b05d2fbe044e1c094e766862/docs/index.rst) · [GitHub API](https://api.github.com/repos/kovidgoyal/kitty).

<a id="anhkysuai-fish-shell-fish-shell"></a>

### fish

- **Repo:** [fish-shell/fish-shell](https://github.com/fish-shell/fish-shell).
- **Mục đích:** Shell tương tác có gợi ý, tô cú pháp và completion sẵn.
- **Điểm đáng dùng:** Tài liệu hướng dẫn thử trong shell hiện tại, hỗ trợ Windows qua WSL/Cygwin/MSYS2; Cargo và COPYING nêu rõ license thành phần.
- **License:** GPL-2.0-only AND LGPL-2.0-or-later AND MIT AND PSF-2.0.
- **Giới hạn:** Cú pháp khác POSIX nên script bash không tự chạy tương thích; cấu hình cá nhân không thay môi trường CI xác định.
- **Tích hợp:** Dùng cho trải nghiệm developer, giữ script dự án có shebang và runtime riêng, kiểm tra completion tùy chỉnh.
- **Đối chiếu:** Zsh cho shell mở rộng; [Nushell](../13-dev-stack-devops/README.md#anhkysuai-nushell-nushell) cho dữ liệu có cấu trúc; [PowerShell](../13-dev-stack-devops/README.md#anhkysuai-powershell-powershell) cho pipeline đối tượng.
- **Mức kiểm chứng:** `docs-read` — Đọc các phần mô tả và giới hạn trong README, thông báo license, metadata manifest và cấu hình CI khi có; chưa đọc toàn bộ mã triển khai, chưa cài hoặc chạy kiểm thử upstream.
- **Snapshot:** kiểm ngày 2026-11-23; commit `bc93a5b80e72b02c9b33237e55e29a82077d3372` (2026-11-21T13:17:40+08:00); 34,513 sao theo GitHub API ngày 2026-11-23. Sao không đại diện chất lượng.
- **Bằng chứng:** [README.rst](https://github.com/fish-shell/fish-shell/blob/bc93a5b80e72b02c9b33237e55e29a82077d3372/README.rst) · [COPYING](https://github.com/fish-shell/fish-shell/blob/bc93a5b80e72b02c9b33237e55e29a82077d3372/COPYING) · [pyproject.toml](https://github.com/fish-shell/fish-shell/blob/bc93a5b80e72b02c9b33237e55e29a82077d3372/pyproject.toml) · [Cargo.toml](https://github.com/fish-shell/fish-shell/blob/bc93a5b80e72b02c9b33237e55e29a82077d3372/Cargo.toml) · [.github/workflows/test.yml](https://github.com/fish-shell/fish-shell/blob/bc93a5b80e72b02c9b33237e55e29a82077d3372/.github/workflows/test.yml) · [GitHub API](https://api.github.com/repos/fish-shell/fish-shell).

<a id="anhkysuai-python-poetry-poetry"></a>

### Poetry

- **Repo:** [python-poetry/poetry](https://github.com/python-poetry/poetry).
- **Mục đích:** Quản lý dependency và đóng gói dự án Python dựa trên pyproject.toml.
- **Điểm đáng dùng:** README phân biệt poetry-core PEP 517 và plugin export/bundle; CI kiểm tra lockfile và smoke-test build/install.
- **License:** MIT.
- **Giới hạn:** SHA đọc là 2.6.0.dev0, yêu cầu Python >=3.11; plugin export không nên coi là tính năng mặc định mọi bản.
- **Tích hợp:** Khóa phiên bản Poetry và lockfile cho mẫu, kiểm tra gói wheel và cài sạch trên Python hỗ trợ.
- **Đối chiếu:** [uv](../13-dev-stack-devops/README.md) cho workflow Python; PDM cho PEP 582/virtualenv; Hatch cho môi trường và build.
- **Mức kiểm chứng:** `docs-read` — Đọc các phần mô tả và giới hạn trong README, thông báo license, metadata manifest và cấu hình CI khi có; chưa đọc toàn bộ mã triển khai, chưa cài hoặc chạy kiểm thử upstream.
- **Snapshot:** kiểm ngày 2026-11-23; commit `3cc663a738522c90dc2b50fcadc74e39ada4b73a` (2026-11-21T11:01:56+01:00); 34,324 sao theo GitHub API ngày 2026-11-23. Sao không đại diện chất lượng.
- **Bằng chứng:** [README.md](https://github.com/python-poetry/poetry/blob/3cc663a738522c90dc2b50fcadc74e39ada4b73a/README.md) · [LICENSE](https://github.com/python-poetry/poetry/blob/3cc663a738522c90dc2b50fcadc74e39ada4b73a/LICENSE) · [pyproject.toml](https://github.com/python-poetry/poetry/blob/3cc663a738522c90dc2b50fcadc74e39ada4b73a/pyproject.toml) · [.github/workflows/tests.yaml](https://github.com/python-poetry/poetry/blob/3cc663a738522c90dc2b50fcadc74e39ada4b73a/.github/workflows/tests.yaml) · [GitHub API](https://api.github.com/repos/python-poetry/poetry).

<a id="anhkysuai-swc-project-swc"></a>

### SWC

- **Repo:** [swc-project/swc](https://github.com/swc-project/swc).
- **Mục đích:** Compiler JavaScript/TypeScript Rust với API cho Rust và JavaScript.
- **Điểm đáng dùng:** Parser là điểm vào thư viện; README mô tả native addon tự giải nén theo target và CI kiểm hợp đồng artifact.
- **License:** Apache-2.0 chủ yếu; kiểm tra thông báo từng thành phần.
- **Giới hạn:** Hỗ trợ target native và cache binary cần phù hợp môi trường triển khai; compiler không thay type checker, số tốc độ chưa đo.
- **Tích hợp:** Khóa bộ crate/package tương thích, kiểm tra transform plugin và artifact trên OS/CPU sử dụng.
- **Đối chiếu:** [Babel](../13-dev-stack-devops/README.md#anhkysuai-babel-babel) cho hệ plugin; [esbuild](../13-dev-stack-devops/README.md#anhkysuai-evanw-esbuild) cho bundling; TypeScript compiler cho kiểm tra kiểu.
- **Mức kiểm chứng:** `docs-read` — Đọc các phần mô tả và giới hạn trong README, thông báo license, metadata manifest và cấu hình CI khi có; chưa đọc toàn bộ mã triển khai, chưa cài hoặc chạy kiểm thử upstream.
- **Snapshot:** kiểm ngày 2026-11-23; commit `62f1d603c7e88c0aabfb496104ccb720c41295f8` (2026-11-23T08:47:32Z); 34,222 sao theo GitHub API ngày 2026-11-23. Sao không đại diện chất lượng.
- **Bằng chứng:** [README.md](https://github.com/swc-project/swc/blob/62f1d603c7e88c0aabfb496104ccb720c41295f8/README.md) · [LICENSE](https://github.com/swc-project/swc/blob/62f1d603c7e88c0aabfb496104ccb720c41295f8/LICENSE) · [package.json](https://github.com/swc-project/swc/blob/62f1d603c7e88c0aabfb496104ccb720c41295f8/package.json) · [Cargo.toml](https://github.com/swc-project/swc/blob/62f1d603c7e88c0aabfb496104ccb720c41295f8/Cargo.toml) · [.github/workflows/CI.yml](https://github.com/swc-project/swc/blob/62f1d603c7e88c0aabfb496104ccb720c41295f8/.github/workflows/CI.yml) · [GitHub API](https://api.github.com/repos/swc-project/swc).

<a id="anhkysuai-vscodium-vscodium"></a>

### VSCodium

- **Repo:** [VSCodium/vscodium](https://github.com/VSCodium/vscodium).
- **Mục đích:** Script tạo bản phân phối VS Code với cấu hình cộng đồng.
- **Điểm đáng dùng:** README nói rõ đây là repo tự động build vscode, không phải fork editor độc lập; CI Linux thể hiện chuỗi xây gói.
- **License:** MIT cho script/build; extension và thành phần theo license riêng.
- **Giới hạn:** Không giả định mọi Microsoft extension/dịch vụ dùng được với bản này; license và marketplace của extension cần xem riêng.
- **Tích hợp:** Dùng cấu hình editor có kiểm kê extension, kiểm tra debug/remote workflow thực tế trước khi chuẩn hóa môi trường.
- **Đối chiếu:** [VS Code](../08-awesome-lists-learning/README.md#6c58-editor-terminal--dòng-lệnh) cho bản Microsoft; Theia cho IDE tùy biến; [Zed](../08-awesome-lists-learning/README.md#6c58-editor-terminal--dòng-lệnh) cho editor native.
- **Mức kiểm chứng:** `docs-read` — Đọc các phần mô tả và giới hạn trong README, thông báo license, metadata manifest và cấu hình CI khi có; chưa đọc toàn bộ mã triển khai, chưa cài hoặc chạy kiểm thử upstream.
- **Snapshot:** kiểm ngày 2026-11-23; commit `ca7f7b44b5e5c3faa663f6cdc043998f71936653` (2026-10-27T20:32:28+01:00); 34,230 sao theo GitHub API ngày 2026-11-23. Sao không đại diện chất lượng.
- **Bằng chứng:** [README.md](https://github.com/VSCodium/vscodium/blob/ca7f7b44b5e5c3faa663f6cdc043998f71936653/README.md) · [LICENSE](https://github.com/VSCodium/vscodium/blob/ca7f7b44b5e5c3faa663f6cdc043998f71936653/LICENSE) · [.github/workflows/ci-build-linux.yml](https://github.com/VSCodium/vscodium/blob/ca7f7b44b5e5c3faa663f6cdc043998f71936653/.github/workflows/ci-build-linux.yml) · [GitHub API](https://api.github.com/repos/VSCodium/vscodium).

<a id="anhkysuai-carbon-language-carbon-lang"></a>

### Carbon Language

**Đã chuyển (2026-11-23):** hồ sơ này nay nằm ở [mục 37](../37-programming-languages-runtimes/README.md#anhkysuai-carbon-language-carbon-lang); catalog con xem [catalog/](../catalog/README.md).

<a id="anhkysuai-tokio-rs-tokio"></a>

### Tokio

- **Repo:** [tokio-rs/tokio](https://github.com/tokio-rs/tokio).
- **Mục đích:** Runtime bất đồng bộ Rust cho tác vụ mạng và I/O.
- **Điểm đáng dùng:** README phân biệt scheduler work-stealing, reactor event queue và socket async; feature flags cho phép chọn thành phần.
- **License:** MIT.
- **Giới hạn:** Type safety không loại bỏ logic race hoặc nghẽn do công việc blocking; backpressure/cancellation cần thiết kế trong ứng dụng.
- **Tích hợp:** Chọn feature tối thiểu, đặt timeout và giới hạn concurrency, đưa công việc CPU/blocking sang executor phù hợp.
- **Đối chiếu:** smol cho runtime gọn; async-std cho API quen std; Go runtime cho ứng dụng Go.
- **Mức kiểm chứng:** `docs-read` — Đọc các phần mô tả và giới hạn trong README, thông báo license, metadata manifest và cấu hình CI khi có; chưa đọc toàn bộ mã triển khai, chưa cài hoặc chạy kiểm thử upstream.
- **Snapshot:** kiểm ngày 2026-11-23; commit `675ba8164071a6eee3dd1f3cb4fbdc1d3664396e` (2026-11-22T00:44:33+01:00); 33,770 sao theo GitHub API ngày 2026-11-23. Sao không đại diện chất lượng.
- **Bằng chứng:** [README.md](https://github.com/tokio-rs/tokio/blob/675ba8164071a6eee3dd1f3cb4fbdc1d3664396e/README.md) · [LICENSE](https://github.com/tokio-rs/tokio/blob/675ba8164071a6eee3dd1f3cb4fbdc1d3664396e/LICENSE) · [Cargo.toml](https://github.com/tokio-rs/tokio/blob/675ba8164071a6eee3dd1f3cb4fbdc1d3664396e/Cargo.toml) · [.github/workflows/ci.yml](https://github.com/tokio-rs/tokio/blob/675ba8164071a6eee3dd1f3cb4fbdc1d3664396e/.github/workflows/ci.yml) · [GitHub API](https://api.github.com/repos/tokio-rs/tokio).

<a id="anhkysuai-remix-run-remix"></a>

### Remix

- **Repo:** [remix-run/remix](https://github.com/remix-run/remix).
- **Mục đích:** Framework TypeScript full-stack với router dựa trên Request/Response chuẩn web.
- **Điểm đáng dùng:** README snapshot mô tả runtime trực tiếp, package remix/router và remix/component cùng adapter server, yêu cầu Node >=24.3.
- **License:** MIT.
- **Giới hạn:** Đây là kiến trúc tài liệu hiện tại, không mặc định áp ví dụ Remix cũ/React Router; cài từ main là preview commit cụ thể.
- **Tích hợp:** Khóa release và tài liệu cùng phiên bản, test route bằng Request cùng phiên đăng nhập/form trên browser thật.
- **Đối chiếu:** [Next.js](../13-dev-stack-devops/README.md) cho React; SvelteKit cho Svelte; [Hono](../13-dev-stack-devops/README.md) cho server Fetch API.
- **Mức kiểm chứng:** `docs-read` — Đọc các phần mô tả và giới hạn trong README, thông báo license, metadata manifest và cấu hình CI khi có; chưa đọc toàn bộ mã triển khai, chưa cài hoặc chạy kiểm thử upstream.
- **Snapshot:** kiểm ngày 2026-11-23; commit `b42a817e3a00ddadee82a3373441f53e41fde081` (2026-11-23T11:30:47+11:00); 33,475 sao theo GitHub API ngày 2026-11-23. Sao không đại diện chất lượng.
- **Bằng chứng:** [README.md](https://github.com/remix-run/remix/blob/b42a817e3a00ddadee82a3373441f53e41fde081/README.md) · [LICENSE](https://github.com/remix-run/remix/blob/b42a817e3a00ddadee82a3373441f53e41fde081/LICENSE) · [package.json](https://github.com/remix-run/remix/blob/b42a817e3a00ddadee82a3373441f53e41fde081/package.json) · [.github/workflows/check-pr.yaml](https://github.com/remix-run/remix/blob/b42a817e3a00ddadee82a3373441f53e41fde081/.github/workflows/check-pr.yaml) · [GitHub API](https://api.github.com/repos/remix-run/remix).

<a id="anhkysuai-yewstack-yew"></a>

### Yew

- **Repo:** [yewstack/yew](https://github.com/yewstack/yew).
- **Mục đích:** Framework Rust/Wasm cho UI web theo component.
- **Điểm đáng dùng:** Macro HTML kết hợp biểu thức Rust, tương tác JavaScript và worker là cơ chế tài liệu mô tả; CI có documentation tests với wasm-bindgen.
- **License:** MIT OR Apache-2.0.
- **Giới hạn:** Wasm không loại bỏ chi phí DOM hay JS interop; phải kiểm tra kích thước tải, khả năng server render và tooling cần dùng.
- **Tích hợp:** Thử một widget tính toán trên web, giữ hợp đồng JS rõ và đo cold load trước khi dùng toàn ứng dụng.
- **Đối chiếu:** Leptos cho reactive Rust; [Dioxus](../13-dev-stack-devops/README.md#anhkysuai-dioxuslabs-dioxus) cho nhiều target; React cho hệ sinh thái JS.
- **Mức kiểm chứng:** `docs-read` — Đọc các phần mô tả và giới hạn trong README, thông báo license, metadata manifest và cấu hình CI khi có; chưa đọc toàn bộ mã triển khai, chưa cài hoặc chạy kiểm thử upstream.
- **Snapshot:** kiểm ngày 2026-11-23; commit `5ee55894001d8671f10f5019bada02fe54400861` (2026-11-23T03:12:50+09:00); 32,871 sao theo GitHub API ngày 2026-11-23. Sao không đại diện chất lượng.
- **Bằng chứng:** [README.md](https://github.com/yewstack/yew/blob/5ee55894001d8671f10f5019bada02fe54400861/README.md) · [LICENSE-APACHE](https://github.com/yewstack/yew/blob/5ee55894001d8671f10f5019bada02fe54400861/LICENSE-APACHE) · [LICENSE-MIT](https://github.com/yewstack/yew/blob/5ee55894001d8671f10f5019bada02fe54400861/LICENSE-MIT) · [Cargo.toml](https://github.com/yewstack/yew/blob/5ee55894001d8671f10f5019bada02fe54400861/Cargo.toml) · [.github/workflows/main-checks.yml](https://github.com/yewstack/yew/blob/5ee55894001d8671f10f5019bada02fe54400861/.github/workflows/main-checks.yml) · [packages/yew/Cargo.toml](https://github.com/yewstack/yew/blob/5ee55894001d8671f10f5019bada02fe54400861/packages/yew/Cargo.toml) · [GitHub API](https://api.github.com/repos/yewstack/yew).

<a id="anhkysuai-dandavison-delta"></a>

### Delta

- **Repo:** [dandavison/delta](https://github.com/dandavison/delta).
- **Mục đích:** Pager tô cú pháp và bố trí diff cho Git, grep và review terminal.
- **Điểm đáng dùng:** Word-level diff, side-by-side, merge conflict và hyperlink hỗ trợ đọc thay đổi; README có chế độ TUI dựa trên gitu.
- **License:** MIT.
- **Giới hạn:** Chế độ TUI còn có stage, commit, rebase nên không chỉ đọc; định dạng màu không thay diff thô dùng cho automation.
- **Tích hợp:** Dùng pager cho người duyệt, giữ đầu ra không màu/không pager trong pipeline và kiểm tra keybinding thao tác ghi.
- **Đối chiếu:** Difftastic cho diff cú pháp; GitUI cho giao diện Git; git diff cho đầu ra gốc.
- **Mức kiểm chứng:** `docs-read` — Đọc các phần mô tả và giới hạn trong README, thông báo license, metadata manifest và cấu hình CI khi có; chưa đọc toàn bộ mã triển khai, chưa cài hoặc chạy kiểm thử upstream.
- **Snapshot:** kiểm ngày 2026-11-23; commit `17a08ca1c593e5cb821f6da6d19627ba20670684` (2026-11-22T23:12:26-05:00); 32,815 sao theo GitHub API ngày 2026-11-23. Sao không đại diện chất lượng.
- **Bằng chứng:** [README.md](https://github.com/dandavison/delta/blob/17a08ca1c593e5cb821f6da6d19627ba20670684/README.md) · [LICENSE](https://github.com/dandavison/delta/blob/17a08ca1c593e5cb821f6da6d19627ba20670684/LICENSE) · [Cargo.toml](https://github.com/dandavison/delta/blob/17a08ca1c593e5cb821f6da6d19627ba20670684/Cargo.toml) · [.github/workflows/ci.yml](https://github.com/dandavison/delta/blob/17a08ca1c593e5cb821f6da6d19627ba20670684/.github/workflows/ci.yml) · [GitHub API](https://api.github.com/repos/dandavison/delta).

<a id="anhkysuai-atuinsh-atuin"></a>

### Atuin

- **Repo:** [atuinsh/atuin](https://github.com/atuinsh/atuin).
- **Mục đích:** Lưu và tìm lịch sử shell cùng thread công cụ agent.
- **Điểm đáng dùng:** SQLite giữ lệnh, exit code, thư mục, host và thời lượng; README mô tả đồng bộ E2EE tùy chọn hoặc dùng offline, MCP để agent tìm kiếm.
- **License:** MIT.
- **Giới hạn:** Lịch sử có thể chứa secret và thông tin dự án; claim mã hóa chưa được audit ở đây, cấp MCP mở thêm phạm vi dữ liệu cho agent.
- **Tích hợp:** Thử offline trước, thiết lập loại trừ lệnh nhạy cảm và chính sách lưu giữ trước khi bật sync/MCP.
- **Đối chiếu:** [fzf](../08-awesome-lists-learning/README.md#6c58-editor-terminal--dòng-lệnh) với history shell; McFly cho tìm lệnh; terminal history mặc định cho phạm vi nhỏ.
- **Mức kiểm chứng:** `docs-read` — Đọc các phần mô tả và giới hạn trong README, thông báo license, metadata manifest và cấu hình CI khi có; chưa đọc toàn bộ mã triển khai, chưa cài hoặc chạy kiểm thử upstream.
- **Snapshot:** kiểm ngày 2026-11-23; commit `86573ef2dbeb8be5eea3835b91fbf5d5fc93991f` (2026-11-21T03:57:08Z); 32,575 sao theo GitHub API ngày 2026-11-23. Sao không đại diện chất lượng.
- **Bằng chứng:** [README.md](https://github.com/atuinsh/atuin/blob/86573ef2dbeb8be5eea3835b91fbf5d5fc93991f/README.md) · [LICENSE](https://github.com/atuinsh/atuin/blob/86573ef2dbeb8be5eea3835b91fbf5d5fc93991f/LICENSE) · [Cargo.toml](https://github.com/atuinsh/atuin/blob/86573ef2dbeb8be5eea3835b91fbf5d5fc93991f/Cargo.toml) · [.github/workflows/docker.yaml](https://github.com/atuinsh/atuin/blob/86573ef2dbeb8be5eea3835b91fbf5d5fc93991f/.github/workflows/docker.yaml) · [GitHub API](https://api.github.com/repos/atuinsh/atuin).

<a id="anhkysuai-devtoys-app-devtoys"></a>

### DevToys

- **Repo:** [DevToys-app/DevToys](https://github.com/DevToys-app/DevToys).
- **Mục đích:** Bộ tiện ích desktop chuyển đổi, định dạng và kiểm tra dữ liệu cho developer.
- **Điểm đáng dùng:** Smart Detection chọn công cụ theo clipboard, có formatter JSON/SQL/XML, JWT, regex, ảnh và cơ chế extension.
- **License:** MIT; phần mềm bên thứ ba có thông báo riêng.
- **Giới hạn:** Clipboard/JWT có thể nhạy cảm; decode JWT không đồng nghĩa xác minh chữ ký, extension cần đánh giá riêng.
- **Tích hợp:** Dùng hỗ trợ thao tác thủ công với dữ liệu mẫu, giữ bước kiểm tra quyết định ở script/CI có thể tái lập.
- **Đối chiếu:** IT-Tools cho tiện ích web tự host; CyberChef cho chuỗi biến đổi; jq cho JSON CLI.
- **Mức kiểm chứng:** `docs-read` — Đọc các phần mô tả và giới hạn trong README, thông báo license, metadata manifest và cấu hình CI khi có; chưa đọc toàn bộ mã triển khai, chưa cài hoặc chạy kiểm thử upstream.
- **Snapshot:** kiểm ngày 2026-11-23; commit `2dbbc8aa594978d11165a0e8112243c96a277dbc` (2026-09-28T17:45:50-07:00); 32,303 sao theo GitHub API ngày 2026-11-23. Sao không đại diện chất lượng.
- **Bằng chứng:** [README.md](https://github.com/DevToys-app/DevToys/blob/2dbbc8aa594978d11165a0e8112243c96a277dbc/README.md) · [LICENSE.md](https://github.com/DevToys-app/DevToys/blob/2dbbc8aa594978d11165a0e8112243c96a277dbc/LICENSE.md) · [.github/workflows/ci.yml](https://github.com/DevToys-app/DevToys/blob/2dbbc8aa594978d11165a0e8112243c96a277dbc/.github/workflows/ci.yml) · [GitHub API](https://api.github.com/repos/DevToys-app/DevToys).

<a id="anhkysuai-reactivex-rxjs"></a>

### RxJS

- **Repo:** [ReactiveX/rxjs](https://github.com/ReactiveX/rxjs).
- **Mục đích:** Kết hợp luồng bất đồng bộ và sự kiện bằng Observable.
- **Điểm đáng dùng:** README HEAD v9 mô tả Observable nền web/fallback, operator qua Symbol, ColdObservable và hủy bằng AbortSignal; CI có migration audit.
- **License:** Apache-2.0.
- **Giới hạn:** v9 chưa có beta npm tại snapshot, next còn trỏ v8 và latest là v7; không trộn API nhánh này với package production.
- **Tích hợp:** Chọn major theo ứng dụng, kiểm thử hủy subscription và hành vi nhiều subscriber rồi mới nâng luồng cũ.
- **Đối chiếu:** AsyncIterable cho luồng chuẩn; XState cho state machine; [MobX](../06-ui-ux-design/README.md#anhkysuai-mobxjs-mobx) cho phản ứng trạng thái.
- **Mức kiểm chứng:** `docs-read` — Đọc các phần mô tả và giới hạn trong README, thông báo license, metadata manifest và cấu hình CI khi có; chưa đọc toàn bộ mã triển khai, chưa cài hoặc chạy kiểm thử upstream.
- **Snapshot:** kiểm ngày 2026-11-23; commit `60d632c3878d7237f2d405d9517091899d553f6d` (2026-11-18T21:50:52-06:00); 31,722 sao theo GitHub API ngày 2026-11-23. Sao không đại diện chất lượng.
- **Bằng chứng:** [README.md](https://github.com/ReactiveX/rxjs/blob/60d632c3878d7237f2d405d9517091899d553f6d/README.md) · [LICENSE.txt](https://github.com/ReactiveX/rxjs/blob/60d632c3878d7237f2d405d9517091899d553f6d/LICENSE.txt) · [package.json](https://github.com/ReactiveX/rxjs/blob/60d632c3878d7237f2d405d9517091899d553f6d/package.json) · [.github/workflows/ci_main.yml](https://github.com/ReactiveX/rxjs/blob/60d632c3878d7237f2d405d9517091899d553f6d/.github/workflows/ci_main.yml) · [GitHub API](https://api.github.com/repos/ReactiveX/rxjs).

<a id="anhkysuai-chinabugotech-hutool"></a>

### Hutool

- **Repo:** [chinabugotech/hutool](https://github.com/chinabugotech/hutool).
- **Mục đích:** Bộ tiện ích Java cho chuỗi, ngày, I/O, mã hóa, JDBC và HTTP.
- **Điểm đáng dùng:** README chia rõ module core, crypto, db, http, cron và extra, thuận tiện chọn phạm vi nhỏ thay vì kéo mọi tiện ích.
- **License:** MulanPSL-2.0.
- **Giới hạn:** Wrapper crypto/HTTP không tự chọn chính sách an toàn; tuân theo LICENSE MulanPSL-2.0 dù lời giới thiệu nói có thể sao chép không ghi chú.
- **Tích hợp:** Chỉ dùng module cần thiết, kiểm tra charset/timezone, timeout và thuật toán đang chọn trước khi đưa vào mẫu backend.
- **Đối chiếu:** Apache Commons cho utility Java; Guava cho collections; Spring utilities cho ứng dụng Spring.
- **Mức kiểm chứng:** `docs-read` — Đọc các phần mô tả và giới hạn trong README, thông báo license, metadata manifest và cấu hình CI khi có; chưa đọc toàn bộ mã triển khai, chưa cài hoặc chạy kiểm thử upstream.
- **Snapshot:** kiểm ngày 2026-11-23; commit `87ec11862baae72914df703e25939eb44a8a843c` (2026-10-09T10:02:32+08:00); 30,219 sao theo GitHub API ngày 2026-11-23. Sao không đại diện chất lượng.
- **Bằng chứng:** [README.md](https://github.com/chinabugotech/hutool/blob/87ec11862baae72914df703e25939eb44a8a843c/README.md) · [LICENSE](https://github.com/chinabugotech/hutool/blob/87ec11862baae72914df703e25939eb44a8a843c/LICENSE) · [pom.xml](https://github.com/chinabugotech/hutool/blob/87ec11862baae72914df703e25939eb44a8a843c/pom.xml) · [GitHub API](https://api.github.com/repos/chinabugotech/hutool).

<a id="anhkysuai-notepad-plus-plus-notepad-plus-plus"></a>

### Notepad++

- **Repo:** [notepad-plus-plus/notepad-plus-plus](https://github.com/notepad-plus-plus/notepad-plus-plus).
- **Mục đích:** Editor mã và văn bản cho Windows hỗ trợ nhiều ngôn ngữ.
- **Điểm đáng dùng:** README cung cấp quy trình build và khóa GPG release; CI_build xây nguồn, hữu ích làm tham chiếu ứng dụng editor Windows.
- **License:** GPL-3.0 theo LICENSE của dự án.
- **Giới hạn:** Phạm vi nền tảng là Windows, không coi plugin là có cùng license/chất lượng; khóa/chữ ký release phải đối chiếu khi tải bản cụ thể.
- **Tích hợp:** Dùng cho thao tác văn bản ở môi trường Windows, giữ danh sách plugin được kiểm và xác minh bản phân phối chính thức.
- **Đối chiếu:** [VS Code](../08-awesome-lists-learning/README.md#6c58-editor-terminal--dòng-lệnh) cho IDE nhẹ; Geany cho editor đa nền; [Micro](../13-dev-stack-devops/README.md#anhkysuai-micro-editor-micro) cho terminal.
- **Mức kiểm chứng:** `docs-read` — Đọc các phần mô tả và giới hạn trong README, thông báo license, metadata manifest và cấu hình CI khi có; chưa đọc toàn bộ mã triển khai, chưa cài hoặc chạy kiểm thử upstream.
- **Snapshot:** kiểm ngày 2026-11-23; commit `6ed1e3cd6a11431cb1d2cb55ab503bff68806610` (2026-11-23T08:08:44+01:00); 29,961 sao theo GitHub API ngày 2026-11-23. Sao không đại diện chất lượng.
- **Bằng chứng:** [README.md](https://github.com/notepad-plus-plus/notepad-plus-plus/blob/6ed1e3cd6a11431cb1d2cb55ab503bff68806610/README.md) · [LICENSE](https://github.com/notepad-plus-plus/notepad-plus-plus/blob/6ed1e3cd6a11431cb1d2cb55ab503bff68806610/LICENSE) · [.github/workflows/CI_build.yml](https://github.com/notepad-plus-plus/notepad-plus-plus/blob/6ed1e3cd6a11431cb1d2cb55ab503bff68806610/.github/workflows/CI_build.yml) · [GitHub API](https://api.github.com/repos/notepad-plus-plus/notepad-plus-plus).

<a id="anhkysuai-micro-editor-micro"></a>

### Micro

- **Repo:** [micro-editor/micro](https://github.com/micro-editor/micro).
- **Mục đích:** Editor terminal dễ dùng, phát hành dưới dạng binary đơn.
- **Điểm đáng dùng:** Keybinding quen thuộc, multi-cursor, split/tab và plugin Lua giúp chỉnh tệp qua SSH; CI có build và test.
- **License:** MIT; dependency theo LICENSE-THIRD-PARTY.
- **Giới hạn:** Clipboard cần điều kiện môi trường riêng; README loại trừ Mingw/Cygwin dù có Windows, plugin Lua cần kiểm soát nguồn.
- **Tích hợp:** Dùng editor tiện ích trên máy dev/SSH, khóa plugin và thử terminal clipboard trước khi đưa vào dev image.
- **Đối chiếu:** [Helix](../13-dev-stack-devops/README.md#anhkysuai-helix-editor-helix) cho modal LSP; [Neovim](../08-awesome-lists-learning/README.md#6c58-editor-terminal--dòng-lệnh) cho cấu hình sâu; nano cho chỉnh tệp cơ bản.
- **Mức kiểm chứng:** `docs-read` — Đọc các phần mô tả và giới hạn trong README, thông báo license, metadata manifest và cấu hình CI khi có; chưa đọc toàn bộ mã triển khai, chưa cài hoặc chạy kiểm thử upstream.
- **Snapshot:** kiểm ngày 2026-11-23; commit `ef8725d69d8806290d8d820ebe1be5ebf8950949` (2026-11-21T20:41:01+01:00); 29,950 sao theo GitHub API ngày 2026-11-23. Sao không đại diện chất lượng.
- **Bằng chứng:** [README.md](https://github.com/micro-editor/micro/blob/ef8725d69d8806290d8d820ebe1be5ebf8950949/README.md) · [LICENSE](https://github.com/micro-editor/micro/blob/ef8725d69d8806290d8d820ebe1be5ebf8950949/LICENSE) · [LICENSE-THIRD-PARTY](https://github.com/micro-editor/micro/blob/ef8725d69d8806290d8d820ebe1be5ebf8950949/LICENSE-THIRD-PARTY) · [go.mod](https://github.com/micro-editor/micro/blob/ef8725d69d8806290d8d820ebe1be5ebf8950949/go.mod) · [.github/workflows/test.yaml](https://github.com/micro-editor/micro/blob/ef8725d69d8806290d8d820ebe1be5ebf8950949/.github/workflows/test.yaml) · [GitHub API](https://api.github.com/repos/micro-editor/micro).

<a id="anhkysuai-wezterm-wezterm"></a>

### WezTerm

- **Repo:** [wezterm/wezterm](https://github.com/wezterm/wezterm).
- **Mục đích:** Terminal và multiplexer đa nền tảng viết Rust, dùng GPU.
- **Điểm đáng dùng:** Repo kết hợp terminal với quản lý phiên và có Nix build; README trỏ tài liệu người dùng riêng cùng kênh hỗ trợ cộng đồng.
- **License:** MIT.
- **Giới hạn:** Dự án được mô tả là duy trì trong thời gian cá nhân; chưa thử render/font/GPU hoặc độ tương thích terminal trên từng OS.
- **Tích hợp:** Thử shell và workflow đa pane của nhóm, lưu cấu hình có version và chọn release phù hợp.
- **Đối chiếu:** [Kitty](../13-dev-stack-devops/README.md#anhkysuai-kovidgoyal-kitty) cho terminal GPU; [Alacritty](../13-dev-stack-devops/README.md#anhkysuai-alacritty-alacritty) cho terminal tối giản; [Zellij](../13-dev-stack-devops/README.md#anhkysuai-zellij-org-zellij) cho quản lý workspace.
- **Mức kiểm chứng:** `docs-read` — Đọc các phần mô tả và giới hạn trong README, thông báo license, metadata manifest và cấu hình CI khi có; chưa đọc toàn bộ mã triển khai, chưa cài hoặc chạy kiểm thử upstream.
- **Snapshot:** kiểm ngày 2026-11-23; commit `ee6f3044d09f83f21a32aead8dac2bc2a32e7fcb` (2026-11-21T00:24:03+01:00); 29,662 sao theo GitHub API ngày 2026-11-23. Sao không đại diện chất lượng.
- **Bằng chứng:** [README.md](https://github.com/wezterm/wezterm/blob/ee6f3044d09f83f21a32aead8dac2bc2a32e7fcb/README.md) · [LICENSE.md](https://github.com/wezterm/wezterm/blob/ee6f3044d09f83f21a32aead8dac2bc2a32e7fcb/LICENSE.md) · [Cargo.toml](https://github.com/wezterm/wezterm/blob/ee6f3044d09f83f21a32aead8dac2bc2a32e7fcb/Cargo.toml) · [.github/workflows/nix-build.yml](https://github.com/wezterm/wezterm/blob/ee6f3044d09f83f21a32aead8dac2bc2a32e7fcb/.github/workflows/nix-build.yml) · [GitHub API](https://api.github.com/repos/wezterm/wezterm).

<a id="anhkysuai-composer-composer"></a>

### Composer

- **Repo:** [composer/composer](https://github.com/composer/composer).
- **Mục đích:** Quản lý dependency dự án PHP.
- **Điểm đáng dùng:** README phân biệt bản hiện hành với 2.2 LTS theo PHP và các binary giải nén/VCS phụ trợ; Packagist là registry liên quan.
- **License:** MIT.
- **Giới hạn:** Khả năng cài package phụ thuộc PHP extension/platform và script/plugin bên thứ ba; quản lý dependency không bảo đảm package an toàn.
- **Tích hợp:** Commit composer.lock cho ứng dụng, khóa toolchain, duyệt plugin/script và thử cài từ lock trong CI.
- **Đối chiếu:** npm cho hệ Node; [Poetry](../13-dev-stack-devops/README.md#anhkysuai-python-poetry-poetry) cho Python; Packagist/Private Packagist cho registry Composer.
- **Mức kiểm chứng:** `docs-read` — Đọc các phần mô tả và giới hạn trong README, thông báo license, metadata manifest và cấu hình CI khi có; chưa đọc toàn bộ mã triển khai, chưa cài hoặc chạy kiểm thử upstream.
- **Snapshot:** kiểm ngày 2026-11-23; commit `8a53515e753d9f60f1ed338cd40e0fae9464af52` (2026-11-19T21:26:52+01:00); 29,589 sao theo GitHub API ngày 2026-11-23. Sao không đại diện chất lượng.
- **Bằng chứng:** [README.md](https://github.com/composer/composer/blob/8a53515e753d9f60f1ed338cd40e0fae9464af52/README.md) · [LICENSE](https://github.com/composer/composer/blob/8a53515e753d9f60f1ed338cd40e0fae9464af52/LICENSE) · [composer.json](https://github.com/composer/composer/blob/8a53515e753d9f60f1ed338cd40e0fae9464af52/composer.json) · [.github/workflows/lint.yml](https://github.com/composer/composer/blob/8a53515e753d9f60f1ed338cd40e0fae9464af52/.github/workflows/lint.yml) · [GitHub API](https://api.github.com/repos/composer/composer).

<a id="anhkysuai-nrwl-nx"></a>

### Nx

- **Repo:** [nrwl/nx](https://github.com/nrwl/nx).
- **Mục đích:** Điều phối monorepo với cache và chạy tác vụ bị ảnh hưởng.
- **Điểm đáng dùng:** Plugin phát hiện task và khai báo input/output cho nhiều stack; lõi Rust và mở rộng TypeScript hỗ trợ workspace đa ngôn ngữ.
- **License:** MIT cho mã repo; dịch vụ CI/cloud theo điều khoản riêng.
- **Giới hạn:** Cache đúng phụ thuộc khai báo input/output/environment; tính năng cloud/self-healing quảng bá không mặc định là local miễn phí hoặc đã kiểm chứng.
- **Tích hợp:** Bắt đầu bằng task build/test có thể tái lập, kiểm tra cache hit sai và quyền secret trước khi bật remote cache.
- **Đối chiếu:** [Turborepo](../08-awesome-lists-learning/README.md#6c514-ngôn-ngữ--runtime) cho JS monorepo; Bazel cho build hermetic; Moon cho task workspace.
- **Mức kiểm chứng:** `docs-read` — Đọc các phần mô tả và giới hạn trong README, thông báo license, metadata manifest và cấu hình CI khi có; chưa đọc toàn bộ mã triển khai, chưa cài hoặc chạy kiểm thử upstream.
- **Snapshot:** kiểm ngày 2026-11-23; commit `341530f8a798dcfa071bb975100f41c214543427` (2026-11-21T22:00:23Z); 29,494 sao theo GitHub API ngày 2026-11-23. Sao không đại diện chất lượng.
- **Bằng chứng:** [README.md](https://github.com/nrwl/nx/blob/341530f8a798dcfa071bb975100f41c214543427/README.md) · [LICENSE](https://github.com/nrwl/nx/blob/341530f8a798dcfa071bb975100f41c214543427/LICENSE) · [package.json](https://github.com/nrwl/nx/blob/341530f8a798dcfa071bb975100f41c214543427/package.json) · [Cargo.toml](https://github.com/nrwl/nx/blob/341530f8a798dcfa071bb975100f41c214543427/Cargo.toml) · [.github/workflows/ci.yml](https://github.com/nrwl/nx/blob/341530f8a798dcfa071bb975100f41c214543427/.github/workflows/ci.yml) · [GitHub API](https://api.github.com/repos/nrwl/nx).

<a id="anhkysuai-niri-wm-niri"></a>

### Niri

**Đã chuyển (2026-11-23):** hồ sơ này nay nằm ở [mục 35](../35-desktop-productivity-apps/README.md#anhkysuai-niri-wm-niri); catalog con xem [catalog/](../catalog/README.md).

<a id="anhkysuai-reflex-dev-reflex"></a>

### Reflex

- **Repo:** [reflex-dev/reflex](https://github.com/reflex-dev/reflex).
- **Mục đích:** Xây ứng dụng web full-stack bằng API Python.
- **Điểm đáng dùng:** README minh họa UI, state class và event handler trong cùng ngôn ngữ; workflow docs_tests chạy ứng dụng tài liệu với pytest.
- **License:** Apache-2.0.
- **Giới hạn:** Viết Python không loại bỏ yêu cầu hiểu browser/server và network state; AI Builder/hosting là dịch vụ riêng, cần đánh giá latency tác vụ.
- **Tích hợp:** Dùng cho mẫu dashboard nội bộ Python, kiểm tra auth, session và tác vụ dài trước khi chọn cho UI công khai.
- **Đối chiếu:** Streamlit cho ứng dụng dữ liệu; NiceGUI cho UI Python; [Dash](../08-awesome-lists-learning/README.md#6c527-đồ-họa-3d--sơ-đồ) cho dashboard.
- **Mức kiểm chứng:** `docs-read` — Đọc các phần mô tả và giới hạn trong README, thông báo license, metadata manifest và cấu hình CI khi có; chưa đọc toàn bộ mã triển khai, chưa cài hoặc chạy kiểm thử upstream.
- **Snapshot:** kiểm ngày 2026-11-23; commit `df7f1571ec6a2e7f814e472199ad2dd03b973c2c` (2026-11-21T00:09:37+05:00); 29,047 sao theo GitHub API ngày 2026-11-23. Sao không đại diện chất lượng.
- **Bằng chứng:** [README.md](https://github.com/reflex-dev/reflex/blob/df7f1571ec6a2e7f814e472199ad2dd03b973c2c/README.md) · [LICENSE](https://github.com/reflex-dev/reflex/blob/df7f1571ec6a2e7f814e472199ad2dd03b973c2c/LICENSE) · [pyproject.toml](https://github.com/reflex-dev/reflex/blob/df7f1571ec6a2e7f814e472199ad2dd03b973c2c/pyproject.toml) · [.github/workflows/docs_tests.yml](https://github.com/reflex-dev/reflex/blob/df7f1571ec6a2e7f814e472199ad2dd03b973c2c/.github/workflows/docs_tests.yml) · [GitHub API](https://api.github.com/repos/reflex-dev/reflex).

<a id="anhkysuai-postcss-postcss"></a>

### PostCSS

- **Repo:** [postcss/postcss](https://github.com/postcss/postcss).
- **Mục đích:** Phân tích và biến đổi CSS qua JavaScript plugin.
- **Điểm đáng dùng:** AST cho plugin đọc/sửa rule; Autoprefixer, Stylelint và preset-env thể hiện các pipeline mở rộng độc lập.
- **License:** MIT.
- **Giới hạn:** Core không tự cung cấp mọi phép biến đổi; thứ tự plugin, target browser và version quyết định kết quả cuối.
- **Tích hợp:** Khóa chuỗi plugin theo template, giữ sourcemap và so CSS/render đầu ra trên browser mục tiêu.
- **Đối chiếu:** Lightning CSS cho transformer tích hợp; Sass cho preprocessing; [Tailwind CSS](../13-dev-stack-devops/README.md) cho utility generation.
- **Mức kiểm chứng:** `docs-read` — Đọc các phần mô tả và giới hạn trong README, thông báo license, metadata manifest và cấu hình CI khi có; chưa đọc toàn bộ mã triển khai, chưa cài hoặc chạy kiểm thử upstream.
- **Snapshot:** kiểm ngày 2026-11-23; commit `8b7a14a76542016ac462a0205e89b58d171c89b6` (2026-11-20T20:11:41Z); 28,980 sao theo GitHub API ngày 2026-11-23. Sao không đại diện chất lượng.
- **Bằng chứng:** [README.md](https://github.com/postcss/postcss/blob/8b7a14a76542016ac462a0205e89b58d171c89b6/README.md) · [LICENSE](https://github.com/postcss/postcss/blob/8b7a14a76542016ac462a0205e89b58d171c89b6/LICENSE) · [package.json](https://github.com/postcss/postcss/blob/8b7a14a76542016ac462a0205e89b58d171c89b6/package.json) · [.github/workflows/test.yml](https://github.com/postcss/postcss/blob/8b7a14a76542016ac462a0205e89b58d171c89b6/.github/workflows/test.yml) · [GitHub API](https://api.github.com/repos/postcss/postcss).

<a id="anhkysuai-nvchad-nvchad"></a>

### NvChad

- **Repo:** [NvChad/NvChad](https://github.com/NvChad/NvChad).
- **Mục đích:** Cấu hình Neovim Lua tập trung UI và nạp plugin theo nhu cầu.
- **Điểm đáng dùng:** README yêu cầu dùng starter config và import repo như plugin qua lazy; chia UI, theme, LSP, file tree và completion thành module.
- **License:** GPL-3.0; plugin có license riêng.
- **Giới hạn:** Thời gian khởi động là đo tác giả trên cấu hình riêng; plugin và language server phải tương thích, không thay nguyên thư mục cấu hình hiện có.
- **Tích hợp:** Thử profile Neovim riêng, khóa plugin và lưu chỉnh sửa người dùng tách khỏi module upstream.
- **Đối chiếu:** [LazyVim](../13-dev-stack-devops/README.md#anhkysuai-lazyvim-lazyvim) cho cấu hình Neovim; AstroNvim cho distribution; [Helix](../13-dev-stack-devops/README.md#anhkysuai-helix-editor-helix) cho editor tích hợp.
- **Mức kiểm chứng:** `docs-read` — Đọc các phần mô tả và giới hạn trong README, thông báo license, metadata manifest và cấu hình CI khi có; chưa đọc toàn bộ mã triển khai, chưa cài hoặc chạy kiểm thử upstream.
- **Snapshot:** kiểm ngày 2026-11-23; commit `87d6a41ec07ab995de912a892749b6b4805ad2b3` (2026-10-25T03:31:02+05:30); 28,557 sao theo GitHub API ngày 2026-11-23. Sao không đại diện chất lượng.
- **Bằng chứng:** [README.md](https://github.com/NvChad/NvChad/blob/87d6a41ec07ab995de912a892749b6b4805ad2b3/README.md) · [LICENSE](https://github.com/NvChad/NvChad/blob/87d6a41ec07ab995de912a892749b6b4805ad2b3/LICENSE) · [GitHub API](https://api.github.com/repos/NvChad/NvChad).

<a id="anhkysuai-google-python-fire"></a>

### Python Fire

- **Repo:** [google/python-fire](https://github.com/google/python-fire).
- **Mục đích:** Sinh CLI trực tiếp từ function, class, module hoặc object Python.
- **Điểm đáng dùng:** Fire ánh xạ cấu trúc đối tượng thành lệnh, có chế độ REPL phục vụ khám phá và debug; package đọc là 0.7.1.
- **License:** Apache-2.0.
- **Giới hạn:** Expose một module có thể đưa nhiều thao tác nội bộ ra CLI ngoài dự tính; README ghi không phải sản phẩm Google chính thức.
- **Tích hợp:** Dùng cho script nội bộ nhỏ với object công khai giới hạn, kiểm thử parse tham số và lỗi trước khi trao cho người dùng.
- **Đối chiếu:** Typer cho CLI có type hint; Click cho điều khiển giao diện rõ; argparse cho thư viện chuẩn.
- **Mức kiểm chứng:** `docs-read` — Đọc các phần mô tả và giới hạn trong README, thông báo license, metadata manifest và cấu hình CI khi có; chưa đọc toàn bộ mã triển khai, chưa cài hoặc chạy kiểm thử upstream.
- **Snapshot:** kiểm ngày 2026-11-23; commit `716bbc23d7eca949fdb682172283c8d18f742cb6` (2025-08-16T17:26:04-04:00); 28,229 sao theo GitHub API ngày 2026-11-23. Sao không đại diện chất lượng.
- **Bằng chứng:** [README.md](https://github.com/google/python-fire/blob/716bbc23d7eca949fdb682172283c8d18f742cb6/README.md) · [LICENSE](https://github.com/google/python-fire/blob/716bbc23d7eca949fdb682172283c8d18f742cb6/LICENSE) · [pyproject.toml](https://github.com/google/python-fire/blob/716bbc23d7eca949fdb682172283c8d18f742cb6/pyproject.toml) · [.github/workflows/build.yml](https://github.com/google/python-fire/blob/716bbc23d7eca949fdb682172283c8d18f742cb6/.github/workflows/build.yml) · [GitHub API](https://api.github.com/repos/google/python-fire).

<a id="anhkysuai-caolan-async"></a>

### Async

- **Repo:** [caolan/async](https://github.com/caolan/async).
- **Mục đích:** Tiện ích điều phối tác vụ JavaScript bất đồng bộ.
- **Điểm đáng dùng:** Manifest mô tả higher-order functions và pattern async; README phân biệt bản async có ESM/MJS với package async-es thuần ESM.
- **License:** MIT.
- **Giới hạn:** Cần chọn API phù hợp code callback hay Promise và kiểm tra giới hạn concurrency; thư viện không tự xử lý idempotency hoặc hủy tác vụ ngoài.
- **Tích hợp:** Dùng khi bảo trì pipeline callback hoặc chuỗi tác vụ cần điều phối, kiểm tra lỗi giữa chừng và tải giới hạn.
- **Đối chiếu:** Promise/async-await cho chuẩn ngôn ngữ; p-limit cho concurrency; [RxJS](../13-dev-stack-devops/README.md#anhkysuai-reactivex-rxjs) cho luồng sự kiện.
- **Mức kiểm chứng:** `docs-read` — Đọc các phần mô tả và giới hạn trong README, thông báo license, metadata manifest và cấu hình CI khi có; chưa đọc toàn bộ mã triển khai, chưa cài hoặc chạy kiểm thử upstream.
- **Snapshot:** kiểm ngày 2026-11-23; commit `3921e54bd0704157dbea238fdfcc0c3619abde1a` (2026-09-28T13:13:30-07:00); 28,120 sao theo GitHub API ngày 2026-11-23. Sao không đại diện chất lượng.
- **Bằng chứng:** [README.md](https://github.com/caolan/async/blob/3921e54bd0704157dbea238fdfcc0c3619abde1a/README.md) · [LICENSE](https://github.com/caolan/async/blob/3921e54bd0704157dbea238fdfcc0c3619abde1a/LICENSE) · [package.json](https://github.com/caolan/async/blob/3921e54bd0704157dbea238fdfcc0c3619abde1a/package.json) · [.github/workflows/ci.yml](https://github.com/caolan/async/blob/3921e54bd0704157dbea238fdfcc0c3619abde1a/.github/workflows/ci.yml) · [GitHub API](https://api.github.com/repos/caolan/async).

<a id="anhkysuai-lazyvim-lazyvim"></a>

### LazyVim

- **Repo:** [LazyVim/LazyVim](https://github.com/LazyVim/LazyVim).
- **Mục đích:** Cấu hình Neovim dựa trên lazy.nvim với plugin và keymap có sẵn.
- **Điểm đáng dùng:** Tách cấu hình mặc định nạp trước cấu hình riêng; README xác định Neovim >=0.11.2, LuaJIT, Git partial clone và compiler C.
- **License:** Apache-2.0; plugin có license riêng.
- **Giới hạn:** Không thay cấu hình đang dùng mà chưa sao lưu; plugin/language server tăng dependency và yêu cầu toolchain ngoài Neovim.
- **Tích hợp:** Dùng starter trong profile riêng, khóa plugin và giữ lua/plugins tùy biến tách khỏi mặc định upstream.
- **Đối chiếu:** [NvChad](../13-dev-stack-devops/README.md#anhkysuai-nvchad-nvchad) cho UI Neovim; AstroNvim cho distribution; [Helix](../13-dev-stack-devops/README.md#anhkysuai-helix-editor-helix) cho editor cấu hình gọn.
- **Mức kiểm chứng:** `docs-read` — Đọc các phần mô tả và giới hạn trong README, thông báo license, metadata manifest và cấu hình CI khi có; chưa đọc toàn bộ mã triển khai, chưa cài hoặc chạy kiểm thử upstream.
- **Snapshot:** kiểm ngày 2026-11-23; commit `5c26fac21fd3896024a23f2dbc62b722f9a731db` (2026-11-08T20:21:29Z); 27,910 sao theo GitHub API ngày 2026-11-23. Sao không đại diện chất lượng.
- **Bằng chứng:** [README.md](https://github.com/LazyVim/LazyVim/blob/5c26fac21fd3896024a23f2dbc62b722f9a731db/README.md) · [LICENSE](https://github.com/LazyVim/LazyVim/blob/5c26fac21fd3896024a23f2dbc62b722f9a731db/LICENSE) · [.github/workflows/ci.yml](https://github.com/LazyVim/LazyVim/blob/5c26fac21fd3896024a23f2dbc62b722f9a731db/.github/workflows/ci.yml) · [GitHub API](https://api.github.com/repos/LazyVim/LazyVim).

<a id="anhkysuai-emscripten-core-emscripten"></a>

### Emscripten

- **Repo:** [emscripten-core/emscripten](https://github.com/emscripten-core/emscripten).
- **Mục đích:** Biên dịch C/C++ sang WebAssembly và JavaScript glue.
- **Điểm đáng dùng:** LLVM/Binaryen cùng lớp hỗ trợ API như OpenGL/SDL giúp chuyển chương trình native ra web; emcc tạo module và loader.
- **License:** MIT OR NCSA; LLVM/Binaryen và thư viện kèm có license riêng.
- **Giới hạn:** Port native vẫn phải giải quyết filesystem, thread, memory và API browser; không suy tính tương thích từ lời giới thiệu có thể port codebase.
- **Tích hợp:** Khóa emsdk/toolchain, thu nhỏ biên JS/Wasm và kiểm thử tải/cấp phát trên browser mục tiêu.
- **Đối chiếu:** WASI SDK cho runtime WASI; wasm-bindgen cho Rust; WebAssembly thủ công cho module nhỏ.
- **Mức kiểm chứng:** `docs-read` — Đọc các phần mô tả và giới hạn trong README, thông báo license, metadata manifest và cấu hình CI khi có; chưa đọc toàn bộ mã triển khai, chưa cài hoặc chạy kiểm thử upstream.
- **Snapshot:** kiểm ngày 2026-11-23; commit `49421518749bf4fb2cca87eadee5eb1b15198d95` (2026-11-22T22:04:42+02:00); 27,792 sao theo GitHub API ngày 2026-11-23. Sao không đại diện chất lượng.
- **Bằng chứng:** [README.md](https://github.com/emscripten-core/emscripten/blob/49421518749bf4fb2cca87eadee5eb1b15198d95/README.md) · [LICENSE](https://github.com/emscripten-core/emscripten/blob/49421518749bf4fb2cca87eadee5eb1b15198d95/LICENSE) · [package.json](https://github.com/emscripten-core/emscripten/blob/49421518749bf4fb2cca87eadee5eb1b15198d95/package.json) · [pyproject.toml](https://github.com/emscripten-core/emscripten/blob/49421518749bf4fb2cca87eadee5eb1b15198d95/pyproject.toml) · [.github/workflows/ci.yml](https://github.com/emscripten-core/emscripten/blob/49421518749bf4fb2cca87eadee5eb1b15198d95/.github/workflows/ci.yml) · [GitHub API](https://api.github.com/repos/emscripten-core/emscripten).

<a id="anhkysuai-microsoft-vcpkg"></a>

### vcpkg

- **Repo:** [microsoft/vcpkg](https://github.com/microsoft/vcpkg).
- **Mục đích:** Quản lý package C/C++ tích hợp CMake, MSBuild và nhiều hệ build.
- **Điểm đáng dùng:** Manifest, version control dependency, binary reuse và asset caching phục vụ build có thể tái lập/offline.
- **License:** MIT cho repo; mỗi port giữ license upstream.
- **Giới hạn:** Port tải và chạy build upstream, có license riêng dưới installed/share; cache offline phải chuẩn bị trước, telemetry có cơ chế opt-out.
- **Tích hợp:** Khóa baseline/triplet, dùng registry và cache có kiểm soát, xuất license của thư viện thực sự được link.
- **Đối chiếu:** Conan cho package C++; CMake FetchContent cho dependency nguồn; Meson subprojects cho build Meson.
- **Mức kiểm chứng:** `docs-read` — Đọc các phần mô tả và giới hạn trong README, thông báo license, metadata manifest và cấu hình CI khi có; chưa đọc toàn bộ mã triển khai, chưa cài hoặc chạy kiểm thử upstream.
- **Snapshot:** kiểm ngày 2026-11-23; commit `277978ad2eddc3b05ecf288dcd33071968cd2f79` (2026-11-22T21:00:08-08:00); 27,632 sao theo GitHub API ngày 2026-11-23. Sao không đại diện chất lượng.
- **Bằng chứng:** [README.md](https://github.com/microsoft/vcpkg/blob/277978ad2eddc3b05ecf288dcd33071968cd2f79/README.md) · [LICENSE.txt](https://github.com/microsoft/vcpkg/blob/277978ad2eddc3b05ecf288dcd33071968cd2f79/LICENSE.txt) · [.github/workflows/check_issues.yml](https://github.com/microsoft/vcpkg/blob/277978ad2eddc3b05ecf288dcd33071968cd2f79/.github/workflows/check_issues.yml) · [GitHub API](https://api.github.com/repos/microsoft/vcpkg).

<a id="anhkysuai-tree-sitter-tree-sitter"></a>

### Tree-sitter

- **Repo:** [tree-sitter/tree-sitter](https://github.com/tree-sitter/tree-sitter).
- **Mục đích:** Sinh parser và cập nhật cây cú pháp tăng dần khi mã thay đổi.
- **Điểm đáng dùng:** Concrete syntax tree và khả năng chịu lỗi cú pháp phù hợp editor; runtime C nhúng được, có binding Rust/Wasm.
- **License:** MIT.
- **Giới hạn:** Cây cú pháp không cung cấp phân giải symbol/type đầy đủ; grammar từng ngôn ngữ có chất lượng, version và license riêng.
- **Tích hợp:** Dùng để chia cấu trúc repo hoặc highlight, khóa grammar ABI và test file dở dang trước khi đưa vào công cụ đọc code.
- **Đối chiếu:** LSP cho ngữ nghĩa editor; ANTLR cho parser generator; ast-grep cho truy vấn AST.
- **Mức kiểm chứng:** `docs-read` — Đọc các phần mô tả và giới hạn trong README, thông báo license, metadata manifest và cấu hình CI khi có; chưa đọc toàn bộ mã triển khai, chưa cài hoặc chạy kiểm thử upstream.
- **Snapshot:** kiểm ngày 2026-11-23; commit `65e36c51acd7cce17f884f41380f275777e3fc19` (2026-11-23T01:20:44-05:00); 27,551 sao theo GitHub API ngày 2026-11-23. Sao không đại diện chất lượng.
- **Bằng chứng:** [README.md](https://github.com/tree-sitter/tree-sitter/blob/65e36c51acd7cce17f884f41380f275777e3fc19/README.md) · [LICENSE](https://github.com/tree-sitter/tree-sitter/blob/65e36c51acd7cce17f884f41380f275777e3fc19/LICENSE) · [Cargo.toml](https://github.com/tree-sitter/tree-sitter/blob/65e36c51acd7cce17f884f41380f275777e3fc19/Cargo.toml) · [CMakeLists.txt](https://github.com/tree-sitter/tree-sitter/blob/65e36c51acd7cce17f884f41380f275777e3fc19/CMakeLists.txt) · [.github/workflows/ci.yml](https://github.com/tree-sitter/tree-sitter/blob/65e36c51acd7cce17f884f41380f275777e3fc19/.github/workflows/ci.yml) · [GitHub API](https://api.github.com/repos/tree-sitter/tree-sitter).

<a id="anhkysuai-schniz-fnm"></a>

### fnm

- **Repo:** [Schniz/fnm](https://github.com/Schniz/fnm).
- **Mục đích:** Quản lý phiên bản Node.js đa nền tảng bằng binary Rust.
- **Điểm đáng dùng:** Đọc .node-version và .nvmrc, hỗ trợ shell setup/completion; CI có fmt, clippy và cargo test.
- **License:** GPL-3.0.
- **Giới hạn:** Cài tool chưa đủ nếu shell chưa nạp môi trường; installer có thể chỉnh cấu hình shell nên phải giữ thay đổi rõ ràng.
- **Tích hợp:** Ghi phiên bản Node trong template, thử trên shell đội đang dùng và giữ CI dùng cùng runtime.
- **Đối chiếu:** [nvm](../08-awesome-lists-learning/README.md#6c514-ngôn-ngữ--runtime) cho shell Unix; Volta cho toolchain JS; [mise](../13-dev-stack-devops/README.md#factory-2026-11-04-mise) cho nhiều runtime.
- **Mức kiểm chứng:** `docs-read` — Đọc các phần mô tả và giới hạn trong README, thông báo license, metadata manifest và cấu hình CI khi có; chưa đọc toàn bộ mã triển khai, chưa cài hoặc chạy kiểm thử upstream.
- **Snapshot:** kiểm ngày 2026-11-23; commit `07f13237ae208f531f8ea88d4cfde3160c22f99a` (2026-10-26T12:25:36-04:00); 27,487 sao theo GitHub API ngày 2026-11-23. Sao không đại diện chất lượng.
- **Bằng chứng:** [README.md](https://github.com/Schniz/fnm/blob/07f13237ae208f531f8ea88d4cfde3160c22f99a/README.md) · [LICENSE](https://github.com/Schniz/fnm/blob/07f13237ae208f531f8ea88d4cfde3160c22f99a/LICENSE) · [package.json](https://github.com/Schniz/fnm/blob/07f13237ae208f531f8ea88d4cfde3160c22f99a/package.json) · [Cargo.toml](https://github.com/Schniz/fnm/blob/07f13237ae208f531f8ea88d4cfde3160c22f99a/Cargo.toml) · [.github/workflows/rust.yml](https://github.com/Schniz/fnm/blob/07f13237ae208f531f8ea88d4cfde3160c22f99a/.github/workflows/rust.yml) · [GitHub API](https://api.github.com/repos/Schniz/fnm).

<a id="anhkysuai-devolutions-unigetui"></a>

### UniGetUI

**Đã chuyển (2026-11-23):** hồ sơ này nay nằm ở [mục 35](../35-desktop-productivity-apps/README.md#anhkysuai-devolutions-unigetui); catalog con xem [catalog/](../catalog/README.md).

<a id="anhkysuai-angular-angular-cli"></a>

### Angular CLI

- **Repo:** [angular/angular-cli](https://github.com/angular/angular-cli).
- **Mục đích:** CLI tạo workspace, scaffold, build và nâng cấp ứng dụng Angular.
- **Điểm đáng dùng:** Monorepo có build system, schematics và SSR; CI sinh JSON Schema types và dùng Bazel/pnpm.
- **License:** MIT.
- **Giới hạn:** HEAD 22.4.0-next.0 là nhánh phát triển; cần khớp Angular, Node, TypeScript thay vì cài CLI mới nhất bất kể dự án.
- **Tích hợp:** Dùng schematic chuẩn cho mẫu Angular, khóa version và kiểm tra migration trên nhánh riêng có build/test.
- **Đối chiếu:** [Nx](../13-dev-stack-devops/README.md#anhkysuai-nrwl-nx) cho workspace Angular lớn; [Vite](../13-dev-stack-devops/README.md) cho stack web khác; Angular DevKit cho generator tùy biến.
- **Mức kiểm chứng:** `docs-read` — Đọc các phần mô tả và giới hạn trong README, thông báo license, metadata manifest và cấu hình CI khi có; chưa đọc toàn bộ mã triển khai, chưa cài hoặc chạy kiểm thử upstream.
- **Snapshot:** kiểm ngày 2026-11-23; commit `090bc9980210eeea4e0e941f276f78f097fb90bb` (2026-11-20T14:45:11+01:00); 27,024 sao theo GitHub API ngày 2026-11-23. Sao không đại diện chất lượng.
- **Bằng chứng:** [README.md](https://github.com/angular/angular-cli/blob/090bc9980210eeea4e0e941f276f78f097fb90bb/README.md) · [LICENSE](https://github.com/angular/angular-cli/blob/090bc9980210eeea4e0e941f276f78f097fb90bb/LICENSE) · [package.json](https://github.com/angular/angular-cli/blob/090bc9980210eeea4e0e941f276f78f097fb90bb/package.json) · [.github/workflows/ci.yml](https://github.com/angular/angular-cli/blob/090bc9980210eeea4e0e941f276f78f097fb90bb/.github/workflows/ci.yml) · [GitHub API](https://api.github.com/repos/angular/angular-cli).

<a id="anhkysuai-cmderdev-cmder"></a>

### Cmder

- **Repo:** [cmderdev/cmder](https://github.com/cmderdev/cmder).
- **Mục đích:** Gói terminal Windows portable gồm launcher, Clink, theme và công cụ dòng lệnh.
- **Điểm đáng dùng:** README phân biệt bản Windows Terminal/ConEmu và cấu hình portable hay chia sẻ; bin được thêm PATH còn opt do người dùng quyết định.
- **License:** MIT cho Cmder; công cụ đi kèm giữ license riêng.
- **Giới hạn:** Gói tổng hợp không có chung một license; PATH tự chèn có thể ưu tiên binary khác, dữ liệu portable cần bảo vệ khi đồng bộ.
- **Tích hợp:** Dùng dev kit Windows có inventory phiên bản, tách cấu hình cá nhân và thử thứ tự PATH trước phân phối.
- **Đối chiếu:** Windows Terminal cho terminal gốc; [PowerShell](../13-dev-stack-devops/README.md#anhkysuai-powershell-powershell) cho shell; [WezTerm](../13-dev-stack-devops/README.md#anhkysuai-wezterm-wezterm) cho đa nền.
- **Mức kiểm chứng:** `docs-read` — Đọc các phần mô tả và giới hạn trong README, thông báo license, metadata manifest và cấu hình CI khi có; chưa đọc toàn bộ mã triển khai, chưa cài hoặc chạy kiểm thử upstream.
- **Snapshot:** kiểm ngày 2026-11-23; commit `5655c5eb90a075b8bcdd8617bd331bd3dd96c5c2` (2026-11-10T06:19:04+03:30); 27,012 sao theo GitHub API ngày 2026-11-23. Sao không đại diện chất lượng.
- **Bằng chứng:** [README.md](https://github.com/cmderdev/cmder/blob/5655c5eb90a075b8bcdd8617bd331bd3dd96c5c2/README.md) · [LICENSE](https://github.com/cmderdev/cmder/blob/5655c5eb90a075b8bcdd8617bd331bd3dd96c5c2/LICENSE) · [.github/workflows/build.yml](https://github.com/cmderdev/cmder/blob/5655c5eb90a075b8bcdd8617bd331bd3dd96c5c2/.github/workflows/build.yml) · [GitHub API](https://api.github.com/repos/cmderdev/cmder).

<a id="anhkysuai-openapitools-openapi-generator"></a>

### OpenAPI Generator

- **Repo:** [OpenAPITools/openapi-generator](https://github.com/OpenAPITools/openapi-generator).
- **Mục đích:** Sinh SDK, server stub và tài liệu từ đặc tả OpenAPI.
- **Điểm đáng dùng:** Nhiều generator/template cho ngôn ngữ và framework, CI kiểm tra consistency các tệp template/test giúp quản lý đầu ra hàng loạt.
- **License:** Apache-2.0; đối chiếu template, đầu vào và license mã sinh.
- **Giới hạn:** Spec/template/options không tin cậy có thể gây code injection theo cảnh báo README; hỗ trợ OpenAPI khác nhau từng generator, mã sinh vẫn phải kiểm thử.
- **Tích hợp:** Khóa generator và template, duyệt spec, chạy sinh trong workspace riêng rồi kiểm tra diff, compile và contract API.
- **Đối chiếu:** Swagger Codegen cho dòng generator khác; Kiota cho client đa ngôn ngữ; openapi-typescript cho kiểu TypeScript.
- **Mức kiểm chứng:** `docs-read` — Đọc các phần mô tả và giới hạn trong README, thông báo license, metadata manifest và cấu hình CI khi có; chưa đọc toàn bộ mã triển khai, chưa cài hoặc chạy kiểm thử upstream.
- **Snapshot:** kiểm ngày 2026-11-23; commit `f885a67d59ecbd2b7df5d00861d8dfba2f81567f` (2026-11-23T13:11:25+08:00); 26,867 sao theo GitHub API ngày 2026-11-23. Sao không đại diện chất lượng.
- **Bằng chứng:** [README.md](https://github.com/OpenAPITools/openapi-generator/blob/f885a67d59ecbd2b7df5d00861d8dfba2f81567f/README.md) · [LICENSE](https://github.com/OpenAPITools/openapi-generator/blob/f885a67d59ecbd2b7df5d00861d8dfba2f81567f/LICENSE) · [pom.xml](https://github.com/OpenAPITools/openapi-generator/blob/f885a67d59ecbd2b7df5d00861d8dfba2f81567f/pom.xml) · [.github/workflows/misc-test.yaml](https://github.com/OpenAPITools/openapi-generator/blob/f885a67d59ecbd2b7df5d00861d8dfba2f81567f/.github/workflows/misc-test.yaml) · [GitHub API](https://api.github.com/repos/OpenAPITools/openapi-generator).

<a id="anhkysuai-discordjs-discord-js"></a>

### discord.js

- **Repo:** [discordjs/discord.js](https://github.com/discordjs/discord.js).
- **Mục đích:** Bộ package Node.js tương tác Discord REST, Gateway và voice.
- **Điểm đáng dùng:** README phân tách wrapper chính, core, builders, rest, ws và scaffold bot để chọn lớp tích hợp cần thiết.
- **License:** Apache-2.0 tại SHA đã đọc.
- **Giới hạn:** Release riêng từng package, không suy version từ monorepo 0.0.0; bot cần bảo vệ token, intent/permission và rate limit, voice có dependency riêng.
- **Tích hợp:** Tạo bot test với quyền tối thiểu, tách secret và xử lý reconnect/idempotency trước khi nối workflow thật.
- **Đối chiếu:** discord.py cho Python; Eris cho Node; Discord REST API trực tiếp cho phạm vi nhỏ.
- **Mức kiểm chứng:** `docs-read` — Đọc các phần mô tả và giới hạn trong README, thông báo license, metadata manifest và cấu hình CI khi có; chưa đọc toàn bộ mã triển khai, chưa cài hoặc chạy kiểm thử upstream.
- **Snapshot:** kiểm ngày 2026-11-23; commit `33799ee19ae13a06a71e2f83fd426f845eaf9bb0` (2026-11-22T21:48:24Z); 26,840 sao theo GitHub API ngày 2026-11-23. Sao không đại diện chất lượng.
- **Bằng chứng:** [README.md](https://github.com/discordjs/discord.js/blob/33799ee19ae13a06a71e2f83fd426f845eaf9bb0/README.md) · [LICENSE](https://github.com/discordjs/discord.js/blob/33799ee19ae13a06a71e2f83fd426f845eaf9bb0/LICENSE) · [package.json](https://github.com/discordjs/discord.js/blob/33799ee19ae13a06a71e2f83fd426f845eaf9bb0/package.json) · [.github/workflows/tests.yml](https://github.com/discordjs/discord.js/blob/33799ee19ae13a06a71e2f83fd426f845eaf9bb0/.github/workflows/tests.yml) · [GitHub API](https://api.github.com/repos/discordjs/discord.js).

<a id="anhkysuai-microsoft-winget-cli"></a>

### WinGet

- **Repo:** [microsoft/winget-cli](https://github.com/microsoft/winget-cli).
- **Mục đích:** Client Windows Package Manager cài và quản lý phần mềm.
- **Điểm đáng dùng:** README phân biệt nguồn Microsoft Store và community repository, group policy có thể thay cấu hình; client nằm trong App Installer.
- **License:** MIT cho client; package theo điều khoản riêng.
- **Giới hạn:** Yêu cầu phiên bản Windows cụ thể, Server Core không hỗ trợ theo README; package nguồn ngoài không được bảo đảm bởi MIT của client.
- **Tích hợp:** Ghi rõ package ID/source/version trong dev setup, kiểm tra policy và publisher trước khi chạy cài hàng loạt.
- **Đối chiếu:** Scoop cho cài theo user; Chocolatey cho package Windows; [UniGetUI](../13-dev-stack-devops/README.md#anhkysuai-devolutions-unigetui) cho giao diện manager.
- **Mức kiểm chứng:** `docs-read` — Đọc các phần mô tả và giới hạn trong README, thông báo license, metadata manifest và cấu hình CI khi có; chưa đọc toàn bộ mã triển khai, chưa cài hoặc chạy kiểm thử upstream.
- **Snapshot:** kiểm ngày 2026-11-23; commit `d9acda871de78385492753450218694d54cd1078` (2026-11-19T11:19:43-08:00); 26,636 sao theo GitHub API ngày 2026-11-23. Sao không đại diện chất lượng.
- **Bằng chứng:** [README.md](https://github.com/microsoft/winget-cli/blob/d9acda871de78385492753450218694d54cd1078/README.md) · [LICENSE](https://github.com/microsoft/winget-cli/blob/d9acda871de78385492753450218694d54cd1078/LICENSE) · [.github/workflows/duplicate-surfacing.lock.yml](https://github.com/microsoft/winget-cli/blob/d9acda871de78385492753450218694d54cd1078/.github/workflows/duplicate-surfacing.lock.yml) · [GitHub API](https://api.github.com/repos/microsoft/winget-cli).

<a id="anhkysuai-swordfish90-cool-retro-term"></a>

### Cool Retro Term

- **Repo:** [Swordfish90/cool-retro-term](https://github.com/Swordfish90/cool-retro-term).
- **Mục đích:** Terminal mô phỏng màn hình CRT bằng Qt/QML trên Linux và macOS.
- **Điểm đáng dùng:** README nêu QML port qtermwidget và Qt6; đã đối chiếu main.qml có thông báo GPL-3.0-or-later và tạo/đóng nhiều cửa sổ.
- **License:** GPL-3.0-or-later cho giao diện ứng dụng; thư viện/font theo license riêng.
- **Giới hạn:** Không lấy WTFPL của một font làm license toàn repo; hiệu ứng CRT có thể giảm độ đọc và tăng tải GPU, submodule/font cần kiểm kê riêng.
- **Tích hợp:** Dùng làm tùy chọn trình diễn cá nhân, thử contrast/font/hiệu ứng và giữ terminal thông thường cho công việc dài.
- **Đối chiếu:** [Kitty](../13-dev-stack-devops/README.md#anhkysuai-kovidgoyal-kitty) cho GPU terminal; [WezTerm](../13-dev-stack-devops/README.md#anhkysuai-wezterm-wezterm) cho terminal/multiplexer; [Alacritty](../13-dev-stack-devops/README.md#anhkysuai-alacritty-alacritty) cho giao diện đơn giản.
- **Mức kiểm chứng:** `docs-read` — Đọc các phần mô tả và giới hạn trong README, thông báo license, metadata manifest và cấu hình CI khi có; chưa đọc toàn bộ mã triển khai, chưa cài hoặc chạy kiểm thử upstream.
- **Snapshot:** kiểm ngày 2026-11-23; commit `1394ce82fa53d2a87d5adc4d99f9eeba598ea53d` (2026-05-31T12:04:28+02:00); 26,590 sao theo GitHub API ngày 2026-11-23. Sao không đại diện chất lượng.
- **Bằng chứng:** [README.md](https://github.com/Swordfish90/cool-retro-term/blob/1394ce82fa53d2a87d5adc4d99f9eeba598ea53d/README.md) · [app/qml/fonts/gohu/LICENSE](https://github.com/Swordfish90/cool-retro-term/blob/1394ce82fa53d2a87d5adc4d99f9eeba598ea53d/app/qml/fonts/gohu/LICENSE) · [.github/workflows/release.yml](https://github.com/Swordfish90/cool-retro-term/blob/1394ce82fa53d2a87d5adc4d99f9eeba598ea53d/.github/workflows/release.yml) · [app/main.cpp](https://github.com/Swordfish90/cool-retro-term/blob/1394ce82fa53d2a87d5adc4d99f9eeba598ea53d/app/main.cpp) · [app/qml/main.qml](https://github.com/Swordfish90/cool-retro-term/blob/1394ce82fa53d2a87d5adc4d99f9eeba598ea53d/app/qml/main.qml) · [gpl-2.0.txt](https://github.com/Swordfish90/cool-retro-term/blob/1394ce82fa53d2a87d5adc4d99f9eeba598ea53d/gpl-2.0.txt) · [gpl-3.0.txt](https://github.com/Swordfish90/cool-retro-term/blob/1394ce82fa53d2a87d5adc4d99f9eeba598ea53d/gpl-3.0.txt) · [GitHub API](https://api.github.com/repos/Swordfish90/cool-retro-term).

<a id="anhkysuai-bendlang-bend"></a>

### Bend

**Đã chuyển (2026-11-23):** hồ sơ này nay nằm ở [mục 37](../37-programming-languages-runtimes/README.md#anhkysuai-bendlang-bend); catalog con xem [catalog/](../catalog/README.md).

<a id="anhkysuai-modernizr-modernizr"></a>

### Modernizr

- **Repo:** [Modernizr/Modernizr](https://github.com/Modernizr/Modernizr).
- **Mục đích:** Phát hiện khả năng HTML/CSS của browser để progressive enhancement.
- **Điểm đáng dùng:** Kết quả thành thuộc tính Modernizr hoặc class trên html, build tùy chọn chỉ chứa feature detect cần dùng.
- **License:** MIT.
- **Giới hạn:** HEAD 4.0.0-alpha; README cảnh báo website lỗi/cũ và khuyên build từ npm. Feature detect không chứng minh hành vi mọi edge case.
- **Tích hợp:** Chỉ thêm detect có nhánh fallback thực tế, kiểm thử trường hợp thiếu tính năng và tránh nạp toàn bộ bộ kiểm tra.
- **Đối chiếu:** CSS @supports cho CSS; API feature checks trực tiếp; Browserslist cho target build.
- **Mức kiểm chứng:** `docs-read` — Đọc các phần mô tả và giới hạn trong README, thông báo license, metadata manifest và cấu hình CI khi có; chưa đọc toàn bộ mã triển khai, chưa cài hoặc chạy kiểm thử upstream.
- **Snapshot:** kiểm ngày 2026-11-23; commit `612ec65ccdba311e8b1153b1076d18f0251943f6` (2026-09-03T17:05:36+02:00); 25,679 sao theo GitHub API ngày 2026-11-23. Sao không đại diện chất lượng.
- **Bằng chứng:** [README.md](https://github.com/Modernizr/Modernizr/blob/612ec65ccdba311e8b1153b1076d18f0251943f6/README.md) · [LICENSE](https://github.com/Modernizr/Modernizr/blob/612ec65ccdba311e8b1153b1076d18f0251943f6/LICENSE) · [package.json](https://github.com/Modernizr/Modernizr/blob/612ec65ccdba311e8b1153b1076d18f0251943f6/package.json) · [.github/workflows/testing.yml](https://github.com/Modernizr/Modernizr/blob/612ec65ccdba311e8b1153b1076d18f0251943f6/.github/workflows/testing.yml) · [GitHub API](https://api.github.com/repos/Modernizr/Modernizr).

<a id="anhkysuai-asdf-vm-asdf"></a>

### asdf

- **Repo:** [asdf-vm/asdf](https://github.com/asdf-vm/asdf).
- **Mục đích:** Quản lý nhiều runtime theo dự án bằng plugin và .tool-versions.
- **Điểm đáng dùng:** CLI thống nhất chọn version theo thư mục, hỗ trợ file version cũ và shell completion; CI Go có race/coverage.
- **License:** MIT.
- **Giới hạn:** Plugin tải/cài runtime là mã ngoài cần kiểm soát; file version không khóa mọi thư viện hệ thống hoặc dependency ứng dụng.
- **Tích hợp:** Ghi .tool-versions và nguồn plugin vào dev setup, thử cài sạch rồi đồng bộ runtime CI.
- **Đối chiếu:** [mise](../13-dev-stack-devops/README.md#factory-2026-11-04-mise) cho runtime/task; [fnm](../13-dev-stack-devops/README.md#anhkysuai-schniz-fnm) cho Node; [pyenv](../13-dev-stack-devops/README.md#anhkysuai-pyenv-pyenv) cho Python.
- **Mức kiểm chứng:** `docs-read` — Đọc các phần mô tả và giới hạn trong README, thông báo license, metadata manifest và cấu hình CI khi có; chưa đọc toàn bộ mã triển khai, chưa cài hoặc chạy kiểm thử upstream.
- **Snapshot:** kiểm ngày 2026-11-23; commit `b41b2d222a93e6607c86fa990c7a49f98d8b1b29` (2026-11-10T20:02:18-05:00); 25,628 sao theo GitHub API ngày 2026-11-23. Sao không đại diện chất lượng.
- **Bằng chứng:** [README.md](https://github.com/asdf-vm/asdf/blob/b41b2d222a93e6607c86fa990c7a49f98d8b1b29/README.md) · [LICENSE](https://github.com/asdf-vm/asdf/blob/b41b2d222a93e6607c86fa990c7a49f98d8b1b29/LICENSE) · [go.mod](https://github.com/asdf-vm/asdf/blob/b41b2d222a93e6607c86fa990c7a49f98d8b1b29/go.mod) · [.github/workflows/tests.yml](https://github.com/asdf-vm/asdf/blob/b41b2d222a93e6607c86fa990c7a49f98d8b1b29/.github/workflows/tests.yml) · [GitHub API](https://api.github.com/repos/asdf-vm/asdf).

<a id="anhkysuai-zloirock-core-js"></a>

### core-js

- **Repo:** [zloirock/core-js](https://github.com/zloirock/core-js).
- **Mục đích:** Polyfill JavaScript tiêu chuẩn và một số đề xuất/API web.
- **Điểm đáng dùng:** Chọn module theo tính năng hoặc bản không làm đổi global namespace; README có hướng tích hợp Babel/SWC, CI unit bằng Karma.
- **License:** MIT.
- **Giới hạn:** Polyfill proposal có thể đổi, global patch ảnh hưởng thư viện khác; không nhầm @babel/polyfill cũ dựa trên core-js 2 với dòng hiện tại.
- **Tích hợp:** Xác định browser target, chỉ nạp tính năng cần thiết và kiểm tra bundle/polyfill trùng lặp.
- **Đối chiếu:** Babel preset-env cho chọn transform; native browser APIs khi target cho phép; es-shims cho shim riêng lẻ.
- **Mức kiểm chứng:** `docs-read` — Đọc các phần mô tả và giới hạn trong README, thông báo license, metadata manifest và cấu hình CI khi có; chưa đọc toàn bộ mã triển khai, chưa cài hoặc chạy kiểm thử upstream.
- **Snapshot:** kiểm ngày 2026-11-23; commit `9ae671c77f29648e8c4d12e48169a78d534c2ea4` (2026-11-23T11:59:40+02:00); 25,515 sao theo GitHub API ngày 2026-11-23. Sao không đại diện chất lượng.
- **Bằng chứng:** [README.md](https://github.com/zloirock/core-js/blob/9ae671c77f29648e8c4d12e48169a78d534c2ea4/README.md) · [LICENSE](https://github.com/zloirock/core-js/blob/9ae671c77f29648e8c4d12e48169a78d534c2ea4/LICENSE) · [package.json](https://github.com/zloirock/core-js/blob/9ae671c77f29648e8c4d12e48169a78d534c2ea4/package.json) · [.github/workflows/ci.yml](https://github.com/zloirock/core-js/blob/9ae671c77f29648e8c4d12e48169a78d534c2ea4/.github/workflows/ci.yml) · [GitHub API](https://api.github.com/repos/zloirock/core-js).

<a id="anhkysuai-gpakosz-tmux"></a>

### Oh my tmux

- **Repo:** [gpakosz/.tmux](https://github.com/gpakosz/.tmux).
- **Mục đích:** Cấu hình tmux có sẵn cho keybinding, status và clipboard.
- **Điểm đáng dùng:** Header .tmux.conf xác nhận dual license; cấu hình lựa chọn clipboard theo hệ và tách override vào .tmux.conf.local.
- **License:** MIT OR WTFPL-2.0.
- **Giới hạn:** Đây là cấu hình, cần tmux và awk/perl/grep/sed; keybinding/PATH/TERM có thể xung đột môi trường sẵn có.
- **Tích hợp:** Thử session riêng, giữ bản sao cấu hình cũ và chỉ ghi tùy biến vào file local để cập nhật upstream dễ hơn.
- **Đối chiếu:** tmux cấu hình tay cho kiểm soát đầy đủ; [Zellij](../13-dev-stack-devops/README.md#anhkysuai-zellij-org-zellij) cho workspace sẵn; [WezTerm](../13-dev-stack-devops/README.md#anhkysuai-wezterm-wezterm) cho multiplexer tích hợp.
- **Mức kiểm chứng:** `docs-read` — Đọc các phần mô tả và giới hạn trong README, thông báo license, metadata manifest và cấu hình CI khi có; chưa đọc toàn bộ mã triển khai, chưa cài hoặc chạy kiểm thử upstream.
- **Snapshot:** kiểm ngày 2026-11-23; commit `58a3dcc0d718ec0fa1c0d5a2fddd640a1ad7a5b7` (2026-08-08T17:37:17+02:00); 25,478 sao theo GitHub API ngày 2026-11-23. Sao không đại diện chất lượng.
- **Bằng chứng:** [README.md](https://github.com/gpakosz/.tmux/blob/58a3dcc0d718ec0fa1c0d5a2fddd640a1ad7a5b7/README.md) · [LICENSE.MIT](https://github.com/gpakosz/.tmux/blob/58a3dcc0d718ec0fa1c0d5a2fddd640a1ad7a5b7/LICENSE.MIT) · [LICENSE.WTFPLv2](https://github.com/gpakosz/.tmux/blob/58a3dcc0d718ec0fa1c0d5a2fddd640a1ad7a5b7/LICENSE.WTFPLv2) · [.tmux.conf](https://github.com/gpakosz/.tmux/blob/58a3dcc0d718ec0fa1c0d5a2fddd640a1ad7a5b7/.tmux.conf) · [GitHub API](https://api.github.com/repos/gpakosz/.tmux).

<a id="anhkysuai-fastfetch-cli-fastfetch"></a>

### Fastfetch

- **Repo:** [fastfetch-cli/fastfetch](https://github.com/fastfetch-cli/fastfetch).
- **Mục đích:** Thu thập và trình bày thông tin hệ thống trong terminal.
- **Điểm đáng dùng:** Cấu hình hiển thị theo module, nhiều OS và CI nhiều kiến trúc hỗ trợ ghi ngữ cảnh máy khi debug.
- **License:** MIT.
- **Giới hạn:** README chỉ bảo đảm thử tích cực x86-64/aarch64; đầu ra có thể lộ hostname/phần cứng và không phải benchmark hiệu năng.
- **Tích hợp:** Dùng báo cáo môi trường kèm lỗi, chọn trường cần chia sẻ và che định danh máy trước gửi ra ngoài.
- **Đối chiếu:** inxi cho thông tin hệ thống; neofetch cho hiển thị cũ; osquery cho inventory có truy vấn.
- **Mức kiểm chứng:** `docs-read` — Đọc các phần mô tả và giới hạn trong README, thông báo license, metadata manifest và cấu hình CI khi có; chưa đọc toàn bộ mã triển khai, chưa cài hoặc chạy kiểm thử upstream.
- **Snapshot:** kiểm ngày 2026-11-23; commit `7b3603707fe4b42e7deca52a729c64d13c479ea5` (2026-11-23T09:31:12+08:00); 25,434 sao theo GitHub API ngày 2026-11-23. Sao không đại diện chất lượng.
- **Bằng chứng:** [README.md](https://github.com/fastfetch-cli/fastfetch/blob/7b3603707fe4b42e7deca52a729c64d13c479ea5/README.md) · [LICENSE](https://github.com/fastfetch-cli/fastfetch/blob/7b3603707fe4b42e7deca52a729c64d13c479ea5/LICENSE) · [CMakeLists.txt](https://github.com/fastfetch-cli/fastfetch/blob/7b3603707fe4b42e7deca52a729c64d13c479ea5/CMakeLists.txt) · [.github/workflows/ci.yml](https://github.com/fastfetch-cli/fastfetch/blob/7b3603707fe4b42e7deca52a729c64d13c479ea5/.github/workflows/ci.yml) · [GitHub API](https://api.github.com/repos/fastfetch-cli/fastfetch).

<a id="anhkysuai-v8-v8"></a>

### V8

**Đã chuyển (2026-11-23):** hồ sơ này nay nằm ở [mục 37](../37-programming-languages-runtimes/README.md#anhkysuai-v8-v8); catalog con xem [catalog/](../catalog/README.md).

<a id="anhkysuai-pypa-pipenv"></a>

### Pipenv

- **Repo:** [pypa/pipenv](https://github.com/pypa/pipenv).
- **Mục đích:** Kết hợp quản lý virtualenv và dependency Python cho ứng dụng.
- **Điểm đáng dùng:** Pipfile mô tả nhu cầu, Pipfile.lock ghi tổ hợp và hash để cài xác định; hỗ trợ Python từ system/pyenv/asdf.
- **License:** MIT.
- **Giới hạn:** Cần Python >=3.11 để chạy phiên bản đọc; hash xác minh artifact không đánh giá an toàn package, .env phải giữ ngoài repo.
- **Tích hợp:** Dùng lockfile trong CI, kiểm tra platform marker và giữ interpreter cùng bản đã test.
- **Đối chiếu:** [uv](../13-dev-stack-devops/README.md) cho workflow Python; [Poetry](../13-dev-stack-devops/README.md#anhkysuai-python-poetry-poetry) cho quản lý dự án; venv/pip-tools cho tổ hợp tối giản.
- **Mức kiểm chứng:** `docs-read` — Đọc các phần mô tả và giới hạn trong README, thông báo license, metadata manifest và cấu hình CI khi có; chưa đọc toàn bộ mã triển khai, chưa cài hoặc chạy kiểm thử upstream.
- **Snapshot:** kiểm ngày 2026-11-23; commit `00ae9dc59e00f1132d74d79d8985ae47c70dd881` (2026-11-17T20:50:16-05:00); 25,021 sao theo GitHub API ngày 2026-11-23. Sao không đại diện chất lượng.
- **Bằng chứng:** [README.md](https://github.com/pypa/pipenv/blob/00ae9dc59e00f1132d74d79d8985ae47c70dd881/README.md) · [LICENSE](https://github.com/pypa/pipenv/blob/00ae9dc59e00f1132d74d79d8985ae47c70dd881/LICENSE) · [pyproject.toml](https://github.com/pypa/pipenv/blob/00ae9dc59e00f1132d74d79d8985ae47c70dd881/pyproject.toml) · [.github/workflows/ci.yaml](https://github.com/pypa/pipenv/blob/00ae9dc59e00f1132d74d79d8985ae47c70dd881/.github/workflows/ci.yaml) · [GitHub API](https://api.github.com/repos/pypa/pipenv).

<a id="anhkysuai-go-delve-delve"></a>

### Delve

- **Repo:** [go-delve/delve](https://github.com/go-delve/delve).
- **Mục đích:** Debugger chuyên dụng cho chương trình Go.
- **Điểm đáng dùng:** Repo có CLI client, API và tài liệu viết client/GUI; go.mod tại SHA yêu cầu Go 1.25, workflow đọc chạy thử trên FreeBSD.
- **License:** MIT.
- **Giới hạn:** Debugger cần quyền truy cập tiến trình, có thể làm lộ memory và dừng thực thi; tương thích Go/OS/CPU phải kiểm tra theo bản dùng.
- **Tích hợp:** Gắn vào dev profile với build debug, giới hạn cổng/đối tượng attach và tránh đưa endpoint debug ra môi trường công khai.
- **Đối chiếu:** GDB cho native chung; VS Code Go cho UI Delve; pprof cho profiling Go.
- **Mức kiểm chứng:** `docs-read` — Đọc các phần mô tả và giới hạn trong README, thông báo license, metadata manifest và cấu hình CI khi có; chưa đọc toàn bộ mã triển khai, chưa cài hoặc chạy kiểm thử upstream.
- **Snapshot:** kiểm ngày 2026-11-23; commit `29f07287b9373351ca9bbb6391bdd8a85968f20f` (2026-11-21T21:58:06+01:00); 24,988 sao theo GitHub API ngày 2026-11-23. Sao không đại diện chất lượng.
- **Bằng chứng:** [README.md](https://github.com/go-delve/delve/blob/29f07287b9373351ca9bbb6391bdd8a85968f20f/README.md) · [LICENSE](https://github.com/go-delve/delve/blob/29f07287b9373351ca9bbb6391bdd8a85968f20f/LICENSE) · [go.mod](https://github.com/go-delve/delve/blob/29f07287b9373351ca9bbb6391bdd8a85968f20f/go.mod) · [.github/workflows/test-freebsd.yml](https://github.com/go-delve/delve/blob/29f07287b9373351ca9bbb6391bdd8a85968f20f/.github/workflows/test-freebsd.yml) · [GitHub API](https://api.github.com/repos/go-delve/delve).

<a id="anhkysuai-uber-go-zap"></a>

### Zap

- **Repo:** [uber-go/zap](https://github.com/uber-go/zap).
- **Mục đích:** Structured logging theo level cho Go.
- **Điểm đáng dùng:** Logger dùng field có kiểu, SugaredLogger cung cấp API linh hoạt hơn; README mô tả encoder hạn chế reflection/allocation và CI make cover.
- **License:** MIT.
- **Giới hạn:** Benchmark upstream không bảo đảm nhanh hơn mọi workload; log vẫn có chi phí I/O và nguy cơ chứa secret, hỗ trợ Go theo hai minor gần nhất.
- **Tích hợp:** Chuẩn hóa field/trace ID, che dữ liệu nhạy cảm, chọn sampling và flush khi shutdown trước benchmark tải thật.
- **Đối chiếu:** slog trong Go chuẩn; zerolog cho structured log; Logrus cho API quen thuộc.
- **Mức kiểm chứng:** `docs-read` — Đọc các phần mô tả và giới hạn trong README, thông báo license, metadata manifest và cấu hình CI khi có; chưa đọc toàn bộ mã triển khai, chưa cài hoặc chạy kiểm thử upstream.
- **Snapshot:** kiểm ngày 2026-11-23; commit `4892335e05f14bce8a98a69a577fcf3844a42623` (2026-09-16T12:17:34-07:00); 24,695 sao theo GitHub API ngày 2026-11-23. Sao không đại diện chất lượng.
- **Bằng chứng:** [README.md](https://github.com/uber-go/zap/blob/4892335e05f14bce8a98a69a577fcf3844a42623/README.md) · [LICENSE](https://github.com/uber-go/zap/blob/4892335e05f14bce8a98a69a577fcf3844a42623/LICENSE) · [go.mod](https://github.com/uber-go/zap/blob/4892335e05f14bce8a98a69a577fcf3844a42623/go.mod) · [.github/workflows/go.yml](https://github.com/uber-go/zap/blob/4892335e05f14bce8a98a69a577fcf3844a42623/.github/workflows/go.yml) · [GitHub API](https://api.github.com/repos/uber-go/zap).

<a id="anhkysuai-reactivex-rxswift"></a>

### RxSwift

- **Repo:** [ReactiveX/RxSwift](https://github.com/ReactiveX/RxSwift).
- **Mục đích:** Reactive Extensions cho Swift, kết hợp sự kiện UI, KVO và tác vụ async.
- **Điểm đáng dùng:** Observable/operator chung và lớp RxCocoa cho Cocoa tách khỏi core; workflow ma trận Xcode chạy script test.
- **License:** MIT.
- **Giới hạn:** Subscription và scheduler phải quản lý đúng vòng đời để tránh retain cycle/cập nhật UI sai thread; không tự chuyển toàn app thành concurrent an toàn.
- **Tích hợp:** Dùng trong codebase Rx hiện hữu, kiểm thử hủy/dispose và luồng lỗi bằng scheduler kiểm soát.
- **Đối chiếu:** Combine cho nền Apple; AsyncSequence cho Swift concurrency; ReactiveSwift cho FRP Swift.
- **Mức kiểm chứng:** `docs-read` — Đọc các phần mô tả và giới hạn trong README, thông báo license, metadata manifest và cấu hình CI khi có; chưa đọc toàn bộ mã triển khai, chưa cài hoặc chạy kiểm thử upstream.
- **Snapshot:** kiểm ngày 2026-11-23; commit `3e33f90c1bcd3cdea25bdb49bd4a594a50c3ab84` (2026-09-04T21:37:02+03:00); 24,626 sao theo GitHub API ngày 2026-11-23. Sao không đại diện chất lượng.
- **Bằng chứng:** [README.md](https://github.com/ReactiveX/RxSwift/blob/3e33f90c1bcd3cdea25bdb49bd4a594a50c3ab84/README.md) · [LICENSE.md](https://github.com/ReactiveX/RxSwift/blob/3e33f90c1bcd3cdea25bdb49bd4a594a50c3ab84/LICENSE.md) · [.github/workflows/tests.yml](https://github.com/ReactiveX/RxSwift/blob/3e33f90c1bcd3cdea25bdb49bd4a594a50c3ab84/.github/workflows/tests.yml) · [GitHub API](https://api.github.com/repos/ReactiveX/RxSwift).

<a id="anhkysuai-react-navigation-react-navigation"></a>

### React Navigation

- **Repo:** [react-navigation/react-navigation](https://github.com/react-navigation/react-navigation).
- **Mục đích:** Routing và navigation cho ứng dụng React Native.
- **Điểm đáng dùng:** Các package core, stack/native-stack, tab và drawer cho phép chọn cơ chế điều hướng phù hợp; CI kiểm tra version dependency.
- **License:** MIT theo khai báo root và LICENSE package core; đối chiếu các package khác khi phân phối.
- **Giới hạn:** HEAD là major 8 sắp phát hành, README ghi 7.x stable; monorepo không cài đúng từng package chỉ bằng URL repo.
- **Tích hợp:** Khóa major cùng native dependency, kiểm thử deep link, back gesture và lưu/khôi phục navigation state.
- **Đối chiếu:** Expo Router cho routing theo file; React Native Navigation cho native navigation; native navigator của nền tảng.
- **Mức kiểm chứng:** `docs-read` — Đọc các phần mô tả và giới hạn trong README, thông báo license, metadata manifest và cấu hình CI khi có; chưa đọc toàn bộ mã triển khai, chưa cài hoặc chạy kiểm thử upstream.
- **Snapshot:** kiểm ngày 2026-11-23; commit `ca036e815f01f5ea9cf7db2c6955d9afa8a10b20` (2026-11-21T15:20:14+01:00); 24,528 sao theo GitHub API ngày 2026-11-23. Sao không đại diện chất lượng.
- **Bằng chứng:** [README.md](https://github.com/react-navigation/react-navigation/blob/ca036e815f01f5ea9cf7db2c6955d9afa8a10b20/README.md) · [packages/core/LICENSE](https://github.com/react-navigation/react-navigation/blob/ca036e815f01f5ea9cf7db2c6955d9afa8a10b20/packages/core/LICENSE) · [package.json](https://github.com/react-navigation/react-navigation/blob/ca036e815f01f5ea9cf7db2c6955d9afa8a10b20/package.json) · [.github/workflows/ci.yml](https://github.com/react-navigation/react-navigation/blob/ca036e815f01f5ea9cf7db2c6955d9afa8a10b20/.github/workflows/ci.yml) · [GitHub API](https://api.github.com/repos/react-navigation/react-navigation).

<a id="anhkysuai-uutils-coreutils"></a>

### uutils coreutils

- **Repo:** [uutils/coreutils](https://github.com/uutils/coreutils).
- **Mục đích:** Triển khai lại bộ GNU coreutils bằng Rust cho nhiều nền tảng.
- **Điểm đáng dùng:** Mục tiêu khớp stdout/exit code GNU cùng cấu hình nhiều utility; có stable tag cho packager và binary main cho báo lỗi.
- **License:** MIT.
- **Giới hạn:** README thừa nhận một số option thiếu/hành vi khác; không thay coreutils của hệ thống chỉ dựa vào mục tiêu drop-in.
- **Tích hợp:** Thử bằng đường dẫn riêng trong CI, chạy script đại diện so kết quả/locale trước khi chọn làm nền dev image.
- **Đối chiếu:** GNU coreutils cho hành vi tham chiếu; BusyBox cho binary gọn; Toybox cho tiện ích hệ thống.
- **Mức kiểm chứng:** `docs-read` — Đọc các phần mô tả và giới hạn trong README, thông báo license, metadata manifest và cấu hình CI khi có; chưa đọc toàn bộ mã triển khai, chưa cài hoặc chạy kiểm thử upstream.
- **Snapshot:** kiểm ngày 2026-11-23; commit `8b16a3dca86ae91df73db3d375205eb7718c4c03` (2026-11-22T23:38:53+01:00); 24,433 sao theo GitHub API ngày 2026-11-23. Sao không đại diện chất lượng.
- **Bằng chứng:** [README.md](https://github.com/uutils/coreutils/blob/8b16a3dca86ae91df73db3d375205eb7718c4c03/README.md) · [LICENSE](https://github.com/uutils/coreutils/blob/8b16a3dca86ae91df73db3d375205eb7718c4c03/LICENSE) · [Cargo.toml](https://github.com/uutils/coreutils/blob/8b16a3dca86ae91df73db3d375205eb7718c4c03/Cargo.toml) · [.github/workflows/CICD.yml](https://github.com/uutils/coreutils/blob/8b16a3dca86ae91df73db3d375205eb7718c4c03/.github/workflows/CICD.yml) · [GitHub API](https://api.github.com/repos/uutils/coreutils).

<a id="anhkysuai-onevcat-kingfisher"></a>

### Kingfisher

- **Repo:** [onevcat/Kingfisher](https://github.com/onevcat/Kingfisher).
- **Mục đích:** Tải, xử lý và cache ảnh từ mạng trong ứng dụng Swift.
- **Điểm đáng dùng:** Cache memory/disk có expiry/limit, cancel/prefetch và processor/downsample hỗ trợ danh sách ảnh; có extension UIKit/AppKit và SwiftUI.
- **License:** MIT.
- **Giới hạn:** README dừng phát hành CocoaPods sau 8.16.0, hướng sang SPM/framework; cache cần tách theo quyền và ảnh lớn cần giới hạn giải mã.
- **Tích hợp:** Khóa package qua SPM, đặt cache policy theo phiên và test reuse cell, hủy tải, low-data cùng memory pressure.
- **Đối chiếu:** Nuke cho image pipeline Swift; SDWebImage cho hệ Objective-C/Swift; AsyncImage cho SwiftUI đơn giản.
- **Mức kiểm chứng:** `docs-read` — Đọc các phần mô tả và giới hạn trong README, thông báo license, metadata manifest và cấu hình CI khi có; chưa đọc toàn bộ mã triển khai, chưa cài hoặc chạy kiểm thử upstream.
- **Snapshot:** kiểm ngày 2026-11-23; commit `4203444ccbf482c885e0b601fa50b9a609660ef4` (2026-11-21T14:25:36+09:00); 24,412 sao theo GitHub API ngày 2026-11-23. Sao không đại diện chất lượng.
- **Bằng chứng:** [README.md](https://github.com/onevcat/Kingfisher/blob/4203444ccbf482c885e0b601fa50b9a609660ef4/README.md) · [LICENSE](https://github.com/onevcat/Kingfisher/blob/4203444ccbf482c885e0b601fa50b9a609660ef4/LICENSE) · [.github/workflows/test.yaml](https://github.com/onevcat/Kingfisher/blob/4203444ccbf482c885e0b601fa50b9a609660ef4/.github/workflows/test.yaml) · [GitHub API](https://api.github.com/repos/onevcat/Kingfisher).

<a id="anhkysuai-delgan-loguru"></a>

### Loguru

- **Repo:** [Delgan/loguru](https://github.com/Delgan/loguru).
- **Mục đích:** Logging Python với logger sẵn và API cấu hình sink gọn.
- **Điểm đáng dùng:** add/remove sink, rotation/retention/compression, structured record và lazy evaluation giúp giảm mã cấu hình.
- **License:** MIT.
- **Giới hạn:** Traceback chi tiết có thể lộ dữ liệu; async/multiprocess cần cấu hình queue và shutdown phù hợp, claim 10x chưa được đo.
- **Tích hợp:** Thiết lập redaction, retention và sink production rõ, tắt chẩn đoán giá trị nhạy cảm và test kết thúc tiến trình.
- **Đối chiếu:** logging chuẩn Python cho kiểm soát dependency; structlog cho log cấu trúc; Rich logging cho console.
- **Mức kiểm chứng:** `docs-read` — Đọc các phần mô tả và giới hạn trong README, thông báo license, metadata manifest và cấu hình CI khi có; chưa đọc toàn bộ mã triển khai, chưa cài hoặc chạy kiểm thử upstream.
- **Snapshot:** kiểm ngày 2026-11-23; commit `e6fb4104f0dbdfe19fc40d307ec1a97fd6c8ab6e` (2026-11-23T08:20:12+01:00); 24,166 sao theo GitHub API ngày 2026-11-23. Sao không đại diện chất lượng.
- **Bằng chứng:** [README.md](https://github.com/Delgan/loguru/blob/e6fb4104f0dbdfe19fc40d307ec1a97fd6c8ab6e/README.md) · [LICENSE](https://github.com/Delgan/loguru/blob/e6fb4104f0dbdfe19fc40d307ec1a97fd6c8ab6e/LICENSE) · [pyproject.toml](https://github.com/Delgan/loguru/blob/e6fb4104f0dbdfe19fc40d307ec1a97fd6c8ab6e/pyproject.toml) · [.github/workflows/tests.yml](https://github.com/Delgan/loguru/blob/e6fb4104f0dbdfe19fc40d307ec1a97fd6c8ab6e/.github/workflows/tests.yml) · [GitHub API](https://api.github.com/repos/Delgan/loguru).

<a id="anhkysuai-air-verse-air"></a>

### Air

- **Repo:** [air-verse/air](https://github.com/air-verse/air).
- **Mục đích:** Theo dõi file rồi build/restart ứng dụng Go khi phát triển.
- **Điểm đáng dùng:** TOML cấu hình watch/build, entrypoint dạng mảng và proxy reload browser; README tách rõ với hot deploy production.
- **License:** GPL-3.0.
- **Giới hạn:** build.bin cũ deprecated, snapshot go.mod cần Go 1.26 cao hơn hướng dẫn 1.25; rebuild có thể lặp tác vụ khởi động gây ghi dữ liệu.
- **Tích hợp:** Dùng dev profile, loại trừ thư mục output, kiểm soát env và viết startup idempotent trong môi trường thử.
- **Đối chiếu:** watchexec cho chạy lệnh theo file; nodemon cho watch tổng quát; CompileDaemon cho Go.
- **Mức kiểm chứng:** `docs-read` — Đọc các phần mô tả và giới hạn trong README, thông báo license, metadata manifest và cấu hình CI khi có; chưa đọc toàn bộ mã triển khai, chưa cài hoặc chạy kiểm thử upstream.
- **Snapshot:** kiểm ngày 2026-11-23; commit `71ea1dee05248122ed22b5870c7fb20a90d80ddd` (2026-08-27T10:41:09+08:00); 24,150 sao theo GitHub API ngày 2026-11-23. Sao không đại diện chất lượng.
- **Bằng chứng:** [README.md](https://github.com/air-verse/air/blob/71ea1dee05248122ed22b5870c7fb20a90d80ddd/README.md) · [LICENSE](https://github.com/air-verse/air/blob/71ea1dee05248122ed22b5870c7fb20a90d80ddd/LICENSE) · [go.mod](https://github.com/air-verse/air/blob/71ea1dee05248122ed22b5870c7fb20a90d80ddd/go.mod) · [.github/workflows/build.yml](https://github.com/air-verse/air/blob/71ea1dee05248122ed22b5870c7fb20a90d80ddd/.github/workflows/build.yml) · [GitHub API](https://api.github.com/repos/air-verse/air).

<a id="anhkysuai-yorukot-superfile"></a>

### Superfile

- **Repo:** [yorukot/superfile](https://github.com/yorukot/superfile).
- **Mục đích:** Trình quản lý tệp trong terminal với theme, hotkey và plugin.
- **Điểm đáng dùng:** README phân tách hướng dẫn nền tảng, bộ phím cho Vim và tùy chọn tắt kiểm tra bản cập nhật.
- **License:** MIT.
- **Giới hạn:** Windows chưa được hỗ trợ đầy đủ; uninstall script xóa cả config/data, workflow thu thập chỉ build website nên không chứng minh hành vi thao tác tệp.
- **Tích hợp:** Thử trên thư mục mẫu, làm quen phím sao chép/xóa và sao lưu cấu hình trước khi gắn vào quy trình hằng ngày.
- **Đối chiếu:** [Yazi](../08-awesome-lists-learning/README.md#6c58-editor-terminal--dòng-lệnh) cho terminal file manager; lf cho TUI gọn; ranger cho Python file manager.
- **Mức kiểm chứng:** `docs-read` — Đọc các phần mô tả và giới hạn trong README, thông báo license, metadata manifest và cấu hình CI khi có; chưa đọc toàn bộ mã triển khai, chưa cài hoặc chạy kiểm thử upstream.
- **Snapshot:** kiểm ngày 2026-11-23; commit `c44f7f3c123214b89918d5a78e7df9d3bdcb00fe` (2026-11-21T03:17:04+08:00); 24,118 sao theo GitHub API ngày 2026-11-23. Sao không đại diện chất lượng.
- **Bằng chứng:** [README.md](https://github.com/yorukot/superfile/blob/c44f7f3c123214b89918d5a78e7df9d3bdcb00fe/README.md) · [LICENSE](https://github.com/yorukot/superfile/blob/c44f7f3c123214b89918d5a78e7df9d3bdcb00fe/LICENSE) · [go.mod](https://github.com/yorukot/superfile/blob/c44f7f3c123214b89918d5a78e7df9d3bdcb00fe/go.mod) · [.github/workflows/website-ci.yml](https://github.com/yorukot/superfile/blob/c44f7f3c123214b89918d5a78e7df9d3bdcb00fe/.github/workflows/website-ci.yml) · [GitHub API](https://api.github.com/repos/yorukot/superfile).

<a id="anhkysuai-ramda-ramda"></a>

### Ramda

- **Repo:** [ramda/ramda](https://github.com/ramda/ramda).
- **Mục đích:** Thư viện lập trình hàm JavaScript với currying và pipeline.
- **Điểm đáng dùng:** Đối số dữ liệu thường ở cuối và tự curry giúp ghép các phép biến đổi nhỏ; vẫn dùng object/array JavaScript thông thường.
- **License:** MIT cho code; logo CC-BY-NC-SA-3.0.
- **Giới hạn:** Thư viện hỗ trợ nhưng không cưỡng chế purity/immutability; phong cách point-free quá mức làm code khó đọc, logo không theo MIT.
- **Tích hợp:** Chọn một số phép biến đổi rõ ràng, giữ type/test cho pipeline nghiệp vụ và kiểm tra bundle khi import.
- **Đối chiếu:** Lodash/fp cho utility hàm; Remeda cho TypeScript; Array methods chuẩn cho thao tác đơn giản.
- **Mức kiểm chứng:** `docs-read` — Đọc các phần mô tả và giới hạn trong README, thông báo license, metadata manifest và cấu hình CI khi có; chưa đọc toàn bộ mã triển khai, chưa cài hoặc chạy kiểm thử upstream.
- **Snapshot:** kiểm ngày 2026-11-23; commit `f4b2e35ff433e18c751326b82acc3c6ab3585e18` (2026-10-11T17:34:56-07:00); 24,054 sao theo GitHub API ngày 2026-11-23. Sao không đại diện chất lượng.
- **Bằng chứng:** [README.md](https://github.com/ramda/ramda/blob/f4b2e35ff433e18c751326b82acc3c6ab3585e18/README.md) · [LICENSE.txt](https://github.com/ramda/ramda/blob/f4b2e35ff433e18c751326b82acc3c6ab3585e18/LICENSE.txt) · [package.json](https://github.com/ramda/ramda/blob/f4b2e35ff433e18c751326b82acc3c6ab3585e18/package.json) · [.github/workflows/build.yml](https://github.com/ramda/ramda/blob/f4b2e35ff433e18c751326b82acc3c6ab3585e18/.github/workflows/build.yml) · [GitHub API](https://api.github.com/repos/ramda/ramda).

<a id="anhkysuai-eza-community-eza"></a>

### eza

**Repo:** [eza-community/eza](https://github.com/eza-community/eza) · **License:** EUPL-1.2 · **Kiểm:** 2026-11-23, `docs-read`, [`471bfbc7b03c`](https://github.com/eza-community/eza/tree/471bfbc7b03cbac8c738e8d9050edb06ee79132a) (commit 2026-07-09). **Sao:** 24,009 tại 2026-11-23 theo [GitHub API](https://api.github.com/repos/eza-community/eza).

| Mục | Đánh giá |
|---|---|
| Mục đích | CLI liệt kê tệp thay thế ls, bổ sung màu, metadata và trạng thái Git. |
| Giá trị và cơ chế theo tài liệu | README phân biệt các cải tiến so với exa, hỗ trợ symlink/xattr và theme YAML; Cargo khai báo Rust 1.90, CI có unit tests và cargo-deny. |
| Giới hạn | Không mặc nhiên dùng output trang trí làm giao diện parse của script. Commit đã đọc là tháng 7/2026; tính nhanh và nhỏ chưa được đo trên cây thư mục lớn. |
| Điều kiện tích hợp | Thử tương tác terminal/font/color trước khi alias, giữ ls chuẩn cho script cần ổn định; kiểm đối số, permission và cách hiển thị tên tệp lạ. |
| Lựa chọn đối chiếu | GNU ls; lsd; broot. |

**Phạm vi bằng chứng:** đã clone, đọc trích đoạn tài liệu, giấy phép và các file cấu hình được dẫn dưới đây; chưa chạy mã, build, benchmark hoặc test upstream. `docs-read` không phải kiểm chứng implementation.

**Nguồn tại cùng SHA:** [README.md](https://github.com/eza-community/eza/blob/471bfbc7b03cbac8c738e8d9050edb06ee79132a/README.md) · [LICENSE.txt](https://github.com/eza-community/eza/blob/471bfbc7b03cbac8c738e8d9050edb06ee79132a/LICENSE.txt) · [Cargo.toml](https://github.com/eza-community/eza/blob/471bfbc7b03cbac8c738e8d9050edb06ee79132a/Cargo.toml) · [.github/workflows/unit-tests.yml](https://github.com/eza-community/eza/blob/471bfbc7b03cbac8c738e8d9050edb06ee79132a/.github/workflows/unit-tests.yml).

<a id="anhkysuai-nikitabobko-aerospace"></a>

### AeroSpace

**Đã chuyển (2026-11-23):** hồ sơ này nay nằm ở [mục 35](../35-desktop-productivity-apps/README.md#anhkysuai-nikitabobko-aerospace); catalog con xem [catalog/](../catalog/README.md).

<a id="anhkysuai-ruby-ruby"></a>

### Ruby

**Đã chuyển (2026-11-23):** hồ sơ này nay nằm ở [mục 37](../37-programming-languages-runtimes/README.md#anhkysuai-ruby-ruby); catalog con xem [catalog/](../catalog/README.md).

<a id="anhkysuai-validatorjs-validator.js"></a>

### validator.js

**Repo:** [validatorjs/validator.js](https://github.com/validatorjs/validator.js) · **License:** MIT · **Kiểm:** 2026-11-23, `docs-read`, [`9ff342479591`](https://github.com/validatorjs/validator.js/tree/9ff342479591ca5a43cb30000195bcf55c1bbed9) (commit 2026-09-11). **Sao:** 23,741 tại 2026-11-23 theo [GitHub API](https://api.github.com/repos/validatorjs/validator.js).

| Mục | Đánh giá |
|---|---|
| Mục đích | Thư viện validator và sanitizer dành riêng cho chuỗi JavaScript. |
| Giá trị và cơ chế theo tài liệu | README nhấn mạnh input phải là string, có import từng hàm và ES module tree-shakeable; CI build/lint rồi test nhiều Node. |
| Giới hạn | Validation định dạng không xác thực quyền sở hữu email/URL hay tính an toàn mọi ngữ cảnh. Ép kiểu đầu vào có thể mất ý nghĩa; chưa kiểm từng regex, locale hoặc input đối nghịch. |
| Điều kiện tích hợp | Chọn validator/options cụ thể, kiểm kiểu trước và xác minh nghiệp vụ riêng; thử Unicode, giới hạn độ dài, trường thiếu và dữ liệu không hợp lệ ở server. |
| Lựa chọn đối chiếu | Zod; [Joi](../34-backend-data-identity-integration/README.md#anhkysuai-hapijs-joi); Valibot. |

**Phạm vi bằng chứng:** đã clone, đọc trích đoạn tài liệu, giấy phép và các file cấu hình được dẫn dưới đây; chưa chạy mã, build, benchmark hoặc test upstream. `docs-read` không phải kiểm chứng implementation.

**Nguồn tại cùng SHA:** [README.md](https://github.com/validatorjs/validator.js/blob/9ff342479591ca5a43cb30000195bcf55c1bbed9/README.md) · [LICENSE](https://github.com/validatorjs/validator.js/blob/9ff342479591ca5a43cb30000195bcf55c1bbed9/LICENSE) · [package.json](https://github.com/validatorjs/validator.js/blob/9ff342479591ca5a43cb30000195bcf55c1bbed9/package.json) · [.github/workflows/ci.yml](https://github.com/validatorjs/validator.js/blob/9ff342479591ca5a43cb30000195bcf55c1bbed9/.github/workflows/ci.yml).

<a id="anhkysuai-kriasoft-react-starter-kit"></a>

### React Starter Kit

**Repo:** [kriasoft/react-starter-kit](https://github.com/kriasoft/react-starter-kit) · **License:** MIT · **Kiểm:** 2026-11-23, `docs-read`, [`dbdb0d4991bb`](https://github.com/kriasoft/react-starter-kit/tree/dbdb0d4991bbaae1671ff62180089f2733dd406a) (commit 2026-10-02). **Sao:** 23,726 tại 2026-11-23 theo [GitHub API](https://api.github.com/repos/kriasoft/react-starter-kit).

| Mục | Đánh giá |
|---|---|
| Mục đích | Template SaaS monorepo React/tRPC chạy trên Cloudflare Workers. |
| Giá trị và cơ chế theo tài liệu | README mô tả ba worker web/app/api nối service bindings, Better Auth/Stripe/Neon và type contract Drizzle-to-UI; CI có format/lint/typecheck/infra checks. |
| Giới hạn | Type-safe không bảo đảm quyền tenant, billing hay dữ liệu đúng lúc runtime. Deployment phụ thuộc dịch vụ cloud và credential riêng; chưa chạy template hoặc thử thanh toán. |
| Điều kiện tích hợp | Fork và thử staging, kiểm auth/org, webhook Stripe sandbox và migration; ghim Bun/toolchain, chốt cấu hình secrets và chi phí cloud trước tạo môi trường thật. |
| Lựa chọn đối chiếu | T3 Stack; Full Stack FastAPI Template; RedwoodSDK. |

**Phạm vi bằng chứng:** đã clone, đọc trích đoạn tài liệu, giấy phép và các file cấu hình được dẫn dưới đây; chưa chạy mã, build, benchmark hoặc test upstream. `docs-read` không phải kiểm chứng implementation.

**Nguồn tại cùng SHA:** [README.md](https://github.com/kriasoft/react-starter-kit/blob/dbdb0d4991bbaae1671ff62180089f2733dd406a/README.md) · [LICENSE](https://github.com/kriasoft/react-starter-kit/blob/dbdb0d4991bbaae1671ff62180089f2733dd406a/LICENSE) · [package.json](https://github.com/kriasoft/react-starter-kit/blob/dbdb0d4991bbaae1671ff62180089f2733dd406a/package.json) · [.github/workflows/ci.yml](https://github.com/kriasoft/react-starter-kit/blob/dbdb0d4991bbaae1671ff62180089f2733dd406a/.github/workflows/ci.yml).

<a id="anhkysuai-aldanial-cloc"></a>

### cloc

**Repo:** [AlDanial/cloc](https://github.com/AlDanial/cloc) · **License:** GPL-2.0 · **Kiểm:** 2026-11-23, `docs-read`, [`414fe1617b75`](https://github.com/AlDanial/cloc/tree/414fe1617b75fa2847844295ac423180db9ca4ea) (commit 2026-11-17). **Sao:** 23,683 tại 2026-11-23 theo [GitHub API](https://api.github.com/repos/AlDanial/cloc).

| Mục | Đánh giá |
|---|---|
| Mục đích | CLI đếm dòng mã, chú thích và dòng trống theo nhiều ngôn ngữ. |
| Giá trị và cơ chế theo tài liệu | README phân biệt script Perl, binary Windows và Docker, hỗ trợ file/thư mục/archive/commit; workflow chạy bộ test của công cụ. |
| Giới hạn | Số dòng không đo chất lượng, năng suất hoặc độ phức tạp nghiệp vụ. Nhận dạng ngôn ngữ và loại trừ generated/vendor ảnh hưởng kết quả; chưa chạy trên repo mẫu. |
| Điều kiện tích hợp | Ghim phiên bản, định nghĩa rule exclude nhất quán và lưu cấu hình với báo cáo; thử vài file đại diện trước dùng để so sánh lịch sử kho. |
| Lựa chọn đối chiếu | tokei; scc; Sloccount. |

**Phạm vi bằng chứng:** đã clone, đọc trích đoạn tài liệu, giấy phép và các file cấu hình được dẫn dưới đây; chưa chạy mã, build, benchmark hoặc test upstream. `docs-read` không phải kiểm chứng implementation.

**Nguồn tại cùng SHA:** [README.md](https://github.com/AlDanial/cloc/blob/414fe1617b75fa2847844295ac423180db9ca4ea/README.md) · [LICENSE](https://github.com/AlDanial/cloc/blob/414fe1617b75fa2847844295ac423180db9ca4ea/LICENSE) · [.github/workflows/build.yml](https://github.com/AlDanial/cloc/blob/414fe1617b75fa2847844295ac423180db9ca4ea/.github/workflows/build.yml).

<a id="anhkysuai-winboat-org-winboat"></a>

### WinBoat

**Đã chuyển (2026-11-23):** hồ sơ này nay nằm ở [mục 35](../35-desktop-productivity-apps/README.md#anhkysuai-winboat-org-winboat); catalog con xem [catalog/](../catalog/README.md).

<a id="anhkysuai-reduxjs-react-redux"></a>

### React Redux

**Repo:** [reduxjs/react-redux](https://github.com/reduxjs/react-redux) · **License:** MIT · **Kiểm:** 2026-11-23, `docs-read`, [`8e54f5b9dbbd`](https://github.com/reduxjs/react-redux/tree/8e54f5b9dbbdcc972c120ad3ce3c1c57fc2e89fd) (commit 2026-10-27). **Sao:** 23,422 tại 2026-11-23 theo [GitHub API](https://api.github.com/repos/reduxjs/react-redux).

| Mục | Đánh giá |
|---|---|
| Mục đích | Binding chính thức kết nối Redux store với ứng dụng React. |
| Giá trị và cơ chế theo tài liệu | README hướng tới template Redux Toolkit/TypeScript và yêu cầu React 18+; package 9.3.1 có Vitest/type tests, CI build/test. |
| Giới hạn | Đây là lớp binding, không phải toàn bộ state architecture. Selector, equality và tổ chức store ảnh hưởng render; chưa kiểm performance, hydration hoặc React version của ứng dụng. |
| Điều kiện tích hợp | Dùng cùng Redux Toolkit/release tương thích, giữ selector có kiểm và tách state server/client; đo render thực tế và thử SSR trước mở rộng store toàn app. |
| Lựa chọn đối chiếu | Zustand; [Jotai](../13-dev-stack-devops/README.md#anhkysuai-pmndrs-jotai); React Context. |

**Phạm vi bằng chứng:** đã clone, đọc trích đoạn tài liệu, giấy phép và các file cấu hình được dẫn dưới đây; chưa chạy mã, build, benchmark hoặc test upstream. `docs-read` không phải kiểm chứng implementation.

**Nguồn tại cùng SHA:** [README.md](https://github.com/reduxjs/react-redux/blob/8e54f5b9dbbdcc972c120ad3ce3c1c57fc2e89fd/README.md) · [LICENSE.md](https://github.com/reduxjs/react-redux/blob/8e54f5b9dbbdcc972c120ad3ce3c1c57fc2e89fd/LICENSE.md) · [package.json](https://github.com/reduxjs/react-redux/blob/8e54f5b9dbbdcc972c120ad3ce3c1c57fc2e89fd/package.json) · [.github/workflows/test.yml](https://github.com/reduxjs/react-redux/blob/8e54f5b9dbbdcc972c120ad3ce3c1c57fc2e89fd/.github/workflows/test.yml).

<a id="anhkysuai-chalk-chalk"></a>

### Chalk

**Repo:** [chalk/chalk](https://github.com/chalk/chalk) · **License:** MIT · **Kiểm:** 2026-11-23, `docs-read`, [`72110019e147`](https://github.com/chalk/chalk/tree/72110019e147683f60e13fa0ff5c14a0c27cd9fe) (commit 2026-10-23). **Sao:** 23,349 tại 2026-11-23 theo [GitHub API](https://api.github.com/repos/chalk/chalk).

| Mục | Đánh giá |
|---|---|
| Mục đích | Thư viện tạo màu và kiểu chữ ANSI cho output terminal JavaScript. |
| Giá trị và cơ chế theo tài liệu | README mô tả chain/nest style, tự nhận khả năng màu và không sửa String.prototype; package 6.0.1 yêu cầu Node 22+, CI chạy test/typecheck. |
| Giới hạn | Đoạn hướng dẫn README còn nhắc Chalk 5/4 nên cần đối chiếu manifest/release hiện tại. Output màu không thích hợp mọi log sink, và hiệu năng chưa benchmark trong pipeline thực. |
| Điều kiện tích hợp | Ghim version phù hợp ESM/runtime, thử TTY/redirect/NO_COLOR và Unicode; giữ output máy đọc được tách khỏi nội dung trang trí terminal. |
| Lựa chọn đối chiếu | yoctocolors; picocolors; Node util.styleText. |

**Phạm vi bằng chứng:** đã clone, đọc trích đoạn tài liệu, giấy phép và các file cấu hình được dẫn dưới đây; chưa chạy mã, build, benchmark hoặc test upstream. `docs-read` không phải kiểm chứng implementation.

**Nguồn tại cùng SHA:** [readme.md](https://github.com/chalk/chalk/blob/72110019e147683f60e13fa0ff5c14a0c27cd9fe/readme.md) · [license](https://github.com/chalk/chalk/blob/72110019e147683f60e13fa0ff5c14a0c27cd9fe/license) · [package.json](https://github.com/chalk/chalk/blob/72110019e147683f60e13fa0ff5c14a0c27cd9fe/package.json) · [.github/workflows/main.yml](https://github.com/chalk/chalk/blob/72110019e147683f60e13fa0ff5c14a0c27cd9fe/.github/workflows/main.yml).

<a id="anhkysuai-conwnet-github1s"></a>

### GitHub1s

**Repo:** [conwnet/github1s](https://github.com/conwnet/github1s) · **License:** MIT trong LICENSE; package.json ghi ISC · **Kiểm:** 2026-11-23, `docs-read`, [`98ddf0fbd549`](https://github.com/conwnet/github1s/tree/98ddf0fbd549c398ffbd2bb6f62051d156d50394) (commit 2026-11-17). **Sao:** 23,307 tại 2026-11-23 theo [GitHub API](https://api.github.com/repos/conwnet/github1s).

| Mục | Đánh giá |
|---|---|
| Mục đích | Trình đọc mã trên browser theo giao diện VS Code, có AI chat tùy model. |
| Giá trị và cơ chế theo tài liệu | README mô tả xem file/history/diff cho GitHub/GitLab/npm và repo remote chỉ đọc; CI build cùng Playwright snapshot tests. |
| Giới hạn | LICENSE MIT và manifest ISC không thống nhất; ưu tiên thông báo file nhưng cần làm rõ khi phân phối. Tìm kiếm phụ thuộc upstream/rate limit; AI có thể gửi mã cho provider. |
| Điều kiện tích hợp | Thử repo công khai trước, cấp token tối thiểu cho repo riêng; kiểm dữ liệu model nhận, lưu token và giới hạn navigation, không coi AI giải thích là xác minh mã. |
| Lựa chọn đối chiếu | github.dev; Sourcegraph; VS Code Web. |

**Phạm vi bằng chứng:** đã clone, đọc trích đoạn tài liệu, giấy phép và các file cấu hình được dẫn dưới đây; chưa chạy mã, build, benchmark hoặc test upstream. `docs-read` không phải kiểm chứng implementation.

**Nguồn tại cùng SHA:** [README.md](https://github.com/conwnet/github1s/blob/98ddf0fbd549c398ffbd2bb6f62051d156d50394/README.md) · [LICENSE](https://github.com/conwnet/github1s/blob/98ddf0fbd549c398ffbd2bb6f62051d156d50394/LICENSE) · [package.json](https://github.com/conwnet/github1s/blob/98ddf0fbd549c398ffbd2bb6f62051d156d50394/package.json) · [.github/workflows/build.yml](https://github.com/conwnet/github1s/blob/98ddf0fbd549c398ffbd2bb6f62051d156d50394/.github/workflows/build.yml).

<a id="anhkysuai-codeeditapp-codeedit"></a>

### CodeEdit

**Repo:** [CodeEditApp/CodeEdit](https://github.com/CodeEditApp/CodeEdit) · **License:** MIT · **Kiểm:** 2026-11-23, `docs-read`, [`fa2aebd86373`](https://github.com/CodeEditApp/CodeEdit/tree/fa2aebd86373211c78626074b53ab75010767575) (commit 2026-08-18). **Sao:** 23,125 tại 2026-11-23 theo [GitHub API](https://api.github.com/repos/CodeEditApp/CodeEdit).

| Mục | Đánh giá |
|---|---|
| Mục đích | Code editor native macOS với hướng mở rộng thành môi trường phát triển đầy đủ. |
| Giá trị và cơ chế theo tài liệu | README liệt kê tìm kiếm, terminal, task, debug, Git và extension; CI gọi script test app trên kiến trúc ARM. |
| Giới hạn | README nói rõ còn phát triển và chưa khuyến nghị production. Danh sách tính năng không chứng minh mọi đường đã hoàn thiện; chưa chạy app, extension hay kiểm file save/recovery. |
| Điều kiện tích hợp | Thử trên bản sao dự án với Git/backup sẵn, đối chiếu ngôn ngữ và debugger cần dùng; kiểm save, undo, terminal và phiên bản macOS trước thay editor chính. |
| Lựa chọn đối chiếu | [Zed](../08-awesome-lists-learning/README.md#6c58-editor-terminal--dòng-lệnh); VS Code; Xcode. |

**Phạm vi bằng chứng:** đã clone, đọc trích đoạn tài liệu, giấy phép và các file cấu hình được dẫn dưới đây; chưa chạy mã, build, benchmark hoặc test upstream. `docs-read` không phải kiểm chứng implementation.

**Nguồn tại cùng SHA:** [README.md](https://github.com/CodeEditApp/CodeEdit/blob/fa2aebd86373211c78626074b53ab75010767575/README.md) · [LICENSE.md](https://github.com/CodeEditApp/CodeEdit/blob/fa2aebd86373211c78626074b53ab75010767575/LICENSE.md) · [.github/workflows/tests.yml](https://github.com/CodeEditApp/CodeEdit/blob/fa2aebd86373211c78626074b53ab75010767575/.github/workflows/tests.yml).

<a id="anhkysuai-gitui-org-gitui"></a>

### GitUI

**Repo:** [gitui-org/gitui](https://github.com/gitui-org/gitui) · **License:** MIT · **Kiểm:** 2026-11-23, `docs-read`, [`d7214eccb3ca`](https://github.com/gitui-org/gitui/tree/d7214eccb3cac52ce3f8d9ca18f218671821eeee) (commit 2026-10-06). **Sao:** 22,681 tại 2026-11-23 theo [GitHub API](https://api.github.com/repos/gitui-org/gitui).

| Mục | Đánh giá |
|---|---|
| Mục đích | Giao diện terminal dùng bàn phím để xem diff, stage từng dòng hoặc hunk, commit và thao tác stash. |
| Giá trị và cơ chế theo tài liệu | README mô tả hỗ trợ hooks, fetch/push và lịch sử commit; Cargo.toml 0.28.1 yêu cầu Rust 1.88, workflow có build Rust. Hữu ích cho thao tác Git tại máy phát triển hoặc SSH. |
| Giới hạn | Upstream vẫn gọi beta, nêu thiếu sparse repo và Git LFS, cần cấu hình credential.helper rõ ràng; interactive rebase nằm trong roadmap. Chưa đo tốc độ hay thử thao tác Git. |
| Điều kiện tích hợp | Thử trên bản sao repo, giữ Git CLI cho ca chưa hỗ trợ; kiểm hooks, credential và phím reset/revert trước dùng với thay đổi chưa commit. |
| Lựa chọn đối chiếu | [Lazygit](../08-awesome-lists-learning/README.md#6c58-editor-terminal--dòng-lệnh); Tig; [GitButler](../13-dev-stack-devops/README.md#anhkysuai-gitbutlerapp-gitbutler). |

**Phạm vi bằng chứng:** đã clone, đọc trích đoạn tài liệu, giấy phép và các file cấu hình được dẫn dưới đây; chưa chạy mã, build, benchmark hoặc test upstream. `docs-read` không phải kiểm chứng implementation.

**Nguồn tại cùng SHA:** [README.md](https://github.com/gitui-org/gitui/blob/d7214eccb3cac52ce3f8d9ca18f218671821eeee/README.md) · [LICENSE.md](https://github.com/gitui-org/gitui/blob/d7214eccb3cac52ce3f8d9ca18f218671821eeee/LICENSE.md) · [Cargo.toml](https://github.com/gitui-org/gitui/blob/d7214eccb3cac52ce3f8d9ca18f218671821eeee/Cargo.toml) · [.github/workflows/ci.yml](https://github.com/gitui-org/gitui/blob/d7214eccb3cac52ce3f8d9ca18f218671821eeee/.github/workflows/ci.yml).

<a id="anhkysuai-emberjs-ember.js"></a>

### Ember.js

**Repo:** [emberjs/ember.js](https://github.com/emberjs/ember.js) · **License:** MIT · **Kiểm:** 2026-11-23, `docs-read`, [`a8dde59e2fcb`](https://github.com/emberjs/ember.js/tree/a8dde59e2fcb7f891a1b1561cdbdafe1f3a0311a) (commit 2026-11-16). **Sao:** 22,570 tại 2026-11-23 theo [GitHub API](https://api.github.com/repos/emberjs/ember.js).

| Mục | Đánh giá |
|---|---|
| Mục đích | Framework JavaScript cho ứng dụng web có routing, component HTML và quy ước phát triển thống nhất. |
| Giá trị và cơ chế theo tài liệu | README tập trung nền tảng lâu dài, tài liệu theo phiên bản và LTS; manifest có build, benchmark và kiểm kiểu. Có giá trị khi đội muốn nhiều quyết định kiến trúc được chuẩn hóa. |
| Giới hạn | Snapshot là ember-source 7.6.0-alpha.1 với Node tối thiểu 20.19; không đồng nhất nhánh chính với bản ổn định. Cam kết LTS trong README chưa được kiểm lịch phát hành độc lập. |
| Điều kiện tích hợp | Chọn phiên bản release phù hợp, kiểm addon và đường nâng cấp; làm một luồng route/data/component mẫu trước quyết định chuyển ứng dụng lớn. |
| Lựa chọn đối chiếu | Angular; Vue; [SvelteKit](../13-dev-stack-devops/README.md#anhkysuai-sveltejs-kit). |

**Phạm vi bằng chứng:** đã clone, đọc trích đoạn tài liệu, giấy phép và các file cấu hình được dẫn dưới đây; chưa chạy mã, build, benchmark hoặc test upstream. `docs-read` không phải kiểm chứng implementation.

**Nguồn tại cùng SHA:** [README.md](https://github.com/emberjs/ember.js/blob/a8dde59e2fcb7f891a1b1561cdbdafe1f3a0311a/README.md) · [LICENSE](https://github.com/emberjs/ember.js/blob/a8dde59e2fcb7f891a1b1561cdbdafe1f3a0311a/LICENSE) · [package.json](https://github.com/emberjs/ember.js/blob/a8dde59e2fcb7f891a1b1561cdbdafe1f3a0311a/package.json) · [.github/workflows/ci.yml](https://github.com/emberjs/ember.js/blob/a8dde59e2fcb7f891a1b1561cdbdafe1f3a0311a/.github/workflows/ci.yml).

<a id="anhkysuai-js-cookie-js-cookie"></a>

### JavaScript Cookie

**Repo:** [js-cookie/js-cookie](https://github.com/js-cookie/js-cookie) · **License:** MIT · **Kiểm:** 2026-11-23, `docs-read`, [`e9a4b83402a9`](https://github.com/js-cookie/js-cookie/tree/e9a4b83402a9d09065831f0e02820478a569253e) (commit 2026-10-22). **Sao:** 22,559 tại 2026-11-23 theo [GitHub API](https://api.github.com/repos/js-cookie/js-cookie).

| Mục | Đánh giá |
|---|---|
| Mục đích | API JavaScript nhỏ để đọc, ghi và xóa cookie phía trình duyệt, với thuộc tính và bộ chuyển đổi encoding. |
| Giá trị và cơ chế theo tài liệu | README có API Cookies.set/get/remove, withAttributes và withConverter; manifest 3.0.8 không phụ thuộc runtime theo mô tả, CI gọi kiểm định dạng, lint và unit test. |
| Giới hạn | Cookie quá lớn hoặc quá nhiều có thể bị trình duyệt xóa; encoding mặc định chủ yếu tương thích giữa các cookie do thư viện tạo. SameSite mặc định không được thư viện đặt rõ. |
| Điều kiện tích hợp | Đặt domain, path, Secure và SameSite theo nhu cầu; khi xóa dùng lại thuộc tính lúc tạo. Giữ cookie phiên nhạy cảm do máy chủ quản lý với HttpOnly; thử trên trình duyệt mục tiêu. |
| Lựa chọn đối chiếu | Cookie Store API; cookie-es; universal-cookie. |

**Phạm vi bằng chứng:** đã clone, đọc trích đoạn tài liệu, giấy phép và các file cấu hình được dẫn dưới đây; chưa chạy mã, build, benchmark hoặc test upstream. `docs-read` không phải kiểm chứng implementation.

**Nguồn tại cùng SHA:** [README.md](https://github.com/js-cookie/js-cookie/blob/e9a4b83402a9d09065831f0e02820478a569253e/README.md) · [LICENSE](https://github.com/js-cookie/js-cookie/blob/e9a4b83402a9d09065831f0e02820478a569253e/LICENSE) · [package.json](https://github.com/js-cookie/js-cookie/blob/e9a4b83402a9d09065831f0e02820478a569253e/package.json) · [.github/workflows/ci.yml](https://github.com/js-cookie/js-cookie/blob/e9a4b83402a9d09065831f0e02820478a569253e/.github/workflows/ci.yml).

<a id="anhkysuai-rustpython-rustpython"></a>

### RustPython

**Đã chuyển (2026-11-23):** hồ sơ này nay nằm ở [mục 37](../37-programming-languages-runtimes/README.md#anhkysuai-rustpython-rustpython); catalog con xem [catalog/](../catalog/README.md).

<a id="anhkysuai-vueuse-vueuse"></a>

### VueUse

**Repo:** [vueuse/vueuse](https://github.com/vueuse/vueuse) · **License:** MIT · **Kiểm:** 2026-11-23, `docs-read`, [`84e7caedab4e`](https://github.com/vueuse/vueuse/tree/84e7caedab4e79e13159d3390fa46f817e3f4eaa) (commit 2026-11-19). **Sao:** 22,402 tại 2026-11-23 theo [GitHub API](https://api.github.com/repos/vueuse/vueuse).

| Mục | Đánh giá |
|---|---|
| Mục đích | Tập tiện ích Composition API cho Vue, gồm trạng thái trình duyệt, lưu trữ và tương tác sự kiện. |
| Giá trị và cơ chế theo tài liệu | README minh họa useMouse, usePreferredDark và useLocalStorage; có TypeScript, bộ lọc sự kiện và addon Router/Firebase/RxJS. Manifest snapshot 15.0.0 tổ chức monorepo với build kiểu và docs. |
| Giới hạn | Tài liệu nêu v14 cần Vue 3.5+, v12 bỏ Vue 2; không coi mọi composable tự an toàn SSR hoặc mọi addon không tăng bundle. Chưa đo kích thước hay thử hydration. |
| Điều kiện tích hợp | Chọn đúng phiên bản Vue, import từng chức năng và kiểm lifecycle cleanup; với localStorage, xử lý dữ liệu cũ, quota và môi trường không có window. |
| Lựa chọn đối chiếu | Vue Composables; react-use; Solid Primitives. |

**Phạm vi bằng chứng:** đã clone, đọc trích đoạn tài liệu, giấy phép và các file cấu hình được dẫn dưới đây; chưa chạy mã, build, benchmark hoặc test upstream. `docs-read` không phải kiểm chứng implementation.

**Nguồn tại cùng SHA:** [README.md](https://github.com/vueuse/vueuse/blob/84e7caedab4e79e13159d3390fa46f817e3f4eaa/README.md) · [LICENSE](https://github.com/vueuse/vueuse/blob/84e7caedab4e79e13159d3390fa46f817e3f4eaa/LICENSE) · [package.json](https://github.com/vueuse/vueuse/blob/84e7caedab4e79e13159d3390fa46f817e3f4eaa/package.json) · [.github/workflows/ci.yml](https://github.com/vueuse/vueuse/blob/84e7caedab4e79e13159d3390fa46f817e3f4eaa/.github/workflows/ci.yml).

<a id="anhkysuai-micropython-micropython"></a>

### MicroPython

**Đã chuyển (2026-11-23):** hồ sơ này nay nằm ở [mục 37](../37-programming-languages-runtimes/README.md#anhkysuai-micropython-micropython); catalog con xem [catalog/](../catalog/README.md).

<a id="anhkysuai-postcss-autoprefixer"></a>

### Autoprefixer

**Repo:** [postcss/autoprefixer](https://github.com/postcss/autoprefixer) · **License:** MIT · **Kiểm:** 2026-11-23, `docs-read`, [`12322da05edc`](https://github.com/postcss/autoprefixer/tree/12322da05edc5823ef1bb98b250a18b929b63cb7) (commit 2026-11-22). **Sao:** 22,197 tại 2026-11-23 theo [GitHub API](https://api.github.com/repos/postcss/autoprefixer).

| Mục | Đánh giá |
|---|---|
| Mục đích | Plugin PostCSS tự thêm vendor prefix theo dữ liệu Can I Use để duy trì CSS theo nhóm trình duyệt mục tiêu. |
| Giá trị và cơ chế theo tài liệu | README có ví dụ biến đổi placeholder và width; manifest 10.7.0 có unit test, coverage và kiểm kích thước, workflow gọi test trên các bản Node. Hữu ích để tập trung chính sách hỗ trợ CSS trong build. |
| Giới hạn | Prefix không đồng nghĩa polyfill mọi tính năng hoặc giao diện hoạt động đúng ở mọi trình duyệt. Kết quả phụ thuộc dữ liệu và cấu hình browser; chưa chạy kiểm hồi quy hiển thị. |
| Điều kiện tích hợp | Khai báo Browserslist rõ ràng, khóa dependency và cập nhật dữ liệu có kiểm soát; kiểm CSS đầu ra cùng ảnh chụp trang thật trước thay đổi mục tiêu trình duyệt. |
| Lựa chọn đối chiếu | Lightning CSS; PostCSS Preset Env; Stylis. |

**Phạm vi bằng chứng:** đã clone, đọc trích đoạn tài liệu, giấy phép và các file cấu hình được dẫn dưới đây; chưa chạy mã, build, benchmark hoặc test upstream. `docs-read` không phải kiểm chứng implementation.

**Nguồn tại cùng SHA:** [README.md](https://github.com/postcss/autoprefixer/blob/12322da05edc5823ef1bb98b250a18b929b63cb7/README.md) · [LICENSE](https://github.com/postcss/autoprefixer/blob/12322da05edc5823ef1bb98b250a18b929b63cb7/LICENSE) · [package.json](https://github.com/postcss/autoprefixer/blob/12322da05edc5823ef1bb98b250a18b929b63cb7/package.json) · [.github/workflows/test.yml](https://github.com/postcss/autoprefixer/blob/12322da05edc5823ef1bb98b250a18b929b63cb7/.github/workflows/test.yml).

<a id="anhkysuai-gleam-lang-gleam"></a>

### Gleam

**Đã chuyển (2026-11-23):** hồ sơ này nay nằm ở [mục 37](../37-programming-languages-runtimes/README.md#anhkysuai-gleam-lang-gleam); catalog con xem [catalog/](../catalog/README.md).

<a id="anhkysuai-qwikdev-qwik"></a>

### Qwik

**Repo:** [QwikDev/qwik](https://github.com/QwikDev/qwik) · **License:** MIT · **Kiểm:** 2026-11-23, `docs-read`, [`782ed25a3c3a`](https://github.com/QwikDev/qwik/tree/782ed25a3c3a8b61c376fca0ef822d5294949579) (commit 2026-11-22). **Sao:** 22,076 tại 2026-11-23 theo [GitHub API](https://api.github.com/repos/QwikDev/qwik).

| Mục | Đánh giá |
|---|---|
| Mục đích | Framework web theo hướng resumability, tải mã tương tác khi cần dựa trên trạng thái do server để lại. |
| Giá trị và cơ chế theo tài liệu | README mô tả lazy-loading có chọn lọc; repo có core/router/React adapter/devtools và optimizer Rust. Đây là hướng tham khảo cho website cần giảm JavaScript ban đầu. |
| Giới hạn | Nhánh được clone là Qwik v2 beta; README chỉ sang nhánh v1 cho bản trước. Tuyên bố tốc độ tải của upstream chưa được đo lại; API, adapter và tích hợp cần kiểm đúng dòng phiên bản. |
| Điều kiện tích hợp | Dùng bản phát hành cụ thể, thử SSR và tương tác dưới mạng chậm; đo dữ liệu serialize, chunk tải thêm và khả năng debug trước chọn cho sản phẩm. |
| Lựa chọn đối chiếu | Astro; [SvelteKit](../13-dev-stack-devops/README.md#anhkysuai-sveltejs-kit); Next.js. |

**Phạm vi bằng chứng:** đã clone, đọc trích đoạn tài liệu, giấy phép và các file cấu hình được dẫn dưới đây; chưa chạy mã, build, benchmark hoặc test upstream. `docs-read` không phải kiểm chứng implementation.

**Nguồn tại cùng SHA:** [README.md](https://github.com/QwikDev/qwik/blob/782ed25a3c3a8b61c376fca0ef822d5294949579/README.md) · [LICENSE](https://github.com/QwikDev/qwik/blob/782ed25a3c3a8b61c376fca0ef822d5294949579/LICENSE) · [package.json](https://github.com/QwikDev/qwik/blob/782ed25a3c3a8b61c376fca0ef822d5294949579/package.json) · [Cargo.toml](https://github.com/QwikDev/qwik/blob/782ed25a3c3a8b61c376fca0ef822d5294949579/Cargo.toml) · [.github/workflows/ci.yml](https://github.com/QwikDev/qwik/blob/782ed25a3c3a8b61c376fca0ef822d5294949579/.github/workflows/ci.yml).

<a id="anhkysuai-gitbutlerapp-gitbutler"></a>

### GitButler

**Repo:** [gitbutlerapp/gitbutler](https://github.com/gitbutlerapp/gitbutler) · **License:** FSL-1.1-MIT; MIT có hiệu lực sau hai năm cho từng phiên bản · **Kiểm:** 2026-11-23, `docs-read`, [`c4087cbd307f`](https://github.com/gitbutlerapp/gitbutler/tree/c4087cbd307fb72c08a0e88cc2e787cdd3030ece) (commit 2026-11-23). **Sao:** 22,010 tại 2026-11-23 theo [GitHub API](https://api.github.com/repos/gitbutlerapp/gitbutler).

| Mục | Đánh giá |
|---|---|
| Mục đích | Ứng dụng và CLI quản lý Git với stacked branch, parallel branch, chỉnh commit và khả năng hoàn tác. |
| Giá trị và cơ chế theo tài liệu | README hướng tới quy trình của lập trình viên và agent; repo tổ chức Tauri/Rust/Svelte, có workflow e2e. Có thể giúp chia và sắp lại thay đổi đang làm giữa nhiều nhánh. |
| Giới hạn | LICENSE hiện là FSL, hạn chế cung cấp sản phẩm hoặc dịch vụ thương mại cạnh tranh; phần MIT là giấy phép tương lai sau hai năm, không phải giấy phép hiện hành của snapshot mới. |
| Điều kiện tích hợp | Dùng thử trên bản sao repo với backup và remote thử nghiệm; kiểm cách tương tác Git CLI, hooks, worktree và lịch sử trước dùng cho nhánh chung. Chưa thử hoàn tác hoặc xử lý xung đột. |
| Lựa chọn đối chiếu | [Lazygit](../08-awesome-lists-learning/README.md#6c58-editor-terminal--dòng-lệnh); [GitUI](../13-dev-stack-devops/README.md#anhkysuai-gitui-org-gitui); Jujutsu. |

**Phạm vi bằng chứng:** đã clone, đọc trích đoạn tài liệu, giấy phép và các file cấu hình được dẫn dưới đây; chưa chạy mã, build, benchmark hoặc test upstream. `docs-read` không phải kiểm chứng implementation.

**Nguồn tại cùng SHA:** [README.md](https://github.com/gitbutlerapp/gitbutler/blob/c4087cbd307fb72c08a0e88cc2e787cdd3030ece/README.md) · [LICENSE.md](https://github.com/gitbutlerapp/gitbutler/blob/c4087cbd307fb72c08a0e88cc2e787cdd3030ece/LICENSE.md) · [package.json](https://github.com/gitbutlerapp/gitbutler/blob/c4087cbd307fb72c08a0e88cc2e787cdd3030ece/package.json) · [Cargo.toml](https://github.com/gitbutlerapp/gitbutler/blob/c4087cbd307fb72c08a0e88cc2e787cdd3030ece/Cargo.toml) · [.github/workflows/test-e2e.yml](https://github.com/gitbutlerapp/gitbutler/blob/c4087cbd307fb72c08a0e88cc2e787cdd3030ece/.github/workflows/test-e2e.yml).

<a id="anhkysuai-eclipse-theia-theia"></a>

### Eclipse Theia

**Repo:** [eclipse-theia/theia](https://github.com/eclipse-theia/theia) · **License:** EPL-2.0; GPL-2.0 với Classpath Exception là secondary; một số tệp MIT · **Kiểm:** 2026-11-23, `docs-read`, [`f5d466aa4652`](https://github.com/eclipse-theia/theia/tree/f5d466aa4652a7b9e99929a3ced8be3087292163) (commit 2026-11-20). **Sao:** 21,783 tại 2026-11-23 theo [GitHub API](https://api.github.com/repos/eclipse-theia/theia).

| Mục | Đánh giá |
|---|---|
| Mục đích | Nền tảng xây IDE và công cụ tùy biến chạy trên trình duyệt hoặc desktop Electron. |
| Giá trị và cơ chế theo tài liệu | README nêu kiến trúc mở rộng và hỗ trợ giao thức extension VS Code; manifest có ví dụ browser, browser-only và Electron cùng build monorepo. Phù hợp tạo môi trường phát triển theo miền sản phẩm. |
| Giới hạn | Repo này là nền tảng, bản Theia IDE được ghép ở repo khác. Hỗ trợ giao thức không bảo đảm mọi extension tương thích; giấy phép có phạm vi từng tệp và trademark riêng. |
| Điều kiện tích hợp | Làm ứng dụng mẫu với ngôn ngữ và extension cần thiết; nếu cung cấp qua web, thiết kế xác thực, quyền workspace, cô lập terminal và lưu dữ liệu. Chưa build IDE hoặc kiểm cách ly. |
| Lựa chọn đối chiếu | Code-OSS; [code-server](../08-awesome-lists-learning/README.md#6c58-editor-terminal--dòng-lệnh); Eclipse Che. |

**Phạm vi bằng chứng:** đã clone, đọc trích đoạn tài liệu, giấy phép và các file cấu hình được dẫn dưới đây; chưa chạy mã, build, benchmark hoặc test upstream. `docs-read` không phải kiểm chứng implementation.

**Nguồn tại cùng SHA:** [README.md](https://github.com/eclipse-theia/theia/blob/f5d466aa4652a7b9e99929a3ced8be3087292163/README.md) · [LICENSE-EPL](https://github.com/eclipse-theia/theia/blob/f5d466aa4652a7b9e99929a3ced8be3087292163/LICENSE-EPL) · [LICENSE-GPL-2.0-ONLY-CLASSPATH-EXCEPTION](https://github.com/eclipse-theia/theia/blob/f5d466aa4652a7b9e99929a3ced8be3087292163/LICENSE-GPL-2.0-ONLY-CLASSPATH-EXCEPTION) · [LICENSE-MIT.txt](https://github.com/eclipse-theia/theia/blob/f5d466aa4652a7b9e99929a3ced8be3087292163/LICENSE-MIT.txt) · [package.json](https://github.com/eclipse-theia/theia/blob/f5d466aa4652a7b9e99929a3ced8be3087292163/package.json) · [.github/workflows/ci-cd.yml](https://github.com/eclipse-theia/theia/blob/f5d466aa4652a7b9e99929a3ced8be3087292163/.github/workflows/ci-cd.yml).

<a id="anhkysuai-folke-lazy.nvim"></a>

### lazy.nvim

**Repo:** [folke/lazy.nvim](https://github.com/folke/lazy.nvim) · **License:** Apache-2.0 · **Kiểm:** 2026-11-23, `docs-read`, [`306a05526ada`](https://github.com/folke/lazy.nvim/tree/306a05526ada86a7b30af95c5cc81ffba93fef97) (commit 2025-12-17). **Sao:** 21,766 tại 2026-11-23 theo [GitHub API](https://api.github.com/repos/folke/lazy.nvim).

| Mục | Đánh giá |
|---|---|
| Mục đích | Trình quản lý plugin Neovim với lazy-loading theo sự kiện, lệnh, filetype và phím tắt. |
| Giá trị và cơ chế theo tài liệu | README mô tả partial clone, cache bytecode Lua, thứ tự dependency, profiling và lazy-lock.json. Có giá trị để quản lý cấu hình editor có thể tái tạo trên nhiều máy. |
| Giới hạn | Cần Neovim có LuaJIT và Git hỗ trợ partial clone; LuaRocks liên quan gói rockspec. Workflow đọc chỉ gọi workflow dùng chung; commit snapshot tháng 12/2025, chưa kiểm tiến độ ngoài repo. |
| Điều kiện tích hợp | Lưu lockfile và cấu hình, xem thay đổi plugin trước cập nhật; đo startup và thử event loading trên cấu hình thật, kiểm nguồn plugin vì chúng chạy mã trong môi trường người dùng. |
| Lựa chọn đối chiếu | mini.deps; Paq; vim-plug. |

**Phạm vi bằng chứng:** đã clone, đọc trích đoạn tài liệu, giấy phép và các file cấu hình được dẫn dưới đây; chưa chạy mã, build, benchmark hoặc test upstream. `docs-read` không phải kiểm chứng implementation.

**Nguồn tại cùng SHA:** [README.md](https://github.com/folke/lazy.nvim/blob/306a05526ada86a7b30af95c5cc81ffba93fef97/README.md) · [LICENSE](https://github.com/folke/lazy.nvim/blob/306a05526ada86a7b30af95c5cc81ffba93fef97/LICENSE) · [.github/workflows/ci.yml](https://github.com/folke/lazy.nvim/blob/306a05526ada86a7b30af95c5cc81ffba93fef97/.github/workflows/ci.yml).

<a id="anhkysuai-oracle-graal"></a>

### GraalVM Community Edition

**Đã chuyển (2026-11-23):** hồ sơ này nay nằm ở [mục 37](../37-programming-languages-runtimes/README.md#anhkysuai-oracle-graal); catalog con xem [catalog/](../catalog/README.md).

<a id="anhkysuai-leptos-rs-leptos"></a>

### Leptos

**Repo:** [leptos-rs/leptos](https://github.com/leptos-rs/leptos) · **License:** MIT · **Kiểm:** 2026-11-23, `docs-read`, [`9b311998b685`](https://github.com/leptos-rs/leptos/tree/9b311998b68584bcf486987518b70d43e3aac030) (commit 2026-11-22). **Sao:** 21,570 tại 2026-11-23 theo [GitHub API](https://api.github.com/repos/leptos-rs/leptos).

| Mục | Đánh giá |
|---|---|
| Mục đích | Framework Rust cho web full-stack với reactive signal, component, routing, SSR và hydration. |
| Giá trị và cơ chế theo tài liệu | README mô tả cập nhật DOM theo signal, streaming HTML/data và server function; workspace tách reactive graph, server_fn và tích hợp Actix/Axum. Có thể chia sẻ kiểu và logic giữa server với trình duyệt. |
| Giới hạn | Chưa benchmark hoặc kiểm hydration. Server function vẫn cần xác thực và kiểm quyền; dependency ứng dụng dùng rand/getrandom phải cấu hình backend JavaScript phù hợp khi build WASM theo README. |
| Điều kiện tích hợp | Thử một luồng form có SSR và server function bằng cargo-leptos, khóa toolchain và crate; đo dung lượng WASM, build time và xử lý lỗi mạng trước quyết định dùng rộng. |
| Lựa chọn đối chiếu | Dioxus; Yew; [SvelteKit](../13-dev-stack-devops/README.md#anhkysuai-sveltejs-kit). |

**Phạm vi bằng chứng:** đã clone, đọc trích đoạn tài liệu, giấy phép và các file cấu hình được dẫn dưới đây; chưa chạy mã, build, benchmark hoặc test upstream. `docs-read` không phải kiểm chứng implementation.

**Nguồn tại cùng SHA:** [README.md](https://github.com/leptos-rs/leptos/blob/9b311998b68584bcf486987518b70d43e3aac030/README.md) · [LICENSE](https://github.com/leptos-rs/leptos/blob/9b311998b68584bcf486987518b70d43e3aac030/LICENSE) · [Cargo.toml](https://github.com/leptos-rs/leptos/blob/9b311998b68584bcf486987518b70d43e3aac030/Cargo.toml) · [.github/workflows/ci.yml](https://github.com/leptos-rs/leptos/blob/9b311998b68584bcf486987518b70d43e3aac030/.github/workflows/ci.yml).

<a id="anhkysuai-samber-lo"></a>

### lo

**Repo:** [samber/lo](https://github.com/samber/lo) · **License:** MIT · **Kiểm:** 2026-11-23, `docs-read`, [`6f5a63afb19f`](https://github.com/samber/lo/tree/6f5a63afb19f34755bea97f2b37a0a7f3814f80c) (commit 2026-11-01). **Sao:** 21,453 tại 2026-11-23 theo [GitHub API](https://api.github.com/repos/samber/lo).

| Mục | Đánh giá |
|---|---|
| Mục đích | Bộ helper Go dùng generics cho slice, map, chuỗi, channel và hàm theo phong cách Lodash. |
| Giá trị và cơ chế theo tài liệu | README phân biệt helper đồng bộ trên tập hữu hạn với reactive stream của samber/ro; go.mod đặt Go 1.18, CI có build, test và coverage. Có thể giảm mã lặp trong biến đổi dữ liệu nghiệp vụ. |
| Giới hạn | Một số API trùng slices/maps chuẩn; tính ngắn gọn không tự bảo đảm ít cấp phát hoặc nhanh hơn vòng lặp. Chưa đọc implementation hay benchmark các helper đồng thời. |
| Điều kiện tích hợp | Dùng ở chỗ làm mã dễ hiểu, thống nhất quy ước với thư viện chuẩn; đo cấp phát ở đường nóng, kiểm semantics thứ tự và lỗi trước thay vòng lặp hiện có. |
| Lựa chọn đối chiếu | Go slices/maps; go-funk; samber/ro. |

**Phạm vi bằng chứng:** đã clone, đọc trích đoạn tài liệu, giấy phép và các file cấu hình được dẫn dưới đây; chưa chạy mã, build, benchmark hoặc test upstream. `docs-read` không phải kiểm chứng implementation.

**Nguồn tại cùng SHA:** [README.md](https://github.com/samber/lo/blob/6f5a63afb19f34755bea97f2b37a0a7f3814f80c/README.md) · [LICENSE](https://github.com/samber/lo/blob/6f5a63afb19f34755bea97f2b37a0a7f3814f80c/LICENSE) · [go.mod](https://github.com/samber/lo/blob/6f5a63afb19f34755bea97f2b37a0a7f3814f80c/go.mod) · [.github/workflows/test.yml](https://github.com/samber/lo/blob/6f5a63afb19f34755bea97f2b37a0a7f3814f80c/.github/workflows/test.yml).

<a id="anhkysuai-pmndrs-jotai"></a>

### Jotai

**Repo:** [pmndrs/jotai](https://github.com/pmndrs/jotai) · **License:** MIT · **Kiểm:** 2026-11-23, `docs-read`, [`5fe0e825f967`](https://github.com/pmndrs/jotai/tree/5fe0e825f9674b16162e6952c0a1afea01c1485f) (commit 2026-11-17). **Sao:** 21,337 tại 2026-11-23 theo [GitHub API](https://api.github.com/repos/pmndrs/jotai).

| Mục | Đánh giá |
|---|---|
| Mục đích | Quản lý state React bằng atom nhỏ có thể kết hợp thành trạng thái suy ra. |
| Giá trị và cơ chế theo tài liệu | README minh họa atom, useAtom và derived atom đọc các atom khác; manifest 3.0.2 cùng CI có kiểm kiểu, lint, spec và build. Hữu ích khi chia state theo vùng và dependency dữ liệu. |
| Giới hạn | Con số core 2KB và khả năng mở rộng là mô tả upstream, chưa đo lại. Thiết kế atom và phạm vi store vẫn quyết định vòng đời, persistence và render; chưa thử SSR hoặc chuyển từ phiên bản cũ. |
| Điều kiện tích hợp | Đặt ranh giới store theo ứng dụng/request, chọn atom ổn định và kiểm trạng thái bất đồng bộ; đo render trên luồng thực tế, khóa React/TypeScript và Jotai tương thích. |
| Lựa chọn đối chiếu | Zustand; Redux Toolkit; Valtio. |

**Phạm vi bằng chứng:** đã clone, đọc trích đoạn tài liệu, giấy phép và các file cấu hình được dẫn dưới đây; chưa chạy mã, build, benchmark hoặc test upstream. `docs-read` không phải kiểm chứng implementation.

**Nguồn tại cùng SHA:** [README.md](https://github.com/pmndrs/jotai/blob/5fe0e825f9674b16162e6952c0a1afea01c1485f/README.md) · [LICENSE](https://github.com/pmndrs/jotai/blob/5fe0e825f9674b16162e6952c0a1afea01c1485f/LICENSE) · [package.json](https://github.com/pmndrs/jotai/blob/5fe0e825f9674b16162e6952c0a1afea01c1485f/package.json) · [.github/workflows/test.yml](https://github.com/pmndrs/jotai/blob/5fe0e825f9674b16162e6952c0a1afea01c1485f/.github/workflows/test.yml).

<a id="anhkysuai-sveltejs-kit"></a>

### SvelteKit

**Repo:** [sveltejs/kit](https://github.com/sveltejs/kit) · **License:** MIT · **Kiểm:** 2026-11-23, `docs-read`, [`ccc695efb0e3`](https://github.com/sveltejs/kit/tree/ccc695efb0e3a747b59e28b8ef57a1c765aa0c02) (commit 2026-11-23). **Sao:** 20,926 tại 2026-11-23 theo [GitHub API](https://api.github.com/repos/sveltejs/kit).

| Mục | Đánh giá |
|---|---|
| Mục đích | Framework ứng dụng web trên Svelte, ghép routing, rendering và build theo môi trường triển khai. |
| Giá trị và cơ chế theo tài liệu | Tài liệu giới thiệu mô tả SSR, CSR, prerender, preload và Vite HMR; README liệt kê adapter Node, static, Cloudflare, Netlify và Vercel. CI có lint, kiểm kiểu và test các gói. |
| Giới hạn | Lựa chọn rendering và adapter ảnh hưởng chức năng server và cách host; bản monorepo 0.0.1 không phải phiên bản phát hành kit. Chưa chạy ứng dụng, kiểm adapter hay đo tốc độ. |
| Điều kiện tích hợp | Chọn deployment target trước, tách dữ liệu bí mật phía server, thử route/form và lỗi tải dữ liệu; khóa Svelte/Vite/Kit tương thích, kiểm output build trong môi trường staging. |
| Lựa chọn đối chiếu | Next.js; Nuxt; Astro. |

**Phạm vi bằng chứng:** đã clone, đọc trích đoạn tài liệu, giấy phép và các file cấu hình được dẫn dưới đây; chưa chạy mã, build, benchmark hoặc test upstream. `docs-read` không phải kiểm chứng implementation.

**Nguồn tại cùng SHA:** [README.md](https://github.com/sveltejs/kit/blob/ccc695efb0e3a747b59e28b8ef57a1c765aa0c02/README.md) · [LICENSE](https://github.com/sveltejs/kit/blob/ccc695efb0e3a747b59e28b8ef57a1c765aa0c02/LICENSE) · [package.json](https://github.com/sveltejs/kit/blob/ccc695efb0e3a747b59e28b8ef57a1c765aa0c02/package.json) · [.github/workflows/ci.yml](https://github.com/sveltejs/kit/blob/ccc695efb0e3a747b59e28b8ef57a1c765aa0c02/.github/workflows/ci.yml) · [documentation/docs/10-getting-started/10-introduction.md](https://github.com/sveltejs/kit/blob/ccc695efb0e3a747b59e28b8ef57a1c765aa0c02/documentation/docs/10-getting-started/10-introduction.md).

<a id="anhkysuai-jetbrains-intellij-community"></a>

### IntelliJ Open Source Repository

**Repo:** [JetBrains/intellij-community](https://github.com/JetBrains/intellij-community) · **License:** Apache-2.0 cho mã theo LICENSE.txt; Open-Source Build Terms và license bên thứ ba áp dụng theo bản phân phối · **Kiểm:** 2026-11-23, `docs-read`, [`54d1587fcb6b`](https://github.com/JetBrains/intellij-community/tree/54d1587fcb6bddb0a39e198783b5929cf12a0b92) (commit 2026-11-23). **Sao:** 20,749 tại 2026-11-23 theo [GitHub API](https://api.github.com/repos/JetBrains/intellij-community).

| Mục | Đánh giá |
|---|---|
| Mục đích | Phần mã nguồn mở của IntelliJ Platform, IntelliJ IDEA và PyCharm để nghiên cứu nền tảng IDE hoặc xây công cụ mở rộng. |
| Giá trị và cơ chế theo tài liệu | README hướng dẫn clone, build và chạy IDE; nguồn có cấu hình Bazel, workflow Jewel chạy Gradle check. Hữu ích cho phát triển plugin hoặc hiểu cơ chế IDE lớn. |
| Giới hạn | Nhánh master chuẩn bị bản lớn kế tiếp; chuyển sang Bazel đang dở và một số test chưa chạy qua Bazel. LICENSE gốc là Build Terms v1.3, nêu mã Apache nhưng điều khoản dữ liệu và bản build cần phân biệt. |
| Điều kiện tích hợp | Chọn tag và SDK mục tiêu, kiểm phạm vi plugin/phần thương mại, dependency và license trước phân phối; dựng thử trong môi trường riêng. Chưa build IDE hoặc đánh giá tương thích plugin. |
| Lựa chọn đối chiếu | [Eclipse Theia](../13-dev-stack-devops/README.md#anhkysuai-eclipse-theia-theia); Code-OSS; Apache NetBeans. |

**Phạm vi bằng chứng:** đã clone, đọc trích đoạn tài liệu, giấy phép và các file cấu hình được dẫn dưới đây; chưa chạy mã, build, benchmark hoặc test upstream. `docs-read` không phải kiểm chứng implementation.

**Nguồn tại cùng SHA:** [README.md](https://github.com/JetBrains/intellij-community/blob/54d1587fcb6bddb0a39e198783b5929cf12a0b92/README.md) · [LICENSE.txt](https://github.com/JetBrains/intellij-community/blob/54d1587fcb6bddb0a39e198783b5929cf12a0b92/LICENSE.txt) · [.github/workflows/jewel-checks.yml](https://github.com/JetBrains/intellij-community/blob/54d1587fcb6bddb0a39e198783b5929cf12a0b92/.github/workflows/jewel-checks.yml).

<a id="anhkysuai-krisk-fuse"></a>

### Fuse.js

**Repo:** [krisk/Fuse](https://github.com/krisk/Fuse) · **License:** Apache-2.0 · **Kiểm:** 2026-11-23, `docs-read`, [`bde3799d927b`](https://github.com/krisk/Fuse/tree/bde3799d927baadbf39f68c37fd9fee9b9fae1a1) (commit 2026-11-22). **Sao:** 20,538 tại 2026-11-23 theo [GitHub API](https://api.github.com/repos/krisk/Fuse).

| Mục | Đánh giá |
|---|---|
| Mục đích | Thư viện fuzzy search JavaScript/TypeScript cho dữ liệu nhỏ hoặc vừa ở trình duyệt và Node. |
| Giá trị và cơ chế theo tài liệu | README mô tả tìm nhiều từ, keys theo trường và FuseWorker chia dữ liệu qua Web Worker; có build, typecheck, test và benchmark script. Phù hợp tìm kiếm cục bộ không cần dịch vụ index riêng. |
| Giới hạn | Snapshot 7.6.0-beta.4; worker không hỗ trợ các option chứa hàm như sortFn/getFn. Con số tăng tốc upstream chưa được đo lại, tìm kiếm fuzzy không thay phân quyền dữ liệu hay search phân tán. |
| Điều kiện tích hợp | Khóa phiên bản, chọn trường/trọng số và kiểm truy vấn tiếng Việt trên tập mẫu; đo bộ nhớ, latency và chi phí truyền worker trước tải toàn bộ dữ liệu cho client. |
| Lựa chọn đối chiếu | MiniSearch; FlexSearch; [Meilisearch](../08-awesome-lists-learning/README.md#6c511-giám-sát-csdl--phân-tích). |

**Phạm vi bằng chứng:** đã clone, đọc trích đoạn tài liệu, giấy phép và các file cấu hình được dẫn dưới đây; chưa chạy mã, build, benchmark hoặc test upstream. `docs-read` không phải kiểm chứng implementation.

**Nguồn tại cùng SHA:** [README.md](https://github.com/krisk/Fuse/blob/bde3799d927baadbf39f68c37fd9fee9b9fae1a1/README.md) · [LICENSE](https://github.com/krisk/Fuse/blob/bde3799d927baadbf39f68c37fd9fee9b9fae1a1/LICENSE) · [package.json](https://github.com/krisk/Fuse/blob/bde3799d927baadbf39f68c37fd9fee9b9fae1a1/package.json) · [.github/workflows/nodejs.yml](https://github.com/krisk/Fuse/blob/bde3799d927baadbf39f68c37fd9fee9b9fae1a1/.github/workflows/nodejs.yml).

<a id="anhkysuai-crystal-lang-crystal"></a>

### Crystal

**Đã chuyển (2026-11-23):** hồ sơ này nay nằm ở [mục 37](../37-programming-languages-runtimes/README.md#anhkysuai-crystal-lang-crystal); catalog con xem [catalog/](../catalog/README.md).

<a id="anhkysuai-fastapi-typer"></a>

### Typer

**Repo:** [fastapi/typer](https://github.com/fastapi/typer) · **License:** MIT · **Kiểm:** 2026-11-23, `docs-read`, [`2517edde5a12`](https://github.com/fastapi/typer/tree/2517edde5a1292a712e2f16e600754c52c6f00d9) (commit 2026-11-18). **Sao:** 20,414 tại 2026-11-23 theo [GitHub API](https://api.github.com/repos/fastapi/typer).

| Mục | Đánh giá |
|---|---|
| Mục đích | Thư viện Python tạo CLI từ type hint, hỗ trợ command, subcommand, argument, option và help tự động. |
| Giá trị và cơ chế theo tài liệu | README còn mô tả chương trình typer chạy script như CLI; pyproject yêu cầu Python 3.11+, đóng gói bằng pdm-backend. Workflow có môi trường uv và nhóm dependency kiểm thử. |
| Giới hạn | Type hint giúp mô tả giao diện nhưng không thay kiểm nghiệp vụ hoặc kiểm quyền của lệnh. Chưa kiểm shell completion, thông báo lỗi hay tương thích với các dependency trên nền tảng mục tiêu. |
| Điều kiện tích hợp | Tách logic nghiệp vụ khỏi hàm command, định nghĩa exit code và output dễ dùng trong pipeline; thêm xác nhận thích hợp cho lệnh phá hủy, thử help và lỗi input. |
| Lựa chọn đối chiếu | Click; argparse; Python Fire. |

**Phạm vi bằng chứng:** đã clone, đọc trích đoạn tài liệu, giấy phép và các file cấu hình được dẫn dưới đây; chưa chạy mã, build, benchmark hoặc test upstream. `docs-read` không phải kiểm chứng implementation.

**Nguồn tại cùng SHA:** [README.md](https://github.com/fastapi/typer/blob/2517edde5a1292a712e2f16e600754c52c6f00d9/README.md) · [LICENSE](https://github.com/fastapi/typer/blob/2517edde5a1292a712e2f16e600754c52c6f00d9/LICENSE) · [pyproject.toml](https://github.com/fastapi/typer/blob/2517edde5a1292a712e2f16e600754c52c6f00d9/pyproject.toml) · [.github/workflows/test.yml](https://github.com/fastapi/typer/blob/2517edde5a1292a712e2f16e600754c52c6f00d9/.github/workflows/test.yml).

<a id="anhkysuai-snapkit-snapkit"></a>

### SnapKit

**Repo:** [SnapKit/SnapKit](https://github.com/SnapKit/SnapKit) · **License:** MIT · **Kiểm:** 2026-11-23, `docs-read`, [`250529bec615`](https://github.com/SnapKit/SnapKit/tree/250529bec615066185ff328984855101820fcbee) (commit 2026-07-13). **Sao:** 20,342 tại 2026-11-23 theo [GitHub API](https://api.github.com/repos/SnapKit/SnapKit).

| Mục | Đánh giá |
|---|---|
| Mục đích | DSL Swift để viết ràng buộc Auto Layout cho giao diện iOS, macOS và tvOS. |
| Giá trị và cơ chế theo tài liệu | README có ví dụ tích hợp Swift Package Manager; Package.swift khai báo thư viện thường, thư viện dynamic, test target và PrivacyInfo.xcprivacy. Có thể làm mã constraint ngắn và nhất quán trong UIKit/AppKit. |
| Giới hạn | Snapshot yêu cầu Swift toolchain 6, README nêu Xcode 26+, iOS/tvOS 14 và macOS 12; language mode vẫn Swift 5. Chưa chạy build/test trên nền tảng Apple hoặc kiểm cảnh báo constraint. |
| Điều kiện tích hợp | Khóa release theo deployment target, thử rotation, Dynamic Type và bố cục nội dung dài; thống nhất cách cập nhật constraint, tránh trộn nhiều cơ chế layout trong cùng vùng. |
| Lựa chọn đối chiếu | Auto Layout anchors; TinyConstraints; SwiftUI. |

**Phạm vi bằng chứng:** đã clone, đọc trích đoạn tài liệu, giấy phép và các file cấu hình được dẫn dưới đây; chưa chạy mã, build, benchmark hoặc test upstream. `docs-read` không phải kiểm chứng implementation.

**Nguồn tại cùng SHA:** [README.md](https://github.com/SnapKit/SnapKit/blob/250529bec615066185ff328984855101820fcbee/README.md) · [LICENSE](https://github.com/SnapKit/SnapKit/blob/250529bec615066185ff328984855101820fcbee/LICENSE) · [Package.swift](https://github.com/SnapKit/SnapKit/blob/250529bec615066185ff328984855101820fcbee/Package.swift).

<a id="anhkysuai-11ty-buildawesome"></a>

### Build Awesome (Eleventy)

**Repo:** [11ty/buildawesome](https://github.com/11ty/buildawesome) · **License:** MIT · **Kiểm:** 2026-11-23, `docs-read`, [`7c4465157465`](https://github.com/11ty/buildawesome/tree/7c4465157465ed78a319d1d5ad478dcb0a3726bd) (commit 2026-11-20). **Sao:** 20,055 tại 2026-11-23 theo [GitHub API](https://api.github.com/repos/11ty/buildawesome).

| Mục | Đánh giá |
|---|---|
| Mục đích | Static site generator JavaScript chuyển thư mục template thành HTML, phù hợp trang nội dung và tài liệu. |
| Giá trị và cơ chế theo tài liệu | README hiện gọi Build Awesome (Eleventy), hỗ trợ Markdown, HTML, Liquid, Nunjucks cùng addon; còn gói @11ty/eleventy tương thích tên cũ. Có test Node, browser Vitest và benchmark riêng. |
| Giới hạn | Manifest 4.0.0-alpha.12 yêu cầu Node 22.15+, nên không coi nhánh chính là bản ổn định. Nội dung tĩnh không tự cung cấp API, tài khoản hay dữ liệu động; chưa thử plugin và đường nâng cấp. |
| Điều kiện tích hợp | Khóa bản/tag và tên package, làm build mẫu với permalink, data và template đang dùng; kiểm link, asset, escaping và thời gian build trước đưa pipeline xuất bản vào CI. |
| Lựa chọn đối chiếu | Astro; [Hugo](../08-awesome-lists-learning/README.md#6c59-framework-backend); Jekyll. |

**Phạm vi bằng chứng:** đã clone, đọc trích đoạn tài liệu, giấy phép và các file cấu hình được dẫn dưới đây; chưa chạy mã, build, benchmark hoặc test upstream. `docs-read` không phải kiểm chứng implementation.

**Nguồn tại cùng SHA:** [README.md](https://github.com/11ty/buildawesome/blob/7c4465157465ed78a319d1d5ad478dcb0a3726bd/README.md) · [LICENSE](https://github.com/11ty/buildawesome/blob/7c4465157465ed78a319d1d5ad478dcb0a3726bd/LICENSE) · [package.json](https://github.com/11ty/buildawesome/blob/7c4465157465ed78a319d1d5ad478dcb0a3726bd/package.json) · [.github/workflows/ci.yml](https://github.com/11ty/buildawesome/blob/7c4465157465ed78a319d1d5ad478dcb0a3726bd/.github/workflows/ci.yml).

<a id="anhkysuai-2026-11-23-tw93-mole"></a>

### Mole

**Đã chuyển (2026-11-23):** hồ sơ này nay nằm ở [mục 35](../35-desktop-productivity-apps/README.md#anhkysuai-2026-11-23-tw93-mole); catalog con xem [catalog/](../catalog/README.md).

<a id="anhkysuai-2026-11-23-rclone-rclone"></a>

### rclone

**Repo:** [rclone/rclone](https://github.com/rclone/rclone) · **License:** MIT · **★ 61,198 (GitHub API, 2026-11-23)**

**Mục đích:** Công cụ dòng lệnh đồng bộ, sao chép và phục vụ dữ liệu giữa nhiều hệ lưu trữ.

**Giá trị:** Mô hình backend lưu trữ thống nhất giúp tham khảo việc gom local, object storage và dịch vụ cloud vào một lớp thao tác.

**Giới hạn:** Lệnh sync, quyền truy cập cloud và cấu hình mã hóa cần kiểm riêng; hỗ trợ backend không chứng minh mọi tính năng có cùng ngữ nghĩa.

**Cách tham khảo/tích hợp:** Thử với tập dữ liệu nhỏ, dùng chế độ xem trước khi thao tác ghi/xóa và lưu credential ngoài mã nguồn.

**Lựa chọn để đối chiếu:** [AlistGo/alist](https://github.com/AlistGo/alist) · [restic/restic](https://github.com/restic/restic). Đây là ứng viên so sánh theo tác vụ; mức phù hợp cần kiểm theo hồ sơ và phiên bản riêng.

**Bằng chứng:** `docs-read`, ngày 2026-11-23, commit [`10fcd4e6976315e956ab7cc28ffc8320f9130088`](https://github.com/rclone/rclone/commit/10fcd4e6976315e956ab7cc28ffc8320f9130088), ngày commit 2026-11-23. Đã clone và đọc chọn lọc phần giới thiệu, cách dùng, giới hạn, license, metadata manifest và CI hiện diện. Chưa kiểm đầy đủ implementation hoặc chạy upstream; các số đo của tác giả chưa được tái lập.

**Nguồn:** [README.md](https://github.com/rclone/rclone/blob/10fcd4e6976315e956ab7cc28ffc8320f9130088/README.md) · [COPYING](https://github.com/rclone/rclone/blob/10fcd4e6976315e956ab7cc28ffc8320f9130088/COPYING) · [go.mod](https://github.com/rclone/rclone/blob/10fcd4e6976315e956ab7cc28ffc8320f9130088/go.mod) · [.github/workflows/build.yml](https://github.com/rclone/rclone/blob/10fcd4e6976315e956ab7cc28ffc8320f9130088/.github/workflows/build.yml) · [metadata GitHub](https://api.github.com/repos/rclone/rclone).

<a id="anhkysuai-2026-11-23-alistgo-alist"></a>

### alist

**Đã chuyển (2026-11-23):** hồ sơ này nay nằm ở [mục 35](../35-desktop-productivity-apps/README.md#anhkysuai-2026-11-23-alistgo-alist); catalog con xem [catalog/](../catalog/README.md).

<a id="anhkysuai-2026-11-23-iina-iina"></a>

### iina

**Đã chuyển (2026-11-23):** hồ sơ này nay nằm ở [mục 35](../35-desktop-productivity-apps/README.md#anhkysuai-2026-11-23-iina-iina); catalog con xem [catalog/](../catalog/README.md).

<a id="anhkysuai-2026-11-23-heyputer-puter"></a>

### puter

**Đã chuyển (2026-11-23):** hồ sơ này nay nằm ở [mục 35](../35-desktop-productivity-apps/README.md#anhkysuai-2026-11-23-heyputer-puter); catalog con xem [catalog/](../catalog/README.md).

<a id="anhkysuai-2026-11-23-schollz-croc"></a>

### croc

**Đã chuyển (2026-11-23):** hồ sơ này nay nằm ở [mục 35](../35-desktop-productivity-apps/README.md#anhkysuai-2026-11-23-schollz-croc); catalog con xem [catalog/](../catalog/README.md).

<a id="anhkysuai-2026-11-23-spacedriveapp-spacedrive"></a>

### spacedrive

**Đã chuyển (2026-11-23):** hồ sơ này nay nằm ở [mục 35](../35-desktop-productivity-apps/README.md#anhkysuai-2026-11-23-spacedriveapp-spacedrive); catalog con xem [catalog/](../catalog/README.md).

<a id="anhkysuai-2026-11-23-pbatard-rufus"></a>

### rufus

**Đã chuyển (2026-11-23):** hồ sơ này nay nằm ở [mục 35](../35-desktop-productivity-apps/README.md#anhkysuai-2026-11-23-pbatard-rufus); catalog con xem [catalog/](../catalog/README.md).

<a id="anhkysuai-2026-11-23-permissionlesstech-bitchat"></a>

### bitchat

**Đã chuyển (2026-11-23):** hồ sơ này nay nằm ở [mục 35](../35-desktop-productivity-apps/README.md#anhkysuai-2026-11-23-permissionlesstech-bitchat); catalog con xem [catalog/](../catalog/README.md).

<a id="anhkysuai-2026-11-23-vorssaint-vorssaint-utils"></a>

### vorssaint-utils

**Đã chuyển (2026-11-23):** hồ sơ này nay nằm ở [mục 35](../35-desktop-productivity-apps/README.md#anhkysuai-2026-11-23-vorssaint-vorssaint-utils); catalog con xem [catalog/](../catalog/README.md).

<a id="anhkysuai-2026-11-23-qarmin-czkawka"></a>

### czkawka

**Đã chuyển (2026-11-23):** hồ sơ này nay nằm ở [mục 35](../35-desktop-productivity-apps/README.md#anhkysuai-2026-11-23-qarmin-czkawka); catalog con xem [catalog/](../catalog/README.md).

<a id="anhkysuai-2026-11-23-monitorcontrol-monitorcontrol"></a>

### MonitorControl

**Đã chuyển (2026-11-23):** hồ sơ này nay nằm ở [mục 35](../35-desktop-productivity-apps/README.md#anhkysuai-2026-11-23-monitorcontrol-monitorcontrol); catalog con xem [catalog/](../catalog/README.md).

<a id="anhkysuai-2026-11-23-serenityos-serenity"></a>

### serenity

**Repo:** [SerenityOS/serenity](https://github.com/SerenityOS/serenity) · **License:** BSD-2-Clause · **★ 33,984 (GitHub API, 2026-11-23)**

**Mục đích:** Hệ điều hành đồ họa kiểu Unix với kernel, thư viện và ứng dụng tự phát triển.

**Giá trị:** Nguồn tham khảo kiến trúc nhiều lớp từ hệ thống đến desktop trong cùng cây mã.

**Giới hạn:** Dự án có mục tiêu và môi trường riêng; không suy hỗ trợ ứng dụng Windows/macOS hoặc độ phù hợp production từ giao diện giống desktop quen thuộc.

**Cách tham khảo/tích hợp:** Ghim phiên bản, xác định quyền cần cấp và thử quy trình trong môi trường riêng; kiểm kết quả và đường khôi phục trước dùng với tài nguyên thật.

**Lựa chọn để đối chiếu:** [reactos/reactos](https://github.com/reactos/reactos) · [redox-os/redox](https://github.com/redox-os/redox). Đây là ứng viên so sánh theo tác vụ; mức phù hợp cần kiểm theo hồ sơ và phiên bản riêng.

**Bằng chứng:** `docs-read`, ngày 2026-11-23, commit [`1eb51f9b226d2fa5acd6740b928269d2cc56cb15`](https://github.com/SerenityOS/serenity/commit/1eb51f9b226d2fa5acd6740b928269d2cc56cb15), ngày commit 2026-11-23. Đã clone và đọc chọn lọc phần giới thiệu, cách dùng, giới hạn, license, metadata manifest và CI hiện diện. Chưa kiểm đầy đủ implementation hoặc chạy upstream; các số đo của tác giả chưa được tái lập.

**Nguồn:** [README.md](https://github.com/SerenityOS/serenity/blob/1eb51f9b226d2fa5acd6740b928269d2cc56cb15/README.md) · [LICENSE](https://github.com/SerenityOS/serenity/blob/1eb51f9b226d2fa5acd6740b928269d2cc56cb15/LICENSE) · [CMakeLists.txt](https://github.com/SerenityOS/serenity/blob/1eb51f9b226d2fa5acd6740b928269d2cc56cb15/CMakeLists.txt) · [.github/workflows/ci.yml](https://github.com/SerenityOS/serenity/blob/1eb51f9b226d2fa5acd6740b928269d2cc56cb15/.github/workflows/ci.yml) · [metadata GitHub](https://api.github.com/repos/SerenityOS/serenity).

<a id="anhkysuai-2026-11-23-chubin-wttr.in"></a>

### wttr.in

**Đã chuyển (2026-11-23):** hồ sơ này nay nằm ở [mục 35](../35-desktop-productivity-apps/README.md#anhkysuai-2026-11-23-chubin-wttr.in); catalog con xem [catalog/](../catalog/README.md).

<a id="anhkysuai-2026-11-23-ente-ente"></a>

### ente

**Đã chuyển (2026-11-23):** hồ sơ này nay nằm ở [mục 35](../35-desktop-productivity-apps/README.md#anhkysuai-2026-11-23-ente-ente); catalog con xem [catalog/](../catalog/README.md).

<a id="anhkysuai-2026-11-23-jordanbaird-ice"></a>

### Ice

**Đã chuyển (2026-11-23):** hồ sơ này nay nằm ở [mục 35](../35-desktop-productivity-apps/README.md#anhkysuai-2026-11-23-jordanbaird-ice); catalog con xem [catalog/](../catalog/README.md).

<a id="anhkysuai-2026-11-23-nickemanarin-screentogif"></a>

### ScreenToGif

**Đã chuyển (2026-11-23):** hồ sơ này nay nằm ở [mục 35](../35-desktop-productivity-apps/README.md#anhkysuai-2026-11-23-nickemanarin-screentogif); catalog con xem [catalog/](../catalog/README.md).

<a id="anhkysuai-2026-11-23-gopeedlab-gopeed"></a>

### gopeed

**Đã chuyển (2026-11-23):** hồ sơ này nay nằm ở [mục 35](../35-desktop-productivity-apps/README.md#anhkysuai-2026-11-23-gopeedlab-gopeed); catalog con xem [catalog/](../catalog/README.md).

<a id="anhkysuai-2026-11-23-molunerfinn-picgo"></a>

### PicGo

**Đã chuyển (2026-11-23):** hồ sơ này nay nằm ở [mục 35](../35-desktop-productivity-apps/README.md#anhkysuai-2026-11-23-molunerfinn-picgo); catalog con xem [catalog/](../catalog/README.md).

<a id="anhkysuai-2026-11-23-kovidgoyal-calibre"></a>

### calibre

**Đã chuyển (2026-11-23):** hồ sơ này nay nằm ở [mục 35](../35-desktop-productivity-apps/README.md#anhkysuai-2026-11-23-kovidgoyal-calibre); catalog con xem [catalog/](../catalog/README.md).

<a id="anhkysuai-2026-11-23-aprilnea-openlogi"></a>

### OpenLogi

**Đã chuyển (2026-11-23):** hồ sơ này nay nằm ở [mục 35](../35-desktop-productivity-apps/README.md#anhkysuai-2026-11-23-aprilnea-openlogi); catalog con xem [catalog/](../catalog/README.md).

<a id="anhkysuai-2026-11-23-arendst-tasmota"></a>

### Tasmota

**Đã chuyển (2026-11-23):** hồ sơ này nay nằm ở [mục 36](../36-self-hosting-homelab/README.md#anhkysuai-2026-11-23-arendst-tasmota); catalog con xem [catalog/](../catalog/README.md).

<a id="anhkysuai-2026-11-23-ayangweb-bongocat"></a>

### BongoCat

**Đã chuyển (2026-11-23):** hồ sơ này nay nằm ở [mục 35](../35-desktop-productivity-apps/README.md#anhkysuai-2026-11-23-ayangweb-bongocat); catalog con xem [catalog/](../catalog/README.md).

<a id="anhkysuai-2026-11-23-magicmirrororg-magicmirror"></a>

### MagicMirror

**Đã chuyển (2026-11-23):** hồ sơ này nay nằm ở [mục 35](../35-desktop-productivity-apps/README.md#anhkysuai-2026-11-23-magicmirrororg-magicmirror); catalog con xem [catalog/](../catalog/README.md).

<a id="anhkysuai-2026-11-23-desktop-desktop"></a>

### desktop

**Repo:** [desktop/desktop](https://github.com/desktop/desktop) · **License:** MIT · **★ 22,136 (GitHub API, 2026-11-23)**

**Mục đích:** Mã nguồn GitHub Desktop, ứng dụng Electron/TypeScript cho thao tác Git bằng giao diện.

**Giá trị:** Có giá trị tham khảo cách trình bày thay đổi, commit và quy trình cộng tác cho người dùng không chuyên CLI.

**Giới hạn:** Kênh chính thức, beta và community được tách riêng; quyền MIT không cấp quyền thương hiệu GitHub. Lượt này chưa build hoặc thử thao tác với repo thật.

**Cách tham khảo/tích hợp:** Ghim phiên bản, xác định quyền cần cấp và thử quy trình trong môi trường riêng; kiểm kết quả và đường khôi phục trước dùng với tài nguyên thật.

**Lựa chọn để đối chiếu:** [gitextensions/gitextensions](https://github.com/gitextensions/gitextensions) · [jesseduffield/lazygit](https://github.com/jesseduffield/lazygit). Đây là ứng viên so sánh theo tác vụ; mức phù hợp cần kiểm theo hồ sơ và phiên bản riêng.

**Bằng chứng:** `docs-read`, ngày 2026-11-23, commit [`2970f9ae1ff0fec6d94aff25b7d47165651670c4`](https://github.com/desktop/desktop/commit/2970f9ae1ff0fec6d94aff25b7d47165651670c4), ngày commit 2026-11-20. Đã clone và đọc chọn lọc phần giới thiệu, cách dùng, giới hạn, license, metadata manifest và CI hiện diện. Chưa kiểm đầy đủ implementation hoặc chạy upstream; các số đo của tác giả chưa được tái lập.

**Nguồn:** [README.md](https://github.com/desktop/desktop/blob/2970f9ae1ff0fec6d94aff25b7d47165651670c4/README.md) · [LICENSE](https://github.com/desktop/desktop/blob/2970f9ae1ff0fec6d94aff25b7d47165651670c4/LICENSE) · [package.json](https://github.com/desktop/desktop/blob/2970f9ae1ff0fec6d94aff25b7d47165651670c4/package.json) · [.github/workflows/ci.yml](https://github.com/desktop/desktop/blob/2970f9ae1ff0fec6d94aff25b7d47165651670c4/.github/workflows/ci.yml) · [metadata GitHub](https://api.github.com/repos/desktop/desktop).

<a id="anhkysuai-2026-11-23-android-nowinandroid"></a>

### nowinandroid

**Repo:** [android/nowinandroid](https://github.com/android/nowinandroid) · **License:** Apache-2.0 · **★ 22,120 (GitHub API, 2026-11-23)**

**Mục đích:** Ứng dụng mẫu Android chính thức dùng Kotlin và Jetpack Compose, kèm tài liệu kiến trúc và modularization.

**Giá trị:** Hữu ích học cách tổ chức ứng dụng, test doubles, screenshot test và baseline profile qua một dự án liên kết nhiều phần.

**Giới hạn:** README ghi work in progress; đây là mẫu tham khảo, không nên sao toàn bộ kiến trúc hoặc giả định số đo hiệu năng đã được tái lập cho ứng dụng khác.

**Cách tham khảo/tích hợp:** Đối chiếu phiên bản SDK, kiến trúc module và thiết bị mục tiêu; thử một luồng nhỏ rồi chọn phần phù hợp với ứng dụng riêng.

**Lựa chọn để đối chiếu:** [android/architecture-samples](https://github.com/android/architecture-samples) · [wasabeef/awesome-android-ui](https://github.com/wasabeef/awesome-android-ui). Đây là ứng viên so sánh theo tác vụ; mức phù hợp cần kiểm theo hồ sơ và phiên bản riêng.

**Bằng chứng:** `docs-read`, ngày 2026-11-23, commit [`2982e63cb691ad49cd009aab43dc206fee6699c2`](https://github.com/android/nowinandroid/commit/2982e63cb691ad49cd009aab43dc206fee6699c2), ngày commit 2026-10-20. Đã clone và đọc chọn lọc phần giới thiệu, cách dùng, giới hạn, license, metadata manifest và CI hiện diện. Chưa kiểm đầy đủ implementation hoặc chạy upstream; các số đo của tác giả chưa được tái lập.

**Nguồn:** [README.md](https://github.com/android/nowinandroid/blob/2982e63cb691ad49cd009aab43dc206fee6699c2/README.md) · [LICENSE](https://github.com/android/nowinandroid/blob/2982e63cb691ad49cd009aab43dc206fee6699c2/LICENSE) · [.github/workflows/Build.yaml](https://github.com/android/nowinandroid/blob/2982e63cb691ad49cd009aab43dc206fee6699c2/.github/workflows/Build.yaml) · [metadata GitHub](https://api.github.com/repos/android/nowinandroid).

<a id="anhkysuai-2026-11-23-caldis-mos"></a>

### Mos

**Đã chuyển (2026-11-23):** hồ sơ này nay nằm ở [mục 35](../35-desktop-productivity-apps/README.md#anhkysuai-2026-11-23-caldis-mos); catalog con xem [catalog/](../catalog/README.md).

<a id="anhkysuai-2026-11-23-komi-store-komi-store"></a>

### komi-store

**Đã chuyển (2026-11-23):** hồ sơ này nay nằm ở [mục 35](../35-desktop-productivity-apps/README.md#anhkysuai-2026-11-23-komi-store-komi-store); catalog con xem [catalog/](../catalog/README.md).

<a id="anhkysuai-2026-11-23-imranr98-obtainium"></a>

### Obtainium

**Đã chuyển (2026-11-23):** hồ sơ này nay nằm ở [mục 35](../35-desktop-productivity-apps/README.md#anhkysuai-2026-11-23-imranr98-obtainium); catalog con xem [catalog/](../catalog/README.md).

<a id="anhkysuai-2026-11-23-videolan-vlc"></a>

### vlc

**Đã chuyển (2026-11-23):** hồ sơ này nay nằm ở [mục 35](../35-desktop-productivity-apps/README.md#anhkysuai-2026-11-23-videolan-vlc); catalog con xem [catalog/](../catalog/README.md).

<a id="anhkysuai-2026-11-23-files-community-files"></a>

### Files

**Đã chuyển (2026-11-23):** hồ sơ này nay nằm ở [mục 35](../35-desktop-productivity-apps/README.md#anhkysuai-2026-11-23-files-community-files); catalog con xem [catalog/](../catalog/README.md).

<a id="anhkysuai-2026-11-23-corentinth-it-tools"></a>

### it-tools

**Repo:** [CorentinTh/it-tools](https://github.com/CorentinTh/it-tools) · **License:** GPL-3.0 · **★ 41,337 (GitHub API, 2026-11-23)**

**Mục đích:** Bộ tiện ích web cho lập trình viên và IT, có thể tự host bằng container.

**Giá trị:** Gom công cụ nhỏ vào một giao diện, thuận tiện cho homelab hoặc bộ công cụ nội bộ.

**Giới hạn:** Cần kiểm từng công cụ trước đưa dữ liệu nhạy cảm vì chưa đọc luồng xử lý/network ở lượt này; ví dụ image latest không phải phiên bản cố định và cần quản lý cập nhật riêng.

**Cách tham khảo/tích hợp:** Ghim phiên bản, xác định quyền cần cấp và thử quy trình trong môi trường riêng; kiểm kết quả và đường khôi phục trước dùng với tài nguyên thật.

**Lựa chọn để đối chiếu:** [gchq/CyberChef](https://github.com/gchq/CyberChef) · [tldr-pages/tldr](https://github.com/tldr-pages/tldr). Đây là ứng viên so sánh theo tác vụ; mức phù hợp cần kiểm theo hồ sơ và phiên bản riêng.

**Bằng chứng:** `docs-read`, ngày 2026-11-23, commit [`d505845f918e946ec300af7b36efc107e2f66e9e`](https://github.com/CorentinTh/it-tools/commit/d505845f918e946ec300af7b36efc107e2f66e9e), ngày commit 2026-02-12. Đã clone và đọc chọn lọc phần giới thiệu, cách dùng, giới hạn, license, metadata manifest và CI hiện diện. Chưa kiểm đầy đủ implementation hoặc chạy upstream; các số đo của tác giả chưa được tái lập.

**Nguồn:** [README.md](https://github.com/CorentinTh/it-tools/blob/d505845f918e946ec300af7b36efc107e2f66e9e/README.md) · [LICENSE](https://github.com/CorentinTh/it-tools/blob/d505845f918e946ec300af7b36efc107e2f66e9e/LICENSE) · [package.json](https://github.com/CorentinTh/it-tools/blob/d505845f918e946ec300af7b36efc107e2f66e9e/package.json) · [.github/workflows/ci.yml](https://github.com/CorentinTh/it-tools/blob/d505845f918e946ec300af7b36efc107e2f66e9e/.github/workflows/ci.yml) · [metadata GitHub](https://api.github.com/repos/CorentinTh/it-tools).

<a id="anhkysuai-2026-11-23-sharex-sharex"></a>

### ShareX

**Đã chuyển (2026-11-23):** hồ sơ này nay nằm ở [mục 35](../35-desktop-productivity-apps/README.md#anhkysuai-2026-11-23-sharex-sharex); catalog con xem [catalog/](../catalog/README.md).

<a id="anhkysuai-2026-11-23-koreader-koreader"></a>

### koreader

**Đã chuyển (2026-11-23):** hồ sơ này nay nằm ở [mục 35](../35-desktop-productivity-apps/README.md#anhkysuai-2026-11-23-koreader-koreader); catalog con xem [catalog/](../catalog/README.md).

<a id="anhkysuai-2026-11-23-koodo-reader-koodo-reader"></a>

### koodo-reader

**Đã chuyển (2026-11-23):** hồ sơ này nay nằm ở [mục 35](../35-desktop-productivity-apps/README.md#anhkysuai-2026-11-23-koodo-reader-koodo-reader); catalog con xem [catalog/](../catalog/README.md).

<a id="anhkysuai-2026-11-23-wox-launcher-wox"></a>

### Wox

**Repo:** [Wox-launcher/Wox](https://github.com/Wox-launcher/Wox) · **License:** GPL-3.0 · **★ 27,684 (GitHub API, 2026-11-23)**

**Mục đích:** Launcher đa nền tảng tập trung tìm kiếm cục bộ, thao tác bàn phím và hệ plugin.

**Giá trị:** Một ô nhập cho nhiều tác vụ giúp tham khảo cách tổ chức hành động desktop có thể mở rộng.

**Giới hạn:** Con số khoảng 150 MB trong README chưa được đo lại; plugin có thể truy cập file/chạy lệnh nên cần kiểm nguồn, quyền và tương thích nền tảng trước cài.

**Cách tham khảo/tích hợp:** Đối chiếu phạm vi và giấy phép, thử một ca nhỏ có kết quả mong đợi trước khi nhúng vào dự án.

**Lựa chọn để đối chiếu:** [Flow-Launcher/Flow.Launcher](https://github.com/Flow-Launcher/Flow.Launcher) · [albertlauncher/albert](https://github.com/albertlauncher/albert). Đây là ứng viên so sánh theo tác vụ; mức phù hợp cần kiểm theo hồ sơ và phiên bản riêng.

**Bằng chứng:** `docs-read`, ngày 2026-11-23, commit [`1be19550178004b902d3da525bf16c596df2362c`](https://github.com/Wox-launcher/Wox/commit/1be19550178004b902d3da525bf16c596df2362c), ngày commit 2026-11-18. Đã clone và đọc chọn lọc phần giới thiệu, cách dùng, giới hạn, license, metadata manifest và CI hiện diện. Chưa kiểm đầy đủ implementation hoặc chạy upstream; các số đo của tác giả chưa được tái lập.

**Nguồn:** [README.md](https://github.com/Wox-launcher/Wox/blob/1be19550178004b902d3da525bf16c596df2362c/README.md) · [LICENSE](https://github.com/Wox-launcher/Wox/blob/1be19550178004b902d3da525bf16c596df2362c/LICENSE) · [.github/workflows/build.yml](https://github.com/Wox-launcher/Wox/blob/1be19550178004b902d3da525bf16c596df2362c/.github/workflows/build.yml) · [metadata GitHub](https://api.github.com/repos/Wox-launcher/Wox).

<a id="anhkysuai-2026-11-23-readest-readest"></a>

### readest

**Đã chuyển (2026-11-23):** hồ sơ này nay nằm ở [mục 35](../35-desktop-productivity-apps/README.md#anhkysuai-2026-11-23-readest-readest); catalog con xem [catalog/](../catalog/README.md).

## 7. Nguồn

- Mục 23 (19 repo của chủ kho, đọc 2026-10-12) · https://github.com/alibaba/open-code-review · https://github.com/googleapis/release-please · https://github.com/oxc-project/oxc · https://github.com/webpro-nl/knip · https://github.com/kucherenko/jscpd · https://github.com/astral-sh/uv · https://github.com/astral-sh/ruff
- https://www.solutelabs.com/blog/top-frontend-web-frameworks · https://www.intuz.com/best-frontend-frameworks/ · https://findarepo.com/categories/web-frameworks/ · https://wasp.sh/resources/2026/02/24/best-frameworks-web-dev-2026 · https://github.com/vanodevium/node-framework-stars · https://encore.dev/articles/best-typescript-backend-frameworks · https://www.hirenodejs.com/blog/nodejs-frameworks-compared-2026 · https://rankingdevs.com/best-backend-tools
- https://www.javacodegeeks.com/2026/02/kotlin-multiplatform-vs-flutter-vs-react-native-the-2026-cross-platform-reality.html · https://www.drizz.dev/post/cross-platform-mobile-development · https://mobisoftinfotech.com/resources/blog/cross-platform-app-development-flutter-vs-react-native-vs-native-apps
- https://spacelift.io/blog/gitops-tools · https://www.pulumi.com/blog/best-kubernetes-iac-tools-2026/ · https://www.qovery.com/blog/best-devops-automation-tools · https://oghabi.it/en-us/blog/devops-2026-trends-overview/ · https://medium.com/@h.stoychev87/devops-cloud-platform-tools-by-category-for-2026-68ed92103c17
- https://www.augmentcode.com/tools/best-spec-driven-development-tools · https://reenbit.com/bmad-vs-spec-kit-vs-openspec-choosing-your-spec-driven-ai-framework/ · https://www.fundesk.io/spec-driven-development-github-spec-kit-guide · https://github.com/Anioko/spec-driven-development · https://www.braingrid.ai/blog/spec-driven-development-tools
- https://dupple.com/learn/best-ai-code-review-tools · https://www.morphllm.com/github-ai-code-review · https://www.stork.ai/blog/best-ai-code-review-tools-2026 · https://screencli.sh/blog/best-ai-pr-review-tools-2026 · https://wetheflywheel.com/en/guides/best-ai-code-review-tools-2026/ · https://blog.codercops.com/blog/ai-code-review-tools-compared-2026
- §4c (12/10/2026): https://github.com/astral-sh/uv · https://pydevtools.com/blog/openai-acquires-astral/ · https://github.com/astral-sh/ruff · https://github.com/microsoft/pyright · https://github.com/biomejs/biome · https://github.com/oxc-project/oxc · https://github.com/webpro-nl/knip · https://github.com/kucherenko/jscpd · https://github.com/renovatebot/renovate · https://github.com/pre-commit/pre-commit · https://github.com/googleapis/release-please · https://github.com/reviewdog/reviewdog · https://github.com/stryker-mutator/stryker-js · https://github.com/GoogleChrome/lighthouse-ci · https://github.com/alibaba/open-code-review

<a id="chuyen-muc-2026-11-23"></a>

## Hồ sơ chuyển về từ mục khác — 23/11/2026

36 hồ sơ được chuyển khi chia lại catalog theo `data/taxonomy.json`. Nội dung, ngày kiểm và mức bằng chứng giữ nguyên như ở mục gốc.

<a id="chuyen-linux"></a>

### linux

`torvalds/linux` · License: GPL-2.0 WITH Linux-syscall-note · ★ 256.236 · docs-read · 2026-11-18

Mã nguồn nhân Linux, lõi của mọi hệ điều hành Linux, quản lý phần cứng, tài nguyên hệ thống và cung cấp dịch vụ nền cho phần mềm khác. Phiên bản trong Makefile là 7.4.0-rc3; hỗ trợ 23 mục kiến trúc trong thư mục arch/ và có thư mục rust/; README hướng dẫn theo vai trò kèm tài liệu build, gửi patch, mailing list. Điều kiện: Giấy phép GPL v2 only (copyleft); đóng góp qua patch gửi email/mailing list theo Documentation/process/submitting-patches.rst. ★ 18/11/2026: 256.236 (GitHub search API), nhóm "Container & DevOps" trong kho-repo của Phan Đông Giang, mục 08 §6c.5

**Hồ sơ gốc:** [mục 08](../08-awesome-lists-learning/README.md#6c55-container--devops) (bảng/đoạn chung, giữ nguyên tại chỗ).

<a id="chuyen-vscode"></a>

### vscode

`microsoft/vscode` · License: MIT · ★ 195.711 · docs-read · 2026-11-18

Kho mã nguồn mở "Code - OSS" nơi Microsoft phát triển trình soạn thảo Visual Studio Code cùng cộng đồng. README nêu VS Code cập nhật hằng tháng, chạy trên Windows, macOS và Linux; thư mục extensions chứa các extension tích hợp sẵn (ngữ pháp, snippet nhiều ngôn ngữ); có sẵn dev container và hỗ trợ Codespaces để build. Điều kiện: Bản VS Code do Microsoft phát hành có tuỳ biến riêng và theo giấy phép sản phẩm Microsoft, khác MIT của mã nguồn; build đầy đủ cần ít nhất 4 nhân và 6 GB RAM. ★ 18/11/2026: 195.711 (GitHub search API), nhóm "Editor, Terminal & Dòng lệnh" trong kho-repo của Phan Đông Giang, mục 08 §6c.5

**Hồ sơ gốc:** [mục 08](../08-awesome-lists-learning/README.md#6c58-editor-terminal--dòng-lệnh) (bảng/đoạn chung, giữ nguyên tại chỗ).

<a id="chuyen-ohmyzsh"></a>

### ohmyzsh

`ohmyzsh/ohmyzsh` · License: MIT · ★ 190.765 · docs-read · 2026-11-18

Khung mã nguồn mở do cộng đồng phát triển để quản lý cấu hình zsh, kèm nhiều plugin và theme. Thư mục plugins có hơn 370 mục và themes hơn 140 mục; hỗ trợ Linux, macOS, FreeBSD, Android và Windows qua WSL2; có huy hiệu OpenSSF Best Practices và CI. Điều kiện: Cần zsh (khuyến nghị 5.0.8+), curl hoặc wget và git; Windows chỉ qua WSL2. ★ 18/11/2026: 190.765 (GitHub search API), nhóm "Editor, Terminal & Dòng lệnh" trong kho-repo của Phan Đông Giang, mục 08 §6c.5

**Hồ sơ gốc:** [mục 08](../08-awesome-lists-learning/README.md#6c58-editor-terminal--dòng-lệnh) (bảng/đoạn chung, giữ nguyên tại chỗ).

<a id="chuyen-gitignore"></a>

### gitignore

`github/gitignore` · License: CC0 1.0 Universal · ★ 176.339 · docs-read · 2026-11-18

Bộ sưu tập mẫu .gitignore của GitHub, dùng cho bộ chọn mẫu khi tạo repo trên GitHub.com. Khoảng 317 file .gitignore theo ngôn ngữ, công cụ và hệ điều hành; chia thư mục gốc, Global và community kèm quy tắc phiên bản; phát hành CC0 nên dùng tự do. ★ 18/11/2026: 176.339 (GitHub search API), nhóm "Editor, Terminal & Dòng lệnh" trong kho-repo của Phan Đông Giang, mục 08 §6c.5

**Hồ sơ gốc:** [mục 08](../08-awesome-lists-learning/README.md#6c58-editor-terminal--dòng-lệnh) (bảng/đoạn chung, giữ nguyên tại chỗ).

<a id="chuyen-terminal"></a>

### terminal

`microsoft/terminal` · License: MIT · ★ 105.413 · docs-read · 2026-11-18

Mã nguồn Windows Terminal, Windows Terminal Preview, console host conhost.exe và các thành phần dùng chung. Phát hành qua Microsoft Store, GitHub Releases và winget; repo còn chứa ColorTool và dự án mẫu dùng Windows Console API; có kênh Canary cho bản dựng mới. Điều kiện: Chỉ cho Windows; cần Windows 10 2004 (build 19041) trở lên. ★ 18/11/2026: 105.413 (GitHub search API), nhóm "Editor, Terminal & Dòng lệnh" trong kho-repo của Phan Đông Giang, mục 08 §6c.5

**Hồ sơ gốc:** [mục 08](../08-awesome-lists-learning/README.md#6c58-editor-terminal--dòng-lệnh) (bảng/đoạn chung, giữ nguyên tại chỗ).

<a id="chuyen-neovim"></a>

### neovim

`neovim/neovim` · License: Apache-2.0 · ★ 103.928 · docs-read · 2026-11-18

Neovim là bản tái cấu trúc mạnh của Vim, hướng tới dễ bảo trì, mở rộng và hỗ trợ giao diện nâng cao. API truy cập từ nhiều ngôn ngữ (C, Go, Lua, Python, Rust…) và trình giả lập terminal nhúng; điều khiển job bất đồng bộ; gói dựng sẵn cho Windows, macOS, Linux và có trong Homebrew, Debian, Fedora, Arch…. ★ 18/11/2026: 103.928 (GitHub search API), nhóm "Editor, Terminal & Dòng lệnh" trong kho-repo của Phan Đông Giang, mục 08 §6c.5

**Hồ sơ gốc:** [mục 08](../08-awesome-lists-learning/README.md#6c58-editor-terminal--dòng-lệnh) (bảng/đoạn chung, giữ nguyên tại chỗ).

<a id="chuyen-zed"></a>

### zed

`zed-industries/zed` · License: Chủ yếu GPL-3.0-or-later · ★ 95.238 · docs-read · 2026-11-18

Zed là trình soạn thảo mã hiệu năng cao, hỗ trợ cộng tác nhiều người, từ nhóm tác giả Atom và Tree-sitter. Có bản cho macOS, Linux và Windows; viết bằng Rust (workspace Cargo với thư mục crates); dùng cargo-about để tự động tuân thủ giấy phép phụ thuộc. Điều kiện: Chưa có bản Web; mã chủ yếu GPL-3.0 (copyleft); phát triển bởi công ty vì lợi nhuận Zed Industries. ★ 18/11/2026: 95.238 (GitHub search API), nhóm "Editor, Terminal & Dòng lệnh" trong kho-repo của Phan Đông Giang, mục 08 §6c.5

**Hồ sơ gốc:** [mục 08](../08-awesome-lists-learning/README.md#6c58-editor-terminal--dòng-lệnh) (bảng/đoạn chung, giữ nguyên tại chỗ).

<a id="chuyen-fzf"></a>

### fzf

`junegunn/fzf` · License: MIT · ★ 84.249 · docs-read · 2026-11-18

fzf là công cụ tìm kiếm mờ đa dụng trên dòng lệnh kiêm bộ công cụ dựng giao diện terminal tương tác. Phân phối dạng một file nhị phân duy nhất; tích hợp sẵn cho Bash, Zsh, Fish, Nushell, Vim và Neovim; có phím tắt dòng lệnh và fuzzy completion cho file, PID, host. ★ 18/11/2026: 84.249 (GitHub search API), nhóm "Editor, Terminal & Dòng lệnh" trong kho-repo của Phan Đông Giang, mục 08 §6c.5

**Hồ sơ gốc:** [mục 08](../08-awesome-lists-learning/README.md#6c58-editor-terminal--dòng-lệnh) (bảng/đoạn chung, giữ nguyên tại chỗ).

<a id="chuyen-lazygit"></a>

### lazygit

`jesseduffield/lazygit` · License: MIT · ★ 83.950 · docs-read · 2026-11-18

lazygit là giao diện terminal đơn giản cho các lệnh git. Stage theo hunk hoặc từng dòng, rebase tương tác, cherry-pick, bisect và undo ngay trong TUI; hỗ trợ worktree và đồ thị commit; có gói cho Homebrew, Scoop, Arch, Debian/Ubuntu, NixOS…. Điều kiện: Cần git. ★ 18/11/2026: 83.950 (GitHub search API), nhóm "Editor, Terminal & Dòng lệnh" trong kho-repo của Phan Đông Giang, mục 08 §6c.5

**Hồ sơ gốc:** [mục 08](../08-awesome-lists-learning/README.md#6c58-editor-terminal--dòng-lệnh) (bảng/đoạn chung, giữ nguyên tại chỗ).

<a id="chuyen-firacode"></a>

### FiraCode

`tonsky/FiraCode` · License: SIL Open Font License 1.1 · ★ 82.209 · docs-read · 2026-11-18

Fira Code là phông chữ đơn cách miễn phí có ligature cho các tổ hợp ký tự lập trình phổ biến. Mã nguồn vẫn tương thích ASCII vì ligature chỉ là tính năng hiển thị; có nhiều character variant và stylistic set (cv01, ss01…); có glyph riêng cho thanh tiến trình tại U+EE00 và hỗ trợ vẽ khung, powerline. Điều kiện: Một số trình soạn thảo không hiển thị ligature (danh sách trong README). ★ 18/11/2026: 82.209 (GitHub search API), nhóm "Editor, Terminal & Dòng lệnh" trong kho-repo của Phan Đông Giang, mục 08 §6c.5

**Hồ sơ gốc:** [mục 08](../08-awesome-lists-learning/README.md#6c58-editor-terminal--dòng-lệnh) (bảng/đoạn chung, giữ nguyên tại chỗ).

<a id="chuyen-code-server"></a>

### code-server

`coder/code-server` · License: MIT · ★ 79.900 · docs-read · 2026-11-18

code-server chạy VS Code trên bất kỳ máy nào và truy cập qua trình duyệt. Có script cài đặt dùng trình quản lý gói hệ thống và chế độ --dry-run để xem trước; dùng kho extension Open-VSX; có devcontainer feature và triển khai cho nhóm qua coder/coder. Điều kiện: Cần máy Linux có WebSockets, tối thiểu 1 GB RAM và 2 vCPU; không dùng được Marketplace của Microsoft do điều khoản dịch vụ, thay bằng Open-VSX. ★ 18/11/2026: 79.900 (GitHub search API), nhóm "Editor, Terminal & Dòng lệnh" trong kho-repo của Phan Đông Giang, mục 08 §6c.5

**Hồ sơ gốc:** [mục 08](../08-awesome-lists-learning/README.md#6c58-editor-terminal--dòng-lệnh) (bảng/đoạn chung, giữ nguyên tại chỗ).

<a id="chuyen-tabby"></a>

### tabby

`Eugeny/tabby` · License: MIT · ★ 75.475 · docs-read · 2026-11-18

Trình giả lập terminal cấu hình cao kèm client SSH, Telnet và serial cho Windows, macOS và Linux (trước đây tên Terminus). Tích hợp client SSH2 có trình quản lý kết nối, chuyển tiếp X11/cổng, jump host và kho mã hoá cho bí mật SSH; hỗ trợ PowerShell, WSL, Git-Bash, Cygwin, MSYS2, CMD và chạy portable trên Windows; có hệ plugin/theme cài từ Settings và bản web app tự host được. Điều kiện: README nói rõ không nhẹ (dựa trên Electron), tốn RAM. ★ 18/11/2026: 75.475 (GitHub search API), nhóm "Editor, Terminal & Dòng lệnh" trong kho-repo của Phan Đông Giang, mục 08 §6c.5

**Hồ sơ gốc:** [mục 08](../08-awesome-lists-learning/README.md#6c58-editor-terminal--dòng-lệnh) (bảng/đoạn chung, giữ nguyên tại chỗ).

<a id="chuyen-yazi"></a>

### yazi

`sxyazi/yazi` · License: MIT · ★ 43.468 · docs-read · 2026-11-18

Trình quản lý file trong terminal viết bằng Rust, dựa trên I/O bất đồng bộ, có xem trước ảnh/mã và hệ plugin Lua. Mọi thao tác I/O bất đồng bộ, lập lịch tác vụ có tiến độ và huỷ được; hỗ trợ sẵn nhiều giao thức ảnh (kitty, iTerm2, WezTerm, Sixel…); có plugin Lua đồng thời, trình quản lý gói plugin/theme và VFS cho file từ xa. Điều kiện: README ghi đang ở beta công khai (dùng hằng ngày được), phát triển mạnh và có thể có thay đổi phá vỡ. ★ 18/11/2026: 43.468 (GitHub search API), nhóm "Editor, Terminal & Dòng lệnh" trong kho-repo của Phan Đông Giang, mục 08 §6c.5

**Hồ sơ gốc:** [mục 08](../08-awesome-lists-learning/README.md#6c58-editor-terminal--dòng-lệnh) (bảng/đoạn chung, giữ nguyên tại chỗ).

<a id="chuyen-cli"></a>

### cli

`googleworkspace/cli` · License: Apache-2.0 · ★ 32.371 · docs-read · 2026-11-18

CLI gws dùng chung cho mọi API Google Workspace (Drive, Gmail, Calendar, Sheets…), sinh lệnh động từ Google Discovery Service, xuất JSON cho người và AI agent. Tự nhận endpoint mới vì đọc Discovery Service lúc chạy; có --dry-run, tự phân trang và xuất NDJSON; kèm thư mục skills cho agent (khoảng 95 mục) và thông tin đăng nhập mã hoá AES-256-GCM với khoá trong keyring. Điều kiện: Cần dự án Google Cloud (OAuth) và tài khoản Google Workspace; README ghi không phải sản phẩm Google hỗ trợ chính thức; đang phát triển, có thể có thay đổi phá vỡ trước v1.0; app OAuth chưa xác minh bị giới hạn khoảng 25 scope. ★ 18/11/2026: 32.371 (GitHub search API), nhóm "Editor, Terminal & Dòng lệnh" trong kho-repo của Phan Đông Giang, mục 08 §6c.5

**Hồ sơ gốc:** [mục 08](../08-awesome-lists-learning/README.md#6c58-editor-terminal--dòng-lệnh) (bảng/đoạn chung, giữ nguyên tại chỗ).

<a id="chuyen-tqdm"></a>

### tqdm

`tqdm/tqdm` · License: MPL-2.0 và MIT · ★ 31.390 · docs-read · 2026-11-18

Thư viện Python hiển thị thanh tiến độ thông minh cho vòng lặp và lệnh shell qua pipe. Chỉ cần bọc iterable bằng tqdm(iterable); overhead khoảng 60ns mỗi vòng lặp theo README và có kiểm thử hồi quy hiệu năng; không cần phụ thuộc nào, chạy trên Linux, Windows, Mac, BSD và Jupyter. Điều kiện: Giấy phép kép MPL-2.0/MIT theo file LICENCE. ★ 18/11/2026: 31.390 (GitHub search API), nhóm "Editor, Terminal & Dòng lệnh" trong kho-repo của Phan Đông Giang, mục 08 §6c.5

**Hồ sơ gốc:** [mục 08](../08-awesome-lists-learning/README.md#6c58-editor-terminal--dòng-lệnh) (bảng/đoạn chung, giữ nguyên tại chỗ).

<a id="chuyen-zsh-syntax-highlighting"></a>

### zsh-syntax-highlighting

`zsh-users/zsh-syntax-highlighting` · License: BSD 3-Clause · ★ 23.096 · docs-read · 2026-11-18

Plugin cho zsh tô màu cú pháp dòng lệnh ngay khi gõ ở dấu nhắc, theo kiểu fish, giúp phát hiện lỗi cú pháp trước khi chạy. Có sẵn trong kho gói của nhiều hệ (Arch, Debian, Fedora, FreeBSD, Gentoo, Homebrew, NetBSD, OpenBSD, Ubuntu, Void); kiến trúc nhiều highlighter tách biệt (main, brackets, cursor, line, pattern, regexp, root); thư mục tests riêng trong repo. Điều kiện: Cần zsh 4.3.11+; phải source ở cuối .zshrc; tô sáng khi tìm lịch sử tăng dần cần zsh 5.4+. ★ 18/11/2026: 23.096 (GitHub search API), nhóm "Editor, Terminal & Dòng lệnh" trong kho-repo của Phan Đông Giang, mục 08 §6c.5

**Hồ sơ gốc:** [mục 08](../08-awesome-lists-learning/README.md#6c58-editor-terminal--dòng-lệnh) (bảng/đoạn chung, giữ nguyên tại chỗ).

<a id="chuyen-witr"></a>

### witr

`pranshuparmar/witr` · License: Apache-2.0 · ★ 23.032 · docs-read · 2026-11-18

Công cụ dòng lệnh (kèm TUI) trả lời câu hỏi vì sao một tiến trình, dịch vụ, container hay cổng đang chạy bằng cách truy ngược chuỗi nguồn gốc của PID. Một binary tĩnh cho Linux, macOS, FreeBSD và Windows; có đầu ra --json và exit code phân biệt để dùng với AI agent; phân phối qua nhiều trình quản lý gói (APT Debian/Ubuntu, Homebrew, MacPorts, Conda, AUR, Winget, npm, Chocolatey, Scoop). ★ 18/11/2026: 23.032 (GitHub search API), nhóm "Editor, Terminal & Dòng lệnh" trong kho-repo của Phan Đông Giang, mục 08 §6c.5

**Hồ sơ gốc:** [mục 08](../08-awesome-lists-learning/README.md#6c58-editor-terminal--dòng-lệnh) (bảng/đoạn chung, giữ nguyên tại chỗ).

<a id="chuyen-nnn"></a>

### nnn

`jarun/nnn` · License: BSD 2-Clause · ★ 22.126 · docs-read · 2026-11-18

Trình quản lý file trên terminal rất nhỏ gọn (~150 KiB), gần như không cần cấu hình, có phân tích dung lượng đĩa, đổi tên hàng loạt và chọn file. Thường dùng dưới 3,5 MB bộ nhớ thường trú; chạy trên Linux, macOS, BSD, Haiku, Cygwin, WSL, Termux; kho plugin trong repo có khoảng 60 mục. ★ 18/11/2026: 22.126 (GitHub search API), nhóm "Editor, Terminal & Dòng lệnh" trong kho-repo của Phan Đông Giang, mục 08 §6c.5

**Hồ sơ gốc:** [mục 08](../08-awesome-lists-learning/README.md#6c58-editor-terminal--dòng-lệnh) (bảng/đoạn chung, giữ nguyên tại chỗ).

<a id="chuyen-larksuite-cli"></a>

### larksuite/cli

`larksuite/cli` · License: MIT · ★ 18.144 · docs-read · 2026-11-18

CLI chính thức của Lark/Feishu cho người và AI agent, bao phủ nhắn tin, tài liệu, Base, Sheets, lịch, mail, tác vụ, cuộc họp và nhiều miền khác. Hơn 200 lệnh theo ba tầng (shortcut, lệnh API, API thô); thư mục skills có 25 skill cho agent; lưu thông tin xác thực qua keychain của hệ điều hành. Điều kiện: Cần ứng dụng và quyền trên Lark/Feishu Open Platform cùng Node.js; README cảnh báo rủi ro agent ảo giác và prompt injection khi hành động dưới danh tính người dùng; mặc định gửi tín hiệu kiểm soát rủi ro (loại hệ điều hành, model phần cứng) tới tên miền Lark/Feishu, tắt bằng lark-cli config risk-control off. ★ 18/11/2026: 18.144 (GitHub search API), nhóm "Editor, Terminal & Dòng lệnh" trong kho-repo của Phan Đông Giang, mục 08 §6c.5

**Hồ sơ gốc:** [mục 08](../08-awesome-lists-learning/README.md#6c58-editor-terminal--dòng-lệnh) (bảng/đoạn chung, giữ nguyên tại chỗ).

<a id="chuyen-cz-cli"></a>

### cz-cli

`commitizen/cz-cli` · License: MIT · ★ 17.503 · docs-read · 2026-11-18

Công cụ dòng lệnh nhắc người dùng điền các trường bắt buộc khi commit để thông điệp commit theo quy ước (ví dụ conventional-changelog). Dùng git cz hoặc npx cz thay cho git commit; commitizen init cài adapter và ghi cấu hình vào package.json (npm, yarn, pnpm); hỗ trợ chạy qua git hook với tuỳ chọn --hook. Điều kiện: README nêu được kiểm thử trên Node.js 12, 14, 16 và cần npm 6+. ★ 18/11/2026: 17.503 (GitHub search API), nhóm "Editor, Terminal & Dòng lệnh" trong kho-repo của Phan Đông Giang, mục 08 §6c.5

**Hồ sơ gốc:** [mục 08](../08-awesome-lists-learning/README.md#6c58-editor-terminal--dòng-lệnh) (bảng/đoạn chung, giữ nguyên tại chỗ).

<a id="chuyen-electerm"></a>

### electerm

`electerm/electerm` · License: MIT · ★ 15.656 · docs-read · 2026-11-18

Trình khách terminal/ssh/sftp/ftp/telnet/serialport/RDP/VNC/Spice mã nguồn mở, kiêm trình quản lý tệp, chạy đa nền tảng. Chạy trên Windows 7+, macOS 10.15+, Linux (nhiều kiến trúc gồm riscv64, LoongArch), Android, iOS, HarmonyOS; hỗ trợ tunnel ssh, nhảy kết nối, Zmodem/Trzsz và đồng bộ bookmark qua gist/webdav; tích hợp trợ lý AI và widget MCP. Điều kiện: Trợ lý AI cần API của nhà cung cấp LLM tự cấu hình; đồng bộ dữ liệu cần tài khoản GitHub/Gitee/WebDAV hoặc electerm cloud. ★ 18/11/2026: 15.656 (GitHub search API), nhóm "Editor, Terminal & Dòng lệnh" trong kho-repo của Phan Đông Giang, mục 08 §6c.5

**Hồ sơ gốc:** [mục 08](../08-awesome-lists-learning/README.md#6c58-editor-terminal--dòng-lệnh) (bảng/đoạn chung, giữ nguyên tại chỗ).

<a id="chuyen-bash-it"></a>

### bash-it

`Bash-it/bash-it` · License: MIT · ★ 15.307 · docs-read · 2026-11-18

Khung cấu hình Bash do cộng đồng đóng góp, gom alias, plugin, completion và theme để quản lý shell hằng ngày (tương tự oh-my-zsh cho Bash). Repo có khoảng 81 plugin, 50 bộ alias, 90 completion và 87 theme; có lệnh chẩn đoán bash-it doctor và tìm/bật/tắt thành phần bằng bash-it search; 97% mã tương thích bash 3.2+. Điều kiện: Trình cài sửa ~/.bashrc tại chỗ (có sao lưu); vài plugin cần bash 5. ★ 18/11/2026: 15.307 (GitHub search API), nhóm "Editor, Terminal & Dòng lệnh" trong kho-repo của Phan Đông Giang, mục 08 §6c.5

**Hồ sơ gốc:** [mục 08](../08-awesome-lists-learning/README.md#6c58-editor-terminal--dòng-lệnh) (bảng/đoạn chung, giữ nguyên tại chỗ).

<a id="chuyen-hugo"></a>

### hugo

`gohugoio/hugo` · License: Apache-2.0 · ★ 90.501 · docs-read · 2026-11-18

Trình sinh trang tĩnh viết bằng Go, tối ưu tốc độ, dùng cho blog, trang tài liệu, trang doanh nghiệp. Có pipeline tài nguyên tích hợp: xử lý CSS, Sass, Tailwind, bundle JS/TypeScript, xử lý ảnh; Hugo Modules chia sẻ theme, nội dung qua Git; bản deploy đẩy thẳng lên S3, Google Cloud Storage, Azure. Điều kiện: Build từ nguồn cần Go 1.27.0+ và Git. ★ 18/11/2026: 90.501 (GitHub search API), nhóm "Framework Backend" trong kho-repo của Phan Đông Giang, mục 08 §6c.5

**Hồ sơ gốc:** [mục 08](../08-awesome-lists-learning/README.md#6c59-framework-backend) (bảng/đoạn chung, giữ nguyên tại chỗ).

<a id="chuyen-open-saas"></a>

### open-saas

`wasp-lang/open-saas` · License: MIT · ★ 16.350 · docs-read · 2026-11-18

Mẫu khởi đầu SaaS miễn phí dựng trên Wasp (React, Node.js, Prisma), kèm xác thực, thanh toán, trang quản trị, blog/tài liệu Astro. Tích hợp sẵn Stripe, Polar.sh hoặc Lemon Squeezy, gửi email SendGrid/Mailgun/SMTP, upload AWS S3; có test đầu-cuối Playwright trong template/e2e-tests; triển khai một lệnh lên Railway hoặc Fly.io. Điều kiện: Các tích hợp cần tài khoản/khoá dịch vụ ngoài (Stripe/Polar/Lemon Squeezy, OpenAI, AWS S3, SendGrid/Mailgun, Plausible/Google Analytics); Wasp CLI chạy trên macOS, Linux hoặc Windows qua WSL. ★ 18/11/2026: 16.350 (GitHub search API), nhóm "Framework Frontend" trong kho-repo của Phan Đông Giang, mục 08 §6c.5

**Hồ sơ gốc:** [mục 08](../08-awesome-lists-learning/README.md#6c510-framework-frontend) (bảng/đoạn chung, giữ nguyên tại chỗ).

<a id="chuyen-lodash"></a>

### lodash

`lodash/lodash` · License: MIT · ★ 61.453 · docs-read · 2026-11-18

Thư viện tiện ích JavaScript (v4.18.1) cho thao tác mảng, đối tượng, chuỗi, số và ghép hàm. Có nhiều bản dựng: core khoảng 4 kB gzip, full khoảng 24 kB gzip, bản FP tự curry; nạp từng phương thức riêng (lodash/at) để giảm kích thước bundle; được Sovereign Tech Agency hỗ trợ và chuyển sang giai đoạn Feature-Complete để giữ ổn định, an toàn lâu dài. ★ 18/11/2026: 61.453 (GitHub search API), nhóm "Ngôn ngữ & Runtime" trong kho-repo của Phan Đông Giang, mục 08 §6c.5

**Hồ sơ gốc:** [mục 08](../08-awesome-lists-learning/README.md#6c514-ngôn-ngữ--runtime) (bảng/đoạn chung, giữ nguyên tại chỗ).

<a id="chuyen-turborepo"></a>

### turborepo

`vercel/turborepo` · License: MIT · ★ 31.361 · docs-read · 2026-11-18

Hệ thống build cho monorepo JavaScript/TypeScript, tự giới thiệu là "build system for coding agents", lõi viết bằng Rust. Lõi Rust (Cargo workspace trong crates/) kèm gói npm turbo; có thư mục examples và test codemod; cộng đồng qua GitHub Discussions và kênh báo lỗ hổng bảo mật riêng. ★ 18/11/2026: 31.361 (GitHub search API), nhóm "Ngôn ngữ & Runtime" trong kho-repo của Phan Đông Giang, mục 08 §6c.5

**Hồ sơ gốc:** [mục 08](../08-awesome-lists-learning/README.md#6c514-ngôn-ngữ--runtime) (bảng/đoạn chung, giữ nguyên tại chỗ).

<a id="chuyen-effect"></a>

### effect

`Effect-TS/effect` · License: MIT · ★ 17.596 · docs-read · 2026-11-18

Thư viện TypeScript để xây ứng dụng an toàn kiểu, xử lý lỗi có kiểu, tiêm phụ thuộc, đồng thời có cấu trúc, lập lịch, tracing và schema. Effect 4.x là bản LTS cam kết hỗ trợ ít nhất ba năm; monorepo gồm effect, platform, sql, opentelemetry, ai, vitest; có MIGRATION.md hướng dẫn nâng từ 3.x. Điều kiện: Cần TypeScript 5.9 trở lên với strict bật, Node.js 22.19 trở lên. ★ 18/11/2026: 17.596 (GitHub search API), nhóm "Ngôn ngữ & Runtime" trong kho-repo của Phan Đông Giang, mục 08 §6c.5

**Hồ sơ gốc:** [mục 08](../08-awesome-lists-learning/README.md#6c514-ngôn-ngữ--runtime) (bảng/đoạn chung, giữ nguyên tại chỗ).

<a id="chuyen-type-fest"></a>

### type-fest

`sindresorhus/type-fest` · License: Song giấy phép MIT hoặc CC0-1.0 · ★ 17.540 · docs-read · 2026-11-18

Bộ sưu tập các kiểu tiện ích TypeScript thiết yếu (Except, Primitive, Class...) dùng khi khai báo kiểu. Chỉ chứa kiểu, có thể thêm làm phụ thuộc hoặc chép thẳng mà không cần ghi công; mỗi kiểu có tài liệu và tệp nguồn riêng trong source/; có test kiểu trong test-d. Điều kiện: Cần TypeScript 6 trở lên, ESM, strict và exactOptionalPropertyTypes bật. ★ 18/11/2026: 17.540 (GitHub search API), nhóm "Ngôn ngữ & Runtime" trong kho-repo của Phan Đông Giang, mục 08 §6c.5

**Hồ sơ gốc:** [mục 08](../08-awesome-lists-learning/README.md#6c514-ngôn-ngữ--runtime) (bảng/đoạn chung, giữ nguyên tại chỗ).

<a id="chuyen-ts-pattern"></a>

### ts-pattern

`gvergnaud/ts-pattern` · License: MIT · ★ 15.222 · docs-read · 2026-11-18

Thư viện pattern matching cho TypeScript với suy luận kiểu và kiểm tra đủ trường hợp. Kiểm tra đầy đủ nhánh bằng .exhaustive(); khớp mẫu trên đối tượng lồng, mảng, tuple, Set, Map và kiểu nguyên thủy; bundle nhỏ khoảng 2 kB. ★ 18/11/2026: 15.222 (GitHub search API), nhóm "Ngôn ngữ & Runtime" trong kho-repo của Phan Đông Giang, mục 08 §6c.5

**Hồ sơ gốc:** [mục 08](../08-awesome-lists-learning/README.md#6c514-ngôn-ngữ--runtime) (bảng/đoạn chung, giữ nguyên tại chỗ).

<a id="chuyen-electron"></a>

### electron

`electron/electron` · License: MIT · ★ 123.959 · docs-read · 2026-11-18

Framework viết ứng dụng desktop đa nền tảng bằng JavaScript, HTML và CSS, dựa trên Node.js và Chromium. Cung cấp binary cho macOS, Windows, Linux (x64 và arm64); được dùng bởi Visual Studio Code; có Electron Fiddle để thử nghiệm nhanh. Điều kiện: macOS Ventura trở lên, Windows 10 trở lên. ★ 18/11/2026: 123.959 (GitHub search API), nhóm "Ứng dụng đa nền tảng & Game" trong kho-repo của Phan Đông Giang, mục 08 §6c.5

**Hồ sơ gốc:** [mục 08](../08-awesome-lists-learning/README.md#6c528-ứng-dụng-đa-nền-tảng--game) (bảng/đoạn chung, giữ nguyên tại chỗ).

<a id="chuyen-imgui"></a>

### imgui

`ocornut/imgui` · License: MIT · ★ 77.153 · docs-read · 2026-11-18

Thư viện giao diện người dùng immediate-mode cho C++, gọn nhẹ, sinh vertex buffer để render trong ứng dụng 3D; hợp cho công cụ, debug trong game engine. Lõi tự chứa trong vài file imgui*.cpp/h, không phụ thuộc ngoài, không cần quy trình build riêng; có backend cho DirectX 9-12, OpenGL, Metal, SDL2/3, GLFW, Android, Allegro; kèm ví dụ trong examples/. ★ 18/11/2026: 77.153 (GitHub search API), nhóm "Ứng dụng đa nền tảng & Game" trong kho-repo của Phan Đông Giang, mục 08 §6c.5

**Hồ sơ gốc:** [mục 08](../08-awesome-lists-learning/README.md#6c528-ứng-dụng-đa-nền-tảng--game) (bảng/đoạn chung, giữ nguyên tại chỗ).

<a id="chuyen-pake"></a>

### Pake

`tw93/Pake` · License: GPL-3.0 kèm ngoại lệ Pake Output Exception · ★ 63.759 · docs-read · 2026-11-18

CLI biến bất kỳ trang web nào thành ứng dụng desktop nhẹ bằng một lệnh, dùng Rust Tauri trên WebView hệ thống. Gói cài thường dưới 10 MB vì không kèm Chromium; hỗ trợ macOS, Windows, Linux; có build trực tuyến qua GitHub Actions và gói sẵn cho nhiều trang phổ biến. Điều kiện: Fork hoặc sản phẩm phái sinh không được dùng tên và logo Pake (TRADEMARK.md); ứng dụng desktop đồ hoạ là bản tải riêng từ pake.run. ★ 18/11/2026: 63.759 (GitHub search API), nhóm "Ứng dụng đa nền tảng & Game" trong kho-repo của Phan Đông Giang, mục 08 §6c.5

**Hồ sơ gốc:** [mục 08](../08-awesome-lists-learning/README.md#6c528-ứng-dụng-đa-nền-tảng--game) (bảng/đoạn chung, giữ nguyên tại chỗ).

<a id="anhkysuai-2026-11-23-jsoncrack"></a>

### JSON Crack

**Repo:** [AykutSarac/jsoncrack.com](https://github.com/AykutSarac/jsoncrack.com) · **License:** Apache-2.0 · **★ 44,603 (GitHub API, 2026-11-23)**

**Mục đích:** Trình xem và chỉnh dữ liệu JSON dưới dạng đồ thị hoặc cây tương tác.

**Giá trị và cơ chế:** README mô tả chuyển đổi JSON/YAML/CSV/XML, truy vấn jq/JSONPath và sinh schema; monorepo có các đích web và extension, thuận tiện khảo sát payload phức tạp.

**Giới hạn:** Cam kết xử lý cục bộ mới được đọc trong tài liệu; chưa kiểm mạng hoặc dữ liệu rất lớn. Không xem việc vẽ đúng đồ thị là kiểm chứng ý nghĩa của dữ liệu.

**Cách tham khảo/tích hợp:** Dùng bản tự host cho dữ liệu riêng, giảm payload trước khi mở và đối chiếu schema bằng công cụ độc lập.

**Thay thế:** jsoneditor, [D2](../16-docs-tools/README.md#anhkysuai-2026-11-23-d2), [Mermaid](https://github.com/mermaid-js/mermaid).

**Bằng chứng:** `docs-read`, ngày 2026-11-23, commit [`a46d0d0adb09`](https://github.com/AykutSarac/jsoncrack.com/commit/a46d0d0adb098e12e577a083e87ead7f61f90098). README và các tài liệu/manifest/CI hiện diện, đọc chọn lọc; chưa kiểm implementation. Chưa cài/chạy upstream.

**Nguồn:** [README.md](https://github.com/AykutSarac/jsoncrack.com/blob/a46d0d0adb098e12e577a083e87ead7f61f90098/README.md) · [LICENSE.md](https://github.com/AykutSarac/jsoncrack.com/blob/a46d0d0adb098e12e577a083e87ead7f61f90098/LICENSE.md) · [metadata GitHub](https://api.github.com/repos/AykutSarac/jsoncrack.com).

<a id="anhkysuai-ryanoasis-nerd-fonts"></a>

### Nerd Fonts

- **Repo:** [ryanoasis/nerd-fonts](https://github.com/ryanoasis/nerd-fonts).
- **Mục đích:** Bộ font được vá thêm glyph và công cụ tạo font cho terminal, editor và prompt.
- **Điểm đáng dùng:** LICENSE tách mã patcher MIT khỏi font OFL và các nguồn icon khác; manifest và workflow shellcheck cho thấy đây vừa là bộ tài sản vừa là công cụ xử lý.
- **License:** MIT cho mã gốc; OFL-1.1 và giấy phép riêng cho font/glyph.
- **Giới hạn:** Không thể suy MIT cho mọi font/icon; phải giữ license và tên font dự trữ theo từng nguồn. Đường dẫn nhánh master không được tác giả coi là ổn định.
- **Tích hợp:** Chọn đúng font từ release hoặc gói hệ thống; khi phân phối asset phải kèm điều khoản của font cụ thể.
- **Đối chiếu:** Font Awesome cho icon web; Material Symbols cho glyph UI; font monospace gốc khi không cần icon.
- **Mức kiểm chứng:** `docs-read` — Đọc các phần mô tả và giới hạn trong README, thông báo license, metadata manifest và cấu hình CI khi có; chưa đọc toàn bộ mã triển khai, chưa cài hoặc chạy kiểm thử upstream.
- **Snapshot:** kiểm ngày 2026-11-23; commit `adbd16ab7ca911eaca7ce3b0f2b7994207c7ecae` (2026-10-18T00:03:51+02:00); 65,280 sao theo GitHub API ngày 2026-11-23. Sao không đại diện chất lượng.
- **Bằng chứng:** [readme.md](https://github.com/ryanoasis/nerd-fonts/blob/adbd16ab7ca911eaca7ce3b0f2b7994207c7ecae/readme.md) · [LICENSE](https://github.com/ryanoasis/nerd-fonts/blob/adbd16ab7ca911eaca7ce3b0f2b7994207c7ecae/LICENSE) · [license-audit.md](https://github.com/ryanoasis/nerd-fonts/blob/adbd16ab7ca911eaca7ce3b0f2b7994207c7ecae/license-audit.md) · [package.json](https://github.com/ryanoasis/nerd-fonts/blob/adbd16ab7ca911eaca7ce3b0f2b7994207c7ecae/package.json) · [.github/workflows/shellcheck.yml](https://github.com/ryanoasis/nerd-fonts/blob/adbd16ab7ca911eaca7ce3b0f2b7994207c7ecae/.github/workflows/shellcheck.yml) · [GitHub API](https://api.github.com/repos/ryanoasis/nerd-fonts).

<a id="anhkysuai-mbadolato-iterm2-color-schemes"></a>

### iTerm2 Color Schemes

- **Repo:** [mbadolato/iTerm2-Color-Schemes](https://github.com/mbadolato/iTerm2-Color-Schemes).
- **Mục đích:** Bộ phối màu terminal và các bản chuyển định dạng cho nhiều editor/terminal.
- **Điểm đáng dùng:** README có đầu ra JSONL dùng máy và CI bắt buộc mỗi scheme có mục license; công cụ tạo các bản port từ nguồn chung.
- **License:** MIT cho công cụ; mỗi theme theo licenses.yml.
- **Giới hạn:** Không áp MIT root cho tất cả theme: registry cho phép unknown/nonfree; tương phản màu và font thực tế cần kiểm tra.
- **Tích hợp:** Chọn theme có quyền phân phối rõ, giữ attribution và thử độ đọc được trong light/dark trước khi đóng gói dev theme.
- **Đối chiếu:** Catppuccin cho hệ theme; Dracula cho bộ màu; theme tích hợp terminal cho ít dependency.
- **Mức kiểm chứng:** `docs-read` — Đọc các phần mô tả và giới hạn trong README, thông báo license, metadata manifest và cấu hình CI khi có; chưa đọc toàn bộ mã triển khai, chưa cài hoặc chạy kiểm thử upstream.
- **Snapshot:** kiểm ngày 2026-11-23; commit `c7fd7a806e240e423b16b0ff8549b2bc680990cc` (2026-11-22T19:16:43-07:00); 27,337 sao theo GitHub API ngày 2026-11-23. Sao không đại diện chất lượng.
- **Bằng chứng:** [README.md](https://github.com/mbadolato/iTerm2-Color-Schemes/blob/c7fd7a806e240e423b16b0ff8549b2bc680990cc/README.md) · [LICENSE](https://github.com/mbadolato/iTerm2-Color-Schemes/blob/c7fd7a806e240e423b16b0ff8549b2bc680990cc/LICENSE) · [.github/workflows/check-licenses.yml](https://github.com/mbadolato/iTerm2-Color-Schemes/blob/c7fd7a806e240e423b16b0ff8549b2bc680990cc/.github/workflows/check-licenses.yml) · [GitHub API](https://api.github.com/repos/mbadolato/iTerm2-Color-Schemes).

<a id="anhkysuai-antonmedv-fx"></a>

### fx

**Repo:** [antonmedv/fx](https://github.com/antonmedv/fx) · **License:** MIT · **Kiểm:** 2026-11-23, `docs-read`, [`0cd57fae925d`](https://github.com/antonmedv/fx/tree/0cd57fae925d65f2f488b227d9c141316859e893) (commit 2026-11-20). **Sao:** 20,723 tại 2026-11-23 theo [GitHub API](https://api.github.com/repos/antonmedv/fx).

| Mục | Đánh giá |
|---|---|
| Mục đích | Công cụ terminal để xem và xử lý JSON; repo gồm ứng dụng Go và bản JavaScript không tương tác cho pipeline. |
| Giá trị và cơ chế theo tài liệu | README npm mô tả ghép hàm JavaScript, xử lý luồng từng object, slurp, raw input và edit-in-place. go.mod có Bubble Tea/Goja, CI kiểm Go trên nhiều kiến trúc cùng bản npm. |
| Giới hạn | README gốc rất ngắn; tính năng npm không được suy đồng nhất hoàn toàn với giao diện Go. Biểu thức và .fxrc.js là mã thực thi, save ghi đè dữ liệu; chưa thử bộ xử lý. |
| Điều kiện tích hợp | Khóa bản và chọn đúng binary/package, dùng biểu thức tin cậy, thử trên bản sao JSON và ghi ra tệp mới trước khi dùng save. Giới hạn slurp với dữ liệu lớn. |
| Lựa chọn đối chiếu | jq; Jless; VisiData. |

**Phạm vi bằng chứng:** đã clone, đọc trích đoạn tài liệu, giấy phép và các file cấu hình được dẫn dưới đây; chưa chạy mã, build, benchmark hoặc test upstream. `docs-read` không phải kiểm chứng implementation.

**Nguồn tại cùng SHA:** [README.md](https://github.com/antonmedv/fx/blob/0cd57fae925d65f2f488b227d9c141316859e893/README.md) · [LICENSE](https://github.com/antonmedv/fx/blob/0cd57fae925d65f2f488b227d9c141316859e893/LICENSE) · [go.mod](https://github.com/antonmedv/fx/blob/0cd57fae925d65f2f488b227d9c141316859e893/go.mod) · [.github/workflows/test.yml](https://github.com/antonmedv/fx/blob/0cd57fae925d65f2f488b227d9c141316859e893/.github/workflows/test.yml) · [npm/README.md](https://github.com/antonmedv/fx/blob/0cd57fae925d65f2f488b227d9c141316859e893/npm/README.md).
