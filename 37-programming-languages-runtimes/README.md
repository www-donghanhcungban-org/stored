# 37. Ngôn ngữ lập trình & runtime

Repo gốc của ngôn ngữ, runtime và trình quản lý phiên bản. Chọn theo chính sách phát hành/LTS, khả năng tương thích ngược và hệ sinh thái gói; số sao không phản ánh độ ổn định runtime.

Mục được lập ngày 2026-11-23 khi chia lại catalog; hồ sơ bên dưới chuyển nguyên văn từ mục cũ, neo cũ vẫn giữ một đoạn dẫn sang đây. Bảng tổng hợp theo danh mục con: [catalog/](../catalog/README.md).

<a id="chuyen-muc-2026-11-23"></a>

## Hồ sơ chuyển về từ mục khác — 23/11/2026

20 hồ sơ được chuyển khi chia lại catalog theo `data/taxonomy.json`. Nội dung, ngày kiểm và mức bằng chứng giữ nguyên như ở mục gốc.

<a id="chuyen-bun"></a>

### Bun

`oven-sh/bun` · License: MIT (+ LGPL-2 link tĩnh) · ★ 96.488

Runtime/bundler/test runner JS của Anthropic; viết lại bằng Rust (#30412, 14/5/2026), v1.4.0 19/8/2026; GitHub NOASSERTION do JavaScriptCore LGPL; ★ 31/10/2026 (GitHub API), mục 13 §6g.3

**Hồ sơ gốc:** [mục 13](../13-dev-stack-devops/README.md) (bảng/đoạn chung, giữ nguyên tại chỗ).

<a id="chuyen-go"></a>

### go

`golang/go` · License: BSD 3-Clause · ★ 140.176 · docs-read · 2026-11-18

Mã nguồn ngôn ngữ lập trình Go: trình biên dịch, bộ công cụ và thư viện chuẩn. Có bản phân phối nhị phân chính thức tại go.dev/dl; thư mục api lưu bề mặt API theo từng phiên bản (go1.txt…) để giữ tương thích; doc/next ghi thay đổi cho bản phát hành kế. Điều kiện: Kho GitHub là bản mirror, kho chính tắc ở go.googlesource.com; issue tracker chỉ dành cho báo lỗi và đề xuất. ★ 18/11/2026: 140.176 (GitHub search API), nhóm "Ngôn ngữ & Runtime" trong kho-repo của Phan Đông Giang, mục 08 §6c.5

**Hồ sơ gốc:** [mục 08](../08-awesome-lists-learning/README.md#6c514-ngôn-ngữ--runtime) (bảng/đoạn chung, giữ nguyên tại chỗ).

<a id="chuyen-node"></a>

### node

`nodejs/node` · License: MIT · ★ 123.898 · docs-read · 2026-11-18

Node.js: runtime JavaScript mã nguồn mở, đa nền tảng, xây trên V8. Quản trị mở dưới OpenJS Foundation; mỗi bản major nhận 30 tháng LTS, tổng 36 tháng tới hết hạn theo lịch mới; bản phát hành có SHASUMS256 ký PGP để xác minh. Điều kiện: Bản Alpha, Current và Nightly không dành cho production; nên dùng dòng LTS. ★ 18/11/2026: 123.898 (GitHub search API), nhóm "Ngôn ngữ & Runtime" trong kho-repo của Phan Đông Giang, mục 08 §6c.5

**Hồ sơ gốc:** [mục 08](../08-awesome-lists-learning/README.md#6c514-ngôn-ngữ--runtime) (bảng/đoạn chung, giữ nguyên tại chỗ).

<a id="chuyen-rust"></a>

### rust

`rust-lang/rust` · License: Kép MIT hoặc Apache License 2.0 · ★ 122.313 · docs-read · 2026-11-18

Kho mã chính của ngôn ngữ Rust: trình biên dịch, thư viện chuẩn và tài liệu. Hệ thống kiểu và mô hình ownership bảo đảm an toàn bộ nhớ và luồng lúc biên dịch; theo dõi giấy phép bằng REUSE (REUSE.toml, license-metadata.json); hệ công cụ đi kèm gồm Cargo, rustfmt, Clippy, rust-analyzer. Điều kiện: Tên và logo Rust/Cargo là nhãn hiệu của Rust Foundation, dùng phải theo chính sách nhãn hiệu; README khuyên không cài từ mã nguồn. ★ 18/11/2026: 122.313 (GitHub search API), nhóm "Ngôn ngữ & Runtime" trong kho-repo của Phan Đông Giang, mục 08 §6c.5

**Hồ sơ gốc:** [mục 08](../08-awesome-lists-learning/README.md#6c514-ngôn-ngữ--runtime) (bảng/đoạn chung, giữ nguyên tại chỗ).

<a id="chuyen-typescript"></a>

### TypeScript

`microsoft/TypeScript` · License: Apache License 2.0 · ★ 111.839 · docs-read · 2026-11-18

Ngôn ngữ TypeScript: thêm kiểu tuỳ chọn cho JavaScript và biên dịch ra JavaScript chuẩn; kho hiện chứa trình biên dịch và language server viết bằng Go (thư mục tsc), gói npm và extension VS Code. Trình biên dịch và language server phát triển bằng Go trong tsc/internal (go.work); có gói npm typescript, gói typescript-wasip1-wasm và extension VS Code trong packages; tsc/CHANGES.md ghi rõ khác biệt có chủ đích giữa trình biên dịch cũ (Strada) và mới (Corsa). ★ 18/11/2026: 111.839 (GitHub search API), nhóm "Ngôn ngữ & Runtime" trong kho-repo của Phan Đông Giang, mục 08 §6c.5

**Hồ sơ gốc:** [mục 08](../08-awesome-lists-learning/README.md#6c514-ngôn-ngữ--runtime) (bảng/đoạn chung, giữ nguyên tại chỗ).

<a id="chuyen-deno"></a>

### deno

`denoland/deno` · License: MIT · ★ 109.037 · docs-read · 2026-11-18

Deno: runtime JavaScript, TypeScript và WebAssembly mặc định an toàn, xây trên V8, Rust và Tokio. Quyền truy cập phải cấp rõ (ví dụ --allow-net); cài qua script, Homebrew, Chocolatey, WinGet, Scoop; có thư viện chuẩn trên JSR. ★ 18/11/2026: 109.037 (GitHub search API), nhóm "Ngôn ngữ & Runtime" trong kho-repo của Phan Đông Giang, mục 08 §6c.5

**Hồ sơ gốc:** [mục 08](../08-awesome-lists-learning/README.md#6c514-ngôn-ngữ--runtime) (bảng/đoạn chung, giữ nguyên tại chỗ).

<a id="chuyen-nvm"></a>

### nvm

`nvm-sh/nvm` · License: MIT · ★ 96.242 · docs-read · 2026-11-18

Node Version Manager: công cụ quản lý nhiều phiên bản Node.js, cài theo từng người dùng và gọi trong từng shell. Chạy trên mọi shell POSIX (sh, dash, ksh, zsh, bash) ở unix, macOS và WSL; có hướng dẫn cài trong Docker cho CI; có thư mục test và GOVERNANCE/PROJECT_CHARTER. Điều kiện: Không hỗ trợ Windows gốc (chỉ WSL, Git Bash, Cygwin), không hỗ trợ Fish, không hỗ trợ cài qua Homebrew. ★ 18/11/2026: 96.242 (GitHub search API), nhóm "Ngôn ngữ & Runtime" trong kho-repo của Phan Đông Giang, mục 08 §6c.5

**Hồ sơ gốc:** [mục 08](../08-awesome-lists-learning/README.md#6c514-ngôn-ngữ--runtime) (bảng/đoạn chung, giữ nguyên tại chỗ).

<a id="chuyen-cpython"></a>

### cpython

`python/cpython` · License: PSF License Agreement · ★ 78.497 · docs-read · 2026-11-18

Mã nguồn chính thức của trình thông dịch Python (CPython) cùng thư viện chuẩn và tài liệu; nhánh main đang ở Python 3.16.0 alpha 2+dev. Hướng dẫn build cho Unix, Linux, BSD, macOS, Cygwin và Windows (PCbuild); hỗ trợ build tối ưu PGO/LTO qua --enable-optimizations; CI trên GitHub Actions và Azure Pipelines. Điều kiện: Nhánh main là bản phát triển (3.16 alpha); bản cài sẵn lấy từ python.org. ★ 18/11/2026: 78.497 (GitHub search API), nhóm "Ngôn ngữ & Runtime" trong kho-repo của Phan Đông Giang, mục 08 §6c.5

**Hồ sơ gốc:** [mục 08](../08-awesome-lists-learning/README.md#6c514-ngôn-ngữ--runtime) (bảng/đoạn chung, giữ nguyên tại chỗ).

<a id="chuyen-swift"></a>

### swift

`swiftlang/swift` · License: Apache License 2.0 kèm Runtime Library Exception · ★ 70.565 · docs-read · 2026-11-18

Mã nguồn trình biên dịch, thư viện chuẩn và runtime của ngôn ngữ lập trình Swift. Ngôn ngữ hệ thống hiệu năng cao, an toàn bộ nhớ mặc định và gọi trực tiếp mã C/Objective-C; có script utils/build-toolchain dựng toolchain giống CI của swift.org; tài liệu nội bộ trong docs/ kèm hướng dẫn PR đầu tiên và FAQ. Điều kiện: Build từ nguồn cần môi trường theo Getting Started guide; bản dựng sẵn lấy từ swift.org. ★ 18/11/2026: 70.565 (GitHub search API), nhóm "Ngôn ngữ & Runtime" trong kho-repo của Phan Đông Giang, mục 08 §6c.5

**Hồ sơ gốc:** [mục 08](../08-awesome-lists-learning/README.md#6c514-ngôn-ngữ--runtime) (bảng/đoạn chung, giữ nguyên tại chỗ).

<a id="anhkysuai-julialang-julia"></a>

### Julia

- **Repo:** [JuliaLang/julia](https://github.com/JuliaLang/julia).
- **Mục đích:** Ngôn ngữ động dành cho tính toán kỹ thuật và khoa học.
- **Điểm đáng dùng:** README chỉ rõ source runtime, tài liệu, hệ package và cách quản lý nhiều phiên bản bằng juliaup; có ích khi xây công cụ số trong môi trường thống nhất.
- **License:** MIT; phụ thuộc có giấy phép riêng.
- **Giới hạn:** Chưa chạy benchmark hoặc package khoa học; hiệu năng phụ thuộc compile, kiểu dữ liệu và workload. Binary không chính thức có thể không được dự án hỗ trợ.
- **Tích hợp:** Dùng Julia/juliaup chính thức, ghi Project/Manifest và phiên bản runtime cho khả năng tái lập.
- **Đối chiếu:** Python với NumPy cho hệ sinh thái; R cho thống kê; MATLAB cho môi trường thương mại kỹ thuật.
- **Mức kiểm chứng:** `docs-read` — Đọc các phần mô tả và giới hạn trong README, thông báo license, metadata manifest và cấu hình CI khi có; chưa đọc toàn bộ mã triển khai, chưa cài hoặc chạy kiểm thử upstream.
- **Snapshot:** kiểm ngày 2026-11-23; commit `562474cbd28258fdf04731b001ece9f4cd2f6171` (2026-11-23T10:21:25+01:00); 49,293 sao theo GitHub API ngày 2026-11-23. Sao không đại diện chất lượng.
- **Bằng chứng:** [README.md](https://github.com/JuliaLang/julia/blob/562474cbd28258fdf04731b001ece9f4cd2f6171/README.md) · [LICENSE.md](https://github.com/JuliaLang/julia/blob/562474cbd28258fdf04731b001ece9f4cd2f6171/LICENSE.md) · [.github/workflows/LabelCheck.yml](https://github.com/JuliaLang/julia/blob/562474cbd28258fdf04731b001ece9f4cd2f6171/.github/workflows/LabelCheck.yml) · [GitHub API](https://api.github.com/repos/JuliaLang/julia).

<a id="anhkysuai-vlang-v"></a>

### V

- **Repo:** [vlang/v](https://github.com/vlang/v).
- **Mục đích:** Ngôn ngữ và compiler hướng cú pháp gọn, backend C/JavaScript.
- **Điểm đáng dùng:** README liệt kê GC mặc định cùng chế độ memory khác và hot reload; workflow đọc có kiểm thử driver cơ sở dữ liệu.
- **License:** MIT.
- **Giới hạn:** Trước 1.0 vẫn đổi API/cú pháp và mục tiêu không undefined behavior còn WIP; tốc độ cùng an toàn là tuyên bố chưa được kiểm chứng ở đây.
- **Tích hợp:** Thử công cụ nhỏ ít rủi ro, khóa compiler và kiểm tra C interop, memory trước khi chuẩn hóa template.
- **Đối chiếu:** [Go](../08-awesome-lists-learning/README.md#6c514-ngôn-ngữ--runtime) cho tooling; [Rust](../08-awesome-lists-learning/README.md#6c514-ngôn-ngữ--runtime) cho kiểm soát bộ nhớ; Zig cho hệ thống và C interop.
- **Mức kiểm chứng:** `docs-read` — Đọc các phần mô tả và giới hạn trong README, thông báo license, metadata manifest và cấu hình CI khi có; chưa đọc toàn bộ mã triển khai, chưa cài hoặc chạy kiểm thử upstream.
- **Snapshot:** kiểm ngày 2026-11-23; commit `827f160f069e5272a36a57a4f5ff5ae0e45cceb6` (2026-11-23T08:50:41+03:00); 38,124 sao theo GitHub API ngày 2026-11-23. Sao không đại diện chất lượng.
- **Bằng chứng:** [README.md](https://github.com/vlang/v/blob/827f160f069e5272a36a57a4f5ff5ae0e45cceb6/README.md) · [LICENSE](https://github.com/vlang/v/blob/827f160f069e5272a36a57a4f5ff5ae0e45cceb6/LICENSE) · [.github/workflows/db_ci.yml](https://github.com/vlang/v/blob/827f160f069e5272a36a57a4f5ff5ae0e45cceb6/.github/workflows/db_ci.yml) · [GitHub API](https://api.github.com/repos/vlang/v).

<a id="anhkysuai-carbon-language-carbon-lang"></a>

### Carbon Language

- **Repo:** [carbon-language/carbon-lang](https://github.com/carbon-language/carbon-lang).
- **Mục đích:** Nghiên cứu ngôn ngữ kế nhiệm C++ với hướng tương tác hai chiều.
- **Điểm đáng dùng:** README nêu mục tiêu LLVM, C++ interop và migration công cụ; CI có cấu hình tối ưu và AddressSanitizer.
- **License:** Apache-2.0 WITH LLVM-exception.
- **Giới hạn:** Tài liệu ghi rõ experimental và chưa sẵn sàng sử dụng; mục tiêu an toàn bộ nhớ/hiệu năng không phải bảo đảm hiện trạng.
- **Tích hợp:** Lưu để theo dõi compiler và thử ví dụ riêng, chưa dùng làm chuẩn ngôn ngữ cho sản phẩm đang giao.
- **Đối chiếu:** [Rust](../08-awesome-lists-learning/README.md#6c514-ngôn-ngữ--runtime) cho ngôn ngữ hệ thống; Zig cho C interop; C++ cho codebase hiện hữu.
- **Mức kiểm chứng:** `docs-read` — Đọc các phần mô tả và giới hạn trong README, thông báo license, metadata manifest và cấu hình CI khi có; chưa đọc toàn bộ mã triển khai, chưa cài hoặc chạy kiểm thử upstream.
- **Snapshot:** kiểm ngày 2026-11-23; commit `0072b2812979e4a75b3467f0fd0ac086eee209a4` (2026-11-22T05:19:35Z); 33,969 sao theo GitHub API ngày 2026-11-23. Sao không đại diện chất lượng.
- **Bằng chứng:** [README.md](https://github.com/carbon-language/carbon-lang/blob/0072b2812979e4a75b3467f0fd0ac086eee209a4/README.md) · [LICENSE](https://github.com/carbon-language/carbon-lang/blob/0072b2812979e4a75b3467f0fd0ac086eee209a4/LICENSE) · [pyproject.toml](https://github.com/carbon-language/carbon-lang/blob/0072b2812979e4a75b3467f0fd0ac086eee209a4/pyproject.toml) · [.github/workflows/tests.yaml](https://github.com/carbon-language/carbon-lang/blob/0072b2812979e4a75b3467f0fd0ac086eee209a4/.github/workflows/tests.yaml) · [GitHub API](https://api.github.com/repos/carbon-language/carbon-lang).

<a id="anhkysuai-bendlang-bend"></a>

### Bend

- **Repo:** [bendlang/bend](https://github.com/bendlang/bend).
- **Mục đích:** Ngôn ngữ hướng tính toán song song và khai báo luật kèm chứng minh.
- **Điểm đáng dùng:** README tại SHA giới thiệu LAWS.bend để ràng buộc thay đổi, cùng purity/linearity và compiler CPU/GPU; workflow có repo gate.
- **License:** Apache-2.0.
- **Giới hạn:** Đánh giá này chưa kiểm tra compiler hoặc tái hiện claim tốc độ/chứng minh; luật đúng hình thức không bảo đảm đặc tả đầy đủ hay toàn hệ thống không có lỗi.
- **Tích hợp:** Lưu làm hướng nghiên cứu formal specification, thử bài toán nhỏ có oracle độc lập trước khi xét cho sản phẩm.
- **Đối chiếu:** Lean cho chứng minh; Dafny cho verification chương trình; [Rust](../08-awesome-lists-learning/README.md#6c514-ngôn-ngữ--runtime) cho ngôn ngữ hệ thống.
- **Mức kiểm chứng:** `docs-read` — Đọc các phần mô tả và giới hạn trong README, thông báo license, metadata manifest và cấu hình CI khi có; chưa đọc toàn bộ mã triển khai, chưa cài hoặc chạy kiểm thử upstream.
- **Snapshot:** kiểm ngày 2026-11-23; commit `6b806192284fc9c64404d9b0b59c937f568d87ec` (2026-11-23T06:50:12-03:00); 25,792 sao theo GitHub API ngày 2026-11-23. Sao không đại diện chất lượng.
- **Bằng chứng:** [README.md](https://github.com/bendlang/bend/blob/6b806192284fc9c64404d9b0b59c937f568d87ec/README.md) · [LICENSE](https://github.com/bendlang/bend/blob/6b806192284fc9c64404d9b0b59c937f568d87ec/LICENSE) · [.github/workflows/repo-gate.yml](https://github.com/bendlang/bend/blob/6b806192284fc9c64404d9b0b59c937f568d87ec/.github/workflows/repo-gate.yml) · [GitHub API](https://api.github.com/repos/bendlang/bend).

<a id="anhkysuai-v8-v8"></a>

### V8

- **Repo:** [v8/v8](https://github.com/v8/v8).
- **Mục đích:** Engine JavaScript C++ dùng độc lập hoặc nhúng trong ứng dụng.
- **Điểm đáng dùng:** README mô tả triển khai ECMAScript và quy trình depot_tools/gclient để lấy dependency; LICENSE phân biệt lõi với thư viện ngoại vi.
- **License:** BSD-3-Clause cho lõi; thư viện ngoài và test có license riêng.
- **Giới hạn:** Clone repo riêng chưa tạo toolchain build hoàn chỉnh; nhúng mã không tin cậy cần mô hình giới hạn tài nguyên/host API, không xem engine là sandbox đủ mặc định.
- **Tích hợp:** Chỉ cân nhắc khi cần nhúng runtime C++, khóa dependency và thiết kế lifecycle/isolation cùng cập nhật an ninh.
- **Đối chiếu:** QuickJS cho engine nhỏ; JavaScriptCore cho nền WebKit; [Node.js](../08-awesome-lists-learning/README.md#6c514-ngôn-ngữ--runtime) cho runtime sẵn.
- **Mức kiểm chứng:** `docs-read` — Đọc các phần mô tả và giới hạn trong README, thông báo license, metadata manifest và cấu hình CI khi có; chưa đọc toàn bộ mã triển khai, chưa cài hoặc chạy kiểm thử upstream.
- **Snapshot:** kiểm ngày 2026-11-23; commit `49f0798037cdd08460664363947a92bcb65f7957` (2026-11-23T01:49:19-08:00); 25,346 sao theo GitHub API ngày 2026-11-23. Sao không đại diện chất lượng.
- **Bằng chứng:** [README.md](https://github.com/v8/v8/blob/49f0798037cdd08460664363947a92bcb65f7957/README.md) · [LICENSE](https://github.com/v8/v8/blob/49f0798037cdd08460664363947a92bcb65f7957/LICENSE) · [LICENSE.fdlibm](https://github.com/v8/v8/blob/49f0798037cdd08460664363947a92bcb65f7957/LICENSE.fdlibm) · [LICENSE.strongtalk](https://github.com/v8/v8/blob/49f0798037cdd08460664363947a92bcb65f7957/LICENSE.strongtalk) · [GitHub API](https://api.github.com/repos/v8/v8).

<a id="anhkysuai-ruby-ruby"></a>

### Ruby

**Repo:** [ruby/ruby](https://github.com/ruby/ruby) · **License:** Ruby License OR BSD-2-Clause; thành phần trong LEGAL có điều khoản riêng · **Kiểm:** 2026-11-23, `docs-read`, [`0b4e7e04e318`](https://github.com/ruby/ruby/tree/0b4e7e04e3187be7fef6389b1518b357860e8802) (commit 2026-11-23). **Sao:** 23,859 tại 2026-11-23 theo [GitHub API](https://api.github.com/repos/ruby/ruby).

| Mục | Đánh giá |
|---|---|
| Mục đích | Mã nguồn ngôn ngữ Ruby thông dịch, hướng đối tượng, dùng cho web và scripting. |
| Giá trị và cơ chế theo tài liệu | README nêu mixin, closure, GC và portability; COPYING cho lựa chọn BSDL hai điều khoản hoặc Ruby License, Cargo chứa phần Rust liên kết vào runtime. |
| Giới hạn | Repo là runtime, không đại diện Rails hoặc toàn bộ gem. Một số file có điều khoản trong LEGAL; chưa build interpreter, chạy RubySpec hay đo JIT/GC. |
| Điều kiện tích hợp | Chọn release còn hỗ trợ và toolchain của hệ đích, ghim gem/native extension; thử tương thích ứng dụng và benchmark workload trước nâng runtime. |
| Lựa chọn đối chiếu | [Python](../08-awesome-lists-learning/README.md#6c521-thuật-toán--phỏng-vấn); [Crystal](../13-dev-stack-devops/README.md#anhkysuai-crystal-lang-crystal); JRuby. |

**Phạm vi bằng chứng:** đã clone, đọc trích đoạn tài liệu, giấy phép và các file cấu hình được dẫn dưới đây; chưa chạy mã, build, benchmark hoặc test upstream. `docs-read` không phải kiểm chứng implementation.

**Nguồn tại cùng SHA:** [README.md](https://github.com/ruby/ruby/blob/0b4e7e04e3187be7fef6389b1518b357860e8802/README.md) · [COPYING](https://github.com/ruby/ruby/blob/0b4e7e04e3187be7fef6389b1518b357860e8802/COPYING) · [COPYING.ja](https://github.com/ruby/ruby/blob/0b4e7e04e3187be7fef6389b1518b357860e8802/COPYING.ja) · [Cargo.toml](https://github.com/ruby/ruby/blob/0b4e7e04e3187be7fef6389b1518b357860e8802/Cargo.toml) · [.github/workflows/annocheck.yml](https://github.com/ruby/ruby/blob/0b4e7e04e3187be7fef6389b1518b357860e8802/.github/workflows/annocheck.yml).

<a id="anhkysuai-rustpython-rustpython"></a>

### RustPython

**Repo:** [RustPython/RustPython](https://github.com/RustPython/RustPython) · **License:** MIT cho interpreter; CC-BY-4.0 cho logo · **Kiểm:** 2026-11-23, `docs-read`, [`ad3268e88a10`](https://github.com/RustPython/RustPython/tree/ad3268e88a10e6cb9b92cec53263acf023eeead4) (commit 2026-11-22). **Sao:** 22,503 tại 2026-11-23 theo [GitHub API](https://api.github.com/repos/RustPython/RustPython).

| Mục | Đánh giá |
|---|---|
| Mục đích | Trình thông dịch Python viết bằng Rust, hướng đến nhúng scripting vào ứng dụng Rust và chạy trong WebAssembly. |
| Giá trị và cơ chế theo tài liệu | README chỉ ra ví dụ embedding, WASI và các lựa chọn SSL; Cargo workspace tách feature cho stdlib, threading, host environment và nhà cung cấp TLS. Hữu ích để thử scripting trong sản phẩm Rust. |
| Giới hạn | README nói rõ chưa hoàn toàn sẵn sàng production; dòng tương thích CPython không chứng minh mọi package hoặc extension hoạt động. Logo có giấy phép riêng, thư viện được mang vào cần kiểm theo thành phần. |
| Điều kiện tích hợp | Lập danh sách cú pháp, module và extension cần dùng; thử cùng workload thực tế, giới hạn quyền host và tài nguyên nếu nhận script không tin cậy. Chưa chạy bộ tương thích hoặc kiểm sandbox. |
| Lựa chọn đối chiếu | [CPython](../08-awesome-lists-learning/README.md#6c514-ngôn-ngữ--runtime); PyO3; [MicroPython](../13-dev-stack-devops/README.md#anhkysuai-micropython-micropython). |

**Phạm vi bằng chứng:** đã clone, đọc trích đoạn tài liệu, giấy phép và các file cấu hình được dẫn dưới đây; chưa chạy mã, build, benchmark hoặc test upstream. `docs-read` không phải kiểm chứng implementation.

**Nguồn tại cùng SHA:** [README.md](https://github.com/RustPython/RustPython/blob/ad3268e88a10e6cb9b92cec53263acf023eeead4/README.md) · [LICENSE](https://github.com/RustPython/RustPython/blob/ad3268e88a10e6cb9b92cec53263acf023eeead4/LICENSE) · [LICENSE-logo](https://github.com/RustPython/RustPython/blob/ad3268e88a10e6cb9b92cec53263acf023eeead4/LICENSE-logo) · [Cargo.toml](https://github.com/RustPython/RustPython/blob/ad3268e88a10e6cb9b92cec53263acf023eeead4/Cargo.toml) · [.github/workflows/ci.yaml](https://github.com/RustPython/RustPython/blob/ad3268e88a10e6cb9b92cec53263acf023eeead4/.github/workflows/ci.yaml).

<a id="anhkysuai-micropython-micropython"></a>

### MicroPython

**Repo:** [micropython/micropython](https://github.com/micropython/micropython) · **License:** MIT cho lõi; các port và thư viện kèm có giấy phép riêng · **Kiểm:** 2026-11-23, `docs-read`, [`1c8e39768802`](https://github.com/micropython/micropython/tree/1c8e39768802b47f80e91924a00cc9bbd6ce7bf5) (commit 2026-11-21). **Sao:** 22,222 tại 2026-11-23 theo [GitHub API](https://api.github.com/repos/micropython/micropython).

| Mục | Đánh giá |
|---|---|
| Mục đích | Triển khai Python cho vi điều khiển và môi trường hạn chế tài nguyên, có API truy cập ngoại vi phần cứng. |
| Giá trị và cơ chế theo tài liệu | README mô tả script .py, bytecode .mpy hoặc mã frozen, cùng GPIO, SPI, I2C, Bluetooth và USB theo port. LICENSE lập bảng phạm vi thư viện, SDK và công cụ đi kèm. |
| Giới hạn | Chỉ hỗ trợ một phần Python 3 và module; tính năng thread, mạng, SSL phụ thuộc port. Giấy phép SDK, btstack và một số thành phần khác cần kiểm riêng; không suy toàn bộ firmware chỉ MIT. |
| Điều kiện tích hợp | Chọn board/port trước, đo RAM, heap và độ trễ với tác vụ thật; xác minh driver, cập nhật firmware và quyền phân phối toàn bộ thành phần được đưa vào bản build. |
| Lựa chọn đối chiếu | CircuitPython; [RustPython](../13-dev-stack-devops/README.md#anhkysuai-rustpython-rustpython); Lua. |

**Phạm vi bằng chứng:** đã clone, đọc trích đoạn tài liệu, giấy phép và các file cấu hình được dẫn dưới đây; chưa chạy mã, build, benchmark hoặc test upstream. `docs-read` không phải kiểm chứng implementation.

**Nguồn tại cùng SHA:** [README.md](https://github.com/micropython/micropython/blob/1c8e39768802b47f80e91924a00cc9bbd6ce7bf5/README.md) · [LICENSE](https://github.com/micropython/micropython/blob/1c8e39768802b47f80e91924a00cc9bbd6ce7bf5/LICENSE) · [pyproject.toml](https://github.com/micropython/micropython/blob/1c8e39768802b47f80e91924a00cc9bbd6ce7bf5/pyproject.toml) · [.github/workflows/docs.yml](https://github.com/micropython/micropython/blob/1c8e39768802b47f80e91924a00cc9bbd6ce7bf5/.github/workflows/docs.yml).

<a id="anhkysuai-gleam-lang-gleam"></a>

### Gleam

**Repo:** [gleam-lang/gleam](https://github.com/gleam-lang/gleam) · **License:** Apache-2.0 · **Kiểm:** 2026-11-23, `docs-read`, [`05fb252bf83e`](https://github.com/gleam-lang/gleam/tree/05fb252bf83e5a29cb73ca0f926e50bd37e7e815) (commit 2026-11-21). **Sao:** 22,083 tại 2026-11-23 theo [GitHub API](https://api.github.com/repos/gleam-lang/gleam).

| Mục | Đánh giá |
|---|---|
| Mục đích | Ngôn ngữ có kiểm kiểu tĩnh, compiler viết bằng Rust sinh mã Erlang hoặc JavaScript. |
| Giá trị và cơ chế theo tài liệu | Tài liệu compiler mô tả parser, sắp xếp dependency, type checker, code generation và cache metadata; tách core không IO, CLI, language server và giao diện WASM. Có hướng dẫn integration và snapshot test. |
| Giới hạn | Đây là đánh giá cấu trúc tài liệu, chưa xác minh compiler hay độ tương thích thư viện. Lựa chọn target ảnh hưởng runtime và thư viện có thể dùng; lợi ích quy mô trong README chưa có benchmark độc lập. |
| Điều kiện tích hợp | Thử một dịch vụ hoặc thư viện nhỏ với target cụ thể; kiểm FFI, xử lý lỗi, gói Hex/npm và pipeline build/deploy trước mở rộng sang hệ thống chính. |
| Lựa chọn đối chiếu | Elixir; Erlang; [TypeScript](../08-awesome-lists-learning/README.md#6c514-ngôn-ngữ--runtime). |

**Phạm vi bằng chứng:** đã clone, đọc trích đoạn tài liệu, giấy phép và các file cấu hình được dẫn dưới đây; chưa chạy mã, build, benchmark hoặc test upstream. `docs-read` không phải kiểm chứng implementation.

**Nguồn tại cùng SHA:** [README.md](https://github.com/gleam-lang/gleam/blob/05fb252bf83e5a29cb73ca0f926e50bd37e7e815/README.md) · [LICENCE](https://github.com/gleam-lang/gleam/blob/05fb252bf83e5a29cb73ca0f926e50bd37e7e815/LICENCE) · [Cargo.toml](https://github.com/gleam-lang/gleam/blob/05fb252bf83e5a29cb73ca0f926e50bd37e7e815/Cargo.toml) · [.github/workflows/ci.yaml](https://github.com/gleam-lang/gleam/blob/05fb252bf83e5a29cb73ca0f926e50bd37e7e815/.github/workflows/ci.yaml) · [docs/compiler/README.md](https://github.com/gleam-lang/gleam/blob/05fb252bf83e5a29cb73ca0f926e50bd37e7e815/docs/compiler/README.md).

<a id="anhkysuai-oracle-graal"></a>

### GraalVM Community Edition

**Repo:** [oracle/graal](https://github.com/oracle/graal) · **License:** GPL-2.0 với Classpath Exception cho bản CE; thành phần GPL-2.0, UPL và BSD riêng · **Kiểm:** 2026-11-23, `docs-read`, [`0e2ec13d8816`](https://github.com/oracle/graal/tree/0e2ec13d8816476a7de70991cc4af28d5f6b8ec9) (commit 2026-11-23). **Sao:** 21,757 tại 2026-11-23 theo [GitHub API](https://api.github.com/repos/oracle/graal).

| Mục | Đánh giá |
|---|---|
| Mục đích | Bộ compiler và runtime hỗ trợ Java cùng biên dịch ahead-of-time thành chương trình native. |
| Giá trị và cơ chế theo tài liệu | README lập bản đồ compiler, SubstrateVM, Truffle, SDK, Sulong và GraalWasm; workflow có build GraalVM. Có thể khảo sát cho dịch vụ cần thời gian khởi động hoặc bộ nhớ khác JVM thông thường. |
| Giới hạn | Tuyên bố startup và tài nguyên của upstream chưa được benchmark tại đây. License theo từng thành phần; GraalJS/GraalPy nằm ở repo khác, không suy mọi bản phân phối mang cùng điều khoản với CE. |
| Điều kiện tích hợp | Chọn distribution/JDK cụ thể, kiểm metadata cho reflection, tài nguyên và thư viện native; đo build time, startup và tải dài hạn bằng ứng dụng thật trước đổi runtime. |
| Lựa chọn đối chiếu | OpenJDK; Eclipse OpenJ9; Quarkus. |

**Phạm vi bằng chứng:** đã clone, đọc trích đoạn tài liệu, giấy phép và các file cấu hình được dẫn dưới đây; chưa chạy mã, build, benchmark hoặc test upstream. `docs-read` không phải kiểm chứng implementation.

**Nguồn tại cùng SHA:** [README.md](https://github.com/oracle/graal/blob/0e2ec13d8816476a7de70991cc4af28d5f6b8ec9/README.md) · [LICENSE](https://github.com/oracle/graal/blob/0e2ec13d8816476a7de70991cc4af28d5f6b8ec9/LICENSE) · [pyproject.toml](https://github.com/oracle/graal/blob/0e2ec13d8816476a7de70991cc4af28d5f6b8ec9/pyproject.toml) · [.github/workflows/build-graalvm.yml](https://github.com/oracle/graal/blob/0e2ec13d8816476a7de70991cc4af28d5f6b8ec9/.github/workflows/build-graalvm.yml).

<a id="anhkysuai-crystal-lang-crystal"></a>

### Crystal

**Repo:** [crystal-lang/crystal](https://github.com/crystal-lang/crystal) · **License:** Apache-2.0 với ngoại lệ attribution cho phần compiler nhúng vào binary đầu ra · **Kiểm:** 2026-11-23, `docs-read`, [`48118b0e8f56`](https://github.com/crystal-lang/crystal/tree/48118b0e8f564567495228e273ef6a88d563d15f) (commit 2026-11-22). **Sao:** 20,518 tại 2026-11-23 theo [GitHub API](https://api.github.com/repos/crystal-lang/crystal).

| Mục | Đánh giá |
|---|---|
| Mục đích | Ngôn ngữ biên dịch native có cú pháp gần Ruby, kiểm kiểu tĩnh và suy luận kiểu. |
| Giá trị và cơ chế theo tài liệu | README mô tả C bindings, sinh mã lúc compile và OOP; LICENSE có ngoại lệ khi compiler đưa một phần mã của nó vào chương trình đầu ra. Có giá trị khảo sát cho CLI hoặc dịch vụ muốn cú pháp ngắn. |
| Giới hạn | Tương thích Ruby không phải mục tiêu; không thể coi gem Ruby dùng trực tiếp. Chưa build compiler, đo hiệu năng hoặc kiểm hỗ trợ dependency trên từng nền tảng; workflow đọc tập trung build thư viện Windows. |
| Điều kiện tích hợp | Thử một chương trình đại diện, khóa compiler và shards, kiểm thư viện C cùng toolchain đóng gói; đo build time, tài nguyên runtime và công sức vận hành trước chuyển mã. |
| Lựa chọn đối chiếu | [Ruby](../13-dev-stack-devops/README.md#anhkysuai-ruby-ruby); [Go](../08-awesome-lists-learning/README.md#6c514-ngôn-ngữ--runtime); Nim. |

**Phạm vi bằng chứng:** đã clone, đọc trích đoạn tài liệu, giấy phép và các file cấu hình được dẫn dưới đây; chưa chạy mã, build, benchmark hoặc test upstream. `docs-read` không phải kiểm chứng implementation.

**Nguồn tại cùng SHA:** [README.md](https://github.com/crystal-lang/crystal/blob/48118b0e8f564567495228e273ef6a88d563d15f/README.md) · [LICENSE](https://github.com/crystal-lang/crystal/blob/48118b0e8f564567495228e273ef6a88d563d15f/LICENSE) · [.github/workflows/win_build_libs.yml](https://github.com/crystal-lang/crystal/blob/48118b0e8f564567495228e273ef6a88d563d15f/.github/workflows/win_build_libs.yml).
