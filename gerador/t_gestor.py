# -*- coding: utf-8 -*-
"""Telas 39-52: Area do Gestor da Escola (RF 10 a RF 17)."""
import math

from blocks import *

TELAS = []
CX = SB_W + 36
CWA = W - SB_W - 72
Y0 = 96 + 36


def reg(fn):
    TELAS.append(fn)
    return fn


def wrap_admin(nome, active, titulo, sub, crumbs, actions, content, cend,
               rfs, dec=None, obs=None, menu=None, papel="ÁREA DO GESTOR",
               user=("Robertson Barros", "Gestor da Escola", "RB"), extra=""):
    page_h = max(cend + 44, 1024)
    b = rect(SB_W, 0, W - SB_W, page_h, BG)
    b += sidebar(page_h, menu or MENU_GESTOR, active, papel, user[0], user[1], user[2])
    b += topbar_admin(titulo, sub, W, SB_W, actions, crumbs)
    b += content
    b += extra
    s, y = nota(page_h, W, rfs, dec, obs)
    b += s
    return nome, svg(nome, W, y, b, WHITE)


def sec(x, y, titulo, sub=None, w=CWA, action=None):
    out = txt(x, y, titulo, 19, INK, True)
    ny = y + 18
    if sub:
        out += txt(x, y + 22, sub, 13, MUTED)
        ny = y + 34
    if action:
        out += txt(x + w, y, action, 13, BLUE_D, True, anchor="end")
    return out, ny


# ================================================================ 39 PAINEL
@reg
def t39():
    c = ""
    y = Y0
    stats = [("Cursos ativos", "9", "+2 neste mês", "book", BLUE, BLUE_L),
             ("Inscrições confirmadas", "412", "+38 esta semana", "check", GREEN, GREEN_L),
             ("Na fila de espera", "27", "6 turmas com fila", "clock", AMBER, AMBER_L),
             ("Certificados a emitir", "58", "3 turmas encerradas", "cert", PURPLE, PURPLE_L)]
    sw = (CWA - 3 * 20) / 4.0
    for i, (l, v, s2, ic, tn, tl) in enumerate(stats):
        c += stat(CX + i * (sw + 20), y, sw, 164, l, v, s2, ic, tn, tl)
    y += 164 + 32

    lw = 700
    rx = CX + lw + 20
    rw = CWA - lw - 20
    s, ny = sec(CX, y, "Turmas em andamento e próximas", "Ocupação de vagas por turma", lw,
                "Ver todas")
    c += s
    s, ly = table(CX, ny + 14, lw, [
        ("Curso / turma", 300, "start"), ("Início", 120, "start"),
        ("Ocupação", 180, "start"), ("Situação", 100, "end")], [
        [("two", "Processo Legislativo", "Turma B - Noite"), "14/09/2026", ("prog", 60, "18/30"),
         ("badge", "Abertas", "abertas")],
        [("two", "Processo Legislativo", "Turma C - Tarde"), "16/09/2026", ("prog", 100, "35/35"),
         ("badge", "Esgotado", "esgotado")],
        [("two", "Ética e Conduta", "Turma única"), "22/09/2026", ("prog", 45, "18/40"),
         ("badge", "Em breve", "breve")],
        [("two", "Tecnologia e Governo Digital", "Turma A"), "05/10/2026", ("prog", 100, "35/35"),
         ("badge", "Esgotado", "esgotado")],
        [("two", "Redação Oficial", "Turma A - Manhã"), "19/10/2026", ("prog", 36, "9/25"),
         ("badge", "Abertas", "abertas")]], 62)
    c += s
    ly += 28
    s, ny2 = sec(CX, ly, "Pendências da Escola", "Ações que dependem do gestor", lw)
    c += s
    pend = [("Lançar frequência da turma encerrada", "Controle Interno · encerrada em 13/05/2026", "alert", AMBER, AMBER_L, "Lançar"),
            ("Emitir 30 certificados", "Audiências Públicas · frequência já lançada", "cert", GREEN, GREEN_L, "Emitir"),
            ("Chamar 3 alunos da fila de espera", "Tecnologia e Governo Digital · Turma A", "clock", BLUE, BLUE_L, "Chamar"),
            ("Aprovar material enviado pelo professor", "Processo Legislativo · 2 arquivos", "folder", PURPLE, PURPLE_L, "Revisar")]
    for i, (t, d, ic, tn, tl, act) in enumerate(pend):
        yy = ny2 + 14 + i * 78
        c += rect(CX, yy, lw, 66, WHITE, BORDER, 8, 1.2)
        c += rect(CX + 18, yy + 15, 36, 36, tl, None, 8)
        c += icon_c(ic, CX + 36, yy + 33, 18, tn, 1.8)
        c += txt(CX + 66, yy + 28, t, 14.5, INK, True)
        c += txt(CX + 66, yy + 48, d, 12.5, MUTED)
        c += btn(CX + lw - 18 - 96, yy + 15, 96, 36, act, "secondary", 13,
                 to={"Lançar": "46", "Emitir": "47", "Chamar": "45", "Revisar": "55"}[act])
    ly = ny2 + 14 + len(pend) * 78

    ry = Y0 + 164 + 32
    c += rect(rx, ry, rw, 300, WHITE, BORDER, 10, 1.2)
    c += txt(rx + 22, ry + 40, "Inscrições por semana", 16, INK, True)
    c += txt(rx + 22, ry + 60, "Últimas 8 semanas", 12, MUTED)
    bars = [42, 58, 35, 76, 64, 92, 71, 88]
    bw = (rw - 60) / 8.0
    for i, v in enumerate(bars):
        h = v * 1.5
        c += rect(rx + 30 + i * bw, ry + 250 - h, bw - 10, h, BLUE if i < 7 else GOLD, None, 4)
        c += ctext(rx + 30 + (bw - 10) / 2.0 + i * bw, ry + 268, "S%d" % (i + 1), 10, MUTED)
    ry += 300 + 20
    c += rect(rx, ry, rw, 262, WHITE, BORDER, 10, 1.2)
    c += txt(rx + 22, ry + 40, "Últimas ações registradas", 16, INK, True)
    logs = [("Inscrição cancelada", "R. Barros · hoje 14h02"),
            ("Curso publicado", "R. Barros · hoje 11h20"),
            ("Certificado emitido (30)", "R. Barros · ontem 16h44"),
            ("Notícia publicada", "C. Nunes · ontem 09h15"),
            ("Professor cadastrado", "R. Barros · 17/08 15h30")]
    for i, (t, d) in enumerate(logs):
        yy = ry + 66 + i * 38
        c += circ(rx + 28, yy + 4, 4, GOLD)
        c += txt(rx + 44, yy + 8, t, 12.5, INK, True)
        c += txt(rx + rw - 22, yy + 8, d, 11.5, MUTED, anchor="end")
    ry += 262
    return wrap_admin("39-gestor-painel", "Painel", "Painel do Gestor",
                      "Visão geral da Escola do Legislativo", None,
                      [("Novo curso", "primary", "plus", "41")], c, max(ly, ry),
                      ["ÁREA DO GESTOR", "RF 10 a RF 17"], None,
                      "Painel inicial com indicadores, turmas em andamento, pendências operacionais e "
                      "log das últimas ações realizadas no sistema.")


# ================================================================ 40 CURSOS
@reg
def t40():
    c = ""
    y = Y0
    c += rect(CX, y, CWA, 88, WHITE, BORDER, 10, 1.2)
    c += rect(CX + 20, y + 24, 380, 40, WHITE, BORDER2, 6, 1.3)
    c += icon("search", CX + 32, y + 35, 17, FAINT, 1.7)
    c += txt(CX + 58, y + 49, "Buscar curso por título ou tema", 13, FAINT)
    for i, (l, wd) in enumerate([("Situação: todas", 190), ("Tema: todos", 170), ("Ano: 2026", 140)]):
        x = CX + 420 + [0, 206, 392][i]
        c += rect(x, y + 24, wd, 40, "#F7FAFC", BORDER2, 6, 1.3)
        c += txt(x + 12, y + 49, l, 13, TXT)
        c += icon("chev-d", x + wd - 28, y + 35, 17, MUTED, 1.8)
    c += btn(CX + CWA - 20 - 110, y + 24, 110, 40, "Filtrar", "ghost", 13.5)
    y += 88 + 24
    s, y = table(CX, y, CWA, [
        ("Curso", 330, "start"), ("Tema", 150, "start"), ("Turmas", 90, "middle"),
        ("Inscritos", 110, "middle"), ("Situação", 150, "middle"), ("Ações", 240, "end")], [
        [("two", "Processo Legislativo Municipal", "8h · Online e Presencial"), "Processo Legislativo",
         "3", "59/95", ("badge", "Publicado", "abertas"),
         ("icons", [("eye", BLUE, "05"), ("edit", MUTED, "41"), ("users", MUTED, "43"),
                    ("trash", RED)])],
        [("two", "Ética e Conduta no Serviço Público", "12h · Presencial"), "Direito",
         "1", "18/40", ("badge", "Em breve", "breve"),
         ("icons", [("eye", BLUE), ("edit", MUTED), ("users", MUTED), ("trash", RED)])],
        [("two", "Tecnologia e Governo Digital", "6h · Híbrido"), "Tecnologia",
         "1", "35/35", ("badge", "Esgotado", "esgotado"),
         ("icons", [("eye", BLUE), ("edit", MUTED), ("users", MUTED), ("trash", RED)])],
        [("two", "Redação Oficial e Técnica Legislativa", "12h · Presencial"), "Redação Oficial",
         "2", "9/50", ("badge", "Publicado", "abertas"),
         ("icons", [("eye", BLUE), ("edit", MUTED), ("users", MUTED), ("trash", RED)])],
        [("two", "Orçamento Público e LOA Municipal", "8h · Online"), "Orçamento",
         "2", "27/60", ("badge", "Publicado", "abertas"),
         ("icons", [("eye", BLUE), ("edit", MUTED), ("users", MUTED), ("trash", RED)])],
        [("two", "LGPD na Administração Pública", "8h · Híbrido"), "Direito",
         "1", "0/50", ("badge", "Rascunho", "encerradas"),
         ("icons", [("eye", BLUE), ("edit", MUTED), ("users", MUTED), ("trash", RED)])],
        [("two", "Controle Interno e Prestação de Contas", "8h · Presencial"), "Controle",
         "1", "30/30", ("badge", "Encerrado", "encerradas"),
         ("icons", [("eye", BLUE), ("edit", MUTED), ("users", MUTED), ("trash", RED)])],
        [("two", "Audiências Públicas e Participação Cidadã", "4h · Online"), "Processo Legislativo",
         "1", "80/80", ("badge", "Encerrado", "encerradas"),
         ("icons", [("eye", BLUE), ("edit", MUTED), ("users", MUTED), ("trash", RED)])]], 66)
    c += s
    y += 24
    s, y = pagination(CX, y, CWA, "23")
    c += s
    return wrap_admin("40-gestor-cursos-lista", "Cursos", "Gestão de cursos",
                      "Cadastro, publicação e acompanhamento dos cursos e eventos",
                      ["Painel", "Cursos"],
                      [("Novo curso", "primary", "plus", "41"),
                       ("Exportar", "ghost", "download")],
                      c, y, ["RF 12"], None,
                      "RF 12 - Gestão de cursos: criar, editar, publicar, despublicar e encerrar cursos "
                      "e eventos, com controle de situação e de turmas vinculadas.")


