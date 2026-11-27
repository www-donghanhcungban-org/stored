# Hồ sơ: anthropics/claude-cookbooks

- Ngày lập: 2026-11-27
- URL: https://github.com/anthropics/claude-cookbooks
- Nguồn: trang repo, danh sách thư mục `main`, README. Chưa đọc: `CONTRIBUTING.md`, nội dung LICENSE, từng notebook, `registry.yaml`. **[chưa xác minh]** là chưa đọc được từ nguồn.

## Tổng quan

| Mục | Nội dung |
|---|---|
| Mô tả | "Bộ sưu tập notebook/công thức cho những cách thú vị và hiệu quả để dùng Claude" |
| README | Mã và hướng dẫn giúp lập trình viên xây ứng dụng với Claude, có đoạn code copy được |
| Giấy phép | MIT |
| Ngôn ngữ | README nói chủ yếu Python; tỷ lệ phần trăm **[chưa xác minh]** |
| Thống kê | 55,3k sao, 6,7k fork, 636 theo dõi, 94 issue mở, 304 PR, 652 commit. Ngày commit cuối **[chưa xác minh]** |
| Đóng góp | Chào đón (ý tưởng, sửa lỗi chính tả, hướng dẫn mới hoặc cải tiến); xem issue và PR hiện có trước. `CONTRIBUTING.md` chưa đọc |

## Cấu trúc thư mục cấp cao
Danh sách thư mục không có mô tả; mục đích chỉ suy ra từ tên, trừ khi README nêu.
- `capabilities/`: README liệt kê phân loại, RAG, tóm tắt.
- `tool_use/`: dùng công cụ (agent chăm sóc khách hàng, máy tính).
- `third_party/`: Pinecone RAG, Voyage AI embeddings.
- `multimodal/`: các notebook thị giác; cũng có notebook sub-agent.
- `misc/`: nhiều notebook (SQL, trang web, tạo ảnh, tải PDF, evals, JSON mode, kiểm duyệt, prompt caching).
- `cost_optimization/`, `latency_optimization/`: tối ưu chi phí và độ trễ cho agent (theo README).
- Có trong danh sách nhưng không nêu mục đích: `extended_thinking/`, `finetuning/`, `images/`, `coding/`, `observability/`, `managed_agents/`, `claude_agent_sdk/`, `skills/`, `tool_evaluation/`, `evals/agentic_search/`, `patterns/agents/`, `anthropic_cookbook/`, `scripts/`, `tests/`, `fable_5_fallback_billing/`, `.claude/`, `.github/`.
- File gốc: `README.md`, `CONTRIBUTING.md`, `LICENSE`, `CLAUDE.md`, `Makefile`, `tox.ini`, `pyproject.toml`, `uv.lock`, `uv.toml`, `requirements-dev.txt`, `registry.yaml`, `authors.yaml`, `lychee.toml`, `.env.example`, `.pre-commit-config.yaml`.

## Notebook nổi bật (bảng công thức trong README)
- `capabilities/`: phân loại, RAG, tóm tắt.
- `tool_use/customer_service_agent.ipynb`: agent chăm sóc khách hàng dùng công cụ.
- `tool_use/calculator_tool.ipynb`: tích hợp công cụ máy tính.
- `misc/how_to_make_sql_queries.ipynb`: tạo truy vấn SQL.
- `third_party/Pinecone/rag_using_pinecone.ipynb`: RAG với Pinecone.
- `misc/read_web_pages_with_haiku.ipynb`: đọc trang web bằng Haiku.
- `third_party/VoyageAI/how_to_create_embeddings.md`: embeddings Voyage AI (hướng dẫn markdown).
- `multimodal/`: `getting_started_with_vision`, `best_practices_for_vision`, `reading_charts_graphs_powerpoints`, `how_to_transcribe_text`.
- `misc/illustrated_responses.ipynb`: Claude kết hợp Stable Diffusion tạo ảnh.
- `multimodal/using_sub_agents.ipynb`: Haiku làm sub-agent cho Opus.
- `misc/pdf_upload_summarization.ipynb`: phân tích và tóm tắt PDF.
- `misc/building_evals.ipynb`: đánh giá prompt tự động.
- `misc/how_to_enable_json_mode.ipynb`: đầu ra JSON nhất quán.
- `misc/building_moderation_filter.ipynb`: bộ lọc kiểm duyệt nội dung.
- `misc/prompt_caching.ipynb`: prompt caching.
- `cost_optimization/cost_optimization.ipynb`: checklist chi phí agent (tỷ lệ đạt và chi phí mỗi tác vụ).
- `latency_optimization/latency_optimization.ipynb`: các đòn bẩy độ trễ.

## Cách chạy
- README **không** có lệnh clone, cài đặt, đặt khóa API hay chạy Jupyter. Điều kiện duy nhất README nêu: cần khóa Claude API ("đăng ký miễn phí").
- Repo có `pyproject.toml`, `uv.lock`, `uv.toml`, `requirements-dev.txt`, `Makefile`, `.env.example`, gợi ý dùng Python/uv, nhưng cách dùng **[chưa xác minh]** (chưa đọc `CONTRIBUTING.md` và README từng thư mục).
- README khuyên người mới học khóa "Claude API Fundamentals" ở `anthropics/courses` (`anthropic_api_fundamentals`).

## Yêu cầu, chi phí, độ cũ
- **Yêu cầu:** khóa Claude API, Python.
- **Chi phí:** README không nêu; dùng notebook gọi API nên tính phí theo mức dùng.
- **Độ cũ:** README chỉ dùng tên chung "Haiku", "Opus", không có số phiên bản hay ngày. Link issue trỏ tới `anthropics/anthropic-cookbook` và vài link notebook dùng tên repo cũ (có thể chuyển hướng, chưa kiểm). Các thư mục `fable_5_fallback_billing` và `claude_agent_sdk` gợi ý có nội dung mới nhưng chưa đọc.

## Đánh giá
- **Phù hợp:** lập trình viên đã dùng Claude API muốn đoạn code Python copy được cho phân loại, RAG, tool use, thị giác, evals, caching, tối ưu chi phí và độ trễ cho agent.
- **Chưa rõ:** có hướng tới người mới hay không (README chỉ người mới sang khóa học riêng).
- **Chưa xác minh:** lệnh chạy cụ thể, ngày commit cuối, ngôn ngữ, nội dung từng thư mục chưa mô tả, độ cũ của tên model trong notebook.
