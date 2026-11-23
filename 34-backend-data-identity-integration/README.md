# 34 · Backend, dữ liệu giao dịch, định danh và tích hợp

> Đọc ngày **2026-11-04**, phạm vi `code-read` cho ba hồ sơ có SHA dưới đây; chưa cài, chạy database, migration, IdP hoặc test upstream. Repo này giữ nghiên cứu và điều kiện nghiệm thu; code triển khai thuộc dự án của xưởng.

## 1. Vì sao cần mục riêng

[Mục 13](../13-dev-stack-devops/README.md) chọn stack/framework; [15](../15-ai-for-data/README.md)/[24](../24-ai-data-engineering/README.md) quản lý dữ liệu phân tích/AI; [12](../12-ai-security-guardrails/README.md) có ReBAC và guardrail; [21](../21-autonomous-workflows/README.md) có durable execution. Mục này nối các lớp đó vào **hợp đồng nghiệp vụ của backend**: ai được làm gì trên bản ghi nào, transaction nào được commit, schema nào tương thích với phiên bản app đang chạy, và retry có tạo tác dụng phụ trùng không.

| Năng lực | Artifact phải có | Cổng nhận của xưởng | Sai lầm cần tránh |
|---|---|---|---|
| Mô hình dữ liệu | ERD/schema, invariants, ownership và retention | FK/unique/check, nullability, timezone/currency và concurrency fixture | Chỉ kiểm CRUD happy path |
| Migration | File versioned + manifest release + kế hoạch expand/contract | Fresh DB, upgrade từ bản được hỗ trợ, rolling compatibility, lock/timeout | Có `down` nghĩa là rollback giữ được dữ liệu |
| Truy cập dữ liệu | Query/schema cùng revision, codegen/config | Compile/vet/diff và integration trên DB đúng version | Codegen type-safe chứng minh phân quyền/hiệu năng |
| Định danh | Issuer/client/flow, redirect, scopes, session/recovery policy | OIDC flow dương/âm, key rotation, expiry/logout | Đăng nhập thành công nghĩa là mọi API đã có quyền đúng |
| Phân quyền/đa tenant | Subject/resource/action/tenant, policy/model revision | Ma trận allow/deny, tenant A không đọc/ghi tenant B | Lấy tenant ID trong body hoặc tin mỗi role trong UI |
| Event/webhook/job | Event schema/version, outbox/inbox, idempotency key | Retry/replay, duplicate/out-of-order, crash-before/after-commit | Gọi "exactly-once" khi chỉ có retry hoặc ACK |

Các cổng trong bảng là đề xuất kỹ thuật, phải được dự án chọn ngưỡng, fixture và chủ sở hữu; chúng chưa được chạy tại `stored`.

## 2. Chọn lớp công cụ, tránh xây cả nền tảng khi chưa cần

| Nhu cầu | Điểm bắt đầu | Hai hướng so sánh | Điều quyết định |
|---|---|---|---|
| Schema SQL có lịch sử triển khai | goose | Migration của framework đang dùng; thay đổi SQL được điều phối bởi pipeline | Engine, khóa/DDL, transaction, backward compatibility và quyền DB |
| Query SQL tường minh, code gọi typed | sqlc | ORM của framework; query SQL viết tay có test | Dialect và generator thực sự hỗ trợ, codegen diff, query plan |
| SSO/federation và lifecycle tài khoản | Keycloak | Auth có sẵn của [Supabase](../13-dev-stack-devops/README.md); nhà cung cấp OIDC managed | Mức vận hành, federation/HA, data residency, recovery và chi phí |
| Quyền theo quan hệ tài nguyên | [OpenFGA](../12-ai-security-guardrails/README.md#openfga) | [SpiceDB](../12-ai-security-guardrails/README.md#spicedb); policy/RBAC trong app nhỏ | Mô hình quyền, consistency/revocation, latency và negative tests |
| Event từ transaction đã commit | Transactional outbox + worker | [Debezium](../15-ai-for-data/README.md); job/workflow [Temporal](../21-autonomous-workflows/README.md) | Boundary commit, replay/idempotence, retention/schema và vận hành |

OpenFGA, SpiceDB, Debezium và Temporal giữ hồ sơ gốc ở mục đã dẫn; không nhân bản catalog hay gán ngày kiểm mới cho chúng. Các lựa chọn ở mỗi hàng giải những lớp khác nhau, không thay thế nhau hoàn toàn.

## 3. Hồ sơ đọc mã

<a id="goose-migrations"></a>

### 3.1. goose của pressly: migration không tự điều phối mọi replica

| Thuộc tính | Giá trị |
|---|---|
| Repo / phân biệt tên | [pressly/goose](https://github.com/pressly/goose), migration SQL/Go; khác coding agent `block/goose` ở mục 01 |
| Phiên bản / license | `2d285d2249855c959765409c68b17a6634f0acb4`; MIT |
| Đã đọc | README/LICENSE, `migration_sql.go`, `provider_options.go`, `provider_run.go`, workflow unit và integration; chưa chạy |
| Cơ chế | Đường SQL dùng transaction thì mở transaction, chạy câu lệnh và cập nhật bảng version rồi commit; nhánh không transaction chạy/cập nhật version ngoài transaction. Khả năng DDL transactional còn phụ thuộc DB. |
| Khóa | API `Provider` chỉ dùng lock khi `useLocker` và `cfg.lockEnabled`; `WithSessionLocker`/`WithLocker` bật khóa tường minh. Không suy default của API này thành default của mọi CLI/integration. Một `Provider` mutex trong process không thay khóa giữa các replica. |
| CI | `ci.yaml` có build/vet/unit; `integration.yaml` gọi `make test-integration`. Có workflow không chứng minh engine/version triển khai đã được phủ. |
| Tích hợp | Chọn một migration runner cho release hoặc locker phù hợp DB, quyền DDL riêng và deadline; migration immutable sau phát hành. Kiểm fresh/upgrade/partial failure và ứng dụng N/N−1 cùng schema mới. |
| Giới hạn | `NO TRANSACTION`, DDL lock/backfill và lệnh ngoài DB có thể gây thay đổi dở dang. Down migration có thể mất dữ liệu; rollback phần mềm thường cần schema expand/contract chứ không tự gọi `down`. |

**Nguồn hồ sơ:** [README.md](https://github.com/pressly/goose/blob/2d285d2249855c959765409c68b17a6634f0acb4/README.md) · [LICENSE](https://github.com/pressly/goose/blob/2d285d2249855c959765409c68b17a6634f0acb4/LICENSE) · [migration_sql.go](https://github.com/pressly/goose/blob/2d285d2249855c959765409c68b17a6634f0acb4/migration_sql.go) · [provider_options.go](https://github.com/pressly/goose/blob/2d285d2249855c959765409c68b17a6634f0acb4/provider_options.go) · [provider_run.go](https://github.com/pressly/goose/blob/2d285d2249855c959765409c68b17a6634f0acb4/provider_run.go) · [.github/workflows/ci.yaml](https://github.com/pressly/goose/blob/2d285d2249855c959765409c68b17a6634f0acb4/.github/workflows/ci.yaml) · [.github/workflows/integration.yaml](https://github.com/pressly/goose/blob/2d285d2249855c959765409c68b17a6634f0acb4/.github/workflows/integration.yaml).

<a id="sqlc"></a>

### 3.2. sqlc: ba cổng khác nhau cho SQL và generated code

| Thuộc tính | Giá trị |
|---|---|
| Repo / SHA / license | [sqlc-dev/sqlc](https://github.com/sqlc-dev/sqlc), `3ad8b20fb02b5bea81591b673da0758b8685d951`, MIT cho repo; generator/plugin/dịch vụ kiểm riêng |
| Đã đọc | README/LICENSE, `diff.go`, `vet.go`, `verify.go`, hướng dẫn vet/CLI và CI; chưa generate hoặc kết nối DB |
| Cơ chế | `diff` gọi Generate, so các file đầu ra với file hiện có và trả lỗi khi thiếu/khác; không kiểm mọi file thừa trong thư mục output. `vet` dùng rule CEL; một số rule EXPLAIN cần kết nối DB. |
| Điểm dễ hiểu nhầm | `verify` khởi tạo client theo cấu hình cloud và lấy query sets trước đó; không quảng bá như cổng offline drop-in. `compile`, `diff`, `vet` và compatibility với schema cũ là các phép kiểm riêng. |
| CI | `ci.yml` có build đa OS/arch, unit/end-to-end cùng PostgreSQL/MySQL và các examples; không suy mọi plugin/ngôn ngữ/dialect có cùng độ phủ. |
| Tích hợp | Ghim compiler/generator/config/schema, chạy compile + vet rule thực sự cấu hình + diff, build code và integration với DB cùng version. Review SQL và giới hạn rows/timeout; không log giá trị nhạy cảm. |
| Giới hạn | Typed query không chứng minh row-level authorization, đúng tenant, lock/deadlock hoặc query plan đủ tốt. Rule lint là heuristic; test cardinality/permission/concurrency độc lập. |

**Nguồn hồ sơ:** [README.md](https://github.com/sqlc-dev/sqlc/blob/3ad8b20fb02b5bea81591b673da0758b8685d951/README.md) · [LICENSE](https://github.com/sqlc-dev/sqlc/blob/3ad8b20fb02b5bea81591b673da0758b8685d951/LICENSE) · [internal/cmd/diff.go](https://github.com/sqlc-dev/sqlc/blob/3ad8b20fb02b5bea81591b673da0758b8685d951/internal/cmd/diff.go) · [internal/cmd/vet.go](https://github.com/sqlc-dev/sqlc/blob/3ad8b20fb02b5bea81591b673da0758b8685d951/internal/cmd/vet.go) · [internal/cmd/verify.go](https://github.com/sqlc-dev/sqlc/blob/3ad8b20fb02b5bea81591b673da0758b8685d951/internal/cmd/verify.go) · [docs/howto/vet.md](https://github.com/sqlc-dev/sqlc/blob/3ad8b20fb02b5bea81591b673da0758b8685d951/docs/howto/vet.md) · [docs/reference/cli.md](https://github.com/sqlc-dev/sqlc/blob/3ad8b20fb02b5bea81591b673da0758b8685d951/docs/reference/cli.md) · [.github/workflows/ci.yml](https://github.com/sqlc-dev/sqlc/blob/3ad8b20fb02b5bea81591b673da0758b8685d951/.github/workflows/ci.yml).

<a id="keycloak"></a>

### 3.3. Keycloak: tách xác thực người dùng khỏi quyền trên tài nguyên

| Thuộc tính | Giá trị |
|---|---|
| Repo / SHA / license | [keycloak/keycloak](https://github.com/keycloak/keycloak), `2174fdf38731f7191a00240f66fb599e9779005d`, Apache-2.0; theme/provider/dependency xem riêng |
| Đã đọc | README/LICENSE, authorization endpoint/checker, authorization-code grant, PKCE utility, production guide và CI; chưa triển khai OIDC/cluster |
| Cơ chế | Authorization endpoint gọi kiểm redirect và PKCE; checker phân biệt client có/không ép phương thức PKCE. Authorization-code grant gọi nhánh kiểm verifier tương ứng. Có hỗ trợ PKCE không đồng nghĩa mọi client đã ép S256. |
| Production | Guide yêu cầu TLS, hostname/proxy đúng, database production và cấu hình vận hành; `start-dev` trong quickstart không là cấu hình phát hành. Readiness phải phân biệt liveness khi bootstrap/migration đang chạy. |
| CI | CI có các nhánh điều kiện; `conformance.yml` là workflow dispatch cho các suite nêu trong file. Không coi tên conformance là bằng chứng mọi flow/provider đạt chứng nhận hoặc đã pass tại SHA này. |
| Tích hợp | Dùng thư viện OIDC chuẩn, ghim issuer/client/redirect/scopes; public client chọn Authorization Code + PKCE S256, kiểm state/nonce theo flow. API xác minh signature, issuer, audience, expiry và scope; quyền từng resource/tenant vẫn do app/policy kiểm. |
| Giới hạn | Session revocation, refresh-token rotation, key rotation, account recovery và admin access cần policy/test riêng; realm/client setup không tự tạo isolation ở database ứng dụng. IdP HA/backup/upgrade tạo một trách nhiệm vận hành mới. |

**Nguồn hồ sơ:** [README.md](https://github.com/keycloak/keycloak/blob/2174fdf38731f7191a00240f66fb599e9779005d/README.md) · [LICENSE.txt](https://github.com/keycloak/keycloak/blob/2174fdf38731f7191a00240f66fb599e9779005d/LICENSE.txt) · [services/src/main/java/org/keycloak/protocol/oidc/endpoints/AuthorizationEndpoint.java](https://github.com/keycloak/keycloak/blob/2174fdf38731f7191a00240f66fb599e9779005d/services/src/main/java/org/keycloak/protocol/oidc/endpoints/AuthorizationEndpoint.java) · [services/src/main/java/org/keycloak/protocol/oidc/endpoints/AuthorizationEndpointChecker.java](https://github.com/keycloak/keycloak/blob/2174fdf38731f7191a00240f66fb599e9779005d/services/src/main/java/org/keycloak/protocol/oidc/endpoints/AuthorizationEndpointChecker.java) · [services/src/main/java/org/keycloak/protocol/oidc/grants/AuthorizationCodeGrantType.java](https://github.com/keycloak/keycloak/blob/2174fdf38731f7191a00240f66fb599e9779005d/services/src/main/java/org/keycloak/protocol/oidc/grants/AuthorizationCodeGrantType.java) · [services/src/main/java/org/keycloak/protocol/oidc/utils/PkceUtils.java](https://github.com/keycloak/keycloak/blob/2174fdf38731f7191a00240f66fb599e9779005d/services/src/main/java/org/keycloak/protocol/oidc/utils/PkceUtils.java) · [docs/guides/server/configuration-production.adoc](https://github.com/keycloak/keycloak/blob/2174fdf38731f7191a00240f66fb599e9779005d/docs/guides/server/configuration-production.adoc) · [.github/workflows/ci.yml](https://github.com/keycloak/keycloak/blob/2174fdf38731f7191a00240f66fb599e9779005d/.github/workflows/ci.yml) · [.github/workflows/conformance.yml](https://github.com/keycloak/keycloak/blob/2174fdf38731f7191a00240f66fb599e9779005d/.github/workflows/conformance.yml).

## 4. Tuyến tích hợp cho một sản phẩm nhiều khách hàng

1. **Domain trước framework:** mô tả entity, invariant, boundary transaction, loại dữ liệu nhạy cảm, RPO/RTO và tenant model. Chọn shared tables/schema-per-tenant/database-per-tenant theo mức cô lập; tenant context lấy từ principal/quyền đã xác minh, không tin tùy ý header/body.
2. **Một thay đổi schema có hai thế hệ app:** thêm cột/index tương thích, deploy code đọc/ghi chuyển tiếp, backfill có checkpoint/throttle, kiểm xong rồi mới bỏ trường cũ. Bảng migration lưu version/checksum/runner; test nâng từ version đang hỗ trợ và khóa/timeout trên dữ liệu có kích thước đại diện.
3. **SQL/query cùng revision:** compiler + configured rules + generated diff, build và integration. Fixture âm phải có tenant khác, ID đoán được, NULL, boundary date/decimal, concurrent update, race/unique constraint. Với DB row-level policy, test bằng role thật của app, tránh tài khoản owner/admin che lỗ hổng.
4. **Identity khác authorization:** test login chuẩn/thiếu PKCE/sai redirect/sai issuer/audience/expired token; kiểm ma trận subject × action × resource × tenant và revoke. Quyền đọc, ghi, export, background jobs và search index đều phải cùng boundary.
5. **Giao dịch khác giao nhận event:** ghi business row và outbox trong cùng transaction; dispatcher retry, consumer dùng inbox/idempotency key hoặc unique business key. Tiêm crash sau external side effect nhưng trước ACK, replay và out-of-order; giữ event version, trace/correlation và dead-letter có người xử lý. Webhook cần kiểm chữ ký trên raw body theo provider, timestamp/replay window và secret rotation.
6. **Vận hành và xóa:** backup rồi restore kiểm số liệu/quyền thực tế, quyền DB tối thiểu, pool/backpressure, timeout/cancellation và load test; diễn tập xóa tenant qua primary/replica/search/cache/queue/backup theo retention đã cam kết. Nối [30](../30-software-testing-quality/README.md), [31](../31-software-supply-chain-security/README.md), [32](../32-platform-delivery-engineering/README.md), [33](../33-reliability-observability-operations/README.md).

## 5. Bộ bằng chứng bàn giao

| Artifact | Điều cần đối chiếu | Vì sao một badge chưa đủ |
|---|---|---|
| Schema/migration manifest | App revision, DB engine/version, compatible range, lock/backfill result | Migration pass trên DB rỗng chưa chứng minh upgrade production |
| Query/codegen report | Query+schema+generator hash, configured vet rules, generated diff, DB tests | Zero rule hoặc zero query không là phép kiểm hữu ích |
| Identity/policy report | Issuer/client/model ID, allow/deny/revoke/tenant fixture, key-rotation result | Token hợp lệ chưa chứng minh có quyền với resource |
| Event delivery report | Key/version, crash points, duplicate/reorder/replay và side-effect count | Retry thành công chưa chứng minh không ghi tiền/email hai lần |
| Recovery report | Backup revision, restore timestamp, data/permission checks, RPO/RTO đạt | Có file backup chưa chứng minh dữ liệu phục hồi dùng được |

Ngưỡng chấp nhận phải gắn nghiệp vụ và dữ liệu đại diện; chưa có số benchmark, kết quả chạy hoặc SLA được chứng minh trong đợt đọc mã này.

## 6. Kỹ thuật đáng học từ nhóm dẫn đầu The $12 Server Challenge (twelve-dollar-server-challenge, đọc README bài dự thi 4/11/2026)

> Nguồn: bài người dùng gửi về cuộc thi của Arjay McCandless, đối chiếu repo https://github.com/arjaythedev/twelve-dollar-server-challenge (MIT) tại `b7b7b651fe243b0417ae82b3bfc1fc4beb53c456`: luật trong `README.md`, `SPEC.md`, bảng `LEADERBOARD.md` và README của bốn bài dẫn đầu trong `submissions/`. Mục này chỉ ghi các kỹ thuật mạnh nhất đã được chấm. **Không chạy bài dự thi nào.**

### 6.1 Bài toán và luật: một chuẩn đo tốt

- Social Media API (feed 20 bài mới nhất kèm tác giả và số like, mở bài, đăng bài, like, health) trên **SQLite in-process**, seed 50k user, 500k bài, 2 triệu like; server 1 vCPU / 2 GB.
- Luật giữ cho bài đo trung thực: không cache kết quả hay bảng trong RAM; **verify chữ ký JWT ở mọi request**; ghi phải **commit trước khi trả lời** (WAL, `synchronous=NORMAL` trở lên). Được phép **group commit** (gom ghi nhiều request vào một transaction, mỗi request chờ commit) và đọc qua **B-tree/cursor API của chính SQLite** (phán quyết 31/10/2026).
- Điểm = số user ảo giữ được 5 phút với p95 < 500 ms, p99 < 1 s, lỗi < 1%; mỗi lần đo khởi động lại app trên DB mới.

### 6.2 Nhóm dẫn đầu (LEADERBOARD.md, 4/11/2026)

| # | Bài | Ngôn ngữ | User giữ 5 phút | req/s | p95 / p99 ms | RAM MB |
|---|---|---|---:|---:|---|---:|
| 1 | `rust-iouring-kensac` | Rust | 310.000 | 29.284 | 62 / 190 | 1.114 |
| 2 | `mojo-iouring-oh-meh` | Mojo | 304.000 | 28.705 | 159 / 545 | 726 |
| 3 | `c-iouring-pavlyhalim` | C | 295.000 | 28.013 | 28 / 117 | 1.536 |
| 4 | `rust-native-scooter1337` | Rust | 290.000 | 27.580 | 26,5 / 514 | 1.035 |
| 5 | `lean-verified-soonhokong` | Lean 4 | 280.000 | 26.738 | 40,6 / 188 | 1.446 |

Cả nhóm có 0% lỗi và khoảng 25–31 µs CPU mỗi request, tức một lõi phục vụ gần 30.000 request/giây trong khi vẫn verify JWT và commit ghi xuống đĩa.

### 6.3 Kỹ thuật chung của nhóm dẫn đầu

**Kết nối (mỗi user là một kết nối keep-alive)**

- **io_uring direct descriptors**: socket nằm trong bảng file cố định của ring thay vì bảng fd của process, nên `LimitNOFILE=65535` chỉ giới hạn một ring. Bài C hạng 3 dùng tới 8 ring × 65.471 slot (trên 500.000 kết nối); bài Mojo mở ring dần, tối đa 16.
- **Nhiều listener `SO_REUSEPORT`** (bài C hạng 3: 8 listener): mỗi listener có hàng đợi accept riêng (`somaxconn` 4.096), cộng lại giữ khoảng 32.000 kết nối chờ khi server bận. Với một listener, một lần chạy ghi nhận 1,8 triệu lần tràn hàng đợi; với tám listener thì không có lần nào khi tăng tới 160.000 user.
- **Kết nối rảnh gần như không tốn gì**: chỉ một bản ghi 40–64 byte, không giữ buffer. Bài C hạng 3 dùng multishot poll và một hàng đợi đọc, cấp buffer từ provided-buffer ring khi có dữ liệu, nên chịu được cơn dồn tải mà không cạn buffer.

**Vòng lặp và xử lý theo lô**

- **Một luồng** chạy event loop, HTTP/1.1, JSON, HS256 và đọc SQLite; ring đặt `SINGLE_ISSUER`, `DEFER_TASKRUN`; nhận dữ liệu bằng multishot receive vào provided buffers.
- **Lô tự hình thành khi bận**: một vòng lặp xử lý nhiều completion rồi mới submit và chờ một lần, nên chi phí syscall được chia cho nhiều request.
- **Không cấp phát trên đường xử lý**: parse request tại chỗ, ghi response vào arena của lô và tái dùng khi lần gửi cuối hoàn tất, dựng sẵn các response lỗi cố định lúc khởi động, dùng pool buffer.

**Đọc dữ liệu**

- **Đọc qua B-tree cursor của SQLite gốc** (amalgamation 3.54.1, không vá, ghim SHA-256): bỏ qua bytecode engine, giải mã bytes của record và ghi thẳng ra JSON.
- **Feed theo đúng index**: duyệt `posts_created_at_id_idx` (`created_at DESC, id DESC`), tương đương đúng `ORDER BY` của truy vấn chuẩn; tra 20 bài theo id tăng dần để các id liền nhau rơi vào cùng lá B-tree; đếm like bằng một lần quét đoạn trên `likes_post_id_idx` khi các id gần nhau (trong khoảng 512), còn không thì seek từng bài.
- **Đúng với mọi dữ liệu**: không giả định id liên tiếp hay timestamp theo id; nếu gặp trường hợp mà truy vấn SQL chuẩn sẽ xử lý khác (ví dụ bài không có user), dùng truy vấn SQL chuẩn; khi khởi động kiểm thứ tự cột của từng bảng và index cần giải mã, sai schema thì từ chối chạy.

**Ghi và độ bền**

- **Ghi bằng SQL đã prepare** (`INSERT … RETURNING`, `ON CONFLICT DO NOTHING`) với **group commit**: một transaction cho mỗi lô (bài C hạng 3), hoặc gom 20 ms rồi chạy tối đa 1.024 request (bài Rust hạng 4); response chỉ gửi sau khi commit thành công, commit lỗi thì đổi thành response lỗi.
- **WAL `synchronous=NORMAL` + VFS `unix-excl`**: process khóa độc quyền file, WAL index nằm trong heap dùng chung cho các connection của process, không cần file `-shm` và không khóa file mỗi transaction.
- **Checkpoint tách khỏi đường phục vụ**: một luồng hoặc connection riêng chạy checkpoint PASSIVE ở độ ưu tiên thấp (nice 19).

**Build tái lập**

- SQLite amalgamation và các phụ thuộc được ghim phiên bản và kiểm SHA-256 trong `build.sh`/`install.sh`; build `-O3 -march=native`, có bài dùng PGO huấn luyện trên database tổng hợp lúc build.

### 6.4 Mang về dự án thật

1. **Group commit có giới hạn lô hoặc thời gian chờ**: giữ cam kết "commit rồi mới trả lời" mà vẫn chia chi phí fsync.
2. **Checkpoint WAL ở luồng hoặc connection riêng**, độ ưu tiên thấp.
3. **`SO_REUSEPORT` với nhiều listener** và theo dõi tràn hàng đợi accept khi có nhiều kết nối keep-alive.
4. **Giữ kết nối rảnh thật nhẹ** (không buffer, bản ghi nhỏ) và cấp buffer khi có dữ liệu.
5. **Feed đi đúng index phủ thứ tự sắp xếp**; kiểm bằng `EXPLAIN QUERY PLAN`; đếm theo khoảng khi id gần nhau.
6. **Serialize thẳng vào buffer, không dựng object trung gian**; dựng sẵn response cố định.
7. **Ghim phiên bản và kiểm SHA-256** cho thư viện native (SQLite) trong script build.

**Nguồn §6:** bài người dùng gửi 4/11/2026 · clone `--depth 1` https://github.com/arjaythedev/twelve-dollar-server-challenge HEAD `b7b7b651fe243b0417ae82b3bfc1fc4beb53c456`: https://github.com/arjaythedev/twelve-dollar-server-challenge/blob/b7b7b651fe243b0417ae82b3bfc1fc4beb53c456/README.md · https://github.com/arjaythedev/twelve-dollar-server-challenge/blob/b7b7b651fe243b0417ae82b3bfc1fc4beb53c456/SPEC.md · https://github.com/arjaythedev/twelve-dollar-server-challenge/blob/b7b7b651fe243b0417ae82b3bfc1fc4beb53c456/LEADERBOARD.md · https://github.com/arjaythedev/twelve-dollar-server-challenge/blob/b7b7b651fe243b0417ae82b3bfc1fc4beb53c456/submissions/rust-iouring-kensac/README.md · https://github.com/arjaythedev/twelve-dollar-server-challenge/blob/b7b7b651fe243b0417ae82b3bfc1fc4beb53c456/submissions/mojo-iouring-oh-meh/README.md · https://github.com/arjaythedev/twelve-dollar-server-challenge/blob/b7b7b651fe243b0417ae82b3bfc1fc4beb53c456/submissions/c-iouring-pavlyhalim/README.md · https://github.com/arjaythedev/twelve-dollar-server-challenge/blob/b7b7b651fe243b0417ae82b3bfc1fc4beb53c456/submissions/rust-native-scooter1337/README.md · https://benchmarks.arjaythedev.com/12-dollar-server/leaderboard.

## Nguồn và giới hạn kiểm chứng

Nguồn ở §3 cố định full SHA cho đường mã, LICENSE và CI đã đọc. Không ghi sao vì GitHub search API bị trả Forbidden trong phiên, không dùng số cũ làm số hiện tại và không suy archive từ clone thành công. Các tiêu chí §1/§4/§5 là thiết kế tổng hợp của kho; công cụ phải được thử trên project, DB và threat model thực tế trước tích hợp.

<a id="anhkysuai-2026-11-23"></a>

## Đánh giá từ kho Anh Kỹ Sư AI — 23/11/2026

Phần này có **100 hồ sơ hoặc phạm vi đối chiếu** từ [nguồn tuyển chọn](https://anhkysuai.com/kho/). [Bảng đủ 1.295 repo](../data/collections/anhkysuai-kho.json) ghi trạng thái đối chiếu từng link; [danh sách URL](../data/collections/anhkysuai-kho-links.txt) phục vụ tra cứu. Nguồn tuyển chọn giúp phát hiện repo; đánh giá bên dưới dựa trên clone và permalink upstream cùng metadata GitHub ngày 2026-11-23.

Mức `docs-read`/`code-read` chỉ áp dụng phạm vi ghi tại mỗi hồ sơ. Chưa cài, build, chạy test hay benchmark mã upstream. Giấy phép có thể tách theo code, model, nội dung, asset hoặc bản enterprise; con số/tuyên bố của tác giả chưa được tái lập nếu không có ghi chú khác.

<a id="anhkysuai-dani-garcia-vaultwarden"></a>

### Vaultwarden

**Đã chuyển (2026-11-23):** hồ sơ này nay nằm ở [mục 36](../36-self-hosting-homelab/README.md#anhkysuai-dani-garcia-vaultwarden); catalog con xem [catalog/](../catalog/README.md).

<a id="anhkysuai-socketio-socket.io"></a>

### Socket.IO

**Repo:** [socketio/socket.io](https://github.com/socketio/socket.io) · **License:** MIT · **Kiểm:** 2026-11-23, `docs-read`, [`0e247793ee17`](https://github.com/socketio/socket.io/tree/0e247793ee17f8461a5c542c4f904a628150d30b) (commit 2026-11-20). **Sao:** 63,266 tại 2026-11-23 theo [GitHub API](https://api.github.com/repos/socketio/socket.io).

| Mục | Đánh giá |
|---|---|
| Mục đích | Hệ thư viện client/server cho giao tiếp sự kiện thời gian thực. |
| Giá trị và cơ chế theo tài liệu | Monorepo tách Engine.IO, parser, client, adapter và emitter; CI riêng của Engine.IO biên dịch và kiểm các biến thể transport. |
| Giới hạn | README gốc chủ yếu dẫn tài liệu. Việc có adapter không tự chứng minh giao hàng đúng một lần hoặc lưu bền sự kiện; ứng dụng vẫn cần thiết kế xác thực và đồng bộ lại. |
| Điều kiện tích hợp | Chọn client/server cùng phiên bản, đọc adapter cho mô hình nhiều node và bổ sung hợp đồng sự kiện cùng kiểm mất kết nối. |
| Lựa chọn đối chiếu | ws; NATS; LiveKit. |

**Phạm vi bằng chứng:** đã clone, đọc trích đoạn tài liệu, giấy phép và các file cấu hình được dẫn dưới đây; chưa chạy mã, build, benchmark hoặc test upstream. `docs-read` không phải kiểm chứng implementation.

**Nguồn tại cùng SHA:** [README.md](https://github.com/socketio/socket.io/blob/0e247793ee17f8461a5c542c4f904a628150d30b/README.md) · [LICENSE](https://github.com/socketio/socket.io/blob/0e247793ee17f8461a5c542c4f904a628150d30b/LICENSE) · [package.json](https://github.com/socketio/socket.io/blob/0e247793ee17f8461a5c542c4f904a628150d30b/package.json) · [.github/workflows/ci-engine.io.yml](https://github.com/socketio/socket.io/blob/0e247793ee17f8461a5c542c4f904a628150d30b/.github/workflows/ci-engine.io.yml).

<a id="anhkysuai-twentyhq-twenty"></a>

### Twenty

**Repo:** [twentyhq/twenty](https://github.com/twentyhq/twenty) · **License:** AGPL-3.0; phần Enterprise thương mại; một số gói MIT · **Kiểm:** 2026-11-23, `docs-read`, [`0bd6a66fd4c3`](https://github.com/twentyhq/twenty/tree/0bd6a66fd4c3156a2a349723785c2d4a9347c766) (commit 2026-11-23). **Sao:** 61,355 tại 2026-11-23 theo [GitHub API](https://api.github.com/repos/twentyhq/twenty).

| Mục | Đánh giá |
|---|---|
| Mục đích | CRM cho đội kỹ thuật, cho phép khai báo đối tượng, trường và view qua SDK rồi phát hành thành app. |
| Giá trị và cơ chế theo tài liệu | README có ví dụ defineObject và CLI app publish; monorepo tách UI/SDK cùng các cổng kiểm chuyên biệt. |
| Giới hạn | LICENSE nêu ngoại lệ thương mại và gói mang giấy phép khác; không coi toàn repo là AGPL hoặc MIT thuần. Chưa kiểm quyền theo workspace hay đồng bộ dữ liệu thực tế. |
| Điều kiện tích hợp | Dùng API/SDK và workspace thử; xác định giấy phép đúng thư mục định tái sử dụng, rồi kiểm schema migration và quyền dữ liệu CRM. |
| Lựa chọn đối chiếu | Odoo; [ERPNext](../34-backend-data-identity-integration/README.md#anhkysuai-frappe-erpnext); SuiteCRM. |

**Phạm vi bằng chứng:** đã clone, đọc trích đoạn tài liệu, giấy phép và các file cấu hình được dẫn dưới đây; chưa chạy mã, build, benchmark hoặc test upstream. `docs-read` không phải kiểm chứng implementation.

**Nguồn tại cùng SHA:** [README.md](https://github.com/twentyhq/twenty/blob/0bd6a66fd4c3156a2a349723785c2d4a9347c766/README.md) · [LICENSE](https://github.com/twentyhq/twenty/blob/0bd6a66fd4c3156a2a349723785c2d4a9347c766/LICENSE) · [package.json](https://github.com/twentyhq/twenty/blob/0bd6a66fd4c3156a2a349723785c2d4a9347c766/package.json) · [.github/workflows/ci-ui.yaml](https://github.com/twentyhq/twenty/blob/0bd6a66fd4c3156a2a349723785c2d4a9347c766/.github/workflows/ci-ui.yaml).

<a id="anhkysuai-appwrite-appwrite"></a>

### Appwrite

**Repo:** [appwrite/appwrite](https://github.com/appwrite/appwrite) · **License:** BSD-3-Clause · **Kiểm:** 2026-11-23, `docs-read`, [`647058d7e5cb`](https://github.com/appwrite/appwrite/tree/647058d7e5cb3df5e57e01490b7f838bc87a168c) (commit 2026-11-23). **Sao:** 58,614 tại 2026-11-23 theo [GitHub API](https://api.github.com/repos/appwrite/appwrite).

| Mục | Đánh giá |
|---|---|
| Mục đích | Nền tảng backend gồm xác thực, dữ liệu, lưu trữ và công cụ cho ứng dụng lẫn agent. |
| Giá trị và cơ chế theo tài liệu | README mô tả SDK và MCP vận hành dự án; repo có PHP cùng workspace Rust, CI phân luồng theo thay đổi và quét phụ thuộc. |
| Giới hạn | Kết nối agent có thể thao tác tài nguyên thật; tuyên bố scale hoặc bảo mật trong README chưa được tái lập. Quyền API và khác biệt cloud/tự host cần xem theo phiên bản. |
| Điều kiện tích hợp | Bắt đầu với project thử và khóa quyền hẹp; kiểm auth, quyền từng tài nguyên, backup và nâng cấp trước khi dùng dữ liệu thật. |
| Lựa chọn đối chiếu | Supabase; PocketBase; [Parse Server](../34-backend-data-identity-integration/README.md#anhkysuai-parse-community-parse-server). |

**Phạm vi bằng chứng:** đã clone, đọc trích đoạn tài liệu, giấy phép và các file cấu hình được dẫn dưới đây; chưa chạy mã, build, benchmark hoặc test upstream. `docs-read` không phải kiểm chứng implementation.

**Nguồn tại cùng SHA:** [README.md](https://github.com/appwrite/appwrite/blob/647058d7e5cb3df5e57e01490b7f838bc87a168c/README.md) · [LICENSE](https://github.com/appwrite/appwrite/blob/647058d7e5cb3df5e57e01490b7f838bc87a168c/LICENSE) · [package.json](https://github.com/appwrite/appwrite/blob/647058d7e5cb3df5e57e01490b7f838bc87a168c/package.json) · [Cargo.toml](https://github.com/appwrite/appwrite/blob/647058d7e5cb3df5e57e01490b7f838bc87a168c/Cargo.toml) · [.github/workflows/ci.yml](https://github.com/appwrite/appwrite/blob/647058d7e5cb3df5e57e01490b7f838bc87a168c/.github/workflows/ci.yml).

<a id="anhkysuai-odoo-odoo"></a>

### Odoo Community

**Repo:** [odoo/odoo](https://github.com/odoo/odoo) · **License:** LGPL-3.0; thành phần bên thứ ba theo giấy phép riêng · **Kiểm:** 2026-11-23, `docs-read`, [`dfd7e0c411d4`](https://github.com/odoo/odoo/tree/dfd7e0c411d45f50395b8cff09379ad6322b8bc8) (commit 2026-11-23). **Sao:** 56,034 tại 2026-11-23 theo [GitHub API](https://api.github.com/repos/odoo/odoo).

| Mục | Đánh giá |
|---|---|
| Mục đích | Bộ ứng dụng doanh nghiệp kết hợp CRM, kho, bán hàng, kế toán và các module nghiệp vụ. |
| Giá trị và cơ chế theo tài liệu | README cho thấy có thể dùng ứng dụng riêng hoặc ghép thành ERP; cấu trúc Python/addon là nguồn tham khảo cách mở rộng nghiệp vụ. |
| Giới hạn | Kho cộng đồng không đại diện mọi tính năng Enterprise. Quy tắc thuế/kế toán và bản địa hóa chưa được xác minh; COPYRIGHT lưu ý giấy phép ở từng thành phần. |
| Điều kiện tích hợp | Chọn nhánh phát hành phù hợp, thử module trên dữ liệu giả lập và kiểm migration, quyền truy cập, sao lưu trước khi kết nối vận hành doanh nghiệp. |
| Lựa chọn đối chiếu | [ERPNext](../34-backend-data-identity-integration/README.md#anhkysuai-frappe-erpnext); Dolibarr; Tryton. |

**Phạm vi bằng chứng:** đã clone, đọc trích đoạn tài liệu, giấy phép và các file cấu hình được dẫn dưới đây; chưa chạy mã, build, benchmark hoặc test upstream. `docs-read` không phải kiểm chứng implementation.

**Nguồn tại cùng SHA:** [README.md](https://github.com/odoo/odoo/blob/dfd7e0c411d45f50395b8cff09379ad6322b8bc8/README.md) · [COPYRIGHT](https://github.com/odoo/odoo/blob/dfd7e0c411d45f50395b8cff09379ad6322b8bc8/COPYRIGHT) · [LICENSE](https://github.com/odoo/odoo/blob/dfd7e0c411d45f50395b8cff09379ad6322b8bc8/LICENSE).

<a id="anhkysuai-tryghost-ghost"></a>

### Ghost

**Repo:** [TryGhost/Ghost](https://github.com/TryGhost/Ghost) · **License:** MIT · **Kiểm:** 2026-11-23, `docs-read`, [`46529412e782`](https://github.com/TryGhost/Ghost/tree/46529412e7829c202f0b55b073ff497e41b278ae) (commit 2026-11-23). **Sao:** 55,885 tại 2026-11-23 theo [GitHub API](https://api.github.com/repos/TryGhost/Ghost).

| Mục | Đánh giá |
|---|---|
| Mục đích | Nền tảng xuất bản nội dung, có CLI tự host, theme và API nội dung. |
| Giá trị và cơ chế theo tài liệu | README dẫn quy trình cài local hoặc máy chủ và tách managed hosting; manifest nêu runtime Node cùng monorepo Nx. |
| Giới hạn | Tài liệu cài nhanh không thay kiểm gửi email, backup và nâng cấp; chưa chạy instance hay đo khả năng phục vụ. Dịch vụ Ghost(Pro) có điều kiện riêng với mã MIT. |
| Điều kiện tích hợp | Dùng bản phát hành qua Ghost CLI, thử theme và Content API; kiểm cấu hình email, khôi phục dữ liệu và đường nâng cấp. |
| Lựa chọn đối chiếu | WordPress; [Wagtail](../34-backend-data-identity-integration/README.md#anhkysuai-wagtail-wagtail); [Strapi](../08-awesome-lists-learning/README.md#6c59-framework-backend). |

**Phạm vi bằng chứng:** đã clone, đọc trích đoạn tài liệu, giấy phép và các file cấu hình được dẫn dưới đây; chưa chạy mã, build, benchmark hoặc test upstream. `docs-read` không phải kiểm chứng implementation.

**Nguồn tại cùng SHA:** [README.md](https://github.com/TryGhost/Ghost/blob/46529412e7829c202f0b55b073ff497e41b278ae/README.md) · [LICENSE](https://github.com/TryGhost/Ghost/blob/46529412e7829c202f0b55b073ff497e41b278ae/LICENSE) · [package.json](https://github.com/TryGhost/Ghost/blob/46529412e7829c202f0b55b073ff497e41b278ae/package.json) · [.github/workflows/ci.yml](https://github.com/TryGhost/Ghost/blob/46529412e7829c202f0b55b073ff497e41b278ae/.github/workflows/ci.yml).

<a id="anhkysuai-etcd-io-etcd"></a>

### etcd

**Repo:** [etcd-io/etcd](https://github.com/etcd-io/etcd) · **License:** Apache-2.0 · **Kiểm:** 2026-11-23, `docs-read`, [`a99e920890e0`](https://github.com/etcd-io/etcd/tree/a99e920890e0b9df77825c30e6a7a9b3bc06c324) (commit 2026-11-22). **Sao:** 52,650 tại 2026-11-23 theo [GitHub API](https://api.github.com/repos/etcd-io/etcd).

| Mục | Đánh giá |
|---|---|
| Mục đích | Kho khóa-giá trị phân tán dùng Raft cho dữ liệu điều phối quan trọng. |
| Giá trị và cơ chế theo tài liệu | README dẫn API gRPC và bộ robustness testing; monorepo tách client, server, API và công cụ vận hành. |
| Giới hạn | README cảnh báo main có thể không ổn định. Con số hiệu năng trong tài liệu chưa được tái lập; quorum, TLS và phục hồi snapshot là trách nhiệm cấu hình/vận hành. |
| Điều kiện tích hợp | Dùng bản phát hành ổn định, thử mất node và phục hồi trước khi làm nền cho khóa phân tán hoặc cấu hình hệ thống. |
| Lựa chọn đối chiếu | [Consul](../34-backend-data-identity-integration/README.md#anhkysuai-hashicorp-consul); ZooKeeper; PostgreSQL advisory locks. |

**Phạm vi bằng chứng:** đã clone, đọc trích đoạn tài liệu, giấy phép và các file cấu hình được dẫn dưới đây; chưa chạy mã, build, benchmark hoặc test upstream. `docs-read` không phải kiểm chứng implementation.

**Nguồn tại cùng SHA:** [README.md](https://github.com/etcd-io/etcd/blob/a99e920890e0b9df77825c30e6a7a9b3bc06c324/README.md) · [LICENSE](https://github.com/etcd-io/etcd/blob/a99e920890e0b9df77825c30e6a7a9b3bc06c324/LICENSE) · [go.mod](https://github.com/etcd-io/etcd/blob/a99e920890e0b9df77825c30e6a7a9b3bc06c324/go.mod) · [.github/workflows/antithesis-test.yml](https://github.com/etcd-io/etcd/blob/a99e920890e0b9df77825c30e6a7a9b3bc06c324/.github/workflows/antithesis-test.yml).

<a id="anhkysuai-clickhouse-clickhouse"></a>

### ClickHouse

**Repo:** [ClickHouse/ClickHouse](https://github.com/ClickHouse/ClickHouse) · **License:** Apache-2.0 · **Kiểm:** 2026-11-23, `docs-read`, [`2ced6e923a0a`](https://github.com/ClickHouse/ClickHouse/tree/2ced6e923a0a365ca9632d5a2891813bd4bbb928) (commit 2026-11-23). **Sao:** 51,073 tại 2026-11-23 theo [GitHub API](https://api.github.com/repos/ClickHouse/ClickHouse).

| Mục | Đánh giá |
|---|---|
| Mục đích | Hệ quản trị dữ liệu hướng phân tích, có bản tự host và dịch vụ cloud. |
| Giá trị và cơ chế theo tài liệu | Cây repo và CMake thể hiện hệ C++ lớn với kiểm cấu hình build; tài liệu dẫn tutorial, vận hành cluster và các phiên bản phát hành. |
| Giới hạn | README thiên về điểm bắt đầu và release; chưa benchmark query hoặc xác minh cấu hình replication. Dịch vụ cloud và tùy chọn build riêng không được suy từ bản mã công khai. |
| Điều kiện tích hợp | Đánh giá schema, kiểu truy vấn và vòng đời dữ liệu với dữ liệu đại diện; ghim release và thử backup/restore khi tự host. |
| Lựa chọn đối chiếu | Apache Druid; DuckDB; Apache Doris. |

**Phạm vi bằng chứng:** đã clone, đọc trích đoạn tài liệu, giấy phép và các file cấu hình được dẫn dưới đây; chưa chạy mã, build, benchmark hoặc test upstream. `docs-read` không phải kiểm chứng implementation.

**Nguồn tại cùng SHA:** [README.md](https://github.com/ClickHouse/ClickHouse/blob/2ced6e923a0a365ca9632d5a2891813bd4bbb928/README.md) · [LICENSE](https://github.com/ClickHouse/ClickHouse/blob/2ced6e923a0a365ca9632d5a2891813bd4bbb928/LICENSE) · [pyproject.toml](https://github.com/ClickHouse/ClickHouse/blob/2ced6e923a0a365ca9632d5a2891813bd4bbb928/pyproject.toml) · [CMakeLists.txt](https://github.com/ClickHouse/ClickHouse/blob/2ced6e923a0a365ca9632d5a2891813bd4bbb928/CMakeLists.txt) · [.github/workflows/weekly_official_docker.yml](https://github.com/ClickHouse/ClickHouse/blob/2ced6e923a0a365ca9632d5a2891813bd4bbb928/.github/workflows/weekly_official_docker.yml).

<a id="anhkysuai-prisma-orm"></a>

### Prisma ORM 8

**Repo:** [prisma/orm](https://github.com/prisma/orm) · **License:** Apache-2.0 · **Kiểm:** 2026-11-23, `docs-read`, [`e023771490d3`](https://github.com/prisma/orm/tree/e023771490d318a8586017871db80d4cc9f618d5) (commit 2026-11-23). **Sao:** 47,694 tại 2026-11-23 theo [GitHub API](https://api.github.com/repos/prisma/orm).

| Mục | Đánh giá |
|---|---|
| Mục đích | ORM viết lại bằng TypeScript, nhấn mạnh khả năng mở rộng và kết hợp cho ứng dụng dữ liệu. |
| Giá trị và cơ chế theo tài liệu | README mô tả scaffold với nhiều framework và PostgreSQL/MongoDB; manifest tại SHA là 8.0.0-rc.25, yêu cầu Node 24 trở lên. |
| Giới hạn | Đây là release candidate, tài liệu nêu có thể còn breaking change và bảng khoảng trống. Không coi nhánh main là Prisma 7 ổn định hoặc suy tính năng đầy đủ từ tên ORM. |
| Điều kiện tích hợp | Dùng môi trường thử và đọc scorecard/upgrade recipe; ứng dụng hiện hữu cần đối chiếu nhánh v7 và kiểm migration trên bản sao dữ liệu. |
| Lựa chọn đối chiếu | Drizzle ORM; TypeORM; Kysely. |

**Phạm vi bằng chứng:** đã clone, đọc trích đoạn tài liệu, giấy phép và các file cấu hình được dẫn dưới đây; chưa chạy mã, build, benchmark hoặc test upstream. `docs-read` không phải kiểm chứng implementation.

**Nguồn tại cùng SHA:** [README.md](https://github.com/prisma/orm/blob/e023771490d318a8586017871db80d4cc9f618d5/README.md) · [LICENSE](https://github.com/prisma/orm/blob/e023771490d318a8586017871db80d4cc9f618d5/LICENSE) · [package.json](https://github.com/prisma/orm/blob/e023771490d318a8586017871db80d4cc9f618d5/package.json) · [.github/workflows/ci.yml](https://github.com/prisma/orm/blob/e023771490d318a8586017871db80d4cc9f618d5/.github/workflows/ci.yml).

<a id="anhkysuai-fastapi-full-stack-fastapi-template"></a>

### Full Stack FastAPI Template

**Repo:** [fastapi/full-stack-fastapi-template](https://github.com/fastapi/full-stack-fastapi-template) · **License:** MIT · **Kiểm:** 2026-11-23, `docs-read`, [`77e550a73bb4`](https://github.com/fastapi/full-stack-fastapi-template/tree/77e550a73bb49dd2967622c5ed11bf7a49603c93) (commit 2026-11-16). **Sao:** 46,322 tại 2026-11-23 theo [GitHub API](https://api.github.com/repos/fastapi/full-stack-fastapi-template).

| Mục | Đánh giá |
|---|---|
| Mục đích | Mẫu full-stack FastAPI, SQLModel/PostgreSQL và frontend React phục vụ cùng miền. |
| Giá trị và cơ chế theo tài liệu | README gắn client sinh tự động, JWT, phục hồi mật khẩu, Pytest/Playwright và Compose; workflow backend dựng dịch vụ rồi migration trước kiểm thử. |
| Giới hạn | Mẫu không tự bảo đảm cấu hình an toàn của sản phẩm mới; dữ liệu bí mật, quyền nghiệp vụ và migration riêng vẫn cần thiết kế. Chưa chạy test upstream. |
| Điều kiện tích hợp | Fork vào repo sản phẩm, thay cấu hình mẫu và thêm kiểm theo yêu cầu nghiệp vụ; giữ liên kết schema API với client và kiểm nâng cấp dependency. |
| Lựa chọn đối chiếu | Cookiecutter Django; JHipster; NestJS starter. |

**Phạm vi bằng chứng:** đã clone, đọc trích đoạn tài liệu, giấy phép và các file cấu hình được dẫn dưới đây; chưa chạy mã, build, benchmark hoặc test upstream. `docs-read` không phải kiểm chứng implementation.

**Nguồn tại cùng SHA:** [README.md](https://github.com/fastapi/full-stack-fastapi-template/blob/77e550a73bb49dd2967622c5ed11bf7a49603c93/README.md) · [LICENSE](https://github.com/fastapi/full-stack-fastapi-template/blob/77e550a73bb49dd2967622c5ed11bf7a49603c93/LICENSE) · [package.json](https://github.com/fastapi/full-stack-fastapi-template/blob/77e550a73bb49dd2967622c5ed11bf7a49603c93/package.json) · [pyproject.toml](https://github.com/fastapi/full-stack-fastapi-template/blob/77e550a73bb49dd2967622c5ed11bf7a49603c93/pyproject.toml) · [.github/workflows/test-backend.yml](https://github.com/fastapi/full-stack-fastapi-template/blob/77e550a73bb49dd2967622c5ed11bf7a49603c93/.github/workflows/test-backend.yml).

<a id="anhkysuai-payloadcms-payload"></a>

### Payload CMS

**Repo:** [payloadcms/payload](https://github.com/payloadcms/payload) · **License:** MIT · **Kiểm:** 2026-11-23, `docs-read`, [`ce66418fcf86`](https://github.com/payloadcms/payload/tree/ce66418fcf8617a215139aaf67fe161bda13c272) (commit 2026-11-21). **Sao:** 45,965 tại 2026-11-23 theo [GitHub API](https://api.github.com/repos/payloadcms/payload).

| Mục | Đánh giá |
|---|---|
| Mục đích | CMS headless tích hợp cùng ứng dụng Next.js, có template website và thương mại điện tử. |
| Giá trị và cơ chế theo tài liệu | README chỉ đường starter với live preview, rich-text và deploy Cloudflare/Vercel; repo monorepo có gói core/plugin và cổng audit phụ thuộc. |
| Giới hạn | Manifest nhánh đọc là 4.0.0-beta.11; tuyên bố production-ready của template chưa được kiểm. Chi phí và giới hạn nhà cung cấp cloud là phạm vi riêng. |
| Điều kiện tích hợp | Thử cấu hình collection, quyền field/document và storage adapter trong staging; ghim phiên bản phù hợp thay vì tự động theo main. |
| Lựa chọn đối chiếu | [Strapi](../08-awesome-lists-learning/README.md#6c59-framework-backend); [Directus](../08-awesome-lists-learning/README.md#6c59-framework-backend); [Wagtail](../34-backend-data-identity-integration/README.md#anhkysuai-wagtail-wagtail). |

**Phạm vi bằng chứng:** đã clone, đọc trích đoạn tài liệu, giấy phép và các file cấu hình được dẫn dưới đây; chưa chạy mã, build, benchmark hoặc test upstream. `docs-read` không phải kiểm chứng implementation.

**Nguồn tại cùng SHA:** [README.md](https://github.com/payloadcms/payload/blob/ce66418fcf8617a215139aaf67fe161bda13c272/README.md) · [LICENSE.md](https://github.com/payloadcms/payload/blob/ce66418fcf8617a215139aaf67fe161bda13c272/LICENSE.md) · [package.json](https://github.com/payloadcms/payload/blob/ce66418fcf8617a215139aaf67fe161bda13c272/package.json) · [.github/workflows/audit-dependencies.yml](https://github.com/payloadcms/payload/blob/ce66418fcf8617a215139aaf67fe161bda13c272/.github/workflows/audit-dependencies.yml).

<a id="anhkysuai-juspay-hyperswitch"></a>

### Hyperswitch

**Repo:** [juspay/hyperswitch](https://github.com/juspay/hyperswitch) · **License:** Apache-2.0 · **Kiểm:** 2026-11-23, `docs-read`, [`05f44e282af4`](https://github.com/juspay/hyperswitch/tree/05f44e282af4c86657abc43390b86c493a56e28d) (commit 2026-11-23). **Sao:** 45,874 tại 2026-11-23 theo [GitHub API](https://api.github.com/repos/juspay/hyperswitch).

| Mục | Đánh giá |
|---|---|
| Mục đích | Hạ tầng thanh toán dạng module cho định tuyến, quan sát chi phí và khôi phục giao dịch. |
| Giá trị và cơ chế theo tài liệu | README mô tả các khối vault, retry và kết nối nhà cung cấp; workspace Rust cho phép tìm từng lớp thay vì một tích hợp thanh toán nguyên khối. |
| Giới hạn | Tuyên bố PCI và cải thiện doanh thu trong tài liệu chưa được xác minh. Routing/retry sai có thể tạo tác động tài chính; chưa thực hiện giao dịch hay kiểm bảo mật. |
| Điều kiện tích hợp | Bắt đầu bằng sandbox của nhà cung cấp, chốt idempotency, token hóa và đối soát; kiểm phạm vi dữ liệu thẻ trước khi đưa vào luồng thật. |
| Lựa chọn đối chiếu | Tích hợp trực tiếp Stripe; Adyen; Kill Bill. |

**Phạm vi bằng chứng:** đã clone, đọc trích đoạn tài liệu, giấy phép và các file cấu hình được dẫn dưới đây; chưa chạy mã, build, benchmark hoặc test upstream. `docs-read` không phải kiểm chứng implementation.

**Nguồn tại cùng SHA:** [README.md](https://github.com/juspay/hyperswitch/blob/05f44e282af4c86657abc43390b86c493a56e28d/README.md) · [LICENSE](https://github.com/juspay/hyperswitch/blob/05f44e282af4c86657abc43390b86c493a56e28d/LICENSE) · [Cargo.toml](https://github.com/juspay/hyperswitch/blob/05f44e282af4c86657abc43390b86c493a56e28d/Cargo.toml) · [.github/workflows/CI-pr.yml](https://github.com/juspay/hyperswitch/blob/05f44e282af4c86657abc43390b86c493a56e28d/.github/workflows/CI-pr.yml).

<a id="anhkysuai-apache-dubbo"></a>

### Apache Dubbo

**Repo:** [apache/dubbo](https://github.com/apache/dubbo) · **License:** Apache-2.0; thành phần giao diện có thông báo riêng · **Kiểm:** 2026-11-23, `docs-read`, [`d809bb12c851`](https://github.com/apache/dubbo/tree/d809bb12c851468420a742dfb2aa5c5532c9e024) (commit 2026-11-20). **Sao:** 41,570 tại 2026-11-23 theo [GitHub API](https://api.github.com/repos/apache/dubbo).

| Mục | Đánh giá |
|---|---|
| Mục đích | Khung Java cho dịch vụ RPC và web, có giao thức Triple tương thích gRPC. |
| Giá trị và cơ chế theo tài liệu | README ghép discovery, cân bằng tải, cấu hình lưu lượng, metrics và tracing; Maven/CI cho thấy các bước build cùng kiểm giấy phép. |
| Giới hạn | Hỗ trợ đa ngôn ngữ còn nằm ở các repo khác. Tuyên bố hiệu năng và khả năng tương thích giao thức chưa được kiểm; triển khai vẫn cần registry và chính sách timeout. |
| Điều kiện tích hợp | Thử một hợp đồng RPC với discovery và tracing, kiểm timeout/retry/idempotency; chọn phiên bản Java, registry và protocol tương thích. |
| Lựa chọn đối chiếu | gRPC; Spring Cloud; Apache Thrift. |

**Phạm vi bằng chứng:** đã clone, đọc trích đoạn tài liệu, giấy phép và các file cấu hình được dẫn dưới đây; chưa chạy mã, build, benchmark hoặc test upstream. `docs-read` không phải kiểm chứng implementation.

**Nguồn tại cùng SHA:** [README.md](https://github.com/apache/dubbo/blob/d809bb12c851468420a742dfb2aa5c5532c9e024/README.md) · [LICENSE](https://github.com/apache/dubbo/blob/d809bb12c851468420a742dfb2aa5c5532c9e024/LICENSE) · [pom.xml](https://github.com/apache/dubbo/blob/d809bb12c851468420a742dfb2aa5c5532c9e024/pom.xml) · [.github/workflows/release-test.yml](https://github.com/apache/dubbo/blob/d809bb12c851468420a742dfb2aa5c5532c9e024/.github/workflows/release-test.yml).

<a id="anhkysuai-frappe-erpnext"></a>

### ERPNext

**Repo:** [frappe/erpnext](https://github.com/frappe/erpnext) · **License:** GPL-3.0 · **Kiểm:** 2026-11-23, `docs-read`, [`22627f9ab9bf`](https://github.com/frappe/erpnext/tree/22627f9ab9bfd99a3d4e8f9f3b7cba3e7e39536d) (commit 2026-11-23). **Sao:** 41,564 tại 2026-11-23 theo [GitHub API](https://api.github.com/repos/frappe/erpnext).

| Mục | Đánh giá |
|---|---|
| Mục đích | Bộ ERP xây trên Frappe, bao phủ kế toán, đơn hàng, sản xuất, tài sản và dự án. |
| Giá trị và cơ chế theo tài liệu | README nối module nghiệp vụ với REST API và cơ chế của Frappe; manifest Python/JavaScript cùng kiểm frontend giúp xác định nền tảng mở rộng. |
| Giới hạn | Phiên bản framework và ứng dụng phải khớp; pyproject ở SHA này yêu cầu Python mới. Quy tắc thuế, kế toán và bản địa hóa chưa được xác minh cho doanh nghiệp cụ thể. |
| Điều kiện tích hợp | Dùng dữ liệu giả lập để kiểm quy trình liên module, quyền và migration; thiết lập backup/restore trước khi nhập sổ sách thật. |
| Lựa chọn đối chiếu | [Odoo Community](../34-backend-data-identity-integration/README.md#anhkysuai-odoo-odoo); Dolibarr; Tryton. |

**Phạm vi bằng chứng:** đã clone, đọc trích đoạn tài liệu, giấy phép và các file cấu hình được dẫn dưới đây; chưa chạy mã, build, benchmark hoặc test upstream. `docs-read` không phải kiểm chứng implementation.

**Nguồn tại cùng SHA:** [README.md](https://github.com/frappe/erpnext/blob/22627f9ab9bfd99a3d4e8f9f3b7cba3e7e39536d/README.md) · [license.txt](https://github.com/frappe/erpnext/blob/22627f9ab9bfd99a3d4e8f9f3b7cba3e7e39536d/license.txt) · [package.json](https://github.com/frappe/erpnext/blob/22627f9ab9bfd99a3d4e8f9f3b7cba3e7e39536d/package.json) · [pyproject.toml](https://github.com/frappe/erpnext/blob/22627f9ab9bfd99a3d4e8f9f3b7cba3e7e39536d/pyproject.toml) · [.github/workflows/pr-checks.yml](https://github.com/frappe/erpnext/blob/22627f9ab9bfd99a3d4e8f9f3b7cba3e7e39536d/.github/workflows/pr-checks.yml).

<a id="anhkysuai-pingcap-tidb"></a>

### TiDB

**Repo:** [pingcap/tidb](https://github.com/pingcap/tidb) · **License:** Apache-2.0 · **Kiểm:** 2026-11-23, `docs-read`, [`8d5a3a1908f4`](https://github.com/pingcap/tidb/tree/8d5a3a1908f495a90552bdcbff1c4723239ff883) (commit 2026-11-23). **Sao:** 40,768 tại 2026-11-23 theo [GitHub API](https://api.github.com/repos/pingcap/tidb).

| Mục | Đánh giá |
|---|---|
| Mục đích | Cơ sở dữ liệu SQL phân tán tách lớp tính toán và lưu trữ. |
| Giá trị và cơ chế theo tài liệu | README trình bày giao dịch phân tán, Raft và kiến trúc mở rộng; Go module cùng CI là điểm bắt đầu đọc các thành phần hệ thống. |
| Giới hạn | Mô tả 2PC/Raft không thay chứng minh tính đúng khi có lỗi. Chưa đo độ trễ, mức tương thích SQL hay chi phí vận hành nhiều node. |
| Điều kiện tích hợp | Thử bộ truy vấn thật, migration và phục hồi khi mất node; chốt topology, backup và quan sát trước khi thay cơ sở dữ liệu hiện tại. |
| Lựa chọn đối chiếu | [CockroachDB](../34-backend-data-identity-integration/README.md#anhkysuai-cockroachdb-cockroach); YugabyteDB; [Vitess](../34-backend-data-identity-integration/README.md#anhkysuai-vitessio-vitess). |

**Phạm vi bằng chứng:** đã clone, đọc trích đoạn tài liệu, giấy phép và các file cấu hình được dẫn dưới đây; chưa chạy mã, build, benchmark hoặc test upstream. `docs-read` không phải kiểm chứng implementation.

**Nguồn tại cùng SHA:** [README.md](https://github.com/pingcap/tidb/blob/8d5a3a1908f495a90552bdcbff1c4723239ff883/README.md) · [LICENSE](https://github.com/pingcap/tidb/blob/8d5a3a1908f495a90552bdcbff1c4723239ff883/LICENSE) · [go.mod](https://github.com/pingcap/tidb/blob/8d5a3a1908f495a90552bdcbff1c4723239ff883/go.mod) · [.github/workflows/check-bazel-prepare.yml](https://github.com/pingcap/tidb/blob/8d5a3a1908f495a90552bdcbff1c4723239ff883/.github/workflows/check-bazel-prepare.yml).

<a id="anhkysuai-yunaiv-ruoyi-vue-pro"></a>

### RuoYi Vue Pro

**Repo:** [YunaiV/ruoyi-vue-pro](https://github.com/YunaiV/ruoyi-vue-pro) · **License:** MIT · **Kiểm:** 2026-11-23, `docs-read`, [`da4b1b4c57e6`](https://github.com/YunaiV/ruoyi-vue-pro/tree/da4b1b4c57e62483ee541683048f76b183b146f1) (commit 2026-11-22). **Sao:** 40,594 tại 2026-11-23 theo [GitHub API](https://api.github.com/repos/YunaiV/ruoyi-vue-pro).

| Mục | Đánh giá |
|---|---|
| Mục đích | Nền tảng quản trị Java/Vue với phân quyền, đa tenant, workflow và module nghiệp vụ. |
| Giá trị và cơ chế theo tài liệu | README phân nhánh rõ theo JDK/Spring Boot; cấu trúc Spring Boot/MyBatis và frontend giúp tham khảo cách ghép admin, CRM và ERP. |
| Giới hạn | Phần lớn tài liệu bằng tiếng Trung; không mặc nhiên coi module mẫu phù hợp nghiệp vụ thật. Workflow đã đọc build Maven với bỏ qua test, nên không phải bằng chứng test đã đạt. |
| Điều kiện tích hợp | Chọn đúng nhánh runtime, kiểm quyền dữ liệu và tenant bằng tình huống phủ định; gỡ cấu hình mẫu và thử migration trước khi dùng. |
| Lựa chọn đối chiếu | JHipster; ELADMIN; ABP Framework. |

**Phạm vi bằng chứng:** đã clone, đọc trích đoạn tài liệu, giấy phép và các file cấu hình được dẫn dưới đây; chưa chạy mã, build, benchmark hoặc test upstream. `docs-read` không phải kiểm chứng implementation.

**Nguồn tại cùng SHA:** [README.md](https://github.com/YunaiV/ruoyi-vue-pro/blob/da4b1b4c57e62483ee541683048f76b183b146f1/README.md) · [LICENSE](https://github.com/YunaiV/ruoyi-vue-pro/blob/da4b1b4c57e62483ee541683048f76b183b146f1/LICENSE) · [pom.xml](https://github.com/YunaiV/ruoyi-vue-pro/blob/da4b1b4c57e62483ee541683048f76b183b146f1/pom.xml) · [.github/workflows/maven.yml](https://github.com/YunaiV/ruoyi-vue-pro/blob/da4b1b4c57e62483ee541683048f76b183b146f1/.github/workflows/maven.yml).

<a id="anhkysuai-photoprism-photoprism"></a>

### PhotoPrism

**Đã chuyển (2026-11-23):** hồ sơ này nay nằm ở [mục 36](../36-self-hosting-homelab/README.md#anhkysuai-photoprism-photoprism); catalog con xem [catalog/](../catalog/README.md).

<a id="anhkysuai-halo-dev-halo"></a>

### Halo

**Repo:** [halo-dev/halo](https://github.com/halo-dev/halo) · **License:** GPL-3.0 · **Kiểm:** 2026-11-23, `docs-read`, [`1ae87378ccf3`](https://github.com/halo-dev/halo/tree/1ae87378ccf323b0e2fcfd0e7016d4c356f76b06) (commit 2026-11-23). **Sao:** 40,378 tại 2026-11-23 theo [GitHub API](https://api.github.com/repos/halo-dev/halo).

| Mục | Đánh giá |
|---|---|
| Mục đích | CMS Java cho blog, nội dung và website có thể mở rộng bằng theme/plugin. |
| Giá trị và cơ chế theo tài liệu | README phân biệt Community với bản Pro/Store; workflow tạo lại tài liệu và client OpenAPI rồi kiểm đồng bộ, hữu ích cho tích hợp API. |
| Giới hạn | Tính năng và plugin trả phí không tự thuộc phạm vi GPL của core. Ví dụ container phục vụ khởi động nhanh, chưa là cấu hình production; chưa thử nâng cấp plugin. |
| Điều kiện tích hợp | Dùng bản phát hành, thử theme và quyền API trên staging; cấu hình lưu tệp, backup, HTTPS và kiểm giấy phép từng plugin. |
| Lựa chọn đối chiếu | [Ghost](../34-backend-data-identity-integration/README.md#anhkysuai-tryghost-ghost); WordPress; [Wagtail](../34-backend-data-identity-integration/README.md#anhkysuai-wagtail-wagtail). |

**Phạm vi bằng chứng:** đã clone, đọc trích đoạn tài liệu, giấy phép và các file cấu hình được dẫn dưới đây; chưa chạy mã, build, benchmark hoặc test upstream. `docs-read` không phải kiểm chứng implementation.

**Nguồn tại cùng SHA:** [README.md](https://github.com/halo-dev/halo/blob/1ae87378ccf323b0e2fcfd0e7016d4c356f76b06/README.md) · [LICENSE](https://github.com/halo-dev/halo/blob/1ae87378ccf323b0e2fcfd0e7016d4c356f76b06/LICENSE) · [build.gradle](https://github.com/halo-dev/halo/blob/1ae87378ccf323b0e2fcfd0e7016d4c356f76b06/build.gradle) · [.github/workflows/openapi-check.yaml](https://github.com/halo-dev/halo/blob/1ae87378ccf323b0e2fcfd0e7016d4c356f76b06/.github/workflows/openapi-check.yaml).

<a id="anhkysuai-gofiber-fiber"></a>

### Fiber

**Repo:** [gofiber/fiber](https://github.com/gofiber/fiber) · **License:** MIT · **Kiểm:** 2026-11-23, `docs-read`, [`e0466d29e78d`](https://github.com/gofiber/fiber/tree/e0466d29e78d94999d86151a27c5efc1d3dc9248) (commit 2026-11-22). **Sao:** 40,316 tại 2026-11-23 theo [GitHub API](https://api.github.com/repos/gofiber/fiber).

| Mục | Đánh giá |
|---|---|
| Mục đích | Framework web Go theo phong cách Express, xây trên fasthttp. |
| Giá trị và cơ chế theo tài liệu | README v3 và go.mod xác định runtime; CI dùng gotestsum và coverage. Công cụ migration được mô tả giúp chuyển cấu trúc từ v2. |
| Giới hạn | Tương thích middleware và vòng đời dữ liệu request cần kiểm theo framework thực tế. Có công cụ chuyển đổi không chứng minh migration đúng; chưa chạy ứng dụng hay benchmark. |
| Điều kiện tích hợp | Ghim phiên bản Go/Fiber, kiểm routing, middleware và lỗi cùng payload đại diện; đọc hướng dẫn migration và rà lại mã sau chuyển đổi. |
| Lựa chọn đối chiếu | [Chi](../34-backend-data-identity-integration/README.md#anhkysuai-go-chi-chi); [Echo](../34-backend-data-identity-integration/README.md#anhkysuai-labstack-echo); [Gin](../08-awesome-lists-learning/README.md#6c59-framework-backend). |

**Phạm vi bằng chứng:** đã clone, đọc trích đoạn tài liệu, giấy phép và các file cấu hình được dẫn dưới đây; chưa chạy mã, build, benchmark hoặc test upstream. `docs-read` không phải kiểm chứng implementation.

**Nguồn tại cùng SHA:** [README.md](https://github.com/gofiber/fiber/blob/e0466d29e78d94999d86151a27c5efc1d3dc9248/README.md) · [LICENSE](https://github.com/gofiber/fiber/blob/e0466d29e78d94999d86151a27c5efc1d3dc9248/LICENSE) · [go.mod](https://github.com/gofiber/fiber/blob/e0466d29e78d94999d86151a27c5efc1d3dc9248/go.mod) · [.github/workflows/test.yml](https://github.com/gofiber/fiber/blob/e0466d29e78d94999d86151a27c5efc1d3dc9248/.github/workflows/test.yml).

<a id="anhkysuai-nextcloud-server"></a>

### Nextcloud Server

**Đã chuyển (2026-11-23):** hồ sơ này nay nằm ở [mục 36](../36-self-hosting-homelab/README.md#anhkysuai-nextcloud-server); catalog con xem [catalog/](../catalog/README.md).

<a id="anhkysuai-fastify-fastify"></a>

### Fastify

**Repo:** [fastify/fastify](https://github.com/fastify/fastify) · **License:** MIT · **Kiểm:** 2026-11-23, `docs-read`, [`6de5abedb244`](https://github.com/fastify/fastify/tree/6de5abedb24424f0e8fa3612035d212d580f8d90) (commit 2026-11-21). **Sao:** 37,456 tại 2026-11-23 theo [GitHub API](https://api.github.com/repos/fastify/fastify).

| Mục | Đánh giá |
|---|---|
| Mục đích | Framework web Node.js với kiến trúc plugin và mục tiêu giảm overhead. |
| Giá trị và cơ chế theo tài liệu | README tách nhánh v6/main khỏi v5; manifest tại SHA là 6.0.0-alpha.6 và CI gọi bộ quality/coverage trên Unix và Windows. |
| Giới hạn | Đây là alpha, không đồng nhất với nhánh ổn định v5. Những tuyên bố nhanh hoặc tiết kiệm chi phí chưa được benchmark trong môi trường ứng dụng. |
| Điều kiện tích hợp | Chọn release và plugin tương thích, định nghĩa schema request/response và kiểm xử lý lỗi; thử nâng cấp trên staging thay vì theo main tự động. |
| Lựa chọn đối chiếu | [Express](../08-awesome-lists-learning/README.md#6c59-framework-backend); Hapi; NestJS. |

**Phạm vi bằng chứng:** đã clone, đọc trích đoạn tài liệu, giấy phép và các file cấu hình được dẫn dưới đây; chưa chạy mã, build, benchmark hoặc test upstream. `docs-read` không phải kiểm chứng implementation.

**Nguồn tại cùng SHA:** [README.md](https://github.com/fastify/fastify/blob/6de5abedb24424f0e8fa3612035d212d580f8d90/README.md) · [LICENSE](https://github.com/fastify/fastify/blob/6de5abedb24424f0e8fa3612035d212d580f8d90/LICENSE) · [package.json](https://github.com/fastify/fastify/blob/6de5abedb24424f0e8fa3612035d212d580f8d90/package.json) · [.github/workflows/ci.yml](https://github.com/fastify/fastify/blob/6de5abedb24424f0e8fa3612035d212d580f8d90/.github/workflows/ci.yml).

<a id="anhkysuai-rustfs-rustfs"></a>

### RustFS

**Repo:** [rustfs/rustfs](https://github.com/rustfs/rustfs) · **License:** Apache-2.0 · **Kiểm:** 2026-11-23, `docs-read`, [`b85c7a7ba003`](https://github.com/rustfs/rustfs/tree/b85c7a7ba003144609c5965681b2edd843a1c4c4) (commit 2026-11-23). **Sao:** 36,392 tại 2026-11-23 theo [GitHub API](https://api.github.com/repos/rustfs/rustfs).

| Mục | Đánh giá |
|---|---|
| Mục đích | Hệ lưu trữ đối tượng phân tán bằng Rust với giao diện S3. |
| Giá trị và cơ chế theo tài liệu | README dẫn ma trận tương thích S3 và mô tả Swift/Keystone; workspace Rust và CI lựa chọn phạm vi kiểm hỗ trợ đánh giá từng tính năng cụ thể. |
| Giới hạn | Tương thích chỉ bao phủ các tính năng được hỗ trợ, không mặc nhiên thay thế mọi S3 backend. Tuyên bố nhanh, an toàn và chịu lỗi chưa được đo hay fault-test. |
| Điều kiện tích hợp | Kiểm chính xác SDK/API đang dùng, multipart, policy và migration; thử mất node và phục hồi trên dữ liệu không quan trọng trước khi lưu bản duy nhất. |
| Lựa chọn đối chiếu | MinIO; [SeaweedFS](../34-backend-data-identity-integration/README.md#anhkysuai-seaweedfs-seaweedfs); Ceph. |

**Phạm vi bằng chứng:** đã clone, đọc trích đoạn tài liệu, giấy phép và các file cấu hình được dẫn dưới đây; chưa chạy mã, build, benchmark hoặc test upstream. `docs-read` không phải kiểm chứng implementation.

**Nguồn tại cùng SHA:** [README.md](https://github.com/rustfs/rustfs/blob/b85c7a7ba003144609c5965681b2edd843a1c4c4/README.md) · [LICENSE](https://github.com/rustfs/rustfs/blob/b85c7a7ba003144609c5965681b2edd843a1c4c4/LICENSE) · [Cargo.toml](https://github.com/rustfs/rustfs/blob/b85c7a7ba003144609c5965681b2edd843a1c4c4/Cargo.toml) · [.github/workflows/ci.yml](https://github.com/rustfs/rustfs/blob/b85c7a7ba003144609c5965681b2edd843a1c4c4/.github/workflows/ci.yml).

<a id="anhkysuai-seaweedfs-seaweedfs"></a>

### SeaweedFS

**Repo:** [seaweedfs/seaweedfs](https://github.com/seaweedfs/seaweedfs) · **License:** Apache-2.0 · **Kiểm:** 2026-11-23, `docs-read`, [`ae0f1a252526`](https://github.com/seaweedfs/seaweedfs/tree/ae0f1a2525261829a1d9b3efca2bac9153ce7143) (commit 2026-11-23). **Sao:** 36,209 tại 2026-11-23 theo [GitHub API](https://api.github.com/repos/seaweedfs/seaweedfs).

| Mục | Đánh giá |
|---|---|
| Mục đích | Hệ lưu trữ phân tán cung cấp S3, filesystem và các lớp dữ liệu dùng chung storage. |
| Giá trị và cơ chế theo tài liệu | README mô tả master/filer/volume, REST API, Iceberg catalog và vector buckets; CI Helm kiểm tài nguyên chart cho triển khai Kubernetes. |
| Giới hạn | Mục tiêu hàng tỷ tệp và độ phức tạp O(1) là mô tả upstream, chưa benchmark. S3, POSIX, lakehouse và vector search có phạm vi tương thích cần đánh giá riêng. |
| Điều kiện tích hợp | Chọn giao diện thực sự cần, thử workload và lỗi volume/filer; kiểm replication, capacity, backup metadata và điều kiện nâng cấp cluster. |
| Lựa chọn đối chiếu | Ceph; [RustFS](../34-backend-data-identity-integration/README.md#anhkysuai-rustfs-rustfs); Garage. |

**Phạm vi bằng chứng:** đã clone, đọc trích đoạn tài liệu, giấy phép và các file cấu hình được dẫn dưới đây; chưa chạy mã, build, benchmark hoặc test upstream. `docs-read` không phải kiểm chứng implementation.

**Nguồn tại cùng SHA:** [README.md](https://github.com/seaweedfs/seaweedfs/blob/ae0f1a2525261829a1d9b3efca2bac9153ce7143/README.md) · [LICENSE](https://github.com/seaweedfs/seaweedfs/blob/ae0f1a2525261829a1d9b3efca2bac9153ce7143/LICENSE) · [go.mod](https://github.com/seaweedfs/seaweedfs/blob/ae0f1a2525261829a1d9b3efca2bac9153ce7143/go.mod) · [.github/workflows/helm_ci.yml](https://github.com/seaweedfs/seaweedfs/blob/ae0f1a2525261829a1d9b3efca2bac9153ce7143/.github/workflows/helm_ci.yml).

<a id="anhkysuai-sahat-hackathon-starter"></a>

### Hackathon Starter

**Repo:** [sahat/hackathon-starter](https://github.com/sahat/hackathon-starter) · **License:** MIT · **Kiểm:** 2026-11-23, `docs-read`, [`376261ba451e`](https://github.com/sahat/hackathon-starter/tree/376261ba451e63169b3f5fae3b823a4f349e1a0d) (commit 2026-11-20). **Sao:** 35,260 tại 2026-11-23 theo [GitHub API](https://api.github.com/repos/sahat/hackathon-starter).

| Mục | Đánh giá |
|---|---|
| Mục đích | Boilerplate Node.js giúp bắt đầu ứng dụng web và học các tích hợp đăng nhập. |
| Giá trị và cơ chế theo tài liệu | README giải thích mục tiêu đơn giản/tái dùng; manifest nêu Node 24 trở lên, CI lint, test và replay kiểm e2e. |
| Giới hạn | Mẫu hackathon không tự đáp ứng yêu cầu sản phẩm thật. Các nhà cung cấp OAuth có cấu hình/quyền riêng; chưa chạy kiểm authentication hoặc checklist production. |
| Điều kiện tích hợp | Fork rồi bỏ phần không dùng, thay cấu hình mẫu và quản lý secrets; kiểm session, redirect OAuth và quyền nghiệp vụ trước khi đưa dữ liệu thật vào. |
| Lựa chọn đối chiếu | [Full Stack FastAPI Template](../34-backend-data-identity-integration/README.md#anhkysuai-fastapi-full-stack-fastapi-template); JHipster; Cookiecutter Django. |

**Phạm vi bằng chứng:** đã clone, đọc trích đoạn tài liệu, giấy phép và các file cấu hình được dẫn dưới đây; chưa chạy mã, build, benchmark hoặc test upstream. `docs-read` không phải kiểm chứng implementation.

**Nguồn tại cùng SHA:** [README.md](https://github.com/sahat/hackathon-starter/blob/376261ba451e63169b3f5fae3b823a4f349e1a0d/README.md) · [LICENSE](https://github.com/sahat/hackathon-starter/blob/376261ba451e63169b3f5fae3b823a4f349e1a0d/LICENSE) · [package.json](https://github.com/sahat/hackathon-starter/blob/376261ba451e63169b3f5fae3b823a4f349e1a0d/package.json) · [.github/workflows/build.yml](https://github.com/sahat/hackathon-starter/blob/376261ba451e63169b3f5fae3b823a4f349e1a0d/.github/workflows/build.yml).

<a id="anhkysuai-laravel-framework"></a>

### Laravel Framework

**Repo:** [laravel/framework](https://github.com/laravel/framework) · **License:** MIT · **Kiểm:** 2026-11-23, `docs-read`, [`3f9a7b15a1a8`](https://github.com/laravel/framework/tree/3f9a7b15a1a866aae9cd3f30d1065a114997bb27) (commit 2026-11-23). **Sao:** 35,058 tại 2026-11-23 theo [GitHub API](https://api.github.com/repos/laravel/framework).

| Mục | Đánh giá |
|---|---|
| Mục đích | Mã lõi framework PHP cho routing, dependency injection, migration, queue và sự kiện. |
| Giá trị và cơ chế theo tài liệu | README phân biệt rõ repo core với laravel/laravel dùng khởi tạo app; Composer và CI PHPUnit theo nhiều phiên bản là điểm tham khảo cho thư viện nền. |
| Giới hạn | Đọc core không đánh giá ứng dụng được tạo hay mọi package hệ sinh thái. Chưa chạy test upstream hoặc kiểm policy xác thực/phân quyền của sản phẩm cụ thể. |
| Điều kiện tích hợp | Dùng skeleton và release tương thích PHP, chọn backend queue/cache theo nhu cầu; thêm kiểm nghiệp vụ, migration và quyền trong repo ứng dụng. |
| Lựa chọn đối chiếu | [Symfony](../34-backend-data-identity-integration/README.md#anhkysuai-symfony-symfony); Django; Rails. |

**Phạm vi bằng chứng:** đã clone, đọc trích đoạn tài liệu, giấy phép và các file cấu hình được dẫn dưới đây; chưa chạy mã, build, benchmark hoặc test upstream. `docs-read` không phải kiểm chứng implementation.

**Nguồn tại cùng SHA:** [README.md](https://github.com/laravel/framework/blob/3f9a7b15a1a866aae9cd3f30d1065a114997bb27/README.md) · [LICENSE.md](https://github.com/laravel/framework/blob/3f9a7b15a1a866aae9cd3f30d1065a114997bb27/LICENSE.md) · [composer.json](https://github.com/laravel/framework/blob/3f9a7b15a1a866aae9cd3f30d1065a114997bb27/composer.json) · [.github/workflows/tests.yml](https://github.com/laravel/framework/blob/3f9a7b15a1a866aae9cd3f30d1065a114997bb27/.github/workflows/tests.yml).

<a id="anhkysuai-surrealdb-surrealdb"></a>

### SurrealDB

**Repo:** [surrealdb/surrealdb](https://github.com/surrealdb/surrealdb) · **License:** BUSL-1.1; Additional Use Grant, đổi Apache-2.0 theo Change Date · **Kiểm:** 2026-11-23, `docs-read`, [`1b73f91bc12f`](https://github.com/surrealdb/surrealdb/tree/1b73f91bc12f462ba6eb9cd792d3e8f3336fb619) (commit 2026-11-17). **Sao:** 33,352 tại 2026-11-23 theo [GitHub API](https://api.github.com/repos/surrealdb/surrealdb).

| Mục | Đánh giá |
|---|---|
| Mục đích | Cơ sở dữ liệu đa mô hình Rust với document, graph, tìm kiếm và sự kiện thời gian thực. |
| Giá trị và cơ chế theo tài liệu | README mô tả triển khai embedded, WebAssembly, node hoặc cluster; Cargo tách engine, IAM, datastore và các lớp dữ liệu. |
| Giới hạn | LICENSE không phải nguồn mở OSI, loại trừ Database Service như định nghĩa và ghi Change Date 2030-01-01 cho phạm vi này. Tuyên bố hợp nhất backend/hiệu năng chưa được thử. |
| Điều kiện tích hợp | Kiểm quyền sử dụng theo mô hình cung cấp dịch vụ, thử query/permission và migration; đánh giá tính đúng và backup riêng cho từng kiểu triển khai. |
| Lựa chọn đối chiếu | PostgreSQL; ArangoDB; EdgeDB/Gel. |

**Phạm vi bằng chứng:** đã clone, đọc trích đoạn tài liệu, giấy phép và các file cấu hình được dẫn dưới đây; chưa chạy mã, build, benchmark hoặc test upstream. `docs-read` không phải kiểm chứng implementation.

**Nguồn tại cùng SHA:** [README.md](https://github.com/surrealdb/surrealdb/blob/1b73f91bc12f462ba6eb9cd792d3e8f3336fb619/README.md) · [LICENSE](https://github.com/surrealdb/surrealdb/blob/1b73f91bc12f462ba6eb9cd792d3e8f3336fb619/LICENSE) · [Cargo.toml](https://github.com/surrealdb/surrealdb/blob/1b73f91bc12f462ba6eb9cd792d3e8f3336fb619/Cargo.toml) · [.github/workflows/ci.yml](https://github.com/surrealdb/surrealdb/blob/1b73f91bc12f462ba6eb9cd792d3e8f3336fb619/.github/workflows/ci.yml).

<a id="anhkysuai-labstack-echo"></a>

### Echo

**Repo:** [labstack/echo](https://github.com/labstack/echo) · **License:** MIT · **Kiểm:** 2026-11-23, `docs-read`, [`59aacddc4a13`](https://github.com/labstack/echo/tree/59aacddc4a13904b8a80a76f1ec838c495b5feca) (commit 2026-11-20). **Sao:** 32,831 tại 2026-11-23 theo [GitHub API](https://api.github.com/repos/labstack/echo).

| Mục | Đánh giá |
|---|---|
| Mục đích | Framework Go xây trên net/http, thêm routing, binding, middleware và xử lý lỗi tập trung. |
| Giá trị và cơ chế theo tài liệu | README mô tả rõ thứ tự pre middleware/router/handler/error handler của v5; CI chạy go test với race detector và coverage. |
| Giới hạn | Echo Pro là thư viện thương mại riêng, không thuộc MIT của core. Chưa chạy test hoặc đo tốc độ; binding request không thay validation và phân quyền nghiệp vụ. |
| Điều kiện tích hợp | Chọn v5 cùng middleware tương thích, định nghĩa validation và error mapping; thử request lỗi, shutdown và giới hạn tài nguyên trước khi phục vụ công khai. |
| Lựa chọn đối chiếu | [Chi](../34-backend-data-identity-integration/README.md#anhkysuai-go-chi-chi); [Fiber](../34-backend-data-identity-integration/README.md#anhkysuai-gofiber-fiber); [Gin](../08-awesome-lists-learning/README.md#6c59-framework-backend). |

**Phạm vi bằng chứng:** đã clone, đọc trích đoạn tài liệu, giấy phép và các file cấu hình được dẫn dưới đây; chưa chạy mã, build, benchmark hoặc test upstream. `docs-read` không phải kiểm chứng implementation.

**Nguồn tại cùng SHA:** [README.md](https://github.com/labstack/echo/blob/59aacddc4a13904b8a80a76f1ec838c495b5feca/README.md) · [LICENSE](https://github.com/labstack/echo/blob/59aacddc4a13904b8a80a76f1ec838c495b5feca/LICENSE) · [go.mod](https://github.com/labstack/echo/blob/59aacddc4a13904b8a80a76f1ec838c495b5feca/go.mod) · [.github/workflows/ci.yml](https://github.com/labstack/echo/blob/59aacddc4a13904b8a80a76f1ec838c495b5feca/.github/workflows/ci.yml).

<a id="anhkysuai-cockroachdb-cockroach"></a>

### CockroachDB

**Repo:** [cockroachdb/cockroach](https://github.com/cockroachdb/cockroach) · **License:** CockroachDB Software License · **Kiểm:** 2026-11-23, `docs-read`, [`d30c905fff79`](https://github.com/cockroachdb/cockroach/tree/d30c905fff79ef825adc96bcc647f1872a90f2ff) (commit 2026-09-23). **Sao:** 32,643 tại 2026-11-23 theo [GitHub API](https://api.github.com/repos/cockroachdb/cockroach).

| Mục | Đánh giá |
|---|---|
| Mục đích | Cơ sở dữ liệu SQL phân tán với giao dịch trên kho khóa-giá trị nhất quán. |
| Giá trị và cơ chế theo tài liệu | README mô tả mở rộng và điều khiển vị trí dữ liệu; Go/Bazel cùng CI kiểm binary cung cấp điểm bắt đầu đánh giá triển khai. |
| Giới hạn | LICENSE yêu cầu license key ngoài Limited Non-Production Use và có nghĩa vụ telemetry theo điều khoản. Tuyên bố chịu lỗi và độ trễ chưa được tái lập. |
| Điều kiện tích hợp | Kiểm quyền/telemetry của mô hình sử dụng, thử bộ SQL và retry giao dịch; đo liên vùng, backup/restore và mất node trên cluster thử. |
| Lựa chọn đối chiếu | [TiDB](../34-backend-data-identity-integration/README.md#anhkysuai-pingcap-tidb); YugabyteDB; PostgreSQL + Citus. |

**Phạm vi bằng chứng:** đã clone, đọc trích đoạn tài liệu, giấy phép và các file cấu hình được dẫn dưới đây; chưa chạy mã, build, benchmark hoặc test upstream. `docs-read` không phải kiểm chứng implementation.

**Nguồn tại cùng SHA:** [README.md](https://github.com/cockroachdb/cockroach/blob/d30c905fff79ef825adc96bcc647f1872a90f2ff/README.md) · [LICENSE](https://github.com/cockroachdb/cockroach/blob/d30c905fff79ef825adc96bcc647f1872a90f2ff/LICENSE) · [go.mod](https://github.com/cockroachdb/cockroach/blob/d30c905fff79ef825adc96bcc647f1872a90f2ff/go.mod) · [.github/workflows/bincheck.yml](https://github.com/cockroachdb/cockroach/blob/d30c905fff79ef825adc96bcc647f1872a90f2ff/.github/workflows/bincheck.yml).

<a id="anhkysuai-filamentphp-filament"></a>

### Filament

**Repo:** [filamentphp/filament](https://github.com/filamentphp/filament) · **License:** MIT · **Kiểm:** 2026-11-23, `docs-read`, [`d837848f98a6`](https://github.com/filamentphp/filament/tree/d837848f98a6f9c3906302d3b7ef46e23b4c5de2) (commit 2026-11-23). **Sao:** 32,543 tại 2026-11-23 theo [GitHub API](https://api.github.com/repos/filamentphp/filament).

| Mục | Đánh giá |
|---|---|
| Mục đích | Khung xây admin, portal và phần mềm nghiệp vụ trên Laravel. |
| Giá trị và cơ chế theo tài liệu | README kết hợp tables, forms, infolists, notifications, widgets và actions; Composer và CI theo PHP/Laravel/database hỗ trợ đánh giá tương thích nền tảng. |
| Giới hạn | Component CRUD không tự tạo chính sách truy cập dữ liệu hoặc quy trình nghiệp vụ đúng. Plugin và theme có thể có giấy phép khác; chưa thử tương tác accessibility hay dữ liệu lớn. |
| Điều kiện tích hợp | Chọn phiên bản Laravel/PHP phù hợp, viết policy cho từng resource/action; thử lọc dữ liệu theo tenant và hành động hàng loạt trước khi cho vận hành. |
| Lựa chọn đối chiếu | Laravel Nova; Django Admin; React Admin. |

**Phạm vi bằng chứng:** đã clone, đọc trích đoạn tài liệu, giấy phép và các file cấu hình được dẫn dưới đây; chưa chạy mã, build, benchmark hoặc test upstream. `docs-read` không phải kiểm chứng implementation.

**Nguồn tại cùng SHA:** [README.md](https://github.com/filamentphp/filament/blob/d837848f98a6f9c3906302d3b7ef46e23b4c5de2/README.md) · [LICENSE.md](https://github.com/filamentphp/filament/blob/d837848f98a6f9c3906302d3b7ef46e23b4c5de2/LICENSE.md) · [package.json](https://github.com/filamentphp/filament/blob/d837848f98a6f9c3906302d3b7ef46e23b4c5de2/package.json) · [composer.json](https://github.com/filamentphp/filament/blob/d837848f98a6f9c3906302d3b7ef46e23b4c5de2/composer.json) · [.github/workflows/tests.yml](https://github.com/filamentphp/filament/blob/d837848f98a6f9c3906302d3b7ef46e23b4c5de2/.github/workflows/tests.yml).

<a id="anhkysuai-meta-rocksdb"></a>

### RocksDB

**Repo:** [meta/rocksdb](https://github.com/meta/rocksdb) · **License:** GPL-2.0 OR Apache-2.0; phần LevelDB có điều khoản riêng · **Kiểm:** 2026-11-23, `docs-read`, [`883ce9ce9e89`](https://github.com/meta/rocksdb/tree/883ce9ce9e89230e8b770935e884dda103cea80f) (commit 2026-11-22). **Sao:** 32,309 tại 2026-11-23 theo [GitHub API](https://api.github.com/repos/meta/rocksdb).

| Mục | Đánh giá |
|---|---|
| Mục đích | Thư viện kho khóa-giá trị lưu bền nhúng với thiết kế LSM. |
| Giá trị và cơ chế theo tài liệu | README nêu trade-off write/read/space amplification và compaction; public API nằm ở include/, CI tuần có valgrind test. |
| Giới hạn | Metadata GitHub chỉ nhận GPL nhưng README cho phép chọn Apache-2.0; giữ thông báo LevelDB riêng. Không phải server phân tán hoàn chỉnh; chưa đo workload hay hành vi khi mất điện. |
| Điều kiện tích hợp | Chỉ dùng public API, thiết kế backup và schema key; thử compaction, giới hạn RAM, write stall và recovery với dữ liệu đại diện. |
| Lựa chọn đối chiếu | LevelDB; LMDB; SQLite. |

**Phạm vi bằng chứng:** đã clone, đọc trích đoạn tài liệu, giấy phép và các file cấu hình được dẫn dưới đây; chưa chạy mã, build, benchmark hoặc test upstream. `docs-read` không phải kiểm chứng implementation.

**Nguồn tại cùng SHA:** [README.md](https://github.com/meta/rocksdb/blob/883ce9ce9e89230e8b770935e884dda103cea80f/README.md) · [COPYING](https://github.com/meta/rocksdb/blob/883ce9ce9e89230e8b770935e884dda103cea80f/COPYING) · [LICENSE.Apache](https://github.com/meta/rocksdb/blob/883ce9ce9e89230e8b770935e884dda103cea80f/LICENSE.Apache) · [LICENSE.leveldb](https://github.com/meta/rocksdb/blob/883ce9ce9e89230e8b770935e884dda103cea80f/LICENSE.leveldb) · [CMakeLists.txt](https://github.com/meta/rocksdb/blob/883ce9ce9e89230e8b770935e884dda103cea80f/CMakeLists.txt) · [.github/workflows/weekly.yml](https://github.com/meta/rocksdb/blob/883ce9ce9e89230e8b770935e884dda103cea80f/.github/workflows/weekly.yml).

<a id="anhkysuai-hasura-graphql-engine"></a>

### Hasura GraphQL Engine

**Repo:** [hasura/graphql-engine](https://github.com/hasura/graphql-engine) · **License:** Apache-2.0; LICENSE-community theo MIT · **Kiểm:** 2026-11-23, `docs-read`, [`96f68d0a35a2`](https://github.com/hasura/graphql-engine/tree/96f68d0a35a2b3ee153ce67585d37efb3cfa6598) (commit 2026-11-11). **Sao:** 32,127 tại 2026-11-23 theo [GitHub API](https://api.github.com/repos/hasura/graphql-engine).

| Mục | Đánh giá |
|---|---|
| Mục đích | Engine cung cấp API GraphQL thống nhất trên các nguồn dữ liệu. |
| Giá trị và cơ chế theo tài liệu | README phân biệt v3/DDN trong thư mục v3 và v2 ổn định, đồng thời giới thiệu connector SDK TypeScript/Python/Go; repo có giấy phép Apache và community MIT. |
| Giới hạn | Không suy tính năng cloud/DDN và connector bên ngoài từ core. Workflow đọc chỉ là lint console; chưa kiểm phân quyền, query plan hoặc tính tương thích dữ liệu. |
| Điều kiện tích hợp | Chọn v2/v3 theo nhu cầu, thử permission với người dùng không có quyền và query phức tạp; ghim connector cùng phiên bản và kiểm migration metadata. |
| Lựa chọn đối chiếu | [PostgREST](../34-backend-data-identity-integration/README.md#anhkysuai-postgrest-postgrest); PostGraphile; GraphQL Yoga. |

**Phạm vi bằng chứng:** đã clone, đọc trích đoạn tài liệu, giấy phép và các file cấu hình được dẫn dưới đây; chưa chạy mã, build, benchmark hoặc test upstream. `docs-read` không phải kiểm chứng implementation.

**Nguồn tại cùng SHA:** [README.md](https://github.com/hasura/graphql-engine/blob/96f68d0a35a2b3ee153ce67585d37efb3cfa6598/README.md) · [LICENSE](https://github.com/hasura/graphql-engine/blob/96f68d0a35a2b3ee153ce67585d37efb3cfa6598/LICENSE) · [LICENSE-community](https://github.com/hasura/graphql-engine/blob/96f68d0a35a2b3ee153ce67585d37efb3cfa6598/LICENSE-community) · [.github/workflows/lint.yml](https://github.com/hasura/graphql-engine/blob/96f68d0a35a2b3ee153ce67585d37efb3cfa6598/.github/workflows/lint.yml).

<a id="anhkysuai-dragonflydb-dragonfly"></a>

### Dragonfly

**Repo:** [dragonflydb/dragonfly](https://github.com/dragonflydb/dragonfly) · **License:** Dragonfly Source-Available License (DSAL) · **Kiểm:** 2026-11-23, `docs-read`, [`034fb0572352`](https://github.com/dragonflydb/dragonfly/tree/034fb057235243595fab604efe16aa0325587a0b) (commit 2026-11-23). **Sao:** 31,916 tại 2026-11-23 theo [GitHub API](https://api.github.com/repos/dragonflydb/dragonfly).

| Mục | Đánh giá |
|---|---|
| Mục đích | Kho dữ liệu trong bộ nhớ hướng đến API Redis và Memcached. |
| Giá trị và cơ chế theo tài liệu | README mô tả mục tiêu dùng với ứng dụng hiện có; CI có kiểm ACL category với Valkey và phạm vi lệnh fuzz, hữu ích cho kế hoạch tương thích. |
| Giới hạn | LICENSE hiện tại là DSAL, có giới hạn production 100 vCPU tổng cùng các điều kiện khác. Không dùng nhãn BUSL cũ; các tuyên bố 25x và giảm tài nguyên chưa được đo. |
| Điều kiện tích hợp | Rà lệnh/module/client thực tế, thử persistence, failover và TTL; kiểm đầy đủ DSAL của phiên bản trước khi thay cache hiện có. |
| Lựa chọn đối chiếu | [Valkey](../34-backend-data-identity-integration/README.md#anhkysuai-valkey-io-valkey); [Redis](../08-awesome-lists-learning/README.md#6c511-giám-sát-csdl--phân-tích); KeyDB. |

**Phạm vi bằng chứng:** đã clone, đọc trích đoạn tài liệu, giấy phép và các file cấu hình được dẫn dưới đây; chưa chạy mã, build, benchmark hoặc test upstream. `docs-read` không phải kiểm chứng implementation.

**Nguồn tại cùng SHA:** [README.md](https://github.com/dragonflydb/dragonfly/blob/034fb057235243595fab604efe16aa0325587a0b/README.md) · [LICENSE.md](https://github.com/dragonflydb/dragonfly/blob/034fb057235243595fab604efe16aa0325587a0b/LICENSE.md) · [pyproject.toml](https://github.com/dragonflydb/dragonfly/blob/034fb057235243595fab604efe16aa0325587a0b/pyproject.toml) · [CMakeLists.txt](https://github.com/dragonflydb/dragonfly/blob/034fb057235243595fab604efe16aa0325587a0b/CMakeLists.txt) · [.github/workflows/ci.yml](https://github.com/dragonflydb/dragonfly/blob/034fb057235243595fab604efe16aa0325587a0b/.github/workflows/ci.yml).

<a id="anhkysuai-influxdata-influxdb"></a>

### InfluxDB 3 Core

**Repo:** [influxdata/influxdb](https://github.com/influxdata/influxdb) · **License:** MIT OR Apache-2.0 · **Kiểm:** 2026-11-23, `docs-read`, [`185688a5a813`](https://github.com/influxdata/influxdb/tree/185688a5a813016c0d26ec10abbad2ca770670ed) (commit 2026-10-22). **Sao:** 31,833 tại 2026-11-23 theo [GitHub API](https://api.github.com/repos/influxdata/influxdb).

| Mục | Đánh giá |
|---|---|
| Mục đích | Cơ sở dữ liệu time series/sự kiện dùng Rust, Arrow, DataFusion và Parquet. |
| Giá trị và cơ chế theo tài liệu | README phân biệt v3 Core với nhánh cũ và Enterprise; mô tả line protocol, SQL/InfluxQL, object storage cùng Python plugin/trigger. |
| Giới hạn | Tương thích write API 1.x/2.x không có nghĩa toàn bộ query/tính năng cũ tương thích. Các độ trễ nêu trong README chưa benchmark; workflow đã đọc chỉ kiểm thông điệp commit. |
| Điều kiện tích hợp | Thử ingest/query thật, retention và backup object store; đối chiếu API cũ, quyền plugin Python và bản Core/Enterprise trước khi chuyển dữ liệu. |
| Lựa chọn đối chiếu | [TimescaleDB](../34-backend-data-identity-integration/README.md#anhkysuai-timescale-timescaledb); [VictoriaMetrics](../08-awesome-lists-learning/README.md#6c511-giám-sát-csdl--phân-tích); QuestDB. |

**Phạm vi bằng chứng:** đã clone, đọc trích đoạn tài liệu, giấy phép và các file cấu hình được dẫn dưới đây; chưa chạy mã, build, benchmark hoặc test upstream. `docs-read` không phải kiểm chứng implementation.

**Nguồn tại cùng SHA:** [README.md](https://github.com/influxdata/influxdb/blob/185688a5a813016c0d26ec10abbad2ca770670ed/README.md) · [LICENSE-APACHE](https://github.com/influxdata/influxdb/blob/185688a5a813016c0d26ec10abbad2ca770670ed/LICENSE-APACHE) · [LICENSE-MIT](https://github.com/influxdata/influxdb/blob/185688a5a813016c0d26ec10abbad2ca770670ed/LICENSE-MIT) · [Cargo.toml](https://github.com/influxdata/influxdb/blob/185688a5a813016c0d26ec10abbad2ca770670ed/Cargo.toml) · [.github/workflows/semantic.yml](https://github.com/influxdata/influxdb/blob/185688a5a813016c0d26ec10abbad2ca770670ed/.github/workflows/semantic.yml).

<a id="anhkysuai-symfony-symfony"></a>

### Symfony

**Repo:** [symfony/symfony](https://github.com/symfony/symfony) · **License:** MIT · **Kiểm:** 2026-11-23, `docs-read`, [`8d1546d0da29`](https://github.com/symfony/symfony/tree/8d1546d0da29d440f669250f91eb89996fda5753) (commit 2026-11-23). **Sao:** 31,458 tại 2026-11-23 theo [GitHub API](https://api.github.com/repos/symfony/symfony).

| Mục | Đánh giá |
|---|---|
| Mục đích | Framework PHP cho ứng dụng web/console và tập component có thể dùng riêng. |
| Giá trị và cơ chế theo tài liệu | README nêu nhịp release, LTS và tài liệu component; Composer cùng CI unit tests hỗ trợ lựa chọn bộ phận nền thay vì lấy toàn framework. |
| Giới hạn | Dòng phát triển tại SHA hướng tới Symfony 8.2; support và runtime phải kiểm theo release được chọn. Chưa chạy kiểm hoặc xác minh tính tương thích bundle ngoài. |
| Điều kiện tích hợp | Chọn bản còn hỗ trợ và component cần dùng, kiểm deprecation/upgrade guide; thêm kiểm container configuration, request lifecycle và nghiệp vụ trong ứng dụng. |
| Lựa chọn đối chiếu | Laravel; Laminas; Slim. |

**Phạm vi bằng chứng:** đã clone, đọc trích đoạn tài liệu, giấy phép và các file cấu hình được dẫn dưới đây; chưa chạy mã, build, benchmark hoặc test upstream. `docs-read` không phải kiểm chứng implementation.

**Nguồn tại cùng SHA:** [README.md](https://github.com/symfony/symfony/blob/8d1546d0da29d440f669250f91eb89996fda5753/README.md) · [LICENSE](https://github.com/symfony/symfony/blob/8d1546d0da29d440f669250f91eb89996fda5753/LICENSE) · [composer.json](https://github.com/symfony/symfony/blob/8d1546d0da29d440f669250f91eb89996fda5753/composer.json) · [.github/workflows/unit-tests.yml](https://github.com/symfony/symfony/blob/8d1546d0da29d440f669250f91eb89996fda5753/.github/workflows/unit-tests.yml).

<a id="anhkysuai-better-auth-better-auth"></a>

### Better Auth

**Repo:** [better-auth/better-auth](https://github.com/better-auth/better-auth) · **License:** MIT · **Kiểm:** 2026-11-23, `docs-read`, [`1aa7c03958f9`](https://github.com/better-auth/better-auth/tree/1aa7c03958f93d2d58af5fb06afd764a40813a60) (commit 2026-11-23). **Sao:** 30,839 tại 2026-11-23 theo [GitHub API](https://api.github.com/repos/better-auth/better-auth).

| Mục | Đánh giá |
|---|---|
| Mục đích | Framework xác thực/ủy quyền TypeScript độc lập framework ứng dụng. |
| Giá trị và cơ chế theo tài liệu | README mô tả plugin cho 2FA, tenant và các luồng mở rộng; workspace/CI build cho thấy hệ gói có thể tích hợp từng phần. |
| Giới hạn | Có tính năng xác thực không đồng nghĩa cấu hình của sản phẩm được bảo vệ đúng. Chưa đọc implementation hoặc kiểm session, reset, tenant isolation hay provider OAuth. |
| Điều kiện tích hợp | Thử với database adapter và framework đích, định nghĩa rõ chính sách session/quyền; thêm kiểm phủ định cho recovery, đăng xuất và truy cập chéo tenant. |
| Lựa chọn đối chiếu | [Auth.js](../34-backend-data-identity-integration/README.md#anhkysuai-nextauthjs-next-auth); Lucia; Ory Kratos. |

**Phạm vi bằng chứng:** đã clone, đọc trích đoạn tài liệu, giấy phép và các file cấu hình được dẫn dưới đây; chưa chạy mã, build, benchmark hoặc test upstream. `docs-read` không phải kiểm chứng implementation.

**Nguồn tại cùng SHA:** [README.md](https://github.com/better-auth/better-auth/blob/1aa7c03958f93d2d58af5fb06afd764a40813a60/README.md) · [LICENSE.md](https://github.com/better-auth/better-auth/blob/1aa7c03958f93d2d58af5fb06afd764a40813a60/LICENSE.md) · [package.json](https://github.com/better-auth/better-auth/blob/1aa7c03958f93d2d58af5fb06afd764a40813a60/package.json) · [.github/workflows/ci.yml](https://github.com/better-auth/better-auth/blob/1aa7c03958f93d2d58af5fb06afd764a40813a60/.github/workflows/ci.yml).

<a id="anhkysuai-encode-django-rest-framework"></a>

### Django REST Framework

**Repo:** [encode/django-rest-framework](https://github.com/encode/django-rest-framework) · **License:** BSD-3-Clause · **Kiểm:** 2026-11-23, `docs-read`, [`7db99000c115`](https://github.com/encode/django-rest-framework/tree/7db99000c115e5b3d0a72c6c9bfec249d39c4476) (commit 2026-11-19). **Sao:** 30,256 tại 2026-11-23 theo [GitHub API](https://api.github.com/repos/encode/django-rest-framework).

| Mục | Đánh giá |
|---|---|
| Mục đích | Bộ công cụ xây Web API trên Django với serializer, policy xác thực và browsable API. |
| Giá trị và cơ chế theo tài liệu | README phân biệt serializer ORM/non-ORM cùng viewset/router; pyproject và CI tox xác định yêu cầu Python/Django ở SHA đã đọc. |
| Giới hạn | Policy được cung cấp không có nghĩa mọi endpoint đã được bảo vệ. Chưa kiểm quyền object-level, pagination hay query count; OAuth còn có gói tùy chọn ngoài repo. |
| Điều kiện tích hợp | Ghim Django/runtime hỗ trợ, khai báo authentication/permission rõ và thử truy cập chéo người dùng; đo N+1 query, validation và schema API trước khi mở công khai. |
| Lựa chọn đối chiếu | Django Ninja; FastAPI; Litestar. |

**Phạm vi bằng chứng:** đã clone, đọc trích đoạn tài liệu, giấy phép và các file cấu hình được dẫn dưới đây; chưa chạy mã, build, benchmark hoặc test upstream. `docs-read` không phải kiểm chứng implementation.

**Nguồn tại cùng SHA:** [README.md](https://github.com/encode/django-rest-framework/blob/7db99000c115e5b3d0a72c6c9bfec249d39c4476/README.md) · [LICENSE.md](https://github.com/encode/django-rest-framework/blob/7db99000c115e5b3d0a72c6c9bfec249d39c4476/LICENSE.md) · [pyproject.toml](https://github.com/encode/django-rest-framework/blob/7db99000c115e5b3d0a72c6c9bfec249d39c4476/pyproject.toml) · [.github/workflows/main.yml](https://github.com/encode/django-rest-framework/blob/7db99000c115e5b3d0a72c6c9bfec249d39c4476/.github/workflows/main.yml).

<a id="anhkysuai-hashicorp-consul"></a>

### Consul

**Repo:** [hashicorp/consul](https://github.com/hashicorp/consul) · **License:** BUSL-1.1; Additional Use Grant · **Kiểm:** 2026-11-23, `docs-read`, [`6b6e7dc3325a`](https://github.com/hashicorp/consul/tree/6b6e7dc3325aad31b26d17d800276d5549546831) (commit 2026-11-23). **Sao:** 30,116 tại 2026-11-23 theo [GitHub API](https://api.github.com/repos/hashicorp/consul).

| Mục | Đánh giá |
|---|---|
| Mục đích | Hệ thống discovery, health check, cấu hình động và service mesh cho hạ tầng phân tán. |
| Giá trị và cơ chế theo tài liệu | README mô tả DNS/HTTP discovery, gateway và TLS theo danh tính; Go module tách API/SDK giúp xác định điểm tích hợp. |
| Giới hạn | LICENSE hiện tại có giới hạn đối với sản phẩm cạnh tranh theo định nghĩa, không phải nhãn nguồn mở thuần. Khả năng HA và bảo vệ mesh chưa được thử dưới lỗi. |
| Điều kiện tích hợp | Kiểm mô hình sử dụng với license của release, thử discovery/ACL/TLS và quorum; chuẩn bị snapshot, rotation và hành vi khi control plane mất kết nối. |
| Lựa chọn đối chiếu | [etcd](../34-backend-data-identity-integration/README.md#anhkysuai-etcd-io-etcd); ZooKeeper; Kubernetes discovery. |

**Phạm vi bằng chứng:** đã clone, đọc trích đoạn tài liệu, giấy phép và các file cấu hình được dẫn dưới đây; chưa chạy mã, build, benchmark hoặc test upstream. `docs-read` không phải kiểm chứng implementation.

**Nguồn tại cùng SHA:** [README.md](https://github.com/hashicorp/consul/blob/6b6e7dc3325aad31b26d17d800276d5549546831/README.md) · [LICENSE](https://github.com/hashicorp/consul/blob/6b6e7dc3325aad31b26d17d800276d5549546831/LICENSE) · [go.mod](https://github.com/hashicorp/consul/blob/6b6e7dc3325aad31b26d17d800276d5549546831/go.mod) · [.github/workflows/build.yml](https://github.com/hashicorp/consul/blob/6b6e7dc3325aad31b26d17d800276d5549546831/.github/workflows/build.yml).

<a id="anhkysuai-apolloconfig-apollo"></a>

### Apollo Configuration Center

**Repo:** [apolloconfig/apollo](https://github.com/apolloconfig/apollo) · **License:** Apache-2.0 · **Kiểm:** 2026-11-23, `docs-read`, [`69a2b1fc0ef4`](https://github.com/apolloconfig/apollo/tree/69a2b1fc0ef43744f9357b07ad1912c54981b38c) (commit 2026-11-21). **Sao:** 29,814 tại 2026-11-23 theo [GitHub API](https://api.github.com/repos/apolloconfig/apollo).

| Mục | Đánh giá |
|---|---|
| Mục đích | Trung tâm cấu hình cho nhiều ứng dụng, môi trường và cluster. |
| Giá trị và cơ chế theo tài liệu | README mô tả server Spring Boot/Cloud và SDK Java/.NET; Maven/CI theo JDK hỗ trợ đánh giá tương thích nền tảng và quản lý cấu hình tập trung. |
| Giới hạn | Không liên quan Apollo GraphQL dù cùng tên. Tuyên bố tin cậy chưa được fault-test; thay đổi cấu hình có thể tác động đồng thời nhiều dịch vụ. |
| Điều kiện tích hợp | Thử namespace/môi trường riêng, kiểm quyền phát hành và rollback; đo client nhận cập nhật, cache khi mất mạng và lịch sử audit trước khi dùng production. |
| Lựa chọn đối chiếu | Spring Cloud Config; Consul KV; [Nacos](../08-awesome-lists-learning/README.md#6c55-container--devops). |

**Phạm vi bằng chứng:** đã clone, đọc trích đoạn tài liệu, giấy phép và các file cấu hình được dẫn dưới đây; chưa chạy mã, build, benchmark hoặc test upstream. `docs-read` không phải kiểm chứng implementation.

**Nguồn tại cùng SHA:** [README.md](https://github.com/apolloconfig/apollo/blob/69a2b1fc0ef43744f9357b07ad1912c54981b38c/README.md) · [LICENSE](https://github.com/apolloconfig/apollo/blob/69a2b1fc0ef43744f9357b07ad1912c54981b38c/LICENSE) · [pom.xml](https://github.com/apolloconfig/apollo/blob/69a2b1fc0ef43744f9357b07ad1912c54981b38c/pom.xml) · [.github/workflows/build.yml](https://github.com/apolloconfig/apollo/blob/69a2b1fc0ef43744f9357b07ad1912c54981b38c/.github/workflows/build.yml).

<a id="anhkysuai-authelia-authelia"></a>

### Authelia

**Repo:** [authelia/authelia](https://github.com/authelia/authelia) · **License:** Apache-2.0 · **Kiểm:** 2026-11-23, `docs-read`, [`b935f93f891a`](https://github.com/authelia/authelia/tree/b935f93f891abf928d7cdee14bc1f8f32c7044cd) (commit 2026-11-23). **Sao:** 29,710 tại 2026-11-23 theo [GitHub API](https://api.github.com/repos/authelia/authelia).

| Mục | Đánh giá |
|---|---|
| Mục đích | Máy chủ SSO/MFA làm cổng xác thực và ủy quyền cho ứng dụng phía sau reverse proxy. |
| Giá trị và cơ chế theo tài liệu | README mô tả OIDC/OAuth2, passkey, TOTP và cách allow/deny/redirect; Go manifest cùng workflow provenance làm điểm kiểm nguồn phát hành. |
| Giới hạn | Bảo vệ phụ thuộc cấu hình proxy và đường bypass; chứng nhận hoặc post-quantum trong mô tả không thay kiểm hệ thống đích. Helm chart được README đánh dấu beta. |
| Điều kiện tích hợp | Thử cả truy cập hợp lệ/lối tắt trực tiếp backend, cấu hình cookie/TLS và recovery; kiểm scope OIDC, secret rotation và log trước khi bảo vệ ứng dụng thật. |
| Lựa chọn đối chiếu | [Authentik](../34-backend-data-identity-integration/README.md#anhkysuai-goauthentik-authentik); [Keycloak](../34-backend-data-identity-integration/README.md#keycloak); Ory. |

**Phạm vi bằng chứng:** đã clone, đọc trích đoạn tài liệu, giấy phép và các file cấu hình được dẫn dưới đây; chưa chạy mã, build, benchmark hoặc test upstream. `docs-read` không phải kiểm chứng implementation.

**Nguồn tại cùng SHA:** [README.md](https://github.com/authelia/authelia/blob/b935f93f891abf928d7cdee14bc1f8f32c7044cd/README.md) · [LICENSE](https://github.com/authelia/authelia/blob/b935f93f891abf928d7cdee14bc1f8f32c7044cd/LICENSE) · [go.mod](https://github.com/authelia/authelia/blob/b935f93f891abf928d7cdee14bc1f8f32c7044cd/go.mod) · [.github/workflows/slsa.yml](https://github.com/authelia/authelia/blob/b935f93f891abf928d7cdee14bc1f8f32c7044cd/.github/workflows/slsa.yml).

<a id="anhkysuai-alibaba-spring-cloud-alibaba"></a>

### Spring Cloud Alibaba

**Repo:** [alibaba/spring-cloud-alibaba](https://github.com/alibaba/spring-cloud-alibaba) · **License:** Apache-2.0 · **Kiểm:** 2026-11-23, `docs-read`, [`1290d136d91b`](https://github.com/alibaba/spring-cloud-alibaba/tree/1290d136d91ba4f3a6764f0429a8aa65ccde9ec0) (commit 2026-11-14). **Sao:** 29,156 tại 2026-11-23 theo [GitHub API](https://api.github.com/repos/alibaba/spring-cloud-alibaba).

| Mục | Đánh giá |
|---|---|
| Mục đích | Bộ tích hợp middleware Alibaba cho ứng dụng Spring Cloud phân tán. |
| Giá trị và cơ chế theo tài liệu | README gom discovery, cấu hình động, flow control, event và transaction qua starter/annotation; Maven parent cho biết quan hệ với Spring Cloud build. |
| Giới hạn | Thêm annotation không chứng minh tính đúng giao dịch hoặc chịu lỗi. Cần khớp version matrix Spring Boot/Cloud/middleware; workflow đã đọc chỉ kiểm liên kết tài liệu. |
| Điều kiện tích hợp | Chọn BOM phù hợp, chỉ bật component cần dùng; thử refresh cấu hình, circuit breaker và lỗi dịch vụ trên staging trước khi đưa vào toàn hệ. |
| Lựa chọn đối chiếu | Spring Cloud gốc; Dubbo; Quarkus. |

**Phạm vi bằng chứng:** đã clone, đọc trích đoạn tài liệu, giấy phép và các file cấu hình được dẫn dưới đây; chưa chạy mã, build, benchmark hoặc test upstream. `docs-read` không phải kiểm chứng implementation.

**Nguồn tại cùng SHA:** [README.md](https://github.com/alibaba/spring-cloud-alibaba/blob/1290d136d91ba4f3a6764f0429a8aa65ccde9ec0/README.md) · [LICENSE](https://github.com/alibaba/spring-cloud-alibaba/blob/1290d136d91ba4f3a6764f0429a8aa65ccde9ec0/LICENSE) · [pom.xml](https://github.com/alibaba/spring-cloud-alibaba/blob/1290d136d91ba4f3a6764f0429a8aa65ccde9ec0/pom.xml) · [.github/workflows/md-link-check.yml](https://github.com/alibaba/spring-cloud-alibaba/blob/1290d136d91ba4f3a6764f0429a8aa65ccde9ec0/.github/workflows/md-link-check.yml).

<a id="anhkysuai-swagger-api-swagger-ui"></a>

### Swagger UI

**Repo:** [swagger-api/swagger-ui](https://github.com/swagger-api/swagger-ui) · **License:** Apache-2.0 · **Kiểm:** 2026-11-23, `docs-read`, [`d157bfe09171`](https://github.com/swagger-api/swagger-ui/tree/d157bfe091710f3a21d4c3be55985293d84b6e57) (commit 2026-11-23). **Sao:** 29,087 tại 2026-11-23 theo [GitHub API](https://api.github.com/repos/swagger-api/swagger-ui).

| Mục | Đánh giá |
|---|---|
| Mục đích | Giao diện hiển thị và tương tác với API sinh từ OpenAPI specification. |
| Giá trị và cơ chế theo tài liệu | README phân biệt swagger-ui, swagger-ui-dist và swagger-ui-react; workflow build/publish Docker cung cấp các cách nhúng vào cổng tài liệu. |
| Giới hạn | Tài liệu đẹp không chứng minh spec khớp implementation. Try-it-out có thể gửi request thật; chưa kiểm auth, CORS hoặc nội dung spec không tin cậy. |
| Điều kiện tích hợp | Chọn gói đúng framework, ghim spec và phiên bản UI; dùng môi trường thử cho thao tác ghi, giới hạn token và kiểm đồng bộ API trong CI ứng dụng. |
| Lựa chọn đối chiếu | Scalar; Redoc; RapiDoc. |

**Phạm vi bằng chứng:** đã clone, đọc trích đoạn tài liệu, giấy phép và các file cấu hình được dẫn dưới đây; chưa chạy mã, build, benchmark hoặc test upstream. `docs-read` không phải kiểm chứng implementation.

**Nguồn tại cùng SHA:** [README.md](https://github.com/swagger-api/swagger-ui/blob/d157bfe091710f3a21d4c3be55985293d84b6e57/README.md) · [LICENSE](https://github.com/swagger-api/swagger-ui/blob/d157bfe091710f3a21d4c3be55985293d84b6e57/LICENSE) · [package.json](https://github.com/swagger-api/swagger-ui/blob/d157bfe091710f3a21d4c3be55985293d84b6e57/package.json) · [composer.json](https://github.com/swagger-api/swagger-ui/blob/d157bfe091710f3a21d4c3be55985293d84b6e57/composer.json) · [.github/workflows/docker-build-push.yml](https://github.com/swagger-api/swagger-ui/blob/d157bfe091710f3a21d4c3be55985293d84b6e57/.github/workflows/docker-build-push.yml).

<a id="anhkysuai-cloudreve-cloudreve"></a>

### Cloudreve

**Đã chuyển (2026-11-23):** hồ sơ này nay nằm ở [mục 36](../36-self-hosting-homelab/README.md#anhkysuai-cloudreve-cloudreve); catalog con xem [catalog/](../catalog/README.md).

<a id="anhkysuai-mongodb-mongo"></a>

### MongoDB Community Server

**Repo:** [mongodb/mongo](https://github.com/mongodb/mongo) · **License:** SSPL-1.0 · **Kiểm:** 2026-11-23, `docs-read`, [`b5fcd1f2c092`](https://github.com/mongodb/mongo/tree/b5fcd1f2c0923b194122d0840475204f83b9647e) (commit 2026-11-23). **Sao:** 28,706 tại 2026-11-23 theo [GitHub API](https://api.github.com/repos/mongodb/mongo).

| Mục | Đánh giá |
|---|---|
| Mục đích | Mã máy chủ MongoDB và router sharding mongos. |
| Giá trị và cơ chế theo tài liệu | README phân biệt server, shell, Compass và driver riêng; cây build/manifest hỗ trợ xác định đây là engine database, không phải gói Node mang version mẫu. |
| Giới hạn | LICENSE hiện hành là SSPL, không suy Apache hay AGPL từ lịch sử phiên bản. Chưa kiểm replication, sharding hoặc truy vấn; shell/client ngoài repo chưa được review. |
| Điều kiện tích hợp | Kiểm điều khoản cung cấp dịch vụ và release hỗ trợ, thử index/query/migration thật; cấu hình xác thực, backup và phục hồi trước khi nhập dữ liệu production. |
| Lựa chọn đối chiếu | PostgreSQL JSONB; CouchDB; FerretDB. |

**Phạm vi bằng chứng:** đã clone, đọc trích đoạn tài liệu, giấy phép và các file cấu hình được dẫn dưới đây; chưa chạy mã, build, benchmark hoặc test upstream. `docs-read` không phải kiểm chứng implementation.

**Nguồn tại cùng SHA:** [README.md](https://github.com/mongodb/mongo/blob/b5fcd1f2c0923b194122d0840475204f83b9647e/README.md) · [LICENSE-Community.txt](https://github.com/mongodb/mongo/blob/b5fcd1f2c0923b194122d0840475204f83b9647e/LICENSE-Community.txt) · [package.json](https://github.com/mongodb/mongo/blob/b5fcd1f2c0923b194122d0840475204f83b9647e/package.json) · [pyproject.toml](https://github.com/mongodb/mongo/blob/b5fcd1f2c0923b194122d0840475204f83b9647e/pyproject.toml).

<a id="anhkysuai-bagisto-bagisto"></a>

### Bagisto

**Repo:** [bagisto/bagisto](https://github.com/bagisto/bagisto) · **License:** MIT · **Kiểm:** 2026-11-23, `docs-read`, [`ac4bd606e7a5`](https://github.com/bagisto/bagisto/tree/ac4bd606e7a57061c8abe3c204addfdad8a5f526) (commit 2026-11-18). **Sao:** 28,405 tại 2026-11-23 theo [GitHub API](https://api.github.com/repos/bagisto/bagisto).

| Mục | Đánh giá |
|---|---|
| Mục đích | Nền tảng thương mại điện tử Laravel/Vue để xây cửa hàng và mở rộng nghiệp vụ. |
| Giá trị và cơ chế theo tài liệu | README mô tả cách cài Composer/Docker và hướng marketplace; Composer nêu PHP 8.4, CI Pest theo database giúp đánh giá nền của ứng dụng. |
| Giới hạn | Không suy mọi extension multi-vendor/B2B trên website có trong core MIT. Các tuyên bố quy mô SKU chưa benchmark; ảnh Docker có seed/index sẵn cần rà trước production. |
| Điều kiện tích hợp | Thử checkout, tồn kho, tax và hoàn tiền bằng dữ liệu giả; chọn payment sandbox, kiểm quyền admin, migration và giấy phép extension trước khi bán hàng thật. |
| Lựa chọn đối chiếu | Saleor; [Medusa](../08-awesome-lists-learning/README.md#6c59-framework-backend); Sylius. |

**Phạm vi bằng chứng:** đã clone, đọc trích đoạn tài liệu, giấy phép và các file cấu hình được dẫn dưới đây; chưa chạy mã, build, benchmark hoặc test upstream. `docs-read` không phải kiểm chứng implementation.

**Nguồn tại cùng SHA:** [README.md](https://github.com/bagisto/bagisto/blob/ac4bd606e7a57061c8abe3c204addfdad8a5f526/README.md) · [LICENSE](https://github.com/bagisto/bagisto/blob/ac4bd606e7a57061c8abe3c204addfdad8a5f526/LICENSE) · [package.json](https://github.com/bagisto/bagisto/blob/ac4bd606e7a57061c8abe3c204addfdad8a5f526/package.json) · [composer.json](https://github.com/bagisto/bagisto/blob/ac4bd606e7a57061c8abe3c204addfdad8a5f526/composer.json) · [.github/workflows/pest-tests.yml](https://github.com/bagisto/bagisto/blob/ac4bd606e7a57061c8abe3c204addfdad8a5f526/.github/workflows/pest-tests.yml).

<a id="anhkysuai-nextauthjs-next-auth"></a>

### Auth.js

**Repo:** [nextauthjs/next-auth](https://github.com/nextauthjs/next-auth) · **License:** ISC · **Kiểm:** 2026-11-23, `docs-read`, [`a1a16a5a7780`](https://github.com/nextauthjs/next-auth/tree/a1a16a5a7780488c7449feece410033f445d0b31) (commit 2026-07-22). **Sao:** 28,390 tại 2026-11-23 theo [GitHub API](https://api.github.com/repos/nextauthjs/next-auth).

| Mục | Đánh giá |
|---|---|
| Mục đích | Bộ gói xác thực JavaScript dùng Web API chuẩn, hỗ trợ OAuth/OIDC và nhiều framework. |
| Giá trị và cơ chế theo tài liệu | README mô tả database adapter hoặc stateless session; ghi rõ Auth.js đã thuộc Better Auth và khuyến nghị dự án mới xem Better Auth trừ khoảng trống tính năng cụ thể. |
| Giới hạn | Khuyến nghị chuyển hướng không đồng nghĩa repo archived; metadata tại ngày kiểm vẫn không archived. Security-by-default là mô tả thiết kế, chưa kiểm callback/session của ứng dụng. |
| Điều kiện tích hợp | Đánh giá nhu cầu stateless và đường migration, ghim adapter/provider; thử đăng xuất, liên kết tài khoản, redirect và hồi phục truy cập trên staging. |
| Lựa chọn đối chiếu | [Better Auth](../34-backend-data-identity-integration/README.md#anhkysuai-better-auth-better-auth); Ory; [Keycloak](../34-backend-data-identity-integration/README.md#keycloak). |

**Phạm vi bằng chứng:** đã clone, đọc trích đoạn tài liệu, giấy phép và các file cấu hình được dẫn dưới đây; chưa chạy mã, build, benchmark hoặc test upstream. `docs-read` không phải kiểm chứng implementation.

**Nguồn tại cùng SHA:** [README.md](https://github.com/nextauthjs/next-auth/blob/a1a16a5a7780488c7449feece410033f445d0b31/README.md) · [LICENSE](https://github.com/nextauthjs/next-auth/blob/a1a16a5a7780488c7449feece410033f445d0b31/LICENSE) · [package.json](https://github.com/nextauthjs/next-auth/blob/a1a16a5a7780488c7449feece410033f445d0b31/package.json) · [.github/workflows/broken-link-checker.yml](https://github.com/nextauthjs/next-auth/blob/a1a16a5a7780488c7449feece410033f445d0b31/.github/workflows/broken-link-checker.yml).

<a id="anhkysuai-valkey-io-valkey"></a>

### Valkey

**Repo:** [valkey-io/valkey](https://github.com/valkey-io/valkey) · **License:** BSD-3-Clause · **Kiểm:** 2026-11-23, `docs-read`, [`28ef86b44342`](https://github.com/valkey-io/valkey/tree/28ef86b44342797ba1512b623b279287eaf979ba) (commit 2026-11-23). **Sao:** 27,839 tại 2026-11-23 theo [GitHub API](https://api.github.com/repos/valkey-io/valkey).

| Mục | Đánh giá |
|---|---|
| Mục đích | Máy chủ cấu trúc dữ liệu cho cache và workload khóa-giá trị thời gian thực. |
| Giá trị và cơ chế theo tài liệu | README xác nhận fork Redis trước đổi license; mô tả hệ build, TLS, module và giới hạn sentinel với TLS module, CI kiểm định nghĩa lệnh. |
| Giới hạn | Không suy tương thích mọi module hay lệnh Redis mới. Persistence, eviction và failover cần kiểm theo cấu hình; RDMA được ghi là thử nghiệm, chưa benchmark. |
| Điều kiện tích hợp | Thử client/lệnh đang dùng và chính sách TTL, bộ nhớ, persistence; kiểm replication/failover và phục hồi trước khi đổi cache hoặc queue backend. |
| Lựa chọn đối chiếu | [Redis](../08-awesome-lists-learning/README.md#6c511-giám-sát-csdl--phân-tích); [Dragonfly](../34-backend-data-identity-integration/README.md#anhkysuai-dragonflydb-dragonfly); KeyDB. |

**Phạm vi bằng chứng:** đã clone, đọc trích đoạn tài liệu, giấy phép và các file cấu hình được dẫn dưới đây; chưa chạy mã, build, benchmark hoặc test upstream. `docs-read` không phải kiểm chứng implementation.

**Nguồn tại cùng SHA:** [README.md](https://github.com/valkey-io/valkey/blob/28ef86b44342797ba1512b623b279287eaf979ba/README.md) · [COPYING](https://github.com/valkey-io/valkey/blob/28ef86b44342797ba1512b623b279287eaf979ba/COPYING) · [CMakeLists.txt](https://github.com/valkey-io/valkey/blob/28ef86b44342797ba1512b623b279287eaf979ba/CMakeLists.txt) · [.github/workflows/ci.yml](https://github.com/valkey-io/valkey/blob/28ef86b44342797ba1512b623b279287eaf979ba/.github/workflows/ci.yml).

<a id="anhkysuai-postgrest-postgrest"></a>

### PostgREST

**Repo:** [PostgREST/postgrest](https://github.com/PostgREST/postgrest) · **License:** MIT · **Kiểm:** 2026-11-23, `docs-read`, [`e1e95101e8d3`](https://github.com/PostgREST/postgrest/tree/e1e95101e8d37d24c07da7f3683a8c936e098f2c) (commit 2026-11-19). **Sao:** 27,763 tại 2026-11-23 theo [GitHub API](https://api.github.com/repos/PostgREST/postgrest).

| Mục | Đánh giá |
|---|---|
| Mục đích | Server tạo REST API từ PostgreSQL hiện có. |
| Giá trị và cơ chế theo tài liệu | README mô tả Haskell/Warp và việc đưa serialization, validation, authorization xuống database; CI tách check, docs, test và build. |
| Giới hạn | Phân quyền database trở thành ranh giới quan trọng của API. Các con số hiệu năng README chưa được tái lập; chưa kiểm JWT, role mapping, RLS hoặc query plan. |
| Điều kiện tích hợp | Thiết kế schema/view/role dành cho API, thử truy cập trái quyền và giới hạn truy vấn; kiểm schema cache, migration và proxy trước khi công khai endpoint. |
| Lựa chọn đối chiếu | Hasura; PostGraphile; [Django REST Framework](../34-backend-data-identity-integration/README.md#anhkysuai-encode-django-rest-framework). |

**Phạm vi bằng chứng:** đã clone, đọc trích đoạn tài liệu, giấy phép và các file cấu hình được dẫn dưới đây; chưa chạy mã, build, benchmark hoặc test upstream. `docs-read` không phải kiểm chứng implementation.

**Nguồn tại cùng SHA:** [README.md](https://github.com/PostgREST/postgrest/blob/e1e95101e8d37d24c07da7f3683a8c936e098f2c/README.md) · [LICENSE](https://github.com/PostgREST/postgrest/blob/e1e95101e8d37d24c07da7f3683a8c936e098f2c/LICENSE) · [.github/workflows/ci.yaml](https://github.com/PostgREST/postgrest/blob/e1e95101e8d37d24c07da7f3683a8c936e098f2c/.github/workflows/ci.yaml).

<a id="anhkysuai-goauthentik-authentik"></a>

### Authentik

**Repo:** [goauthentik/authentik](https://github.com/goauthentik/authentik) · **License:** MIT cho core/client; CC-BY-SA-4.0 website; enterprise riêng · **Kiểm:** 2026-11-23, `docs-read`, [`7e5db84abecb`](https://github.com/goauthentik/authentik/tree/7e5db84abecb04e48adca2166dec83236fc060f0) (commit 2026-11-20). **Sao:** 26,421 tại 2026-11-23 theo [GitHub API](https://api.github.com/repos/goauthentik/authentik).

| Mục | Đánh giá |
|---|---|
| Mục đích | Identity Provider tự host cho SSO qua SAML, OAuth2/OIDC, LDAP và RADIUS. |
| Giá trị và cơ chế theo tài liệu | README chỉ dẫn Compose cho nhỏ/thử và Helm cho quy mô lớn; manifest tại SHA là 2026.11.0-rc1, CI web kiểm frontend. |
| Giới hạn | LICENSE tách website, enterprise và core, nên không gắn MIT cho cả repo. Đây là RC; chưa kiểm flow xác thực, recovery, token hay cấu hình outpost. |
| Điều kiện tích hợp | Chọn release phù hợp, thử từng protocol với ứng dụng đích và tài khoản ít quyền; kiểm backup, MFA recovery, logout và nâng cấp trước khi thay IdP. |
| Lựa chọn đối chiếu | [Authelia](../34-backend-data-identity-integration/README.md#anhkysuai-authelia-authelia); [Keycloak](../34-backend-data-identity-integration/README.md#keycloak); Ory Kratos. |

**Phạm vi bằng chứng:** đã clone, đọc trích đoạn tài liệu, giấy phép và các file cấu hình được dẫn dưới đây; chưa chạy mã, build, benchmark hoặc test upstream. `docs-read` không phải kiểm chứng implementation.

**Nguồn tại cùng SHA:** [README.md](https://github.com/goauthentik/authentik/blob/7e5db84abecb04e48adca2166dec83236fc060f0/README.md) · [LICENSE](https://github.com/goauthentik/authentik/blob/7e5db84abecb04e48adca2166dec83236fc060f0/LICENSE) · [package.json](https://github.com/goauthentik/authentik/blob/7e5db84abecb04e48adca2166dec83236fc060f0/package.json) · [pyproject.toml](https://github.com/goauthentik/authentik/blob/7e5db84abecb04e48adca2166dec83236fc060f0/pyproject.toml) · [.github/workflows/ci-web.yml](https://github.com/goauthentik/authentik/blob/7e5db84abecb04e48adca2166dec83236fc060f0/.github/workflows/ci-web.yml).

<a id="anhkysuai-vapor-vapor"></a>

### Vapor

**Repo:** [vapor/vapor](https://github.com/vapor/vapor) · **License:** MIT · **Kiểm:** 2026-11-23, `docs-read`, [`e4a5b7050f5e`](https://github.com/vapor/vapor/tree/e4a5b7050f5e9e5793be3ebdeb687eac92fd9965) (commit 2026-11-13). **Sao:** 26,233 tại 2026-11-23 theo [GitHub API](https://api.github.com/repos/vapor/vapor).

| Mục | Đánh giá |
|---|---|
| Mục đích | Framework HTTP phía server cho Swift để xây website, API và dịch vụ. |
| Giá trị và cơ chế theo tài liệu | README định vị nền tảng server Swift; cây repo có Swift Package và CI gọi workflow unit test dùng chung, phù hợp nhóm muốn chia sẻ ngôn ngữ Swift. |
| Giới hạn | Package.swift tại SHA yêu cầu Swift 6.4, nêu platform Apple mới và trait UnstableHTTP3; cần đối chiếu release phù hợp. Chưa kiểm runtime Linux, middleware hoặc hiệu năng. |
| Điều kiện tích hợp | Chọn release/toolchain theo tài liệu, thử endpoint và database adapter cần dùng; kiểm concurrency, shutdown, logging và deploy trên hệ điều hành đích. |
| Lựa chọn đối chiếu | Hummingbird; Kitura; FastAPI. |

**Phạm vi bằng chứng:** đã clone, đọc trích đoạn tài liệu, giấy phép và các file cấu hình được dẫn dưới đây; chưa chạy mã, build, benchmark hoặc test upstream. `docs-read` không phải kiểm chứng implementation.

**Nguồn tại cùng SHA:** [README.md](https://github.com/vapor/vapor/blob/e4a5b7050f5e9e5793be3ebdeb687eac92fd9965/README.md) · [LICENSE](https://github.com/vapor/vapor/blob/e4a5b7050f5e9e5793be3ebdeb687eac92fd9965/LICENSE) · [.github/workflows/test.yml](https://github.com/vapor/vapor/blob/e4a5b7050f5e9e5793be3ebdeb687eac92fd9965/.github/workflows/test.yml) · [Package.swift](https://github.com/vapor/vapor/blob/e4a5b7050f5e9e5793be3ebdeb687eac92fd9965/Package.swift).

<a id="anhkysuai-rwf2-rocket"></a>

### Rocket

**Repo:** [rwf2/Rocket](https://github.com/rwf2/Rocket) · **License:** MIT OR Apache-2.0 · **Kiểm:** 2026-11-23, `docs-read`, [`0ca096f705d6`](https://github.com/rwf2/Rocket/tree/0ca096f705d60082593a3e9b035d8c2a92595ca0) (commit 2026-11-21). **Sao:** 25,815 tại 2026-11-23 theo [GitHub API](https://api.github.com/repos/rwf2/Rocket).

| Mục | Đánh giá |
|---|---|
| Mục đích | Framework web async Rust với route macro và kiểu dữ liệu tham số. |
| Giá trị và cơ chế theo tài liệu | Ví dụ README cho thấy parse tham số u8 ảnh hưởng chọn route; Cargo tách core/codegen/http và module database/template/WebSocket, CI nhiều hệ điều hành. |
| Giới hạn | Route có kiểu không thay validation nghiệp vụ hoặc kiểm quyền. Tài liệu main khác từng release; chưa đọc implementation hay đo request parsing và concurrency. |
| Điều kiện tích hợp | Ghim Rust/Rocket, chọn contrib feature cần dùng và dùng docs cùng phiên bản; thử request không hợp lệ, error mapping, auth và shutdown trong ứng dụng. |
| Lựa chọn đối chiếu | Axum; Actix Web; Poem. |

**Phạm vi bằng chứng:** đã clone, đọc trích đoạn tài liệu, giấy phép và các file cấu hình được dẫn dưới đây; chưa chạy mã, build, benchmark hoặc test upstream. `docs-read` không phải kiểm chứng implementation.

**Nguồn tại cùng SHA:** [README.md](https://github.com/rwf2/Rocket/blob/0ca096f705d60082593a3e9b035d8c2a92595ca0/README.md) · [LICENSE-APACHE](https://github.com/rwf2/Rocket/blob/0ca096f705d60082593a3e9b035d8c2a92595ca0/LICENSE-APACHE) · [LICENSE-MIT](https://github.com/rwf2/Rocket/blob/0ca096f705d60082593a3e9b035d8c2a92595ca0/LICENSE-MIT) · [Cargo.toml](https://github.com/rwf2/Rocket/blob/0ca096f705d60082593a3e9b035d8c2a92595ca0/Cargo.toml) · [.github/workflows/ci.yml](https://github.com/rwf2/Rocket/blob/0ca096f705d60082593a3e9b035d8c2a92595ca0/.github/workflows/ci.yml).

<a id="anhkysuai-clockworklabs-spacetimedb"></a>

### SpacetimeDB

**Repo:** [clockworklabs/SpacetimeDB](https://github.com/clockworklabs/SpacetimeDB) · **License:** BUSL-1.1; grant và giấy phép thư mục riêng · **Kiểm:** 2026-11-23, `docs-read`, [`7bb7e80c08bb`](https://github.com/clockworklabs/SpacetimeDB/tree/7bb7e80c08bb80370e1e238d022b281d7beacc0c) (commit 2026-11-23). **Sao:** 25,569 tại 2026-11-23 theo [GitHub API](https://api.github.com/repos/clockworklabs/SpacetimeDB).

| Mục | Đánh giá |
|---|---|
| Mục đích | Database quan hệ đồng thời chạy logic module và đồng bộ state trực tiếp tới client. |
| Giá trị và cơ chế theo tài liệu | README mô tả module Rust/C#/TypeScript/C++ cho ứng dụng phản ứng và game; Cargo tách commitlog, datastore, durability, auth và engine. |
| Giới hạn | Grant hiện giới hạn một instance production và không dùng làm Database Service theo định nghĩa. Tuyên bố không cần DevOps/độ trễ thấp chưa được kiểm; quyền module vẫn phải thiết kế. |
| Điều kiện tích hợp | Kiểm license/SDK đúng phiên bản, thử đồng bộ, phân quyền và migration module; đo hot data, recovery và hành vi client mất kết nối trước khi dùng lâu dài. |
| Lựa chọn đối chiếu | Supabase Realtime; Convex; Nakama. |

**Phạm vi bằng chứng:** đã clone, đọc trích đoạn tài liệu, giấy phép và các file cấu hình được dẫn dưới đây; chưa chạy mã, build, benchmark hoặc test upstream. `docs-read` không phải kiểm chứng implementation.

**Nguồn tại cùng SHA:** [README.md](https://github.com/clockworklabs/SpacetimeDB/blob/7bb7e80c08bb80370e1e238d022b281d7beacc0c/README.md) · [LICENSE.txt](https://github.com/clockworklabs/SpacetimeDB/blob/7bb7e80c08bb80370e1e238d022b281d7beacc0c/LICENSE.txt) · [package.json](https://github.com/clockworklabs/SpacetimeDB/blob/7bb7e80c08bb80370e1e238d022b281d7beacc0c/package.json) · [Cargo.toml](https://github.com/clockworklabs/SpacetimeDB/blob/7bb7e80c08bb80370e1e238d022b281d7beacc0c/Cargo.toml) · [.github/workflows/ci.yml](https://github.com/clockworklabs/SpacetimeDB/blob/7bb7e80c08bb80370e1e238d022b281d7beacc0c/.github/workflows/ci.yml).

<a id="anhkysuai-kataras-iris"></a>

### Iris

**Repo:** [kataras/iris](https://github.com/kataras/iris) · **License:** BSD-3-Clause · **Kiểm:** 2026-11-23, `docs-read`, [`08666267f7f2`](https://github.com/kataras/iris/tree/08666267f7f2f0db48046b127e6fdb41a1002c6c) (commit 2026-11-13). **Sao:** 25,555 tại 2026-11-23 theo [GitHub API](https://api.github.com/repos/kataras/iris).

| Mục | Đánh giá |
|---|---|
| Mục đích | Framework web Go tích hợp routing tham số có kiểu, DI và xử lý lỗi. |
| Giá trị và cơ chế theo tài liệu | README định vị v14; go.mod yêu cầu Go 1.27 và CI chạy go test -race, giúp xác định bộ runtime và cổng kiểm cơ bản. |
| Giới hạn | Các khẳng định nhanh nhất, bảo mật mặc định và chi phí tốt chưa được benchmark/kiểm toán. Nhiều tiện ích tích hợp vẫn cần cấu hình và chọn đúng migration giữa major. |
| Điều kiện tích hợp | Ghim v14/runtime, dùng ví dụ nhỏ rồi kiểm middleware, validation và quyền; đo workload của ứng dụng và rà migration trước khi thay framework. |
| Lựa chọn đối chiếu | [Echo](../34-backend-data-identity-integration/README.md#anhkysuai-labstack-echo); [Fiber](../34-backend-data-identity-integration/README.md#anhkysuai-gofiber-fiber); [Chi](../34-backend-data-identity-integration/README.md#anhkysuai-go-chi-chi). |

**Phạm vi bằng chứng:** đã clone, đọc trích đoạn tài liệu, giấy phép và các file cấu hình được dẫn dưới đây; chưa chạy mã, build, benchmark hoặc test upstream. `docs-read` không phải kiểm chứng implementation.

**Nguồn tại cùng SHA:** [README.md](https://github.com/kataras/iris/blob/08666267f7f2f0db48046b127e6fdb41a1002c6c/README.md) · [LICENSE](https://github.com/kataras/iris/blob/08666267f7f2f0db48046b127e6fdb41a1002c6c/LICENSE) · [go.mod](https://github.com/kataras/iris/blob/08666267f7f2f0db48046b127e6fdb41a1002c6c/go.mod) · [.github/workflows/ci.yml](https://github.com/kataras/iris/blob/08666267f7f2f0db48046b127e6fdb41a1002c6c/.github/workflows/ci.yml).

<a id="anhkysuai-tursodatabase-turso"></a>

### Turso Database

**Repo:** [tursodatabase/turso](https://github.com/tursodatabase/turso) · **License:** MIT · **Kiểm:** 2026-11-23, `docs-read`, [`570cb22d1d91`](https://github.com/tursodatabase/turso/tree/570cb22d1d91d2524761f0fa761e0a0fd8f4765c) (commit 2026-11-23). **Sao:** 25,323 tại 2026-11-23 theo [GitHub API](https://api.github.com/repos/tursodatabase/turso).

| Mục | Đánh giá |
|---|---|
| Mục đích | Database SQL Rust chạy trong tiến trình, tương thích SQLite và thử nghiệm frontend PostgreSQL. |
| Giá trị và cơ chế theo tài liệu | README giải thích VDBE chung cho các dialect, CDC/MVCC và binding; workflow SQL conformance kiểm cả SQLite lẫn PostgreSQL. |
| Giới hạn | FAQ nói chưa đến 1.0 và chưa tương thích SQLite 100%; Postgres frontend còn thử nghiệm. Tuyên bố production của upstream không thay kiểm tính đúng dữ liệu riêng. |
| Điều kiện tích hợp | Đối chiếu COMPAT theo SQL/file/C API đang dùng, thử migration và recovery; giữ backup độc lập, chọn binding và tính năng đã ổn định cho workload đích. |
| Lựa chọn đối chiếu | SQLite; libSQL; DuckDB. |

**Phạm vi bằng chứng:** đã clone, đọc trích đoạn tài liệu, giấy phép và các file cấu hình được dẫn dưới đây; chưa chạy mã, build, benchmark hoặc test upstream. `docs-read` không phải kiểm chứng implementation.

**Nguồn tại cùng SHA:** [README.md](https://github.com/tursodatabase/turso/blob/570cb22d1d91d2524761f0fa761e0a0fd8f4765c/README.md) · [LICENSE.md](https://github.com/tursodatabase/turso/blob/570cb22d1d91d2524761f0fa761e0a0fd8f4765c/LICENSE.md) · [pyproject.toml](https://github.com/tursodatabase/turso/blob/570cb22d1d91d2524761f0fa761e0a0fd8f4765c/pyproject.toml) · [Cargo.toml](https://github.com/tursodatabase/turso/blob/570cb22d1d91d2524761f0fa761e0a0fd8f4765c/Cargo.toml) · [.github/workflows/sqltest.yml](https://github.com/tursodatabase/turso/blob/570cb22d1d91d2524761f0fa761e0a0fd8f4765c/.github/workflows/sqltest.yml).

<a id="anhkysuai-taosdata-tdengine"></a>

### TDengine

**Repo:** [taosdata/TDengine](https://github.com/taosdata/TDengine) · **License:** AGPL-3.0 · **Kiểm:** 2026-11-23, `docs-read`, [`e5bf3b82b611`](https://github.com/taosdata/TDengine/tree/e5bf3b82b611daab89e0cf22724c5f3f73ddc997) (commit 2026-11-03). **Sao:** 25,204 tại 2026-11-23 theo [GitHub API](https://api.github.com/repos/taosdata/TDengine).

| Mục | Đánh giá |
|---|---|
| Mục đích | Cơ sở dữ liệu time series hướng IoT và dữ liệu công nghiệp. |
| Giá trị và cơ chế theo tài liệu | README mô tả ingestion, stream, subscription, phân vùng và tích hợp AI; cây build CMake và CI theo nền tảng cho thấy engine native. |
| Giới hạn | Các tuyên bố duy nhất giải quyết cardinality, TB/PB mỗi ngày hay tốc độ vượt trội chưa benchmark. Phạm vi community/cloud/AI cần đối chiếu; chưa kiểm replication hoặc mất node. |
| Điều kiện tích hợp | Đo ingest/query trên schema sensor thực tế, kiểm retention/downsampling và timestamp lệch; thử backup/restore và quyền connector trước khi đưa dữ liệu thiết bị thật vào. |
| Lựa chọn đối chiếu | InfluxDB; [TimescaleDB](../34-backend-data-identity-integration/README.md#anhkysuai-timescale-timescaledb); QuestDB. |

**Phạm vi bằng chứng:** đã clone, đọc trích đoạn tài liệu, giấy phép và các file cấu hình được dẫn dưới đây; chưa chạy mã, build, benchmark hoặc test upstream. `docs-read` không phải kiểm chứng implementation.

**Nguồn tại cùng SHA:** [README.md](https://github.com/taosdata/TDengine/blob/e5bf3b82b611daab89e0cf22724c5f3f73ddc997/README.md) · [LICENSE](https://github.com/taosdata/TDengine/blob/e5bf3b82b611daab89e0cf22724c5f3f73ddc997/LICENSE) · [CMakeLists.txt](https://github.com/taosdata/TDengine/blob/e5bf3b82b611daab89e0cf22724c5f3f73ddc997/CMakeLists.txt) · [.github/workflows/tdengine-test.yml](https://github.com/taosdata/TDengine/blob/e5bf3b82b611daab89e0cf22724c5f3f73ddc997/.github/workflows/tdengine-test.yml).

<a id="anhkysuai-navidrome-navidrome"></a>

### Navidrome

**Đã chuyển (2026-11-23):** hồ sơ này nay nằm ở [mục 36](../36-self-hosting-homelab/README.md#anhkysuai-navidrome-navidrome); catalog con xem [catalog/](../catalog/README.md).

<a id="anhkysuai-krayin-laravel-crm"></a>

### Krayin CRM

**Repo:** [krayin/laravel-crm](https://github.com/krayin/laravel-crm) · **License:** MIT · **Kiểm:** 2026-11-23, `docs-read`, [`64ef70505c5d`](https://github.com/krayin/laravel-crm/tree/64ef70505c5d4320231420bb21adf99dd1698e4e) (commit 2026-11-17). **Sao:** 24,197 tại 2026-11-23 theo [GitHub API](https://api.github.com/repos/krayin/laravel-crm).

| Mục | Đánh giá |
|---|---|
| Mục đích | CRM Laravel/Vue cho quản lý khách hàng, lead và hoạt động bán hàng. |
| Giá trị và cơ chế theo tài liệu | README nêu modular approach, custom attributes và parse email qua SendGrid; Composer yêu cầu PHP 8.3, CI dựng ứng dụng qua installer. |
| Giới hạn | Module mẫu chưa chứng minh phù hợp mọi quy trình bán hàng. Dữ liệu liên hệ/email và plugin cloud có phạm vi quyền riêng; chưa kiểm tenant, phân quyền hoặc import dữ liệu. |
| Điều kiện tích hợp | Thử pipeline lead với dữ liệu giả, chốt custom fields và policy theo vai trò; kiểm email integration, export/backup và migration trước nhập dữ liệu khách hàng thật. |
| Lựa chọn đối chiếu | [Twenty](../34-backend-data-identity-integration/README.md#anhkysuai-twentyhq-twenty); EspoCRM; SuiteCRM. |

**Phạm vi bằng chứng:** đã clone, đọc trích đoạn tài liệu, giấy phép và các file cấu hình được dẫn dưới đây; chưa chạy mã, build, benchmark hoặc test upstream. `docs-read` không phải kiểm chứng implementation.

**Nguồn tại cùng SHA:** [README.md](https://github.com/krayin/laravel-crm/blob/64ef70505c5d4320231420bb21adf99dd1698e4e/README.md) · [LICENSE](https://github.com/krayin/laravel-crm/blob/64ef70505c5d4320231420bb21adf99dd1698e4e/LICENSE) · [package.json](https://github.com/krayin/laravel-crm/blob/64ef70505c5d4320231420bb21adf99dd1698e4e/package.json) · [composer.json](https://github.com/krayin/laravel-crm/blob/64ef70505c5d4320231420bb21adf99dd1698e4e/composer.json) · [.github/workflows/ci.yml](https://github.com/krayin/laravel-crm/blob/64ef70505c5d4320231420bb21adf99dd1698e4e/.github/workflows/ci.yml).

<a id="anhkysuai-timescale-timescaledb"></a>

### TimescaleDB

**Repo:** [timescale/timescaledb](https://github.com/timescale/timescaledb) · **License:** Apache-2.0 ngoài tsl; Timescale License trong tsl · **Kiểm:** 2026-11-23, `docs-read`, [`96ddfc3e9a5a`](https://github.com/timescale/timescaledb/tree/96ddfc3e9a5ab253dfd45e04bbfb1e638503ee2c) (commit 2026-11-22). **Sao:** 23,889 tại 2026-11-23 theo [GitHub API](https://api.github.com/repos/timescale/timescaledb).

| Mục | Đánh giá |
|---|---|
| Mục đích | Extension PostgreSQL cho time series và truy vấn phân tích. |
| Giá trị và cơ chế theo tài liệu | README minh họa hypertable/columnstore; LICENSE phân tách mã và shared object tsl, CMake có APACHE_ONLY để chọn phạm vi build. |
| Giới hạn | Script cài nhanh được đánh dấu chỉ dùng local/test. Tính năng trong tsl chịu Timescale License riêng, không thể suy Apache cho toàn bộ; chưa đo hiệu năng hoặc kiểm nâng cấp extension. |
| Điều kiện tích hợp | Chọn đúng bản PostgreSQL/extension và phạm vi license, thử ingest/query/retention; kiểm backup, restore và upgrade trên bản sao dữ liệu trước production. |
| Lựa chọn đối chiếu | InfluxDB; QuestDB; PostgreSQL partitioning. |

**Phạm vi bằng chứng:** đã clone, đọc trích đoạn tài liệu, giấy phép và các file cấu hình được dẫn dưới đây; chưa chạy mã, build, benchmark hoặc test upstream. `docs-read` không phải kiểm chứng implementation.

**Nguồn tại cùng SHA:** [README.md](https://github.com/timescale/timescaledb/blob/96ddfc3e9a5ab253dfd45e04bbfb1e638503ee2c/README.md) · [LICENSE](https://github.com/timescale/timescaledb/blob/96ddfc3e9a5ab253dfd45e04bbfb1e638503ee2c/LICENSE) · [LICENSE-APACHE](https://github.com/timescale/timescaledb/blob/96ddfc3e9a5ab253dfd45e04bbfb1e638503ee2c/LICENSE-APACHE) · [CMakeLists.txt](https://github.com/timescale/timescaledb/blob/96ddfc3e9a5ab253dfd45e04bbfb1e638503ee2c/CMakeLists.txt) · [.github/workflows/coccinelle.yaml](https://github.com/timescale/timescaledb/blob/96ddfc3e9a5ab253dfd45e04bbfb1e638503ee2c/.github/workflows/coccinelle.yaml).

<a id="anhkysuai-saleor-saleor"></a>

### Saleor Core

**Repo:** [saleor/saleor](https://github.com/saleor/saleor) · **License:** BSD-3-Clause · **Kiểm:** 2026-11-23, `docs-read`, [`e1ccf4d58002`](https://github.com/saleor/saleor/tree/e1ccf4d580025b06c2ff01441a1e798dc4635f24) (commit 2026-11-20). **Sao:** 23,595 tại 2026-11-23 theo [GitHub API](https://api.github.com/repos/saleor/saleor).

| Mục | Đánh giá |
|---|---|
| Mục đích | Backend thương mại điện tử headless chỉ giao tiếp qua GraphQL. |
| Giá trị và cơ chế theo tài liệu | README mô tả channel cho giá/tiền tệ/tồn kho và mở rộng bằng webhook/apps; Python manifest cùng CI unit tests làm rõ core tách storefront/dashboard. |
| Giới hạn | Nhánh đọc mang phiên bản alpha 3.24; API-only vẫn cần xây giao diện và quản lý integration. Chưa kiểm checkout, concurrency tồn kho hay webhook retry. |
| Điều kiện tích hợp | Dùng payment sandbox, thử một channel với giá/stock/thuế; kiểm quyền app, event ordering và tính nhất quán đơn hàng trước khi đưa giao dịch thật vào. |
| Lựa chọn đối chiếu | [Medusa](../08-awesome-lists-learning/README.md#6c59-framework-backend); [Bagisto](../34-backend-data-identity-integration/README.md#anhkysuai-bagisto-bagisto); Vendure. |

**Phạm vi bằng chứng:** đã clone, đọc trích đoạn tài liệu, giấy phép và các file cấu hình được dẫn dưới đây; chưa chạy mã, build, benchmark hoặc test upstream. `docs-read` không phải kiểm chứng implementation.

**Nguồn tại cùng SHA:** [README.md](https://github.com/saleor/saleor/blob/e1ccf4d580025b06c2ff01441a1e798dc4635f24/README.md) · [LICENSE](https://github.com/saleor/saleor/blob/e1ccf4d580025b06c2ff01441a1e798dc4635f24/LICENSE) · [package.json](https://github.com/saleor/saleor/blob/e1ccf4d580025b06c2ff01441a1e798dc4635f24/package.json) · [pyproject.toml](https://github.com/saleor/saleor/blob/e1ccf4d580025b06c2ff01441a1e798dc4635f24/pyproject.toml) · [.github/workflows/tests.yaml](https://github.com/saleor/saleor/blob/e1ccf4d580025b06c2ff01441a1e798dc4635f24/.github/workflows/tests.yaml).

<a id="anhkysuai-pubkey-rxdb"></a>

### RxDB

**Repo:** [pubkey/rxdb](https://github.com/pubkey/rxdb) · **License:** Apache-2.0 cho repo; premium plugins có phạm vi riêng · **Kiểm:** 2026-11-23, `docs-read`, [`f470b46f79d7`](https://github.com/pubkey/rxdb/tree/f470b46f79d74b9ac6c3f8e738aaedbea6093f9c) (commit 2026-11-23). **Sao:** 23,440 tại 2026-11-23 theo [GitHub API](https://api.github.com/repos/pubkey/rxdb).

| Mục | Đánh giá |
|---|---|
| Mục đích | Database NoSQL JavaScript ưu tiên dữ liệu local với truy vấn reactive và đồng bộ backend. |
| Giá trị và cơ chế theo tài liệu | README mô tả subscribe thay đổi, protocol replication qua HTTP và adapter; package có test Node/browser, workflow build docs. |
| Giới hạn | Sync engine không tự giải quyết xung đột nghiệp vụ hay quyền backend. Premium plugin được bán riêng; chưa kiểm offline recovery, quota browser hoặc hiệu năng storage adapter. |
| Điều kiện tích hợp | Chọn storage/replication adapter, thử mất mạng, conflict và migration schema; backend vẫn phải xác thực/quyền mỗi thao tác, sao lưu dữ liệu cần giữ ngoài browser. |
| Lựa chọn đối chiếu | PouchDB; Dexie; ElectricSQL. |

**Phạm vi bằng chứng:** đã clone, đọc trích đoạn tài liệu, giấy phép và các file cấu hình được dẫn dưới đây; chưa chạy mã, build, benchmark hoặc test upstream. `docs-read` không phải kiểm chứng implementation.

**Nguồn tại cùng SHA:** [README.md](https://github.com/pubkey/rxdb/blob/f470b46f79d74b9ac6c3f8e738aaedbea6093f9c/README.md) · [LICENSE.txt](https://github.com/pubkey/rxdb/blob/f470b46f79d74b9ac6c3f8e738aaedbea6093f9c/LICENSE.txt) · [package.json](https://github.com/pubkey/rxdb/blob/f470b46f79d74b9ac6c3f8e738aaedbea6093f9c/package.json) · [.github/workflows/build.yml](https://github.com/pubkey/rxdb/blob/f470b46f79d74b9ac6c3f8e738aaedbea6093f9c/.github/workflows/build.yml).

<a id="anhkysuai-neondatabase-neon"></a>

### Neon Storage Engine

**Repo:** [neondatabase/neon](https://github.com/neondatabase/neon) · **License:** Apache-2.0 · **Kiểm:** 2026-11-23, `docs-read`, [`fa504217c61b`](https://github.com/neondatabase/neon/tree/fa504217c61bbcaf5c512d75830564541f917f8f) (commit 2026-08-31). **Sao:** 23,381 tại 2026-11-23 theo [GitHub API](https://api.github.com/repos/neondatabase/neon).

| Mục | Đánh giá |
|---|---|
| Mục đích | Nền tảng PostgreSQL tách compute và storage. |
| Giá trị và cơ chế theo tài liệu | README phân biệt compute node, pageserver và safekeeper nhận WAL; Cargo tách các service/storage controller, hướng dẫn local dành cho thí nghiệm và đổi mã. |
| Giới hạn | Repo engine không đồng nghĩa mọi khả năng managed Neon có thể tự host tương đương. Chưa kiểm durability, branching, scale-to-zero hay overhead lưu trữ. |
| Điều kiện tích hợp | Dùng môi trường thử để đọc đường WAL/pageserver, kiểm phiên bản PostgreSQL và object store; đo phục hồi, retention và cost trước khi vận hành platform riêng. |
| Lựa chọn đối chiếu | PostgreSQL chuẩn; CloudNativePG; Aurora PostgreSQL. |

**Phạm vi bằng chứng:** đã clone, đọc trích đoạn tài liệu, giấy phép và các file cấu hình được dẫn dưới đây; chưa chạy mã, build, benchmark hoặc test upstream. `docs-read` không phải kiểm chứng implementation.

**Nguồn tại cùng SHA:** [README.md](https://github.com/neondatabase/neon/blob/fa504217c61bbcaf5c512d75830564541f917f8f/README.md) · [LICENSE](https://github.com/neondatabase/neon/blob/fa504217c61bbcaf5c512d75830564541f917f8f/LICENSE) · [pyproject.toml](https://github.com/neondatabase/neon/blob/fa504217c61bbcaf5c512d75830564541f917f8f/pyproject.toml) · [Cargo.toml](https://github.com/neondatabase/neon/blob/fa504217c61bbcaf5c512d75830564541f917f8f/Cargo.toml) · [.github/workflows/build-macos.yml](https://github.com/neondatabase/neon/blob/fa504217c61bbcaf5c512d75830564541f917f8f/.github/workflows/build-macos.yml).

<a id="anhkysuai-phoenixframework-phoenix"></a>

### Phoenix Web Framework

**Repo:** [phoenixframework/phoenix](https://github.com/phoenixframework/phoenix) · **License:** MIT · **Kiểm:** 2026-11-23, `docs-read`, [`37d342122545`](https://github.com/phoenixframework/phoenix/tree/37d3421225455421bc47f94eee21460908538b15) (commit 2026-11-20). **Sao:** 23,226 tại 2026-11-23 theo [GitHub API](https://api.github.com/repos/phoenixframework/phoenix).

| Mục | Đánh giá |
|---|---|
| Mục đích | Framework web Elixir với installer và client JavaScript riêng. |
| Giá trị và cơ chế theo tài liệu | README giải thích tạo app bằng phx.new và tách docs release/main; mix.exs/package ghi 1.9.0-dev, CI matrix Elixir/OTP. |
| Giới hạn | Đây là Phoenix web, khác Arize Phoenix quan sát AI đã có trong kho. Nhánh đọc là development; chưa kiểm server, channel, LiveView hay dependency ngoài repo. |
| Điều kiện tích hợp | Chọn release tương thích Elixir/OTP, dùng installer tương ứng và thử endpoint/client; kiểm deployment, session, database adapter và nâng cấp trong ứng dụng tạo ra. |
| Lựa chọn đối chiếu | Rails; Django; Laravel. |

**Phạm vi bằng chứng:** đã clone, đọc trích đoạn tài liệu, giấy phép và các file cấu hình được dẫn dưới đây; chưa chạy mã, build, benchmark hoặc test upstream. `docs-read` không phải kiểm chứng implementation.

**Nguồn tại cùng SHA:** [README.md](https://github.com/phoenixframework/phoenix/blob/37d3421225455421bc47f94eee21460908538b15/README.md) · [LICENSE.md](https://github.com/phoenixframework/phoenix/blob/37d3421225455421bc47f94eee21460908538b15/LICENSE.md) · [package.json](https://github.com/phoenixframework/phoenix/blob/37d3421225455421bc47f94eee21460908538b15/package.json) · [mix.exs](https://github.com/phoenixframework/phoenix/blob/37d3421225455421bc47f94eee21460908538b15/mix.exs) · [.github/workflows/ci.yml](https://github.com/phoenixframework/phoenix/blob/37d3421225455421bc47f94eee21460908538b15/.github/workflows/ci.yml).

<a id="anhkysuai-go-chi-chi"></a>

### Chi

**Repo:** [go-chi/chi](https://github.com/go-chi/chi) · **License:** MIT · **Kiểm:** 2026-11-23, `docs-read`, [`c64ed7d6635f`](https://github.com/go-chi/chi/tree/c64ed7d6635f33a8b2feaff7dcfa55677023ac7d) (commit 2026-11-07). **Sao:** 23,145 tại 2026-11-23 theo [GitHub API](https://api.github.com/repos/go-chi/chi).

| Mục | Đánh giá |
|---|---|
| Mục đích | Router Go nhỏ, ghép middleware và route theo chuẩn net/http. |
| Giá trị và cơ chế theo tài liệu | README nhấn mạnh handler chuẩn, context/cancellation và các subpackage tùy chọn; go.mod không khai báo dependency ngoài, CI gọi make test. |
| Giới hạn | Router không cung cấp toàn bộ auth, validation hoặc ORM của ứng dụng. Các benchmark trong README chưa được chạy; tương thích middleware vẫn cần kiểm thứ tự và context thực tế. |
| Điều kiện tích hợp | Dùng khi muốn giữ HTTP stack chuẩn, chốt timeout/limit/error middleware; thử route conflict, hủy request và quyền truy cập trước khi mở endpoint. |
| Lựa chọn đối chiếu | [Echo](../34-backend-data-identity-integration/README.md#anhkysuai-labstack-echo); [Gin](../08-awesome-lists-learning/README.md#6c59-framework-backend); net/http ServeMux. |

**Phạm vi bằng chứng:** đã clone, đọc trích đoạn tài liệu, giấy phép và các file cấu hình được dẫn dưới đây; chưa chạy mã, build, benchmark hoặc test upstream. `docs-read` không phải kiểm chứng implementation.

**Nguồn tại cùng SHA:** [README.md](https://github.com/go-chi/chi/blob/c64ed7d6635f33a8b2feaff7dcfa55677023ac7d/README.md) · [LICENSE](https://github.com/go-chi/chi/blob/c64ed7d6635f33a8b2feaff7dcfa55677023ac7d/LICENSE) · [go.mod](https://github.com/go-chi/chi/blob/c64ed7d6635f33a8b2feaff7dcfa55677023ac7d/go.mod) · [.github/workflows/ci.yml](https://github.com/go-chi/chi/blob/c64ed7d6635f33a8b2feaff7dcfa55677023ac7d/.github/workflows/ci.yml).

<a id="anhkysuai-grpc-grpc-go"></a>

### gRPC-Go

**Repo:** [grpc/grpc-go](https://github.com/grpc/grpc-go) · **License:** Apache-2.0 · **Kiểm:** 2026-11-23, `docs-read`, [`341c59808a9a`](https://github.com/grpc/grpc-go/tree/341c59808a9aaaf920baa4f1c1cd6c9087cae229) (commit 2026-11-22). **Sao:** 23,126 tại 2026-11-23 theo [GitHub API](https://api.github.com/repos/grpc/grpc-go).

| Mục | Đánh giá |
|---|---|
| Mục đích | Triển khai gRPC bằng Go cho RPC trên HTTP/2. |
| Giá trị và cơ chế theo tài liệu | README dẫn API, tài liệu mức thấp và examples; Go manifest và CI có vet-proto, static checks, test/race giúp xác định công cụ hợp đồng RPC. |
| Giới hạn | Hiệu năng và tương thích client/server chưa benchmark. RPC không tự bảo đảm retry an toàn, auth hay backward compatibility của schema; runtime hỗ trợ giới hạn theo dòng Go. |
| Điều kiện tích hợp | Ghim protoc/plugin/runtime, thiết kế deadline/status và auth interceptor; thử stream cancellation, thay đổi schema và idempotency trước khi kết nối nhiều dịch vụ. |
| Lựa chọn đối chiếu | Connect RPC; Apache Thrift; Dubbo. |

**Phạm vi bằng chứng:** đã clone, đọc trích đoạn tài liệu, giấy phép và các file cấu hình được dẫn dưới đây; chưa chạy mã, build, benchmark hoặc test upstream. `docs-read` không phải kiểm chứng implementation.

**Nguồn tại cùng SHA:** [README.md](https://github.com/grpc/grpc-go/blob/341c59808a9aaaf920baa4f1c1cd6c9087cae229/README.md) · [LICENSE](https://github.com/grpc/grpc-go/blob/341c59808a9aaaf920baa4f1c1cd6c9087cae229/LICENSE) · [go.mod](https://github.com/grpc/grpc-go/blob/341c59808a9aaaf920baa4f1c1cd6c9087cae229/go.mod) · [.github/workflows/testing.yml](https://github.com/grpc/grpc-go/blob/341c59808a9aaaf920baa4f1c1cd6c9087cae229/.github/workflows/testing.yml).

<a id="anhkysuai-micro-go-micro"></a>

### Go Micro

**Repo:** [micro/go-micro](https://github.com/micro/go-micro) · **License:** Apache-2.0 · **Kiểm:** 2026-11-23, `docs-read`, [`b65720e0b9b1`](https://github.com/micro/go-micro/tree/b65720e0b9b14425883da9f9df56d94a9b9cd8ed) (commit 2026-11-23). **Sao:** 23,077 tại 2026-11-23 theo [GitHub API](https://api.github.com/repos/micro/go-micro).

| Mục | Đánh giá |
|---|---|
| Mục đích | Framework Go cho dịch vụ phân tán và agent dùng dịch vụ làm tool. |
| Giá trị và cơ chế theo tài liệu | README mô tả RPC/discovery/message/config cùng gateway HTTP/MCP, mỗi component thay được qua interface; CI có unit race và etcd integration. |
| Giới hạn | Khả năng agent/recovery mới được đọc từ docs; cung cấp RPC qua MCP cần ranh giới quyền riêng. Không suy mặc định an toàn hoặc giao hàng bền từ interface thay thế. |
| Điều kiện tích hợp | Bắt đầu một service không model, ghim component và provider; thử auth, timeout/discovery rồi mới cấp agent quyền tool với phạm vi cần thiết. |
| Lựa chọn đối chiếu | Go kit; [Kratos](../08-awesome-lists-learning/README.md#6c59-framework-backend); [Dapr](../08-awesome-lists-learning/README.md#6c55-container--devops). |

**Phạm vi bằng chứng:** đã clone, đọc trích đoạn tài liệu, giấy phép và các file cấu hình được dẫn dưới đây; chưa chạy mã, build, benchmark hoặc test upstream. `docs-read` không phải kiểm chứng implementation.

**Nguồn tại cùng SHA:** [README.md](https://github.com/micro/go-micro/blob/b65720e0b9b14425883da9f9df56d94a9b9cd8ed/README.md) · [LICENSE](https://github.com/micro/go-micro/blob/b65720e0b9b14425883da9f9df56d94a9b9cd8ed/LICENSE) · [go.mod](https://github.com/micro/go-micro/blob/b65720e0b9b14425883da9f9df56d94a9b9cd8ed/go.mod) · [.github/workflows/tests.yaml](https://github.com/micro/go-micro/blob/b65720e0b9b14425883da9f9df56d94a9b9cd8ed/.github/workflows/tests.yaml).

<a id="anhkysuai-jhipster-generator-jhipster"></a>

### JHipster Generator

**Repo:** [jhipster/generator-jhipster](https://github.com/jhipster/generator-jhipster) · **License:** Apache-2.0 · **Kiểm:** 2026-11-23, `docs-read`, [`38680db1ed43`](https://github.com/jhipster/generator-jhipster/tree/38680db1ed43fa1616d09b42d367436c5a686cb7) (commit 2026-11-23). **Sao:** 22,462 tại 2026-11-23 theo [GitHub API](https://api.github.com/repos/jhipster/generator-jhipster).

| Mục | Đánh giá |
|---|---|
| Mục đích | Generator tạo ứng dụng Spring Boot với Angular/React/Vue và kiến trúc microservice. |
| Giá trị và cơ chế theo tài liệu | README nêu tổ hợp Java/Node được CI kiểm; manifest 9.4.1-snapshot và tài liệu JDL/blueprint giúp chuẩn hóa khởi tạo dự án. |
| Giới hạn | README cảnh báo .yo-rc.json có thể khai báo blueprint được thực thi. Generated code vẫn cần kiểm nghiệp vụ và dependency; nhánh snapshot chưa thay bản phát hành. |
| Điều kiện tích hợp | Dùng config tự quản lý, đọc blueprint trước khi chạy; tạo app thử, kiểm quyền/migration và giữ phần tùy chỉnh có thể nâng cấp theo generator. |
| Lựa chọn đối chiếu | [Full Stack FastAPI Template](../34-backend-data-identity-integration/README.md#anhkysuai-fastapi-full-stack-fastapi-template); Spring Initializr; Nx. |

**Phạm vi bằng chứng:** đã clone, đọc trích đoạn tài liệu, giấy phép và các file cấu hình được dẫn dưới đây; chưa chạy mã, build, benchmark hoặc test upstream. `docs-read` không phải kiểm chứng implementation.

**Nguồn tại cùng SHA:** [README.md](https://github.com/jhipster/generator-jhipster/blob/38680db1ed43fa1616d09b42d367436c5a686cb7/README.md) · [LICENSE.txt](https://github.com/jhipster/generator-jhipster/blob/38680db1ed43fa1616d09b42d367436c5a686cb7/LICENSE.txt) · [package.json](https://github.com/jhipster/generator-jhipster/blob/38680db1ed43fa1616d09b42d367436c5a686cb7/package.json) · [.github/workflows/issue-check.yml](https://github.com/jhipster/generator-jhipster/blob/38680db1ed43fa1616d09b42d367436c5a686cb7/.github/workflows/issue-check.yml).

<a id="anhkysuai-livekit-livekit"></a>

### LiveKit Server

**Repo:** [livekit/livekit](https://github.com/livekit/livekit) · **License:** Apache-2.0 · **Kiểm:** 2026-11-23, `docs-read`, [`575f96ee4d0e`](https://github.com/livekit/livekit/tree/575f96ee4d0e14ea5bc31c2e2c192b83848670dc) (commit 2026-11-23). **Sao:** 22,348 tại 2026-11-23 theo [GitHub API](https://api.github.com/repos/livekit/livekit).

| Mục | Đánh giá |
|---|---|
| Mục đích | Máy chủ WebRTC SFU truyền audio, video và dữ liệu giữa người, thiết bị và model. |
| Giá trị và cơ chế theo tài liệu | README tách rõ server Go/Pion khỏi SDK, agent framework và dịch vụ đi kèm; CI dựng Redis và build bằng Mage. |
| Giới hạn | Không gộp độ chính xác STT/LLM/TTS của LiveKit Agents vào server này. Chưa thử call, bandwidth, TURN hay phân quyền room; độ trễ còn phụ thuộc mạng/codec. |
| Điều kiện tích hợp | Thử room/token với thiết bị thật, cấu hình TLS/TURN và network policy; đo reconnect, packet loss, recording consent và chi phí egress trước triển khai. |
| Lựa chọn đối chiếu | mediasoup; Jitsi; Janus. |

**Phạm vi bằng chứng:** đã clone, đọc trích đoạn tài liệu, giấy phép và các file cấu hình được dẫn dưới đây; chưa chạy mã, build, benchmark hoặc test upstream. `docs-read` không phải kiểm chứng implementation.

**Nguồn tại cùng SHA:** [README.md](https://github.com/livekit/livekit/blob/575f96ee4d0e14ea5bc31c2e2c192b83848670dc/README.md) · [LICENSE](https://github.com/livekit/livekit/blob/575f96ee4d0e14ea5bc31c2e2c192b83848670dc/LICENSE) · [go.mod](https://github.com/livekit/livekit/blob/575f96ee4d0e14ea5bc31c2e2c192b83848670dc/go.mod) · [.github/workflows/buildtest.yaml](https://github.com/livekit/livekit/blob/575f96ee4d0e14ea5bc31c2e2c192b83848670dc/.github/workflows/buildtest.yaml).

<a id="anhkysuai-tornadoweb-tornado"></a>

### Tornado

**Repo:** [tornadoweb/tornado](https://github.com/tornadoweb/tornado) · **License:** Apache-2.0 · **Kiểm:** 2026-11-23, `docs-read`, [`a6d0b2e7fcfc`](https://github.com/tornadoweb/tornado/tree/a6d0b2e7fcfc70d29b06d3e7ae8ae799981774f3) (commit 2026-11-20). **Sao:** 22,175 tại 2026-11-23 theo [GitHub API](https://api.github.com/repos/tornadoweb/tornado).

| Mục | Đánh giá |
|---|---|
| Mục đích | Framework web và thư viện mạng async Python cho kết nối dài. |
| Giá trị và cơ chế theo tài liệu | README minh họa RequestHandler chạy trên asyncio và đề cập WebSocket/long polling; pyproject/cibuildwheel cùng CI tox giúp đọc phạm vi runtime. |
| Giới hạn | Ví dụ hello world không dùng đặc tính async và không chứng minh sức tải hàng chục nghìn kết nối. Code blocking trong luồng xử lý vẫn cần xem xét; chưa chạy tải. |
| Điều kiện tích hợp | Chọn release Python phù hợp, kiểm cancellation/timeout và WebSocket auth; tách tác vụ blocking, thêm giới hạn kết nối và quan sát event loop trong ứng dụng. |
| Lựa chọn đối chiếu | Aiohttp; FastAPI; Starlette. |

**Phạm vi bằng chứng:** đã clone, đọc trích đoạn tài liệu, giấy phép và các file cấu hình được dẫn dưới đây; chưa chạy mã, build, benchmark hoặc test upstream. `docs-read` không phải kiểm chứng implementation.

**Nguồn tại cùng SHA:** [README.rst](https://github.com/tornadoweb/tornado/blob/a6d0b2e7fcfc70d29b06d3e7ae8ae799981774f3/README.rst) · [LICENSE](https://github.com/tornadoweb/tornado/blob/a6d0b2e7fcfc70d29b06d3e7ae8ae799981774f3/LICENSE) · [pyproject.toml](https://github.com/tornadoweb/tornado/blob/a6d0b2e7fcfc70d29b06d3e7ae8ae799981774f3/pyproject.toml) · [.github/workflows/test.yml](https://github.com/tornadoweb/tornado/blob/a6d0b2e7fcfc70d29b06d3e7ae8ae799981774f3/.github/workflows/test.yml).

<a id="anhkysuai-elunez-eladmin"></a>

### ELADMIN JPA

**Repo:** [elunez/eladmin](https://github.com/elunez/eladmin) · **License:** Apache-2.0 · **Kiểm:** 2026-11-23, `docs-read`, [`646c58c30f2e`](https://github.com/elunez/eladmin/tree/646c58c30f2e9aecf998b054f05f4d9ba0008995) (commit 2026-11-02). **Sao:** 21,895 tại 2026-11-23 theo [GitHub API](https://api.github.com/repos/elunez/eladmin).

| Mục | Đánh giá |
|---|---|
| Mục đích | Backend quản trị Spring Boot/JPA với RBAC, quyền dữ liệu và generator. |
| Giá trị và cơ chế theo tài liệu | README tách frontend eladmin-web và biến thể MyBatis, nêu cấu hình JWT production riêng; Maven chia module common/logging và nghiệp vụ. |
| Giới hạn | README còn ví dụ tài khoản/mật khẩu mẫu và stack Spring Boot 2.7.18; không coi ví dụ là cấu hình triển khai an toàn. Chưa kiểm code phân quyền, codegen hay module vận hành từ xa. |
| Điều kiện tích hợp | Chọn đúng biến thể, thay mọi cấu hình mẫu và tạo JWT secret riêng; kiểm quyền theo vai trò/dữ liệu, rate limit, migration và dependency trước production. |
| Lựa chọn đối chiếu | [RuoYi Vue Pro](../34-backend-data-identity-integration/README.md#anhkysuai-yunaiv-ruoyi-vue-pro); JHipster; ABP Framework. |

**Phạm vi bằng chứng:** đã clone, đọc trích đoạn tài liệu, giấy phép và các file cấu hình được dẫn dưới đây; chưa chạy mã, build, benchmark hoặc test upstream. `docs-read` không phải kiểm chứng implementation.

**Nguồn tại cùng SHA:** [README.md](https://github.com/elunez/eladmin/blob/646c58c30f2e9aecf998b054f05f4d9ba0008995/README.md) · [LICENSE](https://github.com/elunez/eladmin/blob/646c58c30f2e9aecf998b054f05f4d9ba0008995/LICENSE) · [pom.xml](https://github.com/elunez/eladmin/blob/646c58c30f2e9aecf998b054f05f4d9ba0008995/pom.xml).

<a id="anhkysuai-dgraph-io-dgraph"></a>

### Dgraph

**Repo:** [dgraph-io/dgraph](https://github.com/dgraph-io/dgraph) · **License:** Apache-2.0 · **Kiểm:** 2026-11-23, `docs-read`, [`e95fc26526ad`](https://github.com/dgraph-io/dgraph/tree/e95fc26526adf3929315beba174d35f6a101003c) (commit 2026-11-20). **Sao:** 21,838 tại 2026-11-23 theo [GitHub API](https://api.github.com/repos/dgraph-io/dgraph).

| Mục | Đánh giá |
|---|---|
| Mục đích | Database graph phân tán hỗ trợ GraphQL và API HTTP/gRPC. |
| Giá trị và cơ chế theo tài liệu | README mô tả graph backend, giao dịch và nền Go; CI fuzz DQL cung cấp cổng kiểm parser, platform chính thức là Linux amd64/arm64. |
| Giới hạn | Các tuyên bố linearizable/ACID/scale lớn chưa được fault-test. Hỗ trợ macOS/Windows đã bị bỏ theo README; không suy môi trường local ngang Linux production. |
| Điều kiện tích hợp | Thử model graph, query và ACL với dữ liệu đại diện; kiểm giao dịch cạnh tranh, replication, backup/restore và giới hạn bộ nhớ trước khi migrate. |
| Lựa chọn đối chiếu | Neo4j; ArangoDB; Memgraph. |

**Phạm vi bằng chứng:** đã clone, đọc trích đoạn tài liệu, giấy phép và các file cấu hình được dẫn dưới đây; chưa chạy mã, build, benchmark hoặc test upstream. `docs-read` không phải kiểm chứng implementation.

**Nguồn tại cùng SHA:** [README.md](https://github.com/dgraph-io/dgraph/blob/e95fc26526adf3929315beba174d35f6a101003c/README.md) · [LICENSE.txt](https://github.com/dgraph-io/dgraph/blob/e95fc26526adf3929315beba174d35f6a101003c/LICENSE.txt) · [go.mod](https://github.com/dgraph-io/dgraph/blob/e95fc26526adf3929315beba174d35f6a101003c/go.mod) · [.github/workflows/ci-dgraph-fuzz.yml](https://github.com/dgraph-io/dgraph/blob/e95fc26526adf3929315beba174d35f6a101003c/.github/workflows/ci-dgraph-fuzz.yml).

<a id="anhkysuai-vitessio-vitess"></a>

### Vitess

**Repo:** [vitessio/vitess](https://github.com/vitessio/vitess) · **License:** Apache-2.0 · **Kiểm:** 2026-11-23, `docs-read`, [`9de84fd39cc8`](https://github.com/vitessio/vitess/tree/9de84fd39cc80ce8c56d8b34a4a505a86204c128) (commit 2026-11-21). **Sao:** 21,428 tại 2026-11-23 theo [GitHub API](https://api.github.com/repos/vitessio/vitess).

| Mục | Đánh giá |
|---|---|
| Mục đích | Lớp clustering/sharding để mở rộng hệ MySQL theo chiều ngang. |
| Giá trị và cơ chế theo tài liệu | README mô tả ứng dụng truy vấn qua hệ phân phối và split/merge shard; Go manifest gắn công cụ protobuf/gRPC, phục vụ đọc kiến trúc vận hành dữ liệu. |
| Giới hạn | Tuyên bố scale không giới hạn và cutover vài giây chưa được tái lập. Sharding vẫn đặt yêu cầu lên key/query/giao dịch; workflow chọn được chỉ rerun CI, không chứng minh correctness. |
| Điều kiện tích hợp | Phân tích query và sharding key trước, thử reshard/cutover trên bản sao dữ liệu; kiểm backup, failover, observability và quy trình rollback theo release. |
| Lựa chọn đối chiếu | [TiDB](../34-backend-data-identity-integration/README.md#anhkysuai-pingcap-tidb); MySQL InnoDB Cluster; PostgreSQL + Citus. |

**Phạm vi bằng chứng:** đã clone, đọc trích đoạn tài liệu, giấy phép và các file cấu hình được dẫn dưới đây; chưa chạy mã, build, benchmark hoặc test upstream. `docs-read` không phải kiểm chứng implementation.

**Nguồn tại cùng SHA:** [README.md](https://github.com/vitessio/vitess/blob/9de84fd39cc80ce8c56d8b34a4a505a86204c128/README.md) · [LICENSE](https://github.com/vitessio/vitess/blob/9de84fd39cc80ce8c56d8b34a4a505a86204c128/LICENSE) · [go.mod](https://github.com/vitessio/vitess/blob/9de84fd39cc80ce8c56d8b34a4a505a86204c128/go.mod) · [.github/workflows/ci-rerun.yml](https://github.com/vitessio/vitess/blob/9de84fd39cc80ce8c56d8b34a4a505a86204c128/.github/workflows/ci-rerun.yml).

<a id="anhkysuai-parse-community-parse-server"></a>

### Parse Server

**Repo:** [parse-community/parse-server](https://github.com/parse-community/parse-server) · **License:** Apache-2.0 · **Kiểm:** 2026-11-23, `docs-read`, [`a3f152f64dfa`](https://github.com/parse-community/parse-server/tree/a3f152f64dfaefedf9d9bb3e4c4579413193daab) (commit 2026-11-22). **Sao:** 21,399 tại 2026-11-23 theo [GitHub API](https://api.github.com/repos/parse-community/parse-server).

| Mục | Đánh giá |
|---|---|
| Mục đích | Backend tương thích Parse API chạy trên Node.js/Express, nhúng hoặc độc lập. |
| Giá trị và cơ chế theo tài liệu | README tách server, dashboard và Cloud Code guide; package 9.12.0-alpha.5 có dải Node cụ thể, CI kiểm CodeQL và engine compatibility. |
| Giới hạn | Nhánh đọc là alpha, không coi như release ổn định. Tương thích MongoDB/PostgreSQL và bảo vệ từng class/object chưa được kiểm; master key phải nằm ngoài client. |
| Điều kiện tích hợp | Chọn release/runtime/database được hỗ trợ, thử ACL/class permissions và Cloud Code bằng dữ liệu giả; kiểm migration, upload adapter và backup trước khi phục vụ app. |
| Lựa chọn đối chiếu | [Appwrite](../34-backend-data-identity-integration/README.md#anhkysuai-appwrite-appwrite); Supabase; PocketBase. |

**Phạm vi bằng chứng:** đã clone, đọc trích đoạn tài liệu, giấy phép và các file cấu hình được dẫn dưới đây; chưa chạy mã, build, benchmark hoặc test upstream. `docs-read` không phải kiểm chứng implementation.

**Nguồn tại cùng SHA:** [README.md](https://github.com/parse-community/parse-server/blob/a3f152f64dfaefedf9d9bb3e4c4579413193daab/README.md) · [LICENSE](https://github.com/parse-community/parse-server/blob/a3f152f64dfaefedf9d9bb3e4c4579413193daab/LICENSE) · [package.json](https://github.com/parse-community/parse-server/blob/a3f152f64dfaefedf9d9bb3e4c4579413193daab/package.json) · [.github/workflows/ci.yml](https://github.com/parse-community/parse-server/blob/a3f152f64dfaefedf9d9bb3e4c4579413193daab/.github/workflows/ci.yml).

<a id="anhkysuai-valeriansaliou-sonic"></a>

### Sonic

**Repo:** [valeriansaliou/sonic](https://github.com/valeriansaliou/sonic) · **License:** MPL-2.0 · **Kiểm:** 2026-11-23, `docs-read`, [`f16560b6ea67`](https://github.com/valeriansaliou/sonic/tree/f16560b6ea67fd223354c065f7157646931db1b2) (commit 2026-10-30). **Sao:** 21,389 tại 2026-11-23 theo [GitHub API](https://api.github.com/repos/valeriansaliou/sonic).

| Mục | Đánh giá |
|---|---|
| Mục đích | Search backend trả ID của tài liệu, hướng đến chỉ mục nhỏ và truy vấn nhanh. |
| Giá trị và cơ chế theo tài liệu | README phân biệt identifier index với document index và báo đang làm lại v2; Cargo tách core/server/client, workflow lint/test/supply-chain. |
| Giới hạn | README nói master chỉ nhận bug fix khi tập trung v2; không suy tính năng roadmap như BM25 đã ổn định tại mọi nhánh. Số RAM/độ trễ chưa được đo. |
| Điều kiện tích hợp | Ghim nhánh/release, thử bộ truy vấn và ngôn ngữ thực tế; giữ tài liệu gốc ở database khác, kiểm cập nhật/xóa index và migration trước tích hợp. |
| Lựa chọn đối chiếu | [Meilisearch](../08-awesome-lists-learning/README.md#6c511-giám-sát-csdl--phân-tích); [Typesense](../08-awesome-lists-learning/README.md#6c511-giám-sát-csdl--phân-tích); Tantivy. |

**Phạm vi bằng chứng:** đã clone, đọc trích đoạn tài liệu, giấy phép và các file cấu hình được dẫn dưới đây; chưa chạy mã, build, benchmark hoặc test upstream. `docs-read` không phải kiểm chứng implementation.

**Nguồn tại cùng SHA:** [README.md](https://github.com/valeriansaliou/sonic/blob/f16560b6ea67fd223354c065f7157646931db1b2/README.md) · [LICENSE.md](https://github.com/valeriansaliou/sonic/blob/f16560b6ea67fd223354c065f7157646931db1b2/LICENSE.md) · [Cargo.toml](https://github.com/valeriansaliou/sonic/blob/f16560b6ea67fd223354c065f7157646931db1b2/Cargo.toml) · [.github/workflows/test.yml](https://github.com/valeriansaliou/sonic/blob/f16560b6ea67fd223354c065f7157646931db1b2/.github/workflows/test.yml).

<a id="anhkysuai-gravitational-teleport"></a>

### Teleport Source

**Repo:** [gravitational/teleport](https://github.com/gravitational/teleport) · **License:** AGPL-3.0-only cho source; api Apache-2.0; binary CE khác · **Kiểm:** 2026-11-23, `docs-read`, [`1283425b60ec`](https://github.com/gravitational/teleport/tree/1283425b60ec5f60d509ba4c791183d452923ff7) (commit 2026-08-25). **Sao:** 21,127 tại 2026-11-23 theo [GitHub API](https://api.github.com/repos/gravitational/teleport).

| Mục | Đánh giá |
|---|---|
| Mục đích | Lớp kết nối, xác thực, quyền và audit cho máy chủ, Kubernetes, database và ứng dụng. |
| Giá trị và cơ chế theo tài liệu | README mô tả certificate ngắn hạn, proxy/CA và phiên truy cập; tách rõ API Apache, source AGPL và binary CE theo modified Apache. |
| Giới hạn | Giấy phép source không đại diện binary tải sẵn/Enterprise. Tuyên bố security audit và production chưa kiểm trong lượt này; sai role hoặc CA có thể ảnh hưởng toàn hạ tầng. |
| Điều kiện tích hợp | Chọn hình thức phân phối và edition, thử IdP, role, session recording và recovery; giới hạn tài nguyên kết nối, quản lý CA/rotation trước triển khai rộng. |
| Lựa chọn đối chiếu | Boundary; OpenSSH CA; Pomerium. |

**Phạm vi bằng chứng:** đã clone, đọc trích đoạn tài liệu, giấy phép và các file cấu hình được dẫn dưới đây; chưa chạy mã, build, benchmark hoặc test upstream. `docs-read` không phải kiểm chứng implementation.

**Nguồn tại cùng SHA:** [README.md](https://github.com/gravitational/teleport/blob/1283425b60ec5f60d509ba4c791183d452923ff7/README.md) · [LICENSE](https://github.com/gravitational/teleport/blob/1283425b60ec5f60d509ba4c791183d452923ff7/LICENSE) · [package.json](https://github.com/gravitational/teleport/blob/1283425b60ec5f60d509ba4c791183d452923ff7/package.json) · [Cargo.toml](https://github.com/gravitational/teleport/blob/1283425b60ec5f60d509ba4c791183d452923ff7/Cargo.toml) · [.github/workflows/check.yaml](https://github.com/gravitational/teleport/blob/1283425b60ec5f60d509ba4c791183d452923ff7/.github/workflows/check.yaml).

<a id="anhkysuai-nats-io-nats-server"></a>

### NATS Server

**Repo:** [nats-io/nats-server](https://github.com/nats-io/nats-server) · **License:** Apache-2.0 · **Kiểm:** 2026-11-23, `docs-read`, [`a0385c9af342`](https://github.com/nats-io/nats-server/tree/a0385c9af342ffae6df28999b77a85de5423d3d6) (commit 2026-11-20). **Sao:** 21,113 tại 2026-11-23 theo [GitHub API](https://api.github.com/repos/nats-io/nats-server).

| Mục | Đánh giá |
|---|---|
| Mục đích | Máy chủ truyền thông cho dịch vụ, hệ thống và thiết bị từ cloud tới edge. |
| Giá trị và cơ chế theo tài liệu | README liên kết client nhiều ngôn ngữ và tài liệu riêng; Go manifest có JWT/nkeys, CI build/lint/test giúp xác định nền messaging. |
| Giới hạn | Không suy mọi chế độ có cùng đảm bảo lưu bền hoặc giao hàng. Chưa đọc implementation JetStream, kiểm cluster, slow consumer hay phân quyền subject. |
| Điều kiện tích hợp | Xác định nhu cầu pub/sub và persistence, chọn client cùng release; thử mất kết nối, backpressure, auth/account và phục hồi trước khi dùng cho sự kiện quan trọng. |
| Lựa chọn đối chiếu | RabbitMQ; Kafka; Redis Streams. |

**Phạm vi bằng chứng:** đã clone, đọc trích đoạn tài liệu, giấy phép và các file cấu hình được dẫn dưới đây; chưa chạy mã, build, benchmark hoặc test upstream. `docs-read` không phải kiểm chứng implementation.

**Nguồn tại cùng SHA:** [README.md](https://github.com/nats-io/nats-server/blob/a0385c9af342ffae6df28999b77a85de5423d3d6/README.md) · [LICENSE](https://github.com/nats-io/nats-server/blob/a0385c9af342ffae6df28999b77a85de5423d3d6/LICENSE) · [go.mod](https://github.com/nats-io/nats-server/blob/a0385c9af342ffae6df28999b77a85de5423d3d6/go.mod) · [.github/workflows/tests.yaml](https://github.com/nats-io/nats-server/blob/a0385c9af342ffae6df28999b77a85de5423d3d6/.github/workflows/tests.yaml).

<a id="anhkysuai-apache-shardingsphere"></a>

### Apache ShardingSphere

**Repo:** [apache/shardingsphere](https://github.com/apache/shardingsphere) · **License:** Apache-2.0; thông báo thành phần riêng · **Kiểm:** 2026-11-23, `docs-read`, [`0d551770daf8`](https://github.com/apache/shardingsphere/tree/0d551770daf83981d39d4ecdc0a2b9319a201553) (commit 2026-11-23). **Sao:** 20,836 tại 2026-11-23 theo [GitHub API](https://api.github.com/repos/apache/shardingsphere).

| Mục | Đánh giá |
|---|---|
| Mục đích | Lớp Database Plus đặt trên database hiện có để thống nhất truy cập và khả năng phân tán. |
| Giá trị và cơ chế theo tài liệu | README nhấn mạnh kết nối, mở rộng và cơ chế pluggable thay vì tạo engine mới; Maven CI chạy build/test là điểm đọc hệ Java. |
| Giới hạn | Lớp phân tán không làm mọi SQL/giao dịch của backend tự tương thích. Chưa kiểm routing, sharding, dữ liệu mã hóa hay failover dưới tải. |
| Điều kiện tích hợp | Chọn adapter/proxy theo ứng dụng, kiểm tập SQL và khóa phân mảnh; thử migration, giao dịch chéo shard, observability và rollback trên dữ liệu bản sao. |
| Lựa chọn đối chiếu | [Vitess](../34-backend-data-identity-integration/README.md#anhkysuai-vitessio-vitess); [TiDB](../34-backend-data-identity-integration/README.md#anhkysuai-pingcap-tidb); Apache Calcite. |

**Phạm vi bằng chứng:** đã clone, đọc trích đoạn tài liệu, giấy phép và các file cấu hình được dẫn dưới đây; chưa chạy mã, build, benchmark hoặc test upstream. `docs-read` không phải kiểm chứng implementation.

**Nguồn tại cùng SHA:** [README.md](https://github.com/apache/shardingsphere/blob/0d551770daf83981d39d4ecdc0a2b9319a201553/README.md) · [LICENSE](https://github.com/apache/shardingsphere/blob/0d551770daf83981d39d4ecdc0a2b9319a201553/LICENSE) · [pom.xml](https://github.com/apache/shardingsphere/blob/0d551770daf83981d39d4ecdc0a2b9319a201553/pom.xml) · [.github/workflows/ci.yml](https://github.com/apache/shardingsphere/blob/0d551770daf83981d39d4ecdc0a2b9319a201553/.github/workflows/ci.yml).

<a id="anhkysuai-wagtail-wagtail"></a>

### Wagtail

**Repo:** [wagtail/wagtail](https://github.com/wagtail/wagtail) · **License:** BSD-3-Clause · **Kiểm:** 2026-11-23, `docs-read`, [`9599540ea564`](https://github.com/wagtail/wagtail/tree/9599540ea5648de7d5ecf09eb4b9794fb084b4b6) (commit 2026-11-20). **Sao:** 20,826 tại 2026-11-23 theo [GitHub API](https://api.github.com/repos/wagtail/wagtail).

| Mục | Đánh giá |
|---|---|
| Mục đích | CMS Django cho nội dung có cấu trúc và trải nghiệm biên tập tùy chỉnh. |
| Giá trị và cơ chế theo tài liệu | README mô tả StreamField, Content API, đa site/ngôn ngữ và search; Python manifest/CI kiểm nhiều môi trường, frontend có toolchain riêng. |
| Giới hạn | Các tuyên bố hàng triệu trang/nghìn editor chưa benchmark. Component CMS không thay model quyền, cấu hình media hoặc workflow xuất bản của dự án. |
| Điều kiện tích hợp | Dùng starter và phiên bản Django/Python tương thích, thử content model, preview và permissions; kiểm migration StreamField, search index, ảnh và backup trước nhập nội dung. |
| Lựa chọn đối chiếu | Drupal; Payload; [Strapi](../08-awesome-lists-learning/README.md#6c59-framework-backend). |

**Phạm vi bằng chứng:** đã clone, đọc trích đoạn tài liệu, giấy phép và các file cấu hình được dẫn dưới đây; chưa chạy mã, build, benchmark hoặc test upstream. `docs-read` không phải kiểm chứng implementation.

**Nguồn tại cùng SHA:** [README.md](https://github.com/wagtail/wagtail/blob/9599540ea5648de7d5ecf09eb4b9794fb084b4b6/README.md) · [LICENSE](https://github.com/wagtail/wagtail/blob/9599540ea5648de7d5ecf09eb4b9794fb084b4b6/LICENSE) · [package.json](https://github.com/wagtail/wagtail/blob/9599540ea5648de7d5ecf09eb4b9794fb084b4b6/package.json) · [pyproject.toml](https://github.com/wagtail/wagtail/blob/9599540ea5648de7d5ecf09eb4b9794fb084b4b6/pyproject.toml) · [.github/workflows/test.yml](https://github.com/wagtail/wagtail/blob/9599540ea5648de7d5ecf09eb4b9794fb084b4b6/.github/workflows/test.yml).

<a id="anhkysuai-gofr-dev-gofr"></a>

### GoFr

**Repo:** [gofr-dev/gofr](https://github.com/gofr-dev/gofr) · **License:** Apache-2.0 · **Kiểm:** 2026-11-23, `docs-read`, [`5a8c9ee237d0`](https://github.com/gofr-dev/gofr/tree/5a8c9ee237d060ac8aac4596f1bfe75f0b5a4bc1) (commit 2026-11-23). **Sao:** 20,785 tại 2026-11-23 theo [GitHub API](https://api.github.com/repos/gofr-dev/gofr).

| Mục | Đánh giá |
|---|---|
| Mục đích | Framework Go hướng microservice/Kubernetes, gắn database và observability sẵn. |
| Giá trị và cơ chế theo tài liệu | README gom logs/traces/metrics, health check, migration, pub/sub và MCP cho handler chỉ đọc; CI ví dụ dựng thêm các dịch vụ kiểm. |
| Giới hạn | Danh sách tính năng không chứng minh mọi datasource/handler có policy an toàn. Chưa kiểm cơ chế MCP chỉ đọc, auth, LLM tracing hay circuit breaker. |
| Điều kiện tích hợp | Bắt đầu service nhỏ, ghim connector và kiểm telemetry không lộ bí mật; thử timeout, quyền, migration và failure của dependency trước khi bật AI/tool gateway. |
| Lựa chọn đối chiếu | [Go Micro](../34-backend-data-identity-integration/README.md#anhkysuai-micro-go-micro); [Kratos](../08-awesome-lists-learning/README.md#6c59-framework-backend); Go kit. |

**Phạm vi bằng chứng:** đã clone, đọc trích đoạn tài liệu, giấy phép và các file cấu hình được dẫn dưới đây; chưa chạy mã, build, benchmark hoặc test upstream. `docs-read` không phải kiểm chứng implementation.

**Nguồn tại cùng SHA:** [README.md](https://github.com/gofr-dev/gofr/blob/5a8c9ee237d060ac8aac4596f1bfe75f0b5a4bc1/README.md) · [LICENSE](https://github.com/gofr-dev/gofr/blob/5a8c9ee237d060ac8aac4596f1bfe75f0b5a4bc1/LICENSE) · [go.mod](https://github.com/gofr-dev/gofr/blob/5a8c9ee237d060ac8aac4596f1bfe75f0b5a4bc1/go.mod) · [.github/workflows/go.yml](https://github.com/gofr-dev/gofr/blob/5a8c9ee237d060ac8aac4596f1bfe75f0b5a4bc1/.github/workflows/go.yml).

<a id="anhkysuai-jasontaylordev-cleanarchitecture"></a>

### Clean Architecture ASP.NET Template

**Repo:** [jasontaylordev/CleanArchitecture](https://github.com/jasontaylordev/CleanArchitecture) · **License:** MIT · **Kiểm:** 2026-11-23, `docs-read`, [`21182736a929`](https://github.com/jasontaylordev/CleanArchitecture/tree/21182736a929e1ad37a363e47d39de6e650ca984) (commit 2026-11-23). **Sao:** 20,735 tại 2026-11-23 theo [GitHub API](https://api.github.com/repos/jasontaylordev/CleanArchitecture).

| Mục | Đánh giá |
|---|---|
| Mục đích | Template ASP.NET Core/Aspire cho Angular, React hoặc Web API riêng. |
| Giá trị và cơ chế theo tài liệu | README nêu .NET 10/11, SQLite mặc định và container chỉ cần cho SQL Server/PostgreSQL; CI restore/build và chuẩn bị Playwright. |
| Giới hạn | Cấu trúc Clean Architecture không tự bảo đảm domain design hay phân quyền đúng. Chưa tạo/chạy solution hoặc kiểm mọi tổ hợp frontend/database của template. |
| Điều kiện tích hợp | Chọn framework/client/database theo đội, sinh app thử rồi bỏ phần dư; giữ kiểm nghiệp vụ, migration và cấu hình secret riêng, đối chiếu nâng cấp package trước production. |
| Lựa chọn đối chiếu | Ardalis CleanArchitecture; ABP Framework; ASP.NET Core Web API template. |

**Phạm vi bằng chứng:** đã clone, đọc trích đoạn tài liệu, giấy phép và các file cấu hình được dẫn dưới đây; chưa chạy mã, build, benchmark hoặc test upstream. `docs-read` không phải kiểm chứng implementation.

**Nguồn tại cùng SHA:** [README.md](https://github.com/jasontaylordev/CleanArchitecture/blob/21182736a929e1ad37a363e47d39de6e650ca984/README.md) · [LICENSE](https://github.com/jasontaylordev/CleanArchitecture/blob/21182736a929e1ad37a363e47d39de6e650ca984/LICENSE) · [.github/workflows/build.yml](https://github.com/jasontaylordev/CleanArchitecture/blob/21182736a929e1ad37a363e47d39de6e650ca984/.github/workflows/build.yml).

<a id="anhkysuai-linlinjava-litemall"></a>

### litemall

**Repo:** [linlinjava/litemall](https://github.com/linlinjava/litemall) · **License:** MIT · **Kiểm:** 2026-11-23, `docs-read`, [`a1ef964a718b`](https://github.com/linlinjava/litemall/tree/a1ef964a718b7277925b19ea26afe78ea3a1d325) (commit 2025-10-05). **Sao:** 20,412 tại 2026-11-23 theo [GitHub API](https://api.github.com/repos/linlinjava/litemall).

| Mục | Đánh giá |
|---|---|
| Mục đích | Mẫu cửa hàng nhỏ với backend Spring Boot, admin Vue, WeChat mini-program và web mobile. |
| Giá trị và cơ chế theo tài liệu | README liệt kê catalog, cart, order, coupon và quản trị; Maven/CI build cùng test frontend cho thấy cách ghép ứng dụng bán hàng mẫu. |
| Giới hạn | Commit HEAD là 2025-10-05, khác ngày cập nhật aggregator; cần rà dependency trước dùng. Hướng dẫn dev tắt kiểm domain/TLS của WeChat không phù hợp production; chưa kiểm thanh toán/tồn kho. |
| Điều kiện tích hợp | Dùng để học hoặc làm nguyên mẫu, cập nhật runtime và bỏ dữ liệu/cấu hình mẫu; thử payment sandbox, quyền admin và order concurrency trước bán thật. |
| Lựa chọn đối chiếu | [Bagisto](../34-backend-data-identity-integration/README.md#anhkysuai-bagisto-bagisto); [Medusa](../08-awesome-lists-learning/README.md#6c59-framework-backend); Saleor. |

**Phạm vi bằng chứng:** đã clone, đọc trích đoạn tài liệu, giấy phép và các file cấu hình được dẫn dưới đây; chưa chạy mã, build, benchmark hoặc test upstream. `docs-read` không phải kiểm chứng implementation.

**Nguồn tại cùng SHA:** [README.md](https://github.com/linlinjava/litemall/blob/a1ef964a718b7277925b19ea26afe78ea3a1d325/README.md) · [LICENSE](https://github.com/linlinjava/litemall/blob/a1ef964a718b7277925b19ea26afe78ea3a1d325/LICENSE) · [pom.xml](https://github.com/linlinjava/litemall/blob/a1ef964a718b7277925b19ea26afe78ea3a1d325/pom.xml) · [.github/workflows/main.yml](https://github.com/linlinjava/litemall/blob/a1ef964a718b7277925b19ea26afe78ea3a1d325/.github/workflows/main.yml).

<a id="anhkysuai-graphql-graphql-js"></a>

### GraphQL.js

**Repo:** [graphql/graphql-js](https://github.com/graphql/graphql-js) · **License:** MIT · **Kiểm:** 2026-11-23, `docs-read`, [`52f67c02ffb6`](https://github.com/graphql/graphql-js/tree/52f67c02ffb6aeb72a0e67f4be150665aa229f43) (commit 2026-11-10). **Sao:** 20,346 tại 2026-11-23 theo [GitHub API](https://api.github.com/repos/graphql/graphql-js).

| Mục | Đánh giá |
|---|---|
| Mục đích | Triển khai tham chiếu GraphQL bằng JavaScript, xây schema và thực thi query. |
| Giá trị và cơ chế theo tài liệu | README minh họa GraphQLSchema/resolver và dẫn tests theo specification; manifest 17.1.0, CI kiểm API examples, types và lint. |
| Giới hạn | Đây là thư viện ngôn ngữ/runtime, chưa là HTTP server đầy đủ. Schema có kiểu không tự áp auth, query cost hay chống N+1; chưa chạy conformance/fuzz tests. |
| Điều kiện tích hợp | Ghim phiên bản với server adapter, giữ schema và resolver có kiểm; áp quyền truy cập, giới hạn query và batching theo workload trước mở API. |
| Lựa chọn đối chiếu | GraphQL Yoga; Apollo Server; Mercurius. |

**Phạm vi bằng chứng:** đã clone, đọc trích đoạn tài liệu, giấy phép và các file cấu hình được dẫn dưới đây; chưa chạy mã, build, benchmark hoặc test upstream. `docs-read` không phải kiểm chứng implementation.

**Nguồn tại cùng SHA:** [README.md](https://github.com/graphql/graphql-js/blob/52f67c02ffb6aeb72a0e67f4be150665aa229f43/README.md) · [LICENSE](https://github.com/graphql/graphql-js/blob/52f67c02ffb6aeb72a0e67f4be150665aa229f43/LICENSE) · [package.json](https://github.com/graphql/graphql-js/blob/52f67c02ffb6aeb72a0e67f4be150665aa229f43/package.json) · [.github/workflows/ci.yml](https://github.com/graphql/graphql-js/blob/52f67c02ffb6aeb72a0e67f4be150665aa229f43/.github/workflows/ci.yml).

<a id="anhkysuai-grpc-ecosystem-grpc-gateway"></a>

### gRPC-Gateway

**Repo:** [grpc-ecosystem/grpc-gateway](https://github.com/grpc-ecosystem/grpc-gateway) · **License:** BSD-3-Clause · **Kiểm:** 2026-11-23, `docs-read`, [`452c933896af`](https://github.com/grpc-ecosystem/grpc-gateway/tree/452c933896af82da883e932d4e7e82e4648db046) (commit 2026-11-21). **Sao:** 20,016 tại 2026-11-23 theo [GitHub API](https://api.github.com/repos/grpc-ecosystem/grpc-gateway).

| Mục | Đánh giá |
|---|---|
| Mục đích | Plugin protoc sinh reverse proxy dịch HTTP/JSON sang gRPC theo annotation. |
| Giá trị và cơ chế theo tài liệu | README gắn google.api.http trong protobuf với route REST; Go manifest và CI build examples/make test hỗ trợ duy trì hai giao diện từ hợp đồng chung. |
| Giới hạn | Sinh proxy không bảo đảm auth/header, HTTP status và streaming có cùng ngữ nghĩa mong muốn. Lời chứng thực throughput không thay benchmark; chưa sinh client/server hoặc chạy kiểm. |
| Điều kiện tích hợp | Ghim protoc/plugin/runtime, thử annotation và error mapping với API mẫu; kiểm metadata/auth, validation và backward compatibility trước công khai endpoint REST. |
| Lựa chọn đối chiếu | Connect RPC; Envoy gRPC JSON transcoder; Twirp. |

**Phạm vi bằng chứng:** đã clone, đọc trích đoạn tài liệu, giấy phép và các file cấu hình được dẫn dưới đây; chưa chạy mã, build, benchmark hoặc test upstream. `docs-read` không phải kiểm chứng implementation.

**Nguồn tại cùng SHA:** [README.md](https://github.com/grpc-ecosystem/grpc-gateway/blob/452c933896af82da883e932d4e7e82e4648db046/README.md) · [LICENSE](https://github.com/grpc-ecosystem/grpc-gateway/blob/452c933896af82da883e932d4e7e82e4648db046/LICENSE) · [go.mod](https://github.com/grpc-ecosystem/grpc-gateway/blob/452c933896af82da883e932d4e7e82e4648db046/go.mod) · [.github/workflows/ci.yml](https://github.com/grpc-ecosystem/grpc-gateway/blob/452c933896af82da883e932d4e7e82e4648db046/.github/workflows/ci.yml).

<a id="anhkysuai-psf-requests"></a>

### Requests

- **Repo:** [psf/requests](https://github.com/psf/requests).
- **Mục đích:** HTTP client đồng bộ cho Python với API session, cookie và truyền dữ liệu thuận tiện.
- **Điểm đáng dùng:** README liệt kê pooling, TLS verification, multipart, streaming và proxy; pyproject yêu cầu Python >=3.10, CI có test nhiều cấu hình phát hiện encoding.
- **License:** Apache-2.0.
- **Giới hạn:** Phải đặt timeout và chính sách retry theo tác vụ; HTTP client không tự làm trình duyệt JavaScript. Kiểm cấu hình proxy và .netrc trước khi chạy dưới danh tính người dùng.
- **Tích hợp:** Dùng Session và timeout rõ ràng, giới hạn kích thước tải, giữ xác minh TLS và xử lý mã HTTP.
- **Đối chiếu:** HTTPX cho sync/async và HTTP/2; aiohttp cho async; urllib khi muốn thư viện chuẩn.
- **Mức kiểm chứng:** `docs-read` — Đọc các phần mô tả và giới hạn trong README, thông báo license, metadata manifest và cấu hình CI khi có; chưa đọc toàn bộ mã triển khai, chưa cài hoặc chạy kiểm thử upstream.
- **Snapshot:** kiểm ngày 2026-11-23; commit `3c7baaa05ab4aa49cc819ce3a819d260de19c157` (2026-10-26T11:14:41-06:00); 54,749 sao theo GitHub API ngày 2026-11-23. Sao không đại diện chất lượng.
- **Bằng chứng:** [README.md](https://github.com/psf/requests/blob/3c7baaa05ab4aa49cc819ce3a819d260de19c157/README.md) · [LICENSE](https://github.com/psf/requests/blob/3c7baaa05ab4aa49cc819ce3a819d260de19c157/LICENSE) · [pyproject.toml](https://github.com/psf/requests/blob/3c7baaa05ab4aa49cc819ce3a819d260de19c157/pyproject.toml) · [.github/workflows/run-tests.yml](https://github.com/psf/requests/blob/3c7baaa05ab4aa49cc819ce3a819d260de19c157/.github/workflows/run-tests.yml) · [GitHub API](https://api.github.com/repos/psf/requests).

<a id="anhkysuai-dbeaver-dbeaver"></a>

### DBeaver Community

- **Repo:** [dbeaver/dbeaver](https://github.com/dbeaver/dbeaver).
- **Mục đích:** Công cụ desktop quản trị, truy vấn và chuyển dữ liệu cho nhiều hệ cơ sở dữ liệu.
- **Điểm đáng dùng:** README mô tả OSGi/Eclipse RCP, JDBC/ODBC và tách model plugin khỏi UI để dùng chung với CloudBeaver; có SQL editor, ER diagram và import/export.
- **License:** Apache-2.0; driver và bản thương mại có điều khoản riêng.
- **Giới hạn:** Driver CData và các bản thương mại có giấy phép riêng. Kết nối DB và tính năng AI có thể đưa dữ liệu ra ngoài; cần kiểm endpoint và quyền theo cấu hình thực tế.
- **Tích hợp:** Cài bản phát hành, sử dụng tài khoản DB tối thiểu quyền và kiểm driver/SSH tunnel trước cấp dữ liệu thật.
- **Đối chiếu:** DataGrip cho IDE thương mại; pgAdmin cho PostgreSQL; CloudBeaver cho giao diện web.
- **Mức kiểm chứng:** `docs-read` — Đọc các phần mô tả và giới hạn trong README, thông báo license, metadata manifest và cấu hình CI khi có; chưa đọc toàn bộ mã triển khai, chưa cài hoặc chạy kiểm thử upstream.
- **Snapshot:** kiểm ngày 2026-11-23; commit `14eb8c7cbcb675f63d01030dac6b82efc2550c91` (2026-11-23T10:31:51+01:00); 52,515 sao theo GitHub API ngày 2026-11-23. Sao không đại diện chất lượng.
- **Bằng chứng:** [README.md](https://github.com/dbeaver/dbeaver/blob/14eb8c7cbcb675f63d01030dac6b82efc2550c91/README.md) · [LICENSE.md](https://github.com/dbeaver/dbeaver/blob/14eb8c7cbcb675f63d01030dac6b82efc2550c91/LICENSE.md) · [pom.xml](https://github.com/dbeaver/dbeaver/blob/14eb8c7cbcb675f63d01030dac6b82efc2550c91/pom.xml) · [.github/workflows/codeql.yml](https://github.com/dbeaver/dbeaver/blob/14eb8c7cbcb675f63d01030dac6b82efc2550c91/.github/workflows/codeql.yml) · [GitHub API](https://api.github.com/repos/dbeaver/dbeaver).

<a id="anhkysuai-lysine-dev-okhttp"></a>

### OkHttp

- **Repo:** [lysine-dev/okhttp](https://github.com/lysine-dev/okhttp).
- **Mục đích:** HTTP client cho JVM/Android với API đồng bộ và bất đồng bộ.
- **Điểm đáng dùng:** README nêu pooling, HTTP/2, nén, cache và chiến lược thử địa chỉ thay thế; giới hạn GET có body và cache không thay được được mô tả rõ.
- **License:** Apache-2.0.
- **Giới hạn:** Không nên suy mọi server tùy biến được hỗ trợ; yêu cầu Android/Java và certificate pinning cần kiểm theo phiên bản. Chưa chạy tương thích mạng.
- **Tích hợp:** Dùng artifact theo hướng dẫn tại SHA, cấu hình timeout/TLS và tái dùng client; kiểm danh tính upstream khi nguồn dẫn owner khác bản quen thuộc.
- **Đối chiếu:** JDK HttpClient cho JVM hiện đại; Apache HttpComponents cho tùy chỉnh; Ktor Client cho Kotlin đa nền tảng.
- **Mức kiểm chứng:** `docs-read` — Đọc các phần mô tả và giới hạn trong README, thông báo license, metadata manifest và cấu hình CI khi có; chưa đọc toàn bộ mã triển khai, chưa cài hoặc chạy kiểm thử upstream.
- **Snapshot:** kiểm ngày 2026-11-23; commit `ee0a7ea1b14d2ea924055d291a22c2a3a7ac97cc` (2026-11-23T08:44:40Z); 47,116 sao theo GitHub API ngày 2026-11-23. Sao không đại diện chất lượng.
- **Bằng chứng:** [README.md](https://github.com/lysine-dev/okhttp/blob/ee0a7ea1b14d2ea924055d291a22c2a3a7ac97cc/README.md) · [LICENSE.txt](https://github.com/lysine-dev/okhttp/blob/ee0a7ea1b14d2ea924055d291a22c2a3a7ac97cc/LICENSE.txt) · [.github/workflows/build.yml](https://github.com/lysine-dev/okhttp/blob/ee0a7ea1b14d2ea924055d291a22c2a3a7ac97cc/.github/workflows/build.yml) · [GitHub API](https://api.github.com/repos/lysine-dev/okhttp).

<a id="anhkysuai-go-gorm-gorm"></a>

### GORM

- **Repo:** [go-gorm/gorm](https://github.com/go-gorm/gorm).
- **Mục đích:** ORM Go cho quan hệ dữ liệu, truy vấn và giao dịch.
- **Điểm đáng dùng:** Tài liệu liệt kê association, Preload/Joins, nested transaction, savepoint, DryRun và plugin resolver; CI chạy các kiểm thử theo dialect.
- **License:** MIT.
- **Giới hạn:** Auto migration và eager loading cần kiểm soát thay đổi schema, số truy vấn; chưa kiểm chứng claim mọi tính năng đều có test.
- **Tích hợp:** Khóa driver, viết migration có duyệt và test transaction trên đúng cơ sở dữ liệu sản xuất.
- **Đối chiếu:** Ent cho schema Go; [sqlc](../34-backend-data-identity-integration/README.md#sqlc) cho SQL sinh kiểu; Prisma cho hệ TypeScript.
- **Mức kiểm chứng:** `docs-read` — Đọc các phần mô tả và giới hạn trong README, thông báo license, metadata manifest và cấu hình CI khi có; chưa đọc toàn bộ mã triển khai, chưa cài hoặc chạy kiểm thử upstream.
- **Snapshot:** kiểm ngày 2026-11-23; commit `ead4e04ba7c6a49654649131e587133b1d9f3eca` (2026-10-24T01:06:51+08:00); 39,999 sao theo GitHub API ngày 2026-11-23. Sao không đại diện chất lượng.
- **Bằng chứng:** [README.md](https://github.com/go-gorm/gorm/blob/ead4e04ba7c6a49654649131e587133b1d9f3eca/README.md) · [LICENSE](https://github.com/go-gorm/gorm/blob/ead4e04ba7c6a49654649131e587133b1d9f3eca/LICENSE) · [go.mod](https://github.com/go-gorm/gorm/blob/ead4e04ba7c6a49654649131e587133b1d9f3eca/go.mod) · [.github/workflows/tests.yml](https://github.com/go-gorm/gorm/blob/ead4e04ba7c6a49654649131e587133b1d9f3eca/.github/workflows/tests.yml) · [GitHub API](https://api.github.com/repos/go-gorm/gorm).

<a id="anhkysuai-typeorm-typeorm"></a>

### TypeORM

- **Repo:** [typeorm/typeorm](https://github.com/typeorm/typeorm).
- **Mục đích:** ORM TypeScript/JavaScript hỗ trợ entity, quan hệ, migration và nhiều driver dữ liệu.
- **Điểm đáng dùng:** README cho phép chọn Data Mapper hoặc Active Record, có QueryBuilder và transaction; CI kiểm tra build, manifest, lint.
- **License:** MIT.
- **Giới hạn:** Danh sách driver không chứng minh mọi tính năng tương đương; lazy relation và cascade dễ tạo truy vấn ngoài dự kiến.
- **Tích hợp:** Chọn một pattern nhất quán, duyệt SQL migration và test trên đúng engine thay vì chỉ SQLite giả lập.
- **Đối chiếu:** Prisma cho schema sinh client; Drizzle cho SQL có kiểu; [Sequelize](../34-backend-data-identity-integration/README.md#anhkysuai-sequelize-sequelize) cho ORM JavaScript.
- **Mức kiểm chứng:** `docs-read` — Đọc các phần mô tả và giới hạn trong README, thông báo license, metadata manifest và cấu hình CI khi có; chưa đọc toàn bộ mã triển khai, chưa cài hoặc chạy kiểm thử upstream.
- **Snapshot:** kiểm ngày 2026-11-23; commit `d5b143dd7ed659e2a1cbac044a2c78d90c0f6f8f` (2026-11-16T23:36:37+01:00); 36,684 sao theo GitHub API ngày 2026-11-23. Sao không đại diện chất lượng.
- **Bằng chứng:** [README.md](https://github.com/typeorm/typeorm/blob/d5b143dd7ed659e2a1cbac044a2c78d90c0f6f8f/README.md) · [LICENSE](https://github.com/typeorm/typeorm/blob/d5b143dd7ed659e2a1cbac044a2c78d90c0f6f8f/LICENSE) · [package.json](https://github.com/typeorm/typeorm/blob/d5b143dd7ed659e2a1cbac044a2c78d90c0f6f8f/package.json) · [.github/workflows/tests.yml](https://github.com/typeorm/typeorm/blob/d5b143dd7ed659e2a1cbac044a2c78d90c0f6f8f/.github/workflows/tests.yml) · [GitHub API](https://api.github.com/repos/typeorm/typeorm).

<a id="anhkysuai-numpy-numpy"></a>

### NumPy

**Đã chuyển (2026-11-23):** hồ sơ này nay nằm ở [mục 15](../15-ai-for-data/README.md#anhkysuai-numpy-numpy); catalog con xem [catalog/](../catalog/README.md).

<a id="anhkysuai-sequelize-sequelize"></a>

### Sequelize

- **Repo:** [sequelize/sequelize](https://github.com/sequelize/sequelize).
- **Mục đích:** ORM Node.js dùng Promise với nhiều dialect cơ sở dữ liệu.
- **Điểm đáng dùng:** Relation, eager/lazy loading, transaction và read replication là API tài liệu mô tả; CI build gói theo Node.
- **License:** MIT.
- **Giới hạn:** README phân biệt v6 stable với v7 alpha và đang tìm maintainer; cần kiểm tra dialect/version cụ thể thay vì suy ngang từ danh sách hỗ trợ.
- **Tích hợp:** Khóa major/driver, duyệt migration và thêm test SQL/transaction trên database thật của template.
- **Đối chiếu:** [TypeORM](../34-backend-data-identity-integration/README.md#anhkysuai-typeorm-typeorm) cho entity TypeScript; Prisma cho sinh client; Knex cho query builder.
- **Mức kiểm chứng:** `docs-read` — Đọc các phần mô tả và giới hạn trong README, thông báo license, metadata manifest và cấu hình CI khi có; chưa đọc toàn bộ mã triển khai, chưa cài hoặc chạy kiểm thử upstream.
- **Snapshot:** kiểm ngày 2026-11-23; commit `6f4cca6a74639b5d057f3823359489b52902191e` (2026-11-20T20:29:08-05:00); 30,352 sao theo GitHub API ngày 2026-11-23. Sao không đại diện chất lượng.
- **Bằng chứng:** [README.md](https://github.com/sequelize/sequelize/blob/6f4cca6a74639b5d057f3823359489b52902191e/README.md) · [LICENSE](https://github.com/sequelize/sequelize/blob/6f4cca6a74639b5d057f3823359489b52902191e/LICENSE) · [package.json](https://github.com/sequelize/sequelize/blob/6f4cca6a74639b5d057f3823359489b52902191e/package.json) · [.github/workflows/ci.yml](https://github.com/sequelize/sequelize/blob/6f4cca6a74639b5d057f3823359489b52902191e/.github/workflows/ci.yml) · [GitHub API](https://api.github.com/repos/sequelize/sequelize).

<a id="anhkysuai-automattic-mongoose"></a>

### Mongoose

- **Repo:** [Automattic/mongoose](https://github.com/Automattic/mongoose).
- **Mục đích:** ODM MongoDB cho Node.js với mô hình dữ liệu ứng dụng.
- **Điểm đáng dùng:** README phân biệt driver/model cùng hệ plugin, bản 9 và hỗ trợ Deno alpha; package tại SHA yêu cầu Node >=20.19.
- **License:** MIT.
- **Giới hạn:** Schema ứng dụng không thay constraint/authorization database; Deno alpha và Mongoose Studio là phạm vi riêng cần kiểm tra.
- **Tích hợp:** Khóa major cùng driver MongoDB, kiểm thử validation/update/query và quản lý index qua migration có duyệt.
- **Đối chiếu:** MongoDB Node driver cho truy cập trực tiếp; Prisma cho mô hình đa backend; Typegoose cho lớp TypeScript.
- **Mức kiểm chứng:** `docs-read` — Đọc các phần mô tả và giới hạn trong README, thông báo license, metadata manifest và cấu hình CI khi có; chưa đọc toàn bộ mã triển khai, chưa cài hoặc chạy kiểm thử upstream.
- **Snapshot:** kiểm ngày 2026-11-23; commit `217dfc3b6b1f9cdc96491ce7ca79a7767e6859f3` (2026-11-22T17:37:41-05:00); 27,452 sao theo GitHub API ngày 2026-11-23. Sao không đại diện chất lượng.
- **Bằng chứng:** [README.md](https://github.com/Automattic/mongoose/blob/217dfc3b6b1f9cdc96491ce7ca79a7767e6859f3/README.md) · [LICENSE.md](https://github.com/Automattic/mongoose/blob/217dfc3b6b1f9cdc96491ce7ca79a7767e6859f3/LICENSE.md) · [package.json](https://github.com/Automattic/mongoose/blob/217dfc3b6b1f9cdc96491ce7ca79a7767e6859f3/package.json) · [.github/workflows/test.yml](https://github.com/Automattic/mongoose/blob/217dfc3b6b1f9cdc96491ce7ca79a7767e6859f3/.github/workflows/test.yml) · [GitHub API](https://api.github.com/repos/Automattic/mongoose).

<a id="anhkysuai-google-flatbuffers"></a>

### FlatBuffers

- **Repo:** [google/flatbuffers](https://github.com/google/flatbuffers).
- **Mục đích:** Serialization đa ngôn ngữ cho phép truy cập dữ liệu ngay trong buffer.
- **Điểm đáng dùng:** Schema .fbs và flatc sinh accessor/builder cho từng ngôn ngữ, giảm bước parse/unpack theo mô hình tài liệu.
- **License:** Apache-2.0.
- **Giới hạn:** Khả năng tiến/lùi phụ thuộc quy tắc tiến hóa schema; cần xác minh buffer không tin cậy và không coi version theo ngày là SemVer.
- **Tích hợp:** Khóa compiler/runtime, thêm fixture đọc chéo phiên bản/ngôn ngữ và kiểm thử verifier trước khi nhận dữ liệu ngoài.
- **Đối chiếu:** Protocol Buffers cho message phổ biến; Cap’n Proto cho truy cập buffer; MessagePack cho encoding không schema.
- **Mức kiểm chứng:** `docs-read` — Đọc các phần mô tả và giới hạn trong README, thông báo license, metadata manifest và cấu hình CI khi có; chưa đọc toàn bộ mã triển khai, chưa cài hoặc chạy kiểm thử upstream.
- **Snapshot:** kiểm ngày 2026-11-23; commit `5eb190f00005b8dd1aa4f7ab2db9f01a39e3c76d` (2026-11-06T15:15:33-08:00); 26,658 sao theo GitHub API ngày 2026-11-23. Sao không đại diện chất lượng.
- **Bằng chứng:** [README.md](https://github.com/google/flatbuffers/blob/5eb190f00005b8dd1aa4f7ab2db9f01a39e3c76d/README.md) · [LICENSE](https://github.com/google/flatbuffers/blob/5eb190f00005b8dd1aa4f7ab2db9f01a39e3c76d/LICENSE) · [package.json](https://github.com/google/flatbuffers/blob/5eb190f00005b8dd1aa4f7ab2db9f01a39e3c76d/package.json) · [CMakeLists.txt](https://github.com/google/flatbuffers/blob/5eb190f00005b8dd1aa4f7ab2db9f01a39e3c76d/CMakeLists.txt) · [.github/workflows/build.yml](https://github.com/google/flatbuffers/blob/5eb190f00005b8dd1aa4f7ab2db9f01a39e3c76d/.github/workflows/build.yml) · [GitHub API](https://api.github.com/repos/google/flatbuffers).

<a id="anhkysuai-sqlitebrowser-sqlitebrowser"></a>

### DB Browser for SQLite

- **Repo:** [sqlitebrowser/sqlitebrowser](https://github.com/sqlitebrowser/sqlitebrowser).
- **Mục đích:** GUI tạo, duyệt, sửa và truy vấn tệp SQLite.
- **Điểm đáng dùng:** Giao diện dạng bảng, import/export CSV/SQL, log SQL và biểu đồ đơn giản hỗ trợ kiểm tra dữ liệu của template.
- **License:** MPL-2.0 / GPL-3.0-or-later; sqlean MIT và plugin theo thông báo riêng.
- **Giới hạn:** Không phải spreadsheet đầy đủ; thao tác UI có thể sửa schema/bản ghi, dữ liệu đang được ứng dụng ghi cần xử lý locking/backup cẩn thận.
- **Tích hợp:** Mở bản sao hoặc read-only khi khảo sát, kiểm tra SQL trước commit thay đổi và không nhập extension không tin cậy.
- **Đối chiếu:** [DBeaver](../34-backend-data-identity-integration/README.md#anhkysuai-dbeaver-dbeaver) cho nhiều database; sqlite3 CLI cho truy vấn có thể lặp; Datasette cho xuất bản dữ liệu đọc.
- **Mức kiểm chứng:** `docs-read` — Đọc các phần mô tả và giới hạn trong README, thông báo license, metadata manifest và cấu hình CI khi có; chưa đọc toàn bộ mã triển khai, chưa cài hoặc chạy kiểm thử upstream.
- **Snapshot:** kiểm ngày 2026-11-23; commit `2206215d21123c09a4a6c24d9332ce5d051379a8` (2026-11-23T01:46:15+09:00); 24,826 sao theo GitHub API ngày 2026-11-23. Sao không đại diện chất lượng.
- **Bằng chứng:** [README.md](https://github.com/sqlitebrowser/sqlitebrowser/blob/2206215d21123c09a4a6c24d9332ce5d051379a8/README.md) · [LICENSE](https://github.com/sqlitebrowser/sqlitebrowser/blob/2206215d21123c09a4a6c24d9332ce5d051379a8/LICENSE) · [LICENSE-GPL-3.0](https://github.com/sqlitebrowser/sqlitebrowser/blob/2206215d21123c09a4a6c24d9332ce5d051379a8/LICENSE-GPL-3.0) · [LICENSE-MIT](https://github.com/sqlitebrowser/sqlitebrowser/blob/2206215d21123c09a4a6c24d9332ce5d051379a8/LICENSE-MIT) · [CMakeLists.txt](https://github.com/sqlitebrowser/sqlitebrowser/blob/2206215d21123c09a4a6c24d9332ce5d051379a8/CMakeLists.txt) · [.github/workflows/summarize-dependencies.yml](https://github.com/sqlitebrowser/sqlitebrowser/blob/2206215d21123c09a4a6c24d9332ce5d051379a8/.github/workflows/summarize-dependencies.yml) · [GitHub API](https://api.github.com/repos/sqlitebrowser/sqlitebrowser).

<a id="anhkysuai-websockets-ws"></a>

### ws

**Repo:** [websockets/ws](https://github.com/websockets/ws) · **License:** MIT · **Kiểm:** 2026-11-23, `docs-read`, [`0cc9185755fa`](https://github.com/websockets/ws/tree/0cc9185755faa9b92b9efd566a8ee9f65fffd923) (commit 2026-11-16). **Sao:** 22,838 tại 2026-11-23 theo [GitHub API](https://api.github.com/repos/websockets/ws).

| Mục | Đánh giá |
|---|---|
| Mục đích | WebSocket client và server cho Node.js, dùng cho kênh realtime hoặc dịch vụ kết nối nền. |
| Giá trị và cơ chế theo tài liệu | README có HTTP upgrade, xác thực, broadcast và stream; manifest 8.23.0 có test cùng integration script, CI gọi lint và test. Tách phần giao thức để sản phẩm tự xây logic phiên. |
| Giới hạn | Client trong repo dành cho Node, trình duyệt dùng WebSocket gốc. README cảnh báo permessage-deflate tốn bộ nhớ và có rủi ro phân mảnh khi tải đồng thời; ví dụ authenticate để ứng dụng tự triển khai. |
| Điều kiện tích hợp | Thiết kế xác thực lúc upgrade, giới hạn payload, heartbeat và backpressure; chỉ bật nén sau thử tải đại diện. Chưa xác minh kết quả Autobahn hay benchmark upstream. |
| Lựa chọn đối chiếu | Socket.IO; uWebSockets; Centrifugo. |

**Phạm vi bằng chứng:** đã clone, đọc trích đoạn tài liệu, giấy phép và các file cấu hình được dẫn dưới đây; chưa chạy mã, build, benchmark hoặc test upstream. `docs-read` không phải kiểm chứng implementation.

**Nguồn tại cùng SHA:** [README.md](https://github.com/websockets/ws/blob/0cc9185755faa9b92b9efd566a8ee9f65fffd923/README.md) · [LICENSE](https://github.com/websockets/ws/blob/0cc9185755faa9b92b9efd566a8ee9f65fffd923/LICENSE) · [package.json](https://github.com/websockets/ws/blob/0cc9185755faa9b92b9efd566a8ee9f65fffd923/package.json) · [.github/workflows/ci.yml](https://github.com/websockets/ws/blob/0cc9185755faa9b92b9efd566a8ee9f65fffd923/.github/workflows/ci.yml).

<a id="anhkysuai-redis-go-redis"></a>

### go-redis

**Repo:** [redis/go-redis](https://github.com/redis/go-redis) · **License:** BSD-2-Clause · **Kiểm:** 2026-11-23, `docs-read`, [`f170311248f9`](https://github.com/redis/go-redis/tree/f170311248f9c15d4dcd326ea6e39b752359c1fa) (commit 2026-11-23). **Sao:** 22,293 tại 2026-11-23 theo [GitHub API](https://api.github.com/repos/redis/go-redis).

| Mục | Đánh giá |
|---|---|
| Mục đích | Client Redis cho Go với connection pool, Pub/Sub, pipeline, transaction, Sentinel và Cluster. |
| Giá trị và cơ chế theo tài liệu | README còn có client-side cache và streaming credentials; go.mod yêu cầu Go 1.26.0, ghi rõ một số phiên bản đã bị retract; workflow có go test và kiểm nhiều nền tảng. |
| Giới hạn | Automatic pipelining và MultiDB được đánh dấu experimental. Danh sách hỗ trợ server trong README không bảo đảm mọi lệnh hoặc module trên phiên bản cũ; license client tách với server Redis. |
| Điều kiện tích hợp | Khóa module v9 không nằm trong danh sách retract; đặt timeout/context, giới hạn pool và thử failover, retry cùng lệnh không idempotent trước triển khai. |
| Lựa chọn đối chiếu | Rueidis; Redigo; Valkey Go. |

**Phạm vi bằng chứng:** đã clone, đọc trích đoạn tài liệu, giấy phép và các file cấu hình được dẫn dưới đây; chưa chạy mã, build, benchmark hoặc test upstream. `docs-read` không phải kiểm chứng implementation.

**Nguồn tại cùng SHA:** [README.md](https://github.com/redis/go-redis/blob/f170311248f9c15d4dcd326ea6e39b752359c1fa/README.md) · [LICENSE](https://github.com/redis/go-redis/blob/f170311248f9c15d4dcd326ea6e39b752359c1fa/LICENSE) · [go.mod](https://github.com/redis/go-redis/blob/f170311248f9c15d4dcd326ea6e39b752359c1fa/go.mod) · [.github/workflows/build.yml](https://github.com/redis/go-redis/blob/f170311248f9c15d4dcd326ea6e39b752359c1fa/.github/workflows/build.yml).

<a id="anhkysuai-hapijs-joi"></a>

### Joi

**Repo:** [hapijs/joi](https://github.com/hapijs/joi) · **License:** BSD-3-Clause · **Kiểm:** 2026-11-23, `docs-read`, [`7cfb3ce20017`](https://github.com/hapijs/joi/tree/7cfb3ce20017a4289f7efdcd8803625d4be889df) (commit 2026-11-04). **Sao:** 21,167 tại 2026-11-23 theo [GitHub API](https://api.github.com/repos/hapijs/joi).

| Mục | Đánh giá |
|---|---|
| Mục đích | Thư viện mô tả schema và kiểm tra dữ liệu JavaScript ở biên API hoặc cấu hình. |
| Giá trị và cơ chế theo tài liệu | API.md minh họa object, kiểu dữ liệu, ràng buộc liên trường, validate và validateAsync; schema bất biến khi thêm quy tắc. Manifest 18.3.2 yêu cầu Node 20+, có lab và coverage script. |
| Giới hạn | Các giá trị mặc định là optional trừ khi required; kết quả có thể được chuyển kiểu, nên chỉ kiểm error mà bỏ value dễ gây sai. Validation không thay xác thực quyền hoặc kiểm nghiệp vụ với dữ liệu ngoài. |
| Điều kiện tích hợp | Tạo schema một lần, chốt conversion/unknown keys/presence, dùng value đã xác thực và chuẩn hóa lỗi trả về; kiểm payload biên cùng dữ liệu độc hại trước đưa vào API. |
| Lựa chọn đối chiếu | Zod; Valibot; Ajv. |

**Phạm vi bằng chứng:** đã clone, đọc trích đoạn tài liệu, giấy phép và các file cấu hình được dẫn dưới đây; chưa chạy mã, build, benchmark hoặc test upstream. `docs-read` không phải kiểm chứng implementation.

**Nguồn tại cùng SHA:** [README.md](https://github.com/hapijs/joi/blob/7cfb3ce20017a4289f7efdcd8803625d4be889df/README.md) · [LICENSE.md](https://github.com/hapijs/joi/blob/7cfb3ce20017a4289f7efdcd8803625d4be889df/LICENSE.md) · [package.json](https://github.com/hapijs/joi/blob/7cfb3ce20017a4289f7efdcd8803625d4be889df/package.json) · [.github/workflows/ci-module.yml](https://github.com/hapijs/joi/blob/7cfb3ce20017a4289f7efdcd8803625d4be889df/.github/workflows/ci-module.yml) · [API.md](https://github.com/hapijs/joi/blob/7cfb3ce20017a4289f7efdcd8803625d4be889df/API.md).

<a id="anhkysuai-knex-knex"></a>

### Knex

**Repo:** [knex/knex](https://github.com/knex/knex) · **License:** MIT · **Kiểm:** 2026-11-23, `docs-read`, [`e25d54bcb707`](https://github.com/knex/knex/tree/e25d54bcb707714a17f5a5744eba5c4246bb4d1d) (commit 2026-06-26). **Sao:** 20,338 tại 2026-11-23 theo [GitHub API](https://api.github.com/repos/knex/knex).

| Mục | Đánh giá |
|---|---|
| Mục đích | Query và schema builder SQL cho Node.js với nhiều dialect, transaction, pool kết nối và stream. |
| Giá trị và cơ chế theo tài liệu | README liệt kê PostgreSQL, MySQL/MariaDB, SQLite, SQL Server, Oracle và CockroachDB; manifest 3.3.0 có kiểm kiểu, workflow build rồi unit test. Hữu ích khi muốn kiểm soát câu truy vấn mà giảm mã ghép SQL. |
| Giới hạn | API chung không bảo đảm semantics SQL đồng nhất giữa dialect. Chưa chạy database integration hoặc kiểm raw SQL; transaction và pool vẫn cần thiết kế theo tải và vòng đời request. |
| Điều kiện tích hợp | Chọn driver phù hợp, dùng binding cho giá trị, kiểm SQL sinh ra và migration trên bản sao dữ liệu; đặt timeout/pool, thử rollback và giới hạn transaction trước triển khai. |
| Lựa chọn đối chiếu | Kysely; Drizzle ORM; Prisma. |

**Phạm vi bằng chứng:** đã clone, đọc trích đoạn tài liệu, giấy phép và các file cấu hình được dẫn dưới đây; chưa chạy mã, build, benchmark hoặc test upstream. `docs-read` không phải kiểm chứng implementation.

**Nguồn tại cùng SHA:** [README.md](https://github.com/knex/knex/blob/e25d54bcb707714a17f5a5744eba5c4246bb4d1d/README.md) · [LICENSE](https://github.com/knex/knex/blob/e25d54bcb707714a17f5a5744eba5c4246bb4d1d/LICENSE) · [package.json](https://github.com/knex/knex/blob/e25d54bcb707714a17f5a5744eba5c4246bb4d1d/package.json) · [.github/workflows/unit-tests.yml](https://github.com/knex/knex/blob/e25d54bcb707714a17f5a5744eba5c4246bb4d1d/.github/workflows/unit-tests.yml).

<a id="anhkysuai-2026-11-23-monicahq-monica"></a>

### monica

**Đã chuyển (2026-11-23):** hồ sơ này nay nằm ở [mục 36](../36-self-hosting-homelab/README.md#anhkysuai-2026-11-23-monicahq-monica); catalog con xem [catalog/](../catalog/README.md).

<a id="anhkysuai-2026-11-23-firefly-iii-firefly-iii"></a>

### firefly-iii

**Đã chuyển (2026-11-23):** hồ sơ này nay nằm ở [mục 36](../36-self-hosting-homelab/README.md#anhkysuai-2026-11-23-firefly-iii-firefly-iii); catalog con xem [catalog/](../catalog/README.md).

<a id="anhkysuai-2026-11-23-aureuserp-aureuserp"></a>

### aureuserp

**Repo:** [aureuserp/aureuserp](https://github.com/aureuserp/aureuserp) · **License:** MIT · **★ 12,278 (GitHub API, 2026-11-23)**

**Mục đích:** ERP viết bằng Laravel và Filament, tổ chức chức năng nghiệp vụ qua hệ plugin.

**Giá trị:** Có thể tham khảo cách ghép quản trị bán hàng, tồn kho và hoạt động doanh nghiệp trong một nền tảng PHP.

**Giới hạn:** Tuyên bố production-ready trong README chưa được kiểm bằng vận hành thực tế; cần đối chiếu schema, phân quyền, kế toán địa phương và quyền plugin trước dùng dữ liệu thật.

**Cách tham khảo/tích hợp:** Đọc cấu hình triển khai, giới hạn license và hợp đồng dữ liệu; thử auth, migration, backup/restore với dữ liệu mẫu trước tích hợp.

**Lựa chọn để đối chiếu:** [Dolibarr/dolibarr](https://github.com/Dolibarr/dolibarr) · [frappe/erpnext](https://github.com/frappe/erpnext). Đây là ứng viên so sánh theo tác vụ; mức phù hợp cần kiểm theo hồ sơ và phiên bản riêng.

**Bằng chứng:** `docs-read`, ngày 2026-11-23, commit [`34bf04cb4c46b7963948cc89c57a26990ce5510f`](https://github.com/aureuserp/aureuserp/commit/34bf04cb4c46b7963948cc89c57a26990ce5510f), ngày commit 2026-11-19. Đã clone và đọc chọn lọc phần giới thiệu, cách dùng, giới hạn, license, metadata manifest và CI hiện diện. Chưa kiểm đầy đủ implementation hoặc chạy upstream; các số đo của tác giả chưa được tái lập.

**Nguồn:** [README.md](https://github.com/aureuserp/aureuserp/blob/34bf04cb4c46b7963948cc89c57a26990ce5510f/README.md) · [LICENSE](https://github.com/aureuserp/aureuserp/blob/34bf04cb4c46b7963948cc89c57a26990ce5510f/LICENSE) · [package.json](https://github.com/aureuserp/aureuserp/blob/34bf04cb4c46b7963948cc89c57a26990ce5510f/package.json) · [composer.json](https://github.com/aureuserp/aureuserp/blob/34bf04cb4c46b7963948cc89c57a26990ce5510f/composer.json) · [.github/workflows/pest_tests.yml](https://github.com/aureuserp/aureuserp/blob/34bf04cb4c46b7963948cc89c57a26990ce5510f/.github/workflows/pest_tests.yml) · [metadata GitHub](https://api.github.com/repos/aureuserp/aureuserp).

<a id="anhkysuai-2026-11-23-dolibarr-dolibarr"></a>

### dolibarr

**Repo:** [Dolibarr/dolibarr](https://github.com/Dolibarr/dolibarr) · **License:** GPL-3.0-or-later; phụ thuộc riêng · **★ 7,889 (GitHub API, 2026-11-23)**

**Mục đích:** Bộ ERP/CRM PHP quản lý liên hệ, đơn hàng, hóa đơn, kho và các hoạt động tổ chức.

**Giá trị:** Có nhiều mô-đun và lựa chọn tự triển khai hoặc dịch vụ hosted, phù hợp nghiên cứu quy trình doanh nghiệp tích hợp.

**Giới hạn:** Cần kiểm bản địa hóa kế toán/thuế, phân quyền và nâng cấp dữ liệu; GPL-3.0-or-later của toàn thể tách khỏi license phụ thuộc liệt kê trong COPYRIGHT.

**Cách tham khảo/tích hợp:** Đọc cấu hình triển khai, giới hạn license và hợp đồng dữ liệu; thử auth, migration, backup/restore với dữ liệu mẫu trước tích hợp.

**Lựa chọn để đối chiếu:** [aureuserp/aureuserp](https://github.com/aureuserp/aureuserp) · [frappe/erpnext](https://github.com/frappe/erpnext). Đây là ứng viên so sánh theo tác vụ; mức phù hợp cần kiểm theo hồ sơ và phiên bản riêng.

**Bằng chứng:** `docs-read`, ngày 2026-11-23, commit [`fec9a84ef8ca1667f14bd6663434a11f225e1d19`](https://github.com/Dolibarr/dolibarr/commit/fec9a84ef8ca1667f14bd6663434a11f225e1d19), ngày commit 2026-11-23. Đã clone và đọc chọn lọc phần giới thiệu, cách dùng, giới hạn, license, metadata manifest và CI hiện diện. Chưa kiểm đầy đủ implementation hoặc chạy upstream; các số đo của tác giả chưa được tái lập.

**Nguồn:** [README.md](https://github.com/Dolibarr/dolibarr/blob/fec9a84ef8ca1667f14bd6663434a11f225e1d19/README.md) · [COPYING](https://github.com/Dolibarr/dolibarr/blob/fec9a84ef8ca1667f14bd6663434a11f225e1d19/COPYING) · [COPYRIGHT](https://github.com/Dolibarr/dolibarr/blob/fec9a84ef8ca1667f14bd6663434a11f225e1d19/COPYRIGHT) · [pyproject.toml](https://github.com/Dolibarr/dolibarr/blob/fec9a84ef8ca1667f14bd6663434a11f225e1d19/pyproject.toml) · [.github/workflows/ci-on-pull.yml](https://github.com/Dolibarr/dolibarr/blob/fec9a84ef8ca1667f14bd6663434a11f225e1d19/.github/workflows/ci-on-pull.yml) · [metadata GitHub](https://api.github.com/repos/Dolibarr/dolibarr).

<a id="anhkysuai-2026-11-23-laravel-laravel"></a>

### Laravel application skeleton

**Repo:** [laravel/laravel](https://github.com/laravel/laravel) · **License:** MIT (composer.json và README) · **★ 85,489 (GitHub API, 2026-11-23)**

**Mục đích:** Bộ khung ứng dụng khởi tạo Laravel với cấu hình và phụ thuộc cho dự án PHP.

**Giá trị:** Phù hợp bắt đầu dự án và tham khảo cấu trúc ứng dụng quanh routing, ORM, queue và dependency injection.

**Giới hạn:** Đây là application skeleton, không phải toàn bộ mã framework laravel/framework; cần chọn phiên bản PHP/phụ thuộc, cấu hình secret và môi trường triển khai. MIT được khai báo trong composer.json/README.

**Cách tham khảo/tích hợp:** Đọc cấu hình triển khai, giới hạn license và hợp đồng dữ liệu; thử auth, migration, backup/restore với dữ liệu mẫu trước tích hợp.

**Lựa chọn để đối chiếu:** [laravel/framework](https://github.com/laravel/framework) · [symfony/symfony](https://github.com/symfony/symfony). Đây là ứng viên so sánh theo tác vụ; mức phù hợp cần kiểm theo hồ sơ và phiên bản riêng.

**Bằng chứng:** `docs-read`, ngày 2026-11-23, commit [`a255d7688770af9713daff1439c47ff9bc6abd47`](https://github.com/laravel/laravel/commit/a255d7688770af9713daff1439c47ff9bc6abd47), ngày commit 2026-11-13. Đã clone và đọc chọn lọc phần giới thiệu, cách dùng, giới hạn, license, metadata manifest và CI hiện diện. Chưa kiểm đầy đủ implementation hoặc chạy upstream; các số đo của tác giả chưa được tái lập.

**Nguồn:** [README.md](https://github.com/laravel/laravel/blob/a255d7688770af9713daff1439c47ff9bc6abd47/README.md) · [package.json](https://github.com/laravel/laravel/blob/a255d7688770af9713daff1439c47ff9bc6abd47/package.json) · [composer.json](https://github.com/laravel/laravel/blob/a255d7688770af9713daff1439c47ff9bc6abd47/composer.json) · [.github/workflows/tests.yml](https://github.com/laravel/laravel/blob/a255d7688770af9713daff1439c47ff9bc6abd47/.github/workflows/tests.yml) · [metadata GitHub](https://api.github.com/repos/laravel/laravel).

<a id="chuyen-muc-2026-11-23"></a>

## Hồ sơ chuyển về từ mục khác — 23/11/2026

32 hồ sơ được chuyển khi chia lại catalog theo `data/taxonomy.json`. Nội dung, ngày kiểm và mức bằng chứng giữ nguyên như ở mục gốc.

<a id="chuyen-axios"></a>

### axios

`axios/axios` · License: MIT · ★ 109.516 · docs-read · 2026-11-18

Thư viện HTTP client dựa trên Promise cho trình duyệt và Node.js. Hỗ trợ interceptor request/response, huỷ request và tự chuyển đổi JSON, multipart/form-data; Chạy cả trình duyệt (XMLHttpRequest) lẫn Node.js (module http), có mục hỗ trợ HTTP/2 trong README; Có file định nghĩa kiểu TypeScript (index.d.ts, index.d.cts), bản package.json hiện tại 1.21.1. ★ 18/11/2026: 109.516 (GitHub search API), nhóm "API & Dịch vụ dữ liệu" trong kho-repo của Phan Đông Giang, mục 08 §6c.5

**Hồ sơ gốc:** [mục 08](../08-awesome-lists-learning/README.md#6c52-api--dịch-vụ-dữ-liệu) (bảng/đoạn chung, giữ nguyên tại chỗ).

<a id="chuyen-hoppscotch"></a>

### hoppscotch

`hoppscotch/hoppscotch` · License: MIT · ★ 80.841 · docs-read · 2026-11-18

Hệ sinh thái phát triển API mã nguồn mở: ứng dụng web/desktop để gửi và kiểm thử request REST, GraphQL, WebSocket, SSE, Socket.IO, MQTT. Hỗ trợ nhiều giao thức (REST, GraphQL, WebSocket, Server-Sent Events, Socket.IO, MQTT) và nhiều kiểu xác thực (Basic, Bearer, OAuth 2.0, OIDC/PKCE); Có collection, workspace, team cộng tác và pre-request script JavaScript; Monorepo có backend, CLI, ứng dụng desktop, bản self-host web và trang admin (thư mục packages/). Điều kiện: Một số tính năng (ví dụ SSO) chỉ có ở bản Enterprise; tự host theo tài liệu self-host trên docs.hoppscotch.io. ★ 18/11/2026: 80.841 (GitHub search API), nhóm "API & Dịch vụ dữ liệu" trong kho-repo của Phan Đông Giang, mục 08 §6c.5

**Hồ sơ gốc:** [mục 08](../08-awesome-lists-learning/README.md#6c52-api--dịch-vụ-dữ-liệu) (bảng/đoạn chung, giữ nguyên tại chỗ).

<a id="chuyen-openai-python"></a>

### openai-python

`openai/openai-python` · License: Apache License 2.0 · ★ 32.184 · docs-read · 2026-11-18

Thư viện Python chính thức truy cập REST API của OpenAI, có client đồng bộ và bất đồng bộ. Có định nghĩa kiểu cho mọi tham số request và trường response, sinh từ đặc tả OpenAPI; Hỗ trợ streaming, Realtime API, phân trang tự động, xác minh webhook, retry và timeout cấu hình được; Hỗ trợ xác thực workload identity (Kubernetes, Azure, GCP, X.509) thay cho khoá API dài hạn. Điều kiện: Cần khoá API OpenAI (OPENAI_API_KEY) và tài khoản trả phí theo điều khoản OpenAI; Python 3.10+. ★ 18/11/2026: 32.184 (GitHub search API), nhóm "API & Dịch vụ dữ liệu" trong kho-repo của Phan Đông Giang, mục 08 §6c.5

**Hồ sơ gốc:** [mục 08](../08-awesome-lists-learning/README.md#6c52-api--dịch-vụ-dữ-liệu) (bảng/đoạn chung, giữ nguyên tại chỗ).

<a id="chuyen-jumpserver"></a>

### jumpserver

`jumpserver/jumpserver` · License: GPL-3.0 · ★ 31.982 · docs-read · 2026-11-18

Nền tảng quản lý truy cập đặc quyền (PAM/bastion host) mã nguồn mở, có tính năng AI, cho phép truy cập an toàn tới SSH, RDP, Kubernetes, cơ sở dữ liệu, website, RemoteApp. README nêu rõ lịch bảo trì phiên bản (5.x đang bảo trì, 4.10.x là LTS, 3.10.x chỉ sửa lỗi nghiêm trọng); cài nhanh bằng một script quick_start.sh; README có bản dịch nhiều ngôn ngữ kể cả tiếng Việt. Điều kiện: Máy chủ Linux 64-bit tối thiểu 4 nhân CPU, 8 GB RAM; giấy phép GPLv3 (copyleft); một số thành phần thuộc bản Enterprise; V3 CE hết hỗ trợ 31/12/2026; phải đổi mật khẩu mặc định admin/ChangeMe. ★ 18/11/2026: 31.982 (GitHub search API), nhóm "Bảo mật & Hack" trong kho-repo của Phan Đông Giang, mục 08 §6c.5

**Hồ sơ gốc:** [mục 08](../08-awesome-lists-learning/README.md#6c53-bảo-mật--hack) (bảng/đoạn chung, giữ nguyên tại chỗ).

<a id="chuyen-nacos"></a>

### nacos

`alibaba/nacos` · License: Apache License 2.0 · ★ 33.525 · docs-read · 2026-11-18

Nền tảng khám phá dịch vụ, quản lý cấu hình động và quản lý dịch vụ cho ứng dụng cloud-native và microservice. Đăng ký/khám phá dịch vụ qua DNS hoặc HTTP kèm health check thời gian thực; quản lý cấu hình tập trung, cập nhật không cần redeploy; hỗ trợ Dubbo/gRPC, Spring Cloud và Kubernetes. ★ 18/11/2026: 33.525 (GitHub search API), nhóm "Container & DevOps" trong kho-repo của Phan Đông Giang, mục 08 §6c.5

**Hồ sơ gốc:** [mục 08](../08-awesome-lists-learning/README.md#6c55-container--devops) (bảng/đoạn chung, giữ nguyên tại chỗ).

<a id="chuyen-gin"></a>

### gin

`gin-gonic/gin` · License: MIT · ★ 89.531 · docs-read · 2026-11-18

Framework web HTTP hiệu năng cao cho Go, API kiểu Martini dựa trên httprouter. Router không cấp phát heap; middleware recovery chống panic làm sập server, binding và kiểm tra JSON tự động; bản 1.12.0 đã phát hành, CI có quét bảo mật Trivy và codecov. Điều kiện: Cần Go 1.26+. ★ 18/11/2026: 89.531 (GitHub search API), nhóm "Framework Backend" trong kho-repo của Phan Đông Giang, mục 08 §6c.5

**Hồ sơ gốc:** [mục 08](../08-awesome-lists-learning/README.md#6c59-framework-backend) (bảng/đoạn chung, giữ nguyên tại chỗ).

<a id="chuyen-mall"></a>

### mall

`macrozheng/mall` · License: Apache-2.0 · ★ 85.057 · docs-read · 2026-11-18

Hệ thống thương mại điện tử đầy đủ (cửa hàng và trang quản trị) xây trên Spring Boot và MyBatis, triển khai bằng Docker. Nhánh master dùng Spring Boot 3.5 và JDK 17 (pom: spring-boot-starter-parent 3.5.14); chia module rõ: admin, portal, search (Elasticsearch), security, mbg; có tài liệu và hướng dẫn triển khai Windows, Docker, Docker Compose, Jenkins tại macrozheng.com. Điều kiện: Tài liệu chủ yếu tiếng Trung; cần MySQL, Redis (chỉ mall-admin) và thêm Elasticsearch, RabbitMQ, MongoDB cho đầy đủ; frontend ở repo riêng mall-admin-web, mall-app-web. ★ 18/11/2026: 85.057 (GitHub search API), nhóm "Framework Backend" trong kho-repo của Phan Đông Giang, mục 08 §6c.5

**Hồ sơ gốc:** [mục 08](../08-awesome-lists-learning/README.md#6c59-framework-backend) (bảng/đoạn chung, giữ nguyên tại chỗ).

<a id="chuyen-flask"></a>

### flask

`pallets/flask` · License: BSD-3-Clause · ★ 75.381 · docs-read · 2026-11-18

Framework ứng dụng web WSGI gọn nhẹ cho Python, xây quanh Werkzeug và Jinja. Không ép phụ thuộc hay cấu trúc dự án; hệ sinh thái extension cộng đồng lớn; do tổ chức Pallets duy trì, nhánh chính đang ở 3.2.0.dev. Điều kiện: Cần Python 3.11+ (theo pyproject.toml). ★ 18/11/2026: 75.381 (GitHub search API), nhóm "Framework Backend" trong kho-repo của Phan Đông Giang, mục 08 §6c.5

**Hồ sơ gốc:** [mục 08](../08-awesome-lists-learning/README.md#6c59-framework-backend) (bảng/đoạn chung, giữ nguyên tại chỗ).

<a id="chuyen-strapi"></a>

### strapi

`strapi/strapi` · License: MIT · ★ 73.510 · docs-read · 2026-11-18

Headless CMS mã nguồn mở tự host bằng JavaScript/TypeScript, sinh API REST và GraphQL từ mô hình nội dung. Content-Type Builder thiết kế mô hình trực quan không cần code; tự sinh API REST và GraphQL, có Roles và Permissions, Media Library, i18n, Draft và Publish; hỗ trợ SQLite, PostgreSQL, MySQL, MariaDB. Điều kiện: Tính năng trong ee/ cần giấy phép Enterprise; không có ảnh Docker chính thức; Strapi Cloud là dịch vụ trả phí. ★ 18/11/2026: 73.510 (GitHub search API), nhóm "Framework Backend" trong kho-repo của Phan Đông Giang, mục 08 §6c.5

**Hồ sơ gốc:** [mục 08](../08-awesome-lists-learning/README.md#6c59-framework-backend) (bảng/đoạn chung, giữ nguyên tại chỗ).

<a id="chuyen-protobuf"></a>

### protobuf

`protocolbuffers/protobuf` · License: BSD 3-Clause · ★ 72.179 · docs-read · 2026-11-18

Protocol Buffers: cơ chế tuần tự hoá dữ liệu có cấu trúc trung lập ngôn ngữ và nền tảng của Google, gồm trình biên dịch protoc và runtime cho nhiều ngôn ngữ. Runtime trong repo cho C++, Java, Python, Objective-C, C#, Ruby, PHP, Rust (Go, Dart, JavaScript ở repo riêng); hỗ trợ Bazel Bzlmod (Bazel 8+) và CMake; có bảng điểm OpenSSF Scorecard và file version.json theo dõi phiên bản từng ngôn ngữ. Điều kiện: README khuyên dùng bản phát hành, nhánh main có thể hỏng; C++ cần build từ mã nguồn. ★ 18/11/2026: 72.179 (GitHub search API), nhóm "Framework Backend" trong kho-repo của Phan Đông Giang, mục 08 §6c.5

**Hồ sơ gốc:** [mục 08](../08-awesome-lists-learning/README.md#6c59-framework-backend) (bảng/đoạn chung, giữ nguyên tại chỗ).

<a id="chuyen-express"></a>

### express

`expressjs/express` · License: MIT · ★ 69.801 · docs-read · 2026-11-18

Framework web tối giản, không áp đặt cấu trúc cho Node.js, cung cấp định tuyến và tiện ích HTTP. Phiên bản 5.3.0 trong package.json; định tuyến mạnh, hỗ trợ hơn 14 template engine và content negotiation; có thư mục examples và bộ test, huy hiệu OpenSSF Scorecard. Điều kiện: Cần Node.js 18 trở lên. ★ 18/11/2026: 69.801 (GitHub search API), nhóm "Framework Backend" trong kho-repo của Phan Đông Giang, mục 08 §6c.5

**Hồ sơ gốc:** [mục 08](../08-awesome-lists-learning/README.md#6c59-framework-backend) (bảng/đoạn chung, giữ nguyên tại chỗ).

<a id="chuyen-directus"></a>

### directus

`directus/directus` · License: Monospace Sustainable Core License 1.0 · ★ 38.747 · docs-read · 2026-11-18

Lớp backend bọc bất kỳ cơ sở dữ liệu SQL nào, tự sinh REST và GraphQL API, kèm Studio quản trị trực quan và MCP server cho tác tử AI. Hỗ trợ Postgres, MySQL, MariaDB, MS SQL, SQLite, OracleDB, CockroachDB; phân quyền theo chính sách tới mức trường; có SDK, Dockerfile và nhiều storage driver (S3, GCS, Azure, Cloudinary, Supabase). Điều kiện: Giấy phép không phải OSI: miễn phí cho tổ chức dưới 5 triệu USD doanh thu năm và 50 nhân viên qua Open Innovation Grant; vượt ngưỡng dùng tính năng nâng cao cần giấy phép thương mại; không được dùng để cạnh tranh với dịch vụ thương mại của Monospace. ★ 18/11/2026: 38.747 (GitHub search API), nhóm "Framework Backend" trong kho-repo của Phan Đông Giang, mục 08 §6c.5

**Hồ sơ gốc:** [mục 08](../08-awesome-lists-learning/README.md#6c59-framework-backend) (bảng/đoạn chung, giữ nguyên tại chỗ).

<a id="chuyen-medusa"></a>

### medusa

`medusajs/medusa` · License: MIT cho phần lớn repo · ★ 37.296 · docs-read · 2026-11-18

Nền tảng thương mại điện tử mã nguồn mở có framework tuỳ biến, dùng để xây cửa hàng B2B/DTC, marketplace, POS. Monorepo Yarn với các Commerce Module (product, cart, order, pricing, payment...); provider có sẵn cho Stripe, S3, SendGrid, Redis, OIDC; có Admin dashboard, design system Medusa UI và bộ integration test trên PostgreSQL. Điều kiện: Cần Node.js v22.22.0 trở lên và PostgreSQL; bật cờ tính năng Enterprise đồng nghĩa khẳng định có hợp đồng thương mại; không được dùng RBAC/SSO khi chưa có giấy phép. ★ 18/11/2026: 37.296 (GitHub search API), nhóm "Framework Backend" trong kho-repo của Phan Đông Giang, mục 08 §6c.5

**Hồ sơ gốc:** [mục 08](../08-awesome-lists-learning/README.md#6c59-framework-backend) (bảng/đoạn chung, giữ nguyên tại chỗ).

<a id="chuyen-go-zero"></a>

### go-zero

`zeromicro/go-zero` · License: MIT · ★ 33.431 · docs-read · 2026-11-18

Framework web và RPC cho Go với nhiều thực hành kỹ thuật tích hợp sẵn, kèm công cụ sinh mã goctl. Tích hợp sẵn kiểm soát timeout chuỗi, rate limit, circuit breaker và load shedding thích ứng; goctl sinh mã Go, iOS, Android, Kotlin, Dart, TypeScript, JavaScript từ file .api; có gói mcp và có trong CNCF Landscape. ★ 18/11/2026: 33.431 (GitHub search API), nhóm "Framework Backend" trong kho-repo của Phan Đông Giang, mục 08 §6c.5

**Hồ sơ gốc:** [mục 08](../08-awesome-lists-learning/README.md#6c59-framework-backend) (bảng/đoạn chung, giữ nguyên tại chỗ).

<a id="chuyen-python-telegram-bot"></a>

### python-telegram-bot

`python-telegram-bot/python-telegram-bot` · License: LGPL-3.0 · ★ 29.602 · docs-read · 2026-11-18

Thư viện Python thuần, bất đồng bộ cho Telegram Bot API, kèm các lớp cấp cao trong telegram.ext để viết bot. Hỗ trợ đầy đủ Telegram Bot API 10.0; tương thích Python 3.11+ và đã thử với free threading 3.14; có các gói phụ tuỳ chọn như job-queue, webhooks, rate-limiter. Điều kiện: Cần token bot Telegram; bản sửa đổi hoặc liên kết tĩnh phải phát hành dưới LGPL-3, ứng dụng chỉ dùng thư viện thì không bắt buộc. ★ 18/11/2026: 29.602 (GitHub search API), nhóm "Framework Backend" trong kho-repo của Phan Đông Giang, mục 08 §6c.5

**Hồ sơ gốc:** [mục 08](../08-awesome-lists-learning/README.md#6c59-framework-backend) (bảng/đoạn chung, giữ nguyên tại chỗ).

<a id="chuyen-kratos"></a>

### kratos

`go-kratos/kratos` · License: MIT · ★ 26.032 · docs-read · 2026-11-18

Framework Go nhẹ để xây vi dịch vụ cloud-native, cung cấp API cho transport, middleware, registry, cấu hình, log và sinh mã. Phát triển API-first với Protobuf, sinh mã HTTP/gRPC; log dựa trên log/slog chuẩn kèm mở rộng OpenTelemetry; hệ contrib cho registry, config store, middleware, quan sát. Điều kiện: Cần Go 1.25 trở lên, protoc và protoc-gen-go. ★ 18/11/2026: 26.032 (GitHub search API), nhóm "Framework Backend" trong kho-repo của Phan Đông Giang, mục 08 §6c.5

**Hồ sơ gốc:** [mục 08](../08-awesome-lists-learning/README.md#6c59-framework-backend) (bảng/đoạn chung, giữ nguyên tại chỗ).

<a id="chuyen-gin-vue-admin"></a>

### gin-vue-admin

`flipped-aurora/gin-vue-admin` · License: Apache-2.0 · ★ 25.139 · docs-read · 2026-11-18

Khung hệ thống quản trị full-stack tách frontend/backend dựa trên Gin (Go) và Vue 3, có JWT, menu động, Casbin, trình sinh form và sinh mã. Tích hợp xác thực JWT, phân quyền Casbin, định tuyến và menu động; có trình sinh mã và form generator; có tài liệu trực tuyến, video hướng dẫn và trang demo. Điều kiện: Cần Go >= 1.26.10 và Node; có bản trả phí (Licensed Edition) cho tính năng mở rộng và hỗ trợ thương mại; phải thay khoá Qiniu mẫu trong cấu hình. ★ 18/11/2026: 25.139 (GitHub search API), nhóm "Framework Backend" trong kho-repo của Phan Đông Giang, mục 08 §6c.5

**Hồ sơ gốc:** [mục 08](../08-awesome-lists-learning/README.md#6c59-framework-backend) (bảng/đoạn chung, giữ nguyên tại chỗ).

<a id="chuyen-wechaty"></a>

### wechaty

`wechaty/wechaty` · License: Apache License 2.0 · ★ 23.589 · docs-read · 2026-11-18

SDK RPA hội thoại để viết chatbot một lần chạy trên nhiều nền tảng nhắn tin (WeChat, WhatsApp, Telegram, Line…) thông qua các puppet provider. Chatbot tối thiểu chỉ 6 dòng JavaScript; chọn giao thức qua biến môi trường WECHATY_PUPPET; có ảnh Docker chạy trực tiếp bot.js hoặc bot.ts. Điều kiện: Một số giao thức (puppet) ngoài Web cần token, README hướng dẫn xin token qua wiki; tự động hoá tài khoản nhắn tin có thể vướng điều khoản dịch vụ của nền tảng (chưa xác minh trong README). ★ 18/11/2026: 23.589 (GitHub search API), nhóm "Framework Backend" trong kho-repo của Phan Đông Giang, mục 08 §6c.5

**Hồ sơ gốc:** [mục 08](../08-awesome-lists-learning/README.md#6c59-framework-backend) (bảng/đoạn chung, giữ nguyên tại chỗ).

<a id="chuyen-validator"></a>

### validator

`go-playground/validator` · License: MIT · ★ 20.239 · docs-read · 2026-11-18

Thư viện Go kiểm tra hợp lệ giá trị cho struct và từng trường dựa trên tag. Hỗ trợ kiểm tra chéo trường và chéo struct, đi sâu vào slice, array, map (cả khoá và giá trị); thông báo lỗi tuỳ biến có i18n với thư mục translations; là validator mặc định của framework gin. ★ 18/11/2026: 20.239 (GitHub search API), nhóm "Framework Backend" trong kho-repo của Phan Đông Giang, mục 08 §6c.5

**Hồ sơ gốc:** [mục 08](../08-awesome-lists-learning/README.md#6c59-framework-backend) (bảng/đoạn chung, giữ nguyên tại chỗ).

<a id="chuyen-apijson"></a>

### APIJSON

`APIJSON/APIJSON` · License: Apache License 2.0 · ★ 18.395 · docs-read · 2026-11-18

Giao thức truyền thông dựa trên JSON kèm thư viện ORM cho Java, cho phép client tự mô tả dữ liệu cần lấy để giảm việc viết API backend. Một request lấy được nhiều loại dữ liệu, hỗ trợ CRUD, tìm kiếm mờ, gọi hàm từ xa; README liệt kê demo cho nhiều CSDL như MySQL, PostgreSQL, SQL Server, Oracle, ClickHouse, DuckDB; phát hành qua JitPack, phiên bản 8.4.0 trong pom.xml. ★ 18/11/2026: 18.395 (GitHub search API), nhóm "Framework Backend" trong kho-repo của Phan Đông Giang, mục 08 §6c.5

**Hồ sơ gốc:** [mục 08](../08-awesome-lists-learning/README.md#6c59-framework-backend) (bảng/đoạn chung, giữ nguyên tại chỗ).

<a id="chuyen-hydra"></a>

### hydra

`ory/hydra` · License: Apache License 2.0 · ★ 17.671 · docs-read · 2026-11-18

Máy chủ OAuth 2.0 và nhà cung cấp OpenID Connect, kết nối với hệ thống định danh sẵn có qua ứng dụng login và consent riêng. Được chứng nhận OpenID Certified; không tự quản lý người dùng nên ghép được với Ory Kratos hoặc hệ thống riêng; hỗ trợ PostgreSQL, MySQL, CockroachDB và có nhiều file quickstart docker-compose. Điều kiện: README khuyến nghị hệ thống quan trọng dùng Ory Enterprise License để có bản vá CVE có SLA và bản build doanh nghiệp; telemetry ẩn danh bật mặc định, tắt được. ★ 18/11/2026: 17.671 (GitHub search API), nhóm "Framework Backend" trong kho-repo của Phan Đông Giang, mục 08 §6c.5

**Hồ sơ gốc:** [mục 08](../08-awesome-lists-learning/README.md#6c59-framework-backend) (bảng/đoạn chung, giữ nguyên tại chỗ).

<a id="chuyen-casdoor"></a>

### casdoor

`casdoor/casdoor` · License: Apache License 2.0 · ★ 14.881 · docs-read · 2026-11-18

Máy chủ đăng nhập một lần (SSO) và xác thực có bảng điều khiển web, là nhà cung cấp định danh đầy đủ lưu người dùng và cấp token. Hỗ trợ OAuth 2.0, OIDC, SAML 2.0, CAS, LDAP, SCIM 2.0, WebAuthn trên cùng một thư mục người dùng; phân quyền theo chính sách bằng Casbin (ACL, RBAC, ABAC); tự host bằng một binary Go cộng CSDL, có SDK cho Go, Java, Python, Node.js, .NET, PHP, Rust. Điều kiện: Ảnh all-in-one chỉ để thử, không dùng production (dữ liệu mất cùng container); tài khoản mặc định admin/123 cần đổi. ★ 18/11/2026: 14.881 (GitHub search API), nhóm "Framework Backend" trong kho-repo của Phan Đông Giang, mục 08 §6c.5

**Hồ sơ gốc:** [mục 08](../08-awesome-lists-learning/README.md#6c59-framework-backend) (bảng/đoạn chung, giữ nguyên tại chỗ).

<a id="chuyen-elasticsearch"></a>

### elasticsearch

`elastic/elasticsearch` · License: Mặc định ba giấy phép tuỳ chọn AGPL-3.0-only · ★ 78.816 · docs-read · 2026-11-18

Máy tìm kiếm và phân tích phân tán, kho dữ liệu và cơ sở dữ liệu vector, dùng cho full-text search, log, metric, APM, RAG. Hỗ trợ tìm kiếm vector và tìm kiếm gần thời gian thực trên dữ liệu lớn; có script start-local dựng Elasticsearch và Kibana bằng Docker kèm API key; mã nguồn Java build bằng Gradle với bộ test và benchmarks trong repo. Điều kiện: Script start-local chỉ cho phát triển/thử nghiệm (tắt HTTPS), cần Docker (Windows cần WSL); bản cục bộ kèm trial 1 tháng rồi về bậc Basic; tính năng x-pack chịu Elastic License 2.0. ★ 18/11/2026: 78.816 (GitHub search API), nhóm "Giám sát, CSDL & Phân tích" trong kho-repo của Phan Đông Giang, mục 08 §6c.5

**Hồ sơ gốc:** [mục 08](../08-awesome-lists-learning/README.md#6c511-giám-sát-csdl--phân-tích) (bảng/đoạn chung, giữ nguyên tại chỗ).

<a id="chuyen-redis"></a>

### redis

`redis/redis` · License: Từ Redis 8 · ★ 77.671 · docs-read · 2026-11-18

Kho dữ liệu trong bộ nhớ dùng làm cache, máy chủ cấu trúc dữ liệu, message broker, cơ sở dữ liệu tài liệu và truy vấn vector. Hỗ trợ JSON, time series, Bloom filter, Query Engine với tìm kiếm vector và full-text; có streams, pub/sub, giao dịch và scripting; có API module để mở rộng lệnh. Điều kiện: Giấy phép RSALv2/SSPLv1/AGPLv3 có hạn chế khi cung cấp dạng dịch vụ; dùng tên/logo Redis phải theo chính sách thương hiệu; build đầy đủ module cần CMake 3.25–3.31.6, LLVM 21, Rust. ★ 18/11/2026: 77.671 (GitHub search API), nhóm "Giám sát, CSDL & Phân tích" trong kho-repo của Phan Đông Giang, mục 08 §6c.5

**Hồ sơ gốc:** [mục 08](../08-awesome-lists-learning/README.md#6c511-giám-sát-csdl--phân-tích) (bảng/đoạn chung, giữ nguyên tại chỗ).

<a id="chuyen-meilisearch"></a>

### meilisearch

`meilisearch/meilisearch` · License: MIT AND OpenLDAP AND BUSL-1.1 · ★ 59.889 · docs-read · 2026-11-18

Công cụ tìm kiếm viết bằng Rust cho tìm kiếm toàn văn, ngữ nghĩa và lai, nhúng vào ứng dụng và website qua REST API. Chịu lỗi chính tả, lọc, faceting, sắp xếp và đồng nghĩa có sẵn; tìm kiếm khi gõ trả kết quả dưới 50 ms theo README; tự host bằng một lệnh Docker hoặc binary. Điều kiện: Bản Enterprise Edition (sharding và tính năng nâng cao) cần thỏa thuận thương mại khi dùng production (BUSL-1.1); bản Community MIT dùng tự do. ★ 18/11/2026: 59.889 (GitHub search API), nhóm "Giám sát, CSDL & Phân tích" trong kho-repo của Phan Đông Giang, mục 08 §6c.5

**Hồ sơ gốc:** [mục 08](../08-awesome-lists-learning/README.md#6c511-giám-sát-csdl--phân-tích) (bảng/đoạn chung, giữ nguyên tại chỗ).

<a id="chuyen-typesense"></a>

### typesense

`typesense/typesense` · License: GNU General Public License v3.0 · ★ 27.153 · docs-read · 2026-11-18

Công cụ tìm kiếm nhanh, chịu lỗi chính tả viết bằng C++, tự giới thiệu là phương án mở thay Algolia và dễ dùng hơn Elasticsearch. Viết bằng C++ cho tìm kiếm tức thời dưới 50 ms; có chịu lỗi chính tả, faceting, lọc, sắp xếp và tìm kiếm ngữ nghĩa/lai; nhiều demo trực tiếp trên tập dữ liệu lớn (32 triệu bài hát). Điều kiện: GPL-3.0 (copyleft) khi phân phối bản sửa đổi. ★ 18/11/2026: 27.153 (GitHub search API), nhóm "Giám sát, CSDL & Phân tích" trong kho-repo của Phan Đông Giang, mục 08 §6c.5

**Hồ sơ gốc:** [mục 08](../08-awesome-lists-learning/README.md#6c511-giám-sát-csdl--phân-tích) (bảng/đoạn chung, giữ nguyên tại chỗ).

<a id="chuyen-dolt"></a>

### dolt

`dolthub/dolt` · License: Apache License 2.0 · ★ 24.933 · docs-read · 2026-11-18

Cơ sở dữ liệu SQL tương thích MySQL có quản lý phiên bản kiểu Git: fork, clone, branch, merge, push, pull trên bảng dữ liệu. CLI có cùng lệnh như git (commit, branch, merge, diff, blame theo hàng); chức năng phiên bản dùng được qua bảng hệ thống, hàm và thủ tục SQL; chạy làm MySQL server bằng dolt sql-server. ★ 18/11/2026: 24.933 (GitHub search API), nhóm "Giám sát, CSDL & Phân tích" trong kho-repo của Phan Đông Giang, mục 08 §6c.5

**Hồ sơ gốc:** [mục 08](../08-awesome-lists-learning/README.md#6c511-giám-sát-csdl--phân-tích) (bảng/đoạn chung, giữ nguyên tại chỗ).

<a id="chuyen-doris"></a>

### doris

`apache/doris` · License: Apache-2.0 · ★ 16.238 · docs-read · 2026-11-18

Cơ sở dữ liệu phân tích và tìm kiếm thời gian thực kiến trúc MPP thuộc Apache: phân tích SQL nhanh, tăng tốc truy vấn lakehouse và tìm kiếm hybrid trên dữ liệu có cấu trúc, văn bản, vector. Nạp dữ liệu dạng luồng và truy vấn dưới một giây ở độ đồng thời cao; truy vấn trực tiếp Iceberg, Delta Lake, Hudi; có Kubernetes Operator để triển khai. Điều kiện: Một số phụ thuộc bên thứ ba không tương thích Apache 2.0, cần tắt tính năng tương ứng nếu muốn tuân thủ hoàn toàn. ★ 18/11/2026: 16.238 (GitHub search API), nhóm "Giám sát, CSDL & Phân tích" trong kho-repo của Phan Đông Giang, mục 08 §6c.5

**Hồ sơ gốc:** [mục 08](../08-awesome-lists-learning/README.md#6c511-giám-sát-csdl--phân-tích) (bảng/đoạn chung, giữ nguyên tại chỗ).

<a id="chuyen-excelize"></a>

### excelize

`qax-os/excelize` · License: BSD 3-Clause · ★ 21.137 · docs-read · 2026-11-18

Thư viện Go thuần để đọc và ghi tệp bảng tính XLAM/XLSM/XLSX/XLTM/XLTX của Microsoft Excel 2007 trở lên. Viết bằng Go thuần, không phụ thuộc Excel; có API streaming để ghi/đọc trang tính dữ liệu rất lớn; mỗi thành phần (calc, chart, crypt, datavalidation...) có tệp test riêng. Điều kiện: Cần Go 1.26.0 trở lên. ★ 18/11/2026: 21.137 (GitHub search API), nhóm "Ngôn ngữ & Runtime" trong kho-repo của Phan Đông Giang, mục 08 §6c.5

**Hồ sơ gốc:** [mục 08](../08-awesome-lists-learning/README.md#6c514-ngôn-ngữ--runtime) (bảng/đoạn chung, giữ nguyên tại chỗ).

<a id="chuyen-bitcoin"></a>

### bitcoin

`bitcoin/bitcoin` · License: MIT · ★ 90.693 · docs-read · 2026-11-18

Bitcoin Core: phần mềm nút kết nối mạng ngang hàng Bitcoin, tải và xác thực đầy đủ khối và giao dịch, kèm ví và giao diện đồ họa tùy chọn. Build bằng CMake, có unit test chạy qua ctest và test chức năng/hồi quy viết bằng Python; tag phát hành ổn định được cắt từ nhánh release; có SECURITY.md và quy trình đóng góp trong CONTRIBUTING.md. Điều kiện: README nhấn mạnh nhánh master không đảm bảo ổn định và đây là dự án nhạy cảm bảo mật, lỗi có thể gây mất tiền. ★ 18/11/2026: 90.693 (GitHub search API), nhóm "Tài chính & Crypto" trong kho-repo của Phan Đông Giang, mục 08 §6c.5

**Hồ sơ gốc:** [mục 08](../08-awesome-lists-learning/README.md#6c524-tài-chính--crypto) (bảng/đoạn chung, giữ nguyên tại chỗ).

<a id="chuyen-union"></a>

### union

`unionlabs/union` · License: Hai file giấy phép ở gốc · ★ 73.711 · docs-read · 2026-11-18

Union: lớp hạ tầng zero-knowledge cho truyền thông điệp tổng quát, chuyển tài sản, NFT và DeFi giữa các chuỗi, dựa trên xác minh đồng thuận và triển khai IBC. Gồm nút uniond (Go, CometBLS), prover galoisd (Go, Gnark), relayer voyager (Rust), hợp đồng CosmWasm và EVM, TypeScript SDK; build tái lập được bằng Nix (nix build .#uniond); kết nối chuỗi Cosmos và EVM như Ethereum, Arbitrum, Berachain. Điều kiện: Một số thành phần chỉ build được trên Linux (macOS cần VM NixOS); liên quan tài sản tiền mã hóa. ★ 18/11/2026: 73.711 (GitHub search API), nhóm "Tài chính & Crypto" trong kho-repo của Phan Đông Giang, mục 08 §6c.5

**Hồ sơ gốc:** [mục 08](../08-awesome-lists-learning/README.md#6c524-tài-chính--crypto) (bảng/đoạn chung, giữ nguyên tại chỗ).

<a id="anhkysuai-2026-11-23-thingsboard"></a>

### ThingsBoard

**Repo:** [thingsboard/thingsboard](https://github.com/thingsboard/thingsboard) · **License:** BUSL-1.1 cho 4.4+; một số phần Apache-2.0 · **★ 22,714 (GitHub API, 2026-11-23)**

**Mục đích:** Nền tảng IoT quản lý thiết bị, thu telemetry, rule chain, cảnh báo và dashboard.

**Giá trị và cơ chế:** README và manifest thể hiện hệ backend/frontend đầy đủ cho luồng thiết bị–dữ liệu–hiển thị; hữu ích tham khảo kiến trúc sản phẩm IoT tự lưu trữ.

**Giới hạn:** HEAD 4.4.1-SNAPSHOT chịu BUSL: miễn phí thương mại tối đa 100 thiết bị/một server, phi thương mại 1.000, kèm key và thương hiệu; đổi Apache sau bốn năm. Không dùng nhãn Apache của bản cũ cho HEAD. Chưa triển khai.

**Cách tham khảo/tích hợp:** Đối chiếu số thiết bị và bản license, thử dữ liệu giả lập trước nối hệ thống vận hành.

**Thay thế:** [Node-RED](../05-low-code-llm-platforms/README.md#factory-lowcode-runtime-boundaries-2026-11-04), mainflux, home-assistant.

**Bằng chứng:** `docs-read`, ngày 2026-11-23, commit [`2f2a2bd63a82`](https://github.com/thingsboard/thingsboard/commit/2f2a2bd63a82f4fa4dedd414015576df6156146e). README và các tài liệu/manifest/CI hiện diện, đọc chọn lọc; chưa kiểm implementation. Chưa cài/chạy upstream.

**Nguồn:** [README.md](https://github.com/thingsboard/thingsboard/blob/2f2a2bd63a82f4fa4dedd414015576df6156146e/README.md) · [LICENSE](https://github.com/thingsboard/thingsboard/blob/2f2a2bd63a82f4fa4dedd414015576df6156146e/LICENSE) · [metadata GitHub](https://api.github.com/repos/thingsboard/thingsboard).

<a id="nt-2026-11-23"></a>

## Nâng trần theo khoảng trống — 23/11/2026

Phần này có các hồ sơ mới của đợt nâng trần: mười trinh sát tìm trên internet và GitHub những mảng mà chuyên mục còn thiếu hoặc chỉ có hồ sơ cũ, rồi mỗi repo được clone nông tại một commit cố định, đọc LICENSE, README, ít nhất một file triển khai thật và CI nếu có; không cài hay chạy mã upstream. Mô tả của trinh sát nhiều chỗ sai so với mã thật, và các chỗ đó được sửa ngay trong từng hồ sơ. Số sao lấy sau bằng GitHub search API nên có thể để trống.

<a id="nt-stalwart"></a>

### Stalwart Mail and Collaboration Server

| Thuộc tính | Giá trị |
|---|---|
| Repo | https://github.com/stalwartlabs/stalwart |
| License | AGPL-3.0-only OR LicenseRef-SEL (song song với Stalwart Enterprise License 2.0 trong LICENSES/); 227 file chỉ mang LicenseRef-SEL |
| Phiên bản đã đọc | `b2d3df9a9b1c3e0cd1d5ccccc16acd6f44381afa` (commit 2026-11-23) |
| Kiểm chứng | 2026-11-23; code-read; đã đọc README.md, LICENSES/LicenseRef-SEL.txt, Cargo.toml, crates/main/src/main.rs, crates/dav/src/lib.rs, crates/main/Cargo.toml, .github/workflows/ci.yml, AGENTS.md; chưa chạy upstream |
| Khoảng trống lấp | Tích hợp email/lịch/tài liệu (JMAP, CalDAV, CardDAV): máy chủ thật để thử client tích hợp |
| Cơ chế đáng học | - crates/dav/src/lib.rs định nghĩa các method WebDAV/CalDAV (REPORT, MKCALENDAR, ACL...) ánh xạ sang sự kiện trace, mã tách thành module calendar, card, file, principal<br>- crates/calcard tách riêng parser/writer iCalendar, vCard, JSCalendar, JSContact khỏi tầng giao thức (icalendar/parser.rs, writer.rs)<br>- crates/dav/src/calendar có scheduling.rs, freebusy.rs, availability.rs: CalDAV scheduling (RFC 6638) nằm cùng máy chủ<br>- README nêu webhook cho tự động hóa theo sự kiện và OpenTelemetry/Prometheus cho quan sát (chưa xác minh bằng chạy) |
| Tiêu chí và cách kiểm | CI (.github/workflows/ci.yml) chỉ chạy khi tag v*.*.* hoặc workflow_dispatch và tập trung dựng nhị phân/Docker đa kiến trúc ký cosign; workflow này không có bước test nên không chứng minh độ phủ kiểm thử. Kiểm bằng máy cho giao thức: chưa xác minh. |
| Giới hạn và rủi ro | License kép AGPL hoặc SEL: dùng bản AGPL thì nghĩa vụ mạng của AGPL áp dụng; tính năng Enterprise cần khóa license gắn tên miền (SEL 1.5) và cấm bán lại (SEL 2.3). 227 file chỉ có SEL nên không dùng được theo AGPL. AGENTS.md cấm tác nhân mở issue/PR/báo cáo bảo mật tự sinh, cần tôn trọng nếu dùng agent trên repo. Đây là hệ thống sản xuất, không phải thư viện nhúng; rủi ro vận hành mail (DNS, deliverability) cao. |
| So với | Radicale (CalDAV/CardDAV nhỏ, GPL), Cal.com (calcom-cal.diy, lịch đặt hẹn), Mail-0 Zero (mail-0-zero) |
| Nguồn | [README.md](https://github.com/stalwartlabs/stalwart/blob/b2d3df9a9b1c3e0cd1d5ccccc16acd6f44381afa/README.md) · [LicenseRef-SEL.txt](https://github.com/stalwartlabs/stalwart/blob/b2d3df9a9b1c3e0cd1d5ccccc16acd6f44381afa/LICENSES/LicenseRef-SEL.txt) · [Cargo.toml](https://github.com/stalwartlabs/stalwart/blob/b2d3df9a9b1c3e0cd1d5ccccc16acd6f44381afa/Cargo.toml) · [main.rs](https://github.com/stalwartlabs/stalwart/blob/b2d3df9a9b1c3e0cd1d5ccccc16acd6f44381afa/crates/main/src/main.rs) · [lib.rs](https://github.com/stalwartlabs/stalwart/blob/b2d3df9a9b1c3e0cd1d5ccccc16acd6f44381afa/crates/dav/src/lib.rs) · [Cargo.toml](https://github.com/stalwartlabs/stalwart/blob/b2d3df9a9b1c3e0cd1d5ccccc16acd6f44381afa/crates/main/Cargo.toml) · [ci.yml](https://github.com/stalwartlabs/stalwart/blob/b2d3df9a9b1c3e0cd1d5ccccc16acd6f44381afa/.github/workflows/ci.yml) · [AGENTS.md](https://github.com/stalwartlabs/stalwart/blob/b2d3df9a9b1c3e0cd1d5ccccc16acd6f44381afa/AGENTS.md) |

<a id="nt-glpi"></a>

### GLPI

| Thuộc tính | Giá trị |
|---|---|
| Repo | https://github.com/glpi-project/glpi |
| License | GPL-3.0 |
| Phiên bản đã đọc | `74a89ac1764fa9347e777d63add81e07c635c6b0` (commit 2026-11-23) |
| Kiểm chứng | 2026-11-23; code-read; đã đọc README.md, LICENSE, THREAT_MODEL.md, apirest.md, src/CommonITILValidation.php, src/Telemetry.php, src/Glpi/Application/SystemConfigurator.php, .github/workflows/ci.yml; chưa chạy upstream |
| Khoảng trống lấp | Quản lý ticket/helpdesk có API và quy trình phê duyệt |
| Cơ chế đáng học | - src/CommonITILValidation.php: hằng trạng thái NONE/WAITING/ACCEPTED/REFUSED, quyền VALIDATE và canValidate/getTargetCriteriaForUser xác định ai được duyệt; lớp con ChangeValidation, TicketValidation, ITIL_ValidationStep cho phê duyệt nhiều bước<br>- API REST apirest.md: initSession bằng user token, session token, app token lọc theo IP; session mặc định chỉ đọc để gọi song song, ghi cần session_write=true<br>- THREAT_MODEL.md nêu rõ ranh giới tin cậy và bằng chứng cần cho báo cáo bảo mật (quyền theo profile và entity) |
| Tiêu chí và cách kiểm | CI ci.yml chạy lint trên PHP 8.3 và 8.6, và Playwright theo shard (chỉ đọc phần đầu và job playwright); chạy định kỳ hằng đêm. Có phpstan, php-cs-fixer, rector, phpunit trong thư mục gốc (chỉ thấy file cấu hình). Kiểm bằng máy có. |
| Giới hạn và rủi ro | GPL-3.0: nhúng hay sửa rồi phân phối phải mở mã. src/Telemetry.php thu phiên bản, CSDL, web server, PHP, OS và số liệu sử dụng; cronTelemetry POST JSON tới GLPI_TELEMETRY_URI (mặc định https://telemetry.glpi-project.org, đặt trong SystemConfigurator.php); chưa xác minh tác vụ cron mặc định bật hay tắt. Cần PHP và CSDL, giao diện nặng, plugin ngoài chất lượng khác nhau. AGENTS.md có trong repo. |
| So với | Zammad (zammad, helpdesk Ruby, AGPL), OpenProject (opf-openproject), Plane (makeplane-plane) |
| Nguồn | [README.md](https://github.com/glpi-project/glpi/blob/74a89ac1764fa9347e777d63add81e07c635c6b0/README.md) · [LICENSE](https://github.com/glpi-project/glpi/blob/74a89ac1764fa9347e777d63add81e07c635c6b0/LICENSE) · [THREAT_MODEL.md](https://github.com/glpi-project/glpi/blob/74a89ac1764fa9347e777d63add81e07c635c6b0/THREAT_MODEL.md) · [apirest.md](https://github.com/glpi-project/glpi/blob/74a89ac1764fa9347e777d63add81e07c635c6b0/apirest.md) · [CommonITILValidation.php](https://github.com/glpi-project/glpi/blob/74a89ac1764fa9347e777d63add81e07c635c6b0/src/CommonITILValidation.php) · [Telemetry.php](https://github.com/glpi-project/glpi/blob/74a89ac1764fa9347e777d63add81e07c635c6b0/src/Telemetry.php) · [SystemConfigurator.php](https://github.com/glpi-project/glpi/blob/74a89ac1764fa9347e777d63add81e07c635c6b0/src/Glpi/Application/SystemConfigurator.php) · [ci.yml](https://github.com/glpi-project/glpi/blob/74a89ac1764fa9347e777d63add81e07c635c6b0/.github/workflows/ci.yml) |

<a id="nt-zammad"></a>

### Zammad

| Thuộc tính | Giá trị |
|---|---|
| Repo | https://github.com/zammad/zammad |
| License | AGPL-3.0 |
| Phiên bản đã đọc | `0d1ac50043412d104fe6c3a715e5730e7e0dd4b4` (commit 2026-11-23) |
| Kiểm chứng | 2026-11-23; code-read; đã đọc README.md, LICENSE, AGENTS.md, app/models/trigger.rb, app/models/ticket/escalation.rb, app/models/ai/mcp_confirmation.rb, .github/workflows/ci.yaml, .github/workflows/ci/test.sh; chưa chạy upstream |
| Khoảng trống lấp | Quản lý ticket/helpdesk có REST/GraphQL API (kho thiếu ticketing) |
| Cơ chế đáng học | - app/models/trigger.rb: trigger có activator action hoặc time, execution_condition_mode selective hoặc always; trigger theo thời gian dùng Ticket::DailyEventLock để không chạy lặp trong ngày<br>- app/models/ticket/escalation.rb: after_commit gọi escalation_calculation trên bản sao ticket, có callback_loop chặn đệ quy và bỏ qua khi import_mode<br>- app/models/ai/mcp_confirmation.rb: bản ghi xác nhận MCP có request_id, action_digest, expires_at; chỉ dọn bản đã hết hạn nên một phê duyệt không dùng lại được tới khi hết hạn (đọc theo chú thích mã) |
| Tiêu chí và cách kiểm | CI ci.yaml chạy trên PR và cron thứ Sáu: container zammad-ci với PostgreSQL 18 và Redis, chạy lint.sh (nội dung chưa mở), markdownlint, kiểm assets, pnpm test và rspec bỏ qua nhóm system/searchindex/integration (test.sh). Kiểm bằng máy có. |
| Giới hạn và rủi ro | AGPL-3.0: dịch vụ mạng sửa đổi phải công bố mã. Nhắc: Zammad Foundation sở hữu mã nhưng công ty Zammad GmbH bán dịch vụ đám mây. Hai frontend song song nên bề mặt bảo trì lớn. Cần Ruby, Node, PostgreSQL, Redis và thường Elasticsearch để tìm kiếm. Tính năng AI gửi nội dung ticket cho nhà cung cấp mô hình đã cấu hình (chưa xác minh bằng chạy). AGENTS.md hướng dẫn tác nhân nhưng không đổi license. |
| So với | GLPI (glpi, ITSM PHP, GPL), OpenProject (opf-openproject), Planka (plankanban-planka) |
| Nguồn | [README.md](https://github.com/zammad/zammad/blob/0d1ac50043412d104fe6c3a715e5730e7e0dd4b4/README.md) · [LICENSE](https://github.com/zammad/zammad/blob/0d1ac50043412d104fe6c3a715e5730e7e0dd4b4/LICENSE) · [AGENTS.md](https://github.com/zammad/zammad/blob/0d1ac50043412d104fe6c3a715e5730e7e0dd4b4/AGENTS.md) · [trigger.rb](https://github.com/zammad/zammad/blob/0d1ac50043412d104fe6c3a715e5730e7e0dd4b4/app/models/trigger.rb) · [escalation.rb](https://github.com/zammad/zammad/blob/0d1ac50043412d104fe6c3a715e5730e7e0dd4b4/app/models/ticket/escalation.rb) · [mcp_confirmation.rb](https://github.com/zammad/zammad/blob/0d1ac50043412d104fe6c3a715e5730e7e0dd4b4/app/models/ai/mcp_confirmation.rb) · [ci.yaml](https://github.com/zammad/zammad/blob/0d1ac50043412d104fe6c3a715e5730e7e0dd4b4/.github/workflows/ci.yaml) · [test.sh](https://github.com/zammad/zammad/blob/0d1ac50043412d104fe6c3a715e5730e7e0dd4b4/.github/workflows/ci/test.sh) |

<a id="nt-radicale"></a>

### Radicale

| Thuộc tính | Giá trị |
|---|---|
| Repo | https://github.com/Kozea/Radicale |
| License | GPL-3.0 |
| Phiên bản đã đọc | `c23d6759c70bfa5554b2baeaa01df83ea51bafc7` (commit 2026-11-21) |
| Kiểm chứng | 2026-11-23; code-read; đã đọc README.md, COPYING.md, pyproject.toml, radicale/rights/owner_write.py, radicale/item/`__init__`.py, caldav_compat_tests/README.md, caldav_compat_tests/test_compatibility.py, .github/workflows/test.yml; chưa chạy upstream |
| Khoảng trống lấp | Máy chủ CalDAV/CardDAV đơn giản làm môi trường thử tích hợp lịch, và bộ kiểm tương thích client/server |
| Cơ chế đáng học | - caldav_compat_tests/test_compatibility.py: chạy caldav-server-tester với server Radicale khởi động như tiến trình con, so kết quả với EXPECTED_DEVIATIONS (ví dụ scheduling: unsupported, principal-search: unsupported); phiên bản thư viện client ghim chính xác trong extra caldav_test<br>- radicale/rights/owner_write.py: người dùng đã xác thực đọc được tất cả nhưng chỉ ghi vào thư mục có tên trùng tên mình<br>- radicale/item/`__init__`.py: bọc vobject.readComponents (có allowQP) và phân loại VCALENDAR, VCARD, VLIST; item/filter.py giới hạn số lần liệt kê RRULE vô hạn |
| Tiêu chí và cách kiểm | CI test.yml có job lint rồi chạy tox (ví dụ Python 3.15 trên Ubuntu 26, có biến thể loglevel; chỉ đọc phần đầu file); thư mục radicale/tests, integ_tests và caldav_compat_tests tồn tại, chưa xác minh job nào chạy từng thư mục. Kiểm bằng máy có. |
| Giới hạn và rủi ro | GPL-3.0: sửa và phân phối phải mở mã. Lưu file trong hệ thống tệp đơn giản nên không hợp quy mô lớn hay đa nút; không có scheduling iTIP. Với RFC 5545 đầy đủ (VTIMEZONE, RRULE phức tạp) cần kiểm riêng. Mặc định mở cổng cục bộ, cấu hình xác thực và TLS là việc của người vận hành. |
| So với | Stalwart (stalwart, đủ bộ mail và scheduling), Cal.com (calcom-cal.diy) |
| Nguồn | [README.md](https://github.com/Kozea/Radicale/blob/c23d6759c70bfa5554b2baeaa01df83ea51bafc7/README.md) · [COPYING.md](https://github.com/Kozea/Radicale/blob/c23d6759c70bfa5554b2baeaa01df83ea51bafc7/COPYING.md) · [pyproject.toml](https://github.com/Kozea/Radicale/blob/c23d6759c70bfa5554b2baeaa01df83ea51bafc7/pyproject.toml) · [owner_write.py](https://github.com/Kozea/Radicale/blob/c23d6759c70bfa5554b2baeaa01df83ea51bafc7/radicale/rights/owner_write.py) · [\_\_init\_\_.py](https://github.com/Kozea/Radicale/blob/c23d6759c70bfa5554b2baeaa01df83ea51bafc7/radicale/item/`__init__`.py) · [README.md](https://github.com/Kozea/Radicale/blob/c23d6759c70bfa5554b2baeaa01df83ea51bafc7/caldav_compat_tests/README.md) · [test_compatibility.py](https://github.com/Kozea/Radicale/blob/c23d6759c70bfa5554b2baeaa01df83ea51bafc7/caldav_compat_tests/test_compatibility.py) · [test.yml](https://github.com/Kozea/Radicale/blob/c23d6759c70bfa5554b2baeaa01df83ea51bafc7/.github/workflows/test.yml) |

<a id="nt-oca-dms"></a>

### OCA dms (Odoo 19)

| Thuộc tính | Giá trị |
|---|---|
| Repo | https://github.com/OCA/dms |
| License | LGPL-3.0 (module dms; LICENSE gốc repo là AGPL-3.0) |
| Phiên bản đã đọc | `b41bc8a454b5e6bed53f9b94286dba0cf3d28d7c` (commit 2026-11-11) |
| Kiểm chứng | 2026-11-23; code-read; đã đọc README.md, LICENSE, test.yml, dms/`__manifest__`.py, storage.py, access_groups.py và dms_file.py; chưa chạy upstream |
| Khoảng trống lấp | Quản lý tài liệu trong Odoo làm nền cho kiểm soát tài liệu; không có phiên bản hay phê duyệt |
| Cơ chế đáng học | • dms.storage chọn nơi lưu database, file hoặc attachment, có thao tác di chuyển thủ công khi đổi kiểu (storage.py).<br>• dms.access.group: nhóm cha con, quyền create, write, unlink và biến thể inclusive thừa hưởng, gán cho nhóm Odoo hoặc người dùng cụ thể, gắn vào thư mục (access_groups.py).<br>• Khóa tệp: lock và unlock ghi locked_by, tính is_lock_editor để chỉ người khóa được sửa (dms_file.py).<br>• Chia sẻ qua cổng bằng access_token, so sánh bằng consteq (dms_file.py). |
| Tiêu chí và cách kiểm | CI test.yml chạy trên container Odoo 19 và OCB 19, kiểm license bằng manifestoo; thư mục tests có test truy cập, thư mục, tệp, storage, portal và benchmark. Chưa mở các file test, chưa chạy. |
| Giới hạn và rủi ro | Không có version chain, trạng thái dự thảo hay đã duyệt, hạn rà soát, hay nhật ký phân phối bản kiểm soát: muốn ISO 9001 7.5 (chưa xác minh điều khoản) phải tự xây. License: LICENSE gốc của repo là AGPL-3.0 nhưng manifest module ghi LGPL-3.0 (nhiều mã gốc MuK IT). Phụ thuộc Odoo 19 và các module mail, portal, onboarding. Chia sẻ công khai bằng token cần kiểm cấu hình trước khi mở ra mạng. |
| So với | odoo-odoo trong kho (nền); paperless-ngx trong kho (lưu trữ tài liệu độc lập, không phải Odoo); nextcloud-server trong kho (chia sẻ tệp). |
| Nguồn | [README.md](https://github.com/OCA/dms/blob/b41bc8a454b5e6bed53f9b94286dba0cf3d28d7c/README.md) · [LICENSE](https://github.com/OCA/dms/blob/b41bc8a454b5e6bed53f9b94286dba0cf3d28d7c/LICENSE) · [test.yml](https://github.com/OCA/dms/blob/b41bc8a454b5e6bed53f9b94286dba0cf3d28d7c/.github/workflows/test.yml) · [\_\_manifest\_\_.py](https://github.com/OCA/dms/blob/b41bc8a454b5e6bed53f9b94286dba0cf3d28d7c/dms/`__manifest__`.py) · [storage.py](https://github.com/OCA/dms/blob/b41bc8a454b5e6bed53f9b94286dba0cf3d28d7c/dms/models/storage.py) · [access_groups.py](https://github.com/OCA/dms/blob/b41bc8a454b5e6bed53f9b94286dba0cf3d28d7c/dms/models/access_groups.py) · [dms_file.py](https://github.com/OCA/dms/blob/b41bc8a454b5e6bed53f9b94286dba0cf3d28d7c/dms/models/dms_file.py) |

<a id="nt-loro"></a>

### Loro

| Thuộc tính | Giá trị |
|---|---|
| Repo | https://github.com/loro-dev/loro |
| License | MIT (lõi); skills/moonbit dưới Apache-2.0 |
| Phiên bản đã đọc | `16fe805f935600cd6e4f106f212e9315b878ba95` (commit 2026-11-23) |
| Kiểm chứng | 2026-11-23; code-read; đã đọc LICENSE, README, Cargo.toml, crates/loro/src/lib.rs, rust.yml, docs/shallow-snapshot-concurrency.md, skills/loro/SKILL.md và fit-and-architecture.md; chưa chạy upstream |
| Khoảng trống lấp | Local-first / CRDT (CRDT lõi có lịch sử phiên bản) |
| Cơ chế đáng học | - `LoroDoc` (crates/loro/src/lib.rs) gộp CRDT JSON với lịch sử đầy đủ: `checkout(frontiers)`, `fork_at`, `revert_to` cho time travel; `export(ExportMode)` cho cập nhật theo version vector, snapshot hoặc shallow snapshot.<br>- Shallow snapshot giống git shallow clone; `docs/shallow-snapshot-concurrency.md` nêu bảo đảm cụ thể: cập nhật sau gốc shallow áp dụng bình thường, cập nhật trước gốc là no-op, cập nhật dựa trên phiên bản trước gốc bị từ chối chứ không treo, có test dẫn chiếu.<br>- Có `export_pending_updates` để lưu các cập nhật chờ phụ thuộc nhân quả, kèm chỉ dẫn lưu snapshot và sidecar như một checkpoint (doc comment trong lib.rs).<br>- Repo kèm skill `skills/loro` cho agent (SKILL.md và các chương tham chiếu) nêu rõ khi nào Loro không phù hợp: bất biến tài chính, khoá độc quyền, phân quyền tại thời điểm ghi. |
| Tiêu chí và cách kiểm | Có crate `fuzz` (crdt_fuzzer, one_doc_fuzzer, mem_kv_fuzzer) và nhiều test hồi quy trong `crates/fuzz/tests`; workflow rust.yml (đã mở) chạy `check` 32-bit, kiểm loro-js và `deno task test-all` với test Rust trên macOS. Chưa xác minh kết quả thực tế vì chưa chạy. Có `deny.toml` và thư mục `supply-chain` cho kiểm chuỗi cung ứng (chỉ thấy tồn tại, chưa đọc nội dung). |
| Giới hạn và rủi ro | Mô tả trinh sát đúng về MIT nhưng thiếu: repo có thư mục con skills/moonbit dưới Apache-2.0 (LICENSE riêng) và nhiều crate có LICENSE riêng. CRDT không bảo đảm bất biến toàn cục. Phiên bản crate 1.19.0, thay đổi nhanh. Tuyên bố hiệu năng của tác giả (chưa xác minh). Chuỗi thấy `telemetry` chỉ trong doc comment về origin của import, không phải thu thập dữ liệu. |
| So với | pubkey-rxdb (RxDB, không phải CRDT lõi), tinybase (cùng lô) |
| Nguồn | [LICENSE](https://github.com/loro-dev/loro/blob/16fe805f935600cd6e4f106f212e9315b878ba95/LICENSE) · [README.md](https://github.com/loro-dev/loro/blob/16fe805f935600cd6e4f106f212e9315b878ba95/README.md) · [Cargo.toml](https://github.com/loro-dev/loro/blob/16fe805f935600cd6e4f106f212e9315b878ba95/Cargo.toml) · [crates/loro/Cargo.toml](https://github.com/loro-dev/loro/blob/16fe805f935600cd6e4f106f212e9315b878ba95/crates/loro/Cargo.toml) · [crates/loro/src/lib.rs](https://github.com/loro-dev/loro/blob/16fe805f935600cd6e4f106f212e9315b878ba95/crates/loro/src/lib.rs) · [.github/workflows/rust.yml](https://github.com/loro-dev/loro/blob/16fe805f935600cd6e4f106f212e9315b878ba95/.github/workflows/rust.yml) · [docs/shallow-snapshot-concurrency.md](https://github.com/loro-dev/loro/blob/16fe805f935600cd6e4f106f212e9315b878ba95/docs/shallow-snapshot-concurrency.md) · [skills/loro/SKILL.md](https://github.com/loro-dev/loro/blob/16fe805f935600cd6e4f106f212e9315b878ba95/skills/loro/SKILL.md) · [skills/loro/references/fit-and-architecture.md](https://github.com/loro-dev/loro/blob/16fe805f935600cd6e4f106f212e9315b878ba95/skills/loro/references/fit-and-architecture.md) · [skills/moonbit/LICENSE](https://github.com/loro-dev/loro/blob/16fe805f935600cd6e4f106f212e9315b878ba95/skills/moonbit/LICENSE) |

<a id="nt-authlib"></a>

### Authlib

| Thuộc tính | Giá trị |
|---|---|
| Repo | https://github.com/authlib/authlib |
| License | BSD-3-Clause hoặc giấy phép thương mại (COMMERCIAL-LICENSE) |
| Phiên bản đã đọc | `c451e6d1238678231ee21e31964cc8ce34474a37` (commit 2026-11-20) |
| Kiểm chứng | 2026-11-23; code-read; đã đọc LICENSE, COMMERCIAL-LICENSE, README, pyproject.toml, AGENTS.md, python.yml, rfc7636/challenge.py (và liệt kê rfc6749/grants); chưa chạy upstream |
| Khoảng trống lấp | Xác thực hiện đại (OAuth 2.x/OIDC phía Python); không có passkey |
| Cơ chế đáng học | - Mỗi RFC một module (`authlib/oauth2/rfcNNNN/`): 6749, 6750, 7009, 7523, 7591/7592, 7636, 7662, 8414, 8628, 8693, 9068, 9101, 9207, 9470, 9728, cộng `authlib/oidc/core`; module RFC cắm vào lõi bằng hook hoặc kế thừa, không sửa `rfc6749/` (AGENTS.md).<br>- Dùng được cho cả client và authorization server/resource server, kèm tích hợp Flask, Django, requests, httpx, Starlette (thư mục `authlib/integrations`).<br>- `CodeChallenge` (rfc7636/challenge.py) so khớp S256 bằng `hmac.compare_digest`, nhưng mặc định method là `plain` và hỗ trợ cả plain; PKCE bắt buộc hay không phụ thuộc `is_code_challenge_required`, mặc định không bắt buộc (`required` là tham số đã bị đánh dấu deprecate).<br>- JOSE chuyển sang `joserfc`; `authlib.jose` đã deprecated (AGENTS.md, pyproject). |
| Tiêu chí và cách kiểm | Test bằng pytest trong `tests/` (oauth2, oauth1, flask, django, jose, clients); python.yml (đã mở) chạy ma trận Python 3.11 đến 3.15 và pypy3.11, kèm lint ruff, codespell, zizmor theo AGENTS.md. Không có bộ test conformance OpenID chính thức trong repo (chưa thấy chứng nhận OpenID). |
| Giới hạn và rủi ro | Hai giấy phép: BSD-3-Clause cho mọi dự án, còn COMMERCIAL-LICENSE là điều khoản mua riêng để hỗ trợ thương mại, không phải điều kiện bắt buộc dùng BSD. Mô tả trinh sát về "passkey/WebAuthn, OAuth 2.1" không đúng với mã đã đọc: không có module WebAuthn, và tìm trong authlib/ và docs/ không thấy OAuth 2.1; thư viện là OAuth 2.0/OIDC cộng nhiều RFC mở rộng. Bản 1.10.0b1 (beta). AGENTS.md cấm agent tự động mở issue/PR khi chưa có người duyệt: tôn trọng khi đóng góp. Dùng cho server cần tự bật PKCE bắt buộc và tắt plain. |
| So với | node-oidc-provider (cùng lô), keycloak, authelia-authelia, goauthentik-authentik |
| Nguồn | [LICENSE](https://github.com/authlib/authlib/blob/c451e6d1238678231ee21e31964cc8ce34474a37/LICENSE) · [COMMERCIAL-LICENSE](https://github.com/authlib/authlib/blob/c451e6d1238678231ee21e31964cc8ce34474a37/COMMERCIAL-LICENSE) · [README.md](https://github.com/authlib/authlib/blob/c451e6d1238678231ee21e31964cc8ce34474a37/README.md) · [pyproject.toml](https://github.com/authlib/authlib/blob/c451e6d1238678231ee21e31964cc8ce34474a37/pyproject.toml) · [AGENTS.md](https://github.com/authlib/authlib/blob/c451e6d1238678231ee21e31964cc8ce34474a37/AGENTS.md) · [.github/workflows/python.yml](https://github.com/authlib/authlib/blob/c451e6d1238678231ee21e31964cc8ce34474a37/.github/workflows/python.yml) · [authlib/oauth2/rfc7636/challenge.py](https://github.com/authlib/authlib/blob/c451e6d1238678231ee21e31964cc8ce34474a37/authlib/oauth2/rfc7636/challenge.py) · [authlib/oauth2/rfc6749/grants/authorization_code.py](https://github.com/authlib/authlib/blob/c451e6d1238678231ee21e31964cc8ce34474a37/authlib/oauth2/rfc6749/grants/authorization_code.py) |

<a id="nt-faststream"></a>

### FastStream

| Thuộc tính | Giá trị |
|---|---|
| Repo | https://github.com/ag2ai/faststream |
| License | Apache-2.0 |
| Phiên bản đã đọc | `d78fc4298629666fa4171bb37feeb5397445afd4` (commit 2026-11-22) |
| Kiểm chứng | 2026-11-23; code-read; đã đọc LICENSE, README, pyproject.toml, pr_tests.yaml, asyncapi/factory.py, v3_0_0/generate.py, kafka/testing.py (đầu file); chưa chạy upstream |
| Khoảng trống lấp | Kiến trúc event-driven (Kafka, RabbitMQ, NATS, Redis) có tài liệu AsyncAPI sinh từ mã |
| Cơ chế đáng học | - Khai báo subscriber/publisher bằng decorator trên Pydantic; framework sinh tài liệu AsyncAPI 2.6.0 hoặc 3.0.0 từ chính các khai báo đó (`specification/asyncapi/factory.py`, `v3_0_0/generate.py`), nên hợp đồng sự kiện không lệch khỏi mã.<br>- Một API thống nhất cho nhiều broker (thư mục kafka, confluent, rabbit, nats, redis, mqtt), kèm CLI chạy ứng dụng và phục vụ ASGI.<br>- `TestKafkaBroker` và các bản tương tự cho phép test mà không cần broker thật; test `tests/asyncapi/` đối chiếu schema sinh ra theo từng broker.<br>- Middleware OpenTelemetry và Prometheus tích hợp sẵn (`faststream/opentelemetry`, `faststream/prometheus`). |
| Tiêu chí và cách kiểm | pr_tests.yaml (đã mở) chạy pytest trên Python 3.10 đến 3.15 với `-m "(slow and not connected) or not connected"`, có job riêng kafka smoke và kafka thật với dịch vụ trong CI, bật `covdefaults`; có workflow benchmark CodSpeed. Tất cả kiểm bằng máy, chưa chạy lại. |
| Giới hạn và rủi ro | Repo nay là ag2ai/faststream (chuyển từ tổ chức cũ), license Apache-2.0 đúng như trinh sát. Phiên bản 0.7.9: chưa 1.0, API còn có thể đổi. Tài liệu AsyncAPI chỉ mô tả phía ứng dụng FastStream, không thay một đặc tả viết tay. Kiểm AsyncAPI sinh ra bằng test snapshot của chính dự án, không bằng validator ngoài trong phần đã đọc. Không thấy telemetry trong phần đã mở. |
| So với | nats-io-nats-server (là broker, không phải framework), asyncapi-spec (cùng lô) |
| Nguồn | [LICENSE](https://github.com/ag2ai/faststream/blob/d78fc4298629666fa4171bb37feeb5397445afd4/LICENSE) · [README.md](https://github.com/ag2ai/faststream/blob/d78fc4298629666fa4171bb37feeb5397445afd4/README.md) · [pyproject.toml](https://github.com/ag2ai/faststream/blob/d78fc4298629666fa4171bb37feeb5397445afd4/pyproject.toml) · [.github/workflows/pr_tests.yaml](https://github.com/ag2ai/faststream/blob/d78fc4298629666fa4171bb37feeb5397445afd4/.github/workflows/pr_tests.yaml) · [faststream/specification/asyncapi/factory.py](https://github.com/ag2ai/faststream/blob/d78fc4298629666fa4171bb37feeb5397445afd4/faststream/specification/asyncapi/factory.py) · [faststream/specification/asyncapi/v3_0_0/generate.py](https://github.com/ag2ai/faststream/blob/d78fc4298629666fa4171bb37feeb5397445afd4/faststream/specification/asyncapi/v3_0_0/generate.py) · [faststream/kafka/testing.py](https://github.com/ag2ai/faststream/blob/d78fc4298629666fa4171bb37feeb5397445afd4/faststream/kafka/testing.py) |

<a id="nt-tinybase"></a>

### TinyBase

| Thuộc tính | Giá trị |
|---|---|
| Repo | https://github.com/tinyplex/tinybase |
| License | MIT |
| Phiên bản đã đọc | `540cd40789a2745a6244ef42d29d83b144d5e6ae` (commit 2026-11-12) |
| Kiểm chứng | 2026-11-23; code-read; đã đọc LICENSE, readme.md, package.json, ci.yml, src/common/hlc.ts, src/mergeable-store/index.ts (đầu file), convergence.fuzz.test.ts (đầu file), synchronizer-ws-server/index.ts (đoạn authorize); chưa chạy upstream |
| Khoảng trống lấp | Local-first / CRDT (store reactive có đồng bộ) |
| Cơ chế đáng học | - `MergeableStore` (src/mergeable-store/index.ts) gắn mỗi cell và value một dấu thời gian HLC (`src/common/hlc.ts`) cùng hash theo bảng, hàng, cell; hai peer so hash để chỉ trao đổi phần khác nhau. Gộp theo kiểu last-writer-wins từng cell.<br>- HLC có `MAX_CLOCK_SKEW_SECONDS = 300` và `isHlc` từ chối dấu thời gian vượt ngưỡng, chống đồng hồ lệch.<br>- Nhiều synchronizer cắm được: BroadcastChannel, WebSocket client và server (kèm Durable Object, bản simple), local; WsServer có `authorize`, `canWriteCell`, `canWriteValue` để chặn ghi (dòng 156 đến 177 của synchronizer-ws-server/index.ts), có test riêng cho authorization.<br>- Cùng một store có truy vấn, index, metric, relationship và checkpoint (undo), cộng persister cho IndexedDB, SQLite, PostgreSQL, Yjs, Automerge. |
| Tiêu chí và cách kiểm | `convergence.fuzz.test.ts` (đã mở phần đầu) dùng nhiều seed: các peer sửa ngẫu nhiên qua mạng giả lập có đảo thứ tự và rớt gói, khi mạng yên mọi peer phải có cùng nội dung, stamp và hash. ci.yml chạy compile, lint, spell, tsc và `testUnitFast` trên Node 24. README tuyên bố 100% test coverage (chưa xác minh). |
| Giới hạn và rủi ro | Mô hình dữ liệu là bảng và key-value với LWW từng cell, không phải CRDT văn bản hay danh sách có thứ tự như Loro; không dùng cho chỉnh sửa văn bản đồng thời. Server tự host cần tự lo xác thực và authorize. Phiên bản 10.1.0. MIT đúng như trinh sát. Không thấy telemetry trong phần đã mở. readme.md chủ yếu là HTML sinh ra, ít thông tin kỹ thuật. |
| So với | loro (cùng lô), pubkey-rxdb |
| Nguồn | [LICENSE](https://github.com/tinyplex/tinybase/blob/540cd40789a2745a6244ef42d29d83b144d5e6ae/LICENSE) · [readme.md](https://github.com/tinyplex/tinybase/blob/540cd40789a2745a6244ef42d29d83b144d5e6ae/readme.md) · [package.json](https://github.com/tinyplex/tinybase/blob/540cd40789a2745a6244ef42d29d83b144d5e6ae/package.json) · [.github/workflows/ci.yml](https://github.com/tinyplex/tinybase/blob/540cd40789a2745a6244ef42d29d83b144d5e6ae/.github/workflows/ci.yml) · [src/common/hlc.ts](https://github.com/tinyplex/tinybase/blob/540cd40789a2745a6244ef42d29d83b144d5e6ae/src/common/hlc.ts) · [src/mergeable-store/index.ts](https://github.com/tinyplex/tinybase/blob/540cd40789a2745a6244ef42d29d83b144d5e6ae/src/mergeable-store/index.ts) · [test/unit/synchronizers/convergence.fuzz.test.ts](https://github.com/tinyplex/tinybase/blob/540cd40789a2745a6244ef42d29d83b144d5e6ae/test/unit/synchronizers/convergence.fuzz.test.ts) · [src/synchronizers/synchronizer-ws-server/index.ts](https://github.com/tinyplex/tinybase/blob/540cd40789a2745a6244ef42d29d83b144d5e6ae/src/synchronizers/synchronizer-ws-server/index.ts) |

<a id="nt-node-oidc-provider"></a>

### node-oidc-provider

| Thuộc tính | Giá trị |
|---|---|
| Repo | https://github.com/panva/node-oidc-provider |
| License | MIT |
| Phiên bản đã đọc | `d0c0cf6e0d48c89d3a084e3aaf6a0078642efd49` (commit 2026-11-20) |
| Kiểm chứng | 2026-11-23; code-read; đã đọc LICENSE.md, README, package.json, conformance.yml, test.yml, lib/helpers/pkce.js, certification/oidc/index.js (đầu file), certification/README.md; chưa chạy upstream |
| Khoảng trống lấp | Xác thực hiện đại (OIDC/OAuth 2.x, FAPI) |
| Cơ chế đáng học | - Authorization server Node triển khai OIDC Core cùng PAR (RFC 9126), DPoP (RFC 9449), JAR, JARM, RAR, mTLS, CIBA, Device Flow, FAPI 1.0 và 2.0; các tính năng thử nghiệm (CIMD, OpenID4VCI, attestation) tách riêng và đổi phiên bản theo bản MINOR (README).<br>- `lib/helpers/pkce.js` chỉ chấp nhận method S256 (method khác bị ném lỗi), kiểm định dạng `code_verifier` và so sánh bằng `constantEquals`.<br>- Cấu hình theo từng tính năng bật hoặc tắt trong `lib/helpers/defaults.js`; không phải tính năng nào cũng bật mặc định (README).<br>- Thư mục `certification/` chứa cấu hình chạy chính server này làm đối tượng của bộ kiểm OpenID Conformance Suite (oidc, fapi, vci). |
| Tiêu chí và cách kiểm | conformance.yml (đã mở) chạy các plan của OpenID Conformance Suite (basic, hybrid, implicit, dynamic với nhiều response_type, FAPI...) khi đổi `lib/` hoặc `certification/`, và theo lịch hàng tuần. test.yml chạy audit npm, lint, kiểm tài liệu cấu hình sinh ra và test bằng `node ./test/run`. Tác giả tuyên bố đạt chứng nhận OpenID cho các profile Basic, Implicit, Hybrid, Config, Form Post, 3rd Party-Init, logout, FAPI 1.0, FAPI CIBA, FAPI 2.0 (tuyên bố trong README, chưa xác minh với trang chứng nhận). |
| Giới hạn và rủi ro | Chỉ là thư viện để dựng authorization server: phần đăng nhập, lưu trữ (adapter), tài khoản và giao diện người dùng đều phải tự viết; thư mục `example/` chỉ để tham khảo. Cần Node 22 trở lên (test.yml đặt min 22). Một tác giả chính. Không thấy telemetry trong lib. License MIT đúng như trinh sát; nhiều file thông báo bên thứ ba (THIRD-PARTY-NOTICES.md, chưa đọc). |
| So với | authlib (cùng lô), keycloak, hydra, authelia-authelia |
| Nguồn | [LICENSE.md](https://github.com/panva/node-oidc-provider/blob/d0c0cf6e0d48c89d3a084e3aaf6a0078642efd49/LICENSE.md) · [README.md](https://github.com/panva/node-oidc-provider/blob/d0c0cf6e0d48c89d3a084e3aaf6a0078642efd49/README.md) · [package.json](https://github.com/panva/node-oidc-provider/blob/d0c0cf6e0d48c89d3a084e3aaf6a0078642efd49/package.json) · [.github/workflows/conformance.yml](https://github.com/panva/node-oidc-provider/blob/d0c0cf6e0d48c89d3a084e3aaf6a0078642efd49/.github/workflows/conformance.yml) · [.github/workflows/test.yml](https://github.com/panva/node-oidc-provider/blob/d0c0cf6e0d48c89d3a084e3aaf6a0078642efd49/.github/workflows/test.yml) · [lib/helpers/pkce.js](https://github.com/panva/node-oidc-provider/blob/d0c0cf6e0d48c89d3a084e3aaf6a0078642efd49/lib/helpers/pkce.js) · [certification/oidc/index.js](https://github.com/panva/node-oidc-provider/blob/d0c0cf6e0d48c89d3a084e3aaf6a0078642efd49/certification/oidc/index.js) · [certification/README.md](https://github.com/panva/node-oidc-provider/blob/d0c0cf6e0d48c89d3a084e3aaf6a0078642efd49/certification/README.md) |

<a id="nt-openbao-openbao"></a>

### OpenBao

| Thuộc tính | Giá trị |
|---|---|
| Repo | https://github.com/openbao/openbao |
| License | MPL-2.0 |
| Phiên bản đã đọc | `a238d70d33f18716daecf08ce6b52f789e7d20f4` (commit 2026-11-23) |
| Kiểm chứng | 2026-11-23; code-read; đã đọc README.md, LICENSE, AGENTS.md, internal/builtin/logical/database/path_creds_create.go, .github/workflows/test-go.yml, .github/workflows/ci.yml; chưa chạy upstream |
| Khoảng trống lấp | Bí mật và quyền cho agent/workload: cấp thông tin xác thực ngắn hạn có thu hồi, thay vì để khóa dài hạn trong repo hay prompt |
| Cơ chế đáng học | - Secrets engine trong `internal/builtin/logical`: database, kubernetes, kv, pki, ssh, totp, transit, rabbitmq; auth trong `internal/builtin/credential`: approle, cert, jwt, kubernetes, token, userpass.<br>- `logical/database/path_creds_create.go`: tạo user DB động, tính TTL bằng `CalculateTTL` từ `DefaultTTL`/`MaxTTL` của role, ghi `revocation_statements` vào secret để thu hồi khi hết lease.<br>- Audit device ghi nhật ký có băm giá trị nhạy cảm (`internal/audit`).<br>- Có agent/proxy trong `internal/command/agent` để workload lấy token tự động. |
| Tiêu chí và cách kiểm | Kiểm bằng máy: test-go.yml (đã đọc) chạy test Go chia nhiều runner, có binary test; ci.yml đã mở. Changelog theo từng PR (hơn 500 mục) và CodeQL, Scorecard có workflow (chỉ thấy tên). |
| Giới hạn và rủi ro | MPL-2.0 (copyleft theo file, LICENSE ghi Copyright 2015 HashiCorp). Chỉ thấy lựa chọn telemetry là cấu hình metrics của listener (`UnauthenticatedMetricsAccess`), chưa thấy dữ liệu gửi ra ngoài. Vận hành phức tạp, thay thế Vault cần kiểm tương thích. Chính sách AGENTS.md cấm đóng góp AI và yêu cầu dấu hiệu riêng trong PR, cần lưu ý nếu muốn đóng góp ngược. |
| So với | Infisical (infisical, secret manager nhẹ hơn), SOPS (getsops-sops, mã hóa file thay vì dịch vụ), Vaultwarden (quản lý mật khẩu, khác phạm vi) |
| Nguồn | [README.md](https://github.com/openbao/openbao/blob/a238d70d33f18716daecf08ce6b52f789e7d20f4/README.md) · [LICENSE](https://github.com/openbao/openbao/blob/a238d70d33f18716daecf08ce6b52f789e7d20f4/LICENSE) · [AGENTS.md](https://github.com/openbao/openbao/blob/a238d70d33f18716daecf08ce6b52f789e7d20f4/AGENTS.md) · [path_creds_create.go](https://github.com/openbao/openbao/blob/a238d70d33f18716daecf08ce6b52f789e7d20f4/internal/builtin/logical/database/path_creds_create.go) · [test-go.yml](https://github.com/openbao/openbao/blob/a238d70d33f18716daecf08ce6b52f789e7d20f4/.github/workflows/test-go.yml) · [ci.yml](https://github.com/openbao/openbao/blob/a238d70d33f18716daecf08ce6b52f789e7d20f4/.github/workflows/ci.yml) |

<a id="nt-thunderid"></a>

### ThunderID

| Thuộc tính | Giá trị |
|---|---|
| Repo | https://github.com/thunder-id/thunderid |
| License | Apache-2.0 |
| Phiên bản đã đọc | `e6c45f03135b4fcb6985b076dd7dbf5ef7d0ec2d` (commit 2026-11-23) |
| Kiểm chứng | 2026-11-23; code-read; đã đọc LICENSE, README.md, backend/internal/agent/delegation.go, backend/internal/agent/constants.go, backend/internal/system/mcp/auth/token_verifier.go; chưa chạy upstream |
| Khoảng trống lấp | Agent định danh/ủy quyền: danh tính và grant OAuth riêng cho agent, MCP được bảo vệ bằng token |
| Cơ chế đáng học | - `backend/internal/agent/delegation.go`: `resolveGrantTypes` luôn cấp client_credentials cho agent (trừ public client); agent `delegated` phải có ít nhất một grant trong danh sách ủy quyền (authorization_code, CIBA, device_code, token_exchange, jwt_bearer), nếu không thì báo lỗi `ErrorMissingDelegationGrantType`; nếu chỉ có client_credentials thì tự thêm authorization_code + refresh_token, bật PKCE.<br>- Agent loại personal assistant bị giới hạn chỉ grant cá nhân và không bao giờ có client_credentials, nên không tự hành động bằng quyền riêng (`resolvePersonalAssistantGrantTypes`).<br>- `backend/internal/system/mcp/auth/token_verifier.go`: máy chủ MCP của ThunderID xác thực bearer bằng cùng `BearerAuthenticator` và logic thu hồi token của REST API, đưa SecurityContext vào `TokenInfo.Extra`.<br>- Tài liệu use-case hướng dẫn gắn scope theo công cụ MCP (ví dụ `booking:*`), người dùng thiếu role thì chỉ gọi được công cụ duyệt. |
| Tiêu chí và cách kiểm | CI có workflow `oidc-conformance-test.yml` (đã mở) chạy hằng ngày bộ conformance của OpenID Foundation, profile basic gồm 35 module có trình duyệt theo `plan-config.json`; kiểm bằng máy nhưng là kết quả của upstream, chưa chạy lại. Có test Go cho agent và MCP (`*_test.go`); không đo độ phủ ở đây. |
| Giới hạn và rủi ro | Apache-2.0 (LICENSE đã đọc). Telemetry: có bộ OpenTelemetry nhưng chỉ bật khi cấu hình `enabled` (provider.go, chỉ grep, chưa đọc kỹ). Cần vận hành CSDL, khóa và control plane riêng. Tuyên bố hậu lượng tử, VC/DID, OpenID4VCI/VP chỉ là tuyên bố trong README **(chưa xác minh)**. Repo lớn (khoảng 290 MB clone), nhiều gói, nên mang cơ chế sang dự án khác cần chọn đúng module. |
| So với | keycloak, casdoor, hydra, goauthentik-authentik (IAM tổng quát, chưa coi agent là danh tính hạng nhất); spire (danh tính workload) |
| Nguồn | [LICENSE](https://github.com/thunder-id/thunderid/blob/e6c45f03135b4fcb6985b076dd7dbf5ef7d0ec2d/LICENSE) · [README.md](https://github.com/thunder-id/thunderid/blob/e6c45f03135b4fcb6985b076dd7dbf5ef7d0ec2d/README.md) · [backend/internal/agent/delegation.go](https://github.com/thunder-id/thunderid/blob/e6c45f03135b4fcb6985b076dd7dbf5ef7d0ec2d/backend/internal/agent/delegation.go) · [backend/internal/agent/constants.go](https://github.com/thunder-id/thunderid/blob/e6c45f03135b4fcb6985b076dd7dbf5ef7d0ec2d/backend/internal/agent/constants.go) · [backend/internal/system/mcp/auth/token_verifier.go](https://github.com/thunder-id/thunderid/blob/e6c45f03135b4fcb6985b076dd7dbf5ef7d0ec2d/backend/internal/system/mcp/auth/token_verifier.go) · [backend/internal/system/mcp/tool/model.go](https://github.com/thunder-id/thunderid/blob/e6c45f03135b4fcb6985b076dd7dbf5ef7d0ec2d/backend/internal/system/mcp/tool/model.go) · [.github/workflows/oidc-conformance-test.yml](https://github.com/thunder-id/thunderid/blob/e6c45f03135b4fcb6985b076dd7dbf5ef7d0ec2d/.github/workflows/oidc-conformance-test.yml) · [tests/oidc-conformance/plan-config.json](https://github.com/thunder-id/thunderid/blob/e6c45f03135b4fcb6985b076dd7dbf5ef7d0ec2d/tests/oidc-conformance/plan-config.json) · [docs/content/use-cases/ai-agents/mcp-authorization/try-it-out/connect-via-inspector.mdx](https://github.com/thunder-id/thunderid/blob/e6c45f03135b4fcb6985b076dd7dbf5ef7d0ec2d/docs/content/use-cases/ai-agents/mcp-authorization/try-it-out/connect-via-inspector.mdx) |
