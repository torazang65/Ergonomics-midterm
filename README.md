# 인간공학 중간고사 작업 공간

첨부한 설계에 따라 원본, 근거, 분석, 제출물을 구분한다. 현재는 자료 정리와 작업 서식만 준비된 상태이며 시험 답안·최초 AI 응답·현장 증거·계산 결과는 작성하지 않았다.

```text
AGENTS.md / CLAUDE.md       공통 작업 지침
sources/
  *.pdf                    시험지·syllabus 원본 (기존 이름 유지)
  lectures/*.pdf           강의 PDF 원본 8개
  notes/*.md               강의별 페이지 단위 검색 텍스트 8개
  summaries/*.md           강의별 핵심 개념 정리 8개
  text/                    시험지·syllabus 검색 텍스트
  index.md                 개념·문항별 원본 페이지 색인
  extraction-manifest.json 원본 SHA-256·페이지 수·추출 상태
evidence/
  q1/                      최초 응답·UI 사용 기록·screenshots/
  q3/                      현장 기록·photos/·sketches/
work/
  q1/                      요구사항·주장 검토·설계 연결
  q2/                      정의 확인·계산 검증 기준
  q3/                      관찰 분석·대안·프로토타입·테스트 계획
scripts/                   PDF 텍스트 재추출 도구
references/                외부 출처와 주장 연결
output/                    최종 제출물
```

## 시작점

1. [자료 색인](sources/index.md)에서 필요한 개념을 찾고 강의 요약과 해당 PDF 페이지를 읽는다.
2. Q1(a)는 별도 새 대화에서 시험 프롬프트만 입력하고 [최초 응답 기록](evidence/q1/initial-response.md)에 저장한다.
3. 직접 UI를 사용하거나 현장을 관찰한 뒤 evidence에 사실을 기록한다.
4. 문항별 work/README.md에 따라 근거와 분석을 연결한다.
5. 최종 답안 요청 후 output/에 제출물을 만든다.

## 자료 상태와 확인 사항

- 강의 8개, 580페이지. 요약은 시험 관련 핵심 개념의 탐색용 정리이며 모든 슬라이드의 완전한 전사가 아니다.
- 텍스트가 적은 페이지는 추출본과 manifest에 표시했다. 그림·수식·표의 읽기 순서와 정확성은 PDF에서 확인해야 한다. 전체 페이지의 시각 검수나 OCR은 수행하지 않았다.
- 원본 PDF의 파일명과 위치는 유지했다. Markdown 파일명만 검색하기 쉬운 이름으로 정했다.
- 시험지 PDF p.1: **2026-10-23 09:30 제출**. Syllabus p.2의 10/22 제출 표기 및 p.3 중간고사 일정과 차이가 있어 최신 공지 확인 필요. 현재 작업 기준은 시험지다.
- Q3 지문은 5단계를 명시하지만 답안 항목은 프로토타입까지다. work/q3에 테스트 계획 공간을 확보했으며 실제 수행 여부를 구분한다.
- 주교재는 syllabus p.1에 있는 《사용자 중심 디자인을 위한 인간공학》(2021). 교재 본문은 현재 sources에 없으므로 교재 페이지를 추정해 인용하지 않는다.

## 재추출

pypdf가 설치된 Python으로 `python scripts/extract_sources.py` 실행. sources/notes, sources/text, extraction-manifest.json을 갱신한다. summaries와 index의 수동 정리는 자동 갱신하지 않으므로 원본 교체 시 재검토한다. 원본은 수정하지 않는다.
