# 17 · Prompt Engineering, Prompt Optimization & System Prompt Collections

## 1. Hướng dẫn & tài nguyên

| Tài nguyên | Repo / URL | ★ | Ghi chú |
|---|---|---|---|
| **Prompt Engineering Guide** (DAIR.AI) | dair-ai/Prompt-Engineering-Guide | ~78–79k (9/2026) | Nay bao phủ cả context engineering, RAG, agents; promptingguide.ai |
| **Anthropic Prompt Library & docs** | docs.anthropic.com (prompt engineering, prompt generator, Claude cookbook) | – | Kỹ thuật XML tags, few-shot, chain-of-thought, prefill |
| **OpenAI Cookbook / Prompt guide** | openai/openai-cookbook | 76,6k (12/10/2026) | Xem §2b |
| **awesome-chatgpt-prompts** | f/awesome-chatgpt-prompts | – | Fatih Kadir Akın; prompts.chat |
| **Google Prompting guide (Gemini)** | – | – | |
| Learn Prompting | learnprompting.org | – | Khóa học mở |

## 2. Prompt optimization / "programming, not prompting"

| Dự án | Repo | ★ | Cách tiếp cận |
|---|---|---|---|
| **DSPy** (Stanford NLP) | stanfordnlp/dspy | ~38–39k (9/2026, v3.3.1) | Module hóa (Signature, Module), optimizer (BootstrapFewShot, MIPROv2, GEPA) tự tối ưu prompt/weights theo metric |
| TextGrad | zou-group/textgrad | – | "Gradient" bằng ngôn ngữ tự nhiên |
| Promptfoo | promptfoo/promptfoo | – | Đánh giá/so sánh prompt (mục 07) |
| LangSmith Hub, PromptLayer, Langfuse Prompts | – | – | Quản lý version prompt |
| awesome-dspy | ganarajpr/awesome-dspy | – | Tài nguyên DSPy |

## 2b. Structured output & thư viện lập trình LLM (đã xác minh 2026-10-12)

| Repo | ★ (12/10) | License | Hoạt động gần nhất | Vì sao chất lượng | Lưu ý |
|---|---|---|---|---|---|
| **567-labs/instructor** | 14,0k | MIT | commit 10/10/2026; v1.17.0 (9/9) | Output có cấu trúc kiểm bằng Pydantic, chạy với OpenAI, Anthropic, Google, Ollama; README nói hơn 3 triệu lượt tải/tháng | Retry khi validate lỗi đồng nghĩa thêm lượt gọi LLM và chi phí |
| **dottxt-ai/outlines** | 15,9k | Apache-2.0 | commit 24/8/2026; v1.3.3 (6/8) | Ràng buộc ngay lúc decode (JSON Schema, regex, grammar) nên output hợp lệ theo cấu trúc | Bảo đảm đầy đủ cần truy cập logit, tức model local **(chưa xác minh)** |
| **guidance-ai/guidance** | 21,8k | MIT | commit 21/5/2026; 0.3.2 (18/3) | Ngôn ngữ sinh có ràng buộc (`gen()` theo regex/grammar), tự "tua nhanh" các token mà grammar đã cố định | Chậm lại: không commit từ 5/2026 |
| **BoundaryML/baml** | 9,4k | Apache-2.0 | 0.22.0 (12/10/2026) | Ngôn ngữ có kiểu để viết "prompt function"; kiểu giữ ở runtime; gọi được từ TS, Python, Go, C#, Java | DSL mới + bước codegen; vẫn 0.x |
| **anthropics/claude-cookbooks** (trước là anthropic-cookbook) | 53,4k | MIT | commit 10/10/2026 | Công thức chính thức cho Claude: tool use, RAG, prompt caching, sub-agent | Chỉ cho Claude; vài link trong README còn dùng tên cũ |
| **openai/openai-cookbook** | 76,6k | MIT | commit 9/10/2026 | Ví dụ và hướng dẫn chính thức cho OpenAI API (cookbook.openai.com), nhận cookbook bên thứ ba đã review | Notebook cũ có thể dùng API đã bị thay **(chưa xác minh)** |

**Không nên bắt đầu mới với (kiểm 12/10/2026):**

- `anthropics/courses` (22,9k★): **archive 15/9/2026**, license CC BY-NC 4.0 (phi thương mại).
- `anthropics/prompt-eng-interactive-tutorial` (38,5k★): commit cuối 8/4/2024, không thấy file LICENSE — vẫn đọc để học được, nhưng nội dung đã cũ 2,5 năm.
- `microsoft/promptflow` (11,2k★): **ngừng phát triển tính năng 20/4/2026, nghỉ hẳn 20/4/2027**; Microsoft hướng dẫn chuyển sang Microsoft Agent Framework (mục 02).
- `microsoft/LLMLingua` (6,7k★): commit code cuối 28/10/2025 (9/2026 chỉ ghim CI); `microsoft/poml` (5,0k★): commit cuối 20/9/2025; `MadcowD/ell` (5,8k★): commit cuối 5/6/2025.

**Chọn nhanh:** gọi API đóng (Claude, GPT) cần JSON đúng schema → instructor (hoặc structured output có sẵn của nhà cung cấp); model local cần bảo đảm tuyệt đối → outlines; nhóm đa ngôn ngữ muốn hợp đồng có kiểu → BAML; tối ưu prompt theo metric → DSPy (bảng trên).

## 2c. nokia-applied-research/AnyJev: đọc quyết định có kiểu kèm xác suất từ LLM mở, không cần huấn luyện (link người dùng gửi, 2026-10-16)

**Kết luận:** đáng dùng khi agent chạy model mở và cần **phân loại hoặc định tuyến kèm độ tin** (chọn 1 trong K nhãn, có/không, chấm thang điểm). Phần không cần huấn luyện (`Decider`, mức `L0`) là cách đóng gói gọn ba kỹ thuật đã có bài báo. Số liệu trong README khớp với JSON trong repo, nhưng ô được nêu nổi bật là một trong những ô đẹp nhất. Dự án còn rất mới (Pre-Alpha, 0.3.0) và chưa có ai kiểm chứng độc lập.

### 2c.1 Là gì, và "Jev" là gì

- **Jev** là model "System One" **đóng, chạy qua API** của startup TypeSafe AI (San Francisco), mở early access ngày 15/9/2026. Nó trả quyết định có kiểu (Choice, Score, yes/no) kèm xác suất thay vì sinh văn bản. Các con số 70–500 ms và 0,042 USD cho 1 triệu token đầu vào đều do TypeSafe tự công bố (The Register).
- **AnyJev** là bản mở, giao diện "kiểu Jev", Apache-2.0. README và `CREDITS.md` ghi rõ "Not affiliated with TypeSafe AI or Jev". Gồm hai phần:
  - `Decider`: đọc quyết định từ **bất kỳ LLM mở nào** qua backend transformers, vLLM, SGLang hoặc llama.cpp. Không huấn luyện, không cần nhãn.
  - `Tacit`: 5 checkpoint 1,7B–9B **tự chưng cất** từ Qwen3/Qwen3.5 (Apache-2.0). Model học trả lời trong một lượt forward đáp án mà nó đạt được khi suy luận. Với `adaptive=True`, một phần quyết định có giới hạn được chuyển sang suy luận.
- Có HTTP gateway `python -m anyjev.serve` (`POST /v1/decide`). Gateway **không có xác thực**, mặc định chỉ nghe ở 127.0.0.1.

### 2c.2 Cách hoạt động (đọc mã ở HEAD `b03158e`, 12/10/2026)

| Mức | Làm gì | Gốc kỹ thuật |
|---|---|---|
| `raw` | Một prompt, softmax giới hạn trên token nhãn (A, B, C…) | — |
| `L0`, bước 1 | Đọc K phép xoay vòng thứ tự lựa chọn để mỗi lựa chọn đứng ở mọi vị trí, rồi lấy trung bình **log-prob** (`anyjev/calibrate/permute.py`). Nếu thiên lệch vị trí là cộng tính trên logit thì nó bị triệt tiêu đúng | Permutation debiasing, Zheng et al., ICLR 2024 (arXiv 2309.03882) |
| `L0`, bước 2 | Chia cho prior nhãn rồi chuẩn hoá lại (`contextual.py`). Mặc định ước lượng prior bằng trung bình chạy trên các đầu vào thật, hệ số 0,75 | Batch Calibration, Zhou et al., ICLR 2024; tuỳ chọn content-free theo Zhao et al., ICML 2021 |
| Rotation budget | Dừng sớm khi biên log-odds vượt ngưỡng. Ngưỡng được chứng nhận bằng cận Clopper–Pearson so với đáp án đọc đủ K, nên không cần nhãn. README: trung bình 7,2/18 phép xoay, thông lượng gấp 2,2–2,7 lần | Của AnyJev |
| Tacit `one_forward` / `cot` | Một prefill. Khi biên giữa 2 lựa chọn đầu < `tau`, model suy luận lại; tối đa `max_cot_share` (20%) của 1.000 quyết định gần nhất | Của AnyJev |

Điểm tốt về kỷ luật kỹ thuật:

- `Decider` **không bao giờ sinh token**, nên không có bước parse nào có thể hỏng.
- Mỗi `Decision` mang `level`. Gọi `require="L0"` sẽ từ chối kết quả ở mức yếu hơn.
- `tests/test_readme_numbers.py` kiểm các bảng trong README khớp với JSON đã commit.
- `AGENTS.md` của repo cấm số bịa và cấm agent tự `git commit`.
- Lõi chỉ phụ thuộc numpy. Gói chỉ gọi mạng tới server vLLM do người dùng cấu hình (`urllib` trong `backends/vllm.py` và `tacit.py`); không thấy telemetry.

### 2c.3 Kiểm số liệu (đọc JSON trong `bench/results_v01/2026-09-22/`, 11 model × 3 tác vụ, n = 300, một seed)

- **Ô nổi bật khớp JSON.** Qwen3-8B trên BANKING77-20: tỷ lệ đổi đáp án khi đảo thứ tự 0,230 → 0,073; accuracy 0,747 → 0,803; ECE 0,240 → 0,184; tỷ lệ tự quyết được ở sai ≤ 5% là 7,7% → 46,3%.
- **Nhất quán ở tác vụ 20 lựa chọn.** Trên cả 22 ô (11 model × banking20/newsgroups), `L0` giảm tỷ lệ đổi đáp án và tăng accuracy. Model nhỏ hưởng nhiều nhất: SmolLM2-1.7B trên newsgroups tăng 0,257 → 0,637.
- **Không đồng đều ở "tự quyết được ≤ 5%".** Đây chính là dòng README gọi là quan trọng nhất:
  - Ở tác vụ nhị phân `injection`, chỉ số này **sụp**: Qwen3-8B 0,313 → 0,013; Qwen3-4B 0,117 → 0,020.
  - Qwen3-32B giảm cả accuracy (0,857 → 0,827) lẫn coverage ở `injection`, và giảm coverage ở newsgroups (0,557 → 0,470).
  - `docs/limitations.md` tự thừa nhận: coverage ở n = 300 có phương sai cao, và prior theo batch làm giảm accuracy khi một nhãn áp đảo.
- **Bảng xếp hạng Decision Index 0.3.** Đây là Space cộng đồng `multimodalart/jev-decision-index` trên Hugging Face, không phải của TypeSafe.
  - Điểm 60,22 được người duy trì bảng chạy lại: phần private và độ trễ 98/260/1.080 ms, khớp 98,18% số quyết định.
  - "Hạng 5/149" là **hạng theo nhóm hoà** (cách nhau ≤ 0,9 điểm) tại 12/10. Ở snapshot 15/10, xếp theo điểm thì là **10/168** (`rank_v` = 10, `rank_tie` = 5). Đứng trên nó có Jev 1.14 (61,53); đầu bảng 66,26.
  - Cấu hình nộp bảng là 2 phép xoay, Gemma-4-31B FP8, khác mặc định thư viện.
- **Tacit** (JevBench public 0,823 → 0,887 khi bật adaptive cho Tacit-9B) là số tự báo cáo. JevBench là dự án cá nhân của `fstandhartinger`, MIT, độc lập với TypeSafe.
- **Chưa tự chạy được.** Lệnh cài và chạy test của repo bị bộ phân loại quyền chặn vì là mã bên ngoài. Các con số trên đọc từ JSON, không chạy lại.

### 2c.4 Ai làm, độ tin cậy

