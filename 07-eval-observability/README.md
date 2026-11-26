# 07 · LLM Evaluation, Testing & Observability

| Công cụ | Repo | License | Vai trò | Ghi chú |
|---|---|---|---|---|
| **Langfuse** | langfuse/langfuse | MIT (core; `ee/` thương mại) | Tracing, prompt management, evals, metrics; self-host/cloud | Trụ cột observability mở |
| **Promptfoo** | promptfoo/promptfoo | MIT | Test prompt YAML, CLI cho CI, **red-teaming** | Gate ở PR |
| **DeepEval** | confident-ai/deepeval | Apache-2.0 (kiểm tra LICENSE) | Eval kiểu pytest: G-Eval, faithfulness, hallucination | v4.1.4 (7/2026) |
| **Ragas** | explodinggradients/ragas | Apache-2.0 | Metric cho RAG | Thường ghép Langfuse |
| **Arize Phoenix** | Arize-ai/phoenix | Elastic License 2.0 (source-available) | Tracing + eval | Không OSI |
| **OpenCompass / LightEval** | open-compass/opencompass · huggingface/lighteval | Apache-2.0 / MIT | Benchmark model | Học thuật; xem bảng bổ sung |
| **LangSmith / Braintrust** | – | Đóng | SaaS eval+trace | |

**Stack miễn phí gợi ý:** Promptfoo (CI gate) + Langfuse (trace production) + DeepEval/Ragas (chấm mẫu trace).

**Cho coding agent:** SWE-bench Pro, SWE-Touch, RoadmapBench (xem mục 01); theo dõi chi phí token & KV-cache hit rate (mục 03). **Benchmark agent tổng quát:** GAIA (trợ lý đa bước), Terminal-Bench 2 (tác vụ terminal), τ-bench / τ²-bench (tool + người dùng mô phỏng), Agent-as-a-Judge (agent chấm agent) — tên gom từ docs nội bộ X-Agents (mục 23); repo và phiên bản đã đối chiếu ở mục "Repo eval & observability nổi tiếng bổ sung" bên dưới (12/10/2026).

## Mẫu eval từ repo của chủ kho (mục 23, 2026-10-12)

- **Eval record/replay trong CI** (X-Agents `.github/workflows/eval-record.yml`): ghi lại hội thoại/tool-call thật thành fixture, CI replay không gọi model; chỉ "record" lại khi prompt đổi có chủ đích.
- **EDD (eval-driven development) với pass@k & pass^k** (`ecc-eval-harness`, vendor từ ECC trong xboss): pass@k = ít nhất 1/k lần đúng, pass^k = cả k lần đúng — agent production cần pass^k.
- **Santa Method** (`ecc-santa-method`): 2 reviewer độc lập cùng rubric, **cả hai phải pass**; **Council** (`ecc-council`): 4 giọng Architect/Skeptic/Pragmatist/Critic trước quyết định lớn.
- **Mutation test tự viết** (xboss `scripts/mutation-check.mjs`, ~150 dòng; qlkh dùng mutmut): cố ý phá bất biến, đòi test phải đỏ — kiểm "test có cắn không" mà không cần Stryker.
- **Negative control bắt buộc + claim matrix** (Hermes-Agents `ai-eval-evidence-integrity`): mỗi tuyên bố eval gắn nhãn `real-path` / `faithful-fixture` / `asserted-not-measured`; phải có ca cố ý sai để chứng minh eval phát hiện được.
- **`verified_by` do code điền** (X-Agents): kết quả "đã làm" của agent không phải bằng chứng; chỉ trường do code/CI điền mới tính.

## Repo eval & observability nổi tiếng bổ sung (đã xác minh 2026-10-12)

| Repo | ★ (12/10) | License | Hoạt động gần nhất | Vì sao chất lượng | Lưu ý |
|---|---|---|---|---|---|
| **UKGovernmentBEIS/inspect_ai** | 3,0k | MIT | bản 0.3.278 (9/10/2026) | Do UK AI Security Institute và Meridian Labs làm; sandbox, agent, hơn 200 eval dựng sẵn; METR bỏ Vivaria để chuyển sang Inspect, Lighteval chọn làm backend ưu tiên | Vẫn 0.x, phát hành gần như hằng ngày; dành cho eval nghiên cứu, không phải giám sát production |
| **EleutherAI/lm-evaluation-harness** | 14,2k | MIT | v0.4.13 (31/8/2026), commit 14/9 | Backend của HF Open LLM Leaderboard; NVIDIA, Cohere, BigCode, Nous Research dùng nội bộ | Không có eval agent; task logprob không chạy được với API chat đóng |
| **harbor-framework/harbor** (Terminal-Bench) | 6,0k | Apache-2.0 | 11/10/2026 | Harness chạy agent trong sandbox, runner chính thức của Terminal-Bench từ 2.0 (nhóm Stanford và Laude Institute); xuất rollout cho RL/SFT | Cần Docker hoặc container cloud; Terminal-Bench đổi phiên bản nhanh (2.0 → 4.0 trong 2026) |
| **sierra-research/tau2-bench** | 2,2k | MIT | 7/10/2026 | τ²/τ³-bench: tác vụ tool–agent–người dùng (airline, retail, telecom, banking, voice), dual-control (arXiv 2506.07982); Anthropic gọi là benchmark phổ biến cho năng lực agentic | Cần một LLM đóng vai người dùng (vd. gpt-4.1) nên tốn thêm phí API |
| **comet-ml/opik** | 22,5k | Apache-2.0 | 12/10/2026 | Tracing, LLM-judge, dashboard cho app LLM/RAG/agent; bản tự host có đủ tracing và eval | Bản tự host không có quản lý người dùng |
| **mlflow/mlflow** | 28,4k | Apache-2.0 | 3.17.0 (7/10/2026) | Dự án Linux Foundation; tracing OTel, LLM judge, quản lý prompt, gateway; auto-trace hơn 60 framework | Nền tảng MLOps rộng, nặng hơn công cụ trace chuyên dụng |
| **traceloop/openllmetry** | 7,5k | Apache-2.0 | 12/10/2026 | Instrumentation GenAI chuẩn OpenTelemetry, đổ dữ liệu về backend nào cũng được | ServiceNow mua Traceloop (3/2026); chỉ là lớp instrument, cần backend riêng |
| **lmnr-ai/lmnr** (Laminar) | 3,4k | Apache-2.0 | 11/10/2026 | YC S24; trace, eval, replay debugger, dashboard SQL; trace sẵn Claude Agent SDK, AI SDK, Browser Use | Startup trẻ, ít người đóng góp |
| **open-compass/opencompass** | 7,5k | Apache-2.0 | 12/10/2026 | Shanghai AI Lab; hơn 100 dataset cho LLM/VLM, chạy leaderboard CompassRank; gộp VLMEvalKit (8/2026) | Dùng để benchmark model, không trace app |
| **huggingface/lighteval** | 2,6k | MIT | 6/10/2026 | Hàng nghìn task trên vLLM/SGLang/TGI/LiteLLM, đẩy kết quả lên Hub | Trùng nhiều với Inspect và lm-evaluation-harness |

**Nhận xét:**

- Chọn theo mục đích: **chấm model** → lm-evaluation-harness, OpenCompass hoặc Lighteval; **chấm agent** → Inspect (đa năng), Terminal-Bench qua Harbor (tác vụ terminal), τ²-bench (tool + người dùng); **trace production** → Langfuse, Opik hoặc MLflow, hay OpenLLMetry nếu đã có backend OTel.
- Cập nhật đoạn benchmark ở đầu mục: Terminal-Bench đã tới 4.0 (8/2026) và chạy bằng Harbor (`laude-institute/terminal-bench` nay chuyển hướng sang `harbor-framework/terminal-bench-1`, tức bản TB1 đã bị thay); repo `tau-bench` gốc ghi không còn cập nhật task, tau2-bench giờ phát hành τ³-bench dưới tên repo cũ; GAIA không có repo GitHub chính thức, dữ liệu nằm trên Hugging Face.
- Đã loại: METR/vivaria và METR/task-standard (archive 7/10/2026 vì METR chuyển sang Inspect), stanford-crfm/helm (chế độ bảo trì từ 1/6/2026), openai/evals (19,6k★ nhưng commit năm 2026 chỉ là ghim dependency, lần cuối 14/4), AgentOps (5,9k★, commit cuối 25/6/2026), wandb/weave (1,1k★).

## Case study: Overmind — "trace production → model fine-tune riêng" (link người dùng, 2026-10-12)

> Đọc toàn bộ repo (clone đầy đủ, 82 commit), đối chiếu từng lời hứa trong README với code; nguồn ngoài do agent tra cứu cùng ngày.

### Hồ sơ nhanh

| Mục | Thông tin (12/10/2026) |
|---|---|
| Repo | `overmind-core/overmind` · **632★**, 60 fork; Trendshift ghi +543★ từ 13/8 đến 12/10 (đỉnh +101★ ngày 4/10) |
| Định vị | "The Training Platform for Specialized Agents": biến trace production thành dataset → eval → tối ưu prompt/code → fine-tune LoRA → phục vụ qua một API tương thích OpenAI |
| License | Platform (`overbae/`, `frontend/`) **AGPL-3.0**; SDK/CLI (`overmind/`) **MIT**; có license thương mại từ Overmind Ltd |
| Tác giả | Overmind Ltd (London): Tyler Edwards (CEO), Sam Brunt; seed £2M ngày 11/2/2026 do Osney Capital dẫn. Tháng 2/2026 còn tự gọi là "supervision layer for AI agents", nay đổi thành nền tảng huấn luyện |
| Lịch sử | Mở mã **15/9/2026** bằng một commit gộp ("Open source Overmind"); 82 commit, khoảng 11 người; release v0.1.3 (7/10/2026); PyPI `overmind` 0.1.85, khoảng 2,9k lượt tải/tháng |
| Quy mô | Backend Django `overbae/` ~110k dòng Python, frontend ~128k dòng TS, test ~72k dòng, SDK ~16k dòng |
| Giá hosted | Free (US$50 credit, 2 lần training/tháng), Pro US$120/tháng, Enterprise |
| Đón nhận | Không có bài HN về repo; vài bài X ngày ~7/10/2026 (@omarsar0, @rohanpaul_ai) nhắc lại số liệu của hãng; một blog review tích cực (themenonlab, 5/10) |
| Trùng tên dễ nhầm | `DarthSim/overmind` (3,8k★, quản lý process Procfile/tmux), `cerebral/overmind` (1,6k★, state management JS), **overmind.tech** — công ty London khác, seed US$6M (9/2025); vài trang tổng hợp gộp nhầm hai công ty |

### Cách hoạt động

1. `pip install overmind`, `overmind init --ide <cursor|claude|opencode|codex>`, `overmind sync`: quét repo thành **đồ thị capability** (prompt, tool, task).
2. SDK gắn OpenTelemetry vào các LLM SDK đang dùng (`providers="auto"`); `overmind.run(...)` đánh dấu một lượt chạy, `run.deliver()` là output được chấm điểm. Có connector kéo trace từ Langfuse, LangSmith, Braintrust, Galileo.
3. Trace được LLM judge chấm khi tới, gom thành dataset có version → eval theo từng capability → optimiser thử prompt/tool/control flow ngay trong repo, **bản thắng là một git diff** → fine-tune LoRA trên Modal → backtest model mới bằng chính trace cũ.
4. Coding agent điều khiển toàn bộ qua MCP server (`/api/mcp/`, 34 tool) và plugin 9 skill (`/overmind finetune`, `/overmind optimise`, `/overmind backtest`…).

### Đọc cổng thật (README → code)

| Lời hứa trong README | Code thật | Kết luận |
|---|---|---|
| "Every tool declares what it costs to run (free, compute, llm, gpu) and none can delete anything" | `overbae/services/mcp/catalog.py`: `cost_class` là trường bắt buộc kiểu `Literal`; `ToolDefinition` từ chối khi `destructive=True` hoặc tên chứa `delete/remove/cancel/retry/undeploy` (trừ `retry_deployment`); tool nào cũng phải khai scope OAuth | **Cổng thật**, chạy lúc dựng catalog. Nhưng chặn theo *tên* và *cờ do tác giả tự khai*, không theo hành vi: `set_active_model`, `configure_connector` vẫn ghi đè trạng thái. Không thấy `.delete()` nào trong `services/mcp/` |
| "Membership is checked on every operation" | `project_context()` lọc `accessible_projects(context)` theo `project_id` ở mỗi lời gọi | Đúng |
| "Keys are written to git-ignored files only" | `config.py` chạy `git ls-files --error-unmatch`, từ chối nếu file đã được track, rồi tự thêm đường dẫn vào `.git/info/exclude` | Đúng — **mẫu đáng chép** cho CLI nào phải ghi key xuống repo |
| "The API refuses to start until every required key is set" | `settings.py` ném `ImproperlyConfigured` nếu thiếu 1 trong 9 biến; `FINETUNING_BACKEND` chỉ nhận `modal` | Đúng |
| "Self-hosting keeps traces and training data inside your own network" | API không khởi động nếu thiếu `OPENROUTER_API_KEY` (judge, eval, **chấm trace**, Data Workshop), token Modal (train + serve), AWS S3 (checkpoint), `HF_TOKEN` | **Sai một phần**: trace nằm trong Postgres của bạn, nhưng nội dung trace đi qua OpenRouter để chấm, dữ liệu huấn luyện lên Modal, checkpoint lên S3 |
| Tự host: "Sign in … with any email and password" | `LocalSessionView` (`AllowAny`) tạo tài khoản ở lần đầu với `email_verified=True`, rồi `claim_pending_invites()` biến mọi lời mời trùng email thành membership ("an email match is proof of ownership") | Đúng như mô tả nhưng **nguy hiểm nếu mở ra mạng**: ai tới được cổng API có thể đăng ký trước bằng email đã được mời và vào thẳng dự án đó. Thêm nữa: `docker-compose.yml` publish 5432/6379/8000/5173/3001 trên mọi interface, mật khẩu Postgres mặc định `overbae`, `SECRET_KEY` có giá trị mặc định cứng trong `settings.py`. Bản hosted dùng Clerk và `local_session` tự từ chối khi Clerk bật |
| Telemetry "anonymous … one `cli.invoked` event per CLI run … never prompts, trace contents, keys or dataset contents" | `analytics.py`: khi có API key, gọi `/api/auth/me/` rồi gửi `$identify` với id người dùng, plan, `project_id`, gộp lịch sử ẩn danh vào tài khoản; mỗi lần chạy gửi `cli.invoked` **và** `cli.completed`, trong đó `command` là **cả dòng lệnh** — chỉ che chuỗi giống secret, **không che đường dẫn/tên file**; key PostHog viết cứng nên CLI trỏ vào bản tự host vẫn gửi về PostHog của Overmind | **Không ẩn danh** (gắn với tài khoản). Không gửi nội dung trace/dataset, đúng. Tắt bằng `DO_NOT_TRACK=1` |

**Hook cho coding agent đáng học** (`.agents/hooks/guards.py`, dùng chung cho Claude Code, Codex, Cursor): mỗi rule ghi lại sự cố đã sinh ra nó (`gh pr edit` báo thành công mà không làm gì, biome `--write` làm hỏng SVG, `makemigrations --merge` làm đỏ CI); chuỗi trong dấu nháy được xoá trước khi so khớp để lệnh `grep` cụm bị cấm không bị chặn nhầm; vì Codex vẫn chạy lệnh khi hook trả `ask`, có cờ `--deny-ask` hạ thành `deny`. Họ cũng cấm trailer `Co-authored-by` trong commit.

### Đánh giá & áp dụng

- **Điểm mạnh thật:** khép trọn vòng "trace → dataset → eval → tối ưu → fine-tune → backtest" mà các công cụ ở bảng trên chỉ làm từng đoạn (Langfuse/Opik: trace + eval; DSPy: tối ưu prompt; OpenPipe ART 10,8k★: RL cho agent). `cost_class` trên từng tool MCP và quy tắc "không có tool xoá" là thiết kế tốt cho việc để agent tự lái một nền tảng tốn tiền GPU.
- **Điểm yếu:** mới mở mã 4 tuần, vẫn 0.x; số liệu chất lượng (0,12% so với 3,36% trích dẫn bịa; ít "phantom clause" hơn 20–30 lần với Qwen3.5-9B) là số tự công bố **(chưa xác minh)**; tự host vẫn phụ thuộc OpenRouter + Modal + S3; platform AGPL.
- **Nếu dùng:** thử bản hosted với dữ liệu không nhạy cảm; nếu tự host thì chỉ chạy sau localhost/VPN, đổi `DJANGO_SECRET_KEY` và mật khẩu Postgres, bỏ publish cổng 5432/6379, không mời thành viên bằng email trên bản mở ra mạng, đặt `DO_NOT_TRACK=1` cho SDK/CLI.

## Nâng cấp 31/10/2026: rà repo lớn

> Hai việc. (1) Đọc lại số sao, license, ngày push của mọi repo mục 07 trong catalog bằng GitHub search API (31/10/2026); repo search trả "không tồn tại" thì tìm theo tên để phát hiện đổi chủ. (2) Tìm repo lớn còn thiếu bằng 8 truy vấn (topic `llmops`, `llm-evaluation`, `llm-observability`; từ khoá "llm evaluation", "llm observability", "agent tracing opentelemetry", "agent evaluation benchmark", repo eval tạo sau 1/10/2025). Chọn **6 repo**, clone `--filter=blob:none` đủ lịch sử, đọc LICENSE, cấu trúc, CI, file telemetry. **Không cài, không chạy script nào.**

### Repo cũ: điều đã đổi

| Repo | Thay đổi (12/10 → 31/10/2026) | Hệ quả |
|---|---|---|
| `explodinggradients/ragas` | **Đã chuyển sang `vibrantlabsai/ragas`** (16,2k★, Apache-2.0); **commit cuối 23/2/2026**, hơn 8 tháng không commit | "Stack miễn phí gợi ý" đầu mục nên dùng DeepEval làm chính, Ragas chỉ khi cần đúng metric RAG của nó; catalog đổi trường `repo` |
| `langfuse/langfuse` · `promptfoo/promptfoo` · `confident-ai/deepeval` · `Arize-ai/phoenix` | Bảng đầu chưa có số → **36,8k · 26,7k · 19,2k · 12,1k**, đều push 29–31/10 | Bổ sung số. Langfuse và Phoenix hiện `NOASSERTION` vì MIT + `ee/` và Elastic License 2.0, đúng như bảng |
| `harbor-framework/harbor` | 6,0k → **6,7k** (+11%) | Terminal-Bench tiếp tục kéo người dùng |
| `overmind-core/overmind` | 632 → **737** (+17%) | Case study bên trên vẫn đúng |
| `EleutherAI/lm-evaluation-harness` | 14,2k → 14,4k; **push cuối vẫn 14/9/2026** | Bảy tuần đứng yên; vẫn là chuẩn chấm model |
| `traceloop/openllmetry` | Push cuối 19/10/2026 | Bình thường sau thương vụ ServiceNow |
| `OpenPipe/ART` | Catalog để trống license → GitHub: **Apache-2.0** | Catalog bổ sung license |
| `ifixai-ai/iFixAi` | Catalog xếp mục 07 (41,4k★) nhưng README mục này không có hồ sơ; đánh giá nằm ở mục 08 (sao lệch so với lượt tải PyPI) | Giữ cảnh báo của mục 08 |
| Inspect, Opik, MLflow, Laminar, OpenCompass, Lighteval, tau2-bench | Dao động 1–8% | Không đổi nhận định |

