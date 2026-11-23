<!-- File sinh tự động bởi scripts/build_catalog_views.py; sửa data/projects.json hoặc data/taxonomy.json rồi chạy lại. -->

# eval-observability — Đánh giá, an toàn & chất lượng

[← Mục lục catalog](../README.md) · 73 hồ sơ.

## Eval LLM/agent (`llm-eval`, 26)

| Dự án | Repo | License | ★ | Bằng chứng | Mục | Tóm tắt |
|---|---|---|---|---|---|---|
| [iFixAi](../../07-eval-observability/README.md#ch-ifixai) | `ifixai-ai/iFixAi` | Apache-2.0 | 46.948 | đọc tài liệu 2026-11-23 | 07 | Chẩn đoán agent 'lệch mục tiêu' (misalignment) qua nhiều nhóm kiểm, nhiều provider; |
| [netron](../../07-eval-observability/README.md#chuyen-netron) | `lutzroeder/netron` | MIT | 33.703 | đọc tài liệu 2026-11-18 | 07 | Trình xem mô hình mạng nơ-ron, học sâu và học máy; |
| [Promptfoo](../../07-eval-observability/README.md#core-eval-validity) | `promptfoo/promptfoo` | MIT | 26.736 | đọc mã 2026-11-02 | 07 | red-team; |
| [shap](../../07-eval-observability/README.md#chuyen-shap) | `shap/shap` | MIT License | 25.867 | đọc tài liệu 2026-11-18 | 07 | Thư viện giải thích đầu ra của mô hình học máy bằng giá trị Shapley (SHAP), kèm nhiều biểu đồ trực quan hoá. |
| [DeepEval](../../07-eval-observability/README.md#ch-deepeval) | `confident-ai/deepeval` | Apache-2.0 | 19.605 | đọc tài liệu 2026-11-23 | 07 | . |
| [Ragas](../../07-eval-observability/README.md#ch-ragas) | `vibrantlabsai/ragas` | Apache-2.0 | 16.406 | đọc tài liệu 2026-11-23 | 07 | ; |
| [lm-evaluation-harness](../../07-eval-observability/README.md#ch-lm-evaluation-harness) | `EleutherAI/lm-evaluation-harness` | MIT | 14.524 | đọc tài liệu 2026-11-23 | 07 | Backend HF Open LLM Leaderboard; |
| [OpenPipe ART](../../07-eval-observability/README.md#ch-openpipe-art) | `OpenPipe/ART` | Apache-2.0 | 10.868 | đọc tài liệu 2026-11-23 | 07 | RL (GRPO) huấn luyện agent; |
| [FailproofAI](../../07-eval-observability/README.md#ch-failproofai) | `FailproofAI/failproofai` | MIT + Commons Clause (không phải OSI) | 10.120 | đọc tài liệu 2026-11-23 | 07 | Hook 12 harness (Claude Code, Codex, Copilot CLI, OpenClaw…), 40 policy chặn tool call + trace phiên; |
| [Evidently](../../07-eval-observability/README.md#ch-evidently) | `evidentlyai/evidently` | Apache-2.0 | 8.078 | đọc mã 2026-11-23 | 07 | Metric/test/dashboard cho ML và LLM (100+ metric theo README); |
| [OpenCompass](../../07-eval-observability/README.md#ch-opencompass) | `open-compass/opencompass` | Apache-2.0 | 7.631 | đọc tài liệu 2026-11-23 | 07 | Shanghai AI Lab; |
| [Giskard (v3)](../../07-eval-observability/README.md#ch-giskard-v3) | `Giskard-AI/giskard-oss` | Apache-2.0 | 5.972 | đọc tài liệu 2026-11-23 | 07 | Thư viện test + quét lỗ hổng agent nhiều lượt, v3 viết lại thành 5 gói, v2 ngừng bảo trì; |
| [Inspect AI](../../07-eval-observability/README.md#core-eval-validity) | `UKGovernmentBEIS/inspect_ai` | MIT | 3.153 | đọc mã 2026-11-02 | 07 | UK AISI; |
| [Lighteval](../../07-eval-observability/README.md#ch-lighteval) | `huggingface/lighteval` | MIT | 2.589 | đọc tài liệu 2026-11-23 | 07 | Hugging Face; |
| [Evals Skills (Parlance Labs)](../../07-eval-observability/README.md#nt-evals-skills) | `ai-evals-course/evals-skills` | Apache-2.0 | 1.838 | đọc mã 2026-11-23 | 07 | Chín skill hướng dẫn agent dựng eval theo sản phẩm LLM (phân tích lỗi trên trace, dữ liệu tổng hợp, judge prompt, hiệu chuẩn judge, đánh giá RAG). |
| [Autoevals](../../07-eval-observability/README.md#nt-autoevals) | `braintrustdata/autoevals` | MIT | 1.087 | đọc mã 2026-11-23 | 07 | Thư viện scorer LLM-as-judge dựa trên template YAML với bảng điểm cố định, kèm scorer heuristic và biến trajectory. |
| [JiWER](../../14-voice-multimodal/README.md#ch-jiwer) | `jitsi/jiwer` | Apache-2.0 | 942 | đọc tài liệu 2026-11-23 | 14 | Tính WER/MER/WIL/WIP/CER cho STT bằng RapidFuzz, v4.0.0; |
| [agentevals](../../03-agentic-patterns-loops/README.md#factory-trajectory-oracles-2026-11-04) | `langchain-ai/agentevals` | MIT | 757 | đọc mã 2026-11-04 | 03 | Chấm trajectory: match strict/unordered/subset/superset + tool_args exact/ignore, LLM-judge, graph LangGraph; |
| [Inspect Evals](../../07-eval-observability/README.md#ch-inspect-evals) | `UKGovernmentBEIS/inspect_evals` | MIT | 756 | đọc tài liệu 2026-11-23 | 07 | >200 task Inspect; |
| [AgentLab](../../11-browser-computer-use-sandbox/README.md#agentlab) | `ServiceNow/AgentLab` | Apache-2.0 (notice) | 661 | đọc mã 2026-11-02 | 11 | Thí nghiệm BrowserGym; |
| [chunking_evaluation (Chroma)](../../10-local-llm-rag-memory/README.md#ch-chunking-evaluation-chroma) | `brandonstarxel/chunking_evaluation` | MIT | 514 | đọc tài liệu 2026-11-23 | 10 | Đo chunking mức token: precision/recall/IoU so với đoạn trích chuẩn (báo cáo kỹ thuật Chroma), sinh câu hỏi tổng hợp; |
| [UTMOSv2](../../14-voice-multimodal/README.md#ch-utmosv2) | `sarulab-speech/UTMOSv2` | MIT | 381 | đọc tài liệu 2026-11-23 | 14 | Dự đoán MOS độ tự nhiên giọng tổng hợp; |
| [UltraEval-Audio](../../14-voice-multimodal/README.md#ch-ultraeval-audio) | `OpenBMB/UltraEval-Audio` | Apache-2.0 | 333 | đọc tài liệu 2026-11-23 | 14 | Khung eval audio foundation model: 34 benchmark, 10 ngôn ngữ, hiểu + sinh giọng, lệnh tái lập kết quả (ACL 2026 demo); |
| [EVA (ServiceNow)](../../14-voice-multimodal/README.md#ch-eva-servicenow) | `ServiceNow/eva` | MIT | 235 | đọc tài liệu 2026-11-23 | 14 | Eval voice agent nhiều lượt bot-to-bot: EVA-A (đúng việc) + EVA-X (trải nghiệm); |
| [OpenEvals](../../07-eval-observability/README.md#openevals-factory) | `langchain-ai/openevals` | MIT | — | đọc mã 2026-11-04 | 07 | Scorer exact/JSON và LLM judge Python/JS; |
| [Ragas (số liệu RAG tách retrieval và answer)](../../07-eval-observability/README.md#nt-ragas-rag-metrics) | `explodinggradients/ragas` | Apache-2.0 | — | đọc mã 2026-11-23 | 07 | Bộ metric chấm ứng dụng RAG/LLM, tách rõ phía truy xuất (context precision, context recall) và phía trả lời (faithfulness, answer relevancy). |

## Tracing & observability LLM (`tracing`, 13)

| Dự án | Repo | License | ★ | Bằng chứng | Mục | Tóm tắt |
|---|---|---|---|---|---|---|
| [Langfuse](../../07-eval-observability/README.md#ch-langfuse) | `langfuse/langfuse` | MIT (Expat) cho phần lõi; thư mục ee/ và các đường dẫn ee kh | 37.753 | đọc tài liệu 2026-11-23 | 07 | . |
| [MLflow](../../07-eval-observability/README.md#ch-mlflow) | `mlflow/mlflow` | Apache-2.0 | 28.940 | đọc tài liệu 2026-11-23 | 07 | Linux Foundation; |
| [Opik](../../07-eval-observability/README.md#ch-opik) | `comet-ml/opik` | Apache-2.0 | 23.489 | đọc tài liệu 2026-11-23 | 07 | Trace + LLM-judge; |
| [Arize Phoenix](../../07-eval-observability/README.md#ch-arize-phoenix) | `Arize-ai/phoenix` | Elastic-2.0 (ELv2) | 12.383 | đọc tài liệu 2026-11-23 | 07 | source-available. |
| [OpenLLMetry](../../07-eval-observability/README.md#ch-openllmetry) | `traceloop/openllmetry` | Apache-2.0 | 7.550 | đọc tài liệu 2026-11-23 | 07 | Instrument GenAI chuẩn OTel; |
| [Coze Loop](../../07-eval-observability/README.md#ch-coze-loop) | `coze-dev/coze-loop` | Apache-2.0 | 5.800 | đọc tài liệu 2026-11-23 | 07 | Bản mở Coze Loop (ByteDance): playground prompt, bộ eval, trace; |
| [LangWatch](../../07-eval-observability/README.md#ch-langwatch) | `langwatch/langwatch` | Apache-2.0; thư mục enterprise/ theo LangWatch Enterprise Li | 5.052 | đọc tài liệu 2026-11-23 | 07 | Trace, simulation test agent, AI gateway virtual key, theo dõi coding agent; |
| [Pydantic Logfire (SDK)](../../07-eval-observability/README.md#ch-pydantic-logfire-sdk) | `pydantic/logfire` | MIT (SDK; server đóng mã) | 4.566 | đọc mã 2026-11-23 | 07 | SDK Python bọc OpenTelemetry, che secret mặc định (scrubbing.py: password, secret, auth, api key, session, cookie); |
| [Laminar](../../07-eval-observability/README.md#ch-laminar) | `lmnr-ai/lmnr` | Apache-2.0 | 3.520 | đọc tài liệu 2026-11-23 | 07 | Trace/eval/replay agent; |
| [OpenLIT](../../07-eval-observability/README.md#ch-openlit) | `openlit/openlit` | Apache-2.0 | 3.099 | đọc mã 2026-11-23 | 07 | Nền tảng OTel-native gen_ai.\*: trace, eval, guardrail, GPU; |
| [OpenInference](../../07-eval-observability/README.md#ch-openinference) | `Arize-ai/openinference` | Apache-2.0 | 1.333 | đọc mã 2026-11-23 | 07 | Đặc tả + instrument (~38 gói Python) cho Phoenix; |
| [Overmind](../../07-eval-observability/README.md#ch-overmind) | `overmind-core/overmind` | AGPL-3.0 (platform) / MIT (SDK, thư mục overmind/) | 780 | đọc tài liệu 2026-11-23 | 07 | Trace → dataset → eval → fine-tune LoRA (Modal); |
| [OpenTelemetry GenAI Semantic Conventions](../../07-eval-observability/README.md#ch-opentelemetry-genai-semantic-conventions) | `open-telemetry/semantic-conventions-genai` | Apache-2.0 | 560 | đọc tài liệu 2026-11-23 | 07 | Chuẩn gen_ai.\* đã tách khỏi open-telemetry/semantic-conventions; |

## Benchmark (`benchmark`, 17)

| Dự án | Repo | License | ★ | Bằng chứng | Mục | Tóm tắt |
|---|---|---|---|---|---|---|
| [Berkeley Function Calling Leaderboard (gorilla)](../../02-agent-frameworks/README.md#ch-berkeley-function-calling-leaderboard-gorilla) | `ShishirPatil/gorilla` | Apache-2.0 | 13.085 | đọc tài liệu 2026-11-23 | 02 | BFCL V4: chấm gọi hàm AST + thực thi, multi-turn, agentic (web search, memory, format); |
| [Harbor (Terminal-Bench)](../../07-eval-observability/README.md#ch-harbor-terminal-bench) | `harbor-framework/harbor` | Apache-2.0 | 7.361 | đọc tài liệu 2026-11-23 | 07 | Runner chính thức Terminal-Bench 2.0+; |
| [SWE-bench (harness)](../../01-ai-coding-agents/README.md#ch-swe-bench-harness) | `SWE-bench/SWE-bench` | MIT | 6.234 | đọc tài liệu 2026-11-23 | 01 | Bộ chấm Docker gốc; |
| [AgentBench](../../02-agent-frameworks/README.md#ch-agentbench) | `THUDM/AgentBench` | Apache-2.0 | 3.831 | đọc tài liệu 2026-11-23 | 02 | AgentBench FC (10/2025) trên AgentRL: 5 môi trường container (alfworld, DB, KG, OS, WebShop); |
| [MTEB](../../10-local-llm-rag-memory/README.md#ch-mteb) | `embeddings-benchmark/mteb` | Apache-2.0 | 3.521 | đọc tài liệu 2026-11-23 | 10 | Cổng máy chọn embedding/reranker: CLI `mteb run`, leaderboard HF, task retrieval tự định nghĩa; |
| [tau2-bench](../../07-eval-observability/README.md#ch-tau2-bench) | `sierra-research/tau2-bench` | MIT | 2.500 | đọc tài liệu 2026-11-23 | 07 | τ²/τ³-bench tool–agent–user; |
| [BEIR](../../10-local-llm-rag-memory/README.md#ch-beir) | `beir-cellar/beir` | Apache-2.0 | 2.336 | đọc tài liệu 2026-11-23 | 10 | Chuẩn định dạng corpus/queries/qrels + nDCG@10/Recall@k cho retrieval zero-shot (NeurIPS 2021), 17 bộ dữ liệu tiền xử lý; |
| [OmniDocBench](../../26-document-intelligence-ocr/README.md#omnidocbench) | `opendatalab/OmniDocBench` | Apache-2.0 (eval code); dataset kiểm riêng | 2.140 | đọc mã 2026-11-02 | 26 | Đọc mã/đặc tả 2/11/2026, ea2d138c7d2e; |
| [VBench](../../19-agentic-video-media/README.md#ch-vbench) | `Vchitect/VBench` | Apache-2.0 | 1.851 | đọc tài liệu 2026-11-23 | 19 | Benchmark model sinh video: VBench 16 chiều T2V, VBench-2.0 18 chiều (vật lý, chuyển động người, thường thức), I2V, video dài; |
| [RewardBench](../../07-eval-observability/README.md#ch-rewardbench) | `allenai/reward-bench` | Apache-2.0 | 749 | đọc tài liệu 2026-11-23 | 07 | RewardBench 2 (arXiv 2506.01937) chấm reward model và judge sinh văn bản; |
| [Picovoice Speech-to-Text Benchmark](../../14-voice-multimodal/README.md#ch-picovoice-speech-to-text-benchmark) | `Picovoice/speech-to-text-benchmark` | Apache-2.0 | 698 | đọc tài liệu 2026-11-23 | 14 | Khung đo WER + độ trễ trên LibriSpeech, TED-LIUM, Common Voice, MLS, VoxPopuli, FLEURS…; |
| [SWE-bench Pro](../../01-ai-coding-agents/README.md#ch-swe-bench-pro) | `scaleapi/SWE-bench_Pro-os` | MIT | 570 | đọc tài liệu 2026-11-23 | 01 | V2 642 task định dạng Harbor, HARD-51, locked protocol (agent không mạng trừ endpoint model, verifier chấm `model.patch` ở image sạch (vẫn có mạng)), GATE.md oracle 642/… |
| [WildClawBench](../../07-eval-observability/README.md#nt-wildclawbench) | `InternLM/WildClawBench` | MIT | 535 | đọc mã 2026-11-23 | 07 | Benchmark 60 tác vụ thủ công (6 nhóm, tiếng Anh và Trung) cho agent làm việc thật, chạy mỗi tác vụ trong một container Docker và áp cùng bộ chấm cho bốn harness (OpenCla… |
| [Multi-SWE-bench](../../01-ai-coding-agents/README.md#ch-multi-swe-bench) | `multi-swe-bench/multi-swe-bench` | Apache-2.0 | 364 | đọc tài liệu 2026-11-23 | 01 | ByteDance Seed, issue đa ngôn ngữ (Java/TS/Go/Rust/C++), bản mini/flash; |
| [Open ASR Leaderboard](../../14-voice-multimodal/README.md#ch-open-asr-leaderboard) | `huggingface/open_asr_leaderboard` | Apache-2.0 | 278 | đọc tài liệu 2026-11-23 | 14 | Mã leaderboard ASR của Hugging Face: short/long-form, multilingual (FLEURS/MCV/MLS), chạy HF Jobs cùng phần cứng, có tập riêng tư; |
| [ControlArena](../../07-eval-observability/README.md#nt-control-arena) | `UKGovernmentBEIS/control-arena` | MIT (mã); phụ thuộc Apache-2.0, BSD-3-Clause và LGPL-3.0 | 271 | đọc mã 2026-11-23 | 07 | Thư viện nghiên cứu AI control trên Inspect: nhiều setting sabotage, micro-protocol giám sát và phân tích an toàn/hữu ích. |
| [SWE-bench-Live](../../01-ai-coding-agents/README.md#ch-swe-bench-live) | `microsoft/SWE-bench-Live` | MIT | 264 | đọc tài liệu 2026-11-23 | 01 | Tập tự cập nhật chống nhiễm: Python +50 task/tháng, MultiLang 1.077 task, Windows; |

## Giám sát hệ thống (`ops-monitoring`, 17)

| Dự án | Repo | License | ★ | Bằng chứng | Mục | Tóm tắt |
|---|---|---|---|---|---|---|
| [uptime-kuma](../../36-self-hosting-homelab/README.md#chuyen-uptime-kuma) | `louislam/uptime-kuma` | MIT | 94.567 | đọc tài liệu 2026-11-18 | 36 | Công cụ giám sát uptime tự host, dễ dùng, theo dõi HTTP(s), TCP, ping, DNS, WebSocket, container Docker và có trang trạng thái. |
| [netdata](../../33-reliability-observability-operations/README.md#chuyen-netdata) | `netdata/netdata` | GPL-3.0 | 81.458 | đọc tài liệu 2026-11-18 | 33 | Nền tảng quan sát full-stack thu thập metric theo từng giây, log, trace, luồng mạng, có cảnh báo và học máy, chạy trên Linux, macOS, FreeBSD, Windows, Kubernetes. |
| [grafana](../../33-reliability-observability-operations/README.md#chuyen-grafana) | `grafana/grafana` | AGPL-3.0-only | 77.975 | đọc tài liệu 2026-11-18 | 33 | Nền tảng giám sát và quan sát mã nguồn mở để truy vấn, trực quan hoá, cảnh báo trên metric và log từ nhiều nguồn dữ liệu. |
| [Sentry](../../33-reliability-observability-operations/README.md#anhkysuai-getsentry-sentry) | `getsentry/sentry` | FSL-1.1-Apache-2.0 | 45.868 | đọc tài liệu 2026-11-23 | 33 | Nền tảng thu thập lỗi và ngữ cảnh debug của ứng dụng. |
| [Glances](../../33-reliability-observability-operations/README.md#anhkysuai-nicolargo-glances) | `nicolargo/glances` | LGPL-3.0 | 34.005 | đọc tài liệu 2026-11-23 | 33 | Công cụ Python quan sát hệ thống bằng terminal, WebUI và REST API. |
| [signoz](../../33-reliability-observability-operations/README.md#chuyen-signoz) | `SigNoz/signoz` | MIT | 32.673 | đọc tài liệu 2026-11-18 | 33 | Nền tảng observability mã nguồn mở dựa trên OpenTelemetry, gộp logs, metrics, traces, cảnh báo và dashboard một chỗ. |
| [Beszel](../../33-reliability-observability-operations/README.md#anhkysuai-henrygd-beszel) | `henrygd/beszel` | MIT | 27.564 | đọc tài liệu 2026-11-23 | 33 | Hệ thống giám sát máy chủ với lịch sử, Docker stats và cảnh báo. |
| [skywalking](../../33-reliability-observability-operations/README.md#chuyen-skywalking) | `apache/skywalking` | Apache License 2.0 | 25.010 | đọc tài liệu 2026-11-18 | 33 | Hệ thống APM cho microservice và kiến trúc cloud native: distributed tracing, giám sát và chẩn đoán hệ phân tán. |
| [jaeger](../../33-reliability-observability-operations/README.md#chuyen-jaeger) | `jaegertracing/jaeger` | Apache License 2.0 | 23.422 | đọc tài liệu 2026-11-18 | 33 | Nền tảng distributed tracing do Uber tạo và tặng CNCF, nhận trace qua OTLP và có giao diện truy vấn. |
| [openobserve](../../33-reliability-observability-operations/README.md#chuyen-openobserve) | `openobserve/openobserve` | GNU Affero General Public License v3.0 | 23.096 | đọc tài liệu 2026-11-18 | 33 | Nền tảng observability cloud native viết bằng Rust cho logs, metrics, traces, RUM và quan sát AI/LLM, định vị thay Datadog, Splunk, Elasticsearch. |
| [vector](../../33-reliability-observability-operations/README.md#chuyen-vector) | `vectordotdev/vector` | Mozilla Public License 2.0 | 22.895 | đọc tài liệu 2026-11-18 | 33 | Pipeline dữ liệu observability hiệu năng cao viết bằng Rust, chạy như agent hoặc aggregator để thu, biến đổi và định tuyến logs và metrics. |
| [kibana](../../33-reliability-observability-operations/README.md#chuyen-kibana) | `elastic/kibana` | Mặc định ba giấy phép AGPL-3.0-only | 21.382 | đọc tài liệu 2026-11-18 | 33 | Giao diện để truy vấn, phân tích, trực quan hoá và quản lý dữ liệu lưu trong Elasticsearch. |
| [GoAccess](../../33-reliability-observability-operations/README.md#anhkysuai-allinurl-goaccess) | `allinurl/goaccess` | MIT | 21.150 | đọc tài liệu 2026-11-23 | 33 | Công cụ phân tích access log web, hiển thị terminal hoặc dashboard HTML thời gian thực. |
| [VictoriaMetrics](../../33-reliability-observability-operations/README.md#chuyen-victoriametrics) | `VictoriaMetrics/VictoriaMetrics` | Apache-2.0 | 18.126 | đọc tài liệu 2026-11-18 | 33 | Cơ sở dữ liệu chuỗi thời gian và giải pháp giám sát nhanh, tiết kiệm, mở rộng được; |
| [zipkin](../../33-reliability-observability-operations/README.md#chuyen-zipkin) | `openzipkin/zipkin` | Apache-2.0 | 17.475 | đọc tài liệu 2026-11-18 | 33 | Hệ thống truy vết phân tán, thu thập và tra cứu dữ liệu thời gian để gỡ lỗi độ trễ trong kiến trúc dịch vụ, kèm giao diện web và sơ đồ phụ thuộc. |
| [OpenTelemetry Collector Contrib](../../33-reliability-observability-operations/README.md#otel-collector-egress) | `open-telemetry/opentelemetry-collector-contrib` | Apache-2.0 | — | đọc mã 2026-11-04 | 33 | Scoped redaction processor: allowlist, ignored keys bypass, allowed values precedence; |
| [Pyrra](../../33-reliability-observability-operations/README.md#pyrra-slo-operations) | `pyrra-dev/pyrra` | Apache-2.0 | — | đọc mã 2026-11-04 | 33 | SLO UI/operator+filesystem modes; |
