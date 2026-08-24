# -*- coding: utf-8 -*-
"""Telas 29-38: Area do Aluno e inscricoes (RF 7, RF 8, RF 9)."""
from blocks import *

TELAS = []
ALUNO = dict(nome="Maria Silva", iniciais="MS", papel="Área do Aluno")
ABAS = ["Painel", "Meus cursos", "Meus certificados", "Meus dados"]


def reg(fn):
    TELAS.append(fn)
    return fn


def shell(titulo, sub, aba, crumbs=None):
    b = header_pub(None, ALUNO)
    y = HEAD_H
    b += rect(0, y, W, 168, NAVY)
    b += crumb_light(M, y + 40, crumbs or ["Home", "Área do Aluno"])
    b += avatar(M, y + 62, 62, "MS", NAVY_3)
    b += txt(M + 80, y + 92, titulo, 30, WHITE, True)
    b += txt(M + 80, y + 120, sub, 14, "#B7C7D6")
    b += btn(W - M - 150, y + 74, 150, 44, "Sair da conta", "dark", 13.5, "logout", to="01")
    y += 168
    b += rect(0, y, W, 58, WHITE)
    b += line(0, y + 58, W, y + 58, BORDER, 1.2)
    cx = M
    abas_to = ["29", "34", "37", "38"]
    for i, t in enumerate(ABAS):
        on = i == aba
        wd = tw(t, 14.5, on)
        if not on:
            hot(cx - 10, y + 14, wd + 20, 34, abas_to[i], t)
        b += txt(cx, y + 36, t, 14.5, INK if on else MUTED, on)
        if on:
            b += rect(cx, y + 47, wd, 3.5, GOLD, None, 2)
        cx += wd + 36
    return b, y + 58


# ================================================================ 29 PAINEL
@reg
def t29():
    b, y = shell("Olá, Maria Silva", "Servidora da CMR · matrícula 20.451-7 · CPF 123.***.***-89", 0)
    y += 40
    stats = [("Cursos em andamento", "2", "próximo em 14/09", "book", BLUE, BLUE_L),
             ("Inscrições confirmadas", "3", "1 aguardando início", "check", GREEN, GREEN_L),
             ("Na lista de espera", "1", "posição 3 na fila", "clock", AMBER, AMBER_L),
             ("Certificados emitidos", "7", "todos disponíveis", "cert", PURPLE, PURPLE_L)]
    sw = (CW - 3 * 24) / 4.0
    for i, (l, v, s2, ic, tn, tl) in enumerate(stats):
        b += stat(M + i * (sw + 24), y, sw, 168, l, v, s2, ic, tn, tl)
    y += 168 + 40

    lw = 762
    rx = M + lw + 24
    rw = CW - lw - 24

    b += rect(M, y, lw, 344, WHITE, BORDER, 12, 1.2)
    b += txt(M + 28, y + 46, "Próximas atividades", 20, INK, True)
    b += link(M + lw - 28 - tw("Ver meus cursos", 13), y + 46, "Ver meus cursos", 13, BLUE_D,
              to="34")
    ativ = [("14", "SET", "Processo Legislativo Municipal", "Turma B - Noite · 19h às 22h · Online",
             "Confirmada", "abertas"),
            ("22", "SET", "Ética e Conduta no Serviço Público", "Turma única · 14h às 18h · Presencial",
             "Confirmada", "abertas"),
            ("05", "OUT", "Tecnologia e Governo Digital", "Turma A · 09h às 12h · Híbrido",
             "Lista de espera", "breve")]
    for i, (d, mes, t, s2, st, k) in enumerate(ativ):
        yy = y + 80 + i * 84
        b += rect(M + 28, yy, 62, 66, BLUE_L, None, 8)
        b += ctext(M + 59, yy + 24, d, 22, BLUE_D, True)
        b += ctext(M + 59, yy + 48, mes, 11.5, BLUE_D, True)
        b += txt(M + 108, yy + 24, t, 16, INK, True)
        b += txt(M + 108, yy + 46, s2, 13, MUTED)
        bw = badge_w(st)
        b += badge(M + lw - 28 - bw, yy + 20, st, k)[0]
        b += link(M + lw - 28 - tw("Acessar", 12.5), yy + 58, "Acessar", 12.5, BLUE_D, to="36")
    y2 = y + 344 + 24
    b += rect(M, y2, lw, 216, WHITE, BORDER, 12, 1.2)
    b += txt(M + 28, y2 + 46, "Certificados recentes", 20, INK, True)
    for i, (t, d, cod) in enumerate([("Controle Interno e Prestação de Contas", "13/05/2026 · 8h",
                                      "ELCMR-2026-K2M4-8N1P-5Q7R"),
                                     ("Audiências Públicas e Participação Cidadã", "08/04/2026 · 4h",
                                      "ELCMR-2026-B5T8-2J9L-4W3X")]):
        yy = y2 + 74 + i * 66
        b += icon("cert", M + 28, yy, 22, GREEN, 1.8)
        b += txt(M + 62, yy + 12, t, 14.5, INK, True)
        b += txt(M + 62, yy + 32, d + " · Código " + cod, 12, MUTED)
        b += btn(M + lw - 28 - 116, yy - 4, 116, 36, "Baixar PDF", "secondary", 12.5, "download",
                 to="37")
    ly = y2 + 216

    ry = y
    b += rect(rx, ry, rw, 236, NAVY, None, 12)
    b += txt(rx + 26, ry + 48, "Fila de espera", 18, WHITE, True)
    b += badge(rx + rw - 26 - badge_w("Posição 3"), ry + 32, "Posição 3", "solid-amber")[0]
    b += para(rx + 26, ry + 78, "Tecnologia e Governo Digital", rw - 52, 15, GOLD, 20, True)
    b += para(rx + 26, ry + 108, "Você será avisado por e-mail assim que uma vaga for liberada e terá "
                                 "24 horas para confirmar.", rw - 52, 12.5, "#B7C7D6", 18)
    b += btn(rx + 26, ry + 168, rw - 52, 42, "Sair da lista de espera", "ghost", 13, to="34")
    ry += 236 + 20
    b += rect(rx, ry, rw, 250, WHITE, BORDER, 12, 1.2)
    b += txt(rx + 26, ry + 46, "Meus dados", 18, INK, True)
    for i, (l, v) in enumerate([("E-mail", "maria.santos@email.com"), ("Telefone", "(81) 99999-0000"),
                                ("Vínculo", "Servidora da CMR")]):
        b += txt(rx + 26, ry + 78 + i * 46, l, 11.5, MUTED, True)
        b += para(rx + 26, ry + 98 + i * 46, v, rw - 52, 13.5, INK, 17, maxlines=1)
    b += btn(rx + 26, ry + 196, rw - 52, 42, "Atualizar meus dados", "secondary", 13, to="38")
    ry += 250 + 20
    b += rect(rx, ry, rw, 176, GOLD_L, "#E7D2A4", 12, 1.2)
    b += icon("cert", rx + 26, ry + 30, 22, "#8A6414", 1.8)
    b += txt(rx + 26, ry + 78, "Validar um certificado", 16, "#8A6414", True)
    b += para(rx + 26, ry + 100, "Confira a autenticidade de qualquer certificado da Escola.",
              rw - 52, 12.5, "#8A6414", 18)
    b += btn(rx + 26, ry + 122, rw - 52, 40, "Ir para validação", "gold", 13, to="17")
    ry += 176
    y = max(ly, ry) + 76
    s, y = footer_pub(y)
    b += s
    s, y = nota(y, W, ["ÁREA DO ALUNO", "RF 7", "RF 8", "RF 9"], None,
                "Painel inicial da Área do Aluno com Meus Cursos, Meus Certificados e Atualizar meus "
                "dados, conforme a estrutura definida na seção 2 do documento.")
    b += s
    return "29-aluno-painel", svg("29-aluno-painel", W, y, b, WHITE)


