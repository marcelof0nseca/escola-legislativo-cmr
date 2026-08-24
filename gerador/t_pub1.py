# -*- coding: utf-8 -*-
"""Telas publicas 01-09: home, vitrine, filtros, realizados, detalhe, noticias."""
from blocks import *

TELAS = []


def reg(fn):
    TELAS.append(fn)
    return fn


# ================================================================ 01 HOME
@reg
def t01():
    b = header_pub("Home")
    # ---- hero
    hy, hh = HEAD_H, 440
    b += rect(0, hy, W, hh, NAVY)
    b += rect(0, hy, W, 4, GOLD)
    b += rect(860, hy + 60, 460, 300, NAVY_2, None, 12)
    b += img_ph(880, hy + 80, 420, 260, 10, NAVY_3, "IMAGEM INSTITUCIONAL", "board")
    bw = badge_w("PORTAL OFICIAL DA ESCOLA DO LEGISLATIVO", 11)
    b += rect(M, hy + 56, bw, 26, NAVY_3, GOLD, 13, 1)
    b += txt(M + 12, hy + 73, "PORTAL OFICIAL DA ESCOLA DO LEGISLATIVO", 11, GOLD, True, ls="0.8")
    b += txt(M, hy + 134, "Conhecimento a serviço do", 40, WHITE, True)
    b += txt(M, hy + 182, "Legislativo Municipal", 40, GOLD, True)
    b += para(M, hy + 222, "Agenda de cursos e eventos, inscrições on-line, certificação digital "
                           "e o acervo da Escola do Legislativo da Câmara Municipal do Recife.",
              620, 15.5, "#B7C7D6", 24)
    # busca rapida
    sy = hy + 292
    b += rect(M, sy, 640, 58, WHITE, None, 8)
    b += icon("search", M + 18, sy + 19, 20, MUTED, 1.8)
    b += txt(M + 50, sy + 36, "Buscar cursos, eventos, notícias ou publicações", 15, FAINT)
    b += btn(M + 640 - 132, sy + 8, 124, 42, "Buscar", "primary", 14)
    b += txt(M, sy + 84, "Buscas frequentes:  Processo Legislativo   ·   LGPD   ·   Redação Oficial   ·   Orçamento",
             12.5, "#8FA6BA")
    # ---- acesso rapido (sobreposto)
    qy = hy + hh - 40
    b += rect(M, qy, CW, 122, WHITE, BORDER, 12, 1.2)
    qa = [("cert", "Validar certificado", "Confira a autenticidade de um certificado", GREEN_L, GREEN),
          ("user", "Área do Aluno", "Meus cursos, certificados e dados", BLUE_L, BLUE),
          ("calendar", "Agenda de cursos", "Tudo que vai acontecer na Escola", GOLD_L, GOLD),
          ("book", "Acervo / Biblioteca", "Publicações, manuais e legislações", PURPLE_L, PURPLE)]
    qa_to = ["17", "22", "02", "14"]
    for i, (ic, t, s, tl, tf) in enumerate(qa):
        x = M + i * 300
        hot(x, qy + 6, 300, 110, qa_to[i], t)
        if i:
            b += line(x, qy + 26, x, qy + 96, BORDER, 1.2)
        b += rect(x + 26, qy + 30, 46, 46, tl, None, 9)
        b += icon_c(ic, x + 49, qy + 53, 23, tf, 1.8)
        b += txt(x + 86, qy + 51, t, 15, INK, True)
        b += para(x + 86, qy + 71, s, 186, 12, MUTED, 16, maxlines=2)
    y = qy + 122 + 78

    # ---- RF1 vitrine
    s, y = sec_title(M, y, "Cursos e eventos",
                     "Agenda de capacitações da Escola do Legislativo",
                     "Ver agenda completa")
    b += s
    hot(W - M - 200, y - 64, 210, 28, "02", "Ver agenda completa")
    y += 34
    s, ty = tabs(M, y, ["Com inscrições abertas", "Cursos e eventos realizados"], 0,
                 to=[None, "04"])
    b += s
    b += rect(W - M - 84, y - 22, 36, 36, WHITE, BORDER2, 18, 1.2)
    b += icon_c("chev-l", W - M - 66, y - 4, 16, MUTED, 1.9)
    b += rect(W - M - 40, y - 22, 36, 36, WHITE, BORDER2, 18, 1.2)
    b += icon_c("chev-r", W - M - 22, y - 4, 16, MUTED, 1.9)
    y = ty + 34
    for i, c in enumerate(CURSOS[:3]):
        b += card_curso(M + i * (CARD_W + 24), y, c, hot=(i == 0), to="05")[0]
    y += CARD_H + 34
    b += btn(M + (CW - 260) / 2.0, y, 260, 50, "Ver agenda completa", "ghost", 15, "arrow-r",
             to="02")
    y += 50 + 90

    # ---- RF3 noticias
    s, y = sec_title(M, y, "Notícias em destaque",
                     "Publicadas pela equipe da Escola do Legislativo", "Ver todas as notícias")
    b += s
    hot(W - M - 200, y - 64, 210, 28, "08", "Ver todas as notícias")
    y += 34
    for i, nt in enumerate(NOTICIAS[:3]):
        b += card_noticia(M + i * (384 + 24), y, nt, to="09")
    y += 336 + 84

    # ---- parceiras
    b += rect(0, y, W, 288, BG2)
    b += txt(M, y + 62, "Escolas do Legislativo parceiras", 26, INK, True)
    b += rect(M, y + 74, 46, 4, GOLD, None, 2)
    b += txt(M, y + 96, "Acesse o portal das escolas com instrumentos jurídicos formalizados com a CMR.",
             14.5, MUTED)
    b += txt(W - M, y + 60, "Ver todas as parcerias", 14, BLUE_D, True, anchor="end")
    hot(W - M - 170, y + 40, 180, 30, "13", "Ver todas as parcerias")
    for i, (nome, sigla, url, _) in enumerate(PARCEIRAS):
        x = M + i * 204
        hot(x, y + 128, 180, 108, "13", sigla)
        b += rect(x, y + 128, 180, 108, WHITE, BORDER, 10, 1.2)
        b += rect(x + 16, y + 146, 40, 40, BLUE_L, None, 8)
        b += ctext(x + 36, y + 166, sigla, 13 if len(sigla) <= 4 else 11, BLUE_D, True)
        b += para(x + 16, y + 204, nome, 148, 11.5, TXT, 15, maxlines=2)
        b += icon("link", x + 148, y + 152, 15, FAINT, 1.7)
    y += 288 + 84

    # ---- transparencia + acervo
    cwid = (CW - 24) / 2.0
    for i, (tit, sub, items, ic, acao) in enumerate([
        ("Legislação e Transparência", "Instrumentos jurídicos formalizados pela Escola",
         [("Acordo de Cooperação Técnica nº 04/2026", "ALMG · vigência até 03/2028"),
          ("Termo de Adesão Interlegis nº 11/2025", "ILB/Senado · vigência indeterminada"),
          ("Resolução nº 1.842/2024", "Cria a Escola do Legislativo da CMR")], "shield", "Ver todos os instrumentos"),
        ("Acervo / Biblioteca", "Publicações, manuais e legislações da Escola",
         [("Manual de Técnica Legislativa - 3ª edição", "PDF · 4,2 MB · atualizado em 07/2026"),
          ("Cartilha do Orçamento Público Municipal", "PDF · 1,8 MB · publicado em 05/2026"),
          ("Coletânea de Legislação Municipal 2026", "PDF · 9,6 MB · publicado em 02/2026")], "book", "Ir para o acervo")]):
        x = M + i * (cwid + 24)
        b += rect(x, y, cwid, 336, WHITE, BORDER, 12, 1.2)
        b += rect(x + 28, y + 28, 42, 42, BLUE_L, None, 8)
        b += icon_c(ic, x + 49, y + 49, 21, BLUE, 1.8)
        b += txt(x + 84, y + 46, tit, 18, INK, True)
        b += txt(x + 84, y + 66, sub, 12.5, MUTED)
        yy = y + 102
        for t, m in items:
            b += line(x + 28, yy, x + cwid - 28, yy, "#EDF1F6", 1.2)
            b += txt(x + 28, yy + 28, t, 14, INK, True)
            b += txt(x + 28, yy + 48, m, 12, MUTED)
            b += icon("chev-r", x + cwid - 46, yy + 26, 16, FAINT, 1.8)
            yy += 62
        b += link(x + 28, y + 308, acao, 13.5, BLUE_D, True, True, to=("12" if i == 0 else "14"))
    y += 336 + 76

    s, y = footer_pub(y)
    b += s
    s, y = nota(y, W, ["RF 1", "RF 3", "RF 4", "Busca rápida", "Acesso rápido", "Estrutura do portal"],
                ["RF 3 - As notícias em destaque serão marcadas manualmente pelo gestor ou o portal "
                 "exibe automaticamente as N notícias mais recentes por data de cadastro?"],
                "Home concentra: vitrine de cursos com abas (abertos/realizados), notícias em destaque, "
                "busca rápida por texto simples, ícones de acesso rápido (Validar Certificado e Área do "
                "Aluno), escolas parceiras e instrumentos jurídicos.")
    b += s
    return "01-home", svg("01-home", W, y, b, WHITE)


