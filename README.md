> **먼저 [SECURITY_RULES.md](SECURITY_RULES.md)를 읽으세요.** 최우선: SECURITY_RULES.md를 먼저 읽어라. 준비 단계 Git push는 허용하되 실제 문제를 본 이후 Git push·외부 전송·게시·공유는 금지한다. 허용된 Codex와 로컬 Playwright E2E는 사용 가능하다. Computer use·캡처/녹화/스냅샷/트레이스·보안 우회는 금지한다.

# COFA 개인 플레이북 · 제한시간 문제 해결

**본선 마감: 15:00 제품+발표 HTML, 15:30 서술형. [전체 퀵스타트](QUICKSTART.md) · [HTML 세션 프롬프트](prompts/FINALS_H.md).**

**처음에는 분석과 계획만. 내가 읽고 “구현 시작”을 지시한 뒤 워크트리 구현 → 독립 검증 → 기록·복습으로 진행합니다.**

1. **[QUICKSTART.md](QUICKSTART.md)** — 세션 A/B/C에 순서대로 복붙할 명령. 여기부터 읽으세요.
2. **[핵심 질문 7개](docs/핵심질문7개.md)** — 기출 유형 기반 예상 질문과 실제 구현에서 준비할 근거.
3. **[START_HERE.md](START_HERE.md)** — 계획·역할·워크트리·검증·기록 운영 규칙.

추가 자료: [6쪽 PDF 운영안](pdf/COFA_PLAYBOOK.pdf) · [빈 설명 양식](templates/PROJECT_DEFENSE.md)

## 본선 준비

특정 문제 내용을 포함하지 않는 일반 준비 자료. [현업 UX](docs/FIELD_UX.md) · [디자인 스킬 목록](docs/DESIGN_SKILLS.md) · [설치 명령](DESIGN_SKILLS_START.txt).

본선은 **[FINALS.md](FINALS.md)**에서 시작합니다. 반도체 현장 문제의 데이터·제약 확인과 유형별 검증을 보강했습니다. A가 PLAN에서 계약과 작업 경계를 정하고 승인 후 독립 작업을 Worktree로 병렬 구현합니다. A 통합 후 B가 고정 버전을 검증하며, 병렬화 이득이 작으면 순차 구현합니다. [현장 복붙 TXT](FIELD_START.txt) · [AI 첫 프롬프트 TXT](FIRST_PROMPT.txt)를 제공합니다. 예선 운영안은 docs/QUALIFIER_QUICKSTART.md에 보존하고 QUICKSTART를 본선 전체 흐름으로 갱신했습니다. [90분 합성 연습 문제](practice/BRIEF.md)로 리허설할 수 있습니다.

기존 PDF는 예선 운영안이며 이번 본선 추가 내용을 포함하지 않습니다.

## 자료 받기

제공된 과제 루트에서 실행하고 그 위치에 머무릅니다.

```sh
git clone --depth 1 https://github.com/YounghwanKil/cofa-personal-playbook.git .cofa-playbook
```

이미 받고 준비 문서를 수정하지 않았다면 `git -C .cofa-playbook pull --ff-only`.

## 세션 구성

| 세션 | 역할 | 시작 시점 |
|---|---|---|
| A 구현·통합 | 처음에는 깊은 분석과 PLAN만, 승인 후 구현·워크트리 배정·통합 | 처음부터 |
| B 검증 | 고정된 변경 묶음을 검사하고 REVIEW 작성 | 첫 검토 묶음 준비 후 |
| H 발표 HTML | 전용 Worktree에서 발표 HTML·자산 제작 | 계약 확정·구현 승인 후 |
| C 서술형 | 실제 근거로 구현 과정·검증·가정 기록 | 주요 결과부터, 15:00 이후 최종화 |

처음에는 A만 엽니다. 별도 세션은 대화·실행 상태가 자동 공유되지 않으므로 파일로 인계하고 QUICKSTART의 명령으로 재개합니다. 도구·동시 세션이 허용되지 않으면 A가 순서대로 수행합니다.

운영진 질문도 A가 작성하고 사용자는 실제 답변을 전달합니다. 일반 기술 선택은 A가 추천합니다. 현재 공식 지침이 우선이며 실제 과제 코드·고객 답변·기록은 준비 저장소에 올리지 않습니다.