# ================================================================ 30 SELECIONAR TURMA
def _resumo_inscricao(b, rx, ry, rw, turma="Turma B - Noite", extra=None):
    b += rect(rx, ry, rw, 460, WHITE, BORDER, 12, 1.4)
    b += rect(rx, ry, rw, 6, BLUE, None, 12)
    b += rect(rx, ry + 3, rw, 3, BLUE)
    b += txt(rx + 26, ry + 48, "Resumo da inscrição", 18, INK, True)
    b += line(rx + 26, ry + 66, rx + rw - 26, ry + 66, "#EDF1F6", 1.2)
    itens = [("Curso", "Processo Legislativo Municipal"), ("Turma selecionada", turma),
             ("Datas", "14 e 15/09/2026"), ("Horário", "19h às 22h"),
             ("Carga horária", "8 horas"), ("Formato", "Online - ao vivo"),
             ("Aluno", "Maria Silva dos Santos"), ("Investimento", "Gratuito")]
    for i, (l, v) in enumerate(itens):
        yy = ry + 92 + i * 40
        b += txt(rx + 26, yy, l, 12, MUTED)
        b += txt(rx + rw - 26, yy, v, 12.5, INK, True, anchor="end")
    b += line(rx + 26, ry + 414, rx + rw - 26, ry + 414, "#EDF1F6", 1.2)
    return b, ry + 460