# ================================================================ 02 VITRINE
def _filtros(b, y, chips=None):
    """barra de filtros avancados RF1"""
    h = 118 if not chips else 168
    b += rect(M, y, CW, h, WHITE, BORDER, 10, 1.2)
    b += txt(M + 24, y + 34, "Filtrar cursos e eventos", 15, INK, True)
    b += icon("filter", M + 24 + tw("Filtrar cursos e eventos", 15, True) + 10, y + 20, 17, GOLD, 1.8)
    fw = 250
    labs = [("Mês", "Setembro de 2026"), ("Tema", "Todos os temas"),
            ("Público", "Todos os públicos"), ("Formato", "Todos os formatos")]
    for i, (l, v) in enumerate(labs):
        x = M + 24 + i * (fw + 14)
        b += txt(x, y + 62, l, 12, MUTED, True)
        b += rect(x, y + 70, fw, 40, WHITE, BORDER2, 6, 1.3)
        b += txt(x + 12, y + 95, v, 13.5, TXT)
        b += icon("chev-d", x + fw - 28, y + 81, 17, MUTED, 1.8)
    b += btn(M + CW - 24 - 116, y + 70, 116, 40, "Aplicar", "primary", 13.5, to="03")
    if chips:
        b += line(M + 24, y + 126, M + CW - 24, y + 126, "#EDF1F6", 1.2)
        b += txt(M + 24, y + 152, "Filtros ativos:", 12.5, MUTED, True)
        cx = M + 24 + 90
        for c in chips:
            wd = tw(c, 12, True) + 42
            b += rect(cx, y + 136, wd, 28, BLUE_L, "#A9CBE8", 14, 1)
            b += txt(cx + 12, y + 154, c, 12, BLUE_D, True)
            b += icon("close", cx + wd - 24, y + 143, 13, BLUE_D, 1.9)
            cx += wd + 8
        b += link(cx + 6, y + 155, "Limpar filtros", 12.5, MUTED, True)
    return b, y + h


