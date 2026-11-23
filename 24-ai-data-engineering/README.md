# 24 · AI Data Engineering: Curation, Annotation & Synthetic Data

> Chất lượng model và RAG bắt đầu từ nguồn dữ liệu, quyền dùng, cách chia tập và lịch sử biến đổi. Mục này khảo sát 2/11/2026, đọc README, LICENSE, CI và đường mã được dẫn trong từng hồ sơ. Không chạy công cụ xử lý hay gửi dữ liệu vào dịch vụ bên ngoài; không có kết quả benchmark độc lập tại kho này.

## 1. Phạm vi và đường đi của dữ liệu

Mục này tập trung vào **dữ liệu cho AI**: thu thập có nguồn gốc, làm sạch, khử trùng, xây nhãn, sinh mẫu, chọn mẫu và đóng băng snapshot. Phân tích SQL/BI, data contract và lineage doanh nghiệp đã có ở [mục 15](../15-ai-for-data/README.md); parser/OCR ở [mục 26](../26-document-intelligence-ocr/README.md), chia đoạn và retrieval liên quan [mục 10](../10-local-llm-rag-memory/README.md); hậu huấn luyện ở [mục 25](../25-model-adaptation-post-training/README.md). Bộ công cụ ở đây không tự giải quyết quyền sử dụng nội dung, bảo vệ PII hay chất lượng nhãn.

| Công đoạn | Artifact nên bàn giao ở dự án tích hợp | Rủi ro chính |
|---|---|---|
| Nhập nguồn | URL/origin, ngày lấy, quyền dùng, source ID/hash | Nội dung truy cập được không có nghĩa được phép huấn luyện/phân phối |
| Chuẩn hoá / parse | Văn bản chuẩn hoá, vị trí nguồn, config parser và bản gốc có quyền lưu | Làm mất bảng, dấu tiếng Việt, đơn vị, context hoặc cấu trúc hội thoại |
| Lọc / khử trùng | Recipe, thống kê giữ/loại theo nhóm, cluster ID và lý do | Loại nhầm ngôn ngữ/miền hiếm; chọn bản trùng kém chất lượng |
| Gán nhãn / adjudication | Nhãn, hướng dẫn, người/phiên bản model gán, lịch sử sửa và trường hợp bất đồng | Một lần bấm “accept” không phải ground truth độc lập |
| Sinh dữ liệu | Model/prompt/seed, nguồn context, validator, provenance từng mẫu | Sinh sai có vẻ hợp lý; benchmark bị đưa vào prompt tạo dữ liệu |
| Chia tập | Group/time/source split, hash và báo cáo overlap | Chia ngẫu nhiên từng dòng nhưng cùng tài liệu/người lọt cả train/test |
| Phiên bản / phát hành | Snapshot ID, file hashes, schema/card, retention/deletion plan | Branch/tag thay đổi hoặc cache bị coi là snapshot bất biến |

## 2. Chọn theo vấn đề đang gặp

| Nhu cầu | Ứng viên đã đọc | Lựa chọn đối chiếu | Điều kiện quyết định |
|---|---|---|---|
| Lọc/khử trùng corpus text lớn | DataTrove | Data-Juicer | DataTrove chia pipeline rõ; Data-Juicer có recipe/operator nhiều loại dữ liệu; đo trên phân bố thật |
| Recipe đa phương thức và thử nhiều cách làm sạch | Data-Juicer | DataTrove + bước riêng theo modality | Dependency/model tải thêm, tài nguyên từng operator và khả năng tái lập recipe |
| Gán nhãn ảnh/audio/video/text/time series | Label Studio | Argilla cho feedback/record workflow | Định dạng export, vai trò, quality control cần có trong bản OSS hay bản thương mại |
| Chuyên gia đánh giá/cải thiện dataset LLM | Argilla | Label Studio + schema phù hợp | Argilla đã báo chỉ sửa lỗi; cần người duy trì và kế hoạch nâng cấp |
| Sinh dữ liệu và AI feedback theo pipeline | Distilabel | Operator sinh của Data-Juicer/DataTrove | Nhóm duy trì đã đổi; pin model/prompt và human review kết quả |
| Đánh dấu nhãn nghi sai / ngoại lệ để chuyên gia xem | Cleanlab | Thống kê/rule + human review trong hai công cụ annotation | Có out-of-sample probabilities/features phù hợp; không tự sửa nhãn theo dự đoán |
| Versioning dataset/model theo project ML | DVC | Manifest/hash trong hệ lưu trữ hiện có | Git giữ metadata, cache/remote giữ object; kiểm tải lại và quyền nội dung |
| Versioning data lake/object storage | lakeFS | DVC cho project riêng, hoặc snapshot/manifest trong storage hiện có | LakeFS hiện BUSL-1.1, cần đọc production grant trước chọn dùng |

Không công cụ nào trong bảng bảo đảm tự động “data sạch”. Kết hợp theo công đoạn; giữ một baseline đơn giản để biết operator thêm vào giúp chất lượng hay chỉ giảm số dòng.

## 3. Hồ sơ đọc mã

<a id="datatrove"></a>

### 3.1. DataTrove — pipeline khử trùng có thứ tự và giới hạn