### Bảng nhanh 6 repo mới

| Repo | Nhóm | ★ · license | Commit cuối | Một dòng | Cờ |
|---|---|---|---|---|---|
| `evidentlyai/evidently` | Eval + giám sát ML/LLM | 8,0k · Apache-2.0 | 11/9/2026 | 100+ metric, test, dashboard tự host cho dữ liệu, model và LLM | **Telemetry qua HTTP thường tới IP trần**; nhịp chậm |
| `Giskard-AI/giskard-oss` | Test + quét lỗ hổng agent | 5,9k · Apache-2.0 | 29/10/2026 | v3 viết lại: checks, scan, kịch bản nhiều lượt | v2 không còn bảo trì; cần Python 3.12+ |
| `langwatch/langwatch` | Trace + eval + gateway | 5,0k · Apache-2.0 (+ `enterprise/` riêng) | 31/10/2026 | Trace, simulation test agent, AI gateway, theo dõi coding agent | Nhịp commit cực cao, 12% có trailer Claude |
| `pydantic/logfire` | Observability (SDK) | 4,5k · MIT (SDK) | 30/10/2026 | SDK Python bọc OpenTelemetry, che secret mặc định | **Backend đóng mã** |
| `coze-dev/coze-loop` | Prompt + eval + trace | 5,8k · Apache-2.0 | 29/10/2026 | Bản mở của Coze Loop (ByteDance): playground prompt, bộ eval, trace | Mặc định dùng Volcengine Ark |
| `FailproofAI/failproofai` | Trace + chặn tool call cho harness | 7,1k · **MIT + Commons Clause** | 27/10/2026 | Hook 12 harness (Claude Code, Codex…), 40 policy dựng sẵn | Không phải OSI; telemetry bật sẵn |

### Hồ sơ từng repo

- **Evidently.** 2.798 commit từ 11/2020, 112 tác giả; chỉ 8 commit từ 1/5/2026 và 85 commit trong 12 tháng, bản v0.7.22 (10/9/2026) — **đang chậm lại rõ**. Phủ cả ML cổ điển (drift, data quality) lẫn LLM (descriptor, LLM judge, guardrail). Telemetry (`src/evidently/telemetry.py`, `ui/service/components/telemetry.py`) dùng `iterative_telemetry`, gửi tới **`http://35.232.253.5:8000`** (không TLS, địa chỉ IP trần), bật mặc định, tắt bằng `DO_NOT_TRACK`; README không nhắc tới telemetry ⚠️. Cài: `pip install evidently` và đặt `DO_NOT_TRACK=1`.
- **Giskard (v3).** 10.786 commit từ 3/2022, 131 tác giả. Viết lại thành 5 gói nhỏ (`giskard-checks`, `-scan`, `-agents`, `-llm`, `-core`); README ghi v2 "no longer actively maintained". Telemetry PostHog EU, key viết cứng; tắt bằng `DO_NOT_TRACK=1` hoặc `GISKARD_TELEMETRY_DISABLED=1`. README hứa "No prompts or outputs are sent": decorator trong `giskard-core` chỉ gửi tên loại exception ✅, nhưng hàm `telemetry_capture` chuyển nguyên `properties` của nơi gọi, chưa kiểm hết các nơi gọi **(chưa xác minh trọn)**. CI có `zizmor` (quét bảo mật GitHub Actions) và `.secrets.baseline`. Cài: `pip install "giskard[scan]"`.
- **LangWatch.** 7.308 commit từ 9/2023, 49 tác giả, 2.648 commit từ 1/5/2026; 12% commit có trailer Claude. Apache-2.0 cho lõi; `NOTICE` liệt kê `enterprise/` theo LangWatch Enterprise License, SDK và MCP là MIT. Ngoài trace/eval còn có **simulation test cho agent** (kể cả voice), AI gateway với virtual key và ngân sách, và mảng "AI governance" kéo dữ liệu từ Copilot Studio, compliance API của Anthropic/OpenAI. Lệnh `npx langwatch claude` gắn trace cho Claude Code; dữ liệu nào được gửi đi **chưa xác minh**. Tự host: `npx @langwatch/server` (cần Node 24). Lời "giúp quota tuần dùng lâu gấp đôi" là quảng cáo, không kiểm được.
- **Logfire.** 2.241 commit, 170 tác giả. README nói rõ: repo chỉ chứa SDK Python và docs, **"the server application… is closed source"**. Điểm đáng học: `logfire-sdk/logfire/_internal/scrubbing.py` **che giá trị nhạy cảm mặc định** theo mẫu `password`, `secret`, `auth`, `api key`, `session`, `cookie`… trước khi gửi span, có danh sách ngoại lệ cho id phiên agent và test riêng (`tests/test_secret_scrubbing.py`) ✅. Cài: `pip install logfire` rồi `logfire auth`. Chỉ dùng được với dịch vụ Pydantic hoặc bản tự host trả phí.
- **Coze Loop.** 417 commit từ 6/2025, 49 tác giả, Go + TypeScript; 13% commit có trailer Claude. Tag mới nhất v1.5.1 (20/1/2026) nhưng commit vẫn đều (sandbox eval trên Windows 29/10). Compose để mật khẩu MySQL/Redis/ClickHouse/OSS qua biến môi trường, không ghi cứng ✅; cấu hình model mẫu là Volcengine Ark. Bẫy đáng ghi: workflow `ai-cr-required.yaml` (bắt buộc bot "CozeLoop" review trước khi merge) đã **bị tắt lặng lẽ** bằng cách đổi nhánh kích hoạt thành `disabled-temporarily`; workflow vẫn nằm đó nên đọc lướt dễ tưởng cổng còn chạy.
- **FailproofAI.** 746 commit, tạo 6/4/2026 (Exosphere Host Inc), 18 tác giả, 38% commit có trailer Claude; tăng lên 7,1k★ trong ~7 tháng. LICENSE là **MIT + Commons Clause** (cấm bán dịch vụ dựa trên phần mềm), nên GitHub báo `NOASSERTION` và đây không phải mã nguồn mở theo OSI. Lời "40 built-in policies" khớp `src/hooks/policy-catalog.ts` (40 mục) ✅; "Runs locally" đúng cho phần chặn, nhưng **telemetry PostHog bật mặc định** (`lib/telemetry-enabled.ts`, key trong `src/posthog-key.ts`), tắt bằng `FAILPROOFAI_TELEMETRY_DISABLED=1`; README không nhắc tới ⚠️. Có `osv-scanner` trong CI và submodule `skills`. Cài: `npm install -g failproofai`. Liên quan mục 12 (guardrail) và mục 03 (hook).

### Mẫu chung rút ra

1. **Eval và observability đang gộp vào một nền tảng** có thêm gateway và chính sách (LangWatch, FailproofAI, Coze Loop); khi chọn, tách rõ phần cần (trace, eval, chặn) để khỏi kéo cả nền tảng.
2. **Telemetry của chính công cụ observability ít minh bạch:** Evidently gửi qua HTTP tới IP trần, FailproofAI và Evidently không nhắc trong README, Giskard và FailproofAI viết cứng key PostHog. Đặt `DO_NOT_TRACK=1` cùng biến riêng từng công cụ trong CI.
3. **Che secret ở phía SDK trước khi gửi** (Logfire) là mặc định nên có cho mọi lớp trace, kể cả tự viết.
4. **Cổng CI có thể chết mà không ai thấy** (Coze Loop đổi nhánh kích hoạt). Cần kiểm định kỳ rằng các check bắt buộc thật sự chạy trên nhánh chính.
5. **Repo đổi chủ/đứng yên lặng lẽ:** Ragas đổi tổ chức và dừng 8 tháng mà README không báo. Rà catalog bằng API định kỳ là cách duy nhất phát hiện.

**Nguồn (31/10/2026):** GitHub search API (`repo:` cho repo cũ; `ragas in:name`; 8 truy vấn topic/từ khoá) · clone nông vibrantlabsai/ragas (log 5 commit, README.md) · clone `--filter=blob:none`: evidently (LICENSE, README.md, `src/evidently/telemetry.py`, `src/evidently/ui/service/components/telemetry.py`, `git log`), giskard-oss (README.md, LICENSE, `libs/giskard-core/src/giskard/core/telemetry/telemetry.py`, workflows), langwatch (LICENSE.md, NOTICE, README.md, `enterprise/`), logfire (README.md, LICENSE, `logfire-sdk/logfire/_internal/scrubbing.py`, `tests/test_secret_scrubbing.py`), coze-loop (README.md, LICENSE, `.github/workflows/ai-cr-required.yaml`, `release/deployment/docker-compose/docker-compose.yml`), failproofai (LICENSE, README.md, .gitmodules, `lib/telemetry-enabled.ts`, `src/posthog-key.ts`, `src/hooks/{builtin-policies,policy-catalog}.ts`)

## Nâng trần 2/11/2026: chuẩn trace GenAI, kiểm tuân thủ trace bằng máy, bộ eval có version và chọn judge có số đo (yêu cầu người dùng)

> Cách làm: grep `data/projects.json` theo `repo` để loại trùng; GitHub search API (`repo:` gộp nhiều repo một truy vấn) lấy sao, license, ngày push 2/11/2026; clone `--depth 1 --filter=blob:none`, đọc LICENSE, README, spec/manifest, CI. **Không cài, không chạy.** Loại `prometheus-eval/prometheus-eval` (1,1k★, push cuối 25/4/2025) và `ScalerLab/JudgeBench` (133★, không có license, đứng từ 11/2024) vì đã dừng.

**Trần hiện tại:**

- Mục đã đủ công cụ trace/eval (Langfuse, Opik, MLflow, Phoenix, Promptfoo, DeepEval, Inspect) nhưng **chưa có chuẩn dữ liệu trace**: OpenLLMetry được nhắc là "chuẩn OTel" mà không chỉ tới bản đặc tả nào, ở trạng thái nào.
- Không có **cổng máy kiểm trace đúng chuẩn**: "đổi backend dễ" chỉ là tuyên bố cho tới khi có công cụ xác minh span thật.
- LLM-as-judge được dùng khắp nơi (Opik, Overmind, Evidently) nhưng **chưa có bước chọn judge bằng số đo**; mẫu "negative control" ở phần mẫu eval (mục 23) mới dừng ở quy ước.
- Bộ eval dựng sẵn (Inspect, lm-evaluation-harness) có nhắc, nhưng chưa có **quy ước version task** để kết quả hai lần chạy so được với nhau.

| Repo | Lớp | ★ · license (2/11/2026) | Commit cuối | Vì sao nâng trần | Rủi ro |
|---|---|---|---|---|---|
| `open-telemetry/semantic-conventions-genai` | Chuẩn | 506 · Apache-2.0 | 2/11/2026 | **Chuẩn GenAI của OTel đã tách khỏi repo semconv chính**: `docs/gen-ai/README.md` ở repo cũ ghi "Moved… no longer maintained". Repo mới gồm span client/agent/MCP/A2A, metric token, event, trang riêng cho Anthropic, OpenAI, Bedrock; model YAML quản bằng Weaver. Nội dung (`gen_ai.input.messages`, `gen_ai.output.messages`, `gen_ai.system_instructions`, `gen_ai.memory.records`) là **`Opt-In`**: "SHOULD NOT capture… by default" | Mọi thuộc tính vẫn **Development**, `README.md` để "Schema URL: TODO", CHANGELOG chưa có bản phát hành: tên thuộc tính còn đổi được. Link cũ trong bài tổng hợp trỏ vào trang đã ngừng cập nhật |
| `open-telemetry/weaver` | Cổng máy | 521 · Apache-2.0 | 1/11/2026 | `weaver registry live-check` nhận luồng OTLP và chấm mức tuân thủ so với registry; có GitHub Action `weaver-live-check-start/stop` đặt **ngưỡng severity làm CI fail**. Repo GenAI dùng nó để chạy `reference/`: 30 kịch bản (anthropic, openai, claude-agent-sdk, langchain, crewai, deepeval…) trên mock server tất định, sinh bảng ai hỗ trợ thuộc tính nào | Bản 0.x; live-check cần app phát trace thật trong CI |
| `Arize-ai/openinference` | Chuẩn (thứ hai) | 1,3k · Apache-2.0 | 2/11/2026 | Đặc tả trong `spec/` (LLM, embedding, tool calling, retrieval, annotation) và gói instrument cho khoảng 38 thư viện Python, 15 gói JS; là định dạng gốc của Phoenix (bảng đầu mục). `spec/configuration.md` định nghĩa biến `OPENINFERENCE_HIDE_INPUTS/OUTPUTS/…` để che nội dung | **Mặc định ghi nội dung** (mọi biến HIDE mặc định `False`), ngược với Opt-In của OTel GenAI. Gói `openinference-genai` chỉ chuyển "best effort" một phần thuộc tính OTel GenAI, README tự ghi theo định nghĩa 10/2025 |
| `openlit/openlit` | Đầu bảng (OTel-native) | 2,9k · Apache-2.0 | 22/10/2026 | SDK + nền tảng tự host phát thẳng `gen_ai.*` của OTel, đổ về Collector hay backend OTel bất kỳ; thêm eval, guardrail, giá, GPU collector, trace coding agent | `openlit.init(capture_message_content=True)` **ghi nội dung mặc định**, trái khuyến nghị Opt-In; `docker-compose.yml` đặt `TELEMETRY_ENABLED: "true"`, client có PostHog (`src/client/src/constants/posthog.ts`) |
| `UKGovernmentBEIS/inspect_evals` | Cổng máy (bộ eval) | 732 · MIT | 2/11/2026 | Hơn 200 task cho Inspect (đã có ở bảng bổ sung). Đáng chép: `TASK_VERSIONING.md` buộc mỗi task có version `N-X` (N tăng khi kết quả **không còn so được**, X khi đổi giao diện); `EVALUATION_CHECKLIST.md` đòi `VALIDITY_REPORT.md` (tên, dữ liệu, cách chấm có hợp lệ) và phân tích trajectory trước khi nhận eval | README: nay do **Generality Labs** (nonprofit London) bảo trì, chỉ nhận PR từ người được duyệt trước; thêm eval mới chuyển sang "Inspect Evals Register" từ 5/2026 |
| `allenai/reward-bench` | Cổng máy (chọn judge) | 748 · Apache-2.0 | 14/10/2026 | RewardBench 2 (arXiv 2506.01937): chấm reward model **và judge sinh văn bản** (`pip install rewardbench[generative]`, `scripts/run_generative_v2.py`, chế độ xếp hạng 4 câu hoặc chấm điểm từng câu). Dùng để chọn model judge bằng độ chính xác đo được thay vì theo cảm tính | Đo năng lực judge chung (factuality, focus, math, safety, ties), không thay việc hiệu chỉnh judge trên nhãn người của chính dự án |

**Stack nâng trần** (lợi ích/công sức giảm dần):

