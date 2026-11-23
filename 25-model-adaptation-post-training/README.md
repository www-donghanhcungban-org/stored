# 25 · Model Adaptation & Post-training

> Từ một model nền đến phiên bản chuyên biệt có thể kiểm chứng: chọn đúng phương pháp, đóng băng dữ liệu, huấn luyện, đánh giá, xuất và triển khai. Khảo sát 2/11/2026; đọc README, LICENSE, CI và các đường mã nêu trong từng hồ sơ. Không cài, build hay chạy training của repo ngoài; mọi nhận xét về tốc độ, VRAM và chất lượng ở đây không phải phép đo tại kho này.

## 1. Phạm vi và ranh giới

Mục này giải quyết **thay đổi tham số hoặc cách hậu huấn luyện model**. [Mục 17](../17-prompt-engineering/README.md) quản lý prompt; [mục 10](../10-local-llm-rag-memory/README.md) quản lý truy xuất/bộ nhớ/inference; [mục 24](../24-ai-data-engineering/README.md) quản lý đầu vào và nhãn; [mục 07](../07-eval-observability/README.md) quản lý đánh giá; serving quy mô thuộc [mục 10](../10-local-llm-rag-memory/README.md).

| Lớp | Thay đổi gì | Câu hỏi quyết định |
|---|---|---|
| Prompt / context | Chỉ dẫn và ví dụ lúc gọi | Có thể giải bằng chỉ dẫn rõ và context đủ hay chưa? |
| RAG | Thông tin được truy xuất | Tri thức có cập nhật, cần dẫn nguồn hay phân quyền từng tài liệu không? |
| SFT | Học từ cặp đầu vào–đáp án / hội thoại mẫu | Có cần hành vi, định dạng hoặc kỹ năng lặp lại mà prompt chưa đạt không? |
| LoRA / QLoRA | Cách cập nhật một tập tham số nhỏ; QLoRA giữ base đã lượng tử hoá | Tài nguyên, kiến trúc và đường xuất có hỗ trợ không? Đây không phải mục tiêu học riêng. |
| Preference tuning / DPO | Học lựa chọn tốt hơn từ cặp chosen–rejected | Cặp đáp án có cùng prompt, khác biệt có ý nghĩa và nhãn đáng tin không? |
| RL với reward | Học bằng rollout và tín hiệu thưởng | Reward có đo đúng kết quả, kiểm được gian lận và đủ ngân sách rollout không? |
| Continued pretraining / full tuning | Học tiếp miền hoặc cập nhật nhiều tham số | Lợi ích dự kiến có đủ bù chi phí, rủi ro quên kiến thức và gánh vận hành không? |

Fine-tune không tự tạo cơ chế trích nguồn, xoá dữ liệu theo yêu cầu hay cập nhật tri thức tức thời. Hệ thống có thể ghép RAG với model đã tune; cần đo đóng góp từng phần bằng baseline tách biệt.

## 2. Chọn công cụ theo nhu cầu

| Nhu cầu | Điểm bắt đầu | Khi cân nhắc lựa chọn khác | Điều phải kiểm trước |
|---|---|---|---|
| Thêm adapter vào pipeline Transformers đang có | PEFT | TRL nếu cần trainer SFT/DPO/GRPO | Model revision, target modules, tokenizer và adapter format |
| Nghiên cứu SFT/preference/RL bằng Python | TRL | verl khi rollout/training phân tán thành nút thắt | Loss masking, reference model, reward và phần cứng được CI phủ |
| Thử nghiệm local với UI, xuất GGUF/định dạng khác | Unsloth | PEFT/TRL cho pipeline nhỏ ít thành phần | License core/Studio riêng, hỗ trợ model/backend và bản export thực |
| Pipeline cấu hình, distributed training | Axolotl | LlamaFactory cho WebUI và nhiều stage trong một sản phẩm | Lưu config đã resolve, checkpoint/restart, tương thích kernel |
| Nhóm cần CLI/WebUI chung cho nhiều model/stage | LlamaFactory | TRL/PEFT nếu cần sửa vòng học sâu | Template hội thoại, schema dataset, stage và dependency pin |
| RL post-training đa GPU, nhiều worker rollout/reward | verl | TRL cho baseline nhỏ dễ kiểm | Ray/resource pool, rollout engine, reward sandbox và replay |

Ba lựa chọn cùng dòng không mặc nhiên thay thế nhau: **PEFT là lớp adapter**, **TRL là lớp thuật toán/trainer**, còn Unsloth/Axolotl/LlamaFactory đóng gói nhiều lớp. So sánh từng đường chạy và từng cấu hình, không cộng số sao thành điểm chất lượng.

## 3. Hồ sơ đọc mã

<a id="peft"></a>

### 3.1. PEFT — adapter là artifact có hợp đồng