- Org GitHub "Nokia Applied Research" có 7 repo public, không huy hiệu verified, không thành viên công khai. arXiv 2610.00831 (30/9/2026, tự ghi "early report") ghi đơn vị "Nokia, Sunnyvale, CA" cho 7/9 tác giả. Không tìm được trang nokia.com nào nhắc nhóm này, nên **(chưa xác minh)** là nhóm chính thức của Nokia.
- Commit đầu 21/9/2026; 56 commit; 7 người đóng góp. Tác giả chính Jiamu "Morris" Zhang dùng email rice.edu/case.edu. Backend SGLang và llama.cpp do người ngoài đóng góp.
- Phiên bản: PyPI 0.0.1 (21/9) → 0.3.0 (6/10/2026). Classifier "Development Status :: 2 - Pre-Alpha". ~1,3k★ (shields 16/10/2026).
- Bài báo bên ngoài chủ yếu là MarkTechPost (23/9/2026) và các trang tổng hợp chép README. Không thấy thảo luận Hacker News, phản biện hay tái hiện độc lập.

### 2c.5 Khi nào dùng, lưu ý khi đưa vào sản phẩm

- **Hợp:** định tuyến ticket hoặc intent, gắn nhãn, phát hiện prompt injection bằng model mở tự host. Cần xác suất để đặt ngưỡng "tự quyết / chuyển người", và không có nhãn để huấn luyện bộ phân loại.
- **Không hợp:**
  - API đóng không trả log-prob đầy đủ, như Claude. Khi đó dùng structured output (§2b) và eval riêng.
  - Bài toán có > 26 lựa chọn: `Decider` dừng ở 26.
  - Bài toán đã có đủ nhãn: một bộ phân loại tinh chỉnh thường rẻ hơn K lượt prefill.
- **Lưu ý vận hành:**
  1. **Prior batch là trạng thái theo tiến trình.** Phân phối của một câu hỏi phụ thuộc nhẹ vào các request trước, nên kết quả không tái lập hoàn toàn. Với hệ đa tenant, nên tách `Decider` theo tenant hoặc dùng `prior="content_free"`/`"none"`.
  2. **vLLM** phải chạy với `--logprobs-mode processed_logprobs`. Nếu không, nhãn nằm ngoài top log-prob sẽ ném `LabelTokenError`; trước bản sửa #13 nó bị đọc thành -30 một cách im lặng.
  3. **Gateway không có xác thực.** Không bind ra ngoài 127.0.0.1 nếu chưa có proxy xác thực đứng trước.
  4. Một quyết định leo lên `cot` tốn **vài giây**: cap giới hạn số quyết định leo, không giới hạn thời gian của từng quyết định.
  5. Hãy tự đo lại coverage trên dữ liệu của mình (xem 2c.3) trước khi tin vào ngưỡng "tự quyết".

**Nguồn §2c:** https://github.com/nokia-applied-research/AnyJev (clone 16/10/2026; đọc README.md, AGENTS.md, CREDITS.md, ROADMAP.md, CHANGELOG.md, docs/levels.md, docs/limitations.md, anyjev/calibrate/{permute,contextual}.py, anyjev/serve.py, pyproject.toml, bench/results_v01/2026-09-22/*.json, bench/results_decision_index/2026-10-12/*.json, examples/decision_index/README.md) · https://pypi.org/pypi/anyjev/json · https://arxiv.org/abs/2610.00831 · https://huggingface.co/spaces/multimodalart/jev-decision-index (data/v03.json, data/methodology.json, snapshot 15/10/2026) · https://huggingface.co/morriszjm/AnyJev-L0-Gemma-4-31B · https://huggingface.co/morriszjm/Tacit-9B · https://github.com/fstandhartinger/jevbench · https://www.theregister.com/a/5296711 · https://www.marktechpost.com/2026/09/23/nokia-open-sources-anyjev-a-training-free-layer-that-turns-any-open-llm-into-a-calibrated-decision-model/ (chỉ đọc tiêu đề, trang trả 403) · https://arxiv.org/abs/2309.03882 · https://arxiv.org/abs/2309.17249 · https://arxiv.org/abs/2102.09690

## 3. Bộ sưu tập system prompt (học cách các sản phẩm lớn thiết kế)

| Repo | Nội dung | Ghi chú |
|---|---|---|
| `x1xhlol/system-prompts-and-models-of-ai-tools` | System prompt của Cursor, Devin, v0, Manus, Claude Code, Windsurf… | Rất nhiều sao; nguồn "rò rỉ", dùng để học cấu trúc, không sao chép |
| `anthropics/claude-cookbooks` (tên cũ anthropic-cookbook, URL cũ chuyển hướng), Claude system prompt công khai (docs) | Anthropic công bố system prompt của Claude.ai theo phiên bản | Chính thức |
| `elder-plinius/CL4R1T4S` | Prompt nhiều sản phẩm | Nguồn không chính thức |

## 4. Nguyên tắc rút ra (2026)

1. **Context engineering > prompt engineering**: cấu trúc ngữ cảnh, tool, memory quan trọng hơn câu chữ (mục 03).
2. Prompt là **code**: version hóa, test bằng eval (Promptfoo/DeepEval), tối ưu bằng DSPy/GEPA thay vì chỉnh tay.
3. Với agent: nêu rõ vai trò, công cụ, tiêu chí dừng, định dạng output; đặt dữ liệu không tin cậy vào thẻ riêng (mục 12).
4. Few-shot + XML tags + "think step by step"/extended thinking vẫn hiệu quả; tránh prompt quá dài làm loãng cache.

## 4b. Nâng cấp 31/10/2026: rà repo lớn

> Hai việc. (1) Đọc lại sao, license, ngày push của **13 repo** mục 17 trong catalog (GitHub search API, 31/10/2026). (2) Tìm repo lớn còn thiếu: truy vấn "prompt engineering", "system prompts", "prompt optimization", `topic:prompt-management`, `topic:prompt-engineering`, và "prompt" tạo sau 1/10/2025, lọc theo `data/projects.json`. Bỏ qua kho prompt ảnh/video và repo "jailbreak". Chọn **7 repo**, clone `--filter=blob:none`, đọc LICENSE, manifest, cấu trúc, CI, file Docker/cấu hình, grep mạng và telemetry. **Không chạy script nào của các repo.**

### 4b.1 Repo cũ: điều đã đổi

| Repo | Thay đổi (→ 31/10/2026) | Hệ quả |
|---|---|---|
| `f/awesome-chatgpt-prompts` | **Đổi tên thành `f/prompts.chat`**, 175,4k★. Nay là app Next.js (Prisma, Sentry) kèm `prompts.csv` 180k dòng. LICENSE ghi **hai license**: code MIT, nội dung prompt CC0, nên GitHub báo `NOASSERTION` | Catalog nên đổi `repo` và ghi "MIT (code) + CC0 (prompt)" |
| `x1xhlol/system-prompts-and-models-of-ai-tools` | Catalog `null`; nay **144,4k★**, GitHub nhận **GPL-3.0**, push 12/10 | Bổ sung số và license; GPL áp lên phần biên soạn, không làm prompt của hãng thành mã mở |
| `dair-ai/Prompt-Engineering-Guide` | Push cuối **11/3/2026** (gần 8 tháng); 79,7k★ | Nội dung web promptingguide.ai có thể vẫn cập nhật **(chưa xác minh)**; repo coi như tĩnh |
| `zou-group/textgrad` | Catalog `null`; nay 3,8k★ MIT, **push cuối 25/7/2025** (hơn 15 tháng) | Ngừng phát triển; dùng GEPA hoặc DSPy (dưới) |
| `guidance-ai/guidance` | Push cuối 21/5/2026 | Như §2b đã ghi: chậm lại |
| `stanfordnlp/dspy`, `567-labs/instructor`, `BoundaryML/baml`, cookbook Anthropic/OpenAI | Dao động dưới 5%, đều push trong tháng 10 | Không đổi |

### 4b.2 Bảng nhanh 7 repo mới

| Repo | Nhóm | ★ · license | Commit cuối | Một dòng | Cờ |
|---|---|---|---|---|---|
| `anthropics/prompt-eng-interactive-tutorial` | Khoá học chính chủ | 39k · **không có LICENSE** | 7/4/2024 (`master`) | 9 chương + 3 phụ lục dạng notebook, bản 1P và Bedrock | Model 2024, 9 commit |
| `linshenkx/prompt-optimizer` | Công cụ tối ưu prompt | 40,1k · **AGPL-3.0-only** (từ 30/10/2025) | 30/10/2026 | Web, desktop, extension Chrome, Docker, MCP; v2.13.0 | **Docker lộ API key**, `/mcp` không xác thực |
| `gepa-ai/gepa` | Tối ưu prompt bằng phản tư | 7,2k · MIT | 31/10/2026 | Thư viện Python tiến hoá prompt theo Pareto; là optimizer GEPA trong DSPy | Số liệu marketing lấy từ blog |
| `danielmiessler/Fabric` | Thư viện prompt + CLI | 44,5k · MIT | 29/10/2026 | 265 "pattern" (`system.md`) + CLI Go với ~15 nhà cung cấp | Không có eval cho pattern |
| `asgeirtj/system_prompts_leaks` | System prompt rò rỉ | 70,5k · CC0 | 31/10/2026 | 1.856 file, 649 của Anthropic, cập nhật hằng ngày | Bản quyền văn bản thuộc hãng |
| `elder-plinius/CL4R1T4S` | System prompt rò rỉ | 51,7k · AGPL-3.0 | 22/9/2026 | 80 file, 26 hãng/sản phẩm, một người duy trì | Đã nhắc ở §3, chưa có hồ sơ |
| `Piebald-AI/claude-code-system-prompts` | Prompt Claude Code theo phiên bản | 13k · MIT | 30/10/2026 | 1.057 file prompt/tool/agent của Claude Code v2.1.316, đếm token bằng API | Quảng cáo sản phẩm Piebald |

### 4b.3 Hồ sơ ngắn

- **Anthropic Prompt Engineering Interactive Tutorial.** Khoá nền tảng tốt nhất để học cấu trúc prompt (vai trò, tách dữ liệu bằng thẻ XML, prefill, few-shot, chống bịa, chuỗi prompt, tool use). Nhưng nhánh `master` chỉ có **9 commit, dừng 7/4/2024**; "push 28/8/2026" là nhánh vá `awscli`. Notebook gọi `claude-3-haiku-20240307`; kiểm model đó còn được phục vụ trước khi chạy **(chưa xác minh)**. Repo **không có file LICENSE** nên mặc định giữ mọi quyền: học và tham khảo được, không chép vào sản phẩm. Kỹ thuật vẫn đúng; tài liệu mới hơn ở docs.claude.com và `anthropics/courses`.
- **prompt-optimizer (linshenkx).** 1.039 commit, 881 của tác giả chính; monorepo pnpm 6 gói (core, ui, web, desktop, extension, mcp-server), CI chạy `test:gate` và Playwright e2e. Đổi license **MIT → AGPL-3.0-only ngày 30/10/2025**; file LICENSE có đoạn đầu riêng nên GitHub báo `NOASSERTION`. Kiểm lời quảng cáo: ✅ bản web và desktop gọi thẳng nhà cung cấp AI. ❌ Bản Docker thì khác: `docker/generate-config.sh` **ghi mọi biến `VITE_*` (gồm API key) vào `config.js` phục vụ cho trình duyệt** và in chúng ra log container. `nginx.conf` đặt **`auth_basic off` cho `/mcp`** ngay cả khi có `ACCESS_PASSWORD`, trong khi MCP server dùng chính các key đó. `docker-compose.yml` mặc định `ACCESS_PASSWORD=123456`. Nếu dùng: chạy bản desktop/extension, hoặc Docker chỉ trên `127.0.0.1`, không đặt key qua env.
- **GEPA.** Thư viện của nhóm tác giả bài *GEPA: Reflective Prompt Evolution* (arXiv 2507.19457), 937 commit, 72 tác giả, **32% commit có trailer Claude**. `pyproject.toml` có **`dependencies = []`**: gói lõi không kéo phụ thuộc, `litellm`, `mlflow`, `wandb` nằm ở extra `full` và loại trừ có ghi chú từng bản `litellm` lỗi wheel. Có 71 file test, workflow `dspy_contract.yml` và `dspy_compatibility.yml` kiểm GEPA vẫn khớp với `dspy.GEPA`. ⚠️ Bảng "35x faster than RL" trong README: paper nói **ít lượt rollout hơn tới 35 lần**, không phải nhanh hơn theo thời gian; các số "32% → 89%", "55% → 82%" dẫn tới blog, không có dữ liệu tái lập trong repo. Cài: `pip install gepa` (hoặc dùng qua `dspy.GEPA`).
- **Fabric (Daniel Miessler).** 4.500 commit, 311 tác giả; người commit nhiều nhất là Kayvan Sylvan (1.403), không phải tác giả gốc. CLI Go (`go 1.26`), plugin cho Anthropic, OpenAI, Gemini, Bedrock, Ollama, LM Studio, Claude Code, Codex… Mỗi pattern là `system.md` (+ `user.md`) kiểu "IDENTITY and PURPOSE / OUTPUT INSTRUCTIONS"; **41/265 pattern còn câu "Take a deep breath and think step by step"** (mẹo 2023). Không có eval cho pattern, CI chỉ test code Go. ⚠️ LICENSE MIT ghi "Copyright (c) 2012-2024 Scott Chacon and others", có vẻ chép từ dự án khác khi thêm file 29/8/2024. Không thấy telemetry. Cài: `brew install fabric-ai` hoặc `winget install danielmiessler.Fabric`; README còn đưa `curl … | bash`.
- **system_prompts_leaks (Ásgeir Thor Johnson).** 897 commit, 300 từ 1/7/2026, cập nhật trong ngày khi Claude Code ra bản (commit 31/10 ghi v2.1.316). 649/1.856 file thuộc thư mục Anthropic (Claude.ai, Claude Code, Cowork, Claude Design, Artifact types…). README hứa "full verbatim… carefully curated" nhưng **không mô tả cách trích xuất hay kiểm chứng**. Đầu README là quảng cáo Latitude qua link rút gọn `workers.dev`. License CC0 chỉ áp cho phần người biên soạn đóng góp; văn bản prompt vẫn thuộc các hãng.
- **CL4R1T4S (Pliny).** 206 commit, một tác giả, 80 file. Mục đích tự nêu là "minh bạch AI"; phần đóng góp kêu gọi "Leak, extract, or reverse-engineer". AGPL-3.0 trên văn bản không phải của tác giả có hiệu lực pháp lý không rõ. Dùng như nguồn so sánh, không phải nguồn chuẩn.
- **claude-code-system-prompts (Piebald).** Tách prompt Claude Code thành 1.057 file (393 system, 283 tool, 204 data, 103 agent, 74 skill), mỗi bản phát hành một commit "vX (+N tokens)". `tools/updatePrompts.js` đếm token bằng API `count_tokens` của Anthropic và lấy ngày phát hành từ npm, nên số token là đo thật ✅. ⚠️ README ghi "350 → 515 prompt", còn repo có 1.057 file: cách đếm khác nhau, chưa rõ. Hữu ích để **so sánh diff prompt giữa các phiên bản** khi viết harness; cùng rủi ro bản quyền như baoyu-design (mục 06 §7p.5).

