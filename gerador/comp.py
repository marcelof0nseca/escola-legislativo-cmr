# -*- coding: utf-8 -*-
"""Componentes reutilizaveis do prototipo."""
from ds import *
from ds import hot as ds_hot


# ---------------------------------------------------------------- botoes
_BTN = {
    "primary": (BLUE, BLUE_D, WHITE),
    "dark": (NAVY, NAVY, WHITE),
    "gold": (GOLD, "#966D20", WHITE),
    "success": (GREEN, "#146245", WHITE),
    "danger": (RED, "#83201A", WHITE),
    "secondary": (WHITE, BLUE, BLUE),
    "ghost": (WHITE, BORDER2, TXT),
    "soft": (BLUE_L, BLUE_L, BLUE_D),
    "disabled": ("#EDF1F5", BORDER, FAINT),
}


def btn(x, y, w, h, label, kind="primary", size=14, ic=None, rx=6, hot=False, to=None):
    ds_hot(x, y, w, h, to, label)
    fill, stroke, fg = _BTN.get(kind, _BTN["primary"])
    out = rect(x, y, w, h, fill, stroke, rx, 1.5)
    if ic:
        iw = 18
        total = tw(label, size, True) + iw + 8
        ix = x + (w - total) / 2.0
        out += icon(ic, ix, y + (h - iw) / 2.0, iw, fg, 1.8)
        out += txt(ix + iw + 8, y + h / 2.0 + size * 0.35, label, size, fg, True)
    else:
        out += ctext(x + w / 2.0, y + h / 2.0, label, size, fg, True)
    if hot:
        out += rect(x - 3, y - 3, w + 6, h + 6, None, GOLD, rx + 3, 1.5)
    return out


def link(x, y, label, size=14, color=BLUE_D, ul=True, bold=False, to=None):
    hot_txt(x, y, label, size, bold, to)
    out = txt(x, y, label, size, color, bold)
    if ul:
        out += line(x, y + 4, x + tw(label, size, bold), y + 4, color, 1)
    return out


# ---------------------------------------------------------------- campos
def field(x, y, w, label, value="", h=46, req=False, kind="text", helper=None,
          placeholder=True, ic=None, err=None):
    out = ""
    ly = y
    if label:
        out += txt(x, ly, label, 13, TXT, True)
        if req:
            out += txt(x + tw(label, 13, True) + 5, ly, "*", 13, RED, True)
        ly += 12
    bx = ly + 6
    bs = RED if err else BORDER2
    out += rect(x, bx, w, h, WHITE, bs, 6, 1.4)
    tx0 = x + 14
    if ic:
        out += icon(ic, x + 13, bx + (h - 18) / 2.0, 18, FAINT, 1.7)
        tx0 = x + 40
    if kind == "password":
        dots = value or ""
        cx0 = tx0 + 4
        for i in range(len(dots)):
            out += circ(cx0 + i * 11, bx + h / 2.0, 3.6, TXT)
    else:
        col = TXT if (value and not placeholder) else (TXT if value else FAINT)
        shown = value if value else "Digite aqui"
        out += txt(tx0, bx + h / 2.0 + 5, shown, 15, col if value else FAINT)
    if kind == "select":
        out += icon("chev-d", x + w - 32, bx + (h - 18) / 2.0, 18, MUTED, 1.8)
    if kind == "date":
        out += icon("calendar", x + w - 34, bx + (h - 18) / 2.0, 18, MUTED, 1.6)
    bot = bx + h
    if err:
        out += icon("alert", x, bot + 6, 14, RED, 1.6)
        out += txt(x + 20, bot + 17, err, 12.5, RED)
        bot += 24
    elif helper:
        out += txt(x, bot + 17, helper, 12.5, MUTED)
        bot += 24
    return out, bot


def field_h(label=True, helper=False, h=46):
    return (18 if label else 0) + 6 + h + (24 if helper else 0)


def textarea(x, y, w, label, value="", h=110, req=False):
    out = txt(x, y, label, 13, TXT, True)
    if req:
        out += txt(x + tw(label, 13, True) + 5, y, "*", 13, RED, True)
    out += rect(x, y + 6, w, h, WHITE, BORDER2, 6, 1.4)
    if value:
        out += para(x + 14, y + 30, value, w - 28, 14, TXT)
    else:
        out += txt(x + 14, y + 30, "Digite aqui", 14, FAINT)
    return out, y + 6 + h