| Thuộc tính | Giá trị |
|---|---|
| Repo / tác giả | [huggingface/peft](https://github.com/huggingface/peft) |
| Bằng chứng đọc | `d672982142a705f47696db2dd2218805517509cd` · commit 2026-11-02 · chưa archive khi đọc 2/11/2026 |
| ★ · license (2/11/2026) | 21,866 ★ (GitHub REST API); Apache-2.0 |
| Giá trị cốt lõi | Thêm adapter/LoRA vào model nền; tích hợp Transformers, Diffusers và Accelerate. |
| Đường mã đã đọc | `LoraModel` cùng `PeftModel.save_pretrained()` / `from_pretrained()`: lưu adapter/config, có `selected_adapters`, `safe_serialization=True`, tuỳ chọn lưu embedding. |
| CI đã đọc | Workflow `tests.yml` có bộ test và kiểm chất lượng; sự hiện diện của workflow không chứng minh model tuỳ chọn đã được kiểm trên phần cứng của người dùng. |
| Tích hợp | Dùng PEFT trong dự án huấn luyện; manifest phải ghim base revision, tokenizer revision, adapter config và hash artifact. Kiểm tải lại adapter trong tiến trình inference sạch. |
| Hạn chế / rủi ro | Một adapter không mang đầy đủ base model. `target_modules`, phần embedding bổ sung và phiên bản thư viện ảnh hưởng tính tương thích; checkpoint adapter và model đã merge cần hai kết quả eval riêng. |
| Bài học kiến trúc | Đơn vị phát hành là **base + adapter + tokenizer + config**, không chỉ một thư mục trọng số. License Apache của thư viện không cấp thêm quyền cho base/weights/dataset. |
| Thay thế / liên quan | TRL (trainer), Axolotl/LlamaFactory (đóng gói pipeline), mục 24 và mục 07. |

**Nguồn hồ sơ:** [README](https://github.com/huggingface/peft/blob/d672982142a705f47696db2dd2218805517509cd/README.md) · [LICENSE](https://github.com/huggingface/peft/blob/d672982142a705f47696db2dd2218805517509cd/LICENSE) · [save/load artifact](https://github.com/huggingface/peft/blob/d672982142a705f47696db2dd2218805517509cd/src/peft/peft_model.py) · [LoRA](https://github.com/huggingface/peft/blob/d672982142a705f47696db2dd2218805517509cd/src/peft/tuners/lora/model.py) · [CI](https://github.com/huggingface/peft/blob/d672982142a705f47696db2dd2218805517509cd/.github/workflows/tests.yml).

<a id="trl"></a>

### 3.2. TRL — SFT, preference và RL dùng chung nền trainer

| Thuộc tính | Giá trị |
|---|---|
| Repo / tác giả | [huggingface/trl](https://github.com/huggingface/trl) |
| Bằng chứng đọc | `c734c60d85766aff4542a00643a2ca7e4a3c72ac` · commit 2026-11-02 · chưa archive khi đọc 2/11/2026 |
| ★ · license (2/11/2026) | 19,657 ★ (GitHub REST API); Apache-2.0 |
| Giá trị cốt lõi | Các trainer SFT, DPO, GRPO trên hệ Transformers; ghép PEFT và backend phân tán khi phù hợp. |
| Đường mã đã đọc | `sft_trainer.py` phân biệt dataset language-modeling với prompt–completion và hội thoại, kiểm `assistant_only_loss` / `completion_only_loss`; đã đọc đường DPO và GRPO để phân biệt preference pair với rollout/reward. |
| CI đã đọc | Workflow `tests.yml` định nghĩa nhiều job/nhóm test; không suy từ test Python sang tương đương số học của mọi GPU/backend. |
| Tích hợp | Cố định trainer/config, render vài mẫu thành token và mask trước training; giữ log reward riêng với metric chất lượng held-out; ghim phiên bản Transformers/PEFT theo đường chạy. |
| Hạn chế / rủi ro | Tối ưu loss sai vị trí có thể dạy model lặp lại user/system prompt. Một cờ assistant-only không thay việc kiểm template hỗ trợ mask. Reward tăng không bảo đảm task success hoặc an toàn tăng. |
| Bài học kiến trúc | Trình bày rõ **schema dữ liệu → template → token/mask → loss**. Kiểm lớp trung gian này trước khi tăng số GPU hay độ phức tạp thuật toán. |
| Thay thế / liên quan | PEFT cho adapter; verl cho RL phân tán; Axolotl/LlamaFactory cho cấu hình; mục 17 và mục 24. |

**Nguồn hồ sơ:** [README](https://github.com/huggingface/trl/blob/c734c60d85766aff4542a00643a2ca7e4a3c72ac/README.md) · [LICENSE](https://github.com/huggingface/trl/blob/c734c60d85766aff4542a00643a2ca7e4a3c72ac/LICENSE) · [SFT và masking](https://github.com/huggingface/trl/blob/c734c60d85766aff4542a00643a2ca7e4a3c72ac/trl/trainer/sft_trainer.py) · [DPO](https://github.com/huggingface/trl/blob/c734c60d85766aff4542a00643a2ca7e4a3c72ac/trl/trainer/dpo_trainer.py) · [GRPO](https://github.com/huggingface/trl/blob/c734c60d85766aff4542a00643a2ca7e4a3c72ac/trl/trainer/grpo_trainer.py) · [CI](https://github.com/huggingface/trl/blob/c734c60d85766aff4542a00643a2ca7e4a3c72ac/.github/workflows/tests.yml).

<a id="unsloth"></a>

### 3.3. Unsloth — core training và Studio/CLI có license khác nhau

| Thuộc tính | Giá trị |
|---|---|
| Repo / tác giả | [unslothai/unsloth](https://github.com/unslothai/unsloth) |
| Bằng chứng đọc | `63a3896459a9d57396cb1a61b3041b678387870b` · commit 2026-11-02 · chưa archive khi đọc 2/11/2026 |
| ★ · license (2/11/2026) | 78,950 ★ (GitHub REST API); Core Apache-2.0; Studio AGPL-3.0-only; CLI AGPLv3 |
| Giá trị cốt lõi | Hiện là bộ công cụ có ứng dụng desktop/UI chạy và huấn luyện model, lõi Python tối ưu đường model/adapter, nhiều đường export. Không còn nên mô tả toàn repo chỉ là thư viện fine-tuning. |
| Đường mã đã đọc | `FastLlamaModel.from_pretrained()` có nhánh lượng tử hoá; `get_peft_model()` ghép adapter và gradient checkpointing. Studio có helper tạo train/eval split bằng seed cố định. |
| CI đã đọc | `studio-backend-ci.yml` định nghĩa kiểm backend; ngoài ra tree có workflow cho từng nền tảng. Chưa chạy các job, export hay đo VRAM. |
| Tích hợp | Chọn rõ dùng core Python hay Studio. Giữ một cấu hình/model nhỏ làm baseline, lưu dependency/backend chính xác rồi kiểm artifact ở runtime đích. |
| Hạn chế / rủi ro | README nêu tăng tốc/giảm VRAM là tuyên bố của nhà phát triển, không phải kết quả tái lập tại đây. Split theo seed của Studio là tiện ích, không tự chặn dữ liệu cùng tài liệu/khách hàng lọt sang hai tập. |
| License thật | README §License ghi hai lớp; `LICENSE` gốc tách `unsloth/*`/tests/scripts là Apache và `studio/*`, `unsloth_cli/*` là AGPLv3; header của `eval_dataset.py` ghi rõ AGPL-3.0-only. Khi nhúng/sửa/triển khai Studio cần đọc nghĩa vụ tương ứng; không lấy nhãn Apache ở gốc áp cho toàn repo. |
| Bài học kiến trúc | UI thuận tiện vẫn cần export một manifest training và dataset split độc lập; tách license theo component thay vì một cờ “open source” duy nhất. |
| Thay thế / liên quan | PEFT/TRL cho pipeline thư viện; Axolotl/LlamaFactory cho cấu hình; mục 10, 24 và 26. |

**Nguồn hồ sơ:** [README và license scope](https://github.com/unslothai/unsloth/blob/63a3896459a9d57396cb1a61b3041b678387870b/README.md) · [core LICENSE](https://github.com/unslothai/unsloth/blob/63a3896459a9d57396cb1a61b3041b678387870b/LICENSE) · [Studio LICENSE](https://github.com/unslothai/unsloth/blob/63a3896459a9d57396cb1a61b3041b678387870b/studio/LICENSE.AGPL-3.0) · [loader/adapter](https://github.com/unslothai/unsloth/blob/63a3896459a9d57396cb1a61b3041b678387870b/unsloth/models/llama.py) · [split eval](https://github.com/unslothai/unsloth/blob/63a3896459a9d57396cb1a61b3041b678387870b/studio/backend/core/training/eval_dataset.py) · [CI](https://github.com/unslothai/unsloth/blob/63a3896459a9d57396cb1a61b3041b678387870b/.github/workflows/studio-backend-ci.yml).

<a id="axolotl"></a>

### 3.4. Axolotl — cấu hình có thể phát lại và checkpoint có thể phục hồi

| Thuộc tính | Giá trị |
|---|---|
| Repo / tác giả | [axolotl-ai-cloud/axolotl](https://github.com/axolotl-ai-cloud/axolotl) |
| Bằng chứng đọc | `da7d6b8138d6c0bcf7815ffb2475845dd40718d5` · commit 2026-11-02 · chưa archive khi đọc 2/11/2026 |
| ★ · license (2/11/2026) | 12,654 ★ (GitHub REST API); Apache-2.0 |
| Giá trị cốt lõi | Pipeline fine-tuning đa model, cấu hình và tích hợp phân tán/kernel; phù hợp nhóm muốn chuẩn hoá một recipe training. |
| Đường mã đã đọc | `train.py` tách setup model/reference/trainer, xác định checkpoint trước `trainer.train(resume_from_checkpoint=...)`, lưu tokenizer/config, model card và trọng số qua các nhánh backend. |
| CI đã đọc | `tests.yml` là bộ kiểm nhiều job; tree còn có workflow CPU/distributed/GPU. Chưa xác minh kết quả chạy và coverage của cấu hình riêng. |
| Tích hợp | Lưu YAML gốc cùng config đã resolve, dataset revision, seed và checkpoint. Kiểm resume một lần trong dự án tích hợp trước khi giao job dài; kiểm artifact sau bước save/merge. |
| Hạn chế / rủi ro | Resume checkpoint chứa optimizer/scheduler khác với chỉ nạp adapter. Cấu hình nhiều backend tạo ma trận tương thích lớn; không lấy ví dụ của model này áp sang model khác. |
| Bài học kiến trúc | Recipe là artifact có phiên bản; quá trình phục hồi cần kiểm được, không chỉ có đường chạy từ đầu. |
| Thay thế / liên quan | LlamaFactory cho CLI/WebUI chung, TRL/PEFT khi cần kiểm soát code trainer, verl cho RL rollout quy mô lớn; mục 13 và 24. |

**Nguồn hồ sơ:** [README](https://github.com/axolotl-ai-cloud/axolotl/blob/da7d6b8138d6c0bcf7815ffb2475845dd40718d5/README.md) · [LICENSE](https://github.com/axolotl-ai-cloud/axolotl/blob/da7d6b8138d6c0bcf7815ffb2475845dd40718d5/LICENSE) · [setup/train/save/resume](https://github.com/axolotl-ai-cloud/axolotl/blob/da7d6b8138d6c0bcf7815ffb2475845dd40718d5/src/axolotl/train.py) · [CI](https://github.com/axolotl-ai-cloud/axolotl/blob/da7d6b8138d6c0bcf7815ffb2475845dd40718d5/.github/workflows/tests.yml).

<a id="llamafactory"></a>

### 3.5. LlamaFactory — nhiều stage nhưng mỗi stage có điều kiện riêng

| Thuộc tính | Giá trị |
|---|---|
| Repo / tác giả | [hiyouga/LlamaFactory](https://github.com/hiyouga/LlamaFactory) |
| Bằng chứng đọc | `9997aa078b4da35e04bb492a8a27d45141f4b80b` · commit 2026-10-31 · chưa archive khi đọc 2/11/2026 |
| ★ · license (2/11/2026) | 75,845 ★ (GitHub REST API); Apache-2.0 |
| Giá trị cốt lõi | Cổng CLI/WebUI và recipe chung cho nhiều LLM/VLM, các stage pretraining, SFT, reward model, PPO, DPO, KTO trong đường cấu hình đã đọc. |
| Đường mã đã đọc | `FinetuningArguments` kiểm `stage`, phương pháp `lora/oft/freeze/full`, một số tổ hợp không hợp lệ và yêu cầu reward model cho PPO. `train/sft/workflow.py` tách dataset/model/collator/trainer và các pha train/eval/save. |
| CI đã đọc | `tests.yml` tạo matrix Python 3.11–3.13 trên Linux/Windows/macOS, cài PyTorch CPU, kiểm style/license/build/test; workflow CUDA/NPU ở file khác. Đây không phải bằng chứng mọi model đều huấn luyện được trên CPU. |
| Tích hợp | Chọn template/schema dataset trước khi dùng UI; xuất cấu hình ra file có revision. Kiểm input/output trên mẫu có tool call, Unicode tiếng Việt và hội thoại nhiều lượt theo nhu cầu. |
| Hạn chế / rủi ro | Danh sách “hỗ trợ model” không nói đủ khả năng của từng stage/backend. Không suy tính năng của v1 trainer sang đường legacy hoặc ngược lại. License trọng số và dữ liệu phải kiểm riêng. |
| Bài học kiến trúc | Chặn tổ hợp không hợp lệ bằng cấu hình có kiểu trước khi cấp tài nguyên; UI cần tạo được recipe tái lập để review và dùng CI. |
| Thay thế / liên quan | Axolotl, TRL/PEFT, Unsloth; mục 18 cho tập kiểm tiếng Việt và mục 24 cho dataset contract. |

**Nguồn hồ sơ:** [README](https://github.com/hiyouga/LlamaFactory/blob/9997aa078b4da35e04bb492a8a27d45141f4b80b/README.md) · [LICENSE](https://github.com/hiyouga/LlamaFactory/blob/9997aa078b4da35e04bb492a8a27d45141f4b80b/LICENSE) · [ràng buộc stage](https://github.com/hiyouga/LlamaFactory/blob/9997aa078b4da35e04bb492a8a27d45141f4b80b/src/llamafactory/hparams/finetuning_args.py) · [SFT workflow](https://github.com/hiyouga/LlamaFactory/blob/9997aa078b4da35e04bb492a8a27d45141f4b80b/src/llamafactory/train/sft/workflow.py) · [CI](https://github.com/hiyouga/LlamaFactory/blob/9997aa078b4da35e04bb492a8a27d45141f4b80b/.github/workflows/tests.yml).

<a id="verl"></a>

### 3.6. verl / HybridFlow — tách rollout, reward và cập nhật policy

| Thuộc tính | Giá trị |
|---|---|
| Repo / tác giả | [verl-project/verl](https://github.com/verl-project/verl) |
| Bằng chứng đọc | `6879e1ab07b9cfd0b4b27c31ca4e7afcad1466b3` · commit 2026-11-02 · chưa archive khi đọc 2/11/2026 |
| ★ · license (2/11/2026) | 24,102 ★ (GitHub REST API); Apache-2.0 |
| Giá trị cốt lõi | Hệ RL post-training với điều phối worker phân tán; hướng nghiên cứu HybridFlow có controller kết hợp để ánh xạ training/generation lên phần cứng. |
| Đường mã đã đọc | `RayPPOTrainer` điều phối actor/rollout, critic, reference/reward và resource pool; tính advantage/KL, validation dataloader và ghi mẫu rollout. Dataset RL xử lý prompt/tokenization trong lớp riêng. |
| CI đã đọc | `cpu_unit_tests.yml` là lớp kiểm CPU; tree còn có GPU/NPU và nhiều workflow E2E theo rollout engine. Không coi test CPU là xác nhận hiệu quả của một cụm RL. |
| Tích hợp | Bắt đầu bằng baseline nhỏ có reward kiểm được; đặt trần số rollout/token/thời gian/chi phí, ghi revision của actor và reward, cấu hình pool tài nguyên, checkpoint và log validation. |
| Hạn chế / rủi ro | Thêm rollout engine làm tăng chi phí bộ nhớ và đồng bộ; reward có thể bị khai thác hoặc sai nhãn. Khi reward chấm code/tool, phải cách ly executor như mục 11/12; đây không phải chức năng được bảo đảm chỉ nhờ chọn framework. |
| Bài học kiến trúc | Tách metric “policy tối ưu reward” khỏi “người dùng hoàn thành việc”, giữ validation không tham gia reward và lưu trace đủ để điều tra. |
| Thay thế / liên quan | TRL cho baseline SFT/GRPO/DPO ít lớp; PEFT cho adapter; Axolotl/LlamaFactory cho recipe; mục 07, 11, 12, 21 và 24. |

**Nguồn hồ sơ:** [README](https://github.com/verl-project/verl/blob/6879e1ab07b9cfd0b4b27c31ca4e7afcad1466b3/README.md) · [LICENSE](https://github.com/verl-project/verl/blob/6879e1ab07b9cfd0b4b27c31ca4e7afcad1466b3/LICENSE) · [trainer/resource/reward](https://github.com/verl-project/verl/blob/6879e1ab07b9cfd0b4b27c31ca4e7afcad1466b3/verl/trainer/ppo/ray_trainer.py) · [RL dataset](https://github.com/verl-project/verl/blob/6879e1ab07b9cfd0b4b27c31ca4e7afcad1466b3/verl/utils/dataset/rl_dataset.py) · [CI](https://github.com/verl-project/verl/blob/6879e1ab07b9cfd0b4b27c31ca4e7afcad1466b3/.github/workflows/cpu_unit_tests.yml).

## 4. Chuẩn và hồ sơ cần mang theo model

Các tài liệu dưới đây là nguồn gốc phương pháp và khung báo cáo; chúng không phải chứng nhận rằng một model đã đạt chất lượng hay an toàn.

| Nguồn gốc | Ý nghĩa thực dụng | Điều không được suy rộng |
|---|---|---|
| [LoRA](https://arxiv.org/abs/2106.09685) | Cố định base và học cập nhật low-rank; báo rank, alpha, dropout, modules, embeddings được lưu | Ít tham số trainable không có nghĩa tổng VRAM chỉ bằng kích thước adapter |
| [QLoRA](https://arxiv.org/abs/2305.14314) | Backprop qua base lượng tử hoá vào adapter; ghi quantization và optimizer | Kết quả phần cứng trong paper không là bảo đảm cho mọi model/context/batch |
| [DPO](https://arxiv.org/abs/2305.18290) | Học từ preference pair với objective cụ thể | Chosen/rejected không phải sự thật tuyệt đối; DPO không thay quy trình xây nhãn |
| [HybridFlow](https://arxiv.org/abs/2409.19256) | Thiết kế orchestration training/generation phân tán | Throughput paper phụ thuộc cấu hình; không dự báo tốc độ cụm khác |
| [LlamaFactory paper (ACL 2024)](https://arxiv.org/abs/2403.13372) | Nguồn thiết kế framework thống nhất nhiều phương pháp/model qua CLI/WebUI | Paper 2024 không đại diện toàn bộ feature/compatibility của HEAD 2026 |
| [Model Cards](https://arxiv.org/abs/1810.03993) | Ghi intended use, ngoài phạm vi, dữ liệu, cách đo, kết quả theo nhóm và hạn chế | Có model card không đồng nghĩa được kiểm toán độc lập |
| [Datasheets for Datasets](https://arxiv.org/abs/1803.09010) | Giải thích nguồn, thành phần, thu thập và cách dùng dữ liệu training | License công cụ xử lý không cấp quyền cho nội dung dataset |

**Manifest phát hành nên có:** base/tokenizer revision; dataset/split hash; code/trainer/dependency revision; config đã resolve và seed; precision/quantization/adapter target; phần cứng thực chạy; checkpoint đầu ra/hash; metric baseline–candidate; license code/base/adapter/dataset; runtime đích và kết quả kiểm artifact sau export. Artifact này thuộc dự án tích hợp, kho `stored` chỉ giữ hồ sơ và tiêu chí tham khảo.

## 5. Cổng chất lượng từ dữ liệu đến runtime

| Cổng | Bằng chứng phải lưu ở dự án tích hợp | Chặn phát hành khi |
|---|---|---|
| Baseline | Cùng tập kiểm cho base + prompt, base + RAG và candidate tune; mục tiêu định trước | Chưa biết lỗi cần sửa nằm ở truy xuất, prompt hay hành vi |
| Dữ liệu và quyền | Dataset card, đồng ý/quyền sử dụng, hash/lineage, leakage report theo tài liệu/người/nguồn | Không rõ quyền dùng, PII ngoài mục đích hoặc train–test trùng nhóm |
| Token và loss | Vài mẫu đã render, token/mask, phần bị truncation, test Unicode/tool-call | Mask học user/system sai mục tiêu, đáp án bị cắt hoặc template lệch inference |
| Tài nguyên | Peak allocated/reserved GPU memory, batch/context, tokens thực, thời gian/chi phí trong cấu hình chạy thật | Vượt ngân sách hoặc chỉ ước VRAM từ số tham số |
| Tiến trình | Loss/NaN, checkpoint, log validation, thử resume có kiểm soát | Không thể phục hồi; chọn checkpoint theo tập test cuối |
| Held-out | Task success/định dạng/groundedness nếu dùng RAG, regression kiến thức chung và nhóm tiếng Việt | Candidate không đạt ngưỡng đã định hoặc giảm nhóm quan trọng |
| Preference / reward | Nguồn nhãn, agreement, kiểm reward hacking, judge model/prompt revision | Reward tăng nhưng human/task eval không cải thiện hoặc giữ được |
| Xuất artifact | Load lại trong tiến trình sạch, đúng tokenizer/template, eval sau merge/quantization | File export hợp lệ nhưng hành vi khác candidate đã chấp nhận |
| Serving | Độ trễ/throughput/VRAM theo workload, rate limit/rollback; đối chiếu mục 10 | Chưa có đường rollback hoặc ngân sách inference không đáp ứng |

Không có trần VRAM phổ quát cho “model 7B/8B”. Trọng số, activation theo độ dài context, gradient/optimizer, precision, checkpointing, batch và cách phân tán đều góp phần. Cổng ở trên yêu cầu đo cấu hình cụ thể; số do README công bố chỉ là ứng viên cần tái lập. Loss thấp không đủ chứng minh chất lượng hội thoại, an toàn, tri thức hay độ tin cậy của tool call.

## 6. Stack tham khảo và bài học ghép kho

1. [Mục 17](../17-prompt-engineering/README.md) cố định prompt/schema; [mục 10](../10-local-llm-rag-memory/README.md) thử baseline truy xuất trước khi quyết định tune.
2. [Mục 24](../24-ai-data-engineering/README.md) đóng băng dữ liệu, nhóm split và nhãn; [mục 18](../18-vietnam-community/README.md) cung cấp hướng tìm eval tiếng Việt phù hợp tác vụ.
3. Chọn PEFT + TRL nếu cần pipeline thư viện; Unsloth/Axolotl/LlamaFactory nếu giá trị chính là đóng gói; verl khi quy mô RL tạo nhu cầu orchestration cụ thể.
4. [Mục 07](../07-eval-observability/README.md) giữ held-out, trace và regression; [mục 12](../12-ai-security-guardrails/README.md) kiểm nguồn model/data và reward executor.
5. Chỉ bàn giao artifact đã kiểm sau export cho runtime [mục 10](../10-local-llm-rag-memory/README.md) kèm card/manifest và đường quay về base.

**Trần được nâng:** kho có đường đi từ recipe dữ liệu đến adapter/model đã kiểm, tránh lấy “hỗ trợ LoRA” hay một biểu đồ benchmark làm lý do duy nhất để tích hợp. Chưa chạy phép đo độc lập, chưa kiểm license từng model/dataset và chưa xác minh mọi backend được quảng bá **(chưa xác minh)**.

<a id="factory-2026-11-04"></a>

## 6b. Nâng trần 4/11/2026: hậu huấn luyện thành một tuyến phát hành có đường thoát

**Trần hiện tại:** §3–§6 đã có trainer, loss mask và artifact. Xưởng còn cần một quyết định kinh tế trước training, phép kiểm khôi phục thực sự, hợp đồng chuyển sang inference và kế hoạch khi upstream ngừng duy trì. Phần này là thiết kế vận dụng của kho; chưa huấn luyện hoặc tái lập số đo upstream.

| Lựa chọn | Dùng khi | Cổng quyết định của xưởng | Không được suy ra |
|---|---|---|---|
| Prompt/RAG ở mục 17/10 | Lỗi do thiếu tri thức/context hoặc cần cập nhật/xóa nguồn | Baseline cùng corpus, quyền tài liệu và chi phí/tác vụ được chấp nhận | Fine-tune sẽ tự bổ sung citation hay cập nhật tri thức |
| PEFT + TRL ở §3.1–3.2 | Cần kiểm soát adapter, mask, trainer bằng Python | Snapshot dữ liệu/tokenizer, kiểm token mask, held-out theo tác vụ | Loss giảm tương đương chất lượng sản phẩm tăng |
| Axolotl/LlamaFactory ở §3.4–3.5 | Nhóm cần cấu hình và tuyến train nhất quán | Resolve config, restart, export rồi tải trong runtime sạch | YAML giống nhau bảo đảm kết quả giống trên mọi GPU |
| verl ở §3.6 | Reward/rollout phân tán có lợi ích đã đo | Eval reward hacking, timeout sandbox, budget rollout, held-out độc lập | Reward cao là tiêu chí phát hành đủ |
| torchtune dưới đây | Đọc kiến trúc recipe/checkpointer, duy trì pipeline cũ | Ghim toàn stack và chứng minh đường chuyển sang trainer còn được duy trì | Nhãn PyTorch bảo đảm đang được duy trì |

<a id="torchtune-maintenance"></a>

### torchtune: bài học về checkpoint và điều kiện rời một dependency

| Thuộc tính | Giá trị |
|---|---|
| Repo, loại | [pytorch/torchtune](https://github.com/pytorch/torchtune), `model-training` |
| Phiên bản / license | `bd2a0fc7c31430972728494fa01aaeeb0ebf1ba1`; BSD-3-Clause, không thay license model/dataset |
| Kiểm chứng 2026-11-04 | `code-read`: README, recipe LoRA single-device, checkpointer và CI; chưa chạy training/restore/GPU |
| ★ / trạng thái | Không lấy số mới; README tự thông báo không còn được duy trì tích cực, development đã thu hẹp trong 2025; không suy ra trạng thái archive qua API |
| Cơ chế đã đọc | Recipe khôi phục epoch/seed/max steps từ checkpoint; khi seed hoặc max steps khác config, cảnh báo rồi dùng giá trị checkpoint. Docstring của recipe ghi optimizer/recipe state lưu ở cuối epoch và chưa hỗ trợ checkpoint giữa epoch. Phạm vi là recipe này, không khái quát mọi recipe. |
| CI | `unit_test.yaml` và `gpu_test.yaml` tách unit/GPU, có điều kiện owner; đọc workflow không chứng minh job hiện còn chạy hoặc đã pass. |
| Tích hợp / giới hạn | Dùng như tài liệu kiến trúc hoặc dependency cũ được cô lập; với dự án mới so PEFT/TRL/Axolotl và khả năng chuyển đổi artifact trước. Recipe state, weights và sampler/data position là các hợp đồng khác nhau. |

**Đã đổi so với đợt trước:** thêm bằng chứng maintenance trực tiếp từ README của torchtune. Đây là trường hợp loại khỏi shortlist triển khai mới, không phải thêm một công cụ chỉ vì thương hiệu. Không xác minh lại ngày/mức của sáu hồ sơ cũ chỉ bằng lần đọc này.

**Tuyến nâng sâu cho xưởng:**

1. Khóa quyết định đầu tư: lỗi mục tiêu, baseline prompt/RAG, bộ dữ liệu có quyền dùng, metric chất lượng và ngân sách inference/training. Giữ test theo khách hàng/tenant và thời gian, tránh cùng tài liệu rơi vào train và test.
2. Duyệt vài mẫu đã tokenize cùng mask thực tế. Lưu dataset revision, template, base/tokenizer revision, dependency/kernel/GPU và config đã resolve; hash manifest, không đưa dữ liệu khách hàng vào log mặc định.
3. Đặt ngân sách thất bại: VRAM, wall time, token/rollout, checkpoint retention. Tiêm dừng tiến trình tại ranh giới đã hỗ trợ rồi kiểm có tải optimizer/recipe state; không gọi việc chỉ tải weights là resume training.
4. Eval base, adapter, merged và exported runtime trên cùng corpus; so chất lượng từng nhóm, schema/tool-call, latency và chi phí/tác vụ đạt. Ghim ngưỡng trước khi xem kết quả, không dùng một điểm benchmark chung để thay chấp nhận nghiệp vụ.
5. Phát hành base + adapter + tokenizer + config + kết quả eval + quyền weights/dataset. Canary, kill switch và rollback về phiên bản cũ phải hoạt động độc lập với training; nối [mục 30](../30-software-testing-quality/README.md), [31](../31-software-supply-chain-security/README.md) và [32](../32-platform-delivery-engineering/README.md).
6. Giữ exit test: artifact xuất được nạp lại bằng runtime khác hoặc ghi rõ phụ thuộc không thể thay. Trường hợp torchtune cho thấy cần người sở hữu dependency và điều kiện chuyển đổi, không chỉ pin phiên bản.

**Nguồn §6b:** [README.md](https://github.com/pytorch/torchtune/blob/bd2a0fc7c31430972728494fa01aaeeb0ebf1ba1/README.md) · [LICENSE](https://github.com/pytorch/torchtune/blob/bd2a0fc7c31430972728494fa01aaeeb0ebf1ba1/LICENSE) · [recipes/lora_finetune_single_device.py](https://github.com/pytorch/torchtune/blob/bd2a0fc7c31430972728494fa01aaeeb0ebf1ba1/recipes/lora_finetune_single_device.py) · [torchtune/training/checkpointing/_checkpointer.py](https://github.com/pytorch/torchtune/blob/bd2a0fc7c31430972728494fa01aaeeb0ebf1ba1/torchtune/training/checkpointing/_checkpointer.py) · [.github/workflows/unit_test.yaml](https://github.com/pytorch/torchtune/blob/bd2a0fc7c31430972728494fa01aaeeb0ebf1ba1/.github/workflows/unit_test.yaml) · [.github/workflows/gpu_test.yaml](https://github.com/pytorch/torchtune/blob/bd2a0fc7c31430972728494fa01aaeeb0ebf1ba1/.github/workflows/gpu_test.yaml). Các tiêu chí phát hành trên là đề xuất của kho, chưa phải kết quả chạy upstream.

## 7. Nguồn và cách cập nhật

Nguồn GitHub trong từng hồ sơ ghim full commit SHA đã clone; số sao và `archived` đọc bằng GitHub REST ngày 2/11/2026. Commit date là ngày của `HEAD` đã đọc, khác `pushed_at` (có thể là nhánh khác). README/CI là bằng chứng về thiết kế và định nghĩa kiểm, không phải kết quả thực thi tại kho này. Nguồn ngoài repo gồm các paper gốc ở §4; không dùng bài SEO để quyết định tính tương thích hay license.

Khi cập nhật: đọc lại license từng component, release/changelog, trainer/schema/template và đường save/load; giữ bằng chứng cấu hình cụ thể nếu báo tốc độ/VRAM; đối chiếu model card và rerun eval ở dự án tích hợp. Chỉ bổ sung con số benchmark khi có hardware, dataset/split, config, revision và giới hạn của phép đo.

<a id="anhkysuai-2026-11-23"></a>

## Đánh giá từ kho Anh Kỹ Sư AI — 23/11/2026

Phần này có **4 hồ sơ hoặc phạm vi đối chiếu** từ [nguồn tuyển chọn](https://anhkysuai.com/kho/). [Bảng đủ 1.295 repo](../data/collections/anhkysuai-kho.json) ghi trạng thái đối chiếu từng link; [danh sách URL](../data/collections/anhkysuai-kho-links.txt) phục vụ tra cứu. Nguồn tuyển chọn giúp phát hiện repo; đánh giá bên dưới dựa trên clone và permalink upstream cùng metadata GitHub ngày 2026-11-23.

Mức `docs-read`/`code-read` chỉ áp dụng phạm vi ghi tại mỗi hồ sơ. Chưa cài, build, chạy test hay benchmark mã upstream. Giấy phép có thể tách theo code, model, nội dung, asset hoặc bản enterprise; con số/tuyên bố của tác giả chưa được tái lập nếu không có ghi chú khác.

<a id="anhkysuai-2026-11-23-minimind"></a>

### MiniMind

**Repo:** [jingyaogong/minimind](https://github.com/jingyaogong/minimind) · **License:** Apache-2.0 · **★ 69,135 (GitHub API, 2026-11-23)**

**Mục đích:** Tài liệu và mã huấn luyện mô hình ngôn ngữ nhỏ từ đầu bằng PyTorch.

**Giá trị và cơ chế:** README trình bày chuỗi pretrain, SFT, LoRA, DPO và các biến thể học tăng cường; hữu ích để hiểu từng giai đoạn thay vì chỉ gọi framework mức cao.

**Giới hạn:** Con số hai giờ và chi phí ba nhân dân tệ chỉ là phép chạy SFT một epoch trên RTX 3090 theo tác giả, không phải chi phí huấn luyện toàn bộ. Quyền dữ liệu và weights phải kiểm riêng.

**Cách tham khảo/tích hợp:** Dùng làm bài học có cấu hình và seed cố định, tách dataset khỏi mã Apache-2.0.

**Thay thế:** nanogpt, [LitGPT](../25-model-adaptation-post-training/README.md#anhkysuai-2026-11-23-litgpt), llama-factory.

**Bằng chứng:** `docs-read`, ngày 2026-11-23, commit [`858008eb98da`](https://github.com/jingyaogong/minimind/commit/858008eb98da4428f78053a1cc4d3a3bd5973629). README và các tài liệu/manifest/CI hiện diện, đọc chọn lọc; chưa kiểm implementation. Chưa cài/chạy upstream.

**Nguồn:** [README.md](https://github.com/jingyaogong/minimind/blob/858008eb98da4428f78053a1cc4d3a3bd5973629/README.md) · [LICENSE](https://github.com/jingyaogong/minimind/blob/858008eb98da4428f78053a1cc4d3a3bd5973629/LICENSE) · [metadata GitHub](https://api.github.com/repos/jingyaogong/minimind).

<a id="anhkysuai-2026-11-23-jax"></a>

### JAX

**Repo:** [jax-ml/jax](https://github.com/jax-ml/jax) · **License:** Apache-2.0 · **★ 36,675 (GitHub API, 2026-11-23)**

**Mục đích:** Tính toán mảng và biến đổi chương trình Python hướng tới accelerator.

**Giá trị và cơ chế:** README giải thích tổ hợp grad và jit với XLA; hữu ích khi cần tự động vi phân và tối ưu hàm tính toán trong nghiên cứu mô hình.

**Giới hạn:** Tài liệu nêu rõ có sharp edges và đây là dự án nghiên cứu. Chưa biên dịch workload, đo thời gian compile hoặc kiểm độ chính xác số trên GPU/TPU.

**Cách tham khảo/tích hợp:** Giữ hàm tính toán thuần, xác định dtype và seed; so kết quả với baseline trước khi tối ưu thiết bị.

**Thay thế:** [pytorch](../08-awesome-lists-learning/README.md#6c513-mô-hình-ai--huấn-luyện), [tensorflow](../08-awesome-lists-learning/README.md#6c513-mô-hình-ai--huấn-luyện), numpy.

**Bằng chứng:** `docs-read`, ngày 2026-11-23, commit [`937af6e0b5a5`](https://github.com/jax-ml/jax/commit/937af6e0b5a507f28fd002ce693610627a7e2c2f). README và các tài liệu/manifest/CI hiện diện, đọc chọn lọc; chưa kiểm implementation. Chưa cài/chạy upstream.

**Nguồn:** [README.md](https://github.com/jax-ml/jax/blob/937af6e0b5a507f28fd002ce693610627a7e2c2f/README.md) · [LICENSE](https://github.com/jax-ml/jax/blob/937af6e0b5a507f28fd002ce693610627a7e2c2f/LICENSE) · [metadata GitHub](https://api.github.com/repos/jax-ml/jax).

<a id="anhkysuai-2026-11-23-hanlp"></a>

### HanLP

**Repo:** [hankcs/HanLP](https://github.com/hankcs/HanLP) · **License:** Apache-2.0 cho mã; models theo CC-BY-NC-SA-4.0 hoặc nghiên cứu/giảng dạy · **★ 36,542 (GitHub API, 2026-11-23)**

**Mục đích:** Toolkit NLP đa ngôn ngữ với các tác vụ phân tích và mô hình tiền huấn luyện.

**Giá trị và cơ chế:** README mô tả cả pipeline đơn tác vụ và đa tác vụ trên PyTorch/TensorFlow; thích hợp tham khảo xử lý ngôn ngữ với annotation có cấu trúc.

**Giới hạn:** Mã Apache-2.0 không làm weights được dùng tự do: README nêu models đa ngôn ngữ mặc định phi thương mại, models tiếng Trung chỉ nghiên cứu/giảng dạy. Chưa đo tiếng Việt hoặc kiểm checkpoint cụ thể.

**Cách tham khảo/tích hợp:** Chọn model theo ngôn ngữ/tác vụ và kiểm license checkpoint trước khi dùng thương mại.

**Thay thế:** [spaCy](../08-awesome-lists-learning/README.md#6c525-tài-liệu-ocr--thị-giác-máy-tính), stanza, [transformers](../08-awesome-lists-learning/README.md#6c513-mô-hình-ai--huấn-luyện).

**Bằng chứng:** `docs-read`, ngày 2026-11-23, commit [`959a6966f6e7`](https://github.com/hankcs/HanLP/commit/959a6966f6e7e26d2e89c4112ca9bafbe32eb743). README và các tài liệu/manifest/CI hiện diện, đọc chọn lọc; chưa kiểm implementation. Chưa cài/chạy upstream.

**Nguồn:** [README.md](https://github.com/hankcs/HanLP/blob/959a6966f6e7e26d2e89c4112ca9bafbe32eb743/README.md) · [LICENSE](https://github.com/hankcs/HanLP/blob/959a6966f6e7e26d2e89c4112ca9bafbe32eb743/LICENSE) · [metadata GitHub](https://api.github.com/repos/hankcs/HanLP).

<a id="anhkysuai-2026-11-23-litgpt"></a>

### LitGPT

**Repo:** [Lightning-AI/litgpt](https://github.com/Lightning-AI/litgpt) · **License:** Apache-2.0 cho mã; weights theo model · **★ 13,761 (GitHub API, 2026-11-23)**

**Mục đích:** Các triển khai LLM và recipe pretrain, fine-tune, chuyển đổi và phục vụ model.

**Giá trị và cơ chế:** README trình bày LoRA/QLoRA, adapter, phân tán FSDP cùng cấu hình trực tiếp; phù hợp người muốn hiểu mã huấn luyện và kiểm soát recipe.

**Giới hạn:** Không tải model hay chạy GPU trong đánh giá. Một số weights yêu cầu token/quyền riêng; số hiệu năng và quy mô hàng nghìn thiết bị chưa kiểm. CI CPU có thể bỏ test cần secret trên fork.

**Cách tham khảo/tích hợp:** Bắt đầu model nhỏ và dataset có quyền, lưu cấu hình/seed/checkpoint, xác minh format export trước dùng serving.

**Thay thế:** llama-factory, [Axolotl](../25-model-adaptation-post-training/README.md#axolotl), [MiniMind](../25-model-adaptation-post-training/README.md#anhkysuai-2026-11-23-minimind).

**Bằng chứng:** `docs-read`, ngày 2026-11-23, commit [`5341568a65e9`](https://github.com/Lightning-AI/litgpt/commit/5341568a65e918a85cb284fac038de2157eebf3f). README và các tài liệu/manifest/CI hiện diện, đọc chọn lọc; chưa kiểm implementation. Chưa cài/chạy upstream.

**Nguồn:** [README.md](https://github.com/Lightning-AI/litgpt/blob/5341568a65e918a85cb284fac038de2157eebf3f/README.md) · [LICENSE.md](https://github.com/Lightning-AI/litgpt/blob/5341568a65e918a85cb284fac038de2157eebf3f/LICENSE.md) · [metadata GitHub](https://api.github.com/repos/Lightning-AI/litgpt).

<a id="chuyen-muc-2026-11-23"></a>

## Hồ sơ chuyển về từ mục khác — 23/11/2026

1 hồ sơ được chuyển khi chia lại catalog theo `data/taxonomy.json`. Nội dung, ngày kiểm và mức bằng chứng giữ nguyên như ở mục gốc.

<a id="chuyen-datasets"></a>

### datasets

`huggingface/datasets` · License: Apache License 2.0 · ★ 22.154 · docs-read · 2026-11-18

Thư viện tải, chia sẻ và tiền xử lý tập dữ liệu (từ Hugging Face Hub hoặc file cục bộ) dựa trên Apache Arrow. Tải dữ liệu một dòng với load_dataset() và hỗ trợ streaming; lưu trữ ánh xạ bộ nhớ zero-copy qua Apache Arrow kèm cache tự động; chuyển đổi qua lại NumPy, Pandas, Polars, PyTorch, TensorFlow, JAX, Spark. Điều kiện: Mỗi tập dữ liệu trên Hub có giấy phép riêng do chủ dữ liệu quy định; README khuyên ghim revision để tái lập. ★ 18/11/2026: 22.154 (GitHub search API), nhóm "Tài liệu, OCR & Thị giác máy tính" trong kho-repo của Phan Đông Giang, mục 08 §6c.5

**Hồ sơ gốc:** [mục 08](../08-awesome-lists-learning/README.md#6c525-tài-liệu-ocr--thị-giác-máy-tính) (bảng/đoạn chung, giữ nguyên tại chỗ).
