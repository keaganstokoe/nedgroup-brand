"""Fill the Nedgroup Investments PPTX template with a six-part commentary.

Usage:
  python3 fill_template.py template.pptx content.json out.pptx

content.json (all strings; omit any key to leave that placeholder empty):
{
  "cover": {"eyebrow": "QUARTERLY COMMENTARY · Q2 2026", "title": "Flexible Income Fund",
            "subtitle": "Nedgroup Investments · Managed by Abax Investments since 2012",
            "stats": [["3.0%", "Q2 RETURN", "Benchmark 1.8%"], ["9.8%", "12 MONTHS", "Benchmark 7.0%"],
                      ["R17.0bn", "FUND SIZE", "31 August 2026"], ["", "", ""]],
            "category": "SOUTH AFRICAN MULTI ASSET · INCOME"},
  "fund": {"section": "FUND AND MANAGER", "period": "Q2 2026", "headline": "...",
           "approach": ["INVESTMENT APPROACH", "bullet", "bullet", "", "PORTFOLIO MANAGERS", "names"],
           "context": "market context paragraph"},
  "performance": {"strip": [["PERFORMANCE TO 30 JUNE 2026", "A1 class, net of fees, versus 110% STeFI Call Deposit"],
                            ["3 months · Fund   3.0%", "3 months · Benchmark   1.8%"],
                            ["12 months · Fund   9.8%", "12 months · Benchmark   7.0%"]],
                  "text": "..."},
  "attribution": {"text": "..."},
  "positioning": {"text": "..."},
  "contact": {"details": ["www.nedgroupinvestments.com", "0800 123 263 (RSA only) · +27 21 412 2003", "clientservices@nedgroupinvestments.co.za"],
              "disclaimer": "verbatim disclaimer"},
  "footer_left": "NEDGROUP INVESTMENTS FLEXIBLE INCOME FUND",
  "footer_right": "Source: Nedgroup Investments, 30 June 2026"
}
Text is placed verbatim; the template's layout formatting (fonts, sizes, colours) is inherited.
"""
import json, sys, copy
from pptx import Presentation
from pptx.oxml.ns import qn


def set_lines(ph, lines, lph=None):
    """Fill a placeholder with one paragraph per line, keeping each layout paragraph's formatting."""
    tf = ph.text_frame
    src_paras = list(lph.text_frame.paragraphs) if lph is not None and lph.has_text_frame else []
    # clear existing paragraphs
    for p in list(tf.paragraphs)[1:]:
        p._p.getparent().remove(p._p)
    tf.paragraphs[0].text = ''
    for k, line in enumerate(lines):
        p = tf.paragraphs[0] if k == 0 else tf.add_paragraph()
        p.text = line
        src = src_paras[min(k, len(src_paras) - 1)] if src_paras else None
        if src is not None and src._p.pPr is not None:
            # copy paragraph properties (defRPr carries the size/font/colour) from the layout paragraph
            new_pPr = copy.deepcopy(src._p.pPr)
            old = p._p.pPr
            if old is not None:
                p._p.remove(old)
            p._p.insert(0, new_pPr)
            # also apply to the run so PowerPoint and LibreOffice agree
            dr = new_pPr.find(qn('a:defRPr'))
            if dr is not None:
                for r in p.runs:
                    rPr = r._r.get_or_add_rPr()
                    for a in ('sz', 'b', 'i', 'spc'):
                        if dr.get(a): rPr.set(a, dr.get(a))
                    for child in list(rPr): rPr.remove(child)
                    for child in dr: rPr.append(copy.deepcopy(child))


class PH(dict):
    """idx -> slide placeholder, with set() that carries the matching layout placeholder's formatting."""
    def __init__(self, slide):
        super().__init__({ph.placeholder_format.idx: ph for ph in slide.placeholders})
        self.lmap = {ph.placeholder_format.idx: ph for ph in slide.slide_layout.placeholders}
    def set(self, idx, lines):
        if idx in self:
            set_lines(self[idx], lines, self.lmap.get(idx))


def by_idx(slide):
    return PH(slide)


def attach_layout_refs(slide):
    pass


def main(template, content_path, out):
    c = json.load(open(content_path, encoding='utf-8'))
    prs = Presentation(template)
    # remove any example slides shipped with the template
    for sid in list(prs.slides._sldIdLst):
        prs.part.drop_rel(sid.rId); prs.slides._sldIdLst.remove(sid)
    L = {lo.name: lo for lo in prs.slide_masters[0].slide_layouts}
    fl, fr = c.get('footer_left', ''), c.get('footer_right', '')

    def chrome(s, section, period):
        p = by_idx(s)
        if 10 in p: p.set(10, [section])
        if 11 in p: p.set(11, [period])
        if 40 in p: p.set(40, [fl])
        if 41 in p: p.set(41, [fr])

    cv = c.get('cover', {})
    s = prs.slides.add_slide(L['Cover']); attach_layout_refs(s); p = by_idx(s)
    p.set(10, [cv.get('eyebrow', '')]); p.set(0, [cv.get('title', '')]); p.set(1, [cv.get('subtitle', '')])
    for i, st in enumerate(cv.get('stats', [])[:4]):
        p.set(20 + i, list(st) + [''] * (3 - len(st)))
    p.set(30, [cv.get('category', '')])

    f = c.get('fund', {})
    s = prs.slides.add_slide(L['Fund and manager']); attach_layout_refs(s); p = by_idx(s)
    chrome(s, f.get('section', 'FUND AND MANAGER'), f.get('period', ''))
    p.set(0, [f.get('headline', '')]); p.set(1, f.get('approach', [])); p.set(2, [f.get('context', '')])

    for key, lname in (('performance', 'Update · Performance Commentary'), ('attribution', 'Update · Attribution Commentary'), ('positioning', 'Update · Fund Positioning')):
        blk = c.get(key, {})
        s = prs.slides.add_slide(L[lname]); attach_layout_refs(s); p = by_idx(s)
        chrome(s, blk.get('section', 'QUARTERLY PORTFOLIO UPDATE'), blk.get('period', f.get('period', '')))
        strip = blk.get('strip') or c.get('performance', {}).get('strip') or []
        for k, cell in enumerate(strip[:3]):
            p.set(20 + k, list(cell))
        p.set(0, [blk.get('heading', lname.split('· ')[1])]); p.set(1, [blk.get('text', '')])

    ct = c.get('contact', {})
    s = prs.slides.add_slide(L['Contact and disclaimer']); attach_layout_refs(s); p = by_idx(s)
    chrome(s, 'CONTACT', f.get('period', ''))
    p.set(0, [ct.get('heading', 'For more information')]); p.set(1, ct.get('details', [])); p.set(2, [ct.get('disclaimer', '')])
    prs.save(out)
    print('saved', out, 'slides', len(prs.slides))


if __name__ == '__main__':
    main(*sys.argv[1:4])
