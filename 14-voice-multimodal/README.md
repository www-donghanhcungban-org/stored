# 14 · Voice Agents, Speech & Multimodal (Vision, Image Generation)

> Agent giọng nói thời gian thực, STT/TTS mã mở, model thị giác-ngôn ngữ và công cụ sinh ảnh. Số sao ước lượng giữa–cuối 2026.

## 1. Framework voice agent realtime

| Dự án | Repo | License | ★ | Định vị | Ghi chú |
|---|---|---|---|---|---|
| **Pipecat** (Daily) | pipecat-ai/pipecat | BSD-2 | ~15–16k | Pipeline Python cho voice/multimodal agent | Mặc định tốt cho backend Python |
| **LiveKit Agents** | livekit/agents | Apache-2.0 (model turn-detection license riêng) | ~11–15k | WebRTC, telephony, nhiều client SDK | Cloud tùy chọn |
| **TEN Framework** | TEN-framework/ten-framework | Apache-2.0 | ~11k | Realtime multimodal agent, Agora | |
| Vocode | vocodedev/vocode-core | MIT | ~4k | Ngừng cập nhật cuối 2024 | Legacy |
| OpenAI Realtime API / Gemini Live / Anthropic voice | (đóng) | – | – | Speech-to-speech end-to-end | |
| Dograh, Vapi, Retell | – | – | – | Nền tảng thương mại | |

## 2. Speech-to-text (STT)

| Dự án | Repo | Ghi chú |
|---|---|---|
| **Whisper** | openai/whisper | Model STT mở phổ biến nhất (MIT) |
| **faster-whisper** | SYSTRAN/faster-whisper | CTranslate2, nhanh 4× |
| **whisper.cpp** | ggml-org/whisper.cpp | C/C++, edge/Apple Silicon |
| WhisperX, Deepgram/AssemblyAI (đóng) | – | Diarization / cloud |

## 3. Text-to-speech (TTS)

| Model | License | Thế mạnh | Hạn chế |
|---|---|---|---|
| **Kokoro (82M)** | Apache-2.0 | Nhẹ, nhanh, Elo ~1060 (8/2026) | Không clone giọng, voicepack cố định |
| **Chatterbox** (Resemble) | MIT | Zero-shot clone ~5s audio, 23 ngôn ngữ, Elo ~1020 | Watermark output |
| **F5-TTS** | Code MIT / weights CC-BY-NC | Clone chất lượng cao | Không thương mại hóa weights |
| **Audio8 TTS** 0.6B / 0.1B (Edge0) | 0.6B: Apache-2.0 · 0.1B: **Audio8 Community License** (trần doanh thu US$2M) | Clone zero-shot, 11 ngôn ngữ, ONNX INT4 chạy CPU ~1 GiB, adapter SGLang Omni; xem §3b | Preview, không watermark, chưa có đánh giá độc lập |
| **Fish Audio S2 Pro** | Fish Audio Research License (cấm thương mại nếu không có hợp đồng) | DualAR 4,6B, kiến trúc gốc mà Audio8 dựa theo | "Open weights, not open source" (chính Fish Audio nói) |
| CosyVoice3 (Alibaba), VoxCPM2 (OpenBMB), Higgs Audio v2 (Boson AI) | xem model card từng bản | Mốc so sánh trong bảng benchmark của Audio8 (1,5B / 2,3B / 4,7B) | License VoxCPM2/Higgs **chưa xác minh** trong kho |
| Fish Speech (bản cũ), Orpheus, Coqui XTTS (ngừng) | – | | |

### 3b. Case study: Audio8 TTS (Edge0-AI) – TTS clone giọng cỡ nhỏ (link từ người dùng, 2026-10-12)

> Nguồn: https://github.com/edge0-ai/audio8_tts. Đã clone đầy đủ lịch sử (73 commit): README, NOTICE, LICENSE, `audio8_tts_*.py`, `onnx_runtime*/`, `sglang_omni/`. Cùng với đó là model card Hugging Face (0.6B, 0.1B), các bản port của bên thứ ba và các bài viết bên ngoài.

