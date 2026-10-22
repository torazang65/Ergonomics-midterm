# 도구

- extract_sources.py: pypdf로 원본 PDF를 페이지별 Markdown으로 추출한다. 원본 해시·페이지 수·텍스트 부족 페이지를 manifest에 기록한다.
- verify_q2.py: Q2 SDT·정보량 계산과 자동 검산. `python3 scripts/verify_q2.py` → 결과는 work/q2/verify_output.txt에 저장해 둠.

재추출은 notes/text/manifest를 덮어쓰므로 수동 요약은 sources/summaries에 작성한다.
