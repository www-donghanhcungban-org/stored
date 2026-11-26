<!-- File sinh tự động bởi scripts/build_catalog_views.py; sửa data/projects.json hoặc data/taxonomy.json rồi chạy lại. -->

# policy-as-code — Đánh giá, an toàn & chất lượng

[← Mục lục catalog](../README.md) · 11 hồ sơ.

| Dự án | Repo | License | ★ | Bằng chứng | Mục | Tóm tắt |
|---|---|---|---|---|---|---|
| [Open Policy Agent (OPA)](../../09-engineering-checklists/README.md#nt-open-policy-agent-opa) | `open-policy-agent/opa` | Apache-2.0 | 12.511 | đọc mã 2026-11-23 | 09 | Công cụ quyết định chính sách đa dụng của CNCF (graduated): viết luật bằng Rego, chạy bằng CLI, server REST, thư viện Go hoặc WASM, đóng gói thành bundle. |
| [syft](../../12-ai-security-guardrails/README.md#ch-syft) | `anchore/syft` | Apache-2.0 | 9.956 | đọc tài liệu 2026-11-23 | 12 | Sinh SBOM (CycloneDX/SPDX). |
| [Kyverno](../../31-software-supply-chain-security/README.md#n2-kyverno) | `kyverno/kyverno` | Apache-2.0 | 8.375 | đọc mã 2026-11-23 | 31 | Policy engine Kubernetes đã chuyển sang chính sách CEL với `ImageValidatingPolicy` kiểm chữ ký và attestation. |
| [Agent Governance Toolkit](../../12-ai-security-guardrails/README.md#ch-agent-governance-toolkit) | `microsoft/agent-governance-toolkit` | MIT | 6.599 | đọc tài liệu 2026-11-23 | 12 | Kernel chính sách tất định chặn tool call, danh tính agent, audit; |
| [OPAL (Open Policy Administration Layer)](../../34-backend-data-identity-integration/README.md#n2-opal) | `permitio/opal` | Apache-2.0 | 5.527 | đọc mã 2026-11-23 | 34 | Lớp quản trị cho policy engine (OPA, Cedar Agent): server theo dõi kho git, webhook và nguồn dữ liệu, đẩy thay đổi chính sách và dữ liệu xuống các client cạnh ứng dụng q… |
| [Cerbos](../../12-ai-security-guardrails/README.md#nt-cerbos) | `cerbos/cerbos` | Apache-2.0 | 4.668 | đọc mã 2026-11-23 | 12 | Cerbos là PDP (điểm quyết định phân quyền) tự host, chính sách YAML kiểu RBAC/ABAC với điều kiện CEL, gọi qua CheckResources và PlanResources. |
| [OPA Gatekeeper](../../32-platform-delivery-engineering/README.md#n2-gatekeeper) | `open-policy-agent/gatekeeper` | Apache-2.0 | 4.302 | đọc mã 2026-11-23 | 32 | Admission controller Kubernetes dùng Rego qua template và constraint, kèm audit và CLI `gator`. |
| [OPA / conftest](../../12-ai-security-guardrails/README.md#ch-opa-conftest) | `open-policy-agent/conftest` | Apache-2.0 | 3.299 | đọc tài liệu 2026-11-23 | 12 | Policy-as-code (Rego) chặn PR vi phạm trong CI; |
| [Cedar](../../12-ai-security-guardrails/README.md#cedar) | `cedar-policy/cedar` | Apache-2.0 | 1.833 | đọc mã 2026-11-02 | 12 | Ngôn ngữ/engine authz Rust; |
| [Allstar](../../31-software-supply-chain-security/README.md#n2-allstar) | `ossf/allstar` | Apache-2.0 | 1.467 | đọc mã 2026-11-23 | 31 | Bộ thực thi chính sách bảo mật repo GitHub theo tổ chức, mở issue hoặc tự sửa cài đặt. |
| [AWS CloudFormation Guard](../../13-dev-stack-devops/README.md#n2-cloudformation-guard) | `aws-cloudformation/cloudformation-guard` | Apache-2.0 | 1.396 | đọc mã 2026-11-23 | 13 | Guard là DSL policy-as-code có mục đích chung: viết luật khai báo để kiểm JSON/YAML (CloudFormation, Terraform plan JSON, Kubernetes, AWS Config) bằng `cfn-guard validat… |
