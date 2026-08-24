# -*- coding: utf-8 -*-
"""Design system em SVG para os prototipos do Portal da Escola do Legislativo.

Saida otimizada para importacao no Figma:
 - sem CSS interno (atributos inline) -> cores/fontes chegam intactas
 - sem filtros/sombras -> o Figma nao rasteriza nada
 - cada <text> e uma linha (sem tspan) -> camadas de texto editaveis
"""
import textwrap

# ---------------------------------------------------------------- paleta
NAVY = "#0E2C4B"
NAVY_2 = "#173F62"
NAVY_3 = "#1E4D75"
BLUE = "#1263A5"
BLUE_D = "#0D4E85"
BLUE_L = "#E8F1F9"
BLUE_L2 = "#D3E4F3"
GOLD = "#B8862B"
GOLD_L = "#FAF1DD"
GREEN = "#1B7A57"
GREEN_L = "#E3F3EC"
AMBER = "#B0700A"
AMBER_L = "#FCF0DA"
RED = "#A62B21"
RED_L = "#FAE8E6"
PURPLE = "#5A4A96"
PURPLE_L = "#EDEAF7"
BG = "#F3F6FA"
BG2 = "#E9EEF4"
WHITE = "#FFFFFF"
BORDER = "#DBE3EC"
BORDER2 = "#C2CEDA"
INK = "#122231"
TXT = "#2A3B4A"
MUTED = "#64778A"
FAINT = "#95A5B4"
FONT = "Arial, Helvetica, sans-serif"

W = 1440
M = 120
CW = W - 2 * M


# ---------------------------------------------------------------- base
# ---------------------------------------------------------------- areas clicaveis
HOTS = []


def hot(x, y, w, h, to, label=""):
    """Registra uma area clicavel da tela atual (usada pelo protótipo HTML)."""
    if to:
        HOTS.append((round(float(x), 1), round(float(y), 1), round(float(w), 1),
                     round(float(h), 1), str(to), label))


def hot_txt(x, y, label, size=14, bold=False, to=None, pad=8):
    """Area clicavel ao redor de um texto ja desenhado (x,y = inicio/baseline)."""
    if to:
        w = tw(label, size, bold)
        hot(x - pad, y - size - 2, w + pad * 2, size + 14, to, label)


def esc(s):
    return str(s).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def n(v):
    v = round(float(v), 2)
    return int(v) if v == int(v) else v


def rect(x, y, w, h, fill=WHITE, stroke=None, rx=0, sw=1, op=None):
    a = 'x="%s" y="%s" width="%s" height="%s"' % (n(x), n(y), n(w), n(h))
    if rx:
        a += ' rx="%s"' % n(rx)
    a += ' fill="%s"' % (fill or "none")
    if stroke:
        a += ' stroke="%s" stroke-width="%s"' % (stroke, n(sw))
    if op is not None:
        a += ' opacity="%s"' % op
    return "  <rect %s/>\n" % a


def txt(x, y, s, size=14, fill=TXT, bold=False, anchor="start", op=None, ls=None):
    a = 'x="%s" y="%s" font-family="%s" font-size="%s" fill="%s"' % (
        n(x), n(y), FONT, n(size), fill)
    if bold:
        a += ' font-weight="700"'
    if anchor != "start":
        a += ' text-anchor="%s"' % anchor
    if op is not None:
        a += ' opacity="%s"' % op
    if ls:
        a += ' letter-spacing="%s"' % ls
    return "  <text %s>%s</text>\n" % (a, esc(s))


def line(x1, y1, x2, y2, stroke=BORDER, sw=1, dash=None):
    a = 'x1="%s" y1="%s" x2="%s" y2="%s" stroke="%s" stroke-width="%s"' % (
        n(x1), n(y1), n(x2), n(y2), stroke, n(sw))
    if dash:
        a += ' stroke-dasharray="%s"' % dash
    return "  <line %s/>\n" % a


def circ(cx, cy, r, fill=WHITE, stroke=None, sw=1):
    a = 'cx="%s" cy="%s" r="%s" fill="%s"' % (n(cx), n(cy), n(r), fill or "none")
    if stroke:
        a += ' stroke="%s" stroke-width="%s"' % (stroke, n(sw))
    return "  <circle %s/>\n" % a


def path(d, fill="none", stroke=None, sw=2, cap="round"):
    a = 'd="%s" fill="%s"' % (d, fill or "none")
    if stroke:
        a += ' stroke="%s" stroke-width="%s" stroke-linecap="%s" stroke-linejoin="round"' % (
            stroke, n(sw), cap)
    return "  <path %s/>\n" % a


