<!-- File sinh tự động bởi scripts/build_catalog_views.py; sửa data/projects.json hoặc data/taxonomy.json rồi chạy lại. -->

# devops — Kỹ thuật phần mềm & vận hành

[← Mục lục catalog](../README.md) · 162 hồ sơ.

## Container & Kubernetes (`container-orchestration`, 17)

| Dự án | Repo | License | ★ | Bằng chứng | Mục | Tóm tắt |
|---|---|---|---|---|---|---|
| [moby](../../32-platform-delivery-engineering/README.md#chuyen-moby) | `moby/moby` | Apache License 2.0 | 72.275 | đọc tài liệu 2026-11-18 | 32 | Dự án mã nguồn mở do Docker tạo, cung cấp bộ thành phần để lắp ráp hệ thống container; |
| [dive](../../32-platform-delivery-engineering/README.md#anhkysuai-wagoodman-dive) | `wagoodman/dive` | MIT | 54.755 | đọc tài liệu 2026-11-23 | 32 | Xem layer Docker/OCI image và tìm dung lượng bị lãng phí. |
| [Docker Compose](../../32-platform-delivery-engineering/README.md#anhkysuai-docker-compose) | `docker/compose` | Apache-2.0 | 39.135 | đọc tài liệu 2026-11-23 | 32 | CLI định nghĩa và chạy ứng dụng nhiều container bằng Compose file. |
| [K9s](../../33-reliability-observability-operations/README.md#anhkysuai-derailed-k9s) | `derailed/k9s` | Apache-2.0 | 35.035 | đọc tài liệu 2026-11-23 | 33 | Giao diện terminal để quan sát và thao tác tài nguyên Kubernetes. |
| [K3s](../../32-platform-delivery-engineering/README.md#anhkysuai-k3s-io-k3s) | `k3s-io/k3s` | Apache-2.0; thành phần đi kèm có thông báo riêng | 34.499 | đọc tài liệu 2026-11-23 | 32 | Bản phân phối Kubernetes gọn để triển khai edge, dev và cụm nhỏ. |
| [Podman](../../32-platform-delivery-engineering/README.md#anhkysuai-podman-container-tools-podman) | `podman-container-tools/podman` | Apache-2.0 | 33.363 | đọc tài liệu 2026-11-23 | 32 | Công cụ quản lý OCI container, image, volume và pod, gồm thư viện libpod. |
| [minikube](../../32-platform-delivery-engineering/README.md#anhkysuai-kubernetes-minikube) | `kubernetes/minikube` | Apache-2.0 | 32.261 | đọc tài liệu 2026-11-23 | 32 | Công cụ chạy cluster Kubernetes cục bộ trên macOS, Linux và Windows. |
| [Colima](../../32-platform-delivery-engineering/README.md#anhkysuai-abiosoft-colima) | `abiosoft/colima` | MIT | 31.797 | đọc tài liệu 2026-11-23 | 32 | CLI tạo môi trường container trên macOS/Linux với Docker, containerd hoặc Incus. |
| [Helm](../../32-platform-delivery-engineering/README.md#anhkysuai-helm-helm) | `helm/helm` | Apache-2.0 | 30.466 | đọc tài liệu 2026-11-23 | 32 | Trình quản lý gói Kubernetes dùng chart và template tài nguyên. |
| [OpenFaaS](../../32-platform-delivery-engineering/README.md#anhkysuai-openfaas-faas) | `openfaas/faas` | OpenFaaS CE EULA; đóng góp bên thứ ba theo MIT | 26.268 | đọc tài liệu 2026-11-23 | 32 | Nền tảng chạy function và microservice đóng gói OCI trên Kubernetes. |
| [Rancher](../../32-platform-delivery-engineering/README.md#anhkysuai-rancher-rancher) | `rancher/rancher` | Apache-2.0 | 26.079 | đọc tài liệu 2026-11-23 | 32 | Nền tảng quản lý môi trường Kubernetes và container cho tổ chức. |
| [SlimToolkit](../../32-platform-delivery-engineering/README.md#anhkysuai-slimtoolkit-slim) | `slimtoolkit/slim` | Apache-2.0 | 23.547 | đọc tài liệu 2026-11-23 | 32 | Bộ công cụ xem, tối ưu và debug container, trước đây tên DockerSlim. |
| [Distroless](../../32-platform-delivery-engineering/README.md#anhkysuai-googlecontainertools-distroless) | `GoogleContainerTools/distroless` | Apache-2.0 cho repo; package trong image theo giấy phép tương ứng | 23.297 | đọc tài liệu 2026-11-23 | 32 | Bộ image runtime container chỉ giữ ứng dụng và dependency cần thiết. |
| [containerd](../../32-platform-delivery-engineering/README.md#anhkysuai-containerd-containerd) | `containerd/containerd` | Apache-2.0 | 21.527 | đọc tài liệu 2026-11-23 | 32 | Runtime daemon quản lý image và vòng đời container trên Linux/Windows. |
| [kubectx và kubens](../../32-platform-delivery-engineering/README.md#anhkysuai-ahmetb-kubectx) | `ahmetb/kubectx` | Apache-2.0 | 20.130 | đọc tài liệu 2026-11-23 | 32 | CLI chuyển context/namespace Kubernetes nhanh, có tích hợp tìm kiếm tương tác. |
| [kubesphere](../../32-platform-delivery-engineering/README.md#chuyen-kubesphere) | `kubesphere/kubesphere` | Apache License 2.0 kèm điều kiện bổ sung | 17.083 | đọc tài liệu 2026-11-18 | 32 | Nền tảng container đa thuê bao dùng Kubernetes làm nhân, quản lý ứng dụng cloud-native đa cụm, datacenter và biên qua giao diện web, có kiến trúc mở rộng bằng plugin. |
| [Kubernetes](../../13-dev-stack-devops/README.md#ch-kubernetes) | `kubernetes/kubernetes` | Apache-2.0 | — | đọc tài liệu 2026-11-23 | 13 | . |

## IaC & quản lý cấu hình (`iac-config`, 5)

| Dự án | Repo | License | ★ | Bằng chứng | Mục | Tóm tắt |
|---|---|---|---|---|---|---|
| [ansible](../../32-platform-delivery-engineering/README.md#chuyen-ansible) | `ansible/ansible` | GNU General Public License v3.0 | 71.623 | đọc tài liệu 2026-11-18 | 32 | Hệ thống tự động hoá hạ tầng IT (ansible-core): quản lý cấu hình, triển khai ứng dụng, cấp phát cloud, thực thi tác vụ ad-hoc và tự động hoá mạng. |
| [nacos](../../34-backend-data-identity-integration/README.md#chuyen-nacos) | `alibaba/nacos` | Apache License 2.0 | 33.525 | đọc tài liệu 2026-11-18 | 34 | Nền tảng khám phá dịch vụ, quản lý cấu hình động và quản lý dịch vụ cho ứng dụng cloud-native và microservice. |
| [Pulumi](../../32-platform-delivery-engineering/README.md#anhkysuai-pulumi-pulumi) | `pulumi/pulumi` | Apache-2.0 | 25.939 | đọc tài liệu 2026-11-23 | 32 | Infrastructure as Code dùng ngôn ngữ lập trình thông thường và Automation API. |
| [OpenTofu](../../32-platform-delivery-engineering/README.md#factory-opentofu-2026-11-04) | `opentofu/opentofu` | MPL-2.0 | — | đọc mã 2026-11-04 | 13 | Fork Terraform Đọc sâu 4/11/2026: plan detailed-exitcode 0=no diff/1=error/2=changes; |
| [Terraform](../../13-dev-stack-devops/README.md#ch-terraform) | `hashicorp/terraform` | BSL-1.1 (Business Source License 1.1, licensor IBM) | — | đọc tài liệu 2026-11-23 | 13 | . |

## CI/CD & phát hành (`ci-cd-release`, 7)

| Dự án | Repo | License | ★ | Bằng chứng | Mục | Tóm tắt |
|---|---|---|---|---|---|---|
| [act](../../13-dev-stack-devops/README.md#ch-act) | `nektos/act` | MIT | 72.504 | đọc tài liệu 2026-11-23 | 13 | Chạy GitHub Actions cục bộ; |
| [Harness Open Source](../../32-platform-delivery-engineering/README.md#anhkysuai-harness-harness) | `harness/harness` | Apache-2.0 | 38.955 | đọc tài liệu 2026-11-23 | 32 | Nền tảng tự host code, pipeline DevOps, Gitspaces và artifact registry. |
| [Jenkins](../../32-platform-delivery-engineering/README.md#anhkysuai-jenkinsci-jenkins) | `jenkinsci/jenkins` | MIT | 26.804 | đọc tài liệu 2026-11-23 | 32 | Máy chủ tự động hóa build, kiểm thử và triển khai với hệ plugin. |
| [semantic-release](../../32-platform-delivery-engineering/README.md#anhkysuai-semantic-release-semantic-release) | `semantic-release/semantic-release` | MIT | 24.193 | đọc tài liệu 2026-11-23 | 32 | Tự động chọn version, tạo release notes và publish package theo commit. |
| [GoReleaser](../../13-dev-stack-devops/README.md#goreleaser) | `goreleaser/goreleaser` | MIT | 16.131 | đọc mã 2026-11-02 | 13 | Release pipeline đa nền tảng; |
| [Argo CD](../../32-platform-delivery-engineering/README.md#factory-argocd-2026-11-04) | `argoproj/argo-cd` | Apache-2.0 | — | đọc mã 2026-11-04 | 13 | CNCF graduated Đọc sâu 4/11/2026: Server.Rollback từ chối khi automated sync bật; |
| [Dagger](../../13-dev-stack-devops/README.md#ch-dagger) | `dagger/dagger` | Apache-2.0 | — | đọc tài liệu 2026-11-23 | 13 | . |

## PaaS tự host & bảng điều khiển server (`paas-self-hosting`, 7)

| Dự án | Repo | License | ★ | Bằng chứng | Mục | Tóm tắt |
|---|---|---|---|---|---|---|
| [Coolify](../../36-self-hosting-homelab/README.md#anhkysuai-coollabsio-coolify) | `coollabsio/coolify` | Apache-2.0 | 66.375 | đọc tài liệu 2026-11-23 | 36 | Nền tảng triển khai ứng dụng, cơ sở dữ liệu và dịch vụ trên máy chủ tự quản lý qua SSH. |
| [Portainer Community Edition](../../36-self-hosting-homelab/README.md#anhkysuai-portainer-portainer) | `portainer/portainer` | Zlib | 38.893 | đọc tài liệu 2026-11-23 | 36 | Giao diện quản lý container cho Docker, Swarm, Podman, Kubernetes và ACI. |
| [Dokploy](../../36-self-hosting-homelab/README.md#anhkysuai-dokploy-dokploy) | `Dokploy/dokploy` | Apache-2.0 ngoài proprietary; proprietary theo DSAL-1.0 | 38.652 | đọc tài liệu 2026-11-23 | 36 | PaaS tự host để triển khai ứng dụng, cơ sở dữ liệu và Docker Compose. |
| [1Panel](../../36-self-hosting-homelab/README.md#chuyen-1panel) | `1Panel-dev/1Panel` | GNU GPL v3 | 37.464 | đọc tài liệu 2026-11-18 | 36 | Bảng điều khiển quản trị máy chủ Linux qua web kèm nền tảng quản lý AI: giám sát, tệp, cơ sở dữ liệu, container, website, sao lưu. |
| [Dokku](../../36-self-hosting-homelab/README.md#anhkysuai-dokku-dokku) | `dokku/dokku` | MIT | 32.233 | đọc tài liệu 2026-11-23 | 36 | PaaS dùng Docker để quản lý vòng đời ứng dụng trên máy chủ tự quản. |
| [Dockge](../../36-self-hosting-homelab/README.md#anhkysuai-louislam-dockge) | `louislam/dockge` | MIT | 24.884 | đọc tài liệu 2026-11-23 | 36 | Giao diện quản lý các stack compose.yaml và nhiều Docker host. |
| [sealos](../../32-platform-delivery-engineering/README.md#chuyen-sealos) | `labring/sealos` | Sealos Sustainable Use License 1.0 | 18.398 | đọc tài liệu 2026-11-18 | 32 | Hệ điều hành cloud xây trên Kubernetes, gom cloud IDE (DevBox), cơ sở dữ liệu quản lý, object storage và app store để phát triển, triển khai và vận hành ứng dụng. |

## Mạng, proxy, DNS & chứng chỉ (`networking-proxy`, 8)

| Dự án | Repo | License | ★ | Bằng chứng | Mục | Tóm tắt |
|---|---|---|---|---|---|---|
| [caddy](../../32-platform-delivery-engineering/README.md#chuyen-caddy) | `caddyserver/caddy` | Apache License 2.0 | 79.146 | đọc tài liệu 2026-11-18 | 32 | Máy chủ web/nền tảng máy chủ mở rộng viết bằng Go, mặc định dùng TLS và tự động cấp chứng chỉ HTTPS. |
| [Traefik](../../32-platform-delivery-engineering/README.md#anhkysuai-traefik-traefik) | `traefik/traefik` | MIT | 65.663 | đọc tài liệu 2026-11-23 | 32 | Reverse proxy và ingress tự cập nhật định tuyến từ hệ điều phối dịch vụ. |
| [Pi-hole Core](../../36-self-hosting-homelab/README.md#anhkysuai-pi-hole-pi-hole) | `pi-hole/pi-hole` | EUPL-1.2 | 62.184 | đọc tài liệu 2026-11-23 | 36 | DNS sinkhole chặn tên miền không mong muốn cho cả mạng, có thể kiêm DHCP. |
| [acme.sh](../../32-platform-delivery-engineering/README.md#anhkysuai-acmesh-official-acme.sh) | `acmesh-official/acme.sh` | GPL-3.0 | 47.973 | đọc tài liệu 2026-11-23 | 32 | Client ACME bằng shell để cấp, gia hạn và cài chứng chỉ TLS. |
| [AdGuard Home](../../36-self-hosting-homelab/README.md#anhkysuai-adguardteam-adguardhome) | `AdguardTeam/AdGuardHome` | GPL-3.0 | 38.749 | đọc tài liệu 2026-11-23 | 36 | Máy chủ DNS tự host chặn tên miền quảng cáo và theo dõi trên mạng. |
| [Istio](../../32-platform-delivery-engineering/README.md#anhkysuai-istio-istio) | `istio/istio` | Apache-2.0 | 38.534 | đọc tài liệu 2026-11-23 | 32 | Service mesh bổ sung điều khiển lưu lượng, xác thực giữa dịch vụ và quan sát. |
| [Certbot](../../32-platform-delivery-engineering/README.md#anhkysuai-certbot-certbot) | `certbot/certbot` | Apache-2.0; mã nginxparser theo MIT | 33.346 | đọc tài liệu 2026-11-23 | 32 | Client ACME của EFF để lấy, gia hạn và tùy chọn cài chứng chỉ HTTPS. |
| [cilium](../../32-platform-delivery-engineering/README.md#chuyen-cilium) | `cilium/cilium` | Apache License 2.0 cho thành phần user space | 25.863 | đọc tài liệu 2026-11-18 | 32 | Giải pháp mạng, quan sát và bảo mật cho Kubernetes dựa trên eBPF: CNI, cân bằng tải, chính sách mạng L3-L7, service mesh. |

## Sao lưu, chi phí & vận hành hạ tầng (`backup-cost-ops`, 6)

| Dự án | Repo | License | ★ | Bằng chứng | Mục | Tóm tắt |
|---|---|---|---|---|---|---|
| [rclone](../../13-dev-stack-devops/README.md#anhkysuai-2026-11-23-rclone-rclone) | `rclone/rclone` | MIT | 61.198 | đọc tài liệu 2026-11-23 | 13 | Công cụ dòng lệnh đồng bộ, sao chép và phục vụ dữ liệu giữa nhiều hệ lưu trữ. |
| [PM2](../../32-platform-delivery-engineering/README.md#anhkysuai-unitech-pm2) | `Unitech/pm2` | AGPL-3.0 | 43.342 | đọc tài liệu 2026-11-23 | 32 | Trình quản lý tiến trình cho Node.js/Bun và chương trình chạy lâu dài. |
| [Arthas](../../33-reliability-observability-operations/README.md#anhkysuai-alibaba-arthas) | `alibaba/arthas` | Apache-2.0 | 37.630 | đọc tài liệu 2026-11-23 | 33 | Công cụ chẩn đoán Java đang chạy để tìm vấn đề mà không cần sửa mã ứng dụng. |
| [restic](../../09-engineering-checklists/README.md#operations-recovery-cost-evidence) | `restic/restic` | BSD-2-Clause | 36.948 | đọc mã 2026-11-02 | 09 | Backup snapshot mã hóa/dedupe đa backend; |
| [Velero](../../09-engineering-checklists/README.md#operations-recovery-cost-evidence) | `velero-io/velero` | Apache-2.0 | 10.365 | đọc mã 2026-11-02 | 09 | Canonical mới từ vmware-tanzu/velero; |
| [OpenCost](../../09-engineering-checklists/README.md#operations-recovery-cost-evidence) | `opencost/opencost` | Apache-2.0 | 6.799 | đọc mã 2026-11-02 | 09 | Spec+implementation cost K8s; |

## Terminal, shell & công cụ dòng lệnh (`terminal-cli`, 43)

| Dự án | Repo | License | ★ | Bằng chứng | Mục | Tóm tắt |
|---|---|---|---|---|---|---|
| [ohmyzsh](../../13-dev-stack-devops/README.md#chuyen-ohmyzsh) | `ohmyzsh/ohmyzsh` | MIT | 190.765 | đọc tài liệu 2026-11-18 | 13 | Khung mã nguồn mở do cộng đồng phát triển để quản lý cấu hình zsh, kèm nhiều plugin và theme. |
| [terminal](../../13-dev-stack-devops/README.md#chuyen-terminal) | `microsoft/terminal` | MIT | 105.413 | đọc tài liệu 2026-11-18 | 13 | Mã nguồn Windows Terminal, Windows Terminal Preview, console host conhost.exe và các thành phần dùng chung. |
| [fzf](../../13-dev-stack-devops/README.md#chuyen-fzf) | `junegunn/fzf` | MIT | 84.249 | đọc tài liệu 2026-11-18 | 13 | fzf là công cụ tìm kiếm mờ đa dụng trên dòng lệnh kiêm bộ công cụ dựng giao diện terminal tương tác. |
| [lazygit](../../13-dev-stack-devops/README.md#chuyen-lazygit) | `jesseduffield/lazygit` | MIT | 83.950 | đọc tài liệu 2026-11-18 | 13 | lazygit là giao diện terminal đơn giản cho các lệnh git. |
| [tabby](../../13-dev-stack-devops/README.md#chuyen-tabby) | `Eugeny/tabby` | MIT | 75.475 | đọc tài liệu 2026-11-18 | 13 | Trình giả lập terminal cấu hình cao kèm client SSH, Telnet và serial cho Windows, macOS và Linux (trước đây tên Terminus). |
| [ripgrep](../../13-dev-stack-devops/README.md#anhkysuai-burntsushi-ripgrep) | `BurntSushi/ripgrep` | MIT OR Unlicense | 70.184 | đọc tài liệu 2026-11-23 | 13 | CLI tìm biểu thức chính quy trong cây thư mục, dùng được trên Windows, macOS và Linux. |
| [Alacritty](../../13-dev-stack-devops/README.md#anhkysuai-alacritty-alacritty) | `alacritty/alacritty` | Apache-2.0; thành phần MIT theo thông báo riêng | 66.272 | đọc tài liệu 2026-11-23 | 13 | Terminal dùng OpenGL, chạy trên BSD, Linux, macOS và Windows. |
| [Termux app](../../13-dev-stack-devops/README.md#anhkysuai-termux-termux-app) | `termux/termux-app` | GPL-3.0-only; thành phần terminal có ngoại lệ Apache-2.0 | 65.516 | đọc tài liệu 2026-11-23 | 13 | Ứng dụng terminal và môi trường Linux trên Android; |
| [Git](../../13-dev-stack-devops/README.md#anhkysuai-git-git) | `git/git` | GPL-2.0-only; một số thành phần tương thích có điều khoản riêng | 64.479 | đọc tài liệu 2026-11-23 | 13 | Hệ quản lý phiên bản phân tán cho lịch sử mã, nhánh và thay đổi. |
| [bat](../../13-dev-stack-devops/README.md#anhkysuai-sharkdp-bat) | `sharkdp/bat` | MIT OR Apache-2.0 | 61.377 | đọc tài liệu 2026-11-23 | 13 | Trình đọc file trên terminal có tô cú pháp, số dòng và dấu thay đổi Git. |
| [Starship](../../13-dev-stack-devops/README.md#anhkysuai-starship-starship) | `starship/starship` | ISC | 60.872 | đọc tài liệu 2026-11-23 | 13 | Prompt có cấu hình dùng chung cho nhiều shell và hệ điều hành. |
| [Rich](../../13-dev-stack-devops/README.md#anhkysuai-textualize-rich) | `Textualize/rich` | MIT | 57.853 | đọc tài liệu 2026-11-23 | 13 | Thư viện Python hiển thị bảng, tiến độ, Markdown, cú pháp và traceback trên terminal. |
| [PowerShell](../../13-dev-stack-devops/README.md#anhkysuai-powershell-powershell) | `PowerShell/PowerShell` | MIT | 56.276 | đọc tài liệu 2026-11-23 | 13 | Shell, ngôn ngữ script và hệ cmdlet đa nền tảng, xử lý dữ liệu có cấu trúc. |
| [GitHub CLI](../../13-dev-stack-devops/README.md#anhkysuai-cli-cli) | `cli/cli` | MIT | 47.162 | đọc tài liệu 2026-11-23 | 13 | Công cụ gh đưa tác vụ GitHub vào terminal và tự động hóa. |
| [zx](../../13-dev-stack-devops/README.md#anhkysuai-google-zx) | `google/zx` | Apache-2.0 | 45.865 | đọc tài liệu 2026-11-23 | 13 | Viết script điều phối shell bằng JavaScript/TypeScript với wrapper child_process. |
| [fd](../../13-dev-stack-devops/README.md#anhkysuai-sharkdp-fd) | `sharkdp/fd` | MIT OR Apache-2.0 | 45.169 | đọc tài liệu 2026-11-23 | 13 | Tìm đường dẫn bằng regex hoặc glob với giao diện dòng lệnh ngắn. |
| [Cobra](../../13-dev-stack-devops/README.md#anhkysuai-spf13-cobra) | `spf13/cobra` | Apache-2.0 | 44.825 | đọc tài liệu 2026-11-23 | 13 | Thư viện Go xây CLI có cây lệnh và cờ. |
| [yazi](../../13-dev-stack-devops/README.md#chuyen-yazi) | `sxyazi/yazi` | MIT | 43.468 | đọc tài liệu 2026-11-18 | 13 | Trình quản lý file trong terminal viết bằng Rust, dựa trên I/O bất đồng bộ, có xem trước ảnh/mã và hệ plugin Lua. |
| [Nushell](../../13-dev-stack-devops/README.md#anhkysuai-nushell-nushell) | `nushell/nushell` | MIT | 41.077 | đọc tài liệu 2026-11-23 | 13 | Shell truyền bảng và giá trị có cấu trúc qua pipeline. |
| [zoxide](../../13-dev-stack-devops/README.md#anhkysuai-ajeetdsouza-zoxide) | `ajeetdsouza/zoxide` | MIT | 40.710 | đọc tài liệu 2026-11-23 | 13 | Điều hướng thư mục bằng lịch sử sử dụng thay cho gõ đường dẫn dài. |
| [Zellij](../../13-dev-stack-devops/README.md#anhkysuai-zellij-org-zellij) | `zellij-org/zellij` | MIT | 36.194 | đọc tài liệu 2026-11-23 | 13 | Workspace terminal nhiều pane, session và bố cục cấu hình được. |
| [Kitty](../../13-dev-stack-devops/README.md#anhkysuai-kovidgoyal-kitty) | `kovidgoyal/kitty` | GPL-3.0-only | 35.806 | đọc tài liệu 2026-11-23 | 13 | Terminal dùng GPU cho Linux, macOS và BSD. |
| [fish](../../13-dev-stack-devops/README.md#anhkysuai-fish-shell-fish-shell) | `fish-shell/fish-shell` | GPL-2.0-only AND LGPL-2.0-or-later AND MIT AND PSF-2.0 | 34.513 | đọc tài liệu 2026-11-23 | 13 | Shell tương tác có gợi ý, tô cú pháp và completion sẵn. |
| [Delta](../../13-dev-stack-devops/README.md#anhkysuai-dandavison-delta) | `dandavison/delta` | MIT | 32.815 | đọc tài liệu 2026-11-23 | 13 | Pager tô cú pháp và bố trí diff cho Git, grep và review terminal. |
| [Atuin](../../13-dev-stack-devops/README.md#anhkysuai-atuinsh-atuin) | `atuinsh/atuin` | MIT | 32.575 | đọc tài liệu 2026-11-23 | 13 | Lưu và tìm lịch sử shell cùng thread công cụ agent. |
| [cli](../../13-dev-stack-devops/README.md#chuyen-cli) | `googleworkspace/cli` | Apache-2.0 | 32.452 | đọc tài liệu 2026-11-18 | 13 | CLI gws dùng chung cho mọi API Google Workspace (Drive, Gmail, Calendar, Sheets…), sinh lệnh động từ Google Discovery Service, xuất JSON cho người và AI agent. |
| [tqdm](../../13-dev-stack-devops/README.md#chuyen-tqdm) | `tqdm/tqdm` | MPL-2.0 và MIT | 31.390 | đọc tài liệu 2026-11-18 | 13 | Thư viện Python hiển thị thanh tiến độ thông minh cho vòng lặp và lệnh shell qua pipe. |
| [WezTerm](../../13-dev-stack-devops/README.md#anhkysuai-wezterm-wezterm) | `wezterm/wezterm` | MIT | 29.662 | đọc tài liệu 2026-11-23 | 13 | Terminal và multiplexer đa nền tảng viết Rust, dùng GPU. |
| [Python Fire](../../13-dev-stack-devops/README.md#anhkysuai-google-python-fire) | `google/python-fire` | Apache-2.0 | 28.229 | đọc tài liệu 2026-11-23 | 13 | Sinh CLI trực tiếp từ function, class, module hoặc object Python. |
| [Cmder](../../13-dev-stack-devops/README.md#anhkysuai-cmderdev-cmder) | `cmderdev/cmder` | MIT cho Cmder; công cụ đi kèm giữ license riêng | 27.012 | đọc tài liệu 2026-11-23 | 13 | Gói terminal Windows portable gồm launcher, Clink, theme và công cụ dòng lệnh. |
| [Cool Retro Term](../../13-dev-stack-devops/README.md#anhkysuai-swordfish90-cool-retro-term) | `Swordfish90/cool-retro-term` | GPL-3.0-or-later cho giao diện ứng dụng; thư viện/font theo license riêng | 26.590 | đọc tài liệu 2026-11-23 | 13 | Terminal mô phỏng màn hình CRT bằng Qt/QML trên Linux và macOS. |
| [Oh my tmux!](../../13-dev-stack-devops/README.md#anhkysuai-gpakosz-tmux) | `gpakosz/.tmux` | MIT OR WTFPL-2.0 | 25.478 | đọc tài liệu 2026-11-23 | 13 | Cấu hình tmux có sẵn cho keybinding, status và clipboard. |
| [Superfile](../../13-dev-stack-devops/README.md#anhkysuai-yorukot-superfile) | `yorukot/superfile` | MIT | 24.118 | đọc tài liệu 2026-11-23 | 13 | Trình quản lý tệp trong terminal với theme, hotkey và plugin. |
| [eza](../../13-dev-stack-devops/README.md#anhkysuai-eza-community-eza) | `eza-community/eza` | EUPL-1.2 | 24.009 | đọc tài liệu 2026-11-23 | 13 | CLI liệt kê tệp thay thế ls, bổ sung màu, metadata và trạng thái Git. |
| [cloc](../../13-dev-stack-devops/README.md#anhkysuai-aldanial-cloc) | `AlDanial/cloc` | GPL-2.0 | 23.683 | đọc tài liệu 2026-11-23 | 13 | CLI đếm dòng mã, chú thích và dòng trống theo nhiều ngôn ngữ. |
| [zsh-syntax-highlighting](../../13-dev-stack-devops/README.md#chuyen-zsh-syntax-highlighting) | `zsh-users/zsh-syntax-highlighting` | BSD 3-Clause | 23.096 | đọc tài liệu 2026-11-18 | 13 | Plugin cho zsh tô màu cú pháp dòng lệnh ngay khi gõ ở dấu nhắc, theo kiểu fish, giúp phát hiện lỗi cú pháp trước khi chạy. |
| [witr](../../13-dev-stack-devops/README.md#chuyen-witr) | `pranshuparmar/witr` | Apache-2.0 | 23.032 | đọc tài liệu 2026-11-18 | 13 | Công cụ dòng lệnh (kèm TUI) trả lời câu hỏi vì sao một tiến trình, dịch vụ, container hay cổng đang chạy bằng cách truy ngược chuỗi nguồn gốc của PID. |
| [GitUI](../../13-dev-stack-devops/README.md#anhkysuai-gitui-org-gitui) | `gitui-org/gitui` | MIT | 22.681 | đọc tài liệu 2026-11-23 | 13 | Giao diện terminal dùng bàn phím để xem diff, stage từng dòng hoặc hunk, commit và thao tác stash. |
| [nnn](../../13-dev-stack-devops/README.md#chuyen-nnn) | `jarun/nnn` | BSD 2-Clause | 22.126 | đọc tài liệu 2026-11-18 | 13 | Trình quản lý file trên terminal rất nhỏ gọn (~150 KiB), gần như không cần cấu hình, có phân tích dung lượng đĩa, đổi tên hàng loạt và chọn file. |
| [Typer](../../13-dev-stack-devops/README.md#anhkysuai-fastapi-typer) | `fastapi/typer` | MIT | 20.414 | đọc tài liệu 2026-11-23 | 13 | Thư viện Python tạo CLI từ type hint, hỗ trợ command, subcommand, argument, option và help tự động. |
| [larksuite/cli](../../13-dev-stack-devops/README.md#chuyen-larksuite-cli) | `larksuite/cli` | MIT | 18.144 | đọc tài liệu 2026-11-18 | 13 | CLI chính thức của Lark/Feishu cho người và AI agent, bao phủ nhắn tin, tài liệu, Base, Sheets, lịch, mail, tác vụ, cuộc họp và nhiều miền khác. |
| [electerm](../../13-dev-stack-devops/README.md#chuyen-electerm) | `electerm/electerm` | MIT | 15.656 | đọc tài liệu 2026-11-18 | 13 | Trình khách terminal/ssh/sftp/ftp/telnet/serialport/RDP/VNC/Spice mã nguồn mở, kiêm trình quản lý tệp, chạy đa nền tảng. |
| [bash-it](../../13-dev-stack-devops/README.md#chuyen-bash-it) | `Bash-it/bash-it` | MIT | 15.307 | đọc tài liệu 2026-11-18 | 13 | Khung cấu hình Bash do cộng đồng đóng góp, gom alias, plugin, completion và theme để quản lý shell hằng ngày (tương tự oh-my-zsh cho Bash). |

## Editor & IDE (`editor-ide`, 16)

| Dự án | Repo | License | ★ | Bằng chứng | Mục | Tóm tắt |
|---|---|---|---|---|---|---|
| [vscode](../../13-dev-stack-devops/README.md#chuyen-vscode) | `microsoft/vscode` | MIT | 195.711 | đọc tài liệu 2026-11-18 | 13 | Kho mã nguồn mở "Code - OSS" nơi Microsoft phát triển trình soạn thảo Visual Studio Code cùng cộng đồng. |
| [neovim](../../13-dev-stack-devops/README.md#chuyen-neovim) | `neovim/neovim` | Apache-2.0 | 103.928 | đọc tài liệu 2026-11-18 | 13 | Neovim là bản tái cấu trúc mạnh của Vim, hướng tới dễ bảo trì, mở rộng và hỗ trợ giao diện nâng cao. |
| [zed](../../13-dev-stack-devops/README.md#chuyen-zed) | `zed-industries/zed` | Chủ yếu GPL-3.0-or-later | 95.238 | đọc tài liệu 2026-11-18 | 13 | Zed là trình soạn thảo mã hiệu năng cao, hỗ trợ cộng tác nhiều người, từ nhóm tác giả Atom và Tree-sitter. |
| [FiraCode](../../13-dev-stack-devops/README.md#chuyen-firacode) | `tonsky/FiraCode` | SIL Open Font License 1.1 | 82.209 | đọc tài liệu 2026-11-18 | 13 | Fira Code là phông chữ đơn cách miễn phí có ligature cho các tổ hợp ký tự lập trình phổ biến. |
| [code-server](../../13-dev-stack-devops/README.md#chuyen-code-server) | `coder/code-server` | MIT | 79.900 | đọc tài liệu 2026-11-18 | 13 | code-server chạy VS Code trên bất kỳ máy nào và truy cập qua trình duyệt. |
| [Helix](../../13-dev-stack-devops/README.md#anhkysuai-helix-editor-helix) | `helix-editor/helix` | MPL-2.0 | 46.977 | đọc tài liệu 2026-11-23 | 13 | Editor terminal dạng modal với mô hình lựa chọn văn bản và nhiều selection. |
| [Lapce](../../13-dev-stack-devops/README.md#anhkysuai-lapce-lapce) | `lapce/lapce` | Apache-2.0 | 39.104 | đọc tài liệu 2026-11-23 | 13 | Code editor Rust dùng Floem/wgpu với LSP, terminal và remote development. |
| [VSCodium](../../13-dev-stack-devops/README.md#anhkysuai-vscodium-vscodium) | `VSCodium/vscodium` | MIT cho script/build; extension và thành phần theo license riêng | 34.230 | đọc tài liệu 2026-11-23 | 13 | Script tạo bản phân phối VS Code với cấu hình cộng đồng. |
| [Notepad++](../../13-dev-stack-devops/README.md#anhkysuai-notepad-plus-plus-notepad-plus-plus) | `notepad-plus-plus/notepad-plus-plus` | GPL-3.0 theo LICENSE của dự án | 29.961 | đọc tài liệu 2026-11-23 | 13 | Editor mã và văn bản cho Windows hỗ trợ nhiều ngôn ngữ. |
| [Micro](../../13-dev-stack-devops/README.md#anhkysuai-micro-editor-micro) | `micro-editor/micro` | MIT; dependency theo LICENSE-THIRD-PARTY | 29.950 | đọc tài liệu 2026-11-23 | 13 | Editor terminal dễ dùng, phát hành dưới dạng binary đơn. |
| [NvChad](../../13-dev-stack-devops/README.md#anhkysuai-nvchad-nvchad) | `NvChad/NvChad` | GPL-3.0; plugin có license riêng | 28.557 | đọc tài liệu 2026-11-23 | 13 | Cấu hình Neovim Lua tập trung UI và nạp plugin theo nhu cầu. |
| [LazyVim](../../13-dev-stack-devops/README.md#anhkysuai-lazyvim-lazyvim) | `LazyVim/LazyVim` | Apache-2.0; plugin có license riêng | 27.910 | đọc tài liệu 2026-11-23 | 13 | Cấu hình Neovim dựa trên lazy.nvim với plugin và keymap có sẵn. |
| [CodeEdit](../../13-dev-stack-devops/README.md#anhkysuai-codeeditapp-codeedit) | `CodeEditApp/CodeEdit` | MIT | 23.125 | đọc tài liệu 2026-11-23 | 13 | Code editor native macOS với hướng mở rộng thành môi trường phát triển đầy đủ. |
| [Eclipse Theia](../../13-dev-stack-devops/README.md#anhkysuai-eclipse-theia-theia) | `eclipse-theia/theia` | EPL-2.0; GPL-2.0 với Classpath Exception là secondary; một số tệp MIT | 21.783 | đọc tài liệu 2026-11-23 | 13 | Nền tảng xây IDE và công cụ tùy biến chạy trên trình duyệt hoặc desktop Electron. |
| [lazy.nvim](../../13-dev-stack-devops/README.md#anhkysuai-folke-lazy.nvim) | `folke/lazy.nvim` | Apache-2.0 | 21.766 | đọc tài liệu 2026-11-23 | 13 | Trình quản lý plugin Neovim với lazy-loading theo sự kiện, lệnh, filetype và phím tắt. |
| [IntelliJ Open Source Repository](../../13-dev-stack-devops/README.md#anhkysuai-jetbrains-intellij-community) | `JetBrains/intellij-community` | Apache-2.0 cho mã theo LICENSE.txt; Open-Source Build Terms và license bên thứ ba áp dụng theo bản phân phối | 20.749 | đọc tài liệu 2026-11-23 | 13 | Phần mã nguồn mở của IntelliJ Platform, IntelliJ IDEA và PyCharm để nghiên cứu nền tảng IDE hoặc xây công cụ mở rộng. |

## Môi trường dev & quản lý toolchain (`dev-env`, 26)

| Dự án | Repo | License | ★ | Bằng chứng | Mục | Tóm tắt |
|---|---|---|---|---|---|---|
| [gitignore](../../13-dev-stack-devops/README.md#chuyen-gitignore) | `github/gitignore` | CC0 1.0 Universal | 176.339 | đọc tài liệu 2026-11-18 | 13 | Bộ sưu tập mẫu .gitignore của GitHub, dùng cho bộ chọn mẫu khi tạo repo trên GitHub.com. |
| [uv](../../13-dev-stack-devops/README.md#ch-uv) | `astral-sh/uv` | Apache-2.0 OR MIT | 91.402 | đọc tài liệu 2026-11-23 | 13 | Package manager Python nhanh (Astral); |
| [Homebrew](../../13-dev-stack-devops/README.md#anhkysuai-homebrew-brew) | `Homebrew/brew` | BSD-2-Clause cho code; tài liệu theo CC BY | 50.411 | đọc tài liệu 2026-11-23 | 13 | Trình quản lý gói và môi trường công cụ, có formula, cask và bundle. |
| [pyenv](../../13-dev-stack-devops/README.md#anhkysuai-pyenv-pyenv) | `pyenv/pyenv` | MIT | 45.183 | đọc tài liệu 2026-11-23 | 13 | Chuyển phiên bản Python theo người dùng, thư mục dự án hoặc biến môi trường. |
| [V](../../37-programming-languages-runtimes/README.md#anhkysuai-vlang-v) | `vlang/v` | MIT | 38.124 | đọc tài liệu 2026-11-23 | 37 | Ngôn ngữ và compiler hướng cú pháp gọn, backend C/JavaScript. |
| [pnpm](../../13-dev-stack-devops/README.md#anhkysuai-pnpm-pnpm) | `pnpm/pnpm` | MIT; pnpr/ là PolyForm Shield 1.0.0 source-available | 37.156 | đọc tài liệu 2026-11-23 | 13 | Quản lý package JavaScript với content-addressable store và workspace. |
| [Poetry](../../13-dev-stack-devops/README.md#anhkysuai-python-poetry-poetry) | `python-poetry/poetry` | MIT | 34.324 | đọc tài liệu 2026-11-23 | 13 | Quản lý dependency và đóng gói dự án Python dựa trên pyproject.toml. |
| [Carbon Language](../../37-programming-languages-runtimes/README.md#anhkysuai-carbon-language-carbon-lang) | `carbon-language/carbon-lang` | Apache-2.0 WITH LLVM-exception | 33.969 | đọc tài liệu 2026-11-23 | 37 | Nghiên cứu ngôn ngữ kế nhiệm C++ với hướng tương tác hai chiều. |
| [Composer](../../13-dev-stack-devops/README.md#anhkysuai-composer-composer) | `composer/composer` | MIT | 29.589 | đọc tài liệu 2026-11-23 | 13 | Quản lý dependency dự án PHP. |
| [Nx](../../13-dev-stack-devops/README.md#anhkysuai-nrwl-nx) | `nrwl/nx` | MIT cho mã repo; dịch vụ CI/cloud theo điều khoản riêng | 29.494 | đọc tài liệu 2026-11-23 | 13 | Điều phối monorepo với cache và chạy tác vụ bị ảnh hưởng. |
| [Emscripten](../../13-dev-stack-devops/README.md#anhkysuai-emscripten-core-emscripten) | `emscripten-core/emscripten` | MIT OR NCSA; LLVM/Binaryen và thư viện kèm có license riêng | 27.792 | đọc tài liệu 2026-11-23 | 13 | Biên dịch C/C++ sang WebAssembly và JavaScript glue. |
| [vcpkg](../../13-dev-stack-devops/README.md#anhkysuai-microsoft-vcpkg) | `microsoft/vcpkg` | MIT cho repo; mỗi port giữ license upstream | 27.632 | đọc tài liệu 2026-11-23 | 13 | Quản lý package C/C++ tích hợp CMake, MSBuild và nhiều hệ build. |
| [fnm](../../13-dev-stack-devops/README.md#anhkysuai-schniz-fnm) | `Schniz/fnm` | GPL-3.0 | 27.487 | đọc tài liệu 2026-11-23 | 13 | Quản lý phiên bản Node.js đa nền tảng bằng binary Rust. |
| [Vagrant CLI](../../32-platform-delivery-engineering/README.md#anhkysuai-hashicorp-vagrant) | `hashicorp/vagrant` | MIT | 27.238 | đọc tài liệu 2026-11-23 | 32 | Công cụ mô tả và phân phối môi trường phát triển với máy ảo hoặc provider khác. |
| [OpenAPI Generator](../../13-dev-stack-devops/README.md#anhkysuai-openapitools-openapi-generator) | `OpenAPITools/openapi-generator` | Apache-2.0; đối chiếu template, đầu vào và license mã sinh | 26.867 | đọc tài liệu 2026-11-23 | 13 | Sinh SDK, server stub và tài liệu từ đặc tả OpenAPI. |
| [Bend](../../37-programming-languages-runtimes/README.md#anhkysuai-bendlang-bend) | `bendlang/bend` | Apache-2.0 | 25.792 | đọc tài liệu 2026-11-23 | 37 | Ngôn ngữ hướng tính toán song song và khai báo luật kèm chứng minh. |
| [asdf](../../13-dev-stack-devops/README.md#anhkysuai-asdf-vm-asdf) | `asdf-vm/asdf` | MIT | 25.628 | đọc tài liệu 2026-11-23 | 13 | Quản lý nhiều runtime theo dự án bằng plugin và .tool-versions. |
| [Pipenv](../../13-dev-stack-devops/README.md#anhkysuai-pypa-pipenv) | `pypa/pipenv` | MIT | 25.021 | đọc tài liệu 2026-11-23 | 13 | Kết hợp quản lý virtualenv và dependency Python cho ứng dụng. |
| [Delve](../../13-dev-stack-devops/README.md#anhkysuai-go-delve-delve) | `go-delve/delve` | MIT | 24.988 | đọc tài liệu 2026-11-23 | 13 | Debugger chuyên dụng cho chương trình Go. |
| [Air](../../13-dev-stack-devops/README.md#anhkysuai-air-verse-air) | `air-verse/air` | GPL-3.0 | 24.150 | đọc tài liệu 2026-11-23 | 13 | Theo dõi file rồi build/restart ứng dụng Go khi phát triển. |
| [desktop](../../13-dev-stack-devops/README.md#anhkysuai-2026-11-23-desktop-desktop) | `desktop/desktop` | MIT | 22.136 | đọc tài liệu 2026-11-23 | 13 | Mã nguồn GitHub Desktop, ứng dụng Electron/TypeScript cho thao tác Git bằng giao diện. |
| [GitButler](../../13-dev-stack-devops/README.md#anhkysuai-gitbutlerapp-gitbutler) | `gitbutlerapp/gitbutler` | FSL-1.1-MIT; MIT có hiệu lực sau hai năm cho từng phiên bản | 22.010 | đọc tài liệu 2026-11-23 | 13 | Ứng dụng và CLI quản lý Git với stacked branch, parallel branch, chỉnh commit và khả năng hoàn tác. |
| [Nix](../../13-dev-stack-devops/README.md#nix) | `NixOS/nix` | LGPL-2.1 | 17.960 | đọc mã 2026-11-02 | 13 | Package/build manager Unix; |
| [devenv](../../13-dev-stack-devops/README.md#devenv) | `cachix/devenv` | Apache-2.0 | 7.794 | đọc mã 2026-11-02 | 13 | Môi trường dev khai báo trên Nix với lock/packages/services/tests; |
| [Development Container Specification](../../32-platform-delivery-engineering/README.md#factory-devcontainers-2026-11-04) | `devcontainers/spec` | CC-BY-4.0 (spec); MIT (code) | — | đọc tài liệu 2026-11-04 | 32 | Đặc tả môi trường dev/CI: initializeCommand chạy host; |
| [mise](../../13-dev-stack-devops/README.md#factory-2026-11-04-mise) | `jdx/mise` | MIT | — | đọc mã 2026-11-04 | 13 | Khóa toolchain và task/env; |

## Hệ điều hành & công cụ hệ thống (`os-system`, 17)

| Dự án | Repo | License | ★ | Bằng chứng | Mục | Tóm tắt |
|---|---|---|---|---|---|---|
| [linux](../../13-dev-stack-devops/README.md#chuyen-linux) | `torvalds/linux` | GPL-2.0 WITH Linux-syscall-note | 256.236 | đọc tài liệu 2026-11-18 | 13 | Mã nguồn nhân Linux, lõi của mọi hệ điều hành Linux, quản lý phần cứng, tài nguyên hệ thống và cung cấp dịch vụ nền cho phần mềm khác. |
| [serenity](../../13-dev-stack-devops/README.md#anhkysuai-2026-11-23-serenityos-serenity) | `SerenityOS/serenity` | BSD-2-Clause | 33.984 | đọc tài liệu 2026-11-23 | 13 | Hệ điều hành đồ họa kiểu Unix với kernel, thư viện và ứng dụng tự phát triển. |
| [DevToys](../../13-dev-stack-devops/README.md#anhkysuai-devtoys-app-devtoys) | `DevToys-app/DevToys` | MIT; phần mềm bên thứ ba có thông báo riêng | 32.303 | đọc tài liệu 2026-11-23 | 13 | Bộ tiện ích desktop chuyển đổi, định dạng và kiểm tra dữ liệu cho developer. |
| [Niri](../../35-desktop-productivity-apps/README.md#anhkysuai-niri-wm-niri) | `niri-wm/niri` | GPL-3.0-or-later | 29.212 | đọc tài liệu 2026-11-23 | 35 | Wayland compositor xếp cửa sổ thành dải cột cuộn ngang. |
| [UniGetUI](../../35-desktop-productivity-apps/README.md#anhkysuai-devolutions-unigetui) | `Devolutions/UniGetUI` | MIT; package được cài có license riêng | 27.211 | đọc tài liệu 2026-11-23 | 35 | GUI tập trung cho nhiều package manager, ưu tiên Windows và có bản đa nền. |
| [WinGet](../../13-dev-stack-devops/README.md#anhkysuai-microsoft-winget-cli) | `microsoft/winget-cli` | MIT cho client; package theo điều khoản riêng | 26.636 | đọc tài liệu 2026-11-23 | 13 | Client Windows Package Manager cài và quản lý phần mềm. |
| [Fastfetch](../../13-dev-stack-devops/README.md#anhkysuai-fastfetch-cli-fastfetch) | `fastfetch-cli/fastfetch` | MIT | 25.434 | đọc tài liệu 2026-11-23 | 13 | Thu thập và trình bày thông tin hệ thống trong terminal. |
| [nextai-translator](../../35-desktop-productivity-apps/README.md#chuyen-nextai-translator) | `nextai-translator/nextai-translator` | AGPL-3.0 | 25.067 | đọc tài liệu 2026-11-18 | 35 | Ứng dụng dịch, trau chuốt và tóm tắt văn bản bằng LLM, có tiện ích trình duyệt (Chrome, Firefox) và app desktop Windows/macOS/Linux; |
| [Tasmota](../../36-self-hosting-homelab/README.md#anhkysuai-2026-11-23-arendst-tasmota) | `arendst/Tasmota` | GPL-3.0 | 25.013 | đọc tài liệu 2026-11-23 | 36 | Firmware thay thế cho thiết bị ESP8266/ESP32, điều khiển cục bộ qua MQTT, HTTP và các giao thức thiết bị. |
| [uutils coreutils](../../13-dev-stack-devops/README.md#anhkysuai-uutils-coreutils) | `uutils/coreutils` | MIT | 24.433 | đọc tài liệu 2026-11-23 | 13 | Triển khai lại bộ GNU coreutils bằng Rust cho nhiều nền tảng. |
| [AeroSpace](../../35-desktop-productivity-apps/README.md#anhkysuai-nikitabobko-aerospace) | `nikitabobko/AeroSpace` | MIT | 23.926 | đọc tài liệu 2026-11-23 | 35 | Trình quản lý cửa sổ dạng tiling kiểu i3 cho macOS. |
| [WinBoat](../../35-desktop-productivity-apps/README.md#anhkysuai-winboat-org-winboat) | `winboat-org/winboat` | MIT cho ứng dụng; Windows và phần mềm khách có giấy phép riêng | 23.435 | đọc tài liệu 2026-11-23 | 35 | Ứng dụng Electron giúp chạy cửa sổ phần mềm Windows trong desktop Linux. |
| [voyager](../../35-desktop-productivity-apps/README.md#chuyen-voyager) | `voyager-crew/voyager` | GPL-3.0 | 20.655 | đọc tài liệu 2026-11-18 | 35 | Tiện ích trình duyệt bổ sung thư mục, dòng thời gian, xuất hội thoại và chép công thức cho Gemini, AI Studio, ChatGPT, Claude, DeepSeek và Kimi; |
| [Applite](../../35-desktop-productivity-apps/README.md) | `milanvarady/Applite` | MIT | 7.104 | chưa chuẩn hóa | 35 | GUI Homebrew cho cask/app trên macOS; |
| [Cork](../../35-desktop-productivity-apps/README.md) | `buresdv/Cork` | provisional (không OSI) | 4.717 | chưa chuẩn hóa | 35 | GUI Homebrew; |
| [BrewUI](../../35-desktop-productivity-apps/README.md) | `Homebrew/BrewUI` | AGPL-3.0 | 2.769 | chưa chuẩn hóa | 35 | GUI chính thức của Homebrew (SwiftUI, macOS 26+), cask homebrew-app, ra cùng Homebrew 7.0.0; |
| [CleanMyLinux](../../35-desktop-productivity-apps/README.md) | `Better-Linux/CleanMyLinux` | MIT | 10 | chưa chuẩn hóa | 35 | App dọn dẹp Linux desktop (Tauri v2+Rust+React19), gỡ app + cập nhật đa package manager, có ml/ phân loại app. |

## Ứng dụng tự host (ảnh, git, file...) (`self-hosted-app`, 9)

| Dự án | Repo | License | ★ | Bằng chứng | Mục | Tóm tắt |
|---|---|---|---|---|---|---|
| [awesome-selfhosted](../../36-self-hosting-homelab/README.md#chuyen-awesome-selfhosted) | `awesome-selfhosted/awesome-selfhosted` | CC-BY-SA-3.0 | 338.129 | đọc tài liệu 2026-11-18 | 36 | Danh sách các dịch vụ mạng và ứng dụng web phần mềm tự do có thể tự host trên máy chủ riêng, chia theo hạng mục. |
| [immich](../../36-self-hosting-homelab/README.md#chuyen-immich) | `immich-app/immich` | GNU AGPL v3 | 119.489 | đọc tài liệu 2026-11-18 | 36 | Giải pháp tự host quản lý ảnh và video hiệu năng cao, có ứng dụng web và di động. |
| [core](../../36-self-hosting-homelab/README.md#chuyen-core) | `home-assistant/core` | Apache License 2.0 | 92.443 | đọc tài liệu 2026-11-18 | 36 | Nền tảng tự động hoá nhà ở mã nguồn mở ưu tiên điều khiển cục bộ và quyền riêng tư, chạy được trên Raspberry Pi hoặc máy chủ cục bộ. |
| [gitea](../../36-self-hosting-homelab/README.md#chuyen-gitea) | `go-gitea/gitea` | MIT | 59.145 | đọc tài liệu 2026-11-18 | 36 | Dịch vụ phát triển phần mềm tự host trọn gói: Git hosting, review mã, issue, kanban, wiki, registry gói và CI/CD tương thích GitHub Actions. |
| [it-tools](../../13-dev-stack-devops/README.md#anhkysuai-2026-11-23-corentinth-it-tools) | `CorentinTh/it-tools` | GPL-3.0 | 41.337 | đọc tài liệu 2026-11-23 | 13 | Bộ tiện ích web cho lập trình viên và IT, có thể tự host bằng container. |
| [Proxmox VE Helper Scripts](../../36-self-hosting-homelab/README.md#anhkysuai-community-scripts-proxmoxve) | `community-scripts/ProxmoxVE` | MIT | 30.167 | đọc tài liệu 2026-11-23 | 36 | Bộ script cộng đồng cài ứng dụng vào container hoặc VM trên Proxmox VE. |
| [open-seo](../../36-self-hosting-homelab/README.md#chuyen-open-seo) | `every-app/open-seo` | MIT | 28.117 | đọc tài liệu 2026-11-18 | 36 | Công cụ SEO mã nguồn mở thay thế Semrush/Ahrefs (nghiên cứu từ khoá, theo dõi thứ hạng, backlink, audit site) kèm MCP server và skill cho AI agent. |
| [dashy](../../36-self-hosting-homelab/README.md#chuyen-dashy) | `lissy93/dashy` | MIT | 27.015 | đọc tài liệu 2026-11-18 | 36 | Trang chủ/dashboard tự host cho homelab, tập hợp liên kết ứng dụng kèm widget và giám sát trạng thái. |
| [seafile](../../36-self-hosting-homelab/README.md#chuyen-seafile) | `haiwen/seafile` | GPL v2 kèm ngoại lệ cho phép liên kết với OpenSSL | 15.468 | đọc tài liệu 2026-11-18 | 36 | Repo daemon client đồng bộ của Seafile, hệ thống lưu trữ đám mây mã nguồn mở có mã hoá thư viện và cộng tác nhóm. |

## Bảo mật CI & chuỗi cung ứng (`supply-chain-ci-security`, 1)

| Dự án | Repo | License | ★ | Bằng chứng | Mục | Tóm tắt |
|---|---|---|---|---|---|---|
| [Harden-Runner](../../13-dev-stack-devops/README.md#ch-harden-runner) | `step-security/harden-runner` | Apache-2.0 | 1.295 | đọc tài liệu 2026-11-23 | 13 | Giám sát egress/file/process runner GitHub Actions, egress-policy block; |
