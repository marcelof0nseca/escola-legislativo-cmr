# -*- coding: utf-8 -*-
"""Telas publicas 10-21: institucional, acervo, contato, busca e certificados."""
from blocks import *

TELAS = []


def reg(fn):
    TELAS.append(fn)
    return fn


# ================================================================ 10 QUEM SOMOS
@reg
def t10():
    b = header_pub("A Escola")
    s, y = page_hero(HEAD_H, "Quem Somos",
                     "Missão, competências e composição da Escola do Legislativo",
                     ["Home", "A Escola", "Quem Somos"], 176)
    b += s
    y += 44
    s, ty = tabs(M, y, ["Quem Somos", "História", "Legislação e Transparência", "Escolas parceiras"], 0, to=["10", "11", "12", "13"])
    b += s
    y = ty + 44

    lw = 762
    rx = M + lw + 24
    rw = CW - lw - 24
    b += rect(M, y, lw, 300, WHITE, BORDER, 12, 1.2)
    b += txt(M + 32, y + 52, "A Escola do Legislativo", 24, INK, True)
    b += rect(M + 32, y + 64, 46, 4, GOLD, None, 2)
    b += para(M + 32, y + 104, "Criada pela Resolução nº 1.842/2024, a Escola do Legislativo da Câmara "
                               "Municipal do Recife é a unidade responsável pela formação e pelo "
                               "aperfeiçoamento continuado dos servidores da Casa e pela aproximação "
                               "entre o Poder Legislativo municipal e a sociedade.", lw - 64, 15, TXT, 24)
    b += para(M + 32, y + 208, "Suas ações incluem cursos, seminários, oficinas e publicações, "
                               "oferecidos a servidores, vereadores, agentes públicos de outros órgãos "
                               "e ao cidadão interessado no processo legislativo.", lw - 64, 15, MUTED, 24)
    yy = y + 300 + 24
    for i, (ic, t, d) in enumerate([
            ("flag", "Missão", "Qualificar a atuação do Legislativo municipal por meio da educação continuada."),
            ("eye", "Visão", "Ser referência regional em capacitação e cidadania legislativa até 2030."),
            ("shield", "Valores", "Transparência, impessoalidade, acessibilidade e melhoria contínua.")]):
        x = M + i * ((lw - 48) / 3.0 + 24)
        cwid = (lw - 48) / 3.0
        b += rect(x, yy, cwid, 190, WHITE, BORDER, 12, 1.2)
        b += rect(x + 24, yy + 24, 42, 42, GOLD_L, None, 9)
        b += icon_c(ic, x + 45, yy + 45, 21, GOLD, 1.8)
        b += txt(x + 24, yy + 96, t, 17, INK, True)
        b += para(x + 24, yy + 122, d, cwid - 48, 13, MUTED, 19)
    yy += 190 + 24

    b += rect(M, yy, lw, 396, WHITE, BORDER, 12, 1.2)
    b += txt(M + 32, yy + 52, "Composição da Escola", 24, INK, True)
    b += rect(M + 32, yy + 64, 46, 4, GOLD, None, 2)
    equipe = [("Ricardo Ferraz", "Diretor Geral", "RF"),
              ("Robertson Barros", "Coordenador da Escola do Legislativo", "RB"),
              ("Helena Vasconcelos", "Coordenação Pedagógica", "HV"),
              ("Marcelo Andrade", "Secretaria Acadêmica", "MA"),
              ("Cláudia Nunes", "Comunicação e Acervo", "CN"),
              ("Diego Farias", "Apoio de Tecnologia (DIVINF)", "DF")]
    for i, (nome, cargo, ini) in enumerate(equipe):
        x = M + 32 + (i % 2) * ((lw - 64) / 2.0)
        cy = yy + 104 + (i // 2) * 96
        b += rect(x, cy, (lw - 64) / 2.0 - 16, 80, "#F7FAFC", BORDER, 10, 1)
        b += avatar(x + 16, cy + 16, 48, ini, NAVY_3)
        b += txt(x + 76, cy + 36, nome, 14.5, INK, True)
        b += para(x + 76, cy + 54, cargo, 200, 12, MUTED, 15, maxlines=2)
    yy += 396

    ry = y
    b += rect(rx, ry, rw, 260, NAVY, None, 12)
    b += txt(rx + 26, ry + 52, "A Escola em números", 18, WHITE, True)
    for i, (v, l) in enumerate([("128", "cursos realizados desde 2024"),
                                ("4.310", "certificados emitidos"),
                                ("6", "instrumentos jurídicos vigentes")]):
        b += txt(rx + 26, ry + 100 + i * 56, v, 24, GOLD, True)
        b += txt(rx + 26 + tw(v, 24, True) + 12, ry + 100 + i * 56, l, 12.5, "#B7C7D6")
        if i < 2:
            b += line(rx + 26, ry + 116 + i * 56, rx + rw - 26, ry + 116 + i * 56, "#27476A", 1)
    ry += 260 + 20
    b += rect(rx, ry, rw, 236, WHITE, BORDER, 12, 1.2)
    b += txt(rx + 26, ry + 46, "Onde estamos", 17, INK, True)
    for i, (ic, t1, t2) in enumerate([("pin", "Rua Princesa Isabel, 410 - 1º Andar", "Boa Vista - Recife/PE"),
                                      ("phone", "(81) 3355-4000", "ramal 4120"),
                                      ("mail", "escoladolegislativo@", "recife.pe.leg.br")]):
        b += icon(ic, rx + 26, ry + 70 + i * 56, 18, BLUE, 1.7)
        b += txt(rx + 54, ry + 78 + i * 56, t1, 13, TXT, True)
        b += txt(rx + 54, ry + 96 + i * 56, t2, 12.5, MUTED)
    ry += 236 + 20
    b += rect(rx, ry, rw, 200, WHITE, BORDER, 12, 1.2)
    b += txt(rx + 26, ry + 46, "Documentos", 17, INK, True)
    for i, t in enumerate(["Resolução de criação nº 1.842/2024",
                           "Regimento Interno da Escola", "Plano Anual de Capacitação 2026"]):
        b += icon("file", rx + 26, ry + 68 + i * 42, 17, RED, 1.7)
        b += para(rx + 52, ry + 82 + i * 42, t, rw - 90, 12.5, BLUE_D, 16, maxlines=1)
    ry += 200

    y = max(yy, ry) + 76
    s, y = footer_pub(y)
    b += s
    s, y = nota(y, W, ["A ESCOLA - Quem Somos", "Composição da Escola"], None,
                "Atende ao item 'composição da Escola' informado pelo usuário e à estrutura "
                "A ESCOLA > Quem Somos definida na seção 2 do documento de requisitos.")
    b += s
    return "10-escola-quem-somos", svg("10-escola-quem-somos", W, y, b, WHITE)


# ================================================================ 11 HISTORIA
@reg
def t11():
    b = header_pub("A Escola")
    s, y = page_hero(HEAD_H, "História",
                     "A trajetória da Escola do Legislativo da Câmara Municipal do Recife",
                     ["Home", "A Escola", "História"], 176)
    b += s
    y += 44
    s, ty = tabs(M, y, ["Quem Somos", "História", "Legislação e Transparência", "Escolas parceiras"], 1, to=["10", "11", "12", "13"])
    b += s
    y = ty + 44
    lw = 762
    rx = M + lw + 24
    rw = CW - lw - 24
    b += rect(M, y, lw, 726, WHITE, BORDER, 12, 1.2)
    b += txt(M + 32, y + 52, "Linha do tempo", 24, INK, True)
    b += rect(M + 32, y + 64, 46, 4, GOLD, None, 2)
    s, _ = timeline(M + 32, y + 100, lw - 64, [
        ("2019", "Primeiras capacitações internas",
         "A Câmara passa a promover cursos pontuais de técnica legislativa para servidores efetivos."),
        ("2022", "Programa de Educação Continuada",
         "Criação do programa permanente de capacitação, com calendário semestral e controle manual de inscrições."),
        ("2024", "Criação formal da Escola",
         "A Resolução nº 1.842/2024 institui a Escola do Legislativo como unidade da estrutura da CMR."),
        ("2025", "Abertura ao público externo",
         "Cursos passam a aceitar servidores de outros órgãos e cidadãos, ampliando o alcance da Escola."),
        ("2026", "Portal digital da Escola",
         "Processo nº 3096/2025 dá origem ao portal com inscrições on-line, certificação digital e acervo.")])
    b += s
    b += rect(M, y + 750, lw, 232, BLUE_L, "#A9CBE8", 12, 1.2)
    b += icon("info", M + 32, y + 782, 22, BLUE_D, 1.8)
    b += txt(M + 66, y + 800, "O portal que você está vendo", 18, BLUE_D, True)
    b += para(M + 32, y + 838, "Este portal nasce da solicitação encaminhada pelo Diretor Ricardo Ferraz no "
                               "processo nº 3096/2025, com as necessidades de negócio reportadas por Robertson "
                               "Barros: divulgar a agenda de cursos e eventos, receber inscrições, divulgar "
                               "escolas parceiras e publicar notícias e instrumentos jurídicos formalizados.",
              lw - 64, 14, TXT, 22)
    ly = y + 982

    ry = y
    b += img_ph(rx, ry, rw, 260, 12, TONES[4], "ACERVO FOTOGRÁFICO")
    ry += 260 + 20
    b += rect(rx, ry, rw, 300, WHITE, BORDER, 12, 1.2)
    b += txt(rx + 26, ry + 46, "Marcos institucionais", 17, INK, True)
    for i, (d, t) in enumerate([("Res. 1.842/2024", "Cria a Escola do Legislativo"),
                                ("Portaria 77/2024", "Designa a coordenação"),
                                ("Res. 1.910/2025", "Aprova o Regimento Interno"),
                                ("Proc. 3096/2025", "Autoriza o portal digital")]):
        yy = ry + 70 + i * 56
        b += rect(rx + 26, yy, 8, 8, GOLD, None, 4)
        b += txt(rx + 46, yy + 8, d, 13, INK, True)
        b += txt(rx + 46, yy + 26, t, 12, MUTED)
    ry += 300
    y = max(ly, ry) + 76
    s, y = footer_pub(y)
    b += s
    s, y = nota(y, W, ["A ESCOLA - História"], None,
                "Item 'História' da estrutura do portal (seção 2 do documento).")
    b += s
    return "11-escola-historia", svg("11-escola-historia", W, y, b, WHITE)


# ================================================================ 12 TRANSPARENCIA
@reg
def t12():
    b = header_pub("A Escola")
    s, y = page_hero(HEAD_H, "Legislação e Transparência",
                     "Instrumentos jurídicos formalizados, convênios e normas da Escola",
                     ["Home", "A Escola", "Legislação e Transparência"], 176)
    b += s
    y += 44
    s, ty = tabs(M, y, ["Quem Somos", "História", "Legislação e Transparência", "Escolas parceiras"], 2, to=["10", "11", "12", "13"])
    b += s
    y = ty + 40

    b += rect(M, y, CW, 96, WHITE, BORDER, 10, 1.2)
    for i, (l, v, wd) in enumerate([("Tipo de instrumento", "Todos", 280),
                                    ("Situação", "Vigentes", 240), ("Ano", "2026", 200)]):
        x = M + 24 + i * (wd + 16) if i == 0 else M + 24 + 296 * 1 + (i - 1) * 256
        x = M + 24 + [0, 296, 552][i]
        b += txt(x, y + 34, l, 12, MUTED, True)
        b += rect(x, y + 42, wd, 40, WHITE, BORDER2, 6, 1.3)
        b += txt(x + 12, y + 67, v, 13.5, TXT)
        b += icon("chev-d", x + wd - 28, y + 53, 17, MUTED, 1.8)
    b += rect(M + 24 + 772, y + 42, 260, 40, WHITE, BORDER2, 6, 1.3)
    b += icon("search", M + 36 + 772, y + 53, 17, FAINT, 1.7)
    b += txt(M + 62 + 772, y + 67, "Buscar por objeto ou nº", 13, FAINT)
    b += btn(M + CW - 24 - 116, y + 42, 116, 40, "Filtrar", "primary", 13.5)
    y += 96 + 32

    b += txt(M, y, "Instrumentos jurídicos formalizados", 22, INK, True)
    b += txt(M, y + 24, "Convênios, acordos de cooperação e termos firmados pela Escola do Legislativo.",
             13.5, MUTED)
    y += 52
    s, y = table(M, y, CW, [
        ("Instrumento", 300, "start"), ("Partícipe", 250, "start"),
        ("Objeto", 300, "start"), ("Vigência", 190, "start"), ("", 120, "end")], [
        [("two", "Acordo de Cooperação nº 04/2026", "Assinado em 10/08/2026"), "ALMG - Minas Gerais",
         "Intercâmbio de cursos e material", ("two", "10/08/2026", "até 09/08/2028"),
         ("btns", [("PDF", "secondary")])],
        [("two", "Termo de Adesão nº 11/2025", "Programa Interlegis"), "ILB / Senado Federal",
         "Uso da plataforma Saberes", ("two", "02/2025", "indeterminada"),
         ("btns", [("PDF", "secondary")])],
        [("two", "Convênio nº 22/2025", "Capacitação conjunta"), "ALEPE - Pernambuco",
         "Oferta compartilhada de turmas", ("two", "05/2025", "até 04/2027"),
         ("btns", [("PDF", "secondary")])],
        [("two", "Acordo de Cooperação nº 09/2025", "Escolas do Legislativo"), "ALEP - Paraná",
         "Intercâmbio de metodologias", ("two", "09/2025", "até 08/2027"),
         ("btns", [("PDF", "secondary")])],
        [("two", "Termo de Cooperação nº 03/2024", "Encerrado"), "Câmara Municipal de Olinda",
         "Cursos em rede metropolitana", ("two", "03/2024", "encerrado em 02/2026"),
         ("btns", [("PDF", "secondary")])]], 66)
    b += s
    y += 40

    b += txt(M, y, "Normas da Escola do Legislativo", 22, INK, True)
    y += 32
    docs = [("Resolução nº 1.842/2024", "Cria a Escola do Legislativo da CMR · publicado no DOM de 14/03/2024"),
            ("Resolução nº 1.910/2025", "Aprova o Regimento Interno da Escola · publicado em 22/07/2025"),
            ("Portaria nº 77/2024", "Designa a coordenação da Escola do Legislativo"),
            ("Plano Anual de Capacitação 2026", "Aprovado pela Diretoria Geral em 12/2025")]
    for i, (t, m) in enumerate(docs):
        s, _ = doc_row(M + (i % 2) * (CW / 2.0 + 12), y + (i // 2) * 100, CW / 2.0 - 12, t, m)
        b += s
    y += 2 * 100 + 24
    s, y = alert(M, y, CW, "Transparência ativa",
                 "Todos os instrumentos jurídicos formalizados pela Escola são publicados nesta página em "
                 "até 5 dias úteis após a assinatura, com o inteiro teor em PDF, conforme a política de "
                 "transparência da Câmara Municipal do Recife.", "info")
    b += s
    y += 76
    s, y = footer_pub(y)
    b += s
    s, y = nota(y, W, ["A ESCOLA - Legislação e Transparência", "RF 17"], None,
                "Atende ao item 'lista de instrumentos jurídicos formalizados' informado pelo usuário e "
                "à seção Legislação e Transparência (Parcerias/Convênios) da estrutura do portal.")
    b += s
    return "12-escola-legislacao-transparencia", svg("12-escola-legislacao-transparencia", W, y, b, WHITE)


# ================================================================ 13 PARCEIRAS
@reg
def t13():
    b = header_pub("A Escola")
    s, y = page_hero(HEAD_H, "Escolas do Legislativo parceiras",
                     "Acesse o portal das escolas com instrumentos formalizados com a CMR",
                     ["Home", "A Escola", "Escolas parceiras"], 176)
    b += s
    y += 44
    s, ty = tabs(M, y, ["Quem Somos", "História", "Legislação e Transparência", "Escolas parceiras"], 3, to=["10", "11", "12", "13"])
    b += s
    y = ty + 44
    for i, (nome, sigla, url, inst) in enumerate(PARCEIRAS):
        x = M + (i % 3) * (384 + 24)
        cy = y + (i // 3) * (250 + 24)
        b += rect(x, cy, 384, 250, WHITE, BORDER, 12, 1.2)
        b += rect(x, cy, 384, 6, GOLD, None, 12)
        b += rect(x, cy + 3, 384, 3, GOLD)
        b += rect(x + 24, cy + 34, 60, 60, BLUE_L, None, 10)
        b += ctext(x + 54, cy + 64, sigla[:5], 15, BLUE_D, True)
        b += para(x + 100, cy + 56, nome, 250, 16, INK, 21, True, maxlines=2)
        b += line(x + 24, cy + 116, x + 360, cy + 116, "#EDF1F6", 1.2)
        b += txt(x + 24, cy + 142, "Instrumento formalizado", 11.5, MUTED, True)
        b += para(x + 24, cy + 162, inst, 336, 13, TXT, 18, maxlines=2)
        b += icon("link", x + 24, cy + 196, 16, BLUE, 1.7)
        b += txt(x + 48, cy + 209, url, 12.5, BLUE_D)
        b += btn(x + 250, cy + 194, 110, 38, "Acessar", "secondary", 13)
    y += 2 * (250 + 24) + 20
    s, y = alert(M, y, CW, "Sobre os links externos",
                 "Ao clicar em Acessar, o portal abre o site da escola parceira em nova aba. A Câmara "
                 "Municipal do Recife não se responsabiliza pelo conteúdo mantido por terceiros.", "info")
    b += s
    y += 76
    s, y = footer_pub(y)
    b += s
    s, y = nota(y, W, ["Escolas parceiras", "RF 17"], None,
                "Atende ao item 'incluir links para acesso ao site de escolas do legislativo parceiras' "
                "e à divulgação de escolas parceiras prevista na contextualização do projeto.")
    b += s
    return "13-escolas-parceiras", svg("13-escolas-parceiras", W, y, b, WHITE)


# ================================================================ 14 ACERVO
@reg
def t14():
    b = header_pub("Acervo")
    s, y = page_hero(HEAD_H, "Acervo / Biblioteca",
                     "Publicações, manuais e legislações produzidos ou reunidos pela Escola",
                     ["Home", "Acervo"], 176)
    b += s
    y += 44
    s, ty = tabs(M, y, ["Publicações", "Manuais", "Legislações"], 0)
    b += s
    y = ty + 36
    b += rect(M, y, CW, 76, WHITE, BORDER, 10, 1.2)
    b += rect(M + 20, y + 18, 560, 40, WHITE, BORDER2, 6, 1.3)
    b += icon("search", M + 32, y + 29, 17, FAINT, 1.7)
    b += txt(M + 58, y + 43, "Buscar no acervo por título, autor ou assunto", 13.5, FAINT)
    for i, (l, wd) in enumerate([("Assunto: todos", 200), ("Ano: todos", 160), ("Formato: PDF", 170)]):
        x = M + 600 + [0, 216, 392][i]
        b += rect(x, y + 18, wd, 40, "#F7FAFC", BORDER2, 6, 1.3)
        b += txt(x + 12, y + 43, l, 13, TXT)
        b += icon("chev-d", x + wd - 28, y + 29, 17, MUTED, 1.8)
    b += btn(M + CW - 20 - 100, y + 18, 100, 40, "Buscar", "primary", 13.5)
    y += 76 + 32
    b += txt(M, y, "24 publicações", 15, INK, True)
    b += txt(W - M - 210, y, "Ordenar: mais recentes primeiro", 13, BLUE_D, True)
    y += 24
    pubs = [("Manual de Técnica Legislativa - 3ª edição",
             "Helena Vasconcelos · 2026 · 148 páginas · PDF 4,2 MB", "PDF", RED_L, RED),
            ("Cartilha do Orçamento Público Municipal",
             "Paulo Meneses · 2026 · 46 páginas · PDF 1,8 MB", "PDF", RED_L, RED),
            ("Coletânea de Legislação Municipal 2026",
             "Escola do Legislativo · 2026 · 512 páginas · PDF 9,6 MB", "PDF", RED_L, RED),
            ("Guia do Vereador Iniciante",
             "Escola do Legislativo · 2025 · 72 páginas · PDF 2,4 MB", "PDF", RED_L, RED),
            ("Revista Legislativo Municipal - nº 4",
             "Vários autores · 2025 · 96 páginas · PDF 6,1 MB", "PDF", RED_L, RED),
            ("Anais do Seminário de Participação Cidadã",
             "Escola do Legislativo · 2025 · 210 páginas · PDF 7,8 MB", "PDF", RED_L, RED),
            ("Apostila - Redação Oficial na CMR",
             "Cláudia Nunes · 2025 · 64 páginas · DOCX 1,1 MB", "DOCX", BLUE_L, BLUE),
            ("Planilha modelo - Controle de frequência",
             "Secretaria Acadêmica · 2026 · XLSX 320 KB", "XLSX", GREEN_L, GREEN)]
    for i, (t, m, tp, tl, tf) in enumerate(pubs):
        s, _ = doc_row(M, y + i * 100, CW, t, m, tp, tl, tf)
        b += s
    y += len(pubs) * 100 + 16
    s, y = pagination(M, y, CW, "24")
    b += s
    y += 76
    s, y = footer_pub(y)
    b += s
    s, y = nota(y, W, ["ACERVO/BIBLIOTECA", "RF 17"], None,
                "Seção ACERVO/BIBLIOTECA com as três abas previstas (Publicações, Manuais e Legislações). "
                "Os arquivos são inseridos pelo Gestor da Escola (RF 17).")
    b += s
    return "14-acervo-biblioteca", svg("14-acervo-biblioteca", W, y, b, WHITE)


# ================================================================ 15 CONTATO
@reg
def t15():
    b = header_pub("Contato")
    s, y = page_hero(HEAD_H, "Contato",
                     "Fale com a equipe da Escola do Legislativo da Câmara Municipal do Recife",
                     ["Home", "Contato"], 176)
    b += s
    y += 48
    lw = 700
    rx = M + lw + 40
    rw = CW - lw - 40
    b += rect(M, y, lw, 596, WHITE, BORDER, 12, 1.2)
    b += txt(M + 32, y + 54, "Envie uma mensagem", 22, INK, True)
    b += txt(M + 32, y + 78, "Respondemos em até 2 dias úteis pelo e-mail informado.", 13, MUTED)
    fy = y + 112
    hw = (lw - 64 - 20) / 2.0
    s, _ = field(M + 32, fy, hw, "Nome completo", "", req=True)
    b += s
    s, _ = field(M + 32 + hw + 20, fy, hw, "E-mail", "", req=True, ic="mail")
    b += s
    fy += 88
    s, _ = field(M + 32, fy, hw, "Telefone / WhatsApp", "", ic="phone")
    b += s
    s, _ = field(M + 32 + hw + 20, fy, hw, "Assunto", "Selecione o assunto", kind="select", req=True)
    b += s
    fy += 88
    s, fy = textarea(M + 32, fy, lw - 64, "Mensagem", "", 160, True)
    b += s
    fy += 24
    b += checkbox(M + 32, fy, "Li e concordo com o tratamento dos meus dados para resposta a este contato.",
                  True)
    b += txt(M + 60, fy + 34, "Base legal: LGPD, art. 7º, inciso IX. Os dados não são usados para outra finalidade.",
             12, MUTED)
    b += btn(M + 32, fy + 62, 200, 50, "Enviar mensagem", "primary", 15, "mail")

    ry = y
    b += rect(rx, ry, rw, 300, NAVY, None, 12)
    b += txt(rx + 28, ry + 52, "Escola do Legislativo", 19, WHITE, True)
    b += rect(rx + 28, ry + 64, 40, 3, GOLD, None, 2)
    infos = [("pin", "Rua Princesa Isabel, 410 - 1º Andar", "Boa Vista - Recife/PE - CEP 50050-330"),
             ("phone", "(81) 3355-4000 · ramal 4120", "Segunda a sexta, 8h às 17h"),
             ("mail", "escoladolegislativo@recife.pe.leg.br", "Atendimento por e-mail")]
    for i, (ic, t1, t2) in enumerate(infos):
        yy = ry + 100 + i * 66
        b += icon(ic, rx + 28, yy, 19, GOLD, 1.7)
        b += para(rx + 58, yy + 12, t1, rw - 90, 13.5, WHITE, 18, True, maxlines=2)
        b += txt(rx + 58, yy + 34, t2, 12, "#9FB6CB")
    ry += 300 + 20
    b += img_ph(rx, ry, rw, 240, 12, TONES[3], "MAPA DE LOCALIZAÇÃO", "pin")
    ry += 240 + 20
    b += rect(rx, ry, rw, 194, WHITE, BORDER, 12, 1.2)
    b += txt(rx + 28, ry + 46, "Dúvidas frequentes", 17, INK, True)
    for i, t in enumerate(["Como emito a 2ª via do certificado?",
                           "Posso me inscrever sendo de fora da Câmara?",
                           "Como funciona a lista de espera?"]):
        b += icon("chev-r", rx + 28, ry + 62 + i * 40, 15, GOLD, 1.9)
        b += para(rx + 50, ry + 76 + i * 40, t, rw - 90, 13, BLUE_D, 17, maxlines=1)
    ry += 194

    y = max(y + 596, ry) + 76
    s, y = footer_pub(y)
    b += s
    s, y = nota(y, W, ["CONTATO"], None,
                "Seção CONTATO da estrutura do portal: e-mail, endereço e telefone, com formulário de "
                "mensagem e consentimento LGPD.")
    b += s
    return "15-contato", svg("15-contato", W, y, b, WHITE)


# ================================================================ 16 BUSCA
@reg
def t16():
    b = header_pub(None)
    y = HEAD_H
    b += rect(0, y, W, 160, NAVY)
    b += crumb_light(M, y + 40, ["Home", "Resultados da busca"])
    b += rect(M, y + 62, 900, 56, WHITE, None, 8)
    b += icon("search", M + 18, y + 80, 20, MUTED, 1.8)
    b += txt(M + 50, y + 98, "processo legislativo", 16, INK)
    b += icon("close", M + 856, y + 80, 18, MUTED, 1.9)
    b += btn(M + 920, y + 62, 140, 56, "Buscar", "gold", 15)
    y += 160 + 40
    b += txt(M, y, "18 resultados para", 22, INK, True)
    b += txt(M + tw("18 resultados para", 22, True) + 10, y, "\"processo legislativo\"", 22, BLUE_D, True)
    y += 34
    s, cx = pills(M, y, ["Tudo (18)", "Cursos (7)", "Notícias (5)", "Acervo (4)", "Páginas (2)"], 0)
    b += s
    y += 38 + 32

    grupos = [("Cursos e eventos", "book", [
        ("Processo Legislativo Municipal", "Curso · 14 e 15/09/2026 · Online · 8h · Inscrições abertas",
         "Tramitação de proposições, comissões e técnica de votação na Câmara Municipal."),
        ("Audiências Públicas e Participação Cidadã", "Curso realizado · 08/04/2026 · Online · 4h",
         "Instrumentos de participação popular no processo legislativo municipal.")]),
        ("Notícias", "bell", [
        ("Agenda do 2º semestre de 2026 já está disponível", "Notícia · 05/08/2026 · Agenda",
         "São 14 cursos e 6 eventos abertos a servidores e ao público externo."),
        ("Turma de Redação Oficial forma 25 servidores", "Notícia · 20/07/2026 · Cursos",
         "Curso presencial encerrou com 96% de aproveitamento.")]),
        ("Acervo / Biblioteca", "folder", [
        ("Manual de Técnica Legislativa - 3ª edição", "Publicação · PDF · 4,2 MB · 2026",
         "Guia completo de elaboração e revisão de proposições legislativas.")])]
    for gt, gic, items in grupos:
        b += icon("chev-r", M, y - 14, 16, GOLD, 2)
        b += txt(M + 24, y, gt, 18, INK, True)
        b += line(M + 30 + tw(gt, 18, True), y - 5, W - M, y - 5, BORDER, 1.2)
        y += 22
        for t, meta, desc in items:
            b += rect(M, y, CW, 104, WHITE, BORDER, 10, 1.2)
            b += rect(M + 20, y + 28, 48, 48, BLUE_L, None, 8)
            b += icon_c(gic, M + 44, y + 52, 22, BLUE, 1.8)
            b += txt(M + 86, y + 40, t, 16.5, BLUE_D, True)
            b += txt(M + 86, y + 62, meta, 12.5, GREEN if "abertas" in meta else MUTED, True)
            b += para(M + 86, y + 84, desc, CW - 200, 13, MUTED, 18, maxlines=1)
            hot(M, y, CW, 104, {"book": "05", "bell": "09", "folder": "14"}[gic], t[:24])
            b += icon("chev-r", M + CW - 44, y + 42, 18, FAINT, 1.9)
            y += 104 + 12
        y += 26
    s, y = pagination(M, y, CW, "18")
    b += s
    y += 76
    s, y = footer_pub(y)
    b += s
    s, y = nota(y, W, ["Barra de Busca Rápida"], None,
                "Resultado da busca rápida por texto simples prevista na HOME, agrupando cursos, "
                "notícias, acervo e páginas institucionais.")
    b += s
    return "16-busca-resultados", svg("16-busca-resultados", W, y, b, WHITE)


# ================================================================ 17 VALIDAR
@reg
def t17():
    b = header_pub(None)
    y = HEAD_H
    b += rect(0, y, W, 210, NAVY)
    b += crumb_light(M, y + 44, ["Home", "Validar certificado"])
    b += icon(  "cert", M, y + 74, 30, GOLD, 1.9)
    b += txt(M + 44, y + 100, "Validação de Certificados", 34, WHITE, True)
    b += para(M, y + 130, "Área pública para que qualquer cidadão, empresa ou órgão governamental confira "
                          "a autenticidade dos certificados emitidos pela Escola do Legislativo.",
              760, 15, "#B7C7D6", 22)
    y += 210 + 48

    fw = 700
    fx = M
    b += rect(fx, y, fw, 470, WHITE, BORDER, 12, 1.4)
    b += txt(fx + 36, y + 58, "Informe o código de autenticidade", 22, INK, True)
    b += txt(fx + 36, y + 84, "O código está impresso no rodapé do certificado em PDF.", 13.5, MUTED)
    s, _ = field(fx + 36, y + 122, fw - 72, "Código de Autenticidade do Certificado",
                 "ELCMR-2026-A7K9-3F2D-8B1C", req=True, h=56, ic="key")
    b += s
    # recaptcha
    ry0 = y + 230
    b += rect(fx + 36, ry0, 320, 78, "#F7FAFC", BORDER2, 8, 1.3)
    b += rect(fx + 58, ry0 + 24, 28, 28, WHITE, BORDER2, 4, 1.5)
    b += txt(fx + 100, ry0 + 44, "Não sou um robô", 14, TXT)
    b += rect(fx + 290, ry0 + 18, 44, 44, "#E8EEF4", None, 6)
    b += icon_c("shield", fx + 312, ry0 + 34, 20, "#4A6B8A", 1.8)
    b += txt(fx + 290, ry0 + 70, "reCAPTCHA", 8, MUTED, anchor="middle")
    b += txt(fx + 372, ry0 + 34, "Proteção contra acessos", 12.5, MUTED)
    b += txt(fx + 372, ry0 + 52, "automatizados ao banco de dados.", 12.5, MUTED)
    b += btn(fx + 36, y + 336, 260, 54, "Validar certificado", "primary", 16, "search",
             hot=True, to="18")
    hot(fx + 36, y + 122, fw - 72, 76, "19", "codigo invalido")
    b += btn(fx + 310, y + 336, 170, 54, "Limpar", "ghost", 15)
    b += line(fx + 36, y + 412, fx + fw - 36, y + 412, "#EDF1F6", 1.2)
    b += icon("lock", fx + 36, y + 430, 16, MUTED, 1.7)
    b += txt(fx + 60, y + 442, "Consulta pública e gratuita. Nenhum dado é armazenado nesta consulta.",
             12.5, MUTED)

    rx = M + fw + 24
    rw = CW - fw - 24
    b += rect(rx, y, rw, 470, WHITE, BORDER, 12, 1.2)
    b += txt(rx + 28, y + 52, "Onde encontrar o código", 18, INK, True)
    b += rect(rx + 28, y + 76, rw - 56, 200, "#F7FAFC", BORDER, 8, 1.2)
    b += rect(rx + 44, y + 92, rw - 88, 130, WHITE, BORDER2, 4, 1.2)
    b += ctext(rx + rw / 2.0, y + 128, "CERTIFICADO", 15, NAVY, True)
    b += line(rx + 60, y + 148, rx + rw - 60, y + 148, "#E7D2A4", 1)
    b += ctext(rx + rw / 2.0, y + 168, "Maria Silva dos Santos", 12, MUTED)
    b += rect(rx + 56, y + 186, rw - 112, 28, GOLD_L, "#E7D2A4", 4, 1.2)
    b += ctext(rx + rw / 2.0, y + 200, "ELCMR-2026-A7K9-3F2D-8B1C", 11.5, "#8A6414", True)
    b += path("M%s %s L%s %s" % (n(rx + 60), n(y + 246), n(rx + 100), n(y + 216)), None, RED, 2)
    b += txt(rx + 106, y + 250, "Rodapé do PDF do certificado", 12, RED, True)
    b += line(rx + 28, y + 300, rx + rw - 28, y + 300, "#EDF1F6", 1.2)
    b += txt(rx + 28, y + 330, "Precisa de ajuda?", 15, INK, True)
    for i, t in enumerate(["O código tem 24 caracteres alfanuméricos.",
                           "Digite sem espaços; os hifens são opcionais.",
                           "Certificados anteriores a 2026 devem ser conferidos com a Secretaria."]):
        b += circ(rx + 34, y + 356 + i * 34, 3, GOLD)
        b += para(rx + 48, y + 360 + i * 34, t, rw - 90, 12.5, MUTED, 17, maxlines=2)
    y += 470 + 40

    s, y = alert(M, y, CW, "Cenários possíveis da consulta",
                 "Código válido: o portal exibe a tela de confirmação com os dados do documento. "
                 "Código inválido: o portal exibe a mensagem 'Certificado não encontrado. Verifique se o "
                 "código foi digitado corretamente.'", "info")
    b += s
    y += 76
    s, y = footer_pub(y)
    b += s
    s, y = nota(y, W, ["RF 4"],
                ["RF 4 - Formato de validação impresso no PDF: apenas código alfanumérico + link "
                 "(Opção 1) ou código + QR Code com validação instantânea (Opção 2)? Ver telas 20 e 21."],
                "Tela pública de consulta do RF 4, com campo do código, proteção reCAPTCHA contra "
                "varredura do banco e orientação de onde encontrar o código no PDF.")
    b += s
    return "17-validar-certificado", svg("17-validar-certificado", W, y, b, WHITE)


# ================================================================ 18 VALIDO
@reg
def t18():
    b = header_pub(None)
    y = HEAD_H
    b += rect(0, y, W, 150, NAVY)
    b += crumb_light(M, y + 44, ["Home", "Validar certificado", "Resultado"])
    b += txt(M, y + 96, "Resultado da validação", 30, WHITE, True)
    y += 150 + 44

    b += rect(M, y, CW, 132, GREEN_L, "#A9DCC6", 12, 1.4)
    b += rect(M, y, 6, 132, GREEN, None, 3)
    b += circ(M + 74, y + 66, 32, GREEN)
    b += path("M%s %s l10 11 L%s %s" % (n(M + 60), n(y + 66), n(M + 90), n(y + 54)), None, WHITE, 4)
    b += txt(M + 126, y + 56, "Certificado válido e autêntico", 26, GREEN, True)
    b += txt(M + 126, y + 86, "Documento emitido pela Escola do Legislativo da Câmara Municipal do Recife.",
             14.5, TXT)
    b += badge(M + 126, y + 100, "Código ELCMR-2026-A7K9-3F2D-8B1C", "solid-green", 12, 26)[0]
    y += 132 + 32

    lw = 762
    b += rect(M, y, lw, 526, WHITE, BORDER, 12, 1.2)
    b += txt(M + 32, y + 52, "Dados do documento", 21, INK, True)
    b += line(M + 32, y + 72, M + lw - 32, y + 72, "#EDF1F6", 1.2)
    dados = [("Nome do aluno", "MARIA SILVA DOS SANTOS", True),
             ("CPF", "123.***.***-89", False),
             ("Matrícula (servidor da CMR)", "20.451-7", False),
             ("Curso / evento", "Processo Legislativo Municipal", True),
             ("Carga horária total", "8 (oito) horas", False),
             ("Data de conclusão", "15/09/2026", False),
             ("Data de emissão", "16/09/2026", False),
             ("Situação", "Válido - sem registro de cancelamento", False)]
    for i, (l, v, big) in enumerate(dados):
        yy = y + 100 + (i // 2) * 92
        x = M + 32 + (i % 2) * ((lw - 64) / 2.0)
        b += txt(x, yy, l, 12, MUTED, True)
        b += txt(x, yy + 26, v, 17 if big else 15.5, INK, True)
        b += line(x, yy + 48, x + (lw - 64) / 2.0 - 24, yy + 48, "#F0F4F8", 1.2)
    b += btn(M + 32, y + 452, 210, 46, "Imprimir comprovante", "secondary", 14, "print")
    b += btn(M + 254, y + 452, 210, 46, "Validar outro código", "ghost", 14, "search", to="17")

    rx = M + lw + 24
    rw = CW - lw - 24
    ry = y
    s, ry = alert(rx, ry, rw, "Aviso de privacidade (LGPD)",
                  "Esta página exibe apenas os dados mínimos necessários para comprovar a autenticidade "
                  "do documento. O CPF é apresentado de forma mascarada.", "lgpd")
    b += s
    ry += 20
    b += rect(rx, ry, rw, 236, WHITE, BORDER, 12, 1.2)
    b += txt(rx + 26, ry + 46, "Como conferir", 17, INK, True)
    for i, t in enumerate(["Compare o nome e o CPF mascarado com o documento apresentado.",
                           "Confira o título do curso e a carga horária.",
                           "Em caso de divergência, fale com a Escola do Legislativo."]):
        b += circ(rx + 34, ry + 76 + i * 52, 11, BLUE_L)
        b += ctext(rx + 34, ry + 76 + i * 52, str(i + 1), 11.5, BLUE_D, True)
        b += para(rx + 54, ry + 72 + i * 52, t, rw - 90, 12.5, MUTED, 17)
    ry += 236 + 20
    b += rect(rx, ry, rw, 150, "#F7FAFC", BORDER, 12, 1.2)
    b += txt(rx + 26, ry + 44, "Consulta registrada em", 12.5, MUTED, True)
    b += txt(rx + 26, ry + 72, "19/08/2026 às 14h07", 16, INK, True)
    b += txt(rx + 26, ry + 102, "Nenhum dado do consultante", 12, MUTED)
    b += txt(rx + 26, ry + 120, "é armazenado nesta operação.", 12, MUTED)
    ry += 150
    y = max(y + 526, ry) + 76
    s, y = footer_pub(y)
    b += s
    s, y = nota(y, W, ["RF 4 - Cenário B"],
                ["RF 4 (LGPD) - Quais dados devem aparecer na tela de sucesso? A proposta exibe nome "
                 "completo, CPF mascarado, matrícula (quando servidor), curso, carga horária e data de "
                 "conclusão. Confirmar se a matrícula pode ser exibida publicamente."],
                "Cenário B do RF 4: código válido, com tela de sucesso confirmando as informações do "
                "documento.")
    b += s
    return "18-certificado-valido", svg("18-certificado-valido", W, y, b, WHITE)


# ================================================================ 19 INVALIDO
@reg
def t19():
    b = header_pub(None)
    y = HEAD_H
    b += rect(0, y, W, 150, NAVY)
    b += crumb_light(M, y + 44, ["Home", "Validar certificado", "Resultado"])
    b += txt(M, y + 96, "Resultado da validação", 30, WHITE, True)
    y += 150 + 44

    b += rect(M, y, CW, 132, RED_L, "#EBB7B1", 12, 1.4)
    b += rect(M, y, 6, 132, RED, None, 3)
    b += circ(M + 74, y + 66, 32, RED)
    b += path("M%s %s L%s %s M%s %s L%s %s" % (n(M + 62), n(y + 54), n(M + 86), n(y + 78),
                                               n(M + 86), n(y + 54), n(M + 62), n(y + 78)), None, WHITE, 4)
    b += txt(M + 126, y + 58, "Certificado não encontrado", 26, RED, True)
    b += para(M + 126, y + 88, "Verifique se o código foi digitado corretamente.", 700, 15, TXT, 22)
    y += 132 + 32

    fw = 700
    b += rect(M, y, fw, 380, WHITE, BORDER, 12, 1.4)
    b += txt(M + 36, y + 56, "Tentar novamente", 21, INK, True)
    s, _ = field(M + 36, y + 90, fw - 72, "Código de Autenticidade do Certificado",
                 "ELCMR-2026-A7K9-3F2X", req=True, h=56, ic="key",
                 err="Código não localizado na base de certificados emitidos.")
    b += s
    ry0 = y + 210
    b += rect(M + 36, ry0, 320, 78, "#F7FAFC", BORDER2, 8, 1.3)
    b += rect(M + 58, ry0 + 24, 28, 28, WHITE, BORDER2, 4, 1.5)
    b += txt(M + 100, ry0 + 44, "Não sou um robô", 14, TXT)
    b += rect(M + 290, ry0 + 18, 44, 44, "#E8EEF4", None, 6)
    b += icon_c("shield", M + 312, ry0 + 34, 20, "#4A6B8A", 1.8)
    b += btn(M + 36, y + 310, 240, 50, "Validar novamente", "primary", 15, "search", to="18")
    b += btn(M + 290, y + 310, 150, 50, "Limpar", "ghost", 15, to="17")

    rx = M + fw + 24
    rw = CW - fw - 24
    ry = y
    b += rect(rx, ry, rw, 380, WHITE, BORDER, 12, 1.2)
    b += txt(rx + 28, ry + 52, "Possíveis causas", 18, INK, True)
    for i, (t, d) in enumerate([("Erro de digitação", "Confira letras e números; o código tem 24 caracteres."),
                                ("Certificado ainda não liberado", "O gestor precisa emitir o certificado após o lançamento da frequência."),
                                ("Documento não emitido pela Escola", "O código só existe para certificados da Escola do Legislativo da CMR.")]):
        yy = ry + 84 + i * 82
        b += rect(rx + 28, yy, 6, 52, AMBER, None, 3)
        b += txt(rx + 46, yy + 16, t, 14, INK, True)
        b += para(rx + 46, yy + 36, d, rw - 90, 12.5, MUTED, 17)
    b += line(rx + 28, ry + 322, rx + rw - 28, ry + 322, "#EDF1F6", 1.2)
    b += icon("mail", rx + 28, ry + 340, 16, BLUE, 1.7)
    b += txt(rx + 52, ry + 352, "Fale com a Escola do Legislativo", 13, BLUE_D, True)
    ry += 380
    y = max(y + 380, ry) + 76
    s, y = footer_pub(y)
    b += s
    s, y = nota(y, W, ["RF 4 - Cenário A"], None,
                "Cenário A do RF 4: código inválido, com a mensagem exata definida no documento - "
                "'Certificado não encontrado. Verifique se o código foi digitado corretamente.'")
    b += s
    return "19-certificado-invalido", svg("19-certificado-invalido", W, y, b, WHITE)


# ================================================================ 20-21 PDF
def _pdf(nome, opcao, com_qr, titulo, desc, pros, contras):
    b = rect(0, 0, W, 150, NAVY)
    b += rect(0, 0, W, 4, GOLD)
    b += badge(M, 40, "DECISÃO EM REUNIÃO - RF 4", "solid-amber", 12, 28)[0]
    b += txt(M, 98, titulo, 28, WHITE, True)
    b += txt(M, 124, desc, 14, "#B7C7D6")
    b += rect(W - M - 120, 44, 120, 62, NAVY_3, GOLD, 8, 1.4)
    b += ctext(W - M - 60, 68, "OPÇÃO", 11, GOLD, True)
    b += ctext(W - M - 60, 92, opcao, 24, WHITE, True)
    y = 150 + 44
    cw2 = 1000
    cx = (W - cw2) / 2.0
    b += rect(cx - 14, y - 14, cw2 + 28, 796, BG2, None, 8)
    b += certificado(cx, y, cw2, 768, com_qr)
    y += 768 + 44
    colw = (CW - 24) / 2.0
    for i, (t, items, kind, ic) in enumerate([("Vantagens", pros, "ok", "check"),
                                              ("Pontos de atenção", contras, "warn", "alert")]):
        x = M + i * (colw + 24)
        h = 76 + len(items) * 46
        bgc, stc, fg, _ic = ALERTS[kind]
        b += rect(x, y, colw, h, bgc, stc, 10, 1.2)
        b += icon(ic, x + 24, y + 26, 20, fg, 1.9)
        b += txt(x + 54, y + 42, t, 16, fg, True)
        for j, it in enumerate(items):
            b += circ(x + 30, y + 78 + j * 46, 3.5, fg)
            b += para(x + 46, y + 82 + j * 46, it, colw - 80, 13, TXT, 18)
    y += 76 + max(len(pros), len(contras)) * 46 + 60
    s, y = nota(y, W, ["RF 4 - Geração do código de autenticidade"],
                ["Escolher entre a Opção 1 (somente código alfanumérico + URL) e a Opção 2 "
                 "(código + QR Code com validação instantânea) para impressão no PDF do certificado."],
                "O código identificador único e alfanumérico é gerado automaticamente pelo sistema no "
                "momento da emissão do certificado pelo gestor e consta no rodapé do PDF junto à URL "
                "da página de validação.")
    b += s
    return nome, svg(nome, W, y, b, WHITE)


@reg
def t20():
    return _pdf("20-certificado-pdf-opcao1-codigo", "1", False,
                "Modelo do certificado em PDF - Opção 1: somente código",
                "O interessado acessa o portal e digita o código manualmente na área de validação.",
                ["Layout mais limpo e tradicional, sem elemento gráfico adicional.",
                 "Não depende de câmera nem de leitor de QR Code.",
                 "Menor custo de implementação e de impressão."],
                ["Exige digitação manual de 24 caracteres, com risco de erro.",
                 "Mais passos até o resultado da validação.",
                 "Menos prático para conferência presencial rápida."])


@reg
def t21():
    return _pdf("21-certificado-pdf-opcao2-qrcode", "2", True,
                "Modelo do certificado em PDF - Opção 2: código + QR Code",
                "Ao ler o QR Code, o verificador vai direto para a página com o resultado da validação.",
                ["Validação instantânea pela câmera do celular.",
                 "Elimina erro de digitação do código.",
                 "Mantém o código alfanumérico como alternativa manual.",
                 "Padrão adotado por outras escolas do legislativo."],
                ["Exige geração e armazenamento da imagem do QR no PDF.",
                 "A URL do portal precisa ser estável e pública.",
                 "Requer proteção contra varredura automatizada (reCAPTCHA)."])
