# 21 · Autonomous Workflows: từ vòng lặp trong session đến routine chạy không người trực

> Mục này mở ra từ yêu cầu "autonomous workflow" (2026-10-12). Gom bốn tầng thường bị gọi chung một tên: **(a)** vòng lặp tự trị trong một session (Ralph loop, `/loop`), **(b)** harness cho agent chạy nhiều giờ/nhiều context window (hai bài của Anthropic), **(c)** lập lịch & kích hoạt không cần người mở session (Routines, Desktop tasks, GitHub Actions, gh-aw), **(d)** hạ tầng thực thi bền (Temporal, Inngest, DBOS, Restate, LangGraph) và nền tảng automation mã nguồn mở. Kèm lịch sử AutoGPT/BabyAGI, các kiểu hỏng và guardrail. Liên quan: mục 03 (patterns & loops), 05 (n8n/Dify), 13 (GitHub Actions, CI), 12 (bảo mật), 07 (eval).

---

## 0. Tóm tắt 60 giây

- "Autonomous workflow" năm 2026 không còn là một agent chạy vô hạn kiểu AutoGPT 2023, mà là **vòng lặp có ràng buộc** (giới hạn vòng, ngân sách, điều kiện dừng, kiểm chứng đầu-cuối) đặt trong **harness** có bộ nhớ ngoài (progress file, feature list JSON, git) và chạy trên **trigger** (cron, API, sự kiện GitHub).
- Anthropic công bố hai bài harness: **26/11/2025** (initializer agent + coding agent, `claude-progress.txt`, feature list JSON chỉ được sửa trường `passes`, test đầu-cuối bằng Puppeteer) và **24/3/2026** (planner + generator + evaluator, sprint contract, context reset vs compaction). Bài sau tự nhận: khi model mới ra, **nhiều thành phần harness trở nên thừa** (bỏ reset, bỏ sprint với Opus 4.5/4.6).
- Claude Code có ba cách lập lịch chính thức: **Cloud Routines** (chạy trên hạ tầng Anthropic, tối thiểu 1 giờ, không cần máy bật, trigger lịch/API/GitHub), **Desktop scheduled tasks** (máy của bạn, tối thiểu 1 phút), **`/loop`** (trong session, cron 5 trường, jitter, hết hạn sau 7 ngày, tối đa 50 task/session).
- Ở tầng repo, **GitHub Agentic Workflows (gh-aw)** biên dịch markdown + frontmatter thành workflow GitHub Actions `.lock.yml`, agent mặc định read-only và mọi ghi đi qua job `safe-outputs`.
- Ở tầng hạ tầng, bài toán "agent chạy nhiều giờ, chờ người duyệt, không mất trạng thái khi crash" được giải bằng **durable execution**: Temporal (rộng nhất), Restate (một binary), Inngest/Vercel Workflow (durable function cạnh app TypeScript), DBOS (Postgres), LangGraph checkpoint (khi agent đã là graph).
- Kiểu hỏng kinh điển: runaway loop (một tool lỗi bị gọi 400 lần trong 5 phút), chi phí phi mã, drift khỏi mục tiêu, tuyên bố "xong" quá sớm. Guardrail tối thiểu: giới hạn vòng, phát hiện không-tiến-triển, **spend circuit breaker** (cảnh báo 80% / bóp 90% / dừng 100%), cổng người duyệt theo mức rủi ro, kiểm chứng ngoài.

---

## 1. Bốn tầng của một "autonomous workflow"

| Tầng | Câu hỏi nó trả lời | Công cụ tiêu biểu | Mục liên quan |
|---|---|---|---|
| **Loop trong session** | Làm sao để agent không dừng sớm, tự lặp đến khi đạt điều kiện? | Ralph Wiggum loop (Stop hook), `/loop`, `/goal`, `ScheduleWakeup`, Monitor | 03 |
| **Harness dài hạn** | Làm sao giữ trí nhớ & chất lượng qua nhiều context window? | Anthropic harness (initializer/coding agent; planner/generator/evaluator), progress file, feature list JSON, git, browser test | 03, 07 |
| **Trigger & lập lịch** | Ai đánh thức agent khi không có người? | Claude Routines, Desktop tasks, GitHub Actions `schedule`, gh-aw, Channels/webhook | 13 |
| **Thực thi bền (durable)** | Nếu crash lúc giờ thứ 3, hoặc chờ người duyệt 2 ngày thì sao? | Temporal, Restate, Inngest, DBOS, Vercel Workflow, LangGraph checkpointer | 02 |
| **Automation no/low-code** | Không viết code nhưng cần pipeline có AI step? | n8n, Activepieces, Windmill, Kestra, Huginn, Dify | 05 |

Nguyên tắc chung rút ra: **loop** quyết định *khi nào dừng*, **harness** quyết định *nhớ gì và kiểm chứng gì*, **trigger** quyết định *khi nào bắt đầu*, **durable runtime** quyết định *sống sót thế nào*.

---

## 2. Hai bài harness của Anthropic (đọc gốc, 2026-10-12)

### 2.1 "Effective harnesses for long-running agents" (Justin Young, 26/11/2025)

- **Vấn đề:** agent làm việc qua nhiều context window mất trí nhớ giữa các session. Compaction giúp một phần, nhưng ngay cả Opus 4.5 chạy loop với prompt cao cấp ("xây bản clone claude.ai") vẫn ôm quá nhiều việc một lúc, hết context giữa chừng, để lại code dang dở không tài liệu; session sau có khi tuyên bố "xong" quá sớm.
- **Thiết kế:**
  - **Initializer agent** chạy một lần: viết `init.sh` (khởi động dev server), tạo `claude-progress.txt`, commit git đầu tiên.
  - **Coding agent** chạy mọi session sau: làm **một** feature tăng dần, để lại ghi chú có cấu trúc cho session kế.
  - **Feature list JSON** >200 feature đầu-cuối, ban đầu tất cả `failing`; agent **chỉ được sửa trường `passes`**. Chọn JSON thay vì Markdown vì model ít "vô tình viết đè" hơn.
  - **Git** với commit mô tả rõ để revert; **test đầu-cuối bằng trình duyệt** (Puppeteer MCP) như người dùng thật, vì unit test + curl bỏ sót lỗi (hạn chế: agent không thấy alert modal native).
- **Context reset:** mỗi session bắt đầu trắng; agent tự định vị bằng `pwd`, đọc progress file + `git log`, xem feature list, chạy `init.sh` và một smoke test trước khi làm mới. Chính bước này bắt được bug session trước để lại.
- **Kết quả:** định tính (không số liệu): cấu trúc ngăn one-shot và kết thúc sớm; browser test bắt được bug không thấy trong code. Câu hỏi mở: một agent tổng quát vs. nhiều agent chuyên QA; tổng quát hóa ngoài web app.

### 2.2 "Harness design for long-running application development" (Prithvi Rajasekaran, Anthropic Labs, 24/3/2026)

- **Generator–evaluator** (cảm hứng GAN): tách agent sinh và agent chấm. Dễ tinh chỉnh evaluator cho "khó tính" hơn là bắt generator tự phê bình. Với frontend: 4 tiêu chí (chất lượng thiết kế, độc đáo, tay nghề, chức năng), nặng về thiết kế + độc đáo để tránh output chung chung; evaluator dùng Playwright tương tác trang thật; 5–15 vòng, tới 4 giờ.
- **Hệ 3 agent full-stack:** **Planner** nở prompt ngắn thành product spec (deliverable + thiết kế cấp cao, tìm chỗ thêm tính năng AI) → **Generator** xây theo sprint trên React/Vite/FastAPI/SQLite-Postgres, tự đánh giá, dùng git → **Evaluator** bấm qua app như user, test API & DB, đánh trượt sprint dưới ngưỡng cứng. Giao tiếp qua **file**.
- **Sprint contract:** trước mỗi sprint, generator đề xuất sẽ làm gì + cách xác minh; evaluator duyệt tới khi hai bên đồng ý. Cầu nối giữa spec cao cấp và hiện thực kiểm thử được.
- **Reset vs. compaction:** reset = context trắng + handoff có cấu trúc (sạch nhưng thêm phức tạp, token, độ trễ); compaction = tóm tắt tại chỗ (liền mạch nhưng không dọn context). Sonnet 4.5 có "context anxiety" (vội kết thúc) nên reset là bắt buộc.
- **Số liệu:** retro game maker — chạy đơn 20 phút/$9 nhưng runtime game không chạy; harness đầy đủ 6 giờ/$200, chơi được. DAW (harness V2, Opus 4.6) ~3h50/$124,70; QA agent bắt lỗi kéo clip không hoạt động, ghi âm stub.
- **Thay đổi theo model:** Opus 4.5 gần như hết context anxiety → bỏ reset, chạy một session + compaction tự động. Opus 4.6 lập kế hoạch và tự debug tốt hơn → bỏ sprint, evaluator chỉ chấm một lượt cuối. Evaluator chỉ đáng tiền khi task vượt ngưỡng model làm ổn một mình.
- **Bài học:** đọc trace trên task thực tế; tách việc + agent chuyên biệt nơi còn dư địa; **mỗi thành phần harness mã hóa một giả định về điều model chưa làm được** — model mới ra thì phải xét lại, bỏ phần không còn chịu lực, thêm phần mới.

> **Góc nhìn kho:** đây là bằng chứng rõ nhất rằng harness là *tài sản có hạn sử dụng*. Ghi ngày và model vào mỗi harness nội bộ; đặt lịch "xét lại harness" mỗi khi đổi model.

---

## 3. Claude Code: ba cách lập lịch chính thức (docs code.claude.com, đọc 2026-10-12)

| | Cloud **Routines** | **Desktop** scheduled tasks | **`/loop`** (session) |
|---|---|---|---|
| Chạy ở | Cloud do Anthropic quản lý | Máy bạn | Máy bạn |
| Cần máy bật / session mở | Không / Không | Có / Không | Có / Có |
| Bền qua restart | Có | Có | Khôi phục khi `--resume` (trừ ngoại lệ) |
| Truy cập file local | Không (clone mới) | Có | Có |
| MCP | Connector cấu hình theo task | File cấu hình + connector | Kế thừa session |
| Hỏi quyền | Không (tự trị) | Cấu hình theo task | Kế thừa session |
| Khoảng cách tối thiểu | **1 giờ** | 1 phút | 1 phút |

Gợi ý chính thức: Cloud cho việc phải chạy tin cậy không cần máy; Desktop khi cần file/tool local; `/loop` để poll nhanh trong phiên.

### 3.1 `/loop` và cron trong session (chi tiết đáng nhớ)

- Ba chế độ: `/loop 5m <prompt>` (cron cố định), `/loop <prompt>` (Claude tự chọn khoảng 1 phút–1 giờ theo quan sát, in lý do; có thể dùng tool **Monitor** để stream thay vì poll), `/loop` trần (prompt bảo trì mặc định: tiếp việc dở → chăm PR của nhánh: review, CI đỏ, conflict → dọn dẹp; hoặc `loop.md` ở `.claude/loop.md` / `~/.claude/loop.md`, tối đa 25.000 byte, sửa là có hiệu lực vòng sau).
- Có thể lặp một skill: `/loop 20m /review-pr 1234`; chỉ chạy skill mà Claude được phép tự gọi (skill `disable-model-invocation: true`, lệnh built-in, MCP prompt chỉ thành text).
- Tool nền: `CronCreate` / `CronList` / `CronDelete`; cron 5 trường chuẩn vixie (không hỗ trợ `L`, `W`, `?`, tên `MON`); **tối đa 50 task/session**; ID 8 ký tự; giờ địa phương.
- **Jitter** có chủ đích để tránh dồn API: task định kỳ chạy **trễ** tới nửa khoảng cách, tối đa 30 phút (hàng giờ/ngày: trễ 0–30 phút); riêng `*/5 * * * *` chạy **sớm 15 giây** (4m45s) để tận dụng prompt cache 5 phút; one-shot đúng `:00`/`:30` chạy sớm tới 90 giây → muốn đúng giờ thì đặt lệch (`3 9 * * *`).
- **Hết hạn 7 ngày** cho task định kỳ (chạy lần cuối rồi tự xóa) — chặn loop bị quên. Dừng loop tự điều nhịp bằng `Esc` hoặc Claude gọi `ScheduleWakeup stop:true`; nếu một vòng không hẹn lại, hệ thống hẹn dự phòng ~20 phút rồi kết thúc.
- Giới hạn: chỉ bắn khi Claude Code đang chạy và rảnh; không bù lượt bỏ lỡ; background session giữ `/loop` sống không cần terminal; tắt toàn bộ bằng `CLAUDE_CODE_DISABLE_CRON=1`.

### 3.2 Cloud Routines

- Research preview **14/4/2026**. Trigger: lịch (cron), gọi HTTP API, sự kiện GitHub (issue/PR); tạo từ CLI bằng `/schedule` (từ v2.1.225 gắn được GitHub trigger vào routine có sẵn; API trigger/token vẫn chỉ trên web — nguồn thứ cấp).
- Chạy tự trị, không hỏi quyền, clone repo mới mỗi lần; connector cấu hình theo routine. Nguồn thứ cấp nói routine tính vào hạn mức subscription và giới hạn **5/15/25 lượt tự động/ngày** theo gói — **chưa xác minh trên docs**.
- Khác biệt với `/loop`: không kế thừa session, nên prompt phải **tự đủ** (standalone); phù hợp "mỗi sáng triage issue", "mỗi PR mới chạy security review", "webhook từ CI đẩy lỗi vào".

### 3.3 Gắn với Ralph loop (mục 03)

Ralph Wiggum loop giải bài "không cho agent dừng" trong một session (Stop hook nạp lại prompt, promise string + max vòng). `/loop` giải bài "quay lại định kỳ". Routines giải bài "không cần người". Ba thứ xếp chồng được: Routine mỗi giờ → mở session → trong session chạy Ralph loop tới khi test xanh → push → Routine kế kiểm tra CI.

---

## 4. GitHub Agentic Workflows (`githubnext/gh-aw`)

| Thuộc tính | Giá trị (2026-10-12) |
|---|---|
| Định dạng | Markdown + YAML frontmatter (trigger, permissions, tools, engine); thân markdown là nhiệm vụ cho agent |
| Biên dịch | `gh aw compile` → `.lock.yml` chạy như GitHub Actions thường |
| Engine | GitHub Copilot, Claude Code, OpenAI Codex, Google Gemini, Pi |
| An toàn | Job agent **read-only & sandbox mặc định**; mọi ghi lên GitHub đi qua job **`safe-outputs`** (đệm, kiểm tra, áp dụng với quyền hẹp); lời khuyên: xem lại permissions/tools/network/file sinh ra trước khi deploy, vẫn cần người giám sát |
| Use case gợi ý | triage issue, review PR, điều tra CI fail, bảo trì docs, phân tích dependency, báo cáo repo — **bổ sung** chứ không thay CI/CD tất định |
| Số liệu | ~5,4k★, 584 fork, 18.545 commit, MIT; advisory **GHSA-8h78-hpm7-29gg** ảnh hưởng `>=0.83.3,<0.85.4` (đã rút) |
| Tài nguyên | docs theo task, quickstart, workshop `githubnext/gh-aw-workshop` |

**Nhận xét:** gh-aw là hiện thực hóa "prompt-as-workflow" trên CI: cùng ý tưởng với plugin markdown (mục 20) nhưng ở tầng repo và có cơ chế ghi an toàn — một mẫu tốt để tham chiếu khi tự thiết kế agent chạy trên GitHub Actions (quyền tối thiểu + ghi gián tiếp).

---

## 5. Durable execution cho agent chạy lâu

| Nền tảng | Mô hình | Hợp khi | Lưu ý |
|---|---|---|---|
| **Temporal** | Workflow + Activity, worker chạy dài | Cần Signals/Updates/Worker Versioning, đa ngôn ngữ, quy mô lớn | Nền tảng rộng nhất; không hợp serverless (cần worker sống lâu) |
| **Restate** | Durable functions, một binary tự host | Muốn đơn giản vận hành | Mới hơn, hệ sinh thái nhỏ hơn |
| **Inngest** | Durable function qua HTTP endpoint | App TypeScript/serverless | Cloud free 50k execution, Pro từ $99/tháng (nguồn thứ cấp) |
| **Vercel Workflow** | Durable function trong Vercel | Đã ở Vercel/Next.js | Khóa nền tảng |
| **DBOS** | Thư viện + Postgres làm sổ cái | Postgres đã là DB chính | DBOS Pro ~$99/tháng (nguồn thứ cấp) |
| **LangGraph** | Checkpointer theo node của graph | Agent đã là LangGraph graph | Checkpoint async mặc định có thể mất checkpoint mới nhất khi crash cứng → chỉnh sang sync |

- Kết hợp phổ biến: **LangGraph cho suy luận + Temporal cho orchestration** với agent có side effect. Các nguồn so sánh phần lớn do vendor viết (LangChain, Cordum, bài gần Temporal) — đọc có đối chiếu.
- Điểm chung với harness Anthropic: cả hai **ngoại hóa trạng thái** (sổ cái/checkpoint hay progress file + git); khác nhau ở độ "cứng": durable runtime bảo đảm replay chính xác, harness chỉ bảo đảm "đủ để agent định vị lại".

---

## 6. Nền tảng automation mã nguồn mở có AI step

| Dự án | License | ★ (ước lượng, nguồn thứ cấp) | AI/agent |
|---|---|---|---|
| **n8n** (mục 05) | Sustainable Use (source-available, không OSI) | — | AI Agent node, LangChain nodes |
| **Activepieces** | MIT | ~24,7k | Agent-first; ~400 MCP server / 700+ pieces (số khác nhau theo nguồn) |
| **Kestra** | Apache-2.0 | ~28,4k | AI Agents & RAG là task type; có MCP server riêng; YAML declarative |
| **Windmill** | AGPL-3.0 | ~18k | AI sinh script/flow; code-first |
| **Huginn** | MIT | ~49k | "Agent" kiểu Ruby, tiền LLM; vẫn là chuẩn self-host lâu năm |
| Airflow / Prefect | Apache-2.0 | — | Pipeline dữ liệu theo lịch; không agent-native |

---

## 7. Lịch sử: làn sóng AutoGPT 2023 và bài học

| Dự án | Ra đời | Tình trạng 2026 | ★ |
|---|---|---|---|
| **AutoGPT** (Toran Bruce Richards) | 3/2023 | Chuyển thành nền tảng builder agent (block-based) | >187k (nguồn thứ cấp) |
| **BabyAGI** (Yohei Nakajima) | 4/2023 | Bản gốc archive 9/2024; chuyển sang framework "functions" thực nghiệm | — |
| **AgentGPT** | 4/2023 | Dừng phát triển 11/2023, công ty pivot 7/2024; **đã archive** (push cuối 29/4/2025, §10d.1) | ~36k |

- Loop gốc: tạo task → ưu tiên → thực thi, ba vai trò prompt trên GPT-4. Bài học thống nhất: **độ tin cậy là nút thắt** — chạy không giám sát thì drift, lặp cùng subgoal, đốt token, không biết output đúng hay sai; không học qua lần chạy. Hệ quả: production chọn thiết kế **có giám sát + ràng buộc** thay vì tự trị toàn phần, chính là hướng Anthropic harness, Ralph loop có max vòng, và Routines không kế thừa session.
- Khảo sát kiến trúc (arXiv 2404.11584) xếp ReAct, RAISE, Reflexion, AutoGPT+P, LATS cùng nhóm single-agent; thành công phụ thuộc planning + self-correction (mục 03).

---

## 8. Kiểu hỏng và guardrail

**Kiểu hỏng hay gặp (2026):** hallucinated tool call; kế hoạch nhiều bước gãy giữa chừng; prompt injection từ nội dung lấy về; **runaway cost** do loop (ví dụ vendor: tool scrape trả rỗng bị gọi lại 400 lần/5 phút); suy giảm âm thầm khi đổi model; tuyên bố xong sớm (Anthropic 2025).

**Guardrail tối thiểu cho một workflow tự trị:**

1. **Giới hạn vòng** (max iterations) + **phát hiện không tiến triển** (vòng lặp không sinh thông tin mới → thoát).
2. **Ngân sách token/tiền là hard stop**, không phải dashboard: **spend circuit breaker** cảnh báo 80% / bóp 90% / dừng 100% (arXiv 2606.03115, SPOQ); OWASP LLM06 xếp "unbounded consumption" là rủi ro hàng đầu (mục 12).
3. **Cổng người duyệt theo mức rủi ro** thay vì bắt duyệt mọi bước (lãng phí chú ý người review): allow-list tool, hành động phá hủy/đối ngoại phải qua gate (so sánh: `/loop` trần chỉ push/xóa khi transcript đã cho phép; gh-aw ghi qua `safe-outputs`).
4. **Kiểm chứng ngoài**: evaluator riêng, browser test, feature list chỉ đổi `passes` (mục 2), "evidence or it's a FAIL" (mục 09).
5. **Hạn sử dụng**: 7 ngày của `/loop`, tối đa 50 task, sprint contract, ghi model + ngày vào harness.
6. **Observability** (mục 07): trace mỗi vòng, đếm tool call lặp, chi phí theo run.
7. **Tối đa N repair cùng failure** (xboss AI Delivery Loop: 3; projects-template: chuỗi đỏ cùng chữ ký) → chuyển WAITING/BLOCKED, không lặp tiếp.
8. **Side effect đối ngoại đi qua outbox** (Sales-Hunter ADR-0010): ghi intent trước khi gọi, lease + fencing token, `outcome_unknown` → reconcile bằng read-back thay vì retry mù, pause mặc định, cooldown sống qua restart; "đã đăng" chỉ tính khi có receipt đọc lại.
9. **Tài liệu trạng thái phải tươi bằng máy**: CI kiểm SHA ghi trong PROGRESS/STATUS là tổ tiên của HEAD và nhánh nêu tên còn tồn tại (xboss, Sales-Hunter) — chống "nhật ký tự khai".

