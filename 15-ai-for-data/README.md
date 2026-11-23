# 15 · AI for Data: Query Engines, Dataframes, Text-to-SQL, Notebooks, Data Agents

| Dự án | Repo | License | ★ | Vai trò | Ghi chú |
|---|---|---|---|---|---|
| **DuckDB** | duckdb/duckdb | MIT | **40k+** (5/8/2026) | OLAP in-process, SQL trên Parquet/CSV; 1.4 LTS, 1.5 | Nền cho nhiều tool AI-data |
| **Polars** | pola-rs/polars | MIT | – | Dataframe Rust, >24M tải/tháng | Thay pandas cho dữ liệu lớn |
| **PandasAI** | sinaptik-ai/pandas-ai | MIT (trừ `ee/`) | ~24k | Hỏi dữ liệu bằng ngôn ngữ tự nhiên (SQL, CSV, pandas, polars) | Cập nhật cuối 10/2025 |
| **Vanna** | vanna-ai/vanna | MIT | ~23.7k | Text-to-SQL với RAG trên schema | |
| **marimo** | marimo-team/marimo | Apache-2.0 | ~22–23k | Notebook Python reactive, lưu dạng .py thuần, AI-native | Thay Jupyter cho reproducibility |
| **Jupyter AI** | jupyterlab/jupyter-ai | BSD-3 | – | Nối agent (Claude, Gemini) vào JupyterLab qua Agent Client Protocol | |
| **Ibis** | ibis-project/ibis | Apache-2.0 | ~6.6k | Dataframe portable, backend DuckDB/Polars/BigQuery | |
| **Data Formulator** (Microsoft) | microsoft/data-formulator | MIT | – | Tạo biểu đồ/transform bằng AI | |
| **MindsDB** | mindsdb/mindsdb | Elastic 2.0 | – | "AI trong database", federated query | |
| **Open Interpreter** | openinterpreter/open-interpreter | AGPL-3.0 | – | LLM chạy code local để phân tích | |
| Evidence, Streamlit, Gradio | – | – | – | Dashboard/app dữ liệu | |

**Mẫu kiến trúc phổ biến:** DuckDB/Polars làm engine → LLM sinh SQL/Python (Vanna/PandasAI) → chạy trong sandbox (mục 11) → trực quan hóa (Data Formulator/marimo). Bảo mật: text-to-SQL cần read-only connection + allowlist bảng.

## Bổ sung: text-to-SQL, BI có AI & lớp metadata (đã xác minh 2026-10-12)

| Repo | ★ (12/10) | License | Hoạt động gần nhất | Vì sao chất lượng | Lưu ý |
|---|---|---|---|---|---|
| **Canner/WrenAI** | 17,9k | Apache-2.0 (code), CC-BY-4.0 (docs) | wren v0.15.0 (21/9/2026) | Text-to-SQL/GenBI có quản trị qua semantic layer (MDL); engine Rust kiểm SQL sinh ra trước khi chạy; MCP server; hơn 20 nguồn dữ liệu | Vừa tái cấu trúc lớn; dành sẵn AGPL-3.0 cho module tương lai; tên và logo là thương hiệu |
| **eosphoros-ai/DB-GPT** | 20,1k | MIT | commit 11/10/2026 (v0.8.2, 8/2026) | Trợ lý dữ liệu agentic: Text2SQL, RAG, workflow AWEL; fine-tune Text2SQL qua DB-GPT-Hub; có paper multi-agent | Phát hành thưa |
| **OtterMind/Chat2DB** (chuyển từ chat2db/Chat2DB) | 28,3k | Apache-2.0 sửa đổi, source-available từ v5.3.0 (không OSI) | v5.3.8 (9/10/2026) | Client SQL có AI, tự mang LLM để sinh, giải thích, tối ưu SQL; hơn 40 CSDL; chạy local | Cấm host hoặc cung cấp cho bên thứ ba khi chưa có văn bản cho phép |
| **dataease/SQLBot** | 6,9k | FIT2CLOUD Open Source License (GPLv3 + hạn chế) | v1.10.2 (23/9/2026) | Hỏi dữ liệu bằng LLM + RAG, tách workspace, phân quyền dữ liệu chi tiết; MCP; nhúng vào Dify, n8n, MaxKB | Không được đổi logo/bản quyền; bản phái sinh theo GPLv3 |
| **apache/superset** | 75,1k | Apache-2.0 | 12/10/2026 | BI doanh nghiệp quản trị kiểu ASF; MCP server ngay trong repo (`superset/mcp_service`) cho agent đọc chart, dashboard, SQL Lab | Phần AI chỉ qua MCP, README không có trợ lý AI dựng sẵn |
| **metabase/metabase** | 49,6k | AGPL-3.0 + license thương mại | v64.1 (7/10/2026) | BI dễ dùng, embedded analytics; trợ lý **Metabot** chạy tự host bằng API key riêng, không cần gói trả phí | AGPL; nội dung "verified" và audit AI chỉ có ở Pro/Enterprise |
| **tobymao/sqlglot** | 9,7k | MIT | 12/10/2026 | Parser/transpiler/optimizer SQL không phụ thuộc, hơn 30 dialect; SQLMesh dùng | Chỉ là thư viện; commit breaking ("!") thường xuyên → ghim phiên bản |
| **datahub-project/datahub** | 12,8k | Apache-2.0 | v1.8.0rc5 (8/10/2026) | Nền tảng metadata/ngữ cảnh dữ liệu cho agent, khởi đầu ở LinkedIn; hơn 150 tích hợp, MCP server chính thức | Tích hợp agent native nằm ở DataHub Cloud trả phí; chạy thử local cần 8 GB RAM |

**Nhận xét:**

- Lớp an toàn cho text-to-SQL (bổ sung cho "read-only + allowlist bảng" ở trên): parse câu SQL do LLM sinh bằng **sqlglot**, chặn mọi lệnh không phải `SELECT` và mọi bảng ngoài allowlist **trước khi** gửi tới DB; WrenAI làm việc tương tự trong engine Rust của nó.
- License là điểm khác biệt lớn nhất của nhóm này: Chat2DB bỏ Apache-2.0 từ v5.3.0 và cấm cả việc host miễn phí cho người khác; SQLBot (và DataEase) dùng license FIT2CLOUD; Metabase là AGPL. Superset, WrenAI (phần hiện có), DB-GPT, sqlglot, DataHub dùng license OSI thoáng.
- Commit của sqlglot nay gắn nhãn `[CLAUDE]` và có Claude là đồng tác giả — ví dụ một dự án hạ tầng lớn dùng coding agent công khai.
- Đã cân nhắc nhưng không thêm: pygwalker (16,0k★, commit cuối 5/9/2026), evidence (7,0k★), redash (28,8k★), dataease (24,6k★, FIT2CLOUD), airbyte (22,2k★, MIT + ELv2), great_expectations (11,9k★).

## Nâng cấp 31/10/2026: rà repo lớn

> Cách làm: đọc lại sao, license, trạng thái của 19 repo GitHub đã có trong mục 15 (GitHub API, 31/10/2026); clone và đọc lại mã của Vanna và PandasAI vì hai repo này đã dừng. Tìm repo còn thiếu bằng 18 truy vấn GitHub search (`text-to-sql`, `nl2sql`, `chatbi`, `semantic layer`, `data analysis agent`, `data science agent`, `mcp database sql`, `duckdb`, `dataframe`, topic `data-analysis`/`data-engineering`, và `created:>2025-10-01`). Chọn **5 repo**, clone `--filter=blob:none`, đọc LICENSE, README, manifest, CI, file telemetry và đường thực thi SQL/code. **Không cài, không chạy script của repo.** Số liệu đọc 31/10/2026.

### Trạng thái repo cũ

| Repo | Thay đổi | Hệ quả |
|---|---|---|
| `vanna-ai/vanna` | **Đã archive** (GitHub API 31/10/2026); commit cuối **2/2/2026** (v2.0.2). Trang tổng hợp ghi ngày archive 29/3/2026 **(chưa xác minh)**. README không có thông báo ngừng | Không chọn cho dự án mới. Fork vẫn chạy được nhưng không có bản vá bảo mật |
| `sinaptik-ai/pandas-ai` | Commit cuối **28/10/2025** (v3.0.0 ngày 7/10/2025), tròn 1 năm đứng yên; 23,9k★ | Coi như ngừng phát triển; bảng đầu mục ghi "Cập nhật cuối 10/2025" vẫn đúng |
| `duckdb/duckdb` · `pola-rs/polars` | 42,7k · 40,2k | Polars nay ngang DuckDB; catalog bổ sung sao Polars |
| `marimo-team/marimo` · `microsoft/data-formulator` · `jupyterlab/jupyter-ai` | 23,4k · 17,6k · 4,4k | Catalog bổ sung sao còn thiếu |
| `Canner/WrenAI` · `OtterMind/Chat2DB` · `dataease/SQLBot` · `metabase/metabase` | GitHub báo `NOASSERTION` | Không đổi license: đều là license nhiều phần hoặc tuỳ chỉnh đã ghi ở bảng "Bổ sung" |
| `mindsdb/mindsdb` · `openinterpreter/open-interpreter` | Không có trong kết quả API đợt này | Chưa kiểm lại được; giữ nguyên |

**Vanna 2.0 khi đọc mã (thông tin cho ai còn dùng bản fork):**

- ⚠️ README quảng cáo "row-level security", nhưng `ToolRegistry.transform_args` trong `src/vanna/core/registry.py` mặc định **không làm gì** (NoOp); RLS là chỗ để người dùng tự viết.
- ❌ `src/vanna/tools/run_sql.py` chạy cả câu không phải `SELECT` (INSERT/UPDATE/DELETE) và chỉ báo số dòng bị ảnh hưởng. An toàn phụ thuộc hoàn toàn vào quyền của connection.
- Web component mặc định tải `https://img.vanna.ai/vanna-components.js`; mã legacy 0.x gọi `ask.vanna.ai`. Khi dịch vụ của công ty ngừng, cả hai sẽ hỏng; nên tự host file JS.

**PandasAI 3.0 khi đọc mã:**

- ⚠️ Telemetry chạy **ngay khi import**: `pandasai/helpers/logger.py` gọi `scarf_analytics()` gửi `GET https://package.pandabi.ai/pandasai-telemetry?version=…&platform=…`. Chỉ tắt khi `SCARF_NO_ANALYTICS` hoặc `DO_NOT_TRACK` **bằng đúng chuỗi `"true"`**; giá trị `DO_NOT_TRACK=1` (quy ước phổ biến) **không** tắt được.
- ⚠️ Code Python do LLM sinh chạy **ngay trong tiến trình** (`CodeExecutor.execute_and_return_result`) trừ khi truyền `sandbox=`. Thư mục `ee/` theo license Enterprise, cần ký điều khoản trước khi dùng production.

### Bảng nhanh 5 repo mới

| Repo | Nhóm | ★ · license | Commit cuối | Một dòng | Cờ |
|---|---|---|---|---|---|
| `cube-js/cube` | Semantic layer | 21,1k · Apache-2.0 (+ MIT một số gói) | 31/10/2026 | Định nghĩa metric/dimension một lần, xuất SQL/REST/GraphQL cho BI và agent | **Telemetry bật mặc định**; MCP chỉ ở Cube Cloud |
| `K-Dense-AI/scientific-agent-skills` | Skill phân tích dữ liệu khoa học | 55,5k · MIT | 26/10/2026 | 177 skill theo chuẩn Agent Skills (polars, statsmodels, EDA, tra cứu 100+ CSDL khoa học) | Nạp nhiều skill vào ngữ cảnh |
| `bytebase/dbhub` | MCP cho CSDL | 3,8k · MIT | 26/10/2026 | MCP gọn (2 tool), phân loại câu SQL + giao dịch READ ONLY làm lớp chặn | **Read-only không bật mặc định** |
| `t8y2/dbx` | Client CSDL có AI | 28,4k · Apache-2.0 | 1/11/2026 | Client 25 MB cho 100+ CSDL, trợ lý AI, MCP 3 mức quyền | 6 tháng tuổi, nhịp commit cực cao |
| `ruc-datalab/DeepAnalyze` | Model + agent data science | 4,8k · MIT (code) | 13/10/2026 | Model 8B tự làm pipeline phân tích dữ liệu, có WebUI | Không CI; sandbox Docker tuỳ chọn |

### Hồ sơ ngắn

- **Cube Core.** 11.796 commit từ 2018, 419 tác giả, 12% commit có trailer Claude, có workflow `claude-code-review.yml`. LICENSE gốc: mặc định Apache-2.0, một số gói MIT. ⚠️ `packages/cubejs-backend-shared/src/env.ts`: `CUBEJS_TELEMETRY` mặc định `true`; `track.ts` gửi sự kiện kèm `machineIdSync()` tới `https://track.cube.dev/track` (chỉ bỏ qua khi biến `CI` được đặt). Tắt bằng `CUBEJS_TELEMETRY=false`. Tài liệu MCP và "analytics chat" là dịch vụ hosted của Cube Cloud (MCP connectors chỉ ở gói Premium/Enterprise). Giá trị cho kho: semantic layer giữa LLM và kho dữ liệu, cùng ý với MDL của WrenAI. Cài: `docker run -p 4000:4000 -p 15432:15432 -v ${PWD}:/cube/conf -e CUBEJS_DEV_MODE=true -e CUBEJS_TELEMETRY=false cubejs/cube`.
- **Scientific Agent Skills (K-Dense).** 762 commit, đổi tên từ "Claude Scientific Skills"; 177 thư mục skill. Đã **gỡ 4 skill docx/pdf/pptx/xlsx chép từ `anthropics/skills`** vì license của Anthropic không cho phân phối lại, một ví dụ dọn license đúng. `scan_skills.py` quét bảo mật từng skill bằng LLM, có cache theo hash nội dung; CI chạy `security-scan`, `skill-spec-validation`, `skill-tests` ✅. Rủi ro: cài cả bộ đưa 177 mô tả skill vào ngữ cảnh; README kêu gọi star. Cài: `npx skills add K-Dense-AI/scientific-agent-skills` (chọn skill cần thay vì cài hết).
- **DBHub (Bytebase).** TypeScript, 655 commit, **68% commit có trailer Claude**. Điểm đáng học là `src/utils/sql-access-policy.ts`: phân loại từng câu thành read/dml/ddl/admin/unknown (bắt cả `xp_cmdshell`, `pg_read_file`, `LOAD_FILE`), câu không phân loại được bị coi nguy hiểm như mức cao nhất; thêm **giao dịch READ ONLY ở tầng engine** làm lớp chặn thứ hai (`readonly-transaction.ts` tự ghi rõ DDL vẫn thoát được qua implicit commit). ⚠️ Cờ `--readonly` đã bị bỏ; muốn read-only phải khai báo `readonly = true` trong `dbhub.toml`, mặc định `execute_sql` được ghi. "Ít token hơn 13–14×" là so sánh tự đo. Cài: `npx @bytebase/dbhub@latest --transport stdio --dsn "<dsn>"` kèm file `dbhub.toml` bật read-only.
- **DBX.** Rust + TS, repo tạo 29/4/2026, 9.292 commit (6.524 từ 1/7/2026), 446 tác giả, 28,4k★. Client CSDL đa nền tảng, plugin ký số, trợ lý AI tích hợp, MCP server phát hành riêng (`@dbx-app/mcp-server`) với 3 mức `read_only`/`safe_write`/`high_risk_write` và allowlist kết nối chỉnh trong Settings. Mức mặc định của MCP **chưa xác minh**. README có quảng cáo nhà tài trợ. Cài MCP: `npx -y @dbx-app/mcp-server`.
- **DeepAnalyze (RUC DataLab).** Paper arXiv 2510.16872, model DeepAnalyze-8B và dữ liệu huấn luyện trên Hugging Face, 309 commit, không có workflow CI. Model sinh và chạy code phân tích; từ 3/2026 WebUI v2 có **thực thi trong Docker sandbox** nhưng là tuỳ chọn. Hợp để nghiên cứu "data agent" chạy local bằng vLLM; license weights trên Hugging Face **chưa xác minh**. Cài: tải model rồi `vllm serve DeepAnalyze-8B`.

