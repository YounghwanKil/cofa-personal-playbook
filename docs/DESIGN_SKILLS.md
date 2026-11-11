# 시작 시 검토할 디자인 스킬

2026-11-11 원본 경로와 설명 확인. 아직 사용자 환경에 설치하지 않았다. 스킬은 모델 지침이며 브라우저·MCP·Node 같은 실행 도구를 자동으로 모두 설치하는 것은 아니다. 외부 도구 허용은 공식 규정 우선이다. 설치/인식에 5분 이상 막히면 FIELD_UX와 기존 브라우저로 진행한다.

| 우선순위 | 스킬·출처 | 담당과 쓰임 | 조건 |
|---|---|---|---|
| 1 | [frontend-design](https://github.com/anthropics/skills/tree/main/skills/frontend-design) — Anthropic 제공, OpenAI 기본 스킬 아님 | W/H: 화면 구성·타이포·시각적 일관성 | Codex에 SKILL.md로 설치 가능하나 실제 인식과 도구 호환은 확인 필요 |
| 2 | [playwright](https://github.com/openai/skills/tree/main/skills/.curated/playwright) — OpenAI | B 및 W/H: 실제 클릭·필터·스크린샷·레이아웃 검증 | Node/npm/npx, 브라우저 실행 환경 필요 |
| 조건부 | [figma-implement-design](https://github.com/openai/skills/tree/main/skills/.curated/figma-implement-design) — OpenAI | 제공된 Figma 디자인을 구현할 때 | Figma 원본과 연결된 MCP가 있을 때만 |
| 대안 | [playwright-interactive](https://github.com/openai/skills/tree/main/skills/.curated/playwright-interactive) — OpenAI | 반복 UI 검증 | js_repl과 관련 실행 환경이 이미 준비됐을 때. 일반 playwright와 둘 다 설치할 필요 없음 |

오늘 최소 구성은 frontend-design + playwright다. 유명한 스킬을 많이 설치하는 것보다 실제 한 화면을 만들고 검증하는 데 집중한다. 원본의 미적 제안보다 공식 요구·현재 디자인 시스템·현업 사용성과 마감이 우선이다. 스킬의 예시 문구/가상 콘텐츠를 제품 수치나 발표 성과로 복사하지 않는다.

## 역할별 요청

W: “frontend-design을 적용하되 FIELD_UX의 현업 판단 흐름을 우선해라. 조건 선택→분석 결과→근거 확인의 실제 사용성을 검증하고 가짜 결과를 넣지 마라.”

H: “frontend-design을 적용해 서비스와 시각 규칙을 맞추되 발표용 읽기 흐름을 설계해라. 검증된 구현·수치만 넣고 실제 제출 환경에서 열리는 HTML을 만들어라.”

B: “playwright가 실행 가능하면 실제 UI 조작과 HTML 렌더링을 검사해라. 설치 성공과 브라우저 검사 성공을 구분하고 실제 사용한 검사만 통과로 기록해라.”

## 설치와 인식

[DESIGN_SKILLS_START.txt](../DESIGN_SKILLS_START.txt)에 복붙 명령이 있다. 설치 후 다음 턴에서 스킬이 인식되는지 확인한다. 안 보이면 새 세션에서 확인한다. Worktree마다 재설치하지 않고 동일 사용자 스킬 경로를 사용하되 각 세션에서 인식을 확인한다.

설치 스크립트는 기존 폴더를 덮어쓰지 않는다. Python HTTPS 인증서 문제를 발견해 공식 설치 도구의 --method git 방식을 사용한다. TLS 검증을 끄지 않는다. 별도 Figma 연결이나 브라우저 다운로드가 필요한 경우 그것은 추가 작업이며 자동 완료로 간주하지 않는다.

Codex 스킬 안내: https://developers.openai.com/codex/skills/