**Từ repo của chủ kho (mục 23):** projects-template đo **DORA baseline trước khi bật tự trị** và có `maintain-run.sh` + `threat-model-maintain-cron.md` cho cron bảo trì; X-Agents có `keeper` (canary dependency, ví dụ urllib3) và **human gate 24h** cho đề xuất đối ngoại; Anthropic đã bỏ `opusplan` (projects-template ADR-0007) nhưng dhcb/xboss vẫn còn trong `settings.json`; Claude Code có **auto mode** và `STOP_HOOK_BLOCK_CAP`; Codex có **Goals** (mục tiêu dài hạn) — so sánh trong `projects-template/docs/reports/2026-10-12-doi-chieu-vong-lap-coding.md`; bài "C compiler bằng nhiều Claude song song" được đối chiếu như ví dụ tự trị có harness mạnh.

**Giới hạn năng lực (để đặt kỳ vọng):** METR ước độ dài task agent hoàn thành tự trị (50% tin cậy) tăng gấp đôi ~**7 tháng** trong 6 năm; agent gần 100% với task người làm <4 phút nhưng <10% với task >4 giờ (số từ nguồn thứ cấp dẫn METR 2025, có bản cập nhật 5/2026 — kiểm tra metr.org). Lỗi cộng dồn: 95%/bước × 30 bước ≈ 21% chạy sạch (0,95³⁰) — lý do phải chia nhỏ + kiểm chứng từng bước.

---

## 9. Agent tự sửa CI / từ issue ra PR

- Lớp sản phẩm: Claude Code (GitHub Action + Routines + `/loop` prompt bảo trì "chăm PR"), GitHub Copilot coding agent, Devin, Jules (mục 01). Cơ chế chung: trigger sự kiện (CI đỏ, comment review) → agent đọc log → sửa tối thiểu → push → chờ CI lại; cần quy tắc "không skip/disable test để xanh", "không rewrite history nhánh người khác", giới hạn số vòng re-run.
- Dự án cộng đồng tìm được chủ yếu là demo cá nhân (self-healing-ci-agent…), chưa có chuẩn mở; coi là tham khảo mẫu, không phải thư viện production.

---

## 10. Phân tích & khuyến nghị cho kho này

1. **Chọn tầng trước khi chọn tool:** việc trong phiên → `/loop`/Ralph; việc hằng ngày không máy → Routines; việc theo sự kiện repo → gh-aw hoặc GitHub Action; việc có side effect + chờ người nhiều ngày → Temporal/Restate/DBOS.
2. **Mẫu harness tối thiểu** cho project nội bộ: `init.sh` + `progress.md` + `features.json` (chỉ đổi `passes`) + commit nhỏ + smoke test đầu session + evaluator riêng khi task vượt ngưỡng model.
3. **Mọi loop phải có 4 số**: max vòng, ngân sách, timeout, ngày hết hạn. Không có bốn số này thì chưa phải workflow tự trị, mới là demo.
4. **Routine prompt phải tự đủ** và **chỉ đề xuất** với hành động đối ngoại (đồng bộ với skill `call-prep` ở mục 20: scheduled run only proposes).
5. **Xét lại harness khi đổi model** — mỗi guardrail là một giả định về điểm yếu của model cũ.
6. Có thể đóng gói checklist mục 09 + prompt bảo trì `loop.md` thành một plugin (mục 20) để chạy bằng Routine mỗi sáng.
7. **AI Delivery Loop** (xboss) là state machine đáng chuẩn hoá: Frame → Research → Spec → Ready → Build → Verify → PR → Reconcile; 1 vòng = 1 PR; goal file có risk register + iteration log; PR `feat` phải link spec đã "Approved for implementation".

## 10b. Kiểm ảnh: mariagorskikh/open-instinct, agent cá nhân nhắn qua iMessage (ảnh người dùng gửi, 2026-10-13)

> Ảnh là trang repo GitHub: About "Open Instinct: an open-source Instinct. A personal agent you text on iMessage, with its own computer and a trusted network of other agents. Built on Pi, Inkbox, Maritime and Composio.", 293★, 65 fork, 38 commit, 1 tag, 1 issue, 4 PR, MIT; commit gần nhất `638c657` "Merge pull request #12 from tonydzi/fix/blocked-merchants-scan-all-…" (4 ngày trước) có dấu ✕ đỏ. Đã clone toàn bộ repo (HEAD `79a144a` 11/10/2026), đọc README, `SECURITY.md`, `docs/research/INSTINCT.md`, `packages/core/src/policy.ts`, workflow CI, rồi tự build và chạy test.

### 10b.1 Hồ sơ nhanh

| Mục | Thông tin (đọc 13/10/2026) |
|---|---|
| Repo | `mariagorskikh/open-instinct` · ~324★, 68 fork, **MIT** · 61 commit từ 3/10/2026 (tên đầu là "LibreInstinct") tới 11/10/2026 |
| Tác giả | Maria Gorskikh (~36 commit); người đóng góp khác: mahmoudomarus 7, ishanray 5, aadithyan rajesh 4, Anton Dziatkovskii (tonydzi) 3, Thom Bailly 2 |
| Bản gốc được sao | **Instinct** của Spear Street Technology (Noah Shinn): agent cá nhân thương mại qua iMessage, vòng Series C $1B ở định giá $10B ngày 28/9/2026 (Sequoia, Benchmark, Coatue; theo tin tổng hợp từ Reuters/TechCrunch, chưa đọc bài gốc). README tự gọi bản này là "from-scratch, documented clone", không liên quan tới công ty |
| Kiến trúc | Monorepo pnpm/TypeScript, 11 package: `core`, `gateway`, `server`, `inkbox`, `computer`, `network`, `payments`, `context`, `apps`, `ample`, `cli`; 13 skill |
| Các mảnh ghép | **Inkbox** (số điện thoại iMessage/SMS, email, kênh A2A) · **Maritime** (microVM có desktop Linux riêng cho agent) · vòng agent **Pi** (`earendil-works/pi`, ~115k★; dùng `@earendil-works/pi-ai`, `pi-agent-core`, `pi-coding-agent`, `pi-mcp`) · **Composio** (kết nối app) · **Stripe Link** (thẻ dùng một lần khi mua hộ) |
| Model mặc định | `anthropic/claude-fable-5-1`, dự phòng `anthropic/claude-opus-5-5` (đổi được) |

### 10b.2 Kiểm từng ô trong ảnh

| Ô trong ảnh | Kiểm | Ghi chú |
|---|---|---|
| 293★ · 65 fork · 38 commit | ⚠️ cũ | Nay ~324★, 68 fork (shields 13/10/2026), 61 commit. Repo mới 10 ngày tuổi nên số đổi theo ngày |
| "A personal agent you text on iMessage" | ✅ | Kênh nhắn đi qua Inkbox; ngoài iMessage còn SMS, email và A2A |
| "with its own computer" | ✅ | Mỗi agent có một microVM Maritime với desktop Linux, trình duyệt và shell |
| "a trusted network of other agents" | ✅ | Package `network`: agent nói chuyện với agent qua A2A, phân 6 mức tin cậy (owner/partner/family/friend/contact/stranger) |
| "Built on Pi, Inkbox, Maritime and Composio" | ✅ | Khớp dependency trong `package.json` các package |
| MIT | ✅ | `LICENSE` MIT |
| Commit `638c657` có dấu ✕ đỏ | ⚠️ | Lúc chụp, CI của commit đó đỏ. HEAD hiện là PR #24 (`fix/inkbox-tunnel`); trạng thái CI hiện tại (chưa xác minh) |

**Tổng:** 5✅ / 2⚠️ / 0❌. Mô tả trong ảnh đúng. Hai ⚠️ là số cũ và CI đỏ lúc chụp.

### 10b.3 Điều ảnh không nói (đọc mã và tự chạy)

- **Test thật chạy được.** README ghi 837 test. Tự chạy `pnpm install --frozen-lockfile --ignore-scripts && pnpm build && pnpm -r test` ngày 13/10/2026: **877 test, tất cả pass** (core 221, apps 156, inkbox 141, server 94, payments 66, network 65, gateway 63, computer 43, ample 25, context 3). Chưa chạy `pnpm smoke` (cần tài khoản dịch vụ thật).
- **Quyền được chặn bằng mã, không bằng prompt.** `packages/core/src/policy.ts` kiểm từng lời gọi tool qua `beforeToolCall` theo mức tin cậy của người nhắn, ghi `audit.jsonl`; nội dung từ ngoài được bọc nhãn "untrusted"; `net-guard.ts` chặn SSRF tới địa chỉ nội bộ.
- **`SECURITY.md` tự khai giới hạn rõ:** tool `bash` là shell thật trong VM; chống SSRF chưa chặn được DNS rebinding; email đến không kiểm SPF/DKIM nên có thể bị giả người gửi; `merchantName` trong yêu cầu thanh toán không được đối chiếu với danh sách cho phép/chặn; rate limit chỉ nằm trong bộ nhớ; cookie trình duyệt lưu trong VM; phải tin nền tảng host (Maritime, Inkbox).
- **Cấp quyền tiêu tiền và đọc tin nhắn.** Agent có thể mua hộ bằng thẻ Stripe Link dùng một lần và đọc mọi tin nhắn gửi tới số điện thoại của nó. Đây là chỗ cần đặt hạn mức trước khi thử.
- **CI có cổng bí mật:** build/typecheck/test/smoke, bước "No leftover secrets", workflow quét bí mật trên toàn lịch sử, workflow đẩy image lên GHCR.
- **Trùng tên:** `Merit-Systems/OpenInstinct` (~450★) là dự án khác, không liên quan; README của nó cũng ghi rõ điều này.

### 10b.4 So sánh & dùng thế nào

- **Thuộc nhóm agent cá nhân chạy liên tục**, cùng họ với OpenClaw/Hermes Agent (mục 02) và phần personal agent ở mục 19. Khác biệt: kênh chính là tin nhắn điện thoại, agent có máy riêng, và có mạng agent với mức tin cậy.
- **Đáng mượn cho dự án của chủ kho:** (1) mô hình 6 mức tin cậy kiểm ở `beforeToolCall` + audit log, thay cho luật viết trong prompt; (2) bọc nội dung ngoài thành "untrusted" (khớp ADR "nội dung ngoài là dữ liệu" ở mục 23); (3) `SECURITY.md` liệt kê giới hạn đã biết như một sổ nợ.
- **Chưa nên chạy thật với tiền hay dữ liệu thật:** repo mới 10 ngày, một người viết phần lớn, phụ thuộc bốn dịch vụ trả phí bên ngoài, và còn các lỗ tự khai ở email và thanh toán.

**Nguồn §10b:** https://github.com/mariagorskikh/open-instinct (clone đầy đủ, HEAD 79a144a; README, SECURITY.md, docs/research/INSTINCT.md, packages/core/src/policy.ts, packages/*/package.json, .github/workflows/) · https://trendshift.io/repositories/281812 · https://github.com/earendil-works/pi · https://github.com/Merit-Systems/OpenInstinct · https://aiweekly.co/alerts/instinct-raises-1b-series-c-at-10b-for-personal-ai-agent · https://letsdatascience.com/news/instinct-raises-1-billion-series-c-c9d149f6 · https://officechai.com/ai/ai-agent-startup-instinct-is-now-worth-10-billion-with-just-14-employees/ (Series C của Instinct; WebSearch 13/10/2026) · https://agent37.com/docs/agents-api/instinct

## 10c. Kiểm ảnh "Traditional — the line / AI-native — the loop" (ảnh người dùng gửi, 2026-10-16)

> Ảnh hai nửa. Bên trái là sáu khối đen xếp dọc Plan → Design → Build → Test → Deploy → Maintain, chú thích *"Traditional — the line. One slow loop back is a new release cycle."* Bên phải là sáu vòng tròn quanh một tâm cam "Claude", mũi tên khép kín từ Maintain về Plan, chú thích *"AI-native — the loop. Hours, not weeks, with humans above the loop instigating, directing and governing."*

**Nguồn ảnh:** Figure 2 "The line and the loop" trong **The AI-native SDLC playbook** của Anthropic (blog claude.com, 21/8/2026, Louis Claxton, nhóm Applied AI; bài đọc 40 phút; bản PDF 54 trang, tạo 23/9/2026). Ảnh người dùng gửi trùng nội dung và bố cục với ảnh thứ hai của trang blog (bản người dùng là webp thu nhỏ còn 2000×1266) (`assets.claude.com/75c8e050….png`, 2048×1296). Ảnh trên web **không có alt text** nên công cụ đọc trang bỏ qua nó, chỉ tìm được chú thích trong PDF. Đã đọc toàn văn PDF; bài anh em của Jason Clinton (Deputy CISO), *How Anthropic secures its AI-native SDLC* (21/7/2026), dùng để đối chiếu số liệu.

### 10c.1 Kiểm từng ý trong ảnh

| Ý trong ảnh | Kiểm | Ghi chú |
|---|---|---|
| Sáu giai đoạn Plan · Design · Build · Test · Deploy · Maintain | ✅ | Đúng sáu "stage" của playbook; chính playbook gọi chúng là "non-linear" và gợi ý áp dụng theo thứ tự phụ thuộc giữa các play, không nhất thiết đi vòng |
| "Traditional — the line. One slow loop back is a new release cycle" | ⚠️ | Bên trái là waterfall thuần. Agile/Scrum đã là vòng lặp từ lâu; playbook tự thừa nhận "most organizations sit somewhere between the two columns". Luận điểm thật của playbook hẹp hơn và đúng hơn: **nút cổ chai dời khỏi Build** (Figure 1: build co lại còn vài giờ, các bước người làm quanh nó giữ nguyên độ dài) |
| "Hours, not weeks" | ⚠️ | Là **mục tiêu**, không phải kết quả đo. Playbook chỉ đưa chỉ số dẫn ("intent capture" từ chu kỳ nhiều tuần xuống vài giờ, review PR đầu tiên xuống vài phút), không có case study đo cycle time. Số đo thật nằm ở bài của Clinton và chỉ nói về **khối lượng code**: Claude viết ~80% code được merge ở Anthropic, mỗi kỹ sư ship ~8× code/quý so với 2021–2025, tỷ lệ PR có review góp ý thực chất 16% → 54% |
| "Humans above the loop instigating, directing and governing" | ⚠️ | Chữ trong ảnh và câu kết ("Human judgement stays above it") nói "above", nhưng thân bài nói "humans stay **in** the loop" và đặt người vào **cổng**: chấp nhận `intent.md`/`spec.md`, duyệt `plan.md` trước khi viết code (plan mode chặn sửa file), code owner duyệt PR, người cho phép lên production ("the agent may act up to the production gate and cannot pass it"). Chỉ riêng stage 6 là chạy headless "without a person in the path", và cả ở đó người vẫn triage hàng đợi |
| Claude ở tâm vòng, mũi tên Maintain → Plan | ✅ có điều kiện | Mũi tên khép vòng có cơ chế thật: script **tất định** theo dõi production, vượt ngưỡng thì gọi Claude headless, Claude ghi chẩn đoán thành một `intent.md` mới. Nhưng ảnh đặt Claude ở tâm, còn thứ thật sự nối các giai đoạn là **artifact commit vào git**, và ảnh không vẽ nó (xem 10c.2) |

**Tổng:** 2✅ / 3⚠️ / 0❌. Ảnh không sai, nhưng là ảnh minh hoạ cho một bài hướng dẫn, nói mạnh hơn nội dung bài: "hours, not weeks" chưa có số đo, và "above the loop" bỏ qua các cổng người duyệt mà chính bài coi là bắt buộc.

### 10c.2 Cơ chế thật: vòng quay bằng artifact và cổng, không bằng Claude

Câu then chốt của playbook là chú thích hình ngay sau bảng "The shifts": *"Every stage commits an artifact the next stage can read."* (Figure 3 của PDF là đồ thị phụ thuộc giữa các play.) Chuỗi commit vừa là đầu vào của giai đoạn sau vừa là audit trail.

| Giai đoạn | Artifact commit | Cơ chế | Cổng người / máy |
|---|---|---|---|
| Plan | `intent.md` (proto-spec bằng lời người yêu cầu) | Brainstorm với Claude, template tổ chức (có thể là skill) | Product owner chấp nhận |
| Design | `spec.md` cạnh `intent.md` | Skill chuẩn nội bộ (brand, security, compliance, UX); lo ngại được chuyển cho chủ chính sách | Người chấp nhận spec; tech lead cho việc rủi ro cao |
| Build | `plan.md` (duyệt trước khi có code), rồi diff + test | Plan mode mặc định, `CLAUDE.md` dưới một trang, skill, hook build-time (chặn path bảo vệ, chạy formatter/linter), worktree song song (2–3 phiên), subagent; auto mode chỉ cho việc thường lệ (spec chặt, blast radius nhỏ, đã có test) | Engineer duyệt plan |
| Test | Output test, build log, screenshot diff do Claude chạy và dán | Vòng tự kiểm, subagent verifier, eval liên tục trong CI (bắt đầu với 20–50 task thật) | **Hook chặn agent sửa file test trong lúc sửa lỗi** |
| Deploy | PR kèm kết quả review; quyết định phát hành | `REVIEW.md`, Code Review (research preview), `@claude` sửa theo review, managed settings (ví dụ `requiredMinimumVersion: "2.1.193"`), job CI sandbox, deploy/rollback qua MCP | Code owner; hook approval cho production; rollback phải diễn tập ở staging |
| Maintain | `intent.md` sinh từ ngưỡng bị vượt; file bài học; kết quả quét; bản ghi kênh sự cố | `bands.yaml`: baseline 30 ngày, luật Western Electric; **1σ chỉ log, 2σ Claude đọc để chẩn đoán (tool hạn chế), 3σ được đề xuất PR hoặc runbook đã duyệt trước**; quét định kỳ (Claude Security, mặc định hằng tuần); Claude Tag trực on-call trong Slack | Chủ dịch vụ triage; mỗi sự cố thêm một eval |

Ba nguyên tắc của playbook đáng chép nguyên ý:

1. **Skill là kiểm soát dạng khuyên nhủ, hook là lớp tất định phía sau.** Chính sách phải luôn đúng thì cần hook hoặc review pass, không chỉ skill.
2. **Phát hiện phải tất định;** model chỉ vào cuộc khi đã vượt ngưỡng.
3. **Agent đi được tới cổng production nhưng không được qua.**

**Mâu thuẫn nội bộ nhỏ:** ở stage Test, playbook dặn dùng hook chặn agent sửa file test để agent không thể "làm yếu bài kiểm tra của chính đoạn code nó sửa". Nhưng ví dụ ở stage Maintain lại cho agent "quarantines the flaky test" khi tỉ lệ fail CI vượt 3σ, chỉ dựa vào cổng review. Hai chỗ không hẳn trái nhau (quarantine đi qua PR, không nằm trong một task sửa lỗi), nhưng khi áp dụng nên chọn quy tắc chặt: quarantine test cũng phải có người duyệt riêng, giống quy tắc "không skip/disable test để xanh" ở §9.

### 10c.3 Phản biện bên ngoài

Cả hai bài phản biện tìm được đều do công ty **bán đúng phần chúng chỉ ra là thiếu**, nên cần đọc với dè dặt:

- **Waydev** (Alex Circei, 24/8/2026): thiếu tầng **đo lường**. Mỗi play có "How to measure it", nhưng không nói cách gom và liên kết sáu nguồn dữ liệu. `bands.yaml` cần baseline lịch sử mới báo vượt ngưỡng được. Tốc độ review tăng có thể che tỉ lệ thay đổi gây lỗi tăng về sau.
- **Port** (Yonatan Boguslavski, 28/8/2026): playbook "assumes intent exists". Nó không nói tín hiệu (ticket, cảnh báo) thành `intent.md` thế nào, hay xác định service và chủ sở hữu ra sao. Blast radius cũng không đo được chỉ từ repo vì cần bản đồ phụ thuộc hạ tầng.

Nhận xét độc lập: hai điểm này **khớp với thứ playbook tự ghi là điều kiện tiên quyết**. Bằng chứng governance cần git history, PR metadata, transcript và OpenTelemetry; mỗi artifact cần một "source of truth". Phản biện không bác playbook, chỉ nói phần khó nhất nằm ngoài nó.

### 10c.4 Đối chiếu với kho (ba cột)

| Cơ chế trong playbook | Kho đã có, sâu hơn | Kho đã có, nông hơn | Kho chưa có |
|---|---|---|---|
| Chuỗi `intent → spec → plan → diff → PR` | AI Delivery Loop của xboss (§10 mục 7: Frame → Research → Spec → Ready → Build → Verify → PR → Reconcile, PR `feat` phải link spec đã duyệt); Spec Kit/Kiro (mục 13 §5) | | |
| Hook làm cổng, skill chỉ khuyên | Mục 23 (projects-template: "prompt không phải cơ chế bảo mật", fail closed); mục 03 §8b (hook cưỡng bức ~98% so với chỉ dặn ~60%) | | |
| Harness, kiểm chứng ngoài, giới hạn vòng | §2, §8 của mục này | | |
| Đo trước khi bật tự trị | projects-template đo **DORA baseline** (§8) | | |
| Eval liên tục trong CI, mỗi sự cố thêm một eval | | Mục 07 có công cụ eval, chưa có quy ước "sự cố → eval" | |
| Phát hiện tất định theo **ngưỡng σ** (`bands.yaml`, 1σ/2σ/3σ, Western Electric) gọi agent theo bậc quyền | | | ✅ Mới. Khác cron bảo trì (`maintain-run.sh`) ở chỗ agent chỉ được gọi khi có tín hiệu, và quyền tăng theo độ lệch |
| Managed settings cho tổ chức (`requiredMinimumVersion`, chặn production) | | Mục 12, 23 có `settings.json` cấp project | Cấu hình cấp tổ chức (server-managed) chưa ghi |
| Hook chặn sửa file test trong task sửa lỗi | | Quy tắc "không skip/disable test" (§9) mới ở dạng lời dặn | Hook cụ thể |