def checkbox(x, y, label, checked=False, size=18, sub=None, color=TXT):
    out = rect(x, y, size, size, BLUE if checked else WHITE,
               BLUE if checked else BORDER2, 4, 1.5)
    if checked:
        out += path("M%s %s l%s %s l%s %s" % (n(x + 4), n(y + size * 0.52), n(size * 0.2),
                                              n(size * 0.24), n(size * 0.38), n(-size * 0.42)),
                    None, WHITE, 2.2)
    out += txt(x + size + 10, y + size * 0.72, label, 14, color)
    if sub:
        out += txt(x + size + 10, y + size * 0.72 + 18, sub, 12.5, MUTED)
    return out


def radio(x, y, label, checked=False, size=18, sub=None, w=None):
    out = circ(x + size / 2.0, y + size / 2.0, size / 2.0, WHITE,
               BLUE if checked else BORDER2, 1.6)
    if checked:
        out += circ(x + size / 2.0, y + size / 2.0, size / 2.0 - 4.5, BLUE)
    out += txt(x + size + 10, y + size * 0.72, label, 14, TXT)
    if sub:
        out += para(x + size + 10, y + size * 0.72 + 18, sub, w or 320, 12.5, MUTED)
    return out


def toggle(x, y, on=True, label=None):
    out = rect(x, y, 44, 24, GREEN if on else "#C6D0DA", None, 12)
    out += circ(x + (32 if on else 12), y + 12, 9, WHITE)
    if label:
        out += txt(x + 54, y + 17, label, 14, TXT)
    return out


# ---------------------------------------------------------------- badges
_BADGE = {
    "abertas": (GREEN_L, GREEN, GREEN),
    "breve": (AMBER_L, AMBER, AMBER),
    "esgotado": (RED_L, RED, RED),
    "encerradas": ("#EDF1F5", BORDER2, MUTED),
    "info": (BLUE_L, "#A9CBE8", BLUE_D),
    "gold": (GOLD_L, "#E7D2A4", "#8A6414"),
    "roxo": (PURPLE_L, "#C7BEE8", PURPLE),
    "neutro": ("#EDF1F5", BORDER2, TXT),
    "solid-green": (GREEN, GREEN, WHITE),
    "solid-red": (RED, RED, WHITE),
    "solid-amber": (AMBER, AMBER, WHITE),
    "solid-blue": (BLUE, BLUE, WHITE),
    "solid-navy": (NAVY, NAVY, WHITE),
}


def badge(x, y, label, kind="info", size=12, h=24, pad=12, dot=False, rx=None):
    bgc, stc, fg = _BADGE.get(kind, _BADGE["info"])
    w = tw(label, size, True) + pad * 2 + (14 if dot else 0)
    out = rect(x, y, w, h, bgc, stc, rx if rx is not None else h / 2.0, 1)
    tx0 = x + pad
    if dot:
        out += circ(x + pad + 4, y + h / 2.0, 3.5, fg)
        tx0 += 14
    out += txt(tx0, y + h / 2.0 + size * 0.36, label, size, fg, True)
    return out, w


def badge_w(label, size=12, pad=12, dot=False):
    return tw(label, size, True) + pad * 2 + (14 if dot else 0)


def badges_row(x, y, items, size=12, h=24, gap=8, dot=False):
    out = ""
    cx = x
    for lbl, kind in items:
        s, w = badge(cx, y, lbl, kind, size, h, dot=dot)
        out += s
        cx += w + gap
    return out, cx


# ---------------------------------------------------------------- avisos
_ALERT = {
    "info": (BLUE_L, "#A9CBE8", BLUE_D, "info"),
    "ok": (GREEN_L, "#A9DCC6", GREEN, "check"),
    "warn": (AMBER_L, "#EBCE95", AMBER, "alert"),
    "erro": (RED_L, "#EBB7B1", RED, "alert"),
    "lgpd": (PURPLE_L, "#C7BEE8", PURPLE, "shield"),
}