Đã cân nhắc nhưng chưa thêm: `tencentmusic/supersonic` (5,2k, ChatBI; Apache-2.0 **kèm điều kiện** cấm phân phối bản phái sinh khi chưa mua license, tag cuối 3/3/2025, chỉ 15 commit từ 7/2026), `sqlchat/sqlchat` (5,9k), `clidey/whodb` (5,0k), `streamlit/streamlit` (46,2k, đã nhắc ở bảng đầu), `apache/datafusion` (9,6k), `Eventual-Inc/Daft` (5,8k), `evidence-dev/evidence` (7,1k), `rilldata/rill` (3,0k).

### Mẫu chung rút ra

1. **Text-to-SQL "an toàn" phải đo bằng mã, không bằng README.** Vanna quảng cáo RLS nhưng mặc định NoOp và vẫn chạy DML; DBHub có bộ phân loại + giao dịch READ ONLY nhưng không bật mặc định. Mẫu đúng: read-only bật mặc định, hai lớp (parser như sqlglot/DBHub + quyền DB), và test các câu thoát như `SELECT 1--1;DROP TABLE t`.
2. **Opt-out telemetry phải chấp nhận nhiều dạng giá trị.** PandasAI chỉ nhận `"true"`, nên `DO_NOT_TRACK=1` không có tác dụng; Cube bật mặc định với machine id. Khi kiểm thử cần kiểm cả hai dạng `1`/`true`; khi cấu hình chọn giá trị đúng từng công cụ và dùng biến opt-out riêng. Không thể đặt đồng thời hai giá trị cho cùng một biến.
3. **Code do LLM sinh chạy trong tiến trình là mặc định nguy hiểm** (PandasAI, DeepAnalyze trước 3/2026). Ghép với sandbox ở mục 11.
4. **Dự án text-to-SQL độc lập đang tàn**: Vanna archive, PandasAI dừng 1 năm; phần AI dồn về semantic layer (Cube, WrenAI), BI lớn (Superset MCP, Metabase Metabot) và MCP cho CSDL (DBHub, DBX).
5. **Dọn license khi gom skill**: K-Dense gỡ skill chép từ Anthropic. Kho skill nào vendored nội dung bên thứ ba cần ghi nguồn và license từng skill.

**Nguồn (31/10/2026):** GitHub search API (18 truy vấn + `repo:` cho 19 repo cũ và 5 repo mới) · clone `--filter=blob:none`, đọc: vanna (LICENSE, README.md, pyproject.toml, src/vanna/core/registry.py, src/vanna/tools/run_sql.py, src/vanna/servers/base/templates.py, src/vanna/legacy/), pandas-ai (LICENSE, ee/LICENSE, pyproject.toml, pandasai/helpers/telemetry.py, pandasai/helpers/logger.py, pandasai/agent/base.py), cube (LICENSE, README.md, packages/cubejs-backend-shared/src/{env.ts, track.ts}, docs-mintlify/docs/integrations/mcp-server.mdx, docs-mintlify/admin/ai/mcp-connectors.mdx), scientific-agent-skills (LICENSE.md, README.md, scan_skills.py, .github/workflows/), dbhub (LICENSE, README.md, dbhub.toml.example, src/utils/{sql-access-policy.ts, readonly-transaction.ts}, src/config/env.ts), dbx (LICENSE, NOTICE, README.md), DeepAnalyze (LICENSE, README.md), supersonic (LICENSE) · https://github.com/vanna-ai/vanna · https://landscape.jimmysong.io/projects/vanna/ · https://github.com/sinaptik-ai/pandas-ai · https://github.com/cube-js/cube · https://github.com/K-Dense-AI/scientific-agent-skills · https://github.com/bytebase/dbhub · https://github.com/t8y2/dbx · https://github.com/ruc-datalab/DeepAnalyze · https://arxiv.org/abs/2510.16872 · https://github.com/tencentmusic/supersonic

## 4. Nâng trần 2/11/2026: đo độ đúng text-to-SQL, data contract và lineage (yêu cầu người dùng)

> Cách làm: grep `data/projects.json` theo `repo` để loại trùng; GitHub search API ngày 2/11/2026 (`repo:` cho từng ứng viên; phát hiện `great-expectations/great_expectations` nay là `fivetran/great_expectations` và `dbt-labs/dbt-core` nay là `dbt-labs/dbt` qua truy vấn tên); clone `--depth 1 --filter=blob:none` 7 repo, đọc LICENSE, README, manifest, file chấm điểm, mã telemetry và CI. **Không cài, không chạy mã của repo.**

**Trần hiện tại:**

- Mục có nhiều công cụ text-to-SQL/BI và một lớp **an toàn** đã đo bằng mã (sqlglot, DBHub, "Mẫu chung rút ra" ý 1), nhưng **không có bộ đo độ đúng** của SQL do LLM sinh: không biết WrenAI, DB-GPT hay bản fork Vanna trả lời đúng bao nhiêu phần trăm.
- Không có lớp **chất lượng dữ liệu**: `great_expectations` bị "cân nhắc nhưng không thêm" (bảng Bổ sung 12/10/2026). Agent trả lời đúng SQL trên dữ liệu sai vẫn là trả lời sai.
- Không có chuẩn **lineage**: DataHub (bảng Bổ sung) là kho metadata, nhưng chưa có giao thức mở để job tự phát sự kiện "bảng này sinh từ đâu". Lớp transform (dbt) cũng chưa có trong catalog.

| Repo | Lớp | ★ · license (2/11/2026) | Commit cuối | Vì sao nâng trần | Rủi ro |
|---|---|---|---|---|---|
| `xlang-ai/Spider2` | Chuẩn | 886 · MIT | 12/8/2026 | Text-to-SQL cấp doanh nghiệp: Spider 2.0-Snow 547 task (Snowflake), -Lite 547 task (BigQuery 214, Snowflake 198, SQLite 135), -DBT 68 task; có baseline Spider-Agent (bản gọi tool không cần Docker) và leaderboard | Bản Snow phụ thuộc tài khoản Snowflake của nhóm, đang bị tạm ngưng theo News 12/8/2026; gold SQL chỉ công bố một phần, nhóm khuyên không dùng để SFT |
| `bird-bench/mini_dev` | Chuẩn | 192 · CC BY-SA 4.0 (badge README; repo **không có file LICENSE**) | 28/10/2026 | BIRD Mini-Dev: 500 câu SELECT chất lượng cao trên SQLite, MySQL, PostgreSQL; ba metric EX (đúng kết quả), R-VES (hiệu năng câu SQL), Soft F1; bản cập nhật 2026 (28/10) sửa nhãn sau góp ý cộng đồng; kèm LiveSQLBench | Dữ liệu share-alike; sao thấp vì leaderboard chính nằm ở bird-bench.github.io; R-VES dao động theo máy, README khuyên tăng timeout và chạy lặp |
| `fivetran/great_expectations` (GX Core) | Cổng máy | 11,9k · Apache-2.0 | 22/10/2026 (1.24.1) | "Unit test cho dữ liệu": Expectation + Checkpoint, Python 3.10–3.14. Bản mới **đóng gói agent skill** và lệnh cài: mỗi thư mục skill có manifest sở hữu (phiên bản + hash), chạy lại là no-op, không ghi đè thư mục người dùng đã sửa, ghi qua thư mục tạm rồi rename | Repo đã chuyển sang tổ chức Fivetran (thời điểm và lý do **chưa xác minh**); analytics điều khiển bằng `GX_ANALYTICS_ENABLED`, giá trị mặc định **chưa xác minh**; đóng góp cần ký CLA |
| `sodadata/soda-core` | Cổng máy | 2,5k · **Elastic License 2.0** (GitHub: NOASSERTION) | 29/10/2026 (4.29.1rc0) | Data contract viết bằng YAML, hơn 50 check, chạy CLI/Python trên Postgres, Snowflake, BigQuery, Databricks, DuckDB…; có workflow `claude-de-review.yml` | ⚠️ README gọi là "open source" nhưng LICENSE là **ELv2**: cấm cung cấp dạng dịch vụ hosted, không phải license OSI. Phát hiện bất thường (anomaly detection) nằm ở Soda Cloud |
| `dbt-labs/dbt` (trước là `dbt-core`) | Đầu bảng | 14,1k · Apache-2.0 | 2/11/2026 (2.0.8) | Nhánh `main` nay là **dbt v2.0 viết lại bằng Rust** (binary đơn, artifact Parquet, kiểm chặt lúc parse); v1 Python ở nhánh `1.latest`. Data test và unit test của dbt là cổng chuẩn cho lớp transform | ⚠️ Telemetry bật mặc định: `crates/dbt-clap-core` đặt `send_anonymous_usage_stats` mặc định `true`, chỉ tắt bằng `--no-send-anonymous-usage-stats`, biến `DBT_SEND_ANONYMOUS_USAGE_STATS` hoặc cờ trong `dbt_project.yml`. `DO_NOT_TRACK` chỉ được đọc ở phần docs (docs server, export) và chỉ khi bằng đúng `"1"` |
| `OpenLineage/OpenLineage` | Chuẩn | 2,7k · Apache-2.0 | 29/10/2026 | Chuẩn mở (dự án Graduate của LF AI & Data): mô hình run/job/dataset mở rộng bằng facet, spec OpenAPI + JSON Schema (`spec/`), client Python/Java/Go, tích hợp Spark, Airflow, dbt, Flink; Marquez là bản cài đặt tham chiếu | Chỉ là chuẩn + client: cần backend (Marquez hoặc DataHub) để lưu và xem |
| `sqlfluff/sqlfluff` | Cổng máy | 10,0k · MIT | 1/11/2026 (4.5.0) | Linter và auto-fix SQL, 28 file `dialect_*.py`, templater Jinja/dbt, lõi Rust `sqlfluffrs` đang tách ra; CI test riêng với dbt và SQLMesh; workflow AgentScan phân loại PR do AI agent tạo, viết theo mẫu `pull_request_target` an toàn (không checkout mã của PR) | Chỉ kiểm cú pháp và phong cách, không kiểm ngữ nghĩa hay quyền: bổ sung chứ không thay sqlglot/DBHub |

**Stack nâng trần** (theo thứ tự lợi ích/công sức):

1. **Cổng độ đúng cho text-to-SQL:** chạy BIRD Mini-Dev (SQLite, metric EX) mỗi lần đổi prompt hoặc model của WrenAI, DB-GPT, DBHub + LLM (bảng Bổ sung, Nâng cấp 31/10); thêm tập con SQLite 135 task của Spider 2.0-Lite cho câu hỏi kiểu doanh nghiệp, và Spider 2.0-DBT nếu agent sửa dự án dbt.
2. **Ghép vào lớp an toàn đã có:** SQL do LLM sinh → sqlglot/DBHub phân loại và chặn (Mẫu chung ý 1) → sqlfluff lint → chạy trên kết nối read-only.
3. **Data contract trước khi cho agent đọc bảng:** Checkpoint của GX (Apache-2.0) hoặc contract của Soda (chỉ khi không cung cấp lại dạng dịch vụ, vì ELv2); contract fail thì agent báo "dữ liệu chưa đạt" thay vì trả lời.
4. **Lớp transform có test:** data test và unit test của dbt chạy trong CI; đặt `DBT_SEND_ANONYMOUS_USAGE_STATS=false` cùng `DO_NOT_TRACK=1`, vì chỉ `DO_NOT_TRACK` không tắt được telemetry của CLI.
5. **Lineage cho câu trả lời có nguồn:** phát sự kiện OpenLineage từ dbt/Airflow vào DataHub (đã có) hoặc Marquez; agent trích tên bảng nguồn và lần chạy job khi trả lời.

**Nguồn §4:** GitHub search API 2/11/2026 (`repo:` cho 7 repo trên; `great_expectations in:name`, `dbt in:name org:dbt-labs`; ứng viên loại: `MarquezProject/marquez` 2,3k★ (nhắc trong bước 5), `awslabs/deequ` 3,7k★ (Scala/Spark), `unionai-oss/pandera` 4,5k★, `AlibabaResearch/DAMO-ConvAI` 1,6k★ (monorepo chứa BIRD gốc)) · clone `--depth 1 --filter=blob:none`, đọc: Spider2 (HEAD cafb8673 12/8/2026; LICENSE, README.md), mini_dev (1c49a37 28/10/2026; README.md, evaluation/), great_expectations (99f4d0c 22/10/2026; LICENSE, README.md, `great_expectations/agent_skills/installer.py`, `great_expectations/__main__.py`, `data_context/data_context/abstract_data_context.py`), soda-core (1b71142 29/10/2026; LICENSE, README.md, soda-core/pyproject.toml, .github/workflows/), dbt (1890fb3 2/11/2026; LICENSE, README.md, Cargo.toml, crates/dbt-clap-core/src/lib.rs, crates/dbt-main/src/dbt_lib.rs, crates/dbt-docs-server/src/state.rs), OpenLineage (bad2d7f 29/10/2026; LICENSE, README.md, spec/, client/, integration/), sqlfluff (4339c07 1/11/2026; LICENSE.md, README.md, pyproject.toml, src/sqlfluff/dialects/, .github/workflows/agent-scan.yml) · https://github.com/xlang-ai/Spider2 · https://spider2-sql.github.io · https://github.com/bird-bench/mini_dev · https://bird-bench.github.io · https://github.com/fivetran/great_expectations · https://github.com/sodadata/soda-core · https://github.com/dbt-labs/dbt · https://github.com/OpenLineage/OpenLineage · https://github.com/MarquezProject/marquez · https://github.com/sqlfluff/sqlfluff

