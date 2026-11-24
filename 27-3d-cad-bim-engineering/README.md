# 27 · 3D, CAD/BIM & Engineering Agents

Mục dành cho hình học và dữ liệu kỹ thuật có thể kiểm. Ngày đọc **2026-11-02**: đọc LICENSE, README, CI, API/validator được dẫn; **chưa chạy CAD host, geometry engine hoặc corpus conformance**.

## 1. Ba miền có tiêu chí đúng khác nhau

| Miền | Biểu diễn / công cụ | Tiêu chí đầu ra |
|---|---|---|
| Render / game asset | Mesh, material, UV; Blender, glTF | Hình nhìn thấy, topology/triangle budget, UV/material, license asset |
| CAD / chế tạo | Solid B-rep, tham số, STEP; FreeCAD/OpenSCAD | Kích thước, đơn vị, dung sai, solid hợp lệ, lắp ráp/khả năng chế tạo |
| BIM / AEC | IFC entity/property/relationship; IfcOpenShell | Schema, classification, property/unit, IDS, phối hợp vấn đề qua BCF |

Mesh kín không chứng minh dung sai chế tạo; B-rep hợp lệ không chứng minh tải trọng; IFC qua schema không chứng minh đủ thông tin bàn giao. Không suy ảnh render đẹp thành kiểm chứng kỹ thuật.