def alert(x, y, w, title, body=None, kind="info", h=None):
    bgc, stc, fg, ic = _ALERT.get(kind, _ALERT["info"])
    lines = wrap(body, w - 90, 13.5) if body else []
    hh = h or (26 + (len(lines) * 20 if lines else 0) + 22)
    out = rect(x, y, w, hh, bgc, stc, 8, 1.2)
    out += rect(x, y, 4, hh, fg, None, 2)
    out += icon(ic, x + 18, y + 17, 20, fg, 1.8)
    out += txt(x + 50, y + 31, title, 14, fg, True)
    for i, l in enumerate(lines):
        out += txt(x + 50, y + 53 + i * 20, l, 13.5, TXT)
    return out, y + hh


def alert_h(w, body=None):
    lines = wrap(body, w - 90, 13.5) if body else []
    return 26 + (len(lines) * 20 if lines else 0) + 22


# ---------------------------------------------------------------- cartoes
def card(x, y, w, h, title=None, rx=10, fill=WHITE, stroke=BORDER, pad=24, sub=None):
    out = rect(x, y, w, h, fill, stroke, rx, 1.2)
    ny = y + pad
    if title:
        out += txt(x + pad, ny + 16, title, 17, INK, True)
        ny += 26
        if sub:
            out += txt(x + pad, ny + 12, sub, 13, MUTED)
            ny += 22
        ny += 8
    return out, ny


def sec_title(x, y, title, sub=None, action=None, w=CW):
    out = txt(x, y, title, 26, INK, True)
    out += rect(x, y + 12, 46, 4, GOLD, None, 2)
    ny = y + 30
    if sub:
        out += txt(x, y + 30, sub, 15, MUTED)
        ny = y + 46
    if action:
        out += txt(x + w, y - 2, action, 14, BLUE_D, True, anchor="end")
        out += icon("arrow-r", x + w + 6, y - 16, 16, BLUE_D, 1.8)
    return out, ny


def img_ph(x, y, w, h, rx=8, tone=BLUE_L2, label=None, ic="image"):
    out = rect(x, y, w, h, tone, None, rx)
    out += icon_c(ic, x + w / 2.0, y + h / 2.0 - (8 if label else 0), 34, "#FFFFFF", 2)
    if label:
        out += ctext(x + w / 2.0, y + h / 2.0 + 24, label, 12, "#FFFFFF", True)
    return out


def avatar(x, y, d, initials="RB", tone=NAVY_3):
    out = circ(x + d / 2.0, y + d / 2.0, d / 2.0, tone)
    out += ctext(x + d / 2.0, y + d / 2.0, initials, d * 0.36, WHITE, True)
    return out


