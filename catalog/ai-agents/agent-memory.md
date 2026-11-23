<!-- File sinh tự động bởi scripts/build_catalog_views.py; sửa data/projects.json hoặc data/taxonomy.json rồi chạy lại. -->

# agent-memory — AI agent, skill & điều phối

[← Mục lục catalog](../README.md) · 19 hồ sơ.

| Dự án | Repo | License | ★ | Bằng chứng | Mục | Tóm tắt |
|---|---|---|---|---|---|---|
| [claude-mem](../../10-local-llm-rag-memory/README.md) | `thedotmack/claude-mem` | Apache-2.0 | 107.804 | chưa chuẩn hóa | 10 | 11 hook/9 sự kiện ghi phiên → worker Bun 127.0.0.1:37777 gọi model nén thành observation; |
| [Mem0](../../10-local-llm-rag-memory/README.md) | `mem0ai/mem0` | Apache-2.0 | 68.168 | chưa chuẩn hóa | 10 | 18/9/2026; |
| [MemPalace](../../10-local-llm-rag-memory/README.md) | `MemPalace/mempalace` | MIT | 60.193 | chưa chuẩn hóa | 10 | Bộ nhớ local lưu nguyên văn hội thoại, tìm ngữ nghĩa trên Chroma (có Milvus), MCP + hook cho coding agent; |
| [Hindsight](../../10-local-llm-rag-memory/README.md) | `vectorize-io/hindsight` | MIT | 56.978 | chưa chuẩn hóa | 10 | Agent memory retain/recall/reflect, 1.0 ngày 15/10/2026; |
| [OpenViking](../../10-local-llm-rag-memory/README.md) | `volcengine/OpenViking` | AGPL-3.0 (CLI, examples Apache-2.0) | 41.248 | chưa chuẩn hóa | 10 | Context DB cho agent (ByteDance/Volcengine): hệ file ảo viking:// gộp tài liệu, memory, skill với tóm tắt L0/L1/L2; |
| [cognee](../../10-local-llm-rag-memory/README.md) | `topoteretes/cognee` | Apache-2.0 | 32.963 | chưa chuẩn hóa | 10 | ; |
| [Graphiti (Zep)](../../10-local-llm-rag-memory/README.md) | `getzep/graphiti` | Apache-2.0 | 32.397 | chưa chuẩn hóa | 10 | temporal KG; |
| [Supermemory](../../10-local-llm-rag-memory/README.md#anhkysuai-2026-11-23-supermemory) | `supermemoryai/supermemory` | MIT cho mã công khai; server local/Enterprise có giấy phép riêng | 31.690 | đọc mã 2026-11-23 | 10 | Bộ tích hợp bộ nhớ dài hạn cho ứng dụng AI qua API, SDK và MCP. |
| [TencentDB-Agent-Memory](../../08-awesome-lists-learning/README.md#6c54-bộ-nhớ-ngữ-cảnh--tiết-kiệm-token) | `TencentCloud/TencentDB-Agent-Memory` | MIT | 30.979 | đọc tài liệu 2026-11-18 | 08 | Hệ thống bộ nhớ dùng chung cho AI agent (Memory Hub + Proxy) để lưu, tổ chức và tái sử dụng ngữ cảnh, tài liệu, quy trình giữa các agent như Claude Code, Codex, Hermes,… |
| [agentmemory](../../10-local-llm-rag-memory/README.md) | `rohitg00/agentmemory` | Apache-2.0 | 30.049 | chưa chuẩn hóa | 10 | Bộ nhớ dài hạn cho coding agent qua hook + 54 MCP tool, BM25 + vector cục bộ + graph; |
| [beads](../../08-awesome-lists-learning/README.md#6c-kho-repo-của-phan-đông-giang-phandonggiangcomkho-repo-694-repo-32-nhóm-và-24-repo-aiagent-đọc-mã-bảng-người-dùng-dán-kiểm-18112026) | `gastownhall/beads` | MIT | 28.812 | đọc tài liệu 2026-11-18 | 08 | bd là bộ theo dõi issue dạng đồ thị phân tán cho agent, chạy trên Dolt, thay kế hoạch markdown bằng đồ thị task có phụ thuộc làm bộ nhớ dài hạn. |
| [Letta](../../10-local-llm-rag-memory/README.md) | `letta-ai/letta` | Apache-2.0 | 25.309 | chưa chuẩn hóa | 10 | MemGPT; |
| [Memori](../../08-awesome-lists-learning/README.md#6c54-bộ-nhớ-ngữ-cảnh--tiết-kiệm-token) | `MemoriLabs/Memori` | Apache-2.0 | 17.593 | đọc tài liệu 2026-11-18 | 08 | Lớp bộ nhớ cho AI agent, gắn vào client LLM sẵn có để tự lưu và gợi nhớ hội thoại, lời gọi tool và quyết định; |
| [memvid](../../08-awesome-lists-learning/README.md#6c54-bộ-nhớ-ngữ-cảnh--tiết-kiệm-token) | `memvid/memvid` | Apache-2.0 | 17.429 | đọc tài liệu 2026-11-18 | 08 | Lớp bộ nhớ cho AI agent đóng gói dữ liệu, embedding, chỉ mục tìm kiếm và metadata vào một tệp duy nhất (.mv2), truy xuất trực tiếp không cần cơ sở dữ liệu hay server. |
| [ai-memory](../../10-local-llm-rag-memory/README.md#6h-hồ-sơ-akitaonrailsai-memory-bộ-nhớ-dài-hạn-dùng-chung-cho-20-coding-agent-wiki-markdown-trong-git-mặc-định-không-gọi-llm-ảnh-readme-người-dùng-gửi-đọc-mã-8112026) | `akitaonrails/ai-memory` | MIT | 15.353 | đọc mã 2026-11-08 | 10 | Bộ nhớ dài hạn dùng chung cho 20+ coding agent (Claude Code, Codex, Cursor, Gemini CLI…) của Fabio Akita: một binary Rust, wiki Markdown trong git làm nguồn sự thật, SQL… |
| [memU](../../08-awesome-lists-learning/README.md#6c54-bộ-nhớ-ngữ-cảnh--tiết-kiệm-token) | `NevaMind-AI/memU` | Apache-2.0 | 14.628 | đọc tài liệu 2026-11-18 | 08 | Hệ thống bộ nhớ cá nhân dạng wiki cho agent, dùng chung giữa phiên, agent và thiết bị, tự rút kỹ năng tái sử dụng từ lịch sử agent. |
| [engram](../../10-local-llm-rag-memory/README.md) | `Gentleman-Programming/engram` | MIT | 7.717 | chưa chuẩn hóa | 10 | Bộ nhớ dài hạn cho coding agent: một binary Go + SQLite FTS5, 26 tool MCP + HTTP (127.0.0.1) + CLI + TUI, agent tự ghi qua mem_save (không LLM nén); |
| [LoCoMo](../../10-local-llm-rag-memory/README.md) | `snap-research/locomo` | CC-BY-NC-4.0 (LICENSE.txt; GitHub báo NOASSERTION) | 1.259 | chưa chuẩn hóa | 10 | Benchmark hội thoại rất dài ACL 2024: 10 hội thoại, QA + event summary, chấm F1/EM/ROUGE; |
| [LongMemEval](../../10-local-llm-rag-memory/README.md) | `xiaowu0162/LongMemEval` | MIT | 1.191 | chưa chuẩn hóa | 10 | Benchmark bộ nhớ dài hạn ICLR 2025: 500 câu, 5 năng lực, bản S/M/oracle, bản cleaned 9/2025; |