def poly(pts, fill="none", stroke=None, sw=2):
    a = 'points="%s" fill="%s"' % (pts, fill or "none")
    if stroke:
        a += ' stroke="%s" stroke-width="%s"' % (stroke, n(sw))
    return "  <polygon %s/>\n" % a


def grp(inner, gid=None, tr=None, op=None):
    a = ""
    if gid:
        a += ' id="%s"' % gid
    if tr:
        a += ' transform="%s"' % tr
    if op is not None:
        a += ' opacity="%s"' % op
    return "  <g%s>\n%s  </g>\n" % (a, inner)


def tw(s, size, bold=False):
    return len(str(s)) * size * (0.575 if bold else 0.525)


def wrap(s, width_px, size, bold=False):
    cw = size * (0.575 if bold else 0.525)
    mx = max(6, int(width_px / cw))
    return textwrap.wrap(s, mx) or [""]


def para(x, y, s, width_px, size=15, fill=MUTED, lh=None, bold=False, maxlines=None):
    lh = lh or size * 1.55
    out = ""
    ls = wrap(s, width_px, size, bold)
    if maxlines and len(ls) > maxlines:
        ls = ls[:maxlines]
        ls[-1] = ls[-1] + "..."
    for i, l in enumerate(ls):
        out += txt(x, y + i * lh, l, size, fill, bold)
    return out


def para_h(s, width_px, size=15, lh=None):
    lh = lh or size * 1.55
    return len(wrap(s, width_px, size)) * lh


def ctext(cx, cy, s, size=14, fill=TXT, bold=False):
    return txt(cx, cy + size * 0.35, s, size, fill, bold, anchor="middle")