def _vitrine(nome, titulo, aba, cursos, chips=None, total="18", rfs=None, dec=None, obs=None,
             btn_label="Ver detalhes", show_vagas=True):
    abas_to = ["02", "04"]
    b = header_pub("Cursos e Eventos")
    s, y = page_hero(HEAD_H, titulo,
                     "Agenda de capacitações, seminários e eventos da Escola do Legislativo",
                     ["Home", "Cursos e Eventos"], 170)
    b += s
    y += 40
    b, y = _filtros(b, y, chips)
    y += 34
    s, ty = tabs(M, y, ["Com inscrições abertas", "Cursos e eventos realizados"], aba,
                 to=abas_to)
    b += s
    y = ty + 28
    b += txt(M, y + 8, "%s resultados encontrados" % total, 13.5, MUTED)
    b += txt(W - M - 190, y + 8, "Ordenar por:", 13, MUTED)
    b += txt(W - M - 100, y + 8, "Data mais próxima", 13, BLUE_D, True)
    b += icon("chev-d", W - M - 18, y - 4, 15, BLUE_D, 1.8)
    y += 30
    for i, c in enumerate(cursos):
        cx = M + (i % 3) * (CARD_W + 24)
        cy = y + (i // 3) * (CARD_H + 28)
        b += card_curso(cx, cy, c, btn_label=btn_label, show_vagas=show_vagas, to="05")[0]
    rows = (len(cursos) + 2) // 3
    y += rows * (CARD_H + 28) + 16
    s, y = pagination(M, y, CW, total)
    b += s
    y += 80
    s, y = footer_pub(y)
    b += s
    s, y = nota(y, W, rfs or ["RF 1"], dec, obs)
    b += s
    return nome, svg(nome, W, y, b, WHITE)


@reg
def t02():
    return _vitrine("02-cursos-vitrine", "Cursos e Eventos", 0, CURSOS, None, "18",
                    ["RF 1"], None,
                    "RF 1 - Vitrine com cards contendo imagem de capa, título, data, carga horária, "
                    "etiqueta de status (Em breve / Abertas / Esgotado / Encerradas), etiqueta de formato "
                    "(Presencial / Online / Híbrido) e botão de detalhes. Filtros por mês, tema e público.")


@reg
def t03():
    return _vitrine("03-cursos-filtros-aplicados", "Cursos e Eventos", 0,
                    [CURSOS[0], CURSOS[3], CURSOS[5]],
                    ["Mês: Setembro/2026", "Tema: Direito", "Público: Interno"], "3",
                    ["RF 1"], None,
                    "Demonstra o resultado dos filtros avançados aplicados (mês, tema e público), "
                    "com chips removíveis e contagem de resultados.")


@reg
def t04():
    return _vitrine("04-cursos-realizados", "Cursos e Eventos realizados", 1,
                    CURSOS_FEITOS, None, "42", ["RF 1"], None,
                    "Aba de cursos concluídos exigida no RF 1: mesmos cards, com etiqueta 'Encerrado', "
                    "para consulta das informações de cursos já finalizados.",
                    btn_label="Ver informações")


# ================================================================ 05-07 DETALHE
def _detalhe_base(aba):
    c = CURSOS[0]
    b = header_pub("Cursos e Eventos")
    y = HEAD_H
    b += rect(0, y, W, 300, NAVY)
    b += img_ph(W - M - 420, y + 40, 420, 220, 10, NAVY_3, "IMAGEM DE CAPA DO CURSO")
    b += crumb_light(M, y + 44, ["Home", "Cursos e Eventos", "Processo Legislativo Municipal"])
    s, _ = badges_row(M, y + 66, [c["st"], (c["fmt"], "solid-blue"), (c["tema"], "solid-navy")], 12, 26, 8, dot=True)
    b += s
    b += txt(M, y + 136, "Processo Legislativo Municipal", 36, WHITE, True)
    b += txt(M, y + 168, "Tramitação de proposições, comissões e técnica de votação na Câmara Municipal",
             15.5, "#B7C7D6")
    metas = [("calendar", "14 e 15/09/2026"), ("clock", "19h às 22h · 8 horas"),
             ("pin", "Online · ao vivo"), ("users", "Interno e externo")]
    for i, (ic, t) in enumerate(metas):
        x = M + i * 220
        b += icon(ic, x, y + 212, 17, GOLD, 1.7)
        b += txt(x + 26, y + 226, t, 13.5, "#DCE7F0")
    y += 300 + 40

    lw, rw = 762, 414
    rx = M + lw + 24

    # ---------------- coluna direita (sticky de inscricao)
    ry = y
    b += rect(rx, ry, rw, 372, WHITE, BORDER, 12, 1.4)
    b += rect(rx, ry, rw, 6, GREEN, None, 12)
    b += rect(rx, ry + 3, rw, 3, GREEN)
    b += txt(rx + 24, ry + 44, "Inscrições abertas", 18, GREEN, True)
    b += txt(rx + 24, ry + 66, "Encerram em 10/09/2026 às 23h59", 12.5, MUTED)
    b += txt(rx + 24, ry + 104, "18 de 30 vagas preenchidas", 13, TXT, True)
    b += rect(rx + 24, ry + 114, rw - 48, 8, "#E6ECF2", None, 4)
    b += rect(rx + 24, ry + 114, (rw - 48) * 0.6, 8, AMBER, None, 4)
    b += txt(rx + 24, ry + 142, "12 vagas restantes", 12, AMBER, True)
    b += btn(rx + 24, ry + 162, rw - 48, 52, "Inscrever-se neste curso", "primary", 16, hot=True,
             to="30")
    b += btn(rx + 24, ry + 224, rw - 48, 44, "Entrar na lista de espera", "disabled", 14, to="33")
    b += txt(rx + 24, ry + 288, "Gratuito · Certificado digital ao final", 12.5, MUTED)
    b += line(rx + 24, ry + 304, rx + rw - 24, ry + 304, "#EDF1F6", 1.2)
    b += icon("shield", rx + 24, ry + 324, 17, GREEN, 1.7)
    b += txt(rx + 50, ry + 338, "Frequência mínima de 75% para certificado", 12.5, MUTED)
    ry += 372 + 20

    b += rect(rx, ry, rw, 190, WHITE, BORDER, 12, 1.2)
    b += txt(rx + 24, ry + 40, "Acesso ao curso online", 16, INK, True)
    b += icon("play", rx + rw - 48, ry + 26, 20, BLUE, 1.8)
    b += rect(rx + 24, ry + 58, rw - 48, 62, AMBER_L, "#EBCE95", 8, 1.2)
    b += icon("lock", rx + 40, ry + 78, 18, AMBER, 1.8)
    b += para(rx + 66, ry + 84, "O link da transmissão será liberado nesta página após a confirmação da inscrição.",
              rw - 108, 12.5, AMBER, 17)
    b += txt(rx + 24, ry + 146, "Plataforma: ambiente do portal / transmissão", 12.5, MUTED)
    b += txt(rx + 24, ry + 164, "externa (a definir em reunião)", 12.5, MUTED)
    ry += 190 + 20

    b += rect(rx, ry, rw, 176, WHITE, BORDER, 12, 1.2)
    b += txt(rx + 24, ry + 40, "Compartilhar e apoio", 16, INK, True)
    for i, (ic, t) in enumerate([("link", "Copiar link do curso"),
                                 ("print", "Imprimir ficha do curso"),
                                 ("mail", "Dúvidas: escoladolegislativo@recife.pe.leg.br")]):
        b += icon(ic, rx + 24, ry + 62 + i * 34, 17, MUTED, 1.7)
        b += txt(rx + 50, ry + 76 + i * 34, t, 12.5, BLUE_D if i < 2 else MUTED)
    ry += 176

    # ---------------- coluna esquerda: abas
    s, ty = tabs(M, y + 18, ["O que você vai aprender", "Sobre o professor",
                             "Cronograma e turmas", "Materiais"], aba, 15, 30, lw,
                 to=["05", "06", "07", "36"])
    b += s
    ly = ty + 40
    return b, c, y, ly, lw, rx, rw, ry


@reg
def t05():
    b, c, y0, ly, lw, rx, rw, ry = _detalhe_base(0)
    b += rect(M, ly, lw, 310, WHITE, BORDER, 12, 1.2)
    b += txt(M + 28, ly + 46, "O que você vai aprender (Ementa)", 20, INK, True)
    b += para(M + 28, ly + 80, "O curso apresenta o rito completo de tramitação de proposições na Câmara "
                               "Municipal do Recife, do protocolo à sanção, com exercícios práticos sobre "
                               "emendas, pareceres e ordem do dia.", lw - 56, 14.5, TXT, 22)
    yy = ly + 160
    for i, t in enumerate(["Espécies de proposições e admissibilidade",
                           "Comissões permanentes e temporárias",
                           "Regime de tramitação, quórum e votação",
                           "Redação final, autógrafo, sanção e veto",
                           "Transparência e participação cidadã",
                           "Ordem do dia e técnica de votação"]):
        cx = M + 28 + (i % 2) * ((lw - 56) / 2.0)
        cy = yy + (i // 2) * 32
        b += circ(cx + 8, cy - 4, 8, GREEN_L)
        b += path("M%s %s l2.6 2.8 L%s %s" % (n(cx + 4.5), n(cy - 4), n(cx + 12), n(cy - 9)), None, GREEN, 2)
        b += txt(cx + 26, cy, t, 13.5, TXT)
    ly += 310 + 24

    b += rect(M, ly, lw, 214, WHITE, BORDER, 12, 1.2)
    b += txt(M + 28, ly + 44, "Público-alvo e pré-requisitos", 20, INK, True)
    for i, (t, d) in enumerate([("Público-alvo", "Servidores da CMR, servidores de outros órgãos e público externo interessado em processo legislativo."),
                                ("Pré-requisitos", "Não há. Recomenda-se noção básica de organização do Poder Legislativo municipal.")]):
        b += txt(M + 28, ly + 84 + i * 62, t, 14, INK, True)
        b += para(M + 28, ly + 104 + i * 62, d, lw - 56, 13.5, MUTED, 19)
    ly += 214 + 24

    b += rect(M, ly, lw, 176, WHITE, BORDER, 12, 1.2)
    b += txt(M + 28, ly + 44, "Certificação", 20, INK, True)
    b += para(M + 28, ly + 76, "O certificado digital é emitido pela Escola do Legislativo após o lançamento "
                               "da frequência pelo gestor, exigida a presença mínima de 75%. O documento traz "
                               "código de autenticidade único e pode ser conferido na área pública de validação.",
              lw - 56, 13.5, MUTED, 21)
    b += link(M + 28, ly + 150, "Ir para a validação de certificados", 13.5, BLUE_D, True, True,
              to="17")
    ly += 176

    y = max(ly, ry) + 80
    s, y = footer_pub(y)
    b += s
    s, y = nota(y, W, ["RF 2", "RF 7", "RF 8"],
                ["RF 2 - Para eventos online/híbridos, o link é exibido na própria página de detalhes "
                 "(Opção 1) ou somente após a inscrição (Opção 2)? A tela está desenhada na Opção 2.",
                 "RF 2 - Como deve acontecer um curso online: transmissão em plataforma externa "
                 "(Meet/Teams/YouTube) ou ambiente próprio dentro do portal?"],
                "Aba 'O que você vai aprender' (Ementa) com botão de ação Inscrever-se, painel de vagas "
                "e botão de lista de espera desabilitado enquanto houver vaga.")
    b += s
    return "05-curso-detalhe-ementa", svg("05-curso-detalhe-ementa", W, y, b, WHITE)


@reg
def t06():
    b, c, y0, ly, lw, rx, rw, ry = _detalhe_base(1)
    b += rect(M, ly, lw, 330, WHITE, BORDER, 12, 1.2)
    b += txt(M + 28, ly + 46, "Sobre o professor / instrutor", 20, INK, True)
    b += avatar(M + 28, ly + 72, 92, "HV", NAVY_3)
    b += txt(M + 142, ly + 104, "Dra. Helena Vasconcelos", 20, INK, True)
    b += txt(M + 142, ly + 128, "Procuradora Legislativa · Mestre em Direito Público (UFPE)", 13.5, BLUE_D)
    s, _ = badges_row(M + 142, ly + 142, [("Processo Legislativo", "info"), ("Direito", "info"),
                                          ("12 turmas na Escola", "gold")], 11.5, 24)
    b += s
    b += para(M + 28, ly + 208, "Atua há 16 anos na Procuradoria da Câmara Municipal do Recife, com "
                                "experiência em assessoramento a comissões permanentes e elaboração de "
                                "pareceres sobre admissibilidade de proposições. É autora do Manual de "
                                "Técnica Legislativa publicado no acervo da Escola e ministra cursos de "
                                "formação continuada para servidores desde 2018.", lw - 56, 14, MUTED, 22)
    ly += 330 + 24

    b += rect(M, ly, lw, 198, WHITE, BORDER, 12, 1.2)
    b += txt(M + 28, ly + 44, "Outros cursos deste professor", 20, INK, True)
    for i, (t, d) in enumerate([("Introdução ao Direito Municipal", "Realizado em 03/2026 · 15h"),
                                ("Técnica de Redação de Proposições", "Realizado em 11/2025 · 8h")]):
        yy = ly + 74 + i * 58
        b += rect(M + 28, yy, lw - 56, 50, "#F7FAFC", BORDER, 8, 1)
        b += icon("book", M + 44, yy + 15, 19, BLUE, 1.7)
        b += txt(M + 74, yy + 22, t, 14, INK, True)
        b += txt(M + 74, yy + 40, d, 12, MUTED)
        b += icon("chev-r", M + lw - 56, yy + 16, 16, FAINT, 1.8)
    ly += 198

    y = max(ly, ry) + 80
    s, y = footer_pub(y)
    b += s
    s, y = nota(y, W, ["RF 2", "RF 16"], None,
                "Aba 'Sobre o Professor/Instrutor' com biografia resumida, exigida no RF 2. Os dados "
                "vêm do cadastro de professores mantido pelo gestor (RF 16).")
    b += s
    return "06-curso-detalhe-professor", svg("06-curso-detalhe-professor", W, y, b, WHITE)


@reg
def t07():
    b, c, y0, ly, lw, rx, rw, ry = _detalhe_base(2)
    b += rect(M, ly, lw, 316, WHITE, BORDER, 12, 1.2)
    b += txt(M + 28, ly + 46, "Turmas disponíveis", 20, INK, True)
    b += txt(M + 28, ly + 68, "Escolha a turma no momento da inscrição.", 13, MUTED)
    s, _ = table(M + 28, ly + 88, lw - 56, [
        ("Turma", 190, "start"), ("Dias e horário", 250, "start"),
        ("Vagas", 110, "middle"), ("Situação", 156, "end")], [
        [("two", "Turma A - Manhã", "14 e 15/09"), "Seg e Ter · 09h às 12h", "6/30",
         ("badge", "Disponível", "abertas")],
        [("two", "Turma B - Noite", "14 e 15/09"), "Seg e Ter · 19h às 22h", "18/30",
         ("badge", "Disponível", "abertas")],
        [("two", "Turma C - Online", "16/09"), "Qua · 14h às 18h", "35/35",
         ("badge", "Esgotada", "esgotado")]], 58)
    b += s
    ly += 316 + 24

    b += rect(M, ly, lw, 388, WHITE, BORDER, 12, 1.2)
    b += txt(M + 28, ly + 46, "Cronograma das aulas", 20, INK, True)
    prog = [("Encontro 1", "14/09/2026 · 19h às 22h",
             "Organização da Câmara, espécies de proposições e admissibilidade", "3h"),
            ("Encontro 2", "15/09/2026 · 19h às 22h",
             "Comissões, pareceres, ordem do dia e processo de votação", "3h"),
            ("Atividade final", "até 20/09/2026 · a distância",
             "Estudo de caso avaliativo entregue pelo ambiente do portal", "2h")]
    for i, (t, d, desc, ch) in enumerate(prog):
        yy = ly + 84 + i * 96
        b += circ(M + 44, yy + 20, 15, BLUE_L)
        b += ctext(M + 44, yy + 20, str(i + 1), 13.5, BLUE_D, True)
        if i < len(prog) - 1:
            b += line(M + 44, yy + 36, M + 44, yy + 78, BORDER2, 1.6)
        b += txt(M + 76, yy + 10, t, 15.5, INK, True)
        b += badge(M + 76 + tw(t, 15.5, True) + 12, yy - 4, ch, "gold", 11)[0]
        b += txt(M + 76, yy + 32, d, 13, BLUE_D, True)
        b += para(M + 76, yy + 54, desc, lw - 140, 13, MUTED, 19)
    ly += 388

    y = max(ly, ry) + 80
    s, y = footer_pub(y)
    b += s
    s, y = nota(y, W, ["RF 2", "RF 7", "RF 13"],
                ["Um curso pode ter várias turmas? Se sim, como fica a divulgação dos dias e horários "
                 "de cada turma? A tela está desenhada com múltiplas turmas por curso, cada uma com "
                 "dias, horário e controle próprio de vagas.",
                 "RF 7 - O sistema pode permitir que o mesmo aluno se inscreva em mais de uma turma "
                 "do mesmo curso?"],
                "Aba 'Cronograma' do RF 2 somada à divulgação de turmas (RF 13).")
    b += s
    return "07-curso-detalhe-cronograma-turmas", svg("07-curso-detalhe-cronograma-turmas", W, y, b, WHITE)


# ================================================================ 08-09 NOTICIAS
@reg
def t08():
    b = header_pub("Noticias")
    s, y = page_hero(HEAD_H, "Notícias",
                     "Acompanhe as ações, parcerias e resultados da Escola do Legislativo",
                     ["Home", "Notícias"], 170)
    b += s
    y += 44
    s, cx = pills(M, y, ["Todas", "Cursos", "Parcerias", "Institucional", "Acervo", "Agenda"], 0)
    b += s
    b += rect(W - M - 300, y, 300, 38, WHITE, BORDER2, 19, 1.3)
    b += icon("search", W - M - 288, y + 10, 17, FAINT, 1.7)
    b += txt(W - M - 262, y + 24, "Buscar notícia", 13, FAINT)
    y += 38 + 36

    # destaque
    b += rect(M, y, CW, 320, WHITE, BORDER, 12, 1.2)
    b += img_ph(M, y, 560, 320, 12, TONES[0])
    b += rect(M + 550, y, 10, 320, TONES[0])
    b += badge(M + 596, y + 36, "DESTAQUE DA SEMANA", "gold", 11)[0]
    b += icon("calendar", M + 596, y + 74, 15, FAINT, 1.6)
    b += txt(M + 618, y + 86, "12/08/2026 · Parcerias", 12.5, MUTED)
    b += para(M + 596, y + 130, NOTICIAS[0][0], 560, 26, INK, 32, True)
    b += para(M + 596, y + 202, "O acordo de cooperação técnica assinado nesta semana permite o "
                                "intercâmbio de cursos, material didático e metodologias entre a Escola "
                                "do Legislativo da CMR e a Assembleia Legislativa de Minas Gerais.",
              560, 14, MUTED, 21)
    b += btn(M + 596, y + 258, 170, 44, "Ler notícia", "primary", 14, to="09")
    y += 320 + 28
    for i, nt in enumerate(NOTICIAS[1:]):
        cx0 = M + (i % 3) * (384 + 24)
        cy = y + (i // 3) * (336 + 24)
        b += card_noticia(cx0, cy, nt, to="09")
    y += 2 * (336 + 24) - 24 + 36
    s, y = pagination(M, y, CW, "64")
    b += s
    y += 80
    s, y = footer_pub(y)
    b += s
    s, y = nota(y, W, ["RF 3", "RF 17"], None,
                "Feed completo de notícias com filtro por categoria e busca. As notícias são "
                "cadastradas pelo Gestor/Admin no módulo de gestão de conteúdo (RF 17).")
    b += s
    return "08-noticias-lista", svg("08-noticias-lista", W, y, b, WHITE)


@reg
def t09():
    b = header_pub("Noticias")
    y = HEAD_H
    b += rect(0, y, W, 120, NAVY)
    b += crumb_light(M, y + 44, ["Home", "Notícias", "Escola firma parceria com a ALMG"])
    b += btn(W - M - 150, y + 34, 150, 42, "Voltar", "dark", 13.5, "arrow-l", to="08")
    y += 120
    lw = 800
    rx = M + lw + 40
    rw = CW - lw - 40
    b += rect(0, y, W, 1, BORDER)
    ly = y + 48
    b += badge(M, ly, "Parcerias", "info", 12, 26)[0]
    b += txt(M + 118, ly + 18, "Publicado em 12/08/2026 às 10h32 · Assessoria da Escola do Legislativo",
             12.5, MUTED)
    b += para(M, ly + 74, "Escola do Legislativo firma parceria com a Escola do Legislativo de Minas Gerais",
              lw, 34, INK, 42, True)
    ly += 74 + 90
    b += img_ph(M, ly, lw, 380, 10, TONES[0], "FOTO DA MATÉRIA")
    b += txt(M, ly + 400, "Assinatura do acordo na sede da CMR · Foto: Comunicação/CMR", 12, FAINT)
    ly += 424
    ps = ["A Câmara Municipal do Recife, por meio da Escola do Legislativo, assinou nesta semana acordo "
          "de cooperação técnica com a Escola do Legislativo da Assembleia Legislativa de Minas Gerais.",
          "O instrumento prevê o intercâmbio de cursos, material didático e metodologias de capacitação "
          "continuada, além da possibilidade de oferta conjunta de turmas a distância para servidores "
          "das duas casas legislativas.",
          "Segundo a coordenação da Escola, a primeira ação conjunta será a oferta do curso de Processo "
          "Legislativo Municipal em formato híbrido, com vagas reservadas ao público externo.",
          "O acordo tem vigência de 24 meses e está publicado, na íntegra, na página de Legislação e "
          "Transparência do portal, junto aos demais instrumentos jurídicos formalizados pela Escola."]
    for p in ps:
        b += para(M, ly, p, lw, 15.5, TXT, 26)
        ly += para_h(p, lw, 15.5, 26) + 18
    ly += 10
    b += rect(M, ly, lw, 88, BLUE_L, "#A9CBE8", 10, 1.2)
    b += icon("link", M + 24, ly + 32, 20, BLUE_D, 1.8)
    b += txt(M + 56, ly + 36, "Documento relacionado", 14, BLUE_D, True)
    b += txt(M + 56, ly + 58, "Acordo de Cooperação Técnica nº 04/2026 (PDF · 620 KB)", 13, TXT)
    b += btn(M + lw - 130, ly + 24, 110, 40, "Baixar", "secondary", 13)
    ly += 88 + 34
    b += txt(M, ly, "Assuntos:", 13, MUTED, True)
    s, _ = badges_row(M + 76, ly - 16, [("Parcerias", "neutro"), ("ALMG", "neutro"),
                                        ("Cooperação técnica", "neutro"), ("Capacitação", "neutro")], 12, 26)
    b += s
    ly += 50

    # lateral
    ry = y + 48
    b += rect(rx, ry, rw, 300, WHITE, BORDER, 12, 1.2)
    b += txt(rx + 24, ry + 42, "Outras notícias", 17, INK, True)
    for i, nt in enumerate(NOTICIAS[1:4]):
        yy = ry + 68 + i * 76
        b += line(rx + 24, yy, rx + rw - 24, yy, "#EDF1F6", 1.2)
        b += txt(rx + 24, yy + 22, nt[2], 11.5, BLUE_D, True)
        b += para(rx + 24, yy + 42, nt[0], rw - 48, 13, TXT, 18, maxlines=2)
    ry += 300 + 20
    b += rect(rx, ry, rw, 210, NAVY, None, 12)
    b += txt(rx + 24, ry + 44, "Receba a agenda", 18, WHITE, True)
    b += para(rx + 24, ry + 68, "Cadastre-se no portal e seja avisado por e-mail sobre novas turmas.",
              rw - 48, 13, "#B7C7D6", 19)
    b += rect(rx + 24, ry + 118, rw - 48, 44, WHITE, None, 6)
    b += txt(rx + 38, ry + 145, "seu@email.com", 13.5, FAINT)
    b += btn(rx + 24, ry + 172, rw - 48, 44, "Quero receber a agenda", "gold", 13.5)
    ry += 210
    y = max(ly, ry) + 70
    s, y = footer_pub(y)
    b += s
    s, y = nota(y, W, ["RF 3", "RF 17"], None,
                "Página de leitura da notícia, com documento relacionado (instrumento jurídico) e "
                "notícias correlatas.")
    b += s
    return "09-noticia-detalhe", svg("09-noticia-detalhe", W, y, b, WHITE)
