# -*- coding: utf-8 -*-
"""Telas 56 e 57: mapa de navegacao e painel de decisoes em reuniao."""
from blocks import *
from dados import TELAS as INV, MODULOS, LINKS, FLUXO, DECISOES, TELA_POR_NUM

TELAS = []

CORES = {"publico": (BLUE, BLUE_L), "auth": (GOLD, GOLD_L), "aluno": (GREEN, GREEN_L),
         "gestor": (PURPLE, PURPLE_L), "prof": ("#1D6F73", "#DFEFF0"), "apoio": (MUTED, "#EDF1F5")}


def reg(fn):
    TELAS.append(fn)
    return fn


# ================================================================ 56 MAPA
@reg
def t56():
    MW = 2000
    colw = 296
    gap = 28
    x0 = 80
    b = rect(0, 0, MW, 200, NAVY)
    b += rect(0, 0, MW, 4, GOLD)
    b += rect(x0, 44, 52, 52, NAVY_3, None, 9)
    b += icon_c("board", x0 + 26, 70, 26, GOLD, 1.9)
    b += txt(x0 + 66, 66, "Portal da Escola do Legislativo", 24, WHITE, True)
    b += txt(x0 + 66, 90, "Câmara Municipal do Recife · Divisão de Informática · processo nº 3096/2025",
             13, "#8FA6BA")
    b += txt(x0, 146, "Mapa de navegação do protótipo", 30, WHITE, True)
    b += txt(x0, 176, "57 frames · %d ligações previstas no modo Prototype do Figma" % len(LINKS),
             13.5, "#B7C7D6")
    for i, (l, v) in enumerate([("57", "frames"), ("17", "requisitos funcionais"), ("14", "decisões")]):
        x = MW - 80 - (3 - i) * 150
        b += txt(x, 150, l, 26, GOLD, True)
        b += txt(x, 176, v, 11.5, "#8FA6BA")

    # ---- fluxo principal
    fy = 240
    b += txt(x0, fy, "Fluxo principal do aluno", 17, INK, True)
    b += rect(x0, fy + 10, 40, 3.5, GOLD, None, 2)
    fy += 40
    bw2 = 190
    for i, num in enumerate(FLUXO):
        t = TELA_POR_NUM[num]
        c1, c2 = CORES[t[3]]
        x = x0 + i * (bw2 + 42)
        b += rect(x, fy, bw2, 74, c2, c1, 8, 1.4)
        b += rect(x, fy, 34, 74, c1, None, 8)
        b += rect(x + 24, fy, 10, 74, c1)
        b += ctext(x + 17, fy + 37, num, 15, WHITE, True)
        for j, l in enumerate(wrap(t[2], bw2 - 54, 12.5, True)[:3]):
            b += txt(x + 46, fy + 26 + j * 16, l, 12.5, INK, True)
        if i < len(FLUXO) - 1:
            b += line(x + bw2 + 6, fy + 37, x + bw2 + 32, fy + 37, "#8DA0B3", 2)
            b += path("M%s %s l-8 -5 l0 10 Z" % (n(x + bw2 + 34), n(fy + 37)), "#8DA0B3")
    fy += 74 + 46

    # ---- colunas por modulo
    b += line(x0, fy - 14, MW - 80, fy - 14, BORDER, 1.2)
    tops = {}
    for ci, (key, titulo, sub) in enumerate(MODULOS):
        x = x0 + ci * (colw + gap)
        c1, c2 = CORES[key]
        b += rect(x, fy + 10, colw, 62, c1, None, 8)
        b += txt(x + 18, fy + 40, titulo, 14, WHITE, True)
        b += txt(x + 18, fy + 60, sub, 11, "#FFFFFF", op=0.8)
        y = fy + 86
        for t in [t for t in INV if t[3] == key]:
            b += rect(x, y, colw, 50, WHITE, BORDER, 6, 1.2)
            b += rect(x, y, 4, 50, c1, None, 2)
            b += rect(x + 14, y + 14, 30, 22, c2, None, 4)
            b += ctext(x + 29, y + 25, t[0], 12, c1, True)
            b += para(x + 54, y + 22, t[2], colw - 68, 12.5, INK, 14, True, maxlines=1)
            b += txt(x + 54, y + 39, t[4], 10, MUTED)
            y += 56
        tops[key] = y
    maxy = max(tops.values())

    # ---- setas entre modulos
    for a, bkey in [("publico", "auth"), ("auth", "aluno"), ("auth", "gestor"), ("gestor", "prof")]:
        ia = [m[0] for m in MODULOS].index(a)
        ib = [m[0] for m in MODULOS].index(bkey)
        xa = x0 + ia * (colw + gap) + colw
        xb = x0 + ib * (colw + gap)
        yy = fy + 41
        if ib - ia == 1:
            b += line(xa + 4, yy, xb - 10, yy, GOLD, 2.4)
            b += path("M%s %s l-9 -6 l0 12 Z" % (n(xb - 6), n(yy)), GOLD)
    b += txt(x0, maxy + 34, "Como ligar no Figma:", 14, INK, True)
    b += txt(x0 + 158, maxy + 34, "selecione o botão ou a área clicável → aba Prototype → arraste a "
                                  "setinha até o frame de destino → On click / Navigate to / Instant.",
             13.5, MUTED)
    b += txt(x0, maxy + 62, "As setas deste mapa são apenas indicação visual do fluxo; quem redireciona "
                            "é a ligação criada no painel Prototype.", 12.5, FAINT)
    leg = maxy + 96
    b += line(x0, leg, MW - 80, leg, BORDER, 1.2)
    cx = x0
    for key, titulo, _ in MODULOS:
        c1, c2 = CORES[key]
        b += rect(cx, leg + 22, 14, 14, c1, None, 3)
        b += txt(cx + 22, leg + 34, titulo, 12, TXT)
        cx += tw(titulo, 12) + 60
    H = leg + 72
    return "56-mapa-de-navegacao", svg("56-mapa-de-navegacao", MW, H, b, WHITE)