# ---------------------------------------------------------------- tabelas
def table(x, y, w, cols, rows, row_h=54, head_h=46, zebra=True, rx=10):
    """cols: [(label, largura, align)] ; celula: str | ("badge",label,kind) |
    ("btns",[(label,kind)]) | ("two",linha1,linha2) | ("check",bool) | ("prog", pct, texto)"""
    tot = float(sum(c[1] for c in cols))
    avail = w - 40.0
    if tot and abs(tot - avail) > 0.5:
        k = avail / tot
        cols = [(c[0], c[1] * k, c[2]) for c in cols]
    h = head_h + len(rows) * row_h
    out = rect(x, y, w, h, WHITE, BORDER, rx, 1.2)
    out += rect(x, y, w, head_h, "#F5F8FB", None, rx)
    out += rect(x, y + head_h - 12, w, 12, "#F5F8FB")
    out += line(x, y + head_h, x + w, y + head_h, BORDER, 1.2)
    cx = x + 20
    for lbl, cwid, al in cols:
        ax = cx if al == "start" else (cx + cwid if al == "end" else cx + cwid / 2.0)
        out += txt(ax, y + head_h / 2.0 + 4, lbl.upper(), 11.5, MUTED, True,
                   anchor=al if al != "start" else "start", ls="0.6")
        cx += cwid
    for ri, r in enumerate(rows):
        ry = y + head_h + ri * row_h
        if zebra and ri % 2 == 1:
            out += rect(x + 1, ry, w - 2, row_h, "#FAFCFE")
        if ri:
            out += line(x + 20, ry, x + w - 20, ry, "#EDF1F6", 1)
        cx = x + 20
        for ci, (lbl, cwid, al) in enumerate(cols):
            cell = r[ci] if ci < len(r) else ""
            ax = cx if al == "start" else (cx + cwid if al == "end" else cx + cwid / 2.0)
            anc = "start" if al == "start" else ("end" if al == "end" else "middle")
            if isinstance(cell, tuple):
                t = cell[0]
                if t == "badge":
                    bw = badge_w(cell[1])
                    bx = cx if al == "start" else (cx + cwid - bw if al == "end" else cx + (cwid - bw) / 2.0)
                    out += badge(bx, ry + (row_h - 24) / 2.0, cell[1], cell[2])[0]
                elif t == "btns":
                    total = sum(tw(it[0], 12.5, True) + 26 for it in cell[1]) + 8 * (len(cell[1]) - 1)
                    bx = cx if al == "start" else (cx + cwid - total if al == "end" else cx + (cwid - total) / 2.0)
                    for it in cell[1]:
                        l, k = it[0], it[1]
                        dst = it[2] if len(it) > 2 else None
                        bw = tw(l, 12.5, True) + 26
                        out += btn(bx, ry + (row_h - 30) / 2.0, bw, 30, l, k, 12.5, rx=5, to=dst)
                        bx += bw + 8
                elif t == "two":
                    if anc == "start":
                        out += para(ax, ry + row_h / 2.0 - 3, cell[1], cwid - 16, 14, INK, 18,
                                    True, maxlines=1)
                        out += para(ax, ry + row_h / 2.0 + 15, cell[2], cwid - 16, 12.5, MUTED, 16,
                                    maxlines=1)
                    else:
                        out += txt(ax, ry + row_h / 2.0 - 3, cell[1], 14, INK, True, anchor=anc)
                        out += txt(ax, ry + row_h / 2.0 + 15, cell[2], 12.5, MUTED, anchor=anc)
                elif t == "check":
                    out += checkbox(cx, ry + (row_h - 18) / 2.0, "", cell[1])
                elif t == "avatar":
                    out += avatar(cx, ry + (row_h - 34) / 2.0, 34, cell[2])
                    out += txt(cx + 44, ry + row_h / 2.0 - 3, cell[1], 14, INK, True)
                    out += txt(cx + 44, ry + row_h / 2.0 + 15, cell[3], 12.5, MUTED)
                elif t == "prog":
                    bwid = cwid - 60
                    out += rect(cx, ry + row_h / 2.0 - 4, bwid, 8, "#E6ECF2", None, 4)
                    out += rect(cx, ry + row_h / 2.0 - 4, bwid * cell[1] / 100.0, 8,
                                GREEN if cell[1] >= 75 else AMBER, None, 4)
                    out += txt(cx + bwid + 10, ry + row_h / 2.0 + 4, cell[2], 12.5, MUTED)
                elif t == "bold":
                    out += txt(ax, ry + row_h / 2.0 + 5, cell[1], 14, INK, True, anchor=anc)
                elif t == "mono":
                    out += txt(ax, ry + row_h / 2.0 + 5, cell[1], 13.5, BLUE_D, True, anchor=anc)
                elif t == "icons":
                    total = len(cell[1]) * 34 - 8
                    bx = cx if al == "start" else (cx + cwid - total if al == "end" else cx + (cwid - total) / 2.0)
                    for it in cell[1]:
                        nm, cl = it[0], it[1]
                        dst = it[2] if len(it) > 2 else None
                        ds_hot(bx, ry + (row_h - 30) / 2.0, 30, 30, dst, nm)
                        out += rect(bx, ry + (row_h - 30) / 2.0, 30, 30, WHITE, BORDER2, 5, 1.2)
                        out += icon_c(nm, bx + 15, ry + row_h / 2.0, 16, cl, 1.7)
                        bx += 34
            elif anc == "start":
                out += para(ax, ry + row_h / 2.0 + 5, cell, cwid - 16, 14, TXT, 18, maxlines=1)
            else:
                out += txt(ax, ry + row_h / 2.0 + 5, cell, 14, TXT, anchor=anc)
            cx += cwid
    return out, y + h


def table_h(rows, row_h=54, head_h=46):
    return head_h + rows * row_h