# ---------------------------------------------------------------- icones (grade 24)
_IC = {
    "search": "M11 4a7 7 0 1 0 0 14 7 7 0 0 0 0-14M16.5 16.5 21 21",
    "calendar": "M4 6h16v15H4zM4 10h16M8 3v5M16 3v5",
    "clock": "M12 3a9 9 0 1 0 0 18 9 9 0 0 0 0-18M12 7v5l3.5 2",
    "pin": "M12 21s7-6.3 7-11a7 7 0 1 0-14 0c0 4.7 7 11 7 11ZM12 12a2.5 2.5 0 1 0 0-5 2.5 2.5 0 0 0 0 5",
    "user": "M12 12a4 4 0 1 0 0-8 4 4 0 0 0 0 8M4 21c1.2-4 4.2-6 8-6s6.8 2 8 6",
    "users": "M9 12a3.5 3.5 0 1 0 0-7 3.5 3.5 0 0 0 0 7M2 20c1-3.4 3.6-5 7-5s6 1.6 7 5M16.5 6.2a3.5 3.5 0 0 1 0 6.6M18 15.4c2 .8 3.3 2.3 4 4.6",
    "lock": "M6 11h12v9H6zM8.5 11V8a3.5 3.5 0 0 1 7 0v3",
    "mail": "M3 6h18v13H3zM3 7l9 6 9-6",
    "phone": "M6 3h4l1.6 4.2-2.2 1.6a12 12 0 0 0 5.8 5.8l1.6-2.2L21 14v4a2 2 0 0 1-2.2 2A17 17 0 0 1 4 5.2 2 2 0 0 1 6 3Z",
    "download": "M12 3v12M7.5 11l4.5 4.5L16.5 11M4 20h16",
    "upload": "M12 16V4M7.5 8.5 12 4l4.5 4.5M4 20h16",
    "check": "M4 12.5 9.5 18 20 6",
    "close": "M6 6 18 18M18 6 6 18",
    "chev-d": "M6 9.5 12 15.5 18 9.5",
    "chev-r": "M9.5 5 16 12l-6.5 7",
    "chev-l": "M14.5 5 8 12l6.5 7",
    "arrow-l": "M20 12H4M10 6 4 12l6 6",
    "arrow-r": "M4 12h16M14 6l6 6-6 6",
    "file": "M6 3h8l4 4v14H6zM14 3v4h4",
    "book": "M4 4h7a3 3 0 0 1 3 3v13a3 3 0 0 0-3-3H4zM20 4h-6M20 4v13h-3",
    "bell": "M12 3a6 6 0 0 0-6 6c0 5-2 6-2 6h16s-2-1-2-6a6 6 0 0 0-6-6M10 21h4",
    "edit": "M4 20h4L20 8l-4-4L4 16zM15 5l4 4",
    "trash": "M4 7h16M9 7V4h6v3M6 7l1 14h10l1-14M10 11v6M14 11v6",
    "plus": "M12 5v14M5 12h14",
    "filter": "M3 5h18l-7 8v6l-4 2v-8z",
    "star": "M12 3.5 14.7 9l6.3.9-4.5 4.4 1 6.2-5.5-2.9L6.5 20.5l1-6.2L3 9.9 9.3 9z",
    "shield": "M12 3 20 6v6c0 5-4 8-8 9-4-1-8-4-8-9V6zM8.5 12l2.5 2.5L16 9.5",
    "qr": "M4 4h6v6H4zM14 4h6v6h-6zM4 14h6v6H4zM14 14h2v2h-2zM18 14h2v2h-2zM14 18h2v2h-2zM18 18h2v2h-2z",
    "image": "M3 5h18v14H3zM3 16l5-5 4 4 3-3 6 6",
    "play": "M12 3a9 9 0 1 0 0 18 9 9 0 0 0 0-18M10 8.5l6 3.5-6 3.5z",
    "chart": "M4 20V10M10 20V4M16 20v-7M22 20H2",
    "grid": "M4 4h7v7H4zM13 4h7v7h-7zM4 13h7v7H4zM13 13h7v7h-7z",
    "list": "M4 6h16M4 12h16M4 18h16",
    "eye": "M2 12s3.8-6.5 10-6.5S22 12 22 12s-3.8 6.5-10 6.5S2 12 2 12M12 15a3 3 0 1 0 0-6 3 3 0 0 0 0 6",
    "key": "M15 3a6 6 0 1 0-4.2 10.2L4 20v3h4v-3h3v-3h3l1-1v-3A6 6 0 0 0 15 3",
    "cert": "M5 3h14v13H5zM8 7h8M8 10h5M12 16v5l2.5-1.6L17 21v-5",
    "info": "M12 3a9 9 0 1 0 0 18 9 9 0 0 0 0-18M12 11v6M12 7.5h.01",
    "alert": "M12 3 22 20H2zM12 9v5M12 17h.01",
    "gear": "M12 15.5a3.5 3.5 0 1 0 0-7 3.5 3.5 0 0 0 0 7M12 2l1.4 2.6 2.9-.5.5 2.9 2.6 1.4L18 11l1.4 2.6-2.6 1.4-.5 2.9-2.9-.5L12 20l-1.4-2.6-2.9.5-.5-2.9L4.6 13.6 6 11 4.6 8.4l2.6-1.4.5-2.9 2.9.5z",
    "logout": "M14 4H6a2 2 0 0 0-2 2v12a2 2 0 0 0 2 2h8M18 8l4 4-4 4M22 12H10",
    "folder": "M3 6h6l2 3h10v11H3zM3 6v14",
    "link": "M10 14a4 4 0 0 0 6 .5l3-3a4 4 0 0 0-5.7-5.7L11.6 7.5M14 10a4 4 0 0 0-6-.5l-3 3a4 4 0 0 0 5.7 5.7L12.4 16.5",
    "print": "M7 9V3h10v6M7 18H4V9h16v9h-3M7 14h10v7H7z",
    "cam": "M4 8h4l2-3h4l2 3h4v12H4zM12 17a3.5 3.5 0 1 0 0-7 3.5 3.5 0 0 0 0 7",
    "flag": "M6 21V4M6 4h12l-2.5 4L18 12H6",
    "clip": "M20 11.5 12 19.5a5 5 0 0 1-7-7l8.5-8.5a3.5 3.5 0 0 1 5 5L10 17a2 2 0 0 1-3-3l7.5-7.5",
    "home": "M4 11 12 4l8 7v9h-5v-6H9v6H4z",
    "board": "M3 4h18v13H3zM12 17v4M8 21h8M7 13V9M12 13V7M17 13v-2",
}


def icon(name, x, y, size=20, color=MUTED, sw=1.7, fill="none"):
    d = _IC.get(name)
    if not d:
        return ""
    s = size / 24.0
    inner = path(d, fill=fill, stroke=color, sw=sw / s)
    return '  <g transform="translate(%s,%s) scale(%s)">\n%s  </g>\n' % (n(x), n(y), n(s), inner)


def icon_c(name, cx, cy, size=20, color=MUTED, sw=1.7):
    return icon(name, cx - size / 2.0, cy - size / 2.0, size, color, sw)
