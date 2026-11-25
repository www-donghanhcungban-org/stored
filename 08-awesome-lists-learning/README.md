# 08 · Awesome Lists, Repo học tập & Repo nổi tiếng nhất GitHub

## 1. Repo nhiều sao nhất toàn GitHub (9–10/2026, ước lượng)

| # | Repo | ★ | Nội dung |
|---|---|---|---|
| 1 | codecrafters-io/build-your-own-x | ~547–552k | Tự xây lại công nghệ từ đầu (DB, OS, compiler…) |
| 2 | sindresorhus/awesome | ~400k+ | Awesome của mọi awesome |
| 3 | public-apis/public-apis | ~380k+ | API công khai |
| 4 | freeCodeCamp/freeCodeCamp | ~455k | Chương trình học lập trình miễn phí |
| 7–8 | kamranahmedse/developer-roadmap | ~360–368k | Lộ trình nghề (frontend, backend, AI engineer…) |
| 7–8 | donnemartin/system-design-primer | ~357–372k | Thiết kế hệ thống |
| – | openclaw/openclaw | ~390k | Agent cá nhân (xem mục 02) |

Theo dõi tự động: `EvanLi/Github-Ranking` (cập nhật hằng ngày), gitstarclub.com/rankings.

## 2. Awesome list theo chủ đề của kho này

| Chủ đề | Repo | Ghi chú |
|---|---|---|
| LLM apps / agents thực hành | `Shubhamsaboo/awesome-llm-apps` (~105k★) | 100+ agent, skill, RAG app có code |
| Claude Code | `hesreallyhim/awesome-claude-code` (~37–55k★) · `rohitg00/awesome-claude-code-toolkit` | Skills, hooks, commands, agents, plugins |
| Agent skills | `VoltAgent/awesome-agent-skills` (1000+) · `spencerpauly/awesome-cursor-skills` | Tương thích Claude Code/Codex/Gemini CLI/Cursor |
| Cursor rules (legacy) | `PatrickJS/awesome-cursorrules` · cursor.directory | Chuyển dần sang skills |
| Agent frameworks | `kaushikb11/awesome-llm-agents` · `aloth/awesome-ai-agents` · `e2b-dev/awesome-ai-agents` | |
| MCP | `wong2/awesome-mcp-servers` · `punkpeye/awesome-mcp-servers` · `sadekxD/Awesome-MCP` | |
| Generative UI | `narrowin/awesome-generative-ui` | LLM sinh UI động |
| AI tools cho UI | `maxbogo/awesome-ai-tools-for-ui` | Gồm Taste Skill, Refactoring UI skill |
| Design systems | `klaufel/awesome-design-systems` | |
| Design resources | `bradtraversy/design-resources-for-developers` | |
| Prompt engineering | `dair-ai/Prompt-Engineering-Guide` · `f/awesome-chatgpt-prompts` | |
| GitHub topics | github.com/topics/agent-skills · /claude-skills · /awesome-ai · /ai-agents | Khám phá theo tag |

## 2b. Khoá học & repo học LLM/agent chất lượng cao (đã xác minh 2026-10-12)

| Repo | ★ (12/10) | License | Hoạt động gần nhất | Vì sao đáng học | Lưu ý |
|---|---|---|---|---|---|
| **microsoft/generative-ai-for-beginners** | 121,2k | MIT | 12/10/2026 | 21 bài, hơn 50 bản dịch **có tiếng Việt** (`translations/vi`) | Thiên về Azure; README báo vài bài cũ sau khi GitHub Models ngừng (chưa tự kiểm) |
| **rasbt/LLMs-from-scratch** | 106,4k | Apache-2.0 | 2/10/2026 | Code đi kèm sách Manning *Build a LLM (From Scratch)*, chương 1–7 + phụ lục; vẫn cập nhật | Phần giải thích đầy đủ nằm trong sách trả phí |
| **mlabonne/llm-course** | 83,5k | Apache-2.0 | 2/2026 | Lộ trình 3 nhánh (nền tảng, LLM Scientist, LLM Engineer) + notebook Colab | Phần lớn là link tuyển chọn; ít commit |
| **microsoft/ai-agents-for-beginners** | 77,0k | MIT | 12/10/2026 | 18 bài về agent, rất tích cực (2.067 commit), **có bản tiếng Việt** | Gắn với Microsoft Agent Framework / Foundry (mục 02) |
| **labmlai/annotated_deep_learning_paper_implementations** | 67,5k | MIT | 1/2026 | Hơn 60 paper cài bằng PyTorch, chú thích từng dòng (nn.labml.ai) | README nói thêm hằng tuần nhưng commit cuối 1/2026 |
| **karpathy/nanochat** | 58,6k | MIT | 7/2026 | Karpathy: ChatGPT tối giản toàn bộ chuỗi tokenizer → pretrain → SFT → eval → inference, ~US$48 (~2 giờ trên 8×H100) | Chạy đầy đủ cần node 8×H100. **nanoGPT (63,7k★) đã deprecated** và trỏ sang nanochat; llm.c (31,1k★) không commit từ 5/2025 |
| **huggingface/agents-course** | 33,5k | Apache-2.0 | 6/10/2026 | 4 unit có chứng chỉ, bài cuối chấm trên leaderboard; smolagents, LangGraph, LlamaIndex | Thiên về hệ sinh thái HF |
| **NirDiamant/RAG_Techniques** | 29,8k | **phi thương mại (riêng)** | 11/10/2026 | Hơn 42 notebook RAG chạy được, rộng nhất hiện có | Cấm dùng thương mại; README nhiều quảng cáo. GenAI_Agents (24,6k★) cùng tác giả cũng license phi thương mại |
| **chiphuyen/aie-book** | 17,8k | không có LICENSE | 7/2026 | Tài liệu đi kèm sách *AI Engineering* (O'Reilly): mục lục, tóm tắt, case study | Không phải nội dung sách; ít code |

Thứ tự gợi ý cho người mới: `generative-ai-for-beginners` (bản tiếng Việt) → `ai-agents-for-beginners` → `agents-course` (có bài chấm) → `LLMs-from-scratch` hoặc `nanochat` nếu muốn hiểu bên trong model.

## 2c. Kiểm ảnh "AI Engineer Interview Questions" (ảnh người dùng gửi, 2026-10-12)

> Infographic 20 ô, mỗi ô một câu hỏi + câu trả lời 1–2 dòng, ghi tên **Rathnakumar Udayakumar (@rathanuday)**. Kiểm từng câu trả lời với nguồn gốc (paper, docs nhà cung cấp, OWASP) và chỉ chỗ trong kho có câu trả lời sâu hơn.

### 2c.1 Hồ sơ nguồn

| Mục | Thông tin (12/10/2026) |
|---|---|
| Người đăng | Rathnakumar Udayakumar (LinkedIn `rathanuday`, ~48,9k follower theo trang bài đăng). Nền tảng **quản lý sản phẩm**, không phải kỹ sư ML: theo ZoomInfo từng là Senior PM ở IBM, Product Lead ở Clara Analytics, Product Leader ở Netradyne, nay đồng sáng lập Open Atlas và Nextazy **(nguồn tổng hợp bên thứ ba, chưa xác minh)**; có 2 sách tự xuất bản (*Product Management 101*, *The ABCs of Data Science*). GitHub `rathanuday` không có repo công khai |
| Kiểu nội dung | Infographic giải thích AI/LLM (agent, RAG, failure mode, câu hỏi phỏng vấn) trên LinkedIn; cuối bài thường quảng bá dịch vụ tư vấn visa O-1/EB-1A và cộng đồng Open Atlas |
| Gốc của ảnh | Không tìm thấy bài gốc đã đánh chỉ mục; không thấy bản sớm hơn ghi tên người khác. Tự thiết kế hay đăng lại: **(chưa xác minh)** |

### 2c.2 Từng ô: đúng tới đâu, thiếu gì, đọc thêm ở đâu

Ký hiệu: ✅ đúng và đủ cho mức "câu trả lời 30 giây" · ⚠️ đúng nhưng thiếu ý mà người phỏng vấn sẽ hỏi tiếp · ❌ sai hoặc lỗi thời.

| # | Câu hỏi | Ảnh trả lời | Đánh giá | Ý cần bổ sung khi trả lời thật | Đọc sâu trong kho |
|---|---|---|---|---|---|
| 01 | LLM là gì, hoạt động ra sao | Dự đoán token kế tiếp, transformer, dữ liệu lớn | ⚠️ | Chỉ đúng với giai đoạn pretrain; model chat còn qua **post-training** (SFT, RLHF/RLAIF, DPO). Nên nói thêm tokenizer và cửa sổ ngữ cảnh | mục 08 §2b (`LLMs-from-scratch`, `nanochat`) |
| 02 | Kiến trúc transformer | Self-Attention → Feed-Forward → Add & Norm; "xử lý song song" | ⚠️ | Sơ đồ đặt Add & Norm **một lần ở cuối**, trong khi mỗi sublayer (attention, FFN) đều có residual + norm riêng; paper gốc dùng post-LN, LLM hiện đại dùng **pre-LN/RMSNorm**. Thiếu multi-head, positional encoding (RoPE), causal mask. "Song song" đúng khi train/prefill, còn **sinh token vẫn tuần tự** (KV cache) | mục 08 §2b; mục 10 §1 (inference) |
| 03 | RAG là gì, vì sao dùng | Truy xuất dữ liệu ngoài để grounding, giảm hallucination | ✅ | Giảm chứ không loại bỏ hallucination; truy xuất sai sinh lỗi mới. Nêu lý do thứ hai: dữ liệu mới/riêng tư mà không cần huấn luyện lại | mục 10 §3 |
| 04 | Embedding hoạt động ra sao | Văn bản → vector nhiều chiều mang nghĩa | ✅ | So bằng cosine/dot product; query và tài liệu phải dùng **cùng model**; đổi model là phải embed lại toàn bộ | mục 10 §2, mục 18 (embedding tiếng Việt) |
| 05 | Fine-tuning khác prompting | Prompting ở inference, fine-tuning đổi trọng số | ⚠️ | Thiếu lựa chọn thứ ba là RAG và tiêu chí chọn: prompting → RAG (thiếu kiến thức) → fine-tuning (thiếu hành vi/định dạng, cần rẻ hơn ở quy mô). Nhắc LoRA/PEFT | mục 17 §2, mục 07 (Overmind: trace → LoRA) |
| 06 | Đánh giá hệ LLM/RAG | Accuracy, relevance, faithfulness, correctness, human eval | ⚠️ | Tách **eval truy xuất** (recall@k, MRR) và **eval sinh** (faithfulness, answer relevance); cần golden dataset; LLM-as-judge phải hiệu chỉnh với nhãn người; chạy eval trong CI | mục 07 |
| 07 | Metric phổ biến | BLEU/ROUGE, faithfulness, relevance, context precision/recall, human eval | ⚠️ | BLEU/ROUGE đo trùng n-gram, **tương quan kém với đánh giá của người** cho văn bản mở; chỉ hợp với dịch/tóm tắt có đáp án. Thiếu LLM-as-judge, pass@k (code), tỉ lệ hoàn thành task (agent), chi phí và độ trễ | mục 07 (Ragas, DeepEval, Promptfoo, Inspect AI) |
| 08 | Xử lý hallucination | RAG nguồn tin cậy, trích dẫn, guardrail, kiểm output, người duyệt | ✅ | Trích dẫn cũng có thể bịa → kiểm trích dẫn khớp đoạn nguồn; cho phép model trả "không biết"; structured output + validate schema | mục 12 §2, mục 17 §2b |
| 09 | Agent là gì | Plan → Act → Observe, dùng tool, vòng phản hồi | ✅ | Đây là ReAct. Thiếu **điều kiện dừng** và ngân sách (số bước, token, tiền) — câu hỏi tiếp theo hay gặp | mục 03 §1–2, mục 21 §8 |
| 10 | Thiết kế multi-agent | Vai trò, giao thức, bộ nhớ chung, điều phối | ⚠️ | Thiếu câu "**có nên dùng không**": Anthropic khuyên "tìm giải pháp đơn giản nhất, chỉ thêm phức tạp khi cần"; theo bài về hệ research của họ, agent đơn tốn ~4× và multi-agent ~15× token so với chat. Nêu A2A, cách cô lập (git worktree) và cách gộp kết quả | mục 03 §1, §5; mục 04 §3 |
| 11 | Tool calling | LLM gọi API, hàm, hệ thống ngoài | ⚠️ | Chính xác hơn: model chỉ **sinh lời gọi có cấu trúc** (tên + JSON tham số); **ứng dụng** thực thi và trả kết quả (ngoại lệ: "server tool" như web search do nhà cung cấp chạy). Điểm này quyết định chỗ đặt kiểm quyền. Nêu MCP | mục 04 §2, mục 12 |
| 12 | Xây context cho agent | Bộ nhớ ngắn hạn, dài hạn, kiến thức truy xuất | ⚠️ | Thiếu **context engineering**: output tool chiếm phần lớn cửa sổ, compaction/tóm tắt, context rot, giữ dữ liệu lớn ngoài cửa sổ | mục 03 §4, §8b (context-mode); mục 10 §4 |
| 13 | MLOps | CI/CD, model registry, monitoring, retrain, versioning | ✅ | Với ứng dụng LLM gọi API: **version prompt**, ghim phiên bản model, eval chạy trong CI thay cho retrain | mục 07, mục 13 §4 |
| 14 | Giám sát production | Độ trễ, lỗi, chi phí, drift, chất lượng output, alert | ✅ | Thêm **tracing** từng bước agent (OpenTelemetry GenAI), phản hồi người dùng làm tín hiệu chất lượng | mục 07 (Langfuse, Phoenix, OpenLLMetry) |
| 15 | Xử lý dữ liệu | Nguồn tin cậy, làm sạch, privacy, bộ eval | ✅ | Thêm phân quyền tài liệu khi truy xuất (người dùng chỉ thấy tài liệu họ được phép xem) | mục 12 |
| 16 | Model drift | Phân phối dữ liệu đổi; kiểm thống kê, phân phối embedding | ✅ | Với API: nhà cung cấp **đổi model ngầm** sau alias → ghim phiên bản cụ thể và chạy lại eval khi nâng cấp | mục 07 |
| 17 | Responsible AI | Fairness, bias, minh bạch, tuân thủ, người giám sát | ⚠️ | Không nhắc **bảo mật**: prompt injection là LLM01 trong OWASP Top 10 for LLM 2025; agent có tool làm rủi ro này thành hành động thật | mục 12 §1 |
| 18 | Hệ RAG end-to-end | Ingest → Embed → Store → Retrieve → Generate | ⚠️ | Thiếu các bước tạo khác biệt: chunking có cấu trúc, **hybrid search** (BM25 + vector), **reranking**, viết lại query, lọc theo quyền, cache, eval từng khâu | mục 10 §2–3 (GraphRAG, LightRAG), mục 08 §2b (`RAG_Techniques`) |
| 19 | Thách thức mở rộng | Độ trễ, chi phí, lưu trữ, serving, độ bền | ✅ | Nêu đòn bẩy cụ thể: **prompt caching**, batching, chọn model theo tầng (router), streaming, giới hạn tốc độ | mục 10 §1, §6 (gateway/router) |
| 20 | Bài toán mở | Làm rõ, yêu cầu, giải pháp, trade-off, lặp | ✅ | Khung chung của system design; thêm "đo bằng gì" (eval) trước khi chọn kiến trúc | mục 08 §3 (Alex Xu) |

**Tổng:** 10 ✅, 10 ⚠️, 0 ❌. Không ô nào sai hẳn; điểm yếu là câu trả lời dừng ở định nghĩa, trong khi phỏng vấn thật hỏi tiếp "khi nào không dùng", "đo bằng gì", "hỏng thế nào".

### 2c.3 Chủ đề ảnh bỏ sót (thường gặp năm 2026)

- **Bảo mật LLM/agent:** prompt injection (trực tiếp và gián tiếp qua tài liệu RAG, output tool), quyền tối thiểu cho tool, sandbox → mục 12, mục 11.
- **Structured output** và validate schema → mục 17 §2b.
- **Kinh tế token:** prompt caching, chọn model theo tầng, ước chi phí một tác vụ → mục 10 §6.
- **Inference:** KV cache, quantization, batching liên tục (vLLM, SGLang) → mục 10 §1.
- **Giao thức agent:** MCP, A2A, Agent Skills → mục 04.
- **Coding agent và harness:** vòng lặp agent dài hạn, cổng kiểm bằng máy, git worktree → mục 01, 03, 21.

### 2c.4 Tài liệu ôn phỏng vấn tương tự

★ và lần push cuối đọc qua GitHub search ngày 12/10/2026; không repo nào archive.

| Tài liệu | ★ | License | Push cuối | Có câu trả lời thật? | Ghi chú |
|---|---|---|---|---|---|
| Chip Huyen, *AI Engineering* (O'Reilly, ebook 12/2024, bản in 1/2025) + `chiphuyen/aie-book` | 17,8k | không LICENSE | 7/2026 | Có (sách) | Nền tảng tốt nhất cho cả 20 ô; repo chỉ là tài liệu đi kèm (mục 08 §2b) |
| `KalyanKS-NLP/LLM-Interview-Questions-and-Answers-Hub` | 1,1k | Apache-2.0 | 2/2026 | **Có**, 115 câu trong `Interview_QA/` | Có quảng cáo sách trả phí |
| `amitshekhariitbhu/ai-engineering-interview-questions` | 3,4k | Apache-2.0 | 12/10/2026 | Chủ yếu danh sách câu hỏi, link ra blog/video | Phủ chủ đề mới nhất: MCP, LLMOps, eval, safety |
| `alexeygrigorev/data-science-interviews` | 10,2k | CC-BY-4.0 | 9/2026 | Có | ML/DS cổ điển, ít LLM |
| `chiphuyen/ml-interviews-book` | 4,8k | không LICENSE | 3/2025 | Phần lớn chỉ câu hỏi | Sách miễn phí 2021, trước thời LLM |
| `Devinterview-io/llms-interview-questions` | 1,1k | không LICENSE | 2/2026 | 15/63 câu trong README | Phần còn lại sau tường phí devinterview.io |
| `llmgenai/LLMInterviewQuestions` | 2,0k | không LICENSE | 2/2025 | **Không**, đáp án trong khoá trả phí | Tránh |

Gợi ý: sách *AI Engineering* cho nền tảng → KalyanKS để luyện câu trả lời viết sẵn → danh sách amitshekhar để rà chủ đề mới → các mục kho ở cột "Đọc sâu" để có ý trade-off/đo/hỏng.

### 2c.5 Dùng ảnh thế nào

Tốt làm **checklist chủ đề** trong một trang; không đủ làm câu trả lời. Khi ôn, với mỗi ô hãy chuẩn bị thêm ba ý: một trade-off (khi nào không dùng), một cách đo, một kiểu hỏng; cột "Đọc sâu trong kho" ở bảng §2c.2 chỉ chỗ có sẵn các ý đó.

## 2d. Repo "khoá học" là phễu quảng cáo: `cporter202/automate-for-growth` (ảnh người dùng gửi, 2026-10-12)

> Ảnh chụp README "🚀 Automate Content for Growth — The Complete Course for Scaling Your Social Media Presence" (11 module, nút Star 829, Buy me a coffee, avatar "Chris Porter"). Repo tìm được qua GitHub search, clone đầy đủ để đọc.

| Mục | Thông tin (12/10/2026) |
|---|---|
| Repo | `cporter202/automate-for-growth` · **~894★**, 228 fork; tạo 5/12/2025, **push cuối 9/12/2025**; 9 commit trong 4 ngày, 1 tác giả; **không có LICENSE**; homepage viralwavestudio.com |
| Nội dung thật | 16 file Markdown (~39k từ), **không có code**; 11 module (video Sora 2, "brand authority", đăng đa nền tảng, bulk content, blog, analytics, API, team, case study) |
| Mục đích | Hướng người đọc tới **ViralWave Studio**: 41 link tới viralwavestudio.com, 7 tới `api.viralwavestudio.com`; thư mục `ai-content-generation-tool/` tự gọi sản phẩm là "#1 AI Content Generation Tool" kèm mã giảm 15%; module API chỉ có ví dụ gọi API của chính sản phẩm đó |
| Liên hệ tác giả – sản phẩm | Repo không công bố quan hệ giữa tác giả (Facebook `chris.porter.7731`) và ViralWave Studio **(chưa xác minh là chủ sản phẩm hay affiliate)**; ảnh trong README lưu trên Firebase project `facesift` |
| Case study | Không tên, không nguồn: "0 → 4.000 follower trong 90 ngày", "engagement 6,8%", "US$25.000 doanh thu"; 3 link trong cả module. **Không kiểm chứng được** |

**Đánh giá:** không phải tài liệu học về tự động hoá nội dung mà là tài liệu bán hàng đặt trên GitHub; số sao không nói gì về chất lượng (repo bỏ dở từ 12/2025, ảnh của video quảng bá vẫn kêu gọi star). Không có LICENSE nên về mặt pháp lý không được phép tái sử dụng nội dung.

**Muốn tự động hoá nội dung mạng xã hội thật thì đọc:** n8n, Activepieces (mục 05, mục 21 §6) để dựng pipeline đăng bài; mục 19 và 22 cho sinh video/motion; mục 12 trước khi giao token tài khoản mạng xã hội cho bất kỳ dịch vụ bên thứ ba nào.

**Dấu hiệu nhận ra "khoá học" kiểu này:** đa số link trỏ về một sản phẩm, không có code chạy được, không LICENSE, case study không tên, commit dồn trong vài ngày rồi dừng, README đặt lời kêu gọi star và donate trước mục lục.

### 2d.1 Repo thứ hai cùng tác giả: `cporter202/make-com-automation-recipes` (ảnh người dùng gửi, 2026-10-13)

> Ảnh chụp README "Make.com Automation Recipes — 600+ pre-built workflows & templates" (badge Templates 600+, Categories 12, License MIT; khung "Affiliate disclosure"). Đã clone đầy đủ để đọc.

| Mục | Thông tin (13/10/2026) |
|---|---|
| Repo | `cporter202/make-com-automation-recipes` · **16★, 0 fork** (shields.io); 4 commit: "Initial commit" 8/12/2025, rồi **3 commit cách nhau 7 giây** ngày 12/10/2026 (dựng danh mục 600 template, banner AI, thêm MIT) |
| Nội dung thật | Chỉ 3 file: `README.md` (779 dòng), `LICENSE` (MIT), `assets/hero.png`. **Không có template nào trong repo**: 600 dòng là link tới **thư viện template công khai của chính Make.com** (600 ID khác nhau, thử ngẫu nhiên đều trả 200), chia đều **đúng 50 mục × 12 nhóm** |
| Dấu hiệu sinh tự động | Tên mỗi mục là slug URL đổi sang Title Case ("…With Openai **S** Whisper…"), không có mô tả, không ghi ai làm template, không ghi template dùng bao nhiêu operation |
| Mục đích | **Mọi** link Make.com (603/603) mang mã đối tác `?pc=viralwave` — cùng ViralWave mà repo `automate-for-growth` (§2d) quảng bá. Khác repo trước: lần này **có ghi rõ affiliate** ngay đầu README |
| License | MIT chỉ áp cho README do tác giả viết; bản thân các template thuộc Make.com và người đóng góp gallery, không phải "MIT" |

**Đánh giá:** không phải bộ sưu tập do tác giả xây mà là trang mục lục có link giới thiệu (affiliate) dẫn vào gallery mà Make đã có sẵn và có tìm kiếm, lọc theo app. Không có giá trị thêm ngoài cách chia nhóm. Có công khai affiliate nên trung thực hơn §2d, nhưng badge "600+ templates" dễ hiểu nhầm là template nằm trong repo.

**Muốn mẫu tự động hoá thật:** dùng thẳng gallery chính thức `make.com/en/templates` (không qua link affiliate); nếu cần tự host và đọc được mã thì xem n8n (mục 05, mục 21 §6) và thư viện workflow công khai của n8n (`n8n.io/workflows`). Trước khi bật một template, kiểm quyền OAuth nó xin và số operation mỗi lần chạy, vì gói miễn phí của Make tính theo operation.

**Quy tắc rút ra (bổ sung §2d):** repo "N trăm template/prompt" mà chỉ có một README → đếm link theo tên miền và tham số (`?pc=`, `?ref=`, `utm_`), xem các commit có dồn trong vài giây không. Hai dấu hiệu này đủ để nhận ra danh mục sinh tự động phục vụ affiliate.

### 2d.2 Repo thứ ba cùng tác giả: `cporter202/ai-growth-stack` (ảnh người dùng gửi, 2026-10-16)

> Ảnh chụp README: tiêu đề "API Growth Stack", bốn huy hiệu (APIS 6 · CATEGORIES 6 · STATUS ACTIVE · UPDATED REGULARLY), banner "AI Growth Stack · github.com/cporter202/ai-growth-stack", câu "A curated collection of powerful AI-powered APIs for website optimization, SEO, conversions, and social media growth… not fluff", nút "Buy me a coffee" và avatar "Chris Porter". Đã clone đầy đủ để đọc.

| Mục | Thông tin (16/10/2026) |
|---|---|
| Repo | `cporter202/ai-growth-stack` · **229★, 70 fork** (shields.io); **7 commit trong 15 phút ngày 21/12/2025**, không có commit nào sau đó; commit cuối (`5ccfb8f`) còn dính nguyên câu nhắc mặc định của git trong tiêu đề ("# Please enter the commit message…") |
| Nội dung thật | **Chỉ một file `README.md`** (302 dòng). Không có code, không có ví dụ, **không có LICENSE**, dù mục "License" của README nói repo là "documentation and examples" |
| 6 "API" | Website Data Extraction · AI SEO Analysis · AI Conversion Optimization · AI Website Copywriter · AI Landing Page Optimizer · AI Social Media Content Generator. **Cả 13 link "View on RapidAPI" đều trỏ về cùng một trang hồ sơ người dùng** (`rapidapi.com/user/contact-_OGid12Eu`), không link nào trỏ tới trang của một API cụ thể. Trang này cần JavaScript nên không đọc được danh sách API thật |
| Ai bán | `apidataframe.com` ("API DataFrame", "Professional APIs for Developers") bán **đúng 6 API này** cộng 3 API trích email/số điện thoại/link mạng xã hội, chỉ qua RapidAPI, không công bố giá hay tên người vận hành. Mục License của README dẫn điều khoản "RapidAPI and API DataFrame". Quan hệ giữa tác giả và API DataFrame **không được công bố** (chưa xác minh là chủ hay affiliate) |
| Liên hệ với §2d | Nút cà phê dẫn tới `buymeacoffee.com/viralwavestudio`; bio GitHub của tác giả quảng bá ViralWaveStudio.com. Banner là ảnh sinh bằng AI (tên file "Generated Image December 21, 2025"), lưu trên cùng Firebase project `facesift` như §2d |

**Kiểm từng ô trong ảnh:**

| Ô | Kiểm | Ghi chú |
|---|---|---|
| Tiêu đề "API Growth Stack" | ⚠️ | Banner và tên repo là "**AI** Growth Stack"; hai tên lệch nhau ngay trên cùng một màn hình |
| APIS 6 · CATEGORIES 6 | ✅ | Đúng 6 mục, mỗi mục một "category", nhưng không mục nào có link riêng |
| STATUS ACTIVE | ❌ | Huy hiệu tĩnh (`img.shields.io/badge/STATUS-ACTIVE`), không đo gì; repo không đổi từ 21/12/2025 |
| UPDATED REGULARLY | ❌ | Huy hiệu tĩnh; commit cuối cách ngày đọc gần 10 tháng. Dòng cuối README ghi "Last updated: December 2024", **trước cả ngày tạo repo** |
| "A curated collection… not fluff" | ⚠️ | Không phải tuyển chọn từ nhiều nhà cung cấp: cả 6 là danh mục sản phẩm của một bên bán (API DataFrame) mà README không nói rõ. Phần "Key Features", "Why It's Powerful" là văn quảng cáo chung chung, không có endpoint, giá, giới hạn hay ví dụ gọi |
| Buy me a coffee | ✅ | Link thật, tới tài khoản `viralwavestudio` |

**Tổng:** 2✅ / 2⚠️ / 2❌.

**Đánh giá:** đây là trang quảng cáo cho các API trả phí trên RapidAPI, không phải bộ sưu tập hay tài liệu kỹ thuật. 229★ cho một README không code, không đổi trong 10 tháng, cho thấy số sao của nhóm repo này không phản ánh nội dung (cùng mô hình §2d: 894★, bỏ dở từ 12/2025). Không có LICENSE nên không được phép tái sử dụng nội dung.

**Muốn làm đúng việc này:** trích dữ liệu web và kiểm SEO thì có công cụ mã mở tự chạy được: Crawl4AI, Firecrawl (mục 11), Lighthouse CI cho hiệu năng/SEO kỹ thuật (mục 13). Nếu vẫn cần API trả phí, tìm thẳng trên marketplace, đọc giới hạn và giá của **từng API cụ thể**, và chạy thử gói miễn phí trước. Viết nội dung marketing bằng LLM thì gọi thẳng model, không cần lớp API trung gian không rõ model bên dưới.

**Quy tắc rút ra (bổ sung §2d, §2d.1):** huy hiệu "STATUS ACTIVE / UPDATED REGULARLY" mà URL là `img.shields.io/badge/...` là huy hiệu tĩnh tự gõ, không phải số đo; so với ngày commit cuối. Khi N mục "khác nhau" cùng trỏ về một link, đó là một sản phẩm được trình bày như một danh sách.

### 2d.3 Repo thứ tư & năm cùng tác giả: `marketing-apis-that-drive-roi` + `social-growth-apis-for-creators` (ảnh "4 GitHub repos worth bookmarking", 2026-10-18)

> Ảnh slide của Chris Porter giới thiệu 4 repo; hai repo đầu là của chính `cporter202`. Đã clone cả hai để đọc. Cùng khuôn mẫu §2d–§2d.2, lần này là **danh mục API gắn link affiliate Apify**.

| Mục | Thông tin (18/10/2026) |
|---|---|
| Repo | `cporter202/marketing-apis-that-drive-roi` (slide: 27★/8 fork) · `cporter202/social-growth-apis-for-creators` (slide: 49★/14 fork); cả hai push 17/10/2026, **không có LICENSE** |
| Nội dung thật | Chỉ README + vài thư mục, mỗi thư mục một README là **bảng link tới actor trên Apify store**. marketing: **290 API** (đúng badge) chia 5 nhóm; social: 6 nhóm. Không có code, không có ví dụ gọi, không có đánh giá chất lượng/giá từng actor |
| Mục đích (affiliate) | **3.089 link** mang mã giới thiệu Apify `?fpr=p2hrc6` trên cả hai repo. README mở đầu bằng lời mời vào **cộng đồng Skool trả phí** ("Vibe Coding with Chris") + link Facebook cá nhân; `META.json` có `source_path` ("marketing-apis-290") cho thấy sinh từ khuôn chung |
| Khác §2d.1 | Lần này **không có khung "Affiliate disclosure"** rõ như `make-com-automation-recipes`; người đọc không được báo mọi link đều gắn mã giới thiệu |

**Đánh giá:** không phải "awesome list" trung lập mà là **danh mục affiliate dẫn về Apify store**, bọc trong phễu cộng đồng trả phí — đúng mô hình §2d/§2d.2. "290 API" chỉ là các actor bất kỳ trên Apify, không tuyển chọn hay kiểm chất lượng; badge sao không phản ánh nội dung (nhóm repo này quảng bá chéo để gom sao).

**Muốn dùng scraper/API thật:** tìm thẳng trên **apify.com/store** (không qua link `?fpr=`), đọc giá + giới hạn + đánh giá của **từng actor cụ thể**, chạy thử free tier; scraper mã mở tự host thì có Crawl4AI, Firecrawl (mục 11). Cho API mạng xã hội, cân nhắc điều khoản nền tảng và mục 12 trước khi giao token.

**Quy tắc (bổ sung §2d–§2d.2):** repo "N trăm API" mà mỗi link đều cùng một tham số giới thiệu (`?fpr=`, `?pc=`, `?ref=`) là danh mục affiliate; đếm `grep -rho 'fpr=[a-z0-9]*'` để thấy quy mô. Cùng một tác giả/cùng avatar + "Buy me a coffee"/Skool lặp lại qua nhiều repo là dấu hiệu phễu, không phải tuyển chọn.

## 2e. Kiểm ảnh "Layers of AI: From classical methods to autonomous AI systems" (ảnh người dùng gửi, 2026-10-13)

> Infographic 6 tầng xếp chồng, mũi tên đi lên, mỗi tầng 5 ô: Classical AI → Machine Learning → Neural Networks → Deep Learning → Generative AI → Agentic AI. Ghi nguồn **AIForLeaders.com**.

### 2e.1 Hồ sơ nguồn

| Mục | Thông tin (13/10/2026) |
|---|---|
| Nguồn | aiforleaders.com: newsletter AI hằng ngày cho lãnh đạo doanh nghiệp, do **Adam Danyal** sáng lập, đồng viết với Julia Danyal (theo FAQ của trang). Trang tự nhận "50K+ leaders" đăng ký và "1.6M+ on LinkedIn"; có link "Get AI Certified" sang chiefaileader.com (không ghi giá). Số liệu là tự công bố **(chưa xác minh)** |
| Kiểu nội dung | Infographic phổ thông cho người không chuyên; bản "Layers of AI"/"7 Layers of AI" được nhiều tài khoản LinkedIn đăng lại, có bản kèm link đăng ký aiforleaders.com. Không tìm thấy bài gốc đã đánh chỉ mục |
| Cách làm ảnh | Hai ô "Audio & Image Models" và "Multimodal Models" dùng **cùng một biểu tượng**, ô giữa tầng Classical AI chỉ ghi "AI" dưới biểu tượng kính lúp → nhiều khả năng ảnh do công cụ sinh ảnh dựng và không được soát lại **(chưa xác minh)** |

### 2e.2 Từng tầng: đúng tới đâu

Ký hiệu: ✅ đúng · ⚠️ đúng nhưng gây hiểu sai hoặc thiếu ý · ❌ sai.

| Tầng | Ảnh ghi | Đánh giá | Chỗ cần sửa / bổ sung | Đọc sâu |
|---|---|---|---|---|
| Classical AI | Symbolic AI, Expert Systems, "AI" (kính lúp), Knowledge Representation, Logic & Reasoning | ⚠️ | Ô "AI" gần như chắc là **Search** (tìm kiếm trạng thái: A\*, minimax) bị ghi sai nhãn. Thiếu **planning cổ điển** (STRIPS 1971) — chính là gốc của ô "Planning" ở tầng trên cùng | AIMA (Russell & Norvig) |
| Machine Learning | Supervised, Unsupervised, Classification, Reinforcement Learning, Regression | ⚠️ | Trộn hai trục: **kiểu học** (supervised, unsupervised, RL) và **bài toán** (classification, regression — đều là bài toán supervised). Thiếu đánh giá mô hình (train/test, overfitting) và các thuật toán không phải mạng nơ-ron (cây quyết định, SVM) | mục 08 §2b (`mlabonne/llm-course`) |
| Neural Networks | Perceptrons, Cost Functions, Backpropagation, Activation Functions, Hidden Layers | ✅ | Hàm mất mát không riêng của mạng nơ-ron (hồi quy logistic cũng có); thiếu gradient descent/optimizer — động cơ thật của backprop | `labmlai/annotated_deep_learning_paper_implementations` (§2b) |
| Deep Learning | Transformers, LSTMs, RNNs, CNNs, Autoencoders | ✅ | LSTM là một loại RNN (hai ô chồng nhau). Có thể thêm attention, huấn luyện quy mô lớn trên GPU | `rasbt/LLMs-from-scratch`, `karpathy/nanochat` (§2b) |
| Generative AI | LLMs, Diffusion Models, Audio & Image Models, Multimodal Models, VAEs | ⚠️ | Hai ô trùng biểu tượng và chồng nghĩa (audio/image ⊂ multimodal). Thiếu **GAN** (họ mô hình sinh ảnh lớn trước diffusion). Thiếu **post-training** (SFT, RLHF/DPO) — chỗ tầng ML (RL) quay lại ở tầng trên | mục 14, 19, 22 (multimodal, video, motion) |
| Agentic AI | Memory, Planning, Agents, Tool Use, Autonomous Execution | ⚠️ | Ô "Agents" nằm trong tầng "Agentic AI" là lặp lại tên. Thiếu thứ phân biệt hệ agent chạy được với demo: **vòng lặp + điều kiện dừng**, guardrail/người duyệt, eval, giao thức (MCP, A2A) | mục 03 (§8c ảnh "How AI Agents Work"), 02, 04, 21 |

**Tổng:** 2 ✅, 4 ⚠️, 0 ❌. Các ô đều là khái niệm có thật; sai ở **cấu trúc** hơn là ở từng ô.

### 2e.3 Sai ở cấu trúc "xếp tầng"

1. **Bốn tầng dưới lồng nhau, hai tầng trên thì không.** Neural Networks ⊂ ML, Deep Learning ⊂ Neural Networks là quan hệ tập con thật (cách vẽ vòng tròn lồng nhau AI ⊃ ML ⊃ DL phổ biến trong giáo trình). Generative AI chỉ **phần lớn** nằm trong deep learning (mô hình sinh cũng có n-gram, HMM, GMM). Agentic AI không phải loại mô hình mà là **kiến trúc hệ thống**: model + harness chạy vòng lặp, dùng tool (mục 03 §1, §8c); nó có thể dùng model không sinh văn bản và cả thành phần cổ điển (planner, rule).
2. **Mũi tên đi lên ngụ ý trình tự lịch sử, nhưng lịch sử không thẳng.** Perceptron (Rosenblatt, 1958) ra đời gần như cùng lúc với thuật ngữ "machine learning" (Samuel, 1959); "agent" và "planning" là khái niệm trung tâm của AI cổ điển (giáo trình AIMA định nghĩa AI là nghiên cứu "intelligent agents" từ 1995). Tầng "Agentic AI" năm 2024–2026 là cách cũ chạy trên model mới, không phải tầng mới xây trên Generative AI.
3. **Tầng dưới không bị thay thế.** Hệ luật/expert system vẫn chạy nhiều phần mềm ra quyết định; trong agent hiện đại, phần "luật cứng" (quyền, ngân sách, cổng kiểm) chính là lớp cổ điển bọc quanh LLM.

### 2e.4 Tài liệu tốt hơn cho cùng mục đích

| Tài liệu | Quy mô / license | Vì sao |
|---|---|---|
| Russell & Norvig, *Artificial Intelligence: A Modern Approach* (AIMA, bản 4, 2020) + `aimacode/aima-python` | repo ~8,8k★ (13/10/2026, shields.io), MIT, commit gần nhất 6/2026 | Phủ đủ 6 tầng với quan hệ đúng (search, logic, planning, học máy, deep learning, agent); code Python cho từng thuật toán |
| `microsoft/generative-ai-for-beginners` → `microsoft/ai-agents-for-beginners` | đã có ở §2b, có bản tiếng Việt | Hai tầng trên cùng, có bài thực hành |
| `rasbt/LLMs-from-scratch`, `karpathy/nanochat` | đã có ở §2b | Hiểu Deep Learning → Generative AI từ bên trong |

**Dùng ảnh thế nào:** được làm "bản đồ thuật ngữ" một trang cho người không chuyên. Khi giải thích lại, nói rõ hai tầng trên không phải tập con của tầng dưới, và đừng đọc mũi tên như dòng thời gian. Với người làm sản phẩm, ảnh "How AI Agents Work" (mục 03 §8c) hữu ích hơn vì nói agent chạy thế nào chứ không chỉ liệt kê tên.

## 2f. Kiểm ảnh "How to become an AI engineer in 2026" (Brij Kishore Pandey, ảnh người dùng gửi, 2026-10-13)

> Trang **09 / 17** trong cùng carousel với hai trang đã kiểm ở mục 10 §3b ("10 / 17" RAG, "12 / 17" $0 stack), ký tên **Brij Kishore Pandey (@brijpandeyji)**. Ảnh chia 13 ô kỹ năng quanh dòng "AI Engineer 2026 — 13 areas. Ship systems, measure them, repeat." và khẩu hiệu cuối "Skip the math degree. Ship the system. Repeat." Logo nhận ra chắc chắn: OpenAI, Anthropic, Gemini, Meta, LlamaIndex, PostgreSQL, NVIDIA, Python, Docker, Git, vLLM, Hugging Face, Mistral, GitHub, X. Các logo còn lại (ô 04, 05, 07, 08, 10, 11) **(chưa xác minh)** là sản phẩm nào.

### 2f.1 Từng ô

| # | Ô | Nội dung trong ảnh | Đánh giá | Ghi chú |
|---|---|---|---|---|
| 01 | LLM fundamentals | Transformer, token; context window; sampling, reasoning model | ✅ | Đủ cho người dùng API. Đọc kèm: rasbt/LLMs-from-scratch (§2b) |
| 02 | Prompt + context engineering | System prompt, few-shot; structured output; ghép context | ✅ | "Context assembly" đúng trọng tâm 2026 hơn "prompt engineering" thuần |
| 03 | RAG systems | Embedding, chunking; hybrid search, rerank; GraphRAG | ✅ | Ô này có đủ hybrid search và rerank — đúng phần mà trang 10/17 bỏ sót |
| 04 | Agentic systems | Tool use, MCP; memory, planning; multi-agent | ✅ | Thiếu ý "khi nào **không** nên dùng agent": workflow cố định thường rẻ và dễ kiểm hơn (mục 03) |
| 05 | AI gateways + routing | Route model, fallback; theo dõi chi phí; rate limit | ✅ | Ví dụ mã mở: LiteLLM (~61k★), mục 10 |
| 06 | Guardrails + safety | Phòng prompt injection; che PII; kiểm output | ⚠️ | Chữ "defense" dễ hiểu nhầm là chặn được. OWASP LLM01 ghi rõ chưa có cách phòng chống chắc chắn; cách làm thật là **giới hạn thiệt hại**: quyền tối thiểu cho tool, tách nội dung ngoài, người duyệt hành động rủi ro, test đối kháng (mục 12) |
| 07 | Observability + evals | Tracing, LLM-as-judge; golden set; phát hiện drift | ✅ | LLM-as-judge phải hiệu chỉnh với nhãn người chấm trước khi tin (mục 07) |
| 08 | Production AI engineering | Streaming, caching; async, rate limit; latency budget | ✅ | "Rate limits" lặp lại ô 05 |
| 09 | Software engineering | Python async, FastAPI; Git, Docker, Postgres; test, CI/CD | ⚠️ | Đúng nhưng chỉ Python. Một phần lớn sản phẩm AI 2026 viết bằng TypeScript (Vercel AI SDK, Mastra, Next.js); nên biết ít nhất đọc được |
| 10 | Inference + deployment | vLLM, quantization; serverless GPU; autoscaling | ✅ | Chỉ cần khi tự host model; đa số đội dùng API trước |
| 11 | Multimodal | Vision, tài liệu; giọng nói, ảnh, video; OCR | ✅ | Xem mục 14 |
| 12 | Ecosystem fluency | Model mở; paper, benchmark; Hugging Face | ✅ | Benchmark công khai hay bị nhiễm dữ liệu huấn luyện; tự đo trên golden set của mình (ô 07) đáng tin hơn |
| 13 | Career compounding | Ship công khai; open source; viết và dạy | ✅ | |
| — | "Skip the math degree" | Khẩu hiệu cuối | ⚠️ | Không cần bằng toán, nhưng **xác suất thống kê cơ bản** là bắt buộc để làm eval đúng: cỡ mẫu, khoảng tin cậy, so A/B, đọc phương sai giữa các lần chạy LLM |

**Tổng:** 11 ✅, 3 ⚠️, không ô nào sai. Đây là trang tốt nhất trong ba trang của carousel đã kiểm.

### 2f.2 Ảnh bỏ sót

- **Fine-tuning và dataset engineering.** Không có ô nào nhắc. Sách *AI Engineering* (Chip Huyen, O'Reilly 2025) dành chương 7 cho "khi nào nên và không nên fine-tune" và một chương riêng cho dataset engineering. Kỹ năng quyết định "RAG hay fine-tune hay chỉ sửa prompt" là phần phân biệt AI engineer với người chỉ gọi API.
- **Bảo mật chuỗi cung ứng của agent:** MCP server, skill, plugin cài từ nguồn ngoài; bí mật trong cấu hình agent (mục 12 §3e). Ô 06 chỉ nói về input/output của model.
- **Thiết kế sản phẩm và UX cho AI:** hiển thị độ không chắc chắn, cho người dùng sửa và phản hồi, thu feedback làm dữ liệu eval (chương cuối của sách Chip Huyen).
- **Dùng coding agent hằng ngày** (Claude Code, Codex, Cursor) — kỹ năng thực tế nhất của AI engineer 2026 nhưng ảnh không nhắc (mục 01).
- **Pháp lý và quyền riêng tư** khi xử lý dữ liệu người dùng: GDPR, EU AI Act; ở Việt Nam là Nghị định 13/2023 về dữ liệu cá nhân.

### 2f.3 Tài liệu tương tự để đối chiếu (★ qua shields.io, 13/10/2026)

| Nguồn | ★ / dạng | Khác ảnh |
|---|---|---|
| chiphuyen/aie-book (sách *AI Engineering*) | ~18k, repo tài nguyên đi kèm sách | Có fine-tuning, dataset engineering, user feedback; nặng về eval |
| roadmap.sh/ai-engineer (kamranahmedse/developer-roadmap, ~369k) | Roadmap tương tác | Định nghĩa AI engineer là người **dùng** model có sẵn, khác ML engineer/researcher; có mục câu hỏi "có cần bằng cấp không" |
| patchy631/ai-engineering-hub | ~38k, MIT | Tập ví dụ code RAG/agent chạy được, bổ sung phần thực hành mà ảnh không có |
| microsoft/generative-ai-for-beginners (§2b) | ~121k | Khoá có bài tập, có bản tiếng Việt |

### 2f.4 Dùng ảnh thế nào

Dùng được làm **danh sách tự kiểm** 13 mảng. Trước khi dùng làm lộ trình học: thêm ô fine-tuning/dataset, sửa ô 06 thành "giới hạn thiệt hại prompt injection", và học thống kê cơ bản trước ô 07. Thứ tự học hợp lý: 01 → 02 → 09 → 03 → 07 → 04 → 06 → 05/08 → 10/11; ô 12–13 làm song song suốt.

## 2g. Kiểm ảnh "The Roadmap to Mastering Agentic AI Systems in 2026" (Vinod Chugani, KDnuggets, ảnh người dùng gửi, 2026-10-16)

> Ảnh chụp đầu bài trên **KDnuggets** (Vinod Chugani, 13/10/2026, mục Artificial Intelligence) kèm infographic "The Roadmap to Building Agentic AI Systems in 2026 — from single agents to production-ready, real-world impact", chia 4 cấp: (1) Single Agent Reasoning Loops, (2) Stateful Memory and Graph-Based Flows, (3) Multi-Agent Collaboration, (4) Operational Hardening; đáy là vòng "continuous feedback and evolution". Đã đọc toàn bài. Infographic không ghi tác giả hay công cụ vẽ, và tiêu đề trong ảnh ("Building") khác tiêu đề bài ("Mastering").

### 2g.1 Từng cấp: ảnh và bài viết

| Cấp | Ảnh vẽ | Bài viết nói thêm | Đánh giá | Chỗ cần sửa / bổ sung |
|---|---|---|---|---|
| 1. Single agent loop | Input → Reasoning (plan) → Tool call → Result → Reflection; "plan → act → observe → refine" | ReAct, Plan-and-Solve, Reflection, Tree of Thoughts; function calling; kiểm output bằng Pydantic/TypeChat; ghép context động | ⚠️ | Vòng trong ảnh **không có lối ra**: thiếu điều kiện dừng do máy kiểm và trần số vòng, đúng chỗ agent thật hay hỏng (mục 03, mục 21 §8). Kiểm output có cấu trúc là ý tốt của bài nhưng không có trong ảnh |
| 2. Stateful memory + graph | Long-term memory, state, knowledge sources quanh "graph orchestrator"; conditional flow, tool node, sub-task | Working / episodic (vector) / semantic (knowledge graph) memory; chain vs graph; **checkpoint** để rollback, resume, debug; LangGraph, AutoGen | ⚠️ | Checkpoint và điểm dừng chờ người (human-in-the-loop) là lý do chính để dùng graph, nhưng ảnh không vẽ. Bài vẫn gợi ý **AutoGen**, trong khi README của AutoGen ghi "now in maintenance mode… New users should start with Microsoft Agent Framework" (mục 02) |
| 3. Multi-agent | Coordinator + research/analysis/execution agent, shared context, handoff, synthesize | Hierarchical, debate-and-critique, peer-to-peer; message schema có cấu trúc; giải xung đột bằng vote/hỏi lại/chuyển người; AutoGen, CrewAI, **MCP** | ⚠️ | Không nói cái giá: Anthropic đo hệ multi-agent dùng **khoảng 15× token** so với chat, và không hợp với việc mà các agent phải dùng chung context hoặc phụ thuộc nhau nhiều (phần lớn việc code). Bài gọi MCP là chuẩn cho giao tiếp nhưng MCP là giao thức agent ↔ tool/context; giao thức agent ↔ agent là **A2A**, bài không nhắc (mục 04 §3) |
| 4. Operational hardening | Observability, monitoring, guardrails, evaluation, logging & auditing, reliable infra, CI/CD | Circuit breaker, trần độ sâu đệ quy, trần token; **sandbox** chạy code (Docker, e2b, WebAssembly); LangSmith, Arize Phoenix; đánh giá theo **trajectory** | ⚠️ | Phần này của bài tốt hơn ảnh: ảnh bỏ mất sandbox và trần chi phí. Cả hai đều **không nhắc prompt injection**, rủi ro số 1 khi agent đọc dữ liệu ngoài rồi gọi tool (OWASP LLM01, mục 12), cũng không có cổng người duyệt cho hành động không đảo ngược |

**Tổng:** 0✅ / 4⚠️ / 0❌. Không có ô sai; mỗi cấp đều thiếu đúng phần làm agent an toàn và rẻ.

### 2g.2 Sai ở cấu trúc "4 cấp nối tiếp"

1. **Thiếu cấp 0: có cần agent không.** Anthropic (*Building Effective Agents*) khuyên bắt đầu bằng workflow cố định (prompt chaining, routing, parallelization) và chỉ dùng agent khi không đoán trước được các bước. Lộ trình bắt đầu thẳng từ agent loop dễ khiến người học dùng agent cho việc mà một workflow làm rẻ và dễ kiểm hơn (mục 03 §1).
2. **Multi-agent không phải "cấp trên" của single agent.** Nó là một lựa chọn có giá (15× token, khó gỡ lỗi), hợp với việc song song hoá được như nghiên cứu, không hợp với phần lớn việc code. Mũi tên 3 → 4 ngụ ý ai cũng phải đi qua multi-agent mới tới production.
3. **"Hardening" không đợi tới cấp 4.** Eval, trace, trần chi phí và sandbox cần có từ agent đầu tiên; để cuối cùng là cách tạo ra demo không lên được production (mục 07, mục 21 §8: "mọi loop phải có 4 số").

### 2g.3 Đọc gì thay / đọc kèm

| Tài liệu | Vì sao |
|---|---|
| Anthropic, *Building Effective Agents* (12/2024) và *How we built our multi-agent research system* (13/6/2025) | Cấp 0 (workflow trước agent) và số liệu thật về chi phí, giới hạn của multi-agent |
| `microsoft/ai-agents-for-beginners`, `huggingface/agents-course` (§2b) | Thực hành đủ 4 cấp, có bài chấm điểm; bản tiếng Việt cho bộ của Microsoft |
| Mục 21 §2 (hai bài harness của Anthropic) và §10c (AI-native SDLC) | Cấp 4 làm thật: harness, cổng máy, giới hạn vòng, người duyệt ở cổng |
| Microsoft Agent Framework thay cho AutoGen; LangGraph cho graph + checkpoint (mục 02) | Danh sách framework của bài có một mục đã ngừng phát triển |

**Dùng ảnh thế nào:** được làm sơ đồ tổng quan một trang về các khái niệm. Khi dạy lại, thêm cấp 0 ("workflow trước, agent sau"), chuyển eval/trace/trần chi phí/sandbox lên từ cấp 1, coi multi-agent là lựa chọn có giá chứ không phải bậc tiếp theo, và thay AutoGen bằng Microsoft Agent Framework.

## 2h. Kiểm ảnh "SEO không thiếu việc, nhưng AI đang thay đổi cuộc chơi" (danhnolan.com, ảnh người dùng gửi, 2026-10-25)

> Infographic tiếng Việt của **Danh Nolan** (danhnolan.com, người đào tạo SEO/GEO/AI Search ở TP.HCM). Ảnh là bảng 5 cấp (SEO Junior → Executive → Specialist → Lead → Manager/Head) × 7 mảng việc (Onpage, Technical, Content, Entity, GEO/AI Search, Offpage), mỗi ô tô màu theo mức AI tự động hóa được (đỏ: tự động hóa phần lớn; cam: AI hỗ trợ đáng kể, cần người duyệt; xám: cần phán đoán/chịu trách nhiệm). Kết luận của ảnh: "AI thay tác vụ, không tự động thay cả vai trò". Trang chủ danhnolan.com không có bài viết đi kèm ảnh (đọc 25/10/2026). Mục này đối chiếu ảnh với tài liệu chính thức của Google, nghiên cứu độc lập, và các skill SEO cho agent đang có trên GitHub.

### 2h.1 Ảnh đúng ở đâu

- **Khung "tác vụ, không phải vai trò"** khớp cách các nghiên cứu về mức tiếp xúc AI chia công việc thành tác vụ. Ảnh cũng tự ghi rõ "không phải dự báo mất việc".
- **Các ô đỏ ở cấp Junior/Executive là việc agent làm được ngay hôm nay**, có skill mã mở cho từng việc. Ví dụ `AgriciDaniel/claude-seo` (~20k★, MIT, đọc mã 25/10/2026) có:
  - 26 skill cho audit kỹ thuật, schema, sitemap, hreflang, nội dung, GEO và backlink;
  - script gọi Search Console, GA4, CrUX;
  - không telemetry; API trả phí (DataForSEO, Ahrefs, Firecrawl) là extension tùy chọn.
- **Cột "giá trị con người" khớp yêu cầu của Google**: Google cho phép dùng AI tạo nội dung, nhưng yêu cầu "manually factcheck and review all AI-generated content… before publishing", kể cả title, meta description và alt text (*Using generative AI content*, cập nhật 1/10/2026). Đó chính là bước "biên tập và kiểm chứng" ở ô cam.

### 2h.2 Ảnh thiếu hoặc nói quá

| Ô trong ảnh | Đối chiếu | Kiểm |
|---|---|---|
| **GEO / AI Search** là một mảng riêng, có "chiến lược AI Search" | Google: "There are no additional requirements to appear in AI Overviews or AI Mode, nor other special optimizations necessary"; không cần schema riêng; lưu lượng từ AI features được gộp vào báo cáo Performance, loại "Web" của Search Console (*AI features and your website*, cập nhật 10/12/2025). Với Google, "GEO" phần lớn vẫn là SEO nền tảng. Nghiên cứu *GEO: Generative Engine Optimization* (Aggarwal và cộng sự, KDD 2024) báo cáo tăng hiển thị "tới 40%" trên benchmark GEO-bench của chính nhóm, chứ không đo trên AI Overviews | ⚠️ |
| Junior "Nhập answer-first theo mẫu" được tô đỏ | Sản xuất hàng loạt theo mẫu là đúng kiểu **scaled content abuse**: "Using generative AI tools or other similar tools to generate many pages without adding value for users" (*Spam policies*, cập nhật 28/8/2026). Spam policy cũng bao gồm "attempting to manipulate generative AI responses in Google Search". Ảnh không nhắc ranh giới này | ⚠️ |
| Offpage: "Tìm danh sách nguồn", "Soạn thư outreach" tô đỏ | Tự động hóa được, nhưng gửi thư outreach hàng loạt do AI viết dễ thành spam, và mua hoặc đổi link vi phạm chính sách link spam. Phần cần người làm là quan hệ thật, như ở cột Lead | ⚠️ |
| Technical: Junior/Executive "Rà lỗi, sửa lỗi phổ biến" tô đỏ | Rà lỗi thì agent làm tốt. "Sửa" cần quyền deploy, test và rollback trên site thật, không chỉ cần AI | ⚠️ |
| Không có hàng **đo lường** | Thiếu một thay đổi lớn: Pew Research (dữ liệu 2025, 900 người dùng Mỹ, 68.879 lượt tìm) thấy người dùng nhấp kết quả thường ở **8%** lượt khi có AI summary, so với **15%** khi không có; chỉ ~1% nhấp link nguồn trong summary. Search Console không tách riêng traffic AI Overviews. Vì vậy mọi cấp cần đo lại KPI (hiển thị, chuyển đổi, không chỉ click) | ❌ thiếu |
| Không có hàng **kiểm soát crawler và snippet** | Một quyết định "AI Search" thật nằm ở `robots.txt`, `nosnippet`, `max-snippet`, `noindex` (Google ghi đây là cách giới hạn nội dung hiển thị trong Search), và việc chặn hay mở cho bot AI khác (Cloudflare, GPTBot…). Ảnh bỏ hẳn | ❌ thiếu |
| Mức "Rất cao → Rất thấp" ở hàng "Mức độ tác vụ tiếp xúc AI" | Không kèm nguồn hay số đo. Ảnh ghi "đánh giá dựa trên thực tế ứng dụng AI hiện nay", tức là nhận định của tác giả **(chưa xác minh)** | ⚠️ |

### 2h.3 Công cụ SEO/GEO cho agent (shields 25/10/2026)

| Repo | ★ · license | Commit cuối | Ghi chú |
|---|---|---|---|
| `coreyhaines31/marketingskills` | ~56k · MIT | 10/2026 | Bộ skill marketing tổng quát, có SEO audit (mục 20 §3f) |
| `AgriciDaniel/claude-seo` | ~20k · MIT | 22/10/2026 | 26 skill + 19 agent + script Python. Có **cổng chặn nội dung mỏng** trong `seo-programmatic`: dừng cứng khi vượt 500 trang mà không có lý do, gắn cờ khi nội dung riêng mỗi trang < 40%. Script Indexing API tự ghi rõ chỉ dùng cho JobPosting/BroadcastEvent. `content_humanize.py` chỉ thay cụm từ khuôn mẫu và xóa ký tự Unicode ẩn, tự nói không gỡ được watermark thống kê. Cài qua `git clone` + `install.sh` (README khuyên đọc trước khi chạy) |
| `zubair-trabzada/geo-seo-claude` | ~11k · MIT | 10/2026 | Skill GEO cho Claude Code **(chưa đọc mã)** |
| `TheCraigHewitt/seomachine` | ~7,5k · MIT | 10/2026 | Workspace viết nội dung SEO **(chưa đọc mã)** |
| `aaron-he-zhu/seo-geo-claude-skills` | ~229 · Apache-2.0 | 9/2026 | 20 skill theo khung CORE-EEAT |

### 2h.4 Dùng ảnh thế nào

- **Hợp** để phân việc trong nhóm SEO: ô đỏ giao cho agent nhưng có người duyệt đầu ra; ô cam là AI viết nháp, người sửa và ký; ô xám giữ cho người.
- **Đọc kèm** ba trang chính thức của Google: *AI features and your website*, *Using generative AI content*, *Spam policies* (mục scaled content abuse). Ba trang này đặt ranh giới cho mọi ô đỏ.
- **Thêm hai hàng ảnh thiếu**: đo lường (KPI khi click giảm) và kiểm soát crawler/snippet. Đây là việc của Lead/Manager.
- **Nếu dùng agent làm ô đỏ:** chọn skill có cổng chặn nội dung mỏng như `claude-seo`; đặt giới hạn chi phí cho API trả phí; không cho agent tự đăng hàng loạt trang hay tự gửi outreach.

**Nguồn §2h:** ảnh người dùng gửi 25/10/2026 · https://danhnolan.com (trang chủ, 25/10/2026) · https://developers.google.com/search/docs/appearance/ai-features (cập nhật 10/12/2025) · https://developers.google.com/search/docs/fundamentals/using-gen-ai-content (cập nhật 1/10/2026) · https://developers.google.com/search/docs/essentials/spam-policies (cập nhật 28/8/2026) · https://arxiv.org/abs/2311.09735 (GEO, KDD 2024) · Pew Research qua thewrap.com/ai-summaries-google-article-clicks-half và emarketer.com/content/google-ai-summaries-ending-search-sessions-reducing-click-through-behavior · github.com/AgriciDaniel/claude-seo (clone blob:none 25/10/2026, 412 commit, HEAD 6be93f4; README.md, PRIVACY.md, skills/seo-programmatic/SKILL.md, scripts/{content_humanize,indexing_notify}.py, install.sh) · img.shields.io/github/{stars,license,last-commit}/… cho 7 repo SEO/GEO (25/10/2026) · bên thứ ba: ppc.land/scaled-content-abuse · techcrunch.com/2024/03/05/google-takes-aim-at-seo-optimized-junk-pages-and-spam-with-new-search-update

## 2i. Kiểm ảnh "50 kho lưu trữ GitHub hữu ích" (infographic tiếng Việt, ảnh người dùng gửi, 2026-10-25)

> Infographic tiếng Việt không ghi tác giả: "50 kho lưu trữ GitHub hữu ích — tuyển chọn các kho chất lượng để học hỏi, xây dựng, tự động hóa và đổi mới". Mỗi ô có tên repo, mô tả một dòng và link (nhiều link bị cắt). Đã kiểm **cả 50 mục**: lấy số sao, license và commit cuối qua shields (25/10/2026); dùng `git ls-remote` so HEAD để phát hiện repo đã đổi chỗ (cùng hash = GitHub đang chuyển hướng); đọc README của các mục có vấn đề (nanoGPT, Bumblebee, iFixAi, awesome-claude-skills, TradingAgents, maigret); đối chiếu với hồ sơ đã có trong kho.

### 2i.1 Bảng kiểm (shields 25/10/2026)

| # | Repo | ★ | License | Commit cuối | Kiểm |
|---|---|---|---|---|---|
| 1 | `ifixai-ai/iFixAi` | 34k | Apache-2.0 | 10/2026 | ⚠️ Tên đúng là `iFixAi` (ảnh cắt). Chẩn đoán agent "lệch mục tiêu". ⚠️ 34k★/1,7k fork nhưng PyPI ~481 lượt tải/tháng; README dẫn site thương mại |
| 2 | `public-apis/public-apis` | 492k | MIT | 10/2026 | ✅ |
| 3 | `codecrafters-io/build-your-own-x` | 556k | **không ghi** | 7/2026 | ✅ |
| 4 | `kamranahmedse/developer-roadmap` | 370k | tự đặt/khác | 10/2026 | ✅ License tự đặt |
| 5 | `EbookFoundation/free-programming-books` | 400k | CC-BY-4.0 | 10/2026 | ✅ |
| 6 | `donnemartin/system-design-primer` | 376k | tự đặt/khác | 3/2026 | ✅ |
| 7 | `jwasham/coding-interview-university` | 363k | CC-BY-SA-4.0 | 12/2024 | ✅ Commit cuối 12/2024 |
| 8 | `jlevy/the-art-of-command-line` | 163k | **không ghi** | 7/2023 | ⚠️ Đứng yên từ 7/2023 |
| 9 | `practical-tutorials/project-based-learning` | 288k | MIT | 10/2026 | ✅ |
| 10 | `getify/You-Dont-Know-JS` | 185k | tự đặt/khác | 1/2026 | ✅ |
| 11 | `trimstray/the-book-of-secret-knowledge` | 253k | MIT | 11/2024 | ⚠️ Đứng yên từ 11/2024 |
| 12 | `yangshun/tech-interview-handbook` | 143k | MIT | 8/2026 | ✅ |
| 13 | `awesome-selfhosted/awesome-selfhosted` | 330k | tự đặt/khác | 10/2026 | ✅ |
| 14 | `trekhleb/javascript-algorithms` | 197k | MIT | 7/2026 | ✅ |
| 15 | `Chalarangelo/30-seconds-of-code` | 129k | CC-BY-4.0 | 9/2026 | ✅ CC-BY-4.0 |
| 16 | `github/gitignore` | 176k | CC0-1.0 | 10/2026 | ✅ |
| 17 | `ollama/ollama` | 185k | MIT | 10/2026 | ✅ |
| 18 | `langchain-ai/langchain` | 148k | MIT | 10/2026 | ✅ |
| 19 | `n8n-io/n8n` | 209k | tự đặt/khác | 10/2026 | ✅ License fair-code (Sustainable Use), không OSI |
| 20 | `openclaw/openclaw` | 393k | MIT | 10/2026 | ✅ Hồ sơ mục 02 |
| 21 | `langgenius/dify` | 159k | tự đặt/khác | 10/2026 | ✅ Apache-2.0 có điều khoản thêm |
| 22 | `langflow-ai/langflow` | 156k | MIT | 10/2026 | ✅ |
| 23 | `mem0ai/mem0` | 68k | Apache-2.0 | 10/2026 | ✅ |
| 24 | `browser-use/browser-use` | 119k | MIT | 10/2026 | ✅ |
| 25 | `crewAIInc/crewAI` | 60k | MIT | 10/2026 | ✅ |
| 26 | `geekan/MetaGPT` | 71k | MIT | 1/2026 | ⚠️ Đã chuyển sang `FoundationAgents/MetaGPT` |
| 27 | `microsoft/autogen` | 62k | CC-BY-4.0 | 10/2026 | ⚠️ **Chế độ bảo trì**; kế nhiệm là Microsoft Agent Framework (mục 02) |
| 28 | `Aider-AI/aider` | 50k | Apache-2.0 | 5/2026 | ⚠️ Commit cuối 5/2026 |
| 29 | `microsoft/markitdown` | 192k | MIT | 10/2026 | ✅ |
| 30 | `open-webui/open-webui` | 157k | tự đặt/khác | 10/2026 | ✅ License riêng giữ thương hiệu |
| 31 | `soxoj/maigret` | 39k | MIT | 10/2026 | ✅ OSINT: dựng hồ sơ một người từ username trên ~5.900 trang. Dual-use, cần cơ sở pháp lý khi dùng |
| 32 | `TauricResearch/TradingAgents` | 114k | Apache-2.0 | 10/2026 | ✅ Khung nghiên cứu, README không phải lời khuyên đầu tư |
| 33 | `browserbase/stagehand` | 26k | MIT | 10/2026 | ✅ |
| 34 | `mendableai/firecrawl` | 195k | AGPL-3.0 | 10/2026 | ⚠️ Đã chuyển sang `firecrawl/firecrawl`; **AGPL-3.0** |
| 35 | `huggingface/transformers` | 168k | Apache-2.0 | 10/2026 | ✅ |
| 36 | `vllm-project/vllm` | 95k | Apache-2.0 | 10/2026 | ✅ |
| 37 | `ggml-org/llama.cpp` | 132k | MIT | 10/2026 | ✅ |
| 38 | `run-llama/llama_index` | 53k | MIT | 10/2026 | ✅ |
| 39 | `karpathy/nanoGPT` | 64k | MIT | 11/2025 | ❌ README tự ghi "very old and deprecated" (11/2025), dùng `karpathy/nanochat` |
| 40 | `infiniflow/ragflow` | 93k | Apache-2.0 | 10/2026 | ✅ |
| 41 | `supermemoryai/supermemory` | 31k | MIT | 10/2026 | ✅ |
| 42 | `ComposioHQ/awesome-claude-skills` | 78k | **không ghi** | 7/2026 | ⚠️ Không có LICENSE; chép lại skill tài liệu của Anthropic (`document-skills`, "All rights reserved"); link UTM về Composio |
| 43 | `perplexityai/bumblebee` | 5.1k | Apache-2.0 | 10/2026 | ✅ Trình quét **chỉ đọc** lockfile, extension, cấu hình MCP trên máy dev (Go, v0.1.2), không phải "bảo mật AI" chung |
| 44 | `comfyanonymous/ComfyUI` | 143k | GPL-3.0 | 10/2026 | ⚠️ Đã chuyển sang `Comfy-Org/ComfyUI`; GPL-3.0 |
| 45 | `deepseek-ai/DeepSeek-V3` | 105k | MIT | 8/2025 | ⚠️ Ảnh trỏ tới tổ chức, không phải một repo; repo model (vd. DeepSeek-V3, commit cuối 8/2025) là trọng số + inference, không phải mã huấn luyện |
| 46 | `lobehub/lobe-chat` | 83k | tự đặt/khác | 10/2026 | ⚠️ Đã đổi tên thành `lobehub/lobehub`; license cộng đồng có điều kiện thương mại |
| 47 | `freeCodeCamp/freeCodeCamp` | 458k | BSD-3-Clause | 10/2026 | ✅ |
| 48 | `jwasham/coding-interview-university` | 363k | CC-BY-SA-4.0 | 12/2024 | ❌ **Trùng #7** |
| 49 | `langchain-ai/langchain` | 148k | MIT | 10/2026 | ❌ Trùng #18 (hoặc LangGraph; link bị cắt) |
| 50 | `n8n-io/n8n` | 209k | tự đặt/khác | 10/2026 | ❌ **Trùng #19** |

**Tổng:** 50 ô nhưng chỉ **47 repo khác nhau**: #48 trùng #7, #50 trùng #19, #49 trỏ `langchain-ai/l…` (trùng #18 nếu là LangChain). Repo tồn tại cả 50, không link nào chết. Còn lại:

- **4 repo đã đổi chỗ** (cùng HEAD với tên mới): MetaGPT → `FoundationAgents/MetaGPT`, Firecrawl → `firecrawl/firecrawl`, ComfyUI → `Comfy-Org/ComfyUI`, Lobe Chat → `lobehub/lobehub`. Link cũ vẫn chạy nhờ chuyển hướng, nhưng script hay lockfile nên dùng tên mới.
- **2 repo đã thôi phát triển chính:** nanoGPT (chính Karpathy ghi "deprecated", chuyển sang nanochat) và AutoGen (bảo trì, nhường cho Microsoft Agent Framework). **3 tài liệu đứng yên** từ 2023–2024 (the-art-of-command-line, the-book-of-secret-knowledge, coding-interview-university) vẫn đọc được, nhưng phần công cụ có thể đã cũ.
- **License cần đọc trước khi dùng thương mại:** n8n (Sustainable Use, không OSI), Firecrawl (**AGPL-3.0**), ComfyUI (GPL-3.0), Open WebUI và LobeHub (license riêng có điều kiện thương hiệu/thương mại), Dify (Apache-2.0 kèm điều khoản). `ComposioHQ/awesome-claude-skills` không có LICENSE mà lại chép skill tài liệu của Anthropic ghi "All rights reserved".
- **Mô tả sai hoặc lệch:**
  - #43 Bumblebee không phải "công cụ bảo mật AI" chung, mà là trình quét chỉ đọc cho phản ứng sự cố chuỗi cung ứng trên máy dev, có đọc cả cấu hình MCP.
  - #45 trỏ tới cả tổ chức DeepSeek, không phải một kho mã.
  - #1 iFixAi có số sao rất lệch so với lượt tải PyPI **(chưa xác minh là sao ảo; cần thận trọng)**.
- **Dual-use:** #31 maigret dựng hồ sơ cá nhân từ username, chỉ dùng khi có cơ sở pháp lý theo quy định bảo vệ dữ liệu cá nhân.

### 2i.2 Ảnh gom ba nhóm khác nhau

| Nhóm | Mục | Nên đọc ở |
|---|---|---|
| Học lập trình (tài liệu, lộ trình) | #2–16, #47–48 | Mục 08 §1–§3 (build-your-own-x, developer-roadmap, system-design-primer đã có hồ sơ) |
| Hạ tầng LLM và agent | #17–30, #33–41, #44–46 | Mục 02, 05, 10, 11, 14 (đa số đã có hồ sơ và đã kiểm license) |
| Công cụ ngách | #1, #31, #32, #42, #43 | Bảng trên; Bumblebee hợp với §3 mục 12 (chuỗi cung ứng) |

**Dùng thế nào:** coi ảnh là danh sách tên để tra, không phải danh sách để cài. Trước khi dùng một mục: thay tên repo cũ bằng tên mới; bỏ nanoGPT và AutoGen cho dự án mới; đọc license nếu nhúng vào sản phẩm. Với agent tự chủ (browser-use, OpenClaw, crewAI), đọc hồ sơ an toàn trong kho trước.

**Nguồn §2i:** ảnh người dùng gửi 25/10/2026 · img.shields.io/github/{{stars,license,last-commit}}/<repo>.json cho 47 repo (25/10/2026) · `git ls-remote` so HEAD: comfyanonymous/ComfyUI = Comfy-Org/ComfyUI, geekan/MetaGPT = FoundationAgents/MetaGPT, mendableai/firecrawl = firecrawl/firecrawl, lobehub/lobe-chat = lobehub/lobehub · README: github.com/karpathy/nanoGPT (thông báo 11/2025), github.com/perplexityai/bumblebee (26 commit, v0.1.2), github.com/ifixai-ai/iFixAi (331 commit từ 27/4/2026), github.com/ComposioHQ/awesome-claude-skills (`document-skills/*/LICENSE.txt`), github.com/TauricResearch/TradingAgents, github.com/soxoj/maigret · img.shields.io/pypi/dm/ifixai.json · bên thứ ba: decrypt.co/368944/perplexity-open-source-bumblebee-ai-scanner-mcp-infection-malware · discuss.pytorch.kr/t/ifixai-ai-45/11296 · pypi.org/project/iFixAi

## 2j. Nâng cấp 31/10/2026: rà repo lớn (awesome list và khoá học)

> Hai việc. (1) Đọc lại sao, license, ngày push của **31 repo** mục 08 đã có trong catalog (GitHub search API, 31/10/2026). (2) Tìm repo lớn còn thiếu: 7 truy vấn GitHub (`topic:awesome-list llm`, "awesome agents", "awesome claude", `topic:awesome ai`, "llm course tutorial", "for-beginners", và "awesome" tạo sau 1/10/2025), lọc theo `data/projects.json`. Chọn **7 repo**, clone `--filter=blob:none` và đọc file thật. Với awesome list, "độ sâu" là: sao, commit cuối, license đọc từ file, số mục đếm được, **thử 10 link** (lấy đều trong danh sách; link GitHub kiểm bằng `git ls-remote` vì proxy chặn trang HTML của github.com), người duy trì. **Không chạy script nào của các repo.**

### 2j.1 Repo cũ: điều đã đổi

| Repo | Thay đổi (12/10 → 31/10/2026) | Hệ quả |
|---|---|---|
| `kamranahmedse/developer-roadmap` | **Đã chuyển sang `nilbuild/developer-roadmap`** (370,9k★, GitHub báo `NOASSERTION`, push 31/10/2026); tìm theo tên cũ không còn kết quả | Catalog nên đổi `repo`; link cũ vẫn chuyển hướng **(chưa xác minh)** |
| `Shubhamsaboo/awesome-llm-apps` | ~105k → **143,6k** (+37%) | Vẫn là danh sách "có code" lớn nhất §2 |
| `hesreallyhim/awesome-claude-code` | ~45k → **57k**; GitHub báo `NOASSERTION` | Bảng §2 ghi "37–55k" đã cũ |
| `AgriciDaniel/claude-seo` | ~20k → **25k** | §2h |
| `mlabonne/llm-course` | Push cuối **5/2/2026** (gần 9 tháng) | Coi là tài liệu tĩnh; §2b đã ghi "ít commit" |
| `KalyanKS-NLP/LLM-Interview-Questions-and-Answers-Hub` | Push cuối **9/2/2026** | Bộ câu hỏi không theo kịp chủ đề 2026 (§2c.3) |
| `wong2/awesome-mcp-servers` · `EvanLi/Github-Ranking` | Catalog ghi `null`; nay **4,4k★ MIT** (push 13/7) · **12,7k★ MIT** (push 31/10) | Bổ sung số và license |
| `rasbt/LLMs-from-scratch`, `donnemartin/system-design-primer`, `NirDiamant/RAG_Techniques` | GitHub báo `NOASSERTION` | Không đổi license: catalog giữ license đã đọc trong file (Apache-2.0 + phần sách; CC BY 4.0; phi thương mại) |

Các repo khác dao động dưới 5%. `ai-engineering-from-scratch` ở §3 mục 8 ghi "(chưa xác minh)": nay đã xác minh, xem `rohitg00/…` dưới đây.

### 2j.2 Bảng nhanh 7 repo mới

| Repo | Nhóm | ★ · license | Commit cuối | Một dòng | Cờ |
|---|---|---|---|---|---|
| `rohitg00/ai-engineering-from-scratch` | Khoá học | 76,1k · MIT | 29/10/2026 | 542 bài trong 20 phase, code Python/TS/Rust/Julia, có bản README tiếng Việt | Gần như một người viết, 7 tháng tuổi |
| `sickn33/agentic-awesome-skills` | Kho skill + danh mục | 48,9k · MIT (code) + CC BY 4.0 (nội dung) | 31/10/2026 | 2.886 `SKILL.md`, installer npm ghim phiên bản, MCP "AAS Core" | Cài cả bộ làm phình ngữ cảnh |
| `VoltAgent/awesome-openclaw-skills` | Awesome list | 53,5k · MIT | 30/10/2026 | 5.213 skill OpenClaw lọc từ ClawHub, chia 30 nhóm | "Curated, not audited"; link đi qua `clawskills.sh` |
| `github/awesome-copilot` | Kho tuỳ biến chính chủ | 40,6k · MIT | 30/10/2026 | 222 agent, 193 instruction, 448 skill, 110 plugin, 8 hook cho Copilot | Quét rủi ro PR chỉ là "soft gate" |
| `e2b-dev/awesome-ai-agents` | Awesome list | 30,7k · **CC BY-NC-SA 4.0** | 21/8/2026 | 215 agent (mở và đóng), mỗi mục có category/mô tả/link | **Nội dung đứng yên từ 2024**, commit 2026 chỉ gắn UTM |
| `aishwaryanr/awesome-generative-ai-guide` | Lộ trình + danh sách khoá | 30,1k · MIT | 28/10/2026 | ~116 khoá ngoài + khoá miễn phí tự soạn, ngân hàng câu hỏi phỏng vấn | Kèm quảng cáo khoá Maven trả phí |
| `microsoft/mcp-for-beginners` | Khoá học | 17,6k · MIT | 30/10/2026 | 13 module MCP, mẫu đa ngôn ngữ, 54 bản dịch (có `vi`) | Không có CI cho code mẫu; SDK ghim `>=` |

### 2j.3 Awesome list: đếm mục và thử link

| Repo | Số mục (đếm 31/10) | 10 link thử | Người duy trì | Ghi chú |
|---|---|---|---|---|
| `VoltAgent/awesome-openclaw-skills` | 5.213 dòng `- [` trong `categories/*.md` (badge ghi 5.200, README ghi 5.300+) | **10/10 sống** (trang `clawskills.sh`; slug giả trả 404, nên 200 là thật) | VoltAgent (Necati Özmen, ~300/566 commit), 161 tác giả | README công bố đã loại 7.215 skill (4.065 spam, 373 độc hại theo báo cáo bảo mật công khai, 886 crypto…). CI chỉ bắt PR phải có link ClawHub. Repo lỡ commit `.claude/settings.local.json` chứa đường dẫn máy tác giả. Badge vẫn trỏ tên cũ `awesome-clawdbot-skills` |
| `e2b-dev/awesome-ai-agents` | 215 mục `## [` | 7 sống, **2 chết** (`encode.software` hết phân giải, ảnh `useinput.com`), 1 không kiểm được (trang org GitHub) | E2B (Tereza Tizkova ~340/473 commit) | Commit theo năm: 345 (2023), 120 (2024), 3 (2025), 5 (2026); 5 commit gần nhất đều là **thêm `utm_source` vào link e2b.dev**. LICENSE là CC BY-NC-SA 4.0 nên GitHub báo `NOASSERTION`; không chép nội dung vào sản phẩm thương mại |
| `aishwaryanr/awesome-generative-ai-guide` | `courses.md`: 116 link ngoài; 695 file (khoá tự soạn, 134 file phỏng vấn) | **9/10 sống**, 1 YouTube trả 429 (giới hạn tần suất, không phải chết) | Aishwarya Naresh Reganti (LevelUp Labs), 32 tác giả; 55/508 commit có trailer Claude | README tự ghi "một số listing bên ngoài có thể cần trả phí"; mỗi trang dẫn sang khoá Maven có phí |
| `sickn33/agentic-awesome-skills` | 2.886 `SKILL.md` trong `skills/` (+5.988 bản trong `plugins/`); mô tả ghi "2.884+" ✅ | `docs/sources/sources.md` có 64 link upstream: **10/10 sống** | `sickn33` (Nick), 502 tác giả; 899 commit của bot | Phần lớn mục là file trong repo, nên "link rot" ít liên quan; rủi ro là chất lượng từng skill |
| `github/awesome-copilot` | 222 / 193 / 448 / 110 / 8 (agent / instruction / skill / plugin / hook) | 10/10 là link `aka.ms` cài vào VS Code, trỏ về file `main` của chính repo | GitHub (Aaron Powell ~790 commit), 598 tác giả | Link cài trỏ `main`, không ghim commit |

### 2j.4 Hồ sơ ngắn

- **`rohitg00/ai-engineering-from-scratch`.** Tạo 18/3/2026, 2.631 commit, **2.368 commit của Rohit Ghumare** (nhịp 725 commit tháng 4, 808 tháng 10). Lời "542 lessons, 20 phases" ✅ khớp số thư mục `phases/*/*`. Có 1.423 file code trong `phases/`, CI `curriculum.yml` chạy `audit_lessons.py` và test lab chứng chỉ; bản dịch README do workflow chạy **NLLB-200 ngay trong runner** (không gửi API ngoài). Thư mục `certifications/claude` là tài liệu ôn **không chính thức**, tự ghi "confirm facts in the official…" và dẫn trang FAQ của Anthropic. `i18n/vi/README.md` chỉ dịch README, bài học vẫn tiếng Anh. Rủi ro: một người viết rất nhanh, chất lượng từng bài chưa ai đánh giá độc lập **(chưa xác minh)**. Học trên web hoặc `git clone https://github.com/rohitg00/ai-engineering-from-scratch`.
- **`sickn33/agentic-awesome-skills`.** Không chỉ là danh sách: monorepo có app web (Supabase, Vercel), 14 workflow (CodeQL, dependency-review, `skill-review` dùng Tessl khi có token), `LICENSE-CONTENT` tách CC BY 4.0 cho nội dung. Installer đáng học: README hướng dẫn **`npm exec --yes --ignore-scripts --package=agentic-awesome-skills@20.3.0 -- agentic-awesome-skills --release 20.3.0 --path .agents/skills --skills brainstorming,systematic-debugging --dry-run`**, tức ghim phiên bản, tắt script npm, xem trước rồi mới ghi. `tools/bin/install.js` chỉ gọi `git` và registry npm. Thận trọng: cài `--all` đưa hàng nghìn mô tả skill vào ngữ cảnh; README tự cảnh báo Antigravity bị quá tải.
- **`VoltAgent/awesome-openclaw-skills`.** Cùng chủ với `VoltAgent/awesome-agent-skills` (đã có trong catalog). Bảng "đã loại 7.215" là điểm cộng hiếm thấy, nhưng README nói rõ **"curated, not audited"** và khuyên xem báo cáo VirusTotal trên ClawHub trước khi cài. Mọi link đi qua `clawskills.sh` (site của VoltAgent) chứ không thẳng tới ClawHub, nên danh sách phụ thuộc một domain trung gian. Có khối quảng cáo Cloudways kèm mã giảm giá. Cài: `openclaw skills install <slug>` hoặc `npx clawhub install <slug>`.
- **`github/awesome-copilot`.** Repo chính chủ GitHub, 2.947 commit, 1.044 commit từ 1/7/2026. **64 workflow**, trong đó `pr-risk-scan.yml` chạy `eng/pr-risk-scan.mjs` với 5 luật regex: lời lẽ "bỏ qua guardrail", `curl | bash`, `npx -y`/`uvx`, lệnh chạy gói động, phiên bản không ghim. Kết quả chỉ được **bình luận vào PR (soft gate)**, không chặn merge. Có cả `resource-staleness-report` và `duplicate-resource-detector` viết bằng GitHub Agentic Workflows. Cài: `copilot plugin install <plugin>@awesome-copilot`.
- **`e2b-dev/awesome-ai-agents`.** Danh sách agent sớm nhất (6/2023) và được dẫn nhiều nhất. Đến 2026 nó là **tài liệu lịch sử**: hầu như không có mục mới sau 2024, nhiều agent trong list có thể đã ngừng (chưa kiểm từng mục), và commit gần đây chỉ gắn UTM cho link sản phẩm E2B. License CC BY-NC-SA (phi thương mại, chia sẻ tương tự), GitHub không nhận ra. Dùng để tra lịch sử, không để chọn công cụ.
- **`aishwaryanr/awesome-generative-ai-guide`.** Kết hợp danh sách khoá, lộ trình theo cấp, cập nhật nghiên cứu và **ngân hàng câu hỏi phỏng vấn** (bổ sung cho §2c.4). Commit đều (60 từ 1/7). Mỗi khoá có ký hiệu miễn phí/ngoài/video và năm. Nhược: lẫn quảng cáo khoá trả phí của chính tác giả.
- **`microsoft/mcp-for-beginners`.** 13 module từ khái niệm tới lab, README nói theo **MCP spec 2026-07-28** (khớp mục 04), có `02-Security`. 8.415 file là bản dịch tự động (`localizeflow[bot]` 831 commit), có `translations/vi` (cập nhật 19/9/2026, chậm hơn bản gốc). **Không có workflow CI nào**, nên 26 manifest mẫu trong `03-GettingStarted` (npm, pip, .NET, Maven) không được build tự động; mẫu TypeScript khai báo `"@modelcontextprotocol/sdk": ">=1.32.0"`, có thể kéo SDK v2 thay đổi API. Khi học, ghim phiên bản SDK trước khi chạy.

### 2j.5 Mẫu chung rút ra

1. **"Awesome list" đã thành kho nội dung**: 3/5 danh sách lớn mới (agentic-awesome-skills, awesome-copilot, openclaw-skills) chứa hoặc trỏ tới mã chạy được (skill, hook, plugin). Kiểm tra lúc này là kiểm **chuỗi cung ứng**, không chỉ kiểm link chết.
2. **Cổng tự động ít khi chặn thật**: risk-scan của awesome-copilot chỉ bình luận; CI của openclaw-skills chỉ đòi link ClawHub. Lớp lọc thật nằm ở registry (ClawHub + VirusTotal) hoặc người duyệt.
3. **Link rot thấp ở list còn sống, cao ở list đứng yên**: 10/10 ở openclaw-skills và sources của agentic-awesome-skills; 2/10 chết ở e2b. Ngày commit cuối không đủ: e2b "push 21/8/2026" nhưng nội dung dừng từ 2024.
4. **License nội dung khác license code**: CC BY-NC-SA (e2b), MIT + CC BY (agentic-awesome-skills), MIT + CC0 (prompts.chat, mục 17). GitHub báo `NOASSERTION` hoặc sai; đọc file.
5. **Sao tăng nhanh ở repo một người viết bằng agent**: ai-engineering-from-scratch (76k trong 7 tháng). Nội dung có CI kiểm cấu trúc nhưng chưa có đánh giá sư phạm độc lập.

**Nguồn §2j:** GitHub search API 31/10/2026 (`repo:` cho repo cũ và mới; 7 truy vấn chủ đề) · `meta_all.json`/`status_all.json` đợt rà 31/10 · clone `--filter=blob:none` 7 repo, đọc: rohitg00/ai-engineering-from-scratch (LICENSE, README.md, i18n/, phases/ (cây), .github/workflows/{curriculum,translate}.yml, certifications/claude/README.md), sickn33/agentic-awesome-skills (LICENSE, LICENSE-CONTENT, package.json, README.md, tools/bin/install.js, .github/workflows/skill-review.yml, docs/sources/sources.md), VoltAgent/awesome-openclaw-skills (LICENSE, README.md, categories/*.md, .github/workflows/pr-check.yml, .claude/settings.local.json), github/awesome-copilot (LICENSE, README.md, .github/workflows/pr-risk-scan.yml, eng/pr-risk-scan.mjs, docs/README.agents.md), e2b-dev/awesome-ai-agents (LICENSE.md, README.md, lịch sử commit), aishwaryanr/awesome-generative-ai-guide (LICENSE.md, README.md, courses.md), microsoft/mcp-for-beginners (LICENSE, README.md, 03-GettingStarted/01-first-server/solution/typescript/package.json, .github/) · thử link bằng curl và `git ls-remote` 31/10/2026 · https://github.com/nilbuild/developer-roadmap · https://clawskills.sh · https://aiengineeringfromscratch.com

## 3. Tài liệu nền tảng nên đọc (thứ tự gợi ý)

1. Anthropic – *Building Effective Agents* → *Effective Context Engineering for AI Agents* → *Writing tools for agents*.
2. ReAct (Yao 2022), Reflexion (Shinn 2023), *Landscape of Emerging AI Agent Architectures* (2024).
3. Manus – *Context Engineering for AI Agents: Lessons from Building Manus* (2025).
4. *Harness Engineering: Source-Code Study of Eleven Systems* (arXiv 2609.00006, 2026).
5. Geoffrey Huntley – *Ralph* (ghuntley.com/ralph) + README plugin `ralph-wiggum`.
6. agentskills.io spec · modelcontextprotocol.io spec · a2a-protocol.org spec · docs.ag-ui.com.
7. Refactoring UI · Laws of UX.
8. Alex Xu – *System Design Interview* Vol 1&2 (ghi chú 28 chương trong `seeker19110/system-design-notes`, kèm ~25 link paper gốc: Dynamo, Bigtable, Raft, Kafka…; upstream/license chưa rõ) · `ai-engineering-from-scratch` (được dhcb `2026-10-05-ai-engineering-source-inventory.md` liệt kê; chưa xác minh).

## 4. Nâng trần 2/11/2026: khoá học có cổng chấm, sách mở về vận hành và đánh giá (yêu cầu người dùng)

> Tìm tài liệu nền tảng cấp cao còn thiếu (khoá chính chủ, sách mở, bài tập có test). Số sao, license và ngày push lấy từ GitHub search API ngày 2/11/2026; clone `--filter=blob:none`, đọc LICENSE, README, cây thư mục, CI và file chính. **Không chạy mã nào của các repo.**

**Trần hiện tại**

- §2b và §2j toàn là khoá "đọc và làm theo" (Microsoft for-beginners, agents-course, ai-engineering-from-scratch). Cách đánh giá dừng ở số sao, link còn sống và CI kiểm cấu trúc. Chỉ agents-course có bài được chấm (leaderboard).
- Chưa có bài tập nào **chấm bằng unit test**, tức chưa có cách đo "đã học xong" bằng máy.
- §3 chỉ liệt kê blog và paper. Thiếu sách mở về **vận hành training/inference** và về **đánh giá LLM**, hai lớp mà mục 07 và mục 10 giả định người đọc đã biết.
- Bản tiếng Việt đã có ở các khóa Microsoft (§2b/§2j); đợt này bổ sung HF course nhưng phải ghi rõ phần chưa dịch.

**Bảng repo mới**

| Repo | Lớp | ★ · license (2/11/2026) | Commit cuối | Vì sao nâng trần | Rủi ro |
|---|---|---|---|---|---|
| `stanford-cs336/assignment1-basics` | Cổng máy | 3,1k · MIT | 7/4/2026 | Bài tập "LM from scratch" của CS336 (BPE, Transformer, AdamW, vòng huấn luyện), chấm bằng **48 test pytest + 15 snapshot (14 `.npz` + 1 `.pkl`)**. `tests/adapters.py` có 21 hàm nối mã người học vào test. `AGENTS.md`/`CLAUDE.md` yêu cầu agent đóng vai trợ giảng: không viết mã lời giải, không chạy lệnh | ⚠️ README vẫn ghi "Spring 2025", trong khi CHANGELOG đã là 26.0.x (4/2026). Phần huấn luyện và leaderboard cần GPU (handout nói B200) |
| `huggingface/course` | Chuẩn (khoá chính chủ) | 4,3k · Apache-2.0 | 6/10/2026 | Khoá chính thức của HF, 13 chương (0–12), gồm cả *Fine-tune LLMs* và *Build Reasoning Models*. Có **`chapters/vi`** (78 file mdx, chương 0–9) | Bản tiếng Việt **thiếu chương 10–12**. CI chỉ chạy `black` (`make quality`), không chạy notebook. ⚠️ Repo `huggingface/llm-course` chỉ có README 2 dòng, đừng nhầm |
| `stas00/ml-engineering` | Đầu bảng | 19,6k · CC BY-SA 4.0 | 1/11/2026 | Sách mở về training và inference LLM/VLM, viết từ kinh nghiệm huấn luyện BLOOM-176B: compute, network, storage, debug, testing. Kèm script đo (`network/benchmarks/all_reduce_bench.py`, `torch-dist-bench.py`, `storage/mmap-io-bench.py`…) và skill `skills/ml-engineering/SKILL.md` (164 dòng) + `skills/evaluate-cluster` | CC BY-SA áp cho toàn bộ nội dung. Script đo cần cluster thật (không chạy trong đợt này). Một tác giả chính |
| `huggingface/evaluation-guidebook` | Chuẩn (nền tảng eval) | 2,2k · CC BY-NC-SA 4.0 (GitHub báo `NOASSERTION`) | 3/12/2025 | 43 file: benchmark tự động, LLM-as-judge, đánh giá bằng người, troubleshooting (tokenization, tái lập kết quả), "yearly dives" 2023–2025 | ❌ README ghi **"NO LONGER MAINTAINED"**: bản mới nằm ở HF Space `OpenEvals/evaluation-guidebook`. License phi thương mại |
| `google-research/tuning_playbook` | Chuẩn | 30,4k · CC BY 4.0 (GitHub báo `NOASSERTION`) | 18/6/2024 | Quy trình tune siêu tham số có hệ thống (Google Research và Harvard): chọn kiến trúc, optimizer, batch size; thí nghiệm tăng dần; khi nào dừng. README khoảng 2.100 dòng | Đứng yên từ 2024, tự ghi "not an officially supported Google product". Viết cho deep learning nói chung, không bàn post-training LLM |

Ghi chú: `anthropics/courses` (23k★) **đã archive** (xem mục 17). Notebook trong đó gọi model Claude 3 (`claude-3-haiku-20240307` xuất hiện 82 lần), nên chạy lại cần đổi model ID. Phần *Prompt evaluations* (9 bài, 5 bài dùng promptfoo) vẫn nên đọc để học khái niệm.

**Stack nâng trần**

1. **Biến "đọc" thành "chấm được"**: sau `LLMs-from-scratch` hoặc `nanochat` (§2b), làm cs336 assignment1 tới khi `uv run pytest` xanh. Cấu hình agent khi học theo `AGENTS.md` của cs336 (trợ giảng, không viết lời giải). Áp cùng mẫu cho mọi repo học trong kho.
2. **Lộ trình tiếng Việt**: `huggingface/course` `chapters/vi` (chương 0–9) song song với `generative-ai-for-beginners/translations/vi` (§2b), sau đó đọc bản tiếng Anh chương 10–12.
3. **Học đánh giá trước khi dùng công cụ eval**: đọc evaluation-guidebook (bản Space), rồi mới tới lm-evaluation-harness, Inspect và promptfoo ở mục 07.
4. **Vận hành**: đọc ml-engineering khi bắt đầu tự host GPU (vLLM/SGLang ở mục 10); đọc tuning_playbook trước khi fine-tune.
5. **Tiêu chí chọn khoá mới**: ưu tiên khoá có test hoặc leaderboard (cs336, agents-course) hơn khoá chỉ có notebook không CI (như `mcp-for-beginners` §2j).

**Nguồn §4:** GitHub search API 2/11/2026 (`repo:` cho 7 repo, gồm `anthropics/courses` và `karpathy/nn-zero-to-hero`, cái sau đã xét nhưng không thêm vì đứng yên từ 8/2024) · clone `--filter=blob:none`: stanford-cs336/assignment1-basics (HEAD `a158843` 7/4/2026: LICENSE, README.md, CHANGELOG.md, AGENTS.md, CLAUDE.md, tests/), huggingface/course (`8b893f0` 6/10/2026: LICENSE, README.md, `chapters/en/_toctree.yml`, cây `chapters/vi`, `.github/workflows/quality.yml`), huggingface/llm-course (`aaee936`: chỉ README), stas00/ml-engineering (`dfcd0f8` 1/11/2026: LICENSE-CC-BY-SA, README.md, SKILL.md, skills/, script benchmark), huggingface/evaluation-guidebook (`e09b159` 3/12/2025: LICENSE, README.md, contents/, yearly_dives/), google-research/tuning_playbook (`7554a51` 12/6/2024: LICENSE, README.md), anthropics/courses (`f4dbb13`: LICENSE, README.md, đếm model ID trong `*.ipynb`) · https://huggingface.co/course/vi/chapter1/1 · https://huggingface.co/spaces/OpenEvals/evaluation-guidebook · https://cs336.stanford.edu

<a id="learning-prerequisites-evidence"></a>

## 5. Nâng trần 2/11/2026: điều kiện đầu vào, bài chuyển giao và bằng chứng học được (rà soát toàn diện)

> Bổ sung chiều sâu cho đợt §4 trong cùng ngày, không coi đây là một đợt phát hành mới của các dự án. Đọc metadata GitHub, clone nông, LICENSE, nội dung bài học, bài tập và CI của ba repo dưới đây. Mức bằng chứng: **đã đọc mã/cấu hình**, chưa cài hay chạy bài tập; số sao đọc 2/11/2026. Ngày commit là HEAD của nhánh mặc định, không phải ngày `pushed_at` của cả repo.

### 5.1 Khoảng trống sau §4

§4 thêm cổng chấm của CS336 và sách vận hành, nhưng vẫn thiếu cách chọn **điểm bắt đầu**. Người chưa biết shell không nên đi thẳng vào harness; người chưa biết gradient/split dữ liệu dễ chạy notebook mà không hiểu kết quả. Một test xanh khi agent đã viết cả lời giải cũng chưa chứng minh người học tự chuyển kiến thức sang bài mới. Các tiêu chí chuyển cấp dưới đây là **đề xuất biên tập của kho**, không phải điều kiện cấp chứng chỉ của trường hay benchmark đã được kiểm nghiệm.

| Repo | Vai trò | ★ · license (2/11/2026) | HEAD · ngày commit | Giá trị và giới hạn |
|---|---|---|---|---|
| `missing-semester/missing-semester` | Nền thao tác cho developer | 6.152 · **CC BY-NC-SA 4.0**, gồm cả source website, bài tập và video | `1d695c94ccafdce3f06d6b9dfe3e6f106097693a` · 8/10/2026 | Bản 2026 có shell, Git, chất lượng code, shipping và agentic coding; bài tập yêu cầu tự cấu hình công cụ. CI build Jekyll và kiểm link, **không phải autograder bài người học** |
| `d2l-ai/d2l-en` (*Dive into Deep Learning*) | Nền toán + mô hình | 29.986 · docs **CC BY-SA 4.0**, sample code **MIT sửa đổi** theo hai file license riêng | `23d7a5aecceee57d1292c56e90cce307f183bb0a` · 16/3/2024 | Chương Preliminaries nối tensor, đại số tuyến tính, vi tích phân, autograd, xác suất vào code; có CI gửi bài chạy nhiều framework lên AWS Batch. HEAD cũ; cấu hình build ghim Python 3.9/PyTorch 2.0/CUDA 11, không suy ra chạy sạch trên stack 2026 |
| `DataTalksClub/mlops-zoomcamp` | Đồ án vòng đời ML | 15.516 · **không tìm thấy LICENSE trong checkout** | `1cf2248a803bf8a2685f87941a679eca2712516d` · 16/9/2026 | Khóa của cộng đồng DataTalks.Club, có prerequisites, rubric về tracking/deploy/monitoring/reproducibility và peer review. Đọc miễn phí không đồng nghĩa được phép phân phối lại toàn bộ tài liệu/mã |

### 5.2 Đọc cổng thật và điều kiện tích hợp

- **Missing Semester** do Anish Athalye, Jon Gjengset và Jose Javier Gonzalez, các cựu sinh viên MIT, đồng giảng. Bài `code-quality` yêu cầu cố ý làm hỏng code để kiểm CI phát hiện; bài `agentic-coding` nối test thất bại vào vòng sửa của agent. Hai workflow của website chỉ build/kiểm link. Dùng như lớp học shell/Git/debug trước mục 01/13; có thể tự làm lại bài tập trên một repo riêng. License NC/SA cần được xét trước khi đóng gói nội dung vào khóa thương mại. [Bài học và bài tập ghim commit](https://github.com/missing-semester/missing-semester/blob/1d695c94ccafdce3f06d6b9dfe3e6f106097693a/_2026/code-quality.md), [license](https://github.com/missing-semester/missing-semester/blob/1d695c94ccafdce3f06d6b9dfe3e6f106097693a/license.md), [CI](https://github.com/missing-semester/missing-semester/tree/1d695c94ccafdce3f06d6b9dfe3e6f106097693a/.github/workflows).
- **D2L** là sách của Aston Zhang, Zachary Lipton, Mu Li và Alex Smola, có bản in Cambridge University Press 2023. `chapter_preliminaries/autograd.md` chứa code đối chiếu nhiều framework, không chỉ hình minh họa. Hợp cho người thiếu nền trước `LLMs-from-scratch`/CS336 (§2b/§4); không phải khóa vận hành agent. `LICENSE-SUMMARY` tách nội dung và sample code; khi lấy một đoạn code phải kiểm đúng phạm vi. CI có bước evaluate framework, nhưng **chưa xác minh kết quả run gần nhất**. [Preliminaries](https://github.com/d2l-ai/d2l-en/blob/23d7a5aecceee57d1292c56e90cce307f183bb0a/chapter_preliminaries/index.md), [license summary](https://github.com/d2l-ai/d2l-en/blob/23d7a5aecceee57d1292c56e90cce307f183bb0a/LICENSE-SUMMARY), [build dependencies](https://github.com/d2l-ai/d2l-en/blob/23d7a5aecceee57d1292c56e90cce307f183bb0a/static/build.yml).
- **MLOps Zoomcamp** yêu cầu Python, Docker, command line, ML và ít nhất một năm lập trình theo README; do đó không xếp làm khóa nhập môn đầu tiên. Rubric có thể tham khảo để đánh giá đồ án nhưng là **peer review**, không phải chứng nhận mọi đường code đã được kiểm. CI mẫu chỉ nhận PR vào `develop` với thay đổi dưới `06-best-practices/code/**`; đường dẫn integration test ghi `integraton-test` trong khi thư mục thật là `integration-test`. CD mẫu còn dùng `terraform apply -auto-approve` và tự ghi phần lấy model chưa phù hợp production. Nên học cơ chế và tự thiết kế pipeline cho repo đích, không chép nguyên workflow. [Prerequisites](https://github.com/DataTalksClub/mlops-zoomcamp/blob/1cf2248a803bf8a2685f87941a679eca2712516d/README.md), [rubric](https://github.com/DataTalksClub/mlops-zoomcamp/blob/1cf2248a803bf8a2685f87941a679eca2712516d/07-project/README.md), [CI mẫu](https://github.com/DataTalksClub/mlops-zoomcamp/blob/1cf2248a803bf8a2685f87941a679eca2712516d/.github/workflows/ci-tests.yml), [CD mẫu](https://github.com/DataTalksClub/mlops-zoomcamp/blob/1cf2248a803bf8a2685f87941a679eca2712516d/.github/workflows/cd-deploy.yml).

### 5.3 Ma trận chọn và bằng chứng chuyển cấp

| Người học / mục tiêu | Điểm bắt đầu | Bằng chứng đề xuất để chuyển cấp | Không suy rộng từ bằng chứng |
|---|---|---|---|
| Biết viết code, chưa tự debug môi trường | Missing Semester | Tạo repo nhỏ có CLI, test, CI; cố ý gây một lỗi rồi tìm và sửa bằng log/Git; giải thích từng quyền/lệnh agent được dùng | Website khóa build xanh không chứng minh bài người học đúng |
| Muốn hiểu model thay vì chỉ gọi API | D2L → `LLMs-from-scratch` → CS336 §4 | Tự giải thích shape/gradient; kiểm đạo hàm số trên ví dụ nhỏ; làm bài khác dữ liệu mà vẫn qua test | Học toàn bộ toán không phải điều kiện bắt buộc cho mọi ứng dụng LLM |
| Đã biết ML, cần đưa model vào dịch vụ | MLOps Zoomcamp; sách ml-engineering §4 | Repo đồ án có dependency ghim, dữ liệu mẫu, training/run ID, deployment, test tích hợp và cảnh báo được kích hoạt thử | Peer score không chứng minh chịu tải, phục hồi hay an toàn production |
| Chỉ cần xây agent ứng dụng | agents-course §2b + nền shell/Git còn thiếu | Một workflow có tool giả lập, timeout/trần chi phí, tập eval giữ riêng và log lý do thất bại | Không cần học training cluster hay CS336 trước mọi dự án agent |

### 5.4 Ghép thành lộ trình có thể kiểm lại

1. **Đánh giá đầu vào bằng việc nhỏ**, không bằng số khóa đã xem: tái lập một lỗi CLI, đọc một tensor shape hoặc viết một test API; chọn nhánh tương ứng trong §5.3.
2. **Một repo đồ án xuyên suốt**: mỗi bài học thêm một artifact vào repo của người học, từ test/CI (mục 13), eval giữ riêng (mục 07), đến dữ liệu/model có phiên bản (mục 10/15). Kho này chỉ lưu đánh giá, không chứa bài giải hay công cụ đào tạo.
3. **Tách mức hỗ trợ của agent** trong báo cáo học: tự làm / gợi ý / sinh một phần / sinh toàn bộ; khi kiểm chuyển giao dùng bài mới và yêu cầu người học giải thích, chẩn đoán lỗi. Đây là đề xuất đánh giá của kho, chưa có nghiên cứu trong đợt này chứng minh ngưỡng tối ưu.
4. **Đồ án kết thúc bằng một lỗi có kiểm soát**: làm hỏng schema, dừng một dependency giả hoặc gây timeout trong môi trường thử, rồi chứng minh test/alert và phục hồi hoạt động. Nối sang thực hành vận hành ở mục 09 §3d.

**Đã đổi sau §4:** không hạ thấp các nguồn đã có chỉ vì không có autograder; thay vào đó phân biệt build tài liệu, test ví dụ, chấm bài và khả năng chuyển giao. Khóa nền tảng cũ vẫn hữu ích nếu ghi rõ phần dependency đã cũ; phần không có LICENSE không được gắn nhãn MIT từ suy đoán.

**Nguồn §5:** metadata GitHub API ngày 2/11/2026 và các permalink ở §5.2; đọc thêm nguồn chính thức ngoài repo: [Missing Semester 2026](https://missing.csail.mit.edu/2026/course-shell/), [D2L Preface](https://d2l.ai/chapter_preface/index.html), [DataTalks.Club MLOps Zoomcamp](https://datatalks.club/blog/mlops-zoomcamp.html), [tài liệu đồ án](https://datatalksclub.github.io/docs/courses/mlops-zoomcamp/project/). Đã đọc `license.md`, `.github/workflows/{build,links}.yml`, `_2026/{course-shell,code-quality,agentic-coding}.md` của Missing Semester; `LICENSE*`, `chapter_preliminaries/{index,autograd}.md`, `.github/workflows/ci.yml`, `static/build.yml` của D2L; `README.md`, `07-project/README.md`, `06-best-practices/code/{model.py,tests/model_test.py}`, hai workflow CI/CD của Zoomcamp. **Chưa chạy bài tập, model, cloud hay workflow của các nguồn.**

## 5b. Kiểm ảnh codecrafters-io/build-your-own-x: license thật, nhịp bảo trì và link chết (ảnh trang repo người dùng gửi, 3/11/2026)

> Ảnh là trang repo: 288 issue, 401 PR, 52,3k fork, 559k★, commit cuối `aa17439` (Paul Kuruvilla, "4 months ago"), About "Master programming by recreating your favorite technologies from scratch", link codecrafters.io, topic awesome-list/free/programming/tutorial-code/tutorial-exercises/tutorials. Repo đã có ở §1 (bảng #1) và §2i (#3). Đợt này clone đủ lịch sử, HEAD `aa17439b62f384511a5561ce308e9598b94d8989`, và kiểm link.

| Ô trong ảnh / câu hỏi | Kết quả | Đối chiếu (3/11/2026) |
|---|---|---|
| 559k★, 52,3k fork | ✅ | 559.221★, 52.319 fork (GitHub search API) |
| 288 issue + 401 PR | ✅ | API trả 689 issue+PR mở (= 288 + 401). Hàng đợi đóng góp lớn so với nhịp duyệt |
| Commit cuối "4 months ago" | ✅ | `aa17439` ngày 14/7/2026. Trong 12 tháng gần nhất chỉ có hai đợt merge: một loạt PR ngày 21/2/2026 và vài PR tháng 6–7/2026. 616 commit từ 9/5/2018 |
| **License** (ảnh không hiện) | ✅ CC0, nhưng chỉ khai trong README | Repo **không có file LICENSE**, nên GitHub API trả `license: null` (vì thế §2i ghi "không ghi"). Mục "Origins & License" cuối README gắn badge CC0 1.0. Catalog ghi CC0 là đúng theo README. CC0 áp cho danh sách; mỗi bài hướng dẫn được dẫn link có license riêng của tác giả |
| Quan hệ thương mại | ℹ️ | Repo thuộc org CodeCrafters (nền tảng học có trả phí); dòng đầu README là banner dẫn tới `codecrafters.io/github-banner`. Người khởi xướng ban đầu là Daniel Stefanovic |

**Nội dung và độ tươi của link** (kiểm bằng curl ngày 3/11/2026 từ môi trường của kho; chỉ đọc mã trạng thái HTTP, không đọc nội dung)

- README có **31 chủ đề** (`#### Build your own …`: Database, Docker, Git, Operating System, Programming Language, Web Browser, AI Model, Neural Network…) và khoảng 389 mục; tách được 359 link dạng `* [..](url)`. Tên miền nhiều nhất: github.com 42, youtube.com 34, medium.com 20, aosabook.org 11.
- Kết quả: **257 trả 200**; 73 trả 403 và 17 trả 429. Toàn bộ 42 link github.com rơi vào 403 vì proxy của môi trường kiểm chặn curl tới GitHub, còn Medium và YouTube thường chặn bot, nên nhóm 403/429 **không kết luận được**.
- **Chắc chắn hỏng (404, kiểm hai lần): 4 link**: `sj14.gitlab.io` (Go Unix shell), `joaoventura.net` (Python web server), `seasonofcode.com` (X window manager), `joshburns-xyz.vercel.app` (Git plugin).
- **Không truy cập được: 6 link**: `blog.usejournal.com` (không còn DNS), `tutorials.botsfloor.com`, `dev.stephendiehl.com/fun/` ("Write You a Haskell"), `stories.algolia.com`, `ilovephp.jondh.me.uk`, `lethalbrains.com` (timeout); `jamesmolloy.co.uk` (hướng dẫn OS kinh điển) trả 503. Một số có thể chỉ tạm thời; nên tìm bản lưu trên web.archive.org.
- Tức là ít nhất khoảng 3% link đã hỏng; con số thật có thể cao hơn trong nhóm chưa kiểm được.

**Dùng thế nào**: vẫn là điểm vào tốt nhất để chọn bài "tự dựng lại X". Nhưng hãy coi đây là danh mục 2018–2024 được bảo trì thưa: kiểm ngày đăng và phiên bản ngôn ngữ của từng bài, dùng bản lưu archive khi link chết. Với bài có cổng chấm tự động, xem codecrafters.io (trả phí) hoặc các khoá có autograder ở §4.

**Nguồn §5b:** ảnh trang repo người dùng gửi 3/11/2026 · clone https://github.com/codecrafters-io/build-your-own-x HEAD `aa17439b62f384511a5561ce308e9598b94d8989` (https://github.com/codecrafters-io/build-your-own-x/blob/aa17439b62f384511a5561ce308e9598b94d8989/README.md, mục "Origins & License"; `git log`) · curl HTTP status 359 link ngày 3/11/2026 (`-L --max-time 12`, kiểm lại 404/000 với timeout 20–30 s) · GitHub search API `repo:codecrafters-io/build-your-own-x` 3/11/2026.

## 6. Nâng trần 4/11/2026: đào tạo theo vai trò và bài chuyển giao của xưởng

<a id="learning-factory-2026-11-04"></a>

§4–§5 đã phân biệt đọc sách, test ví dụ, chấm bài và khả năng chuyển giao. Khoảng trống còn lại là **đào tạo đội làm sản phẩm phần mềm**, ngoài nhánh ML/agent: yêu cầu → giao diện/API → dữ liệu → test → phát hành → vận hành. Đợt này đọc nguồn ghim commit, chưa chạy bài tập hay xác minh kết quả cấp chứng chỉ.

### 6.1 Hai nguồn bổ sung và cổng thực tế

<a id="exercism-python-factory"></a>

**Exercism Python track** (exercism/python), MIT, SHA **6105f6d9d3ef66ce3d5c8f529d2882af3d76b706**, HEAD 2026-09-30; đọc 2026-11-04. Có đề bài, test và lời giải mẫu/approach. Ví dụ leap_test.py nhập hàm leap_year và kiểm các ranh giới chia 4/100/400; bin/test_exercises.py là đường runner, workflow test-runner.yml gọi Docker Compose. Đây là bài nhỏ có đầu vào/đầu ra rõ để luyện test/debug; **không phải** bằng chứng người học thiết kế được hệ nhiều dịch vụ. Học viên có thể nhìn thấy test và lời giải, nên test xanh không đo được độc lập khả năng tự làm. Image runner trong docker-compose.yml không ghim digest; nếu dùng làm cổng nội bộ phải ghim artifact riêng và lưu phiên bản bài tập.

<a id="full-stack-open-factory"></a>

**Full Stack Open** (fullstack-hy2020/fullstack-hy2020.github.io), khóa của Đại học Helsinki, SHA **9c24482abcf387699d0f36bcdff5811dbe2ce5a7**, HEAD 2026-10-17; đọc 2026-11-04. Phần 11 yêu cầu dựng pipeline cho ứng dụng mẫu, rồi áp dụng sang ứng dụng tự làm; nối được React/Node, test, CI/CD, container và relational database. LICENSE gốc là **CC BY-NC-SA 3.0**, không gắn nhãn MIT hoặc coi nội dung là mã nguồn mở OSI. Tham khảo/link khóa; xét điều khoản trước khi đóng gói lại thành khóa thương mại hay phân phối bản dịch.

**Đọc CI thay vì đoán:** workflow continuous-integration-workflow.yml của website dùng Gatsby build trên nhánh source với Node 10. Đó là build nội dung website, **không phải autograder bài học viên**; không lấy Node 10 làm runtime cho ứng dụng sản phẩm mới. Phần 11 cũng tự nói không phủ triển khai phức tạp như zero downtime và migration; nối sang mục 32/34 để học phần còn thiếu, thay vì gắn nhãn “production-ready” sau khi hoàn tất khóa.

### 6.2 Ma trận vai trò và bằng chứng trưởng thành

| Vai trò/tình huống | Nguồn đầu vào | Artifact thực hành trong repo riêng | Bài kiểm chuyển giao |
|---|---|---|---|
| Developer mới, thiếu thao tác/debug | Missing Semester §5 + Exercism | Test ranh giới và ca lỗi, log chẩn đoán, PR nhỏ | Bài tương tự nhưng dữ liệu/quy tắc mới; giải thích lỗi mà không đọc đáp án |
| Full-stack developer | Full Stack Open + mục 06/29/30/34 | API contract, migration, UI có trạng thái lỗi, test tích hợp và pipeline | Thay schema có tương thích ngược, phát hiện regression và rollback trong môi trường thử |
| AI application engineer | agents-course/LLM guidebook đã có + mục 07/10 | Dataset eval riêng, tool giới hạn quyền, báo cáo chất lượng/latency/cost | Chẩn đoán retrieval fail khác generation fail, sửa mà không lộ holdout |
| Tech lead/QA/platform | System Design Primer + mục 09/29–34 | ADR, kế hoạch kiểm theo rủi ro, SLO và bằng chứng phục hồi | Review độc lập một release có lỗi được cài trước; quyết định go/no-go có căn cứ |

### 6.3 Từ đào tạo sang năng lực giao hàng

- **Đầu vào theo việc cần làm:** chọn nhánh từ một bài chẩn đoán, không bắt mọi người học training model trước khi làm web/API. Dùng 2–4 nguồn cùng vai trò để đối chiếu, tránh khóa học bị biến thành một stack bắt buộc.
- **Cùng một sản phẩm mẫu của đội:** yêu cầu và acceptance ID → code/test → phát hành → incident giả lập; mỗi người đóng góp artifact khác nhau để luyện bàn giao. Kho stored chỉ ghi đánh giá nguồn, không chứa app hay bài giải triển khai.
- **Tách hỗ trợ AI khỏi năng lực được đánh giá:** ghi đã dùng agent ở bước nào; giữ một bài chuyển giao mới, phần giải thích và phần sửa lỗi trực tiếp. Không suy phẩm chất con người từ số commit hay lượng code sinh.
- **Nghiệm thu có reviewer:** chất lượng giải pháp, test có bắt được lỗi cố ý, khả năng tái lập và vận hành; thời gian/ngưỡng do vai trò quyết định. Các tiêu chí này là đề xuất cho xưởng, chưa phải rubric đã được nghiên cứu kiểm định.

**Nguồn §6:** [LICENSE](https://github.com/exercism/python/blob/6105f6d9d3ef66ce3d5c8f529d2882af3d76b706/LICENSE) · [README.md](https://github.com/exercism/python/blob/6105f6d9d3ef66ce3d5c8f529d2882af3d76b706/README.md) · [exercises/practice/leap/leap_test.py](https://github.com/exercism/python/blob/6105f6d9d3ef66ce3d5c8f529d2882af3d76b706/exercises/practice/leap/leap_test.py) · [bin/test_exercises.py](https://github.com/exercism/python/blob/6105f6d9d3ef66ce3d5c8f529d2882af3d76b706/bin/test_exercises.py) · [docker-compose.yml](https://github.com/exercism/python/blob/6105f6d9d3ef66ce3d5c8f529d2882af3d76b706/docker-compose.yml) · [.github/workflows/test-runner.yml](https://github.com/exercism/python/blob/6105f6d9d3ef66ce3d5c8f529d2882af3d76b706/.github/workflows/test-runner.yml) · [LICENSE](https://github.com/fullstack-hy2020/fullstack-hy2020.github.io/blob/9c24482abcf387699d0f36bcdff5811dbe2ce5a7/LICENSE) · [src/content/11/en/part11a.md](https://github.com/fullstack-hy2020/fullstack-hy2020.github.io/blob/9c24482abcf387699d0f36bcdff5811dbe2ce5a7/src/content/11/en/part11a.md) · [.github/workflows/continuous-integration-workflow.yml](https://github.com/fullstack-hy2020/fullstack-hy2020.github.io/blob/9c24482abcf387699d0f36bcdff5811dbe2ce5a7/.github/workflows/continuous-integration-workflow.yml)

## 6b. Hồ sơ patchy631/ai-engineering-hub: hơn 90 dự án AI chạy được, xếp theo mức độ (ảnh README người dùng gửi, đọc 6/11/2026)

> Ảnh là phần đầu README: badge "GitHub Trending #1 Repository Of The Day", banner LLMs · RAG · AI Agents · MCP · LLMOps · Evaluations (join.DailyDoseofDS.com), "93+ Production-Ready Projects across all skill levels", hướng dẫn chuyên sâu về LLM, RAG, agent, ứng dụng agent thật. §2 trước đây chỉ có một dòng bảng. Đã clone `--filter=blob:none`, HEAD `042aeb5067384981eeba6a07fa882f436bb1660d` (30/10/2026). **Không chạy dự án nào.**

| Thuộc tính | Giá trị (6/11/2026) |
|---|---|
| Repo | https://github.com/patchy631/ai-engineering-hub · **41.193★** (GitHub search API), MIT, tạo 21/10/2024 |
| Tác giả | Akshay Pachaar (`patchy631`, Daily Dose of Data Science) cùng cộng tác viên, nổi bật là Sitam Meur; 554 commit |
| Nội dung | Hơn 100 thư mục dự án, mỗi dự án là một ứng dụng độc lập có README riêng (118 README), 69 file `requirements.txt`/`pyproject.toml`, 53 file `.env.example` để điền key |
| Lộ trình | README xếp **88 dự án** theo mức: **22 cơ bản** (OCR và thị giác, giao diện chat, RAG cơ bản, đa phương tiện), **44 trung cấp** (agent và workflow, voice, RAG nâng cao, đa phương thức, MCP, so sánh và đánh giá model), **22 nâng cao** (fine-tuning, hệ agent nâng cao, MCP và hạ tầng, hệ thống production). Kèm `ai-engineering-roadmap/` cho người mới và `courses/anthropic-academy-courses/` |

**Điểm mạnh**

- **Học bằng dự án chạy được**: mỗi thư mục là một ứng dụng hoàn chỉnh (thường Streamlit hoặc notebook) kèm file phụ thuộc và mẫu `.env`, nên clone một thư mục là chạy được ngay.
- **Phủ đủ chuỗi AI engineering hiện nay**: RAG (cơ bản, agentic, corrective, ColBERT, ModernBERT, multimodal, Milvus + Groq, Docling), agent (CrewAI, AutoGen, Swarm, A2A, ACP), MCP (memory, voice, video RAG, Graphiti, MindsDB, Pixeltable), voice agent, OCR local (Llama 3.2 Vision, Gemma 3, Qwen 2.5 VL), fine-tuning (DeepSeek, GRPO trên Qwen3, knowledge distillation), context engineering, eval và observability, triển khai an toàn (OpenClaw).
- **Bài so sánh model đặt cạnh nhau** (Llama 4 vs DeepSeek-R1, Qwen3 vs DeepSeek-R1, Sonnet 4 vs o4, gpt-oss vs Qwen3, MiniMax M2 vs Sonnet 4.5 vs Kimi K2 vs Gemini 3…), tiện để chọn model cho bài toán cụ thể.
- **Ưu tiên chạy cục bộ**: nhiều dự án dùng model mở qua Ollama (local ChatGPT với DeepSeek hoặc Gemma 3, OCR 100% local).
- **Cập nhật đều**: dự án mới theo các model và chuẩn mới (MCP, A2A, gpt-oss, YOLO26), nhiều cộng tác viên.

**Dùng thế nào**: người mới bắt đầu từ `ai-engineering-roadmap`, rồi đi theo ba mức cơ bản → trung cấp → nâng cao trong README. Muốn tham khảo cách làm một tính năng (RAG cho tài liệu, voice agent, MCP server) thì mở đúng thư mục đó, đọc README, điền `.env` theo mẫu rồi chạy. Kết hợp với lộ trình học ở §1–§2 và các khóa có chấm tự động ở §4.

**Nguồn §6b:** ảnh README người dùng gửi 6/11/2026 · clone https://github.com/patchy631/ai-engineering-hub HEAD `042aeb5067384981eeba6a07fa882f436bb1660d`: https://github.com/patchy631/ai-engineering-hub/blob/042aeb5067384981eeba6a07fa882f436bb1660d/README.md (Projects by Difficulty) · https://github.com/patchy631/ai-engineering-hub/blob/042aeb5067384981eeba6a07fa882f436bb1660d/LICENSE · `ai-engineering-roadmap/`, `courses/` · `git ls-tree`, `git shortlog` · GitHub search API `ai-engineering-hub` 6/11/2026.

## 6c. Kho repo của Phan Đông Giang (phandonggiang.com/kho-repo): 694 repo, 32 nhóm, và 24 repo AI/agent đọc mã (bảng người dùng dán, kiểm 18/11/2026)

> Người dùng dán bảng repo của trang https://phandonggiang.com/kho-repo (trang chặn truy cập tự động nên không tải trực tiếp). Bảng có 694 repo với số sao, nhóm, ngôn ngữ, link và mô tả. Mục này ghi lại toàn bộ danh sách đã kiểm và đọc mã 24 repo AI/agent nổi bật chưa có hồ sơ. Tác giả cũng là người làm ảnh "8 plugin, 8 kỹ năng, 8 MCP" ở mục 20 §3zb.

### 6c.1 Toàn bộ danh sách đã kiểm

- **Dữ liệu:** [`data/collections/phandonggiang-kho-repo.json`](../data/collections/phandonggiang-kho-repo.json). Có đủ 694 repo; mỗi mục ghi tên chuẩn, số sao, fork, giấy phép, ngày push, ngôn ngữ, mô tả theo GitHub search API ngày 18/11/2026, và mục tương ứng của kho này.
- **Số sao khớp:** sao trên trang lệch dưới 10% so với API ở 691/694 repo; tổng sao cả danh sách khoảng 34,7 triệu.
- **Đổi tên:** 3 repo đã chuyển chủ: `forrestchang/andrej-karpathy-skills` → `multica-ai/andrej-karpathy-skills`, `facebook/create-react-app` → `react/create-react-app`, `dwarvesf/hidden` → `consolelabs/hidden`.
- **Trạng thái:** `base/node` đã archive; `microsoft/onnxruntime` không truy cập công khai được ngày 18/11/2026.
- **Giấy phép:** MIT 236, Apache-2.0 159, GPL/AGPL 88; 174 repo không ghi giấy phép chuẩn (NOASSERTION hoặc không có), cần đọc file LICENSE trước khi dùng.
- **Nhóm lớn nhất:** Mô hình AI & Huấn luyện (53), Học AI & ML (51), Nền tảng AI/RAG/Workflow (41), Năng suất & Ghi chú (40), Editor & Terminal (37), Awesome (33), AI Ảnh & Giọng nói (33), AI Agent & MCP (32), Tài liệu/OCR (31), Trợ lý lập trình AI (26).
- **Trùng với kho:** `andrej-karpathy-skills` (mục 20 §3k.3); `aaif-goose/goose` là `block/goose` (mục 01) đã chuyển sang tổ chức mới.

### 6c.2 Hai mươi bốn repo AI/agent đọc mã

| Repo | ★ (18/11/2026) | Giấy phép | Làm gì | Điểm mạnh (đọc mã) | Cài | Điều kiện dùng |
|---|---|---|---|---|---|---|
| [`karpathy/autoresearch`](https://github.com/karpathy/autoresearch) | 100.199 | MIT (chỉ ghi trong README) | Bộ huấn luyện LLM nhỏ trên một GPU (rút gọn từ nanochat) để agent tự thử nghiệm qua đêm: sửa `train.py`, huấn luyện 5 phút, đo `val_bpb`, giữ hoặc bỏ thay đổi rồi lặp lại; người chỉ viết `program.md`. | Ba file chính (`prepare.py` cố định, `train.py` agent sửa, `program.md` người sửa) nên diff dễ duyệt; ngân sách 5 phút mỗi lần nên khoảng 12 thí nghiệm mỗi giờ so sánh được; chỉ số `val_bpb` không phụ thuộc kích thước từ vựng. | `uv sync && uv run prepare.py && uv run train.py` | GPU NVIDIA (thử trên H100), Python 3.10+; CPU/MPS dùng các fork README liệt kê; README khuyên chạy agent với mọi quyền bị tắt. |
| [`farion1231/cc-switch`](https://github.com/farion1231/cc-switch) | 155.259 | MIT | App desktop (Tauri 2) quản lý nhà cung cấp API cho 12 công cụ lập trình AI (Claude Code, Codex, Gemini CLI, OpenCode…): đổi nhà cung cấp một cú nhấp, quản lý MCP, Skills, Prompts và theo dõi mức dùng. | Hơn 90 preset, chỉ thay endpoint, khóa, model và tự sao lưu cấu hình trước lần ghi đầu; chế độ Routing chuyển đổi định dạng Anthropic/OpenAI/Gemini có failover và circuit breaker; bảng thống kê token, cache, chi phí đọc từ log cục bộ. | `brew install --cask cc-switch` (macOS); bản Windows/Linux ở trang Releases | Cần khóa hoặc tài khoản từng nhà cung cấp; README tự cảnh báo dùng gói thuê bao ngoài client chính thức (tính năng Accounts) có thể trái điều khoản nhà cung cấp. |
| [`Panniantong/Agent-Reach`](https://github.com/Panniantong/Agent-Reach) | 112.815 | MIT | CLI Python cho agent đọc và tìm trên X, Reddit, YouTube, Bilibili, Xiaohongshu, V2EX, LinkedIn, GitHub… bằng một cú pháp `agent-reach <kênh> <hành động>`. | Mỗi hành động có danh sách công cụ chính và dự phòng; chỉ đọc, không đăng, không đăng nhập thay, không hỏi mật khẩu; mọi thứ cài vào `~/.agent-reach/`, gỡ có liệt kê trước. | Nhắn agent cài theo `docs/install.md` (`uv tool install` bản phát hành) | Python 3.10+, uv; nhiều kênh dùng cookie đăng nhập từ Chrome, README khuyên dùng tài khoản phụ; gói `agent-reach` trên PyPI không phải của dự án. |
| [`D4Vinci/Scrapling`](https://github.com/D4Vinci/Scrapling) | 103.979 | BSD-3-Clause | Framework thu thập web Python gộp HTTP nhanh, trình duyệt, parser và crawl đồng thời; dùng từ Python, terminal hoặc agent qua MCP server và Agent Skill. | Spider kiểu Scrapy có pause/resume, AutoThrottle, tùy chọn tuân thủ `robots.txt`; theo dõi phần tử thích ứng khi trang đổi; xuất Markdown sạch cho RAG; kiểu đầy đủ, kiểm bằng PyRight và MyPy. | `pip install "scrapling[fetchers]"` rồi `scrapling install` | Python 3.10+; README nêu chỉ dùng cho giáo dục và nghiên cứu, phải tuân luật dữ liệu, điều khoản website và `robots.txt`. |
| [`TauricResearch/TradingAgents`](https://github.com/TauricResearch/TradingAgents) | 122.976 | Apache-2.0 | Framework nhiều agent trên LangGraph mô phỏng công ty giao dịch: analyst cơ bản, tâm lý, tin tức, kỹ thuật; tranh luận bull/bear; trader, quản trị rủi ro, portfolio manager ra quyết định. | Vai trò tách bạch, analyst chạy song song; nhiều nhà cung cấp LLM, tầng quick/deep chạy được trên nhà cung cấp khác nhau; dữ liệu SEC EDGAR đọc đúng như đã nộp tại ngày chạy để chống look-ahead khi backtest. | `pip install .` rồi `tradingagents` | Python 3.11+, khóa ít nhất một LLM; dự án ghi rõ chỉ phục vụ nghiên cứu, không phải lời khuyên đầu tư. |
| [`cheaper-inference/OmniRoute`](https://github.com/cheaper-inference/OmniRoute) | 88.432 | MIT | Cổng AI tự host, một endpoint tương thích OpenAI (`localhost:20128/v1`) định tuyến Claude Code, Codex, Cursor, Cline tới nhiều nhà cung cấp, có fallback và nén token; có dashboard, CLI, MCP, A2A. | "Combo" định tuyến với 22 chiến lược; ba tầng chịu lỗi gồm circuit breaker; pipeline nén 12 engine; telemetry tắt mặc định, khóa lưu mã hóa AES-256-GCM. | `npm install -g omniroute && omniroute` | Node.js 22/24; tự mang khóa từng nhà cung cấp; nhà cung cấp gắn `tos: avoid` bị loại khỏi định tuyến tự động mặc định. |
| [`mvanhorn/last30days-skill`](https://github.com/mvanhorn/last30days-skill) | 69.159 | MIT | Skill tìm song song thông tin 30 ngày gần nhất về một chủ đề trên Reddit, X, YouTube, Hacker News, Polymarket, GitHub và hơn 25 nguồn, chấm theo tương tác thật rồi tổng hợp có dẫn nguồn. | Reddit, HN, Polymarket, GitHub chạy không cần khóa; chạy cục bộ, không tracking; `--preflight` xem trước sẽ đọc/ghi gì; đầu ra JSON có phiên bản. | `/plugin marketplace add mvanhorn/last30days-skill` rồi `/plugin install last30days` | Python 3.12+; X, TikTok, Instagram… cần khóa hoặc dịch vụ trả theo dùng; đặt khóa rerank thì chủ đề gửi tới nhà cung cấp đó. |
| [`code-yeongyu/oh-my-openagent`](https://github.com/code-yeongyu/oh-my-openagent) | 70.982 | Sustainable Use License 1.0 | Agent lập trình `omo` (trước là plugin oh-my-opencode): nghiên cứu, lập kế hoạch, viết code, tự kiểm chứng tới khi xong, phối hợp model đắt và rẻ. | Từ khóa `ultrawork`/`ulw` làm kỹ từng bước, `mass ulw` chạy đồ thị nhiều agent song song; bộ nhớ "Kibitzer" là markdown trong git; `omo doctor --models` cho biết model nào chạy từng việc. | `curl -fsSL https://get.omo.dev/install.sh \| bash` (npm: `omo-ai`) | Giấy phép chỉ cho dùng nội bộ hoặc phi thương mại; gói npm đúng là `omo-ai`. |
| [`ayghri/i-have-adhd`](https://github.com/ayghri/i-have-adhd) | 61.520 | MIT | Skill bắt trợ lý lập trình trả lời gọn theo 10 luật: hành động kế tiếp lên đầu, bước đánh số, danh sách tối đa 5 mục, ước lượng thời gian cụ thể. | Hướng dẫn cài cho hơn 10 host (Claude Code, Codex, Gemini CLI, Copilot, Cursor…); hook SessionStart tùy chọn để luôn bật; có bộ eval (cases, rubric, kết quả). | `claude plugin marketplace add ayghri/i-have-adhd` rồi `claude plugin install i-have-adhd@i-have-adhd` | Hook luôn bật cần Node.js. |
| [`Imbad0202/academic-research-skills`](https://github.com/Imbad0202/academic-research-skills) | 57.341 | CC-BY-NC-4.0 | Bộ skill Claude Code cho nghiên cứu học thuật: pipeline 10 giai đoạn từ nghiên cứu tài liệu, viết, phản biện tới xuất bản, dừng xin xác nhận ở từng giai đoạn và có cổng liêm chính. | Kiểm trích dẫn qua Semantic Scholar, audit đối chiếu nguồn với từng nhận định (tùy chọn); SR-Screener sàng lọc bằng 2 reviewer AI mù và trọng tài, tính kappa, đếm PRISMA 2020; có `DATA_FLOWS.md` nêu dữ liệu nào rời máy. | `/plugin marketplace add Imbad0202/academic-research-skills` rồi `/plugin install academic-research-skills` | Giấy phép cấm dùng thương mại, bắt buộc ghi nguồn; cần khóa API; người dùng chịu trách nhiệm mọi nhận định nộp đi. |
| [`agno-agi/agno`](https://github.com/agno-agi/agno) | 43.222 | Apache-2.0 | Nền tảng agent tự quản: dựng agent bằng Agno SDK, Claude Agent SDK hoặc Codex SDK, ghép team và workflow, chạy như dịch vụ bền trên AgentOS có REST API, MCP, xác thực, lập lịch và phê duyệt của người. | Module agent, team, workflow, memory, knowledge, guardrails, tracing; AgentOS có durable execution, resume/replay, RBAC, cách ly dữ liệu theo người dùng; template triển khai Docker, AWS, GCP, Azure, Helm. | Nhắn agent clone `agno-agi/agentos-railway` và làm theo skill setup-platform | Cần khóa nhà cung cấp model; tắt telemetry bằng `AGNO_TELEMETRY=false`; template mặc định dùng PostgreSQL. |
| [`musistudio/claude-code-router`](https://github.com/musistudio/claude-code-router) | 38.217 | MIT | Cổng model cục bộ kiêm bảng điều khiển: Claude Code, Codex, Grok CLI, Kimi CLI, OpenCode dùng chung endpoint `127.0.0.1:3456`, còn nhà cung cấp, định tuyến, fallback quản lý một chỗ. | Hỗ trợ OpenAI Chat/Responses, Anthropic Messages, Gemini và endpoint tùy chỉnh; định tuyến theo điều kiện, xoay khóa, fallback; log request, token, độ trễ, chi phí; có app desktop, CLI, Docker. | `npm install -g @musistudio/claude-code-router` rồi `ccr ui` | Node.js 22+; tự có khóa nhà cung cấp; đọc hướng dẫn Docker trước khi mở ra mạng ngoài. |
| [`virgiliojr94/book-to-skill`](https://github.com/virgiliojr94/book-to-skill) | 38.301 | MIT | Biến sách kỹ thuật hoặc thư mục tài liệu (PDF, EPUB, DOCX, MD, HTML…) thành agent skill có cấu trúc: `SKILL.md`, file theo chương, glossary, để agent nạp khi cần. | Trích xuất tất định bằng Python, lùi về stdlib khi thiếu công cụ; mỗi chương một file nạp theo nhu cầu (README đo tốn ít token hơn 24–51 lần); xử lý cục bộ; đẩy lên GitHub mặc định tạo repo private. | `npx skills add virgiliojr94/book-to-skill` | Chỉ dùng tài liệu mình có quyền đọc, skill từ sách có bản quyền giữ private; chỉ cài từ repo chính thức (`SECURITY-NOTICE.md` cảnh báo bản re-upload). |
| [`ComposioHQ/composio`](https://github.com/ComposioHQ/composio) | 31.153 | MIT | SDK TypeScript và Python cùng CLI cho agent dùng hơn 1.000 toolkit đã xác thực sẵn, phiên theo người dùng, có trigger, sandbox và endpoint MCP do Composio host. | Adapter cho OpenAI Agents, Anthropic, Claude Agent SDK, Vercel AI SDK, LangGraph, LlamaIndex, Mastra, CrewAI…; meta tool tìm và chạy tool lúc runtime thay vì nạp hàng trăm định nghĩa; CLI cho coding agent dùng tool từ shell. | `pip install composio` hoặc `npm install @composio/core` | Cần tài khoản và `COMPOSIO_API_KEY`; toolkit chạy qua nền tảng Composio và tài khoản ứng dụng của người dùng cuối. |
| [`gastownhall/beads`](https://github.com/gastownhall/beads) | 28.812 | MIT | `bd` là bộ theo dõi issue dạng đồ thị phân tán cho agent, chạy trên Dolt, thay kế hoạch markdown bằng đồ thị task có phụ thuộc làm bộ nhớ dài hạn. | ID dạng hash tránh xung đột khi nhiều agent làm nhiều nhánh; `bd ready` lấy việc đã hết chặn, `bd update --claim` nhận việc nguyên tử; script cài kiểm checksum, có guard phiên bản schema. | `brew install beads` hoặc `npm install -g @beads/bd`, rồi `bd init` | `bd init` mặc định sửa `AGENTS.md` và cài tích hợp agent, trừ khi dùng `--skip-agents` hoặc `--stealth`. |
| [`openai/symphony`](https://github.com/openai/symphony) | 28.077 | Apache-2.0 | Biến issue trên tracker (Linear, GitHub Issues, Jira, Asana, GitLab) thành các lượt triển khai cô lập: mỗi issue một workspace, chạy Codex App Server tới khi xong; gồm đặc tả `SPEC.md` và bản tham chiếu Elixir. | `SPEC.md` đủ để tự cài bằng ngôn ngữ khác; issue kết thúc thì tự dừng agent và dọn workspace; token tracker bị gỡ khỏi môi trường tiến trình Codex con; việc cần người duyệt được đánh dấu blocked. | Theo `elixir/README.md`: `mise install`, `mix setup`, `./bin/symphony ./WORKFLOW.md` | Dự án ghi là bản xem trước kỹ thuật, chỉ thử trong môi trường tin cậy; cần Codex CLI và khóa tracker. |
| [`phuryn/pm-skills`](https://github.com/phuryn/pm-skills) | 28.113 | MIT | Marketplace plugin quản lý sản phẩm: 72 skill và 42 command chia 9 plugin (discovery, strategy, execution, go-to-market, growth, analytics…), mỗi skill mã hóa một khung PM (Teresa Torres, Marty Cagan, Alberto Savoia). | Command nối chuỗi skill, ví dụ `/discover` từ brainstorm tới thử nghiệm; cài được trên Claude Code và Codex; có `tests/` và `validate_plugins.py`. | `claude plugin marketplace add phuryn/pm-skills` rồi `claude plugin install pm-toolkit@pm-skills` | Command chỉ chạy trên Claude Code/Cowork, công cụ khác dùng skill; plugin `pm-ai-shipping` đã chuyển sang `phuryn/product-engineering`. |
| [`walkinglabs/learn-harness-engineering`](https://github.com/walkinglabs/learn-harness-engineering) | 25.317 | MIT | Khóa học theo dự án về harness engineering: môi trường, quản lý trạng thái, xác minh, cơ chế kiểm soát để coding agent chạy tin cậy; 14 bài giảng, 8 dự án, phân tích harness của Claude Code, Codex, Pi, DeepSeek. | Tài liệu 15 ngôn ngữ, có tiếng Việt (`docs/vi`); skill `harness-creator` kèm template `AGENTS.md`, `feature-list.json`, `progress.md` và 10 ca eval; `tools/audit-harness.sh` kiểm repo theo 5 phân hệ, không cần Node.js. | `bash tools/audit-harness.sh /path/to/repo` | Làm dự án cần một coding agent có quyền sửa file và chạy lệnh. |
| [`browser-use/browser-harness`](https://github.com/browser-use/browser-harness) | 19.133 | MIT | Cho Claude Code, Codex, Cursor điều khiển Chrome thật của người dùng qua CDP với phiên đã đăng nhập; agent tự viết helper còn thiếu nên harness tốt dần; nay là engine bên trong CLI browser-use. | Lõi giữ cố định, agent chỉ ghi `agent_helpers.py`; 18 interaction-skill (iframe, shadow DOM, upload, download, dialog…); có MCP server; tác giả đo trên 100 tác vụ BU Bench: token đầu vào trung vị và chi phí thấp nhất. | `uv tool install browser-use && browser-use skill install` | Chrome 144+ và bật "Allow remote debugging"; agent điều khiển cả trình duyệt với phiên của bạn; ghi hình mặc định tắt. |
| [`mindfold-ai/Trellis`](https://github.com/mindfold-ai/Trellis) | 15.152 | AGPL-3.0 | Khung kỹ thuật lưu spec, task, bộ nhớ vào `.trellis/` trong repo để mọi coding agent làm theo chuẩn dự án qua nhiều phiên, vòng Plan → Implement → Verify → Finish. | Spec tự chèn vào ngữ cảnh mỗi phiên; sub-agent research, implement, check (lint, type, test, tự sửa) và update-spec đưa bài học trở lại spec; `trellis ablate` tạm gỡ để so có và không có Trellis. | `npm install -g @mindfoldhq/trellis@latest` rồi `trellis init -u <tên>` | Node.js 18+, Python 3.9+; AGPL-3.0: cung cấp bản sửa đổi qua mạng thì phải công bố mã. |
| [`tt-a1i/archify`](https://github.com/tt-a1i/archify) | 97.508 | Apache-2.0 | Skill biến mô tả, câu hỏi hoặc repo thành một file HTML tương tác tự chứa: sơ đồ kiến trúc, workflow, ERD, timeline, waterfall hoặc trang giải thích. | Mỗi chế độ có JSON IR có schema; validator kiểm schema, layout, HTML/SVG, khoảng cách nhãn trước khi giao, lỗi trả mã luật và cách sửa; node sơ đồ dẫn chứng file và dòng ghim theo commit; xuất PNG/PDF, theme sáng/tối, nhiều ngôn ngữ. | `npx -y skills@latest add https://archify.si --skill archify` | Node.js 18+; mã trước một commit mốc vẫn theo MIT (ghi trong `NOTICE`); kênh chính thức chỉ có archify.si và GitHub. |
| [`hugohe3/ppt-master`](https://github.com/hugohe3/ppt-master) | 77.973 | MIT | Quy trình cho agent tạo file PowerPoint sửa được từ PDF, DOCX, trang web hoặc văn bản: phân tích, thiết kế từng trang, xuất PPTX cục bộ; chiết template từ mẫu, điền vào .pptx có sẵn, thêm chuyển cảnh và thuyết minh. | Xuất shape native và slide master thật, chart/table có Edit Data; công thức thành OMML sửa được; chế độ sửa .pptx giữ nguyên các trang không đổi; tìm ảnh web và tự chèn credit. | `git clone` rồi `pip install -r requirements.txt` | Python 3.10–3.14; tốn nhiều token, nên dùng model ngữ cảnh dài; sinh ảnh cần khóa nhà cung cấp. |
| [`google/skills`](https://github.com/google/skills) | 24.400 | Apache-2.0 | Bộ Agent Skills chính thức của Google, chủ yếu Google Cloud (GKE, Compute Engine, Cloud Storage, BigQuery, Gemini, IAM…) cùng Ads, Analytics, Identity; kèm plugin Skill + MCP. | 207 `SKILL.md` theo nhóm; `index.json` sinh tự động; mỗi skill ghi khi nào dùng và khi nào không; plugin cho Claude Code, Codex, Antigravity; cập nhật bằng `npx skills update`. | `npx skills add google/skills` | Phần lớn skill cần dự án GCP, gcloud và quyền IAM; nhiều skill gắn tag `agent-skills/1.0` vào User-Agent khi chạy lệnh gcloud (bỏ được nếu yêu cầu). |
| [`GoogleChrome/modern-web-guidance`](https://github.com/GoogleChrome/modern-web-guidance) | 22.163 | Apache-2.0 | Bộ skill đưa kiến thức nền tảng web hiện đại, thực hành tốt và dữ liệu Baseline vào coding agent; agent gọi CLI để lấy guide phù hợp. Đội Chrome, Edge, Firefox và MDN cùng quản lý. | 262 tính năng web, guide chia css, forms, performance, accessibility, security, pwa…; tìm kiếm cục bộ offline (embedding + BM25), không cần khóa; chặn guide Origin Trial trừ khi bật; lệnh `legacy-scan` tìm mẫu cũ trong codebase. | `npx modern-web-guidance@latest install` | CLI gửi telemetry ẩn danh (lượt cài, tên agent, ID guide, truy vấn), tắt bằng `DISABLE_TELEMETRY=1`. |

### 6c.4 Nhóm AI Agent & MCP: so sánh, chọn 16 repo đọc mã (18/11/2026)

Nhóm có 32 repo. Bốn repo đã đọc ở §6c.2 (autoresearch, Agno, Composio, Symphony); `aaif-goose/goose` là `block/goose` đã có hồ sơ ở mục 01. Còn 27 repo được đọc mã và so với các repo cùng loại trong kho, chỉ thêm repo còn bảo trì (commit trong 6 tháng), giấy phép rõ, có giá trị riêng và tính năng kiểm được trong mã.

| Repo | ★ (18/11/2026) | Giấy phép | Làm gì | Điểm mạnh (đọc mã) | Cài | Điều kiện dùng |
|---|---|---|---|---|---|---|
| [`zhayujie/CowAgent`](https://github.com/zhayujie/CowAgent) | 47.982 | MIT | Agent cá nhân (tên cũ chatgpt-on-wechat) tự lập kế hoạch, dùng công cụ, skill, MCP, có bộ nhớ dài hạn và kho tri thức. | Kênh có sẵn: Web, WeChat, Feishu, DingTalk, WeCom, QQ, Telegram, Slack, Discord; bộ nhớ ba tầng truy hồi lai từ khóa và vector; đổi nhà cung cấp model ngay trên web console. | `bash <(curl -fsSL https://cdn.link-ai.tech/code/cow/run.sh)` | Cần khóa LLM; chế độ Agent có quyền hệ điều hành nên chỉ chạy ở môi trường tin cậy, đặt `web_password` khi mở ra ngoài. |
| [`tinyhumansai/openhuman`](https://github.com/tinyhumansai/openhuman) | 42.740 | GPL-3.0 | Agent harness bằng Rust vừa là app desktop, terminal, server vừa là thư viện nhúng agent vào sản phẩm. | Nhúng được qua crate `openhuman-embed`; nén token theo Recursive Language Models, benchmark SWE-bench công khai; approval gate, sandbox (OS jail hoặc Docker), bí mật lưu trong keyring. | `curl -fsSL https://raw.githubusercontent.com/tinyhumansai/openhuman/main/scripts/install.sh` rồi chạy bằng bash | Dự án tự ghi early beta; BYOK 26 nhà cung cấp hoặc model cục bộ; GPL-3.0. |
| [`ashishpatel26/500-AI-Agents-Projects`](https://github.com/ashishpatel26/500-AI-Agents-Projects) | 40.062 | MIT | Bộ sưu tập hơn 500 dự án và ca dùng agent theo ngành và framework (LangGraph, CrewAI, AutoGen, Agno, LlamaIndex). | 21 agent mẫu chạy được trong `agents/`, mỗi cái có `agent.py`, `requirements.txt`, `metadata.yaml`; bảng so sánh framework; khóa CrewAI + MCP 3 bài. | `cd agents/01-web-research-agent && pip install -r requirements.txt` | Agent mẫu cần khóa API; dự án ngoài được liệt kê theo giấy phép riêng. |
| [`agentscope-ai/QwenPaw`](https://github.com/agentscope-ai/QwenPaw) | 37.892 | Apache-2.0 | Trợ lý cá nhân chạy cục bộ hoặc cloud, mở rộng bằng skill và plugin, nối nhiều kênh nhắn tin; có console web, TUI, app desktop. | Bộ nhớ ba lớp lưu Markdown; runtime QwenPaw Local và model QwenPaw-Flash chạy không cần khóa, cùng Ollama, LM Studio và 14+ nhà cung cấp; sandbox mức kernel, Tool Guard, File Guard, Skill Scanner. | `pip install qwenpaw && qwenpaw init --defaults && qwenpaw app` | Python 3.11–3.13; LLM cloud cần khóa. |
| [`assafelovic/gpt-researcher`](https://github.com/assafelovic/gpt-researcher) | 30.761 | Apache-2.0 | Agent nghiên cứu sâu tạo báo cáo chi tiết có trích dẫn từ web và tài liệu cục bộ, agent lập kế hoạch và agent thực thi chạy song song. | Chế độ deep research đệ quy và luồng nhiều agent; nhiều nguồn tìm (Tavily, Brave, Exa, arXiv, PubMed Central, Semantic Scholar, SearxNG, MCP…); xuất PDF, Word; dùng như gói pip. | `pip install gpt-researcher` | Mặc định cần OpenAI và Tavily (đổi được sang API tương thích). |
| [`milind-soni/OpenMausBot`](https://github.com/milind-soni/OpenMausBot) | 24.862 | Apache-2.0 (trừ thư mục enterprise/) | App chat nơi mỗi bot là một agent thật chạy CLI claude, codex hoặc grok trên máy bạn, có tính cách, model và ứng dụng kết nối riêng. | Local-first: harness server trên 127.0.0.1 quản lý tiến trình, dữ liệu ở `~/.openmausbot`; dùng lại đăng nhập CLI sẵn có, không proxy trung gian; app cho macOS, Windows, Ubuntu và gói npm cho server. | `npm install -g openmausbot && openmausbot` | Node 24+, ít nhất một CLI agent đã đăng nhập; thư mục `enterprise/` chạy production cần license key. |
| [`NVIDIA/NemoClaw`](https://github.com/NVIDIA/NemoClaw) | 23.053 | Apache-2.0 | Bộ tham chiếu của NVIDIA chạy agent (OpenClaw, Hermes, LangChain Deep Agents) trong sandbox NVIDIA OpenShell, kèm CLI quản lý vòng đời. | Onboarding có hướng dẫn, managed inference, chính sách mạng kiểm soát egress, lưu trạng thái qua OpenShell; blueprint khai báo policies và provider profiles. | Theo `docs/get-started` (script cài nemoclaw.sh của NVIDIA) | Alpha; cần NVIDIA OpenShell và nền tảng hỗ trợ (DGX, WSL…). |
| [`camel-ai/owl`](https://github.com/camel-ai/owl) | 20.198 | Apache-2.0 (khai trong pyproject) | Khung nhiều agent OWL (Optimized Workforce Learning) trên CAMEL-AI tự động hóa tác vụ thực tế bằng agent cộng tác có công cụ tìm, trình duyệt, đa phương tiện. | README ghi điểm GAIA trung bình 69,09, hạng 1 trong khung mã nguồn mở; MCPToolkit và nhiều toolkit (Playwright, tìm kiếm, chạy code, Excel, GitHub); ví dụ cho Claude, Qwen, DeepSeek, OpenAI. | `uv pip install -e .` | Cần khóa model có tool calling mạnh; Python 3.10–3.12. |
| [`elizaOS/eliza`](https://github.com/elizaOS/eliza) | 19.901 | MIT | Khung TypeScript và bộ sản phẩm cho agent tự trị: runtime lõi, app, CLI, cloud, plugin chính chủ. | Không phụ thuộc model, mở rộng qua plugin (81 mục: nhắn tin, trình duyệt, ví EVM/Solana có ranh giới phê duyệt); kiểm mô hình trạng thái bằng Quint và helper xác minh bằng Dafny. | `bun install && bun run dev` | Bun 1.4.2; benchmark trực tiếp cần khóa nhà cung cấp. |
| [`microsoft/agent-lightning`](https://github.com/microsoft/agent-lightning) | 18.973 | MIT | Khung học tăng cường gọn (~3.500 dòng) huấn luyện agent với harness thật; v1.0 viết lại hoàn toàn. | Ba thành phần Trainer (verl + vLLM), API Gateway thu dữ liệu, Rollout Controller; agent chạy qua proxy không cần sửa mã, chạy được như Kubernetes Job; ví dụ huấn luyện coding agent nâng SWE-bench Verified từ 41,8% lên 56,4% với Qwen3.5-9B. | `uv sync && bash scripts/setup_verl.sh 0.8.0 cu130` | Cần GPU CUDA và stack verl. |
| [`gastownhall/gastown`](https://github.com/gastownhall/gastown) | 18.828 | MIT | Trình quản lý workspace điều phối nhiều agent lập trình (Claude Code, Copilot, Codex, Gemini) với trạng thái công việc bền trong git worktree. | Trạng thái lưu trong Beads; Refinery là hàng đợi merge kiểu Bors có chia đôi để cô lập thay đổi lỗi; giám sát ba tầng Witness, Deacon, Dogs phát hiện agent bị kẹt. | `brew install gastown` | Git 2.20+, Go 1.26.2+, Beads, Dolt, tmux 3.0+ và CLI agent. |
| [`emcie-co/parlant`](https://github.com/emcie-co/parlant) | 18.334 | Apache-2.0 | Nền tảng mở dựng agent chăm sóc khách hàng, vận hành từ coding agent, kèm chat widget, chuyển giao người, kiểm thử, phân tích. | Policy giữ agent đúng chính sách và tự kiểm trước khi trả lời; tự mang model, không cộng phí suy luận; Dashboard CLI cho coding agent. | `pip install parlant` | Mặc định cần khóa OpenRouter; Dashboard host thu phí theo workspace, framework miễn phí. |
| [`rowboatlabs/rowboat`](https://github.com/rowboatlabs/rowboat) | 18.291 | Apache-2.0 | Nhóm chat nơi người và nhiều agent (Claude Code, Codex, Hermes…) cộng tác, kèm app desktop dựng đồ thị tri thức từ email, họp, Slack. | Mỗi tổ chức có MCP server tại `/mcp` với OAuth 2.1, mọi hành động ghi cho thành viên; server Harbor tự host trên Postgres; agent tạo agent mới phải được người duyệt. | `claude mcp add --transport http my-team https://<org>/mcp` | Tự host cần Postgres, tên miền, OIDC; giao thức còn v0. |
| [`googleapis/mcp-toolbox`](https://github.com/googleapis/mcp-toolbox) | 16.897 | Apache-2.0 | MCP server (tên cũ genai-toolbox) nối agent, IDE, ứng dụng với cơ sở dữ liệu doanh nghiệp, có công cụ dựng sẵn và khung tự định nghĩa qua `tools.yaml`. | `--prebuilt=<db>` cho AlloyDB, BigQuery, Cloud SQL, Spanner, PostgreSQL, MySQL, MongoDB, Snowflake… (57 nguồn); connection pooling, IAM, OpenTelemetry; SDK Python, JS/TS, Go, Java; theo SemVer (1.17.0). | `npx -y @toolbox-sdk/server --prebuilt=postgres --stdio` | Cần thông tin kết nối cơ sở dữ liệu; nguồn GCP cần tài khoản. |
| [`eigent-ai/eigent`](https://github.com/eigent-ai/eigent) | 15.843 | Apache-2.0 | App desktop Cowork dựng và chạy đội agent (một hoặc nhiều agent) tự động hóa quy trình, trên CAMEL-AI. | Nhiều agent song song hoặc một meta agent; model cục bộ (vLLM, Ollama, LM Studio) và tự host backend; MCP, skill, toolkit trình duyệt và terminal, lập lịch định kỳ. | `npm install && npm run dev` | Quick Start cần tài khoản cloud Eigent; tự host theo `server/README_EN.md`; Node 18–22. |
| [`microsoft/RD-Agent`](https://github.com/microsoft/RD-Agent) | 15.412 | MIT | Khung agent tự động hóa R&D dữ liệu (đề xuất ý tưởng và hiện thực) cho quant tài chính, khai phá dữ liệu, đọc báo cáo, Kaggle, tinh chỉnh LLM. | CLI nhiều kịch bản (`fin_quant`, `fin_factor`, `data_science`, `kaggle`…); LiteLLM cho nhiều nhà cung cấp; UI Streamlit và Web UI theo dõi. | `pip install rdagent` | Chỉ Linux, Docker chạy không sudo; không dùng cho tư vấn tài chính; Web UI chạy code sinh ra nên cần môi trường cô lập. |

**Chưa thêm (11 repo, giữ trong file dữ liệu):** `microsoft/JARVIS` (commit cuối 29/7/2025); `TransformerOptimus/SuperAGI` (commit cuối 22/1/2025); `google-gemini/gemini-fullstack-langgraph-quickstart` (commit cuối 18/6/2025); `Alibaba-NLP/DeepResearch` (commit cuối 27/2/2026); `QwenLM/Qwen-Agent` (commit cuối 4/3/2026); `cft0808/edict` (commit cuối 6/5/2026); `RightNow-AI/openfang` (commit cuối 12/5/2026, trước 1.0); `dzhng/deep-research` (commit cuối 11/4/2026; gpt-researcher phủ cùng việc); `openai/swarm` (dự án ghi đã được OpenAI Agents SDK thay thế); `leon-ai/leon` (Leon 2.0 chưa phát hành); `Fosowl/agenticSeek` (tác giả ghi là dự án phụ, không lộ trình).

**Chọn theo việc:** nền tảng agent dịch vụ: Agno (§6c.2), elizaOS, Parlant (chăm sóc khách hàng); điều phối nhiều coding agent: Gas Town, Rowboat, OpenMausBot, Eigent; trợ lý cá nhân: CowAgent (kênh nhắn tin Trung Quốc), QwenPaw (chạy cục bộ không khóa), openhuman (nhúng như thư viện Rust); nghiên cứu: gpt-researcher, RD-Agent; an toàn khi chạy agent: NemoClaw; huấn luyện agent: agent-lightning; nối cơ sở dữ liệu: MCP Toolbox; học: 500-AI-Agents-Projects.

### 6c.5 Lọc lại toàn bộ kho: đọc mã 437 repo, giữ 410 repo (18/11/2026)

Áp cùng tiêu chí cho cả 694 repo: còn bảo trì (commit trong 6 tháng, từ 18/5/2026), không tự nêu ngừng hay thay thế, giấy phép rõ, có giá trị riêng so với repo cùng loại trong kho, tính năng kiểm được trong mã. Lọc máy bằng GitHub API loại trước các repo commit cũ, không có giấy phép, archive hoặc ngoài phạm vi kho. Còn 437 repo được clone nông, đọc README, LICENSE và cây thư mục; giữ 410 repo, không thêm 27 repo (lý do ghi cạnh từng repo). Trường `review` trong `data/collections/phandonggiang-kho-repo.json` ghi kết luận cho từng repo trong 694 repo. Giấy phép hạn chế (phi thương mại, Sustainable Use, Business Source, Elastic License, source-available) được ghi ở cột giấy phép, catalog đặt `open_source: false`.

#### 6c.5.1 AI Ảnh, Giọng nói & Deepfake

Đọc mã 19 repo, giữ 16.

| Repo | ★ (18/11/2026) | Giấy phép | Làm gì | Điểm mạnh (đọc mã) | Cài | Điều kiện dùng |
|---|---|---|---|---|---|---|
| [`RVC-Project/Retrieval-based-Voice-Conversion-WebUI`](https://github.com/RVC-Project/Retrieval-based-Voice-Conversion-WebUI) | 39.314 | MIT (kèm file MIT协议暨相关引用库协议: người dùng và người phát tán âm thanh xuất ra tự chịu toàn bộ trách nhiệm; liệt kê giấy phép thư viện tham chiếu) | Khung chuyển đổi giọng nói (đổi giọng) dựa trên VITS với cơ chế truy xuất đặc trưng top1, có WebUI huấn luyện/suy luận và giao diện đổi giọng thời gian thực. | Dùng truy xuất top1 thay đặc trưng nguồn bằng đặc trưng tập huấn luyện để hạn chế rò rỉ âm sắc; tích hợp thuật toán trích cao độ RMVPE và tách giọng/nhạc nền qua pymss/MSST; đổi giọng thời gian thực đạt độ trễ đầu-cuối 170ms (90ms với ASIO) theo README. | `python -m pip install -r requirments_cpu_py312.txt (hoặc bản cu118/cu128) rồi python webui.py` | Cần Python 3.12 x64; tải model từ Hugging Face lj1995/VoiceConversionWebUI; người dùng tự chịu trách nhiệm về âm thanh tạo ra (điều khoản kèm giấy phép). |
| [`freestylefly/awesome-gpt-image-2`](https://github.com/freestylefly/awesome-gpt-image-2) | 35.915 | MIT | Thư viện prompt có cấu trúc cho GPT-Image2 với hơn 500 ví dụ và các mẫu prompt theo nhóm (UI, infographic, poster, sản phẩm…), kèm website trưng bày và agent skill chọn phong cách. | 544 ví dụ chia theo danh mục trong docs/gallery.md cùng dữ liệu data/cases.json; có agent skill gpt-image-2-style-library phát hành trên npm, cài được cho Claude Code và Codex; README có bản tiếng Anh, tiếng Trung giản thể và tiếng Nhật. | `npx skills add freestylefly/awesome-gpt-image-2 --skill gpt-image-2-style-library` | Nội dung lấy từ cộng đồng công khai (YouMind, OpenNana); docs/disclaimer.md nói không bảo đảm dùng thương mại, cần xin phép chủ quyền gốc; sinh ảnh trên website cần đăng nhập Google hoặc khoá APIMart; tự host website cần Supabase, Stripe và khoá APIMart. |
| [`huggingface/diffusers`](https://github.com/huggingface/diffusers) | 34.936 | Apache License 2.0 | Thư viện Python của Hugging Face cho các mô hình khuếch tán (diffusion) tiền huấn luyện để sinh ảnh, âm thanh và cấu trúc 3D phân tử, dùng cho cả suy luận lẫn huấn luyện. | Ba thành phần cốt lõi có thể ghép: pipeline, scheduler nhiễu và model; có 94 mục trong src/diffusers/pipelines; tải hàng chục nghìn checkpoint từ Hub chỉ bằng from_pretrained. | `pip install --upgrade diffusers[torch]` | Mỗi checkpoint trên Hub có giấy phép riêng (chưa xác minh từng model); cần PyTorch, GPU để chạy nhanh. |
| [`invoke-ai/InvokeAI`](https://github.com/invoke-ai/InvokeAI) | 29.111 | Apache License 2.0 (kèm file giấy phép riêng cho trọng số: CreativeML Open RAIL-M cho SD1/SD2, CreativeML Open RAIL++-M cho SDXL, cùng LICENSE-HiDiffusion và LICENSE-PiD) | Công cụ sáng tạo hình ảnh bằng AI tự host, chạy web server cục bộ với giao diện React, có Unified Canvas, workflow dạng node và quản lý gallery. | Hỗ trợ nhiều họ mô hình như SD 1.5, SDXL, SD 3.5, Flux.1, Flux.2, Qwen Image, Z-Image; Unified Canvas tích hợp in-painting/out-painting và công cụ cọ; workflow dạng node có thể chia sẻ, kèm phân đoạn đối tượng SAM/SAM2. | `Tải Invoke Launcher tại https://github.com/invoke-ai/launcher/releases/latest` | Cần phần cứng tương thích (GPU); một số mô hình chỉ qua API (Nano Banana, GPT Image, Wan) cần tài khoản/khoá dịch vụ ngoài; trọng số mô hình theo giấy phép RAIL riêng có hạn chế sử dụng. |
| [`deezer/spleeter`](https://github.com/deezer/spleeter) | 28.537 | MIT | Thư viện tách nguồn âm thanh của Deezer viết bằng Python/TensorFlow, có mô hình tiền huấn luyện tách giọng hát, trống, bass, piano và phần còn lại. | Có mô hình sẵn 2, 4 và 5 stems; dùng được cả qua dòng lệnh lẫn làm thư viện Python, có Docker; được dùng trong phần mềm âm thanh chuyên nghiệp như iZotope RX 8, SpectraLayers 7, VirtualDJ. | `pip install spleeter rồi spleeter separate -p spleeter:2stems -o output audio_example.mp3` | Cần ffmpeg và libsndfile; README ghi có vấn đề đã biết trên Apple M1 do TensorFlow; có bản thương mại Spleeter Pro riêng. |
| [`index-tts/index-tts`](https://github.com/index-tts/index-tts) | 25.165 | bilibili Model Use License Agreement (không phải giấy phép OSI: cần giấy phép riêng nếu trên 100 triệu MAU hoặc doanh thu năm trên 1 tỷ NDT; cấm dùng để cải thiện mô hình AI khác trừ mô hình phi thương mại; cấm dùng rủi ro cao) | Hệ thống chuyển văn bản thành giọng nói zero-shot nhân bản giọng từ một đoạn âm thanh tham chiếu, bản mới nhất IndexTTS-2.5 hỗ trợ tiếng Trung, Anh, Nhật, Tây Ban Nha, Ả Rập. | Điều khiển cảm xúc, tốc độ nói (duration_factor 0.5x–2.0x) và phát âm (Pinyin, phoneme CMU, Kana); hỗ trợ triển khai production qua vLLM; có WebUI và công cụ kiểm tra GPU tools/gpu_check.py. | `uv sync --all-extras rồi hf download IndexTeam/IndexTTS-2.5 --local-dir=checkpoints rồi uv run webui.py` | File DISCLAIMER cấm tổng hợp giọng chính trị gia, người nổi tiếng hoặc cá nhân khi chưa được phép, cấm lừa đảo, giả mạo, dùng thương mại giọng tổng hợp khi chưa được phép; dùng thương mại liên hệ indexspeech@bilibili.com; cần CUDA 12.8 trở lên khi dùng GPU NVIDIA. |
| [`QwenAudio/CosyVoice`](https://github.com/QwenAudio/CosyVoice) | 24.435 | Apache License 2.0 | Hệ thống chuyển văn bản thành giọng nói dựa trên mô hình ngôn ngữ lớn (Fun-CosyVoice 3.0, CosyVoice 2.0/1.0), hỗ trợ nhân bản giọng zero-shot, đa ngôn ngữ và phương ngữ. | Phủ 9 ngôn ngữ phổ biến và hơn 18 phương ngữ tiếng Trung; streaming hai chiều với độ trễ thấp tới 150ms; hỗ trợ suy luận vLLM, runtime Triton TensorRT-LLM và có script huấn luyện trong examples/libritts. | `pip install -r requirements.txt (môi trường conda python 3.10) rồi python example.py` | README hướng dẫn clone từ FunAudioLLM/CosyVoice (HEAD trùng commit với repo này); phần Disclaimer nói nội dung chỉ cho mục đích học thuật, một số ví dụ lấy từ internet; giấy phép từng trọng số model chưa xác minh. |
| [`PicoTrex/Awesome-Nano-Banana-images`](https://github.com/PicoTrex/Awesome-Nano-Banana-images) | 24.080 | Apache-2.0 (file LICENSE); badge README lại ghi CC BY 4.0 — không nhất quán | Thư viện tuyển chọn ảnh do Nano-banana/Nano-banana-pro của Google tạo kèm prompt theo từng tình huống sử dụng. | README có 6 bản ngôn ngữ (Trung, Anh, Nhật, Hàn, Tây Ban Nha, Thổ Nhĩ Kỳ); mỗi ví dụ ghi tác giả nguồn; đã phát hành bộ dữ liệu Nano-consistent-150k trên Hugging Face |  | Ảnh/prompt lấy từ Twitter/X, Xiaohongshu — bản quyền thuộc tác giả gốc; cần dịch vụ Nano-banana của Google để tái tạo |
| [`chidiwilliams/buzz`](https://github.com/chidiwilliams/buzz) | 22.883 | MIT | Ứng dụng máy tính để bàn chép lời và dịch âm thanh ngoại tuyến bằng Whisper của OpenAI. | Hỗ trợ nhiều backend Whisper với CUDA, Apple Silicon và Vulkan qua whisper.cpp; xuất TXT, SRT, VTT và có CLI; có bản Flatpak, Snap, PyPI và bộ cài macOS/Windows | `pip install buzz-captions && python -m buzz` | Bản Windows không ký số (cảnh báo khi cài); PyPI cần ffmpeg và Python 3.12 |
| [`w-okada/voice-changer`](https://github.com/w-okada/voice-changer) | 21.406 | MIT; kèm LICENSE-CLA (thỏa thuận người đóng góp) và LICENSE-NOTICE (vocoder DiffSinger, Beatrice có giấy phép riêng) | VCClient: phần mềm đổi giọng thời gian thực bằng AI, hỗ trợ RVC và Beatrice v2. | Chạy độc lập trên PC hoặc qua mạng để giảm tải máy chơi game; có REST API; hỗ trợ Windows, Mac M1, Linux và Google Colab |  | Model Beatrice có giấy phép độc quyền riêng; giọng Tsukuyomi-chan/Amitaro có điều khoản cấm dùng để công kích, tuyên truyền chính trị, phải ghi rõ là giọng chuyển đổi; bản Mac không ký số |
| [`modelscope/FunASR`](https://github.com/modelscope/FunASR) | 21.062 | MIT cho mã; model theo MODEL_LICENSE (FunASR Model Open Source License v1.1 của Alibaba Group: bắt buộc ghi nguồn và giữ tên model, chấm dứt quyền nếu vi phạm) | Bộ công cụ nhận dạng tiếng nói công nghiệp cho triển khai offline, streaming và edge, gồm ASR, VAD, dấu câu, người nói. | Có model Fun-ASR-Nano và bản MLT-Nano 31 ngôn ngữ; SenseVoiceSmall chạy CPU kèm nhận diện cảm xúc và sự kiện âm thanh; có phục vụ tương thích OpenAI | `pip install torch torchaudio && pip install funasr` | Model chịu điều khoản MODEL_LICENSE (ghi nguồn, cấm bôi nhọ phần mềm); GPU cần PyTorch khớp driver NVIDIA |
| [`DrewThomasson/ebook2audiobook`](https://github.com/DrewThomasson/ebook2audiobook) | 20.578 | Apache-2.0 | Chuyển sách điện tử thành sách nói có chương và metadata bằng nhiều engine TTS, hỗ trợ nhân bản giọng. | Hỗ trợ hàng chục engine TTS (XTTSv2, Piper, Kokoro, F5-TTS…) và 1696 ngôn ngữ; chạy tối thiểu 2 GB RAM / 1 GB VRAM; có GUI web, chế độ headless, Docker và gói pip | `pip install ebook2audiobook` | Chỉ dùng cho ebook không DRM, có được hợp pháp; nhân bản giọng cần tôn trọng quyền giọng nói; giấy phép từng model TTS riêng (chưa xác minh) |
| [`NVIDIA-NeMo/Speech`](https://github.com/NVIDIA-NeMo/Speech) | 18.763 | Apache-2.0 (kèm THIRD-PARTY-NOTICES) | NeMo Speech của NVIDIA: bộ công cụ huấn luyện và suy luận ASR, TTS, speech LLM (tách từ NeMo). | Bản v3.0.0 và container NGC 26.07.00; model Nemotron-3.5-ASR-Streaming 40 ngôn ngữ, MagpieTTS đa ngôn ngữ; cài tái lập bằng uv.lock | `git clone https://github.com/NVIDIA-NeMo/Speech.git && cd Speech && uv sync --extra all --extra cu13` | Stack hỗ trợ cần GPU NVIDIA với CUDA 12/13; giấy phép checkpoint trên Hugging Face riêng (chưa xác minh) |
| [`apple-aiml-research/ml-stable-diffusion`](https://github.com/apple-aiml-research/ml-stable-diffusion) | 17.959 | MIT (Copyright 2024 Apple Inc.) | Chạy Stable Diffusion trên Apple Silicon bằng Core ML: gói Python chuyển model PyTorch sang Core ML và gói Swift tích hợp vào app. | Có bảng benchmark trên iPhone/iPad/Mac; hỗ trợ nén trọng số (palettization, lượng tử hoá) qua coremltools; có Swift package cho Xcode | `pip install -e .` | Cần macOS 13.1+/iOS 16.2+, chip M1/A14 trở lên; phải chấp nhận Terms of Use của model Stable Diffusion trên Hugging Face |
| [`k2-fsa/sherpa-onnx`](https://github.com/k2-fsa/sherpa-onnx) | 16.011 | Apache-2.0 | Thư viện xử lý tiếng nói chạy cục bộ bằng ONNX Runtime: ASR streaming/không streaming, TTS, VAD, phân tách người nói, keyword spotting. | Hỗ trợ Android, iOS, Windows, macOS, Linux, HarmonyOS trên x64/arm/riscv64 và WebAssembly; binding 12 ngôn ngữ lập trình (C++, Python, Java, Go, Rust, Dart…); có app demo Flutter và Tauri |  |  |
| [`alphacep/vosk-api`](https://github.com/alphacep/vosk-api) | 15.272 | Apache-2.0 (file COPYING) | Bộ công cụ nhận dạng tiếng nói ngoại tuyến mã nguồn mở cho hơn 20 ngôn ngữ, có API streaming. | Model nhỏ khoảng 50 MB với từ vựng lớn; binding Python, Java, Node.js, C#, Rust, Go và các ngôn ngữ khác; chạy từ Raspberry Pi, Android đến cụm máy chủ |  |  |

**Chưa thêm (3 repo, giữ trong file dữ liệu):** `hacksider/Deep-Live-Cam` (công cụ hoán đổi khuôn mặt (deepfake), rủi ro dùng sai với người thật); `deepfakes/faceswap` (công cụ hoán đổi khuôn mặt (deepfake), rủi ro dùng sai với người thật); `Anjok07/ultimatevocalremovergui` (không có file LICENSE).

#### 6c.5.2 API & Dịch vụ dữ liệu

Đọc mã 5 repo, giữ 5.

| Repo | ★ (18/11/2026) | Giấy phép | Làm gì | Điểm mạnh (đọc mã) | Cài | Điều kiện dùng |
|---|---|---|---|---|---|---|
| [`public-apis/public-apis`](https://github.com/public-apis/public-apis) | 499.885 | MIT | Danh sách tuyển chọn các API công khai miễn phí theo hơn 60 chủ đề, do cộng đồng và APILayer duy trì. | Hơn 60 nhóm chủ đề trong mục lục; mỗi API ghi kiểu xác thực, HTTPS và CORS; có mục MCP connector |  | README chứa quảng cáo APILayer (dịch vụ trả phí); mỗi API có điều khoản và khoá riêng |
| [`axios/axios`](https://github.com/axios/axios) | 109.516 | MIT (Copyright (c) 2014-present Matt Zabriskie & Collaborators) | Thư viện HTTP client dựa trên Promise cho trình duyệt và Node.js. | Hỗ trợ interceptor request/response, huỷ request và tự chuyển đổi JSON, multipart/form-data; Chạy cả trình duyệt (XMLHttpRequest) lẫn Node.js (module http), có mục hỗ trợ HTTP/2 trong README; Có file định nghĩa kiểu TypeScript (index.d.ts, index.d.cts), bản package.json hiện tại 1.21.1 | `npm install axios` |  |
| [`hoppscotch/hoppscotch`](https://github.com/hoppscotch/hoppscotch) | 80.841 | MIT (Copyright (c) 2022) | Hệ sinh thái phát triển API mã nguồn mở: ứng dụng web/desktop để gửi và kiểm thử request REST, GraphQL, WebSocket, SSE, Socket.IO, MQTT. | Hỗ trợ nhiều giao thức (REST, GraphQL, WebSocket, Server-Sent Events, Socket.IO, MQTT) và nhiều kiểu xác thực (Basic, Bearer, OAuth 2.0, OIDC/PKCE); Có collection, workspace, team cộng tác và pre-request script JavaScript; Monorepo có backend, CLI, ứng dụng desktop, bản self-host web và trang admin (thư mục packages/) |  | Một số tính năng (ví dụ SSO) chỉ có ở bản Enterprise; tự host theo tài liệu self-host trên docs.hoppscotch.io |
| [`openai/openai-python`](https://github.com/openai/openai-python) | 32.184 | Apache License 2.0 | Thư viện Python chính thức truy cập REST API của OpenAI, có client đồng bộ và bất đồng bộ. | Có định nghĩa kiểu cho mọi tham số request và trường response, sinh từ đặc tả OpenAPI; Hỗ trợ streaming, Realtime API, phân trang tự động, xác minh webhook, retry và timeout cấu hình được; Hỗ trợ xác thực workload identity (Kubernetes, Azure, GCP, X.509) thay cho khoá API dài hạn | `pip install openai` | Cần khoá API OpenAI (OPENAI_API_KEY) và tài khoản trả phí theo điều khoản OpenAI; Python 3.10+ |
| [`LibreTranslate/LibreTranslate`](https://github.com/LibreTranslate/LibreTranslate) | 17.783 | GNU Affero General Public License v3 (AGPL-3.0); kèm Hướng dẫn nhãn hiệu (TRADEMARK.md) hạn chế dùng tên/logo LibreTranslate | API dịch máy mã nguồn mở, tự host hoàn toàn, không phụ thuộc dịch vụ độc quyền như Google hay Azure. | Động cơ dịch dựa trên thư viện mã nguồn mở Argos Translate; Có sẵn docker-compose (kể cả bản CUDA) và manifest k8s.yaml để tự triển khai; Có CI chạy test, phát hành gói PyPI và Docker image (theo badge workflow trong README), phiên bản hiện tại 1.9.6 |  | AGPL-3.0: cung cấp qua mạng bản đã sửa phải công khai mã nguồn; dùng tên/logo LibreTranslate cho bản sửa đổi hoặc trong tên miền cần xin phép bằng văn bản theo TRADEMARK.md |

#### 6c.5.3 Bảo mật & Hack

Đọc mã 9 repo, giữ 9.

| Repo | ★ (18/11/2026) | Giấy phép | Làm gì | Điểm mạnh (đọc mã) | Cài | Điều kiện dùng |
|---|---|---|---|---|---|---|
| [`Hack-with-Github/Awesome-Hacking`](https://github.com/Hack-with-Github/Awesome-Hacking) | 125.873 | CC0 1.0 Universal | Tuyển tập các awesome list cho hacker, pentester và nhà nghiên cứu bảo mật. | Gom khoảng 80 liên kết tới các danh sách chuyên đề (Android, CTF, fuzzing, malware analysis, OSINT, prompt injection…); Chia hai mục: Awesome Repositories và Other Useful Repositories, mỗi dòng có mô tả ngắn; Giấy phép CC0, dùng lại tự do |  | Nội dung dẫn tới công cụ tấn công; chỉ dùng hợp pháp trên hệ thống được phép |
| [`sherlock-project/sherlock`](https://github.com/sherlock-project/sherlock) | 113.816 | MIT (Copyright (c) 2019 Sherlock Project) | Công cụ dòng lệnh tìm tài khoản mạng xã hội theo tên người dùng trên hơn 400 trang. | Kiểm tra nhiều username cùng lúc, xuất kết quả ra txt, CSV hoặc xlsx; Hỗ trợ proxy, giới hạn theo trang (--site) và nạp danh sách trang từ file JSON; Cài được qua pipx/pip/uv, Docker hoặc dnf, phiên bản pyproject 0.16.2 | `pipx install sherlock-project` | Công cụ OSINT tra cứu tài khoản người khác: cần tuân thủ luật về quyền riêng tư và điều khoản các trang được truy vấn (dự án không nêu cụ thể); README cảnh báo gói ParrotOS và Ubuntu 24.04 do bên thứ ba duy trì có vẻ bị hỏng |
| [`NationalSecurityAgency/ghidra`](https://github.com/NationalSecurityAgency/ghidra) | 100.473 | Apache License 2.0; thành phần bên thứ ba theo các giấy phép riêng trong thư mục licenses/ và GPL/ (GPL, LGPL, BSD…); kèm DISCLAIMER.md miễn trừ bảo đảm của Chính phủ Mỹ | Khung kỹ nghệ đảo ngược phần mềm (SRE) do Ban Nghiên cứu của NSA tạo và duy trì: dịch ngược, disassembly, decompile, vẽ đồ thị và scripting. | Hỗ trợ nhiều tập lệnh vi xử lý và định dạng thực thi, chạy được tương tác hoặc tự động; Mở rộng bằng extension/script Java hoặc Python (có PyGhidra); Chạy trên Windows, macOS, Linux, phiên bản ứng dụng 12.3 | `Tải bản phát hành zip từ GitHub Releases, giải nén rồi chạy ./ghidraRun (cần JDK 25 64-bit)` | Cần JDK 25 64-bit; README cảnh báo một số phiên bản có lỗ hổng bảo mật đã biết, cần đọc Security Advisories; DISCLAIMER.md: người dùng cam kết bồi hoàn cho Chính phủ Mỹ với mọi khiếu nại phát sinh từ việc sử dụng |
| [`swisskyrepo/PayloadsAllTheThings`](https://github.com/swisskyrepo/PayloadsAllTheThings) | 82.743 | MIT (Copyright (c) 2019 Swissky); kèm DISCLAIMER.md chỉ cho mục đích giáo dục và nghiên cứu | Bộ tài liệu payload và kỹ thuật bypass cho bảo mật ứng dụng web, chia theo từng loại lỗ hổng. | Hơn 60 thư mục chuyên đề (CORS, CRLF, JWT, GraphQL, deserialization, SSRF…), mỗi mục có README mô tả và cách khai thác; Nhiều mục có file Intruder dùng trực tiếp với Burp Intruder; Có bản hiển thị web PayloadsAllTheThingsWeb |  | DISCLAIMER: chỉ dùng cho giáo dục và nghiên cứu, tuân thủ pháp luật và chỉ trên hệ thống có ủy quyền rõ ràng |
| [`danielmiessler/SecLists`](https://github.com/danielmiessler/SecLists) | 74.821 | MIT (Copyright (c) 2018 Daniel Miessler) | Tập hợp các loại danh sách dùng khi đánh giá bảo mật: username, mật khẩu, URL, mẫu dữ liệu nhạy cảm, payload fuzzing, web shell. | Tổ chức theo thư mục Discovery, Fuzzing, Passwords, Usernames, Payloads, Web-Shells, Pattern-Matching và Ai/LLM_Testing; Cài được qua git clone, zip, apt (Kali) hoặc pacman (BlackArch); Có công cụ sinh/biến đổi wordlist trong thư mục .bin | `git clone --depth 1 https://github.com/danielmiessler/SecLists.git` | README cảnh báo phần mềm diệt virus có thể báo nhầm; không nên lưu trên máy chủ quan trọng vì rủi ro local file include; dung lượng lớn |
| [`zhaoxuya520/reverse-skill`](https://github.com/zhaoxuya520/reverse-skill) | 44.842 | MIT (Copyright (c) 2026 zhaoxuya520) | Gói skill định tuyến cho AI agent (Claude Code, Codex, Cursor, OpenCode…) làm dịch ngược, pentest, phân tích malware và CTF: chọn phương pháp, kiểm tra công cụ có sẵn và chạy quy trình lặp lại được. | Bảng định tuyến tập trung trong skills/config/routing.json với 44 route, kèm bộ hồi quy 221 ca; Bao phủ nhiều kịch bản (APK, binary, .NET, JS, firmware, malware/YARA, API, LLM security) và thư mục CTF-Sandbox-Orchestrator; CI chạy trên Windows và Ubuntu, có cổng phạm vi/uỷ quyền (scope.md) trước khi tác động mục tiêu | `git clone https://github.com/zhaoxuya520/reverse-skill.git rồi bash skills/scripts/refresh-tool-index.sh` | Chỉ dùng cho nghiên cứu bảo mật hợp pháp, CTF, hệ thống sở hữu hoặc được uỷ quyền rõ ràng; RULES.md yêu cầu người dùng duyệt trước khi chạy script; cần JDK, Node.js 22.12+, Python 3 và một AI client; kho có chuỗi payload có thể bị antivirus phát hiện; README chứa chỉ thị dành cho AI agent (README_AI.md) cần coi là dữ liệu |
| [`jumpserver/jumpserver`](https://github.com/jumpserver/jumpserver) | 31.982 | GPL-3.0 (GNU General Public License v3); README ghi Copyright (c) 2014-2026 FIT2CLOUD | Nền tảng quản lý truy cập đặc quyền (PAM/bastion host) mã nguồn mở, có tính năng AI, cho phép truy cập an toàn tới SSH, RDP, Kubernetes, cơ sở dữ liệu, website, RemoteApp. | README nêu rõ lịch bảo trì phiên bản (5.x đang bảo trì, 4.10.x là LTS, 3.10.x chỉ sửa lỗi nghiêm trọng); cài nhanh bằng một script quick_start.sh; README có bản dịch nhiều ngôn ngữ kể cả tiếng Việt | `curl -sSL https://github.com/jumpserver/jumpserver/releases/latest/download/quick_start.sh rồi chạy bằng bash` | Máy chủ Linux 64-bit tối thiểu 4 nhân CPU, 8 GB RAM; giấy phép GPLv3 (copyleft); một số thành phần thuộc bản Enterprise; V3 CE hết hỗ trợ 31/12/2026; phải đổi mật khẩu mặc định admin/ChangeMe |
| [`Infisical/infisical`](https://github.com/Infisical/infisical) | 30.570 | MIT (Expat) cho phần ngoài thư mục ee/; các thư mục ee/ theo giấy phép thương mại riêng (ee/LICENSE, cần giấy phép Infisical) | Nền tảng hạ tầng bảo mật mã nguồn mở để quản lý bí mật, chứng chỉ, khoá, truy cập đặc quyền và truy cập của AI agent; có quét lộ bí mật. | Hỗ trợ xoay vòng bí mật và bí mật động cho PostgreSQL, MySQL, AWS IAM; có Kubernetes Operator, CLI và SDK cho nhiều ngôn ngữ (Node, Python, Go, Java, .NET, Rust...); tự host được bằng Docker Compose | `git clone https://github.com/Infisical/infisical && cd infisical && cp .env.example .env && docker compose -f docker-compose.prod.yml up` | Tính năng trong thư mục ee/ cần giấy phép doanh nghiệp Infisical; chạy cục bộ cần Git và Docker; có bản Infisical Cloud trả phí/miễn phí tuỳ gói |
| [`google/magika`](https://github.com/google/magika) | 18.831 | Apache-2.0 | Công cụ nhận diện loại tệp bằng mô hình học sâu nhỏ gọn, có CLI viết bằng Rust và thư viện Python, JavaScript, Rust, Go. | Huấn luyện trên khoảng 100 triệu mẫu với hơn 200 loại nội dung, độ chính xác trung bình khoảng 99% trên tập test; suy luận khoảng 5 ms mỗi tệp trên một CPU; được Google dùng cho Gmail, Drive, Safe Browsing và tích hợp với VirusTotal | `pip install magika (hoặc pipx install magika, brew install magika, npm install magika)` | README ghi không phải dự án Google chính thức, không được Google hỗ trợ; gói npm và binding Go còn thử nghiệm/đang làm |

#### 6c.5.4 Bộ nhớ, Ngữ cảnh & Tiết kiệm token

Đọc mã 5 repo, giữ 4.

| Repo | ★ (18/11/2026) | Giấy phép | Làm gì | Điểm mạnh (đọc mã) | Cài | Điều kiện dùng |
|---|---|---|---|---|---|---|
| [`TencentCloud/TencentDB-Agent-Memory`](https://github.com/TencentCloud/TencentDB-Agent-Memory) | 30.979 | MIT (Copyright (C) 2026 Tencent) | Hệ thống bộ nhớ dùng chung cho AI agent (Memory Hub + Proxy) để lưu, tổ chức và tái sử dụng ngữ cảnh, tài liệu, quy trình giữa các agent như Claude Code, Codex, Hermes, OpenClaw. | Tích hợp không cần sửa mã: trỏ base URL của agent tới Proxy; khởi động cả ba dịch vụ bằng một script start-all.sh và có bảng điều khiển web; README báo PersonaMem tăng từ 48% lên 76% khi bật | `git clone https://github.com/TencentCloud/TencentDB-Agent-Memory.git && cd TencentDB-Agent-Memory/deploy/global-images && cp .env.example .env && ./start-all.sh` | Cần điền hai bộ tham số LLM (khoá API nhà cung cấp LLM) trong .env; Node >= 22.16; backend MongoDB còn thử nghiệm |
| [`MemoriLabs/Memori`](https://github.com/MemoriLabs/Memori) | 17.593 | Apache-2.0 | Lớp bộ nhớ cho AI agent, gắn vào client LLM sẵn có để tự lưu và gợi nhớ hội thoại, lời gọi tool và quyết định; có SDK Python và TypeScript. | Không phụ thuộc LLM, kho dữ liệu hay framework (hỗ trợ Anthropic, Bedrock, Gemini, LangChain, Agno...); README báo đạt 87% trên LoCoMo với trung bình 721 token mỗi truy vấn; có plugin cho OpenClaw và tuỳ chọn tự mang cơ sở dữ liệu (BYODB) | `pip install memori (hoặc npm install @memorilabs/memori)` | Quickstart cần đăng ký Memori Cloud lấy MEMORI_API_KEY và khoá LLM (ví dụ OPENAI_API_KEY); muốn tự host dữ liệu dùng chế độ BYODB |
| [`memvid/memvid`](https://github.com/memvid/memvid) | 17.429 | Apache-2.0 | Lớp bộ nhớ cho AI agent đóng gói dữ liệu, embedding, chỉ mục tìm kiếm và metadata vào một tệp duy nhất (.mv2), truy xuất trực tiếp không cần cơ sở dữ liệu hay server. | Viết bằng Rust, có CLI và SDK Node.js, Python; ghi chỉ-thêm (append-only) theo Smart Frame bất biến, hỗ trợ xem lại trạng thái bộ nhớ trong quá khứ; tính năng tuỳ chọn gồm BM25 (Tantivy), tìm vector HNSW với embedding cục bộ qua ONNX, trích PDF, CLIP, Whisper | `cargo add memvid-core (hoặc npm install -g memvid-cli, pip install memvid-sdk)` | Rust 1.85.0+ khi dùng thư viện Rust; tính năng api_embed cần khoá OpenAI; embedding cục bộ cần tải mô hình ONNX riêng |
| [`NevaMind-AI/memU`](https://github.com/NevaMind-AI/memU) | 14.628 | Apache-2.0 (file LICENSE.txt) | Hệ thống bộ nhớ cá nhân dạng wiki cho agent, dùng chung giữa phiên, agent và thiết bị, tự rút kỹ năng tái sử dụng từ lịch sử agent. | Lõi logic bộ nhớ chỉ khoảng 500 dòng; có adapter cho Codex, Claude Code, Cursor, OpenClaw, Hermes, WorkBuddy với ma trận hỗ trợ theo hệ điều hành; lưu trữ SQLite cục bộ hoặc Postgres với pgvector | `pip install memu-cli` | Bản cloud cần API key từ memu.so; tự host cần khoá nhà cung cấp embedding (OpenAI, Jina, Voyage...); Python 3.11+ |

**Chưa thêm (1 repo, giữ trong file dữ liệu):** `Ebony-Vinyl/dsh-our-free-model` (còn thử nghiệm: Huy hiệu trạng thái trong README ghi "beta").

#### 6c.5.5 Container & DevOps

Đọc mã 17 repo, giữ 16.

| Repo | ★ (18/11/2026) | Giấy phép | Làm gì | Điểm mạnh (đọc mã) | Cài | Điều kiện dùng |
|---|---|---|---|---|---|---|
| [`torvalds/linux`](https://github.com/torvalds/linux) | 256.236 | GPL-2.0 WITH Linux-syscall-note (GPL v2 only kèm ngoại lệ syscall; một số tệp có thể theo giấy phép khác, xem Documentation/process/license-rules.rst) | Mã nguồn nhân Linux, lõi của mọi hệ điều hành Linux, quản lý phần cứng, tài nguyên hệ thống và cung cấp dịch vụ nền cho phần mềm khác. | Phiên bản trong Makefile là 7.4.0-rc3; hỗ trợ 23 mục kiến trúc trong thư mục arch/ và có thư mục rust/; README hướng dẫn theo vai trò kèm tài liệu build, gửi patch, mailing list |  | Giấy phép GPL v2 only (copyleft); đóng góp qua patch gửi email/mailing list theo Documentation/process/submitting-patches.rst |
| [`fatedier/frp`](https://github.com/fatedier/frp) | 110.640 | Apache-2.0 | Reverse proxy nhanh giúp đưa dịch vụ cục bộ nằm sau NAT/tường lửa ra Internet, hỗ trợ TCP, UDP, HTTP, HTTPS và chế độ P2P. | Gồm frps (máy có IP công khai) và frpc (máy trong LAN) phát hành sẵn nhị phân; có dashboard, metrics Prometheus, xác thực token/OIDC, TLS, giới hạn băng thông; hỗ trợ cấu hình TOML, biến môi trường và hot-reload | `Tải nhị phân frps/frpc từ trang Releases rồi chạy với tệp cấu hình` | Cần một máy chủ có IP công khai; README lưu ý phần mềm diệt virus có thể đánh dấu nhầm frpc là mã độc; v2 đang phát triển sẽ không tương thích v1 |
| [`caddyserver/caddy`](https://github.com/caddyserver/caddy) | 79.146 | Apache License 2.0 | Máy chủ web/nền tảng máy chủ mở rộng viết bằng Go, mặc định dùng TLS và tự động cấp chứng chỉ HTTPS. | HTTPS tự động qua ZeroSSL và Let's Encrypt, có CA nội bộ cho tên/IP nội bộ; hỗ trợ HTTP/1.1, HTTP/2 và HTTP/3 mặc định; cấu hình động qua JSON API, Caddyfile và config adapter, kiến trúc module (thư mục modules/ có caddyhttp, caddytls, caddypki) | `Tải bản thực thi từ GitHub Releases; build: cd caddy/cmd/caddy && go build (hoặc xcaddy build)` | Build từ mã cần Go 1.26.0 trở lên; bind cổng thấp trên Linux cần setcap cap_net_bind_service |
| [`moby/moby`](https://github.com/moby/moby) | 72.275 | Apache License 2.0 | Dự án mã nguồn mở do Docker tạo, cung cấp bộ thành phần để lắp ráp hệ thống container; là upstream của Docker Engine. | Docker cam kết dùng Moby làm upstream cho sản phẩm Docker; cung cấp module Go github.com/moby/moby/client và api cho Docker Engine API; có badge OpenSSF Scorecard và OpenSSF Best Practices |  | Bản phát hành chỉ hỗ trợ theo khả năng (best effort), không hỗ trợ thương mại; module github.com/docker/docker đã ngừng cập nhật từ v29; việc dùng và chuyển giao có thể chịu hạn chế xuất khẩu của Mỹ và các chính phủ khác |
| [`ansible/ansible`](https://github.com/ansible/ansible) | 71.623 | GNU General Public License v3.0 (README ghi "v3.0 or later"); thư mục licenses/ chứa thêm Apache, BSD-3-Clause, MIT, PSF, Simplified BSD cho các phần riêng | Hệ thống tự động hoá hạ tầng IT (ansible-core): quản lý cấu hình, triển khai ứng dụng, cấp phát cloud, thực thi tác vụ ad-hoc và tự động hoá mạng. | Không cần agent, dùng SSH sẵn có; điều phối nhiều node, hỗ trợ cập nhật cuốn chiếu không downtime; được Red Hat tài trợ với hơn 5000 người đóng góp | `pip install ansible-core` | GPL v3: phân phối bản sửa đổi phải theo điều khoản copyleft |
| [`Kong/kong`](https://github.com/Kong/kong) | 44.390 | Apache License 2.0 | API Gateway cloud-native, mở rộng bằng plugin, đồng thời làm cổng cho lưu lượng LLM và MCP (định tuyến, cân bằng tải, xác thực, giới hạn tốc độ). | Định tuyến, cân bằng tải, health check cấu hình qua Admin API REST hoặc khai báo; xác thực JWT, basic auth, OAuth, ACL qua plugin; chạy DB-less hoặc hybrid (tách control plane/data plane), có Kubernetes Ingress Controller chính thức | `git clone https://github.com/Kong/docker-kong && cd docker-kong/compose && KONG_DATABASE=postgres docker-compose --profile database up` | Một số tính năng gateway bổ sung và control plane SaaS thuộc gói thương mại Konnect; tính năng AI cần khoá của nhà cung cấp LLM tương ứng (chưa xác minh chi tiết) |
| [`alibaba/nacos`](https://github.com/alibaba/nacos) | 33.525 | Apache License 2.0 | Nền tảng khám phá dịch vụ, quản lý cấu hình động và quản lý dịch vụ cho ứng dụng cloud-native và microservice. | Đăng ký/khám phá dịch vụ qua DNS hoặc HTTP kèm health check thời gian thực; quản lý cấu hình tập trung, cập nhật không cần redeploy; hỗ trợ Dubbo/gRPC, Spring Cloud và Kubernetes | `unzip nacos-server-<phiên bản>.zip && cd nacos/bin && sh startup.sh -m standalone` |  |
| [`dapr/dapr`](https://github.com/dapr/dapr) | 26.204 | Apache License 2.0 | Runtime chạy dạng sidecar cho ứng dụng phân tán, workflow bền vững và AI agent, cung cấp API thống nhất qua HTTP/gRPC. | Dự án tốt nghiệp (graduated) của CNCF; workflow bền vững tự tiếp tục sau sự cố, có mTLS và chính sách truy cập giữa dịch vụ; API state, pub/sub, actors, secrets, jobs với SDK cho .NET, Java, Go, JS, Python, Rust, C++, PHP | `Xem hướng dẫn Getting Started tại docs.dapr.io (cài qua Dapr CLI)` |  |
| [`cilium/cilium`](https://github.com/cilium/cilium) | 25.863 | Apache License 2.0 cho thành phần user space; mã eBPF trong bpf/ theo GPL-2.0 và BSD-2-Clause | Giải pháp mạng, quan sát và bảo mật cho Kubernetes dựa trên eBPF: CNI, cân bằng tải, chính sách mạng L3-L7, service mesh. | Dự án tốt nghiệp (graduated) của CNCF; có thể thay thế hoàn toàn kube-proxy bằng hash table eBPF; duy trì 3 nhánh ổn định (v1.18 đến v1.20), ảnh có SBOM định dạng SPDX từ 1.13 | `Xem hướng dẫn cài đặt docs.cilium.io (Helm chart trên Artifact Hub)` | Cần nhân Linux hỗ trợ eBPF; ảnh chỉ cho AMD64 và AArch64; ảnh build từ main/RC không dùng cho production |
| [`PrefectHQ/prefect`](https://github.com/PrefectHQ/prefect) | 24.175 | Apache License 2.0 | Framework điều phối workflow bằng Python để xây dựng pipeline dữ liệu với lập lịch, retry, cache và tự động hoá theo sự kiện. | Biến script thành workflow chỉ bằng decorator flow và task; có Prefect server tự host với UI tại localhost:4200; hỗ trợ lập lịch cron qua serve() và chạy deployment theo sự kiện | `pip install -U prefect` | Cần Python 3.11 trở lên; Prefect Cloud là dịch vụ quản lý tuỳ chọn |
| [`keploy/keploy`](https://github.com/keploy/keploy) | 19.881 | Apache License 2.0 | Công cụ kiểm thử API và tích hợp, ghi lại lưu lượng thật (API, truy vấn DB, sự kiện streaming) bằng eBPF rồi phát lại thành test và mock. | Không cần sửa code hay SDK, độc lập ngôn ngữ; mock được Postgres, MySQL, MongoDB, Kafka, RabbitMQ; tích hợp CI/CD và đóng băng thời gian để phát lại tất định | `keploy record -c "CMD_TO_RUN_APP" rồi keploy test -c "CMD_TO_RUN_APP" --delay 10 (cài agent qua script install.sh của keploy.io)` | Một số phụ thuộc giao thức không mã nguồn mở theo README; một số tính năng (console, mock registry, mở rộng bằng AI) thuộc nền tảng keploy.io (chưa xác minh phạm vi miễn phí) |
| [`labring/sealos`](https://github.com/labring/sealos) | 18.398 | Sealos Sustainable Use License 1.0 (biến thể Sustainable Use License, không phải giấy phép mã nguồn mở chuẩn): chỉ dùng nội bộ doanh nghiệp hoặc cá nhân phi thương mại; cấm cung cấp dịch vụ cloud cho bên thứ ba; chỉ phân phối miễn phí phi thương mại | Hệ điều hành cloud xây trên Kubernetes, gom cloud IDE (DevBox), cơ sở dữ liệu quản lý, object storage và app store để phát triển, triển khai và vận hành ứng dụng. | Cloud IDE DevBox truy cập từ VSCode và Cursor; cơ sở dữ liệu quản lý PostgreSQL, MySQL, MongoDB, Redis cùng object storage tương thích S3; đa tenant theo workspace với RBAC và quota tài nguyên |  | Giấy phép cấm dùng để cung cấp dịch vụ cloud (công khai, riêng hay managed) cho bên thứ ba và hạn chế phân phối; đóng góp phải đồng ý CLA và điều khoản đổi giấy phép |
| [`argoproj/argo-workflows`](https://github.com/argoproj/argo-workflows) | 17.105 | Apache License 2.0 | Engine workflow gốc container chạy trên Kubernetes, hiện thực dưới dạng CRD; mỗi bước là một container, mô tả theo chuỗi bước hoặc DAG. | Dự án CNCF đã tốt nghiệp (graduated), README liệt kê hơn 200 tổ chức đang dùng; hỗ trợ artifact S3/GCS/Azure Blob/Git/HTTP, cron, retry, timeout, giao diện web và REST/gRPC API; có SDK Java, Go, Python (Hera) và TypeScript (Juno) | `Theo hướng dẫn https://argo-workflows.readthedocs.io/en/latest/quick-start/` | Cần cụm Kubernetes |
| [`kubesphere/kubesphere`](https://github.com/kubesphere/kubesphere) | 17.083 | Apache License 2.0 kèm điều kiện bổ sung (KubeSphere Open Source License): bản 4.x trở đi cần giấy phép thương mại hoặc phép rõ ràng để dùng thương mại cung cấp cho bên thứ ba, cung cấp dạng SaaS, hoặc gỡ/sửa logo-tên KubeSphere; người đóng góp đồng ý maintainer được đổi giấy phép; bản 3.4.x trở về trước theo giấy phép cũ | Nền tảng container đa thuê bao dùng Kubernetes làm nhân, quản lý ứng dụng cloud-native đa cụm, datacenter và biên qua giao diện web, có kiến trúc mở rộng bằng plugin. | Quản lý đa cụm Kubernetes từ một control plane tập trung; tích hợp DevOps (Argo CD, Jenkins), service mesh dựa Istio, App Store cho Helm và biên qua KubeEdge; hỗ trợ cài đặt air-gapped | `helm upgrade --install -n kubesphere-system --create-namespace ks-core https://charts.kubesphere.io/main/ks-core-1.1.3.tgz --debug --wait` | Cần cụm Kubernetes; giấy phép v4.x cấm dùng thương mại cho bên thứ ba, SaaS hoặc đổi thương hiệu nếu không có giấy phép thương mại (liên hệ kubesphere@yunify.com) |
| [`budtmo/docker-android`](https://github.com/budtmo/docker-android) | 16.155 | Apache License 2.0 có sửa đổi (Custom Apache 2.0): fork phải gỡ Google Form ID hoặc tắt thu thập dữ liệu; người dùng đồng ý cho maintainer thu thập và dùng vĩnh viễn dữ liệu không định danh (thời gian, phiên bản hệ điều hành, thành phố/vùng/quốc gia qua ipinfo.io, cấu hình dùng) | Image Docker chạy trình giả lập Android (Android 9 đến 14) phục vụ phát triển và kiểm thử ứng dụng native, web và hybrid. | Có nhiều hồ sơ thiết bị như Samsung Galaxy S10, Nexus, Pixel C; xem màn hình qua VNC trên web (cổng 6080) và điều khiển từ ngoài bằng adb connect; hỗ trợ Appium, Espresso và image MCP server | `docker run -d -p 6080:6080 -e EMULATOR_DEVICE="Samsung Galaxy S10" -e WEB_VNC=true --device /dev/kvm --name android-container budtmo/docker-android:emulator_11.0` | Chỉ chạy trên Ubuntu có ảo hoá KVM (macOS/Windows cần máy ảo Ubuntu hoặc WSL2 trên Windows 11); giấy phép bắt buộc chấp nhận thu thập dữ liệu sử dụng; MCP server và AI-Agent còn beta |
| [`apache/dolphinscheduler`](https://github.com/apache/dolphinscheduler) | 14.557 | Apache License 2.0 (kèm NOTICE) | Nền tảng điều phối dữ liệu low-code của Apache, tạo và quản lý workflow có phụ thuộc phức tạp qua giao diện kéo thả, Python SDK hoặc Open API. | Bốn chế độ triển khai Standalone, Cluster, Docker và Kubernetes; kiến trúc phi tập trung nhiều master và worker, mở rộng ngang; có hơn 30 plugin tác vụ trong repo như Spark, Flink, SQL, Shell, Python, Kubeflow, SageMaker, EMR | `Theo hướng dẫn standalone/Docker/Kubernetes tại https://dolphinscheduler.apache.org` |  |

**Chưa thêm (1 repo, giữ trong file dữ liệu):** `kubeflow/kubeflow` (repo chỉ là cổng dẫn tới dự án con, không chứa mã).

#### 6c.5.6 Danh sách Awesome & Tổng hợp

Đọc mã 14 repo, giữ 14.

| Repo | ★ (18/11/2026) | Giấy phép | Làm gì | Điểm mạnh (đọc mã) | Cài | Điều kiện dùng |
|---|---|---|---|---|---|---|
| [`sindresorhus/awesome`](https://github.com/sindresorhus/awesome) | 538.588 | CC0 1.0 Universal | Danh sách gốc tổng hợp các awesome list theo chủ đề như nền tảng, ngôn ngữ lập trình, front-end, back-end, khoa học máy tính. | Hơn 600 mục liên kết tới các awesome list; có hướng dẫn tạo list (create-list.md) và quy tắc đóng góp; nội dung CC0 dùng tự do |  |  |
| [`vinta/awesome-python`](https://github.com/vinta/awesome-python) | 335.505 | Creative Commons Attribution 4.0 International (CC BY 4.0) | Danh sách tuyển chọn có chủ kiến các framework, thư viện và công cụ Python, chia theo nhóm như AI/ML, web, dữ liệu, cơ sở dữ liệu. | Có website awesome-python.com để tìm kiếm và lọc, được dựng từ README bằng mã trong thư mục website; phân loại thành nhiều danh mục từ AI and Agents tới Web Scraping, ORM, Data Validation |  | Nội dung theo CC BY 4.0, cần ghi công khi dùng lại |
| [`avelino/awesome-go`](https://github.com/avelino/awesome-go) | 194.515 | MIT | Danh sách tuyển chọn các framework, thư viện và phần mềm Go, có website awesome-go.com. | Có test Go tự động kiểm danh sách, gồm kiểm repo cũ không còn bảo trì (stale_repositories_test.go) và độ trưởng thành (maturity_test.go); hàng nghìn mục theo danh mục; website triển khai qua Netlify |  |  |
| [`awesomedata/awesome-public-datasets`](https://github.com/awesomedata/awesome-public-datasets) | 80.184 | MIT | Danh sách các nguồn dữ liệu công khai chất lượng cao theo chủ đề như nông nghiệp, sinh học, khí hậu, kinh tế. | README sinh tự động từ repo apd-core với siêu dữ liệu YAML cho từng bộ dữ liệu; hơn 1000 mục đánh dấu trạng thái OK hoặc cần sửa |  | README nói phần lớn dữ liệu miễn phí nhưng một số không; điều khoản dùng tuỳ từng nguồn dữ liệu |
| [`fffaraz/awesome-cpp`](https://github.com/fffaraz/awesome-cpp) | 74.480 | MIT | Danh sách tuyển chọn framework, thư viện và tài nguyên C++ (và C), kèm danh sách sách và video. | Hơn 1300 mục theo danh mục từ AI, audio, cryptography tới game engine, GUI; có file riêng books.md và videos.md |  |  |
| [`vuejs/awesome-vue`](https://github.com/vuejs/awesome-vue) | 73.473 | MIT | Danh sách tuyển chọn tài nguyên, thư viện, công cụ và dự án liên quan đến Vue.js. | Thuộc tổ chức vuejs trên GitHub; mục lục chia nhóm rõ (tài nguyên chính thức, hướng dẫn, công ty và dự án dùng Vue, thành phần UI); có huy hiệu Awesome và Track Awesome List |  |  |
| [`deepseek-ai/awesome-deepseek-integration`](https://github.com/deepseek-ai/awesome-deepseek-integration) | 39.943 | CC0 1.0 Universal | Danh sách phần mềm và framework đã tích hợp DeepSeek API (ứng dụng, framework agent, RAG, plugin…). | Do tổ chức deepseek-ai duy trì; README có bản tiếng Anh, giản thể, phồn thể, Nhật, Tây Ban Nha; chia nhóm theo loại tích hợp (ứng dụng, AI agent, RAG, FHE…) |  | Cần API key từ DeepSeek Open Platform để dùng các tích hợp |
| [`academic/awesome-datascience`](https://github.com/academic/awesome-datascience) | 30.344 | MIT | Kho tài nguyên mở để học và áp dụng khoa học dữ liệu: khái niệm, lộ trình, dự án, công cụ. | Cập nhật gần (commit 2026-11-17); có CONTRIBUTING.md và CODE_OF_CONDUCT.md; mục lục từ 'Khoa học dữ liệu là gì' đến agents và dự án |  |  |
| [`enescingoz/awesome-n8n-templates`](https://github.com/enescingoz/awesome-n8n-templates) | 26.460 | Creative Commons Attribution 4.0 International (CC BY 4.0) | Bộ sưu tập hơn 280 mẫu workflow n8n (file JSON) cho Gmail, Telegram, OpenAI, Slack, Google Sheets… chia theo 18 nhóm. | Kho có 369 file JSON mẫu chia theo thư mục chủ đề; README dịch sang nhiều ngôn ngữ (tr, de, es, fr, ja, ko…); mỗi mẫu có mô tả và liên kết trong bảng | `Nhập file JSON vào n8n rồi cấu hình credential cho từng dịch vụ` | Cần n8n (Cloud hoặc tự host theo giấy phép của n8n) và tài khoản/credential các dịch vụ kết nối; README nói các mẫu thu thập từ mạng, không do tác giả tạo hay sở hữu, quyền thuộc tác giả gốc, không chịu trách nhiệm thiệt hại; CC BY 4.0 yêu cầu ghi công |
| [`lukasmasuch/best-of-ml-python`](https://github.com/lukasmasuch/best-of-ml-python) | 23.874 | Creative Commons Attribution-ShareAlike 4.0 International (CC BY-SA 4.0) | Danh sách xếp hạng các thư viện machine learning Python, cập nhật hằng tuần theo điểm chất lượng dự án. | 920 dự án chia 34 nhóm; xếp hạng bằng điểm chất lượng tính tự động từ GitHub và trình quản lý gói; có projects.yaml và thư mục history lưu lịch sử cập nhật |  | CC BY-SA 4.0: ghi công và chia sẻ cùng giấy phép khi phái sinh |
| [`dipakkr/awesome-ai-engineering`](https://github.com/dipakkr/awesome-ai-engineering) | 22.589 | MIT | Danh sách tài nguyên cho sinh viên và người đi làm: học ngôn ngữ lập trình, AI/ML, LLM, Web3, bảo mật, cloud/DevOps, hackathon, học bổng, thực tập. | Mục lục rộng (AI & ML, LLM, Web3, an ninh mạng, cloud/DevOps, frontend); có thư mục riêng theo chủ đề (ML, Python, GSOC, Robotics…); có CONTRIBUTORS.md và hướng dẫn đóng góp |  |  |
| [`EthicalML/awesome-production-machine-learning`](https://github.com/EthicalML/awesome-production-machine-learning) | 21.115 | MIT | Danh sách tuyển chọn thư viện mã nguồn mở để triển khai, giám sát, version, mở rộng và bảo mật machine learning trong production. | Chia nhóm theo mảng (AutoML, data pipeline, deployment & serving, evaluation & monitoring, feature store…); tóm tắt thư viện mới hằng tháng qua releases; có công cụ tìm kiếm trên Hugging Face Spaces và CITATION.cff |  |  |
| [`keon/awesome-nlp`](https://github.com/keon/awesome-nlp) | 19.170 | CC0 1.0 Universal | Danh sách tuyển chọn tài nguyên xử lý ngôn ngữ tự nhiên: nghiên cứu, hướng dẫn, sách, thư viện theo ngôn ngữ, dataset. | Phạm vi nêu rõ (LLM chỉ khi phục vụ tác vụ NLP cốt lõi); thư viện chia theo nhiều ngôn ngữ lập trình (Python, C++, Java, Go, Rust…); có hướng dẫn đóng góp và mẫu PR |  |  |
| [`owainlewis/awesome-artificial-intelligence`](https://github.com/owainlewis/awesome-artificial-intelligence) | 16.855 | MIT | Danh sách tài nguyên có chọn lọc cho lập trình viên học xây dựng và vận hành hệ thống AI tạo sinh và agent. | Có tiêu chí tuyển chọn ghi trong CURATION.md; rà soát hằng tuần bằng tự động hoá (AUTOMATION.md, scripts, tests); nhóm theo học nền tảng, xây ứng dụng LLM, đánh giá và triển khai |  |  |

#### 6c.5.7 Dựng video & Slide tự động

Đọc mã 11 repo, giữ 10.

| Repo | ★ (18/11/2026) | Giấy phép | Làm gì | Điểm mạnh (đọc mã) | Cài | Điều kiện dùng |
|---|---|---|---|---|---|---|
| [`slidevjs/slidev`](https://github.com/slidevjs/slidev) | 49.543 | MIT | Công cụ tạo slide thuyết trình cho lập trình viên từ Markdown, chạy trên Vite và Vue 3. | Hỗ trợ code highlight, live coding (Shiki, Monaco), LaTeX (KaTeX), sơ đồ Mermaid, chế độ người trình bày, vẽ chú thích, ghi hình; xuất PDF, PNG, PPTX; monorepo nhiều gói (cli, parser, client, create-app, create-theme, extension VS Code) | `npm init slidev` | Cần Node.js >= 22.12.0 |
| [`zarazhangrui/frontend-slides`](https://github.com/zarazhangrui/frontend-slides) | 32.485 | MIT (Copyright (c) 2025 Zara Zhang) | Skill cho coding agent (đóng gói thành plugin Claude Code) tạo bài trình chiếu HTML từ đầu hoặc chuyển từ file PowerPoint. | Kết quả là một file HTML duy nhất với CSS/JS nội tuyến, không cần npm hay công cụ build; cho chọn phong cách qua 3 bản xem trước trực quan thay vì mô tả bằng lời; có script extract-pptx.py, deploy.sh, export-pdf.sh trong thư mục scripts | `/plugin marketplace add https://github.com/zarazhangrui/frontend-slides rồi /plugin install frontend-slides@frontend-slides` | Cần coding agent có quyền đọc file và chạy shell (Claude Code, Codex…) |
| [`op7418/guizang-ppt-skill`](https://github.com/op7418/guizang-ppt-skill) | 29.991 | AGPL-3.0 (văn bản GNU AGPL v3 chuẩn, không thêm điều khoản) | Skill cho agent (Claude Code, Codex) tạo PPT dạng một file HTML lật ngang, ảnh minh hoạ cho PPT và ảnh bìa đa nền tảng, có chế độ diễn giả và tập dượt. | Hai hệ thị giác: Style A tạp chí điện tử với 10 bố cục và Style B Swiss với 22 bố cục khoá; có script kiểm tra deck như validate-swiss-deck.mjs và validate-presenter-mode.mjs; README song ngữ Trung/Anh kèm checklist kinh nghiệm thực chiến | `npx skills add https://github.com/op7418/guizang-ppt-skill --skill guizang-ppt-skill` | Cần agent có quyền shell; tạo ảnh minh hoạ là tuỳ chọn, dùng GPT-Image trong Codex; giấy phép AGPL-3.0 (copyleft, áp cả khi cung cấp qua mạng) |
| [`jianchang512/pyvideotrans`](https://github.com/jianchang512/pyvideotrans) | 19.769 | GPL-3.0 | Công cụ dịch video tự động: nhận dạng giọng nói, dịch phụ đề, lồng tiếng AI nhiều vai và ghép lại video, có GUI, CLI và WebUI. | Quy trình một chạm ASR → dịch phụ đề → TTS → ghép video, cho dừng để sửa tay từng bước; hỗ trợ cả mô hình cục bộ (Faster-Whisper, Edge-TTS, F5-TTS…) lẫn nhiều API trực tuyến; có bản .exe đóng gói sẵn cho Windows và Dockerfile cho WebUI | `uv run sp.py (GUI) hoặc uv run cli.py --task vtv --name ./video.mp4 …` | Cần FFmpeg; GPU NVIDIA cần CUDA 12.8 và cuDNN 9.11; API trực tuyến cần tự đăng ký, chịu phí và tuân điều khoản nhà cung cấp; mô hình cục bộ có giấy phép riêng (kiểm tra trước khi dùng thương mại); người dùng phải có quyền hợp pháp với nội dung xử lý |
| [`Huanshere/VideoLingo`](https://github.com/Huanshere/VideoLingo) | 19.299 | Apache-2.0 | Ứng dụng Streamlit kết hợp nhận dạng giọng nói, dịch, cắt dòng phụ đề và lồng tiếng để tạo file phụ đề và video có phụ đề hoặc lồng tiếng. | Nhận dạng và căn chỉnh mức từ bằng Qwen3-ASR + Qwen3-ForcedAligner chạy cục bộ; có HTTP API cục bộ (uv run start.py --api) cho agent và script; cài một chạm trên Windows bằng OneKeyStart.bat, hỗ trợ cả macOS và Linux | `git clone https://github.com/Huanshere/VideoLingo.git && cd VideoLingo && uv run start.py` | Cần API LLM tương thích OpenAI (URL, khoá, model) trả được JSON có cấu trúc; ASR/TTS trực tuyến (ElevenLabs, Azure…) gửi âm thanh tới nhà cung cấp và có thể tính phí; Docker cần GPU NVIDIA và NVIDIA Container Toolkit |
| [`AaronFeng753/Waifu2x-Extension-GUI`](https://github.com/AaronFeng753/Waifu2x-Extension-GUI) | 17.237 | Giấy phép riêng: miễn phí CHỈ cho dùng cá nhân; dùng thương mại phải mua bản Premium qua Patreon (không phải giấy phép mã nguồn mở) | Ứng dụng GUI cho Windows phóng to ảnh, GIF, video bằng siêu phân giải học máy và nội suy khung hình video. | Tích hợp nhiều thuật toán siêu phân giải (Waifu2x, Real-ESRGAN, Real-CUGAN, Anime4K…) và nội suy khung hình (RIFE, CAIN, DAIN, IFRNet); hỗ trợ GPU AMD, NVIDIA, Intel và đa GPU cho mọi engine; gói portable chỉ cần giải nén là chạy | `Tải gói portable Windows x64 từ GitHub Releases (bản mới nhất), giải nén rồi chạy` | Chỉ Windows x64; giấy phép chỉ cho dùng cá nhân, dùng thương mại phải mua Premium; nếu thuật toán có bằng sáng chế tại nước bạn thì phải tự xin phép (theo LICENSE) |
| [`Anionex/banana-slides`](https://github.com/Anionex/banana-slides) | 16.025 | AGPL-3.0 (file LICENSE chuẩn); README thêm: dùng thương mại mã đóng cần xin phép tác giả; CLA cho phép người duy trì cấp lại giấy phép đóng | Ứng dụng tạo slide AI-native dựa trên mô hình sinh ảnh, tạo bài trình chiếu từ ý tưởng, dàn ý, tài liệu hoặc mẫu và sửa bằng ngôn ngữ tự nhiên. | Ba điểm bắt đầu: ý tưởng, dàn ý, mô tả từng trang; phân tích tài liệu PDF, Docx, MD, Txt làm nguồn; xuất PPTX hoặc PDF và PPTX chỉnh sửa được (đang beta), có Docker Compose, bản desktop và CLI | `docker compose up -d (sau khi cấu hình .env)` | Cần khoá API mô hình văn bản và sinh ảnh (Google, OpenAI, Volcengine… hoặc OAuth OpenAI); xuất PPTX chỉnh sửa tốt hơn cần khoá Baidu AI Cloud; bản phát hành mới nhất là v0.9.0-rc.8; AGPL và dùng thương mại mã đóng cần xin phép |
| [`mltframework/shotcut`](https://github.com/mltframework/shotcut) | 15.717 | GPL-3.0 (file COPYING) | Trình biên tập video miễn phí, mã nguồn mở, đa nền tảng dựa trên framework MLT và Qt 6. | Bản nhị phân được build thường xuyên tại shotcut.org; CI build cho Linux, macOS và Windows; dựa trên MLT, FFmpeg, Frei0r, SDL | `Tải bản nhị phân tại https://www.shotcut.org/download/; build: cmake rồi cmake --build . rồi cmake --install .` | Build từ nguồn cần MLT, Qt 6 (tối thiểu 6.4), FFTW, FFmpeg, Frei0r, SDL; README khuyến cáo chỉ người thử beta hoặc người đóng góp mới nên tự build |
| [`Zulko/moviepy`](https://github.com/Zulko/moviepy) | 15.163 | MIT (Copyright (c) 2015 Zulko) | Thư viện Python biên tập video: cắt, nối, chèn tiêu đề, ghép nhiều lớp (non-linear editing), xử lý và tạo hiệu ứng tuỳ biến. | Đọc và ghi hầu hết định dạng âm thanh, video phổ biến kể cả GIF, chạy trên Windows, Mac, Linux với Python 3.9+; truy cập từng pixel qua mảng numpy để viết hiệu ứng ngắn gọn; tài liệu trực tuyến build tự động mỗi lần push, phiên bản hiện tại 2.2.0 | `pip install moviepy` | Dùng FFmpeg để mã hoá và giải mã; v2.0 có thay đổi phá vỡ so với v1, v1 không còn được duy trì |
| [`JuneYaooo/rea-video`](https://github.com/JuneYaooo/rea-video) | 10.336 | Apache-2.0 (kèm file NOTICE) | Công cụ CLI và skill cho agent phân tích ngược video theo từng cảnh quay: quay thật, do AI tạo hay dựng bằng code, và cách làm lại; xuất báo cáo HTML/PDF và VIDEO.md. | Chế độ chỉ dùng công cụ chạy offline và miễn phí, eval công bố độ chính xác 98,3% trên tập tuning và tới 99,6% trên holdout; phân tích cả phụ đề, cắt dựng, âm thanh (giọng người hay AI, BPM nhạc); xuất VIDEO.md định dạng mở phân tầng cho agent đọc tiết kiệm token | `Bảo agent: Install https://github.com/JuneYaooo/rea-video, then break down this video: /path/to/video.mp4` | Cần ffmpeg và Python 3.10+; mô hình thị giác (Gemini, Doubao) là tuỳ chọn, cần endpoint và khoá, tính phí theo nhà cung cấp; README cấm đăng lại video người khác, chỉ dùng để học rồi làm lại bằng tư liệu có quyền và tuân luật dán nhãn nội dung AI |

**Chưa thêm (1 repo, giữ trong file dữ liệu):** `jub0t/Concat` (còn thử nghiệm: README ghi Concat đang ở giai đoạn beta (phiên bản 0.2.11)).

#### 6c.5.8 Editor, Terminal & Dòng lệnh

Đọc mã 35 repo, giữ 33.

| Repo | ★ (18/11/2026) | Giấy phép | Làm gì | Điểm mạnh (đọc mã) | Cài | Điều kiện dùng |
|---|---|---|---|---|---|---|
| [`microsoft/vscode`](https://github.com/microsoft/vscode) | 195.711 | MIT (Code - OSS); bản phân phối Visual Studio Code của Microsoft dùng giấy phép sản phẩm Microsoft riêng | Kho mã nguồn mở "Code - OSS" nơi Microsoft phát triển trình soạn thảo Visual Studio Code cùng cộng đồng. | README nêu VS Code cập nhật hằng tháng, chạy trên Windows, macOS và Linux; thư mục extensions chứa các extension tích hợp sẵn (ngữ pháp, snippet nhiều ngôn ngữ); có sẵn dev container và hỗ trợ Codespaces để build | `Tải tại https://code.visualstudio.com/Download` | Bản VS Code do Microsoft phát hành có tuỳ biến riêng và theo giấy phép sản phẩm Microsoft, khác MIT của mã nguồn; build đầy đủ cần ít nhất 4 nhân và 6 GB RAM |
| [`ohmyzsh/ohmyzsh`](https://github.com/ohmyzsh/ohmyzsh) | 190.765 | MIT | Khung mã nguồn mở do cộng đồng phát triển để quản lý cấu hình zsh, kèm nhiều plugin và theme. | Thư mục plugins có hơn 370 mục và themes hơn 140 mục; hỗ trợ Linux, macOS, FreeBSD, Android và Windows qua WSL2; có huy hiệu OpenSSF Best Practices và CI | `sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"` | Cần zsh (khuyến nghị 5.0.8+), curl hoặc wget và git; Windows chỉ qua WSL2 |
| [`github/gitignore`](https://github.com/github/gitignore) | 176.339 | CC0 1.0 Universal | Bộ sưu tập mẫu .gitignore của GitHub, dùng cho bộ chọn mẫu khi tạo repo trên GitHub.com. | Khoảng 317 file .gitignore theo ngôn ngữ, công cụ và hệ điều hành; chia thư mục gốc, Global và community kèm quy tắc phiên bản; phát hành CC0 nên dùng tự do |  |  |
| [`microsoft/terminal`](https://github.com/microsoft/terminal) | 105.413 | MIT | Mã nguồn Windows Terminal, Windows Terminal Preview, console host conhost.exe và các thành phần dùng chung. | Phát hành qua Microsoft Store, GitHub Releases và winget; repo còn chứa ColorTool và dự án mẫu dùng Windows Console API; có kênh Canary cho bản dựng mới | `winget install --id Microsoft.WindowsTerminal -e` | Chỉ cho Windows; cần Windows 10 2004 (build 19041) trở lên |
| [`neovim/neovim`](https://github.com/neovim/neovim) | 103.928 | Apache-2.0, trừ các phần đóng góp theo giấy phép Vim (Vim license) | Neovim là bản tái cấu trúc mạnh của Vim, hướng tới dễ bảo trì, mở rộng và hỗ trợ giao diện nâng cao. | API truy cập từ nhiều ngôn ngữ (C, Go, Lua, Python, Rust…) và trình giả lập terminal nhúng; điều khiển job bất đồng bộ; gói dựng sẵn cho Windows, macOS, Linux và có trong Homebrew, Debian, Fedora, Arch… | `make CMAKE_BUILD_TYPE=RelWithDebInfo && sudo make install` |  |
| [`zed-industries/zed`](https://github.com/zed-industries/zed) | 95.238 | Chủ yếu GPL-3.0-or-later, có thành phần Apache-2.0 nơi đánh dấu (file LICENSE-GPL và LICENSE-APACHE) | Zed là trình soạn thảo mã hiệu năng cao, hỗ trợ cộng tác nhiều người, từ nhóm tác giả Atom và Tree-sitter. | Có bản cho macOS, Linux và Windows; viết bằng Rust (workspace Cargo với thư mục crates); dùng cargo-about để tự động tuân thủ giấy phép phụ thuộc | `Tải tại https://zed.dev/download` | Chưa có bản Web; mã chủ yếu GPL-3.0 (copyleft); phát triển bởi công ty vì lợi nhuận Zed Industries |
| [`junegunn/fzf`](https://github.com/junegunn/fzf) | 84.249 | MIT | fzf là công cụ tìm kiếm mờ đa dụng trên dòng lệnh kiêm bộ công cụ dựng giao diện terminal tương tác. | Phân phối dạng một file nhị phân duy nhất; tích hợp sẵn cho Bash, Zsh, Fish, Nushell, Vim và Neovim; có phím tắt dòng lệnh và fuzzy completion cho file, PID, host | `brew install fzf` |  |
| [`jesseduffield/lazygit`](https://github.com/jesseduffield/lazygit) | 83.950 | MIT | lazygit là giao diện terminal đơn giản cho các lệnh git. | Stage theo hunk hoặc từng dòng, rebase tương tác, cherry-pick, bisect và undo ngay trong TUI; hỗ trợ worktree và đồ thị commit; có gói cho Homebrew, Scoop, Arch, Debian/Ubuntu, NixOS… | `brew install lazygit` | Cần git |
| [`tonsky/FiraCode`](https://github.com/tonsky/FiraCode) | 82.209 | SIL Open Font License 1.1 | Fira Code là phông chữ đơn cách miễn phí có ligature cho các tổ hợp ký tự lập trình phổ biến. | Mã nguồn vẫn tương thích ASCII vì ligature chỉ là tính năng hiển thị; có nhiều character variant và stylistic set (cv01, ss01…); có glyph riêng cho thanh tiến trình tại U+EE00 và hỗ trợ vẽ khung, powerline | `Tải Fira_Code_v6.2.zip từ GitHub Releases` | Một số trình soạn thảo không hiển thị ligature (danh sách trong README) |
| [`coder/code-server`](https://github.com/coder/code-server) | 79.900 | MIT | code-server chạy VS Code trên bất kỳ máy nào và truy cập qua trình duyệt. | Có script cài đặt dùng trình quản lý gói hệ thống và chế độ --dry-run để xem trước; dùng kho extension Open-VSX; có devcontainer feature và triển khai cho nhóm qua coder/coder | `curl -fsSL https://code-server.dev/install.sh rồi chạy bằng sh` | Cần máy Linux có WebSockets, tối thiểu 1 GB RAM và 2 vCPU; không dùng được Marketplace của Microsoft do điều khoản dịch vụ, thay bằng Open-VSX |
| [`Eugeny/tabby`](https://github.com/Eugeny/tabby) | 75.475 | MIT (Copyright (c) 2017 Tabby Developers) | Trình giả lập terminal cấu hình cao kèm client SSH, Telnet và serial cho Windows, macOS và Linux (trước đây tên Terminus). | Tích hợp client SSH2 có trình quản lý kết nối, chuyển tiếp X11/cổng, jump host và kho mã hoá cho bí mật SSH; hỗ trợ PowerShell, WSL, Git-Bash, Cygwin, MSYS2, CMD và chạy portable trên Windows; có hệ plugin/theme cài từ Settings và bản web app tự host được | `Tải bản phát hành từ GitHub Releases hoặc kho packagecloud (deb/rpm)` | README nói rõ không nhẹ (dựa trên Electron), tốn RAM |
| [`jgm/pandoc`](https://github.com/jgm/pandoc) | 46.954 | GPL-2.0-or-later (file COPYRIGHT; một số phần mã có bản quyền/giấy phép khác được liệt kê riêng) | Thư viện Haskell và công cụ dòng lệnh chuyển đổi tài liệu giữa rất nhiều định dạng markup (Markdown, HTML, LaTeX, docx, EPUB, JATS…). | Hỗ trợ hàng chục định dạng đầu vào và đầu ra (README liệt kê từ asciidoc, docx, epub, ipynb tới jira, latex); có pandoc-lua-engine cho filter Lua, pandoc-server và bản wasm trong repo; phát hành qua Hackage, Homebrew, Chocolatey và bộ cài cho Windows/macOS/Linux | `brew install pandoc` | Giấy phép GPL-2.0-or-later (copyleft) khi phân phối hoặc nhúng thư viện |
| [`sxyazi/yazi`](https://github.com/sxyazi/yazi) | 43.468 | MIT (Copyright (c) 2023 sxyazi); bộ icon theo LICENSE-ICONS: MIT (Copyright (c) 2023 nvim-tree) | Trình quản lý file trong terminal viết bằng Rust, dựa trên I/O bất đồng bộ, có xem trước ảnh/mã và hệ plugin Lua. | Mọi thao tác I/O bất đồng bộ, lập lịch tác vụ có tiến độ và huỷ được; hỗ trợ sẵn nhiều giao thức ảnh (kitty, iTerm2, WezTerm, Sixel…); có plugin Lua đồng thời, trình quản lý gói plugin/theme và VFS cho file từ xa | `Xem hướng dẫn tại yazi-rs.github.io/docs/installation` | README ghi đang ở beta công khai (dùng hằng ngày được), phát triển mạnh và có thể có thay đổi phá vỡ |
| [`googleworkspace/cli`](https://github.com/googleworkspace/cli) | 32.371 | Apache-2.0 | CLI gws dùng chung cho mọi API Google Workspace (Drive, Gmail, Calendar, Sheets…), sinh lệnh động từ Google Discovery Service, xuất JSON cho người và AI agent. | Tự nhận endpoint mới vì đọc Discovery Service lúc chạy; có --dry-run, tự phân trang và xuất NDJSON; kèm thư mục skills cho agent (khoảng 95 mục) và thông tin đăng nhập mã hoá AES-256-GCM với khoá trong keyring | `npm install -g @googleworkspace/cli` | Cần dự án Google Cloud (OAuth) và tài khoản Google Workspace; README ghi không phải sản phẩm Google hỗ trợ chính thức; đang phát triển, có thể có thay đổi phá vỡ trước v1.0; app OAuth chưa xác minh bị giới hạn khoảng 25 scope |
| [`tqdm/tqdm`](https://github.com/tqdm/tqdm) | 31.390 | MPL-2.0 và MIT (file LICENCE: mặc định MIT cho tác giả đóng góp; mọi file có phần MPL-2.0 của Casper da Costa-Luis; một số phần MIT của Google Inc. và tác giả gốc) | Thư viện Python hiển thị thanh tiến độ thông minh cho vòng lặp và lệnh shell qua pipe. | Chỉ cần bọc iterable bằng tqdm(iterable); overhead khoảng 60ns mỗi vòng lặp theo README và có kiểm thử hồi quy hiệu năng; không cần phụ thuộc nào, chạy trên Linux, Windows, Mac, BSD và Jupyter | `pip install tqdm` | Giấy phép kép MPL-2.0/MIT theo file LICENCE |
| [`manaflow-ai/cmux`](https://github.com/manaflow-ai/cmux) | 28.813 | GPL-3.0-or-later cho app macOS, iOS, CLI, cmux-tui; các thư mục server (web/, workers/…, services/iroh-relay-minter/, cmux-tui/relays/cloudflare-do/) theo BUSL-1.1, cần giấy phép thương mại của Manaflow để dùng production kể cả tự host | Terminal macOS dựa trên Ghostty với tab dọc và thông báo dành cho AI coding agent, kèm trình duyệt trong app, SSH và CLI/socket API để tự động hoá. | App macOS native viết bằng Swift/AppKit, render GPU qua libghostty và đọc cấu hình Ghostty sẵn có; sidebar hiện nhánh git, trạng thái PR, cổng đang lắng nghe và thông báo agent; có CLI và socket API để tạo workspace, chia pane, gửi phím và điều khiển trình duyệt | `brew tap manaflow-ai/cmux rồi brew install --cask cmux` | Chỉ macOS; phần server theo BUSL-1.1 cần giấy phép thương mại khi chạy production; đóng góp phải ký CLA với Manaflow, Inc. |
| [`every-app/open-seo`](https://github.com/every-app/open-seo) | 28.117 | MIT (Copyright (c) 2026 Ben Senescu) | Công cụ SEO mã nguồn mở thay thế Semrush/Ahrefs (nghiên cứu từ khoá, theo dõi thứ hạng, backlink, audit site) kèm MCP server và skill cho AI agent. | Có MCP server và Agent Skills cho Claude Code, Codex, ChatGPT; tự host bằng Docker (Compose) hoặc Cloudflare, có tài liệu riêng cho từng cách; trả theo mức dùng thay vì thuê bao | `everyapp install https://github.com/every-app/open-seo (sau npm install -g everyapp và everyapp setup)` | Cần khoá API DataForSEO trả phí (hoặc tài khoản treg); bản hosted có thuê bao 10 USD/tháng và cộng 28% phí DataForSEO; tự host qua EveryApp cần gói Cloudflare 5 USD/tháng |
| [`toon-format/toon`](https://github.com/toon-format/toon) | 25.638 | MIT (Copyright (c) 2025-PRESENT Johann Schopplich) | Bản cài đặt TypeScript và CLI cho TOON (Token-Oriented Object Notation), định dạng mã hoá gọn của mô hình dữ liệu JSON nhằm giảm token khi đưa dữ liệu vào LLM. | Biểu diễn không mất mát mô hình dữ liệu JSON với dạng bảng cho mảng đồng nhất; ví dụ trong README giảm từ khoảng 117 xuống 66 token; có gói thư viện @toon-format/toon và CLI @toon-format/cli, theo spec v4.4 có kho riêng | `npm install @toon-format/toon` | README nói định dạng ổn định nhưng vẫn đang tiến hoá; với dữ liệu lồng sâu hoặc không đồng nhất JSON có thể hiệu quả hơn |
| [`nextai-translator/nextai-translator`](https://github.com/nextai-translator/nextai-translator) | 25.067 | AGPL-3.0 (theo file LICENSE; badge README ghi MIT không khớp) | Ứng dụng dịch, trau chuốt và tóm tắt văn bản bằng LLM, có tiện ích trình duyệt (Chrome, Firefox) và app desktop Windows/macOS/Linux; trước đây tên openai-translator. | Ba chế độ dịch, trau chuốt, tóm tắt cho 55 ngôn ngữ, có streaming và TTS; chạy cả tiện ích trình duyệt lẫn desktop (Tauri) đa nền tảng; hỗ trợ dịch ảnh chụp màn hình và sổ từ vựng | `Tải bộ cài từ GitHub Releases hoặc cài tiện ích từ Chrome Web Store/Firefox Add-ons` | Cần khoá API OpenAI hoặc Azure OpenAI (hoặc nhà cung cấp LLM khác, README quảng bá TeamoRouter); đổi tên do cảnh báo nhãn hiệu từ OpenAI; app desktop chưa ký nên Windows/macOS cảnh báo khi cài |
| [`steipete/CodexBar`](https://github.com/steipete/CodexBar) | 23.202 | MIT | Ứng dụng thanh menu macOS 14+ (kèm app desktop Linux Qt 6 và CLI) hiển thị hạn mức sử dụng của các nhà cung cấp AI lập trình cùng thời điểm đặt lại. | README liệt kê 114 nhà cung cấp được hỗ trợ; hiển thị cửa sổ phiên, tuần, tháng kèm đếm ngược tới lần đặt lại và huy hiệu sự cố từ trang trạng thái; có CLI codexbar cho macOS và Linux qua Homebrew, AUR và tarball phát hành | `brew install --cask codexbar` | Cần macOS 14+ (Linux: glibc 2.39+, Qt 6.4+ và CLI cài riêng); dùng lại phiên đăng nhập sẵn có của từng nhà cung cấp (OAuth, khoá API, cookie trình duyệt, file cục bộ). |
| [`zsh-users/zsh-syntax-highlighting`](https://github.com/zsh-users/zsh-syntax-highlighting) | 23.096 | BSD 3-Clause (file COPYING.md, không có file LICENSE) | Plugin cho zsh tô màu cú pháp dòng lệnh ngay khi gõ ở dấu nhắc, theo kiểu fish, giúp phát hiện lỗi cú pháp trước khi chạy. | Có sẵn trong kho gói của nhiều hệ (Arch, Debian, Fedora, FreeBSD, Gentoo, Homebrew, NetBSD, OpenBSD, Ubuntu, Void); kiến trúc nhiều highlighter tách biệt (main, brackets, cursor, line, pattern, regexp, root); thư mục tests riêng trong repo | `brew install zsh-syntax-highlighting` | Cần zsh 4.3.11+; phải source ở cuối .zshrc; tô sáng khi tìm lịch sử tăng dần cần zsh 5.4+. |
| [`pranshuparmar/witr`](https://github.com/pranshuparmar/witr) | 23.032 | Apache-2.0 | Công cụ dòng lệnh (kèm TUI) trả lời câu hỏi vì sao một tiến trình, dịch vụ, container hay cổng đang chạy bằng cách truy ngược chuỗi nguồn gốc của PID. | Một binary tĩnh cho Linux, macOS, FreeBSD và Windows; có đầu ra --json và exit code phân biệt để dùng với AI agent; phân phối qua nhiều trình quản lý gói (APT Debian/Ubuntu, Homebrew, MacPorts, Conda, AUR, Winget, npm, Chocolatey, Scoop) | `brew install witr` |  |
| [`wavetermdev/waveterm`](https://github.com/wavetermdev/waveterm) | 22.719 | Apache-2.0 (kèm file NOTICE) | Terminal mã nguồn mở tích hợp AI cho macOS, Linux và Windows, có phiên SSH bền, trình sửa file từ xa và xem trước file trong bố cục khối kéo thả. | Hỗ trợ tự mang khoá API (OpenAI, Claude, Gemini, Azure) hoặc mô hình cục bộ qua Ollama và LM Studio, không cần tài khoản; phiên SSH tự kết nối lại sau gián đoạn mạng hoặc khởi động lại; lệnh wsh để quản lý workspace và chép file giữa máy cục bộ và máy SSH |  | Tính năng AI cần khoá API của nhà cung cấp hoặc mô hình cục bộ (Wave AI hiện là beta miễn phí kèm credit); macOS 11+, Windows 10 1809+, Linux glibc 2.28+. |
| [`jarun/nnn`](https://github.com/jarun/nnn) | 22.126 | BSD 2-Clause | Trình quản lý file trên terminal rất nhỏ gọn (~150 KiB), gần như không cần cấu hình, có phân tích dung lượng đĩa, đổi tên hàng loạt và chọn file. | Thường dùng dưới 3,5 MB bộ nhớ thường trú; chạy trên Linux, macOS, BSD, Haiku, Cygwin, WSL, Termux; kho plugin trong repo có khoảng 60 mục | `sh -c "$(curl -Ls https://raw.githubusercontent.com/jarun/nnn/master/misc/quickstart.sh)"` |  |
| [`voyager-crew/voyager`](https://github.com/voyager-crew/voyager) | 20.655 | GPL-3.0 (kèm thông báo MIT bên thứ ba trong THIRD_PARTY_NOTICES.md) | Tiện ích trình duyệt bổ sung thư mục, dòng thời gian, xuất hội thoại và chép công thức cho Gemini, AI Studio, ChatGPT, Claude, DeepSeek và Kimi; mỗi tính năng là plugin JSON. | Plugin là JSON thuần, không chạy mã, gỡ sạch khi tắt; phát hành trên Chrome Web Store, Edge Add-ons và Firefox Add-ons; README có 10 bản ngôn ngữ |  | Dự án độc lập, không liên kết với Google, Anthropic, OpenAI hay Moonshot AI; trên Gemini for Enterprise chỉ chạy thư viện prompt; copyleft GPL-3.0. |
| [`larksuite/cli`](https://github.com/larksuite/cli) | 18.144 | MIT | CLI chính thức của Lark/Feishu cho người và AI agent, bao phủ nhắn tin, tài liệu, Base, Sheets, lịch, mail, tác vụ, cuộc họp và nhiều miền khác. | Hơn 200 lệnh theo ba tầng (shortcut, lệnh API, API thô); thư mục skills có 25 skill cho agent; lưu thông tin xác thực qua keychain của hệ điều hành | `npx @larksuite/cli@latest install` | Cần ứng dụng và quyền trên Lark/Feishu Open Platform cùng Node.js; README cảnh báo rủi ro agent ảo giác và prompt injection khi hành động dưới danh tính người dùng; mặc định gửi tín hiệu kiểm soát rủi ro (loại hệ điều hành, model phần cứng) tới tên miền Lark/Feishu, tắt bằng lark-cli config risk-control off. |
| [`commitizen/cz-cli`](https://github.com/commitizen/cz-cli) | 17.503 | MIT | Công cụ dòng lệnh nhắc người dùng điền các trường bắt buộc khi commit để thông điệp commit theo quy ước (ví dụ conventional-changelog). | Dùng git cz hoặc npx cz thay cho git commit; commitizen init cài adapter và ghi cấu hình vào package.json (npm, yarn, pnpm); hỗ trợ chạy qua git hook với tuỳ chọn --hook | `npm install -g commitizen` | README nêu được kiểm thử trên Node.js 12, 14, 16 và cần npm 6+. |
| [`iamgio/quarkdown`](https://github.com/iamgio/quarkdown) | 16.396 | GPL-3.0 | Hệ thống dàn trang dựa trên Markdown mở rộng có hàm (Turing-complete), biên dịch một nguồn thành sách in, bài báo, cơ sở tri thức hoặc trình chiếu. | Hỗ trợ đích HTML dạng liền mạch và dạng trang qua paged.js; định nghĩa hàm, biến và thư viện ngay trong Markdown kèm hệ quyền hạn chế truy cập tài nguyên; cài qua script, Homebrew hoặc Scoop | `brew install quarkdown-labs/quarkdown/quarkdown` | Xuất PDF cần trình duyệt (script cài tự cài kèm); copyleft GPL-3.0. |
| [`alam00000/bentopdf`](https://github.com/alam00000/bentopdf) | 16.388 | AGPL-3.0; cấp phép kép, có giấy phép thương mại riêng (COMMERCIAL-LICENSE.md, 79 USD trọn đời cho một sản phẩm) | Bộ công cụ PDF chạy hoàn toàn phía trình duyệt, tự host được: gộp, tách, sửa, chuyển đổi, bảo mật PDF mà không tải tệp lên máy chủ. | Tài liệu nêu hơn 50 công cụ PDF theo nhóm (sắp xếp, sửa, chuyển đổi, bảo mật); có ảnh Docker ghcr.io và hướng dẫn tự host gồm Docker Compose, Podman, hosting tĩnh và triển khai air-gapped; xử lý trong trình duyệt bằng WASM, tệp không rời máy người dùng. | `docker run -p 3000:8080 ghcr.io/alam00000/bentopdf-simple:latest` | AGPL-3.0: dùng trong sản phẩm đóng nguồn phải mua giấy phép thương mại; các thư viện AGPL (PyMuPDF, Ghostscript, CPDF) tải từ CDN jsDelivr lúc chạy, môi trường offline phải tự cấu hình; Hyper Compress và Kura cấp phép riêng. |
| [`YishenTu/claudian`](https://github.com/YishenTu/claudian) | 16.021 | MIT | Plugin Obsidian nhúng các agent lập trình AI (Claude Code, Codex, Grok Build, OpenCode, Pi…) vào vault, cho agent đọc ghi tệp, tìm kiếm, chạy lệnh trong vault. | Hỗ trợ nhiều harness: Claude Code, Codex, Grok Build, Antigravity CLI, OpenCode, Pi, DeepSeek Harness; có sửa nội dòng với xem trước diff cấp từ, nhắn tin giữa các phiên và kết nối MCP; có trên kho Community Plugins của Obsidian, giao diện 10 ngôn ngữ. | `Obsidian rồi Settings rồi Community plugins rồi tìm "Claudian" và cài` | Cần ít nhất một CLI agent đã cài và gói đăng ký hoặc API của nhà cung cấp; Obsidian 1.13.0+, chỉ desktop; dữ liệu nhập, tệp đính kèm, kết quả tool được gửi tới nhà cung cấp mô hình đã chọn. |
| [`electerm/electerm`](https://github.com/electerm/electerm) | 15.656 | MIT | Trình khách terminal/ssh/sftp/ftp/telnet/serialport/RDP/VNC/Spice mã nguồn mở, kiêm trình quản lý tệp, chạy đa nền tảng. | Chạy trên Windows 7+, macOS 10.15+, Linux (nhiều kiến trúc gồm riscv64, LoongArch), Android, iOS, HarmonyOS; hỗ trợ tunnel ssh, nhảy kết nối, Zmodem/Trzsz và đồng bộ bookmark qua gist/webdav; tích hợp trợ lý AI và widget MCP. | `npm i -g electerm` | Trợ lý AI cần API của nhà cung cấp LLM tự cấu hình; đồng bộ dữ liệu cần tài khoản GitHub/Gitee/WebDAV hoặc electerm cloud. |
| [`Bash-it/bash-it`](https://github.com/Bash-it/bash-it) | 15.307 | MIT | Khung cấu hình Bash do cộng đồng đóng góp, gom alias, plugin, completion và theme để quản lý shell hằng ngày (tương tự oh-my-zsh cho Bash). | Repo có khoảng 81 plugin, 50 bộ alias, 90 completion và 87 theme; có lệnh chẩn đoán bash-it doctor và tìm/bật/tắt thành phần bằng bash-it search; 97% mã tương thích bash 3.2+. | `git clone --depth=1 https://github.com/Bash-it/bash-it.git ~/.bash_it && ~/.bash_it/install.sh` | Trình cài sửa ~/.bashrc tại chỗ (có sao lưu); vài plugin cần bash 5. |
| [`siteboon/claudecodeui`](https://github.com/siteboon/claudecodeui) | 14.670 | AGPL-3.0-or-later kèm điều khoản bổ sung theo Mục 7 (bắt buộc ghi công, cấm dùng tên Siteboon/CloudCLI để quảng bá, không cấp quyền nhãn hiệu); phần đóng góp cũ của người khác vẫn GPL-3.0 | Giao diện web/desktop/di động (CloudCLI UI) cho Claude Code, Cursor CLI và Codex, xem và điều khiển phiên agent cục bộ hoặc từ xa. | Có chat, terminal tích hợp, trình duyệt tệp, Git explorer và quản lý phiên; tự phát hiện phiên có sẵn khi mở localhost:3001; tool của Claude Code tắt mặc định, bật chọn lọc trong cài đặt. | `npx @cloudcli-ai/cloudcli` | Cần Node.js 22+ và gói đăng ký AI riêng (Claude, Cursor…); AGPL: chạy bản sửa đổi như dịch vụ mạng phải công bố mã; chế độ Docker Sandbox còn thử nghiệm và cần CLI sbx; bản Cloud trả phí từ 7 EUR/tháng. |

**Chưa thêm (2 repo, giữ trong file dữ liệu):** `CorentinTh/it-tools` (commit cuối 12/2/2026); `storytold/pdfcraft` (còn thử nghiệm: README tự nhận đang ở giai đoạn alpha (tháng 10/2026)).

#### 6c.5.9 Framework Backend

Đọc mã 24 repo, giữ 22.

| Repo | ★ (18/11/2026) | Giấy phép | Làm gì | Điểm mạnh (đọc mã) | Cài | Điều kiện dùng |
|---|---|---|---|---|---|---|
| [`gohugoio/hugo`](https://github.com/gohugoio/hugo) | 90.501 | Apache-2.0 | Trình sinh trang tĩnh viết bằng Go, tối ưu tốc độ, dùng cho blog, trang tài liệu, trang doanh nghiệp. | Có pipeline tài nguyên tích hợp: xử lý CSS, Sass, Tailwind, bundle JS/TypeScript, xử lý ảnh; Hugo Modules chia sẻ theme, nội dung qua Git; bản deploy đẩy thẳng lên S3, Google Cloud Storage, Azure. | `CGO_ENABLED=0 go install github.com/gohugoio/hugo@latest` | Build từ nguồn cần Go 1.27.0+ và Git. |
| [`gin-gonic/gin`](https://github.com/gin-gonic/gin) | 89.531 | MIT | Framework web HTTP hiệu năng cao cho Go, API kiểu Martini dựa trên httprouter. | Router không cấp phát heap; middleware recovery chống panic làm sập server, binding và kiểm tra JSON tự động; bản 1.12.0 đã phát hành, CI có quét bảo mật Trivy và codecov. | `import "github.com/gin-gonic/gin" (Go modules tự tải)` | Cần Go 1.26+. |
| [`macrozheng/mall`](https://github.com/macrozheng/mall) | 85.057 | Apache-2.0 | Hệ thống thương mại điện tử đầy đủ (cửa hàng và trang quản trị) xây trên Spring Boot và MyBatis, triển khai bằng Docker. | Nhánh master dùng Spring Boot 3.5 và JDK 17 (pom: spring-boot-starter-parent 3.5.14); chia module rõ: admin, portal, search (Elasticsearch), security, mbg; có tài liệu và hướng dẫn triển khai Windows, Docker, Docker Compose, Jenkins tại macrozheng.com. |  | Tài liệu chủ yếu tiếng Trung; cần MySQL, Redis (chỉ mall-admin) và thêm Elasticsearch, RabbitMQ, MongoDB cho đầy đủ; frontend ở repo riêng mall-admin-web, mall-app-web. |
| [`pallets/flask`](https://github.com/pallets/flask) | 75.381 | BSD-3-Clause | Framework ứng dụng web WSGI gọn nhẹ cho Python, xây quanh Werkzeug và Jinja. | Không ép phụ thuộc hay cấu trúc dự án; hệ sinh thái extension cộng đồng lớn; do tổ chức Pallets duy trì, nhánh chính đang ở 3.2.0.dev. | `flask run` | Cần Python 3.11+ (theo pyproject.toml). |
| [`strapi/strapi`](https://github.com/strapi/strapi) | 73.510 | MIT (Expat) cho Community Edition; mã trong thư mục ee/ theo giấy phép Enterprise riêng (packages/core/admin/ee/LICENSE); người có tài khoản Strapi Cloud theo điều khoản cloud | Headless CMS mã nguồn mở tự host bằng JavaScript/TypeScript, sinh API REST và GraphQL từ mô hình nội dung. | Content-Type Builder thiết kế mô hình trực quan không cần code; tự sinh API REST và GraphQL, có Roles và Permissions, Media Library, i18n, Draft và Publish; hỗ trợ SQLite, PostgreSQL, MySQL, MariaDB. | `npx create-strapi@latest my-project` | Tính năng trong ee/ cần giấy phép Enterprise; không có ảnh Docker chính thức; Strapi Cloud là dịch vụ trả phí. |
| [`protocolbuffers/protobuf`](https://github.com/protocolbuffers/protobuf) | 72.179 | BSD 3-Clause (Google Inc.); kèm điều khoản: mã do protoc sinh ra thuộc chủ sở hữu file .proto đầu vào | Protocol Buffers: cơ chế tuần tự hoá dữ liệu có cấu trúc trung lập ngôn ngữ và nền tảng của Google, gồm trình biên dịch protoc và runtime cho nhiều ngôn ngữ. | Runtime trong repo cho C++, Java, Python, Objective-C, C#, Ruby, PHP, Rust (Go, Dart, JavaScript ở repo riêng); hỗ trợ Bazel Bzlmod (Bazel 8+) và CMake; có bảng điểm OpenSSF Scorecard và file version.json theo dõi phiên bản từng ngôn ngữ | `Tải protoc-$VERSION-$PLATFORM.zip từ trang GitHub Releases; Bazel: bazel_dep(name = "protobuf", version = <VERSION>)` | README khuyên dùng bản phát hành, nhánh main có thể hỏng; C++ cần build từ mã nguồn |
| [`expressjs/express`](https://github.com/expressjs/express) | 69.801 | MIT | Framework web tối giản, không áp đặt cấu trúc cho Node.js, cung cấp định tuyến và tiện ích HTTP. | Phiên bản 5.3.0 trong package.json; định tuyến mạnh, hỗ trợ hơn 14 template engine và content negotiation; có thư mục examples và bộ test, huy hiệu OpenSSF Scorecard | `npm install express` | Cần Node.js 18 trở lên |
| [`jeecgboot/JeecgBoot`](https://github.com/jeecgboot/JeecgBoot) | 48.504 | Apache-2.0 kèm điều khoản bổ sung cuối file LICENSE: không được dùng phần mềm để phát triển phần mềm có thể bị coi là cạnh tranh với nó | Nền tảng low-code AI cho Java (Spring Boot 4, Spring Cloud Alibaba, MyBatis-Plus) và Vue3, sinh mã CRUD, biểu mẫu, quy trình, báo cáo và ứng dụng AI. | Phiên bản 3.9.6 phát hành 2026-11-05; tích hợp sẵn RBAC, phân quyền dữ liệu, đa tenant, BPM Flowable, báo cáo JimuReport; hỗ trợ chạy đơn khối và vi dịch vụ qua docker-compose | `./start-docker-compose.sh` | Cần Docker, docker-compose, Maven, pnpm; tài khoản mặc định admin/123456 phải đổi; điều khoản cấm phát triển phần mềm cạnh tranh trong LICENSE; README đề nghị không mạo danh thương hiệu JeecgBoot; tính năng AI cần khoá API mô hình lớn hoặc Ollama |
| [`appsmithorg/appsmith`](https://github.com/appsmithorg/appsmith) | 41.264 | Apache-2.0 | Nền tảng low-code mã nguồn mở để xây ứng dụng nội bộ như dashboard, trang quản trị, công cụ tự động hoá IT. | Hỗ trợ cài qua Docker (khuyến nghị), Kubernetes và AWS AMI; mã gồm client và server trong thư mục app; có bản Cloud và tài liệu, hướng dẫn, mẫu ứng dụng | `Docker theo hướng dẫn docs.appsmith.com (image appsmith/appsmith-ce)` | Tự host bằng Docker/Kubernetes hoặc dùng tài khoản Appsmith Cloud |
| [`directus/directus`](https://github.com/directus/directus) | 38.747 | Monospace Sustainable Core License 1.0 (MSCL-1.0-GPL), source-available; cấm Competing Use và vượt cơ chế license key; tự chuyển sang GPL-3.0 sau 4 năm kể từ ngày phát hành | Lớp backend bọc bất kỳ cơ sở dữ liệu SQL nào, tự sinh REST và GraphQL API, kèm Studio quản trị trực quan và MCP server cho tác tử AI. | Hỗ trợ Postgres, MySQL, MariaDB, MS SQL, SQLite, OracleDB, CockroachDB; phân quyền theo chính sách tới mức trường; có SDK, Dockerfile và nhiều storage driver (S3, GCS, Azure, Cloudinary, Supabase) | `docker compose (repo có Dockerfile và docker-compose.yml) hoặc Directus Cloud` | Giấy phép không phải OSI: miễn phí cho tổ chức dưới 5 triệu USD doanh thu năm và 50 nhân viên qua Open Innovation Grant; vượt ngưỡng dùng tính năng nâng cao cần giấy phép thương mại; không được dùng để cạnh tranh với dịch vụ thương mại của Monospace |
| [`medusajs/medusa`](https://github.com/medusajs/medusa) | 37.296 | MIT cho phần lớn repo; tài liệu Enterprise Edition (RBAC, SSO, liệt kê trong ENTERPRISE-LICENSE.md) là độc quyền, cần hợp đồng thương mại với MedusaJS, Inc. | Nền tảng thương mại điện tử mã nguồn mở có framework tuỳ biến, dùng để xây cửa hàng B2B/DTC, marketplace, POS. | Monorepo Yarn với các Commerce Module (product, cart, order, pricing, payment...); provider có sẵn cho Stripe, S3, SendGrid, Redis, OIDC; có Admin dashboard, design system Medusa UI và bộ integration test trên PostgreSQL | `npx create-medusa-app@latest my-medusa-store` | Cần Node.js v22.22.0 trở lên và PostgreSQL; bật cờ tính năng Enterprise đồng nghĩa khẳng định có hợp đồng thương mại; không được dùng RBAC/SSO khi chưa có giấy phép |
| [`zeromicro/go-zero`](https://github.com/zeromicro/go-zero) | 33.431 | MIT | Framework web và RPC cho Go với nhiều thực hành kỹ thuật tích hợp sẵn, kèm công cụ sinh mã goctl. | Tích hợp sẵn kiểm soát timeout chuỗi, rate limit, circuit breaker và load shedding thích ứng; goctl sinh mã Go, iOS, Android, Kotlin, Dart, TypeScript, JavaScript từ file .api; có gói mcp và có trong CNCF Landscape | `go get -u github.com/zeromicro/go-zero; go install github.com/zeromicro/go-zero/tools/goctl@latest` |  |
| [`python-telegram-bot/python-telegram-bot`](https://github.com/python-telegram-bot/python-telegram-bot) | 29.602 | LGPL-3.0 (repo kèm LICENSE GPLv3, LICENSE.lesser và LICENSE.dual) | Thư viện Python thuần, bất đồng bộ cho Telegram Bot API, kèm các lớp cấp cao trong telegram.ext để viết bot. | Hỗ trợ đầy đủ Telegram Bot API 10.0; tương thích Python 3.11+ và đã thử với free threading 3.14; có các gói phụ tuỳ chọn như job-queue, webhooks, rate-limiter | `pip install python-telegram-bot --upgrade` | Cần token bot Telegram; bản sửa đổi hoặc liên kết tĩnh phải phát hành dưới LGPL-3, ứng dụng chỉ dùng thư viện thì không bắt buộc |
| [`go-kratos/kratos`](https://github.com/go-kratos/kratos) | 26.032 | MIT | Framework Go nhẹ để xây vi dịch vụ cloud-native, cung cấp API cho transport, middleware, registry, cấu hình, log và sinh mã. | Phát triển API-first với Protobuf, sinh mã HTTP/gRPC; log dựa trên log/slog chuẩn kèm mở rộng OpenTelemetry; hệ contrib cho registry, config store, middleware, quan sát | `go install github.com/go-kratos/kratos/cmd/kratos/v3@latest` | Cần Go 1.25 trở lên, protoc và protoc-gen-go |
| [`flipped-aurora/gin-vue-admin`](https://github.com/flipped-aurora/gin-vue-admin) | 25.139 | Apache-2.0 | Khung hệ thống quản trị full-stack tách frontend/backend dựa trên Gin (Go) và Vue 3, có JWT, menu động, Casbin, trình sinh form và sinh mã. | Tích hợp xác thực JWT, phân quyền Casbin, định tuyến và menu động; có trình sinh mã và form generator; có tài liệu trực tuyến, video hướng dẫn và trang demo | `cd server && go generate && go build -o server main.go; cd web && npm install && npm run serve` | Cần Go >= 1.26.10 và Node; có bản trả phí (Licensed Edition) cho tính năng mở rộng và hỗ trợ thương mại; phải thay khoá Qiniu mẫu trong cấu hình |
| [`nocobase/nocobase`](https://github.com/nocobase/nocobase) | 24.955 | NocoBase License Agreement (LICENSE.txt, cập nhật 16/11/2026): bản Community dựa trên Apache-2.0 (LICENSE-APACHE.txt) kèm điều khoản bổ sung có hiệu lực ưu tiên; tính năng bản Commercial không theo Apache-2.0 | Nền tảng mã nguồn mở để xây dựng, vận hành và phát triển hệ thống nghiệp vụ cùng AI; agent viết mã, NocoBase cung cấp nền tảng (quyền, workflow, phê duyệt, tệp) và quản trị. | Có sẵn khối nền phân quyền, workflow, tệp cho ứng dụng nghiệp vụ; khởi tạo được bằng Skill cho coding agent hoặc bằng lệnh pnpm với SQLite không cần máy chủ CSDL; README có bản dịch nhiều ngôn ngữ kể cả tiếng Việt | `pnpm create @nocobase/app@beta my-app --template-tag=beta` | Cần Node.js 24+ và pnpm 11, Windows dùng WSL; quick start trong README dùng bản beta (NocoBase 3); giấy phép cấm xoá/sửa dòng chữ "AI + NocoBase" kèm liên kết ở góc giao diện ứng dụng và cấm phát hành công khai plugin trùng tính năng bản Commercial |
| [`wechaty/wechaty`](https://github.com/wechaty/wechaty) | 23.589 | Apache License 2.0 (kèm file NOTICE) | SDK RPA hội thoại để viết chatbot một lần chạy trên nhiều nền tảng nhắn tin (WeChat, WhatsApp, Telegram, Line…) thông qua các puppet provider. | Chatbot tối thiểu chỉ 6 dòng JavaScript; chọn giao thức qua biến môi trường WECHATY_PUPPET; có ảnh Docker chạy trực tiếp bot.js hoặc bot.ts | `npm install wechaty` | Một số giao thức (puppet) ngoài Web cần token, README hướng dẫn xin token qua wiki; tự động hoá tài khoản nhắn tin có thể vướng điều khoản dịch vụ của nền tảng (chưa xác minh trong README) |
| [`go-playground/validator`](https://github.com/go-playground/validator) | 20.239 | MIT | Thư viện Go kiểm tra hợp lệ giá trị cho struct và từng trường dựa trên tag. | Hỗ trợ kiểm tra chéo trường và chéo struct, đi sâu vào slice, array, map (cả khoá và giá trị); thông báo lỗi tuỳ biến có i18n với thư mục translations; là validator mặc định của framework gin | `go get github.com/go-playground/validator/v10` |  |
| [`APIJSON/APIJSON`](https://github.com/APIJSON/APIJSON) | 18.395 | Apache License 2.0 (file LICENSE ghi bản quyền APIJSON group, kèm phần cảm ơn và danh sách giấy phép phụ thuộc) | Giao thức truyền thông dựa trên JSON kèm thư viện ORM cho Java, cho phép client tự mô tả dữ liệu cần lấy để giảm việc viết API backend. | Một request lấy được nhiều loại dữ liệu, hỗ trợ CRUD, tìm kiếm mờ, gọi hàm từ xa; README liệt kê demo cho nhiều CSDL như MySQL, PostgreSQL, SQL Server, Oracle, ClickHouse, DuckDB; phát hành qua JitPack, phiên bản 8.4.0 trong pom.xml | `Thêm repository jitpack.io và dependency APIJSON vào pom.xml (theo README)` |  |
| [`ory/hydra`](https://github.com/ory/hydra) | 17.671 | Apache License 2.0 | Máy chủ OAuth 2.0 và nhà cung cấp OpenID Connect, kết nối với hệ thống định danh sẵn có qua ứng dụng login và consent riêng. | Được chứng nhận OpenID Certified; không tự quản lý người dùng nên ghép được với Ory Kratos hoặc hệ thống riêng; hỗ trợ PostgreSQL, MySQL, CockroachDB và có nhiều file quickstart docker-compose | `Cài Ory CLI rồi chạy ory create project (quickstart) hoặc tự host theo hướng dẫn cài đặt` | README khuyến nghị hệ thống quan trọng dùng Ory Enterprise License để có bản vá CVE có SLA và bản build doanh nghiệp; telemetry ẩn danh bật mặc định, tắt được |
| [`apitable/apitable`](https://github.com/apitable/apitable) | 15.669 | GNU AGPL v3 (kèm LICENSING.md và thư mục licenses) | Nền tảng cơ sở dữ liệu dạng bảng tính trực quan, API-oriented, mã nguồn mở thay thế Airtable với cộng tác thời gian thực. | Cộng tác thời gian thực bằng thuật toán Operational Transformation; 7 kiểu view gồm Grid, Gallery, Kanban, Gantt, Calendar; có phân quyền cột, hàng, thư mục và hệ widget mở rộng | `Tải https://apitable.github.io/install.sh bằng curl rồi chạy bằng bash (docker compose)` | Cần Docker và docker-compose v2; theo LICENSING.md nếu gỡ logo "Powered by APITable" trên trang nhúng thì phải phát hành ứng dụng nhúng theo AGPL (hoặc mua Enterprise); đóng góp phải ký CLA |
| [`casdoor/casdoor`](https://github.com/casdoor/casdoor) | 14.881 | Apache License 2.0 | Máy chủ đăng nhập một lần (SSO) và xác thực có bảng điều khiển web, là nhà cung cấp định danh đầy đủ lưu người dùng và cấp token. | Hỗ trợ OAuth 2.0, OIDC, SAML 2.0, CAS, LDAP, SCIM 2.0, WebAuthn trên cùng một thư mục người dùng; phân quyền theo chính sách bằng Casbin (ACL, RBAC, ABAC); tự host bằng một binary Go cộng CSDL, có SDK cho Go, Java, Python, Node.js, .NET, PHP, Rust | `docker run -p 8000:8000 casbin/casdoor-all-in-one` | Ảnh all-in-one chỉ để thử, không dùng production (dữ liệu mất cùng container); tài khoản mặc định admin/123 cần đổi |

**Chưa thêm (2 repo, giữ trong file dữ liệu):** `Avaiga/taipy` (commit cuối 7/5/2026); `amplication/amplication` (commit cuối 2/4/2026).

#### 6c.5.10 Framework Frontend

Đọc mã 6 repo, giữ 6.

| Repo | ★ (18/11/2026) | Giấy phép | Làm gì | Điểm mạnh (đọc mã) | Cài | Điều kiện dùng |
|---|---|---|---|---|---|---|
| [`GrapesJS/grapesjs`](https://github.com/GrapesJS/grapesjs) | 26.418 | BSD 3-Clause (Copyright Artur Arseniev) | Framework trình dựng web kéo thả mã nguồn mở để tạo template HTML cho website, newsletter, ứng dụng di động, thường nhúng vào CMS. | Có Block Manager, Style Manager, Asset Manager, Code Viewer và lưu trữ cục bộ/từ xa; phân phối qua npm, UNPKG và CDNJS; monorepo có gói webmcp thử nghiệm cho agent AI thao tác editor | `npm i grapesjs` |  |
| [`handsontable/handsontable`](https://github.com/handsontable/handsontable) | 22.084 | Giấy phép riêng của Handsoncode (không phải mã nguồn mở): dùng cá nhân hoặc đánh giá theo handsontable-non-commercial-license.pdf; dùng thương mại cần thoả thuận giấy phép trả phí; cấm dùng để phát triển phần mềm cạnh tranh | Thành phần lưới dữ liệu JavaScript giao diện giống bảng tính, dùng với JavaScript/TypeScript, React, Angular, Vue để nhập, sửa, kiểm hợp lệ và xử lý dữ liệu. | README liệt kê khoảng 400 công thức dựng sẵn, ảo hoá hàng, lọc, sắp xếp, định dạng có điều kiện; hỗ trợ IME, đa ngôn ngữ, RTL và nhắm WCAG 2.2 AA; có wrapper React, Angular, Vue3 trong thư mục wrappers | `npm install handsontable` | Cần khoá giấy phép (licenseKey); dùng thương mại phải mua giấy phép; bản dùng thử chỉ để đánh giá ngoài production, hết hạn thì lưới bị chặn; dự án phi thương mại phải xin giấy phép miễn phí; đóng góp cần ký CLA |
| [`diegomura/react-pdf`](https://github.com/diegomura/react-pdf) | 16.858 | MIT | Trình render React để tạo file PDF trên trình duyệt và máy chủ bằng các thành phần Document, Page, View, Text. | Render được trong DOM qua PDFViewer và ghi file trên Node qua ReactPDF.render; có StyleSheet kiểu flexbox; monorepo nhiều gói trong packages, phát hành gói @react-pdf/renderer | `yarn add @react-pdf/renderer` |  |
| [`udecode/plate`](https://github.com/udecode/plate) | 16.712 | MIT (mặc định cho repo; gói có file LICENSE riêng thì theo file đó, ví dụ packages/cli cũng là MIT) | Framework trình soạn thảo văn bản giàu định dạng (rich-text) cho React, kèm các mẫu khởi đầu và tài liệu tại platejs.org. | Có mẫu playground có AI và mẫu tối giản; repo chứa gói platejs, plitejs (runtime lõi mô hình tài liệu, giao dịch) và cli; có tài liệu tiếng Trung trong tooling/cn |  | Mẫu Notion-like (Potion) có backend nằm ở pro.platejs.org, chưa xác minh điều kiện sử dụng |
| [`wasp-lang/open-saas`](https://github.com/wasp-lang/open-saas) | 16.350 | MIT | Mẫu khởi đầu SaaS miễn phí dựng trên Wasp (React, Node.js, Prisma), kèm xác thực, thanh toán, trang quản trị, blog/tài liệu Astro. | Tích hợp sẵn Stripe, Polar.sh hoặc Lemon Squeezy, gửi email SendGrid/Mailgun/SMTP, upload AWS S3; có test đầu-cuối Playwright trong template/e2e-tests; triển khai một lệnh lên Railway hoặc Fly.io | `npm i -g @wasp.sh/wasp-cli && wasp new -t saas` | Các tích hợp cần tài khoản/khoá dịch vụ ngoài (Stripe/Polar/Lemon Squeezy, OpenAI, AWS S3, SendGrid/Mailgun, Plausible/Google Analytics); Wasp CLI chạy trên macOS, Linux hoặc Windows qua WSL |
| [`millionco/react-doctor`](https://github.com/millionco/react-doctor) | 15.154 | Modified MIT License (Million Software, Inc.): MIT kèm điều khoản cần xin phép bằng văn bản trước khi dùng mã làm dữ liệu huấn luyện/tinh chỉnh/đánh giá AI hoặc bán/cung cấp dưới dạng dịch vụ trả phí có giá trị chủ yếu từ phần mềm | Công cụ quét tĩnh có tính tất định cho dự án React, báo lỗi về state/effect, hiệu năng, kiến trúc, bảo mật, a11y và khả năng bảo trì. | Hỗ trợ Next.js, Vite, Astro, TanStack, React Native, Expo; có lệnh cài skill cho agent và lệnh cài quét CI cho từng PR; có plugin eslint và oxlint trong packages | `npx react-doctor@latest` | CLI thu thập báo cáo crash và dữ liệu sử dụng ẩn danh (tắt bằng --no-telemetry); giấy phép cấm dùng làm dữ liệu huấn luyện AI hoặc bán dạng SaaS khi chưa được phép |

#### 6c.5.11 Giám sát, CSDL & Phân tích

Đọc mã 22 repo, giữ 21.

| Repo | ★ (18/11/2026) | Giấy phép | Làm gì | Điểm mạnh (đọc mã) | Cài | Điều kiện dùng |
|---|---|---|---|---|---|---|
| [`louislam/uptime-kuma`](https://github.com/louislam/uptime-kuma) | 94.567 | MIT | Công cụ giám sát uptime tự host, dễ dùng, theo dõi HTTP(s), TCP, ping, DNS, WebSocket, container Docker và có trang trạng thái. | Thông báo qua Telegram, Discord, Slack, email và hơn 90 dịch vụ; chu kỳ kiểm tra 20 giây, nhiều trang trạng thái gắn tên miền riêng; hỗ trợ 2FA, proxy, thông tin chứng chỉ | `docker run -d --restart=always -p 3001:3001 -v uptime-kuma:/app/data --name uptime-kuma louislam/uptime-kuma:2` | Không hỗ trợ hệ thống file NFS; không hỗ trợ FreeBSD/OpenBSD/NetBSD, Replit/Heroku; README cảnh báo uptimekuma.co không phải trang chính thức |
| [`netdata/netdata`](https://github.com/netdata/netdata) | 81.458 | GPL-3.0 (file LICENSE; README ghi Agent là GPLv3+); Netdata UI là mã đóng theo giấy phép NCUL1, Netdata Cloud mã đóng có bậc miễn phí và trả phí | Nền tảng quan sát full-stack thu thập metric theo từng giây, log, trace, luồng mạng, có cảnh báo và học máy, chạy trên Linux, macOS, FreeBSD, Windows, Kubernetes. | Hơn 800 tích hợp gồm OpenTelemetry, SNMP, NetFlow/IPFIX/sFlow, IPMI; Agent có máy chủ MCP tích hợp; mở rộng từ một nút tới hàng trăm nghìn nút qua kiến trúc Parent |  | Telemetry ẩn danh bật mặc định (tắt bằng --disable-telemetry hoặc file opt-out); giao diện UI mã đóng giấy phép NCUL1; tính năng Cloud (SSO, RBAC, truy cập từ xa) cần tài khoản Netdata Cloud |
| [`elastic/elasticsearch`](https://github.com/elastic/elasticsearch) | 78.816 | Mặc định ba giấy phép tuỳ chọn AGPL-3.0-only, SSPL v1, Elastic License 2.0; một số file theo giấy phép tương thích Apache 2.0; mã trong x-pack chỉ theo Elastic License 2.0 | Máy tìm kiếm và phân tích phân tán, kho dữ liệu và cơ sở dữ liệu vector, dùng cho full-text search, log, metric, APM, RAG. | Hỗ trợ tìm kiếm vector và tìm kiếm gần thời gian thực trên dữ liệu lớn; có script start-local dựng Elasticsearch và Kibana bằng Docker kèm API key; mã nguồn Java build bằng Gradle với bộ test và benchmarks trong repo | `curl -fsSL https://elastic.co/start-local rồi chuyển cho sh (script start-local)` | Script start-local chỉ cho phát triển/thử nghiệm (tắt HTTPS), cần Docker (Windows cần WSL); bản cục bộ kèm trial 1 tháng rồi về bậc Basic; tính năng x-pack chịu Elastic License 2.0 |
| [`grafana/grafana`](https://github.com/grafana/grafana) | 77.975 | AGPL-3.0-only (mặc định); một số thư mục như packages/grafana-data, grafana-ui, grafana-runtime, packaging theo Apache-2.0 theo LICENSING.md | Nền tảng giám sát và quan sát mã nguồn mở để truy vấn, trực quan hoá, cảnh báo trên metric và log từ nhiều nguồn dữ liệu. | Dashboard động với biến template, trộn nhiều nguồn dữ liệu trong một biểu đồ; cảnh báo gửi tới Slack, PagerDuty, OpsGenie; có bản demo trực tiếp tại play.grafana.org |  | AGPL-3.0: cung cấp bản sửa đổi qua mạng phải công bố mã nguồn |
| [`redis/redis`](https://github.com/redis/redis) | 77.671 | Từ Redis 8: tuỳ chọn một trong RSALv2, SSPLv1 hoặc AGPLv3; Redis 7.2 trở về trước theo BSD-3-Clause | Kho dữ liệu trong bộ nhớ dùng làm cache, máy chủ cấu trúc dữ liệu, message broker, cơ sở dữ liệu tài liệu và truy vấn vector. | Hỗ trợ JSON, time series, Bloom filter, Query Engine với tìm kiếm vector và full-text; có streams, pub/sub, giao dịch và scripting; có API module để mở rộng lệnh | `docker run -d -p 6379:6379 redis:latest` | Giấy phép RSALv2/SSPLv1/AGPLv3 có hạn chế khi cung cấp dạng dịch vụ; dùng tên/logo Redis phải theo chính sách thương hiệu; build đầy đủ module cần CMake 3.25–3.31.6, LLVM 21, Rust |
| [`meilisearch/meilisearch`](https://github.com/meilisearch/meilisearch) | 59.889 | MIT AND OpenLDAP AND BUSL-1.1 (SPDX trong LICENSE): phần lớn MIT; connector LMDB (heed) thêm OpenLDAP 2.8; phần Enterprise Edition theo Business Source License 1.1 (LICENSE-EE), chỉ dùng phi sản xuất, chuyển sang MIT sau 4 năm | Công cụ tìm kiếm viết bằng Rust cho tìm kiếm toàn văn, ngữ nghĩa và lai, nhúng vào ứng dụng và website qua REST API. | Chịu lỗi chính tả, lọc, faceting, sắp xếp và đồng nghĩa có sẵn; tìm kiếm khi gõ trả kết quả dưới 50 ms theo README; tự host bằng một lệnh Docker hoặc binary | `docker run -it --rm -p 7700:7700 -v $(pwd)/meili_data:/meili_data getmeili/meilisearch:latest` | Bản Enterprise Edition (sharding và tính năng nâng cao) cần thỏa thuận thương mại khi dùng production (BUSL-1.1); bản Community MIT dùng tự do |
| [`apache/airflow`](https://github.com/apache/airflow) | 47.520 | Apache License 2.0 (kèm file NOTICE) | Nền tảng viết, lập lịch và giám sát workflow (Dag) bằng mã Python; scheduler chạy task trên các worker theo phụ thuộc. | Workflow định nghĩa bằng mã nên quản lý phiên bản và test được; có giao diện web trực quan hoá pipeline và CLI phong phú; dự án Apache có bộ constraints cố định để cài lặp lại được | `pip install 'apache-airflow==3.4.0' --constraint "https://raw.githubusercontent.com/apache/airflow/constraints-3.4.0/constraints-3.10.txt"` | README khuyên cài kèm file constraints vì pip install trần có thể hỏng |
| [`SigNoz/signoz`](https://github.com/SigNoz/signoz) | 32.673 | MIT (Expat) cho phần lớn mã; thư mục ee/ và cmd/enterprise/ theo SigNoz Enterprise License (ee/LICENSE) — chỉ dùng production khi có giấy phép Enterprise hợp lệ | Nền tảng observability mã nguồn mở dựa trên OpenTelemetry, gộp logs, metrics, traces, cảnh báo và dashboard một chỗ. | Gộp APM, quản lý log, metrics, distributed tracing và cảnh báo trong một sản phẩm; truy vấn bằng Query Builder, PromQL hoặc ClickHouse SQL; tự host bằng Docker, Kubernetes hoặc Linux | `Xem https://signoz.io/docs/install/self-host/ (Docker, Kubernetes, Linux)` | Mã trong ee/ cần giấy phép SigNoz Enterprise để dùng production; trợ lý Noz chỉ có trên SigNoz Cloud (README) |
| [`typesense/typesense`](https://github.com/typesense/typesense) | 27.153 | GNU General Public License v3.0 (LICENSE.txt) | Công cụ tìm kiếm nhanh, chịu lỗi chính tả viết bằng C++, tự giới thiệu là phương án mở thay Algolia và dễ dùng hơn Elasticsearch. | Viết bằng C++ cho tìm kiếm tức thời dưới 50 ms; có chịu lỗi chính tả, faceting, lọc, sắp xếp và tìm kiếm ngữ nghĩa/lai; nhiều demo trực tiếp trên tập dữ liệu lớn (32 triệu bài hát) | `docker run -p 8108:8108 -v/tmp/data:/data typesense/typesense:29.0 --data-dir /data --api-key=<khóa>` | GPL-3.0 (copyleft) khi phân phối bản sửa đổi |
| [`apache/skywalking`](https://github.com/apache/skywalking) | 25.010 | Apache License 2.0 (kèm file NOTICE) | Hệ thống APM cho microservice và kiến trúc cloud native: distributed tracing, giám sát và chẩn đoán hệ phân tán. | Có agent cho Java, .Net Core, PHP, NodeJS, Golang, Lua, Rust, C++, Python và JavaScript phía client; agent Rover dùng eBPF để giám sát Kubernetes; nhận dữ liệu từ Zipkin, OpenTelemetry, Prometheus, Zabbix, Fluentd | `Tải bản phát hành tại https://skywalking.apache.org/downloads/` |  |
| [`dolthub/dolt`](https://github.com/dolthub/dolt) | 24.933 | Apache License 2.0 | Cơ sở dữ liệu SQL tương thích MySQL có quản lý phiên bản kiểu Git: fork, clone, branch, merge, push, pull trên bảng dữ liệu. | CLI có cùng lệnh như git (commit, branch, merge, diff, blame theo hàng); chức năng phiên bản dùng được qua bảng hệ thống, hàm và thủ tục SQL; chạy làm MySQL server bằng dolt sql-server | `brew install dolt (Linux: script install.sh từ GitHub Releases, xem README)` |  |
| [`jaegertracing/jaeger`](https://github.com/jaegertracing/jaeger) | 23.422 | Apache License 2.0 (kèm file NOTICE) | Nền tảng distributed tracing do Uber tạo và tặng CNCF, nhận trace qua OTLP và có giao diện truy vấn. | Dự án CNCF đã graduated (10/2019); Jaeger v2 dựa trên thành phần OpenTelemetry Collector; có chính sách bảo đảm tương thích cấu hình với thời gian ân hạn ít nhất 3 tháng | `docker run --rm --name jaeger -p 16686:16686 -p 4317:4317 -p 4318:4318 jaegertracing/jaeger:latest` |  |
| [`openobserve/openobserve`](https://github.com/openobserve/openobserve) | 23.096 | GNU Affero General Public License v3.0 | Nền tảng observability cloud native viết bằng Rust cho logs, metrics, traces, RUM và quan sát AI/LLM, định vị thay Datadog, Splunk, Elasticsearch. | Triển khai một binary duy nhất; lưu trữ cột Parquet trên S3 (README nêu chi phí lưu trữ thấp hơn 140 lần so với Elasticsearch); truy vấn bằng SQL và PromQL, gốc OpenTelemetry | `docker run -d --name openobserve -v $PWD/data:/data -p 5080:5080 -e ZO_ROOT_USER_EMAIL=... -e ZO_ROOT_USER_PASSWORD=... public.ecr.aws/zinclabs/openobserve:latest` | AGPL-3.0 (copyleft cả khi cung cấp qua mạng); có Enterprise Edition riêng (điều khoản chưa xác minh) |
| [`vectordotdev/vector`](https://github.com/vectordotdev/vector) | 22.895 | Mozilla Public License 2.0 | Pipeline dữ liệu observability hiệu năng cao viết bằng Rust, chạy như agent hoặc aggregator để thu, biến đổi và định tuyến logs và metrics. | Viết bằng Rust với mục tiêu thiết kế chính là độ tin cậy; có ngôn ngữ biến đổi VRL và lệnh vector validate, vector test, vector top, vector tap; do nhóm Community Open Source Engineering của Datadog duy trì | `Xem https://vector.dev/docs/setup/installation/` |  |
| [`elastic/kibana`](https://github.com/elastic/kibana) | 21.382 | Mặc định ba giấy phép AGPL-3.0-only, SSPL v1 và Elastic License 2.0 (chọn một); một số file Apache 2.0 tương thích theo header; mã chỉ theo Elastic License 2.0 nằm trong thư mục x-pack | Giao diện để truy vấn, phân tích, trực quan hoá và quản lý dữ liệu lưu trong Elasticsearch. | Là giao diện chính thức của Elastic Stack; README có bảng tương thích phiên bản Kibana–Elasticsearch rõ ràng; có bản tải sẵn và bản hosted trên Elastic Cloud | `Tải tại https://www.elastic.co/downloads/kibana` | Cần Elasticsearch cùng phiên bản major; mã x-pack chỉ theo Elastic License 2.0 |
| [`VictoriaMetrics/VictoriaMetrics`](https://github.com/VictoriaMetrics/VictoriaMetrics) | 18.126 | Apache-2.0 (bản single-node và cluster); tính năng Enterprise/LTS cần giấy phép thương mại (có bản dùng thử miễn phí) | Cơ sở dữ liệu chuỗi thời gian và giải pháp giám sát nhanh, tiết kiệm, mở rộng được; dùng làm lưu trữ dài hạn hoặc thay thế Prometheus/Graphite trong Grafana. | Hỗ trợ PromQL và MetricsQL; nhận dữ liệu qua Prometheus remote write, InfluxDB line protocol, Graphite, OpenTSDB, DataDog, NewRelic, OpenTelemetry; có bản single-node và cluster cùng bộ công cụ vmagent, vmalert, vmauth, vmbackup | `docker run victoriametrics/victoria-metrics (ảnh Docker Hub/Quay hoặc binary từ GitHub Releases)` | Tính năng Enterprise và bản LTS cần giấy phép thương mại |
| [`RyanCodrai/turbovec`](https://github.com/RyanCodrai/turbovec) | 17.499 | MIT | Chỉ mục vector chạy trong tiến trình cho Python và Rust, nén mỗi chiều còn 2 hoặc 4 bit theo thuật toán TurboQuant của Google Research và tìm kiếm trực tiếp trên dạng nén bằng nhân SIMD. | Không cần bước huấn luyện, thêm/xoá vector trực tiếp; sync(path) ghi tăng dần, an toàn khi crash; có tích hợp LangChain, LlamaIndex, Haystack, Agno và hỗ trợ lọc theo allowlist id | `pip install turbovec (Rust: cargo add turbovec)` | Quét toàn bộ (không phải chỉ mục đồ thị), lượng tử hoá mất mát; số chiều phải là bội số của 8 và tối đa 16.384; là thư viện, không có máy chủ mạng |
| [`openzipkin/zipkin`](https://github.com/openzipkin/zipkin) | 17.475 | Apache-2.0 | Hệ thống truy vết phân tán, thu thập và tra cứu dữ liệu thời gian để gỡ lỗi độ trễ trong kiến trúc dịch vụ, kèm giao diện web và sơ đồ phụ thuộc. | Nhận dữ liệu qua HTTP, Kafka, gRPC, RabbitMQ, ActiveMQ, Pulsar; lưu trong bộ nhớ, Cassandra hoặc Elasticsearch; có bản slim, ảnh Docker và công thức Homebrew | `docker run -d -p 9411:9411 openzipkin/zipkin` | Máy chủ cần JRE 17+; ứng dụng phải được gắn thư viện instrumentation |
| [`alibaba/zvec`](https://github.com/alibaba/zvec) | 16.261 | Apache-2.0 | Cơ sở dữ liệu vector nhúng trong tiến trình, nhẹ và nhanh, nhúng trực tiếp vào ứng dụng; đã dùng thực tế trong Alibaba Group. | Hỗ trợ vector dày và thưa, full-text search và hybrid search trong một truy vấn; WAL bảo đảm bền dữ liệu khi crash; SDK Python, Node.js, Java và chạy trên máy chủ, desktop, Android, iOS | `pip install zvec` | Python 64-bit 3.10–3.14, Java 8+; ghi chỉ cho một tiến trình tại một thời điểm |
| [`apache/doris`](https://github.com/apache/doris) | 16.238 | Apache-2.0; README lưu ý một số phụ thuộc bên thứ ba không tương thích Apache 2.0, cần tắt vài tính năng để tuân thủ (xem thirdparty/LICENSE.txt) | Cơ sở dữ liệu phân tích và tìm kiếm thời gian thực kiến trúc MPP thuộc Apache: phân tích SQL nhanh, tăng tốc truy vấn lakehouse và tìm kiếm hybrid trên dữ liệu có cấu trúc, văn bản, vector. | Nạp dữ liệu dạng luồng và truy vấn dưới một giây ở độ đồng thời cao; truy vấn trực tiếp Iceberg, Delta Lake, Hudi; có Kubernetes Operator để triển khai |  | Một số phụ thuộc bên thứ ba không tương thích Apache 2.0, cần tắt tính năng tương ứng nếu muốn tuân thủ hoàn toàn |
| [`open-metadata/OpenMetadata`](https://github.com/open-metadata/OpenMetadata) | 15.805 | Apache-2.0 | Nền tảng danh mục dữ liệu và quản trị metadata mã nguồn mở, gom lineage, chất lượng dữ liệu, sở hữu, glossary, hợp đồng dữ liệu thành đồ thị tri thức làm ngữ cảnh cho người dùng và agent AI. | Hơn 130 connector; có lineage mức cột, kiểm thử chất lượng dữ liệu và profiling; cung cấp máy chủ MCP, API, SDK Python | `pip install "openmetadata-ingestion" (máy chủ: theo Quickstart Guide trên docs.open-metadata.org)` | Tính năng quản lý doanh nghiệp, AI Studio, hỗ trợ thương mại thuộc sản phẩm Collate trả phí |

**Chưa thêm (1 repo, giữ trong file dữ liệu):** `xerj-org/xerj` (còn thử nghiệm: chỉ có bản release candidate (v1.0.0-rc.101), chưa có bản 1.0 ổn định).

#### 6c.5.12 Học AI & Machine Learning

Đọc mã 23 repo, giữ 21.

| Repo | ★ (18/11/2026) | Giấy phép | Làm gì | Điểm mạnh (đọc mã) | Cài | Điều kiện dùng |
|---|---|---|---|---|---|---|
| [`microsoft/ML-For-Beginners`](https://github.com/microsoft/ML-For-Beginners) | 92.302 | MIT | Giáo trình 12 tuần, 26 bài về học máy cổ điển của Microsoft Cloud Advocates, chủ yếu dùng Scikit-learn. | Mỗi bài có quiz trước và sau, hướng dẫn, lời giải và bài tập; dạy theo dự án với dữ liệu nhiều nơi trên thế giới; có bản dịch sang hơn 50 ngôn ngữ |  |  |
| [`datawhalechina/hello-agents`](https://github.com/datawhalechina/hello-agents) | 87.250 | CC BY-NC-SA 4.0 (Attribution-NonCommercial-ShareAlike 4.0 International) | Giáo trình tiếng Trung của cộng đồng Datawhale hướng dẫn xây dựng hệ thống agent AI từ nguyên lý đến thực hành. | 16 chương đã hoàn thành từ khái niệm, ReAct, Plan-and-Solve, Reflection tới MCP, A2A, Agentic-RL và đánh giá; có bản đọc trực tuyến; hướng dẫn tự xây framework HelloAgents trên API kiểu OpenAI |  | Giấy phép CC BY-NC-SA 4.0 cấm dùng thương mại; nội dung chủ yếu tiếng Trung; ví dụ code cần khoá API LLM |
| [`josephmisiti/awesome-machine-learning`](https://github.com/josephmisiti/awesome-machine-learning) | 74.850 | File LICENSE chỉ có dòng "Creative Commons Legal Code" và "No need", không ghi rõ giấy phép CC cụ thể (chưa xác minh) | Danh sách tuyển chọn các framework, thư viện và phần mềm học máy, phân theo ngôn ngữ lập trình, kèm danh sách sách, khoá học, blog, sự kiện. | Phân loại theo ngôn ngữ và lĩnh vực (thị giác máy tính, NLP, nhận dạng tiếng nói…); có các file riêng cho sách, khoá học, blog, meetup; có quy tắc đánh dấu thư viện ngừng duy trì |  | Tác giả chỉ nhận PR khi gửi email xác minh là người thật (do quá nhiều PR do LLM tạo) |
| [`microsoft/AI-For-Beginners`](https://github.com/microsoft/AI-For-Beginners) | 70.987 | MIT License (Copyright (c) Microsoft Corporation) | Giáo trình AI cho người mới gồm 12 tuần, 24 bài, có quiz và lab, từ AI biểu tượng, mạng nơ-ron, thị giác máy tính, NLP đến đạo đức AI. | Notebook Jupyter thực hành cho cả PyTorch và TensorFlow; thư mục translations có 56 bản dịch ngôn ngữ; có thư mục examples với ví dụ cho người mới (Hello AI World, mạng nơ-ron đơn giản, phân loại ảnh) | `git clone --filter=blob:none --sparse https://github.com/microsoft/AI-For-Beginners.git` |  |
| [`HKUDS/DeepTutor`](https://github.com/HKUDS/DeepTutor) | 60.107 | Apache License 2.0 | Không gian học tập agent-native kết hợp gia sư, nghiên cứu, tạo nội dung và luyện tập (Chat, Quiz, Research, Visualize, Mastery Path, Reading) trên một runtime mở rộng được. | Phát hành dày đặc, bản mới nhất v1.7.3 ngày 2026-11-16; truy xuất tri thức với LlamaIndex, PageIndex, GraphRAG hoặc LightRAG; có Docker image ghcr.io/hkuds/deeptutor, gói pip và bản desktop cho macOS và Windows | `pip install -U "deeptutor[full]" rồi deeptutor init và deeptutor start` | Cần khoá nhà cung cấp LLM (cấu hình ở deeptutor init); Python 3.11–3.14 và Node.js 20.9+ khi cài từ pip; bản desktop Windows preview chưa ký số |
| [`bojieli/ai-agent-book`](https://github.com/bojieli/ai-agent-book) | 58.567 | Apache License 2.0 (README nêu một số dự án con có thể có giấy phép riêng) | Sách mã nguồn mở “深入理解 AI Agent：设计原理与工程实践” gồm 10 chương quanh công thức Agent = LLM + ngữ cảnh + công cụ, kèm thực nghiệm minh hoạ. | README nêu 109 thực nghiệm đi kèm; có bản PDF/EPUB và bản dịch cộng đồng sang 15 ngôn ngữ, trong đó có tiếng Việt; bản đọc trực tuyến tự build lại sau mỗi lần đẩy lên main |  | Tự biên dịch PDF cần pandoc, xelatex và ElegantBook |
| [`luongnv89/claude-howto`](https://github.com/luongnv89/claude-howto) | 47.381 | MIT License (Copyright (c) 2024 luongnv89) | Hướng dẫn học Claude Code theo lộ trình 10 mô-đun (slash command, memory, skills, subagents, MCP, hooks, plugins, checkpoints, CLI) với sơ đồ Mermaid và mẫu cấu hình chép dùng ngay. | 10 thư mục mô-đun có mẫu slash command, CLAUDE.md, hook, MCP, subagent và plugin; có bản dịch tiếng Việt, Nhật, Hàn, Ukraina, Ba Tư; README nêu đồng bộ với Claude Code v2.1.325 (11/2026) | `git clone https://github.com/luongnv89/claude-howto.git rồi chép mẫu vào .claude/ của dự án` | Cần Claude Code (sản phẩm của Anthropic) đã cài; dự án cộng đồng, không phải tài liệu chính thức |
| [`THU-MAIC/OpenMAIC`](https://github.com/THU-MAIC/OpenMAIC) | 43.841 | MIT License (Copyright (c) 2026 THU-MAIC) | Nền tảng lớp học tương tác đa agent: biến chủ đề hoặc tài liệu thành bài học với slide, quiz, mô phỏng HTML, PBL, bảng trắng và giọng đọc do giáo viên và bạn học AI dẫn dắt. | Bản ổn định v1.4.2 (2026-11-09) và v1.5.0-rc.3 (2026-11-17); hỗ trợ nhiều nhà cung cấp mô hình gồm OpenAI, Anthropic, Gemini, DeepSeek, Qwen, Ollama; xuất lớp học ra PPTX, HTML ngoại tuyến hoặc ZIP | `git clone https://github.com/THU-MAIC/OpenMAIC.git rồi pnpm install` | Cần Node.js ≥ 22.19, pnpm ≥ 10, PostgreSQL 16 và khoá API nhà cung cấp mô hình (mặc định OPENAI_API_KEY) |
| [`aymericdamien/TensorFlow-Examples`](https://github.com/aymericdamien/TensorFlow-Examples) | 43.729 | The MIT License (MIT) | Bộ ví dụ hướng dẫn TensorFlow dạng notebook và mã nguồn cho cả TF v1 và TF v2, từ cơ bản đến mạng nơ-ron. | Có hai thư mục tensorflow_v1 và tensorflow_v2 với notebook kèm mã; bao quát hồi quy tuyến tính và logistic, Word2Vec, GBDT, CNN, LSTM, GAN, TensorBoard; commit gần nhất 2026-11-13 | `pip install tensorflow` |  |
| [`datawhalechina/happy-llm`](https://github.com/datawhalechina/happy-llm) | 34.981 | Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0) | Giáo trình hệ thống về LLM từ khái niệm NLP, Transformer, mô hình tiền huấn luyện đến tự xây và huấn luyện LLaMA2, RAG, Agent và Agentic-RL. | 8 chương đều đánh dấu hoàn thành; có mô hình 215M (Base và SFT) đã huấn luyện trên ModelScope; có bản PDF miễn phí và đọc trực tuyến |  | Giấy phép cấm dùng thương mại và yêu cầu chia sẻ cùng giấy phép |
| [`datawhalechina/self-llm`](https://github.com/datawhalechina/self-llm) | 32.814 | Apache License 2.0 | Bộ hướng dẫn tiếng Trung cho người mới về cấu hình môi trường, triển khai, ứng dụng và tinh chỉnh (toàn phần, LoRA) các LLM mã nguồn mở trên Linux. | README nêu hỗ trợ hơn 50 mô hình (thư mục models có 61 mục); có hướng dẫn riêng cho AMD, Ascend, MLX và MUSA; có ví dụ ứng dụng như Chat-嬛嬛, Tianji, AMChat |  | Hướng dẫn nhắm nền tảng Linux; cần GPU tuỳ mô hình (chưa xác minh cấu hình cụ thể) |
| [`harvard-edge/cs249r_book`](https://github.com/harvard-edge/cs249r_book) | 30.242 | Đa giấy phép: LICENSE.md là CC BY-NC-SA 4.0 cho tài liệu học; sách trong books/ là CC BY-NC-ND 4.0 (MIT Press); TinyTorch MIT; MLSys·im Apache 2.0; StaffML AGPL v3; kho câu hỏi StaffML CC BY-NC 4.0 | Giáo trình Machine Learning Systems của Harvard gồm bộ sách nhiều tập, TinyTorch, lab, bộ kit phần cứng, MLSys·im và StaffML trong một repo. | Tập I sắp in bởi MIT Press; khởi nguồn từ lớp CS249r ở Harvard và khoá HarvardX TinyML; README có bản tiếng Trung, Nhật, Hàn |  | Nội dung sách và tài liệu cấm dùng thương mại; sách không được sửa đổi hay dịch khi chưa xin phép; StaffML là AGPL v3 |
| [`liguodongiot/llm-action`](https://github.com/liguodongiot/llm-action) | 25.290 | Apache License 2.0 | Tập hợp bài viết và mã thực hành tiếng Trung về huấn luyện, tinh chỉnh, suy luận, nén, đánh giá, hạ tầng AI và LLMOps cho LLM. | Mục lục bao quát huấn luyện phân tán, PEFT, lượng tử hoá, cắt tỉa, chưng cất, trình biên dịch AI, thích ứng phần cứng nội địa Trung Quốc; thư mục llm-train có ví dụ cho alpaca-lora, chatglm, deepspeedchat; có loạt 7 bài nguyên lý tinh chỉnh hiệu quả tham số |  |  |
| [`NirDiamant/GenAI_Agents`](https://github.com/NirDiamant/GenAI_Agents) | 25.024 | Giấy phép tùy chỉnh (Custom License Agreement) của Nir Diamant: chỉ dùng phi thương mại, bắt buộc ghi công; mọi dùng thương mại cần văn bản cho phép của tác giả; đóng góp trao cho tác giả giấy phép độc quyền kể cả thương mại | Bộ sưu tập notebook hướng dẫn và cài đặt mẫu các agent GenAI, từ chatbot đơn giản tới hệ đa agent. | 64 bài hướng dẫn được đánh số trong README (65 notebook trong all_agents_tutorials); README ghi ngày 2026-10-31 đã cập nhật notebook sang LangChain 1.x và LangGraph 1.x, thay các model đã ngừng; có nhóm bài "From Scratch" bằng Python thuần |  | Cấm dùng thương mại khi chưa có văn bản cho phép; mỗi notebook cần API key riêng (OpenAI và nhà cung cấp khác); README nói không phải notebook nào cũng đã chạy hết với dịch vụ thật |
| [`liyupi/ai-guide`](https://github.com/liyupi/ai-guide) | 22.185 | Nội dung Markdown và hình: CC BY-NC-SA 4.0, tác giả giữ toàn bộ quyền thương mại; mã nguồn (.vuepress, package.json): MIT theo LICENSE-CODE | Kho kiến thức AI miễn phí bằng tiếng Trung của 程序员鱼皮, trọng tâm là giáo trình Vibe Coding từ số 0, kèm hướng dẫn công cụ AI và DeepSeek. | Có bản đọc trực tuyến tại ai.codefather.cn; có bản dịch tiếng Anh và tiếng Trung phồn thể trong thư mục translations; giáo trình chia mục từ cơ bản, công cụ, dự án thực hành tới kiếm tiền từ sản phẩm |  | Nội dung cấm dùng thương mại (CC BY-NC-SA 4.0), muốn thương mại phải xin phép tác giả; nội dung chủ yếu tiếng Trung |
| [`NirDiamant/agents-towards-production`](https://github.com/NirDiamant/agents-towards-production) | 21.917 | Giấy phép tùy chỉnh (Custom License Agreement) của Nir Diamant: chỉ dùng phi thương mại, bắt buộc ghi công; mọi dùng thương mại cần văn bản cho phép của tác giả; người đóng góp giữ quyền với phần mình đóng góp | Bộ bài hướng dẫn xây agent GenAI cấp production: workflow có trạng thái, bộ nhớ vector, tìm web, Docker, FastAPI, guardrail bảo mật, GPU. | README nêu 28 bài hướng dẫn, thư mục tutorials có 24 bài; nhiều bài do chính các công ty (LangChain, Redis...) đóng góp; có bài fine-tune LoRA chạy trên laptop không cần API key | `git clone https://github.com/NirDiamant/agents-towards-production.git && cd tutorials/<bài> && pip install -r requirements.txt` | Cấm dùng thương mại khi chưa có văn bản cho phép; nhiều bài cần tài khoản/khoá API của dịch vụ tài trợ |
| [`mrdbourke/pytorch-deep-learning`](https://github.com/mrdbourke/pytorch-deep-learning) | 19.432 | MIT (Copyright (c) 2021 Daniel Bourke) | Tài liệu khoá học Learn PyTorch for Deep Learning: notebook từ nền tảng PyTorch tới thị giác máy, transfer learning, tái hiện paper và triển khai mô hình. | 10 phần 00–09 đều có notebook trong repo; README ghi toàn bộ tài liệu đã hoàn thành với 321 video; có bản sách đọc trực tuyến tại learnpytorch.io | `Mở notebook trên Google Colab (SETUP.md)` |  |
| [`google-gemini/cookbook`](https://github.com/google-gemini/cookbook) | 17.956 | Apache License 2.0 | Bộ notebook hướng dẫn và ví dụ thực hành dùng Gemini API, chia thành Quick Starts và Examples. | 62 mục trong thư mục quickstarts, mỗi notebook có nút mở trên Colab; có cả bản JavaScript (quickstarts-js); cập nhật các model và API mới như Gemini 4, TTS, Live API, Webhooks |  | Cần tài khoản Google và API key tạo ở Google AI Studio |
| [`GoogleCloudPlatform/generative-ai`](https://github.com/GoogleCloudPlatform/generative-ai) | 17.955 | Apache License 2.0 | Kho notebook, mã mẫu và ứng dụng mẫu minh hoạ cách dùng Gemini, tìm kiếm, RAG, thị giác, giọng nói trên Google Cloud. | Khoảng 347 notebook chia theo thư mục gemini, search, rag-grounding, vision, audio, agents; có notebook mở đầu cho Gemini 4 Hydrogen và Carbon; dùng renovate.json để cập nhật phụ thuộc |  | Cần dự án Google Cloud; README nói đây không phải sản phẩm Google được hỗ trợ chính thức, mã chỉ để minh hoạ |
| [`datawhalechina/leedl-tutorial`](https://github.com/datawhalechina/leedl-tutorial) | 16.878 | Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0) | Giáo trình học sâu tiếng Trung dựa trên khoá Machine Learning 2021 của GS Lý Hoành Nghị (Đài Loan), kèm bài tập. | Thư mục Homework có 15 bài tập HW1–HW15 cùng phần Warmup; được chính GS Lý Hoành Nghị giới thiệu; đã có bản sách in |  | Cấm dùng thương mại (CC BY-NC-SA 4.0); nội dung tiếng Trung; không có README ở gốc repo (README nằm trong docs/) |
| [`Arindam200/awesome-ai-apps`](https://github.com/Arindam200/awesome-ai-apps) | 16.758 | MIT (Copyright (c) 2025 Arindam Majumder) | Bộ sưu tập 144 ứng dụng LLM và agent chạy được: agent văn bản, trợ lý giọng nói, RAG, công cụ MCP, fine-tune. | 144 dự án chia theo 8 thư mục (starter, simple, advance, mcp, memory, rag, voice, fine_tuning), khớp số trong README; mỗi dự án nằm trong thư mục riêng có README; hướng dẫn chạy bằng uv hoặc pip | `git clone https://github.com/Arindam200/awesome-ai-apps.git && cd <dự án> && uv sync` | Cần Python 3.10+ và API key theo README từng dự án; phần lớn dự án chạy trên Nebius Token Factory |

**Chưa thêm (2 repo, giữ trong file dữ liệu):** `MLEveryday/100-Days-Of-ML-Code` (bản sao/bản dịch: bản tiếng Trung dựa trên dự án tiếng Anh của Avik-Jain; mới có Day 1–54, Day 55–100 chưa viết); `meta-llama/llama-cookbook` (commit cuối 3/11/2025).

#### 6c.5.13 Mô hình AI & Huấn luyện

Đọc mã 34 repo, giữ 33.

| Repo | ★ (18/11/2026) | Giấy phép | Làm gì | Điểm mạnh (đọc mã) | Cài | Điều kiện dùng |
|---|---|---|---|---|---|---|
| [`tensorflow/tensorflow`](https://github.com/tensorflow/tensorflow) | 201.750 | Apache License 2.0 | Nền tảng học máy mã nguồn mở đầu-cuối do Google phát triển, dùng để nghiên cứu, huấn luyện và triển khai mô hình ML. | Có API Python và C++ ổn định; gói pip hỗ trợ GPU CUDA (Ubuntu, Windows) và có bản tensorflow-cpu gọn hơn; có bản nightly tf-nightly trên PyPI | `pip install tensorflow` | GPU cần card hỗ trợ CUDA; thiết bị khác (DirectX, macOS Metal) qua Device Plugins |
| [`huggingface/transformers`](https://github.com/huggingface/transformers) | 169.322 | Apache License 2.0 | Thư viện định nghĩa mô hình học máy tiên tiến cho văn bản, thị giác, âm thanh, video và đa phương thức, dùng cho cả suy luận và huấn luyện. | Có hơn 550 thư mục kiến trúc mô hình trong src/transformers/models; API Pipeline cấp cao cho nhiều tác vụ; tương thích với hệ sinh thái huấn luyện (DeepSpeed, FSDP) và suy luận (vLLM, SGLang, TGI) | `pip install "transformers[torch]"` | Cần Python 3.11+ và PyTorch 2.6+; tải checkpoint từ Hugging Face Hub, một số mô hình có giấy phép riêng |
| [`pytorch/pytorch`](https://github.com/pytorch/pytorch) | 105.813 | BSD 3 điều khoản (kiểu BSD sửa đổi, nhiều chủ bản quyền gồm Facebook, Idiap, NEC; cấm dùng tên để quảng bá sản phẩm phái sinh) | Gói Python cung cấp tính toán tensor tăng tốc GPU và mạng nơ-ron sâu dựa trên autograd kiểu băng ghi (tape-based). | Gồm torch, torch.autograd, torch.nn, torch.multiprocessing, torch.utils; hỗ trợ build với NVIDIA CUDA, AMD ROCm và Intel GPU; có wheel cho NVIDIA Jetson và image Docker dựng sẵn | `Lệnh pip/conda tại https://pytorch.org/get-started/locally/` | Build từ mã nguồn cần Python 3.11+, trình biên dịch C++20, ít nhất 10 GB đĩa |
| [`tensorflow/models`](https://github.com/tensorflow/models) | 77.629 | Apache License 2.0 (áp dụng cho các thư mục community, official, orbit, research, tensorflow_models) | TensorFlow Model Garden: kho triển khai các mô hình tiên tiến (SOTA) và giải pháp mô hình hoá cho người dùng TensorFlow. | Thư mục official được đội TensorFlow bảo trì theo API TensorFlow 2 mới nhất; có thư viện orbit cho vòng lặp huấn luyện tùy biến tích hợp tf.distribute (CPU, GPU, TPU); phát hành gói pip tf-models-official và bản nightly | `pip3 install tf-models-official` | Thư mục research do nhà nghiên cứu bảo trì, có thể dùng TensorFlow 1 |
| [`keras-team/keras`](https://github.com/keras-team/keras) | 64.429 | Apache License 2.0 | Keras 3: framework học sâu đa backend (JAX, TensorFlow, PyTorch; OpenVINO chỉ suy luận) với API cấp cao để xây và huấn luyện mô hình. | Có mã backend cho JAX, TensorFlow, PyTorch và NumPy trong keras/src/backend; bảng phiên bản backend tối thiểu rõ ràng (TensorFlow 2.16.1, JAX 0.4.20, PyTorch 2.6.0); có file requirements riêng cho CUDA và TPU | `pip install keras --upgrade` | Cần cài thêm backend (tensorflow, jax hoặc torch); hỗ trợ Linux và macOS, Windows khuyến nghị dùng WSL2 |
| [`oobabooga/textgen`](https://github.com/oobabooga/textgen) | 47.739 | GNU Affero General Public License v3 (AGPL-3.0) | TextGen: ứng dụng desktop và giao diện web chạy LLM cục bộ, hỗ trợ chat, thị giác, gọi công cụ, tìm kiếm web, kèm API. | Hỗ trợ nhiều backend (llama.cpp, ik_llama.cpp, Transformers, ExLlamaV3, TensorRT-LLM); API tương thích OpenAI/Anthropic có tool-calling và hỗ trợ MCP; bản portable cho Linux, Windows, macOS với CUDA, Vulkan, ROCm, CPU | `Tải bản portable tại https://github.com/oobabooga/textgen/releases; hoặc pip install -r requirements/portable/requirements.txt rồi python server.py --portable --api --auto-launch` | AGPL-3.0 (cung cấp qua mạng phải công bố mã nguồn); bản cài đầy đủ cần khoảng 10 GB đĩa; người dùng tự tải mô hình (theo giấy phép của từng mô hình) |
| [`janhq/jan`](https://github.com/janhq/jan) | 45.781 | Apache License 2.0 (Copyright 2025 Menlo Research; yêu cầu ghi công trong tài liệu hướng tới người dùng khi phù hợp) | Jan: ứng dụng desktop mã nguồn mở thay thế ChatGPT, tải và chạy LLM cục bộ hoặc kết nối mô hình đám mây. | Máy chủ API tương thích OpenAI cục bộ tại localhost:1337; tích hợp Model Context Protocol (MCP); có bản cho Windows, macOS, Linux (deb, AppImage, Arm64), Microsoft Store và Flathub | `Tải từ https://jan.ai/ hoặc GitHub Releases; build: make dev` | Kết nối mô hình đám mây (OpenAI, Anthropic, Mistral, Groq...) cần khoá API riêng; macOS 13.6+, Windows 10+; build cần Node.js 20+, Yarn 4.5.3+, Rust |
| [`ray-project/ray`](https://github.com/ray-project/ray) | 44.315 | Apache License 2.0 (kèm thông báo mã bên thứ ba theo MIT, BSD, Apache trong cùng file LICENSE) | Ray: framework hợp nhất để mở rộng ứng dụng AI và Python từ laptop lên cụm, gồm runtime phân tán lõi và các thư viện AI. | Có thư viện Data, Train, Tune, RLlib, Serve (đều có trong python/ray); trừu tượng lõi Tasks, Actors, Objects; chạy trên máy đơn, cụm, nhà cung cấp đám mây và Kubernetes, có Ray Dashboard | `pip install ray` |  |
| [`gradio-app/gradio`](https://github.com/gradio-app/gradio) | 44.076 | Apache License 2.0 | Gradio: gói Python để nhanh chóng dựng demo hoặc ứng dụng web cho mô hình ML, API hay hàm Python bất kỳ, kèm tính năng chia sẻ. | Hơn 30 component dựng sẵn cho ML; lớp gr.Interface bọc giao diện quanh hàm chỉ với vài dòng; share=True tạo URL công khai (gradio.live); có client Python và JS trong thư mục client | `pip install --upgrade gradio` | Cần Python 3.10+; share=True làm demo truy cập công khai qua máy chủ chia sẻ của Gradio |
| [`deepspeedai/DeepSpeed`](https://github.com/deepspeedai/DeepSpeed) | 43.337 | Apache License 2.0 | DeepSpeed: thư viện tối ưu huấn luyện và suy luận học sâu quy mô lớn trên nền PyTorch (ZeRO, 3D-Parallelism, MoE...). | Gồm các kỹ thuật ZeRO, ZeRO-Infinity, 3D-Parallelism, Ulysses Sequence Parallelism, DeepSpeed-MoE; đã dùng huấn luyện Megatron-Turing NLG 530B và BLOOM 176B; hỗ trợ nhiều bộ tăng tốc phần cứng và phần lớn tính năng trên Windows | `pip install deepspeed (kiểm tra bằng ds_report)` | Phải cài PyTorch trước; cần trình biên dịch CUDA hoặc ROCm (nvcc/hipcc) để build ops; Windows chưa hỗ trợ AIO và GDS |
| [`lyogavin/airllm`](https://github.com/lyogavin/airllm) | 42.585 | Apache License 2.0 | Thư viện Python giảm bộ nhớ khi suy luận LLM bằng cách nạp mô hình theo từng lớp, cho phép chạy mô hình 70B trên GPU 4GB mà không cần lượng tử hoá; gần đây thêm cả huấn luyện adapter. | Một API AutoModel.from_pretrained nhận repo ID Hugging Face và tự nhận loại mô hình; có lớp riêng cho Llama, Qwen, Mistral, Mixtral, ChatGLM, Baichuan, InternLM, Kimi K3 trong air_llm/airllm; hỗ trợ prefetch và nén 4bit/8bit tuỳ chọn, chạy được trên CPU và macOS. | `pip install airllm` | Cần tải trọng số mô hình từ Hugging Face (tuân giấy phép từng mô hình); macOS chỉ hỗ trợ Apple Silicon, cần mlx, và chỉ mô hình kiểu Llama/Mistral; con số VRAM cho mô hình mới là do dự án tự công bố (chưa xác minh). |
| [`hpcaitech/ColossalAI`](https://github.com/hpcaitech/ColossalAI) | 41.423 | Apache License 2.0 (Copyright 2021- HPC-AI Technology Inc.) | Hệ thống huấn luyện và suy luận phân tán cho mô hình AI lớn trên PyTorch, cung cấp nhiều chiến lược song song để giảm chi phí và bộ nhớ. | Hỗ trợ data, pipeline, tensor 1D/2D/2.5D/3D, sequence parallelism, ZeRO và auto-parallelism; README có bảng benchmark huấn luyện mô hình 7B/70B trên H200/B200; kèm ứng dụng mẫu như ColossalChat (RLHF) và Colossal-LLaMA. | `pip install colossalai` | Chỉ hỗ trợ Linux; cần GPU NVIDIA compute capability ≥ 7.0, CUDA ≥ 11.0, PyTorch 2.2 đến dưới 2.14, Python 3.10 đến dưới 3.13; README quảng cáo dịch vụ đám mây trả phí HPC-AI (không bắt buộc). |
| [`AlexsJones/llmfit`](https://github.com/AlexsJones/llmfit) | 39.055 | MIT License (Copyright (c) 2026 Alex Jones) | Công cụ dòng lệnh/TUI viết bằng Rust dò phần cứng máy (CPU, RAM, GPU, VRAM) và gợi ý những LLM mã nguồn mở chạy tốt trên máy đó theo các mức lượng tử hoá. | Tự nhận diện NVIDIA CUDA, Apple Silicon, AMD ROCm, Intel OneAPI và chấm điểm mô hình theo chất lượng, tốc độ, độ vừa, ngữ cảnh; có TUI, CLI, web dashboard và REST API (/api/v1/system, /api/v1/models); phân phối qua WinGet, Scoop, Homebrew, MacPorts, crates.io và pip/uv. | `brew install AlexsJones/llmfit/llmfit` | Theo README chỉ liên lạc dịch vụ ngoài khi người dùng dùng tính năng tương ứng (tải mô hình, truy vấn runtime, leaderboard cộng đồng). |
| [`Lightning-AI/pytorch-lightning`](https://github.com/Lightning-AI/pytorch-lightning) | 31.450 | Apache License 2.0 | Framework deep learning trên PyTorch để tiền huấn luyện và tinh chỉnh mô hình, tách phần kỹ thuật (đa GPU, mixed precision, phân tán) khỏi logic mô hình. | Gồm hai gói lõi PyTorch Lightning và Lightning Fabric (thư mục src/pytorch_lightning, src/lightning_fabric); mở rộng từ CPU tới nhiều node GPU mà không đổi mã lõi; cài qua pip hoặc conda-forge. | `pip install lightning` | README quảng cáo Lightning Cloud trả phí nhưng có thể chạy trên phần cứng riêng. |
| [`fastai/fastai`](https://github.com/fastai/fastai) | 28.272 | Apache License 2.0 | Thư viện deep learning cấp cao trên PyTorch, cung cấp thành phần dựng sẵn cho thị giác, văn bản, dữ liệu bảng và hệ gợi ý, đồng thời có tầng thấp cho nhà nghiên cứu. | Có module vision, text, tabular, collab, medical trong gói fastai; hệ callback hai chiều can thiệp được dữ liệu, mô hình, optimizer trong lúc huấn luyện; tài liệu viết dạng notebook mở được trên Colab, kèm sách và khoá học miễn phí. | `pip install fastai` | Nên cài PyTorch phù hợp máy trước. |
| [`mozilla-ai/llamafile`](https://github.com/mozilla-ai/llamafile) | 26.664 | Apache License 2.0 (Copyright 2023 Mozilla Foundation); phần sửa llama.cpp và whisper.cpp theo MIT | Đóng gói LLM thành một file thực thi duy nhất chạy cục bộ trên hầu hết hệ điều hành và kiến trúc CPU, ghép llama.cpp với Cosmopolitan Libc; kèm whisperfile cho chuyển giọng nói thành văn bản. | Không cần cài đặt, tải một file .llamafile rồi chmod +x là chạy; từ 0.10.0 dùng hệ build mới bám sát llama.cpp mới nhất; có thêm whisperfile, stable-diffusion.cpp và agent.cpp trong cây mã. | `curl -LO https://huggingface.co/mozilla-ai/llamafile_0.10/resolve/main/Qwen3.5-0.8B-Q8_0.llamafile && chmod +x Qwen3.5-0.8B-Q8_0.llamafile` | Trên Windows chỉ chạy được file thực thi dưới 4GB, phải đổi đuôi thành .exe; bản 0.10 có thể thiếu một số tính năng của bản cũ; trọng số mô hình theo giấy phép riêng. |
| [`shap/shap`](https://github.com/shap/shap) | 25.867 | MIT License (Copyright (c) 2018 Scott Lundberg) | Thư viện giải thích đầu ra của mô hình học máy bằng giá trị Shapley (SHAP), kèm nhiều biểu đồ trực quan hoá. | Có thuật toán chính xác tốc độ cao cho tree ensemble (XGBoost, LightGBM, CatBoost, scikit-learn, pyspark) viết bằng C++; GPUTreeExplainer qua gói shap-cuda; tuân SPEC 0 về phiên bản phụ thuộc tối thiểu. | `pip install shap` | Tăng tốc GPU cần gói riêng shap[cuda] và phần cứng CUDA. |
| [`lucidrains/vit-pytorch`](https://github.com/lucidrains/vit-pytorch) | 25.580 | MIT License (Copyright (c) 2020 Phil Wang) | Bộ cài đặt Vision Transformer và nhiều biến thể ViT bằng PyTorch để phân loại ảnh và tự giám sát. | README có hơn 40 mục biến thể như Simple ViT, NaViT, CaiT, MaxViT, MobileViT, Masked Autoencoder, Dino; khoảng 85 file trong gói vit_pytorch; có thư mục tests và examples. | `pip install vit-pytorch` |  |
| [`pyg-team/pytorch_geometric`](https://github.com/pyg-team/pytorch_geometric) | 24.147 | MIT License (Copyright (c) 2023 PyG Team) | Thư viện PyG trên PyTorch để viết và huấn luyện mạng nơ-ron đồ thị (GNN) cho dữ liệu có cấu trúc. | Cài đặt sẵn rất nhiều lớp GNN (khoảng 129 mục Conv trong torch_geometric.nn.conv); có mini-batch loader cho nhiều đồ thị nhỏ và đồ thị lớn, hỗ trợ đa GPU; có bài báo PyG 1.0 và 2.0 cùng tài liệu ReadTheDocs. | `pip install torch_geometric` | Một số tính năng cần gói mở rộng biên dịch sẵn (pyg_lib, torch_scatter, torch_sparse) khớp phiên bản PyTorch/CUDA. |
| [`PaddlePaddle/Paddle`](https://github.com/PaddlePaddle/Paddle) | 24.146 | Apache License 2.0 (Copyright (c) 2016 PaddlePaddle Authors) | Nền tảng deep learning công nghiệp mã nguồn mở của Trung Quốc (PaddlePaddle), hỗ trợ huấn luyện và suy luận, gồm cả mô hình lớn. | Bản phát hành mới nhất theo README là 3.3; hợp nhất đồ thị động/tĩnh với song song tự động, có trình biên dịch mạng nơ-ron và vi phân bậc cao; thích ứng nhiều loại chip phần cứng qua giao diện chuẩn hoá. |  | Hướng dẫn cài đặt nằm ở trang paddlepaddle.org.cn (Quick Install), README không ghi lệnh cụ thể. |
| [`jundot/omlx`](https://github.com/jundot/omlx) | 23.705 | Apache-2.0 | Máy chủ suy luận LLM tối ưu cho Mac Apple Silicon (dựa trên MLX), có continuous batching, KV cache phân tầng RAM/SSD và quản lý từ thanh menu; cung cấp API tương thích OpenAI. | KV cache hai tầng nóng (RAM) và lạnh (SSD) lưu dạng safetensors, dùng lại được cả sau khi khởi động lại máy chủ; hỗ trợ LLM, VLM, OCR, embedding và reranker với dashboard quản trị /admin chạy offline; cài qua DMG, Homebrew hoặc từ mã nguồn | `brew tap jundot/omlx https://github.com/jundot/omlx && brew install jundot/omlx/omlx` | Cần macOS 15.0+, Python 3.11–3.13 và Apple Silicon (M1–M5); kernel tuỳ biến cần Xcode đầy đủ; suy luận nhiều Mac là thử nghiệm |
| [`mlc-ai/mlc-llm`](https://github.com/mlc-ai/mlc-llm) | 23.535 | Apache-2.0 (kèm file NOTICE) | Trình biên dịch học máy và engine triển khai hiệu năng cao cho mô hình ngôn ngữ lớn, chạy gốc trên nhiều nền tảng phần cứng. | MLCEngine thống nhất cung cấp API tương thích OpenAI qua REST, Python, JavaScript, iOS và Android; hỗ trợ GPU AMD, NVIDIA, Apple, Intel qua Vulkan, ROCm, CUDA, Metal, cùng WebGPU/WASM trên trình duyệt và OpenCL trên Android; nền tảng kỹ thuật TVM/TensorIR có công bố khoa học | `python -m pip install --pre -U -f https://mlc.ai/wheels mlc-llm-nightly-cpu mlc-ai-nightly-cpu` |  |
| [`microsoft/unilm`](https://github.com/microsoft/unilm) | 22.246 | MIT (Copyright Microsoft Corporation); README ghi một phần mã dựa trên dự án transformers | Kho mã nghiên cứu của Microsoft về tiền huấn luyện tự giám sát quy mô lớn qua nhiều tác vụ, ngôn ngữ và phương thức, gồm mã và mô hình như UniLM, LayoutLM, BEiT, E5, TrOCR, Kosmos, BitNet. | Gần 60 thư mục dự án con gồm mô hình ngôn ngữ, thị giác, giọng nói và tài liệu (LayoutLMv3, BEiT-3, WavLM, TrOCR...); nhiều công trình kèm bài báo hội nghị và mô hình tiền huấn luyện công bố; giấy phép MIT |  | Mỗi dự án con có hướng dẫn và yêu cầu riêng; trọng số mô hình có thể kèm điều khoản riêng (chưa xác minh) |
| [`recommenders-team/recommenders`](https://github.com/recommenders-team/recommenders) | 22.002 | MIT (Copyright Microsoft Corporation và Recommenders contributors) | Thư viện Python và bộ notebook mẫu, thực hành tốt để xây dựng, đánh giá và đưa vào vận hành hệ thống gợi ý, thuộc LF AI & Data. | Hơn 30 thuật toán gợi ý cổ điển và học sâu (ALS, SAR, NCF, LightGCN, SASRec, xDeepFM...) kèm notebook quick start/deep dive; tiện ích chia dữ liệu, nạp dataset và chỉ số đánh giá offline cùng notebook benchmark MovieLens; cài được từ PyPI với các extra gpu, spark, dev | `uv pip install recommenders` | Một số extra cần GPU hoặc Spark; phần vận hành mẫu hướng tới Azure |
| [`onnx/onnx`](https://github.com/onnx/onnx) | 21.702 | Apache-2.0 (kèm NOTICE, thư mục LICENSES, tuân thủ REUSE) | Định dạng mở và hệ sinh thái cho mô hình AI (học sâu và ML truyền thống): định nghĩa đồ thị tính toán mở rộng được, toán tử dựng sẵn và kiểu dữ liệu chuẩn, cùng gói Python để làm việc với mô hình ONNX. | Có đặc tả IR, quy tắc phiên bản và tài liệu toán tử đầy đủ; tiện ích suy luận shape/type và chuyển đổi opset; wheel abi3 trên PyPI, huy hiệu OpenSSF Scorecard, SLSA 2 và hỗ trợ build tái lập | `pip install onnx` |  |
| [`openai/gpt-oss`](https://github.com/openai/gpt-oss) | 20.547 | Apache-2.0; kèm file USAGE_POLICY yêu cầu tuân thủ luật hiện hành | Kho mã tham chiếu cho dòng mô hình trọng số mở gpt-oss-120b và gpt-oss-20b của OpenAI, gồm cài đặt suy luận PyTorch, Triton, Metal, công cụ browser/python và client. | Hai mô hình MoE (117B và 21B tham số) với lượng tử hoá MXFP4, bản 120b chạy trên một GPU 80GB và bản 20b trong 16GB bộ nhớ; hướng dẫn chạy qua Transformers, vLLM và cài đặt tham chiếu Triton/Metal; mức suy luận cấu hình được (low, medium, high) và hỗ trợ gọi hàm, công cụ | `pip install gpt-oss` | Mô hình phải dùng định dạng phản hồi harmony; cài đặt tham chiếu chủ yếu cho mục đích giáo dục, không nhằm chạy production; bản torch cần ít nhất 4 GPU H100; trên Linux cần CUDA; chính sách sử dụng yêu cầu tuân thủ luật |
| [`NVIDIA/Megatron-LM`](https://github.com/NVIDIA/Megatron-LM) | 18.431 | BSD-3-Clause của NVIDIA cho phần lớn file; một số file từ Hugging Face, Google Research, Facebook, Microsoft, Mamba, Triton... theo Apache-2.0 và giấy phép ghi đầu file | Thư viện tối ưu cho GPU để huấn luyện mô hình transformer quy mô lớn, gồm Megatron Core (khối xây dựng ghép được) và Megatron-LM (kịch bản huấn luyện tham chiếu). | Hỗ trợ các chiến lược song song TP, PP, DP, EP, CP cùng độ chính xác hỗn hợp FP16, BF16, FP8; có checkpoint phân tán, suy luận, export TensorRT-LLM và hậu huấn luyện (lượng tử hoá, chưng cất, tỉa); phát hành megatron-core trên PyPI, bản 0.19 tháng 8/2026 | `uv pip install megatron-core` | Cần GPU NVIDIA; khuyến nghị Python 3.12+ và PyTorch 2.6.0+; build từ nguồn tốn nhiều bộ nhớ |
| [`FlashML-org/FreeToken`](https://github.com/FlashML-org/FreeToken) | 17.276 | Apache-2.0 | Engine phục vụ mô hình Mixture-of-Experts chạy trên thiết bị biên, cho phép chạy mô hình MoE trọng số mở cỡ lớn trên phần cứng tiêu dùng như PC chơi game. | Thực thi đồng thời CPU–GPU thích ứng băng thông, cache expert LRU toàn cục và phân bổ lại VRAM lúc chạy không cần khởi động lại; hỗ trợ nhiều định dạng lượng tử hoá (MXFP4, NVFP4, FP8, BF16, GGUF) và API tương thích Anthropic/OpenAI; có bài báo arXiv và ứng dụng desktop cho Windows/Linux | `uv pip install "freetoken[accel]"` | CLI cần Linux x86_64, GPU NVIDIA (RTX 30/40/50) với driver r580+ (CUDA 13) |
| [`tracel-ai/burn`](https://github.com/tracel-ai/burn) | 16.297 | Song giấy phép MIT hoặc Apache-2.0 (LICENSE-MIT, LICENSE-APACHE) | Thư viện tensor và framework học sâu viết bằng Rust cho tính toán số, huấn luyện và suy luận với cùng một mã nguồn. | Biên dịch JIT luồng phép toán tensor với hợp nhất kernel tự động, giữ đồ thị động; backend CubeCL chạy CUDA, ROCm, Metal, Vulkan, WebGPU và backend CPU thuần Rust hỗ trợ no_std; hệ sinh thái gồm burn-onnx, burn-store, burn-vision, burn-rl, burn-dataset |  | Cần Rust 1.95 trở lên |
| [`modelscope/ms-swift`](https://github.com/modelscope/ms-swift) | 16.120 | Apache License 2.0 (README: mô hình và bộ dữ liệu theo giấy phép riêng của từng nguồn) | Khung tinh chỉnh và triển khai mô hình ngôn ngữ lớn và đa phương thức của cộng đồng ModelScope: huấn luyện trước, tinh chỉnh, căn chỉnh (DPO, GRPO…), suy luận, đánh giá, lượng tử hoá và triển khai. | README nêu hỗ trợ 600+ mô hình văn bản và 400+ mô hình đa phương thức; có Megatron-SWIFT (TP/PP/CP/EP) và họ thuật toán GRPO (DAPO, GSPO, RLOO…); suy luận tăng tốc qua vLLM, SGLang, LmDeploy kèm giao diện tương thích OpenAI | `pip install ms-swift -U` | Cần GPU (CUDA/ROCm/Ascend…) cho huấn luyện thực tế, Python ≥ 3.10; mô hình và dữ liệu tải về phải tuân giấy phép gốc của chúng |
| [`NVIDIA/TensorRT-LLM`](https://github.com/NVIDIA/TensorRT-LLM) | 15.091 | Apache License 2.0; có phần mã dẫn xuất từ dự án khác mang giấy phép riêng (MIT, BSD 3-Clause…) liệt kê trong LICENSE | Thư viện của NVIDIA tối ưu suy luận LLM và mô hình sinh hình ảnh/video trên GPU NVIDIA, với kernel chuyên dụng, runtime và API Python (LLM API, trtllm-serve). | Kiến trúc dựa trên PyTorch với LLM API Python cấp cao; có tối ưu như tách prefill/decode, wide expert parallelism, giải mã suy đoán; có chính sách ngừng dùng rõ ràng với 3 tháng chuyển tiếp từ bản 1.0 | `pip3 install tensorrt_llm` | Cần GPU NVIDIA được hỗ trợ, CUDA Toolkit, Linux (cài pip) hoặc container; mặc định thu thập telemetry ẩn danh, tắt bằng TRTLLM_NO_USAGE_STATS=1 hoặc --no-telemetry |
| [`cactus-compute/cactus`](https://github.com/cactus-compute/cactus) | 14.802 | Apache License 2.0 (README: áp dụng cả cho runtime nhị phân dựng sẵn) | Gói Python chạy cục bộ mô hình văn bản, giọng nói và thị giác (Needle, Whistle, Mirage) cho gọi công cụ, trích xuất có cấu trúc, phiên âm, hiểu ảnh và tinh chỉnh mô hình. | Một gói pip cung cấp agent gọi công cụ, phiên âm có mốc thời gian theo từ và mô tả ảnh; có lệnh cactus-mlx chạy checkpoint CQ trên Apple silicon kèm máy chủ API tương thích OpenAI; thư mục tests có bộ test cho suy luận, LoRA, MLX, đóng gói | `pip install -U cactus-compute` | Python ≥ 3.9; lần đầu tự tải engine và trọng số mô hình; cactus-mlx cần Apple silicon, macOS 26+ và Python 3.12+; có telemetry đếm sử dụng ẩn danh, tắt bằng CACTUS_TELEMETRY=0 |
| [`BlinkDL/RWKV-LM`](https://github.com/BlinkDL/RWKV-LM) | 14.782 | Apache License 2.0 | Mã tham chiếu kiến trúc RWKV (đến RWKV-7 "Goose" và nghiên cứu RWKV-8): mạng RNN song song hoá được với hiệu năng ngang Transformer, gồm mã huấn luyện và demo suy luận. | RWKV-7 thời gian tuyến tính, bộ nhớ trạng thái hằng (không KV-cache); mã huấn luyện tham chiếu RWKV-v7/train_temp chạy cấu hình mặc định trên 1 GPU 7 GB VRAM; là dự án thuộc Linux Foundation AI | `pip install pytorch-lightning==1.9.5 deepspeed wandb ninja --upgrade (rồi chạy script trong RWKV-v7/train_temp)` | Huấn luyện cần GPU CUDA, Python 3.10+, torch 2.5+ và giữ pytorch-lightning==1.9.5; trọng số tải riêng từ Hugging Face |

**Chưa thêm (1 repo, giữ trong file dữ liệu):** `tensorflow/tfjs` (commit cuối 6/4/2026).

#### 6c.5.14 Ngôn ngữ & Runtime

Đọc mã 14 repo, giữ 14.

| Repo | ★ (18/11/2026) | Giấy phép | Làm gì | Điểm mạnh (đọc mã) | Cài | Điều kiện dùng |
|---|---|---|---|---|---|---|
| [`golang/go`](https://github.com/golang/go) | 140.176 | BSD 3-Clause (Copyright The Go Authors) kèm file PATENTS cấp quyền sáng chế bổ sung của Google | Mã nguồn ngôn ngữ lập trình Go: trình biên dịch, bộ công cụ và thư viện chuẩn. | Có bản phân phối nhị phân chính thức tại go.dev/dl; thư mục api lưu bề mặt API theo từng phiên bản (go1.txt…) để giữ tương thích; doc/next ghi thay đổi cho bản phát hành kế | `Tải bản nhị phân tại https://go.dev/dl/` | Kho GitHub là bản mirror, kho chính tắc ở go.googlesource.com; issue tracker chỉ dành cho báo lỗi và đề xuất |
| [`nodejs/node`](https://github.com/nodejs/node) | 123.898 | MIT (Node.js contributors); LICENSE kèm giấy phép của các thư viện bên thứ ba được nhúng | Node.js: runtime JavaScript mã nguồn mở, đa nền tảng, xây trên V8. | Quản trị mở dưới OpenJS Foundation; mỗi bản major nhận 30 tháng LTS, tổng 36 tháng tới hết hạn theo lịch mới; bản phát hành có SHASUMS256 ký PGP để xác minh | `Tải bản cài tại https://nodejs.org/en/download/` | Bản Alpha, Current và Nightly không dành cho production; nên dùng dòng LTS |
| [`rust-lang/rust`](https://github.com/rust-lang/rust) | 122.313 | Kép MIT hoặc Apache License 2.0 (tuỳ chọn), một số phần theo giấy phép kiểu BSD (xem COPYRIGHT) | Kho mã chính của ngôn ngữ Rust: trình biên dịch, thư viện chuẩn và tài liệu. | Hệ thống kiểu và mô hình ownership bảo đảm an toàn bộ nhớ và luồng lúc biên dịch; theo dõi giấy phép bằng REUSE (REUSE.toml, license-metadata.json); hệ công cụ đi kèm gồm Cargo, rustfmt, Clippy, rust-analyzer | `Cài theo chương Installation của The Rust Book (https://doc.rust-lang.org/book/ch01-01-installation.html)` | Tên và logo Rust/Cargo là nhãn hiệu của Rust Foundation, dùng phải theo chính sách nhãn hiệu; README khuyên không cài từ mã nguồn |
| [`microsoft/TypeScript`](https://github.com/microsoft/TypeScript) | 111.839 | Apache License 2.0 (kèm NOTICE.txt về mã bên thứ ba) | Ngôn ngữ TypeScript: thêm kiểu tuỳ chọn cho JavaScript và biên dịch ra JavaScript chuẩn; kho hiện chứa trình biên dịch và language server viết bằng Go (thư mục tsc), gói npm và extension VS Code. | Trình biên dịch và language server phát triển bằng Go trong tsc/internal (go.work); có gói npm typescript, gói typescript-wasip1-wasm và extension VS Code trong packages; tsc/CHANGES.md ghi rõ khác biệt có chủ đích giữa trình biên dịch cũ (Strada) và mới (Corsa) | `npm install -D typescript` |  |
| [`denoland/deno`](https://github.com/denoland/deno) | 109.037 | MIT (Copyright 2018-2026 the Deno authors) | Deno: runtime JavaScript, TypeScript và WebAssembly mặc định an toàn, xây trên V8, Rust và Tokio. | Quyền truy cập phải cấp rõ (ví dụ --allow-net); cài qua script, Homebrew, Chocolatey, WinGet, Scoop; có thư viện chuẩn trên JSR | `curl -fsSL https://deno.land/install.sh rồi chạy bằng sh (hoặc brew install deno)` |  |
| [`nvm-sh/nvm`](https://github.com/nvm-sh/nvm) | 96.242 | MIT (Copyright 2010 Tim Caswell, 2014 Jordan Harband) | Node Version Manager: công cụ quản lý nhiều phiên bản Node.js, cài theo từng người dùng và gọi trong từng shell. | Chạy trên mọi shell POSIX (sh, dash, ksh, zsh, bash) ở unix, macOS và WSL; có hướng dẫn cài trong Docker cho CI; có thư mục test và GOVERNANCE/PROJECT_CHARTER | `curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.41.0/install.sh rồi chạy bằng bash` | Không hỗ trợ Windows gốc (chỉ WSL, Git Bash, Cygwin), không hỗ trợ Fish, không hỗ trợ cài qua Homebrew |
| [`python/cpython`](https://github.com/python/cpython) | 78.497 | PSF License Agreement (Python Software Foundation License Version 2) kèm các giấy phép lịch sử BeOpen, CNRI, CWI; mã trong tài liệu theo Zero-Clause BSD | Mã nguồn chính thức của trình thông dịch Python (CPython) cùng thư viện chuẩn và tài liệu; nhánh main đang ở Python 3.16.0 alpha 2+dev. | Hướng dẫn build cho Unix, Linux, BSD, macOS, Cygwin và Windows (PCbuild); hỗ trợ build tối ưu PGO/LTO qua --enable-optimizations; CI trên GitHub Actions và Azure Pipelines | `./configure && make && make test && sudo make install` | Nhánh main là bản phát triển (3.16 alpha); bản cài sẵn lấy từ python.org |
| [`swiftlang/swift`](https://github.com/swiftlang/swift) | 70.565 | Apache License 2.0 kèm Runtime Library Exception | Mã nguồn trình biên dịch, thư viện chuẩn và runtime của ngôn ngữ lập trình Swift. | Ngôn ngữ hệ thống hiệu năng cao, an toàn bộ nhớ mặc định và gọi trực tiếp mã C/Objective-C; có script utils/build-toolchain dựng toolchain giống CI của swift.org; tài liệu nội bộ trong docs/ kèm hướng dẫn PR đầu tiên và FAQ | `./swift/utils/build-toolchain $BUNDLE_PREFIX` | Build từ nguồn cần môi trường theo Getting Started guide; bản dựng sẵn lấy từ swift.org |
| [`lodash/lodash`](https://github.com/lodash/lodash) | 61.453 | MIT (OpenJS Foundation); mã mẫu trong tài liệu theo CC0; thư viện trong node_modules và vendor theo giấy phép riêng | Thư viện tiện ích JavaScript (v4.18.1) cho thao tác mảng, đối tượng, chuỗi, số và ghép hàm. | Có nhiều bản dựng: core khoảng 4 kB gzip, full khoảng 24 kB gzip, bản FP tự curry; nạp từng phương thức riêng (lodash/at) để giảm kích thước bundle; được Sovereign Tech Agency hỗ trợ và chuyển sang giai đoạn Feature-Complete để giữ ổn định, an toàn lâu dài | `npm i --save lodash` |  |
| [`vercel/turborepo`](https://github.com/vercel/turborepo) | 31.361 | MIT (Copyright (c) 2026 Vercel, Inc) | Hệ thống build cho monorepo JavaScript/TypeScript, tự giới thiệu là "build system for coding agents", lõi viết bằng Rust. | Lõi Rust (Cargo workspace trong crates/) kèm gói npm turbo; có thư mục examples và test codemod; cộng đồng qua GitHub Discussions và kênh báo lỗ hổng bảo mật riêng | `npm i turbo (chưa xác minh trong README; README chỉ dẫn tới turborepo.dev)` |  |
| [`qax-os/excelize`](https://github.com/qax-os/excelize) | 21.137 | BSD 3-Clause | Thư viện Go thuần để đọc và ghi tệp bảng tính XLAM/XLSM/XLSX/XLTM/XLTX của Microsoft Excel 2007 trở lên. | Viết bằng Go thuần, không phụ thuộc Excel; có API streaming để ghi/đọc trang tính dữ liệu rất lớn; mỗi thành phần (calc, chart, crypt, datavalidation...) có tệp test riêng | `go get github.com/xuri/excelize/v2` | Cần Go 1.26.0 trở lên |
| [`Effect-TS/effect`](https://github.com/Effect-TS/effect) | 17.596 | MIT (Copyright (c) 2023 Effectful Technologies Inc) | Thư viện TypeScript để xây ứng dụng an toàn kiểu, xử lý lỗi có kiểu, tiêm phụ thuộc, đồng thời có cấu trúc, lập lịch, tracing và schema. | Effect 4.x là bản LTS cam kết hỗ trợ ít nhất ba năm; monorepo gồm effect, platform, sql, opentelemetry, ai, vitest; có MIGRATION.md hướng dẫn nâng từ 3.x | `npm install effect` | Cần TypeScript 5.9 trở lên với strict bật, Node.js 22.19 trở lên |
| [`sindresorhus/type-fest`](https://github.com/sindresorhus/type-fest) | 17.540 | Song giấy phép MIT hoặc CC0-1.0 (license-mit, license-cc0) | Bộ sưu tập các kiểu tiện ích TypeScript thiết yếu (Except, Primitive, Class...) dùng khi khai báo kiểu. | Chỉ chứa kiểu, có thể thêm làm phụ thuộc hoặc chép thẳng mà không cần ghi công; mỗi kiểu có tài liệu và tệp nguồn riêng trong source/; có test kiểu trong test-d | `npm install type-fest` | Cần TypeScript 6 trở lên, ESM, strict và exactOptionalPropertyTypes bật |
| [`gvergnaud/ts-pattern`](https://github.com/gvergnaud/ts-pattern) | 15.222 | MIT (Copyright (c) 2021 Gabriel Vergnaud) | Thư viện pattern matching cho TypeScript với suy luận kiểu và kiểm tra đủ trường hợp. | Kiểm tra đầy đủ nhánh bằng .exhaustive(); khớp mẫu trên đối tượng lồng, mảng, tuple, Set, Map và kiểu nguyên thủy; bundle nhỏ khoảng 2 kB | `npm install ts-pattern` |  |

#### 6c.5.15 Năng suất, Ghi chú & Việc làm

Đọc mã 37 repo, giữ 36.

| Repo | ★ (18/11/2026) | Giấy phép | Làm gì | Điểm mạnh (đọc mã) | Cài | Điều kiện dùng |
|---|---|---|---|---|---|---|
| [`koala73/worldmonitor`](https://github.com/koala73/worldmonitor) | 90.854 | AGPL-3.0-only; dùng mã nguồn đóng hoặc dùng thương hiệu chính thức cần giấy phép thương mại riêng | Bảng điều khiển tình báo toàn cầu thời gian thực: tổng hợp tin bằng AI, theo dõi địa chính trị, hạ tầng, tài chính trên bản đồ 3D/2D, có web, desktop, terminal, CLI và SDK. | Tự host toàn bộ stack bằng Docker (dashboard, Redis, AIS relay); chạy AI cục bộ với Ollama không cần khoá API; app desktop Tauri 2 cho Windows, macOS, Linux và dashboard terminal qua npx | `npx worldmonitor (hoặc tự host: git clone rồi npm install && npm run dev)` | AGPL-3.0 buộc công bố mã khi chạy dịch vụ mạng; không được trình bày bản fork như trang chính thức (thương hiệu World Monitor); một số nguồn dữ liệu cần thông tin xác thực riêng (.env.example); Node.js 24 |
| [`career-ops-hq/career-ops`](https://github.com/career-ops-hq/career-ops) | 83.377 | MIT (Copyright (c) 2026 Santiago Fernández de Valderrama) | Agent tìm việc mã nguồn mở chạy cục bộ trong CLI AI (Claude Code, Codex, OpenCode...): đánh giá tin tuyển dụng theo CV, tạo CV PDF tối ưu ATS, soạn câu trả lời và theo dõi ứng tuyển; người dùng tự bấm nộp. | Chạy cục bộ, không thu telemetry; hỗ trợ nhiều CLI AI qua Agent Skill Standard và cả mô hình cục bộ miễn phí; quét cổng ATS (Greenhouse, Lever, Ashby...) với tuỳ chọn --verify bằng Playwright loại tin đã đóng | `npx @santifer/career-ops init` | Cần Node.js và một CLI AI với nhà cung cấp mô hình riêng (dữ liệu CV gửi tới nhà cung cấp đó); phải tuân thủ ToS từng nền tảng việc làm, không scrape nơi cấm, không spam hay nộp hàng loạt; tự kiểm tra tài liệu AI tạo vì có thể bịa (LEGAL_DISCLAIMER.md) |
| [`AppFlowy-IO/AppFlowy`](https://github.com/AppFlowy-IO/AppFlowy) | 79.108 | AGPL-3.0 | Không gian làm việc kiểu Notion mã nguồn mở có AI, giữ quyền kiểm soát dữ liệu; ứng dụng desktop và di động. | Viết bằng Flutter và Rust (thư mục frontend/appflowy_flutter và frontend/rust-lib); có bản cho macOS, Windows, Linux, iOS và Android; có hướng dẫn tự host | `Tải bản phát hành từ GitHub Releases (hoặc FlatHub, Snapcraft)` | AGPL-3.0: phân phối hoặc cung cấp qua mạng bản sửa đổi phải công bố mã nguồn; Android cần bản 10 trở lên, không hỗ trợ ARMv7 |
| [`toeverything/AFFiNE`](https://github.com/toeverything/AFFiNE) | 74.618 | Hỗn hợp: MIT cho phần lớn mã (LICENSE-MIT); packages/backend và packages/common/native theo AFFiNE Enterprise Edition License (cần thuê bao EE để dùng production phần không thuộc bản Community) | Không gian làm việc tất cả trong một, local-first, gộp tài liệu, bảng trắng (canvas) và cơ sở dữ liệu, thay thế Notion và Miro. | Tài liệu và bảng trắng hợp nhất trên canvas edgeless dựa trên BlockSuite; local-first kèm đồng bộ và cộng tác thời gian thực; có ứng dụng web, Electron, iOS và Android trong packages/frontend/apps |  | Phần backend theo giấy phép EE: dùng production cần thuê bao AFFiNE EE (phần thuộc bản Community thì không); đóng góp cần ký CLA |
| [`ai-job-search-dev/ai-job-search`](https://github.com/ai-job-search-dev/ai-job-search) | 72.306 | MIT | Khung quy trình xin việc chạy trên Claude Code: dựng hồ sơ, tìm và chấm điểm tin tuyển dụng, soạn CV và thư xin việc LaTeX riêng cho từng vị trí, luyện phỏng vấn và theo dõi kết quả. | Chuỗi lệnh /setup, /scrape, /rank, /apply, /interview, /outcome và các lệnh mở rộng như /upskill, /html-report; CV và thư biên dịch bằng LaTeX kèm vòng kiểm tra PDF; skill cổng việc làm tách sang repo community-portals, cài với --ignore-scripts | `gh repo clone ai-job-search-dev/ai-job-search (dùng bản sao riêng tư), rồi chạy /setup trong Claude Code` | Cần Claude Code (gói Pro/Max/Team hoặc API trả tiền), Python 3.10+, Bun, LaTeX; /setup ghi dữ liệu cá nhân vào file được theo dõi nên không dùng fork công khai; skill linkedin-search chỉ dùng cá nhân, cần xem ghi chú ToS từng cổng; dự án không liên kết với Anthropic |
| [`nocodb/nocodb`](https://github.com/nocodb/nocodb) | 65.560 | Sustainable Use License 1.0 (không phải nguồn mở OSI; cập nhật 29/01/2026) | Nền tảng cơ sở dữ liệu không cần code với giao diện kiểu bảng tính (thay thế Airtable), chạy trên SQLite hoặc PostgreSQL. | Chạy nhanh bằng một lệnh Docker với SQLite hoặc PostgreSQL; script Auto-upstall cài sẵn PostgreSQL, Redis, Traefik và SSL; có REST API và SDK (packages/nocodb-sdk) | `docker run -d --name noco -v "$(pwd)"/nocodb:/usr/app/data/ -p 8080:8080 nocodb/nocodb:latest` | Sustainable Use License: chỉ dùng/sửa cho mục đích kinh doanh nội bộ, phi thương mại hoặc cá nhân; chỉ được phân phối miễn phí cho mục đích phi thương mại; không còn phát hành binary dựng sẵn |
| [`usememos/memos`](https://github.com/usememos/memos) | 64.528 | MIT | Ứng dụng ghi chú nhanh tự host, sắp xếp ghi chú Markdown theo dòng thời gian cá nhân, tự chọn riêng tư hay chia sẻ. | Chạy bằng một lệnh Docker, toàn bộ dữ liệu nằm trong một thư mục ~/.memos; backend Go kèm web frontend; có API, MCP server, Web Clipper và bot Telegram | `docker run -d --name memos -p 5230:5230 -v ~/.memos:/var/opt/memos neosmemo/memos:stable` |  |
| [`sansan0/TrendRadar`](https://github.com/sansan0/TrendRadar) | 63.705 | GPL-3.0 | Trợ lý theo dõi tin nóng: gom bảng xếp hạng thịnh hành từ nhiều nền tảng (Trung Quốc) và RSS, lọc theo từ khoá, phân tích bằng AI và đẩy thông báo qua nhiều kênh. | Mặc định theo dõi 11 nền tảng như Zhihu, Weibo và hỗ trợ RSS; đẩy qua WeCom, Feishu, DingTalk, Telegram, Email, ntfy, Bark, Slack, webhook; có MCP server và triển khai qua GitHub Actions, Docker hoặc chạy cục bộ | `uv run python -m trendradar (hoặc docker compose up -d, hoặc fork chạy GitHub Actions)` | Dữ liệu nền tảng lấy qua API của dự án newsnow (có thể tự host); phân tích AI cần khoá API mô hình (mặc định DeepSeek); tài liệu chủ yếu tiếng Trung; tác giả nói đây là chia sẻ mã nguồn mở, không phải sản phẩm thương mại |
| [`laurent22/joplin`](https://github.com/laurent22/joplin) | 57.228 | AGPL-3.0-or-later mặc định; thư mục có LICENSE riêng theo file đó (packages/server theo Joplin Server Personal Use License, chỉ phi thương mại); logo và biểu tượng giữ mọi quyền; Joplin là nhãn hiệu đã đăng ký | Ứng dụng ghi chú và việc cần làm mã nguồn mở, offline-first, ghi chú Markdown sắp theo sổ, đồng bộ có mã hoá đầu cuối. | Có bản Windows, Linux, macOS, Android, iOS và Web Clipper cho Firefox/Chrome; đồng bộ mã hoá đầu cuối qua Nextcloud, Dropbox, OneDrive, Joplin Cloud; nhập từ Evernote, tìm kiếm toàn văn, hỗ trợ plugin và theme |  | Joplin Server chỉ được dùng phi thương mại cá nhân trừ khi có cho phép bằng văn bản; không dùng logo/biểu tượng khi chưa xin phép |
| [`paperless-ngx/paperless-ngx`](https://github.com/paperless-ngx/paperless-ngx) | 48.232 | GPL-3.0 | Hệ thống quản lý tài liệu tự host, biến giấy tờ quét thành kho lưu trữ trực tuyến tìm kiếm được. | Kế nhiệm chính thức của Paperless và Paperless-ng; triển khai bằng docker compose với script cài đặt sẵn; có bản demo công khai và bản dịch điều phối qua Crowdin | `bash -c "$(curl -L https://raw.githubusercontent.com/paperless-ngx/paperless-ngx/main/install-paperless-ngx.sh)"` | Dữ liệu lưu dạng rõ, không mã hoá: dự án khuyến cáo không chạy trên máy chủ không tin cậy, tự chịu rủi ro, nên chạy trên máy chủ tại nhà có sao lưu |
| [`siyuan-note/siyuan`](https://github.com/siyuan-note/siyuan) | 47.272 | AGPL-3.0 | Hệ thống quản lý tri thức cá nhân ưu tiên riêng tư, tham chiếu cấp khối và soạn Markdown WYSIWYG. | Tham chiếu khối hai chiều, nhúng truy vấn SQL, cơ sở dữ liệu dạng bảng và flashcard lặp lại ngắt quãng; xuất Markdown, PDF, Word, HTML; có ứng dụng Android/iOS/HarmonyOS và image Docker b3log/siyuan | `docker run -d -v workspace_dir_host:workspace_dir_container -p 6806:6806 b3log/siyuan serve --workspace=workspace_dir_container --accessAuthCode=<mật khẩu>` | Một số tính năng chỉ dành cho thành viên trả phí; AI dùng OpenAI API cần khoá; chạy Docker cần đặt accessAuthCode |
| [`reactive-resume/reactive-resume`](https://github.com/reactive-resume/reactive-resume) | 45.869 | MIT | Trình tạo CV và thư xin việc miễn phí, mã nguồn mở, có kiểm tra CV và theo dõi hồ sơ ứng tuyển, dùng bản host sẵn hoặc tự host. | 18 mẫu CV, xem trước PDF trực tiếp, xuất PDF, Word, Markdown, JSON; nhập từ JSON Resume, LinkedIn, PDF, Word; có REST API, MCP server và tự host qua Docker, Vercel, Cloudflare Workers | `docker compose up -d --build` | Tính năng AI cần nhà cung cấp do người dùng kết nối (có thể phát sinh chi phí); nhập Word cần nhà cung cấp AI |
| [`logseq/logseq`](https://github.com/logseq/logseq) | 45.639 | AGPL-3.0 | Nền tảng quản lý tri thức và cộng tác ưu tiên quyền riêng tư, mã nguồn mở; ghi chú dạng khối, hỗ trợ Markdown và Org-mode, có bản desktop, web và mobile. | Có plugin API với tài liệu tại plugins-doc.logseq.com; hỗ trợ chú thích PDF và quản lý công việc; có ứng dụng mobile (thư mục android, ios trong repo). | `Tải bản phát hành tại github.com/logseq/logseq/releases hoặc dùng bản web app.logseq.com` | Giấy phép AGPL-3.0 (copyleft mạnh, áp dụng cả khi cung cấp qua mạng); README nói bản DB đang beta, mobile mới và RTC đang alpha, có thể mất dữ liệu nên cần sao lưu. |
| [`lfnovo/open-notebook`](https://github.com/lfnovo/open-notebook) | 42.052 | MIT | Phương án mã nguồn mở, tự host thay cho Google NotebookLM: tổ chức tài liệu đa phương tiện, tìm kiếm và trò chuyện với AI trên nội dung nghiên cứu, tạo podcast nhiều giọng. | Hỗ trợ hơn 20 nhà cung cấp mô hình kể cả chạy cục bộ qua Ollama, LM Studio; tìm kiếm toàn văn và vector; có REST API và triển khai bằng Docker Compose với SurrealDB. | `curl -o docker-compose.yml https://raw.githubusercontent.com/lfnovo/open-notebook/main/docker-compose.yml && docker compose up -d` | Cần Docker và khoá API của nhà cung cấp AI hoặc máy chủ mô hình cục bộ (Ollama); phải đặt OPEN_NOTEBOOK_ENCRYPTION_KEY trong .env. |
| [`outline/outline`](https://github.com/outline/outline) | 41.292 | Business Source License 1.1 (không phải giấy phép nguồn mở): cấm dùng làm Document Service thương mại cho bên thứ ba; chuyển sang Apache-2.0 vào ngày 2030-11-15 | Cơ sở tri thức (wiki) cộng tác nhanh cho nhóm, viết bằng React và Node.js; có bản hosted tại getoutline.com hoặc tự host. | Có image container chính thức outlinewiki/outline trên Docker Hub; test bằng Vitest, migration bằng Sequelize; có tài liệu kiến trúc docs/ARCHITECTURE.md. | `Theo hướng dẫn tự host tại docs.getoutline.com/s/hosting (image Docker outlinewiki/outline)` | BSL 1.1: không được cung cấp Outline như dịch vụ tài liệu thương mại cho bên thứ ba; dự án yêu cầu không gửi PR do AI tạo và phải thảo luận qua issue trước khi gửi PR. |
| [`TriliumNext/Trilium`](https://github.com/TriliumNext/Trilium) | 38.981 | AGPL-3.0 | Ứng dụng ghi chú phân cấp đa nền tảng, mã nguồn mở, hướng tới xây dựng cơ sở tri thức cá nhân lớn; có bản desktop và máy chủ đồng bộ tự host. | Mã hoá ghi chú theo từng ghi chú, đồng bộ qua máy chủ tự host và có REST API (ETAPI); hỗ trợ canvas Excalidraw, mind map, bản đồ quan hệ, scripting; README nói mở rộng tốt tới hơn 100 000 ghi chú. | `Tải bản phát hành tại github.com/TriliumNext/Trilium/releases/latest hoặc chạy bằng Docker theo docs.triliumnotes.org` | Giấy phép AGPL-3.0; giao diện web chỉ hỗ trợ bản mới nhất của Chrome và Firefox; chưa có app mobile chính thức (dùng giao diện web mobile). |
| [`iOfficeAI/OfficeCLI`](https://github.com/iOfficeAI/OfficeCLI) | 33.400 | Apache-2.0 (kèm file NOTICE bắt buộc giữ khi phân phối lại) | Công cụ dòng lệnh cho AI agent tạo, đọc, sửa tài liệu Word, Excel, PowerPoint mà không cần cài Office; có bộ dựng HTML/PNG để xem trước tài liệu. | Một file nhị phân tự chứa, nhúng sẵn runtime .NET; lệnh watch xem trước trực tiếp trên trình duyệt; xuất JSON có cấu trúc cho từng phần tử tài liệu. | `brew install officecli (hoặc npm install -g @officecli/officecli, hoặc script install.sh trong repo)` | Lệnh officecli install tự cài skill vào các AI coding agent phát hiện được trên máy; build từ nguồn cần .NET 10 SDK. |
| [`Zackriya-Solutions/meetily`](https://github.com/Zackriya-Solutions/meetily) | 32.777 | MIT | Trợ lý cuộc họp AI ưu tiên quyền riêng tư: ghi âm, phiên âm thời gian thực và tóm tắt cuộc họp chạy cục bộ trên máy. | Âm thanh và bản phiên âm không rời khỏi máy, tóm tắt bằng mô hình cục bộ mặc định; hỗ trợ Ollama, Claude, Groq, OpenRouter hoặc endpoint tương thích OpenAI; có bộ cài Windows, macOS Apple Silicon và script cài Linux. | `Linux: tải scripts/install-linux.sh bằng curl -fsSL rồi chạy bằng sh; Windows, macOS: bộ cài từ GitHub Releases` | Windows cần CPU x64 hỗ trợ AVX2; Linux cần x86_64 glibc 2.35 trở lên; nhận diện người nói, MCP, xuất PDF/DOCX thuộc bản PRO trả phí; dùng nhà cung cấp AI đám mây thì bản phiên âm được gửi đi; ghi âm cuộc họp phải tuân thủ luật về sự đồng ý ghi âm (chưa xác minh trong README). |
| [`posquit0/Awesome-CV`](https://github.com/posquit0/Awesome-CV) | 28.975 | LaTeX Project Public License (LPPL) 1.3c | Mẫu LaTeX cho CV, résumé và thư xin việc, dễ tuỳ biến. | Build bằng LuaLaTeX qua latexmk, có Dockerfile ghim digest làm môi trường chuẩn; có bộ test make test kiểm số trang, liên kết, font nhúng; có mẫu trên Overleaf. | `latexmk (hoặc docker build --tag awesome-cv . && docker run --rm --volume "$PWD:/doc" awesome-cv)` | Cần TeX Live đầy đủ (khuyến nghị 2026) với lualatex, latexmk, fontawesome6 và font Source Sans 3, Roboto; không hỗ trợ XeLaTeX và pdfLaTeX. |
| [`dream-num/univer`](https://github.com/dream-num/univer) | 28.964 | Apache-2.0 | Office SDK để nhúng bảng tính và tài liệu soạn thảo vào ứng dụng của bạn; repo chứa lõi Web SDK (mô hình nội dung, engine công thức và render, Facade API). | Lõi Sheets và Docs mở theo Apache-2.0, dùng được trong ứng dụng thương mại; kiến trúc plugin với hệ lệnh hỗ trợ undo/redo; có Facade API cho ứng dụng và agent. | `pnpm add @univerjs/presets @univerjs/preset-sheets-core` | Plugin Web SDK thương mại, Server SDK (cộng tác thời gian thực, nhập/xuất file Office) và AI SDK thương mại được cấp phép riêng. |
| [`super-productivity/super-productivity`](https://github.com/super-productivity/super-productivity) | 23.776 | MIT | Ứng dụng to-do, theo dõi thời gian và lập kế hoạch ngày cho công việc cá nhân, ưu tiên offline và quyền riêng tư. | Tích hợp Jira, GitHub, GitLab, Linear và nhiều công cụ khác; đồng bộ qua SuperSync mã hoá đầu cuối (tự host được), Dropbox hoặc WebDAV; chạy trên Linux, macOS, Windows, Android, iOS và trình duyệt. | `Mở app.super-productivity.com hoặc tải theo wiki 2.01-Downloads-and-Install` | Bản web có một số giới hạn so với bản desktop. |
| [`docmost/docmost`](https://github.com/docmost/docmost) | 22.367 | AGPL-3.0 cho phần lõi; các thư mục apps/server/src/ee, apps/client/src/ee, packages/ee theo giấy phép Docmost Enterprise (packages/ee/License) | Phần mềm wiki và tài liệu cộng tác mã nguồn mở, tự host được. | Cộng tác thời gian thực, lịch sử trang, quản lý quyền theo space và nhóm; vẽ sơ đồ bằng Draw.io, Excalidraw và Mermaid; giao diện hơn 10 ngôn ngữ. | `Theo tài liệu tự host tại docmost.com/docs (có docker-compose.yml trong repo)` | Lõi AGPL-3.0; tính năng Enterprise cần giấy phép Enterprise riêng. |
| [`teableio/teable`](https://github.com/teableio/teable) | 21.999 | AGPL-3.0 cho apps/nestjs-backend và apps/nextjs-app; MIT cho các gói trong packages/; điều khoản bổ sung theo mục 7(e) AGPL: cấm sửa, thay hoặc gỡ tài sản thương hiệu Teable | Nền tảng cơ sở dữ liệu dạng bảng tính trên PostgreSQL (kiểu Airtable) kèm AI chat, tự động hoá và App Builder; tự host hoặc dùng bản cloud. | Có các view Grid, Form, Kanban, Gallery, Calendar cùng công thức, lịch sử bản ghi và cộng tác thời gian thực; dữ liệu nằm trên PostgreSQL thật, có API và truy vấn SQL; bản tự host standalone chạy bằng Docker theo hướng dẫn chính thức | `Docker theo hướng dẫn https://help.teable.ai/en/deploy/docker (phát triển: pnpm install rồi make switch-db-mode)` | AGPL-3.0 (nghĩa vụ công bố mã khi phục vụ qua mạng) và cấm thay/gỡ thương hiệu Teable; tính năng AI và doanh nghiệp trong image chính thức cần gói trả phí kích hoạt bằng license key; bản standalone không có AI/App Builder |
| [`nashsu/llm_wiki`](https://github.com/nashsu/llm_wiki) | 21.730 | GPL-3.0 | Ứng dụng desktop (Tauri v2) dùng LLM đọc tài liệu của người dùng rồi tự xây và duy trì một wiki cá nhân có liên kết, theo mẫu LLM Wiki của Andrej Karpathy. | Nạp được PDF, Office, EPUB/MOBI, ảnh, web clip với truy vết nguồn; hỗ trợ nhiều nhà cung cấp LLM (OpenAI, Anthropic, Google, Ollama, tuỳ chỉnh); có HTTP API cục bộ và MCP server đi kèm, thư mục wiki tương thích Obsidian | `Tải bản cài từ GitHub Releases; build: npm install rồi npm run tauri build` | Cần cấu hình nhà cung cấp LLM (API key + model) hoặc Ollama cục bộ; tìm kiếm vector và tìm web (Tavily, SerpApi, Firecrawl) là tuỳ chọn, cần khoá riêng; giấy phép GPL-3.0 copyleft |
| [`danielmiessler/LifeOS`](https://github.com/danielmiessler/LifeOS) | 19.921 | MIT | Bộ khung (harness) AI cá nhân chạy trên Claude Code hoặc agent khác, lưu mục tiêu, bối cảnh và trí nhớ của người dùng, cung cấp skill, hook và định tuyến để hỗ trợ công việc và đời sống. | Có 97 skill công khai theo README; bộ cài giữ nguyên thư mục USER/ và gộp settings thay vì ghi đè; mã TypeScript và Bash, thiết kế không khoá vào một nhà cung cấp harness | `Tải https://ourlifeos.ai/install.sh bằng curl -fsSL rồi chạy bằng bash (hoặc nhờ AI đọc https://ourlifeos.ai/install)` | Cần harness AI coding (đường được thử nhiều nhất là Claude Code) và bun; README cảnh báo bảo mật không được bảo đảm, người dùng tự chịu trách nhiệm và bộ cài yêu cầu xác nhận điều này; repo công khai được sinh từ cây mã riêng nên PR không merge trực tiếp |
| [`ActivityWatch/activitywatch`](https://github.com/ActivityWatch/activitywatch) | 19.697 | MPL-2.0 | Trình theo dõi thời gian sử dụng máy tính mã nguồn mở, ghi lại ứng dụng, cửa sổ, tab trình duyệt và trạng thái AFK, lưu dữ liệu cục bộ trên máy người dùng. | Dữ liệu lưu cục bộ, người dùng kiểm soát; kiến trúc module gồm server (Python và Rust) cùng các watcher tách riêng làm submodule; có DOI Zenodo để trích dẫn trong nghiên cứu | `Tải bản cài từ https://github.com/ActivityWatch/activitywatch/releases` |  |
| [`docusealco/docuseal`](https://github.com/docusealco/docuseal) | 19.082 | AGPL-3.0 kèm điều khoản bổ sung mục 7(b) (LICENSE_ADDITIONAL_TERMS): phải giữ ghi công DocuSeal gốc trong giao diện tương tác | Nền tảng mã nguồn mở để tạo biểu mẫu PDF, điền và ký điện tử tài liệu trực tuyến, có API và webhook để tích hợp. | Trình dựng trường biểu mẫu PDF kiểu WYSIWYG với 12 loại trường và nhiều người ký mỗi tài liệu; tự động ký điện tử PDF và xác minh chữ ký; chạy một lệnh Docker, mặc định SQLite, hỗ trợ PostgreSQL/MySQL qua DATABASE_URL | `docker run --name docuseal -p 3000:3000 -v.:/data docuseal/docuseal` | AGPL-3.0 và bắt buộc giữ ghi công DocuSeal trong UI; một số tính năng (white-label, SSO/SAML, nhắc tự động, xác minh SMS, gửi hàng loạt, nhúng form) chỉ có ở bản Pro trả phí; gửi email cần cấu hình SMTP |
| [`foambubble/foam`](https://github.com/foambubble/foam) | 17.490 | MIT | Hệ thống quản lý tri thức cá nhân dạng tiện ích Visual Studio Code, dùng ghi chú Markdown liên kết bằng [[wikilink]], có thể xuất bản lên web. | Có đồ thị ghi chú, panel backlink, khám phá tag phân cấp và tự cập nhật liên kết khi đổi tên file; hỗ trợ daily note và template; vault Obsidian thường dùng được ngay làm workspace Foam | `Cài tiện ích foam.foam-vscode từ VS Code Marketplace` | Cần Visual Studio Code; xuất bản web tuỳ chọn dùng GitHub |
| [`suitenumerique/docs`](https://github.com/suitenumerique/docs) | 16.995 | MIT; README cảnh báo một số tính năng (ví dụ xuất PDF) dùng gói XL của BlockNote theo GPL, không tương thích MIT, có thể build không kèm bằng PUBLISH_AS_MIT=true | Trình soạn thảo cộng tác thời gian thực mã nguồn mở (La Suite Docs của chính phủ Pháp), thay thế Notion/Google Docs, hỗ trợ tự host. | Cộng tác thời gian thực với con trỏ, bình luận và phân quyền chi tiết, có soạn thảo ngoại tuyến; nhập .docx/.md và xuất .docx/.odt/.pdf; tự host qua Kubernetes, Docker Compose, Nix hoặc YunoHost | `Xem documentation/installation/README.md (phát triển: make bootstrap rồi make run)` | Gói BlockNote XL theo GPL cho một số tính năng nâng cao; tính năng AI tuỳ chọn cần URL và API key của nhà cung cấp; lưu trữ cần dịch vụ tương thích S3 |
| [`AgriciDaniel/claude-obsidian`](https://github.com/AgriciDaniel/claude-obsidian) | 16.579 | MIT | Plugin Claude Code (bộ Agent Skills) biến vault Obsidian thành wiki tri thức do AI nạp nguồn, liên kết, trả lời có trích dẫn và kiểm tra sức khoẻ, theo mẫu LLM Wiki của Karpathy. | Có 15 skill và 3 agent (verifier, wiki-ingest, wiki-lint) trong repo; dữ liệu là Markdown thuần cục bộ, bản gốc trong inbox/ được giữ nguyên; có bộ test và chạy được trên Codex, OpenCode, Gemini, Cursor, Windsurf qua script cài | `claude plugin marketplace add AgriciDaniel/claude-obsidian rồi claude plugin install claude-obsidian@agricidaniel-claude-obsidian` | Cần Claude Code (hoặc host agent khác hỗ trợ), Python 3.11+ và Obsidian để xem; trên Windows phải dùng WSL để ghi vào vault; nội dung được gửi tới công cụ AI đang dùng |
| [`omnivore-app/omnivore`](https://github.com/omnivore-app/omnivore) | 16.420 | AGPL-3.0 | Ứng dụng đọc-để-sau (read-it-later) mã nguồn mở, lưu bài viết, PDF, newsletter để đọc, tô sáng và ghi chú; hiện chỉ chạy dạng tự host. | Có tô sáng, ghi chú, tìm kiếm, nhãn và hỗ trợ ngoại tuyến; có ứng dụng iOS, Android, tiện ích trình duyệt Chrome, Safari, Firefox, Edge và client RSS; có plugin Logseq và Obsidian | `Xem self-hosting/GUIDE.md (phát triển: cd self-hosting/docker-compose/self-build rồi docker compose up)` | Dịch vụ cloud đã ngừng từ tháng 11/2024, chỉ còn tự host; AGPL-3.0 copyleft khi phục vụ qua mạng |
| [`documenso/documenso`](https://github.com/documenso/documenso) | 15.813 | AGPL-3.0; riêng thư mục packages/ee theo Documenso Commercial License (chỉ dùng production khi có gói Enterprise) | Nền tảng ký tài liệu điện tử mã nguồn mở, thay thế DocuSign, có thể tự host. | Tự host được bằng Docker hoặc Docker Compose theo tài liệu chính thức; stack TypeScript, React Router v7, Hono, Prisma, tRPC; ký PDF bằng @libpdf/core | `npm run dx rồi npm run dev (phát triển); tự host theo hướng dẫn Docker` | AGPL-3.0 buộc công khai mã sửa đổi khi cung cấp qua mạng; tính năng trong packages/ee cần gói Enterprise trả phí để dùng production; không nhận PR từ bên ngoài |
| [`liketrek/TREK`](https://github.com/liketrek/TREK) | 15.737 | AGPL-3.0; kèm chính sách thương hiệu (TRADEMARKS.md) và dữ liệu bên thứ ba CC BY 4.0 (NOTICE.md) | Ứng dụng lập kế hoạch du lịch tự host: lên lịch trình cộng tác thời gian thực trên bản đồ, tour đi bộ/đạp xe, đặt chỗ, chia chi phí, nhật ký và trợ lý AI. | Bản đồ Leaflet/MapLibre với OpenFreeMap, không cần token; dự báo thời tiết 16 ngày từ Open-Meteo, không cần khoá; triển khai bằng Docker, Docker Compose, Helm, TrueNAS SCALE | `docker run -d --name trek -p 3000:3000 -e ENCRYPTION_KEY=... mauriceboe/trek` | Cần ENCRYPTION_KEY; Google Places/Amap cần khoá API; tên và logo TREK chịu chính sách thương hiệu riêng; dữ liệu ranh giới CC BY 4.0 phải ghi nguồn |
| [`xournalpp/xournalpp`](https://github.com/xournalpp/xournalpp) | 15.687 | GPL-2.0 | Phần mềm ghi chú viết tay viết bằng C++, hỗ trợ bút cảm ứng lực và chú thích lên PDF. | Hỗ trợ bút cảm ứng lực (Wacom, Huion, XP Pen); chú thích lên PDF, xuất SVG/PNG/PDF từ GUI và dòng lệnh; plugin bằng Lua và hỗ trợ LaTeX | `sudo apt install xournalpp hoặc flatpak install flathub com.github.xournalpp.xournalpp` | Tính năng LaTeX cần cài LaTeX riêng |
| [`streetwriters/notesnook`](https://github.com/streetwriters/notesnook) | 14.952 | GPL-3.0 | Ứng dụng ghi chú mã hoá đầu-cuối, thay thế Evernote, có bản web, desktop và di động. | Mã hoá mọi thứ trên thiết bị bằng XChaCha20-Poly1305 và Argon2; monorepo gồm client web (React), desktop (Electron), mobile (React Native) và web clipper; có công cụ Vericrypt để tự kiểm chứng mã hoá |  | Đồng bộ cần tài khoản có email; dịch vụ chịu chính sách bảo mật và điều khoản của Notesnook |
| [`Thysrael/Horizon`](https://github.com/Thysrael/Horizon) | 14.539 | MIT | Radar tin tức dùng AI: gom tin từ RSS, Hacker News, Reddit, Telegram, X, GitHub…, chấm điểm, lọc trùng và tạo bản tin hằng ngày tiếng Anh và tiếng Trung. | Profile cấu hình tiêu chí chấm điểm và đầu ra riêng cho từng loại nội dung; phát bản tin qua Markdown, Pages, email, WeChat và webhook; có MCP và Agent Skill để trợ lý AI điều khiển | `uv sync (sau khi git clone) hoặc pip install -e .` | Cần khoá API mô hình (OpenAI, Gemini…) qua biến môi trường, hoặc đăng nhập ChatGPT cho thuê bao đủ điều kiện |

**Chưa thêm (1 repo, giữ trong file dữ liệu):** `storytold/wordcraft` (còn thử nghiệm: README ghi WordCraft đang ở giai đoạn alpha, ước tính khoảng 60% sẵn sàng cho công việc thực).

#### 6c.5.16 Nền tảng AI, RAG & Workflow

Đọc mã 34 repo, giữ 29.

| Repo | ★ (18/11/2026) | Giấy phép | Làm gì | Điểm mạnh (đọc mã) | Cài | Điều kiện dùng |
|---|---|---|---|---|---|---|
| [`ChatGPTNextWeb/NextChat`](https://github.com/ChatGPTNextWeb/NextChat) | 88.972 | MIT | Giao diện trò chuyện AI nhẹ, hỗ trợ Claude, DeepSeek, GPT, Gemini; chạy dạng web (Vercel/Docker) hoặc ứng dụng desktop Tauri. | Triển khai một chạm lên Vercel, client desktop khoảng 5MB cho Linux/Windows/macOS; dữ liệu lưu cục bộ trong trình duyệt; hỗ trợ MCP, plugin và Realtime Chat | `docker pull yidadaa/chatgpt-next-web` | Cần khoá API của nhà cung cấp mô hình (ví dụ OPENAI_API_KEY); MCP cần đặt ENABLE_MCP=true khi build |
| [`pathwaycom/serviette`](https://github.com/pathwaycom/serviette) | 58.709 | MIT | Máy chủ RAG không cần code trên Pathway: trỏ vào thư mục tài liệu, chọn vector database và embedder trong một file YAML, có chat và REST API trích dẫn nguồn, cập nhật trong vài giây khi tài liệu đổi. | Hỗ trợ 8 vector database gồm pgvector, Qdrant, Milvus, ChromaDB, Weaviate, Pinecone, MongoDB Atlas; benchmark lập chỉ mục tới 50 GB văn bản; embedder cục bộ miễn phí là mặc định | `pip install serviette rồi serviette demo --embedder openai` | Cần PATHWAY_LICENSE_KEY miễn phí (đăng nhập GitHub hoặc LinkedIn); API mô hình sinh câu trả lời tính phí theo lượt nếu dùng; cần pip 23.1 trở lên |
| [`AstrBotDevs/AstrBot`](https://github.com/AstrBotDevs/AstrBot) | 47.132 | AGPL-3.0; kèm EULA.md (người dùng đồng ý khi cài, chạy) | Nền tảng chatbot Agent tất cả trong một, kết nối LLM với các ứng dụng nhắn tin như QQ, WeChat Work, Feishu, DingTalk, Telegram, Slack. | Hỗ trợ MCP, Skills, cơ sở tri thức và nén ngữ cảnh tự động; hơn 1000 plugin cài một chạm; Agent Sandbox chạy code và shell cô lập, có WebUI | `uv tool install astrbot --python 3.12 rồi astrbot init rồi astrbot run` | Cần khoá API mô hình và tài khoản bot của nền tảng nhắn tin; EULA ràng buộc người dùng khi cài đặt; AGPL-3.0 buộc công khai mã sửa đổi khi cung cấp qua mạng |
| [`chatboxai/chatbox`](https://github.com/chatboxai/chatbox) | 42.390 | GPL-3.0 | Ứng dụng khách desktop (Community Edition) để trò chuyện với ChatGPT, Claude, Gemini, Ollama và các LLM khác trên Windows, macOS, Linux. | Hỗ trợ nhiều nhà cung cấp LLM gồm OpenAI, Azure OpenAI, Claude, Gemini, Ollama; dữ liệu lưu cục bộ trên máy; có bản desktop, web, iOS và Android | `Tải bộ cài từ trang releases của repo rồi cấu hình nhà cung cấp AI trong settings` | Cần khoá API của nhà cung cấp LLM (hoặc Ollama cục bộ); GPLv3 copyleft; repo là bản Community, đồng bộ code với bản pro |
| [`mindsdb/mindshub`](https://github.com/mindsdb/mindshub) | 39.865 | MIT (thành phần đi kèm theo giấy phép riêng của từng submodule) | Không gian làm việc cho agent (MindsHub) để làm việc tri thức và phát triển phần mềm, chọn được nhiều mô hình; repo là superproject gom app desktop/web, backend agent và data vault. | Gom 4 submodule frontend, core_api, core_agent (anton), data-vault để build toàn stack từ nguồn; có Makefile với make setup, make dev, make dist-mac, make dist-win; kho kết nối dữ liệu giữ thông tin xác thực theo từng kết nối | `git clone --recurse-submodules https://github.com/mindsdb/minds.git && make setup && make dev` | Bản hosted có gói Pro trả phí; Linux phải build từ nguồn; README dẫn tên repo mindsdb/minds |
| [`The-Vibe-Company/quivr`](https://github.com/The-Vibe-Company/quivr) | 39.657 | MIT | Engine mã nguồn mở (Go) lưu trữ, tìm kiếm và cảnh báo trên nội dung liên tục đổ về (bài báo, email, PDF, RSS) qua HTTP API, không có giao diện riêng. | Tìm kiếm theo từ khoá, theo ngữ nghĩa hoặc kết hợp, kết quả trỏ tới đúng đoạn, tài liệu và phiên bản; plugin là dịch vụ HTTP nhỏ viết bằng ngôn ngữ bất kỳ; có lệnh quivr mcp cho agent AI và API /v0 giữ tương thích suốt 2.x | `git clone https://github.com/The-Vibe-Company/quivr.git && cd quivr && make dev` | Cần Linux x86_64 hoặc Mac Apple Silicon, Docker Compose v2, Go, Python 3.12 và jq; lần chạy đầu tải khoảng 1 GB |
| [`ItzCrazyKns/Vane`](https://github.com/ItzCrazyKns/Vane) | 38.240 | MIT | Công cụ trả lời bằng AI tự host, chú trọng riêng tư, kết hợp tìm kiếm web qua SearxNG với LLM cục bộ (Ollama) hoặc đám mây và trích dẫn nguồn. | Ảnh Docker đóng gói sẵn cả Vane và SearxNG; có chế độ Speed, Balanced, Quality và tìm theo web, thảo luận, bài học thuật; hỗ trợ tải lên tệp PDF, văn bản, ảnh để hỏi đáp | `docker run -d -p 3000:3000 -v vane-data:/home/vane/data --name vane itzcrazykns1337/vane:latest` | Cần khoá API nhà cung cấp LLM hoặc Ollama; SearxNG tự quản phải bật định dạng JSON và Wolfram Alpha |
| [`yetone/magpie`](https://github.com/yetone/magpie) | 38.190 | MIT | Ứng dụng (menu bar, TUI, web, CLI) và gateway cục bộ cho phép đổi mô hình của nhiều agent lập trình (Claude Code, Codex, Gemini CLI…) từ một chỗ, tự chuyển tài khoản khi hết quota. | Gateway tại 127.0.0.1:3425 dịch qua lại giữa OpenAI Chat, OpenAI Responses, Anthropic Messages và Gemini kể cả streaming và tool call; có tuỳ chọn che (mask) khoá, mật khẩu, email trên máy trước khi gửi đi; chạy trên macOS, Windows, Linux, Docker và Termux | `Tải app từ usemagpie.ai hoặc chạy script cài https://usemagpie.ai/install.sh bằng sh` | Cần khoá API hoặc gói đăng ký của nhà cung cấp; app đọc thông tin đăng nhập của agent (file Claude Code, Codex, Keychain) trừ khi tắt; dùng gói đăng ký cho agent khác có thể vướng điều khoản nhà cung cấp (chưa xác minh) |
| [`khoj-ai/khoj`](https://github.com/khoj-ai/khoj) | 38.161 | AGPL-3.0 | Ứng dụng AI cá nhân (second brain) tự host được: trò chuyện với LLM cục bộ hoặc online, trả lời từ internet và tài liệu riêng, tạo agent và tự động hoá nghiên cứu. | Đọc PDF, Markdown, Notion, Word, org-mode; truy cập từ trình duyệt, Obsidian, Emacs, desktop, điện thoại, WhatsApp; có ảnh Docker và gói PyPI | `pip install 'khoj[local]'` | AGPL-3.0 (copyleft cả khi phục vụ qua mạng); cần khoá API nếu dùng LLM online |
| [`Tencent/WeKnora`](https://github.com/Tencent/WeKnora) | 37.678 | MIT, trừ các thành phần bên thứ ba liệt kê trong LICENSE theo giấy phép riêng | Khung quản lý tri thức doanh nghiệp dựa trên LLM của Tencent: RAG có trích dẫn, agent nhiều bước và wiki trên cùng kho tri thức. | Tự đồng bộ từ Feishu, Confluence, GitLab, Notion, RSS và hơn 10 định dạng tài liệu; RBAC nhiều workspace với 4 vai trò và nhật ký audit; có MCP server tích hợp và 29 nhà cung cấp mô hình dựng sẵn | `git clone https://github.com/Tencent/WeKnora.git && cd WeKnora && cp .env.example .env && docker compose up -d` | Cần Docker, Docker Compose, Git; cần cấu hình mô hình (khoá API hoặc Ollama) |
| [`SillyTavern/SillyTavern`](https://github.com/SillyTavern/SillyTavern) | 35.764 | AGPL-3.0 | Giao diện frontend LLM cho người dùng chuyên sâu, chạy bằng Node.js. | Có script khởi động Start.bat, start.sh và Dockerfile; mã giao diện kèm thư mục locales đa ngôn ngữ; tài liệu riêng tại docs.sillytavern.app |  | AGPL-3.0; README chỉ dẫn tới tài liệu ngoài, chi tiết yêu cầu chưa xác minh |
| [`onyx-dot-app/onyx`](https://github.com/onyx-dot-app/onyx) | 33.445 | MIT Expat cho phần ngoài thư mục ee; nội dung trong các thư mục ee theo Onyx Enterprise License | Lớp tri thức và ngữ cảnh cho đội nhóm và agent AI: index dữ liệu từ hơn 50 ứng dụng, agentic RAG, deep research, agent tuỳ biến, tự host được. | Triển khai tự host, có thể air-gap, qua Docker, Kubernetes, Helm, Terraform; có chế độ Lite dưới 1 GB RAM; truy cập qua web, desktop, bot Slack và Discord, MCP server, tiện ích Chrome | `Chạy script cài https://onyx.app/install_onyx.sh bằng bash` | Tính năng trong thư mục ee (SSO, RBAC…) thuộc bản Enterprise theo giấy phép riêng; cần nhà cung cấp LLM (tự host hoặc thương mại) |
| [`Cinnamon/kotaemon`](https://github.com/Cinnamon/kotaemon) | 25.914 | Apache License 2.0 | Giao diện web RAG mã nguồn mở để hỏi đáp trên tài liệu, kiêm khung dựng pipeline RAG cho nhà phát triển (xây trên Gradio). | Retriever lai full-text và vector có re-ranking, trích dẫn kèm xem PDF tô sáng trong trình duyệt; hỗ trợ nhiều người dùng, LLM cục bộ (ollama, llama-cpp-python) lẫn API (OpenAI, Azure, Groq); có ảnh Docker lite/full cho linux/amd64 và linux/arm64, có ví dụ GraphRAG/LightRAG. | `docker run -p 7860:7860 -it --rm ghcr.io/cinnamon/kotaemon:main-lite` | Cần Python ≥ 3.10; khoá API của nhà cung cấp LLM nếu không dùng mô hình cục bộ; định dạng ngoài pdf/html/xlsx cần Unstructured hoặc ảnh full. |
| [`HKUDS/RAG-Anything`](https://github.com/HKUDS/RAG-Anything) | 24.604 | MIT License | Khung RAG đa phương thức xây trên LightRAG, xử lý tài liệu có văn bản, ảnh, bảng, công thức từ khâu phân tích đến truy vấn. | Có báo cáo kỹ thuật arXiv 2510.12323 và gói PyPI raganything; parser MinerU hoặc Docling, xử lý chuyên biệt ảnh/bảng/phương trình và đồ thị tri thức đa phương thức; có chế độ truy vấn tăng cường bằng VLM. | `pip install raganything` | Cần khoá API LLM/embedding (ví dụ README dùng OpenAI); parser MinerU mặc định chỉ chạy Python 3.10–3.13 và chưa hỗ trợ MinerU 4.x. |
| [`1Panel-dev/MaxKB`](https://github.com/1Panel-dev/MaxKB) | 23.169 | GNU GPL v3 | Nền tảng mã nguồn mở xây agent cấp doanh nghiệp: pipeline RAG, workflow agentic, gọi công cụ MCP, nhúng vào hệ thống bên thứ ba. | Một lệnh docker run là có giao diện web ở cổng 8080; không gắn mô hình, hỗ trợ cả mô hình riêng (DeepSeek, Llama, Qwen) và công khai (OpenAI, Claude, Gemini); đa phương thức văn bản, ảnh, âm thanh, video; stack Vue + Django + LangChain + PostgreSQL/pgvector. | `docker run -d --name=maxkb --restart=always -p 8080:8080 -v ~/.maxkb:/opt/maxkb 1panel/maxkb` | GPLv3 (copyleft); mật khẩu admin mặc định công bố trong README phải đổi ngay; cần khoá API khi dùng mô hình công khai. |
| [`dyad-sh/dyad`](https://github.com/dyad-sh/dyad) | 22.314 | Apache License 2.0 cho mã ngoài src/pro; mã trong src/pro theo Functional Source License 1.1 (Apache 2.0 future license) | Ứng dụng desktop dựng app bằng AI chạy cục bộ, tương tự Lovable, v0, Bolt nhưng chạy trên máy người dùng. | Không cần đăng ký, tải về là dùng; tự mang khoá API (BYOK), không khoá nhà cung cấp; chạy trên Mac và Windows, có bộ test e2e Playwright trong repo. | `Tải bản cài từ https://www.dyad.sh/#download` | Cần khoá API AI của riêng người dùng; phần src/pro là fair-source FSL 1.1 (giới hạn dùng cạnh tranh); đóng góp cần ký CLA. |
| [`vercel/chatbot`](https://github.com/vercel/chatbot) | 21.060 | Apache License 2.0 | Mẫu ứng dụng chatbot mã nguồn mở dựng bằng Next.js App Router và AI SDK, có lưu lịch sử chat và xác thực. | Dùng AI SDK với Vercel AI Gateway truy cập nhiều mô hình (Mistral, Moonshot, DeepSeek, OpenAI, xAI); giao diện shadcn/ui + Tailwind; lưu dữ liệu bằng Neon Postgres và Vercel Blob, xác thực Auth.js; triển khai một nhấp lên Vercel. | `pnpm install && pnpm db:migrate && pnpm dev` | Ngoài Vercel cần AI_GATEWAY_API_KEY; cần Postgres và Blob storage (mặc định dịch vụ Vercel/Neon); hướng dẫn chạy cục bộ dùng Vercel CLI liên kết tài khoản. |
| [`kortix-ai/CompanyOS`](https://github.com/kortix-ai/CompanyOS) | 20.759 | Elastic License 2.0 (không phải giấy phép OSI: cấm cung cấp dưới dạng dịch vụ hosted/managed, cấm vượt qua cơ chế license key); có thêm White-Label License miễn phí với điều kiện dùng Platinum làm nhà cung cấp compute độc quyền | Bộ khung agent cloud-native cho doanh nghiệp: agent chạy liên tục theo sự kiện, song song, mỗi phiên có máy tính đám mây riêng và chung bộ nhớ công ty. | Kích hoạt agent bằng lịch, webhook ký, sự kiện connector và change request; mọi thay đổi lên main qua change request người duyệt; tự host bằng một stack Docker Compose (kortix self-host start), dùng mô hình bất kỳ với khoá riêng. | `Tải script https://kortix.com/install bằng curl rồi chạy bằng bash; sau đó kortix self-host start` | Elastic License 2.0 giới hạn dùng làm dịch vụ cho bên thứ ba; white-label buộc dùng Platinum làm compute độc quyền; self-host vẫn kéo ảnh từ Docker Hub; cần khoá nhà cung cấp mô hình. |
| [`rocketride-org/rocketride-server`](https://github.com/rocketride-org/rocketride-server) | 20.021 | MIT License (Copyright 2026 Aparavi Software AG) | Meta-harness AI mã nguồn mở với runtime C++ để dựng, kiểm thử, phát hành pipeline và agent AI, điều khiển từ IDE, terminal hoặc coding agent. | Engine C++ cùng SDK Python (pip install rocketride) và TypeScript (npm install rocketride), có extension VS Code/Open VSX và MCP server; pipeline lưu dạng file .pipe JSON để review trong git; chạy cục bộ, Docker, on-prem hoặc Helm, README nói không có bản enterprise trả phí. | `pip install rocketride` | Ảnh Docker chỉ amd64 (Apple Silicon cần --platform linux/amd64); RocketRide Cloud là dịch vụ tuỳ chọn. |
| [`nesquena/hermes-webui`](https://github.com/nesquena/hermes-webui) | 19.555 | MIT License | Giao diện web nhẹ cho Hermes Agent (Nous Research), gần tương đương đầy đủ trải nghiệm CLI: phiên chat, duyệt file workspace, profile, chủ đề. | Không bước build, chỉ Python và vanilla JS; khởi chạy bằng bootstrap.py/start.sh/ctl.sh, có Docker Compose và Nix flake/module NixOS; thư mục tests có hơn 2000 file. | `git clone https://github.com/nesquena/hermes-webui.git && cd hermes-webui && python3 bootstrap.py` | Cần Hermes Agent (bootstrap tự thử cài từ script chính thức nếu thiếu) và mô hình/khoá đã cấu hình trong Hermes; truy cập từ xa khuyến nghị qua SSH tunnel. |
| [`lss233/kirara-ai`](https://github.com/lss233/kirara-ai) | 19.293 | GNU AGPL v3 | Chatbot đa nền tảng (QQ, Telegram, Discord, WeChat) kết nối các LLM phổ biến, có WebUI quản lý, workflow và chợ plugin. | Hỗ trợ OpenAI, DeepSeek, Claude, Gemini, Qwen, Kimi và mô hình vẽ Stable Diffusion, Flux, Midjourney; có HTTP API, preset nhân cách, chuyển văn bản thành giọng nói (Azure, VITS); có gói PyPI, ảnh Docker, kiểm Mypy và đo coverage Codecov. | `Xem hướng dẫn tại https://kirara-docs.app.lss233.com/guide/getting-started.html` | AGPLv3 (copyleft cả khi chạy qua mạng); cần khoá API LLM và tài khoản bot trên từng nền tảng chat; tài liệu và cộng đồng chủ yếu tiếng Trung. |
| [`langbot-app/LangBot`](https://github.com/langbot-app/LangBot) | 19.067 | Apache-2.0 | Nền tảng mã nguồn mở xây bot nhắn tức thời dùng LLM, nối mô hình với Discord, Telegram, Slack, WeChat, QQ, Lark và nhiều nền tảng khác. | Hỗ trợ hơn 10 nền tảng IM (Discord, Telegram, Slack, LINE, QQ, WeChat, WeCom, Lark, DingTalk, KOOK, Matrix); có bảng quản trị web, RAG, hệ plugin và hỗ trợ MCP; tích hợp Dify, Coze, n8n, Langflow | `curl -fsSL https://langbot.app/install.sh rồi chạy bằng bash (hoặc cd docker && docker compose --profile all up -d)` | Cần khoá API nhà cung cấp LLM và tài khoản bot của từng nền tảng IM; đóng góp phải ký CLA (CLA.md) |
| [`arc53/DocsGPT`](https://github.com/arc53/DocsGPT) | 18.375 | MIT | Nền tảng tự host xây agent AI trả lời dựa trên tài liệu có trích nguồn, kèm workflow trực quan, công cụ, widget, API tương thích OpenAI và máy chủ MCP. | Toàn bộ kể cả SSO, nhóm, hạn mức đều theo MIT; nạp tri thức từ PDF, Office, web, âm thanh và đồng bộ Google Drive, SharePoint, Confluence, GitHub, S3; có guardrail chặn PII, bí mật, prompt injection | `curl -fsSL https://docs.ac/install rồi chạy bằng bash` | Cần Docker cho trình cài; cần khoá API mô hình đám mây hoặc mô hình cục bộ (Ollama, vLLM) |
| [`MODSetter/SurfSense`](https://github.com/MODSetter/SurfSense) | 16.893 | Apache-2.0 (dòng đầu: Copyright (c) SurfSense) | Ứng dụng desktop mã nguồn mở kiểu NotebookLM chạy trên máy, có agent nghiên cứu, chuyển đổi và chỉnh sửa tài liệu cục bộ, chạy được không mạng. | Chỉ mục nằm trên đĩa, tự chọn mô hình cục bộ hay từ xa, không cần tài khoản; sửa Word dưới dạng tracked changes, tạo Excel có công thức và biểu đồ, xử lý PDF (điền form, gộp, tách); có bản cài Windows, macOS, Linux và Docker | `Tải bản cài tại surfsense.com/downloads hoặc curl -fsSL https://raw.githubusercontent.com/MODSetter/SurfSense/main/docker/scripts/install.sh rồi chạy bằng bash` | Plugin của SurfSense (Google Search, YouTube, Reddit, Amazon…) cần license SurfSense trả phí (dùng thử 14 ngày, nhập email); thu thập dữ liệu các trang này cần tự cân nhắc ToS; chuyển đổi Office cần LibreOffice |
| [`corsairdev/corsair`](https://github.com/corsairdev/corsair) | 15.650 | Apache-2.0 | Nền tảng tích hợp sản phẩm (dựa trên REST) để agent và người dùng ứng dụng kết nối tới các dịch vụ bên thứ ba với một cú pháp chung, lo OAuth, làm mới token, webhook. | Kho có khoảng 737 gói plugin tích hợp (@corsair-dev/*); dùng chung cho agent, backend và dashboard, không chỉ MCP; tự host được, thông tin xác thực mã hoá lưu trong CSDL của mình | `npm install corsair @corsair-dev/slack (một gói mỗi dịch vụ)` | Corsair Hub (dịch vụ host cho trang OAuth, callback) cần khoá API, signing secret và tài khoản tại hub.corsair.dev; có Privacy Policy và Terms of Service riêng |
| [`n8n-io/self-hosted-ai-starter-kit`](https://github.com/n8n-io/self-hosted-ai-starter-kit) | 15.376 | Apache-2.0 | Mẫu Docker Compose dựng nhanh môi trường AI cục bộ gồm n8n tự host, Ollama, Qdrant và PostgreSQL. | Có profile riêng cho GPU Nvidia, GPU AMD trên Linux và CPU; kèm sẵn workflow mẫu chat với Llama3.2 qua Ollama; do chính tổ chức n8n-io biên soạn | `git clone https://github.com/n8n-io/self-hosted-ai-starter-kit.git && cd self-hosted-ai-starter-kit && cp .env.example .env && docker compose --profile cpu up` | Cần Docker; README nói chưa tối ưu cho production, hợp cho proof-of-concept; phải tự đổi secret/mật khẩu trong .env; bản thân n8n theo giấy phép riêng của n8n (chưa xác minh trong repo này) |
| [`GaiZhenbiao/ChuanhuChatGPT`](https://github.com/GaiZhenbiao/ChuanhuChatGPT) | 15.240 | GPL-3.0 | Giao diện web nhẹ dựa trên Gradio cho ChatGPT và nhiều LLM khác, kèm hỏi đáp theo tệp, tìm kiếm web, agent và chạy mô hình cục bộ. | Hỗ trợ nhiều API (OpenAI, Azure, Gemini, Claude, DeepSeek, MiniMax…) và mô hình cục bộ (ChatGLM, LLaMA, Qwen); cài được như ứng dụng PWA, giao diện thích ứng di động; hỗ trợ fine-tune GPT-3.5 | `git clone https://github.com/GaiZhenbiao/ChuanhuChatGPT.git && cd ChuanhuChatGPT && pip install -r requirements.txt && python ChuanhuChatbot.py` | Cần khoá API nhà cung cấp trong config.json; GPL-3.0 copyleft khi phân phối bản sửa đổi |
| [`botpress/botpress`](https://github.com/botpress/botpress) | 15.002 | MIT (Copyright 2023 Botpress Technologies, Inc.) | Kho mã mở của Botpress Cloud gồm các integration công khai trên Botpress Hub, CLI, SDK, API client và bot mẫu viết bằng mã. | Thư mục integrations có 83 integration công khai do Botpress duy trì; CLI bp có init và deploy integration lên workspace; SDK và CLI phát hành trên npm (@botpress/sdk, @botpress/cli) | `npm install -g @botpress/cli && bp init` | Cần tài khoản Botpress Cloud để deploy; repo không phải bản tự host — Botpress v12 on-premise nằm ở repo botpress/v12; integration đã công khai thì không cập nhật lại được |
| [`llmware-ai/llmware`](https://github.com/llmware-ai/llmware) | 14.820 | Apache-2.0 (kèm file NOTICE) | Framework Python xây ứng dụng LLM dựa trên tri thức chạy cục bộ, riêng tư, gồm danh mục mô hình và pipeline RAG. | Danh mục 300+ mô hình, trong đó 50+ mô hình SLIM, BLING, DRAGON, Industry-BERT do llmware tinh chỉnh; hỗ trợ GGUF, OpenVINO, ONNXRuntime (cả QNN) và PyTorch; Library phân tích, chia đoạn, nhúng nhiều định dạng tệp với nhiều vector DB | `pip3 install llmware` | Python 3.10–3.14; mô hình đám mây (OpenAI, Anthropic, Google) cần khoá API riêng |

**Chưa thêm (5 repo, giữ trong file dữ liệu):** `xtekky/gpt4free` (dựa vào nhà cung cấp bên thứ ba không chính thức, dự án tự nêu chỉ cho mục đích giáo dục, rủi ro điều khoản dịch vụ); `router-for-me/CLIProxyAPI` (chức năng chính là dùng tài khoản thuê bao qua proxy, rủi ro điều khoản nhà cung cấp); `decolua/9router` (xoay vòng nhiều tài khoản và gói đăng ký qua proxy, rủi ro điều khoản nhà cung cấp); `RasaHQ/rasa` (dự án tự nêu ngừng/thay thế: README ghi Rasa Open Source đang ở chế độ bảo trì (Maintenance Mode); hướng tương lai là Hello Rasa và CALM); `lidge-jun/opencodex` (gộp nhiều tài khoản thuê bao qua proxy, dự án tự cảnh báo có thể bị khoá tài khoản).

#### 6c.5.17 Quy chuẩn & Thực hành tốt

Đọc mã 2 repo, giữ 2.

| Repo | ★ (18/11/2026) | Giấy phép | Làm gì | Điểm mạnh (đọc mã) | Cài | Điều kiện dùng |
|---|---|---|---|---|---|---|
| [`realworld-apps/realworld`](https://github.com/realworld-apps/realworld) | 84.386 | MIT (Copyright 2021 Thinkster, 2026 c4ffein) | Dự án RealWorld: cùng một ứng dụng bản sao Medium.com được dựng bằng nhiều frontend và backend khác nhau, tất cả theo chung một đặc tả API. | Hơn 100 bản triển khai liệt kê trên CodebaseShow; có đặc tả API, bộ test E2E chung và theme CSS chung; có API host công khai api.realworld.show không cần khoá |  | Logo framework có giấy phép riêng (docs/non-included/LICENSES_LOGOS.md) |
| [`you-dont-need/You-Dont-Need-Lodash-Underscore`](https://github.com/you-dont-need/You-Dont-Need-Lodash-Underscore) | 19.111 | MIT (Copyright (c) 2018 You-Dont-Need) | Danh sách đối chiếu các hàm Lodash/Underscore với cách viết JavaScript gốc (ES5/ES6+), kèm plugin ESLint cảnh báo chỗ có thể dùng hàm gốc thay thư viện. | Có plugin ESLint phát hành trên npm (eslint-plugin-you-dont-need-lodash-underscore, package.json bản 6.14.0) với cấu hình sẵn plugin:you-dont-need-lodash-underscore/compatible; README chia mục Array, Collection, Object… và ghi rõ khác biệt null-safety giữa Lodash và hàm gốc; repo có thư mục tests và script test (mocha). | `npm install --save-dev eslint-plugin-you-dont-need-lodash-underscore` |  |

#### 6c.5.18 Skill, Prompt & Mẫu cho AI

Đọc mã 8 repo, giữ 6.

| Repo | ★ (18/11/2026) | Giấy phép | Làm gì | Điểm mạnh (đọc mã) | Cài | Điều kiện dùng |
|---|---|---|---|---|---|---|
| [`alchaincyf/nuwa-skill`](https://github.com/alchaincyf/nuwa-skill) | 38.518 | MIT (Copyright (c) 2026 Huashu (花叔)) | Agent Skill "女娲" chưng cất cách nghĩ, mô hình tư duy và giọng nói của một nhân vật công khai (Munger, Naval, Musk…) thành skill riêng: chỉ cần nhập tên, skill tự nghiên cứu, trích xuất và kiểm định. | Theo chuẩn mở Agent Skills, README liệt kê chạy được trên Claude Code, Codex, Cursor, OpenClaw, Hermes, Gemini CLI… và có plugin cho DeepSeek Harness; thư mục examples có 15 skill nhân vật đã chưng cất sẵn; mỗi skill sinh ra có mục "giới hạn trung thực" nói rõ điều không làm được. | `npx skills add alchaincyf/nuwa-skill` | Chỉ dựa trên thông tin công khai về người thật; README tự nêu: không chưng cất được trực giác, chỉ là ảnh chụp tới mốc nghiên cứu, phát ngôn công khai không đồng nghĩa niềm tin thật. |
| [`JimLiu/baoyu-skills`](https://github.com/JimLiu/baoyu-skills) | 27.646 | MIT (Copyright (c) 2026 Jim Liu); README ghi skill đăng lên ClawHub được phát hành theo MIT-0 theo luật registry đó | Bộ 21 Agent Skill cho Claude Code/Codex phục vụ sản xuất nội dung: sinh ảnh bìa, minh hoạ, infographic, slide, truyện tranh, dịch bài, chuyển URL/YouTube/X sang Markdown và đăng lên WeChat, Weibo, X. | Thư mục skills có 21 skill độc lập, cài riêng từng skill được; hỗ trợ nhiều backend sinh ảnh (OpenAI, Azure, OpenRouter, Google, DashScope, Z.AI, MiniMax, Seedream…) chọn qua biến môi trường; có marketplace plugin Claude Code và script đăng từng skill lên ClawHub. | `npx skills add jimliu/baoyu-skills` | Cần Node.js và npx bun; nhiều skill cần khoá API (OPENAI_API_KEY, GOOGLE_API_KEY…) hoặc thông tin xác thực WeChat; hai skill baoyu-danger-gemini-web và baoyu-danger-x-to-markdown dùng API đảo ngược (reverse-engineered) của Gemini Web và X, dùng cookie đăng nhập, bắt buộc người dùng chấp thuận rủi ro trước khi chạy — có thể trái điều khoản dịch vụ. |
| [`KKKKhazix/khazix-skills`](https://github.com/KKKKhazix/khazix-skills) | 22.367 | MIT (Copyright (c) 2026 数字生命卡兹克) | Bộ 6 Agent Skill tác giả dùng hằng ngày: leader (biến ý tưởng mơ hồ thành mục tiêu agent chạy được lâu), storage-analyzer (quét ổ đĩa và đề xuất dọn), aihot (lấy tin AI từ aihot.news), neat-freak (đối soát tài liệu/CLAUDE.md/bộ nhớ agent), hv-analysis (báo cáo nghiên cứu), khazix-writer (viết bài tiếng Trung theo giọng tác giả). | Theo chuẩn Agent Skills, dùng được với Claude Code, Codex và hơn 40 agent; storage-analyzer hỗ trợ macOS, Windows, Linux, quét chỉ đọc, xoá cần xác nhận và có CI đa nền tảng; workflow validate chạy test, kiểm gói và fixture đánh giá trên Ubuntu, macOS, Windows. | `Nói với agent: Install this skill: https://github.com/KKKKhazix/khazix-skills/tree/main/<skill-name>` | Cần agent có quyền hệ thống tệp, duyệt web hoặc chạy lệnh cho các skill quét máy/nghiên cứu; aihot phụ thuộc dịch vụ aihot.news (không cần khoá API). |
| [`nidhinjs/prompt-master`](https://github.com/nidhinjs/prompt-master) | 16.111 | MIT (Copyright (c) 2026 Nidhin Joseph Nelson) | Skill cho Claude viết prompt chính xác cho các công cụ AI khác (ChatGPT, Cursor, Claude Code, Midjourney, Stable Diffusion, Sora…): dò công cụ đích, trích ý định, hỏi tối đa 3 câu làm rõ rồi xuất một prompt gọn. | Quy trình 8 bước có kiểm tra phiên bản model theo tài liệu chính thức khi yêu cầu phụ thuộc bản mới nhất; thư mục references có templates.md (483 dòng) và patterns.md (82 dòng); cài được bằng cách tải ZIP lên Skills của claude.ai hoặc clone vào ~/.claude/skills. | `git clone https://github.com/nidhinjs/prompt-master.git ~/.claude/skills/prompt-master` |  |
| [`yusufkaraaslan/Skill_Seekers`](https://github.com/yusufkaraaslan/Skill_Seekers) | 15.333 | MIT (Copyright (c) 2025 Yusuf Karaaslan) | Công cụ CLI Python (kèm máy chủ MCP) biến trang tài liệu, repo GitHub, PDF, video, notebook, wiki… (18 loại nguồn) thành tài sản tri thức có cấu trúc để đóng gói thành AI Skill, dữ liệu RAG hoặc ngữ cảnh cho trợ lý lập trình (22 đích xuất). | Phát hành trên PyPI (skill-seekers), yêu cầu Python 3.10+, có các gói tuỳ chọn [mcp], [all-llms], [all]; lệnh scan dùng agent AI dò framework của dự án và sinh cấu hình; chế độ LOCAL dùng Claude Code, Codex, Kimi Code… không tốn phí API, thư mục tests có 191 mục. | `pip install skill-seekers` | Chế độ API cần khoá nhà cung cấp (ví dụ ANTHROPIC_API_KEY để tải skill lên Claude); cào trang tài liệu/GitHub cần tuân thủ điều khoản của nguồn (chưa xác minh README có nêu). |
| [`Orchestra-Research/AI-Research-SKILLs`](https://github.com/Orchestra-Research/AI-Research-SKILLs) | 14.630 | MIT (Copyright (c) 2025 Claude AI Research Skills Contributors) | Thư viện 98 Agent Skill giúp agent AI tự làm nghiên cứu AI trọn vòng đời: từ ý tưởng, khảo sát tài liệu, huấn luyện/tinh chỉnh/đánh giá/triển khai mô hình đến viết bài báo, có skill autoresearch điều phối. | 98 tệp SKILL.md chia 23 nhóm (kiến trúc mô hình, fine-tuning, huấn luyện phân tán, suy luận, RAG, an toàn, viết bài ML…); có trình cài tương tác qua npm (@orchestra-research/ai-research-skills); có CITATION.cff và CONTRIBUTING.md. | `npx @orchestra-research/ai-research-skills` |  |

**Chưa thêm (2 repo, giữ trong file dữ liệu):** `op7418/Humanizer-zh` (bản sao/bản dịch: Bản tiếng Trung chuyển thể từ blader/humanizer v3.0.0 (README ghi nguồn), có viết lại và thêm nhóm kiểm F cho tiếng Trung); `jnMetaCode/agency-agents-zh` (bản sao/bản dịch: Bản tiếng Trung cộng đồng của msitarzewski/agency-agents (261 agent dịch từ bản gốc, thêm 67 agent riêng cho thị trường Trung Quốc)).

#### 6c.5.19 Sách, Khóa học & Lộ trình

Đọc mã 12 repo, giữ 11.

| Repo | ★ (18/11/2026) | Giấy phép | Làm gì | Điểm mạnh (đọc mã) | Cài | Điều kiện dùng |
|---|---|---|---|---|---|---|
| [`EbookFoundation/free-programming-books`](https://github.com/EbookFoundation/free-programming-books) | 401.778 | Creative Commons Attribution 4.0 International (CC BY 4.0) | Danh sách cộng đồng các sách, khoá học, podcast/screencast lập trình miễn phí bằng nhiều ngôn ngữ, có trang web tĩnh và trang tìm kiếm. | Thư mục books có 49 tệp danh sách theo ngôn ngữ, cùng casts, courses, more; có trang tìm kiếm ebookfoundation.github.io/free-programming-books-search; do Free Ebook Foundation duy trì, nguồn gốc từ danh sách trên StackOverflow. |  | Nội dung theo CC BY 4.0 — dùng lại phải ghi công. |
| [`practical-tutorials/project-based-learning`](https://github.com/practical-tutorials/project-based-learning) | 289.941 | MIT License | Danh sách các hướng dẫn lập trình theo dự án, giúp người học tự xây ứng dụng từ đầu, chia theo ngôn ngữ chính. | Chia theo khoảng 22 ngôn ngữ từ C/C++ tới Swift; có workflow GitHub Actions quét liên kết hỏng (link-rot); khoảng 287 mục liên kết trong README |  |  |
| [`ossu/computer-science`](https://github.com/ossu/computer-science) | 211.241 | MIT License | Lộ trình tự học khoa học máy tính trọn vẹn bằng khoá học trực tuyến miễn phí, thiết kế theo yêu cầu cử nhân CS. | Bám chuẩn CS 2013 (Curriculum Guidelines for Undergraduate Degree Programs in Computer Science); chia Intro CS, Core CS, Advanced CS và Final Project; có CHANGELOG, FAQ và mục extras cho khoá học, sách bổ sung |  | Một số khoá học liên kết là của nền tảng bên ngoài, có thể cần tài khoản (chưa xác minh từng khoá) |
| [`getify/You-Dont-Know-JS`](https://github.com/getify/You-Dont-Know-JS) | 184.857 | Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International (CC BY-NC-ND 4.0) | Bộ sách (ấn bản 2) đi sâu vào cơ chế cốt lõi của ngôn ngữ JavaScript, đọc miễn phí trên GitHub. | Ấn bản 2 gồm Get Started, Scope & Closures và "The Unbooks" (Objects & Classes, Types & Grammar); đọc trực tuyến miễn phí trong repo; ấn bản 1 vẫn giữ ở nhánh 1st-ed |  | Giấy phép CC BY-NC-ND 4.0: không dùng thương mại, không được tạo tác phẩm phái sinh; Types & Grammar còn là bản nháp thô |
| [`Chalarangelo/30-seconds-of-code`](https://github.com/Chalarangelo/30-seconds-of-code) | 129.545 | Creative Commons Attribution 4.0 International (CC BY 4.0) cho đoạn mã; README nói các nội dung khác (văn bản, ảnh, mã nguồn website, logo, tên, thương hiệu) không được dùng khi chưa có đồng ý của chủ sở hữu | Kho bài viết lập trình ngắn kèm đoạn mã, giải thích và ví dụ, xuất bản thành website 30secondsofcode.org. | Khoảng 768 file Markdown trong content; website dựng bằng Astro (astro ^6.4.6 trong package.json); có tìm kiếm theo tên, thẻ, ngôn ngữ và nhóm theo collection |  | Chỉ đoạn mã theo CC BY 4.0; văn bản, ảnh, mã website, logo, thương hiệu cần xin phép chủ sở hữu |
| [`justjavac/free-programming-books-zh_CN`](https://github.com/justjavac/free-programming-books-zh_CN) | 119.647 | GNU General Public License v3.0 | Danh mục sách lập trình miễn phí bằng tiếng Trung, chia theo chủ đề chung và theo ngôn ngữ lập trình. | Chia hai nhóm lớn: chủ đề không phụ thuộc ngôn ngữ (hệ điều hành, AI, phân tán, biên dịch...) và theo ngôn ngữ (Android, C/C++, Go, Java...); nhận đóng góp qua Pull Request, có quy ước đánh dấu liên kết hỏng |  | Nội dung chủ yếu tiếng Trung; bản quyền từng cuốn sách thuộc tác giả gốc (chưa xác minh từng liên kết) |
| [`microsoft/Web-Dev-For-Beginners`](https://github.com/microsoft/Web-Dev-For-Beginners) | 97.125 | MIT License | Giáo trình 12 tuần, 24 bài học nhập môn phát triển web (JavaScript, CSS, HTML) theo dự án thực hành của Microsoft Cloud Advocates. | 24 bài học có quiz trước và sau bài, bài tập và thử thách; dự án thực hành như terrarium, typing game, browser extension, space game, bank app, AI chat; bản dịch tự động sang hơn 50 ngôn ngữ trong thư mục translations, có tiếng Việt | `git clone https://github.com/microsoft/Web-Dev-For-Beginners.git` |  |
| [`PKUFlyingPig/cs-self-learning`](https://github.com/PKUFlyingPig/cs-self-learning) | 76.777 | MIT License | Sách "CS 自学指南" tổng hợp kinh nghiệm và các khoá học mở chất lượng để tự học khoa học máy tính, đọc trực tuyến tại csdiy.wiki. | Khoảng 270 file Markdown trong docs, chia theo mảng như hệ điều hành, cơ sở dữ liệu, học máy, an ninh hệ thống; dựng web bằng MkDocs (mkdocs.yml); có bản tiếng Anh tại csdiy.wiki/en |  | Nội dung chính tiếng Trung, bản tiếng Anh song song |
| [`jaywcjlove/linux-command`](https://github.com/jaywcjlove/linux-command) | 37.238 | MIT License | Sổ tay tra cứu hơn 600 lệnh Linux bằng tiếng Trung, kèm website, gói npm và ảnh Docker để xem cục bộ. | 621 file trong thư mục command; phát hành gói npm linux-command (phiên bản 1.22.0 trong package.json); có ảnh Docker wcjiang/linux-command chạy web ở cổng 3000 | `docker run --name linux-command --rm -d -p 9665:3000 wcjiang/linux-command:latest` | README nói nội dung lấy từ mạng và cộng đồng, bản quyền thuộc tác giả gốc, không bảo đảm tính chính xác; dùng website là chấp nhận điều khoản sử dụng và quyền riêng tư của trang |
| [`fastai/fastbook`](https://github.com/fastai/fastbook) | 25.495 | GPL v3 cho mã (code trong notebook và file .py); phần văn xuôi (gồm ô markdown) không được phép phân phối lại hay đổi định dạng, chỉ được sao chép/fork cho mục đích cá nhân, cấm dùng thương mại và phát sóng | Bộ notebook Jupyter nhập môn học sâu với fastai và PyTorch, là nền của khoá học course.fast.ai và sách Deep Learning for Coders. | 20 chương notebook từ intro tới conclusion cùng phụ lục blog, Jupyter; mở từng chương trực tiếp trên Google Colab; README dịch sang nhiều ngôn ngữ, có README_vn.md |  | Văn xuôi không được phân phối lại, cấm dùng thương mại hoặc phát sóng; bản quyền thuộc Jeremy Howard và Sylvain Gugger; nên dùng Colab hoặc máy có GPU (chưa xác minh yêu cầu cụ thể) |
| [`KAYOKG/BibliotecaDev`](https://github.com/KAYOKG/BibliotecaDev) | 15.364 | MIT (LICENSE.md, Copyright (c) 2023 KAYOKG) | Danh mục sách cho lập trình viên bằng tiếng Bồ Đào Nha, chia theo chủ đề (thuật toán, kiến trúc, DevOps, Agile, sự nghiệp…), kèm thư mục LivrosDev chứa file PDF. | README chia 11 nhóm chủ đề có mô tả, bảng sách ghi tên, tác giả, trạng thái và ngôn ngữ; thư mục LivrosDev có 110 file PDF; có index.html để duyệt dạng trang web |  | Thư mục LivrosDev chứa PDF sách thương mại của nhiều nhà xuất bản (ví dụ Harvard Business Review, Casa do Código); giấy phép MIT của repo không cấp quyền với nội dung sách, cần lưu ý bản quyền |

**Chưa thêm (1 repo, giữ trong file dữ liệu):** `ageron/handson-ml` (dự án tự nêu ngừng/thay thế: README nói repo dành cho ấn bản 1 (2017) đã lỗi thời, thay bằng ấn bản 3 (ageron/handson-ml3) và bản PyTorch (ageron/handson-mlp)).

#### 6c.5.20 Thu thập dữ liệu & Trình duyệt tự động

Đọc mã 10 repo, giữ 9.

| Repo | ★ (18/11/2026) | Giấy phép | Làm gì | Điểm mạnh (đọc mã) | Cài | Điều kiện dùng |
|---|---|---|---|---|---|---|
| [`puppeteer/puppeteer`](https://github.com/puppeteer/puppeteer) | 95.855 | Apache License 2.0 | Thư viện JavaScript cung cấp API cấp cao để điều khiển Chrome hoặc Firefox qua DevTools Protocol hoặc WebDriver BiDi, mặc định chạy headless. | Gói puppeteer phiên bản 25.18.1, tự tải Chrome tương thích khi cài, có gói puppeteer-core không kèm trình duyệt; hỗ trợ cả CDP và WebDriver BiDi; README giới thiệu chrome-devtools-mcp dựa trên Puppeteer và API WebMCP thử nghiệm | `npm i puppeteer` | Trình quản lý gói chặn install script thì cần chạy npx puppeteer browsers install để tải trình duyệt |
| [`NaiboWang/EasySpider`](https://github.com/NaiboWang/EasySpider) | 44.797 | GNU AGPL-3.0; README nói cá nhân và doanh nghiệp dùng miễn phí kể cả thương mại, nhưng sản phẩm phái sinh phải theo AGPL-3.0 | Phần mềm cào dữ liệu và tự động hoá trình duyệt trực quan không cần viết code: chọn phần tử trên trang để thiết kế rồi chạy tác vụ thu thập. | Tự nhận diện khối cùng loại để chọn tất cả và trích từng trường; có giao diện Electron kèm extension Chrome và tầng thực thi Python dùng Selenium; có bản cho Windows, macOS và Linux qua trang Releases | `Tải bản mới nhất từ trang Releases của repo` | README cấm dùng cho mục đích trái pháp luật như cào website chính phủ/quân sự, người dùng tự chịu hậu quả; AGPL-3.0 buộc mở mã sản phẩm phái sinh; README quảng cáo dịch vụ proxy và giải CAPTCHA trả phí |
| [`ScrapeGraphAI/Scrapegraph-ai`](https://github.com/ScrapeGraphAI/Scrapegraph-ai) | 32.840 | MIT (Copyright 2024 Scrapgraph-ai team) | Thư viện Python dùng LLM và logic đồ thị để dựng pipeline cào dữ liệu từ website và tài liệu cục bộ (XML, HTML, JSON, Markdown); chỉ cần mô tả thông tin muốn lấy. | Pipeline SmartScraperGraph trích dữ liệu từ một trang theo prompt; chạy được với mô hình cục bộ qua Ollama hoặc API như OpenAI; tích hợp LangChain, LlamaIndex, CrewAI và có MCP server | `pip install scrapegraphai && playwright install` | Cần LLM (khoá API nhà cung cấp hoặc mô hình cục bộ như Ollama); README quảng bá thêm bản dịch vụ trả phí scrapegraphai.com |
| [`jackwener/OpenCLI`](https://github.com/jackwener/OpenCLI) | 31.148 | Apache License 2.0 | CLI tự động hoá trình duyệt cho AI agent: biến website thành lệnh CLI có đầu ra JSON xác định và điều khiển Chrome đang đăng nhập qua extension Browser Bridge. | Phiên bản 2.0.3, thư mục clis có 174 adapter dựng sẵn (Bilibili, Zhihu, Reddit, HackerNews, Twitter/X…); lệnh trả JSON thống nhất dạng ok/data/error với exit code khác 0 khi lỗi; có skill cho agent viết adapter mới và lệnh opencli doctor kiểm tra cài đặt | `npm install -g @jackwener/opencli` | Cần Node.js >= 20.18.1 và extension Chrome Browser Bridge; dùng phiên đăng nhập thật của người dùng; một số adapter (xiaoyuzhou) cần credential cục bộ |
| [`alibaba/page-agent`](https://github.com/alibaba/page-agent) | 29.706 | MIT (Copyright (c) 2026 SimonLuvRamen và Alibaba Group Holding Limited); phần xử lý DOM và prompt dẫn xuất từ browser-use (MIT) | Thư viện JavaScript nhúng vào trang web để tạo AI agent trong trang, điều khiển giao diện bằng ngôn ngữ tự nhiên dựa trên DOM dạng văn bản. | Chạy hoàn toàn trong trang, không cần extension, Python hay trình duyệt headless; thao tác DOM dạng văn bản, không cần ảnh chụp hay LLM đa phương thức; có extension Chrome cho tác vụ nhiều trang và MCP server (Beta) | `npm install page-agent` | Cần LLM tự cấp (baseURL và apiKey); CDN demo dùng API LLM thử nghiệm miễn phí chỉ để đánh giá kỹ thuật và phải đồng ý điều khoản của nó; thiết kế cho phía client, không cho tự động hoá phía server |
| [`lexmount/moli`](https://github.com/lexmount/moli) | 23.946 | MIT OR Apache-2.0 (LICENSE-MIT và LICENSE-APACHE); kèm thông báo bên thứ ba Chromium BSD-3-Clause và Selenium NOTICE | Trình duyệt headless viết bằng Rust cho AI agent, ưu tiên cấu trúc DOM và chỉ tính layout/vẽ khi cần; dùng qua CLI, CDP, WebDriver Classic hoặc WebDriver BiDi. | Runtime web đầy đủ với V8, DOM, CSS, Fetch/XHR/WebSocket, IndexedDB và OPFS; CDP, WebDriver Classic và BiDi dùng chung một binary, không cần ChromeDriver hay cài trình duyệt; CLI xuất trực tiếp HTML, Markdown, JSON và cây ngữ nghĩa, hỗ trợ Linux, macOS, Windows | `Tải rồi chạy bằng sh: https://github.com/lexmount/moli/releases/latest/download/moli-installer.sh (Linux/macOS)` | Dùng độc lập được, không cần Lexmount Browser (dịch vụ cloud trả phí của Lexmount) |
| [`citrolabs/ego-lite`](https://github.com/citrolabs/ego-lite) | 23.415 | MIT (Copyright (c) 2026 CitroLabs); chỉ áp cho nội dung repo, bản thân trình duyệt ego lite là bản tải riêng | Repo chứa skill ego-browser và plugin để AI agent (Claude Code, Codex, Cursor…) điều khiển trình duyệt ego lite, mỗi agent chạy trong một Space cô lập song song với người dùng. | Skill ego-browser cung cấp công cụ JavaScript trong trang (snapshot, fill…) cho agent gọi trực tiếp; mỗi agent có Space riêng nên không chiếm trình duyệt của người dùng; kèm thư mục learnings có công cụ dựng sẵn cho x.com, Google, GitHub | `npx skills add citrolabs/ego-lite` | Cần cài ứng dụng ego lite (tải riêng, mã nguồn không nằm trong repo); chỉ macOS và Windows, Linux còn trong lộ trình; có thể di chuyển dữ liệu đăng nhập Chrome; ứng dụng thu tín hiệu sản phẩm đơn giản |
| [`getmaxun/maxun`](https://github.com/getmaxun/maxun) | 18.503 | GNU AGPL-3.0 | Nền tảng dữ liệu web mã nguồn mở biến website thành API có cấu trúc: trích xuất, cào, crawl, tìm kiếm, giám sát thay đổi và trích dữ liệu bằng AI. | Có Recorder Mode ghi thao tác trình duyệt thành robot và AI Mode trích dữ liệu bằng ngôn ngữ tự nhiên; dùng qua dashboard, API, SDK, CLI và MCP; tự host được bằng Docker Compose (repo có docker-compose.yml) |  | AGPL-3.0; bản hosted tại app.maxun.dev cần tài khoản; AI Mode cần LLM |
| [`apify/apify-mcp-server`](https://github.com/apify/apify-mcp-server) | 16.749 | MIT (Copyright (c) 2025 Apify) | MCP server chính thức của Apify cho phép AI agent tìm, xem giá, chạy hàng nghìn Actor trong Apify Store để cào dữ liệu và tự động hoá trình duyệt, dùng bản hosted hoặc chạy cục bộ qua stdio. | Endpoint hosted https://mcp.apify.com xác thực OAuth hoặc Bearer token; có hướng dẫn cấu hình cho Claude Code, ChatGPT, Cursor, VS Code và các client khác; cho giới hạn chi phí lần chạy qua maxTotalChargeUsd hoặc maxItems | `claude mcp add apify "https://mcp.apify.com" -t http` | Cần tài khoản/API token Apify, lần chạy Actor tính phí theo giá từng Actor (gói free có 5 USD mỗi tháng); bản cục bộ cần Node.js 22+; telemetry bật mặc định (tắt bằng TELEMETRY_ENABLED=false); giới hạn 20 request/giây mỗi tài khoản |

**Chưa thêm (1 repo, giữ trong file dữ liệu):** `browser-use/web-ui` (commit cuối 15/5/2026).

#### 6c.5.21 Thuật toán & Phỏng vấn

Đọc mã 8 repo, giữ 8.

| Repo | ★ (18/11/2026) | Giấy phép | Làm gì | Điểm mạnh (đọc mã) | Cài | Điều kiện dùng |
|---|---|---|---|---|---|---|
| [`jwasham/coding-interview-university`](https://github.com/jwasham/coding-interview-university) | 364.487 | Creative Commons Attribution-ShareAlike 4.0 International (CC BY-SA 4.0) | Kế hoạch tự học nhiều tháng gồm danh sách chủ đề và liên kết tài liệu để chuẩn bị phỏng vấn kỹ sư phần mềm ở các công ty lớn. | Có bản dịch sang nhiều ngôn ngữ trong thư mục translations; dạng checklist theo chủ đề (Big O, mảng, danh sách liên kết, sắp xếp…) kèm video bài giảng; còn được cập nhật (commit 2026-11-07) |  | Nội dung CC BY-SA 4.0: phải ghi công và chia sẻ cùng giấy phép khi phái sinh |
| [`TheAlgorithms/Python`](https://github.com/TheAlgorithms/Python) | 226.210 | MIT License (Copyright 2016-2022 TheAlgorithms and contributors) | Kho cài đặt rất nhiều thuật toán và cấu trúc dữ liệu bằng Python nhằm mục đích giáo dục. | DIRECTORY.md liệt kê khoảng 1372 mục; chia theo nhiều thư mục chủ đề (ciphers, dynamic_programming, graphs, machine_learning…); có CONTRIBUTING.md và cộng đồng Discord |  | README nói cài đặt chỉ để học, có thể kém hiệu quả hơn thư viện chuẩn Python |
| [`trekhleb/javascript-algorithms`](https://github.com/trekhleb/javascript-algorithms) | 196.737 | MIT License (Copyright 2018 Oleksii Trekhleb) | Kho ví dụ thuật toán và cấu trúc dữ liệu phổ biến viết bằng JavaScript, mỗi mục có README giải thích riêng. | Mỗi thuật toán có README riêng kèm liên kết đọc thêm; có bộ test Jest và ESLint (npm test, npm run lint); README dịch ra nhiều ngôn ngữ, gồm tiếng Việt | `npm install && npm test` |  |
| [`Snailclimb/JavaGuide`](https://github.com/Snailclimb/JavaGuide) | 159.603 | Apache License 2.0 | Bộ tài liệu tiếng Trung về kiến thức Java backend và chuẩn bị phỏng vấn, đọc trực tuyến tại javaguide.cn. | Có lộ trình học Java và kế hoạch luyện phỏng vấn backend; có trang đọc trực tuyến và README tiếng Anh, tiếng Nhật; còn cập nhật (commit 2026-10-25) |  | Nội dung chủ yếu tiếng Trung; README yêu cầu ghi nguồn khi đăng lại và cảnh báo xử lý pháp lý nếu sao chép trái phép; có quảng bá tài liệu trả phí |
| [`yangshun/tech-interview-handbook`](https://github.com/yangshun/tech-interview-handbook) | 143.319 | MIT License (Copyright 2017-Present Yangshun Tay) | Tài liệu miễn phí, chọn lọc để chuẩn bị phỏng vấn kỹ thuật (thuật toán, hồ sơ, câu hỏi hành vi), đọc trên techinterviewhandbook.org. | Của tác giả Blind 75, có Grind 75; gồm cheatsheet thuật toán theo chủ đề, hướng dẫn viết CV và câu hỏi hành vi; mã nguồn website nằm trong apps/website (monorepo pnpm) |  | Tác giả nói giấy phép mã là của cá nhân, không phải của chủ lao động (Meta) |
| [`krahets/hello-algo`](https://github.com/krahets/hello-algo) | 132.403 | Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0) | Sách mã nguồn mở, miễn phí, minh hoạ bằng hoạt hình về cấu trúc dữ liệu và thuật toán cho người mới, mã chạy được. | Mã ví dụ bằng nhiều ngôn ngữ (Python, Java, C++, C, C#, Go, Rust, Swift, TypeScript, Zig…); có bản tiếng Trung giản thể, phồn thể, Anh, Nhật, Nga, Hàn; còn cập nhật (commit 2026-11-18) |  | CC BY-NC-SA 4.0: cấm dùng thương mại, phải ghi công và chia sẻ cùng giấy phép |
| [`iluwatar/java-design-patterns`](https://github.com/iluwatar/java-design-patterns) | 94.884 | MIT License (Copyright 2014-2024 Ilkka Seppälä) | Kho cài đặt minh hoạ các mẫu thiết kế (design pattern) bằng Java, có chú thích như bài hướng dẫn. | Khoảng 190 thư mục mẫu (adapter, builder, circuit-breaker, CQRS…); có trang java-design-patterns.com duyệt theo tag/danh mục; README dịch sang nhiều ngôn ngữ |  | Bản e-book của dự án là sản phẩm trả phí (payhip) |
| [`doocs/advanced-java`](https://github.com/doocs/advanced-java) | 79.182 | Creative Commons Attribution-ShareAlike 4.0 International (CC BY-SA 4.0) | Tài liệu tiếng Trung tổng hợp kiến thức Java nâng cao: tải cao, phân tán, sẵn sàng cao, microservice, xử lý dữ liệu lớn, dạng câu hỏi phỏng vấn. | Chia chuyên đề rõ (hàng đợi tin nhắn, Elasticsearch, cache Redis…); nhiều bài trả lời câu hỏi phỏng vấn cụ thể; còn cập nhật (commit 2026-11-14) |  | README ghi phần lớn nội dung từ 中华石杉 và bản quyền thuộc tác giả đó, có thể mâu thuẫn với giấy phép CC BY-SA 4.0; nội dung tiếng Trung |

#### 6c.5.22 Thư viện giao diện & CSS

Đọc mã 3 repo, giữ 3.

| Repo | ★ (18/11/2026) | Giấy phép | Làm gì | Điểm mạnh (đọc mã) | Cài | Điều kiện dùng |
|---|---|---|---|---|---|---|
| [`twbs/bootstrap`](https://github.com/twbs/bootstrap) | 175.080 | MIT License (Copyright 2011-2026 The Bootstrap Authors); tài liệu theo Creative Commons BY 3.0 | Framework front-end CSS/JS để dựng giao diện web responsive nhanh. | Phát hành qua npm, yarn, Bun, Composer, NuGet; có test JS, coverage và OpenSSF Scorecard trong README; nhánh v5-dev duy trì Bootstrap 5 | `npm install bootstrap@6.0.0-alpha.1` | Nhánh mặc định đang phát triển Bootstrap 6 (bản 6.0.0-alpha.1); bản ổn định Bootstrap 5 ở nhánh v5-dev |
| [`FortAwesome/Font-Awesome`](https://github.com/FortAwesome/Font-Awesome) | 77.044 | Font Awesome Free License: icon CC BY 4.0, font SIL OFL 1.1, mã MIT; yêu cầu giữ chú thích ghi công | Bộ icon và toolkit Font Awesome bản Free (phiên bản 7), cung cấp SVG, webfont, CSS/SCSS và gói JS. | Bản 7 hiện hành, bản 6 là LTS chỉ vá lỗi nghiêm trọng; có khoảng 2000 icon SVG nhóm solid cùng nhóm regular và brands; phát hành theo SemVer có ghi chú nâng cấp UPGRADING.md | `npm install @fortawesome/fontawesome-free` | Bắt buộc ghi công theo CC BY/OFL/MIT (chú thích có sẵn trong file, không được gỡ); chỉ phần Free, bản Pro cần giấy phép trả phí |
| [`carbon-app/carbon`](https://github.com/carbon-app/carbon) | 36.148 | MIT | Ứng dụng web (carbon.now.sh) tạo ảnh đẹp từ mã nguồn để chia sẻ, tuỳ chỉnh theme, font, nền. | Xuất ảnh PNG và SVG, nhúng snippet qua carbon.now.sh/embed; nhập mã bằng kéo thả file hoặc ID GitHub gist; README có hơn 20 bản dịch | `Dùng trực tiếp tại https://carbon.now.sh (có thể cài dạng PWA)` | Lưu snippet cần tạo tài khoản |

#### 6c.5.23 Trợ lý lập trình AI

Đọc mã 21 repo, giữ 19.

| Repo | ★ (18/11/2026) | Giấy phép | Làm gì | Điểm mạnh (đọc mã) | Cài | Điều kiện dùng |
|---|---|---|---|---|---|---|
| [`abi/screenshot-to-code`](https://github.com/abi/screenshot-to-code) | 81.279 | MIT | Chuyển ảnh chụp màn hình, mockup, thiết kế Figma và video quay màn hình thành mã frontend bằng mô hình AI. | Hỗ trợ nhiều stack: HTML+Tailwind, React+Tailwind, Vue+Tailwind, Bootstrap, Ionic; backend FastAPI và frontend React/Vite, có docker-compose; có công cụ xem trước bằng Chromium headless để agent tự kiểm kết quả | `docker-compose up -d --build (sau khi đặt OPENAI_API_KEY vào .env)` | Cần ít nhất một khoá API OpenAI, Anthropic hoặc Gemini (trả phí); Replicate khuyến nghị cho xử lý ảnh |
| [`Alishahryar1/free-claude-code`](https://github.com/Alishahryar1/free-claude-code) | 71.094 | AGPL-3.0-only | Proxy cục bộ định tuyến các agent lập trình (Claude Code, Codex, OpenCode, Aider…) tới mô hình của nhiều nhà cung cấp, kể cả gói miễn phí và mô hình cục bộ. | Hỗ trợ 12 harness và 61 nhà cung cấp theo README; cung cấp bốn API: Anthropic Messages, OpenAI Chat Completions, OpenAI Responses, Gemini; có retry, giới hạn tốc độ và fallback model/nhà cung cấp/khoá | `Tải scripts/install.sh từ repo rồi chạy bằng sh; sau đó fcc-server và fcc-claude` | Cần khoá API của nhà cung cấp (vd. NVIDIA NIM); dự án độc lập, không liên kết Anthropic; hạn mức miễn phí do nhà cung cấp quyết định và phải tuân ToS từng nhà cung cấp; AGPL ràng buộc khi phân phối/dịch vụ mạng |
| [`herdrdev/herdr`](https://github.com/herdrdev/herdr) | 51.611 | Apache-2.0 | Trình quản lý terminal kiểu tmux cho các agent lập trình: giữ phiên chạy nền, theo dõi trạng thái từng pane, gom nhiều máy SSH vào một cửa sổ. | Một binary Rust, không dùng Electron; đánh dấu pane đang làm, bị chặn hay rảnh và có CLI/socket API để agent điều khiển; khôi phục bố cục sau khi khởi động lại, có Homebrew và mise | `brew install herdr (hoặc tải https://herdr.dev/install.sh rồi chạy bằng sh)` |  |
| [`anywhere-labs/dsh-desktop`](https://github.com/anywhere-labs/dsh-desktop) | 36.277 | MIT | Ứng dụng desktop Windows/macOS/Linux đóng gói Web UI, Host và hệ plugin của DeepSeek Harness thành ứng dụng gốc với cửa sổ, tray, terminal, cập nhật. | Chạy bản DeepSeek Harness được ghim cố định không sửa (upstream.json ghi commit theo kênh stable/beta/next); có bộ cài Windows x64, macOS Universal, Linux deb/AppImage/tar.gz cho x64 và arm64; kèm SHA256SUMS để kiểm tra bản tải | `Tải bộ cài từ GitHub Releases hoặc dshdesktop.cn; Linux: sudo apt install ./DSH-NEXT-<version>-amd64.deb` | Dự án cộng đồng độc lập, không liên kết DeepSeek; upstream ghim là bản rc (0.2.1-rc.3 stable); bản Linux không tự cập nhật; có chính sách quyền riêng tư PRIVACY.md cần đọc |
| [`iOfficeAI/AionUi`](https://github.com/iOfficeAI/AionUi) | 34.354 | Apache-2.0 | Ứng dụng desktop "Cowork" cho phép agent AI đọc file, viết mã, duyệt web và tự động hoá tác vụ, tích hợp nhiều CLI agent sẵn có. | Có agent dựng sẵn (engine aionrs) dùng với khoá API bất kỳ; tự phát hiện và điều phối nhiều CLI agent như Claude Code, Codex, Gemini CLI, kèm chế độ Team leader/teammate; truy cập từ xa qua WebUI, Telegram, Lark, DingTalk, WeChat và lập lịch cron | `brew install aionui (hoặc tải bộ cài từ GitHub Releases)` | Cần khoá API của nhà cung cấp mô hình; agent có quyền truy cập file đầy đủ trên máy |
| [`TabbyML/tabby`](https://github.com/TabbyML/tabby) | 33.933 | Apache-2.0 cho phần ngoài ee/; thư mục ee/ theo Tabby Enterprise License riêng | Trợ lý lập trình AI tự host, thay thế GitHub Copilot tại chỗ, có gợi ý mã và Answer Engine. | Tự chứa, không cần DBMS hay dịch vụ đám mây; có giao diện OpenAPI và chạy trên GPU phổ thông (CUDA, Metal); có xác thực LDAP và đánh chỉ mục Merge Request GitLab làm ngữ cảnh | `docker run -it --gpus all -p 8080:8080 -v $HOME/.tabby:/data tabbyml/tabby serve --model StarCoder-1B --device cuda --chat-model Qwen2-1.5B-Instruct` | Tính năng thư mục ee/ chịu giấy phép Enterprise; nên có GPU để chạy mô hình |
| [`charmbracelet/crush`](https://github.com/charmbracelet/crush) | 29.112 | FSL-1.1-MIT (Functional Source License, cấm dùng cạnh tranh, chuyển sang MIT sau 2 năm) | Agent lập trình chạy trong terminal của Charm, nối công cụ, mã và quy trình với LLM tuỳ chọn. | Đổi mô hình giữa phiên mà giữ ngữ cảnh, hỗ trợ API tương thích OpenAI/Anthropic; dùng LSP lấy thêm ngữ cảnh và mở rộng bằng MCP (http, stdio, sse); chạy trên macOS, Linux, Windows, Android, FreeBSD, OpenBSD, NetBSD | `brew install charmbracelet/tap/crush (hoặc npm install -g @charmland/crush)` | Giấy phép FSL không cho phép sử dụng cạnh tranh trước khi chuyển MIT; cần khoá API nhà cung cấp (vd. ANTHROPIC_API_KEY, OPENAI_API_KEY); đóng góp cần ký CLA |
| [`ccch1mneyyy/dsh-Go`](https://github.com/ccch1mneyyy/dsh-Go) | 26.168 | AGPL-3.0 (sdk/ và examples/ theo MIT; tên, logo DSH Go và linh vật Deepy, Whale girl không thuộc giấy phép, xem ASSETS.md) | Ứng dụng di động (Flutter) cho DeepSeek Harness: chạy engine DSH ngay trên điện thoại với môi trường Linux tích hợp, hoặc điều khiển DSH trên máy tính qua SSH/DSHarness Remote. | Bản Android đã phát hành (Android 8+), cài Ubuntu, Node.js và DSH trong app không cần root hay Termux; giao diện song ngữ Anh và Trung, chia sẻ cuộc trò chuyện dạng liên kết mã hoá đầu cuối; có chế độ điều khiển điện thoại với hành động nhạy cảm mặc định do người dùng duyệt | `Tải APK arm64 từ GitHub Releases hoặc go.dshtui.com/download` | Cần nhà cung cấp mô hình tự cấu hình (dịch vụ bên thứ ba theo điều khoản và chi phí riêng); iOS chưa có bản cài công khai, phải tự ký trên Mac; tác giả yêu cầu không dùng thương hiệu, linh vật cho sản phẩm thương mại khi chưa xin phép |
| [`slopus/happy`](https://github.com/slopus/happy) | 24.687 | MIT | Monorepo của Happy: app di động (iOS, Android, web), CLI gốc bọc Claude Code và Codex để tiếp tục phiên từ điện thoại, và relay server đồng bộ mã hoá. | Đồng bộ phiên giữa máy tính và điện thoại mã hoá đầu cuối; CLI `happy claude` và `happy codex` cài qua npm; có app iOS native (Swift/UIKit), Android native (Kotlin/Compose) và push server trên Cloudflare Worker | `npm install -g happy && happy claude` | Dùng gói thuê bao hoặc đăng nhập sẵn có của Claude, Codex, Grok…; README khuyên chuyển sang app desktop (repo riêng happy-desktop) cho phiên đa mô hình và nhóm |
| [`getpaseo/paseo`](https://github.com/getpaseo/paseo) | 24.279 | Apache-2.0 (thành phần bên thứ ba giữ giấy phép riêng) | Môi trường phát triển agentic mã nguồn mở (desktop, mobile, web, CLI) điều phối nhiều agent CLI như Claude Code, Codex, Copilot, OpenCode song song qua một daemon cục bộ. | Mỗi agent chạy trong worktree riêng, agent có thể tạo worktree và gọi agent khác; tự host, README nêu không telemetry hay bắt đăng nhập; hệ plugin chạy trên daemon hiển thị đồng nhất trên mọi client | `npm install -g @getpaseo/cli (hoặc tải app ở paseo.sh/download)` | Cần ít nhất một agent CLI đã cài và cấu hình thông tin đăng nhập; plugin chạy với quyền truy cập máy daemon, chỉ cài mã tin cậy |
| [`winfunc/opcode`](https://github.com/winfunc/opcode) | 22.452 | AGPL-3.0 | Ứng dụng desktop Tauri 2 làm GUI cho Claude Code: quản lý dự án và phiên, tạo agent tuỳ biến, theo dõi chi phí token, quản lý MCP server và checkpoint phiên. | Duyệt dự án và phiên trong ~/.claude/projects kèm tìm kiếm; timeline checkpoint có rẽ nhánh, khôi phục và xem diff; dashboard chi phí và token theo mô hình, dự án, thời gian | `bun install && bun run tauri build (build từ mã nguồn)` | Cần Claude Code CLI; README ghi bản thực thi phát hành sẽ có sau, hiện phải build từ nguồn (Rust, Bun); dự án độc lập, không liên kết với Anthropic |
| [`1jehuang/jcode`](https://github.com/1jehuang/jcode) | 21.866 | MIT | Coding agent viết bằng Rust tối ưu hiệu năng, chạy hàng chục agent song song với ít RAM; có chế độ swarm để nhiều agent cùng phối hợp trong một repo. | README đo khoảng 3,3 MB RAM mỗi phiên thêm và 19,1 ms tới lúc nhập được, kèm script tái hiện benchmark; server thông báo cho agent khi tệp nó đã đọc bị agent khác sửa; hỗ trợ nhiều nhà cung cấp gồm Claude OAuth và OpenAI Codex OAuth | `curl -fsSL https://jcode.sh/install rồi chuyển cho bash (script cài macOS và Linux)` | Cần tài khoản hoặc khoá của nhà cung cấp mô hình; có thu thập thống kê sử dụng tối thiểu (TELEMETRY.md), chia sẻ transcript đầy đủ là tuỳ chọn, mặc định tắt; script cài cho macOS và Linux |
| [`google/artemis`](https://github.com/google/artemis) | 17.651 | Apache-2.0 (third_party/mobile_use theo Apache-2.0 của Minitap) | Agent đa phương thức điều khiển điện thoại Android thật bằng ngôn ngữ tự nhiên cho kiểm thử và tác vụ hằng ngày, kèm MCP server để IDE AI điều khiển thiết bị, lấy Logcat và ảnh chụp màn hình. | README báo hơn 99% hoàn thành tác vụ trên benchmark AndroidWorld; định vị phần tử bằng chỉ số với dự phòng toạ độ và thị giác; script start.sh tự cài ADB, scrcpy, FFmpeg và cấu hình MCP cho nhiều IDE | `git clone https://github.com/google/artemis.git && cd artemis && ./start.sh` | Cần thiết bị Android bật USB Debugging hoặc emulator; cần khoá API mô hình đa phương thức (chưa xác minh chi tiết); script khởi động tự cài công cụ hệ thống và cấu hình MCP toàn cục; chưa hỗ trợ iOS |
| [`HKUDS/DeepCode`](https://github.com/HKUDS/DeepCode) | 16.850 | MIT | Coding agent đa tác tử của HKU Data Intelligence Lab với TUI, Web, Desktop dùng chung một dịch vụ cục bộ; hỗ trợ Goal chạy dài, tự động hoá headless và Paper2Code. | Phát hành v2.4.0 ngày 2026-11-16; Goal có checklist lệnh xác minh do DeepCode tự chạy trước khi nhận hoàn thành, kèm reviewer độc lập tuỳ chọn; chế độ headless `deepcode exec` xuất sự kiện NDJSON cho CI | `uv tool install --python 3.12 deepcode-hku && deepcode init` | Cần khoá API nhà cung cấp mô hình (ví dụ OpenRouter); Desktop chưa có installer, phải chạy từ mã nguồn với Node.js 22+, Rust và Tauri 2 |
| [`ParadevAI/Paradev`](https://github.com/ParadevAI/Paradev) | 16.371 | MIT (Copyright Superset Inc.) | Ứng dụng desktop (trước đây là Superset) chạy song song nhiều agent CLI như Claude Code, Codex, OpenCode, mỗi tác vụ có worktree, nhánh và terminal riêng. | Mỗi tác vụ một Git worktree và nhánh riêng; khung Changes và Pull request để review, commit, push, merge ngay trong app; trình duyệt tích hợp xem trước dev server theo từng workspace | `Tải .dmg (macOS) hoặc AppImage (Linux, thử nghiệm) từ GitHub Releases` | Chủ yếu macOS, Linux thử nghiệm, chưa có Windows; tự mang thuê bao hoặc khoá API của agent; host từ xa, app iPhone/iPad và automation thuộc gói Pro |
| [`CoplayDev/unity-mcp`](https://github.com/CoplayDev/unity-mcp) | 16.042 | MIT | MCP server và gói Unity (MCP for Unity) cho phép trợ lý AI điều khiển Unity Editor bằng ngôn ngữ tự nhiên: tạo scene, GameObject, sửa script C#, quản lý asset, chạy test, build. | 50 điểm vào công cụ MCP, dùng được với mọi MCP client; hỗ trợ Unity 2021.3 LTS tới 6.x; phát hành đều, bản v10.3.0 ngày 2026-10-04 | `Unity Package Manager → Add from git URL: https://github.com/CoplayDev/unity-mcp.git?path=/MCPForUnity#main` | Cần Unity 2021.3 LTS trở lên và Python 3.10+ qua uv; cần một MCP client |
| [`NanmiCoder/cc-haha`](https://github.com/NanmiCoder/cc-haha) | 15.484 | cc-haha Community Source License 1.0 (giấy phép source-available tự soạn, không phải OSI); dùng cá nhân/phi thương mại và nội bộ doanh nghiệp được phép; nhận việc trả phí, bán lại, SaaS, tùy biến thu phí cần giấy phép thương mại bằng văn bản; phân phối lại phải ghi nguồn 'Based on cc-haha'; mã bên thứ ba (agent-desktop) giữ Apache-2.0 | Ứng dụng desktop (macOS, Windows, Linux) làm không gian làm việc kiểu Claude Code: nhiều phiên, worktree, review diff, duyệt quyền bằng GUI, dùng nhiều nhà cung cấp mô hình; kèm app di động ghép bằng mã QR. | Có Agent Teams, điều phối Workflow, trình quản lý MCP/SubAgent và Computer Use (macOS engine riêng, Windows/Linux tái dùng agent-desktop của Vercel Labs ghim bản 1.0.2); hỗ trợ Claude, ChatGPT, Grok và endpoint cục bộ; có app Android (APK) và iOS (TestFlight) điều khiển từ xa | `Tải bộ cài desktop từ GitHub Releases rồi cấu hình nhà cung cấp mô hình và API key trong Settings` | Cần API key/tài khoản nhà cung cấp mô hình; giấy phép cấm dùng thương mại (nhận việc, bán, SaaS, sửa thu phí) khi chưa có giấy phép bằng văn bản; bộ cài Windows chưa ký có thể bị SmartScreen cảnh báo; app di động chỉ giao diện tiếng Trung |
| [`OrchestratorInc/agent-orchestrator`](https://github.com/OrchestratorInc/agent-orchestrator) | 14.860 | Apache-2.0 | Ứng dụng desktop chạy cục bộ để điều phối một đội agent lập trình: mỗi việc có agent, nhánh và worktree riêng, theo dõi PR, CI và review trên bảng Kanban. | Hỗ trợ nhiều agent như Claude Code, Codex, Cursor, opencode, Aider, GitHub Copilot; lỗi CI, bình luận review và xung đột merge được chuyển lại cho agent sở hữu nhánh; có bộ cài macOS, Windows, Linux (AppImage, deb, rpm) và app di động ghép bằng QR | `Tải từ orchestrator.inc/download hoặc GitHub Releases, mở app và trỏ vào repo cần quản lý` | Cần cài sẵn CLI của agent lập trình và tài khoản tương ứng; thu telemetry sử dụng (gồm installation ID và tên người dùng GitHub, email nếu đăng nhập AO Cloud) qua PostHog, tắt được trong Settings |
| [`fathah/hermes-desktop`](https://github.com/fathah/hermes-desktop) | 14.591 | MIT | Hermes One: ứng dụng desktop do cộng đồng duy trì để cài đặt, cấu hình và trò chuyện với Hermes Agent của Nous Research qua giao diện đồ họa thay cho CLI. | Dùng script cài đặt chính thức của Hermes và lưu tại ~/.hermes; có GUI cho chat, phiên, profile, bộ nhớ, skill, công cụ, lịch chạy, gateway nhắn tin và Kanban; README có bản tiếng Anh, Trung, Nhật, Tây Ban Nha | `Tải bộ cài từ hermesone.org hoặc GitHub Releases (không cài qua npm)` | README ghi dự án đang phát triển tích cực, tính năng có thể đổi hoặc hỏng; bộ cài Windows không ký số, gói .rpm không ký GPG; cần cấu hình nhà cung cấp mô hình |

**Chưa thêm (2 repo, giữ trong file dữ liệu):** `Twigpine/openclaude` (LICENSE tự nêu mã dẫn xuất từ Claude Code độc quyền và không có quyền phân phối); `dataelement/dsh-desktop` (trùng loại với anywhere-labs/dsh-desktop (app desktop DeepSeek Harness, nhiều sao hơn)).

#### 6c.5.24 Tài chính & Crypto

Đọc mã 11 repo, giữ 11.

| Repo | ★ (18/11/2026) | Giấy phép | Làm gì | Điểm mạnh (đọc mã) | Cài | Điều kiện dùng |
|---|---|---|---|---|---|---|
| [`bitcoin/bitcoin`](https://github.com/bitcoin/bitcoin) | 90.693 | MIT (file COPYING) | Bitcoin Core: phần mềm nút kết nối mạng ngang hàng Bitcoin, tải và xác thực đầy đủ khối và giao dịch, kèm ví và giao diện đồ họa tùy chọn. | Build bằng CMake, có unit test chạy qua ctest và test chức năng/hồi quy viết bằng Python; tag phát hành ổn định được cắt từ nhánh release; có SECURITY.md và quy trình đóng góp trong CONTRIBUTING.md | `Bản nhị phân tại bitcoincore.org/en/download; build từ mã theo doc/build-*.md` | README nhấn mạnh nhánh master không đảm bảo ổn định và đây là dự án nhạy cảm bảo mật, lỗi có thể gây mất tiền |
| [`unionlabs/union`](https://github.com/unionlabs/union) | 73.711 | Hai file giấy phép ở gốc: LICENSE-APACHE (Apache-2.0) và LICENSE-MIT (Copyright 2024 Union.fi Labs, Inc.); README không nêu điều khoản riêng | Union: lớp hạ tầng zero-knowledge cho truyền thông điệp tổng quát, chuyển tài sản, NFT và DeFi giữa các chuỗi, dựa trên xác minh đồng thuận và triển khai IBC. | Gồm nút uniond (Go, CometBLS), prover galoisd (Go, Gnark), relayer voyager (Rust), hợp đồng CosmWasm và EVM, TypeScript SDK; build tái lập được bằng Nix (nix build .#uniond); kết nối chuỗi Cosmos và EVM như Ethereum, Arbitrum, Berachain | Cài Nix rồi `nix build .#uniond -L` (xem `nix flake show` để liệt kê gói) | Một số thành phần chỉ build được trên Linux (macOS cần VM NixOS); liên quan tài sản tiền mã hóa |
| [`ZhuLinsen/daily_stock_analysis`](https://github.com/ZhuLinsen/daily_stock_analysis) | 73.114 | MIT | Hệ thống phân tích cổ phiếu theo danh mục theo dõi bằng mô hình ngôn ngữ lớn cho thị trường A, Hồng Kông, Mỹ, Nhật, Hàn, Đài Loan; tự động phân tích hằng ngày và đẩy báo cáo dạng bảng quyết định. | Đẩy thông báo qua WeCom, Feishu, Telegram, Discord, Slack, email; chạy được qua GitHub Actions, Docker, dịch vụ FastAPI hoặc lịch cục bộ; có Web/desktop với backtest, danh mục và agent hỏi đáp với 15 chiến lược dựng sẵn | git clone rồi `pip install -r requirements.txt`, sao .env.example thành .env và `python main.py` | Cần API key của ít nhất một nhà cung cấp LLM và ít nhất một kênh thông báo; README tuyên bố chỉ dùng cho học tập/nghiên cứu, không phải lời khuyên đầu tư, tác giả không chịu trách nhiệm thua lỗ |
| [`microsoft/qlib`](https://github.com/microsoft/qlib) | 50.373 | MIT (Copyright Microsoft Corporation) | Qlib: nền tảng đầu tư định lượng hướng AI mã nguồn mở của Microsoft, bao trọn từ khám phá ý tưởng, xử lý dữ liệu, huấn luyện mô hình đến backtest. | Hỗ trợ học có giám sát, mô hình hóa động lực thị trường và học tăng cường; có bài báo arXiv 2009.11189 mô tả nền tảng; phát hành trên PyPI dạng gói pyqlib, chạy Linux, Windows, macOS | `pip install pyqlib` | Bộ dữ liệu chính thức tạm tắt do chính sách bảo mật dữ liệu, README trỏ tới nguồn cộng đồng; dữ liệu mẫu thu từ Yahoo Finance có thể không hoàn hảo; bản mã trên main có thay đổi phá tương thích chưa phát hành về nạp artefact (cần trusted=True) |
| [`HKUDS/Vibe-Trading`](https://github.com/HKUDS/Vibe-Trading) | 38.452 | MIT (Copyright 2026 Vibe-Trading Contributors); NOTICE ghi kèm định nghĩa đặc trưng Qlib theo Apache-2.0 và font theo SIL OFL 1.1 | Agent giao dịch cá nhân biến câu hỏi tài chính thành báo cáo nghiên cứu, backtest chạy được và danh mục giấy; có thể ủy quyền cho broker hỗ trợ đặt lệnh thật trong giới hạn người dùng đặt. | Phát hành trên PyPI (vibe-trading-ai, bản v0.1.19 ngày 2026-11-05); có Web, CLI, API và công cụ Agent/MCP dùng chung; README nêu 19 kết nối broker với quyền theo từng broker và công tắc dừng khẩn cấp cho giao dịch thật | `pip install -U vibe-trading-ai` | Cần API key nhà cung cấp LLM; README tuyên bố không phải lời khuyên đầu tư, tính năng giao dịch qua broker là thử nghiệm, chưa được kiểm chứng với tài khoản broker thật, tự chịu rủi ro; liên quan tiền thật khi bật giao dịch live |
| [`Fincept-Corporation/FinceptTerminal`](https://github.com/Fincept-Corporation/FinceptTerminal) | 33.938 | AGPL-3.0-or-later; nhãn hiệu Fincept cấm dùng trong bản fork/phái sinh/thương mại khi chưa có phép bằng văn bản; không còn bán giấy phép thương mại riêng (dùng bản Enterprise độc quyền) | Fincept Terminal: ứng dụng desktop phân tích tài chính (C++20, Qt6, Python) với nghiên cứu cổ phiếu, danh mục, tin tức, trình soạn node và tự động hóa AI. | Có bộ cài Windows, Linux (AppImage, deb, rpm) ở bản v4.5.2; giá lấy trực tiếp trên máy người dùng từ nguồn họ chọn (broker, sàn, Yahoo Finance); toolchain build được ghim phiên bản (CMake 3.27.7, Qt 6.8.3, Python 3.11.9) | Tải bộ cài từ GitHub Releases; build từ mã: `./setup.sh` trên Linux/macOS | AGPL-3.0: phân phối bản sửa hoặc chạy làm dịch vụ phải công bố mã; README khuyên doanh nghiệp dùng bản Enterprise trả phí; tính năng tài khoản Fincept và AI dùng máy chủ Fincept; dữ liệu cần API key/tài khoản nguồn riêng của người dùng |
| [`akfamily/akshare`](https://github.com/akfamily/akshare) | 23.377 | MIT (Copyright 2019-2026 AKFamily) | AKShare: thư viện Python lấy dữ liệu tài chính (cổ phiếu, quỹ, phái sinh, tiền mã hóa, vĩ mô…) từ nhiều nguồn công khai qua giao diện hàm đơn giản. | Phát hành trên PyPI, yêu cầu Python 64-bit 3.11.5 trở lên; dự án đi kèm AKTools cung cấp máy chủ MCP đã đăng ký trong MCP Registry chính thức (io.github.akfamily/aktools) và HTTP API; có tài liệu tiếng Trung đầy đủ | `pip install akshare --upgrade` | README tuyên bố dữ liệu chỉ dùng cho nghiên cứu học thuật, nhà đầu tư phải tự lưu ý rủi ro dữ liệu; dữ liệu lấy từ website bên thứ ba |
| [`stefan-jansen/machine-learning-for-trading`](https://github.com/stefan-jansen/machine-learning-for-trading) | 21.870 | MIT License (Copyright (c) 2024-2026 Stefan Jansen) | Mã nguồn và notebook của sách Machine Learning for Trading bản 3: quy trình ML cho giao dịch từ nguồn dữ liệu, đặc trưng, mô hình, backtest tới giao dịch thật và MLOps. | 27 thư mục chương và 9 case study (ETF, crypto perps, NASDAQ-100, FX…) chạy cùng một pipeline; môi trường tái lập bằng Docker (docker-compose) hoặc uv; bản 2 vẫn giữ trên nhánh second-edition | `docker compose pull ml4t (hoặc uv sync)` | Phần giao dịch thật dùng tài khoản môi giới (Interactive Brokers, Alpaca, QuantConnect); một số dữ liệu cần tải riêng |
| [`AI4Finance-Foundation/FinGPT`](https://github.com/AI4Finance-Foundation/FinGPT) | 21.589 | MIT License (Copyright (c) 2024 AI4Finance Foundation Inc.) | Dự án mô hình ngôn ngữ lớn mã nguồn mở cho tài chính: tinh chỉnh LoRA các LLM mở cho phân tích cảm xúc, dự báo, RAG và benchmark tài chính. | Thư mục fingpt có các module Forecaster, Sentiment Analysis, RAG, MultiAgentsRAG, Benchmark; mô hình LoRA phát hành trên HuggingFace; nhiều bài báo được nhận tại workshop NeurIPS/IJCAI 2023 | `pip install -r requirements.txt && pip install -e .` | Mô hình cục bộ cần GPU, hoặc dùng API đám mây (ví dụ OpenAI) cần khoá; README ghi chỉ cho mục đích học thuật, không phải lời khuyên tài chính; mô hình nền (Llama…) có giấy phép riêng |
| [`hummingbot/hummingbot`](https://github.com/hummingbot/hummingbot) | 21.248 | Apache License 2.0 | Framework mã nguồn mở để thiết kế và chạy bot giao dịch tự động (market making, arbitrage…) trên nhiều sàn tập trung và phi tập trung. | CLI hbot điều khiển bot không tương tác với exit code ổn định; connector cho CEX CLOB, DEX CLOB và AMM DEX (qua Gateway); có chế độ paper trade trên dữ liệu Binance thật không cần API key | `make install && conda activate hummingbot (hoặc make setup && make deploy với Docker)` | Giao dịch thật cần API key sàn hoặc khoá ví và dùng tiền thật; cần Anaconda/Miniconda hoặc Docker |
| [`xbtlin/ai-berkshire`](https://github.com/xbtlin/ai-berkshire) | 17.175 | MIT License (Copyright (c) 2026 xbtlin) | Bộ skill nghiên cứu đầu tư giá trị cho Claude Code và Codex, hệ thống hoá phương pháp của Buffett, Munger, Đoàn Vĩnh Bình, Lý Lục để sinh báo cáo phân tích doanh nghiệp. | Có 21 file skill trong thư mục skills cùng codex-skills; công cụ tools/financial_rigor.py tính bằng decimal.Decimal để kiểm vốn hoá; báo cáo cấu trúc thống nhất với kết luận Pass/Fail/Gray Zone | `Cài Claude Code hoặc Codex rồi cài skills theo README` | Cần Claude Code hoặc Codex (tài khoản và chi phí token cao); README ghi chỉ cho giáo dục và nghiên cứu, không phải lời khuyên đầu tư; nội dung chủ yếu tiếng Trung; README gợi ý --dangerously-skip-permissions (tắt hàng rào duyệt) |

#### 6c.5.25 Tài liệu, OCR & Thị giác máy tính

Đọc mã 23 repo, giữ 22.

| Repo | ★ (18/11/2026) | Giấy phép | Làm gì | Điểm mạnh (đọc mã) | Cài | Điều kiện dùng |
|---|---|---|---|---|---|---|
| [`microsoft/markitdown`](https://github.com/microsoft/markitdown) | 196.149 | MIT License (Copyright (c) Microsoft Corporation) | Tiện ích Python chuyển nhiều định dạng tệp (PDF, Word, PowerPoint, Excel, HTML, ảnh, âm thanh, EPub…) sang Markdown để đưa vào LLM. | Có CLI markitdown và extras tuỳ chọn theo định dạng ([pdf], [docx], [all]…); repo gồm các gói markitdown-mcp, markitdown-ocr và plugin mẫu; tích hợp tuỳ chọn Azure Document Intelligence và Content Understanding | `pip install 'markitdown[all]'` | Python 3.10–3.14; chú thích ảnh và phiên âm dùng dịch vụ web; Azure là API trả phí cần khoá; README cảnh báo phải lọc đầu vào trong môi trường không tin cậy |
| [`Stirling-Tools/Stirling-PDF`](https://github.com/Stirling-Tools/Stirling-PDF) | 96.871 | MIT License cho phần lõi; các thư mục app/proprietary, app/saas, engine, một số thư mục frontend theo Stirling PDF User License (độc quyền, dùng production cần thuê bao) | Nền tảng chỉnh sửa PDF tự host (desktop, trình duyệt, server có API riêng) với hơn 50 công cụ: sửa, gộp, tách, ký, che, chuyển đổi, OCR, nén. | Chạy nhanh bằng một lệnh docker run; REST API cho hầu hết công cụ và pipeline tự động không cần code; giao diện hơn 40 ngôn ngữ | `docker run -p 8080:8080 docker.stirlingpdf.com/stirlingtools/stirling-pdf` | Mô hình open-core: phần độc quyền cấm dùng production, phân phối, dùng thương mại khi không có User License trả phí; tính năng SSO/enterprise thuộc gói trả phí |
| [`opencv/opencv`](https://github.com/opencv/opencv) | 91.621 | Apache License 2.0 | Thư viện thị giác máy tính mã nguồn mở (C++ với binding Python, Java, JS, Objective-C) cho xử lý ảnh, video, đặc trưng, DNN, hiệu chỉnh camera. | Nhánh mặc định 5.x (phiên bản 5.2.0-dev); các module core, imgproc, dnn, calib, video, videoio, stitching, objdetect…; chức năng bổ sung ở repo opencv_contrib |  |  |
| [`ultralytics/ultralytics`](https://github.com/ultralytics/ultralytics) | 63.544 | GNU Affero General Public License v3.0 (AGPL-3.0); có Ultralytics Enterprise License thương mại thay thế | Gói Python và CLI cho các mô hình YOLO (tới YOLO26) phục vụ phát hiện vật thể, phân đoạn, ước lượng tư thế, độ sâu, phân loại, OBB và theo dõi. | Một gói thống nhất Python và CLI cho nhiều tác vụ thị giác; mô hình huấn luyện sẵn tự tải từ release khi dùng lần đầu; có trên PyPI, conda-forge và Docker Hub | `pip install ultralytics` | AGPL-3.0: dùng trong sản phẩm/dịch vụ phải mở mã hoặc mua Enterprise License |
| [`roboflow/supervision`](https://github.com/roboflow/supervision) | 51.661 | MIT License (Copyright (c) 2022 Roboflow) | Bộ công cụ Python cho thị giác máy tính độc lập mô hình: chuẩn hoá kết quả phát hiện, annotator vẽ, tải/chuyển đổi dataset, đếm theo vùng, metric. | Connector cho Ultralytics, Transformers, MMDetection, Inference về kiểu sv.Detections; module annotators, dataset, metrics, key_points, geometry; có codecov và demo trên Colab, HuggingFace Spaces | `pip install supervision` | Python>=3.10; dùng Roboflow Inference cần Roboflow API key |
| [`google/langextract`](https://github.com/google/langextract) | 39.339 | Apache License 2.0 | Thư viện Python dùng LLM để trích xuất thông tin có cấu trúc từ văn bản phi cấu trúc theo chỉ dẫn và ví dụ few-shot của người dùng. | Gắn mỗi kết quả trích xuất với vị trí chính xác trong văn bản nguồn; xử lý tài liệu dài bằng chia đoạn, chạy song song và nhiều lượt; hỗ trợ Gemini, OpenAI và mô hình cục bộ qua Ollama, xuất HTML trực quan hoá tương tác | `pip install langextract` | Mô hình đám mây (Gemini, OpenAI) cần API key, mô hình cục bộ thì không; README ghi không phải sản phẩm Google hỗ trợ chính thức; ứng dụng y tế còn chịu Health AI Developer Foundations Terms of Use |
| [`PDFMathTranslate/PDFMathTranslate`](https://github.com/PDFMathTranslate/PDFMathTranslate) | 38.500 | GNU Affero General Public License v3 (AGPL-3.0) | Công cụ dịch tài liệu PDF khoa học (pdf2zh) giữ nguyên bố cục, công thức, biểu đồ, mục lục và chú thích. | Có CLI, giao diện tương tác và Docker; hỗ trợ nhiều dịch vụ dịch (mặc định Google, có DeepL, OpenAI…); xuất cả bản dịch đơn ngữ và song ngữ, có chế độ --ultrafast cho PDF có sẵn văn bản | `uv tool install --python 3.12 pdf2zh` | Giấy phép AGPL-3.0 (copyleft, áp dụng cả khi cung cấp qua mạng); cần Python 3.11–3.12; một số dịch vụ dịch cần khoá API; bản 2.0 phát triển ở repo riêng PDFMathTranslate-next |
| [`google-ai-edge/mediapipe`](https://github.com/google-ai-edge/mediapipe) | 37.733 | Apache License 2.0 | Bộ thư viện và framework học máy chạy trên thiết bị (Android, iOS, web, desktop, edge/IoT) với các giải pháp dựng sẵn cho thị giác, văn bản, âm thanh và GenAI. | MediaPipe Tasks cung cấp API đa nền tảng kèm mô hình huấn luyện sẵn; MediaPipe Studio cho trực quan hoá, thử và đo hiệu năng giải pháp trên trình duyệt; framework cấp thấp dựa trên graph và calculator để tự dựng pipeline |  | Tài liệu chính nằm ở developers.google.com/edge/mediapipe; build framework từ nguồn dùng Bazel |
| [`huggingface/pytorch-image-models`](https://github.com/huggingface/pytorch-image-models) | 37.290 | Apache License 2.0 | Thư viện timm: tập hợp mô hình ảnh, layer, optimizer, scheduler, data loader và script huấn luyện/kiểm định tham chiếu cho PyTorch. | Phát hành đều (bản 1.0.31 ngày 3/11/2026); mọi mô hình hỗ trợ forward_intermediates() và prune_intermediate_layers(); có script train, validate, inference, sweep siêu tham số và xuất ONNX | `pip install timm` | Mã Apache 2.0 nhưng trọng số huấn luyện sẵn chủ yếu từ ImageNet (chỉ cho nghiên cứu phi thương mại), một số trọng số Facebook theo CC-BY-NC 4.0; README khuyên hỏi tư vấn pháp lý trước khi dùng thương mại |
| [`facebookresearch/detectron2`](https://github.com/facebookresearch/detectron2) | 34.995 | Apache License 2.0 | Thư viện PyTorch của Meta AI cho phát hiện đối tượng và phân đoạn ảnh, kế nhiệm Detectron và maskrcnn-benchmark. | Hỗ trợ panoptic segmentation, DensePose, Cascade R-CNN, rotated box, PointRend, ViTDet, MViTv2; có Model Zoo lớn với kết quả baseline và mô hình huấn luyện sẵn; xuất mô hình sang TorchScript hoặc Caffe2 | `python -m pip install 'git+https://github.com/facebookresearch/detectron2.git'` | Cần Linux hoặc macOS, Python ≥ 3.7, PyTorch ≥ 1.8 kèm torchvision khớp, gcc/g++ ≥ 5.4; Windows không được hỗ trợ chính thức |
| [`explosion/spaCy`](https://github.com/explosion/spaCy) | 34.067 | MIT License | Thư viện xử lý ngôn ngữ tự nhiên công nghiệp viết bằng Python và Cython, có pipeline huấn luyện sẵn. | Hỗ trợ tách từ và huấn luyện cho hơn 70 ngôn ngữ; có mô hình cho gắn nhãn từ loại, phân tích cú pháp, NER, phân loại văn bản và hỗ trợ transformer như BERT; có hệ thống huấn luyện, đóng gói và tích hợp LLM | `pip install spacy` | Python >=3.7, <3.13 (chỉ 64 bit) theo README |
| [`opendataloader-project/opendataloader-pdf`](https://github.com/opendataloader-project/opendataloader-pdf) | 30.331 | Apache License 2.0 (NOTICE: Copyright 2025-2026 Hancom, Inc.; thành phần bên thứ ba theo giấy phép riêng trong THIRD_PARTY) | Bộ phân tích PDF trích xuất Markdown, JSON có bounding box và HTML cho pipeline RAG/LLM, đồng thời tự gắn thẻ PDF chưa gắn thẻ thành Tagged PDF phục vụ trợ năng. | Chế độ cục bộ tất định với thứ tự đọc XY-Cut++ và bounding box cho mọi phần tử; chế độ hybrid xử lý bảng phức tạp, OCR, công thức LaTeX và mô tả hình; có SDK Python, Node.js và Java, tích hợp LangChain | `pip install -U opendataloader-pdf` | Cần Java 11+ và Python 3.11+; xuất PDF/UA-1, PDF/UA-2 và accessibility studio là bản enterprise trả phí; con số benchmark #1 do dự án tự công bố |
| [`JaidedAI/EasyOCR`](https://github.com/JaidedAI/EasyOCR) | 30.151 | Apache License 2.0 | Thư viện OCR dùng ngay, nhận dạng chữ trong ảnh với hơn 80 ngôn ngữ và các hệ chữ phổ biến. | Hỗ trợ Latin, Trung, Ả Rập, Devanagari, Cyrillic…; API đơn giản trả về bounding box, văn bản và độ tin cậy; có Dockerfile và tùy chọn bộ phát hiện DBNet | `pip install easyocr` | Trên Windows cần cài torch và torchvision trước; DBNet cần Ninja để biên dịch; bản phát hành ổn định gần nhất ghi trong README là 1.7.2 (24/9/2024) |
| [`serengil/deepface`](https://github.com/serengil/deepface) | 23.709 | MIT License | Framework Python nhẹ cho nhận diện khuôn mặt và phân tích thuộc tính khuôn mặt (tuổi, giới tính, cảm xúc, chủng tộc). | Bọc nhiều mô hình nhận diện (VGG-Face, FaceNet, ArcFace, SFace, GhostFaceNet…) và nhiều bộ phát hiện khuôn mặt; chạy trên ONNX Runtime, TensorFlow hoặc PyTorch; có API REST, gRPC và tìm kiếm 1:N dựa trên cơ sở dữ liệu | `pip install deepface` | Các mô hình và bộ phát hiện được bọc có giấy phép riêng của từng nguồn; xử lý dữ liệu sinh trắc học khuôn mặt cần tuân thủ luật bảo vệ dữ liệu (README không nêu điều khoản riêng) |
| [`huggingface/datasets`](https://github.com/huggingface/datasets) | 22.154 | Apache License 2.0 | Thư viện tải, chia sẻ và tiền xử lý tập dữ liệu (từ Hugging Face Hub hoặc file cục bộ) dựa trên Apache Arrow. | Tải dữ liệu một dòng với load_dataset() và hỗ trợ streaming; lưu trữ ánh xạ bộ nhớ zero-copy qua Apache Arrow kèm cache tự động; chuyển đổi qua lại NumPy, Pandas, Polars, PyTorch, TensorFlow, JAX, Spark | `pip install datasets` | Mỗi tập dữ liệu trên Hub có giấy phép riêng do chủ dữ liệu quy định; README khuyên ghim revision để tái lập |
| [`firecrawl/pdf-inspector`](https://github.com/firecrawl/pdf-inspector) | 20.052 | MIT (Copyright (c) 2026 Firecrawl) | Thư viện Rust phân loại PDF (dạng văn bản hay ảnh quét) và trích xuất văn bản có vị trí, chuyển thành Markdown sạch mà không cần OCR; có binding Python, Node.js và WebAssembly. | Phân loại TextBased/Scanned/ImageBased/Mixed trong khoảng 10–50 ms kèm điểm tin cậy và định tuyến OCR theo trang; dò bảng hai chế độ (hình chữ nhật từ lệnh vẽ PDF và heuristic theo căn lề), hỗ trợ bố cục nhiều cột và RTL; OCR chọn lọc PP-OCRv6 Small chạy cục bộ chỉ cho trang cần OCR | `cargo add pdf-inspector (hoặc pip install pdf-inspector; npm install @firecrawl/pdf-inspector)` | OCR chọn lọc cần PDFium, ONNX Runtime và file mô hình đặt ngoài gói |
| [`pytorch/vision`](https://github.com/pytorch/vision) | 18.016 | BSD 3-Clause (Copyright (c) Soumith Chintala 2016); mô hình huấn luyện sẵn có thể theo giấy phép riêng (mô hình SWAG là CC-BY-NC 4.0) | Gói torchvision của PyTorch cung cấp bộ dữ liệu phổ biến, kiến trúc mô hình và các phép biến đổi ảnh cho thị giác máy tính. | Mã nguồn có các mô-đun datasets, models, transforms, ops, io và tv_tensors; README có bảng tương thích phiên bản torch/torchvision/Python tới torch 2.13 và torchvision 0.28; hỗ trợ backend ảnh tensor torch và PIL (Pillow, Pillow-SIMD) | `Cài theo hướng dẫn https://pytorch.org/get-started/locally/ (cùng torch)` | Không phân phối bộ dữ liệu, người dùng tự xác định quyền dùng theo giấy phép từng bộ dữ liệu; mô hình huấn luyện sẵn có thể có điều khoản riêng, SWAG là CC-BY-NC 4.0 (phi thương mại) |
| [`cvat-ai/cvat`](https://github.com/cvat-ai/cvat) | 17.157 | MIT (Copyright 2018-2022 Intel Corporation, 2022-2025 CVAT.ai Corporation); một số tài sản serverless và phụ thuộc có giấy phép riêng | CVAT Community là bản mã nguồn mở tự host của nền tảng gán nhãn dữ liệu cho ảnh, video, âm thanh và 3D, phục vụ thị giác máy tính. | Hỗ trợ gán nhãn ảnh, video, âm thanh và 3D cùng quản lý bộ dữ liệu, cộng tác nhiều người với vai trò và quy trình review; cho phép nối mô hình ML riêng để hỗ trợ gán nhãn tự động; repo kèm SDK (cvat-sdk), CLI (cvat-cli), Helm chart và docker compose | `git clone https://github.com/cvat-ai/cvat && cd cvat && docker compose up -d` | Cần Docker Engine, Docker Compose và Git; kiểm thử chủ yếu trên trình duyệt Chromium, Safari/WebKit không hỗ trợ; tài sản serverless và phụ thuộc có thể theo giấy phép khác |
| [`wkentaro/labelme`](https://github.com/wkentaro/labelme) | 16.335 | GNU GPL v3 | Công cụ gán nhãn ảnh có giao diện đồ hoạ viết bằng Python và Qt, hỗ trợ đa giác, hình chữ nhật, hình tròn, đường, điểm và gán nhãn video. | Xuất bộ dữ liệu định dạng VOC (phân đoạn ngữ nghĩa và thực thể) và COCO (phân đoạn thực thể); gán nhãn hỗ trợ AI bằng SAM, EfficientSAM, YOLO-world và SAM3; giao diện có 21 ngôn ngữ, gồm tiếng Việt | `pip install labelme` | Giấy phép GPLv3 (copyleft); bản thực thi độc lập trên labelme.io là bản trả phí một lần |
| [`Unstructured-IO/unstructured`](https://github.com/Unstructured-IO/unstructured) | 15.762 | Apache License 2.0 | Thư viện Python mã nguồn mở để nạp và tiền xử lý tài liệu (PDF, HTML, Word, ảnh…) thành dữ liệu có cấu trúc cho quy trình LLM. | Cung cấp hàm partition theo loại tài liệu như partition_pdf, partition_text; cài theo nhóm phụ thuộc tuỳ chọn (all-docs, docx, pptx…); có image Docker đa nền tảng x86_64 và Apple silicon | `pip install "unstructured[all-docs]"` | Tuỳ loại tài liệu cần thêm gói hệ thống libmagic-dev, poppler-utils, tesseract-ocr, libreoffice; chất lượng cao hơn qua API Transform trả phí của nhà phát triển (thư viện mã nguồn mở vẫn miễn phí) |
| [`cmusatyalab/openface`](https://github.com/cmusatyalab/openface) | 15.451 | Apache License 2.0 (mã và mô hình Torch/Python của Carnegie Mellon University); phần bên thứ ba theo MIT, BSD, CC0 | Thư viện nhận dạng khuôn mặt bằng mạng nơ-ron sâu của CMU, gồm thư viện Python, mô hình huấn luyện sẵn, script huấn luyện và các demo. | Có script batch-represent sinh biểu diễn cho lô ảnh và demo so sánh ảnh, phân loại, webcam, web thời gian thực; kèm script đánh giá độ chính xác trên LFW và script huấn luyện mô hình mới; có báo cáo kỹ thuật CMU-CS-16-118 để trích dẫn |  | Dùng mô hình Torch (Lua); một số phần bên thứ ba theo giấy phép riêng (MIT, BSD, CC0) |
| [`davisking/dlib`](https://github.com/davisking/dlib) | 14.477 | Boost Software License 1.0 | Bộ công cụ C++ hiện đại chứa thuật toán học máy và công cụ xây dựng phần mềm C++ phức tạp, có API Python. | Giấy phép Boost cho phép dùng cả trong phần mềm thương mại mã đóng; cài được qua pip, vcpkg hoặc CMake, hỗ trợ bật lệnh AVX để tăng tốc; có bộ unit test chạy bằng dtest --runall | `pip install dlib (C++: vcpkg install dlib)` | Cần trình biên dịch C++17 và CMake khi build |

**Chưa thêm (1 repo, giữ trong file dữ liệu):** `ultralytics/yolov5` (đã có ultralytics/ultralytics cùng tác giả, bản mới hơn (tới YOLO26)).

#### 6c.5.26 Tự host & Nhà thông minh

Đọc mã 9 repo, giữ 9.

| Repo | ★ (18/11/2026) | Giấy phép | Làm gì | Điểm mạnh (đọc mã) | Cài | Điều kiện dùng |
|---|---|---|---|---|---|---|
| [`awesome-selfhosted/awesome-selfhosted`](https://github.com/awesome-selfhosted/awesome-selfhosted) | 338.129 | CC-BY-SA-3.0 | Danh sách các dịch vụ mạng và ứng dụng web phần mềm tự do có thể tự host trên máy chủ riêng, chia theo hạng mục. | Khoảng 1277 mục liệt kê trong README chia theo nhiều hạng mục (Analytics, Backup, Automation…); có kiểm tra tự động link chết và dự án không còn bảo trì; phần mềm không tự do tách riêng ở non-free.md, có bản HTML tại awesome-selfhosted.net |  | Nội dung theo CC-BY-SA-3.0 (ghi công, chia sẻ tương tự) |
| [`immich-app/immich`](https://github.com/immich-app/immich) | 119.489 | GNU AGPL v3 | Giải pháp tự host quản lý ảnh và video hiệu năng cao, có ứng dụng web và di động. | Sao lưu tự động và nền từ di động, chống trùng lặp, hỗ trợ ảnh raw, LivePhoto/MotionPhoto; tìm kiếm theo metadata, vật thể, khuôn mặt và CLIP, nhận diện và gom nhóm khuôn mặt; hỗ trợ nhiều người dùng, OAuth, chia sẻ công khai và đối tác, có các file docker compose kèm cấu hình tăng tốc phần cứng | `Cài theo hướng dẫn https://docs.immich.app/install/requirements (docker compose)` | Giấy phép AGPLv3; README khuyến cáo luôn theo kế hoạch sao lưu 3-2-1 cho ảnh và video |
| [`home-assistant/core`](https://github.com/home-assistant/core) | 92.443 | Apache License 2.0 | Nền tảng tự động hoá nhà ở mã nguồn mở ưu tiên điều khiển cục bộ và quyền riêng tư, chạy được trên Raspberry Pi hoặc máy chủ cục bộ. | Kiến trúc mô-đun với khoảng 1569 thư mục tích hợp trong homeassistant/components; thuộc Open Home Foundation và có cộng đồng toàn cầu; có demo trực tuyến và tài liệu kiến trúc, hướng dẫn tạo tích hợp riêng | `Cài theo hướng dẫn https://home-assistant.io/getting-started/` | Đóng góp mã cần ký CLA (có file CLA.md) |
| [`syncthing/syncthing`](https://github.com/syncthing/syncthing) | 90.532 | Mozilla Public License 2.0 | Chương trình đồng bộ tệp liên tục, ngang hàng giữa hai hay nhiều máy tính, không cần máy chủ trung tâm. | Bản phát hành ký GPG, bản macOS và Windows được ký mã; có huy hiệu CII Best Practices; dựng từ mã nguồn chỉ bằng `go run build.go`, có Dockerfile chính thức | `go run build.go (hoặc xem hướng dẫn Getting Started và README-Docker)` |  |
| [`go-gitea/gitea`](https://github.com/go-gitea/gitea) | 59.145 | MIT | Dịch vụ phát triển phần mềm tự host trọn gói: Git hosting, review mã, issue, kanban, wiki, registry gói và CI/CD tương thích GitHub Actions. | Viết bằng Go, chạy trên Linux, macOS, FreeBSD/OpenBSD, Windows với nhiều kiến trúc (amd64, ARM, RISC-V 64, PowerPC); có ảnh Docker chính thức và bản demo demo.gitea.com; có go-sdk, CLI gt và action runner chính thức | `./gitea web (sau khi build) hoặc ảnh Docker gitea/gitea` |  |
| [`blakeblackshear/frigate`](https://github.com/blakeblackshear/frigate) | 37.549 | MIT (tên Frigate, thương hiệu Frigate NVR và logo là thương hiệu của Frigate, Inc., không thuộc MIT — xem TRADEMARK.md) | NVR chạy cục bộ cho camera IP, tích hợp chặt với Home Assistant, phát hiện vật thể bằng AI theo thời gian thực. | Chỉ chạy phát hiện vật thể ở vùng có chuyển động để giảm tài nguyên; giao tiếp qua MQTT, ghi hình 24/7 và lưu giữ theo vật thể phát hiện; restream RTSP và xem trực tiếp độ trễ thấp qua WebRTC/MSE | `docker compose (xem docs.frigate.video)` | Khuyến nghị mạnh dùng GPU hoặc bộ tăng tốc AI; không dùng tên/logo Frigate trái chính sách thương hiệu; ghi hình camera cần tuân thủ luật quyền riêng tư nơi lắp đặt |
| [`1Panel-dev/1Panel`](https://github.com/1Panel-dev/1Panel) | 37.464 | GNU GPL v3 | Bảng điều khiển quản trị máy chủ Linux qua web kèm nền tảng quản lý AI: giám sát, tệp, cơ sở dữ liệu, container, website, sao lưu. | Kho ứng dụng tích hợp cài một chạm (README nêu 165+ ứng dụng); cấu hình tên miền và SSL một chạm cho website như WordPress, Halo; sao lưu/khôi phục một chạm tích hợp nhiều kho lưu trữ đám mây | `bash -c "$(curl -sSL https://resource.1panel.pro/v2/quick_start.sh)"` | Chỉ chạy trên Linux; một số tính năng (đa node, chống sửa website, AI Gateway…) chỉ có ở bản Pro/Ent trả phí; cài đặt bằng script tải từ mạng chạy quyền root |
| [`lissy93/dashy`](https://github.com/lissy93/dashy) | 27.015 | MIT | Trang chủ/dashboard tự host cho homelab, tập hợp liên kết ứng dụng kèm widget và giám sát trạng thái. | Cấu hình bằng một tệp YAML hoặc qua giao diện; giám sát trạng thái thời gian thực, widget, nhiều trang, xác thực đa người dùng có SSO; hơn 30 ngôn ngữ dịch bởi người | `docker run -p 8080:8080 lissy93/dashy` |  |
| [`haiwen/seafile`](https://github.com/haiwen/seafile) | 15.468 | GPL v2 kèm ngoại lệ cho phép liên kết với OpenSSL (README: client iOS Apache 2.0, Android GPLv3, server core AGPLv3, Seahub Apache 2.0) | Repo daemon client đồng bộ của Seafile, hệ thống lưu trữ đám mây mã nguồn mở có mã hoá thư viện và cộng tác nhóm. | Đồng bộ chọn lọc, chỉ truyền phần thay đổi và tiếp tục được khi gián đoạn; mã hoá thư viện bằng mật khẩu người dùng, mã hoá phía client khi đồng bộ desktop; xử lý xung đột dựa trên lịch sử thay vì dấu thời gian | `Xem hướng dẫn build tại manual.seafile.com` | Repo này chỉ là daemon client; server, web UI và app di động nằm ở repo riêng với giấy phép khác; khách hàng Pro liên hệ qua email |

#### 6c.5.27 Đồ họa, 3D & Sơ đồ

Đọc mã 10 repo, giữ 10.

| Repo | ★ (18/11/2026) | Giấy phép | Làm gì | Điểm mạnh (đọc mã) | Cài | Điều kiện dùng |
|---|---|---|---|---|---|---|
| [`d3/d3`](https://github.com/d3/d3) | 113.955 | ISC (văn bản giấy phép kiểu ISC, Copyright 2010-2026 Mike Bostock) | Thư viện JavaScript mã nguồn mở cấp thấp để trực quan hoá dữ liệu trên nền chuẩn web. | Phiên bản 7.9.2 trong package.json; tài liệu tại d3js.org và thư viện ví dụ trên Observable; dùng được qua npm hoặc CDN ESM | `npm install d3` |  |
| [`hakimel/reveal.js`](https://github.com/hakimel/reveal.js) | 72.597 | MIT | Framework trình chiếu HTML mã nguồn mở, tạo slide chạy trên trình duyệt. | Hỗ trợ slide lồng dọc, Markdown, Auto-Animate, xuất PDF, ghi chú người nói; phiên bản 6.0.2 trong package.json; có trình chỉnh sửa trực quan Slides.com cùng tác giả | `Xem revealjs.com/installation` | Khoá học video reveal.js là trả phí; Slides.com là dịch vụ riêng |
| [`drawdb-io/drawdb`](https://github.com/drawdb-io/drawdb) | 40.335 | GNU AGPL v3 | Trình soạn sơ đồ quan hệ thực thể (ERD) cơ sở dữ liệu chạy trên trình duyệt, sinh và nhập/xuất script SQL. | Dùng không cần tạo tài khoản; xuất/nhập SQL và sinh migration; có Dockerfile và ảnh ghcr.io/drawdb-io/drawdb | `docker run -p 3000:80 ghcr.io/drawdb-io/drawdb:latest` | Tính năng chia sẻ cần tự dựng drawdb-server; AGPLv3 buộc công bố mã khi cung cấp bản sửa qua mạng |
| [`DayuanJiang/next-ai-draw-io`](https://github.com/DayuanJiang/next-ai-draw-io) | 37.029 | Apache License 2.0 | Ứng dụng vẽ và sửa sơ đồ draw.io bằng cách trò chuyện với AI; có bản web, desktop và MCP server cho agent. | Hỗ trợ 25 nhà cung cấp mô hình kể cả preset tương thích OpenAI; mỗi thay đổi của AI là một phiên bản so sánh, khôi phục, hoàn tác được; xuất .drawio, .png, .svg | `npx @next-ai-drawio/mcp-server@latest (MCP) hoặc git clone rồi npm install, npm run dev` | Cần API key nhà cung cấp mô hình AI (mặc định AWS Bedrock); bản demo trực tuyến có giới hạn sử dụng |
| [`lutzroeder/netron`](https://github.com/lutzroeder/netron) | 33.703 | MIT | Trình xem mô hình mạng nơ-ron, học sâu và học máy; hiển thị đồ thị mô hình trên trình duyệt hoặc ứng dụng desktop. | Hỗ trợ ONNX, TensorFlow Lite, PyTorch, Core ML, OpenVINO, Keras, Safetensors và nhiều định dạng khác; có bản trình duyệt netron.app không cần cài; có bản macOS, Linux, Windows và gói Python | `pip install netron rồi netron [FILE]` |  |
| [`pascalorg/editor`](https://github.com/pascalorg/editor) | 25.591 | MIT (Copyright 2026 Pascal Group Inc.) | Trình biên tập mô hình công trình 3D mã nguồn mở cho kiến trúc, xây dựng (AECO) chạy trên trình duyệt, có CLI cục bộ và máy chủ MCP cho AI agent. | Chạy cục bộ không cần tài khoản, dữ liệu lưu SQLite trên máy; tự host bằng một container Docker; có gói npm @pascal-app/core, viewer, cli để nhúng vào ứng dụng React | `npx @pascal-app/cli editor` | CLI cần Node.js 22.23.4+/24.22.1+/26.12.1+; chế độ hosted cần tài khoản Pascal và API key, một số thao tác tốn credit; mỗi dịch vụ CLI cục bộ chỉ dùng một agent client |
| [`plotly/dash`](https://github.com/plotly/dash) | 24.494 | MIT | Framework Python để xây ứng dụng web dữ liệu và học máy, gắn thành phần giao diện (dropdown, slider, biểu đồ) trực tiếp với mã phân tích Python. | Xây trên Plotly.js, React và Flask; khoảng 50 loại biểu đồ qua Plotly.js; được Plotly bảo trì, phát hành trên PyPI | `pip install dash` | Bản mã nguồn mở chạy cục bộ; tính năng triển khai, xác thực, mở rộng nằm ở Dash Enterprise trả phí |
| [`ahmedkhaleel2004/gitdiagram`](https://github.com/ahmedkhaleel2004/gitdiagram) | 18.977 | MIT | Biến kho GitHub thành sơ đồ kiến trúc tương tác do AI sinh, hoặc video thuyết minh khoảng một phút. | Bấm thành phần trong sơ đồ để nhảy tới file mã; xuất PNG hoặc mã Mermaid; có máy chủ MCP từ xa không cần khoá cho AI agent | `claude mcp add --transport http gitdiagram https://gitdiagram.com/mcp` | Chạy cục bộ cần Bun, Cloudflare R2, Upstash Redis và khoá API OpenAI hoặc OpenRouter; video cần thêm khoá Anthropic; kho riêng cần GitHub token; tạo video mới đang ở dạng truy cập sớm |
| [`tangency-labs/solidcraft`](https://github.com/tangency-labs/solidcraft) | 16.970 | MIT hoặc Apache-2.0 (song cấp phép) cho mã; giao diện, theme, icon, tên và logo theo SolidCraft Brand and Interface Licence riêng (LICENSE-BRAND) | Ứng dụng CAD 3D tham số mã nguồn mở viết bằng Rust thuần: phác thảo, ràng buộc, dựng khối theo dòng thời gian tính năng; chạy desktop, trình duyệt, CLI và máy chủ MCP. | 75/76 chi tiết tham chiếu công khai khớp thể tích, diện tích, trọng tâm với giá trị giải tích hoặc FreeCAD; nhập xuất STEP, IGES, 3MF, STL, OBJ, glTF; có lắp ráp, kim loại tấm và máy chủ MCP qua solidcraft-cli mcp | `sudo snap install solidcraft` | README nói bản còn sớm, dùng được cho chi tiết đơn giản (phiên bản 0.x); dùng UI kit, theme, icon, tên SolidCraft ngoài SolidCraft hoặc phân phối fork trùng diện mạo cần phép bằng văn bản; DISCLAIMER yêu cầu người có chuyên môn kiểm kết quả trước khi dùng cho quyết định thiết kế, sản xuất, an toàn |
| [`plait-board/drawnix`](https://github.com/plait-board/drawnix) | 15.080 | MIT | Bảng trắng mã nguồn mở tất cả trong một: sơ đồ tư duy, lưu đồ, vẽ tay trên canvas vô hạn, xây trên framework Plait. | Chuyển cú pháp Mermaid thành lưu đồ và Markdown thành sơ đồ tư duy; xuất PNG, JPG, JSON và tự lưu vào bộ nhớ trình duyệt; có image Docker để tự host | `docker pull pubuzhixing/drawnix:latest` |  |

#### 6c.5.28 Ứng dụng đa nền tảng & Game

Đọc mã 11 repo, giữ 11.

| Repo | ★ (18/11/2026) | Giấy phép | Làm gì | Điểm mạnh (đọc mã) | Cài | Điều kiện dùng |
|---|---|---|---|---|---|---|
| [`electron/electron`](https://github.com/electron/electron) | 123.959 | MIT | Framework viết ứng dụng desktop đa nền tảng bằng JavaScript, HTML và CSS, dựa trên Node.js và Chromium. | Cung cấp binary cho macOS, Windows, Linux (x64 và arm64); được dùng bởi Visual Studio Code; có Electron Fiddle để thử nghiệm nhanh | `npm install electron --save-dev` | macOS Ventura trở lên, Windows 10 trở lên |
| [`godotengine/godot`](https://github.com/godotengine/godot) | 120.330 | MIT (Copyright Godot Engine contributors, Juan Linietsky, Ariel Manzur); mã bên thứ ba trong thirdparty/ theo giấy phép riêng ghi ở COPYRIGHT.txt | Engine game 2D và 3D đa nền tảng với giao diện biên tập thống nhất, xuất game một cú bấm ra desktop, di động, web. | Giấy phép MIT, không thu phí bản quyền; xuất sang Linux, macOS, Windows, Android, iOS và web; được Godot Foundation phi lợi nhuận hỗ trợ | `Tải binary tại godotengine.org/download` | Xuất sang console cần qua bên thứ ba (theo trang consoles của Godot, chưa xác minh chi tiết) |
| [`ocornut/imgui`](https://github.com/ocornut/imgui) | 77.153 | MIT | Thư viện giao diện người dùng immediate-mode cho C++, gọn nhẹ, sinh vertex buffer để render trong ứng dụng 3D; hợp cho công cụ, debug trong game engine. | Lõi tự chứa trong vài file imgui*.cpp/h, không phụ thuộc ngoài, không cần quy trình build riêng; có backend cho DirectX 9-12, OpenGL, Metal, SDL2/3, GLFW, Android, Allegro; kèm ví dụ trong examples/ | `Thêm các file imgui*.cpp, imgui*.h và một backend vào dự án` |  |
| [`tw93/Pake`](https://github.com/tw93/Pake) | 63.759 | GPL-3.0 kèm ngoại lệ Pake Output Exception (ứng dụng sinh ra bằng Pake được phân phối theo giấy phép tuỳ chọn, kể cả độc quyền; bản sửa của chính Pake vẫn theo GPLv3) | CLI biến bất kỳ trang web nào thành ứng dụng desktop nhẹ bằng một lệnh, dùng Rust Tauri trên WebView hệ thống. | Gói cài thường dưới 10 MB vì không kèm Chromium; hỗ trợ macOS, Windows, Linux; có build trực tuyến qua GitHub Actions và gói sẵn cho nhiều trang phổ biến | `pnpm install -g pake-cli` | Fork hoặc sản phẩm phái sinh không được dùng tên và logo Pake (TRADEMARK.md); ứng dụng desktop đồ hoạ là bản tải riêng từ pake.run |
| [`78/xiaozhi-esp32`](https://github.com/78/xiaozhi-esp32) | 33.378 | MIT (Copyright 2025 Shenzhen Xinzhi Future Technology Co., Ltd. và Project Contributors) | Firmware chatbot giọng nói AI XiaoZhi cho vi điều khiển ESP32, dùng mô hình lớn như Qwen/DeepSeek và điều khiển thiết bị qua giao thức MCP. | Hỗ trợ 138 thư mục bo mạch và 171 biến thể phát hành trên ESP32, ESP32-C3/C5/C6/S3/P4; đánh thức bằng giọng nói offline qua ESP-SR, truyền âm thanh Opus qua WebSocket hoặc MQTT + UDP; MCP phía thiết bị (loa, LED, servo, GPIO) và phía cloud, giao diện 39 ngôn ngữ | `Build bằng ESP-IDF v6.0.1+ (khuyến nghị release/v6.1) hoặc nạp firmware theo docs.xiaozhi.me/en/firmware/flashing.html` | Cần phần cứng ESP32; mặc định kết nối máy chủ chính thức xiaozhi.me (cần đăng ký tài khoản), có thể tự host bằng server mã nguồn mở của bên thứ ba |
| [`4ian/GDevelop`](https://github.com/4ian/GDevelop) | 29.018 | MIT cho Core, GDJS, newIDE và Extensions (LICENSE.md); tên và logo GDevelop là tài sản độc quyền của Florian Rival | Phần mềm làm game không cần code, mã nguồn mở, tạo game 2D, 3D và nhiều người chơi cho mobile, desktop và web bằng hệ thống sự kiện và behavior. | Engine GDJS viết bằng TypeScript, render bằng PixiJS và Three.js (WebGL); editor newIDE dùng React và Electron, Core gắn sang JavaScript qua WebAssembly; vật lý Box2D và Jolt Physics chạy WebAssembly trong Extensions | `Tải ứng dụng tại gdevelop.io; đóng góp mã theo newIDE/README.md` | Không được dùng tên/logo GDevelop (tài sản riêng của Florian Rival); dịch vụ online và hỗ trợ thương mại có trả phí |
| [`Tencent/ncnn`](https://github.com/Tencent/ncnn) | 24.062 | BSD 3-Clause (LICENSE.txt), trừ các thành phần bên thứ ba có giấy phép riêng liệt kê trong file | Framework suy luận mạng nơ-ron hiệu năng cao tối ưu cho mobile, nhúng và desktop, chạy trên CPU và GPU Vulkan. | Không phụ thuộc runtime bên thứ ba; có công cụ pnnx chuyển mô hình PyTorch và ONNX sang ncnn; có API C++, C và binding Python, được dùng trong QQ, Qzone, WeChat | `pip3 install pnnx (xuất mô hình), rồi dùng API C++ hoặc Python ncnn` | Tuân thủ thêm giấy phép của các thành phần bên thứ ba đi kèm |
| [`Unity-Technologies/ml-agents`](https://github.com/Unity-Technologies/ml-agents) | 19.884 | Apache License 2.0 (Copyright 2017 Unity Technologies); có file Third Party Notices.md | Bộ công cụ mã nguồn mở biến game và mô phỏng Unity thành môi trường huấn luyện tác tử thông minh (học tăng cường, học bắt chước). | Gồm package Unity com.unity.ml-agents và gói Python mlagents, mlagents-envs; có API Gym và PettingZoo cùng plugin trainer tùy biến; tài liệu chính thức trên docs.unity3d.com | `python -m pip install mlagents==1.1.0` | Cần Unity 6000.0 trở lên và Python 3.10.12 theo hướng dẫn cài đặt; Unity Editor theo điều khoản riêng của Unity; có analytics trong editor (xem tài liệu về quyền riêng tư) |
| [`microsoft/AirSim`](https://github.com/microsoft/AirSim) | 18.618 | MIT (Copyright Microsoft Corporation) | Trình mô phỏng drone, ô tô và phương tiện khác xây dựng trên Unreal Engine (có bản Unity thử nghiệm) phục vụ nghiên cứu AI cho phương tiện tự hành. | Hỗ trợ software-in-the-loop với PX4 và ArduPilot, hardware-in-loop với PX4; API qua RPC cho C++, Python, C# và Java để lấy ảnh, trạng thái và điều khiển phương tiện; chế độ Computer Vision lấy ảnh độ sâu, phân đoạn, pháp tuyến bề mặt | `Tải binary tại github.com/Microsoft/AirSim/releases hoặc build theo build_windows/build_linux/build_macos` | Cần Unreal Engine (theo điều khoản riêng của Epic) hoặc Unity; bản Unity mới ở mức thử nghiệm; macOS chỉ có hướng dẫn build, không có binary |
| [`alibaba/MNN`](https://github.com/alibaba/MNN) | 16.562 | Apache License 2.0 (LICENSE.txt) | Framework học sâu nhẹ và hiệu quả cho suy luận và huấn luyện trên thiết bị, kèm MNN-LLM chạy mô hình ngôn ngữ lớn và MNN-Diffusion chạy stable diffusion cục bộ. | Tích hợp trong hơn 30 ứng dụng của Alibaba như Taobao, Tmall, DingTalk; MNN 3.6.1 thêm backend Hexagon chạy trên DSP Qualcomm; có ứng dụng mẫu MNN Chat Android/iOS chạy LLM đa phương thức offline | `Build từ mã nguồn bằng CMake theo tài liệu mnn-docs.readthedocs.io` |  |
| [`carla-simulator/carla`](https://github.com/carla-simulator/carla) | 14.632 | MIT (Copyright 2024 Computer Vision Center, UAB) cho mã; tài sản số (asset) của CARLA theo CC-BY; Unreal Engine theo điều khoản riêng | Trình mô phỏng mã nguồn mở cho nghiên cứu lái xe tự động, hỗ trợ phát triển, huấn luyện và kiểm định hệ thống tự lái với cảm biến và điều kiện môi trường tùy biến. | Cung cấp tài sản số mở (bố cục đô thị, tòa nhà, xe) dùng tự do; có Python API và hệ sinh thái Scenario_Runner, ROS-bridge, leaderboard; nhánh ue58-dev dùng Unreal Engine 5.8 song song nhánh ue4-dev | `git clone -b ue58-dev https://github.com/carla-simulator/carla.git CarlaUE5 rồi build theo hướng dẫn Linux/Windows` | Cần liên kết tài khoản GitHub với Epic Games để truy cập fork Unreal Engine 5.8; yêu cầu Ubuntu 22.04/24.04 hoặc Windows 11, GPU NVIDIA RTX 3070 trở lên, 16 GB VRAM, 32 GB RAM; tài sản theo CC-BY cần ghi công |

### 6c.3 Dùng danh sách này thế nào

- Tìm theo nhóm hoặc mục kho trong file JSON (trường `group`, `kho_section`), rồi xem hồ sơ chi tiết nếu repo đã có trong catalog.
- Repo nhóm "Khác", "Tiện ích Windows & Hệ thống", "Tải & phát Video, Nhạc" nằm ngoài phạm vi kho nên chỉ giữ trong file dữ liệu.
- Mọi repo trong phạm vi kho đã có kết luận ở trường `review`: có hồ sơ (§6c.2, §6c.4, §6c.5) hoặc lý do chưa thêm; khi repo commit lại hoặc thêm giấy phép thì xét lại.
- Lọc lại 18/11/2026: hai repo thêm trước đó chưa đạt tiêu chí nhưng vẫn giữ hồ sơ, có ghi chú trong catalog: `karpathy/autoresearch` (commit cuối 25/3/2026, không có file LICENSE) và `multica-ai/andrej-karpathy-skills` (commit cuối 20/4/2026, API không nhận diện giấy phép).
- Liên quan: mục 20 §3zb (8 plugin, 8 kỹ năng, 8 MCP của cùng tác giả), mục 01 (coding agent), mục 02 (agent framework), mục 11 (trình duyệt cho agent).

**Nguồn §6c:** bảng người dùng dán từ https://phandonggiang.com/kho-repo ngày 18/11/2026 · GitHub search API cho từng repo 18/11/2026 · clone nông 24 repo, đọc README, LICENSE và cây thư mục (HEAD ghi trong `data/projects.json`).

<a id="anhkysuai-2026-11-23"></a>

## Đánh giá từ kho Anh Kỹ Sư AI — 23/11/2026

Phần này có **92 hồ sơ hoặc phạm vi đối chiếu** từ [nguồn tuyển chọn](https://anhkysuai.com/kho/). [Bảng đủ 1.295 repo](../data/collections/anhkysuai-kho.json) ghi trạng thái đối chiếu từng link; [danh sách URL](../data/collections/anhkysuai-kho-links.txt) phục vụ tra cứu. Nguồn tuyển chọn giúp phát hiện repo; đánh giá bên dưới dựa trên clone và permalink upstream cùng metadata GitHub ngày 2026-11-23.

Mức `docs-read`/`code-read` chỉ áp dụng phạm vi ghi tại mỗi hồ sơ. Chưa cài, build, chạy test hay benchmark mã upstream. Giấy phép có thể tách theo code, model, nội dung, asset hoặc bản enterprise; con số/tuyên bố của tác giả chưa được tái lập nếu không có ghi chú khác.

<a id="anhkysuai-2026-11-23-google-research"></a>

### Google Research code collection

**Repo:** [google-research/google-research](https://github.com/google-research/google-research) · **License:** Apache-2.0 cho mã; CC-BY-4.0 cho dữ liệu theo README · **★ 39,263 (GitHub API, 2026-11-23)**

**Mục đích:** Monorepo tập hợp mã nghiên cứu được Google Research công bố.

**Giá trị và cơ chế:** README xác định phạm vi giấy phép tách mã và dữ liệu, khuyến nghị lấy riêng thư mục quan tâm; là nguồn bài học thực nghiệm đa chủ đề.

**Giới hạn:** Không phải sản phẩm Google được hỗ trợ theo README. Đợt này chỉ đọc tài liệu root và cây thư mục, không kiểm từng nghiên cứu hoặc quyền checkpoint bên ngoài.

**Cách tham khảo/tích hợp:** Chọn đúng thư mục bài báo, ghim SHA và kiểm license/phụ thuộc tại phạm vi đó trước khi tái lập.

**Thay thế:** papers-with-code, [transformers](../08-awesome-lists-learning/README.md#6c513-mô-hình-ai--huấn-luyện), [pytorch](../08-awesome-lists-learning/README.md#6c513-mô-hình-ai--huấn-luyện).

**Bằng chứng:** `docs-read`, ngày 2026-11-23, commit [`87e25a5ba04d`](https://github.com/google-research/google-research/commit/87e25a5ba04d2c4cf0108f0cec96d648fe2b945a). README và các tài liệu/manifest/CI hiện diện, đọc chọn lọc; chưa kiểm implementation. Chưa cài/chạy upstream.

**Nguồn:** [README.md](https://github.com/google-research/google-research/blob/87e25a5ba04d2c4cf0108f0cec96d648fe2b945a/README.md) · [LICENSE](https://github.com/google-research/google-research/blob/87e25a5ba04d2c4cf0108f0cec96d648fe2b945a/LICENSE) · [metadata GitHub](https://api.github.com/repos/google-research/google-research).

<a id="anhkysuai-2026-11-23-learnopencv-examples"></a>

### LearnOpenCV Examples

**Repo:** [spmallick/learnopencv](https://github.com/spmallick/learnopencv) · **License:** Không có license chung được xác minh; từng ví dụ có điều khoản riêng · **★ 23,258 (GitHub API, 2026-11-23)**

**Mục đích:** Tìm bài học và mã ví dụ về thị giác máy tính, OpenCV và học sâu.

**Giá trị và cơ chế:** README là chỉ mục theo bài viết dẫn tới nhiều thư mục ví dụ; thuận tiện tìm một bài toán và xem tài nguyên đi kèm.

**Giới hạn:** Chỉ đọc tài liệu và license mẫu, chưa đánh giá toàn bộ ví dụ. LICENSE BSD-3-Clause trong Mask-RCNN không chứng minh quyền dùng toàn kho; môi trường và độ mới khác nhau theo bài.

**Cách tham khảo/tích hợp:** Chọn một ví dụ cụ thể rồi kiểm riêng mã, dependency, dữ liệu và license trước khi tái sử dụng.

**Thay thế:** [opencv](../08-awesome-lists-learning/README.md#6c525-tài-liệu-ocr--thị-giác-máy-tính), google-research, DeepLearningExamples.

**Bằng chứng:** `docs-read`, ngày 2026-11-23, commit [`c2c1b0d61a1c`](https://github.com/spmallick/learnopencv/commit/c2c1b0d61a1c9e18f9b2e2f0d50f40b257006fca). README và các tài liệu/manifest/CI hiện diện, đọc chọn lọc; chưa kiểm implementation. Chưa cài/chạy upstream.

**Nguồn:** [README.md](https://github.com/spmallick/learnopencv/blob/c2c1b0d61a1c9e18f9b2e2f0d50f40b257006fca/README.md) · [Mask-RCNN/LICENSE](https://github.com/spmallick/learnopencv/blob/c2c1b0d61a1c9e18f9b2e2f0d50f40b257006fca/Mask-RCNN/LICENSE) · [metadata GitHub](https://api.github.com/repos/spmallick/learnopencv).

<a id="anhkysuai-2026-11-23-gemini-fullstack-langgraph-quickstart"></a>

### Gemini Fullstack LangGraph Quickstart

**Repo:** [google-gemini/gemini-fullstack-langgraph-quickstart](https://github.com/google-gemini/gemini-fullstack-langgraph-quickstart) · **License:** Apache-2.0 · **★ 18,371 (GitHub API, 2026-11-23)**

**Mục đích:** Mẫu ứng dụng nghiên cứu web với React, LangGraph và Gemini.

**Giá trị và cơ chế:** Đã đọc graph: tạo truy vấn, tìm kiếm có grounding, chèn citation, phản chiếu khoảng trống kiến thức rồi lặp hoặc tổng hợp; giới hạn số vòng nằm trong configuration.

**Giới hạn:** Không thấy CI trong tree nên giữ docs-read dù đã đọc các node chính. Chưa gọi API hoặc kiểm nguồn trích dẫn; model mặc định tại snapshot có thể cần đổi khi triển khai.

**Cách tham khảo/tích hợp:** Dùng làm bài học graph và vòng phản hồi, cấu hình khóa/model cùng giới hạn chi phí, rồi đánh giá câu trả lời với tập câu hỏi có đáp án.

**Thay thế:** [gpt-researcher](../08-awesome-lists-learning/README.md#6c4-nhóm-ai-agent--mcp-so-sánh-chọn-16-repo-đọc-mã-18112026), Open Deep Research, [LangGraph](../02-agent-frameworks/README.md#core-framework-semantics).

**Bằng chứng:** `docs-read`, ngày 2026-11-23, commit [`e34e569de465`](https://github.com/google-gemini/gemini-fullstack-langgraph-quickstart/commit/e34e569de465340e42f36cd3cab4fac0c3ce7036). Đọc các node web research/reflection/finalize, điều kiện dừng và configuration; không thấy CI trong tree nên giữ docs-read, chưa gọi dịch vụ model. Chưa cài/chạy upstream.

**Nguồn:** [README.md](https://github.com/google-gemini/gemini-fullstack-langgraph-quickstart/blob/e34e569de465340e42f36cd3cab4fac0c3ce7036/README.md) · [LICENSE](https://github.com/google-gemini/gemini-fullstack-langgraph-quickstart/blob/e34e569de465340e42f36cd3cab4fac0c3ce7036/LICENSE) · [backend/src/agent/graph.py](https://github.com/google-gemini/gemini-fullstack-langgraph-quickstart/blob/e34e569de465340e42f36cd3cab4fac0c3ce7036/backend/src/agent/graph.py) · [backend/src/agent/configuration.py](https://github.com/google-gemini/gemini-fullstack-langgraph-quickstart/blob/e34e569de465340e42f36cd3cab4fac0c3ce7036/backend/src/agent/configuration.py) · [metadata GitHub](https://api.github.com/repos/google-gemini/gemini-fullstack-langgraph-quickstart).

<a id="anhkysuai-2026-11-23-awesome-claude-skills-travisvn"></a>

### Awesome Claude Skills (travisvn)

**Repo:** [travisvn/awesome-claude-skills](https://github.com/travisvn/awesome-claude-skills) · **License:** Chưa tìm thấy LICENSE tại snapshot · **★ 15,915 (GitHub API, 2026-11-23)**

**Mục đích:** Chỉ mục tài nguyên và bộ kỹ năng cộng đồng dành cho Claude và các quy trình liên quan.

**Giá trị và cơ chế:** README gom liên kết, mô tả cách dùng skills và tài nguyên tham khảo; thuận tiện khám phá một kỹ năng trước khi đọc nguồn gốc.

**Giới hạn:** Tree tại SHA chỉ có tài liệu và không có LICENSE. Danh sách không xác nhận tính an toàn, quyền tái sử dụng hay chất lượng từng kỹ năng; chưa cài hoặc chạy mục nào.

**Cách tham khảo/tích hợp:** Dùng như điểm tìm kiếm, theo từng liên kết để kiểm license, quyền công cụ và nội dung trước khi đưa vào môi trường làm việc.

**Thay thế:** [awesome-agent-skills](https://github.com/VoltAgent/awesome-agent-skills), [anthropics/skills](https://github.com/anthropics/skills), [Agency Agents 中文](../17-prompt-engineering/README.md#anhkysuai-2026-11-23-agency-agents-zh).

**Bằng chứng:** `docs-read`, ngày 2026-11-23, commit [`1da55aa810f2`](https://github.com/travisvn/awesome-claude-skills/commit/1da55aa810f206d3fe2005e7e3989b15a275d942). README và các tài liệu/manifest/CI hiện diện, đọc chọn lọc; chưa kiểm implementation. Chưa cài/chạy upstream.

**Nguồn:** [README.md](https://github.com/travisvn/awesome-claude-skills/blob/1da55aa810f206d3fe2005e7e3989b15a275d942/README.md) · [metadata GitHub](https://api.github.com/repos/travisvn/awesome-claude-skills).

<a id="anhkysuai-2026-11-23-asabeneh-30-days-of-python"></a>

### 30-Days-Of-Python

**Repo:** [Asabeneh/30-Days-Of-Python](https://github.com/Asabeneh/30-Days-Of-Python) · **License:** Chưa xác lập ở phạm vi đã đọc · **★ 79,356 (GitHub API, 2026-11-23)**

**Mục đích:** Lộ trình Python theo ngày, có giải thích cú pháp và bài tập tăng dần.

**Giá trị:** Phù hợp người mới cần một chuỗi bài thực hành liên tục; cấu trúc theo ngày và các bản dịch giúp chia nhỏ việc học.

**Giới hạn:** Không thấy giấy phép chung ở gốc cây đã đọc; mốc 30 ngày và tuyên bố chứng chỉ không chứng minh năng lực sau khóa. Chưa xác lập giấy phép chung cho nội dung chính ở phạm vi đã đọc; không suy quyền tái sử dụng từ repo công khai.

**Cách tham khảo/tích hợp:** Dẫn link bài gốc, chọn bài chuyển giao riêng để kiểm kiến thức; chưa nên đóng gói lại nội dung khi quyền tái sử dụng chưa rõ.

**Lựa chọn để đối chiếu:** [exercism/python](https://github.com/exercism/python) · [TheAlgorithms/Python](https://github.com/TheAlgorithms/Python). Đây là ứng viên so sánh theo tác vụ; mức phù hợp cần kiểm theo hồ sơ và phiên bản riêng.

**Bằng chứng:** `docs-read`, ngày 2026-11-23, commit [`50c11a80a6e3924a7be58c89f409697e12cb4d70`](https://github.com/Asabeneh/30-Days-Of-Python/commit/50c11a80a6e3924a7be58c89f409697e12cb4d70), ngày commit 2026-09-30. Đã clone và đọc chọn lọc phần giới thiệu, cách dùng, giới hạn, license, metadata manifest và CI hiện diện. Chưa kiểm đầy đủ implementation hoặc chạy upstream; các số đo của tác giả chưa được tái lập.

**Nguồn:** [readme.md](https://github.com/Asabeneh/30-Days-Of-Python/blob/50c11a80a6e3924a7be58c89f409697e12cb4d70/readme.md) · [metadata GitHub](https://api.github.com/repos/Asabeneh/30-Days-Of-Python).

<a id="anhkysuai-2026-11-23-byoungd-up"></a>

### up

**Repo:** [byoungd/up](https://github.com/byoungd/up) · **License:** CC BY-NC 4.0 (nội dung); MIT (mã) · **★ 70,840 (GitHub API, 2026-11-23)**

**Mục đích:** Sách mở song ngữ về tự học, dự án, nghề nghiệp và ứng dụng AI vào quá trình học.

**Giá trị:** Kết hợp chương đọc với worksheet và chu kỳ nhìn lại kết quả, phù hợp thiết kế lộ trình theo vấn đề thực tế.

**Giới hạn:** Nội dung CC BY-NC 4.0, mã cấu hình/site MIT; không được gắn MIT cho toàn bộ sách. Đây là trải nghiệm và hướng dẫn của tác giả, chưa phải hiệu quả học tập đã tái lập.

**Cách tham khảo/tích hợp:** Dẫn nguồn và chọn worksheet phù hợp; tách quyền sử dụng văn bản khỏi quyền của mã site.

**Lựa chọn để đối chiếu:** [charlax/professional-programming](https://github.com/charlax/professional-programming) · [MichaelCade/90DaysOfDevOps](https://github.com/MichaelCade/90DaysOfDevOps). Đây là ứng viên so sánh theo tác vụ; mức phù hợp cần kiểm theo hồ sơ và phiên bản riêng.

**Bằng chứng:** `docs-read`, ngày 2026-11-23, commit [`9f83b2503638b3c7ff6e3bb52f3992038b4b4978`](https://github.com/byoungd/up/commit/9f83b2503638b3c7ff6e3bb52f3992038b4b4978), ngày commit 2026-11-14. Đã clone và đọc chọn lọc phần giới thiệu, cách dùng, giới hạn, license, metadata manifest và CI hiện diện. Chưa kiểm đầy đủ implementation hoặc chạy upstream; các số đo của tác giả chưa được tái lập.

**Nguồn:** [README.md](https://github.com/byoungd/up/blob/9f83b2503638b3c7ff6e3bb52f3992038b4b4978/README.md) · [LICENSE-CODE.md](https://github.com/byoungd/up/blob/9f83b2503638b3c7ff6e3bb52f3992038b4b4978/LICENSE-CODE.md) · [LICENSE-CONTENT.md](https://github.com/byoungd/up/blob/9f83b2503638b3c7ff6e3bb52f3992038b4b4978/LICENSE-CONTENT.md) · [LICENSE.md](https://github.com/byoungd/up/blob/9f83b2503638b3c7ff6e3bb52f3992038b4b4978/LICENSE.md) · [package.json](https://github.com/byoungd/up/blob/9f83b2503638b3c7ff6e3bb52f3992038b4b4978/package.json) · [.github/workflows/ci.yml](https://github.com/byoungd/up/blob/9f83b2503638b3c7ff6e3bb52f3992038b4b4978/.github/workflows/ci.yml) · [metadata GitHub](https://api.github.com/repos/byoungd/up).

<a id="anhkysuai-2026-11-23-thealgorithms-java"></a>

### Java

**Repo:** [TheAlgorithms/Java](https://github.com/TheAlgorithms/Java) · **License:** MIT · **★ 67,311 (GitHub API, 2026-11-23)**

**Mục đích:** Tập hợp các thuật toán và cấu trúc dữ liệu triển khai bằng Java phục vụ học tập.

**Giá trị:** Thuận tiện đọc nhiều cách giải trong cùng hệ ngôn ngữ và đối chiếu với bài tập; repo có cấu hình Maven và workflow build.

**Giới hạn:** README nói rõ các bản triển khai dùng cho học và có thể kém hiệu quả hơn thư viện chuẩn; CI trong repo chưa được chạy lại trong đợt này.

**Cách tham khảo/tích hợp:** Dùng làm ví dụ để giải thích, viết test biên và so độ phức tạp; ưu tiên thư viện chuẩn khi xây sản phẩm.

**Lựa chọn để đối chiếu:** [TheAlgorithms/Python](https://github.com/TheAlgorithms/Python) · [TheAlgorithms/C-Plus-Plus](https://github.com/TheAlgorithms/C-Plus-Plus). Đây là ứng viên so sánh theo tác vụ; mức phù hợp cần kiểm theo hồ sơ và phiên bản riêng.

**Bằng chứng:** `docs-read`, ngày 2026-11-23, commit [`f4d6708297f86629a9e415070935b903ea8b1858`](https://github.com/TheAlgorithms/Java/commit/f4d6708297f86629a9e415070935b903ea8b1858), ngày commit 2026-11-20. Đã clone và đọc chọn lọc phần giới thiệu, cách dùng, giới hạn, license, metadata manifest và CI hiện diện. Chưa kiểm đầy đủ implementation hoặc chạy upstream; các số đo của tác giả chưa được tái lập.

**Nguồn:** [README.md](https://github.com/TheAlgorithms/Java/blob/f4d6708297f86629a9e415070935b903ea8b1858/README.md) · [LICENSE](https://github.com/TheAlgorithms/Java/blob/f4d6708297f86629a9e415070935b903ea8b1858/LICENSE) · [pom.xml](https://github.com/TheAlgorithms/Java/blob/f4d6708297f86629a9e415070935b903ea8b1858/pom.xml) · [.github/workflows/build.yml](https://github.com/TheAlgorithms/Java/blob/f4d6708297f86629a9e415070935b903ea8b1858/.github/workflows/build.yml) · [metadata GitHub](https://api.github.com/repos/TheAlgorithms/Java).

<a id="anhkysuai-2026-11-23-leonardomso-33-js-concepts"></a>

### 33-js-concepts

**Repo:** [leonardomso/33-js-concepts](https://github.com/leonardomso/33-js-concepts) · **License:** MIT · **★ 66,535 (GitHub API, 2026-11-23)**

**Mục đích:** Tài liệu các khái niệm JavaScript, từ kiểu dữ liệu và hàm đến bất đồng bộ, DOM và chủ đề mở rộng.

**Giá trị:** Phù hợp rà lỗ hổng kiến thức ngôn ngữ trước khi học framework; mỗi chủ đề dẫn giải thích và ví dụ.

**Giới hạn:** Tên 33 khái niệm không phản ánh toàn bộ phần mở rộng hiện có; danh sách tài nguyên không thay bài kiểm khả năng tự giải vấn đề.

**Cách tham khảo/tích hợp:** Chọn chủ đề yếu và viết ví dụ/test riêng; dùng như tài liệu học, không như bộ khung ứng dụng.

**Lựa chọn để đối chiếu:** [javascript-tutorial/en.javascript.info](https://github.com/javascript-tutorial/en.javascript.info) · [Asabeneh/30-Days-Of-JavaScript](https://github.com/Asabeneh/30-Days-Of-JavaScript). Đây là ứng viên so sánh theo tác vụ; mức phù hợp cần kiểm theo hồ sơ và phiên bản riêng.

**Bằng chứng:** `docs-read`, ngày 2026-11-23, commit [`16d0d95c02b19df6a8c841f1a0012d7b7367a340`](https://github.com/leonardomso/33-js-concepts/commit/16d0d95c02b19df6a8c841f1a0012d7b7367a340), ngày commit 2026-06-06. Đã clone và đọc chọn lọc phần giới thiệu, cách dùng, giới hạn, license, metadata manifest và CI hiện diện. Chưa kiểm đầy đủ implementation hoặc chạy upstream; các số đo của tác giả chưa được tái lập.

**Nguồn:** [README.md](https://github.com/leonardomso/33-js-concepts/blob/16d0d95c02b19df6a8c841f1a0012d7b7367a340/README.md) · [LICENSE](https://github.com/leonardomso/33-js-concepts/blob/16d0d95c02b19df6a8c841f1a0012d7b7367a340/LICENSE) · [package.json](https://github.com/leonardomso/33-js-concepts/blob/16d0d95c02b19df6a8c841f1a0012d7b7367a340/package.json) · [.github/workflows/tests.yml](https://github.com/leonardomso/33-js-concepts/blob/16d0d95c02b19df6a8c841f1a0012d7b7367a340/.github/workflows/tests.yml) · [metadata GitHub](https://api.github.com/repos/leonardomso/33-js-concepts).

<a id="anhkysuai-2026-11-23-rust-lang-rustlings"></a>

### rustlings

**Repo:** [rust-lang/rustlings](https://github.com/rust-lang/rustlings) · **License:** MIT · **★ 64,770 (GitHub API, 2026-11-23)**

**Mục đích:** Bộ bài tập nhỏ để luyện đọc và viết Rust, được giới thiệu dùng cùng Rust Book.

**Giá trị:** Chia việc học thành các bài sửa lỗi và hoàn thiện mã; repo có Cargo manifest và workflow Rust để đối chiếu cách tổ chức bài tập.

**Giới hạn:** Hoàn thành bài nhỏ chưa chứng minh khả năng thiết kế hệ thống hay vận hành ứng dụng Rust; chưa chạy bộ bài trong đợt này.

**Cách tham khảo/tích hợp:** Chọn bài theo năng lực đầu vào và bổ sung bài chuyển giao mới sau mỗi nhóm chủ đề.

**Lựa chọn để đối chiếu:** [google/comprehensive-rust](https://github.com/google/comprehensive-rust) · [exercism/python](https://github.com/exercism/python). Đây là ứng viên so sánh theo tác vụ; mức phù hợp cần kiểm theo hồ sơ và phiên bản riêng.

**Bằng chứng:** `docs-read`, ngày 2026-11-23, commit [`f7b9b3c5882a1a43275130b95142d94f847526f5`](https://github.com/rust-lang/rustlings/commit/f7b9b3c5882a1a43275130b95142d94f847526f5), ngày commit 2026-10-26. Đã clone và đọc chọn lọc phần giới thiệu, cách dùng, giới hạn, license, metadata manifest và CI hiện diện. Chưa kiểm đầy đủ implementation hoặc chạy upstream; các số đo của tác giả chưa được tái lập.

**Nguồn:** [README.md](https://github.com/rust-lang/rustlings/blob/f7b9b3c5882a1a43275130b95142d94f847526f5/README.md) · [LICENSE](https://github.com/rust-lang/rustlings/blob/f7b9b3c5882a1a43275130b95142d94f847526f5/LICENSE) · [Cargo.toml](https://github.com/rust-lang/rustlings/blob/f7b9b3c5882a1a43275130b95142d94f847526f5/Cargo.toml) · [.github/workflows/rust.yml](https://github.com/rust-lang/rustlings/blob/f7b9b3c5882a1a43275130b95142d94f847526f5/.github/workflows/rust.yml) · [metadata GitHub](https://api.github.com/repos/rust-lang/rustlings).

<a id="anhkysuai-2026-11-23-tldr-pages-tldr"></a>

### tldr

**Repo:** [tldr-pages/tldr](https://github.com/tldr-pages/tldr) · **License:** CC-BY-4.0 (nội dung); MIT (scripts) · **★ 64,283 (GitHub API, 2026-11-23)**

**Mục đích:** Kho ví dụ ngắn cho các lệnh dòng lệnh, dùng qua nhiều client độc lập.

**Giá trị:** Tổ chức theo lệnh và tình huống sử dụng giúp tra nhanh hơn tài liệu tham số đầy đủ; phù hợp tham khảo cách viết trợ giúp CLI.

**Giới hạn:** Ví dụ lệnh có thể thay đổi hoặc tác động dữ liệu; giấy phép nội dung khác mã tiện ích của kho và không thay quyền của các lệnh được giới thiệu.

**Cách tham khảo/tích hợp:** Tra ví dụ rồi đối chiếu man page của phiên bản thực tế; chỉ chạy sau khi hiểu tham số và phạm vi dữ liệu.

**Lựa chọn để đối chiếu:** [LeCoupa/awesome-cheatsheets](https://github.com/LeCoupa/awesome-cheatsheets) · [cheat/cheat](https://github.com/cheat/cheat). Đây là ứng viên so sánh theo tác vụ; mức phù hợp cần kiểm theo hồ sơ và phiên bản riêng.

**Bằng chứng:** `docs-read`, ngày 2026-11-23, commit [`801e81e66c3ad6e879cfe40a214dc973e24ad983`](https://github.com/tldr-pages/tldr/commit/801e81e66c3ad6e879cfe40a214dc973e24ad983), ngày commit 2026-11-23. Đã clone và đọc chọn lọc phần giới thiệu, cách dùng, giới hạn, license, metadata manifest và CI hiện diện. Chưa kiểm đầy đủ implementation hoặc chạy upstream; các số đo của tác giả chưa được tái lập.

**Nguồn:** [README.md](https://github.com/tldr-pages/tldr/blob/801e81e66c3ad6e879cfe40a214dc973e24ad983/README.md) · [LICENSE.md](https://github.com/tldr-pages/tldr/blob/801e81e66c3ad6e879cfe40a214dc973e24ad983/LICENSE.md) · [package.json](https://github.com/tldr-pages/tldr/blob/801e81e66c3ad6e879cfe40a214dc973e24ad983/package.json) · [.github/workflows/ci.yml](https://github.com/tldr-pages/tldr/blob/801e81e66c3ad6e879cfe40a214dc973e24ad983/.github/workflows/ci.yml) · [metadata GitHub](https://api.github.com/repos/tldr-pages/tldr).

<a id="anhkysuai-2026-11-23-youngyangyang04-leetcode-master"></a>

### leetcode-master

**Repo:** [youngyangyang04/leetcode-master](https://github.com/youngyangyang04/leetcode-master) · **License:** Chưa xác lập ở phạm vi đã đọc · **★ 62,844 (GitHub API, 2026-11-23)**

**Mục đích:** Lộ trình bài thuật toán bằng tiếng Trung với giải thích, hình minh họa và nhiều bản triển khai ngôn ngữ.

**Giá trị:** Có thứ tự luyện bài và liên kết chủ đề, hữu ích để chọn bài theo kỹ thuật giải thay vì làm ngẫu nhiên.

**Giới hạn:** Cây gốc chưa cho thấy giấy phép chung; có liên kết sách và dịch vụ học. Nội dung lời giải không phải thước đo độc lập năng lực phỏng vấn. Chưa xác lập giấy phép chung cho nội dung chính ở phạm vi đã đọc; không suy quyền tái sử dụng từ repo công khai.

**Cách tham khảo/tích hợp:** Dẫn bài gốc, tự viết lời giải trước khi đọc đáp án và kiểm bài biến thể; không sao chép nội dung dài khi chưa rõ quyền.

**Lựa chọn để đối chiếu:** [azl397985856/leetcode](https://github.com/azl397985856/leetcode) · [halfrost/LeetCode-Go](https://github.com/halfrost/LeetCode-Go). Đây là ứng viên so sánh theo tác vụ; mức phù hợp cần kiểm theo hồ sơ và phiên bản riêng.

**Bằng chứng:** `docs-read`, ngày 2026-11-23, commit [`6fe1571732d41e8f425f8e702992adf7ffae95a0`](https://github.com/youngyangyang04/leetcode-master/commit/6fe1571732d41e8f425f8e702992adf7ffae95a0), ngày commit 2026-10-24. Đã clone và đọc chọn lọc phần giới thiệu, cách dùng, giới hạn, license, metadata manifest và CI hiện diện. Chưa kiểm đầy đủ implementation hoặc chạy upstream; các số đo của tác giả chưa được tái lập.

**Nguồn:** [README.md](https://github.com/youngyangyang04/leetcode-master/blob/6fe1571732d41e8f425f8e702992adf7ffae95a0/README.md) · [metadata GitHub](https://api.github.com/repos/youngyangyang04/leetcode-master).

<a id="anhkysuai-2026-11-23-solido-awesome-flutter"></a>

### awesome-flutter

**Repo:** [Solido/awesome-flutter](https://github.com/Solido/awesome-flutter) · **License:** CC0-1.0 (tuyên bố trong README) · **★ 62,009 (GitHub API, 2026-11-23)**

**Mục đích:** Danh sách tuyển chọn thư viện, công cụ và bài học cho Flutter.

**Giá trị:** Phân loại thành phần UI, đồ họa và các mức bài học, hữu ích để tạo danh sách ứng viên theo tác vụ.

**Giới hạn:** Có nội dung tài trợ; việc được liệt kê không xác nhận tương thích hay bảo trì. Giấy phép danh sách không đại diện các package được dẫn.

**Cách tham khảo/tích hợp:** Mở repo gốc của từng package, kiểm phiên bản Flutter và license trước khi chọn.

**Lựa chọn để đối chiếu:** [jondot/awesome-react-native](https://github.com/jondot/awesome-react-native) · [wasabeef/awesome-android-ui](https://github.com/wasabeef/awesome-android-ui). Đây là ứng viên so sánh theo tác vụ; mức phù hợp cần kiểm theo hồ sơ và phiên bản riêng.

**Bằng chứng:** `docs-read`, ngày 2026-11-23, commit [`7d43415ee0f9e446ec20795daebf4b8f3926f1d3`](https://github.com/Solido/awesome-flutter/commit/7d43415ee0f9e446ec20795daebf4b8f3926f1d3), ngày commit 2026-09-03. Đã clone và đọc chọn lọc phần giới thiệu, cách dùng, giới hạn, license, metadata manifest và CI hiện diện. Chưa kiểm đầy đủ implementation hoặc chạy upstream; các số đo của tác giả chưa được tái lập.

**Nguồn:** [README.md](https://github.com/Solido/awesome-flutter/blob/7d43415ee0f9e446ec20795daebf4b8f3926f1d3/README.md) · [metadata GitHub](https://api.github.com/repos/Solido/awesome-flutter).

<a id="anhkysuai-2026-11-23-rust-unofficial-awesome-rust"></a>

### awesome-rust

**Repo:** [rust-unofficial/awesome-rust](https://github.com/rust-unofficial/awesome-rust) · **License:** CC0-1.0 · **★ 60,746 (GitHub API, 2026-11-23)**

**Mục đích:** Danh sách ứng dụng, crate và tài nguyên học tập của hệ sinh thái Rust.

**Giá trị:** Phân theo bài toán từ hệ thống, dữ liệu đến đồ họa, giúp phát hiện ứng viên thay vì chỉ tìm theo tên crate.

**Giới hạn:** Danh sách CC0 không cấp lại giấy phép của từng crate; nhãn tuyển chọn không bảo đảm API hay khả năng bảo trì.

**Cách tham khảo/tích hợp:** Dùng như chỉ mục rồi đọc tài liệu và CI của crate đích ở phiên bản định tích hợp.

**Lựa chọn để đối chiếu:** [akullpp/awesome-java](https://github.com/akullpp/awesome-java) · [ziadoz/awesome-php](https://github.com/ziadoz/awesome-php). Đây là ứng viên so sánh theo tác vụ; mức phù hợp cần kiểm theo hồ sơ và phiên bản riêng.

**Bằng chứng:** `docs-read`, ngày 2026-11-23, commit [`c45fd68e40b99cd29a679941ac09046006240cdc`](https://github.com/rust-unofficial/awesome-rust/commit/c45fd68e40b99cd29a679941ac09046006240cdc), ngày commit 2026-11-23. Đã clone và đọc chọn lọc phần giới thiệu, cách dùng, giới hạn, license, metadata manifest và CI hiện diện. Chưa kiểm đầy đủ implementation hoặc chạy upstream; các số đo của tác giả chưa được tái lập.

**Nguồn:** [README.md](https://github.com/rust-unofficial/awesome-rust/blob/c45fd68e40b99cd29a679941ac09046006240cdc/README.md) · [LICENSE.txt](https://github.com/rust-unofficial/awesome-rust/blob/c45fd68e40b99cd29a679941ac09046006240cdc/LICENSE.txt) · [Cargo.toml](https://github.com/rust-unofficial/awesome-rust/blob/c45fd68e40b99cd29a679941ac09046006240cdc/Cargo.toml) · [.github/workflows/lint.yml](https://github.com/rust-unofficial/awesome-rust/blob/c45fd68e40b99cd29a679941ac09046006240cdc/.github/workflows/lint.yml) · [metadata GitHub](https://api.github.com/repos/rust-unofficial/awesome-rust).

<a id="anhkysuai-2026-11-23-wasabeef-awesome-android-ui"></a>

### awesome-android-ui

**Repo:** [wasabeef/awesome-android-ui](https://github.com/wasabeef/awesome-android-ui) · **License:** MIT · **★ 58,634 (GitHub API, 2026-11-23)**

**Mục đích:** Danh sách thư viện UI/UX Android kèm ví dụ hình ảnh và nhãn giấy phép.

**Giá trị:** Tra cứu bằng loại thành phần giúp chọn ứng viên UI nhanh; phần hình ảnh hỗ trợ so hành vi mong muốn.

**Giới hạn:** Ảnh demo và nhãn license trong danh sách là dữ kiện thứ cấp; cần kiểm tương thích Android/Compose và điều kiện của từng thư viện.

**Cách tham khảo/tích hợp:** Chọn vài thành phần rồi kiểm trên thiết bị, accessibility và vòng đời màn hình của ứng dụng đích.

**Lựa chọn để đối chiếu:** [Solido/awesome-flutter](https://github.com/Solido/awesome-flutter) · [vsouza/awesome-ios](https://github.com/vsouza/awesome-ios). Đây là ứng viên so sánh theo tác vụ; mức phù hợp cần kiểm theo hồ sơ và phiên bản riêng.

**Bằng chứng:** `docs-read`, ngày 2026-11-23, commit [`312f9be3c50b3ea33ff3ba7eb9aa1c21b52de8b2`](https://github.com/wasabeef/awesome-android-ui/commit/312f9be3c50b3ea33ff3ba7eb9aa1c21b52de8b2), ngày commit 2026-06-05. Đã clone và đọc chọn lọc phần giới thiệu, cách dùng, giới hạn, license, metadata manifest và CI hiện diện. Chưa kiểm đầy đủ implementation hoặc chạy upstream; các số đo của tác giả chưa được tái lập.

**Nguồn:** [README.md](https://github.com/wasabeef/awesome-android-ui/blob/312f9be3c50b3ea33ff3ba7eb9aa1c21b52de8b2/README.md) · [LICENSE](https://github.com/wasabeef/awesome-android-ui/blob/312f9be3c50b3ea33ff3ba7eb9aa1c21b52de8b2/LICENSE) · [metadata GitHub](https://api.github.com/repos/wasabeef/awesome-android-ui).

<a id="anhkysuai-2026-11-23-firstcontributions-first-contributions"></a>

### first-contributions

**Repo:** [firstcontributions/first-contributions](https://github.com/firstcontributions/first-contributions) · **License:** MIT · **★ 56,976 (GitHub API, 2026-11-23)**

**Mục đích:** Bài thực hành hướng dẫn người mới đi qua fork, clone, tạo nhánh, commit và pull request.

**Giá trị:** Tách quy trình đóng góp thành những thao tác nhỏ, có tài liệu bằng nhiều ngôn ngữ và hướng dẫn GUI.

**Giới hạn:** PR đổi một tên trong danh sách chỉ luyện thao tác Git; không thay bài tập đọc code, viết test hay xử lý review kỹ thuật.

**Cách tham khảo/tích hợp:** Dùng để làm quen workflow, sau đó chuyển sang một lỗi nhỏ có test và tiêu chí nghiệm thu.

**Lựa chọn để đối chiếu:** [github/opensource.guide](https://github.com/github/opensource.guide) · [charlax/professional-programming](https://github.com/charlax/professional-programming). Đây là ứng viên so sánh theo tác vụ; mức phù hợp cần kiểm theo hồ sơ và phiên bản riêng.

**Bằng chứng:** `docs-read`, ngày 2026-11-23, commit [`85f68cdb811f0c9b7cb7113e8393c73acfb522af`](https://github.com/firstcontributions/first-contributions/commit/85f68cdb811f0c9b7cb7113e8393c73acfb522af), ngày commit 2026-11-23. Đã clone và đọc chọn lọc phần giới thiệu, cách dùng, giới hạn, license, metadata manifest và CI hiện diện. Chưa kiểm đầy đủ implementation hoặc chạy upstream; các số đo của tác giả chưa được tái lập.

**Nguồn:** [README.md](https://github.com/firstcontributions/first-contributions/blob/85f68cdb811f0c9b7cb7113e8393c73acfb522af/README.md) · [LICENSE](https://github.com/firstcontributions/first-contributions/blob/85f68cdb811f0c9b7cb7113e8393c73acfb522af/LICENSE) · [.github/workflows/auto-pr-merge.yml](https://github.com/firstcontributions/first-contributions/blob/85f68cdb811f0c9b7cb7113e8393c73acfb522af/.github/workflows/auto-pr-merge.yml) · [metadata GitHub](https://api.github.com/repos/firstcontributions/first-contributions).

<a id="anhkysuai-2026-11-23-azl397985856-leetcode"></a>

### leetcode

**Repo:** [azl397985856/leetcode](https://github.com/azl397985856/leetcode) · **License:** CC-BY-NC-ND-4.0 · **★ 55,703 (GitHub API, 2026-11-23)**

**Mục đích:** Kho lời giải và ghi chép thuật toán LeetCode, có lộ trình và phân nhóm kiến thức.

**Giá trị:** Hữu ích để đối chiếu nhiều kỹ thuật giải và giải thích sau khi tự làm bài.

**Giới hạn:** README nói đây là kho lưu trữ lời giải giai đoạn 2020–2021 và tác giả đã chuyển trọng tâm; commit mới không đồng nghĩa toàn bộ bài đã được rà lại.

**Cách tham khảo/tích hợp:** Kiểm đề bài và runtime hiện tại, bổ sung test biến thể; đọc giấy phép Creative Commons cụ thể trước khi tái phân phối.

**Lựa chọn để đối chiếu:** [youngyangyang04/leetcode-master](https://github.com/youngyangyang04/leetcode-master) · [TheAlgorithms/Java](https://github.com/TheAlgorithms/Java). Đây là ứng viên so sánh theo tác vụ; mức phù hợp cần kiểm theo hồ sơ và phiên bản riêng.

**Bằng chứng:** `docs-read`, ngày 2026-11-23, commit [`b2365578d556be14ec9786c82b21134b1a3b7655`](https://github.com/azl397985856/leetcode/commit/b2365578d556be14ec9786c82b21134b1a3b7655), ngày commit 2026-11-15. Đã clone và đọc chọn lọc phần giới thiệu, cách dùng, giới hạn, license, metadata manifest và CI hiện diện. Chưa kiểm đầy đủ implementation hoặc chạy upstream; các số đo của tác giả chưa được tái lập.

**Nguồn:** [README.md](https://github.com/azl397985856/leetcode/blob/b2365578d556be14ec9786c82b21134b1a3b7655/README.md) · [LICENSE.txt](https://github.com/azl397985856/leetcode/blob/b2365578d556be14ec9786c82b21134b1a3b7655/LICENSE.txt) · [package.json](https://github.com/azl397985856/leetcode/blob/b2365578d556be14ec9786c82b21134b1a3b7655/package.json) · [.github/workflows/ci.yml](https://github.com/azl397985856/leetcode/blob/b2365578d556be14ec9786c82b21134b1a3b7655/.github/workflows/ci.yml) · [metadata GitHub](https://api.github.com/repos/azl397985856/leetcode).

<a id="anhkysuai-2026-11-23-vsouza-awesome-ios"></a>

### awesome-ios

**Repo:** [vsouza/awesome-ios](https://github.com/vsouza/awesome-ios) · **License:** MIT · **★ 54,087 (GitHub API, 2026-11-23)**

**Mục đích:** Danh sách tài nguyên và thư viện iOS, Objective-C và Swift theo loại chức năng.

**Giá trị:** Có các nhóm kiến trúc, kiểm chất lượng, dữ liệu và giao diện, phù hợp tìm công cụ cho một yêu cầu cụ thể.

**Giới hạn:** Repo danh sách dùng MIT nhưng các dự án liên kết giữ license riêng; danh sách rộng chứa nhiều thế hệ API.

**Cách tham khảo/tích hợp:** Đối chiếu phiên bản iOS/Swift, trạng thái upstream và license của từng thư viện trước khi thử.

**Lựa chọn để đối chiếu:** [dkhamsing/open-source-ios-apps](https://github.com/dkhamsing/open-source-ios-apps) · [matteocrippa/awesome-swift](https://github.com/matteocrippa/awesome-swift). Đây là ứng viên so sánh theo tác vụ; mức phù hợp cần kiểm theo hồ sơ và phiên bản riêng.

**Bằng chứng:** `docs-read`, ngày 2026-11-23, commit [`630ca87d5f93373c8098d42c8dc780e79eb44d12`](https://github.com/vsouza/awesome-ios/commit/630ca87d5f93373c8098d42c8dc780e79eb44d12), ngày commit 2026-08-27. Đã clone và đọc chọn lọc phần giới thiệu, cách dùng, giới hạn, license, metadata manifest và CI hiện diện. Chưa kiểm đầy đủ implementation hoặc chạy upstream; các số đo của tác giả chưa được tái lập.

**Nguồn:** [README.md](https://github.com/vsouza/awesome-ios/blob/630ca87d5f93373c8098d42c8dc780e79eb44d12/README.md) · [LICENSE](https://github.com/vsouza/awesome-ios/blob/630ca87d5f93373c8098d42c8dc780e79eb44d12/LICENSE) · [.github/workflows/quality-check.yml](https://github.com/vsouza/awesome-ios/blob/630ca87d5f93373c8098d42c8dc780e79eb44d12/.github/workflows/quality-check.yml) · [metadata GitHub](https://api.github.com/repos/vsouza/awesome-ios).

<a id="anhkysuai-2026-11-23-dkhamsing-open-source-ios-apps"></a>

### open-source-ios-apps

**Repo:** [dkhamsing/open-source-ios-apps](https://github.com/dkhamsing/open-source-ios-apps) · **License:** CC0-1.0 · **★ 53,439 (GitHub API, 2026-11-23)**

**Mục đích:** Danh sách ứng dụng nguồn mở cho các nền tảng Apple, sinh README từ dữ liệu cấu trúc.

**Giá trị:** contents.json là nguồn dữ liệu chính theo README, thuận tiện tham khảo cách tách catalog máy đọc được khỏi trang trình bày.

**Giới hạn:** CC0 của danh sách không áp cho mã và tài sản của ứng dụng được dẫn; có mục lưu trữ và ứng dụng cũ.

**Cách tham khảo/tích hợp:** Dùng catalog để tìm ứng dụng mẫu rồi đánh giá license, SDK và khả năng build tại repo gốc.

**Lựa chọn để đối chiếu:** [serhii-londar/open-source-mac-os-apps](https://github.com/serhii-londar/open-source-mac-os-apps) · [vsouza/awesome-ios](https://github.com/vsouza/awesome-ios). Đây là ứng viên so sánh theo tác vụ; mức phù hợp cần kiểm theo hồ sơ và phiên bản riêng.

**Bằng chứng:** `docs-read`, ngày 2026-11-23, commit [`061610415072c3f3d04a4b0f90519766640b390f`](https://github.com/dkhamsing/open-source-ios-apps/commit/061610415072c3f3d04a4b0f90519766640b390f), ngày commit 2026-11-22. Đã clone và đọc chọn lọc phần giới thiệu, cách dùng, giới hạn, license, metadata manifest và CI hiện diện. Chưa kiểm đầy đủ implementation hoặc chạy upstream; các số đo của tác giả chưa được tái lập.

**Nguồn:** [README.md](https://github.com/dkhamsing/open-source-ios-apps/blob/061610415072c3f3d04a4b0f90519766640b390f/README.md) · [LICENSE](https://github.com/dkhamsing/open-source-ios-apps/blob/061610415072c3f3d04a4b0f90519766640b390f/LICENSE) · [.github/workflows/ruby.yml](https://github.com/dkhamsing/open-source-ios-apps/blob/061610415072c3f3d04a4b0f90519766640b390f/.github/workflows/ruby.yml) · [metadata GitHub](https://api.github.com/repos/dkhamsing/open-source-ios-apps).

<a id="anhkysuai-2026-11-23-charlax-professional-programming"></a>

### professional-programming

**Repo:** [charlax/professional-programming](https://github.com/charlax/professional-programming) · **License:** MIT · **★ 51,693 (GitHub API, 2026-11-23)**

**Mục đích:** Bộ tài nguyên đọc cho kỹ sư phần mềm về thiết kế, lập trình, vận hành và cách làm việc.

**Giá trị:** Danh sách theo chủ đề và có phần nguyên tắc chọn tài liệu, phù hợp xây tuyến đọc theo vai trò.

**Giới hạn:** Tác giả nói danh sách không toàn diện và không đồng tình với mọi nhận định trong tài liệu liên kết; việc đọc không chứng minh năng lực thực hành.

**Cách tham khảo/tích hợp:** Chọn ít tài liệu quanh một vấn đề, ghi quyết định áp dụng và kiểm qua một nhiệm vụ thực tế.

**Lựa chọn để đối chiếu:** [karanpratapsingh/system-design](https://github.com/karanpratapsingh/system-design) · [MichaelCade/90DaysOfDevOps](https://github.com/MichaelCade/90DaysOfDevOps). Đây là ứng viên so sánh theo tác vụ; mức phù hợp cần kiểm theo hồ sơ và phiên bản riêng.

**Bằng chứng:** `docs-read`, ngày 2026-11-23, commit [`30da020f25210357175593977f044110e1150baf`](https://github.com/charlax/professional-programming/commit/30da020f25210357175593977f044110e1150baf), ngày commit 2026-11-20. Đã clone và đọc chọn lọc phần giới thiệu, cách dùng, giới hạn, license, metadata manifest và CI hiện diện. Chưa kiểm đầy đủ implementation hoặc chạy upstream; các số đo của tác giả chưa được tái lập.

**Nguồn:** [README.md](https://github.com/charlax/professional-programming/blob/30da020f25210357175593977f044110e1150baf/README.md) · [LICENSE](https://github.com/charlax/professional-programming/blob/30da020f25210357175593977f044110e1150baf/LICENSE) · [metadata GitHub](https://api.github.com/repos/charlax/professional-programming).

<a id="anhkysuai-2026-11-23-serhii-londar-open-source-mac-os-apps"></a>

### open-source-mac-os-apps

**Repo:** [serhii-londar/open-source-mac-os-apps](https://github.com/serhii-londar/open-source-mac-os-apps) · **License:** CC0-1.0 · **★ 51,516 (GitHub API, 2026-11-23)**

**Mục đích:** Danh sách ứng dụng macOS theo nhóm công việc, có dữ liệu JSON đi cùng README.

**Giá trị:** Bao gồm ứng dụng native và đa nền tảng, hữu ích tìm sản phẩm tham chiếu và mô hình UX desktop.

**Giới hạn:** CC0 chỉ áp dụng cho danh sách; mức hỗ trợ phiên bản macOS, ký ứng dụng và license của mỗi sản phẩm phải kiểm riêng.

**Cách tham khảo/tích hợp:** Lọc ứng viên từ applications.json rồi kiểm nguồn phát hành và yêu cầu hệ điều hành của từng app.

**Lựa chọn để đối chiếu:** [jaywcjlove/awesome-mac](https://github.com/jaywcjlove/awesome-mac) · [dkhamsing/open-source-ios-apps](https://github.com/dkhamsing/open-source-ios-apps). Đây là ứng viên so sánh theo tác vụ; mức phù hợp cần kiểm theo hồ sơ và phiên bản riêng.

**Bằng chứng:** `docs-read`, ngày 2026-11-23, commit [`4b5a56315b886ac8fff3f997665913b393f4edca`](https://github.com/serhii-londar/open-source-mac-os-apps/commit/4b5a56315b886ac8fff3f997665913b393f4edca), ngày commit 2026-11-23. Đã clone và đọc chọn lọc phần giới thiệu, cách dùng, giới hạn, license, metadata manifest và CI hiện diện. Chưa kiểm đầy đủ implementation hoặc chạy upstream; các số đo của tác giả chưa được tái lập.

**Nguồn:** [README.md](https://github.com/serhii-londar/open-source-mac-os-apps/blob/4b5a56315b886ac8fff3f997665913b393f4edca/README.md) · [LICENSE](https://github.com/serhii-londar/open-source-mac-os-apps/blob/4b5a56315b886ac8fff3f997665913b393f4edca/LICENSE) · [.github/workflows/pr.yml](https://github.com/serhii-londar/open-source-mac-os-apps/blob/4b5a56315b886ac8fff3f997665913b393f4edca/.github/workflows/pr.yml) · [metadata GitHub](https://api.github.com/repos/serhii-londar/open-source-mac-os-apps).

<a id="anhkysuai-2026-11-23-akullpp-awesome-java"></a>

### awesome-java

**Repo:** [akullpp/awesome-java](https://github.com/akullpp/awesome-java) · **License:** CC BY-SA 4.0 (nội dung); MIT (mã) · **★ 49,614 (GitHub API, 2026-11-23)**

**Mục đích:** Danh sách thư viện, framework và công cụ Java theo bài toán.

**Giá trị:** Có nhóm so tương thích API, kiểm thử, CLI và hạ tầng; dữ liệu giúp tìm ứng viên theo vai trò trong stack.

**Giới hạn:** Nội dung danh sách CC BY-SA 4.0 nhưng mã cập nhật README dùng MIT; số sao và trạng thái trong danh sách không thay kiểm upstream.

**Cách tham khảo/tích hợp:** Dùng làm chỉ mục tìm ứng viên, dẫn về nguồn gốc rồi kiểm phiên bản, giấy phép và mức bảo trì của từng lựa chọn trước tích hợp.

**Lựa chọn để đối chiếu:** [rust-unofficial/awesome-rust](https://github.com/rust-unofficial/awesome-rust) · [ziadoz/awesome-php](https://github.com/ziadoz/awesome-php). Đây là ứng viên so sánh theo tác vụ; mức phù hợp cần kiểm theo hồ sơ và phiên bản riêng.

**Bằng chứng:** `docs-read`, ngày 2026-11-23, commit [`46bce2a6da3f11dc35bcc68dbf9473b2dc4f8ee0`](https://github.com/akullpp/awesome-java/commit/46bce2a6da3f11dc35bcc68dbf9473b2dc4f8ee0), ngày commit 2026-09-23. Đã clone và đọc chọn lọc phần giới thiệu, cách dùng, giới hạn, license, metadata manifest và CI hiện diện. Chưa kiểm đầy đủ implementation hoặc chạy upstream; các số đo của tác giả chưa được tái lập.

**Nguồn:** [README.md](https://github.com/akullpp/awesome-java/blob/46bce2a6da3f11dc35bcc68dbf9473b2dc4f8ee0/README.md) · [LICENSE](https://github.com/akullpp/awesome-java/blob/46bce2a6da3f11dc35bcc68dbf9473b2dc4f8ee0/LICENSE) · [LICENSE-CODE](https://github.com/akullpp/awesome-java/blob/46bce2a6da3f11dc35bcc68dbf9473b2dc4f8ee0/LICENSE-CODE) · [.github/workflows/update-readme.yml](https://github.com/akullpp/awesome-java/blob/46bce2a6da3f11dc35bcc68dbf9473b2dc4f8ee0/.github/workflows/update-readme.yml) · [metadata GitHub](https://api.github.com/repos/akullpp/awesome-java).

<a id="anhkysuai-2026-11-23-type-challenges-type-challenges"></a>

### type-challenges

**Repo:** [type-challenges/type-challenges](https://github.com/type-challenges/type-challenges) · **License:** MIT · **★ 48,571 (GitHub API, 2026-11-23)**

**Mục đích:** Bộ thử thách hệ kiểu TypeScript có mức độ và cách chơi trực tuyến hoặc cục bộ.

**Giá trị:** Dùng để luyện conditional/mapped types và kiểm tiện ích kiểu nhỏ trước khi viết API công khai.

**Giới hạn:** Giải được câu đố kiểu không chứng minh thiết kế API dễ sử dụng; dạng kiểm và kết quả còn phụ thuộc phiên bản TypeScript.

**Cách tham khảo/tích hợp:** Chọn bài theo mục tiêu, thực hành lại trên môi trường riêng và kiểm bằng bài chuyển giao; khi dùng lại nội dung phải đối chiếu giấy phép đúng phạm vi.

**Lựa chọn để đối chiếu:** [sindresorhus/type-fest](https://github.com/sindresorhus/type-fest) · [leonardomso/33-js-concepts](https://github.com/leonardomso/33-js-concepts). Đây là ứng viên so sánh theo tác vụ; mức phù hợp cần kiểm theo hồ sơ và phiên bản riêng.

**Bằng chứng:** `docs-read`, ngày 2026-11-23, commit [`91220864b0cbb84106c3b97e8d116316db2856e7`](https://github.com/type-challenges/type-challenges/commit/91220864b0cbb84106c3b97e8d116316db2856e7), ngày commit 2026-10-26. Đã clone và đọc chọn lọc phần giới thiệu, cách dùng, giới hạn, license, metadata manifest và CI hiện diện. Chưa kiểm đầy đủ implementation hoặc chạy upstream; các số đo của tác giả chưa được tái lập.

**Nguồn:** [README.md](https://github.com/type-challenges/type-challenges/blob/91220864b0cbb84106c3b97e8d116316db2856e7/README.md) · [LICENSE](https://github.com/type-challenges/type-challenges/blob/91220864b0cbb84106c3b97e8d116316db2856e7/LICENSE) · [package.json](https://github.com/type-challenges/type-challenges/blob/91220864b0cbb84106c3b97e8d116316db2856e7/package.json) · [.github/workflows/issue-pr.yaml](https://github.com/type-challenges/type-challenges/blob/91220864b0cbb84106c3b97e8d116316db2856e7/.github/workflows/issue-pr.yaml) · [metadata GitHub](https://api.github.com/repos/type-challenges/type-challenges).

<a id="anhkysuai-2026-11-23-asabeneh-30-days-of-javascript"></a>

### 30-Days-Of-JavaScript

**Repo:** [Asabeneh/30-Days-Of-JavaScript](https://github.com/Asabeneh/30-Days-Of-JavaScript) · **License:** Chưa xác lập ở phạm vi đã đọc · **★ 47,012 (GitHub API, 2026-11-23)**

**Mục đích:** Chuỗi bài học JavaScript theo ngày, kèm ví dụ trình duyệt, Node.js và bài tập.

**Giá trị:** Thích hợp cho người mới muốn đi tuần tự từ kiểu dữ liệu và cú pháp đến thao tác web.

**Giới hạn:** Không thấy giấy phép chung trong gốc repo đã đọc; chứng chỉ được dẫn sang dịch vụ khác, không phải bằng chứng đánh giá độc lập của kho. Chưa xác lập giấy phép chung cho nội dung chính ở phạm vi đã đọc; không suy quyền tái sử dụng từ repo công khai.

**Cách tham khảo/tích hợp:** Chọn bài theo mục tiêu, thực hành lại trên môi trường riêng và kiểm bằng bài chuyển giao; khi dùng lại nội dung phải đối chiếu giấy phép đúng phạm vi.

**Lựa chọn để đối chiếu:** [javascript-tutorial/en.javascript.info](https://github.com/javascript-tutorial/en.javascript.info) · [leonardomso/33-js-concepts](https://github.com/leonardomso/33-js-concepts). Đây là ứng viên so sánh theo tác vụ; mức phù hợp cần kiểm theo hồ sơ và phiên bản riêng.

**Bằng chứng:** `docs-read`, ngày 2026-11-23, commit [`b143737586aa17d7afc2e31d0b257c40512913d7`](https://github.com/Asabeneh/30-Days-Of-JavaScript/commit/b143737586aa17d7afc2e31d0b257c40512913d7), ngày commit 2026-08-27. Đã clone và đọc chọn lọc phần giới thiệu, cách dùng, giới hạn, license, metadata manifest và CI hiện diện. Chưa kiểm đầy đủ implementation hoặc chạy upstream; các số đo của tác giả chưa được tái lập.

**Nguồn:** [readMe.md](https://github.com/Asabeneh/30-Days-Of-JavaScript/blob/b143737586aa17d7afc2e31d0b257c40512913d7/readMe.md) · [metadata GitHub](https://api.github.com/repos/Asabeneh/30-Days-Of-JavaScript).

<a id="anhkysuai-2026-11-23-karanpratapsingh-system-design"></a>

### system-design

**Repo:** [karanpratapsingh/system-design](https://github.com/karanpratapsingh/system-design) · **License:** CC BY-NC-ND 4.0 · **★ 46,996 (GitHub API, 2026-11-23)**

**Mục đích:** Tài liệu thiết kế hệ thống, bao quát mạng, lưu trữ, phân phối và các bài toán phỏng vấn.

**Giá trị:** Tập hợp khái niệm cùng sơ đồ để thống nhất từ vựng trước khi thảo luận trade-off kiến trúc.

**Giới hạn:** Giấy phép CC BY-NC-ND 4.0 hạn chế thương mại và bản phái sinh; bài đọc không thay thử tải hay kiểm failure mode của hệ thực tế.

**Cách tham khảo/tích hợp:** Chọn bài theo mục tiêu, thực hành lại trên môi trường riêng và kiểm bằng bài chuyển giao; khi dùng lại nội dung phải đối chiếu giấy phép đúng phạm vi.

**Lựa chọn để đối chiếu:** [donnemartin/system-design-primer](https://github.com/donnemartin/system-design-primer) · [ashishps1/awesome-system-design-resources](https://github.com/ashishps1/awesome-system-design-resources). Đây là ứng viên so sánh theo tác vụ; mức phù hợp cần kiểm theo hồ sơ và phiên bản riêng.

**Bằng chứng:** `docs-read`, ngày 2026-11-23, commit [`6dcea405d41401bfbe4031b6b80f7a2d87b712ba`](https://github.com/karanpratapsingh/system-design/commit/6dcea405d41401bfbe4031b6b80f7a2d87b712ba), ngày commit 2026-10-18. Đã clone và đọc chọn lọc phần giới thiệu, cách dùng, giới hạn, license, metadata manifest và CI hiện diện. Chưa kiểm đầy đủ implementation hoặc chạy upstream; các số đo của tác giả chưa được tái lập.

**Nguồn:** [README.md](https://github.com/karanpratapsingh/system-design/blob/6dcea405d41401bfbe4031b6b80f7a2d87b712ba/README.md) · [LICENSE](https://github.com/karanpratapsingh/system-design/blob/6dcea405d41401bfbe4031b6b80f7a2d87b712ba/LICENSE) · [metadata GitHub](https://api.github.com/repos/karanpratapsingh/system-design).

<a id="anhkysuai-2026-11-23-docker-awesome-compose"></a>

### awesome-compose

**Repo:** [docker/awesome-compose](https://github.com/docker/awesome-compose) · **License:** CC0-1.0 · **★ 46,752 (GitHub API, 2026-11-23)**

**Mục đích:** Các mẫu Docker Compose để ghép dịch vụ trong môi trường phát triển cục bộ.

**Giá trị:** Cho ví dụ cụ thể về kết nối ứng dụng, reverse proxy và cơ sở dữ liệu, hữu ích làm điểm xuất phát cho môi trường dev.

**Giới hạn:** README nói rõ mẫu không được triển khai nguyên trạng lên production; chưa đánh giá hardening, backup hoặc khả năng phục hồi.

**Cách tham khảo/tích hợp:** Dùng làm chỉ mục tìm ứng viên, dẫn về nguồn gốc rồi kiểm phiên bản, giấy phép và mức bảo trì của từng lựa chọn trước tích hợp.

**Lựa chọn để đối chiếu:** [GoogleCloudPlatform/microservices-demo](https://github.com/GoogleCloudPlatform/microservices-demo) · [veggiemonk/awesome-docker](https://github.com/veggiemonk/awesome-docker). Đây là ứng viên so sánh theo tác vụ; mức phù hợp cần kiểm theo hồ sơ và phiên bản riêng.

**Bằng chứng:** `docs-read`, ngày 2026-11-23, commit [`503c0dcef31b07fb77b2d4c5556bfafdf86f4f1a`](https://github.com/docker/awesome-compose/commit/503c0dcef31b07fb77b2d4c5556bfafdf86f4f1a), ngày commit 2026-11-19. Đã clone và đọc chọn lọc phần giới thiệu, cách dùng, giới hạn, license, metadata manifest và CI hiện diện. Chưa kiểm đầy đủ implementation hoặc chạy upstream; các số đo của tác giả chưa được tái lập.

**Nguồn:** [README.md](https://github.com/docker/awesome-compose/blob/503c0dcef31b07fb77b2d4c5556bfafdf86f4f1a/README.md) · [LICENSE](https://github.com/docker/awesome-compose/blob/503c0dcef31b07fb77b2d4c5556bfafdf86f4f1a/LICENSE) · [.github/workflows/codeql-analysis.yml](https://github.com/docker/awesome-compose/blob/503c0dcef31b07fb77b2d4c5556bfafdf86f4f1a/.github/workflows/codeql-analysis.yml) · [metadata GitHub](https://api.github.com/repos/docker/awesome-compose).

<a id="anhkysuai-2026-11-23-lecoupa-awesome-cheatsheets"></a>

### awesome-cheatsheets

**Repo:** [LeCoupa/awesome-cheatsheets](https://github.com/LeCoupa/awesome-cheatsheets) · **License:** MIT · **★ 46,697 (GitHub API, 2026-11-23)**

**Mục đích:** Các bảng tra nhanh cho ngôn ngữ, framework, cơ sở dữ liệu và công cụ phát triển.

**Giá trị:** Mỗi chủ đề gói trong ít file, thuận tiện kiểm kiến thức và nhớ lại cú pháp khi đổi stack.

**Giới hạn:** Độ ngắn gọn làm mất ngữ cảnh và ngoại lệ; ví dụ cần đối chiếu phiên bản tài liệu chính thức trước khi dùng trong sản phẩm.

**Cách tham khảo/tích hợp:** Chọn bài theo mục tiêu, thực hành lại trên môi trường riêng và kiểm bằng bài chuyển giao; khi dùng lại nội dung phải đối chiếu giấy phép đúng phạm vi.

**Lựa chọn để đối chiếu:** [tldr-pages/tldr](https://github.com/tldr-pages/tldr) · [gto76/python-cheatsheet](https://github.com/gto76/python-cheatsheet). Đây là ứng viên so sánh theo tác vụ; mức phù hợp cần kiểm theo hồ sơ và phiên bản riêng.

**Bằng chứng:** `docs-read`, ngày 2026-11-23, commit [`774445f64658289826909165d4ef446f4cf59f13`](https://github.com/LeCoupa/awesome-cheatsheets/commit/774445f64658289826909165d4ef446f4cf59f13), ngày commit 2026-10-17. Đã clone và đọc chọn lọc phần giới thiệu, cách dùng, giới hạn, license, metadata manifest và CI hiện diện. Chưa kiểm đầy đủ implementation hoặc chạy upstream; các số đo của tác giả chưa được tái lập.

**Nguồn:** [README.md](https://github.com/LeCoupa/awesome-cheatsheets/blob/774445f64658289826909165d4ef446f4cf59f13/README.md) · [LICENSE](https://github.com/LeCoupa/awesome-cheatsheets/blob/774445f64658289826909165d4ef446f4cf59f13/LICENSE) · [metadata GitHub](https://api.github.com/repos/LeCoupa/awesome-cheatsheets).

<a id="anhkysuai-2026-11-23-dataexpert-io-data-engineer-handbook"></a>

### data-engineer-handbook

**Repo:** [DataExpert-io/data-engineer-handbook](https://github.com/DataExpert-io/data-engineer-handbook) · **License:** Chưa xác lập ở phạm vi đã đọc · **★ 45,248 (GitHub API, 2026-11-23)**

**Mục đích:** Chỉ mục sách, khóa học, cộng đồng, bài viết và tài nguyên data engineering.

**Giá trị:** Hữu ích chọn tuyến học hoặc nguồn đọc theo vai trò trong pipeline dữ liệu.

**Giới hạn:** README có quảng bá khóa và mốc thời gian của từng đợt học; không thấy giấy phép chung, không coi toàn bộ tài liệu liên kết là được phép tái phân phối. Chưa xác lập giấy phép chung cho nội dung chính ở phạm vi đã đọc; không suy quyền tái sử dụng từ repo công khai.

**Cách tham khảo/tích hợp:** Dùng làm chỉ mục tìm ứng viên, dẫn về nguồn gốc rồi kiểm phiên bản, giấy phép và mức bảo trì của từng lựa chọn trước tích hợp.

**Lựa chọn để đối chiếu:** [DataTalksClub/data-engineering-zoomcamp](https://github.com/DataTalksClub/data-engineering-zoomcamp) · [charlax/professional-programming](https://github.com/charlax/professional-programming). Đây là ứng viên so sánh theo tác vụ; mức phù hợp cần kiểm theo hồ sơ và phiên bản riêng.

**Bằng chứng:** `docs-read`, ngày 2026-11-23, commit [`103edb0c056380ac8c0ab0bffdf149a4f1f0f128`](https://github.com/DataExpert-io/data-engineer-handbook/commit/103edb0c056380ac8c0ab0bffdf149a4f1f0f128), ngày commit 2026-08-03. Đã clone và đọc chọn lọc phần giới thiệu, cách dùng, giới hạn, license, metadata manifest và CI hiện diện. Chưa kiểm đầy đủ implementation hoặc chạy upstream; các số đo của tác giả chưa được tái lập.

**Nguồn:** [README.md](https://github.com/DataExpert-io/data-engineer-handbook/blob/103edb0c056380ac8c0ab0bffdf149a4f1f0f128/README.md) · [metadata GitHub](https://api.github.com/repos/DataExpert-io/data-engineer-handbook).

<a id="anhkysuai-2026-11-23-yangshun-front-end-interview-handbook"></a>

### front-end-interview-handbook

**Repo:** [yangshun/front-end-interview-handbook](https://github.com/yangshun/front-end-interview-handbook) · **License:** MIT · **★ 44,001 (GitHub API, 2026-11-23)**

**Mục đích:** Tài liệu chuẩn bị phỏng vấn frontend về HTML, CSS, JavaScript và cách luyện tập.

**Giá trị:** Tập trung đặc thù frontend thay vì chỉ thuật toán; phù hợp xây bài chẩn đoán kiến thức theo vai trò.

**Giới hạn:** Có liên kết dịch vụ GreatFrontEnd của tác giả; quyền và tính năng nền tảng luyện tập riêng không suy từ MIT của repo.

**Cách tham khảo/tích hợp:** Chọn bài theo mục tiêu, thực hành lại trên môi trường riêng và kiểm bằng bài chuyển giao; khi dùng lại nội dung phải đối chiếu giấy phép đúng phạm vi.

**Lựa chọn để đối chiếu:** [leonardomso/33-js-concepts](https://github.com/leonardomso/33-js-concepts) · [javascript-tutorial/en.javascript.info](https://github.com/javascript-tutorial/en.javascript.info). Đây là ứng viên so sánh theo tác vụ; mức phù hợp cần kiểm theo hồ sơ và phiên bản riêng.

**Bằng chứng:** `docs-read`, ngày 2026-11-23, commit [`75ee62afc63bb9b48be160b0710bfcba6ab01a75`](https://github.com/yangshun/front-end-interview-handbook/commit/75ee62afc63bb9b48be160b0710bfcba6ab01a75), ngày commit 2026-10-05. Đã clone và đọc chọn lọc phần giới thiệu, cách dùng, giới hạn, license, metadata manifest và CI hiện diện. Chưa kiểm đầy đủ implementation hoặc chạy upstream; các số đo của tác giả chưa được tái lập.

**Nguồn:** [README.md](https://github.com/yangshun/front-end-interview-handbook/blob/75ee62afc63bb9b48be160b0710bfcba6ab01a75/README.md) · [LICENSE](https://github.com/yangshun/front-end-interview-handbook/blob/75ee62afc63bb9b48be160b0710bfcba6ab01a75/LICENSE) · [package.json](https://github.com/yangshun/front-end-interview-handbook/blob/75ee62afc63bb9b48be160b0710bfcba6ab01a75/package.json) · [metadata GitHub](https://api.github.com/repos/yangshun/front-end-interview-handbook).

<a id="anhkysuai-2026-11-23-ashishps1-awesome-system-design-resources"></a>

### awesome-system-design-resources

**Repo:** [ashishps1/awesome-system-design-resources](https://github.com/ashishps1/awesome-system-design-resources) · **License:** GPL-3.0 · **★ 43,550 (GitHub API, 2026-11-23)**

**Mục đích:** Tài nguyên thiết kế hệ thống từ mạng/API/CSDL đến phân tán và bài phỏng vấn.

**Giá trị:** Các nhóm khái niệm và mức độ bài tập giúp lập danh sách đọc theo khoảng trống kiến thức.

**Giới hạn:** Là nguồn tuyển chọn có liên kết khóa/newsletter; không xác nhận độ đúng hoặc mức cập nhật của mọi nguồn ngoài.

**Cách tham khảo/tích hợp:** Dùng làm chỉ mục tìm ứng viên, dẫn về nguồn gốc rồi kiểm phiên bản, giấy phép và mức bảo trì của từng lựa chọn trước tích hợp.

**Lựa chọn để đối chiếu:** [karanpratapsingh/system-design](https://github.com/karanpratapsingh/system-design) · [donnemartin/system-design-primer](https://github.com/donnemartin/system-design-primer). Đây là ứng viên so sánh theo tác vụ; mức phù hợp cần kiểm theo hồ sơ và phiên bản riêng.

**Bằng chứng:** `docs-read`, ngày 2026-11-23, commit [`58bf0b48badf1e6d62d1e3d024e9578ff809c95f`](https://github.com/ashishps1/awesome-system-design-resources/commit/58bf0b48badf1e6d62d1e3d024e9578ff809c95f), ngày commit 2026-11-01. Đã clone và đọc chọn lọc phần giới thiệu, cách dùng, giới hạn, license, metadata manifest và CI hiện diện. Chưa kiểm đầy đủ implementation hoặc chạy upstream; các số đo của tác giả chưa được tái lập.

**Nguồn:** [README.md](https://github.com/ashishps1/awesome-system-design-resources/blob/58bf0b48badf1e6d62d1e3d024e9578ff809c95f/README.md) · [LICENSE](https://github.com/ashishps1/awesome-system-design-resources/blob/58bf0b48badf1e6d62d1e3d024e9578ff809c95f/LICENSE) · [metadata GitHub](https://api.github.com/repos/ashishps1/awesome-system-design-resources).

<a id="anhkysuai-2026-11-23-faif-python-patterns"></a>

### python-patterns

**Repo:** [faif/python-patterns](https://github.com/faif/python-patterns) · **License:** Chưa xác lập ở phạm vi đã đọc · **★ 43,118 (GitHub API, 2026-11-23)**

**Mục đích:** Ví dụ design pattern và idiom Python, kèm thảo luận anti-pattern.

**Giá trị:** README nhấn mạnh lý do chọn mẫu và trade-off, hữu ích tránh áp dụng pattern chỉ theo hình thức.

**Giới hạn:** Không thấy giấy phép chung trong gốc repo đã đọc; ví dụ học tập chưa được kiểm như thư viện sản phẩm. Chưa xác lập giấy phép chung cho nội dung chính ở phạm vi đã đọc; không suy quyền tái sử dụng từ repo công khai.

**Cách tham khảo/tích hợp:** Chọn bài theo mục tiêu, thực hành lại trên môi trường riêng và kiểm bằng bài chuyển giao; khi dùng lại nội dung phải đối chiếu giấy phép đúng phạm vi.

**Lựa chọn để đối chiếu:** [TheAlgorithms/Python](https://github.com/TheAlgorithms/Python) · [realpython/python-guide](https://github.com/realpython/python-guide). Đây là ứng viên so sánh theo tác vụ; mức phù hợp cần kiểm theo hồ sơ và phiên bản riêng.

**Bằng chứng:** `docs-read`, ngày 2026-11-23, commit [`0712925f8a4b3129e6e54f8ab3580c6f996aa359`](https://github.com/faif/python-patterns/commit/0712925f8a4b3129e6e54f8ab3580c6f996aa359), ngày commit 2026-11-06. Đã clone và đọc chọn lọc phần giới thiệu, cách dùng, giới hạn, license, metadata manifest và CI hiện diện. Chưa kiểm đầy đủ implementation hoặc chạy upstream; các số đo của tác giả chưa được tái lập.

**Nguồn:** [README.md](https://github.com/faif/python-patterns/blob/0712925f8a4b3129e6e54f8ab3580c6f996aa359/README.md) · [pyproject.toml](https://github.com/faif/python-patterns/blob/0712925f8a4b3129e6e54f8ab3580c6f996aa359/pyproject.toml) · [.github/workflows/lint_python.yml](https://github.com/faif/python-patterns/blob/0712925f8a4b3129e6e54f8ab3580c6f996aa359/.github/workflows/lint_python.yml) · [metadata GitHub](https://api.github.com/repos/faif/python-patterns).

<a id="anhkysuai-2026-11-23-patrickjs-awesome-cursorrules"></a>

### awesome-cursorrules

**Repo:** [PatrickJS/awesome-cursorrules](https://github.com/PatrickJS/awesome-cursorrules) · **License:** CC0-1.0 · **★ 41,184 (GitHub API, 2026-11-23)**

**Mục đích:** Các mẫu Cursor Project Rules theo framework và quy trình, hiện dùng định dạng .mdc.

**Giá trị:** Cho ví dụ cách mô tả ràng buộc và kiến trúc cục bộ theo loại file/tác vụ.

**Giới hạn:** Quy tắc trong prompt không là cổng thực thi; các tuyên bố ngăn hallucination phải được kiểm bằng test/check thực tế.

**Cách tham khảo/tích hợp:** Dùng làm chỉ mục tìm ứng viên, dẫn về nguồn gốc rồi kiểm phiên bản, giấy phép và mức bảo trì của từng lựa chọn trước tích hợp.

**Lựa chọn để đối chiếu:** [obra/superpowers](https://github.com/obra/superpowers) · [mattpocock/skills](https://github.com/mattpocock/skills). Đây là ứng viên so sánh theo tác vụ; mức phù hợp cần kiểm theo hồ sơ và phiên bản riêng.

**Bằng chứng:** `docs-read`, ngày 2026-11-23, commit [`b044f956f021b6e8877f16781bcfc466a6a120e9`](https://github.com/PatrickJS/awesome-cursorrules/commit/b044f956f021b6e8877f16781bcfc466a6a120e9), ngày commit 2026-05-30. Đã clone và đọc chọn lọc phần giới thiệu, cách dùng, giới hạn, license, metadata manifest và CI hiện diện. Chưa kiểm đầy đủ implementation hoặc chạy upstream; các số đo của tác giả chưa được tái lập.

**Nguồn:** [README.md](https://github.com/PatrickJS/awesome-cursorrules/blob/b044f956f021b6e8877f16781bcfc466a6a120e9/README.md) · [LICENSE](https://github.com/PatrickJS/awesome-cursorrules/blob/b044f956f021b6e8877f16781bcfc466a6a120e9/LICENSE) · [package.json](https://github.com/PatrickJS/awesome-cursorrules/blob/b044f956f021b6e8877f16781bcfc466a6a120e9/package.json) · [.github/workflows/main.yml](https://github.com/PatrickJS/awesome-cursorrules/blob/b044f956f021b6e8877f16781bcfc466a6a120e9/.github/workflows/main.yml) · [metadata GitHub](https://api.github.com/repos/PatrickJS/awesome-cursorrules).

<a id="anhkysuai-2026-11-23-gto76-python-cheatsheet"></a>

### python-cheatsheet

**Repo:** [gto76/python-cheatsheet](https://github.com/gto76/python-cheatsheet) · **License:** Chưa xác lập ở phạm vi đã đọc · **★ 38,997 (GitHub API, 2026-11-23)**

**Mục đích:** Bảng tra Python về collections, cú pháp, dữ liệu, module và ví dụ sử dụng.

**Giá trị:** Hữu ích tra nhanh một nhóm thao tác và gợi ý ví dụ thử nhỏ khi lập trình.

**Giới hạn:** Không thấy giấy phép chung cho nội dung; license của font trong web không cấp quyền cho toàn repo. Ví dụ dài cần kiểm theo runtime. Chưa xác lập giấy phép chung cho nội dung chính ở phạm vi đã đọc; không suy quyền tái sử dụng từ repo công khai.

**Cách tham khảo/tích hợp:** Chọn bài theo mục tiêu, thực hành lại trên môi trường riêng và kiểm bằng bài chuyển giao; khi dùng lại nội dung phải đối chiếu giấy phép đúng phạm vi.

**Lựa chọn để đối chiếu:** [LeCoupa/awesome-cheatsheets](https://github.com/LeCoupa/awesome-cheatsheets) · [realpython/python-guide](https://github.com/realpython/python-guide). Đây là ứng viên so sánh theo tác vụ; mức phù hợp cần kiểm theo hồ sơ và phiên bản riêng.

**Bằng chứng:** `docs-read`, ngày 2026-11-23, commit [`f2ace2d90ea2f153d7f47edc368586ce8f15d8d7`](https://github.com/gto76/python-cheatsheet/commit/f2ace2d90ea2f153d7f47edc368586ce8f15d8d7), ngày commit 2026-07-27. Đã clone và đọc chọn lọc phần giới thiệu, cách dùng, giới hạn, license, metadata manifest và CI hiện diện. Chưa kiểm đầy đủ implementation hoặc chạy upstream; các số đo của tác giả chưa được tái lập.

**Nguồn:** [README.md](https://github.com/gto76/python-cheatsheet/blob/f2ace2d90ea2f153d7f47edc368586ce8f15d8d7/README.md) · [web/OnlineWebFonts_COM_cb7eb796ae7de7195a34c485cacebad1/License.txt](https://github.com/gto76/python-cheatsheet/blob/f2ace2d90ea2f153d7f47edc368586ce8f15d8d7/web/OnlineWebFonts_COM_cb7eb796ae7de7195a34c485cacebad1/License.txt) · [metadata GitHub](https://api.github.com/repos/gto76/python-cheatsheet).

<a id="anhkysuai-2026-11-23-huihut-interview"></a>

### interview

**Repo:** [huihut/interview](https://github.com/huihut/interview) · **License:** CC BY-NC-SA 4.0 · **★ 38,329 (GitHub API, 2026-11-23)**

**Mục đích:** Ghi chép tiếng Trung ôn C/C++, cấu trúc dữ liệu, hệ điều hành, mạng và liên kết chương trình.

**Giá trị:** Gom kiến thức nền theo chủ đề, hữu ích xây bài chẩn đoán cho vị trí C/C++.

**Giới hạn:** Nội dung CC BY-NC-SA 4.0 và có trích dẫn từ nhiều nguồn; không suy quyền thương mại hoặc chất lượng đáp án từ số sao.

**Cách tham khảo/tích hợp:** Chọn bài theo mục tiêu, thực hành lại trên môi trường riêng và kiểm bằng bài chuyển giao; khi dùng lại nội dung phải đối chiếu giấy phép đúng phạm vi.

**Lựa chọn để đối chiếu:** [TheAlgorithms/C-Plus-Plus](https://github.com/TheAlgorithms/C-Plus-Plus) · [charlax/professional-programming](https://github.com/charlax/professional-programming). Đây là ứng viên so sánh theo tác vụ; mức phù hợp cần kiểm theo hồ sơ và phiên bản riêng.

**Bằng chứng:** `docs-read`, ngày 2026-11-23, commit [`7a7166804a0ffc8f156e906bf4c1a94bb9f6a94b`](https://github.com/huihut/interview/commit/7a7166804a0ffc8f156e906bf4c1a94bb9f6a94b), ngày commit 2026-09-17. Đã clone và đọc chọn lọc phần giới thiệu, cách dùng, giới hạn, license, metadata manifest và CI hiện diện. Chưa kiểm đầy đủ implementation hoặc chạy upstream; các số đo của tác giả chưa được tái lập.

**Nguồn:** [README.md](https://github.com/huihut/interview/blob/7a7166804a0ffc8f156e906bf4c1a94bb9f6a94b/README.md) · [LICENSE](https://github.com/huihut/interview/blob/7a7166804a0ffc8f156e906bf4c1a94bb9f6a94b/LICENSE) · [metadata GitHub](https://api.github.com/repos/huihut/interview).

<a id="anhkysuai-2026-11-23-fengdu78-coursera-ml-andrewng-notes"></a>

### Coursera-ML-AndrewNg-Notes

**Repo:** [fengdu78/Coursera-ML-AndrewNg-Notes](https://github.com/fengdu78/Coursera-ML-AndrewNg-Notes) · **License:** Chưa xác lập ở phạm vi đã đọc · **★ 38,151 (GitHub API, 2026-11-23)**

**Mục đích:** Bản ghi chú và bản dịch tiếng Trung cho khóa machine learning của Andrew Ng.

**Giá trị:** Có bản Markdown/Word để đọc lại khái niệm và công thức của khóa học.

**Giới hạn:** Không thấy license chung; tài liệu khóa học gốc và phần dịch có thể giữ quyền riêng. Nội dung lịch sử không thay tài liệu framework hiện tại. Chưa xác lập giấy phép chung cho nội dung chính ở phạm vi đã đọc; không suy quyền tái sử dụng từ repo công khai.

**Cách tham khảo/tích hợp:** Chọn bài theo mục tiêu, thực hành lại trên môi trường riêng và kiểm bằng bài chuyển giao; khi dùng lại nội dung phải đối chiếu giấy phép đúng phạm vi.

**Lựa chọn để đối chiếu:** [microsoft/Data-Science-For-Beginners](https://github.com/microsoft/Data-Science-For-Beginners) · [d2l-ai/d2l-zh](https://github.com/d2l-ai/d2l-zh). Đây là ứng viên so sánh theo tác vụ; mức phù hợp cần kiểm theo hồ sơ và phiên bản riêng.

**Bằng chứng:** `docs-read`, ngày 2026-11-23, commit [`f41f2ab2a7f1fa7b5d659f315732b1afaf157948`](https://github.com/fengdu78/Coursera-ML-AndrewNg-Notes/commit/f41f2ab2a7f1fa7b5d659f315732b1afaf157948), ngày commit 2026-10-05. Đã clone và đọc chọn lọc phần giới thiệu, cách dùng, giới hạn, license, metadata manifest và CI hiện diện. Chưa kiểm đầy đủ implementation hoặc chạy upstream; các số đo của tác giả chưa được tái lập.

**Nguồn:** [README.md](https://github.com/fengdu78/Coursera-ML-AndrewNg-Notes/blob/f41f2ab2a7f1fa7b5d659f315732b1afaf157948/README.md) · [metadata GitHub](https://api.github.com/repos/fengdu78/Coursera-ML-AndrewNg-Notes).

<a id="anhkysuai-2026-11-23-microsoft-data-science-for-beginners"></a>

### Data-Science-For-Beginners

**Repo:** [microsoft/Data-Science-For-Beginners](https://github.com/microsoft/Data-Science-For-Beginners) · **License:** MIT · **★ 38,120 (GitHub API, 2026-11-23)**

**Mục đích:** Giáo trình nhập môn data science gồm bài học, quiz trước/sau, hướng dẫn và bài tập.

**Giá trị:** Phân tách tài liệu cho người học và giáo viên, phù hợp dựng khóa thực hành theo dự án.

**Giới hạn:** Con số thời lượng và hiệu quả sư phạm là mô tả của tác giả; chưa chạy bài tập hoặc đánh giá đầu ra học viên.

**Cách tham khảo/tích hợp:** Chọn bài theo mục tiêu, thực hành lại trên môi trường riêng và kiểm bằng bài chuyển giao; khi dùng lại nội dung phải đối chiếu giấy phép đúng phạm vi.

**Lựa chọn để đối chiếu:** [DataTalksClub/data-engineering-zoomcamp](https://github.com/DataTalksClub/data-engineering-zoomcamp) · [d2l-ai/d2l-zh](https://github.com/d2l-ai/d2l-zh). Đây là ứng viên so sánh theo tác vụ; mức phù hợp cần kiểm theo hồ sơ và phiên bản riêng.

**Bằng chứng:** `docs-read`, ngày 2026-11-23, commit [`4d2ac427ad6f022e73a75c4f46a28bbb7978ec3f`](https://github.com/microsoft/Data-Science-For-Beginners/commit/4d2ac427ad6f022e73a75c4f46a28bbb7978ec3f), ngày commit 2026-07-17. Đã clone và đọc chọn lọc phần giới thiệu, cách dùng, giới hạn, license, metadata manifest và CI hiện diện. Chưa kiểm đầy đủ implementation hoặc chạy upstream; các số đo của tác giả chưa được tái lập.

**Nguồn:** [README.md](https://github.com/microsoft/Data-Science-For-Beginners/blob/4d2ac427ad6f022e73a75c4f46a28bbb7978ec3f/README.md) · [LICENSE](https://github.com/microsoft/Data-Science-For-Beginners/blob/4d2ac427ad6f022e73a75c4f46a28bbb7978ec3f/LICENSE) · [package.json](https://github.com/microsoft/Data-Science-For-Beginners/blob/4d2ac427ad6f022e73a75c4f46a28bbb7978ec3f/package.json) · [metadata GitHub](https://api.github.com/repos/microsoft/Data-Science-For-Beginners).

<a id="anhkysuai-2026-11-23-pkuanonym-rekcarc-tsc-uht"></a>

### REKCARC-TSC-UHT

**Repo:** [PKUanonym/REKCARC-TSC-UHT](https://github.com/PKUanonym/REKCARC-TSC-UHT) · **License:** CC BY-SA 4.0 (LICENSE); README liên kết CC BY-NC-SA 4.0, tài liệu bên thứ ba giữ quyền riêng · **★ 38,116 (GitHub API, 2026-11-23)**

**Mục đích:** Kho hướng dẫn môn học và tài liệu tham khảo ngành khoa học máy tính của Đại học Thanh Hoa.

**Giá trị:** Giúp nhận diện nội dung từng môn và kinh nghiệm học trong một chương trình cụ thể.

**Giới hạn:** LICENSE là CC BY-SA 4.0 nhưng link trong README lại trỏ BY-NC-SA; quyền tài liệu bên thứ ba được giữ riêng. Không coi toàn bộ kho có cùng quyền tái phân phối.

**Cách tham khảo/tích hợp:** Chọn bài theo mục tiêu, thực hành lại trên môi trường riêng và kiểm bằng bài chuyển giao; khi dùng lại nội dung phải đối chiếu giấy phép đúng phạm vi.

**Lựa chọn để đối chiếu:** [Developer-Y/cs-video-courses](https://github.com/Developer-Y/cs-video-courses) · [jwasham/coding-interview-university](https://github.com/jwasham/coding-interview-university). Đây là ứng viên so sánh theo tác vụ; mức phù hợp cần kiểm theo hồ sơ và phiên bản riêng.

**Bằng chứng:** `docs-read`, ngày 2026-11-23, commit [`ee2403d24dbe85fb33444133bb9ab98be5ea2f67`](https://github.com/PKUanonym/REKCARC-TSC-UHT/commit/ee2403d24dbe85fb33444133bb9ab98be5ea2f67), ngày commit 2026-11-15. Đã clone và đọc chọn lọc phần giới thiệu, cách dùng, giới hạn, license, metadata manifest và CI hiện diện. Chưa kiểm đầy đủ implementation hoặc chạy upstream; các số đo của tác giả chưa được tái lập.

**Nguồn:** [README.md](https://github.com/PKUanonym/REKCARC-TSC-UHT/blob/ee2403d24dbe85fb33444133bb9ab98be5ea2f67/README.md) · [LICENSE](https://github.com/PKUanonym/REKCARC-TSC-UHT/blob/ee2403d24dbe85fb33444133bb9ab98be5ea2f67/LICENSE) · [metadata GitHub](https://api.github.com/repos/PKUanonym/REKCARC-TSC-UHT).

<a id="anhkysuai-2026-11-23-denysdovhan-wtfjs"></a>

### wtfjs

**Repo:** [denysdovhan/wtfjs](https://github.com/denysdovhan/wtfjs) · **License:** WTFPL · **★ 37,691 (GitHub API, 2026-11-23)**

**Mục đích:** Các ví dụ JavaScript dễ gây bất ngờ về ép kiểu, so sánh và hành vi ngôn ngữ, kèm giải thích.

**Giá trị:** Tạo corpus nhỏ để luyện dự đoán kết quả và tìm các góc cạnh cần test.

**Giới hạn:** Các câu đố có chủ ý bất thường; không dùng chúng như phong cách viết ứng dụng hoặc bằng chứng mọi runtime giống nhau.

**Cách tham khảo/tích hợp:** Chọn bài theo mục tiêu, thực hành lại trên môi trường riêng và kiểm bằng bài chuyển giao; khi dùng lại nội dung phải đối chiếu giấy phép đúng phạm vi.

**Lựa chọn để đối chiếu:** [leonardomso/33-js-concepts](https://github.com/leonardomso/33-js-concepts) · [javascript-tutorial/en.javascript.info](https://github.com/javascript-tutorial/en.javascript.info). Đây là ứng viên so sánh theo tác vụ; mức phù hợp cần kiểm theo hồ sơ và phiên bản riêng.

**Bằng chứng:** `docs-read`, ngày 2026-11-23, commit [`a2c83226a15890004758971264211f116fff367a`](https://github.com/denysdovhan/wtfjs/commit/a2c83226a15890004758971264211f116fff367a), ngày commit 2026-10-05. Đã clone và đọc chọn lọc phần giới thiệu, cách dùng, giới hạn, license, metadata manifest và CI hiện diện. Chưa kiểm đầy đủ implementation hoặc chạy upstream; các số đo của tác giả chưa được tái lập.

**Nguồn:** [README.md](https://github.com/denysdovhan/wtfjs/blob/a2c83226a15890004758971264211f116fff367a/README.md) · [LICENSE](https://github.com/denysdovhan/wtfjs/blob/a2c83226a15890004758971264211f116fff367a/LICENSE) · [package.json](https://github.com/denysdovhan/wtfjs/blob/a2c83226a15890004758971264211f116fff367a/package.json) · [.github/workflows/release.yml](https://github.com/denysdovhan/wtfjs/blob/a2c83226a15890004758971264211f116fff367a/.github/workflows/release.yml) · [metadata GitHub](https://api.github.com/repos/denysdovhan/wtfjs).

<a id="anhkysuai-2026-11-23-veggiemonk-awesome-docker"></a>

### awesome-docker

**Repo:** [veggiemonk/awesome-docker](https://github.com/veggiemonk/awesome-docker) · **License:** Apache-2.0 · **★ 37,288 (GitHub API, 2026-11-23)**

**Mục đích:** Danh sách công cụ và tài nguyên Docker theo hạ tầng, bảo mật, build và vận hành.

**Giá trị:** Có phân biệt mục thương mại và nguồn mở; hữu ích tìm nhóm công cụ quanh container.

**Giới hạn:** License của danh sách không đại diện image hay dịch vụ được dẫn; nhãn hoạt động không thay kiểm hỗ trợ phiên bản và nguồn image.

**Cách tham khảo/tích hợp:** Dùng làm chỉ mục tìm ứng viên, dẫn về nguồn gốc rồi kiểm phiên bản, giấy phép và mức bảo trì của từng lựa chọn trước tích hợp.

**Lựa chọn để đối chiếu:** [docker/awesome-compose](https://github.com/docker/awesome-compose) · [awesome-foss/awesome-sysadmin](https://github.com/awesome-foss/awesome-sysadmin). Đây là ứng viên so sánh theo tác vụ; mức phù hợp cần kiểm theo hồ sơ và phiên bản riêng.

**Bằng chứng:** `docs-read`, ngày 2026-11-23, commit [`00e5cbc02d897e5a577840597ed51b33feb5677d`](https://github.com/veggiemonk/awesome-docker/commit/00e5cbc02d897e5a577840597ed51b33feb5677d), ngày commit 2026-11-12. Đã clone và đọc chọn lọc phần giới thiệu, cách dùng, giới hạn, license, metadata manifest và CI hiện diện. Chưa kiểm đầy đủ implementation hoặc chạy upstream; các số đo của tác giả chưa được tái lập.

**Nguồn:** [README.md](https://github.com/veggiemonk/awesome-docker/blob/00e5cbc02d897e5a577840597ed51b33feb5677d/README.md) · [LICENSE](https://github.com/veggiemonk/awesome-docker/blob/00e5cbc02d897e5a577840597ed51b33feb5677d/LICENSE) · [go.mod](https://github.com/veggiemonk/awesome-docker/blob/00e5cbc02d897e5a577840597ed51b33feb5677d/go.mod) · [.github/workflows/broken_links.yml](https://github.com/veggiemonk/awesome-docker/blob/00e5cbc02d897e5a577840597ed51b33feb5677d/.github/workflows/broken_links.yml) · [metadata GitHub](https://api.github.com/repos/veggiemonk/awesome-docker).

<a id="anhkysuai-2026-11-23-awesome-foss-awesome-sysadmin"></a>

### awesome-sysadmin

**Repo:** [awesome-foss/awesome-sysadmin](https://github.com/awesome-foss/awesome-sysadmin) · **License:** CC BY-SA 4.0 · **★ 35,799 (GitHub API, 2026-11-23)**

**Mục đích:** Danh sách phần mềm và tài nguyên quản trị hệ thống từ backup đến định danh, triển khai và giám sát.

**Giá trị:** Có bản HTML được khuyến nghị và kho dữ liệu riêng, thuận tiện làm chỉ mục công cụ theo nhiệm vụ.

**Giới hạn:** README gọi bản Markdown là legacy; cần theo nguồn dữ liệu hiện hành. CC BY-SA của danh sách không cấp quyền cho từng sản phẩm.

**Cách tham khảo/tích hợp:** Dùng làm chỉ mục tìm ứng viên, dẫn về nguồn gốc rồi kiểm phiên bản, giấy phép và mức bảo trì của từng lựa chọn trước tích hợp.

**Lựa chọn để đối chiếu:** [veggiemonk/awesome-docker](https://github.com/veggiemonk/awesome-docker) · [awesome-selfhosted/awesome-selfhosted](https://github.com/awesome-selfhosted/awesome-selfhosted). Đây là ứng viên so sánh theo tác vụ; mức phù hợp cần kiểm theo hồ sơ và phiên bản riêng.

**Bằng chứng:** `docs-read`, ngày 2026-11-23, commit [`ed63cb4d7d63dc8ea84bbd6a1770683d3d3e4f64`](https://github.com/awesome-foss/awesome-sysadmin/commit/ed63cb4d7d63dc8ea84bbd6a1770683d3d3e4f64), ngày commit 2026-10-22. Đã clone và đọc chọn lọc phần giới thiệu, cách dùng, giới hạn, license, metadata manifest và CI hiện diện. Chưa kiểm đầy đủ implementation hoặc chạy upstream; các số đo của tác giả chưa được tái lập.

**Nguồn:** [README.md](https://github.com/awesome-foss/awesome-sysadmin/blob/ed63cb4d7d63dc8ea84bbd6a1770683d3d3e4f64/README.md) · [LICENSE.txt](https://github.com/awesome-foss/awesome-sysadmin/blob/ed63cb4d7d63dc8ea84bbd6a1770683d3d3e4f64/LICENSE.txt) · [metadata GitHub](https://api.github.com/repos/awesome-foss/awesome-sysadmin).

<a id="anhkysuai-2026-11-23-jondot-awesome-react-native"></a>

### awesome-react-native

**Repo:** [jondot/awesome-react-native](https://github.com/jondot/awesome-react-native) · **License:** Chưa xác lập ở phạm vi đã đọc · **★ 35,709 (GitHub API, 2026-11-23)**

**Mục đích:** Danh sách thư viện và tài liệu React Native, có nhóm UI, công cụ phát triển và AI.

**Giá trị:** Tổ chức theo chức năng ứng dụng, hữu ích dựng shortlist cho một màn hình hoặc khả năng native cần thêm.

**Giới hạn:** Tuyên bố mọi mục hợp React Native hiện đại chưa được kiểm độc lập; không thấy license chung trong gốc repo đã đọc. Chưa xác lập giấy phép chung cho nội dung chính ở phạm vi đã đọc; không suy quyền tái sử dụng từ repo công khai.

**Cách tham khảo/tích hợp:** Dùng làm chỉ mục tìm ứng viên, dẫn về nguồn gốc rồi kiểm phiên bản, giấy phép và mức bảo trì của từng lựa chọn trước tích hợp.

**Lựa chọn để đối chiếu:** [Solido/awesome-flutter](https://github.com/Solido/awesome-flutter) · [wasabeef/awesome-android-ui](https://github.com/wasabeef/awesome-android-ui). Đây là ứng viên so sánh theo tác vụ; mức phù hợp cần kiểm theo hồ sơ và phiên bản riêng.

**Bằng chứng:** `docs-read`, ngày 2026-11-23, commit [`673360681d1026269753de05593f2e6dd826afc2`](https://github.com/jondot/awesome-react-native/commit/673360681d1026269753de05593f2e6dd826afc2), ngày commit 2026-08-26. Đã clone và đọc chọn lọc phần giới thiệu, cách dùng, giới hạn, license, metadata manifest và CI hiện diện. Chưa kiểm đầy đủ implementation hoặc chạy upstream; các số đo của tác giả chưa được tái lập.

**Nguồn:** [README.md](https://github.com/jondot/awesome-react-native/blob/673360681d1026269753de05593f2e6dd826afc2/README.md) · [metadata GitHub](https://api.github.com/repos/jondot/awesome-react-native).

<a id="anhkysuai-2026-11-23-liquidslr-leetcode-company-wise-problems"></a>

### leetcode-company-wise-problems

**Repo:** [liquidslr/leetcode-company-wise-problems](https://github.com/liquidslr/leetcode-company-wise-problems) · **License:** Chưa xác lập ở phạm vi đã đọc · **★ 35,703 (GitHub API, 2026-11-23)**

**Mục đích:** Danh sách câu hỏi LeetCode dạng CSV theo công ty và khoảng thời gian.

**Giá trị:** Dữ liệu có cấu trúc giúp lọc bài theo chủ đề hoặc nhóm luyện tập thay vì đọc danh sách dài.

**Giới hạn:** Metadata mô tả mốc tháng10/2025 còn README ghi tháng6/2025; commit mới không xác nhận độ mới dữ liệu. Không thấy license chung và không xác minh nguồn nhãn công ty. Chưa xác lập giấy phép chung cho nội dung chính ở phạm vi đã đọc; không suy quyền tái sử dụng từ repo công khai.

**Cách tham khảo/tích hợp:** Chọn bài theo mục tiêu, thực hành lại trên môi trường riêng và kiểm bằng bài chuyển giao; khi dùng lại nội dung phải đối chiếu giấy phép đúng phạm vi.

**Lựa chọn để đối chiếu:** [youngyangyang04/leetcode-master](https://github.com/youngyangyang04/leetcode-master) · [halfrost/LeetCode-Go](https://github.com/halfrost/LeetCode-Go). Đây là ứng viên so sánh theo tác vụ; mức phù hợp cần kiểm theo hồ sơ và phiên bản riêng.

**Bằng chứng:** `docs-read`, ngày 2026-11-23, commit [`2b71796266751b4736a7ef180efb6847879166ee`](https://github.com/liquidslr/leetcode-company-wise-problems/commit/2b71796266751b4736a7ef180efb6847879166ee), ngày commit 2026-10-20. Đã clone và đọc chọn lọc phần giới thiệu, cách dùng, giới hạn, license, metadata manifest và CI hiện diện. Chưa kiểm đầy đủ implementation hoặc chạy upstream; các số đo của tác giả chưa được tái lập.

**Nguồn:** [Readme.md](https://github.com/liquidslr/leetcode-company-wise-problems/blob/2b71796266751b4736a7ef180efb6847879166ee/Readme.md) · [metadata GitHub](https://api.github.com/repos/liquidslr/leetcode-company-wise-problems).

<a id="anhkysuai-2026-11-23-thealgorithms-c-plus-plus"></a>

### C-Plus-Plus

**Repo:** [TheAlgorithms/C-Plus-Plus](https://github.com/TheAlgorithms/C-Plus-Plus) · **License:** MIT (mã); CC BY-SA 4.0 (tài liệu) · **★ 34,902 (GitHub API, 2026-11-23)**

**Mục đích:** Các thuật toán C++ về toán, khoa học máy tính và lĩnh vực liên quan để học và giảng dạy.

**Giá trị:** Có nhiều cách triển khai cùng mục tiêu và cấu hình CMake, thuận tiện so chiến lược và viết test biên.

**Giới hạn:** Mã MIT nhưng README ghi tài liệu CC BY-SA4.0; ví dụ giáo dục không phải thư viện đã kiểm cho yêu cầu sản phẩm.

**Cách tham khảo/tích hợp:** Chọn bài theo mục tiêu, thực hành lại trên môi trường riêng và kiểm bằng bài chuyển giao; khi dùng lại nội dung phải đối chiếu giấy phép đúng phạm vi.

**Lựa chọn để đối chiếu:** [TheAlgorithms/Java](https://github.com/TheAlgorithms/Java) · [TheAlgorithms/Python](https://github.com/TheAlgorithms/Python). Đây là ứng viên so sánh theo tác vụ; mức phù hợp cần kiểm theo hồ sơ và phiên bản riêng.

**Bằng chứng:** `docs-read`, ngày 2026-11-23, commit [`fdcc29b0ac2848e9d1a8d926e171cc5b39f97759`](https://github.com/TheAlgorithms/C-Plus-Plus/commit/fdcc29b0ac2848e9d1a8d926e171cc5b39f97759), ngày commit 2026-10-03. Đã clone và đọc chọn lọc phần giới thiệu, cách dùng, giới hạn, license, metadata manifest và CI hiện diện. Chưa kiểm đầy đủ implementation hoặc chạy upstream; các số đo của tác giả chưa được tái lập.

**Nguồn:** [README.md](https://github.com/TheAlgorithms/C-Plus-Plus/blob/fdcc29b0ac2848e9d1a8d926e171cc5b39f97759/README.md) · [LICENSE](https://github.com/TheAlgorithms/C-Plus-Plus/blob/fdcc29b0ac2848e9d1a8d926e171cc5b39f97759/LICENSE) · [CMakeLists.txt](https://github.com/TheAlgorithms/C-Plus-Plus/blob/fdcc29b0ac2848e9d1a8d926e171cc5b39f97759/CMakeLists.txt) · [.github/workflows/stale.yml](https://github.com/TheAlgorithms/C-Plus-Plus/blob/fdcc29b0ac2848e9d1a8d926e171cc5b39f97759/.github/workflows/stale.yml) · [metadata GitHub](https://api.github.com/repos/TheAlgorithms/C-Plus-Plus).

<a id="anhkysuai-2026-11-23-halfrost-leetcode-go"></a>

### LeetCode-Go

**Repo:** [halfrost/LeetCode-Go](https://github.com/halfrost/LeetCode-Go) · **License:** MIT (mã Go); nội dung sách Creative Commons chưa xác định đầy đủ biến thể · **★ 33,803 (GitHub API, 2026-11-23)**

**Mục đích:** Lời giải LeetCode bằng Go và nội dung sách giải thuật đi kèm.

**Giá trị:** Cho ví dụ idiom Go theo nhiều nhóm bài và có workflow test để đọc cách tổ chức kiểm thử.

**Giới hạn:** Tuyên bố coverage/hiệu năng chưa tái lập; mã MIT còn sách và hình có giấy phép Creative Commons chưa nêu biến thể rõ trong đoạn README.

**Cách tham khảo/tích hợp:** Chọn bài theo mục tiêu, thực hành lại trên môi trường riêng và kiểm bằng bài chuyển giao; khi dùng lại nội dung phải đối chiếu giấy phép đúng phạm vi.

**Lựa chọn để đối chiếu:** [TheAlgorithms/Java](https://github.com/TheAlgorithms/Java) · [youngyangyang04/leetcode-master](https://github.com/youngyangyang04/leetcode-master). Đây là ứng viên so sánh theo tác vụ; mức phù hợp cần kiểm theo hồ sơ và phiên bản riêng.

**Bằng chứng:** `docs-read`, ngày 2026-11-23, commit [`1dde49c8ab37a08f21a4fb249d7bd90af4a9c58e`](https://github.com/halfrost/LeetCode-Go/commit/1dde49c8ab37a08f21a4fb249d7bd90af4a9c58e), ngày commit 2026-07-08. Đã clone và đọc chọn lọc phần giới thiệu, cách dùng, giới hạn, license, metadata manifest và CI hiện diện. Chưa kiểm đầy đủ implementation hoặc chạy upstream; các số đo của tác giả chưa được tái lập.

**Nguồn:** [README.md](https://github.com/halfrost/LeetCode-Go/blob/1dde49c8ab37a08f21a4fb249d7bd90af4a9c58e/README.md) · [LICENSE](https://github.com/halfrost/LeetCode-Go/blob/1dde49c8ab37a08f21a4fb249d7bd90af4a9c58e/LICENSE) · [go.mod](https://github.com/halfrost/LeetCode-Go/blob/1dde49c8ab37a08f21a4fb249d7bd90af4a9c58e/go.mod) · [.github/workflows/test.yml](https://github.com/halfrost/LeetCode-Go/blob/1dde49c8ab37a08f21a4fb249d7bd90af4a9c58e/.github/workflows/test.yml) · [metadata GitHub](https://api.github.com/repos/halfrost/LeetCode-Go).

<a id="anhkysuai-2026-11-23-google-comprehensive-rust"></a>

### comprehensive-rust

**Repo:** [google/comprehensive-rust](https://github.com/google/comprehensive-rust) · **License:** Apache-2.0 (mã); CC BY-4.0 (tài liệu) · **★ 33,558 (GitHub API, 2026-11-23)**

**Mục đích:** Giáo trình Rust của nhóm Android tại Google, gồm kiến thức nền và các nhánh chuyên sâu.

**Giá trị:** Có tài liệu cho giảng dạy nhiều ngày cùng cấu hình build khóa học, thuận tiện xây lộ trình theo nền tảng người học.

**Giới hạn:** Mã Apache-2.0, văn bản và hình CC BY4.0; thời lượng khóa không chứng minh người học làm được hệ production.

**Cách tham khảo/tích hợp:** Chọn bài theo mục tiêu, thực hành lại trên môi trường riêng và kiểm bằng bài chuyển giao; khi dùng lại nội dung phải đối chiếu giấy phép đúng phạm vi.

**Lựa chọn để đối chiếu:** [rust-lang/rustlings](https://github.com/rust-lang/rustlings) · [sunface/rust-course](https://github.com/sunface/rust-course). Đây là ứng viên so sánh theo tác vụ; mức phù hợp cần kiểm theo hồ sơ và phiên bản riêng.

**Bằng chứng:** `docs-read`, ngày 2026-11-23, commit [`baf25efd192d7c68ef0552aa6803c8aba0f77c4f`](https://github.com/google/comprehensive-rust/commit/baf25efd192d7c68ef0552aa6803c8aba0f77c4f), ngày commit 2026-11-17. Đã clone và đọc chọn lọc phần giới thiệu, cách dùng, giới hạn, license, metadata manifest và CI hiện diện. Chưa kiểm đầy đủ implementation hoặc chạy upstream; các số đo của tác giả chưa được tái lập.

**Nguồn:** [README.md](https://github.com/google/comprehensive-rust/blob/baf25efd192d7c68ef0552aa6803c8aba0f77c4f/README.md) · [LICENSE](https://github.com/google/comprehensive-rust/blob/baf25efd192d7c68ef0552aa6803c8aba0f77c4f/LICENSE) · [LICENSE-CC-BY](https://github.com/google/comprehensive-rust/blob/baf25efd192d7c68ef0552aa6803c8aba0f77c4f/LICENSE-CC-BY) · [Cargo.toml](https://github.com/google/comprehensive-rust/blob/baf25efd192d7c68ef0552aa6803c8aba0f77c4f/Cargo.toml) · [.github/workflows/build.yml](https://github.com/google/comprehensive-rust/blob/baf25efd192d7c68ef0552aa6803c8aba0f77c4f/.github/workflows/build.yml) · [metadata GitHub](https://api.github.com/repos/google/comprehensive-rust).

<a id="anhkysuai-2026-11-23-ziadoz-awesome-php"></a>

### awesome-php

**Repo:** [ziadoz/awesome-php](https://github.com/ziadoz/awesome-php) · **License:** WTFPL · **★ 32,815 (GitHub API, 2026-11-23)**

**Mục đích:** Danh sách thư viện, framework, công cụ và tài liệu PHP theo nhiệm vụ.

**Giá trị:** Bao quát Composer, backend, CMS và nhiều thành phần nhỏ, phù hợp tìm ứng viên ngoài framework đang dùng.

**Giới hạn:** Có cả công cụ thương mại; WTFPL của danh sách không đại diện giấy phép của thư viện hay IDE liên kết.

**Cách tham khảo/tích hợp:** Dùng làm chỉ mục tìm ứng viên, dẫn về nguồn gốc rồi kiểm phiên bản, giấy phép và mức bảo trì của từng lựa chọn trước tích hợp.

**Lựa chọn để đối chiếu:** [akullpp/awesome-java](https://github.com/akullpp/awesome-java) · [rust-unofficial/awesome-rust](https://github.com/rust-unofficial/awesome-rust). Đây là ứng viên so sánh theo tác vụ; mức phù hợp cần kiểm theo hồ sơ và phiên bản riêng.

**Bằng chứng:** `docs-read`, ngày 2026-11-23, commit [`2a84423c910d7329ac36be2613a889368df0d5ad`](https://github.com/ziadoz/awesome-php/commit/2a84423c910d7329ac36be2613a889368df0d5ad), ngày commit 2026-10-30. Đã clone và đọc chọn lọc phần giới thiệu, cách dùng, giới hạn, license, metadata manifest và CI hiện diện. Chưa kiểm đầy đủ implementation hoặc chạy upstream; các số đo của tác giả chưa được tái lập.

**Nguồn:** [README.md](https://github.com/ziadoz/awesome-php/blob/2a84423c910d7329ac36be2613a889368df0d5ad/README.md) · [LICENSE.md](https://github.com/ziadoz/awesome-php/blob/2a84423c910d7329ac36be2613a889368df0d5ad/LICENSE.md) · [.github/workflows/ci.yml](https://github.com/ziadoz/awesome-php/blob/2a84423c910d7329ac36be2613a889368df0d5ad/.github/workflows/ci.yml) · [metadata GitHub](https://api.github.com/repos/ziadoz/awesome-php).

<a id="anhkysuai-2026-11-23-abhisheknaiidu-awesome-github-profile-readme"></a>

### awesome-github-profile-readme

**Repo:** [abhisheknaiidu/awesome-github-profile-readme](https://github.com/abhisheknaiidu/awesome-github-profile-readme) · **License:** CC0-1.0 · **★ 31,667 (GitHub API, 2026-11-23)**

**Mục đích:** Bộ mẫu và tài nguyên làm README hồ sơ GitHub, chia theo phong cách trình bày.

**Giá trị:** Hữu ích tìm bố cục giới thiệu dự án và tham khảo cách sinh nội dung động.

**Giới hạn:** Ảnh, font, badge và dịch vụ ngoài có quyền/độ sẵn sàng riêng; mẫu đẹp không xác nhận chất lượng kỹ thuật hoặc uy tín hồ sơ.

**Cách tham khảo/tích hợp:** Dùng làm chỉ mục tìm ứng viên, dẫn về nguồn gốc rồi kiểm phiên bản, giấy phép và mức bảo trì của từng lựa chọn trước tích hợp.

**Lựa chọn để đối chiếu:** [matiassingers/awesome-readme](https://github.com/matiassingers/awesome-readme) · [alexpate/awesome-design-systems](https://github.com/alexpate/awesome-design-systems). Đây là ứng viên so sánh theo tác vụ; mức phù hợp cần kiểm theo hồ sơ và phiên bản riêng.

**Bằng chứng:** `docs-read`, ngày 2026-11-23, commit [`a2f2de46099a6d503d9240d8f90b4f504755b27f`](https://github.com/abhisheknaiidu/awesome-github-profile-readme/commit/a2f2de46099a6d503d9240d8f90b4f504755b27f), ngày commit 2026-09-12. Đã clone và đọc chọn lọc phần giới thiệu, cách dùng, giới hạn, license, metadata manifest và CI hiện diện. Chưa kiểm đầy đủ implementation hoặc chạy upstream; các số đo của tác giả chưa được tái lập.

**Nguồn:** [README.md](https://github.com/abhisheknaiidu/awesome-github-profile-readme/blob/a2f2de46099a6d503d9240d8f90b4f504755b27f/README.md) · [LICENSE](https://github.com/abhisheknaiidu/awesome-github-profile-readme/blob/a2f2de46099a6d503d9240d8f90b4f504755b27f/LICENSE) · [.github/workflows/prettier.yml](https://github.com/abhisheknaiidu/awesome-github-profile-readme/blob/a2f2de46099a6d503d9240d8f90b4f504755b27f/.github/workflows/prettier.yml) · [metadata GitHub](https://api.github.com/repos/abhisheknaiidu/awesome-github-profile-readme).

<a id="anhkysuai-2026-11-23-sunface-rust-course"></a>

### rust-course

**Repo:** [sunface/rust-course](https://github.com/sunface/rust-course) · **License:** Chưa xác lập ở phạm vi đã đọc · **★ 31,146 (GitHub API, 2026-11-23)**

**Mục đích:** Sách Rust tiếng Trung với giải thích, ví dụ và hướng dẫn học.

**Giá trị:** Một nguồn đọc có chiều sâu bằng tiếng Trung để đối chiếu các khái niệm Rust.

**Giới hạn:** README chủ động chọn No License và cấm tự đóng gói bản sửa đổi để phân phối; MIT của rustlings-zh trong assets không cấp quyền cho toàn sách. Chưa xác lập giấy phép chung cho nội dung chính ở phạm vi đã đọc; không suy quyền tái sử dụng từ repo công khai.

**Cách tham khảo/tích hợp:** Chọn bài theo mục tiêu, thực hành lại trên môi trường riêng và kiểm bằng bài chuyển giao; khi dùng lại nội dung phải đối chiếu giấy phép đúng phạm vi.

**Lựa chọn để đối chiếu:** [google/comprehensive-rust](https://github.com/google/comprehensive-rust) · [rust-lang/rustlings](https://github.com/rust-lang/rustlings). Đây là ứng viên so sánh theo tác vụ; mức phù hợp cần kiểm theo hồ sơ và phiên bản riêng.

**Bằng chứng:** `docs-read`, ngày 2026-11-23, commit [`8ff5c256b228c21131cb313f14427c0859cf6b4b`](https://github.com/sunface/rust-course/commit/8ff5c256b228c21131cb313f14427c0859cf6b4b), ngày commit 2026-11-23. Đã clone và đọc chọn lọc phần giới thiệu, cách dùng, giới hạn, license, metadata manifest và CI hiện diện. Chưa kiểm đầy đủ implementation hoặc chạy upstream; các số đo của tác giả chưa được tái lập.

**Nguồn:** [README.md](https://github.com/sunface/rust-course/blob/8ff5c256b228c21131cb313f14427c0859cf6b4b/README.md) · [assets/rustlings-zh/LICENSE](https://github.com/sunface/rust-course/blob/8ff5c256b228c21131cb313f14427c0859cf6b4b/assets/rustlings-zh/LICENSE) · [.github/workflows/ci.yml](https://github.com/sunface/rust-course/blob/8ff5c256b228c21131cb313f14427c0859cf6b4b/.github/workflows/ci.yml) · [metadata GitHub](https://api.github.com/repos/sunface/rust-course).

<a id="anhkysuai-2026-11-23-michaelcade-90daysofdevops"></a>

### 90DaysOfDevOps

**Repo:** [MichaelCade/90DaysOfDevOps](https://github.com/MichaelCade/90DaysOfDevOps) · **License:** CC BY-NC-SA 4.0 · **★ 30,930 (GitHub API, 2026-11-23)**

**Mục đích:** Nhật ký học và tuyến tài nguyên DevOps/DevSecOps theo các đợt thực hành.

**Giá trị:** Kết nối nguyên tắc, quy trình và công cụ thay vì chỉ liệt kê lệnh riêng lẻ.

**Giới hạn:** Nội dung CC BY-NC-SA4.0; các phiên bản công cụ qua nhiều năm cần kiểm lại và mốc90ngày không là cam kết kết quả.

**Cách tham khảo/tích hợp:** Chọn bài theo mục tiêu, thực hành lại trên môi trường riêng và kiểm bằng bài chuyển giao; khi dùng lại nội dung phải đối chiếu giấy phép đúng phạm vi.

**Lựa chọn để đối chiếu:** [milanm/DevOps-Roadmap](https://github.com/milanm/DevOps-Roadmap) · [yeasy/docker_practice](https://github.com/yeasy/docker_practice). Đây là ứng viên so sánh theo tác vụ; mức phù hợp cần kiểm theo hồ sơ và phiên bản riêng.

**Bằng chứng:** `docs-read`, ngày 2026-11-23, commit [`2941b895eaac2056ec9431a21f3d09a60a3752f8`](https://github.com/MichaelCade/90DaysOfDevOps/commit/2941b895eaac2056ec9431a21f3d09a60a3752f8), ngày commit 2026-06-24. Đã clone và đọc chọn lọc phần giới thiệu, cách dùng, giới hạn, license, metadata manifest và CI hiện diện. Chưa kiểm đầy đủ implementation hoặc chạy upstream; các số đo của tác giả chưa được tái lập.

**Nguồn:** [README.md](https://github.com/MichaelCade/90DaysOfDevOps/blob/2941b895eaac2056ec9431a21f3d09a60a3752f8/README.md) · [LICENSE.md](https://github.com/MichaelCade/90DaysOfDevOps/blob/2941b895eaac2056ec9431a21f3d09a60a3752f8/LICENSE.md) · [.github/workflows/send-tweet.yml](https://github.com/MichaelCade/90DaysOfDevOps/blob/2941b895eaac2056ec9431a21f3d09a60a3752f8/.github/workflows/send-tweet.yml) · [metadata GitHub](https://api.github.com/repos/MichaelCade/90DaysOfDevOps).

<a id="anhkysuai-2026-11-23-wilsonfreitas-awesome-quant"></a>

### awesome-quant

**Repo:** [wilsonfreitas/awesome-quant](https://github.com/wilsonfreitas/awesome-quant) · **License:** Chưa xác lập ở phạm vi đã đọc · **★ 30,838 (GitHub API, 2026-11-23)**

**Mục đích:** Danh sách công cụ nghiên cứu định lượng, dữ liệu thị trường, backtest và quản lý rủi ro.

**Giá trị:** Có nhóm theo nhiệm vụ và hướng dẫn chọn backtesting, hữu ích định vị công cụ trước khi đọc repo gốc.

**Giới hạn:** Không thấy license chung; kết quả backtest hay tính hợp lệ dữ liệu không được suy từ việc xuất hiện trong danh sách. Chưa xác lập giấy phép chung cho nội dung chính ở phạm vi đã đọc; không suy quyền tái sử dụng từ repo công khai.

**Cách tham khảo/tích hợp:** Dùng làm chỉ mục tìm ứng viên, dẫn về nguồn gốc rồi kiểm phiên bản, giấy phép và mức bảo trì của từng lựa chọn trước tích hợp.

**Lựa chọn để đối chiếu:** [pandas-dev/pandas](https://github.com/pandas-dev/pandas) · [microsoft/qlib](https://github.com/microsoft/qlib). Đây là ứng viên so sánh theo tác vụ; mức phù hợp cần kiểm theo hồ sơ và phiên bản riêng.

**Bằng chứng:** `docs-read`, ngày 2026-11-23, commit [`c285428fce3da53b9a3b0c5ef3594310046a2b52`](https://github.com/wilsonfreitas/awesome-quant/commit/c285428fce3da53b9a3b0c5ef3594310046a2b52), ngày commit 2026-11-14. Đã clone và đọc chọn lọc phần giới thiệu, cách dùng, giới hạn, license, metadata manifest và CI hiện diện. Chưa kiểm đầy đủ implementation hoặc chạy upstream; các số đo của tác giả chưa được tái lập.

**Nguồn:** [README.md](https://github.com/wilsonfreitas/awesome-quant/blob/c285428fce3da53b9a3b0c5ef3594310046a2b52/README.md) · [pyproject.toml](https://github.com/wilsonfreitas/awesome-quant/blob/c285428fce3da53b9a3b0c5ef3594310046a2b52/pyproject.toml) · [.github/workflows/build.yml](https://github.com/wilsonfreitas/awesome-quant/blob/c285428fce3da53b9a3b0c5ef3594310046a2b52/.github/workflows/build.yml) · [metadata GitHub](https://api.github.com/repos/wilsonfreitas/awesome-quant).

<a id="anhkysuai-2026-11-23-allthingssmitty-css-protips"></a>

### css-protips

**Repo:** [AllThingsSmitty/css-protips](https://github.com/AllThingsSmitty/css-protips) · **License:** CC0-1.0 · **★ 30,305 (GitHub API, 2026-11-23)**

**Mục đích:** Tuyển tập mẹo CSS ngắn kèm ví dụ và giải thích cách dùng.

**Giá trị:** Hữu ích khi rà soát stylesheet: reset, bố cục, focus và selector được đặt thành các mục nhỏ dễ tra.

**Giới hạn:** Snippet minh họa chưa chứng minh tương thích với mọi trình duyệt hoặc hệ thống thiết kế; cần thử trên DOM và tập trình duyệt thực tế.

**Cách tham khảo/tích hợp:** Dùng làm chỉ mục tìm ứng viên, dẫn về nguồn gốc rồi kiểm phiên bản, giấy phép và mức bảo trì của từng lựa chọn trước tích hợp.

**Lựa chọn để đối chiếu:** [joshbuchea/HEAD](https://github.com/joshbuchea/HEAD) · [30-seconds/30-seconds-of-code](https://github.com/30-seconds/30-seconds-of-code). Đây là ứng viên so sánh theo tác vụ; mức phù hợp cần kiểm theo hồ sơ và phiên bản riêng.

**Bằng chứng:** `docs-read`, ngày 2026-11-23, commit [`f84d588897b99ad517ffd60c80ca7f8ca42e3c5a`](https://github.com/AllThingsSmitty/css-protips/commit/f84d588897b99ad517ffd60c80ca7f8ca42e3c5a), ngày commit 2026-09-22. Đã clone và đọc chọn lọc phần giới thiệu, cách dùng, giới hạn, license, metadata manifest và CI hiện diện. Chưa kiểm đầy đủ implementation hoặc chạy upstream; các số đo của tác giả chưa được tái lập.

**Nguồn:** [README.md](https://github.com/AllThingsSmitty/css-protips/blob/f84d588897b99ad517ffd60c80ca7f8ca42e3c5a/README.md) · [LICENSE](https://github.com/AllThingsSmitty/css-protips/blob/f84d588897b99ad517ffd60c80ca7f8ca42e3c5a/LICENSE) · [metadata GitHub](https://api.github.com/repos/AllThingsSmitty/css-protips).

<a id="anhkysuai-2026-11-23-joshbuchea-head"></a>

### HEAD

**Repo:** [joshbuchea/HEAD](https://github.com/joshbuchea/HEAD) · **License:** CC0-1.0 (tuyên bố trong README) · **★ 30,276 (GitHub API, 2026-11-23)**

**Mục đích:** Cẩm nang các phần tử và metadata trong HTML head, từ cấu hình tối thiểu đến mạng xã hội và nền tảng.

**Giá trị:** Danh mục có thứ tự khuyến nghị và mục deprecated riêng, phù hợp làm checklist khi tạo trang web.

**Giới hạn:** Không nên chép toàn bộ thẻ: nhiều mục chỉ dành cho nền tảng cụ thể và metadata thừa dễ mâu thuẫn; cần kiểm yêu cầu hiện hành của nơi xuất bản.

**Cách tham khảo/tích hợp:** Dùng làm chỉ mục tìm ứng viên, dẫn về nguồn gốc rồi kiểm phiên bản, giấy phép và mức bảo trì của từng lựa chọn trước tích hợp.

**Lựa chọn để đối chiếu:** [AllThingsSmitty/css-protips](https://github.com/AllThingsSmitty/css-protips) · [yangshun/front-end-interview-handbook](https://github.com/yangshun/front-end-interview-handbook). Đây là ứng viên so sánh theo tác vụ; mức phù hợp cần kiểm theo hồ sơ và phiên bản riêng.

**Bằng chứng:** `docs-read`, ngày 2026-11-23, commit [`de1304eeb62feb6bec90c28fc78fe29d2500d606`](https://github.com/joshbuchea/HEAD/commit/de1304eeb62feb6bec90c28fc78fe29d2500d606), ngày commit 2026-05-01. Đã clone và đọc chọn lọc phần giới thiệu, cách dùng, giới hạn, license, metadata manifest và CI hiện diện. Chưa kiểm đầy đủ implementation hoặc chạy upstream; các số đo của tác giả chưa được tái lập.

**Nguồn:** [README.md](https://github.com/joshbuchea/HEAD/blob/de1304eeb62feb6bec90c28fc78fe29d2500d606/README.md) · [.github/workflows/sync-readme.yml](https://github.com/joshbuchea/HEAD/blob/de1304eeb62feb6bec90c28fc78fe29d2500d606/.github/workflows/sync-readme.yml) · [metadata GitHub](https://api.github.com/repos/joshbuchea/HEAD).

<a id="anhkysuai-2026-11-23-realpython-python-guide"></a>

### python-guide

**Repo:** [realpython/python-guide](https://github.com/realpython/python-guide) · **License:** CC-BY-NC-SA-3.0 · **★ 29,926 (GitHub API, 2026-11-23)**

**Mục đích:** Hitchhiker’s Guide to Python: hướng dẫn thực hành cài đặt, môi trường, thư viện, kiểm thử và triển khai.

**Giá trị:** Phù hợp đọc theo vấn đề khi chuyển từ học cú pháp sang tổ chức dự án Python.

**Giới hạn:** README tự nhận work in progress và còn nhắc công cụ lịch sử; cần đối chiếu phiên bản Python/thư viện. Nội dung mang CC BY-NC-SA 3.0, có giới hạn phi thương mại.

**Cách tham khảo/tích hợp:** Chọn bài theo mục tiêu, thực hành lại trên môi trường riêng và kiểm bằng bài chuyển giao; khi dùng lại nội dung phải đối chiếu giấy phép đúng phạm vi.

**Lựa chọn để đối chiếu:** [Asabeneh/30-Days-Of-Python](https://github.com/Asabeneh/30-Days-Of-Python) · [gto76/python-cheatsheet](https://github.com/gto76/python-cheatsheet). Đây là ứng viên so sánh theo tác vụ; mức phù hợp cần kiểm theo hồ sơ và phiên bản riêng.

**Bằng chứng:** `docs-read`, ngày 2026-11-23, commit [`a4d4fa63489b4fcce30c34a9a4aba7599969afe1`](https://github.com/realpython/python-guide/commit/a4d4fa63489b4fcce30c34a9a4aba7599969afe1), ngày commit 2026-07-27. Đã clone và đọc chọn lọc phần giới thiệu, cách dùng, giới hạn, license, metadata manifest và CI hiện diện. Chưa kiểm đầy đủ implementation hoặc chạy upstream; các số đo của tác giả chưa được tái lập.

**Nguồn:** [Readme.rst](https://github.com/realpython/python-guide/blob/a4d4fa63489b4fcce30c34a9a4aba7599969afe1/Readme.rst) · [LICENSE](https://github.com/realpython/python-guide/blob/a4d4fa63489b4fcce30c34a9a4aba7599969afe1/LICENSE) · [metadata GitHub](https://api.github.com/repos/realpython/python-guide).

<a id="anhkysuai-2026-11-23-systemdesign42-system-design-academy"></a>

### system-design-academy

**Repo:** [systemdesign42/system-design-academy](https://github.com/systemdesign42/system-design-academy) · **License:** CC-BY-NC-ND-4.0 · **★ 29,830 (GitHub API, 2026-11-23)**

**Mục đích:** Chỉ mục bài học và case study về thiết kế hệ thống, được chia theo công ty và công nghệ.

**Giá trị:** Có thể dùng để tìm tình huống thực tế rồi đọc nguồn gốc, thay vì học kiến trúc chỉ qua sơ đồ chung.

**Giới hạn:** Nội dung và nguồn liên kết không đồng nghĩa kiến trúc đang vận hành; LICENSE ghi CC BY-NC-ND 4.0, hạn chế thương mại và bản phái sinh.

**Cách tham khảo/tích hợp:** Chọn bài theo mục tiêu, thực hành lại trên môi trường riêng và kiểm bằng bài chuyển giao; khi dùng lại nội dung phải đối chiếu giấy phép đúng phạm vi.

**Lựa chọn để đối chiếu:** [karanpratapsingh/system-design](https://github.com/karanpratapsingh/system-design) · [ashishps1/awesome-system-design-resources](https://github.com/ashishps1/awesome-system-design-resources). Đây là ứng viên so sánh theo tác vụ; mức phù hợp cần kiểm theo hồ sơ và phiên bản riêng.

**Bằng chứng:** `docs-read`, ngày 2026-11-23, commit [`bc306d27408b23e33f996af9ce0d4cb17afe38ad`](https://github.com/systemdesign42/system-design-academy/commit/bc306d27408b23e33f996af9ce0d4cb17afe38ad), ngày commit 2026-11-20. Đã clone và đọc chọn lọc phần giới thiệu, cách dùng, giới hạn, license, metadata manifest và CI hiện diện. Chưa kiểm đầy đủ implementation hoặc chạy upstream; các số đo của tác giả chưa được tái lập.

**Nguồn:** [README.md](https://github.com/systemdesign42/system-design-academy/blob/bc306d27408b23e33f996af9ce0d4cb17afe38ad/README.md) · [LICENSE.md](https://github.com/systemdesign42/system-design-academy/blob/bc306d27408b23e33f996af9ce0d4cb17afe38ad/LICENSE.md) · [metadata GitHub](https://api.github.com/repos/systemdesign42/system-design-academy).

<a id="anhkysuai-2026-11-23-viatsko-awesome-vscode"></a>

### awesome-vscode

**Repo:** [viatsko/awesome-vscode](https://github.com/viatsko/awesome-vscode) · **License:** CC0-1.0 · **★ 29,263 (GitHub API, 2026-11-23)**

**Mục đích:** Danh sách extension, cấu hình và tài nguyên cho Visual Studio Code theo ngôn ngữ và tác vụ.

**Giá trị:** Phân nhóm lint, IntelliSense, migration và theme giúp rút ngắn bước tìm công cụ phù hợp.

**Giới hạn:** CC0 áp dụng cho danh sách; từng extension có quyền truy cập, nhà phát hành và giấy phép riêng. Link-check CI không chứng minh extension an toàn hoặc còn tương thích.

**Cách tham khảo/tích hợp:** Dùng làm chỉ mục tìm ứng viên, dẫn về nguồn gốc rồi kiểm phiên bản, giấy phép và mức bảo trì của từng lựa chọn trước tích hợp.

**Lựa chọn để đối chiếu:** [microsoft/vscode](https://github.com/microsoft/vscode) · [PatrickJS/awesome-cursorrules](https://github.com/PatrickJS/awesome-cursorrules). Đây là ứng viên so sánh theo tác vụ; mức phù hợp cần kiểm theo hồ sơ và phiên bản riêng.

**Bằng chứng:** `docs-read`, ngày 2026-11-23, commit [`9c3bf848287d3967a744e7c057ea49ec9e89b396`](https://github.com/viatsko/awesome-vscode/commit/9c3bf848287d3967a744e7c057ea49ec9e89b396), ngày commit 2026-06-21. Đã clone và đọc chọn lọc phần giới thiệu, cách dùng, giới hạn, license, metadata manifest và CI hiện diện. Chưa kiểm đầy đủ implementation hoặc chạy upstream; các số đo của tác giả chưa được tái lập.

**Nguồn:** [README.md](https://github.com/viatsko/awesome-vscode/blob/9c3bf848287d3967a744e7c057ea49ec9e89b396/README.md) · [LICENSE](https://github.com/viatsko/awesome-vscode/blob/9c3bf848287d3967a744e7c057ea49ec9e89b396/LICENSE) · [package.json](https://github.com/viatsko/awesome-vscode/blob/9c3bf848287d3967a744e7c057ea49ec9e89b396/package.json) · [.github/workflows/links.yml](https://github.com/viatsko/awesome-vscode/blob/9c3bf848287d3967a744e7c057ea49ec9e89b396/.github/workflows/links.yml) · [metadata GitHub](https://api.github.com/repos/viatsko/awesome-vscode).

<a id="anhkysuai-2026-11-23-ashishps1-awesome-low-level-design"></a>

### awesome-low-level-design

**Repo:** [ashishps1/awesome-low-level-design](https://github.com/ashishps1/awesome-low-level-design) · **License:** GPL-3.0 · **★ 28,222 (GitHub API, 2026-11-23)**

**Mục đích:** Tài nguyên học thiết kế hướng đối tượng, UML, concurrency và luyện phỏng vấn low-level design.

**Giá trị:** Trình tự từ OOP đến quan hệ lớp và nguyên tắc thiết kế giúp tạo lộ trình học có cấu trúc.

**Giới hạn:** Nhiều bài học nằm trên website ngoài; giấy phép GPL của repo không cấp quyền cho toàn bộ nguồn liên kết, và học thuộc pattern chưa chứng minh thiết kế phù hợp thực tế.

**Cách tham khảo/tích hợp:** Dùng làm chỉ mục tìm ứng viên, dẫn về nguồn gốc rồi kiểm phiên bản, giấy phép và mức bảo trì của từng lựa chọn trước tích hợp.

**Lựa chọn để đối chiếu:** [faif/python-patterns](https://github.com/faif/python-patterns) · [huihut/interview](https://github.com/huihut/interview). Đây là ứng viên so sánh theo tác vụ; mức phù hợp cần kiểm theo hồ sơ và phiên bản riêng.

**Bằng chứng:** `docs-read`, ngày 2026-11-23, commit [`31595db8c21a8f7785b2ef45d90f16fd8053abad`](https://github.com/ashishps1/awesome-low-level-design/commit/31595db8c21a8f7785b2ef45d90f16fd8053abad), ngày commit 2026-08-19. Đã clone và đọc chọn lọc phần giới thiệu, cách dùng, giới hạn, license, metadata manifest và CI hiện diện. Chưa kiểm đầy đủ implementation hoặc chạy upstream; các số đo của tác giả chưa được tái lập.

**Nguồn:** [README.md](https://github.com/ashishps1/awesome-low-level-design/blob/31595db8c21a8f7785b2ef45d90f16fd8053abad/README.md) · [LICENSE](https://github.com/ashishps1/awesome-low-level-design/blob/31595db8c21a8f7785b2ef45d90f16fd8053abad/LICENSE) · [metadata GitHub](https://api.github.com/repos/ashishps1/awesome-low-level-design).

<a id="anhkysuai-2026-11-23-kdeldycke-awesome-falsehood"></a>

### awesome-falsehood

**Repo:** [kdeldycke/awesome-falsehood](https://github.com/kdeldycke/awesome-falsehood) · **License:** CC0-1.0 · **★ 27,887 (GitHub API, 2026-11-23)**

**Mục đích:** Danh sách các giả định sai thường gặp khi lập trình về tên, email, thời gian, địa lý và dữ liệu đời thực.

**Giá trị:** Hữu ích để mở rộng trường hợp biên khi thiết kế schema, validation và bộ kiểm thử.

**Giới hạn:** Các bài liên kết là ví dụ phản chứng theo bối cảnh; không nên chuyển chúng thành một bộ regex hoặc quy tắc chung mà chưa đọc nguồn cụ thể.

**Cách tham khảo/tích hợp:** Dùng làm chỉ mục tìm ứng viên, dẫn về nguồn gốc rồi kiểm phiên bản, giấy phép và mức bảo trì của từng lựa chọn trước tích hợp.

**Lựa chọn để đối chiếu:** [charlax/professional-programming](https://github.com/charlax/professional-programming) · [jwasham/coding-interview-university](https://github.com/jwasham/coding-interview-university). Đây là ứng viên so sánh theo tác vụ; mức phù hợp cần kiểm theo hồ sơ và phiên bản riêng.

**Bằng chứng:** `docs-read`, ngày 2026-11-23, commit [`0b1aaba9cf2ce879b2188a93ea8ee46604a62304`](https://github.com/kdeldycke/awesome-falsehood/commit/0b1aaba9cf2ce879b2188a93ea8ee46604a62304), ngày commit 2026-10-08. Đã clone và đọc chọn lọc phần giới thiệu, cách dùng, giới hạn, license, metadata manifest và CI hiện diện. Chưa kiểm đầy đủ implementation hoặc chạy upstream; các số đo của tác giả chưa được tái lập.

**Nguồn:** [readme.md](https://github.com/kdeldycke/awesome-falsehood/blob/0b1aaba9cf2ce879b2188a93ea8ee46604a62304/readme.md) · [license](https://github.com/kdeldycke/awesome-falsehood/blob/0b1aaba9cf2ce879b2188a93ea8ee46604a62304/license) · [pyproject.toml](https://github.com/kdeldycke/awesome-falsehood/blob/0b1aaba9cf2ce879b2188a93ea8ee46604a62304/pyproject.toml) · [.github/workflows/docs.yaml](https://github.com/kdeldycke/awesome-falsehood/blob/0b1aaba9cf2ce879b2188a93ea8ee46604a62304/.github/workflows/docs.yaml) · [metadata GitHub](https://api.github.com/repos/kdeldycke/awesome-falsehood).

<a id="anhkysuai-2026-11-23-oi-wiki-oi-wiki"></a>

### OI-wiki

**Repo:** [OI-wiki/OI-wiki](https://github.com/OI-wiki/OI-wiki) · **License:** CC-BY-SA-4.0 + SATA (nội dung ngoài mã); mã cần kiểm riêng · **★ 27,219 (GitHub API, 2026-11-23)**

**Mục đích:** Wiki tiếng Trung về thuật toán và lập trình thi đấu, có tài liệu, ví dụ và quy trình xây site.

**Giá trị:** Phạm vi kiến thức rộng, liên kết giữa chủ đề giúp học từ cơ bản đến bài toán thi đấu.

**Giới hạn:** README thừa nhận có trang chưa hoàn thiện; nội dung ngoài mã áp dụng CC BY-SA 4.0 kèm SATA, còn package build ghi UNLICENSED. Cần phân biệt quyền của văn bản, ví dụ mã và nguồn trích dẫn khi tái sử dụng.

**Cách tham khảo/tích hợp:** Chọn bài theo mục tiêu, thực hành lại trên môi trường riêng và kiểm bằng bài chuyển giao; khi dùng lại nội dung phải đối chiếu giấy phép đúng phạm vi.

**Lựa chọn để đối chiếu:** [TheAlgorithms/C-Plus-Plus](https://github.com/TheAlgorithms/C-Plus-Plus) · [TheAlgorithms/Java](https://github.com/TheAlgorithms/Java). Đây là ứng viên so sánh theo tác vụ; mức phù hợp cần kiểm theo hồ sơ và phiên bản riêng.

**Bằng chứng:** `docs-read`, ngày 2026-11-23, commit [`f80d6d6f780ced1c216c71ad96cabaea9308a62c`](https://github.com/OI-wiki/OI-wiki/commit/f80d6d6f780ced1c216c71ad96cabaea9308a62c), ngày commit 2026-11-19. Đã clone và đọc chọn lọc phần giới thiệu, cách dùng, giới hạn, license, metadata manifest và CI hiện diện. Chưa kiểm đầy đủ implementation hoặc chạy upstream; các số đo của tác giả chưa được tái lập.

**Nguồn:** [README.md](https://github.com/OI-wiki/OI-wiki/blob/f80d6d6f780ced1c216c71ad96cabaea9308a62c/README.md) · [package.json](https://github.com/OI-wiki/OI-wiki/blob/f80d6d6f780ced1c216c71ad96cabaea9308a62c/package.json) · [pyproject.toml](https://github.com/OI-wiki/OI-wiki/blob/f80d6d6f780ced1c216c71ad96cabaea9308a62c/pyproject.toml) · [.github/workflows/test.yml](https://github.com/OI-wiki/OI-wiki/blob/f80d6d6f780ced1c216c71ad96cabaea9308a62c/.github/workflows/test.yml) · [metadata GitHub](https://api.github.com/repos/OI-wiki/OI-wiki).

<a id="anhkysuai-2026-11-23-alexpate-awesome-design-systems"></a>

### Awesome Design Systems (alexpate)

**Repo:** [alexpate/awesome-design-systems](https://github.com/alexpate/awesome-design-systems) · **License:** Unlicense · **★ 26,418 (GitHub API, 2026-11-23)**

**Mục đích:** Danh mục design system với chỉ báo component, giọng điệu, bộ thiết kế và mã nguồn.

**Giá trị:** Các cột so sánh giúp tìm ví dụ phù hợp cho quy tắc giao diện và tài liệu thiết kế.

**Giới hạn:** Unlicense của danh sách không bao gồm logo, Figma kit hoặc component của thương hiệu được dẫn; dấu có mã nguồn chưa chứng minh được phép dùng lại.

**Cách tham khảo/tích hợp:** Dùng làm chỉ mục tìm ứng viên, dẫn về nguồn gốc rồi kiểm phiên bản, giấy phép và mức bảo trì của từng lựa chọn trước tích hợp.

**Lựa chọn để đối chiếu:** [viatsko/awesome-vscode](https://github.com/viatsko/awesome-vscode) · [joshbuchea/HEAD](https://github.com/joshbuchea/HEAD). Đây là ứng viên so sánh theo tác vụ; mức phù hợp cần kiểm theo hồ sơ và phiên bản riêng.

**Bằng chứng:** `docs-read`, ngày 2026-11-23, commit [`5f21c294018a460d9d51118ca21c463a37838209`](https://github.com/alexpate/awesome-design-systems/commit/5f21c294018a460d9d51118ca21c463a37838209), ngày commit 2026-11-13. Đã clone và đọc chọn lọc phần giới thiệu, cách dùng, giới hạn, license, metadata manifest và CI hiện diện. Chưa kiểm đầy đủ implementation hoặc chạy upstream; các số đo của tác giả chưa được tái lập.

**Nguồn:** [README.md](https://github.com/alexpate/awesome-design-systems/blob/5f21c294018a460d9d51118ca21c463a37838209/README.md) · [LICENSE](https://github.com/alexpate/awesome-design-systems/blob/5f21c294018a460d9d51118ca21c463a37838209/LICENSE) · [metadata GitHub](https://api.github.com/repos/alexpate/awesome-design-systems).

<a id="anhkysuai-2026-11-23-matteocrippa-awesome-swift"></a>

### awesome-swift

**Repo:** [matteocrippa/awesome-swift](https://github.com/matteocrippa/awesome-swift) · **License:** CC0-1.0 · **★ 26,398 (GitHub API, 2026-11-23)**

**Mục đích:** Chỉ mục thư viện và tài nguyên Swift theo chức năng, có dữ liệu cấu trúc contents.json.

**Giá trị:** Cấu trúc dữ liệu nguồn và quy trình kiểm link/schema thuận lợi cho tìm kiếm hoặc cập nhật danh sách.

**Giới hạn:** Số dự án và ngày trong README là metadata của danh sách; từng thư viện cần kiểm nền tảng, phiên bản Swift và giấy phép riêng.

**Cách tham khảo/tích hợp:** Dùng làm chỉ mục tìm ứng viên, dẫn về nguồn gốc rồi kiểm phiên bản, giấy phép và mức bảo trì của từng lựa chọn trước tích hợp.

**Lựa chọn để đối chiếu:** [vsouza/awesome-ios](https://github.com/vsouza/awesome-ios) · [dkhamsing/open-source-ios-apps](https://github.com/dkhamsing/open-source-ios-apps). Đây là ứng viên so sánh theo tác vụ; mức phù hợp cần kiểm theo hồ sơ và phiên bản riêng.

**Bằng chứng:** `docs-read`, ngày 2026-11-23, commit [`c18cbf89da283178c038b39f7eb402e0b144b9ec`](https://github.com/matteocrippa/awesome-swift/commit/c18cbf89da283178c038b39f7eb402e0b144b9ec), ngày commit 2026-11-11. Đã clone và đọc chọn lọc phần giới thiệu, cách dùng, giới hạn, license, metadata manifest và CI hiện diện. Chưa kiểm đầy đủ implementation hoặc chạy upstream; các số đo của tác giả chưa được tái lập.

**Nguồn:** [README.md](https://github.com/matteocrippa/awesome-swift/blob/c18cbf89da283178c038b39f7eb402e0b144b9ec/README.md) · [LICENSE](https://github.com/matteocrippa/awesome-swift/blob/c18cbf89da283178c038b39f7eb402e0b144b9ec/LICENSE) · [.github/workflows/pr.yml](https://github.com/matteocrippa/awesome-swift/blob/c18cbf89da283178c038b39f7eb402e0b144b9ec/.github/workflows/pr.yml) · [metadata GitHub](https://api.github.com/repos/matteocrippa/awesome-swift).

<a id="anhkysuai-2026-11-23-yeasy-docker_practice"></a>

### docker_practice

**Repo:** [yeasy/docker_practice](https://github.com/yeasy/docker_practice) · **License:** CC-BY-NC-SA-4.0 · **★ 26,387 (GitHub API, 2026-11-23)**

**Mục đích:** Sách tiếng Trung về Docker, từ khái niệm container đến mạng, lưu trữ, bảo mật và vận hành.

**Giá trị:** Có lộ trình chương, ví dụ thực hành và bộ kiểm tra tài liệu/canonical examples trong cấu hình CI.

**Giới hạn:** Nội dung CC BY-NC-SA 4.0; lệnh mẫu cần đối chiếu phiên bản Docker và môi trường đích. CI chỉ được đọc cấu hình, chưa chạy trong lượt nghiên cứu.

**Cách tham khảo/tích hợp:** Chọn bài theo mục tiêu, thực hành lại trên môi trường riêng và kiểm bằng bài chuyển giao; khi dùng lại nội dung phải đối chiếu giấy phép đúng phạm vi.

**Lựa chọn để đối chiếu:** [docker/awesome-compose](https://github.com/docker/awesome-compose) · [MichaelCade/90DaysOfDevOps](https://github.com/MichaelCade/90DaysOfDevOps). Đây là ứng viên so sánh theo tác vụ; mức phù hợp cần kiểm theo hồ sơ và phiên bản riêng.

**Bằng chứng:** `docs-read`, ngày 2026-11-23, commit [`7f8424a7c5cf000860ad88ed861030c773d9d93a`](https://github.com/yeasy/docker_practice/commit/7f8424a7c5cf000860ad88ed861030c773d9d93a), ngày commit 2026-11-11. Đã clone và đọc chọn lọc phần giới thiệu, cách dùng, giới hạn, license, metadata manifest và CI hiện diện. Chưa kiểm đầy đủ implementation hoặc chạy upstream; các số đo của tác giả chưa được tái lập.

**Nguồn:** [README.md](https://github.com/yeasy/docker_practice/blob/7f8424a7c5cf000860ad88ed861030c773d9d93a/README.md) · [package.json](https://github.com/yeasy/docker_practice/blob/7f8424a7c5cf000860ad88ed861030c773d9d93a/package.json) · [.github/workflows/ci.yaml](https://github.com/yeasy/docker_practice/blob/7f8424a7c5cf000860ad88ed861030c773d9d93a/.github/workflows/ci.yaml) · [metadata GitHub](https://api.github.com/repos/yeasy/docker_practice).

<a id="anhkysuai-2026-11-23-keon-algorithms"></a>

### algorithms

**Repo:** [keon/algorithms](https://github.com/keon/algorithms) · **License:** MIT · **★ 25,611 (GitHub API, 2026-11-23)**

**Mục đích:** Các triển khai Python ngắn cho thuật toán và cấu trúc dữ liệu, kèm ví dụ sử dụng.

**Giá trị:** Cách chia mỗi thuật toán thành tệp riêng cùng chú thích độ phức tạp thuận tiện cho học và đối chiếu cách giải.

**Giới hạn:** Mục tiêu là ví dụ giáo dục; chưa kiểm độ đúng, hiệu năng hoặc API của gói PyPI tại lượt này. Manifest yêu cầu Python từ 3.10.

**Cách tham khảo/tích hợp:** Chọn bài theo mục tiêu, thực hành lại trên môi trường riêng và kiểm bằng bài chuyển giao; khi dùng lại nội dung phải đối chiếu giấy phép đúng phạm vi.

**Lựa chọn để đối chiếu:** [TheAlgorithms/Python](https://github.com/TheAlgorithms/Python) · [norvig/pytudes](https://github.com/norvig/pytudes). Đây là ứng viên so sánh theo tác vụ; mức phù hợp cần kiểm theo hồ sơ và phiên bản riêng.

**Bằng chứng:** `docs-read`, ngày 2026-11-23, commit [`bd1d152f9ec7331c69be662831610b003b10fc7a`](https://github.com/keon/algorithms/commit/bd1d152f9ec7331c69be662831610b003b10fc7a), ngày commit 2026-09-24. Đã clone và đọc chọn lọc phần giới thiệu, cách dùng, giới hạn, license, metadata manifest và CI hiện diện. Chưa kiểm đầy đủ implementation hoặc chạy upstream; các số đo của tác giả chưa được tái lập.

**Nguồn:** [README.md](https://github.com/keon/algorithms/blob/bd1d152f9ec7331c69be662831610b003b10fc7a/README.md) · [LICENSE](https://github.com/keon/algorithms/blob/bd1d152f9ec7331c69be662831610b003b10fc7a/LICENSE) · [pyproject.toml](https://github.com/keon/algorithms/blob/bd1d152f9ec7331c69be662831610b003b10fc7a/pyproject.toml) · [.github/workflows/publish.yml](https://github.com/keon/algorithms/blob/bd1d152f9ec7331c69be662831610b003b10fc7a/.github/workflows/publish.yml) · [metadata GitHub](https://api.github.com/repos/keon/algorithms).

<a id="anhkysuai-2026-11-23-javascript-tutorial-en.javascript.info"></a>

### en.javascript.info

**Repo:** [javascript-tutorial/en.javascript.info](https://github.com/javascript-tutorial/en.javascript.info) · **License:** Giấy phép nội dung dựa trên CC-BY-NC-4.0; xem LICENSE.md · **★ 25,536 (GitHub API, 2026-11-23)**

**Mục đích:** Nguồn nội dung tiếng Anh của Modern JavaScript Tutorial, chia bài học và bài tập theo thư mục.

**Giá trị:** Cấu trúc bài và bài tập hỗ trợ học JavaScript có trình tự, đồng thời có quy trình đóng góp và bản dịch.

**Giới hạn:** LICENSE cho đọc miễn phí nhưng yêu cầu liên hệ khi dùng theo cách khác và dựa trên CC BY-NC; không coi đây là giấy phép phần mềm tự do cho toàn bộ sách.

**Cách tham khảo/tích hợp:** Chọn bài theo mục tiêu, thực hành lại trên môi trường riêng và kiểm bằng bài chuyển giao; khi dùng lại nội dung phải đối chiếu giấy phép đúng phạm vi.

**Lựa chọn để đối chiếu:** [Asabeneh/30-Days-Of-JavaScript](https://github.com/Asabeneh/30-Days-Of-JavaScript) · [leonardomso/33-js-concepts](https://github.com/leonardomso/33-js-concepts). Đây là ứng viên so sánh theo tác vụ; mức phù hợp cần kiểm theo hồ sơ và phiên bản riêng.

**Bằng chứng:** `docs-read`, ngày 2026-11-23, commit [`20208769e528337949e946f526534d61d38bac47`](https://github.com/javascript-tutorial/en.javascript.info/commit/20208769e528337949e946f526534d61d38bac47), ngày commit 2026-07-25. Đã clone và đọc chọn lọc phần giới thiệu, cách dùng, giới hạn, license, metadata manifest và CI hiện diện. Chưa kiểm đầy đủ implementation hoặc chạy upstream; các số đo của tác giả chưa được tái lập.

**Nguồn:** [README.md](https://github.com/javascript-tutorial/en.javascript.info/blob/20208769e528337949e946f526534d61d38bac47/README.md) · [LICENSE.md](https://github.com/javascript-tutorial/en.javascript.info/blob/20208769e528337949e946f526534d61d38bac47/LICENSE.md) · [metadata GitHub](https://api.github.com/repos/javascript-tutorial/en.javascript.info).

<a id="anhkysuai-2026-11-23-awesome-dsh-plugin-awesome-dsh-plugin"></a>

### awesome-dsh-plugin

**Repo:** [awesome-dsh-plugin/awesome-dsh-plugin](https://github.com/awesome-dsh-plugin/awesome-dsh-plugin) · **License:** CC0-1.0 · **★ 25,478 (GitHub API, 2026-11-23)**

**Mục đích:** Danh sách plugin cộng đồng cho DeepSeek Harness, có dữ liệu plugin và kiểm tra manifest.

**Giá trị:** Phân nhóm UI, model, công cụ và workflow giúp tìm phần mở rộng theo nhu cầu; cấu trúc dữ liệu có thể tham khảo cho kho plugin.

**Giới hạn:** CC0 chỉ cấp quyền với danh sách; plugin có thể chạy công cụ hoặc thay agent loop nên phải đọc riêng mã, quyền và phiên bản DSH hỗ trợ.

**Cách tham khảo/tích hợp:** Dùng làm chỉ mục tìm ứng viên, dẫn về nguồn gốc rồi kiểm phiên bản, giấy phép và mức bảo trì của từng lựa chọn trước tích hợp.

**Lựa chọn để đối chiếu:** [PatrickJS/awesome-cursorrules](https://github.com/PatrickJS/awesome-cursorrules) · [VoltAgent/awesome-agent-skills](https://github.com/VoltAgent/awesome-agent-skills). Đây là ứng viên so sánh theo tác vụ; mức phù hợp cần kiểm theo hồ sơ và phiên bản riêng.

**Bằng chứng:** `docs-read`, ngày 2026-11-23, commit [`1cfebf33f8f7f3a363507fd1609cbb6cb6bc6c37`](https://github.com/awesome-dsh-plugin/awesome-dsh-plugin/commit/1cfebf33f8f7f3a363507fd1609cbb6cb6bc6c37), ngày commit 2026-11-22. Đã clone và đọc chọn lọc phần giới thiệu, cách dùng, giới hạn, license, metadata manifest và CI hiện diện. Chưa kiểm đầy đủ implementation hoặc chạy upstream; các số đo của tác giả chưa được tái lập.

**Nguồn:** [README.md](https://github.com/awesome-dsh-plugin/awesome-dsh-plugin/blob/1cfebf33f8f7f3a363507fd1609cbb6cb6bc6c37/README.md) · [LICENSE](https://github.com/awesome-dsh-plugin/awesome-dsh-plugin/blob/1cfebf33f8f7f3a363507fd1609cbb6cb6bc6c37/LICENSE) · [package.json](https://github.com/awesome-dsh-plugin/awesome-dsh-plugin/blob/1cfebf33f8f7f3a363507fd1609cbb6cb6bc6c37/package.json) · [.github/workflows/pr-check.yml](https://github.com/awesome-dsh-plugin/awesome-dsh-plugin/blob/1cfebf33f8f7f3a363507fd1609cbb6cb6bc6c37/.github/workflows/pr-check.yml) · [metadata GitHub](https://api.github.com/repos/awesome-dsh-plugin/awesome-dsh-plugin).

<a id="anhkysuai-2026-11-23-norvig-pytudes"></a>

### pytudes

**Repo:** [norvig/pytudes](https://github.com/norvig/pytudes) · **License:** MIT · **★ 24,430 (GitHub API, 2026-11-23)**

**Mục đích:** Các bài luyện Python của Peter Norvig, thường dưới dạng notebook hoặc chương trình ngắn.

**Giá trị:** Tập trung rèn cách suy nghĩ và diễn đạt lời giải; phù hợp người đã có nền tảng muốn đọc cách phân tích vấn đề.

**Giới hạn:** README phân biệt học nghề lập trình với hướng dẫn cài ứng dụng; nhiều ví dụ không nhằm production, môi trường notebook và dữ liệu cần kiểm từng bài.

**Cách tham khảo/tích hợp:** Chọn bài theo mục tiêu, thực hành lại trên môi trường riêng và kiểm bằng bài chuyển giao; khi dùng lại nội dung phải đối chiếu giấy phép đúng phạm vi.

**Lựa chọn để đối chiếu:** [keon/algorithms](https://github.com/keon/algorithms) · [quii/learn-go-with-tests](https://github.com/quii/learn-go-with-tests). Đây là ứng viên so sánh theo tác vụ; mức phù hợp cần kiểm theo hồ sơ và phiên bản riêng.

**Bằng chứng:** `docs-read`, ngày 2026-11-23, commit [`3b4c5dd5fcec2dd48d34b8e4c03cea245ff039d7`](https://github.com/norvig/pytudes/commit/3b4c5dd5fcec2dd48d34b8e4c03cea245ff039d7), ngày commit 2026-11-20. Đã clone và đọc chọn lọc phần giới thiệu, cách dùng, giới hạn, license, metadata manifest và CI hiện diện. Chưa kiểm đầy đủ implementation hoặc chạy upstream; các số đo của tác giả chưa được tái lập.

**Nguồn:** [README.md](https://github.com/norvig/pytudes/blob/3b4c5dd5fcec2dd48d34b8e4c03cea245ff039d7/README.md) · [LICENSE](https://github.com/norvig/pytudes/blob/3b4c5dd5fcec2dd48d34b8e4c03cea245ff039d7/LICENSE) · [.github/workflows/on-file-change.yml](https://github.com/norvig/pytudes/blob/3b4c5dd5fcec2dd48d34b8e4c03cea245ff039d7/.github/workflows/on-file-change.yml) · [metadata GitHub](https://api.github.com/repos/norvig/pytudes).

<a id="anhkysuai-2026-11-23-vonng-ddia"></a>

### ddia

**Repo:** [Vonng/ddia](https://github.com/Vonng/ddia) · **License:** CC-BY-4.0 (tuyên bố repo); quyền nguyên tác cần đối chiếu · **★ 23,989 (GitHub API, 2026-11-23)**

**Mục đích:** Bản dịch tiếng Trung của Designing Data-Intensive Applications, gồm nội dung cho các ấn bản.

**Giá trị:** Nguồn đọc bổ trợ về lưu trữ và hệ phân tán, có cấu trúc chương và lịch sử hiệu đính cộng đồng.

**Giới hạn:** LICENSE repo ghi CC BY 4.0 nhưng tuyên bố pháp lý trong README giới hạn bản dịch cho học/nghiên cứu, không phát hành công khai hay thương mại và dành quyền khác cho tác giả/nhà xuất bản; cần giải quyết mâu thuẫn này trước tái sử dụng.

**Cách tham khảo/tích hợp:** Chọn bài theo mục tiêu, thực hành lại trên môi trường riêng và kiểm bằng bài chuyển giao; khi dùng lại nội dung phải đối chiếu giấy phép đúng phạm vi.

**Lựa chọn để đối chiếu:** [karanpratapsingh/system-design](https://github.com/karanpratapsingh/system-design) · [systemdesign42/system-design-academy](https://github.com/systemdesign42/system-design-academy). Đây là ứng viên so sánh theo tác vụ; mức phù hợp cần kiểm theo hồ sơ và phiên bản riêng.

**Bằng chứng:** `docs-read`, ngày 2026-11-23, commit [`bd8ef56e032f57184080d1418d8d9ae8dc3d483c`](https://github.com/Vonng/ddia/commit/bd8ef56e032f57184080d1418d8d9ae8dc3d483c), ngày commit 2026-11-07. Đã clone và đọc chọn lọc phần giới thiệu, cách dùng, giới hạn, license, metadata manifest và CI hiện diện. Chưa kiểm đầy đủ implementation hoặc chạy upstream; các số đo của tác giả chưa được tái lập.

**Nguồn:** [README.md](https://github.com/Vonng/ddia/blob/bd8ef56e032f57184080d1418d8d9ae8dc3d483c/README.md) · [LICENSE](https://github.com/Vonng/ddia/blob/bd8ef56e032f57184080d1418d8d9ae8dc3d483c/LICENSE) · [go.mod](https://github.com/Vonng/ddia/blob/bd8ef56e032f57184080d1418d8d9ae8dc3d483c/go.mod) · [.github/workflows/repository-cards.yml](https://github.com/Vonng/ddia/blob/bd8ef56e032f57184080d1418d8d9ae8dc3d483c/.github/workflows/repository-cards.yml) · [metadata GitHub](https://api.github.com/repos/Vonng/ddia).

<a id="anhkysuai-2026-11-23-quii-learn-go-with-tests"></a>

### learn-go-with-tests

**Repo:** [quii/learn-go-with-tests](https://github.com/quii/learn-go-with-tests) · **License:** MIT · **★ 23,972 (GitHub API, 2026-11-23)**

**Mục đích:** Giáo trình Go học qua test-driven development, từ ngôn ngữ cơ bản tới xây ứng dụng.

**Giá trị:** Bài học gắn khái niệm với vòng viết test và cải tiến thiết kế, có nhiều định dạng đọc và bản dịch.

**Giới hạn:** Cần thực hành bài chuyển giao để kiểm hiểu biết; cấu hình build sách không chứng minh mọi ví dụ đúng trên mọi phiên bản Go, và bản dịch có thể lệch tiến độ.

**Cách tham khảo/tích hợp:** Chọn bài theo mục tiêu, thực hành lại trên môi trường riêng và kiểm bằng bài chuyển giao; khi dùng lại nội dung phải đối chiếu giấy phép đúng phạm vi.

**Lựa chọn để đối chiếu:** [golang/tour](https://github.com/golang/tour) · [google/comprehensive-rust](https://github.com/google/comprehensive-rust). Đây là ứng viên so sánh theo tác vụ; mức phù hợp cần kiểm theo hồ sơ và phiên bản riêng.

**Bằng chứng:** `docs-read`, ngày 2026-11-23, commit [`592e9f747e9e851af40eb0a5cb0ac4fe86ef18a6`](https://github.com/quii/learn-go-with-tests/commit/592e9f747e9e851af40eb0a5cb0ac4fe86ef18a6), ngày commit 2026-10-26. Đã clone và đọc chọn lọc phần giới thiệu, cách dùng, giới hạn, license, metadata manifest và CI hiện diện. Chưa kiểm đầy đủ implementation hoặc chạy upstream; các số đo của tác giả chưa được tái lập.

**Nguồn:** [README.md](https://github.com/quii/learn-go-with-tests/blob/592e9f747e9e851af40eb0a5cb0ac4fe86ef18a6/README.md) · [LICENSE.md](https://github.com/quii/learn-go-with-tests/blob/592e9f747e9e851af40eb0a5cb0ac4fe86ef18a6/LICENSE.md) · [go.mod](https://github.com/quii/learn-go-with-tests/blob/592e9f747e9e851af40eb0a5cb0ac4fe86ef18a6/go.mod) · [.github/workflows/go.yml](https://github.com/quii/learn-go-with-tests/blob/592e9f747e9e851af40eb0a5cb0ac4fe86ef18a6/.github/workflows/go.yml) · [metadata GitHub](https://api.github.com/repos/quii/learn-go-with-tests).

<a id="anhkysuai-2026-11-23-anderspitman-awesome-tunneling"></a>

### awesome-tunneling

**Repo:** [anderspitman/awesome-tunneling](https://github.com/anderspitman/awesome-tunneling) · **License:** Chưa xác lập ở phạm vi đã đọc · **★ 22,073 (GitHub API, 2026-11-23)**

**Mục đích:** Danh sách công cụ tunneling và overlay network, chú trọng khả năng tự host.

**Giá trị:** Phân nhóm nguồn mở, thương mại và mạng overlay giúp tìm lựa chọn theo cách triển khai.

**Giới hạn:** Tiêu chí sao GitHub hoặc khách hàng trong README không phải kiểm toán bảo mật; thiếu giấy phép chung ở gốc đã đọc và từng công cụ cần kiểm xác thực, mã hóa, quyền nhà cung cấp. Chưa xác lập giấy phép chung cho nội dung chính ở phạm vi đã đọc; không suy quyền tái sử dụng từ repo công khai.

**Cách tham khảo/tích hợp:** Dùng làm chỉ mục tìm ứng viên, dẫn về nguồn gốc rồi kiểm phiên bản, giấy phép và mức bảo trì của từng lựa chọn trước tích hợp.

**Lựa chọn để đối chiếu:** [fatedier/frp](https://github.com/fatedier/frp) · [tailscale/tailscale](https://github.com/tailscale/tailscale). Đây là ứng viên so sánh theo tác vụ; mức phù hợp cần kiểm theo hồ sơ và phiên bản riêng.

**Bằng chứng:** `docs-read`, ngày 2026-11-23, commit [`f28b57dca0824ed33d4129c8ef1b9c080051a177`](https://github.com/anderspitman/awesome-tunneling/commit/f28b57dca0824ed33d4129c8ef1b9c080051a177), ngày commit 2026-11-17. Đã clone và đọc chọn lọc phần giới thiệu, cách dùng, giới hạn, license, metadata manifest và CI hiện diện. Chưa kiểm đầy đủ implementation hoặc chạy upstream; các số đo của tác giả chưa được tái lập.

**Nguồn:** [README.md](https://github.com/anderspitman/awesome-tunneling/blob/f28b57dca0824ed33d4129c8ef1b9c080051a177/README.md) · [metadata GitHub](https://api.github.com/repos/anderspitman/awesome-tunneling).

<a id="anhkysuai-2026-11-23-matiassingers-awesome-readme"></a>

### awesome-readme

**Repo:** [matiassingers/awesome-readme](https://github.com/matiassingers/awesome-readme) · **License:** CC0-1.0 (tuyên bố trong README) · **★ 21,760 (GitHub API, 2026-11-23)**

**Mục đích:** Danh sách README tiêu biểu cùng bài viết, ví dụ kiến trúc và công cụ tạo hình minh họa.

**Giá trị:** Giúp chọn bố cục trình bày vấn đề, cài đặt, ảnh và kiến trúc khi viết tài liệu dự án.

**Giới hạn:** Chất lượng trình bày không chứng minh chất lượng phần mềm; CC0 của danh sách không bao gồm tài sản và văn bản ở các repo được dẫn.

**Cách tham khảo/tích hợp:** Dùng làm chỉ mục tìm ứng viên, dẫn về nguồn gốc rồi kiểm phiên bản, giấy phép và mức bảo trì của từng lựa chọn trước tích hợp.

**Lựa chọn để đối chiếu:** [github/opensource.guide](https://github.com/github/opensource.guide) · [abhisheknaiidu/awesome-github-profile-readme](https://github.com/abhisheknaiidu/awesome-github-profile-readme). Đây là ứng viên so sánh theo tác vụ; mức phù hợp cần kiểm theo hồ sơ và phiên bản riêng.

**Bằng chứng:** `docs-read`, ngày 2026-11-23, commit [`f0742eb55c9f038c3444a84ab9a3b4fe785ab425`](https://github.com/matiassingers/awesome-readme/commit/f0742eb55c9f038c3444a84ab9a3b4fe785ab425), ngày commit 2026-11-10. Đã clone và đọc chọn lọc phần giới thiệu, cách dùng, giới hạn, license, metadata manifest và CI hiện diện. Chưa kiểm đầy đủ implementation hoặc chạy upstream; các số đo của tác giả chưa được tái lập.

**Nguồn:** [readme.md](https://github.com/matiassingers/awesome-readme/blob/f0742eb55c9f038c3444a84ab9a3b4fe785ab425/readme.md) · [metadata GitHub](https://api.github.com/repos/matiassingers/awesome-readme).

<a id="anhkysuai-2026-11-23-git-tips-tips"></a>

### tips

**Repo:** [git-tips/tips](https://github.com/git-tips/tips) · **License:** MIT · **★ 21,725 (GitHub API, 2026-11-23)**

**Mục đích:** Tập hợp mẹo và lệnh Git để tra cứu theo thao tác.

**Giá trị:** Nhiều ví dụ ngắn thuận tiện học staging, lịch sử và xử lý nhánh; có tài liệu tương tác và bản dịch.

**Giới hạn:** README ghi bộ lệnh từng được thử với Git 2.7.4; lệnh xóa, reset hoặc sửa lịch sử cần hiểu trạng thái repo và kiểm trên bản sao trước dùng.

**Cách tham khảo/tích hợp:** Chọn bài theo mục tiêu, thực hành lại trên môi trường riêng và kiểm bằng bài chuyển giao; khi dùng lại nội dung phải đối chiếu giấy phép đúng phạm vi.

**Lựa chọn để đối chiếu:** [firstcontributions/first-contributions](https://github.com/firstcontributions/first-contributions) · [tldr-pages/tldr](https://github.com/tldr-pages/tldr). Đây là ứng viên so sánh theo tác vụ; mức phù hợp cần kiểm theo hồ sơ và phiên bản riêng.

**Bằng chứng:** `docs-read`, ngày 2026-11-23, commit [`727551c5dab24c7b1d63814222a06f9d01546bc4`](https://github.com/git-tips/tips/commit/727551c5dab24c7b1d63814222a06f9d01546bc4), ngày commit 2026-08-10. Đã clone và đọc chọn lọc phần giới thiệu, cách dùng, giới hạn, license, metadata manifest và CI hiện diện. Chưa kiểm đầy đủ implementation hoặc chạy upstream; các số đo của tác giả chưa được tái lập.

**Nguồn:** [README.md](https://github.com/git-tips/tips/blob/727551c5dab24c7b1d63814222a06f9d01546bc4/README.md) · [LICENSE](https://github.com/git-tips/tips/blob/727551c5dab24c7b1d63814222a06f9d01546bc4/LICENSE) · [package.json](https://github.com/git-tips/tips/blob/727551c5dab24c7b1d63814222a06f9d01546bc4/package.json) · [.github/workflows/deploy-docs.yml](https://github.com/git-tips/tips/blob/727551c5dab24c7b1d63814222a06f9d01546bc4/.github/workflows/deploy-docs.yml) · [metadata GitHub](https://api.github.com/repos/git-tips/tips).

<a id="anhkysuai-2026-11-23-rockerboo-awesome-neovim"></a>

### awesome-neovim

**Repo:** [rockerBOO/awesome-neovim](https://github.com/rockerBOO/awesome-neovim) · **License:** CC0-1.0 · **★ 21,607 (GitHub API, 2026-11-23)**

**Mục đích:** Danh mục plugin tập trung vào các khả năng riêng của Neovim.

**Giá trị:** Phân nhóm LSP, completion, UI, tìm kiếm và AI giúp tìm phần mở rộng theo công việc.

**Giới hạn:** README chủ động không bao quát plugin chỉ tương thích Vim; cần kiểm phiên bản Neovim, dependencies và quyền từng plugin, không coi việc có trong danh sách là đã kiểm toán.

**Cách tham khảo/tích hợp:** Dùng làm chỉ mục tìm ứng viên, dẫn về nguồn gốc rồi kiểm phiên bản, giấy phép và mức bảo trì của từng lựa chọn trước tích hợp.

**Lựa chọn để đối chiếu:** [neovim/neovim](https://github.com/neovim/neovim) · [viatsko/awesome-vscode](https://github.com/viatsko/awesome-vscode). Đây là ứng viên so sánh theo tác vụ; mức phù hợp cần kiểm theo hồ sơ và phiên bản riêng.

**Bằng chứng:** `docs-read`, ngày 2026-11-23, commit [`0c160033536aa472374b1aac9c4ba83217f5158c`](https://github.com/rockerBOO/awesome-neovim/commit/0c160033536aa472374b1aac9c4ba83217f5158c), ngày commit 2026-11-20. Đã clone và đọc chọn lọc phần giới thiệu, cách dùng, giới hạn, license, metadata manifest và CI hiện diện. Chưa kiểm đầy đủ implementation hoặc chạy upstream; các số đo của tác giả chưa được tái lập.

**Nguồn:** [README.md](https://github.com/rockerBOO/awesome-neovim/blob/0c160033536aa472374b1aac9c4ba83217f5158c/README.md) · [LICENSE](https://github.com/rockerBOO/awesome-neovim/blob/0c160033536aa472374b1aac9c4ba83217f5158c/LICENSE) · [.github/workflows/pr-compliance-check.yml](https://github.com/rockerBOO/awesome-neovim/blob/0c160033536aa472374b1aac9c4ba83217f5158c/.github/workflows/pr-compliance-check.yml) · [metadata GitHub](https://api.github.com/repos/rockerBOO/awesome-neovim).

<a id="anhkysuai-2026-11-23-milanm-devops-roadmap"></a>

### DevOps-Roadmap

**Repo:** [milanm/DevOps-Roadmap](https://github.com/milanm/DevOps-Roadmap) · **License:** Apache-2.0 · **★ 21,026 (GitHub API, 2026-11-23)**

**Mục đích:** Lộ trình DevOps 2026 với tài nguyên học Git, Linux, mạng, container, IaC và vận hành.

**Giá trị:** Sắp xếp chủ đề theo tiến trình giúp xác định phần còn thiếu trong nền tảng kỹ thuật.

**Giới hạn:** README nói rõ mục đích là hiểu bối cảnh và lựa chọn công cụ theo nhu cầu; danh sách không bảo đảm hoàn thành trong một thời hạn hoặc thay kinh nghiệm vận hành.

**Cách tham khảo/tích hợp:** Chọn bài theo mục tiêu, thực hành lại trên môi trường riêng và kiểm bằng bài chuyển giao; khi dùng lại nội dung phải đối chiếu giấy phép đúng phạm vi.

**Lựa chọn để đối chiếu:** [MichaelCade/90DaysOfDevOps](https://github.com/MichaelCade/90DaysOfDevOps) · [veggiemonk/awesome-docker](https://github.com/veggiemonk/awesome-docker). Đây là ứng viên so sánh theo tác vụ; mức phù hợp cần kiểm theo hồ sơ và phiên bản riêng.

**Bằng chứng:** `docs-read`, ngày 2026-11-23, commit [`ae79066e63a11827ed02b5bf0cff0f4b00a650e5`](https://github.com/milanm/DevOps-Roadmap/commit/ae79066e63a11827ed02b5bf0cff0f4b00a650e5), ngày commit 2026-11-02. Đã clone và đọc chọn lọc phần giới thiệu, cách dùng, giới hạn, license, metadata manifest và CI hiện diện. Chưa kiểm đầy đủ implementation hoặc chạy upstream; các số đo của tác giả chưa được tái lập.

**Nguồn:** [README.md](https://github.com/milanm/DevOps-Roadmap/blob/ae79066e63a11827ed02b5bf0cff0f4b00a650e5/README.md) · [LICENSE](https://github.com/milanm/DevOps-Roadmap/blob/ae79066e63a11827ed02b5bf0cff0f4b00a650e5/LICENSE) · [metadata GitHub](https://api.github.com/repos/milanm/DevOps-Roadmap).

<a id="anhkysuai-2026-11-23-pluja-awesome-privacy"></a>

### awesome-privacy

**Repo:** [pluja/awesome-privacy](https://github.com/pluja/awesome-privacy) · **License:** CC0-1.0 · **★ 20,352 (GitHub API, 2026-11-23)**

**Mục đích:** Danh mục dịch vụ và phần mềm ưu tiên quyền riêng tư theo loại nhu cầu.

**Giá trị:** README phân biệt privacy, security và anonymity, hữu ích làm bước tìm lựa chọn thay thế.

**Giới hạn:** Tuyên bố của danh sách chưa thay kiểm chính sách, mô hình đe dọa hoặc kiểm toán độc lập; mỗi dịch vụ cần đánh giá hiện trạng và giấy phép riêng.

**Cách tham khảo/tích hợp:** Dùng làm chỉ mục tìm ứng viên, dẫn về nguồn gốc rồi kiểm phiên bản, giấy phép và mức bảo trì của từng lựa chọn trước tích hợp.

**Lựa chọn để đối chiếu:** [privacyguides/privacyguides.org](https://github.com/privacyguides/privacyguides.org) · [awesome-foss/awesome-sysadmin](https://github.com/awesome-foss/awesome-sysadmin). Đây là ứng viên so sánh theo tác vụ; mức phù hợp cần kiểm theo hồ sơ và phiên bản riêng.

**Bằng chứng:** `docs-read`, ngày 2026-11-23, commit [`887accc6c2f782409aa26848961dc4618c59618c`](https://github.com/pluja/awesome-privacy/commit/887accc6c2f782409aa26848961dc4618c59618c), ngày commit 2026-11-14. Đã clone và đọc chọn lọc phần giới thiệu, cách dùng, giới hạn, license, metadata manifest và CI hiện diện. Chưa kiểm đầy đủ implementation hoặc chạy upstream; các số đo của tác giả chưa được tái lập.

**Nguồn:** [README.md](https://github.com/pluja/awesome-privacy/blob/887accc6c2f782409aa26848961dc4618c59618c/README.md) · [LICENSE](https://github.com/pluja/awesome-privacy/blob/887accc6c2f782409aa26848961dc4618c59618c/LICENSE) · [package.json](https://github.com/pluja/awesome-privacy/blob/887accc6c2f782409aa26848961dc4618c59618c/package.json) · [.github/workflows/pr-check.yml](https://github.com/pluja/awesome-privacy/blob/887accc6c2f782409aa26848961dc4618c59618c/.github/workflows/pr-check.yml) · [metadata GitHub](https://api.github.com/repos/pluja/awesome-privacy).

<a id="anhkysuai-2026-11-23-tianxingchen-embodied-ai-guide"></a>

### Embodied-AI-Guide

**Repo:** [TianxingChen/Embodied-AI-Guide](https://github.com/TianxingChen/Embodied-AI-Guide) · **License:** Non-Commercial Use License (tùy chỉnh) · **★ 17,035 (GitHub API, 2026-11-23)**

**Mục đích:** Kho kiến thức tiếng Trung về embodied AI, thuật toán, điều khiển, hạ tầng và phần cứng.

**Giá trị:** Lộ trình theo nền tảng người học kết hợp dự án thực hành và chỉ mục tài liệu giúp định hướng nghiên cứu robot.

**Giới hạn:** Giấy phép phi thương mại riêng cấm cả sử dụng nội bộ tổ chức vì lợi nhuận nếu chưa được phép; không gắn nhãn nguồn mở chỉ vì repo công khai.

**Cách tham khảo/tích hợp:** Chọn bài theo mục tiêu, thực hành lại trên môi trường riêng và kiểm bằng bài chuyển giao; khi dùng lại nội dung phải đối chiếu giấy phép đúng phạm vi.

**Lựa chọn để đối chiếu:** [AtsushiSakai/PythonRobotics](https://github.com/AtsushiSakai/PythonRobotics) · [datawhalechina/every-embodied](https://github.com/datawhalechina/every-embodied). Đây là ứng viên so sánh theo tác vụ; mức phù hợp cần kiểm theo hồ sơ và phiên bản riêng.

**Bằng chứng:** `docs-read`, ngày 2026-11-23, commit [`236f5fb35ca7058a0ff842046a6b11cfd521b7b5`](https://github.com/TianxingChen/Embodied-AI-Guide/commit/236f5fb35ca7058a0ff842046a6b11cfd521b7b5), ngày commit 2026-11-18. Đã clone và đọc chọn lọc phần giới thiệu, cách dùng, giới hạn, license, metadata manifest và CI hiện diện. Chưa kiểm đầy đủ implementation hoặc chạy upstream; các số đo của tác giả chưa được tái lập.

**Nguồn:** [README.md](https://github.com/TianxingChen/Embodied-AI-Guide/blob/236f5fb35ca7058a0ff842046a6b11cfd521b7b5/README.md) · [LICENSE](https://github.com/TianxingChen/Embodied-AI-Guide/blob/236f5fb35ca7058a0ff842046a6b11cfd521b7b5/LICENSE) · [metadata GitHub](https://api.github.com/repos/TianxingChen/Embodied-AI-Guide).

<a id="anhkysuai-2026-11-23-github-opensource.guide"></a>

### opensource.guide

**Repo:** [github/opensource.guide](https://github.com/github/opensource.guide) · **License:** CC-BY-4.0 · **★ 15,815 (GitHub API, 2026-11-23)**

**Mục đích:** Hướng dẫn xây dựng, đóng góp và duy trì cộng đồng dự án nguồn mở.

**Giá trị:** Tổng hợp thực hành cộng đồng và ví dụ, có thể dùng làm nền cho CONTRIBUTING, quản trị và hỗ trợ maintainer.

**Giới hạn:** Nội dung CC BY 4.0, phần mềm và trích dẫn bên thứ ba có notices riêng; hướng dẫn cần điều chỉnh theo quy mô, quyền quyết định và bối cảnh pháp lý của dự án.

**Cách tham khảo/tích hợp:** Chọn bài theo mục tiêu, thực hành lại trên môi trường riêng và kiểm bằng bài chuyển giao; khi dùng lại nội dung phải đối chiếu giấy phép đúng phạm vi.

**Lựa chọn để đối chiếu:** [firstcontributions/first-contributions](https://github.com/firstcontributions/first-contributions) · [matiassingers/awesome-readme](https://github.com/matiassingers/awesome-readme). Đây là ứng viên so sánh theo tác vụ; mức phù hợp cần kiểm theo hồ sơ và phiên bản riêng.

**Bằng chứng:** `docs-read`, ngày 2026-11-23, commit [`e7ac98e94600c5eea834f9a026c000d26b28df24`](https://github.com/github/opensource.guide/commit/e7ac98e94600c5eea834f9a026c000d26b28df24), ngày commit 2026-09-30. Đã clone và đọc chọn lọc phần giới thiệu, cách dùng, giới hạn, license, metadata manifest và CI hiện diện. Chưa kiểm đầy đủ implementation hoặc chạy upstream; các số đo của tác giả chưa được tái lập.

**Nguồn:** [README.md](https://github.com/github/opensource.guide/blob/e7ac98e94600c5eea834f9a026c000d26b28df24/README.md) · [LICENSE](https://github.com/github/opensource.guide/blob/e7ac98e94600c5eea834f9a026c000d26b28df24/LICENSE) · [package.json](https://github.com/github/opensource.guide/blob/e7ac98e94600c5eea834f9a026c000d26b28df24/package.json) · [.github/workflows/tests.yml](https://github.com/github/opensource.guide/blob/e7ac98e94600c5eea834f9a026c000d26b28df24/.github/workflows/tests.yml) · [metadata GitHub](https://api.github.com/repos/github/opensource.guide).

<a id="anhkysuai-2026-11-23-rougier-numpy-100"></a>

### numpy-100

**Repo:** [rougier/numpy-100](https://github.com/rougier/numpy-100) · **License:** MIT · **★ 14,704 (GitHub API, 2026-11-23)**

**Mục đích:** 100 bài tập NumPy có lời giải, sinh bản Markdown và notebook từ một nguồn dữ liệu.

**Giá trị:** Phù hợp luyện thao tác mảng và tạo bài thực hành ngắn cho lớp học hoặc tự đánh giá.

**Giới hạn:** Lời giải cần thử với phiên bản NumPy đang dùng và giải thích được hành vi số học; đọc đáp án không thay làm bài độc lập. Cần sửa nguồn thay vì tệp sinh.

**Cách tham khảo/tích hợp:** Chọn bài theo mục tiêu, thực hành lại trên môi trường riêng và kiểm bằng bài chuyển giao; khi dùng lại nội dung phải đối chiếu giấy phép đúng phạm vi.

**Lựa chọn để đối chiếu:** [microsoft/Data-Science-For-Beginners](https://github.com/microsoft/Data-Science-For-Beginners) · [norvig/pytudes](https://github.com/norvig/pytudes). Đây là ứng viên so sánh theo tác vụ; mức phù hợp cần kiểm theo hồ sơ và phiên bản riêng.

**Bằng chứng:** `docs-read`, ngày 2026-11-23, commit [`cf3b5a29749410758ccaab876302ed861bb94323`](https://github.com/rougier/numpy-100/commit/cf3b5a29749410758ccaab876302ed861bb94323), ngày commit 2026-10-23. Đã clone và đọc chọn lọc phần giới thiệu, cách dùng, giới hạn, license, metadata manifest và CI hiện diện. Chưa kiểm đầy đủ implementation hoặc chạy upstream; các số đo của tác giả chưa được tái lập.

**Nguồn:** [README.md](https://github.com/rougier/numpy-100/blob/cf3b5a29749410758ccaab876302ed861bb94323/README.md) · [LICENSE.txt](https://github.com/rougier/numpy-100/blob/cf3b5a29749410758ccaab876302ed861bb94323/LICENSE.txt) · [.github/workflows/generate_solutions_files.yml](https://github.com/rougier/numpy-100/blob/cf3b5a29749410758ccaab876302ed861bb94323/.github/workflows/generate_solutions_files.yml) · [metadata GitHub](https://api.github.com/repos/rougier/numpy-100).

<a id="anhkysuai-2026-11-23-996icu-996.icu"></a>

### 996.ICU

**Repo:** [996icu/996.ICU](https://github.com/996icu/996.ICU) · **License:** Anti-996 License 1.0 (Draft) · **★ 277,255 (GitHub API, 2026-11-23)**

**Mục đích:** Kho tư liệu và chiến dịch cộng đồng về điều kiện lao động lập trình viên, kèm bản nháp Anti-996 License.

**Giá trị:** Có giá trị tham khảo lịch sử cộng đồng và cách dùng repo để tập hợp thông tin/xây đề xuất giấy phép.

**Giới hạn:** Đây không phải thư viện triển khai; Anti-996 có điều kiện về lao động nên không đồng nhất với MIT. Tuyên bố và danh sách cộng đồng cần đối chiếu nguồn, không dùng như kết luận pháp lý.

**Cách tham khảo/tích hợp:** Chọn bài theo mục tiêu, thực hành lại trên môi trường riêng và kiểm bằng bài chuyển giao; khi dùng lại nội dung phải đối chiếu giấy phép đúng phạm vi.

**Lựa chọn để đối chiếu:** [github/opensource.guide](https://github.com/github/opensource.guide) · [charlax/professional-programming](https://github.com/charlax/professional-programming). Đây là ứng viên so sánh theo tác vụ; mức phù hợp cần kiểm theo hồ sơ và phiên bản riêng.

**Bằng chứng:** `docs-read`, ngày 2026-11-23, commit [`f5e35f48d769bf92ed885888bfe911d3e5b5a63d`](https://github.com/996icu/996.ICU/commit/f5e35f48d769bf92ed885888bfe911d3e5b5a63d), ngày commit 2025-08-22. Đã clone và đọc chọn lọc phần giới thiệu, cách dùng, giới hạn, license, metadata manifest và CI hiện diện. Chưa kiểm đầy đủ implementation hoặc chạy upstream; các số đo của tác giả chưa được tái lập.

**Nguồn:** [README.md](https://github.com/996icu/996.ICU/blob/f5e35f48d769bf92ed885888bfe911d3e5b5a63d/README.md) · [LICENSE](https://github.com/996icu/996.ICU/blob/f5e35f48d769bf92ed885888bfe911d3e5b5a63d/LICENSE) · [LICENSE_CN](https://github.com/996icu/996.ICU/blob/f5e35f48d769bf92ed885888bfe911d3e5b5a63d/LICENSE_CN) · [metadata GitHub](https://api.github.com/repos/996icu/996.ICU).

<a id="anhkysuai-2026-11-23-trimstray-the-book-of-secret-knowledge"></a>

### the-book-of-secret-knowledge

**Repo:** [trimstray/the-book-of-secret-knowledge](https://github.com/trimstray/the-book-of-secret-knowledge) · **License:** MIT · **★ 260,664 (GitHub API, 2026-11-23)**

**Mục đích:** Tuyển tập công cụ, tài liệu, cheatsheet và lệnh cho quản trị hệ thống, mạng và DevOps.

**Giá trị:** Phạm vi rộng thuận tiện tìm gợi ý xử lý vấn đề và công cụ để khảo sát tiếp.

**Giới hạn:** HEAD đã đọc từ 2024; nhiều lệnh có tác động hệ thống và link có thể lỗi thời. Cần hiểu đầu vào/quyền và thử độc lập, MIT của danh sách không cấp quyền mọi công cụ được dẫn.

**Cách tham khảo/tích hợp:** Chọn bài theo mục tiêu, thực hành lại trên môi trường riêng và kiểm bằng bài chuyển giao; khi dùng lại nội dung phải đối chiếu giấy phép đúng phạm vi.

**Lựa chọn để đối chiếu:** [tldr-pages/tldr](https://github.com/tldr-pages/tldr) · [awesome-foss/awesome-sysadmin](https://github.com/awesome-foss/awesome-sysadmin). Đây là ứng viên so sánh theo tác vụ; mức phù hợp cần kiểm theo hồ sơ và phiên bản riêng.

**Bằng chứng:** `docs-read`, ngày 2026-11-23, commit [`7d37069a361d3fd9f214480755f7969744e866fa`](https://github.com/trimstray/the-book-of-secret-knowledge/commit/7d37069a361d3fd9f214480755f7969744e866fa), ngày commit 2024-11-19. Đã clone và đọc chọn lọc phần giới thiệu, cách dùng, giới hạn, license, metadata manifest và CI hiện diện. Chưa kiểm đầy đủ implementation hoặc chạy upstream; các số đo của tác giả chưa được tái lập.

**Nguồn:** [README.md](https://github.com/trimstray/the-book-of-secret-knowledge/blob/7d37069a361d3fd9f214480755f7969744e866fa/README.md) · [LICENSE.md](https://github.com/trimstray/the-book-of-secret-knowledge/blob/7d37069a361d3fd9f214480755f7969744e866fa/LICENSE.md) · [metadata GitHub](https://api.github.com/repos/trimstray/the-book-of-secret-knowledge).

<a id="anhkysuai-2026-11-23-digitalplatdev-freedomain"></a>

### FreeDomain

**Repo:** [DigitalPlatDev/FreeDomain](https://github.com/DigitalPlatDev/FreeDomain) · **License:** AGPL-3.0 · **★ 209,028 (GitHub API, 2026-11-23)**

**Mục đích:** Thông tin công khai và tài liệu học DNS/đăng ký tên miền của DigitalPlat FreeDomain.

**Giá trị:** Có lộ trình từ đăng ký tới cấu hình nameserver và triển khai, hữu ích cho học DNS thực hành.

**Giới hạn:** README chỉ rõ mã ứng dụng nằm tại DigitalPlatDev/Domain-OSS; repo này không chứng minh độ bền hoặc điều khoản miễn phí của dịch vụ tên miền, cần kiểm nhà cung cấp trước phụ thuộc lâu dài.

**Cách tham khảo/tích hợp:** Chọn bài theo mục tiêu, thực hành lại trên môi trường riêng và kiểm bằng bài chuyển giao; khi dùng lại nội dung phải đối chiếu giấy phép đúng phạm vi.

**Lựa chọn để đối chiếu:** [DigitalPlatDev/Domain-OSS](https://github.com/DigitalPlatDev/Domain-OSS) · [ripienaar/free-for-dev](https://github.com/ripienaar/free-for-dev). Đây là ứng viên so sánh theo tác vụ; mức phù hợp cần kiểm theo hồ sơ và phiên bản riêng.

**Bằng chứng:** `docs-read`, ngày 2026-11-23, commit [`9c7c54110705760267b07b6e6a6d406d1172a1bf`](https://github.com/DigitalPlatDev/FreeDomain/commit/9c7c54110705760267b07b6e6a6d406d1172a1bf), ngày commit 2026-08-12. Đã clone và đọc chọn lọc phần giới thiệu, cách dùng, giới hạn, license, metadata manifest và CI hiện diện. Chưa kiểm đầy đủ implementation hoặc chạy upstream; các số đo của tác giả chưa được tái lập.

**Nguồn:** [README.md](https://github.com/DigitalPlatDev/FreeDomain/blob/9c7c54110705760267b07b6e6a6d406d1172a1bf/README.md) · [LICENSE](https://github.com/DigitalPlatDev/FreeDomain/blob/9c7c54110705760267b07b6e6a6d406d1172a1bf/LICENSE) · [metadata GitHub](https://api.github.com/repos/DigitalPlatDev/FreeDomain).

<a id="anhkysuai-2026-11-23-521xueweihan-hellogithub"></a>

### HelloGitHub

**Repo:** [521xueweihan/HelloGitHub](https://github.com/521xueweihan/HelloGitHub) · **License:** Chưa xác lập ở phạm vi đã đọc · **★ 190,692 (GitHub API, 2026-11-23)**

**Mục đích:** Tạp chí/danh mục tiếng Trung giới thiệu các dự án GitHub dễ tiếp cận theo kỳ.

**Giá trị:** Nguồn phát hiện dự án và ý tưởng thực hành cho người mới, có đường dẫn đọc chi tiết và đóng góp.

**Giới hạn:** Chưa thấy giấy phép chung ở gốc đã đọc; bài giới thiệu không thay kiểm mã, bảo trì và license repo gốc. Nên dẫn nguồn thay vì sao lại nguyên phần mô tả. Chưa xác lập giấy phép chung cho nội dung chính ở phạm vi đã đọc; không suy quyền tái sử dụng từ repo công khai.

**Cách tham khảo/tích hợp:** Dùng làm chỉ mục tìm ứng viên, dẫn về nguồn gốc rồi kiểm phiên bản, giấy phép và mức bảo trì của từng lựa chọn trước tích hợp.

**Lựa chọn để đối chiếu:** [firstcontributions/first-contributions](https://github.com/firstcontributions/first-contributions) · [MunGell/awesome-for-beginners](https://github.com/MunGell/awesome-for-beginners). Đây là ứng viên so sánh theo tác vụ; mức phù hợp cần kiểm theo hồ sơ và phiên bản riêng.

**Bằng chứng:** `docs-read`, ngày 2026-11-23, commit [`d65699c2892f3ad7516398a3fbd3855913f9d17d`](https://github.com/521xueweihan/HelloGitHub/commit/d65699c2892f3ad7516398a3fbd3855913f9d17d), ngày commit 2026-11-01. Đã clone và đọc chọn lọc phần giới thiệu, cách dùng, giới hạn, license, metadata manifest và CI hiện diện. Chưa kiểm đầy đủ implementation hoặc chạy upstream; các số đo của tác giả chưa được tái lập.

**Nguồn:** [README.md](https://github.com/521xueweihan/HelloGitHub/blob/d65699c2892f3ad7516398a3fbd3855913f9d17d/README.md) · [metadata GitHub](https://api.github.com/repos/521xueweihan/HelloGitHub).

<a id="anhkysuai-2026-11-23-cyc2018-cs-notes"></a>

### CS-Notes

**Repo:** [CyC2018/CS-Notes](https://github.com/CyC2018/CS-Notes) · **License:** CC-BY-NC-SA-4.0 (nội dung); thành phần website riêng · **★ 186,565 (GitHub API, 2026-11-23)**

**Mục đích:** Ghi chú tiếng Trung về khoa học máy tính, Java, thuật toán và lộ trình chuẩn bị phỏng vấn.

**Giá trị:** Tuyến học phân theo nền tảng và mục tiêu giúp liên kết kiến thức hệ điều hành, mạng, dữ liệu và thiết kế hệ thống.

**Giới hạn:** Nội dung README mang CC BY-NC-SA 4.0, khác MIT của thư viện tô màu Prism bên trong; kiến thức/phỏng vấn cần đối chiếu phiên bản và thực hành độc lập.

**Cách tham khảo/tích hợp:** Chọn bài theo mục tiêu, thực hành lại trên môi trường riêng và kiểm bằng bài chuyển giao; khi dùng lại nội dung phải đối chiếu giấy phép đúng phạm vi.

**Lựa chọn để đối chiếu:** [huihut/interview](https://github.com/huihut/interview) · [charlax/professional-programming](https://github.com/charlax/professional-programming). Đây là ứng viên so sánh theo tác vụ; mức phù hợp cần kiểm theo hồ sơ và phiên bản riêng.

**Bằng chứng:** `docs-read`, ngày 2026-11-23, commit [`cb9f180fb26da7b7100fde250a5dd137455b3a02`](https://github.com/CyC2018/CS-Notes/commit/cb9f180fb26da7b7100fde250a5dd137455b3a02), ngày commit 2026-11-10. Đã clone và đọc chọn lọc phần giới thiệu, cách dùng, giới hạn, license, metadata manifest và CI hiện diện. Chưa kiểm đầy đủ implementation hoặc chạy upstream; các số đo của tác giả chưa được tái lập.

**Nguồn:** [README.md](https://github.com/CyC2018/CS-Notes/blob/cb9f180fb26da7b7100fde250a5dd137455b3a02/README.md) · [docs/_style/prism-master/LICENSE](https://github.com/CyC2018/CS-Notes/blob/cb9f180fb26da7b7100fde250a5dd137455b3a02/docs/_style/prism-master/LICENSE) · [.github/workflows/website.yml](https://github.com/CyC2018/CS-Notes/blob/cb9f180fb26da7b7100fde250a5dd137455b3a02/.github/workflows/website.yml) · [metadata GitHub](https://api.github.com/repos/CyC2018/CS-Notes).

<a id="anhkysuai-2026-11-23-ripienaar-free-for-dev"></a>

### free-for-dev

**Repo:** [ripienaar/free-for-dev](https://github.com/ripienaar/free-for-dev) · **License:** Chưa xác lập ở phạm vi đã đọc · **★ 143,415 (GitHub API, 2026-11-23)**

**Mục đích:** Danh sách SaaS/PaaS/IaaS có gói miễn phí hữu ích cho lập trình và hạ tầng.

**Giá trị:** Phân nhóm dịch vụ giúp lập danh sách lựa chọn ban đầu và tìm công cụ cho thử nghiệm.

**Giới hạn:** Giới hạn miễn phí, điều khoản và yêu cầu thẻ có thể đổi; chưa kiểm riêng từng nhà cung cấp. Không thấy license chung ở gốc đã đọc và free tier không đồng nghĩa nguồn mở. Chưa xác lập giấy phép chung cho nội dung chính ở phạm vi đã đọc; không suy quyền tái sử dụng từ repo công khai.

**Cách tham khảo/tích hợp:** Dùng làm chỉ mục tìm ứng viên, dẫn về nguồn gốc rồi kiểm phiên bản, giấy phép và mức bảo trì của từng lựa chọn trước tích hợp.

**Lựa chọn để đối chiếu:** [DigitalPlatDev/FreeDomain](https://github.com/DigitalPlatDev/FreeDomain) · [awesome-foss/awesome-sysadmin](https://github.com/awesome-foss/awesome-sysadmin). Đây là ứng viên so sánh theo tác vụ; mức phù hợp cần kiểm theo hồ sơ và phiên bản riêng.

**Bằng chứng:** `docs-read`, ngày 2026-11-23, commit [`9c424e150a269cd3079f3b3d72a51e34f7526d0c`](https://github.com/ripienaar/free-for-dev/commit/9c424e150a269cd3079f3b3d72a51e34f7526d0c), ngày commit 2026-11-23. Đã clone và đọc chọn lọc phần giới thiệu, cách dùng, giới hạn, license, metadata manifest và CI hiện diện. Chưa kiểm đầy đủ implementation hoặc chạy upstream; các số đo của tác giả chưa được tái lập.

**Nguồn:** [README.md](https://github.com/ripienaar/free-for-dev/blob/9c424e150a269cd3079f3b3d72a51e34f7526d0c/README.md) · [metadata GitHub](https://api.github.com/repos/ripienaar/free-for-dev).

<a id="anhkysuai-2026-11-23-jaywcjlove-awesome-mac"></a>

### awesome-mac

**Repo:** [jaywcjlove/awesome-mac](https://github.com/jaywcjlove/awesome-mac) · **License:** Mâu thuẫn CC0 / CC-BY-4.0 / CC-BY-SA-4.0; chưa kết luận · **★ 119,172 (GitHub API, 2026-11-23)**

**Mục đích:** Danh mục phần mềm macOS theo tác vụ, phân biệt nguồn mở, freeware và App Store.

**Giá trị:** Có thể dùng để tìm công cụ rồi kiểm repo gốc theo nhu cầu nền tảng.

**Giới hạn:** Giấy phép mâu thuẫn: LICENSE là CC0, README CC BY 4.0, package.json CC BY-SA 4.0; cần làm rõ phạm vi trước tái phân phối. Quyền mỗi ứng dụng được liệt kê là riêng.

**Cách tham khảo/tích hợp:** Dùng làm chỉ mục tìm ứng viên, dẫn về nguồn gốc rồi kiểm phiên bản, giấy phép và mức bảo trì của từng lựa chọn trước tích hợp.

**Lựa chọn để đối chiếu:** [serhii-londar/open-source-mac-os-apps](https://github.com/serhii-londar/open-source-mac-os-apps) · [vsouza/awesome-ios](https://github.com/vsouza/awesome-ios). Đây là ứng viên so sánh theo tác vụ; mức phù hợp cần kiểm theo hồ sơ và phiên bản riêng.

**Bằng chứng:** `docs-read`, ngày 2026-11-23, commit [`23ca709562e808a98ad5fc503214c1e2f864e5a4`](https://github.com/jaywcjlove/awesome-mac/commit/23ca709562e808a98ad5fc503214c1e2f864e5a4), ngày commit 2026-11-23. Đã clone và đọc chọn lọc phần giới thiệu, cách dùng, giới hạn, license, metadata manifest và CI hiện diện. Chưa kiểm đầy đủ implementation hoặc chạy upstream; các số đo của tác giả chưa được tái lập.

**Nguồn:** [README.md](https://github.com/jaywcjlove/awesome-mac/blob/23ca709562e808a98ad5fc503214c1e2f864e5a4/README.md) · [LICENSE](https://github.com/jaywcjlove/awesome-mac/blob/23ca709562e808a98ad5fc503214c1e2f864e5a4/LICENSE) · [package.json](https://github.com/jaywcjlove/awesome-mac/blob/23ca709562e808a98ad5fc503214c1e2f864e5a4/package.json) · [.github/workflows/ci.yml](https://github.com/jaywcjlove/awesome-mac/blob/23ca709562e808a98ad5fc503214c1e2f864e5a4/.github/workflows/ci.yml) · [metadata GitHub](https://api.github.com/repos/jaywcjlove/awesome-mac).

<a id="anhkysuai-2026-11-23-papers-we-love-papers-we-love"></a>

### papers-we-love

**Repo:** [papers-we-love/papers-we-love](https://github.com/papers-we-love/papers-we-love) · **License:** Chưa xác lập ở phạm vi đã đọc · **★ 111,762 (GitHub API, 2026-11-23)**

**Mục đích:** Chỉ mục paper khoa học máy tính và cộng đồng đọc, thảo luận nghiên cứu.

**Giá trị:** Tập hợp chủ đề và gợi ý cách đọc paper, phù hợp xây nhóm đọc hoặc lần lại nền tảng của một kỹ thuật.

**Giới hạn:** README nói không thể lưu mọi paper vì bản quyền; từng tài liệu có quyền riêng, danh sách không cấp quyền tái xuất bản toàn bộ PDF hoặc xác nhận kết quả đã tái lập. Chưa xác lập giấy phép chung cho nội dung chính ở phạm vi đã đọc; không suy quyền tái sử dụng từ repo công khai.

**Cách tham khảo/tích hợp:** Dùng làm chỉ mục tìm ứng viên, dẫn về nguồn gốc rồi kiểm phiên bản, giấy phép và mức bảo trì của từng lựa chọn trước tích hợp.

**Lựa chọn để đối chiếu:** [floodsung/Deep-Learning-Papers-Reading-Roadmap](https://github.com/floodsung/Deep-Learning-Papers-Reading-Roadmap) · [satellite-image-deep-learning/techniques](https://github.com/satellite-image-deep-learning/techniques). Đây là ứng viên so sánh theo tác vụ; mức phù hợp cần kiểm theo hồ sơ và phiên bản riêng.

**Bằng chứng:** `docs-read`, ngày 2026-11-23, commit [`0b33c953aae0c90e6d15c4ed41b01e76358f3c28`](https://github.com/papers-we-love/papers-we-love/commit/0b33c953aae0c90e6d15c4ed41b01e76358f3c28), ngày commit 2026-10-28. Đã clone và đọc chọn lọc phần giới thiệu, cách dùng, giới hạn, license, metadata manifest và CI hiện diện. Chưa kiểm đầy đủ implementation hoặc chạy upstream; các số đo của tác giả chưa được tái lập.

**Nguồn:** [README.md](https://github.com/papers-we-love/papers-we-love/blob/0b33c953aae0c90e6d15c4ed41b01e76358f3c28/README.md) · [.github/workflows/lychee.yml](https://github.com/papers-we-love/papers-we-love/blob/0b33c953aae0c90e6d15c4ed41b01e76358f3c28/.github/workflows/lychee.yml) · [metadata GitHub](https://api.github.com/repos/papers-we-love/papers-we-love).

<a id="anhkysuai-2026-11-23-mungell-awesome-for-beginners"></a>

### awesome-for-beginners

**Repo:** [MunGell/awesome-for-beginners](https://github.com/MunGell/awesome-for-beginners) · **License:** CC0-1.0 (tuyên bố trong README) · **★ 91,702 (GitHub API, 2026-11-23)**

**Mục đích:** Danh sách dự án có cơ hội đóng góp đầu tiên, chia theo ngôn ngữ và nhãn issue.

**Giá trị:** Giúp người mới tìm nơi thực hành pull request có phạm vi phù hợp.

**Giới hạn:** Nhãn good-first-issue không bảo đảm issue còn mở hoặc phù hợp kỹ năng; cần đọc CONTRIBUTING và trao đổi ở repo đích. CC0 chỉ áp dụng danh sách.

**Cách tham khảo/tích hợp:** Dùng làm chỉ mục tìm ứng viên, dẫn về nguồn gốc rồi kiểm phiên bản, giấy phép và mức bảo trì của từng lựa chọn trước tích hợp.

**Lựa chọn để đối chiếu:** [firstcontributions/first-contributions](https://github.com/firstcontributions/first-contributions) · [github/opensource.guide](https://github.com/github/opensource.guide). Đây là ứng viên so sánh theo tác vụ; mức phù hợp cần kiểm theo hồ sơ và phiên bản riêng.

**Bằng chứng:** `docs-read`, ngày 2026-11-23, commit [`f7bf7d43cb26d555e51a4c6c83af563a08795605`](https://github.com/MunGell/awesome-for-beginners/commit/f7bf7d43cb26d555e51a4c6c83af563a08795605), ngày commit 2026-10-01. Đã clone và đọc chọn lọc phần giới thiệu, cách dùng, giới hạn, license, metadata manifest và CI hiện diện. Chưa kiểm đầy đủ implementation hoặc chạy upstream; các số đo của tác giả chưa được tái lập.

**Nguồn:** [README.md](https://github.com/MunGell/awesome-for-beginners/blob/f7bf7d43cb26d555e51a4c6c83af563a08795605/README.md) · [.github/workflows/build.yml](https://github.com/MunGell/awesome-for-beginners/blob/f7bf7d43cb26d555e51a4c6c83af563a08795605/.github/workflows/build.yml) · [metadata GitHub](https://api.github.com/repos/MunGell/awesome-for-beginners).

<a id="anhkysuai-2026-11-23-developer-y-cs-video-courses"></a>

### cs-video-courses

**Repo:** [Developer-Y/cs-video-courses](https://github.com/Developer-Y/cs-video-courses) · **License:** Chưa xác lập ở phạm vi đã đọc · **★ 84,915 (GitHub API, 2026-11-23)**

**Mục đích:** Danh sách khóa học khoa học máy tính có video bài giảng ở cấp đại học.

**Giá trị:** Phân nhóm nền tảng, hệ thống, AI, mạng và toán giúp tìm chuỗi bài học có chiều sâu.

**Giới hạn:** Repo chỉ dẫn tài nguyên, không cấp quyền video/tài liệu của trường; yêu cầu kiến thức đầu vào, khả năng truy cập và độ mới cần kiểm từng khóa. Chưa xác lập giấy phép chung cho nội dung chính ở phạm vi đã đọc; không suy quyền tái sử dụng từ repo công khai.

**Cách tham khảo/tích hợp:** Chọn bài theo mục tiêu, thực hành lại trên môi trường riêng và kiểm bằng bài chuyển giao; khi dùng lại nội dung phải đối chiếu giấy phép đúng phạm vi.

**Lựa chọn để đối chiếu:** [ossu/computer-science](https://github.com/ossu/computer-science) · [papers-we-love/papers-we-love](https://github.com/papers-we-love/papers-we-love). Đây là ứng viên so sánh theo tác vụ; mức phù hợp cần kiểm theo hồ sơ và phiên bản riêng.

**Bằng chứng:** `docs-read`, ngày 2026-11-23, commit [`dcaeff11aab30d18e74d19e5f9c61b962575eafe`](https://github.com/Developer-Y/cs-video-courses/commit/dcaeff11aab30d18e74d19e5f9c61b962575eafe), ngày commit 2026-11-21. Đã clone và đọc chọn lọc phần giới thiệu, cách dùng, giới hạn, license, metadata manifest và CI hiện diện. Chưa kiểm đầy đủ implementation hoặc chạy upstream; các số đo của tác giả chưa được tái lập.

**Nguồn:** [README.md](https://github.com/Developer-Y/cs-video-courses/blob/dcaeff11aab30d18e74d19e5f9c61b962575eafe/README.md) · [metadata GitHub](https://api.github.com/repos/Developer-Y/cs-video-courses).

<a id="anhkysuai-2026-11-23-d2l-ai-d2l-zh"></a>

### d2l-zh

**Repo:** [d2l-ai/d2l-zh](https://github.com/d2l-ai/d2l-zh) · **License:** Apache-2.0 · **★ 82,676 (GitHub API, 2026-11-23)**

**Mục đích:** Bản tiếng Trung Dive into Deep Learning kết hợp lý thuyết, công thức và notebook thực hành.

**Giá trị:** Tuyến chương nối toán, code và thử nghiệm; INFO.md giải thích cách dựng tài liệu có hoặc không thực thi notebook.

**Giới hạn:** HEAD bản tiếng Trung đã đọc từ 2023; cần kiểm tương thích framework và đồng bộ với ấn bản khác. LICENSE gốc Apache-2.0 chưa thay việc kiểm quyền nội dung sách/ảnh khi tái xuất bản.

**Cách tham khảo/tích hợp:** Chọn bài theo mục tiêu, thực hành lại trên môi trường riêng và kiểm bằng bài chuyển giao; khi dùng lại nội dung phải đối chiếu giấy phép đúng phạm vi.

**Lựa chọn để đối chiếu:** [GokuMohandas/Made-With-ML](https://github.com/GokuMohandas/Made-With-ML) · [microsoft/Data-Science-For-Beginners](https://github.com/microsoft/Data-Science-For-Beginners). Đây là ứng viên so sánh theo tác vụ; mức phù hợp cần kiểm theo hồ sơ và phiên bản riêng.

**Bằng chứng:** `docs-read`, ngày 2026-11-23, commit [`e6b18ccea71451a55fcd861d7b96fddf2587b09a`](https://github.com/d2l-ai/d2l-zh/commit/e6b18ccea71451a55fcd861d7b96fddf2587b09a), ngày commit 2023-08-17. Đã clone và đọc chọn lọc phần giới thiệu, cách dùng, giới hạn, license, metadata manifest và CI hiện diện. Chưa kiểm đầy đủ implementation hoặc chạy upstream; các số đo của tác giả chưa được tái lập.

**Nguồn:** [README.md](https://github.com/d2l-ai/d2l-zh/blob/e6b18ccea71451a55fcd861d7b96fddf2587b09a/README.md) · [LICENSE](https://github.com/d2l-ai/d2l-zh/blob/e6b18ccea71451a55fcd861d7b96fddf2587b09a/LICENSE) · [.github/workflows/ci.yml](https://github.com/d2l-ai/d2l-zh/blob/e6b18ccea71451a55fcd861d7b96fddf2587b09a/.github/workflows/ci.yml) · [index.md](https://github.com/d2l-ai/d2l-zh/blob/e6b18ccea71451a55fcd861d7b96fddf2587b09a/index.md) · [INFO.md](https://github.com/d2l-ai/d2l-zh/blob/e6b18ccea71451a55fcd861d7b96fddf2587b09a/INFO.md) · [metadata GitHub](https://api.github.com/repos/d2l-ai/d2l-zh).

<a id="anhkysuai-2026-11-23-enaqx-awesome-react"></a>

### awesome-react

**Repo:** [enaqx/awesome-react](https://github.com/enaqx/awesome-react) · **License:** Chưa xác lập ở phạm vi đã đọc · **★ 75,386 (GitHub API, 2026-11-23)**

**Mục đích:** Danh mục tài nguyên React/React Native, tutorial, thư viện và kiến trúc ứng dụng.

**Giá trị:** Hữu ích tìm đường dẫn theo chủ đề trước khi đọc tài liệu chính thức hoặc mã repo liên quan.

**Giới hạn:** README nhấn mạnh tài nguyên miễn phí nhưng chưa thấy giấy phép chung; danh sách có tính lịch sử, cần kiểm phiên bản React và tình trạng bảo trì từng thư viện. Chưa xác lập giấy phép chung cho nội dung chính ở phạm vi đã đọc; không suy quyền tái sử dụng từ repo công khai.

**Cách tham khảo/tích hợp:** Dùng làm chỉ mục tìm ứng viên, dẫn về nguồn gốc rồi kiểm phiên bản, giấy phép và mức bảo trì của từng lựa chọn trước tích hợp.

**Lựa chọn để đối chiếu:** [jondot/awesome-react-native](https://github.com/jondot/awesome-react-native) · [yangshun/front-end-interview-handbook](https://github.com/yangshun/front-end-interview-handbook). Đây là ứng viên so sánh theo tác vụ; mức phù hợp cần kiểm theo hồ sơ và phiên bản riêng.

**Bằng chứng:** `docs-read`, ngày 2026-11-23, commit [`e6fd973eefe57d288a60e6d21bb9d8f343addfe9`](https://github.com/enaqx/awesome-react/commit/e6fd973eefe57d288a60e6d21bb9d8f343addfe9), ngày commit 2026-09-04. Đã clone và đọc chọn lọc phần giới thiệu, cách dùng, giới hạn, license, metadata manifest và CI hiện diện. Chưa kiểm đầy đủ implementation hoặc chạy upstream; các số đo của tác giả chưa được tái lập.

**Nguồn:** [README.md](https://github.com/enaqx/awesome-react/blob/e6fd973eefe57d288a60e6d21bb9d8f343addfe9/README.md) · [metadata GitHub](https://api.github.com/repos/enaqx/awesome-react).

<a id="anhkysuai-2026-11-23-avik-jain-100-days-of-ml-code"></a>

### 100-Days-Of-ML-Code

**Repo:** [Avik-Jain/100-Days-Of-ML-Code](https://github.com/Avik-Jain/100-Days-Of-ML-Code) · **License:** MIT · **★ 52,078 (GitHub API, 2026-11-23)**

**Mục đích:** Chuỗi bài thực hành machine learning theo ngày, từ tiền xử lý tới các thuật toán cơ bản.

**Giá trị:** Có minh họa và liên kết code/dataset, phù hợp dùng như bộ bài tập nền tảng.

**Giới hạn:** Commit được clone từ năm 2020; cần cập nhật API thư viện, cách chia dữ liệu và kiểm quyền dataset. Mốc 100 ngày không bảo đảm kết quả học tập.

**Cách tham khảo/tích hợp:** Chọn bài theo mục tiêu, thực hành lại trên môi trường riêng và kiểm bằng bài chuyển giao; khi dùng lại nội dung phải đối chiếu giấy phép đúng phạm vi.

**Lựa chọn để đối chiếu:** [GokuMohandas/Made-With-ML](https://github.com/GokuMohandas/Made-With-ML) · [d2l-ai/d2l-zh](https://github.com/d2l-ai/d2l-zh). Đây là ứng viên so sánh theo tác vụ; mức phù hợp cần kiểm theo hồ sơ và phiên bản riêng.

**Bằng chứng:** `docs-read`, ngày 2026-11-23, commit [`5d67810c1498082e7bb262cf6397d7861dfd9891`](https://github.com/Avik-Jain/100-Days-Of-ML-Code/commit/5d67810c1498082e7bb262cf6397d7861dfd9891), ngày commit 2020-07-15. Đã clone và đọc chọn lọc phần giới thiệu, cách dùng, giới hạn, license, metadata manifest và CI hiện diện. Chưa kiểm đầy đủ implementation hoặc chạy upstream; các số đo của tác giả chưa được tái lập.

**Nguồn:** [README.md](https://github.com/Avik-Jain/100-Days-Of-ML-Code/blob/5d67810c1498082e7bb262cf6397d7861dfd9891/README.md) · [LICENSE](https://github.com/Avik-Jain/100-Days-Of-ML-Code/blob/5d67810c1498082e7bb262cf6397d7861dfd9891/LICENSE) · [metadata GitHub](https://api.github.com/repos/Avik-Jain/100-Days-Of-ML-Code).

<a id="anhkysuai-2026-11-23-gokumohandas-made-with-ml"></a>

### Made-With-ML

**Repo:** [GokuMohandas/Made-With-ML](https://github.com/GokuMohandas/Made-With-ML) · **License:** MIT · **★ 50,134 (GitHub API, 2026-11-23)**

**Mục đích:** Khóa học kết hợp ML và kỹ nghệ phần mềm từ thiết kế đến triển khai, đánh giá và vận hành.

**Giá trị:** Liên kết experiment tracking, testing, serving và rollback trong cùng quy trình phát triển ứng dụng ML.

**Giới hạn:** Một số luồng production dùng Anyscale/AWS và credentials; cần kiểm chi phí, phiên bản và quyền trước chạy. Tuyên bố production-grade chưa được xác minh bằng triển khai ở lượt này.

**Cách tham khảo/tích hợp:** Chọn bài theo mục tiêu, thực hành lại trên môi trường riêng và kiểm bằng bài chuyển giao; khi dùng lại nội dung phải đối chiếu giấy phép đúng phạm vi.

**Lựa chọn để đối chiếu:** [DataTalksClub/data-engineering-zoomcamp](https://github.com/DataTalksClub/data-engineering-zoomcamp) · [d2l-ai/d2l-zh](https://github.com/d2l-ai/d2l-zh). Đây là ứng viên so sánh theo tác vụ; mức phù hợp cần kiểm theo hồ sơ và phiên bản riêng.

**Bằng chứng:** `docs-read`, ngày 2026-11-23, commit [`3361aeb8ddfc2affdba9f545c978c38c85cee764`](https://github.com/GokuMohandas/Made-With-ML/commit/3361aeb8ddfc2affdba9f545c978c38c85cee764), ngày commit 2026-03-04. Đã clone và đọc chọn lọc phần giới thiệu, cách dùng, giới hạn, license, metadata manifest và CI hiện diện. Chưa kiểm đầy đủ implementation hoặc chạy upstream; các số đo của tác giả chưa được tái lập.

**Nguồn:** [README.md](https://github.com/GokuMohandas/Made-With-ML/blob/3361aeb8ddfc2affdba9f545c978c38c85cee764/README.md) · [LICENSE](https://github.com/GokuMohandas/Made-With-ML/blob/3361aeb8ddfc2affdba9f545c978c38c85cee764/LICENSE) · [pyproject.toml](https://github.com/GokuMohandas/Made-With-ML/blob/3361aeb8ddfc2affdba9f545c978c38c85cee764/pyproject.toml) · [.github/workflows/serve.yaml](https://github.com/GokuMohandas/Made-With-ML/blob/3361aeb8ddfc2affdba9f545c978c38c85cee764/.github/workflows/serve.yaml) · [metadata GitHub](https://api.github.com/repos/GokuMohandas/Made-With-ML).

<a id="anhkysuai-2026-11-23-floodsung-deep-learning-papers-reading-roadmap"></a>

### Deep-Learning-Papers-Reading-Roadmap

**Repo:** [floodsung/Deep-Learning-Papers-Reading-Roadmap](https://github.com/floodsung/Deep-Learning-Papers-Reading-Roadmap) · **License:** Chưa xác lập ở phạm vi đã đọc · **★ 39,608 (GitHub API, 2026-11-23)**

**Mục đích:** Lộ trình đọc paper deep learning từ nền tảng tới các nhánh kiến trúc và ứng dụng.

**Giá trị:** Có giá trị tham khảo lịch sử phát triển và thứ tự đọc các công trình nền tảng.

**Giới hạn:** HEAD đã đọc từ 2022 nên cụm state-of-the-art trong README không phản ánh đầy đủ hiện tại; không thấy giấy phép chung và paper giữ bản quyền riêng. Chưa xác lập giấy phép chung cho nội dung chính ở phạm vi đã đọc; không suy quyền tái sử dụng từ repo công khai.

**Cách tham khảo/tích hợp:** Chọn bài theo mục tiêu, thực hành lại trên môi trường riêng và kiểm bằng bài chuyển giao; khi dùng lại nội dung phải đối chiếu giấy phép đúng phạm vi.

**Lựa chọn để đối chiếu:** [papers-we-love/papers-we-love](https://github.com/papers-we-love/papers-we-love) · [satellite-image-deep-learning/techniques](https://github.com/satellite-image-deep-learning/techniques). Đây là ứng viên so sánh theo tác vụ; mức phù hợp cần kiểm theo hồ sơ và phiên bản riêng.

**Bằng chứng:** `docs-read`, ngày 2026-11-23, commit [`a994642f82f071926fcb472bcf6cd63e4abba7ab`](https://github.com/floodsung/Deep-Learning-Papers-Reading-Roadmap/commit/a994642f82f071926fcb472bcf6cd63e4abba7ab), ngày commit 2022-02-07. Đã clone và đọc chọn lọc phần giới thiệu, cách dùng, giới hạn, license, metadata manifest và CI hiện diện. Chưa kiểm đầy đủ implementation hoặc chạy upstream; các số đo của tác giả chưa được tái lập.

**Nguồn:** [README.md](https://github.com/floodsung/Deep-Learning-Papers-Reading-Roadmap/blob/a994642f82f071926fcb472bcf6cd63e4abba7ab/README.md) · [metadata GitHub](https://api.github.com/repos/floodsung/Deep-Learning-Papers-Reading-Roadmap).

<a id="anhkysuai-2026-11-23-accumulatemore-cv"></a>

### CV

**Repo:** [AccumulateMore/CV](https://github.com/AccumulateMore/CV) · **License:** Chưa xác lập ở phạm vi đã đọc · **★ 24,337 (GitHub API, 2026-11-23)**

**Mục đích:** Bộ ghi chú tiếng Trung từ các khóa deep learning, PyTorch, NLP và agent.

**Giá trị:** Tổ chức theo số bài và nguồn video, thuận tiện đối chiếu lại nội dung khi tự học.

**Giới hạn:** Không thấy giấy phép chung ở gốc; ghi chú/video/dataset có thể có quyền khác nhau. README còn placeholder cho khóa tương lai nên không coi toàn bộ mục đã hoàn tất. Chưa xác lập giấy phép chung cho nội dung chính ở phạm vi đã đọc; không suy quyền tái sử dụng từ repo công khai.

**Cách tham khảo/tích hợp:** Chọn bài theo mục tiêu, thực hành lại trên môi trường riêng và kiểm bằng bài chuyển giao; khi dùng lại nội dung phải đối chiếu giấy phép đúng phạm vi.

**Lựa chọn để đối chiếu:** [d2l-ai/d2l-zh](https://github.com/d2l-ai/d2l-zh) · [microsoft/Data-Science-For-Beginners](https://github.com/microsoft/Data-Science-For-Beginners). Đây là ứng viên so sánh theo tác vụ; mức phù hợp cần kiểm theo hồ sơ và phiên bản riêng.

**Bằng chứng:** `docs-read`, ngày 2026-11-23, commit [`e05116c8336e8dd4da56118970ae45a3e358e0d3`](https://github.com/AccumulateMore/CV/commit/e05116c8336e8dd4da56118970ae45a3e358e0d3), ngày commit 2026-09-20. Đã clone và đọc chọn lọc phần giới thiệu, cách dùng, giới hạn, license, metadata manifest và CI hiện diện. Chưa kiểm đầy đủ implementation hoặc chạy upstream; các số đo của tác giả chưa được tái lập.

**Nguồn:** [README.md](https://github.com/AccumulateMore/CV/blob/e05116c8336e8dd4da56118970ae45a3e358e0d3/README.md) · [metadata GitHub](https://api.github.com/repos/AccumulateMore/CV).

<a id="anhkysuai-2026-11-23-datawhalechina-easy-vibe"></a>

### easy-vibe

**Repo:** [datawhalechina/easy-vibe](https://github.com/datawhalechina/easy-vibe) · **License:** CC-BY-NC-SA-4.0 · **★ 20,502 (GitHub API, 2026-11-23)**

**Mục đích:** Khóa nhập môn xây sản phẩm với AI, có lộ trình từ prototype đến frontend/backend và workflow agent.

**Giá trị:** Tuyến học theo mục tiêu và demo tương tác giúp người mới chia một ý tưởng thành các bước thực hành.

**Giới hạn:** Nội dung CC BY-NC-SA 4.0; công cụ/dịch vụ AI liên kết có chi phí và điều khoản riêng. Dựng được demo chưa chứng minh bảo mật, kiểm thử và vận hành production.

**Cách tham khảo/tích hợp:** Chọn bài theo mục tiêu, thực hành lại trên môi trường riêng và kiểm bằng bài chuyển giao; khi dùng lại nội dung phải đối chiếu giấy phép đúng phạm vi.

**Lựa chọn để đối chiếu:** [firstcontributions/first-contributions](https://github.com/firstcontributions/first-contributions) · [github/opensource.guide](https://github.com/github/opensource.guide). Đây là ứng viên so sánh theo tác vụ; mức phù hợp cần kiểm theo hồ sơ và phiên bản riêng.

**Bằng chứng:** `docs-read`, ngày 2026-11-23, commit [`f2239c67052b6ad9ae3e72bc6b7a76f3c903cf64`](https://github.com/datawhalechina/easy-vibe/commit/f2239c67052b6ad9ae3e72bc6b7a76f3c903cf64), ngày commit 2026-10-22. Đã clone và đọc chọn lọc phần giới thiệu, cách dùng, giới hạn, license, metadata manifest và CI hiện diện. Chưa kiểm đầy đủ implementation hoặc chạy upstream; các số đo của tác giả chưa được tái lập.

**Nguồn:** [README.md](https://github.com/datawhalechina/easy-vibe/blob/f2239c67052b6ad9ae3e72bc6b7a76f3c903cf64/README.md) · [package.json](https://github.com/datawhalechina/easy-vibe/blob/f2239c67052b6ad9ae3e72bc6b7a76f3c903cf64/package.json) · [.github/workflows/deploy.yml](https://github.com/datawhalechina/easy-vibe/blob/f2239c67052b6ad9ae3e72bc6b7a76f3c903cf64/.github/workflows/deploy.yml) · [metadata GitHub](https://api.github.com/repos/datawhalechina/easy-vibe).

## Nguồn

- https://gitstarclub.com/rankings · https://www.countly.net/most-starred-github-repositories-june-2026 · https://www.stackscan.com/blog/github-statistics · https://github.com/EvanLi/Github-Ranking · https://www.firecrawl.dev/blog/best-github-repos
- https://github.com/Shubhamsaboo/awesome-llm-apps · https://github.com/hesreallyhim/awesome-claude-code · https://github.com/rohitg00/awesome-claude-code-toolkit · https://claudefa.st/blog/tools/resources/awesome-claude-code · https://github.com/topics/agent-skills · https://github.com/topics/claude-skills
- https://github.com/kaushikb11/awesome-llm-agents · https://github.com/aloth/awesome-ai-agents
- §2b (12/10/2026): https://github.com/microsoft/generative-ai-for-beginners · https://github.com/rasbt/LLMs-from-scratch · https://github.com/mlabonne/llm-course · https://github.com/microsoft/ai-agents-for-beginners · https://github.com/labmlai/annotated_deep_learning_paper_implementations · https://github.com/karpathy/nanochat · https://github.com/karpathy/nanoGPT · https://github.com/karpathy/llm.c · https://github.com/huggingface/agents-course · https://github.com/NirDiamant/RAG_Techniques · https://github.com/NirDiamant/GenAI_Agents · https://github.com/chiphuyen/aie-book · https://github.com/datawhalechina/happy-llm (34,3k★, tiếng Trung, CC BY-NC-SA)
- §2c ảnh "AI Engineer Interview Questions" (12/10/2026): https://www.linkedin.com/in/rathanuday · https://www.linkedin.com/posts/rathanuday_ai-agents-dont-fail-because-theyre-not-activity-7411823219176865792-xB4z · https://www.zoominfo.com/p/Rathnakumar-Udayakumar/-1632233212 (bên thứ ba) · https://www.goodreads.com/author/show/29625821.Rathnakumar_Udayakumar · kiểm nội dung: https://arxiv.org/abs/1706.03762 (§3.1 post-LN) · https://arxiv.org/abs/2002.04745 (Pre-LN) · https://arxiv.org/abs/2302.13971 (LLaMA, RMSNorm) · https://arxiv.org/abs/2303.16634 (G-Eval: BLEU/ROUGE tương quan thấp với người) · https://www.anthropic.com/engineering/building-effective-agents · https://www.anthropic.com/engineering/multi-agent-research-system (4×/15× token) · https://platform.claude.com/docs/en/agents-and-tools/tool-use/overview · https://genai.owasp.org/llmrisk/llm01-prompt-injection/ · tài liệu ôn: https://github.com/chiphuyen/aie-book, https://github.com/KalyanKS-NLP/LLM-Interview-Questions-and-Answers-Hub, https://github.com/amitshekhariitbhu/ai-engineering-interview-questions, https://github.com/alexeygrigorev/data-science-interviews, https://github.com/chiphuyen/ml-interviews-book, https://github.com/Devinterview-io/llms-interview-questions, https://github.com/llmgenai/LLMInterviewQuestions
- §2d (12/10/2026): https://github.com/cporter202/automate-for-growth (clone đầy đủ, 9 commit, HEAD 2cc3193) · https://viralwavestudio.com · bản sao 0★: arnelnrose/automate_for_growth, klikydigital/automate-for-growth
- §2e ảnh "Layers of AI" (13/10/2026): https://aiforleaders.com (FAQ: Adam Danyal, Julia Danyal) · bản đăng lại trên LinkedIn: https://de.linkedin.com/in/meheli-sinha, https://sa.linkedin.com/in/alhadlaq · kiểm nội dung: https://cvw.cac.cornell.edu/AI-overview/machine-learning/functionality-and-implementation (sơ đồ lồng nhau là quy ước dạy học) · https://lib.conestogac.on.ca/genai/learn-more · https://aima.cs.berkeley.edu · https://github.com/aimacode/aima-python · https://langchain.com/blog/the-anatomy-of-an-agent-harness
- §2d.1 (13/10/2026): https://github.com/cporter202/make-com-automation-recipes (clone đầy đủ, 4 commit, HEAD 6fa1e09; 16★ shields) · https://www.make.com/en/templates (gallery chính thức; thử https://www.make.com/templates/11218, /10893 → 200) · https://n8n.io/workflows
- §2d.2 (16/10/2026): https://github.com/cporter202/ai-growth-stack (clone đầy đủ, 7 commit 21/12/2025, chỉ README.md; 229★/70 fork shields) · https://rapidapi.com/user/contact-_OGid12Eu (trang cần JavaScript, không đọc được danh sách) · https://apidataframe.com (9 API, chỉ qua RapidAPI, không tên người vận hành) · https://github.com/cporter202 (40 repo, bio ViralWaveStudio.com) · https://www.buymeacoffee.com/viralwavestudio
- §2g (16/10/2026): https://www.kdnuggets.com/the-roadmap-to-mastering-agentic-ai-systems-in-2026 (Vinod Chugani, 13/10/2026, đọc toàn bài) · https://github.com/microsoft/autogen (README: "now in maintenance mode… New users should start with Microsoft Agent Framework"; 61,4k★) · https://www.anthropic.com/engineering/multi-agent-research-system (13/6/2025: agent ~4×, multi-agent ~15× token so với chat) · https://www.anthropic.com/engineering/building-effective-agents · https://machinelearningmastery.com/the-roadmap-for-mastering-agentic-ai-in-2026/ (bài khác cùng chủ đề)
- §2f ảnh Brij "How to become an AI engineer in 2026" (13/10/2026): https://genai.owasp.org/llmrisk/llm01-prompt-injection/ ("unclear if there are fool-proof methods of prevention") · https://roadmap.sh/ai-engineer · https://github.com/chiphuyen/aie-book (README: chương fine-tuning, dataset engineering) · https://github.com/patchy631/ai-engineering-hub · shields.io: aie-book ~18k, ai-engineering-hub ~38k MIT, developer-roadmap ~369k, litellm ~61k

<a id="xlsx-2026-11-23"></a>

## Đánh giá bổ sung từ bảng "Top 100 GitHub AI Skills" — 23/11/2026

Phần này có **1 hồ sơ** từ bảng xlsx người dùng gửi ngày 2026-11-23; đọc bằng `git clone --depth 1`, không cài hay chạy mã upstream. Lúc đọc, REST API của GitHub bị chặn nên trong hồ sơ ★ và `pushed_at` ghi **(chưa xác minh)**; số sao lấy lại cùng ngày qua GitHub search API nằm trong `data/projects.json` và [catalog/](../catalog/README.md), `pushed_at` vẫn chưa xác minh.

<a id="xlsx-2026-11-23-awesome-agent-skills-jqueryscript"></a>

### awesome-agent-skills (jqueryscript)

**Repo:** [jqueryscript/awesome-agent-skills](https://github.com/jqueryscript/awesome-agent-skills) · **License:** huy hiệu README ghi CC BY 4.0; **không có file LICENSE** (GitHub API: không nhận diện) · **★ 16 (GitHub search API, 2026-11-23)**

**Mục đích:** Danh mục một file README về ~500 Agent Skill, xếp theo nhóm việc và sao GitHub; do ScriptByAI (jqueryscript) tuyển chọn. **Không phải** `VoltAgent/awesome-agent-skills` đã có trong catalog (khác chủ, khác repo).

**Giá trị và cơ chế:** Repo chỉ có `README.md` (856 dòng, 34 mục `##`, 498 dòng entry có `⭐`; README tự ghi 501). Chia theo nhóm việc (Official, Collections, Coding, UI, Review, Testing, Browser, Security, Docs, Research, …), kèm bảng "Skill vs MCP/Plugin/Prompt/Subagent", mục "Before Installing" và FAQ ghi rõ sao không bằng an toàn. Changelog theo tuần từ 2026-06-15; commit cuối 2026-11-19. Là nguồn tốt để phát hiện repo mới (gsap-skills, MiniMax-AI/skills, n8n-skills, WordPress/agent-skills đều nằm trong danh sách).

**Giới hạn:** Sao in trong README là ảnh chụp lúc cập nhật nhóm, đã lệch: `anthropics/skills` ghi 182,9k (API hôm nay 199.295), `gsap-skills` 16,9k (18.948), MiniMax 13,9k (13.903, khớp). Mô tả từng entry là câu tóm tắt của người tuyển chọn, không có bằng chứng đã đọc mã; mục đã loại không có. 36 commit, một tác giả; không CI, không script kiểm link. Giấy phép chỉ qua huy hiệu nên quyền tái dùng nội dung chưa rõ.

**Cách tham khảo/tích hợp:** Dùng làm danh sách ứng viên để đọc mã, không trích số sao. Lấy mẫu phân nhóm và mục "Before Installing" làm checklist thẩm định; không sao chép mô tả.

**Thay thế:** [VoltAgent/awesome-agent-skills](../08-awesome-lists-learning/README.md) (37.472★ theo search 2026-11-23; số trong catalog nên rà), [sickn33/agentic-awesome-skills](../08-awesome-lists-learning/README.md) (50.191★ theo search; catalog 48.916), `heilcheng/awesome-agent-skills` (6.424★), `libukai/awesome-agent-skills` (5.231★), hai bản sau chưa đọc.

**Bằng chứng:** `docs-read`, ngày 2026-11-23, commit [`f2f8eaca4f7e`](https://github.com/jqueryscript/awesome-agent-skills/commit/f2f8eaca4f7e107d22e682d49af6f4e266a7fdc3) (2026-11-19). Đọc toàn bộ cấu trúc, đầu/cuối README, các entry liên quan. Chưa kiểm từng link và từng skill được liệt kê.

**Nguồn:** [README.md](https://github.com/jqueryscript/awesome-agent-skills/blob/f2f8eaca4f7e107d22e682d49af6f4e266a7fdc3/README.md) · [metadata GitHub](https://api.github.com/search/repositories?q=repo:jqueryscript/awesome-agent-skills).

<a id="chuan-hoa-2026-11-23"></a>

## Chuẩn hóa bằng chứng hồ sơ cũ — 23/11/2026

Các hồ sơ dưới đây có từ trước khi kho ghi mức kiểm. Ngày 2026-11-23 mỗi repo được clone nông tại commit ghi trong bảng, đọc LICENSE, README, manifest và CI (nếu có); không cài, build hay chạy mã upstream. Nhận định cũ ở phần trên giữ nguyên; chỗ nào khác với lần đọc này được ghi trong cột Nhận định. Số sao lấy qua GitHub search API cùng ngày.

<a id="ch-agentic-awesome-skills"></a>

### Agentic Awesome Skills

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/sickn33/agentic-awesome-skills |
| License | MIT (code) + CC BY 4.0 (nội dung, LICENSE-CONTENT) |
| Phiên bản đã đọc | `a99b3d3bb6db184e75020f26714bce1951629356` (commit 2026-11-23) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE, LICENSE-CONTENT, package.json; chưa chạy upstream |
| Bảo trì | Commit mới nhất 2026-11-23 |
| Nhận định | Thư viện lớn các SKILL.md cho agent lập trình kèm công cụ AAS Core (tìm, xác thực, lập kế hoạch). Quy mô lớn nên cần soát từng skill trước khi cài; README nói tạm dừng publish npm, dùng GitHub để cập nhật. |
| Nguồn | [README.md](https://github.com/sickn33/agentic-awesome-skills/blob/a99b3d3bb6db184e75020f26714bce1951629356/README.md) · [LICENSE](https://github.com/sickn33/agentic-awesome-skills/blob/a99b3d3bb6db184e75020f26714bce1951629356/LICENSE) · [LICENSE-CONTENT](https://github.com/sickn33/agentic-awesome-skills/blob/a99b3d3bb6db184e75020f26714bce1951629356/LICENSE-CONTENT) · [package.json](https://github.com/sickn33/agentic-awesome-skills/blob/a99b3d3bb6db184e75020f26714bce1951629356/package.json) |

<a id="ch-agents-course"></a>

### agents-course

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/huggingface/agents-course |
| License | Apache-2.0 |
| Phiên bản đã đọc | `9b3d6b3887bc489510da0239d4c1bc1ee23fd40f` (commit 2026-11-03) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE; chưa chạy upstream |
| Bảo trì | Commit mới nhất 2026-11-03 |
| Nhận định | Khóa học agent của Hugging Face (từ nền tảng tới bài tập cuối có benchmark), nội dung chính nằm ở hf.co/learn. Chứng chỉ do HF cấp là tuyên bố cũ, **(chưa xác minh)**. |
| Nguồn | [README.md](https://github.com/huggingface/agents-course/blob/9b3d6b3887bc489510da0239d4c1bc1ee23fd40f/README.md) · [LICENSE](https://github.com/huggingface/agents-course/blob/9b3d6b3887bc489510da0239d4c1bc1ee23fd40f/LICENSE) |

<a id="ch-ai-agents-for-beginners"></a>

### ai-agents-for-beginners

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/microsoft/ai-agents-for-beginners |
| License | MIT |
| Phiên bản đã đọc | `3bee2ddf8e7aab27b17ef9e1d4a3f2c541a1913e` (commit 2026-11-16) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE; chưa chạy upstream |
| Bảo trì | Commit mới nhất 2026-11-16 |
| Nhận định | Khóa 18 bài về agent của Microsoft (khung agent, tool use, agentic RAG, đa agent, an toàn, triển khai...), có bản dịch hàng chục ngôn ngữ gồm tiếng Việt. Một số bài gắn dịch vụ Azure/Microsoft Agent Framework. |
| Nguồn | [README.md](https://github.com/microsoft/ai-agents-for-beginners/blob/3bee2ddf8e7aab27b17ef9e1d4a3f2c541a1913e/README.md) · [LICENSE](https://github.com/microsoft/ai-agents-for-beginners/blob/3bee2ddf8e7aab27b17ef9e1d4a3f2c541a1913e/LICENSE) |

<a id="ch-ai-engineering-from-scratch"></a>

### AI Engineering from Scratch

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/rohitg00/ai-engineering-from-scratch |
| License | MIT |
| Phiên bản đã đọc | `9712e323fde8cb2ec933310ac619e920e8e31017` (commit 2026-11-18) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE, package.json, .github/workflows/translate.yml; chưa chạy upstream |
| Bảo trì | Commit mới nhất 2026-11-18 |
| Nhận định | Khóa AI engineering từ cơ bản, 20 phase/542 bài, kèm cheatsheet, phỏng vấn, dự án. Bản i18n là dịch máy nên chất lượng cần kiểm khi dùng; chưa chạy code bài học. |
| Nguồn | [README.md](https://github.com/rohitg00/ai-engineering-from-scratch/blob/9712e323fde8cb2ec933310ac619e920e8e31017/README.md) · [LICENSE](https://github.com/rohitg00/ai-engineering-from-scratch/blob/9712e323fde8cb2ec933310ac619e920e8e31017/LICENSE) · [package.json](https://github.com/rohitg00/ai-engineering-from-scratch/blob/9712e323fde8cb2ec933310ac619e920e8e31017/package.json) · [.github/workflows/translate.yml](https://github.com/rohitg00/ai-engineering-from-scratch/blob/9712e323fde8cb2ec933310ac619e920e8e31017/.github/workflows/translate.yml) |

<a id="ch-ai-engineering-interview-questions"></a>

### ai-engineering-interview-questions

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/amitshekhariitbhu/ai-engineering-interview-questions |
| License | Apache-2.0 |
| Phiên bản đã đọc | `ceb74cd826db44450e42884914972b4a9de72813` (commit 2026-11-23) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE; chưa chạy upstream |
| Bảo trì | Commit mới nhất 2026-11-23 |
| Nhận định | Danh sách câu hỏi/đáp phỏng vấn AI engineering (RAG, agent, MCP, LLMOps...), phần lớn dạng tài liệu một file; độ chính xác đáp án là tuyên bố của tác giả **(chưa xác minh)**. |
| Nguồn | [README.md](https://github.com/amitshekhariitbhu/ai-engineering-interview-questions/blob/ceb74cd826db44450e42884914972b4a9de72813/README.md) · [LICENSE](https://github.com/amitshekhariitbhu/ai-engineering-interview-questions/blob/ceb74cd826db44450e42884914972b4a9de72813/LICENSE) |

<a id="ch-ai-growth-stack"></a>

### ai-growth-stack

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/cporter202/ai-growth-stack |
| License | không có file LICENSE |
| Phiên bản đã đọc | `efed75900404a033c0e3dc4dc2d6ad7f502d3cf4` (commit 2026-10-17) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md; chưa chạy upstream |
| Bảo trì | Commit mới nhất 2026-10-17 (clone nông không xem được lịch sử); ghi chú cũ nói không đổi từ 12/2025 |
| Nhận định | Danh mục 6 "API" quảng bá qua RapidAPI, thực chất chỉ là một README quảng cáo, không có mã hay giấy phép. Badge STATUS ACTIVE là tuyên bố của tác giả **(chưa xác minh)**; không đáng làm nguồn kỹ thuật. |
| Nguồn | [README.md](https://github.com/cporter202/ai-growth-stack/blob/efed75900404a033c0e3dc4dc2d6ad7f502d3cf4/README.md) |

<a id="ch-aie-book"></a>

### aie-book

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/chiphuyen/aie-book |
| License | không có file LICENSE |
| Phiên bản đã đọc | `f375e0065ef19e4f411b809a2f9a2d65582db287` (commit 2026-07-03) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md; chưa chạy upstream |
| Bảo trì | Commit mới nhất 2026-07-03 |
| Nhận định | Tài liệu đồng hành sách AI Engineering của Chip Huyen (mục lục, tóm tắt chương, tài nguyên). Không có giấy phép nên chỉ nên dẫn liên kết, không sao chép. |
| Nguồn | [README.md](https://github.com/chiphuyen/aie-book/blob/f375e0065ef19e4f411b809a2f9a2d65582db287/README.md) |

<a id="ch-aima-python"></a>

### aima-python

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/aimacode/aima-python |
| License | MIT |
| Phiên bản đã đọc | `c12988eddcaeedd3365fd718a4e165178549d528` (commit 2026-11-20) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE, pyproject.toml; chưa chạy upstream |
| Bảo trì | Commit mới nhất 2026-11-20 |
| Nhận định | Code Python cho giáo trình AIMA (search, logic, planning, ML, agent), có notebook, tests và docs; có CI (tests, docs). Phù hợp học thuật hơn là dùng sản xuất. |
| Nguồn | [README.md](https://github.com/aimacode/aima-python/blob/c12988eddcaeedd3365fd718a4e165178549d528/README.md) · [LICENSE](https://github.com/aimacode/aima-python/blob/c12988eddcaeedd3365fd718a4e165178549d528/LICENSE) · [pyproject.toml](https://github.com/aimacode/aima-python/blob/c12988eddcaeedd3365fd718a4e165178549d528/pyproject.toml) |

<a id="ch-annotated-deep-learning-paper-implementations"></a>

### annotated_deep_learning_paper_implementations

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/labmlai/annotated_deep_learning_paper_implementations |
| License | MIT |
| Phiên bản đã đọc | `db59a04a8a2c6af922f1656f8c0fd113dd9a51b8` (commit 2026-11-01) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc readme.md, license, setup.py; chưa chạy upstream |
| Bảo trì | Commit mới nhất 2026-11-01 |
| Nhận định | Bộ cài đặt PyTorch có chú thích cạnh code cho nhiều paper (transformer, GAN, RL, diffusion...), site nn.labml.ai. Gói pip phụ thuộc torchtext cũ nên cài nguyên gói có thể lỗi (chưa xác minh), dùng đọc là chính. |
| Nguồn | [readme.md](https://github.com/labmlai/annotated_deep_learning_paper_implementations/blob/db59a04a8a2c6af922f1656f8c0fd113dd9a51b8/readme.md) · [license](https://github.com/labmlai/annotated_deep_learning_paper_implementations/blob/db59a04a8a2c6af922f1656f8c0fd113dd9a51b8/license) · [setup.py](https://github.com/labmlai/annotated_deep_learning_paper_implementations/blob/db59a04a8a2c6af922f1656f8c0fd113dd9a51b8/setup.py) |

<a id="ch-automate-for-growth"></a>

### automate-for-growth

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/cporter202/automate-for-growth |
| License | không có file LICENSE |
| Phiên bản đã đọc | `29d439dd167c5b63681dcd0d5e09a9f816ae3c25` (commit 2026-10-17) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md; chưa chạy upstream |
| Bảo trì | Commit mới nhất 2026-10-17 (clone nông); ghi chú cũ nói dừng từ 12/2025 |
| Nhận định | "Khóa học" tự động hóa nội dung mạng xã hội gồm các module markdown, không có mã chạy được chứng minh; nội dung mang tính quảng bá (nhận định phễu quảng cáo ViralWave là của lần đọc trước, chưa xác minh lại đầy đủ). Không giấy phép; nên tránh. |
| Nguồn | [README.md](https://github.com/cporter202/automate-for-growth/blob/29d439dd167c5b63681dcd0d5e09a9f816ae3c25/README.md) |

<a id="ch-awesome-ai-agents-e2b"></a>

### Awesome AI Agents (E2B)

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/e2b-dev/awesome-ai-agents |
| License | CC-BY-NC-SA-4.0 |
| Phiên bản đã đọc | `9596ab1e69fbbb6c95291141c8dab5c181083216` (commit 2026-08-21) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE.md; chưa chạy upstream |
| Bảo trì | Commit mới nhất 2026-08-21; ghi chú cũ nói phần lớn commit gần đây chỉ gắn UTM |
| Nhận định | Danh sách khoảng 200 agent AI do E2B bảo trì, ít cập nhật nội dung. License phi thương mại hạn chế dùng lại; tình trạng link chết là kết quả thử cũ, không kiểm lại. |
| Nguồn | [README.md](https://github.com/e2b-dev/awesome-ai-agents/blob/9596ab1e69fbbb6c95291141c8dab5c181083216/README.md) · [LICENSE.md](https://github.com/e2b-dev/awesome-ai-agents/blob/9596ab1e69fbbb6c95291141c8dab5c181083216/LICENSE.md) |

<a id="ch-awesome-claude-code"></a>

### awesome-claude-code

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/hesreallyhim/awesome-claude-code |
| License | CC-BY-NC-ND-4.0 (khác catalog cũ: không có) |
| Phiên bản đã đọc | `325e7162b39f6698c76d69e221489f21f433effe` (commit 2026-11-23) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE; chưa chạy upstream |
| Bảo trì | Commit mới nhất 2026-11-23 |
| Nhận định | Danh sách tuyển chọn tài nguyên cho Claude Code (skill, hook, lệnh, công cụ), sinh README từ CSV/YAML. License NC-ND hạn chế sao chép/phái sinh nên chỉ nên dẫn liên kết. |
| Nguồn | [README.md](https://github.com/hesreallyhim/awesome-claude-code/blob/325e7162b39f6698c76d69e221489f21f433effe/README.md) · [LICENSE](https://github.com/hesreallyhim/awesome-claude-code/blob/325e7162b39f6698c76d69e221489f21f433effe/LICENSE) |

<a id="ch-awesome-design-systems"></a>

### awesome-design-systems

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/klaufel/awesome-design-systems |
| License | CC0-1.0 |
| Phiên bản đã đọc | `dc4d0202e58884000bd4b03f871260bd38a4b03c` (commit 2026-11-10) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE; chưa chạy upstream |
| Bảo trì | Commit mới nhất 2026-11-10 |
| Nhận định | Danh sách tuyển chọn tài liệu và bài viết về design system hướng tới lập trình viên. Công khai tên miền công cộng, rủi ro license thấp; độ sống của liên kết chưa kiểm. |
| Nguồn | [README.md](https://github.com/klaufel/awesome-design-systems/blob/dc4d0202e58884000bd4b03f871260bd38a4b03c/README.md) · [LICENSE](https://github.com/klaufel/awesome-design-systems/blob/dc4d0202e58884000bd4b03f871260bd38a4b03c/LICENSE) |

<a id="ch-awesome-generative-ai-guide"></a>

### Awesome Generative AI Guide

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/aishwaryanr/awesome-generative-ai-guide |
| License | MIT |
| Phiên bản đã đọc | `3a067b647eba7022606c49056dfa5d167181e61f` (commit 2026-11-02) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE.md; chưa chạy upstream |
| Bảo trì | Commit mới nhất 2026-11-02 |
| Nhận định | Kho tổng hợp khóa học, lộ trình, ôn phỏng vấn và cập nhật nghiên cứu GenAI. Quảng cáo khóa trả phí và kết quả thử link (9/10 sống) là ghi chú cũ, chưa kiểm lại. |
| Nguồn | [README.md](https://github.com/aishwaryanr/awesome-generative-ai-guide/blob/3a067b647eba7022606c49056dfa5d167181e61f/README.md) · [LICENSE.md](https://github.com/aishwaryanr/awesome-generative-ai-guide/blob/3a067b647eba7022606c49056dfa5d167181e61f/LICENSE.md) |

<a id="ch-awesome-generative-ui"></a>

### awesome-generative-ui

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/narrowin/awesome-generative-ui |
| License | CC-BY-4.0 |
| Phiên bản đã đọc | `3a8f2a9de6a76495a5ca8b0373aeb5512f8a3ddc` (commit 2026-10-26) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE; chưa chạy upstream |
| Bảo trì | Commit mới nhất 2026-10-26 |
| Nhận định | Danh sách tuyển chọn tài nguyên cho UI sinh bởi AI (LLM sinh/ghép component). Yêu cầu ghi công theo CC BY; kho nhỏ, chủ yếu liên kết ngoài. |
| Nguồn | [README.md](https://github.com/narrowin/awesome-generative-ui/blob/3a8f2a9de6a76495a5ca8b0373aeb5512f8a3ddc/README.md) · [LICENSE](https://github.com/narrowin/awesome-generative-ui/blob/3a8f2a9de6a76495a5ca8b0373aeb5512f8a3ddc/LICENSE) |

<a id="ch-awesome-github-copilot"></a>

### Awesome GitHub Copilot

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/github/awesome-copilot |
| License | MIT |
| Phiên bản đã đọc | `f10fdb8b2660ce85c98f220b2f1ca24653768a5c` (commit 2026-11-20) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE, package.json; chưa chạy upstream |
| Bảo trì | Commit mới nhất 2026-11-20 |
| Nhận định | Kho cộng đồng do GitHub chính chủ duy trì: agent, instruction, skill, hook, plugin cho Copilot, có website tìm kiếm. Nội dung cộng đồng đóng góp nên cần soát trước khi dùng; chi tiết luật pr-risk-scan là ghi chú cũ, chưa xác minh. |
| Nguồn | [README.md](https://github.com/github/awesome-copilot/blob/f10fdb8b2660ce85c98f220b2f1ca24653768a5c/README.md) · [LICENSE](https://github.com/github/awesome-copilot/blob/f10fdb8b2660ce85c98f220b2f1ca24653768a5c/LICENSE) · [package.json](https://github.com/github/awesome-copilot/blob/f10fdb8b2660ce85c98f220b2f1ca24653768a5c/package.json) |

<a id="ch-awesome-llm-apps"></a>

### awesome-llm-apps

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/Shubhamsaboo/awesome-llm-apps |
| License | Apache-2.0 |
| Phiên bản đã đọc | `14c5f8ff0094659f321801385d2b52ccc65fea3b` (commit 2026-11-17) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE; chưa chạy upstream |
| Bảo trì | Commit mới nhất 2026-11-17 |
| Nhận định | Tuyển tập 100+ ứng dụng LLM/agent/RAG mẫu, mỗi ứng dụng tự đóng gói riêng; tuyên bố "tested end-to-end" của README **(chưa xác minh)**. Phụ thuộc khóa API nhiều nhà cung cấp. |
| Nguồn | [README.md](https://github.com/Shubhamsaboo/awesome-llm-apps/blob/14c5f8ff0094659f321801385d2b52ccc65fea3b/README.md) · [LICENSE](https://github.com/Shubhamsaboo/awesome-llm-apps/blob/14c5f8ff0094659f321801385d2b52ccc65fea3b/LICENSE) |

<a id="ch-awesome-mcp-servers"></a>

### awesome-mcp-servers

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/wong2/awesome-mcp-servers |
| License | MIT (khác catalog cũ: không có) |
| Phiên bản đã đọc | `39eb1d76d76e562657f3c657266a504cea159e23` (commit 2026-07-13) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE; chưa chạy upstream |
| Bảo trì | Commit mới nhất 2026-07-13; README ghi không nhận PR, gửi qua website |
| Nhận định | Danh sách MCP server tuyển chọn, README chuyển hướng việc đóng góp sang website. Commit gần nhất tháng 7/2026 nên có thể lệch so với website; có mục nhà tài trợ trong README. |
| Nguồn | [README.md](https://github.com/wong2/awesome-mcp-servers/blob/39eb1d76d76e562657f3c657266a504cea159e23/README.md) · [LICENSE](https://github.com/wong2/awesome-mcp-servers/blob/39eb1d76d76e562657f3c657266a504cea159e23/LICENSE) |

<a id="ch-awesome-openclaw-skills"></a>

### Awesome OpenClaw Skills

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/VoltAgent/awesome-openclaw-skills |
| License | MIT |
| Phiên bản đã đọc | `2ddb4d0ee520904c49cfd7f857535174cbd7669b` (commit 2026-11-18) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE, .github/workflows/pr-check.yml; chưa chạy upstream |
| Bảo trì | Commit mới nhất 2026-11-18 |
| Nhận định | Danh sách skill OpenClaw lấy từ ClawHub theo nhóm. Chỉ kiểm định dạng PR, không audit nội dung; cần tự soát skill trước khi cài. |
| Nguồn | [README.md](https://github.com/VoltAgent/awesome-openclaw-skills/blob/2ddb4d0ee520904c49cfd7f857535174cbd7669b/README.md) · [LICENSE](https://github.com/VoltAgent/awesome-openclaw-skills/blob/2ddb4d0ee520904c49cfd7f857535174cbd7669b/LICENSE) · [.github/workflows/pr-check.yml](https://github.com/VoltAgent/awesome-openclaw-skills/blob/2ddb4d0ee520904c49cfd7f857535174cbd7669b/.github/workflows/pr-check.yml) |

<a id="ch-cs336-assignment-1-basics"></a>

### CS336 Assignment 1 (Basics)

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/stanford-cs336/assignment1-basics |
| License | MIT |
| Phiên bản đã đọc | `a158843b20107949f1a8d7df1b05cd33b9166712` (commit 2026-04-07) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE, AGENTS.md, pyproject.toml; chưa chạy upstream |
| Bảo trì | Commit mới nhất 2026-04-07 |
| Nhận định | Bài tập 1 CS336 (xây LM từ đầu: BPE tokenizer, Transformer, AdamW) chấm bằng bộ test pytest và snapshot, không có CI. Số test/snapshot cụ thể chưa đếm; chưa chạy bài. |
| Nguồn | [README.md](https://github.com/stanford-cs336/assignment1-basics/blob/a158843b20107949f1a8d7df1b05cd33b9166712/README.md) · [LICENSE](https://github.com/stanford-cs336/assignment1-basics/blob/a158843b20107949f1a8d7df1b05cd33b9166712/LICENSE) · [AGENTS.md](https://github.com/stanford-cs336/assignment1-basics/blob/a158843b20107949f1a8d7df1b05cd33b9166712/AGENTS.md) · [pyproject.toml](https://github.com/stanford-cs336/assignment1-basics/blob/a158843b20107949f1a8d7df1b05cd33b9166712/pyproject.toml) |

<a id="ch-data-science-interviews"></a>

### data-science-interviews

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/alexeygrigorev/data-science-interviews |
| License | CC-BY-4.0 |
| Phiên bản đã đọc | `919f44547ef5ffc2bd59674fd301940529f4c1a8` (commit 2026-08-18) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE; chưa chạy upstream |
| Bảo trì | Commit mới nhất 2026-08-18 |
| Nhận định | Câu hỏi và đáp án phỏng vấn data science cổ điển (lý thuyết, kỹ thuật), ít liên quan LLM. Cần ghi công theo CC BY. |
| Nguồn | [README.md](https://github.com/alexeygrigorev/data-science-interviews/blob/919f44547ef5ffc2bd59674fd301940529f4c1a8/README.md) · [LICENSE](https://github.com/alexeygrigorev/data-science-interviews/blob/919f44547ef5ffc2bd59674fd301940529f4c1a8/LICENSE) |

<a id="ch-deep-learning-tuning-playbook"></a>

### Deep Learning Tuning Playbook

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/google-research/tuning_playbook |
| License | CC-BY-4.0 |
| Phiên bản đã đọc | `7554a51f5d3002ba90308d39701b586f5a9b962e` (commit 2024-06-12) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE; chưa chạy upstream |
| Bảo trì | Commit mới nhất 2024-06-12, đứng yên gần 2,5 năm |
| Nhận định | Cẩm nang tune siêu tham số có hệ thống của Google Research/Harvard. Nội dung ổn định nhưng không còn cập nhật; ví dụ mô hình có thể đã cũ. |
| Nguồn | [README.md](https://github.com/google-research/tuning_playbook/blob/7554a51f5d3002ba90308d39701b586f5a9b962e/README.md) · [LICENSE](https://github.com/google-research/tuning_playbook/blob/7554a51f5d3002ba90308d39701b586f5a9b962e/LICENSE) |

<a id="ch-design-resources-for-developers"></a>

### design-resources-for-developers

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/bradtraversy/design-resources-for-developers |
| License | MIT |
| Phiên bản đã đọc | `035bac33121d13f51983c2997ba7369abdce082c` (commit 2026-10-18) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc LICENSE, readme.md, .github/workflows/validate-contribution.yml; chưa chạy upstream |
| Bảo trì | low-activity: Commit cuối 2026-10-18; README nói tạm dừng nhận tài nguyên mới, chỉ nhận báo lỗi bảo trì |
| Nhận định | Danh sách tài nguyên thiết kế (đồ họa UI, font, màu, icon, ảnh stock, mockup, CSS framework...) do Brad Traversy gom, README có mục lục theo nhóm. Đáng tham khảo làm điểm xuất phát; hiện không nhận mục mới nên độ cập nhật sẽ giảm dần. |
| Nguồn | [LICENSE](https://github.com/bradtraversy/design-resources-for-developers/blob/035bac33121d13f51983c2997ba7369abdce082c/LICENSE) · [readme.md](https://github.com/bradtraversy/design-resources-for-developers/blob/035bac33121d13f51983c2997ba7369abdce082c/readme.md) · [validate-contribution.yml](https://github.com/bradtraversy/design-resources-for-developers/blob/035bac33121d13f51983c2997ba7369abdce082c/.github/workflows/validate-contribution.yml) |

<a id="ch-developer-roadmap"></a>

### developer-roadmap

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/nilbuild/developer-roadmap |
| License | Tùy biến, hạn chế (file `license`): chỉ dùng cá nhân, không đăng lại nội dung/hình; khớp "custom" của catalog |
| Phiên bản đã đọc | `57b601f727a265925c30de66456cfddd5c56757b` (commit 2026-11-23) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc license, readme.md, package.json, .github/workflows/sync-content-to-repo.yml; chưa chạy upstream |
| Bảo trì | active: Commit cuối 2026-11-23 |
| Nhận định | Roadmap tương tác roadmap.sh; repo giữ nội dung dạng markdown theo thư mục roadmaps/ cùng script đồng bộ sang cơ sở dữ liệu. Giá trị tham khảo cao về lộ trình, nhưng license cấm tái sử dụng/đăng lại nội dung nên không dùng làm nguồn dữ liệu cho dự án khác. |
| Nguồn | [license](https://github.com/nilbuild/developer-roadmap/blob/57b601f727a265925c30de66456cfddd5c56757b/license) · [readme.md](https://github.com/nilbuild/developer-roadmap/blob/57b601f727a265925c30de66456cfddd5c56757b/readme.md) · [package.json](https://github.com/nilbuild/developer-roadmap/blob/57b601f727a265925c30de66456cfddd5c56757b/package.json) · [sync-content-to-repo.yml](https://github.com/nilbuild/developer-roadmap/blob/57b601f727a265925c30de66456cfddd5c56757b/.github/workflows/sync-content-to-repo.yml) |

<a id="ch-freecodecamp"></a>

### freeCodeCamp

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/freeCodeCamp/freeCodeCamp |
| License | BSD-3-Clause cho phần mềm; `curriculum/` ghi riêng là copyright © freeCodeCamp.org (catalog chỉ ghi BSD-3) |
| Phiên bản đã đọc | `e6f7968747dacccf8f8c85fdcac799a6b1ac46e9` (commit 2026-11-23) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc LICENSE.md, README.md, package.json, .github/workflows/node.js-tests.yml; chưa chạy upstream |
| Bảo trì | active: Commit cuối 2026-11-23; nhiều workflow CI/deploy |
| Nhận định | Codebase nền tảng học lập trình và chương trình học (curriculum/) của freeCodeCamp; monorepo pnpm có api, client, e2e. Mã tái dùng được theo BSD-3, còn nội dung bài học thì không nên coi là cùng license. |
| Nguồn | [LICENSE.md](https://github.com/freeCodeCamp/freeCodeCamp/blob/e6f7968747dacccf8f8c85fdcac799a6b1ac46e9/LICENSE.md) · [README.md](https://github.com/freeCodeCamp/freeCodeCamp/blob/e6f7968747dacccf8f8c85fdcac799a6b1ac46e9/README.md) · [package.json](https://github.com/freeCodeCamp/freeCodeCamp/blob/e6f7968747dacccf8f8c85fdcac799a6b1ac46e9/package.json) · [node.js-tests.yml](https://github.com/freeCodeCamp/freeCodeCamp/blob/e6f7968747dacccf8f8c85fdcac799a6b1ac46e9/.github/workflows/node.js-tests.yml) |

<a id="ch-generative-ai-for-beginners"></a>

### generative-ai-for-beginners

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/microsoft/generative-ai-for-beginners |
| License | MIT |
| Phiên bản đã đọc | `e45c369a8c76bdae831cb5a172d36a6a0fc3a6a2` (commit 2026-11-17) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc LICENSE, README.md; chưa chạy upstream |
| Bảo trì | active: Commit cuối 2026-11-17 |
| Nhận định | Khóa 21 bài của Microsoft Cloud Advocates về xây ứng dụng generative AI (prompt, chat, search, function calling, bảo mật, RAG, agent). README nhắc 50+ bản dịch do Co-op Translator duy trì nên có thể chậm hơn bản gốc (chưa đo). |
| Nguồn | [LICENSE](https://github.com/microsoft/generative-ai-for-beginners/blob/e45c369a8c76bdae831cb5a172d36a6a0fc3a6a2/LICENSE) · [README.md](https://github.com/microsoft/generative-ai-for-beginners/blob/e45c369a8c76bdae831cb5a172d36a6a0fc3a6a2/README.md) |

<a id="ch-github-ranking"></a>

### Github-Ranking

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/EvanLi/Github-Ranking |
| License | MIT (khác catalog cũ: null) |
| Phiên bản đã đọc | `1737eb25adc277c0e1b3aa80cea985f8f4bfe829` (commit 2026-11-23) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc LICENSE, README.md, auto_run.sh; chưa chạy upstream |
| Bảo trì | active: Cập nhật tự động hằng ngày; commit cuối 2026-11-23 (auto update) |
| Nhận định | Bảng xếp hạng repo nhiều sao/fork được sinh tự động bằng script Python và commit hằng ngày. Số liệu là snapshot do bot ghi, không phải đánh giá chất lượng; phụ thuộc máy chủ cron của tác giả. |
| Nguồn | [LICENSE](https://github.com/EvanLi/Github-Ranking/blob/1737eb25adc277c0e1b3aa80cea985f8f4bfe829/LICENSE) · [README.md](https://github.com/EvanLi/Github-Ranking/blob/1737eb25adc277c0e1b3aa80cea985f8f4bfe829/README.md) · [auto_run.sh](https://github.com/EvanLi/Github-Ranking/blob/1737eb25adc277c0e1b3aa80cea985f8f4bfe829/auto_run.sh) |

<a id="ch-hugging-face-course"></a>

### Hugging Face Course

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/huggingface/course |
| License | Apache-2.0 |
| Phiên bản đã đọc | `8b893f0ede6c781045692a7f892f25a0c92b4805` (commit 2026-10-06) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc LICENSE, README.md, .github/workflows/quality.yml, chapters/en/_toctree.yml; chưa chạy upstream |
| Bảo trì | low-activity: Commit cuối 2026-10-06 |
| Nhận định | Khóa NLP/Transformers chính chủ Hugging Face, nội dung nằm trong chapters/<ngôn ngữ>. Bản tiếng Việt có nhưng thiếu các chương mới (10–12); README liệt kê bản dịch nhiều ngôn ngữ ở trạng thái WIP. |
| Nguồn | [LICENSE](https://github.com/huggingface/course/blob/8b893f0ede6c781045692a7f892f25a0c92b4805/LICENSE) · [README.md](https://github.com/huggingface/course/blob/8b893f0ede6c781045692a7f892f25a0c92b4805/README.md) · [quality.yml](https://github.com/huggingface/course/blob/8b893f0ede6c781045692a7f892f25a0c92b4805/.github/workflows/quality.yml) · [_toctree.yml](https://github.com/huggingface/course/blob/8b893f0ede6c781045692a7f892f25a0c92b4805/chapters/en/_toctree.yml) |

<a id="ch-llm-course"></a>

### llm-course

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/mlabonne/llm-course |
| License | Apache-2.0 |
| Phiên bản đã đọc | `7abd96e8284bfae232048fdb77b52397a2114847` (commit 2026-02-05) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc LICENSE, README.md; chưa chạy upstream |
| Bảo trì | low-activity: Commit cuối 2026-02-05; repo chỉ có README, ảnh và LICENSE |
| Nhận định | Lộ trình học LLM của Maxime Labonne (nền tảng, xây LLM, triển khai ứng dụng) dưới dạng README kèm link notebook Colab. Là danh mục link, không có code trong repo; README cũng quảng bá sách Packt của tác giả. Chưa kiểm các notebook bên ngoài. |
| Nguồn | [LICENSE](https://github.com/mlabonne/llm-course/blob/7abd96e8284bfae232048fdb77b52397a2114847/LICENSE) · [README.md](https://github.com/mlabonne/llm-course/blob/7abd96e8284bfae232048fdb77b52397a2114847/README.md) |

<a id="ch-llm-evaluation-guidebook"></a>

### LLM Evaluation Guidebook

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/huggingface/evaluation-guidebook |
| License | CC-BY-NC-SA-4.0 |
| Phiên bản đã đọc | `e09b159dddd03498e44929fc45bd581c94c13c7f` (commit 2025-12-03) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc LICENSE, README.md; chưa chạy upstream |
| Bảo trì | deprecated-by-readme: README: NO LONGER MAINTAINED; bản mới ở HF Space OpenEvals/evaluation-guidebook (commit cuối 2025-12-03) |
| Nhận định | Sổ tay đánh giá LLM (benchmark tự động, LLM-as-judge, người chấm, xử lý sự cố). Repo đã ngừng bảo trì theo README; nếu dùng nên tham chiếu bản HF Space (chưa đọc) và lưu ý license phi thương mại. |
| Nguồn | [LICENSE](https://github.com/huggingface/evaluation-guidebook/blob/e09b159dddd03498e44929fc45bd581c94c13c7f/LICENSE) · [README.md](https://github.com/huggingface/evaluation-guidebook/blob/e09b159dddd03498e44929fc45bd581c94c13c7f/README.md) |

<a id="ch-llm-interview-questions-and-answers-hub"></a>

### LLM Interview Questions and Answers Hub

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/KalyanKS-NLP/LLM-Interview-Questions-and-Answers-Hub |
| License | Apache-2.0 |
| Phiên bản đã đọc | `280c8b642acd65006b11aad76633826a867f3a63` (commit 2026-02-09) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc LICENSE, README.md; chưa chạy upstream |
| Bảo trì | low-activity: Commit cuối 2026-02-09 (đổi mức giảm giá sách) |
| Nhận định | Bộ câu hỏi phỏng vấn LLM kèm đáp án viết sẵn, chia thành các file QA_x-y.md. Hữu ích để ôn nhanh; chất lượng đáp án chưa thẩm định (chưa xác minh), và README mang tính phễu cho sách/newsletter của tác giả. |
| Nguồn | [LICENSE](https://github.com/KalyanKS-NLP/LLM-Interview-Questions-and-Answers-Hub/blob/280c8b642acd65006b11aad76633826a867f3a63/LICENSE) · [README.md](https://github.com/KalyanKS-NLP/LLM-Interview-Questions-and-Answers-Hub/blob/280c8b642acd65006b11aad76633826a867f3a63/README.md) |

<a id="ch-llms-from-scratch"></a>

### LLMs-from-scratch

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/rasbt/LLMs-from-scratch |
| License | Apache-2.0 |
| Phiên bản đã đọc | `5790c0c50bcb7d95bf9ee39f438c09ea31826b7d` (commit 2026-11-22) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc LICENSE.txt, README.md, pyproject.toml, .github/workflows/basic-tests-linux-uv.yml; chưa chạy upstream |
| Bảo trì | active: Commit cuối 2026-11-22 |
| Nhận định | Code từng chương để dựng, tiền huấn luyện và tinh chỉnh GPT nhỏ bằng PyTorch theo sách; pyproject yêu cầu Python >=3.10,<3.15. Giá trị giáo dục cao; chưa chạy notebook nào. Mô hình nhỏ cho mục đích học, không phải hệ thống production. |
| Nguồn | [LICENSE.txt](https://github.com/rasbt/LLMs-from-scratch/blob/5790c0c50bcb7d95bf9ee39f438c09ea31826b7d/LICENSE.txt) · [README.md](https://github.com/rasbt/LLMs-from-scratch/blob/5790c0c50bcb7d95bf9ee39f438c09ea31826b7d/README.md) · [pyproject.toml](https://github.com/rasbt/LLMs-from-scratch/blob/5790c0c50bcb7d95bf9ee39f438c09ea31826b7d/pyproject.toml) · [basic-tests-linux-uv.yml](https://github.com/rasbt/LLMs-from-scratch/blob/5790c0c50bcb7d95bf9ee39f438c09ea31826b7d/.github/workflows/basic-tests-linux-uv.yml) |

<a id="ch-machine-learning-engineering-open-book"></a>

### Machine Learning Engineering Open Book

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/stas00/ml-engineering |
| License | CC-BY-SA-4.0 |
| Phiên bản đã đọc | `1a78efc30ab987bfd8a016df00acfcdd653a268c` (commit 2026-11-21) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc LICENSE-CC-BY-SA, README.md, SKILL.md, skills/ml-engineering/SKILL.md; chưa chạy upstream |
| Bảo trì | active: Commit cuối 2026-11-21 |
| Nhận định | Sách mở ghi lại kinh nghiệm huấn luyện/suy luận LLM và VLM quy mô lớn (SLURM, mạng, lưu trữ, gỡ lỗi, benchmark). Có kèm skill cho agent; chưa kiểm các script benchmark. Copyleft ShareAlike khi tái phân phối nội dung. |
| Nguồn | [LICENSE-CC-BY-SA](https://github.com/stas00/ml-engineering/blob/1a78efc30ab987bfd8a016df00acfcdd653a268c/LICENSE-CC-BY-SA) · [README.md](https://github.com/stas00/ml-engineering/blob/1a78efc30ab987bfd8a016df00acfcdd653a268c/README.md) · [SKILL.md](https://github.com/stas00/ml-engineering/blob/1a78efc30ab987bfd8a016df00acfcdd653a268c/SKILL.md) · [SKILL.md](https://github.com/stas00/ml-engineering/blob/1a78efc30ab987bfd8a016df00acfcdd653a268c/skills/ml-engineering/SKILL.md) |

<a id="ch-make-com-automation-recipes"></a>

### make.com-automation-recipes

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/cporter202/make-com-automation-recipes |
| License | MIT (khác catalog cũ: null) |
| Phiên bản đã đọc | `a8544d3ce5f2fd0ce7a2ff58bc884a7b20af55d9` (commit 2026-10-17) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc LICENSE, README.md; chưa chạy upstream |
| Bảo trì | low-activity: Commit cuối 2026-10-17 |
| Nhận định | Thư viện 600+ link tới template Make.com, mọi link gắn mã affiliate (README có tuyên bố affiliate). Không phải mã/workflow tự chứa; giá trị tham khảo thấp, nên coi là phễu quảng bá. |
| Nguồn | [LICENSE](https://github.com/cporter202/make-com-automation-recipes/blob/a8544d3ce5f2fd0ce7a2ff58bc884a7b20af55d9/LICENSE) · [README.md](https://github.com/cporter202/make-com-automation-recipes/blob/a8544d3ce5f2fd0ce7a2ff58bc884a7b20af55d9/README.md) |

<a id="ch-marketing-apis-that-drive-roi"></a>

### marketing-apis-that-drive-roi

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/cporter202/marketing-apis-that-drive-roi |
| License | Không có file LICENSE (khớp catalog: không license) |
| Phiên bản đã đọc | `e35d6b971973b899d1b0c9b25dbc5b4773f3ebf3` (commit 2026-10-20) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, META.json; chưa chạy upstream |
| Bảo trì | low-activity: Commit cuối 2026-10-20 |
| Nhận định | Danh mục 290 "API" thực chất là actor Apify chia theo nhóm, không có mã nguồn đáng kể. Cùng mẫu phễu affiliate với các repo cporter202 khác; không có license nên không có quyền tái sử dụng rõ ràng. |
| Nguồn | [README.md](https://github.com/cporter202/marketing-apis-that-drive-roi/blob/e35d6b971973b899d1b0c9b25dbc5b4773f3ebf3/README.md) · [META.json](https://github.com/cporter202/marketing-apis-that-drive-roi/blob/e35d6b971973b899d1b0c9b25dbc5b4773f3ebf3/META.json) |

<a id="ch-mcp-for-beginners"></a>

### MCP for Beginners

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/microsoft/mcp-for-beginners |
| License | MIT |
| Phiên bản đã đọc | `c7efcc2ac5839100dd2cd961e8cc44dfefc1e7bf` (commit 2026-11-21) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc LICENSE, README.md, 03-GettingStarted/01-first-server/solution/typescript/package.json; chưa chạy upstream |
| Bảo trì | active: Commit cuối 2026-11-21 |
| Nhận định | Giáo trình MCP của Microsoft từ khái niệm, bảo mật tới server/client mẫu và case study. Mẫu code không có CI nên chưa có bảo đảm chạy được; bản dịch (kể cả tiếng Việt) có thể chậm hơn gốc (chưa đo). |
| Nguồn | [LICENSE](https://github.com/microsoft/mcp-for-beginners/blob/c7efcc2ac5839100dd2cd961e8cc44dfefc1e7bf/LICENSE) · [README.md](https://github.com/microsoft/mcp-for-beginners/blob/c7efcc2ac5839100dd2cd961e8cc44dfefc1e7bf/README.md) · [package.json](https://github.com/microsoft/mcp-for-beginners/blob/c7efcc2ac5839100dd2cd961e8cc44dfefc1e7bf/03-GettingStarted/01-first-server/solution/typescript/package.json) |

<a id="ch-nanochat"></a>

### nanochat

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/karpathy/nanochat |
| License | MIT |
| Phiên bản đã đọc | `92d63d4e8bb4df75c3b71618f31ddde2378b2bcd` (commit 2026-07-03) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc LICENSE, README.md, pyproject.toml; chưa chạy upstream |
| Bảo trì | low-activity: Commit cuối 2026-07-03 |
| Nhận định | Chuỗi huấn luyện ChatGPT tối giản (tokenizer, pretrain, finetune, eval, chat) với mã gọn trong thư mục nanochat/. Phù hợp để học và thử nghiệm; leaderboard là số liệu tự công bố (chưa xác minh), chưa chạy. |
| Nguồn | [LICENSE](https://github.com/karpathy/nanochat/blob/92d63d4e8bb4df75c3b71618f31ddde2378b2bcd/LICENSE) · [README.md](https://github.com/karpathy/nanochat/blob/92d63d4e8bb4df75c3b71618f31ddde2378b2bcd/README.md) · [pyproject.toml](https://github.com/karpathy/nanochat/blob/92d63d4e8bb4df75c3b71618f31ddde2378b2bcd/pyproject.toml) |

<a id="ch-rag-techniques"></a>

### RAG_Techniques

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/NirDiamant/RAG_Techniques |
| License | Tùy biến, phi thương mại, bắt buộc ghi công (khớp catalog "Non-commercial (custom)") |
| Phiên bản đã đọc | `2fd7bd0ffe5b8520cfd1a6ee75fcb86fc41bf8c6` (commit 2026-11-02) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc LICENSE, README.md, .github/workflows/notebook-smoke.yml; chưa chạy upstream |
| Bảo trì | active: Commit cuối 2026-11-02 |
| Nhận định | Bộ notebook kỹ thuật RAG (simple, rerank, graph RAG, self-RAG, RAPTOR...). Cấm dùng thương mại nên không chép vào sản phẩm; CI chỉ parse notebook, không chứng minh kết quả chạy đúng. |
| Nguồn | [LICENSE](https://github.com/NirDiamant/RAG_Techniques/blob/2fd7bd0ffe5b8520cfd1a6ee75fcb86fc41bf8c6/LICENSE) · [README.md](https://github.com/NirDiamant/RAG_Techniques/blob/2fd7bd0ffe5b8520cfd1a6ee75fcb86fc41bf8c6/README.md) · [notebook-smoke.yml](https://github.com/NirDiamant/RAG_Techniques/blob/2fd7bd0ffe5b8520cfd1a6ee75fcb86fc41bf8c6/.github/workflows/notebook-smoke.yml) |

<a id="ch-social-growth-apis-for-creators"></a>

### social-growth-apis-for-creators

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/cporter202/social-growth-apis-for-creators |
| License | Không có file LICENSE (khớp catalog: không license) |
| Phiên bản đã đọc | `828f6bc12a138119ba52c8f4209d64601682ac01` (commit 2026-10-20) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, META.json; chưa chạy upstream |
| Bảo trì | low-activity: Commit cuối 2026-10-20 |
| Nhận định | Danh mục actor Apify cho mạng xã hội (Facebook/Meta, Instagram/TikTok, YouTube, X/LinkedIn...) do cporter202 gom, không có mã đáng kể. Không license và mục đích affiliate nên giá trị tham khảo thấp. |
| Nguồn | [README.md](https://github.com/cporter202/social-growth-apis-for-creators/blob/828f6bc12a138119ba52c8f4209d64601682ac01/README.md) · [META.json](https://github.com/cporter202/social-growth-apis-for-creators/blob/828f6bc12a138119ba52c8f4209d64601682ac01/META.json) |

<a id="ch-system-design-primer"></a>

### system-design-primer

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/donnemartin/system-design-primer |
| License | CC-BY-4.0 |
| Phiên bản đã đọc | `ae9bbd7b02d90b9866215de185217d33f39ab733` (commit 2026-03-19) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc LICENSE.txt, README.md; chưa chạy upstream |
| Bảo trì | low-activity: Commit cuối 2026-03-19 |
| Quy mô (25/11/2026) | 379.184 ★, 59.358 fork, 646 issue mở (GitHub search API); thẻ repo theo ảnh người dùng gửi (chưa xác minh độc lập): 128 contributor, 21 "Used by". Clone nông lại cùng ngày: HEAD vẫn `ae9bbd7`, LICENSE.txt vẫn CC BY 4.0 (GitHub báo `NOASSERTION`) |
| Nhận định | Tài liệu học thiết kế hệ thống kèm đề mẫu và lời giải trong solutions/, bản dịch ngôn ngữ khác trong repo. Nền tảng tốt nhưng nội dung cập nhật chậm; chưa đối chiếu với thực tế công nghệ hiện tại. |
| Nguồn | [LICENSE.txt](https://github.com/donnemartin/system-design-primer/blob/ae9bbd7b02d90b9866215de185217d33f39ab733/LICENSE.txt) · [README.md](https://github.com/donnemartin/system-design-primer/blob/ae9bbd7b02d90b9866215de185217d33f39ab733/README.md) |

<a id="nt-2026-11-23"></a>

## Nâng trần theo khoảng trống — 23/11/2026

Phần này có các hồ sơ mới của đợt nâng trần: mười trinh sát tìm trên internet và GitHub những mảng mà chuyên mục còn thiếu hoặc chỉ có hồ sơ cũ, rồi mỗi repo được clone nông tại một commit cố định, đọc LICENSE, README, ít nhất một file triển khai thật và CI nếu có; không cài hay chạy mã upstream. Mô tả của trinh sát nhiều chỗ sai so với mã thật, và các chỗ đó được sửa ngay trong từng hồ sơ. Số sao lấy sau bằng GitHub search API nên có thể để trống.

<a id="nt-awesome-lint"></a>

### awesome-lint

| Thuộc tính | Giá trị |
|---|---|
| Repo | https://github.com/sindresorhus/awesome-lint |
| License | MIT |
| Phiên bản đã đọc | `4f870abda373cfa18c67822c39ee29c451ae8a70` (commit 2026-07-06) |
| Kiểm chứng | 2026-11-23; code-read; đã đọc readme.md, license, package.json, cli.js, rules/git-repo-age.js, rules/github.js, lib/github-api.js, workflow main.yml; chưa chạy upstream |
| Khoảng trống lấp | Cổng kiểm bằng máy cho awesome-list được duy trì thật sự (lint cấu trúc Markdown và siêu dữ liệu repo) |
| Cơ chế đáng học | <br>- Bộ quy tắc remark-lint riêng cho awesome-list trong `rules/` (badge, list-item, heading, toc, double-link, license, contributing...), cộng quy tắc Markdown chung trong `config.js`.<br>- Quy tắc kiểm repo qua GitHub API: `git-repo-age.js` đòi repo tối thiểu 30 ngày tuổi; `github.js` đòi có mô tả, topic `awesome` và `awesome-list`, license được GitHub nhận diện.<br>- Chú thích điều khiển `disable`, `enable`, `ignore` trong chính README để miễn trừ có chủ đích.<br>- CLI nhận URL hoặc đường dẫn; với URL thì `git clone --depth 1` rồi lint (`index.js`). |
| Tiêu chí và cách kiểm | Mã thoát lỗi khi có vi phạm do CLI báo; test bằng `node --test` kèm snapshot cho từng rule trong `test/rules`, và `xo` lint, chạy trên Node 20 và 24 qua `main.yml` (đã mở). Quy tắc dùng API đọc `github_token` nếu có; lỗi API thì rule bỏ qua im lặng (`github-api.js` trả undefined), nên cổng này có thể pass khi không lấy được dữ liệu repo. |
| Giới hạn và rủi ro | License MIT (file `license`). Mô tả của trinh sát có phần sai: repo không kiểm link chết (không có phụ thuộc hay rule kiểm URL còn sống trong `package.json`, `config.js`), chỉ kiểm cú pháp và siêu dữ liệu repo; kiểm link nên ghép với lychee. Gọi GitHub API không xác thực nếu thiếu token nên dễ chạm giới hạn tốc độ. Chuẩn "awesome" là quy ước của danh sách awesome.re, không phải chuẩn bắt buộc của mọi danh sách. |
| So với | lychee (`lychee`, kiểm link chết); markdownlint (`markdownlint`, lint Markdown chung, không có rule awesome); mức quản trị danh sách so với awesome-claude-code (`awesome-claude-code`, một danh sách cần kiểm) |
| Nguồn | [license](https://github.com/sindresorhus/awesome-lint/blob/4f870abda373cfa18c67822c39ee29c451ae8a70/license) · [readme.md](https://github.com/sindresorhus/awesome-lint/blob/4f870abda373cfa18c67822c39ee29c451ae8a70/readme.md) · [package.json](https://github.com/sindresorhus/awesome-lint/blob/4f870abda373cfa18c67822c39ee29c451ae8a70/package.json) · [cli.js](https://github.com/sindresorhus/awesome-lint/blob/4f870abda373cfa18c67822c39ee29c451ae8a70/cli.js) · [git-repo-age.js](https://github.com/sindresorhus/awesome-lint/blob/4f870abda373cfa18c67822c39ee29c451ae8a70/rules/git-repo-age.js) · [github.js](https://github.com/sindresorhus/awesome-lint/blob/4f870abda373cfa18c67822c39ee29c451ae8a70/rules/github.js) · [github-api.js](https://github.com/sindresorhus/awesome-lint/blob/4f870abda373cfa18c67822c39ee29c451ae8a70/lib/github-api.js) · [main.yml](https://github.com/sindresorhus/awesome-lint/blob/4f870abda373cfa18c67822c39ee29c451ae8a70/.github/workflows/main.yml) |

<a id="nt-juice-shop"></a>

### OWASP Juice Shop

| Thuộc tính | Giá trị |
|---|---|
| Repo | https://github.com/juice-shop/juice-shop |
| License | MIT |
| Phiên bản đã đọc | `c9f99228d9d56afb5f5ca7925376292f7fa44b13` (commit 2026-11-19) |
| Kiểm chứng | 2026-11-23; code-read; đã đọc README, LICENSE, AGENTS.md, challenges.yml, routes/login.ts, config/default.yml, rsn/rsn.ts, workflow ci.yml; chưa chạy upstream |
| Khoảng trống lấp | Học bảo mật: ứng dụng web cố ý có lỗ hổng bao phủ OWASP Top 10 dùng cho đào tạo, CTF và thử công cụ quét |
| Cơ chế đáng học | <br>- Sổ thử thách khai báo dạng dữ liệu trong `data/static/challenges.yml` (118 mục, mỗi mục có category, độ khó, gợi ý, `mitigationUrl`, khóa); mã lỗi gắn nhãn `vuln-code-snippet` ngay trong route (ví dụ nối chuỗi vào câu SQL ở `routes/login.ts`).<br>- Chế độ an toàn `safetyMode` (enabled, disabled, auto) và `disabledEnv` theo từng thử thách để tắt mục nguy hiểm khi chạy Docker hay Heroku (`config/default.yml`).<br>- Công cụ `rsn` so snapshot mã thử thách với `cache.json` để CI báo khi mã vô tình lệch khỏi bài tập (`rsn/rsn.ts`).<br>- `AGENTS.md` nêu thứ tự ưu tiên chỉ dẫn cho agent và cảnh báo không sửa lỗi cố ý. |
| Tiêu chí và cách kiểm | CI `ci.yml` (đã mở) chạy lint, `npm run rsn`, test đơn vị giao diện và máy chủ, test tích hợp API; thư mục `test/` có api, server, cypress, smoke. Kiểm bằng máy; chưa chạy trong hồ sơ này. |
| Giới hạn và rủi ro | License MIT (README ghi rõ). Ứng dụng cố ý dễ bị tấn công: chỉ chạy cô lập, không phơi ra Internet; một số thử thách (XSS API, SSRF, đọc tệp) cần tắt trong Docker. Một số thử thách cần nhà cung cấp AI/LLM bên ngoài (README). Có số liệu Prometheus (`routes/metrics.ts`) nhưng chưa thấy telemetry gửi ra ngoài trong mã đã đọc. Hồ sơ chỉ đọc mã, tuyệt đối không chạy upstream. Các "lỗi" trong repo là cố ý nên không được lấy làm mẫu mã. |
| So với | OWASP Web Security Testing Guide (`owasp-web-security-testing-guide`, phương pháp luận, không có app thực hành); WebGoat (cùng lô, bài học tương tác Java); AI Red Teaming Guide (`ai-red-teaming-guide`, tài liệu) |
| Nguồn | [LICENSE](https://github.com/juice-shop/juice-shop/blob/c9f99228d9d56afb5f5ca7925376292f7fa44b13/LICENSE) · [README.md](https://github.com/juice-shop/juice-shop/blob/c9f99228d9d56afb5f5ca7925376292f7fa44b13/README.md) · [AGENTS.md](https://github.com/juice-shop/juice-shop/blob/c9f99228d9d56afb5f5ca7925376292f7fa44b13/AGENTS.md) · [challenges.yml](https://github.com/juice-shop/juice-shop/blob/c9f99228d9d56afb5f5ca7925376292f7fa44b13/data/static/challenges.yml) · [login.ts](https://github.com/juice-shop/juice-shop/blob/c9f99228d9d56afb5f5ca7925376292f7fa44b13/routes/login.ts) · [default.yml](https://github.com/juice-shop/juice-shop/blob/c9f99228d9d56afb5f5ca7925376292f7fa44b13/config/default.yml) · [rsn.ts](https://github.com/juice-shop/juice-shop/blob/c9f99228d9d56afb5f5ca7925376292f7fa44b13/rsn/rsn.ts) · [ci.yml](https://github.com/juice-shop/juice-shop/blob/c9f99228d9d56afb5f5ca7925376292f7fa44b13/.github/workflows/ci.yml) |

<a id="nt-webgoat"></a>

### OWASP WebGoat

| Thuộc tính | Giá trị |
|---|---|
| Repo | https://github.com/WebGoat/WebGoat |
| License | GPL-2.0-or-later |
| Phiên bản đã đọc | `4e98f1cbbf896fdd06edcc9930515ebe0ade7c69` (commit 2026-11-09) |
| Kiểm chứng | 2026-11-23; code-read; đã đọc README, LICENSE.txt, AGENTS.md, WEBGOAT_IN_THE_AGE_OF_AI.md, SqlInjectionLesson5a.java, workflow build.yml, workflow lesson-vulnerability-triage.yml; chưa chạy upstream |
| Khoảng trống lấp | Học bảo mật: bài học tương tác Java/Spring Boot về lỗ hổng ứng dụng, kèm WebWolf làm máy chủ của kẻ tấn công |
| Cơ chế đáng học | <br>- Kiến trúc bài học: mỗi bài kế thừa `Lesson`, mỗi bài tập là `AssignmentEndpoint` trả `AttackResult` (success hoặc failed kèm phản hồi); `CourseConfiguration` gắn bài tập theo package (theo AGENTS.md).<br>- Bài tập mẫu `SqlInjectionLesson5a.java` nối chuỗi vào câu SQL và coi đạt khi truy vấn trả từ 6 dòng, đồng thời giải thích cho người học.<br>- WebWolf là ứng dụng thứ hai (cổng 9090) đóng vai máy chủ bắt request của kẻ tấn công.<br>- `AGENTS.md` chặn agent tự vá lỗ hổng bài học; `lesson-vulnerability-triage.yml` tự gắn nhãn issue hoặc PR báo "lỗ hổng" của bài học cố ý. |
| Tiêu chí và cách kiểm | CI `build.yml` (đã mở) chạy pre-commit và `mvn verify`; kiểm kiểu và quy tắc qua Spotless, Checkstyle, PMD (theo AGENTS.md, chưa xác minh trong pom); có test đơn vị theo từng bài trong `src/test`. Kiểm bằng máy, chưa chạy trong hồ sơ này. |
| Giới hạn và rủi ro | License GPL-2.0-or-later (đọc từ header `LICENSE.txt` và SPDX trong mã; chưa đối chiếu từng thư mục con, tài sản nhúng và phụ thuộc). Ứng dụng cố ý dễ bị tấn công; README cảnh báo máy chạy sẽ cực kỳ dễ bị tấn công, mặc định gắn localhost. Có keystore mẫu `goatkeystore.pkcs12` trong repo (khóa cho bài học, không dùng thật). Yêu cầu Java 25 và Spring Boot 4.1 theo AGENTS.md. Mô tả "Java" của trinh sát đúng. Mã lỗi cố ý, không dùng làm mẫu. |
| So với | OWASP Juice Shop (cùng lô, thử thách kiểu CTF, Node/Angular); OWASP WSTG (`owasp-web-security-testing-guide`, phương pháp kiểm thử); cybersecurity-threats-guide (`cybersecurity-threats-guide`, tài liệu tổng quan) |
| Nguồn | [LICENSE.txt](https://github.com/WebGoat/WebGoat/blob/4e98f1cbbf896fdd06edcc9930515ebe0ade7c69/LICENSE.txt) · [README.md](https://github.com/WebGoat/WebGoat/blob/4e98f1cbbf896fdd06edcc9930515ebe0ade7c69/README.md) · [AGENTS.md](https://github.com/WebGoat/WebGoat/blob/4e98f1cbbf896fdd06edcc9930515ebe0ade7c69/AGENTS.md) · [WEBGOAT_IN_THE_AGE_OF_AI.md](https://github.com/WebGoat/WebGoat/blob/4e98f1cbbf896fdd06edcc9930515ebe0ade7c69/WEBGOAT_IN_THE_AGE_OF_AI.md) · [SqlInjectionLesson5a.java](https://github.com/WebGoat/WebGoat/blob/4e98f1cbbf896fdd06edcc9930515ebe0ade7c69/src/main/java/org/owasp/webgoat/lessons/sqlinjection/introduction/SqlInjectionLesson5a.java) · [build.yml](https://github.com/WebGoat/WebGoat/blob/4e98f1cbbf896fdd06edcc9930515ebe0ade7c69/.github/workflows/build.yml) · [lesson-vulnerability-triage.yml](https://github.com/WebGoat/WebGoat/blob/4e98f1cbbf896fdd06edcc9930515ebe0ade7c69/.github/workflows/lesson-vulnerability-triage.yml) |
