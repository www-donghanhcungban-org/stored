#!/usr/bin/env python3
"""Sinh catalog con trong catalog/ từ data/projects.json + data/taxonomy.json; --check báo lỗi nếu file đã sinh bị cũ."""
import argparse
import json
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
LEVEL_VI = {'code-read': 'đọc mã', 'docs-read': 'đọc tài liệu', 'checks-run': 'đã chạy kiểm', 'reproduced': 'tái lập', 'unassessed': 'chưa chuẩn hóa'}
HEADER = '<!-- File sinh tự động bởi scripts/build_catalog_views.py; sửa data/projects.json hoặc data/taxonomy.json rồi chạy lại. -->\n\n'


def cell(text):
    return str(text).replace('\\', '\\\\').replace('|', '\\|').replace('\n', ' ').strip()


def summary(notes, limit=170):
    s = re.split(r'(?<=[.;])\s', notes.strip(), maxsplit=1)[0]
    return s if len(s) <= limit else s[:limit - 1].rstrip() + '…'


def stars(p):
    return f"{p['stars']:,}".replace(',', '.') if isinstance(p.get('stars'), int) else '—'


def link(p, depth):
    target = p.get('profile_anchor') or p.get('profile_path')
    return f"[{cell(p['name'])}]({'../' * depth}{target})"


def row(p, depth):
    level = LEVEL_VI.get(p.get('verification_level') or 'unassessed', '')
    date = p.get('last_verified_at', '')
    repo = f"`{p['repo']}`" if p.get('repo') else ''
    return f"| {link(p, depth)} | {repo} | {cell(p.get('license') or '—')} | {stars(p)} | {level} {date}".rstrip() + f" | {p['section']} | {cell(summary(p['notes']))} |"


TABLE = '| Dự án | Repo | License | ★ | Bằng chứng | Mục | Tóm tắt |\n|---|---|---|---|---|---|---|\n'


def order(p):
    return (-(p['stars'] if isinstance(p.get('stars'), int) else -1), p['name'].lower())


def render(root):
    data = json.loads((root / 'data/projects.json').read_text(encoding='utf-8'))
    tax = json.loads((root / 'data/taxonomy.json').read_text(encoding='utf-8'))
    by_cat = {}
    for p in data['projects']:
        by_cat.setdefault(p['category'], []).append(p)
    files = {}
    idx = [HEADER + '# Catalog theo nhóm, danh mục và danh mục con\n',
           f"Sinh từ `data/projects.json` ({len(data['projects'])} hồ sơ) theo `data/taxonomy.json`. Mỗi dòng dẫn về hồ sơ gốc trong README chuyên mục; số sao và mức bằng chứng chỉ đúng tại ngày ghi trong hồ sơ. Sắp xếp theo ★ giảm dần; ★ để trống là chưa có số tin cậy.\n",
           'Chọn công cụ theo tác vụ: xem [PLAYBOOK.md](../PLAYBOOK.md) (skill/tính năng đã chắt lọc kèm cách áp dụng) và [GUIDES.md](../GUIDES.md).\n']
    for g, gv in tax['groups'].items():
        n = sum(len(by_cat.get(c, [])) for c in gv['categories'])
        idx.append(f"## {gv['label']} ({n})\n")
        idx.append('| Danh mục | Số hồ sơ | Danh mục con |\n|---|---|---|')
        for c, cv in gv['categories'].items():
            ps = by_cat.get(c, [])
            subs = cv.get('subcategories', {})
            sub_txt = ', '.join(f"{lab} ({sum(1 for p in ps if p.get('subcategory') == k)})" for k, lab in subs.items()) or '—'
            idx.append(f"| [{c}]({g}/{c}.md) | {len(ps)} | {cell(sub_txt)} |")
            out = [HEADER + f"# {c} — {gv['label']}\n", f"[← Mục lục catalog](../README.md) · {len(ps)} hồ sơ.\n"]
            if subs:
                for k, lab in subs.items():
                    sp = sorted((p for p in ps if p.get('subcategory') == k), key=order)
                    if not sp:
                        continue
                    out.append(f"## {lab} (`{k}`, {len(sp)})\n")
                    out.append(TABLE + '\n'.join(row(p, 2) for p in sp) + '\n')
            else:
                out.append(TABLE + '\n'.join(row(p, 2) for p in sorted(ps, key=order)) + '\n')
            files[f'catalog/{g}/{c}.md'] = '\n'.join(out).rstrip() + '\n'
        idx.append('')
    files['catalog/README.md'] = '\n'.join(idx).rstrip() + '\n'
    return files


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--root', type=Path, default=ROOT)
    ap.add_argument('--check', action='store_true')
    a = ap.parse_args()
    files = render(a.root)
    existing = {str(p.relative_to(a.root)) for p in (a.root / 'catalog').rglob('*.md')} if (a.root / 'catalog').exists() else set()
    stale = sorted(k for k, v in files.items() if not (a.root / k).is_file() or (a.root / k).read_text(encoding='utf-8') != v)
    extra = sorted(existing - set(files))
    if a.check:
        if stale or extra:
            print('catalog/ cũ so với dữ liệu; chạy python3 -I scripts/build_catalog_views.py\n' + '\n'.join(stale + extra)); return 1
        print(f'OK: catalog/ khớp dữ liệu ({len(files)} file).'); return 0
    for k in extra:
        (a.root / k).unlink()
    for k, v in files.items():
        (a.root / k).parent.mkdir(parents=True, exist_ok=True)
        (a.root / k).write_text(v, encoding='utf-8')
    print(f'Đã ghi {len(files)} file, xóa {len(extra)} file thừa.'); return 0


if __name__ == '__main__':
    sys.exit(main())