# ================================================================ 41 CURSO FORM
@reg
def t41():
    c = ""
    y = Y0
    c += rect(CX, y, CWA, 68, WHITE, BORDER, 10, 1.2)
    for i, (t, on) in enumerate([("1. Informações do curso", True), ("2. Turmas e vagas", False),
                                 ("3. Professor e materiais", False), ("4. Publicação", False)]):
        x = CX + 28 + i * 268
        c += circ(x + 13, y + 34, 13, BLUE if on else "#E6ECF2")
        c += ctext(x + 13, y + 34, str(i + 1), 12.5, WHITE if on else MUTED, True)
        c += txt(x + 34, y + 39, t[3:], 13.5, INK if on else MUTED, on)
        if i < 3:
            c += line(x + 210, y + 34, x + 258, y + 34, BORDER2, 1.4)
    y += 68 + 24

    lw = 740
    rx = CX + lw + 20
    rw = CWA - lw - 20
    c += rect(CX, y, lw, 704, WHITE, BORDER, 10, 1.2)
    c += txt(CX + 28, y + 46, "Informações do curso", 19, INK, True)
    fy = y + 78
    hw = (lw - 56 - 18) / 2.0
    s, _ = field(CX + 28, fy, lw - 56, "Título do curso ou evento", "Processo Legislativo Municipal", req=True)
    c += s
    fy += 88
    s, _ = textarea(CX + 28, fy, lw - 56, "Ementa - O que o aluno vai aprender",
                    "Tramitação de proposições, comissões, ordem do dia, votação, redação final, "
                    "sanção e veto, com exercícios práticos.", 108, True)
    c += s
    fy += 136
    s, _ = field(CX + 28, fy, hw, "Tema", "Processo Legislativo", req=True, kind="select")
    c += s
    s, _ = field(CX + 28 + hw + 18, fy, hw, "Público-alvo", "Interno e externo", req=True, kind="select")
    c += s
    fy += 88
    s, _ = field(CX + 28, fy, hw, "Formato", "Online", req=True, kind="select",
                 helper="Presencial / Online / Híbrido - vira etiqueta no card.")
    c += s
    s, _ = field(CX + 28 + hw + 18, fy, hw, "Carga horária total", "8 horas", req=True,
                 helper="Impressa no certificado.")
    c += s
    fy += 108
    s, _ = field(CX + 28, fy, hw, "Início das inscrições", "20/08/2026", req=True, kind="date")
    c += s
    s, _ = field(CX + 28 + hw + 18, fy, hw, "Fim das inscrições", "10/09/2026", req=True, kind="date")
    c += s
    fy += 88
    c += txt(CX + 28, fy, "Imagem de capa do card", 13, TXT, True)
    c += rect(CX + 28, fy + 18, lw - 56, 96, "#F7FAFC", BORDER2, 8, 1.4, )
    c += icon("upload", CX + 48, fy + 48, 24, BLUE, 1.8)
    c += txt(CX + 84, fy + 56, "Arraste a imagem ou clique para enviar", 14, BLUE_D, True)
    c += txt(CX + 84, fy + 78, "JPG ou PNG · proporção 16:9 · até 2 MB", 12, MUTED)
    c += btn(CX + lw - 56 - 120 + 28, fy + 46, 120, 40, "Selecionar", "secondary", 13)
    ly = y + 704

    ry = y
    c += rect(rx, ry, rw, 340, WHITE, BORDER, 10, 1.2)
    c += txt(rx + 22, ry + 42, "Pré-visualização do card", 16, INK, True)
    c += txt(rx + 22, ry + 62, "Assim o curso aparece na vitrine", 12, MUTED)
    pw = rw - 44
    c += rect(rx + 22, ry + 80, pw, 230, WHITE, BORDER, 8, 1.2)
    c += img_ph(rx + 22, ry + 80, pw, 90, 8, TONES[0])
    c += rect(rx + 22, ry + 162, pw, 8, TONES[0])
    s2, _ = badges_row(rx + 34, ry + 182, [("Inscrições abertas", "abertas"), ("Online", "info")], 10.5, 20, 6)
    c += s2
    c += para(rx + 34, ry + 224, "Processo Legislativo Municipal", pw - 24, 14, INK, 18, True, maxlines=2)
    c += txt(rx + 34, ry + 262, "14 e 15/09/2026 · 8h", 11.5, MUTED)
    c += btn(rx + 34, ry + 274, pw - 24, 28, "Ver detalhes", "primary", 11.5, rx=4)
    ry += 340 + 20
    c += rect(rx, ry, rw, 214, WHITE, BORDER, 10, 1.2)
    c += txt(rx + 22, ry + 42, "Situação da publicação", 16, INK, True)
    for i, (t, on, d) in enumerate([("Rascunho", False, "Só o gestor vê"),
                                    ("Publicado - inscrições em breve", False, "Aparece sem botão"),
                                    ("Publicado - inscrições abertas", True, "Aceita inscrições")]):
        c += radio(rx + 22, ry + 66 + i * 48, t, on, 18, d, rw - 70)
    ry += 214 + 20
    c += rect(rx, ry, rw, 128, "#F7FAFC", BORDER, 10, 1.2)
    c += btn(rx + 22, ry + 24, rw - 44, 46, "Salvar e continuar", "primary", 14.5, hot=True,
             to="42")
    c += btn(rx + 22, ry + 78, rw - 44, 38, "Salvar como rascunho", "ghost", 13)
    ry += 128
    return wrap_admin("41-gestor-curso-cadastro", "Cursos", "Novo curso",
                      "Passo 1 de 4 · informações gerais", ["Painel", "Cursos", "Novo curso"],
                      None, c, max(ly, ry), ["RF 12"], None,
                      "RF 12 - Cadastro do curso com os campos que alimentam o card da vitrine (RF 1) e "
                      "a página de detalhes (RF 2): título, ementa, tema, público, formato, carga "
                      "horária, período de inscrição e imagem de capa.")


