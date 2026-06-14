# lecture-deck

AI 에이전트용 **강의안·교안 생성 스킬**. 16:9 HTML 슬라이드를 보고서식 교안 스타일(크림 배경·다크 마스트헤드·러스트 액센트)로 만들고, **편집 · PDF 저장 · 전체화면 발표** 도구가 내장된 단일 HTML 파일을 출력한다.

- 서술형(비유·슬로건 금지) 합니다체 본문, 비개발자 눈높이 설명
- 슬라이드 1장 = PDF 1페이지(16:9), 배경색 포함 정확 출력
- 우상단 버튼: **편집**(브라우저에서 바로 수정 → HTML로 저장) · **PDF** · **발표**(←/→/Space, Esc)

## 설치

[vercel-labs `skills` CLI](https://github.com/vercel-labs/skills)로 설치한다(코덱스·제미나이·커서·클로드 등 여러 에이전트에 동기화):

```bash
npx skills add cdsassj00/lecture-deck
```

설치 후 동기화할 에이전트를 고르면 끝이다. 수동 설치도 가능하다:

```bash
git clone https://github.com/cdsassj00/lecture-deck.git ~/.agents/skills/lecture-deck
```

## 사용

에이전트에게 자연어로 요청한다.

```
"하네스 엔지니어링으로 임원 강의안 만들어줘 (비개발자 대상, 3시간)"
"데이터 리터러시 교안 16:9로 써줘"
```

생성된 HTML을 브라우저로 열어 **편집 → 저장(HTML)**, **PDF**, **발표** 버튼을 쓴다.

## 구성

| 파일 | 내용 |
|---|---|
| `SKILL.md` | 워크플로·규칙(에이전트가 읽음) |
| `assets/deck-template.html` | 전체 디자인 시스템 + 레이아웃 예시 + 편집/PDF/발표 도구 |
| `references/writing-style.md` | 문체·제목·비개발자 표현 규칙 |
| `references/layout-primitives.md` | 슬라이드 부품과 밀도 규칙 |
| `scripts/render_check.py` | 렌더·넘침 검사·PDF 확인(자가검증) |

## 자가검증(선택)

```bash
python scripts/render_check.py <결과.html> --pdf
```

`playwright`(또는 시스템 Chrome)가 있으면 각 슬라이드를 PNG로 캡처하고 넘침·박스 이탈을 점검한다.