@reg
def t30():
    b, y = shell("Inscrição em curso", "Confira os dados e escolha a turma desejada", 1,
                 ["Home", "Cursos e Eventos", "Processo Legislativo Municipal", "Inscrição"])
    y += 40
    lw = 762
    rx = M + lw + 24
    rw = CW - lw - 24

    s, ny = alert(M, y, lw, "Você está logada como Maria Silva dos Santos",
                  "Servidora da Câmara Municipal do Recife · matrícula 20.451-7 · CPF 123.***.***-89. "
                  "Se algum dado estiver incorreto, atualize antes de confirmar.", "ok")
    b += s
    ly = ny + 24
    b += rect(M, ly, lw, 452, WHITE, BORDER, 12, 1.2)
    b += txt(M + 28, ly + 48, "Escolha a turma", 21, INK, True)
    b += txt(M + 28, ly + 72, "O sistema verifica a disponibilidade de vagas em cada turma.", 13, MUTED)
    turmas = [("Turma A - Manhã", "14 e 15/09/2026 · 09h às 12h · Online", "6 de 30 vagas ocupadas",
               "Disponível", "abertas", False, 20),
              ("Turma B - Noite", "14 e 15/09/2026 · 19h às 22h · Online", "18 de 30 vagas ocupadas",
               "Disponível", "abertas", True, 60),
              ("Turma C - Tarde", "16/09/2026 · 14h às 18h · Presencial", "35 de 35 vagas ocupadas",
               "Esgotada", "esgotado", False, 100)]
    for i, (t, d, v, st, k, sel, pct) in enumerate(turmas):
        yy = ly + 100 + i * 108
        cheia = st == "Esgotada"
        b += rect(M + 28, yy, lw - 56, 92, BLUE_L if sel else ("#FAFBFC" if cheia else WHITE),
                  BLUE if sel else BORDER2, 10, 1.6 if sel else 1.2)
        hot(M + 28, yy, lw - 56, 92, ("31" if cheia else None), t)
        b += radio(M + 48, yy + 36, "", sel)
        b += txt(M + 84, yy + 32, t, 16, FAINT if cheia else INK, True)
        b += txt(M + 84, yy + 54, d, 13, MUTED)
        b += txt(M + 84, yy + 76, v, 12, MUTED)
        bw = badge_w(st)
        b += badge(M + lw - 84 - bw, yy + 20, st, k)[0]
        b += rect(M + lw - 84 - 120, yy + 58, 120, 7, "#E6ECF2", None, 4)
        b += rect(M + lw - 84 - 120, yy + 58, 120 * pct / 100.0, 7,
                  RED if pct >= 100 else (AMBER if pct >= 60 else GREEN), None, 4)
    ly += 452 + 24
    s, ly = alert(M, ly, lw, "Verificação automática do sistema",
                  "Ao confirmar, o portal checa se ainda há vaga na turma escolhida e se você já não "
                  "possui inscrição ativa neste curso. Havendo vaga, o registro é gravado com status "
                  "'Confirmada'.", "info")
    b += s

    ry = y
    b, ry = _resumo_inscricao(b, rx, ry, rw)
    ry += 20
    b += btn(rx, ry, rw, 56, "Confirmar inscrição", "primary", 16, hot=True, to="32")
    ry += 68
    b += btn(rx, ry, rw, 48, "Cancelar e voltar ao curso", "ghost", 14, to="05")
    ry += 68
    b += rect(rx, ry, rw, 176, "#F7FAFC", BORDER, 12, 1.2)
    b += icon("info", rx + 24, ry + 26, 18, MUTED, 1.8)
    b += txt(rx + 50, ry + 40, "Antes de confirmar", 14, INK, True)
    for i, t in enumerate(["A vaga só é garantida após a confirmação.",
                           "Você pode cancelar a inscrição pela Área do Aluno.",
                           "O certificado exige 75% de frequência."]):
        b += circ(rx + 30, ry + 74 + i * 32, 3, GOLD)
        b += para(rx + 44, ry + 78 + i * 32, t, rw - 74, 12.5, MUTED, 17, maxlines=2)
    ry += 176
    y = max(ly, ry) + 76
    s, y = footer_pub(y)
    b += s
    s, y = nota(y, W, ["RF 7", "RF 13"],
                ["RF 7 - O sistema pode permitir que o mesmo aluno se inscreva em mais de uma turma do "
                 "mesmo curso? Hoje a tela permite apenas uma seleção."],
                "RF 7: usuário logado seleciona a turma, o sistema verifica Vagas Ocupadas < Vagas "
                "Totais e se o aluno já não está inscrito, e grava o registro com status 'Confirmada'.")
    b += s
    return "30-aluno-inscricao-selecionar-turma", svg("30-aluno-inscricao-selecionar-turma", W, y, b, WHITE)


# ================================================================ 31 SEM VAGA
@reg
def t31():
    b, y = shell("Inscrição em curso", "A turma escolhida não tem mais vagas", 1,
                 ["Home", "Cursos e Eventos", "Processo Legislativo Municipal", "Inscrição"])
    y += 40
    lw = 762
    rx = M + lw + 24
    rw = CW - lw - 24
    s, ly = alert(M, y, lw, "A Turma C - Tarde está esgotada",
                  "As 35 vagas desta turma já foram preenchidas enquanto você navegava. Veja abaixo as "
                  "alternativas disponíveis para este mesmo curso.", "warn")
    b += s
    ly += 24
    b += rect(M, ly, lw, 250, GREEN_L, "#A9DCC6", 12, 1.4)
    b += icon("check", M + 28, ly + 28, 22, GREEN, 2)
    b += txt(M + 60, ly + 46, "Há vaga em outra turma deste curso", 20, GREEN, True)
    b += para(M + 28, ly + 76, "O sistema localizou turmas do mesmo curso com vagas disponíveis. "
                               "Selecione uma delas para continuar sua inscrição agora.",
              lw - 56, 13.5, TXT, 20)
    for i, (t, d, v) in enumerate([("Turma A - Manhã", "14 e 15/09 · 09h às 12h · Online", "24 vagas livres"),
                                   ("Turma B - Noite", "14 e 15/09 · 19h às 22h · Online", "12 vagas livres")]):
        x = M + 28 + i * ((lw - 76) / 2.0 + 20)
        b += rect(x, ly + 128, (lw - 76) / 2.0, 96, WHITE, "#A9DCC6", 10, 1.2)
        b += txt(x + 20, ly + 156, t, 15.5, INK, True)
        b += txt(x + 20, ly + 178, d, 12.5, MUTED)
        b += badge(x + 20, ly + 190, v, "abertas", 11.5)[0]
        b += btn(x + (lw - 76) / 2.0 - 116, ly + 182, 96, 34, "Escolher", "success", 12.5,
                 to="30")
    ly += 250 + 24
    b += rect(M, ly, lw, 236, WHITE, BORDER, 12, 1.2)
    b += txt(M + 28, ly + 48, "Ou entre na lista de espera da Turma C", 20, INK, True)
    b += para(M + 28, ly + 78, "Se você só pode participar da Turma C - Tarde, entre na lista de espera. "
                               "O processo é o mesmo da inscrição, porém o registro fica com status "
                               "'Em fila de espera' e respeita a ordem de chegada.", lw - 56, 13.5, MUTED, 20)
    b += rect(M + 28, ly + 146, lw - 56, 62, AMBER_L, "#EBCE95", 8, 1.2)
    b += icon("clock", M + 48, ly + 164, 19, AMBER, 1.8)
    b += txt(M + 76, ly + 172, "Você entraria na posição 4 da fila", 14, AMBER, True)
    b += txt(M + 76, ly + 192, "3 pessoas já aguardam vaga nesta turma.", 12.5, TXT)
    b += btn(M + lw - 28 - 220, ly + 158, 200, 40, "Entrar na lista de espera", "gold", 13,
             to="33")
    ly += 236

    ry = y
    b, ry = _resumo_inscricao(b, rx, ry, rw, "Turma C - Tarde (esgotada)")
    ry += 20
    b += btn(rx, ry, rw, 56, "Confirmar inscrição", "disabled", 16)
    b += ctext(rx + rw / 2.0, ry + 78, "Selecione uma turma com vaga para continuar", 12.5, MUTED)
    ry += 110
    y = max(ly, ry) + 76
    s, y = footer_pub(y)
    b += s
    s, y = nota(y, W, ["RF 7", "RF 8"], None,
                "RF 7: quando não há vaga na turma escolhida, o sistema exibe as turmas do mesmo curso "
                "que possuem vaga; se nenhuma turma tiver vaga, habilita o botão de lista de espera (RF 8).")
    b += s
    return "31-aluno-inscricao-sem-vaga-outra-turma", svg("31-aluno-inscricao-sem-vaga-outra-turma", W, y, b, WHITE)