# ================================================================ 42 TURMAS
@reg
def t42():
    c = ""
    y = Y0
    c += rect(CX, y, CWA, 108, WHITE, BORDER, 10, 1.2)
    c += rect(CX, y, 6, 108, BLUE, None, 3)
    c += txt(CX + 28, y + 42, "Processo Legislativo Municipal", 20, INK, True)
    s2, _ = badges_row(CX + 28, y + 58, [("Publicado", "abertas"), ("8 horas", "neutro"),
                                         ("Interno e externo", "info"), ("3 turmas", "gold")], 11.5, 24)
    c += s2
    c += btn(CX + CWA - 28 - 150, y + 34, 150, 42, "Nova turma", "primary", 13.5, "plus")
    c += btn(CX + CWA - 28 - 150 - 130, y + 34, 120, 42, "Editar curso", "ghost", 13.5, to="41")
    y += 108 + 24
    s, y = sec(CX, y, "Turmas do curso", "Cada turma tem dias, horário, local e controle próprio de vagas")
    c += s
    y += 14
    s, y = table(CX, y, CWA, [
        ("Turma", 190, "start"), ("Dias e horário", 250, "start"), ("Local / plataforma", 200, "start"),
        ("Vagas", 190, "start"), ("Situação", 130, "middle"), ("Ações", 110, "end")], [
        [("two", "Turma A - Manhã", "14 e 15/09/2026"), "Seg e Ter · 09h às 12h", "Sala virtual - Escola",
         ("prog", 20, "6/30"), ("badge", "Abertas", "abertas"),
         ("icons", [("edit", MUTED), ("users", BLUE, "43")])],
        [("two", "Turma B - Noite", "14 e 15/09/2026"), "Seg e Ter · 19h às 22h", "Sala virtual - Escola",
         ("prog", 60, "18/30"), ("badge", "Abertas", "abertas"),
         ("icons", [("edit", MUTED), ("users", BLUE)])],
        [("two", "Turma C - Tarde", "16/09/2026"), "Qua · 14h às 18h", "Auditório - 1º andar",
         ("prog", 100, "35/35"), ("badge", "Esgotada", "esgotado"),
         ("icons", [("edit", MUTED), ("users", BLUE)])]], 72)
    c += s
    y += 32

    lw = 700
    rx = CX + lw + 20
    rw = CWA - lw - 20
    c += rect(CX, y, lw, 468, WHITE, BORDER, 10, 1.2)
    c += txt(CX + 28, y + 46, "Nova turma", 19, INK, True)
    fy = y + 78
    hw = (lw - 56 - 18) / 2.0
    s, _ = field(CX + 28, fy, hw, "Identificação da turma", "Turma D - Noite", req=True)
    c += s
    s, _ = field(CX + 28 + hw + 18, fy, hw, "Total de vagas", "30", req=True,
                 helper="Base do controle Vagas Ocupadas < Vagas Totais.")
    c += s
    fy += 106
    s, _ = field(CX + 28, fy, hw, "Data de início", "20/10/2026", req=True, kind="date")
    c += s
    s, _ = field(CX + 28 + hw + 18, fy, hw, "Data de término", "21/10/2026", req=True, kind="date")
    c += s
    fy += 88
    s, _ = field(CX + 28, fy, hw, "Horário", "19h às 22h", req=True, ic="clock")
    c += s
    s, _ = field(CX + 28 + hw + 18, fy, hw, "Local / plataforma", "Sala virtual - Escola", req=True, ic="pin")
    c += s
    fy += 88
    s, _ = field(CX + 28, fy, hw, "Professor responsável", "Dra. Helena Vasconcelos", req=True, kind="select")
    c += s
    s, _ = field(CX + 28 + hw + 18, fy, hw, "Vagas reservadas ao público interno", "15",
                 helper="Opcional. Reserva por tipo de vínculo.")
    c += s
    fy += 106
    c += btn(CX + 28, fy, 180, 46, "Criar turma", "primary", 14.5)
    c += btn(CX + 222, fy, 130, 46, "Cancelar", "ghost", 14.5)
    ly = y + 468

    ry = y
    s, ry = alert(rx, ry, rw, "Divulgação das turmas",
                  "Cada turma aparece na página de detalhes do curso com seus dias, horário e vagas. O "
                  "aluno escolhe a turma no momento da inscrição.", "info")
    c += s
    ry += 20
    c += rect(rx, ry, rw, 236, WHITE, BORDER, 10, 1.2)
    c += txt(rx + 22, ry + 42, "Regras de vagas", 16, INK, True)
    for i, t in enumerate(["A inscrição só é gravada se Vagas Ocupadas < Vagas Totais.",
                           "Turma cheia habilita a lista de espera automática.",
                           "Cancelamento devolve a vaga imediatamente ao total disponível.",
                           "O gestor pode ampliar o total de vagas a qualquer momento."]):
        c += circ(rx + 30, ry + 74 + i * 40, 3.5, GOLD)
        c += para(rx + 44, ry + 78 + i * 40, t, rw - 76, 12.5, MUTED, 17)
    ry += 236
    return wrap_admin("42-gestor-turmas", "Turmas", "Gestão de turmas",
                      "Turmas, horários e vagas do curso selecionado",
                      ["Painel", "Cursos", "Processo Legislativo Municipal", "Turmas"],
                      None, c, max(ly, ry), ["RF 13"],
                      ["Um curso pode ter várias turmas? Se sim, como fica a divulgação dos dias e "
                       "horários das turmas? O protótipo assume várias turmas por curso, cada uma com "
                       "período, horário, local, professor e total de vagas próprios."],
                      "RF 13 - Gestão de turmas: criação de turmas vinculadas ao curso com controle "
                      "individual de vagas.")


# ================================================================ 43 INSCRICOES
def _inscricoes(nome, modal, rfs, dec, obs):
    c = ""
    y = Y0
    stats = [("Confirmadas", "59", GREEN), ("Em fila de espera", "12", AMBER),
             ("Canceladas", "7", RED), ("Total de vagas", "95", BLUE)]
    sw = (CWA - 3 * 20) / 4.0
    for i, (l, v, tn) in enumerate(stats):
        c += rect(CX + i * (sw + 20), y, sw, 96, WHITE, BORDER, 10, 1.2)
        c += rect(CX + i * (sw + 20), y, 5, 96, tn, None, 3)
        c += txt(CX + i * (sw + 20) + 24, y + 44, v, 26, INK, True)
        c += txt(CX + i * (sw + 20) + 24, y + 68, l, 12.5, MUTED)
    y += 96 + 24
    c += rect(CX, y, CWA, 88, WHITE, BORDER, 10, 1.2)
    c += rect(CX + 20, y + 24, 300, 40, WHITE, BORDER2, 6, 1.3)
    c += icon("search", CX + 32, y + 35, 17, FAINT, 1.7)
    c += txt(CX + 58, y + 49, "Buscar por nome ou CPF", 13, FAINT)
    for i, (l, wd) in enumerate([("Curso: Processo Legislativo", 260), ("Turma: todas", 160),
                                 ("Situação: todas", 170)]):
        x = CX + 340 + [0, 276, 452][i]
        c += rect(x, y + 24, wd, 40, "#F7FAFC", BORDER2, 6, 1.3)
        c += txt(x + 12, y + 49, l, 12.5, TXT)
        c += icon("chev-d", x + wd - 26, y + 35, 16, MUTED, 1.8)
    c += btn(CX + CWA - 20 - 120, y + 24, 120, 40, "Exportar", "ghost", 13, "download")
    y += 88 + 24
    s, y = table(CX, y, CWA, [
        ("Aluno", 300, "start"), ("Vínculo", 170, "start"), ("Turma", 160, "start"),
        ("Inscrito em", 130, "start"), ("Situação", 150, "middle"), ("Ações", 190, "end")], [
        [("avatar", "Maria Silva dos Santos", "MS", "CPF 123.***.***-89"), "Servidora CMR · 20.451-7",
         "Turma B - Noite", "19/08/2026", ("badge", "Confirmada", "abertas"),
         ("btns", [("Ver", "secondary"), ("Cancelar", "danger", "44")])],
        [("avatar", "João Pedro Albuquerque", "JA", "CPF 987.***.***-21"), "Servidor de outro órgão",
         "Turma B - Noite", "18/08/2026", ("badge", "Confirmada", "abertas"),
         ("btns", [("Ver", "secondary"), ("Cancelar", "danger")])],
        [("avatar", "Ana Beatriz Correia", "AC", "CPF 456.***.***-33"), "Público externo",
         "Turma A - Manhã", "18/08/2026", ("badge", "Confirmada", "abertas"),
         ("btns", [("Ver", "secondary"), ("Cancelar", "danger")])],
        [("avatar", "Carlos Henrique Lima", "CL", "CPF 321.***.***-77"), "Servidor CMR · 18.902-4",
         "Turma C - Tarde", "17/08/2026", ("badge", "Em fila de espera", "breve"),
         ("btns", [("Chamar", "success", "45"), ("Remover", "ghost")])],
        [("avatar", "Fernanda Duarte Melo", "FM", "CPF 654.***.***-10"), "Público externo",
         "Turma C - Tarde", "17/08/2026", ("badge", "Em fila de espera", "breve"),
         ("btns", [("Chamar", "success"), ("Remover", "ghost")])],
        [("avatar", "Rodrigo Alves Barbosa", "RB", "CPF 789.***.***-55"), "Servidor CMR · 21.007-9",
         "Turma A - Manhã", "16/08/2026", ("badge", "Cancelada", "esgotado"),
         ("btns", [("Ver log", "ghost")])]], 74)
    c += s
    y += 24
    s, y = pagination(CX, y, CWA, "78")
    c += s
    extra = ""
    if modal:
        page_h = max(y + 44, 1024)
        extra += overlay(W, page_h)
        mw, mh = 660, 690
        mx, my = (W - mw) / 2.0, 196
        s2, my2 = modal_cancel(mx, my, mw, mh)
        extra += s2
    return wrap_admin(nome, "Inscrições", "Gestão de inscrições",
                      "Inscrições confirmadas, fila de espera e cancelamentos",
                      ["Painel", "Inscrições"], None, c, y, rfs, dec, obs, extra=extra)


def modal_cancel(mx, my, mw, mh):
    s, my2 = modal(mx, my, mw, mh, "Cancelar inscrição do aluno",
                   sub="Processo Legislativo Municipal · Turma B - Noite")
    s += rect(mx + 32, my2, mw - 64, 84, "#F7FAFC", BORDER, 8, 1.2)
    s += avatar(mx + 50, my2 + 18, 48, "MS", NAVY_3)
    s += txt(mx + 110, my2 + 40, "Maria Silva dos Santos", 15.5, INK, True)
    s += txt(mx + 110, my2 + 62, "CPF 123.***.***-89 · Servidora CMR · matrícula 20.451-7", 12.5, MUTED)
    s += rect(mx + 32, my2 + 100, mw - 64, 96, AMBER_L, "#EBCE95", 8, 1.2)
    s += icon("alert", mx + 52, my2 + 124, 20, AMBER, 1.9)
    s += txt(mx + 82, my2 + 132, "A vaga será liberada", 14.5, AMBER, True)
    s += para(mx + 82, my2 + 154, "Ao confirmar, a vaga volta a ficar disponível e poderá ser preenchida "
                                  "por outro aluno, inclusive pelo próximo da fila de espera.",
              mw - 140, 12.5, TXT, 18)
    s2, _ = field(mx + 32, my2 + 216, mw - 64, "Motivo do cancelamento", "Solicitação do aluno",
                  req=True, kind="select")
    c2, _ = textarea(mx + 32, my2 + 306, mw - 64, "Observação para o log", "", 70)
    s += s2 + c2
    s += line(mx, my2 + 410, mx + mw, my2 + 410, BORDER, 1.2)
    s += icon("info", mx + 32, my2 + 428, 15, MUTED, 1.7)
    s += txt(mx + 54, my2 + 440, "Esta ação será registrada em log com data, hora, usuário responsável, "
                                 "aluno, curso e turma.", 12, MUTED)
    s += btn(mx + mw - 32 - 210, my2 + 462, 210, 46, "Confirmar cancelamento", "danger", 14,
             hot=True, to="43")
    s += btn(mx + mw - 32 - 210 - 140, my2 + 462, 130, 46, "Voltar", "ghost", 14, to="43")
    return s, my2


