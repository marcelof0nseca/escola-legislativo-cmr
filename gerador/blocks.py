# -*- coding: utf-8 -*-
"""Blocos compostos: card de curso, card de noticia, certificado, QR, etc."""
from comp import *

TONES = [BLUE_L2, "#D9E7DA", "#E5DED2", "#DAE0EC", "#E2DDEB", "#D6E4E8",
         "#E8DFD6", "#DCE6DE"]

# ---------------------------------------------------------------- dados de exemplo
CURSOS = [
    dict(t="Processo Legislativo Municipal", tema="Processo Legislativo",
         d="14 e 15/09/2026", hr="19h às 22h", ch="8h", fmt="Online",
         st=("Inscrições abertas", "abertas"), vagas=(18, 30),
         pub="Interno e externo", prof="Dra. Helena Vasconcelos", tone=0),
    dict(t="Ética e Conduta no Serviço Público", tema="Direito",
         d="22 a 24/09/2026", hr="14h às 18h", ch="12h", fmt="Presencial",
         st=("Inscrições em breve", "breve"), vagas=(0, 40),
         pub="Interno", prof="Prof. Marcelo Andrade", tone=1),
    dict(t="Tecnologia e Governo Digital", tema="Tecnologia",
         d="05 e 06/10/2026", hr="09h às 12h", ch="6h", fmt="Híbrido",
         st=("Esgotado", "esgotado"), vagas=(35, 35),
         pub="Interno e externo", prof="Prof. Diego Farias", tone=2),
    dict(t="Redação Oficial e Técnica Legislativa", tema="Redação Oficial",
         d="19 a 21/10/2026", hr="09h às 12h", ch="12h", fmt="Presencial",
         st=("Inscrições abertas", "abertas"), vagas=(9, 25),
         pub="Interno", prof="Profa. Cláudia Nunes", tone=3),
    dict(t="Orçamento Público e LOA Municipal", tema="Orçamento",
         d="03 e 04/11/2026", hr="14h às 18h", ch="8h", fmt="Online",
         st=("Inscrições abertas", "abertas"), vagas=(27, 60),
         pub="Interno e externo", prof="Dr. Paulo Meneses", tone=4),
    dict(t="LGPD na Administração Pública", tema="Direito",
         d="17/11/2026", hr="09h às 17h", ch="8h", fmt="Híbrido",
         st=("Inscrições em breve", "breve"), vagas=(0, 50),
         pub="Interno e externo", prof="Dra. Renata Lopes", tone=5),
]

CURSOS_FEITOS = [
    dict(t="Controle Interno e Prestação de Contas", tema="Controle",
         d="12 e 13/05/2026", hr="14h às 18h", ch="8h", fmt="Presencial",
         st=("Encerrado", "encerradas"), vagas=(30, 30),
         pub="Interno", prof="Dr. Sérgio Batista", tone=6),
    dict(t="Audiências Públicas e Participação Cidadã", tema="Processo Legislativo",
         d="08/04/2026", hr="09h às 13h", ch="4h", fmt="Online",
         st=("Encerrado", "encerradas"), vagas=(80, 80),
         pub="Externo", prof="Profa. Ana Beatriz", tone=7),
    dict(t="Introdução ao Direito Municipal", tema="Direito",
         d="03 a 07/03/2026", hr="19h às 22h", ch="15h", fmt="Presencial",
         st=("Encerrado", "encerradas"), vagas=(25, 25),
         pub="Interno e externo", prof="Dr. Fernando Rocha", tone=1),
]

NOTICIAS = [
    ("Escola do Legislativo firma parceria com a ALMG",
     "Acordo de cooperação técnica permite intercâmbio de cursos e material didático entre as duas escolas.",
     "12/08/2026", "Parcerias"),
    ("Agenda do 2º semestre de 2026 já está disponível",
     "São 14 cursos e 6 eventos abertos a servidores e ao público externo, com certificação digital.",
     "05/08/2026", "Agenda"),
    ("Novas publicações no acervo digital da Escola",
     "Coletânea de manuais de técnica legislativa e cartilhas sobre orçamento público.",
     "28/07/2026", "Acervo"),
    ("Turma de Redação Oficial forma 25 servidores",
     "Curso presencial encerrou com 96% de aproveitamento e certificados já disponíveis.",
     "20/07/2026", "Cursos"),
    ("Escola recebe visita técnica da Câmara de Olinda",
     "Encontro tratou de metodologias de capacitação continuada no Legislativo municipal.",
     "11/07/2026", "Institucional"),
]

