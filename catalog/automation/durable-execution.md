<!-- File sinh tự động bởi scripts/build_catalog_views.py; sửa data/projects.json hoặc data/taxonomy.json rồi chạy lại. -->

# durable-execution — Tự động hóa & quy trình

[← Mục lục catalog](../README.md) · 15 hồ sơ.

| Dự án | Repo | License | ★ | Bằng chứng | Mục | Tóm tắt |
|---|---|---|---|---|---|---|
| [Conductor OSS](../../21-autonomous-workflows/README.md) | `conductor-oss/conductor` | Apache-2.0 | 32.399 | chưa chuẩn hóa | 21 | Engine workflow gốc Netflix (2016), nay có task LLM/MCP/A2A, SWITCH theo quyết định model, DO_WHILE có trần vòng; |
| [dapr](../../08-awesome-lists-learning/README.md#6c55-container--devops) | `dapr/dapr` | Apache License 2.0 | 26.204 | đọc tài liệu 2026-11-18 | 08 | Runtime chạy dạng sidecar cho ứng dụng phân tán, workflow bền vững và AI agent, cung cấp API thống nhất qua HTTP/gRPC. |
| [iii engine](../../10-local-llm-rag-memory/README.md#ch-iii-engine) | `iii-hq/iii` | Elastic-2.0 (engine/) và Apache-2.0 (SDK, docs, workers) | 18.937 | đọc tài liệu 2026-11-23 | 10 | Runtime worker/function/trigger thay Express+DB+queue+OTEL; |
| [Trigger.dev](../../21-autonomous-workflows/README.md) | `triggerdotdev/trigger.dev` | Apache-2.0 | 16.667 | chưa chuẩn hóa | 21 | Task TypeScript dài không timeout, retry, queue, waitpoint người duyệt, cron, module chat/skills cho agent; |
| [Hatchet](../../21-autonomous-workflows/README.md) | `hatchet-dev/hatchet` | MIT | 8.212 | chưa chuẩn hóa | 21 | Engine Go/Postgres: durable task, DAG, durable sleep/event wait, cron, webhook, rate limit, OTel; |
| [Absurd](../../21-autonomous-workflows/README.md) | `earendil-works/absurd` | Apache-2.0 | 2.522 | chưa chuẩn hóa | 21 | Durable execution chỉ cần Postgres (một file SQL), SDK TS/Py/Go; |
| [Temporal Python SDK](../../21-autonomous-workflows/README.md#temporal-replay-factory) | `temporalio/sdk-python` | MIT | 1.243 | đọc mã 2026-11-04 | 21 | Replay history gate: default raise_on_replay_failure=True; |
| [Restate TypeScript SDK](../../21-autonomous-workflows/README.md#restate-typescript-sdk) | `restatedev/sdk-typescript` | MIT | 125 | đọc mã 2026-11-02 | 21 | Durable ctx.run + ingress idempotency; |
| [Temporal AI integrations](../../21-autonomous-workflows/README.md) | `temporalio/ai-integrations` | MIT | 36 | chưa chuẩn hóa | 21 | Plugin durable cho OpenAI Agents (GA), LangGraph/Strands (preview), deepagents, Google ADK, Claude Agent SDK (pre-release); |
| [DBOS](../../21-autonomous-workflows/README.md) | `dbos-inc/dbos-transact-py` | MIT | — | chưa chuẩn hóa | 21 | Durable execution trên Postgres (có bản TS) |
| [Inngest](../../21-autonomous-workflows/README.md) | `inngest/inngest` | Apache-2.0 (server) | — | chưa chuẩn hóa | 21 | Durable function qua HTTP endpoint, hợp TypeScript/serverless |
| [Kiro Crew Task Runner](../../03-agentic-patterns-loops/README.md#beyond-the-agent-5-lop-2026-11-11) |  | proprietary | — | đọc tài liệu 2026-11-11 | 03 | Task Runner của AWS Kiro: spec Markdown → các bước, mỗi bước một phiên mới, test rồi commit, phiên reviewer riêng đọc git diff, hỏng thì revert; |
| [Restate](../../21-autonomous-workflows/README.md) | `restatedev/restate` | BUSL-1.1 | — | chưa chuẩn hóa | 21 | Durable functions, một binary tự host |
| [Temporal](../../21-autonomous-workflows/README.md) | `temporalio/temporal` | MIT | — | chưa chuẩn hóa | 21 | Durable workflow + activity, worker dài hạn; |
| [Vercel Workflow](../../21-autonomous-workflows/README.md) |  | — | — | chưa chuẩn hóa | 21 | Durable function trong Vercel |