# ---------------------------------------------------------------- abas
def tabs(x, y, items, active=0, size=15, gap=34, underline_w=None, to=None):
    out = ""
    cx = x
    for i, it in enumerate(items):
        wdt = tw(it, size, i == active)
        if to and i < len(to) and i != active:
            ds_hot(cx - 10, y - size - 4, wdt + 20, size + 26, to[i], it)
        col = INK if i == active else MUTED
        out += txt(cx, y, it, size, col, i == active)
        if i == active:
            out += rect(cx, y + 12, wdt, 3.5, GOLD, None, 2)
        cx += wdt + gap
    out += line(x, y + 14, x + (underline_w or CW), y + 14, BORDER, 1.5)
    return out, y + 14


def pills(x, y, items, active=0, h=38, gap=10, to=None):
    out = ""
    cx = x
    for i, it in enumerate(items):
        wdt = tw(it, 14, i == active) + 34
        on = i == active
        if to and i < len(to) and not on:
            ds_hot(cx, y, wdt, h, to[i], it)
        out += rect(cx, y, wdt, h, NAVY if on else WHITE, NAVY if on else BORDER2, h / 2.0, 1.3)
        out += ctext(cx + wdt / 2.0, y + h / 2.0, it, 14, WHITE if on else TXT, on)
        cx += wdt + gap
    return out, cx


def breadcrumb(x, y, items):
    out = ""
    cx = x
    for i, it in enumerate(items):
        last = i == len(items) - 1
        out += txt(cx, y, it, 13, INK if last else MUTED, last)
        cx += tw(it, 13, last)
        if not last:
            out += icon("chev-r", cx + 5, y - 11, 13, FAINT, 1.8)
            cx += 23
    return out


def pagination(x, y, w, total="128", pages=(1, 2, 3, 4)):
    out = txt(x, y + 20, "Exibindo 1-10 de %s registros" % total, 13, MUTED)
    cx = x + w - (len(pages) + 2) * 40
    out += rect(cx, y, 34, 34, WHITE, BORDER2, 6, 1.2)
    out += icon_c("chev-l", cx + 17, y + 17, 15, MUTED, 1.8)
    cx += 40
    for p in pages:
        on = p == 1
        out += rect(cx, y, 34, 34, BLUE if on else WHITE, BLUE if on else BORDER2, 6, 1.2)
        out += ctext(cx + 17, y + 17, str(p), 13.5, WHITE if on else TXT, on)
        cx += 40
    out += rect(cx, y, 34, 34, WHITE, BORDER2, 6, 1.2)
    out += icon_c("chev-r", cx + 17, y + 17, 15, MUTED, 1.8)
    return out, y + 34


def stat(x, y, w, h, label, value, sub=None, ic="chart", tone=BLUE, tone_l=BLUE_L):
    out = rect(x, y, w, h, WHITE, BORDER, 10, 1.2)
    out += rect(x + 20, y + 20, 42, 42, tone_l, None, 9)
    out += icon_c(ic, x + 41, y + 41, 21, tone, 1.8)
    out += txt(x + 20, y + 90, str(value), 30, INK, True)
    out += txt(x + 20, y + 114, label, 13, MUTED)
    if sub:
        out += txt(x + 20, y + 134, sub, 12, GREEN, True)
    return out


# ---------------------------------------------------------------- modais
def modal(x, y, w, h, title, rx=12, close=True, sub=None):
    out = rect(x, y, w, h, WHITE, BORDER2, rx, 1.4)
    out += rect(x, y, w, 6, NAVY, None, rx)
    out += rect(x, y + 4, w, 4, NAVY)
    out += txt(x + 32, y + 52, title, 21, INK, True)
    ny = y + 66
    if sub:
        out += txt(x + 32, y + 78, sub, 13.5, MUTED)
        ny = y + 92
    if close:
        out += icon_c("close", x + w - 34, y + 46, 18, MUTED, 1.9)
    out += line(x, ny + 12, x + w, ny + 12, BORDER, 1.2)
    return out, ny + 34


def overlay(w, h, op=0.55):
    return rect(0, 0, w, h, "#0A1826", None, 0, op=op)


# ---------------------------------------------------------------- header publico
NAV = ["Home", "Cursos e Eventos", "A Escola", "Acervo", "Noticias", "Contato"]
NAV_ACENTO = {"Noticias": "Notícias"}
HEAD_H = 128