PARCEIRAS = [
    ("Escola do Legislativo de Minas Gerais", "ALMG", "www.almg.gov.br", "Acordo de Cooperação Técnica"),
    ("Escola do Legislativo do Paraná", "ALEP", "escola.assembleia.pr.leg.br", "Acordo de Cooperação Técnica"),
    ("Instituto Legislativo Brasileiro", "ILB", "saberes.senado.leg.br", "Termo de Adesão - Interlegis"),
    ("Escola do Legislativo de Pernambuco", "ALEPE", "www.alepe.pe.gov.br", "Convênio de Capacitação"),
    ("Câmara Municipal de Olinda", "CMO", "www.olinda.pe.leg.br", "Termo de Cooperação"),
    ("ABEL - Assoc. Bras. de Escolas do Legislativo", "ABEL", "abel.org.br", "Filiação institucional"),
]


# ---------------------------------------------------------------- card de curso
CARD_W = 384
CARD_H = 452


def card_curso(x, y, c, w=CARD_W, btn_label="Ver detalhes", btn_kind="primary",
               hot=False, show_vagas=True, to=None):
    h = CARD_H
    out = rect(x, y, w, h, WHITE, BORDER, 10, 1.2)
    out += img_ph(x, y, w, 168, 10, TONES[c["tone"] % len(TONES)])
    out += rect(x, y + 158, w, 10, TONES[c["tone"] % len(TONES)])
    bw = badge_w(c["tema"], 11.5, 10)
    out += rect(x + 16, y + 16, bw, 22, "#FFFFFF", None, 11, op=0.92)
    out += txt(x + 26, y + 31, c["tema"], 11.5, INK, True)
    py = y + 186
    out += badges_row(x + 20, py, [c["st"], (c["fmt"], "info")], 11.5, 24, 8, dot=True)[0]
    ty = py + 46
    for i, l in enumerate(wrap(c["t"], w - 40, 17.5, True)[:2]):
        out += txt(x + 20, ty + i * 23, l, 17.5, INK, True)
    ty += 23 * min(2, len(wrap(c["t"], w - 40, 17.5, True))) + 6
    out += line(x + 20, ty, x + w - 20, ty, "#EDF1F6", 1.2)
    my = ty + 26
    metas = [("calendar", "%s  -  %s" % (c["d"], c["hr"])),
             ("clock", "Carga horária: %s" % c["ch"]),
             ("users", "Público: %s" % c["pub"])]
    for ic, t in metas:
        out += icon(ic, x + 20, my - 12, 16, MUTED, 1.6)
        out += txt(x + 44, my + 1, t, 13, TXT)
        my += 24
    fy = y + h - 66
    out += line(x + 20, fy - 14, x + w - 20, fy - 14, "#EDF1F6", 1.2)
    if show_vagas:
        oc, tot = c["vagas"]
        pct = 0 if not tot else min(100, oc * 100.0 / tot)
        out += txt(x + 20, fy + 10, "%s/%s vagas" % (oc, tot), 12.5, MUTED, True)
        out += rect(x + 20, fy + 18, 96, 6, "#E6ECF2", None, 3)
        out += rect(x + 20, fy + 18, 96 * pct / 100.0, 6,
                    RED if pct >= 100 else (AMBER if pct >= 70 else GREEN), None, 3)
    bwd = tw(btn_label, 13.5, True) + 40
    out += btn(x + w - 20 - bwd, fy - 4, bwd, 42, btn_label, btn_kind, 13.5, hot=hot, to=to)
    ds_hot(x, y, w, 168, to, "capa")
    return out, y + h


