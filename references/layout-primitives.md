# 레이아웃 부품 가이드

`assets/deck-template.html`에 모든 부품이 예시 슬라이드로 들어 있다. 복제·편집해서 쓴다. CSS는 수정하지 않는다.

## 슬라이드 골격

```
<section class="slide">
  <div class="hdr"><div class="ht">강의제목<span>EN</span></div><div class="hr">1부 · 구분</div></div>
  <div class="stage">
    <div class="crumb">1부 · 구분</div>
    <h2 class="atitle"><span class="lbl">[구분]</span> 주제 <span class="sub">— 부제</span></h2>
    <div class="titlerule"></div>
    <div class="body ...">  ...본문...  </div>
  </div>
  <div class="pageno">03</div>
</section>
```

- 다크 표지/마무리: `<section class="slide dark">` + `.dwrap`(표지) 또는 `.recap`(요약).
- 본문 그리드: `.body.split-l`(좌 텍스트 넓게) / `.split-r`(우 도식 넓게) / `.split`(반반) / `.colflow`(단일 세로).

## 밀도 규칙 (휑함 방지 — 매우 중요)

- 빈 박스로 때우지 말 것. **실제 설명문 + 도식**으로 채운다.
- 개념 리스트는 `<div class="concepts fill">` 로 감싸면 칼럼 높이를 균등 분배해 채운다.
- **가로 스트립**(단계/계보)은 한 줄만 두면 위아래가 빈다 → 둘째 행(데이터 릴레이 `.relay`나 미리보기)을 추가하거나 카드 밴드로 감싼다.
- 좌측 텍스트 칼럼 중단이 비면 `.pull`(인용)로 채운다.
- 하단은 `.note`(정리/출처 바)로 마감해 바닥 여백을 없앤다.

## 부품 목록 (언제 쓰나)

| 부품 | 클래스 | 용도 |
|---|---|---|
| 번호 개념 정의 | `.concepts.fill > .concept`(.no/.cn/.en/p) | 핵심 개념 2~4개 설명 — **기본 부품** |
| 설명 문단 | `.lead` | 슬라이드 도입 2~3문장 |
| 정리/출처 바 | `.note`(.nl + p) / `.srcline` | 하단 결론·출처 |
| 표 | `table.grid`(.grp 그룹행, .pill 배지) / `.tight`(행 많을 때) | 비교·커리큘럼 |
| 가로 타임라인 | `.lineage > .ln`(.dot/.yr/.tm/p, .hot 강조) | 연혁·계보 |
| 2계층 대비 | `.layer2`(.lay.top/.bot, .conn) | 상/하위 대비 |
| 순서 흐름(반복) | `.loop > .lp`(.lpn/.lpt) + `.back` | 단계 + 되풀이 |
| 폭증가 스택 | `.stack`(.sb .s1~.s4) | 계층 구조 |
| 분기 흐름 | `.veri`(.vbox, .vbox.fail, .arr) | 판정/검증(PASS/FAIL) |
| 가로 단계 | `.steps > .st`(.sn/.sh/p) | 좌→우 절차 |
| 데이터 릴레이 | `.relay`(.rc .rk/.rv, .ra) | 단계 사이 산출물 전달 |
| 영역 카드 3열 | `.domain`(.dh + ul.dl) | 영역별 적용 |
| 수치 강조 | `.stats > .stat`(.sv/.sl) | 핵심 지표 |
| 인용 | `.pull`(+ span) | 핵심 문장/원칙(따옴표) |

## 도식 채움 주의

- `.figwrap`은 도식을 세로 중앙 정렬한다. 항목이 적은 흐름에 `.figwrap.flow`(space-between)를 쓰면 박스가 위아래로 벌어져 보이니, **항목 3개 이하 흐름엔 `.flow`를 빼고** 자연 중앙 정렬로 둔다.
- 가로 단계/릴레이는 `flex:1; flex-direction:column; justify-content:space-around` 래퍼에 넣어 세로로 분산하면 꽉 찬다(템플릿 본문 D 참고).

## 표준 구성 (3시간 강의 예시)

표지 → 커리큘럼 표 → [이론] 정의/계보 → [이론] 핵심 구분 → [이론] 구조 → [이론] 구성요소(표) → [이론] 부품(개념4) → [사례] (도식) → [관점] (2열) → [실습] 준비 → [실습 ①②③] (단계+릴레이) → [적용] (영역카드) → 강의 요약(다크).