## 5. Data ingestion and asset orchestration

> Mở rộng ngày 2/11/2026. §4 đã có dbt, GX/Soda và OpenLineage; phần còn thiếu là **dữ liệu tới từ đâu, cập nhật thế nào, phục hồi có làm trùng hay bỏ mất không**. Các repo dưới đây đã đọc LICENSE/CI/mã chính tại commit ghim, không cài và không chạy. Mục này khác durable workflow ở mục 21: đơn vị quản lý là asset/partition/cursor và độ tươi dữ liệu.

| Repo | ★ · license (2/11/2026) | Commit đọc | Cơ chế đáng học | Giới hạn / điều kiện |
|---|---|---|---|---|
| [dagster-io/dagster](https://github.com/dagster-io/dagster/tree/ef5c227a91576661f7c4b8619b855cd95e68ccd5) | 16,361 · Apache-2.0 | 2026-10-30 · `ef5c227` | Asset dependencies, partition/backfill, resource và asset check | Cần storage/daemon/deployment; một số quan sát vận hành thuộc Dagster+; telemetry instance thường bật mặc định |
| [dlt-hub/dlt](https://github.com/dlt-hub/dlt/tree/f3b6223c82fbaf8e9119497689022e8c211883fb) | 6,049 · Apache-2.0 | 2026-10-31 · `f3b6223` | Python ingestion, cursor có state, schema inference, destination và merge | Incremental cursor không đồng nghĩa dedup toàn bảng; cần khóa/merge phù hợp; telemetry bật mặc định |
| [debezium/debezium](https://github.com/debezium/debezium/tree/859540ed7983caa6939927c9ed0fc3f83f713e61) | 13,305 · Apache-2.0 | 2026-11-01 · `859540e` | CDC theo log CSDL; snapshot rồi stream thay đổi có offset/schema | Quyền replication và hạ tầng connector; có thể phát lại event sau lỗi; exactly-once phụ thuộc connector và cấu hình toàn tuyến |

### 5.1 Đọc cơ chế trước khi chọn

- **Dagster (Dagster Labs và cộng đồng):** [BackfillPolicy](https://github.com/dagster-io/dagster/blob/ef5c227a91576661f7c4b8619b855cd95e68ccd5/python_modules/dagster/dagster/_core/definitions/backfill_policy.py) tách một run cho nhiều partition với nhiều run có trần partition; [tài liệu backfill chính thức](https://dagster.io/docs/guides/build/partitions-and-backfills/backfilling-data) giải thích khi cần tính lại lịch sử. Asset check phải gắn với điều kiện ngăn downstream phù hợp, không suy ra mọi check tự chặn materialization. [Cấu hình instance](https://github.com/dagster-io/dagster/blob/ef5c227a91576661f7c4b8619b855cd95e68ccd5/python_modules/dagster/dagster/_core/instance/methods/settings_methods.py) đặt telemetry mặc định `True` cho instance thường, `False` cho ephemeral; tắt bằng `telemetry.enabled: false` trong cấu hình instance. Cần kiểm riêng dữ liệu log/metadata và dịch vụ Dagster+ khi tích hợp.
- **dlt (dltHub):** [Incremental](https://github.com/dlt-hub/dlt/blob/f3b6223c82fbaf8e9119497689022e8c211883fb/dlt/extract/incremental/__init__.py) giữ cursor và xử lý trùng vùng biên; [merge loading](https://dlthub.com/docs/general-usage/merge-loading) mới là nơi upsert/dedup staging theo khóa. Khi nguồn có cập nhật đến muộn, cửa sổ lag và merge phải được thiết kế cùng nhau; đừng coi `max(updated_at)` là bảo đảm không mất bản ghi. [RuntimeConfiguration](https://github.com/dlt-hub/dlt/blob/f3b6223c82fbaf8e9119497689022e8c211883fb/dlt/common/configuration/specs/runtime_configuration.py) đặt `dlthub_telemetry=True`; [hướng dẫn telemetry](https://github.com/dlt-hub/dlt/blob/f3b6223c82fbaf8e9119497689022e8c211883fb/docs/website/docs/reference/telemetry.md) có cấu hình `[runtime] dlthub_telemetry=false`.
- **Debezium (cộng đồng Debezium):** đọc `README.md`, `LICENSE.txt`, `debezium-core`, connector PostgreSQL và CI connector. [FAQ chính thức](https://debezium.io/documentation/faq/) nêu lỗi xác nhận/khởi động lại có thể tạo event lặp; [tài liệu exactly-once](https://debezium.io/documentation/reference/3.5/configuration/eos.html) mô tả điều kiện Kafka Connect. Tên sản phẩm hoặc trạng thái một connector không chứng minh exactly-once từ nguồn tới bảng đích. So với polling dlt: CDC nhận delete và thứ tự log rõ hơn, đổi lại thêm quyền và gánh vận hành; với batch file nhỏ, polling có thể đủ.

### 5.2 Ma trận lựa chọn

| Bài toán | Khởi đầu phù hợp | Ràng buộc cần chứng minh |
|---|---|---|
| API/file theo giờ, số nguồn vừa phải | dlt + lịch ở mục 21 | Cursor, khóa đích, delete/tombstone, retry và state restore |
| Nhiều asset phụ thuộc, cần tính lại lịch sử | Dagster + dlt/dbt | Partition mapping, backfill đồng thời, giới hạn tải nguồn, chặn asset lỗi |
| CSDL có thay đổi liên tục, cần delete/latency thấp | Debezium + sink có upsert | Quyền replication, snapshot/offset, replay, schema evolution, khóa nguồn |
| BI/agent đọc dữ liệu | Bất kỳ luồng trên + GX/Soda/dbt + DataHub/OpenLineage (§4) | Freshness theo domain, quyền từng tenant, lineage và khả năng truy ngược câu trả lời |

### 5.3 Cổng chất lượng cho đường dữ liệu

1. **Hợp đồng nguồn:** ghi owner, timezone/cursor, khóa, schema, dữ liệu nhạy cảm, quyền lưu và SLA cập nhật; tách nó khỏi schema suy ra tự động.
2. **Replay nhỏ trước:** tập có insert/update/delete, trùng event, đến muộn, đổi schema; so cả tập khóa và giá trị sau khi chạy lại/khôi phục state, không chỉ số dòng.
3. **Quarantine và publish:** bản không hợp lệ vào vùng cách ly; chỉ xuất partition đạt contract/freshness, không để agent âm thầm đọc lẫn dữ liệu dở dang.
4. **Backfill có ngân sách:** ghim code/schema, snapshot đầu vào, phạm vi partition và concurrency; không để chạy lịch thường xung đột backfill trên cùng khóa.
5. **Đo vận hành:** lag nguồn→đích, tỷ lệ bản ghi bị loại, sai lệch khóa, thời gian phục hồi và chi phí mỗi lần đồng bộ. Ghép OpenLineage/DataHub và eval text-to-SQL (§4) để phân biệt SQL sai với dữ liệu cũ.

**Liên quan:** dữ liệu để huấn luyện/gán nhãn thuộc [mục 24](../24-ai-data-engineering/README.md); đây là pipeline dữ liệu vận hành. Lịch/retry tổng quát ở [mục 21](../21-autonomous-workflows/README.md), kiểm quyền ở mục 12.

**Nguồn §5:** GitHub metadata/HEAD 2/11/2026 và permalink trên; LICENSE, README, CI, `BackfillPolicy`, instance settings, `Incremental`, runtime telemetry, Debezium core/PostgreSQL; tài liệu chính thức Dagster/dlt/Debezium. Các cổng trên là tiêu chí để dự án đích áp dụng, chưa có kết quả chạy trong khảo sát này.

## 6. Nâng sâu 4/11/2026: thay đổi dữ liệu phải có plan, test, audit và đường phục hồi

**Trần hiện tại:** kho đã có text-to-SQL, semantic layer, ingestion và lineage. Xưởng cần thêm vòng đời thay đổi mô hình dữ liệu: AI đề xuất SQL → review thay đổi → test logic → tính dữ liệu ở môi trường riêng → audit kết quả → promote có kiểm soát. Phân quyền DB/tenant và migration giao dịch thuộc [mục 34](../34-backend-data-identity-integration/README.md); mô hình analytical không thay migration OLTP.

<a id="factory-2026-11-04-sqlmesh"></a>

### SQLMesh: version mô hình và audit có đường chặn thật

| Thuộc tính | Kết quả đọc |
|---|---|
| Repo · license · SHA | `TobikoData/sqlmesh` · Apache-2.0 · `c4dbac499c312ccab17cb328ffb6ecfd801ce73d` |
| Cơ chế | Model SQL/Python, snapshot/version, plan tác động và virtual environment; test dùng fixture, audit trả hàng dữ liệu vi phạm |
| Cổng test | `Context._run_plan_tests` raise `PlanError` nếu test không thành công; `skip_tests` và chế độ chỉ test thay đổi là nhánh cấu hình cần kiểm, không mặc nhiên mọi plan đều chạy mọi test |
| Cổng audit | `ModelAudit.blocking=True` mặc định, nhưng `StandaloneAudit` mặc định không blocking và validator từ chối `blocking=True`; không thể chỉ bật cờ để đổi loại audit này thành cổng chặn. Scheduler gom audit có kết quả lỗi: blocking → `NodeAuditsErrors`, nonblocking → cảnh báo |
| Telemetry | `disable_anonymized_analytics=False` trong config; dispatcher đích `analytics.tobikodata.com/v1/`. Có optout `SQLMESH__DISABLE_ANONYMIZED_ANALYTICS=true` hoặc config tương ứng; không khẳng định payload đã được audit toàn bộ |
| CI | `pr.yaml` có docs/tests/lint và ma trận; chưa chạy SQLMesh, engine cloud hay benchmark trong đợt này |

**Phạm vi kiểm (2026-11-04):** đọc tài liệu, LICENSE, mã đường gọi và workflow tại SHA dưới đây; không cài/chạy upstream. Các cổng nghiệm thu là đề xuất cho repo tích hợp, chưa phải kết quả chạy của kho. Số sao không thu thập trong đợt này.

| Lựa chọn | Mặt mạnh | Phạm vi khác nhau |
|---|---|---|
| SQLMesh | Plan/version/environment gắn với backfill và audit | Hợp với vòng thay đổi analytical model; cần đánh giá engine, state store và lịch chạy |
| dbt | Mô hình biến đổi, tests và ecosystem | So feature ở đúng bản/adapter; không gộp dbt Core/fusion/cloud thành một thực thể |
| Great Expectations / Soda | Kiểm data quality theo expectation/check | Bổ sung contract ở nguồn/đầu ra; không tự thay kế hoạch deployment SQL |
| Dagster + OpenLineage | Orchestration tài sản và quan hệ chạy | Bổ sung nguồn gốc, không tự chứng minh ý nghĩa nghiệp vụ của SQL |

**Stack cho xưởng:** chốt schema và ví dụ nghiệp vụ → AI chỉ đề xuất SQL trên dữ liệu đã giảm nhạy cảm → parser/lint + test fixture → đọc plan gồm dữ liệu cần backfill → chạy môi trường dev có hạn mức → audit blocking → promote và theo dõi freshness/volume/business invariant. Ghi plan digest, snapshot/model revision, engine, window thời gian và lineage. Không cho text-to-SQL agent quyền DDL/write production chỉ vì truy vấn đã parse.

**Cổng nghiệm thu:** fixture làm sai join cardinality, duplicate key, timezone, tiền tệ, late-arriving data và PII phải gây lỗi đúng test/audit; test rỗng, audit bị skip/nonblocking và backfill ngoài window phải được phát hiện. So sánh kết quả theo khóa/grain, không chỉ row count. Thử rollback/khôi phục state và dữ liệu trên engine đích trước khi gọi quy trình có thể phục hồi; đổi virtual view không tự đảo ngược side effect bên ngoài hay mọi DDL.

**Nguồn §6:** [LICENSE](https://github.com/TobikoData/sqlmesh/blob/c4dbac499c312ccab17cb328ffb6ecfd801ce73d/LICENSE) · [test callsite](https://github.com/TobikoData/sqlmesh/blob/c4dbac499c312ccab17cb328ffb6ecfd801ce73d/sqlmesh/core/context.py) · [audit types](https://github.com/TobikoData/sqlmesh/blob/c4dbac499c312ccab17cb328ffb6ecfd801ce73d/sqlmesh/core/audit/definition.py) · [scheduler enforcement](https://github.com/TobikoData/sqlmesh/blob/c4dbac499c312ccab17cb328ffb6ecfd801ce73d/sqlmesh/core/scheduler.py) · [analytics config](https://github.com/TobikoData/sqlmesh/blob/c4dbac499c312ccab17cb328ffb6ecfd801ce73d/sqlmesh/core/config/root.py) · [analytics dispatcher](https://github.com/TobikoData/sqlmesh/blob/c4dbac499c312ccab17cb328ffb6ecfd801ce73d/sqlmesh/core/analytics/dispatcher.py) · [CI](https://github.com/TobikoData/sqlmesh/blob/c4dbac499c312ccab17cb328ffb6ecfd801ce73d/.github/workflows/pr.yaml).

## 7. Đọc lại K-Dense-AI/scientific-agent-skills cho phân tích dữ liệu: 177 skill, 57,4k★, v2.72.0 (bài đăng người dùng gửi, đọc mã 16/11/2026)

> Bài đăng "Skill và tool hay trên GitHub, phần 2" giới thiệu bộ skill cho nghiên cứu và phân tích dữ liệu. Repo đã có dòng ở §3 (đọc 31/10); mục này đọc lại bản mới và đối chiếu từng nhóm skill bài nhắc. Mọi ý trong bài khớp mã.

| Thuộc tính | Giá trị (16/11/2026) |
|---|---|
| Repo | https://github.com/K-Dense-AI/scientific-agent-skills · **57.429★, 5.047 fork** (GitHub search API) · MIT · tag v2.72.0 · 765 commit · đổi tên từ "Claude Scientific Skills" |
| Thành phần | 177 thư mục skill theo chuẩn Agent Skills; hơn 70 skill gói Python viết theo phiên bản; skill `database-lookup` ghi 80 cơ sở dữ liệu có cách truy cập (công khai, đăng ký, có phép), cộng các skill truy cập dữ liệu riêng, tổng hơn 100 nguồn |
| Chạy trên | Claude Code, Claude Cowork, Codex, Gemini CLI, Google Antigravity, Cursor và host khác theo Agent Skills |
| Kiểm | `tests/` (kiểm cấu trúc skill, schema, đường dẫn cá nhân), `scan_skills.py` và workflow quét bảo mật skill, báo cáo quét cập nhật hằng tuần |

### 7.1 Các nhóm skill cho phân tích dữ liệu (đối chiếu tên thư mục)

| Nhóm trong bài | Skill trong repo |
|---|---|
| EDA, kiểm định giả thuyết, thiết kế thực nghiệm | `exploratory-data-analysis`, `statistical-analysis`, `experimental-design` |
| Cỡ mẫu, sai số đo | `statistical-power` (tính cỡ mẫu và power trước khi làm nghiên cứu), `uncertainty-and-units` (đơn vị vật lý và lan truyền sai số đo theo GUM bằng `pint`, `uncertainties`) |
| Bảng dữ liệu lớn, GPU | `polars`, `dask`, `vaex`; `optimize-for-gpu` (tăng tốc NumPy, SciPy, pandas, scikit-learn trên GPU NVIDIA và **kiểm kết quả vẫn đúng và nhanh hơn**) |
| Biểu đồ chuẩn công bố | `matplotlib`, `seaborn` |
| Machine learning, Bayes, chuỗi thời gian | `scikit-learn`, `statsmodels`, `shap`, `pymc`, `timesfm-forecasting` |
| Kinh tế, tài chính, học thuật | `database-lookup` (FRED cần `FRED_API_KEY`; SEC EDGAR gọi endpoint kèm header User-Agent định danh; có ghi giới hạn tốc độ từng API), `usfiscaldata`, `literature-review` (arXiv, PubMed) |

### 7.2 Điểm mạnh

- **Quy trình thay prompt rời**: mỗi skill là workflow có ví dụ chạy được và quy tắc kiểm, ví dụ power analysis trước khi thu dữ liệu, lan truyền sai số theo chuẩn đo lường, GPU phải chứng minh kết quả đúng.
- **Theo phiên bản gói**: hướng dẫn cho từng thư viện ghi phạm vi phiên bản, tránh agent dùng API cũ.
- **Truy cập dữ liệu có kỷ luật**: ghi cách xác thực, header bắt buộc và giới hạn tốc độ của từng nguồn, xếp hàng request với API giới hạn.
- **An toàn chuỗi cung ứng skill**: quét bảo mật mọi skill trong CI và khi có PR.

### 7.3 Cài và dùng

```bash
npx skills add K-Dense-AI/scientific-agent-skills
```

- Cài một skill: `gh skill install K-Dense-AI/scientific-agent-skills scanpy` (GitHub CLI 2.90.0+); thêm `--agent cursor` cho Cursor.
- Bộ 177 skill lớn: chỉ cài nhóm cần dùng cho dự án (ví dụ `exploratory-data-analysis`, `statistical-analysis`, `polars`, `scikit-learn`, `shap`).
- Nguồn cần khoá (FRED…) đặt khoá qua biến môi trường như skill hướng dẫn.
- Cùng hãng: K-Dense BYOK, trợ lý nghiên cứu chạy trên desktop dùng bộ skill này với khoá API của bạn.
- Liên quan: §4 (text-to-SQL), mục 24 (dữ liệu cho AI), mục 25 (huấn luyện).

**Nguồn §7:** bài đăng người dùng gửi 16/11/2026 · clone `--filter=blob:none` HEAD `ec59a29a03d5c40f73ab40878df04860bc00e876`: https://github.com/K-Dense-AI/scientific-agent-skills/blob/ec59a29a03d5c40f73ab40878df04860bc00e876/README.md · https://github.com/K-Dense-AI/scientific-agent-skills/blob/ec59a29a03d5c40f73ab40878df04860bc00e876/LICENSE.md · https://github.com/K-Dense-AI/scientific-agent-skills/blob/ec59a29a03d5c40f73ab40878df04860bc00e876/skills/database-lookup/SKILL.md · https://github.com/K-Dense-AI/scientific-agent-skills/blob/ec59a29a03d5c40f73ab40878df04860bc00e876/skills/statistical-power/SKILL.md · https://github.com/K-Dense-AI/scientific-agent-skills/blob/ec59a29a03d5c40f73ab40878df04860bc00e876/skills/uncertainty-and-units/SKILL.md · https://github.com/K-Dense-AI/scientific-agent-skills/blob/ec59a29a03d5c40f73ab40878df04860bc00e876/skills/optimize-for-gpu/SKILL.md · GitHub search API 16/11/2026.

<a id="anhkysuai-2026-11-23"></a>

## Đánh giá từ kho Anh Kỹ Sư AI — 23/11/2026

Phần này có **8 hồ sơ hoặc phạm vi đối chiếu** từ [nguồn tuyển chọn](https://anhkysuai.com/kho/). [Bảng đủ 1.295 repo](../data/collections/anhkysuai-kho.json) ghi trạng thái đối chiếu từng link; [danh sách URL](../data/collections/anhkysuai-kho-links.txt) phục vụ tra cứu. Nguồn tuyển chọn giúp phát hiện repo; đánh giá bên dưới dựa trên clone và permalink upstream cùng metadata GitHub ngày 2026-11-23.

Mức `docs-read`/`code-read` chỉ áp dụng phạm vi ghi tại mỗi hồ sơ. Chưa cài, build, chạy test hay benchmark mã upstream. Giấy phép có thể tách theo code, model, nội dung, asset hoặc bản enterprise; con số/tuyên bố của tác giả chưa được tái lập nếu không có ghi chú khác.

<a id="anhkysuai-2026-11-23-scikit-learn"></a>

### scikit-learn

**Repo:** [scikit-learn/scikit-learn](https://github.com/scikit-learn/scikit-learn) · **License:** BSD-3-Clause · **★ 68,299 (GitHub API, 2026-11-23)**

**Mục đích:** Bộ công cụ Python cho học máy và khai phá dữ liệu.

**Giá trị và cơ chế:** Manifest xác nhận nền NumPy, SciPy, joblib và threadpoolctl; phù hợp làm baseline truyền thống để so sánh trước khi tăng độ phức tạp của giải pháp AI.

**Giới hạn:** Bản mã đang đọc yêu cầu Python 3.12 trở lên. Chưa huấn luyện mô hình hoặc đo bộ nhớ; workflow CUDA có điều kiện chạy, không chứng minh mọi thuật toán hỗ trợ GPU.

**Cách tham khảo/tích hợp:** Ghim môi trường và lưu quy trình tiền xử lý cùng mô hình; đánh giá trên tập kiểm tách biệt.

**Thay thế:** [XGBoost](../15-ai-for-data/README.md#anhkysuai-2026-11-23-xgboost), lightgbm, [pytorch](../08-awesome-lists-learning/README.md#6c513-mô-hình-ai--huấn-luyện).

**Bằng chứng:** `docs-read`, ngày 2026-11-23, commit [`135c488ae340`](https://github.com/scikit-learn/scikit-learn/commit/135c488ae340a248178d7ed89282e3273aedd9fc). README và các tài liệu/manifest/CI hiện diện, đọc chọn lọc; chưa kiểm implementation. Chưa cài/chạy upstream.

**Nguồn:** [README.rst](https://github.com/scikit-learn/scikit-learn/blob/135c488ae340a248178d7ed89282e3273aedd9fc/README.rst) · [COPYING](https://github.com/scikit-learn/scikit-learn/blob/135c488ae340a248178d7ed89282e3273aedd9fc/COPYING) · [metadata GitHub](https://api.github.com/repos/scikit-learn/scikit-learn).

<a id="anhkysuai-2026-11-23-pandas"></a>

### pandas

**Repo:** [pandas-dev/pandas](https://github.com/pandas-dev/pandas) · **License:** BSD-3-Clause · **★ 50,607 (GitHub API, 2026-11-23)**

**Mục đích:** Thư viện Python xử lý bảng, chuỗi thời gian và dữ liệu phân tích.

**Giá trị và cơ chế:** Manifest phân tách hệ build Meson/Cython và phụ thuộc NumPy; là nền trực tiếp để kiểm dữ liệu, tạo baseline và chuẩn bị đầu vào cho công cụ AI.

**Giới hạn:** Đã đọc tài liệu và manifest, chưa thử khối lượng dữ liệu hoặc tương thích phiên bản. Các bảng lớn có thể đòi hỏi chiến lược chia dữ liệu; hiệu quả phải đo trên workload thực tế.

**Cách tham khảo/tích hợp:** Chốt dtype, quy tắc null và timezone; lưu phép biến đổi tất định thay vì chỉ lưu bảng kết quả.

**Thay thế:** [Polars](https://github.com/pola-rs/polars), [DuckDB](https://github.com/duckdb/duckdb), dask.

**Bằng chứng:** `docs-read`, ngày 2026-11-23, commit [`717bcd3eda55`](https://github.com/pandas-dev/pandas/commit/717bcd3eda554a0b2e826889f9e30efbd88f00cd). README và các tài liệu/manifest/CI hiện diện, đọc chọn lọc; chưa kiểm implementation. Chưa cài/chạy upstream.

**Nguồn:** [README.md](https://github.com/pandas-dev/pandas/blob/717bcd3eda554a0b2e826889f9e30efbd88f00cd/README.md) · [LICENSE](https://github.com/pandas-dev/pandas/blob/717bcd3eda554a0b2e826889f9e30efbd88f00cd/LICENSE) · [metadata GitHub](https://api.github.com/repos/pandas-dev/pandas).

<a id="anhkysuai-2026-11-23-xgboost"></a>

### XGBoost

**Repo:** [dmlc/xgboost](https://github.com/dmlc/xgboost) · **License:** Apache-2.0 · **★ 29,015 (GitHub API, 2026-11-23)**

**Mục đích:** Thư viện gradient boosting cho dữ liệu có cấu trúc, hỗ trợ huấn luyện và suy luận.

**Giá trị và cơ chế:** README cùng CMake cho thấy lõi native và giao diện nhiều ngôn ngữ; là mẫu tham khảo tốt cho mô hình cây trong pipeline dữ liệu bảng.

**Giới hạn:** Chưa huấn luyện dữ liệu mẫu hoặc tái hiện số đo hiệu suất; lợi ích GPU/phân tán phụ thuộc bản dựng, dữ liệu và tham số. License dataset tách khỏi thư viện.

**Cách tham khảo/tích hợp:** Đánh giá bằng chia tập theo thời gian hoặc nhóm phù hợp, lưu cấu hình và phiên bản model cùng schema đầu vào.

**Thay thế:** lightgbm, catboost, [scikit-learn](../15-ai-for-data/README.md#anhkysuai-2026-11-23-scikit-learn).

**Bằng chứng:** `docs-read`, ngày 2026-11-23, commit [`e0e4564aea60`](https://github.com/dmlc/xgboost/commit/e0e4564aea606e688b6db58d6a9235ac19748dcb). README và các tài liệu/manifest/CI hiện diện, đọc chọn lọc; chưa kiểm implementation. Chưa cài/chạy upstream.

**Nguồn:** [README.md](https://github.com/dmlc/xgboost/blob/e0e4564aea606e688b6db58d6a9235ac19748dcb/README.md) · [LICENSE](https://github.com/dmlc/xgboost/blob/e0e4564aea606e688b6db58d6a9235ac19748dcb/LICENSE) · [metadata GitHub](https://api.github.com/repos/dmlc/xgboost).

<a id="anhkysuai-2026-11-23-redash"></a>

### Redash

**Repo:** [getredash/redash](https://github.com/getredash/redash) · **License:** BSD-2-Clause; tài sản bản đồ có điều khoản riêng · **★ 28,899 (GitHub API, 2026-11-23)**

**Mục đích:** Truy vấn nguồn dữ liệu và chia sẻ biểu đồ, dashboard, lịch làm mới và cảnh báo.

**Giá trị và cơ chế:** README mô tả SQL editor, schema browser và API; phù hợp nhóm muốn cộng tác trực tiếp trên truy vấn thay vì xây dashboard từ đầu.

**Giới hạn:** Chưa kiểm quyền từng datasource hoặc thực thi truy vấn; cấu hình tài khoản DB và chia sẻ dashboard quyết định phạm vi dữ liệu. LICENSE.borders bổ sung attribution cho tài sản bản đồ.

**Cách tham khảo/tích hợp:** Dùng tài khoản nguồn chỉ đọc, kiểm giới hạn truy vấn và thời gian làm mới với dashboard nhỏ.

**Thay thế:** [Metabase](https://github.com/metabase/metabase), [Apache Superset](https://github.com/apache/superset), [DataEase](../15-ai-for-data/README.md#anhkysuai-2026-11-23-dataease).

**Bằng chứng:** `docs-read`, ngày 2026-11-23, commit [`f561a53dc55e`](https://github.com/getredash/redash/commit/f561a53dc55eeb3f20615be951560dc78bb23f4c). README và các tài liệu/manifest/CI hiện diện, đọc chọn lọc; chưa kiểm implementation. Chưa cài/chạy upstream.

**Nguồn:** [README.md](https://github.com/getredash/redash/blob/f561a53dc55eeb3f20615be951560dc78bb23f4c/README.md) · [LICENSE](https://github.com/getredash/redash/blob/f561a53dc55eeb3f20615be951560dc78bb23f4c/LICENSE) · [LICENSE.borders](https://github.com/getredash/redash/blob/f561a53dc55eeb3f20615be951560dc78bb23f4c/LICENSE.borders) · [metadata GitHub](https://api.github.com/repos/getredash/redash).

<a id="anhkysuai-2026-11-23-dataease"></a>

### DataEase

**Repo:** [dataease/dataease](https://github.com/dataease/dataease) · **License:** GPLv3 sửa đổi, kèm điều kiện thương hiệu/đóng góp · **★ 24,729 (GitHub API, 2026-11-23)**

**Mục đích:** Nền tảng BI với dashboard kéo thả và nhiều loại nguồn dữ liệu.

**Giá trị và cơ chế:** README mô tả Vue/Spring, nguồn SQL/NoSQL/API và tích hợp xử lý dữ liệu; hữu ích tham khảo trải nghiệm self-service BI.

**Giới hạn:** LICENSE thêm điều khoản không bỏ/sửa logo, copyright trên console/app và cho nhà sản xuất đổi điều khoản đóng góp; không gọi GPLv3 thuần. xpack có phạm vi riêng; chưa kiểm truy vấn hay phân quyền.

**Cách tham khảo/tích hợp:** Đối chiếu điều khoản với cách nhúng dashboard, dùng nguồn thử chỉ đọc và đo chi phí refresh trước triển khai.

**Thay thế:** [Metabase](https://github.com/metabase/metabase), [Apache Superset](https://github.com/apache/superset), [Redash](../15-ai-for-data/README.md#anhkysuai-2026-11-23-redash).

**Bằng chứng:** `docs-read`, ngày 2026-11-23, commit [`28fb59c38b78`](https://github.com/dataease/dataease/commit/28fb59c38b786fc4b7810f866977b8a0f1288202). README và các tài liệu/manifest/CI hiện diện, đọc chọn lọc; chưa kiểm implementation. Chưa cài/chạy upstream.

**Nguồn:** [README.md](https://github.com/dataease/dataease/blob/28fb59c38b786fc4b7810f866977b8a0f1288202/README.md) · [LICENSE](https://github.com/dataease/dataease/blob/28fb59c38b786fc4b7810f866977b8a0f1288202/LICENSE) · [metadata GitHub](https://api.github.com/repos/dataease/dataease).

<a id="anhkysuai-2026-11-23-matplotlib"></a>

### Matplotlib

**Repo:** [matplotlib/matplotlib](https://github.com/matplotlib/matplotlib) · **License:** Matplotlib License (permissive; gồm điều khoản lịch sử) · **★ 23,498 (GitHub API, 2026-11-23)**

**Mục đích:** Thư viện Python tạo đồ thị tĩnh, tương tác và hoạt hình.

**Giá trị và cơ chế:** README và pyproject thể hiện hệ backend xuất nhiều định dạng; phù hợp figure nghiên cứu, báo cáo và pipeline hình ảnh tái tạo được.

**Giới hạn:** Chưa render figure hay kiểm font tiếng Việt. LICENSE yêu cầu giữ thông báo và mô tả thay đổi khi phân phối bản phái sinh; không quy toàn bộ thành MIT. Backend và phiên bản ảnh hưởng đầu ra.

**Cách tham khảo/tích hợp:** Ghim môi trường, font và style; xuất vector cho bài viết, kiểm nhãn/trục và kích thước bằng ảnh thật.

**Thay thế:** plotly, [Bokeh](../15-ai-for-data/README.md#anhkysuai-2026-11-23-bokeh), altair.

**Bằng chứng:** `docs-read`, ngày 2026-11-23, commit [`a275fb423622`](https://github.com/matplotlib/matplotlib/commit/a275fb42362221dfa3aff9a130beb351166d7def). README và các tài liệu/manifest/CI hiện diện, đọc chọn lọc; chưa kiểm implementation. Chưa cài/chạy upstream.

**Nguồn:** [README.md](https://github.com/matplotlib/matplotlib/blob/a275fb42362221dfa3aff9a130beb351166d7def/README.md) · [LICENSE/LICENSE](https://github.com/matplotlib/matplotlib/blob/a275fb42362221dfa3aff9a130beb351166d7def/LICENSE/LICENSE) · [metadata GitHub](https://api.github.com/repos/matplotlib/matplotlib).

<a id="anhkysuai-2026-11-23-thingsboard"></a>

### ThingsBoard

**Đã chuyển (2026-11-23):** hồ sơ này nay nằm ở [mục 34](../34-backend-data-identity-integration/README.md#anhkysuai-2026-11-23-thingsboard); catalog con xem [catalog/](../catalog/README.md).

<a id="anhkysuai-2026-11-23-bokeh"></a>

### Bokeh

**Repo:** [bokeh/bokeh](https://github.com/bokeh/bokeh) · **License:** BSD-3-Clause · **★ 20,485 (GitHub API, 2026-11-23)**

**Mục đích:** Tạo đồ thị và ứng dụng dữ liệu tương tác trong browser từ Python.

**Giá trị và cơ chế:** README và pyproject cho thấy thư viện Python cùng BokehJS, tích hợp template và server Tornado; phù hợp dashboard nghiên cứu hoặc dữ liệu cập nhật.

**Giới hạn:** Chưa đo dữ liệu lớn/streaming; phiên bản HEAD đòi Python mới, cần xét môi trường hiện có. Trang tĩnh và ứng dụng dùng Python server có yêu cầu triển khai khác nhau.

**Cách tham khảo/tích hợp:** Bắt đầu bằng biểu đồ độc lập, chỉ dùng server khi cần callback Python và kiểm kích thước dữ liệu gửi browser.

**Thay thế:** plotly, [Matplotlib](../15-ai-for-data/README.md#anhkysuai-2026-11-23-matplotlib), [Streamlit](../06-ui-ux-design/README.md#anhkysuai-2026-11-23-streamlit).

**Bằng chứng:** `docs-read`, ngày 2026-11-23, commit [`56c5170b30b5`](https://github.com/bokeh/bokeh/commit/56c5170b30b562f5f155df04b3a790d1f3cbf949). README và các tài liệu/manifest/CI hiện diện, đọc chọn lọc; chưa kiểm implementation. Chưa cài/chạy upstream.

**Nguồn:** [README.md](https://github.com/bokeh/bokeh/blob/56c5170b30b562f5f155df04b3a790d1f3cbf949/README.md) · [LICENSE.txt](https://github.com/bokeh/bokeh/blob/56c5170b30b562f5f155df04b3a790d1f3cbf949/LICENSE.txt) · [metadata GitHub](https://api.github.com/repos/bokeh/bokeh).

## Nguồn

- https://duckdb.org/2026/08/05/github-40k-stars · https://en.wikipedia.org/wiki/Polars_(software) · https://github.com/sinaptik-ai/pandas-ai · https://github.com/topics/sql?l=python · https://aitools.flocci.in/alternatives/pandasai · https://jupysql.readthedocs.io/en/latest/tutorials/duckdb-github.html
- Bổ sung (12/10/2026): https://github.com/Canner/WrenAI · https://github.com/eosphoros-ai/DB-GPT · https://github.com/OtterMind/Chat2DB · https://github.com/dataease/SQLBot · https://github.com/apache/superset · https://github.com/apache/superset/tree/master/superset/mcp_service · https://github.com/metabase/metabase · https://www.metabase.com/docs/latest/ai/settings · https://github.com/tobymao/sqlglot · https://github.com/datahub-project/datahub · https://github.com/Kanaries/pygwalker · https://github.com/evidence-dev/evidence · https://github.com/getredash/redash · https://github.com/dataease/dataease · https://github.com/airbytehq/airbyte · https://github.com/great-expectations/great_expectations

<a id="chuyen-muc-2026-11-23"></a>

## Hồ sơ chuyển về từ mục khác — 23/11/2026

9 hồ sơ được chuyển khi chia lại catalog theo `data/taxonomy.json`. Nội dung, ngày kiểm và mức bằng chứng giữ nguyên như ở mục gốc.

<a id="chuyen-daily-stock-analysis"></a>

### daily_stock_analysis

`ZhuLinsen/daily_stock_analysis` · License: MIT · ★ 73.114 · docs-read · 2026-11-18

Hệ thống phân tích cổ phiếu theo danh mục theo dõi bằng mô hình ngôn ngữ lớn cho thị trường A, Hồng Kông, Mỹ, Nhật, Hàn, Đài Loan; tự động phân tích hằng ngày và đẩy báo cáo dạng bảng quyết định. Đẩy thông báo qua WeCom, Feishu, Telegram, Discord, Slack, email; chạy được qua GitHub Actions, Docker, dịch vụ FastAPI hoặc lịch cục bộ; có Web/desktop với backtest, danh mục và agent hỏi đáp với 15 chiến lược dựng sẵn. Điều kiện: Cần API key của ít nhất một nhà cung cấp LLM và ít nhất một kênh thông báo; README tuyên bố chỉ dùng cho học tập/nghiên cứu, không phải lời khuyên đầu tư, tác giả không chịu trách nhiệm thua lỗ. ★ 18/11/2026: 73.114 (GitHub search API), nhóm "Tài chính & Crypto" trong kho-repo của Phan Đông Giang, mục 08 §6c.5

**Hồ sơ gốc:** [mục 08](../08-awesome-lists-learning/README.md#6c524-tài-chính--crypto) (bảng/đoạn chung, giữ nguyên tại chỗ).

<a id="chuyen-qlib"></a>

### qlib

`microsoft/qlib` · License: MIT · ★ 50.373 · docs-read · 2026-11-18

Qlib: nền tảng đầu tư định lượng hướng AI mã nguồn mở của Microsoft, bao trọn từ khám phá ý tưởng, xử lý dữ liệu, huấn luyện mô hình đến backtest. Hỗ trợ học có giám sát, mô hình hóa động lực thị trường và học tăng cường; có bài báo arXiv 2009.11189 mô tả nền tảng; phát hành trên PyPI dạng gói pyqlib, chạy Linux, Windows, macOS. Điều kiện: Bộ dữ liệu chính thức tạm tắt do chính sách bảo mật dữ liệu, README trỏ tới nguồn cộng đồng; dữ liệu mẫu thu từ Yahoo Finance có thể không hoàn hảo; bản mã trên main có thay đổi phá tương thích chưa phát hành về nạp artefact (cần trusted=True). ★ 18/11/2026: 50.373 (GitHub search API), nhóm "Tài chính & Crypto" trong kho-repo của Phan Đông Giang, mục 08 §6c.5

**Hồ sơ gốc:** [mục 08](../08-awesome-lists-learning/README.md#6c524-tài-chính--crypto) (bảng/đoạn chung, giữ nguyên tại chỗ).

<a id="chuyen-finceptterminal"></a>

### FinceptTerminal

`Fincept-Corporation/FinceptTerminal` · License: AGPL-3.0-or-later · ★ 33.938 · docs-read · 2026-11-18

Fincept Terminal: ứng dụng desktop phân tích tài chính (C++20, Qt6, Python) với nghiên cứu cổ phiếu, danh mục, tin tức, trình soạn node và tự động hóa AI. Có bộ cài Windows, Linux (AppImage, deb, rpm) ở bản v4.5.2; giá lấy trực tiếp trên máy người dùng từ nguồn họ chọn (broker, sàn, Yahoo Finance); toolchain build được ghim phiên bản (CMake 3.27.7, Qt 6.8.3, Python 3.11.9). Điều kiện: AGPL-3.0: phân phối bản sửa hoặc chạy làm dịch vụ phải công bố mã; README khuyên doanh nghiệp dùng bản Enterprise trả phí; tính năng tài khoản Fincept và AI dùng máy chủ Fincept; dữ liệu cần API key/tài khoản nguồn riêng của người dùng. ★ 18/11/2026: 33.938 (GitHub search API), nhóm "Tài chính & Crypto" trong kho-repo của Phan Đông Giang, mục 08 §6c.5

**Hồ sơ gốc:** [mục 08](../08-awesome-lists-learning/README.md#6c524-tài-chính--crypto) (bảng/đoạn chung, giữ nguyên tại chỗ).

<a id="chuyen-akshare"></a>

### akshare

`akfamily/akshare` · License: MIT · ★ 23.377 · docs-read · 2026-11-18

AKShare: thư viện Python lấy dữ liệu tài chính (cổ phiếu, quỹ, phái sinh, tiền mã hóa, vĩ mô…) từ nhiều nguồn công khai qua giao diện hàm đơn giản. Phát hành trên PyPI, yêu cầu Python 64-bit 3.11.5 trở lên; dự án đi kèm AKTools cung cấp máy chủ MCP đã đăng ký trong MCP Registry chính thức (io.github.akfamily/aktools) và HTTP API; có tài liệu tiếng Trung đầy đủ. Điều kiện: README tuyên bố dữ liệu chỉ dùng cho nghiên cứu học thuật, nhà đầu tư phải tự lưu ý rủi ro dữ liệu; dữ liệu lấy từ website bên thứ ba. ★ 18/11/2026: 23.377 (GitHub search API), nhóm "Tài chính & Crypto" trong kho-repo của Phan Đông Giang, mục 08 §6c.5

**Hồ sơ gốc:** [mục 08](../08-awesome-lists-learning/README.md#6c524-tài-chính--crypto) (bảng/đoạn chung, giữ nguyên tại chỗ).

<a id="chuyen-hummingbot"></a>

### hummingbot

`hummingbot/hummingbot` · License: Apache License 2.0 · ★ 21.248 · docs-read · 2026-11-18

Framework mã nguồn mở để thiết kế và chạy bot giao dịch tự động (market making, arbitrage…) trên nhiều sàn tập trung và phi tập trung. CLI hbot điều khiển bot không tương tác với exit code ổn định; connector cho CEX CLOB, DEX CLOB và AMM DEX (qua Gateway); có chế độ paper trade trên dữ liệu Binance thật không cần API key. Điều kiện: Giao dịch thật cần API key sàn hoặc khoá ví và dùng tiền thật; cần Anaconda/Miniconda hoặc Docker. ★ 18/11/2026: 21.248 (GitHub search API), nhóm "Tài chính & Crypto" trong kho-repo của Phan Đông Giang, mục 08 §6c.5

**Hồ sơ gốc:** [mục 08](../08-awesome-lists-learning/README.md#6c524-tài-chính--crypto) (bảng/đoạn chung, giữ nguyên tại chỗ).

<a id="chuyen-spacy"></a>

### spaCy

`explosion/spaCy` · License: MIT License · ★ 34.067 · docs-read · 2026-11-18

Thư viện xử lý ngôn ngữ tự nhiên công nghiệp viết bằng Python và Cython, có pipeline huấn luyện sẵn. Hỗ trợ tách từ và huấn luyện cho hơn 70 ngôn ngữ; có mô hình cho gắn nhãn từ loại, phân tích cú pháp, NER, phân loại văn bản và hỗ trợ transformer như BERT; có hệ thống huấn luyện, đóng gói và tích hợp LLM. Điều kiện: Python >=3.7, <3.13 (chỉ 64 bit) theo README. ★ 18/11/2026: 34.067 (GitHub search API), nhóm "Tài liệu, OCR & Thị giác máy tính" trong kho-repo của Phan Đông Giang, mục 08 §6c.5

**Hồ sơ gốc:** [mục 08](../08-awesome-lists-learning/README.md#6c525-tài-liệu-ocr--thị-giác-máy-tính) (bảng/đoạn chung, giữ nguyên tại chỗ).

<a id="chuyen-dash"></a>

### dash

`plotly/dash` · License: MIT · ★ 24.494 · docs-read · 2026-11-18

Framework Python để xây ứng dụng web dữ liệu và học máy, gắn thành phần giao diện (dropdown, slider, biểu đồ) trực tiếp với mã phân tích Python. Xây trên Plotly.js, React và Flask; khoảng 50 loại biểu đồ qua Plotly.js; được Plotly bảo trì, phát hành trên PyPI. Điều kiện: Bản mã nguồn mở chạy cục bộ; tính năng triển khai, xác thực, mở rộng nằm ở Dash Enterprise trả phí. ★ 18/11/2026: 24.494 (GitHub search API), nhóm "Đồ họa, 3D & Sơ đồ" trong kho-repo của Phan Đông Giang, mục 08 §6c.5

**Hồ sơ gốc:** [mục 08](../08-awesome-lists-learning/README.md#6c527-đồ-họa-3d--sơ-đồ) (bảng/đoạn chung, giữ nguyên tại chỗ).

<a id="anhkysuai-numpy-numpy"></a>

### NumPy

- **Repo:** [numpy/numpy](https://github.com/numpy/numpy).
- **Mục đích:** Nền tảng mảng nhiều chiều và tính toán số cho Python.
- **Điểm đáng dùng:** Broadcasting, đại số tuyến tính, FFT và tích hợp C/C++/Fortran giúp dựng xử lý dữ liệu; tài liệu test có pytest và Hypothesis tùy chọn.
- **License:** BSD-3-Clause AND 0BSD AND MIT AND CC0-1.0.
- **Giới hạn:** HEAD là 2.6.0.dev0 cần Python >=3.12; dtype, overflow và ABI native cần kiểm thử, không lấy workflow redirect artifact làm bằng chứng suite đã chạy.
- **Tích hợp:** Khóa phiên bản cùng thư viện native, kiểm thử shape/dtype và kết quả số trên dữ liệu đại diện.
- **Đối chiếu:** JAX cho autodiff/accelerator; [PyTorch](../08-awesome-lists-learning/README.md#6c513-mô-hình-ai--huấn-luyện) cho tensor; [Polars](../15-ai-for-data/README.md) cho bảng dữ liệu.
- **Mức kiểm chứng:** `docs-read` — Đọc các phần mô tả và giới hạn trong README, thông báo license, metadata manifest và cấu hình CI khi có; chưa đọc toàn bộ mã triển khai, chưa cài hoặc chạy kiểm thử upstream.
- **Snapshot:** kiểm ngày 2026-11-23; commit `d592eb072efbd8dcabb5d624ba3706e675ec3538` (2026-11-22T17:20:36-07:00); 33,458 sao theo GitHub API ngày 2026-11-23. Sao không đại diện chất lượng.
- **Bằng chứng:** [README.md](https://github.com/numpy/numpy/blob/d592eb072efbd8dcabb5d624ba3706e675ec3538/README.md) · [LICENSE.txt](https://github.com/numpy/numpy/blob/d592eb072efbd8dcabb5d624ba3706e675ec3538/LICENSE.txt) · [pyproject.toml](https://github.com/numpy/numpy/blob/d592eb072efbd8dcabb5d624ba3706e675ec3538/pyproject.toml) · [.github/workflows/circleci.yml](https://github.com/numpy/numpy/blob/d592eb072efbd8dcabb5d624ba3706e675ec3538/.github/workflows/circleci.yml) · [GitHub API](https://api.github.com/repos/numpy/numpy).

<a id="anhkysuai-meta-prophet"></a>

### Prophet

**Repo:** [meta/prophet](https://github.com/meta/prophet) · **License:** MIT · **Kiểm:** 2026-11-23, `docs-read`, [`5cf15c0f6e5d`](https://github.com/meta/prophet/tree/5cf15c0f6e5d5259d9dd8d511fb4e15a45884cdc) (commit 2026-10-22). **Sao:** 20,496 tại 2026-11-23 theo [GitHub API](https://api.github.com/repos/meta/prophet).

| Mục | Đánh giá |
|---|---|
| Mục đích | Dự báo chuỗi thời gian bằng mô hình cộng với xu hướng, mùa vụ theo năm/tuần/ngày và ảnh hưởng ngày lễ. |
| Giá trị và cơ chế theo tài liệu | README mô tả trường hợp phù hợp là dữ liệu có mùa vụ mạnh và nhiều chu kỳ lịch sử; có gói Python/R, CI kiểm Python. Có thể làm baseline cho dự báo nhu cầu hoặc chỉ số hoạt động. |
| Giới hạn | README 2026 xác nhận maintenance mode từ v1.4.0: sửa lỗi, dependency và đồng bộ R/Python, không có tính năng mới dự kiến. Tuyên bố chống outlier không thay kiểm định trên dữ liệu cụ thể. |
| Điều kiện tích hợp | Backtest theo trục thời gian, so với seasonal naive, kiểm leakage và khoảng dự báo; chuẩn hóa lịch/ngày lễ, theo dõi sai số theo phân khúc trước dùng quyết định sản phẩm. |
| Lựa chọn đối chiếu | StatsForecast; Statsmodels; Darts. |

**Phạm vi bằng chứng:** đã clone, đọc trích đoạn tài liệu, giấy phép và các file cấu hình được dẫn dưới đây; chưa chạy mã, build, benchmark hoặc test upstream. `docs-read` không phải kiểm chứng implementation.

**Nguồn tại cùng SHA:** [README.md](https://github.com/meta/prophet/blob/5cf15c0f6e5d5259d9dd8d511fb4e15a45884cdc/README.md) · [LICENSE](https://github.com/meta/prophet/blob/5cf15c0f6e5d5259d9dd8d511fb4e15a45884cdc/LICENSE) · [.github/workflows/build-and-test.yml](https://github.com/meta/prophet/blob/5cf15c0f6e5d5259d9dd8d511fb4e15a45884cdc/.github/workflows/build-and-test.yml).

<a id="chuan-hoa-2026-11-23"></a>

## Chuẩn hóa bằng chứng hồ sơ cũ — 23/11/2026

Các hồ sơ dưới đây có từ trước khi kho ghi mức kiểm. Ngày 2026-11-23 mỗi repo được clone nông tại commit ghi trong bảng, đọc LICENSE, README, manifest và CI (nếu có); không cài, build hay chạy mã upstream. Nhận định cũ ở phần trên giữ nguyên; chỗ nào khác với lần đọc này được ghi trong cột Nhận định. Số sao lấy qua GitHub search API cùng ngày.

<a id="ch-apache-superset"></a>

### Apache Superset

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/apache/superset |
| License | Apache-2.0 (khớp catalog) |
| Phiên bản đã đọc | `174aa908fbef0cc5e2e913b3c5fbf63166298cc9` (commit 2026-11-23) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE.txt, pyproject.toml, setup.py (manifest chỉ trích dòng name/version/license); chưa chạy upstream |
| Bảo trì | Commit cuối 2026-11-23; rất nhiều workflow CI (chỉ xem tên). |
| Nhận định | Nền tảng BI và khám phá dữ liệu mã nguồn mở của ASF (dashboard, SQL Lab, nhiều connector). Repo có sẵn AGENTS.md, CLAUDE.md, GEMINI.md cho trợ lý lập trình. |
| Nguồn | [README](https://github.com/apache/superset/blob/174aa908fbef0cc5e2e913b3c5fbf63166298cc9/README.md) · [LICENSE](https://github.com/apache/superset/blob/174aa908fbef0cc5e2e913b3c5fbf63166298cc9/LICENSE.txt) · [pyproject.toml](https://github.com/apache/superset/blob/174aa908fbef0cc5e2e913b3c5fbf63166298cc9/pyproject.toml) · [setup.py](https://github.com/apache/superset/blob/174aa908fbef0cc5e2e913b3c5fbf63166298cc9/setup.py) |

<a id="ch-bird-mini-dev"></a>

### BIRD Mini-Dev

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/bird-bench/mini_dev |
| License | Không có file LICENSE; README chỉ có badge CC BY-SA 4.0 (khớp catalog) |
| Phiên bản đã đọc | `1c49a375e76c471e218564da3f4617513d33e371` (commit 2026-10-28) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md (manifest chỉ trích dòng name/version/license); chưa chạy upstream |
| Bảo trì | Commit cuối 2026-10-28; không có CI. |
| Nhận định | Bộ dữ liệu và mã đánh giá BIRD Mini-Dev cho text-to-SQL (SQLite, MySQL, PostgreSQL; metric EX, R-VES, Soft F1) kèm live_sql_bench_sqlite. Không có file LICENSE nên điều khoản mã chưa rõ; chỉ badge README nêu CC BY-SA 4.0 (dữ liệu share-alike). |
| Nguồn | [README](https://github.com/bird-bench/mini_dev/blob/1c49a375e76c471e218564da3f4617513d33e371/README.md) |

<a id="ch-chat2db"></a>

### Chat2DB

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/OtterMind/Chat2DB |
| License | Apache-2.0 sửa đổi từ v5.3.0 (source-available, khớp catalog); bản trước 5.3.0 vẫn Apache-2.0 |
| Phiên bản đã đọc | `96428d5a6598fc3a78f7fb47553f47ce4e71b02a` (commit 2026-11-11) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE (manifest chỉ trích dòng name/version/license); chưa chạy upstream |
| Bảo trì | Commit cuối 2026-11-11; có CI (chỉ xem tên workflow). |
| Nhận định | Client CSDL và SQL workspace có AI (desktop, web, Docker, CLI, MCP). LICENSE từ v5.3.0 cho dùng cá nhân, tổ chức nội bộ, nghiên cứu/phi lợi nhuận; cấm cung cấp dịch vụ/sản phẩm ngoài, nhúng, white-label hoặc OEM nếu chưa có giấy phép thương mại. Không phải OSS đúng nghĩa. |
| Nguồn | [README](https://github.com/OtterMind/Chat2DB/blob/96428d5a6598fc3a78f7fb47553f47ce4e71b02a/README.md) · [LICENSE](https://github.com/OtterMind/Chat2DB/blob/96428d5a6598fc3a78f7fb47553f47ce4e71b02a/LICENSE) |

<a id="ch-cube-core"></a>

### Cube Core

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/cube-js/cube |
| License | Apache-2.0 mặc định, MIT cho một số gói (khớp catalog) |
| Phiên bản đã đọc | `b27ad6dd1e0b34f6e0ce4ace71ac5d0a8453a1b8` (commit 2026-11-23) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE, package.json, DEPRECATION.md (manifest chỉ trích dòng name/version/license); chưa chạy upstream |
| Bảo trì | Commit cuối 2026-11-23; nhiều workflow CI (chỉ xem tên). |
| Nhận định | Lớp ngữ nghĩa (semantic layer) mã nguồn mở cho phân tích và API dữ liệu; LICENSE gốc nói mặc định Apache-2.0 trừ khi header hoặc LICENSE của gói chỉ định MIT (client là MIT, backend Apache-2.0 theo README). Có DEPRECATION.md liệt kê tính năng sắp gỡ. |
| Nguồn | [README](https://github.com/cube-js/cube/blob/b27ad6dd1e0b34f6e0ce4ace71ac5d0a8453a1b8/README.md) · [LICENSE](https://github.com/cube-js/cube/blob/b27ad6dd1e0b34f6e0ce4ace71ac5d0a8453a1b8/LICENSE) · [package.json](https://github.com/cube-js/cube/blob/b27ad6dd1e0b34f6e0ce4ace71ac5d0a8453a1b8/package.json) · [DEPRECATION.md](https://github.com/cube-js/cube/blob/b27ad6dd1e0b34f6e0ce4ace71ac5d0a8453a1b8/DEPRECATION.md) |

<a id="ch-data-formulator"></a>

### Data Formulator

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/microsoft/data-formulator |
| License | MIT (khớp catalog) |
| Phiên bản đã đọc | `5477f0e236426dc8f74a498ec400414fba7fbc0f` (commit 2026-08-15) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE, pyproject.toml, package.json (manifest chỉ trích dòng name/version/license); chưa chạy upstream |
| Bảo trì | Commit cuối 2026-08-15 (khoảng 100 ngày trước thời điểm kiểm); pyproject 0.8.0b1 (beta). |
| Nhận định | Công cụ Microsoft khám phá và trực quan hóa dữ liệu bằng agent AI (cài qua uvx/pip, có demo online). Cần CLA khi đóng góp. Bản hiện tại đánh dấu beta. |
| Nguồn | [README](https://github.com/microsoft/data-formulator/blob/5477f0e236426dc8f74a498ec400414fba7fbc0f/README.md) · [LICENSE](https://github.com/microsoft/data-formulator/blob/5477f0e236426dc8f74a498ec400414fba7fbc0f/LICENSE) · [pyproject.toml](https://github.com/microsoft/data-formulator/blob/5477f0e236426dc8f74a498ec400414fba7fbc0f/pyproject.toml) · [package.json](https://github.com/microsoft/data-formulator/blob/5477f0e236426dc8f74a498ec400414fba7fbc0f/package.json) |

<a id="ch-datahub"></a>

### DataHub

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/datahub-project/datahub |
| License | Apache-2.0 (khớp catalog) |
| Phiên bản đã đọc | `c45a1233fe1e9f7e91905d55156bfa0676f52d2e` (commit 2026-11-23) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE, NOTICE (manifest chỉ trích dòng name/version/license); chưa chạy upstream |
| Bảo trì | Commit cuối 2026-11-23; rất nhiều workflow CI (chỉ xem tên). |
| Nhận định | Nền tảng metadata/data catalog (lineage cấp cột, governance, hơn 150 tích hợp theo README: tuyên bố tác giả), có module datahub-agent-context cho agent. README tách bản tự host (Apache 2.0) khỏi bản cloud thương mại. |
| Nguồn | [README](https://github.com/datahub-project/datahub/blob/c45a1233fe1e9f7e91905d55156bfa0676f52d2e/README.md) · [LICENSE](https://github.com/datahub-project/datahub/blob/c45a1233fe1e9f7e91905d55156bfa0676f52d2e/LICENSE) · [NOTICE](https://github.com/datahub-project/datahub/blob/c45a1233fe1e9f7e91905d55156bfa0676f52d2e/NOTICE) |

<a id="ch-db-gpt"></a>

### DB-GPT

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/eosphoros-ai/DB-GPT |
| License | MIT (khớp catalog) |
| Phiên bản đã đọc | `c7a8def445d5c76b01eb0651c085eb9c7133892e` (commit 2026-11-22) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE, pyproject.toml (manifest chỉ trích dòng name/version/license); chưa chạy upstream |
| Bảo trì | Commit cuối 2026-11-22; có CI. README.md đọc đầu trang; README.hi.md không dùng. |
| Nhận định | Framework ứng dụng dữ liệu AI-native (AWEL, agent, text-to-SQL, nhiều ngôn ngữ README), pyproject dbgpt-mono 0.8.3. Có DISCKAIMER.md và SKILL_MIGRATION_GUIDE.md; repo dùng nhiều thành phần nên cần kiểm phụ thuộc trước khi dùng. |
| Nguồn | [README](https://github.com/eosphoros-ai/DB-GPT/blob/c7a8def445d5c76b01eb0651c085eb9c7133892e/README.md) · [LICENSE](https://github.com/eosphoros-ai/DB-GPT/blob/c7a8def445d5c76b01eb0651c085eb9c7133892e/LICENSE) · [pyproject.toml](https://github.com/eosphoros-ai/DB-GPT/blob/c7a8def445d5c76b01eb0651c085eb9c7133892e/pyproject.toml) |

<a id="ch-dbhub"></a>

### DBHub

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/bytebase/dbhub |
| License | MIT (khớp catalog) |
| Phiên bản đã đọc | `b45ab6d1119d2a18454565c949647649cbeaafe2` (commit 2026-11-21) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE, package.json (manifest chỉ trích dòng name/version/license); chưa chạy upstream |
| Bảo trì | Commit cuối 2026-11-21; có CI (chỉ xem tên). |
| Nhận định | MCP server cho CSDL (Postgres, MySQL...) của Bytebase, gói npm dbhub 2.1.0. README tự giới thiệu là bản thay thế còn bảo trì cho server-postgres chính thức đã archive; nhắc dùng Bytebase nếu cần guardrail doanh nghiệp. |
| Nguồn | [README](https://github.com/bytebase/dbhub/blob/b45ab6d1119d2a18454565c949647649cbeaafe2/README.md) · [LICENSE](https://github.com/bytebase/dbhub/blob/b45ab6d1119d2a18454565c949647649cbeaafe2/LICENSE) · [package.json](https://github.com/bytebase/dbhub/blob/b45ab6d1119d2a18454565c949647649cbeaafe2/package.json) |

<a id="ch-dbt-v2-rust"></a>

### dbt (v2, Rust)

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/dbt-labs/dbt |
| License | Apache-2.0 (khớp catalog; bản phân phối dbt thương mại dùng license riêng) |
| Phiên bản đã đọc | `15a0ed70a69eaeeba0388b2fedf91d41a136f0e9` (commit 2026-11-23) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE, Cargo.toml, pyproject.toml (manifest chỉ trích dòng name/version/license); chưa chạy upstream |
| Bảo trì | Commit cuối 2026-11-23; nhiều workflow CI (chỉ xem tên). |
| Nhận định | Nhánh main là dbt v2.0 viết lại bằng Rust (Cargo workspace, crates/dbt-*); v1 Python chuyển sang nhánh 1.latest. Mã trong repo Apache-2.0; README nói bản "dbt" phân phối có tùy biến theo giấy phép sản phẩm của dbt Labs. |
| Nguồn | [README](https://github.com/dbt-labs/dbt/blob/15a0ed70a69eaeeba0388b2fedf91d41a136f0e9/README.md) · [LICENSE](https://github.com/dbt-labs/dbt/blob/15a0ed70a69eaeeba0388b2fedf91d41a136f0e9/LICENSE) · [Cargo.toml](https://github.com/dbt-labs/dbt/blob/15a0ed70a69eaeeba0388b2fedf91d41a136f0e9/Cargo.toml) · [pyproject.toml](https://github.com/dbt-labs/dbt/blob/15a0ed70a69eaeeba0388b2fedf91d41a136f0e9/pyproject.toml) |

<a id="ch-dbx"></a>

### DBX

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/t8y2/dbx |
| License | Apache-2.0 (khớp catalog) |
| Phiên bản đã đọc | `b1a48f113ef64de788dbf84f296bc770630d60d1` (commit 2026-11-23) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE, package.json, NOTICE (manifest chỉ trích dòng name/version/license); chưa chạy upstream |
| Bảo trì | Commit cuối 2026-11-23; nhiều workflow CI (chỉ xem tên). |
| Nhận định | Client CSDL đa nền tảng (README nêu 100+ CSDL, bản 25 MB, trợ lý AI, MCP: tuyên bố tác giả) viết bằng Rust/Tauri, version 0.6.72. NOTICE ghi mã debugger PL/SQL dùng lại từ đóng góp bên thứ ba. |
| Nguồn | [README](https://github.com/t8y2/dbx/blob/b1a48f113ef64de788dbf84f296bc770630d60d1/README.md) · [LICENSE](https://github.com/t8y2/dbx/blob/b1a48f113ef64de788dbf84f296bc770630d60d1/LICENSE) · [package.json](https://github.com/t8y2/dbx/blob/b1a48f113ef64de788dbf84f296bc770630d60d1/package.json) · [NOTICE](https://github.com/t8y2/dbx/blob/b1a48f113ef64de788dbf84f296bc770630d60d1/NOTICE) |

<a id="ch-deepanalyze"></a>

### DeepAnalyze

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/ruc-datalab/DeepAnalyze |
| License | MIT cho code (khớp catalog); README không nêu license weights nên chưa xác minh |
| Phiên bản đã đọc | `afc697a11675c59683b9f6596c3ab3b3d661182a` (commit 2026-11-02) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE (manifest chỉ trích dòng name/version/license); chưa chạy upstream |
| Bảo trì | Commit cuối 2026-11-02; không có thư mục .github (CI). |
| Nhận định | Mô hình 8B và agent tự làm pipeline khoa học dữ liệu (chuẩn bị, phân tích, mô hình, báo cáo), có WebUI và API. Mã MIT; license trọng số trên Hugging Face và dữ liệu huấn luyện chưa đối chiếu **(chưa xác minh)**. |
| Nguồn | [README](https://github.com/ruc-datalab/DeepAnalyze/blob/afc697a11675c59683b9f6596c3ab3b3d661182a/README.md) · [LICENSE](https://github.com/ruc-datalab/DeepAnalyze/blob/afc697a11675c59683b9f6596c3ab3b3d661182a/LICENSE) |

<a id="ch-duckdb"></a>

### DuckDB

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/duckdb/duckdb |
| License | MIT (khớp catalog) |
| Phiên bản đã đọc | `61a915cee25238738a95eef16cdf109e6ae76982` (commit 2026-11-23) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE (manifest chỉ trích dòng name/version/license); chưa chạy upstream |
| Bảo trì | Commit cuối 2026-11-23; nhiều workflow CI (chỉ xem tên). |
| Nhận định | CSDL phân tích nhúng in-process (C++), nền tảng cho nhiều công cụ dữ liệu khác trong catalog. Copyright thuộc Stichting DuckDB Foundation; repo có AI_POLICY.md về đóng góp do AI. |
| Nguồn | [README](https://github.com/duckdb/duckdb/blob/61a915cee25238738a95eef16cdf109e6ae76982/README.md) · [LICENSE](https://github.com/duckdb/duckdb/blob/61a915cee25238738a95eef16cdf109e6ae76982/LICENSE) |

<a id="ch-great-expectations-gx-core"></a>

### Great Expectations (GX Core)

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/fivetran/great_expectations |
| License | Apache-2.0 (khớp catalog) |
| Phiên bản đã đọc | `e08d1a800c8b759c84b820e420f5699392c53a98` (commit 2026-11-17) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE, setup.py (manifest chỉ trích dòng name/version/license); chưa chạy upstream |
| Bảo trì | Commit cuối 2026-11-17. Catalog dùng fivetran/great_expectations; git ls-remote của great-expectations/great_expectations trả cùng SHA, README còn badge theo tên cũ. |
| Nhận định | GX Core: thư viện kiểm chất lượng dữ liệu (Expectation, Checkpoint), hỗ trợ Python 3.10 đến 3.14. Repo vẫn có thể truy cập theo cả hai tên (cùng HEAD); README chưa cập nhật badge sang tổ chức mới. |
| Nguồn | [README](https://github.com/fivetran/great_expectations/blob/e08d1a800c8b759c84b820e420f5699392c53a98/README.md) · [LICENSE](https://github.com/fivetran/great_expectations/blob/e08d1a800c8b759c84b820e420f5699392c53a98/LICENSE) · [setup.py](https://github.com/fivetran/great_expectations/blob/e08d1a800c8b759c84b820e420f5699392c53a98/setup.py) |

<a id="ch-ibis"></a>

### Ibis

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/ibis-project/ibis |
| License | Apache-2.0 (khớp catalog) |
| Phiên bản đã đọc | `6d40f963fee940063e09956c7e60d073f4302259` (commit 2026-11-05) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE.txt, pyproject.toml (manifest chỉ trích dòng name/version/license); chưa chạy upstream |
| Bảo trì | Commit cuối 2026-11-05; có nhiều workflow CI (chỉ xem tên). |
| Nhận định | API DataFrame Python độc lập backend, biên dịch sang SQL cho nhiều engine (DuckDB, BigQuery...). Gói PyPI ibis-framework 12.0.0. |
| Nguồn | [README](https://github.com/ibis-project/ibis/blob/6d40f963fee940063e09956c7e60d073f4302259/README.md) · [LICENSE](https://github.com/ibis-project/ibis/blob/6d40f963fee940063e09956c7e60d073f4302259/LICENSE.txt) · [pyproject.toml](https://github.com/ibis-project/ibis/blob/6d40f963fee940063e09956c7e60d073f4302259/pyproject.toml) |

<a id="ch-jupyter-ai"></a>

### Jupyter AI

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/jupyterlab/jupyter-ai |
| License | BSD-3-Clause (khớp catalog) |
| Phiên bản đã đọc | `3739489155e5afb86b6fbfc539c571d948edf636` (commit 2026-11-21) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE, pyproject.toml (manifest chỉ trích dòng name/version/license); chưa chạy upstream |
| Bảo trì | Commit cuối 2026-11-21. |
| Nhận định | Tiện ích JupyterLab nối các agent AI (Claude, Codex, Copilot, Gemini...) qua Agent Client Protocol vào notebook, kèm Jupyter MCP server và hệ thống quyền. README hiện tại mô tả hướng agent, khác thiết kế magic cũ. |
| Nguồn | [README](https://github.com/jupyterlab/jupyter-ai/blob/3739489155e5afb86b6fbfc539c571d948edf636/README.md) · [LICENSE](https://github.com/jupyterlab/jupyter-ai/blob/3739489155e5afb86b6fbfc539c571d948edf636/LICENSE) · [pyproject.toml](https://github.com/jupyterlab/jupyter-ai/blob/3739489155e5afb86b6fbfc539c571d948edf636/pyproject.toml) |

<a id="ch-marimo"></a>

### marimo

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/marimo-team/marimo |
| License | Apache-2.0 (khớp catalog) |
| Phiên bản đã đọc | `6d3c29020d313f108fd60ac734705e57ad216b3f` (commit 2026-11-23) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE, pyproject.toml (manifest chỉ trích dòng name/version/license); chưa chạy upstream |
| Bảo trì | Commit cuối 2026-11-23; có workflow CI (chỉ xem tên). |
| Nhận định | Notebook Python phản ứng (reactive), lưu dạng file .py thân thiện git, chạy được như script hoặc app. Phiên bản 0.25.2 theo pyproject. |
| Nguồn | [README](https://github.com/marimo-team/marimo/blob/6d3c29020d313f108fd60ac734705e57ad216b3f/README.md) · [LICENSE](https://github.com/marimo-team/marimo/blob/6d3c29020d313f108fd60ac734705e57ad216b3f/LICENSE) · [pyproject.toml](https://github.com/marimo-team/marimo/blob/6d3c29020d313f108fd60ac734705e57ad216b3f/pyproject.toml) |

<a id="ch-metabase"></a>

### Metabase

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/metabase/metabase |
| License | AGPL-3.0 cho phần ngoài /enterprise, Metabase Commercial License cho /enterprise, license riêng cho embed (khớp ý catalog "AGPL + thương mại") |
| Phiên bản đã đọc | `525909ae2146eab25de6e8cafce72604569ed2d6` (commit 2026-11-23) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE.txt, LICENSE-AGPL.txt, LICENSE-MCL.txt, LICENSE-EMBEDDING.txt, package.json (manifest chỉ trích dòng name/version/license); chưa chạy upstream |
| Bảo trì | Commit cuối 2026-11-23; rất nhiều workflow CI (chỉ xem tên). |
| Nhận định | Công cụ BI tự phục vụ. Giấy phép nhiều phần: AGPL cho phần lõi, thư mục enterprise và tính năng Enterprise theo license thương mại, app-embed.js có thỏa thuận riêng nên không thể coi toàn repo là AGPL. |
| Nguồn | [README](https://github.com/metabase/metabase/blob/525909ae2146eab25de6e8cafce72604569ed2d6/README.md) · [LICENSE](https://github.com/metabase/metabase/blob/525909ae2146eab25de6e8cafce72604569ed2d6/LICENSE.txt) · [LICENSE-AGPL.txt](https://github.com/metabase/metabase/blob/525909ae2146eab25de6e8cafce72604569ed2d6/LICENSE-AGPL.txt) · [LICENSE-MCL.txt](https://github.com/metabase/metabase/blob/525909ae2146eab25de6e8cafce72604569ed2d6/LICENSE-MCL.txt) · [LICENSE-EMBEDDING.txt](https://github.com/metabase/metabase/blob/525909ae2146eab25de6e8cafce72604569ed2d6/LICENSE-EMBEDDING.txt) · [package.json](https://github.com/metabase/metabase/blob/525909ae2146eab25de6e8cafce72604569ed2d6/package.json) |

<a id="ch-mindsdb"></a>

### MindsDB

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/mindsdb/minds |
| License | MIT (KHÁC catalog ghi Elastic-2.0) |
| Phiên bản đã đọc | `3f7d3c690295c52b64f512333c59465d20bce0b9` (commit 2026-10-23) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE (manifest chỉ trích dòng name/version/license); chưa chạy upstream |
| Bảo trì | Commit cuối 2026-10-23; README mới cho thấy repo đã thành MindsHub. |
| Nhận định | Repo mindsdb/mindsdb nay hiển thị nội dung MindsHub (agent workspace dạng Electron/web, superproject pin submodule frontend và backend), README tự tham chiếu mindsdb/minds; git ls-remote của hai tên trả cùng HEAD nên đây là đổi tên/đổi định hướng. Không còn là "AI trong database, federated query" như catalog. |
| Nguồn | [README](https://github.com/mindsdb/minds/blob/3f7d3c690295c52b64f512333c59465d20bce0b9/README.md) · [LICENSE](https://github.com/mindsdb/minds/blob/3f7d3c690295c52b64f512333c59465d20bce0b9/LICENSE) |

<a id="ch-open-interpreter"></a>

### Open Interpreter

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/openinterpreter/open-interpreter |
| License | Apache-2.0 (khác catalog cũ: AGPL-3.0) |
| Phiên bản đã đọc | `a786d8474b0d7289320c16f00e852679fae7866e` (commit 2026-11-23) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE, package.json, .github/workflows/Dockerfile.bazel, FORK_BRANDING.md; chưa chạy upstream |
| Bảo trì | Có commit ngày 2026-11-23 |
| Nhận định | Coding agent chạy ở terminal, viết lại bằng Rust (codex-rs), tối ưu cho mô hình giá rẻ; FORK_BRANDING.md nói rõ kế thừa tên crate/giao thức từ OpenAI Codex. Lưu ý lớn: kho hiện nay không còn là bản Python AGPL cũ. |
| Nguồn | [README.md](https://github.com/openinterpreter/open-interpreter/blob/a786d8474b0d7289320c16f00e852679fae7866e/README.md) · [LICENSE](https://github.com/openinterpreter/open-interpreter/blob/a786d8474b0d7289320c16f00e852679fae7866e/LICENSE) · [package.json](https://github.com/openinterpreter/open-interpreter/blob/a786d8474b0d7289320c16f00e852679fae7866e/package.json) · [Dockerfile.bazel](https://github.com/openinterpreter/open-interpreter/blob/a786d8474b0d7289320c16f00e852679fae7866e/.github/workflows/Dockerfile.bazel) · [FORK_BRANDING.md](https://github.com/openinterpreter/open-interpreter/blob/a786d8474b0d7289320c16f00e852679fae7866e/FORK_BRANDING.md) |

<a id="ch-openlineage"></a>

### OpenLineage

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/OpenLineage/OpenLineage |
| License | Apache-2.0 |
| Phiên bản đã đọc | `eeb493c36e7e65cf33843a80df1029c5f2fd5c1e` (commit 2026-11-22) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE, LICENSE.insert.txt, pyproject.toml, .github/workflows/codeql.yml; chưa chạy upstream |
| Bảo trì | Có commit ngày 2026-11-22; CI CircleCI + GitHub Actions |
| Nhận định | Chuẩn mở về metadata/lineage: mô hình run/job/dataset mở rộng bằng facet, thuộc LF AI & Data (Graduate theo README). Có AGENTS.md và CLAUDE.md trong kho. |
| Nguồn | [README.md](https://github.com/OpenLineage/OpenLineage/blob/eeb493c36e7e65cf33843a80df1029c5f2fd5c1e/README.md) · [LICENSE](https://github.com/OpenLineage/OpenLineage/blob/eeb493c36e7e65cf33843a80df1029c5f2fd5c1e/LICENSE) · [LICENSE.insert.txt](https://github.com/OpenLineage/OpenLineage/blob/eeb493c36e7e65cf33843a80df1029c5f2fd5c1e/LICENSE.insert.txt) · [pyproject.toml](https://github.com/OpenLineage/OpenLineage/blob/eeb493c36e7e65cf33843a80df1029c5f2fd5c1e/pyproject.toml) · [codeql.yml](https://github.com/OpenLineage/OpenLineage/blob/eeb493c36e7e65cf33843a80df1029c5f2fd5c1e/.github/workflows/codeql.yml) |

<a id="ch-pandasai"></a>

### PandasAI

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/sinaptik-ai/pandas-ai |
| License | MIT (trừ pandasai/ee/ theo license riêng) |
| Phiên bản đã đọc | `bbbb771d31062d81f6fa19bafb40620d5cbe48f4` (commit 2025-10-28) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE, pyproject.toml, .github/workflows/cd.yml; chưa chạy upstream |
| Bảo trì | Commit cuối 2025-10-28, hơn 1 năm không đổi |
| Nhận định | Thư viện Python hỏi đáp dữ liệu bằng ngôn ngữ tự nhiên (pyproject v3.0.0, Python >=3.8,<3.12). LICENSE nêu rõ thư mục ee/ dưới giấy phép khác, phần còn lại MIT. Chưa xác minh claim telemetry (chưa đọc mã). |
| Nguồn | [README.md](https://github.com/sinaptik-ai/pandas-ai/blob/bbbb771d31062d81f6fa19bafb40620d5cbe48f4/README.md) · [LICENSE](https://github.com/sinaptik-ai/pandas-ai/blob/bbbb771d31062d81f6fa19bafb40620d5cbe48f4/LICENSE) · [pyproject.toml](https://github.com/sinaptik-ai/pandas-ai/blob/bbbb771d31062d81f6fa19bafb40620d5cbe48f4/pyproject.toml) · [cd.yml](https://github.com/sinaptik-ai/pandas-ai/blob/bbbb771d31062d81f6fa19bafb40620d5cbe48f4/.github/workflows/cd.yml) |

<a id="ch-polars"></a>

### Polars

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/pola-rs/polars |
| License | MIT |
| Phiên bản đã đọc | `a76f708b788547a3f5c21c6c21b31af2d0855ba7` (commit 2026-11-23) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE, Cargo.toml, .github/workflows/benchmark-remote.yml; chưa chạy upstream |
| Bảo trì | Có commit ngày 2026-11-23; nhiều workflow CI |
| Nhận định | Thư viện DataFrame lõi Rust (workspace crates/*), có binding Python/Node/R; README trỏ tới skill và MCP cho agent. Có AI_POLICY.md. |
| Nguồn | [README.md](https://github.com/pola-rs/polars/blob/a76f708b788547a3f5c21c6c21b31af2d0855ba7/README.md) · [LICENSE](https://github.com/pola-rs/polars/blob/a76f708b788547a3f5c21c6c21b31af2d0855ba7/LICENSE) · [Cargo.toml](https://github.com/pola-rs/polars/blob/a76f708b788547a3f5c21c6c21b31af2d0855ba7/Cargo.toml) · [benchmark-remote.yml](https://github.com/pola-rs/polars/blob/a76f708b788547a3f5c21c6c21b31af2d0855ba7/.github/workflows/benchmark-remote.yml) |

<a id="ch-soda-core"></a>

### Soda Core

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/sodadata/soda-core |
| License | Elastic-2.0 (ELv2; pyproject khai "Proprietary") |
| Phiên bản đã đọc | `484c2d9fbcfe2107eaa00995e54c2fae887fcb4c` (commit 2026-11-21) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE, pyproject.toml, .github/workflows/claude-de-review.yml; chưa chạy upstream |
| Bảo trì | Có commit ngày 2026-11-21; version 4.31.1rc0 |
| Nhận định | Engine data contract/data quality: hợp đồng YAML, CLI + Python API, nhiều data source. LICENSE là Elastic License 2.0 (không OSI) dù README gọi "open source"; pyproject workspace ghi license "Proprietary" nên metadata không nhất quán. |
| Nguồn | [README.md](https://github.com/sodadata/soda-core/blob/484c2d9fbcfe2107eaa00995e54c2fae887fcb4c/README.md) · [LICENSE](https://github.com/sodadata/soda-core/blob/484c2d9fbcfe2107eaa00995e54c2fae887fcb4c/LICENSE) · [pyproject.toml](https://github.com/sodadata/soda-core/blob/484c2d9fbcfe2107eaa00995e54c2fae887fcb4c/pyproject.toml) · [claude-de-review.yml](https://github.com/sodadata/soda-core/blob/484c2d9fbcfe2107eaa00995e54c2fae887fcb4c/.github/workflows/claude-de-review.yml) |

<a id="ch-spider-2-0"></a>

### Spider 2.0

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/xlang-ai/Spider2 |
| License | MIT |
| Phiên bản đã đọc | `cafb867313aab4e674652054198f383cf4018943` (commit 2026-08-12) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE; chưa chạy upstream |
| Bảo trì | Commit cuối 2026-08-12; README tự báo tài khoản Snowflake bị tạm ngưng |
| Nhận định | Benchmark text-to-SQL doanh nghiệp (spider2-lite, spider2-snow, spider2-dbt, thư mục methods cho baseline). Bản Snow phụ thuộc tài khoản Snowflake của nhóm; News 2026-08-12 xin lỗi vì tài khoản bị tạm ngưng. |
| Nguồn | [README.md](https://github.com/xlang-ai/Spider2/blob/cafb867313aab4e674652054198f383cf4018943/README.md) · [LICENSE](https://github.com/xlang-ai/Spider2/blob/cafb867313aab4e674652054198f383cf4018943/LICENSE) |

<a id="ch-sqlbot"></a>

### SQLBot

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/dataease/SQLBot |
| License | GPL-3.0 sửa đổi (thêm điều kiện: giữ LOGO/bản quyền ở frontend; người đóng góp đồng ý cho dùng thương mại và đổi điều khoản) (khác catalog cũ: FIT2CLOUD Open Source License) |
| Phiên bản đã đọc | `dd12090a70859103fcdf07cdad2052dcb23328bc` (commit 2026-11-23) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE, .github/workflows/build_and_push.yml; chưa chạy upstream |
| Bảo trì | Có commit ngày 2026-11-23 |
| Nhận định | Hệ thống ChatBI text-to-SQL dựa LLM + RAG của DataEase (README tiếng Trung), có cách ly workspace, phân quyền dữ liệu, nhúng web và MCP. Giấy phép là GPLv3 sửa đổi với điều kiện bổ sung, cần đọc kỹ trước khi dùng thương mại. |
| Nguồn | [README.md](https://github.com/dataease/SQLBot/blob/dd12090a70859103fcdf07cdad2052dcb23328bc/README.md) · [LICENSE](https://github.com/dataease/SQLBot/blob/dd12090a70859103fcdf07cdad2052dcb23328bc/LICENSE) · [build_and_push.yml](https://github.com/dataease/SQLBot/blob/dd12090a70859103fcdf07cdad2052dcb23328bc/.github/workflows/build_and_push.yml) |

<a id="ch-sqlfluff"></a>

### SQLFluff

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/sqlfluff/sqlfluff |
| License | MIT |
| Phiên bản đã đọc | `1aa1dd056a4a693b1d373250aa4b70ef6ef27ab1` (commit 2026-11-23) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE.md, pyproject.toml, .github/workflows/add-issue-labels.yaml; chưa chạy upstream |
| Bảo trì | Có commit ngày 2026-11-23; pyproject v4.5.0 |
| Nhận định | Linter SQL tự sửa lỗi, nhiều dialect, hỗ trợ templater Jinja/dbt. Có AGENTS.md và AI_POLICY.md. Chi tiết lõi Rust sqlfluffrs và workflow AgentScan chưa đọc. |
| Nguồn | [README.md](https://github.com/sqlfluff/sqlfluff/blob/1aa1dd056a4a693b1d373250aa4b70ef6ef27ab1/README.md) · [LICENSE.md](https://github.com/sqlfluff/sqlfluff/blob/1aa1dd056a4a693b1d373250aa4b70ef6ef27ab1/LICENSE.md) · [pyproject.toml](https://github.com/sqlfluff/sqlfluff/blob/1aa1dd056a4a693b1d373250aa4b70ef6ef27ab1/pyproject.toml) · [add-issue-labels.yaml](https://github.com/sqlfluff/sqlfluff/blob/1aa1dd056a4a693b1d373250aa4b70ef6ef27ab1/.github/workflows/add-issue-labels.yaml) |

<a id="ch-sqlglot"></a>

### sqlglot

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/tobymao/sqlglot |
| License | MIT |
| Phiên bản đã đọc | `d3a2eafd171021d269e06b5f7a370451d6e9f04c` (commit 2026-11-23) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE, pyproject.toml, .github/workflows/benchmark-sqlglot.yml; chưa chạy upstream |
| Bảo trì | Có commit ngày 2026-11-23 |
| Nhận định | Parser/transpiler/optimizer SQL thuần Python không phụ thuộc, hơn 30 dialect. README nay ghi chỉ nhận PR từ maintainer vì quá nhiều PR do LLM sinh; góp ý qua issue. |
| Nguồn | [README.md](https://github.com/tobymao/sqlglot/blob/d3a2eafd171021d269e06b5f7a370451d6e9f04c/README.md) · [LICENSE](https://github.com/tobymao/sqlglot/blob/d3a2eafd171021d269e06b5f7a370451d6e9f04c/LICENSE) · [pyproject.toml](https://github.com/tobymao/sqlglot/blob/d3a2eafd171021d269e06b5f7a370451d6e9f04c/pyproject.toml) · [benchmark-sqlglot.yml](https://github.com/tobymao/sqlglot/blob/d3a2eafd171021d269e06b5f7a370451d6e9f04c/.github/workflows/benchmark-sqlglot.yml) |

<a id="ch-vanna"></a>

### Vanna

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/vanna-ai/vanna |
| License | MIT |
| Phiên bản đã đọc | `365d0617c1a4567ffee1b19b40c27feb4206bfcf` (commit 2026-02-02) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE, pyproject.toml, .github/workflows/python-publish.yaml; chưa chạy upstream |
| Bảo trì | Commit cuối 2026-02-02; catalog ghi archive qua API, clone không xác nhận được |
| Nhận định | Text-to-SQL Vanna 2.0 (pyproject v2.0.2): hỏi đáp SQL có phân quyền theo người dùng, component web, FastAPI; có hướng dẫn migrate từ 0.x (LegacyVannaAdapter). Trạng thái archived theo API GitHub **(chưa xác minh)** từ clone. |
| Nguồn | [README.md](https://github.com/vanna-ai/vanna/blob/365d0617c1a4567ffee1b19b40c27feb4206bfcf/README.md) · [LICENSE](https://github.com/vanna-ai/vanna/blob/365d0617c1a4567ffee1b19b40c27feb4206bfcf/LICENSE) · [pyproject.toml](https://github.com/vanna-ai/vanna/blob/365d0617c1a4567ffee1b19b40c27feb4206bfcf/pyproject.toml) · [python-publish.yaml](https://github.com/vanna-ai/vanna/blob/365d0617c1a4567ffee1b19b40c27feb4206bfcf/.github/workflows/python-publish.yaml) |

<a id="ch-wrenai"></a>

### WrenAI

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/Canner/WrenAI |
| License | Apache-2.0 (core/sdk/skills/examples và root); docs CC-BY-4.0; AGPL-3.0 chỉ là văn bản dự phòng cho module tương lai |
| Phiên bản đã đọc | `48de0b6cbd02cbbe3753f29e37f4be24e8a9a7fd` (commit 2026-11-23) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README.md, LICENSE, LICENSE-AGPL-3.0, LICENSE-APACHE-2.0, LICENSE-CC-BY-4.0, .github/workflows/cleanup-issues.yml; chưa chạy upstream |
| Bảo trì | Có commit ngày 2026-11-23 |
| Nhận định | Nền tảng GenBI mã nguồn mở cho agent: sinh SQL có quản trị, định nghĩa nghiệp vụ lưu trong Git, 22+ nguồn dữ liệu (theo README, **chưa xác minh**). LICENSE là bản đa giấy phép theo đường dẫn; AGPL chưa áp dụng cho module nào hiện nay. |
| Nguồn | [README.md](https://github.com/Canner/WrenAI/blob/48de0b6cbd02cbbe3753f29e37f4be24e8a9a7fd/README.md) · [LICENSE](https://github.com/Canner/WrenAI/blob/48de0b6cbd02cbbe3753f29e37f4be24e8a9a7fd/LICENSE) · [LICENSE-AGPL-3.0](https://github.com/Canner/WrenAI/blob/48de0b6cbd02cbbe3753f29e37f4be24e8a9a7fd/LICENSE-AGPL-3.0) · [LICENSE-APACHE-2.0](https://github.com/Canner/WrenAI/blob/48de0b6cbd02cbbe3753f29e37f4be24e8a9a7fd/LICENSE-APACHE-2.0) · [LICENSE-CC-BY-4.0](https://github.com/Canner/WrenAI/blob/48de0b6cbd02cbbe3753f29e37f4be24e8a9a7fd/LICENSE-CC-BY-4.0) · [cleanup-issues.yml](https://github.com/Canner/WrenAI/blob/48de0b6cbd02cbbe3753f29e37f4be24e8a9a7fd/.github/workflows/cleanup-issues.yml) |