### 10c.5 Dùng thế nào

- **Trích dẫn ảnh này như minh hoạ, không như bằng chứng.** Muốn nói về năng suất thì dùng số đo của bài Clinton (80% code, 8×, 16% → 54%) và ghi rõ đó là số nội bộ Anthropic, tự báo cáo.
- **Phần đáng lấy nhất là bảng 10c.2,** không phải hình tròn. Với dự án của chủ kho, thêm hai thứ "chưa có": (1) hook chặn sửa `tests/**` khi task là sửa lỗi; (2) một `bands.yaml` nhỏ cho tỉ lệ fail CI, quyền theo bậc (1σ log, 2σ đọc, 3σ chỉ mở PR), chạy bằng Routine (§3.2).
- **Giữ người ở cổng, không chỉ "ở trên".** Thứ tự an toàn là duyệt plan → code owner duyệt PR → người duyệt production, đúng như thân bài playbook, dù hình vẽ gợi ý ít người hơn.
- Một số tính năng playbook dựa vào vẫn chưa ổn định (đọc 16/10/2026): Code Review là research preview; Claude Security và Claude Tag là public beta; Claude Design là beta.

**Nguồn §10c:** https://claude.com/blog/the-ai-native-sdlc-playbook (21/8/2026; HTML + ảnh `assets.claude.com/75c8e050ace91c2b288498fe45384469cfb00aa2.png`) · PDF "AI Native SDLC Playbook_designv2" (54 trang, link từ trang blog, đọc toàn văn) · https://academy.claude.com/courses/ai-native-sdlc-playbook · https://claude.com/blog/how-anthropic-secures-its-ai-native-software-development-lifecycle (Jason Clinton, 21/7/2026) · https://waydev.co/anthropics-ai-native-sdlc-playbook-has-a-missing-layer-measurement/ · https://www.port.io/blog/anthropic-ai-native-sdlc-playbook

## 10d. Nâng cấp 31/10/2026: rà repo lớn, cập nhật trạng thái và 5 repo mới

> **Cách làm.** (1) Đọc lại số sao, license, trạng thái của 18 mục trong catalog mục 21 bằng GitHub API (31/10/2026); nhiều mục trước đây để trống số sao. (2) Chạy 6 truy vấn GitHub search (`ralph loop`, `durable execution`, `workflow orchestration`, `autonomous coding loop` tạo sau 1/10/2025, `agent orchestrator parallel`, `harness agent`), lọc repo đã có trong kho. Chọn **5 repo** phủ ba tầng của §1: loop trong session, harness dài hạn, durable runtime. Clone `--filter=blob:none`, đọc LICENSE, hook, script loop, CI, grep telemetry. **Không cài, không chạy.**

### 10d.1 Thay đổi trạng thái của repo đã có

| Repo | Thay đổi (GitHub API 31/10/2026) | Hệ quả |
|---|---|---|
| `reworkd/AgentGPT` | **Đã archive** (read-only); push cuối 29/4/2025; 36,3k★, GPL-3.0 | §7 đổi "maintenance mode" thành **archive**. Chỉ còn giá trị lịch sử |
| `yoheinakajima/babyagi` | 22,4k★; push cuối **31/1/2026**; GitHub **không nhận file license** (catalog ghi MIT) | Gần 9 tháng đứng yên. Kiểm lại license trước khi chép mã |
| `githubnext/gh-aw` | Repo đã chuyển sang **`github/gh-aw`** (5.545★, MIT, push 31/10/2026) | Link cũ vẫn chuyển hướng; nên trích `github/gh-aw` |
| `temporalio/temporal` | 24,1k★ (catalog trống) | Bổ sung số |
| `restatedev/restate` | 4,6k★; GitHub `NOASSERTION` (catalog ghi BUSL-1.1) | Không phải mã mở OSI; giữ cờ |
| `inngest/inngest` | 6k★; GitHub `NOASSERTION` (server SSPL chuyển Apache sau 3 năm, theo docs, **chưa xác minh** lại) | Giữ ghi chú "Apache-2.0 (server)" kèm cờ kiểm |
| `dbos-inc/dbos-transact-py` | 1,7k★, MIT | Bổ sung số |
| `activepieces/activepieces`, `windmill-labs/windmill` | 25,3k★ và 18,3k★; GitHub `NOASSERTION` (catalog ghi MIT và AGPL-3.0) | Nhiều khả năng do có phần enterprise license riêng (**chưa xác minh** lại); đọc LICENSE trước khi nhúng |
| `Significant-Gravitas/AutoGPT` | 187,8k★; `NOASSERTION` (MIT + Polyform Shield cho platform) | Như §7 |
| `kestra-io/kestra`, `huginn/huginn` | 30,1k★, 50,2k★, vẫn hoạt động | §6 cập nhật số: Kestra ~28,4k → 30,1k, Huginn ~49k → 50,2k |

### 10d.2 Bảng nhanh 5 repo mới

| Repo | Tầng (§1) | ★ · license | Commit cuối | Một dòng | Cờ |
|---|---|---|---|---|---|
| `OthmanAdi/planning-with-files` | Harness + loop | 27,8k · MIT | 30/10/2026 | Lập kế hoạch bằng file (`task_plan.md`, `findings.md`, `progress.md`) + hook giữ plan qua compaction và chặn dừng sớm | Hook chạy trên mọi Read/Grep |
| `snarktank/ralph` | Loop | 22,1k · MIT | 2/2/2026 | Bản Ralph loop gọn nhất: `ralph.sh` + `prd.json` (`passes`) + `progress.txt` | **`--dangerously-skip-permissions`**, đứng yên 9 tháng |
| `wanshuiyin/Auto-claude-code-research-in-sleep` (ARIS) | Harness nghiên cứu | 18,4k · MIT | 1/11/2026 | 91 skill cho vòng nghiên cứu ML chạy qua đêm: review chéo model, thí nghiệm, viết paper | 834/1.300 commit có trailer Claude |
| `conductor-oss/conductor` | Durable runtime | 32,4k · Apache-2.0 | 30/10/2026 | Engine workflow (gốc Netflix, 2016) nay có task LLM, MCP, A2A, `DO_WHILE` cho agent | Cần Java 21; "agentspan" mới từ 7/2026 |
| `triggerdotdev/trigger.dev` | Durable runtime | 16,7k · Apache-2.0 | 31/10/2026 | Task TypeScript dài không timeout, retry, queue, waitpoint chờ người, cron; tự host bằng Docker/K8s | **PostHog ở MCP CLI, không đọc `DO_NOT_TRACK`** |

### 10d.3 Hồ sơ từng repo