Case study sẵn có: [Dhcb-Tools: Revit/AutoCAD, dryRun→confirm→snapshot](../23-own-repos-lessons/README.md#44-dhcb-tools--agent-cho-cadbim-desktop-revit--autocad) và [Blender: verify ladder, hash scene/spec](../23-own-repos-lessons/README.md#61-design-os-3d-blender--agent-điều-khiển-blender-ship-được-phần-in-3d). Các nguồn từng ghi theo docs nội bộ vẫn giữ nhãn chưa xác minh; phần dưới đọc trực tiếp upstream.

## 2. Hồ sơ nền tảng và chuẩn

### IfcOpenShell

| Thuộc tính | Giá trị |
|---|---|
| Repo | [IfcOpenShell/IfcOpenShell](https://github.com/IfcOpenShell/IfcOpenShell) |
| Snapshot | 2,917★, chưa archive (GitHub API, 2026-11-02); HEAD `28bae192780e` ngày 2026-10-30 |
| License | LGPL-3.0-or-later (core); GPL-3.0-or-later (Bonsai); [file thật](https://github.com/IfcOpenShell/IfcOpenShell/blob/28bae192780ebd34936441f1f7bc1ffb9d282be9/README.md) |
| Bằng chứng | [Triển khai/đặc tả](https://github.com/IfcOpenShell/IfcOpenShell/blob/28bae192780ebd34936441f1f7bc1ffb9d282be9/src/ifctester/ifctester/ids.py); [CI tại cùng commit](https://github.com/IfcOpenShell/IfcOpenShell/tree/28bae192780ebd34936441f1f7bc1ffb9d282be9/.github/workflows); đọc mã/đặc tả, chưa chạy |

Monorepo có core IFC, IfcTester, IfcDiff, IfcClash và Bonsai. IfcTester open/from_string có validate mặc định false: chỉ bỏ bước validate() tường minh; decode vẫn qua XMLSchema và bắt lỗi, nên không kết luận validation mặc định bị tắt. Kiểm schema IDS, đánh giá requirements và kiểm schema IFC là các cổng riêng.

**Tích hợp và giới hạn:** Chọn đúng package thay vì gán một license cho cả monorepo. IDS pass chỉ bao phủ yêu cầu đã viết; thêm kiểm schema/geometry/domain và fixture âm. API/core version phải khớp exporter.

### FreeCAD

| Thuộc tính | Giá trị |
|---|---|
| Repo | [FreeCAD/FreeCAD](https://github.com/FreeCAD/FreeCAD) |
| Snapshot | 35,047★, chưa archive (GitHub API, 2026-11-02); HEAD `66644dee63d3` ngày 2026-11-01 |
| License | LGPL-2.1-or-later; thành phần riêng kiểm thêm; [file thật](https://github.com/FreeCAD/FreeCAD/blob/66644dee63d3d260f1e0b9a8517d1a13631e903f/LICENSE) |
| Bằng chứng | [Triển khai/đặc tả](https://github.com/FreeCAD/FreeCAD/blob/66644dee63d3d260f1e0b9a8517d1a13631e903f/src/Mod/Part/App/TopoShape.cpp); [CI tại cùng commit](https://github.com/FreeCAD/FreeCAD/tree/66644dee63d3d260f1e0b9a8517d1a13631e903f/.github/workflows); đọc mã/đặc tả, chưa chạy |

CAD tham số/B-rep dựa OpenCascade; TopoShape::isValid dùng BRepCheck_Analyzer. Đây là cổng hình học cụ thể, không chỉ ảnh chụp hoặc exit code.

**Tích hợp và giới hạn:** Dùng Python/GUI/CLI theo workbench và build. Kiểm recompute, valid solid, kích thước và export/reimport STEP; API/workbench/plugin khác license và khả năng headless. Chưa chạy model thật.

### OpenSCAD

| Thuộc tính | Giá trị |
|---|---|
| Repo | [openscad/openscad](https://github.com/openscad/openscad) |
| Snapshot | 10,572★, chưa archive (GitHub API, 2026-11-02); HEAD `8e8df3ddae29` ngày 2026-11-01 |
| License | GPL-2.0-or-later + ngoại lệ liên kết CGAL; [file thật](https://github.com/openscad/openscad/blob/8e8df3ddae295e8667cbc9f6c4fbb7c88b0ec45b/COPYING) |
| Bằng chứng | [Triển khai/đặc tả](https://github.com/openscad/openscad/blob/8e8df3ddae295e8667cbc9f6c4fbb7c88b0ec45b/src/openscad.cc); [CI tại cùng commit](https://github.com/openscad/openscad/tree/8e8df3ddae295e8667cbc9f6c4fbb7c88b0ec45b/.github/workflows); đọc mã/đặc tả, chưa chạy |

Mô hình CSG viết bằng mã, thuận lợi diff và tái sinh; CLI có export và phân biệt render/preview. Hợp chi tiết tham số hơn thao tác trực tiếp mesh nghệ thuật.

**Tích hợp và giới hạn:** Ghim engine/backend, tham số, font và dependency; kiểm số solid/dimension sau xuất. File STL không tự mang hợp đồng đơn vị hay dung sai; license output/asset kiểm riêng.

### Trimesh

| Thuộc tính | Giá trị |
|---|---|
| Repo | [mikedh/trimesh](https://github.com/mikedh/trimesh) |
| Snapshot | 3,716★, chưa archive (GitHub API, 2026-11-02); HEAD `6c158cce2265` ngày 2026-10-23 |
| License | MIT; [file thật](https://github.com/mikedh/trimesh/blob/6c158cce226500fc64b12acd265af0cf01d1c212/LICENSE.md) |
| Bằng chứng | [Triển khai/đặc tả](https://github.com/mikedh/trimesh/blob/6c158cce226500fc64b12acd265af0cf01d1c212/trimesh/base.py); [CI tại cùng commit](https://github.com/mikedh/trimesh/tree/6c158cce226500fc64b12acd265af0cf01d1c212/.github/workflows); đọc mã/đặc tả, chưa chạy |

is_watertight kiểm mỗi cạnh thuộc hai mặt; is_volume còn kiểm winding, center_mass hữu hạn và volume dương. Đây là các predicate khác nhau, không dùng một cờ watertight đại diện mọi kiểm.

**Tích hợp và giới hạn:** API Python cho mesh loading/analysis; giữ scale/unit và hash mesh. is_volume chưa chứng minh self-intersection-free, wall thickness, độ bền hay tính chế tạo; không thay kernel B-rep.

### buildingSMART IDS

| Thuộc tính | Giá trị |
|---|---|
| Repo | [buildingSMART/IDS](https://github.com/buildingSMART/IDS) |
| Snapshot | 329★, chưa archive (GitHub API, 2026-11-02); HEAD `870f9c4e6e8f` ngày 2026-09-25 |
| License | CC-BY-ND-4.0 (đặc tả); [file thật](https://github.com/buildingSMART/IDS/blob/870f9c4e6e8f414e737b4d84ca1aa9b46fc6c8f3/LICENSE) |
| Bằng chứng | [Triển khai/đặc tả](https://github.com/buildingSMART/IDS/blob/870f9c4e6e8f414e737b4d84ca1aa9b46fc6c8f3/Schema/ids.xsd); [CI tại cùng commit](https://github.com/buildingSMART/IDS/tree/870f9c4e6e8f414e737b4d84ca1aa9b46fc6c8f3/.github/workflows); đọc mã/đặc tả, chưa chạy |

Chuẩn XML mô tả thông tin IFC cần bàn giao; repo có XSD, testcases và workflow AuditAllIdsFiles. Dùng làm corpus kiểm validator thay vì chỉ tin tuyên bố hỗ trợ IDS.

**Tích hợp và giới hạn:** Ghim release/spec corpus, phân applicability và requirements; đặc tả có ND nên không tự gắn license phần mềm/đổi tên bản sửa. XSD validity và compliance với model là hai phép kiểm.

### buildingSMART BCF-XML

| Thuộc tính | Giá trị |
|---|---|
| Repo | [buildingSMART/BCF-XML](https://github.com/buildingSMART/BCF-XML) |
| Snapshot | 263★, chưa archive (GitHub API, 2026-11-02); HEAD `bc48611d0d7a` ngày 2023-11-28 |
| License | CC-BY-ND-4.0 (đặc tả); [file thật](https://github.com/buildingSMART/BCF-XML/blob/bc48611d0d7a1587f028a2b69677a1aafd5cd0a8/LICENSE) |
| Bằng chứng | [Triển khai/đặc tả](https://github.com/buildingSMART/BCF-XML/blob/bc48611d0d7a1587f028a2b69677a1aafd5cd0a8/.github/workflows/check-test-cases.yml); [CI tại cùng commit](https://github.com/buildingSMART/BCF-XML/tree/bc48611d0d7a1587f028a2b69677a1aafd5cd0a8/.github/workflows); đọc mã/đặc tả, chưa chạy |

Chuẩn trao đổi issue/viewpoint, có schema/testcases; default branch release_3_0 tại lần đọc. Không mặc định tương thích BCF2.1 của một host với3.0.

**Tích hợp và giới hạn:** Chọn version theo consumer, kiểm GUID/viewpoint/model revision và round-trip. CI CheckTestCases là bằng chứng repo có kiểm spec, kho chưa chạy corpus; khác BCF API và khác kiểm model IFC.

## 3. Cổng kiểm theo biểu diễn

| Lớp kiểm | Bằng chứng tối thiểu | Giới hạn |
|---|---|---|
| Contract | Đơn vị, trục tọa độ, kích thước, hệ dung sai, phiên bản schema và giới hạn xuất | Prompt có số đo không thay spec máy đọc được |
| Mesh | Số component, bounding box, watertight, winding, volume hữu hạn/dương | Chưa chứng minh wall thickness, khoảng hở hoặc độ bền |
| B-rep | Shape validity, solid count, volume/bbox, round-trip STEP với sai số đã định | Chưa chứng minh thiết kế có thể gia công/lắp ráp |
| BIM | IFC schema, yêu cầu IDS áp dụng đúng tập phần tử, unit/property/classification | IDS chỉ kiểm yêu cầu đã viết; không bao trùm toàn bộ quy chuẩn xây dựng |
| Trao đổi vấn đề | BCF version, GUID/viewpoint liên kết đúng model revision | BCF đóng issue không tự chứng minh model được sửa đúng |
| Host thật | Revit/AutoCAD/Blender version, file mở/save/reopen, ảnh và dữ liệu sau lệnh | Test bridge/CLI trên Linux không chứng minh add-in chạy đúng trong host |

## 4. Kiến trúc agent sửa model

1. Đọc capability và schema của host; tra tên tham số có thật. Agent đề xuất lệnh có phạm vi phần tử cụ thể.
2. Tạo preview/dry-run với **model revision, operation hash, affected IDs** và ước lượng tài nguyên. Query lớn có limit/pagination.
3. Xác nhận gắn với chính preview; model thay đổi thì preview hết hiệu lực. Dùng transaction/snapshot theo khả năng host; không gọi undo là rollback đã kiểm.
4. Thực thi, lấy IDs thay đổi và đọc lại giá trị/hình học. Timeout có thể là đã chạy: đối soát operation ID trước retry.
5. Chạy cổng rẻ trước render đắt; bằng chứng khóa vào hash scene/spec. Ghi `passed`, `failed`, `not-run` theo từng check.
6. Kiểm xuất/nhập lại bằng bộ đọc độc lập khi cần bàn giao; giữ native file cùng STEP/IFC/mesh. Liên kết [04](../04-protocols-standards/README.md), [11](../11-browser-computer-use-sandbox/README.md), [21](../21-autonomous-workflows/README.md), [23](../23-own-repos-lessons/README.md).

## 5. Chọn stack theo nhu cầu

- **BIM kiểm thông tin:** IFC + IDS chính thức → IfcTester → báo cáo phần tử lỗi → BCF. Cần test requirement bị thiếu/sai và trường hợp không áp dụng, không chỉ fixture xanh.
- **Chi tiết tham số:** FreeCAD/OpenSCAD → kiểm hình học → STEP/STL → kiểm kích thước lại; muốn giao dịch trong Revit dùng host bridge của case study, không thay bằng mesh generator.
- **Asset mesh:** Blender → Trimesh → kiểm kỹ thuật + render review; license texture/font/model là lớp riêng với license code.

## 5b. Kiểm bài giới thiệu CanvasAnvil (codingfeng101/canvasanvil): “bản vẽ cải tạo nội thất chuyên nghiệp từ một câu” phần lớn là ảnh do model sinh ảnh vẽ (bài người dùng gửi, đọc mã 3/11/2026)

> Bài người dùng gửi: "CanvasAnvil: The AI Studio For Everything… turns a single sentence into a full set of professional interior renovation drawings, including floor plans, ceiling layouts, and material lists… Open source: github.com/codingfeng101/canvasanvil". Đã clone `--filter=blob:none` đủ lịch sử, HEAD `27f1aea1b8a7e2fcfe01cb2610a3d4e54db4987e` (1/11/2026). **Không cài, không chạy.**

### 5b.1 Hồ sơ nhanh

| Thuộc tính | Giá trị (3/11/2026) |
|---|---|
| Repo | https://github.com/codingfeng101/canvasanvil · **113★, 8 fork**, tạo 24/1/2026 (GitHub search API). README ghi v2.2.0 |
| License | MIT, "Copyright (c) 2026 CodingFeng101" |
| Lịch sử | 157 commit, một tác giả (hai email), **88 commit có trailer Co-Authored-By Claude** |
| Là gì | Web app React + Vite + server Node với 4 workspace: sơ đồ (flowchart, xuất XML), nội thất ("CAD"), slide (PPT xuất PDF hoặc PPT dạng ảnh), chỉnh ảnh. Dùng API tương thích OpenAI do người dùng tự cấu hình (`server/ai/model.ts`: key, base URL, model theo từng request) |

### 5b.2 Kiểm nhận định "bộ bản vẽ kỹ thuật chuyên nghiệp"

Đọc `client/workspaces/cad/lib/tasks.ts` và `resources/prompts/cad/`:

1. LLM sinh **plan JSON + một mặt bằng 2D dạng SVG** (`svg-markup.ts`, `apply-cad-patch.ts`). Đây là phần duy nhất có hình học vector.
2. Agent "Master Renovation Scheme" viết phương án tổng làm nguồn chung.
3. Với mỗi tờ (Renovation Plan Layout, Floor Finish Plan, **Reflected Ceiling Plan**, Wall Setting-Out, **MEP**, Elevations, Detail Drawings, hai bảng phân tích), một agent riêng viết **prompt JSON "directly usable by the downstream image generator"** (`images-agents/reflected-ceiling-plan.md`). Prompt này được gửi tới model sinh ảnh (`server/ai/image.ts`: `/images/generations`, gpt-image hoặc dall-e-3, hoặc cổng chat tương thích).
4. Bảng vật tư (BOM) do LLM viết từ plan JSON + SVG (`bom-prompt.md`).

| Nhận định | Kết quả |
|---|---|
| "single sentence → full set of drawings" | ✅ đúng về luồng: một yêu cầu kéo theo chuỗi agent sinh đủ các tờ |
| "professional interior renovation drawings… floor plans, ceiling layouts" | ⚠️ **phần lớn là ảnh raster do AI vẽ**, không phải bản vẽ CAD: không có lớp (layer), kích thước không đo được, không xuất DXF, DWG hay IFC (grep dxf, dwg, ifc trong `client/` và `server/` không có kết quả). Kích thước, ký hiệu đèn, MEP và chi tiết trên ảnh có thể trông hợp lý nhưng không có cơ chế kiểm tra nào ràng buộc chúng với mặt bằng SVG |
| "material lists" | ⚠️ văn bản do LLM viết, không tính từ hình học; số lượng cần kiểm lại |
| "Open source" | ✅ MIT. Nhưng cần API key trả phí của bên thứ ba cho LLM và model sinh ảnh |

### 5b.3 Dữ liệu và rủi ro

- **Langfuse tùy chọn ghi toàn bộ nội dung**: nếu đặt `LANGFUSE_PUBLIC_KEY` (`server/telemetry/langfuse.ts`), mọi request chat ghi `recordInputs` và `recordOutputs`, và `server/routes/chat.ts` lấy **IP của người dùng (`x-forwarded-for`) làm `userId`**. Không bật thì không gửi. Ai tự host cho người khác dùng cần thông báo việc này và cân nhắc dữ liệu cá nhân (mục 18 §4e).
- Nội dung yêu cầu và ảnh tham chiếu đi tới nhà cung cấp model mà người dùng cấu hình.
- Dự án nhỏ, một tác giả; README ghi "PRs welcome", 0 issue mở.

### 5b.4 Đặt trong bối cảnh mục 27

- Khác với các cổng kiểm theo biểu diễn ở §3 (IFC/IDS, hình học có kiểm), CanvasAnvil cho ra **ảnh minh họa phương án**: dùng được để trao đổi ý tưởng với khách hoặc làm moodboard, **không dùng làm hồ sơ thi công** khi chưa có người có chứng chỉ dựng lại trên CAD/BIM thật.
- Nếu muốn agent ra bản vẽ đo được: sinh hình học (SVG/DXF/IFC) rồi kiểm bằng máy (kích thước phòng, va chạm, IDS), như các stack ở §5, thay vì nhờ model sinh ảnh vẽ tờ hoàn chỉnh.

**Nguồn §5b:** bài người dùng gửi 3/11/2026 · clone https://github.com/codingfeng101/canvasanvil HEAD `27f1aea1b8a7e2fcfe01cb2610a3d4e54db4987e`: https://github.com/codingfeng101/canvasanvil/blob/27f1aea1b8a7e2fcfe01cb2610a3d4e54db4987e/README.md · https://github.com/codingfeng101/canvasanvil/blob/27f1aea1b8a7e2fcfe01cb2610a3d4e54db4987e/LICENSE · https://github.com/codingfeng101/canvasanvil/blob/27f1aea1b8a7e2fcfe01cb2610a3d4e54db4987e/client/workspaces/cad/lib/tasks.ts · https://github.com/codingfeng101/canvasanvil/blob/27f1aea1b8a7e2fcfe01cb2610a3d4e54db4987e/resources/prompts/cad/images-agents/reflected-ceiling-plan.md · https://github.com/codingfeng101/canvasanvil/blob/27f1aea1b8a7e2fcfe01cb2610a3d4e54db4987e/resources/prompts/cad/bom-prompt.md · https://github.com/codingfeng101/canvasanvil/blob/27f1aea1b8a7e2fcfe01cb2610a3d4e54db4987e/server/ai/image.ts · https://github.com/codingfeng101/canvasanvil/blob/27f1aea1b8a7e2fcfe01cb2610a3d4e54db4987e/server/ai/model.ts · https://github.com/codingfeng101/canvasanvil/blob/27f1aea1b8a7e2fcfe01cb2610a3d4e54db4987e/server/telemetry/langfuse.ts · https://github.com/codingfeng101/canvasanvil/blob/27f1aea1b8a7e2fcfe01cb2610a3d4e54db4987e/server/routes/chat.ts · GitHub search API `repo:codingfeng101/canvasanvil` 3/11/2026.

<a id="factory-2026-11-04"></a>

## 6. Nâng trần 4/11/2026: CAD tạo bằng mã phải có hợp đồng đơn vị và vòng xuất–nhập

**Trần hiện tại:** §3 đã tách mesh/B-rep/BIM và §4 có đọc lại host. Xưởng còn cần fixture hồi quy hình học, unit/tolerance qua exporter và quy trình kiểm artifact độc lập với ảnh preview. Các ngưỡng dưới đây do dự án tích hợp chọn theo domain, không phải một chuẩn an toàn chế tạo chung.

| Lựa chọn | Điểm mạnh phù hợp | Bằng chứng nghiệm thu | Giới hạn phải giữ |
|---|---|---|---|
| CadQuery dưới đây | Sinh B-rep tham số bằng Python, hợp backend/CI không GUI | Validity + số solid + bbox/volume + STEP round-trip có đơn vị | Kernel hợp lệ không chứng minh chi tiết sản xuất được |
| FreeCAD ở §2 | Workbench/tài liệu tham số và GUI cho kỹ sư | Recompute, mở/lưu/mở lại file, đọc giá trị sau chỉnh | Phiên bản host/add-in và headless cần kiểm riêng |
| OpenSCAD ở §2 | Mô hình CSG bằng mã dễ review | Render backend đã ghim, solid/dimension sau export | Preview không thay render; STL không tự định nghĩa unit |
| IfcOpenShell/IfcTester ở §2 | BIM và yêu cầu thông tin IDS | Schema IFC + IDS + GUID/property/domain | IDS pass chỉ phủ yêu cầu được mô tả |
| Trimesh ở §2 | Kiểm mesh độc lập sau tessellation | Component, winding, volume, bbox/scale | Không thay kernel B-rep, kiểm độ bền hoặc DFM |

<a id="cadquery"></a>

### CadQuery: exporter và importer đều mang tham số đơn vị

| Thuộc tính | Giá trị |
|---|---|
| Repo / SHA / license | [CadQuery/cadquery](https://github.com/CadQuery/cadquery), `8178185a24a035c9af7f4679033be14267f6a6ef`, Apache-2.0; OCP/OCCT và dependency kiểm quyền riêng |
| Kiểm chứng 2026-11-04 | `code-read`: README/LICENSE, `shapes.py`, export/import STEP và workflow container; chưa tạo shape/build hoặc chạy kernel |
| Cơ chế cụ thể | `Shape.isValid()` gọi `BRepCheck_Analyzer(...).IsValid()`. `export()` nhận `unit="MM"`, `outputUnit`, chuyển tham số cho `exportStep`; import STEP nhận `unit="MM"`, đặt target cascade unit trước khi đọc, để OCCT scale từ unit khai trong file. |
| Cổng đã có trong upstream | Workflow `apptainer_build.yml` build container rồi gọi `pytest tests/`; sự hiện diện workflow không xác nhận run thành công hoặc mọi distro/phiên bản kernel đều tương đương. |
| Tích hợp | Khóa schema tham số, phiên bản CadQuery/OCP/OCCT, đơn vị đầu vào/xuất/nhập và tolerance theo model units. Lưu script + input manifest + checksum STEP/STL + số đo sau reimport. |
| Hạn chế / rủi ro | Một cờ valid không chứng minh đúng kích thước, không self-intersection ở mọi phép biểu diễn, wall thickness, clearance hoặc tuân quy chuẩn. Python script do agent sinh cần sandbox/quota như mã thực thi, không mở quyền ghi host tùy ý. |

**Tuyến nâng sâu:**

1. Mô tả yêu cầu thành schema: đơn vị, hệ tọa độ, miền tham số, dung sai kích thước, số solid và feature quan trọng; có fixture biên/âm (rỗng, chiều âm, giao nhau, lỗ nhỏ hơn ngưỡng). Agent chỉ đề xuất tham số/lệnh trong capability của host.
2. Sinh bằng engine đã ghim, giữ artifact gốc và lịch sử tham số; kiểm exception, recompute, validity, số solid, bbox và volume có ý nghĩa. Sai một cổng không được che bằng ảnh render đẹp.
3. Export STEP theo unit rõ, import vào tiến trình sạch bằng target unit rõ; so dimensions/volume theo tolerance nghiệp vụ. Đối với STL, mang unit trong manifest ngoài file và kiểm lại scale ở consumer.
4. Chạy hồi quy hình học trên nhiều bộ tham số; so invariants/đặc trưng thay vì hash binary đơn độc vì kernel/export có thể đổi byte không đổi hình. Với BIM thêm schema/IDS; với host thật kiểm save/reopen và readback.
5. Kỹ sư có thẩm quyền duyệt DFM/tải trọng/quy chuẩn theo ngữ cảnh; giữ report đo và người duyệt bên cạnh model revision. Nối [mục 30](../30-software-testing-quality/README.md) cho contract/hồi quy, [31](../31-software-supply-chain-security/README.md) cho dependency/asset.

**Đã đổi so với đợt trước:** bổ sung CadQuery như một tuyến B-rep chạy trong pipeline, và kiểm đơn vị ở cả hai phía STEP thay vì chỉ ghi unit trong prompt. Không suy ảnh CanvasAnvil ở §5b thành artifact CAD đo được. **Nguồn §6:** [README.md](https://github.com/CadQuery/cadquery/blob/8178185a24a035c9af7f4679033be14267f6a6ef/README.md) · [LICENSE](https://github.com/CadQuery/cadquery/blob/8178185a24a035c9af7f4679033be14267f6a6ef/LICENSE) · [cadquery/occ_impl/shapes.py](https://github.com/CadQuery/cadquery/blob/8178185a24a035c9af7f4679033be14267f6a6ef/cadquery/occ_impl/shapes.py) · [exporter STEP](https://github.com/CadQuery/cadquery/blob/8178185a24a035c9af7f4679033be14267f6a6ef/cadquery/occ_impl/exporters/__init__.py) · [importer STEP](https://github.com/CadQuery/cadquery/blob/8178185a24a035c9af7f4679033be14267f6a6ef/cadquery/occ_impl/importers/__init__.py) · [.github/workflows/apptainer_build.yml](https://github.com/CadQuery/cadquery/blob/8178185a24a035c9af7f4679033be14267f6a6ef/.github/workflows/apptainer_build.yml).

<a id="anhkysuai-2026-11-23"></a>

## Đánh giá từ kho Anh Kỹ Sư AI — 23/11/2026

Phần này có **34 hồ sơ hoặc phạm vi đối chiếu** từ [nguồn tuyển chọn](https://anhkysuai.com/kho/). [Bảng đủ 1.295 repo](../data/collections/anhkysuai-kho.json) ghi trạng thái đối chiếu từng link; [danh sách URL](../data/collections/anhkysuai-kho-links.txt) phục vụ tra cứu. Nguồn tuyển chọn giúp phát hiện repo; đánh giá bên dưới dựa trên clone và permalink upstream cùng metadata GitHub ngày 2026-11-23.

Mức `docs-read`/`code-read` chỉ áp dụng phạm vi ghi tại mỗi hồ sơ. Chưa cài, build, chạy test hay benchmark mã upstream. Giấy phép có thể tách theo code, model, nội dung, asset hoặc bản enterprise; con số/tuyên bố của tác giả chưa được tái lập nếu không có ghi chú khác.

<a id="anhkysuai-2026-11-23-graphdeco-gaussian-splatting"></a>

### 3D Gaussian Splatting

**Repo:** [graphdeco-inria/gaussian-splatting](https://github.com/graphdeco-inria/gaussian-splatting) · **License:** INRIA tùy chỉnh, nghiên cứu/đánh giá phi thương mại; thương mại cần chấp thuận · **★ 24,526 (GitHub API, 2026-11-23)**

**Mục đích:** Tái dựng cảnh và tổng hợp góc nhìn mới bằng biểu diễn các Gaussian 3D.

**Giá trị và cơ chế:** Mã tham chiếu của nghiên cứu mô tả tối ưu biểu diễn từ ảnh đã hiệu chuẩn và kết xuất theo góc nhìn; hữu ích để học pipeline novel-view synthesis.

**Giới hạn:** LICENSE giới hạn nghiên cứu và đánh giá phi thương mại, có ngoại lệ MIT cho một file tiện ích. Chưa huấn luyện, đo chất lượng hoặc tái hiện tốc độ công bố.

**Cách tham khảo/tích hợp:** Đọc phạm vi license trước khi tích hợp; dùng tập cảnh có quyền khai thác và lưu cấu hình, checkpoint khi so sánh.

**Thay thế:** gsplat, Nerfstudio, Instant-NGP.

**Bằng chứng:** `docs-read`, ngày 2026-11-23, commit [`54c035f7834b`](https://github.com/graphdeco-inria/gaussian-splatting/commit/54c035f7834b564019656c3e3fcc3646292f727d). README và các tài liệu/manifest/CI hiện diện, đọc chọn lọc; chưa kiểm implementation. Chưa cài/chạy upstream.

**Nguồn:** [README.md](https://github.com/graphdeco-inria/gaussian-splatting/blob/54c035f7834b564019656c3e3fcc3646292f727d/README.md) · [LICENSE.md](https://github.com/graphdeco-inria/gaussian-splatting/blob/54c035f7834b564019656c3e3fcc3646292f727d/LICENSE.md) · [metadata GitHub](https://api.github.com/repos/graphdeco-inria/gaussian-splatting).

<a id="anhkysuai-2026-11-23-atsushisakai-pythonrobotics"></a>

### PythonRobotics

**Repo:** [AtsushiSakai/PythonRobotics](https://github.com/AtsushiSakai/PythonRobotics) · **License:** MIT · **★ 30,959 (GitHub API, 2026-11-23)**

**Mục đích:** Mã ví dụ và giáo trình thuật toán robotics bằng Python: định vị, bản đồ, SLAM và lập đường đi.

**Giá trị:** Ví dụ nhỏ phục vụ hiểu ý tưởng thuật toán, thuận tiện so cách mô hình hóa và trực quan hóa.

**Giới hạn:** Mô phỏng giáo dục chưa chứng minh an toàn hay độ ổn định khi điều khiển robot thực; chưa chạy hoặc tái lập phép đo.

**Cách tham khảo/tích hợp:** Chọn bài theo mục tiêu, thực hành lại trên môi trường riêng và kiểm bằng bài chuyển giao; khi dùng lại nội dung phải đối chiếu giấy phép đúng phạm vi.

**Lựa chọn để đối chiếu:** [TianxingChen/Embodied-AI-Guide](https://github.com/TianxingChen/Embodied-AI-Guide) · [bulletphysics/bullet3](https://github.com/bulletphysics/bullet3). Đây là ứng viên so sánh theo tác vụ; mức phù hợp cần kiểm theo hồ sơ và phiên bản riêng.

**Bằng chứng:** `docs-read`, ngày 2026-11-23, commit [`ef64608ceb0012f2a0b3d532fddc80243e807cfa`](https://github.com/AtsushiSakai/PythonRobotics/commit/ef64608ceb0012f2a0b3d532fddc80243e807cfa), ngày commit 2026-11-10. Đã clone và đọc chọn lọc phần giới thiệu, cách dùng, giới hạn, license, metadata manifest và CI hiện diện. Chưa kiểm đầy đủ implementation hoặc chạy upstream; các số đo của tác giả chưa được tái lập.

**Nguồn:** [README.md](https://github.com/AtsushiSakai/PythonRobotics/blob/ef64608ceb0012f2a0b3d532fddc80243e807cfa/README.md) · [LICENSE](https://github.com/AtsushiSakai/PythonRobotics/blob/ef64608ceb0012f2a0b3d532fddc80243e807cfa/LICENSE) · [.github/workflows/Linux_CI.yml](https://github.com/AtsushiSakai/PythonRobotics/blob/ef64608ceb0012f2a0b3d532fddc80243e807cfa/.github/workflows/Linux_CI.yml) · [metadata GitHub](https://api.github.com/repos/AtsushiSakai/PythonRobotics).

<a id="anhkysuai-2026-11-23-babylonjs-babylon.js"></a>

### Babylon.js

**Repo:** [BabylonJS/Babylon.js](https://github.com/BabylonJS/Babylon.js) · **License:** Apache-2.0 · **★ 26,430 (GitHub API, 2026-11-23)**

**Mục đích:** Engine JavaScript cho dựng hình và ứng dụng 3D trên web, có playground và gói mô-đun.

**Giá trị:** Tài liệu và ví dụ phong phú hỗ trợ tạo cảnh tương tác; các gói ES6 cho phép chọn phần cần dùng.

**Giới hạn:** README cảnh báo CDN công cộng chỉ dành học/thử nghiệm và yêu cầu tự phục vụ gói cho production; cần đo tải GPU, bộ nhớ và thiết bị đích trước triển khai.

**Cách tham khảo/tích hợp:** Thử trên bản sao mô hình với đơn vị và dung sai đã biết, kiểm đầu ra/round-trip và quyền của từng thành phần trước đưa vào quy trình kỹ thuật.

**Lựa chọn để đối chiếu:** [mrdoob/three.js](https://github.com/mrdoob/three.js) · [pixijs/pixijs](https://github.com/pixijs/pixijs). Đây là ứng viên so sánh theo tác vụ; mức phù hợp cần kiểm theo hồ sơ và phiên bản riêng.

**Bằng chứng:** `docs-read`, ngày 2026-11-23, commit [`47f84cf6dc635e97bfef29408be1cea41279334a`](https://github.com/BabylonJS/Babylon.js/commit/47f84cf6dc635e97bfef29408be1cea41279334a), ngày commit 2026-11-21. Đã clone và đọc chọn lọc phần giới thiệu, cách dùng, giới hạn, license, metadata manifest và CI hiện diện. Chưa kiểm đầy đủ implementation hoặc chạy upstream; các số đo của tác giả chưa được tái lập.

**Nguồn:** [readme.md](https://github.com/BabylonJS/Babylon.js/blob/47f84cf6dc635e97bfef29408be1cea41279334a/readme.md) · [license.md](https://github.com/BabylonJS/Babylon.js/blob/47f84cf6dc635e97bfef29408be1cea41279334a/license.md) · [package.json](https://github.com/BabylonJS/Babylon.js/blob/47f84cf6dc635e97bfef29408be1cea41279334a/package.json) · [.github/workflows/stale.yml](https://github.com/BabylonJS/Babylon.js/blob/47f84cf6dc635e97bfef29408be1cea41279334a/.github/workflows/stale.yml) · [metadata GitHub](https://api.github.com/repos/BabylonJS/Babylon.js).

<a id="anhkysuai-2026-11-23-ssloy-tinyrenderer"></a>

### TinyRenderer

**Repo:** [ssloy/tinyrenderer](https://github.com/ssloy/tinyrenderer) · **License:** Zlib (mã; xem LICENSE.txt) · **★ 24,570 (GitHub API, 2026-11-23)**

**Mục đích:** Khóa học dựng hình bằng C++ với renderer phần mềm nhỏ và bài học rasterization, camera, shading.

**Giá trị:** Phù hợp hiểu pipeline đồ họa qua từng bước thay vì dựa ngay vào engine lớn.

**Giới hạn:** Đây là triển khai giáo dục; chưa đo tính đúng hoặc hiệu năng render. Giấy phép tệp mã có điều khoản kiểu zlib, còn bài viết và asset cần kiểm phạm vi riêng.

**Cách tham khảo/tích hợp:** Chọn bài theo mục tiêu, thực hành lại trên môi trường riêng và kiểm bằng bài chuyển giao; khi dùng lại nội dung phải đối chiếu giấy phép đúng phạm vi.

**Lựa chọn để đối chiếu:** [BabylonJS/Babylon.js](https://github.com/BabylonJS/Babylon.js) · [google/filament](https://github.com/google/filament). Đây là ứng viên so sánh theo tác vụ; mức phù hợp cần kiểm theo hồ sơ và phiên bản riêng.

**Bằng chứng:** `docs-read`, ngày 2026-11-23, commit [`97eb7a480e762285899a93c5d21e70a79e60782e`](https://github.com/ssloy/tinyrenderer/commit/97eb7a480e762285899a93c5d21e70a79e60782e), ngày commit 2026-07-29. Đã clone và đọc chọn lọc phần giới thiệu, cách dùng, giới hạn, license, metadata manifest và CI hiện diện. Chưa kiểm đầy đủ implementation hoặc chạy upstream; các số đo của tác giả chưa được tái lập.

**Nguồn:** [README.md](https://github.com/ssloy/tinyrenderer/blob/97eb7a480e762285899a93c5d21e70a79e60782e/README.md) · [LICENSE.txt](https://github.com/ssloy/tinyrenderer/blob/97eb7a480e762285899a93c5d21e70a79e60782e/LICENSE.txt) · [CMakeLists.txt](https://github.com/ssloy/tinyrenderer/blob/97eb7a480e762285899a93c5d21e70a79e60782e/CMakeLists.txt) · [metadata GitHub](https://api.github.com/repos/ssloy/tinyrenderer).

<a id="anhkysuai-2026-11-23-cesiumgs-cesium"></a>

### cesium

**Repo:** [CesiumGS/cesium](https://github.com/CesiumGS/cesium) · **License:** Apache-2.0 · **★ 15,979 (GitHub API, 2026-11-23)**

**Mục đích:** Thư viện JavaScript dựng quả địa cầu 3D và bản đồ 2D trong trình duyệt.

**Giá trị:** Hỗ trợ dữ liệu động và các định dạng mở, phù hợp trực quan hóa không gian địa lý và 3D Tiles.

**Giới hạn:** Apache-2.0 áp dụng engine; Cesium ion, dữ liệu địa hình/ảnh và nhà cung cấp bản đồ có điều khoản riêng. Cần đo tải dữ liệu/GPU và kiểm hệ tọa độ cho trường hợp đích.

**Cách tham khảo/tích hợp:** Ghim phiên bản và nguồn dữ liệu, kiểm CRS, đơn vị và một tập mẫu có kết quả chuẩn trước tích hợp pipeline GIS.

**Lựa chọn để đối chiếu:** [maplibre/maplibre-gl-js](https://github.com/maplibre/maplibre-gl-js) · [keplergl/kepler.gl](https://github.com/keplergl/kepler.gl). Đây là ứng viên so sánh theo tác vụ; mức phù hợp cần kiểm theo hồ sơ và phiên bản riêng.

**Bằng chứng:** `docs-read`, ngày 2026-11-23, commit [`8b9674e1aa4c22f917bf841d33fe0325d089c98e`](https://github.com/CesiumGS/cesium/commit/8b9674e1aa4c22f917bf841d33fe0325d089c98e), ngày commit 2026-11-21. Đã clone và đọc chọn lọc phần giới thiệu, cách dùng, giới hạn, license, metadata manifest và CI hiện diện. Chưa kiểm đầy đủ implementation hoặc chạy upstream; các số đo của tác giả chưa được tái lập.

**Nguồn:** [README.md](https://github.com/CesiumGS/cesium/blob/8b9674e1aa4c22f917bf841d33fe0325d089c98e/README.md) · [LICENSE.md](https://github.com/CesiumGS/cesium/blob/8b9674e1aa4c22f917bf841d33fe0325d089c98e/LICENSE.md) · [package.json](https://github.com/CesiumGS/cesium/blob/8b9674e1aa4c22f917bf841d33fe0325d089c98e/package.json) · [.github/workflows/cla.yml](https://github.com/CesiumGS/cesium/blob/8b9674e1aa4c22f917bf841d33fe0325d089c98e/.github/workflows/cla.yml) · [metadata GitHub](https://api.github.com/repos/CesiumGS/cesium).

<a id="anhkysuai-2026-11-23-bulletphysics-bullet3"></a>

### bullet3

**Repo:** [bulletphysics/bullet3](https://github.com/bulletphysics/bullet3) · **License:** Zlib (chính); Extras và bên thứ ba có ngoại lệ · **★ 14,892 (GitHub API, 2026-11-23)**

**Mục đích:** SDK C++ mô phỏng vật lý và phát hiện va chạm, có PyBullet cho Python.

**Giá trị:** Bao quát game, robot và nghiên cứu học tăng cường; hữu ích thử mô hình động lực học hoặc va chạm.

**Giới hạn:** LICENSE nêu ngoại lệ cho Extras và thư viện bên thứ ba; mô phỏng cần kiểm đơn vị, bước thời gian và sai số trước suy sang hệ vật lý thật. Issue tracker đang đóng theo README.

**Cách tham khảo/tích hợp:** Tách simulator khỏi adapter phần cứng, chọn dữ liệu chuẩn để kiểm độ đúng và sai số trước sử dụng thực tế.

**Lựa chọn để đối chiếu:** [jrouwe/JoltPhysics](https://github.com/jrouwe/JoltPhysics) · [google-deepmind/mujoco](https://github.com/google-deepmind/mujoco). Đây là ứng viên so sánh theo tác vụ; mức phù hợp cần kiểm theo hồ sơ và phiên bản riêng.

**Bằng chứng:** `docs-read`, ngày 2026-11-23, commit [`d3afe76132fc76b0f9b2359cbaef47a3766e7fbb`](https://github.com/bulletphysics/bullet3/commit/d3afe76132fc76b0f9b2359cbaef47a3766e7fbb), ngày commit 2026-10-09. Đã clone và đọc chọn lọc phần giới thiệu, cách dùng, giới hạn, license, metadata manifest và CI hiện diện. Chưa kiểm đầy đủ implementation hoặc chạy upstream; các số đo của tác giả chưa được tái lập.

**Nguồn:** [README.md](https://github.com/bulletphysics/bullet3/blob/d3afe76132fc76b0f9b2359cbaef47a3766e7fbb/README.md) · [LICENSE.txt](https://github.com/bulletphysics/bullet3/blob/d3afe76132fc76b0f9b2359cbaef47a3766e7fbb/LICENSE.txt) · [pyproject.toml](https://github.com/bulletphysics/bullet3/blob/d3afe76132fc76b0f9b2359cbaef47a3766e7fbb/pyproject.toml) · [CMakeLists.txt](https://github.com/bulletphysics/bullet3/blob/d3afe76132fc76b0f9b2359cbaef47a3766e7fbb/CMakeLists.txt) · [.github/workflows/cmake.yml](https://github.com/bulletphysics/bullet3/blob/d3afe76132fc76b0f9b2359cbaef47a3766e7fbb/.github/workflows/cmake.yml) · [metadata GitHub](https://api.github.com/repos/bulletphysics/bullet3).

<a id="anhkysuai-2026-11-23-assimp-assimp"></a>

### assimp

**Repo:** [assimp/assimp](https://github.com/assimp/assimp) · **License:** BSD-3-Clause (mã chính); test/models-nonbsd có ngoại lệ · **★ 13,337 (GitHub API, 2026-11-23)**

**Mục đích:** Thư viện C/C++ nhập nhiều định dạng mô hình 3D vào cấu trúc thống nhất và xử lý mesh.

**Giá trị:** Hữu ích cho pipeline asset cần chuẩn hóa dữ liệu, normals, triangulation hoặc loại bỏ đỉnh trùng.

**Giới hạn:** Giấy phép BSD-3-Clause của phần chính không bao gồm mọi model kiểm thử trong models-nonbsd; cần kiểm độ bảo toàn vật liệu/animation với định dạng đích và dữ liệu không tin cậy.

**Cách tham khảo/tích hợp:** Thử trên bản sao mô hình với đơn vị và dung sai đã biết, kiểm đầu ra/round-trip và quyền của từng thành phần trước đưa vào quy trình kỹ thuật.

**Lựa chọn để đối chiếu:** [google/draco](https://github.com/google/draco) · [cnr-isti-vclab/meshlab](https://github.com/cnr-isti-vclab/meshlab). Đây là ứng viên so sánh theo tác vụ; mức phù hợp cần kiểm theo hồ sơ và phiên bản riêng.

**Bằng chứng:** `docs-read`, ngày 2026-11-23, commit [`93fe5d82fb206e850a21809bf45800ae00b17fc7`](https://github.com/assimp/assimp/commit/93fe5d82fb206e850a21809bf45800ae00b17fc7), ngày commit 2026-11-20. Đã clone và đọc chọn lọc phần giới thiệu, cách dùng, giới hạn, license, metadata manifest và CI hiện diện. Chưa kiểm đầy đủ implementation hoặc chạy upstream; các số đo của tác giả chưa được tái lập.

**Nguồn:** [Readme.md](https://github.com/assimp/assimp/blob/93fe5d82fb206e850a21809bf45800ae00b17fc7/Readme.md) · [LICENSE](https://github.com/assimp/assimp/blob/93fe5d82fb206e850a21809bf45800ae00b17fc7/LICENSE) · [CMakeLists.txt](https://github.com/assimp/assimp/blob/93fe5d82fb206e850a21809bf45800ae00b17fc7/CMakeLists.txt) · [.github/workflows/cifuzz.yml](https://github.com/assimp/assimp/blob/93fe5d82fb206e850a21809bf45800ae00b17fc7/.github/workflows/cifuzz.yml) · [metadata GitHub](https://api.github.com/repos/assimp/assimp).

<a id="anhkysuai-2026-11-23-alicevision-meshroom"></a>

### Meshroom

**Repo:** [alicevision/Meshroom](https://github.com/alicevision/Meshroom) · **License:** MPL-2.0 (framework); plugin/phụ thuộc riêng · **★ 13,108 (GitHub API, 2026-11-23)**

**Mục đích:** Framework lập pipeline xử lý dữ liệu bằng đồ thị node, có plugin thị giác máy tính và tái dựng 3D.

**Giá trị:** Tài liệu mô tả cache trung gian và chỉ làm mất hiệu lực các node phía sau khi tham số đổi, phù hợp quy trình xử lý ảnh nhiều bước.

**Giới hạn:** MPL-2.0 của framework tách khỏi license plugin, model và phụ thuộc; yêu cầu GPU và độ chính xác tái dựng phải kiểm cho pipeline cụ thể, chưa được benchmark ở lượt này.

**Cách tham khảo/tích hợp:** Ghim phiên bản và nguồn dữ liệu, kiểm CRS, đơn vị và một tập mẫu có kết quả chuẩn trước tích hợp pipeline GIS.

**Lựa chọn để đối chiếu:** [OpenDroneMap/ODM](https://github.com/OpenDroneMap/ODM) · [openMVG/openMVG](https://github.com/openMVG/openMVG). Đây là ứng viên so sánh theo tác vụ; mức phù hợp cần kiểm theo hồ sơ và phiên bản riêng.

**Bằng chứng:** `docs-read`, ngày 2026-11-23, commit [`890a9969ec0794f0c8b895f8af780a5beceb9f9f`](https://github.com/alicevision/Meshroom/commit/890a9969ec0794f0c8b895f8af780a5beceb9f9f), ngày commit 2026-11-22. Đã clone và đọc chọn lọc phần giới thiệu, cách dùng, giới hạn, license, metadata manifest và CI hiện diện. Chưa kiểm đầy đủ implementation hoặc chạy upstream; các số đo của tác giả chưa được tái lập.

**Nguồn:** [README.md](https://github.com/alicevision/Meshroom/blob/890a9969ec0794f0c8b895f8af780a5beceb9f9f/README.md) · [COPYING.md](https://github.com/alicevision/Meshroom/blob/890a9969ec0794f0c8b895f8af780a5beceb9f9f/COPYING.md) · [LICENSE-MPL2.md](https://github.com/alicevision/Meshroom/blob/890a9969ec0794f0c8b895f8af780a5beceb9f9f/LICENSE-MPL2.md) · [CMakeLists.txt](https://github.com/alicevision/Meshroom/blob/890a9969ec0794f0c8b895f8af780a5beceb9f9f/CMakeLists.txt) · [.github/workflows/run-tests.yml](https://github.com/alicevision/Meshroom/blob/890a9969ec0794f0c8b895f8af780a5beceb9f9f/.github/workflows/run-tests.yml) · [metadata GitHub](https://api.github.com/repos/alicevision/Meshroom).

<a id="anhkysuai-2026-11-23-jrouwe-joltphysics"></a>

### JoltPhysics

**Repo:** [jrouwe/JoltPhysics](https://github.com/jrouwe/JoltPhysics) · **License:** MIT · **★ 12,381 (GitHub API, 2026-11-23)**

**Mục đích:** Thư viện C++ mô phỏng vật rắn và va chạm, thiết kế chú trọng đa luồng cho game/VR.

**Giá trị:** Phần design considerations giải thích cách chia sẻ dữ liệu vật lý với các luồng khác, hữu ích khi nghiên cứu engine thời gian thực.

**Giới hạn:** Khả năng CPU, cấu hình build và độ xác định cần kiểm trên nền tảng đích; thành tích game hoặc benchmark upstream chưa được tái lập ở lượt này.

**Cách tham khảo/tích hợp:** Tách simulator khỏi adapter phần cứng, chọn dữ liệu chuẩn để kiểm độ đúng và sai số trước sử dụng thực tế.

**Lựa chọn để đối chiếu:** [bulletphysics/bullet3](https://github.com/bulletphysics/bullet3) · [google-deepmind/mujoco](https://github.com/google-deepmind/mujoco). Đây là ứng viên so sánh theo tác vụ; mức phù hợp cần kiểm theo hồ sơ và phiên bản riêng.

**Bằng chứng:** `docs-read`, ngày 2026-11-23, commit [`1a14e5e68d25c425a70fd1f04dcad21339176615`](https://github.com/jrouwe/JoltPhysics/commit/1a14e5e68d25c425a70fd1f04dcad21339176615), ngày commit 2026-11-21. Đã clone và đọc chọn lọc phần giới thiệu, cách dùng, giới hạn, license, metadata manifest và CI hiện diện. Chưa kiểm đầy đủ implementation hoặc chạy upstream; các số đo của tác giả chưa được tái lập.

**Nguồn:** [README.md](https://github.com/jrouwe/JoltPhysics/blob/1a14e5e68d25c425a70fd1f04dcad21339176615/README.md) · [LICENSE](https://github.com/jrouwe/JoltPhysics/blob/1a14e5e68d25c425a70fd1f04dcad21339176615/LICENSE) · [.github/workflows/build.yml](https://github.com/jrouwe/JoltPhysics/blob/1a14e5e68d25c425a70fd1f04dcad21339176615/.github/workflows/build.yml) · [metadata GitHub](https://api.github.com/repos/jrouwe/JoltPhysics).

<a id="anhkysuai-2026-11-23-keplergl-kepler.gl"></a>

### kepler.gl

**Repo:** [keplergl/kepler.gl](https://github.com/keplergl/kepler.gl) · **License:** MIT · **★ 12,105 (GitHub API, 2026-11-23)**

**Mục đích:** Ứng dụng và component React/Redux khám phá trực quan dữ liệu địa lý trên web.

**Giá trị:** Kết hợp MapLibre và deck.gl, nhiều lớp dữ liệu và cấu hình UI giúp tạo dashboard không gian.

**Giới hạn:** Manifest ở SHA đã đọc là 3.3.0-alpha.27; khả năng hàng triệu điểm là tuyên bố upstream cần đo lại. Basemap, dữ liệu và token nhà cung cấp có quyền riêng.

**Cách tham khảo/tích hợp:** Ghim phiên bản và nguồn dữ liệu, kiểm CRS, đơn vị và một tập mẫu có kết quả chuẩn trước tích hợp pipeline GIS.

**Lựa chọn để đối chiếu:** [CesiumGS/cesium](https://github.com/CesiumGS/cesium) · [opengeos/GeoLibre](https://github.com/opengeos/GeoLibre). Đây là ứng viên so sánh theo tác vụ; mức phù hợp cần kiểm theo hồ sơ và phiên bản riêng.

**Bằng chứng:** `docs-read`, ngày 2026-11-23, commit [`229456eb089a2db71584c02ba39dce20bcc5b989`](https://github.com/keplergl/kepler.gl/commit/229456eb089a2db71584c02ba39dce20bcc5b989), ngày commit 2026-11-23. Đã clone và đọc chọn lọc phần giới thiệu, cách dùng, giới hạn, license, metadata manifest và CI hiện diện. Chưa kiểm đầy đủ implementation hoặc chạy upstream; các số đo của tác giả chưa được tái lập.

**Nguồn:** [README.md](https://github.com/keplergl/kepler.gl/blob/229456eb089a2db71584c02ba39dce20bcc5b989/README.md) · [LICENSE](https://github.com/keplergl/kepler.gl/blob/229456eb089a2db71584c02ba39dce20bcc5b989/LICENSE) · [package.json](https://github.com/keplergl/kepler.gl/blob/229456eb089a2db71584c02ba39dce20bcc5b989/package.json) · [.github/workflows/test.yml](https://github.com/keplergl/kepler.gl/blob/229456eb089a2db71584c02ba39dce20bcc5b989/.github/workflows/test.yml) · [metadata GitHub](https://api.github.com/repos/keplergl/kepler.gl).

<a id="anhkysuai-2026-11-23-pointcloudlibrary-pcl"></a>

### Point Cloud Library

**Repo:** [PointCloudLibrary/pcl](https://github.com/PointCloudLibrary/pcl) · **License:** BSD-3-Clause · **★ 11,230 (GitHub API, 2026-11-23)**

**Mục đích:** Thư viện C++ xử lý point cloud cho ứng dụng hình học và nhận thức 3D.

**Giá trị:** Nền tảng chuyên dụng để xây pipeline đám mây điểm; repo công bố tài liệu, CI và giấy phép BSD.

**Giới hạn:** README cảnh báo website cũ từng bị xâm nhập; nên dùng nguồn tài liệu hiện tại. Cần kiểm mật độ điểm, đơn vị, nhiễu và chi phí bộ nhớ với dữ liệu thực.

**Cách tham khảo/tích hợp:** Ghim phiên bản và nguồn dữ liệu, kiểm CRS, đơn vị và một tập mẫu có kết quả chuẩn trước tích hợp pipeline GIS.

**Lựa chọn để đối chiếu:** [isl-org/Open3D](https://github.com/isl-org/Open3D) · [cnr-isti-vclab/meshlab](https://github.com/cnr-isti-vclab/meshlab). Đây là ứng viên so sánh theo tác vụ; mức phù hợp cần kiểm theo hồ sơ và phiên bản riêng.

**Bằng chứng:** `docs-read`, ngày 2026-11-23, commit [`fd39f32af932d50e033dba17b29e6d5fa4f64255`](https://github.com/PointCloudLibrary/pcl/commit/fd39f32af932d50e033dba17b29e6d5fa4f64255), ngày commit 2026-11-14. Đã clone và đọc chọn lọc phần giới thiệu, cách dùng, giới hạn, license, metadata manifest và CI hiện diện. Chưa kiểm đầy đủ implementation hoặc chạy upstream; các số đo của tác giả chưa được tái lập.

**Nguồn:** [README.md](https://github.com/PointCloudLibrary/pcl/blob/fd39f32af932d50e033dba17b29e6d5fa4f64255/README.md) · [LICENSE.txt](https://github.com/PointCloudLibrary/pcl/blob/fd39f32af932d50e033dba17b29e6d5fa4f64255/LICENSE.txt) · [CMakeLists.txt](https://github.com/PointCloudLibrary/pcl/blob/fd39f32af932d50e033dba17b29e6d5fa4f64255/CMakeLists.txt) · [.github/workflows/clang-tidy.yml](https://github.com/PointCloudLibrary/pcl/blob/fd39f32af932d50e033dba17b29e6d5fa4f64255/.github/workflows/clang-tidy.yml) · [metadata GitHub](https://api.github.com/repos/PointCloudLibrary/pcl).

<a id="anhkysuai-2026-11-23-turfjs-turf"></a>

### turf

**Repo:** [Turfjs/turf](https://github.com/Turfjs/turf) · **License:** MIT · **★ 10,553 (GitHub API, 2026-11-23)**

**Mục đích:** Engine phân tích không gian dạng mô-đun bằng JavaScript/TypeScript, thao tác GeoJSON.

**Giá trị:** Chạy được trong trình duyệt và Node.js, thuận tiện bổ sung phép đo, thao tác hình học và thống kê cho ứng dụng bản đồ.

**Giới hạn:** Cần kiểm đơn vị, hệ tọa độ, trường hợp hình học không hợp lệ và độ chính xác của từng phép; không suy tính đúng từ việc có cấu hình test trong repo.

**Cách tham khảo/tích hợp:** Ghim phiên bản và nguồn dữ liệu, kiểm CRS, đơn vị và một tập mẫu có kết quả chuẩn trước tích hợp pipeline GIS.

**Lựa chọn để đối chiếu:** [geopandas/geopandas](https://github.com/geopandas/geopandas) · [OSGeo/gdal](https://github.com/OSGeo/gdal). Đây là ứng viên so sánh theo tác vụ; mức phù hợp cần kiểm theo hồ sơ và phiên bản riêng.

**Bằng chứng:** `docs-read`, ngày 2026-11-23, commit [`938a6c6318b444636e086985c0d29cec19f5329b`](https://github.com/Turfjs/turf/commit/938a6c6318b444636e086985c0d29cec19f5329b), ngày commit 2026-11-17. Đã clone và đọc chọn lọc phần giới thiệu, cách dùng, giới hạn, license, metadata manifest và CI hiện diện. Chưa kiểm đầy đủ implementation hoặc chạy upstream; các số đo của tác giả chưa được tái lập.

**Nguồn:** [README.md](https://github.com/Turfjs/turf/blob/938a6c6318b444636e086985c0d29cec19f5329b/README.md) · [LICENSE](https://github.com/Turfjs/turf/blob/938a6c6318b444636e086985c0d29cec19f5329b/LICENSE) · [package.json](https://github.com/Turfjs/turf/blob/938a6c6318b444636e086985c0d29cec19f5329b/package.json) · [.github/workflows/ci.yml](https://github.com/Turfjs/turf/blob/938a6c6318b444636e086985c0d29cec19f5329b/.github/workflows/ci.yml) · [metadata GitHub](https://api.github.com/repos/Turfjs/turf).

<a id="anhkysuai-2026-11-23-satellite-image-deep-learning-techniques"></a>

### techniques

**Repo:** [satellite-image-deep-learning/techniques](https://github.com/satellite-image-deep-learning/techniques) · **License:** Apache-2.0 · **★ 10,312 (GitHub API, 2026-11-23)**

**Mục đích:** Chỉ mục kỹ thuật deep learning cho ảnh vệ tinh và ảnh hàng không, phân nhóm theo nhiệm vụ.

**Giá trị:** Hữu ích tìm paper/model cho classification, segmentation và detection theo loại đối tượng hoặc hiện tượng.

**Giới hạn:** Apache-2.0 của danh sách không bao gồm model, dataset hay paper liên kết; kết quả công bố cần kiểm điều kiện địa lý, cảm biến, phân bố dữ liệu và benchmark riêng.

**Cách tham khảo/tích hợp:** Dùng làm chỉ mục tìm ứng viên, dẫn về nguồn gốc rồi kiểm phiên bản, giấy phép và mức bảo trì của từng lựa chọn trước tích hợp.

**Lựa chọn để đối chiếu:** [sshuair/awesome-gis](https://github.com/sshuair/awesome-gis) · [sacridini/Awesome-Geospatial](https://github.com/sacridini/Awesome-Geospatial). Đây là ứng viên so sánh theo tác vụ; mức phù hợp cần kiểm theo hồ sơ và phiên bản riêng.

**Bằng chứng:** `docs-read`, ngày 2026-11-23, commit [`2ac02750505b174dc5cdab1b8eccf68cb803eb41`](https://github.com/satellite-image-deep-learning/techniques/commit/2ac02750505b174dc5cdab1b8eccf68cb803eb41), ngày commit 2026-11-21. Đã clone và đọc chọn lọc phần giới thiệu, cách dùng, giới hạn, license, metadata manifest và CI hiện diện. Chưa kiểm đầy đủ implementation hoặc chạy upstream; các số đo của tác giả chưa được tái lập.

**Nguồn:** [README.md](https://github.com/satellite-image-deep-learning/techniques/blob/2ac02750505b174dc5cdab1b8eccf68cb803eb41/README.md) · [LICENSE](https://github.com/satellite-image-deep-learning/techniques/blob/2ac02750505b174dc5cdab1b8eccf68cb803eb41/LICENSE) · [.github/workflows/action.yml](https://github.com/satellite-image-deep-learning/techniques/blob/2ac02750505b174dc5cdab1b8eccf68cb803eb41/.github/workflows/action.yml) · [metadata GitHub](https://api.github.com/repos/satellite-image-deep-learning/techniques).

<a id="anhkysuai-2026-11-23-opengeos-geolibre"></a>

### GeoLibre

**Repo:** [opengeos/GeoLibre](https://github.com/opengeos/GeoLibre) · **License:** MIT · **★ 8,778 (GitHub API, 2026-11-23)**

**Mục đích:** Nền tảng GIS dùng chung workspace trên web, desktop, mobile và notebook, có xử lý WebAssembly.

**Giá trị:** Kết hợp bản đồ, DuckDB-WASM và công cụ địa lý trong giao diện chung, phù hợp khám phá dữ liệu tại máy.

**Giới hạn:** Tuyên bố xử lý hoàn toàn local phải kiểm theo công cụ/lớp dữ liệu thực dùng; basemap hoặc endpoint ngoài có thể có quyền/luồng dữ liệu riêng. Chưa xác minh số lượng và hiệu năng công cụ quảng bá.

**Cách tham khảo/tích hợp:** Ghim phiên bản và nguồn dữ liệu, kiểm CRS, đơn vị và một tập mẫu có kết quả chuẩn trước tích hợp pipeline GIS.

**Lựa chọn để đối chiếu:** [keplergl/kepler.gl](https://github.com/keplergl/kepler.gl) · [geopandas/geopandas](https://github.com/geopandas/geopandas). Đây là ứng viên so sánh theo tác vụ; mức phù hợp cần kiểm theo hồ sơ và phiên bản riêng.

**Bằng chứng:** `docs-read`, ngày 2026-11-23, commit [`a7b8e10a19c43f71b134a97777aedcb4d8217246`](https://github.com/opengeos/GeoLibre/commit/a7b8e10a19c43f71b134a97777aedcb4d8217246), ngày commit 2026-11-23. Đã clone và đọc chọn lọc phần giới thiệu, cách dùng, giới hạn, license, metadata manifest và CI hiện diện. Chưa kiểm đầy đủ implementation hoặc chạy upstream; các số đo của tác giả chưa được tái lập.

**Nguồn:** [README.md](https://github.com/opengeos/GeoLibre/blob/a7b8e10a19c43f71b134a97777aedcb4d8217246/README.md) · [LICENSE](https://github.com/opengeos/GeoLibre/blob/a7b8e10a19c43f71b134a97777aedcb4d8217246/LICENSE) · [package.json](https://github.com/opengeos/GeoLibre/blob/a7b8e10a19c43f71b134a97777aedcb4d8217246/package.json) · [.github/workflows/ci.yml](https://github.com/opengeos/GeoLibre/blob/a7b8e10a19c43f71b134a97777aedcb4d8217246/.github/workflows/ci.yml) · [metadata GitHub](https://api.github.com/repos/opengeos/GeoLibre).

<a id="anhkysuai-2026-11-23-google-draco"></a>

### Draco

**Repo:** [google/draco](https://github.com/google/draco) · **License:** Apache-2.0 · **★ 7,565 (GitHub API, 2026-11-23)**

**Mục đích:** Thư viện nén/giải nén mesh và point cloud 3D để giảm lưu trữ và truyền dữ liệu.

**Giá trị:** Có C++ và decoder JavaScript/WASM, phù hợp pipeline asset web hoặc truyền mô hình.

**Giới hạn:** README khuyên ghim URL decoder theo phiên bản vì cache của đường dẫn chung có thể gây lỗi khi phát hành; cần đo tỷ lệ nén, sai số lượng tử hóa và tương thích encoder/decoder.

**Cách tham khảo/tích hợp:** Ghim phiên bản và nguồn dữ liệu, kiểm CRS, đơn vị và một tập mẫu có kết quả chuẩn trước tích hợp pipeline GIS.

**Lựa chọn để đối chiếu:** [assimp/assimp](https://github.com/assimp/assimp) · [zeux/meshoptimizer](https://github.com/zeux/meshoptimizer). Đây là ứng viên so sánh theo tác vụ; mức phù hợp cần kiểm theo hồ sơ và phiên bản riêng.

**Bằng chứng:** `docs-read`, ngày 2026-11-23, commit [`d6c1acf366a9c8745e6f1e96d94c2ddcad279e21`](https://github.com/google/draco/commit/d6c1acf366a9c8745e6f1e96d94c2ddcad279e21), ngày commit 2026-11-16. Đã clone và đọc chọn lọc phần giới thiệu, cách dùng, giới hạn, license, metadata manifest và CI hiện diện. Chưa kiểm đầy đủ implementation hoặc chạy upstream; các số đo của tác giả chưa được tái lập.

**Nguồn:** [README.md](https://github.com/google/draco/blob/d6c1acf366a9c8745e6f1e96d94c2ddcad279e21/README.md) · [LICENSE](https://github.com/google/draco/blob/d6c1acf366a9c8745e6f1e96d94c2ddcad279e21/LICENSE) · [CMakeLists.txt](https://github.com/google/draco/blob/d6c1acf366a9c8745e6f1e96d94c2ddcad279e21/CMakeLists.txt) · [.github/workflows/ci.yml](https://github.com/google/draco/blob/d6c1acf366a9c8745e6f1e96d94c2ddcad279e21/.github/workflows/ci.yml) · [metadata GitHub](https://api.github.com/repos/google/draco).

<a id="anhkysuai-2026-11-23-opendronemap-odm"></a>

### ODM

**Repo:** [OpenDroneMap/ODM](https://github.com/OpenDroneMap/ODM) · **License:** AGPL-3.0 · **★ 6,634 (GitHub API, 2026-11-23)**

**Mục đích:** Bộ CLI xử lý ảnh drone thành point cloud, mô hình 3D, ảnh trực giao và mô hình độ cao.

**Giá trị:** Có thể ghép vào pipeline xử lý ảnh tự động nhờ đầu ra hình học và địa lý đa dạng.

**Giới hạn:** Cần dữ liệu chụp phù hợp, tài nguyên tính toán và kiểm độ chính xác tọa độ bằng mốc độc lập; AGPL và tài sản/ứng dụng desktop khác cần đối chiếu riêng.

**Cách tham khảo/tích hợp:** Ghim phiên bản và nguồn dữ liệu, kiểm CRS, đơn vị và một tập mẫu có kết quả chuẩn trước tích hợp pipeline GIS.

**Lựa chọn để đối chiếu:** [alicevision/Meshroom](https://github.com/alicevision/Meshroom) · [openMVG/openMVG](https://github.com/openMVG/openMVG). Đây là ứng viên so sánh theo tác vụ; mức phù hợp cần kiểm theo hồ sơ và phiên bản riêng.

**Bằng chứng:** `docs-read`, ngày 2026-11-23, commit [`9078435bbdbfa37622e4e99e7856ed0a7a23e017`](https://github.com/OpenDroneMap/ODM/commit/9078435bbdbfa37622e4e99e7856ed0a7a23e017), ngày commit 2026-11-11. Đã clone và đọc chọn lọc phần giới thiệu, cách dùng, giới hạn, license, metadata manifest và CI hiện diện. Chưa kiểm đầy đủ implementation hoặc chạy upstream; các số đo của tác giả chưa được tái lập.

**Nguồn:** [README.md](https://github.com/OpenDroneMap/ODM/blob/9078435bbdbfa37622e4e99e7856ed0a7a23e017/README.md) · [LICENSE](https://github.com/OpenDroneMap/ODM/blob/9078435bbdbfa37622e4e99e7856ed0a7a23e017/LICENSE) · [.github/workflows/native-builds.yaml](https://github.com/OpenDroneMap/ODM/blob/9078435bbdbfa37622e4e99e7856ed0a7a23e017/.github/workflows/native-builds.yaml) · [metadata GitHub](https://api.github.com/repos/OpenDroneMap/ODM).

<a id="anhkysuai-2026-11-23-librecad-librecad"></a>

### LibreCAD

**Repo:** [LibreCAD/LibreCAD](https://github.com/LibreCAD/LibreCAD) · **License:** GPL-2.0 (toàn thể); thành phần/tài sản riêng · **★ 6,631 (GitHub API, 2026-11-23)**

**Mục đích:** Ứng dụng CAD 2D dựa trên Qt, hỗ trợ bản vẽ kỹ thuật và nhiều định dạng xuất/nhập.

**Giá trị:** Có giá trị cho soạn và kiểm bản vẽ 2D; tài liệu phân tách nhánh phát triển, release và công cụ chuyển đổi.

**Giới hạn:** Master là bản trước phát hành theo README; cần kiểm round-trip DXF/DWG, font và đơn vị. Toàn thể GPLv2, tài sản và thư viện đi kèm có các giấy phép riêng.

**Cách tham khảo/tích hợp:** Thử trên bản sao mô hình với đơn vị và dung sai đã biết, kiểm đầu ra/round-trip và quyền của từng thành phần trước đưa vào quy trình kỹ thuật.

**Lựa chọn để đối chiếu:** [qcad/qcad](https://github.com/qcad/qcad) · [FreeCAD/FreeCAD](https://github.com/FreeCAD/FreeCAD). Đây là ứng viên so sánh theo tác vụ; mức phù hợp cần kiểm theo hồ sơ và phiên bản riêng.

**Bằng chứng:** `docs-read`, ngày 2026-11-23, commit [`954217a719f7fff1f54bdf4ee894a0e462e21934`](https://github.com/LibreCAD/LibreCAD/commit/954217a719f7fff1f54bdf4ee894a0e462e21934), ngày commit 2026-11-22. Đã clone và đọc chọn lọc phần giới thiệu, cách dùng, giới hạn, license, metadata manifest và CI hiện diện. Chưa kiểm đầy đủ implementation hoặc chạy upstream; các số đo của tác giả chưa được tái lập.

**Nguồn:** [README.md](https://github.com/LibreCAD/LibreCAD/blob/954217a719f7fff1f54bdf4ee894a0e462e21934/README.md) · [LICENSE](https://github.com/LibreCAD/LibreCAD/blob/954217a719f7fff1f54bdf4ee894a0e462e21934/LICENSE) · [CMakeLists.txt](https://github.com/LibreCAD/LibreCAD/blob/954217a719f7fff1f54bdf4ee894a0e462e21934/CMakeLists.txt) · [.github/workflows/build-all.yml](https://github.com/LibreCAD/LibreCAD/blob/954217a719f7fff1f54bdf4ee894a0e462e21934/.github/workflows/build-all.yml) · [metadata GitHub](https://api.github.com/repos/LibreCAD/LibreCAD).

<a id="anhkysuai-2026-11-23-openmvg-openmvg"></a>

### openMVG

**Repo:** [openMVG/openMVG](https://github.com/openMVG/openMVG) · **License:** MPL-2.0 · **★ 6,606 (GitHub API, 2026-11-23)**

**Mục đích:** Framework C++ hình học đa góc nhìn và Structure from Motion để tái dựng 3D từ ảnh.

**Giá trị:** Phân tách thư viện, binary và pipeline hỗ trợ nghiên cứu thuật toán camera, ghép đặc trưng và hình học nhiều ảnh.

**Giới hạn:** MPL-2.0 của OpenMVG đi kèm danh mục phụ thuộc riêng; độ tin cậy phải kiểm với calibration, ảnh và ground truth của bài toán, không suy từ tuyên bố test-driven.

**Cách tham khảo/tích hợp:** Ghim phiên bản và nguồn dữ liệu, kiểm CRS, đơn vị và một tập mẫu có kết quả chuẩn trước tích hợp pipeline GIS.

**Lựa chọn để đối chiếu:** [alicevision/Meshroom](https://github.com/alicevision/Meshroom) · [colmap/colmap](https://github.com/colmap/colmap). Đây là ứng viên so sánh theo tác vụ; mức phù hợp cần kiểm theo hồ sơ và phiên bản riêng.

**Bằng chứng:** `docs-read`, ngày 2026-11-23, commit [`e0162aef9a5ba6ec9f54c39ed49ea47a0e82e1db`](https://github.com/openMVG/openMVG/commit/e0162aef9a5ba6ec9f54c39ed49ea47a0e82e1db), ngày commit 2026-11-06. Đã clone và đọc chọn lọc phần giới thiệu, cách dùng, giới hạn, license, metadata manifest và CI hiện diện. Chưa kiểm đầy đủ implementation hoặc chạy upstream; các số đo của tác giả chưa được tái lập.

**Nguồn:** [README.md](https://github.com/openMVG/openMVG/blob/e0162aef9a5ba6ec9f54c39ed49ea47a0e82e1db/README.md) · [COPYRIGHT.md](https://github.com/openMVG/openMVG/blob/e0162aef9a5ba6ec9f54c39ed49ea47a0e82e1db/COPYRIGHT.md) · [LICENSE](https://github.com/openMVG/openMVG/blob/e0162aef9a5ba6ec9f54c39ed49ea47a0e82e1db/LICENSE) · [.github/workflows/compile_and_run_test.yml](https://github.com/openMVG/openMVG/blob/e0162aef9a5ba6ec9f54c39ed49ea47a0e82e1db/.github/workflows/compile_and_run_test.yml) · [metadata GitHub](https://api.github.com/repos/openMVG/openMVG).

<a id="anhkysuai-2026-11-23-osgeo-gdal"></a>

### GDAL

**Repo:** [OSGeo/gdal](https://github.com/OSGeo/gdal) · **License:** MIT (chính); thành phần/driver xem LICENSE.TXT · **★ 6,173 (GitHub API, 2026-11-23)**

**Mục đích:** Thư viện và công cụ chuyển đổi dữ liệu địa lý raster/vector theo nhiều định dạng.

**Giá trị:** Là lớp tích hợp hữu ích giữa định dạng dữ liệu và pipeline GIS; tài liệu nêu cách build, image và chính sách bảo mật.

**Giới hạn:** MIT là giấy phép chính, LICENSE.TXT tổng hợp nhiều thành phần; driver/build quyết định tính năng thực có. Cần kiểm CRS, nodata, độ chính xác và dữ liệu đầu vào không tin cậy.

**Cách tham khảo/tích hợp:** Ghim phiên bản và nguồn dữ liệu, kiểm CRS, đơn vị và một tập mẫu có kết quả chuẩn trước tích hợp pipeline GIS.

**Lựa chọn để đối chiếu:** [geopandas/geopandas](https://github.com/geopandas/geopandas) · [Turfjs/turf](https://github.com/Turfjs/turf). Đây là ứng viên so sánh theo tác vụ; mức phù hợp cần kiểm theo hồ sơ và phiên bản riêng.

**Bằng chứng:** `docs-read`, ngày 2026-11-23, commit [`6d7a6388745ef760b68d3ea460d700f4be5479c4`](https://github.com/OSGeo/gdal/commit/6d7a6388745ef760b68d3ea460d700f4be5479c4), ngày commit 2026-11-22. Đã clone và đọc chọn lọc phần giới thiệu, cách dùng, giới hạn, license, metadata manifest và CI hiện diện. Chưa kiểm đầy đủ implementation hoặc chạy upstream; các số đo của tác giả chưa được tái lập.

**Nguồn:** [README.md](https://github.com/OSGeo/gdal/blob/6d7a6388745ef760b68d3ea460d700f4be5479c4/README.md) · [LICENSE.TXT](https://github.com/OSGeo/gdal/blob/6d7a6388745ef760b68d3ea460d700f4be5479c4/LICENSE.TXT) · [CMakeLists.txt](https://github.com/OSGeo/gdal/blob/6d7a6388745ef760b68d3ea460d700f4be5479c4/CMakeLists.txt) · [.github/workflows/cifuzz.yml](https://github.com/OSGeo/gdal/blob/6d7a6388745ef760b68d3ea460d700f4be5479c4/.github/workflows/cifuzz.yml) · [metadata GitHub](https://api.github.com/repos/OSGeo/gdal).

<a id="anhkysuai-2026-11-23-cgal-cgal"></a>

### CGAL

**Repo:** [CGAL/cgal](https://github.com/CGAL/cgal) · **License:** GPL/LGPL theo package, hoặc thương mại; xem Installation/LICENSE · **★ 6,137 (GitHub API, 2026-11-23)**

**Mục đích:** Thư viện C++ thuật toán hình học tính toán, dạng header-only từ dòng 5.x.

**Giá trị:** Cung cấp nền tảng cho bài toán hình học cần thuật toán chuyên dụng; repo tách cấu trúc phát triển khỏi tarball phát hành.

**Giới hạn:** Giấy phép phải kiểm theo package trong Installation/LICENSE và header; CC0 ở một số tệp ngoài tarball không đại diện toàn bộ thư viện. Cần kiểm kernel số học, độ chính xác và chi phí biên dịch.

**Cách tham khảo/tích hợp:** Ghim phiên bản và nguồn dữ liệu, kiểm CRS, đơn vị và một tập mẫu có kết quả chuẩn trước tích hợp pipeline GIS.

**Lựa chọn để đối chiếu:** [PointCloudLibrary/pcl](https://github.com/PointCloudLibrary/pcl) · [libigl/libigl](https://github.com/libigl/libigl). Đây là ứng viên so sánh theo tác vụ; mức phù hợp cần kiểm theo hồ sơ và phiên bản riêng.

**Bằng chứng:** `docs-read`, ngày 2026-11-23, commit [`a25894af4d4510d24c259940a69622b7502eef86`](https://github.com/CGAL/cgal/commit/a25894af4d4510d24c259940a69622b7502eef86), ngày commit 2026-11-22. Đã clone và đọc chọn lọc phần giới thiệu, cách dùng, giới hạn, license, metadata manifest và CI hiện diện. Chưa kiểm đầy đủ implementation hoặc chạy upstream; các số đo của tác giả chưa được tái lập.

**Nguồn:** [README.md](https://github.com/CGAL/cgal/blob/a25894af4d4510d24c259940a69622b7502eef86/README.md) · [LICENSE.md](https://github.com/CGAL/cgal/blob/a25894af4d4510d24c259940a69622b7502eef86/LICENSE.md) · [copyright](https://github.com/CGAL/cgal/blob/a25894af4d4510d24c259940a69622b7502eef86/copyright) · [CMakeLists.txt](https://github.com/CGAL/cgal/blob/a25894af4d4510d24c259940a69622b7502eef86/CMakeLists.txt) · [.github/workflows/checks.yml](https://github.com/CGAL/cgal/blob/a25894af4d4510d24c259940a69622b7502eef86/.github/workflows/checks.yml) · [Installation/LICENSE](https://github.com/CGAL/cgal/blob/a25894af4d4510d24c259940a69622b7502eef86/Installation/LICENSE) · [metadata GitHub](https://api.github.com/repos/CGAL/cgal).

<a id="anhkysuai-2026-11-23-cnr-isti-vclab-meshlab"></a>

### meshlab

**Repo:** [cnr-isti-vclab/meshlab](https://github.com/cnr-isti-vclab/meshlab) · **License:** GPL-3.0 · **★ 5,931 (GitHub API, 2026-11-23)**

**Mục đích:** Ứng dụng xử lý mesh tam giác 3D để chỉnh, làm sạch, kiểm tra, render và chuyển đổi.

**Giá trị:** Giao diện tương tác giúp thử thuật toán xử lý dữ liệu quét 3D trước khi thiết kế pipeline tự động.

**Giới hạn:** Cần giữ bản gốc và kiểm topology/đơn vị sau thao tác làm sạch; GPLv3 của ứng dụng không được suy từ BSL-1.0 chỉ xuất hiện ở tệp CMake.

**Cách tham khảo/tích hợp:** Ghim phiên bản và nguồn dữ liệu, kiểm CRS, đơn vị và một tập mẫu có kết quả chuẩn trước tích hợp pipeline GIS.

**Lựa chọn để đối chiếu:** [assimp/assimp](https://github.com/assimp/assimp) · [PointCloudLibrary/pcl](https://github.com/PointCloudLibrary/pcl). Đây là ứng viên so sánh theo tác vụ; mức phù hợp cần kiểm theo hồ sơ và phiên bản riêng.

**Bằng chứng:** `docs-read`, ngày 2026-11-23, commit [`71e7b0b53cd98f520f84cb17b31bac6f1ef947cc`](https://github.com/cnr-isti-vclab/meshlab/commit/71e7b0b53cd98f520f84cb17b31bac6f1ef947cc), ngày commit 2026-07-24. Đã clone và đọc chọn lọc phần giới thiệu, cách dùng, giới hạn, license, metadata manifest và CI hiện diện. Chưa kiểm đầy đủ implementation hoặc chạy upstream; các số đo của tác giả chưa được tái lập.

**Nguồn:** [README.md](https://github.com/cnr-isti-vclab/meshlab/blob/71e7b0b53cd98f520f84cb17b31bac6f1ef947cc/README.md) · [LICENSE.txt](https://github.com/cnr-isti-vclab/meshlab/blob/71e7b0b53cd98f520f84cb17b31bac6f1ef947cc/LICENSE.txt) · [CMakeLists.txt](https://github.com/cnr-isti-vclab/meshlab/blob/71e7b0b53cd98f520f84cb17b31bac6f1ef947cc/CMakeLists.txt) · [.github/workflows/BuildMeshLab.yml](https://github.com/cnr-isti-vclab/meshlab/blob/71e7b0b53cd98f520f84cb17b31bac6f1ef947cc/.github/workflows/BuildMeshLab.yml) · [metadata GitHub](https://api.github.com/repos/cnr-isti-vclab/meshlab).

<a id="anhkysuai-2026-11-23-gboeing-osmnx"></a>

### osmnx

**Repo:** [gboeing/osmnx](https://github.com/gboeing/osmnx) · **License:** MIT · **★ 5,908 (GitHub API, 2026-11-23)**

**Mục đích:** Gói Python tải, mô hình hóa và phân tích mạng đường phố cùng dữ liệu OpenStreetMap.

**Giá trị:** Hỗ trợ nghiên cứu mạng đi bộ, xe đạp, lái xe và tiện ích đô thị trong một quy trình Python.

**Giới hạn:** MIT cấp quyền mã, dữ liệu OpenStreetMap có yêu cầu attribution riêng; cần kiểm độ đầy đủ, thời điểm dữ liệu và giả định routing/travel time trước sử dụng quyết định thực tế.

**Cách tham khảo/tích hợp:** Ghim phiên bản và nguồn dữ liệu, kiểm CRS, đơn vị và một tập mẫu có kết quả chuẩn trước tích hợp pipeline GIS.

**Lựa chọn để đối chiếu:** [geopandas/geopandas](https://github.com/geopandas/geopandas) · [Turfjs/turf](https://github.com/Turfjs/turf). Đây là ứng viên so sánh theo tác vụ; mức phù hợp cần kiểm theo hồ sơ và phiên bản riêng.

**Bằng chứng:** `docs-read`, ngày 2026-11-23, commit [`af346c03401c3f6960ae84617061fa5108533183`](https://github.com/gboeing/osmnx/commit/af346c03401c3f6960ae84617061fa5108533183), ngày commit 2026-11-18. Đã clone và đọc chọn lọc phần giới thiệu, cách dùng, giới hạn, license, metadata manifest và CI hiện diện. Chưa kiểm đầy đủ implementation hoặc chạy upstream; các số đo của tác giả chưa được tái lập.

**Nguồn:** [README.md](https://github.com/gboeing/osmnx/blob/af346c03401c3f6960ae84617061fa5108533183/README.md) · [LICENSE.txt](https://github.com/gboeing/osmnx/blob/af346c03401c3f6960ae84617061fa5108533183/LICENSE.txt) · [pyproject.toml](https://github.com/gboeing/osmnx/blob/af346c03401c3f6960ae84617061fa5108533183/pyproject.toml) · [.github/workflows/ci.yml](https://github.com/gboeing/osmnx/blob/af346c03401c3f6960ae84617061fa5108533183/.github/workflows/ci.yml) · [metadata GitHub](https://api.github.com/repos/gboeing/osmnx).

<a id="anhkysuai-2026-11-23-sshuair-awesome-gis"></a>

### awesome-gis

**Repo:** [sshuair/awesome-gis](https://github.com/sshuair/awesome-gis) · **License:** MIT · **★ 5,640 (GitHub API, 2026-11-23)**

**Mục đích:** Danh mục tài nguyên GIS gồm công cụ, dữ liệu, sách, khóa học và cộng đồng.

**Giá trị:** Phân nhóm desktop, web, remote sensing và deep learning giúp lập danh sách công cụ để khảo sát tiếp.

**Giới hạn:** MIT của danh sách không bao gồm dữ liệu và dịch vụ được dẫn; từng công cụ cần kiểm phiên bản, giấy phép và khả năng đáp ứng bài toán địa lý cụ thể.

**Cách tham khảo/tích hợp:** Dùng làm chỉ mục tìm ứng viên, dẫn về nguồn gốc rồi kiểm phiên bản, giấy phép và mức bảo trì của từng lựa chọn trước tích hợp.

**Lựa chọn để đối chiếu:** [sacridini/Awesome-Geospatial](https://github.com/sacridini/Awesome-Geospatial) · [satellite-image-deep-learning/techniques](https://github.com/satellite-image-deep-learning/techniques). Đây là ứng viên so sánh theo tác vụ; mức phù hợp cần kiểm theo hồ sơ và phiên bản riêng.

**Bằng chứng:** `docs-read`, ngày 2026-11-23, commit [`0f21c1f6aa9fcefb044456827e9eb8363135f392`](https://github.com/sshuair/awesome-gis/commit/0f21c1f6aa9fcefb044456827e9eb8363135f392), ngày commit 2026-07-21. Đã clone và đọc chọn lọc phần giới thiệu, cách dùng, giới hạn, license, metadata manifest và CI hiện diện. Chưa kiểm đầy đủ implementation hoặc chạy upstream; các số đo của tác giả chưa được tái lập.

**Nguồn:** [README.md](https://github.com/sshuair/awesome-gis/blob/0f21c1f6aa9fcefb044456827e9eb8363135f392/README.md) · [LICENSE](https://github.com/sshuair/awesome-gis/blob/0f21c1f6aa9fcefb044456827e9eb8363135f392/LICENSE) · [metadata GitHub](https://api.github.com/repos/sshuair/awesome-gis).

<a id="anhkysuai-2026-11-23-adam-cad-cadam"></a>

### CADAM

**Repo:** [Adam-CAD/CADAM](https://github.com/Adam-CAD/CADAM) · **License:** GPL-3.0 · **★ 5,455 (GitHub API, 2026-11-23)**

**Mục đích:** Ứng dụng web text/image-to-CAD tạo mô hình tham số OpenSCAD và xuất STL, SCAD, DXF.

**Giá trị:** Kết hợp sinh mẫu bằng AI với điều chỉnh kích thước, phù hợp thử ý tưởng mô hình sơ bộ.

**Giới hạn:** Quickstart có Supabase và cấu hình server/API nên không suy toàn bộ xử lý AI nằm offline dù dựng hình dùng WASM; mẫu sinh cần kiểm hình học, đơn vị và khả năng chế tạo.

**Cách tham khảo/tích hợp:** Thử trên bản sao mô hình với đơn vị và dung sai đã biết, kiểm đầu ra/round-trip và quyền của từng thành phần trước đưa vào quy trình kỹ thuật.

**Lựa chọn để đối chiếu:** [xiangechen/chili3d](https://github.com/xiangechen/chili3d) · [FreeCAD/FreeCAD](https://github.com/FreeCAD/FreeCAD). Đây là ứng viên so sánh theo tác vụ; mức phù hợp cần kiểm theo hồ sơ và phiên bản riêng.

**Bằng chứng:** `docs-read`, ngày 2026-11-23, commit [`e339e3ad85601bb1e23a5ff9c7f33b51ddf602f5`](https://github.com/Adam-CAD/CADAM/commit/e339e3ad85601bb1e23a5ff9c7f33b51ddf602f5), ngày commit 2026-10-14. Đã clone và đọc chọn lọc phần giới thiệu, cách dùng, giới hạn, license, metadata manifest và CI hiện diện. Chưa kiểm đầy đủ implementation hoặc chạy upstream; các số đo của tác giả chưa được tái lập.

**Nguồn:** [README.md](https://github.com/Adam-CAD/CADAM/blob/e339e3ad85601bb1e23a5ff9c7f33b51ddf602f5/README.md) · [LICENSE](https://github.com/Adam-CAD/CADAM/blob/e339e3ad85601bb1e23a5ff9c7f33b51ddf602f5/LICENSE) · [package.json](https://github.com/Adam-CAD/CADAM/blob/e339e3ad85601bb1e23a5ff9c7f33b51ddf602f5/package.json) · [metadata GitHub](https://api.github.com/repos/Adam-CAD/CADAM).

<a id="anhkysuai-2026-11-23-sacridini-awesome-geospatial"></a>

### Awesome-Geospatial

**Repo:** [sacridini/Awesome-Geospatial](https://github.com/sacridini/Awesome-Geospatial) · **License:** CC0-1.0 · **★ 5,387 (GitHub API, 2026-11-23)**

**Mục đích:** Danh sách công cụ phân tích địa lý, dữ liệu, thư viện và nền tảng theo nhóm ứng dụng.

**Giá trị:** Bao quát cả GIS, lidar, radar, cơ sở dữ liệu và mô hình không gian, hữu ích tìm hướng khảo sát.

**Giới hạn:** Danh sách có cả sản phẩm thương mại; CC0 không mở quyền của các sản phẩm/dataset liên kết. Cần kiểm nguồn gốc, bảo trì và khả năng tương tác từng lựa chọn.

**Cách tham khảo/tích hợp:** Dùng làm chỉ mục tìm ứng viên, dẫn về nguồn gốc rồi kiểm phiên bản, giấy phép và mức bảo trì của từng lựa chọn trước tích hợp.

**Lựa chọn để đối chiếu:** [sshuair/awesome-gis](https://github.com/sshuair/awesome-gis) · [opengeos/GeoLibre](https://github.com/opengeos/GeoLibre). Đây là ứng viên so sánh theo tác vụ; mức phù hợp cần kiểm theo hồ sơ và phiên bản riêng.

**Bằng chứng:** `docs-read`, ngày 2026-11-23, commit [`2a03232855b42ce405d41766e5a33a445b2d6f1a`](https://github.com/sacridini/Awesome-Geospatial/commit/2a03232855b42ce405d41766e5a33a445b2d6f1a), ngày commit 2026-11-18. Đã clone và đọc chọn lọc phần giới thiệu, cách dùng, giới hạn, license, metadata manifest và CI hiện diện. Chưa kiểm đầy đủ implementation hoặc chạy upstream; các số đo của tác giả chưa được tái lập.

**Nguồn:** [README.md](https://github.com/sacridini/Awesome-Geospatial/blob/2a03232855b42ce405d41766e5a33a445b2d6f1a/README.md) · [LICENSE](https://github.com/sacridini/Awesome-Geospatial/blob/2a03232855b42ce405d41766e5a33a445b2d6f1a/LICENSE) · [metadata GitHub](https://api.github.com/repos/sacridini/Awesome-Geospatial).

<a id="anhkysuai-2026-11-23-projectphysx-fluidx3d"></a>

### FluidX3D

**Repo:** [ProjectPhysX/FluidX3D](https://github.com/ProjectPhysX/FluidX3D) · **License:** Giấy phép phi thương mại tùy chỉnh; xem LICENSE.md · **★ 5,380 (GitHub API, 2026-11-23)**

**Mục đích:** Phần mềm CFD dùng lattice Boltzmann trên OpenCL cho CPU/GPU.

**Giá trị:** Tài liệu trình bày mô hình, tính toán và hiển thị cùng benchmark, hữu ích nghiên cứu mô phỏng dòng chảy.

**Giới hạn:** Giấy phép tùy chỉnh chỉ miễn phí cho phạm vi phi thương mại; tuyên bố nhanh nhất chưa được tái lập. Cần kiểm độ hội tụ, điều kiện biên và xác thực vật lý cho từng mô phỏng.

**Cách tham khảo/tích hợp:** Tách simulator khỏi adapter phần cứng, chọn dữ liệu chuẩn để kiểm độ đúng và sai số trước sử dụng thực tế.

**Lựa chọn để đối chiếu:** [OpenFOAM/OpenFOAM-dev](https://github.com/OpenFOAM/OpenFOAM-dev) · [bulletphysics/bullet3](https://github.com/bulletphysics/bullet3). Đây là ứng viên so sánh theo tác vụ; mức phù hợp cần kiểm theo hồ sơ và phiên bản riêng.

**Bằng chứng:** `docs-read`, ngày 2026-11-23, commit [`cc40a3837ede8d996eb1092b8584c360237b0797`](https://github.com/ProjectPhysX/FluidX3D/commit/cc40a3837ede8d996eb1092b8584c360237b0797), ngày commit 2026-11-15. Đã clone và đọc chọn lọc phần giới thiệu, cách dùng, giới hạn, license, metadata manifest và CI hiện diện. Chưa kiểm đầy đủ implementation hoặc chạy upstream; các số đo của tác giả chưa được tái lập.

**Nguồn:** [README.md](https://github.com/ProjectPhysX/FluidX3D/blob/cc40a3837ede8d996eb1092b8584c360237b0797/README.md) · [LICENSE.md](https://github.com/ProjectPhysX/FluidX3D/blob/cc40a3837ede8d996eb1092b8584c360237b0797/LICENSE.md) · [metadata GitHub](https://api.github.com/repos/ProjectPhysX/FluidX3D).

<a id="anhkysuai-2026-11-23-geopandas-geopandas"></a>

### geopandas

**Repo:** [geopandas/geopandas](https://github.com/geopandas/geopandas) · **License:** BSD-3-Clause · **★ 5,308 (GitHub API, 2026-11-23)**

**Mục đích:** Mở rộng pandas với GeoSeries/GeoDataFrame và phép toán hình học qua Shapely.

**Giá trị:** Cho phép kết hợp bảng dữ liệu với hình học và chuyển CRS trong cùng workflow phân tích Python.

**Giới hạn:** README nêu phép toán hình học theo mặt phẳng Cartesian; cần chọn CRS và đơn vị phù hợp, kiểm lệch hệ tọa độ trước tính diện tích/khoảng cách.

**Cách tham khảo/tích hợp:** Ghim phiên bản và nguồn dữ liệu, kiểm CRS, đơn vị và một tập mẫu có kết quả chuẩn trước tích hợp pipeline GIS.

**Lựa chọn để đối chiếu:** [Turfjs/turf](https://github.com/Turfjs/turf) · [OSGeo/gdal](https://github.com/OSGeo/gdal). Đây là ứng viên so sánh theo tác vụ; mức phù hợp cần kiểm theo hồ sơ và phiên bản riêng.

**Bằng chứng:** `docs-read`, ngày 2026-11-23, commit [`3e92048f628971d0ed24b512740fae82ed6376c5`](https://github.com/geopandas/geopandas/commit/3e92048f628971d0ed24b512740fae82ed6376c5), ngày commit 2026-11-19. Đã clone và đọc chọn lọc phần giới thiệu, cách dùng, giới hạn, license, metadata manifest và CI hiện diện. Chưa kiểm đầy đủ implementation hoặc chạy upstream; các số đo của tác giả chưa được tái lập.

**Nguồn:** [README.md](https://github.com/geopandas/geopandas/blob/3e92048f628971d0ed24b512740fae82ed6376c5/README.md) · [LICENSE.txt](https://github.com/geopandas/geopandas/blob/3e92048f628971d0ed24b512740fae82ed6376c5/LICENSE.txt) · [pyproject.toml](https://github.com/geopandas/geopandas/blob/3e92048f628971d0ed24b512740fae82ed6376c5/pyproject.toml) · [.github/workflows/tests.yaml](https://github.com/geopandas/geopandas/blob/3e92048f628971d0ed24b512740fae82ed6376c5/.github/workflows/tests.yaml) · [metadata GitHub](https://api.github.com/repos/geopandas/geopandas).

<a id="anhkysuai-2026-11-23-xiangechen-chili3d"></a>

### chili3d

**Repo:** [xiangechen/chili3d](https://github.com/xiangechen/chili3d) · **License:** AGPL-3.0 (app); LGPL-3.0 (cpp); Pro riêng · **★ 5,016 (GitHub API, 2026-11-23)**

**Mục đích:** Ứng dụng CAD 3D trong trình duyệt dùng OpenCascade/WASM, hỗ trợ tham số, direct modeling và AI.

**Giá trị:** Chung document và undo stack cho thao tác tay/AI giúp giữ mô hình có thể chỉnh tiếp sau khi sinh.

**Giới hạn:** AI gọi endpoint bằng khóa người dùng theo README, nên cần kiểm dữ liệu/khóa gửi đi; app AGPLv3, module cpp LGPLv3 và Pro có phạm vi thương mại riêng.

**Cách tham khảo/tích hợp:** Thử trên bản sao mô hình với đơn vị và dung sai đã biết, kiểm đầu ra/round-trip và quyền của từng thành phần trước đưa vào quy trình kỹ thuật.

**Lựa chọn để đối chiếu:** [Adam-CAD/CADAM](https://github.com/Adam-CAD/CADAM) · [jasonsutter87/sketchcraft](https://github.com/jasonsutter87/sketchcraft). Đây là ứng viên so sánh theo tác vụ; mức phù hợp cần kiểm theo hồ sơ và phiên bản riêng.

**Bằng chứng:** `docs-read`, ngày 2026-11-23, commit [`a7a176bab5706cb2376635ba7c070e37efbbd69e`](https://github.com/xiangechen/chili3d/commit/a7a176bab5706cb2376635ba7c070e37efbbd69e), ngày commit 2026-11-21. Đã clone và đọc chọn lọc phần giới thiệu, cách dùng, giới hạn, license, metadata manifest và CI hiện diện. Chưa kiểm đầy đủ implementation hoặc chạy upstream; các số đo của tác giả chưa được tái lập.

**Nguồn:** [README.md](https://github.com/xiangechen/chili3d/blob/a7a176bab5706cb2376635ba7c070e37efbbd69e/README.md) · [LICENSE](https://github.com/xiangechen/chili3d/blob/a7a176bab5706cb2376635ba7c070e37efbbd69e/LICENSE) · [package.json](https://github.com/xiangechen/chili3d/blob/a7a176bab5706cb2376635ba7c070e37efbbd69e/package.json) · [.github/workflows/main.yml](https://github.com/xiangechen/chili3d/blob/a7a176bab5706cb2376635ba7c070e37efbbd69e/.github/workflows/main.yml) · [metadata GitHub](https://api.github.com/repos/xiangechen/chili3d).

<a id="anhkysuai-2026-11-23-puran-water-autocad-mcp"></a>

### autocad-mcp

**Repo:** [puran-water/autocad-mcp](https://github.com/puran-water/autocad-mcp) · **License:** MIT · **★ 683 (GitHub API, 2026-11-23)**

**Mục đích:** MCP tích hợp AutoCAD LT hoặc xử lý DXF headless để đọc và sửa bản vẽ qua công cụ.

**Giá trị:** Tài liệu phân biệt backend, drawing được chỉ định và luồng revision, hữu ích nghiên cứu tự động hóa CAD có trạng thái.

**Giới hạn:** AutoCAD và yêu cầu nền tảng cấp phép riêng; README nói lệnh thành công không đồng nghĩa thiết kế được duyệt, không hỗ trợ tự chuyển document. Cần thử trên bản sao và kiểm undo/revision.

**Cách tham khảo/tích hợp:** Thử trên bản sao mô hình với đơn vị và dung sai đã biết, kiểm đầu ra/round-trip và quyền của từng thành phần trước đưa vào quy trình kỹ thuật.

**Lựa chọn để đối chiếu:** [mcp-servers-for-revit/mcp-servers-for-revit](https://github.com/mcp-servers-for-revit/mcp-servers-for-revit) · [LibreCAD/LibreCAD](https://github.com/LibreCAD/LibreCAD). Đây là ứng viên so sánh theo tác vụ; mức phù hợp cần kiểm theo hồ sơ và phiên bản riêng.

**Bằng chứng:** `docs-read`, ngày 2026-11-23, commit [`d8d537d295976f97e30d7eacdc71e6e440dd02b9`](https://github.com/puran-water/autocad-mcp/commit/d8d537d295976f97e30d7eacdc71e6e440dd02b9), ngày commit 2026-11-16. Đã clone và đọc chọn lọc phần giới thiệu, cách dùng, giới hạn, license, metadata manifest và CI hiện diện. Chưa kiểm đầy đủ implementation hoặc chạy upstream; các số đo của tác giả chưa được tái lập.

**Nguồn:** [README.md](https://github.com/puran-water/autocad-mcp/blob/d8d537d295976f97e30d7eacdc71e6e440dd02b9/README.md) · [LICENSE](https://github.com/puran-water/autocad-mcp/blob/d8d537d295976f97e30d7eacdc71e6e440dd02b9/LICENSE) · [pyproject.toml](https://github.com/puran-water/autocad-mcp/blob/d8d537d295976f97e30d7eacdc71e6e440dd02b9/pyproject.toml) · [.github/workflows/ci.yml](https://github.com/puran-water/autocad-mcp/blob/d8d537d295976f97e30d7eacdc71e6e440dd02b9/.github/workflows/ci.yml) · [metadata GitHub](https://api.github.com/repos/puran-water/autocad-mcp).

<a id="anhkysuai-2026-11-23-mcp-servers-for-revit-mcp-servers-for-revit"></a>

### MCP servers for Revit (Sparx fork)

**Repo:** [mcp-servers-for-revit/mcp-servers-for-revit](https://github.com/mcp-servers-for-revit/mcp-servers-for-revit) · **License:** MIT · **★ 464 (GitHub API, 2026-11-23)**

**Mục đích:** Fork MCP cho Autodesk Revit gồm server TypeScript, add-in C# và bộ lệnh Revit API.

**Giá trị:** Kiến trúc ba phần giúp nối AI với thao tác đọc/tạo/sửa/xóa phần tử BIM; có tài liệu test theo phiên bản.

**Giới hạn:** Yêu cầu Revit đã cài và có giấy phép; thao tác thay đổi mô hình cần giới hạn project, transaction và kiểm kết quả kỹ thuật. MIT của bridge không cấp quyền Revit.

**Cách tham khảo/tích hợp:** Thử trên bản sao mô hình với đơn vị và dung sai đã biết, kiểm đầu ra/round-trip và quyền của từng thành phần trước đưa vào quy trình kỹ thuật.

**Lựa chọn để đối chiếu:** [mcp-servers-for-revit/revit-mcp](https://github.com/mcp-servers-for-revit/revit-mcp) · [puran-water/autocad-mcp](https://github.com/puran-water/autocad-mcp). Đây là ứng viên so sánh theo tác vụ; mức phù hợp cần kiểm theo hồ sơ và phiên bản riêng.

**Bằng chứng:** `docs-read`, ngày 2026-11-23, commit [`86cf7057785f2423fc0d0892c9a5d9c93deb1aa3`](https://github.com/mcp-servers-for-revit/mcp-servers-for-revit/commit/86cf7057785f2423fc0d0892c9a5d9c93deb1aa3), ngày commit 2026-04-05. Đã clone và đọc chọn lọc phần giới thiệu, cách dùng, giới hạn, license, metadata manifest và CI hiện diện. Chưa kiểm đầy đủ implementation hoặc chạy upstream; các số đo của tác giả chưa được tái lập.

**Nguồn:** [README.md](https://github.com/mcp-servers-for-revit/mcp-servers-for-revit/blob/86cf7057785f2423fc0d0892c9a5d9c93deb1aa3/README.md) · [LICENSE](https://github.com/mcp-servers-for-revit/mcp-servers-for-revit/blob/86cf7057785f2423fc0d0892c9a5d9c93deb1aa3/LICENSE) · [.github/workflows/release.yml](https://github.com/mcp-servers-for-revit/mcp-servers-for-revit/blob/86cf7057785f2423fc0d0892c9a5d9c93deb1aa3/.github/workflows/release.yml) · [metadata GitHub](https://api.github.com/repos/mcp-servers-for-revit/mcp-servers-for-revit).

<a id="anhkysuai-2026-11-23-francisreboucas-constructcraft"></a>

### constructcraft

**Repo:** [francisreboucas/constructcraft](https://github.com/francisreboucas/constructcraft) · **License:** GPL-3.0-or-later (app); cc_skp MIT; tài sản riêng · **★ 287 (GitHub API, 2026-11-23)**

**Mục đích:** Ứng dụng BIM bằng Rust, sinh mặt bằng, mặt cắt, lịch và sheet từ một mô hình tham số.

**Giá trị:** Có hướng automation qua CLI/MCP và mô hình dữ liệu chung, phù hợp tham khảo authoring BIM độc lập nhà cung cấp.

**Giới hạn:** README còn mục MVP/roadmap; cần kiểm round-trip IFC/SketchUp và độ đúng bản vẽ trước dự án thật. GPLv3+ của app khác MIT cc_skp, font và icon đi kèm.

**Cách tham khảo/tích hợp:** Thử trên bản sao mô hình với đơn vị và dung sai đã biết, kiểm đầu ra/round-trip và quyền của từng thành phần trước đưa vào quy trình kỹ thuật.

**Lựa chọn để đối chiếu:** [FreeCAD/FreeCAD](https://github.com/FreeCAD/FreeCAD) · [jasonsutter87/sketchcraft](https://github.com/jasonsutter87/sketchcraft). Đây là ứng viên so sánh theo tác vụ; mức phù hợp cần kiểm theo hồ sơ và phiên bản riêng.

**Bằng chứng:** `docs-read`, ngày 2026-11-23, commit [`8461032285ff5ba9597207dcb623517b438654a0`](https://github.com/francisreboucas/constructcraft/commit/8461032285ff5ba9597207dcb623517b438654a0), ngày commit 2026-11-22. Đã clone và đọc chọn lọc phần giới thiệu, cách dùng, giới hạn, license, metadata manifest và CI hiện diện. Chưa kiểm đầy đủ implementation hoặc chạy upstream; các số đo của tác giả chưa được tái lập.

**Nguồn:** [README.md](https://github.com/francisreboucas/constructcraft/blob/8461032285ff5ba9597207dcb623517b438654a0/README.md) · [LICENSE](https://github.com/francisreboucas/constructcraft/blob/8461032285ff5ba9597207dcb623517b438654a0/LICENSE) · [Cargo.toml](https://github.com/francisreboucas/constructcraft/blob/8461032285ff5ba9597207dcb623517b438654a0/Cargo.toml) · [.github/workflows/ci.yml](https://github.com/francisreboucas/constructcraft/blob/8461032285ff5ba9597207dcb623517b438654a0/.github/workflows/ci.yml) · [metadata GitHub](https://api.github.com/repos/francisreboucas/constructcraft).

<a id="anhkysuai-2026-11-23-jasonsutter87-sketchcraft"></a>

### sketchcraft

**Repo:** [jasonsutter87/sketchcraft](https://github.com/jasonsutter87/sketchcraft) · **License:** MIT · **★ 136 (GitHub API, 2026-11-23)**

**Mục đích:** Ứng dụng dựng hình push/pull 3D bằng Rust, có desktop, CLI và MCP.

**Giá trị:** Hỗ trợ hình học nhà/phòng/nội thất và scripting, phù hợp thử mô hình đơn giản với nhiều cách tương tác.

**Giới hạn:** README ghi chưa ký bởi Apple/Microsoft; chưa kiểm file SketchUp round-trip, updater hoặc chất lượng hình học. Cần xác minh bản phát hành và thử trên dữ liệu mẫu trước sử dụng.

**Cách tham khảo/tích hợp:** Thử trên bản sao mô hình với đơn vị và dung sai đã biết, kiểm đầu ra/round-trip và quyền của từng thành phần trước đưa vào quy trình kỹ thuật.

**Lựa chọn để đối chiếu:** [xiangechen/chili3d](https://github.com/xiangechen/chili3d) · [francisreboucas/constructcraft](https://github.com/francisreboucas/constructcraft). Đây là ứng viên so sánh theo tác vụ; mức phù hợp cần kiểm theo hồ sơ và phiên bản riêng.

**Bằng chứng:** `docs-read`, ngày 2026-11-23, commit [`90c46597783bfefa9befdfa8a884c34d63439a81`](https://github.com/jasonsutter87/sketchcraft/commit/90c46597783bfefa9befdfa8a884c34d63439a81), ngày commit 2026-11-22. Đã clone và đọc chọn lọc phần giới thiệu, cách dùng, giới hạn, license, metadata manifest và CI hiện diện. Chưa kiểm đầy đủ implementation hoặc chạy upstream; các số đo của tác giả chưa được tái lập.

**Nguồn:** [README.md](https://github.com/jasonsutter87/sketchcraft/blob/90c46597783bfefa9befdfa8a884c34d63439a81/README.md) · [LICENSE](https://github.com/jasonsutter87/sketchcraft/blob/90c46597783bfefa9befdfa8a884c34d63439a81/LICENSE) · [Cargo.toml](https://github.com/jasonsutter87/sketchcraft/blob/90c46597783bfefa9befdfa8a884c34d63439a81/Cargo.toml) · [.github/workflows/ci.yml](https://github.com/jasonsutter87/sketchcraft/blob/90c46597783bfefa9befdfa8a884c34d63439a81/.github/workflows/ci.yml) · [metadata GitHub](https://api.github.com/repos/jasonsutter87/sketchcraft).

<a id="anhkysuai-2026-11-23-anhkysuai-byte-autocad-mcp-anhkysuai"></a>

### AutoCAD MCP Anh Kỹ Sư AI (fork)

**Repo:** [anhkysuai-byte/autocad-mcp-anhkysuai](https://github.com/anhkysuai-byte/autocad-mcp-anhkysuai) · **License:** MIT · **★ 1 (GitHub API, 2026-11-23)**

**Mục đích:** Fork của tích hợp MCP AutoCAD LT/DXF trong hệ sinh thái Anh Kỹ Sư AI.

**Giá trị:** Được lưu để truy vết đúng link nguồn và quan hệ với upstream puran-water/autocad-mcp.

**Giới hạn:** HEAD được clone trùng SHA với upstream trong đợt này; chưa thấy khác biệt chức năng để coi là giải pháp độc lập. Các giới hạn AutoCAD, document và duyệt kỹ thuật giữ nguyên.

**Cách tham khảo/tích hợp:** Ưu tiên đối chiếu upstream khi cập nhật; giữ liên kết fork để theo dõi nếu có thay đổi riêng, không suy giá trị mới chỉ từ tên repo.

**Lựa chọn để đối chiếu:** [puran-water/autocad-mcp](https://github.com/puran-water/autocad-mcp) · [LibreCAD/LibreCAD](https://github.com/LibreCAD/LibreCAD). Đây là ứng viên so sánh theo tác vụ; mức phù hợp cần kiểm theo hồ sơ và phiên bản riêng.

**Bằng chứng:** `docs-read`, ngày 2026-11-23, commit [`d8d537d295976f97e30d7eacdc71e6e440dd02b9`](https://github.com/anhkysuai-byte/autocad-mcp-anhkysuai/commit/d8d537d295976f97e30d7eacdc71e6e440dd02b9), ngày commit 2026-11-16. Đã clone và đọc chọn lọc phần giới thiệu, cách dùng, giới hạn, license, metadata manifest và CI hiện diện. Chưa kiểm đầy đủ implementation hoặc chạy upstream; các số đo của tác giả chưa được tái lập.

**Nguồn:** [README.md](https://github.com/anhkysuai-byte/autocad-mcp-anhkysuai/blob/d8d537d295976f97e30d7eacdc71e6e440dd02b9/README.md) · [LICENSE](https://github.com/anhkysuai-byte/autocad-mcp-anhkysuai/blob/d8d537d295976f97e30d7eacdc71e6e440dd02b9/LICENSE) · [pyproject.toml](https://github.com/anhkysuai-byte/autocad-mcp-anhkysuai/blob/d8d537d295976f97e30d7eacdc71e6e440dd02b9/pyproject.toml) · [.github/workflows/ci.yml](https://github.com/anhkysuai-byte/autocad-mcp-anhkysuai/blob/d8d537d295976f97e30d7eacdc71e6e440dd02b9/.github/workflows/ci.yml) · [metadata GitHub](https://api.github.com/repos/anhkysuai-byte/autocad-mcp-anhkysuai).

<a id="anhkysuai-2026-11-23-ruvnet-ruview"></a>

### RuView

**Repo:** [ruvnet/RuView](https://github.com/ruvnet/RuView) · **License:** MIT · **★ 104,891 (GitHub API, 2026-11-23)**

**Mục đích:** Nền tảng thử nghiệm cảm nhận không gian bằng tín hiệu WiFi/radar, có tích hợp smart home và agent.

**Giá trị:** Tài liệu phân biệt adapter phần cứng, simulator và trạng thái capability, hữu ích khảo sát pipeline tín hiệu tới ứng dụng.

**Giới hạn:** Tuyên bố theo dõi nhịp thở/nhịp tim hoặc xuyên tường chưa được tái lập; một số provider còn beta, simulator hoặc gated. Không coi mô phỏng hay tín hiệu hiện diện là thiết bị đo sức khỏe đã xác thực.

**Cách tham khảo/tích hợp:** Tách simulator khỏi adapter phần cứng, chọn dữ liệu chuẩn để kiểm độ đúng và sai số trước sử dụng thực tế.

**Lựa chọn để đối chiếu:** [AtsushiSakai/PythonRobotics](https://github.com/AtsushiSakai/PythonRobotics) · [arendst/Tasmota](https://github.com/arendst/Tasmota). Đây là ứng viên so sánh theo tác vụ; mức phù hợp cần kiểm theo hồ sơ và phiên bản riêng.

**Bằng chứng:** `docs-read`, ngày 2026-11-23, commit [`8139c7e6258a19da9c9861fa035705dd3f031b56`](https://github.com/ruvnet/RuView/commit/8139c7e6258a19da9c9861fa035705dd3f031b56), ngày commit 2026-11-21. Đã clone và đọc chọn lọc phần giới thiệu, cách dùng, giới hạn, license, metadata manifest và CI hiện diện. Chưa kiểm đầy đủ implementation hoặc chạy upstream; các số đo của tác giả chưa được tái lập.

**Nguồn:** [README.md](https://github.com/ruvnet/RuView/blob/8139c7e6258a19da9c9861fa035705dd3f031b56/README.md) · [LICENSE](https://github.com/ruvnet/RuView/blob/8139c7e6258a19da9c9861fa035705dd3f031b56/LICENSE) · [pyproject.toml](https://github.com/ruvnet/RuView/blob/8139c7e6258a19da9c9861fa035705dd3f031b56/pyproject.toml) · [.github/workflows/ci.yml](https://github.com/ruvnet/RuView/blob/8139c7e6258a19da9c9861fa035705dd3f031b56/.github/workflows/ci.yml) · [metadata GitHub](https://api.github.com/repos/ruvnet/RuView).

## Nguồn

Các permalink trong từng hồ sơ cố định đúng phiên bản đã đọc; số sao/trạng thái archive là snapshot GitHub API ngày 2026-11-02. Không chạy mã, huấn luyện model hoặc tái lập kết quả của upstream.

<a id="nt-2026-11-23"></a>

## Nâng trần theo khoảng trống — 23/11/2026

Phần này có các hồ sơ mới của đợt nâng trần: mười trinh sát tìm trên internet và GitHub những mảng mà chuyên mục còn thiếu hoặc chỉ có hồ sơ cũ, rồi mỗi repo được clone nông tại một commit cố định, đọc LICENSE, README, ít nhất một file triển khai thật và CI nếu có; không cài hay chạy mã upstream. Mô tả của trinh sát nhiều chỗ sai so với mã thật, và các chỗ đó được sửa ngay trong từng hồ sơ. Số sao lấy sau bằng GitHub search API nên có thể để trống.

<a id="nt-opengeospatial-geoparquet"></a>

### GeoParquet (đặc tả)

| Thuộc tính | Giá trị |
|---|---|
| Repo | https://github.com/opengeospatial/geoparquet |
| License | Apache-2.0 (LICENSE đã mở) |
| Phiên bản đã đọc | `7dafbdc3a694e36b2da5484f05a5ed3ef0521e65` (commit 2026-11-21) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README, CHANGELOG, format-specs/geoparquet.md, schema.json, test_json_schema.py, scripts.yml, lint.yml; chưa chạy upstream |
| Khoảng trống lấp | Chuẩn cloud-native cho dữ liệu không gian (GeoParquet); nguồn chuẩn để viết skill kiểm file |
| Cơ chế đáng học | - Metadata khóa `geo` trong Parquet với trường bắt buộc `version`, `primary_column`, `columns`; mỗi cột geometry có `encoding` (chỉ WKB), `geometry_types`, `crs`, `bbox`, `covering`, `epoch`, `orientation` (`format-specs/geoparquet.md`).<br>- Bản 2.0.0 chuyển sang kiểu logic GEOMETRY/GEOGRAPHY gốc của Parquet, CRS đi theo cột, thống kê hình học theo row group để lọc không gian (CHANGELOG).<br>- `format-specs/schema.json` là JSON Schema (hằng `version` là 2.0.0, `encoding` là WKB) dùng kiểm khóa metadata; `compatible-parquet.md` giải thích file Parquet ghi kiểu gốc nhưng thiếu metadata geo. |
| Tiêu chí và cách kiểm | Có kiểm bằng máy cho phần metadata: `scripts/test_json_schema.py` dựng ca hợp lệ và không hợp lệ ngay lúc chạy rồi kiểm với schema (tải schema PROJJSON từ proj.org khi chạy), `test_example.py` kiểm ví dụ; workflow `scripts.yml` còn sinh lại ví dụ và đòi cây git sạch, `lint.yml` chạy pre-commit (đã mở cả hai). Ghi chú: không có bộ kiểm dữ liệu hình học ngay trong repo; README trỏ tới gpq và script validate của GDAL. |
| Giới hạn và rủi ro | Bản 2.0.0 chưa được OGC phê duyệt chính thức (README) nên có thể còn đổi khi qua OGC. Thư mục `test_data` có 13 file mẫu, không phải corpus tuân thủ đầy đủ. Hệ sinh thái công cụ mới chuyển 2.0: gpq (đã đọc) mặc định ghi metadata 1.0.0. Tuyên bố hiệu năng và độ phổ biến trong README là của tác giả **(chưa xác minh)**. |
| So với | GDAL (`osgeo-gdal`) là thư viện đọc/ghi và có script validate; hồ sơ này là đặc tả chứ không phải công cụ. gpq (cùng đợt) là validator Go. |
| Nguồn | [README](https://github.com/opengeospatial/geoparquet/blob/7dafbdc3a694e36b2da5484f05a5ed3ef0521e65/README.md) · [LICENSE](https://github.com/opengeospatial/geoparquet/blob/7dafbdc3a694e36b2da5484f05a5ed3ef0521e65/LICENSE) · [CHANGELOG](https://github.com/opengeospatial/geoparquet/blob/7dafbdc3a694e36b2da5484f05a5ed3ef0521e65/CHANGELOG.md) · [geoparquet.md](https://github.com/opengeospatial/geoparquet/blob/7dafbdc3a694e36b2da5484f05a5ed3ef0521e65/format-specs/geoparquet.md) · [schema.json](https://github.com/opengeospatial/geoparquet/blob/7dafbdc3a694e36b2da5484f05a5ed3ef0521e65/format-specs/schema.json) · [test_json_schema](https://github.com/opengeospatial/geoparquet/blob/7dafbdc3a694e36b2da5484f05a5ed3ef0521e65/scripts/test_json_schema.py) · [scripts.yml](https://github.com/opengeospatial/geoparquet/blob/7dafbdc3a694e36b2da5484f05a5ed3ef0521e65/.github/workflows/scripts.yml) · [lint.yml](https://github.com/opengeospatial/geoparquet/blob/7dafbdc3a694e36b2da5484f05a5ed3ef0521e65/.github/workflows/lint.yml) |

<a id="nt-buildingsmart-certification-datasets"></a>

### buildingSMART Certification datasets

| Thuộc tính | Giá trị |
|---|---|
| Repo | https://github.com/buildingSMART/Certification-datasets |
| License | CC-BY-4.0 theo nội dung `LICENSE` (bản quyền buildingSMART International Ltd); GitHub ghi NOASSERTION vì file chỉ nêu giấy phép bằng văn xuôi. Cần ghi nguồn khi tái dùng; chưa có tuyên bố riêng về từng file IFC |
| Phiên bản đã đọc | `5030f652e85d3e679b392fcb38bfa3328d6d9f79` (commit 2026-11-18) |
| Kiểm chứng | 2026-11-23; docs-read; đã đọc README, LICENSE, import-certification.md, README thư mục IFC 4.3.2.0, Infra-Road.ifc (đầu file); chưa chạy upstream |
| Khoảng trống lấp | Kiểm IFC bằng máy (corpus dữ liệu chứng nhận); thực tế là mẫu và tiêu chí nhập, chưa phải bộ kiểm máy |
| Cơ chế đáng học | - Ba thư mục theo phiên bản (IFC 2x3 TC1, IFC 4 ADD2 TC1, IFC 4.3 ADD2), mỗi thư mục có Simple-Scene gồm 10 file Building-\* và Infra-\* (kiến trúc, kết cấu, HVAC, cầu, đường, ray...).<br>- Thư mục IFC 4 ADD2 TC1 thêm 5 file ISO Spec - ReferenceView_V1.2 (tessellation, tường có ô cửa).<br>- `import-certification.md` liệt kê tiêu chí nhập tối thiểu: mở đủ 10 mô hình, hình học, định vị và CRS, phân cấp Project-Site-Building-Storey, vật liệu, màu, thuộc tính và GUID, lượng, phân loại, assembly, group/system, space, mặt đường và vạch kẻ (chỉ IFC 4.3). |
| Tiêu chí và cách kiểm | Điều kiện đạt: mọi tiêu chí phải Pass hoặc Partial Pass, một tiêu chí Fail là loại (theo `import-certification.md`). Kiểm hoàn toàn thủ công theo mô tả; repo không có test, script hay workflow; chưa chạy phần mềm nào với bộ này. Muốn dùng làm fixture kiểm tự động phải tự viết kiểm (ví dụ nạp bằng IfcOpenShell). |
| Giới hạn và rủi ro | Giữ nguyên mô tả "Previous content ... moved" trong README: nội dung cộng đồng cũ đã chuyển sang repo Community-Sample-Test-Files, nên đừng kỳ vọng kho mẫu rộng. File IFC sinh bằng Sketchup IFC manager (header Infra-Road.ifc), nên chỉ phủ phạm vi ReferenceView. Chuẩn IFC là ISO 16739 và chuẩn trả phí; hồ sơ không nhận định ở cấp điều khoản. Danh sách tiêu chí nhập chỉ là bộ tối thiểu công bố, không phải toàn bộ quy trình chứng nhận. |
| So với | IfcOpenShell (`ifcopenshell`) là thư viện đọc IFC có thể dùng nạp bộ này; buildingSMART IDS (`buildingsmart-ids`) là đặc tả kiểm yêu cầu thông tin; buildingSMART/validate (cùng đợt) là dịch vụ kiểm file. |
| Nguồn | [README](https://github.com/buildingSMART/Certification-datasets/blob/5030f652e85d3e679b392fcb38bfa3328d6d9f79/README.md) · [LICENSE](https://github.com/buildingSMART/Certification-datasets/blob/5030f652e85d3e679b392fcb38bfa3328d6d9f79/LICENSE) · [import-certification](https://github.com/buildingSMART/Certification-datasets/blob/5030f652e85d3e679b392fcb38bfa3328d6d9f79/import-certification.md) · [README 4.3.2.0](https://github.com/buildingSMART/Certification-datasets/blob/5030f652e85d3e679b392fcb38bfa3328d6d9f79/IFC%204.3.2.0%20%28IFC%204.3%20ADD2%29/README.md) · [Infra-Road.ifc](https://github.com/buildingSMART/Certification-datasets/blob/5030f652e85d3e679b392fcb38bfa3328d6d9f79/IFC%204.3.2.0%20%28IFC%204.3%20ADD2%29/Simple-Scene/Infra-Road.ifc) |

<a id="nt-planetlabs-gpq"></a>

### gpq

| Thuộc tính | Giá trị |
|---|---|
| Repo | https://github.com/planetlabs/gpq |
| License | Apache-2.0 (LICENSE đã mở) |
| Phiên bản đã đọc | `a5a6b208af6730539db96eb9a4083f0359836b28` (commit 2026-09-19) |
| Kiểm chứng | 2026-11-23; code-read; đã đọc readme.md, LICENSE, go.mod, internal/validator/rules.go, internal/geoparquet/metadata.go, test.yml; chưa chạy upstream |
| Khoảng trống lấp | Chuẩn cloud-native cho dữ liệu không gian: validator và bộ chuyển đổi GeoParquet dạng CLI nhẹ |
| Cơ chế đáng học | - `internal/validator/rules.go` định nghĩa Rule (tiêu đề và hàm Validate), ví dụ `RequiredVersion`, `RequiredPrimaryColumn`, kiểm encoding và loại hình học; lỗi nghiêm trọng dùng `ErrFatal` để dừng.<br>- `gpq validate file.parquet` in báo cáo từng mục kiểm, có `--format json`; thoát mã 1 nếu có mục thất bại (readme.md). Kiểm cả dữ liệu hình học (encoding, hướng vòng, bbox) theo readme.<br>- `gpq convert` đi hai chiều với GeoJSON; có bản WASM chạy trên web (readme). |
| Tiêu chí và cách kiểm | Có kiểm bằng máy: `validator_test.go` chạy bộ ca trong `internal/validator/testdata` (all-pass, bad-bbox-length, bad-crs, bad-encoding...); workflow `test.yml` chạy golangci-lint và `go test -v ./...` (đã mở workflow); chưa chạy. Mã thoát là cổng cho CI. |
| Giới hạn và rủi ro | Chưa thấy hỗ trợ GeoParquet 2.0: hằng `Version = "1.0.0"` trong `metadata.go`, rules.go không có xử lý GEOMETRY/GEOGRAPHY (grep), và `RequiredVersion` chỉ kiểm chuỗi không rỗng nên file 2.0 có thể qua hoặc trượt tùy mục khác; cần thử với file 2.0 thật trước khi đưa vào CI. Kiểm CRS dùng schema PROJJSON qua httploader nên có phụ thuộc mạng. Commit cuối 2026-09-19, bảo trì chủ yếu là cập nhật phụ thuộc; không suy ra dự án ngừng. |
| So với | Đặc tả GeoParquet (`opengeospatial-geoparquet`, cùng đợt) là chuẩn gốc; GDAL (`osgeo-gdal`) có script validate bằng Python cho cùng mục đích. |
| Nguồn | [readme](https://github.com/planetlabs/gpq/blob/a5a6b208af6730539db96eb9a4083f0359836b28/readme.md) · [LICENSE](https://github.com/planetlabs/gpq/blob/a5a6b208af6730539db96eb9a4083f0359836b28/LICENSE) · [go.mod](https://github.com/planetlabs/gpq/blob/a5a6b208af6730539db96eb9a4083f0359836b28/go.mod) · [rules.go](https://github.com/planetlabs/gpq/blob/a5a6b208af6730539db96eb9a4083f0359836b28/internal/validator/rules.go) · [metadata.go](https://github.com/planetlabs/gpq/blob/a5a6b208af6730539db96eb9a4083f0359836b28/internal/geoparquet/metadata.go) · [test.yml](https://github.com/planetlabs/gpq/blob/a5a6b208af6730539db96eb9a4083f0359836b28/.github/workflows/test.yml) |

<a id="nt-modelon-pyfmi"></a>

### PyFMI

| Thuộc tính | Giá trị |
|---|---|
| Repo | https://github.com/modelon-community/PyFMI |
| License | LGPL-3.0 (LICENSE đã mở); nhắc rằng FMU ví dụ lấy từ FMU SDK của Qtronic có giấy phép riêng theo README |
| Phiên bản đã đọc | `678617a00b8adaa63718aea9c251caa9086b2652` (commit 2026-11-23) |
| Kiểm chứng | 2026-11-23; code-read; đã đọc README, LICENSE, CHANGELOG, `load_fmu` trong fmi.pyx, fmi3.pyx, build.yml; chưa chạy upstream |
| Khoảng trống lấp | Đồng mô phỏng FMI và Modelica: nạp, chạy FMU từ Python |
| Cơ chế đáng học | - `load_fmu` trong `fmi.pyx` tự nhận phiên bản FMI và loại (me, cs, se, auto) rồi trả lớp tương ứng; mô tả `allow_unzipped_fmu`, log, kiểm đối số.<br>- Lớp riêng cho từng phiên bản (`fmi1.pyx`, `fmi2.pyx`, `fmi3.pyx`); fmi3 có `FMUModelME3` và `FMUModelCS3`.<br>- `master.pyx` (khoảng 2000 dòng) triển khai thuật toán Master để ghép nhiều FMU; CHANGELOG nêu bước sự kiện, `dynamic_diagnostics`, `get_fmu_kind`. |
| Tiêu chí và cách kiểm | Có test: thư mục `tests` (test_fmi2, test_fmi3, test_fmi3_sim, test_fmi_master, test_step_events...); workflow `build.yml` build image phát triển rồi chạy `make test` (đã mở workflow). Theo README, 95 trên 116 FMU Cross Check đạt với PyFMI 2.11.0 trên Ubuntu 20.04 và mọi Reference FMUs v0.0.27 đạt: số liệu của tác giả, chưa xác minh. |
| Giới hạn và rủi ro | Rủi ro vận hành: FMU là thư viện native chạy cùng tiến trình nên cần coi FMU lạ là mã không tin cậy; FMU cần công cụ thực thi ngoài (ví dụ AMESim) không được hỗ trợ (README). LGPL cho phép dùng làm thư viện nhưng có nghĩa vụ khi liên kết tĩnh hoặc sửa. Không có SSP; cần OMSimulator hoặc công cụ khác nếu cần mô tả hệ thống SSP. |
| So với | OMSimulator (cùng đợt) hỗ trợ SSP và FMI trong một môi trường; kho chưa có hồ sơ FMI cùng loại, các hồ sơ simulation hiện có (`bulletphysics-bullet3`, `jrouwe-joltphysics`) là vật lý thời gian thực, khác nhiệm vụ. |
| Nguồn | [README](https://github.com/modelon-community/PyFMI/blob/678617a00b8adaa63718aea9c251caa9086b2652/README.md) · [LICENSE](https://github.com/modelon-community/PyFMI/blob/678617a00b8adaa63718aea9c251caa9086b2652/LICENSE) · [CHANGELOG](https://github.com/modelon-community/PyFMI/blob/678617a00b8adaa63718aea9c251caa9086b2652/CHANGELOG) · [fmi.pyx](https://github.com/modelon-community/PyFMI/blob/678617a00b8adaa63718aea9c251caa9086b2652/src/pyfmi/fmi.pyx) · [fmi3.pyx](https://github.com/modelon-community/PyFMI/blob/678617a00b8adaa63718aea9c251caa9086b2652/src/pyfmi/fmi3.pyx) · [build.yml](https://github.com/modelon-community/PyFMI/blob/678617a00b8adaa63718aea9c251caa9086b2652/.github/workflows/build.yml) |

<a id="nt-openmodelica-omsimulator"></a>

### OMSimulator

| Thuộc tính | Giá trị |
|---|---|
| Repo | https://github.com/OpenModelica/OMSimulator |
| License | OSMC-PL (`OSMC-License.txt`): chế độ AGPL-3.0 cho mọi bên; OSMC-Internal-EPL và OSMC-External-EPL chỉ cho thành viên OSMC cấp 1 và 2. Không có file LICENSE; `3rdParty/` mang giấy phép bên thứ ba chưa đọc |
| Phiên bản đã đọc | `fd7aecbee9d3f546e484152c9a4c4aee0d483406` (commit 2026-11-20) |
| Kiểm chứng | 2026-11-23; code-read; đã đọc README, OSMC-License.txt, testsuite/README.md, Jenkinsfile, coverage.yml, tiêu đề ComponentFMU3CS.h; chưa chạy upstream |
| Khoảng trống lấp | Đồng mô phỏng FMI và SSP (OpenModelica) |
| Cơ chế đáng học | - `src/OMSimulatorLib` có lớp thành phần riêng cho FMU CS/ME và FMI 3 (`ComponentFMU3CS`, `ComponentFMU3ME`), DCP, bảng dữ liệu, CSV reader/writer, vòng lặp đại số (`AlgLoop`) và thư mục `ssd` cho mô tả hệ thống SSP.<br>- Dùng được như CLI, thư viện C, gói pip (`pip install OMSimulator`) hoặc GUI PySide6 không cần `omc` (README).<br>- Testsuite theo thư mục chủ đề, mỗi test mang header và khối `## Result:` ở cuối file; `omc-diff` so kết quả thực với kỳ vọng (`testsuite/README.md`). |
| Tiêu chí và cách kiểm | Có kiểm bằng máy nhưng chạy trên bản đã cài: `ctest` với `-DOMS_ENABLE_TESTSUITE=ON` (testsuite/README); workflow `coverage.yml` build trong container docker.openmodelica.org và chạy testsuite với đo coverage, cho phép bước test thất bại rồi fail job cuối (đã mở); Jenkinsfile có stage kiểm và nhiều nền tảng (chỉ đọc phần đầu). README dẫn báo cáo MSL4 do OpenModelica công bố: chưa xác minh. |
| Giới hạn và rủi ro | License hai tầng dễ hiểu nhầm: người dùng thương mại không phải thành viên chỉ có AGPL-3.0, nghĩa vụ chia sẻ mã khi phục vụ qua mạng nếu nhúng. Nhánh master là "unstable" theo README; bản ổn định ở maintenance/v2.1. Build phức tạp (CMake, 3rdParty, submodule). Phần lớn hạ tầng kiểm chạy ở Jenkins nên không thấy hết từ repo GitHub. |
| So với | PyFMI (`modelon-pyfmi`, cùng đợt) chỉ làm FMU từ Python và không có SSP; OMSimulator thiên về hệ thống ghép SSP. Kho chưa có hồ sơ FMI/SSP khác để so. |
| Nguồn | [README](https://github.com/OpenModelica/OMSimulator/blob/fd7aecbee9d3f546e484152c9a4c4aee0d483406/README.md) · [OSMC-License](https://github.com/OpenModelica/OMSimulator/blob/fd7aecbee9d3f546e484152c9a4c4aee0d483406/OSMC-License.txt) · [testsuite README](https://github.com/OpenModelica/OMSimulator/blob/fd7aecbee9d3f546e484152c9a4c4aee0d483406/testsuite/README.md) · [Jenkinsfile](https://github.com/OpenModelica/OMSimulator/blob/fd7aecbee9d3f546e484152c9a4c4aee0d483406/Jenkinsfile) · [coverage.yml](https://github.com/OpenModelica/OMSimulator/blob/fd7aecbee9d3f546e484152c9a4c4aee0d483406/.github/workflows/coverage.yml) · [ComponentFMU3CS.h](https://github.com/OpenModelica/OMSimulator/blob/fd7aecbee9d3f546e484152c9a4c4aee0d483406/src/OMSimulatorLib/ComponentFMU3CS.h) |

<a id="nt-buildingsmart-validate"></a>

### buildingSMART Validation Service

| Thuộc tính | Giá trị |
|---|---|
| Repo | https://github.com/buildingSMART/validate |
| License | MIT (LICENSE đã mở, bản quyền buildingSMART International 2026); submodule ifc-gherkin-rules, ifc-validation-data-model và kho chứng chỉ có license riêng, chưa đọc |
| Phiên bản đã đọc | `5ceadbca687667601d687c2a5ff686ed263f2917` (commit 2026-11-17) |
| Kiểm chứng | 2026-11-23; code-read; đã đọc README, LICENSE, .gitmodules, check_gherkin.py, check_programs.py, validate_header.py, playwright.yml; chưa chạy upstream |
| Khoảng trống lấp | Kiểm IFC bằng máy: dịch vụ validate chính thức; không có kiểm IDS |
| Cơ chế đáng học | - `tasks/check_programs.py` gọi từng bước như tiến trình con có timeout: `ifcopenshell.simple_spf --json` (cú pháp), `ifcopenshell.validate --json --rules --fields` (schema), kiểm header, magic số và ClamAV, chữ ký số, bSDD, tiền điều kiện, quy tắc chuẩn.<br>- `checks/check_gherkin.py` bọc `ifc_gherkin_rules.run` với `RuleType`, `max_outcomes`; chính các file quy tắc nằm trong submodule bên ngoài.<br>- `header_policy/validate_header.py` kiểm header theo schema pydantic và cấu hình YAML; có `check_signatures.py` và kho chứng chỉ nhà cung cấp (submodule) để xác thực chữ ký. |
| Tiêu chí và cách kiểm | Có kiểm bằng máy: thư mục tests cho `ifc_validation` và `header_policy`, workflow `playwright.yml` chạy kiểm UI đầu cuối trong container Playwright với Postgres và Redis trên nhánh development (đã mở workflow); các workflow khác chỉ nhìn tên. Chưa chạy dịch vụ. |
| Giới hạn và rủi ro | Phải triển khai nhiều thành phần (Django, Postgres, Redis, Celery, tùy chọn nhiều máy swarm) nên nặng hơn dùng thư viện trực tiếp. Quy tắc nghiệp vụ nằm ở submodule không được đọc nên không thể đánh giá độ phủ quy tắc. README liệt kê tài khoản mặc định root/root và SYSTEM/system cho môi trường dev: không dùng ngoài dev. bSDD đang tắt theo README. Chuẩn IFC (ISO 16739) trả phí nên không nhận định cấp điều khoản. |
| So với | IfcOpenShell (`ifcopenshell`) là lõi validate mà dịch vụ này gọi; buildingSMART IDS (`buildingsmart-ids`) là đặc tả kiểm yêu cầu mà repo này chưa có; Certification datasets (cùng đợt) là bộ mẫu kiểm tay. |
| Nguồn | [README](https://github.com/buildingSMART/validate/blob/5ceadbca687667601d687c2a5ff686ed263f2917/README.md) · [LICENSE](https://github.com/buildingSMART/validate/blob/5ceadbca687667601d687c2a5ff686ed263f2917/LICENSE) · [.gitmodules](https://github.com/buildingSMART/validate/blob/5ceadbca687667601d687c2a5ff686ed263f2917/.gitmodules) · [check_gherkin](https://github.com/buildingSMART/validate/blob/5ceadbca687667601d687c2a5ff686ed263f2917/backend/apps/ifc_validation/checks/check_gherkin.py) · [check_programs](https://github.com/buildingSMART/validate/blob/5ceadbca687667601d687c2a5ff686ed263f2917/backend/apps/ifc_validation/tasks/check_programs.py) · [validate_header](https://github.com/buildingSMART/validate/blob/5ceadbca687667601d687c2a5ff686ed263f2917/backend/apps/ifc_validation/checks/header_policy/validate_header.py) · [playwright.yml](https://github.com/buildingSMART/validate/blob/5ceadbca687667601d687c2a5ff686ed263f2917/.github/workflows/playwright.yml) |

<a id="nt-pythonocc-core"></a>

### pythonocc-core

| Thuộc tính | Giá trị |
|---|---|
| Repo | https://github.com/tpaviot/pythonocc-core |
| License | LGPL-3.0 |
| Phiên bản đã đọc | `e685bfe954e76b643fc63e6fedd1a4b433751cc8` (commit 2026-11-17) |
| Kiểm chứng | 2026-11-23; code-read; đã đọc README.md, LICENSE, src/Extend/DataExchange.py, src/Extend/ShapeFactory.py, azure-pipelines.yml và conda-build.yml; chưa chạy upstream |
| Khoảng trống lấp | Kernel B-rep và STEP AP242 từ Python; kiểm hình học là tự gọi OCCT, không có cổng kiểm sẵn |
| Cơ chế đáng học | • write_step_file(shape, filename, application_protocol) chọn schema qua DESTEP_Parameters: AP203, AP214IS, AP242DIS; tệp AP242 chứa lưới tam giác chỉ xuất được khi chọn AP242DIS, kèm cảnh báo (DataExchange.py).<br>• read_step_file đọc bằng STEPControl_Reader, báo lỗi bằng AssertionError khi ReadFile, TransferRoots hoặc không có shape; gộp nhiều shape thành compound (DataExchange.py).<br>• measure_shape_volume và khối tâm dùng brepgprop và GProp_GProps; có thêm bounding box căn trục và có hướng (ShapeFactory.py).<br>• Lớp Extend là lớp Python mỏng có type stub (.pyi, py.typed) phủ lên binding OCCT thô. |
| Tiêu chí và cách kiểm | CI là azure-pipelines.yml chạy conda-build.yml cho Ubuntu, macOS, Windows trên Python 3.10 trở lên và lịch build hằng đêm; thư mục test có test dataexchange, shapefactory, topology, brepgraph. Không có ngưỡng dung sai nào đóng gói sẵn. Chưa chạy. |
| Giới hạn và rủi ro | LGPL-3.0 (liên kết động thì thường dễ, nhưng nhúng cần đọc kỹ điều kiện); OCCT có license riêng (chưa xác minh). Không có kiểm hợp lệ solid hay xác thực AP242 PMI sẵn; đọc STEP của bên thứ ba đi qua mã C++ nên coi tệp là đầu vào không tin cậy.  Không đo tốc độ hay độ chính xác. |
| So với | cadquery trong kho (dựng hình bằng script trên OCP); ifcopenshell trong kho (IFC, cũng dựa trên OCCT); trimesh trong kho (lưới, không phải B-rep); freecad trong kho. |
| Nguồn | [README.md](https://github.com/tpaviot/pythonocc-core/blob/e685bfe954e76b643fc63e6fedd1a4b433751cc8/README.md) · [LICENSE](https://github.com/tpaviot/pythonocc-core/blob/e685bfe954e76b643fc63e6fedd1a4b433751cc8/LICENSE) · [DataExchange.py](https://github.com/tpaviot/pythonocc-core/blob/e685bfe954e76b643fc63e6fedd1a4b433751cc8/src/Extend/DataExchange.py) · [ShapeFactory.py](https://github.com/tpaviot/pythonocc-core/blob/e685bfe954e76b643fc63e6fedd1a4b433751cc8/src/Extend/ShapeFactory.py) · [azure-pipelines.yml](https://github.com/tpaviot/pythonocc-core/blob/e685bfe954e76b643fc63e6fedd1a4b433751cc8/azure-pipelines.yml) · [conda-build.yml](https://github.com/tpaviot/pythonocc-core/blob/e685bfe954e76b643fc63e6fedd1a4b433751cc8/conda-build.yml) |

<a id="nt-geoparquet-io"></a>

### geoparquet-io (gpio)

| Thuộc tính | Giá trị |
|---|---|
| Repo | https://github.com/geoparquet/geoparquet-io |
| License | Apache-2.0 |
| Phiên bản đã đọc | `14bee5991cf9fdc79ac1e397dc7162ca6391426d` (commit 2026-11-23) |
| Kiểm chứng | 2026-11-23; code-read; đã đọc README.md, LICENSE, check_verdict.py, duckdb_utils.py, validate.py, stac_check.py và tests.yml; chưa chạy upstream |
| Khoảng trống lấp | Cổng kiểm máy và tối ưu GeoParquet; STAC chỉ kiểm JSON, OGC API chưa thấy |
| Cơ chế đáng học | • check_verdict.py: một mô-đun duy nhất quyết định mức nặng và mã thoát cho mọi lệnh check; mỗi vấn đề có nhãn mức riêng, kết quả xấu nhất thắng, check không chạy được là FAILURE; exit_code trả 1 khi FAILURE hoặc khi WARNING và có --strict.<br>• validate.py kiểm GeoParquet theo đặc tả 1.0, 1.1, 2.0 và kiểu địa lý gốc của Parquet; kết quả đi qua cùng mô hình verdict.<br>• stac_check.py kiểm tệp STAC Item hoặc Collection bằng pystac.validation và báo lỗi nếu truyền nhầm tệp dữ liệu (stac_check.py).<br>• duckdb_utils.py: đặt QUERY_FARM_TELEMETRY_OPT_OUT mặc định là 1 trước khi LOAD extension, nêu lý do là lỗi crash tiến trình do luồng telemetry (issue 779). |
| Tiêu chí và cách kiểm | Cổng kiểm là mã tất định trên metadata và dữ liệu Parquet; tests.yml chạy pre-commit lint, kiểm bảo mật phụ thuộc, test, slow test hằng đêm, và đồng bộ tài liệu sinh tự động. Không chạy lại ở đây; ngưỡng cỡ row group trong check_parquet_structure.py chỉ đọc lướt. |
| Giới hạn và rủi ro | Apache-2.0. Extension A5 phân phối từ kho Query.Farm với DuckDB 2.0 trở lên, gpio tin kho đó qua TLS; README nêu cần ghim python-duckdb dưới 1.6 khi cài bằng conda. Đọc và ghi S3, GCS, Azure, HTTPS cần quản lý khóa truy cập. Số sao trinh sát ghi (177) không được xác minh. Thư mục skills và plugins/gpio-fiboa chưa đọc. |
| So với | osgeo-gdal trong kho (chuyển đổi đa định dạng); geopandas-geopandas trong kho (thư viện dataframe); duckdb trong kho (engine nền); stac-geoparquet (cùng đợt). |
| Nguồn | [README.md](https://github.com/geoparquet/geoparquet-io/blob/14bee5991cf9fdc79ac1e397dc7162ca6391426d/README.md) · [LICENSE](https://github.com/geoparquet/geoparquet-io/blob/14bee5991cf9fdc79ac1e397dc7162ca6391426d/LICENSE) · [check_verdict.py](https://github.com/geoparquet/geoparquet-io/blob/14bee5991cf9fdc79ac1e397dc7162ca6391426d/geoparquet_io/core/check_verdict.py) · [duckdb_utils.py](https://github.com/geoparquet/geoparquet-io/blob/14bee5991cf9fdc79ac1e397dc7162ca6391426d/geoparquet_io/core/duckdb_utils.py) · [validate.py](https://github.com/geoparquet/geoparquet-io/blob/14bee5991cf9fdc79ac1e397dc7162ca6391426d/geoparquet_io/core/validate.py) · [stac_check.py](https://github.com/geoparquet/geoparquet-io/blob/14bee5991cf9fdc79ac1e397dc7162ca6391426d/geoparquet_io/core/stac_check.py) · [tests.yml](https://github.com/geoparquet/geoparquet-io/blob/14bee5991cf9fdc79ac1e397dc7162ca6391426d/.github/workflows/tests.yml) |

<a id="nt-stac-geoparquet"></a>

### stac-geoparquet

| Thuộc tính | Giá trị |
|---|---|
| Repo | https://github.com/stac-utils/stac-geoparquet |
| License | MIT |
| Phiên bản đã đọc | `9431ee49353363fd6c27e011eb0448de201e01df` (commit 2026-11-20) |
| Kiểm chứng | 2026-11-23; code-read; đã đọc README.md, LICENSE, `_api.py`, `_to_parquet.py`, continuous-integration.yml, tests/test_arrow.py (tên hàm) và pyproject.toml; chưa chạy upstream |
| Khoảng trống lấp | Chuẩn cloud-native cho catalog STAC: lưu hàng triệu item dưới dạng GeoParquet; không phải bộ kiểm hợp lệ |
| Cơ chế đáng học | • from_batches trong `_api.py` lấy batch bằng next() để không giữ batch trước, ném ValueError nếu schema lệch, bỏ batch rỗng kèm cảnh báo, ghi log CPU và RSS mỗi batch.<br>• to_parquet trong `_to_parquet.py` nhận Table, RecordBatchReader hoặc luồng Arrow PyCapsule, không nạp hết vào bộ nhớ, ghi collections vào metadata footer và schema_version GeoParquet.<br>• Test khứ hồi round-trip, NDJSON, hai cột geometry, filesystem không cục bộ (tests/test_arrow.py).<br>• Dùng release-please để phát hành, có bản đặc tả riêng trong thư mục spec. |
| Tiêu chí và cách kiểm | Kiểm bằng máy là pytest trong CI và pre-commit; có test khứ hồi nhưng tên hàm là cái duy nhất đã đọc, nội dung test chưa mở hết. Không có ngưỡng chất lượng dữ liệu hay xác thực schema STAC. |
| Giới hạn và rủi ro | MIT, bản quyền gốc 2022 Tom Augspurger. Kiểu dữ liệu chung phụ thuộc pyarrow, geopandas, pyproj nên cài nặng; pgstac và Delta Lake là phụ thuộc tùy chọn cần psycopg hoặc deltalake. Số sao trinh sát ghi (159) chưa xác minh. Không kiểm thử các trường hợp STAC extension phức tạp ở đây. |
| So với | geoparquet-io (cùng đợt: tối ưu và kiểm tệp GeoParquet, có kiểm STAC JSON); osgeo-gdal trong kho; opendronemap-odm trong kho (nguồn ảnh drone, quan hệ chưa xác minh). |
| Nguồn | [README.md](https://github.com/stac-utils/stac-geoparquet/blob/9431ee49353363fd6c27e011eb0448de201e01df/README.md) · [LICENSE](https://github.com/stac-utils/stac-geoparquet/blob/9431ee49353363fd6c27e011eb0448de201e01df/LICENSE) · [_api.py](https://github.com/stac-utils/stac-geoparquet/blob/9431ee49353363fd6c27e011eb0448de201e01df/stac_geoparquet/arrow/_api.py) · [_to_parquet.py](https://github.com/stac-utils/stac-geoparquet/blob/9431ee49353363fd6c27e011eb0448de201e01df/stac_geoparquet/arrow/_to_parquet.py) · [continuous-integration.yml](https://github.com/stac-utils/stac-geoparquet/blob/9431ee49353363fd6c27e011eb0448de201e01df/.github/workflows/continuous-integration.yml) · [test_arrow.py](https://github.com/stac-utils/stac-geoparquet/blob/9431ee49353363fd6c27e011eb0448de201e01df/tests/test_arrow.py) · [pyproject.toml](https://github.com/stac-utils/stac-geoparquet/blob/9431ee49353363fd6c27e011eb0448de201e01df/pyproject.toml) |

<a id="nt-libcosim"></a>

### libcosim (Open Simulation Platform)

| Thuộc tính | Giá trị |
|---|---|
| Repo | https://github.com/open-simulation-platform/libcosim |
| License | MPL-2.0 |
| Phiên bản đã đọc | `9b58267a040e32ed50aa95c2019b304f0fbbe796` (commit 2026-10-13) |
| Kiểm chứng | 2026-11-23; code-read; đã đọc README.md, LICENSE, version.txt, docs/main_page.md, hai header thuật toán, ssp_parser.hpp, proxy_uri_sub_resolver.cpp, ci-cmake.yml và CHANGELOG.md; chưa chạy upstream |
| Khoảng trống lấp | Đồng mô phỏng FMI: FMI 1.0 và 2.0 thật, SSP hạn chế, không phải Modelica hay FMI 3 |
| Cơ chế đáng học | • algorithm: fixed_step_algorithm chạy mọi slave song song theo bội số của bước cơ sở; ecco_algorithm điều chỉnh bước theo bảo toàn năng lượng giữa các power bond với safety_factor, min và max step, abs_tolerance, rel_tolerance (hai header thuật toán).<br>• Tách mô tả hệ thống khỏi thực thi: system_structure đọc từ OSP-IS hoặc SSP, model_uri_resolver biến URI thành FMU, execution chạy (docs/main_page.md).<br>• proxyfmu: URI có host và cổng, chạy FMU ở tiến trình tách riêng hoặc từ xa (proxy_uri_sub_resolver.cpp), kèm test proxy.<br>• ssp_parser đọc DefaultExperiment gồm thời gian bắt đầu, dừng và thuật toán (ssp_parser.hpp). |
| Tiêu chí và cách kiểm | tests/ có khoảng 40 file test C++ (thuật toán, FMU v1 v2, SSP, proxy, observer); CI ci-cmake.yml build Debian bookworm Debug và Release cả thư viện chung và tĩnh, kèm CI Conan. Chưa build, chưa chạy. Bản FMI Library trong CI là 3.0.4 (tên thư viện, không phải hỗ trợ FMI 3). |
| Giới hạn và rủi ro | MPL-2.0 (copyleft theo từng file, dễ dùng làm thư viện liên kết). FMU nạp trong tiến trình, tương đương chạy mã không tin cậy; proxyfmu qua mạng cần kiểm kênh và xác thực (chưa đọc). SSP chỉ hạn chế; CHANGELOG dừng ở v0.11.2 (2026-05-18) trong khi version.txt là 0.11.3, nên ghi chú phát hành chậm hơn mã. Số sao trinh sát ghi (76) chưa xác minh. Gói Python, Java và C bọc ngoài không hỗ trợ đủ tính năng theo README. |
| So với | MasterSim (cùng đợt: master đơn giản, có GUI Qt, BSD, chỉ FMI 1 và 2, không SSP); kho chưa có công cụ đồng mô phỏng FMI nào khác; bullet3 và JoltPhysics trong kho là engine vật lý, không cùng nhiệm vụ. |
| Nguồn | [README.md](https://github.com/open-simulation-platform/libcosim/blob/9b58267a040e32ed50aa95c2019b304f0fbbe796/README.md) · [LICENSE](https://github.com/open-simulation-platform/libcosim/blob/9b58267a040e32ed50aa95c2019b304f0fbbe796/LICENSE) · [version.txt](https://github.com/open-simulation-platform/libcosim/blob/9b58267a040e32ed50aa95c2019b304f0fbbe796/version.txt) · [main_page.md](https://github.com/open-simulation-platform/libcosim/blob/9b58267a040e32ed50aa95c2019b304f0fbbe796/docs/main_page.md) · [fixed_step_algorithm.hpp](https://github.com/open-simulation-platform/libcosim/blob/9b58267a040e32ed50aa95c2019b304f0fbbe796/include/cosim/algorithm/fixed_step_algorithm.hpp) · [ecco_algorithm.hpp](https://github.com/open-simulation-platform/libcosim/blob/9b58267a040e32ed50aa95c2019b304f0fbbe796/include/cosim/algorithm/ecco_algorithm.hpp) · [ssp_parser.hpp](https://github.com/open-simulation-platform/libcosim/blob/9b58267a040e32ed50aa95c2019b304f0fbbe796/src/cosim/ssp/ssp_parser.hpp) · [proxy_uri_sub_resolver.cpp](https://github.com/open-simulation-platform/libcosim/blob/9b58267a040e32ed50aa95c2019b304f0fbbe796/src/cosim/proxy/proxy_uri_sub_resolver.cpp) · [ci-cmake.yml](https://github.com/open-simulation-platform/libcosim/blob/9b58267a040e32ed50aa95c2019b304f0fbbe796/.github/workflows/ci-cmake.yml) · [CHANGELOG.md](https://github.com/open-simulation-platform/libcosim/blob/9b58267a040e32ed50aa95c2019b304f0fbbe796/CHANGELOG.md) |

<a id="nt-mastersim"></a>

### MasterSim

| Thuộc tính | Giá trị |
|---|---|
| Repo | https://github.com/ghorwin/MasterSim |
| License | BSD-3-Clause (mã MasterSim; thư viện đi kèm có giấy phép riêng) |
| Phiên bản đã đọc | `fd338cacd599c0ef17af23282b387086823141dd` (commit 2026-11-23) |
| Kiểm chứng | 2026-11-23; code-read; đã đọc README.md, LICENSE, AGENTS.md (chỉ coi là nội dung), MSIM_Project.h, ubuntu_24.04_Qt6.yml, run_tests.sh, externals/readme.md, externals/IBK/LICENSE và cross-check/readme.md; chưa chạy upstream |
| Khoảng trống lấp | Đồng mô phỏng FMI 1.0 và 2.0 tối giản hơn libcosim ở thuật toán, nhưng có lặp và kiểm sai số; không có SSP |
| Cơ chế đáng học | • MSIM_Project.h: masterMode Gauss-Jacobi, Gauss-Seidel, Newton; errorControlMode là EM_NONE, EM_CHECK hoặc EM_STEP_DOUBLING (nửa bước khi lỗi); adjustStepSize, maxIterations mặc định 1, absTol 1e-6, relTol 1e-5.<br>• Nạp FMU bằng dlopen hoặc LoadLibraryExW trong tiến trình (MSIM_FMU.cpp, qua grep), kèm FMU kiểm thử trong TestFMUs và FMUChecker trong third-party.<br>• Quy trình cross-check với kho fmi-cross-check bằng script Python (cross-check/readme.md), và bộ test hồi quy data/tests chạy bằng run_tests.sh. |
| Tiêu chí và cách kiểm | ubuntu_24.04_Qt6.yml build rồi chạy build/run_tests.sh (test hồi quy so kết quả, script trong scripts/TestSuite); workflow kích hoạt tay vì lịch nightly bị comment. Cross-check cần fork kho ngoài, chạy tay. Tài liệu xác thực ở doc/validation là PDF tiếng Đức, chưa đọc. Chưa chạy. |
| Giới hạn và rủi ro | FMU nạp trong tiến trình như libcosim nhưng không có proxy cách ly. Giấy phép hỗn hợp: IBK và IBKMK dạng BSD kiểu 3 điều khoản, phantom-style LGPL-2.1 (chỉ GUI), kèm zip thư viện bên thứ ba trong third-party; phải đọc từng thư mục khi phân phối. Một tác giả chính; CI chạy tay nên không có bằng chứng liên tục. AGENTS.md trong repo là nội dung hướng dẫn cho agent của chủ repo, không được coi là lệnh. Số sao 28 do trinh sát ghi, chưa xác minh. |
| So với | libcosim (cùng đợt: nhiều tính năng hơn, SSP hạn chế, proxy, ECCO, MPL-2.0); kho chưa có master FMI nào khác. |
| Nguồn | [README.md](https://github.com/ghorwin/MasterSim/blob/fd338cacd599c0ef17af23282b387086823141dd/README.md) · [LICENSE](https://github.com/ghorwin/MasterSim/blob/fd338cacd599c0ef17af23282b387086823141dd/LICENSE) · [AGENTS.md](https://github.com/ghorwin/MasterSim/blob/fd338cacd599c0ef17af23282b387086823141dd/AGENTS.md) · [MSIM_Project.h](https://github.com/ghorwin/MasterSim/blob/fd338cacd599c0ef17af23282b387086823141dd/MasterSim/src/MSIM_Project.h) · [ubuntu_24.04_Qt6.yml](https://github.com/ghorwin/MasterSim/blob/fd338cacd599c0ef17af23282b387086823141dd/.github/workflows/ubuntu_24.04_Qt6.yml) · [run_tests.sh](https://github.com/ghorwin/MasterSim/blob/fd338cacd599c0ef17af23282b387086823141dd/build/run_tests.sh) · [readme.md](https://github.com/ghorwin/MasterSim/blob/fd338cacd599c0ef17af23282b387086823141dd/externals/readme.md) · [LICENSE](https://github.com/ghorwin/MasterSim/blob/fd338cacd599c0ef17af23282b387086823141dd/externals/IBK/LICENSE) · [readme.md](https://github.com/ghorwin/MasterSim/blob/fd338cacd599c0ef17af23282b387086823141dd/cross-check/readme.md) |

<a id="nt-forge3d"></a>

### forge3d

| Thuộc tính | Giá trị |
|---|---|
| Repo | https://github.com/milos-agathon/forge3d |
| License | Apache-2.0 OR MIT (lõi); tính năng Pro cần khóa thương mại |
| Phiên bản đã đọc | `6679f554fdfd859b8a8987f296a2600f8633e950` (commit 2026-11-23) |
| Kiểm chứng | 2026-11-23; code-read; đã đọc README.md, determinism.py, `_license.py`, determinism-matrix.yml, public-funnel-monitor.yml, Cargo.toml, pyproject.toml; chưa chạy upstream |
| Khoảng trống lấp | Dựng 3D / WebGPU (địa hình, bản đồ, render headless) |
| Cơ chế đáng học | - `python/forge3d/determinism.py`: cảnh `terra_determinata_v1` sinh từ DEM 129x129 bằng phép float32 chính xác IEEE, IBL .hdr tạo byte-exact; chạy trong subprocess đặt `FORGE3D_DETERMINISTIC=1` và `WGPU_BACKENDS` trước khi import vì backend bị khóa ở lần tạo context GPU đầu.<br>- `.github/workflows/determinism-matrix.yml`: ma trận intel/amd/nvidia/apple/browser/wasm; nvidia là cổng bắt buộc trên runner tự host; các nhánh khác ghi rõ "informational" hoặc dấu ABSENT; chặn `+relaxed-simd`.<br>- `python/forge3d/_license.py`: kiểm khóa Pro ngoại tuyến bằng chữ ký Ed25519, có thời gian ân hạn 14 ngày. |
| Tiêu chí và cách kiểm | Hash vàng nằm ở `tests/goldens/determinism/` (terra_determinata_v1.sha256 và các canary probe/raster); dung sai 0 byte; kiểm bằng máy trong CI nhưng nhiều nhánh GPU chỉ mang tính thông tin trên runner hosted. CI chính có nhiều làn (Fast Contract, ORBIS Wasm, Visual Golden Paths...) mới chỉ đọc tên bước trong ci.yml. |
| Giới hạn và rủi ro | Open core: `MapPlate`, xuất vector và pipeline nhập tòa nhà là Pro, cần khóa thương mại (README); LICENSE là MIT còn LICENSE-APACHE riêng, Cargo.toml ghi `Apache-2.0 OR MIT`. `fetch_dem` tải dữ liệu độ cao từ mạng (README). Workflow `public-funnel-monitor.yml` chạy mỗi giờ để kiểm trang chủ/PyPI của chính dự án, không ảnh hưởng người dùng. AGENTS.md là nhật ký phản tư của agent, không phải hướng dẫn cho người dùng. Tính tất định chỉ chứng minh cho một cảnh tham chiếu, không cho mọi cảnh. Phiên bản 1.52.0. |
| So với | CesiumJS, kepler.gl, GDAL (cùng nhóm địa không gian trong kho) |
| Nguồn | [README.md](https://github.com/milos-agathon/forge3d/blob/6679f554fdfd859b8a8987f296a2600f8633e950/README.md) · [LICENSE](https://github.com/milos-agathon/forge3d/blob/6679f554fdfd859b8a8987f296a2600f8633e950/LICENSE) · [LICENSE-APACHE](https://github.com/milos-agathon/forge3d/blob/6679f554fdfd859b8a8987f296a2600f8633e950/LICENSE-APACHE) · [Cargo.toml](https://github.com/milos-agathon/forge3d/blob/6679f554fdfd859b8a8987f296a2600f8633e950/Cargo.toml) · [pyproject.toml](https://github.com/milos-agathon/forge3d/blob/6679f554fdfd859b8a8987f296a2600f8633e950/pyproject.toml) · [AGENTS.md](https://github.com/milos-agathon/forge3d/blob/6679f554fdfd859b8a8987f296a2600f8633e950/AGENTS.md) · [determinism.py](https://github.com/milos-agathon/forge3d/blob/6679f554fdfd859b8a8987f296a2600f8633e950/python/forge3d/determinism.py) · [_license.py](https://github.com/milos-agathon/forge3d/blob/6679f554fdfd859b8a8987f296a2600f8633e950/python/forge3d/_license.py) · [determinism-matrix.yml](https://github.com/milos-agathon/forge3d/blob/6679f554fdfd859b8a8987f296a2600f8633e950/.github/workflows/determinism-matrix.yml) · [public-funnel-monitor.yml](https://github.com/milos-agathon/forge3d/blob/6679f554fdfd859b8a8987f296a2600f8633e950/.github/workflows/public-funnel-monitor.yml) · [terra_determinata_v1.sha256](https://github.com/milos-agathon/forge3d/blob/6679f554fdfd859b8a8987f296a2600f8633e950/tests/goldens/determinism/terra_determinata_v1.sha256) |

<a id="n2-2026-11-24"></a>

## Nâng trần đợt hai — 23/11/2026

Hồ sơ lập trong đợt nâng trần thứ hai: đọc mã hoặc tài liệu tại commit cố định, chưa chạy upstream; mô tả của trinh sát sai ở nhiều repo nên điều ghi ở đây là điều đã đọc.

<a id="n2-ifc43-spec-development"></a>

### buildingSMART IFC 4.3.x (bản phát triển)

| Thuộc tính | Giá trị |
|---|---|
| Repo | https://github.com/buildingSMART/IFC4.3.x-development |
| License | Đặc tả: CC-BY-ND-4.0; thư mục code/: MIT |
| Phiên bản đã đọc | `0f1c7acb287740d7d40e2d0021c216a9cdf638ab` (commit 2026-11-23) |
| Kiểm chứng | 2026-11-24; code-read; đã đọc LICENSE.md, README.md, code/LICENSE, code/README.md, .github/workflows/pr-validation.yml, code/generators/express.py; chưa chạy upstream |
| Khoảng trống lấp | Nguồn đặc tả IFC 4.3.x để đối chiếu phiên bản schema và cơ chế sinh/kiểm schema bằng máy (không phải IDS validator) |
| Cơ chế đáng học | - Đặc tả viết bằng UML (schemas/*.uml, gộp ở ifc4x3_add2.uml) và Markdown (docs/); bộ sinh trong code/generators (express.py, xsd.py, pset.py, json.py, bsdd.py) tạo EXPRESS, XSD, Pset XML, JSON.<br>- Cổng PR pr-validation.yml: chạy pytest code/tests, sinh EXPRESS từ nhánh PR và nhánh nền rồi so dòng; từng Pset/Qto/entity mới thêm trong diff UML phải có file XML/mục JSON/tài liệu MD tương ứng.<br>- Có chế độ shadow_mode để thử cổng mà không làm hỏng job, và workflow cài SHACL validator (đã thấy bước cài, chưa đọc phần dùng shapes.ttl). |
| Tiêu chí và cách kiểm | Kiểm bằng máy trong CI: cuối file EXPRESS là END_SCHEMA;, số dòng ≥ 10.000, tỷ lệ so baseline trong [0,5; 1,5], mỗi thực thể/Pset mới phải được generator phát ra. Chưa chạy, nên chưa biết các cổng có xanh ở HEAD. |
| Giới hạn và rủi ro | License chia đôi: đặc tả CC-BY-ND 4.0 (chia sẻ nguyên bản được, phân phối bản đã sửa thì không), code/ MIT; mã IFC dev có thể đổi bất kỳ lúc nào, không thay cho bản ISO chính thức; ngưỡng 10.000 dòng và ±50% là heuristic thô. Phần khớp với IDS/chứng nhận phải tìm ở repo khác. |
| So với | ifcopenshell (thư viện đọc/ghi IFC), buildingsmart-ids (đặc tả kiểm yêu cầu thông tin): repo này là nguồn schema, không phải bộ kiểm. |
| Nguồn | [LICENSE.md](https://github.com/buildingSMART/IFC4.3.x-development/blob/0f1c7acb287740d7d40e2d0021c216a9cdf638ab/LICENSE.md) · [README.md](https://github.com/buildingSMART/IFC4.3.x-development/blob/0f1c7acb287740d7d40e2d0021c216a9cdf638ab/README.md) · [LICENSE](https://github.com/buildingSMART/IFC4.3.x-development/blob/0f1c7acb287740d7d40e2d0021c216a9cdf638ab/code/LICENSE) · [README.md](https://github.com/buildingSMART/IFC4.3.x-development/blob/0f1c7acb287740d7d40e2d0021c216a9cdf638ab/code/README.md) · [CI pr-validation.yml](https://github.com/buildingSMART/IFC4.3.x-development/blob/0f1c7acb287740d7d40e2d0021c216a9cdf638ab/.github/workflows/pr-validation.yml) · [express.py](https://github.com/buildingSMART/IFC4.3.x-development/blob/0f1c7acb287740d7d40e2d0021c216a9cdf638ab/code/generators/express.py) |

<a id="n2-pystac"></a>

### PySTAC

| Thuộc tính | Giá trị |
|---|---|
| Repo | https://github.com/stac-utils/pystac |
| License | Apache-2.0 |
| Phiên bản đã đọc | `924560a62579c0e84584fab198f96bdb56ad2547` (commit 2026-11-19) |
| Kiểm chứng | 2026-11-24; code-read; đã đọc LICENSE, README.md, pyproject.toml, `core/pystac/validation/__init__.py`, core/pystac/validation/stac_validator.py, core/pystac/validation/local_validator.py; chưa chạy upstream |
| Khoảng trống lấp | Chuẩn cloud-native cho dữ liệu không gian: lớp tạo và kiểm catalog STAC bằng schema |
| Cơ chế đáng học | - core/pystac/validation/stac_validator.py: JsonSchemaSTACValidator kiểm core rồi từng extension theo schema URI; schema lõi lấy từ cache cục bộ (local_validator.py, STAC 1.1.0), schema khác tải qua StacIO, có tham số allow_list giới hạn base URL.<br>- `validation/__init__.py`: validate (một đối tượng), validate_all và validate_all_dict (đệ quy theo link con/item), ném STACValidationError kèm best_match của jsonschema.<br>- Thay được validator qua STACValidator trừu tượng và set_validator; extension tách thành gói pystac-ext-* riêng. |
| Tiêu chí và cách kiểm | CI chạy pre-commit lint rồi pytest tests --block-network --record-mode=none (ma trận Python 3.10-3.13 trên Linux/Windows/macOS); coverage fail_under = 65 trong pyproject. Chưa chạy lại. |
| Giới hạn và rủi ro | Validation cần cài jsonschema (extra validation), nếu không thiếu thư viện thì không kiểm; schema extension mặc định tải từ mạng nên cần allow_list hoặc cache khi chạy trong CI cô lập; ngưỡng coverage 65% khá thấp; cassette HTTP ghi sẵn cho test. |
| So với | stac-geoparquet (STAC dạng GeoParquet), opengeospatial-geoparquet (định dạng), geopandas-geopandas (dataframe không gian). |
| Nguồn | [LICENSE](https://github.com/stac-utils/pystac/blob/924560a62579c0e84584fab198f96bdb56ad2547/LICENSE) · [README.md](https://github.com/stac-utils/pystac/blob/924560a62579c0e84584fab198f96bdb56ad2547/README.md) · [pyproject.toml](https://github.com/stac-utils/pystac/blob/924560a62579c0e84584fab198f96bdb56ad2547/pyproject.toml) · [`__init__.py`](https:`//github.com/stac-utils/pystac/blob/924560a62579c0e84584fab198f96bdb56ad2547/core/pystac/validation/__init__.py`) · [stac_validator.py](https://github.com/stac-utils/pystac/blob/924560a62579c0e84584fab198f96bdb56ad2547/core/pystac/validation/stac_validator.py) · [local_validator.py](https://github.com/stac-utils/pystac/blob/924560a62579c0e84584fab198f96bdb56ad2547/core/pystac/validation/local_validator.py) · [CI continuous-integration.yml](https://github.com/stac-utils/pystac/blob/924560a62579c0e84584fab198f96bdb56ad2547/.github/workflows/continuous-integration.yml) |

<a id="n2-titiler"></a>

### TiTiler

| Thuộc tính | Giá trị |
|---|---|
| Repo | https://github.com/developmentseed/titiler |
| License | MIT |
| Phiên bản đã đọc | `92f9afbf614f190898d8a605433ffa5e877b15eb` (commit 2026-11-16) |
| Kiểm chứng | 2026-11-24; code-read; đã đọc LICENSE, README.md, SECURITY.md, AGENT.md, src/titiler/core/titiler/core/factory.py, src/titiler/core/titiler/core/dependencies.py; chưa chạy upstream |
| Khoảng trống lấp | Chuẩn cloud-native cho dữ liệu không gian: lớp phục vụ tile động từ COG/STAC |
| Cơ chế đáng học | - factory.py: TilerFactory.tile đăng ký /tiles/{tileMatrixSetId}/{z}/{x}/{y}, mở dataset trong rasterio.Env(**env) bằng reader tiêm được; mọi tham số tách thành dependency thay thế được (path, reader, layer, colormap, render).<br>- dependencies.py: DatasetPathParams là điểm cắm để giới hạn nguồn; application/settings.py có biến TITILER_API_*, gồm disable_cog/stac/mosaic/zarr, global_access_token (query access_token), telemetry_enabled=false mặc định.<br>- core/telemetry.py: OpenTelemetry tùy chọn (no-op nếu không cài opentelemetry), SECURITY.md hướng dẫn tắt VRT driver và các tùy chọn GDAL_VRT_* (GDAL 3.12). |
| Tiêu chí và cách kiểm | CI cicd.yml: ma trận Python 3.11-3.14, pre-commit và mypy ở bản mới nhất, rồi scripts/test chạy pytest từng module (core, xarray, mosaic, application, extensions) kèm coverage gửi Codecov; còn các workflow scorecard, zizmor, benchmark. Chỉ đọc cicd.yml, không đọc các workflow còn lại. |
| Giới hạn và rủi ro | Mặc định nhận url tùy ý và CORS *, không có allowlist nguồn (nguy cơ SSRF/đọc file là suy luận của hồ sơ này); cần tự giới hạn khi mở ra Internet; global_access_token chỉ là một khoá chung trong query; phụ thuộc GDAL/rasterio (rủi ro I/O); AGENT.md là hướng dẫn cho agent của chính repo, chỉ đọc làm dữ liệu. |
| So với | osgeo-gdal (thư viện I/O nền), geoparquet-io (công cụ GeoParquet), stac-geoparquet; chưa có tile server khác trong nhóm này của kho. |
| Nguồn | [LICENSE](https://github.com/developmentseed/titiler/blob/92f9afbf614f190898d8a605433ffa5e877b15eb/LICENSE) · [README.md](https://github.com/developmentseed/titiler/blob/92f9afbf614f190898d8a605433ffa5e877b15eb/README.md) · [SECURITY.md](https://github.com/developmentseed/titiler/blob/92f9afbf614f190898d8a605433ffa5e877b15eb/SECURITY.md) · [AGENT.md](https://github.com/developmentseed/titiler/blob/92f9afbf614f190898d8a605433ffa5e877b15eb/AGENT.md) · [factory.py](https://github.com/developmentseed/titiler/blob/92f9afbf614f190898d8a605433ffa5e877b15eb/src/titiler/core/titiler/core/factory.py) · [dependencies.py](https://github.com/developmentseed/titiler/blob/92f9afbf614f190898d8a605433ffa5e877b15eb/src/titiler/core/titiler/core/dependencies.py) · [settings.py](https://github.com/developmentseed/titiler/blob/92f9afbf614f190898d8a605433ffa5e877b15eb/src/titiler/application/titiler/application/settings.py) · [telemetry.py](https://github.com/developmentseed/titiler/blob/92f9afbf614f190898d8a605433ffa5e877b15eb/src/titiler/core/titiler/core/telemetry.py) · [CI cicd.yml](https://github.com/developmentseed/titiler/blob/92f9afbf614f190898d8a605433ffa5e877b15eb/.github/workflows/cicd.yml) · [test](https://github.com/developmentseed/titiler/blob/92f9afbf614f190898d8a605433ffa5e877b15eb/scripts/test) |

<a id="n2-ogcapi-features"></a>

### OGC API - Features (đặc tả)

| Thuộc tính | Giá trị |
|---|---|
| Repo | https://github.com/opengeospatial/ogcapi-features |
| License | OGC License (tùy biến, giống MIT nhưng bản sửa phải ghi chú chưa được OGC duyệt) |
| Phiên bản đã đọc | `3c2c8dda19ad5287c6a021c73c925c430542ba04` (commit 2026-11-23) |
| Kiểm chứng | 2026-11-24; docs-read; đã đọc LICENSE, README.md, core/standard/clause_2_conformance.adoc, core/standard/abstract_tests/ATS_class_core.adoc, core/standard/abstract_tests/core/ATS_api-definition-op.adoc, core/openapi/ogcapi-features-1.yaml; chưa chạy upstream |
| Khoảng trống lấp | Chuẩn cloud-native cho dữ liệu không gian: đặc tả API đặc trưng với test conformance dạng ATS |
| Cơ chế đáng học | - core/standard/abstract_tests: ATS_class_core.adoc include từng test (mục đích, yêu cầu, phương pháp) cho mỗi conformance class; core/openapi/ogcapi-features-1.yaml là định nghĩa OpenAPI 3.0 dùng lại được.<br>- extensions/transactions/.../executable-tests: run_ats.py (chỉ stdlib) chạy ATS Part 4 với --landing-page, test không đủ điều kiện conformance thì SKIP kèm lý do; docker-compose dựng PostGIS và ldproxy.<br>- README liệt kê validator chính thức (TEAM Engine của OGC) và OGC Checker (Geonovum, kiểm bản 1.0.1 Part 1) để kiểm API thật. |
| Tiêu chí và cách kiểm | ATS là văn bản, không tự chạy; riêng transactions có runner thử (exit code qua run-tests.sh, chưa chạy). Bộ kiểm chính thức và chương trình chứng nhận nằm ngoài repo (TEAM Engine). Không có workflow CI (git ls-files không có .github). |
| Giới hạn và rủi ro | License OGC tùy biến (không phải SPDX chuẩn, bản sửa phải ghi chú chưa được OGC duyệt), nên không tính nguồn mở theo OSI; kho không tự kiểm đặc tả bằng CI; executable-tests là bản thử khi soạn ATS, tuyên bố đầy đủ phụ thuộc README tác giả (chưa xác minh). |
| So với | opengeospatial-geoparquet (đặc tả OGC liên quan), spectral (kiểm OpenAPI cho hợp đồng API). |
| Nguồn | [LICENSE](https://github.com/opengeospatial/ogcapi-features/blob/3c2c8dda19ad5287c6a021c73c925c430542ba04/LICENSE) · [README.md](https://github.com/opengeospatial/ogcapi-features/blob/3c2c8dda19ad5287c6a021c73c925c430542ba04/README.md) · [clause_2_conformance.adoc](https://github.com/opengeospatial/ogcapi-features/blob/3c2c8dda19ad5287c6a021c73c925c430542ba04/core/standard/clause_2_conformance.adoc) · [ATS_class_core.adoc](https://github.com/opengeospatial/ogcapi-features/blob/3c2c8dda19ad5287c6a021c73c925c430542ba04/core/standard/abstract_tests/ATS_class_core.adoc) · [ATS_api-definition-op.adoc](https://github.com/opengeospatial/ogcapi-features/blob/3c2c8dda19ad5287c6a021c73c925c430542ba04/core/standard/abstract_tests/core/ATS_api-definition-op.adoc) · [ogcapi-features-1.yaml](https://github.com/opengeospatial/ogcapi-features/blob/3c2c8dda19ad5287c6a021c73c925c430542ba04/core/openapi/ogcapi-features-1.yaml) · [README.md](https://github.com/opengeospatial/ogcapi-features/blob/3c2c8dda19ad5287c6a021c73c925c430542ba04/extensions/transactions/create-replace-update-delete/executable-tests/README.md) · [docker-compose.yml](https://github.com/opengeospatial/ogcapi-features/blob/3c2c8dda19ad5287c6a021c73c925c430542ba04/extensions/transactions/create-replace-update-delete/executable-tests/docker-compose.yml) |

<a id="n2-fmpy"></a>

### FMPy

| Thuộc tính | Giá trị |
|---|---|
| Repo | https://github.com/CATIA-Systems/FMPy |
| License | BSD-2-Clause (icon: CC-BY-4.0) |
| Phiên bản đã đọc | `e42e288f448830c5f146ae334b38e91d17ff19fa` (commit 2026-09-09) |
| Kiểm chứng | 2026-11-24; code-read; đã đọc LICENSE.txt, README.md, pyproject.toml, src/fmpy/validation.py, src/fmpy/cli.py, src/fmpy/model_description.py; chưa chạy upstream |
| Khoảng trống lấp | Đồng mô phỏng FMI/SSP: cổng kiểm FMU bằng máy |
| Cơ chế đáng học | - validation.py: validate_fmu mở file/thư mục FMU, cảnh báo đường dẫn có dấu gạch ngược, rồi gọi read_model_description(validate=True, validate_variable_names=True, validate_model_structure=True) và trả danh sách vấn đề.<br>- model_description.py: kiểm XSD theo phiên bản (src/fmpy/schema/fmi1, fmi2, fmi3) bằng lxml, ném ValidationError kèm các lỗi.<br>- cli.py: lệnh fmpy validate in số vấn đề và thoát bằng sys.exit(len(problems)); tests/test_validation.py có các hàm test cho dẫn xuất, tên biến, giá trị bắt đầu (chỉ thấy tên hàm). |
| Tiêu chí và cách kiểm | Cổng máy đọc được: XSD cộng các luật ngữ nghĩa trong validation.py; CI build.yml dựng binary và wheel ba nền tảng rồi chạy pytest tests (Python 3.10). Exit code = số lỗi nên giá trị lớn có thể bị cắt modulo 256 và không phân biệt loại lỗi; chưa chạy. |
| Giới hạn và rủi ro | validate chỉ đọc modelDescription, không thực thi FMU; simulate nạp binary FMU (mã gốc, không sandbox) nên FMU lạ là mã không tin cậy; build kéo submodule Reference-FMUs và mpack, gói có binary dựng sẵn; tuyên bố hỗ trợ đầy đủ FMI 3.0 là của tác giả (chưa xác minh). |
| So với | modelon-pyfmi (thư viện FMI khác), openmodelica-omsimulator (đồng mô phỏng/SSP). |
| Nguồn | [LICENSE.txt](https://github.com/CATIA-Systems/FMPy/blob/e42e288f448830c5f146ae334b38e91d17ff19fa/LICENSE.txt) · [README.md](https://github.com/CATIA-Systems/FMPy/blob/e42e288f448830c5f146ae334b38e91d17ff19fa/README.md) · [pyproject.toml](https://github.com/CATIA-Systems/FMPy/blob/e42e288f448830c5f146ae334b38e91d17ff19fa/pyproject.toml) · [validation.py](https://github.com/CATIA-Systems/FMPy/blob/e42e288f448830c5f146ae334b38e91d17ff19fa/src/fmpy/validation.py) · [cli.py](https://github.com/CATIA-Systems/FMPy/blob/e42e288f448830c5f146ae334b38e91d17ff19fa/src/fmpy/cli.py) · [model_description.py](https://github.com/CATIA-Systems/FMPy/blob/e42e288f448830c5f146ae334b38e91d17ff19fa/src/fmpy/model_description.py) · [CI build.yml](https://github.com/CATIA-Systems/FMPy/blob/e42e288f448830c5f146ae334b38e91d17ff19fa/.github/workflows/build.yml) · [.gitmodules](https://github.com/CATIA-Systems/FMPy/blob/e42e288f448830c5f146ae334b38e91d17ff19fa/.gitmodules) |
