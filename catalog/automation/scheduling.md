<!-- File sinh tự động bởi scripts/build_catalog_views.py; sửa data/projects.json hoặc data/taxonomy.json rồi chạy lại. -->

# scheduling — Tự động hóa & quy trình

[← Mục lục catalog](../README.md) · 10 hồ sơ.

| Dự án | Repo | License | ★ | Bằng chứng | Mục | Tóm tắt |
|---|---|---|---|---|---|---|
| [Cal.diy](../../21-autonomous-workflows/README.md#anhkysuai-calcom-cal.diy) | `calcom/cal.diy` | MIT | 50.329 | đọc tài liệu 2026-11-23 | 21 | Bản cộng đồng tự host cho đặt lịch, tách khỏi các tính năng thương mại của Cal.com. |
| [Postiz](../../21-autonomous-workflows/README.md#anhkysuai-gitroomhq-postiz-app) | `gitroomhq/postiz-app` | AGPL-3.0 | 42.201 | đọc tài liệu 2026-11-23 | 21 | Ứng dụng lập lịch và quản lý xuất bản nội dung trên các kênh mạng xã hội. |
| [Healthchecks](../../33-reliability-observability-operations/README.md#n2-healthchecks) | `healthchecks/healthchecks` | BSD-3-Clause | 10.543 | đọc mã 2026-11-23 | 33 | Dịch vụ giám sát cron theo kiểu dead-man's switch: job gọi URL ping (`/start`, `/fail`, `/<exitstatus>`), nếu ping không đến đúng hạn cộng thời gian ân hạn thì chuyển tr… |
| [BullMQ](../../21-autonomous-workflows/README.md#n2-bullmq) | `taskforcesh/bullmq` | MIT | 9.628 | đọc mã 2026-11-23 | 21 | Hàng đợi job cho Node/Bun (kèm bản Python, Elixir, .NET, Rust, PHP) chạy trên Redis, từ v6 có thêm backend PostgreSQL cùng API Queue/Worker/FlowProducer. |
| [gh-aw (GitHub Agentic Workflows)](../../21-autonomous-workflows/README.md#ch-gh-aw-github-agentic-workflows) | `github/gh-aw` | MIT | 5.678 | đọc tài liệu 2026-11-23 | 21 | Markdown+frontmatter → .lock.yml GitHub Actions; |
| [Radicale](../../34-backend-data-identity-integration/README.md#nt-radicale) | `Kozea/Radicale` | GPL-3.0 | 5.245 | đọc mã 2026-11-23 | 34 | Máy chủ CalDAV/CardDAV nhỏ bằng Python (3.9.3.dev), lưu lịch/danh bạ dạng file .ics/.vcf trên đĩa, phụ thuộc defusedxml, libpass, vobject. |
| [pg-boss](../../21-autonomous-workflows/README.md#n2-timgit-pg-boss) | `timgit/pg-boss` | MIT | 4.159 | đọc mã 2026-11-23 | 21 | Hàng đợi job trên Postgres cho Node.js với SKIP LOCKED, retry có backoff, cron, dead letter, phụ thuộc job và các chính sách hàng đợi chống trùng. |
| [Graphile Worker](../../21-autonomous-workflows/README.md#n2-graphile-worker) | `graphile/worker` | MIT | 2.454 | đọc mã 2026-11-23 | 21 | Hàng đợi job Postgres cho Node.js với job_key (thay thế, debounce, throttle), retry lũy thừa, cron và gọi add_job từ SQL. |
| [Claude Code /loop & scheduled tasks](../../21-autonomous-workflows/README.md#ch-claude-code-loop-scheduled-tasks) |  | — | — | đọc tài liệu 2026-11-23 | 21 | Cron trong session: CronCreate/List/Delete, jitter, 7 ngày, 50 task, loop.md. |
| [Claude Code Routines](../../21-autonomous-workflows/README.md#ch-claude-code-routines) |  | — | — | đọc tài liệu 2026-11-23 | 21 | Cloud scheduled agent của Anthropic: trigger cron/API/GitHub, min 1h, không hỏi quyền; |