@reg
def t43():
    return _inscricoes("43-gestor-inscricoes", False, ["RF 11", "RF 13"], None,
                       "RF 13 - Gestão de inscrições: o gestor visualiza todas as inscrições dos cursos "
                       "disponíveis, com filtro por curso, turma e situação, e exportação da lista.")


@reg
def t44():
    return _inscricoes("44-gestor-cancelar-inscricao-log", True, ["RF 11"], None,
                       "RF 11 - Cancelamento pelo gestor: o sistema confirma a ação, alerta que a vaga "
                       "será liberada e registra em log o responsável, data, hora, aluno, curso e turma.")


# ================================================================ 45 FILA
@reg
def t45():
    c = ""
    y = Y0
    s, ny = alert(CX, y, CWA, "Uma vaga foi liberada na Turma C - Tarde",
                  "Rodrigo Alves Barbosa cancelou a inscrição em 19/08/2026 às 14h02. A vaga está "
                  "disponível para o próximo da fila.", "warn")
    c += s
    y = ny + 24
    lw = 700
    rx = CX + lw + 20
    rw = CWA - lw - 20
    s, ny2 = sec(CX, y, "Fila de espera - Processo Legislativo Municipal / Turma C - Tarde",
                 "A ordem de chegada é respeitada automaticamente", lw)
    c += s
    s, ly = table(CX, ny2 + 14, lw, [
        ("Pos.", 60, "middle"), ("Aluno", 260, "start"), ("Entrou na fila", 170, "start"),
        ("Situação", 210, "end")], [
        [("bold", "1"), ("avatar", "Carlos Henrique Lima", "CL", "Servidor CMR · 18.902-4"),
         "17/08/2026 09h12", ("btns", [("Chamar agora", "success", "43"),
                                       ("Remover", "ghost")])],
        [("bold", "2"), ("avatar", "Fernanda Duarte Melo", "FM", "Público externo"),
         "17/08/2026 15h48", ("badge", "Aguardando", "encerradas")],
        [("bold", "3"), ("avatar", "Paulo Ricardo Nunes", "PN", "Servidor de outro órgão"),
         "18/08/2026 08h05", ("badge", "Aguardando", "encerradas")],
        [("bold", "4"), ("avatar", "Juliana Ferreira Souza", "JS", "Servidora CMR · 19.774-2"),
         "18/08/2026 11h30", ("badge", "Aguardando", "encerradas")]], 74)
    c += s
    ly += 28
    s, ny3 = sec(CX, ly, "Convocações em andamento", "Alunos que já foram avisados da vaga", lw)
    c += s
    s, ly = table(CX, ny3 + 14, lw, [
        ("Aluno", 260, "start"), ("Avisado em", 170, "start"), ("Prazo", 130, "start"),
        ("Situação", 140, "end")], [
        [("avatar", "Marcos Vinícius Gomes", "MG", "Turma A - Manhã"), "18/08/2026 10h00",
         ("two", "Vence hoje", "19/08 às 10h00"), ("badge", "Aguardando", "breve")],
        [("avatar", "Tereza Cristina Alves", "TA", "Turma A - Manhã"), "16/08/2026 14h20",
         ("two", "Expirado", "17/08 às 14h20"), ("badge", "Perdeu a vaga", "esgotado")]], 74)
    c += s

    ry = y
    c += rect(rx, ry, rw, 386, WHITE, BORDER, 10, 1.2)
    c += txt(rx + 22, ry + 44, "Como preencher a vaga", 17, INK, True)
    c += txt(rx + 22, ry + 66, "Decisão pendente de reunião (RF 10)", 12, AMBER, True)
    c += rect(rx + 22, ry + 86, rw - 44, 128, BLUE_L, BLUE, 8, 1.6)
    c += radio(rx + 40, ry + 106, "Opção 1 - Automática", True, 18,
               "O sistema envia e-mail ao próximo da fila e dá 24h para ele assumir a vaga. "
               "Expirado o prazo, chama o seguinte.", rw - 100)
    c += rect(rx + 22, ry + 228, rw - 44, 112, WHITE, BORDER2, 8, 1.2)
    c += radio(rx + 40, ry + 248, "Opção 2 - Manual", False, 18,
               "Alguém da Escola entra em contato com o próximo da fila e confirma a inscrição pelo "
               "painel.", rw - 100)
    ry += 386 + 20
    c += rect(rx, ry, rw, 200, WHITE, BORDER, 10, 1.2)
    c += txt(rx + 22, ry + 44, "Configuração da fila", 17, INK, True)
    for i, (l, v) in enumerate([("Prazo para assumir a vaga", "24 horas"),
                                ("Aviso por e-mail", "Ativado"),
                                ("Aviso por WhatsApp", "Desativado")]):
        c += txt(rx + 22, ry + 78 + i * 40, l, 12.5, MUTED)
        c += txt(rx + rw - 22, ry + 78 + i * 40, v, 12.5, INK, True, anchor="end")
    c += btn(rx + 22, ry + 148, rw - 44, 38, "Alterar configuração", "ghost", 13)
    ry += 200
    return wrap_admin("45-gestor-fila-espera", "Fila de espera", "Gestão da fila de espera",
                      "Ordem da fila, convocações e prazos", ["Painel", "Fila de espera"],
                      None, c, max(ly, ry), ["RF 8", "RF 10"],
                      ["RF 10 - Quando surgir vaga, o sistema avisa automaticamente o próximo da fila "
                       "por e-mail com 24h para assumir (Opção 1) ou o contato é feito manualmente pela "
                       "equipe da Escola (Opção 2)?"],
                      "RF 8 e RF 10 - Fila organizada pela ordem de entrada de cada aluno, com "
                      "convocação, prazo de resposta e histórico de vagas perdidas.")


# ================================================================ 46 FREQUENCIA
@reg
def t46():
    c = ""
    y = Y0
    c += rect(CX, y, CWA, 104, WHITE, BORDER, 10, 1.2)
    c += rect(CX, y, 6, 104, GREEN, None, 3)
    c += txt(CX + 28, y + 42, "Controle Interno e Prestação de Contas", 19, INK, True)
    c += txt(CX + 28, y + 66, "Turma única · 12 e 13/05/2026 · Presencial · 8 horas · 30 inscritos",
             13, MUTED)
    c += btn(CX + CWA - 28 - 170, y + 32, 170, 42, "Salvar frequência", "primary", 13.5,
             hot=True, to="47")
    c += btn(CX + CWA - 28 - 170 - 150, y + 32, 140, 42, "Lista de presença", "ghost", 13.5, "print")
    y += 104 + 24
    c += rect(CX, y, CWA, 76, WHITE, BORDER, 10, 1.2)
    s2, cx2 = pills(CX + 24, y + 20, ["Encontro 1 - 12/05", "Encontro 2 - 13/05", "Consolidado"], 0, 36)
    c += s2
    c += txt(CX + CWA - 24, y + 44, "Frequência mínima para certificado: 75%", 13, MUTED, anchor="end")
    y += 76 + 24
    s, y = table(CX, y, CWA, [
        ("", 50, "start"), ("Aluno", 300, "start"), ("Vínculo", 200, "start"),
        ("Encontro 1", 130, "middle"), ("Encontro 2", 130, "middle"),
        ("Frequência", 180, "start"), ("Situação", 110, "end")], [
        [("check", True), ("avatar", "Maria Silva dos Santos", "MS", "CPF 123.***.***-89"),
         "Servidora CMR", ("badge", "Presente", "abertas"), ("badge", "Presente", "abertas"),
         ("prog", 100, "100%"), ("badge", "Apto", "abertas")],
        [("check", True), ("avatar", "João Pedro Albuquerque", "JA", "CPF 987.***.***-21"),
         "Outro órgão", ("badge", "Presente", "abertas"), ("badge", "Presente", "abertas"),
         ("prog", 100, "100%"), ("badge", "Apto", "abertas")],
        [("check", True), ("avatar", "Ana Beatriz Correia", "AC", "CPF 456.***.***-33"),
         "Público externo", ("badge", "Presente", "abertas"), ("badge", "Falta", "esgotado"),
         ("prog", 50, "50%"), ("badge", "Inapto", "esgotado")],
        [("check", False), ("avatar", "Carlos Henrique Lima", "CL", "CPF 321.***.***-77"),
         "Servidor CMR", ("badge", "Presente", "abertas"), ("badge", "Presente", "abertas"),
         ("prog", 100, "100%"), ("badge", "Apto", "abertas")],
        [("check", True), ("avatar", "Fernanda Duarte Melo", "FM", "CPF 654.***.***-10"),
         "Público externo", ("badge", "Falta", "esgotado"), ("badge", "Presente", "abertas"),
         ("prog", 50, "50%"), ("badge", "Inapto", "esgotado")],
        [("check", True), ("avatar", "Juliana Ferreira Souza", "JS", "CPF 111.***.***-44"),
         "Servidora CMR", ("badge", "Presente", "abertas"), ("badge", "Presente", "abertas"),
         ("prog", 100, "100%"), ("badge", "Apto", "abertas")]], 74)
    c += s
    y += 32
    cwid = (CWA - 20) / 2.0
    s, _ = alert(CX, y, cwid, "Como a frequência é lançada",
                 "O gestor marca presença por encontro. O sistema calcula o percentual sobre a carga "
                 "horária total e define quem está apto ao certificado.", "info")
    c += s
    s, _ = alert(CX + cwid + 20, y, cwid, "Importação da lista de presença",
                 "Para cursos presenciais é possível imprimir a lista assinada e depois lançar as "
                 "presenças em lote nesta tela.", "ok")
    c += s
    y += alert_h(cwid, "O gestor marca presença por encontro. O sistema calcula o percentual sobre a "
                       "carga horária total e define quem está apto ao certificado.")
    return wrap_admin("46-gestor-frequencia", "Frequência", "Controle de frequência",
                      "Lançamento de presença por encontro", ["Painel", "Cursos", "Frequência"],
                      None, c, y, ["RF 14"],
                      ["RF 14 - Confirmar o percentual mínimo de frequência para emissão do certificado "
                       "(proposta: 75%) e se haverá avaliação além da presença."],
                      "RF 14 - Controle de frequência por encontro, com cálculo automático do "
                      "percentual e indicação de quem está apto ao certificado.")


