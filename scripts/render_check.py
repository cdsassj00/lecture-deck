# -*- coding: utf-8 -*-
"""강의안 HTML 자가검증: 각 .slide를 PNG로 캡처하고, 넘침(overflow)·박스 이탈을 보고한다.

사용법:
  python render_check.py <deck.html> [--out _shots] [--pdf]

필요: playwright (pip install playwright; playwright install chromium) 또는 시스템 Chrome.
출력: _shots/slide_NN.png, 콘솔에 ISSUES(넘침/이탈)·콘솔에러 목록.
ISSUES가 비어 있어야 통과. PNG는 사람이 육안으로 밀도·문체를 최종 확인한다.
"""
import sys, pathlib, argparse, json

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("html")
    ap.add_argument("--out", default="_shots")
    ap.add_argument("--pdf", action="store_true", help="PDF도 생성해 페이지 수·크기 확인")
    a = ap.parse_args()
    html = pathlib.Path(a.html).resolve()
    out = pathlib.Path(a.out); out.mkdir(exist_ok=True)
    from playwright.sync_api import sync_playwright
    errs = []
    with sync_playwright() as p:
        try: b = p.chromium.launch(channel="chrome")
        except Exception: b = p.chromium.launch()
        pg = b.new_page(viewport={"width":1280,"height":720}, device_scale_factor=2)
        pg.on("pageerror", lambda e: errs.append("JS:"+str(e)))
        pg.goto(html.as_uri(), wait_until="networkidle")
        pg.wait_for_timeout(2500)  # 폰트 로딩
        issues = pg.evaluate(r"""() => {
          const r=[];
          document.querySelectorAll('.slide').forEach((s,i)=>{
            ['.stage','.dwrap','.recap'].forEach(sel=>{const st=s.querySelector(sel);
              if(st && st.scrollHeight-st.clientHeight>2) r.push([i+1,'OVERFLOW',sel,st.scrollHeight+'>'+st.clientHeight]);});
            s.querySelectorAll('.note,.steps,.relay,.stack,.veri,.layer2,.loop,table,.concepts').forEach(e=>{
              const sr=s.getBoundingClientRect(), er=e.getBoundingClientRect();
              if(er.bottom>sr.bottom+1||er.right>sr.right+1) r.push([i+1,'ESCAPE',e.className.split(' ')[0]]);});
          });
          return r;
        }""")
        n = len(pg.query_selector_all(".slide"))
        for i, s in enumerate(pg.query_selector_all(".slide"), 1):
            s.scroll_into_view_if_needed(); pg.wait_for_timeout(40)
            s.screenshot(path=str(out / f"slide_{i:02d}.png"))
        if a.pdf:
            pg.emulate_media(media="print")
            pg.pdf(path=str(out/"deck.pdf"), prefer_css_page_size=True, print_background=True)
        b.close()
    print(f"slides: {n}  -> {out}/slide_*.png")
    print("ISSUES:", json.dumps(issues, ensure_ascii=False))
    print("JS ERRORS:", errs)
    print("PASS" if not issues and not errs else "CHECK ISSUES ABOVE")

if __name__ == "__main__":
    main()
