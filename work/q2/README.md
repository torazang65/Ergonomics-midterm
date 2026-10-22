# Q2 작업 지시

## 읽을 자료

시험지 p.6-8 원본, 3장 p.16-48 및 p.54-61 원본, definitions.md. 계산 전에 원본 표·수식을 대조한다.

## 현재 할 일·산출물

1. definitions.md에 조건부 분모, d′·β 정의·가정, X/Y 방향, 로그 밑·0항 처리 확정.
2. 시험 원자료를 직접 대조해 입력 파일 작성.
3. 별도 계산 요청 시 scripts/verify_q2.py 구현 후 계산 결과와 검산 기록 저장.
4. 기존 풀이를 제공하지 않은 별도 세션에서 문제 데이터와 확정 정의만으로 독립 검산.
5. 검증된 결과와 강의 근거를 바탕으로 해석 작성.

## 완료 기준

- 표본 수, 행·열 합, 확률의 합·범위를 검증.
- T=H(X)+H(Y)-H(X,Y), H(Y|X)=H(X,Y)-H(X), H(X|Y)=H(X,Y)-H(Y) 확인.
- 0≤T≤min(H(X),H(Y)), 조건부 엔트로피 비음성 확인.
- 반올림 전 수치로 계산하고 마지막에만 반올림.
- 성능·판단 기준·정보 전달·오류 비용·UI 영향을 구분.

## 상태 (2026-10-22)

1~4 완료: definitions.md 확정, input.json, verify_output.txt, independent-check.md. 5는 results.md에 분석 메모로 작성했다. Codex·Claude CLI 초안 비교 기록은 reviews/에, 최종 답안은 ../../output/q2-final-answer.md에 있다.