# ================================================================ 47 CERTIFICADOS
@reg
def t47():
    c = ""
    y = Y0
    stats = [("Aptos ao certificado", "26", GREEN), ("Inaptos", "4", RED),
             ("Já emitidos", "0", BLUE), ("Total da turma", "30", NAVY)]
    sw = (CWA - 3 * 20) / 4.0
    for i, (l, v, tn) in enumerate(stats):
        c += rect(CX + i * (sw + 20), y, sw, 96, WHITE, BORDER, 10, 1.2)
        c += rect(CX + i * (sw + 20), y, 5, 96, tn, None, 3)
        c += txt(CX + i * (sw + 20) + 24, y + 44, v, 26, INK, True)
        c += txt(CX + i * (sw + 20) + 24, y + 68, l, 12.5, MUTED)
    y += 96 + 24
    c += rect(CX, y, CWA, 104, WHITE, BORDER, 10, 1.2)
    c += rect(CX, y, 6, 104, PURPLE, None, 3)
    c += txt(CX + 28, y + 42, "Controle Interno e Prestação de Contas", 19, INK, True)
    c += txt(CX + 28, y + 66, "Turma única · encerrada em 13/05/2026 · frequência lançada em 15/05/2026",
             13, MUTED)
    c += btn(CX + CWA - 28 - 230, y + 32, 230, 42, "Emitir 26 certificados", "primary", 13.5, "cert", hot=True)
    y += 104 + 24
    lw = 700
    rx = CX + lw + 20
    rw = CWA - lw - 20
    s, ly = table(CX, y, lw, [
        ("", 46, "start"), ("Aluno", 250, "start"), ("Frequência", 120, "middle"),
        ("Situação", 130, "middle"), ("Código gerado", 130, "end")], [
        [("check", True), ("avatar", "Maria Silva dos Santos", "MS", "Servidora CMR"),
         "100%", ("badge", "Apto", "abertas"), ("mono", "ao emitir")],
        [("check", True), ("avatar", "João Pedro Albuquerque", "JA", "Outro órgão"),
         "100%", ("badge", "Apto", "abertas"), ("mono", "ao emitir")],
        [("check", False), ("avatar", "Ana Beatriz Correia", "AC", "Público externo"),
         "50%", ("badge", "Inapto", "esgotado"), "-"],
        [("check", True), ("avatar", "Carlos Henrique Lima", "CL", "Servidor CMR"),
         "100%", ("badge", "Apto", "abertas"), ("mono", "ao emitir")],
        [("check", False), ("avatar", "Fernanda Duarte Melo", "FM", "Público externo"),
         "50%", ("badge", "Inapto", "esgotado"), "-"],
        [("check", True), ("avatar", "Juliana Ferreira Souza", "JS", "Servidora CMR"),
         "100%", ("badge", "Apto", "abertas"), ("mono", "ao emitir")]], 70)
    c += s

    ry = y
    c += rect(rx, ry, rw, 330, WHITE, BORDER, 10, 1.2)
    c += txt(rx + 22, ry + 44, "O que acontece ao emitir", 17, INK, True)
    passos = [("Gera o código único", "Código alfanumérico exclusivo por documento."),
              ("Monta o PDF", "Com nome, curso, carga horária e data de conclusão."),
              ("Imprime o código no rodapé", "Junto à URL da página pública de validação."),
              ("Libera na Área do Aluno", "O aluno recebe aviso por e-mail e baixa o PDF.")]
    for i, (t, d) in enumerate(passos):
        yy = ry + 76 + i * 62
        c += circ(rx + 34, yy + 8, 13, PURPLE_L)
        c += ctext(rx + 34, yy + 8, str(i + 1), 12, PURPLE, True)
        if i < 3:
            c += line(rx + 34, yy + 22, rx + 34, yy + 50, BORDER2, 1.4)
        c += txt(rx + 58, yy + 4, t, 13.5, INK, True)
        c += para(rx + 58, yy + 24, d, rw - 96, 12, MUTED, 16)
    ry += 330 + 20
    c += rect(rx, ry, rw, 244, WHITE, BORDER, 10, 1.2)
    c += txt(rx + 22, ry + 44, "Modelo do certificado", 17, INK, True)
    c += rect(rx + 22, ry + 66, rw - 44, 116, "#F7FAFC", BORDER2, 6, 1.2)
    c += ctext(rx + rw / 2.0, ry + 100, "CERTIFICADO", 14, NAVY, True)
    c += line(rx + 60, ry + 116, rx + rw - 60, ry + 116, "#E7D2A4", 1)
    c += rect(rx + 44, ry + 140, rw - 88, 26, GOLD_L, "#E7D2A4", 4, 1.1)
    c += ctext(rx + rw / 2.0, ry + 153, "ELCMR-2026-XXXX-XXXX-XXXX", 10.5, "#8A6414", True)
    c += btn(rx + 22, ry + 194, rw - 44, 38, "Editar modelo do certificado", "ghost", 13, to="21")
    ry += 244
    y = max(ly, ry) + 32
    s, y = alert(CX, y, CWA, "Segunda via e cancelamento",
                 "O gestor pode reemitir um certificado (mantendo o mesmo código) ou invalidar um "
                 "documento emitido por engano; nesse caso a validação pública passa a informar que o "
                 "certificado foi cancelado.", "warn")
    c += s
    return wrap_admin("47-gestor-certificados-emissao", "Certificados", "Emissão de certificados",
                      "Geração dos certificados e dos códigos de autenticidade",
                      ["Painel", "Certificados"], None, c, y, ["RF 4", "RF 15"],
                      ["RF 4 - Definir o formato impresso no PDF: apenas código (Opção 1) ou código + "
                       "QR Code (Opção 2). Ver telas 20 e 21."],
                      "RF 15 - Emissão em lote dos certificados dos alunos aptos, com geração "
                      "automática do código identificador único e exclusivo de cada documento.")


