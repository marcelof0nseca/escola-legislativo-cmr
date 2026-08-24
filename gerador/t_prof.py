# -*- coding: utf-8 -*-
"""Telas 53-55: Area do Professor (acesso restrito)."""
from blocks import *
from t_gestor import wrap_admin, sec, CX, CWA, Y0

TELAS = []
PROF = ("Helena Vasconcelos", "Professora", "HV")


def reg(fn):
    TELAS.append(fn)
    return fn


def wrap_prof(nome, active, titulo, sub, crumbs, actions, c, cend, rfs, dec=None, obs=None, extra=""):
    return wrap_admin(nome, active, titulo, sub, crumbs, actions, c, cend, rfs, dec, obs,
                      menu=MENU_PROF, papel="ÁREA DO PROFESSOR", user=PROF, extra=extra)


# ================================================================ 53 PAINEL
@reg
def t53():
    c = ""
    y = Y0
    c += rect(CX, y, CWA, 116, NAVY, None, 10)
    c += rect(CX, y, 6, 116, GOLD, None, 3)
    c += avatar(CX + 28, y + 30, 56, "HV", NAVY_3)
    c += txt(CX + 100, y + 54, "Olá, Dra. Helena Vasconcelos", 22, WHITE, True)
    c += txt(CX + 100, y + 80, "Procuradora Legislativa · Processo Legislativo e Direito Municipal",
             13.5, "#B7C7D6")
    c += badge(CX + CWA - 28 - badge_w("Acesso restrito"), y + 44, "Acesso restrito", "gold", 12, 28)[0]
    y += 116 + 24
    stats = [("Cursos vinculados", "3", "1 em andamento", "book", BLUE, BLUE_L),
             ("Turmas ativas", "2", "próxima em 14/09", "users", GREEN, GREEN_L),
             ("Alunos inscritos", "59", "nas turmas ativas", "user", GOLD, GOLD_L),
             ("Materiais enviados", "12", "4 aguardando revisão", "folder", PURPLE, PURPLE_L)]
    sw = (CWA - 3 * 20) / 4.0
    for i, (l, v, s2, ic, tn, tl) in enumerate(stats):
        c += stat(CX + i * (sw + 20), y, sw, 164, l, v, s2, ic, tn, tl)
    y += 164 + 32
    s, ny = sec(CX, y, "Meus cursos vinculados",
                "Você só tem acesso aos cursos em que está vinculada como professora", CWA)
    c += s
    y = ny + 16
    cursos = [("Processo Legislativo Municipal", "8 horas · Online e Presencial",
               [("Turma A - Manhã", "14 e 15/09/2026 · 09h às 12h", "6/30", "Confirmada"),
                ("Turma B - Noite", "14 e 15/09/2026 · 19h às 22h", "18/30", "Confirmada")], "abertas"),
              ("Introdução ao Direito Municipal", "15 horas · Presencial",
               [("Turma A", "03 a 07/03/2026 · 19h às 22h", "25/25", "Encerrada")], "encerradas")]
    for t, meta, turmas, k in cursos:
        h = 96 + len(turmas) * 62
        c += rect(CX, y, CWA, h, WHITE, BORDER, 10, 1.2)
        c += rect(CX + 24, y + 24, 44, 44, BLUE_L, None, 8)
        c += icon_c("book", CX + 46, y + 46, 22, BLUE, 1.8)
        c += txt(CX + 84, y + 42, t, 18, INK, True)
        c += txt(CX + 84, y + 64, meta, 13, MUTED)
        c += badge(CX + CWA - 24 - badge_w("Em andamento" if k == "abertas" else "Encerrado"),
                   y + 32, "Em andamento" if k == "abertas" else "Encerrado", k)[0]
        for i, (tn2, td, tv, ts) in enumerate(turmas):
            yy = y + 88 + i * 62
            c += line(CX + 24, yy, CX + CWA - 24, yy, "#EDF1F6", 1.2)
            c += icon("users", CX + 30, yy + 18, 17, MUTED, 1.7)
            c += txt(CX + 58, yy + 26, tn2, 14.5, INK, True)
            c += txt(CX + 200, yy + 26, td, 13, MUTED)
            c += txt(CX + 480, yy + 26, tv + " inscritos", 13, TXT, True)
            c += btn(CX + CWA - 24 - 150, yy + 12, 150, 36, "Ver alunos", "secondary", 12.5,
                     to="54")
            c += btn(CX + CWA - 24 - 150 - 140, yy + 12, 130, 36, "Materiais", "ghost", 12.5,
                     to="55")
        y += h + 20
    y += 12
    s, y = alert(CX, y, CWA, "O que o professor pode fazer no portal",
                 "Conforme definido no documento de requisitos, o acesso do professor é restrito a "
                 "consultar a lista de alunos inscritos e enviar materiais para os cursos vinculados a "
                 "ele. Frequência, certificados e cadastros são de responsabilidade do Gestor da Escola.",
                 "info")
    c += s
    return wrap_prof("53-professor-painel", "Painel", "Painel do Professor",
                     "Cursos e turmas vinculados a você", None, None, c, y,
                     ["ÁREA DO PROFESSOR", "RF 16"], None,
                     "Painel do professor com os cursos vinculados e atalhos para a lista de alunos e "
                     "para o envio de materiais.")