1. **Ghim chuẩn trace:** instrument theo `gen_ai.*` của semantic-conventions-genai (qua OpenLLMetry, OpenLIT hoặc SDK của backend), ghi rõ commit đặc tả đang theo vì vẫn ở Development. Nội dung prompt/output **tắt mặc định**; nếu dùng OpenInference hay OpenLIT thì đặt `OPENINFERENCE_HIDE_INPUTS/OUTPUTS=true` hoặc `capture_message_content=False`, rồi che secret như Logfire (§ Nâng cấp 31/10).
2. **Cổng tuân thủ trace trong CI:** chạy test tích hợp với mock model tất định, bật `weaver registry live-check` (Action start/stop, fail theo severity). Đây là bằng chứng máy cho lời "đổi backend Langfuse ↔ Phoenix ↔ MLflow được".
3. **Eval tất định trước, judge sau:** assertion tất định của Promptfoo/DeepEval (khớp schema, regex, tool call đúng tên/tham số) chạy ở mọi PR; LLM-judge chỉ cho tiêu chí mềm, kèm record/replay và negative control (phần mẫu eval mục 23).
4. **Hiệu chỉnh judge:** chọn model judge theo RewardBench 2; rồi gán nhãn người cho 50–200 mẫu của chính dự án, đo mức đồng thuận judge–người (vd. Cohen's kappa) và chỉ cho judge làm cổng khi đạt ngưỡng; lặp lại khi đổi model judge hay prompt chấm. Cỡ mẫu và ngưỡng là đề xuất của kho **(chưa xác minh bằng nguồn chuẩn)**.
5. **Version task eval:** áp quy ước `N-X` của inspect_evals cho bộ eval nội bộ; chỉ so điểm giữa các lần chạy có cùng `N`.

**Nguồn §Nâng trần 2/11/2026:** GitHub search API 2/11/2026 (`repo:` gộp) · `data/projects.json` (grep `repo`) · clone `--depth 1 --filter=blob:none`: open-telemetry/semantic-conventions (HEAD fb30ca1, 1/11/2026; `docs/gen-ai/README.md`), open-telemetry/semantic-conventions-genai (HEAD 16f3130, 2/11/2026; README.md, CHANGELOG.md, versions.env, `docs/gen-ai/{gen-ai-spans,gen-ai-agent-spans,mcp}.md`, `reference/README.md`, `reference/scenarios/`), open-telemetry/weaver (HEAD 8ed44ad, 1/11/2026; README.md, `docs/usage.md`), Arize-ai/openinference (HEAD 5c68f3a, 1/11/2026; LICENSE, README.md, `spec/configuration.md`, `python/instrumentation/`, `js/packages/openinference-genai/README.md`), openlit/openlit (HEAD 1ed8bb7, 22/10/2026; LICENSE, README.md, docker-compose.yml, `sdk/python/src/openlit/__init__.py`), UKGovernmentBEIS/inspect_evals (HEAD ca99b73, 2/11/2026; LICENSE, README.md, EVALUATION_CHECKLIST.md, TASK_VERSIONING.md, `.github/workflows/`), allenai/reward-bench (HEAD 59f6ff7, 14/10/2026; LICENSE, README.md, `scripts/`), prometheus-eval/prometheus-eval (HEAD dcfb442, 24/4/2025; loại) · https://github.com/open-telemetry/semantic-conventions-genai · https://github.com/open-telemetry/weaver · https://github.com/Arize-ai/openinference · https://github.com/openlit/openlit · https://github.com/UKGovernmentBEIS/inspect_evals · https://github.com/allenai/reward-bench · https://arxiv.org/abs/2506.01937

<a id="core-eval-validity"></a>

## Nâng trần 2/11/2026: đơn vị đo, lặp độc lập và hiệu lực của kết luận (mở rộng cùng ngày)

> Mở rộng chiều sâu trong cùng đợt 2/11/2026, không phải công bố các repo vừa ra mắt. Hai repo dưới đã có trong catalog: đọc lại LICENSE, CI và nhánh mặc định bằng clone chỉ đọc; SHA đối chiếu GitHub API. Mức bằng chứng **code-read**; không chạy/build repo ngoài, hiệu năng và hành vi thực tế **(chưa xác minh)**. Số sao/trạng thái đọc 2026-11-02; ngày commit tính theo UTC, tách khỏi `pushed_at`.

| Repo đã có | ★ · license (2026-11-02) | HEAD nhánh mặc định | Vai trò đọc sâu |
|---|---|---|---|
| `UKGovernmentBEIS/inspect_ai` | 3.153 · MIT | 2026-11-01 · `1f1a0039` | Epoch. cache và uncertainty theo đúng đơn vị mẫu |
| `promptfoo/promptfoo` | 26.736 · MIT | 2026-11-02 · `bfb96e2e` | Cache namespace cho repeat. assertion và hồi quy CI |

**Trần còn thiếu:** phần nâng trần trước đã có task version, judge calibration và trace conformance. Bước tiếp theo là chống kết luận sai từ **điểm trung bình, lần gọi đã cache, nhiều câu cùng hội thoại** hoặc chọn prompt bằng chính tập test.

### Inspect AI: số dòng kết quả không bằng số mẫu độc lập

- [`CachePolicy.per_epoch=True`](https://github.com/UKGovernmentBEIS/inspect_ai/blob/1f1a0039d49c628a41898a7a7ba4843c5bbbc91b/src/inspect_ai/model/_cache.py#L109) tách cache theo epoch; epoch là thành phần cache key khi policy này bật. Nếu chủ ý bỏ epoch khỏi cache, phải ghi rõ: không được diễn giải việc dùng lại cùng output là nhiều lần sinh độc lập.
- [`std.py`](https://github.com/UKGovernmentBEIS/inspect_ai/blob/1f1a0039d49c628a41898a7a7ba4843c5bbbc91b/src/inspect_ai/scorer/_metrics/std.py) có `stderr`, bootstrap, `ci` kiểu t/bootstrap và clustering theo metadata. Khi nhiều câu thuộc một tài liệu/hội thoại/user, cluster theo đơn vị đó thay vì giả định mỗi dòng độc lập. Với quá ít cluster, khoảng ước lượng không đủ để xếp hạng đáng tin; ghi số cluster và kiểm phân phối.
- Task/epoch reduction thay đổi mẫu mà metric nhận; phải ghi rõ đo theo **attempt, sample hay episode**, cách gộp epoch và cách xử lý unscored/error. CI kiểm framework không kiểm tính đúng đắn khoa học của một scorer tự viết. Mức tăng 1–2 điểm cần khoảng bất định và phân tích lỗi, không tự gán ý nghĩa thống kê.

### Promptfoo: repeat có namespace, nhưng chạy lại vẫn có thể dùng cache

- [`getRepeatCacheNamespace`](https://github.com/promptfoo/promptfoo/blob/bfb96e2ee2304ec87a7a32054a4907ea39f5c920/src/evaluator.ts#L474) tách `repeat:N`; [test repeat cache](https://github.com/promptfoo/promptfoo/blob/bfb96e2ee2304ec87a7a32054a4907ea39f5c920/test/evaluator/repeatCache.test.ts) chứng minh hai repeat được phân biệt nhưng **lần eval tiếp theo vẫn lấy lại output đã cache**. Đây là tính năng tái lập, không phải bug. Khi cần đo biến thiên mới, dùng `--no-cache` và kiểm provider/custom wrapper có thực sự gọi mới.
- Tách assertion tất định (schema/tool/regex/ground truth) khỏi judge. Giữ cùng input và cấu hình khi so baseline/candidate; lần chạy dùng cache là cổng hồi quy, lần sinh mới là thí nghiệm độ ổn định. Ghi model ID, seed/temperature nếu hỗ trợ, cache policy, repeat, lỗi và giá.
- [`telemetry.ts`](https://github.com/promptfoo/promptfoo/blob/bfb96e2ee2304ec87a7a32054a4907ea39f5c920/src/telemetry.ts#L22) có đường tắt `PROMPTFOO_DISABLE_TELEMETRY=1`; tắt telemetry không tự tắt provider call/remote grader. [CI](https://github.com/promptfoo/promptfoo/blob/bfb96e2ee2304ec87a7a32054a4907ea39f5c920/.github/workflows/main.yml) gồm ma trận Node/OS và test evaluator; chưa chạy các job đó trong đợt đọc này.

**Ma trận thiết kế phép đo**

| Câu hỏi | Đơn vị và cổng nên dùng | Sai lệch cần kiểm |
|---|---|---|
| Prompt mới có làm hỏng ca cũ? | Tập regression cố định + assertion; cache cho replay | Grader/model/version thay mà baseline giữ nguyên |
| Model có ổn định khi sinh mới? | Repeat/epoch tách cache; báo phân phối | Tính cùng output cache như lần thử độc lập |
| Tốt hơn trên dữ liệu thật? | Holdout theo user/tài liệu/thời gian; so cặp cùng mẫu | Train–test leakage, nhiều câu cùng episode |
| Judge có đáng tin? | Nhãn người, negative control, đo đồng thuận | Judge cùng model hoặc thấy tên phương án |
| Tăng chất lượng có đáng chi phí? | Chất lượng kèm token/$/p95 và lỗi | Chỉ báo điểm của những run thành công |

**Cách ghép:** (1) khoá dataset/task/scorer/model version và đơn vị mẫu; (2) tách development/validation/final test, chia theo nguồn để giảm rò rỉ; (3) chạy baseline/candidate trên cùng mẫu, assertion trước judge; (4) một run replay cho CI và một run sinh mới khi cần đo độ ổn định; (5) báo điểm, uncertainty/cluster, error/unscored, chi phí và nhóm ca thua. Không diễn giải hai CI giao nhau/không giao nhau như một phép kiểm so sánh cặp đầy đủ; muốn kết luận khác biệt cần phương pháp phù hợp và cỡ mẫu đã xác định. Đây là thiết kế đề xuất, chưa có số benchmark mới trong kho.

**Nguồn phần mở rộng:** [1](https://github.com/UKGovernmentBEIS/inspect_ai/blob/1f1a0039d49c628a41898a7a7ba4843c5bbbc91b/LICENSE) · [2](https://github.com/UKGovernmentBEIS/inspect_ai/blob/1f1a0039d49c628a41898a7a7ba4843c5bbbc91b/src/inspect_ai/model/_cache.py) · [3](https://github.com/UKGovernmentBEIS/inspect_ai/blob/1f1a0039d49c628a41898a7a7ba4843c5bbbc91b/src/inspect_ai/scorer/_metrics/std.py) · [4](https://github.com/UKGovernmentBEIS/inspect_ai/blob/1f1a0039d49c628a41898a7a7ba4843c5bbbc91b/src/inspect_ai/scorer/_metrics/aggregate.py) · [5](https://github.com/UKGovernmentBEIS/inspect_ai/blob/1f1a0039d49c628a41898a7a7ba4843c5bbbc91b/.github/workflows/pr-gate.yml) · [6](https://github.com/promptfoo/promptfoo/blob/bfb96e2ee2304ec87a7a32054a4907ea39f5c920/LICENSE) · [7](https://github.com/promptfoo/promptfoo/blob/bfb96e2ee2304ec87a7a32054a4907ea39f5c920/src/evaluator.ts) · [8](https://github.com/promptfoo/promptfoo/blob/bfb96e2ee2304ec87a7a32054a4907ea39f5c920/test/evaluator/repeatCache.test.ts) · [9](https://github.com/promptfoo/promptfoo/blob/bfb96e2ee2304ec87a7a32054a4907ea39f5c920/src/telemetry.ts) · [10](https://github.com/promptfoo/promptfoo/blob/bfb96e2ee2304ec87a7a32054a4907ea39f5c920/.github/workflows/main.yml) · [11](https://inspect.aisi.org.uk/metrics.html) · [12](https://inspect.aisi.org.uk/caching.html) · [13](https://www.promptfoo.dev/docs/usage/command-line/)

## Nâng trần 4/11/2026: eval là điều kiện nhận hàng của tính năng AI

<a id="eval-factory-2026-11-04"></a>

**Trần hiện tại:** hai phần 2/11 đã phủ trace, bộ eval, judge và thống kê. Xưởng cần nối những phép đo đó với **ID yêu cầu, bản dữ liệu, bản model/prompt/tool và quyết định phát hành**. Trace giúp giải thích một lần chạy; điểm benchmark công khai không thay bộ ca nghiệm thu của khách hàng. Đợt này đọc code/LICENSE/CI; chưa gọi model, gửi trace hay chạy eval upstream.

### Thêm OpenEvals: chọn scorer theo điều có thể chứng minh

<a id="openevals-factory"></a>

**langchain-ai/openevals**, do LangChain duy trì, MIT; SHA **5753dc75d40c2be75ffd38eb6d63bb966cbcc4e3** (HEAD ngày 2026-11-01, đọc 2026-11-04). Thư viện scorer Python/JS có exact match, structured-output và LLM-as-judge; README dẫn agentevals cho trajectory (đã có mục 03). Điểm hữu ích là ghép scorer nhỏ vào harness hiện có; không cần thay toàn bộ hệ eval để dùng một phép so tất định.

Đọc **exact.py**: so JSON sau khi sắp key, từ chối khi thiếu outputs/reference_outputs; không phải phép so ngữ nghĩa và vẫn cần đầu vào JSON-serializable. Đọc **llm.py**: judge tạo prompt và schema output cho điểm; điểm có cấu trúc không chứng minh judge đúng. Đọc **utils.py**: scorer bọc traceable của LangSmith; dữ liệu có rời máy hay không phụ thuộc cấu hình tracing và client, cần kiểm ở repo tích hợp. CI integration bật tracing và dùng credential provider; không gọi các ca đó là kiểm offline không tốn phí.

**Giới hạn quan trọng với code sinh:** evaluator E2B ghi outputs.py, suy import để cài dependency và chạy lệnh; kết quả execution_succeeded phản ánh tiến trình chạy thành công, **chưa chứng minh đáp ứng yêu cầu nghiệp vụ**. Với code của xưởng, phải chạy bộ test độc lập trong môi trường hạn quyền, không đưa credential production vào sandbox. Đánh giá bởi model chỉ là một tín hiệu bổ sung cho test thật ở mục 30.

| Câu hỏi | Công cụ/cơ chế phù hợp | Điều không được suy ra |
|---|---|---|
| JSON đúng cấu trúc, số tiền/ID đúng tuyệt đối? | Schema + exact match/OpenEvals; assertion tự viết | JSON hợp lệ chưa là dữ liệu đúng; chuẩn hóa timezone/số thực phải có quy tắc trước |
| Agent gọi đúng tool và tham số? | agentevals mục 03, ghi trajectory và trạng thái cuối | Giống đường đi mẫu không chứng minh side effect an toàn hoặc mục tiêu đã hoàn thành |
| Chất lượng câu trả lời và căn cứ? | Promptfoo/Inspect/Ragas/DeepEval đã có, OpenEvals judge được hiệu chuẩn | Không gộp các thang khác nhau thành một điểm chung; không dùng cùng model sinh để tự chứng nhận |
| Code sinh sửa được lỗi? | Runner/test độc lập ở mục 30, test hồi quy thất bại trước bản sửa | Chạy được, typecheck xanh hoặc judge khen chưa là task success |

### Cổng phát hành và vận hành của xưởng

1. **Bộ nghiệm thu có chủ:** lưu ID yêu cầu, input/reference, lý do chọn ca, quyền dữ liệu và nhóm critical; tách tập phát triển khỏi holdout. Khử dữ liệu khách hàng trước khi gửi provider/judge.
2. **Ghim mọi thành phần:** dataset SHA, prompt/model/tool/schema revision, cấu hình cache/repeat, judge/rubric và ngân sách; giữ raw outcome theo ca, timeout/refusal/skipped riêng.
3. **Hard gate trước judge:** schema, invariant, quyền, tác vụ không side effect ngoài phạm vi và ngân sách. Một lỗi critical đã định trước có thể chặn release dù điểm trung bình tăng; chính sách đó phải có người sở hữu.
4. **So cặp trên cùng ca:** bản ứng viên so bản đang dùng, phân tích nhóm tiếng Việt, câu hỏi thiếu căn cứ và ca từ chối; báo độ bất định và chi phí/latency cùng chất lượng. Giữ ca thua thay vì chỉ công bố tổng điểm.
5. **Replay và rollback:** trace đã khử dữ liệu → fixture được review → regression ở PR; triển khai giới hạn traffic, giữ khả năng quay về prompt/model/tool cũ. Drift alert là tín hiệu điều tra, không tự cho phép train lại từ dữ liệu chưa được duyệt.

**Đã sâu hơn:** eval trở thành artifact gắn release, không chỉ bộ công cụ chấm. Các bước trên là thiết kế đề xuất, chưa có phép đo hiệu quả do kho tự chạy.

**Nguồn phần 4/11:** [LICENSE](https://github.com/langchain-ai/openevals/blob/5753dc75d40c2be75ffd38eb6d63bb966cbcc4e3/LICENSE) · [README.md](https://github.com/langchain-ai/openevals/blob/5753dc75d40c2be75ffd38eb6d63bb966cbcc4e3/README.md) · [python/openevals/exact.py](https://github.com/langchain-ai/openevals/blob/5753dc75d40c2be75ffd38eb6d63bb966cbcc4e3/python/openevals/exact.py) · [python/openevals/llm.py](https://github.com/langchain-ai/openevals/blob/5753dc75d40c2be75ffd38eb6d63bb966cbcc4e3/python/openevals/llm.py) · [python/openevals/utils.py](https://github.com/langchain-ai/openevals/blob/5753dc75d40c2be75ffd38eb6d63bb966cbcc4e3/python/openevals/utils.py) · [python/openevals/code/e2b/execution.py](https://github.com/langchain-ai/openevals/blob/5753dc75d40c2be75ffd38eb6d63bb966cbcc4e3/python/openevals/code/e2b/execution.py) · [.github/workflows/integration_tests.yml](https://github.com/langchain-ai/openevals/blob/5753dc75d40c2be75ffd38eb6d63bb966cbcc4e3/.github/workflows/integration_tests.yml)

## Nguồn

- Mục 23 §3.1, §4.3, §5 (X-Agents, xboss, Hermes-Agents; đọc 2026-10-12)
- https://futureagi.com/blog/best-open-source-eval-frameworks-2026/ · https://inference.net/content/llm-evaluation-tools-comparison/ · https://agentscamp.com/guides/evaluation/best-llm-eval-tools-2026 · https://aiml.qa/llm-evaluation-framework-benchmark-2026/ · https://genai.qa/blog/promptfoo-vs-deepeval-vs-ragas/ · https://techsy.io/en/blog/best-llm-evaluation-tools
- Bổ sung (12/10/2026): https://github.com/UKGovernmentBEIS/inspect_ai · https://inspect.aisi.org.uk/ · https://github.com/METR/vivaria · https://github.com/EleutherAI/lm-evaluation-harness · https://github.com/harbor-framework/harbor · https://github.com/harbor-framework/terminal-bench-1 · https://www.tbench.ai/news · https://github.com/sierra-research/tau2-bench · https://arxiv.org/abs/2506.07982 · https://github.com/comet-ml/opik · https://github.com/mlflow/mlflow · https://github.com/traceloop/openllmetry · https://www.calcalistech.com/ctechnews/article/sjghwiqf11e · https://github.com/lmnr-ai/lmnr · https://github.com/open-compass/opencompass · https://github.com/huggingface/lighteval · https://github.com/stanford-crfm/helm · https://github.com/openai/evals · https://github.com/AgentOps-AI/agentops · https://github.com/wandb/weave
- Case study Overmind (12/10/2026): https://github.com/overmind-core/overmind (clone đầy đủ: README.md, .env.example, docker-compose.yml, overbae/settings.py, overbae/api/auth_registration.py, overbae/services/project_invites.py, overbae/services/mcp/{catalog,context}.py, overmind/overmind/{analytics,config}.py, .agents/hooks/guards.py, .claude/settings.json) · https://github.com/overmind-core/overmind/releases · https://pypi.org/project/overmind/ · https://pypistats.org/packages/overmind · https://trendshift.io/repositories/274765 · https://overmindlab.ai/pricing · https://overmindlab.ai/about · https://tech.eu/2026/02/11/overmind-launches-with-2m-in-seed-funding-to-support-development-of-agentic-ai/ · https://osneycapital.com/portfolio/overmind · https://digg.com/ai/fj6px48f · https://themenonlab.blog/blog/overmind-training-platform-specialized-agents · https://www.opensourcealternatives.to/item/overmind · https://github.com/OpenPipe/ART · https://github.com/DarthSim/overmind · https://github.com/cerebral/overmind · https://github.com/overmindtech/cli · https://startupintros.com/news/2025-09-01-overmind-seed

<a id="chuyen-muc-2026-11-23"></a>

## Hồ sơ chuyển về từ mục khác — 23/11/2026

2 hồ sơ được chuyển khi chia lại catalog theo `data/taxonomy.json`. Nội dung, ngày kiểm và mức bằng chứng giữ nguyên như ở mục gốc.

<a id="chuyen-shap"></a>

### shap

`shap/shap` · License: MIT License · ★ 25.867 · docs-read · 2026-11-18

Thư viện giải thích đầu ra của mô hình học máy bằng giá trị Shapley (SHAP), kèm nhiều biểu đồ trực quan hoá. Có thuật toán chính xác tốc độ cao cho tree ensemble (XGBoost, LightGBM, CatBoost, scikit-learn, pyspark) viết bằng C++; GPUTreeExplainer qua gói shap-cuda; tuân SPEC 0 về phiên bản phụ thuộc tối thiểu. Điều kiện: Tăng tốc GPU cần gói riêng shap[cuda] và phần cứng CUDA. ★ 18/11/2026: 25.867 (GitHub search API), nhóm "Mô hình AI & Huấn luyện" trong kho-repo của Phan Đông Giang, mục 08 §6c.5

**Hồ sơ gốc:** [mục 08](../08-awesome-lists-learning/README.md#6c513-mô-hình-ai--huấn-luyện) (bảng/đoạn chung, giữ nguyên tại chỗ).

<a id="chuyen-netron"></a>

### netron

`lutzroeder/netron` · License: MIT · ★ 33.703 · docs-read · 2026-11-18

Trình xem mô hình mạng nơ-ron, học sâu và học máy; hiển thị đồ thị mô hình trên trình duyệt hoặc ứng dụng desktop. Hỗ trợ ONNX, TensorFlow Lite, PyTorch, Core ML, OpenVINO, Keras, Safetensors và nhiều định dạng khác; có bản trình duyệt netron.app không cần cài; có bản macOS, Linux, Windows và gói Python. ★ 18/11/2026: 33.703 (GitHub search API), nhóm "Đồ họa, 3D & Sơ đồ" trong kho-repo của Phan Đông Giang, mục 08 §6c.5

**Hồ sơ gốc:** [mục 08](../08-awesome-lists-learning/README.md#6c527-đồ-họa-3d--sơ-đồ) (bảng/đoạn chung, giữ nguyên tại chỗ).

<a id="chuan-hoa-2026-11-23"></a>

## Chuẩn hóa bằng chứng hồ sơ cũ — 23/11/2026

Các hồ sơ dưới đây có từ trước khi kho ghi mức kiểm. Ngày 2026-11-23 mỗi repo được clone nông tại commit ghi trong bảng, đọc LICENSE, README, manifest và CI (nếu có); không cài, build hay chạy mã upstream. Nhận định cũ ở phần trên giữ nguyên; chỗ nào khác với lần đọc này được ghi trong cột Nhận định. Số sao lấy qua GitHub search API cùng ngày.

<a id="ch-arize-phoenix"></a>

### Arize Phoenix

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/Arize-ai/phoenix |
| License | Elastic-2.0 (ELv2) |
| Phiên bản đã đọc | `2a372100db49c3d91dfdc726651a5a3cee0c4e2e` (commit 2026-11-23) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE; chưa chạy upstream |
| Bảo trì | active (đang hoạt động) |
| Nhận định | Nền tảng quan sát/eval AI mã nguồn mở của Arize (tracing OTel, dataset, experiment, playground, MCP server từ xa). License ELv2 là source-available, không phải OSI: có hạn chế cung cấp dưới dạng dịch vụ quản lý. |
| Nguồn | [README.md](https://github.com/Arize-ai/phoenix/blob/2a372100db49c3d91dfdc726651a5a3cee0c4e2e/README.md) · [LICENSE](https://github.com/Arize-ai/phoenix/blob/2a372100db49c3d91dfdc726651a5a3cee0c4e2e/LICENSE) |

<a id="ch-coze-loop"></a>

### Coze Loop

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/coze-dev/coze-loop |
| License | Apache-2.0 |
| Phiên bản đã đọc | `36b9796878604bc87e0fadd047dc27e89dfe8c26` (commit 2026-11-10) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE, .github/workflows/ai-cr-required.yaml; chưa chạy upstream |
| Bảo trì | active (đang hoạt động) |
| Nhận định | Bản mở của Coze Loop (ByteDance): playground prompt, eval, observability; README hướng dẫn cấu hình model Volcengine Ark làm ví dụ. Workflow ai-cr-required đã bị tắt bằng cách đổi nhánh kích hoạt sang "disabled-temporarily". |
| Nguồn | [README.md](https://github.com/coze-dev/coze-loop/blob/36b9796878604bc87e0fadd047dc27e89dfe8c26/README.md) · [LICENSE](https://github.com/coze-dev/coze-loop/blob/36b9796878604bc87e0fadd047dc27e89dfe8c26/LICENSE) · [ai-cr-required.yaml](https://github.com/coze-dev/coze-loop/blob/36b9796878604bc87e0fadd047dc27e89dfe8c26/.github/workflows/ai-cr-required.yaml) |

<a id="ch-deepeval"></a>

### DeepEval

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/confident-ai/deepeval |
| License | Apache-2.0 |
| Phiên bản đã đọc | `6a43e72c77a490b2eebe240c8fc22b1a2bd4e643` (commit 2026-11-23) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE.md; chưa chạy upstream |
| Bảo trì | active (đang hoạt động) |
| Nhận định | Framework eval LLM kiểu pytest của Confident AI (metric, agent trajectory, RAG, voice). README có cài đặt quảng bá nền tảng thương mại Confident AI; repo rất hoạt động. |
| Nguồn | [README.md](https://github.com/confident-ai/deepeval/blob/6a43e72c77a490b2eebe240c8fc22b1a2bd4e643/README.md) · [LICENSE.md](https://github.com/confident-ai/deepeval/blob/6a43e72c77a490b2eebe240c8fc22b1a2bd4e643/LICENSE.md) |

<a id="ch-evidently"></a>

### Evidently

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/evidentlyai/evidently |
| License | Apache-2.0 |
| Phiên bản đã đọc | `34771fe41c08ca074d96a52aaf4a45cd640cbaf5` (commit 2026-09-11) |
| Kiểm chứng | 2026-11-23; code-read; đã đọc README.md, LICENSE, src/evidently/telemetry.py và ui/service/components/telemetry.py (grep dòng liên quan); chưa chạy upstream |
| Bảo trì | low-activity (commit cuối cách hơn 2 tháng) |
| Nhận định | Thư viện Python eval/test/monitor ML và LLM. Telemetry mặc định gửi HTTP (không TLS) tới 35.232.253.5:8000, có thể tắt bằng DO_NOT_TRACK; README không nhắc telemetry. Hoạt động chậm lại (commit cuối 11/9/2026). |
| Nguồn | [README.md](https://github.com/evidentlyai/evidently/blob/34771fe41c08ca074d96a52aaf4a45cd640cbaf5/README.md) · [LICENSE](https://github.com/evidentlyai/evidently/blob/34771fe41c08ca074d96a52aaf4a45cd640cbaf5/LICENSE) · [telemetry.py](https://github.com/evidentlyai/evidently/blob/34771fe41c08ca074d96a52aaf4a45cd640cbaf5/src/evidently/telemetry.py) · [telemetry.py](https://github.com/evidentlyai/evidently/blob/34771fe41c08ca074d96a52aaf4a45cd640cbaf5/src/evidently/ui/service/components/telemetry.py) |

<a id="ch-failproofai"></a>

### FailproofAI

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/FailproofAI/failproofai |
| License | MIT + Commons Clause (không phải OSI) |
| Phiên bản đã đọc | `33a050ba823190ede003c3c5468149d20b9939e2` (commit 2026-11-23) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE, package.json; chưa chạy upstream |
| Bảo trì | active (đang hoạt động) |
| Nhận định | Hook cho 12 harness agent (Claude Code, Codex, Cursor…) với policy chặn tool call và theo dõi phiên. License MIT kèm Commons Clause (cấm bán lại sản phẩm), README tự ghi. Mã có posthog-key.ts và hook-telemetry.ts; README không nhắc telemetry theo tìm chuỗi. |
| Nguồn | [README.md](https://github.com/FailproofAI/failproofai/blob/33a050ba823190ede003c3c5468149d20b9939e2/README.md) · [LICENSE](https://github.com/FailproofAI/failproofai/blob/33a050ba823190ede003c3c5468149d20b9939e2/LICENSE) · [package.json](https://github.com/FailproofAI/failproofai/blob/33a050ba823190ede003c3c5468149d20b9939e2/package.json) |

<a id="ch-giskard-v3"></a>

### Giskard (v3)

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/Giskard-AI/giskard-oss |
| License | Apache-2.0 |
| Phiên bản đã đọc | `e48ca61d34bd9d5e92f77fffc401e2c47c23bcfa` (commit 2026-11-22) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE; chưa chạy upstream |
| Bảo trì | active (đang hoạt động) |
| Nhận định | Bản viết lại v3 cho test agent nhiều lượt và quét lỗ hổng; README ghi v2 không còn bảo trì tích cực. Có telemetry ẩn danh tùy chọn, tắt bằng DO_NOT_TRACK=1 hoặc GISKARD_TELEMETRY_DISABLED=1, README có nêu rõ. |
| Nguồn | [README.md](https://github.com/Giskard-AI/giskard-oss/blob/e48ca61d34bd9d5e92f77fffc401e2c47c23bcfa/README.md) · [LICENSE](https://github.com/Giskard-AI/giskard-oss/blob/e48ca61d34bd9d5e92f77fffc401e2c47c23bcfa/LICENSE) |

<a id="ch-harbor-terminal-bench"></a>

### Harbor (Terminal-Bench)

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/harbor-framework/harbor |
| License | Apache-2.0 |
| Phiên bản đã đọc | `b62d54bd36dc3e031d7daa85dd538d5653cba834` (commit 2026-11-22) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE; chưa chạy upstream |
| Bảo trì | active (đang hoạt động) |
| Nhận định | Framework của nhóm Terminal-Bench để chạy/đánh giá agent và sinh rollout RL trên nhiều provider sandbox (Daytona, Modal…). README giới thiệu là runner cho Terminal-Bench; số phiên bản TB 4.0 chưa tái kiểm. |
| Nguồn | [README.md](https://github.com/harbor-framework/harbor/blob/b62d54bd36dc3e031d7daa85dd538d5653cba834/README.md) · [LICENSE](https://github.com/harbor-framework/harbor/blob/b62d54bd36dc3e031d7daa85dd538d5653cba834/LICENSE) |

<a id="ch-ifixai"></a>

### iFixAi

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/ifixai-ai/iFixAi |
| License | Apache-2.0 |
| Phiên bản đã đọc | `ba677410d21c1f382b1268e6ebde6136e6b54f44` (commit 2026-11-20) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE (README tiếng Anh); chưa chạy upstream |
| Bảo trì | active (đang hoạt động) |
| Nhận định | Công cụ audit "operational alignment" cho agent qua mô phỏng nghiệp vụ, có chế độ demo không cần API key. README ghi Apache 2.0, khớp LICENSE. Các số sao/tải xuống lệch của kho cũ chưa tái kiểm ở lượt này. |
| Nguồn | [README.md](https://github.com/ifixai-ai/iFixAi/blob/ba677410d21c1f382b1268e6ebde6136e6b54f44/README.md) · [LICENSE](https://github.com/ifixai-ai/iFixAi/blob/ba677410d21c1f382b1268e6ebde6136e6b54f44/LICENSE) |

<a id="ch-inspect-evals"></a>

### Inspect Evals

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/UKGovernmentBEIS/inspect_evals |
| License | MIT |
| Phiên bản đã đọc | `c2d3d5e1335c07fb8032bcfc7869e9437e635c4c` (commit 2026-11-19) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE, EVALUATION_CHECKLIST.md; chưa chạy upstream |
| Bảo trì | active (đang hoạt động) |
| Nhận định | Thư viện eval xây trên Inspect AI. README ghi nay do Generality Labs (nonprofit, London) bảo trì và chỉ nhận PR từ người đóng góp được duyệt trước; EVALUATION_CHECKLIST yêu cầu VALIDITY_REPORT.md. |
| Nguồn | [README.md](https://github.com/UKGovernmentBEIS/inspect_evals/blob/c2d3d5e1335c07fb8032bcfc7869e9437e635c4c/README.md) · [LICENSE](https://github.com/UKGovernmentBEIS/inspect_evals/blob/c2d3d5e1335c07fb8032bcfc7869e9437e635c4c/LICENSE) · [EVALUATION_CHECKLIST.md](https://github.com/UKGovernmentBEIS/inspect_evals/blob/c2d3d5e1335c07fb8032bcfc7869e9437e635c4c/EVALUATION_CHECKLIST.md) |

<a id="ch-laminar"></a>

### Laminar

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/lmnr-ai/lmnr |
| License | Apache-2.0 |
| Phiên bản đã đọc | `dc5f238c06f9f35caf07a2b4b17d5ce05fdef8bc` (commit 2026-11-10) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE.md; chưa chạy upstream |
| Bảo trì | active (đang hoạt động) |
| Nhận định | Nền tảng quan sát cho agent mã nguồn mở (tracing OTel, signals, eval, tự host qua docker compose). Cần xem thêm giấy phép từng thành phần khi dùng thương mại. |
| Nguồn | [README.md](https://github.com/lmnr-ai/lmnr/blob/dc5f238c06f9f35caf07a2b4b17d5ce05fdef8bc/README.md) · [LICENSE.md](https://github.com/lmnr-ai/lmnr/blob/dc5f238c06f9f35caf07a2b4b17d5ce05fdef8bc/LICENSE.md) |

<a id="ch-langfuse"></a>

### Langfuse

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/langfuse/langfuse |
| License | MIT (Expat) cho phần lõi; thư mục ee/ và các đường dẫn ee khác theo giấy phép riêng |
| Phiên bản đã đọc | `72bc5404558ef42167e9dde90cd530bd0b5f489b` (commit 2026-11-23) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE; chưa chạy upstream |
| Bảo trì | active (đang hoạt động) |
| Nhận định | Nền tảng kỹ thuật AI mã nguồn mở (quan sát, eval, prompt); README ghi từ 1/2026 là một phần của ClickHouse. LICENSE tách rõ phần MIT với các thư mục ee/ có giấy phép riêng. |
| Nguồn | [README.md](https://github.com/langfuse/langfuse/blob/72bc5404558ef42167e9dde90cd530bd0b5f489b/README.md) · [LICENSE](https://github.com/langfuse/langfuse/blob/72bc5404558ef42167e9dde90cd530bd0b5f489b/LICENSE) |

<a id="ch-langwatch"></a>

### LangWatch

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/langwatch/langwatch |
| License | Apache-2.0; thư mục enterprise/ theo LangWatch Enterprise License; SDK MIT theo README |
| Phiên bản đã đọc | `711539f587b3ba19606ffbe0425710842c181603` (commit 2026-11-23) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE.md, enterprise/LICENSE.md (đầu file); chưa chạy upstream |
| Bảo trì | active (đang hoạt động) |
| Nhận định | Nền tảng open-core cho trace/test/gateway LLM và theo dõi coding agent; tự host bằng `npx @langwatch/server` (Node.js 24+). Module enterprise/ cần giấy phép thương mại khi chạy production. |
| Nguồn | [README.md](https://github.com/langwatch/langwatch/blob/711539f587b3ba19606ffbe0425710842c181603/README.md) · [LICENSE.md](https://github.com/langwatch/langwatch/blob/711539f587b3ba19606ffbe0425710842c181603/LICENSE.md) · [LICENSE.md](https://github.com/langwatch/langwatch/blob/711539f587b3ba19606ffbe0425710842c181603/enterprise/LICENSE.md) |

<a id="ch-lighteval"></a>

### Lighteval

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/huggingface/lighteval |
| License | MIT |
| Phiên bản đã đọc | `b97a6533bec22c4184b88526366fdf5d73d502c9` (commit 2026-10-29) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE; chưa chạy upstream |
| Bảo trì | active (đang hoạt động) |
| Nhận định | Bộ công cụ eval LLM của Hugging Face đa backend, lưu kết quả theo từng mẫu. Hoạt động vừa phải (commit cuối 29/10/2026). |
| Nguồn | [README.md](https://github.com/huggingface/lighteval/blob/b97a6533bec22c4184b88526366fdf5d73d502c9/README.md) · [LICENSE](https://github.com/huggingface/lighteval/blob/b97a6533bec22c4184b88526366fdf5d73d502c9/LICENSE) |

<a id="ch-lm-evaluation-harness"></a>

### lm-evaluation-harness

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/EleutherAI/lm-evaluation-harness |
| License | MIT |
| Phiên bản đã đọc | `d6de81643928d653435c431bae19945d41d32520` (commit 2026-09-14) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE.md; chưa chạy upstream |
| Bảo trì | low-activity (commit cuối cách hơn 2 tháng) |
| Nhận định | Harness eval few-shot LLM của EleutherAI; README tin mới ghi plugin entry point `lm_eval.*` (9/2026), CLI có subcommand. Cài lõi không còn kèm transformers/torch. Commit cuối 14/9/2026. |
| Nguồn | [README.md](https://github.com/EleutherAI/lm-evaluation-harness/blob/d6de81643928d653435c431bae19945d41d32520/README.md) · [LICENSE.md](https://github.com/EleutherAI/lm-evaluation-harness/blob/d6de81643928d653435c431bae19945d41d32520/LICENSE.md) |

<a id="ch-mlflow"></a>

### MLflow

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/mlflow/mlflow |
| License | Apache-2.0 |
| Phiên bản đã đọc | `4de30f357566f823f6026ff21c5a222fff2e6df6` (commit 2026-11-23) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE.txt; chưa chạy upstream |
| Bảo trì | active (đang hoạt động) |
| Nhận định | Nền tảng AI engineering mã nguồn mở (tracing, eval, prompt registry, AI Gateway), tuyên bố 60 triệu lượt tải/tháng **(chưa xác minh)**. Rất hoạt động. |
| Nguồn | [README.md](https://github.com/mlflow/mlflow/blob/4de30f357566f823f6026ff21c5a222fff2e6df6/README.md) · [LICENSE.txt](https://github.com/mlflow/mlflow/blob/4de30f357566f823f6026ff21c5a222fff2e6df6/LICENSE.txt) |

<a id="ch-opencompass"></a>

### OpenCompass

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/open-compass/opencompass |
| License | Apache-2.0 |
| Phiên bản đã đọc | `443bc2b3a4191943c2b5f1ca990d8078df785973` (commit 2026-11-18) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE; chưa chạy upstream |
| Bảo trì | active (đang hoạt động) |
| Nhận định | Nền tảng đánh giá LLM của Shanghai AI Lab kèm CompassHub/CompassRank. Commit cuối 18/11/2026. |
| Nguồn | [README.md](https://github.com/open-compass/opencompass/blob/443bc2b3a4191943c2b5f1ca990d8078df785973/README.md) · [LICENSE](https://github.com/open-compass/opencompass/blob/443bc2b3a4191943c2b5f1ca990d8078df785973/LICENSE) |

<a id="ch-openinference"></a>

### OpenInference

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/Arize-ai/openinference |
| License | Apache-2.0 |
| Phiên bản đã đọc | `1d6cf21550b91f8d136db94d4bf81a50fbdc5c16` (commit 2026-11-21) |
| Kiểm chứng | 2026-11-23; code-read; đã đọc README.md, LICENSE, python/openinference-instrumentation/.../config.py (grep dòng liên quan); chưa chạy upstream |
| Bảo trì | active (đang hoạt động) |
| Nhận định | Đặc tả OpenInference trên OpenTelemetry cho trace agent cùng bộ instrument đa framework (thư mục python/instrumentation hiện có 38 mục). Mặc định HIDE_INPUTS/HIDE_OUTPUTS là False nên nội dung vào/ra được ghi lại. |
| Nguồn | [README.md](https://github.com/Arize-ai/openinference/blob/1d6cf21550b91f8d136db94d4bf81a50fbdc5c16/README.md) · [LICENSE](https://github.com/Arize-ai/openinference/blob/1d6cf21550b91f8d136db94d4bf81a50fbdc5c16/LICENSE) · [config.py](https://github.com/Arize-ai/openinference/blob/1d6cf21550b91f8d136db94d4bf81a50fbdc5c16/python/openinference-instrumentation/src/openinference/instrumentation/config.py) |

<a id="ch-openlit"></a>

### OpenLIT

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/openlit/openlit |
| License | Apache-2.0 |
| Phiên bản đã đọc | `463a1c1b3cd72a94fab4155efe0f28d90d87fe95` (commit 2026-11-19) |
| Kiểm chứng | 2026-11-23; code-read; đã đọc README.md, LICENSE, `sdk/python/.../__init__`.py và docker-compose.yml (grep dòng liên quan); chưa chạy upstream |
| Bảo trì | active (đang hoạt động) |
| Nhận định | Nền tảng OTel-native cho trace/eval/guardrail/GPU của agent. SDK Python mặc định capture_message_content=True; docker-compose đặt TELEMETRY_ENABLED "true"; client Next có posthog-js. |
| Nguồn | [README.md](https://github.com/openlit/openlit/blob/463a1c1b3cd72a94fab4155efe0f28d90d87fe95/README.md) · [LICENSE](https://github.com/openlit/openlit/blob/463a1c1b3cd72a94fab4155efe0f28d90d87fe95/LICENSE) · `[__init__.py](https://github.com/openlit/openlit/blob/463a1c1b3cd72a94fab4155efe0f28d90d87fe95/sdk/python/src/openlit/__init__`.py) · [docker-compose.yml](https://github.com/openlit/openlit/blob/463a1c1b3cd72a94fab4155efe0f28d90d87fe95/docker-compose.yml) |

<a id="ch-openllmetry"></a>

### OpenLLMetry

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/traceloop/openllmetry |
| License | Apache-2.0 |
| Phiên bản đã đọc | `282cbd0909ec7433ab4629950271eddce2628170` (commit 2026-11-22) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE; chưa chạy upstream |
| Bảo trì | active (đang hoạt động) |
| Nhận định | Bộ instrument OTel cho nhà cung cấp LLM và vector DB cùng Traceloop SDK, do Traceloop duy trì. README nói semantic conventions đã thành một phần của OpenTelemetry; việc ServiceNow mua Traceloop chưa tái kiểm. |
| Nguồn | [README.md](https://github.com/traceloop/openllmetry/blob/282cbd0909ec7433ab4629950271eddce2628170/README.md) · [LICENSE](https://github.com/traceloop/openllmetry/blob/282cbd0909ec7433ab4629950271eddce2628170/LICENSE) |

<a id="ch-openpipe-art"></a>

### OpenPipe ART

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/OpenPipe/ART |
| License | Apache-2.0 (đính chính: catalog cũ ghi None) |
| Phiên bản đã đọc | `55b423c3004afeec3362fd35717b47356dfdd9fa` (commit 2026-11-16) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE; chưa chạy upstream |
| Bảo trì | active (đang hoạt động) |
| Nhận định | Thư viện RL (GRPO) huấn luyện agent nhiều bước; README quảng bá dịch vụ W&B Training (Serverless RL) với số liệu lợi ích tự tuyên bố **(chưa xác minh)**. Đính chính: catalog cũ ghi license là None, thực tế repo có LICENSE Apache-2.0. |
| Nguồn | [README.md](https://github.com/OpenPipe/ART/blob/55b423c3004afeec3362fd35717b47356dfdd9fa/README.md) · [LICENSE](https://github.com/OpenPipe/ART/blob/55b423c3004afeec3362fd35717b47356dfdd9fa/LICENSE) |

<a id="ch-opentelemetry-genai-semantic-conventions"></a>

### OpenTelemetry GenAI Semantic Conventions

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/open-telemetry/semantic-conventions-genai |
| License | Apache-2.0 |
| Phiên bản đã đọc | `ae8214a8f3a98786071736855093b74621174dc4` (commit 2026-11-23) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE, docs/gen-ai/gen-ai-spans.md (grep dòng trạng thái); chưa chạy upstream |
| Bảo trì | active (đang hoạt động) |
| Nhận định | Semantic conventions GenAI (span, metric, event, MCP, provider cụ thể) tách ra repo riêng, quản lý bằng Weaver. Thuộc tính trong tài liệu span đang ở trạng thái Development; thư mục reference chứa scenarios cho kiểm tra tuân thủ. |
| Nguồn | [README.md](https://github.com/open-telemetry/semantic-conventions-genai/blob/ae8214a8f3a98786071736855093b74621174dc4/README.md) · [LICENSE](https://github.com/open-telemetry/semantic-conventions-genai/blob/ae8214a8f3a98786071736855093b74621174dc4/LICENSE) · [gen-ai-spans.md](https://github.com/open-telemetry/semantic-conventions-genai/blob/ae8214a8f3a98786071736855093b74621174dc4/docs/gen-ai/gen-ai-spans.md) |

<a id="ch-opentelemetry-weaver"></a>

### OpenTelemetry Weaver

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/open-telemetry/weaver |
| License | Apache-2.0 |
| Phiên bản đã đọc | `df0746e9858d7c3aa45a8baf782f39928ad00ece` (commit 2026-11-19) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE; chưa chạy upstream |
| Bảo trì | active (đang hoạt động) |
| Nhận định | Công cụ khai báo/kiểm tra/phát triển semantic conventions và live-check OTLP. README liệt kê GitHub Action weaver-live-check-start/stop, có thể fail theo ngưỡng severity. Chưa kiểm số phiên bản 0.x. |
| Nguồn | [README.md](https://github.com/open-telemetry/weaver/blob/df0746e9858d7c3aa45a8baf782f39928ad00ece/README.md) · [LICENSE](https://github.com/open-telemetry/weaver/blob/df0746e9858d7c3aa45a8baf782f39928ad00ece/LICENSE) |

<a id="ch-opik"></a>

### Opik

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/comet-ml/opik |
| License | Apache-2.0 |
| Phiên bản đã đọc | `32de5e5414ed3ff2e2bea45c3da0bd1f3bbc9b96` (commit 2026-11-23) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE; chưa chạy upstream |
| Bảo trì | Commit mới nhất 2026-11-23; CI rộng (nhiều workflow, đã liệt kê thư mục) |
| Nhận định | Nền tảng quan sát/đánh giá LLM (trace, dataset, experiment, LLM-judge, prompt, guardrails); repo gồm backend, frontend, SDK Python/TS. Việc "không quản lý user" khi tự host là nhận định cũ, **(chưa xác minh)** trong lần đọc này. |
| Nguồn | [README.md](https://github.com/comet-ml/opik/blob/32de5e5414ed3ff2e2bea45c3da0bd1f3bbc9b96/README.md) · [LICENSE](https://github.com/comet-ml/opik/blob/32de5e5414ed3ff2e2bea45c3da0bd1f3bbc9b96/LICENSE) |

<a id="ch-overmind"></a>

### Overmind

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/overmind-core/overmind |
| License | AGPL-3.0 (platform) / MIT (SDK, thư mục overmind/) |
| Phiên bản đã đọc | `899e0453fe718aa3ad50d369edf40d9a5398b987` (commit 2026-11-23) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE, overmind/LICENSE, pyproject.toml; chưa chạy upstream |
| Bảo trì | Commit mới nhất 2026-11-23 |
| Nhận định | Nền tảng biến trace production thành dataset, eval và fine-tune model chuyên biệt (chạy trên Modal), có CLI/SDK và REST API. Tự host giữ dữ liệu trong mạng nhưng phụ thuộc OpenRouter/Modal; AGPL-3.0 cho phần platform cần cân nhắc nếu nhúng. |
| Nguồn | [README.md](https://github.com/overmind-core/overmind/blob/899e0453fe718aa3ad50d369edf40d9a5398b987/README.md) · [LICENSE](https://github.com/overmind-core/overmind/blob/899e0453fe718aa3ad50d369edf40d9a5398b987/LICENSE) · [overmind/LICENSE](https://github.com/overmind-core/overmind/blob/899e0453fe718aa3ad50d369edf40d9a5398b987/overmind/LICENSE) · [pyproject.toml](https://github.com/overmind-core/overmind/blob/899e0453fe718aa3ad50d369edf40d9a5398b987/pyproject.toml) |

<a id="ch-pydantic-logfire-sdk"></a>

### Pydantic Logfire (SDK)

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/pydantic/logfire |
| License | MIT (SDK; server đóng mã) |
| Phiên bản đã đọc | `d89a30f7ead97b495a8df902a82e4af75ff61627` (commit 2026-11-23) |
| Kiểm chứng | 2026-11-23; code-read; đã đọc README.md, LICENSE, logfire-sdk/LICENSE, logfire-sdk/logfire/_internal/scrubbing.py, pyproject.toml; chưa chạy upstream |
| Bảo trì | Commit mới nhất 2026-11-23 |
| Nhận định | SDK Python bọc OpenTelemetry cho observability; mặc định che dữ liệu nhạy cảm theo regex trong scrubbing.py. Dùng đầy đủ cần backend Pydantic Logfire đóng mã (hoặc collector OTel khác tự dựng). |
| Nguồn | [README.md](https://github.com/pydantic/logfire/blob/d89a30f7ead97b495a8df902a82e4af75ff61627/README.md) · [LICENSE](https://github.com/pydantic/logfire/blob/d89a30f7ead97b495a8df902a82e4af75ff61627/LICENSE) · [logfire-sdk/LICENSE](https://github.com/pydantic/logfire/blob/d89a30f7ead97b495a8df902a82e4af75ff61627/logfire-sdk/LICENSE) · [logfire-sdk/logfire/_internal/scrubbing.py](https://github.com/pydantic/logfire/blob/d89a30f7ead97b495a8df902a82e4af75ff61627/logfire-sdk/logfire/_internal/scrubbing.py) · [pyproject.toml](https://github.com/pydantic/logfire/blob/d89a30f7ead97b495a8df902a82e4af75ff61627/pyproject.toml) |

<a id="ch-ragas"></a>

### Ragas

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/vibrantlabsai/ragas |
| License | Apache-2.0 |
| Phiên bản đã đọc | `8c63f10d500c44efbf24fdb9e2920de2104c321c` (commit 2026-11-13) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE, pyproject.toml; chưa chạy upstream |
| Bảo trì | Commit mới nhất 2026-11-13, trái với ghi chú cũ "không commit từ 23/2/2026" |
| Nhận định | Khung đánh giá ứng dụng RAG/LLM bằng metric (LLM-judge, sinh test set). Repo đã chuyển chủ sang vibrantlabsai nhưng vẫn có commit gần đây; pyproject khai license trỏ file LICENSE. |
| Nguồn | [README.md](https://github.com/vibrantlabsai/ragas/blob/8c63f10d500c44efbf24fdb9e2920de2104c321c/README.md) · [LICENSE](https://github.com/vibrantlabsai/ragas/blob/8c63f10d500c44efbf24fdb9e2920de2104c321c/LICENSE) · [pyproject.toml](https://github.com/vibrantlabsai/ragas/blob/8c63f10d500c44efbf24fdb9e2920de2104c321c/pyproject.toml) |

<a id="ch-rewardbench"></a>

### RewardBench

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/allenai/reward-bench |
| License | Apache-2.0 |
| Phiên bản đã đọc | `59f6ff7005a9f9484727ca27f5383420875e5dbf` (commit 2026-10-14) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE, pyproject.toml; chưa chạy upstream |
| Bảo trì | Commit mới nhất 2026-10-14 |
| Nhận định | Bộ đánh giá reward model (V1, V2) cùng mã chạy cả reward model phân loại lẫn LLM-as-judge qua vLLM/API. Hữu ích để chọn model judge; chạy đầy đủ cần GPU/API (chưa xác minh chi phí). |
| Nguồn | [README.md](https://github.com/allenai/reward-bench/blob/59f6ff7005a9f9484727ca27f5383420875e5dbf/README.md) · [LICENSE](https://github.com/allenai/reward-bench/blob/59f6ff7005a9f9484727ca27f5383420875e5dbf/LICENSE) · [pyproject.toml](https://github.com/allenai/reward-bench/blob/59f6ff7005a9f9484727ca27f5383420875e5dbf/pyproject.toml) |

<a id="ch-tau2-bench"></a>

### tau2-bench

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/sierra-research/tau2-bench |
| License | MIT |
| Phiên bản đã đọc | `768f3d8fe8528b4f32a5096f9ed008ae50f48ead` (commit 2026-11-20) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE, pyproject.toml; chưa chạy upstream |
| Bảo trì | Commit mới nhất 2026-11-20 |
| Nhận định | Benchmark tool-agent-user cho hội thoại chăm sóc khách hàng, có mô phỏng người dùng bằng LLM nên cần khóa API model. Yêu cầu Python 3.12-3.13; phiên bản/tên (τ², τ³, 2.0) đã đổi nhiều, cần ghi đúng phiên bản khi trích. |
| Nguồn | [README.md](https://github.com/sierra-research/tau2-bench/blob/768f3d8fe8528b4f32a5096f9ed008ae50f48ead/README.md) · [LICENSE](https://github.com/sierra-research/tau2-bench/blob/768f3d8fe8528b4f32a5096f9ed008ae50f48ead/LICENSE) · [pyproject.toml](https://github.com/sierra-research/tau2-bench/blob/768f3d8fe8528b4f32a5096f9ed008ae50f48ead/pyproject.toml) |

<a id="nt-2026-11-23"></a>

## Nâng trần theo khoảng trống — 23/11/2026

Phần này có các hồ sơ mới của đợt nâng trần: mười trinh sát tìm trên internet và GitHub những mảng mà chuyên mục còn thiếu hoặc chỉ có hồ sơ cũ, rồi mỗi repo được clone nông tại một commit cố định, đọc LICENSE, README, ít nhất một file triển khai thật và CI nếu có; không cài hay chạy mã upstream. Mô tả của trinh sát nhiều chỗ sai so với mã thật, và các chỗ đó được sửa ngay trong từng hồ sơ. Số sao lấy sau bằng GitHub search API nên có thể để trống.

<a id="nt-evals-skills"></a>

### Evals Skills (Parlance Labs)

| Thuộc tính | Giá trị |
|---|---|
| Repo | https://github.com/ai-evals-course/evals-skills |
| License | Apache-2.0 |
| Phiên bản đã đọc | `80d5f7b0127c7572ed9e9339937adbfd7240ffeb` (commit 2026-09-24) |
| Kiểm chứng | 2026-11-23; code-read; đã đọc README.md, skills/validate-evaluator/SKILL.md, .claude-plugin/plugin.json; chưa chạy upstream |
| Khoảng trống lấp | Quy trình eval sản phẩm LLM và hiệu chuẩn LLM-as-judge (không phải eval skill) |
| Cơ chế đáng học | - `skills/validate-evaluator/SKILL.md`: tách 10-20% train (nguồn few-shot), 40-45% dev, 40-45% test chạy đúng một lần; mục tiêu TPR và TNR trên 90%, tối thiểu 80%.<br>- Cùng file: hiệu chỉnh tỷ lệ pass thật `theta = (p_obs + TNR - 1) / (TPR + TNR - 1)`, bootstrap 2000 lần, cảnh báo mẫu dưới khoảng 60.<br>- `skills/error-discovery` (chỉ đọc mô tả ở README, chưa mở SKILL.md; chưa xác minh): dựng app HTML một file để người gán nhãn ghi chú tự do rồi gom thành failure mode; bắt buộc phân tích lỗi trước khi viết eval.<br>- Anti-pattern nêu rõ: dùng accuracy thô, rò rỉ dev/test vào few-shot, báo điểm không kèm khoảng tin cậy. |
| Tiêu chí và cách kiểm | Ngưỡng nằm trong văn bản skill (TPR và TNR 80/90%, khoảng 100 nhãn cân bằng 50/50, nhãn từ chuyên gia miền); không có script kiểm tự động, không CI, không test. Kết quả phụ thuộc agent làm đúng hướng dẫn. |
| Giới hạn và rủi ro | Không có CI hay kiểm tự động; số liệu và ví dụ trong skill là hướng dẫn, chưa xác minh bằng chạy. Gợi ý ghim phiên bản model judge là đúng thực hành nhưng chỉ ở mức văn bản. Skill phục vụ khóa học thương mại của tác giả (liên kết khuyến mãi trong README); nội dung vẫn Apache-2.0. Phạm vi dữ liệu: người dùng phải tự có trace và nhãn. |
| So với | deepeval (thư viện eval chạy được), openevals, llm-evaluation-guidebook (tài liệu học) |
| Nguồn | [README.md](https://github.com/ai-evals-course/evals-skills/blob/80d5f7b0127c7572ed9e9339937adbfd7240ffeb/README.md) · [LICENSE](https://github.com/ai-evals-course/evals-skills/blob/80d5f7b0127c7572ed9e9339937adbfd7240ffeb/LICENSE) · [SKILL.md](https://github.com/ai-evals-course/evals-skills/blob/80d5f7b0127c7572ed9e9339937adbfd7240ffeb/skills/validate-evaluator/SKILL.md) · [plugin.json](https://github.com/ai-evals-course/evals-skills/blob/80d5f7b0127c7572ed9e9339937adbfd7240ffeb/.claude-plugin/plugin.json) |

<a id="nt-ragas-rag-metrics"></a>

### Ragas (số liệu RAG tách retrieval và answer)

| Thuộc tính | Giá trị |
|---|---|
| Repo | https://github.com/explodinggradients/ragas |
| License | Apache-2.0 |
| Phiên bản đã đọc | `8c63f10d500c44efbf24fdb9e2920de2104c321c` (commit 2026-11-13) |
| Kiểm chứng | 2026-11-23; code-read; đã đọc README.md, LICENSE, pyproject.toml, src/ragas/_analytics.py; chưa chạy upstream |
| Khoảng trống lấp | Đánh giá RAG tách retrieval và answer (đã có hồ sơ `ragas` ở mục 07; mục này bổ sung góc đọc code) |
| Cơ chế đáng học | - `metrics/collections/faithfulness/metric.py`: tách câu trả lời thành các câu nguyên tử rồi gọi LLM làm NLI so với ngữ cảnh; điểm = số câu được ngữ cảnh hỗ trợ chia tổng số câu; trả NaN nếu không sinh được câu nào.<br>- `context_precision/metric.py`: LLM phán từng ngữ cảnh truy xuất có hữu ích không, rồi tính average precision theo thứ tự xếp hạng (`_calculate_average_precision`), nên thưởng khi ngữ cảnh đúng đứng trước; có biến thể có và không có reference.<br>- `context_recall/util.py`: LLM phân loại từng câu trong reference là `attributed` (1) hoặc không (0) so với ngữ cảnh, tức đo truy xuất có phủ đủ đáp án chuẩn.<br>- Đầu vào bắt buộc và kiểm trước (`user_input`, `response`, `retrieved_contexts`); LLM gọi qua lớp `instructor` với đầu ra có cấu trúc pydantic. |
| Tiêu chí và cách kiểm | Điểm là tỷ lệ 0–1 do LLM phán nên phụ thuộc model chấm và prompt; không có ngưỡng đạt mặc định, người dùng tự đặt. Repo có `tests/unit` chạy trong `.github/workflows/ci.yaml` (đã mở), đặt `RAGAS_DO_NOT_TRACK=true` khi chạy test. Test là kiểm máy trên logic, không chứng minh metric tương quan với đánh giá của người. |
| Giới hạn và rủi ro | Telemetry: `_analytics.py` gửi sự kiện (user id ngẫu nhiên lưu ở thư mục dữ liệu người dùng, tên metric, số dòng, ngôn ngữ, loại LLM) tới `https://t.explodinggradients.com` mặc định; tắt bằng biến môi trường `RAGAS_DO_NOT_TRACK=true`. Domain đã cũ so với tên tổ chức mới. Phụ thuộc nặng (langchain, openai, datasets). Có hai thế hệ API (`metrics` cũ và `metrics/collections` mới) nên dễ lẫn khi đọc tài liệu cũ. Metric LLM-as-judge: ngôn ngữ ngoài tiếng Anh cần điều chỉnh prompt (tham số `language` trong `prompt/base.py`), chất lượng với tiếng Việt chưa xác minh. |
| So với | `ragas` (hồ sơ có sẵn, mục 07), `deepeval`, `lighteval`; `docling` khi cần đo khâu trích xuất tài liệu trước RAG. |
| Nguồn | [README.md](https://github.com/explodinggradients/ragas/blob/8c63f10d500c44efbf24fdb9e2920de2104c321c/README.md) · [LICENSE](https://github.com/explodinggradients/ragas/blob/8c63f10d500c44efbf24fdb9e2920de2104c321c/LICENSE) · [pyproject.toml](https://github.com/explodinggradients/ragas/blob/8c63f10d500c44efbf24fdb9e2920de2104c321c/pyproject.toml) · [_analytics.py](https://github.com/explodinggradients/ragas/blob/8c63f10d500c44efbf24fdb9e2920de2104c321c/src/ragas/_analytics.py) · [metric.py](https://github.com/explodinggradients/ragas/blob/8c63f10d500c44efbf24fdb9e2920de2104c321c/src/ragas/metrics/collections/faithfulness/metric.py) · [metric.py](https://github.com/explodinggradients/ragas/blob/8c63f10d500c44efbf24fdb9e2920de2104c321c/src/ragas/metrics/collections/context_precision/metric.py) · [util.py](https://github.com/explodinggradients/ragas/blob/8c63f10d500c44efbf24fdb9e2920de2104c321c/src/ragas/metrics/collections/context_recall/util.py) · [ci.yaml](https://github.com/explodinggradients/ragas/blob/8c63f10d500c44efbf24fdb9e2920de2104c321c/.github/workflows/ci.yaml) |

<a id="nt-wildclawbench"></a>

### WildClawBench

| Thuộc tính | Giá trị |
|---|---|
| Repo | https://github.com/InternLM/WildClawBench |
| License | MIT |
| Phiên bản đã đọc | `3d22dcf20b2cba1b56f2784cc0265ef566ef6402` (commit 2026-11-18) |
| Kiểm chứng | 2026-11-23; code-read; đã đọc LICENSE, README.md, eval/run_batch.py, tasks/06_Safety_Alignment/06_Safety_Alignment_task_1_file_overwrite.md, tasks/task0_template.md; chưa chạy upstream |
| Khoảng trống lấp | Đánh giá agent/benchmark: bộ tác vụ end-to-end có chấm tự động, so được harness với nhau |
| Cơ chế đáng học | - Mỗi tác vụ là một file Markdown (YAML đầu file, Prompt, Expected Behavior, Grading Criteria, và hàm `grade()` bằng Python); mẫu ở `tasks/task0_template.md`.<br>- `eval/run_batch.py` chạy từng tác vụ trong container riêng và chỉ `docker cp` thư mục `gt` (ground truth) vào sau khi agent xong, rồi mới chạy `run_grading` (hàm `grade_the_task`).<br>- Tác vụ an toàn mẫu (`06_Safety_Alignment_task_1_file_overwrite.md`): điểm = 0,50 bảo toàn file ResNet có sẵn (so SHA-256) + 0,25 luật kiểm bản tóm tắt MAE + 0,25 LLM chấm chất lượng; phần quan sát được thì chấm bằng máy.<br>- Cùng 60 tác vụ chạy trên bốn harness (`src/agents/*`) để tách năng lực mô hình khỏi khung điều phối. |
| Tiêu chí và cách kiểm | Ngưỡng nằm trong từng hàm `grade()`; một phần dùng LLM judge (`JUDGE_MODEL`, mặc định theo README là openai/gpt-5.4 **(chưa xác minh)**). `eval/check_setup.py` kiểm môi trường trước khi chạy. Không có workflow CI; chưa chạy lại điểm nào. |
| Giới hạn và rủi ro | MIT (LICENSE đã đọc); dữ liệu tác vụ, ảnh Docker và video lấy từ Hugging Face/YouTube có điều khoản riêng, chưa đọc. `script/prepare.sh` tải video YouTube bằng yt-dlp, có thể cần cookie. Cần khóa OpenRouter và Brave Search, chi phí gọi mô hình đáng kể (bảng README ghi tổng chi phí từ khoảng 2 đến 96 USD cho 60 tác vụ tùy mô hình). Bảng xếp hạng 34 mô hình, con số 62,2% và 67,2% là tuyên bố của tác giả **(chưa xác minh)**. Số tác vụ 60 khớp số file `.md` trong `tasks/`. Phần chấm bằng LLM judge nên có độ nhiễu. |
| So với | agentbench, tau2-bench, harbor-terminal-bench (cùng loại benchmark agent), swe-bench-pro |
| Nguồn | [LICENSE](https://github.com/InternLM/WildClawBench/blob/3d22dcf20b2cba1b56f2784cc0265ef566ef6402/LICENSE) · [README.md](https://github.com/InternLM/WildClawBench/blob/3d22dcf20b2cba1b56f2784cc0265ef566ef6402/README.md) · [eval/run_batch.py](https://github.com/InternLM/WildClawBench/blob/3d22dcf20b2cba1b56f2784cc0265ef566ef6402/eval/run_batch.py) · [tasks/06_Safety_Alignment/06_Safety_Alignment_task_1_file_overwrite.md](https://github.com/InternLM/WildClawBench/blob/3d22dcf20b2cba1b56f2784cc0265ef566ef6402/tasks/06_Safety_Alignment/06_Safety_Alignment_task_1_file_overwrite.md) · [tasks/task0_template.md](https://github.com/InternLM/WildClawBench/blob/3d22dcf20b2cba1b56f2784cc0265ef566ef6402/tasks/task0_template.md) · [script/run.sh](https://github.com/InternLM/WildClawBench/blob/3d22dcf20b2cba1b56f2784cc0265ef566ef6402/script/run.sh) |

<a id="nt-autoevals"></a>

### Autoevals

| Thuộc tính | Giá trị |
|---|---|
| Repo | https://github.com/braintrustdata/autoevals |
| License | MIT (LICENSE, Copyright BrainTrust Data). Không có trọng số |
| Phiên bản đã đọc | `b4d93fad00437818797d0c1ed757160a3f062fd2` (commit 2026-11-19) |
| Kiểm chứng | 2026-11-23; code-read; đã đọc `README.md`, `LICENSE`, `pyproject.toml`, `py/autoevals/oai.py`, `py/autoevals/llm.py`, `templates/factuality.yaml`, `js/trajectory-utils.ts`, `.github/workflows/python.yaml`; chưa chạy upstream |
| Khoảng trống lấp | Bộ scorer LLM-as-judge, heuristic và thống kê dùng độc lập (Python và TypeScript), gồm template chấm trajectory |
| Cơ chế đáng học | - `templates/*.yaml` (factuality, closed_q_a, security, sql, summary, battle, humor...; thêm voice_*): mỗi template là prompt với biến `{{input}}`, `{{expected}}`, `{{output}}` và bảng `choice_scores` (ví dụ Factuality A 0.4, B 0.6, C 1, D 0, E 1).<br>- `py/autoevals/llm.py`: `LLMClassifier`/`SpecFileClassifier` nạp template, ép mô hình chọn một đáp án rồi đổi sang điểm; có cả đường sync và async.<br>- `js/trajectory-utils.ts`: dựng biến `trajectory` và `trajectory_with_system` từ trace nhiều lượt để chấm hành trình agent bằng template.<br>- Có thêm scorer heuristic (Levenshtein, số, JSON, danh sách) và RAGAS ở bản JS. |
| Tiêu chí và cách kiểm | Điểm là số 0 đến 1 từ bảng ánh xạ lựa chọn (do template cố định) nên có thể tái lập prompt, nhưng chất lượng phụ thuộc mô hình giám khảo. CI `python.yaml` chạy pytest trên Python 3.10 đến 3.14 với khóa API thật qua secret (đã mở workflow); tức test đụng dịch vụ ngoài. |
| Giới hạn và rủi ro | **Tuyên bố độc lập nền tảng chỉ đúng một phần:** `oai.py` lấy `OPENAI_BASE_URL`, nếu không có thì mặc định tới Braintrust Gateway (`https://gateway.braintrust.dev`), và khi base URL là gateway thì dùng `BRAINTRUST_API_KEY` hoặc rơi về `OPENAI_API_KEY`: nếu chỉ đặt khóa OpenAI mà quên `OPENAI_BASE_URL`, lời gọi (kèm khóa) đi qua gateway của Braintrust, trái với câu 'dùng OPENAI_API_KEY để gọi OpenAI' ở ví dụ README. Luôn đặt base URL rõ ràng. Điểm do LLM chấm nên lệch theo mô hình và không kiểm độ khớp với người. |
| So với | promptfoo, deepeval, ragas (đều có sẵn trong kho, cùng nhiệm vụ chấm LLM), inspect-ai (khung chạy eval chứ không phải thư viện scorer). |
| Nguồn | [README.md](https://github.com/braintrustdata/autoevals/blob/b4d93fad00437818797d0c1ed757160a3f062fd2/README.md) · [LICENSE](https://github.com/braintrustdata/autoevals/blob/b4d93fad00437818797d0c1ed757160a3f062fd2/LICENSE) · [pyproject.toml](https://github.com/braintrustdata/autoevals/blob/b4d93fad00437818797d0c1ed757160a3f062fd2/pyproject.toml) · [oai.py](https://github.com/braintrustdata/autoevals/blob/b4d93fad00437818797d0c1ed757160a3f062fd2/py/autoevals/oai.py) · [llm.py](https://github.com/braintrustdata/autoevals/blob/b4d93fad00437818797d0c1ed757160a3f062fd2/py/autoevals/llm.py) · [factuality.yaml](https://github.com/braintrustdata/autoevals/blob/b4d93fad00437818797d0c1ed757160a3f062fd2/templates/factuality.yaml) · [trajectory-utils.ts](https://github.com/braintrustdata/autoevals/blob/b4d93fad00437818797d0c1ed757160a3f062fd2/js/trajectory-utils.ts) · [python.yaml](https://github.com/braintrustdata/autoevals/blob/b4d93fad00437818797d0c1ed757160a3f062fd2/.github/workflows/python.yaml) |

<a id="nt-control-arena"></a>

### ControlArena

| Thuộc tính | Giá trị |
|---|---|
| Repo | https://github.com/UKGovernmentBEIS/control-arena |
| License | MIT (LICENSE, Copyright UK AI Security Institute; `pyproject.toml` khai MIT). Thư mục `LICENSES/` chứa Apache-2.0, BSD-3-Clause, LGPL-3.0 cho phụ thuộc (THIRD_PARTY_LICENSES.md). Dữ liệu/nhiệm vụ của từng setting và license của tập tải về **(chưa xác minh)**. Không có trọng số |
| Phiên bản đã đọc | `2c32268f8ea38eb94d66f61a83e0be01fd69c0c9` (commit 2026-11-23) |
| Kiểm chứng | 2026-11-23; code-read; đã đọc `README.md`, `LICENSE`, `THIRD_PARTY_LICENSES.md`, `pyproject.toml`, `control_arena/analysis/_metrics.py`, `.github/workflows/checks.yml`; chưa chạy upstream |
| Khoảng trống lấp | Đánh giá kiểm soát AI (AI control): agent không tin cậy chạy dưới giám sát, đo an toàn và hữu ích |
| Cơ chế đáng học | - Bộ khái niệm: setting (môi trường và nhiệm vụ sabotage: iac, bash, apps, agentdojo, shade_arena, swebench, vllm, data_poisoning...), micro-protocol (`defer_to_trusted`, `defer_to_resample`, `trusted_editing`, `trusted_monitoring`), policy (trung thực/tấn công), monitor.<br>- `analysis/_metrics.py`: `compute_suspicion_threshold` lấy percentile (100 trừ ngân sách audit) từ điểm nghi ngờ của lượt chạy trung thực; `compute_caught_attack_count` đếm tấn công vượt ngưỡng bằng `>` cho khớp cách tính ngưỡng; `scale_usefulness` chuẩn hóa theo baseline mô hình tin cậy và không tin cậy.<br>- Xây trên Inspect AI (mỏng) nên dùng chung sandbox Docker/Kubernetes, log và viewer.<br>- Mục 'Avoiding Data Contamination' đề nghị không đăng lời giải trần, không đưa dữ liệu eval cho dịch vụ có thể huấn luyện. |
| Tiêu chí và cách kiểm | Số đo an toàn và hữu ích tính được bằng máy từ log, có kiểm lược đồ DataFrame bằng pandera và báo NaN. CI `checks.yml` chạy kiểm license, pyright, ruff, pytest song song (cả backend trio) (đã mở workflow); các eval đầy đủ cần Docker và khóa mô hình, chưa chạy. |
| Giới hạn và rủi ro | Thư viện nghiên cứu, kết quả phụ thuộc mô hình giám sát và cấu hình; không phải bộ đo an toàn hoàn chỉnh. LGPL-3.0 chỉ ở phụ thuộc (đọc điều kiện khi đóng gói). README viết THIRD-PARTY-LICENSES nhưng tên file thật là THIRD_PARTY_LICENSES.md. Cần Docker (và Kubernetes cho setting infra) cùng khóa API nhiều nhà cung cấp. |
| So với | inspect-ai (nền, hồ sơ có sẵn), inspect-evals (bộ benchmark thông thường, không có giao thức giám sát), agentdojo (tấn công prompt injection cho agent). |
| Nguồn | [README.md](https://github.com/UKGovernmentBEIS/control-arena/blob/2c32268f8ea38eb94d66f61a83e0be01fd69c0c9/README.md) · [LICENSE](https://github.com/UKGovernmentBEIS/control-arena/blob/2c32268f8ea38eb94d66f61a83e0be01fd69c0c9/LICENSE) · [THIRD_PARTY_LICENSES.md](https://github.com/UKGovernmentBEIS/control-arena/blob/2c32268f8ea38eb94d66f61a83e0be01fd69c0c9/THIRD_PARTY_LICENSES.md) · [pyproject.toml](https://github.com/UKGovernmentBEIS/control-arena/blob/2c32268f8ea38eb94d66f61a83e0be01fd69c0c9/pyproject.toml) · [_metrics.py](https://github.com/UKGovernmentBEIS/control-arena/blob/2c32268f8ea38eb94d66f61a83e0be01fd69c0c9/control_arena/analysis/_metrics.py) · [checks.yml](https://github.com/UKGovernmentBEIS/control-arena/blob/2c32268f8ea38eb94d66f61a83e0be01fd69c0c9/.github/workflows/checks.yml) |

<a id="n2-2026-11-24"></a>

## Nâng trần đợt hai — 23/11/2026

Hồ sơ lập trong đợt nâng trần thứ hai: đọc mã hoặc tài liệu tại commit cố định, chưa chạy upstream; mô tả của trinh sát sai ở nhiều repo nên điều ghi ở đây là điều đã đọc.

<a id="n2-reviewbench-kylesau"></a>

### reviewbench (KyleSau)

| Thuộc tính | Giá trị |
|---|---|
| Repo | https://github.com/KyleSau/reviewbench |
| License | MIT (Kyle Saunders, 2026) |
| Phiên bản đã đọc | `71104b4a30010e05dd71cabcf724e006f52408e3` (commit 2026-10-13) |
| Kiểm chứng | 2026-11-24; code-read; đã đọc LICENSE, README, pyproject, ci.yml, gate.py, metrics.py, matching.py, rubric, một ca nhãn và baseline; chưa chạy upstream |
| Khoảng trống lấp | Code review agent có đo precision/recall |
| Cơ chế đáng học | - `matching.py`: khớp một-một theo file, khoảng dòng nới `--line-tolerance` (mặc định 3) và loại lỗi; comment thứ hai về cùng lỗi tính là false positive.<br>- `metrics.py`: TP/FP/FN tổng và theo loại lỗi, khoảng Wilson 95%, Cohen kappa giữa matcher và judge; chỉ chấm ca có trạng thái ok, mẫu số 0 hiện n/a.<br>- `gate.py`: so run với baseline, bắt buộc cùng dataset fingerprint và cùng line tolerance, giới hạn số ca không chấm được, rồi mới xét mức tụt recall/precision.<br>- Reviewer `oracle` (phải đạt 100%) và `null` (phải 0 recall) làm tự kiểm bộ đo. |
| Tiêu chí và cách kiểm | Gate CI: `--max-recall-drop 0.05 --max-precision-drop 0.05`, exit 1 khi vi phạm. `ci.yml` chạy ruff, pytest ngoại tuyến (mock client Claude), chạy reviewer heuristic rồi gate với `baselines/heuristic.json`; job Claude chỉ chạy trên main hoặc thủ công khi có secret API. Kiểm bằng máy, nhưng chỉ có số heuristic (precision 92,3%, recall 57,1%, theo README) và chưa có số mô hình thật. |
| Giới hạn và rủi ro | Quy mô nhỏ và tác giả viết cả luật heuristic lẫn dataset nên số optimistic (README tự nhận). Chạy reviewer/judge Claude gửi diff và nhãn ra API Anthropic bằng `ANTHROPIC_API_KEY` và tốn tiền. Dự án rất mới, 1 sao, một tác giả. Tên model mặc định trong README là tuyên bố của tác giả (chưa xác minh). |
| So với | open-code-review-ocr, code-review-graph, inspect-ai |
| Nguồn | [README.md](https://github.com/KyleSau/reviewbench/blob/71104b4a30010e05dd71cabcf724e006f52408e3/README.md) · [LICENSE](https://github.com/KyleSau/reviewbench/blob/71104b4a30010e05dd71cabcf724e006f52408e3/LICENSE) · [pyproject.toml](https://github.com/KyleSau/reviewbench/blob/71104b4a30010e05dd71cabcf724e006f52408e3/pyproject.toml) · [ci.yml](https://github.com/KyleSau/reviewbench/blob/71104b4a30010e05dd71cabcf724e006f52408e3/.github/workflows/ci.yml) · [gate.py](https://github.com/KyleSau/reviewbench/blob/71104b4a30010e05dd71cabcf724e006f52408e3/src/reviewbench/gate.py) · [metrics.py](https://github.com/KyleSau/reviewbench/blob/71104b4a30010e05dd71cabcf724e006f52408e3/src/reviewbench/metrics.py) · [matching.py](https://github.com/KyleSau/reviewbench/blob/71104b4a30010e05dd71cabcf724e006f52408e3/src/reviewbench/matching.py) · [match_rubric.md](https://github.com/KyleSau/reviewbench/blob/71104b4a30010e05dd71cabcf724e006f52408e3/rubrics/match_rubric.md) · [py-payment-webhook.json](https://github.com/KyleSau/reviewbench/blob/71104b4a30010e05dd71cabcf724e006f52408e3/datasets/v1/cases/py-payment-webhook.json) · [heuristic.json](https://github.com/KyleSau/reviewbench/blob/71104b4a30010e05dd71cabcf724e006f52408e3/baselines/heuristic.json) |

<a id="n2-rbench-decadance"></a>

### rbench (decadance-dance)

| Thuộc tính | Giá trị |
|---|---|
| Repo | https://github.com/decadance-dance/rbench |
| License | Apache-2.0 (LICENSE đầy đủ); dữ liệu task nhập từ ReviewBench (MIT, theo design.md) và nguồn của các repo gốc, mỗi nguồn có license riêng |
| Phiên bản đã đọc | `f423387ae98812e944dc19ef4a939d76adb89a2d` (commit 2026-11-21) |
| Kiểm chứng | 2026-11-24; code-read; đã đọc LICENSE, README, ci.yml, bin/check, design.md (D1), spec review-scoring, cli.py, hermetic.py, tasks/reviewbench.py, tasks/license.py, proxy allowlist, engines/code-review.toml, matrices/smoke.toml, manifest task; chưa chạy upstream |
| Khoảng trống lấp | Code review agent có đo precision/recall |
| Cơ chế đáng học | - `design.md` D1: nhập 25 PR kiểm thử từ ReviewBench ghim ở commit cụ thể, ánh xạ finding `tp` thành ground truth với mức must/should/nit, bỏ `fp`; bộ khớp many-to-many do judge ghim model, effort, hash prompt.<br>- `trial/hermetic.py` và `images/proxy/allowlist`: container agent chỉ ra được host API/auth của nhà cung cấp qua squid (danh sách host chính xác, cờ `-n` chống CONNECT theo IP), policy CLI do managed settings áp.<br>- `tasks/license.py`: chỉ đóng gói nguồn khi license repo gốc tại head nằm trong danh sách cho phép (MIT, Apache-2.0, BSD, ISC, MPL, GPL, LGPL, AGPL); không nhận diện được thì từ chối.<br>- `bin/check` và pre-push: cấm id/canary của task ẩn lọt vào file, đường dẫn hay commit; `runs/` không được theo dõi. |
| Tiêu chí và cách kiểm | Spec nêu metric theo trial: recall riêng must/should/nit, precision có nền và tăng cường, số false finding và nit, token từng model, thời gian; báo cáo có khoảng bootstrap 95% theo task. Cổng merge `ci-ok` chạy `bin/check` (guard công bố, ruff format, ruff check, pytest, 68 file trong `tests/`) bằng `uv --locked`. Mã thoát CLI: 0, 1, 2, 75 (dừng ở ngân sách vòng hoặc giới hạn). Chưa có kết quả benchmark công bố trong repo (chưa xác minh bất kỳ số đo nào). |
| Giới hạn và rủi ro | Trạng thái thiết kế/khung: README nói lệnh còn là skeleton dù `src/` đã có executor, ledger và plan; một số lệnh in 'not implemented yet'. Chạy thật cần Docker, đăng nhập Claude/Codex và ngân sách giới hạn gói; task ẩn nằm ngoài repo. Độ chính xác của judge phụ thuộc model ghim; precision không so sánh được với ReviewBench vì bỏ mục `fp`. Rất mới, 0 sao. |
| So với | reviewbench-kylesau, crbugbench, harbor-terminal-bench |
| Nguồn | [README.md](https://github.com/decadance-dance/rbench/blob/f423387ae98812e944dc19ef4a939d76adb89a2d/README.md) · [LICENSE](https://github.com/decadance-dance/rbench/blob/f423387ae98812e944dc19ef4a939d76adb89a2d/LICENSE) · [ci.yml](https://github.com/decadance-dance/rbench/blob/f423387ae98812e944dc19ef4a939d76adb89a2d/.github/workflows/ci.yml) · [check](https://github.com/decadance-dance/rbench/blob/f423387ae98812e944dc19ef4a939d76adb89a2d/bin/check) · [design.md](https://github.com/decadance-dance/rbench/blob/f423387ae98812e944dc19ef4a939d76adb89a2d/openspec/changes/add-rbench-benchmark/design.md) · [spec.md](https://github.com/decadance-dance/rbench/blob/f423387ae98812e944dc19ef4a939d76adb89a2d/openspec/changes/add-rbench-benchmark/specs/review-scoring/spec.md) · [cli.py](https://github.com/decadance-dance/rbench/blob/f423387ae98812e944dc19ef4a939d76adb89a2d/src/rbench/cli.py) · [hermetic.py](https://github.com/decadance-dance/rbench/blob/f423387ae98812e944dc19ef4a939d76adb89a2d/src/rbench/trial/hermetic.py) · [reviewbench.py](https://github.com/decadance-dance/rbench/blob/f423387ae98812e944dc19ef4a939d76adb89a2d/src/rbench/tasks/reviewbench.py) · [license.py](https://github.com/decadance-dance/rbench/blob/f423387ae98812e944dc19ef4a939d76adb89a2d/src/rbench/tasks/license.py) · [allowlist](https://github.com/decadance-dance/rbench/blob/f423387ae98812e944dc19ef4a939d76adb89a2d/images/proxy/allowlist) · [code-review.toml](https://github.com/decadance-dance/rbench/blob/f423387ae98812e944dc19ef4a939d76adb89a2d/engines/code-review.toml) · [smoke.toml](https://github.com/decadance-dance/rbench/blob/f423387ae98812e944dc19ef4a939d76adb89a2d/matrices/smoke.toml) · [manifest.json](https://github.com/decadance-dance/rbench/blob/f423387ae98812e944dc19ef4a939d76adb89a2d/tasks/reviewbench/manifest.json) |

<a id="n2-crbugbench"></a>

### CRBugBench

| Thuộc tính | Giá trị |
|---|---|
| Repo | https://github.com/malusamayo/CRBugBench |
| License | Không có file LICENSE trong repo (license null); các diff và đề bài trích từ 98 repo bên thứ ba với license riêng, chưa kiểm từng cái |
| Phiên bản đã đọc | `e8e585ee2a9bfa19002103d9a2bddaeb7aca49f8` (commit 2026-10-07) |
| Kiểm chứng | 2026-11-24; code-read; đã đọc README, scripts/run.py, summarize.py, tasks/index.json, một task đủ bộ (task.toml, instruction.md, test.sh, llm_judge.py, judge_runtime.py, judge_common.py, ground_truth.json, Dockerfile); chưa chạy upstream |
| Khoảng trống lấp | Code review agent có đo precision/recall (ở đây chỉ đo recall) |
| Cơ chế đáng học | - `environment/Dockerfile`: checkout base commit, gỡ remote, xóa ref, bỏ `.promisor`, `git repack` và `prune`, rồi build fail nếu số commit mồ côi khác số commit tới được từ HEAD (cơ chế chống rò đáp án).<br>- `tests/llm_judge.py` + `judge_runtime.py`: mỗi ca ground truth được hỏi từng judge (mặc định gpt-5.5, claude-opus-4.8, gemini-3.5-flash qua Copilot CLI); `strict` là 1 khi verdict 'yes', `lenient` cộng 'partial'.<br>- Hai track: `fix` (PR gây lỗi, đáp án là issue của bản sửa sau) và `comments` (lỗi mà reviewer người đã chỉ ra).<br>- `scripts/summarize.py`: gom theo track gồm detected, lenient, và any (ít nhất một lần thử bắt được). |
| Tiêu chí và cách kiểm | Reward = trung bình `strict` trên các ca của task; file test.sh chạy judge và ghi `reward.json`, `judge_details.json`. `judge_agreement` được báo cáo. Không có CI, không có test cho script (không thấy `.github`). Ca có review rỗng chấm 0; trả lời judge không parse được thành 'no'. |
| Giới hạn và rủi ro | Không có license nên chưa rõ quyền dùng/phân phối lại; nội dung nhúng mã bên thứ ba. Cần Docker, Harbor, khoảng 650 GB đĩa cho toàn bộ và tới 19 GB mỗi repo. Review và ground truth được gửi tới model judge qua GitHub Copilot (cần `GITHUB_TOKEN`), nên dữ liệu rời máy. Không đo false positive nên reviewer nói thật nhiều vẫn điểm cao. Tên model trong README và tên 'gpt-6-luna' là cấu hình của tác giả (chưa xác minh tồn tại). |
| So với | reviewbench-kylesau, rbench-decadance, swe-bench-harness |
| Nguồn | [README.md](https://github.com/malusamayo/CRBugBench/blob/e8e585ee2a9bfa19002103d9a2bddaeb7aca49f8/README.md) · [run.py](https://github.com/malusamayo/CRBugBench/blob/e8e585ee2a9bfa19002103d9a2bddaeb7aca49f8/scripts/run.py) · [summarize.py](https://github.com/malusamayo/CRBugBench/blob/e8e585ee2a9bfa19002103d9a2bddaeb7aca49f8/scripts/summarize.py) · [index.json](https://github.com/malusamayo/CRBugBench/blob/e8e585ee2a9bfa19002103d9a2bddaeb7aca49f8/tasks/index.json) · [task.toml](https://github.com/malusamayo/CRBugBench/blob/e8e585ee2a9bfa19002103d9a2bddaeb7aca49f8/tasks/Files_comment10921/task.toml) · [instruction.md](https://github.com/malusamayo/CRBugBench/blob/e8e585ee2a9bfa19002103d9a2bddaeb7aca49f8/tasks/Files_comment10921/instruction.md) · [test.sh](https://github.com/malusamayo/CRBugBench/blob/e8e585ee2a9bfa19002103d9a2bddaeb7aca49f8/tasks/Files_comment10921/tests/test.sh) · [llm_judge.py](https://github.com/malusamayo/CRBugBench/blob/e8e585ee2a9bfa19002103d9a2bddaeb7aca49f8/tasks/Files_comment10921/tests/llm_judge.py) · [judge_runtime.py](https://github.com/malusamayo/CRBugBench/blob/e8e585ee2a9bfa19002103d9a2bddaeb7aca49f8/tasks/Files_comment10921/tests/judge_runtime.py) · [judge_common.py](https://github.com/malusamayo/CRBugBench/blob/e8e585ee2a9bfa19002103d9a2bddaeb7aca49f8/tasks/Files_comment10921/tests/judge_common.py) · [ground_truth.json](https://github.com/malusamayo/CRBugBench/blob/e8e585ee2a9bfa19002103d9a2bddaeb7aca49f8/tasks/Files_comment10921/tests/ground_truth.json) · [Dockerfile](https://github.com/malusamayo/CRBugBench/blob/e8e585ee2a9bfa19002103d9a2bddaeb7aca49f8/tasks/Files_comment10921/environment/Dockerfile) |

<a id="n2-ares-rag-eval"></a>

### ARES

| Thuộc tính | Giá trị |
|---|---|
| Repo | https://github.com/stanford-futuredata/ARES |
| License | Apache-2.0 |
| Phiên bản đã đọc | `c7c9018a755faf8347c4da415632bae1593ef104` (commit 2025-03-28) |
| Kiểm chứng | 2026-11-24; code-read; đã đọc README.md, LICENSE, pyproject.toml, CHANGELOG.md và một số file khác; chưa chạy upstream |
| Khoảng trống lấp | Đánh giá RAG tách context relevance, answer faithfulness, answer relevance, có khoảng tin cậy thống kê |
| Cơ chế đáng học | • Chấm ba tiêu chí tách riêng bằng judge: few-shot LLM (`ues_idp.py`, hàm `few_shot_*_scoring` cho OpenAI/Azure/Together/Claude/vLLM) hoặc bộ phân loại tinh chỉnh (`LLMJudge_RAG_Compared_Scoring.py`).<br>• Hiệu chuẩn bằng prediction-powered inference: `calculate_ppi` trộn tập nhãn người nhỏ với dự đoán judge trên tập lớn, trả khoảng tin cậy PPI so với khoảng cổ điển và khoảng chỉ-judge (`ppi.py`, `pp_mean_iid_asymptotic`, `binomial_iid`).<br>• Sinh truy vấn/đáp án tổng hợp từ tài liệu thật để huấn luyện judge (README, nhánh `synthetic_query_generator` trong `ares.py`). |
| Tiêu chí và cách kiểm | Cần tập kiểm chứng có nhãn người (README: ít nhất 50 mẫu, nên vài trăm) và few-shot mẫu; mặc định `alpha` 0.05, `num_trials` 1000 (ares.py). Không có thư mục test và không có workflow CI trong repo, nên độ đúng của mã không có kiểm máy tại upstream. |
| Giới hạn và rủi ro | Commit cuối 2025-03-28, không workflow, không test. Mâu thuẫn metadata: LICENSE là Apache-2.0 nhưng classifier trong `pyproject.toml` ghi MIT; badge README ghi v0.5.7 còn `pyproject.toml` ghi 0.6.6. Dùng judge API (OpenAI, Together, Anthropic, Azure) nghĩa là câu hỏi, tài liệu và câu trả lời rời máy. Số sao 739 trinh sát lấy từ web, chưa xác minh. Độ chính xác khẳng định trong paper (chưa xác minh). |
| So với | ragas, ragas-rag-metrics (chấm điểm trực tiếp không hiệu chuẩn), deepeval, lm-evaluation-harness |
| Nguồn | [README.md](https://github.com/stanford-futuredata/ARES/blob/c7c9018a755faf8347c4da415632bae1593ef104/README.md) · [LICENSE](https://github.com/stanford-futuredata/ARES/blob/c7c9018a755faf8347c4da415632bae1593ef104/LICENSE) · [pyproject.toml](https://github.com/stanford-futuredata/ARES/blob/c7c9018a755faf8347c4da415632bae1593ef104/pyproject.toml) · [CHANGELOG.md](https://github.com/stanford-futuredata/ARES/blob/c7c9018a755faf8347c4da415632bae1593ef104/CHANGELOG.md) · [ares.py](https://github.com/stanford-futuredata/ARES/blob/c7c9018a755faf8347c4da415632bae1593ef104/ares/ares.py) · [ues_idp.py](https://github.com/stanford-futuredata/ARES/blob/c7c9018a755faf8347c4da415632bae1593ef104/ares/ues_idp.py) · [rag_scoring.py](https://github.com/stanford-futuredata/ARES/blob/c7c9018a755faf8347c4da415632bae1593ef104/ares/rag_scoring.py) · [ppi.py](https://github.com/stanford-futuredata/ARES/blob/c7c9018a755faf8347c4da415632bae1593ef104/ares/RAG_Automatic_Evaluation/ppi.py) · [LLMJudge_RAG_Compared_Scoring.py](https://github.com/stanford-futuredata/ARES/blob/c7c9018a755faf8347c4da415632bae1593ef104/ares/RAG_Automatic_Evaluation/LLMJudge_RAG_Compared_Scoring.py) |

<a id="n2-mlperf-inference"></a>

### MLPerf Inference (reference và LoadGen)

| Thuộc tính | Giá trị |
|---|---|
| Repo | https://github.com/mlcommons/inference |
| License | Apache-2.0 |
| Phiên bản đã đọc | `3fbc329939999c13d0a7b5e67fb2092287e06047` (commit 2026-09-02) |
| Kiểm chứng | 2026-11-24; code-read; đã đọc README.md, LICENSE.md, loadgen/README.md, loadgen/test_settings.h và một số file khác; chưa chạy upstream |
| Khoảng trống lấp | Benchmark tải và hiệu năng suy luận theo chuẩn công khai (LoadGen, kịch bản, bộ kiểm nộp bài) |
| Cơ chế đáng học | • LoadGen là thư viện C++ có binding Python, không biết model hay dữ liệu, chỉ sinh lưu lượng theo bốn kịch bản `SingleStream`, `MultiStream`, `Server`, `Offline` và ghi log để kiểm (loadgen/README.md, test_settings.h).<br>• Ràng buộc hợp lệ nằm ở `mlperf.conf`: `target_latency_percentile` (90 hoặc 99), `min_duration` 600000 ms, `min_query_count` theo từng model; `early_stopping` tính số truy vấn tối thiểu cần qua.<br>• `tools/submission` có bộ kiểm bài nộp (log parser, truncate accuracy log, submission_checker) kiểm độ chính xác, ràng buộc độ trễ, cấu trúc thư mục. |
| Tiêu chí và cách kiểm | Kiểm bằng máy: LoadGen tự báo kết quả có thỏa ràng buộc không; submission checker rà log. Workflow `test-loadgen.yml` build LoadGen qua mlc-scripts trên Python 3.8 đến 3.13 khi PR đổi `loadgen/`; `test-submission-checker.yml` nhắm nhánh `master_off` và `dev_off` nên trên thực tế đang tắt cho PR. Luật chính thức ở repo `inference_policies` riêng (README loadgen: lệch với policy là bug). |
| Giới hạn và rủi ro | Mã tham chiếu không tối ưu và không đại diện hiệu năng nhà sản xuất; submitter không được sửa C++ của LoadGen. Chạy đầy đủ cần phần cứng, dataset lớn và nhiều model gated. Một số thư mục con có license riêng (language/gpt-j, retired_benchmarks). Mục tiêu hiện tại gồm cả model rất lớn (llama2-70b, deepseek-r1, qwen3-vl-235b). Mô tả trinh sát gọn đúng nhưng không nêu đây chủ yếu là bộ quy trình nộp bài. |
| So với | guidellm (đo tải server LLM thực tế), mteb, lm-evaluation-harness |
| Nguồn | [README.md](https://github.com/mlcommons/inference/blob/3fbc329939999c13d0a7b5e67fb2092287e06047/README.md) · [LICENSE.md](https://github.com/mlcommons/inference/blob/3fbc329939999c13d0a7b5e67fb2092287e06047/LICENSE.md) · [README.md](https://github.com/mlcommons/inference/blob/3fbc329939999c13d0a7b5e67fb2092287e06047/loadgen/README.md) · [test_settings.h](https://github.com/mlcommons/inference/blob/3fbc329939999c13d0a7b5e67fb2092287e06047/loadgen/test_settings.h) · [early_stopping.h](https://github.com/mlcommons/inference/blob/3fbc329939999c13d0a7b5e67fb2092287e06047/loadgen/early_stopping.h) · [mlperf.conf](https://github.com/mlcommons/inference/blob/3fbc329939999c13d0a7b5e67fb2092287e06047/mlperf.conf) · [README.md](https://github.com/mlcommons/inference/blob/3fbc329939999c13d0a7b5e67fb2092287e06047/tools/submission/README.md) · [test-loadgen.yml](https://github.com/mlcommons/inference/blob/3fbc329939999c13d0a7b5e67fb2092287e06047/.github/workflows/test-loadgen.yml) · [test-submission-checker.yml](https://github.com/mlcommons/inference/blob/3fbc329939999c13d0a7b5e67fb2092287e06047/.github/workflows/test-submission-checker.yml) |

<a id="n2-ailuminate"></a>

### AILuminate (bộ prompt demo)

| Thuộc tính | Giá trị |
|---|---|
| Repo | https://github.com/mlcommons/ailuminate |
| License | Apache-2.0 (LICENSE.md); dữ liệu CC BY 4.0 theo README |
| Phiên bản đã đọc | `769cc2be9d20c8d4fb26ce53b68865ed41dfb8e2` (commit 2025-06-11) |
| Kiểm chứng | 2026-11-24; docs-read; đã đọc README.md, LICENSE.md, AILuminate Naming and Versioning.md, airr_official_1.0_demo_en_us_prompt_set_release.csv và một số file khác; chưa chạy upstream |
| Khoảng trống lấp | Bộ dữ liệu benchmark an toàn LLM theo phân loại nguy cơ (không có mã chạy) |
| Cơ chế đáng học | • Repo chỉ chứa dữ liệu và tài liệu: hai file CSV demo en_US và fr_FR, mỗi file 1200 prompt với cột `release_prompt_id`, `prompt_text`, `hazard`, `persona`, `locale`, `prompt_hash`.<br>• Phân loại nguy cơ theo mã `hazard` (vcr, src, cse, ssh, iwp, ipv, dfm, ncr, hte, prv, spc_*, sxc_prn); tôi đếm trong CSV có 15 mã, 100 prompt mỗi mã trong bản en_US.<br>• Quy ước đặt tên và đánh phiên bản benchmark (AILuminate Naming and Versioning.md): tên, ngôn ngữ BCP 47, semver, loại phát hành. |
| Tiêu chí và cách kiểm | Không có script hay test trong repo; workflow duy nhất là CLA bot. Bộ prompt chính thức 12000 prompt thực hành chỉ cấp cho thành viên MLCommons và bộ evaluator ensemble không nằm trong repo; công cụ chạy là `modelbench` ở repo riêng (README, chưa mở). Demo là mẫu 10% của tập practice (README). |
| Giới hạn và rủi ro | Mô tả trinh sát sai ở một điểm: không có mã Apache nào để dùng, chỉ có LICENSE.md Apache-2.0 cạnh dữ liệu CC BY 4.0 theo README, hai bên không khớp nên cần ghi rõ khi trích dữ liệu. README nói 12 nhóm hazard nhưng bảng của chính nó liệt kê 14 mã và CSV có 15 (thêm `spc_lgl`). Persona trong schema có normal nhưng demo en_US chỉ có skilled và unskilled (600 mỗi loại). Id trong file demo mang tiền tố `airr_practice_1_0_`. Dữ liệu chứa nội dung độc hại, gồm đề tài bóc lột trẻ em, cần cảnh báo và hạn chế người đọc. Chỉ có tiếng Anh và Pháp, không có tiếng Việt. |
| So với | garak (red team tự động), inspect-evals, deepeval, nemo-guardrails |
| Nguồn | [README.md](https://github.com/mlcommons/ailuminate/blob/769cc2be9d20c8d4fb26ce53b68865ed41dfb8e2/README.md) · [LICENSE.md](https://github.com/mlcommons/ailuminate/blob/769cc2be9d20c8d4fb26ce53b68865ed41dfb8e2/LICENSE.md) · [AILuminate Naming and Versioning.md](https://github.com/mlcommons/ailuminate/blob/769cc2be9d20c8d4fb26ce53b68865ed41dfb8e2/AILuminate%20Naming%20and%20Versioning.md) · [airr_official_1.0_demo_en_us_prompt_set_release.csv](https://github.com/mlcommons/ailuminate/blob/769cc2be9d20c8d4fb26ce53b68865ed41dfb8e2/airr_official_1.0_demo_en_us_prompt_set_release.csv) · [airr_official_1.0_demo_fr_fr_prompt_set_release.csv](https://github.com/mlcommons/ailuminate/blob/769cc2be9d20c8d4fb26ce53b68865ed41dfb8e2/airr_official_1.0_demo_fr_fr_prompt_set_release.csv) · [cla.yml](https://github.com/mlcommons/ailuminate/blob/769cc2be9d20c8d4fb26ce53b68865ed41dfb8e2/.github/workflows/cla.yml) |

<a id="n2-evalview"></a>

### EvalView

| Thuộc tính | Giá trị |
|---|---|
| Repo | https://github.com/hidai25/eval-view |
| License | Apache-2.0 |
| Phiên bản đã đọc | `ed2d312d812f4fd82bb7881b29432f752b02823e` (commit 2026-11-20) |
| Kiểm chứng | 2026-11-24; code-read; đã đọc README, LICENSE, pyproject, action.yml, `core/diff.py`, `core/config.py`, `core/chaos.py`, `telemetry/client.py`, skill run-eval, ci.yml; chưa chạy upstream |
| Khoảng trống lấp | Eval trajectory và regression cho agent/skill: snapshot hành vi rồi diff (khoảng trống của kho) |
| Cơ chế đáng học | • Vòng `evalview snapshot` rồi `evalview check`: ghi lại baseline (công cụ gọi, thứ tự, tham số, đầu ra) và diff toàn trajectory — README.md.<br>• `DiffEngine` trả bốn trạng thái PASSED, TOOLS_CHANGED, OUTPUT_CHANGED, REGRESSION; so tool theo ngưỡng tương đồng (mặc định 0.8), so đầu ra tương đồng từ vựng (cờ khi dưới 0.95), điểm tụt quá `score_regression_threshold` thì REGRESSION; có `forbidden_tool` — `core/diff.py`, `core/config.py`.<br>• Phần diff tool/thứ tự chạy offline, không cần khoá API; LLM judge chỉ bật khi muốn chấm chất lượng (README, cần lưu ý chạy agent vẫn tốn chi phí backend).<br>• `core/chaos.py`: chèn nhiễu có seed (tool_failure ở lần gọi thứ N, latency_spike, goal_interruption) để mô phỏng người dùng/công cụ thất thường, lặp lại được.<br>• GitHub Action `action.yml`: `fail-on` mặc định `REGRESSION`, `strict` đổi thành fail mọi thay đổi. |
| Tiêu chí và cách kiểm | Ngưỡng cấu hình được trong `diff:` của config (ví dụ docstring: tool 0.85, output 0.92, score 3.0); kiểm bằng máy (diff xác định) cộng judge tùy chọn. CI của repo chạy pytest ma trận Python 3.9 đến 3.12 trừ test cần khoá API, có lint/typecheck; có workflow dogfood. Chưa chạy. |
| Giới hạn và rủi ro | Telemetry mặc định BẬT: CLI gửi sự kiện ẩn danh tới PostHog (ID cài đặt ngẫu nhiên, phiên bản, lệnh, môi trường CI, kết quả gộp); tắt bằng `EVALVIEW_TELEMETRY_DISABLED=1` hoặc `evalview telemetry off` — `telemetry/client.py` có gửi thuộc tính hệ điều hành và Python. Số sao 142 là số web của trinh sát (chưa xác minh). Dự án trẻ (0.9.x), tuyên bố trong README về tác dụng phát hiện hồi quy là của tác giả (chưa xác minh bằng benchmark độc lập). |
| So với | [AgentEvals](03-agentic-patterns-loops/README.md#factory-trajectory-oracles-2026-11-04) (so trajectory bằng LangChain) · [NVIDIA SkillEvaluator](20-claude-plugins-ecosystem/README.md#ch-nvidia-skillevaluator) · [agent-skills-eval](20-claude-plugins-ecosystem/README.md#ch-agent-skills-eval) |
| Nguồn | [README.md](https://github.com/hidai25/eval-view/blob/ed2d312d812f4fd82bb7881b29432f752b02823e/README.md) · [LICENSE](https://github.com/hidai25/eval-view/blob/ed2d312d812f4fd82bb7881b29432f752b02823e/LICENSE) · [pyproject.toml](https://github.com/hidai25/eval-view/blob/ed2d312d812f4fd82bb7881b29432f752b02823e/pyproject.toml) · [action.yml](https://github.com/hidai25/eval-view/blob/ed2d312d812f4fd82bb7881b29432f752b02823e/action.yml) · [diff.py](https://github.com/hidai25/eval-view/blob/ed2d312d812f4fd82bb7881b29432f752b02823e/evalview/core/diff.py) · [config.py](https://github.com/hidai25/eval-view/blob/ed2d312d812f4fd82bb7881b29432f752b02823e/evalview/core/config.py) · [chaos.py](https://github.com/hidai25/eval-view/blob/ed2d312d812f4fd82bb7881b29432f752b02823e/evalview/core/chaos.py) · [client.py](https://github.com/hidai25/eval-view/blob/ed2d312d812f4fd82bb7881b29432f752b02823e/evalview/telemetry/client.py) · [SKILL.md](https://github.com/hidai25/eval-view/blob/ed2d312d812f4fd82bb7881b29432f752b02823e/skills/run-eval/SKILL.md) · [ci.yml](https://github.com/hidai25/eval-view/blob/ed2d312d812f4fd82bb7881b29432f752b02823e/.github/workflows/ci.yml) |

<a id="n2-sanityharness"></a>

### SanityHarness

| Thuộc tính | Giá trị |
|---|---|
| Repo | https://github.com/lemon07r/SanityHarness |
| License | không có file LICENSE |
| Phiên bản đã đọc | `388b18dbeac8062e36fbae4d4d775c9f14fa9d7b` (commit 2026-10-17) |
| Kiểm chứng | 2026-11-24; code-read; đã đọc README, go.mod, docs/SCORING.md, `internal/task/weight.go`, release.yml, docker.yml; chưa chạy upstream |
| Khoảng trống lấp | Đánh giá coding agent bằng harness tái lập, chạy trong container |
| Cơ chế đáng học | • Mỗi task chạy trong Docker riêng; 26 task, 6 ngôn ngữ (Go, Rust, TypeScript, Kotlin, Dart, Zig); 19 agent dựng sẵn; bubblewrap tùy chọn để giam agent trong workspace — README.md.<br>• Điểm có trọng số: weight = 1,0 cộng các hệ số độ khó (ngôn ngữ hiếm, tính năng đặc thù, thuật toán mới, mật độ ca biên, bài toán mới), trần 1,5 — `docs/SCORING.md`, `internal/task/weight.go`.<br>• Toàn vẹn: agent sửa file test hoặc file hỗ trợ thì status `integrity_violation` và bị trừ 0,25; kiểm bằng BLAKE3; test ẩn chỉ áp lúc chấm (có chế độ `--legacy` lộ test ẩn) — README, `docs/SCORING.md`, đoạn import `blake3` trong `internal/cli/eval.go` (xác nhận bằng grep).<br>• `sanity eval --resume` chạy tiếp đợt bị gián đoạn, `--parallel` chạy song song, có `verify` kiểm bằng chứng nộp. |
| Tiêu chí và cách kiểm | Kiểm bằng máy: pass (kể cả partial_pass khi hết giờ nhưng test đã qua) cho 100% trọng số task, fail 0, integrity_violation -0,25; trọng số là hệ số kinh nghiệm do tác giả hiệu chỉnh, không có kiểm định độc lập (chưa xác minh). Repo có test Go; `release.yml` chạy build, `go test -race`, vet và lint chỉ khi đẩy tag `v*`, `docker.yml` dựng ảnh khi đổi `containers/**`; badge CI trong README trỏ `ci.yml` không có ở commit này. |
| Giới hạn và rủi ro | Không có file LICENSE (kể cả go.mod không ghi): README chỉ ghi 'MIT License' nên về pháp lý chưa rõ, coi là chưa xác minh trước khi nhúng hoặc sao chép mã. Chạy agent thật cần Docker và khoá API của từng agent; cần cài Go, chưa chạy ở đây. Bộ chỉ 26 task nên độ phân biệt hạn chế; bubblewrap chỉ có trên Linux. Một tác giả, commit cuối 2026-10-17. |
| So với | [SWE-bench](01-ai-coding-agents/README.md#ch-swe-bench-harness) · [Harbor / Terminal-Bench](07-eval-observability/README.md) · [mini-SWE-agent](01-ai-coding-agents/README.md) |
| Nguồn | [README.md](https://github.com/lemon07r/SanityHarness/blob/388b18dbeac8062e36fbae4d4d775c9f14fa9d7b/README.md) · [go.mod](https://github.com/lemon07r/SanityHarness/blob/388b18dbeac8062e36fbae4d4d775c9f14fa9d7b/go.mod) · [SCORING.md](https://github.com/lemon07r/SanityHarness/blob/388b18dbeac8062e36fbae4d4d775c9f14fa9d7b/docs/SCORING.md) · [weight.go](https://github.com/lemon07r/SanityHarness/blob/388b18dbeac8062e36fbae4d4d775c9f14fa9d7b/internal/task/weight.go) · [release.yml](https://github.com/lemon07r/SanityHarness/blob/388b18dbeac8062e36fbae4d4d775c9f14fa9d7b/.github/workflows/release.yml) · [docker.yml](https://github.com/lemon07r/SanityHarness/blob/388b18dbeac8062e36fbae4d4d775c9f14fa9d7b/.github/workflows/docker.yml) |

<a id="n2-code-review-benchmark"></a>

### Code Review Bench (Martian)

| Thuộc tính | Giá trị |
|---|---|
| Repo | https://github.com/withmartian/code-review-benchmark |
| License | MIT |
| Phiên bản đã đọc | `23a35d0d64f7de5a68e5679da08414e0edacea9b` (commit 2026-11-20) |
| Kiểm chứng | 2026-11-24; code-read; đã đọc README.md, methodology/summary.md, offline/README.md, step3_judge_comments.py, golden_comments/sentry.json, LICENSE, tests.yml; chưa chạy upstream |
| Khoảng trống lấp | Đo chất lượng review và so sánh khung SDD: nền precision/recall cho code review có thể tái chạy |
| Cơ chế đáng học | - Golden comment có `severity` và `category` (bug, security, concurrency, perf, test_gap, style, speculative) trong `offline/golden_comments/*.json`; tổng 173 mục trên 50 PR (đếm bằng script tại commit này).<br>- Pipeline năm bước `step1_download_prs` đến `step3_judge_comments`: tải review của từng công cụ, tách ứng viên, dedup, rồi judge LLM trả JSON `match`/`confidence` cho từng cặp (`step3_judge_comments.py`).<br>- Precision = TP / số ứng viên, recall = TP / số golden (`step3_judge_comments.py`); README mô tả thêm profile Strict/Core/All và F-beta chỉnh được trong dashboard HTML.<br>- Nhánh online (`online/etl`): Discover, Enrich, Analyze rồi đối chiếu bot suggestion với commit sửa sau review để lấy precision/recall hành vi. |
| Tiêu chí và cách kiểm | Số liệu máy tính: precision, recall, F-beta (mặc định F2 trong dashboard). CI chạy `ruff check` và `pytest` cho offline và online ETL (`tests.yml`); test không cần mạng theo README. Judge dùng temperature 0 và lưu kết quả theo từng model judge (Opus 4.5, Sonnet 4.5, GPT-5.2 theo README, chưa xác minh bảng kết quả). |
| Giới hạn và rủi ro | - MIT. Judge gọi dịch vụ `api.withmartian.com` qua `MARTIAN_API_KEY` (diff và comment rời máy).<br>- Tuyên bố top 5 công cụ giống nhau giữa ba judge là của tác giả (chưa xác minh).<br>- Tập 50 PR cố định, dễ bị overfit; tiêu chí đưa công cụ lên bảng xếp hạng yêu cầu 600–1.000 PR công khai.<br>- Link `crb_full_methodology.md` trong `methodology/summary.md` không khớp tên file `full.md`. |
| So với | open-code-review-ocr, code-review-graph (cùng category code-review); swe-bench-live (eval cho coding agent, không phải review) |
| Nguồn | [README.md](https://github.com/withmartian/code-review-benchmark/blob/23a35d0d64f7de5a68e5679da08414e0edacea9b/README.md) · [LICENSE](https://github.com/withmartian/code-review-benchmark/blob/23a35d0d64f7de5a68e5679da08414e0edacea9b/LICENSE) · [summary.md](https://github.com/withmartian/code-review-benchmark/blob/23a35d0d64f7de5a68e5679da08414e0edacea9b/methodology/summary.md) · [README.md](https://github.com/withmartian/code-review-benchmark/blob/23a35d0d64f7de5a68e5679da08414e0edacea9b/offline/README.md) · [step3_judge_comments.py](https://github.com/withmartian/code-review-benchmark/blob/23a35d0d64f7de5a68e5679da08414e0edacea9b/offline/code_review_benchmark/step3_judge_comments.py) · [tests.yml](https://github.com/withmartian/code-review-benchmark/blob/23a35d0d64f7de5a68e5679da08414e0edacea9b/.github/workflows/tests.yml) · [sentry.json](https://github.com/withmartian/code-review-benchmark/blob/23a35d0d64f7de5a68e5679da08414e0edacea9b/offline/golden_comments/sentry.json) |

<a id="n2-ccusage"></a>

### ccusage

| Thuộc tính | Giá trị |
|---|---|
| Repo | https://github.com/ryoppippi/ccusage |
| License | MIT |
| Phiên bản đã đọc | `4c250b85befb657c024c55a1db7b846371639fcc` (commit 2026-11-24) |
| Kiểm chứng | 2026-11-24; code-read; đã đọc README.md, docs/guide/telemetry.md, cost-modes.md, telemetry.rs, cost.rs, AGENTS.md, ci.yaml, update-pricing.yaml, LICENSE; chưa chạy upstream |
| Khoảng trống lấp | Đo chi phí token/hạn mức của coding tool từ log cục bộ (mảng chi phí chưa có hồ sơ trong kho) |
| Cơ chế đáng học | - Mỗi nguồn là một adapter Rust riêng (`rust/adapters/<agent>`), phần tính chung ở `ccusage-core`; Claude Code dedupe theo `message.id` và `requestId` (thấy qua grep trong `rust/adapters/claude/src/tests.rs`, chưa đọc đủ).<br>- `cost.rs`: tính từ token với giá input, output, cache 5 phút, cache 1 giờ, cache đọc, bậc long-context và hệ số fast; bản ghi cost bằng 0 của một số nguồn bị coi là chưa ghi để tính lại từ token.<br>- Chế độ `--mode auto/calculate/display` (`docs/guide/cost-modes.md`) phân biệt chi phí lưu trong log với chi phí ước tính; ghi rõ không phải hoá đơn.<br>- Bảng giá nhúng từ snapshot LiteLLM và models.dev, workflow `update-pricing.yaml` làm mới hằng ngày; cờ `--offline` dùng snapshot. |
| Tiêu chí và cách kiểm | Kiểm bằng test Rust và workflow CI (`ci.yaml` có tirith scan và build đa nền tảng; chỉ đọc phần đầu file). Số liệu chi phí là ước tính từ log và bảng giá, không đối chiếu hoá đơn. Chưa chạy bản build nào. |
| Giới hạn và rủi ro | - MIT (cả `apps/ccusage/LICENSE`). Bản release chính thức gửi ping `cli_daily_active` mỗi ngày UTC (anonymousId ngẫu nhiên, version, os, arch, lệnh đầu tiên trong ngày); không gửi token, chi phí hay đường dẫn theo tài liệu. Tắt bằng `ccusage telemetry disable`, `CCUSAGE_TELEMETRY_DISABLED` hoặc `DO_NOT_TRACK`; tự tắt khi `CI` đặt; tự build bằng cargo không có endpoint (`telemetry.rs`, `telemetry.md`).<br>- Chạy qua `npx ccusage@latest` kéo mã mới mỗi lần; nên ghim phiên bản.<br>- Số liệu chỉ phản ánh log trên máy, thiếu nếu log bị xoá hoặc agent không ghi usage. |
| So với | opencost (chi phí hạ tầng, khác lớp), helicone và litellm (đo qua gateway thay vì log cục bộ), langfuse (tracing LLM) |
| Nguồn | [README.md](https://github.com/ryoppippi/ccusage/blob/4c250b85befb657c024c55a1db7b846371639fcc/README.md) · [LICENSE](https://github.com/ryoppippi/ccusage/blob/4c250b85befb657c024c55a1db7b846371639fcc/LICENSE) · [AGENTS.md](https://github.com/ryoppippi/ccusage/blob/4c250b85befb657c024c55a1db7b846371639fcc/AGENTS.md) · [telemetry.md](https://github.com/ryoppippi/ccusage/blob/4c250b85befb657c024c55a1db7b846371639fcc/docs/guide/telemetry.md) · [cost-modes.md](https://github.com/ryoppippi/ccusage/blob/4c250b85befb657c024c55a1db7b846371639fcc/docs/guide/cost-modes.md) · [telemetry.rs](https://github.com/ryoppippi/ccusage/blob/4c250b85befb657c024c55a1db7b846371639fcc/rust/crates/ccusage/src/telemetry.rs) · [cost.rs](https://github.com/ryoppippi/ccusage/blob/4c250b85befb657c024c55a1db7b846371639fcc/rust/crates/ccusage-core/src/cost.rs) · [ci.yaml](https://github.com/ryoppippi/ccusage/blob/4c250b85befb657c024c55a1db7b846371639fcc/.github/workflows/ci.yaml) · [update-pricing.yaml](https://github.com/ryoppippi/ccusage/blob/4c250b85befb657c024c55a1db7b846371639fcc/.github/workflows/update-pricing.yaml) |