def header_pub(active=None, logged=None, w=W):
    """logged=None (deslogado) ou dict(nome=..., iniciais=...)"""
    dest = {"Home": "01", "Cursos e Eventos": "02", "A Escola": "10",
            "Acervo": "14", "Noticias": "08", "Contato": "15"}
    out = rect(0, 0, w, 40, NAVY)
    out += txt(M, 25, "CÂMARA MUNICIPAL DO RECIFE", 12, "#9FB6CB", True, ls="1.2")
    rx0 = w - M
    for lbl in ["Mapa do site", "Alto contraste", "Acessibilidade"][::1]:
        wd = tw(lbl, 12)
        out += txt(rx0, 25, lbl, 12, "#9FB6CB", anchor="end")
        rx0 -= wd + 26
    out += rect(0, 40, w, HEAD_H - 40, WHITE)
    out += line(0, HEAD_H, w, HEAD_H, BORDER, 1.5)
    # brasao + wordmark
    ds_hot(M, 58, 280, 54, "01", "logo")
    out += rect(M, 62, 46, 46, NAVY, None, 8)
    out += icon_c("board", M + 23, 85, 24, GOLD, 1.9)
    out += txt(M + 60, 80, "Escola do Legislativo", 20, INK, True)
    out += txt(M + 60, 99, "Câmara Municipal do Recife", 12.5, MUTED)
    # nav
    cx = 430
    for item in NAV:
        lbl = NAV_ACENTO.get(item, item)
        on = (item == active)
        wd = tw(lbl, 14, on)
        ds_hot(cx - 10, 70, wd + 20, 38, dest.get(item), lbl)
        out += txt(cx, 90, lbl, 14, INK if on else TXT, on)
        if on:
            out += rect(cx, 100, wd, 3, GOLD, None, 2)
        cx += wd + 28
    # acoes
    ds_hot(w - M - 40, 68, 40, 40, "16", "busca")
    out += rect(w - M - 40, 68, 40, 40, WHITE, BORDER2, 8, 1.3)
    out += icon_c("search", w - M - 20, 88, 18, TXT, 1.8)
    if logged:
        ds_hot(w - M - 246, 68, 196, 40, "29", "conta")
        out += rect(w - M - 246, 68, 196, 40, "#F5F8FB", BORDER2, 8, 1.3)
        out += avatar(w - M - 238, 72, 32, logged.get("iniciais", "MS"))
        out += txt(w - M - 198, 84, logged.get("nome", "Maria Silva"), 13, INK, True)
        out += txt(w - M - 198, 100, logged.get("papel", "Área do Aluno"), 11.5, MUTED)
        out += icon("chev-d", w - M - 74, 79, 16, MUTED, 1.8)
    else:
        out += btn(w - M - 200, 68, 148, 40, "Entrar / Cadastre-se", "primary", 13.5, to="22")
    return out


def footer_pub(y, w=W):
    """rodape institucional (CONTATO + parceiras + transparencia). devolve (svg, altura)"""
    h = 330
    out = rect(0, y, w, h, NAVY)
    out += rect(0, y, w, 4, GOLD)
    cols = [
        ("Escola do Legislativo", [
            "Rua Princesa Isabel, 410 - 1o Andar",
            "Boa Vista - Recife/PE - CEP 50050-330",
            "(81) 3355-4000 | ramal 4120",
            "escoladolegislativo@recife.pe.leg.br",
            "Atendimento: seg a sex, 8h as 17h",
        ]),
        ("Institucional", ["Quem Somos", "História e composição",
                           "Legislação e Transparência",
                           "Instrumentos jurídicos", "Escolas parceiras"]),
        ("Serviços", ["Cursos e eventos", "Área do Aluno",
                           "Validar certificado", "Acervo / Biblioteca", "Notícias"]),
        ("Escolas parceiras", ["ALMG - Minas Gerais", "ALEP - Paraná",
                               "Interlegis / ILB", "ABEL - Associação Brasileira",
                               "Ver todas as parceiras"]),
    ]
    dests = [[None] * 5,
             ["10", "11", "12", "12", "13"],
             ["02", "29", "17", "14", "08"],
             ["13"] * 5]
    cw = 270
    for i, (t, items) in enumerate(cols):
        cx = M + i * cw
        out += txt(cx, y + 62, t, 15, WHITE, True)
        out += rect(cx, y + 74, 28, 3, GOLD, None, 2)
        for j, it in enumerate(items):
            ds_hot(cx - 6, y + 92 + j * 26, tw(it, 13) + 26, 24, dests[i][j], it)
            out += txt(cx, y + 106 + j * 26, it, 13, "#B7C7D6")
            if i == 3:
                out += icon("link", cx + tw(it, 13) + 8, y + 94 + j * 26, 13, "#7D93A8", 1.7)
    out += line(M, y + h - 66, w - M, y + h - 66, "#2A4A6B", 1.2)
    out += txt(M, y + h - 34, "© 2026 Câmara Municipal do Recife - Divisão de Informática", 12.5, "#8FA6BA")
    out += txt(w - M, y + h - 34, "Política de Privacidade  |  LGPD  |  Termos de uso", 12.5, "#8FA6BA", anchor="end")
    return out, y + h


