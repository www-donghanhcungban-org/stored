# 26 · Document Intelligence, OCR & Structured Extraction

Từ ảnh/PDF đến dữ liệu có cấu trúc kèm bằng chứng. Ngày đọc **2026-11-02**: đã đọc LICENSE, README, CI và các file triển khai được dẫn; **không cài, chạy model hoặc tái lập benchmark**. Điểm số và giá do tác giả công bố không phải kết quả của kho.

## 1. Chọn đúng lớp xử lý

| Đầu vào / nhu cầu | Hướng ưu tiên | Phải kiểm trước khi chọn |
|---|---|---|
| PDF có lớp text tốt, cần trích văn bản | Parser native/Docling (đã có mục 10) | Thứ tự đọc, text ẩn/sai encoding, bảng và tọa độ |
| Scan sạch, CPU, cần searchable PDF | Tesseract + OCRmyPDF | Language pack `vie`, DPI, xoay/nghiêng; searchable không có nghĩa hiểu bảng |
| Bảng, công thức, layout phức tạp | PP-StructureV3; so Docling/Marker/MinerU | Chất lượng từng thành phần, model revision, quyền weights |
| Corpus PDF cho LLM | olmOCR, có đánh dấu fallback và lỗi trang | Ngôn ngữ/domain, trang bị loại, tốc độ/chi phí trên corpus riêng |
| Hóa đơn/hợp đồng ra JSON | Parser + schema extractor + đối chiếu trường | Citation trang/bbox, tổng tiền/đơn vị, trường thiếu phải null |
| So sánh parser | OmniDocBench + tập tài liệu đích | Version dữ liệu/metric, contamination, không suy điểm công khai sang tiếng Việt |

