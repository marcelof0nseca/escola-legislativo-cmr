# -*- coding: utf-8 -*-
"""Telas 22-28: login, cadastro e recuperacao de senha (RF 5 e RF 6)."""
from blocks import *

TELAS = []


def reg(fn):
    TELAS.append(fn)
    return fn


def atalhos(y, w, titulo, items):
    """Faixa de atalhos de prototipo (grupo ATALHOS-PROTOTIPO, apagavel no Figma)."""
    h = 108
    inner = rect(0, y, w, h, GOLD_L)
    inner += rect(0, y, w, 2, GOLD)
    inner += rect(0, y + h - 2, w, 2, GOLD)
    inner += icon("info", M, y + 30, 18, "#8A6414", 1.8)
    inner += txt(M + 26, y + 44, titulo, 13.5, "#8A6414", True)
    cx = M
    for lbl, kind, dst in items:
        wd = tw(lbl, 13.5, True) + 52
        inner += btn(cx, y + 58, wd, 40, lbl, kind, 13.5, "arrow-r", to=dst)
        cx += wd + 12
    inner += txt(w - M, y + 84, "Ligue cada botão ao frame correspondente no modo Prototype",
                 12, "#8A6414", anchor="end")
    return grp(inner, "ATALHOS-PROTOTIPO"), y + h


def _split(titulo, chamada, bullets, h=980):
    """Painel institucional a esquerda das telas de acesso."""
    pw = 560
    b = rect(0, 0, pw, h, NAVY)
    b += rect(0, 0, 4, h, GOLD)
    b += rect(64, 64, 52, 52, NAVY_3, None, 9)
    b += icon_c("board", 90, 90, 26, GOLD, 1.9)
    b += txt(128, 84, "Escola do Legislativo", 17, WHITE, True)
    b += txt(128, 104, "Câmara Municipal do Recife", 12.5, "#8FA6BA")
    b += txt(64, 232, titulo, 34, WHITE, True)
    b += para(64, 274, chamada, pw - 128, 15, "#B7C7D6", 24)
    yy = 380
    for ic, t, d in bullets:
        b += rect(64, yy, 42, 42, NAVY_3, None, 8)
        b += icon_c(ic, 85, yy + 21, 20, GOLD, 1.8)
        b += txt(120, yy + 18, t, 15, WHITE, True)
        b += para(120, yy + 40, d, pw - 190, 13, "#8FA6BA", 18)
        yy += 92
    b += line(64, h - 130, pw - 64, h - 130, "#27476A", 1.2)
    b += icon("shield", 64, h - 106, 18, GOLD, 1.7)
    b += para(92, h - 94, "Seus dados são tratados conforme a LGPD (Lei 13.709/2018) e usados apenas "
                          "para gestão das capacitações da Escola.", pw - 160, 12.5, "#8FA6BA", 18)
    return b, pw


