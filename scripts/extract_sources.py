"""PDF 원본을 보존하고 페이지별 검색용 Markdown과 추출 상태를 생성한다."""
from pathlib import Path
import hashlib
import json
import re
import unicodedata
from urllib.parse import quote
from pypdf import PdfReader

ROOT = Path(__file__).resolve().parents[1]
NAMES = {'Lecture 1': '01-introduction', '2장': '02-research-methods', '3장': '03-cognition', '2026 4장': '04-perception-decision', '5장': '05-vision', '6장': '06-displays', '8장': '08-controls', 'laddering': '09-laddering-cjm'}

def main():
    records = []
    for src in sorted((ROOT / 'sources').rglob('*.pdf')):
        name = unicodedata.normalize('NFC', src.name)
        is_lecture = src.parent.name == 'lectures'
        slug = next((v for k, v in NAMES.items() if name.startswith(k)), src.stem) if is_lecture else ('exam' if 'midterm' in name else 'syllabus')
        dest = ROOT / 'sources' / ('notes' if is_lecture else 'text') / f'{slug}.md'
        dest.parent.mkdir(parents=True, exist_ok=True)
        pages = [(p.extract_text() or '').strip() for p in PdfReader(src).pages]
        sparse = [i for i,t in enumerate(pages,1) if len(re.sub(r'\s','',t)) < 60]
        link = quote(str(src.relative_to(dest.parent)), safe='/') if src.is_relative_to(dest.parent) else quote('../' + str(src.relative_to(ROOT / 'sources')), safe='/')
        out = [f'# {name}', '', f'- 원본: [{name}]({link})', f'- PDF 페이지 수: {len(pages)}', '- 성격: 자동 추출한 검색용 텍스트. 요약이나 교정본이 아님.', '- 페이지 번호는 PDF의 1부터 시작하는 물리 페이지 번호. 인쇄된 슬라이드 번호와 다를 수 있음.', '- 수식·표·그림·읽기 순서는 손실될 수 있으므로 인용·계산 전에 원본 확인 필요.', f'- 텍스트 부족 페이지(그림 중심 또는 추출 누락 가능): {", ".join(map(str,sparse)) or "없음"}', '', '## 페이지 탐색', '']
        for i,t in enumerate(pages,1):
            title = next((s.strip() for s in t.splitlines() if s.strip()), '텍스트 없음')[:85].replace('|','/')
            out.append(f'- [PDF p. {i}: {title}](#pdf-page-{i})')
        for i,t in enumerate(pages,1):
            out += ['', f'<a id="pdf-page-{i}"></a>', f'## PDF p. {i}', '']
            if i in sparse: out += ['> 텍스트 부족: 그림·도표·수식 포함 여부를 원본에서 확인하세요.', '']
            out += [t or '[추출 가능한 텍스트 없음]', '']
        dest.write_text('\n'.join(out), encoding='utf-8')
        records.append(dict(source=str(src.relative_to(ROOT)), markdown=str(dest.relative_to(ROOT)), pages=len(pages), sparse_pages=sparse, sha256=hashlib.sha256(src.read_bytes()).hexdigest()))
    (ROOT/'sources/extraction-manifest.json').write_text(json.dumps(records,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    for r in records: print(f'{r["markdown"]}: {r["pages"]} pages; {len(r["sparse_pages"])} sparse')

if __name__ == '__main__': main()