- **`planning-with-files`.** 580 commit từ 3/1/2026, 78 tác giả, v3.27.0 (126 tag), 245 commit từ 1/8. Hỗ trợ ~15 host (thư mục `.codex`, `.cursor`, `.gemini`, `.kiro`, `.hermes`, `.pi`…). Phần đáng học nằm trong `scripts/check-complete.sh --gate` (Stop hook): chỉ chặn dừng khi **đủ 5 điều kiện**: plan ở chế độ gated, phase còn `in_progress`, `stop_hook_active` không bật, **số lần chặn dưới trần `PWF_GATE_CAP` (mặc định 20)**, và **ledger có tiến triển từ lần chặn trước** (không tiến triển thì cho dừng). Code còn ghi chú lỗi cũ (#178: glob `*stop_hook_active*true*` từng khớp nhầm). `attest-plan.sh` khoá `task_plan.md` bằng SHA-256; nếu file bị sửa ngoài ý muốn, hook **từ chối nạp plan vào ngữ cảnh** và báo `[PLAN TAMPERED]`. `PLANNING_DISABLED=1` tắt cho phiên CI. 103 file test. "Crash-proof" trong mô tả ⚠️: thực chất là khôi phục bằng `session-catchup.py` đọc lại file, không có bảo đảm giao dịch. Cài: `/plugin marketplace add OthmanAdi/planning-with-files` rồi `/plugin install planning-with-files@planning-with-files`; agent khác: `npx skills add OthmanAdi/planning-with-files --skill planning-with-files -g`.
- **`snarktank/ralph`** (Ryan Carson). Chỉ 20 commit (7/1–2/2/2026), không tag. `ralph.sh` lặp tối đa `MAX_ITERATIONS` (mặc định 10), mỗi vòng mở **tiến trình mới** (context sạch) chạy `amp --dangerously-allow-all` hoặc `claude --dangerously-skip-permissions --print`; agent chọn story ưu tiên cao nhất có `passes: false` trong `prd.json`, chạy check, commit, ghi `progress.txt`. Dừng khi output có `<promise>COMPLETE</promise>`. Bẫy: chuỗi này cũng có trong chính `CLAUDE.md`/`prompt.md`, và script grep **toàn bộ output** nên agent chỉ cần trích lại hướng dẫn là loop dừng sai; lỗi từng vòng bị nuốt (`|| true`). Hợp làm ví dụ dạy, không hợp chạy trên máy có dữ liệu thật. Bản Claude Code dài hơi hơn đã có ở mục 03 (`frankbria/ralph-claude-code`).
- **ARIS.** 1.300 commit từ 10/3/2026, 116 tác giả, 197 `SKILL.md` (91 skill chính + bản Codex). Mô tả "Markdown-only skills" ⚠️: repo có 11 MCP server (`codex-exec`, `gemini-review`, `claude-review`…), ~50 tool Python (watchdog GPU, hàng đợi thí nghiệm, kiểm trích dẫn). `auto-review-loop`: **`MAX_ROUNDS = 4`**, dừng khi reviewer ở model khác cho **điểm ≥ 6/10 và** verdict `ready`/`almost`; trạng thái lưu file để khôi phục; skill **tự dặn không bọc trong `/loop` hay cron** vì sẽ mất bộ nhớ reviewer và tốn token vô ích. `tools/threat_scan.py` là lớp quét prompt-injection bằng regex, fail-closed, lấy mẫu từ Hermes Agent (MIT, có ghi công). CLI riêng ARIS-Code (Rust, MIT) nằm ở nhánh `aris-code`. Cài: `claude plugin marketplace add wanshuiyin/Auto-claude-code-research-in-sleep` rồi `claude plugin install aris@aris` và `/aris:setup`.
- **`conductor-oss/conductor`.** 6.119 commit từ 7/12/2016, 464 tác giả, v3.34.0-rc1; Orkes giữ nhịp chính (Netflix ngừng bản gốc cuối 2023, **chưa xác minh** ngày). Module `ai/` (từ 2/2026) thêm task `LLM_CHAT_COMPLETE`, `LIST_MCP_TOOLS`, `CALL_MCP_TOOL`, A2A, vector DB; `SWITCH` có `evaluatorType: decision` gọi model để chọn nhánh. Ví dụ agent trong README dùng `DO_WHILE` với điều kiện **`iteration < 10`**: trần vòng nằm trong định nghĩa workflow ✅ đúng guardrail §8. Có ví dụ human-in-loop và cancel. "Chạy trong 60 giây" cần Node + Java 21, CLI tải JAR server về `~/.conductor-cli/`. Telemetry server **chưa kiểm**. Cài: `npm install -g @conductor-oss/conductor-cli` rồi `conductor server start`.
- **`triggerdotdev/trigger.dev`.** 8.610 commit từ 30/11/2022, 167 tác giả, 896 commit từ 1/8. SDK v3 có nhóm module mới cho agent: `chat.ts` (từ 5/2026), `skills.ts`, `subAgentStream.ts`, `steeringContext.ts`, `compactionResponse.ts`, cùng `wait`/waitpoint token cho người duyệt, `schedules` (cron), `idempotencyKeys`, `concurrencyLimits`. LICENSE Apache-2.0 ở gốc và từng package ✅. Tự host: `hosting/docker`, `hosting/k8s`. Telemetry: MCP server trong CLI gửi PostHog (phản hồi người dùng); tắt bằng `--skip-telemetry` hoặc `TRIGGER_TELEMETRY_DISABLED`, **không đọc `DO_NOT_TRACK`** ⚠️. Mặc định SDK kết nối cloud của Trigger.dev. Cài (theo `docs/snippets/step-cli-init.mdx`): `npx trigger.dev@latest init` (nên ghim phiên bản thay `@latest`).

### 10d.4 Vị trí trong bản đồ §1 và §5

| Tầng | Thêm vào | So với đã có |
|---|---|---|
| Loop trong session | `snarktank/ralph`, Stop gate của planning-with-files | Ralph cũ (mục 03) dùng Stop hook; bản snarktank dùng tiến trình mới mỗi vòng |
| Harness dài hạn | planning-with-files, ARIS | Gần với harness Anthropic §2.1 (progress file, feature list `passes`), thêm plan có băm và reviewer khác model |
| Durable runtime | Trigger.dev, Conductor | Trigger.dev cạnh Inngest (TypeScript, có cloud); Conductor cạnh Temporal (JVM, workflow JSON) |

### 10d.5 Mẫu chung rút ra

1. **Stop gate tốt có trần và phát hiện đứng yên**: planning-with-files (20 lần, ledger không đổi thì cho dừng), ARIS (4 vòng), Conductor (`iteration < 10`). Ralph chỉ có trần vòng và điều kiện dừng dễ khớp nhầm.
2. **Không đặt loop trong loop**: ARIS cấm bọc vòng review trong `/loop`/cron; lịch nên kích hoạt *sự kiện bên ngoài* (thí nghiệm xong), không kích hoạt lại cả vòng.
3. **Bảo vệ file trạng thái khỏi bị sửa lén** (băm SHA-256 plan) là bước tiếp theo của "feature list chỉ đổi `passes`" (§2.1).
4. **Reviewer khác model là mặc định mới** (ARIS, codex-plugin-cc ở mục 20 §3t), đúng bài generator–evaluator §2.2, nhưng luôn kèm số vòng tối đa.
5. **Durable runtime đã có primitive cho agent** (waitpoint, chat stream, MCP task); trước khi tự viết harness có trạng thái, xem runtime đã có chưa. Telemetry của CLI vẫn phải kiểm từng cái: `DO_NOT_TRACK` chưa phổ quát.

**Nguồn §10d:** GitHub search API 31/10/2026 (6 truy vấn; `repo:` cho `github/gh-aw`, `yoheinakajima/babyagi`) · `meta_all.json`/`status_all.json` của đợt rà · clone `--filter=blob:none` 31/10/2026, đọc: OthmanAdi/planning-with-files (LICENSE, hooks/hooks.json, scripts/{gate-stop.sh, check-complete.sh, attest-plan.sh}, tests/) · snarktank/ralph (LICENSE, ralph.sh, prompt.md, CLAUDE.md, .claude-plugin/marketplace.json) · wanshuiyin/Auto-claude-code-research-in-sleep (LICENSE, README.md, .claude-plugin/marketplace.json, skills/auto-review-loop/SKILL.md, tools/{watchdog.py, threat_scan.py}, nhánh `aris-code`: LICENSE, cây thư mục) · conductor-oss/conductor (LICENSE, README.md, ai/DECISION_SWITCH.md, cây `ai/examples/`) · triggerdotdev/trigger.dev (LICENSE, README.md, packages/cli-v3/src/{mcp/telemetry.ts, cli/common.ts}, cây packages/trigger-sdk/src/v3/, hosting/) · https://github.com/OthmanAdi/planning-with-files · https://github.com/snarktank/ralph · https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep · https://github.com/conductor-oss/conductor · https://github.com/triggerdotdev/trigger.dev · https://github.com/github/gh-aw · https://github.com/reworkd/AgentGPT

## 10e. Nâng trần 2/11/2026: durable execution bọc thẳng agent SDK, chuẩn sự kiện và cổng quét workflow CI (yêu cầu người dùng)

> Đọc lại §0–§10d và catalog; grep `repo` trong `data/projects.json` trước khi thêm. Sao/license/ngày bằng GitHub search API 2/11/2026; clone `--depth 1 --filter=blob:none`, đọc LICENSE, README, CHANGELOG, cấu hình telemetry, tài liệu ngữ nghĩa thực thi. **Không cài, không chạy.**

**Trần hiện tại**

- §5 và §10d có Temporal, Restate, Inngest, DBOS, Trigger.dev, Conductor ở mức *nền tảng*; chưa có **lớp tích hợp** biến vòng lặp của agent SDK (OpenAI Agents, LangGraph, deepagents, Strands, Claude Agent SDK) thành workflow replay được, nên khuyến nghị "LangGraph cho suy luận + Temporal cho orchestration" vẫn phải tự viết keo.
- §4 (gh-aw) và §9 đặt agent chạy trên GitHub Actions, nhưng chưa có **cổng máy quét workflow** (template injection, `pull_request_target`, quyền thừa) trước khi cho agent tự chạy theo sự kiện.
- Trigger (cron/webhook/sự kiện) chưa có định dạng chuẩn; chống chạy trùng ở §8 mục 8 (outbox, receipt) chưa gắn với khoá dedupe chuẩn.

**Bảng repo mới**

| Repo | Lớp | ★ · license (2/11/2026) | Commit cuối | Vì sao nâng trần | Rủi ro |
|---|---|---|---|---|---|
| `temporalio/ai-integrations` | Đầu bảng (keo agent ↔ durable) | 36 · MIT | 31/10/2026 (`88745dc`) | Nơi mới của các plugin tách khỏi `temporalio/sdk-python` (1.35.0; các thư mục `contrib/{openai_agents,langgraph,deepagents,google_adk_agents,strands}` nay chỉ còn README chuyển hướng cùng các module shim tương thích (`__init__.py`, `workflow.py`, `testing.py`) re-export API từ gói độc lập mới): OpenAI Agents (**GA**), LangGraph và Strands (Public Preview), deepagents, Google ADK, Claude Agent SDK (Pre-release); có bản TS (OpenAI Agents, Vercel AI SDK, Strands, ADK), Go, Java. Lời gọi model chạy thành activity, nên crash giữa vòng không mất tiến trình | Repo mới, ít sao; README ghi rõ `@function_tool` **không** tự thành activity mà chạy trong workflow, tool có I/O phải tự bọc activity, nếu không sẽ vỡ tính tất định khi replay; đa số plugin chưa GA |
| `hatchet-dev/hatchet` | Đầu bảng (durable + queue) | 8.212 · MIT | 2/11/2026 (`964f6bc`) | Engine Go trên Postgres: durable task (README tự nhận thay được workflow Temporal/DBOS), DAG, durable sleep/event wait, cron, webhook, rate limit, concurrency, OTel; SDK Python/TS/Go/Ruby; v0.114.2 (26/10/2026) thêm pause rate-limit, `RetryAfter`, ảnh FIPS, "Replay as new" | Cài nhanh bằng `curl … \| bash` (nên đọc script trước); PostHog phía server chỉ bật khi đặt `SERVER_ANALYTICS_POSTHOG_ENABLED` + khoá (đọc `pkg/config/server/server.go`), CLI **chưa kiểm**; `AI_POLICY.md` bắt khai báo dùng AI khi đóng góp |
| `earendil-works/absurd` | Đầu bảng (tối giản) | 2.522 · Apache-2.0 | 20/10/2026 (`3cfc64f`) | Durable execution **chỉ cần Postgres**: một file `sql/absurd.sql` (~3,2k dòng) + migration, SDK TS/Python/Go, `absurdctl`, có `docs/agents.md` và skill cho coding agent; mẫu cron bằng idempotency key | v0.5.1, còn sớm; README hứa "exactly-once" nhưng `docs/concepts.md` ghi mã ngoài step vẫn có thể chạy lại: side effect phải nằm trong step và idempotent |
| `cloudevents/spec` | Chuẩn | 5.947 · Apache-2.0 | 22/10/2026 (`1025510`) | Chuẩn CNCF (graduated 25/1/2024), v1.0.2: thuộc tính bắt buộc `id`, `source`, `specversion`, `type`; "`source` + `id` trùng = sự kiện trùng" cho khoá dedupe sẵn; extension `distributed-tracing`, `expirytime`, `sequence`, `recordedtime`; binding HTTP/AMQP/Kafka… | Bản trên `main` là WIP; `v2.md` chỉ là danh sách cân nhắc, chưa có lịch |
| `zizmorcore/zizmor` | Cổng máy | 6.856 · MIT | 2/11/2026 (`fbf8d0c`) | Phân tích tĩnh GitHub Actions/Dependabot/pre-commit, ~40 audit: `template-injection`, `dangerous-triggers`, `excessive-permissions`, `bot-conditions` (actor bot giả mạo được), `unpinned-uses`, `secrets-inherit`, `cache-poisoning`…; có chế độ tự sửa | Bản trên `main` là 1.32.0-rc2; chưa có audit riêng cho action AI agent (grep `claude`/`agent` không thấy), phải tự thêm quy tắc cho prompt lấy từ issue/comment |
| `rhysd/actionlint` | Cổng máy | 4.371 · MIT | HEAD 19/4/2026 (`011a6d1`), push 16/7/2026 | Kiểm cú pháp và kiểu biểu thức `${{ }}`, input/output action, reusable workflow, cú pháp cron, script injection; tích hợp shellcheck/pyflakes cho `run:` | Chậm lại (v1.7.12); phần bảo mật mỏng hơn zizmor, nên chạy cả hai |

> Cùng đợt 2/11/2026, mục 13 §6h cũng hồ sơ hoá `zizmor` và `actionlint` (lint bảo mật GitHub Actions); catalog chỉ giữ một dòng cho mỗi repo, mục này nhìn từ góc workflow agent tự trị.

**Stack nâng trần**

1. **Cổng CI cho mọi workflow agent** (rẻ nhất, lợi ích ngay): `actionlint` + `zizmor` chặn merge với `.lock.yml` của gh-aw (§4), workflow Claude Code Action và loop CI (§9, mục 03 §8g `loop-engineering`); đặc biệt cấm `pull_request_target` + checkout mã PR và nội suy `github.event.comment.body` vào prompt/`run:`.
2. **Agent SDK đang dùng → plugin durable tương ứng**: OpenAI Agents/LangGraph/Strands/deepagents (mục 02) chạy trong Temporal (§5) qua `temporalio/ai-integrations`; mọi tool có I/O bọc thành activity, có test replay trước khi deploy.
3. **Không muốn vận hành cụm**: chọn Absurd (chỉ Postgres, hợp khi DBOS §5 đã quen Postgres) hoặc Hatchet (cần queue + DAG + rate limit chung một chỗ, thay Trigger.dev §10d khi muốn tự host Go/Postgres). Giữ 4 số bắt buộc của §10 (max vòng, ngân sách, timeout, hạn dùng) trong định nghĩa workflow.
4. **Trigger theo chuẩn**: đóng gói mọi trigger (cron, webhook GitHub, tin nhắn) thành CloudEvents; dùng `source`+`id` làm idempotency key ở outbox (§8 mục 8) và `expirytime` cho hạn dùng.
5. **Trace xuyên tầng**: gắn trace OTel GenAI (`invoke_agent`, `execute_tool`, mục 02 §4d) vào span workflow của Temporal/Hatchet để một lần chạy tự trị xem được từ trigger tới tool call.

**Nguồn §10e:** GitHub search API 2/11/2026 (`repo:` cho 6 repo trên, `temporalio/sdk-python`; `org:serverlessworkflow` không trả về repo `specification` nên chưa đưa vào) · clone 2/11/2026, đọc: temporalio/sdk-python (`pyproject.toml`, `temporalio/contrib/{openai_agents,langgraph,deepagents,google_adk_agents,strands}/README.md`) · temporalio/ai-integrations (LICENSE, cây `python/`, `typescript/`, `go/`, `java/`, `python/openai_agents/README.md`, dòng "Release stage" của từng plugin) · hatchet (LICENSE, README.md, CHANGELOG.md, AI_POLICY.md, `pkg/config/server/server.go`, `pkg/config/loader/loader.go`) · absurd (LICENSE, README.md, CHANGELOG.md, `sql/`, `docs/{concepts,storage}.md`, `docs/patterns/cron.md`) · cloudevents/spec (LICENSE, README.md, `cloudevents/spec.md`, `cloudevents/v2.md`, cây `cloudevents/extensions/`) · zizmor (LICENSE, README.md, `Cargo.toml`, cây `crates/zizmor/src/audit/`) · actionlint (LICENSE.txt, README.md, CHANGELOG.md) · https://github.com/temporalio/ai-integrations · https://temporal.io/blog/announcing-openai-agents-sdk-integration · https://github.com/hatchet-dev/hatchet · https://lucumr.pocoo.org/2025/11/3/absurd-workflows/ · https://github.com/cloudevents/spec · https://docs.zizmor.sh/audits/ · https://github.com/rhysd/actionlint

---

## 10f. Nâng trần toàn diện 2/11/2026: phục hồi, idempotency và timeout có hợp đồng kiểm

> Sau §5/§8/§10e, bổ sung ngữ nghĩa SDK thay vì thêm một danh sách workflow engine. Clone nông, đọc LICENSE, CI và implementation; metadata GitHub ngày 2/11/2026, hai repo chưa archive. **Đã đọc mã; chưa chạy SDK/server, replay hay thử crash.** Các cổng phía dưới là tiêu chí tham khảo cho dự án tích hợp.

| Dự án | ★ · license (đọc 2/11/2026) | HEAD / ngày commit | Lớp và điều kiện dùng |
|---|---|---|---|
| [Temporal Python SDK](https://github.com/temporalio/sdk-python) | 1,243 · MIT | `c1a79fb659ff` · 2026-10-30 | Workflow replay/activity retries; RetryPolicy maximum_attempts=0 là không giới hạn, heartbeat cần gọi thật |
| [Restate TypeScript SDK](https://github.com/restatedev/sdk-typescript) | 125 · MIT | `280fbc32e385` · 2026-11-02 | Durable ctx.run + ingress idempotency; side effect bên ngoài vẫn phải idempotent; kiểm SDK/server compatibility |

### Temporal Python SDK

SDK MIT của Temporal, tách workflow tất định và activity thực hiện I/O. [Activity API](https://github.com/temporalio/sdk-python/blob/c1a79fb659ffab144d7949213664a584809089f7/temporalio/workflow/_activities.py) có `start_to_close_timeout`, `schedule_to_close_timeout`, `heartbeat_timeout` và retry policy. [RetryPolicy](https://github.com/temporalio/sdk-python/blob/c1a79fb659ffab144d7949213664a584809089f7/temporalio/common.py) mặc định `maximum_attempts=0`, nghĩa là không đặt trần số lần thử; cần ràng buộc tổng thời gian hoặc số lần theo nghiệp vụ. Retry activity có thể gọi lại dịch vụ ngoài, nên payment/send/publish cần idempotency key tại dịch vụ nhận, không dựa riêng vào workflow ID.

[SDK guide](https://github.com/temporalio/sdk-python/blob/c1a79fb659ffab144d7949213664a584809089f7/README.md) yêu cầu activity thường heartbeat nếu cần nhận cancellation; đặt `heartbeat_timeout` không tự tạo heartbeat. Worker shutdown còn có thể chờ nếu activity không chịu dừng. Hướng dẫn có `Replayer` để kiểm history khi đổi workflow; CI [ci.yml](https://github.com/temporalio/sdk-python/blob/c1a79fb659ffab144d7949213664a584809089f7/.github/workflows/ci.yml) chạy test/time-skipping, không thay crash test của ứng dụng. Workflow sandbox giữ replay tất định, không phải biên bảo mật OS cho code không tin cậy. Tích hợp với `ai-integrations` ở §10e nhưng mọi tool có I/O vẫn phải có activity/timeout rõ.

### Restate TypeScript SDK

SDK MIT dùng `ctx.run` để ghi kết quả thao tác không tất định vào journal. [Context API](https://github.com/restatedev/sdk-typescript/blob/280fbc32e3858f853aa19296b7edcf771a22bc99/packages/libs/restate-sdk/src/context.ts) yêu cầu side effect idempotent; crash sau khi API ngoài đã ghi nhưng trước lúc kết quả được lưu vẫn có thể gọi lại callback. Tạo business idempotency key ổn định ngoài callback và đưa tới nhà cung cấp. [Ingress client](https://github.com/restatedev/sdk-typescript/blob/280fbc32e3858f853aa19296b7edcf771a22bc99/packages/libs/restate-sdk-clients/src/ingress.ts) có điều kiện retry theo idempotency key; bảo vệ ingress không thay dedupe ở API bên ngoài. [Handler options](https://github.com/restatedev/sdk-typescript/blob/280fbc32e3858f853aa19296b7edcf771a22bc99/packages/libs/restate-sdk/src/types/rpc.ts) tách `inactivityTimeout`, `abortTimeout`, retry và thời gian giữ idempotency/journal. Sau retention, đừng giả định key còn chặn trùng vô hạn. Server và SDK phải tương thích; tính năng pause retry ở README cần server/protocol cụ thể. So Temporal, hợp RPC/service durable TypeScript; vẫn cần Restate server và thiết kế vận hành riêng.

**Hợp đồng phục hồi tham khảo:** trigger có ID (CloudEvents §10e) → workflow/invocation ID ổn định → step có key nghiệp vụ → external receipt → journal/checkpoint → trạng thái cuối và đối soát. Không có transaction xuyên mọi API; phần ghi tiền/gửi thư/đăng bài cần thiết kế dedupe, kiểm receipt hoặc compensation cụ thể. Compensation là hành động nghiệp vụ mới, không tự xoá được thư đã gửi.

| Điểm gây lỗi phải thử tại dự án tích hợp | Điều kiện đạt |
|---|---|
| Worker chết trước/sau external commit, trước checkpoint | Retry dùng cùng business key; cuối cùng chỉ có một tác dụng phụ hoặc có đối soát phát hiện trùng |
| Webhook/cron gửi lặp và lệch thứ tự | Dedupe theo nguồn + event ID; không tạo thêm workflow ngoài chủ ý |
| API chậm, 429/5xx kéo dài | Có timeout từng lần và hạn tổng; backoff và ngân sách không vượt trần |
| Hết quyền/cancellation khi đang chạy | Ngừng bước tiếp theo, kiểm receipt bước đang dở; không coi cancel là rollback |
| Deploy code mới khi workflow cũ chưa xong | Replay history/kiểm tương thích pass hoặc có đường version/migration |
| Operator retry sau thời gian retention | Kiểm trạng thái nghiệp vụ trước khi tạo tác dụng phụ mới |

**Bảng chọn tầng kiểm:** replay phát hiện workflow mất tất định; unit test thử policy retry; integration test dùng dịch vụ giả kiểm số receipt; fault injection cắt worker/mạng kiểm khoảng trống trước checkpoint. So sánh engine bằng cùng hợp đồng trên, không suy ra “exactly-once ngoại hệ” từ chữ durable. Dữ liệu nhạy cảm trong history/journal cần policy lưu giữ và truy cập phù hợp; xem mục 12 §4d cho kiểm quyền khi job phục hồi sau nhiều giờ.

**Đối chiếu ba cột:** đã có và sâu hơn: danh sách engine, chuẩn trigger, circuit breaker (§5/§8/§10e); đã có nhưng mỏng hơn: retry/idempotency mới là khuyến nghị; mới: SDK implementation, cửa sổ external commit–checkpoint, heartbeat và kiểm retention/version. Không thay đổi kết luận về license engine Restate ở §5 bằng license MIT của riêng SDK.

**Nguồn §10f:** [Temporal SDK LICENSE](https://github.com/temporalio/sdk-python/blob/c1a79fb659ffab144d7949213664a584809089f7/LICENSE); [Restate SDK LICENSE](https://github.com/restatedev/sdk-typescript/blob/280fbc32e3858f853aa19296b7edcf771a22bc99/LICENSE), [CI SDK](https://github.com/restatedev/sdk-typescript/blob/280fbc32e3858f853aa19296b7edcf771a22bc99/.github/workflows/test.yml); [Temporal retries](https://docs.temporal.io/encyclopedia/retry-policies), [Temporal activity failures](https://docs.temporal.io/encyclopedia/detecting-activity-failures), [Restate durable steps](https://docs.restate.dev/develop/ts/durable-steps). Mọi số sao và HEAD thuộc snapshot 2/11/2026, không phải phiên bản package đã chạy.

## 10g. Hồ sơ duongbirken2510/AI-Money: “thực nghiệm 20 ngày để AI tự kiếm tiền nuôi server”, bot Facebook lách bộ lọc nhóm (link người dùng gửi, đọc mã 3/11/2026)

> Người dùng gửi ảnh dòng chữ "GITHUB REPO: github.com/duongbirken2510/AI-Money". Đã clone đủ lịch sử, HEAD `31a660d6a26ff92691949c76cdf63bd71fbc9f0a` (3/11/2026 10:53 +07). **Không cài, không chạy**, không truy cập website của dự án.

### 10g.1 Hồ sơ nhanh

| Thuộc tính | Giá trị (3/11/2026) |
|---|---|
| Repo | https://github.com/duongbirken2510/AI-Money · **13★, 8 fork**, tạo 3/11/2026 03:22 UTC. Chỉ có **2 commit** (bản đẩy lên đầu tiên và một commit thêm banner) |
| Tác giả | Dương Birken (`duongbirken2510`). Repo khác của tác giả: `deskaura` (0★, tạo 2/11/2026) |
| License | **Không có file LICENSE.** README có mục "Giấy phép & Cam kết" nhưng chỉ ghi mục đích học tập, không cấp quyền dùng. Mặc định là bảo lưu mọi quyền |
| Mô tả | Một agent được giao "tối hậu thư": trong 20 ngày phải tự kiếm doanh thu thật > 0đ để trả tiền server (`kiemtien.deta.vn`). Sản phẩm gồm "Liên Hoa Các" (chùa online 4-trong-1: gõ mõ, thả hoa đăng trả phí qua VietQR, gieo quẻ do AI luận giải), thần số học Pythagoras, cẩm nang 12 bài chatbot chốt đơn (bán phần mở khóa), khoảng 9 công cụ AI miễn phí và gói dịch vụ B2B dựng landing page |
| Mã | Khoảng 10.000 dòng Python thuần: `server.py` 3.500 dòng (`ThreadingHTTPServer` + SQLite, không framework), `social_autopilot.py` 1.870, `numerology_comment_bot.py` 1.026, `fb_poster.py` 939, `agent_worker.py` 781. Frontend HTML/Canvas/WebAudio trong `public/`. 34 MB, phần lớn là ảnh. Không có test, không có CI |
| AI | Gemini API (key của chủ site), hoặc CLI Antigravity `agy` chạy với `--sandbox` và câu dặn trong prompt "không gọi tool, không chạy shell". 3 skill trong `.agents/skills/` (đăng bài nhóm Facebook, landing page, three.js) |

### 10g.2 Đọc mã: phần làm đúng

- **Webhook ngân hàng** (`server.py:886`, `verify_webhook_auth`): nhận SePay (Apikey hoặc secret trên URL) và Casso V1/V2 (HMAC-SHA512), mọi phép so sánh dùng `hmac.compare_digest`. **Chưa cấu hình secret thì từ chối** (`unconfigured`). Có lọc giao dịch trùng theo `tx_ref` trong bảng `webhook_logs`.
- Khóa admin cũng so bằng `compare_digest` và bắt buộc có trong `config.json`. Server bind `127.0.0.1:8080` (biến `HOST` mặc định), đưa ra ngoài qua Cloudflare Tunnel. Secret không commit; chỉ có `config.example.json`.

### 10g.3 Rủi ro (đọc mã)

- ⚠️ **Tự động hóa tài khoản Facebook cá nhân để lách bộ lọc nhóm.** `fb_poster.py`, `social_autopilot.py` và `numerology_comment_bot.py` điều khiển Chrome đang đăng nhập Facebook qua CDP (`127.0.0.1:9225`) để đăng bài vào nhóm và **tự trả lời bình luận mỗi 4 giờ**. Skill `.agents/skills/facebook-group-posting/SKILL.md` nêu thẳng mục đích "anti-filter": không đặt link trong chữ để **Admin Assist của nhóm không tự từ chối**, mà in tên miền vào watermark của ảnh đính kèm. Điều khoản của Meta cấm tự động hóa tài khoản theo cách này; rủi ro bị khóa tài khoản và bị coi là spam **(điều khoản chưa đối chiếu nguyên văn)**. Kho chỉ ghi đây là dữ kiện, không khuyến nghị dùng.
- ⚠️ **Thu dữ liệu cá nhân mà không thấy chính sách bảo mật.** Form B2B lấy số điện thoại/Zalo và ghi chú; thần số học nhận họ tên và ngày sinh; có bảng `private_messages`, `group_messages`, `free_chat_trials`, `viewers`. Grep `public/*.html` không thấy trang chính sách bảo mật hay cơ chế xin đồng ý. Theo Luật 91/2025 + NĐ 356/2025 (mục 18 §4e, checklist 01 mục A–B), site thu thập như vậy ít nhất ở **mức 1** và phải có thông báo cùng sự đồng ý.
- ⚠️ Webhook chấp nhận secret qua **query string** (`?secret=`), và trang admin hiển thị sẵn URL có kèm secret. Secret trên URL dễ lọt vào log của proxy hoặc tunnel. Nên dùng header hoặc HMAC.
- Trường `_test` do client gửi lên khiến lead B2B không được tính vào thống kê sự kiện (`server.py:3381`). Không phải lỗ hổng, nhưng bất kỳ ai cũng làm lệch được số liệu "minh bạch" của thực nghiệm.
- Nội dung tâm linh và thần số học có thu phí (thắp "Đại Liên Hoa Đăng 30 ngày" 20.000đ) do AI luận giải. README tự ghi "không phải cơ sở tôn giáo, không tuyên truyền mê tín". Quảng cáo dịch vụ loại này vẫn chịu Luật Quảng cáo (mục 18 §5d có rule cho claim tuyệt đối).
- Mới 1 ngày, 2 commit, không test, không CI, không license. Số liệu doanh thu và lượt dùng trong README và ảnh (`tsh-daily-*.png`) là **tự công bố, chưa xác minh**.

### 10g.4 Đặt trong bối cảnh

- Cùng dòng "giao agent một mục tiêu kinh doanh rồi để nó tự chạy" (mục 21 §10, lịch sử AutoGPT/BabyAGI): điểm khác là có **tiền thật qua VietQR + webhook** và một deadline cứng. Bài học có giá trị là phần webhook fail-closed, không phải phần tăng trưởng.
- Nếu dựng thử nghiệm tương tự: dùng API chính thức của nền tảng (Facebook Graph API cho Page, Zalo OA) thay vì điều khiển trình duyệt; có trang chính sách bảo mật và ô đồng ý trước khi nhận số điện thoại hay ngày sinh; chạy vn-law-check (mục 18 §4e) trước khi mở site.

**Nguồn §10g:** ảnh người dùng gửi 3/11/2026 · clone https://github.com/duongbirken2510/AI-Money HEAD `31a660d6a26ff92691949c76cdf63bd71fbc9f0a` (README.md, `server.py` dòng 107–113, 886–926, 2545–2563, 3215–3240, 3370–3400, 3496–3497; `agent_worker.py` dòng 60–100; `fb_poster.py`; `numerology_comment_bot.py`; `.agents/skills/facebook-group-posting/SKILL.md`; grep chính sách bảo mật trong `public/*.html`) · GitHub search API `repo:duongbirken2510/AI-Money`, `user:duongbirken2510` 3/11/2026.

## 10h. Hồ sơ pullboard-dev/pullboard: hàng đợi điều phối nhiều agent sống trong repo, “agent thứ hai kiểm tra” thực thi bằng khác phiên chạy (ảnh README người dùng gửi, đọc mã 3/11/2026)

> Ảnh là phần đầu README: logo, "pullboard.dev · lives in your git repo · no dependencies · Walk away, and it builds", badge "pullboard 1169 items", "npm v0.9.3", "license MIT"; ba bước Vision → Specification → Inspection; ảnh chụp trang live "32 agents, 22 building, 3 reviewing, 180 landed in 24 hours" với bảng 45 seat (`core-695`…). Đã clone `--filter=blob:none` đủ lịch sử, HEAD `6231e10d4f22673b41ec5797a642b7b6f8e9fd06` (28/10/2026). **Không cài, không chạy.**

### 10h.1 Hồ sơ nhanh

| Thuộc tính | Giá trị (3/11/2026) |
|---|---|
| Repo | https://github.com/pullboard-dev/pullboard · **528★** (GitHub search API; ảnh chụp ngày 28/10 ghi 426). Tạo 7/10/2026. npm `pullboard` 0.9.3 (40 bản từ 16/7/2026) |
| License | MIT, "Copyright (c) 2026 Corey Olson". Đóng góp phải ký **CLA** (dựa trên Apache ICLA 2.2) qua bot, ngoài sign-off DCO kiểm trong CI |
| Lịch sử | **7.341 commit trong 24 ngày** (4/10 → 28/10/2026), tất cả dưới tên **Corey Olson** (hai email), cao điểm 886 commit/ngày (24/10). Không có trailer Co-Authored-By: hàng chục agent commit dưới cùng một danh tính nên git không cho biết agent nào làm gì |
| Thành phần | CLI Node (`bin/pullboard.js`, Node ≥ 22.13), **0 phụ thuộc npm** (đúng như "no dependencies"); board là **một file SQLite trong `.git`** dùng chung cho mọi worktree, không commit; `SPEC.md`, `DOCTRINE.md`, `pullboard.json`, `AGENTS.md` và git hook ở checkout chính; skill cho agent; trang "Pullboard View" chạy local. Relay tùy chọn (`relay/`) cho điện thoại và máy khác |

### 10h.2 Kiểm ảnh

| Ô trong ảnh | Kết quả | Đối chiếu |
|---|---|---|
| "no dependencies" | ✅ | `package.json` không có `dependencies` lẫn `devDependencies` |
| "npm v0.9.3", MIT | ✅ | npm latest 0.9.3; `LICENSE` MIT |
| "pullboard 1169 items" | ⚠️ tự công bố | Badge đọc `docs/badges/items.json` trong repo, tức số do chính dự án ghi |
| "32 agents… 180 landed in 24 hours" | ⚠️ tự công bố | Là ảnh chụp trang live ngày 28/10 (`docs/img/live-floor-*.png`). Có thể đối chiếu một phần với git: 7.341 commit trong 24 ngày, khoảng 300 commit/ngày. Một "item landed" có thể gồm nhiều commit, nên không so trực tiếp được. Từ 28/10 tới 3/11 repo công khai **không có commit mới**, nên trang live tại thời điểm đọc có thể đang chạy trên bản khác **(chưa xác minh)** |
| "lives in your git repo" / "Nothing is hosted" | ⚠️ đúng cho phần lõi | Board, spec, hook đều local. Nhưng README cũng giới thiệu **relay** chạy tại `app.pullboard.dev` (Railway): lưu bản ghi board đã niêm phong, journal, backup, liên kết GitHub App. Theo `docs/architecture.md`, relay chỉ đọc được metadata (repo `owner/name`, thời điểm, thiết bị); nội dung cần khóa board, chỉ máy và điện thoại đã ghép cặp có. Board không liên kết hoặc 90 ngày không hoạt động thì bị xóa |

### 10h.3 Đọc mã: "agent thứ hai kiểm tra" thực thi tới đâu

- Luật PB1 trong blueprint: "A builder never verifies their own work." Trong mã: `src/bar-check.js:86` từ chối khi `builderSession === reviewerSession` (`BAR_SELF_SIGN`). Mỗi ghi chú bar-check chỉ nhận một câu trả lời của reviewer (`:81`). Lane được build trong worktree riêng, không build ở checkout chính (`src/board.js:996`).
- Giới hạn: "khác người" ở đây là **khác phiên chạy**. Hai phiên có thể cùng model, cùng prompt, cùng máy, cùng tài khoản. Không có chữ ký số theo từng agent, và commit đều mang danh tính chủ repo. Đây là cổng chống "tự khen" hữu ích, nhưng chưa phải review độc lập theo nghĩa khác model hay khác người (so với Kornia mục 14 §5f và quy trình reviewer khác model của design-os-vietnamese mục 18 §5d).
- CI: `check-signoffs.js` kiểm sign-off của mọi commit với chính sách ở base tin cậy (đọc file sự kiện, không nội suy giá trị do contributor đưa vào shell), `pullboard spec check`, test chia shard. Action ghim theo tag (`actions/checkout@v4`), không theo SHA.
- Grep `telemetry` chỉ thấy "private telemetry" về sức khỏe relay, đọc local (`src/relay-canary-*.js`); không thấy client analytics gửi ra ngoài.

### 10h.4 Đặt trong bối cảnh

- Cùng bài toán với nhóm "đội agent" ở mục 03 §8f (Agent Teams) và ADE ở mục 01 (Orca §3n, Vibe Kanban): điểm khác là Pullboard đưa **spec và luật** vào repo, có máy kiểm (bar-check, spec check, hook), thay vì chỉ là giao diện quản lý phiên.
- Rủi ro: một người duy trì, dự án mới 4 tuần, nhịp hàng trăm commit mỗi ngày do agent viết; số liệu năng suất đều tự công bố. Nếu thử, chạy trên repo phụ, không liên kết relay với repo khách hàng, và đọc `DOCTRINE.md` + `SPEC.md` để biết hook sẽ chặn những gì.

**Nguồn §10h:** ảnh README người dùng gửi 3/11/2026 · clone https://github.com/pullboard-dev/pullboard HEAD `6231e10d4f22673b41ec5797a642b7b6f8e9fd06`: https://github.com/pullboard-dev/pullboard/blob/6231e10d4f22673b41ec5797a642b7b6f8e9fd06/README.md · https://github.com/pullboard-dev/pullboard/blob/6231e10d4f22673b41ec5797a642b7b6f8e9fd06/package.json · https://github.com/pullboard-dev/pullboard/blob/6231e10d4f22673b41ec5797a642b7b6f8e9fd06/LICENSE · https://github.com/pullboard-dev/pullboard/blob/6231e10d4f22673b41ec5797a642b7b6f8e9fd06/CLA.md · https://github.com/pullboard-dev/pullboard/blob/6231e10d4f22673b41ec5797a642b7b6f8e9fd06/docs/architecture.md · https://github.com/pullboard-dev/pullboard/blob/6231e10d4f22673b41ec5797a642b7b6f8e9fd06/relay/README.md · https://github.com/pullboard-dev/pullboard/blob/6231e10d4f22673b41ec5797a642b7b6f8e9fd06/src/bar-check.js · https://github.com/pullboard-dev/pullboard/blob/6231e10d4f22673b41ec5797a642b7b6f8e9fd06/src/blueprints/pullboard.json · https://github.com/pullboard-dev/pullboard/blob/6231e10d4f22673b41ec5797a642b7b6f8e9fd06/bin/check-signoffs.js · `docs/badges/items.json`; `git shortlog`, `git log` theo ngày · https://registry.npmjs.org/pullboard · GitHub search API 3/11/2026.

## 10i. Nâng trần 4/11/2026: workflow phục hồi được và nâng phiên bản không phá lịch sử

**Trần hiện tại:** §10f đã phân biệt retry, timeout và idempotency. Với xưởng phần mềm, khoảng trống tiếp theo là kiểm **tương thích lịch sử khi đổi code**, và xác nhận tác động ngoài hệ thống chỉ xảy ra theo hợp đồng nghiệp vụ. Một workflow hoàn thành sau restart chưa chứng minh nó không gửi hai email, tạo hai hoá đơn hoặc gọi model thêm tiền.

<a id="temporal-replay-factory"></a>

### 10i.1 Temporal Python SDK: dùng lịch sử thật làm tập regression

Đọc mã ngày **2026-11-04**, SHA `1845f25aeac33114b9c46fbccfac19976129f796`, license MIT; chỉ đọc source/LICENSE/CI, chưa chạy Temporal, không tái lập khả năng phục hồi.

`Replayer.replay_workflow` và `replay_workflows` mặc định `raise_on_replay_failure=True`; đường gọi thực sự ném lỗi khi replay trả `replay_failure`. Khi đặt `False`, API đơn `replay_workflow` trả lỗi trong trường `WorkflowReplayResult.replay_failure`; API nhiều lịch sử `replay_workflows` tích luỹ lỗi trong map `WorkflowReplayResults.replay_failures`. Caller phải kiểm đúng trường theo API đã gọi. `tests/worker/test_replayer.py` có lịch sử nondeterministic và assertion `NondeterminismError`: đây là mẫu negative fixture hữu ích, không phải kết quả kiểm của kho này. CI gọi `poe test`, xuất JUnit và chạy thêm môi trường time-skipping; việc đọc YAML không xác nhận mọi run ở upstream đều xanh.

`RetryPolicy.maximum_attempts=0` vẫn là **không đặt trần số lần thử**; deadline/timeout và giới hạn nghiệp vụ cần được định nghĩa riêng. Retry activity không mang lại exactly-once cho API bên ngoài. Xưởng cần operation ID ổn định, khoá/unique constraint hoặc idempotency key ở đích, cùng bước đối soát khi timeout làm kết quả trở nên không rõ.

| Lựa chọn | Nên chọn khi | Cổng cần thêm tại dự án tích hợp |
|---|---|---|
| Temporal SDK + history replay | Có workflow đang chạy qua nhiều phiên bản, cần kiểm thay đổi code trên history đã lưu | Tập history đã ẩn dữ liệu; replay phải có số workflow >0, không có failure; phân biệt API không ném với kết quả sạch |
| [Restate SDK](#restate-typescript-sdk) | App TypeScript muốn durable context và ingress idempotency | Crash ở trước/sau side effect, gửi trùng key, kiểm sổ nghiệp vụ; pin tương thích SDK/server |
| DBOS, đã so ở §5 | Đã dùng Postgres, muốn trạng thái durable gần dữ liệu ứng dụng | Kiểm transaction boundary và tác động ngoài DB; không suy transaction DB bao trùm dịch vụ ngoài |
| Job/queue thông thường + outbox | Tác vụ nhỏ, không cần orchestration dài hạn | Lease/ack, retry có trần, DLQ và đối soát; ít thành phần hơn nhưng vẫn phải kiểm duplicate |

### 10i.2 Đường nghiệm thu cho xưởng

1. Tách phần suy luận agent khỏi activity có side effect; manifest ghi workflow type, deployment/version, retry/deadline và chủ sở hữu.
2. Lưu history đại diện cho nhánh thành công, lỗi, chờ người duyệt, huỷ và phiên bản cũ; xoá/che dữ liệu nhạy cảm trước khi đưa vào CI. History cũng là tài sản có quyền truy cập và retention.
3. Khi đổi orchestration, replay tập history cũ trước rollout. Có negative fixture đã biết sai để chứng minh cổng thực sự bắt nondeterminism; không chấp nhận tập history rỗng.
4. Fault injection tại dự án tích hợp: worker chết trước/sau API call, mất mạng sau khi đích đã commit, hết lease, request lặp. Artifact là run ID + operation ID + số side effect cuối, không chỉ log “retry succeeded”.
5. Đưa workflow error/queue age/cost vào [mục 33](../33-reliability-observability-operations/README.md); stop/cancel có đường đối soát. Kết quả replay sạch chỉ áp cho history đã chọn, không chứng minh mọi tương tác production.

**Đã đổi so với lượt trước:** bổ sung đường gọi của replay và tình huống API thu lỗi thay vì ném; cập nhật SHA phạm vi SDK. Không suy rằng Temporal server hay toàn bộ integration ở §10e đã được kiểm lại.

**Nguồn §10i:** [LICENSE](https://github.com/temporalio/sdk-python/blob/1845f25aeac33114b9c46fbccfac19976129f796/LICENSE) · [temporalio/worker/_replayer.py](https://github.com/temporalio/sdk-python/blob/1845f25aeac33114b9c46fbccfac19976129f796/temporalio/worker/_replayer.py) · [temporalio/common.py](https://github.com/temporalio/sdk-python/blob/1845f25aeac33114b9c46fbccfac19976129f796/temporalio/common.py) · [tests/worker/test_replayer.py](https://github.com/temporalio/sdk-python/blob/1845f25aeac33114b9c46fbccfac19976129f796/tests/worker/test_replayer.py) · [.github/workflows/ci.yml](https://github.com/temporalio/sdk-python/blob/1845f25aeac33114b9c46fbccfac19976129f796/.github/workflows/ci.yml).

## 10i. Hồ sơ deepseek-ai/dsh-superagent-prototype: agent chủ động cho một repo GitHub, phân quyền nhiều tầng nhưng worker chạy lệnh không cần duyệt (ảnh README người dùng gửi, đọc mã 4/11/2026)

> Ảnh là phần đầu README: "dsh-superagent", ghi chú "Research prototype for reference only, not an official DeepSeek product… with much of the engineering done by coding agents… not production-ready", nhắc bài "Exploring Super-agent Design: Towards a More Autonomous Agent System", mô tả agent chủ động cho một repo GitHub (tùy chọn Feishu), cách cài "Ask your coding agent: Read SETUP.md…" và 7 tài liệu đánh số 000–006. Đã clone đủ lịch sử, HEAD `8c32a9dc5d72c033816c6a8110b37f40cf94fba4` (31/10/2026). **Không cài, không chạy.**

### 10i.1 Hồ sơ nhanh

| Thuộc tính | Giá trị (4/11/2026) |
|---|---|
| Repo | https://github.com/deepseek-ai/dsh-superagent-prototype · **18.363★** sau 4 ngày (tạo 31/10/2026, GitHub search API) |
| License | MIT, "Copyright (c) 2026 DeepSeek Harness Team" |
| Lịch sử | **1 commit duy nhất** ("feat: add the dsh-superagent research prototype", tác giả `DeepSeek Harness Team <team@dsh.dev>`): bản được dọn lại để công bố, không xem được quá trình phát triển. README tự ghi phần lớn mã do coding agent viết |
| Thành phần | Bundle (plugin) cho **DeepSeek Harness** (mục 01, `deepseek-harness`), phụ thuộc `@deepseek-ai/cordis` 4.0.5-alpha.1. 216 file: `src/` 111, `tests/` 65 (vitest), `prompts/` 15, `docs/` 9 (000–008), `skills/`, `locale/` |
| Cách chạy | Chạy trong một profile DeepSeek Harness riêng (`superagent`), panel web tại `127.0.0.1:3082`. Nghe GitHub bằng **polling** thông báo của tài khoản agent (mặc định mỗi phút), không cần webhook hay mở cổng vào. Feishu qua `lark-cli` |

### 10i.2 Đọc mã: mô hình quyền làm kỹ

- **Tách "ai được ra lệnh" khỏi nội dung tin nhắn.** `docs/002-authorization.md`: "The host enforces allowed lists, rules and Mandates. Messages, comments and quoted documents are inputs to a decision; they cannot change those permissions." Có ba mức: `explicit` (người trong danh sách gọi agent), `inferred` (theo dõi thread, bot trong danh sách), `not admitted` (bot lạ và mọi thứ khác). Bot và CI chỉ được làm **ngữ cảnh** trên ticket đã có, không tạo quyền mới.
- **Chế độ chủ động mặc định là `observe`**: ứng viên suy ra được đánh giá, nhưng chỉ ghi lại "would accept" chứ không nhận việc. Phải chủ động chuyển sang `auto` sau khi xem lại các quyết định. Bảng admission mặc định `ignore` với người ngoài danh sách.
- **Mỗi ticket có Mandate** (quy tắc đã khớp, phạm vi). Executor trả lại tin nhắn vượt phạm vi để đánh giá lại. Siết một ô của bảng admission không dừng ngay các ticket đang mở, nhưng có thể thu hồi Mandate của chúng khi được kiểm lại trước lúc chạy tiếp.
- **Vệ sinh credential**: dịch vụ subprocess bỏ mọi biến môi trường có tên chứa KEY, PASSWORD, SECRET hoặc TOKEN; worker dùng file git config riêng (`worker-gitconfig`) với tài khoản agent riêng qua wrapper `gh-agent`; API panel yêu cầu header `x-orchestrator-request: 1` và từ chối `Origin` khác (chống CSRF). `SETUP.md` cấm agent hỏi secret trong chat; bước nhập secret do người vận hành tự chạy.
- **Tài liệu tự nói rõ giới hạn**, đúng kiểu kho muốn thấy.

### 10i.3 Rủi ro (theo chính tài liệu)

- ⚠️ **Worker chạy lệnh không cần duyệt.** `docs/003-execution.md`: "Executor Sessions run commands without approval as the operator's OS user." Danh sách lệnh bị chặn (`DSH_SUPERAGENT_BLOCKED_COMMANDS`) và thư mục riêng chỉ là mặc định: "not a security boundary. A worker can still execute a program by absolute path." Worker còn giữ credential `gh` của tài khoản agent qua credential helper.
- ⚠️ **Prompt injection qua ngữ cảnh**: mọi tin nhắn trên thread đã đăng ký (kể cả bot, log CI, comment của người ngoài danh sách) đều tới worker làm ngữ cảnh. Chúng không tạo quyền mới trong host, nhưng worker chạy shell không cần duyệt với credential của tài khoản agent nên vẫn có thể bị dẫn đi. Phạm vi thiệt hại phụ thuộc vào quyền của tài khoản agent trên repo.
- **Auto-merge do prompt quyết định**: "Auto-merge is governed by the Delivery requirements prompt. The host has no merge-specific decision logic." Nếu cho tài khoản agent quyền merge, cổng duy nhất là branch protection của GitHub và lời dặn trong prompt.
- Background job được chạy tối đa 30 phút sau mỗi lượt; server dựng cho người review có thể chạy tới khi assignment kết thúc.
- Phiên bản 0.1.0, phụ thuộc bản alpha của cordis, một commit, tự nhận "not production-ready".

### 10i.4 Dùng thế nào

- Chạy trên **máy hoặc VM riêng** (user OS riêng, không có credential khác), vì giới hạn lệnh không phải ranh giới bảo mật. Container hoặc VM là lớp cách ly thật (mục 11 §3).
- Cấp cho tài khoản agent **quyền tối thiểu**: không quyền admin, bật branch protection bắt buộc review và check trên `main`, để auto-merge không thể bỏ qua cổng.
- Giữ `observe` lâu, đọc các Decision đã ghi rồi mới bật `auto`; danh sách người được ra lệnh càng ngắn càng tốt.
- So với Pullboard (§10h): Pullboard điều phối nhiều agent trong một repo bằng board và luật trong git; dsh-superagent là **một agent trực** nhận việc từ GitHub/IM với mô hình quyền chặt hơn ở phía host, nhưng cả hai đều không sandbox lệnh.

**Nguồn §10i:** ảnh README người dùng gửi 4/11/2026 · clone https://github.com/deepseek-ai/dsh-superagent-prototype HEAD `8c32a9dc5d72c033816c6a8110b37f40cf94fba4`: https://github.com/deepseek-ai/dsh-superagent-prototype/blob/8c32a9dc5d72c033816c6a8110b37f40cf94fba4/README.md · https://github.com/deepseek-ai/dsh-superagent-prototype/blob/8c32a9dc5d72c033816c6a8110b37f40cf94fba4/SETUP.md · https://github.com/deepseek-ai/dsh-superagent-prototype/blob/8c32a9dc5d72c033816c6a8110b37f40cf94fba4/LICENSE · https://github.com/deepseek-ai/dsh-superagent-prototype/blob/8c32a9dc5d72c033816c6a8110b37f40cf94fba4/package.json · https://github.com/deepseek-ai/dsh-superagent-prototype/blob/8c32a9dc5d72c033816c6a8110b37f40cf94fba4/docs/002-authorization.md · https://github.com/deepseek-ai/dsh-superagent-prototype/blob/8c32a9dc5d72c033816c6a8110b37f40cf94fba4/docs/003-execution.md · https://github.com/deepseek-ai/dsh-superagent-prototype/blob/8c32a9dc5d72c033816c6a8110b37f40cf94fba4/docs/005-panel.md · https://github.com/deepseek-ai/dsh-superagent-prototype/blob/8c32a9dc5d72c033816c6a8110b37f40cf94fba4/docs/006-deployment.md · `prompts/dispatch.md` · GitHub search API `dsh-superagent` 4/11/2026.

<a id="anhkysuai-2026-11-23"></a>

## Đánh giá từ kho Anh Kỹ Sư AI — 23/11/2026

Phần này có **28 hồ sơ hoặc phạm vi đối chiếu** từ [nguồn tuyển chọn](https://anhkysuai.com/kho/). [Bảng đủ 1.295 repo](../data/collections/anhkysuai-kho.json) ghi trạng thái đối chiếu từng link; [danh sách URL](../data/collections/anhkysuai-kho-links.txt) phục vụ tra cứu. Nguồn tuyển chọn giúp phát hiện repo; đánh giá bên dưới dựa trên clone và permalink upstream cùng metadata GitHub ngày 2026-11-23.

Mức `docs-read`/`code-read` chỉ áp dụng phạm vi ghi tại mỗi hồ sơ. Chưa cài, build, chạy test hay benchmark mã upstream. Giấy phép có thể tách theo code, model, nội dung, asset hoặc bản enterprise; con số/tuyên bố của tác giả chưa được tái lập nếu không có ghi chú khác.

<a id="anhkysuai-2026-11-23-changedetection-io"></a>

### changedetection.io

**Repo:** [dgtlmoon/changedetection.io](https://github.com/dgtlmoon/changedetection.io) · **License:** Apache-2.0 · **★ 35,973 (GitHub API, 2026-11-23)**

**Mục đích:** Theo dõi thay đổi website và gửi thông báo khi nội dung quan tâm thay đổi.

**Giá trị và cơ chế:** README tách lấy trang, điều kiện theo dõi và thông báo; bổ sung tóm tắt/điều kiện LLM qua nhà cung cấp đám mây hoặc Ollama.

**Giới hạn:** Chưa kiểm tra trình duyệt thực, chống bỏ sót thay đổi hay tính đúng của bộ lọc. Trang động và cookie đăng nhập làm tăng công vận hành; dùng LLM ngoài máy có thể gửi nội dung theo dõi đi.

**Cách tham khảo/tích hợp:** Tạo vài watch có mẫu thay đổi đã biết, kiểm tra selector và ngưỡng rồi mới tăng lịch quét.

**Thay thế:** [Huginn](https://github.com/huginn/huginn), [n8n](https://github.com/n8n-io/n8n), [Crawlee](../24-ai-data-engineering/README.md#anhkysuai-2026-11-23-crawlee).

**Bằng chứng:** `docs-read`, ngày 2026-11-23, commit [`ae3d178881ce`](https://github.com/dgtlmoon/changedetection.io/commit/ae3d178881ceef13e524c8ec9378ec3b2a5b29b5). README và các tài liệu/manifest/CI hiện diện, đọc chọn lọc; chưa kiểm implementation. Chưa cài/chạy upstream.

**Nguồn:** [README.md](https://github.com/dgtlmoon/changedetection.io/blob/ae3d178881ceef13e524c8ec9378ec3b2a5b29b5/README.md) · [LICENSE](https://github.com/dgtlmoon/changedetection.io/blob/ae3d178881ceef13e524c8ec9378ec3b2a5b29b5/LICENSE) · [metadata GitHub](https://api.github.com/repos/dgtlmoon/changedetection.io).

<a id="anhkysuai-mastodon-mastodon"></a>

### Mastodon

**Repo:** [mastodon/mastodon](https://github.com/mastodon/mastodon) · **License:** AGPL-3.0-or-later · **Kiểm:** 2026-11-23, `docs-read`, [`47c3a7dafa52`](https://github.com/mastodon/mastodon/tree/47c3a7dafa52551850756744e189beb447fc2c48) (commit 2026-11-23). **Sao:** 50,713 tại 2026-11-23 theo [GitHub API](https://api.github.com/repos/mastodon/mastodon).

| Mục | Đánh giá |
|---|---|
| Mục đích | Máy chủ mạng xã hội liên thông bằng ActivityPub. |
| Giá trị và cơ chế theo tài liệu | README mô tả federation, timeline, media và công cụ kiểm duyệt; repo có ứng dụng web cùng kiểm thử JavaScript. |
| Giới hạn | Tự host tạo trách nhiệm kiểm duyệt, lưu media và vận hành liên thông; tính riêng tư không thể suy chỉ từ nhãn federated. Chưa thử federation hay tải thực tế. |
| Điều kiện tích hợp | Dùng instance thử, kiểm chính sách liên thông và quyền ứng dụng; cân nhắc AGPL khi sửa server và cung cấp qua mạng. |
| Lựa chọn đối chiếu | Misskey; Pleroma; GoToSocial. |

**Phạm vi bằng chứng:** đã clone, đọc trích đoạn tài liệu, giấy phép và các file cấu hình được dẫn dưới đây; chưa chạy mã, build, benchmark hoặc test upstream. `docs-read` không phải kiểm chứng implementation.

**Nguồn tại cùng SHA:** [README.md](https://github.com/mastodon/mastodon/blob/47c3a7dafa52551850756744e189beb447fc2c48/README.md) · [LICENSE](https://github.com/mastodon/mastodon/blob/47c3a7dafa52551850756744e189beb447fc2c48/LICENSE) · [package.json](https://github.com/mastodon/mastodon/blob/47c3a7dafa52551850756744e189beb447fc2c48/package.json) · [.github/workflows/test-js.yml](https://github.com/mastodon/mastodon/blob/47c3a7dafa52551850756744e189beb447fc2c48/.github/workflows/test-js.yml).

<a id="anhkysuai-calcom-cal.diy"></a>

### Cal.diy

**Repo:** [calcom/cal.diy](https://github.com/calcom/cal.diy) · **License:** MIT · **Kiểm:** 2026-11-23, `docs-read`, [`ae027bb70e69`](https://github.com/calcom/cal.diy/tree/ae027bb70e694e2d2c44569f398d6cbcee0389b1) (commit 2026-11-13). **Sao:** 50,329 tại 2026-11-23 theo [GitHub API](https://api.github.com/repos/calcom/cal.diy).

| Mục | Đánh giá |
|---|---|
| Mục đích | Bản cộng đồng tự host cho đặt lịch, tách khỏi các tính năng thương mại của Cal.com. |
| Giá trị và cơ chế theo tài liệu | README nêu rõ đã bỏ Teams, Organizations, Insights, Workflows và SSO/SAML; LICENSE MIT khớp mô tả phạm vi cộng đồng. |
| Giới hạn | Tác giả khuyến cáo dùng cá nhân, không production. Không suy chức năng Enterprise hoặc độ sẵn sàng của Cal.com sang Cal.diy. |
| Điều kiện tích hợp | Thử riêng luồng đặt lịch, múi giờ, lịch ngoài và OAuth; dùng Cal.com hoặc sản phẩm phù hợp nếu cần điều kiện vận hành thương mại đã hỗ trợ. |
| Lựa chọn đối chiếu | Cal.com; Easy!Appointments; Rallly. |

**Phạm vi bằng chứng:** đã clone, đọc trích đoạn tài liệu, giấy phép và các file cấu hình được dẫn dưới đây; chưa chạy mã, build, benchmark hoặc test upstream. `docs-read` không phải kiểm chứng implementation.

**Nguồn tại cùng SHA:** [README.md](https://github.com/calcom/cal.diy/blob/ae027bb70e694e2d2c44569f398d6cbcee0389b1/README.md) · [LICENSE](https://github.com/calcom/cal.diy/blob/ae027bb70e694e2d2c44569f398d6cbcee0389b1/LICENSE) · [package.json](https://github.com/calcom/cal.diy/blob/ae027bb70e694e2d2c44569f398d6cbcee0389b1/package.json) · [.github/workflows/run-ci.yml](https://github.com/calcom/cal.diy/blob/ae027bb70e694e2d2c44569f398d6cbcee0389b1/.github/workflows/run-ci.yml).

<a id="anhkysuai-discourse-discourse"></a>

### Discourse

**Repo:** [discourse/discourse](https://github.com/discourse/discourse) · **License:** GPL-2.0; COPYRIGHT.md ghi or-later, package.json ghi only · **Kiểm:** 2026-11-23, `docs-read`, [`a672f97a50b3`](https://github.com/discourse/discourse/tree/a672f97a50b352e3ff18caccb6a4cf89c53d115f) (commit 2026-11-23). **Sao:** 48,108 tại 2026-11-23 theo [GitHub API](https://api.github.com/repos/discourse/discourse).

| Mục | Đánh giá |
|---|---|
| Mục đích | Nền tảng cộng đồng với chủ đề thảo luận, chat, theme và plugin. |
| Giá trị và cơ chế theo tài liệu | README nêu các hướng self-host và plugin AI/Data Explorer; workflow Tests phân tách core, plugin và chat. |
| Giới hạn | Có bất nhất giữa thông báo COPYRIGHT cho phép GPLv2-or-later và package.json ghi GPLv2-only; giữ rõ hai nguồn thay vì tự kết luận. Chưa kiểm plugin bên ngoài hoặc vận hành mail. |
| Điều kiện tích hợp | Dùng quy trình triển khai được hỗ trợ, thử backup và plugin trên staging; kiểm phạm vi giấy phép của mã định tái sử dụng. |
| Lựa chọn đối chiếu | Flarum; NodeBB; [Zulip](../21-autonomous-workflows/README.md#anhkysuai-zulip-zulip). |

**Phạm vi bằng chứng:** đã clone, đọc trích đoạn tài liệu, giấy phép và các file cấu hình được dẫn dưới đây; chưa chạy mã, build, benchmark hoặc test upstream. `docs-read` không phải kiểm chứng implementation.

**Nguồn tại cùng SHA:** [README.md](https://github.com/discourse/discourse/blob/a672f97a50b352e3ff18caccb6a4cf89c53d115f/README.md) · [COPYRIGHT.md](https://github.com/discourse/discourse/blob/a672f97a50b352e3ff18caccb6a4cf89c53d115f/COPYRIGHT.md) · [LICENSE.txt](https://github.com/discourse/discourse/blob/a672f97a50b352e3ff18caccb6a4cf89c53d115f/LICENSE.txt) · [package.json](https://github.com/discourse/discourse/blob/a672f97a50b352e3ff18caccb6a4cf89c53d115f/package.json) · [.github/workflows/tests.yml](https://github.com/discourse/discourse/blob/a672f97a50b352e3ff18caccb6a4cf89c53d115f/.github/workflows/tests.yml).

<a id="anhkysuai-rocketchat-rocket.chat"></a>

### Rocket.Chat

**Repo:** [RocketChat/Rocket.Chat](https://github.com/RocketChat/Rocket.Chat) · **License:** MIT; thư mục ee theo giấy phép thương mại riêng · **Kiểm:** 2026-11-23, `docs-read`, [`62e0e5ac583d`](https://github.com/RocketChat/Rocket.Chat/tree/62e0e5ac583d64690b8ac18a5834a18b50f4b0d7) (commit 2026-11-20). **Sao:** 46,603 tại 2026-11-23 theo [GitHub API](https://api.github.com/repos/RocketChat/Rocket.Chat).

| Mục | Đánh giá |
|---|---|
| Mục đích | Nền tảng liên lạc nhóm có thể tự host, mở rộng bằng ứng dụng và tích hợp. |
| Giá trị và cơ chế theo tài liệu | README phân nhóm deployment, collaboration và Apps-Engine; manifest và CI cho thấy monorepo TypeScript với các lớp kiểm khác nhau. |
| Giới hạn | Các tuyên bố an toàn/E2EE cần kiểm theo cấu hình; LICENSE tách apps/meteor/ee và ee khỏi MIT. Nhánh đã đọc là bản phát triển, chưa thử call/federation. |
| Điều kiện tích hợp | Chọn bản phát hành, đối chiếu tính năng CE/EE; thử SSO, quyền, lưu trữ và phục hồi trước khi thay hệ liên lạc hiện tại. |
| Lựa chọn đối chiếu | [Mattermost](../21-autonomous-workflows/README.md#anhkysuai-mattermost-mattermost); [Zulip](../21-autonomous-workflows/README.md#anhkysuai-zulip-zulip); Matrix/Element. |

**Phạm vi bằng chứng:** đã clone, đọc trích đoạn tài liệu, giấy phép và các file cấu hình được dẫn dưới đây; chưa chạy mã, build, benchmark hoặc test upstream. `docs-read` không phải kiểm chứng implementation.

**Nguồn tại cùng SHA:** [README.md](https://github.com/RocketChat/Rocket.Chat/blob/62e0e5ac583d64690b8ac18a5834a18b50f4b0d7/README.md) · [LICENSE](https://github.com/RocketChat/Rocket.Chat/blob/62e0e5ac583d64690b8ac18a5834a18b50f4b0d7/LICENSE) · [package.json](https://github.com/RocketChat/Rocket.Chat/blob/62e0e5ac583d64690b8ac18a5834a18b50f4b0d7/package.json) · [.github/workflows/ci.yml](https://github.com/RocketChat/Rocket.Chat/blob/62e0e5ac583d64690b8ac18a5834a18b50f4b0d7/.github/workflows/ci.yml).

<a id="anhkysuai-gitroomhq-postiz-app"></a>

### Postiz

**Repo:** [gitroomhq/postiz-app](https://github.com/gitroomhq/postiz-app) · **License:** AGPL-3.0 · **Kiểm:** 2026-11-23, `docs-read`, [`ab9eb87d6283`](https://github.com/gitroomhq/postiz-app/tree/ab9eb87d628303f0df0fa0b44cb766dda9c27604) (commit 2026-11-23). **Sao:** 42,201 tại 2026-11-23 theo [GitHub API](https://api.github.com/repos/gitroomhq/postiz-app).

| Mục | Đánh giá |
|---|---|
| Mục đích | Ứng dụng lập lịch và quản lý xuất bản nội dung trên các kênh mạng xã hội. |
| Giá trị và cơ chế theo tài liệu | Monorepo tách backend, frontend, orchestrator, extension và SDK; README cùng workflow build cung cấp điểm bắt đầu cho triển khai tự quản. |
| Giới hạn | Mỗi kênh cần quyền API và giới hạn riêng; tài liệu không chứng minh mọi tích hợp luôn hoạt động. Chưa đăng nội dung, kiểm OAuth hoặc phục hồi lịch gửi thất bại. |
| Điều kiện tích hợp | Thử bằng tài khoản và nội dung nháp, kiểm múi giờ, token và retry; chỉ cấp quyền cần thiết và theo dõi trạng thái xuất bản. |
| Lựa chọn đối chiếu | Mixpost; Buffer; Hootsuite. |

**Phạm vi bằng chứng:** đã clone, đọc trích đoạn tài liệu, giấy phép và các file cấu hình được dẫn dưới đây; chưa chạy mã, build, benchmark hoặc test upstream. `docs-read` không phải kiểm chứng implementation.

**Nguồn tại cùng SHA:** [README.md](https://github.com/gitroomhq/postiz-app/blob/ab9eb87d628303f0df0fa0b44cb766dda9c27604/README.md) · [LICENSE](https://github.com/gitroomhq/postiz-app/blob/ab9eb87d628303f0df0fa0b44cb766dda9c27604/LICENSE) · [package.json](https://github.com/gitroomhq/postiz-app/blob/ab9eb87d628303f0df0fa0b44cb766dda9c27604/package.json) · [.github/workflows/build.yml](https://github.com/gitroomhq/postiz-app/blob/ab9eb87d628303f0df0fa0b44cb766dda9c27604/.github/workflows/build.yml).

<a id="anhkysuai-novuhq-novu"></a>

### Novu

**Repo:** [novuhq/novu](https://github.com/novuhq/novu) · **License:** MIT và Enterprise theo phạm vi gói/thư mục · **Kiểm:** 2026-11-23, `docs-read`, [`31d684d3404f`](https://github.com/novuhq/novu/tree/31d684d3404f4fd3bda55566811b3dbc8b9892e2) (commit 2026-11-23). **Sao:** 40,412 tại 2026-11-23 theo [GitHub API](https://api.github.com/repos/novuhq/novu).

| Mục | Đánh giá |
|---|---|
| Mục đích | Hạ tầng điều phối thông báo và hội thoại qua inbox, email, SMS, push và chat. |
| Giá trị và cơ chế theo tài liệu | README mô tả workflow, digest, webhook và inbox nhúng; monorepo tách API, worker, WebSocket và giao diện quản trị. |
| Giới hạn | Kho có LICENSE-MIT, LICENSE-ENTERPRISE và quy định gói EE; không coi toàn bộ tính năng là MIT. Chưa kiểm giao hàng, đồng ý nhận tin hoặc lỗi nhà cung cấp. |
| Điều kiện tích hợp | Thử một workflow với provider sandbox, định nghĩa dedup/retry và preference của người nhận; kiểm ranh giới CE/EE, secrets và retention sự kiện. |
| Lựa chọn đối chiếu | Knock; Courier; [ntfy](../21-autonomous-workflows/README.md#anhkysuai-binwiederhier-ntfy). |

**Phạm vi bằng chứng:** đã clone, đọc trích đoạn tài liệu, giấy phép và các file cấu hình được dẫn dưới đây; chưa chạy mã, build, benchmark hoặc test upstream. `docs-read` không phải kiểm chứng implementation.

**Nguồn tại cùng SHA:** [README.md](https://github.com/novuhq/novu/blob/31d684d3404f4fd3bda55566811b3dbc8b9892e2/README.md) · [LICENSE-ENTERPRISE](https://github.com/novuhq/novu/blob/31d684d3404f4fd3bda55566811b3dbc8b9892e2/LICENSE-ENTERPRISE) · [LICENSE-MIT](https://github.com/novuhq/novu/blob/31d684d3404f4fd3bda55566811b3dbc8b9892e2/LICENSE-MIT) · [package.json](https://github.com/novuhq/novu/blob/31d684d3404f4fd3bda55566811b3dbc8b9892e2/package.json) · [.github/workflows/check-only.yml](https://github.com/novuhq/novu/blob/31d684d3404f4fd3bda55566811b3dbc8b9892e2/.github/workflows/check-only.yml).

<a id="anhkysuai-chatwoot-chatwoot"></a>

### Chatwoot

**Repo:** [chatwoot/chatwoot](https://github.com/chatwoot/chatwoot) · **License:** MIT ngoài phạm vi enterprise; enterprise có điều khoản riêng · **Kiểm:** 2026-11-23, `docs-read`, [`14b264e9498b`](https://github.com/chatwoot/chatwoot/tree/14b264e9498b4084f588eca30085ea6806131b6f) (commit 2026-11-23). **Sao:** 40,392 tại 2026-11-23 theo [GitHub API](https://api.github.com/repos/chatwoot/chatwoot).

| Mục | Đánh giá |
|---|---|
| Mục đích | Hộp thư hỗ trợ khách hàng gom nhiều kênh và trung tâm trợ giúp. |
| Giá trị và cơ chế theo tài liệu | README mô tả inbox, phân công, nhãn, ghi chú và các kênh liên lạc; manifest Ruby/Vue cùng runtime giúp đánh giá cách tự host. |
| Giới hạn | Captain AI và các tuyên bố tự động xử lý chưa được kiểm. LICENSE tách enterprise; quyền API, lưu dữ liệu khách hàng và giới hạn nhà cung cấp vẫn cần quản lý. |
| Điều kiện tích hợp | Thử một kênh với dữ liệu giả lập, chốt phân quyền, retention và chuyển giao cho người; kiểm tính năng CE/EE trước khi thay helpdesk. |
| Lựa chọn đối chiếu | Zammad; FreeScout; Zendesk. |

**Phạm vi bằng chứng:** đã clone, đọc trích đoạn tài liệu, giấy phép và các file cấu hình được dẫn dưới đây; chưa chạy mã, build, benchmark hoặc test upstream. `docs-read` không phải kiểm chứng implementation.

**Nguồn tại cùng SHA:** [README.md](https://github.com/chatwoot/chatwoot/blob/14b264e9498b4084f588eca30085ea6806131b6f/README.md) · [LICENSE](https://github.com/chatwoot/chatwoot/blob/14b264e9498b4084f588eca30085ea6806131b6f/LICENSE) · [package.json](https://github.com/chatwoot/chatwoot/blob/14b264e9498b4084f588eca30085ea6806131b6f/package.json) · [.github/workflows/deploy_check.yml](https://github.com/chatwoot/chatwoot/blob/14b264e9498b4084f588eca30085ea6806131b6f/.github/workflows/deploy_check.yml).

<a id="anhkysuai-mattermost-mattermost"></a>

### Mattermost

**Repo:** [mattermost/mattermost](https://github.com/mattermost/mattermost) · **License:** AGPL-3.0 hoặc thương mại cho source; Apache-2.0 cho phần chỉ định; enterprise riêng · **Kiểm:** 2026-11-23, `docs-read`, [`72bef7f84497`](https://github.com/mattermost/mattermost/tree/72bef7f84497e86c6000500571284e5e30ac2d78) (commit 2026-11-23). **Sao:** 39,694 tại 2026-11-23 theo [GitHub API](https://api.github.com/repos/mattermost/mattermost).

| Mục | Đánh giá |
|---|---|
| Mục đích | Nền tảng liên lạc và workflow nhóm có thể tự triển khai. |
| Giá trị và cơ chế theo tài liệu | README mô tả ứng dụng Go/React với PostgreSQL, chat và tích hợp; LICENSE phân tách nguồn, công cụ quản trị và bản binary do nhà cung cấp phát hành. |
| Giới hạn | MIT dành cho binary chính thức không có nghĩa toàn bộ mã nguồn MIT. Các khả năng call, AI, compliance và enterprise chưa được kiểm theo edition. |
| Điều kiện tích hợp | Chọn đúng edition và hình thức phân phối, thử tích hợp cùng phân quyền; kiểm lưu media, backup/restore và nghĩa vụ giấy phép trước khi sửa source. |
| Lựa chọn đối chiếu | [Zulip](../21-autonomous-workflows/README.md#anhkysuai-zulip-zulip); [Rocket.Chat](../21-autonomous-workflows/README.md#anhkysuai-rocketchat-rocket.chat); Matrix/Element. |

**Phạm vi bằng chứng:** đã clone, đọc trích đoạn tài liệu, giấy phép và các file cấu hình được dẫn dưới đây; chưa chạy mã, build, benchmark hoặc test upstream. `docs-read` không phải kiểm chứng implementation.

**Nguồn tại cùng SHA:** [README.md](https://github.com/mattermost/mattermost/blob/72bef7f84497e86c6000500571284e5e30ac2d78/README.md) · [LICENSE.enterprise](https://github.com/mattermost/mattermost/blob/72bef7f84497e86c6000500571284e5e30ac2d78/LICENSE.enterprise) · [LICENSE.txt](https://github.com/mattermost/mattermost/blob/72bef7f84497e86c6000500571284e5e30ac2d78/LICENSE.txt) · [.github/workflows/docs-ci.yaml](https://github.com/mattermost/mattermost/blob/72bef7f84497e86c6000500571284e5e30ac2d78/.github/workflows/docs-ci.yaml).

<a id="anhkysuai-rssnext-folo"></a>

### Folo

**Repo:** [RSSNext/Folo](https://github.com/RSSNext/Folo) · **License:** AGPL-3.0-only; icons/mgc không được phân phối lại · **Kiểm:** 2026-11-23, `docs-read`, [`292d15d94f9e`](https://github.com/RSSNext/Folo/tree/292d15d94f9e7680899e1e2567c1c0d48a423f48) (commit 2026-11-19). **Sao:** 39,338 tại 2026-11-23 theo [GitHub API](https://api.github.com/repos/RSSNext/Folo).

| Mục | Đánh giá |
|---|---|
| Mục đích | Trình đọc RSS đa nền tảng gom blog, tin tức, podcast, video và nguồn xã hội. |
| Giá trị và cơ chế theo tài liệu | README mô tả đồng bộ subscriptions/read status, tóm tắt và dịch bằng AI; monorepo có workflow build iOS với Expo. |
| Giới hạn | LICENSE loại trừ quyền phân phối lại icons/mgc. Các nền tảng và khả năng AI mới được đọc từ tài liệu; chưa thử đồng bộ hoặc kiểm dữ liệu gửi đến dịch vụ AI. |
| Điều kiện tích hợp | Dùng bộ feed thử, kiểm import/export và quyền riêng tư; phân biệt ứng dụng client với dịch vụ đồng bộ và xử lý AI trước khi tự host hoặc fork. |
| Lựa chọn đối chiếu | FreshRSS; Miniflux; NewsBlur. |

**Phạm vi bằng chứng:** đã clone, đọc trích đoạn tài liệu, giấy phép và các file cấu hình được dẫn dưới đây; chưa chạy mã, build, benchmark hoặc test upstream. `docs-read` không phải kiểm chứng implementation.

**Nguồn tại cùng SHA:** [README.md](https://github.com/RSSNext/Folo/blob/292d15d94f9e7680899e1e2567c1c0d48a423f48/README.md) · [LICENSE](https://github.com/RSSNext/Folo/blob/292d15d94f9e7680899e1e2567c1c0d48a423f48/LICENSE) · [package.json](https://github.com/RSSNext/Folo/blob/292d15d94f9e7680899e1e2567c1c0d48a423f48/package.json) · [.github/workflows/build-ios.yml](https://github.com/RSSNext/Folo/blob/292d15d94f9e7680899e1e2567c1c0d48a423f48/.github/workflows/build-ios.yml).

<a id="anhkysuai-binwiederhier-ntfy"></a>

### ntfy

**Repo:** [binwiederhier/ntfy](https://github.com/binwiederhier/ntfy) · **License:** Apache-2.0 OR GPL-2.0; tài nguyên bên thứ ba riêng · **Kiểm:** 2026-11-23, `docs-read`, [`e33bf6c8293d`](https://github.com/binwiederhier/ntfy/tree/e33bf6c8293d7e8315c7fb5b5b478190baacc9cb) (commit 2026-11-22). **Sao:** 35,703 tại 2026-11-23 theo [GitHub API](https://api.github.com/repos/binwiederhier/ntfy).

| Mục | Đánh giá |
|---|---|
| Mục đích | Dịch vụ thông báo pub/sub qua HTTP PUT/POST cho điện thoại và máy tính. |
| Giá trị và cơ chế theo tài liệu | README phân biệt instance tự host, dịch vụ ntfy.sh và các app di động riêng; go.mod cùng CI build tài liệu/kiểm giúp tìm đường tích hợp script. |
| Giới hạn | Không đăng ký ở ví dụ công cộng không đồng nghĩa topic riêng tư. Chưa kiểm ACL, lưu bền, push delivery hay giới hạn thuê bao; README xác nhận dual license, còn âm thanh/tài nguyên mang điều khoản riêng. |
| Điều kiện tích hợp | Tạo topic và tài khoản thử, cấu hình xác thực/quyền cùng rate limit; tránh gửi bí mật trong nội dung và kiểm hành vi khi thiết bị mất kết nối. |
| Lựa chọn đối chiếu | Gotify; [Novu](../21-autonomous-workflows/README.md#anhkysuai-novuhq-novu); Apprise. |

**Phạm vi bằng chứng:** đã clone, đọc trích đoạn tài liệu, giấy phép và các file cấu hình được dẫn dưới đây; chưa chạy mã, build, benchmark hoặc test upstream. `docs-read` không phải kiểm chứng implementation.

**Nguồn tại cùng SHA:** [README.md](https://github.com/binwiederhier/ntfy/blob/e33bf6c8293d7e8315c7fb5b5b478190baacc9cb/README.md) · [LICENSE](https://github.com/binwiederhier/ntfy/blob/e33bf6c8293d7e8315c7fb5b5b478190baacc9cb/LICENSE) · [LICENSE.GPLv2](https://github.com/binwiederhier/ntfy/blob/e33bf6c8293d7e8315c7fb5b5b478190baacc9cb/LICENSE.GPLv2) · [go.mod](https://github.com/binwiederhier/ntfy/blob/e33bf6c8293d7e8315c7fb5b5b478190baacc9cb/go.mod) · [.github/workflows/test.yaml](https://github.com/binwiederhier/ntfy/blob/e33bf6c8293d7e8315c7fb5b5b478190baacc9cb/.github/workflows/test.yaml).

<a id="anhkysuai-karakeep-app-karakeep"></a>

### Karakeep

**Repo:** [karakeep-app/karakeep](https://github.com/karakeep-app/karakeep) · **License:** AGPL-3.0 · **Kiểm:** 2026-11-23, `docs-read`, [`85695fa3ec6a`](https://github.com/karakeep-app/karakeep/tree/85695fa3ec6a0f6e4a3c85c82b55ab98ebcbfb08) (commit 2026-11-22). **Sao:** 30,785 tại 2026-11-23 theo [GitHub API](https://api.github.com/repos/karakeep-app/karakeep).

| Mục | Đánh giá |
|---|---|
| Mục đích | Ứng dụng lưu bookmark, ghi chú, ảnh/PDF với tìm kiếm và phân loại bằng AI. |
| Giá trị và cơ chế theo tài liệu | README xác nhận tên cũ Hoarder, mô tả REST API/CLI, rule engine, OCR và lưu trang; monorepo có worker và migration queue riêng. |
| Giới hạn | Lưu trữ trang/video phụ thuộc công cụ ngoài và nội dung nguồn. Chưa đo tìm kiếm/OCR hay kiểm dữ liệu đưa vào LLM; bản sao bookmark không tự là archive đầy đủ. |
| Điều kiện tích hợp | Thử bộ liên kết đa dạng, chọn model/local provider phù hợp và kiểm quyền chia sẻ; sao lưu cả database, tệp và dữ liệu worker. |
| Lựa chọn đối chiếu | [Linkwarden](../21-autonomous-workflows/README.md#anhkysuai-linkwarden-linkwarden); [ArchiveBox](../11-browser-computer-use-sandbox/README.md#anhkysuai-archivebox-archivebox); Linkding. |

**Phạm vi bằng chứng:** đã clone, đọc trích đoạn tài liệu, giấy phép và các file cấu hình được dẫn dưới đây; chưa chạy mã, build, benchmark hoặc test upstream. `docs-read` không phải kiểm chứng implementation.

**Nguồn tại cùng SHA:** [README.md](https://github.com/karakeep-app/karakeep/blob/85695fa3ec6a0f6e4a3c85c82b55ab98ebcbfb08/README.md) · [LICENSE](https://github.com/karakeep-app/karakeep/blob/85695fa3ec6a0f6e4a3c85c82b55ab98ebcbfb08/LICENSE) · [package.json](https://github.com/karakeep-app/karakeep/blob/85695fa3ec6a0f6e4a3c85c82b55ab98ebcbfb08/package.json) · [.github/workflows/ci.yml](https://github.com/karakeep-app/karakeep/blob/85695fa3ec6a0f6e4a3c85c82b55ab98ebcbfb08/.github/workflows/ci.yml).

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

<a id="anhkysuai-celery-celery"></a>

### Celery

**Repo:** [celery/celery](https://github.com/celery/celery) · **License:** BSD-3-Clause · **Kiểm:** 2026-11-23, `docs-read`, [`c5742e22c99f`](https://github.com/celery/celery/tree/c5742e22c99f82f03b07945e9e08566d8b4714fa) (commit 2026-11-23). **Sao:** 29,262 tại 2026-11-23 theo [GitHub API](https://api.github.com/repos/celery/celery).

| Mục | Đánh giá |
|---|---|
| Mục đích | Task queue phân tán cho công việc nền trong hệ Python. |
| Giá trị và cơ chế theo tài liệu | README mô tả giao thức nhiều ngôn ngữ và phiên bản Python hỗ trợ; license xác nhận BSD-3-Clause, CI smoke tests dựng môi trường broker/container. |
| Giới hạn | Hàng đợi không tự bảo đảm tác vụ chạy đúng một lần. Broker, result backend, ack và retry quyết định hành vi lỗi; chưa kiểm mất worker hay tải thực tế. |
| Điều kiện tích hợp | Chọn broker/backend được hỗ trợ, viết task idempotent và timeout; thử retry, duplicate, shutdown và quan sát backlog trước khi chuyển việc nền quan trọng. |
| Lựa chọn đối chiếu | RQ; Dramatiq; Temporal. |

**Phạm vi bằng chứng:** đã clone, đọc trích đoạn tài liệu, giấy phép và các file cấu hình được dẫn dưới đây; chưa chạy mã, build, benchmark hoặc test upstream. `docs-read` không phải kiểm chứng implementation.

**Nguồn tại cùng SHA:** [README.rst](https://github.com/celery/celery/blob/c5742e22c99f82f03b07945e9e08566d8b4714fa/README.rst) · [LICENSE](https://github.com/celery/celery/blob/c5742e22c99f82f03b07945e9e08566d8b4714fa/LICENSE) · [pyproject.toml](https://github.com/celery/celery/blob/c5742e22c99f82f03b07945e9e08566d8b4714fa/pyproject.toml) · [.github/workflows/smoke-tests.yml](https://github.com/celery/celery/blob/c5742e22c99f82f03b07945e9e08566d8b4714fa/.github/workflows/smoke-tests.yml).

<a id="anhkysuai-zulip-zulip"></a>

### Zulip

**Repo:** [zulip/zulip](https://github.com/zulip/zulip) · **License:** Apache-2.0 · **Kiểm:** 2026-11-23, `docs-read`, [`7bb11b60d91d`](https://github.com/zulip/zulip/tree/7bb11b60d91def4644f6c74be6611fcc85488b06) (commit 2026-11-22). **Sao:** 26,291 tại 2026-11-23 theo [GitHub API](https://api.github.com/repos/zulip/zulip).

| Mục | Đánh giá |
|---|---|
| Mục đích | Ứng dụng chat nhóm tổ chức hội thoại theo topic để hỗ trợ trao đổi trực tiếp và bất đồng bộ. |
| Giá trị và cơ chế theo tài liệu | README mô tả server/web app và tài liệu đóng góp; pyproject Django cùng CI nhiều Ubuntu/Debian/Python giúp đánh giá nền tự host. |
| Giới hạn | Các số liệu người dùng/contributor trong README không là kiểm chứng sức tải của đội riêng. Chưa chạy chat, search, notification hay migration; client di động có repo riêng. |
| Điều kiện tích hợp | Thử cách tổ chức topic với một nhóm, kiểm quyền và xuất dữ liệu; cấu hình mail/push, retention, backup/restore trước khi chuyển lịch sử trao đổi. |
| Lựa chọn đối chiếu | [Mattermost](../21-autonomous-workflows/README.md#anhkysuai-mattermost-mattermost); [Rocket.Chat](../21-autonomous-workflows/README.md#anhkysuai-rocketchat-rocket.chat); Matrix/Element. |

**Phạm vi bằng chứng:** đã clone, đọc trích đoạn tài liệu, giấy phép và các file cấu hình được dẫn dưới đây; chưa chạy mã, build, benchmark hoặc test upstream. `docs-read` không phải kiểm chứng implementation.

**Nguồn tại cùng SHA:** [README.md](https://github.com/zulip/zulip/blob/7bb11b60d91def4644f6c74be6611fcc85488b06/README.md) · [LICENSE](https://github.com/zulip/zulip/blob/7bb11b60d91def4644f6c74be6611fcc85488b06/LICENSE) · [package.json](https://github.com/zulip/zulip/blob/7bb11b60d91def4644f6c74be6611fcc85488b06/package.json) · [pyproject.toml](https://github.com/zulip/zulip/blob/7bb11b60d91def4644f6c74be6611fcc85488b06/pyproject.toml) · [.github/workflows/zulip-ci.yml](https://github.com/zulip/zulip/blob/7bb11b60d91def4644f6c74be6611fcc85488b06/.github/workflows/zulip-ci.yml).

<a id="anhkysuai-knadh-listmonk"></a>

### listmonk

**Repo:** [knadh/listmonk](https://github.com/knadh/listmonk) · **License:** AGPL-3.0 · **Kiểm:** 2026-11-23, `docs-read`, [`6242fd857bc0`](https://github.com/knadh/listmonk/tree/6242fd857bc0e9ed106e8dfc59d2328f9ec7363b) (commit 2026-11-22). **Sao:** 24,430 tại 2026-11-23 theo [GitHub API](https://api.github.com/repos/knadh/listmonk).

| Mục | Đánh giá |
|---|---|
| Mục đích | Trình quản lý newsletter và mailing list tự host dùng Go/Vue/PostgreSQL. |
| Giá trị và cơ chế theo tài liệu | README mô tả single binary, Compose và lệnh install/upgrade; workflow build sanity cung cấp cách đóng gói sản phẩm độc lập. |
| Giới hạn | Tuyên bố upgrade idempotent chưa được thử. Gửi thư còn phụ thuộc nhà cung cấp SMTP, danh sách đồng ý nhận và deliverability; chưa gửi email hay đo throughput. |
| Điều kiện tích hợp | Thử với danh sách nội bộ đã đồng ý, xác minh unsubscribe/bounce và template; quản lý SMTP credentials, rate limit, backup database và đường nâng cấp. |
| Lựa chọn đối chiếu | Mautic; Keila; Mailtrain. |

**Phạm vi bằng chứng:** đã clone, đọc trích đoạn tài liệu, giấy phép và các file cấu hình được dẫn dưới đây; chưa chạy mã, build, benchmark hoặc test upstream. `docs-read` không phải kiểm chứng implementation.

**Nguồn tại cùng SHA:** [README.md](https://github.com/knadh/listmonk/blob/6242fd857bc0e9ed106e8dfc59d2328f9ec7363b/README.md) · [LICENSE](https://github.com/knadh/listmonk/blob/6242fd857bc0e9ed106e8dfc59d2328f9ec7363b/LICENSE) · [go.mod](https://github.com/knadh/listmonk/blob/6242fd857bc0e9ed106e8dfc59d2328f9ec7363b/go.mod) · [.github/workflows/build-sanity.yml](https://github.com/knadh/listmonk/blob/6242fd857bc0e9ed106e8dfc59d2328f9ec7363b/.github/workflows/build-sanity.yml).

<a id="anhkysuai-wekan-wekan"></a>

### WeKan

**Repo:** [wekan/wekan](https://github.com/wekan/wekan) · **License:** MIT · **Kiểm:** 2026-11-23, `docs-read`, [`938689d594a9`](https://github.com/wekan/wekan/tree/938689d594a9ee442ab89fe61fecc93639a7a837) (commit 2026-11-23). **Sao:** 21,174 tại 2026-11-23 theo [GitHub API](https://api.github.com/repos/wekan/wekan).

| Mục | Đánh giá |
|---|---|
| Mục đích | Ứng dụng bảng kanban cộng tác xây bằng Meteor. |
| Giá trị và cơ chế theo tài liệu | README mô tả self-host và các backend database/FerretDB; manifest có kiểm Node/e2e, CI đóng gói BSD với bước xác minh artifact. |
| Giới hạn | Độ phủ bản dịch không đồng nghĩa chất lượng dịch, README cũng phân biệt rõ điều này. Một số backend ghi thử nghiệm; chưa kiểm board permissions, đồng bộ hoặc upgrade database. |
| Điều kiện tích hợp | Chọn database được hỗ trợ ổn định, thử import/export và quyền board; kiểm attachment, mail, backup/restore cùng runtime phù hợp trước chuyển dữ liệu công việc. |
| Lựa chọn đối chiếu | Kanboard; Planka; [Plane](../28-product-discovery-experimentation/README.md#anhkysuai-makeplane-plane). |

**Phạm vi bằng chứng:** đã clone, đọc trích đoạn tài liệu, giấy phép và các file cấu hình được dẫn dưới đây; chưa chạy mã, build, benchmark hoặc test upstream. `docs-read` không phải kiểm chứng implementation.

**Nguồn tại cùng SHA:** [README.md](https://github.com/wekan/wekan/blob/938689d594a9ee442ab89fe61fecc93639a7a837/README.md) · [LICENSE](https://github.com/wekan/wekan/blob/938689d594a9ee442ab89fe61fecc93639a7a837/LICENSE) · [package.json](https://github.com/wekan/wekan/blob/938689d594a9ee442ab89fe61fecc93639a7a837/package.json) · [.github/workflows/bsd.yml](https://github.com/wekan/wekan/blob/938689d594a9ee442ab89fe61fecc93639a7a837/.github/workflows/bsd.yml).

<a id="anhkysuai-linkwarden-linkwarden"></a>

### Linkwarden

**Repo:** [linkwarden/linkwarden](https://github.com/linkwarden/linkwarden) · **License:** AGPL-3.0 · **Kiểm:** 2026-11-23, `docs-read`, [`24adcc146ba3`](https://github.com/linkwarden/linkwarden/tree/24adcc146ba356632859a1e8adb4bffae2874d11) (commit 2026-11-10). **Sao:** 20,508 tại 2026-11-23 theo [GitHub API](https://api.github.com/repos/linkwarden/linkwarden).

| Mục | Đánh giá |
|---|---|
| Mục đích | Trình quản lý bookmark cộng tác với đọc, chú thích và lưu ảnh/PDF của trang. |
| Giá trị và cơ chế theo tài liệu | README giải thích chống link rot và chia sẻ công khai/nhóm; workspace tách web/worker, CI điều phối unit/integration/e2e web/email/extension. |
| Giới hạn | Lưu screenshot/PDF không bảo đảm giữ toàn bộ nội dung động hay có đăng nhập. Chưa kiểm ACL, crawler, nhập/xuất hoặc khả năng restore; dịch vụ Cloud là phạm vi khác. |
| Điều kiện tích hợp | Thử nhiều loại URL và quyền collection, tách worker lấy trang khỏi dữ liệu nhạy cảm; backup database/artifact, kiểm quota và hành vi link hỏng. |
| Lựa chọn đối chiếu | [Karakeep](../21-autonomous-workflows/README.md#anhkysuai-karakeep-app-karakeep); [ArchiveBox](../11-browser-computer-use-sandbox/README.md#anhkysuai-archivebox-archivebox); Linkding. |

**Phạm vi bằng chứng:** đã clone, đọc trích đoạn tài liệu, giấy phép và các file cấu hình được dẫn dưới đây; chưa chạy mã, build, benchmark hoặc test upstream. `docs-read` không phải kiểm chứng implementation.

**Nguồn tại cùng SHA:** [README.md](https://github.com/linkwarden/linkwarden/blob/24adcc146ba356632859a1e8adb4bffae2874d11/README.md) · [LICENSE.md](https://github.com/linkwarden/linkwarden/blob/24adcc146ba356632859a1e8adb4bffae2874d11/LICENSE.md) · [package.json](https://github.com/linkwarden/linkwarden/blob/24adcc146ba356632859a1e8adb4bffae2874d11/package.json) · [.github/workflows/ci.yml](https://github.com/linkwarden/linkwarden/blob/24adcc146ba356632859a1e8adb4bffae2874d11/.github/workflows/ci.yml).

<a id="anhkysuai-mail-0-zero"></a>

### Zero Email

**Repo:** [Mail-0/Zero](https://github.com/Mail-0/Zero) · **License:** MIT · **Kiểm:** 2026-11-23, `docs-read`, [`4b642dfd9890`](https://github.com/Mail-0/Zero/tree/4b642dfd9890a1fdcb1b98a177fe74ca3142c445) (commit 2026-11-15). **Sao:** 10,898 tại 2026-11-23 theo [GitHub API](https://api.github.com/repos/Mail-0/Zero).

| Mục | Đánh giá |
|---|---|
| Mục đích | Ứng dụng email tự host gom provider ngoài và bổ sung hỗ trợ AI. |
| Giá trị và cơ chế theo tài liệu | README nêu Next.js/React, Node/Drizzle/PostgreSQL và Better Auth/Google OAuth; manifest tách frontend/server, CI chủ yếu lint. |
| Giới hạn | Tự host app không thay thế Gmail/Outlook hoặc chính sách model/provider. README thừa nhận dữ liệu gửi dịch vụ ngoài thuộc điều khoản của họ; chưa kiểm quyền OAuth, đồng bộ, gửi thư hay AI. |
| Điều kiện tích hợp | Thử tài khoản riêng với mail giả lập, hạn chế OAuth scope và model access; kiểm lưu token, xóa dữ liệu, backup và xác nhận thao tác gửi trước dùng thư thật. |
| Lựa chọn đối chiếu | Roundcube; SnappyMail; Thunderbird. |

**Phạm vi bằng chứng:** đã clone, đọc trích đoạn tài liệu, giấy phép và các file cấu hình được dẫn dưới đây; chưa chạy mã, build, benchmark hoặc test upstream. `docs-read` không phải kiểm chứng implementation.

**Nguồn tại cùng SHA:** [README.md](https://github.com/Mail-0/Zero/blob/4b642dfd9890a1fdcb1b98a177fe74ca3142c445/README.md) · [LICENSE](https://github.com/Mail-0/Zero/blob/4b642dfd9890a1fdcb1b98a177fe74ca3142c445/LICENSE) · [package.json](https://github.com/Mail-0/Zero/blob/4b642dfd9890a1fdcb1b98a177fe74ca3142c445/package.json) · [.github/workflows/ci.yml](https://github.com/Mail-0/Zero/blob/4b642dfd9890a1fdcb1b98a177fe74ca3142c445/.github/workflows/ci.yml).

<a id="anhkysuai-2026-11-23-hcengineering-platform"></a>

### Huly Platform

**Repo:** [hcengineering/platform](https://github.com/hcengineering/platform) · **License:** EPL-2.0 · **★ 28,174 (GitHub API, 2026-11-23)**

**Mục đích:** Huly Platform: nền tảng ứng dụng doanh nghiệp tích hợp quản lý dự án, chat, CRM và nhân sự.

**Giá trị:** Có giá trị tham khảo mô hình nhiều ứng dụng cùng nền tảng và tài liệu chuyển sang tự triển khai.

**Giới hạn:** README tại SHA nêu repo đã đóng băng, không còn duy trì chủ động và dịch vụ Hosted Huly đã ngừng. Chỉ nên cân nhắc với kế hoạch tự bảo trì, sao lưu và di chuyển dữ liệu.

**Cách tham khảo/tích hợp:** Thử với dự án mẫu, đối chiếu phân quyền, xuất dữ liệu và migration trước dùng quy trình hoặc dữ liệu công việc thật.

**Lựa chọn để đối chiếu:** [opf/openproject](https://github.com/opf/openproject) · [go-vikunja/vikunja](https://github.com/go-vikunja/vikunja). Đây là ứng viên so sánh theo tác vụ; mức phù hợp cần kiểm theo hồ sơ và phiên bản riêng.

**Bằng chứng:** `docs-read`, ngày 2026-11-23, commit [`a1dd19d4f7699e8b8d9e0dbeb610c7884b6255bc`](https://github.com/hcengineering/platform/commit/a1dd19d4f7699e8b8d9e0dbeb610c7884b6255bc), ngày commit 2026-11-09. Đã clone và đọc chọn lọc phần giới thiệu, cách dùng, giới hạn, license, metadata manifest và CI hiện diện. Chưa kiểm đầy đủ implementation hoặc chạy upstream; các số đo của tác giả chưa được tái lập.

**Nguồn:** [README.md](https://github.com/hcengineering/platform/blob/a1dd19d4f7699e8b8d9e0dbeb610c7884b6255bc/README.md) · [LICENSE](https://github.com/hcengineering/platform/blob/a1dd19d4f7699e8b8d9e0dbeb610c7884b6255bc/LICENSE) · [.github/workflows/main.yml](https://github.com/hcengineering/platform/blob/a1dd19d4f7699e8b8d9e0dbeb610c7884b6255bc/.github/workflows/main.yml) · [metadata GitHub](https://api.github.com/repos/hcengineering/platform).

<a id="anhkysuai-2026-11-23-opf-openproject"></a>

### openproject

**Repo:** [opf/openproject](https://github.com/opf/openproject) · **License:** GPL-3.0 · **★ 17,648 (GitHub API, 2026-11-23)**

**Mục đích:** Nền tảng quản lý dự án, danh mục, tác vụ, roadmap và cộng tác có thể tự host.

**Giá trị:** Phạm vi quản lý rộng phù hợp tổ chức cần quy trình nhiều dự án và quyền kiểm soát dữ liệu.

**Giới hạn:** Cần đối chiếu tính năng theo bản triển khai và chi phí vận hành; mã GPLv3, icon font có CC BY 3.0 riêng. Chưa kiểm migration, phân quyền hay tích hợp bằng chạy thử.

**Cách tham khảo/tích hợp:** Thử với dự án mẫu, đối chiếu phân quyền, xuất dữ liệu và migration trước dùng quy trình hoặc dữ liệu công việc thật.

**Lựa chọn để đối chiếu:** [go-vikunja/vikunja](https://github.com/go-vikunja/vikunja) · [Leantime/leantime](https://github.com/Leantime/leantime). Đây là ứng viên so sánh theo tác vụ; mức phù hợp cần kiểm theo hồ sơ và phiên bản riêng.

**Bằng chứng:** `docs-read`, ngày 2026-11-23, commit [`3a0f515d05258e83f938488f02c88429a0579706`](https://github.com/opf/openproject/commit/3a0f515d05258e83f938488f02c88429a0579706), ngày commit 2026-11-23. Đã clone và đọc chọn lọc phần giới thiệu, cách dùng, giới hạn, license, metadata manifest và CI hiện diện. Chưa kiểm đầy đủ implementation hoặc chạy upstream; các số đo của tác giả chưa được tái lập.

**Nguồn:** [README.md](https://github.com/opf/openproject/blob/3a0f515d05258e83f938488f02c88429a0579706/README.md) · [COPYRIGHT](https://github.com/opf/openproject/blob/3a0f515d05258e83f938488f02c88429a0579706/COPYRIGHT) · [COPYRIGHT_short](https://github.com/opf/openproject/blob/3a0f515d05258e83f938488f02c88429a0579706/COPYRIGHT_short) · [LICENSE](https://github.com/opf/openproject/blob/3a0f515d05258e83f938488f02c88429a0579706/LICENSE) · [package.json](https://github.com/opf/openproject/blob/3a0f515d05258e83f938488f02c88429a0579706/package.json) · [.github/workflows/test-core.yml](https://github.com/opf/openproject/blob/3a0f515d05258e83f938488f02c88429a0579706/.github/workflows/test-core.yml) · [metadata GitHub](https://api.github.com/repos/opf/openproject).

<a id="anhkysuai-2026-11-23-plankanban-planka"></a>

### planka

**Repo:** [plankanban/planka](https://github.com/plankanban/planka) · **License:** PLANKA Community License 1.1; Pro/Enterprise riêng · **★ 12,705 (GitHub API, 2026-11-23)**

**Mục đích:** Ứng dụng Kanban tự host theo dõi dự án và công việc nhóm, có bản Community và Pro.

**Giá trị:** Giao diện board và API phù hợp nhóm cần kiểm soát dữ liệu; README mô tả rõ nâng cấp Community sang Pro là migration thật.

**Giới hạn:** Community License cho dùng nội bộ nhưng hạn chế hosting thương mại cho bên thứ ba; tệp Pro/Enterprise cần license riêng, nên đây là fair-code chứ không phải quyền nguồn mở không hạn chế lĩnh vực.

**Cách tham khảo/tích hợp:** Thử với dự án mẫu, đối chiếu phân quyền, xuất dữ liệu và migration trước dùng quy trình hoặc dữ liệu công việc thật.

**Lựa chọn để đối chiếu:** [kanboard/kanboard](https://github.com/kanboard/kanboard) · [usekaneo/kaneo](https://github.com/usekaneo/kaneo). Đây là ứng viên so sánh theo tác vụ; mức phù hợp cần kiểm theo hồ sơ và phiên bản riêng.

**Bằng chứng:** `docs-read`, ngày 2026-11-23, commit [`2cf423824a09f84df7dc3acf0ded9a700292d882`](https://github.com/plankanban/planka/commit/2cf423824a09f84df7dc3acf0ded9a700292d882), ngày commit 2026-11-06. Đã clone và đọc chọn lọc phần giới thiệu, cách dùng, giới hạn, license, metadata manifest và CI hiện diện. Chưa kiểm đầy đủ implementation hoặc chạy upstream; các số đo của tác giả chưa được tái lập.

**Nguồn:** [README.md](https://github.com/plankanban/planka/blob/2cf423824a09f84df7dc3acf0ded9a700292d882/README.md) · [LICENSE.md](https://github.com/plankanban/planka/blob/2cf423824a09f84df7dc3acf0ded9a700292d882/LICENSE.md) · [package.json](https://github.com/plankanban/planka/blob/2cf423824a09f84df7dc3acf0ded9a700292d882/package.json) · [.github/workflows/build-and-test.yml](https://github.com/plankanban/planka/blob/2cf423824a09f84df7dc3acf0ded9a700292d882/.github/workflows/build-and-test.yml) · [metadata GitHub](https://api.github.com/repos/plankanban/planka).

<a id="anhkysuai-2026-11-23-leantime-leantime"></a>

### leantime

**Repo:** [Leantime/leantime](https://github.com/Leantime/leantime) · **License:** AGPL-3.0 (core); app/Plugins có license riêng · **★ 12,139 (GitHub API, 2026-11-23)**

**Mục đích:** Công cụ quản lý dự án gắn mục tiêu, chiến lược, kế hoạch và thực thi cho nhóm không chuyên PM.

**Giá trị:** Tập trung khả năng tiếp cận và kết nối mục tiêu với công việc, phù hợp thử quy trình quản lý nhẹ.

**Giới hạn:** Core AGPLv3 nhưng README loại trừ plugin trong app/Plugins có thể mang enterprise license; các tuyên bố phù hợp ADHD/autism/dyslexia là định hướng thiết kế, chưa được đánh giá hiệu quả ở đây.

**Cách tham khảo/tích hợp:** Thử với dự án mẫu, đối chiếu phân quyền, xuất dữ liệu và migration trước dùng quy trình hoặc dữ liệu công việc thật.

**Lựa chọn để đối chiếu:** [opf/openproject](https://github.com/opf/openproject) · [go-vikunja/vikunja](https://github.com/go-vikunja/vikunja). Đây là ứng viên so sánh theo tác vụ; mức phù hợp cần kiểm theo hồ sơ và phiên bản riêng.

**Bằng chứng:** `docs-read`, ngày 2026-11-23, commit [`e4763f16c36139bccdf03fc4e5b21edcd2774ac3`](https://github.com/Leantime/leantime/commit/e4763f16c36139bccdf03fc4e5b21edcd2774ac3), ngày commit 2026-11-22. Đã clone và đọc chọn lọc phần giới thiệu, cách dùng, giới hạn, license, metadata manifest và CI hiện diện. Chưa kiểm đầy đủ implementation hoặc chạy upstream; các số đo của tác giả chưa được tái lập.

**Nguồn:** [README.md](https://github.com/Leantime/leantime/blob/e4763f16c36139bccdf03fc4e5b21edcd2774ac3/README.md) · [LICENSE](https://github.com/Leantime/leantime/blob/e4763f16c36139bccdf03fc4e5b21edcd2774ac3/LICENSE) · [package.json](https://github.com/Leantime/leantime/blob/e4763f16c36139bccdf03fc4e5b21edcd2774ac3/package.json) · [composer.json](https://github.com/Leantime/leantime/blob/e4763f16c36139bccdf03fc4e5b21edcd2774ac3/composer.json) · [.github/workflows/unittests.yml](https://github.com/Leantime/leantime/blob/e4763f16c36139bccdf03fc4e5b21edcd2774ac3/.github/workflows/unittests.yml) · [metadata GitHub](https://api.github.com/repos/Leantime/leantime).

<a id="anhkysuai-2026-11-23-kanboard-kanboard"></a>

### kanboard

**Repo:** [kanboard/kanboard](https://github.com/kanboard/kanboard) · **License:** MIT · **★ 9,975 (GitHub API, 2026-11-23)**

**Mục đích:** Phần mềm quản lý dự án tập trung vào phương pháp Kanban.

**Giá trị:** Phạm vi gọn phù hợp nhóm muốn workflow bảng công việc thay vì bộ quản trị nhiều mô-đun.

**Giới hạn:** README công bố maintenance mode: tác giả chủ yếu sửa nhỏ, vẫn nhận đóng góp và có release; không nên kỳ vọng roadmap tính năng lớn do maintainer tự phát triển.

**Cách tham khảo/tích hợp:** Thử với dự án mẫu, đối chiếu phân quyền, xuất dữ liệu và migration trước dùng quy trình hoặc dữ liệu công việc thật.

**Lựa chọn để đối chiếu:** [plankanban/planka](https://github.com/plankanban/planka) · [usekaneo/kaneo](https://github.com/usekaneo/kaneo). Đây là ứng viên so sánh theo tác vụ; mức phù hợp cần kiểm theo hồ sơ và phiên bản riêng.

**Bằng chứng:** `docs-read`, ngày 2026-11-23, commit [`ee4e5ddd889c2408174cd9567f5cda7a831e2041`](https://github.com/kanboard/kanboard/commit/ee4e5ddd889c2408174cd9567f5cda7a831e2041), ngày commit 2026-11-22. Đã clone và đọc chọn lọc phần giới thiệu, cách dùng, giới hạn, license, metadata manifest và CI hiện diện. Chưa kiểm đầy đủ implementation hoặc chạy upstream; các số đo của tác giả chưa được tái lập.

**Nguồn:** [README.md](https://github.com/kanboard/kanboard/blob/ee4e5ddd889c2408174cd9567f5cda7a831e2041/README.md) · [LICENSE](https://github.com/kanboard/kanboard/blob/ee4e5ddd889c2408174cd9567f5cda7a831e2041/LICENSE) · [composer.json](https://github.com/kanboard/kanboard/blob/ee4e5ddd889c2408174cd9567f5cda7a831e2041/composer.json) · [.github/workflows/unit_tests.yml](https://github.com/kanboard/kanboard/blob/ee4e5ddd889c2408174cd9567f5cda7a831e2041/.github/workflows/unit_tests.yml) · [metadata GitHub](https://api.github.com/repos/kanboard/kanboard).

<a id="anhkysuai-2026-11-23-usekaneo-kaneo"></a>

### kaneo

**Repo:** [usekaneo/kaneo](https://github.com/usekaneo/kaneo) · **License:** MIT · **★ 9,867 (GitHub API, 2026-11-23)**

**Mục đích:** Quản lý dự án tự host với board, list, calendar, Gantt và kết nối GitHub/Gitea.

**Giá trị:** REST API, CLI và MCP được giới thiệu cùng workflow cập nhật theo hoạt động repo, hữu ích cho nhóm phát triển.

**Giới hạn:** Cần thử phân quyền, webhook, đồng bộ và migration trong môi trường riêng; MIT của mã không tự bao gồm điều khoản Kaneo Cloud hoặc dịch vụ tích hợp.

**Cách tham khảo/tích hợp:** Thử với dự án mẫu, đối chiếu phân quyền, xuất dữ liệu và migration trước dùng quy trình hoặc dữ liệu công việc thật.

**Lựa chọn để đối chiếu:** [go-vikunja/vikunja](https://github.com/go-vikunja/vikunja) · [kanboard/kanboard](https://github.com/kanboard/kanboard). Đây là ứng viên so sánh theo tác vụ; mức phù hợp cần kiểm theo hồ sơ và phiên bản riêng.

**Bằng chứng:** `docs-read`, ngày 2026-11-23, commit [`e46680d28a00be1173922ad065ca69243e30ab31`](https://github.com/usekaneo/kaneo/commit/e46680d28a00be1173922ad065ca69243e30ab31), ngày commit 2026-11-23. Đã clone và đọc chọn lọc phần giới thiệu, cách dùng, giới hạn, license, metadata manifest và CI hiện diện. Chưa kiểm đầy đủ implementation hoặc chạy upstream; các số đo của tác giả chưa được tái lập.

**Nguồn:** [README.md](https://github.com/usekaneo/kaneo/blob/e46680d28a00be1173922ad065ca69243e30ab31/README.md) · [LICENSE](https://github.com/usekaneo/kaneo/blob/e46680d28a00be1173922ad065ca69243e30ab31/LICENSE) · [package.json](https://github.com/usekaneo/kaneo/blob/e46680d28a00be1173922ad065ca69243e30ab31/package.json) · [.github/workflows/ci.yml](https://github.com/usekaneo/kaneo/blob/e46680d28a00be1173922ad065ca69243e30ab31/.github/workflows/ci.yml) · [metadata GitHub](https://api.github.com/repos/usekaneo/kaneo).

<a id="anhkysuai-2026-11-23-ahmadhassan-bted-jantt"></a>

### Jantt

**Repo:** [AhmadHassan-BTed/Jantt](https://github.com/AhmadHassan-BTed/Jantt) · **License:** MIT · **★ 6,239 (GitHub API, 2026-11-23)**

**Mục đích:** Công cụ/libraries Gantt tương tác có AI Copilot BYOK, nhiều view và tính lịch công việc.

**Giá trị:** Có hướng dùng qua web, framework và MCP, phù hợp nghiên cứu chuyển lịch tác vụ giữa giao diện và tự động hóa.

**Giới hạn:** Tuyên bố 100.000 task, 60 FPS và cloud miễn phí là thông tin upstream chưa đo lại; cần kiểm thuật toán critical path, múi giờ, lịch làm việc và dữ liệu gửi nhà cung cấp AI.

**Cách tham khảo/tích hợp:** Thử với dự án mẫu, đối chiếu phân quyền, xuất dữ liệu và migration trước dùng quy trình hoặc dữ liệu công việc thật.

**Lựa chọn để đối chiếu:** [frappe/gantt](https://github.com/frappe/gantt) · [usekaneo/kaneo](https://github.com/usekaneo/kaneo). Đây là ứng viên so sánh theo tác vụ; mức phù hợp cần kiểm theo hồ sơ và phiên bản riêng.

**Bằng chứng:** `docs-read`, ngày 2026-11-23, commit [`49407b4a4e33c6b238a813442b5d988f6ac95f99`](https://github.com/AhmadHassan-BTed/Jantt/commit/49407b4a4e33c6b238a813442b5d988f6ac95f99), ngày commit 2026-11-23. Đã clone và đọc chọn lọc phần giới thiệu, cách dùng, giới hạn, license, metadata manifest và CI hiện diện. Chưa kiểm đầy đủ implementation hoặc chạy upstream; các số đo của tác giả chưa được tái lập.

**Nguồn:** [README.md](https://github.com/AhmadHassan-BTed/Jantt/blob/49407b4a4e33c6b238a813442b5d988f6ac95f99/README.md) · [LICENSE](https://github.com/AhmadHassan-BTed/Jantt/blob/49407b4a4e33c6b238a813442b5d988f6ac95f99/LICENSE) · [package.json](https://github.com/AhmadHassan-BTed/Jantt/blob/49407b4a4e33c6b238a813442b5d988f6ac95f99/package.json) · [.github/workflows/ci.yml](https://github.com/AhmadHassan-BTed/Jantt/blob/49407b4a4e33c6b238a813442b5d988f6ac95f99/.github/workflows/ci.yml) · [metadata GitHub](https://api.github.com/repos/AhmadHassan-BTed/Jantt).

<a id="anhkysuai-2026-11-23-frappe-gantt"></a>

### gantt

**Repo:** [frappe/gantt](https://github.com/frappe/gantt) · **License:** MIT · **★ 6,159 (GitHub API, 2026-11-23)**

**Mục đích:** Thư viện JavaScript vẽ biểu đồ Gantt có tùy chỉnh timeline và các khoảng thời gian bỏ qua.

**Giá trị:** Phù hợp nhúng lịch tác vụ nhẹ vào ứng dụng web, với API và cấu hình được ghi ngay trong README.

**Giới hạn:** Thư viện hiển thị không tự cung cấp hệ quản lý dự án hay bảo đảm tính lịch phức tạp; cần kiểm phụ thuộc task, múi giờ và hiệu năng với số lượng mục thực tế.

**Cách tham khảo/tích hợp:** Thử với dự án mẫu, đối chiếu phân quyền, xuất dữ liệu và migration trước dùng quy trình hoặc dữ liệu công việc thật.

**Lựa chọn để đối chiếu:** [AhmadHassan-BTed/Jantt](https://github.com/AhmadHassan-BTed/Jantt) · [visjs/vis-timeline](https://github.com/visjs/vis-timeline). Đây là ứng viên so sánh theo tác vụ; mức phù hợp cần kiểm theo hồ sơ và phiên bản riêng.

**Bằng chứng:** `docs-read`, ngày 2026-11-23, commit [`5c83708d300a99d9142edea0d4d52f421e3a2e68`](https://github.com/frappe/gantt/commit/5c83708d300a99d9142edea0d4d52f421e3a2e68), ngày commit 2026-03-05. Đã clone và đọc chọn lọc phần giới thiệu, cách dùng, giới hạn, license, metadata manifest và CI hiện diện. Chưa kiểm đầy đủ implementation hoặc chạy upstream; các số đo của tác giả chưa được tái lập.

**Nguồn:** [README.md](https://github.com/frappe/gantt/blob/5c83708d300a99d9142edea0d4d52f421e3a2e68/README.md) · [license.txt](https://github.com/frappe/gantt/blob/5c83708d300a99d9142edea0d4d52f421e3a2e68/license.txt) · [package.json](https://github.com/frappe/gantt/blob/5c83708d300a99d9142edea0d4d52f421e3a2e68/package.json) · [.github/workflows/publish.yml](https://github.com/frappe/gantt/blob/5c83708d300a99d9142edea0d4d52f421e3a2e68/.github/workflows/publish.yml) · [metadata GitHub](https://api.github.com/repos/frappe/gantt).

<a id="anhkysuai-2026-11-23-go-vikunja-vikunja"></a>

### Vikunja

**Repo:** [go-vikunja/vikunja](https://github.com/go-vikunja/vikunja) · **License:** AGPL-3.0-or-later (chính); GPL-3.0-or-later (desktop); ảnh riêng · **★ 6,147 (GitHub API, 2026-11-23)**

**Mục đích:** Ứng dụng quản lý công việc có thể tự host, kèm lựa chọn hosted và Pro.

**Giá trị:** Phù hợp cá nhân/nhóm muốn sở hữu dữ liệu và chọn cách vận hành theo nhu cầu.

**Giới hạn:** README tách admin panel, audit log và time tracking sang Pro; phần lớn mã AGPL-3.0-or-later, desktop GPL-3.0-or-later và ảnh Unsplash có quyền riêng.

**Cách tham khảo/tích hợp:** Thử với dự án mẫu, đối chiếu phân quyền, xuất dữ liệu và migration trước dùng quy trình hoặc dữ liệu công việc thật.

**Lựa chọn để đối chiếu:** [usekaneo/kaneo](https://github.com/usekaneo/kaneo) · [Leantime/leantime](https://github.com/Leantime/leantime). Đây là ứng viên so sánh theo tác vụ; mức phù hợp cần kiểm theo hồ sơ và phiên bản riêng.

**Bằng chứng:** `docs-read`, ngày 2026-11-23, commit [`84751cab7f3f7b746dc2f57192e5f255e87b4793`](https://github.com/go-vikunja/vikunja/commit/84751cab7f3f7b746dc2f57192e5f255e87b4793), ngày commit 2026-11-22. Đã clone và đọc chọn lọc phần giới thiệu, cách dùng, giới hạn, license, metadata manifest và CI hiện diện. Chưa kiểm đầy đủ implementation hoặc chạy upstream; các số đo của tác giả chưa được tái lập.

**Nguồn:** [README.md](https://github.com/go-vikunja/vikunja/blob/84751cab7f3f7b746dc2f57192e5f255e87b4793/README.md) · [LICENSE](https://github.com/go-vikunja/vikunja/blob/84751cab7f3f7b746dc2f57192e5f255e87b4793/LICENSE) · [go.mod](https://github.com/go-vikunja/vikunja/blob/84751cab7f3f7b746dc2f57192e5f255e87b4793/go.mod) · [.github/workflows/ci.yml](https://github.com/go-vikunja/vikunja/blob/84751cab7f3f7b746dc2f57192e5f255e87b4793/.github/workflows/ci.yml) · [metadata GitHub](https://api.github.com/repos/go-vikunja/vikunja).

## 11. Nguồn

- Mục 23 §2, §4.3, §4.5 (projects-template, xboss, Sales-Hunter; đọc 2026-10-12)
- Anthropic AI-native SDLC (§10c): https://claude.com/blog/the-ai-native-sdlc-playbook (21/8/2026, kèm PDF 54 trang) · https://claude.com/blog/how-anthropic-secures-its-ai-native-software-development-lifecycle (21/7/2026)
- Anthropic: https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents (26/11/2025) · https://www.anthropic.com/engineering/harness-design-long-running-apps (24/3/2026) · https://www.anthropic.com/engineering/building-effective-agents
- Claude Code docs: https://code.claude.com/docs/en/scheduled-tasks · https://code.claude.com/docs/en/routines · https://code.claude.com/docs/en/desktop-scheduled-tasks · https://code.claude.com/docs/en/github-actions · https://code.claude.com/docs/en/goal · https://code.claude.com/docs/en/channels
- Routines (thứ cấp): prosperinai.substack.com, makerkit.dev, claudefa.st, alexdunlop.com, automatonagency.com, swapbiswas.com, apito.ai
- gh-aw: https://github.com/githubnext/gh-aw · https://github.com/githubnext/gh-aw-workshop
- Durable execution: hackernoon.com (LangGraph/DBOS/Inngest/Temporal), zenml.io (8 Inngest alternatives), langchain.com/resources/langgraph-vs-temporal, cordum.io, cadenya.com, appliedtechnologyindex.com, skill.re, arXiv 2607.19297
- Automation OSS: pinggy.io, lyzr.ai, dev.to/badass_tech, automationatlas.io, blog.n8n.io (2 bài), emergent.sh, usecarly.com, aidiscoverywire.com
- AutoGPT/BabyAGI/AgentGPT: futureagi.com, datacamp.com/tutorial/agentgpt, medium.com/@roseserene, fastcompany.com, bairesdev.com, ibm.com/think/topics/evolution-of-ai-agents, lilianweng.github.io/posts/2023-06-23-agent, arXiv 2404.11584
- Failure modes & guardrail: atlan.com/know/ai-agent/what-is-an-agent-loop, openempower.com, medium.com/@Quaxel (12 guardrails), blogs.oracle.com, arXiv 2606.03115 (SPOQ), blog.traversaal.ai (spend circuit breaker), watchtoweragents.com, sqmagazine.co.uk (METR), withtai.com, arXiv 2509.08646, arXiv 2603.05344
- Harness (thứ cấp): preprints.org/manuscript/202603.1756, gist 0xK8oX, pub.towardsai.net, ai-eval.org, ai-heroes.co, theaiautomators.com, victorinollc.com, agentsdesign.dev, arXiv 2607.14159 (MemoHarness)
- Self-healing CI (demo cộng đồng): github.com/Adityaraj1005/self-healing-ci-agent và các PR "self-heal CI" tìm thấy qua search