# ================================================================ 22 LOGIN
@reg
def t22():
    H = 980
    b, pw = _split("Bem-vindo à Área Restrita",
                   "Acesse para se inscrever em cursos, acompanhar suas turmas e baixar seus certificados.",
                   [("calendar", "Inscrições on-line", "Garanta sua vaga nas turmas com inscrições abertas."),
                    ("cert", "Certificados digitais", "Baixe a qualquer momento, com código de autenticidade."),
                    ("users", "Um cadastro só", "Servidores da CMR, de outros órgãos e público externo.")], H)
    fx = pw + 190
    fw = 440
    b += rect(pw, 0, W - pw, H, WHITE)
    hot(W - 220, 40, 170, 30, "01", "Voltar ao portal")
    b += txt(W - 64, 56, "Voltar ao portal", 13.5, BLUE_D, True, anchor="end")
    b += icon("arrow-l", W - 64 - tw("Voltar ao portal", 13.5, True) - 24, 44, 15, BLUE_D, 1.8)
    y = 138
    b += txt(fx, y, "Entrar", 32, INK, True)
    b += txt(fx, y + 30, "Informe suas credenciais de acesso ao portal.", 14.5, MUTED)
    y += 76
    s, y = field(fx, y, fw, "CPF", "123.456.789-00", req=True, h=52, ic="user",
                 helper="Identificador principal de acesso (ver decisão em reunião).")
    b += s
    y += 18
    s, y = field(fx, y, fw, "Senha", "12345678", req=True, h=52, kind="password", ic="lock")
    b += s
    b += icon("eye", fx + fw - 38, y - 35, 18, MUTED, 1.7)
    y += 24
    b += checkbox(fx, y, "Manter minha sessão", False)
    b += txt(fx + 28, y + 34, "A sessão permanece por 7 dias.", 12, MUTED)
    b += link(fx + fw - tw("Esqueci minha senha", 13.5), y + 14, "Esqueci minha senha", 13.5,
              BLUE_D, to="26")
    y += 74
    b += btn(fx, y, fw, 54, "Entrar", "primary", 16, hot=True, to="29")
    y += 54 + 34
    b += line(fx, y, fx + fw / 2.0 - 24, y, BORDER, 1.2)
    b += ctext(fx + fw / 2.0, y, "ou", 13, MUTED)
    b += line(fx + fw / 2.0 + 24, y, fx + fw, y, BORDER, 1.2)
    y += 26
    b += btn(fx, y, fw, 52, "Entrar com a rede da Câmara (Single Sign-On)", "ghost", 13.5,
             "lock", to="29")
    b += txt(fx, y + 74, "Exclusivo para servidores da CMR, usando o login e a senha da rede interna.",
             12.5, MUTED)
    y += 108
    b += line(fx, y, fx + fw, y, BORDER, 1.2)
    y += 34
    b += txt(fx, y, "Ainda não tem cadastro?", 14, TXT)
    b += link(fx + tw("Ainda não tem cadastro?", 14) + 8, y, "Cadastre-se", 14, BLUE_D, True,
              True, to="24")
    y += 34
    b += icon("info", fx, y, 16, MUTED, 1.7)
    b += para(fx + 24, y + 12, "Se você chegou aqui pelo botão Inscrever-se de um curso, após entrar "
                               "você volta direto para a confirmação da inscrição.", fw - 24, 12.5, MUTED, 18)
    y = H
    s, y = atalhos(y, W, "Atalhos do protótipo - simular o acesso de cada perfil:",
                   [("Entrar como Aluno", "primary", "29"), ("Entrar como Gestor", "dark", "39"),
                    ("Entrar como Professor", "gold", "53")])
    b += s
    s, y = nota(y, W, ["RF 5"],
                ["RF 5 - Qual será o identificador principal de acesso: CPF (Opção 1, recomendada, "
                 "garante unicidade) ou e-mail (Opção 2, padrão de mercado)? A tela está desenhada com CPF.",
                 "RF 5 - Servidores da CMR usarão as credenciais da rede interna (LDAP/Active Directory - "
                 "Single Sign-On) ou o portal terá banco de senhas isolado? O botão de SSO está previsto."],
                "Campos exigidos no RF 5: login, senha com ocultação de caracteres, checkbox 'Manter "
                "minha sessão' (7 dias) e link 'Esqueci minha senha'. O botão Entrar/Login também "
                "aparece no cabeçalho de todas as páginas públicas.")
    b += s
    return "22-login", svg("22-login", W, y, b, WHITE)