**Ranh giới:** mục 16 là tài liệu phần mềm/docs-for-AI; mục 10 là retrieval/memory; mục này giữ độ trung thực khi biến tài liệu gốc thành dữ liệu. Docling có hồ sơ gốc ở [10 §6b](../10-local-llm-rag-memory/README.md#6b-nâng-cấp-31102026-rà-repo-lớn), không thêm bản ghi trùng.

## 2. Hồ sơ và bằng chứng

### PaddleOCR

| Thuộc tính | Giá trị |
|---|---|
| Repo | [PaddlePaddle/PaddleOCR](https://github.com/PaddlePaddle/PaddleOCR) |
| Snapshot | 92,120★, chưa archive (GitHub API, 2026-11-02); HEAD `dab3fe353790` ngày 2026-09-16 |
| License | Apache-2.0 (code); weights kiểm riêng; [file thật](https://github.com/PaddlePaddle/PaddleOCR/blob/dab3fe35379033fdcb2d0e9572fac0b36c9a9ebf/LICENSE) |
| Bằng chứng | [Triển khai/đặc tả](https://github.com/PaddlePaddle/PaddleOCR/blob/dab3fe35379033fdcb2d0e9572fac0b36c9a9ebf/paddleocr/_pipelines/pp_structurev3.py); [CI tại cùng commit](https://github.com/PaddlePaddle/PaddleOCR/tree/dab3fe35379033fdcb2d0e9572fac0b36c9a9ebf/.github/workflows); đọc mã/đặc tả, chưa chạy |

PP-StructureV3 tách layout/OCR/table và có phép ghép Markdown nhiều trang; wrapper kiểm tổ hợp language/OCR version. Nên so pipeline có tọa độ với VLM theo loại tài liệu, không lấy một điểm SOTA của README đại diện mọi tác vụ.

**Tích hợp và giới hạn:** API Python/pipeline qua PaddleX; ghim backend và model revision. Quyền từng checkpoint và độ đúng biểu mẫu tiếng Việt chưa xác minh; chưa chạy CPU/GPU.

### olmOCR

| Thuộc tính | Giá trị |
|---|---|
| Repo | [allenai/olmocr](https://github.com/allenai/olmocr) |
| Snapshot | 19,814★, chưa archive (GitHub API, 2026-11-02); HEAD `f7cfe4c22098` ngày 2026-03-25 |
| License | Apache-2.0 (code); weights kiểm riêng; [file thật](https://github.com/allenai/olmocr/blob/f7cfe4c22098b154c76b6ec950d1c0a464eecf8d/LICENSE) |
| Bằng chứng | [Triển khai/đặc tả](https://github.com/allenai/olmocr/blob/f7cfe4c22098b154c76b6ec950d1c0a464eecf8d/olmocr/pipeline.py); [CI tại cùng commit](https://github.com/allenai/olmocr/tree/f7cfe4c22098b154c76b6ec950d1c0a464eecf8d/.github/workflows); đọc mã/đặc tả, chưa chạy |

Pipeline có retry, kiểm xoay và cờ is_fallback; mức fallback quá ngưỡng có thể loại cả tài liệu. --apply_filter là opt-in và filter trong mã giữ English/unknown, nên không bật như một bước làm sạch chung cho corpus tiếng Việt.

**Tích hợp và giới hạn:** Local GPU hoặc endpoint tương thích OpenAI; ghi lại trang fallback/bị bỏ. README có giá và benchmark do nhóm công bố, kho chưa tái lập; không suy giá đó sang hạ tầng khác.

### OCRmyPDF

| Thuộc tính | Giá trị |
|---|---|
| Repo | [ocrmypdf/OCRmyPDF](https://github.com/ocrmypdf/OCRmyPDF) |
| Snapshot | 35,208★, chưa archive (GitHub API, 2026-11-02); HEAD `b457e9efa68c` ngày 2026-10-25 |
| License | MPL-2.0 (code); dependency licenses riêng; [file thật](https://github.com/ocrmypdf/OCRmyPDF/blob/b457e9efa68c3a46be2470ffb222ed1bccc4dcbc/LICENSE) |
| Bằng chứng | [Triển khai/đặc tả](https://github.com/ocrmypdf/OCRmyPDF/blob/b457e9efa68c3a46be2470ffb222ed1bccc4dcbc/src/ocrmypdf/_validation.py); [CI tại cùng commit](https://github.com/ocrmypdf/OCRmyPDF/tree/b457e9efa68c3a46be2470ffb222ed1bccc4dcbc/.github/workflows); đọc mã/đặc tả, chưa chạy |

Thêm lớp text để tìm kiếm trong PDF scan, có kiểm language pack tồn tại trước xử lý. Vai trò khác parser hiểu layout/schema; phù hợp bảo toàn PDF với OCR cơ bản.

**Tích hợp và giới hạn:** CLI/Python API nối Tesseract; kiểm version Ghostscript, language vie, sandbox và trần tài nguyên. PDF/A/searchable không chứng minh bảng/trường trích đúng.

### Tesseract

| Thuộc tính | Giá trị |
|---|---|
| Repo | [tesseract-ocr/tesseract](https://github.com/tesseract-ocr/tesseract) |
| Snapshot | 77,298★, chưa archive (GitHub API, 2026-11-02); HEAD `d1ebd2a789f8` ngày 2026-11-02 |
| License | Apache-2.0; [file thật](https://github.com/tesseract-ocr/tesseract/blob/d1ebd2a789f8220209d675c1d4bc18d7a25c8e26/LICENSE) |
| Bằng chứng | [Triển khai/đặc tả](https://github.com/tesseract-ocr/tesseract/blob/d1ebd2a789f8220209d675c1d4bc18d7a25c8e26/src/api/baseapi.cpp); [CI tại cùng commit](https://github.com/tesseract-ocr/tesseract/tree/d1ebd2a789f8220209d675c1d4bc18d7a25c8e26/.github/workflows); đọc mã/đặc tả, chưa chạy |

Engine OCR cổ điển có API Init/Recognize và xuất hOCR/TSV; làm baseline CPU để đo lợi ích thật của model lớn. Language pack là artifact phải ghim riêng.

**Tích hợp và giới hạn:** Thư viện C++/CLI, hoặc qua OCRmyPDF. Độ đúng phụ thuộc preprocessing/segmentation; không tự hiểu quan hệ bảng, ngữ nghĩa hóa đơn hay citation RAG.

### MinerU

| Thuộc tính | Giá trị |
|---|---|
| Repo | [opendatalab/MinerU](https://github.com/opendatalab/MinerU) |
| Snapshot | 82,987★, chưa archive (GitHub API, 2026-11-02); HEAD `0ef2c20c4a56` ngày 2026-10-30 |
| License | Apache-2.0 + điều khoản bổ sung; [file thật](https://github.com/opendatalab/MinerU/blob/0ef2c20c4a56e68f81a66647f819d924ef2d89ce/LICENSE.md) |
| Bằng chứng | [Triển khai/đặc tả](https://github.com/opendatalab/MinerU/blob/0ef2c20c4a56e68f81a66647f819d924ef2d89ce/mineru/cli/commands/parse.py); [CI tại cùng commit](https://github.com/opendatalab/MinerU/tree/0ef2c20c4a56e68f81a66647f819d924ef2d89ce/.github/workflows); đọc mã/đặc tả, chưa chạy |

Reader cho agent có parse/read theo trang/block và locator ổn định. CLI thư viện tài liệu mặc định chỉ đọc nhóm trang đầu theo README, nên consumer phải đi tiếp theo continuation và kiểm tổng trang.

**Tích hợp và giới hạn:** License thật yêu cầu giấy phép riêng khi bạn và Affiliates tính gộp có MAU vượt 100 triệu hoặc doanh thu tháng vượt 20 triệu USD; dịch vụ online phải attribution. Không gắn nhãn Apache thuần/OSI. Ghim cache/config/model; quyền weights và độ bền locator sau thay tài liệu cần kiểm riêng.

### Marker

| Thuộc tính | Giá trị |
|---|---|
| Repo | [datalab-to/marker](https://github.com/datalab-to/marker) |
| Snapshot | 40,748★, chưa archive (GitHub API, 2026-11-02); HEAD `71dd5fd7e51a` ngày 2026-10-29 |
| License | Apache-2.0 (code); modified OpenRAIL-M (weights); [file thật](https://github.com/datalab-to/marker/blob/71dd5fd7e51ab24f8624b6ba2fcb6014b4e40ed4/LICENSE) |
| Bằng chứng | [Triển khai/đặc tả](https://github.com/datalab-to/marker/blob/71dd5fd7e51ab24f8624b6ba2fcb6014b4e40ed4/marker/converters/pdf.py); [CI tại cùng commit](https://github.com/datalab-to/marker/tree/71dd5fd7e51ab24f8624b6ba2fcb6014b4e40ed4/.github/workflows); đọc mã/đặc tả, chưa chạy |

PdfConverter dựng Document qua provider/builder/processor rồi renderer, cho phép output Markdown/JSON và xử lý riêng block. Cần đo lỗi từng tầng, nhất là khi thêm LLM sửa kết quả OCR.

**Tích hợp và giới hạn:** README tách code Apache khỏi model weights: sử dụng weights thương mại vượt điều kiện miễn phí cần license riêng. Không coi license code bao trùm weights; tắt/kiểm endpoint LLM tùy chọn trước tài liệu nhạy cảm.

### OmniDocBench

| Thuộc tính | Giá trị |
|---|---|
| Repo | [opendatalab/OmniDocBench](https://github.com/opendatalab/OmniDocBench) |
| Snapshot | 2,140★, chưa archive (GitHub API, 2026-11-02); HEAD `ea2d138c7d2e` ngày 2026-10-29 |
| License | Apache-2.0 (eval code); dataset kiểm riêng; [file thật](https://github.com/opendatalab/OmniDocBench/blob/ea2d138c7d2e185feb71ef8014e97d7206820b34/LICENSE) |
| Bằng chứng | [Triển khai/đặc tả](https://github.com/opendatalab/OmniDocBench/blob/ea2d138c7d2e185feb71ef8014e97d7206820b34/configs/end2end.yaml); [CI tại cùng commit](https://github.com/opendatalab/OmniDocBench/tree/ea2d138c7d2e185feb71ef8014e97d7206820b34/.github/workflows); đọc mã/đặc tả, chưa chạy |

Config end-to-end chấm text/reading order bằng edit distance, table bằng TEDS, formula bằng CDM/edit distance. Match có timeout/fallback; phải giữ config và lỗi evaluator cùng kết quả.

**Tích hợp và giới hạn:** Ghim version corpus lẫn code; v1.5 và v1.6 không mặc nhiên so cùng bảng. README/giấy phép eval không xác nhận quyền mọi trang dữ liệu, và corpus công khai chưa đại diện biểu mẫu tiếng Việt.

## 3. Cổng kiểm cho pipeline tài liệu

1. **Đầu vào bất biến:** hash file, số trang, nguồn/quyền sử dụng, loại native/scan, ngôn ngữ; giữ bản gốc. PDF không tin cậy xử lý trong sandbox, có trần trang/pixel/thời gian; không tự chạy nội dung nhúng.
2. **Chuẩn hóa có kiểm:** xoay/deskew/dewarp kèm ảnh trước/sau; chuẩn hóa NFC để chấm tiếng Việt nhưng giữ nguyên bản gốc phục vụ truy vết.
3. **Kết quả trung gian:** mỗi block có `document_hash`, `page`, `bbox` nếu parser cung cấp, `parser_ref`, `model_revision`, trạng thái OCR/fallback. Nếu parser chỉ ra Markdown, ghi rõ chưa có bbox; không bịa tọa độ.
4. **Trích schema:** kiểu dữ liệu, đơn vị, định dạng tiền/ngày và quy tắc cross-field; trường thiếu/không đọc được trả null + lý do. Citation phải trỏ đúng trang/vùng chứa giá trị; không chỉ kiểm JSON hợp lệ.
5. **Chấm tập đích:** CER/text edit distance, table TEDS hoặc độ đúng ô, reading order, precision/recall từng trường, tỷ lệ bỏ trang, p95 latency và chi phí/trang đạt yêu cầu. Ngưỡng lấy từ tác vụ; không dùng một điểm tổng để che lỗi trường quan trọng.
6. **Review có trọng tâm:** số tiền, mã số thuế, điều khoản và kích thước bản vẽ cần đối chiếu với ảnh gốc; độ tự tin model tự khai chưa đủ để bỏ bước này. Liên kết [07](../07-eval-observability/README.md), [12](../12-ai-security-guardrails/README.md), [18](../18-vietnam-community/README.md), [24](../24-ai-data-engineering/README.md).

## 4. Bài học kiến trúc

Một pipeline tốt giữ riêng **trang xử lý thành công, fallback, bị bỏ và chưa kiểm**. Cache phải khóa theo hash tài liệu + parser/model/config; thay model hoặc trang gốc phải làm mất hiệu lực bằng chứng cũ. Chunk cho RAG ở bước sau không được làm mất trang/bbox và provenance.

Paper gốc [OmniDocBench (CVPR 2025)](https://openaccess.thecvf.com/content/CVPR2025/html/Ouyang_OmniDocBench_Benchmarking_Diverse_PDF_Document_Parsing_with_Comprehensive_Annotations_CVPR_2025_paper.html) hỗ trợ đánh giá nhiều thành phần tài liệu; benchmark miền đích vẫn cần corpus riêng, nhất là biểu mẫu tiếng Việt và ảnh chụp điện thoại.

<a id="factory-2026-11-04"></a>

## 5. Nâng trần 4/11/2026: tài liệu vào xưởng phải có nguồn gốc và trạng thái từng trang

**Trần hiện tại:** §2–§4 đã tách OCR, layout, bảng và citation. Khoảng thiếu là hợp đồng đưa tài liệu khách hàng vào phần mềm: giới hạn tài nguyên, trạng thái partial, định danh phiên bản, quyền truy xuất và xóa dữ liệu dẫn xuất. Bản đọc bổ sung không tự chứng minh accuracy trên PDF tiếng Việt hoặc dữ liệu thực tế của xưởng.

| Tuyến | Nên chọn | Đầu ra cần giữ | Cổng và giới hạn |
|---|---|---|---|
| PDF đã có text đáng tin | Native extraction, Docling; so OCRmyPDF ở §2 khi cần searchable PDF | Text có trang/bbox, version parser và hash file | Reading order, ký tự/font và bảng; không OCR lại mọi trang vì có thể làm sai text đúng |
| Scan/ảnh nhiều nhiễu | Tesseract/PaddleOCR ở §2 | Text, vùng, confidence và lỗi từng trang | CER/WER trên corpus đúng ngôn ngữ; confidence không được dùng như xác suất trường nghiệp vụ đúng |
| Tài liệu nhiều bố cục/bảng | Docling/PaddleOCR/MinerU ở §2 | Cấu trúc bảng/ô/span, trang/bbox, provenance | Đo cấu trúc lẫn giá trị ô; Markdown nhìn đẹp chưa đủ |
| Trích trường hợp đồng/hóa đơn | Parser + schema + luật nghiệp vụ + hàng chờ review | Trường, raw value, normalized value, nguồn và trạng thái | Decimal/unit/date, tổng tiền, thiếu/không đọc được/không áp dụng phải phân biệt |

<a id="docling-factory"></a>

### Docling đọc sâu: hai cờ false chưa chứng minh chạy hoàn toàn offline

Hồ sơ gốc ở [mục 10](../10-local-llm-rag-memory/README.md); giữ nguyên thực thể catalog `docling`, không tạo bản sao cho mục 26.

| Thuộc tính | Giá trị |
|---|---|
| Repo / SHA / license | [docling-project/docling](https://github.com/docling-project/docling), `0634e2f74561e5950d69b2cace67ef95400506ad`, MIT cho thư viện; quyền weights/artifact phải kiểm riêng |
| Kiểm chứng 2026-11-04 | `code-read`: converter, pipeline options, base/standard PDF pipeline, LICENSE và CI; chưa convert tài liệu hoặc bắt lưu lượng |
| Default đã đọc | `enable_remote_services=False`, `allow_external_plugins=False`, nhưng `artifacts_path=None` được mô tả sẽ lấy model từ nguồn từ xa khi cần. Pipeline truyền các cờ tới factory/model; không suy ra mọi plugin hoặc cấu hình tùy chọn đều giữ nguyên mặc định. |
| Partial | `convert_all()` cho `PARTIAL_SUCCESS` đi tiếp ngay cả khi `raises_on_error=True`; việc không ném exception không có nghĩa tài liệu đã xử lý đủ. `document_timeout` có thể cho kết quả partial. |
| Giới hạn đầu vào | `max_num_pages` / `max_file_size` mặc định ở converter là `sys.maxsize`; xưởng cần đặt giới hạn tường minh, không dùng mặc định như một quota nghiệp vụ. |
| CI / chưa phủ | `ci.yml` gọi các lane trong `checks.yml`; có điều kiện lọc thay đổi và danh sách example không hỗ trợ/không chạy ở CI. Không nhận định mọi định dạng, model và backend đã được CI bao phủ. |

**Tuyến tích hợp và cổng nhận tài liệu:**

1. Nhận file bằng content hash + source revision + tenant/ACL; loại file được chấp nhận, page/size/time quota và sandbox parser là hợp đồng riêng. Tên file hoặc prompt trong PDF không được coi là chỉ dẫn điều khiển agent.
2. Chọn native/OCR theo từng trang; ghi parser/model/version, model artifact đã chuẩn bị, ngôn ngữ và trạng thái OCR. Nếu yêu cầu offline, cấp model artifacts cục bộ và kiểm lưu lượng thực tế trong môi trường tích hợp; hai cờ mặc định không thay phép kiểm này.
3. Lưu trạng thái `success/partial/failed` từng trang và toàn tài liệu; hàng chờ review tiếp nhận trang lỗi/timeout. Không đưa kết quả partial vào chỉ mục như bản đầy đủ, không biến thiếu trường thành chuỗi rỗng hợp lệ.
4. Đo corpus có gold annotation: text, reading order, table cells, field exact match/normalization và tỷ lệ citation chỉ đúng vùng. Chia theo scan/native, tiếng Việt, bảng dài, file mã hóa và trang xoay; báo cả file bị loại và lỗi.
5. Chunk/index chỉ từ phiên bản đã duyệt, giữ page/bbox/ACL xuyên retrieval tới câu trả lời; câu trả lời phải kiểm citation tồn tại và thuộc revision/tenant hiện hành. Nối [24](../24-ai-data-engineering/README.md), [10](../10-local-llm-rag-memory/README.md), [12](../12-ai-security-guardrails/README.md).
6. Diễn tập thay thế và xóa nguồn: raw file, extraction, chunks, embedding, cache và audit reference phải có retention/lineage. Phép kiểm là query không còn trả nội dung đã thu hồi, không chỉ xóa một hàng metadata.

**Đã đổi so với đợt trước:** chuẩn hóa phạm vi đọc Docling tại SHA mới và đưa `PARTIAL_SUCCESS` vào điều kiện nghiệm thu; chưa đánh giá lại accuracy hoặc quyền từng bộ weights. **Nguồn §5:** [README.md](https://github.com/docling-project/docling/blob/0634e2f74561e5950d69b2cace67ef95400506ad/README.md) · [LICENSE](https://github.com/docling-project/docling/blob/0634e2f74561e5950d69b2cace67ef95400506ad/LICENSE) · [docling/datamodel/pipeline_options.py](https://github.com/docling-project/docling/blob/0634e2f74561e5950d69b2cace67ef95400506ad/docling/datamodel/pipeline_options.py) · [docling/document_converter.py](https://github.com/docling-project/docling/blob/0634e2f74561e5950d69b2cace67ef95400506ad/docling/document_converter.py) · [docling/pipeline/base_pipeline.py](https://github.com/docling-project/docling/blob/0634e2f74561e5950d69b2cace67ef95400506ad/docling/pipeline/base_pipeline.py) · [docling/pipeline/standard_pdf_pipeline.py](https://github.com/docling-project/docling/blob/0634e2f74561e5950d69b2cace67ef95400506ad/docling/pipeline/standard_pdf_pipeline.py) · [.github/workflows/ci.yml](https://github.com/docling-project/docling/blob/0634e2f74561e5950d69b2cace67ef95400506ad/.github/workflows/ci.yml) · [.github/workflows/checks.yml](https://github.com/docling-project/docling/blob/0634e2f74561e5950d69b2cace67ef95400506ad/.github/workflows/checks.yml).

<a id="anhkysuai-2026-11-23"></a>

## Đánh giá từ kho Anh Kỹ Sư AI — 23/11/2026

Phần này có **3 hồ sơ hoặc phạm vi đối chiếu** từ [nguồn tuyển chọn](https://anhkysuai.com/kho/). [Bảng đủ 1.295 repo](../data/collections/anhkysuai-kho.json) ghi trạng thái đối chiếu từng link; [danh sách URL](../data/collections/anhkysuai-kho-links.txt) phục vụ tra cứu. Nguồn tuyển chọn giúp phát hiện repo; đánh giá bên dưới dựa trên clone và permalink upstream cùng metadata GitHub ngày 2026-11-23.

Mức `docs-read`/`code-read` chỉ áp dụng phạm vi ghi tại mỗi hồ sơ. Chưa cài, build, chạy test hay benchmark mã upstream. Giấy phép có thể tách theo code, model, nội dung, asset hoặc bản enterprise; con số/tuyên bố của tác giả chưa được tái lập nếu không có ghi chú khác.

<a id="anhkysuai-2026-11-23-surya"></a>

### Surya

**Repo:** [datalab-to/surya](https://github.com/datalab-to/surya) · **License:** Apache-2.0 cho mã; AI Pubs OpenRAIL-M sửa đổi cho model · **★ 21,612 (GitHub API, 2026-11-23)**

**Mục đích:** OCR và phân tích layout tài liệu bằng VLM, xuất text, bảng và thứ tự đọc.

**Giá trị và cơ chế:** Đọc client thấy ảnh được đổi PNG/base64 và gửi chat-completions, có batch, retry lỗi/lặp token; CLI chọn OCR toàn trang hoặc layout rồi từng block. Đây là client điều phối backend, không phải toàn bộ model.

**Giới hạn:** MODEL_LICENSE đặt ngưỡng trên 5 triệu USD doanh thu năm trước hoặc tổng vốn huy động, có ngoại lệ cá nhân/nghiên cứu ở hai điều ngưỡng; điều cấm cạnh tranh và attribution/share-alike cho cả output vẫn riêng. Điểm benchmark upstream chưa tái hiện.

**Cách tham khảo/tích hợp:** Kiểm license weights, chạy corpus scan thực có bảng/chữ nhỏ và giữ tọa độ nguồn để đối chiếu.

**Thay thế:** [PaddleOCR](../26-document-intelligence-ocr/README.md#paddleocr), [Docling](../26-document-intelligence-ocr/README.md#docling-factory), [Tesseract](../26-document-intelligence-ocr/README.md#tesseract).

**Bằng chứng:** `code-read`, ngày 2026-11-23, commit [`253888005c21`](https://github.com/datalab-to/surya/commit/253888005c21865f0ded5d50872727f2a3b307f1). Client chat-completions theo batch, retry và CLI OCR; không tải/chạy weights hay tái hiện benchmark. Chưa cài/chạy upstream.

**Nguồn:** [README.md](https://github.com/datalab-to/surya/blob/253888005c21865f0ded5d50872727f2a3b307f1/README.md) · [LICENSE](https://github.com/datalab-to/surya/blob/253888005c21865f0ded5d50872727f2a3b307f1/LICENSE) · [MODEL_LICENSE](https://github.com/datalab-to/surya/blob/253888005c21865f0ded5d50872727f2a3b307f1/MODEL_LICENSE) · [surya/inference/backends/openai_client.py](https://github.com/datalab-to/surya/blob/253888005c21865f0ded5d50872727f2a3b307f1/surya/inference/backends/openai_client.py) · [surya/scripts/ocr_text.py](https://github.com/datalab-to/surya/blob/253888005c21865f0ded5d50872727f2a3b307f1/surya/scripts/ocr_text.py) · [metadata GitHub](https://api.github.com/repos/datalab-to/surya).

<a id="anhkysuai-2026-11-23-umi-ocr"></a>

### Umi-OCR

**Repo:** [hiroi-sora/Umi-OCR](https://github.com/hiroi-sora/Umi-OCR) · **License:** MIT cho app; engine/plugin theo thành phần · **★ 48,885 (GitHub API, 2026-11-23)**

**Mục đích:** Ứng dụng OCR desktop cho screenshot, ảnh hàng loạt, PDF và mã QR.

**Giá trị và cơ chế:** Đã đọc route /api/ocr nhận base64, kiểm options rồi gửi MissionOCR; manager chọn engine, chạy theo path/bytes/base64 và áp ignore-area/parser trước trả text hoặc tọa độ.

**Giới hạn:** Chưa chạy OCR hay kiểm toàn server; tree không có workflow CI nên giữ mức docs-read dù đã xem luồng xử lý. Khả năng offline/ngôn ngữ phụ thuộc plugin và weights được chọn.

**Cách tham khảo/tích hợp:** Thử tài liệu tiếng Việt nhiều cột, kiểm thứ tự đọc và lưu bounding box để đối chiếu trước xuất searchable PDF.

**Thay thế:** [Tesseract.js](../26-document-intelligence-ocr/README.md#anhkysuai-2026-11-23-tesseract-js), surya, [PaddleOCR](../26-document-intelligence-ocr/README.md#paddleocr).

**Bằng chứng:** `docs-read`, ngày 2026-11-23, commit [`83173efc4f44`](https://github.com/hiroi-sora/Umi-OCR/commit/83173efc4f4453b41223ea96d63d44534bf0505c). Đọc endpoint OCR, kiểm đầu vào và dispatch mission sang engine cùng hậu xử lý; không thấy GitHub Actions workflow trong tree nên giữ docs-read. Chưa cài/chạy upstream.

**Nguồn:** [README.md](https://github.com/hiroi-sora/Umi-OCR/blob/83173efc4f4453b41223ea96d63d44534bf0505c/README.md) · [LICENSE](https://github.com/hiroi-sora/Umi-OCR/blob/83173efc4f4453b41223ea96d63d44534bf0505c/LICENSE) · [UmiOCR-data/py_src/server/ocr_server.py](https://github.com/hiroi-sora/Umi-OCR/blob/83173efc4f4453b41223ea96d63d44534bf0505c/UmiOCR-data/py_src/server/ocr_server.py) · [UmiOCR-data/py_src/mission/mission_ocr.py](https://github.com/hiroi-sora/Umi-OCR/blob/83173efc4f4453b41223ea96d63d44534bf0505c/UmiOCR-data/py_src/mission/mission_ocr.py) · [metadata GitHub](https://api.github.com/repos/hiroi-sora/Umi-OCR).

<a id="anhkysuai-2026-11-23-tesseract-js"></a>

### Tesseract.js

**Repo:** [naptha/tesseract.js](https://github.com/naptha/tesseract.js) · **License:** Apache-2.0 · **★ 38,851 (GitHub API, 2026-11-23)**

**Mục đích:** Bọc Tesseract WebAssembly để OCR ảnh trong browser và Node.js.

**Giá trị và cơ chế:** Đã đọc worker gán jobId/action, gửi message và resolve/reject theo phản hồi; scheduler phân việc cho worker rảnh và tiếp hàng đợi khi kết thúc. Khởi tạo nạp core, ngôn ngữ rồi initialize.

**Giới hạn:** README nói rõ không hỗ trợ PDF trực tiếp và không cải thiện model nhận dạng Tesseract. Chưa chạy OCR/CI hoặc đo RAM; số worker và dữ liệu ngôn ngữ ảnh hưởng bộ nhớ.

**Cách tham khảo/tích hợp:** Tái sử dụng worker, rasterize PDF riêng và kiểm ảnh tiếng Việt/độ nghiêng trước tăng concurrency.

**Thay thế:** scribe-js, [Umi-OCR](../26-document-intelligence-ocr/README.md#anhkysuai-2026-11-23-umi-ocr), surya.

**Bằng chứng:** `code-read`, ngày 2026-11-23, commit [`a1ca80d9e31c`](https://github.com/naptha/tesseract.js/commit/a1ca80d9e31c34512d0ded75ff8821ddcf3f2f91). Đọc worker message/job lifecycle, scheduler queue và CI lint/test theo ma trận Node; chưa kiểm lõi Tesseract/WASM hoặc chạy OCR. Chưa cài/chạy upstream.

**Nguồn:** [README.md](https://github.com/naptha/tesseract.js/blob/a1ca80d9e31c34512d0ded75ff8821ddcf3f2f91/README.md) · [LICENSE.md](https://github.com/naptha/tesseract.js/blob/a1ca80d9e31c34512d0ded75ff8821ddcf3f2f91/LICENSE.md) · [src/createWorker.js](https://github.com/naptha/tesseract.js/blob/a1ca80d9e31c34512d0ded75ff8821ddcf3f2f91/src/createWorker.js) · [src/createScheduler.js](https://github.com/naptha/tesseract.js/blob/a1ca80d9e31c34512d0ded75ff8821ddcf3f2f91/src/createScheduler.js) · [metadata GitHub](https://api.github.com/repos/naptha/tesseract.js).

## Nguồn

Các permalink trong từng hồ sơ cố định đúng phiên bản đã đọc; số sao/trạng thái archive là snapshot GitHub API ngày 2026-11-02. Không chạy mã, huấn luyện model hoặc tái lập kết quả của upstream.

<a id="nt-2026-11-23"></a>

## Nâng trần theo khoảng trống — 23/11/2026

Phần này có các hồ sơ mới của đợt nâng trần: mười trinh sát tìm trên internet và GitHub những mảng mà chuyên mục còn thiếu hoặc chỉ có hồ sơ cũ, rồi mỗi repo được clone nông tại một commit cố định, đọc LICENSE, README, ít nhất một file triển khai thật và CI nếu có; không cài hay chạy mã upstream. Mô tả của trinh sát nhiều chỗ sai so với mã thật, và các chỗ đó được sửa ngay trong từng hồ sơ. Số sao lấy sau bằng GitHub search API nên có thể để trống.

<a id="nt-paperless-ai"></a>

### Paperless-AI

| Thuộc tính | Giá trị |
|---|---|
| Repo | https://github.com/clusterzx/paperless-ai |
| License | MIT |
| Phiên bản đã đọc | `595496d65513d3ef9a0aff49df7f16a73aa01fc4` (commit 2026-11-23) |
| Kiểm chứng | 2026-11-23; code-read; đã đọc LICENSE, README.md, PRIVACY_POLICY.md, package.json, src/server/processing/analyzer.ts, src/server/env.ts, src/server/mcp/tools.ts, docs/guide/prompt-rules.md, docs/guide/mcp.md, .github/workflows/ci.yml; chưa chạy upstream |
| Khoảng trống lấp | Quản lý tài liệu/hồ sơ tuân thủ (DMS, OCR): lớp AI gắn thẻ và hỏi đáp trên kho tài liệu |
| Cơ chế đáng học | • `src/server/processing/analyzer.ts`: gọi LLM với JSON schema, nếu đầu ra bị cắt (truncated) thì không áp dụng mà thử lại một lần với ngân sách token lớn hơn; JSON hỏng thì hỏi lại một lần rồi mới lỗi.<br>• Prompt chỉ đưa vào danh sách tag/correspondent/loại tài liệu sẵn có và loại tag đánh dấu nội bộ (`buildPromptContext`), nên AI bị giới hạn trong từ vựng của kho.<br>• Prompt rules theo điều kiện (tag, loại, người gửi, storage path, custom field) chọn prompt và model riêng cho từng loại hồ sơ (`docs/guide/prompt-rules.md`).<br>• MCP server với API key theo scope (read, write, delete, metadata, upload, chat), giới hạn theo thư viện và rate limit (`src/server/mcp/tools.ts`, `docs/guide/mcp.md`). |
| Tiêu chí và cách kiểm | CI (`ci.yml`) chạy typecheck, eslint, vitest, build, thử build trên CPU x86-64-v2 giả lập và hai bộ Playwright e2e; thư mục `test/` có 15 nhóm test. Kiểm bằng máy cho mã, không có đánh giá độ chính xác phân loại của AI (chưa thấy trong phần đã đọc). |
| Giới hạn và rủi ro | MIT. Nội dung tài liệu được gửi tới nhà cung cấp LLM đã cấu hình (OpenAI, Anthropic, Azure, tương thích OpenAI) trừ khi dùng Ollama/cục bộ; chính sách riêng tư trong repo chỉ nói về tiện ích Chrome. Telemetry ONNX Runtime bị tắt mặc định (`ORT_DISABLE_TELEMETRY` mặc định 1 trong `env.ts`). README cảnh báo phải hoàn tất setup trước khi mở ra mạng ngoài. Mô tả trinh sát hơi hẹp: v4.5.1 còn có kho lưu trữ tích hợp không cần Paperless-ngx, OCR PaddleOCR và MCP. Số sao 6159 (chưa xác minh). |
| So với | paperless-ngx (DMS nền mà nó mở rộng); OCRmyPDF (OCR lớp dưới, không có AI phân loại); Open Notebook (hỏi đáp RAG trên tri thức). |
| Nguồn | [LICENSE](https://github.com/clusterzx/paperless-ai/blob/595496d65513d3ef9a0aff49df7f16a73aa01fc4/LICENSE) · [README.md](https://github.com/clusterzx/paperless-ai/blob/595496d65513d3ef9a0aff49df7f16a73aa01fc4/README.md) · [PRIVACY_POLICY.md](https://github.com/clusterzx/paperless-ai/blob/595496d65513d3ef9a0aff49df7f16a73aa01fc4/PRIVACY_POLICY.md) · [package.json](https://github.com/clusterzx/paperless-ai/blob/595496d65513d3ef9a0aff49df7f16a73aa01fc4/package.json) · [analyzer.ts](https://github.com/clusterzx/paperless-ai/blob/595496d65513d3ef9a0aff49df7f16a73aa01fc4/src/server/processing/analyzer.ts) · [env.ts](https://github.com/clusterzx/paperless-ai/blob/595496d65513d3ef9a0aff49df7f16a73aa01fc4/src/server/env.ts) · [tools.ts](https://github.com/clusterzx/paperless-ai/blob/595496d65513d3ef9a0aff49df7f16a73aa01fc4/src/server/mcp/tools.ts) · [prompt-rules.md](https://github.com/clusterzx/paperless-ai/blob/595496d65513d3ef9a0aff49df7f16a73aa01fc4/docs/guide/prompt-rules.md) · [mcp.md](https://github.com/clusterzx/paperless-ai/blob/595496d65513d3ef9a0aff49df7f16a73aa01fc4/docs/guide/mcp.md) · [ci.yml](https://github.com/clusterzx/paperless-ai/blob/595496d65513d3ef9a0aff49df7f16a73aa01fc4/.github/workflows/ci.yml) |

<a id="nt-papermerge"></a>

### Papermerge (kho cũ)

| Thuộc tính | Giá trị |
|---|---|
| Repo | https://github.com/ciur/papermerge |
| License | Apache-2.0 |
| Phiên bản đã đọc | `adac0a76f11489864be8b0a5ce0f785748824bec` (commit 2026-09-05) |
| Kiểm chứng | 2026-11-23; code-read; đã đọc LICENSE, README.md, pyproject.toml, changelog.md, config/settings/base.py, papermerge/test/test_automate.py, docker/docker-compose.yml, .github/workflows/docker.yml, run_tests.sh; chưa chạy upstream |
| Khoảng trống lấp | Quản lý tài liệu/hồ sơ tuân thủ (DMS, OCR): lưu trữ số hóa tài liệu quét |
| Cơ chế đáng học | • Quy tắc tự động gán (model `Automate`) với bốn thuật toán khớp ALL, ANY, LITERAL, REGEX trên văn bản OCR; `papermerge/test/test_automate.py` kiểm khớp và áp dụng lên hàng đợi inbox.<br>• Thư mục nhập (importer dir) và vòng lặp quét với ngưỡng 'file không đổi tối thiểu' trong `config/settings/base.py`; cấu hình bằng Configula (`papermerge.conf.py`, biến PAPERMERGE_*).<br>• Phần lõi KHÔNG nằm trong repo này: `pyproject.toml` kéo `papermerge-core` từ git, nên phần đọc được chỉ là vỏ Django, cấu hình, docker và test. |
| Tiêu chí và cách kiểm | Test Django chạy bằng `run_tests.sh` (settings test); workflow duy nhất `docker.yml` chỉ build và đẩy image khi phát hành, không chạy test. Phụ thuộc Django 3.2 và Python ^3.8. |
| Giới hạn và rủi ro | Apache-2.0. README ghi rõ kho đã ARCHIVED, phát triển chuyển sang papermerge/papermerge-core, tác giả tập trung vào bản SaaS và tìm người bảo trì bản mã mở (tuyên bố trong README, cờ archive trên GitHub chưa kiểm). Mô tả trinh sát sai: đây không phải DMS đang hoạt động. `config/settings/base.py` có SECRET_KEY cố định và DEBUG=True, `docker-compose.yml` dùng mật khẩu Postgres mẫu: chỉ dùng làm tham khảo, không triển khai nguyên trạng. Changelog dừng ở 3.0.1 (2024-01). Số sao 2930 (chưa xác minh). |
| So với | paperless-ngx (đang bảo trì, nên chọn thay thế); Paperless-AI; OCRmyPDF (chỉ OCR). |
| Nguồn | [LICENSE](https://github.com/ciur/papermerge/blob/adac0a76f11489864be8b0a5ce0f785748824bec/LICENSE) · [README.md](https://github.com/ciur/papermerge/blob/adac0a76f11489864be8b0a5ce0f785748824bec/README.md) · [pyproject.toml](https://github.com/ciur/papermerge/blob/adac0a76f11489864be8b0a5ce0f785748824bec/pyproject.toml) · [changelog.md](https://github.com/ciur/papermerge/blob/adac0a76f11489864be8b0a5ce0f785748824bec/changelog.md) · [base.py](https://github.com/ciur/papermerge/blob/adac0a76f11489864be8b0a5ce0f785748824bec/config/settings/base.py) · [test_automate.py](https://github.com/ciur/papermerge/blob/adac0a76f11489864be8b0a5ce0f785748824bec/papermerge/test/test_automate.py) · [docker-compose.yml](https://github.com/ciur/papermerge/blob/adac0a76f11489864be8b0a5ce0f785748824bec/docker/docker-compose.yml) · [docker.yml](https://github.com/ciur/papermerge/blob/adac0a76f11489864be8b0a5ce0f785748824bec/.github/workflows/docker.yml) · [run_tests.sh](https://github.com/ciur/papermerge/blob/adac0a76f11489864be8b0a5ce0f785748824bec/run_tests.sh) |

<a id="nt-chandra-ocr"></a>

### Chandra OCR 2

| Thuộc tính | Giá trị |
|---|---|
| Repo | https://github.com/datalab-to/chandra |
| License | Mã Apache-2.0 (`LICENSE`); trọng số AI Pubs OpenRAIL-M sửa đổi (`MODEL_LICENSE`) với ngưỡng 2 triệu USD doanh thu hoặc vốn huy động và điều khoản cấm cạnh tranh |
| Phiên bản đã đọc | `9c3a195573bec72b6e73cd66be099350ac11a4f5` (commit 2026-11-16) |
| Kiểm chứng | 2026-11-23; code-read; đã đọc README.md, LICENSE, MODEL_LICENSE, pyproject.toml; chưa chạy upstream |
| Khoảng trống lấp | Model card, dataset card và license theo trọng số |
| Cơ chế đáng học | - `LICENSE` (Apache-2.0) áp cho mã; `MODEL_LICENSE` (AI Pubs OpenRAIL-M sửa đổi) áp cho trọng số `datalab-to/chandra-ocr-2`; `pyproject.toml` ghi `Apache-2.0` nên metadata gói không phản ánh license trọng số.<br>- `chandra/model/vllm.py` và `chandra/settings.py`: gọi máy chủ vLLM qua client OpenAI (`VLLM_API_BASE` mặc định `http://localhost:8000/v1`), `temperature=0.0`, `top_p=0.1`, thử lại tối đa `MAX_VLLM_RETRIES=6`; ảnh được thu về tối thiểu `MIN_IMAGE_DIM=1536`.<br>- `chandra/model/util.py` `detect_repeat_token`: phát hiện đầu ra lặp (cửa sổ 500 ký tự, ngưỡng lặp co giãn nghịch theo độ dài chuỗi) để kích hoạt thử lại, cách chặn vòng lặp sinh của VLM đáng mượn.<br>- `chandra/skills/SKILL.md`: skill hướng dẫn agent gọi CLI `chandra ... --stdout`. |
| Tiêu chí và cách kiểm | Có `tests/unit/test_chandra.py` (mock, không cần GPU) và workflow `integration.yml` chạy `pytest tests/unit tests/integration` trên runner GPU T4 mỗi lần push, dùng `HF_TOKEN` (đã mở workflow này; `publish.yml` chưa mở). Độ chính xác chỉ có bảng tự công bố trong README (olmocr, đa ngôn ngữ 43 ngôn ngữ): dòng `vi` là Chandra 2 80.4%, Chandra 1 81.6%, Gemini 2.5 Flash 89.5%, GPT-5 Mini 83.6% (chưa xác minh, số của hãng). |
| Giới hạn và rủi ro | Ràng buộc trọng số (MODEL_LICENSE, Attachment A): cấm dùng cho mọi mục đích nếu đơn vị có doanh thu năm trước trên 2 triệu USD hoặc đã huy động trên 2 triệu USD, trừ dùng cá nhân/nghiên cứu; cấm nếu cung cấp sản phẩm cạnh tranh với hãng; điều 4(a) buộc đưa các hạn chế này vào thỏa thuận hạ nguồn, điều 8 share-a-like, điều 9 cho hãng quyền hạn chế hoặc cập nhật từ xa. README nói rõ tự host thương mại cần giấy phép. Do đó không phải mã nguồn mở theo nghĩa OSI đối với trọng số: `open_source: true` chỉ đúng cho phần mã. README còn quảng bá nền tảng trả phí của hãng. Tiếng Việt kém Gemini theo chính bảng của hãng. |
| So với | `marker` và `surya` (cùng tác giả Datalab, đã có hồ sơ), `olmocr`, `paddleocr`, `mineru`; so điều kiện license trọng số với `dots-ocr` ở cùng lô. |
| Nguồn | [README.md](https://github.com/datalab-to/chandra/blob/9c3a195573bec72b6e73cd66be099350ac11a4f5/README.md) · [LICENSE](https://github.com/datalab-to/chandra/blob/9c3a195573bec72b6e73cd66be099350ac11a4f5/LICENSE) · [MODEL_LICENSE](https://github.com/datalab-to/chandra/blob/9c3a195573bec72b6e73cd66be099350ac11a4f5/MODEL_LICENSE) · [pyproject.toml](https://github.com/datalab-to/chandra/blob/9c3a195573bec72b6e73cd66be099350ac11a4f5/pyproject.toml) · [settings.py](https://github.com/datalab-to/chandra/blob/9c3a195573bec72b6e73cd66be099350ac11a4f5/chandra/settings.py) · [vllm.py](https://github.com/datalab-to/chandra/blob/9c3a195573bec72b6e73cd66be099350ac11a4f5/chandra/model/vllm.py) · [util.py](https://github.com/datalab-to/chandra/blob/9c3a195573bec72b6e73cd66be099350ac11a4f5/chandra/model/util.py) · [SKILL.md](https://github.com/datalab-to/chandra/blob/9c3a195573bec72b6e73cd66be099350ac11a4f5/chandra/skills/SKILL.md) · [test_chandra.py](https://github.com/datalab-to/chandra/blob/9c3a195573bec72b6e73cd66be099350ac11a4f5/tests/unit/test_chandra.py) · [integration.yml](https://github.com/datalab-to/chandra/blob/9c3a195573bec72b6e73cd66be099350ac11a4f5/.github/workflows/integration.yml) |

<a id="nt-pdf-extract-kit"></a>

### PDF-Extract-Kit

| Thuộc tính | Giá trị |
|---|---|
| Repo | https://github.com/opendatalab/PDF-Extract-Kit |
| License | AGPL-3.0 |
| Phiên bản đã đọc | `fdb25fd4bd9058ba4e13ac16cb68d4f06b23df56` (commit 2025-01-03) |
| Kiểm chứng | 2026-11-23; code-read; đã đọc README.md, LICENSE.md, requirements.txt, configs/ocr.yaml; chưa chạy upstream |
| Khoảng trống lấp | OCR/layout cho tiếng Việt và tài liệu kỹ thuật |
| Cơ chế đáng học | - `pdf_extract_kit/registry/registry.py`: hai registry `TASK_REGISTRY` và `MODEL_REGISTRY` đăng ký tác vụ và model bằng decorator; tác vụ lấy cấu hình từ `configs/*.yaml` nên đổi model chỉ cần sửa YAML.<br>- `configs/layout_detection.yaml` và `tasks/layout_detection/models/yolo.py`: DocLayout-YOLO với `img_size 1024`, `conf_thres 0.25`, `iou_thres 0.45`, trọng số tải riêng về `models/Layout/YOLO/`.<br>- `configs/ocr.yaml` và `tasks/ocr/models/paddle_ocr.py`: OCR PaddleOCR 2.7.3 với `lang: ch`, `det_db_box_thresh: 0.3`, mô hình PP-OCRv4 tiếng Trung; để đọc tiếng Việt phải đổi mô hình nhận dạng, repo không cấu hình sẵn (chưa xác minh khả năng).<br>- `project/pdf2markdown` là ví dụ ghép các tác vụ thành pipeline PDF sang Markdown (chỉ đọc cấu trúc thư mục). |
| Tiêu chí và cách kiểm | Không có workflow CI và không có thư mục test của dự án. Phần Evaluation Metrics trong README ghi Coming Soon, tức chưa có chuẩn đo đi kèm; chất lượng chỉ được minh họa bằng ảnh. Kiểm bằng cách chạy script demo bằng tay. |
| Giới hạn và rủi ro | AGPL-3.0 cho cả repo (README giải thích do dùng mã YOLO của Ultralytics và PyMuPDF đều AGPL), nghĩa là nhúng vào dịch vụ mạng sẽ kéo theo nghĩa vụ công bố mã nguồn; license trọng số tải riêng trên Hugging Face/ModelScope chưa đọc (chưa xác minh). Commit cuối 2025-01-03 (khoảng 22 tháng so với ngày kiểm). Ràng buộc phụ thuộc cũ (`paddleocr==2.7.3`, `doclayout-yolo==0.0.2`, `paddlepaddle-gpu`). Mặc định là tiếng Trung và Anh; không có hỗ trợ tiếng Việt được nêu trong repo. |
| So với | `mineru` (sản phẩm hoàn chỉnh dựa trên bộ này, đã có hồ sơ), `docling`, `marker`, `surya`, `paddleocr`. |
| Nguồn | [README.md](https://github.com/opendatalab/PDF-Extract-Kit/blob/fdb25fd4bd9058ba4e13ac16cb68d4f06b23df56/README.md) · [LICENSE.md](https://github.com/opendatalab/PDF-Extract-Kit/blob/fdb25fd4bd9058ba4e13ac16cb68d4f06b23df56/LICENSE.md) · [requirements.txt](https://github.com/opendatalab/PDF-Extract-Kit/blob/fdb25fd4bd9058ba4e13ac16cb68d4f06b23df56/requirements.txt) · [ocr.yaml](https://github.com/opendatalab/PDF-Extract-Kit/blob/fdb25fd4bd9058ba4e13ac16cb68d4f06b23df56/configs/ocr.yaml) · [layout_detection.yaml](https://github.com/opendatalab/PDF-Extract-Kit/blob/fdb25fd4bd9058ba4e13ac16cb68d4f06b23df56/configs/layout_detection.yaml) · [registry.py](https://github.com/opendatalab/PDF-Extract-Kit/blob/fdb25fd4bd9058ba4e13ac16cb68d4f06b23df56/pdf_extract_kit/registry/registry.py) · [paddle_ocr.py](https://github.com/opendatalab/PDF-Extract-Kit/blob/fdb25fd4bd9058ba4e13ac16cb68d4f06b23df56/pdf_extract_kit/tasks/ocr/models/paddle_ocr.py) · [yolo.py](https://github.com/opendatalab/PDF-Extract-Kit/blob/fdb25fd4bd9058ba4e13ac16cb68d4f06b23df56/pdf_extract_kit/tasks/layout_detection/models/yolo.py) |

<a id="nt-dots-ocr"></a>

### dots.ocr (dots.mocr)

| Thuộc tính | Giá trị |
|---|---|
| Repo | https://github.com/rednote-hilab/dots.ocr |
| License | MIT (`LICENSE`) kèm `dots.ocr LICENSE AGREEMENT` riêng cho Model Materials (điều khoản sử dụng chấp nhận được, luật Trung Quốc, MIT thắng khi xung đột) |
| Phiên bản đã đọc | `36d7248878f181c6257dc1cbd799ae940970444f` (commit 2026-03-24) |
| Kiểm chứng | 2026-11-23; code-read; đã đọc README.md, LICENSE, dots.ocr LICENSE AGREEMENT, NOTICE; chưa chạy upstream |
| Khoảng trống lấp | OCR/layout cho tiếng Việt và tài liệu kỹ thuật |
| Cơ chế đáng học | - `dots_ocr/utils/prompts.py`: một mô hình, nhiều tác vụ chọn bằng chế độ prompt (`prompt_layout_all_en`, `prompt_layout_only_en`, `prompt_ocr`, `prompt_grounding_ocr`, `prompt_web_parsing`, `prompt_scene_spotting`, `prompt_image_to_svg`); prompt layout quy định 11 loại phần tử, bbox `[x1,y1,x2,y2]`, bảng HTML, công thức LaTeX, sắp theo thứ tự đọc.<br>- `dots_ocr/parser.py`: `_parse_single_image` kiểm `min_pixels`/`max_pixels`, gọi vLLM hoặc Hugging Face, hậu xử lý JSON; nếu JSON hỏng thì đặt cờ `filtered` và ghi phản hồi thô thay vì bỏ trang.<br>- `dots_ocr/utils/output_cleaner.py`: sửa đầu ra JSON hỏng bằng regex (thiếu dấu phân cách, bbox lỗi) và ghi báo cáo trước/sau làm sạch.<br>- Triển khai khuyến nghị bằng vLLM (README: tích hợp chính thức từ vLLM 0.11.0), `demo/` có script gọi API. |
| Tiêu chí và cách kiểm | Không có test hay CI trong repo (không có `tests/` và không có `.github/workflows`). Số liệu benchmark (olmOCR-Bench, OmniDocBench v1.5, XDocParse, Elo) là bảng tự công bố trong README (chưa xác minh). Hậu xử lý có cờ `filtered` để báo trang model xuất JSON lỗi, nhưng không có ngưỡng chất lượng tự động. |
| Giới hạn và rủi ro | License kép: `LICENSE` là MIT (2025, rednote-hilab) còn `dots.ocr LICENSE AGREEMENT` (hiệu lực 8/8/2025, Xingyin Information Technology Shanghai) định nghĩa Model Materials gồm cả trọng số, mã, dữ liệu; điều 1.6 nói MIT thắng khi mâu thuẫn, nhưng điều 3.3 cấm dùng để nhận dạng giấy tờ giả, trích thông tin cá nhân nhạy cảm không có căn cứ pháp lý, số hóa trái phép ấn phẩm hay cào hàng loạt (vi phạm làm chấm dứt mọi license), điều 5.2 hạn chế dữ liệu GDPR/HIPAA, luật áp dụng là Trung Quốc và trọng tài Hàng Châu. Hiệu lực pháp lý của hai văn bản chồng nhau chưa rõ. Văn bản thỏa thuận nhắc tên dots.mocr và repo dots.mocr, trong khi thư mục là dots.ocr: repo đã đổi thương hiệu 19/3/2026. Phụ thuộc `transformers==4.56.1`, `trust_remote_code=True` khi tải model Hugging Face trong `parser.py`. Tuyên bố hỗ trợ mọi chữ viết, chưa thấy README nêu riêng tiếng Việt (chưa xác minh). |
| So với | `chandra-ocr` (cùng lô, license trọng số chặt hơn), `paddleocr`, `olmocr`, `mineru`, `docling`. |
| Nguồn | [README.md](https://github.com/rednote-hilab/dots.ocr/blob/36d7248878f181c6257dc1cbd799ae940970444f/README.md) · [LICENSE](https://github.com/rednote-hilab/dots.ocr/blob/36d7248878f181c6257dc1cbd799ae940970444f/LICENSE) · [dots.ocr LICENSE AGREEMENT](https://github.com/rednote-hilab/dots.ocr/blob/36d7248878f181c6257dc1cbd799ae940970444f/dots.ocr%20LICENSE%20AGREEMENT) · [NOTICE](https://github.com/rednote-hilab/dots.ocr/blob/36d7248878f181c6257dc1cbd799ae940970444f/NOTICE) · [requirements.txt](https://github.com/rednote-hilab/dots.ocr/blob/36d7248878f181c6257dc1cbd799ae940970444f/requirements.txt) · [parser.py](https://github.com/rednote-hilab/dots.ocr/blob/36d7248878f181c6257dc1cbd799ae940970444f/dots_ocr/parser.py) · [prompts.py](https://github.com/rednote-hilab/dots.ocr/blob/36d7248878f181c6257dc1cbd799ae940970444f/dots_ocr/utils/prompts.py) · [output_cleaner.py](https://github.com/rednote-hilab/dots.ocr/blob/36d7248878f181c6257dc1cbd799ae940970444f/dots_ocr/utils/output_cleaner.py) |

<a id="nt-table-transformer"></a>

### Table Transformer (TATR)

| Thuộc tính | Giá trị |
|---|---|
| Repo | https://github.com/microsoft/table-transformer |
| License | Mã: MIT (LICENSE gốc), thư mục `detr/` có LICENSE Apache-2.0 riêng. Trọng số: README dẫn checkpoint trên Hugging Face (tài khoản bsmock); điều khoản của trọng số và của dữ liệu PubTables-1M **(chưa xác minh)**, chưa mở thẻ model/dataset |
| Phiên bản đã đọc | `16d124f616109746b7785f03085100f1f6247575` (commit 2023-09-06) |
| Kiểm chứng | 2026-11-23; code-read; đã đọc `README.md`, `LICENSE`, `detr/LICENSE`, `src/inference.py`, `src/postprocess.py`, `src/structure_config.json`, `src/grits.py`; chưa chạy upstream |
| Khoảng trống lấp | Trích xuất bảng và biểu mẫu: phát hiện bảng và nhận dạng cấu trúc hàng, cột, ô gộp |
| Cơ chế đáng học | - Hai mô hình DETR tách biệt (phát hiện bảng; nhận dạng cấu trúc với 6 lớp: bảng, cột, hàng, tiêu đề cột, tiêu đề hàng chiếu, ô gộp), cấu hình ở `src/structure_config.json` (resnet18, 125 query).<br>- `src/postprocess.py` lọc theo ngưỡng riêng từng lớp, NMS theo độ chứa, căn hàng/cột theo token chữ rồi dựng ô bằng giao hàng-cột (`objects_to_cells`).<br>- `src/inference.py` nối ảnh sang HTML/CSV nhưng chữ phải do OCR hoặc PDF cấp riêng; mô hình chỉ cho hình học.<br>- `src/grits.py` cài thước đo GriTS (so lưới bảng bằng quy hoạch động) để chấm cấu trúc, không chỉ IoU hộp. |
| Tiêu chí và cách kiểm | Ngưỡng điểm mặc định 0.5 cho mọi lớp trong `inference.py`; đo bằng GriTS và các script eval trong `src/eval.py` (chỉ liệt kê, chưa mở). `src/` không có bộ test riêng (`detr/test_all.py` chưa mở); thư mục workflow chỉ thấy tên file CodeQL, chưa mở. |
| Giới hạn và rủi ro | Đã ngừng cập nhật thực chất: commit cuối 2023-09-06 (tuyên bố của trinh sát là repo archived **(chưa xác minh)**, không gọi API). Trọng số chỉ có cho PubTables-1M (và v1.1 Pub/Fin/All), tên miền khác phải tự huấn luyện. `torch.load` không đặt `weights_only` trong `inference.py` nên chỉ nạp checkpoint tin cậy. Chưa chạy nên chưa biết độ chính xác trên biểu mẫu tiếng Việt. |
| So với | docling (hồ sơ có sẵn, bảng là một phần pipeline), mineru, surya, marker, olmocr: các công cụ này gói cả OCR và bố cục; TATR hẹp nhưng cho điểm tin cậy từng ô và có thước đo GriTS. |
| Nguồn | [README.md](https://github.com/microsoft/table-transformer/blob/16d124f616109746b7785f03085100f1f6247575/README.md) · [LICENSE](https://github.com/microsoft/table-transformer/blob/16d124f616109746b7785f03085100f1f6247575/LICENSE) · [LICENSE](https://github.com/microsoft/table-transformer/blob/16d124f616109746b7785f03085100f1f6247575/detr/LICENSE) · [inference.py](https://github.com/microsoft/table-transformer/blob/16d124f616109746b7785f03085100f1f6247575/src/inference.py) · [postprocess.py](https://github.com/microsoft/table-transformer/blob/16d124f616109746b7785f03085100f1f6247575/src/postprocess.py) · [structure_config.json](https://github.com/microsoft/table-transformer/blob/16d124f616109746b7785f03085100f1f6247575/src/structure_config.json) · [grits.py](https://github.com/microsoft/table-transformer/blob/16d124f616109746b7785f03085100f1f6247575/src/grits.py) |