# ---------------------------------------------------------------- card de noticia
def card_noticia(x, y, nt, w=384, h=336, big=False, to=None):
    t, sub, data, cat = nt
    ds_hot(x, y, w, h, to, t[:30])
    out = rect(x, y, w, h, WHITE, BORDER, 10, 1.2)
    ih = 190 if big else 150
    out += img_ph(x, y, w, ih, 10, TONES[(len(t) + 2) % len(TONES)])
    out += rect(x, y + ih - 10, w, 10, TONES[(len(t) + 2) % len(TONES)])
    bw = badge_w(cat, 11, 10)
    out += rect(x + 16, y + 16, bw, 22, WHITE, None, 4, op=0.94)
    out += txt(x + 26, y + 31, cat, 11, BLUE_D, True)
    ty = y + ih + 30
    out += icon("calendar", x + 20, ty - 22, 14, FAINT, 1.6)
    out += txt(x + 40, ty - 11, data, 12, MUTED)
    ts = 19 if big else 16.5
    ls = wrap(t, w - 40, ts, True)[:2]
    for i, l in enumerate(ls):
        out += txt(x + 20, ty + 12 + i * (ts + 5), l, ts, INK, True)
    py = ty + 12 + len(ls) * (ts + 5) + 12
    out += para(x + 20, py, sub, w - 40, 13.5, MUTED, 20, maxlines=3 if big else 2)
    out += link(x + 20, y + h - 24, "Ler notícia completa", 13, BLUE_D, True, True)
    out += icon("arrow-r", x + 20 + tw("Ler notícia completa", 13, True) + 6, y + h - 36, 14, BLUE_D, 1.8)
    return out


# ---------------------------------------------------------------- QR falso
_QRPAT = [
    "1111111011010101111111", "1000001010001110100001", "1011101011011010111011",
    "1011101001110100101101", "1011101011000110111011", "1000001001011101000001",
    "1111111010101011111111", "0000000011100100000000", "1101101101011011011011",
    "0100011010110100110100", "1110100101101011001011", "0101110110010110110110",
    "1011001011101001011001", "0100110100010110101100", "1110101101101011010011",
    "0000000101011010110101", "1111111011010110011011", "1000001001101001101100",
    "1011101010110101011011", "1011101101001011010110", "1011101011010110101001",
    "1111111001101011011010",
]


def qr(x, y, size=120, color=INK):
    mods = len(_QRPAT)
    m = size / float(mods)
    out = rect(x - 6, y - 6, size + 12, size + 12, WHITE, None, 4)
    for r, rowd in enumerate(_QRPAT):
        c = 0
        while c < mods:
            if rowd[c] == "1":
                c2 = c
                while c2 + 1 < mods and rowd[c2 + 1] == "1":
                    c2 += 1
                out += rect(x + c * m, y + r * m, (c2 - c + 1) * m, m, color)
                c = c2 + 1
            else:
                c += 1
    return out