# ================================================================ 23 LOGIN ERRO
@reg
def t23():
    H = 980
    b, pw = _split("Bem-vindo à Área Restrita",
                   "Acesse para se inscrever em cursos, acompanhar suas turmas e baixar seus certificados.",
                   [("shield", "Mensagem genérica", "O sistema não informa qual campo está errado."),
                    ("lock", "Bloqueio temporário", "Proteção contra tentativas automatizadas."),
                    ("key", "Recuperação segura", "Link único e temporário enviado por e-mail.")], H)
    fx = pw + 190
    fw = 440
    b += rect(pw, 0, W - pw, H, WHITE)
    y = 120
    b += txt(fx, y, "Entrar", 32, INK, True)
    y += 44
    s, y = alert(fx, y, fw, "Usuário ou senha incorretos.",
                 "Você tem mais 2 tentativas antes do bloqueio temporário da conta.", "erro")
    b += s
    y += 28
    s, y = field(fx, y, fw, "CPF", "123.456.789-00", req=True, h=52, ic="user", err=" ")
    b += s
    y += 6
    s, y = field(fx, y, fw, "Senha", "1234", req=True, h=52, kind="password", ic="lock",
                 err="Verifique suas credenciais e tente novamente.")
    b += s
    y += 20
    b += checkbox(fx, y, "Manter minha sessão", False)
    hot(fx + fw - tw("Esqueci minha senha", 13.5) - 8, y, tw("Esqueci minha senha", 13.5) + 16,
        26, "26", "Esqueci minha senha")
    b += txt(fx + fw - tw("Esqueci minha senha", 13.5), y + 14, "Esqueci minha senha", 13.5, BLUE_D)
    b += line(fx + fw - tw("Esqueci minha senha", 13.5), y + 18, fx + fw, y + 18, BLUE_D, 1)
    y += 56
    b += btn(fx, y, fw, 54, "Entrar", "primary", 16, to="29")
    y += 54 + 40
    b += rect(fx, y, fw, 200, AMBER_L, "#EBCE95", 10, 1.2)
    b += icon("lock", fx + 22, y + 24, 22, AMBER, 1.8)
    b += txt(fx + 56, y + 42, "Política de bloqueio (proposta)", 15, AMBER, True)
    for i, t in enumerate(["Após 5 tentativas consecutivas malsucedidas, a conta é bloqueada por 30 minutos.",
                           "O aluno pode liberar o acesso antes disso usando 'Esqueci minha senha'.",
                           "As tentativas são registradas em log de segurança com data, hora e IP."]):
        b += circ(fx + 30, y + 84 + i * 38, 3.5, AMBER)
        b += para(fx + 46, y + 88 + i * 38, t, fw - 76, 12.5, TXT, 17)
    y = H
    s, y = nota(y, W, ["RF 5 - Cenário B"],
                ["RF 5 - Confirmar a política de bloqueio: bloquear a conta por 30 minutos após 5 "
                 "tentativas consecutivas malsucedidas? Confirmar número de tentativas e tempo."],
                "Cenário B do RF 5: mensagem de erro genérica ('Usuário ou senha incorretos.'), sem "
                "indicar qual campo está errado, para evitar varredura de CPF/e-mail.")
    b += s
    return "23-login-erro-e-bloqueio", svg("23-login-erro-e-bloqueio", W, y, b, WHITE)