| Thuộc tính | Giá trị |
|---|---|
| Repo / tác giả | [huggingface/datatrove](https://github.com/huggingface/datatrove) |
| Bằng chứng đọc | `4c488a135cc582b482df81895e631aadff2fa4c1` · commit 2026-10-27 · chưa archive khi đọc 2/11/2026 |
| ★ · license (2/11/2026) | 3,414 ★ (GitHub REST API); Apache-2.0 |
| Giá trị cốt lõi | Thư viện xử lý/lọc/khử trùng corpus text; block Reader/Filter/Writer cùng executor và pipeline nhiều bước. |
| Đường mã đã đọc | MinHash tách signature → bucket → cluster → filter. `MinhashDedupCluster` dùng union-find, giữ root theo thứ tự xử lý chứ không xếp hạng chất lượng. `LocalPipelineExecutor` tách thực thi khỏi step. |
| CI đã đọc | `testing.yml` kiểm Ruff và pytest Python 3.11–3.13; môi trường CPU loại một số GPU dependency. Không coi đây là benchmark corpus hay kiểm path endpoint từ xa. |
| Tích hợp | Dùng DataTrove ở dự án xử lý dữ liệu, lưu recipe/n-gram/hash parameters và input/output IDs; thử trên mẫu có bản gần trùng, biến thể dấu và nguồn lặp. |
| Hạn chế / rủi ro | MinHash là xấp xỉ; ngưỡng và tokenizer ảnh hưởng false positive/negative. Source cảnh báo lọc chất lượng sau dedup có thể loại bản được giữ trong khi các bản tốt hơn đã mất; đặt bước lọc phù hợp trước khi tạo signature và đo ảnh hưởng. |
| Bài học kiến trúc | Thứ tự operator là một phần hợp đồng dữ liệu; lưu cả lý do loại và mapping cluster để audit, không chỉ số dòng cuối. |
| Thay thế / liên quan | Data-Juicer cho recipe nhiều modality; Distilabel khi trọng tâm là generation; mục 10 và 25. |

**Nguồn hồ sơ:** [README](https://github.com/huggingface/datatrove/blob/4c488a135cc582b482df81895e631aadff2fa4c1/README.md) · [LICENSE](https://github.com/huggingface/datatrove/blob/4c488a135cc582b482df81895e631aadff2fa4c1/LICENSE) · [MinHash và thứ tự lọc](https://github.com/huggingface/datatrove/blob/4c488a135cc582b482df81895e631aadff2fa4c1/src/datatrove/pipeline/dedup/minhash.py) · [executor](https://github.com/huggingface/datatrove/blob/4c488a135cc582b482df81895e631aadff2fa4c1/src/datatrove/executor/local.py) · [CI](https://github.com/huggingface/datatrove/blob/4c488a135cc582b482df81895e631aadff2fa4c1/.github/workflows/testing.yml).

<a id="data-juicer"></a>

### 3.2. Data-Juicer — recipe dữ liệu là thành phần có phiên bản

| Thuộc tính | Giá trị |
|---|---|
| Repo / tác giả | [datajuicer/data-juicer](https://github.com/datajuicer/data-juicer) |
| Bằng chứng đọc | `09178e1e0ac76cfbfe11232d66244e1ccc5add6f` · commit 2026-11-02 · chưa archive khi đọc 2/11/2026 |
| ★ · license (2/11/2026) | 7,208 ★ (GitHub REST API); Apache-2.0; giữ attribution các phần dẫn xuất trong LICENSE |
| Giá trị cốt lõi | Operator và recipe xử lý/lọc/tổng hợp dữ liệu text, ảnh, audio, video; so sánh thay đổi recipe thay vì chỉ đổi model. Canonical hiện ở `datajuicer/data-juicer`, không còn lấy namespace ModelScope làm định danh chính. |
| Đường mã đã đọc | `dj_dataset.py` điều phối xử lý dataset; `DocumentMinhashDeduplicator` công khai lựa chọn tokenization, window, permutation và Jaccard threshold. Một ngưỡng chung không chứng minh phù hợp tiếng Việt. |
| CI đã đọc | `unit-test.yml` là workflow regression GPU chạy theo lịch/manual, có nhánh standalone/distributed. Không suy rằng toàn bộ bài regression được chạy cho mọi pull request; cần đọc thêm workflow partial khi tích hợp. |
| Tích hợp | Phiên bản hoá YAML recipe, operator config, model/tokenizer tải thêm và input snapshot; xuất thống kê từng step theo ngôn ngữ/nguồn/lớp. Xem paper gốc như thiết kế, không dùng số cải thiện ở paper làm dự báo dự án khác. |
| Hạn chế / rủi ro | Operator dùng LLM/perplexity/embedding có thêm chi phí và model license; dependency cho nhiều modality làm môi trường lớn. Nhãn Apache của toolkit không áp sang dataset hay model tải về. |
| Bài học kiến trúc | Tách processing, phân tích thống kê và đánh giá downstream; recipe phải được đo cả tỷ lệ giữ lại lẫn tác động lên tác vụ. |
| Thay thế / liên quan | DataTrove cho corpus text, Distilabel cho generation/feedback, Label Studio/Argilla cho chuyên gia; mục 15, 18 và 25. |

**Nguồn hồ sơ:** [README](https://github.com/datajuicer/data-juicer/blob/09178e1e0ac76cfbfe11232d66244e1ccc5add6f/README.md) · [LICENSE và attribution](https://github.com/datajuicer/data-juicer/blob/09178e1e0ac76cfbfe11232d66244e1ccc5add6f/LICENSE) · [dataset processing](https://github.com/datajuicer/data-juicer/blob/09178e1e0ac76cfbfe11232d66244e1ccc5add6f/data_juicer/core/data/dj_dataset.py) · [dedup parameters](https://github.com/datajuicer/data-juicer/blob/09178e1e0ac76cfbfe11232d66244e1ccc5add6f/data_juicer/ops/deduplicator/document_minhash_deduplicator.py) · [regression CI](https://github.com/datajuicer/data-juicer/blob/09178e1e0ac76cfbfe11232d66244e1ccc5add6f/.github/workflows/unit-test.yml).

<a id="label-studio"></a>

### 3.3. Label Studio — nhãn người và prediction phải phân biệt được

| Thuộc tính | Giá trị |
|---|---|
| Repo / tác giả | [HumanSignal/label-studio](https://github.com/HumanSignal/label-studio) |
| Bằng chứng đọc | `e94d5189c77a0e92732014bea3a5fee003d946d9` · commit 2026-11-02 · chưa archive khi đọc 2/11/2026 |
| ★ · license (2/11/2026) | 28,612 ★ (GitHub REST API); Apache-2.0 (bản mã được đọc) |
| Giá trị cốt lõi | UI gán nhãn nhiều loại dữ liệu, định dạng task/result có cấu trúc và export phục vụ training/eval. |
| Đường mã đã đọc | `tasks/models.py` tách `Annotation` với `Prediction`; annotation có `completed_by`, `ground_truth`, trạng thái bỏ qua và thời gian. Một cờ ground-truth vẫn là dữ liệu ứng dụng, không phải chứng minh nhãn đúng. |
| CI đã đọc | `tests.yml` định nghĩa kiểm backend; đọc workflow và model dữ liệu, chưa chạy UI/export hay kiểm quyền người dùng thực tế. |
| Cấu hình cần kiểm | Settings mặc định `COLLECT_ANALYTICS` bật; `DISABLE_SIGNUP_WITHOUT_LINK` mặc định false; SSRF protection mặc định true. Dự án tích hợp cần quyết định analytics, kiểm quyền đăng ký và nguồn truy cập, không suy “self-host” là hoàn toàn offline. |
| Tích hợp | Thiết kế hướng dẫn/nhãn và task ID trước; lưu source ID, revision nhãn và export hash. Tách prediction hỗ trợ với nhãn đã được chuyên gia duyệt; kiểm feature cần dùng thuộc OSS hay sản phẩm thương mại. |
| Hạn chế / rủi ro | Dữ liệu annotation có thể chứa PII; cấu hình storage, ML backend và analytics tạo luồng dữ liệu riêng. Chưa audit toàn bộ mạng/telemetry và phân quyền **(chưa xác minh)**. |
| Bài học kiến trúc | Lưu người, thời điểm, guideline revision và lý do bất đồng; tách “đã annotate” khỏi “đã adjudicate”. |
| Thay thế / liên quan | Argilla cho feedback LLM, Cleanlab cho danh sách cần xem lại, Data-Juicer/DataTrove cho preprocessing; mục 12, 18 và 25. |

**Nguồn hồ sơ:** [README](https://github.com/HumanSignal/label-studio/blob/e94d5189c77a0e92732014bea3a5fee003d946d9/README.md) · [LICENSE](https://github.com/HumanSignal/label-studio/blob/e94d5189c77a0e92732014bea3a5fee003d946d9/LICENSE) · [annotation/prediction](https://github.com/HumanSignal/label-studio/blob/e94d5189c77a0e92732014bea3a5fee003d946d9/label_studio/tasks/models.py) · [settings mặc định](https://github.com/HumanSignal/label-studio/blob/e94d5189c77a0e92732014bea3a5fee003d946d9/label_studio/core/settings/base.py) · [CI](https://github.com/HumanSignal/label-studio/blob/e94d5189c77a0e92732014bea3a5fee003d946d9/.github/workflows/tests.yml).

<a id="argilla"></a>

### 3.4. Argilla — workflow feedback có điều kiện bảo trì

| Thuộc tính | Giá trị |
|---|---|
| Repo / tác giả | [argilla-io/argilla](https://github.com/argilla-io/argilla) |
| Bằng chứng đọc | `5338519accb13ae422f8bf9c0642651c249c49af` · commit 2025-08-05 · chưa archive khi đọc 2/11/2026 |
| ★ · license (2/11/2026) | 5,191 ★ (GitHub REST API); Apache-2.0 |
| Giá trị cốt lõi | Cộng tác giữa kỹ sư và chuyên gia để tạo dataset; record có response, trạng thái, metadata và vector hỗ trợ lựa chọn/review. |
| Đường mã đã đọc | Model server tách `Record`, `Response`, `Dataset` và metadata/vector; model client dataset giữ hợp đồng dữ liệu. Đây là nền lưu workflow, không tự thay thế kiểm chất lượng nhãn. |
| Bảo trì thực tế | README đầu file ghi tác giả gốc đã chuyển dự án, không thêm feature, vẫn cam kết bugfix/patch và tìm người duy trì. HEAD mặc định đã đọc có ngày 5/8/2025 dù `pushed_at` repo mới hơn; không dùng pushed-at làm bằng chứng feature đang phát triển. |
| CI đã đọc | `argilla.yml` định nghĩa kiểm Python/package; còn các workflow frontend/server riêng. Chưa chạy kiểm, chưa xác minh lịch release hỗ trợ dài hạn **(chưa xác minh)**. |
| Tích hợp | Phù hợp khi workflow hiện có cần human feedback có schema; trước chọn mới cần xác định người duy trì, export/backup và đường chuyển dữ liệu. Giữ schema questions/responses, guideline và revision khi export. |
| Hạn chế / rủi ro | Công cụ ổn định không bảo đảm dependency/web stack được vá đúng nhu cầu; đừng xếp ngang công cụ đang thêm tính năng chỉ vì chưa archive. |
| Bài học kiến trúc | Trạng thái bảo trì là dữ kiện nhiều chiều: archive, HEAD, release, tuyên bố maintainer và khả năng export; không chỉ một cờ “active”. |
| Thay thế / liên quan | Label Studio cho annotation đa loại, Distilabel cho AI feedback sinh tự động, Cleanlab để ưu tiên review; mục 07 và 25. |

**Nguồn hồ sơ:** [tuyên bố bảo trì](https://github.com/argilla-io/argilla/blob/5338519accb13ae422f8bf9c0642651c249c49af/README.md) · [LICENSE](https://github.com/argilla-io/argilla/blob/5338519accb13ae422f8bf9c0642651c249c49af/LICENSE) · [server schema](https://github.com/argilla-io/argilla/blob/5338519accb13ae422f8bf9c0642651c249c49af/argilla-server/src/argilla_server/models/database.py) · [client dataset](https://github.com/argilla-io/argilla/blob/5338519accb13ae422f8bf9c0642651c249c49af/argilla/src/argilla/_models/_dataset.py) · [CI](https://github.com/argilla-io/argilla/blob/5338519accb13ae422f8bf9c0642651c249c49af/.github/workflows/argilla.yml).

<a id="distilabel"></a>

### 3.5. Distilabel — sinh dữ liệu cần provenance ngoài cache

| Thuộc tính | Giá trị |
|---|---|
| Repo / tác giả | [argilla-io/distilabel](https://github.com/argilla-io/distilabel) |
| Bằng chứng đọc | `313fac85b1a2472dd88db1a31c2b754599f46476` · commit 2025-12-15 · chưa archive khi đọc 2/11/2026 |
| ★ · license (2/11/2026) | 3,447 ★ (GitHub REST API); Apache-2.0 |
| Giá trị cốt lõi | Pipeline synthetic data và AI feedback có step, batch và khả năng tiếp tục công việc từ cache. |
| Đường mã đã đọc | `BasePipeline.run(use_cache=True)` quản lý stage/batch state; pipeline signature mô tả bước/kết nối, lớp local phụ trách execution. Cache hỗ trợ resume, không tự là model/dataset provenance hoàn chỉnh. |
| Bảo trì thực tế | README ghi tác giả gốc đã chuyển dự án; một nhóm cộng đồng nhận duy trì, khuyến nghị nhánh `develop` cho bản sửa mới. Hồ sơ này đọc HEAD nhánh mặc định `main` ngày 15/12/2025, không gán thay mọi trạng thái của `develop`. |
| CI đã đọc | `test.yml` chạy lint, unit/integration trên Python 3.9–3.12; sự tồn tại của CI không chứng minh model API bên ngoài cho kết quả ổn định. |
| Tích hợp | Lưu generator/judge provider + model revision, prompt hash, input source/split, sampling config, chi phí, validator và phiên bản người duyệt. Chỉ cho dữ liệu đã kiểm vào tập training; held-out cuối không dùng để sinh hoặc chấm/chọn mẫu. |
| Hạn chế / rủi ro | LLM-as-judge và generator có thể cùng thiên lệch; cache giữ được output cũ nhưng không bảo đảm lần gọi mới tái lập. Điều khoản provider/dataset vẫn áp dụng độc lập. |
| Bài học kiến trúc | Sinh mẫu và chấp nhận mẫu là hai bước khác nhau; lưu cả mẫu bị loại và lý do để phát hiện lọc thiên lệch. |
| Thay thế / liên quan | Data-Juicer/DataTrove cho bước generation trong pipeline dữ liệu; Argilla/Label Studio cho human review; mục 07, 17 và 25. |

**Nguồn hồ sơ:** [tuyên bố bảo trì](https://github.com/argilla-io/distilabel/blob/313fac85b1a2472dd88db1a31c2b754599f46476/README.md) · [LICENSE](https://github.com/argilla-io/distilabel/blob/313fac85b1a2472dd88db1a31c2b754599f46476/LICENSE) · [signature/cache/stage](https://github.com/argilla-io/distilabel/blob/313fac85b1a2472dd88db1a31c2b754599f46476/src/distilabel/pipeline/base.py) · [local executor](https://github.com/argilla-io/distilabel/blob/313fac85b1a2472dd88db1a31c2b754599f46476/src/distilabel/pipeline/local.py) · [CI](https://github.com/argilla-io/distilabel/blob/313fac85b1a2472dd88db1a31c2b754599f46476/.github/workflows/test.yml).

<a id="lakefs"></a>

### 3.6. lakeFS — dữ liệu có branch/commit, license hiện là BUSL

| Thuộc tính | Giá trị |
|---|---|
| Repo / tác giả | [treeverse/lakeFS](https://github.com/treeverse/lakeFS) |
| Bằng chứng đọc | `a247a81d32f05aca22ced14536ca0e6cfdaa1794` · commit 2026-11-01 · chưa archive khi đọc 2/11/2026 |
| ★ · license (2/11/2026) | 5,575 ★ (GitHub REST API); BUSL-1.1; source-available, không phải license mã nguồn mở OSI |
| Giá trị cốt lõi | Versioning data lake qua giao diện kiểu Git; branch, commit và rollback hỗ trợ môi trường thử và Write–Audit–Publish trên object storage. |
| Đường mã đã đọc | `pkg/catalog/catalog.go` định nghĩa thao tác repository/branch/commit/merge và kiểm định danh trước khi gọi lớp lưu trữ. CI có Go test, validator và web UI test. |
| License thật | LICENSE cho lakeFS 1.87.0 là BUSL-1.1. Production grant yêu cầu bản không sửa và chỉ dùng nội bộ tổ chức; không cung cấp chức năng cho bên thứ ba. Một phiên bản chuyển Apache-2.0 sau 4 năm kể từ khi phát hành dưới license này. Đọc điều khoản đầy đủ trước khi nhúng/fork/host. |
| Tích hợp | Có thể dùng để đóng băng snapshot training và branch dữ liệu trước khi promote. Dataset manifest phải tham chiếu commit bất biến, không chỉ tên branch; quyền nội dung, retention và quyền object storage vẫn phải quản lý riêng. |
| Hạn chế / rủi ro | Snapshot khôi phục trạng thái dữ liệu không khôi phục model/provider đã thay đổi hay giấy phép đã hết hạn. Chi phí storage/GC/metadata và quyền xóa dữ liệu cần thiết kế ở dự án dùng, chưa đo tại đây. |
| Bài học kiến trúc | Chỉ promote snapshot sau data gates; giữ một đường rollback dữ liệu có định danh. Tách tính hữu ích kỹ thuật khỏi quyền triển khai theo license hiện hành. |
| Thay thế / liên quan | DVC cho project ML cần license permissive; snapshot bất biến + file manifest/hash là baseline; DataTrove/Data-Juicer xử lý nội dung, không thay lakeFS; mục 15 và 25. |

**Nguồn hồ sơ:** [README và license scope](https://github.com/treeverse/lakeFS/blob/a247a81d32f05aca22ced14536ca0e6cfdaa1794/README.md) · [BUSL-1.1 đầy đủ](https://github.com/treeverse/lakeFS/blob/a247a81d32f05aca22ced14536ca0e6cfdaa1794/LICENSE) · [catalog API](https://github.com/treeverse/lakeFS/blob/a247a81d32f05aca22ced14536ca0e6cfdaa1794/pkg/catalog/catalog.go) · [CI](https://github.com/treeverse/lakeFS/blob/a247a81d32f05aca22ced14536ca0e6cfdaa1794/.github/workflows/test.yaml).

<a id="cleanlab"></a>

### 3.7. Cleanlab — xếp hạng dữ liệu cần xem lại, không tự định nghĩa sự thật

| Thuộc tính | Giá trị |
|---|---|
| Repo / tác giả | [cleanlab/cleanlab](https://github.com/cleanlab/cleanlab) |
| Bằng chứng đọc | `750625747de1b26d8530954f51f0530bd0b51d3c` · commit 2026-01-13 · chưa archive khi đọc 2/11/2026 |
| ★ · license (2/11/2026) | 11,728 ★ (GitHub REST API); Apache-2.0 |
| Giá trị cốt lõi | Công cụ data-centric AI tìm ứng viên lỗi nhãn, ngoại lệ và vấn đề dataset từ model probabilities/features; có Datalab và hàm chuyên biệt theo tác vụ. |
| Đường mã đã đọc | `find_label_issues()` trả mask hoặc thứ tự ứng viên theo điểm; tài liệu ngay trong source khuyến nghị `pred_probs` ngoài mẫu và cross-validation. Datalab gom issue report theo cấu hình. |
| CI / bảo trì | `ci.yml` định nghĩa kiểm thư viện; HEAD ngày 13/1/2026 và repo chưa archive tại 2/11. Chưa có bằng chứng đủ để gọi dự án đã ngừng, cũng không nên mặc định nhịp phát triển nhanh. |
| Tích hợp | Dùng probabilities từ mô hình không học trên chính mẫu đang chấm; đưa ứng viên cho người duyệt, ghi quyết định và đánh giá lại trên held-out. Tách bước phát hiện vấn đề khỏi sửa hoặc loại dữ liệu. |
| Hạn chế / rủi ro | Confidence phụ thuộc model, calibration và phân bố; nhãn hiếm/khác thường có thể đúng. Không lấy mức độ không đồng ý với model làm ground truth, không dùng report để khẳng định dữ liệu đã sạch toàn bộ. |
| Bài học kiến trúc | Cổng chất lượng nên xuất **bằng chứng + danh sách review**, cho phép chuyên gia giữ lại ngoại lệ và theo dõi tác động của quyết định. |
| Thay thế / liên quan | Rule/statistics là baseline; Label Studio/Argilla để adjudicate, Data-Juicer/DataTrove để áp recipe đã chấp nhận; mục 07, 15, 18 và 25. |

**Nguồn hồ sơ:** [README](https://github.com/cleanlab/cleanlab/blob/750625747de1b26d8530954f51f0530bd0b51d3c/README.md) · [LICENSE](https://github.com/cleanlab/cleanlab/blob/750625747de1b26d8530954f51f0530bd0b51d3c/LICENSE) · [out-of-sample và issue ranking](https://github.com/cleanlab/cleanlab/blob/750625747de1b26d8530954f51f0530bd0b51d3c/cleanlab/filter.py) · [Datalab](https://github.com/cleanlab/cleanlab/blob/750625747de1b26d8530954f51f0530bd0b51d3c/cleanlab/datalab/datalab.py) · [CI](https://github.com/cleanlab/cleanlab/blob/750625747de1b26d8530954f51f0530bd0b51d3c/.github/workflows/ci.yml).

<a id="dvc"></a>

### 3.8. DVC — dataset/model lớn gắn với lịch sử Git

| Thuộc tính | Giá trị |
|---|---|
| Repo / tác giả | [treeverse/dvc](https://github.com/treeverse/dvc) |
| Bằng chứng đọc | `56e59829512ff134aa269099a2099587b810b4dd` · commit 2026-08-06 · chưa archive khi đọc 2/11/2026 |
| ★ · license (2/11/2026) | 15,958 ★ (GitHub REST API); Apache-2.0 |
| Giá trị cốt lõi | Version dữ liệu/model bằng metadata trong Git và cache/remote cho artifact lớn; pipeline nối dependencies, params, command và outputs. Canonical hiện là `treeverse/dvc` (URL `iterative/dvc` chuyển hướng). |
| Đường mã đã đọc | `repo/reproduce.py` lập thứ tự chạy các stage theo dependency graph; `stage/run.py` có đường gọi subprocess cho command. Reproduce là thực thi pipeline, không phải chỉ đọc metadata. |
| CI / trạng thái | `tests.yaml` chia test theo nền tảng/nhóm; LICENSE giữ Apache-2.0. HEAD đã đọc ngày 6/8/2026, khác pushed-at toàn repo; không suy nhịp bảo trì từ lần push nhánh khác. |
| Tích hợp | Phù hợp nhóm cần dataset/model + code + params trong cùng lịch sử Git. Giữ metadata/lock cùng Git commit; kiểm quyền truy cập remote, hash/cache còn tải lại được và môi trường chạy. Chỉ reproduce recipe đã review trong môi trường phù hợp. |
| Hạn chế / rủi ro | Git commit metadata không mang theo toàn bộ object cache; mất remote/credential/retention có thể làm không tái lập được. Repro chạy command nên không dùng pipeline nguồn lạ như một thao tác read-only. |
| So với lakeFS | DVC theo dự án ML/working tree/experiment; lakeFS theo data lake/object namespace và branch dùng chung. DVC giữ Apache, lakeFS hiện BUSL; cùng chủ không có nghĩa cùng license hay cùng mô hình vận hành. |
| Bài học kiến trúc | Phiên bản code và con trỏ dữ liệu phải được phát hành cùng nhau; “reproducible” cần cả artifact khả dụng lẫn môi trường và command có thể kiểm. |
| Thay thế / liên quan | lakeFS khi cần branch dữ liệu quy mô hệ thống; manifest/hash bất biến cho baseline nhỏ; DataTrove/Data-Juicer xử lý nội dung; mục 13, 15 và 25. |

**Nguồn hồ sơ:** [README](https://github.com/treeverse/dvc/blob/56e59829512ff134aa269099a2099587b810b4dd/README.rst) · [LICENSE](https://github.com/treeverse/dvc/blob/56e59829512ff134aa269099a2099587b810b4dd/LICENSE) · [dependency graph/reproduce](https://github.com/treeverse/dvc/blob/56e59829512ff134aa269099a2099587b810b4dd/dvc/repo/reproduce.py) · [thực thi command](https://github.com/treeverse/dvc/blob/56e59829512ff134aa269099a2099587b810b4dd/dvc/stage/run.py) · [CI](https://github.com/treeverse/dvc/blob/56e59829512ff134aa269099a2099587b810b4dd/.github/workflows/tests.yaml).

## 4. Chuẩn gốc, data card và hợp đồng dữ liệu

| Nguồn | Vai trò | Bằng chứng áp dụng nên có |
|---|---|---|
| [Datasheets for Datasets](https://arxiv.org/abs/1803.09010) | Tài liệu về mục đích, thành phần, thu thập, xử lý, cách dùng và hạn chế | Card ghi nguồn/người chịu trách nhiệm, nhóm thiếu phủ, quyền dùng, retention và điều kiện ngoài phạm vi |
| [Croissant 1.0](https://docs.mlcommons.org/croissant/docs/croissant-spec.html) | Metadata dataset máy đọc được: resource, cấu trúc record/field và cách tải | Mô tả khớp artifact thực, references/hashes và kiểm bằng implementation phù hợp; metadata không chứng nhận nội dung đúng |
| [W3C DCAT 3](https://www.w3.org/TR/vocab-dcat-3/) | Từ vựng catalog: dataset/distribution, versioning, checksum và dataset series | Định danh dataset khác định danh một bản export; quan hệ phiên bản có thể truy vết |
| [W3C PROV](https://www.w3.org/TR/prov-overview/) | Mô hình entity–activity–agent cho nguồn gốc và biến đổi | Input/output ID, recipe/code/config revision, người/model tạo hoặc duyệt, thời điểm |
| [Confident Learning](https://arxiv.org/abs/1911.00068) | Phương pháp ước lượng vấn đề nhãn từ phân bố nhãn và dự đoán | Đặc tả nguồn probabilities, giả định và human review; không coi điểm nghi ngờ là kết luận chắc chắn |
| [Data-Juicer paper](https://arxiv.org/abs/2309.02033) | Recipe/operator và vòng phản hồi giữa xử lý dữ liệu với kết quả model | So baseline/recipe trên cùng task/split; giữ kết quả của cả nhóm tốt lên lẫn nhóm giảm |

Croissant 1.0 là phiên bản của trang đặc tả đã đọc, không phải khẳng định không có bản mới hơn. PROV-Overview là tài liệu tổng quan dạng W3C Note; các đặc tả PROV-DM/PROV-O được nó liên kết có trạng thái riêng. DCAT 3 là W3C Recommendation ngày 22/8/2024. Chọn phần cần trao đổi metadata; không bắt dự án nhỏ triển khai toàn bộ hệ ontology.

**Dataset manifest tối thiểu ở dự án tích hợp:** dataset ID/version; source ID + quyền dùng; hashes; schema; ngôn ngữ/nhóm phủ; preprocessing/parser/config revision; split theo nhóm/thời gian; generator/judge/annotator provenance; chính sách PII và xoá; thống kê loại/giữ; reviewer và các giới hạn đã biết. Với synthetic data, phân biệt license của toolkit, model, dữ liệu gốc và quyền đầu ra của provider.

## 5. Cổng kiểm có thể đo và quy trình human review

| Cổng | Phép kiểm / artifact | Điều kiện chặn hoặc chuyển review |
|---|---|---|
| Nguồn và quyền | Origin, license/terms, consent nếu cần, thời gian lấy và phạm vi sử dụng | Không rõ quyền hoặc nguồn tổng hợp chỉ dẫn lại không có provenance |
| Schema / encoding | Trường bắt buộc, type, NFC/Unicode, null/empty, đơn vị, tool-call JSON theo schema | Text lỗi dấu, nhãn ngoài taxonomy, mất bảng/đơn vị hoặc role hội thoại sai |
| PII / secrets | Bộ dò thích hợp + lấy mẫu người duyệt, log số loại được che/xoá | Dữ liệu nhạy cảm vượt mục đích; detector đơn lẻ chưa đủ xác nhận không có PII |
| Dedup / leakage | Exact hash + near-duplicate/cluster; split theo source/document/person/time | Cùng cluster/định danh nhóm lọt train–validation–test; benchmark bị đưa vào generation context |
| Chất lượng lọc | So phân bố trước/sau theo ngôn ngữ, miền, nhãn; lấy mẫu retained/rejected | Chỉ tăng tỷ lệ lọc nhưng làm mất nhóm tiếng Việt/nhãn hiếm quan trọng |
| Nhãn người | Guideline version, pilot, overlap để đo agreement, adjudication và audit trail | Không rõ định nghĩa nhãn; bất đồng chưa xử lý hoặc người duyệt chỉ chấp nhận prediction |
| Synthetic data | Generator/judge revision, validator, human sample review, diversity/overlap report | Sai sự thật/logic, lặp mẫu, cùng model tự sinh tự chấm không có kiểm khác |
| Phiên bản | Dataset snapshot/commit + hashes, recipe/dependency pin, export round-trip | Chỉ có URL nhánh mutable, không tải lại được artifact hoặc export mất trường |
| Hiệu quả downstream | Baseline và recipe trên cùng held-out, metric theo nhóm, chi phí xử lý | Data score tăng nhưng task quality giảm, hoặc tối ưu recipe trực tiếp theo test cuối |

**Cách human review tham khảo:** viết hướng dẫn có ví dụ đúng/sai/khó; thử trên mẫu nhỏ; cho hai người chấm phần overlap; adjudicator giải quyết bất đồng; lưu bản trước/sau và lý do. Tỷ lệ agreement, số mẫu và ngưỡng chấp nhận do dự án xác định theo tác vụ/rủi ro, không có một con số chuẩn cho mọi dataset. Máy ưu tiên mẫu cần xem; người duyệt phải được phép giữ ngoại lệ và bác prediction.

**Phòng leakage theo vòng đời:** gom nhóm/đặt ranh giới đánh giá trước khi tạo biến thể hoặc synthetic descendants; propagate source/cluster ID sang mọi bản dẫn xuất; chỉ dùng training partition cho generation/selection; held-out cuối không dùng để chỉnh filter, prompt generator hay judge. Kiểm lại overlap ở bản export cuối vì nhiều pipeline có thể tái đưa bản trùng vào sau bước dedup. Nếu không biết nguồn training của base model, chỉ có thể giảm nguy cơ contamination, không khẳng định đã loại hoàn toàn **(chưa xác minh)**.

## 6. Stack ghép với các mục khác

1. Dự án tích hợp lập dataset card/manifest và quyền dùng; [mục 15](../15-ai-for-data/README.md) cho data contract/lineage, [mục 12](../12-ai-security-guardrails/README.md) cho threat model và dữ liệu nhạy cảm.
2. Parser/OCR của [mục 26](../26-document-intelligence-ocr/README.md) giữ mapping về nguồn; DataTrove hoặc Data-Juicer làm recipe có revision, log tác động từng step.
3. Label Studio/Argilla thu nhãn chuyên gia; Cleanlab đưa ứng viên cần xem lại. Distilabel/generator là nhánh riêng đi qua validator và review trước khi nhập vào tập chấp nhận.
4. Snapshot được đóng băng bằng hệ versioning phù hợp license hoặc manifest/hash bất biến. Chỉ promote sau schema, leakage, PII và chất lượng theo nhóm.
5. [Mục 07](../07-eval-observability/README.md) giữ tập kiểm không tham gia tối ưu recipe; [mục 18](../18-vietnam-community/README.md) đối chiếu nhóm tiếng Việt; [mục 25](../25-model-adaptation-post-training/README.md) nhận dataset đã chấp nhận cùng provenance.

**Trần được nâng:** kho nối được nguồn → recipe → nhãn → snapshot → tác vụ đo được. Tốc độ parser, tỷ lệ dedup hoặc số sample synthetic không còn được coi là đại diện đầy đủ cho chất lượng dữ liệu. Chưa chạy pipeline thực, chưa benchmark tiếng Việt, chưa xác minh mọi model/dataset license được dependency tải **(chưa xác minh)**.

## 6b. Nâng trần 4/11/2026: dataset phát hành phải khôi phục và kiểm lại được

**Trần hiện tại:** §5 đã có schema, PII, group split và chống leakage. Xưởng còn thiếu cổng **tải lại artifact từ môi trường sạch**, và hợp đồng thu hồi dữ liệu khi một nguồn/nhãn/consent không còn hợp lệ. Một lockfile đẹp không chứng minh object remote còn tồn tại hoặc recipe tái tạo được cùng dữ liệu.

<a id="dvc-factory-artifact"></a>

### 6b.1 DVC: phân biệt lấy lại object với chạy lại pipeline

Đọc mã/LICENSE/CI **2026-11-04** tại `56e59829512ff134aa269099a2099587b810b4dd`, Apache-2.0; SHA trùng phạm vi khảo sát trước, đây là đọc sâu cơ chế chứ không phải công bố release mới. Chưa chạy DVC, tải dataset hay huấn luyện.

`dvc/repo/pull.py` gọi `fetch` rồi `checkout`; `allow_missing` mặc định false nhưng caller có thể truyền khác. Cổng nghiệm thu phải giữ điều kiện không bỏ qua object thiếu và kiểm dữ liệu dùng được sau checkout. `dvc/repo/reproduce.py` điều phối stage dependency, có đường run-cache và xử lý lỗi stage. Lấy object từ remote, tái sử dụng cache và thực thi lại recipe là ba phép kiểm khác nhau; không ghi “reproduced” chỉ vì `pull` thành công. `status.py` mô tả cả trạng thái missing/new/deleted; trạng thái working tree không thay kiểm quyền dùng dữ liệu.

| Lựa chọn | Bài toán phù hợp | Cổng riêng cần giữ |
|---|---|---|
| DVC + Git metadata | Dataset/model theo từng project và recipe | Clone/cache sạch, tải đúng object, hashes/manifest, schema và khả năng đọc; pin môi trường khi thử reproduce |
| [lakeFS](#lakefs) | Branch/commit trên data lake dùng chung | Production grant BUSL cần kiểm theo phiên bản; permission và retention của object store vẫn riêng |
| Object store bất biến + manifest | Pipeline đơn giản, muốn ít dependency | Tự giữ checksum, source lineage và quyền truy cập; không mặc định có dependency DAG |
| [DataTrove](#datatrove) / [Data-Juicer](#data-juicer) | Biến đổi/lọc/khử trùng corpus | Thống kê theo nhóm và downstream holdout; các công cụ này không thay artifact registry/versioning |

### 6b.2 Cổng promote dữ liệu cho xưởng

| Thời điểm | Bằng chứng máy đọc | Negative case / điều kiện chặn |
|---|---|---|
| Trước xử lý | Source manifest: origin ID, quyền dùng, revision, hash, retention và nguồn consent nếu áp dụng | Không xác định được phạm vi sử dụng; source ID bị mất sau parse |
| Sau biến đổi | Input/output lineage, recipe/dependency/model revisions, số lượng theo source/nhóm, lý do loại | Mất một ngôn ngữ/tenant/nhóm hiếm nhưng tổng số dòng vẫn hợp lệ |
| Trước split | Cluster/group/time keys được truyền qua mọi bản dẫn xuất | Một source và synthetic descendant lọt hai partition; held-out dùng để chọn filter |
| Trước promote | Schema/PII/leakage/downstream reports và các case không kết luận được | Chỉ data score tăng mà task quality giảm; quyền truy cập của CI rộng hơn mục đích |
| Sau lưu trữ | Receipt tải từ remote vào môi trường sạch, checksum, record count và representative reader test | Cache local che object thiếu; `allow_missing` hoặc skip làm kết quả xanh giả |
| Khi thu hồi | Source → derived records → export/model/index versions bị ảnh hưởng, quyết định giữ/xoá và biên bản kiểm | Chỉ xoá source nhưng bản dẫn xuất/index/backup còn truy cập; nhầm rollback với xoá dữ liệu |

Đường đi tham khảo: source manifest → xử lý có thống kê theo nhóm → snapshot/version bất biến → tải lại và đọc từ môi trường sạch → promote đúng revision sang [mục 10](../10-local-llm-rag-memory/README.md), [25](../25-model-adaptation-post-training/README.md), [26](../26-document-intelligence-ocr/README.md). Khi dữ liệu bị thu hồi, xác định cả artifact đã phát hành và dữ liệu sao lưu; yêu cầu xoá khỏi weights sau training cần cơ chế/đánh giá riêng, không được hứa “đã quên” chỉ từ việc xoá file.

CI DVC ở SHA này có matrix OS/Python và đặt `DVC_NO_ANALYTICS` ở các job được đọc. Điều đó cho thấy cấu hình từng job quan trọng; chưa audit toàn bộ telemetry runtime của DVC hoặc dịch vụ remote. Các ngưỡng quyền riêng tư, coverage nhóm và chất lượng do dự án đặt trước khi nhìn holdout. Đợt này chỉ kiểm hồ sơ của kho, chưa nghiệm thu dataset thực tế.

**Nguồn §6b:** [LICENSE](https://github.com/treeverse/dvc/blob/56e59829512ff134aa269099a2099587b810b4dd/LICENSE) · [dvc/repo/reproduce.py](https://github.com/treeverse/dvc/blob/56e59829512ff134aa269099a2099587b810b4dd/dvc/repo/reproduce.py) · [dvc/repo/pull.py](https://github.com/treeverse/dvc/blob/56e59829512ff134aa269099a2099587b810b4dd/dvc/repo/pull.py) · [dvc/repo/status.py](https://github.com/treeverse/dvc/blob/56e59829512ff134aa269099a2099587b810b4dd/dvc/repo/status.py) · [.github/workflows/tests.yaml](https://github.com/treeverse/dvc/blob/56e59829512ff134aa269099a2099587b810b4dd/.github/workflows/tests.yaml).

## 6c. Business Ontology cho doanh nghiệp: quy trình 8 bước, Core mở rộng theo ngành, kiến trúc 5 lớp, và công cụ mở cho từng bước (3 infographic người dùng gửi, 8/11/2026)

> Ba ảnh: (1) "Quy trình triển khai Business Ontology" 8 bước, 5 vai trò, 4 đầu ra; (2) "Mô hình Core Ontology và mở rộng theo ngành" với 8 Object lõi và 4 ngành; (3) "Kiến trúc Ontology cho Doanh nghiệp" từ nguồn dữ liệu tới người dùng, có lớp quản trị và bảo mật bên dưới. Ba ảnh là một bộ khái niệm, không kèm repo; mục này ghi lại ý chính và ghép với chuẩn, công cụ mở để làm được từng bước.

### 6c.1 Ý chính của ba ảnh

**Quy trình 8 bước** (ảnh 1):

| Bước | Việc | Vai trò chính | Ra gì |
|---|---|---|---|
| 1 | Xác định bài toán và KPI | Business Owner | Mục tiêu, phạm vi, chỉ số đo |
| 2 | Phân tích quy trình nghiệp vụ end-to-end | BA | Hoạt động, đầu vào, đầu ra, tác nhân |
| 3 | Xác định Object (thực thể cốt lõi) | BA, Data Architect | Danh sách Object |
| 4 | Định nghĩa Property và Trạng thái trong vòng đời | Data Architect | Thuộc tính, máy trạng thái |
| 5 | Mô hình Relationship (liên kết, sở hữu, phụ thuộc, bao gồm) | Data Architect | Đồ thị quan hệ |
| 6 | Thiết lập Business Rules (ràng buộc, logic suy luận, điều kiện xử lý) | BA, Data Architect | Bộ luật |
| 7 | Mapping dữ liệu từ CRM, ERP, Excel; làm sạch, chuẩn hóa | Data Engineer | Data Mapping |
| 8 | AI Agent, Dashboard, Action (tự động hóa, gợi ý, cảnh báo) | AI Engineer | Use case AI |

Bốn đầu ra: Ontology Catalog, Data Mapping, Test Cases, Use Cases AI.

**Core chung, mở rộng theo ngành** (ảnh 2): 8 Object lõi dùng mọi nơi (Customer, Product, Order, Contract, Invoice, Payment, Employee, Supplier); mỗi ngành thêm Object riêng: sản xuất (BOM, lệnh sản xuất, vật tư, chất lượng), xây dựng (công trình, hạng mục, khối lượng, nghiệm thu), thương mại (kho, giao hàng, khuyến mại, nhà phân phối), du lịch (tour, booking, lịch khởi hành, dịch vụ). Cùng một Core phục vụ Data Platform, BI, AI Agent, ERP/CRM và báo cáo quản trị.

**Kiến trúc 5 lớp** (ảnh 3): nguồn dữ liệu (CRM, ERP, kế toán MISA, Excel, HRM, sản xuất, website/app) → Data Platform (tích hợp, làm sạch, kho dữ liệu hoặc lakehouse, BI và API) → Business Ontology (Object, Property, Relationship, Business Rules, KPI, Action) → AI và ứng dụng (AI Agent, Copilot, dashboard, workflow, cảnh báo, tự động hóa) → người dùng (CEO, trưởng phòng, nhân viên, khách hàng), có vòng phản hồi và yêu cầu xử lý quay lại lớp ứng dụng. Lớp quản trị và bảo mật nằm dưới mọi lớp: phân quyền, audit log, data quality, quy trình phê duyệt.

### 6c.2 Khái niệm ứng với chuẩn mở và sản phẩm đã có

| Khái niệm trong ảnh | Palantir Foundry Ontology | Chuẩn W3C / mở |
|---|---|---|
| Object | Object type | `owl:Class`, LinkML `class` |
| Property | Property, Shared property | `owl:DatatypeProperty`, LinkML `slot` |
| Relationship | Link type | `owl:ObjectProperty` |
| Business Rules | Functions, ràng buộc trên Action | SHACL shapes |
| Action | Action type | API hoặc workflow ghi lại vào hệ thống nguồn |
| Core + mở rộng ngành | Interfaces (hình dạng chung cho nhiều Object type) | LinkML `imports`, `is_a`, `mixins`; schema.org làm từ vựng lõi |
| Phân quyền | Roles | quyền ở lớp truy vấn và ứng dụng |

Palantir mô tả Ontology là mô hình thế giới của tổ chức, ánh xạ dataset và model vào object type, property, link và action, và dùng Object View gom chi tiết, đối tượng liên kết, chỉ số và dashboard của một object vào một chỗ. Đây là bản thương mại gần nhất với ba ảnh.

### 6c.3 Công cụ mở cho từng bước

| Bước | Công cụ | Repo | ★ (8/11/2026) | Giấy phép | Dùng làm gì |
|---|---|---|---|---|---|
| 3–5 | LinkML | `linkml/linkml` | 691 | Apache-2.0 | Viết Object, Property, Relationship bằng YAML hướng đối tượng, sinh ra JSON Schema, SQL DDL, Pydantic, OWL, SHACL và tài liệu từ một nguồn; `imports` cho Core và module ngành |
| 3–5 | Protégé | `protegeproject/protege` | 1.634 | BSD-2-Clause | Trình soạn ontology OWL 2 có giao diện, kiến trúc plugin, cho BA và Data Architect xem và sửa trực quan |
| 3 | schema.org | `schemaorg/schemaorg` | 6.300 | Apache-2.0 | Từ vựng chung có sẵn Person, Organization, Product, Order, Invoice, Offer để đặt tên Core thống nhất |
| 6, kiểm thử | pySHACL | `RDFLib/pySHACL` | 371 | Apache-2.0 | Kiểm dữ liệu theo SHACL (chuẩn W3C): biến Business Rules thành bài kiểm chạy được, ra Test Cases |
| 7 | Ontop | `ontop/ontop` | 1.016 | Apache-2.0 | Knowledge graph ảo trên cơ sở dữ liệu quan hệ: ánh xạ bảng vào ontology bằng R2RML, dịch SPARQL thành SQL, dữ liệu vẫn ở nguồn |
| 1, 8 | MetricFlow | `dbt-labs/metricflow` | 1.866 | Apache-2.0 | Định nghĩa KPI bằng code một lần, dùng chung cho BI, API và agent |

Cùng nhóm đã có hồ sơ: Cube (`cube-js/cube`) và WrenAI (`Canner/WrenAI`) ở mục 15 làm semantic layer cho BI và text-to-SQL.

### 6c.4 Làm theo ba ảnh

1. Chọn một bài toán có KPI rõ (bước 1) và viết Core 8 Object bằng LinkML, đặt tên theo schema.org.
2. Thêm một module ngành bằng `imports` (ví dụ xây dựng: công trình, hạng mục, khối lượng, nghiệm thu), giữ Core không đổi.
3. Viết Business Rules thành SHACL và chạy pySHACL trên dữ liệu mẫu; mỗi luật là một Test Case.
4. Ánh xạ bảng CRM, ERP, MISA vào Object bằng Ontop (không phải chép dữ liệu) hoặc pipeline vào lakehouse; định nghĩa KPI trong MetricFlow.
5. Cho AI Agent đọc ontology (tên Object, quan hệ, luật) làm ngữ cảnh và gọi Action qua API có phân quyền, audit log và bước phê duyệt như lớp quản trị trong ảnh 3.

**Nguồn §6c:** 3 infographic người dùng gửi 8/11/2026 · https://www.palantir.com/docs/foundry/ontology/core-concepts · clone `--depth 1 --sparse` 8/11/2026: https://github.com/linkml/linkml/blob/5dcae0f60bb524b3aec2b8a488fcce3546da8149/README.md · https://github.com/protegeproject/protege/blob/bf03cccc65ea664e139d6829bba6d209ef58ee55/README.md · https://github.com/schemaorg/schemaorg/blob/02bbb0f199023dd3fc335b27dde8a71066f84f61/README.md · https://github.com/RDFLib/pySHACL/blob/df57bd4390bd397811d7c2d3b7cf0e49cd21c189/README.md · https://github.com/ontop/ontop/blob/964dbb79431fb958fce9de0784424f7c0e35f9bf/README.md · https://github.com/dbt-labs/metricflow/blob/fe4b8c1ccb72a8ca77494b345777eff20a714119/README.md · GitHub search API 8/11/2026.

## 7. Nguồn và nguyên tắc cập nhật

Mỗi hồ sơ dẫn README/LICENSE/CI/source ghim full SHA đã clone. Stars và `archived` lấy từ GitHub REST ngày 2/11/2026; commit date lấy từ HEAD đã đọc. `pushed_at` có thể là hoạt động nhánh khác. Không gọi repo “còn phát triển mạnh” chỉ vì chưa archive. Không chạy mã, upload dataset hay kiểm chứng con số marketing trong đợt này.

**Đối chiếu ngoài repo:** [báo cáo FineWeb của Hugging Face](https://huggingfacefw-blogpost-fineweb-v1.static.hf.space/index.html) nêu rõ việc đánh giá recipe downstream thay vì chỉ dùng điểm “data sạch”; [Secure Label Studio](https://labelstud.io/guide/security) mô tả tắt analytics và giới hạn truy cập. Tài liệu Label Studio đang nói SSRF tắt mặc định trong khi source tại SHA hồ sơ ghi true: cần kiểm phiên bản triển khai, đặt cấu hình rõ thay vì suy từ docs. [Thông báo license của lakeFS ngày 22/9/2026](https://lakefs.io/blog/lakefs-business-source-license/) xác nhận thay đổi từ v1.87.0 và DVC giữ Apache-2.0; điều khoản license ghim trong hồ sơ là nguồn quyết định.

Khi cập nhật: kiểm lại namespace, license từng component, maintainer note và HEAD/release hỗ trợ; so schema export và default analytics; xem dependency/model tải từ đâu; giữ paper/spec ở phiên bản đã đọc. Nếu không có phép đo downstream, ghi rõ công cụ giúp làm bước nào và chưa chứng minh tác động gì.

<a id="anhkysuai-2026-11-23"></a>

## Đánh giá từ kho Anh Kỹ Sư AI — 23/11/2026

Phần này có **13 hồ sơ hoặc phạm vi đối chiếu** từ [nguồn tuyển chọn](https://anhkysuai.com/kho/). [Bảng đủ 1.295 repo](../data/collections/anhkysuai-kho.json) ghi trạng thái đối chiếu từng link; [danh sách URL](../data/collections/anhkysuai-kho-links.txt) phục vụ tra cứu. Nguồn tuyển chọn giúp phát hiện repo; đánh giá bên dưới dựa trên clone và permalink upstream cùng metadata GitHub ngày 2026-11-23.

Mức `docs-read`/`code-read` chỉ áp dụng phạm vi ghi tại mỗi hồ sơ. Chưa cài, build, chạy test hay benchmark mã upstream. Giấy phép có thể tách theo code, model, nội dung, asset hoặc bản enterprise; con số/tuyên bố của tác giả chưa được tái lập nếu không có ghi chú khác.

<a id="anhkysuai-2026-11-23-scrapy"></a>

### Scrapy

**Repo:** [scrapy/scrapy](https://github.com/scrapy/scrapy) · **License:** BSD-3-Clause · **★ 65,548 (GitHub API, 2026-11-23)**

**Mục đích:** Framework Python thu thập dữ liệu có cấu trúc từ website.

**Giá trị và cơ chế:** README và manifest xác nhận kiến trúc crawler sử dụng Twisted cùng các thành phần parser; CI có cổng tĩnh trước tác vụ kiểm lớn, hữu ích cho pipeline thu thập có thể bảo trì.

**Giới hạn:** Đã đọc tài liệu, phụ thuộc và cấu hình CI, chưa chạy spider. Không nên mặc định website cần JavaScript sẽ hoạt động chỉ với HTTP crawler.

**Cách tham khảo/tích hợp:** Đặt giới hạn tốc độ, lưu URL/ngày lấy và viết fixture cho selector trước khi thu thập diện rộng.

**Thay thế:** [Crawlee](../24-ai-data-engineering/README.md#anhkysuai-2026-11-23-crawlee), [Crawl4AI](https://github.com/unclecode/crawl4ai), [Colly](../24-ai-data-engineering/README.md#anhkysuai-2026-11-23-colly).

**Bằng chứng:** `docs-read`, ngày 2026-11-23, commit [`00acf3f31a32`](https://github.com/scrapy/scrapy/commit/00acf3f31a322871a47aead5fec610d900263103). README và các tài liệu/manifest/CI hiện diện, đọc chọn lọc; chưa kiểm implementation. Chưa cài/chạy upstream.

**Nguồn:** [README.rst](https://github.com/scrapy/scrapy/blob/00acf3f31a322871a47aead5fec610d900263103/README.rst) · [LICENSE](https://github.com/scrapy/scrapy/blob/00acf3f31a322871a47aead5fec610d900263103/LICENSE) · [metadata GitHub](https://api.github.com/repos/scrapy/scrapy).

<a id="anhkysuai-2026-11-23-cheerio"></a>

### Cheerio

**Repo:** [cheeriojs/cheerio](https://github.com/cheeriojs/cheerio) · **License:** MIT · **★ 30,553 (GitHub API, 2026-11-23)**

**Mục đích:** Phân tích và thao tác HTML/XML trong Node.js bằng API gần jQuery.

**Giá trị và cơ chế:** README trình bày kết hợp parse5 hoặc htmlparser2 với selector và sửa cây tài liệu; phù hợp trích xuất dữ liệu từ HTML đã tải.

**Giới hạn:** Không chạy JavaScript trang hay tái tạo bố cục trình duyệt. Chưa thử tập HTML lỗi thực tế hoặc đo RAM; kết quả phụ thuộc parser và chế độ XML.

**Cách tham khảo/tích hợp:** Tách bước tải URL khỏi parse, lưu fixture HTML và kiểm selector khi cấu trúc nguồn thay đổi.

**Thay thế:** [jsoup](../24-ai-data-engineering/README.md#anhkysuai-2026-11-23-jsoup), beautifulsoup, [Crawlee](../24-ai-data-engineering/README.md#anhkysuai-2026-11-23-crawlee).

**Bằng chứng:** `docs-read`, ngày 2026-11-23, commit [`ad5347d1b344`](https://github.com/cheeriojs/cheerio/commit/ad5347d1b344ba60db6b0edd7fc8e5fe2ed42d6b). README và các tài liệu/manifest/CI hiện diện, đọc chọn lọc; chưa kiểm implementation. Chưa cài/chạy upstream.

**Nguồn:** [Readme.md](https://github.com/cheeriojs/cheerio/blob/ad5347d1b344ba60db6b0edd7fc8e5fe2ed42d6b/Readme.md) · [LICENSE](https://github.com/cheeriojs/cheerio/blob/ad5347d1b344ba60db6b0edd7fc8e5fe2ed42d6b/LICENSE) · [metadata GitHub](https://api.github.com/repos/cheeriojs/cheerio).

<a id="anhkysuai-2026-11-23-crawlee"></a>

### Crawlee

**Repo:** [apify/crawlee](https://github.com/apify/crawlee) · **License:** Apache-2.0 · **★ 26,523 (GitHub API, 2026-11-23)**

**Mục đích:** Framework Node.js cho crawling và scraping bằng HTTP hoặc trình duyệt.

**Giá trị và cơ chế:** README tổ chức crawler, hàng đợi, lưu kết quả và adapter trình duyệt; hữu ích xây pipeline thu thập có điều phối thay vì script tải từng URL.

**Giới hạn:** Node tối thiểu và Playwright là phụ thuộc cần xét theo bản ghim; chưa chạy trình duyệt hay kiểm khả năng qua từng website. Tuyên bố chống chặn không là bảo đảm truy cập.

**Cách tham khảo/tích hợp:** Chọn HTTP khi HTML đủ dữ liệu, browser khi cần render; giới hạn concurrency và lưu fixture để kiểm extraction.

**Thay thế:** [Scrapy](../24-ai-data-engineering/README.md#anhkysuai-2026-11-23-scrapy), [Colly](../24-ai-data-engineering/README.md#anhkysuai-2026-11-23-colly), [Crawl4AI](https://github.com/unclecode/crawl4ai).

**Bằng chứng:** `docs-read`, ngày 2026-11-23, commit [`4d7f4e41d497`](https://github.com/apify/crawlee/commit/4d7f4e41d4976513e401f68da0e6d0e389204b9c). README và các tài liệu/manifest/CI hiện diện, đọc chọn lọc; chưa kiểm implementation. Chưa cài/chạy upstream.

**Nguồn:** [README.md](https://github.com/apify/crawlee/blob/4d7f4e41d4976513e401f68da0e6d0e389204b9c/README.md) · [LICENSE.md](https://github.com/apify/crawlee/blob/4d7f4e41d4976513e401f68da0e6d0e389204b9c/LICENSE.md) · [metadata GitHub](https://api.github.com/repos/apify/crawlee).

<a id="anhkysuai-2026-11-23-colly"></a>

### Colly

**Repo:** [gocolly/colly](https://github.com/gocolly/colly) · **License:** Apache-2.0 · **★ 25,607 (GitHub API, 2026-11-23)**

**Mục đích:** Thư viện Go thu thập dữ liệu web theo callback và selector.

**Giá trị và cơ chế:** README mô tả quản lý cookie/session, đồng bộ/bất đồng bộ, giới hạn delay và concurrency theo domain; dễ nhúng vào dịch vụ Go.

**Giới hạn:** Không phải browser renderer. Chưa xác minh hành vi retry hoặc giới hạn trên website thực; cần thiết kế chống lặp URL, lưu tiến độ và xử lý thay đổi HTML.

**Cách tham khảo/tích hợp:** Dùng callback rõ ràng cho fetch–parse–persist và kiểm extractor bằng HTML fixture; đặt ngân sách tốc độ theo nguồn.

**Thay thế:** [Scrapy](../24-ai-data-engineering/README.md#anhkysuai-2026-11-23-scrapy), [Crawlee](../24-ai-data-engineering/README.md#anhkysuai-2026-11-23-crawlee), [Cheerio](../24-ai-data-engineering/README.md#anhkysuai-2026-11-23-cheerio).

**Bằng chứng:** `docs-read`, ngày 2026-11-23, commit [`d42a1f44c086`](https://github.com/gocolly/colly/commit/d42a1f44c086ea74c375361a0199247cdfebe31b). README và các tài liệu/manifest/CI hiện diện, đọc chọn lọc; chưa kiểm implementation. Chưa cài/chạy upstream.

**Nguồn:** [README.md](https://github.com/gocolly/colly/blob/d42a1f44c086ea74c375361a0199247cdfebe31b/README.md) · [LICENSE.txt](https://github.com/gocolly/colly/blob/d42a1f44c086ea74c375361a0199247cdfebe31b/LICENSE.txt) · [metadata GitHub](https://api.github.com/repos/gocolly/colly).

<a id="anhkysuai-2026-11-23-newspaper3k"></a>

### Newspaper3k

**Repo:** [codelucas/newspaper](https://github.com/codelucas/newspaper) · **License:** MIT; mã kế thừa có GOOSE-LICENSE riêng · **★ 15,191 (GitHub API, 2026-11-23)**

**Mục đích:** Thư viện Python trích bài báo, metadata và nội dung chính từ trang web.

**Giá trị và cơ chế:** README trình bày luồng Article.download → parse và các trường tác giả/ngày/nội dung; hữu ích pipeline tổng hợp tin với API gọn.

**Giới hạn:** Chưa thử độ chính xác ngày đăng hoặc loại boilerplate; ví dụ README không chứng minh phù hợp mọi website. Nhánh Python2 được đánh dấu bỏ; mã kế thừa cần giữ license tương ứng.

**Cách tham khảo/tích hợp:** Lưu HTML và kết quả để kiểm lại, phân biệt thời gian nguồn với thời gian crawl, bổ sung extractor riêng khi trang thay đổi.

**Thay thế:** trafilatura, readability, [Scrapy](../24-ai-data-engineering/README.md#anhkysuai-2026-11-23-scrapy).

**Bằng chứng:** `docs-read`, ngày 2026-11-23, commit [`745dfe3abe9e`](https://github.com/codelucas/newspaper/commit/745dfe3abe9ef5608461d335163c93c9e6c172fa). README và các tài liệu/manifest/CI hiện diện, đọc chọn lọc; chưa kiểm implementation. Chưa cài/chạy upstream.

**Nguồn:** [README.rst](https://github.com/codelucas/newspaper/blob/745dfe3abe9ef5608461d335163c93c9e6c172fa/README.rst) · [LICENSE](https://github.com/codelucas/newspaper/blob/745dfe3abe9ef5608461d335163c93c9e6c172fa/LICENSE) · [metadata GitHub](https://api.github.com/repos/codelucas/newspaper).

<a id="anhkysuai-2026-11-23-cocoindex"></a>

### CocoIndex

**Repo:** [cocoindex-io/cocoindex](https://github.com/cocoindex-io/cocoindex) · **License:** Apache-2.0 · **★ 11,929 (GitHub API, 2026-11-23)**

**Mục đích:** Framework khai báo biến đổi dữ liệu và cập nhật chỉ mục khi nguồn thay đổi.

**Giá trị và cơ chế:** Đọc memo_fingerprint thấy canonicalize kiểu dữ liệu/custom hook rồi tạo fingerprint qua lõi Rust; fingerprint_call ghép hàm, đối số và version. Cơ chế hỗ trợ tái dùng tính toán khi đầu vào không đổi.

**Giới hạn:** Chỉ kiểm phần khóa memo Python, chưa chứng minh engine incremental hoặc connector đầu-cuối. Khóa thiếu phụ thuộc ngữ nghĩa có thể gây cache cũ; chưa đo tính đúng đồng bộ.

**Cách tham khảo/tích hợp:** Khai báo phụ thuộc và version model rõ, thử thay file/xóa dữ liệu rồi đối chiếu chỉ mục đích.

**Thay thế:** [dlt (data load tool)](../15-ai-for-data/README.md#5-data-ingestion-and-asset-orchestration), [unstructured](../08-awesome-lists-learning/README.md#6c525-tài-liệu-ocr--thị-giác-máy-tính), [LlamaIndex](https://github.com/run-llama/llama_index).

**Bằng chứng:** `code-read`, ngày 2026-11-23, commit [`90c98f4a637e`](https://github.com/cocoindex-io/cocoindex/commit/90c98f4a637ed4cde1c59f63b9a6add0b2bc8602). Canonicalization/fingerprint_call Python và tài liệu khóa memo, CI; chưa kiểm engine incremental Rust đầu-cuối. Chưa cài/chạy upstream.

**Nguồn:** [README.md](https://github.com/cocoindex-io/cocoindex/blob/90c98f4a637ed4cde1c59f63b9a6add0b2bc8602/README.md) · [LICENSE](https://github.com/cocoindex-io/cocoindex/blob/90c98f4a637ed4cde1c59f63b9a6add0b2bc8602/LICENSE) · [python/cocoindex/_internal/memo_fingerprint.py](https://github.com/cocoindex-io/cocoindex/blob/90c98f4a637ed4cde1c59f63b9a6add0b2bc8602/python/cocoindex/_internal/memo_fingerprint.py) · [docs/src/content/docs/advanced_topics/memoization_keys.mdx](https://github.com/cocoindex-io/cocoindex/blob/90c98f4a637ed4cde1c59f63b9a6add0b2bc8602/docs/src/content/docs/advanced_topics/memoization_keys.mdx) · [metadata GitHub](https://api.github.com/repos/cocoindex-io/cocoindex).

<a id="anhkysuai-2026-11-23-jsoup"></a>

### jsoup

**Repo:** [jhy/jsoup](https://github.com/jhy/jsoup) · **License:** MIT · **★ 11,419 (GitHub API, 2026-11-23)**

**Mục đích:** Thư viện Java tải, parse, trích xuất và chỉnh sửa HTML/XML.

**Giá trị và cơ chế:** README trình bày DOM, CSS/XPath selector và làm sạch HTML theo safelist; phù hợp pipeline Java xử lý HTML không chuẩn mà không cần trình duyệt.

**Giới hạn:** Chưa chạy corpus parser hoặc kiểm cấu hình sanitizer; không thực thi JavaScript của trang. Safelist phải phù hợp mục đích, không suy mọi đầu ra luôn an toàn với mọi ngữ cảnh nhúng.

**Cách tham khảo/tích hợp:** Tách fetch khỏi parse và lưu fixture trang, kiểm selector/safelist trước đưa nội dung vào giao diện.

**Thay thế:** [Cheerio](../24-ai-data-engineering/README.md#anhkysuai-2026-11-23-cheerio), beautifulsoup, htmlunit.

**Bằng chứng:** `docs-read`, ngày 2026-11-23, commit [`d90d57521d93`](https://github.com/jhy/jsoup/commit/d90d57521d931db7bf7ee464a4c0a1a9293db088). README và các tài liệu/manifest/CI hiện diện, đọc chọn lọc; chưa kiểm implementation. Chưa cài/chạy upstream.

**Nguồn:** [README.md](https://github.com/jhy/jsoup/blob/d90d57521d931db7bf7ee464a4c0a1a9293db088/README.md) · [LICENSE](https://github.com/jhy/jsoup/blob/d90d57521d931db7bf7ee464a4c0a1a9293db088/LICENSE) · [metadata GitHub](https://api.github.com/repos/jhy/jsoup).

<a id="anhkysuai-pathwaycom-pathway"></a>

### Pathway Live Data Framework

**Repo:** [pathwaycom/pathway](https://github.com/pathwaycom/pathway) · **License:** BUSL-1.1; Additional Use Grant · **Kiểm:** 2026-11-23, `docs-read`, [`8206d9a0e492`](https://github.com/pathwaycom/pathway/tree/8206d9a0e49223c5771acefe5088cbe3814d5292) (commit 2026-11-23). **Sao:** 61,964 tại 2026-11-23 theo [GitHub API](https://api.github.com/repos/pathwaycom/pathway).

| Mục | Đánh giá |
|---|---|
| Mục đích | Khung Python ETL cho dữ liệu batch/streaming, phân tích trực tiếp và pipeline RAG. |
| Giá trị và cơ chế theo tài liệu | README mô tả API Python chạy trên engine Rust với tính toán tăng dần; manifest và CI cho thấy wheel được build từ cùng commit trước pytest. |
| Giới hạn | LICENSE là BSL với Additional Use Grant, không phải giấy phép OSI. Mức hiệu năng, tính đúng khi replay và giới hạn bộ nhớ chưa được tái lập. |
| Điều kiện tích hợp | Đánh giá connector và sự kiện cập nhật/xóa bằng corpus nhỏ; kiểm đầy đủ điều khoản production của đúng phiên bản trước khi triển khai. |
| Lựa chọn đối chiếu | Apache Flink; Spark Structured Streaming; Bytewax. |

**Phạm vi bằng chứng:** đã clone, đọc trích đoạn tài liệu, giấy phép và các file cấu hình được dẫn dưới đây; chưa chạy mã, build, benchmark hoặc test upstream. `docs-read` không phải kiểm chứng implementation.

**Nguồn tại cùng SHA:** [README.md](https://github.com/pathwaycom/pathway/blob/8206d9a0e49223c5771acefe5088cbe3814d5292/README.md) · [LICENSE.txt](https://github.com/pathwaycom/pathway/blob/8206d9a0e49223c5771acefe5088cbe3814d5292/LICENSE.txt) · [pyproject.toml](https://github.com/pathwaycom/pathway/blob/8206d9a0e49223c5771acefe5088cbe3814d5292/pyproject.toml) · [Cargo.toml](https://github.com/pathwaycom/pathway/blob/8206d9a0e49223c5771acefe5088cbe3814d5292/Cargo.toml) · [.github/workflows/pytest.yml](https://github.com/pathwaycom/pathway/blob/8206d9a0e49223c5771acefe5088cbe3814d5292/.github/workflows/pytest.yml).

<a id="anhkysuai-apache-spark"></a>

### Apache Spark

**Repo:** [apache/spark](https://github.com/apache/spark) · **License:** Apache-2.0; thông báo giấy phép bên thứ ba · **Kiểm:** 2026-11-23, `docs-read`, [`659273a41595`](https://github.com/apache/spark/tree/659273a41595e2ed86976c0be6d0a6e6b9923ef7) (commit 2026-11-23). **Sao:** 44,610 tại 2026-11-23 theo [GitHub API](https://api.github.com/repos/apache/spark).

| Mục | Đánh giá |
|---|---|
| Mục đích | Engine phân tích phân tán cho SQL, DataFrame, machine learning và xử lý luồng. |
| Giá trị và cơ chế theo tài liệu | README chỉ rõ Scala/Java/Python cùng SQL, MLlib, GraphX và Structured Streaming; Maven và CI thể hiện nền tảng đa ngôn ngữ. |
| Giới hạn | README đánh dấu R đã deprecated. Khả năng mở rộng và tính đúng của job streaming chưa được tái lập; LICENSE chứa cả thông báo thành phần và dữ liệu bên thứ ba. |
| Điều kiện tích hợp | Dùng release tương thích Java/Python và connector, đo với tập dữ liệu đại diện; kiểm checkpoint, partition, skew và phục hồi job trước production. |
| Lựa chọn đối chiếu | Apache Flink; Dask; DuckDB. |

**Phạm vi bằng chứng:** đã clone, đọc trích đoạn tài liệu, giấy phép và các file cấu hình được dẫn dưới đây; chưa chạy mã, build, benchmark hoặc test upstream. `docs-read` không phải kiểm chứng implementation.

**Nguồn tại cùng SHA:** [README.md](https://github.com/apache/spark/blob/659273a41595e2ed86976c0be6d0a6e6b9923ef7/README.md) · [LICENSE](https://github.com/apache/spark/blob/659273a41595e2ed86976c0be6d0a6e6b9923ef7/LICENSE) · [LICENSE-binary](https://github.com/apache/spark/blob/659273a41595e2ed86976c0be6d0a6e6b9923ef7/LICENSE-binary) · [pyproject.toml](https://github.com/apache/spark/blob/659273a41595e2ed86976c0be6d0a6e6b9923ef7/pyproject.toml) · [pom.xml](https://github.com/apache/spark/blob/659273a41595e2ed86976c0be6d0a6e6b9923ef7/pom.xml) · [.github/workflows/build_uds.yml](https://github.com/apache/spark/blob/659273a41595e2ed86976c0be6d0a6e6b9923ef7/.github/workflows/build_uds.yml).

<a id="anhkysuai-airbytehq-airbyte"></a>

### Airbyte

**Repo:** [airbytehq/airbyte](https://github.com/airbytehq/airbyte) · **License:** Elastic-2.0; kiểm giấy phép connector theo thư mục · **Kiểm:** 2026-11-23, `docs-read`, [`f5cbf0fd54a3`](https://github.com/airbytehq/airbyte/tree/f5cbf0fd54a3f79b179c8752fb3731ec713114cc) (commit 2026-11-17). **Sao:** 22,434 tại 2026-11-23 theo [GitHub API](https://api.github.com/repos/airbytehq/airbyte).

| Mục | Đánh giá |
|---|---|
| Mục đích | Nền tảng chuyển/đồng bộ dữ liệu từ API, database và tệp đến kho dữ liệu hoặc ứng dụng AI. |
| Giá trị và cơ chế theo tài liệu | README phân biệt Core/Cloud, connector catalog và MCP quản lý pipeline; Gradle cùng CI docs cho thấy repo nhiều thành phần. |
| Giới hạn | License gốc hiện là ELv2, không suy mọi connector nguồn mở theo nhãn marketing. Số connector không bảo đảm chất lượng từng nguồn; chưa kiểm incremental sync, CDC, schema drift hay agent tools. |
| Điều kiện tích hợp | Thử một cặp nguồn/đích với dữ liệu mẫu, kiểm cursor/delete/retry và quyền tối thiểu; ghim connector, review license và chi phí trước lịch sync thật. |
| Lựa chọn đối chiếu | Meltano; dlt; [Debezium](../15-ai-for-data/README.md#5-data-ingestion-and-asset-orchestration). |

**Phạm vi bằng chứng:** đã clone, đọc trích đoạn tài liệu, giấy phép và các file cấu hình được dẫn dưới đây; chưa chạy mã, build, benchmark hoặc test upstream. `docs-read` không phải kiểm chứng implementation.

**Nguồn tại cùng SHA:** [README.md](https://github.com/airbytehq/airbyte/blob/f5cbf0fd54a3f79b179c8752fb3731ec713114cc/README.md) · [LICENSE](https://github.com/airbytehq/airbyte/blob/f5cbf0fd54a3f79b179c8752fb3731ec713114cc/LICENSE) · [LICENSE_SHORT](https://github.com/airbytehq/airbyte/blob/f5cbf0fd54a3f79b179c8752fb3731ec713114cc/LICENSE_SHORT) · [build.gradle](https://github.com/airbytehq/airbyte/blob/f5cbf0fd54a3f79b179c8752fb3731ec713114cc/build.gradle) · [.github/workflows/docs-build.yml](https://github.com/airbytehq/airbyte/blob/f5cbf0fd54a3f79b179c8752fb3731ec713114cc/.github/workflows/docs-build.yml).

<a id="anhkysuai-antonmedv-fx"></a>

### fx

**Đã chuyển (2026-11-23):** hồ sơ này nay nằm ở [mục 13](../13-dev-stack-devops/README.md#anhkysuai-antonmedv-fx); catalog con xem [catalog/](../catalog/README.md).

<a id="anhkysuai-meta-prophet"></a>

### Prophet

**Đã chuyển (2026-11-23):** hồ sơ này nay nằm ở [mục 15](../15-ai-for-data/README.md#anhkysuai-meta-prophet); catalog con xem [catalog/](../catalog/README.md).

<a id="anhkysuai-2026-11-23-datatalksclub-data-engineering-zoomcamp"></a>

### data-engineering-zoomcamp

**Repo:** [DataTalksClub/data-engineering-zoomcamp](https://github.com/DataTalksClub/data-engineering-zoomcamp) · **License:** Chưa xác lập ở phạm vi đã đọc · **★ 47,025 (GitHub API, 2026-11-23)**

**Mục đích:** Khóa data engineering theo mô-đun, từ container và điều phối đến warehouse, batch, streaming và dự án cuối.

**Giá trị:** Có bài thực hành và dự án đầu-cuối, thuận tiện xây lộ trình học hạ tầng dữ liệu theo sản phẩm cụ thể.

**Giới hạn:** Không thấy giấy phép chung ở gốc; LICENSE MIT trong ví dụ PyFlink chỉ áp cho phạm vi đó. Chi phí dịch vụ cloud và khả năng hoàn tất khóa chưa được kiểm. Chưa xác lập giấy phép chung cho nội dung chính ở phạm vi đã đọc; không suy quyền tái sử dụng từ repo công khai.

**Cách tham khảo/tích hợp:** Chọn bài theo mục tiêu, thực hành lại trên môi trường riêng và kiểm bằng bài chuyển giao; khi dùng lại nội dung phải đối chiếu giấy phép đúng phạm vi.

**Lựa chọn để đối chiếu:** [DataExpert-io/data-engineer-handbook](https://github.com/DataExpert-io/data-engineer-handbook) · [GokuMohandas/Made-With-ML](https://github.com/GokuMohandas/Made-With-ML). Đây là ứng viên so sánh theo tác vụ; mức phù hợp cần kiểm theo hồ sơ và phiên bản riêng.

**Bằng chứng:** `docs-read`, ngày 2026-11-23, commit [`813d2774083186d0c9705c920deaf3e6e1693335`](https://github.com/DataTalksClub/data-engineering-zoomcamp/commit/813d2774083186d0c9705c920deaf3e6e1693335), ngày commit 2026-11-16. Đã clone và đọc chọn lọc phần giới thiệu, cách dùng, giới hạn, license, metadata manifest và CI hiện diện. Chưa kiểm đầy đủ implementation hoặc chạy upstream; các số đo của tác giả chưa được tái lập.

**Nguồn:** [README.md](https://github.com/DataTalksClub/data-engineering-zoomcamp/blob/813d2774083186d0c9705c920deaf3e6e1693335/README.md) · [07-streaming/extras/extras/pyflink/LICENSE](https://github.com/DataTalksClub/data-engineering-zoomcamp/blob/813d2774083186d0c9705c920deaf3e6e1693335/07-streaming/extras/extras/pyflink/LICENSE) · [metadata GitHub](https://api.github.com/repos/DataTalksClub/data-engineering-zoomcamp).

<a id="chuyen-muc-2026-11-23"></a>

## Hồ sơ chuyển về từ mục khác — 23/11/2026

2 hồ sơ được chuyển khi chia lại catalog theo `data/taxonomy.json`. Nội dung, ngày kiểm và mức bằng chứng giữ nguyên như ở mục gốc.

<a id="chuyen-scrapling"></a>

### Scrapling

`D4Vinci/Scrapling` · License: BSD-3-Clause · ★ 103.979 · docs-read · 2026-11-18

Framework thu thập web Python gộp HTTP nhanh, trình duyệt, parser và crawl đồng thời; dùng từ Python, terminal hoặc agent qua MCP server và Agent Skill. Spider kiểu Scrapy có pause/resume, AutoThrottle, tùy chọn tuân thủ robots.txt; theo dõi phần tử thích ứng khi trang đổi; xuất Markdown sạch cho RAG; kiểu đầy đủ, kiểm bằng PyRight và MyPy. Điều kiện: Python 3.10+; README nêu chỉ dùng cho giáo dục và nghiên cứu. phải tuân luật dữ liệu. điều khoản website và robots.txt. ★ 18/11/2026: 103.979 (GitHub search API), nhóm "Thu thập dữ liệu & Trình duyệt tự động" trong kho-repo của Phan Đông Giang, mục 08 §6c

**Hồ sơ gốc:** [mục 08](../08-awesome-lists-learning/README.md#6c-kho-repo-của-phan-đông-giang-phandonggiangcomkho-repo-694-repo-32-nhóm-và-24-repo-aiagent-đọc-mã-bảng-người-dùng-dán-kiểm-18112026) (bảng/đoạn chung, giữ nguyên tại chỗ).

<a id="chuyen-openmetadata"></a>

### OpenMetadata

`open-metadata/OpenMetadata` · License: Apache-2.0 · ★ 15.805 · docs-read · 2026-11-18

Nền tảng danh mục dữ liệu và quản trị metadata mã nguồn mở, gom lineage, chất lượng dữ liệu, sở hữu, glossary, hợp đồng dữ liệu thành đồ thị tri thức làm ngữ cảnh cho người dùng và agent AI. Hơn 130 connector; có lineage mức cột, kiểm thử chất lượng dữ liệu và profiling; cung cấp máy chủ MCP, API, SDK Python. Điều kiện: Tính năng quản lý doanh nghiệp, AI Studio, hỗ trợ thương mại thuộc sản phẩm Collate trả phí. ★ 18/11/2026: 15.805 (GitHub search API), nhóm "Giám sát, CSDL & Phân tích" trong kho-repo của Phan Đông Giang, mục 08 §6c.5

**Hồ sơ gốc:** [mục 08](../08-awesome-lists-learning/README.md#6c511-giám-sát-csdl--phân-tích) (bảng/đoạn chung, giữ nguyên tại chỗ).