| Thuộc tính | Giá trị (đọc 2026-10-12) |
|---|---|
| Repo / tên | `Edge0-AI/Audio8_TTS` (1,6k★, 161 fork, 8 issue + 1 PR mở). README vẫn trỏ badge và star-history về `Audio8-AI/Audio8_TTS`; trên Hugging Face, model nằm ở `Edge0/…`, `Audio8/…`, lệnh cài lại ghi `AutoArk-AI/…` → **3 tên tổ chức** cho cùng một dự án. Email commit thuộc domain `autoark.ai` |
| Tuổi | Commit đầu 27/7/2026, cuối 1/9/2026; 0.1B ra 19/8/2026 |
| Lịch sử commit | Một phần commit có tác giả `Your Name <you@example.com>`, `root@pytorch-training-…svc.cluster.local` và `Codex <codex@localhost>`; một PR huấn luyện 0.1B bị revert ngay trong ngày → quy trình phát hành còn non |
| Mã nguồn | ~2,6k dòng Python: infer, chuẩn bị codec, SFT (`torchrun`), runtime ONNX (CLI + web/HTTP + giọng đăng ký sẵn), adapter SGLang Omni (API `/v1/audio/speech` kiểu OpenAI, SSE streaming) |
| Kiến trúc | **DualAR** theo Fish Audio S2 Pro: slow AR 24 lớp (1 token ngữ nghĩa mỗi frame) + fast AR 4 lớp (10 codebook × 4.096); codec 44,1 kHz (~21,5 frame/s) đóng gói trong checkpoint; 601M tham số không kể codec. Bản 0.1B thay slow AR bằng **Falcon-H1** (lai Mamba2 + attention): main ~170M + codec decoder ~120M (HF ghi 0.2B) |
| Triển khai | GPU: SGLang Omni, RTF 0,116, p50 0,691 s trên 1×H20 (tác giả tự đo). CPU: ONNX INT4 ~1 GiB trên Apple M2. Cộng đồng đã port sang audio.cpp, Core AI (coreai-model-zoo #47) và có API trên DeepInfra |
| Benchmark (tự công bố) | Seed-TTS EN WER **1,506** (tốt nhất bảng), ZH CER 0,950; nhưng **SIM** (độ giống giọng) thấp nhất bảng (63,2 so với 72–75 của CosyVoice3/VoxCPM2), hard-ZH CER 11,5 kém hẳn CosyVoice3 (5,83). Tác giả tự ghi: normalizer khác nhau nên chỉ là "reference comparisons" |

**Mâu thuẫn và rủi ro**

- **License:** README và NOTICE ghi "Code and model weights in this repository are released under Apache 2.0", nhưng weights **0.1B** trên Hugging Face dùng *Audio8 Community License v1.0*: miễn phí cho phi thương mại và cho đơn vị doanh thu dưới **US$2M/năm** (tính cả công ty mẹ/con), trên mức đó phải mua license. Kiến trúc lấy cảm hứng từ Fish S2 Pro, mà weights Fish dùng Research License cấm thương mại. Audio8 chỉ ghi "inspired by"; kho chưa kiểm được codec bundled có nguồn gốc từ đâu **(chưa xác minh)**.
- **Lạm dụng:** clone giọng zero-shot nhưng **không có watermark**, chỉ khuyến nghị xin đồng ý và công bố là audio tổng hợp. Chatterbox (§3) watermark output; nên tự thêm watermark hoặc log nguồn khi đưa vào sản phẩm.
- **Chất lượng:** câu vào nên ≤150 ký tự; transcript tham chiếu phải khớp audio; Transformers 5.x sinh code toàn 0; một bài nghe thử không chính thức chê "okay, robotic"; bản port audio.cpp ghi đường clone 0.6B chưa được đánh giá bằng ASR.
- **Tiếng Việt: không hỗ trợ** (11 ngôn ngữ khuyến nghị không có vi). Cho tiếng Việt xem mục 18 (ViGen…).

**Bài học:** (1) tách **slow AR ngữ nghĩa / fast AR codebook** giúp model nhỏ vẫn đạt WER thấp, nhưng độ giống giọng (SIM) là thứ mất đi khi thu nhỏ → luôn đọc cả WER **lẫn** SIM; (2) gói kèm runtime ONNX INT4 + giọng đăng ký sẵn là mẫu tốt để chạy TTS offline trên CPU cho voice agent (Pipecat/LiveKit §1, Personal Jarvis mục 01 §3c); (3) kiểm tra license **theo từng checkpoint**, không theo README.

## 4. Vision-language model (VLM) mã mở

| Model | Repo | ★ | Ghi chú |
|---|---|---|---|
| **Qwen3-VL** (Alibaba) | QwenLM/Qwen3-VL | ~20k | Apache-2.0; 2B/7B, 72B sắp mở |
| LLaVA-NeXT / LLaVA-OneVision-2 | LLaVA-VL/LLaVA-NeXT · EvolvingLMMs-Lab/LLaVA-OneVision-2 | ~4.7k / ~1.2k | Framework huấn luyện mở (4/2026) |
| InternVL | OpenGVLab/InternVL | – | |
| Gemma 3 / Llama 4 / Pixtral | – | – | Open-weight đa phương thức |

## 5. Sinh ảnh / video

| Công cụ | Repo | ★ | Trạng thái |
|---|---|---|---|
| **ComfyUI** | comfyanonymous/ComfyUI | ~122–136k | Node-based, hỗ trợ model mới nhanh nhất (Flux, video); **đã thắng** |
| AUTOMATIC1111 WebUI | AUTOMATIC1111/stable-diffusion-webui | ~164k | Release cuối v1.10.1 (7/2024), dừng phát triển |
| Forge / Forge Neo | lllyasviel/stable-diffusion-webui-forge | – | Khuyến nghị thay A1111 |
| Fooocus | lllyasviel/Fooocus | ~53k | LTS, chỉ sửa lỗi |
| Flux (Black Forest Labs), SDXL, Wan/HunyuanVideo | – | – | Model |
| **Wan 2.2 / LTX-2** | Wan-Video/Wan2.2 · Lightricks/LTX-2 | – | Model video mở X-Studio chọn cho xưởng video (mục 23 §3.2); OpenMontage bundle Wan (mục 19) |

### 5b. 3D & tài liệu (từ repo của chủ kho, mục 23)

- **Ảnh/văn bản → 3D** (research `design-os-3d-blender`, 28/7/2026, gắn `[UNVERIFIED]`): Microsoft **TRELLIS.2** (MIT, PBR native), TripoSG/SR/SF, Direct3D-S2, Step1X-3D, **Hunyuan3D 2.1** (license hạn chế lãnh thổ EU/UK/KR, kể cả output), PartCrafter, HoloPart, **UniRig**/MagicArticulate (rigging); marketplace in 3D.
- **Agent điều khiển Blender**: `ahujasid/blender-mcp` (~24,6k★ theo docs nội bộ) hoặc headless `blender -b -P`; mẫu sentinel `AGENT_OK/AGENT_FAIL` + verify ladder rẻ→đắt (assert số → preview 0,2s → render) vì exit code của Blender sai cả hai chiều.
- **Scan tài liệu di động** (X-Scanner, Flutter): OpenCV edge detection + perspective warp, OCR on-device (ML Kit) — `docs/research/2026-10-11-scanner-product-suggestions.md`.

## 5c. Nâng cấp 31/10/2026: rà repo lớn

> Cách làm: đọc lại sao, license, trạng thái của 17 repo GitHub đã có trong mục 14 (GitHub API, 31/10/2026). Tìm repo còn thiếu bằng 12 truy vấn GitHub search (`text to speech`, `tts`, `speech recognition`, `voice agent`, topic `text-to-speech`/`speech-recognition`/`multimodal`, `vision language model`, `image generation`, `ocr`, và `created:>2025-10-01` cho repo mới). Lọc bỏ repo đã có trong `data/projects.json`, chọn **6 repo**, clone `--filter=blob:none` rồi đọc LICENSE, README, manifest, CI, file telemetry và host mạng trong mã. **Không cài, không chạy script của repo.** Số liệu đọc 31/10/2026.

### 5c.1 Trạng thái repo cũ

| Repo | Thay đổi | Hệ quả |
|---|---|---|
| `hexgrad/kokoro` | Push cuối **6/8/2025** (9,8k★) | Repo code đứng yên hơn 1 năm; model Kokoro-82M vẫn được dùng qua wrapper như `remsky/Kokoro-FastAPI` (5,6k★, push 31/10/2026) và backend của LocalAI |
| `QwenLM/Qwen3-VL` | Push cuối **30/1/2026** | Dòng "72B sắp mở" ở §4 không còn cập nhật; theo dõi model card Hugging Face thay vì repo |
| `AUTOMATIC1111/stable-diffusion-webui` | Push cuối 2/3/2026, 165,2k★ | Đúng như §5 ghi "dừng phát triển" |
| `lllyasviel/Fooocus` | Push cuối 1/12/2025 | Hết giai đoạn LTS trên thực tế |
| `black-forest-labs/flux2` | Push cuối 12/3/2026 (2,8k★) | Repo tham chiếu, ít cập nhật |
| `Comfy-Org/ComfyUI` | **144,4k★** (bảng §5 ghi ~122–136k, repo cũ `comfyanonymous/ComfyUI`) | Đã chuyển sang tổ chức Comfy-Org; cập nhật tên repo |
| `Edge0-AI/Audio8_TTS` | 1,6k → **2,1k** | Hồ sơ §3b vẫn đúng |
| `openai/whisper` · `ggml-org/whisper.cpp` · `SYSTRAN/faster-whisper` | 111,7k · 54,8k · 26,4k | Catalog bổ sung sao còn thiếu |
| `resemble-ai/chatterbox` | 27,5k, push cuối 21/7/2026 | Hơn 3 tháng không push |
| `TEN-framework/ten-framework` · `fishaudio/fish-speech` | GitHub báo `NOASSERTION` | Không đổi license: TEN có điều khoản bổ sung trên Apache-2.0 **(chưa xác minh)**, Fish dùng Research License (đã ghi §3) |
| VoxCPM2 (§3) | License "chưa xác minh" | Nay đã đọc: **Apache-2.0 cho cả code và weights** theo README và LICENSE của `OpenBMB/VoxCPM` (xem dưới) |

### 5c.2 Bảng nhanh 6 repo mới

| Repo | Nhóm | ★ · license | Commit cuối | Một dòng | Cờ |
|---|---|---|---|---|---|
| `debpalash/VoiceStudio` | App giọng nói | 96,8k · **AGPL-3.0 + CLA** | 1/11/2026 | Clone, thiết kế giọng, lồng tiếng video, đọc chính tả; desktop + mobile | Sao tăng bất thường; bán license thương mại |
| `jamiepine/voicebox` | App giọng nói | 59,1k · MIT | 7/10/2026 | "ElevenLabs + WisprFlow" chạy local, 8 engine TTS, MCP `voicebox_speak` | Bảo trì bằng agent Capy; không có bản Linux dựng sẵn |
| `microsoft/VibeVoice` | ASR + TTS | 55,1k · MIT | 8/10/2026 | ASR 60 phút một lượt (ai nói, lúc nào), streaming ASR, TTS realtime 0,5B | Code TTS dài từng bị gỡ vì lạm dụng; không CI |
| `RVC-Boss/GPT-SoVITS` | Clone giọng | 64,4k · MIT | 31/10/2026 | Huấn luyện TTS từ ~1 phút giọng, WebUI | Tag cuối 6/6/2025; nhịp chậm |
| `OpenBMB/VoxCPM` | TTS | 40,9k · Apache-2.0 | 8/10/2026 | VoxCPM2 2B, 30 ngôn ngữ **có tiếng Việt**, 48 kHz, thiết kế giọng | Benchmark tự công bố |
| `cjpais/Handy` | STT desktop | 35,9k · MIT | 27/10/2026 | Giữ phím, nói, chữ dán vào app đang mở; Whisper/Parakeet offline | Tải model từ `blob.handy.computer` |

### 5c.3 Hồ sơ ngắn

- **VoiceStudio.** Repo tạo 10/4/2026; trong ~7 tháng có 6.378 commit, 155 tác giả, **40% commit có trailer Claude**, 96,8k★: tốc độ tăng sao này cao bất thường so với mọi repo TTS khác trong đợt **(chưa xác minh nguồn sao)**. Biến môi trường còn tên cũ `OMNIVOICE_*`, submodule `omnivoice-gallery`. `LICENSE-NOTICE.md`: AGPL-3.0, người đóng góp ký CLA trao quyền cho Yupcha Softwares Private Limited, công ty bán license thương mại và bản Pro. Telemetry PostHog có trong mã (`backend/core/analytics.py`), **tắt mặc định**, chỉ gửi trường trong allowlist, không gửi traceback ✅; tắt cứng bằng `OMNIVOICE_ANALYTICS_DISABLED=1`. Có workflow `scam-guard` tự xoá các bình luận dụ dán lệnh `irm … | iex` trong issue. Cài theo README là `curl -fsSL https://voicestudio.sh/install | sh` (chạy script từ xa).
- **Voicebox.** Tauri + Python backend, 813 commit từ 25/1/2026, tag cuối v0.5.0 (25/4/2026). README ghi dự án được "Capy Captain" (agent của capy.ai, nhà tài trợ) điều phối hằng ngày: một repo lớn bảo trì chủ yếu bằng agent. 8 engine TTS (Qwen3-TTS, LuxTTS, Chatterbox, HumeAI TADA, Kokoro…), Whisper cho đọc chính tả, MCP server cho agent nói bằng giọng đã clone. Có `RESPONSIBLE_USE.md` nhưng không có watermark trong mã **(chưa xác minh hết engine)**. Cài: tải DMG/MSI hoặc `docker compose up`.
- **VibeVoice (Microsoft).** 161 commit, không có workflow CI. Ghi chú 5/9/2025 trong README: code TTS dài (1,5B) bị **gỡ vì bị dùng sai mục đích**, Playground để "Disabled". Từ 2026 dự án chuyển sang ASR: VibeVoice-ASR 7B (60 phút một lượt, hơn 50 ngôn ngữ, hotword), bản streaming (9/2026), bản BitNet chạy CPU qua `microsoft/VibeASR.cpp`. Commit 7/10/2026 "Remove remote audio URL fetching from streaming ASR" bỏ khả năng tải URL từ xa. Cài: `pip install -e .` từ clone hoặc qua Transformers (`microsoft/VibeVoice-ASR-HF`).
- **GPT-SoVITS.** 1.066 commit, MIT, chủ yếu một tác giả (621 commit). Bản mới nhất v2Pro (6/6/2025); chỉ 20 commit từ 1/7/2026. `install.sh` tải model từ Hugging Face hoặc ModelScope; README hỗ trợ zh/en/ja/ko/yue, **không có tiếng Việt**. Không có CI kiểm thử, chỉ build Windows và Docker. Cài: `bash install.sh --device CU128 --source HF`.
- **VoxCPM (OpenBMB).** 182 commit, Apache-2.0; README nói rõ **weights và code đều Apache-2.0, dùng thương mại được** ✅ (khác Fish S2 Pro, F5-TTS weights ở §3). VoxCPM2: 2B, 30 ngôn ngữ trong đó có tiếng Việt, 48 kHz, voice design. Bảng benchmark là tự đo. Phục vụ nhanh qua `nano-vllm-voxcpm`. Đây là ứng viên TTS clone giọng tiếng Việt có license thoáng nhất trong kho, nên đánh giá cùng mục 18 (VieNeu-TTS). Cài: `pip install voxcpm`.
- **Handy.** Tauri (Rust + React), 902 commit, 178 tác giả, 9 workflow (có Playwright). STT hoàn toàn offline sau khi tải model (Whisper, Parakeet V3), VAD Silero. Mạng: model tải từ `blob.handy.computer`, cập nhật từ GitHub Releases; xử lý hậu kỳ bằng LLM là tuỳ chọn và gọi OpenAI/OpenRouter. Không thấy telemetry. Cài: `brew install --cask handy` (cask cộng đồng) hoặc tải từ Releases.

Đã cân nhắc nhưng chưa thêm: `k2-fsa/OmniVoice` (16,1k, TTS 600+ ngôn ngữ, tạo 3/2026), `index-tts/index-tts` (24,8k, `NOASSERTION`), `m-bain/whisperX` (25,0k), `modelscope/FunASR` (20,9k), `k2-fsa/sherpa-onnx` (15,6k), `KittenML/KittenTTS` (16,7k), `kyutai-labs/pocket-tts` (10,2k), `QwenLM/Qwen3-TTS` (14,1k, push cuối 17/3/2026), `livekit/livekit` (22,0k), `supertone-oss-archive/supertonic` (13,8k, **đã archive**).

### 5c.4 Mẫu chung rút ra

1. **Weights mới là chỗ quyết định license.** VoxCPM ghi rõ weights Apache-2.0; ngược lại F5-TTS, Fish, Audio8 0.1B (§3, §3b) tách license weights. Luôn kiểm model card từng checkpoint.
2. **Clone giọng kéo theo trách nhiệm**: Microsoft gỡ hẳn code TTS; Voicebox, VoiceStudio chỉ có văn bản "responsible use". Sản phẩm dùng clone giọng nên tự thêm watermark hoặc nhật ký nguồn.
3. **App voice local vẫn có đường mạng**: tải model từ CDN riêng (Handy), PostHog tuỳ chọn (VoiceStudio), LLM cloud cho hậu kỳ (Handy, Voicebox). Telemetry tắt mặc định kèm allowlist trường như VoiceStudio là mẫu tốt.
4. **Repo lớn được bảo trì bằng agent** đã thành phổ biến (VoiceStudio 40% commit có Claude, Voicebox do Capy điều phối). Số commit cao không còn là thước đo công sức con người.
5. **Cài bằng `curl … | sh`** vẫn là đường chính ở app desktop (VoiceStudio); scam-guard của VoiceStudio cho thấy lệnh dán vào shell cũng là kênh phát tán malware.

**Nguồn §5c:** GitHub search API 31/10/2026 (12 truy vấn + `repo:` cho 17 repo cũ và 6 repo mới) · clone `--filter=blob:none`, đọc: VoiceStudio (LICENSE, LICENSE-NOTICE.md, README.md, backend/core/analytics.py, .gitmodules, .github/workflows/scam-guard.yml), voicebox (LICENSE, README.md, RESPONSIBLE_USE.md, backend/, app/src/), VibeVoice (LICENSE, README.md, lịch sử commit), GPT-SoVITS (LICENSE, README.md, install.sh), VoxCPM (LICENSE, README.md, pyproject.toml), Handy (LICENSE, README.md, src-tauri/src/, src-tauri/tauri.conf.json) · https://github.com/debpalash/VoiceStudio · https://github.com/jamiepine/voicebox · https://github.com/microsoft/VibeVoice · https://github.com/RVC-Boss/GPT-SoVITS · https://github.com/OpenBMB/VoxCPM · https://github.com/cjpais/Handy · https://huggingface.co/openbmb/VoxCPM2

## 5d. Nâng trần 2/11/2026: đo chất lượng giọng nói (WER, MOS, eval voice agent) và watermark (yêu cầu người dùng)

> Mục 14 đã có framework, model STT/TTS và app giọng nói, nhưng chưa có công cụ nào để **đo** chúng. Đợt này thêm lớp đo và lớp gắn nhãn đầu ra. Số liệu đọc bằng GitHub search API ngày 2/11/2026. Clone `--depth 1 --filter=blob:none` 7 repo, đọc LICENSE, README, `pyproject.toml`, `.env.example` và file chính. **Không cài, không chạy.**

### 5d.1 Trần hiện tại

- Chọn model theo **benchmark tự công bố**: Elo của Kokoro/Chatterbox (§3), bảng của Audio8 (§3b), VoxCPM (§5c). Kho chưa có công cụ nào để dự án tự đo lại trên dữ liệu của mình, nhất là tiếng Việt.
- STT chưa có cổng **WER/CER**, TTS chưa có điểm **MOS** tự động, voice agent (Pipecat, LiveKit §1) chưa có eval hội thoại nhiều lượt.
- §5c.4 khuyên "tự thêm watermark" cho clone giọng nhưng chưa chỉ công cụ nào. Chỉ Chatterbox có watermark sẵn (§3).

### 5d.2 Bảng repo mới

| Repo | Lớp | ★ · license (2/11/2026) | Commit cuối | Vì sao nâng trần | Rủi ro |
|---|---|---|---|---|---|
| `jitsi/jiwer` | Cổng máy (STT) | 942 · Apache-2.0 | 16/4/2026 | Thư viện Python chuẩn để tính WER, MER, WIL, WIP, CER bằng RapidFuzz; v4.0.0. Đủ nhỏ để chạy trong CI trên bộ audio mẫu của dự án | Kết quả phụ thuộc bước chuẩn hoá văn bản (dấu, số, viết hoa). Với tiếng Việt phải tự định nghĩa và ghi rõ chuẩn hoá thanh điệu và số |
| `huggingface/open_asr_leaderboard` | Chuẩn đo (ASR) | 278 · Apache-2.0 | 30/10/2026 | Mã của Open ASR Leaderboard: bộ test công khai (short-form, long-form, multilingual FLEURS/MCV/MLS), chạy trên Hugging Face Jobs cùng phần cứng để tái lập, có cả tập riêng tư. Là thước đo trung lập để so Whisper, Parakeet, VibeVoice-ASR | Normalizer chủ yếu cho tiếng Anh (`EnglishTextNormalizer`); với nhánh multilingual dùng `BasicMultilingualTextNormalizer`. Kết quả tiếng Việt **(chưa xác minh có công bố)** |
| `Picovoice/speech-to-text-benchmark` | Cổng máy (STT) | 698 · Apache-2.0 | 7/10/2026 | Khung nhỏ đo WER và độ trễ trên LibriSpeech, TED-LIUM, Common Voice, MLS, VoxPopuli, FLEURS…; có engine Whisper, whisper.cpp streaming, Moonshine, Vosk, Nemotron cùng các API cloud | **Benchmark của nhà bán**: có engine Cheetah/Leopard của chính Picovoice. Dùng khung đo, đừng dùng bảng kết quả |
| `sarulab-speech/UTMOSv2` | Cổng máy (TTS) | 377 · MIT | 2/4/2026 | Dự đoán MOS độ tự nhiên, hạng 1 ở 7/16 chỉ số của VoiceMOS Challenge 2024 Track 1 (SLT 2024). Dùng để chặn hồi quy chất lượng TTS khi đổi model hay voicepack | Huấn luyện cho giọng tổng hợp chất lượng cao, phần lớn tiếng Anh/Nhật. Với tiếng Việt chỉ nên so tương đối giữa hai phiên bản, không coi là điểm tuyệt đối **(chưa xác minh)** |
| `ServiceNow/eva` | Cổng máy (voice agent) | 235 · MIT | 29/10/2026 | Eval hội thoại nói nhiều lượt theo kiểu bot đối thoại với bot: **EVA-A** (làm đúng việc) và **EVA-X** (tự nhiên, ngắn, hợp hội thoại nói). 213 kịch bản doanh nghiệp, bộ nhiễu (tiếng ồn, giọng vùng miền, mạng chập chờn), kết quả cho 12 hệ thống | Cần key ElevenLabs/OpenAI/Google/AWS cho người dùng giả và giám khảo LLM, nên tốn phí. Kịch bản tiếng Anh |
| `OpenBMB/UltraEval-Audio` | Cổng máy (tổng hợp) | 328 · Apache-2.0 | 28/10/2026 | Gom 34 benchmark (giọng nói, âm thanh, y tế, âm nhạc; 10 ngôn ngữ) cho cả hiểu và sinh giọng, kèm lệnh tái lập kết quả của các model phổ biến (ACL 2026 demo) | Khung lớn, tự cài phụ thuộc riêng cho từng model. README đủ tiếng Anh, có bản tiếng Trung |
| `facebookresearch/audioseal` | Đầu bảng (watermark) | 802 · MIT (cả weights từ 4/2024) | 2/11/2026 | Watermark âm thanh theo từng đoạn: dò được vị trí đoạn bị chèn, chạy streaming từ v0.2. Đã nằm trong **danh sách soft-binding của C2PA** (`com.aiwatermark.audioseal.1`, xem mục 19 §3d) | Watermark có thể bị tấn công gỡ. Chỉ là một lớp, phải đi kèm manifest C2PA |

**Đã xem nhưng không thêm:** `SpeechColab/Leaderboard` (558★, không có LICENSE, push cuối 3/2025) · `tarepan/SpeechMOS` (368★, MIT, đứng yên từ 10/2023) · `boson-ai/EmergentTTS-Eval-public` (237★, Apache-2.0, push cuối 12/2025).

### 5d.3 Stack nâng trần

1. **Cổng WER/CER cho STT (nửa ngày).** Chuẩn bị 50–200 câu audio tiếng Việt thật của sản phẩm kèm transcript chuẩn. Tính bằng `jiwer` sau một bước chuẩn hoá cố định, chặn PR khi WER tăng quá ngưỡng. Áp cho Whisper, faster-whisper (§2), PhoWhisper (mục 18) và VibeVoice-ASR (§5c).
2. **So model bằng khung trung lập (1 ngày).** Dùng harness của Open ASR Leaderboard hoặc Picovoice với dữ liệu của mình. Không tin bảng số của nhà bán, kể cả bảng của Picovoice.
3. **MOS tự động cho TTS (1 ngày).** Chấm UTMOSv2 trên bộ câu cố định mỗi khi đổi model hay giọng (Kokoro, VoxCPM2, VieNeu…). Chỉ so tương đối, và định kỳ cho người nghe thật duyệt lại.
4. **Eval voice agent (2–3 ngày).** Chạy EVA (EVA-A/EVA-X và bộ nhiễu) cho agent dựng bằng Pipecat hoặc LiveKit (§1) trước khi lên production. Tự viết kịch bản tiếng Việt theo cùng khung.
5. **Gắn nhãn giọng clone.** Chèn AudioSeal vào đầu ra TTS clone giọng (VoxCPM, GPT-SoVITS, Voicebox ở §5c), ký manifest C2PA (mục 19 §3d), lưu nhật ký người đồng ý cho giọng.

**Nguồn §5d:** GitHub search API 2/11/2026 (`repo:` cho 7 repo; 6 truy vấn `word error rate`, `MOS prediction`, `TTS evaluation`, `ASR benchmark leaderboard`, `voice agent evaluation`, `audioseal OR videoseal`) · clone `--depth 1 --filter=blob:none` 2/11/2026: jitsi/jiwer (HEAD 2227002, 16/4/2026; README.md, LICENSE, pyproject.toml), huggingface/open_asr_leaderboard (edd6842, 30/10/2026; README.md, LICENSE, normalizer/normalizer.py), Picovoice/speech-to-text-benchmark (aea7914, 7/10/2026; README.md, LICENSE, engine.py), sarulab-speech/UTMOSv2 (cc2700d, 2/4/2026; README.md, LICENSE), ServiceNow/eva (236f4ea, 29/10/2026; README.md, LICENSE, .env.example), OpenBMB/UltraEval-Audio (c0be484, 28/10/2026; README.md, LICENSE), facebookresearch/audioseal (98f56cd, 2/11/2026; README.md, LICENSE) · danh sách soft-binding C2PA: github.com/c2pa-org/specifications `softbinding-alg-list/softbinding-algorithm-list.json` (HEAD 66ee450)

## 5e. Voice reliability

> Mở rộng khảo sát ngày 2/11/2026. §5d đã đo WER/MOS và tác vụ hội thoại; phần này đánh giá **đường truyền, lượt nói và quyền thu âm**. Đọc LICENSE, CI và mã nguồn tại commit ghim dưới đây; không cài hay chạy mã ngoài. Các ngưỡng vận hành phải lấy từ yêu cầu của sản phẩm, chưa có kết quả chạy tiếng Việt trong khảo sát này.

### 5e.1 Hai thành phần dưới framework

| Repo | ★ · license (2/11/2026) | Commit đọc | Cơ chế đáng học | Giới hạn / điều kiện |
|---|---|---|---|---|
| [snakers4/silero-vad](https://github.com/snakers4/silero-vad/tree/066409f3d9db45a30d21dfcbf9147826ffdd7052) | 10,581 · MIT | 2026-10-22 · `066409f` | VAD để tách đoạn tiếng nói trước STT, có ONNX/TorchScript và trạng thái streaming | VAD không xác định người nói, không đo hiểu đúng ý hay sự đồng ý; cần kiểm tiếng ồn/giọng vùng miền trên dữ liệu đích |
| [aiortc/aiortc](https://github.com/aiortc/aiortc/tree/d6a003fcb6511675318b4494e5b225b78abd2af2) | 5,124 · BSD-3-Clause | 2026-11-01 · `d6a003f` | WebRTC/ORTC Python asyncio, media track, RTP/RTCP và data channel | Là transport thấp tầng; không cung cấp sẵn signaling production, quản lý lượt nói hay chính sách lưu âm thanh |

**Silero VAD (Silero Team).** [Mã wrapper ONNX](https://github.com/snakers4/silero-vad/blob/066409f3d9db45a30d21dfcbf9147826ffdd7052/src/silero_vad/utils_vad.py) quy định khung 512 mẫu ở 16 kHz và 256 mẫu ở 8 kHz, có `reset_states()` khi cấu hình stream đổi. Vì vậy không dùng chung trạng thái model giữa các phiên độc lập nếu wrapper đang giữ state. README có đường cài qua Torch Hub; triển khai cần ghim revision và checksum model. So với WebRTC VAD hoặc VAD sẵn trong Pipecat/LiveKit (§1), Silero là lựa chọn model có thể tách riêng để thử cùng một audio corpus; chưa có phép đo chung trong khảo sát này.

**aiortc (Jeremy Lainé và cộng đồng).** [RTCPeerConnection](https://github.com/aiortc/aiortc/blob/d6a003fcb6511675318b4494e5b225b78abd2af2/src/aiortc/rtcpeerconnection.py) cung cấp trạng thái kết nối và `close()` để dọn sender/receiver/transport. [CI upstream](https://github.com/aiortc/aiortc/blob/d6a003fcb6511675318b4494e5b225b78abd2af2/.github/workflows/tests.yml) có test nhưng khảo sát này không chạy và không suy ra chất lượng mạng production. Chọn aiortc khi cần kiểm soát transport Python; chọn Pipecat khi muốn pipeline processor, LiveKit khi cần room/participant và hạ tầng realtime đã đóng gói. Không tự thay framework hoàn chỉnh bằng một thư viện transport chỉ vì API nhỏ hơn.

### 5e.2 Ma trận lỗi cần đo riêng

| Ranh giới | Tình huống kiểm | Bằng chứng phải lưu |
|---|---|---|
| Thu âm → VAD | Im lặng, nhạc/ồn, nói nhỏ, giọng Bắc/Trung/Nam, ngắt giữa câu | False start, bỏ mất tiếng đầu/cuối, thời gian chốt lượt; phiên bản VAD và normalizer |
| STT → LLM → TTS | Cùng câu hỏi bằng transcript chuẩn và bằng audio | Chênh lệch hoàn thành tác vụ; WER thấp vẫn có thể sai số tiền/tên riêng |
| Lượt nói | Người dùng chen ngang khi TTS phát và khi tool đang chạy | Thời gian tới lúc ngừng audio, không phát tiếp đoạn TTS cũ; hủy audio không mặc nhiên hủy tác vụ ghi |
| Transport | Mất mạng, reconnect, gói tới chậm/lặp, đóng tab | Session/turn ID, thứ tự sự kiện, dọn tài nguyên; tool có side effect dùng khóa chống chạy trùng |
| Quyền và dữ liệu | Từ chối/rút quyền microphone, bật/tắt ghi âm, xoá phiên | Trạng thái UI khớp capture thật; thời hạn lưu, nơi gửi audio, quyền tái dùng giọng tách khỏi quyền microphone |

**Chuẩn gốc:** [Media Capture and Streams của W3C](https://www.w3.org/TR/2025/CRD-mediacapture-streams-20251009/) yêu cầu xin quyền và chỉ báo capture; đây không phải bằng chứng người dùng đã đồng ý lưu lâu dài hay clone giọng. [SEA-HELM Audio](https://arxiv.org/abs/2610.19869) (preprint, 10/2026) minh họa phép đo chênh lệch text→speech, nhưng năm ngôn ngữ trong abstract **không có tiếng Việt**; không chuyển số điểm của paper thành kết quả tiếng Việt.

### 5e.3 Stack và cổng phát hành

1. Chốt policy microphone/recording/clone giọng; đưa lý do và khả năng rút quyền vào giao diện, giữ audio thô tách khỏi trace ứng dụng.
2. Ghim transport + VAD + STT/TTS/model revision; đo từng đoạn `end_of_user_speech → transcript_final → first_llm_token → first_audio` và toàn tuyến bằng p50/p95, không cộng trung bình để suy ra p95.
3. Kết hợp WER/CER (§5d) với độ đúng các trường quan trọng, lượt nói và kết quả tool; tách phiên bị lỗi mạng khỏi câu trả lời sai.
4. Thử interruption/reconnect bằng dữ liệu có đồng ý; tác vụ ghi chỉ xác nhận một lần qua executor (mục 03/21), không replay tool chỉ vì phải phát lại audio.
5. Gắn metadata nguồn giọng/watermark khi phù hợp (§5d và mục 19); watermark không thay hồ sơ quyền sử dụng giọng.

**Nguồn §5e:** GitHub metadata/HEAD 2/11/2026 và các permalink trên; clone chỉ đọc LICENSE, README, CI, `utils_vad.py`, `rtcpeerconnection.py`; W3C Media Capture and Streams; SEA-HELM Audio (preprint). Không có benchmark chạy mới.

## 5f. Hồ sơ kornia/kornia: thư viện thị giác máy tính khả vi trên PyTorch, đang chuyển sang làm đặc tả thực thi được (ảnh README người dùng gửi, đọc mã 3/11/2026)

> Ảnh là phần đầu README: logo Kornia "Open Source and Computer Vision, Powered by PyTorch"; badge pypi 0.9.0, downloads 120M, G-Star 98, license Apache 2.0; khối "Direction" (reference implementation và executable specification); mục "When to use Kornia" (1.200+ operator, tham số theo lô, minimal solver và RANSAC theo lô). Đã clone `--filter=blob:none` đủ lịch sử, HEAD `a733fe3b6248652b0a509d002cf452b2167965f0` (2/11/2026). **Không cài, không chạy test.**

### 5f.1 Kiểm ảnh

| Ô trong ảnh | Kết quả | Đối chiếu (3/11/2026) |
|---|---|---|
| "pypi package 0.9.0" | ✅ | PyPI `kornia` 0.9.0, Python ≥ 3.11; phụ thuộc `torch>=2.5.1`, `numpy`, `kornia_rs` (phần Rust). `main` đang là `0.9.1.dev` |
| "license Apache 2.0" | ✅ | `LICENSE` Apache-2.0, cộng thêm file `COPYRIGHT` |
| "downloads 120M" | ⚠️ khó kiểm | Có vẻ là tổng tích lũy. pypistats (không tính mirror) cho **2,18 triệu/tháng**; `ROADMAP.md` tự ghi "~3M downloads/month" |
| "1,200+ public operators" | ⚠️ chưa xác minh | Đếm `__all__` trong các `__init__.py` được **712 tên**. Đây là cận dưới, vì không phải module con nào cũng khai `__all__`. Con số 1.200 có thể tính cả lớp augmentation, model và alias |
| "From Kornia 0.9.1, a `sigma` tensor … validated on the device" | ⚠️ chưa phát hành | README trên `main` đang mô tả bản 0.9.1 chưa ra. Người dùng 0.9.0 chưa có hành vi này |
| ★ | ✅ | 12.188★, 1.494 fork, 144 issue+PR mở (GitHub search API) |

### 5f.2 Điều đáng học (đọc mã)

- **"Đặc tả thực thi được" thay vì thêm API.** `ROADMAP.md` (23/10/2026) nói rõ lỗi nguy hiểm nhất của mã hình học là sai **quy ước**: `align_corners`, tâm hay góc pixel, (x,y) hay (row,col), tọa độ chuẩn hóa hay pixel, chiều quay, chuẩn hóa homography. Code vẫn chạy nhưng sai về toán, và "this is exactly the error class LLMs reproduce". Lộ trình ba bước: **ghi rõ** (mỗi op có khối Convention trong docs và test `test_convention_*`; hiện có **1.413 test** như vậy) → **sửa và deprecate trong một cửa sổ chung** → **đóng băng** một tập "Tier A" có bảo đảm autograd, gradcheck, compile, dtype/device. Tier A **mới là đề xuất**, chưa áp dụng.
- **Conformance corpus** (dự kiến): bộ vector vàng trung lập với framework, kèm tolerance và metadata quy ước, để các port sang JAX, Rust/Triton, bản vendor **và mã do LLM sinh ra** có thể tự kiểm. Đây là mẫu tốt cho mọi thư viện có lỗi khó thấy.
- **Chính sách AI rõ ràng**: `AI_POLICY.md` và `CONTRIBUTING.md` không phân loại đóng góp theo mức dùng AI, chỉ yêu cầu nói rõ AI đã giúp gì và "care". Từ 1/8/2026 có 1.456 commit, trong đó **999 có trailer Co-Authored-By Claude**. Maintainer chính Dmytro Mishkin có 431 commit trong kỳ. Repo có `AGENTS.md` và `CLAUDE.md`. PR im lặng 15 ngày bị gắn nhãn stale nhưng **không bị đóng**.
- **Phát hành**: `pypi-release.yml` dùng trusted publishing (`id-token: write`, `pypa/gh-action-pypi-publish@release/v1`). ROADMAP ghi đã đối chiếu wheel PyPI với bản build trong CI. Tuy vậy PyPI **không có provenance** cho `kornia-0.9.0-py3-none-any.whl`. CI có workflow riêng cho typecheck, import-surface, test gói PyPI định kỳ, upstream probe và tutorial. Action **ghim theo tag** (`actions/checkout@v7`, `setup-pixi@v0.11.2`), không theo SHA.
- Không thấy telemetry (grep `telemetry|posthog|sentry_sdk` trong `kornia/`).

### 5f.3 Rủi ro và cách dùng

- Phiên bản 0.x, và lộ trình đã báo trước một **cửa sổ sửa quy ước** (box, camera, augmentation) có cảnh báo deprecation ít nhất một bản minor. Ghim phiên bản; đọc trang "Conventions & Pitfalls" và "stability policy" trước khi nâng.
- Ảnh và tham số phải là float trong `[0, 1]`. Đầu vào số nguyên không được hỗ trợ theo `CONTRIBUTING.md`.
- **Với agent viết mã thị giác**: bắt agent trích dẫn khối Convention của op đang dùng, và tái dùng test `test_convention_*` của Kornia làm cổng kiểm trước khi tin hàm hình học tự viết.

| Thư viện | ★ (3/11) | License | Khác Kornia |
|---|---|---|---|
| **kornia/kornia** | 12k | Apache-2.0 | Khả vi, chạy theo lô trên GPU; hình học epipolar, camera, RANSAC; đang xây đặc tả |
| `pytorch/vision` (torchvision) | – | BSD-3-Clause | Transform cơ bản (resize, crop, flip, jitter); mỗi lần gọi một tham số **(theo README Kornia)** |
| OpenCV | – | Apache-2.0 | Rộng nhất nhưng chạy trên CPU hoặc CUDA riêng, không khả vi |
| `albumentations` | – | MIT (bản gốc) | Augmentation trên CPU bằng numpy **(không đọc mã)** |

**Nguồn §5f:** ảnh README người dùng gửi 3/11/2026 · clone https://github.com/kornia/kornia HEAD `a733fe3b6248652b0a509d002cf452b2167965f0` (README.md, ROADMAP.md, AI_POLICY.md, CONTRIBUTING.md, LICENSE, pyproject.toml, `.github/workflows/{pypi-release,tests}.yml`; đếm `def test_convention_`, `gradcheck`, `__all__`; `git shortlog --since=2026-08-01`) · https://pypi.org/pypi/kornia/json · PyPI integrity API (0.9.0: không có provenance) · https://pypistats.org/api/packages/kornia/recent (2.176.424/tháng) · GitHub search API `repo:kornia/kornia` 3/11/2026.

## 5g. Nâng sâu 4/11/2026: từ ghi âm yêu cầu đến transcript kiểm chứng được

**Trần hiện tại:** mục này đã có ASR/TTS, đo WER và voice reliability. Với xưởng phần mềm, ghi âm phỏng vấn khách hàng, dựng phụ đề demo và voice UI cần thêm provenance của transcript, timestamp, speaker và quyền dữ liệu. Transcript do ASR không tự thành yêu cầu đã được khách hàng xác nhận; tóm tắt phải dẫn về đoạn ghi âm và giữ phần không nghe rõ.

<a id="factory-2026-11-04-whisperx"></a>

### WhisperX: forced alignment và diarization là các bước có lỗi riêng

| Thuộc tính | Kết quả đọc |
|---|---|
| Repo · SHA | `m-bain/whisperX` · `5d3678b8535698a2826a5db9eb3e4105aef85dd9` |
| License | Code BSD-2-Clause; weights ASR, alignment và diarization có license/điều kiện riêng. Không suy BSD của wrapper sang tất cả model |
| Đường xử lý | `whisperx/transcribe.py`: ASR → alignment nếu không tắt → diarization nếu bật → gán speaker theo word → writer. `alignment.py` có model mặc định theo ngôn ngữ, gồm tiếng Việt |
| Phụ thuộc | `DiarizationPipeline` tải `pyannote/speaker-diarization-community-1` qua `Pipeline.from_pretrained`, có tham số token/cache; README yêu cầu chấp nhận điều khoản model. Tải model/cache không chứng minh audio đã rời máy; cũng không được suy toàn bộ pipeline offline khi chưa kiểm egress |
| Giới hạn | README tự nêu speech chồng lấn xử lý kém, diarization không hoàn hảo, từ ngoài dictionary alignment có thể thiếu timing. Nhãn SPEAKER không xác thực danh tính con người |
| CI | `.github/workflows/tests.yml` dùng uv chạy pytest theo ma trận Python; chưa chạy inference, đo WER hay GPU trong đợt này |

**Phạm vi kiểm (2026-11-04):** đọc tài liệu, LICENSE, mã đường gọi và workflow tại SHA dưới đây; không cài/chạy upstream. Các cổng nghiệm thu là đề xuất cho repo tích hợp, chưa phải kết quả chạy của kho. Số sao không thu thập trong đợt này.

| Lựa chọn | Vai trò | Điều kiện lựa chọn |
|---|---|---|
| Whisper / faster-whisper | ASR văn bản/segment; faster-whisper dùng CTranslate2 | Baseline cho chất lượng, latency và bộ nhớ cùng model/corpus |
| whisper.cpp | ASR tối ưu triển khai cục bộ theo nền tảng | Kiểm feature/model format/hardware trên thiết bị đích |
| WhisperX | Ghép ASR với alignment và speaker diarization | Cần phụ đề có word timing hoặc phân đoạn hội thoại; chấp nhận thêm model và lỗi ghép |
| LiveKit / Pipecat | Pipeline voice tương tác theo thời gian thực | Đo barge-in, timeout, mất gói, khôi phục kết nối; không thay bộ chép lời batch |

**Stack cho xưởng:** ghi nhận quyền thu âm và mục đích → mã hóa/giới hạn lưu giữ → chốt audio hash và model revisions → ASR/align/diarize → người nghe kiểm lại đoạn có giá trị pháp lý/nghiệp vụ → liên kết yêu cầu/ADR tới timestamp → xóa dữ liệu theo policy. Nếu cần bí mật, prefetch model qua đường được phép rồi kiểm pipeline trong môi trường egress bị chặn; đo thay vì tin nhãn local.

**Cổng nghiệm thu:** corpus tách tiếng Việt vùng miền, code-switching, số tiền/tên riêng, nhiễu và nhiều người nói; đo WER/CER cùng lỗi entity quan trọng, sai số timestamp và speaker attribution. Fixture audio im lặng, quá ngắn, không có speech, chồng lấn phải có trạng thái rõ, không sinh transcript bịa thành yêu cầu. Chỉ xuất artifact đã lọc PII theo scope; review thủ công các quyết định quan trọng. Benchmark tốc độ quảng cáo upstream chưa được tái lập tại kho.

**Nguồn §5g:** [LICENSE](https://github.com/m-bain/whisperX/blob/5d3678b8535698a2826a5db9eb3e4105aef85dd9/LICENSE) · [README/limits](https://github.com/m-bain/whisperX/blob/5d3678b8535698a2826a5db9eb3e4105aef85dd9/README.md) · [pipeline callsite](https://github.com/m-bain/whisperX/blob/5d3678b8535698a2826a5db9eb3e4105aef85dd9/whisperx/transcribe.py) · [language alignment](https://github.com/m-bain/whisperX/blob/5d3678b8535698a2826a5db9eb3e4105aef85dd9/whisperx/alignment.py) · [diarization load](https://github.com/m-bain/whisperX/blob/5d3678b8535698a2826a5db9eb3e4105aef85dd9/whisperx/diarize.py) · [CI](https://github.com/m-bain/whisperX/blob/5d3678b8535698a2826a5db9eb3e4105aef85dd9/.github/workflows/tests.yml).

<a id="anhkysuai-2026-11-23"></a>

## Đánh giá từ kho Anh Kỹ Sư AI — 23/11/2026

Phần này có **19 hồ sơ hoặc phạm vi đối chiếu** từ [nguồn tuyển chọn](https://anhkysuai.com/kho/). [Bảng đủ 1.295 repo](../data/collections/anhkysuai-kho.json) ghi trạng thái đối chiếu từng link; [danh sách URL](../data/collections/anhkysuai-kho-links.txt) phục vụ tra cứu. Nguồn tuyển chọn giúp phát hiện repo; đánh giá bên dưới dựa trên clone và permalink upstream cùng metadata GitHub ngày 2026-11-23.

Mức `docs-read`/`code-read` chỉ áp dụng phạm vi ghi tại mỗi hồ sơ. Chưa cài, build, chạy test hay benchmark mã upstream. Giấy phép có thể tách theo code, model, nội dung, asset hoặc bản enterprise; con số/tuyên bố của tác giả chưa được tái lập nếu không có ghi chú khác.

<a id="anhkysuai-2026-11-23-upscayl"></a>

### Upscayl

**Repo:** [upscayl/upscayl](https://github.com/upscayl/upscayl) · **License:** AGPL-3.0 · **★ 53,098 (GitHub API, 2026-11-23)**

**Mục đích:** Ứng dụng tăng độ phân giải ảnh bằng mô hình AI trên desktop.

**Giá trị và cơ chế:** README xác định backend Real-ESRGAN/Vulkan và gói cho nhiều hệ điều hành; hữu ích cho luồng xử lý ảnh cần giao diện thay vì viết pipeline từ đầu.

**Giới hạn:** Cần GPU tương thích Vulkan; nhiều GPU tích hợp không được bảo đảm. Chi tiết do mô hình suy diễn không phải thông tin phục hồi được chứng minh; commit HEAD đã đọc là 27/3/2026.

**Cách tham khảo/tích hợp:** Thử ảnh đại diện và quyền weights/backend riêng; lưu ảnh gốc cùng tham số để kiểm lại kết quả.

**Thay thế:** real-esrgan, chaiNNer, [ImageMagick](../06-ui-ux-design/README.md#anhkysuai-2026-11-23-imagemagick).

**Bằng chứng:** `docs-read`, ngày 2026-11-23, commit [`a00d55fee90e`](https://github.com/upscayl/upscayl/commit/a00d55fee90e0f9435d5eaa86e76700df8199af8). README và các tài liệu/manifest/CI hiện diện, đọc chọn lọc; chưa kiểm implementation. Chưa cài/chạy upstream.

**Nguồn:** [README.md](https://github.com/upscayl/upscayl/blob/a00d55fee90e0f9435d5eaa86e76700df8199af8/README.md) · [LICENSE](https://github.com/upscayl/upscayl/blob/a00d55fee90e0f9435d5eaa86e76700df8199af8/LICENSE) · [metadata GitHub](https://api.github.com/repos/upscayl/upscayl).

<a id="anhkysuai-2026-11-23-rembg"></a>

### rembg

**Repo:** [danielgatis/rembg](https://github.com/danielgatis/rembg) · **License:** MIT cho mã; BRIA RMBG 2.0 và weights khác có license riêng · **★ 25,642 (GitHub API, 2026-11-23)**

**Mục đích:** Tách nền ảnh bằng Python, CLI hoặc HTTP với các model phân đoạn.

**Giá trị và cơ chế:** README chia chế độ ảnh, thư mục, server và byte stream; ONNX Runtime có lựa chọn CPU/CUDA/ROCm, thuận tiện ghép vào pipeline xử lý ảnh.

**Giới hạn:** Model mặc định BRIA RMBG 2.0 yêu cầu thỏa thuận trả phí khi thương mại; MIT chỉ áp dụng mã. Một số backend cloud tùy chọn gửi ảnh ra ngoài. Chưa đánh giá tóc, cạnh mờ hay throughput.

**Cách tham khảo/tích hợp:** Chọn model có quyền phù hợp, kiểm chất lượng alpha trên corpus của mình và ghim weights riêng.

**Thay thế:** [HivisionIDPhotos](../14-voice-multimodal/README.md#anhkysuai-2026-11-23-hivision-id-photos), backgroundremover, sam2.

**Bằng chứng:** `docs-read`, ngày 2026-11-23, commit [`991927b77667`](https://github.com/danielgatis/rembg/commit/991927b77667946dab59c50df31f7d4640e80457). README và các tài liệu/manifest/CI hiện diện, đọc chọn lọc; chưa kiểm implementation. Chưa cài/chạy upstream.

**Nguồn:** [README.md](https://github.com/danielgatis/rembg/blob/991927b77667946dab59c50df31f7d4640e80457/README.md) · [LICENSE.txt](https://github.com/danielgatis/rembg/blob/991927b77667946dab59c50df31f7d4640e80457/LICENSE.txt) · [metadata GitHub](https://api.github.com/repos/danielgatis/rembg).

<a id="anhkysuai-2026-11-23-hivision-id-photos"></a>

### HivisionIDPhotos

**Repo:** [Zeyi-Lin/HivisionIDPhotos](https://github.com/Zeyi-Lin/HivisionIDPhotos) · **License:** Apache-2.0 cho mã; weights tải riêng cần đối chiếu · **★ 21,758 (GitHub API, 2026-11-23)**

**Mục đích:** Tạo ảnh thẻ bằng tách nền, căn chỉnh khuôn mặt và bố trí theo kích thước yêu cầu.

**Giá trị và cơ chế:** README trình bày đường dùng Gradio, Python và API, nhiều kiểu nền và layout in; có thể chọn suy luận CPU offline hoặc thành phần đám mây.

**Giới hạn:** Mã Apache không tự xác nhận quyền tất cả weights tải về. Chưa thử ảnh hoặc đo nhận diện; tính năng đổi trang phục còn ghi chờ, không coi đã hoàn thành.

**Cách tham khảo/tích hợp:** Chọn bộ model có giấy phép rõ, kiểm tỷ lệ khuôn mặt và DPI theo yêu cầu nơi tiếp nhận ảnh.

**Thay thế:** [rembg](../14-voice-multimodal/README.md#anhkysuai-2026-11-23-rembg), [opencv](../08-awesome-lists-learning/README.md#6c525-tài-liệu-ocr--thị-giác-máy-tính), [ImageMagick](../06-ui-ux-design/README.md#anhkysuai-2026-11-23-imagemagick).

**Bằng chứng:** `docs-read`, ngày 2026-11-23, commit [`5c191e2577f1`](https://github.com/Zeyi-Lin/HivisionIDPhotos/commit/5c191e2577f14755a69d9df6db415fab23aca484). README và các tài liệu/manifest/CI hiện diện, đọc chọn lọc; chưa kiểm implementation. Chưa cài/chạy upstream.

**Nguồn:** [README.md](https://github.com/Zeyi-Lin/HivisionIDPhotos/blob/5c191e2577f14755a69d9df6db415fab23aca484/README.md) · [LICENSE](https://github.com/Zeyi-Lin/HivisionIDPhotos/blob/5c191e2577f14755a69d9df6db415fab23aca484/LICENSE) · [metadata GitHub](https://api.github.com/repos/Zeyi-Lin/HivisionIDPhotos).

<a id="anhkysuai-2026-11-23-videocaptioner"></a>

### VideoCaptioner

**Repo:** [WEIFENG2333/VideoCaptioner](https://github.com/WEIFENG2333/VideoCaptioner) · **License:** GPL-3.0 · **★ 16,612 (GitHub API, 2026-11-23)**

**Mục đích:** CLI và ứng dụng desktop tạo, tối ưu, dịch và ghép phụ đề video.

**Giá trị và cơ chế:** README tách transcribe, subtitle, dub, synthesize và process; hỗ trợ nhiều backend ASR cùng dịch truyền thống/LLM, thuận tiện ghép chuỗi xử lý media.

**Giới hạn:** Manifest ghi beta; dịch vụ miễn phí/phụ thuộc bên ngoài có thể thay đổi. Chưa kiểm độ đúng bản dịch, timestamp hay chất lượng lồng tiếng; một số chế độ cần API key và gửi nội dung ra ngoài.

**Cách tham khảo/tích hợp:** Chọn backend theo ngôn ngữ, duyệt SRT trước burn-in và giữ file gốc để sửa.

**Thay thế:** subtitle-edit, [WhisperX](../14-voice-multimodal/README.md#factory-2026-11-04-whisperx), [buzz](../08-awesome-lists-learning/README.md#6c51-ai-ảnh-giọng-nói--deepfake).

**Bằng chứng:** `docs-read`, ngày 2026-11-23, commit [`95842ecb5618`](https://github.com/WEIFENG2333/VideoCaptioner/commit/95842ecb5618c0b6a548a336bdfb0eb859bdb501). README và các tài liệu/manifest/CI hiện diện, đọc chọn lọc; chưa kiểm implementation. Chưa cài/chạy upstream.

**Nguồn:** [README.md](https://github.com/WEIFENG2333/VideoCaptioner/blob/95842ecb5618c0b6a548a336bdfb0eb859bdb501/README.md) · [LICENSE](https://github.com/WEIFENG2333/VideoCaptioner/blob/95842ecb5618c0b6a548a336bdfb0eb859bdb501/LICENSE) · [metadata GitHub](https://api.github.com/repos/WEIFENG2333/VideoCaptioner).

<a id="anhkysuai-2026-11-23-paddledetection"></a>

### PaddleDetection

**Repo:** [PaddlePaddle/PaddleDetection](https://github.com/PaddlePaddle/PaddleDetection) · **License:** Apache-2.0 cho mã; dataset/weights cần đối chiếu · **★ 14,487 (GitHub API, 2026-11-23)**

**Mục đích:** Bộ công cụ detection, segmentation, keypoint và tracking trên PaddlePaddle.

**Giá trị và cơ chế:** README tiếng Anh cùng cấu trúc cấu hình trình bày nhiều họ model, data augmentation và đường triển khai server/edge; hữu ích tham khảo pipeline vision có cấu hình rõ.

**Giới hạn:** README gốc chỉ trỏ README_cn; bản tiếng Anh chứa nhiều thông tin lịch sử, chưa xác minh toàn model zoo tại HEAD. Chưa chạy huấn luyện hoặc tái hiện mAP/FPS; quyền từng dữ liệu và weight tách riêng.

**Cách tham khảo/tích hợp:** Chọn một cấu hình hỗ trợ phần cứng mục tiêu, kiểm tập ảnh thực và export runtime trước mở rộng.

**Thay thế:** mmdetection, [ultralytics](../08-awesome-lists-learning/README.md#6c525-tài-liệu-ocr--thị-giác-máy-tính), [detectron2](../08-awesome-lists-learning/README.md#6c525-tài-liệu-ocr--thị-giác-máy-tính).

**Bằng chứng:** `docs-read`, ngày 2026-11-23, commit [`b25522a0f4bd`](https://github.com/PaddlePaddle/PaddleDetection/commit/b25522a0f4bde8c80603f3ba5e3472059972e3b5). README và các tài liệu/manifest/CI hiện diện, đọc chọn lọc; chưa kiểm implementation. Chưa cài/chạy upstream.

**Nguồn:** [README.md](https://github.com/PaddlePaddle/PaddleDetection/blob/b25522a0f4bde8c80603f3ba5e3472059972e3b5/README.md) · [LICENSE](https://github.com/PaddlePaddle/PaddleDetection/blob/b25522a0f4bde8c80603f3ba5e3472059972e3b5/LICENSE) · [README_en.md](https://github.com/PaddlePaddle/PaddleDetection/blob/b25522a0f4bde8c80603f3ba5e3472059972e3b5/README_en.md) · [metadata GitHub](https://api.github.com/repos/PaddlePaddle/PaddleDetection).

<a id="anhkysuai-2026-11-23-fluidvoice"></a>

### FluidVoice

**Repo:** [altic-dev/FluidVoice](https://github.com/altic-dev/FluidVoice) · **License:** GPL-3.0 cho app macOS; runtime Fluid Intelligence nguồn đóng · **★ 13,212 (GitHub API, 2026-11-23)**

**Mục đích:** Ứng dụng macOS nhập văn bản bằng giọng nói và lưu nội dung cuộc họp.

**Giá trị và cơ chế:** README mô tả speech model chạy trên thiết bị, cleanup tùy chọn và tích hợp vào ứng dụng đang dùng; đáng tham khảo luồng dictation desktop.

**Giới hạn:** Repo chỉ là macOS app; iOS/Windows/Linux có trạng thái beta riêng. Fluid Intelligence đi kèm binary chính thức không có mã trong source build. Chưa đo WER, độ trễ hay xác minh toàn luồng dữ liệu.

**Cách tham khảo/tích hợp:** Thử microphone, tiếng Việt và quyền Accessibility với model phù hợp; phân biệt app GPL với runtime/weights đi kèm.

**Thay thế:** [Whisper](https://github.com/openai/whisper), [buzz](../08-awesome-lists-learning/README.md#6c51-ai-ảnh-giọng-nói--deepfake), whisper-typing.

**Bằng chứng:** `docs-read`, ngày 2026-11-23, commit [`80ba776b8b07`](https://github.com/altic-dev/FluidVoice/commit/80ba776b8b07f052e8279a4f57161696112d32e5). README và các tài liệu/manifest/CI hiện diện, đọc chọn lọc; chưa kiểm implementation. Chưa cài/chạy upstream.

**Nguồn:** [README.md](https://github.com/altic-dev/FluidVoice/blob/80ba776b8b07f052e8279a4f57161696112d32e5/README.md) · [LICENSE](https://github.com/altic-dev/FluidVoice/blob/80ba776b8b07f052e8279a4f57161696112d32e5/LICENSE) · [metadata GitHub](https://api.github.com/repos/altic-dev/FluidVoice).

<a id="anhkysuai-2026-11-23-deep-live-cam"></a>

### Deep-Live-Cam

**Repo:** [hacksider/Deep-Live-Cam](https://github.com/hacksider/Deep-Live-Cam) · **License:** AGPL-3.0 cho mã; InsightFace models phi thương mại/nghiên cứu · **★ 98,767 (GitHub API, 2026-11-23)**

**Mục đích:** Ứng dụng thay khuôn mặt trong ảnh, video và camera thời gian thực.

**Giá trị và cơ chế:** README trình bày đầu vào một ảnh và pipeline sử dụng model InsightFace/ONNX; phù hợp tham khảo ghép luồng camera với inference media.

**Giới hạn:** License model được README giới hạn nghiên cứu phi thương mại, tách khỏi AGPL của mã. Chưa đo latency, độ ổn định hay kiểm bộ lọc nội dung; CLI được ghi không duy trì. Không suy quyền dùng khuôn mặt từ license phần mềm.

**Cách tham khảo/tích hợp:** Chỉ thử bằng người/tài sản đã cho phép, giữ dấu nguồn ảnh và kiểm quyền weights cùng khả năng GPU.

**Thay thế:** [FaceSwap](../14-voice-multimodal/README.md#anhkysuai-2026-11-23-faceswap), facefusion, [InsightFace](../14-voice-multimodal/README.md#anhkysuai-2026-11-23-insightface).

**Bằng chứng:** `docs-read`, ngày 2026-11-23, commit [`08896a51c9a6`](https://github.com/hacksider/Deep-Live-Cam/commit/08896a51c9a6198f50dc9f7508acf39fc460c8f1). README và các tài liệu/manifest/CI hiện diện, đọc chọn lọc; chưa kiểm implementation. Chưa cài/chạy upstream.

**Nguồn:** [README.md](https://github.com/hacksider/Deep-Live-Cam/blob/08896a51c9a6198f50dc9f7508acf39fc460c8f1/README.md) · [LICENSE](https://github.com/hacksider/Deep-Live-Cam/blob/08896a51c9a6198f50dc9f7508acf39fc460c8f1/LICENSE) · [metadata GitHub](https://api.github.com/repos/hacksider/Deep-Live-Cam).

<a id="anhkysuai-2026-11-23-stable-diffusion-v1-compvis"></a>

### Stable Diffusion v1 — CompVis

**Repo:** [CompVis/stable-diffusion](https://github.com/CompVis/stable-diffusion) · **License:** CreativeML Open RAIL-M · **★ 73,598 (GitHub API, 2026-11-23)**

**Mục đích:** Triển khai và tài liệu tham chiếu cho Stable Diffusion v1 tạo ảnh từ văn bản trong latent space.

**Giá trị và cơ chế:** README giải thích UNet kết hợp text encoder CLIP đóng băng, ảnh huấn luyện 512×512 và cơ chế điều kiện prompt; hữu ích học kiến trúc diffusion gốc.

**Giới hạn:** Đây là repo v1 lịch sử, HEAD 2022; không đại diện mọi biến thể Stable Diffusion mới. License có hạn chế cách dùng, weights được mô tả là nghiên cứu; chưa tải/chạy model hay tái hiện kết quả.

**Cách tham khảo/tích hợp:** Dùng làm nguồn học, đối chiếu checkpoint/model card và thử với tài sản có quyền trong môi trường ghim.

**Thay thế:** [diffusers](../08-awesome-lists-learning/README.md#6c51-ai-ảnh-giọng-nói--deepfake), [ComfyUI](../19-agentic-video-media/README.md#3h-kiểm-ảnh-ai-video-stack-remotion-skills-blender-và-blender-mcp-faster-whisper-chatterbox-gsap-ảnh-người-dùng-gửi-đọc-mã-8112026), [InvokeAI](../08-awesome-lists-learning/README.md#6c51-ai-ảnh-giọng-nói--deepfake).

**Bằng chứng:** `docs-read`, ngày 2026-11-23, commit [`21f890f9da3c`](https://github.com/CompVis/stable-diffusion/commit/21f890f9da3cfbeaba8e2ac3c425ee9e998d5229). README và các tài liệu/manifest/CI hiện diện, đọc chọn lọc; chưa kiểm implementation. Chưa cài/chạy upstream.

**Nguồn:** [README.md](https://github.com/CompVis/stable-diffusion/blob/21f890f9da3cfbeaba8e2ac3c425ee9e998d5229/README.md) · [LICENSE](https://github.com/CompVis/stable-diffusion/blob/21f890f9da3cfbeaba8e2ac3c425ee9e998d5229/LICENSE) · [metadata GitHub](https://api.github.com/repos/CompVis/stable-diffusion).

<a id="anhkysuai-2026-11-23-real-time-voice-cloning"></a>

### Real-Time Voice Cloning

**Repo:** [CorentinJ/Real-Time-Voice-Cloning](https://github.com/CorentinJ/Real-Time-Voice-Cloning) · **License:** MIT cho mã; dữ liệu/weights cần đối chiếu · **★ 60,247 (GitHub API, 2026-11-23)**

**Mục đích:** Triển khai SV2TTS để tổng hợp giọng từ mẫu âm thanh tham chiếu.

**Giá trị và cơ chế:** README chia ba tầng speaker encoder, synthesizer và vocoder, chỉ rõ nguồn Tacotron/WaveRNN kế thừa; phù hợp học cách tách biểu diễn người nói khỏi sinh âm thanh.

**Giới hạn:** Chưa nghe hoặc đo đầu ra; real-time trong tên không bảo đảm toàn pipeline nhanh trên mọi máy. Manifest giới hạn Python 3.9 và nhiều phụ thuộc cũ, cần môi trường riêng. Quyền giọng/weights tách khỏi MIT.

**Cách tham khảo/tích hợp:** Dùng giọng được cho phép, kiểm pronunciation và độ giống trước tích hợp; giữ baseline audio để so sánh.

**Thay thế:** [OpenVoice](../14-voice-multimodal/README.md#anhkysuai-2026-11-23-openvoice), [Coqui TTS](../14-voice-multimodal/README.md#anhkysuai-2026-11-23-coqui-tts), [MockingBird](../14-voice-multimodal/README.md#anhkysuai-2026-11-23-mockingbird).

**Bằng chứng:** `docs-read`, ngày 2026-11-23, commit [`890f3a031871`](https://github.com/CorentinJ/Real-Time-Voice-Cloning/commit/890f3a03187195b9829db2079b75c2ba2ab0405c). README và các tài liệu/manifest/CI hiện diện, đọc chọn lọc; chưa kiểm implementation. Chưa cài/chạy upstream.

**Nguồn:** [README.md](https://github.com/CorentinJ/Real-Time-Voice-Cloning/blob/890f3a03187195b9829db2079b75c2ba2ab0405c/README.md) · [LICENSE](https://github.com/CorentinJ/Real-Time-Voice-Cloning/blob/890f3a03187195b9829db2079b75c2ba2ab0405c/LICENSE) · [metadata GitHub](https://api.github.com/repos/CorentinJ/Real-Time-Voice-Cloning).

<a id="anhkysuai-2026-11-23-yolov5"></a>

### YOLOv5

**Repo:** [ultralytics/yolov5](https://github.com/ultralytics/yolov5) · **License:** AGPL-3.0; Enterprise License tùy chọn · **★ 58,302 (GitHub API, 2026-11-23)**

**Mục đích:** Họ model và công cụ PyTorch cho detection, segmentation và classification.

**Giá trị và cơ chế:** README cùng train/detect/export entrypoints cho thấy pipeline từ huấn luyện đến triển khai; phù hợp baseline vision và hệ thống cần mô hình đã có nhiều cấu hình.

**Giới hạn:** Chưa huấn luyện hoặc tái hiện mAP/FPS; README phân biệt YOLOv5 với package ultralytics mới hơn. AGPL và lựa chọn thương mại là hai chế độ khác nhau, không suy quyền weights/dataset từ nhãn repo.

**Cách tham khảo/tích hợp:** Chốt dataset, metric và format export; kiểm false positives/negatives trên dữ liệu đích trước đưa vào sản phẩm.

**Thay thế:** [MMDetection](../14-voice-multimodal/README.md#anhkysuai-2026-11-23-mmdetection), paddledetection, [detectron2](../08-awesome-lists-learning/README.md#6c525-tài-liệu-ocr--thị-giác-máy-tính).

**Bằng chứng:** `docs-read`, ngày 2026-11-23, commit [`1e7cf74cb64d`](https://github.com/ultralytics/yolov5/commit/1e7cf74cb64d719b34f7315aa13eab9e32cde672). README và các tài liệu/manifest/CI hiện diện, đọc chọn lọc; chưa kiểm implementation. Chưa cài/chạy upstream.

**Nguồn:** [README.md](https://github.com/ultralytics/yolov5/blob/1e7cf74cb64d719b34f7315aa13eab9e32cde672/README.md) · [LICENSE](https://github.com/ultralytics/yolov5/blob/1e7cf74cb64d719b34f7315aa13eab9e32cde672/LICENSE) · [metadata GitHub](https://api.github.com/repos/ultralytics/yolov5).

<a id="anhkysuai-2026-11-23-faceswap"></a>

### FaceSwap

**Repo:** [deepfakes/faceswap](https://github.com/deepfakes/faceswap) · **License:** GPL-3.0 · **★ 57,629 (GitHub API, 2026-11-23)**

**Mục đích:** Pipeline xử lý khuôn mặt với các giai đoạn trích xuất, huấn luyện và chuyển đổi media.

**Giá trị và cơ chế:** README nêu rõ entrypoint Extract–Train–Convert cùng GUI; phù hợp học cách tổ chức dữ liệu huấn luyện và tách thao tác xử lý ảnh/video.

**Giới hạn:** Chưa tải weights, huấn luyện hoặc kiểm chất lượng ghép. Bộ dữ liệu, góc mặt và ánh sáng ảnh hưởng mạnh kết quả; GPL chỉ cấp quyền phần mềm, không thay quyền sử dụng hình ảnh con người.

**Cách tham khảo/tích hợp:** Thử bằng dữ liệu có sự cho phép, lưu nguyên bản và xem từng đoạn video trước công bố kết quả.

**Thay thế:** facefusion, [Deep-Live-Cam](../14-voice-multimodal/README.md#anhkysuai-2026-11-23-deep-live-cam), [InsightFace](../14-voice-multimodal/README.md#anhkysuai-2026-11-23-insightface).

**Bằng chứng:** `docs-read`, ngày 2026-11-23, commit [`f530cb7508ae`](https://github.com/deepfakes/faceswap/commit/f530cb7508ae670f6474f8a7d9c4df94705cf96b). README và các tài liệu/manifest/CI hiện diện, đọc chọn lọc; chưa kiểm implementation. Chưa cài/chạy upstream.

**Nguồn:** [README.md](https://github.com/deepfakes/faceswap/blob/f530cb7508ae670f6474f8a7d9c4df94705cf96b/README.md) · [LICENSE](https://github.com/deepfakes/faceswap/blob/f530cb7508ae670f6474f8a7d9c4df94705cf96b/LICENSE) · [metadata GitHub](https://api.github.com/repos/deepfakes/faceswap).

<a id="anhkysuai-2026-11-23-coqui-tts"></a>

### Coqui TTS

**Repo:** [coqui-ai/TTS](https://github.com/coqui-ai/TTS) · **License:** MPL-2.0 cho mã; XTTS dùng CPML, model khác theo manifest · **★ 46,270 (GitHub API, 2026-11-23)**

**Mục đích:** Thư viện tổng hợp giọng nói với recipe huấn luyện, fine-tune và model có sẵn.

**Giá trị và cơ chế:** README trình bày Trainer API, phân tích dataset và nhiều họ TTS/vocoder; manifest model ghi riêng license và yêu cầu chấp nhận điều khoản, hữu ích quản lý vòng đời speech model.

**Giới hạn:** HEAD lấy được ở 2024, chưa kiểm hoạt động release/hosting hiện nay. XTTS trong .models.json ghi CPML/tos_required, không dùng MPL để suy quyền weights. Chưa đo WER, chất lượng hay streaming latency.

**Cách tham khảo/tích hợp:** Chọn model có điều khoản phù hợp, dùng giọng được cho phép và kiểm phát âm/ngôn ngữ trên audio thật.

**Thay thế:** [OpenVoice](../14-voice-multimodal/README.md#anhkysuai-2026-11-23-openvoice), piper, [Kokoro TTS](https://github.com/hexgrad/kokoro).

**Bằng chứng:** `docs-read`, ngày 2026-11-23, commit [`dbf1a08a0d4e`](https://github.com/coqui-ai/TTS/commit/dbf1a08a0d4e47fdad6172e433eeb34bc6b13b4e). Đọc README, MPL-2.0, manifest model và tài liệu XTTS; ghi rõ nhãn CPML nhưng chưa đọc toàn bộ điều khoản CPML bên ngoài. Chưa cài/chạy upstream.

**Nguồn:** [README.md](https://github.com/coqui-ai/TTS/blob/dbf1a08a0d4e47fdad6172e433eeb34bc6b13b4e/README.md) · [LICENSE.txt](https://github.com/coqui-ai/TTS/blob/dbf1a08a0d4e47fdad6172e433eeb34bc6b13b4e/LICENSE.txt) · [TTS/.models.json](https://github.com/coqui-ai/TTS/blob/dbf1a08a0d4e47fdad6172e433eeb34bc6b13b4e/TTS/.models.json) · [docs/source/models/xtts.md](https://github.com/coqui-ai/TTS/blob/dbf1a08a0d4e47fdad6172e433eeb34bc6b13b4e/docs/source/models/xtts.md) · [metadata GitHub](https://api.github.com/repos/coqui-ai/TTS).

<a id="anhkysuai-2026-11-23-chattts"></a>

### ChatTTS

**Repo:** [2noise/ChatTTS](https://github.com/2noise/ChatTTS) · **License:** AGPL-3.0-or-later cho mã; CC-BY-NC-4.0 cho model · **★ 40,036 (GitHub API, 2026-11-23)**

**Mục đích:** Model tổng hợp giọng đối thoại với điều khiển nhịp, khoảng ngừng và biểu cảm.

**Giá trị và cơ chế:** README phân biệt hạ tầng thuật toán với sản phẩm cộng đồng, mô tả multi-speaker và prosody cho tiếng Anh/Trung; hữu ích thử giọng hội thoại cho trợ lý.

**Giới hạn:** Weights được công bố cho học thuật/nghiên cứu và phi thương mại; không thể coi toàn pipeline AGPL mở cho mọi mục đích. Tiếng Việt chưa nằm trong danh sách hỗ trợ đã đọc. Chưa nghe/đo chất lượng.

**Cách tham khảo/tích hợp:** Thử corpus đối thoại được phép sử dụng, kiểm phát âm/pauses và quyền model trước ghép thành sản phẩm.

**Thay thế:** [Kokoro TTS](https://github.com/hexgrad/kokoro), [OpenVoice](../14-voice-multimodal/README.md#anhkysuai-2026-11-23-openvoice), [Coqui TTS](../14-voice-multimodal/README.md#anhkysuai-2026-11-23-coqui-tts).

**Bằng chứng:** `docs-read`, ngày 2026-11-23, commit [`77b89ee281cd`](https://github.com/2noise/ChatTTS/commit/77b89ee281cd479f5b1a787ada330dc975ca1f2a). README và các tài liệu/manifest/CI hiện diện, đọc chọn lọc; chưa kiểm implementation. Chưa cài/chạy upstream.

**Nguồn:** [README.md](https://github.com/2noise/ChatTTS/blob/77b89ee281cd479f5b1a787ada330dc975ca1f2a/README.md) · [LICENSE](https://github.com/2noise/ChatTTS/blob/77b89ee281cd479f5b1a787ada330dc975ca1f2a/LICENSE) · [metadata GitHub](https://api.github.com/repos/2noise/ChatTTS).

<a id="anhkysuai-2026-11-23-openvoice"></a>

### OpenVoice

**Repo:** [myshell-ai/OpenVoice](https://github.com/myshell-ai/OpenVoice) · **License:** MIT cho V1/V2 theo LICENSE và README · **★ 38,308 (GitHub API, 2026-11-23)**

**Mục đích:** Tạo giọng theo mẫu tham chiếu với điều khiển phong cách và chuyển ngôn ngữ.

**Giá trị và cơ chế:** README phân tách màu giọng, biểu cảm/nhịp và zero-shot cross-lingual; V2 liệt kê sáu ngôn ngữ gốc, phù hợp học cách kết hợp TTS với tone-color conversion.

**Giới hạn:** Chưa chạy notebook hoặc nghe kết quả. Tuyên bố chất lượng/clone chính xác là từ tác giả; tiếng Việt không nằm trong danh sách native đã đọc. License phần mềm không thay sự cho phép dùng giọng của người khác.

**Cách tham khảo/tích hợp:** Dùng mẫu có quyền, kiểm pronunciation và chất lượng qua từng ngôn ngữ trước tích hợp dịch vụ.

**Thay thế:** [Coqui TTS](../14-voice-multimodal/README.md#anhkysuai-2026-11-23-coqui-tts), [Real-Time Voice Cloning](../14-voice-multimodal/README.md#anhkysuai-2026-11-23-real-time-voice-cloning), [Kokoro TTS](https://github.com/hexgrad/kokoro).

**Bằng chứng:** `docs-read`, ngày 2026-11-23, commit [`74a1d147b17a`](https://github.com/myshell-ai/OpenVoice/commit/74a1d147b17a8c3092dd5430504bd83ef6c7eb23). README và các tài liệu/manifest/CI hiện diện, đọc chọn lọc; chưa kiểm implementation. Chưa cài/chạy upstream.

**Nguồn:** [README.md](https://github.com/myshell-ai/OpenVoice/blob/74a1d147b17a8c3092dd5430504bd83ef6c7eb23/README.md) · [LICENSE](https://github.com/myshell-ai/OpenVoice/blob/74a1d147b17a8c3092dd5430504bd83ef6c7eb23/LICENSE) · [metadata GitHub](https://api.github.com/repos/myshell-ai/OpenVoice).

<a id="anhkysuai-2026-11-23-real-esrgan"></a>

### Real-ESRGAN

**Repo:** [xinntao/Real-ESRGAN](https://github.com/xinntao/Real-ESRGAN) · **License:** BSD-3-Clause (mã); kiểm riêng điều khoản weights · **★ 37,617 (GitHub API, 2026-11-23)**

**Mục đích:** Khôi phục và tăng độ phân giải ảnh, với các model dành cho ảnh thực và anime.

**Giá trị và cơ chế:** README phân biệt model theo nội dung, cung cấp luồng suy luận Python và bản NCNN/Vulkan; hữu ích để khảo sát pipeline phục hồi ảnh/video.

**Giới hạn:** Chưa chạy suy luận hoặc đo chất lượng. Kết quả phụ thuộc loại suy giảm ảnh và weights; chi tiết được tái tạo có thể không phản ánh ảnh gốc.

**Cách tham khảo/tích hợp:** Thử một tập ảnh có bản đối chiếu, chọn model phù hợp và kiểm quyền phân phối weights trước khi đóng gói.

**Thay thế:** Upscayl, waifu2x, [Anime4K](../19-agentic-video-media/README.md#anhkysuai-2026-11-23-anime4k).

**Bằng chứng:** `docs-read`, ngày 2026-11-23, commit [`a4abfb2979a7`](https://github.com/xinntao/Real-ESRGAN/commit/a4abfb2979a7bbff3f69f58f58ae324608821e27). README và các tài liệu/manifest/CI hiện diện, đọc chọn lọc; chưa kiểm implementation. Chưa cài/chạy upstream.

**Nguồn:** [README.md](https://github.com/xinntao/Real-ESRGAN/blob/a4abfb2979a7bbff3f69f58f58ae324608821e27/README.md) · [LICENSE](https://github.com/xinntao/Real-ESRGAN/blob/a4abfb2979a7bbff3f69f58f58ae324608821e27/LICENSE) · [metadata GitHub](https://api.github.com/repos/xinntao/Real-ESRGAN).

<a id="anhkysuai-2026-11-23-mockingbird"></a>

### MockingBird

**Repo:** [babysor/MockingBird](https://github.com/babysor/MockingBird) · **License:** MIT · **★ 36,856 (GitHub API, 2026-11-23)**

**Mục đích:** Tham khảo tổng hợp giọng nói tiếng Quan thoại từ mẫu giọng ngắn.

**Giá trị và cơ chế:** Dự án kế thừa hướng SV2TTS, tách encoder, synthesizer và vocoder, kèm giao diện web và cấu hình huấn luyện/suy luận.

**Giới hạn:** README thông báo không còn cập nhật tích cực; sản phẩm Noiz được giới thiệu riêng. Chưa tạo audio, kiểm chất lượng hay khả năng tiếng Việt; dependency cũ cần đánh giá lại.

**Cách tham khảo/tích hợp:** Dùng để học cấu trúc pipeline và thử với giọng đã có quyền sử dụng, đồng thời kiểm điều khoản từng bộ weights.

**Thay thế:** [OpenVoice](../14-voice-multimodal/README.md#anhkysuai-2026-11-23-openvoice), [Real-Time Voice Cloning](../14-voice-multimodal/README.md#anhkysuai-2026-11-23-real-time-voice-cloning), [Coqui TTS](../14-voice-multimodal/README.md#anhkysuai-2026-11-23-coqui-tts).

**Bằng chứng:** `docs-read`, ngày 2026-11-23, commit [`28dc5e14f12d`](https://github.com/babysor/MockingBird/commit/28dc5e14f12d7c754612af2fde8e78a4b03f8616). README và các tài liệu/manifest/CI hiện diện, đọc chọn lọc; chưa kiểm implementation. Chưa cài/chạy upstream.

**Nguồn:** [README.md](https://github.com/babysor/MockingBird/blob/28dc5e14f12d7c754612af2fde8e78a4b03f8616/README.md) · [LICENSE.txt](https://github.com/babysor/MockingBird/blob/28dc5e14f12d7c754612af2fde8e78a4b03f8616/LICENSE.txt) · [metadata GitHub](https://api.github.com/repos/babysor/MockingBird).

<a id="anhkysuai-2026-11-23-openpose"></a>

### OpenPose

**Repo:** [CMU-Perceptual-Computing-Lab/openpose](https://github.com/CMU-Perceptual-Computing-Lab/openpose) · **License:** Giấy phép OpenPose tùy chỉnh, nghiên cứu phi thương mại; thương mại cần thỏa thuận · **★ 34,610 (GitHub API, 2026-11-23)**

**Mục đích:** Ước lượng keypoint cơ thể, bàn tay, khuôn mặt và bàn chân cho nhiều người trong ảnh hoặc video.

**Giá trị và cơ chế:** README mô tả pipeline hợp nhất các vùng cơ thể, cung cấp ví dụ và cấu hình build để nghiên cứu pose estimation.

**Giới hạn:** LICENSE cấp quyền nghiên cứu phi thương mại với điều kiện cụ thể; không thể suy từ mã công khai rằng được dùng thương mại. Chưa build hoặc kiểm độ chính xác và tốc độ.

**Cách tham khảo/tích hợp:** Đối chiếu giấy phép với mục đích sử dụng, kiểm toolchain và dữ liệu thử nghiệm trước khi chọn làm thành phần sản phẩm.

**Thay thế:** [mediapipe](../08-awesome-lists-learning/README.md#6c525-tài-liệu-ocr--thị-giác-máy-tính), MMPose, Ultralytics YOLO.

**Bằng chứng:** `docs-read`, ngày 2026-11-23, commit [`5c5d96523ef9`](https://github.com/CMU-Perceptual-Computing-Lab/openpose/commit/5c5d96523ef917bd30301245fdc8343937cae48d). README và các tài liệu/manifest/CI hiện diện, đọc chọn lọc; chưa kiểm implementation. Chưa cài/chạy upstream.

**Nguồn:** [README.md](https://github.com/CMU-Perceptual-Computing-Lab/openpose/blob/5c5d96523ef917bd30301245fdc8343937cae48d/README.md) · [LICENSE](https://github.com/CMU-Perceptual-Computing-Lab/openpose/blob/5c5d96523ef917bd30301245fdc8343937cae48d/LICENSE) · [metadata GitHub](https://api.github.com/repos/CMU-Perceptual-Computing-Lab/openpose).

<a id="anhkysuai-2026-11-23-mmdetection"></a>

### MMDetection

**Repo:** [open-mmlab/mmdetection](https://github.com/open-mmlab/mmdetection) · **License:** Apache-2.0 · **★ 33,052 (GitHub API, 2026-11-23)**

**Mục đích:** Huấn luyện và đánh giá các mô hình phát hiện vật thể, phân đoạn instance và các bài toán liên quan.

**Giá trị và cơ chế:** README trình bày thư viện PyTorch theo module, cấu hình và model zoo; phù hợp so sánh nhiều kiến trúc trong cùng hệ sinh thái OpenMMLab.

**Giới hạn:** Chưa chạy model hoặc kiểm tổ hợp phiên bản CUDA, PyTorch và các operator. License mã không tự xác nhận quyền của mọi dataset/weights trong model zoo.

**Cách tham khảo/tích hợp:** Ghim cấu hình và checkpoint, dựng môi trường tương thích rồi kiểm metric trên dữ liệu đại diện của dự án.

**Thay thế:** PaddleDetection, [YOLOv5](../14-voice-multimodal/README.md#anhkysuai-2026-11-23-yolov5), [detectron2](../08-awesome-lists-learning/README.md#6c525-tài-liệu-ocr--thị-giác-máy-tính).

**Bằng chứng:** `docs-read`, ngày 2026-11-23, commit [`cfd5d3a985b0`](https://github.com/open-mmlab/mmdetection/commit/cfd5d3a985b0249de009b67d04f37263e11cdf3d). README và các tài liệu/manifest/CI hiện diện, đọc chọn lọc; chưa kiểm implementation. Chưa cài/chạy upstream.

**Nguồn:** [README.md](https://github.com/open-mmlab/mmdetection/blob/cfd5d3a985b0249de009b67d04f37263e11cdf3d/README.md) · [LICENSE](https://github.com/open-mmlab/mmdetection/blob/cfd5d3a985b0249de009b67d04f37263e11cdf3d/LICENSE) · [metadata GitHub](https://api.github.com/repos/open-mmlab/mmdetection).

<a id="anhkysuai-2026-11-23-insightface"></a>

### InsightFace

**Repo:** [deepinsight/insightface](https://github.com/deepinsight/insightface) · **License:** MIT theo README cho SDK; SCRFD Apache-2.0; pretrained models phi thương mại · **★ 30,285 (GitHub API, 2026-11-23)**

**Mục đích:** Bộ công cụ phân tích khuôn mặt với detection, alignment, recognition và các thành phần liên quan.

**Giá trị và cơ chế:** README SDK tách rõ license mã và model tải sẵn; MODEL.LICENSE của buffalo_l ghi grant non-commercial. Bản nguồn còn mô tả dịch vụ và công cụ xử lý riêng tư.

**Giới hạn:** Không lấy LICENSE Apache của thư mục SCRFD làm license toàn repo. Chưa chạy nhận diện hoặc đánh giá sai lệch; quyền dùng weights và dữ liệu khuôn mặt cần kiểm riêng.

**Cách tham khảo/tích hợp:** Chọn module và model theo đúng phạm vi giấy phép, xác định mục đích cùng quyền xử lý dữ liệu trước khi thử nghiệm.

**Thay thế:** [deepface](../08-awesome-lists-learning/README.md#6c525-tài-liệu-ocr--thị-giác-máy-tính), [opencv](../08-awesome-lists-learning/README.md#6c525-tài-liệu-ocr--thị-giác-máy-tính), face_recognition.

**Bằng chứng:** `docs-read`, ngày 2026-11-23, commit [`c6c3af7bd2d0`](https://github.com/deepinsight/insightface/commit/c6c3af7bd2d0a0bf4b78c78437357f3521aa5d52). Đọc README gốc và SDK, license nested SCRFD và MODEL.LICENSE buffalo_l; chưa kiểm implementation hay độ chính xác model. Chưa cài/chạy upstream.

**Nguồn:** [README.md](https://github.com/deepinsight/insightface/blob/c6c3af7bd2d0a0bf4b78c78437357f3521aa5d52/README.md) · [detection/scrfd/LICENSE](https://github.com/deepinsight/insightface/blob/c6c3af7bd2d0a0bf4b78c78437357f3521aa5d52/detection/scrfd/LICENSE) · [python-package/README.md](https://github.com/deepinsight/insightface/blob/c6c3af7bd2d0a0bf4b78c78437357f3521aa5d52/python-package/README.md) · [server/backend/insightface_server/licensing/defaults/buffalo_l/MODEL.LICENSE](https://github.com/deepinsight/insightface/blob/c6c3af7bd2d0a0bf4b78c78437357f3521aa5d52/server/backend/insightface_server/licensing/defaults/buffalo_l/MODEL.LICENSE) · [metadata GitHub](https://api.github.com/repos/deepinsight/insightface).

## 6. Nguồn

- https://micdrop.dev/blog/open-source-voice-agent-frameworks · https://livekit.com/blog/best-open-source-voice-and-video-ai-agent-frameworks · https://www.forasoft.com/blog/article/pipecat-vs-livekit-agents · https://github.com/pipecat-ai/pipecat · https://techsy.io/en/blog/best-open-source-voice-agent-frameworks · https://grokipedia.com/page/List_of_open-source_voice_AI_frameworks
- https://ocdevel.com/blog/20250720-tts · https://pinggy.io/blog/best_open_source_self_hosted_text_to_speech_models/ · https://www.tryspeakeasy.io/blog/open-source-text-to-speech-2026 · https://localaimaster.com/blog/best-local-tts-models · https://www.spheron.network/blog/deploy-open-source-tts-gpu-cloud-2026/
- https://github.com/QwenLM/Qwen3-VL · https://github.com/LLaVA-VL/LLaVA-NeXT · https://github.com/EvolvingLMMs-Lab/LLaVA-OneVision-2
- https://en.wikipedia.org/wiki/ComfyUI · https://en.wikipedia.org/wiki/Automatic1111 · https://github.com/lllyasviel/Fooocus · https://insiderllm.com/guides/comfyui-vs-automatic1111-vs-fooocus/ · https://meetrix.io/blogs/fooocus-vs-automatic1111-vs-comfyui/
- Audio8 TTS (2026-10-12): https://github.com/edge0-ai/audio8_tts (clone đầy đủ) · https://huggingface.co/Audio8/Audio8-TTS-Preview-0.6b · https://huggingface.co/Audio8/Audio8-TTS-Preview-0.1b · https://audio8-ai.github.io/Audio8_TTS/ · https://deepinfra.com/Audio8/Audio8-TTS-Preview-0.6b · https://github.com/john-rocky/coreai-model-zoo/pull/47 · https://github.com/0xShug0/audio.cpp/blob/main/docs/community_models/audio8_tts.md · https://hackernoon.com/audio8-tts-preview-06b-compact-multilingual-voice-cloning · https://creativeaishow.com/audio8-tts-preview-the-free-0-6b-ai-voice-cloning-model-that-runs-on-your-cpu/ · https://huggingface.co/fishaudio/s2-pro/blob/main/LICENSE.md · https://fish.audio/fr/blog/what-we-mean-by-open-source-for-s2/

<a id="xlsx-2026-11-23"></a>

## Đánh giá bổ sung từ bảng "Top 100 GitHub AI Skills" — 23/11/2026

Phần này có **1 hồ sơ** từ bảng xlsx người dùng gửi ngày 2026-11-23; đọc bằng `git clone --depth 1`, không cài hay chạy mã upstream. Lúc đọc, REST API của GitHub bị chặn nên trong hồ sơ ★ và `pushed_at` ghi **(chưa xác minh)**; số sao lấy lại cùng ngày qua GitHub search API nằm trong `data/projects.json` và [catalog/](../catalog/README.md), `pushed_at` vẫn chưa xác minh.

<a id="xlsx-2026-11-23-liveavatar-agent-skills"></a>

### heygen-com/liveavatar-agent-skills

**Repo:** [heygen-com/liveavatar-agent-skills](https://github.com/heygen-com/liveavatar-agent-skills) · **License:** MIT (LICENSE, © 2026 HeyGen; chỉ áp cho 4 file skill, dịch vụ LiveAvatar là sản phẩm thương mại cần API key) · **★ (chưa xác minh; GitHub API bị chặn ngày 2026-11-23)**

**Mục đích:** 4 skill cho agent lập trình tích hợp avatar hội thoại thời gian thực của LiveAvatar (HeyGen): `liveavatar-demo` (dựng demo từ danh mục 4 repo mẫu), `liveavatar-integrate` (chọn lối Embed / FULL / LITE rồi hướng dẫn từng bước), `liveavatar-debug` (triệu chứng: avatar câm, âm thanh vỡ, lỗi auth), `liveavatar-feedback` (gửi góp ý cho đội LiveAvatar).

**Giá trị và cơ chế:** repo chỉ là tri thức dạng văn bản (không có mã chạy, `package.json` không có dependency). Điểm đáng học: `liveavatar-integrate` ép tách backend/frontend (`X-API-KEY` chỉ ở backend, frontend chỉ nhận `livekit_client_token`) và khuyến nghị bắt đầu bằng sandbox (`is_sandbox: true`, phiên khoảng 1 phút). `liveavatar-demo` ghi thẳng điều agent **không** làm được (không nghe được avatar nói, không tự nhập key). `liveavatar-feedback` có cổng đồng ý đúng nghĩa: SKILL.md bắt buộc trình bản tóm tắt cho người dùng, "Nothing is sent until you say yes", từ chối thì bỏ.

**Giới hạn:** phụ thuộc dịch vụ trả phí và API `api.liveavatar.com`; `liveavatar-demo` clone và cài repo bên thứ ba (4 demo, trong đó có demo dùng GPT-Live) rồi chạy `npm install`/`uv` trên máy bạn, tức là thực thi mã ngoài repo này. Không có CI, không có test, không có kiểm schema skill. Dữ liệu rời máy: lưu lượng hội thoại qua LiveAvatar/LiveKit; feedback chỉ gửi sau khi người dùng đồng ý (theo văn bản SKILL.md, chưa kiểm hành vi thực).

**Cách tham khảo/tích hợp:** dùng làm mẫu cho skill tích hợp API thương mại: lead bằng "gotcha", nhãn rõ chỗ chạy (backend/frontend) và loại auth, cổng đồng ý trước khi gửi dữ liệu. Nếu dùng thật, giữ key trong biến môi trường backend và dùng sandbox trước; kiểm từng repo demo trước khi để agent chạy `npm install`.

**Thay thế:** [LiveKit Agents](../14-voice-multimodal/README.md) (id `livekit-agents`, tự dựng pipeline STT-LLM-TTS), [Pipecat](../14-voice-multimodal/README.md) (id `pipecat`), skill video không thời gian thực của cùng hãng ở [heygen-com/skills](../19-agentic-video-media/README.md#xlsx-2026-11-23-heygen-skills).

**Bằng chứng:** `code-read`, ngày 2026-11-23, commit [`88960dc00ebb`](https://github.com/heygen-com/liveavatar-agent-skills/commit/88960dc00ebb35c128b15345a97c5aebcd89a676) (2026-09-10). Đọc README, LICENSE, package.json, `liveavatar-feedback/SKILL.md` toàn bộ, đầu `liveavatar-demo/SKILL.md` và `liveavatar-integrate/SKILL.md`; không có `.github/` nên không có CI để đọc. Chưa cài, chưa gọi API, chưa kiểm 4 repo demo.

**Nguồn:** [README.md](https://github.com/heygen-com/liveavatar-agent-skills/blob/88960dc00ebb35c128b15345a97c5aebcd89a676/README.md) · [LICENSE](https://github.com/heygen-com/liveavatar-agent-skills/blob/88960dc00ebb35c128b15345a97c5aebcd89a676/LICENSE) · [package.json](https://github.com/heygen-com/liveavatar-agent-skills/blob/88960dc00ebb35c128b15345a97c5aebcd89a676/package.json) · [skills/liveavatar-feedback/SKILL.md](https://github.com/heygen-com/liveavatar-agent-skills/blob/88960dc00ebb35c128b15345a97c5aebcd89a676/skills/liveavatar-feedback/SKILL.md) · [skills/liveavatar-demo/SKILL.md](https://github.com/heygen-com/liveavatar-agent-skills/blob/88960dc00ebb35c128b15345a97c5aebcd89a676/skills/liveavatar-demo/SKILL.md) · [skills/liveavatar-integrate/SKILL.md](https://github.com/heygen-com/liveavatar-agent-skills/blob/88960dc00ebb35c128b15345a97c5aebcd89a676/skills/liveavatar-integrate/SKILL.md) · [metadata GitHub](https://api.github.com/repos/heygen-com/liveavatar-agent-skills) (không đọc được, 403).

<a id="chuan-hoa-2026-11-23"></a>

## Chuẩn hóa bằng chứng hồ sơ cũ — 23/11/2026

Các hồ sơ dưới đây có từ trước khi kho ghi mức kiểm. Ngày 2026-11-23 mỗi repo được clone nông tại commit ghi trong bảng, đọc LICENSE, README, manifest và CI (nếu có); không cài, build hay chạy mã upstream. Nhận định cũ ở phần trên giữ nguyên; chỗ nào khác với lần đọc này được ghi trong cột Nhận định. Số sao lấy qua GitHub search API cùng ngày.

<a id="ch-ace-step-1-5"></a>

### ACE-Step 1.5

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/ace-step/ACE-Step-1.5 |
| License | MIT (mã); trọng số chưa kiểm |
| Phiên bản đã đọc | `ca1e85fe9430179831e6bc6be790c332190a3866` (commit 2026-08-29) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE, pyproject.toml; chưa chạy upstream |
| Bảo trì | Đang hoạt động (commit 2026-08-29) |
| Nhận định | Mô hình sinh nhạc mã nguồn mở có CLI, API server, Gradio UI và Docker (kể cả Jetson, XPU, ROCm). Giấy phép trọng số trên Hugging Face **(chưa xác minh)** vì chưa đọc model card. |
| Nguồn | [README.md](https://github.com/ace-step/ACE-Step-1.5/blob/ca1e85fe9430179831e6bc6be790c332190a3866/README.md) · [LICENSE](https://github.com/ace-step/ACE-Step-1.5/blob/ca1e85fe9430179831e6bc6be790c332190a3866/LICENSE) · [pyproject.toml](https://github.com/ace-step/ACE-Step-1.5/blob/ca1e85fe9430179831e6bc6be790c332190a3866/pyproject.toml) |

<a id="ch-audio8-tts"></a>

### Audio8 TTS

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/Edge0-AI/Audio8_TTS |
| License | Apache-2.0 (mã và hai bản 0.6B); 0.1B dùng Audio8 Community License v1.0 |
| Phiên bản đã đọc | `aef426db7229b93c8cb9a00c7c054b2b234e2979` (commit 2026-11-16) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE, NOTICE, pyproject.toml; chưa chạy upstream |
| Bảo trì | Đang hoạt động (commit 2026-11-16) |
| Nhận định | TTS gọn cho voice cloning zero-shot, kèm ONNX INT8 cho CPU và llama.cpp/GGUF. Chất lượng từng ngôn ngữ khác nhau theo chính README; không có ONNX cho Realistic Air; số liệu chất lượng là của tác giả **(chưa xác minh)**. |
| Nguồn | [README.md](https://github.com/Edge0-AI/Audio8_TTS/blob/aef426db7229b93c8cb9a00c7c054b2b234e2979/README.md) · [LICENSE](https://github.com/Edge0-AI/Audio8_TTS/blob/aef426db7229b93c8cb9a00c7c054b2b234e2979/LICENSE) · [NOTICE](https://github.com/Edge0-AI/Audio8_TTS/blob/aef426db7229b93c8cb9a00c7c054b2b234e2979/NOTICE) · [pyproject.toml](https://github.com/Edge0-AI/Audio8_TTS/blob/aef426db7229b93c8cb9a00c7c054b2b234e2979/pyproject.toml) |

<a id="ch-audioseal"></a>

### AudioSeal

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/facebookresearch/audioseal |
| License | MIT |
| Phiên bản đã đọc | `1496f7662d6aa625602bb0dcd1b4997b63b47609` (commit 2026-11-03) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE, pyproject.toml; chưa chạy upstream |
| Bảo trì | Đang hoạt động (commit 2026-11-03) |
| Nhận định | Watermark âm thanh định vị theo đoạn gồm generator và detector, có mã huấn luyện. Khả năng chống tấn công gỡ watermark là tuyên bố của tác giả **(chưa xác minh)**. |
| Nguồn | [README.md](https://github.com/facebookresearch/audioseal/blob/1496f7662d6aa625602bb0dcd1b4997b63b47609/README.md) · [LICENSE](https://github.com/facebookresearch/audioseal/blob/1496f7662d6aa625602bb0dcd1b4997b63b47609/LICENSE) · [pyproject.toml](https://github.com/facebookresearch/audioseal/blob/1496f7662d6aa625602bb0dcd1b4997b63b47609/pyproject.toml) |

<a id="ch-eva-servicenow"></a>

### EVA (ServiceNow)

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/ServiceNow/eva |
| License | MIT |
| Phiên bản đã đọc | `5a79590f3fc68f5c27a844729ca5160c54e3526b` (commit 2026-11-18) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE, pyproject.toml, THIRD_PARTY_NOTICES; chưa chạy upstream |
| Bảo trì | Đang hoạt động (commit 2026-11-18) |
| Nhận định | Khung đánh giá voice agent hội thoại nhiều lượt theo hai trục Accuracy và Experience, kiến trúc bot-to-bot, kèm bộ nhiễu/accent/kết nối kém (accent cần ElevenLabs caller). Kết quả 12 hệ thống là số của tác giả **(chưa xác minh)**. |
| Nguồn | [README.md](https://github.com/ServiceNow/eva/blob/5a79590f3fc68f5c27a844729ca5160c54e3526b/README.md) · [LICENSE](https://github.com/ServiceNow/eva/blob/5a79590f3fc68f5c27a844729ca5160c54e3526b/LICENSE) · [pyproject.toml](https://github.com/ServiceNow/eva/blob/5a79590f3fc68f5c27a844729ca5160c54e3526b/pyproject.toml) · [THIRD_PARTY_NOTICES](https://github.com/ServiceNow/eva/blob/5a79590f3fc68f5c27a844729ca5160c54e3526b/THIRD_PARTY_NOTICES) |

<a id="ch-fish-audio-s2-pro"></a>

### Fish Audio S2 Pro

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/fishaudio/fish-speech |
| License | Fish Audio Community License v1.0 (mã và Drama 3; trọng số S2-Pro vẫn Research License) — khác catalog cũ "Fish Audio Research License" |
| Phiên bản đã đọc | `0f8a12e8a651062fdee9c33a894bdccd3a8513f1` (commit 2026-10-30) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE, pyproject.toml; chưa chạy upstream |
| Bảo trì | Đang hoạt động (commit 2026-10-30) |
| Nhận định | Mã và model TTS Fish Audio; README khuyên dùng SGLang-Omni/vLLM-Omni để suy luận hiệu quả. Không phải mã nguồn mở theo OSI; mọi dùng thương mại phải đọc điều kiện doanh thu và cấm dịch vụ hosted. Hồ sơ cũ ghi S2 Pro là trọng tâm, nay đã lỗi thời. |
| Nguồn | [README.md](https://github.com/fishaudio/fish-speech/blob/0f8a12e8a651062fdee9c33a894bdccd3a8513f1/README.md) · [LICENSE](https://github.com/fishaudio/fish-speech/blob/0f8a12e8a651062fdee9c33a894bdccd3a8513f1/LICENSE) · [pyproject.toml](https://github.com/fishaudio/fish-speech/blob/0f8a12e8a651062fdee9c33a894bdccd3a8513f1/pyproject.toml) |

<a id="ch-flux-2"></a>

### FLUX.2

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/black-forest-labs/flux2 |
| License | Apache-2.0 (mã); trọng số tùy bản (4B Apache-2.0; 9B/dev FLUX Non-Commercial) |
| Phiên bản đã đọc | `50fe5162777813d869182b139e83b10743caef15` (commit 2026-03-12) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE.md, pyproject.toml, model_licenses/LICENSE-FLUX-NON-COMMERICAL; chưa chạy upstream |
| Bảo trì | Ít hoạt động (commit cuối 2026-03-12) |
| Nhận định | Mã suy luận tối thiểu cho tạo/sửa ảnh của FLUX.2 (family klein và dev). Chỉ bản 4B dùng thương mại được theo README; 9B/dev cấm thương mại và sản xuất. Commit cuối 2026-03-12 nên coi là ít hoạt động. |
| Nguồn | [README.md](https://github.com/black-forest-labs/flux2/blob/50fe5162777813d869182b139e83b10743caef15/README.md) · [LICENSE.md](https://github.com/black-forest-labs/flux2/blob/50fe5162777813d869182b139e83b10743caef15/LICENSE.md) · [pyproject.toml](https://github.com/black-forest-labs/flux2/blob/50fe5162777813d869182b139e83b10743caef15/pyproject.toml) · [LICENSE-FLUX-NON-COMMERICAL](https://github.com/black-forest-labs/flux2/blob/50fe5162777813d869182b139e83b10743caef15/model_licenses/LICENSE-FLUX-NON-COMMERICAL) |

<a id="ch-fooocus"></a>

### Fooocus

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/lllyasviel/Fooocus |
| License | GPL-3.0 |
| Phiên bản đã đọc | `ae05379cc97bc4361ec8b4ec90193dab21be763f` (commit 2025-09-02) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc readme.md, LICENSE, fooocus_version.py; chưa chạy upstream |
| Bảo trì | Ít hoạt động (commit cuối 2025-09-02) |
| Nhận định | Phần mềm tạo ảnh offline dựa trên SDXL với Gradio UI. GPL-3.0 là copyleft nên cần cân nhắc khi nhúng; chỉ sửa lỗi nên không phù hợp để theo kịp model mới (README tự giới thiệu WebUI Forge, ComfyUI). |
| Nguồn | [readme.md](https://github.com/lllyasviel/Fooocus/blob/ae05379cc97bc4361ec8b4ec90193dab21be763f/readme.md) · [LICENSE](https://github.com/lllyasviel/Fooocus/blob/ae05379cc97bc4361ec8b4ec90193dab21be763f/LICENSE) · [fooocus_version.py](https://github.com/lllyasviel/Fooocus/blob/ae05379cc97bc4361ec8b4ec90193dab21be763f/fooocus_version.py) |

<a id="ch-gpt-sovits"></a>

### GPT-SoVITS

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/RVC-Boss/GPT-SoVITS |
| License | MIT |
| Phiên bản đã đọc | `6d51ffceafbf240145619af4c92408a6e54b7924` (commit 2026-11-12) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE; chưa chạy upstream |
| Bảo trì | Đang hoạt động (commit 2026-11-12) |
| Nhận định | WebUI TTS/voice conversion few-shot (1 phút dữ liệu) kèm công cụ tách giọng, cắt dữ liệu, ASR tiếng Trung. Chưa kiểm giấy phép các model tiền huấn luyện đi kèm **(chưa xác minh)**; công nghệ nhân bản giọng cần cơ chế đồng ý và gắn nhãn. |
| Nguồn | [README.md](https://github.com/RVC-Boss/GPT-SoVITS/blob/6d51ffceafbf240145619af4c92408a6e54b7924/README.md) · [LICENSE](https://github.com/RVC-Boss/GPT-SoVITS/blob/6d51ffceafbf240145619af4c92408a6e54b7924/LICENSE) |

<a id="ch-handy"></a>

### Handy

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/cjpais/Handy |
| License | MIT |
| Phiên bản đã đọc | `939c9573a346859016de1f9d87369a9765af1671` (commit 2026-11-21) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE, package.json; chưa chạy upstream |
| Bảo trì | Đang hoạt động (commit 2026-11-21) |
| Nhận định | Ứng dụng desktop Tauri chuyển giọng thành văn bản hoàn toàn offline (Whisper) và dán vào ô đang chọn. Tuyên bố riêng tư/không gửi dữ liệu là của tác giả **(chưa xác minh)**; chưa đọc mã mạng. |
| Nguồn | [README.md](https://github.com/cjpais/Handy/blob/939c9573a346859016de1f9d87369a9765af1671/README.md) · [LICENSE](https://github.com/cjpais/Handy/blob/939c9573a346859016de1f9d87369a9765af1671/LICENSE) · [package.json](https://github.com/cjpais/Handy/blob/939c9573a346859016de1f9d87369a9765af1671/package.json) |

<a id="ch-jiwer"></a>

### JiWER

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/jitsi/jiwer |
| License | Apache-2.0 |
| Phiên bản đã đọc | `2227002889f20f3fb19d523eeb322732cb67b431` (commit 2026-04-16) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE, pyproject.toml; chưa chạy upstream |
| Bảo trì | Ít hoạt động (commit cuối 2026-04-16) |
| Nhận định | Thư viện Python nhỏ tính WER, MER, WIL, WIP, CER qua RapidFuzz. Kết quả phụ thuộc bước chuẩn hóa văn bản do người dùng định nghĩa; phù hợp cổng CI vì nhẹ. |
| Nguồn | [README.md](https://github.com/jitsi/jiwer/blob/2227002889f20f3fb19d523eeb322732cb67b431/README.md) · [LICENSE](https://github.com/jitsi/jiwer/blob/2227002889f20f3fb19d523eeb322732cb67b431/LICENSE) · [pyproject.toml](https://github.com/jitsi/jiwer/blob/2227002889f20f3fb19d523eeb322732cb67b431/pyproject.toml) |

<a id="ch-kokoro-tts"></a>

### Kokoro TTS

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/hexgrad/kokoro |
| License | Apache-2.0 |
| Phiên bản đã đọc | `dfb907a02bba8152ca444717ca5d78747ccb4bec` (commit 2025-08-06) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE, pyproject.toml; chưa chạy upstream |
| Bảo trì | Ít hoạt động (commit cuối 2025-08-06) |
| Nhận định | Thư viện suy luận cho model TTS Kokoro-82M (open-weight, README nói trọng số Apache). Giấy phép trọng số trên Hugging Face **(chưa xác minh)**; repo đứng yên, không có CI. |
| Nguồn | [README.md](https://github.com/hexgrad/kokoro/blob/dfb907a02bba8152ca444717ca5d78747ccb4bec/README.md) · [LICENSE](https://github.com/hexgrad/kokoro/blob/dfb907a02bba8152ca444717ca5d78747ccb4bec/LICENSE) · [pyproject.toml](https://github.com/hexgrad/kokoro/blob/dfb907a02bba8152ca444717ca5d78747ccb4bec/pyproject.toml) |

<a id="ch-livekit-agents"></a>

### LiveKit Agents

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/livekit/agents |
| License | Apache-2.0 (mã); model turn detection: LiveKit Model License |
| Phiên bản đã đọc | `8b202a2abc49db9339b2e4ae3639293e58aeabfc` (commit 2026-11-23) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE, MODEL_LICENSE, NOTICE; chưa chạy upstream |
| Bảo trì | Đang hoạt động (commit 2026-11-23) |
| Nhận định | Framework Python dựng agent thời gian thực (STT-LLM-TTS/Realtime API, WebRTC, telephony, MCP, test framework). Model turn detection bị ràng buộc dùng với framework này; nhiều workflow (tests, evals, release-gate) chỉ biết tên. |
| Nguồn | [README.md](https://github.com/livekit/agents/blob/8b202a2abc49db9339b2e4ae3639293e58aeabfc/README.md) · [LICENSE](https://github.com/livekit/agents/blob/8b202a2abc49db9339b2e4ae3639293e58aeabfc/LICENSE) · [MODEL_LICENSE](https://github.com/livekit/agents/blob/8b202a2abc49db9339b2e4ae3639293e58aeabfc/MODEL_LICENSE) · [NOTICE](https://github.com/livekit/agents/blob/8b202a2abc49db9339b2e4ae3639293e58aeabfc/NOTICE) |

<a id="ch-llava-next"></a>

### LLaVA-NeXT

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/LLaVA-VL/LLaVA-NeXT |
| License | Apache-2.0 |
| Phiên bản đã đọc | `bce12e479bc4dfee2b9c50c88137b01ff51bd483` (commit 2026-06-15) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE, pyproject.toml; chưa chạy upstream |
| Bảo trì | Ít hoạt động (commit cuối 2026-06-15) |
| Nhận định | Mã LLaVA-NeXT/Video/Critic cho mô hình đa phương thức. Pipeline huấn luyện đã chuyển sang repo khác; dữ liệu và checkpoint chịu license gốc riêng theo README nên phải kiểm từng checkpoint. |
| Nguồn | [README.md](https://github.com/LLaVA-VL/LLaVA-NeXT/blob/bce12e479bc4dfee2b9c50c88137b01ff51bd483/README.md) · [LICENSE](https://github.com/LLaVA-VL/LLaVA-NeXT/blob/bce12e479bc4dfee2b9c50c88137b01ff51bd483/LICENSE) · [pyproject.toml](https://github.com/LLaVA-VL/LLaVA-NeXT/blob/bce12e479bc4dfee2b9c50c88137b01ff51bd483/pyproject.toml) |

<a id="ch-open-asr-leaderboard"></a>

### Open ASR Leaderboard

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/huggingface/open_asr_leaderboard |
| License | Apache-2.0 |
| Phiên bản đã đọc | `c4696193a333f7948cb113dc93bb54f661bd9a0b` (commit 2026-11-20) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE; chưa chạy upstream |
| Bảo trì | Đang hoạt động (commit 2026-11-20) |
| Nhận định | Khung đo ASR trung lập (short-form, long-form, multilingual) với bộ dữ liệu công khai trên Hugging Face. Tập riêng tư không công khai nên không tự tái lập được phần đó; kết quả bảng xếp hạng **(chưa xác minh)** ở đây. |
| Nguồn | [README.md](https://github.com/huggingface/open_asr_leaderboard/blob/c4696193a333f7948cb113dc93bb54f661bd9a0b/README.md) · [LICENSE](https://github.com/huggingface/open_asr_leaderboard/blob/c4696193a333f7948cb113dc93bb54f661bd9a0b/LICENSE) |

<a id="ch-picovoice-speech-to-text-benchmark"></a>

### Picovoice Speech-to-Text Benchmark

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/Picovoice/speech-to-text-benchmark |
| License | Apache-2.0 |
| Phiên bản đã đọc | `272be8f2244c10dfb2994f192bd6390982b17a5d` (commit 2026-11-16) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE; chưa chạy upstream |
| Bảo trì | Đang hoạt động (commit 2026-11-16) |
| Nhận định | Khung nhỏ đo WER, độ trễ, bộ nhớ trên LibriSpeech, TED-LIUM, Common Voice, MLS... Dùng khung đo được, nhưng bảng kết quả trong repo là số của nhà bán **(chưa xác minh)**. |
| Nguồn | [README.md](https://github.com/Picovoice/speech-to-text-benchmark/blob/272be8f2244c10dfb2994f192bd6390982b17a5d/README.md) · [LICENSE](https://github.com/Picovoice/speech-to-text-benchmark/blob/272be8f2244c10dfb2994f192bd6390982b17a5d/LICENSE) |

<a id="ch-pipecat"></a>

### Pipecat

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/pipecat-ai/pipecat |
| License | BSD-2-Clause |
| Phiên bản đã đọc | `218a7f83635639c6a36ed45747a6644fdc1eeeff` (commit 2026-11-22) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE, pyproject.toml; chưa chạy upstream |
| Bảo trì | Đang hoạt động (commit 2026-11-22) |
| Nhận định | Framework Python dựng agent thoại và đa phương thức với pipeline plugin (hơn 70 mục trong services), có thư mục evals. Rủi ro ở cấp tích hợp: mỗi provider có license/điều khoản riêng. |
| Nguồn | [README.md](https://github.com/pipecat-ai/pipecat/blob/218a7f83635639c6a36ed45747a6644fdc1eeeff/README.md) · [LICENSE](https://github.com/pipecat-ai/pipecat/blob/218a7f83635639c6a36ed45747a6644fdc1eeeff/LICENSE) · [pyproject.toml](https://github.com/pipecat-ai/pipecat/blob/218a7f83635639c6a36ed45747a6644fdc1eeeff/pyproject.toml) |

<a id="ch-qwen3-vl"></a>

### Qwen3-VL

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/QwenLM/Qwen3-VL |
| License | Apache-2.0 |
| Phiên bản đã đọc | `96588727e44c78b25ba03ea03b8e12f7e64fd0da` (commit 2026-01-30) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE; chưa chạy upstream |
| Bảo trì | Ít hoạt động (commit cuối 2026-01-30) |
| Nhận định | Repo mã, cookbook, evaluation, finetune cho Qwen3-VL (agent GUI, 2D/3D grounding, video dài). License từng checkpoint trên Hugging Face chưa đọc **(chưa xác minh)**; theo dõi model card thay vì repo. |
| Nguồn | [README.md](https://github.com/QwenLM/Qwen3-VL/blob/96588727e44c78b25ba03ea03b8e12f7e64fd0da/README.md) · [LICENSE](https://github.com/QwenLM/Qwen3-VL/blob/96588727e44c78b25ba03ea03b8e12f7e64fd0da/LICENSE) |