# ================================================================ 24 CADASTRO
@reg
def t24():
    b = header_pub(None)
    s, y = page_hero(HEAD_H, "Criar cadastro no portal",
                     "Um único cadastro dá acesso às inscrições, ao histórico de cursos e aos certificados",
                     ["Home", "Entrar / Cadastre-se", "Criar cadastro"], 176)
    b += s
    y += 44
    lw = 800
    rx = M + lw + 40
    rw = CW - lw - 40

    # passos
    b += rect(M, y, lw, 84, WHITE, BORDER, 10, 1.2)
    for i, (t, on) in enumerate([("1. Seus dados", True), ("2. Confirmação", False), ("3. Pronto", False)]):
        x = M + 32 + i * 250
        b += circ(x + 14, y + 42, 15, BLUE if on else "#E6ECF2")
        b += ctext(x + 14, y + 42, str(i + 1), 13.5, WHITE if on else MUTED, True)
        b += txt(x + 38, y + 47, t[3:], 14, INK if on else MUTED, on)
        if i < 2:
            b += line(x + 190, y + 42, x + 240, y + 42, BORDER2, 1.5)
    y += 84 + 24

    b += rect(M, y, lw, 900, WHITE, BORDER, 12, 1.2)
    b += txt(M + 32, y + 52, "Dados do aluno", 22, INK, True)
    b += txt(M + 32, y + 76, "Campos marcados com * são obrigatórios.", 13, MUTED)
    fy = y + 108
    hw = (lw - 64 - 20) / 2.0
    s, _ = field(M + 32, fy, lw - 64, "Nome completo", "Maria Silva dos Santos", req=True,
                 helper="Texto, até 150 caracteres. Será impresso no certificado.")
    b += s
    fy += 106
    s, _ = field(M + 32, fy, hw, "CPF", "123.456.789-00", req=True,
                 helper="11 dígitos. Chave única, com validação de algoritmo.")
    b += s
    s, _ = field(M + 32 + hw + 20, fy, hw, "E-mail", "maria.santos@email.com", req=True, ic="mail",
                 helper="Até 100 caracteres, com validação de formato.")
    b += s
    fy += 106
    s, _ = field(M + 32, fy, hw, "Telefone / WhatsApp", "(81) 99999-0000", req=True, ic="phone",
                 helper="Até 15 caracteres, com máscara.")
    b += s
    s, _ = field(M + 32 + hw + 20, fy, hw, "Tipo de vínculo", "Servidor da Câmara Municipal do Recife",
                 req=True, kind="select",
                 helper="Servidor da CMR / de outro órgão / público externo.")
    b += s
    fy += 106
    b += rect(M + 32, fy - 14, lw - 64, 128, BLUE_L, "#A9CBE8", 8, 1.2)
    s, _ = field(M + 48, fy + 4, hw - 16, "Matrícula", "20.451-7", req=True,
                 helper="Até 20 caracteres.")
    b += s
    b += icon("info", M + 48 + hw + 20, fy + 18, 17, BLUE_D, 1.8)
    b += txt(M + 74 + hw + 20, fy + 32, "Campo condicional", 13, BLUE_D, True)
    b += para(M + 48 + hw + 20, fy + 56, "Exibido e obrigatório apenas quando o tipo de vínculo for "
                                          "'Servidor da Câmara Municipal do Recife'.", hw - 32, 12.5, TXT, 17)
    fy += 142
    s, _ = field(M + 32, fy, hw, "Senha", "12345678", req=True, kind="password", ic="lock",
                 helper="Mínimo 8 caracteres, com letras e números.")
    b += s
    s, _ = field(M + 32 + hw + 20, fy, hw, "Confirmar senha", "12345678", req=True, kind="password", ic="lock",
                 helper="Repita a senha digitada acima.")
    b += s
    fy += 112
    b += line(M + 32, fy, M + lw - 32, fy, "#EDF1F6", 1.2)
    fy += 26
    b += checkbox(M + 32, fy, "Li e aceito os Termos de Uso e a Política de Privacidade do portal.", True)
    fy += 34
    b += checkbox(M + 32, fy, "Autorizo o envio de e-mails sobre novas turmas e eventos da Escola.", False)
    fy += 44
    b += rect(M + 32, fy, 320, 78, "#F7FAFC", BORDER2, 8, 1.3)
    b += rect(M + 54, fy + 24, 28, 28, WHITE, BORDER2, 4, 1.5)
    b += txt(M + 96, fy + 44, "Não sou um robô", 14, TXT)
    b += rect(M + 286, fy + 18, 44, 44, "#E8EEF4", None, 6)
    b += icon_c("shield", M + 308, fy + 34, 20, "#4A6B8A", 1.8)
    b += btn(M + 372, fy, 240, 54, "Criar meu cadastro", "primary", 16, hot=True, to="25")
    b += btn(M + 626, fy, 140, 54, "Cancelar", "ghost", 15)

    ry = y
    s, ry = alert(rx, ry, rw, "Por que pedimos estes dados?",
                  "A LGPD determina que os dados tratados tenham finalidade específica. Cada campo aqui "
                  "existe para emitir certificado, controlar vagas ou comunicar mudanças de turma.", "lgpd")
    b += s
    ry += 20
    b += rect(rx, ry, rw, 320, WHITE, BORDER, 12, 1.2)
    b += txt(rx + 26, ry + 46, "Finalidade de cada dado", 17, INK, True)
    for i, (d, f) in enumerate([("Nome completo", "Impressão no certificado"),
                                ("CPF", "Identificação única e validação"),
                                ("E-mail", "Login, avisos e recuperação de senha"),
                                ("Telefone/WhatsApp", "Aviso de mudança de turma"),
                                ("Tipo de vínculo", "Reserva de vagas por público"),
                                ("Matrícula", "Vínculo funcional na CMR")]):
        yy = ry + 74 + i * 40
        b += circ(rx + 32, yy, 3.5, GOLD)
        b += txt(rx + 46, yy + 5, d, 12.5, INK, True)
        b += txt(rx + 46 + tw(d, 12.5, True) + 8, yy + 5, "· " + f, 12, MUTED)
    ry += 320 + 20
    b += rect(rx, ry, rw, 176, "#F7FAFC", BORDER, 12, 1.2)
    b += txt(rx + 26, ry + 44, "Já tem cadastro?", 17, INK, True)
    b += para(rx + 26, ry + 68, "Use seu CPF e senha para entrar. Se esqueceu a senha, recupere pelo e-mail cadastrado.",
              rw - 52, 13, MUTED, 19)
    b += btn(rx + 26, ry + 118, rw - 52, 44, "Ir para o login", "secondary", 14, "arrow-r",
             to="22")
    ry += 176
    y = max(y + 900, ry) + 70
    s, y = footer_pub(y)
    b += s
    s, y = nota(y, W, ["RF 6"],
                ["RF 6 - Modelo de acesso: cadastro único com login/senha (Opção 1, permite Área do "
                 "Aluno com histórico e certificados) ou formulário aberto a cada curso (Opção 2, sem "
                 "histórico)? Todo o protótipo está desenhado na Opção 1.",
                 "RF 6 - Confirmar a lista final de dados coletados no cadastro, à luz da finalidade "
                 "específica exigida pela LGPD."],
                "Campos previstos no RF 6: Nome Completo (150), CPF (11, chave única com validação de "
                "algoritmo), E-mail (100), Telefone/WhatsApp (15), Tipo de Vínculo, Matrícula (20, "
                "condicional ao vínculo com a CMR) e Senha (armazenada com hash criptografado).")
    b += s
    return "24-cadastro-aluno", svg("24-cadastro-aluno", W, y, b, WHITE)