# ================================================================ 54 ALUNOS
@reg
def t54():
    c = ""
    y = Y0
    c += rect(CX, y, CWA, 104, WHITE, BORDER, 10, 1.2)
    c += rect(CX, y, 6, 104, BLUE, None, 3)
    c += txt(CX + 28, y + 42, "Processo Legislativo Municipal", 19, INK, True)
    c += txt(CX + 28, y + 66, "Turma B - Noite · 14 e 15/09/2026 · 19h às 22h · Online · 18 inscritos",
             13, MUTED)
    c += btn(CX + CWA - 28 - 160, y + 32, 160, 42, "Imprimir lista", "ghost", 13.5, "print")
    y += 104 + 24
    c += rect(CX, y, CWA, 76, WHITE, BORDER, 10, 1.2)
    s2, _ = pills(CX + 20, y + 18, ["Turma A - Manhã (6)", "Turma B - Noite (18)", "Turma C - Tarde (35)"], 1, 40)
    c += s2
    c += rect(CX + CWA - 20 - 260, y + 18, 260, 40, WHITE, BORDER2, 6, 1.3)
    c += icon("search", CX + CWA - 20 - 248, y + 29, 17, FAINT, 1.7)
    c += txt(CX + CWA - 20 - 222, y + 43, "Buscar aluno", 13, FAINT)
    y += 76 + 24
    alunos = [("Maria Silva dos Santos", "MS", "Servidora CMR", "Confirmada", "abertas"),
              ("João Pedro Albuquerque", "JA", "Servidor de outro órgão", "Confirmada", "abertas"),
              ("Ana Beatriz Correia", "AC", "Público externo", "Confirmada", "abertas"),
              ("Carlos Henrique Lima", "CL", "Servidor CMR", "Confirmada", "abertas"),
              ("Fernanda Duarte Melo", "FM", "Público externo", "Confirmada", "abertas"),
              ("Juliana Ferreira Souza", "JS", "Servidora CMR", "Confirmada", "abertas"),
              ("Paulo Ricardo Nunes", "PN", "Servidor de outro órgão", "Confirmada", "abertas"),
              ("Marcos Vinícius Gomes", "MG", "Público externo", "Confirmada", "abertas")]
    rows = [[("bold", str(i + 1)),
             ("avatar", a[0], a[1], a[2]),
             "***@email.com", "Turma B - Noite",
             ("badge", a[3], a[4])] for i, a in enumerate(alunos)]
    s, y = table(CX, y, CWA, [
        ("#", 60, "middle"), ("Aluno", 380, "start"), ("Contato", 240, "start"),
        ("Turma", 220, "start"), ("Situação", 200, "end")], rows, 70)
    c += s
    y += 32
    cwid = (CWA - 20) / 2.0
    s, _ = alert(CX, y, cwid, "Dados protegidos (LGPD)",
                 "O professor vê apenas o necessário para conduzir a turma. CPF, telefone e e-mail "
                 "completo dos alunos não são exibidos nesta lista.", "lgpd")
    c += s
    s, _ = alert(CX + cwid + 20, y, cwid, "Frequência é do gestor",
                 "O lançamento de presença e a emissão de certificados são feitos pelo Gestor da "
                 "Escola. O professor pode imprimir a lista para colher assinaturas.", "info")
    c += s
    y += alert_h(cwid, "O professor vê apenas o necessário para conduzir a turma. CPF, telefone e "
                       "e-mail completo dos alunos não são exibidos nesta lista.")
    return wrap_prof("54-professor-alunos-inscritos", "Alunos inscritos", "Alunos inscritos",
                     "Consulta da lista de alunos das turmas vinculadas",
                     ["Painel", "Meus cursos", "Alunos inscritos"], None, c, y,
                     ["ÁREA DO PROFESSOR", "RF 16"], None,
                     "Consulta da lista de alunos inscritos, prevista na estrutura do portal para a "
                     "ÁREA DO PROFESSOR, restrita às turmas vinculadas ao professor.")


