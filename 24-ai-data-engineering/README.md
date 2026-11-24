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

<a id="nt-2026-11-23"></a>

## Nâng trần theo khoảng trống — 23/11/2026

Phần này có các hồ sơ mới của đợt nâng trần: mười trinh sát tìm trên internet và GitHub những mảng mà chuyên mục còn thiếu hoặc chỉ có hồ sơ cũ, rồi mỗi repo được clone nông tại một commit cố định, đọc LICENSE, README, ít nhất một file triển khai thật và CI nếu có; không cài hay chạy mã upstream. Mô tả của trinh sát nhiều chỗ sai so với mã thật, và các chỗ đó được sửa ngay trong từng hồ sơ. Số sao lấy sau bằng GitHub search API nên có thể để trống.

<a id="nt-feast"></a>

### Feast (feature store)

| Thuộc tính | Giá trị |
|---|---|
| Repo | https://github.com/feast-dev/feast |
| License | Apache-2.0 |
| Phiên bản đã đọc | `a291a0f12bf78bdc28409c97139e43fb347b5da4` (commit 2026-11-23) |
| Kiểm chứng | 2026-11-23; code-read; đã đọc LICENSE, README.md, sdk/python/feast/infra/offline_stores/dask.py, sdk/python/feast/infra/offline_stores/offline_utils.py, sdk/python/feast/permissions/enforcer.py; chưa chạy upstream |
| Khoảng trống lấp | Feature store cho ML (kho chưa có mảng này) |
| Cơ chế đáng học | - Point-in-time join: `dask.py` chuẩn hóa timestamp về UTC, sắp xếp rồi dùng `merge_asof`, `_filter_ttl` loại giá trị mới hơn mốc sự kiện hoặc cũ hơn `ttl` của feature view; `offline_utils.py` dựng truy vấn tương ứng cho store SQL.<br>- Tách offline store, online store (Redis, DynamoDB, SQLite, Postgres, vector store...) và registry thành interface thay được (`sdk/python/feast/infra/`).<br>- Quyền: `permissions/enforcer.py` áp `Permission` lên tài nguyên; nếu chưa định nghĩa quyền thì mọi người dùng đã xác thực đều có toàn quyền (có cảnh báo log).<br>- `audit/audit_logger.py` ghi JSONL cho lời gọi MCP/REST và quyết định authz, ghi chú rằng không đưa token, hàng entity hay giá trị feature vào log (tuyên bố trong docstring, chưa kiểm hết các lối ghi). |
| Tiêu chí và cách kiểm | CI `unit_tests.yml` chạy test Python và test Go (`go test ./go/...`); còn nhiều workflow integration (duckdb, ray, rbac, registry) mà tôi chưa mở. Tính đúng của point-in-time join có test unit/universal trong `sdk/python/tests` (chưa mở). Chưa chạy. |
| Giới hạn và rủi ro | Apache-2.0. Mặc định không có quyền thì cho phép mọi user đã xác thực: phải tự định nghĩa permissions và bật auth khi dùng feature server. Telemetry rời máy: không thấy trong file đã đọc; CHANGELOG nhắc gauge Prometheus về cài đặt (số đo cục bộ). Bề mặt rất rộng (hàng chục store contrib), mỗi cái có mức hỗ trợ khác nhau; repo có AGENTS.md/CLAUDE.md/skills chỉ là nội dung đọc. |
| So với | MLflow (theo dõi thực nghiệm, mục 07), lakeFS (phiên bản hóa dữ liệu, mục 24), DataHub (metadata/lineage); kho chưa có feature store nào khác |
| Nguồn | [LICENSE](https://github.com/feast-dev/feast/blob/a291a0f12bf78bdc28409c97139e43fb347b5da4/LICENSE) · [README.md](https://github.com/feast-dev/feast/blob/a291a0f12bf78bdc28409c97139e43fb347b5da4/README.md) · [dask.py](https://github.com/feast-dev/feast/blob/a291a0f12bf78bdc28409c97139e43fb347b5da4/sdk/python/feast/infra/offline_stores/dask.py) · [offline_utils.py](https://github.com/feast-dev/feast/blob/a291a0f12bf78bdc28409c97139e43fb347b5da4/sdk/python/feast/infra/offline_stores/offline_utils.py) · [enforcer.py](https://github.com/feast-dev/feast/blob/a291a0f12bf78bdc28409c97139e43fb347b5da4/sdk/python/feast/permissions/enforcer.py) · [audit_logger.py](https://github.com/feast-dev/feast/blob/a291a0f12bf78bdc28409c97139e43fb347b5da4/sdk/python/feast/audit/audit_logger.py) · [unit_tests.yml](https://github.com/feast-dev/feast/blob/a291a0f12bf78bdc28409c97139e43fb347b5da4/.github/workflows/unit_tests.yml) |

<a id="nt-lakehq-sail"></a>

### Sail (LakeSail)

| Thuộc tính | Giá trị |
|---|---|
| Repo | https://github.com/lakehq/sail |
| License | Apache-2.0 |
| Phiên bản đã đọc | `d7b5c1e01b804e551eec9e7cbacd49e81be8a663` (commit 2026-11-23) |
| Kiểm chứng | 2026-11-23; code-read; đã đọc LICENSE, README.md, scripts/common-gold-data/metrics.jq, scripts/spark-tests/run-tests.sh, .github/workflows/spark-tests.yml; chưa chạy upstream |
| Khoảng trống lấp | Engine truy vấn nhúng/Rust và thay thế Spark |
| Cơ chế đáng học | - Giao diện Spark Connect (`crates/sail-spark-connect`) nên không cần viết lại mã PySpark; parser Spark SQL tự viết (`sail-sql-parser`, `sail-sql-analyzer`).<br>- Gold data: `crates/sail-spark-connect/tests/gold_data/**.json` ghi đầu ra parser theo từng câu SQL; `scripts/common-gold-data/metrics.jq` đếm tp/tn/fp/fn và workflow `gold-data.yml` so báo cáo với commit nền của PR.<br>- Workflow `spark-tests.yml` dựng PySpark vá sẵn và chạy `scripts/spark-tests/run-tests.sh` với server Sail (cổng 50051); đặt `SPARK_TESTING_REMOTE_PORT` rỗng thì chạy trên Spark gốc để đối chiếu.<br>- Worker không trạng thái, shuffle trao đổi trực tiếp Arrow giữa worker (tuyên bố trong README, chưa kiểm). |
| Tiêu chí và cách kiểm | Tương thích đo bằng gold data (mức parser/plan, không phải kết quả truy vấn) và test PySpark trong CI; README tự ghi script `compatibility_check` là thử nghiệm, chỉ kiểm hàm được cài và không bao Spark SQL dạng chuỗi. Benchmark TPC-H SF100 trên r8g.4xlarge: Spark 534,78 s so với Sail 52,81 s, do tác giả công bố, chưa tái lập. |
| Giới hạn và rủi ro | Apache-2.0. Telemetry: exporter OTLP tắt trừ khi đặt `telemetry.exporter.otlp.endpoint` (theo `application.yaml` và `telemetry.rs`), tức không gửi ra ngoài mặc định. Phiên bản 0.7.3, phụ thuộc DataFusion 55.x nên API và hành vi còn đổi nhanh; không phải bản thay thế đủ cho mọi tính năng Spark (MLlib, một số UDF, streaming cần xem docs). Quy mô phụ thuộc cấu hình cluster/Kubernetes. |
| So với | Apache Spark (engine được thay thế), DuckDB, Polars; Apache DataFusion (nền của Sail, hồ sơ trong đợt này) |
| Nguồn | [LICENSE](https://github.com/lakehq/sail/blob/d7b5c1e01b804e551eec9e7cbacd49e81be8a663/LICENSE) · [README.md](https://github.com/lakehq/sail/blob/d7b5c1e01b804e551eec9e7cbacd49e81be8a663/README.md) · [metrics.jq](https://github.com/lakehq/sail/blob/d7b5c1e01b804e551eec9e7cbacd49e81be8a663/scripts/common-gold-data/metrics.jq) · [run-tests.sh](https://github.com/lakehq/sail/blob/d7b5c1e01b804e551eec9e7cbacd49e81be8a663/scripts/spark-tests/run-tests.sh) · [spark-tests.yml](https://github.com/lakehq/sail/blob/d7b5c1e01b804e551eec9e7cbacd49e81be8a663/.github/workflows/spark-tests.yml) · [gold-data.yml](https://github.com/lakehq/sail/blob/d7b5c1e01b804e551eec9e7cbacd49e81be8a663/.github/workflows/gold-data.yml) · [telemetry.rs](https://github.com/lakehq/sail/blob/d7b5c1e01b804e551eec9e7cbacd49e81be8a663/crates/sail-telemetry/src/telemetry.rs) |

<a id="nt-apache-gravitino"></a>

### Apache Gravitino

| Thuộc tính | Giá trị |
|---|---|
| Repo | https://github.com/apache/gravitino |
| License | Apache-2.0 (LICENSE gốc; kèm LICENSE.iceberg, LICENSE.lance, LICENSE.trino và LICENSE.bin cho phần phân phối/bundle) |
| Phiên bản đã đọc | `9a3748eb6d67af1bc87b5e1d7f521c562e5f72d8` (commit 2026-11-23) |
| Kiểm chứng | 2026-11-23; code-read; đã đọc LICENSE, README.md, core/src/main/java/org/apache/gravitino/authorization/GravitinoAuthorizer.java, docs/security/authorization-pushdown.md, conf/gravitino.conf.template; chưa chạy upstream |
| Khoảng trống lấp | Catalog/metadata đa engine và quản trị truy cập |
| Cơ chế đáng học | - Giao diện `GravitinoAuthorizer` (`core/.../authorization/`): `authorize(principal, metalake, object, privilege, ctx)`; `canAccessDomain` mặc định đóng (fail closed).<br>- Đẩy quyền xuống nơi lưu dữ liệu: thuộc tính catalog `authorization-provider` là `ranger` hoặc `chain` (`docs/security/authorization-pushdown.md`); catalog không đặt thì chỉ quản quyền trong Gravitino.<br>- Mỗi nguồn là một module catalog (`catalogs/catalog-*`), gồm `catalog-model` cho model AI, cùng connector `trino-connector`, `spark-connector`, `flink-connector`.<br>- Có `mcp-server` (Python) cho agent truy cập metadata. |
| Tiêu chí và cách kiểm | Rất nhiều workflow CI: `build.yml` (gradle assemble, test), integration test riêng cho backend, access-control, Trino, Spark, Flink, Python, MCP, multi-instance consistency. Chỉ đọc một phần `build.yml` (các dòng run); chưa mở các workflow integration. Chưa chạy. |
| Giới hạn và rủi ro | Apache-2.0 cho mã nguồn; bản bin/bundle kèm các LICENSE riêng (iceberg, lance, trino) cần đọc khi phân phối lại. Mô tả của trinh sát "cả dữ liệu lẫn model/AI" đúng nhưng AI asset là WIP theo README. Quyền Gravitino chỉ cưỡng chế ở nơi khác nếu cấu hình pushdown. Dự án ASF top-level nhưng triển khai nặng (server, backend lưu entity, từng connector). |
| So với | DataHub (catalog/lineage, mục 15), OpenMetadata (mục 24), Project Nessie (catalog giao dịch, hồ sơ đợt này), OpenFGA (phân quyền, mục 12) |
| Nguồn | [LICENSE](https://github.com/apache/gravitino/blob/9a3748eb6d67af1bc87b5e1d7f521c562e5f72d8/LICENSE) · [README.md](https://github.com/apache/gravitino/blob/9a3748eb6d67af1bc87b5e1d7f521c562e5f72d8/README.md) · [GravitinoAuthorizer.java](https://github.com/apache/gravitino/blob/9a3748eb6d67af1bc87b5e1d7f521c562e5f72d8/core/src/main/java/org/apache/gravitino/authorization/GravitinoAuthorizer.java) · [authorization-pushdown.md](https://github.com/apache/gravitino/blob/9a3748eb6d67af1bc87b5e1d7f521c562e5f72d8/docs/security/authorization-pushdown.md) · [gravitino.conf.template](https://github.com/apache/gravitino/blob/9a3748eb6d67af1bc87b5e1d7f521c562e5f72d8/conf/gravitino.conf.template) · [build.yml](https://github.com/apache/gravitino/blob/9a3748eb6d67af1bc87b5e1d7f521c562e5f72d8/.github/workflows/build.yml) |

<a id="nt-projectnessie-nessie"></a>

### Project Nessie

| Thuộc tính | Giá trị |
|---|---|
| Repo | https://github.com/projectnessie/nessie |
| License | Apache-2.0 |
| Phiên bản đã đọc | `6e94baa550519903f2006f40ccb1d901d8908342` (commit 2026-11-23) |
| Kiểm chứng | 2026-11-23; code-read; đã đọc LICENSE, README.md, SECURITY_THREAT_MODEL.md, versioned/spi/src/main/java/org/projectnessie/versioned/VersionStore.java, servers/quarkus-config/src/main/java/org/projectnessie/quarkus/config/QuarkusNessieAuthorizationConfig.java; chưa chạy upstream |
| Khoảng trống lấp | Catalog/metadata đa engine và quản trị truy cập |
| Cơ chế đáng học | - `VersionStore` (`versioned/spi/`): merge/transplant với `mergeKeyBehaviors`, tùy chọn dry-run (thử merge, kiểm xung đột nhưng không commit), ném `MergeConflictException`/`ReferenceConflictException`.<br>- Phân quyền bằng biểu thức CEL theo principal, reference, content key, thao tác (các lớp `CelAuthorizer`, `CompiledAuthorizationRules` trong `servers/quarkus-authz`, chưa mở nội dung; cấu hình mặc định đọc ở `QuarkusNessieAuthorizationConfig.java`); cấu hình `nessie.server.authorization.rules`.<br>- Tài liệu mô hình đe dọa `SECURITY_THREAT_MODEL.md` đánh dấu từng claim là documented, maintainer hoặc inferred.<br>- Công cụ GC riêng (`gc/`) dọn dữ liệu mồ côi cho Iceberg. |
| Tiêu chí và cách kiểm | CI `ci.yml` (đọc các bước run) chạy `codeChecks`, `assemble`, test Quarkus, test events, kiểm tích hợp công cụ build; test version store tách theo backend (`versioned/storage/*-tests`). Kiểm bằng máy; chưa chạy. |
| Giới hạn và rủi ro | Apache-2.0. README ghi rõ mặc định xác thực tắt (mọi yêu cầu là user anonymous) và `nessie.server.authorization.enabled` mặc định false: phải tự bật OIDC và rule CEL. CHANGELOG nêu nhiều version store cũ (JDBC, CASSANDRA, MONGODB, DynamoDB đời 1) đã deprecated, cần dùng bản `*2`. Image đã chuyển sang ghcr.io và quay.io. |
| So với | lakeFS (phiên bản hóa dữ liệu kiểu Git trên object store, mục 24), Apache Gravitino (catalog liên hợp, hồ sơ đợt này), DataHub |
| Nguồn | [LICENSE](https://github.com/projectnessie/nessie/blob/6e94baa550519903f2006f40ccb1d901d8908342/LICENSE) · [README.md](https://github.com/projectnessie/nessie/blob/6e94baa550519903f2006f40ccb1d901d8908342/README.md) · [SECURITY_THREAT_MODEL.md](https://github.com/projectnessie/nessie/blob/6e94baa550519903f2006f40ccb1d901d8908342/SECURITY_THREAT_MODEL.md) · [VersionStore.java](https://github.com/projectnessie/nessie/blob/6e94baa550519903f2006f40ccb1d901d8908342/versioned/spi/src/main/java/org/projectnessie/versioned/VersionStore.java) · [QuarkusNessieAuthorizationConfig.java](https://github.com/projectnessie/nessie/blob/6e94baa550519903f2006f40ccb1d901d8908342/servers/quarkus-config/src/main/java/org/projectnessie/quarkus/config/QuarkusNessieAuthorizationConfig.java) · [ci.yml](https://github.com/projectnessie/nessie/blob/6e94baa550519903f2006f40ccb1d901d8908342/.github/workflows/ci.yml) |

<a id="nt-apache-xtable"></a>

### Apache XTable (Incubating)

| Thuộc tính | Giá trị |
|---|---|
| Repo | https://github.com/apache/incubator-xtable |
| License | Apache-2.0 (bundled jar của xtable-utilities kèm jol-core GPL-2.0 với Classpath Exception, và README nói bundled jar không mang LICENSE/NOTICE cho phần gói kèm) |
| Phiên bản đã đọc | `603a057c7a623747be0abcf553431dc36269c5c5` (commit 2026-11-23) |
| Kiểm chứng | 2026-11-23; code-read; đã đọc LICENSE, README.md, DISCLAIMER, THREAT_MODEL.md, xtable-core/src/main/java/org/apache/xtable/conversion/ConversionController.java; chưa chạy upstream |
| Khoảng trống lấp | Định dạng bảng mở và catalog lakehouse (Iceberg/Parquet/Delta) |
| Cơ chế đáng học | - `ConversionController`: chế độ FULL hoặc INCREMENTAL; `getFormatsToSyncIncrementally` bỏ qua incremental nếu `isIncrementalSyncSafe()` sai hoặc không đủ lịch sử, rồi rơi về snapshot sync.<br>- Mô hình trung gian `InternalTable`/`InternalSnapshot`/`TableChange` (`xtable-api/.../model`), mỗi định dạng có `ConversionSource` và `ConversionTarget` (Delta, Hudi, Iceberg, Paimon).<br>- `TableSyncMetadata` lưu instant đã đồng bộ cuối để lần sau chạy tiếp.<br>- Cấu hình YAML (`sourceFormat`, `targetFormats`, `datasets`) và có thể thay converter bằng lớp tự viết. |
| Tiêu chí và cách kiểm | CI `mvn-ci-build.yml` chạy `./mvnw clean install` (gồm unit test; IT như `ITConversionController`, `ITDeltaLogTruncationSafetyCheck` thuộc profile verify) và Spotless; có workflow kiểm license. Tính tương thích đo bằng test chuyển đổi cho từng cặp định dạng. Chưa chạy. |
| Giới hạn và rủi ro | Apache-2.0 nhưng DISCLAIMER: Incubator, chưa được ASF xác nhận. Bundled jar chứa jol-core (GPL-2.0 with Classpath Exception) và README nói rõ không phải artifact phát hành. THREAT_MODEL.md ở trạng thái v1 draft chờ PPMC rà. Chuyển metadata không sửa dữ liệu nhưng đích thành bản sao metadata có thể lệch nếu ghi đồng thời từ hai phía; cần một nguồn ghi duy nhất. |
| So với | Project Nessie (catalog giao dịch), Apache Gravitino (catalog liên hợp), lakeFS; kho chưa có hồ sơ Iceberg/Delta/Hudi riêng |
| Nguồn | [LICENSE](https://github.com/apache/incubator-xtable/blob/603a057c7a623747be0abcf553431dc36269c5c5/LICENSE) · [README.md](https://github.com/apache/incubator-xtable/blob/603a057c7a623747be0abcf553431dc36269c5c5/README.md) · [DISCLAIMER](https://github.com/apache/incubator-xtable/blob/603a057c7a623747be0abcf553431dc36269c5c5/DISCLAIMER) · [THREAT_MODEL.md](https://github.com/apache/incubator-xtable/blob/603a057c7a623747be0abcf553431dc36269c5c5/THREAT_MODEL.md) · [ConversionController.java](https://github.com/apache/incubator-xtable/blob/603a057c7a623747be0abcf553431dc36269c5c5/xtable-core/src/main/java/org/apache/xtable/conversion/ConversionController.java) · [pom.xml](https://github.com/apache/incubator-xtable/blob/603a057c7a623747be0abcf553431dc36269c5c5/xtable-utilities/pom.xml) · [mvn-ci-build.yml](https://github.com/apache/incubator-xtable/blob/603a057c7a623747be0abcf553431dc36269c5c5/.github/workflows/mvn-ci-build.yml) |

<a id="nt-bitol-odcs"></a>

### Open Data Contract Standard (ODCS)

| Thuộc tính | Giá trị |
|---|---|
| Repo | https://github.com/bitol-io/open-data-contract-standard |
| License | Apache-2.0 |
| Phiên bản đã đọc | `7c7597ee04ec58f67ea4a9cbcddab2043ff7d01f` (commit 2026-11-17) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc LICENSE, README.md, docs/data-quality.md, schema/README.md, schema/odcs-json-schema-latest.json; chưa chạy upstream |
| Khoảng trống lấp | Data contract (ODCS) và kiểm chứng hợp đồng |
| Cơ chế đáng học | - `schema/odcs-json-schema-v3.2.0.json` là bản chốt, `odcs-json-schema-latest.json` bám đầu nhánh; `validate-schema-parity.sh` kiểm latest trùng bản đã đánh phiên bản.<br>- Quality 4 mức trong `docs/data-quality.md`: `text`, `library` (metric `nullValues`, `missingValues`, `invalidValues`, `duplicateValues`, `rowCount` có operator so sánh), `sql`, `custom` (engine: soda, greatExpectations, dqx).<br>- `required` ở gốc: `version`, `apiVersion`, `kind`, `id`; `type` của server dùng `const` cho từng loại hệ thống.<br>- Đặt tên `.odcs.yaml` để công cụ tự nhận diện. |
| Tiêu chí và cách kiểm | Workflow `validate-examples.yaml` cài ajv-cli, chạy `validate-schema-parity.sh`, `validate-examples.sh` (mọi ví dụ phải hợp lệ) và `validate-negative.sh` (44 file trong `src/script/negative-tests` phải bị schema từ chối). Kiểm bằng máy nhưng chỉ ở tầng cấu trúc. Chưa chạy. |
| Giới hạn và rủi ro | Apache-2.0. Là chuẩn nên không có telemetry. Số phiên bản schema trong thư mục nhiều và gồm bản gắn ngày, người dùng cần ghim phiên bản; chuẩn mô tả hợp đồng chứ không bắt buộc ai thi hành. Mô tả trinh sát đúng (có JSON Schema, kiểm bằng máy được) nhưng kiểm ở đây là hợp lệ cấu trúc, không phải kiểm hợp đồng với dữ liệu thật. |
| So với | Soda Core và Great Expectations (engine thi hành quality, mục 15), DataHub/OpenMetadata (catalog giữ metadata hợp đồng) |
| Nguồn | [LICENSE](https://github.com/bitol-io/open-data-contract-standard/blob/7c7597ee04ec58f67ea4a9cbcddab2043ff7d01f/LICENSE) · [README.md](https://github.com/bitol-io/open-data-contract-standard/blob/7c7597ee04ec58f67ea4a9cbcddab2043ff7d01f/README.md) · [data-quality.md](https://github.com/bitol-io/open-data-contract-standard/blob/7c7597ee04ec58f67ea4a9cbcddab2043ff7d01f/docs/data-quality.md) · [README.md](https://github.com/bitol-io/open-data-contract-standard/blob/7c7597ee04ec58f67ea4a9cbcddab2043ff7d01f/schema/README.md) · [odcs-json-schema-latest.json](https://github.com/bitol-io/open-data-contract-standard/blob/7c7597ee04ec58f67ea4a9cbcddab2043ff7d01f/schema/odcs-json-schema-latest.json) · [validate-examples.yaml](https://github.com/bitol-io/open-data-contract-standard/blob/7c7597ee04ec58f67ea4a9cbcddab2043ff7d01f/.github/workflows/validate-examples.yaml) · [validate-negative.sh](https://github.com/bitol-io/open-data-contract-standard/blob/7c7597ee04ec58f67ea4a9cbcddab2043ff7d01f/src/script/validate-negative.sh) |

<a id="nt-datasketch"></a>

### datasketch

| Thuộc tính | Giá trị |
|---|---|
| Repo | https://github.com/ekzhu/datasketch |
| License | MIT |
| Phiên bản đã đọc | `c7eaaeea3f39909f906a9cf8ad4d21a878cb4e07` (commit 2026-10-09) |
| Kiểm chứng | 2026-11-23; code-read; đã đọc README.rst, LICENSE, pyproject.toml, datasketch/lsh.py; chưa chạy upstream |
| Khoảng trống lấp | Chống rò rỉ dữ liệu huấn luyện và khử trùng lặp |
| Cơ chế đáng học | - `datasketch/lsh.py` `_optimal_param`: chọn cặp (b, r) cho `MinHashLSH` bằng cách quét mọi b và r sao cho `b*r <= num_perm`, tối thiểu hóa tổng có trọng số của xác suất dương tính giả và âm tính giả tính bằng tích phân; tham số `weights` mặc định (0.5, 0.5) chỉnh theo ưu tiên.<br>- `datasketch/minhash.py`: từ 2.0.0 mặc định sơ đồ `affine32` (sửa lệch ước lượng quá cao ở tập lớn), có `affine64` và `legacy`; `_check_scheme_consistency` làm lỗi to nếu trộn sơ đồ trong một chỉ mục thay vì trả kết quả sai âm thầm.<br>- `MinHashLSH.insertion_session` và `MinHash.bulk` để nạp theo lô; `datasketch/lsh_bloom.py` (LSHBloom) giảm bộ nhớ cho chỉ mục khử trùng lặp rất lớn (chỉ đọc README).<br>- `docs/lsh.rst`: benchmark trên hai kho tổng hợp (gần trùng và cụm chồng lấn) cho thấy độ chính xác phụ thuộc phân bố cặp quanh ngưỡng. |
| Tiêu chí và cách kiểm | CI `test.yml` (đã mở) chạy `pytest --cov` trên Python 3.9 đến 3.13 và đẩy coverage lên Codecov; có workflow riêng cho Redis, Cassandra, Mongo. Test trong `test/` kiểm tính đúng của sketch và LSH bằng máy; độ chính xác khử trùng lặp trên văn bản thật phải tự đo: `docs/lsh.rst` chỉ báo kết quả trên dữ liệu tổng hợp. |
| Giới hạn và rủi ro | MinHash ước lượng Jaccard theo tập shingle: bản dịch, diễn đạt lại hay thay đổi nhỏ đều lọt; với dữ liệu tiếng Việt phải tự quyết định tách từ và kích thước shingle. LSH có dương tính giả và âm tính giả theo ngưỡng. Nâng 2.0.0 làm hash khác bản cũ nên chỉ mục đã lưu phải dựng lại (hoặc dùng `scheme="legacy"`). Backend Redis và Cassandra là dịch vụ ngoài cần bảo mật riêng. Không telemetry thấy trong phần đã đọc, nhưng chưa quét toàn bộ mã. |
| So với | `datatrove` và `data-juicer` (có hàm khử trùng lặp hoàn chỉnh cho corpus huấn luyện, hồ sơ có sẵn mục 24), `cleanlab`. |
| Nguồn | [README.rst](https://github.com/ekzhu/datasketch/blob/c7eaaeea3f39909f906a9cf8ad4d21a878cb4e07/README.rst) · [LICENSE](https://github.com/ekzhu/datasketch/blob/c7eaaeea3f39909f906a9cf8ad4d21a878cb4e07/LICENSE) · [pyproject.toml](https://github.com/ekzhu/datasketch/blob/c7eaaeea3f39909f906a9cf8ad4d21a878cb4e07/pyproject.toml) · [lsh.py](https://github.com/ekzhu/datasketch/blob/c7eaaeea3f39909f906a9cf8ad4d21a878cb4e07/datasketch/lsh.py) · [minhash.py](https://github.com/ekzhu/datasketch/blob/c7eaaeea3f39909f906a9cf8ad4d21a878cb4e07/datasketch/minhash.py) · [lsh.rst](https://github.com/ekzhu/datasketch/blob/c7eaaeea3f39909f906a9cf8ad4d21a878cb4e07/docs/lsh.rst) · [test.yml](https://github.com/ekzhu/datasketch/blob/c7eaaeea3f39909f906a9cf8ad4d21a878cb4e07/.github/workflows/test.yml) |

<a id="nt-nemo-curator"></a>

### NVIDIA NeMo Curator

| Thuộc tính | Giá trị |
|---|---|
| Repo | https://github.com/NVIDIA-NeMo/Curator |
| License | Apache-2.0 (LICENSE gốc, header file Apache-2.0). Mô hình phân loại/embedding tải từ nơi khác có điều khoản riêng **(chưa xác minh)**, không mở |
| Phiên bản đã đọc | `a27996bcef0576453749cf9d29ca55521b5d1370` (commit 2026-11-23) |
| Kiểm chứng | 2026-11-23; code-read; đã đọc `README.md`, `LICENSE`, `pyproject.toml`, `nemo_curator/stages/deduplication/fuzzy/workflow.py`, `nemo_curator/stages/deduplication/exact/identification.py`, `.github/workflows/cicd-main.yml`; chưa chạy upstream |
| Khoảng trống lấp | Khử trùng lặp dữ liệu huấn luyện quy mô lớn (chưa có chống rò rỉ benchmark, xem giới hạn) |
| Cơ chế đáng học | - `FuzzyDeduplicationWorkflow` (`fuzzy/workflow.py`): MinHash, LSH, đồ thị cạnh, thành phần liên thông, rồi danh sách id cần bỏ; mặc định `char_ngrams=24`, `num_bands=20`, `minhashes_per_band=13`, seed 42, cảnh báo nếu `char_ngrams<20` vì ~5% dương tính giả.<br>- `ExactDuplicateIdentification` (`exact/identification.py`) băm cột văn bản, có `normalize_text` (hạ chữ, gộp khoảng trắng).<br>- Cùng bộ stage cho văn bản, ảnh, video, âm thanh trên Ray; thư mục `semantic/` thêm khử trùng lặp theo embedding (K-means, ngưỡng `eps`).<br>- Bước loại bản sao chỉ ghi danh sách id (`perform_removal` mặc định False), tách nhận diện khỏi xóa. |
| Tiêu chí và cách kiểm | Tham số được cảnh báo ngay trong mã; CI `cicd-main.yml` chạy unit test theo thư mục (có `stages-deduplication`) trên CPU (đã mở phần đầu file, chưa thấy phần GPU); thư mục `benchmarking/` đo hiệu năng hằng đêm (chỉ đọc README, chưa mở kết quả). |
| Giới hạn và rủi ro | Đường dedup (exact, fuzzy) import `cudf` nên cần GPU CUDA 12 và RAPIDS 26.8 (`pyproject.toml`); gói `text_cpu` không phủ phần này. **Mô tả của trinh sát chưa đúng:** grep không thấy stage chống rò rỉ benchmark (decontamination) trong mã/tài liệu; repo chỉ khử trùng lặp trong tập huấn luyện. Phụ thuộc Ray, nhiều extra; tốc độ đổi phiên bản cao (26.02 đã đổi kiến trúc). |
| So với | datatrove (hồ sơ có sẵn, chạy CPU/Slurm, MinHash cũng có), distilabel (sinh dữ liệu, không dedup), argilla. |
| Nguồn | [README.md](https://github.com/NVIDIA-NeMo/Curator/blob/a27996bcef0576453749cf9d29ca55521b5d1370/README.md) · [LICENSE](https://github.com/NVIDIA-NeMo/Curator/blob/a27996bcef0576453749cf9d29ca55521b5d1370/LICENSE) · [pyproject.toml](https://github.com/NVIDIA-NeMo/Curator/blob/a27996bcef0576453749cf9d29ca55521b5d1370/pyproject.toml) · [workflow.py](https://github.com/NVIDIA-NeMo/Curator/blob/a27996bcef0576453749cf9d29ca55521b5d1370/nemo_curator/stages/deduplication/fuzzy/workflow.py) · [identification.py](https://github.com/NVIDIA-NeMo/Curator/blob/a27996bcef0576453749cf9d29ca55521b5d1370/nemo_curator/stages/deduplication/exact/identification.py) · [cicd-main.yml](https://github.com/NVIDIA-NeMo/Curator/blob/a27996bcef0576453749cf9d29ca55521b5d1370/.github/workflows/cicd-main.yml) |

<a id="nt-bespoke-curator"></a>

### Bespoke Curator

| Thuộc tính | Giá trị |
|---|---|
| Repo | https://github.com/bespokelabsai/curator |
| License | Apache-2.0 (LICENSE; `pyproject.toml` khai Apache-2.0). Không có trọng số |
| Phiên bản đã đọc | `fab184b26578429568c39c6b1e6b1d67e1650ae1` (commit 2026-11-02) |
| Kiểm chứng | 2026-11-23; code-read; đã đọc `README.md`, `LICENSE`, `pyproject.toml`, `src/bespokelabs/curator/llm/llm.py`, `src/bespokelabs/curator/telemetry/client.py`, `src/bespokelabs/curator/status_tracker/online_status_tracker.py`, `.github/workflows/lint-and-test.yaml`; chưa chạy upstream |
| Khoảng trống lấp | Sinh dữ liệu tổng hợp bằng LLM có cache và chạy tiếp (post-training, fine-tuning) |
| Cơ chế đáng học | - `llm/llm.py`: mỗi lần chạy có vân tay xxh64 từ hash dataset, hash hàm prompt và tham số sinh; thư mục chạy trùng vân tay thì dùng lại bản đã có (resume), `CURATOR_DISABLE_CACHE` tắt.<br>- Nhiều processor chung giao diện (`request_processor/`): online (OpenAI, Anthropic, LiteLLM), batch (OpenAI, Anthropic, Gemini, Azure, Mistral), vLLM offline.<br>- Kết quả ghi `responses_*.jsonl` và dataset Arrow; đọc lại chịu được dòng lỗi và báo khi toàn bộ phản hồi lỗi.<br>- Có thêm trainer Fireworks/Tinker và CodeExecutor, ngoài phạm vi dữ liệu. |
| Tiêu chí và cách kiểm | CI chạy ruff và pytest với `--cov-fail-under=80` (đã mở workflow); nhưng tính đúng của dữ liệu sinh ra không được kiểm tự động, chỉ kiểm cơ chế gọi và cache. |
| Giới hạn và rủi ro | Telemetry PostHog bật mặc định: khóa ghi công khai nằm trong `telemetry/client.py`, tắt bằng `TELEMETRY_ENABLED=false`; `online_status_tracker.py` gửi sự kiện `OnlineRequest` với toàn bộ trường của tracker (đếm yêu cầu/token/chi phí; có chứa nội dung prompt hay không **(chưa xác minh)**). Viewer lưu trữ chỉ bật khi `CURATOR_VIEWER=1`, khi đó dữ liệu chạy lên api.bespokelabs.ai. Phụ thuộc vLLM ghim `^0.6.3` đã cũ. Commit gần nhất 2026-11-02. |
| So với | distilabel (hồ sơ có sẵn, pipeline sinh dữ liệu dạng đồ thị), datatrove và nemo-curator (lọc/dedup chứ không sinh), argilla. |
| Nguồn | [README.md](https://github.com/bespokelabsai/curator/blob/fab184b26578429568c39c6b1e6b1d67e1650ae1/README.md) · [LICENSE](https://github.com/bespokelabsai/curator/blob/fab184b26578429568c39c6b1e6b1d67e1650ae1/LICENSE) · [pyproject.toml](https://github.com/bespokelabsai/curator/blob/fab184b26578429568c39c6b1e6b1d67e1650ae1/pyproject.toml) · [llm.py](https://github.com/bespokelabsai/curator/blob/fab184b26578429568c39c6b1e6b1d67e1650ae1/src/bespokelabs/curator/llm/llm.py) · [client.py](https://github.com/bespokelabsai/curator/blob/fab184b26578429568c39c6b1e6b1d67e1650ae1/src/bespokelabs/curator/telemetry/client.py) · [online_status_tracker.py](https://github.com/bespokelabsai/curator/blob/fab184b26578429568c39c6b1e6b1d67e1650ae1/src/bespokelabs/curator/status_tracker/online_status_tracker.py) · [lint-and-test.yaml](https://github.com/bespokelabsai/curator/blob/fab184b26578429568c39c6b1e6b1d67e1650ae1/.github/workflows/lint-and-test.yaml) |

<a id="n2-2026-11-24"></a>

## Nâng trần đợt hai — 23/11/2026

Hồ sơ lập trong đợt nâng trần thứ hai: đọc mã hoặc tài liệu tại commit cố định, chưa chạy upstream; mô tả của trinh sát sai ở nhiều repo nên điều ghi ở đây là điều đã đọc.

<a id="n2-lakekeeper-lakekeeper"></a>

### Lakekeeper

| Thuộc tính | Giá trị |
|---|---|
| Repo | https://github.com/lakekeeper/lakekeeper |
| License | Apache-2.0 |
| Phiên bản đã đọc | `4e05f79682b11ab04ec2ec5fc75814a98858d850` (commit 2026-11-23) |
| Kiểm chứng | 2026-11-24; code-read; đã đọc service/authz/mod.rs, server/s3_signer/policy.rs, docs/docs/authorization.md và authorization-cedar.md, workflow integration.yml và unittests.yml; chưa chạy upstream |
| Khoảng trống lấp | Catalog/metadata đa engine và quản trị truy cập (Iceberg REST Catalog) |
| Cơ chế đáng học | • Trait `Authorizer` (service/authz/mod.rs) tách quyết định truy cập khỏi catalog; có OpenFGA (mã nguồn mở), AllowAll và bản tự viết; kiểu hành động theo cấp server, project, warehouse, namespace, table, view.<br>• Cấp quyền đọc ghi kho dữ liệu bằng credential tạm thời (vended credentials) hoặc remote signing cho S3, Azure, GCS; bộ ký S3 (s3_signer/policy.rs) từ chối tham số truy vấn và header `x-` không nằm trong danh sách cho phép, từ chối tham số trùng.<br>• Sự kiện thay đổi dạng CloudEvents (NATS, Kafka) và giao diện `ContractVerification` để chặn thay đổi từ hệ thống ngoài; lưu trạng thái trong Postgres nên mở rộng ngang. |
| Tiêu chí và cách kiểm | Unittests có cổng bắt buộc (sqlx-check, format, clippy, openapi sinh khớp, MSRV, cargo-audit, unused-deps). integration.yml dựng ảnh server rồi chạy ma trận pyiceberg, starrocks, trino, trino với OPA, spark với OpenFGA... Không thấy bộ conformance riêng cho đặc tả REST: mô tả của trinh sát (kiểm qua conformance REST spec) chỉ đúng theo nghĩa kiểm tích hợp với các engine, không phải bộ kiểm đặc tả độc lập. |
| Giới hạn và rủi ro | Apache-2.0, nhưng Cedar (quyền dạng policy-as-code) chỉ có ở Lakekeeper Plus (bản thương mại, docs ghi rõ), bản mở dùng OpenFGA tức phải chạy thêm dịch vụ. Chỉ backend Postgres >=15. Không biểu diễn row filter hay column mask (docs authorization.md). Chưa tìm thấy telemetry gửi ra ngoài (tìm theo từ khóa, chưa quét toàn bộ). Sao 1516 do trinh sát ghi (chưa xác minh). |
| So với | apache-iceberg, apache-gravitino, polaris (lưu ý id polaris trong kho là thư viện UI Shopify, khác Apache Polaris), unitycatalog-unitycatalog |
| Nguồn | [LICENSE](https://github.com/lakekeeper/lakekeeper/blob/4e05f79682b11ab04ec2ec5fc75814a98858d850/LICENSE) · [README.md](https://github.com/lakekeeper/lakekeeper/blob/4e05f79682b11ab04ec2ec5fc75814a98858d850/README.md) · [NOTICE](https://github.com/lakekeeper/lakekeeper/blob/4e05f79682b11ab04ec2ec5fc75814a98858d850/NOTICE) · [authorization.md](https://github.com/lakekeeper/lakekeeper/blob/4e05f79682b11ab04ec2ec5fc75814a98858d850/docs/docs/authorization.md) · [authorization-cedar.md](https://github.com/lakekeeper/lakekeeper/blob/4e05f79682b11ab04ec2ec5fc75814a98858d850/docs/docs/authorization-cedar.md) · [mod.rs](https://github.com/lakekeeper/lakekeeper/blob/4e05f79682b11ab04ec2ec5fc75814a98858d850/crates/lakekeeper/src/service/authz/mod.rs) · [policy.rs](https://github.com/lakekeeper/lakekeeper/blob/4e05f79682b11ab04ec2ec5fc75814a98858d850/crates/lakekeeper/src/server/s3_signer/policy.rs) · [integration.yml](https://github.com/lakekeeper/lakekeeper/blob/4e05f79682b11ab04ec2ec5fc75814a98858d850/.github/workflows/integration.yml) · [unittests.yml](https://github.com/lakekeeper/lakekeeper/blob/4e05f79682b11ab04ec2ec5fc75814a98858d850/.github/workflows/unittests.yml) |

<a id="n2-unitycatalog-unitycatalog"></a>

### Unity Catalog (OSS)

| Thuộc tính | Giá trị |
|---|---|
| Repo | https://github.com/unitycatalog/unitycatalog |
| License | Apache-2.0 |
| Phiên bản đã đọc | `d5b5b0de3d84688332619d561e4daa4d031356b7` (commit 2026-11-23) |
| Kiểm chứng | 2026-11-24; code-read; đã đọc auth/UnityCatalogAuthorizer.java, auth/AuthorizeExpressions.java, auth/JCasbinAuthorizer.java, etc/conf/server.properties, roadmap.md, workflow unit-tests.yml; chưa chạy upstream |
| Khoảng trống lấp | Catalog/metadata đa engine và quản trị truy cập (bảng, volume, hàm, mô hình AI) |
| Cơ chế đáng học | • Giao diện `UnityCatalogAuthorizer` (grant, revoke, hierarchy parent-child, `authorize`, `authorizeAny`) với hai bản: JCasbin lưu luật trong bảng `casbin_rule` và đồng bộ định kỳ giữa các instance, hoặc OPA gọi qua `server.authorization.opa.decision-url`.<br>• Quy tắc quyền khai báo bằng biểu thức trên annotation `@AuthorizeExpression`, gom hằng số dùng chung (AuthorizeExpressions.java) để hai endpoint cấp credential cho cùng thao tác không lệch nhau; cờ `strict-privilege-checks` bật mặc định.<br>• Cấp credential tạm thời theo bảng, volume, đường dẫn, mô hình qua `StorageCredentialVendor` (AWS, Azure, GCP) và có ghi audit; lộ API riêng cùng tương thích Iceberg REST và Hive metastore (theo README, chưa kiểm). |
| Tiêu chí và cách kiểm | CI unit-tests chạy ma trận Spark và Delta (kể cả bản nguồn), có Postgres/MySQL, thêm workflow Python client, helm chart, upgrade-tests; nhiều workflow đã bị tắt (tiền tố disabled_). Kiểm bằng máy, chưa chạy ở đây. |
| Giới hạn và rủi ro | Apache-2.0; dự án sandbox của LF AI & Data, phiên bản 0.8.0-SNAPSHOT (chưa 1.0). Phân quyền mặc định tắt (`server.authorization=disable` trong server.properties), cần cấu hình issuer OIDC trước khi bật. Thông số trinh sát (sao, license) chưa xác minh nay đã xác nhận license Apache-2.0. Lộ trình ghi Iceberg REST đầy đủ và S3 tương thích là việc còn phải làm (roadmap.md), nên đừng giả định hỗ trợ đầy đủ. |
| So với | apache-gravitino, apache-iceberg, openmetadata, lakekeeper-lakekeeper |
| Nguồn | [LICENSE](https://github.com/unitycatalog/unitycatalog/blob/d5b5b0de3d84688332619d561e4daa4d031356b7/LICENSE) · [README.md](https://github.com/unitycatalog/unitycatalog/blob/d5b5b0de3d84688332619d561e4daa4d031356b7/README.md) · [roadmap.md](https://github.com/unitycatalog/unitycatalog/blob/d5b5b0de3d84688332619d561e4daa4d031356b7/roadmap.md) · [server.properties](https://github.com/unitycatalog/unitycatalog/blob/d5b5b0de3d84688332619d561e4daa4d031356b7/etc/conf/server.properties) · [UnityCatalogAuthorizer.java](https://github.com/unitycatalog/unitycatalog/blob/d5b5b0de3d84688332619d561e4daa4d031356b7/server/src/main/java/io/unitycatalog/server/auth/UnityCatalogAuthorizer.java) · [AuthorizeExpressions.java](https://github.com/unitycatalog/unitycatalog/blob/d5b5b0de3d84688332619d561e4daa4d031356b7/server/src/main/java/io/unitycatalog/server/auth/AuthorizeExpressions.java) · [JCasbinAuthorizer.java](https://github.com/unitycatalog/unitycatalog/blob/d5b5b0de3d84688332619d561e4daa4d031356b7/server/src/main/java/io/unitycatalog/server/auth/JCasbinAuthorizer.java) · [unit-tests.yml](https://github.com/unitycatalog/unitycatalog/blob/d5b5b0de3d84688332619d561e4daa4d031356b7/.github/workflows/unit-tests.yml) |

<a id="n2-synthetic-data-kit"></a>

### Synthetic Data Kit

| Thuộc tính | Giá trị |
|---|---|
| Repo | https://github.com/meta-llama/synthetic-data-kit |
| License | MIT |
| Phiên bản đã đọc | `27a5541b2cc3537954c381eafc5398ab0838a397` (commit 2025-10-25) |
| Kiểm chứng | 2026-11-24; code-read; đã đọc README.md, LICENSE, pyproject.toml, synthetic_data_kit/config.yaml và một số file khác; chưa chạy upstream |
| Khoảng trống lấp | Sinh dữ liệu tổng hợp QA/CoT từ tài liệu để fine-tune, kèm bước lọc bằng LLM judge |
| Cơ chế đáng học | • CLI bốn bước `ingest`, `create`, `curate`, `save-as`, thư mục đầu ra tách theo giai đoạn (config.yaml `paths`).<br>• Parser theo định dạng (`parsers/` có pdf, html, docx, ppt, txt, youtube) và generator QA, CoT, VQA (`generators/`).<br>• `curate` cho LLM chấm từng cặp từ 1 đến 10 theo batch nhỏ, nhiệt độ 0.1, giữ cặp có điểm từ ngưỡng 7.0 trở lên (`core/curate.py`, prompt `qa_rating` trong config).<br>• Prompt và tham số nằm cả trong YAML nên chỉnh được không sửa mã. |
| Tiêu chí và cách kiểm | Judge chấm 1 đến 10 theo bốn tiêu chí (accuracy 0 đến 3, relevance 0 đến 2, clarity 0 đến 2, usefulness 0 đến 3) và lọc theo ngưỡng; không có kiểm độc lập ngoài LLM. CI chạy pre-commit/ruff và pytest trên Python 3.8 đến 3.12 với khóa API giả cùng `synthetic-data-kit system-check` (ci.yml); tôi chưa mở nội dung thư mục tests. |
| Giới hạn và rủi ro | Khóa `enable_deduplication` và `similarity_threshold` có trong config nhưng grep toàn mã Python không thấy chỗ đọc, nên tuyên bố khử trùng lặp chưa có tác dụng ở commit này. Mặc định `provider` là `api-endpoint` tới api.llama.com nên nội dung tài liệu rời máy, chuyển sang vLLM cục bộ mới giữ dữ liệu tại chỗ. Phụ thuộc trực tiếp gồm PyMuPDF (theo hiểu biết của tôi là AGPL hoặc thương mại, chưa xác minh trong repo) và pytube. Phiên bản 0.0.5b1, commit cuối 2025-10-25. Chất lượng dữ liệu phụ thuộc model sinh và model chấm. |
| So với | distilabel, bespoke-curator, argilla, datatrove |
| Nguồn | [README.md](https://github.com/meta-llama/synthetic-data-kit/blob/27a5541b2cc3537954c381eafc5398ab0838a397/README.md) · [LICENSE](https://github.com/meta-llama/synthetic-data-kit/blob/27a5541b2cc3537954c381eafc5398ab0838a397/LICENSE) · [pyproject.toml](https://github.com/meta-llama/synthetic-data-kit/blob/27a5541b2cc3537954c381eafc5398ab0838a397/pyproject.toml) · [config.yaml](https://github.com/meta-llama/synthetic-data-kit/blob/27a5541b2cc3537954c381eafc5398ab0838a397/synthetic_data_kit/config.yaml) · [curate.py](https://github.com/meta-llama/synthetic-data-kit/blob/27a5541b2cc3537954c381eafc5398ab0838a397/synthetic_data_kit/core/curate.py) · [ci.yml](https://github.com/meta-llama/synthetic-data-kit/blob/27a5541b2cc3537954c381eafc5398ab0838a397/.github/workflows/ci.yml) |

<a id="n2-deduplicate-text-datasets"></a>

### Deduplicate Text Datasets (ExactSubstr)

| Thuộc tính | Giá trị |
|---|---|
| Repo | https://github.com/google-research/deduplicate-text-datasets |
| License | Apache-2.0 |
| Phiên bản đã đọc | `4e9888ac3f95dc4f6169867a04c4c19df02dafe3` (commit 2024-05-21) |
| Kiểm chứng | 2026-11-24; code-read; đã đọc README.md, LICENSE, Cargo.toml, src/main.rs và một số file khác; chưa chạy upstream |
| Khoảng trống lấp | Khử trùng lặp chính xác bằng suffix array và phát hiện trùng giữa train và test |
| Cơ chế đáng học | • Dựng suffix array trên toàn bộ dataset ghép thành một file byte (`make`, `make_part`, `merge` trong `src/main.rs`; `table.rs` phỏng theo thư viện suffix của BurntSushi).<br>• `self-similar` tìm mọi chuỗi con lặp từ `length-threshold` byte trở lên trong một dataset; `across-similar` so hai dataset (dùng cho rò rỉ train/test); `collect` gộp thành khoảng byte cần xóa.<br>• `count-occurrences` đếm số lần một chuỗi xuất hiện trong O(log N). |
| Tiêu chí và cách kiểm | Khớp chính xác theo byte nên kiểm được: README hướng dẫn chạy lại trên kết quả (3374227 trùng còn 374 sau một lượt, chưa xác minh) và đối chiếu `grep -c`. Không có test và không có CI trong repo. Ngưỡng `length-threshold` phụ thuộc dataset (bài báo dùng 50 token, tương đương 100 byte theo README). |
| Giới hạn và rủi ro | Là mã nghiên cứu, README tự nói có thể không làm đúng điều bạn cần và không phải sản phẩm Google chính thức. Commit cuối 2024-05-21, phụ thuộc Cargo cũ (clap 3.1, zstd 0.5, crossbeam 0.3). `scripts/run_pipeline.sh` gọi `collect --data-name` trong khi CLI trong main.rs chỉ có `--data-file`, nên script mẫu lỗi thời. Chỉ khử trùng lặp chính xác, phần NearDup chỉ phát hành cụm kết quả, không kèm mã. Đòi nhiều RAM (C4 khoảng 300GB cần trên 600GB RAM theo README). Việc ghi lại dataset sau khi xóa phải tự viết, chỉ có script cho wiki40b. |
| So với | datasketch (gần trùng MinHash), datatrove, nemo-curator |
| Nguồn | [README.md](https://github.com/google-research/deduplicate-text-datasets/blob/4e9888ac3f95dc4f6169867a04c4c19df02dafe3/README.md) · [LICENSE](https://github.com/google-research/deduplicate-text-datasets/blob/4e9888ac3f95dc4f6169867a04c4c19df02dafe3/LICENSE) · [Cargo.toml](https://github.com/google-research/deduplicate-text-datasets/blob/4e9888ac3f95dc4f6169867a04c4c19df02dafe3/Cargo.toml) · [main.rs](https://github.com/google-research/deduplicate-text-datasets/blob/4e9888ac3f95dc4f6169867a04c4c19df02dafe3/src/main.rs) · [run_pipeline.sh](https://github.com/google-research/deduplicate-text-datasets/blob/4e9888ac3f95dc4f6169867a04c4c19df02dafe3/scripts/run_pipeline.sh) |

<a id="n2-detect-pretrain-code"></a>

### Min-K% Prob (detect-pretrain-code)

| Thuộc tính | Giá trị |
|---|---|
| Repo | https://github.com/swj0419/detect-pretrain-code |
| License | Apache-2.0 (file LICENSE, văn bản Apache 2.0 nguyên bản) |
| Phiên bản đã đọc | `a5048f93c4fa6491aab0638bb3e6fd5a662d7698` (commit 2023-11-03) |
| Kiểm chứng | 2026-11-24; code-read; đã đọc README.md, LICENSE, src/run.py, src/eval.py, process_data.py; chưa chạy upstream |
| Khoảng trống lấp | Chống rò rỉ dữ liệu huấn luyện: kiểm một đoạn văn bản có thể đã nằm trong dữ liệu huấn luyện của một LLM hay chưa (membership inference), dùng để dò nhiễm bẩn benchmark |
| Cơ chế đáng học | - Min-K% Prob: `np.sort(all_prob)[:k]` lấy k% log-xác suất thấp nhất rồi lấy trung bình đảo dấu; quét k = 5, 10, 20, 30, 40, 50, 60% trong một lần chạy (`src/run.py`, hàm `inference`). <br>- Bốn baseline cùng lượt: `ppl`, hiệu log-likelihood giữa mô hình đích và mô hình tham chiếu, tỉ số `ppl/zlib`, tỉ số `ppl/lowercase_ppl` (`src/run.py`). <br>- Đánh giá: `sweep` dựng đường ROC rồi báo AUC, độ chính xác và TPR tại FPR thấp; `fig_fpr_tpr` ghi `auc.txt` và `auc.png` (`src/eval.py`). <br>- Hai tập đo đi kèm trên Hugging Face: WikiMIA (độ dài 32/64/128/256) và BookMIA (512), nhãn 0 là chưa thấy, 1 là đã thấy (README). |
| Tiêu chí và cách kiểm | Có tiêu chí định lượng (AUC, TPR tại FPR nhỏ) tính bằng `sklearn.metrics.roc_curve` trên tập có nhãn; không có test tự động, không workflow CI, không file requirements trong repo. Hiệu lực trên dữ liệu thật của dự án khác là **(chưa xác minh)**; README tự dặn dùng đầu vào cùng độ dài. |
| Giới hạn và rủi ro | Mã nghiên cứu, commit cuối 2023-11-03, không thấy bảo trì sau đó. Nhánh OpenAI dùng `openai.Completion.create(engine=..., echo=True, logprobs=5)` kiểu SDK cũ và khoá API gán cứng trong mã (cần tự sửa); mô hình `text-davinci-*` còn gọi được hay không là **(chưa xác minh)**. `eval.py` in "TPR@5%FPR" ra console nhưng ghi "TPR@0.1%FPR" vào `auc.txt` cho cùng một giá trị `fpr<.05`: nhãn sai, đừng trích số từ file. README ghi độ dài "54" (chắc là 64). `process_data.py` có đường dẫn cứng `/fsx-...` và import `ipdb`. Cần tải mô hình và dữ liệu Hugging Face (dữ liệu rời máy khi tải về). Dùng để dò nhiễm bẩn chỉ cho tín hiệu thống kê, không phải bằng chứng một văn bản có trong tập huấn luyện. |
| So với | datatrove và datasketch (khử trùng lặp, cùng nhóm data-curation nhưng làm theo băm/MinHash chứ không dùng logit mô hình); data-juicer, nemo-curator (lọc/làm sạch corpus, không dò nhiễm bẩn benchmark). |
| Nguồn | [README](https://github.com/swj0419/detect-pretrain-code/blob/a5048f93c4fa6491aab0638bb3e6fd5a662d7698/README.md) · [LICENSE](https://github.com/swj0419/detect-pretrain-code/blob/a5048f93c4fa6491aab0638bb3e6fd5a662d7698/LICENSE) · [run.py](https://github.com/swj0419/detect-pretrain-code/blob/a5048f93c4fa6491aab0638bb3e6fd5a662d7698/src/run.py) · [eval.py](https://github.com/swj0419/detect-pretrain-code/blob/a5048f93c4fa6491aab0638bb3e6fd5a662d7698/src/eval.py) · [process_data.py](https://github.com/swj0419/detect-pretrain-code/blob/a5048f93c4fa6491aab0638bb3e6fd5a662d7698/process_data.py) |

<a id="n2-meltano"></a>

### Meltano

| Thuộc tính | Giá trị |
|---|---|
| Repo | https://github.com/meltano/meltano |
| License | MIT |
| Phiên bản đã đọc | `3913352432f32632e16807142111455d5f64cb89` (commit 2026-11-12) |
| Kiểm chứng | 2026-11-24; code-read; đã đọc README, LICENSE, bundle/settings.yml, plugin_test_service.py, validation_service.py, state_store/base.py, tracking/README.md, pyproject.toml, test.yml; chưa chạy upstream |
| Khoảng trống lấp | ELT khai báo theo Singer và kiểm thử extractor/loader |
| Cơ chế đáng học | - Cấu hình dự án khai báo trong `meltano.yml`; plugin (extractor, loader, transform, utility) cài vào venv riêng và gọi qua `plugin_invoker`.<br>- `plugin_test_service.py`: `meltano test` với extractor chạy plugin và đọc dòng Singer, chỉ đạt khi thấy ít nhất một thông điệp RECORD hoặc BATCH, rồi dừng tiến trình; với loader gửi thông điệp thử và cảnh báo sẽ ghi bảng `meltano_test_stream` vào đích thật.<br>- `validation_service.py`: kiểm dữ liệu qua plugin utility, kết quả SUCCESS hoặc FAILURE từ exit code.<br>- `state_store/` trừu tượng hóa nơi lưu bookmark (hệ thống DB, filesystem, S3, Azure, Google) với `StateIDLockedError` để khóa theo state id, cho phép chạy gia tăng lặp lại. |
| Tiêu chí và cách kiểm | CI `test.yml` chạy khi PR, push, merge group (đã mở phần đầu workflow); có workflow benchmark, CodeQL, zizmor, dependency-review, integration. Test hợp lệ extractor chỉ là kiểm 'có ra bản ghi', không kiểm độ đúng dữ liệu. Chưa chạy; chưa đọc ngưỡng độ phủ. |
| Giới hạn và rủi ro | MIT (bản quyền Arch Data, Inc.). Usage tracking qua Snowplow: `send_anonymous_usage_stats` có `value: true` (bật mặc định) trong `settings.yml`; tắt bằng cài đặt hoặc `disable_tracking`; có `project_id` để định danh dự án. `meltano test` loader ghi dữ liệu thử vào đích. Là bộ điều phối ELT chứ không phải bộ biến đổi hay lược đồ dữ liệu; chất lượng phụ thuộc từng plugin Singer (tap/target) do cộng đồng viết. Đo 600+ nguồn là tuyên bố của README (chưa xác minh). |
| So với | Airbyte (`airbytehq-airbyte`) có connector đóng gói container; dlt (`dlt-data-load-tool`) viết pipeline bằng Python; Dagster (`dagster`) là orchestrator có asset; SQLMesh (`sqlmesh`) tập trung biến đổi. |
| Nguồn | [README](https://github.com/meltano/meltano/blob/3913352432f32632e16807142111455d5f64cb89/README.md) · [LICENSE](https://github.com/meltano/meltano/blob/3913352432f32632e16807142111455d5f64cb89/LICENSE) · [settings.yml](https://github.com/meltano/meltano/blob/3913352432f32632e16807142111455d5f64cb89/src/meltano/core/bundle/settings.yml) · [plugin_test_service.py](https://github.com/meltano/meltano/blob/3913352432f32632e16807142111455d5f64cb89/src/meltano/core/plugin_test_service.py) · [validation_service.py](https://github.com/meltano/meltano/blob/3913352432f32632e16807142111455d5f64cb89/src/meltano/core/validation_service.py) · [state_store/base.py](https://github.com/meltano/meltano/blob/3913352432f32632e16807142111455d5f64cb89/src/meltano/core/state_store/base.py) · [tracking/README](https://github.com/meltano/meltano/blob/3913352432f32632e16807142111455d5f64cb89/src/meltano/core/tracking/README.md) · [pyproject.toml](https://github.com/meltano/meltano/blob/3913352432f32632e16807142111455d5f64cb89/pyproject.toml) · [test.yml](https://github.com/meltano/meltano/blob/3913352432f32632e16807142111455d5f64cb89/.github/workflows/test.yml) |

<a id="n2-fiftyone"></a>

### FiftyOne

| Thuộc tính | Giá trị |
|---|---|
| Repo | https://github.com/voxel51/fiftyone |
| License | Apache-2.0 |
| Phiên bản đã đọc | `ba7162b57857c24c23972197320e6328c6db6b70` (commit 2026-11-20) |
| Kiểm chứng | 2026-11-24; code-read; đã đọc README.md, LICENSE, setup.py, config.py, service.py; chưa chạy upstream |
| Khoảng trống lấp | Quản trị chất lượng dữ liệu thị giác: duyệt, truy vấn, đánh giá mô hình trên từng mẫu và nối vòng lặp gắn nhãn |
| Cơ chế đáng học | • `fiftyone/utils/eval/detection.py::evaluate_detections`: đánh giá detection/instance/polygon/keypoint/temporal, tham số `iou=0.50`, `classwise`, `custom_metrics`, ghi kết quả vào từng sample dưới `eval_key` để lọc TP/FP/FN trong App.<br>• `fiftyone/utils/*.py` có tích hợp annotation hai chiều (`cvat.py`, `labelstudio.py`, `labelbox.py`, `scale.py`, `annotations.py`) cho vòng lặp gửi nhãn rồi nhập lại.<br>• `fiftyone/core/config.py` quản lý cấu hình bằng biến môi trường `FIFTYONE_*` (backend đánh giá, `default_segmentation_backend`...), tách bằng lớp config thay được.<br>• `package/db` đóng gói binary MongoDB tải từ fastdl.mongodb.org để chạy CSDL cục bộ không cần cài sẵn. |
| Tiêu chí và cách kiểm | CI `test.yml` (đã đọc) chạy pytest qua `tests/utils/pytest_wrapper.py` trên ma trận Python và OS (có job Windows riêng), có coverage, loại trừ `benchmarking`, `isolated`, `intensive`; `pr.yml` chạy lint và nhiều job (image CI prebaked trong registry riêng, không tái dựng ngoài tổ chức). Chưa chạy. Chất lượng lỗi nhãn do `fiftyone-brain` quyết định, chưa đọc ở hồ sơ này. |
| Giới hạn và rủi ro | Apache-2.0 cho repo (LICENSE và package/db/LICENSE đều Apache-2.0). Telemetry: `do_not_track` mặc định False, docs ghi "UUID import và sự kiện dùng App" được theo dõi, App có `@segment/analytics-next`; tắt bằng `FIFTYONE_DO_NOT_TRACK=true`. Gói `fiftyone-db` tải MongoDB 7.0 từ fastdl.mongodb.org: license của binary MongoDB là điều khoản riêng của MongoDB (theo hiểu biết chung, chưa xác minh trong repo) nên cần xét khi phân phối lại. Có bản thương mại Voxel51 Teams/Enterprise (README), một số tính năng tập thể nằm ngoài bản mở. Repo có `enterprise-sync.yml` và nhánh community nên lịch sử qua đồng bộ. |
| So với | cvat và label-studio (công cụ gắn nhãn; FiftyOne kết nối với chúng); cleanlab (phát hiện lỗi nhãn bằng thuật toán, tương ứng phần fiftyone-brain); nemo-curator (chuẩn bị dữ liệu quy mô lớn) |
| Nguồn | [README.md](https://github.com/voxel51/fiftyone/blob/ba7162b57857c24c23972197320e6328c6db6b70/README.md) · [LICENSE](https://github.com/voxel51/fiftyone/blob/ba7162b57857c24c23972197320e6328c6db6b70/LICENSE) · [setup.py](https://github.com/voxel51/fiftyone/blob/ba7162b57857c24c23972197320e6328c6db6b70/setup.py) · [config.py](https://github.com/voxel51/fiftyone/blob/ba7162b57857c24c23972197320e6328c6db6b70/fiftyone/core/config.py) · [service.py](https://github.com/voxel51/fiftyone/blob/ba7162b57857c24c23972197320e6328c6db6b70/fiftyone/core/service.py) · [detection.py](https://github.com/voxel51/fiftyone/blob/ba7162b57857c24c23972197320e6328c6db6b70/fiftyone/utils/eval/detection.py) · [setup.py](https://github.com/voxel51/fiftyone/blob/ba7162b57857c24c23972197320e6328c6db6b70/package/db/setup.py) · [test.yml](https://github.com/voxel51/fiftyone/blob/ba7162b57857c24c23972197320e6328c6db6b70/.github/workflows/test.yml) · [config.rst](https://github.com/voxel51/fiftyone/blob/ba7162b57857c24c23972197320e6328c6db6b70/docs/source/user_guide/config.rst) |