# ================================================================ 25 CADASTRO OK
@reg
def t25():
    b = header_pub(None)
    y = HEAD_H
    b += rect(0, y, W, 120, NAVY)
    y += 120 + 70
    cw2 = 800
    cx = (W - cw2) / 2.0
    b += rect(cx, y, cw2, 520, WHITE, BORDER, 14, 1.4)
    b += rect(cx, y, cw2, 8, GREEN, None, 14)
    b += rect(cx, y + 4, cw2, 4, GREEN)
    b += circ(cx + cw2 / 2.0, y + 96, 44, GREEN_L)
    b += path("M%s %s l14 15 L%s %s" % (n(cx + cw2 / 2.0 - 20), n(y + 96), n(cx + cw2 / 2.0 + 22), n(y + 80)),
              None, GREEN, 5)
    b += ctext(cx + cw2 / 2.0, y + 176, "Cadastro criado com sucesso!", 28, INK, True)
    b += ctext(cx + cw2 / 2.0, y + 212, "Enviamos um e-mail de confirmação para maria.santos@email.com",
               15, MUTED)
    b += rect(cx + 60, y + 250, cw2 - 120, 96, BLUE_L, "#A9CBE8", 10, 1.2)
    b += icon("arrow-r", cx + 84, y + 286, 20, BLUE_D, 1.9)
    b += txt(cx + 116, y + 288, "Você estava se inscrevendo em um curso", 15, BLUE_D, True)
    b += txt(cx + 116, y + 312, "Processo Legislativo Municipal · Turma B - Noite · 14 e 15/09/2026",
             13.5, TXT)
    b += btn(cx + 60, y + 378, 340, 54, "Continuar a inscrição no curso", "primary", 15.5,
             hot=True, to="30")
    b += btn(cx + 416, y + 378, 200, 54, "Ir para Área do Aluno", "secondary", 15, to="29")
    b += btn(cx + 632, y + 378, 108, 54, "Início", "ghost", 15, to="01")
    b += ctext(cx + cw2 / 2.0, y + 470, "Guarde seu CPF e sua senha: são eles que dão acesso ao portal.",
               12.5, MUTED)
    y += 520 + 80
    s, y = footer_pub(y)
    b += s
    s, y = nota(y, W, ["RF 5 - Cenário A", "RF 6", "RF 7"], None,
                "Após o cadastro/login originado do botão Inscrever-se, o sistema redireciona de volta "
                "para a confirmação da inscrição no curso específico; caso contrário, vai para a página "
                "inicial da Área do Aluno.")
    b += s
    return "25-cadastro-confirmacao", svg("25-cadastro-confirmacao", W, y, b, WHITE)