# ================================================================ 55 MATERIAIS
@reg
def t55():
    c = ""
    y = Y0
    lw = 700
    rx = CX + lw + 20
    rw = CWA - lw - 20
    c += rect(CX, y, CWA, 104, WHITE, BORDER, 10, 1.2)
    c += rect(CX, y, 6, 104, PURPLE, None, 3)
    c += txt(CX + 28, y + 42, "Materiais - Processo Legislativo Municipal", 19, INK, True)
    c += txt(CX + 28, y + 66, "Arquivos disponibilizados aos alunos das turmas A, B e C", 13, MUTED)
    c += btn(CX + CWA - 28 - 180, y + 32, 180, 42, "Enviar material", "primary", 13.5, "upload",
             to="55")
    y += 104 + 24
    s, ly = table(CX, y, lw, [
        ("Arquivo", 300, "start"), ("Turmas", 140, "start"), ("Enviado em", 130, "start"),
        ("Situação", 130, "end")], [
        [("two", "Apostila - Processo Legislativo", "PDF · 3,1 MB"), "Todas", "08/09/2026",
         ("badge", "Publicado", "abertas")],
        [("two", "Slides do Encontro 1", "PDF · 1,4 MB"), "Todas", "12/09/2026",
         ("badge", "Publicado", "abertas")],
        [("two", "Modelo de proposição comentado", "DOCX · 240 KB"), "Turma B", "12/09/2026",
         ("badge", "Publicado", "abertas")],
        [("two", "Estudo de caso avaliativo", "PDF · 180 KB"), "Todas", "13/09/2026",
         ("badge", "Em revisão", "breve")],
        [("two", "Vídeo - Tramitação passo a passo", "Link externo"), "Turma C", "13/09/2026",
         ("badge", "Em revisão", "breve")]], 66)
    c += s
    ly += 28
    c += rect(CX, ly, lw, 396, WHITE, BORDER, 10, 1.2)
    c += txt(CX + 28, ly + 46, "Enviar novo material", 19, INK, True)
    fy = ly + 78
    c += rect(CX + 28, fy, lw - 56, 128, "#F7FAFC", BLUE, 8, 1.6)
    c += icon_c("upload", CX + 28 + (lw - 56) / 2.0, fy + 46, 34, BLUE, 1.9)
    c += ctext(CX + 28 + (lw - 56) / 2.0, fy + 84, "Arraste o arquivo aqui ou clique para selecionar",
               14.5, BLUE_D, True)
    c += ctext(CX + 28 + (lw - 56) / 2.0, fy + 106, "PDF, DOCX, PPTX, XLSX ou link externo · até 50 MB",
               12, MUTED)
    fy += 152
    hw = (lw - 56 - 18) / 2.0
    s, _ = field(CX + 28, fy, hw, "Título do material", "Slides do Encontro 2", req=True)
    c += s
    s, _ = field(CX + 28 + hw + 18, fy, hw, "Disponibilizar para", "Todas as turmas", req=True, kind="select")
    c += s
    fy += 88
    c += checkbox(CX + 28, fy, "Avisar os alunos por e-mail sobre o novo material", True)
    c += btn(CX + 28, fy + 40, 190, 46, "Enviar material", "primary", 14.5, hot=True)
    c += btn(CX + 232, fy + 40, 130, 46, "Cancelar", "ghost", 14.5)
    ly += 396

    ry = y
    c += rect(rx, ry, rw, 268, WHITE, BORDER, 10, 1.2)
    c += txt(rx + 22, ry + 44, "Como o aluno vê", 17, INK, True)
    for i, (t, m) in enumerate([("Apostila - Processo Legislativo", "PDF · 3,1 MB"),
                                ("Slides do Encontro 1", "PDF · 1,4 MB"),
                                ("Modelo de proposição", "DOCX · 240 KB")]):
        yy = ry + 70 + i * 62
        c += rect(rx + 22, yy, rw - 44, 52, "#F7FAFC", BORDER, 8, 1)
        c += rect(rx + 34, yy + 12, 28, 28, RED_L, None, 6)
        c += icon_c("file", rx + 48, yy + 26, 15, RED, 1.7)
        c += para(rx + 70, yy + 22, t, rw - 150, 12, INK, 15, True, maxlines=1)
        c += txt(rx + 70, yy + 40, m, 10.5, MUTED)
        c += icon("download", rx + rw - 52, yy + 16, 16, BLUE_D, 1.8)
    c += txt(rx + 22, ry + 250, "Sala do curso na Área do Aluno", 12, MUTED)
    ry += 268 + 20
    c += rect(rx, ry, rw, 236, WHITE, BORDER, 10, 1.2)
    c += txt(rx + 22, ry + 44, "Regras de envio", 17, INK, True)
    for i, t in enumerate(["Você só envia materiais para cursos vinculados a você.",
                           "O gestor pode revisar e despublicar um material.",
                           "Links externos também são aceitos (vídeo, planilha).",
                           "Os alunos são avisados por e-mail, se marcado."]):
        c += circ(rx + 30, ry + 76 + i * 38, 3.5, GOLD)
        c += para(rx + 44, ry + 80 + i * 38, t, rw - 76, 12.5, MUTED, 17)
    ry += 236
    return wrap_prof("55-professor-materiais-upload", "Materiais", "Materiais do curso",
                     "Upload de materiais para os cursos vinculados",
                     ["Painel", "Meus cursos", "Materiais"], None, c, max(ly, ry),
                     ["ÁREA DO PROFESSOR", "RF 17"], None,
                     "Upload de materiais para os cursos vinculados, previsto na estrutura do portal "
                     "para a ÁREA DO PROFESSOR.")
