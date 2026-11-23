<!-- File sinh tự động bởi scripts/build_catalog_views.py; sửa data/projects.json hoặc data/taxonomy.json rồi chạy lại. -->

# security — Đánh giá, an toàn & chất lượng

[← Mục lục catalog](../README.md) · 63 hồ sơ.

## Quét lỗ hổng ứng dụng (`appsec-scanner`, 5)

| Dự án | Repo | License | ★ | Bằng chứng | Mục | Tóm tắt |
|---|---|---|---|---|---|---|
| [security-audit-skill (Cloudflare)](../../20-claude-plugins-ecosystem/README.md#3zc-kiểm-bài-5-repo-skill-đáng-lưu-matt-pocock-addy-osmani-cloudflare-obsidian-google-egm-bài-người-dùng-gửi-đọc-mã-16112026) | `cloudflare/security-audit-skill` | MIT | 73.608 | đọc tài liệu 2026-11-16 | 12 | Skill audit bảo mật 1 repo, 6 pha (recon → hunt theo coverage ledger → verifier mới bác bỏ → findings.json theo schema → kiểm lại → báo cáo); |
| [magika](../../12-ai-security-guardrails/README.md#chuyen-magika) | `google/magika` | Apache-2.0 | 18.831 | đọc tài liệu 2026-11-18 | 12 | Công cụ nhận diện loại tệp bằng mô hình học sâu nhỏ gọn, có CLI viết bằng Rust và thư viện Python, JavaScript, Rust, Go. |
| [Semgrep](../../12-ai-security-guardrails/README.md#ch-semgrep) | `semgrep/semgrep` | LGPL-2.1 | 17.385 | đọc tài liệu 2026-11-23 | 12 | SAST; |
| [Trail of Bits skills](../../12-ai-security-guardrails/README.md#ch-trail-of-bits-skills) | `trailofbits/skills` | CC-BY-SA-4.0 | 7.918 | đọc tài liệu 2026-11-23 | 12 | Marketplace 44 plugin; |
| [claude-code-security-review](../../12-ai-security-guardrails/README.md#ch-claude-code-security-review) | `anthropics/claude-code-security-review` | MIT | 6.660 | đọc tài liệu 2026-11-23 | 12 | Action + /security-review; |

## Guardrail & an toàn agent (`agent-guardrails`, 13)

| Dự án | Repo | License | ★ | Bằng chứng | Mục | Tóm tắt |
|---|---|---|---|---|---|---|
| [SkillSpector](../../12-ai-security-guardrails/README.md#ch-skillspector) | `NVIDIA/SkillSpector` | Apache-2.0 | 23.695 | đọc tài liệu 2026-11-23 | 12 | Quét skill tĩnh + LLM (71 pattern/17 nhóm), thuộc NVIDIA Verified Skills pipeline → NVIDIA skills catalog; |
| [Guardrails AI](../../12-ai-security-guardrails/README.md#ch-guardrails-ai) | `guardrails-ai/guardrails` | Apache-2.0 | 7.579 | đọc tài liệu 2026-11-23 | 12 | Validator output; |
| [NeMo Guardrails](../../12-ai-security-guardrails/README.md#ch-nemo-guardrails) | `NVIDIA-NeMo/Guardrails` | Apache-2.0 | 7.413 | đọc tài liệu 2026-11-23 | 12 | Colang rails; |
| [dcg (Destructive Command Guard)](../../12-ai-security-guardrails/README.md#ch-dcg-destructive-command-guard) | `Dicklesworthstone/destructive_command_guard` | MIT kèm rider cấm OpenAI/Anthropic (không OSI) | 6.235 | đọc tài liệu 2026-11-23 | 12 | Hook Rust chặn lệnh phá huỷ cho 6+ coding agent; |
| [PurpleLlama](../../12-ai-security-guardrails/README.md#ch-purplellama) | `meta-llama/PurpleLlama` | MIT (CodeShield, CyberSecEval, LlamaFirewall, SensitiveDocCl | 4.457 | đọc tài liệu 2026-11-23 | 12 | Llama Guard (4, 12B, phân loại 14 nhóm MLCommons), Prompt Guard 2 (injection/jailbreak), LlamaFirewall, CodeShield, CyberSecEval; |
| [agent-scan](../../12-ai-security-guardrails/README.md#ch-agent-scan) | `snyk/agent-scan` | Apache-2.0 | 3.274 | đọc tài liệu 2026-11-23 | 12 | Trước là mcp-scan; |
| [skill-scanner (Cisco)](../../12-ai-security-guardrails/README.md#ch-skill-scanner-cisco) | `cisco-ai-defense/skill-scanner` | Apache-2.0 | 2.674 | đọc tài liệu 2026-11-23 | 12 | Quét skill best-effort; |
| [Cisco MCP Scanner](../../04-protocols-standards/README.md#ch-cisco-mcp-scanner) | `cisco-ai-defense/mcp-scanner` | Apache-2.0 | 1.127 | đọc tài liệu 2026-11-23 | 04 | Quét tool MCP bằng YARA, LLM judge, API Cisco AI Defense, readiness tĩnh; |
| [AgentDojo](../../11-browser-computer-use-sandbox/README.md#ch-agentdojo) | `ethz-spylab/agentdojo` | MIT | 1.069 | đọc tài liệu 2026-11-23 | 11 | Đo utility + tỷ lệ tấn công prompt injection thành công trên 4 suite (workspace, slack, travel, banking), registry tấn công và phòng thủ (tool_filter, detector); |
| [Open-Prompt-Injection](../../17-prompt-engineering/README.md) | `liu00222/Open-Prompt-Injection` | MIT | 510 | chưa chuẩn hóa | 17 | Benchmark tấn công/phòng thủ prompt injection, đo ASV, detector DataSentinel, PromptLocate (checkpoint Google Drive); |
| [YesWeHack claude-kit](../../12-ai-security-guardrails/README.md#ch-yeswehack-claude-kit) | `yeswehack/claude-kit` | GPL-3.0 | 357 | đọc tài liệu 2026-11-23 | 12 | Plugin Claude Code chính chủ YesWeHack: luật luôn bật qua hook SessionStart (chỉ cat file) + skill write/triage/gotchas (14 lớp lỗi) để báo cáo bug bounty chỉ từ bằng ch… |
| [LLM Guard](../../12-ai-security-guardrails/README.md#ch-llm-guard) | `protectai/llm-guard` | MIT | — | đọc tài liệu 2026-11-23 | 12 | ~35 scanner; |
| [OWASP MCP Top 10](../../12-ai-security-guardrails/README.md#ch-owasp-mcp-top-10) | `OWASP/www-project-mcp-top-10` | CC-BY-SA-4.0 | — | đọc tài liệu 2026-11-23 | 12 | . |

## Secret & chuỗi cung ứng (`secrets-supply-chain`, 17)

| Dự án | Repo | License | ★ | Bằng chứng | Mục | Tóm tắt |
|---|---|---|---|---|---|---|
| [Trivy](../../12-ai-security-guardrails/README.md#ch-trivy) | `aquasecurity/trivy` | Apache-2.0 | 38.881 | đọc tài liệu 2026-11-23 | 12 | Bị xâm nhập 3/2026 (CVE-2026-33634): ghim Action theo SHA; |
| [infisical](../../31-software-supply-chain-security/README.md#chuyen-infisical) | `Infisical/infisical` | MIT | 30.570 | đọc tài liệu 2026-11-18 | 31 | Nền tảng hạ tầng bảo mật mã nguồn mở để quản lý bí mật, chứng chỉ, khoá, truy cập đặc quyền và truy cập của AI agent; |
| [SOPS](../../31-software-supply-chain-security/README.md#anhkysuai-getsops-sops) | `getsops/sops` | MPL-2.0 | 23.807 | đọc tài liệu 2026-11-23 | 31 | Công cụ sửa tệp bí mật đã mã hóa theo YAML, JSON, ENV, INI hoặc binary. |
| [Grype](../../13-dev-stack-devops/README.md#ch-grype) | `anchore/grype` | Apache-2.0 | 13.159 | đọc tài liệu 2026-11-23 | 13 | Quét lỗ hổng image/filesystem/SBOM syft, ưu tiên EPSS/KEV, OpenVEX; |
| [OSV-Scanner](../../12-ai-security-guardrails/README.md#ch-osv-scanner) | `google/osv-scanner` | Apache-2.0 | 11.342 | đọc tài liệu 2026-11-23 | 12 | Quét dependency/container theo OSV.dev; |
| [cosign](../../12-ai-security-guardrails/README.md#ch-cosign) | `sigstore/cosign` | Apache-2.0 | 6.403 | đọc tài liệu 2026-11-23 | 12 | Ký keyless Fulcio/Rekor; |
| [OpenSSF Scorecard](../../12-ai-security-guardrails/README.md#ch-openssf-scorecard) | `ossf/scorecard` | Apache-2.0 | 5.801 | đọc tài liệu 2026-11-23 | 12 | Điểm sức khoẻ bảo mật repo (heuristic); |
| [Bumblebee (Perplexity)](../../12-ai-security-guardrails/README.md#ch-bumblebee-perplexity) | `perplexityai/bumblebee` | Apache-2.0 | 5.169 | đọc tài liệu 2026-11-23 | 12 | Trình quét chỉ đọc (Go, không dependency ngoài stdlib) lockfile, metadata package manager, extension, cấu hình MCP trên máy dev macOS/Linux để đối chiếu advisory chuỗi c… |
| [Varlock](../../12-ai-security-guardrails/README.md#ch-varlock) | `dmno-dev/varlock` | MIT | 4.874 | đọc tài liệu 2026-11-23 | 12 | .env.schema cho agent đọc schema không đọc secret, quét rò rỉ, che log, plugin 1Password/Vault/cloud; |
| [ModelScan](../../12-ai-security-guardrails/README.md#ch-modelscan) | `protectai/modelscan` | Apache-2.0 | 792 | đọc tài liệu 2026-11-23 | 12 | Quét file model (pickle, H5, Keras, SavedModel); |
| [fickling](../../12-ai-security-guardrails/README.md#ch-fickling) | `trailofbits/fickling` | LGPL-3.0 | 676 | đọc tài liệu 2026-11-23 | 12 | Trail of Bits: phân tích pickle, hook allowlist import ML khi load; |
| [model-signing (Model Transparency)](../../12-ai-security-guardrails/README.md#ch-model-signing-model-transparency) | `sigstore/model-transparency` | Apache-2.0 | 249 | đọc tài liệu 2026-11-23 | 12 | Ký/xác minh thư mục model bằng Sigstore/khoá/PKCS#11, DSSE + in-toto; |
| [gitleaks](../../12-ai-security-guardrails/README.md#ch-gitleaks) | `gitleaks/gitleaks` | MIT | — | đọc tài liệu 2026-11-23 | 12 | secret scan. |
| [GUAC](../../31-software-supply-chain-security/README.md#factory-2026-11-04-guac) | `guacsec/guac` | Apache-2.0 | — | đọc mã 2026-11-04 | 31 | Đồ thị metadata chuỗi cung ứng; |
| [in-toto](../../31-software-supply-chain-security/README.md#factory-2026-11-04-in-toto) | `in-toto/in-toto` | Apache-2.0 | — | đọc mã 2026-11-04 | 31 | Layout/link ký số và rules chuỗi cung ứng; |
| [OWASP Dependency-Track](../../31-software-supply-chain-security/README.md#factory-2026-11-04-owasp-dependency-track) | `DependencyTrack/dependency-track` | Apache-2.0 | — | đọc mã 2026-11-04 | 31 | Quản trị rủi ro component theo SBOM, phân tích bất đồng bộ; |
| [trufflehog](../../12-ai-security-guardrails/README.md#ch-trufflehog) | `trufflesecurity/trufflehog` | AGPL-3.0 | — | đọc tài liệu 2026-11-23 | 12 | secret scan. |

## Pentest & red team (`offensive-redteam`, 17)

| Dự án | Repo | License | ★ | Bằng chứng | Mục | Tóm tắt |
|---|---|---|---|---|---|---|
| [sherlock](../../12-ai-security-guardrails/README.md#chuyen-sherlock) | `sherlock-project/sherlock` | MIT | 113.816 | đọc tài liệu 2026-11-18 | 12 | Công cụ dòng lệnh tìm tài khoản mạng xã hội theo tên người dùng trên hơn 400 trang. |
| [PayloadsAllTheThings](../../08-awesome-lists-learning/README.md#6c53-bảo-mật--hack) | `swisskyrepo/PayloadsAllTheThings` | MIT | 82.743 | đọc tài liệu 2026-11-18 | 08 | Bộ tài liệu payload và kỹ thuật bypass cho bảo mật ứng dụng web, chia theo từng loại lỗ hổng. |
| [SecLists](../../08-awesome-lists-learning/README.md#6c53-bảo-mật--hack) | `danielmiessler/SecLists` | MIT | 74.821 | đọc tài liệu 2026-11-18 | 08 | Tập hợp các loại danh sách dùng khi đánh giá bảo mật: username, mật khẩu, URL, mẫu dữ liệu nhạy cảm, payload fuzzing, web shell. |
| [Strix](../../12-ai-security-guardrails/README.md#ch-strix) | `usestrix/strix` | Apache-2.0 | 73.091 | đọc tài liệu 2026-11-23 | 12 | Agent pentest tự chủ trong container Kali (dual-use); |
| [Anthropic-Cybersecurity-Skills (cộng đồng)](../../12-ai-security-guardrails/README.md#ch-anthropic-cybersecurity-skills-cong-ong) | `mukul975/Anthropic-Cybersecurity-Skills` | Apache-2.0 | 36.623 | đọc tài liệu 2026-11-23 | 12 | ~817 skill; |
| [PentAGI](../../12-ai-security-guardrails/README.md#ch-pentagi) | `vxcontrol/pentagi` | MIT (kèm EULA) | 32.865 | đọc tài liệu 2026-11-23 | 12 | 13/10/2026; |
| [HexStrike AI](../../12-ai-security-guardrails/README.md#ch-hexstrike-ai) | `0x4m4/hexstrike-ai` | MIT | 13.246 | đọc tài liệu 2026-11-23 | 12 | MCP gói 150+ công cụ pentest; |
| [claude-red](../../12-ai-security-guardrails/README.md#ch-claude-red) | `SnailSploit/claude-red` | MIT | 10.086 | đọc tài liệu 2026-11-23 | 12 | 78 SKILL.md red-team cho Claude (dual-use); |
| [garak](../../12-ai-security-guardrails/README.md#factory-2026-11-04-garak) | `NVIDIA/garak` | Apache-2.0 | 9.814 | đọc mã 2026-11-04 | 12 | Máy quét lỗ hổng LLM của NVIDIA; |
| [A.I.G (AI-Infra-Guard)](../../12-ai-security-guardrails/README.md#ch-a-i-g-ai-infra-guard) | `Tencent/AI-Infra-Guard` | Apache-2.0 | 7.622 | đọc tài liệu 2026-11-23 | 12 | Nền tảng red team AI của Tencent Zhuque Lab: quét hạ tầng AI, MCP, skill, agent, jailbreak; |
| [Decepticon](../../12-ai-security-guardrails/README.md#ch-decepticon) | `BitterSecurity/Decepticon` | Apache-2.0 | 6.500 | đọc tài liệu 2026-11-23 | 12 | Agent red team tự chủ (LangGraph, 16 agent, Kali sandbox, Sliver C2, Neo4j KG); |
| [Claude-BugHunter](../../12-ai-security-guardrails/README.md#ch-claude-bughunter) | `elementalsouls/Claude-BugHunter` | MIT (mã) + CC-BY-4.0 (nội dung) | 5.360 | đọc tài liệu 2026-11-23 | 12 | Clone đầy đủ 17/10/2026 (HEAD 35e7614): 83 skill (58 hunt-\*) + 15 command, dual-use săn lỗi/red-team; |
| [PyRIT](../../12-ai-security-guardrails/README.md#ch-pyrit) | `microsoft/PyRIT` | MIT | 4.718 | đọc tài liệu 2026-11-23 | 12 | Red-team AI tạo sinh; |
| [DeepTeam](../../17-prompt-engineering/README.md) | `confident-ai/deepteam` | Apache-2.0 | 3.079 | chưa chuẩn hóa | 17 | Red-team LLM/agent 50+ lỗ hổng; |
| [MITRE ATLAS Data](../../12-ai-security-guardrails/README.md#ch-mitre-atlas-data) | `mitre-atlas/atlas-data` | Apache-2.0 | 203 | đọc tài liệu 2026-11-23 | 12 | Dữ liệu ATLAS YAML phát hành hằng tháng (2026.10: 16 tactic, 129 technique, 77 case study); |
| [ARTEX](../../12-ai-security-guardrails/README.md) | `Autumn-27/ARTEX` | AGPL-3.0 | — | chưa chuẩn hóa | 12 | Agent pentest tự chủ (Go+Next.js); |
| [Claude-Red (fork)](../../23-own-repos-lessons/README.md) | `www-donghanhcungban-org/Claude-Red` | MIT | — | chưa chuẩn hóa | 23 | Fork SnailSploit/claude-red v0.3.0: 78 SKILL.md red-team dual-use, manifest claude-skills.json; |

## Danh tính & truy cập (`identity-access`, 7)

| Dự án | Repo | License | ★ | Bằng chứng | Mục | Tóm tắt |
|---|---|---|---|---|---|---|
| [jumpserver](../../34-backend-data-identity-integration/README.md#chuyen-jumpserver) | `jumpserver/jumpserver` | GPL-3.0 | 31.982 | đọc tài liệu 2026-11-18 | 34 | Nền tảng quản lý truy cập đặc quyền (PAM/bastion host) mã nguồn mở, có tính năng AI, cho phép truy cập an toàn tới SSH, RDP, Kubernetes, cơ sở dữ liệu, website, RemoteAp… |
| [hydra](../../34-backend-data-identity-integration/README.md#chuyen-hydra) | `ory/hydra` | Apache License 2.0 | 17.671 | đọc tài liệu 2026-11-18 | 34 | Máy chủ OAuth 2.0 và nhà cung cấp OpenID Connect, kết nối với hệ thống định danh sẵn có qua ứng dụng login và consent riêng. |
| [casdoor](../../34-backend-data-identity-integration/README.md#chuyen-casdoor) | `casdoor/casdoor` | Apache License 2.0 | 14.881 | đọc tài liệu 2026-11-18 | 34 | Máy chủ đăng nhập một lần (SSO) và xác thực có bảng điều khiển web, là nhà cung cấp định danh đầy đủ lưu người dùng và cấp token. |
| [SpiceDB](../../12-ai-security-guardrails/README.md#spicedb) | `authzed/spicedb` | Apache-2.0 | 7.185 | đọc mã 2026-11-02 | 12 | Zanzibar/ReBAC; |
| [OpenFGA](../../12-ai-security-guardrails/README.md#openfga) | `openfga/openfga` | Apache-2.0 | 6.077 | đọc mã 2026-11-02 | 12 | ReBAC HTTP/gRPC; |
| [SPIRE](../../12-ai-security-guardrails/README.md#spire) | `spiffe/spire` | Apache-2.0 | 2.602 | đọc mã 2026-11-02 | 12 | Workload identity SPIFFE/SVID; |
| [Keycloak](../../34-backend-data-identity-integration/README.md#keycloak) | `keycloak/keycloak` | Apache-2.0 | — | đọc mã 2026-11-04 | 34 | OIDC/SSO; |

## Quyền riêng tư (`privacy`, 4)

| Dự án | Repo | License | ★ | Bằng chứng | Mục | Tóm tắt |
|---|---|---|---|---|---|---|
| [uBlock](../../35-desktop-productivity-apps/README.md#anhkysuai-2026-11-23-gorhill-ublock) | `gorhill/uBlock` | GPL-3.0 | 69.588 | đọc tài liệu 2026-11-23 | 35 | uBlock Origin: tiện ích trình duyệt chặn nội dung theo các bộ lọc và quy tắc. |
| [Presidio](../../12-ai-security-guardrails/README.md#4e-kiểm-infographic-5-vị-trí-cần-đặt-guardrails-trong-ai-agent-ảnh-người-dùng-gửi-2026-11-02) | `data-privacy-stack/presidio` | MIT | 11.631 | đọc tài liệu 2026-11-02 | 12 | Phát hiện và che PII (text, ảnh, dữ liệu có cấu trúc; |
| [VideoSeal](../../19-agentic-video-media/README.md) | `facebookresearch/videoseal` | MIT | 817 | chưa chuẩn hóa | 19 | Watermark ẩn ảnh/video (VideoSeal, PixelSeal, ChunkySeal) + WmForger thử tấn công; |
| [AudioSeal](../../14-voice-multimodal/README.md#ch-audioseal) | `facebookresearch/audioseal` | MIT | 802 | đọc tài liệu 2026-11-23 | 14 | Watermark âm thanh định vị theo đoạn, streaming từ v0.2; |