**Về ba kho prompt rò rỉ:** kho này chỉ ghi nhận để học cấu trúc (thứ tự phần, cách mô tả tool, quy tắc an toàn), **không trích nội dung**. Với prompt của Anthropic, nguồn chính thức là trang system prompt công khai trong docs (§3).

### 4b.4 Mẫu chung rút ra

1. **Prompt "đã tối ưu" cần eval, không cần thêm mẹo**: GEPA có test, contract với DSPy và benchmark trong paper; Fabric có 265 pattern nhưng không có eval nào. Quy tắc §4 mục 2 ("prompt là code, test bằng eval") vẫn đúng và là chỗ phân biệt.
2. **Lời "chạy hoàn toàn phía client" chỉ đúng cho bản nào đó**: prompt-optimizer đúng ở bản desktop, sai ở bản Docker (key vào `config.js`, `/mcp` mở). Kiểm từng hình thức triển khai.
3. **License nhảy giữa các bản**: prompt-optimizer MIT → AGPL; prompts.chat tách MIT/CC0; tutorial Anthropic không có LICENSE. Ghi license theo ngày đọc.
4. **Prompt rò rỉ đã thành nguồn cập nhật theo giờ** (system_prompts_leaks, Piebald). Hữu ích để theo dõi thay đổi harness, nhưng không có quy trình kiểm chứng và quyền sở hữu không rõ.
5. **Repo chính chủ cũng có thể bị bỏ lại**: tutorial của Anthropic 39k★ nhưng dừng từ 4/2024. Sao không phải thước đo độ mới.