def page_hero(y, title, sub=None, crumbs=None, h=150, w=W, tone=NAVY):
    out = rect(0, y, w, h, tone)
    ty = y + 62
    if crumbs:
        out += _crumb_light(M, y + 44, crumbs)
        ty = y + 92
    out += txt(M, ty, title, 34, WHITE, True)
    if sub:
        out += txt(M, ty + 30, sub, 15.5, "#B7C7D6")
    return out, y + h


def _crumb_light(x, y, items):
    out = ""
    cx = x
    for i, it in enumerate(items):
        last = i == len(items) - 1
        out += txt(cx, y, it, 12.5, WHITE if last else "#9FB6CB", last)
        cx += tw(it, 12.5, last)
        if not last:
            out += icon("chev-r", cx + 5, y - 11, 12, "#7D93A8", 1.8)
            cx += 21
    return out


crumb_light = _crumb_light
ALERTS = _ALERT


# ---------------------------------------------------------------- shell admin
SB_W = 268

MENU_GESTOR = [
    ("Painel", "grid", "39"),
    ("Cursos", "book", "40"),
    ("Turmas", "users", "42"),
    ("Inscrições", "list", "43"),
    ("Fila de espera", "clock", "45"),
    ("Frequência", "check", "46"),
    ("Certificados", "cert", "47"),
    ("Professores", "user", "48"),
    ("Conteúdo do portal", "edit", "49"),
    ("Relatórios", "chart", "52"),
]

MENU_PROF = [
    ("Painel", "grid", "53"),
    ("Meus cursos", "book", "53"),
    ("Alunos inscritos", "users", "54"),
    ("Materiais", "folder", "55"),
    ("Meus dados", "user", ""),
]


def sidebar(h, menu, active, papel="ÁREA DO GESTOR", nome="Robertson Barros",
            cargo="Gestor da Escola", ini="RB"):
    out = rect(0, 0, SB_W, h, NAVY)
    out += rect(28, 30, 42, 42, NAVY_3, None, 8)
    out += icon_c("board", 49, 51, 22, GOLD, 1.9)
    out += txt(80, 46, "Escola do", 14, WHITE, True)
    out += txt(80, 64, "Legislativo", 14, WHITE, True)
    out += txt(28, 104, papel, 10.5, GOLD, True, ls="1.4")
    out += line(28, 118, SB_W - 28, 118, "#27476A", 1.2)
    y = 138
    for lbl, ic, _dst in menu:
        on = lbl == active
        if not on:
            ds_hot(14, y, SB_W - 28, 44, _dst, lbl)
        if on:
            out += rect(14, y, SB_W - 28, 44, NAVY_3, None, 8)
            out += rect(14, y + 9, 3.5, 26, GOLD, None, 2)
        out += icon(ic, 34, y + 12, 19, GOLD if on else "#8FA6BA", 1.8)
        out += txt(68, y + 28, lbl, 14, WHITE if on else "#B7C7D6", on)
        y += 50
    out += line(28, h - 122, SB_W - 28, h - 122, "#27476A", 1.2)
    out += avatar(28, h - 98, 40, ini, "#2C5480")
    out += txt(78, h - 78, nome, 13.5, WHITE, True)
    out += txt(78, h - 60, cargo, 12, "#8FA6BA")
    out += icon("logout", 28, h - 44, 17, "#8FA6BA", 1.8)
    out += txt(54, h - 31, "Sair do sistema", 13, "#B7C7D6")
    return out