# ================================================================ 26-28 SENHA
def _senha_shell(h=880):
    b = rect(0, 0, W, h, WHITE)
    b += rect(0, 0, W, 120, NAVY)
    b += rect(M, 34, 52, 52, NAVY_3, None, 9)
    b += icon_c("board", M + 26, 60, 26, GOLD, 1.9)
    b += txt(M + 64, 54, "Escola do Legislativo", 17, WHITE, True)
    b += txt(M + 64, 74, "Câmara Municipal do Recife", 12.5, "#8FA6BA")
    hot(W - M - 130, 48, 140, 32, "22", "Voltar ao login")
    b += txt(W - M, 66, "Voltar ao login", 13.5, "#B7C7D6", anchor="end")
    return b


@reg
def t26():
    H = 780
    b = _senha_shell(H)
    cw2 = 560
    cx = (W - cw2) / 2.0
    y = 190
    b += rect(cx, y, cw2, 470, WHITE, BORDER, 14, 1.4)
    b += rect(cx + 40, y + 44, 54, 54, BLUE_L, None, 10)
    b += icon_c("key", cx + 67, y + 71, 26, BLUE, 1.9)
    b += txt(cx + 40, y + 140, "Esqueci minha senha", 26, INK, True)
    b += para(cx + 40, y + 172, "Informe o identificador cadastrado. Se ele existir na base, enviaremos "
                                "um link de recuperação para o e-mail vinculado à conta.",
              cw2 - 80, 14, MUTED, 21)
    s, _ = field(cx + 40, y + 248, cw2 - 80, "CPF ou e-mail cadastrado", "123.456.789-00",
                 req=True, h=52, ic="user")
    b += s
    b += btn(cx + 40, y + 348, cw2 - 80, 54, "Enviar link de recuperação", "primary", 15.5,
             "mail", hot=True, to="27")
    b += line(cx + 40, y + 428, cx + cw2 - 40, y + 428, BORDER, 1.2)
    b += ctext(cx + cw2 / 2.0, y + 450, "Lembrou a senha? Voltar para o login", 13, BLUE_D)
    y = H
    s, y = nota(y, W, ["RF 5 - Recuperação de senha"], None,
                "O sistema solicita o identificador do usuário (CPF ou e-mail). Por segurança, a "
                "resposta é sempre a mesma, exista ou não o identificador na base.")
    b += s
    return "26-senha-esqueci", svg("26-senha-esqueci", W, y, b, WHITE)