**Nguồn §4b:** GitHub search API 31/10/2026 (`repo:` cho 13 repo cũ và 7 repo mới; 6 truy vấn chủ đề) · `meta_all.json`/`status_all.json` đợt rà 31/10 · clone `--filter=blob:none` 8 repo, đọc: f/prompts.chat (LICENSE, cây gốc, prompts.csv), anthropics/prompt-eng-interactive-tutorial (README.md, cây `Anthropic 1P/`, `AmazonBedrock/`, nhánh), linshenkx/prompt-optimizer (LICENSE và lịch sử, README.md, docker/{docker-compose.yml, nginx.conf, generate-config.sh, generate-auth.sh}, middleware.js, packages/mcp-server/{README.md, src/config/environment.ts}, .github/workflows/test.yml), gepa-ai/gepa (LICENSE, pyproject.toml, README.md, .github/workflows/, tests/), danielmiessler/Fabric (LICENSE và lịch sử, README.md, go.mod, internal/plugins/ai/, data/patterns/*/system.md, .github/workflows/patterns.yaml), asgeirtj/system_prompts_leaks (LICENSE, README.md, cây thư mục), elder-plinius/CL4R1T4S (LICENSE, README.md), Piebald-AI/claude-code-system-prompts (LICENSE, README.md, tools/updatePrompts.js, cây system-prompts/) · https://arxiv.org/abs/2507.19457

## 4c. Nâng trần 2/11/2026: định dạng prompt có spec, công cụ so sánh, red-team và tối ưu có cổng validation (yêu cầu người dùng)

> Tìm repo **chưa có trong catalog** ở ba lớp: chuẩn, cổng máy, đầu bảng. GitHub search API 2/11/2026 (`repo:` và truy vấn "red teaming llm", "prompt testing", "prompt injection benchmark"); clone `--depth 1 --filter=blob:none`, đọc LICENSE, README, `pyproject`/`package.json`, module telemetry. **Không cài, không chạy.**

**Trần hiện tại:**

- Mục có hướng dẫn (§1), optimizer (DSPy, GEPA ở §2, §4b), structured output (§2b) và kho system prompt (§3, §4b). Nguyên tắc §4 mục 2 "prompt là code, test bằng eval" có, nhưng công cụ eval/red-team nằm ở mục 07 và 12 (promptfoo, garak, PyRIT), mục này chưa có.
- Prompt chưa có **định dạng file chuẩn**: mỗi dự án tự đặt chuỗi trong code, nên không lint, không diff, không chạy lại được giữa các runtime.
- Chưa có benchmark prompt injection để đo phòng thủ của prompt, và optimizer ở §4b chưa nói gì về **cổng validation giữ lại** (held-out) khi chấp nhận thay đổi.

| Repo | Lớp | ★ · license (2/11/2026) | Commit cuối | Vì sao nâng trần | Rủi ro |
|---|---|---|---|---|---|
| `microsoft/prompty` | Chuẩn (định dạng file) | 1,3k · MIT | 21/10/2026 | `.prompty` = Markdown + frontmatter (model, connection, template); v2 có spec (`spec/spec.md`, TypeSpec trong `schema/`) và **conformance vectors** dùng chung cho runtime Python, TypeScript, Rust, C#; extension VS Code chạy bằng F5; có OpenTelemetry | Đổi lớn từ v1 lên v2; runtime Go/Java/Swift còn dở **(chưa xác minh)** |
| `google/dotprompt` | Chuẩn (định dạng file) | 573 · Apache-2.0 | 5/10/2026 | Định dạng prompt thực thi được dựa trên Handlebars, dùng trong Firebase Genkit; spec viết thành YAML test (`spec/*.yaml`) chạy chung cho JS, Python, Go, Rust, Java, Dart; có OpenSSF Scorecard | Ít sao; gắn với hệ Genkit |
| `ianarawjo/ChainForge` | Đầu bảng (so sánh prompt) | 3,0k · MIT | 29/10/2026 | Môi trường dạng luồng để so prompt × model × tham số, node đánh giá (Python, so ground truth), vẽ kết quả; kèm 188 flow chuyển từ OpenAI evals | Hợp khám phá hơn CI; bản web giới hạn tính năng |
| `confident-ai/deepteam` | Cổng máy (red-team) | 3,1k · Apache-2.0 | 23/10/2026 | 50+ lỗ hổng (PII, prompt leakage, BOLA, SSRF, tool metadata poisoning…) và nhiều kiểu tấn công, chấm bằng LLM judge chạy cục bộ; có guardrails | ❌ **Telemetry bật mặc định**: `deepteam/telemetry.py` lấy IP công khai qua `api.ipify.org` rồi gửi kèm span tới New Relic, cùng PostHog và Sentry (key viết cứng). Tắt bằng `DEEPTEAM_TELEMETRY_OPT_OUT=YES`; không đọc `DO_NOT_TRACK` |
| `liu00222/Open-Prompt-Injection` | Cổng máy (benchmark) | 510 · MIT | 27/9/2026 | Bộ công cụ học thuật (slide của tác giả đặt ở duke.edu) chuẩn hoá tấn công/phòng thủ prompt injection, đo ASV; có detector DataSentinel và PromptLocate | Checkpoint tải từ Google Drive, không ghim băm; ví dụ dùng PaLM2 cũ |
| `microsoft/SkillOpt` | Đầu bảng (optimizer) | 18,8k · MIT | 29/10/2026 | Coi tài liệu skill/prompt là tham số để huấn luyện: sửa add/delete/replace có giới hạn, **chỉ nhận sửa khi điểm validation held-out tăng**; sản phẩm là `best_skill.md` 300–2.000 token, không thêm lượt gọi lúc chạy | Số "tốt nhất 52/52 ô" là tự công bố (paper arXiv 2605.23904) **(chưa xác minh)**; `SkillOpt-Sleep` đọc transcript Claude Code/Codex/Cursor của người dùng |

**Stack nâng trần** (lợi ích/công sức giảm dần):

1. Đưa prompt ra file có spec: `.prompty` (đa runtime, hệ Microsoft) hoặc `.prompt` của dotprompt (hệ Genkit). File riêng thì diff, review và chạy eval được như code (§4 mục 2).
2. Eval hồi quy bằng promptfoo (mục 07) trên chính các file đó; ChainForge để khám phá nhanh trước khi chốt test case.
3. Red-team trước khi phát hành: deepteam hoặc garak/PyRIT (mục 12), luôn đặt `DEEPTEAM_TELEMETRY_OPT_OUT=YES`; đo phòng thủ injection bằng Open-Prompt-Injection.
4. Tối ưu: DSPy/GEPA (§2, §4b) cho pipeline, SkillOpt cho prompt/skill dạng tài liệu. Với mọi optimizer, giữ quy tắc của SkillOpt: **tách tập validation, chỉ nhận thay đổi làm điểm tăng**.
5. Quản lý phiên bản prompt (Langfuse, LangSmith ở §2) lưu cùng điểm eval, không chỉ lưu văn bản.

**Nguồn §4c:** GitHub search API 2/11/2026 · clone `--depth 1 --filter=blob:none` 2/11/2026: microsoft/prompty (LICENSE, README.md, `spec/`, `schema/model/conformance/`, `runtime/`), google/dotprompt (LICENSE, README.md, `spec/`), ianarawjo/ChainForge (LICENSE.md, README.md), confident-ai/deepteam (LICENSE.md, README.md, `deepteam/telemetry.py`), liu00222/Open-Prompt-Injection (LICENSE, README.md), microsoft/SkillOpt (LICENSE, README.md, pyproject.toml, `docs/sleep/README.md`, grep telemetry) · https://github.com/microsoft/prompty · https://github.com/google/dotprompt · https://chainforge.ai · https://www.trydeepteam.com · https://github.com/liu00222/Open-Prompt-Injection · https://arxiv.org/abs/2605.23904

<a id="core-prompt-optimization"></a>

## 4d. Nâng trần 2/11/2026: optimizer có holdout thật và ngân sách kiểm chứng (mở rộng cùng ngày)

> Mở rộng chiều sâu trong cùng đợt 2/11/2026, không phải công bố các repo vừa ra mắt. Hai repo dưới đã có trong catalog: đọc lại LICENSE, CI và nhánh mặc định bằng clone chỉ đọc; SHA đối chiếu GitHub API. Mức bằng chứng **code-read**; không chạy/build repo ngoài, hiệu năng và hành vi thực tế **(chưa xác minh)**. Số sao/trạng thái đọc 2026-11-02; ngày commit tính theo UTC, tách khỏi `pushed_at`.

| Repo đã có | ★ · license (2026-11-02) | HEAD nhánh mặc định | Vai trò đọc sâu |
|---|---|---|---|
| `stanfordnlp/dspy` | 38.885 · MIT | 2026-10-29 · `25162c4f` | Lập trình prompt và adapter GEPA có budget |
| `gepa-ai/gepa` | 7.245 · MIT | 2026-10-31 · `8c7b697a` | Reflective search. Pareto validation và giới hạn đo |

**Trần còn thiếu:** §4c khuyên “validation held-out”, nhưng thư viện không luôn ép tách tập. Mục này thêm đường đọc từ **API optimizer → tập dùng chọn ứng viên → ngân sách → phép chấm cuối**, để một điểm validation tăng không bị hiểu nhầm thành model tổng quát tốt hơn.

### DSPy: chữ ký có kiểu không thay metric và dữ liệu tách biệt

- [`dspy.GEPA`](https://github.com/stanfordnlp/dspy/blob/25162c4fc05c2d2d019b0ffb5b6b2a9f315ec007/dspy/teleprompt/gepa/gepa.py#L377) buộc chọn đúng một trong `auto`, `max_full_evals`, `max_metric_calls`; trace/feedback giúp optimizer đề xuất sửa prompt. Chi phí search gồm model đích, model reflection và grader, nên số metric call không tự quy đổi thành một trần USD.
- Adapter ở SHA đọc này ghi **`max_reflection_cost` chưa hỗ trợ** và từ chối tham số đó vì DSPy LM thiếu giao diện tổng cost GEPA cần. Không chép một cấu hình GEPA standalone sang DSPy rồi tin đã có cùng cap. Đặt trần metric + timeout/quota ngoài và đối soát token/cost thực.
- [`MIPROv2.compile`](https://github.com/stanfordnlp/dspy/blob/25162c4fc05c2d2d019b0ffb5b6b2a9f315ec007/dspy/teleprompt/mipro_optimizer_v2.py#L113) nhận train/val, dùng validation để tìm instruction/few-shot; final test phải tách khỏi cả hai. Output có kiểu/khớp Signature chỉ là hợp đồng dữ liệu, chưa là metric chất lượng. [CI upstream](https://github.com/stanfordnlp/dspy/blob/25162c4fc05c2d2d019b0ffb5b6b2a9f315ec007/.github/workflows/run_tests.yml) có lint/type/test và workflow scan; đây không phải kết quả tối ưu của ứng dụng đang dùng kho.

### GEPA standalone: `valset=None` tái dùng trainset

- [`optimize()`](https://github.com/gepa-ai/gepa/blob/8c7b697a71977980afc7537dac0881e784eef99f/src/gepa/api.py#L153) nói rõ nếu không truyền `valset` thì dùng lại trainset; mã tạo `val_loader=train_loader`. Tên “validation” trong kết quả vì thế **không bảo đảm dữ liệu held-out**. Người tích hợp phải chia tập theo nguồn/episode và truyền valset khác thật.
- [`GEPAEngine`](https://github.com/gepa-ai/gepa/blob/8c7b697a71977980afc7537dac0881e784eef99f/src/gepa/core/engine.py#L116) dùng namespace cache riêng khi val loader khác train loader; đây là bảo vệ cache index, không phát hiện hai bộ có nội dung trùng/near-duplicate. Tập validation vẫn tham gia chọn ứng viên/Pareto, nên cần một final test chưa dùng chọn prompt.
- API có metric/stop callback và resume `run_dir`; nếu thay dữ liệu, metric hay model mà tái dùng run state cũ, điểm cũ không tự trở thành thí nghiệm hợp lệ. Paper GEPA cung cấp bằng chứng trong điều kiện tác giả đo; không suy ra sẽ hơn RL/prompt tay trên mọi task. [CI](https://github.com/gepa-ai/gepa/blob/8c7b697a71977980afc7537dac0881e784eef99f/.github/workflows/run_tests.yml) kiểm thư viện, **(chưa xác minh)** benchmark cho miền của người tích hợp.

**Ma trận chọn mức tối ưu**

| Bài toán | Bắt đầu bằng | Cổng nhận thay đổi |
|---|---|---|
| Ít dữ liệu, chưa có metric tin cậy | Prompt thủ công + ChainForge/Promptfoo §4c | Assertion và nhãn người trước khi tăng search |
| Pipeline nhiều module, cần kiểu và few-shot | DSPy/MIPROv2 | Validation tách theo nguồn + final test độc lập |
| Có trajectory/feedback giàu thông tin | DSPy GEPA hoặc GEPA adapter | Budget toàn search; không chọn bằng chính final test |
| Chỉ sửa tài liệu skill/prompt | SkillOpt §4c hoặc GEPA adapter phù hợp | Eval trigger/quality và safety regression |
| Cần cam kết $ cứng | Optimizer + gateway/quota/time cap | Đối soát reflection/grader/model, không chỉ metric-call count |

**Cách ghép:** xác định metric và negative control bằng mục 07; chia train/validation/final test trước search, kiểm dedup; ghi seed/model/prompt version và toàn bộ budget; chọn **một** optimizer để có baseline; đánh giá ứng viên thắng một lần trên final test kèm safety/structured-output regression; lưu prompt tối ưu cùng cấu hình và điểm đo (Prompty/Dotprompt §4c). Khi đổi dữ liệu/metric, tạo run/version mới. Chỉ chuyển sang fine-tuning khi lỗi còn lại có bằng chứng do năng lực model thay vì retrieval/tool/prompt, đối chiếu mục model adaptation khi chọn hướng đó.

**Nguồn phần mở rộng:** [1](https://github.com/stanfordnlp/dspy/blob/25162c4fc05c2d2d019b0ffb5b6b2a9f315ec007/LICENSE) · [2](https://github.com/stanfordnlp/dspy/blob/25162c4fc05c2d2d019b0ffb5b6b2a9f315ec007/dspy/teleprompt/gepa/gepa.py) · [3](https://github.com/stanfordnlp/dspy/blob/25162c4fc05c2d2d019b0ffb5b6b2a9f315ec007/dspy/teleprompt/mipro_optimizer_v2.py) · [4](https://github.com/stanfordnlp/dspy/blob/25162c4fc05c2d2d019b0ffb5b6b2a9f315ec007/.github/workflows/run_tests.yml) · [5](https://github.com/gepa-ai/gepa/blob/8c7b697a71977980afc7537dac0881e784eef99f/LICENSE) · [6](https://github.com/gepa-ai/gepa/blob/8c7b697a71977980afc7537dac0881e784eef99f/src/gepa/api.py) · [7](https://github.com/gepa-ai/gepa/blob/8c7b697a71977980afc7537dac0881e784eef99f/src/gepa/core/engine.py) · [8](https://github.com/gepa-ai/gepa/blob/8c7b697a71977980afc7537dac0881e784eef99f/.github/workflows/run_tests.yml) · [9](https://arxiv.org/abs/2507.19457) · [10](https://openreview.net/pdf?id=RQm2KQTM5r)

## 4e. Kiểm khung RCCOF của Danh Nolan (Role, Context, Constraint, Output format, Few-shot): “đặc tả mở” có DOI nhưng không có dữ liệu đo (link người dùng gửi, 3/11/2026)

> Người dùng gửi https://danhnolan.com/en/rccof. Đã đọc trang tiếng Anh, bản ghi Zenodo 10.5281/zenodo.22856974 qua API, PDF đính kèm (`RCCOF_Framework_Specification_v1.0-v3.pdf`, 7.519 byte, 2 trang) và bản ghi liên quan 10.5281/zenodo.22843346. Đối chiếu với docs prompt chính thức của Anthropic (platform.claude.com, "Prompting best practices", đọc 3/11/2026).

### 4e.1 Nó là gì

| Thuộc tính | Giá trị |
|---|---|
| Tác giả | Danh Nolan (Văn Hùng Danh), danhnolan.com, ORCID 0009-0007-7906-5091. Trang có Zalo và số điện thoại để liên hệ học "master program" có phí (không ghi giá) |
| Ngày, phiên bản | v1.0, đăng Zenodo 20/9/2026 (loại **Report**, tác giả tự nộp, không qua bình duyệt); trang web cập nhật 24/9/2026. Zenodo ghi 58 lượt xem, 14 lượt tải (3/11/2026) |
| Nội dung | Prompt gồm 5 lớp: **R**ole (vai trò chuyên môn), **C**ontext (persona, search intent, "emotional trigger", dữ kiện đã kiểm), **C**onstraint (giới hạn độ dài, cấm từ sáo, "không bịa ngoài dữ kiện"), **O**utput format (ví dụ H2 + đoạn trả lời trước 40–60 từ + 3 gạch đầu dòng + CTA), **F**ew-shot (1–2 đoạn mẫu). Ba quy tắc: đặt [TASK] cuối prompt; mọi số liệu phải nằm trong Context; bắt phân tích phản đối của người dùng trước khi viết. "Quy tắc 70/30": 70% giá trị đến từ con người |
| License | **Tự mâu thuẫn trên trang**: mục quyền ghi "All rights reserved" với văn bản gốc, còn FAQ và Zenodo ghi **CC BY 4.0** |
| Hệ sinh thái | Cùng tác giả còn DLN, WGS, SQA-200, SEO Master, EP-9, 4-ZIA, E-PROVE, PIOC, SIUM-1, MME-GA4; bản ghi Zenodo liên quan là "Decision Ladder Navigation™ (DLN)" (technical note, 19/9/2026) |

### 4e.2 Kiểm nhận định

| Nhận định | Kết quả | Căn cứ |
|---|---|---|
| "eliminates over 95% of factual hallucinations in enterprise generation benchmarks" (trang web) | ❌ không có nguồn | PDF trên Zenodo không có benchmark, bộ dữ liệu, model, phương pháp đo hay con số 95%. Trang web không nêu tên benchmark. PDF còn tự ghi "guarantees 100% Brand Voice alignment" và "Replicates 100% authentic Brand Voice DNA" mà không có bằng chứng |
| Biên tập giảm từ 45–90 phút xuống 5–10 phút mỗi bài | ❌ không có nguồn | Không có dữ liệu đi kèm |
| "Deterministic" control architecture | ⚠️ sai khái niệm | Prompt không làm đầu ra của LLM thành tất định; chỉ thu hẹp phân phối. Muốn chắc chắn về định dạng thì dùng structured output hoặc schema (mục 17 §2b) và cổng kiểm sau sinh |
| "A prohibition contracts the space of acceptable outputs where a recommendation only expands it" (lệnh cấm hiệu quả hơn khuyến nghị) | ⚠️ ngược với docs của nhà cung cấp | Anthropic khuyên "**Tell Claude what to do instead of what not to do**" và xếp "NEVER use ellipses" là cách kém hiệu quả hơn so với giải thích lý do. Danh sách từ cấm vẫn có ích, nhưng kiểm bằng linter sau sinh chắc hơn là chỉ cấm trong prompt (mục 18 §5d, mục 06 §7i) |
| Rule 1: đặt task ở đầu khiến model "bắt đầu sinh trước khi đọc Constraints phía sau" | ⚠️ đúng khuyến nghị, sai cơ chế | Model đọc toàn bộ prompt trước khi sinh token đầu tiên. Khuyến nghị đặt câu hỏi ở cuối có căn cứ khác: Anthropic ghi "Queries at the end can improve response quality by up to 30 percent in tests", chủ yếu với tài liệu dài, nhiều nguồn |
| Rule 2: mọi số liệu phải được cung cấp, "do not infer or fabricate" | ✅ hợp lý | Đây là grounding cơ bản. Tuy vậy cấm trong prompt không đảm bảo; cần kiểm đối chiếu dữ kiện sau sinh |
| Few-shot 1–2 đoạn mẫu | ✅ nhưng ít | Anthropic khuyên **3–5 ví dụ**, đa dạng, bọc trong thẻ `<example>` để không bị chép nguyên mẫu |
| Tính mới | ⚠️ | Năm thành phần đều đã có trong hướng dẫn chính thức (vai trò, ngữ cảnh, định dạng, ví dụ) và trong các khung viết tắt phổ biến có trước như CO-STAR, RISEN, CRISPE (kho chưa có hồ sơ riêng cho các khung này). Điểm riêng là áp vào nội dung marketing và AEO |

### 4e.3 Dùng thế nào

- Dùng như một **checklist nhớ** khi viết prompt nội dung: có vai trò, dữ kiện, ràng buộc, định dạng và ví dụ chưa. Không coi đây là "đặc tả" hay "tiêu chuẩn": nó không có bộ kiểm, phiên bản máy đọc hay dữ liệu đo.
- Thay câu cấm bằng mô tả điều muốn có kèm lý do; giữ danh sách từ cấm nhưng chặn bằng linter (design-os-vietnamese, antislop).
- Đo thật trước khi tin con số: cùng bộ đề bài, có và không dùng khung, chấm hallucination bằng đối chiếu dữ kiện (mục 07 cho công cụ eval).
- Một DOI Zenodo chỉ cho biết tài liệu đã được lưu trữ và trích dẫn được; nó **không** có nghĩa là đã được bình duyệt hay kiểm chứng.

**Nguồn §4e:** https://danhnolan.com/en/rccof (đọc 3/11/2026) · https://zenodo.org/api/records/22856974 và PDF `RCCOF_Framework_Specification_v1.0-v3.pdf` · https://zenodo.org/api/records/22843346 · https://doi.org/10.5281/zenodo.22856974 · https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices (mục "Add context to improve performance", "Control the format of responses", "Use examples effectively", "Long context prompting").

<a id="factory-prompt-release-2026-11-04"></a>

## 4f. Nâng trần 4/11/2026: prompt là artifact phát hành, có ranh giới tin cậy và cổng hồi quy

**Trần và khoảng trống.** §4c–§4d đã có định dạng prompt, optimizer, holdout và ngân sách. Phần còn thiếu cho xưởng là **artifact nào được deploy**, ai có quyền đổi endpoint/model, và cách trả về bản cũ khi metric sản phẩm xấu đi. Kết quả tối ưu tốt trên validation không tự cấp quyền nạp mọi file optimizer gửi sang.

### 4f.1 Đọc sâu DSPy: state JSON và chương trình pickle có quyền khác nhau

`stanfordnlp/dspy` (MIT), HEAD `c941671b1d2b6e208d472e93f954632b94000277` đọc ngày 4/11/2026. `BaseModule.save` tách lưu state (`.json`/`.pkl`) khỏi lưu toàn chương trình (`save_program=True`, cloudpickle). `BaseModule.load` mặc định `allow_pickle=False`; nhánh `.pkl` từ chối nếu chưa cho phép. Hàm top-level `dspy.load` cho chương trình cũng yêu cầu `allow_pickle=True` trước khi gọi `cloudpickle.load`. Bật cờ này là chấp nhận một nguồn có thể thực thi code, không chỉ là chọn định dạng nén. [State save/load và callsite]( https://github.com/stanfordnlp/dspy/blob/c941671b1d2b6e208d472e93f954632b94000277/dspy/primitives/base_module.py ) · [whole-program load]( https://github.com/stanfordnlp/dspy/blob/c941671b1d2b6e208d472e93f954632b94000277/dspy/utils/saving.py ).

Ở `Predict.load_state`, `_sanitize_lm_state` mặc định loại các khóa `api_base`, `base_url`, `model_list`; cờ `allow_unsafe_lm_state` mở đường giữ các khóa này và cho phép class LM tùy biến. Kết luận chỉ áp dụng đường state-load đã đọc, không khẳng định mọi nhánh import/plugin đều bị sandbox. Vì vậy bản prompt được review phải kèm schema, hash và cấu hình model/endpoint độc lập do môi trường kiểm soát. **JSON ít quyền thực thi hơn pickle không có nghĩa nội dung JSON đáng tin để đưa vào prompt.** [Sanitize và LM callsite]( https://github.com/stanfordnlp/dspy/blob/c941671b1d2b6e208d472e93f954632b94000277/dspy/predict/predict.py ).

Loader so dependency versions với metadata đã lưu và **cảnh báo** khi lệch; không coi cảnh báo đó là kiểm tương thích bắt buộc. CI upstream có lint/test/build nhưng chưa chạy ở đây; khả năng round-trip artifact và chất lượng sau deploy phải kiểm trong ứng dụng đích. [CI]( https://github.com/stanfordnlp/dspy/blob/c941671b1d2b6e208d472e93f954632b94000277/.github/workflows/run_tests.yml ) · [license]( https://github.com/stanfordnlp/dspy/blob/c941671b1d2b6e208d472e93f954632b94000277/LICENSE ).

### 4f.2 Ma trận lựa chọn và ranh giới

| Cách làm | Khi có ích | Cổng còn cần |
|---|---|---|
| Prompt thủ công, file review trong git | Tác vụ nhỏ, baseline rẻ và dễ audit | Contract đầu ra, eval hồi quy, model/config ghim; không mặc định cần optimizer |
| DSPy / GEPA (§2, §4d) | Có metric nhiệm vụ và corpus đủ để tối ưu | Train/validation/test tách đúng; artifact/source được tin; phí tính cả search/judge/retry, không chỉ lượt inference cuối |
| BAML / Outlines / Instructor (§2b) | Kiểu/schema, parsing và retry structured output | Schema pass không chứng minh tính đúng ngữ nghĩa hay quyền gọi tool; cần kiểm dữ kiện và quyền ở ứng dụng |
| Prompty / Dotprompt (§4c) | Định dạng prompt có thể review và chạy giữa runtime | Conformance với phiên bản runtime; secret/endpoint quản ở môi trường, không chép vào artifact |

### 4f.3 Luồng prompt → bản phát hành → theo dõi

1. Định nghĩa contract: input có provenance, output schema, quy tắc từ chối khi thiếu dữ liệu và metric nghiệp vụ. Tập case gồm tiếng Việt, không dấu, input nhiễu và trường hợp không nên gọi tool.
2. Ghim nguồn corpus và quyền dữ liệu; tách nhóm theo khách hàng/thời gian/tài liệu để tránh cùng nội dung rơi vào train và test. Tập tối ưu không thay tập nghiệm thu giữ kín.
3. Tối ưu có ngân sách; lưu baseline cố định cùng model, tool, retrieval và giới hạn tương đương. Không thay metric sau khi thấy kết quả rồi gọi đó là cải thiện đã xác nhận.
4. Đóng gói prompt/state + schema + model/config ID + dependency lock + bộ case/version + kết quả theo từng nhóm + hash. State JSON được kiểm schema; pickle chỉ từ nguồn đã tin và môi trường phù hợp; không lấy artifact không rõ nguồn chỉ vì `load` hỗ trợ.
5. Cổng phát hành kiểm hồi quy chất lượng, tỷ lệ lỗi parse/từ chối sai, tool call ngoài dự kiến, latency phân vị và tổng phí trên ngưỡng do sản phẩm đặt. Nêu số case thực chạy, skip, lỗi provider và bất định; không đổi lỗi API thành pass.
6. Canary và theo dõi drift ở mục 07/28; giữ bundle cũ để rollback nguyên prompt/config/retrieval phù hợp, không chỉ một chuỗi system prompt. Input thu hồi về eval phải được xử lý quyền truy cập và dữ liệu cá nhân.

**Tiêu chí chấp nhận:** có bundle định danh duy nhất, baseline và held-out report cùng schema; người/CI có thể đối chiếu artifact chạy thật với artifact đã duyệt; khi provider/model đổi có lượt kiểm mới. Đây là yêu cầu thiết kế của kho, chưa phải cam kết tính năng tự có của DSPy.

**Nguồn §4f:** permalink implementation/LICENSE/CI DSPy trên; đối chiếu cơ chế optimizer, spec và eval ở §4c–§4d. Không tuyên bố tái lập chất lượng/chi phí hay chạy model upstream trong đợt đọc này.

<a id="anhkysuai-2026-11-23"></a>

## Đánh giá từ kho Anh Kỹ Sư AI — 23/11/2026

Phần này có **3 hồ sơ hoặc phạm vi đối chiếu** từ [nguồn tuyển chọn](https://anhkysuai.com/kho/). [Bảng đủ 1.295 repo](../data/collections/anhkysuai-kho.json) ghi trạng thái đối chiếu từng link; [danh sách URL](../data/collections/anhkysuai-kho-links.txt) phục vụ tra cứu. Nguồn tuyển chọn giúp phát hiện repo; đánh giá bên dưới dựa trên clone và permalink upstream cùng metadata GitHub ngày 2026-11-23.

Mức `docs-read`/`code-read` chỉ áp dụng phạm vi ghi tại mỗi hồ sơ. Chưa cài, build, chạy test hay benchmark mã upstream. Giấy phép có thể tách theo code, model, nội dung, asset hoặc bản enterprise; con số/tuyên bố của tác giả chưa được tái lập nếu không có ghi chú khác.

<a id="anhkysuai-2026-11-23-awesome-gpt-image-2-prompts-evolink"></a>

### Awesome GPT Image 2 Prompts — EvoLink

**Repo:** [Evolink-AI/awesome-gpt-image-2-API-Prompts](https://github.com/Evolink-AI/awesome-gpt-image-2-API-Prompts) · **License:** CC0-1.0 cho nội dung được cấp quyền; nguồn bên thứ ba cần đối chiếu · **★ 17,430 (GitHub API, 2026-11-23)**

**Mục đích:** Thư mục prompt và ví dụ tạo/chỉnh sửa ảnh được tuyển chọn theo tình huống thiết kế.

**Giá trị và cơ chế:** README tổ chức prompt đầy đủ, nguồn và tác giả để người đọc điều chỉnh yêu cầu bố cục, phong cách và đầu ra; hữu ích làm bộ tham chiếu kỹ thuật viết prompt.

**Giới hạn:** Đã đọc phần giới thiệu và mẫu chọn lọc, không rà hết README hơn một triệu ký tự. Không xác nhận chất lượng mọi ví dụ hay quyền của ảnh gốc. API/skill automation là repo riêng.

**Cách tham khảo/tích hợp:** Lấy cấu trúc yêu cầu và viết lại bằng tài sản có quyền; lưu kết quả thử theo model/phiên bản.

**Thay thế:** [Awesome Nano Banana Pro Prompts](../17-prompt-engineering/README.md#anhkysuai-2026-11-23-awesome-nano-banana-pro-prompts), awesome-gpt4o-images, [Promptfoo](../07-eval-observability/README.md#core-eval-validity).

**Bằng chứng:** `docs-read`, ngày 2026-11-23, commit [`e2a269ad1a05`](https://github.com/Evolink-AI/awesome-gpt-image-2-API-Prompts/commit/e2a269ad1a055a0b4f6c1e170341c6c1aba30faa). README và các tài liệu/manifest/CI hiện diện, đọc chọn lọc; chưa kiểm implementation. Chưa cài/chạy upstream.

**Nguồn:** [README.md](https://github.com/Evolink-AI/awesome-gpt-image-2-API-Prompts/blob/e2a269ad1a055a0b4f6c1e170341c6c1aba30faa/README.md) · [LICENSE](https://github.com/Evolink-AI/awesome-gpt-image-2-API-Prompts/blob/e2a269ad1a055a0b4f6c1e170341c6c1aba30faa/LICENSE) · [metadata GitHub](https://api.github.com/repos/Evolink-AI/awesome-gpt-image-2-API-Prompts).

<a id="anhkysuai-2026-11-23-awesome-nano-banana-pro-prompts"></a>

### Awesome Nano Banana Pro Prompts

**Repo:** [YouMind-OpenLab/awesome-nano-banana-pro-prompts](https://github.com/YouMind-OpenLab/awesome-nano-banana-pro-prompts) · **License:** CC-BY-4.0; quyền tác giả bên thứ ba được lưu ý riêng · **★ 13,854 (GitHub API, 2026-11-23)**

**Mục đích:** Bộ prompt cộng đồng theo các tình huống avatar, infographic, quảng cáo và storyboard.

**Giá trị và cơ chế:** README tổ chức mẫu có tham chiếu và gallery riêng; phù hợp học cách mô tả bố cục, chữ và điều kiện hình ảnh cho công cụ tạo ảnh.

**Giới hạn:** Chỉ đọc cấu trúc và mẫu chọn lọc, chưa thử toàn bộ prompt. Tuyên bố license của bộ sưu tập không tự chứng minh quyền mọi ảnh/mẫu cộng đồng; README có thông báo bản quyền và cơ chế gỡ.

**Cách tham khảo/tích hợp:** Dùng làm nguồn ý tưởng, viết lại prompt với tài sản có quyền và giữ attribution khi tái sử dụng nội dung.

**Thay thế:** [Awesome GPT Image 2 Prompts — EvoLink](../17-prompt-engineering/README.md#anhkysuai-2026-11-23-awesome-gpt-image-2-prompts-evolink), awesome-gpt4o-images, [Promptfoo](../07-eval-observability/README.md#core-eval-validity).

**Bằng chứng:** `docs-read`, ngày 2026-11-23, commit [`445f95a70ec7`](https://github.com/YouMind-OpenLab/awesome-nano-banana-pro-prompts/commit/445f95a70ec77ab56a93e76055054bd257fad467). README và các tài liệu/manifest/CI hiện diện, đọc chọn lọc; chưa kiểm implementation. Chưa cài/chạy upstream.

**Nguồn:** [README.md](https://github.com/YouMind-OpenLab/awesome-nano-banana-pro-prompts/blob/445f95a70ec77ab56a93e76055054bd257fad467/README.md) · [LICENSE](https://github.com/YouMind-OpenLab/awesome-nano-banana-pro-prompts/blob/445f95a70ec77ab56a93e76055054bd257fad467/LICENSE) · [metadata GitHub](https://api.github.com/repos/YouMind-OpenLab/awesome-nano-banana-pro-prompts).

<a id="anhkysuai-2026-11-23-agency-agents-zh"></a>

### Agency Agents 中文

**Repo:** [jnMetaCode/agency-agents-zh](https://github.com/jnMetaCode/agency-agents-zh) · **License:** MIT · **★ 22,271 (GitHub API, 2026-11-23)**

**Mục đích:** Bộ mô tả vai trò agent bằng tiếng Trung, mở rộng từ Agency Agents cho nhiều quy trình và nền tảng.

**Giá trị và cơ chế:** README trình bày bản dịch cộng đồng cùng vai trò bổ sung, gợi ý đầu vào, cách phối hợp và đầu ra theo chuyên môn; license ghi công tác giả gốc và người chuyển ngữ.

**Giới hạn:** Đây là tập hướng dẫn/prompt, chưa chứng minh năng lực chuyên gia hoặc độ tin cậy. Các sản phẩm desktop và memory được quảng bá là repo riêng; chưa đọc toàn bộ vai trò.

**Cách tham khảo/tích hợp:** Chọn vài vai trò đúng việc, sửa tiêu chí đầu ra và kiểm kết quả trên tác vụ mẫu trước khi đưa vào workflow.

**Thay thế:** [Agency Agents 中文](../17-prompt-engineering/README.md#anhkysuai-2026-11-23-agency-agents-zh), awesome-claude-skills, [anthropics/skills](https://github.com/anthropics/skills).

**Bằng chứng:** `docs-read`, ngày 2026-11-23, commit [`6b22c1e651ed`](https://github.com/jnMetaCode/agency-agents-zh/commit/6b22c1e651eded6d1b6bf553d3f0903c1b18e99f). README và các tài liệu/manifest/CI hiện diện, đọc chọn lọc; chưa kiểm implementation. Chưa cài/chạy upstream.

**Nguồn:** [README.md](https://github.com/jnMetaCode/agency-agents-zh/blob/6b22c1e651eded6d1b6bf553d3f0903c1b18e99f/README.md) · [LICENSE](https://github.com/jnMetaCode/agency-agents-zh/blob/6b22c1e651eded6d1b6bf553d3f0903c1b18e99f/LICENSE) · [metadata GitHub](https://api.github.com/repos/jnMetaCode/agency-agents-zh).

## 5. Nguồn

- https://github.com/dair-ai/Prompt-Engineering-Guide · https://www.star-history.com/dair-ai/prompt-engineering-guide/ · https://dev.to/web_dev-usman/10-github-repos-every-serious-prompt-writer-should-be-using-21jk
- https://github.com/stanfordnlp/dspy · https://futureagi.com/blog/what-is-dspy-2026/ · https://www.promptquorum.com/power-local-llm/dspy-review · https://github.com/ganarajpr/awesome-dspy · https://github.com/dx-corp/dspy-0to1-guide
- https://en.wikipedia.org/wiki/Fatih_Kadir_Akin
- §2b (12/10/2026): https://github.com/567-labs/instructor · https://github.com/dottxt-ai/outlines · https://github.com/guidance-ai/guidance · https://github.com/BoundaryML/baml · https://github.com/anthropics/claude-cookbooks · https://github.com/openai/openai-cookbook · https://github.com/anthropics/courses · https://github.com/anthropics/prompt-eng-interactive-tutorial · https://github.com/microsoft/promptflow · https://github.com/microsoft/promptflow/tree/main/migration-guide/PromptFlow-to-MAF · https://github.com/microsoft/LLMLingua · https://github.com/microsoft/poml · https://github.com/MadcowD/ell

<a id="chuan-hoa-2026-11-23"></a>

## Chuẩn hóa bằng chứng hồ sơ cũ — 23/11/2026

Các hồ sơ dưới đây có từ trước khi kho ghi mức kiểm. Ngày 2026-11-23 mỗi repo được clone nông tại commit ghi trong bảng, đọc LICENSE, README, manifest và CI (nếu có); không cài, build hay chạy mã upstream. Nhận định cũ ở phần trên giữ nguyên; chỗ nào khác với lần đọc này được ghi trong cột Nhận định. Số sao lấy qua GitHub search API cùng ngày.

<a id="ch-anyjev"></a>

### AnyJev

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/nokia-applied-research/AnyJev |
| License | Apache-2.0 |
| Phiên bản đã đọc | `35311c58955716cb8955ce1368a665988bc63735` (commit 2026-10-21) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc LICENSE, README.md, pyproject.toml, ci.yml; chưa chạy upstream |
| Bảo trì | Commit gần nhất 21/10/2026; v0.3.0. |
| Nhận định | Thư viện quyết định có kiểu (choice/yes-no/score) kèm xác suất từ LLM, kèm mô hình Tacit riêng. Các tuyên bố hiệu năng/leaderboard trong README là của tác giả **(chưa xác minh)**. |
| Nguồn | [LICENSE](https://github.com/nokia-applied-research/AnyJev/blob/35311c58955716cb8955ce1368a665988bc63735/LICENSE) · [README.md](https://github.com/nokia-applied-research/AnyJev/blob/35311c58955716cb8955ce1368a665988bc63735/README.md) · [pyproject.toml](https://github.com/nokia-applied-research/AnyJev/blob/35311c58955716cb8955ce1368a665988bc63735/pyproject.toml) · [ci.yml](https://github.com/nokia-applied-research/AnyJev/blob/35311c58955716cb8955ce1368a665988bc63735/.github/workflows/ci.yml) |

<a id="ch-awesome-chatgpt-prompts"></a>

### awesome-chatgpt-prompts

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/f/prompts.chat |
| License | MIT (mã) + CC0-1.0 (prompt) (khác catalog cũ: CC0) |
| Phiên bản đã đọc | `32bbb1576e999fe57dc57d18eca9370e7ac46e24` (commit 2026-11-23) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc LICENSE, LICENSE-MIT, LICENSE-CC0, README.md, package.json, ci.yml; chưa chạy upstream |
| Bảo trì | Commit gần nhất 23/11/2026. |
| Nhận định | Thư viện prompt lớn nhất, nay là ứng dụng Next.js tự host (prompts.chat) kèm dữ liệu prompts.csv. Nội dung prompt CC0 dùng tự do, mã MIT. Số sao 143k+ trong README là tuyên bố tác giả **(chưa xác minh)**. |
| Nguồn | [LICENSE](https://github.com/f/prompts.chat/blob/32bbb1576e999fe57dc57d18eca9370e7ac46e24/LICENSE) · [LICENSE-MIT](https://github.com/f/prompts.chat/blob/32bbb1576e999fe57dc57d18eca9370e7ac46e24/LICENSE-MIT) · [LICENSE-CC0](https://github.com/f/prompts.chat/blob/32bbb1576e999fe57dc57d18eca9370e7ac46e24/LICENSE-CC0) · [README.md](https://github.com/f/prompts.chat/blob/32bbb1576e999fe57dc57d18eca9370e7ac46e24/README.md) · [package.json](https://github.com/f/prompts.chat/blob/32bbb1576e999fe57dc57d18eca9370e7ac46e24/package.json) · [ci.yml](https://github.com/f/prompts.chat/blob/32bbb1576e999fe57dc57d18eca9370e7ac46e24/.github/workflows/ci.yml) |

<a id="ch-baml"></a>

### BAML

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/BoundaryML/baml |
| License | Apache-2.0 |
| Phiên bản đã đọc | `ae11385a781c2b61a13fde186962132bbf1835fc` (commit 2026-11-21) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc LICENSE, README.md, package.json, go.mod, atb2-deploy.yml; chưa chạy upstream |
| Bảo trì | Commit gần nhất 21/11/2026. |
| Nhận định | Ngôn ngữ/toolchain có kiểu để viết hàm prompt và agent, codegen SDK nhiều ngôn ngữ, nhiều build workflow. Có telemetry CLI ẩn danh có thể tắt (TELEMETRY.md, đã đọc đầu file); định vị đã mở rộng từ DSL prompt sang ngôn ngữ cho agent. |
| Nguồn | [LICENSE](https://github.com/BoundaryML/baml/blob/ae11385a781c2b61a13fde186962132bbf1835fc/LICENSE) · [README.md](https://github.com/BoundaryML/baml/blob/ae11385a781c2b61a13fde186962132bbf1835fc/README.md) · [package.json](https://github.com/BoundaryML/baml/blob/ae11385a781c2b61a13fde186962132bbf1835fc/package.json) · [go.mod](https://github.com/BoundaryML/baml/blob/ae11385a781c2b61a13fde186962132bbf1835fc/go.mod) · [atb2-deploy.yml](https://github.com/BoundaryML/baml/blob/ae11385a781c2b61a13fde186962132bbf1835fc/.github/workflows/atb2-deploy.yml) |

<a id="ch-chainforge"></a>

### ChainForge

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/ianarawjo/ChainForge |
| License | MIT |
| Phiên bản đã đọc | `22af5549a3c154505ab92880fb7be9753c67ed4f` (commit 2026-10-29) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc LICENSE.md, README.md, docker-build.yml; chưa chạy upstream |
| Bảo trì | Commit gần nhất 29/10/2026. |
| Nhận định | Môi trường luồng dữ liệu trực quan để so sánh prompt x model và đo chất lượng bằng node đánh giá; chạy local (Flask) hoặc Docker. Con số 188 trong catalog chưa kiểm lại **(chưa xác minh)**. |
| Nguồn | [LICENSE.md](https://github.com/ianarawjo/ChainForge/blob/22af5549a3c154505ab92880fb7be9753c67ed4f/LICENSE.md) · [README.md](https://github.com/ianarawjo/ChainForge/blob/22af5549a3c154505ab92880fb7be9753c67ed4f/README.md) · [docker-build.yml](https://github.com/ianarawjo/ChainForge/blob/22af5549a3c154505ab92880fb7be9753c67ed4f/.github/workflows/docker-build.yml) |

<a id="ch-cl4r1t4s"></a>

### CL4R1T4S

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/elder-plinius/CL4R1T4S |
| License | AGPL-3.0 (file LICENSE) |
| Phiên bản đã đọc | `93a584765460c2fb0ad58380bba476f2149df138` (commit 2026-11-09) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc LICENSE, README.md; chưa chạy upstream |
| Bảo trì | Commit gần nhất 09/11/2026; một người duy trì. |
| Nhận định | Kho prompt hệ thống "trích xuất" của nhiều hãng/agent theo thư mục từng hãng. Tính xác thực của prompt là tuyên bố của người đóng góp **(chưa xác minh)**; AGPL chỉ chắc chắn cho phần biên soạn, bản quyền nội dung prompt thuộc hãng gốc. |
| Nguồn | [LICENSE](https://github.com/elder-plinius/CL4R1T4S/blob/93a584765460c2fb0ad58380bba476f2149df138/LICENSE) · [README.md](https://github.com/elder-plinius/CL4R1T4S/blob/93a584765460c2fb0ad58380bba476f2149df138/README.md) |

<a id="ch-claude-code-system-prompts"></a>

### Claude Code System Prompts

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/Piebald-AI/claude-code-system-prompts |
| License | MIT |
| Phiên bản đã đọc | `659d9f4cff186a44099048926a695647c0ba1814` (commit 2026-11-20) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc LICENSE, README.md; chưa chạy upstream |
| Bảo trì | Commit gần nhất 20/11/2026; bám phiên bản Claude Code v2.1.330. |
| Nhận định | Danh mục prompt/tool/agent/skill của Claude Code theo từng phiên bản, kèm số token và changelog. Giấy phép MIT chỉ áp cho phần biên soạn; prompt gốc thuộc Anthropic. |
| Nguồn | [LICENSE](https://github.com/Piebald-AI/claude-code-system-prompts/blob/659d9f4cff186a44099048926a695647c0ba1814/LICENSE) · [README.md](https://github.com/Piebald-AI/claude-code-system-prompts/blob/659d9f4cff186a44099048926a695647c0ba1814/README.md) |

<a id="ch-claude-cookbooks"></a>

### Claude Cookbooks

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/anthropics/claude-cookbooks |
| License | MIT |
| Phiên bản đã đọc | `8ad5de647d4f0f50c95d74aabc8aa20a3f70cdd3` (commit 2026-11-20) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc LICENSE, README.md, pyproject.toml, claude-link-review.yml; chưa chạy upstream |
| Bảo trì | Commit gần nhất 20/11/2026. |
| Nhận định | Tập notebook/hướng dẫn chính thức dựng ứng dụng với Claude, có registry.yaml/authors.yaml và CI kiểm notebook. Ví dụ phụ thuộc API Claude có phí. |
| Nguồn | [LICENSE](https://github.com/anthropics/claude-cookbooks/blob/8ad5de647d4f0f50c95d74aabc8aa20a3f70cdd3/LICENSE) · [README.md](https://github.com/anthropics/claude-cookbooks/blob/8ad5de647d4f0f50c95d74aabc8aa20a3f70cdd3/README.md) · [pyproject.toml](https://github.com/anthropics/claude-cookbooks/blob/8ad5de647d4f0f50c95d74aabc8aa20a3f70cdd3/pyproject.toml) · [claude-link-review.yml](https://github.com/anthropics/claude-cookbooks/blob/8ad5de647d4f0f50c95d74aabc8aa20a3f70cdd3/.github/workflows/claude-link-review.yml) |

<a id="ch-deepteam"></a>

### DeepTeam

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/confident-ai/deepteam |
| License | Apache-2.0 |
| Phiên bản đã đọc | `6306f0ff319a932955399405af82f78ee91e9370` (commit 2026-10-23) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc LICENSE.md, README.md, pyproject.toml, test_core.yml; chưa chạy upstream |
| Bảo trì | Commit gần nhất 23/10/2026; v1.0.10. |
| Nhận định | Khung red-team LLM/agent mô phỏng jailbreak, prompt injection, kèm guardrail, xây trên DeepEval. Telemetry bật trừ khi đặt DEEPTEAM_TELEMETRY_OPT_OUT=YES, cần tắt khi dùng với dữ liệu nhạy cảm. |
| Nguồn | [LICENSE.md](https://github.com/confident-ai/deepteam/blob/6306f0ff319a932955399405af82f78ee91e9370/LICENSE.md) · [README.md](https://github.com/confident-ai/deepteam/blob/6306f0ff319a932955399405af82f78ee91e9370/README.md) · [pyproject.toml](https://github.com/confident-ai/deepteam/blob/6306f0ff319a932955399405af82f78ee91e9370/pyproject.toml) · [test_core.yml](https://github.com/confident-ai/deepteam/blob/6306f0ff319a932955399405af82f78ee91e9370/.github/workflows/test_core.yml) |

<a id="ch-dotprompt"></a>

### Dotprompt

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/google/dotprompt |
| License | Apache-2.0 |
| Phiên bản đã đọc | `97751971e864662d67bc329911cce9f4dfab378c` (commit 2026-11-18) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc LICENSE, README.md, package.json, bazel.yml; chưa chạy upstream |
| Bảo trì | Commit gần nhất 18/11/2026. |
| Nhận định | Định dạng file prompt thực thi (Handlebars) trung lập ngôn ngữ/nhà cung cấp, có nhiều thư viện runtime song song. Mức hoàn thiện từng ngôn ngữ khác nhau, chưa kiểm. |
| Nguồn | [LICENSE](https://github.com/google/dotprompt/blob/97751971e864662d67bc329911cce9f4dfab378c/LICENSE) · [README.md](https://github.com/google/dotprompt/blob/97751971e864662d67bc329911cce9f4dfab378c/README.md) · [package.json](https://github.com/google/dotprompt/blob/97751971e864662d67bc329911cce9f4dfab378c/package.json) · [bazel.yml](https://github.com/google/dotprompt/blob/97751971e864662d67bc329911cce9f4dfab378c/.github/workflows/bazel.yml) |

<a id="ch-fabric"></a>

### Fabric

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/danielmiessler/Fabric |
| License | MIT |
| Phiên bản đã đọc | `9a906e7c7fb81a25885c41d3eb7ba1b0e2f9a98a` (commit 2026-11-22) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc LICENSE, README.md, go.mod, ci.yml; chưa chạy upstream |
| Bảo trì | Commit gần nhất 22/11/2026. |
| Nhận định | CLI Go và thư viện pattern system.md theo tác vụ thực tế, dùng nhiều nhà cung cấp LLM. Số pattern hiện 268 thư mục; chưa đánh giá chất lượng pattern. |
| Nguồn | [LICENSE](https://github.com/danielmiessler/Fabric/blob/9a906e7c7fb81a25885c41d3eb7ba1b0e2f9a98a/LICENSE) · [README.md](https://github.com/danielmiessler/Fabric/blob/9a906e7c7fb81a25885c41d3eb7ba1b0e2f9a98a/README.md) · [go.mod](https://github.com/danielmiessler/Fabric/blob/9a906e7c7fb81a25885c41d3eb7ba1b0e2f9a98a/go.mod) · [ci.yml](https://github.com/danielmiessler/Fabric/blob/9a906e7c7fb81a25885c41d3eb7ba1b0e2f9a98a/.github/workflows/ci.yml) |

<a id="ch-guidance"></a>

### Guidance

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/guidance-ai/guidance |
| License | MIT |
| Phiên bản đã đọc | `21b1d90dfbebff4b141df70c714c8af15aa5f4af` (commit 2026-05-21) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc LICENSE.md, README.md, pyproject.toml, call_cpu_tests.yml; chưa chạy upstream |
| Bảo trì | Commit gần nhất 21/05/2026, gần 6 tháng không commit. |
| Nhận định | Mô hình lập trình điều khiển sinh có ràng buộc, nhiều backend (Transformers, llama.cpp, OpenAI). Hoạt động chậm lại rõ rệt từ 5/2026, cân nhắc khi chọn dài hạn. |
| Nguồn | [LICENSE.md](https://github.com/guidance-ai/guidance/blob/21b1d90dfbebff4b141df70c714c8af15aa5f4af/LICENSE.md) · [README.md](https://github.com/guidance-ai/guidance/blob/21b1d90dfbebff4b141df70c714c8af15aa5f4af/README.md) · [pyproject.toml](https://github.com/guidance-ai/guidance/blob/21b1d90dfbebff4b141df70c714c8af15aa5f4af/pyproject.toml) · [call_cpu_tests.yml](https://github.com/guidance-ai/guidance/blob/21b1d90dfbebff4b141df70c714c8af15aa5f4af/.github/workflows/call_cpu_tests.yml) |

<a id="ch-instructor"></a>

### Instructor

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/567-labs/instructor |
| License | MIT |
| Phiên bản đã đọc | `0acb3a19c3ec6f89c6a204340c52a30ee33fa04b` (commit 2026-11-18) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc LICENSE, README.md, pyproject.toml, evals.yml; chưa chạy upstream |
| Bảo trì | Commit gần nhất 18/11/2026; v1.18.0. |
| Nhận định | Structured output kiểm bằng Pydantic, đa nhà cung cấp LLM, có evals chạy hằng tuần. Repo thuộc tổ chức 567-labs, tên cũ của tác giả cá nhân có thể còn xuất hiện ở tài liệu cũ. |
| Nguồn | [LICENSE](https://github.com/567-labs/instructor/blob/0acb3a19c3ec6f89c6a204340c52a30ee33fa04b/LICENSE) · [README.md](https://github.com/567-labs/instructor/blob/0acb3a19c3ec6f89c6a204340c52a30ee33fa04b/README.md) · [pyproject.toml](https://github.com/567-labs/instructor/blob/0acb3a19c3ec6f89c6a204340c52a30ee33fa04b/pyproject.toml) · [evals.yml](https://github.com/567-labs/instructor/blob/0acb3a19c3ec6f89c6a204340c52a30ee33fa04b/.github/workflows/evals.yml) |

<a id="ch-open-prompt-injection"></a>

### Open-Prompt-Injection

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/liu00222/Open-Prompt-Injection |
| License | MIT |
| Phiên bản đã đọc | `fbed5cca347488f88363790ae3ae97c56116da6a` (commit 2026-09-27) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc LICENSE, README.md; chưa chạy upstream |
| Bảo trì | Commit gần nhất 27/09/2026. |
| Nhận định | Bộ công cụ nghiên cứu để cài đặt và đánh giá tấn công/phòng thủ prompt injection. Mã học thuật, không có workflow CI, chưa chạy nên chưa rõ độ tái lập. |
| Nguồn | [LICENSE](https://github.com/liu00222/Open-Prompt-Injection/blob/fbed5cca347488f88363790ae3ae97c56116da6a/LICENSE) · [README.md](https://github.com/liu00222/Open-Prompt-Injection/blob/fbed5cca347488f88363790ae3ae97c56116da6a/README.md) |

<a id="ch-openai-cookbook"></a>

### OpenAI Cookbook

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/openai/openai-cookbook |
| License | MIT |
| Phiên bản đã đọc | `dfd760b4de0bd175b51ad05b9b5260c36dfea09c` (commit 2026-11-16) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc LICENSE, README.md, stale.yaml; chưa chạy upstream |
| Bảo trì | Commit gần nhất 16/11/2026. |
| Nhận định | Ví dụ và bài viết chính thức về OpenAI API, đọc trên cookbook.openai.com. Ví dụ phụ thuộc API OpenAI có phí. |
| Nguồn | [LICENSE](https://github.com/openai/openai-cookbook/blob/dfd760b4de0bd175b51ad05b9b5260c36dfea09c/LICENSE) · [README.md](https://github.com/openai/openai-cookbook/blob/dfd760b4de0bd175b51ad05b9b5260c36dfea09c/README.md) · [stale.yaml](https://github.com/openai/openai-cookbook/blob/dfd760b4de0bd175b51ad05b9b5260c36dfea09c/.github/workflows/stale.yaml) |

<a id="ch-outlines"></a>

### Outlines

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/dottxt-ai/outlines |
| License | Apache-2.0 |
| Phiên bản đã đọc | `c52af8472c6fe8a607a733ec11b709476af77a96` (commit 2026-08-24) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc LICENSE, README.md, pyproject.toml, build_documentation.yml; chưa chạy upstream |
| Bảo trì | Commit gần nhất 24/08/2026, khoảng 3 tháng trước ngày kiểm. |
| Nhận định | Thư viện structured generation ràng buộc lúc decode (JSON Schema/regex/grammar). Tốc độ commit chậm hơn các repo cùng nhóm; README có phần chào mời dịch vụ thương mại. |
| Nguồn | [LICENSE](https://github.com/dottxt-ai/outlines/blob/c52af8472c6fe8a607a733ec11b709476af77a96/LICENSE) · [README.md](https://github.com/dottxt-ai/outlines/blob/c52af8472c6fe8a607a733ec11b709476af77a96/README.md) · [pyproject.toml](https://github.com/dottxt-ai/outlines/blob/c52af8472c6fe8a607a733ec11b709476af77a96/pyproject.toml) · [build_documentation.yml](https://github.com/dottxt-ai/outlines/blob/c52af8472c6fe8a607a733ec11b709476af77a96/.github/workflows/build_documentation.yml) |

<a id="ch-prompt-engineering-guide"></a>

### Prompt Engineering Guide

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/dair-ai/Prompt-Engineering-Guide |
| License | MIT |
| Phiên bản đã đọc | `57673726396dd94acb23bdb1e67f27c78ee85a8e` (commit 2026-03-11) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc LICENSE.md, README.md, package.json, claude-code-review.yml; chưa chạy upstream |
| Bảo trì | Commit gần nhất 11/03/2026, hơn 8 tháng trước. |
| Nhận định | Tập hướng dẫn, bài báo, notebook về prompt engineering và web promptingguide.ai. Nội dung đứng yên từ 3/2026, README quảng bá khoá học của DAIR.AI Academy. |
| Nguồn | [LICENSE.md](https://github.com/dair-ai/Prompt-Engineering-Guide/blob/57673726396dd94acb23bdb1e67f27c78ee85a8e/LICENSE.md) · [README.md](https://github.com/dair-ai/Prompt-Engineering-Guide/blob/57673726396dd94acb23bdb1e67f27c78ee85a8e/README.md) · [package.json](https://github.com/dair-ai/Prompt-Engineering-Guide/blob/57673726396dd94acb23bdb1e67f27c78ee85a8e/package.json) · [claude-code-review.yml](https://github.com/dair-ai/Prompt-Engineering-Guide/blob/57673726396dd94acb23bdb1e67f27c78ee85a8e/.github/workflows/claude-code-review.yml) |

<a id="ch-prompt-engineering-interactive-tutorial"></a>

### Prompt Engineering Interactive Tutorial

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/anthropics/prompt-eng-interactive-tutorial |
| License | không có file LICENSE |
| Phiên bản đã đọc | `0d277542e927652da25b0014c9b346723af55881` (commit 2024-04-07) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md; chưa chạy upstream |
| Bảo trì | Commit gần nhất 07/04/2024, gần như bỏ ngỏ. |
| Nhận định | Khoá thực hành prompt cho Claude bằng notebook, có bản 1P và Bedrock. Không có giấy phép nên chưa rõ quyền tái sử dụng; nội dung đứng yên từ 4/2024. |
| Nguồn | [README.md](https://github.com/anthropics/prompt-eng-interactive-tutorial/blob/0d277542e927652da25b0014c9b346723af55881/README.md) |

<a id="ch-prompt-optimizer"></a>

### Prompt Optimizer

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/linshenkx/prompt-optimizer |
| License | AGPL-3.0-only |
| Phiên bản đã đọc | `5ae83f476bfd8704308a4bbeee65dcd5860b0f47` (commit 2026-11-23) |
| Kiểm chứng | 2026-11-23; code-read; đã đọc README, LICENSE, package.json, docker-compose.yml, generate-auth.sh, generate-config.sh, nginx.conf, docker.yml, CHANGELOG; chưa chạy upstream |
| Bảo trì | Hoạt động tích cực: commit 2026-11-23, bản 2.16.2 cùng ngày. |
| Nhận định | Công cụ tối ưu prompt chạy dạng web, desktop, extension Chrome, Docker và MCP server (monorepo pnpm). Đã đọc docker/*.sh, compose và nginx.conf: mật khẩu mặc định 123456, khóa API đặt qua VITE_* bị chép vào config.js phía client và in ra log khởi động, /mcp không qua Basic auth; chỉ đọc cấu hình, chưa chạy. |
| Nguồn | [README](https://github.com/linshenkx/prompt-optimizer/blob/5ae83f476bfd8704308a4bbeee65dcd5860b0f47/README.md) · [LICENSE](https://github.com/linshenkx/prompt-optimizer/blob/5ae83f476bfd8704308a4bbeee65dcd5860b0f47/LICENSE) · [package.json](https://github.com/linshenkx/prompt-optimizer/blob/5ae83f476bfd8704308a4bbeee65dcd5860b0f47/package.json) · [docker-compose.yml](https://github.com/linshenkx/prompt-optimizer/blob/5ae83f476bfd8704308a4bbeee65dcd5860b0f47/docker/docker-compose.yml) · [generate-auth.sh](https://github.com/linshenkx/prompt-optimizer/blob/5ae83f476bfd8704308a4bbeee65dcd5860b0f47/docker/generate-auth.sh) · [generate-config.sh](https://github.com/linshenkx/prompt-optimizer/blob/5ae83f476bfd8704308a4bbeee65dcd5860b0f47/docker/generate-config.sh) · [nginx.conf](https://github.com/linshenkx/prompt-optimizer/blob/5ae83f476bfd8704308a4bbeee65dcd5860b0f47/docker/nginx.conf) · [docker.yml](https://github.com/linshenkx/prompt-optimizer/blob/5ae83f476bfd8704308a4bbeee65dcd5860b0f47/.github/workflows/docker.yml) · [CHANGELOG](https://github.com/linshenkx/prompt-optimizer/blob/5ae83f476bfd8704308a4bbeee65dcd5860b0f47/CHANGELOG.md) |

<a id="ch-prompty"></a>

### Prompty

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/microsoft/prompty |
| License | MIT |
| Phiên bản đã đọc | `a4e8dcd2d79d641bb6bb52eb3177777fc55129cb` (commit 2026-10-21) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README, LICENSE; chưa chạy upstream |
| Bảo trì | Commit gần nhất 2026-10-21; nhiều workflow CI theo từng runtime (chỉ đọc danh sách, chưa mở nội dung). |
| Nhận định | Định dạng file .prompty (markdown + YAML) cho prompt LLM, có spec/, schema/ và fixtures đối chiếu giữa các runtime; extension VS Code. Mức trưởng thành từng runtime là tuyên bố của README **(chưa xác minh)**; thư mục go/java/swift có mặt nhưng README không liệt kê là gói phát hành. |
| Nguồn | [README](https://github.com/microsoft/prompty/blob/a4e8dcd2d79d641bb6bb52eb3177777fc55129cb/README.md) · [LICENSE](https://github.com/microsoft/prompty/blob/a4e8dcd2d79d641bb6bb52eb3177777fc55129cb/LICENSE) |

<a id="ch-skillopt"></a>

### SkillOpt

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/microsoft/SkillOpt |
| License | MIT |
| Phiên bản đã đọc | `dc0b5e654cafa1073a2819086151c1e0d13012f0` (commit 2026-11-23) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README, LICENSE, pyproject.toml, ci.yml; chưa chạy upstream |
| Bảo trì | Hoạt động tích cực: commit 2026-11-23; pyproject 0.2.0 (Alpha). |
| Nhận định | Khung "huấn luyện" skill/prompt của agent bằng vòng phản chiếu có cổng validation held-out (epoch, batch, learning rate); có skillopt_sleep đọc transcript agent và plugin cho nhiều agent. Số liệu paper/benchmark là tự công bố **(chưa xác minh)**; pyproject ghi Development Status Alpha. |
| Nguồn | [README](https://github.com/microsoft/SkillOpt/blob/dc0b5e654cafa1073a2819086151c1e0d13012f0/README.md) · [LICENSE](https://github.com/microsoft/SkillOpt/blob/dc0b5e654cafa1073a2819086151c1e0d13012f0/LICENSE) · [pyproject.toml](https://github.com/microsoft/SkillOpt/blob/dc0b5e654cafa1073a2819086151c1e0d13012f0/pyproject.toml) · [ci.yml](https://github.com/microsoft/SkillOpt/blob/dc0b5e654cafa1073a2819086151c1e0d13012f0/.github/workflows/ci.yml) |

<a id="ch-system-prompts-and-models-of-ai-tools"></a>

### system-prompts-and-models-of-ai-tools

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools |
| License | GPL-3.0 (LICENSE.md) (khác catalog cũ) |
| Phiên bản đã đọc | `162db92f54d717d8ebd12292e155aeef32bb4b3c` (commit 2026-10-12) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README, LICENSE.md; chưa chạy upstream |
| Bảo trì | Commit gần nhất 2026-10-12; còn cập nhật. |
| Nhận định | Bộ sưu tập system prompt và định nghĩa tool của nhiều sản phẩm AI, tổ chức theo thư mục từng hãng; README chủ yếu là quảng bá, tài trợ và ví crypto, không mô tả cách thu thập hay kiểm chứng tính xác thực **(chưa xác minh)**. GPL-3.0 chỉ áp cho phần tác giả repo; bản quyền văn bản prompt thuộc các hãng, nên chỉ dùng để học cấu trúc. |
| Nguồn | [README](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools/blob/162db92f54d717d8ebd12292e155aeef32bb4b3c/README.md) · [LICENSE.md](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools/blob/162db92f54d717d8ebd12292e155aeef32bb4b3c/LICENSE.md) |

<a id="ch-system-prompts-leaks"></a>

### System Prompts Leaks

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/asgeirtj/system_prompts_leaks |
| License | CC0-1.0 (phần biên soạn) |
| Phiên bản đã đọc | `8c615a1387fec799b96f28d30617aab98d196afd` (commit 2026-11-23) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README, LICENSE; chưa chạy upstream |
| Bảo trì | Hoạt động tích cực: commit 2026-11-23. |
| Nhận định | Kho sao chép system prompt công khai/rò rỉ của nhiều chatbot, tổ chức theo hãng (Anthropic, OpenAI, Google, xAI...), cập nhật liên tục. README không nêu cách trích xuất hay kiểm chứng tính chân thực **(chưa xác minh)**; CC0 không chuyển quyền của chủ sở hữu văn bản gốc. |
| Nguồn | [README](https://github.com/asgeirtj/system_prompts_leaks/blob/8c615a1387fec799b96f28d30617aab98d196afd/README.md) · [LICENSE](https://github.com/asgeirtj/system_prompts_leaks/blob/8c615a1387fec799b96f28d30617aab98d196afd/LICENSE) |

<a id="ch-textgrad"></a>

### TextGrad

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/zou-group/textgrad |
| License | MIT |
| Phiên bản đã đọc | `75e912e210864b61999781778cdf756d4468120f` (commit 2025-07-25) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README, LICENSE, setup.py; chưa chạy upstream |
| Bảo trì | Commit gần nhất 2025-07-25 (hơn 4 tháng trước ngày kiểm), mức hoạt động thấp. |
| Nhận định | Khung "autograd bằng văn bản": LLM đưa phản hồi ngôn ngữ làm gradient để tối ưu prompt/lời giải; có bài Nature, thư mục evaluation và notebook ví dụ. Kết quả trong paper là tuyên bố tác giả **(chưa xác minh)**. |
| Nguồn | [README](https://github.com/zou-group/textgrad/blob/75e912e210864b61999781778cdf756d4468120f/README.md) · [LICENSE](https://github.com/zou-group/textgrad/blob/75e912e210864b61999781778cdf756d4468120f/LICENSE) · [setup.py](https://github.com/zou-group/textgrad/blob/75e912e210864b61999781778cdf756d4468120f/setup.py) |

<a id="n2-2026-11-24"></a>

## Nâng trần đợt hai — 23/11/2026

Hồ sơ lập trong đợt nâng trần thứ hai: đọc mã hoặc tài liệu tại commit cố định, chưa chạy upstream; mô tả của trinh sát sai ở nhiều repo nên điều ghi ở đây là điều đã đọc.

<a id="n2-promptory"></a>

### Promptory

| Thuộc tính | Giá trị |
|---|---|
| Repo | https://github.com/hsanchez/promptory |
| License | Apache-2.0 |
| Phiên bản đã đọc | `10bea0a5be28aa95219c25fff33cf305749077ad` (commit 2026-05-29) |
| Kiểm chứng | 2026-11-24; code-read; đã đọc README.md, pyproject.toml, gates.py, lint.py, metadata.py, evidence.py, serve.py, prek.toml, LICENSE; chưa chạy upstream |
| Khoảng trống lấp | Prompt như mã: registry, lint, hồi quy CI và cổng phát hành có bằng chứng |
| Cơ chế đáng học | - `metadata.py`: `write_metadata` ghi checksum SHA-256 từng file lúc release, `verify_metadata` báo `checksum mismatch`/`file missing`.<br>- `gates.py`: mỗi gate `(kind, name, required_status)` trong `promptspec.yaml` thất bại nếu thiếu bằng chứng, bị thu hồi hoặc sai trạng thái.<br>- `evidence.py`: bằng chứng JSON bất biến (kind, name, status, tool, created_at), so sánh metric giữa hai bản; `lifecycle.jsonl` ghi sự kiện chỉ thêm.<br>- `lint.py`: biến Jinja phải khớp `required_variables`, YAML hợp lệ, kích thước ≤ `max_file_bytes`. |
| Tiêu chí và cách kiểm | `prompt check` (lint), `prompt verify` (checksum), `prompt gate --format github/json` cho CI. Kiểm trước khi commit bằng prek (ruff, ty, pytest, 130 hàm test đếm bằng grep). Không có `.github/workflows` tại commit này. Evidence do công cụ ngoài tạo, Promptory không xác thực nội dung. |
| Giới hạn và rủi ro | - Apache-2.0, phụ thuộc jinja2, pyyaml, typer, rich; `serve` tuỳ chọn thêm FastAPI.<br>- Cổng chỉ tin file bằng chứng tự khai; ai ghi được file thì làm gate xanh.<br>- Sidecar `serve.py` không có xác thực, chỉ nên đặt nội bộ.<br>- Dự án mới, một commit, chưa có phát hành; thư mục `.claude/settings.local.json` bị commit (cho phép `gh api`). |
| So với | promptfoo (chạy eval và red team, không quản lý phiên bản), dotprompt và prompty (định dạng file prompt), langfuse (prompt registry kèm tracing, dịch vụ) |
| Nguồn | [README.md](https://github.com/hsanchez/promptory/blob/10bea0a5be28aa95219c25fff33cf305749077ad/README.md) · [LICENSE](https://github.com/hsanchez/promptory/blob/10bea0a5be28aa95219c25fff33cf305749077ad/LICENSE) · [pyproject.toml](https://github.com/hsanchez/promptory/blob/10bea0a5be28aa95219c25fff33cf305749077ad/pyproject.toml) · [gates.py](https://github.com/hsanchez/promptory/blob/10bea0a5be28aa95219c25fff33cf305749077ad/src/promptory/gates.py) · [lint.py](https://github.com/hsanchez/promptory/blob/10bea0a5be28aa95219c25fff33cf305749077ad/src/promptory/lint.py) · [metadata.py](https://github.com/hsanchez/promptory/blob/10bea0a5be28aa95219c25fff33cf305749077ad/src/promptory/metadata.py) · [evidence.py](https://github.com/hsanchez/promptory/blob/10bea0a5be28aa95219c25fff33cf305749077ad/src/promptory/evidence.py) · [serve.py](https://github.com/hsanchez/promptory/blob/10bea0a5be28aa95219c25fff33cf305749077ad/src/promptory/serve.py) · [prek.toml](https://github.com/hsanchez/promptory/blob/10bea0a5be28aa95219c25fff33cf305749077ad/prek.toml) |