# ================================================================ 48 PROFESSORES
@reg
def t48():
    c = ""
    y = Y0
    c += rect(CX, y, CWA, 88, WHITE, BORDER, 10, 1.2)
    c += rect(CX + 20, y + 24, 360, 40, WHITE, BORDER2, 6, 1.3)
    c += icon("search", CX + 32, y + 35, 17, FAINT, 1.7)
    c += txt(CX + 58, y + 49, "Buscar professor por nome ou CPF", 13, FAINT)
    for i, (l, wd) in enumerate([("Situação: ativos", 190), ("Área: todas", 180)]):
        x = CX + 400 + i * 206
        c += rect(x, y + 24, wd, 40, "#F7FAFC", BORDER2, 6, 1.3)
        c += txt(x + 12, y + 49, l, 13, TXT)
        c += icon("chev-d", x + wd - 28, y + 35, 17, MUTED, 1.8)
    c += btn(CX + CWA - 20 - 170, y + 24, 170, 40, "Novo professor", "primary", 13.5, "plus")
    y += 88 + 24
    s, y = table(CX, y, CWA, [
        ("Professor", 300, "start"), ("Área de atuação", 210, "start"), ("Cursos vinculados", 170, "start"),
        ("Acesso ao portal", 170, "middle"), ("Situação", 120, "middle"), ("Ações", 130, "end")], [
        [("avatar", "Dra. Helena Vasconcelos", "HV", "helena.v@recife.pe.leg.br"), "Processo Legislativo",
         ("two", "3 cursos", "12 turmas"), ("badge", "Liberado", "abertas"), ("badge", "Ativo", "abertas"),
         ("icons", [("edit", MUTED), ("book", BLUE), ("trash", RED)])],
        [("avatar", "Prof. Marcelo Andrade", "MA", "marcelo.a@recife.pe.leg.br"), "Direito Administrativo",
         ("two", "2 cursos", "4 turmas"), ("badge", "Liberado", "abertas"), ("badge", "Ativo", "abertas"),
         ("icons", [("edit", MUTED), ("book", BLUE), ("trash", RED)])],
        [("avatar", "Prof. Diego Farias", "DF", "diego.f@recife.pe.leg.br"), "Tecnologia",
         ("two", "1 curso", "1 turma"), ("badge", "Liberado", "abertas"), ("badge", "Ativo", "abertas"),
         ("icons", [("edit", MUTED), ("book", BLUE), ("trash", RED)])],
        [("avatar", "Profa. Cláudia Nunes", "CN", "claudia.n@recife.pe.leg.br"), "Redação Oficial",
         ("two", "2 cursos", "5 turmas"), ("badge", "Liberado", "abertas"), ("badge", "Ativo", "abertas"),
         ("icons", [("edit", MUTED), ("book", BLUE), ("trash", RED)])],
        [("avatar", "Dr. Paulo Meneses", "PM", "convidado externo"), "Orçamento Público",
         ("two", "1 curso", "2 turmas"), ("badge", "Pendente", "breve"), ("badge", "Ativo", "abertas"),
         ("icons", [("edit", MUTED), ("book", BLUE), ("trash", RED)])],
        [("avatar", "Dr. Sérgio Batista", "SB", "convidado externo"), "Controle Interno",
         ("two", "1 curso", "1 turma"), ("badge", "Revogado", "encerradas"), ("badge", "Inativo", "encerradas"),
         ("icons", [("edit", MUTED), ("book", BLUE), ("trash", RED)])]], 74)
    c += s
    y += 32
    lw = 700
    rx = CX + lw + 20
    rw = CWA - lw - 20
    c += rect(CX, y, lw, 396, WHITE, BORDER, 10, 1.2)
    c += txt(CX + 28, y + 46, "Cadastrar professor", 19, INK, True)
    fy = y + 78
    hw = (lw - 56 - 18) / 2.0
    s, _ = field(CX + 28, fy, hw, "Nome completo", "Dra. Helena Vasconcelos", req=True)
    c += s
    s, _ = field(CX + 28 + hw + 18, fy, hw, "CPF", "111.222.333-44", req=True)
    c += s
    fy += 88
    s, _ = field(CX + 28, fy, hw, "E-mail (login do professor)", "helena.v@recife.pe.leg.br",
                 req=True, ic="mail")
    c += s
    s, _ = field(CX + 28 + hw + 18, fy, hw, "Área de atuação", "Processo Legislativo", req=True, kind="select")
    c += s
    fy += 88
    s, _ = textarea(CX + 28, fy, lw - 56, "Biografia resumida (exibida na página do curso)",
                    "Procuradora Legislativa, mestre em Direito Público pela UFPE, atua há 16 anos na "
                    "Câmara Municipal do Recife.", 84)
    c += s
    fy += 116
    c += btn(CX + 28, fy, 190, 46, "Salvar professor", "primary", 14.5)
    c += btn(CX + 232, fy, 130, 46, "Cancelar", "ghost", 14.5)
    ly = y + 396

    ry = y
    c += rect(rx, ry, rw, 300, WHITE, BORDER, 10, 1.2)
    c += txt(rx + 22, ry + 44, "Permissões do professor", 17, INK, True)
    c += txt(rx + 22, ry + 64, "Acesso restrito, conforme o documento", 12, MUTED)
    perms = [("Ver a lista de alunos inscritos", True),
             ("Enviar materiais dos cursos vinculados", True),
             ("Ver os próprios cursos e turmas", True),
             ("Lançar frequência", False),
             ("Emitir certificados", False),
             ("Editar cursos e turmas", False),
             ("Publicar notícias e acervo", False)]
    for i, (t, on) in enumerate(perms):
        yy = ry + 90 + i * 28
        c += circ(rx + 30, yy, 8, GREEN_L if on else RED_L)
        if on:
            c += path("M%s %s l2.6 2.8 L%s %s" % (n(rx + 26), n(yy), n(rx + 34), n(yy - 5)), None, GREEN, 2)
        else:
            c += path("M%s %s L%s %s M%s %s L%s %s" % (n(rx + 27), n(yy - 3), n(rx + 33), n(yy + 3),
                                                       n(rx + 33), n(yy - 3), n(rx + 27), n(yy + 3)),
                      None, RED, 1.8)
        c += txt(rx + 48, yy + 4, t, 12.5, TXT if on else MUTED)
    ry += 300 + 20
    c += rect(rx, ry, rw, 190, WHITE, BORDER, 10, 1.2)
    c += txt(rx + 22, ry + 44, "Vincular a cursos", 17, INK, True)
    for i, t in enumerate(["Processo Legislativo Municipal", "Introdução ao Direito Municipal"]):
        c += checkbox(rx + 22, ry + 68 + i * 34, "", True)
        c += para(rx + 50, ry + 82 + i * 34, t, rw - 90, 12.5, TXT, 16, maxlines=1)
    c += btn(rx + 22, ry + 138, rw - 44, 38, "Gerenciar vínculos", "ghost", 13)
    ry += 190
    return wrap_admin("48-gestor-professores", "Professores", "Gestão de professores",
                      "Cadastro, permissões e vínculo com cursos", ["Painel", "Professores"],
                      None, c, max(ly, ry), ["RF 16"], None,
                      "RF 16 - Gestão de professores, com o acesso restrito previsto no documento: ver "
                      "a lista de alunos inscritos e fazer upload de materiais apenas dos cursos "
                      "vinculados a ele.")


# ================================================================ 49-51 CONTEUDO
def _conteudo(nome, aba, titulo, sub, corpo, cend, rfs, obs, dec=None):
    c = ""
    y = Y0
    s2, cx2 = pills(CX, y, ["Notícias", "Acervo / Biblioteca", "Escolas parceiras e páginas"], aba, 40)
    c += s2
    y += 40 + 24
    c += corpo(y)[0]
    return wrap_admin(nome, "Conteúdo do portal", titulo, sub, ["Painel", "Conteúdo do portal"],
                      None, c, cend, rfs, dec, obs)


@reg
def t49():
    y0 = Y0 + 64
    c = ""
    s2, _ = pills(CX, Y0, ["Notícias", "Acervo / Biblioteca", "Escolas parceiras e páginas"], 0,
                  40, to=["49", "50", "51"])
    c += s2
    y = y0
    c += rect(CX, y, CWA, 88, WHITE, BORDER, 10, 1.2)
    c += rect(CX + 20, y + 24, 360, 40, WHITE, BORDER2, 6, 1.3)
    c += icon("search", CX + 32, y + 35, 17, FAINT, 1.7)
    c += txt(CX + 58, y + 49, "Buscar notícia por título", 13, FAINT)
    for i, (l, wd) in enumerate([("Categoria: todas", 200), ("Situação: todas", 180)]):
        x = CX + 400 + i * 216
        c += rect(x, y + 24, wd, 40, "#F7FAFC", BORDER2, 6, 1.3)
        c += txt(x + 12, y + 49, l, 13, TXT)
        c += icon("chev-d", x + wd - 28, y + 35, 17, MUTED, 1.8)
    c += btn(CX + CWA - 20 - 160, y + 24, 160, 40, "Nova notícia", "primary", 13.5, "plus")
    y += 88 + 24
    s, y = table(CX, y, CWA, [
        ("Título", 400, "start"), ("Categoria", 160, "start"), ("Publicação", 150, "start"),
        ("Destaque na home", 180, "middle"), ("Situação", 130, "middle"), ("Ações", 110, "end")], [
        [("two", "Escola firma parceria com a ALMG", "por Assessoria da Escola"), "Parcerias",
         "12/08/2026", ("badge", "Em destaque", "gold"), ("badge", "Publicada", "abertas"),
         ("icons", [("edit", MUTED), ("trash", RED)])],
        [("two", "Agenda do 2º semestre já disponível", "por C. Nunes"), "Agenda",
         "05/08/2026", ("badge", "Em destaque", "gold"), ("badge", "Publicada", "abertas"),
         ("icons", [("edit", MUTED), ("trash", RED)])],
        [("two", "Novas publicações no acervo digital", "por C. Nunes"), "Acervo",
         "28/07/2026", ("badge", "Em destaque", "gold"), ("badge", "Publicada", "abertas"),
         ("icons", [("edit", MUTED), ("trash", RED)])],
        [("two", "Turma de Redação Oficial forma 25 servidores", "por Assessoria"), "Cursos",
         "20/07/2026", ("badge", "Não", "encerradas"), ("badge", "Publicada", "abertas"),
         ("icons", [("edit", MUTED), ("trash", RED)])],
        [("two", "Escola recebe visita da Câmara de Olinda", "por R. Barros"), "Institucional",
         "11/07/2026", ("badge", "Não", "encerradas"), ("badge", "Publicada", "abertas"),
         ("icons", [("edit", MUTED), ("trash", RED)])],
        [("two", "Balanço do 1º semestre de 2026", "rascunho"), "Institucional",
         "-", ("badge", "Não", "encerradas"), ("badge", "Rascunho", "breve"),
         ("icons", [("edit", MUTED), ("trash", RED)])]], 70)
    c += s
    y += 32
    lw = 700
    rx = CX + lw + 20
    rw = CWA - lw - 20
    c += rect(CX, y, lw, 468, WHITE, BORDER, 10, 1.2)
    c += txt(CX + 28, y + 46, "Nova notícia", 19, INK, True)
    fy = y + 78
    s, _ = field(CX + 28, fy, lw - 56, "Título", "Escola firma parceria com a ALMG", req=True)
    c += s
    fy += 88
    s, _ = textarea(CX + 28, fy, lw - 56, "Resumo (aparece no card da home)",
                    "Acordo de cooperação técnica permite intercâmbio de cursos e material didático.", 76)
    c += s
    fy += 108
    hw = (lw - 56 - 18) / 2.0
    s, _ = field(CX + 28, fy, hw, "Categoria", "Parcerias", req=True, kind="select")
    c += s
    s, _ = field(CX + 28 + hw + 18, fy, hw, "Data de publicação", "12/08/2026", req=True, kind="date")
    c += s
    fy += 88
    c += checkbox(CX + 28, fy, "Destacar esta notícia na página inicial", True,
                  sub="Decisão em reunião: destaque manual pelo gestor ou automático pelas mais recentes.")
    fy += 56
    c += btn(CX + 28, fy, 180, 46, "Publicar notícia", "primary", 14.5)
    c += btn(CX + 222, fy, 170, 46, "Salvar rascunho", "ghost", 14.5)
    ly = y + 468

    ry = y
    c += rect(rx, ry, rw, 300, WHITE, BORDER, 10, 1.2)
    c += txt(rx + 22, ry + 44, "Destaques da home", 17, INK, True)
    c += txt(rx + 22, ry + 64, "Ordem de exibição na página inicial", 12, MUTED)
    for i, t in enumerate(["Escola firma parceria com a ALMG",
                           "Agenda do 2º semestre já disponível",
                           "Novas publicações no acervo digital"]):
        yy = ry + 88 + i * 68
        c += rect(rx + 22, yy, rw - 44, 56, "#F7FAFC", BORDER, 8, 1)
        c += icon("list", rx + 36, yy + 19, 16, FAINT, 1.8)
        c += para(rx + 60, yy + 26, t, rw - 120, 12.5, INK, 16, True, maxlines=2)
        c += circ(rx + rw - 40, yy + 28, 11, GOLD_L)
        c += ctext(rx + rw - 40, yy + 28, str(i + 1), 11.5, "#8A6414", True)
    ry += 300 + 20
    s, ry = alert(rx, ry, rw, "Quantos destaques?",
                  "A home está desenhada para 3 notícias em destaque. O número final depende da decisão "
                  "sobre destaque manual ou automático.", "warn")
    c += s
    return wrap_admin("49-gestor-conteudo-noticias", "Conteúdo do portal", "Conteúdo do portal",
                      "Notícias publicadas no portal da Escola",
                      ["Painel", "Conteúdo do portal", "Notícias"], None, c, max(ly, ry),
                      ["RF 3", "RF 17"],
                      ["RF 3 - As notícias em destaque são marcadas manualmente pelo gestor (como está "
                       "nesta tela) ou o portal exibe automaticamente as N mais recentes por data de "
                       "cadastro?"],
                      "RF 17 - Gestão de conteúdo: cadastro, publicação e destaque das notícias que "
                      "alimentam a home e a página de notícias.")