# ---------------------------------------------------------------- certificado (PDF)
def certificado(x, y, w, h, com_qr=False, codigo="ELCMR-2026-A7K9-3F2D-8B1C"):
    out = rect(x, y, w, h, WHITE, BORDER2, 4, 1.4)
    out += rect(x + 18, y + 18, w - 36, h - 36, None, GOLD, 2, 1.6)
    out += rect(x + 24, y + 24, w - 48, h - 48, None, "#E7D2A4", 2, 1)
    cx = x + w / 2.0
    out += rect(cx - 26, y + 56, 52, 52, NAVY, None, 8)
    out += icon_c("board", cx, y + 82, 28, GOLD, 2)
    out += ctext(cx, y + 132, "CÂMARA MUNICIPAL DO RECIFE", 13, NAVY, True)
    out += ctext(cx, y + 152, "ESCOLA DO LEGISLATIVO", 11.5, GOLD, True)
    out += ctext(cx, y + 208, "CERTIFICADO", 40, NAVY, True)
    out += rect(cx - 60, y + 228, 120, 3, GOLD, None, 2)
    out += ctext(cx, y + 274, "Certificamos que", 14, MUTED)
    out += ctext(cx, y + 312, "MARIA SILVA DOS SANTOS", 28, INK, True)
    out += ctext(cx, y + 352, "CPF 123.***.***-89  -  Matrícula 20.451-7", 13, MUTED)
    out += ctext(cx, y + 392, "concluiu com aproveitamento o curso", 14, MUTED)
    out += ctext(cx, y + 424, "Processo Legislativo Municipal", 22, INK, True)
    out += ctext(cx, y + 458, "carga horária de 8 (oito) horas, realizado nos dias 14 e 15 de setembro de 2026,", 13.5, TXT)
    out += ctext(cx, y + 478, "com frequência de 100% e aprovação na avaliação final.", 13.5, TXT)
    out += ctext(cx, y + h - 236, "Recife, 16 de setembro de 2026.", 13.5, MUTED)
    sy = y + h - 190
    for i, (nome, cargo) in enumerate([("Ricardo Ferraz", "Diretor Geral"),
                                       ("Robertson Barros", "Coordenador da Escola do Legislativo")]):
        sx = x + w * (0.30 if i == 0 else 0.70)
        out += line(sx - 130, sy, sx + 130, sy, "#8A99A8", 1.2)
        out += ctext(sx, sy + 16, nome, 13, INK, True)
        out += ctext(sx, sy + 34, cargo, 11.5, MUTED)
    fy = y + h - 104
    out += line(x + 40, fy, x + w - 40, fy, "#E7D2A4", 1.2)
    if com_qr:
        out += qr(x + 46, fy + 16, 68, NAVY)
        tx0 = x + 132
    else:
        tx0 = x + 46
    out += txt(tx0, fy + 30, "CÓDIGO DE AUTENTICIDADE", 9.5, GOLD, True, ls="1.2")
    out += txt(tx0, fy + 52, codigo, 16, NAVY, True, ls="1")
    out += txt(tx0, fy + 72, "Valide em: escoladolegislativo.recife.pe.leg.br/validar-certificado", 10.5, MUTED)
    if com_qr:
        out += txt(x + w - 46, fy + 30, "Aponte a câmera do celular para o QR Code", 10.5, MUTED, anchor="end")
        out += txt(x + w - 46, fy + 50, "e veja a validação na hora.", 10.5, MUTED, anchor="end")
        out += txt(x + w - 46, fy + 74, "Documento emitido eletronicamente", 10, FAINT, anchor="end")
    else:
        out += txt(x + w - 46, fy + 40, "Documento emitido eletronicamente pela", 10.5, MUTED, anchor="end")
        out += txt(x + w - 46, fy + 58, "Escola do Legislativo - CMR", 10.5, MUTED, anchor="end")
    return out


# ---------------------------------------------------------------- listas
def doc_row(x, y, w, titulo, meta, tipo="PDF", tone=RED_L, tone_fg=RED, h=88,
            acao="Baixar", ic="file", to=None):
    out = rect(x, y, w, h, WHITE, BORDER, 8, 1.2)
    out += rect(x + 20, y + (h - 48) / 2.0, 48, 48, tone, None, 8)
    out += icon_c(ic, x + 44, y + h / 2.0, 22, tone_fg, 1.8)
    bw = tw(acao, 13, True) + 52
    disp = w - 84 - (bw + 96)
    out += para(x + 84, y + h / 2.0 - 4, titulo, disp, 15.5, INK, 20, True, maxlines=1)
    out += para(x + 84, y + h / 2.0 + 17, meta, disp, 12.5, MUTED, 16, maxlines=1)
    out += btn(x + w - 20 - bw, y + (h - 38) / 2.0, bw, 38, acao, "secondary", 13, "download", to=to)
    out += badge(x + w - 20 - bw - 66, y + (h - 24) / 2.0, tipo, "neutro", 11)[0]
    return out, y + h


def timeline(x, y, w, items):
    out = ""
    yy = y
    for i, (ano, titulo, desc) in enumerate(items):
        out += circ(x + 9, yy + 10, 9, WHITE, BLUE, 3)
        if i < len(items) - 1:
            out += line(x + 9, yy + 22, x + 9, yy + 118, BORDER2, 2)
        out += txt(x + 40, yy + 8, ano, 20, BLUE_D, True)
        out += txt(x + 110, yy + 8, titulo, 17, INK, True)
        out += para(x + 40, yy + 34, desc, w - 60, 13.5, MUTED, 20)
        yy += 116
    return out, yy
