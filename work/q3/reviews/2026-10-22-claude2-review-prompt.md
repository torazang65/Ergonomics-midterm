# Q3 A안 답안 초안 Claude CLI 별도 세션 비판 검토 요청

이 요청은 현재 Q3 답안 초안에 대한 비판 검토다. 독립 검산이나 실제 사용성 실험이 아니다. 한국어로 답하라. 파일은 수정하지 말고 로컬 자료만 Read 도구로 읽어라. 초안의 결론에 동의하는 것을 목표로 삼지 마라. 새로운 관찰·인터뷰·테스트 결과나 수치를 만들지 마라.

## 배경

- 이 초안은 문제를 최초 기록의 핵심으로 되돌린 판본이다. 핵심 문제: Mac 창 개요에서 다른 앱은 창이 하나라 빨리 찾지만, 카카오톡은 채팅마다 창이 생겨 비슷한 창 여러 개 중 원하는 상대를 찾기 어렵다. 선택안은 A(통합 대화 창), 보조안은 C(분리한 창의 큰 상대 이름), B(대화목록 버튼)는 제외했다.
- 이전 검토 work/q3/reviews/2026-10-22-claude-*는 B 초안에 대한 것이다. 그 검토의 지적을 현재 초안이 해소했는지도 확인하라.
- 사용자 자기보고: 10월 22일 저녁 집에서 공부 중 친구에게 질문하려 함 → 네 손가락 창 개요에서 목표를 못 찾음 → Dock에서 카카오톡 → 창 4개가 함께 뜸 → 하나씩 닫으며 찾음. 후속 확인: 목록에서 상대를 고르면 다른 창을 닫지 않고 접근 가능. 불편 당시 목록 창은 열려 있었으나 다른 창들에 가려져 있었음. 시간·오선택·닫은 창 수·화면 거리·글자 크기는 측정하지 않았다.

## 읽을 자료

PDF 파일명은 Unicode 정규화가 다를 수 있으므로 필요하면 디렉터리 목록에서 확인하라. PDF 페이지는 1부터 센다. PDF를 직접 읽을 수 없으면 sources/notes/의 페이지별 자동 추출본(`<a id="pdf-page-N">` 앵커)을 보고, 그 경우 '추출본 기준'이라고 표시하라.

- AGENTS.md, work/q3/README.md
- sources/2026 midterm.pdf PDF p.1, 9-11 (추출본 sources/text/exam.md)
- sources/lectures/3장 보충 2026.pdf PDF p.71, 89, 97, 98, 101 (추출본 sources/notes/03-cognition.md)
- sources/lectures/2026 4장 보충.pdf PDF p.53 (04-perception-decision.md)
- sources/lectures/5장 보충 vision and visual acuity.pdf PDF p.9 (05-vision.md)
- sources/lectures/Lecture 1 인간공학 소개 2026.pdf PDF p.25 (01-introduction.md)
- sources/lectures/6장 디스플레이 보충 2026.pdf PDF p.32 (06-displays.md)
- sources/lectures/8장 콘트롤 보충.pdf PDF p.4 (08-controls.md)
- sources/lectures/2장 보충 인간공학 연구방법론.pdf PDF p.22-23, 32 (02-research-methods.md)
- evidence/q3/observation.md, evidence/q3/2026-10-22-followup-message.txt, evidence/q3/2026-10-22-followup2-message.txt, work/q3/user-followup.md
- 이미지: evidence/q3/photos/Kakaotalk Reference.png, 2026-10-22-followup-list-open.png, output/q3-prototype.png
- 검토 대상: output/q3-answer-draft.md
- 참고 작업 파일: work/q3/process.md, work/q3/followup-analysis.md, work/q3/kakao-return.html, work/q3/reviews/2026-10-22-claude-decisions.md

## 검토 질문

1. 시험 요구(직접 관찰·체험, 문제 하나, 페르소나·페인 포인트, 원리별 원인 진단, HMW와 인지적 한계를 극복하는 아이디어 2개 이상, 최우수안 선정과 구체적 프로토타입)를 충족하는가? 약한 단계를 지적하라.
2. 2단계 네 원인이 강의 원문 정의와 맞는가? 특히 (a) 5장 p.9 시각·시력을 측정 없이 썸네일 이름 식별에 연결한 것, (b) 3장 p.97·98의 시각 탐색·구조화된 탐색을 창 개요 배치에 적용한 것, (c) 소개 p.25 '작업을 인간에게 맞추자'를 원인 진단으로 쓴 것, (d) 유사성 묶음 지각과 4장 p.53 재인 혼동의 연결이 원문 범위 안인지 판단하라. 단순 관련성을 원인 진단으로 대체한 부분을 지적하라.
3. 이미지·자기보고로 뒷받침되는 주장과 추론이 구분되었는가? Kakaotalk Reference.png에서 실제로 보이는 것(카카오톡 창 수, 목록 창 유무, 썸네일에서 이름 가독성)과 초안 서술을 대조하라. 과장이나 관찰되지 않은 사실을 찾아라.
4. A 선택이 진단과 논리적으로 이어지는가? A가 만드는 새 부담(목표가 마지막 대화와 다를 때의 추가 선택, 동시 비교, 기존 습관)을 충분히 다뤘는가? 카카오톡에 이미 비슷한 보기 설정이 있을 가능성처럼 확인하지 않은 전제가 결론을 흔드는지 판단하라. B 제외 이유는 타당한가?
5. 그림 output/q3-prototype.png와 모형 kakao-return.html이 4단계 서술을 넘어서지 않는가? 실제 캡처와 모의 화면의 구분이 분명한가?
6. 5단계 계획의 편향·실행 가능성, 분량(시험지 p.1 지시), 중복, 문장, 제출 형식(이미지 상대경로 등)을 지적하라.

## 출력

- 전체 판정: 진행 가능 / 보완 후 가능 / 주제 재선정 필요.
- 중요한 지적부터 번호를 매겨 '문제 위치(단계·문장), 근거(원본 파일명과 PDF 페이지 또는 이미지), 구체 수정안'을 제시하라. 없으면 없다고 하라.
- 원문이나 이미지를 직접 확인하지 못한 부분은 명시하고 페이지·기능을 추정하지 마라.
- 짧은 수정 문단을 제안할 수 있으나 새로운 관찰이나 수치를 만들지 마라.