# ================================================================ 57 DECISOES
@reg
def t57():
    b = rect(0, 0, W, 230, NAVY)
    b += rect(0, 0, W, 4, GOLD)
    b += badge(M, 44, "PAUTA DA REUNIÃO", "solid-amber", 12, 28)[0]
    b += txt(M, 118, "Decisões pendentes do Portal da Escola do Legislativo", 32, WHITE, True)
    b += para(M, 152, "Pontos marcados como [DECISÃO EM REUNIÃO] no documento preliminar de "
                      "especificação de requisitos. Cada item indica em quais telas do protótipo a "
                      "escolha aparece.", 900, 14.5, "#B7C7D6", 22)
    b += rect(W - M - 200, 60, 200, 110, NAVY_3, GOLD, 10, 1.4)
    b += ctext(W - M - 100, 96, str(len(DECISOES)), 40, GOLD, True)
    b += ctext(W - M - 100, 128, "decisões a tomar", 12, WHITE, True)
    b += ctext(W - M - 100, 148, "processo nº 3096/2025", 10.5, "#8FA6BA")
    y = 230 + 44

    cwid = (CW - 24) / 2.0

    def _card_h(d):
        _n, _rf, perg, oa, ob, _t = d
        ql = len(wrap(perg, cwid - 44, 15, True)[:2])
        oh = 0
        for op in (oa, ob):
            oh += max(46, para_h(op, cwid - 116, 12.5, 17) + 24) + 8
        return 66 + ql * 22 + 20 + oh + 48

    for row in [DECISOES[i:i + 2] for i in range(0, len(DECISOES), 2)]:
        ch = max(_card_h(d) for d in row)
        for j, (num, rf, pergunta, oa, ob, telas) in enumerate(row):
            x = M + j * (cwid + 24)
            yy = y
            b += rect(x, yy, cwid, ch, WHITE, BORDER, 12, 1.3)
            b += rect(x, yy, cwid, 5, GOLD, None, 12)
            b += rect(x, yy + 3, cwid, 2, GOLD)
            b += circ(x + 34, yy + 40, 17, NAVY)
            b += ctext(x + 34, yy + 40, num, 12.5, WHITE, True)
            b += badge(x + 60, yy + 28, rf, "info", 11)[0]
            ql = len(wrap(pergunta, cwid - 44, 15, True)[:2])
            b += para(x + 22, yy + 82, pergunta, cwid - 44, 15, INK, 21, True, maxlines=2)
            oy = yy + 66 + ql * 22 + 20
            for lbl, txt_op in [("A", oa), ("B", ob)]:
                hh = max(46, para_h(txt_op, cwid - 116, 12.5, 17) + 24)
                b += rect(x + 22, oy, cwid - 44, hh, "#F7FAFC", BORDER, 8, 1.1)
                b += circ(x + 42, oy + hh / 2.0, 11, WHITE, BORDER2, 1.5)
                b += ctext(x + 42, oy + hh / 2.0, lbl, 11.5, MUTED, True)
                b += para(x + 62, oy + 20, txt_op, cwid - 100, 12.5, TXT, 17, maxlines=3)
                oy += hh + 8
            b += line(x + 22, yy + ch - 40, x + cwid - 22, yy + ch - 40, "#EDF1F6", 1.2)
            b += icon("board", x + 22, yy + ch - 30, 14, MUTED, 1.7)
            b += txt(x + 44, yy + ch - 19, "Telas: " + telas, 11.5, MUTED)
            b += txt(x + cwid - 22, yy + ch - 19, "Decisão: ____________", 11.5, FAINT, anchor="end")
        y += ch + 20
    y += 4

    b += rect(M, y, CW, 190, NAVY, None, 12)
    b += txt(M + 32, y + 48, "Encaminhamento sugerido", 20, WHITE, True)
    for i, (t, d) in enumerate([("1. Validar o protótipo",
                                 "Percorrer os 57 frames com a equipe da Escola do Legislativo."),
                                ("2. Fechar as 14 decisões",
                                 "Registrar as escolhas em ata e anexar ao processo nº 3096/2025."),
                                ("3. Consolidar a especificação",
                                 "Atualizar o documento de requisitos com as decisões tomadas.")]):
        x = M + 32 + i * 388
        b += txt(x, y + 92, t, 14.5, GOLD, True)
        b += para(x, y + 116, d, 340, 12.5, "#B7C7D6", 18)
    y += 190 + 44
    return "57-decisoes-em-reuniao", svg("57-decisoes-em-reuniao", W, y, b, WHITE)
