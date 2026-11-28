# Hồ sơ: vercel-labs/cma-chat-sdk

- Ngày lập: 2026-11-28
- URL: https://github.com/vercel-labs/cma-chat-sdk
- Nguồn: trang repo và README. Chưa đọc: `.env.example`, `AGENTS.md`, `CLAUDE.md`, `package.json`, mã nguồn. **[chưa xác minh]** là chưa đọc được từ nguồn.
- Liên quan: repo này được README của `managed-agents/chat-sdk` (trong `claude-quickstarts`) nhắc tới như mẫu Slack.

## Tổng quan

| Mục | Nội dung |
|---|---|
| Mô tả | About: "Build with Claude Managed Agents and Chat SDK". Topics: chat-sdk, claude, vercel. Nhãn "Public template" |
| Mục đích | Mẫu bot Slack: "nhà phân tích nghiên cứu Claude Managed Agents". Nhắc bot trong kênh hoặc nhắn riêng, bot tìm và đọc nguồn trong sandbox do Anthropic quản lý rồi phát bản tóm tắt vào thread. Mỗi thread Slack ứng với một phiên Managed Agents bền vững |
| Giấy phép | **[chưa xác minh]** (README không nêu) |
| Ngôn ngữ | Không nêu; ngăn xếp TypeScript/Next.js |
| Thống kê | 5 sao, 1 theo dõi, 1 fork, 1 commit. Ngày commit cuối, issue, PR **[chưa xác minh]**; chỉ cộng tác viên mới tạo PR được |
| Đóng góp | Không nêu |
| Cảnh báo thử nghiệm | Không có rõ ràng, chỉ nhãn "Public template" |

## Ngăn xếp

Slack qua Chat SDK (chat-sdk.dev) và Vercel Connect; agent là Claude Managed Agents dùng "Claude Sonnet 5"; trạng thái lưu ở Upstash Redis (Vercel Marketplace); Next.js 16 trên Vercel; trình quản lý gói pnpm.

## Cấu trúc

Gốc: `scripts/cma/`, `src/`, `.env.example`, `.nvmrc`, `AGENTS.md`, `CLAUDE.md`, `README.md`, `biome.jsonc`, `knip.json`, `next.config.ts`, `package.json`, `pnpm-lock.yaml`, `pnpm-workspace.yaml`, `tsconfig.json`. File chính theo README: `src/lib/bot.ts`, `research-handler.ts`, `managed-agents.ts`, `config.ts`, `debug-card.tsx`, `src/app/api/webhooks/[platform]/route.ts`, `scripts/cma/cli.ts`, `scripts/cma/lib/agent.ts` (model, system prompt, tool posture), `setup.ts`, `update.ts`, `archive.ts`.

## Yêu cầu

README: Node.js 24+, khóa API Anthropic có quyền Managed Agents, dự án Vercel, Redis. Slack nối qua Vercel Connect; README không mô tả bước tạo ứng dụng Slack riêng.

## Cài đặt và triển khai (nguyên văn README)

```bash
git clone https://github.com/vercel-labs/claude-research-bot
cd claude-research-bot
pnpm install
vercel link
vercel connect create slack --name claude-research-bot --triggers
vercel connect attach slack/claude-research-bot \
  --project YOUR_VERCEL_PROJECT \
  --environment production \
  --triggers \
  --trigger-path /api/webhooks/slack
vercel integration add upstash/upstash-kv
npm run cma:setup -- --vercel
vercel env add ANTHROPIC_API_KEY
vercel deploy --prod
```

Thêm `ANTHROPIC_API_KEY` vào `.env.local` trước khi chạy `cma:setup`. Mời bot vào kênh hoặc nhắn riêng. Trong thread chỉ có một người thì không cần @mention; nhiều người thì bot chỉ trả lời khi được nhắc.

**Điểm không khớp:** URL clone và tên Vercel Connect dùng `claude-research-bot`, trong khi repo là `cma-chat-sdk`. Chưa kiểm tra repo `vercel-labs/claude-research-bot` có tồn tại không, nên làm theo lệnh clone nguyên văn có thể lỗi; thử clone chính repo `cma-chat-sdk`.

## Biến môi trường

- `ANTHROPIC_API_KEY` (bắt buộc): xác thực Managed Agents.
- `CLAUDE_AGENT_ID` (bắt buộc): analyst bền vững do `cma:setup` tạo.
- `CLAUDE_ENVIRONMENT_ID` (bắt buộc): sandbox do setup tạo.
- `REDIS_URL` (bắt buộc): đăng ký, chống trùng, ánh xạ thread/phiên.
- `SLACK_CONNECTOR` (bắt buộc): UID của Slack connector trên Vercel Connect.
- `BOT_USERNAME` (tùy chọn, mặc định `claude-research-bot`).
- `CLAUDE_DEBUG_MODE` (tùy chọn, mặc định `false`): chẩn đoán theo lượt.

Lệnh khác: `npm run cma:update` (đẩy thay đổi prompt/model thành phiên bản agent mới); `npm run cma:archive` (vĩnh viễn, README bảo kiểm tra ID trước).

## Bảo mật

README: Bash bị tắt cho analyst vì nó đọc trang web không tin cậy; nếu Bash tự động duyệt và mạng mở thì trang độc hại có thể lừa nó gửi dữ liệu hội thoại ra ngoài. Phiên được ghim vào phiên bản agent đã tạo ra nó, nên thử thay đổi prompt trong thread mới.

## Chi phí

Không nêu. Chế độ gỡ lỗi báo token và cache prompt nhưng không có giá của Anthropic, Vercel hay Upstash.

## Đánh giá

- **Phù hợp:** nhóm đã dùng Vercel và Anthropic muốn bot nghiên cứu trên Slack có nhớ theo thread. Gắn chặt với Vercel Connect và Upstash.
- **Lưu ý:** repo rất mới (5 sao, 1 commit), chưa rõ giấy phép nên chưa chắc được phép tái sử dụng.
- **Chưa xác minh:** giấy phép, ngày commit cuối, mã nguồn, tính hợp lệ của repo `claude-research-bot` trong lệnh clone, chi phí.