@reg
def t50():
    c = ""
    s2, _ = pills(CX, Y0, ["Notícias", "Acervo / Biblioteca", "Escolas parceiras e páginas"], 1,
                  40, to=["49", "50", "51"])
    c += s2
    y = Y0 + 64
    lw = 700
    rx = CX + lw + 20
    rw = CWA - lw - 20
    c += rect(CX, y, CWA, 88, WHITE, BORDER, 10, 1.2)
    c += rect(CX + 20, y + 24, 360, 40, WHITE, BORDER2, 6, 1.3)
    c += icon("search", CX + 32, y + 35, 17, FAINT, 1.7)
    c += txt(CX + 58, y + 49, "Buscar no acervo", 13, FAINT)
    s3, _ = pills(CX + 400, y + 24, ["Publicações", "Manuais", "Legislações"], 0, 40)
    c += s3
    c += btn(CX + CWA - 20 - 170, y + 24, 170, 40, "Novo arquivo", "primary", 13.5, "upload")
    y += 88 + 24
    s, y = table(CX, y, CWA, [
        ("Arquivo", 380, "start"), ("Seção", 160, "start"), ("Autor", 180, "start"),
        ("Publicado em", 150, "start"), ("Downloads", 120, "middle"), ("Ações", 110, "end")], [
        [("two", "Manual de Técnica Legislativa - 3ª ed.", "PDF · 4,2 MB"), "Manuais",
         "Helena Vasconcelos", "12/07/2026", "1.248",
         ("icons", [("edit", MUTED), ("trash", RED)])],
        [("two", "Cartilha do Orçamento Público Municipal", "PDF · 1,8 MB"), "Publicações",
         "Paulo Meneses", "20/05/2026", "864",
         ("icons", [("edit", MUTED), ("trash", RED)])],
        [("two", "Coletânea de Legislação Municipal 2026", "PDF · 9,6 MB"), "Legislações",
         "Escola do Legislativo", "14/02/2026", "2.017",
         ("icons", [("edit", MUTED), ("trash", RED)])],
        [("two", "Guia do Vereador Iniciante", "PDF · 2,4 MB"), "Publicações",
         "Escola do Legislativo", "03/11/2025", "1.530",
         ("icons", [("edit", MUTED), ("trash", RED)])],
        [("two", "Revista Legislativo Municipal nº 4", "PDF · 6,1 MB"), "Publicações",
         "Vários autores", "18/09/2025", "742",
         ("icons", [("edit", MUTED), ("trash", RED)])],
        [("two", "Apostila - Redação Oficial na CMR", "DOCX · 1,1 MB"), "Manuais",
         "Cláudia Nunes", "05/08/2025", "998",
         ("icons", [("edit", MUTED), ("trash", RED)])]], 70)
    c += s
    y += 32
    c += rect(CX, y, lw, 350, WHITE, BORDER, 10, 1.2)
    c += txt(CX + 28, y + 46, "Enviar arquivo para o acervo", 19, INK, True)
    fy = y + 78
    hw = (lw - 56 - 18) / 2.0
    s, _ = field(CX + 28, fy, lw - 56, "Título da publicação", "Manual de Técnica Legislativa - 3ª edição",
                 req=True)
    c += s
    fy += 88
    s, _ = field(CX + 28, fy, hw, "Seção do acervo", "Manuais", req=True, kind="select",
                 helper="Publicações / Manuais / Legislações.")
    c += s
    s, _ = field(CX + 28 + hw + 18, fy, hw, "Autor(es)", "Helena Vasconcelos")
    c += s
    fy += 106
    c += rect(CX + 28, fy, lw - 56, 88, "#F7FAFC", BORDER2, 8, 1.4)
    c += icon("upload", CX + 48, fy + 30, 22, BLUE, 1.8)
    c += txt(CX + 82, fy + 38, "Arraste o arquivo ou clique para enviar", 14, BLUE_D, True)
    c += txt(CX + 82, fy + 60, "PDF, DOCX ou XLSX · até 20 MB", 12, MUTED)
    c += btn(CX + lw - 28 - 120, fy + 26, 120, 38, "Selecionar", "secondary", 13)
    ly = y + 350

    ry = y
    c += rect(rx, ry, rw, 350, WHITE, BORDER, 10, 1.2)
    c += txt(rx + 22, ry + 44, "Como o acervo aparece", 17, INK, True)
    c += rect(rx + 22, ry + 68, rw - 44, 46, WHITE, BORDER, 6, 1.2)
    c += rect(rx + 32, ry + 78, 26, 26, RED_L, None, 5)
    c += icon_c("file", rx + 45, ry + 91, 14, RED, 1.7)
    c += para(rx + 66, ry + 88, "Manual de Técnica Legislativa", rw - 130, 11.5, INK, 14, True, maxlines=1)
    c += txt(rx + 66, ry + 102, "PDF · 4,2 MB", 10, MUTED)
    c += para(rx + 22, ry + 138, "Os arquivos ficam disponíveis na seção ACERVO/BIBLIOTECA do portal, "
                                 "separados nas abas Publicações, Manuais e Legislações, com busca por "
                                 "título, autor e assunto.", rw - 44, 12.5, MUTED, 18)
    c += line(rx + 22, ry + 226, rx + rw - 22, ry + 226, "#EDF1F6", 1.2)
    c += txt(rx + 22, ry + 254, "Downloads no mês", 12.5, MUTED, True)
    c += txt(rx + 22, ry + 286, "3.412", 26, INK, True)
    c += txt(rx + 100, ry + 286, "+18% vs. mês anterior", 12, GREEN, True)
    ry += 350
    return wrap_admin("50-gestor-conteudo-acervo", "Conteúdo do portal", "Conteúdo do portal",
                      "Publicações, manuais e legislações do acervo",
                      ["Painel", "Conteúdo do portal", "Acervo"], None, c, max(ly, ry),
                      ["ACERVO/BIBLIOTECA", "RF 17"], None,
                      "RF 17 - Inserção de materiais no acervo pelo Gestor da Escola, distribuídos nas "
                      "três abas previstas na estrutura do portal.")