@reg
def t27():
    H = 780
    b = _senha_shell(H)
    cw2 = 560
    cx = (W - cw2) / 2.0
    y = 190
    b += rect(cx, y, cw2, 462, WHITE, BORDER, 14, 1.4)
    b += circ(cx + cw2 / 2.0, y + 88, 40, GREEN_L)
    b += icon_c("mail", cx + cw2 / 2.0, y + 88, 34, GREEN, 2)
    b += ctext(cx + cw2 / 2.0, y + 168, "Verifique seu e-mail", 26, INK, True)
    b += ctext(cx + cw2 / 2.0, y + 204, "Se o identificador informado estiver cadastrado, enviamos", 14, MUTED)
    b += ctext(cx + cw2 / 2.0, y + 226, "um link de recuperação para  m****@email.com", 14, MUTED)
    b += rect(cx + 40, y + 258, cw2 - 80, 76, AMBER_L, "#EBCE95", 10, 1.2)
    b += icon("clock", cx + 60, y + 284, 20, AMBER, 1.8)
    b += txt(cx + 90, y + 288, "O link é válido por 2 horas", 14, AMBER, True)
    b += txt(cx + 90, y + 312, "Depois disso será necessário solicitar um novo link.", 12.5, TXT)
    b += btn(cx + 40, y + 356, cw2 - 80, 50, "Voltar para o login", "primary", 15, to="22")
    hot(cx + 40, y + 258, cw2 - 80, 76, "28", "abrir link do e-mail")
    b += ctext(cx + cw2 / 2.0, y + 436, "Não recebeu? Reenviar em 00:59", 13, MUTED)
    y = H
    s, y = nota(y, W, ["RF 5 - Recuperação de senha"], None,
                "O sistema gera um token único, criptografado e temporário (validade de 2 horas) e "
                "envia o link para o e-mail cadastrado do usuário.")
    b += s
    return "27-senha-link-enviado", svg("27-senha-link-enviado", W, y, b, WHITE)


@reg
def t28():
    H = 880
    b = _senha_shell(H)
    cw2 = 560
    cx = (W - cw2) / 2.0
    y = 178
    b += rect(cx, y, cw2, 590, WHITE, BORDER, 14, 1.4)
    b += rect(cx + 40, y + 40, 54, 54, GREEN_L, None, 10)
    b += icon_c("lock", cx + 67, y + 67, 26, GREEN, 1.9)
    b += txt(cx + 40, y + 136, "Criar nova senha", 26, INK, True)
    b += para(cx + 40, y + 166, "Link validado para Maria Silva dos Santos. Defina uma nova senha de acesso.",
              cw2 - 80, 14, MUTED, 21)
    s, _ = field(cx + 40, y + 216, cw2 - 80, "Nova senha", "12345678", req=True, h=52,
                 kind="password", ic="lock")
    b += s
    s, _ = field(cx + 40, y + 306, cw2 - 80, "Confirmar nova senha", "12345678", req=True, h=52,
                 kind="password", ic="lock")
    b += s
    b += rect(cx + 40, y + 392, cw2 - 80, 108, "#F7FAFC", BORDER, 8, 1.2)
    b += txt(cx + 58, y + 420, "A senha deve conter:", 12.5, INK, True)
    for i, (t, ok) in enumerate([("Mínimo de 8 caracteres", True), ("Ao menos uma letra e um número", True),
                                 ("Diferente das 3 últimas senhas usadas", False)]):
        x = cx + 58 + (i % 2) * 240
        yy = y + 444 + (i // 2) * 26
        b += circ(x + 6, yy - 4, 7, GREEN_L if ok else "#E6ECF2")
        if ok:
            b += path("M%s %s l2.4 2.6 L%s %s" % (n(x + 2.6), n(yy - 4), n(x + 9.6), n(yy - 8.6)), None, GREEN, 1.8)
        b += txt(x + 20, yy, t, 12, GREEN if ok else MUTED)
    b += btn(cx + 40, y + 522, cw2 - 80, 54, "Salvar nova senha", "primary", 15.5, hot=True,
             to="22")
    y = H
    s, y = nota(y, W, ["RF 5 - Recuperação de senha"], None,
                "Tela segura acessada pelo link recebido por e-mail. Após o uso, o sistema invalida o "
                "link e a senha é gravada com hash criptografado.")
    b += s
    return "28-senha-nova", svg("28-senha-nova", W, y, b, WHITE)