# ================================================================ 32 CONFIRMADA
@reg
def t32():
    b = header_pub(None, ALUNO)
    y = HEAD_H
    b += rect(0, y, W, 110, NAVY)
    y += 110 + 56
    cw2 = 900
    cx = (W - cw2) / 2.0
    b += rect(cx, y, cw2, 660, WHITE, BORDER, 14, 1.4)
    b += rect(cx, y, cw2, 8, GREEN, None, 14)
    b += rect(cx, y + 4, cw2, 4, GREEN)
    b += circ(cx + cw2 / 2.0, y + 92, 42, GREEN_L)
    b += path("M%s %s l13 14 L%s %s" % (n(cx + cw2 / 2.0 - 19), n(y + 92), n(cx + cw2 / 2.0 + 21), n(y + 77)),
              None, GREEN, 5)
    b += ctext(cx + cw2 / 2.0, y + 168, "Inscrição confirmada!", 30, INK, True)
    b += ctext(cx + cw2 / 2.0, y + 202, "Sua vaga está garantida. Enviamos a confirmação para maria.santos@email.com",
               14.5, MUTED)
    b += rect(cx + 48, y + 236, cw2 - 96, 168, "#F7FAFC", BORDER, 10, 1.2)
    dados = [("Curso", "Processo Legislativo Municipal"), ("Turma", "Turma B - Noite"),
             ("Datas", "14 e 15/09/2026 · 19h às 22h"), ("Formato", "Online - ao vivo"),
             ("Protocolo", "INS-2026-004812"), ("Situação", "Confirmada")]
    for i, (l, v) in enumerate(dados):
        x = cx + 76 + (i % 3) * ((cw2 - 152) / 3.0)
        yy = y + 280 + (i // 3) * 72
        b += txt(x, yy, l, 11.5, MUTED, True)
        if l == "Situação":
            b += badge(x, yy + 10, v, "abertas", 12, 26)[0]
        else:
            b += para(x, yy + 24, v, (cw2 - 152) / 3.0 - 20, 14.5, INK, 18, True, maxlines=2)
    b += rect(cx + 48, y + 424, cw2 - 96, 84, AMBER_L, "#EBCE95", 10, 1.2)
    b += icon("lock", cx + 72, y + 452, 20, AMBER, 1.8)
    b += txt(cx + 102, y + 456, "Link de acesso ao curso online", 15, AMBER, True)
    b += txt(cx + 102, y + 480, "Liberado nesta página e na Área do Aluno a partir de 13/09/2026, "
                                "24h antes do início.", 13, TXT)
    b += btn(cx + 48, y + 536, 260, 52, "Ir para Meus Cursos", "primary", 15, hot=True, to="34")
    b += btn(cx + 322, y + 536, 230, 52, "Adicionar à agenda", "secondary", 14, "calendar")
    b += btn(cx + 566, y + 536, 230, 52, "Ver outros cursos", "ghost", 14, to="02")
    b += ctext(cx + cw2 / 2.0, y + 622, "Precisa cancelar? Você pode fazer isso a qualquer momento em Meus Cursos.",
               12.5, MUTED)
    y += 660 + 80
    s, y = footer_pub(y)
    b += s
    s, y = nota(y, W, ["RF 7"], None,
                "Registro gravado na tabela de inscrições com status 'Confirmada', conforme a ação "
                "final descrita no RF 7.")
    b += s
    return "32-aluno-inscricao-confirmada", svg("32-aluno-inscricao-confirmada", W, y, b, WHITE)


# ================================================================ 33 LISTA DE ESPERA
@reg
def t33():
    b = header_pub(None, ALUNO)
    y = HEAD_H
    b += rect(0, y, W, 110, NAVY)
    y += 110 + 56
    cw2 = 900
    cx = (W - cw2) / 2.0
    b += rect(cx, y, cw2, 622, WHITE, BORDER, 14, 1.4)
    b += rect(cx, y, cw2, 8, AMBER, None, 14)
    b += rect(cx, y + 4, cw2, 4, AMBER)
    b += circ(cx + cw2 / 2.0, y + 92, 42, AMBER_L)
    b += icon_c("clock", cx + cw2 / 2.0, y + 92, 40, AMBER, 2.2)
    b += ctext(cx + cw2 / 2.0, y + 168, "Você entrou na lista de espera", 30, INK, True)
    b += ctext(cx + cw2 / 2.0, y + 202, "Processo Legislativo Municipal · Turma C - Tarde", 15, MUTED)
    b += rect(cx + 48, y + 234, cw2 - 96, 128, AMBER_L, "#EBCE95", 10, 1.2)
    b += ctext(cx + 160, y + 288, "4ª", 42, AMBER, True)
    b += ctext(cx + 160, y + 322, "sua posição na fila", 12.5, TXT)
    b += line(cx + 272, y + 258, cx + 272, y + 338, "#EBCE95", 1.4)
    b += txt(cx + 306, y + 274, "Como funciona a fila", 15, AMBER, True)
    b += para(cx + 306, y + 300, "A ordem de chegada é respeitada. Quando alguém cancelar a inscrição, "
                                 "a vaga é oferecida ao próximo da fila.", cw2 - 400, 13, TXT, 19)
    b += rect(cx + 48, y + 386, cw2 - 96, 106, "#F7FAFC", BORDER, 10, 1.2)
    b += txt(cx + 76, y + 418, "Situação da sua inscrição", 12, MUTED, True)
    b += badge(cx + 76, y + 430, "Em fila de espera", "breve", 13, 30)[0]
    b += txt(cx + 340, y + 418, "Protocolo", 12, MUTED, True)
    b += txt(cx + 340, y + 446, "FIL-2026-000317", 15, INK, True)
    b += txt(cx + 600, y + 418, "Entrada na fila", 12, MUTED, True)
    b += txt(cx + 600, y + 446, "19/08/2026 às 14h07", 15, INK, True)
    b += btn(cx + 48, y + 516, 260, 52, "Ir para Meus Cursos", "primary", 15, to="34")
    b += btn(cx + 322, y + 516, 240, 52, "Ver outras turmas", "secondary", 14, to="07")
    b += ctext(cx + cw2 / 2.0, y + 586, "Você receberá um e-mail assim que uma vaga for liberada.", 12.5, MUTED)
    y += 622 + 80
    s, y = footer_pub(y)
    b += s
    s, y = nota(y, W, ["RF 8"],
                ["RF 10 - Quando surgir vaga, o sistema avisa automaticamente o próximo da fila por "
                 "e-mail dando 24h para assumir (Opção 1) ou o contato é feito manualmente pela equipe "
                 "da Escola (Opção 2)? O texto desta tela depende dessa definição."],
                "RF 8: mesmo fluxo da inscrição, porém com status 'Em fila de espera', respeitando a "
                "ordem de cada aluno na fila.")
    b += s
    return "33-aluno-lista-espera-confirmada", svg("33-aluno-lista-espera-confirmada", W, y, b, WHITE)


# ================================================================ 34 MEUS CURSOS
def _meus_cursos(nome, modal_on, rfs, dec, obs):
    b, y = shell("Meus cursos", "Inscrições confirmadas, em fila de espera e concluídas", 1)
    y += 40
    s, cxx = pills(M, y, ["Todos (11)", "Em andamento (2)", "Confirmados (3)", "Fila de espera (1)",
                          "Concluídos (5)"], 0)
    b += s
    b += rect(W - M - 260, y, 260, 38, WHITE, BORDER2, 19, 1.3)
    b += icon("search", W - M - 248, y + 10, 17, FAINT, 1.7)
    b += txt(W - M - 222, y + 24, "Buscar curso", 13, FAINT)
    y += 38 + 30
    s, y = table(M, y, CW, [
        ("Curso / turma", 400, "start"), ("Datas", 190, "start"), ("Formato", 130, "middle"),
        ("Situação", 170, "middle"), ("Ações", 310, "end")], [
        [("two", "Processo Legislativo Municipal", "Turma B - Noite · 19h às 22h"), "14 e 15/09/2026",
         "Online", ("badge", "Confirmada", "abertas"),
         ("btns", [("Acessar curso", "primary", "36"), ("Cancelar", "danger", "35")])],
        [("two", "Ética e Conduta no Serviço Público", "Turma única · 14h às 18h"), "22 a 24/09/2026",
         "Presencial", ("badge", "Confirmada", "abertas"),
         ("btns", [("Detalhes", "secondary", "05"), ("Cancelar", "danger", "35")])],
        [("two", "Tecnologia e Governo Digital", "Turma C - Tarde · 09h às 12h"), "05 e 06/10/2026",
         "Híbrido", ("badge", "Em fila de espera", "breve"),
         ("btns", [("Ver posição", "secondary"), ("Sair da fila", "ghost")])],
        [("two", "LGPD na Administração Pública", "Turma A · 09h às 17h"), "17/11/2026",
         "Híbrido", ("badge", "Confirmada", "abertas"),
         ("btns", [("Detalhes", "secondary"), ("Cancelar", "danger")])],
        [("two", "Controle Interno e Prestação de Contas", "Turma única · 14h às 18h"), "12 e 13/05/2026",
         "Presencial", ("badge", "Concluído", "encerradas"),
         ("btns", [("Certificado", "success", "37"), ("Materiais", "ghost", "36")])],
        [("two", "Audiências Públicas e Participação Cidadã", "Turma B · 09h às 13h"), "08/04/2026",
         "Online", ("badge", "Concluído", "encerradas"),
         ("btns", [("Certificado", "success"), ("Materiais", "ghost")])],
        [("two", "Introdução ao Direito Municipal", "Turma A · 19h às 22h"), "03 a 07/03/2026",
         "Presencial", ("badge", "Cancelada por mim", "esgotado"),
         ("btns", [("Ver curso", "ghost")])]], 70)
    b += s
    y += 24
    s, y = pagination(M, y, CW, "11")
    b += s
    y += 40
    s, y = alert(M, y, CW, "Sobre o cancelamento",
                 "Ao cancelar uma inscrição, o sistema pede confirmação e avisa que a vaga liberada "
                 "poderá ser preenchida por outro aluno, inclusive por quem está na fila de espera.",
                 "info")
    b += s
    y += 76
    s, fy = footer_pub(y)
    b += s
    if modal_on:
        b += overlay(W, fy)
        mw, mh = 620, 516
        mx, my = (W - mw) / 2.0, 360
        s, my2 = modal(mx, my, mw, mh, "Cancelar inscrição",
                       sub="Processo Legislativo Municipal · Turma B - Noite")
        b += s
        b += rect(mx + 32, my2, mw - 64, 96, RED_L, "#EBB7B1", 10, 1.2)
        b += icon("alert", mx + 52, my2 + 24, 22, RED, 1.9)
        b += txt(mx + 84, my2 + 34, "Esta ação libera sua vaga", 15, RED, True)
        b += para(mx + 84, my2 + 56, "A vaga voltará a ficar disponível e poderá ser preenchida por "
                                     "outro aluno, inclusive pela fila de espera.", mw - 140, 12.5, TXT, 18)
        b += txt(mx + 32, my2 + 134, "Datas: 14 e 15/09/2026 · 19h às 22h · Online · 8h", 13, MUTED)
        b += txt(mx + 32, my2 + 158, "Protocolo da inscrição: INS-2026-004812", 13, MUTED)
        s2, _ = field(mx + 32, my2 + 186, mw - 64, "Motivo do cancelamento (opcional)",
                      "Conflito de agenda", kind="select")
        b += s2
        b += line(mx, my2 + 274, mx + mw, my2 + 274, BORDER, 1.2)
        b += btn(mx + mw - 32 - 210, my2 + 296, 210, 48, "Sim, cancelar inscrição", "danger",
                 14.5, hot=True, to="34")
        b += btn(mx + mw - 32 - 210 - 150, my2 + 296, 140, 48, "Manter", "ghost", 14.5, to="34")
    s, y = nota(fy, W, rfs, dec, obs)
    b += s
    return nome, svg(nome, W, y, b, WHITE)


@reg
def t34():
    return _meus_cursos("34-aluno-meus-cursos", False, ["ÁREA DO ALUNO - Meus Cursos", "RF 7", "RF 8", "RF 9"],
                        None,
                        "Lista de todas as inscrições do aluno, com situação (Confirmada, Em fila de "
                        "espera, Concluído, Cancelada) e ação de cancelamento exigida no RF 9.")


@reg
def t35():
    return _meus_cursos("35-aluno-cancelar-inscricao", True, ["RF 9"], None,
                        "RF 9: o sistema confirma a ação do aluno e alerta que o cancelamento abrirá a "
                        "vaga, que poderá ser preenchida por outro aluno.")


# ================================================================ 36 SALA DO CURSO
@reg
def t36():
    b, y = shell("Processo Legislativo Municipal", "Turma B - Noite · 14 e 15/09/2026 · Online", 1,
                 ["Home", "Área do Aluno", "Meus cursos", "Processo Legislativo Municipal"])
    y += 40
    lw = 762
    rx = M + lw + 24
    rw = CW - lw - 24
    b += rect(M, y, lw, 168, GREEN_L, "#A9DCC6", 12, 1.4)
    b += icon("play", M + 32, y + 34, 26, GREEN, 1.9)
    b += txt(M + 70, y + 56, "A aula ao vivo começa em 2 dias", 20, GREEN, True)
    b += txt(M + 32, y + 92, "14/09/2026 · 19h às 22h · transmissão on-line", 14, TXT)
    b += btn(M + 32, y + 112, 240, 44, "Acessar a sala virtual", "success", 14.5, "link", hot=True)
    b += txt(M + 288, y + 140, "Link liberado após a confirmação da inscrição.", 12.5, MUTED)
    ly = y + 168 + 24

    b += rect(M, ly, lw, 462, WHITE, BORDER, 12, 1.2)
    b += txt(M + 28, ly + 48, "Materiais do curso", 21, INK, True)
    b += txt(M + 28, ly + 72, "Arquivos enviados pelo professor e pela Escola.", 13, MUTED)
    mats = [("Apostila - Processo Legislativo Municipal", "PDF · 3,1 MB · enviado em 08/09/2026", "PDF", RED_L, RED),
            ("Slides do Encontro 1", "PDF · 1,4 MB · enviado em 12/09/2026", "PDF", RED_L, RED),
            ("Modelo de proposição comentado", "DOCX · 240 KB · enviado em 12/09/2026", "DOCX", BLUE_L, BLUE),
            ("Estudo de caso avaliativo", "PDF · 180 KB · entrega até 20/09/2026", "PDF", AMBER_L, AMBER)]
    for i, (t, m, tp, tl, tf) in enumerate(mats):
        s, _ = doc_row(M + 28, ly + 100 + i * 88, lw - 56, t, m, tp, tl, tf, 76)
        b += s
    ly += 462 + 24
    b += rect(M, ly, lw, 300, WHITE, BORDER, 12, 1.2)
    b += txt(M + 28, ly + 48, "Cronograma e minha frequência", 21, INK, True)
    s, _ = table(M + 28, ly + 76, lw - 56, [
        ("Encontro", 200, "start"), ("Data e horário", 240, "start"),
        ("Presença", 150, "middle"), ("Situação", 116, "end")], [
        ["Encontro 1", "14/09/2026 · 19h às 22h", ("badge", "Aguardando", "encerradas"), "-"],
        ["Encontro 2", "15/09/2026 · 19h às 22h", ("badge", "Aguardando", "encerradas"), "-"],
        ["Atividade final", "até 20/09/2026", ("badge", "Não entregue", "breve"), "-"]], 54)
    b += s
    ly += 300

    ry = y
    b += rect(rx, ry, rw, 260, WHITE, BORDER, 12, 1.2)
    b += txt(rx + 26, ry + 46, "Minha inscrição", 18, INK, True)
    for i, (l, v, k) in enumerate([("Situação", "Confirmada", "abertas"), ("Protocolo", "INS-2026-004812", None),
                                   ("Turma", "Turma B - Noite", None), ("Carga horária", "8 horas", None)]):
        yy = ry + 78 + i * 44
        b += txt(rx + 26, yy, l, 11.5, MUTED, True)
        if k:
            b += badge(rx + rw - 26 - badge_w(v), yy - 12, v, k)[0]
        else:
            b += txt(rx + rw - 26, yy, v, 13, INK, True, anchor="end")
    b += btn(rx + 26, ry + 200, rw - 52, 42, "Cancelar minha inscrição", "ghost", 13, to="35")
    ry += 260 + 20
    b += rect(rx, ry, rw, 220, WHITE, BORDER, 12, 1.2)
    b += txt(rx + 26, ry + 46, "Professor", 18, INK, True)
    b += avatar(rx + 26, ry + 66, 52, "HV", NAVY_3)
    b += txt(rx + 90, ry + 90, "Dra. Helena Vasconcelos", 14.5, INK, True)
    b += para(rx + 90, ry + 108, "Procuradora Legislativa", rw - 130, 12.5, MUTED, 16)
    b += line(rx + 26, ry + 142, rx + rw - 26, ry + 142, "#EDF1F6", 1.2)
    b += icon("mail", rx + 26, ry + 162, 16, BLUE, 1.7)
    b += para(rx + 50, ry + 174, "Dúvidas pelo canal da Escola", rw - 90, 12.5, BLUE_D, 17)
    ry += 220 + 20
    b += rect(rx, ry, rw, 176, "#F7FAFC", BORDER, 12, 1.2)
    b += icon("cert", rx + 26, ry + 26, 20, GREEN, 1.8)
    b += txt(rx + 26, ry + 76, "Certificado", 16, INK, True)
    b += para(rx + 26, ry + 98, "Liberado na Área do Aluno após o lançamento da frequência pelo gestor "
                                "(mínimo 75%).", rw - 52, 12.5, MUTED, 18)
    ry += 176
    y = max(ly, ry) + 76
    s, y = footer_pub(y)
    b += s
    s, y = nota(y, W, ["RF 2", "RF 7", "RF 14"],
                ["RF 2 - Confirmar se o link do curso online fica visível apenas aqui, após a inscrição "
                 "(Opção 2), e qual ambiente será usado na transmissão."],
                "Acesso do aluno aos materiais do curso enviados pelo professor, ao link da aula online "
                "e ao acompanhamento da própria frequência.")
    b += s
    return "36-aluno-sala-do-curso-materiais", svg("36-aluno-sala-do-curso-materiais", W, y, b, WHITE)


# ================================================================ 37 CERTIFICADOS
@reg
def t37():
    b, y = shell("Meus certificados", "Todos os certificados emitidos em seu nome pela Escola", 2)
    y += 40
    s, cxx = pills(M, y, ["Todos (7)", "2026 (4)", "2025 (3)"], 0)
    b += s
    b += btn(W - M - 200, y - 2, 200, 42, "Validar um certificado", "secondary", 13.5, "shield",
             to="17")
    y += 38 + 30
    certs = [("Controle Interno e Prestação de Contas", "13/05/2026 · 8 horas · Presencial",
              "ELCMR-2026-K2M4-8N1P-5Q7R", "100%"),
             ("Audiências Públicas e Participação Cidadã", "08/04/2026 · 4 horas · Online",
              "ELCMR-2026-B5T8-2J9L-4W3X", "100%"),
             ("Introdução ao Direito Municipal", "07/03/2026 · 15 horas · Presencial",
              "ELCMR-2026-R4V6-7H2K-9D5F", "87%"),
             ("Redação Oficial e Técnica Legislativa", "21/11/2025 · 12 horas · Presencial",
              "ELCMR-2025-P8L3-5C1M-2Z6N", "92%")]
    for i, (t, m, cod, freq) in enumerate(certs):
        yy = y + i * 128
        b += rect(M, yy, CW, 112, WHITE, BORDER, 10, 1.2)
        b += rect(M, yy, 6, 112, GREEN, None, 3)
        b += rect(M + 28, yy + 26, 60, 60, GREEN_L, None, 10)
        b += icon_c("cert", M + 58, yy + 56, 28, GREEN, 1.8)
        b += txt(M + 108, yy + 42, t, 17, INK, True)
        b += txt(M + 108, yy + 66, m, 13, MUTED)
        b += icon("key", M + 108, yy + 78, 14, FAINT, 1.6)
        b += txt(M + 130, yy + 90, "Código " + cod, 12, BLUE_D, True)
        b += txt(M + 700, yy + 44, "Frequência", 11.5, MUTED, True)
        b += txt(M + 700, yy + 68, freq, 18, GREEN, True)
        b += badge(M + 790, yy + 44, "Válido", "abertas", 11.5)[0]
        b += btn(M + CW - 28 - 150, yy + 36, 150, 42, "Baixar PDF", "primary", 13.5, "download",
                 to="21")
        b += btn(M + CW - 28 - 150 - 130, yy + 36, 120, 42, "Validar", "ghost", 13.5, to="17")
    y += len(certs) * 128 + 16
    s, y = alert(M, y, CW, "Certificado com código de autenticidade",
                 "Cada certificado traz um código alfanumérico único gerado pelo sistema no momento da "
                 "emissão, impresso no rodapé do PDF junto à URL da página pública de validação.", "info")
    b += s
    y += 24
    b += rect(M, y, CW, 190, "#F7FAFC", BORDER, 12, 1.2)
    b += txt(M + 28, y + 46, "Cursos concluídos aguardando certificado", 18, INK, True)
    b += txt(M + 28, y + 70, "O certificado é liberado depois que o gestor lança a frequência da turma.",
             13, MUTED)
    b += rect(M + 28, y + 92, CW - 56, 70, WHITE, BORDER, 8, 1.2)
    b += icon("clock", M + 50, y + 118, 20, AMBER, 1.8)
    b += txt(M + 80, y + 122, "Seminário de Transparência Legislativa", 14.5, INK, True)
    b += txt(M + 80, y + 144, "Concluído em 30/07/2026 · aguardando lançamento de frequência", 12.5, MUTED)
    b += badge(M + CW - 56 - 130, y + 114, "Em processamento", "breve", 12)[0]
    y += 190 + 76
    s, y = footer_pub(y)
    b += s
    s, y = nota(y, W, ["ÁREA DO ALUNO - Meus Certificados", "RF 4", "RF 15"], None,
                "Download dos certificados emitidos, com código de autenticidade visível e atalho para "
                "a área pública de validação.")
    b += s
    return "37-aluno-meus-certificados", svg("37-aluno-meus-certificados", W, y, b, WHITE)


# ================================================================ 38 MEUS DADOS
@reg
def t38():
    b, y = shell("Atualizar meus dados", "Mantenha seus dados corretos: eles vão para o certificado", 3)
    y += 40
    lw = 800
    rx = M + lw + 40
    rw = CW - lw - 40
    b += rect(M, y, lw, 648, WHITE, BORDER, 12, 1.2)
    b += txt(M + 32, y + 52, "Dados cadastrais", 21, INK, True)
    fy = y + 88
    hw = (lw - 64 - 20) / 2.0
    s, _ = field(M + 32, fy, lw - 64, "Nome completo", "Maria Silva dos Santos", req=True,
                 helper="Nome impresso no certificado.")
    b += s
    fy += 106
    b += txt(M + 32, fy, "CPF", 13, TXT, True)
    b += rect(M + 32, fy + 18, hw, 46, "#F0F3F7", BORDER, 6, 1.4)
    b += txt(M + 46, fy + 47, "123.456.789-00", 15, MUTED)
    b += icon("lock", M + 32 + hw - 32, fy + 32, 17, FAINT, 1.7)
    b += txt(M + 32, fy + 82, "Chave única de identificação; não pode ser alterado.", 12.5, MUTED)
    s, _ = field(M + 32 + hw + 20, fy, hw, "E-mail", "maria.santos@email.com", req=True, ic="mail",
                 helper="Usado para avisos e recuperação de senha.")
    b += s
    fy += 106
    s, _ = field(M + 32, fy, hw, "Telefone / WhatsApp", "(81) 99999-0000", req=True, ic="phone")
    b += s
    s, _ = field(M + 32 + hw + 20, fy, hw, "Tipo de vínculo", "Servidor da Câmara Municipal do Recife",
                 req=True, kind="select")
    b += s
    fy += 88
    s, _ = field(M + 32, fy, hw, "Matrícula", "20.451-7", req=True,
                 helper="Obrigatório para servidor da CMR.")
    b += s
    s, _ = field(M + 32 + hw + 20, fy, hw, "Lotação (opcional)", "Divisão de Informática")
    b += s
    fy += 108
    b += line(M + 32, fy, M + lw - 32, fy, "#EDF1F6", 1.2)
    b += checkbox(M + 32, fy + 24, "Quero receber avisos por e-mail sobre novas turmas e eventos.", True)
    b += btn(M + 32, fy + 66, 210, 50, "Salvar alterações", "primary", 15, hot=True, to="29")
    b += btn(M + 254, fy + 66, 140, 50, "Cancelar", "ghost", 15, to="29")

    ry = y
    b += rect(rx, ry, rw, 300, WHITE, BORDER, 12, 1.2)
    b += txt(rx + 26, ry + 46, "Alterar senha", 18, INK, True)
    s, _ = field(rx + 26, ry + 76, rw - 52, "Senha atual", "12345678", kind="password", ic="lock")
    b += s
    s, _ = field(rx + 26, ry + 152, rw - 52, "Nova senha", "", kind="password", ic="lock")
    b += s
    b += btn(rx + 26, ry + 232, rw - 52, 44, "Atualizar senha", "secondary", 14)
    ry += 300 + 20
    s, ry = alert(rx, ry, rw, "Seus direitos como titular (LGPD)",
                  "Você pode solicitar a correção ou a exclusão dos seus dados. A exclusão não apaga os "
                  "certificados já emitidos, que precisam ser mantidos para validação pública.", "lgpd")
    b += s
    ry += 20
    b += rect(rx, ry, rw, 176, WHITE, BORDER, 12, 1.2)
    b += txt(rx + 26, ry + 44, "Histórico da conta", 17, INK, True)
    for i, (l, v) in enumerate([("Cadastro criado em", "12/02/2025"),
                                ("Último acesso", "19/08/2026 às 14h02"),
                                ("Última alteração", "03/06/2026")]):
        b += txt(rx + 26, ry + 76 + i * 34, l, 12.5, MUTED)
        b += txt(rx + rw - 26, ry + 76 + i * 34, v, 12.5, INK, True, anchor="end")
    ry += 176
    y = max(y + 648, ry) + 76
    s, y = footer_pub(y)
    b += s
    s, y = nota(y, W, ["ÁREA DO ALUNO - Atualizar meus dados", "RF 6"], None,
                "Manutenção dos dados do RF 6 pelo próprio aluno, com CPF bloqueado por ser chave única "
                "e alteração de senha em bloco separado.")
    b += s
    return "38-aluno-atualizar-dados", svg("38-aluno-atualizar-dados", W, y, b, WHITE)