def topbar_admin(title, sub=None, w=W, x0=SB_W, actions=None, crumbs=None):
    ww = w - x0
    out = rect(x0, 0, ww, 96, WHITE)
    out += line(x0, 96, w, 96, BORDER, 1.2)
    ty = 46
    if crumbs:
        out += breadcrumb(x0 + 36, 34, crumbs)
        ty = 62
    out += txt(x0 + 36, ty, title, 23, INK, True)
    if sub:
        out += txt(x0 + 36, ty + 21, sub, 13, MUTED)
    cx = w - 36
    out += rect(cx - 40, 28, 40, 40, WHITE, BORDER2, 8, 1.3)
    out += icon_c("bell", cx - 20, 48, 18, TXT, 1.8)
    out += circ(cx - 10, 36, 7, RED)
    out += ctext(cx - 10, 36, "3", 9.5, WHITE, True)
    cx -= 52
    if actions:
        for act in actions[::-1]:
            lbl, kind, ic = act[0], act[1], act[2]
            dst = act[3] if len(act) > 3 else None
            wd = tw(lbl, 13.5, True) + (60 if ic else 36)
            out += btn(cx - wd, 28, wd, 40, lbl, kind, 13.5, ic, to=dst)
            cx -= wd + 12
    return out


# ---------------------------------------------------------------- nota de analise
def nota(y, w, rfs, decisoes=None, obs=None, telas=None):
    """Faixa de anotacao de analise (grupo NOTA-ANALISE, apagavel no Figma)."""
    inner = ""
    dh = 0
    if decisoes:
        dh = sum(28 + para_h(d, w - 300, 13.5, 19) for d in decisoes) + 34
    oh = (para_h(obs, w - 200, 13.5, 20) + 34) if obs else 0
    h = 108 + dh + oh
    inner += rect(0, y, w, h, "#101E2B")
    inner += rect(0, y, w, 3, GOLD)
    inner += txt(M, y + 36, "NOTA DE ANÁLISE - NÃO FAZ PARTE DA INTERFACE", 11,
                 GOLD, True, ls="1.6")
    inner += txt(M, y + 40, "", 11)
    inner += txt(M, y + 68, "Requisitos atendidos nesta tela", 12.5, "#8FA6BA", True)
    cx = M + 240
    for r in rfs:
        wd = tw(r, 12, True) + 22
        inner += rect(cx, y + 55, wd, 22, "#1D3448", "#2F5171", 4, 1)
        inner += ctext(cx + wd / 2.0, y + 66, r, 12, "#CFE0EE", True)
        cx += wd + 8
    yy = y + 100
    if decisoes:
        inner += txt(M, yy, "Decisões pendentes de reunião", 12.5, "#E9B44C", True)
        yy += 22
        for d in decisoes:
            inner += circ(M + 6, yy - 4, 4.5, "#D9534F")
            for i, l in enumerate(wrap(d, w - 300, 13.5)):
                inner += txt(M + 22, yy + i * 19, l, 13.5, "#C7D6E3")
            yy += para_h(d, w - 300, 13.5, 19) + 10
        yy += 12
    if obs:
        inner += txt(M, yy, "Observação", 12.5, "#8FA6BA", True)
        yy += 20
        for i, l in enumerate(wrap(obs, w - 200, 13.5)):
            inner += txt(M, yy + i * 20, l, 13.5, "#9FB6CB")
    return grp(inner, "NOTA-ANALISE"), y + h


def nota_h(w, rfs, decisoes=None, obs=None):
    dh = 0
    if decisoes:
        dh = sum(28 + para_h(d, w - 300, 13.5, 19) for d in decisoes) + 34
    oh = (para_h(obs, w - 200, 13.5, 20) + 34) if obs else 0
    return 108 + dh + oh


# ---------------------------------------------------------------- documento
def svg(name, width, height, body, bgc=BG):
    return (
        '<svg xmlns="http://www.w3.org/2000/svg" width="%s" height="%s" '
        'viewBox="0 0 %s %s">\n'
        '  <title>%s</title>\n'
        '  <rect width="%s" height="%s" fill="%s"/>\n'
        '%s</svg>\n' % (n(width), n(height), n(width), n(height), esc(name),
                        n(width), n(height), bgc, body)
    )
