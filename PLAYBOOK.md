# Playbook: skill & tính năng đáng mang sang dự án khác

> Đợt chắt lọc **2026-11-23** từ 2.296 hồ sơ của kho. Mỗi mục ghi bài toán, cơ chế cốt lõi, các bước áp dụng, khi nào nên/không nên dùng, rủi ro, phương án thay thế và link về hồ sơ gốc có mức bằng chứng. Các bước "Áp dụng" là **đề xuất cho repo tích hợp**, kho chưa cài hay chạy thử; trước khi dùng, kiểm lại ngày đọc, license và mọi chỗ ghi **(chưa xác minh)** trong hồ sơ gốc.

Chọn theo bài toán bằng bảng "Nhu cầu → item" ở đầu mỗi chương; tra toàn bộ ứng viên cùng loại trong [catalog/](catalog/README.md) (nhóm → danh mục → danh mục con) và tuyến đọc ở [GUIDES.md](GUIDES.md). Phương pháp đọc bằng chứng: [METHOD.md](METHOD.md).

| Chương | Phạm vi | Số mục |
|---|---|---|
| [1. AI agent, skill & điều phối](#1-ai-agent-skill--điều-phối) | AI agent, skill & điều phối | 24 |
| [2. Tài liệu, dữ liệu, văn phòng & tự động hóa](#2-tài-liệu-dữ-liệu-văn-phòng--tự-động-hóa) | Tài liệu, dữ liệu, văn phòng & tự động hóa | 24 |
| [3. Thiết kế, giao diện, motion & media](#3-thiết-kế-giao-diện-motion--media) | Thiết kế, giao diện, motion & media | 25 |
| [4. Xưởng phần mềm: chất lượng, phát hành & vận hành](#4-xưởng-phần-mềm-chất-lượng-phát-hành--vận-hành) | Xưởng phần mềm: chất lượng, phát hành & vận hành | 25 |

**Nguyên tắc chung khi mang sang dự án khác**

1. Bắt đầu từ phương án nhỏ nhất đáp ứng tác vụ; thêm skill/công cụ khi phép đo cho thấy thiếu.
2. Ghim phiên bản (tag/SHA), đọc LICENSE thật (code, model, nội dung, font/nhạc có thể khác nhau) và ghi lại dữ liệu rời máy (telemetry, API bên thứ ba).
3. Với skill/plugin cho agent: cài ở phạm vi project, xem quyền tool/hook trước khi bật, có bộ eval kích hoạt và đường gỡ.
4. Với tự động hóa gửi ra ngoài (mail, tin nhắn, ghi dữ liệu): luôn có bước người duyệt, khóa chống gửi trùng và đọc lại kết quả.

## 1. AI agent, skill & điều phối

> Chắt lọc từ các mục 01, 02, 03, 04, 07, 10, 11, 12, 17, 20, 21 và `data/projects.json` (snapshot catalog, đọc 23/11/2026). Ưu tiên hồ sơ `code-read`/`docs-read` có `profile_anchor`; mục nào catalog chưa chuẩn hóa mức kiểm (`unassessed`) được ghi rõ. Cơ chế lấy từ hồ sơ trong kho; **kho không cài, không chạy** hầu hết upstream này, nên hiệu quả thực tế, số liệu tự công bố và mọi điều không có trong hồ sơ là **(chưa xác minh)**. Các bước "Áp dụng" là đề xuất cho repo tích hợp, chưa được chạy. Trước khi dùng, kiểm lại license, telemetry và phiên bản tại thời điểm tích hợp (METHOD.md §5).

### Nhu cầu → item nên dùng

| Nhu cầu | Item nên dùng trước | Bổ sung / thay thế |
|---|---|---|
| Agent code theo quy trình spec → plan → TDD → review | 1.2 addyosmani/agent-skills | 1.1 Superpowers, 1.3 mattpocock/skills |
| Rà thiết kế hoặc audit bảo mật bằng reviewer "ngữ cảnh mới" | 1.4 EGM (spec), 1.5 security-audit-skill (bảo mật) | 1.9 Pullboard (builder ≠ reviewer) |
| Giao việc cho subagent, giữ kế hoạch qua compaction/phiên | 1.6 Deep Agents + 1.7 planning-with-files | 1.8 vòng Stop-hook có cổng máy |
| Giảm token log/tool output; nhớ giữa các phiên/agent | 1.10 Think-in-Code (context-mode/RTK), 1.11 ai-memory | claude-mem, engram |
| Đưa skill/plugin vào repo an toàn, ghim, cập nhật, thu hồi | 1.12 Agent Skills spec + `skills` lock, 1.13 agnix + `claude plugin validate` | autoskills (lưu ý license NC) |
| Chứng minh skill/agent thực sự giúp (có baseline) | 1.14 `claude plugin eval` / SkillsBench, 1.15 agentevals, 1.16 Promptfoo/Inspect | SkillEvaluator, skillgrade, coder_eval, garak |
| Viết/đưa MCP server ra dùng chung nhiều người | 1.17 MCP SDK + Conformance, 1.18 agentgateway | Cisco MCP Scanner (§4c mục 04) |
| Cho agent chạy lệnh mà không phá máy/rò bí mật | 1.19 sandbox tiến trình (sandbox-runtime/bubblewrap), 1.20 Codex execpolicy | nono, dcg, gVisor/Firecracker |
| Guardrail và quyền theo user/tenant cho tool | 1.21 ranh giới guardrail (OpenAI Agents SDK), 1.22 Cedar/OpenFGA | SpiceDB, NeMo Guardrails, Presidio |
| Agent chạy lâu, dừng chờ người, có side effect thật | 1.23 LangGraph checkpoint/interrupt, 1.24 Temporal/Restate | DBOS, queue + outbox |

---

### 1.1 Superpowers (obra/superpowers) — Quy trình kỹ thuật trọn vòng cho agent với lõi nhỏ, tự nạp qua một hook

- **Giải quyết:** agent nhảy thẳng vào code, bỏ thiết kế, không viết test, báo "xong" khi chưa kiểm.
- **Cơ chế cốt lõi:** 15 skill nối thành chuỗi `brainstorming` → `using-git-worktrees` → `writing-plans` → `executing-plans`/`subagent-driven-development` → `test-driven-development` → `requesting-/receiving-code-review` → `verification-before-completion` → `finishing-a-development-branch` (kèm `systematic-debugging`, `dispatching-parallel-agents`, `writing-skills`). **Một hook duy nhất** SessionStart (`startup|clear|compact`) chèn toàn văn `using-superpowers/SKILL.md` để agent tự tìm và dùng skill khác; hook đọc file cục bộ, không gọi mạng. Skill TDD ép **xóa code viết trước test**. Thư mục plugin cho Claude Code, Codex, Cursor, OpenCode, Gemini và nhiều host khác.
- **Áp dụng vào dự án khác:**
  1. Cài plugin ở phạm vi dự án, ghim phiên bản (v7.0.1 lúc đọc); đặt `SUPERPOWERS_DISABLE_TELEMETRY=1` trong env của phiên.
  2. Commit hoặc stash mọi thay đổi trước khi giao việc, vì skill TDD yêu cầu xóa code chưa có test.
  3. Chọn một tính năng nhỏ, đi đủ chuỗi brainstorm → plan → subagent-driven → review; lưu plan vào repo.
  4. Biến `verification-before-completion` thành cổng máy: hook Stop/CI chạy test thật (văn xuôi trong skill không phải cổng).
  5. Xác minh: so với baseline không plugin trên 3–5 task thật (tỷ lệ test pass, số lần sửa lại, token).
- **Phù hợp khi / Không nên khi:** Phù hợp khi muốn **ép quy trình** hơn là thư viện kiến thức. Không nên cài chồng với addyosmani/agent-skills hay ECC (cùng phủ plan/TDD/review); không nên khi repo có nhiều code chưa commit.
- **Rủi ro & điều kiện:** MIT. **Không có CI** trong repo chính; eval ở repo riêng `superpowers-evals` **không khai license**, chạy ở chế độ quyền rộng. "Visual companion" tùy chọn tải logo kèm số phiên bản (telemetry đếm người dùng, có biến tắt). Tồn đọng ~375 issue/PR; phát hành theo đợt lớn.
- **Thay thế:** 1.2 addyosmani/agent-skills; 1.3 mattpocock/skills; compound-engineering (mục 20 §3r.1).
- **Hồ sơ gốc:** [20 §3o.1](20-claude-plugins-ecosystem/README.md#3o1-obrasuperpowers--quy-trình-kỹ-thuật-cho-agent-lõi-nhỏ) · catalog `unassessed` (hồ sơ đọc mã, không chạy) · 31/10/2026

### 1.2 addyosmani/agent-skills — Bảy bước Spec → Ship có eval định tuyến skill chạy trong CI

- **Giải quyết:** cần vòng đời kỹ thuật đầy đủ (spec, plan, build tăng dần, test, review, simplify, ship) mà vẫn đo được skill có được chọn đúng.
- **Cơ chế cốt lõi:** 25 skill, 4 agent persona (code-reviewer, security-auditor, test-engineer, web-performance-auditor), 9 command (`/spec`, `/plan`, `/build`, `/test`, `/review`, `/code-simplify`, `/ship`, `/webperf`, `/constraints`), 7 checklist. CI `validate-skills.js` (frontmatter, mục bắt buộc, ngân sách dòng, link) + **eval routing `run-evals.js --min-rank1 95`** (TF-IDF trên description, tất định, không tốn token). Ba tầng eval: cấu trúc (CI) → routing (CI) → hành vi (`--behavioral`, chạy tay). Sổ `evals/skill-impact.md` ghi các thay đổi bị từ chối vì eval. Hook là tùy chọn (`sdd-cache` revalidate bằng `If-None-Match`/`If-Modified-Since`). `/ship` chạy song song ba persona rồi gộp go/no-go.
- **Áp dụng vào dự án khác:**
  1. Cài plugin Claude Code (hoặc `commands/*.toml` cho Gemini/Codex); hoặc chỉ vendor vài skill (doubt-driven, source-driven, incremental-implementation).
  2. Dùng thứ tự `/spec` → `/plan` → `/build` → `/test` → `/review` → `/code-simplify` → `/ship` cho mỗi tính năng; lưu spec vào repo.
  3. Nếu cần hook, tự thêm vào `.claude/settings.json` kèm script test có sẵn.
  4. Sao chép mẫu eval routing (bộ ca prompt → skill kỳ vọng hạng 1, ngưỡng ≥95%) cho skill nội bộ của bạn vào CI.
  5. Xác minh: CI xanh với ngưỡng routing; một ca cố ý sai mô tả skill phải làm CI đỏ.
- **Phù hợp khi / Không nên khi:** Phù hợp khi muốn rộng (security, performance, observability, launch) và quản trị tốt. Không nên cài cùng Superpowers; không coi routing TF-IDF là hiểu ngữ nghĩa (README tự nói là xấp xỉ).
- **Rủi ro & điều kiện:** MIT; không telemetry; `source-driven-development` gọi WebFetch tới docs chính thức. Bảo trì đều (100+ tác giả). Tầng eval hành vi tốn token, chạy tay.
- **Thay thế:** 1.1 Superpowers; 1.3 mattpocock/skills.
- **Hồ sơ gốc:** [20 §3o.2](20-claude-plugins-ecosystem/README.md#3o2-addyosmaniagent-skills--25-skill-vòng-đời-kỹ-thuật-có-eval-routing-trong-ci) · [20 §3zc](20-claude-plugins-ecosystem/README.md#3zc-kiểm-bài-5-repo-skill-đáng-lưu-matt-pocock-addy-osmani-cloudflare-obsidian-google-egm-bài-người-dùng-gửi-đọc-mã-16112026) · `docs-read` · 16/11/2026

### 1.3 mattpocock/skills — Skill nhỏ ghép được và mẫu quản trị phạm vi chặn phình skill

- **Giải quyết:** agent không hiểu đúng ý, dài dòng, code không chạy, kiến trúc thành "ball of mud"; và repo skill nội bộ phình vô hạn.
- **Cơ chế cốt lõi:** 4 failure mode → 4 nhóm skill: `/grill-me`, `/grill-with-docs` (phỏng vấn theo cây quyết định; "sự thật thì tự tra bằng subagent, quyết định thì hỏi người"), glossary + ADR, `/tdd` (red-green-refactor), `/diagnosing-bugs` (vòng gỡ lỗi có cổng theo pha), `/improve-codebase-architecture`. Luật: skill user-invoked (`disable-model-invocation: true`) được gọi skill model-invoked, không gọi skill user-invoked khác. Quản trị: `SCOPE.md` (chỉ nhận issue có failure quan sát trong phiên thật) + `.out-of-scope/*.md` (mỗi ý tưởng bị từ chối một file có lý do).
- **Áp dụng vào dự án khác:**
  1. `claude plugin install mattpocock-skills@claude-plugins-official` hoặc `npx skills@latest add` cho host khác; chạy `/setup-matt-pocock-skills` một lần mỗi repo.
  2. Nếu cần hành vi ổn định: vendor bằng lock + tiền tố (vd. `mp-`) thay cho plugin tự cập nhật; không cài nhóm `in-progress/`.
  3. Dùng `/grill-with-docs` để sinh glossary + ADR làm đầu vào spec.
  4. Chép mẫu `SCOPE.md` + `.out-of-scope/` cho repo skill/harness riêng của bạn.
  5. Xác minh: so phiên có/không skill trên cùng task (số vòng hỏi lại, test pass).
- **Phù hợp khi / Không nên khi:** Phù hợp khi muốn người dùng giữ quyền điều khiển, ghép từng skill. Không nên khi cần một quy trình "sở hữu toàn bộ"; không dùng `git-guardrails-claude-code` (đã đóng băng) làm cổng an toàn vì grep chuỗi lệnh thô dễ né.
- **Rủi ro & điều kiện:** MIT. **Không có workflow CI kiểm nội dung skill**; bằng chứng hiệu quả chủ yếu là kinh nghiệm tác giả (chưa xác minh độc lập). Giả định `gh`/`glab`; bản cài qua skills.sh không tự cập nhật.
- **Thay thế:** 1.2 addyosmani/agent-skills; 1.1 Superpowers.
- **Hồ sơ gốc:** [20 §3c](20-claude-plugins-ecosystem/README.md#3c-case-study-mattpocockskills--skills-for-real-engineers-ảnh-người-dùng-gửi-2026-10-12) · [20 §3zc](20-claude-plugins-ecosystem/README.md#3zc-kiểm-bài-5-repo-skill-đáng-lưu-matt-pocock-addy-osmani-cloudflare-obsidian-google-egm-bài-người-dùng-gửi-đọc-mã-16112026) · `docs-read` · 16/11/2026

### 1.4 Elephant-Goldfish Model (google/elephant-goldfish-model) — Agent đủ ngữ cảnh viết spec, subagent ngữ cảnh mới rà giả định ngầm

- **Giải quyết:** spec viết bởi agent "biết quá nhiều" chứa giả định ngầm; review trong cùng ngữ cảnh không phát hiện được.
- **Cơ chế cốt lõi:** 7 skill (`egm-brainstorm`, `egm-draft`, `egm-review`, `egm-review-loop`, `egm-resolve`…) + 9 persona reviewer, toàn prompt. Skill review **từ chối chạy khi host không tạo được subagent**. Bản Claude Code ép cô lập: persona `tools: [Read, Grep, Glob]`, `omitClaudeMd: true`. Quy tắc hội tụ: "sạch" = không còn Blocker/Major; hội tụ = **hai lượt sạch liên tiếp**, trần **5 lượt**, phát hiện "churn"; dừng chờ người ở mỗi lượt. CI chỉ kiểm cấu trúc.
- **Áp dụng vào dự án khác:**
  1. `claude plugin marketplace add google/elephant-goldfish-model` → `claude plugin install egm@egm`; ghim phiên bản.
  2. Dùng bản `.claude-plugin/` để có cô lập cứng (bản `agents/` cho host khác chỉ dặn bằng lời).
  3. Áp quy tắc nội bộ kiểu `AI_POLICY.md`: thay đổi >100 dòng hoặc ≥3 file lõi phải có design doc qua EGM trước PR.
  4. Đặt trần chi phí cho mỗi vòng review (5 lượt × nhiều persona).
  5. Xác minh: log mỗi lượt có danh sách Blocker/Major; dừng đúng ở 2 lượt sạch hoặc trần.
- **Phù hợp khi / Không nên khi:** Phù hợp với tính năng có quyết định kiến trúc khó đảo ngược. Không nên cho bug nhỏ, rõ (README tự khuyên bỏ qua).
- **Rủi ro & điều kiện:** Apache-2.0; không telemetry; "không phải sản phẩm Google hỗ trợ chính thức"; câu "hàng nghìn kỹ sư Google dùng" **(chưa xác minh)**. Tốn token, repo không công bố số đo; hai bộ persona dễ lệch nhau.
- **Thay thế:** reviewer subagent trong X-Templates (mục 23); 1.2 (`/review`); 1.9 Pullboard.
- **Hồ sơ gốc:** [20 §3u](20-claude-plugins-ecosystem/README.md#3u-kiểm-ảnh-googleelephant-goldfish-model-egm--design-with-an-elephant-review-with-a-goldfish-ảnh-readme-người-dùng-gửi-clone-2112026) · [20 §3zc](20-claude-plugins-ecosystem/README.md#3zc-kiểm-bài-5-repo-skill-đáng-lưu-matt-pocock-addy-osmani-cloudflare-obsidian-google-egm-bài-người-dùng-gửi-đọc-mã-16112026) · `docs-read` · 16/11/2026

### 1.5 cloudflare/security-audit-skill — Audit bảo mật nhiều pha với verifier bác bỏ và validator JSON tất định

- **Giải quyết:** agent audit bảo mật sinh nhiều cảnh báo sai, không có độ phủ đo được, kết quả không có cấu trúc.
- **Cơ chế cốt lõi:** trinh sát → săn theo **coverage ledger** → mỗi ứng viên giao một agent mới tìm cách bác bỏ → ghi `findings.json` theo schema → agent mới kiểm lại → báo cáo. Hai validator Node (`validate-findings.cjs`, `validate-coverage-ledger.cjs`) không mạng, không `child_process`, mở file `O_NOFOLLOW`, kiểm trace `entrypoint → propagation → sink` có `file`/`line`, fingerprint không trùng, trường bắt buộc theo verdict; hồ sơ ghi đã chạy test validator 65/65 pass. **Chỉ là văn xuôi:** file/dòng trích dẫn có tồn tại không, verifier có khác agent tìm ra không.
- **Áp dụng vào dự án khác:**
  1. `npx skills add https://github.com/cloudflare/security-audit-skill --skill security-audit`; chạy trong sandbox (1.19) không có secret.
  2. Đưa hai validator vào CI để `findings.json`/ledger sai schema làm job thất bại.
  3. Tự thêm phần harness mà skill thiếu: kiểm file/dòng trích dẫn bằng code, verifier dùng **model khác**, PoC + bản vá cho phát hiện `confirmed`.
  4. Xác minh: một `findings.json` cố ý sai thứ tự trace phải bị validator từ chối.
- **Phù hợp khi / Không nên khi:** Phù hợp audit một repo trong một phiên. Không nên coi `confirmed` là đã khai thác được nếu chưa có PoC/sandbox thật.
- **Rủi ro & điều kiện:** MIT; 14 commit, không tag/release. Số liệu harness Cloudflare (128 repo, tỷ lệ bác bỏ) là blog tự công bố, không nêu model/chi phí/tỷ lệ bỏ sót **(chưa xác minh)**.
- **Thay thế:** `claude-code-security-review` (mục 12); trail-of-bits-skills (mục 12); garak cho model/endpoint (mục 12 §4f).
- **Hồ sơ gốc:** [12 §3m](12-ai-security-guardrails/README.md#3m-cloudflaresecurity-audit-skill-skill-audit-bảo-mật-nhiều-pha-hạt-giống-của-harness-tìm-lỗ-hổng-của-cloudflare-ảnh-người-dùng-gửi-clone-đầy-đủ-2026-10-25) · [20 §3zc](20-claude-plugins-ecosystem/README.md#3zc-kiểm-bài-5-repo-skill-đáng-lưu-matt-pocock-addy-osmani-cloudflare-obsidian-google-egm-bài-người-dùng-gửi-đọc-mã-16112026) · `docs-read` · 16/11/2026

### 1.6 Deep Agents (langchain-ai/deepagents) — Subagent có hợp đồng ngữ cảnh rõ: isolated hay fork

- **Giải quyết:** điều phối subagent mà không làm bẩn context chính, nhưng cũng không mất bằng chứng khi subagent chỉ trả tóm tắt.
- **Cơ chế cốt lõi:** `SubAgentMiddleware` phân biệt `isolated` (mặc định, chỉ nhận nhiệm vụ) và `fork` (kế thừa hội thoại/state); parent chỉ nhận báo cáo cuối. `FilesystemBackend` `virtual_mode=True` chặn traversal nhưng **không có process isolation**. `graph.py` đặt `recursion_limit=9_999` (không phải ngân sách hợp lý). Eval upstream chạy thủ công (`workflow_dispatch`).
- **Áp dụng vào dự án khác:**
  1. Định nghĩa hợp đồng đầu ra cho mỗi subagent: `run_id`, artifact/nguồn/exit reason, không chỉ verdict.
  2. Dùng `isolated` cho điều tra/review độc lập; `fork` chỉ khi cần lịch sử, kiểm quyền tool không tăng.
  3. Đặt lại `recursion_limit` và trần token/thời gian theo task.
  4. Chạy code không tin cậy qua backend sandbox (1.19), không qua FilesystemBackend.
  5. Xác minh: thử compaction/restart, đo tỷ lệ bằng chứng còn tra lại được.
- **Phù hợp khi / Không nên khi:** Phù hợp khi đã dùng LangGraph và cần subagent + filesystem + summarization + HITL. Không nên khi một workflow tất định đủ dùng.
- **Rủi ro & điều kiện:** MIT; eval cần nhiều provider key; hành vi thực tế **(chưa xác minh)**.
- **Thay thế:** subagent có sẵn trong Claude Code; 1.7 planning-with-files; Agent Teams (mục 03 §8f).
- **Hồ sơ gốc:** [03 §8j](03-agentic-patterns-loops/README.md#core-context-contracts) · `code-read` · 02/11/2026

### 1.7 planning-with-files — Kế hoạch 3 file trên đĩa với cổng Stop có trần và khôi phục phiên có phạm vi

- **Giải quyết:** agent quên kế hoạch sau compaction hoặc giữa phiên; dừng sớm khi việc chưa xong; vòng lặp vô hạn.
- **Cơ chế cốt lõi:** plan/ledger trên đĩa + hook mỗi lượt. `check-complete.sh` chặn Stop khi phase `in_progress`, chưa chạm `PWF_GATE_CAP` (20) và ledger còn tăng; ledger không đổi hoặc chạm cap thì **cho dừng** (được dừng ≠ hoàn thành). `attest-plan.sh` băm plan để phát hiện lệch khỏi bản đã attest (không phải chữ ký). `session-catchup.py` lọc transcript theo project/cwd, quarantine nguồn thiếu định danh. CI đa OS ép có shell để test hook không bị skip.
- **Áp dụng vào dự án khác:**
  1. Cài vào host có hook (Claude Code…); commit 3 file plan vào repo hoặc thư mục làm việc.
  2. Bật cổng Stop opt-in, giữ cap; không đặt hai cổng Stop/hai vòng tự sửa chồng nhau.
  3. Đo tiến triển bằng artifact/test, không đếm dòng ledger; phân loại `complete`/`stalled`/`budget_exhausted`/`blocked`.
  4. Xác minh: phiên mới sau compaction đọc đúng plan; ca ledger đứng yên phải được cho dừng với trạng thái `stalled`.
- **Phù hợp khi / Không nên khi:** Phù hợp cho task dài nhiều phiên. Không nên khi host không hỗ trợ hook, hoặc đã có vòng Ralph riêng.
- **Rủi ro & điều kiện:** MIT; attestation không bảo vệ khỏi tác nhân sửa được cả plan lẫn hash.
- **Thay thế:** 1.8 vòng Stop-hook có cổng máy; 1.6 Deep Agents; TodoWrite có sẵn của host.
- **Hồ sơ gốc:** [03 §8j](03-agentic-patterns-loops/README.md#core-context-contracts) · `code-read` · 02/11/2026

### 1.8 Vòng Ralph / Stop-hook với ba cổng máy — Cho agent lặp tới khi xong, nhưng "xong" do file trạng thái quyết định

- **Giải quyết:** agent tự tuyên bố hoàn thành (`<promise>`) hoặc lặp mãi trên cùng lỗi.
- **Cơ chế cốt lõi:** dạng gốc `while :; do cat PROMPT.md | claude ; done` — bộ nhớ duy nhất là file trong repo. Plugin `ralph-loop` dùng Stop hook nạp lại prompt, kết thúc bằng promise string + trần vòng. Phản biện trong kho thay promise bằng: (1) Stop hook đọc **file trạng thái do script/CI điền** (test, lint, build); (2) dừng BLOCKED khi cùng chữ ký lỗi lặp N lần; (3) trần vòng (`STOP_HOOK_BLOCK_CAP`, mặc định 8) + fingerprint sha256 diff; (4) evidence gate: phải nêu đường dẫn bằng chứng có thật. Hook đọc `stop_hook_active` để tránh đệ quy; mọi hook có biến tắt và có test.
- **Áp dụng vào dự án khác:**
  1. Viết `PROMPT.md` có tiêu chí kiểm bằng máy (tests pass, lint sạch, build ok).
  2. Script CI/local ghi kết quả vào một file trạng thái; Stop hook chỉ đọc file đó.
  3. Thêm trần vòng, phát hiện lỗi lặp cùng chữ ký, kiểm `stop_hook_active`.
  4. Viết test cho hook (`tests/claude-hooks.test.ts` là mẫu trong hồ sơ).
  5. Xác minh: ca test đỏ cố định phải kết thúc BLOCKED trước trần, không lặp mãi.
- **Phù hợp khi / Không nên khi:** Phù hợp greenfield, tiêu chí rõ. Không nên để vòng tự merge/tag khi người khác phụ thuộc output; không dùng với prompt mơ hồ.
- **Rủi ro & điều kiện:** mẫu thiết kế, không phải một gói; `/goal`, `/batch` **(chưa xác minh)** trên docs chính thức. Tốn token theo số vòng.
- **Thay thế:** 1.7 planning-with-files; `/loop` và Routines (mục 21 §3); oh-my-claudecode ralph có cổng test (mục 03 §8g).
- **Hồ sơ gốc:** [03 §3](03-agentic-patterns-loops/README.md#3-ralph-wiggum-loop--vòng-lặp-tự-trị-cho-coding-agent) · catalog `unassessed` (mẫu từ tài liệu + repo của chủ kho) · 12/10/2026

### 1.9 Pullboard (pullboard-dev/pullboard) — Hàng đợi nhiều agent sống trong repo, builder không được tự duyệt

- **Giải quyết:** điều phối nhiều agent song song trên một repo mà vẫn có spec, luật và kiểm chéo bằng máy.
- **Cơ chế cốt lõi:** CLI Node 0 phụ thuộc; board là **một file SQLite trong `.git`** dùng chung mọi worktree; `SPEC.md`, `DOCTRINE.md`, `pullboard.json`, `AGENTS.md`, git hook. Luật PB1 "builder không tự verify": `src/bar-check.js` từ chối khi `builderSession === reviewerSession` (`BAR_SELF_SIGN`); lane build trong worktree riêng. CI kiểm sign-off DCO và `pullboard spec check`. "Khác người" chỉ là **khác phiên chạy** (có thể cùng model/máy/tài khoản).
- **Áp dụng vào dự án khác:**
  1. Thử trên repo phụ; đọc `DOCTRINE.md` + `SPEC.md` để biết hook chặn gì.
  2. Mỗi agent một git worktree; giữ board trong `.git` (không commit).
  3. Bổ sung reviewer khác model hoặc người cho thay đổi rủi ro (bar-check chưa phải review độc lập).
  4. Không liên kết relay `app.pullboard.dev` với repo khách hàng.
  5. Xác minh: thử cho cùng phiên vừa build vừa review — phải bị từ chối.
- **Phù hợp khi / Không nên khi:** Phù hợp khi đã chạy nhiều agent và cần hàng đợi + spec trong repo. Không nên cho repo khách hàng/nhạy cảm khi dự án còn non.
- **Rủi ro & điều kiện:** MIT + CLA; một người duy trì, dự án ~4 tuần lúc đọc; số liệu năng suất tự công bố **(chưa xác minh)**; relay tùy chọn lưu metadata. Action CI ghim theo tag, không theo SHA.
- **Thay thế:** Orca (mục 01 §3n, lưu ý mặc định chạy agent toàn quyền); Agent Teams (mục 03 §8f); Vibe Kanban (mục 01).
- **Hồ sơ gốc:** [21 §10h](21-autonomous-workflows/README.md#10h-hồ-sơ-pullboard-devpullboard-hàng-đợi-điều-phối-nhiều-agent-sống-trong-repo-agent-thứ-hai-kiểm-tra-thực-thi-bằng-khác-phiên-chạy-ảnh-readme-người-dùng-gửi-đọc-mã-3112026) · `code-read` · 03/11/2026

### 1.10 Think in Code + lọc output (context-mode, RTK) — Ngân sách context thành cổng máy thay vì lời dặn

- **Giải quyết:** log, test output, trang web, JSON lớn tràn cửa sổ ngữ cảnh, đốt token, đẩy compaction sớm.
- **Cơ chế cốt lõi:** context-mode: tool MCP `ctx_execute*` chạy script, **chỉ stdout vào context**; `ctx_index` chia markdown vào SQLite FTS5 (BM25 + trigram, RRF); hook PreToolUse **deny** `curl`/`wget`/`WebFetch` và chuyển Bash output >20 dòng sang `ctx_*`; throttling cứng (`ctx_search` lần 9+ bị chặn); 5–6 hook ghi sự kiện phiên vào SQLite để truy xuất sau compaction; redaction secret trong log. RTK: binary Rust, hook viết lại `git status` → `rtk git status`, lọc/gộp output CLI, giữ output đầy đủ khi lệnh lỗi. "Think in Code" (viết script tóm tắt thay vì `cat`) áp được **không cần cài gì**.
- **Áp dụng vào dự án khác:**
  1. Ngay lập tức: thêm vào `CLAUDE.md`/`AGENTS.md` quy tắc xử lý log/CSV bằng script in tổng hợp; chuyển output dài ra file.
  2. Nếu cài context-mode: chạy `/context-mode:ctx-doctor` sau cài để chắc hook hoạt động.
  3. Giữ sandbox của host bật và kiểm xem tiến trình MCP server có nằm trong sandbox không (có thể **nới** ranh giới mạng/FS).
  4. Áp lại luật `deny` của `.claude/settings.json` cho tool `ctx_*`.
  5. Xác minh: A/B có/không công cụ trên task thật — đo pass@1, số lượt sửa, chi phí, không chỉ byte.
- **Phù hợp khi / Không nên khi:** Phù hợp phiên dài nhiều log/web. Không nên khi host không sandbox được MCP server, hoặc khi cần đóng gói thành dịch vụ hosted (ELv2).
- **Rủi ro & điều kiện:** context-mode **Elastic-2.0** (không OSI; cấm cung cấp dạng hosted); "sandbox" chỉ là ranh giới tiến trình, script có quyền dùng env/credential; mặc định không timeout. Con số 98% là **byte** tác giả tự đo, không đo chất lượng **(chưa xác minh)**; mất thông tin là phản biện thật. RTK Apache-2.0, chỉ lọc output shell.
- **Thay thế:** subagent/`/compact` có sẵn; Serena (đọc code mức symbol, GPL-3.0); Read gate của claude-mem.
- **Hồ sơ gốc:** [03 §8b](03-agentic-patterns-loops/README.md#8b-case-study-context-mode--giữ-output-tool-ngoài-cửa-sổ-ngữ-cảnh-link-từ-người-dùng-2026-10-12) · catalog `unassessed` (đọc mã context-mode, không chạy) · 16/10/2026

### 1.11 ai-memory (akitaonrails/ai-memory) — Bộ nhớ dài hạn dùng chung cho nhiều coding agent, wiki Markdown trong git, mặc định không gọi LLM

- **Giải quyết:** đổi agent (Claude Code → Codex) hoặc đổi máy phải giải thích lại; memory dùng LLM nén thì tốn quota và gửi transcript ra ngoài.
- **Cơ chế cốt lõi:** một binary Rust; nguồn sự thật là **wiki `.md` trong git**, SQLite chỉ là chỉ mục dựng lại được (FTS5, entity, đồ thị, embedding tùy chọn). Hook ghi prompt/tool call/ranh giới phiên qua lớp riêng tư có kiểu rồi server gom thành trang wiki — ghi, tìm, handoff đều không cần API key. **Handoff có kiểu**, có chủ, chỉ nhận một lần. Lão hóa bộ nhớ không LLM (phân rã, gộp gần trùng, gắn cờ mâu thuẫn, không xóa cứng). "Dream" bằng LLM mặc định tắt, phải qua eval recall. Hỗ trợ 20+ harness.
- **Áp dụng vào dự án khác:**
  1. `curl -fsSL …/install.sh | sh` (installer kiểm SHA-256) rồi `ai-memory setup --plan` để xem trước thay đổi trước khi áp.
  2. Chạy server trên máy/homelab bạn kiểm soát; nhóm trỏ chung một server, tri thức chia theo dự án.
  3. Thêm plugin `claude plugin install ai-memory@ai-memory` (Codex tương tự).
  4. Xác minh: khởi động lại agent, hỏi "What do you remember about this project?"; thử handoff Claude Code → Codex cùng thư mục.
- **Phù hợp khi / Không nên khi:** Phù hợp khi dùng nhiều harness, muốn bộ nhớ grep/sửa tay được. Không nên cài chồng với memory plugin khác dùng cùng hook SessionStart; không dùng trong container cloud tạm thời nếu dữ liệu không được giữ.
- **Rủi ro & điều kiện:** MIT; `DATA_HANDLING.md` ghi không telemetry, không tự kiểm cập nhật; cài theo `curl | sh` chạm hệ thống. Nhịp phát hành nhanh — ghim bản. Kết quả LongMemEval trong `evals/` **(chưa xác minh)** bởi kho.
- **Thay thế:** claude-mem (mục 10 §4e: truy xuất 3 lớp + Read gate, nhưng telemetry PostHog bật mặc định và model nén thường là cloud); engram (mục 10 §4c); `CLAUDE.md` + auto-memory có sẵn.
- **Hồ sơ gốc:** [10 §6h](10-local-llm-rag-memory/README.md#6h-hồ-sơ-akitaonrailsai-memory-bộ-nhớ-dài-hạn-dùng-chung-cho-20-coding-agent-wiki-markdown-trong-git-mặc-định-không-gọi-llm-ảnh-readme-người-dùng-gửi-đọc-mã-8112026) · `code-read` · 08/11/2026 · đối chiếu [10 §4e claude-mem](10-local-llm-rag-memory/README.md#4e-thedotmackclaude-mem-trí-nhớ-giữa-các-phiên-bằng-hook--ai-nén-yêu-cầu-người-dùng-clone-2026-10-30) (`unassessed`, 30/10/2026)

### 1.12 Agent Skills spec + `skills` CLI lock — Chuẩn SKILL.md liên thông và lockfile băm nội dung cho vòng đời skill

- **Giải quyết:** skill trôi phiên bản giữa hai phiên, không biết đang chạy nội dung nào, không gỡ/khôi phục được.
- **Cơ chế cốt lõi:** spec `agentskills/agentskills` + `skills-ref` validator kiểm frontmatter/name/description/compatibility; trường `license`, `metadata`, `allowed-tools` (**experimental, tùy host**; validator không thi hành sandbox/quyền). `vercel-labs/skills`: `skills-lock.json` ghi source/sourceUrl/ref/skillPath và `computedHash` SHA-256 thư mục; fetch theo commit SHA đầy đủ; lệnh check/update/remove có test. Telemetry và request security audit dùng **chung** công tắc `DO_NOT_TRACK`/`DISABLE_TELEMETRY`; audit API lỗi trả `null`, không chặn cài.
- **Áp dụng vào dự án khác:**
  1. Viết skill nội bộ đúng spec; chạy `skills-ref validate` trong CI.
  2. Cài skill ngoài bằng `npx skills add <repo> --skill <tên>`, commit `skills-lock.json`; ghim ref là SHA.
  3. Mỗi cập nhật: diff toàn bộ artifact (script, reference, quyền, mạng, license) qua review trước khi merge lock mới.
  4. Nếu tắt telemetry, thêm cổng quét riêng (mục 12) vì audit của CLI cũng tắt theo.
  5. Xác minh: sửa tay một file skill đã cài, `skills check` phải báo lệch hash; thử `remove` rồi khôi phục đúng hash.
- **Phù hợp khi / Không nên khi:** Phù hợp mọi dự án dùng skill trên nhiều harness. Không nên coi hash là chứng nhận nguồn tốt, hoặc `allowed-tools` là quyền đã được thi hành.
- **Rủi ro & điều kiện:** spec Apache-2.0; CLI MIT. Validator chuẩn hóa NFKC cho phép một số ký tự Unicode trong `name` mà host có thể từ chối; ma trận tương thích **(chưa xác minh)**. `remove` không thu hồi credential hay side effect.
- **Thay thế:** autoskills (hash từng file + registry review, nhưng **CC-BY-NC-4.0**); marketplace `claude-plugins-official`; vendor thủ công.
- **Hồ sơ gốc:** [20 §3w](20-claude-plugins-ecosystem/README.md#skill-lifecycle-2026-11-02) · `code-read` · 02/11/2026

### 1.13 agnix + `claude plugin validate --strict` — Cổng tiếp nhận tất định cho CLAUDE.md, SKILL.md, hook, MCP và plugin

- **Giải quyết:** frontmatter sai làm skill "vô hình", hook lỗi, `.mcp.json` trỏ URL `http://` ra ngoài, cấu hình đa harness lệch nhau.
- **Cơ chế cốt lõi:** `claude plugin validate` (docs chính thức) kiểm kiểu dữ liệu, path phải bắt đầu `./` và không thoát plugin root, `.mcp.json` (URL `http://`, header giống credential), tên giả danh; `--strict` biến cảnh báo thành lỗi. agnix: 757 luật đa harness (Claude Code, Codex, Cursor, Copilot, Gemini, Kiro…), auto-fix, LSP, GitHub Action; CLI **exit 1** khi còn errors hoặc khi `--strict` còn warnings, chạy validate lại sau autofix; telemetry chỉ khi build với feature `telemetry` (`default = []`).
- **Áp dụng vào dự án khác:**
  1. Thêm `claude plugin validate --strict` vào CI cho mọi plugin/marketplace tự viết hoặc vendor.
  2. Thêm `npx agnix .` (hoặc GitHub Action) với `--strict` theo chính sách; review mọi suppression/luật bị tắt.
  3. Commit một fixture sai có chủ đích để chứng minh wrapper CI thật sự nhận mã thoát lỗi.
  4. Xác minh: job đỏ trên fixture sai, xanh trên bản sạch.
- **Phù hợp khi / Không nên khi:** Phù hợp mọi repo có cấu hình agent. Không nên coi lint sạch là skill hữu ích hay an toàn (cần 1.14 và scanner mục 12).
- **Rủi ro & điều kiện:** agnix MIT OR Apache-2.0, một người dẫn dắt, nhịp commit cao; binary tải sẵn có build cùng feature hay không **(chưa xác minh)**. `claude plugin validate` là tài liệu sản phẩm, catalog `unassessed`.
- **Thay thế:** validator riêng của từng harness; SkillEvaluator tầng 1 (mục 20 §3v); `skills-ref validate` (1.12).
- **Hồ sơ gốc:** [20 §3y](20-claude-plugins-ecosystem/README.md#factory-skill-admission-2026-11-04) · [20 §3v](20-claude-plugins-ecosystem/README.md#3v-nâng-trần-2112026-validator-chính-thức-linter-cấu-hình-agent-và-eval-kích-hoạt-skill-yêu-cầu-người-dùng) · `code-read` · 04/11/2026

### 1.14 Eval skill có baseline (`claude plugin eval`, SkillsBench) — Đo skill có được kích hoạt và có làm kết quả tốt hơn so với không có skill

- **Giải quyết:** không biết skill có được gọi đúng lúc, có kích hoạt sai, và có thật sự cải thiện kết quả hay chỉ tốn token.
- **Cơ chế cốt lõi:** `claude plugin eval` (từ v2.1.269 theo docs): case = prompt + grader (`regex`, `tool_used`, `tool_order`, `file_exists` miễn phí; `llm`, `baseline` tốn judge), mặc định 3 lần chạy, so với nhánh **không plugin**, `--threshold`, `--max-cost-usd`, mã thoát 0/1/2 cho CI. SkillsBench: mỗi task = `task.md` + Docker + `environment/skills/` + `oracle/solve.sh` + verifier; **oracle phải pass trước khi chạy agent**; verifier ghi `reward.txt` 1/0 từ mã thoát pytest với phụ thuộc test ghim phiên bản.
- **Áp dụng vào dự án khác:**
  1. Mỗi PR: eval kích hoạt rẻ với grader `tool_used`/`regex`, gồm cả ca **không nên kích hoạt**.
  2. Nightly/trước release: eval có baseline không skill, đặt `--max-cost-usd`.
  3. Với task nặng: copy khuôn SkillsBench (`task.md`/oracle/verifier), ghim phụ thuộc verifier, bắt buộc oracle pass.
  4. Không dùng cùng bộ ca để vừa chỉnh mô tả skill vừa kết luận; giữ held-out.
  5. Xác minh: báo cáo có số lần chạy, tỷ lệ kích hoạt sai, chất lượng so baseline, chi phí.
- **Phù hợp khi / Không nên khi:** Phù hợp trước khi đưa skill vào nhiều nhóm. Không nên dùng skill mẫu trong SkillsBench làm skill chuẩn (vd. `ffmpeg-video-editing` chỉ là cheatsheet theo task).
- **Rủi ro & điều kiện:** eval tốn hạn mức/API; định dạng case khác `evals.json` của skill-creator. SkillsBench Apache-2.0, chạy đầy đủ cần BenchFlow CLI + Modal/Docker + khóa model; mục tiêu "SOTA dưới 50%" là tuyên bố dự án **(chưa xác minh)**.
- **Thay thế:** NVIDIA SkillEvaluator (3 tầng); `mgechev/skillgrade`; `UiPath/coder_eval` (`skill_triggered` đa harness).
- **Hồ sơ gốc:** [20 SkillsBench](20-claude-plugins-ecosystem/README.md#xlsx-2026-11-23-skillsbench) · `code-read` · 23/11/2026 · [20 §3v](20-claude-plugins-ecosystem/README.md#3v-nâng-trần-2112026-validator-chính-thức-linter-cấu-hình-agent-và-eval-kích-hoạt-skill-yêu-cầu-người-dùng) (docs `claude plugin eval`, `unassessed`, 02/11/2026)

### 1.15 agentevals (langchain-ai/agentevals) — Chấm trajectory tool call tất định, tách khỏi chấm kết quả

- **Giải quyết:** đổi prompt/harness làm hỏng hình dạng vòng lặp (bỏ bước kiểm, đổi đối số tool) mà test kết quả không bắt được.
- **Cơ chế cốt lõi:** `create_trajectory_match_evaluator` 4 chế độ `strict`/`unordered`/`subset`/`superset` và `tool_args_match_mode` (`exact`/`ignore`); mặc định `strict` + `exact`. `strict` kiểm số message, role, tên và args tool — **không so nội dung văn bản hay payload tool trả về**. `subset` có thể cho qua đường thiếu bước bắt buộc. Có bản LLM-as-judge và bản cho graph LangGraph; Python + TS.
- **Áp dụng vào dự án khác:**
  1. Lưu trajectory tham chiếu cho mỗi luồng quan trọng; xuất từ trace OTel thay vì log riêng.
  2. CI: `superset` cho luồng cần đủ tool then chốt, `strict` cho workflow cố định; ghim cả chế độ và matcher args.
  3. Thêm assertion bất biến nghiệp vụ (approve trước write, không vượt tenant) và test artifact cuối riêng.
  4. Xác minh bằng bộ ca phá cổng: đổi tenant trong args, bỏ bước kiểm, gọi lại side effect, thêm tool bị cấm — ghi cổng nào bắt ca nào.
- **Phù hợp khi / Không nên khi:** Phù hợp luồng agent có tool đã ổn định. Không nên dùng làm oracle nội dung.
- **Rủi ro & điều kiện:** MIT; API còn sớm (0.0.x); quickstart dùng model giám khảo (dữ liệu ra provider); CI tích hợp dùng LangSmith secrets — tách chạy offline tất định khỏi judge.
- **Thay thế:** 1.16 Promptfoo/Inspect; trace + eval của mục 07; 1.14 cho skill.
- **Hồ sơ gốc:** [03 §8l](03-agentic-patterns-loops/README.md#factory-trajectory-oracles-2026-11-04) · `code-read` · 04/11/2026

### 1.16 Promptfoo / Inspect AI — Eval hồi quy có đơn vị đo đúng và không nhầm cache là lần chạy độc lập

- **Giải quyết:** kết luận "prompt/skill mới tốt hơn" dựa trên điểm trung bình, output đã cache hoặc các mẫu không độc lập.
- **Cơ chế cốt lõi:** Promptfoo: `getRepeatCacheNamespace` tách `repeat:N`, nhưng **lần eval tiếp theo vẫn lấy output đã cache** (cần `--no-cache` để đo biến thiên); tách assertion tất định khỏi judge; `PROMPTFOO_DISABLE_TELEMETRY=1` không tắt provider call/remote grader. Inspect AI: `CachePolicy.per_epoch=True` đưa epoch vào cache key; `std.py` có stderr, bootstrap, CI và **clustering theo metadata** cho mẫu cùng tài liệu/hội thoại.
- **Áp dụng vào dự án khác:**
  1. Tập regression cố định + assertion tất định (schema/tool/regex) chạy mỗi PR, cho phép cache để replay.
  2. Thí nghiệm ổn định: `--no-cache`/epoch tách cache, báo phân phối và khoảng bất định, cluster theo đơn vị độc lập.
  3. Ghi model ID, seed/temperature, cache policy, repeat, lỗi, giá vào artifact.
  4. Xác minh: một thay đổi cố ý làm hỏng ca cũ phải làm job đỏ; lỗi provider không được tính là pass.
- **Phù hợp khi / Không nên khi:** Phù hợp mọi thay đổi prompt/skill/model. Không nên kết luận từ chênh 1–2 điểm không có khoảng bất định.
- **Rủi ro & điều kiện:** cả hai MIT; Promptfoo có telemetry (có biến tắt); provider/judge gửi dữ liệu ra ngoài.
- **Thay thế:** OpenEvals (mục 07); garak cho red-team model/endpoint (mục 12 §4f); DSPy/GEPA khi tối ưu prompt cần holdout thật (mục 17 §4d).
- **Hồ sơ gốc:** [07 core-eval-validity](07-eval-observability/README.md#core-eval-validity) · `code-read` · 02/11/2026

### 1.17 MCP Python SDK + MCP Conformance — Ghim spec, harness và baseline để "MCP đúng chuẩn" có nghĩa kiểm lại được

- **Giải quyết:** nâng SDK MCP làm đổi nghĩa "pass" âm thầm; server pass schema nhưng lộ transport/auth.
- **Cơ chế cốt lõi:** CI của Python SDK ghim `@modelcontextprotocol/conformance@0.2.0-alpha.11`, chạy nhiều wire (`2025-11-25`, `2026-07-28`) với baseline riêng. `MCPServer` bật DNS-rebinding protection cho localhost ở đường SSE đã đọc, nhưng `TransportSecurityMiddleware` không nhận settings thì protection tắt. Conformance tách `--suite`, `--spec-version`, `--requirements <revision>`; lỗi ở scenario `not_scored` không làm exit code thất bại; LICENSE chuyển MIT → Apache-2.0 (docs CC-BY-4.0).
- **Áp dụng vào dự án khác:**
  1. Inventory client/server, transport, wire revision đang dùng.
  2. Ghim SDK, harness SHA, file requirements và baseline expected-failure trong repo.
  3. Lưu `checks.json` tách passed/failed/skipped/not-scored/expected-failure; không thêm failure vào baseline chỉ để xanh.
  4. Cấu hình Host/Origin allowlist và token verifier (issuer/audience) rõ ràng; thử request giả.
  5. Xác minh: negative fixture phải bị harness bắt; ca truy cập chéo tenant phải bị từ chối (ngoài phạm vi conformance).
- **Phù hợp khi / Không nên khi:** Phù hợp khi tự viết/vận hành MCP server. Không nên coi conformance là bằng chứng quyền truy cập dữ liệu đúng.
- **Rủi ro & điều kiện:** SDK MIT, v2 phá vỡ tương thích; conformance license hỗn hợp; trạng thái CI upstream **(chưa xác minh)**.
- **Thay thế:** A2A TCK (mục 04 §4c); Cisco MCP Scanner; 1.18 agentgateway cho lớp quyền.
- **Hồ sơ gốc:** [04 §4d](04-protocols-standards/README.md#core-protocol-boundaries) · [04 §4f](04-protocols-standards/README.md#factory-protocol-conformance-evidence-2026-11-04) · `code-read` · 02/11/2026 và 04/11/2026

### 1.18 agentgateway — Proxy MCP/A2A/LLM có JWT và RBAC CEL theo tool, prompt, resource

- **Giải quyết:** nhiều người/agent dùng chung MCP server mà không có quyền theo từng tool, không có điểm audit chung.
- **Cơ chế cốt lõi:** proxy Rust (LF Projects); JWT yêu cầu issuer, audience chỉ ép khi danh sách cấu hình không rỗng, có mode `Permissive`; policy CEL theo `jwt.sub` và `mcp.tool.name`. **`McpAuthorizationSet::validate` trả `true` khi không có rule** — cài gateway + JWT chưa tự giới hạn tool. Ví dụ cấu hình có CORS `*` và token passthrough.
- **Áp dụng vào dự án khác:**
  1. Đặt gateway trước các MCP server; chặn network để không bypass được gateway.
  2. Cấu hình JWT strict với issuer + audience thật; không dùng `Permissive` ở production.
  3. Viết policy CEL cho từng tool/prompt/resource; không chép nguyên ví dụ (CORS `*`, passthrough).
  4. Xác minh: user không có quyền bị từ chối cả khi list lẫn khi gọi trực tiếp tên tool đã biết; token sai audience bị chặn.
- **Phù hợp khi / Không nên khi:** Phù hợp MCP dùng chung nhiều người/tenant. Không nên cho một người dùng một máy local (thêm bề mặt vận hành).
- **Rủi ro & điều kiện:** Apache-2.0; default-allow khi thiếu rule là điều kiện tiên quyết phải xử lý; quyền nghiệp vụ tenant vẫn do backend kiểm.
- **Thay thế:** Apache APISIX (mục 04); policy engine 1.22 đặt ở tool gateway tự viết; verifier của MCP SDK (1.17).
- **Hồ sơ gốc:** [04 §4d](04-protocols-standards/README.md#core-protocol-boundaries) · `code-read` · 02/11/2026

### 1.19 Sandbox tiến trình mức OS (anthropics/sandbox-runtime, bubblewrap) — Chặn mạng mặc định và giới hạn file cho lệnh agent chạy

- **Giải quyết:** agent chạy lệnh/script có thể đọc home/secret, ghi ra ngoài thư mục làm việc, gọi mạng tùy ý.
- **Cơ chế cốt lõi:** sandbox-runtime: sandbox OS cho tiến trình, không cần container — Seatbelt (macOS), bubblewrap (Linux); **mạng chặn mặc định**, chỉ mở domain allowlist qua proxy; làm cho Claude Code. Bubblewrap: CLI nhận bind mount chỉ đọc/ghi, namespace mạng/PID/user, seccomp; **chính đối số wrapper quyết định phạm vi**; `--not-a-security-boundary` thêm fail-open. Dùng chung kernel; không tự cấp quota CPU/RAM/thời gian.
- **Áp dụng vào dự án khác:**
  1. Phân loại job theo độ tin cậy: máy dev → sandbox-runtime; code không tin cậy trên server → jail namespace + seccomp không mạng; đa tenant → microVM/gVisor.
  2. Dựng wrapper từ manifest quyền đã review: chỉ mount input, output riêng, egress allowlist, không đưa secret vào env.
  3. Đặt timeout/quota ở lớp ngoài.
  4. Xác minh bằng fixture âm: đọc file sentinel ngoài input, ghi ra ngoài output, gọi domain ngoài scope, chạy quá timeout — tất cả phải bị chặn; fixture hợp lệ vẫn chạy. Lưu exit status + profile hash.
- **Phù hợp khi / Không nên khi:** Phù hợp mọi agent chạy lệnh trên máy thật. Không nên dùng làm ranh giới cho tenant không tin cậy (cần VM); không gọi "tiến trình con mang theo env" là sandbox.
- **Rủi ro & điều kiện:** sandbox-runtime Apache-2.0, **beta research preview**, Windows alpha, định dạng config có thể đổi (catalog `unassessed`). Bubblewrap LGPL (LICENSE 2.1; `bubblewrap.c` 2.0-or-later); user namespace có thể bị host tắt.
- **Thay thế:** nono (Landlock/Seatbelt + proxy giữ credential, mục 12 §4b); gVisor; Firecracker/E2B/Kata (mục 11 §3).
- **Hồ sơ gốc:** [11 §3g bubblewrap](11-browser-computer-use-sandbox/README.md#factory-2026-11-04-bubblewrap) · `code-read` · 04/11/2026 · [11 §3b sandbox-runtime](11-browser-computer-use-sandbox/README.md#3b-repo-nổi-tiếng-bổ-sung-computer-use-crawl-cho-llm-sandbox-đã-xác-minh-2026-10-12) (`unassessed`, 12/10/2026)

### 1.20 Codex execpolicy — Policy lệnh có ca kiểm dương/âm, và biết rằng JSON "forbidden" không tự làm CI đỏ

- **Giải quyết:** cần biết chắc lệnh nào agent được chạy, phê duyệt dựa trên đối số nào, và cổng policy có thật sự chặn.
- **Cơ chế cốt lõi:** prefix rules có `match`/`not_match` được kiểm lúc nạp (ghim ca hồi quy của chính policy), chọn quyết định chặt nhất trong các rule khớp; `Decision` phân biệt chặn / xin reviewer / quyết định người dùng. `codex execpolicy check` in JSON rồi trả `Ok(())` — **`forbidden` không tự làm exit khác 0**. Runtime còn kết hợp approval policy và sandbox; lệnh không match đi đường heuristic. Binary ở đường dẫn tuyệt đối có thể cần `host_executable`.
- **Áp dụng vào dự án khác:**
  1. Viết rules trong repo, kèm `match`/`not_match` cho từng rule.
  2. Wrapper CI parse trường `decision`; xử lý rõ trường hợp không match; không lấy exit 0 làm allow.
  3. Đóng băng base SHA, task, model, rules, giới hạn thời gian/chi phí cho mỗi lần chạy agent.
  4. Xác minh: ca bị cấm dừng trước side effect; ca không match có kết quả định trước; canary hợp lệ vẫn chạy; lưu policy hash + argv + cwd.
- **Phù hợp khi / Không nên khi:** Phù hợp khi dùng Codex CLI hoặc cần mẫu policy lệnh kiểm được. Không nên coi policy là sandbox (cần 1.19).
- **Rủi ro & điều kiện:** Apache-2.0; chưa chạy CI/binary upstream; heuristic cho lệnh không match cần thử trên host thật.
- **Thay thế:** hook PreToolUse `deny` của Claude Code (mục 03 §3); dcg (mục 12 §4b: chú ý license cấm OpenAI/Anthropic và fail-open mặc định); agent-governance-toolkit (fail-closed).
- **Hồ sơ gốc:** [01 §3o](01-ai-coding-agents/README.md#factory-coding-policy-2026-11-04) · `code-read` · 04/11/2026

### 1.21 Ranh giới guardrail và handoff (OpenAI Agents SDK) — Biết cổng nào chạy trước hành động và đường nào không đi qua cổng

- **Giải quyết:** gắn "guardrail" nhưng tool vẫn chạy trước khi kiểm, hoặc handoff sang specialist bỏ qua kiểm.
- **Cơ chế cốt lõi:** `InputGuardrail` mặc định `run_in_parallel=True` — model có thể đã tốn token và **thực thi tool trước khi bị hủy**. Input guardrail chỉ cho agent đầu chuỗi, output guardrail cho agent cuối; handoff không tự áp guardrail lên tool của specialist. Tool guardrails áp pipeline `FunctionTool` (kể cả local MCP có cấu hình), không áp trực tiếp cho handoff, hosted/built-in tools. `pre_approval_tool_input_guardrails=True` kiểm trước approval và kiểm lại sau. Bản đồ 7 vị trí guardrail trong mục 12 §4e: đầu vào (kể cả kết quả tool), truy xuất, trước gọi tool, môi trường chạy, đầu ra, duyệt người, **trần vòng/ngân sách**, kill switch + audit.
- **Áp dụng vào dự án khác:**
  1. Lập ma trận tool → pipeline → guardrail → principal → side effect.
  2. Kiểm điều kiện bắt buộc ở chế độ blocking và ngay tại side effect; không dựa output guardrail để "hoàn tác".
  3. Mỗi ô guardrail ghi rõ **code enforce** hay prompt dặn; ô chỉ có prompt không tính.
  4. Canary function tool có receipt: thử input bị từ chối, handoff, timeout, approval với args đổi.
  5. Xác minh: input bị từ chối ở blocking không khởi chạy hành động; mọi blocked/budget-exhausted có trạng thái riêng.
- **Phù hợp khi / Không nên khi:** Phù hợp agent có handoff và function tool. Không nên thêm vòng agent khi rule/state machine tất định giải được.
- **Rủi ro & điều kiện:** MIT; SDK không cấp quyền dùng model hay miễn nghĩa vụ dữ liệu; nghiệm thu **(chưa xác minh)** bằng thực nghiệm.
- **Thay thế:** NeMo Guardrails, Presidio, Prompt Guard 2 (mục 12 §4e); LangGraph `interrupt()` (1.23).
- **Hồ sơ gốc:** [02 §4h](02-agent-frameworks/README.md#factory-framework-guardrail-boundaries-2026-11-04) · `code-read` · 04/11/2026 · [12 §4e](12-ai-security-guardrails/README.md#4e-kiểm-infographic-5-vị-trí-cần-đặt-guardrails-trong-ai-agent-ảnh-người-dùng-gửi-2026-11-02) (`docs-read`, 02/11/2026)

### 1.22 Cedar / OpenFGA cho tool của agent — Quyết định "agent thay mặt ai, được làm gì trên tài nguyên tenant nào" bằng engine quyền

- **Giải quyết:** agent gọi tool hoặc RAG đọc được dữ liệu tenant khác; prompt hệ thống và token hợp lệ không đủ.
- **Cơ chế cốt lõi:** Cedar: ngôn ngữ/engine Rust, default deny, `forbid` thắng `permit`, có schema validator/CLI/WASM; nhưng `ErrorHandling::Skip` **bỏ qua policy lỗi** — một `forbid` lỗi không tự thành deny. OpenFGA: ReBAC kiểu Zanzibar, API `Check` user–relation–object, ghim `authorization_model_id`, `HIGHER_CONSISTENCY` bỏ cache; quickstart in-memory mất dữ liệu. Kiến trúc tham khảo: user/tenant xác thực → credential ngắn hạn → tool gateway gắn user/actor/tenant/resource/action từ dữ kiện tin cậy → engine quyết định → backend kiểm lại + audit.
- **Áp dụng vào dự án khác:**
  1. Chọn một engine: Cedar cho policy thuộc tính trong tiến trình; OpenFGA/SpiceDB cho kho quan hệ dùng chung.
  2. Tool gateway lấy `tenant_id` từ session đã xác thực, **không từ prompt**.
  3. Với Cedar: validate schema, coi diagnostics có lỗi là deny cho thao tác nhạy cảm; với OpenFGA: datastore bền, ghim model ID.
  4. Áp cùng ACL cho retrieval, download, mutation và job nền.
  5. Xác minh: cùng object ID khác tenant phải deny; revoke rồi kiểm lại với consistency đã chọn; engine timeout → hành động dừng.
- **Phù hợp khi / Không nên khi:** Phù hợp agent nhiều người dùng/tenant. Không nên vận hành cả OpenFGA lẫn SpiceDB cho cùng một bộ quyền.
- **Rủi ro & điều kiện:** cả hai Apache-2.0; không phải OAuth server; bảng cổng là đề xuất, **chưa chạy**.
- **Thay thế:** SpiceDB (ZedToken cho thu hồi); OPA tự tích hợp; SPIRE cho danh tính workload (không quyết định quyền).
- **Hồ sơ gốc:** [12 Cedar](12-ai-security-guardrails/README.md#cedar) · [12 OpenFGA](12-ai-security-guardrails/README.md#openfga) · `code-read` · 02/11/2026

### 1.23 LangGraph checkpoint + `interrupt()` — Dừng chờ người duyệt và sống lại sau lỗi, với ngữ nghĩa chạy lại rõ ràng

- **Giải quyết:** agent nhiều bước cần human-in-the-loop và phục hồi sau crash mà không lặp side effect.
- **Cơ chế cốt lõi:** `InMemorySaver` chỉ cho debug/test, production dùng PostgresSaver. `Pregel.stream` có durability `sync`/`async` (mặc định)/`exit`; **`durability` vô tác dụng nếu thiếu checkpointer**. `interrupt()` resume bằng **chạy lại node từ đầu**; nhiều interrupt khớp theo thứ tự — side effect trước interrupt phải idempotent hoặc tách node.
- **Áp dụng vào dự án khác:**
  1. Cấu hình checkpointer bền (Postgres) và chọn durability theo trade-off độ trễ/mất tiến trình.
  2. Tách side effect (gửi mail, trừ tiền) vào node riêng sau interrupt, có idempotency key.
  3. `thread_id` gắn tenant; màn duyệt hiển thị payload thật.
  4. Xác minh: kill tiến trình giữa bước rồi resume — state còn, side effect không lặp.
- **Phù hợp khi / Không nên khi:** Phù hợp luồng nhiều trạng thái có duyệt người. Không nên khi workflow hữu hạn ít nhánh (dùng hàm/queue tất định).
- **Rủi ro & điều kiện:** MIT; "có checkpoint" không có nghĩa exactly-once với dịch vụ ngoài.
- **Thay thế:** PydanticAI (output có kiểu + `UsageLimits`, cùng hồ sơ); 1.24 Temporal/Restate; Deep Agents (1.6).
- **Hồ sơ gốc:** [02 §4e](02-agent-frameworks/README.md#core-framework-semantics) · `code-read` · 02/11/2026

### 1.24 Temporal / Restate — Durable execution cho agent chạy lâu, kèm replay history và idempotency ở đích

- **Giải quyết:** agent chạy hàng giờ, gọi API ngoài, bị crash/deploy giữa chừng; retry gây gửi trùng, trừ tiền trùng.
- **Cơ chế cốt lõi:** Temporal Python SDK tách workflow tất định khỏi activity I/O; `RetryPolicy.maximum_attempts=0` là **không trần**; heartbeat phải gọi thật; `Replayer.replay_workflow(s)` mặc định `raise_on_replay_failure=True`, đặt `False` thì phải đọc `replay_failure(s)`. Restate TS SDK: `ctx.run` ghi kết quả vào journal; crash sau khi API ngoài đã ghi nhưng trước khi lưu vẫn gọi lại callback; ingress có idempotency key; timeout/retention tách bạch.
- **Áp dụng vào dự án khác:**
  1. Tách phần suy luận agent khỏi activity có side effect; đặt timeout, deadline và trần retry theo nghiệp vụ.
  2. Tạo business idempotency key ổn định **ngoài** callback và gửi tới nhà cung cấp.
  3. Lưu tập history đại diện (đã che dữ liệu) và replay trong CI trước mỗi rollout; có negative fixture nondeterministic; không chấp nhận tập rỗng.
  4. Fault injection: worker chết trước/sau API call, request lặp, hết lease.
  5. Xác minh: artifact gồm run ID + operation ID + số side effect cuối (=1 hoặc đối soát phát hiện trùng).
- **Phù hợp khi / Không nên khi:** Phù hợp agent có side effect thật, chạy dài, nhiều phiên bản code. Không nên cho tác vụ nhỏ (job/queue + outbox đủ).
- **Rủi ro & điều kiện:** SDK MIT (license engine Restate xét riêng ở mục 21 §5); history/journal chứa dữ liệu nhạy cảm cần retention/ACL; khả năng phục hồi **(chưa xác minh)** bằng chạy thử.
- **Thay thế:** DBOS (mục 21 §5); Hatchet (mục 21); 1.23 LangGraph checkpoint.
- **Hồ sơ gốc:** [21 §10i.1 Temporal](21-autonomous-workflows/README.md#temporal-replay-factory) · `code-read` · 04/11/2026 · [21 §10f Restate](21-autonomous-workflows/README.md#restate-typescript-sdk) · `code-read` · 02/11/2026

## 2. Tài liệu, dữ liệu, văn phòng & tự động hóa

Chương này chắt lọc 24 kỹ năng/công cụ trong kho `stored` hữu ích nhất cho các dự án xử lý giấy tờ văn phòng: điền báo cáo từ Excel tổng, trích hồ sơ chất lượng khách hàng, OCR PDF, RAG tiếng Việt trên quy trình/tiêu chuẩn, dashboard và gửi file qua email sau bước xác nhận. Tiêu chí chọn là mức hữu ích và bằng chứng trong hồ sơ, không phải số sao.

**Cách đọc mức bằng chứng:** `code-read` / `docs-read` theo [METHOD.md](METHOD.md) §2, tức kho đã đọc mã hoặc tài liệu tại commit ghim; **không có mục nào được kho cài, chạy hay benchmark**. "Chưa chuẩn hóa" nghĩa là hồ sơ Markdown có nghiên cứu nhưng bản ghi catalog chưa có `verification_level`. Mọi đường dẫn "Hồ sơ gốc" tính từ gốc repo `stored`.

### Nhu cầu → item nên dùng

| Nhu cầu của dự án | Item nên dùng trước | Đi kèm / thay thế |
|---|---|---|
| Điền báo cáo tự động từ file Excel tổng | 2.13 pandas + 2.14 Great Expectations (kiểm dữ liệu) → 2.1/2.2 skill xlsx/docx | 2.3 SheetJS (nếu app JS), 2.4 Typst (xuất PDF) |
| Trích hồ sơ chất lượng khách hàng (PDF/scan → trường có cấu trúc) | 2.7 Docling + 2.10 Cổng kiểm 6 bước của mục 26 | 2.9 PaddleOCR (bảng), 2.23 Label Studio (hàng chờ duyệt) |
| OCR PDF scan thành PDF tìm kiếm được | 2.8 OCRmyPDF (+ Tesseract `vie`) | 2.9 PaddleOCR khi có bảng/layout phức tạp |
| RAG tiếng Việt trên quy trình, tiêu chuẩn nội bộ | 2.11 embedding tiếng Việt BKAI/AITeamVN + 2.12 ViRE (đo retrieval) | 2.7 Docling (parse), 2.16 CocoIndex (cập nhật chỉ mục khi tài liệu đổi) |
| Văn bản tiếng Việt do agent sinh đúng chuẩn (NFC, kiểu dấu) | 2.15 linter design-os-vietnamese (lấy ý tưởng) | Cổng NFC tự viết theo 18 §5c |
| Dashboard cho quản lý | 2.18 Redash (SQL + lịch làm mới + cảnh báo) | Metabase, Superset, DataEase; 2.17 dlt để gom dữ liệu nguồn |
| Gửi file qua email sau khi người xác nhận | 2.22 Outbox + cổng duyệt (21 §8) → 2.21 gws CLI (Gmail, có `--dry-run`) | 2.20 Temporal (gửi bền, idempotent), listmonk/Novu |
| Cho agent dựng/sửa workflow n8n | 2.19 n8n-skills (czlonkowski) + n8n-mcp chạy cục bộ | Node-RED, n8n-agent-skills (chỉ lấy ý tưởng side-effects-gate) |
| Đo chất lượng skill "điền báo cáo" tự viết | 2.24 SkillsBench (khuôn task/oracle/verifier) | 2.6 notion-doc (template + lint đầu ra) |

---

### 2.1 anthropics/skills — docx/xlsx/pdf/pptx — Mẫu tham chiếu chính chủ cho agent đọc/ghi file Office và PDF

- **Giải quyết:** Cho coding agent một quy trình có sẵn để tạo, đọc, sửa Word/Excel/PowerPoint/PDF thay vì tự mò thư viện mỗi lần.
- **Cơ chế cốt lõi:** Repo `anthropics/skills` có 19 skill theo spec Agent Skills (`spec/agent-skills-spec.md`, `template/SKILL.md`); bốn skill tài liệu `docx`, `pdf`, `pptx`, `xlsx` nằm trong nhóm này. Cài bằng `/plugin marketplace add anthropics/skills`. README tự ghi "for demonstration and educational purposes only"; hành vi trong sản phẩm Claude có thể khác.
- **Áp dụng vào dự án khác:**
  1. Dùng bốn skill như **tài liệu tham khảo** để thiết kế skill nội bộ (ví dụ "điền mẫu báo cáo tháng"): đọc cấu trúc SKILL.md, cách chia script và bước kiểm.
  2. Viết skill riêng theo `template/SKILL.md` và spec Agent Skills, gắn đúng mẫu báo cáo của đơn vị.
  3. Nếu dùng trong Claude Code/Cowork cho việc nội bộ, cài theo phạm vi dự án và ghim commit. Muốn chép (vendor) mã skill vào repo sản phẩm thì đọc lại `LICENSE.txt` của đúng thư mục skill tại commit đã ghim: ngày 23/11/2026 bốn skill tài liệu có Apache-2.0 nhưng repo không có LICENSE ở gốc.
  4. Lấy thêm `skill-creator` (Apache-2.0) để tạo và eval skill riêng.
- **Phù hợp khi / Không nên khi:** Phù hợp khi cần khuôn mẫu chất lượng cho skill văn phòng và chạy trong môi trường Claude. Không nên khi cần hành vi ổn định cam kết lâu dài: README ghi "for demonstration and educational purposes only" và hành vi trong sản phẩm Claude có thể khác. Khi đóng gói lại mã skill, theo điều kiện Apache-2.0 trong từng thư mục (giữ thông báo, ghi thay đổi).
- **Rủi ro & điều kiện:** **Đính chính 23/11/2026:** hồ sơ 31/10/2026 ghi bốn skill tài liệu "© Anthropic, All rights reserved"; đọc lại tại commit `e4bb5d9` (16/11/2026) thì `skills/docx`, `pdf`, `pptx`, `xlsx` đều có `LICENSE.txt` Apache-2.0 và SKILL.md ghi "Complete terms in LICENSE.txt". Repo không có LICENSE ở gốc (GitHub báo không license) và `doc-coauthoring` không có file license, nên đừng suy license của skill từ gốc repo. License có thể đổi tiếp: đọc lại tại commit ghim trước khi dùng. Repo chỉ 61 commit, khoảng 1k PR mở: nhận đóng góp hạn chế. Dữ liệu rời máy tùy host agent/model đang dùng.
- **Thay thế:** 2.2 MiniMax skills (MIT, có `minimax-docx`/`minimax-xlsx`); 2.5 GenOffice; 2.3 SheetJS cho riêng bảng tính.
- **Hồ sơ gốc:** [20 §3s.4](20-claude-plugins-ecosystem/README.md#3s4-anthropicsskills--skill-mẫu-và-spec-agent-skills-của-anthropic) · hồ sơ gốc đọc 2026-10-31 (chưa chuẩn hóa); license đọc lại 2026-11-23 tại `e4bb5d9`

### 2.2 MiniMax-AI/skills (minimax-docx, minimax-xlsx, minimax-pdf, pptx-generator) — Bộ skill Office license MIT, có cổng XSD cho docx

- **Giải quyết:** Cần skill tạo DOCX/XLSX/PDF/PPTX nhưng muốn license thoáng để nhúng vào dự án.
- **Cơ chế cốt lõi:** 17 skill (Beta); nhóm tài liệu gồm `minimax-docx` dùng .NET OpenXML SDK kèm cổng XSD, `minimax-xlsx`, `minimax-pdf`, `pptx-generator`. Cài qua marketplace Claude Code, Cursor, Codex, OpenCode. Có `validate_skills.py` kiểm cấu trúc/frontmatter chạy tay; `CREDITS.md` ghi nguồn dẫn xuất.
- **Áp dụng vào dự án khác:**
  1. Chỉ cài nhóm tài liệu cần (ví dụ `minimax-docx`, `minimax-xlsx`), ghim SHA.
  2. Đọc `skills/minimax-docx/scripts/setup.sh` trước khi chạy (hồ sơ chưa đọc file này).
  3. Chuẩn bị phụ thuộc trong môi trường riêng: dotnet, `reportlab`, `pypdf`, Playwright theo skill.
  4. Đặt bộ file mẫu thật (mẫu báo cáo đơn vị) và so kết quả với skill Anthropic trước khi chọn.
  5. Giữ NOTICE khi nhúng phần dẫn xuất Apache-2.0.
- **Phù hợp khi / Không nên khi:** Phù hợp khi cần sinh Word chuẩn OOXML có kiểm schema và muốn license MIT. Không nên khi cần độ ổn định cao (Beta, có thể đổi không báo) hoặc khi không chấp nhận cài dotnet/Playwright.
- **Rủi ro & điều kiện:** MIT + Apache-2.0 cho phần dẫn xuất; `minimax-docx` có LICENSE MIT riêng. Không có CI. Nhóm media (`vision-analysis`…) gửi ảnh người dùng tới API MiniMax: **không dùng cho hồ sơ khách hàng**. Hành vi script setup/render **(chưa xác minh)**.
- **Thay thế:** 2.1 anthropics/skills; 2.5 GenOffice; 2.4 Typst cho đầu ra PDF.
- **Hồ sơ gốc:** [20 · MiniMax-AI/skills](20-claude-plugins-ecosystem/README.md#xlsx-2026-11-23-minimax-skills) · docs-read · 2026-11-23

### 2.3 SheetJS Community Edition — Đọc/ghi nhiều định dạng bảng tính trong ứng dụng JavaScript

- **Giải quyết:** Đọc file Excel tổng hoặc xuất bảng tính từ web app/Node mà không cần Office.
- **Cơ chế cốt lõi:** Bản Community Edition tập trung chuyển đổi dữ liệu workbook; README phân biệt rõ khả năng nâng cao thuộc SheetJS Pro. Repo GitHub nay chỉ hướng dẫn sang `git.sheetjs.com`, bản trên GitHub không đại diện phát hành mới nhất.
- **Áp dụng vào dự án khác:**
  1. Lấy package theo nguồn chính thức mới trong README, ghim phiên bản.
  2. Viết lớp đọc "Excel tổng" → JSON có schema (tên sheet, dòng tiêu đề, kiểu cột).
  3. Thử bằng workbook thật: công thức, ô gộp, định dạng ngày/tiền Việt Nam, file lớn.
  4. Nếu cần giữ định dạng/công thức khi ghi lại, kiểm round-trip trước khi dùng thật.
- **Phù hợp khi / Không nên khi:** Phù hợp cho app JS/TS cần nhập–xuất dữ liệu bảng. Không nên khi cần giữ nguyên định dạng phức tạp của mẫu báo cáo (tính năng có thể nằm ở bản Pro) hoặc stack là Python.
- **Rủi ro & điều kiện:** Apache-2.0. Chạy cục bộ, không có dữ liệu rời máy theo mô tả. Round-trip công thức/định dạng/file lớn **(chưa xác minh)**.
- **Thay thế:** ExcelJS, openpyxl, LibreOffice (liệt kê trong hồ sơ, chưa có hồ sơ riêng); 2.13 pandas phía Python.
- **Hồ sơ gốc:** [16 · SheetJS](16-docs-tools/README.md#anhkysuai-2026-11-23-sheetjs-community-edition) · docs-read · 2026-11-23

### 2.4 Typst — Dàn trang báo cáo PDF từ markup có template, quản lý cùng phiên bản dự án

- **Giải quyết:** Xuất báo cáo PDF đẹp, ổn định từ dữ liệu, thay cho việc chỉnh tay Word.
- **Cơ chế cốt lõi:** Compiler và CLI Rust dàn trang tài liệu từ markup; có set/show rules và scripting tích hợp, toán học và tài liệu tham khảo. Giao diện cộng tác online là dịch vụ khác với compiler trong repo.
- **Áp dụng vào dự án khác:**
  1. Ghim phiên bản compiler, font (có dấu tiếng Việt) và template trong repo.
  2. Viết template báo cáo; truyền dữ liệu đã kiểm (từ 2.13/2.14) vào bằng scripting.
  3. Tạo fixture: một bộ dữ liệu mẫu → PDF kỳ vọng; so PDF sinh ra mỗi lần đổi template.
  4. Chạy compiler trong CI hoặc trong bước "sinh bản nháp" của quy trình.
- **Phù hợp khi / Không nên khi:** Phù hợp khi đầu ra cuối là PDF và người nhận không cần sửa. Không nên khi khách hàng bắt buộc nhận file Word/Excel sửa được.
- **Rủi ro & điều kiện:** Apache-2.0; chạy cục bộ. Font và gói bổ sung quản lý riêng. Chưa biên dịch corpus thật **(chưa xác minh chất lượng tiếng Việt)**.
- **Thay thế:** pandoc ([08 §6c.5.8](08-awesome-lists-learning/README.md#6c58-editor-terminal--dòng-lệnh)), tectonic, quarto.
- **Hồ sơ gốc:** [16 · Typst](16-docs-tools/README.md#anhkysuai-2026-11-23-typst) · docs-read · 2026-11-23

### 2.5 GenOffice — Bộ soạn Office có agent, sửa OOXML kèm tracked changes, có CLI và MCP

- **Giải quyết:** Để AI sửa tài liệu/bảng tính/slide có cấu trúc mà người duyệt vẫn thấy được thay đổi (tracked changes/diff).
- **Cơ chế cốt lõi:** README mô tả chỉnh sửa OOXML, tracked changes/diff và export về định dạng gốc; monorepo tách ứng dụng và engine; có CLI/MCP/headless. Tính năng ẩn nội dung chỉ áp dụng cho AI trong app, còn CLI/MCP/headless vẫn đọc file trực tiếp.
- **Áp dụng vào dự án khác:**
  1. Chỉ làm việc trên **bản sao** tài liệu.
  2. Thử luồng "agent sửa → tracked changes → người duyệt chấp nhận" trên một mẫu báo cáo thật.
  3. Mở lại file kết quả trong Microsoft Office/LibreOffice để kiểm round-trip.
  4. Kiểm endpoint AI đang cấu hình trước khi đưa tài liệu nhạy cảm vào.
- **Phù hợp khi / Không nên khi:** Phù hợp khi người duyệt quen làm việc bằng tracked changes. Không nên khi chưa kiểm cam kết "giữ byte không đổi" trên file của mình.
- **Rủi ro & điều kiện:** Apache-2.0 kèm Unicode License V3. Nội dung có thể đi tới model AI đã cấu hình. Tương thích Office và giữ byte **(chưa xác minh)**.
- **Thay thế:** onlyoffice, libreoffice (nêu trong hồ sơ); 2.1/2.2 skill docx.
- **Hồ sơ gốc:** [16 · GenOffice](16-docs-tools/README.md#anhkysuai-2026-11-23-genoffice) · docs-read · 2026-11-23

### 2.6 agent-notion-template-docs (notion-doc) — Mẫu "một template chuẩn + lint chặn lệch + hook nhắc" cho định dạng đầu ra

- **Giải quyết:** Agent mỗi lần sinh báo cáo HTML một kiểu; cần khóa hình thức đầu ra về một template.
- **Cơ chế cốt lõi:** Một `template.html` chuẩn (CSS token) thay cho CSS agent tự chế. Hook `PostToolUse` chạy `notion-doc-lint.py`: file có dấu vân tay template thì lint bắt class/CSS lạ; HTML tài liệu thiếu dấu vân tay thì nhắc nạp skill; lỗi thì fail-open. CI lint ví dụ, test hook; workflow hằng tuần so token với ảnh chụp tham chiếu. Chỉ quyết định **hình thức**, không lấy dữ liệu từ Notion.
- **Áp dụng vào dự án khác:**
  1. Thiết kế một template báo cáo/email chuẩn của đơn vị, gắn dấu vân tay.
  2. Viết lint so file đầu ra với template (class/token cho phép).
  3. Gắn lint vào hook sau khi agent ghi file, và vào CI.
  4. Đổi mô tả skill để không "MUST" cho mọi tài liệu; tự lưu Prism nếu cần chạy offline.
- **Phù hợp khi / Không nên khi:** Phù hợp cho báo cáo HTML/email nội bộ cần nhìn thống nhất. Không nên dùng nguyên giao diện kiểu Notion cho sản phẩm công khai khi chưa xem điều khoản thương hiệu.
- **Rủi ro & điều kiện:** MIT. Template nạp Prism từ cdnjs (script ngoài). Skill tự nhận quyền với mọi tài liệu, sẽ giành với skill khác. Một tác giả, 31 commit. Chưa chạy lint/hook.
- **Thay thế:** obsidian-skills (16), `canvas-design` trong 2.1; 2.4 Typst cho đầu ra PDF.
- **Hồ sơ gốc:** [16 · notion-doc](16-docs-tools/README.md#xlsx-2026-11-23-agent-notion-template-docs) · docs-read · 2026-11-23

### 2.7 Docling — Parser tài liệu (PDF, Office, HTML…) ra Markdown/JSON cho RAG và trích xuất, có trạng thái partial

- **Giải quyết:** Biến hồ sơ PDF/DOCX/PPTX của khách hàng thành text có cấu trúc (bảng, layout) để trích trường hoặc đưa vào RAG.
- **Cơ chế cốt lõi:** Mặc định `enable_remote_services=False`, `allow_external_plugins=False`, nhưng `artifacts_path=None` sẽ lấy model từ xa khi cần. `convert_all()` cho `PARTIAL_SUCCESS` đi tiếp kể cả khi `raises_on_error=True`; `document_timeout` có thể cho kết quả partial. `max_num_pages`/`max_file_size` mặc định là `sys.maxsize`.
- **Áp dụng vào dự án khác:**
  1. Đặt giới hạn trang/kích thước/thời gian tường minh; chạy parser trong sandbox.
  2. Tải model artifacts về cục bộ, cấu hình `artifacts_path`, rồi kiểm lưu lượng mạng thực tế nếu cần offline.
  3. Ghi trạng thái `success/partial/failed` từng trang; trang partial vào hàng chờ duyệt, không đưa vào chỉ mục như bản đủ.
  4. Lưu `document_hash`, trang, bbox (nếu có), phiên bản parser/model cùng mỗi block.
  5. Đo trên corpus hồ sơ thật có nhãn trước khi dùng (xem 2.10).
- **Phù hợp khi / Không nên khi:** Phù hợp cho PDF có lớp text và tài liệu Office nhiều định dạng. Không nên coi "không ném exception" là xử lý đủ; với scan chất lượng kém, so thêm 2.8/2.9.
- **Rủi ro & điều kiện:** MIT cho thư viện; quyền weights/model **phải kiểm riêng**. Hai cờ mặc định false **chưa chứng minh chạy hoàn toàn offline**. Chưa convert tài liệu nào trong kho.
- **Thay thế:** 2.9 PaddleOCR (PP-StructureV3); MinerU, Marker (mục 26, chú ý license weights/doanh thu).
- **Hồ sơ gốc:** [26 · Docling](26-document-intelligence-ocr/README.md#docling-factory) · code-read · 2026-11-04

### 2.8 OCRmyPDF (+ Tesseract) — Thêm lớp text vào PDF scan để tìm kiếm, chạy CPU

- **Giải quyết:** Kho hồ sơ scan không tìm kiếm được; cần OCR hàng loạt mà vẫn giữ PDF gốc.
- **Cơ chế cốt lõi:** OCRmyPDF là CLI/Python API nối Tesseract, thêm lớp text vào PDF scan, **kiểm language pack tồn tại trước khi xử lý** (`_validation.py`). Tesseract có API Init/Recognize, xuất hOCR/TSV; language pack là artifact phải ghim riêng.
- **Áp dụng vào dự án khác:**
  1. Cài Tesseract kèm language pack `vie`, ghim phiên bản Ghostscript/Tesseract.
  2. Tiền xử lý: kiểm DPI, xoay/nghiêng trước OCR.
  3. Chạy OCRmyPDF theo lô trong sandbox có trần tài nguyên; giữ file gốc và hash.
  4. Đo CER trên một tập trang tiếng Việt có bản gõ chuẩn trước khi triển khai rộng.
- **Phù hợp khi / Không nên khi:** Phù hợp cho scan sạch, cần searchable PDF, máy chỉ có CPU. Không nên dùng để trích bảng/trường hóa đơn: searchable PDF không chứng minh hiểu bảng.
- **Rủi ro & điều kiện:** OCRmyPDF MPL-2.0, dependency có license riêng; Tesseract Apache-2.0. Chạy cục bộ. Độ đúng tiếng Việt phụ thuộc tiền xử lý **(chưa xác minh)**.
- **Thay thế:** 2.9 PaddleOCR; Umi-OCR, Tesseract.js (mục 26).
- **Hồ sơ gốc:** [26 · OCRmyPDF](26-document-intelligence-ocr/README.md#ocrmypdf), [26 · Tesseract](26-document-intelligence-ocr/README.md#tesseract) · code-read · 2026-11-02

### 2.9 PaddleOCR (PP-StructureV3) — OCR kèm phân tích layout và bảng, ghép Markdown nhiều trang

- **Giải quyết:** Hồ sơ chất lượng có bảng thông số, biểu mẫu nhiều cột mà OCR thuần không giữ được cấu trúc.
- **Cơ chế cốt lõi:** PP-StructureV3 tách layout/OCR/table và ghép Markdown nhiều trang; wrapper kiểm tổ hợp ngôn ngữ/phiên bản OCR. API Python/pipeline qua PaddleX.
- **Áp dụng vào dự án khác:**
  1. Ghim backend và model revision.
  2. Chạy trên tập hồ sơ mẫu có bảng; đo cả cấu trúc bảng lẫn giá trị từng ô.
  3. Giữ tọa độ nguồn để người duyệt đối chiếu ảnh gốc.
  4. So với Docling trên cùng tập trước khi chọn.
- **Phù hợp khi / Không nên khi:** Phù hợp khi tài liệu nhiều bảng/layout và chấp nhận dựng môi trường Paddle. Không nên lấy điểm SOTA trong README làm đại diện cho biểu mẫu tiếng Việt.
- **Rủi ro & điều kiện:** Apache-2.0 cho code; **quyền từng checkpoint chưa xác minh**. Chưa chạy CPU/GPU; độ đúng biểu mẫu tiếng Việt **(chưa xác minh)**.
- **Thay thế:** 2.7 Docling; MinerU (Apache-2.0 + điều khoản bổ sung theo MAU/doanh thu); Surya (license model có ngưỡng doanh thu).
- **Hồ sơ gốc:** [26 · PaddleOCR](26-document-intelligence-ocr/README.md#paddleocr) · code-read · 2026-11-02

### 2.10 Cổng kiểm 6 bước cho pipeline tài liệu (mục 26 §3, §5) — Hợp đồng để trích trường có bằng chứng, không chỉ "JSON hợp lệ"

- **Giải quyết:** Trích hồ sơ khách hàng ra JSON trông đúng nhưng sai số tiền, mã số, thiếu trang mà không ai biết.
- **Cơ chế cốt lõi:** Sáu cổng: (1) đầu vào bất biến (hash, số trang, nguồn/quyền, native/scan); (2) chuẩn hóa có ảnh trước/sau, NFC để chấm nhưng giữ bản gốc; (3) block có `document_hash`, `page`, `bbox`, `parser_ref`, `model_revision`, trạng thái fallback; (4) trích theo schema, trường thiếu trả `null` + lý do, citation trỏ đúng vùng; (5) chấm trên tập đích (CER, TEDS, precision/recall từng trường); (6) review trọng tâm số tiền, mã số thuế, điều khoản. Đây là khuyến nghị của kho, chưa chạy.
- **Áp dụng vào dự án khác:**
  1. Viết schema trường của "hồ sơ chất lượng" (kiểu, đơn vị, định dạng ngày/tiền, luật chéo trường).
  2. Lưu `raw value`, `normalized value`, nguồn (trang/bbox) và trạng thái cho mỗi trường.
  3. Phân biệt rõ "thiếu", "không đọc được", "không áp dụng"; không đổi thành chuỗi rỗng.
  4. Lập tập 30–100 hồ sơ có nhãn, đo từng trường; ngưỡng lấy từ hậu quả sai.
  5. Đưa trường quan trọng hoặc độ tin thấp vào hàng chờ duyệt (2.23).
- **Phù hợp khi / Không nên khi:** Phù hợp cho mọi luồng trích xuất có hậu quả nghiệp vụ. Không cần đầy đủ khi chỉ OCR để tìm kiếm.
- **Rủi ro & điều kiện:** Không phụ thuộc license. Chi phí lớn nhất là tạo tập nhãn và thời gian người duyệt. Ngưỡng cụ thể do dự án tự đặt.
- **Thay thế:** OmniDocBench (đo parser, dataset kiểm riêng) ở mục 26; cổng dữ liệu của mục 24 §5.
- **Hồ sơ gốc:** [26 §3](26-document-intelligence-ocr/README.md#3-cổng-kiểm-cho-pipeline-tài-liệu), [26 §5](26-document-intelligence-ocr/README.md#factory-2026-11-04) · khuyến nghị tổng hợp, chưa chạy · 2026-11-02 / 2026-11-04

### 2.11 Embedding tiếng Việt BKAI bi-encoder / AITeamVN Vietnamese_Embedding — Cặp embedding thực dụng cho RAG tiếng Việt

- **Giải quyết:** Tìm đúng đoạn trong quy trình, tiêu chuẩn nội bộ bằng câu hỏi tiếng Việt.
- **Cơ chế cốt lõi:** `bkai-foundation-models/vietnamese-bi-encoder` (Apache-2.0, nền PhoBERT, khoảng 485k lượt tải/tháng, MRR@10 80,73 trên Zalo Legal 2021); `AITeamVN/Vietnamese_Embedding` (Apache-2.0, BGE-M3 tinh chỉnh 300k bộ ba, ngữ cảnh 2.048 token, MRR@10 0,818). VN-MTEB (mục 18 §5b) có 50 task tiếng Việt và đã khai báo sẵn các model này.
- **Áp dụng vào dự án khác:**
  1. Gom 50–200 câu hỏi thật kèm đoạn đúng (qrels) từ chính tài liệu quy trình.
  2. Chạy cả hai embedding (và BM25) trên cùng chunking, đo nDCG@10/Recall@10.
  3. Chạy phần retrieval của VN-MTEB để có baseline độc lập.
  4. Chọn model theo điểm trên dữ liệu của mình; ghi revision model.
- **Phù hợp khi / Không nên khi:** Phù hợp cho RAG tự host, dữ liệu không được rời máy. Không nên tin điểm công bố: cả hai chỉ có điểm **tự báo cáo trên một tập pháp luật**; BKAI huấn luyện phần lớn trên dữ liệu dịch máy.
- **Rủi ro & điều kiện:** Apache-2.0 (theo trang HF). Chạy cục bộ sau khi tải model. Task VN-MTEB phần lớn dịch từ tiếng Anh, cách dịch **(chưa xác minh)**. Catalog chưa chuẩn hóa mức kiểm cho hai model.
- **Thay thế:** BGE-M3/bge-reranker (FlagEmbedding, mục 10); `elasticsearch-analysis-vietnamese` cho BM25 (mục 18 §4d).
- **Hồ sơ gốc:** [18 §4c](18-vietnam-community/README.md#4c-repo--model-tiếng-việt-đã-xác-minh-2026-10-12), [18 §5b](18-vietnam-community/README.md#5b-nâng-trần-2112026-benchmark-tiếng-việt-chạy-được-và-cổng-kiểm-văn-bản-tiếng-việt-yêu-cầu-người-dùng) · chưa chuẩn hóa (số liệu đọc HF/GitHub) · 2026-10-12 / 2026-11-02

### 2.12 ViRE — Giao thức đo retrieval tiếng Việt xuyên domain (BM25, dense, sparse, hybrid)

- **Giải quyết:** Biết chắc hệ RAG tiếng Việt tìm đúng tài liệu trước khi lo câu trả lời.
- **Cơ chế cốt lõi:** Benchmark retrieval đa domain (paper EACL 2026: sáu domain, mười dataset), so lexical/dense/sparse/late-interaction/hybrid cùng giao thức. Đọc `cli.py`/`metrics.py`: quickstart lấy mẫu cả query lẫn candidate corpus; metric loại gold index ngoài miền và có heuristic đổi chỉ số 1-based.
- **Áp dụng vào dự án khác:**
  1. Dùng CLI/metric của ViRE trên tập câu hỏi–đoạn của chính dự án.
  2. Báo kích thước candidate pool; kiểm coverage/qrels và chuẩn hóa ID tường minh.
  3. So BM25, embedding (2.11), hybrid rồi reranker trên cùng corpus/chunking.
  4. Không dùng điểm trên corpus lấy mẫu làm đại diện chỉ mục production đầy đủ.
- **Phù hợp khi / Không nên khi:** Phù hợp làm cổng retrieval trong CI của RAG tiếng Việt. Không nên chuyển kết quả trên bộ giáo dục thành kết luận cho pháp lý/kỹ thuật.
- **Rủi ro & điều kiện:** Code MIT; quyền dữ liệu nguồn kiểm từng dataset. 7★, ít người bảo trì. Chưa tái lập điểm.
- **Thay thế:** VN-MTEB (mục 18 §5b), MTEB task tùy biến (mục 10).
- **Hồ sơ gốc:** [18 §5c](18-vietnam-community/README.md#5c-vietnamese-domain-evaluation) · code-read · 2026-11-02

### 2.13 pandas — Nền biến đổi tất định cho "Excel tổng → bảng báo cáo"

- **Giải quyết:** Đọc file Excel tổng, lọc, gộp, tính chỉ tiêu cho báo cáo một cách lặp lại được.
- **Cơ chế cốt lõi:** Thư viện Python xử lý bảng và chuỗi thời gian; build Meson/Cython, phụ thuộc NumPy. Hồ sơ khuyên chốt dtype, quy tắc null, timezone và lưu phép biến đổi thay vì chỉ lưu bảng kết quả.
- **Áp dụng vào dự án khác:**
  1. Viết hàm `load_master(path)` khai báo rõ sheet, dòng tiêu đề, dtype từng cột.
  2. Viết các phép biến đổi thành hàm thuần, có test với file Excel mẫu nhỏ.
  3. Chuẩn hóa ngày/tiền/đơn vị và chuỗi tiếng Việt (NFC) ngay khi đọc.
  4. Kiểm dữ liệu bằng 2.14 trước khi đổ vào mẫu (2.1/2.2/2.4).
- **Phù hợp khi / Không nên khi:** Phù hợp cho file Excel cỡ vừa, stack Python. Không nên khi dữ liệu quá lớn so với RAM (cân nhắc Polars/DuckDB).
- **Rủi ro & điều kiện:** BSD-3-Clause; chạy cục bộ. Chưa thử tải dữ liệu/tương thích phiên bản.
- **Thay thế:** Polars, DuckDB, dask (nêu trong hồ sơ); 2.3 SheetJS phía JS.
- **Hồ sơ gốc:** [15 · pandas](15-ai-for-data/README.md#anhkysuai-2026-11-23-pandas) · docs-read · 2026-11-23

### 2.14 Great Expectations (GX Core) — "Unit test cho dữ liệu" chặn báo cáo khi Excel nguồn sai

- **Giải quyết:** Báo cáo tự động đúng công thức nhưng sai vì dữ liệu nguồn thiếu, trùng, sai kiểu.
- **Cơ chế cốt lõi:** Expectation + Checkpoint, Python 3.10–3.14. Bản mới đóng gói agent skill: mỗi thư mục skill có manifest sở hữu (phiên bản + hash), chạy lại là no-op, không ghi đè thư mục người dùng đã sửa. Hồ sơ đề xuất: contract fail thì agent báo "dữ liệu chưa đạt" thay vì trả lời.
- **Áp dụng vào dự án khác:**
  1. Viết expectation cho Excel tổng: cột bắt buộc, kiểu, khoảng giá trị, khóa không trùng.
  2. Chạy Checkpoint ngay sau bước đọc (2.13).
  3. Fail → dừng quy trình, gửi thông báo lỗi dữ liệu cho người phụ trách, không sinh báo cáo.
  4. Lưu kết quả kiểm cùng bản báo cáo để truy vết.
- **Phù hợp khi / Không nên khi:** Phù hợp khi báo cáo định kỳ dựa trên dữ liệu người khác nhập tay. Không nên dùng nếu chỉ một vài kiểm đơn giản (assert trong pandas có thể đủ).
- **Rủi ro & điều kiện:** Apache-2.0, đóng góp cần ký CLA. Repo đã chuyển sang tổ chức Fivetran (lý do **chưa xác minh**); giá trị mặc định của `GX_ANALYTICS_ENABLED` **chưa xác minh**, nên đặt tắt tường minh.
- **Thay thế:** Soda Core (Elastic License 2.0, không phải OSI); data test của dbt; pandera (ứng viên được nhắc, chưa có hồ sơ).
- **Hồ sơ gốc:** [15 §4](15-ai-for-data/README.md#4-nâng-trần-2112026-đo-độ-đúng-text-to-sql-data-contract-và-lineage-yêu-cầu-người-dùng) · chưa chuẩn hóa (đọc LICENSE/README/installer, không chạy) · 2026-11-02

### 2.15 design-os-vietnamese (linter `validate_copy.py`) — Cổng máy cho văn bản tiếng Việt do agent sinh

- **Giải quyết:** Báo cáo/email tiếng Việt do agent viết lẫn Unicode NFD, kiểu dấu cũ/mới (`hoà`/`hòa`), câu dịch máy.
- **Cơ chế cốt lõi:** Linter offline `shared/scripts/validate_copy.py` (1.745 dòng): chuẩn hóa NFC, kiểu dấu, câu dịch máy, luật theo ngành; `check_i18n_parity.py` kiểm khớp khóa và plural ICU en/vi. 16 skill cho Claude Code/Codex/Gemini, CI chạy unittest.
- **Áp dụng vào dự án khác:**
  1. Đọc linter để lấy danh sách luật (NFC, một kiểu dấu thống nhất, mẫu câu dịch máy).
  2. Nếu dự án có thể cạnh tranh với tác giả: **tự viết lại** cổng tương tự, không nhúng mã.
  3. Chạy cổng trên mọi văn bản đầu ra (thân email, báo cáo) trước bước duyệt.
  4. Thêm danh sách thuật ngữ chuẩn của đơn vị.
- **Phù hợp khi / Không nên khi:** Phù hợp khi văn bản gửi khách hàng/cơ quan. Không thay người chấm nội dung chuyên môn; luật pháp lý trong rule chưa đối chiếu văn bản gốc.
- **Rủi ro & điều kiện:** **PolyForm Shield 1.0.0**, không phải OSI, cấm dùng trong sản phẩm cạnh tranh với tác giả. README ghi 489 cặp eval nhưng đếm được 575 dòng. Chạy offline.
- **Thay thế:** Cổng NFC/CLDR tự viết theo 18 §5c.2; Vale (mục 16) cho lint văn xuôi.
- **Hồ sơ gốc:** [18 §5d](18-vietnam-community/README.md#5d-hồ-sơ-jangtrinhdesign-os-vietnamese-16-skill-viết-tiếng-việt-theo-ngành-linter-tất-định-và-kho-tri-thức-có-neo-sha-256-link-người-dùng-gửi-đọc-mã-3112026) · code-read · 2026-11-03

### 2.16 CocoIndex — Cập nhật chỉ mục RAG theo thay đổi nguồn, tái dùng tính toán qua khóa memo

- **Giải quyết:** Quy trình/tiêu chuẩn được sửa thường xuyên; không muốn parse và embed lại toàn bộ kho mỗi lần.
- **Cơ chế cốt lõi:** Framework khai báo biến đổi dữ liệu và cập nhật chỉ mục khi nguồn đổi. `memo_fingerprint` canonicalize kiểu dữ liệu/custom hook rồi tạo fingerprint qua lõi Rust; `fingerprint_call` ghép hàm, đối số và version để tái dùng kết quả khi đầu vào không đổi.
- **Áp dụng vào dự án khác:**
  1. Khai báo luồng: thư mục tài liệu → parse (2.7) → chunk → embed (2.11) → chỉ mục.
  2. Đưa version parser/model vào khóa memo để đổi model thì tính lại.
  3. Thử sửa một file, xóa một file, rồi kiểm chỉ mục đích không còn nội dung cũ.
  4. Giữ trang/nguồn trong metadata chunk để trích dẫn.
- **Phù hợp khi / Không nên khi:** Phù hợp cho kho tài liệu sống, cập nhật thường xuyên. Không nên khi kho nhỏ và tĩnh (index lại toàn bộ đơn giản hơn).
- **Rủi ro & điều kiện:** Apache-2.0. Hồ sơ **chỉ kiểm phần khóa memo Python**, chưa chứng minh engine incremental hay connector đầu–cuối; khóa thiếu phụ thuộc có thể gây cache cũ.
- **Thay thế:** 2.17 dlt; LlamaIndex; unstructured (mục 08).
- **Hồ sơ gốc:** [24 · CocoIndex](24-ai-data-engineering/README.md#anhkysuai-2026-11-23-cocoindex) · code-read · 2026-11-23

### 2.17 dlt (data load tool) — Gom dữ liệu từ API/file vào kho phân tích, có cursor và merge

- **Giải quyết:** Dashboard cần dữ liệu từ nhiều hệ thống (ERP, Sheets, API) cập nhật định kỳ mà không viết script tay mỗi nguồn.
- **Cơ chế cốt lõi:** Ingestion Python; `Incremental` giữ cursor và xử lý trùng vùng biên; merge loading mới là nơi upsert/dedup theo khóa. Telemetry `dlthub_telemetry=True` mặc định, tắt bằng `[runtime] dlthub_telemetry=false`.
- **Áp dụng vào dự án khác:**
  1. Viết hợp đồng nguồn: owner, timezone/cursor, khóa, SLA cập nhật.
  2. Cấu hình incremental + merge theo khóa; thiết kế cửa sổ lag cho bản ghi đến muộn.
  3. Tắt telemetry trong cấu hình.
  4. Thử replay nhỏ có insert/update/delete/trùng trước khi chạy lịch thật.
- **Phù hợp khi / Không nên khi:** Phù hợp cho nguồn API/file theo giờ, số nguồn vừa phải. Không nên coi `max(updated_at)` là bảo đảm không mất bản ghi; CSDL thay đổi liên tục cần CDC (Debezium).
- **Rủi ro & điều kiện:** Apache-2.0; telemetry bật mặc định. Chưa chạy.
- **Thay thế:** Dagster (orchestration asset), Debezium (CDC), Airbyte (Elastic-2.0, mục 24).
- **Hồ sơ gốc:** [15 §5](15-ai-for-data/README.md#5-data-ingestion-and-asset-orchestration) · code-read · 2026-11-02

### 2.18 Redash — Dashboard từ SQL, lịch làm mới và cảnh báo, cộng tác trên truy vấn

- **Giải quyết:** Quản lý cần xem chỉ tiêu cập nhật mà không phải chờ báo cáo tay.
- **Cơ chế cốt lõi:** SQL editor, schema browser, API; chia sẻ biểu đồ/dashboard, lịch làm mới và cảnh báo.
- **Áp dụng vào dự án khác:**
  1. Tạo tài khoản CSDL **chỉ đọc** cho Redash.
  2. Dựng một dashboard nhỏ từ bảng đã qua cổng 2.14/2.17.
  3. Đặt giới hạn truy vấn và tần suất làm mới; đo tải lên nguồn.
  4. Kiểm phạm vi chia sẻ dashboard theo người xem.
- **Phù hợp khi / Không nên khi:** Phù hợp cho nhóm biết SQL, muốn dashboard nhanh, license thoáng. Không nên khi cần phân quyền dữ liệu chi tiết từng người dùng mà chưa kiểm.
- **Rủi ro & điều kiện:** BSD-2-Clause; tài sản bản đồ có `LICENSE.borders` riêng. Quyền datasource và thực thi truy vấn **(chưa xác minh)**.
- **Thay thế:** Metabase (AGPL-3.0), Apache Superset (Apache-2.0, có MCP server), DataEase (GPLv3 sửa đổi, điều kiện thương hiệu).
- **Hồ sơ gốc:** [15 · Redash](15-ai-for-data/README.md#anhkysuai-2026-11-23-redash), [15 · bảng BI](15-ai-for-data/README.md#bổ-sung-text-to-sql-bi-có-ai--lớp-metadata-đã-xác-minh-2026-10-12) · docs-read · 2026-11-23

### 2.19 n8n-skills (czlonkowski) + n8n-mcp — Cho coding agent dựng, kiểm và vận hành workflow n8n

- **Giải quyết:** Muốn agent xây luồng tự động (đọc mail, lưu file, gọi API) trên n8n mà không sai node/tham số.
- **Cơ chế cốt lõi:** 14 skill + 1 router; `hooks.json` gắn `SessionStart`, 7 `PreToolUse` (create/update/validate/test workflow, credentials…) và 1 `PostToolUse`; hook chỉ chèn nhắc, không chặn (fail open). `create-workflow.sh` quét node Code/HTTP thiếu ghi chú "Why". Có 5 build-task chấm bằng `score.py`. Skill `n8n-self-hosting` kèm compose/Caddyfile với mặc định an toàn. Server `n8n-mcp`: 7 tool tra cứu + 21 tool quản lý, tắt tool ghi/xóa bằng `DISABLED_TOOLS`.
- **Áp dụng vào dự án khác:**
  1. Chạy `n8n-mcp` cục bộ qua `.mcp.json.example` (stdio), **không** dùng endpoint hosted khi workflow chứa dữ liệu khách hàng.
  2. Tắt telemetry n8n-mcp (`N8N_MCP_TELEMETRY_DISABLED=true`) trước lần chạy đầu.
  3. Dùng `DISABLED_TOOLS` để tắt tool xóa/credential khi agent chỉ cần dựng nháp.
  4. Ghim SHA plugin, đọc `hooks/` trước khi bật; cài `jq`.
  5. Export workflow ra JSON trong git, kiểm bằng validate trước khi deploy (05 §Nâng trần 2/11).
- **Phù hợp khi / Không nên khi:** Phù hợp khi đã chọn n8n làm nền automation. Không nên khi license n8n (Sustainable Use, không OSI) không hợp mô hình kinh doanh.
- **Rủi ro & điều kiện:** n8n-skills MIT (hook dẫn xuất Apache-2.0); n8n-mcp MIT, **telemetry bật mặc định thu workflow đã làm sạch và câu intent để làm dataset ML**, không đọc `DO_NOT_TRACK`. `mcp.json` gốc trỏ dịch vụ hosted của tác giả. Không CI; gần như một tác giả. Chưa chạy hook/eval.
- **Thay thế:** n8n-agent-skills (tmolavi, chỉ lấy ý `side-effects-gate.sh`), Node-RED (05, chú ý `adminAuth` ≠ `httpNodeAuth`), Activepieces/Kestra/Windmill (21 §6).
- **Hồ sơ gốc:** [05 · n8n-skills](05-low-code-llm-platforms/README.md#xlsx-2026-11-23-n8n-skills-czlonkowski), [05 · n8n-mcp](05-low-code-llm-platforms/README.md#hồ-sơ-từng-repo) · code-read (n8n-skills); n8n-mcp chưa chuẩn hóa · 2026-11-23 / 2026-10-31

### 2.20 Temporal Python SDK — Chạy bền bước gửi mail/ghi hệ thống, retry có trần và kiểm replay khi đổi code

- **Giải quyết:** Quy trình nhiều bước (chờ duyệt hàng giờ rồi gửi) không được mất trạng thái khi restart và không được gửi trùng.
- **Cơ chế cốt lõi:** Workflow tất định + activity làm I/O; activity có `start_to_close_timeout`, `schedule_to_close_timeout`, `heartbeat_timeout`, retry policy. `RetryPolicy.maximum_attempts=0` = **không giới hạn**. `Replayer.replay_workflow(s)` mặc định ném lỗi khi replay thất bại; dùng history thật làm regression. Retry activity **không** mang lại exactly-once cho API ngoài.
- **Áp dụng vào dự án khác:**
  1. Tách bước suy luận/sinh nháp khỏi activity có side effect (gửi mail, ghi Drive).
  2. Đặt trần retry và deadline theo nghiệp vụ; activity dài phải gọi heartbeat thật.
  3. Tạo operation ID ổn định làm idempotency key cho bước gửi; có bước đối soát khi timeout.
  4. Lưu history đại diện (thành công, lỗi, **chờ người duyệt**, hủy), che dữ liệu nhạy cảm, replay trong CI trước mỗi lần đổi workflow.
- **Phù hợp khi / Không nên khi:** Phù hợp khi có bước chờ người và side effect đối ngoại. Không nên khi tác vụ nhỏ, ngắn: job/queue + outbox (2.22) ít thành phần hơn.
- **Rủi ro & điều kiện:** SDK MIT; cần Temporal server và worker sống lâu. History chứa dữ liệu nghiệp vụ, cần quyền truy cập và retention. Chưa chạy SDK/replay.
- **Thay thế:** Restate TypeScript SDK (21 §10f); Celery + outbox (21); DBOS (21 §5).
- **Hồ sơ gốc:** [21 §10i.1](21-autonomous-workflows/README.md#temporal-replay-factory), [21 §10f](21-autonomous-workflows/README.md#temporal-python-sdk) · code-read · 2026-11-04

### 2.21 googleworkspace/cli (`gws`) — Một CLI cho Gmail, Drive, Sheets, Calendar, xuất JSON cho agent, có `--dry-run`

- **Giải quyết:** Gửi mail có đính kèm, lưu file lên Drive, ghi Google Sheets từ script/agent mà không tự viết client cho từng API.
- **Cơ chế cốt lõi:** Sinh lệnh động từ Google Discovery Service lúc chạy (tự nhận endpoint mới); có `--dry-run`, tự phân trang, xuất NDJSON; kèm thư mục skills cho agent (khoảng 95 mục; đây là nhóm skill `gws-*`); thông tin đăng nhập mã hóa AES-256-GCM với khóa trong keyring.
- **Áp dụng vào dự án khác:**
  1. Tạo dự án Google Cloud + OAuth, xin **scope tối thiểu** (ví dụ chỉ gửi mail, chỉ một thư mục Drive).
  2. Cài `npm install -g @googleworkspace/cli`, ghim phiên bản.
  3. Mọi lệnh có side effect chạy `--dry-run` trước; lưu output dry-run làm bằng chứng cho người duyệt.
  4. Chỉ chạy lệnh thật sau cổng duyệt (2.22); đọc lại kết quả (message ID) làm receipt.
  5. Chỉ chép các skill `gws-*` cần dùng vào dự án, không cài cả thư mục.
- **Phù hợp khi / Không nên khi:** Phù hợp cho đơn vị dùng Google Workspace. Không nên khi cần ổn định API lâu dài: README ghi **không phải sản phẩm Google hỗ trợ chính thức**, có thể thay đổi phá vỡ trước v1.0.
- **Rủi ro & điều kiện:** Apache-2.0. Dữ liệu đi tới Google API theo tài khoản; app OAuth chưa xác minh bị giới hạn khoảng 25 scope. Hồ sơ chỉ docs-read, nội dung từng skill `gws-*` **(chưa xác minh)**.
- **Thay thế:** listmonk (AGPL-3.0, email hàng loạt tự host), Novu (MIT + Enterprise, điều phối thông báo), Zero Email (MIT, client mail tự host).
- **Hồ sơ gốc:** [08 §6c.5.8](08-awesome-lists-learning/README.md#6c58-editor-terminal--dòng-lệnh) · docs-read · 2026-11-18

### 2.22 Outbox + cổng duyệt theo mức rủi ro (mục 21 §8) — Khuôn an toàn cho mọi hành động đối ngoại như gửi email

- **Giải quyết:** Agent/automation gửi nhầm, gửi trùng hoặc gửi khi chưa có người xác nhận.
- **Cơ chế cốt lõi:** Guardrail tối thiểu: cổng người duyệt theo mức rủi ro (hành động phá hủy/đối ngoại phải qua gate); side effect đối ngoại đi qua **outbox**: ghi intent trước khi gọi, lease + fencing token, `outcome_unknown` → đối soát bằng đọc lại thay vì retry mù, pause mặc định; "đã gửi" chỉ tính khi có receipt đọc lại. Kèm trần vòng lặp, ngân sách là hard stop, tối đa N lần sửa cùng lỗi. Ý outbox lấy từ ADR nội bộ của chủ kho (Sales-Hunter ADR-0010) **(chưa xác minh độc lập)**.
- **Áp dụng vào dự án khác:**
  1. Tạo bảng `outbox`: id, loại hành động, người nhận, file đính kèm (hash), trạng thái (`draft/approved/sent/outcome_unknown/failed`), người duyệt, thời điểm.
  2. Agent chỉ được ghi `draft`; chỉ người (qua UI/tin nhắn) chuyển sang `approved`.
  3. Worker gửi chỉ lấy bản `approved`, dùng id làm idempotency key, ghi receipt (message ID) rồi mới đánh `sent`.
  4. Timeout → `outcome_unknown` → đọc lại hộp thư đã gửi trước khi thử lại.
  5. Mặc định pause khi lỗi lặp; báo người phụ trách.
- **Phù hợp khi / Không nên khi:** Phù hợp cho mọi luồng gửi file ra ngoài đơn vị. Không cần đầy đủ cho thông báo nội bộ vô hại (vẫn nên dedupe).
- **Rủi ro & điều kiện:** Là mẫu thiết kế, không phụ thuộc license. Chi phí: thêm bảng trạng thái và UI duyệt. Phải tự kiểm bằng fault injection (21 §10f).
- **Thay thế:** 2.20 Temporal (chờ duyệt trong workflow bền); `side-effects-gate.sh` của n8n-agent-skills (chỉ nhắc, không chặn); `safe-outputs` của gh-aw (21 §4).
- **Hồ sơ gốc:** [21 §8](21-autonomous-workflows/README.md#8-kiểu-hỏng-và-guardrail) · khuyến nghị tổng hợp, chưa chạy · ngày hồ sơ không ghi riêng (mục 21, đợt 2026-10)

### 2.23 Label Studio — Hàng chờ để người duyệt kết quả máy trích, tách "dự đoán" khỏi "đã duyệt"

- **Giải quyết:** Trường trích từ hồ sơ khách hàng cần người kiểm, nhưng phải biết rõ giá trị nào là máy đoán, giá trị nào người đã xác nhận.
- **Cơ chế cốt lõi:** UI gán nhãn nhiều loại dữ liệu; `tasks/models.py` tách `Annotation` (có `completed_by`, `ground_truth`, trạng thái bỏ qua, thời gian) với `Prediction`. Settings mặc định: `COLLECT_ANALYTICS` bật, `DISABLE_SIGNUP_WITHOUT_LINK` false, SSRF protection true.
- **Áp dụng vào dự án khác:**
  1. Đưa kết quả trích (2.7/2.9) vào như `Prediction` kèm ảnh trang gốc và vùng bbox.
  2. Người duyệt sửa/xác nhận → `Annotation`; lưu người, thời điểm, phiên bản hướng dẫn.
  3. Tắt analytics, bật kiểm soát đăng ký, giới hạn truy cập mạng.
  4. Export kết quả đã duyệt có hash; dùng làm tập nhãn đo lại pipeline (2.10).
- **Phù hợp khi / Không nên khi:** Phù hợp khi khối lượng hồ sơ cần duyệt lớn, nhiều người duyệt. Không nên khi chỉ vài hồ sơ/ngày (một bảng tính duyệt đơn giản đủ).
- **Rủi ro & điều kiện:** Apache-2.0. Dữ liệu duyệt có PII; storage/ML backend/analytics tạo luồng dữ liệu riêng; phân quyền và telemetry đầy đủ **(chưa xác minh)**. Kiểm tính năng thuộc OSS hay bản thương mại.
- **Thay thế:** Argilla (feedback LLM), Cleanlab (xếp hạng mẫu cần xem lại) ở mục 24.
- **Hồ sơ gốc:** [24 · Label Studio](24-ai-data-engineering/README.md#label-studio), [24 §5](24-ai-data-engineering/README.md#5-cổng-kiểm-có-thể-đo-và-quy-trình-human-review) · code-read · 2026-11-02

### 2.24 SkillsBench — Khuôn task/oracle/verifier để đo skill văn phòng tự viết

- **Giải quyết:** Tự viết skill "điền báo cáo"/"trích hồ sơ" nhưng không biết nó đúng bao nhiêu và có hỏng khi đổi model.
- **Cơ chế cốt lõi:** Mỗi task: `task.md` + `environment/skills/` + `oracle/solve.sh` + `verifier/test.sh`/`test_outputs.py`; oracle phải pass trước khi chạy agent; verifier ghi `reward.txt` 1/0 từ mã thoát pytest, phụ thuộc test ghim phiên bản. CI kiểm cấu trúc task và frontmatter skill.
- **Áp dụng vào dự án khác:**
  1. Với mỗi skill, tạo 5–10 task: file Excel/PDF đầu vào + đầu ra kỳ vọng.
  2. Viết oracle (lời giải tất định) và chạy để chứng minh verifier đúng.
  3. Verifier so ô/trường cụ thể, không chỉ "file mở được".
  4. Chạy bộ task mỗi khi đổi skill, model hoặc prompt; lưu điểm theo phiên bản.
- **Phù hợp khi / Không nên khi:** Phù hợp khi skill được dùng định kỳ, có hậu quả sai. Không cần dùng nguyên framework BenchFlow; chỉ chép cấu trúc.
- **Rủi ro & điều kiện:** Apache-2.0. Chạy đầy đủ cần Docker/Modal và khóa model; skill mẫu trong benchmark là bản theo task, không phải skill chuẩn. Leaderboard **(chưa xác minh)**.
- **Thay thế:** skillgrade, agent-skills-eval, nvidia-skillevaluator (mục 20); eval build-task của 2.19.
- **Hồ sơ gốc:** [20 · SkillsBench](20-claude-plugins-ecosystem/README.md#xlsx-2026-11-23-skillsbench) · code-read · 2026-11-23

---

### Ghép thành quy trình: báo cáo tự động → kiểm duyệt → gửi mail

Quy trình dưới đây chỉ dùng các item đã có hồ sơ trong kho. **Chưa có bản nào được kho chạy thử**; đây là thiết kế tham khảo, cần dựng và kiểm ở repo dự án.

```
[Excel tổng] → (1) Đọc & chuẩn hóa ─→ (2) Cổng dữ liệu ─fail→ báo lỗi, DỪNG
                                          │ pass
                                          ▼
                     (3) Điền mẫu / dàn trang → (4) Cổng văn bản & tự kiểm
                                          │
                                          ▼
                     (5) Ghi OUTBOX trạng thái draft + gói bằng chứng
                                          │
                       ╔══════════════════▼══════════════════╗
                       ║ (6) CỔNG NGƯỜI XÁC NHẬN (bắt buộc)  ║
                       ║  approve / reject / sửa             ║
                       ╚══════════════════╤══════════════════╝
                                          │ approved
                                          ▼
                     (7) Gửi bền, idempotent → (8) Đọc lại receipt → sent
```

1. **Đọc và chuẩn hóa** (2.13 pandas; 2.3 SheetJS nếu stack JS): đọc Excel tổng với dtype, null, ngày/tiền và NFC khai báo rõ; lưu hash file nguồn.
2. **Cổng dữ liệu** (2.14 Great Expectations): expectation cho cột bắt buộc, khóa, khoảng giá trị. Fail thì dừng, báo người phụ trách dữ liệu, không sinh báo cáo.
3. **Điền mẫu / dàn trang**: file Office sửa được dùng skill theo khuôn 2.1 (tham khảo) hoặc 2.2 (MIT, cổng XSD cho docx); PDF chỉ đọc dùng 2.4 Typst với template ghim. Định dạng HTML/email theo khuôn template + lint của 2.6.
4. **Cổng văn bản và tự kiểm**: chạy cổng NFC/kiểu dấu tiếng Việt (2.15, tự viết lại nếu vướng license); chạy bộ task 2.24 khi skill hoặc model vừa đổi. Lỗi thì quay lại bước 3, tối đa N lần rồi chuyển BLOCKED (21 §8 ý 7).
5. **Ghi outbox** (2.22): agent chỉ được tạo bản ghi `draft` gồm người nhận, tiêu đề, thân thư, hash file đính kèm, kết quả cổng 2–4 và output `gws ... --dry-run` (2.21). Agent **không có quyền** chuyển trạng thái.
6. **Cổng người xác nhận (bắt buộc, không tự động bỏ qua)**: người phụ trách xem gói bằng chứng (bản nháp, file đính kèm, dry-run, kết quả kiểm) rồi chọn approve/reject/sửa. Có thể báo "có bản chờ duyệt" qua ntfy hoặc Novu (21, docs-read). Nếu chạy trong 2.20 Temporal thì đây là trạng thái "chờ người duyệt" của workflow; nếu dùng n8n (2.19) thì bước duyệt phải là thao tác của người, không phải node tự động. Không có approve thì quy trình dừng ở `draft`, quá hạn thì hủy.
7. **Gửi bền, idempotent**: worker (activity Temporal 2.20, hoặc job + outbox) chỉ lấy bản `approved`, gọi `gws` gửi Gmail với id outbox làm idempotency key; retry có trần và deadline.
8. **Đọc lại và đối soát**: chỉ đánh `sent` khi đọc lại được message ID trong hộp thư đã gửi; timeout thì `outcome_unknown` → đối soát trước khi thử lại, không retry mù (21 §8 ý 8, §10f).

**Biến thể trích hồ sơ khách hàng:** thay bước 1–2 bằng 2.7 Docling / 2.8 OCRmyPDF / 2.9 PaddleOCR → schema và cổng 6 bước (2.10) → hàng chờ duyệt 2.23; chỉ trường đã duyệt mới đi tiếp vào bước 3.

**Điều phải tự kiểm trước khi đưa vào thật (chưa ai trong kho chạy):** gửi trùng khi worker chết sau lúc Gmail đã nhận; người duyệt reject thì không có thư nào đi; file đính kèm bị đổi sau khi duyệt (so hash) thì phải chặn; OAuth scope chỉ đủ cho gửi mail/thư mục cần thiết; telemetry của dlt, n8n-mcp, Label Studio, GX đã tắt.

## 3. Thiết kế, giao diện, motion & media

> Chương chắt lọc từ mục 06, 14, 19, 22 và phần skill thiết kế/media ở mục 20 của kho `stored`, cùng `data/projects.json`. Chọn theo **cơ chế dùng lại được và bằng chứng trong hồ sơ**, không theo số sao. Mức bằng chứng ghi theo `verification_level` của catalog; nếu catalog chưa gắn mức, ghi ngày và việc đã làm theo chính hồ sơ. Không có mục nào ở đây được kho cài đặt và benchmark lại trên dự án thật; ngưỡng, giá và hiệu năng của upstream phải kiểm lại trước khi tích hợp (METHOD.md §2, §5). Đường dẫn tính từ gốc repo `stored`.
>
> Bài học xuyên suốt các hồ sơ: **"gu" chỉ bền khi có cổng máy đi kèm** (06 §4, §7t). Nên dựng cổng máy trước (lint, a11y, so ảnh, loudness), rồi mới thêm skill gu.

### Nhu cầu → item nên dùng

| Nhu cầu | Item nên dùng (thứ tự gợi ý) |
|---|---|
| Agent sinh UI mới mà không ra "mùi AI" | 3.1 frontend-design → 3.2 Taste Skill (có inspector) → 3.4 unslop để sửa màn cũ |
| Chặn "AI slop" và lệch token bằng máy trong CI | 3.3 Impeccable detector + 3.8 `@shadcn/lint`/stylelint + 3.10 axe-core |
| Có một nguồn token cho web, mobile, Figma và agent | 3.6 DESIGN.md (spec Google) → 3.7 DTCG + Style Dictionary → 3.13 đồng bộ Figma |
| Thư viện component dùng chung giữa nhiều sản phẩm | 3.8 shadcn/ui làm nền → 3.9 Storybook addon-vitest làm hợp đồng → 3.11 so ảnh |
| Giao diện tiếng Việt và đa ngôn ngữ không vỡ | 3.12 Lingui/i18next + pseudo-locale → 3.11 so ảnh theo locale |
| Motion UI có nguyên tắc, không hại a11y/hiệu năng | 3.14 LottieFiles motion skill + GSAP skills → 3.15 cổng reduced-motion, web-vitals, kiểm theo mốc thời gian |
| Video sản phẩm, explainer làm bằng code | 3.16 HyperFrames (Apache-2.0) hoặc 3.17 Remotion (xem license) → 3.20 lemo-opuscar cho phong cách/cổng đọc chữ |
| Cắt, ghép, chuyển mã footage bằng agent | 3.18 ffmpeg-skill (kajisho5) → 3.19 dựng theo transcript (herk-edit-kit, video-use) → 3.21 OTIO/PySceneDetect |
| Phát hành video thương mại an toàn | 3.22 loudness R128 + VMAF + C2PA + manifest quyền asset |
| Phụ đề, chép lời, voice agent, giọng đọc | 3.23 faster-whisper/WhisperX → 3.24 Pipecat/LiveKit + Silero VAD → 3.25 TTS có license rõ + đo WER/MOS |

---

### 3.1 frontend-design (Anthropic) — prompt ngắn, chính chủ, buộc agent lập brief và né 5 cụm "dấu hiệu AI"

- **Giải quyết:** UI do agent sinh mặc định giống nhau (nền kem + serif + accent đất nung, gradient trang trí, bộ card SaaS, eyebrow viết hoa, mũi tên "→").
- **Cơ chế cốt lõi:** `SKILL.md` 71 dòng, giống hệt nhau ở ba repo của Anthropic. Vai "design lead", buộc xác định chủ đề, người dùng, việc chính trước khi thiết kế. Quy trình hai lượt: lên plan token (4–6 hex, font, wireframe ASCII), tự so plan với "bản mặc định" rồi sửa trước khi code. Liệt kê cụ thể 5 cụm dấu hiệu AI và có phần viết nội dung UI (CTA rõ hành động, sentence case). Skill do model tự gọi theo mô tả, không phải lệnh `/`. Không có cổng máy; chỉ dặn tự chụp màn hình để phê bình.
- **Áp dụng vào dự án khác:**
  1. Cài qua `/plugin marketplace add anthropics/claude-code` rồi `/plugin install frontend-design@claude-code-plugins`, hoặc chép từ `anthropics/skills`.
  2. Ghi rõ ràng buộc brand trong prompt; skill ghi "lời của brief luôn thắng".
  3. Bật cho landing, prototype, trang mới; tắt hoặc để design system thắng ở app nghiệp vụ đã có hệ thiết kế.
  4. Ghép một cổng máy (3.3 hoặc 3.10) vì skill không tự đo.
  5. Ghim bản SKILL.md vào repo vì nội dung đổi theo thời gian (đã viết lại 6/2026 và 9/2026, có lời khuyên bị đảo ngược).
- **Phù hợp khi / Không nên khi:** Phù hợp khi cần hướng thẩm mỹ nhanh, ít token. Không nên khi sản phẩm đã có design system chặt hoặc cần bằng chứng đo được.
- **Rủi ro & điều kiện:** Code/prompt Apache-2.0 (`LICENSE.txt` của `anthropics/skills`). Không gửi dữ liệu ra ngoài ngoài model đang dùng. Không có benchmark; con số "1,1 triệu lượt cài" **(chưa xác minh)**. Nội dung skill trôi theo upstream.
- **Thay thế:** Taste Skill (3.2), Refactoring UI Skill (3.5), Hallmark (06 §7l).
- **Hồ sơ gốc:** [06 §7g.3](06-ui-ux-design/README.md#7g3-frontend-design-anthropic-prompt-ngắn-chính-chủ-thay-đổi-theo-thời-gian) · catalog chưa gắn mức (hồ sơ đọc 3 bản SKILL.md và git log) · 18/10/2026

### 3.2 Taste Skill (`Leonxlnx/taste-skill`) — skill chống slop có "chia bài" hướng thiết kế và inspector chạy trên Chrome thật

- **Giải quyết:** Agent chọn mặc định thay vì chọn hướng; skill chỉ là lời dặn mà không nhìn bản render.
- **Cơ chế cốt lõi:** `scripts/draw.mjs` rút 3 trong 20 hướng thiết kế theo `--sector`/`--idea`, rồi rút type, palette, hero, section từ thư viện JSON (20 directions, 58 heroes, 185 sections, 56 palettes, 44 type, 202 sites) để in "direction sheet". `scripts/inspect.mjs` + `lib/cdp.mjs` điều khiển Chrome/Edge qua CDP (không cần Playwright), mở trang ở 1440/768/390px, đo số dòng tiêu đề, cỡ chữ, font thật, ghi `FAIL`/`WARN` và lưu screenshot cho vòng look-and-fix. `lint.mjs` là phương án tĩnh khi không có Chrome.
- **Áp dụng vào dự án khác:**
  1. Lấy bản `skills/taste-skill` ổn định, bỏ các biến thể `*-experimental`.
  2. Chạy `node scripts/draw.mjs --sector <ngành> --idea "<ý tưởng>"` để chốt hướng trước khi code.
  3. Cài Node 22+ và có Chrome/Edge; chạy `inspect.mjs` trên dev server sau mỗi vòng sửa.
  4. Nếu đã dùng frontend-design (3.1), chỉ mượn `inspect.mjs` + house rules để tránh nạp hai bộ luật lớn.
  5. Lưu `.taste-skill/inspect/` làm bằng chứng PR, không commit ảnh lớn vào repo.
- **Phù hợp khi / Không nên khi:** Phù hợp khi cần cổng đo trên bản render mà không muốn cài Playwright. Không nên khi ngân sách ngữ cảnh hẹp (skill chính 529 dòng + 11 reference + thư viện JSON).
- **Rủi ro & điều kiện:** Code MIT. Inspector chạy cục bộ; không thấy ghi chép gửi dữ liệu trong hồ sơ. Có hệ sinh thái thương mại (TasteCode, website, tài trợ) cần tách khỏi phần OSS. Một phần commit do agent viết; sao tăng mạnh. Inspector chưa được chạy end-to-end trong hồ sơ.
- **Thay thế:** Impeccable (3.3), XIAS (06 §7d), frontend-design (3.1).
- **Hồ sơ gốc:** [06 §7j](06-ui-ux-design/README.md#7j-hồ-sơ-leonxlnxtaste-skill-taste-skill--skill-chống-ai-slop-có-inspector-chạy-trên-trình-duyệt-thật-bổ-sung-hồ-sơ-clone-2026-10-19) · catalog chưa gắn mức (hồ sơ clone đủ, tự chạy `tests/skill_test.sh`, `draw.mjs`, `lint.mjs`; inspector chưa chạy) · 19/10/2026

### 3.3 Impeccable (`pbakaus/impeccable`) — từ vựng thiết kế cho agent cộng detector tất định chạy được ở hook và CI

- **Giải quyết:** Cần một cổng máy bắt "AI slop" chạy được cả ngoài agent, có exit code cho CI.
- **Cơ chế cốt lõi:** 1 skill `/impeccable` + 23 lệnh (`init` → `PRODUCT.md`, `document` → `DESIGN.md`, steer `bolder`/`quieter`/`typeset`…, review `critique`/`audit`/`polish`, `live` overlay ghi về source). Engine Rust 16 crate, 62 rule tất định; rule cần bản render (tương phản, chữ nhỏ) chạy khi quét URL bằng Chrome/Edge. Chạy ở ba chỗ: hook trong agent, CLI `npx impeccable detect src/ --json|--github` (exit 2 khi có lỗi), Chrome extension. Từ 26/10/2026 launcher kiểm engine tải về với manifest checksum trong repo.
- **Áp dụng vào dự án khác:**
  1. Thêm `npx impeccable detect src/ --github` vào CI, kể cả khi không dùng skill.
  2. Ghim phiên bản skill/CLI và engine (hồ sơ ghi `skill-v4.8.0`/`engine-v0.1.18`), kiểm checksum binary.
  3. Đặt `DO_NOT_TRACK=1` hoặc `npx impeccable telemetry off`; thêm `.impeccable/` vào `.gitignore`.
  4. Chỉ bật hook sau khi chấp nhận việc tải engine; chạy không giám sát thì cân nhắc tắt hook.
  5. Tắt rule có chủ đích bằng comment `impeccable-disable`, ghi lý do trong PR.
  6. Không bật `live` trên site đã deploy; đọc script `impeccable:manual-edit-validate` trong `package.json` trước khi dùng live.
- **Phù hợp khi / Không nên khi:** Phù hợp khi dự án đã có frontend và muốn cổng tự động lớn nhất trong nhóm. Không nên khi môi trường cấm tải binary hoặc cấm gọi dịch vụ ngoài.
- **Rủi ro & điều kiện:** Apache-2.0 (+ `NOTICE.md`). **Dữ liệu rời máy:** khi bắt đầu thiết kế mới, skill luôn gọi catalog impeccable.style; tắt telemetry không chặn request này (README nói không gửi tên dự án, file, code). README tự nói "hooks run outside model approval". Repo 4.441 file do nhân bản cho 20 host.
- **Thay thế:** Taste Skill (3.2), XIAS (06 §7d), `@shadcn/lint` (3.8).
- **Hồ sơ gốc:** [20 §3n.1](20-claude-plugins-ecosystem/README.md#3n1-pbakausimpeccable--skill-thiết-kế--detector-tất-định-chạy-ở-hook) · [19 §3h](19-agentic-video-media/README.md#3h-kiểm-ảnh-ai-video-stack-remotion-skills-blender-và-blender-mcp-faster-whisper-chatterbox-gsap-ảnh-người-dùng-gửi-đọc-mã-8112026) · `docs-read` · 08/11/2026 (đọc mã hook/checksum 31/10/2026, không chạy engine)

### 3.4 unslop (`heydamir/unslop`) — sửa UI "vibecoded" theo 9 lượt có thứ tự, kiểm trước sửa sau

- **Giải quyết:** Màn hình đã làm bằng AI cần nâng chất mà không thiết kế lại từ đầu.
- **Cơ chế cốt lõi:** `SKILL.md` 233 dòng + 5 tham chiếu (`signs.md`, `tokens.md`, `effects.md`, `visuals.md`, `refs.md`). Liệt kê từng dấu hiệu slop kèm vị trí, đề xuất hướng trước khi sửa để người dùng lái sớm; màn đã tốt chỉ gợi ý chỉnh nhỏ. Chín lượt: spacing, màu, icon, copy, chữ, layout, chi tiết, hình ảnh, motion; cuối có "Do not" và checklist. `snapshot.mjs` chụp trang đang chạy, `story.mjs` dựng video vuông dưới 10 giây trước/sau (Playwright + ffmpeg).
- **Áp dụng vào dự án khác:**
  1. Chép `skills/unslop` vào `.claude/skills/` (Codex: `~/.agents/skills/`).
  2. Thử trước trên hai màn mẫu trong `examples/`.
  3. Gọi `/unslop this dashboard`, duyệt danh sách dấu hiệu và hướng đề xuất trước khi cho sửa.
  4. Cài `playwright` + Chromium và ffmpeg nếu cần ảnh/video trước-sau cho PR.
  5. Chạy lại cổng máy (3.10, 3.11) sau khi sửa vì skill không tự đo a11y.
- **Phù hợp khi / Không nên khi:** Phù hợp cho màn cũ cần "unslop" có kiểm soát. Không nên khi cần cổng chặn tự động trong CI.
- **Rủi ro & điều kiện:** **CC BY 4.0** (không phải license phần mềm thường gặp): dùng thương mại được nhưng phải ghi công tác giả và link repo. Lượt hình ảnh có thể gọi fal, Replicate, OpenAI images, Higgsfield, tức gửi prompt/ảnh ra ngoài nếu bật. Repo mới (tạo 29/10/2026), 12 commit.
- **Thay thế:** antislop (06 §7i), Taste Skill (3.2), Hallmark (06 §7l).
- **Hồ sơ gốc:** [06 §7zb](06-ui-ux-design/README.md#7zb-đọc-lại-heydamirunslop-skill-biến-ui-vibecoded-thành-giao-diện-có-chủ-đích-114k-sau-10-ngày-ảnh-người-dùng-gửi-đọc-mã-8112026) · `code-read` · 08/11/2026

### 3.5 Refactoring UI Skill (`s0xDk/refactoring-ui-skill`) — thang giá trị kiểm được và `tokens.css` đã đúng tương phản

- **Giải quyết:** Thiếu lớp "hệ thống" (spacing, type, màu, bóng) bên dưới skill gu; khó sửa UI cũ có lý do.
- **Cơ chế cốt lõi:** `SKILL.md` 267 dòng với thang spacing/type/weight/màu HSL, 5 mức bóng, 9 hard rule; `references/diagnose.md` là bảng triệu chứng → cách sửa; `assets/tokens.css` có ramp xám/primary 9 mức, 3 bộ accent, lớp semantic và khối dark mode. Hồ sơ tính lại tương phản WCAG cả light và dark, khớp chú thích trong file (ví dụ chữ trắng trên `primary-500` khoảng 5,8:1).
- **Áp dụng vào dự án khác:**
  1. Chép `tokens.css` làm điểm khởi đầu, đổi hue theo brand.
  2. Chạy lại phép tính tương phản sau khi đổi hue (dùng tỉ lệ WCAG 2, không dùng APCA).
  3. Dùng `diagnose.md` làm checklist khi review UI cũ.
  4. Đặt skill này làm lớp thang giá trị, để 3.1 hoặc 3.2 quyết định cá tính.
- **Phù hợp khi / Không nên khi:** Phù hợp cho web/CSS chưa có token. Không nên dùng như nguồn cho mobile native (hồ sơ ghi chưa nói tới).
- **Rủi ro & điều kiện:** MIT. Chỉ 2 commit, một tác giả, chưa có lịch sử bảo trì. README nói không chứa chữ/hình của sách *Refactoring UI*. Có repo trùng tên khác không có LICENSE (`lovropodobnik/…`); chọn đúng bản `s0xDk`.
- **Thay thế:** Radix Colors / Harmony / Capsize (06 §7t), `ui-ux-pro-max-skill` (06 §7g.2).
- **Hồ sơ gốc:** [06 §7g.4](06-ui-ux-design/README.md#7g4-refactoring-ui-skill-hai-repo-trùng-tên-chọn-bản-s0xdk) · catalog chưa gắn mức (hồ sơ clone đủ, tính lại tương phản light/dark) · 18–19/10/2026

### 3.6 DESIGN.md theo spec Google + trích bằng dembrandt — một file hệ thiết kế agent đọc được và lint được

- **Giải quyết:** Agent không biết hệ thiết kế của sản phẩm; file mô tả viết tay không kiểm được bằng máy.
- **Cơ chế cốt lõi:** Spec `google-labs-code/design.md` (alpha, bản 0.4.0): YAML front matter chứa token + phần văn xuôi giải thích, kèm CLI `lint`/`diff`/`export`. Hồ sơ chạy linter trên 11 DESIGN.md "chính chủ": chỉ 6/11 có token máy đọc được, 1/11 (Vercel) sạch hoàn toàn; linter bắt được tham chiếu gãy và tương phản dưới AA. dembrandt mở URL bằng Playwright, xuất token và DESIGN.md theo spec Google 0.4, có test chạy linter thật, đọc robots.txt, và Action "Drift Gate" chặn lệch token trong CI.
- **Áp dụng vào dự án khác:**
  1. Viết DESIGN.md cho brand của mình theo spec Google (YAML token + văn xuôi), đặt ở gốc repo.
  2. Thêm `npx @google/design.md@<phiên bản ghim> lint DESIGN.md` vào CI.
  3. Nếu đã có site, chạy dembrandt trên **site của mình** để có bản nháp token, rồi sửa tay.
  4. Khai token `on-primary` rõ ràng để tránh lỗi chữ trắng trên primary sáng.
  5. Bật Drift Gate (hoặc `lint`/`diff`) để chặn lệch giữa DESIGN.md và code.
- **Phù hợp khi / Không nên khi:** Phù hợp khi nhiều agent/công cụ cần cùng một mô tả hệ thiết kế. Không nên chép DESIGN.md của thương hiệu khác vào sản phẩm (logo, màu, font có quyền riêng).
- **Rủi ro & điều kiện:** Spec Apache-2.0, trạng thái alpha nên định dạng có thể đổi. dembrandt MIT; `--key`/`--compare` gửi dữ liệu lên dembrandt.com, còn lại chạy offline; có cờ `--stealth` giả vân tay trình duyệt, chỉ chạy trên site được phép. Kho `awesome-design-md` là bản trích xuất, README tự ghi không sở hữu.
- **Thay thế:** designlang/design-extract (06 §7p.4, không theo spec Google), `bergside/awesome-design-skills` (06 §7g.5), DTCG (3.7).
- **Hồ sơ gốc:** [06 §7c](06-ui-ux-design/README.md#7c-kiểm-ảnh-voltagentofficial-design-md-danh-mục-designmd-chính-chủ-ảnh-người-dùng-gửi-2026-10-13) · [06 §7p.4](06-ui-ux-design/README.md#7p4-figma-trích-design-system-từ-web-công-cụ-vẽ) · catalog chưa gắn mức (hồ sơ §7c tự chạy linter 0.4.0 trên 11 file; dembrandt đọc mã) · 13/10/2026 và 31/10/2026

### 3.7 DTCG 2025.10 + Style Dictionary — một nguồn token, kiểm bằng JSON Schema, build ra mọi nền tảng

- **Giải quyết:** Token rải ở nhiều `tokens.css`, theme Tailwind, Figma variables; không có định dạng chung để kiểm tự động.
- **Cơ chế cốt lõi:** DTCG có Format, Color và Resolver Module bản 2025.10, kèm JSON Schema (`schemas/src/2025.10/`) và test-suite gồm cả ca hợp lệ lẫn ca phải bị từ chối. Style Dictionary build một nguồn token ra CSS, iOS, Android, JS; bản 5.7 hỗ trợ DTCG (`usesDtcg`, kiểu `duration` 2025.10), 5.7.1 vá lỗi prototype pollution. Hồ sơ mục 22 đề xuất dùng cùng đường này cho token motion (duration, cubicBezier, transition).
- **Áp dụng vào dự án khác:**
  1. Viết `tokens.json` theo Format 2025.10; tách primitive và semantic.
  2. Kiểm `tokens.json` bằng JSON Schema của DTCG trong CI.
  3. Build bằng Style Dictionary (Node ≥ 22) ra biến CSS và theme Tailwind; ghim bản ≥ 5.7.1.
  4. Lấy màu từ Radix Colors hoặc Harmony, căn chữ bằng Capsize (06 §7t).
  5. Thêm token motion (3.15) vào cùng nguồn để GSAP/Motion/CSS không dùng số viết tay.
- **Phù hợp khi / Không nên khi:** Phù hợp khi có từ hai nền tảng hoặc có Figma cần đồng bộ. Không nên khi chỉ là một landing tĩnh; một file CSS biến là đủ.
- **Rủi ro & điều kiện:** DTCG dưới W3C Software and Document License, là báo cáo Community Group, **không phải W3C Recommendation** (mã spec vẫn ghi `CG-DRAFT`). Style Dictionary Apache-2.0; hỗ trợ Resolver Module 2025.10 **(chưa xác minh)**. Không nhúng mã APCA (license hạn chế, 06 §7t).
- **Thay thế:** DESIGN.md YAML (3.6), `tokens.css` của Refactoring UI (3.5), Penpot design token gốc (06 §7zg).
- **Hồ sơ gốc:** [06 §7t](06-ui-ux-design/README.md#7t-nâng-trần-2112026-nền-móng-tokenmàuchữ-và-cổng-máy-cho-frontend-a11y-visual-regression-hiệu-năng-lint-css-yêu-cầu-người-dùng) · catalog chưa gắn mức (hồ sơ clone, đọc README/LICENSE/schema/CHANGELOG, không chạy) · 02/11/2026

### 3.8 shadcn/ui + `@shadcn/lint` + stylelint — mã component nằm trong repo, "gu" thành lỗi lint có cách sửa

- **Giải quyết:** Agent hay restyle component, dùng màu thô và giá trị tùy ý; lời dặn "dùng token" không bền.
- **Cơ chế cốt lõi:** shadcn/ui là copy-paste source qua CLI trên Tailwind, từ 7/2026 cài mới dùng Base UI (vẫn hỗ trợ Radix), có MCP chính thức trong CLI, skill và `llms.txt`. `@shadcn/lint` có đúng 6 luật (`no-restyle`, `no-raw-colors`, `no-arbitrary-values`, `no-inline-styles`, `no-unknown-classes`, `require-static-classes`), mỗi luật một trang docs; không telemetry. stylelint phủ CSS thuần với `color-no-hex`, `declaration-property-value-allowed-list`, `no-unknown-custom-properties`.
- **Áp dụng vào dự án khác:**
  1. Khởi tạo shadcn/ui, khóa primitive (Base UI hoặc Radix) cho toàn dự án.
  2. Bật `@shadcn/lint` cho JSX/Tailwind và stylelint cho CSS trong pre-commit và CI.
  3. Đưa thông báo lỗi lint vào vòng sửa của agent thay cho đoạn luật dài trong `CLAUDE.md`.
  4. Ghim stylelint bản stable (nhánh chính đang `18.0.0-next.0`).
  5. Version các component đã chỉnh như một package nội bộ khi dùng cho nhiều sản phẩm (3.9).
- **Phù hợp khi / Không nên khi:** Phù hợp cho React + Tailwind. Không nên khi dự án Vue/Angular (xem shadcn-vue, ng-zorro ở 06 §7r.3); Oxlint chỉ đọc khối script trong `.vue`/`.svelte`.
- **Rủi ro & điều kiện:** Tất cả MIT. Mã component copy vào repo nên tự bảo trì bản vá. Eval "mọi model về 0 lỗi" của `@shadcn/lint` không tái lập được (kết quả bị gitignore).
- **Thay thế:** Animate UI (06 §7zf), React Aria (06 §7f.3), Impeccable (3.3).
- **Hồ sơ gốc:** [06 §7p.3](06-ui-ux-design/README.md#7p3-design-system-và-lint-sẵn-cho-agent) · [06 §7t](06-ui-ux-design/README.md#7t-nâng-trần-2112026-nền-móng-tokenmàuchữ-và-cổng-máy-cho-frontend-a11y-visual-regression-hiệu-năng-lint-css-yêu-cầu-người-dùng) · catalog chưa gắn mức (đọc mã lint 31/10/2026; stylelint đọc `lib/rules/` 02/11/2026) · 31/10–02/11/2026

### 3.9 Storybook `@storybook/addon-vitest` — story là ca kiểm thử trình duyệt, component là hợp đồng

- **Giải quyết:** Ảnh đẹp không chứng minh modal giữ focus, form xử lý lỗi server hay nút đang tải không gửi hai lần.
- **Cơ chế cốt lõi:** Plugin biến story thành test qua `vitestTransform`, nạp setup-file và project annotations. Đường a11y ở preview có ba chế độ: **todo** (warning, mặc định của addon-a11y), **error** (failed), **off**; chỉ khi có violation và mode failed thì test thất bại. `storybookjs/test-runner` đã kết thúc hỗ trợ chính thức.
- **Áp dụng vào dự án khác:**
  1. Viết story cho loading, empty, error, disabled, permission-denied cùng trạng thái thành công, dùng dữ liệu giả đã khử PII.
  2. Cài addon-vitest bản **stable** tương thích Storybook/Vite/Vitest (hồ sơ đọc nhánh next 11.0.0-beta.0, không khuyên cài beta).
  3. Đặt `a11y.test` thành `error` cho phạm vi cần chặn; thêm một fixture cố ý lỗi để chứng minh pipeline từ chối.
  4. Báo tổng số story hợp lệ/đã chạy/skipped; bộ lọc rỗng không được tính là pass.
  5. Chuyển khỏi test-runner cũ; hệ không phải Vite thì thử Playwright/portable stories và so coverage trước.
- **Phù hợp khi / Không nên khi:** Phù hợp cho thư viện component dùng nhiều sản phẩm, dự án Vite. Không thay E2E xuyên backend (dùng Playwright, mục 11/30).
- **Rủi ro & điều kiện:** MIT. Phụ thuộc chuỗi phiên bản Storybook/Vite/Vitest/browser provider; kiểm migration guide khi nâng.
- **Thay thế:** Playwright component/E2E (mục 30), axe-core trực tiếp (3.10), test-runner cũ chỉ cho hệ đang chạy.
- **Hồ sơ gốc:** [06 §7y.2](06-ui-ux-design/README.md#storybook-addon-vitest-factory) · [06 §7y](06-ui-ux-design/README.md#ui-factory-2026-11-04) · `code-read` · 04/11/2026

### 3.10 axe-core + eslint-plugin-jsx-a11y + script cổng của XIAS — cổng a11y tĩnh và động

- **Giải quyết:** Lỗi tương phản, vùng chạm, focus lặp lại ở UI agent sinh (ví dụ Ant Design 4,10:1; số "65" 2,92:1 trong XIAS).
- **Cơ chế cốt lõi:** axe-core: 105 luật WCAG 2.0/2.1/2.2 A–AAA và best practice; README tự nói chỉ bắt trung bình **57%** lỗi WCAG; ca không chắc trả `incomplete` cho người kiểm. jsx-a11y: 39 luật bắt lỗi ngay trong JSX trước khi render. XIAS (`plugin87/ux-ui-agent-skills`) có script chạy độc lập trên HTML: `verify_states.mjs` (tương phản theo hover/focus/disabled), `verify_target_size.mjs`, `verify_overflow.mjs` (280px), `axe_audit.mjs`, `lint_intent.mjs` (nút xóa không mang màu primary), và hook `Stop` buộc agent nói "UNMEASURED" khi chưa đo.
- **Áp dụng vào dự án khác:**
  1. Bật jsx-a11y trong ESLint (lưu ý peerDeps chỉ tới ESLint ^9).
  2. Chạy `@axe-core/playwright` (gói Deque, hồ sơ **chưa đọc mã**) trên mỗi route và trạng thái chính; chặn PR khi có `serious`/`critical`.
  3. Đưa `incomplete` cho người review; ghi phần kiểm thủ công (keyboard, screen reader).
  4. Mượn các script trạng thái/vùng chạm/280px của XIAS cho phần axe không đo; cài Chrome vì script gọi `channel: 'chrome'`.
  5. Không nạp nguyên `CLAUDE.md` 319 dòng của XIAS nếu dự án đã có luật riêng; lấy từng phần bằng `npx ux-ui-agent-skills add`.
- **Phù hợp khi / Không nên khi:** Phù hợp cho mọi UI web. Không nên coi axe pass là chứng nhận WCAG đầy đủ.
- **Rủi ro & điều kiện:** axe-core **MPL-2.0** (copyleft theo file: sửa file của axe thì phải công bố phần sửa). jsx-a11y MIT, commit cuối 3/1/2026, PR hỗ trợ ESLint 10 chưa merge. XIAS MIT nhưng thư viện 138 design system phần lớn chép từ hai kho MIT khác **không ghi công**; hồ sơ tự chạy được 49/52 cổng, không phải 52/52 như README.
- **Thay thế:** Storybook a11y mode error (3.9), `web-quality-skills` (06 §7t), Impeccable `audit` (3.3).
- **Hồ sơ gốc:** [06 §7t](06-ui-ux-design/README.md#7t-nâng-trần-2112026-nền-móng-tokenmàuchữ-và-cổng-máy-cho-frontend-a11y-visual-regression-hiệu-năng-lint-css-yêu-cầu-người-dùng) · [06 §7d](06-ui-ux-design/README.md#7d-kiểm-ảnh-plugin87ux-ui-agent-skills-xias-bộ-skill-biến-claude-thành-senior-design-architect-ảnh--tên-repo-người-dùng-gửi-2026-10-13) · catalog chưa gắn mức (axe/jsx-a11y đọc mã 02/11/2026; XIAS tự chạy `npm test`, `accuracy_report.mjs` 13/10/2026) · 13/10–02/11/2026

### 3.11 pixelmatch hoặc Argos — visual regression có baseline được duyệt

- **Giải quyết:** Không có cách biết commit mới làm lệch giao diện ở khổ nào, locale nào.
- **Cơ chế cốt lõi:** pixelmatch khoảng 600 dòng, không phụ thuộc, tính sai khác màu bằng OKLab và HyAB, nhận ra pixel khử răng cưa (v8.0.0). Argos là nền tảng review ảnh chụp trong PR (Playwright, Storybook, Cypress), so bằng `odiff-bin`.
- **Áp dụng vào dự án khác:**
  1. Chụp Storybook hoặc trang mẫu ở 375, 768, 1440 và 280px, cho từng locale chính.
  2. Ổn định ảnh: font tải xong, tắt hoặc seek animation (3.15), dữ liệu giả cố định.
  3. Tự host bằng pixelmatch với tolerance có lý do; hoặc dùng Argos SaaS nếu cần giao diện duyệt.
  4. Baseline chỉ cập nhật khi có người duyệt, không tự ghi đè trong lượt sửa lỗi.
  5. Ghi số ảnh được so; cổng chạy 0 ảnh phải đỏ.
- **Phù hợp khi / Không nên khi:** Phù hợp cho design system và trang marketing ổn định. Không nên dùng để chấm đúng/sai nghiệp vụ hay ý nghĩa nút.
- **Rủi ro & điều kiện:** pixelmatch ISC, Argos MIT. Argos tự host cần Postgres, RabbitMQ, Redis, DynamoDB, S3, GitHub App; bản tự host chạy được **(chưa xác minh)**; dùng SaaS nghĩa là ảnh chụp UI rời máy. Lost Pixel đã archive.
- **Thay thế:** BackstopJS, reg-suit (06 §7t, tự host), Storybook addon-vitest kết hợp chụp ảnh (3.9).
- **Hồ sơ gốc:** [06 §7t](06-ui-ux-design/README.md#7t-nâng-trần-2112026-nền-móng-tokenmàuchữ-và-cổng-máy-cho-frontend-a11y-visual-regression-hiệu-năng-lint-css-yêu-cầu-người-dùng) · catalog chưa gắn mức (đọc LICENSE/README/index.js, docker-compose của Argos) · 02/11/2026

### 3.12 Lingui hoặc i18next + pseudo-locale — vòng extract → dịch → review → compile → render theo locale

- **Giải quyết:** UI qua axe và so ảnh bằng tiếng Anh vẫn có thể mất dấu tiếng Việt, cắt nút khi chuỗi dài, sai plural, sai tiền.
- **Cơ chế cốt lõi:** i18next: runtime đa framework, `PluralResolver.js` dùng `Intl.PluralRules`, `interpolation.escapeValue: true` mặc định. Lingui: macro biến JS/JSX thành ICU MessageFormat, catalog rồi compile; `pseudoLocale` kéo dài chữ và giả RTL. Điểm bẫy đã đọc mã: **`lingui compile --strict` kiểm thiếu sau khi áp `fallbackLocales`**, nên xanh vẫn có thể là câu tiếng Anh thay cho tiếng Việt. Weblate là lớp cộng tác dịch (GPL-3.0-or-later), review mặc định không bật.
- **Áp dụng vào dự án khác:**
  1. Chọn một runtime: i18next nếu đã có JSON catalog/nhiều framework; Lingui nếu muốn macro + ICU + compile.
  2. Đo số message thiếu/fuzzy của catalog `vi` **trước fallback**, chặn CI theo con số này.
  3. Chạy Playwright với pseudo-locale và với `vi`, rồi axe/so ảnh (3.10, 3.11).
  4. Gom formatter ngày/số/tiền vào một lớp chung; chốt locale và timezone từng màn.
  5. Giữ catalog, glossary, phiên bản công cụ trong git; chỉ coi Weblate là cổng khi đã cấu hình quyền reviewer.
  6. Kiểm font có glyph tiếng Việt, dấu tổ hợp, input method trên thiết bị thật.
- **Phù hợp khi / Không nên khi:** Phù hợp cho sản phẩm có từ hai ngôn ngữ hoặc tiền/ngày theo locale. Không nên tắt `escapeValue` toàn cục chỉ để bản dịch có markup.
- **Rủi ro & điều kiện:** i18next, Lingui MIT; Weblate GPL-3.0-or-later (tự host có chi phí vận hành, xét license khi sửa/phân phối). Dữ liệu Intl/CLDR khác phiên bản runtime cho kết quả khác. Chưa đo bundle size hay độ chính xác dịch AI.
- **Thay thế:** FormatJS/react-intl **(chưa xác minh)**, quy trình PR thuần git, kiểm nội dung Việt ở mục 18 §5b.
- **Hồ sơ gốc:** [06 §7u](06-ui-ux-design/README.md#i18n-lifecycle-2026-11-02) · `code-read` · 02/11/2026

### 3.13 Đồng bộ token và component contract với Figma (`sync-figma-token`, `component-contracts-figma`) — báo lệch nghiêm ngặt, duyệt rồi mới áp

- **Giải quyết:** Token và component giữa Figma và code trôi dần; agent sửa một phía mà phía kia không biết.
- **Cơ chế cốt lõi:** `sync-figma-token` so token giữa code và Figma variables, xuất báo cáo lệch nghiêm ngặt, **bắt buộc duyệt trước khi áp**, chỉ áp phần chênh và lưu báo cáo. `component-contracts-figma`: một file JSON contract là nguồn chung; `cc-figma-tokens` dựng collection Primitives/Semantic, `cc-figma-component` dựng component set với variant theo contract. Các skill chạy trên Figma MCP (`figma/mcp-server-guide`).
- **Áp dụng vào dự án khác:**
  1. Cài plugin `figma` từ `figma/mcp-server-guide` và nối Figma MCP.
  2. Viết contract JSON cho component chính (props, variant, state) cạnh token DTCG (3.7).
  3. Chạy `/sync-figma-token` trước mỗi lần bàn giao code; lưu báo cáo lệch trong PR.
  4. Dùng `/cc-figma-component` để dựng component set từ contract thay vì vẽ tay.
  5. Hỏi tác giả trước khi phân phối lại vì các repo chưa có LICENSE.
- **Phù hợp khi / Không nên khi:** Phù hợp khi đội có designer làm trên Figma và code dùng chung token. Không nên khi không có ghế Figma phù hợp hoặc không dùng Figma.
- **Rủi ro & điều kiện:** **Không có file LICENSE** ở cả hai repo (dùng nội bộ chép được, phân phối lại cần hỏi). Skill Figma chính chủ theo Figma Developer Terms. Dữ liệu thiết kế đi qua Figma MCP. Repo nhỏ, một tác giả mỗi repo.
- **Thay thế:** Penpot + MCP (06 §7zg), Framelink Figma-Context-MCP (06 §7p.4, PostHog bật mặc định), uSpec (06 §7ze).
- **Hồ sơ gốc:** [06 §7ze](06-ui-ux-design/README.md#7ze-kiểm-ảnh-bộ-skill-figma-cho-claude-telos-academy-11-skill-từ-figma-use-tới-cc-figma-tokens-ảnh-người-dùng-gửi-đọc-mã-16112026) · `code-read` · 16/11/2026

### 3.14 LottieFiles motion-design-skill + GSAP skills — phán đoán motion có bảng số, cộng kỹ thuật chính chủ

- **Giải quyết:** Agent làm animation tùy hứng: linear, opacity-only, thời lượng sai, stagger dài.
- **Cơ chế cốt lõi:** motion-design-skill: 1 SKILL.md + 16 reference; checklist 8 bước (mục tiêu cảm xúc → personality → property → duration → easing → hero/staging → lớp phụ → "1/3 rules"); 4 archetype có khoảng thời gian (Playful 150–300ms, Premium 350–600ms, Corporate 200–400ms, Energetic 100–250ms); bảng duration; entrance ease-out, exit ease-in; không linear cho chuyển động không gian; stagger tổng dưới 500ms. Thư viện-agnostic, không sinh file Lottie. gsap-skills: 8 skill chính thức (`gsap-core`, `-timeline`, `-scrolltrigger`, `-plugins`, `-utils`, `-react` với `useGSAP`/`gsap.context()`/SSR, `-performance`, `-frameworks`).
- **Áp dụng vào dự án khác:**
  1. Cài motion-design-skill làm lớp "phán đoán"; chọn một archetype cho sản phẩm và ghi vào DESIGN.md.
  2. Đưa bảng duration/easing vào token motion DTCG (3.7) thay cho số viết tay.
  3. Nếu dùng GSAP, cài `gsap-skills` để agent dùng `useGSAP` và cleanup đúng trong React.
  4. Đặt checklist chuẩn (WCAG, reduced-motion, 3.15) **trước** luật gu của skill.
- **Phù hợp khi / Không nên khi:** Phù hợp cho UI motion và motion graphics. Không nên dùng GSAP trong công cụ animation no-code cạnh tranh với Webflow (điều cấm của license GSAP).
- **Rủi ro & điều kiện:** Cả hai repo skill MIT. **Thư viện GSAP** dùng GreenSock Standard "no charge" License: miễn phí cả thương mại từ 4/2025 nhưng **không phải open source** (cấm công cụ no-code cạnh tranh Webflow, cấm reverse engineering). motion-design-skill 4 commit, 1 contributor, không cập nhật từ 5/2026; gsap-skills không commit code từ 4/2026.
- **Thay thế:** Motion (`motion/react`, 22 §2.6; Motion+ trả phí), Emil Kowalski skills (06 §7z.1), React Spring (06).
- **Hồ sơ gốc:** [22 §2.5](22-motion-design-animation/README.md#25-lottiefilesmotion-design-skill--nguyên-lý-không-thư-viện) · [22 §2.4](22-motion-design-animation/README.md#24-greensockgsap-skills--8-skill-chính-thức-của-gsap) · [22 §9l](22-motion-design-animation/README.md#9l-kiểm-ảnh-4-skill-claude-code-làm-animation-threejs-gsap-design-dna-motion-design-ảnh-người-dùng-gửi-đọc-mã-16112026) · `docs-read` · 16/11/2026

### 3.15 Cổng motion: reduced-motion + web-vitals + kiểm theo mốc thời gian (dotLottie/WAAPI) — motion có tiêu chí đạt/trượt

- **Giải quyết:** Skill motion dạy gu nhưng không có cổng nào thử reduced motion, jank, INP/CLS hay trạng thái giữa transition.
- **Cơ chế cốt lõi:** Ranh giới chuẩn: WCAG 2.2 SC 2.2.2 (chuyển động tự chạy > 5 giây song song nội dung khác phải pause/stop/hide được), 2.3.1 (ngưỡng flash), 2.3.3 AAA; Apple HIG (purposeful, optional, cancelable). `web-vitals` (Apache-2.0) đo LCP/INP/CLS người dùng thật, build `attribution` chỉ ra phần tử gây chậm. dotLottie-web (MIT) có `setFrame`, pause/freeze, destroy, state machine để kiểm một mốc xác định. Web Animations cho đặt `currentTime` khi pause; `cancel()` có thể làm `finished` reject.
- **Áp dụng vào dự án khác:**
  1. Thêm một lượt Playwright với `reducedMotion: 'reduce'` cạnh lượt thường; kiểm không còn transform lớn/tự chạy và không mất trạng thái.
  2. Seek/pause tại start, midpoint, overshoot, settle, cancel/reverse rồi so DOM/state và ảnh (3.11).
  3. Thử chuỗi input nhanh: hover/focus/click đảo chiều, unmount khi đang chạy, tạo–destroy nhiều lần.
  4. Gắn `web-vitals/attribution`, so INP/CLS trước–sau khi thêm animation trên thiết bị đích.
  5. Với dotLottie, gọi `setWasmUrl` **trước** preload/khởi tạo và tự host WASM nếu cần offline/CSP chặt.
- **Phù hợp khi / Không nên khi:** Phù hợp cho mọi web UI có animation. Không nên tự đặt luật "cấm mọi motion"; chuẩn có ngoại lệ "thiết yếu".
- **Rủi ro & điều kiện:** WCAG theo W3C Document License. dotLottie-web mặc định tải WASM từ jsDelivr, fallback unpkg (dữ liệu request rời máy). INP/LCP chỉ đo trên Chromium, cần nơi nhận RUM. Token Material 3 motion **(chưa xác minh)**.
- **Thay thế:** lottie-web (22 §9e), Lottie spec schema `lottie/lottie-spec` (22 §9g), `web-quality-skills` (06 §7t).
- **Hồ sơ gốc:** [22 §9g](22-motion-design-animation/README.md#9g-nâng-trần-2112026-nguyên-lý-motion-chính-thức-reduced-motion-và-cổng-đo-cho-motion-yêu-cầu-người-dùng) · [22 §9h](22-motion-design-animation/README.md#9h-motion-runtime-verification) · `code-read` (dotlottie-web) · 02/11/2026

### 3.16 HyperFrames (HeyGen) — HTML thuần thành video tất định, Apache-2.0, có skill cho agent

- **Giải quyết:** Cần làm video sản phẩm/explainer bằng code mà đội chỉ có HTML/CSS, và license engine phải dùng thương mại được.
- **Cơ chế cốt lõi:** Composition là `index.html`; timing bằng `data-start`, `data-duration`, `data-track-index`, `class="clip"`; adapter GSAP (mặc định), CSS, Lottie, Three.js, Anime.js, WAAPI. `@hyperframes/engine` seek timeline tới từng frame trong headless Chrome (Puppeteer), chụp, FFmpeg encode; `producer` trộn audio. CLI `init|preview|render|lint|check|snapshot|doctor…`; xuất MP4/MOV/WebM/GIF/PNG; chạy local, Docker, AWS Lambda hoặc cloud render của HeyGen. 21 skill (router `/hyperframes`, workflow `/product-launch-video`, `/pr-to-video`, `/embedded-captions`…).
- **Áp dụng vào dự án khác:**
  1. Cài `npx skills add heygen-com/hyperframes` hoặc `claude plugin install hyperframes@hyperframes`; Node 22+, FFmpeg.
  2. Ghim phiên bản HyperFrames, Chrome, FFmpeg trong render manifest (3.21).
  3. Chạy `hyperframes lint`/`check` trong CI trước render.
  4. Render master cục bộ hoặc Lambda; chỉ dùng cloud render/media library HeyGen khi chấp nhận tài khoản và dữ liệu rời máy.
  5. Đưa bản xuất qua cổng phát hành (3.22).
- **Phù hợp khi / Không nên khi:** Phù hợp khi đội mạnh HTML/CSS, cần license thoáng. Không nên khi cần render hàng loạt đã chín (README HyperFrames tự thừa nhận Remotion Lambda chín hơn) hoặc cần API ổn định (vẫn 0.8.x pre-1.0).
- **Rủi ro & điều kiện:** Toolkit Apache-2.0; **GSAP, font, ảnh, nhạc trong composition có license riêng** (Apache của toolkit không cấp quyền media). Có thể tải font lần render đầu. Stack nặng (Node 22, Chrome, FFmpeg); 180 PR mở; lực hút lock-in qua tính năng cần tài khoản HeyGen.
- **Thay thế:** Remotion (3.17), Motion Canvas/Revideo (22 §9b), Playwright + ffmpeg tự chế (claude-motion-design, 22 §3.3).
- **Hồ sơ gốc:** [22 §2.1](22-motion-design-animation/README.md#21-hyperframes-heygen--write-html-render-video-built-for-agents) · [19 §3h](19-agentic-video-media/README.md#3h-kiểm-ảnh-ai-video-stack-remotion-skills-blender-và-blender-mcp-faster-whisper-chatterbox-gsap-ảnh-người-dùng-gửi-đọc-mã-8112026) · `docs-read` · 08/11/2026

### 3.17 Remotion + `remotion-dev/skills` — video bằng React, đơn vị là frame; kiểm license trước khi chọn

- **Giải quyết:** Video có data/props, cần hệ sinh thái React và render hàng loạt.
- **Cơ chế cốt lõi:** `useCurrentFrame()`, `durationInFrames`, `fps` trong `<Composition>`; headless Chrome chụp từng frame, FFmpeg encode; Node API, CLI, Lambda, WebCodecs. 12–13 skill chính thức gom dưới `/remotion-best-practices` (create, markup, render, captions, maps, multimedia…). Đọc mã: `random(seed)` ổn định khi truyền cùng seed nhưng **`random(null)` gọi `Math.random()`**; seed không khóa font, ảnh URL động, codec, browser, GPU. `render-media.ts` nhận `inputProps`, `frameRange`, concurrency, timeout cần lưu cùng manifest. MCP server của Remotion đã deprecated.
- **Áp dụng vào dự án khác:**
  1. Kiểm điều kiện pháp nhân với Remotion License **trước** khi viết dòng code đầu tiên.
  2. `npx create-video@latest`, thêm skill bằng `npx skills add remotion-dev/skills`.
  3. Luôn truyền seed tường minh cho `random`; lưu `inputProps`, `frameRange`, phiên bản engine/browser/codec.
  4. Dùng `/remotion-captions` với transcript từ 3.23.
  5. Đưa master qua cổng phát hành (3.22).
- **Phù hợp khi / Không nên khi:** Phù hợp cho cá nhân, tổ chức đủ điều kiện Free License, hoặc công ty đã mua Company License. Không nên khi công ty vượt ngưỡng nhân sự mà chưa có ngân sách license.
- **Rủi ro & điều kiện:** **Remotion License, không phải OSI**: miễn phí cho cá nhân, tổ chức lợi nhuận tới 3 nhân viên, phi lợi nhuận, đánh giá; còn lại cần Company License (giá theo remotion.pro 10/2026, có thể đổi ở v5). Repo skill **không có LICENSE riêng** và nội dung trôi theo monorepo. Font/nhạc/ảnh/template kiểm riêng. Byte-for-byte giống nhau giữa phần cứng **(chưa xác minh)**.
- **Thay thế:** HyperFrames (3.16), Motion Canvas (22 §9b), `claude-remotion-skill` (22 §5.3).
- **Hồ sơ gốc:** [22 §2.2](22-motion-design-animation/README.md#22-remotion--video-bằng-react-đơn-vị-thời-gian-là-frame) · [22 §9j.1](22-motion-design-animation/README.md#remotion-factory) · [22 §2.3](22-motion-design-animation/README.md#23-remotion-devskills--12-skill-chính-thức) · `docs-read` (catalog 08/11/2026); đọc mã `random.ts`/`render-media.ts`/LICENSE 04/11/2026

### 3.18 ffmpeg-skill (`kajisho5`) — 42 tool có kiểu bọc ffmpeg/ffprobe, quy trình probe → sửa → kiểm → verify

- **Giải quyết:** Agent tự ghép lệnh ffmpeg dễ sai, ghi đè file nguồn, không kiểm đầu ra.
- **Cơ chế cốt lõi:** 42 tool Python chỉ dùng thư viện chuẩn, nhận tham số có kiểu (`--aspect 9:16 --fit pad`). `input_schema` của mỗi tool **sinh từ parser `argparse`** lúc chạy, CI báo lỗi nếu lệch. Từ chối ghi đè nguồn nếu thiếu `--overwrite`. MCP mặc định chỉ liệt kê 12 tool "stable"; 30 tool còn lại beta. PRIVACY.md: không telemetry, không mạng (trừ engine Whisper người dùng tự cài có thể tải model). CI ma trận Ubuntu/macOS/Windows × Python 3.10/3.13 × FFmpeg 6.1–9, CodeQL, Scorecard, ClusterFuzzLite.
- **Áp dụng vào dự án khác:**
  1. Cài `npx ffmpeg-skill` hoặc plugin, ghim phiên bản (hồ sơ đọc v4.7.0, commit `c559cb5`).
  2. Chạy `doctor` để biết FFmpeg có codec cần.
  3. Đặt `FFMPEG_SKILL_MCP_TOOLS` chỉ gồm tool đang cần.
  4. Luôn `--dry-run --json` trước bước ghi; không bỏ cờ bảo vệ nguồn.
  5. Ghép `ffprobe` vào bước verify của pipeline (3.21).
- **Phù hợp khi / Không nên khi:** Phù hợp khi agent xử lý video/audio cục bộ thường xuyên. Không nên khi chỉ cần vài công thức; bản cheatsheet `n0an/ffmpeg-skill` nhẹ hơn nhiều.
- **Rủi ro & điều kiện:** Skill MIT; **FFmpeg là LGPL-2.1+ hoặc GPL tùy cấu hình build** (xét khi phân phối kèm). Repo rất lớn (khoảng 27 nghìn dòng Python), một tác giả; 30/42 tool beta. Chưa chạy test hay tool nào trong hồ sơ. ★ (chưa xác minh).
- **Thay thế:** `n0an/ffmpeg-skill` (cheatsheet, `docs-read`), ffmpeg.wasm (19, trong trình duyệt), LosslessCut (19, GUI).
- **Hồ sơ gốc:** [19 ffmpeg-skill (kajisho5)](19-agentic-video-media/README.md#xlsx-2026-11-23-ffmpeg-skill-kajisho5) · `code-read` · 23/11/2026

### 3.19 Dựng footage theo transcript từng từ (herk-edit-kit `cut-silences`, video-use) — LLM "đọc" video thay vì "xem"

- **Giải quyết:** Đưa toàn bộ khung hình cho model rất tốn; cắt khoảng lặng/lỗi bằng tay chậm.
- **Cơ chế cốt lõi:** herk-edit-kit (tên cũ HyperFrames Student Kit): `cut-silences.mjs` đọc JSON transcript từng từ (ElevenLabs Scribe hoặc JSON chung), sinh **EDL** + transcript đã tái định thời, chỉ chạy ffmpeg khi có `--apply`; CI chạy `check`, `test`, `preflight`, `hyperframes lint` trên 3 OS; `skills-lock.json` ghi hash từng skill bên thứ ba. video-use: gộp transcript thành `takes_packed.md` khoảng 12KB, chỉ gọi ảnh `timeline_view` (filmstrip + sóng âm) ở điểm quyết định; `helpers/render.py` có fade 30ms, loudnorm −14 LUFS. "Tự đánh giá ở mỗi điểm cắt" của video-use chỉ là lời dặn, không có mã kiểm.
- **Áp dụng vào dự án khác:**
  1. Lấy transcript từng từ bằng engine cục bộ (faster-whisper/WhisperX, 3.23) nếu footage nhạy cảm.
  2. Sinh EDL, cho người xem lại EDL/transcript trước khi `--apply`.
  3. Khóa hash skill bên thứ ba như `skills-lock.json`.
  4. Chạy `npm run check`/`npm test` của kit sau khi ghim.
  5. Đưa bản xuất qua loudness và kiểm timeline (3.21, 3.22).
- **Phù hợp khi / Không nên khi:** Phù hợp cho talking-head, podcast video, short-form từ footage dài. Không nên khi footage không có lời thoại rõ (transcript không đại diện nội dung hình).
- **Rủi ro & điều kiện:** herk-edit-kit **license ba lớp**: MIT cho tài liệu gốc, pipeline theo `PIPELINE-USE-PERMISSION.txt`, skill HyperFrames Apache-2.0, GSAP/font/media mẫu có quyền riêng. **Dữ liệu rời máy:** mặc định gửi âm thanh tới `api.elevenlabs.io`; `kie.mjs` gửi ảnh/prompt tới `api.kie.ai`. video-use MIT, mọi âm thanh đi ElevenLabs, không có Whisper cục bộ, không CI.
- **Thay thế:** claude-video `/watch` (19 §3b, có engine local), PySceneDetect (3.21), ffmpeg-skill (3.18).
- **Hồ sơ gốc:** [22 herk-edit-kit](22-motion-design-animation/README.md#xlsx-2026-11-23-herk-edit-kit) · [19 §3b](19-agentic-video-media/README.md#3b-nâng-cấp-31102026-rà-repo-lớn) · `code-read` (herk-edit-kit, 23/11/2026); video-use catalog chưa gắn mức (đọc mã 31/10/2026)

### 3.20 lemo-opuscar — phim làm hoàn toàn bằng code với 66 phong cách, có cổng máy cho thời gian đọc chữ

- **Giải quyết:** Video AI hay đặt chữ quá ngắn để đọc; skill video phần lớn chỉ có lời dặn, khó kiểm.
- **Cơ chế cốt lõi:** Hình vẽ bằng canvas/WebGL render từng khung, nhạc từ thư viện sample, lời dẫn bằng TTS; không dùng model sinh video. 66 phong cách trong `styles/` (mỗi cái có `STYLE.md` + phim mẫu), `DIRECTOR.md`, `TECHNIQUE.md`. `core/render/readcheck.mjs` buộc mỗi khối chữ đứng yên ≥ (số chữ CJK ÷ 4,5 + ký tự Latin ÷ 15) + 1,5 giây; **mã thoát 2 ("không chạy được") không được tính là pass**. Có contact sheet (`sheet.py`) và kiểm ASR cho lời đọc (`asr_check.py`).
- **Áp dụng vào dự án khác:**
  1. Cài `claude plugin marketplace add lemomo-ai/lemo-opuscar` rồi `claude plugin install lemo-opuscar@lemolab`; Node 20+, ffmpeg 7+, Python 3.11+.
  2. Mượn riêng quy tắc `readcheck` (công thức thời gian đọc + exit code "không chạy được ≠ pass") cho pipeline video của mình.
  3. Dùng `asr_check.py` để so lời đọc TTS với kịch bản.
  4. Tạo phong cách riêng qua `MY-STYLES.md` (lưu ở `~/lemo-my-styles/`).
  5. Chọn Kokoro cục bộ thay edge-tts nếu không muốn gửi văn bản tới Microsoft.
- **Phù hợp khi / Không nên khi:** Phù hợp cho explainer, bản tin, Evidence Films có nguồn số liệu. Không nên khi cần cảnh quay thật hoặc ngân sách agent thấp (mỗi phim khoảng 30–60 phút agent).
- **Rủi ro & điều kiện:** Mã và tài liệu MIT; phim mẫu và ảnh tĩnh CC BY 4.0; font OFL; tài sản 3D từ Poly Haven. edge-tts gọi dịch vụ Microsoft. Repo mới (tạo 26/9/2026), phần lớn commit từ một tài khoản.
- **Thay thế:** HyperFrames (3.16), herk-edit-kit `motion-showreel` (3.19), OpenFilm (22 §9e).
- **Hồ sơ gốc:** [22 §9k](22-motion-design-animation/README.md#9k-đọc-lại-lemomo-ailemo-opuscar-66-phong-cách-phim-làm-bằng-code-cài-bằng-plugin-claude-code-ảnh-slide-người-dùng-gửi-đọc-mã-8112026) · `code-read` · 08/11/2026

### 3.21 OpenTimelineIO + PySceneDetect + asset manifest — pipeline media dựng lại được

- **Giải quyết:** Video xuất ra không tái kiểm được: không biết asset nào, phiên bản renderer nào, timeline lệch, thiếu footage.
- **Cơ chế cốt lõi:** OTIO: clip/track/gap/transition, `RationalTime` lưu giá trị + rate, `ExternalReference` trỏ `target_url` và `available_range`; OTIO **cho phép `source_range` vượt `available_range` mà không tự xác minh**; effects phụ thuộc ứng dụng; không phải renderer. PySceneDetect: `ContentDetector`, `AdaptiveDetector` (so content score với rolling average) xuất scene list ứng viên.
- **Áp dụng vào dự án khác:**
  1. Lập asset manifest: URL gốc, hash, license, ngày tải, biến đổi cho mỗi ảnh/footage/font/nhạc/giọng; asset chưa rõ quyền ở trạng thái chưa duyệt.
  2. Ghim fps/timebase, resolution, color space, sample rate, duration; dùng rational time.
  3. Preflight trước render: asset tồn tại, source range đủ handles, font tải xong, caption trong duration/safe area.
  4. Dùng PySceneDetect tạo candidate cut, đối chiếu shot list hoặc nhãn người.
  5. Khi đổi editor bằng OTIO, test round-trip duration/source range/track/effect; effect mất nghĩa thì bake hoặc báo.
  6. Lưu manifest, timeline, master, bản phát hành và kết quả kiểm liên kết bằng hash.
- **Phù hợp khi / Không nên khi:** Phù hợp cho xưởng làm video lặp lại, nhiều người/agent. Không nên dùng số cut làm điểm "video hay".
- **Rủi ro & điều kiện:** OTIO Apache-2.0, PySceneDetect BSD-3-Clause; chạy cục bộ. Chưa kiểm round-trip adapter hay chạy renderer tại kho. Seed không bảo đảm GPU sinh ảnh/video tất định.
- **Thay thế:** EDL của herk-edit-kit (3.19), ffmpeg scene filter, cut viết tay trong Remotion/HyperFrames.
- **Hồ sơ gốc:** [19 §3e](19-agentic-video-media/README.md#3e-reproducible-media-pipelines) · `code-read` · 02/11/2026

### 3.22 Cổng phát hành media: loudness EBU R128 + VMAF + C2PA (c2patool/c2pa-rs) — chất lượng kỹ thuật và provenance theo trust policy

- **Giải quyết:** Pipeline dừng ở file MP4; không có thước đo khách quan cho tiếng/hình sau nén và không gắn nhãn nguồn gốc AI.
- **Cơ chế cốt lõi:** EBU R128/ITU-R BS.1770: phát sóng −23 LUFS ±1 LU, true peak −1 dBTP; `ffmpeg -af loudnorm` mặc định theo R128 (nền tảng streaming dùng mục tiêu khác, nhiều skill mục 22 master −14 LUFS). VMAF (+ PSNR, SSIM, CAMBI dò banding) **cần video tham chiếu**; `ffmpeg-quality-metrics` bọc ffmpeg tính theo từng frame. c2pa-rs tách `ValidationState` **Invalid / Valid / Trusted**; c2patool nhánh đọc thường trả thành công khi in được report, **không tự áp chính sách "chỉ Trusted"**; nhánh `fragment` mới trả lỗi khi có file Invalid.
- **Áp dụng vào dự án khác:**
  1. Thêm `loudnorm` hai lượt và kiểm độ dài, fps, frame đen/đứng vào QC; ghi mục tiêu LUFS theo nơi đăng.
  2. Render master, so mỗi bản nén cho từng kênh với master bằng `ffmpeg-quality-metrics` (cần ffmpeg build có `libvmaf`); chặn theo ngưỡng tự đặt.
  3. Ký manifest C2PA **sau bước nén cuối** (ghi model, công cụ, cờ AI-generated, asset nguồn).
  4. Verifier đọc `validation_state` theo trust policy, không chỉ nhìn exit 0.
  5. Có bộ ca âm: asset sửa sau ký, thiếu manifest, signer ngoài policy, transcoding mất metadata.
  6. Thêm watermark ẩn (VideoSeal/AudioSeal) làm lớp dự phòng khi metadata bị gỡ.
- **Phù hợp khi / Không nên khi:** Phù hợp cho video phát hành ra ngoài, nhất là có nội dung AI. Không nên dùng VMAF để chấm video AI tự sinh không có tham chiếu (dùng VBench khi chọn model).
- **Rủi ro & điều kiện:** VMAF BSD-2-Clause-Patent; c2pa-rs/c2patool MIT OR Apache-2.0 (0.x, API đổi nhanh); spec C2PA CC-BY-4.0. Ký thật cần chứng thư trong trust list; không có thì manifest chỉ là "tự khai". C2PA không cấp quyền dùng asset, không chứng minh nội dung đúng. Chưa ký asset hay diễn tập trust store tại kho.
- **Thay thế:** `qc.py` (mục 23), VBench để chọn model (19 §3d), `opus-sound-layer qa.py` cho loudness (22 §9i).
- **Hồ sơ gốc:** [19 §3d](19-agentic-video-media/README.md#3d-nâng-trần-2112026-nguồn-gốc-nội-dung-c2pa-watermark-và-đo-chất-lượng-video-vmaf-vbench-loudness-yêu-cầu-người-dùng) · [19 §3g](19-agentic-video-media/README.md#factory-media-release-2026-11-04) · `code-read` (c2patool, c2pa-rs 04/11/2026); VMAF/R128 catalog chưa gắn mức (đọc README/LICENSE 02/11/2026)

### 3.23 faster-whisper + WhisperX — chép lời có timestamp từng từ, alignment và diarization là bước có lỗi riêng

- **Giải quyết:** Phụ đề khớp giọng, cắt theo transcript, ghi âm phỏng vấn khách hàng thành văn bản dẫn được về đoạn ghi âm.
- **Cơ chế cốt lõi:** faster-whisper chạy Whisper trên CTranslate2; README công bố nhanh tới 4 lần bản gốc, có `BatchedInferencePipeline`, timestamp từng từ, lọc VAD; GPU cần CUDA 12 + cuDNN 9. WhisperX (`transcribe.py`): ASR → alignment (có model mặc định theo ngôn ngữ, **gồm tiếng Việt**) → diarization nếu bật → gán speaker theo word → writer. Diarization tải `pyannote/speaker-diarization-community-1` qua `Pipeline.from_pretrained` (cần token và chấp nhận điều khoản model). README tự nêu speech chồng lấn xử lý kém, nhãn SPEAKER không xác thực danh tính.
- **Áp dụng vào dự án khác:**
  1. Dùng faster-whisper làm baseline (`pip install faster-whisper`); bật `word_timestamps` cho phụ đề.
  2. Chỉ thêm WhisperX khi cần word timing chính xác hoặc phân người nói.
  3. Ghim model revision và hash audio; prefetch model rồi kiểm pipeline trong môi trường chặn egress nếu cần bí mật.
  4. Dựng corpus tiếng Việt (vùng miền, code-switching, số tiền, tên riêng, nhiều người nói) và đo WER/CER bằng `jiwer` (3.25).
  5. Có fixture im lặng/quá ngắn/chồng lấn với trạng thái rõ, không sinh transcript bịa.
- **Phù hợp khi / Không nên khi:** Phù hợp cho batch transcription, phụ đề, dựng theo transcript. Không nên dùng cho voice agent realtime (dùng 3.24).
- **Rủi ro & điều kiện:** faster-whisper MIT; WhisperX code BSD-2-Clause nhưng **weights ASR/alignment/diarization có license riêng** (không suy BSD sang model). Tải model/cache không chứng minh audio đã rời máy hay chưa; kiểm egress. Benchmark tốc độ là số upstream, chưa tái lập.
- **Thay thế:** whisper.cpp (thiết bị cục bộ), VibeVoice-ASR (14 §5c), PhoWhisper (mục 18).
- **Hồ sơ gốc:** [14 §5g WhisperX](14-voice-multimodal/README.md#factory-2026-11-04-whisperx) · [19 §3h](19-agentic-video-media/README.md#3h-kiểm-ảnh-ai-video-stack-remotion-skills-blender-và-blender-mcp-faster-whisper-chatterbox-gsap-ảnh-người-dùng-gửi-đọc-mã-8112026) · `code-read` (WhisperX 04/11/2026) · `docs-read` (faster-whisper 08/11/2026)

### 3.24 Voice agent realtime: Pipecat/LiveKit + Silero VAD (+ aiortc khi cần transport thấp tầng) — đo lượt nói, barge-in, reconnect

- **Giải quyết:** Voice agent chạy được trong demo nhưng hỏng ở chen ngang, mất mạng, giọng vùng miền, quyền micro.
- **Cơ chế cốt lõi:** Pipecat là pipeline Python cho voice/multimodal agent; LiveKit Agents có WebRTC, telephony, nhiều client SDK (cơ chế hai framework **chưa đọc mã trong hồ sơ**). Silero VAD: wrapper ONNX quy định khung 512 mẫu ở 16 kHz, 256 ở 8 kHz, có `reset_states()`, nên không dùng chung state giữa các phiên độc lập. aiortc: WebRTC/ORTC asyncio, `RTCPeerConnection` có trạng thái và `close()` dọn sender/receiver; không có signaling production, quản lý lượt nói hay chính sách lưu âm.
- **Áp dụng vào dự án khác:**
  1. Chọn Pipecat (pipeline processor, backend Python) hoặc LiveKit (room/participant, hạ tầng realtime đóng gói); aiortc chỉ khi cần tự kiểm soát transport.
  2. Ghim transport, VAD, STT/TTS và model revision; ghim revision + checksum model Silero.
  3. Đo từng đoạn `end_of_user_speech → transcript_final → first_llm_token → first_audio` theo p50/p95.
  4. Thử ma trận lỗi: im lặng/ồn/giọng Bắc–Trung–Nam, chen ngang khi TTS phát và khi tool chạy, mất mạng/reconnect, rút quyền micro.
  5. Tác vụ có side effect chỉ xác nhận một lần qua executor; hủy audio không mặc nhiên hủy tác vụ ghi.
  6. Đánh giá hội thoại nhiều lượt bằng EVA (ServiceNow) với kịch bản tiếng Việt tự viết.
- **Phù hợp khi / Không nên khi:** Phù hợp cho voice agent hỏi đáp/đặt lịch/CSKH. Không nên thay framework hoàn chỉnh bằng thư viện transport chỉ vì API nhỏ hơn.
- **Rủi ro & điều kiện:** Pipecat BSD-2, LiveKit Agents Apache-2.0 (**model turn-detection license riêng**), Silero MIT, aiortc BSD-3-Clause. Audio thường rời máy tới STT/TTS/LLM cloud tùy cấu hình; giữ audio thô tách khỏi trace, có policy lưu và quyền clone giọng riêng với quyền micro. EVA cần key ElevenLabs/OpenAI/Google/AWS (tốn phí).
- **Thay thế:** TEN Framework (14 §1), OpenAI Realtime/Gemini Live (đóng), WebRTC VAD hoặc VAD sẵn trong framework.
- **Hồ sơ gốc:** [14 §5e](14-voice-multimodal/README.md#5e-voice-reliability) · [14 §1](14-voice-multimodal/README.md#1-framework-voice-agent-realtime) · `code-read` (Silero VAD, aiortc 02/11/2026); Pipecat/LiveKit catalog chưa gắn mức

### 3.25 TTS có license rõ (VoxCPM2, Kokoro, Chatterbox) + đo WER/MOS + watermark AudioSeal — chọn giọng đọc theo weights, không theo code

- **Giải quyết:** Chọn TTS theo benchmark tự công bố, rồi phát hiện weights cấm thương mại hoặc không có tiếng Việt; không có cách chặn hồi quy chất lượng giọng.
- **Cơ chế cốt lõi:** VoxCPM (OpenBMB): README và LICENSE ghi **Apache-2.0 cho cả code và weights**; VoxCPM2 2B, 30 ngôn ngữ **có tiếng Việt**, 48 kHz, thiết kế giọng; hồ sơ gọi là ứng viên TTS clone giọng tiếng Việt có license thoáng nhất trong kho (benchmark tự đo). Kokoro 82M Apache-2.0, nhẹ, không clone giọng, repo code đứng từ 8/2025. Chatterbox MIT, mọi file sinh ra có watermark PerTh kèm script kiểm. Đo: `jiwer` (WER/CER), UTMOSv2 (dự đoán MOS, chỉ so tương đối với tiếng Việt), AudioSeal (watermark theo đoạn, MIT cả weights, có id soft-binding C2PA).
- **Áp dụng vào dự án khác:**
  1. Đọc model card của **từng checkpoint** trước khi chọn; loại F5-TTS weights (CC-BY-NC), Fish S2 Pro (Research License) nếu cần thương mại.
  2. Thử VoxCPM2 (`pip install voxcpm`) cho tiếng Việt; Kokoro khi cần nhẹ, không clone.
  3. Lập bộ câu cố định; chấm UTMOSv2 mỗi khi đổi model/giọng, định kỳ cho người nghe thật duyệt.
  4. Vòng TTS → STT → `jiwer` để bắt đọc sai số tiền, tên riêng; tự định nghĩa chuẩn hóa dấu thanh và số.
  5. Với giọng clone: lưu nhật ký đồng ý, chèn AudioSeal và ký C2PA (3.22).
- **Phù hợp khi / Không nên khi:** Phù hợp cho lời dẫn video, voice UI, voice agent. Không nên clone giọng khi chưa có đồng ý bằng văn bản của chủ giọng.
- **Rủi ro & điều kiện:** **License code và weights tách nhau**: VoxCPM Apache-2.0 cả hai; Kokoro Apache-2.0; Chatterbox MIT (repo lưu trữ công khai từ 8/2026); F5-TTS/Fish/Audio8 0.1B có weights hạn chế. Model tải từ Hugging Face; suy luận cục bộ được. Watermark có thể bị tấn công gỡ, không thay hồ sơ quyền giọng. UTMOSv2 với tiếng Việt **(chưa xác minh)**.
- **Thay thế:** VieNeu-TTS (mục 18), Voicebox app local nhiều engine (14 §5c), ElevenLabs skills (22, dịch vụ trả phí).
- **Hồ sơ gốc:** [14 §5c](14-voice-multimodal/README.md#5c-nâng-cấp-31102026-rà-repo-lớn) · [14 §3](14-voice-multimodal/README.md#3-text-to-speech-tts) · [14 §5d](14-voice-multimodal/README.md#5d-nâng-trần-2112026-đo-chất-lượng-giọng-nói-wer-mos-eval-voice-agent-và-watermark-yêu-cầu-người-dùng) · `docs-read` (Chatterbox 08/11/2026); VoxCPM/Kokoro/jiwer/UTMOSv2/AudioSeal catalog chưa gắn mức (đọc LICENSE/README 31/10–02/11/2026)

---

**Ghi chú phạm vi:** Chương này chỉ chép lại cơ chế đã có trong hồ sơ; không có bước nào ở trên được kho chạy thử trên dự án tích hợp. Trước khi áp dụng, kiểm lại license, telemetry/endpoint và trạng thái bảo trì tại commit sẽ dùng (METHOD.md §5). Ngày "kiểm" là ngày đọc trong hồ sơ, không phải ngày tái lập.

## 4. Xưởng phần mềm: chất lượng, phát hành & vận hành

> Chắt lọc từ các mục 09, 13, 28–34 và `data/projects.json` của kho `stored` (đọc lại ngày 2026-11-23). Mọi "cơ chế cốt lõi" lấy từ hồ sơ gốc; **mức bằng chứng là của hồ sơ** (`code-read` = đã đọc LICENSE/mã/CI tại SHA cố định; `docs-read` = đọc tài liệu; `unassessed` = hồ sơ cũ chưa chuẩn hóa mức kiểm). Kho chưa cài, chạy hay benchmark công cụ nào; các bước "Áp dụng" là đề xuất cho repo sản phẩm, phải kiểm lại license/phiên bản trước khi dùng. Mục 27 (CAD/BIM) không đưa vào vì không có hồ sơ là công cụ kỹ thuật phần mềm dùng chung.

**Nguyên tắc xuyên suốt rút từ các hồ sơ:** (1) một cổng chỉ có giá trị khi **mã thoát** của nó thực sự đỏ lúc có lỗi — nhiều công cụ mặc định thoát 0 khi chỉ in cảnh báo; (2) mỗi cổng cần một **fixture cố tình sai** chứng minh nó chặn được; (3) phân biệt pass / fail / chưa chạy / bị chặn / không áp dụng — "0 test" hay "scanner timeout" không phải pass.

### Nhu cầu → item nên dùng

| Nhu cầu | Item nên dùng (theo thứ tự ưu tiên) | Ghi chú chọn |
|---|---|---|
| Test xanh nhưng không chắc có test chạy | 4.1 pytest/Vitest → 4.2 Hypothesis | Bắt "0 test = pass" trước khi bàn coverage |
| Mock lệch production (DB, queue) | 4.3 Testcontainers → 4.23 goose | Integration với dependency thật, ghim image |
| API công khai hay bị phá client | 4.8 oasdiff → 4.4 Schemathesis | Diff spec trước, fuzz runtime sau |
| Kiến trúc trôi, import trái lớp | 4.7 dependency-cruiser → 4.9 Doorstop/ADR | Rule có fixture xấu/tốt |
| CI/dependency là bề mặt tấn công | 4.12 actionlint+zizmor → 4.13 SBOM+quét → 4.15 SOPS | Pin SHA, quyền tối thiểu, secret ngoài git |
| Môi trường "máy tôi chạy được" | 4.16 mise → 4.11 pre-commit | Cùng entrypoint local và CI |
| Phát hành/hạ tầng an toàn, quay lui được | 4.19 semantic-release → 4.17 OpenTofu → 4.18 Argo CD | Build một lần, promote theo digest |
| Biết khi production hỏng và phục hồi | 4.21 Sloth → 4.20 OTel Collector → 4.22 restic | SLO + telemetry có redaction + restore drill |
| SaaS nhiều tenant, đăng nhập/quyền | 4.24 Keycloak → 4.23 goose | Identity ≠ authorization; test chéo tenant |
| Ra quyết định sản phẩm bằng số đo | 4.25 flagd/GrowthBook → 4.5 k6 (guardrail hiệu năng) | Assignment ≠ exposure ≠ kết luận |

---

### 4.1 pytest & Vitest (cổng "không thu được test là đỏ") — Ngăn pipeline báo xanh khi thực tế không có test nào chạy

- **Giải quyết:** Suite "xanh" do không collect được test, cấu hình lọc hết target, hoặc shell pipeline nuốt mã thoát.
- **Cơ chế cốt lõi:** pytest `_main` collect rồi `runtestloop`, trả `TESTS_FAILED` khi có failure và **`NO_TESTS_COLLECTED = 5`** khi không thu được test; enum tách interruption/internal/usage error. Vitest `test-run.ts` thất bại khi module không ok, nhưng khi không có module thì phụ thuộc `passWithNoTests` — logger mô tả trường hợp cấu hình đó thoát 0 dù không có file test.
- **Áp dụng vào dự án khác:**
  1. Gọi runner trực tiếp trong CI (không `| tee` làm mất exit code; dùng `set -o pipefail` nếu cần pipe).
  2. Coi pytest exit 5 là lỗi với suite bắt buộc; không bật `passWithNoTests` ở Vitest cho job required.
  3. Xuất report JUnit/JSON, kiểm **số test executed ≥ ngưỡng kỳ vọng** và giữ skipped/todo/xfail thành cột riêng.
  4. Fixture âm: một nhánh CI chạy với thư mục test rỗng/sai pattern phải đỏ.
  5. Snapshot mới phải có reviewer; không để agent tự duyệt snapshot do chính bản sửa tạo ra.
- **Phù hợp khi / Không nên khi:** Phù hợp mọi repo Python (pytest) hoặc JS/TS dùng Vite (Vitest). Không nên dùng Vitest Browser Mode như E2E toàn hệ; repo JS không dùng Vite có thể giữ Jest.
- **Rủi ro & điều kiện:** Plugin/hook pytest có thể thay hành vi — test cấu hình trước khi áp kỳ vọng mã thoát; session fixture dễ tạo phụ thuộc thứ tự. Retry phải ghi riêng first-attempt-fail.
- **Thay thế:** Jest (`docs-read`, [30#anhkysuai-jestjs-jest](30-software-testing-quality/README.md#anhkysuai-jestjs-jest)); testify cho Go ([30#anhkysuai-stretchr-testify](30-software-testing-quality/README.md#anhkysuai-stretchr-testify)).
- **Hồ sơ gốc:** [30-software-testing-quality/README.md#pytest-factory](30-software-testing-quality/README.md#pytest-factory) · [30-software-testing-quality/README.md#vitest-factory](30-software-testing-quality/README.md#vitest-factory) · `code-read` (pytest `8b005ed7`, Vitest `289caab9`) · kiểm 2026-11-04

### 4.2 Hypothesis — Tìm phản ví dụ cho invariant nghiệp vụ mà test viết tay bỏ sót

- **Giải quyết:** Test ví dụ chỉ phủ vài input "đẹp"; lỗi làm tròn tiền, serialize/parse, state machine lọt qua.
- **Cơ chế cốt lõi:** Sinh input theo strategy, tìm và **thu nhỏ** phản ví dụ; example database lưu ca hữu ích để chạy lại nhưng **không phải đặc tả đầy đủ** của lỗi đã biết — tài liệu khuyên ghi ví dụ rõ ràng cho regression quan trọng. Settings `deadline`/`max_examples`/`derandomize` chọn theo suite.
- **Áp dụng vào dự án khác:**
  1. Chọn 2–3 invariant độc lập implementation: `decode(encode(x)) == x`, tổng phân bổ bảo toàn theo quy tắc làm tròn, thao tác bị từ chối không đổi trạng thái.
  2. Khai báo miền input rõ (strategy), không viết lại cùng công thức của hàm cần kiểm làm oracle.
  3. Khi tìm được phản ví dụ, chép nó thành `@example`/test cố định có version.
  4. Ghim phiên bản Hypothesis; ghi settings/seed vào report.
- **Phù hợp khi / Không nên khi:** Phù hợp parser, tính tiền, serialization, máy trạng thái. Không nên thay kiểm yêu cầu nghiệp vụ hay dùng timeout làm assertion đúng/sai.
- **Rủi ro & điều kiện:** Sinh dữ liệu tốt không tự sinh oracle đúng; cùng seed không bảo đảm tái tạo sau khi nâng dependency. License MPL-2.0.
- **Thay thế:** fast-check cho JS/TS (ghi nhận trong [13 §4b](13-dev-stack-devops/README.md#4b-quality-gate-stack-quan-sát-trong-19-repo-của-chủ-kho-mục-23-2026-10-12), `unassessed`); Schemathesis (4.4) dùng Hypothesis để sinh request.
- **Hồ sơ gốc:** [30-software-testing-quality/README.md#hypothesis-factory](30-software-testing-quality/README.md#hypothesis-factory) · `code-read` (`535f94db`) · kiểm 2026-11-04

### 4.3 Testcontainers (Python) — Integration test với Postgres/Redis/queue thật, sống ngắn

- **Giải quyết:** Mock hoặc SQLite khác hành vi DB production (transaction, constraint, kiểu dữ liệu).
- **Cơ chế cốt lõi:** `Container.start` khởi tạo Ryuk (khi bật), tạo container và gọi wait strategy; context manager cleanup khi khởi động lỗi. `PostgresContainer` kiểm readiness bằng truy vấn psql. Module `testcontainers.postgres` đã deprecated → `testcontainers.community.postgres`; constructor mặc định image **`postgres:latest`**.
- **Áp dụng vào dự án khác:**
  1. Ghim image theo version/digest đúng DB production, không dùng default `latest`.
  2. Trong fixture: start container → áp **migration thật** → seed dữ liệu thử → chạy test ghi/đọc/transaction/constraint.
  3. Mỗi worker/tenant dùng DB hoặc schema riêng để test song song không đụng nhau.
  4. Chạy trên runner CI có Docker với phạm vi quyền phù hợp; ghi image digest vào report.
- **Phù hợp khi / Không nên khi:** Phù hợp backend có dependency stateful. Không nên dùng làm sandbox chạy code không tin cậy (Ryuk mount Docker socket).
- **Rủi ro & điều kiện:** Cần Docker/OCI daemon, tài nguyên; DB ready chưa chứng minh migration và nghiệp vụ đúng. Rootless/remote daemon **(chưa xác minh)**.
- **Thay thế:** Docker Compose cho môi trường thử dài hơn ([32#anhkysuai-docker-compose](32-platform-delivery-engineering/README.md#anhkysuai-docker-compose), `docs-read`); json-server cho mock API nhanh ([30#anhkysuai-2026-11-23-typicode-json-server](30-software-testing-quality/README.md#anhkysuai-2026-11-23-typicode-json-server)).
- **Hồ sơ gốc:** [30-software-testing-quality/README.md#testcontainers-python-factory](30-software-testing-quality/README.md#testcontainers-python-factory) · `code-read` (`6146aa11`) · kiểm 2026-11-04

### 4.4 Schemathesis — Sinh request từ OpenAPI/GraphQL để tìm lỗi biên và chuỗi thao tác

- **Giải quyết:** Ca biên và chuỗi request khó viết tay; server trả 5xx hoặc response sai schema.
- **Cơ chế cốt lõi:** `checks.py` chạy registry check (vd. `not_a_server_error`, `max_response_time`), có hook/custom checks; OpenAPI checks tách conformance status/content-type/response-schema khỏi assertion nghiệp vụ tự viết. Hỗ trợ stateful sequences; README cảnh báo request thật có thể tạo/sửa/xóa dữ liệu.
- **Áp dụng vào dự án khác:**
  1. Chạy trên môi trường thử với tenant/dataset dùng-xong-bỏ, credential tối thiểu, giới hạn tốc độ.
  2. Bật các check mặc định + viết custom check cho quyền (principal A không đọc tài nguyên của B) và invariant tiền/trạng thái.
  3. Lưu reproducer của mỗi lỗi thành test regression.
  4. Đặt sau bước `oasdiff` (4.8): spec đúng trước, runtime khớp spec sau.
- **Phù hợp khi / Không nên khi:** Phù hợp API có schema và môi trường thử. Không nên chạy vào production hay dựa vào nó khi schema cho phép cả câu trả lời sai về tiền/quyền.
- **Rủi ro & điều kiện:** Schema sai/thiếu thì conformance vẫn qua; tính năng BOLA/độ phủ **(chưa xác minh)**.
- **Thay thế:** Bruno CLI chạy collection có assertion trong CI ([30#anhkysuai-usebruno-bruno](30-software-testing-quality/README.md#anhkysuai-usebruno-bruno), `docs-read`); test HTTP tự viết + Zod ở biên API ([30#anhkysuai-colinhacks-zod](30-software-testing-quality/README.md#anhkysuai-colinhacks-zod), `code-read`).
- **Hồ sơ gốc:** [30-software-testing-quality/README.md#schemathesis-factory](30-software-testing-quality/README.md#schemathesis-factory) · `code-read` (`8033ef46`) · kiểm 2026-11-04

### 4.5 Grafana k6 — Hồi quy latency/error dưới tải với threshold quyết định mã thoát

- **Giải quyết:** Không biết bản mới có làm chậm/lỗi dưới tải; script load "in checks failed" nhưng CI vẫn xanh.
- **Cơ chế cốt lõi:** `Check` trả boolean và phát metric `checks`; **check false không tự quyết định exit**. `run.go` tính threshold cuối lượt và gắn `ThresholdsHaveFailed` khi vượt ngưỡng — chỉ threshold làm CI đỏ.
- **Áp dụng vào dự án khác:**
  1. Khai báo workload: tốc độ đến/concurrency, tỷ lệ thao tác, payload, warmup, thời lượng.
  2. Đặt threshold trên `checks` (vd. tỷ lệ pass) **và** trên latency/error, lấy ngưỡng từ SLO đã được chủ sản phẩm chấp nhận.
  3. Báo p50/p95/p99 kèm số mẫu, lỗi, dropped iterations.
  4. Chạy theo lịch/trước release, không trên mọi PR; fixture: endpoint cố tình chậm phải làm job đỏ.
- **Phù hợp khi / Không nên khi:** Phù hợp dịch vụ có SLO latency. Không nên suy khả năng chịu tải production từ máy/tải khác, hoặc nhúng/phân phối k6 khi chưa xét AGPL.
- **Rủi ro & điều kiện:** AGPL-3.0; script không dùng được toàn bộ API Node; load generator cũng có giới hạn tài nguyên.
- **Thay thế:** Không có hồ sơ load-test `code-read` khác trong phạm vi; Lighthouse CI cho hiệu năng web front-end (đứng yên từ 6/2025, [13 §4c](13-dev-stack-devops/README.md#4c-thông-số-các-repo-trong-quality-gate-stack-đã-xác-minh-2026-10-12)).
- **Hồ sơ gốc:** [30-software-testing-quality/README.md#k6-factory](30-software-testing-quality/README.md#k6-factory) · `code-read` (`48d8dbbc`) · kiểm 2026-11-04

### 4.6 Playwright — Người chấm E2E tất định cho luồng người dùng quan trọng

- **Giải quyết:** Luồng đăng nhập/đặt hàng hỏng mà unit test không thấy; test UI dùng `sleep` gây flaky.
- **Cơ chế cốt lõi:** Actionability kiểm điều kiện trước thao tác; matcher như `toHaveURL` **retry theo điều kiện** thay vì sleep. `BrowserContext` có thể nạp lại storage state (IndexedDB phải bật khi snapshot). `click()` thành công không chứng minh entity đã tạo đúng.
- **Áp dụng vào dự án khác:**
  1. Chọn 3–5 critical journeys; mỗi test kết thúc bằng assertion hậu điều kiện **và** đọc lại entity qua API test/backend.
  2. Mỗi worker dùng tài khoản/dataset/tenant riêng; storage state coi như bí mật, cấp lại khi hết hạn.
  3. Thêm ca từ chối quyền (user B không thấy dữ liệu user A).
  4. Lưu trace/ảnh làm artifact; chạy ma trận trình duyệt theo nhu cầu sản phẩm.
- **Phù hợp khi / Không nên khi:** Phù hợp web app có luồng nghiệp vụ. Không nên dùng E2E thay unit/integration cho logic chi tiết.
- **Rủi ro & điều kiện:** Context riêng không xóa dữ liệu trên server; cookie/credential trong state có thể lộ. Kho chưa chạy matrix CI upstream.
- **Thay thế:** Storybook addon-vitest cho component + a11y (đặt `a11y.test=error` mới chặn, [06#storybook-addon-vitest-factory](06-ui-ux-design/README.md#storybook-addon-vitest-factory), `code-read`); Playwright CLI/MCP cho agent (mục 11, `unassessed`).
- **Hồ sơ gốc:** [11-browser-computer-use-sandbox/README.md#playwright](11-browser-computer-use-sandbox/README.md#playwright) · `code-read` (`820620c9`) · kiểm 2026-11-02

### 4.7 dependency-cruiser — Biến luật ranh giới module JS/TS thành cổng CI

- **Giải quyết:** Domain import UI/DB adapter, production import test, cycle — kiến trúc trôi dần khi nhiều người/agent cùng sửa.
- **Cơ chế cốt lõi:** CLI trả exit code từ reporter. **JSON reporter đặt `exitCode: 0`**; Error reporter (`err`) dùng `summary.advisedExitCode`. Nhiều rule khởi tạo là warning.
- **Áp dụng vào dự án khác:**
  1. Cài làm dev dependency ghim lockfile; viết 3–5 rule `error` thể hiện boundary thật (domain ↛ adapter, package chỉ qua public entry, cấm cycle).
  2. Gate dùng `--output-type err`; JSON/graph chỉ là artifact phụ.
  3. Thêm fixture import trái lớp phải đỏ, fixture hợp lệ phải xanh; kiểm alias/tsconfig và include/exclude.
  4. Nợ cũ ghi baseline có owner, không cho tăng âm thầm.
- **Phù hợp khi / Không nên khi:** Phù hợp monorepo/app JS/TS nhiều module. Không nên thêm chỉ để vẽ graph khi pipeline đã chặn đủ boundary; không phủ dependency động/runtime.
- **Rủi ro & điều kiện:** Chạy JSON reporter rồi thấy exit 0 không chứng minh không vi phạm; severity phải theo hợp đồng của đội.
- **Thay thế:** Structurizr cho mô hình C4 khai báo ([29#structurizr-model-code-boundary](29-software-architecture-api-contracts/README.md#structurizr-model-code-boundary), `code-read`); import-linter cho Python, ArchUnit cho Java (nêu trong hồ sơ, chưa có hồ sơ riêng).
- **Hồ sơ gốc:** [29-software-architecture-api-contracts/README.md#dependency-cruiser-architecture-gates](29-software-architecture-api-contracts/README.md#dependency-cruiser-architecture-gates) · `code-read` (`e6517db0`) · kiểm 2026-11-04

### 4.8 oasdiff — Chặn breaking change của OpenAPI trước khi phát hành

- **Giải quyết:** Thêm field request bắt buộc, xóa operation, đổi auth làm hỏng client/SDK/gateway dù server nội bộ vẫn trả 200.
- **Cơ chế cốt lõi:** `oasdiff breaking` mặc định **`--fail-on` rỗng** → chỉ in mà thoát 0; callsite severity/exit chỉ bật fail khi cấu hình. Tài liệu phân biệt hợp đồng với việc server chấp nhận dữ liệu rộng hơn.
- **Áp dụng vào dự án khác:**
  1. Lưu spec **của bản đã phát hành** (có version/hash) làm base, không so với file bị ghi đè trong cùng PR.
  2. Gate: `oasdiff breaking --fail-on ERR base.yaml revision.yaml` (chọn `WARN` nếu policy chặt hơn).
  3. Fixture: thêm required field / xóa operation / đổi security requirement phải làm job đỏ.
  4. Ignore/override severity là thay đổi policy cần review.
  5. Ghép lint quy ước (Spectral) và runtime test (4.4).
- **Phù hợp khi / Không nên khi:** Phù hợp API công bố cho client ngoài hoặc SDK. Không áp cho AsyncAPI/Protobuf/GraphQL (cần công cụ đúng định dạng).
- **Rủi ro & điều kiện:** Diff spec không gọi server, không biết authorization hay idempotency thực.
- **Thay thế:** Spectral (lint OpenAPI, [05-low-code-llm-platforms/README.md](05-low-code-llm-platforms/README.md), `unassessed`); Schemathesis (4.4) cho conformance runtime.
- **Hồ sơ gốc:** [29-software-architecture-api-contracts/README.md#oasdiff-compatibility-gates](29-software-architecture-api-contracts/README.md#oasdiff-compatibility-gates) · `code-read` (`aa8a46f6`) · kiểm 2026-11-04

### 4.9 Doorstop + ADR (MADR) — Truy vết yêu cầu → test, phát hiện khi yêu cầu gốc đổi

- **Giải quyết:** Không biết test nào cần xem lại khi yêu cầu thay đổi; quyết định kiến trúc chỉ nằm trong đầu người.
- **Cơ chế cốt lõi:** Doorstop lưu yêu cầu/test case dạng YAML có ID và link; `Item.cleared`/`reviewed` so **stamp** của parent/link với nội dung để biết review đã lỗi thời (suspect). `ItemValidator` bỏ qua item inactive; "unreviewed changes"/suspect chỉ là **warning** — CLI có `--error-all` để nâng thành lỗi. MADR v4 có mục **Confirmation** trỏ tới cách kiểm quyết định.
- **Áp dụng vào dự án khác:**
  1. Bắt đầu bằng requirement ID + acceptance examples trong Markdown; viết ADR theo MADR với Confirmation = tên job CI.
  2. Khi trace ảnh hưởng đáng kể (nhiều đội, kiểm toán), chuyển sang Doorstop; chạy `doorstop` với profile `--error-all` trong CI.
  3. Fixture: đổi nội dung parent mà không review downstream phải đỏ.
  4. Liên kết requirement → test run → artifact digest trong manifest phát hành (4.10).
- **Phù hợp khi / Không nên khi:** Phù hợp sản phẩm có yêu cầu truy vết/kiểm toán. Không nên dùng cho prototype nhỏ — Markdown + ADR đủ.
- **Rủi ro & điều kiện:** Stamp là dấu toàn vẹn nội dung, không là chữ ký người duyệt hay bằng chứng test đã chạy. LGPL-3.0-only khi nhúng/phân phối thư viện. Khả năng SSO/audit kiểu ALM **(chưa xác minh)**.
- **Thay thế:** MADR thuần (chuẩn mẫu, [09 §3c](09-engineering-checklists/README.md#3c-nâng-trần-2112026-chuẩn-cấp-dự-án-dạng-máy-đọc-được-slo-và-adr-yêu-cầu-người-dùng)); Structurizr cho view kiến trúc.
- **Hồ sơ gốc:** [29-software-architecture-api-contracts/README.md#doorstop-requirements-traceability](29-software-architecture-api-contracts/README.md#doorstop-requirements-traceability) · `code-read` (`f5f2bef0`) · kiểm 2026-11-04

### 4.10 Hợp đồng bằng chứng phát hành & ngoại lệ có hạn (thực hành, kèm OWASP SAMM) — Biến checklist tự khai thành bằng chứng gắn đúng bản phát hành

- **Giải quyết:** Checklist do agent đánh dấu đầy; báo cáo scanner cũ/sai target; ignore wildcard vĩnh viễn không ai chịu trách nhiệm.
- **Cơ chế cốt lõi:** Mỗi dòng kiểm gồm **control ID · owner · target/revision · lệnh/phương pháp · artifact URI + checksum · kết quả · hạn hiệu lực · reviewer · exception**; tách pass/fail/skipped/not-applicable/inconclusive. Manifest phát hành giữ source SHA, candidate digest, run ID, tool versions; "0 test" không là đạt. SAMM Core là model YAML 5 business functions/15 practices để đặt mục tiêu trưởng thành tổ chức — workflow của nó chỉ lint/sinh Markdown, **không chứng minh tổ chức đã làm**.
- **Áp dụng vào dự án khác:**
  1. Tạo file manifest (vd. `release-evidence.json`) do runner CI ghi, không do người/agent tự điền.
  2. Mỗi exception bắt buộc có owner, phạm vi, lý do, biện pháp bù và **ngày hết hạn**; job release đỏ khi exception hết hạn.
  3. Giữ một fixture lỗi đã biết cho mỗi cổng (sai digest, test không collect, truy cập khác tenant…).
  4. Ánh xạ control tới chuẩn: ASVS/WSTG cho ứng dụng, OSPS Baseline/SLSA cho repo & phát hành, SAMM cho tổ chức — không gộp thành một điểm.
  5. Sau incident, thêm một ca regression và cập nhật control liên quan.
- **Phù hợp khi / Không nên khi:** Phù hợp từ mức "production đội nhỏ" trở lên. Không nên dựng hệ thống quản trị nặng cho prototype — một bảng trong repo là đủ.
- **Rủi ro & điều kiện:** SAMM là CC BY-SA 4.0 (giữ attribution/ShareAlike khi chuyển thể). Đây là thiết kế quản trị; chưa công cụ nào trong kho tự chứng minh toàn quy trình.
- **Thay thế:** OSPS Baseline + `osps-baseline-action` ([09 §3c](09-engineering-checklists/README.md#3c-nâng-trần-2112026-chuẩn-cấp-dự-án-dạng-máy-đọc-được-slo-và-adr-yêu-cầu-người-dùng), `unassessed`); X-Templates G0–G8 ([23-own-repos-lessons/README.md#x-templates-factory-evidence](23-own-repos-lessons/README.md#x-templates-factory-evidence), `code-read`).
- **Hồ sơ gốc:** [09-engineering-checklists/README.md#checklist-factory-2026-11-04](09-engineering-checklists/README.md#checklist-factory-2026-11-04) · [09-engineering-checklists/README.md#owasp-samm-factory](09-engineering-checklists/README.md#owasp-samm-factory) · [FACTORY.md#6-hợp-đồng-bằng-chứng-phát-hành](FACTORY.md#6-hợp-đồng-bằng-chứng-phát-hành) · `code-read` (SAMM `bc2b5474`) + tổng hợp của kho · kiểm 2026-11-04

### 4.11 pre-commit (+ Renovate) — Cùng một bộ format/lint/secret-scan ở máy dev và CI, dependency tự cập nhật có kiểm soát

- **Giải quyết:** Lint/format chỉ chạy ở máy một vài người; dependency cũ tích tụ CVE.
- **Cơ chế cốt lõi:** pre-commit là framework hook git đa ngôn ngữ, **ghim phiên bản hook theo repo**; hook local bỏ qua được bằng `--no-verify` nên **phải chạy lại trong CI**. Renovate tự mở PR cập nhật cho >90 trình quản lý gói (AGPL-3.0). Hồ sơ khuyến nghị gom nhóm cập nhật và đặt độ trễ (cooldown) để tránh bản độc vừa phát hành.
- **Áp dụng vào dự án khác:**
  1. Tạo `.pre-commit-config.yaml` với formatter/linter của stack (Ruff hoặc Black cho Python; Biome hoặc Prettier cho JS/TS) + gitleaks, mọi `rev` ghim cụ thể.
  2. CI chạy `pre-commit run --all-files` trong job required duy nhất `quality-gate`.
  3. Bật Renovate (hoặc Dependabot) với nhóm theo hệ sinh thái, giới hạn số PR mở cùng lúc và độ trễ phát hành.
  4. PR cập nhật dependency phải qua cùng bộ test/SBOM scan như PR thường.
- **Phù hợp khi / Không nên khi:** Phù hợp mọi repo nhiều người/agent cùng sửa. Không nên coi hook local là cổng bảo vệ.
- **Rủi ro & điều kiện:** Hồ sơ là metadata/README (`unassessed`), chi tiết cấu hình Renovate **(chưa xác minh)**; Renovate self-host chịu AGPL. Đổi phiên bản formatter có thể tạo diff lớn — chuẩn hóa một lần riêng.
- **Thay thế:** Dependabot (ghi nhận trong [13 §4b](13-dev-stack-devops/README.md#4b-quality-gate-stack-quan-sát-trong-19-repo-của-chủ-kho-mục-23-2026-10-12)); Prettier `--check` trong CI ([30#anhkysuai-prettier-prettier](30-software-testing-quality/README.md#anhkysuai-prettier-prettier), `docs-read`).
- **Hồ sơ gốc:** [13-dev-stack-devops/README.md#4c-thông-số-các-repo-trong-quality-gate-stack-đã-xác-minh-2026-10-12](13-dev-stack-devops/README.md#4c-thông-số-các-repo-trong-quality-gate-stack-đã-xác-minh-2026-10-12) · `unassessed` (đọc metadata/README) · kiểm 2026-10-12

### 4.12 actionlint + zizmor — Lint đúng và lint an toàn cho chính file workflow CI

- **Giải quyết:** CI là bề mặt tấn công chính: template injection, `pull_request_target` nguy hiểm, `GITHUB_TOKEN` thừa quyền, Action không pin SHA (vụ Trivy/tj-actions trong hồ sơ).
- **Cơ chế cốt lõi:** actionlint kiểm kiểu biểu thức `${{ }}`, gọi shellcheck/pyflakes cho `run:`, cảnh báo input không tin cậy dùng thẳng trong script. zizmor (Rust) có 41 audit gồm `template-injection`, `dangerous-triggers`, `excessive-permissions`, `unpinned-uses`, `cache-poisoning`, chế độ offline/online, xuất SARIF.
- **Áp dụng vào dự án khác:**
  1. Thêm `actionlint` và `zizmor --format=sarif` vào job required `quality-gate` trên mọi PR.
  2. Đặt `permissions: {}` ở đầu workflow, mở quyền theo job.
  3. Pin mọi `uses:` theo full SHA; bỏ `pull_request_target` có checkout mã PR.
  4. Fixture: workflow có `${{ github.event.pull_request.title }}` trong `run:` phải bị báo.
- **Phù hợp khi / Không nên khi:** Phù hợp mọi repo dùng GitHub Actions. Không dùng được cho GitLab CI/Jenkins.
- **Rủi ro & điều kiện:** Audit online của zizmor cần `GH_TOKEN`; actionlint nhịp bảo trì chậm lại, một người bảo trì chính. Hồ sơ đọc README/docs, chưa chạy.
- **Thay thế:** step-security/harden-runner giám sát egress lúc chạy (bản free chỉ repo public, gửi telemetry); OpenSSF Scorecard chấm tổng thể ([12 §3d](12-ai-security-guardrails/README.md#3d-repo-bảo-mật-nổi-tiếng-đã-xác-minh-2026-10-12)).
- **Hồ sơ gốc:** [13-dev-stack-devops/README.md#6h-nâng-trần-2112026-chuẩn-slsa-lint-bảo-mật-github-actions-quét-lỗ-hổng-theo-sbom-và-giám-sát-runner-yêu-cầu-người-dùng](13-dev-stack-devops/README.md#6h-nâng-trần-2112026-chuẩn-slsa-lint-bảo-mật-github-actions-quét-lỗ-hổng-theo-sbom-và-giám-sát-runner-yêu-cầu-người-dùng) · `unassessed` (đọc LICENSE/README/danh sách audit) · kiểm 2026-11-02

### 4.13 Syft → Grype / OSV-Scanner (SBOM theo digest + quét lỗ hổng) — Biết artifact chứa gì và có CVE nào trước khi deploy

- **Giải quyết:** Không trả lời được "image đang chạy dùng thư viện nào, có bị CVE mới ảnh hưởng không".
- **Cơ chế cốt lõi:** Syft sinh SBOM; Grype quét image/filesystem/**SBOM của syft** (`grype sbom:./sbom.json`), xếp ưu tiên theo EPSS/KEV, lọc bằng OpenVEX. OSV-Scanner quét theo dữ liệu OSV.dev, chạy offline được. Mục 31 nhấn mạnh: SBOM phải **gắn đúng artifact digest**; CVE match, khả năng khai thác và chấp nhận rủi ro là ba quyết định khác nhau.
- **Áp dụng vào dự án khác:**
  1. Sau build, sinh SBOM cho **đúng image digest** sẽ promote, lưu kèm manifest (4.10).
  2. Chọn **một** scanner làm cổng chính (Grype hoặc OSV-Scanner) để tránh nhiễu; đặt ngưỡng severity, ưu tiên KEV.
  3. Exception có owner + hạn (VEX hoặc file ignore được review).
  4. Scanner timeout/không tải được DB = inconclusive, không phải pass.
  5. Fixture: đổi byte artifact sau khi tạo SBOM → digest mismatch phải đỏ.
- **Phù hợp khi / Không nên khi:** Phù hợp mọi sản phẩm phát hành container/package. Không nên coi có file SBOM là SBOM đầy đủ.
- **Rủi ro & điều kiện:** Ghim Action/binary scanner theo SHA + checksum (Trivy từng bị cài backdoor 3/2026 theo hồ sơ 12). Hồ sơ Syft/Grype/OSV ở mức `unassessed`.
- **Thay thế:** Trivy (một binary cho lỗ hổng/misconfig/secret, [12 §3d](12-ai-security-guardrails/README.md#3d-repo-bảo-mật-nổi-tiếng-đã-xác-minh-2026-10-12)); cosign để ký và verify issuer/subject/digest (cùng hồ sơ); in-toto khi cần ràng buộc nhiều bước ([31#factory-2026-11-04-in-toto](31-software-supply-chain-security/README.md#factory-2026-11-04-in-toto), `code-read` — lưu ý cần `DISALLOW *` và command alignment chỉ là warning).
- **Hồ sơ gốc:** [31-software-supply-chain-security/README.md#3-so-sánh-theo-quyết-định-cần-đưa-ra](31-software-supply-chain-security/README.md#3-so-sánh-theo-quyết-định-cần-đưa-ra) · [13 §6h](13-dev-stack-devops/README.md#6h-nâng-trần-2112026-chuẩn-slsa-lint-bảo-mật-github-actions-quét-lỗ-hổng-theo-sbom-và-giám-sát-runner-yêu-cầu-người-dùng) · tổng hợp của mục 31 + `unassessed` cho từng scanner · kiểm 2026-11-04 / 2026-11-02

### 4.14 OWASP Dependency-Track — Theo dõi lỗ hổng/policy liên tục cho mọi phiên bản đang chạy

- **Giải quyết:** Scan một lần lúc merge không phát hiện CVE công bố sau khi bản cũ đã deploy; nhiều sản phẩm/phiên bản cần một portfolio.
- **Cơ chế cốt lõi:** `BomResource` nhận SBOM và trả token theo dõi; `EventResource` đọc trạng thái xử lý; `CelPolicyEngine` đánh giá điều kiện policy, tạo policy violations. **Upload HTTP thành công ≠ phân tích thành công**: endpoint token cũ trả `processing=false` cả khi token không tồn tại.
- **Áp dụng vào dự án khác:**
  1. Upload CycloneDX cho đúng project/version/release digest.
  2. Adapter CI poll trạng thái tới terminal với timeout, rồi đọc policy violations để quyết định chặn.
  3. Fixture: token rác / job thất bại phải là inconclusive, không pass.
  4. Giữ inventory deployment để khi CVE mới ảnh hưởng bản cũ, truy ra owner và rebuild/rollback.
  5. Backup/restore DB của Dependency-Track; pin image digest, đọc tài liệu cutover v4→v5.
- **Phù hợp khi / Không nên khi:** Phù hợp khi có nhiều release/sản phẩm cần theo dõi. Không nên dựng cho một repo nhỏ — Grype/OSV theo lịch là đủ.
- **Rủi ro & điều kiện:** Là dịch vụ có state + phụ thuộc feed advisory ngoài; cần quyền API theo project và theo dõi tuổi feed.
- **Thay thế:** GUAC để truy vấn đồ thị ảnh hưởng (ingest ≠ trust decision, [31#factory-2026-11-04-guac](31-software-supply-chain-security/README.md#factory-2026-11-04-guac), `code-read`); Grype/OSV-Scanner theo lịch (4.13).
- **Hồ sơ gốc:** [31-software-supply-chain-security/README.md#factory-2026-11-04-owasp-dependency-track](31-software-supply-chain-security/README.md#factory-2026-11-04-owasp-dependency-track) · `code-read` (`2e3fd965`) · kiểm 2026-11-04

### 4.15 SOPS — Giữ file bí mật mã hóa trong git, giải mã bằng KMS/age/PGP

- **Giải quyết:** Secret nằm plaintext trong repo/CI hoặc phân tán khó review thay đổi.
- **Cơ chế cốt lõi:** Sửa tệp YAML/JSON/ENV/INI/binary đã mã hóa; README liệt kê backend KMS cloud, age và PGP; CI upstream build/test CLI theo OS/arch.
- **Áp dụng vào dự án khác:**
  1. Thử với tệp giả trước; định nghĩa policy recipient (ai/khóa nào giải mã được môi trường nào).
  2. Diễn tập **recovery và rotation khóa** trước khi đưa secret thật vào.
  3. Chỉ job deploy có quyền giải mã; PR từ fork không có quyền.
  4. Kiểm không có plaintext trong log, diff, artifact; vẫn chạy gitleaks (4.11).
- **Phù hợp khi / Không nên khi:** Phù hợp đội nhỏ muốn GitOps cho cấu hình có secret. Không nên coi mã hóa tệp thay quản trị khóa/KMS hay bảo vệ plaintext trong editor/CI.
- **Rủi ro & điều kiện:** Cơ chế cryptography và recovery khi mất khóa **(chưa xác minh)** — hồ sơ chỉ `docs-read`. MPL-2.0.
- **Thay thế:** age; git-crypt; Sealed Secrets (nêu trong hồ sơ, chưa có hồ sơ riêng).
- **Hồ sơ gốc:** [31-software-supply-chain-security/README.md#anhkysuai-getsops-sops](31-software-supply-chain-security/README.md#anhkysuai-getsops-sops) · `docs-read` (`9aa10f12`) · kiểm 2026-11-23

### 4.16 mise — Khóa phiên bản toolchain và một entrypoint task chung cho local/CI

- **Giải quyết:** "Máy tôi chạy được": Node/Python/linter khác phiên bản giữa dev, CI và agent.
- **Cơ chế cốt lõi:** `mise.toml` khai báo tools/tasks/env; `mise lock` ghi version + URL/checksum khi backend có; `mise install --locked` dùng dữ liệu lock (`ResolveOptions.use_locked_version`); `lock` có trust check và từ chối khóa version không xác minh được. **Lock tool không khóa package của app**; `exec`/hook/env/postinstall có thể chạy mã — trust là cho phép, không phải sandbox.
- **Áp dụng vào dự án khác:**
  1. Review `mise.toml` (tools + tasks `lint`/`test`/`build`) trước khi `mise trust`.
  2. Tạo lock cho mọi platform thật sự dùng (dev macOS, CI Linux…).
  3. CI: `mise install --locked` → cài dependency app bằng frozen lockfile (npm ci / `uv sync --frozen`) → chạy cùng task như local.
  4. Ghi tool versions + lock digest vào report; tách task cần secret khỏi PR không tin cậy.
  5. Fixture: thiếu platform trong lock phải fail rõ, không âm thầm lấy latest.
- **Phù hợp khi / Không nên khi:** Phù hợp repo đa ngôn ngữ, nhiều người/agent. Không nên khi cần khóa cả dependency hệ thống bit-for-bit (dùng Nix).
- **Rủi ro & điều kiện:** Lock thiếu digest ≠ tái lập byte-for-byte; cache hit không được bỏ qua xác minh input.
- **Thay thế:** Nix/devenv ([13 §6i](13-dev-stack-devops/README.md#6i-nâng-trần-toàn-diện-2112026-môi-trường-dev-build-và-release-tái-lập)); Dev Containers (`initializeCommand` chạy trên host, [32#factory-devcontainers-2026-11-04](32-platform-delivery-engineering/README.md#factory-devcontainers-2026-11-04), `docs-read`).
- **Hồ sơ gốc:** [13-dev-stack-devops/README.md#factory-2026-11-04-mise](13-dev-stack-devops/README.md#factory-2026-11-04-mise) · `code-read` (`02d59ef9`) · kiểm 2026-11-04

### 4.17 OpenTofu — Plan hạ tầng được review chính là plan được apply

- **Giải quyết:** Apply một plan khác với plan đã duyệt; CI nuốt lỗi hoặc coi "có thay đổi" là lỗi; secret rò qua state/plan.
- **Cơ chế cốt lõi:** Với `-detailed-exitcode`: **0 = không đổi, 1 = lỗi, 2 = có thay đổi**. Backend local kiểm lineage/serial của saved plan với state → báo stale khi lệch. Docs ghi state/plan có thể chứa password/private key dù terminal đã che.
- **Áp dụng vào dự án khác:**
  1. CI phân loại rõ 0/1/2 (không `set -e` mù, không `|| true`).
  2. Lưu saved plan làm artifact có quyền đọc hạn chế; review + policy/cost diff trên chính plan đó.
  3. Apply **đúng file plan đã duyệt**; không sinh plan mới sau approval.
  4. Bảo vệ state (encryption, retention, quyền); không đăng plan JSON lên comment PR public.
- **Phù hợp khi / Không nên khi:** Phù hợp hạ tầng cloud nhiều môi trường. Không nên chọn chỉ vì cú pháp quen; cấu hình cloud nhỏ có thể dùng công cụ native nếu giữ diff/review/audit.
- **Rủi ro & điều kiện:** Kiểm lineage không thay phân quyền review/apply; provider action không chắc quay lui được. MPL-2.0.
- **Thay thế:** Pulumi ([32#anhkysuai-pulumi-pulumi](32-platform-delivery-engineering/README.md#anhkysuai-pulumi-pulumi)); Terraform (đọc lại license phiên bản định dùng).
- **Hồ sơ gốc:** [32-platform-delivery-engineering/README.md#factory-opentofu-2026-11-04](32-platform-delivery-engineering/README.md#factory-opentofu-2026-11-04) · `code-read` (`c570669d`) · kiểm 2026-11-04

### 4.18 Argo CD — GitOps Kubernetes với đường phục hồi được viết đúng trạng thái controller

- **Giải quyết:** Runbook "bấm rollback" thất bại giữa sự cố; nhầm Synced/Healthy với "sản phẩm chạy đúng".
- **Cơ chế cốt lõi:** `Server.Rollback` kiểm quyền và **từ chối khi automated sync đang bật** (`rollback cannot be initiated when auto-sync is enabled`). Synced = live khớp desired theo cách so của Argo CD; Healthy = health assessment đã cấu hình, không thay smoke test hay restore dữ liệu.
- **Áp dụng vào dự án khác:**
  1. Chọn đường phục hồi chính: **revert commit desired state trong Git rồi sync**; ghi rõ vào runbook.
  2. Nếu dùng rollback trực tiếp, runbook có bước tắt auto-sync có kiểm soát.
  3. Sau sync chạy functional smoke + SLO gate (4.21), không dừng ở Healthy.
  4. Review prune/self-heal/ApplicationSet trên manifest thực; kiểm image cũ còn tương thích schema (4.23).
- **Phù hợp khi / Không nên khi:** Phù hợp đội đã dùng Kubernetes. Không nên thêm Kubernetes chỉ để dùng GitOps — hệ nhỏ dùng CI deploy có audit/rollback.
- **Rủi ro & điều kiện:** Quay image cũ không đảo migration đã chạy. Kho chưa dựng cluster.
- **Thay thế:** Flux (chưa đọc mã); Coolify/Dokku cho PaaS tự host nhỏ ([32#anhkysuai-coollabsio-coolify](36-self-hosting-homelab/README.md#anhkysuai-coollabsio-coolify), `docs-read`); Helm cho đóng gói chart ([32#anhkysuai-helm-helm](32-platform-delivery-engineering/README.md#anhkysuai-helm-helm)).
- **Hồ sơ gốc:** [32-platform-delivery-engineering/README.md#factory-argocd-2026-11-04](32-platform-delivery-engineering/README.md#factory-argocd-2026-11-04) · `code-read` (`211c2b4f`) · kiểm 2026-11-04

### 4.19 semantic-release / release-please — Version, changelog và tag sinh tự động từ commit, phát hành từ cổng đã qua test

- **Giải quyết:** Đánh version tay, changelog thiếu, token publish nằm trong job ai cũng chạy được.
- **Cơ chế cốt lõi:** semantic-release tách core/plugin/nhánh để quyết định kênh phân phối; cấu hình chia sẻ thống nhất nhiều repo. Commit convention sai có thể chọn sai SemVer. release-please: conventional commits → **release PR** + changelog + tag (dùng trong repo của chủ kho).
- **Áp dụng vào dự án khác:**
  1. Bật commitlint/conventional commits trước.
  2. Chạy `--dry-run` trên nhánh release rõ ràng, khóa phiên bản plugin.
  3. Job publish chỉ chạy sau `quality-gate` xanh, token publish chỉ cấp cho job đó (nhánh bảo vệ).
  4. Publish **cùng artifact digest** đã test; với binary Go dùng GoReleaser và kiểm checksum/cosign phía nhận.
- **Phù hợp khi / Không nên khi:** semantic-release hợp thư viện/package phát hành liên tục; release-please hợp đội muốn có PR review trước tag. Không nên khi version do quyết định kinh doanh.
- **Rủi ro & điều kiện:** Hồ sơ `docs-read`/`unassessed`; bảo vệ token publish. GoReleaser: file cấu hình upstream bật `pro: true`, chép nguyên không chạy với bản OSS.
- **Thay thế:** Changesets (nêu trong hồ sơ); GoReleaser ([13#goreleaser](13-dev-stack-devops/README.md#goreleaser)).
- **Hồ sơ gốc:** [32-platform-delivery-engineering/README.md#anhkysuai-semantic-release-semantic-release](32-platform-delivery-engineering/README.md#anhkysuai-semantic-release-semantic-release) · `docs-read` (`abd63c04`) · kiểm 2026-11-23; release-please tại [13 §4c](13-dev-stack-devops/README.md#4c-thông-số-các-repo-trong-quality-gate-stack-đã-xác-minh-2026-10-12) · `unassessed` · 2026-10-12

### 4.20 OpenTelemetry Collector (redaction processor) — Một điểm chặn PII/secret trước khi telemetry rời hệ thống

- **Giải quyết:** Log/trace/metric chứa PII, token, nội dung nghiệp vụ đi thẳng tới vendor; mỗi dịch vụ tự che theo kiểu riêng.
- **Cơ chế cốt lõi:** Redaction processor: allowlist loại key không được phép trước khi mask value; `ignored_keys`/patterns được giữ nguyên; `allowed_values` ưu tiên cho phép hơn mask. Factory gắn xử lý vào traces/logs/metrics **chỉ khi processor có trong pipeline**. Độ ổn định: traces beta, logs/metrics alpha.
- **Áp dụng vào dự án khác:**
  1. Dùng distribution chứa redaction processor, ghim version + config hash.
  2. Đặt processor **trước exporter** trong từng pipeline (traces/logs/metrics).
  3. Fixture canary: secret/PII dạng string/số/nested trong span/log body/resource attributes → kiểm ở **đích nhận thử**, không chỉ unit test regex.
  4. Không bật `allow_all_keys`/ignore rộng; quyết định rõ về `summary: debug` (có thể lộ tên key).
- **Phù hợp khi / Không nên khi:** Phù hợp nhiều dịch vụ cùng gửi telemetry. Không nên coi regex là bằng chứng đã ẩn danh mọi PII; giảm dữ liệu ngay tại SDK nếu được.
- **Rủi ro & điều kiện:** Exporter quyết định đích; chưa audit receiver/exporter/auth.
- **Thay thế:** Sentry cho lỗi ứng dụng (FSL, lọc dữ liệu + sampling, [33#anhkysuai-getsentry-sentry](33-reliability-observability-operations/README.md#anhkysuai-getsentry-sentry), `docs-read`); filter/transform processor của OTel.
- **Hồ sơ gốc:** [33-reliability-observability-operations/README.md#otel-collector-egress](33-reliability-observability-operations/README.md#otel-collector-egress) · `code-read` (`970f5977`) · kiểm 2026-11-04

### 4.21 Sloth (SLO as code) — Viết SLO một lần, sinh recording rule và cảnh báo burn-rate nhất quán

- **Giải quyết:** PromQL copy-paste lệch giữa dashboard và alert; không có error budget để quyết định dừng rollout.
- **Cơ chế cốt lõi:** `generate` sinh recording rules/metadata và **multiwindow multi-burn alerts**; `validate` gọi generator, kiểm spec và ID SLO trùng, trả lỗi khi fail (không chỉ parse YAML). Period mặc định `30d`; có flag tắt recording/alert/default plugins.
- **Áp dụng vào dự án khác:**
  1. Service owner định nghĩa SLI theo hành trình người dùng (numerator/denominator, window, exclusions).
  2. Lưu SLO source + phiên bản generator/plugin trong repo; CI `sloth validate` → `generate` → diff artifact.
  3. Rule fixtures: healthy, fast burn, slow burn, thiếu traffic, thiếu series; quy định dữ liệu thiếu là unknown, không phải 100%.
  4. Rollout rule rồi kiểm alert tới kênh thử có ack/auto-resolve.
  5. Nối error budget vào quyết định GO/NO-GO của release.
- **Phù hợp khi / Không nên khi:** Phù hợp đã có Prometheus. Không nên khi chỉ có 1–2 SLO (viết rule tay đủ); không chạy hai generator cho cùng SLO.
- **Rủi ro & điều kiện:** Generator hợp lệ vẫn có thể dùng sai denominator; plugin chạy trong CI phải review/pin. Objective 99.x trong ví dụ không phải SLA mẫu.
- **Thay thế:** Pyrra (UI + operator; reconcile ≠ rule đã evaluate, [33#pyrra-slo-operations](33-reliability-observability-operations/README.md#pyrra-slo-operations), `code-read`); OpenSLO làm định dạng trung lập ([09 §3c](09-engineering-checklists/README.md#3c-nâng-trần-2112026-chuẩn-cấp-dự-án-dạng-máy-đọc-được-slo-và-adr-yêu-cầu-người-dùng)).
- **Hồ sơ gốc:** [33-reliability-observability-operations/README.md#sloth-slo-generator](33-reliability-observability-operations/README.md#sloth-slo-generator) · `code-read` (`dfab41f3`) · kiểm 2026-11-04

### 4.22 restic (+ restore drill) — Backup mã hóa, kiểm toàn vẹn có phạm vi và chứng minh bằng phục hồi thật

- **Giải quyết:** "Có backup" nhưng chưa từng restore; RPO/RTO chỉ là con số trên giấy.
- **Cơ chế cốt lõi:** Snapshot mã hóa, dedupe, nhiều backend. `check` **mặc định không đọc toàn bộ payload** — phải `--read-data` hoặc `--read-data-subset`. `restore` có đích riêng và dry-run; mặc định ghi đè đích.
- **Áp dụng vào dự án khác:**
  1. Backup **export DB nhất quán** (công cụ của DB) + file/object; không backup file DB đang ghi.
  2. Lưu mật khẩu/credential phục hồi ở nơi ngoài máy cần cứu.
  3. Lịch `check --read-data-subset` luân phiên; ghi tỷ lệ dữ liệu đã đọc.
  4. Định kỳ restore vào **môi trường trống tách biệt**, mở ứng dụng, kiểm bản ghi/quyền/schema; ghi RPO/RTO thực đo.
- **Phù hợp khi / Không nên khi:** Phù hợp VPS/một máy, file và DB export. Không nên dùng thay PITR/snapshot native khi cần nhất quán giao dịch cao.
- **Rủi ro & điều kiện:** Ba tầng bằng chứng khác nhau: job thành công → integrity check → restore + nghiệm thu; chỉ tầng cuối cho RPO/RTO. BSD-2-Clause.
- **Thay thế:** Velero cho resource/PV Kubernetes (FSB beta, node agent cần root); backup/PITR native của nhà cung cấp DB.
- **Hồ sơ gốc:** [09-engineering-checklists/README.md#operations-recovery-cost-evidence](09-engineering-checklists/README.md#operations-recovery-cost-evidence) · `code-read` (restic `dd09b6bd`) · kiểm 2026-11-02

### 4.23 goose (migration expand/contract) — Migration SQL có version, chạy an toàn khi hai thế hệ app cùng sống

- **Giải quyết:** Migration chạy dở dang, nhiều replica cùng migrate, rollback app làm vỡ schema, `down` làm mất dữ liệu.
- **Cơ chế cốt lõi:** Đường SQL có transaction: mở tx → chạy lệnh → cập nhật bảng version → commit; nhánh `NO TRANSACTION` chạy ngoài tx. API `Provider` **chỉ khóa khi bật locker** (`WithSessionLocker`/`WithLocker`); mutex trong process không thay khóa giữa replica.
- **Áp dụng vào dự án khác:**
  1. Một runner migration duy nhất cho release (job riêng) hoặc bật session locker phù hợp DB; quyền DDL riêng + timeout.
  2. Migration immutable sau phát hành; theo **expand → deploy code chuyển tiếp → backfill có checkpoint → contract**.
  3. CI: fresh DB + upgrade từ phiên bản đang hỗ trợ + chạy app N và N−1 trên schema mới (dùng Testcontainers, 4.3).
  4. Fixture: migration không tương thích bản cũ phải làm cổng đỏ; test partial failure.
- **Phù hợp khi / Không nên khi:** Phù hợp service Go/SQL hoặc khi muốn migration SQL thuần. Không nên thêm nếu framework đang dùng đã có migration đủ tốt.
- **Rủi ro & điều kiện:** DDL transactional phụ thuộc DB; backfill/lock có thể gây dở dang. Khác coding agent `block/goose`.
- **Thay thế:** sqlc cho query typed (`compile`/`vet`/`diff` là ba cổng khác nhau; `verify` cần cloud, [34#sqlc](34-backend-data-identity-integration/README.md#sqlc), `code-read`); migration của framework (Laravel, [34#anhkysuai-2026-11-23-laravel-laravel](34-backend-data-identity-integration/README.md#anhkysuai-2026-11-23-laravel-laravel), `docs-read`).
- **Hồ sơ gốc:** [34-backend-data-identity-integration/README.md#goose-migrations](34-backend-data-identity-integration/README.md#goose-migrations) · `code-read` (`2d285d22`) · kiểm 2026-11-04

### 4.24 Keycloak (OIDC + PKCE) — Tách xác thực người dùng khỏi quyền trên tài nguyên

- **Giải quyết:** Tự viết login/SSO; nhầm "token hợp lệ" với "có quyền với bản ghi này của tenant này".
- **Cơ chế cốt lõi:** Authorization endpoint gọi kiểm redirect và PKCE; checker phân biệt client có/không **ép** phương thức PKCE; authorization-code grant kiểm verifier tương ứng — có hỗ trợ PKCE không có nghĩa mọi client đã ép S256. Production guide yêu cầu TLS, hostname/proxy, DB production; `start-dev` không dùng phát hành.
- **Áp dụng vào dự án khác:**
  1. Dùng thư viện OIDC chuẩn; ghim issuer/client/redirect/scopes; public client = Authorization Code + PKCE **S256 bắt buộc**.
  2. API verify signature, issuer, audience, expiry, scope.
  3. Tenant lấy từ principal đã xác minh, không từ header/body; quyền từng resource do app/policy engine kiểm.
  4. Test âm: thiếu PKCE, sai redirect, sai issuer/audience, token hết hạn, user tenant A truy cập tenant B, sau revoke.
  5. Lên kế hoạch HA/backup/upgrade cho IdP như một dịch vụ production.
- **Phù hợp khi / Không nên khi:** Phù hợp SaaS cần SSO/federation, lifecycle tài khoản. Không nên tự vận hành khi auth managed hoặc auth của nền tảng (Supabase) đã đủ.
- **Rủi ro & điều kiện:** Session/refresh/key rotation, account recovery, admin access cần policy/test riêng; realm không tạo isolation ở DB ứng dụng. Conformance suite trong CI là workflow dispatch — chưa chứng nhận.
- **Thay thế:** authentik ([34#anhkysuai-goauthentik-authentik](34-backend-data-identity-integration/README.md#anhkysuai-goauthentik-authentik), `docs-read`); OpenFGA cho quyền theo quan hệ (ghim model ID, `HIGHER_CONSISTENCY`, [12-ai-security-guardrails/README.md#openfga](12-ai-security-guardrails/README.md#openfga), `code-read`).
- **Hồ sơ gốc:** [34-backend-data-identity-integration/README.md#keycloak](34-backend-data-identity-integration/README.md#keycloak) · `code-read` (`2174fdf3`) · kiểm 2026-11-04

### 4.25 OpenFeature/flagd + GrowthBook — Rollout có kill switch, tách assignment, exposure và kết luận thí nghiệm

- **Giải quyết:** Bật tính năng cho tất cả cùng lúc; A/B test "thắng" do log sai mẫu (đếm người chưa thấy treatment), SRM, hoặc dừng sớm khi thấy xanh.
- **Cơ chế cốt lõi:** flagd `fractional.go`: nhánh implicit băm `[flagKey, targetingKey]` và **từ chối targetingKey thiếu/null/rỗng**; có đường explicit hashing input riêng. GrowthBook SDK có `trackingCallback`/`onFeatureUsage` và **trả sớm khi thiếu callback** → chọn biến thể và ghi exposure là hai việc phải kiểm riêng. Hồ sơ 28 yêu cầu A/A, SRM, power/MDE trước khi chạy.
- **Áp dụng vào dự án khác:**
  1. Đánh giá flag qua giao diện OpenFeature (provider thay được), ghim daemon/provider/schema/flag version.
  2. Mỗi flag có owner, **ngày hết hạn**, fallback khi mất nguồn và kill switch đã diễn tập.
  3. Fixture assignment: cùng subject qua client/server, trước/sau login, restart, đổi rule → kết quả nhất quán.
  4. Log exposure (kèm reason/error) khi người dùng thực sự thấy treatment; chạy A/A + kiểm SRM trước thí nghiệm thật.
  5. Đóng băng metric contract (numerator/denominator, window, đơn vị randomization, phương pháp dừng); báo effect size + khoảng bất định + guardrail.
- **Phù hợp khi / Không nên khi:** Flag hợp mọi sản phẩm có rollout dần; A/B chỉ khi đủ traffic. Không nên dùng flag làm cổng quyền truy cập dữ liệu; traffic thấp thì ưu tiên usability/cohort.
- **Rủi ro & điều kiện:** GrowthBook có thư mục enterprise license riêng; percentage rollout không tự là randomization đúng cấp account/team.
- **Thay thế:** Unleash (AGPL; custom strategy trả unknown trong playground, [28#unleash](28-product-discovery-experimentation/README.md#unleash), `code-read`); PostHog (analytics + flags + replay, ee proprietary, [28#posthog](28-product-discovery-experimentation/README.md#posthog), `code-read`).
- **Hồ sơ gốc:** [28-product-discovery-experimentation/README.md#flagd](28-product-discovery-experimentation/README.md#flagd) · `code-read` (`90255568`) · kiểm 2026-11-04 · [28-product-discovery-experimentation/README.md#growthbook](28-product-discovery-experimentation/README.md#growthbook) · `code-read` (`0553a68d`) · kiểm 2026-11-02

---

### Bộ khởi đầu tối thiểu cho repo mới

Thêm theo thứ tự; mỗi cổng phải có **một fixture cố tình sai làm nó đỏ** trước khi tính là "đã có".

1. **Toolchain + dependency khóa** — `mise.toml` + `mise lock` (4.16) và lockfile app cài ở chế độ frozen; CI và local gọi cùng task. *Fixture:* xóa platform khỏi lock → CI đỏ.
2. **Một job required `quality-gate`** — `pre-commit run --all-files` gồm formatter/linter của stack + gitleaks (4.11); nhánh chính chỉ merge khi job này xanh. *Fixture:* commit secret giả → đỏ.
3. **Test runner không chấp nhận "0 test"** — pytest coi exit 5 là lỗi / Vitest không `passWithNoTests`, kiểm số test đã chạy (4.1), cộng ít nhất một integration test với DB thật qua Testcontainers + migration thật (4.3, 4.23). *Fixture:* pattern test sai → đỏ.
4. **CI tự bảo vệ** — `permissions: {}`, pin Action theo SHA, `actionlint` + `zizmor` (4.12). *Fixture:* biểu thức `${{ github.event.* }}` trong `run:` → bị báo.
5. **SBOM + quét lỗ hổng theo digest** — Syft sinh SBOM cho artifact sẽ phát hành, một scanner chính (Grype hoặc OSV-Scanner) với ngưỡng severity và exception có hạn (4.13); Renovate/Dependabot mở PR vá (4.11). *Fixture:* scanner không tải được DB → inconclusive, không pass.
6. **Cổng hợp đồng** — nếu có API: `oasdiff breaking --fail-on ERR` so với spec đã phát hành (4.8); nếu JS/TS nhiều module: dependency-cruiser reporter `err` (4.7). *Fixture:* xóa một operation / import trái lớp → đỏ.
7. **Phát hành từ một artifact** — build một lần, promote theo digest, version/changelog bằng semantic-release hoặc release-please chỉ sau `quality-gate` (4.19); runner ghi manifest bằng chứng (SHA, digest, số test, kết quả scan, exception còn hạn) (4.10). *Fixture:* exception hết hạn → release đỏ.
8. **Vận hành tối thiểu trước khi có người dùng thật** — một SLO cho hành trình chính (4.21, có thể bắt đầu bằng rule viết tay) và một lần restore thật vào môi trường trống có ghi RPO/RTO đo được (4.22). *Fixture:* alert burn-rate thử phải tới đúng kênh và được ack.

Các item còn lại (Hypothesis, Schemathesis, k6, Playwright, Doorstop, Dependency-Track, SOPS, OpenTofu, Argo CD, OTel Collector, Keycloak, flagd/GrowthBook) thêm khi rủi ro hoặc quy mô sản phẩm đòi hỏi, theo mức "Thử nghiệm → Production đội nhỏ → Rủi ro cao" ở [FACTORY.md §4](FACTORY.md#4-ba-mức-áp-dụng-tránh-dựng-nền-quá-lớn).
