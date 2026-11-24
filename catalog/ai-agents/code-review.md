<!-- File sinh tự động bởi scripts/build_catalog_views.py; sửa data/projects.json hoặc data/taxonomy.json rồi chạy lại. -->

# code-review — AI agent, skill & điều phối

[← Mục lục catalog](../README.md) · 11 hồ sơ.

| Dự án | Repo | License | ★ | Bằng chứng | Mục | Tóm tắt |
|---|---|---|---|---|---|---|
| [open-code-review (ocr)](../../13-dev-stack-devops/README.md#ch-open-code-review-ocr) | `alibaba/open-code-review` | Apache-2.0 | 49.180 | đọc tài liệu 2026-11-23 | 13 | Review AI theo luật glob đường dẫn (rule.json, first-match-wins), ocr delegate không cần API key; |
| [code-review-graph](../../13-dev-stack-devops/README.md#ch-code-review-graph) | `tirth8205/code-review-graph` | MIT | 32.522 | đọc tài liệu 2026-11-23 | 13 | Đồ thị mã Tree-sitter/SQLite cấp blast radius cho review qua MCP; |
| [Qodo Merge](../../13-dev-stack-devops/README.md#ch-qodo-merge) | `The-PR-Agent/pr-agent` | MIT | 16.601 | đọc tài liệu 2026-11-23 | 13 | self-host; |
| [Code Review Bench (Martian)](../../07-eval-observability/README.md#n2-code-review-benchmark) | `withmartian/code-review-benchmark` | MIT | 306 | đọc mã 2026-11-23 | 07 | Bộ đo công cụ AI code review gồm nhánh offline (50 PR từ Sentry, Grafana, Cal.com, Discourse, Keycloak, 173 golden comment có mức nghiêm trọng và nhãn loại) và nhánh onl… |
| [SecPriv](../../12-ai-security-guardrails/README.md#nt-secpriv-skill) | `facebookresearch/secpriv-skill` | MIT | 12 | đọc mã 2026-11-23 | 12 | Một prompt skill duy nhất (SKILL.md, khoảng 18 KB) cho agent review mã theo 5 pha gộp bảo mật (20 loại CWE) và riêng tư (10 loại GDPR), có bước validator với 7 luật loại… |
| [CRBugBench](../../07-eval-observability/README.md#n2-crbugbench) | `malusamayo/CRBugBench` | — | 4 | đọc mã 2026-11-23 | 07 | Bộ 995 tác vụ định dạng Harbor (500 track fix, 495 track comment, 98 repo mã nguồn mở) để đo reviewer agent có bắt được lỗi đã biết mà agent không thấy hay không; |
| [Kestrel Review](../../13-dev-stack-devops/README.md#n2-kestrel-review) | `lpliu-art/kestrel` | Apache-2.0 | 2 | đọc mã 2026-11-23 | 13 | Công cụ review code theo hướng 'luật là câu hỏi': pipeline tất định đọc diff, khớp trigger, biến mỗi luật thành câu hỏi gửi model Jev của TypeSafe AI (trả lựa chọn có hi… |
| [reviewbench (KyleSau)](../../07-eval-observability/README.md#n2-reviewbench-kylesau) | `KyleSau/reviewbench` | MIT | 1 | đọc mã 2026-11-23 | 07 | Bộ đo reviewer AI nhỏ gọn: 25 PR dạng diff (Python, TypeScript, C#) với 21 lỗi gài tay và 6 PR sạch, chấm bằng bộ khớp tất định (cùng file, lệch dòng tối đa 3, cùng loại… |
| [rbench (decadance-dance)](../../07-eval-observability/README.md#n2-rbench-decadance) | `decadance-dance/rbench` | Apache-2.0 | 0 | đọc mã 2026-11-23 | 07 | Benchmark có thể tiếp tục chạy cho engine review code (Claude Code review, Codex review, ponytail, review-council, rreview, plain): mỗi trial là một dự án docker compose… |
| [CodeRabbit](../../13-dev-stack-devops/README.md#ch-coderabbit) |  | proprietary (SaaS, không có file LICENSE) | — | đọc tài liệu 2026-11-23 | 13 | $24/$48. |
| [Greptile](../../13-dev-stack-devops/README.md#ch-greptile) |  | proprietary (theo catalog; chưa xác minh) | — | đọc tài liệu 2026-11-23 | 13 | . |