@reg
def t51():
    c = ""
    s2, _ = pills(CX, Y0, ["Notícias", "Acervo / Biblioteca", "Escolas parceiras e páginas"], 2,
                  40, to=["49", "50", "51"])
    c += s2
    y = Y0 + 64
    s, ny = sec(CX, y, "Escolas do Legislativo parceiras",
                "Links exibidos no portal e na página de parcerias", CWA)
    c += s
    c += btn(CX + CWA - 180, y - 12, 180, 40, "Nova parceira", "primary", 13.5, "plus")
    s, y = table(CX, ny + 20, CWA, [
        ("Escola", 330, "start"), ("Endereço do site", 280, "start"),
        ("Instrumento formalizado", 250, "start"), ("Situação", 130, "middle"), ("Ações", 110, "end")],
        [[("two", p[0], p[1]), p[2], p[3],
          ("badge", "Vigente" if i < 5 else "Encerrado", "abertas" if i < 5 else "encerradas"),
          ("icons", [("edit", MUTED), ("trash", RED)])] for i, p in enumerate(PARCEIRAS)], 66)
    c += s
    y += 32
    s, ny = sec(CX, y, "Instrumentos jurídicos formalizados",
                "Alimentam a página Legislação e Transparência", CWA)
    c += s
    c += btn(CX + CWA - 210, y - 12, 210, 40, "Novo instrumento", "primary", 13.5, "plus")
    s, y = table(CX, ny + 20, CWA, [
        ("Instrumento", 300, "start"), ("Partícipe", 240, "start"), ("Objeto", 260, "start"),
        ("Vigência", 190, "start"), ("Arquivo", 110, "end")], [
        [("two", "Acordo de Cooperação nº 04/2026", "assinado em 10/08/2026"), "ALMG - Minas Gerais",
         "Intercâmbio de cursos", ("two", "10/08/2026", "até 09/08/2028"),
         ("icons", [("file", RED), ("edit", MUTED)])],
        [("two", "Termo de Adesão nº 11/2025", "Programa Interlegis"), "ILB / Senado Federal",
         "Uso da plataforma Saberes", ("two", "02/2025", "indeterminada"),
         ("icons", [("file", RED), ("edit", MUTED)])],
        [("two", "Convênio nº 22/2025", "capacitação conjunta"), "ALEPE - Pernambuco",
         "Oferta compartilhada de turmas", ("two", "05/2025", "até 04/2027"),
         ("icons", [("file", RED), ("edit", MUTED)])]], 66)
    c += s
    y += 32
    s, ny = sec(CX, y, "Páginas institucionais", "Conteúdo das seções A ESCOLA e CONTATO", CWA)
    c += s
    y = ny + 20
    pgs = [("Quem Somos", "Missão, competências e composição da Escola", "Atualizada em 02/08/2026", "users"),
           ("História", "Linha do tempo e marcos institucionais", "Atualizada em 12/06/2026", "book"),
           ("Legislação e Transparência", "Normas e instrumentos jurídicos", "Atualizada em 12/08/2026", "shield"),
           ("Contato", "E-mail, endereço, telefone e horário", "Atualizada em 15/03/2026", "phone")]
    cwid = (CWA - 3 * 20) / 4.0
    for i, (t, d, m, ic) in enumerate(pgs):
        x = CX + i * (cwid + 20)
        c += rect(x, y, cwid, 176, WHITE, BORDER, 10, 1.2)
        c += rect(x + 20, y + 20, 40, 40, BLUE_L, None, 8)
        c += icon_c(ic, x + 40, y + 40, 20, BLUE, 1.8)
        c += txt(x + 20, y + 88, t, 15, INK, True)
        c += para(x + 20, y + 108, d, cwid - 40, 12, MUTED, 16, maxlines=2)
        c += txt(x + 20, y + 148, m, 11, FAINT)
        c += btn(x + cwid - 20 - 76, y + 132, 76, 30, "Editar", "ghost", 12, rx=5)
    y += 176
    return wrap_admin("51-gestor-conteudo-parceiras-e-paginas", "Conteúdo do portal",
                      "Conteúdo do portal", "Escolas parceiras, instrumentos jurídicos e páginas",
                      ["Painel", "Conteúdo do portal", "Parceiras e páginas"], None, c, y,
                      ["RF 17", "Escolas parceiras", "Instrumentos jurídicos"], None,
                      "RF 17 - Manutenção das informações do portal pelo Gestor: links das escolas "
                      "parceiras, lista de instrumentos jurídicos formalizados e páginas institucionais.")


# ================================================================ 52 RELATORIOS
@reg
def t52():
    c = ""
    y = Y0
    c += rect(CX, y, CWA, 100, WHITE, BORDER, 10, 1.2)
    for i, (l, v, wd) in enumerate([("Período", "01/01/2026 a 19/08/2026", 260),
                                    ("Curso", "Todos os cursos", 240),
                                    ("Tipo de vínculo", "Todos", 200)]):
        x = CX + 24 + [0, 276, 532][i]
        c += txt(x, y + 34, l, 12, MUTED, True)
        c += rect(x, y + 42, wd, 40, WHITE, BORDER2, 6, 1.3)
        c += txt(x + 12, y + 67, v, 13, TXT)
        c += icon("chev-d", x + wd - 28, y + 53, 17, MUTED, 1.8)
    c += btn(CX + CWA - 24 - 120, y + 42, 120, 40, "Gerar", "primary", 13.5)
    c += btn(CX + CWA - 24 - 120 - 140, y + 42, 130, 40, "Exportar", "ghost", 13.5, "download")
    y += 100 + 24
    stats = [("Inscrições no período", "1.284", "+22% vs. 2025", "list", BLUE, BLUE_L),
             ("Taxa de comparecimento", "82%", "meta: 80%", "check", GREEN, GREEN_L),
             ("Certificados emitidos", "946", "em 23 turmas", "cert", PURPLE, PURPLE_L),
             ("Cancelamentos", "97", "7,5% das inscrições", "close", RED, RED_L)]
    sw = (CWA - 3 * 20) / 4.0
    for i, (l, v, s2, ic, tn, tl) in enumerate(stats):
        c += stat(CX + i * (sw + 20), y, sw, 164, l, v, s2, ic, tn, tl)
    y += 164 + 24
    lw = 700
    rx = CX + lw + 20
    rw = CWA - lw - 20
    c += rect(CX, y, lw, 320, WHITE, BORDER, 10, 1.2)
    c += txt(CX + 24, y + 42, "Inscrições por mês", 17, INK, True)
    vals = [88, 124, 96, 152, 118, 143, 167, 189]
    meses = ["JAN", "FEV", "MAR", "ABR", "MAI", "JUN", "JUL", "AGO"]
    bw = (lw - 80) / 8.0
    for i, v in enumerate(vals):
        h = v * 0.92
        c += rect(CX + 44 + i * bw, y + 260 - h, bw - 16, h, BLUE if i < 7 else GOLD, None, 4)
        c += ctext(CX + 44 + (bw - 16) / 2.0 + i * bw, y + 250 - h, str(v), 11, MUTED, True)
        c += ctext(CX + 44 + (bw - 16) / 2.0 + i * bw, y + 282, meses[i], 11, MUTED)
    c += line(CX + 30, y + 264, CX + lw - 30, y + 264, BORDER, 1.2)
    ly = y + 320 + 24
    s, ly = table(CX, ly, lw, [
        ("Curso", 260, "start"), ("Turmas", 90, "middle"), ("Inscritos", 100, "middle"),
        ("Presença", 120, "middle"), ("Certificados", 110, "end")], [
        ["Processo Legislativo Municipal", "3", "59", "88%", "42"],
        ["Redação Oficial e Técnica Legislativa", "2", "41", "91%", "38"],
        ["Orçamento Público e LOA Municipal", "2", "56", "76%", "40"],
        ["Controle Interno e Prestação de Contas", "1", "30", "83%", "26"],
        ["Audiências Públicas e Participação Cidadã", "1", "80", "72%", "58"]], 58)
    c += s

    ry = y
    c += rect(rx, ry, rw, 330, WHITE, BORDER, 10, 1.2)
    c += txt(rx + 22, ry + 42, "Público atendido", 17, INK, True)
    pub = [("Servidores da CMR", 52, BLUE), ("Servidores de outros órgãos", 27, GREEN),
           ("Público externo", 21, GOLD)]
    cx0, cy0, r = rx + rw / 2.0, ry + 140, 62
    ang = -90
    for l, p, col in pub:
        c += path("M%s %s L%s %s A%s %s 0 %s 1 %s %s Z" % (
            n(cx0), n(cy0),
            n(cx0 + r * math.cos(math.radians(ang))),
            n(cy0 + r * math.sin(math.radians(ang))),
            n(r), n(r), 1 if p > 50 else 0,
            n(cx0 + r * math.cos(math.radians(ang + p * 3.6))),
            n(cy0 + r * math.sin(math.radians(ang + p * 3.6)))), col)
        ang += p * 3.6
    c += circ(cx0, cy0, 34, WHITE)
    c += ctext(cx0, cy0 - 6, "1.284", 18, INK, True)
    c += ctext(cx0, cy0 + 14, "inscrições", 10.5, MUTED)
    for i, (l, p, col) in enumerate(pub):
        yy = ry + 232 + i * 30
        c += rect(rx + 24, yy, 12, 12, col, None, 3)
        c += txt(rx + 44, yy + 11, l, 12.5, TXT)
        c += txt(rx + rw - 24, yy + 11, "%d%%" % p, 12.5, INK, True, anchor="end")
    ry += 330 + 20
    c += rect(rx, ry, rw, 240, WHITE, BORDER, 10, 1.2)
    c += txt(rx + 22, ry + 42, "Relatórios prontos", 17, INK, True)
    for i, t in enumerate(["Lista de presença por turma", "Inscritos por curso (CSV)",
                           "Certificados emitidos no período", "Log de cancelamentos"]):
        yy = ry + 66 + i * 42
        c += icon("file", rx + 24, yy, 17, BLUE, 1.7)
        c += para(rx + 48, yy + 13, t, rw - 120, 12.5, TXT, 16, maxlines=1)
        c += icon("download", rx + rw - 40, yy, 17, BLUE_D, 1.8)
    ry += 240
    return wrap_admin("52-gestor-relatorios", "Relatórios", "Relatórios e indicadores",
                      "Acompanhamento das capacitações da Escola", ["Painel", "Relatórios"],
                      None, c, max(ly, ry), ["RF 12", "RF 13", "RF 14", "RF 15"], None,
                      "Apoio à gestão: consolida inscrições, presença, certificados e cancelamentos, "
                      "substituindo os controles manuais citados na contextualização do projeto.")
