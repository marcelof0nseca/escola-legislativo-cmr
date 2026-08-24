# -*- coding: utf-8 -*-
"""Gera todos os SVGs, o guia de navegacao, a matriz de requisitos e o preview."""
import io
import os
import re

import t_pub1
import t_pub2
import t_auth
import t_aluno
import t_gestor
import t_prof
import t_apoio
import ds
import proto_html
from dados import TELAS as INV, MODULOS, LINKS, DECISOES, TELA_POR_NUM

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(RAIZ, "figma-telas")

FUNCS = (t_pub1.TELAS + t_pub2.TELAS + t_auth.TELAS + t_aluno.TELAS +
         t_gestor.TELAS + t_prof.TELAS + t_apoio.TELAS)


def w(path, txt):
    with io.open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(txt)


def build_svgs():
    if not os.path.isdir(OUT):
        os.makedirs(OUT)
    feitos, hots = {}, {}
    for fn in FUNCS:
        ds.HOTS[:] = []
        nome, s = fn()
        w(os.path.join(OUT, nome + ".svg"), s)
        m = re.search(r'width="(\d+)" height="(\d+)"', s)
        feitos[nome] = (int(m.group(1)), int(m.group(2)), len(s))
        hots[nome] = [list(h) for h in ds.HOTS]
    return feitos, hots


def build_guia(dims, nhots=0):
    L = []
    A = L.append
    A("# Guia de navegação no Figma — Portal da Escola do Legislativo")
    A("")
    A("Câmara Municipal do Recife · Divisão de Informática · processo nº 3096/2025")
    A("")
    A("São **%d frames** na pasta `figma-telas/`, cobrindo todos os requisitos do documento "
      "preliminar de especificação." % len(INV))
    A("")
    A("## 0. Ver o protótipo navegando (sem Figma)")
    A("")
    A("Abra **`prototipo.html`** no navegador (duplo clique, ou botão direito → *Open with Live Server* "
      "no VS Code). Ele já vem navegável: os botões, menus, abas e cards são clicáveis e levam para a "
      "tela de destino, com **%d áreas clicáveis** distribuídas nas %d telas." % (nhots, len(INV)))
    A("")
    A("| Recurso | Como usar |")
    A("|---|---|")
    A("| Navegar | Clique nos botões, menus, abas e cards da própria tela |")
    A("| Ver o que é clicável | Botão **Áreas clicáveis** no topo, ou tecla `H` |")
    A("| Descobrir os cliques | Clique em qualquer área vazia: os pontos de clique piscam |")
    A("| Pular para uma tela | Lista suspensa no topo, agrupada por módulo |")
    A("| Tela anterior / próxima | Setas do topo ou `←` `→` do teclado |")
    A("| Link direto para uma tela | `prototipo.html#30` abre a tela 30 |")
    A("")
    A("`preview.html` é diferente: mostra as 57 telas lado a lado, em galeria, para conferência rápida.")
    A("")
    A("> Os arquivos `.svg` sozinhos **não** são navegáveis — são imagens. Quem dá a navegação é o "
      "`prototipo.html` (no navegador) ou o modo Prototype do Figma (item 3 abaixo).")
    A("")
    A("## 1. Como importar no Figma")
    A("")
    A("1. Crie um arquivo novo no Figma (`Design file`).")
    A("2. Selecione **todos** os arquivos `.svg` da pasta `figma-telas/` e arraste para dentro do canvas.")
    A("3. Cada arquivo vira **um Frame** já com o nome correto (`01-home`, `02-cursos-vitrine`, ...).")
    A("   Se algum vier como Group, selecione e use `Selection to frame` (Shift+A) mantendo o nome.")
    A("4. Organize os frames em colunas por módulo — a ordem numérica já segue o fluxo.")
    A("5. Aba **Prototype** → selecione o botão/área clicável → arraste a setinha até o frame de destino")
    A("   → `On click` · `Navigate to` · `Instant` (ou `Smart Animate`).")
    A("")
    A("> Dica: para telas com modal (35 e 44), use `Open overlay` em vez de `Navigate to` se quiser o "
      "efeito de sobreposição.")
    A("")
    A("### Grupos que podem ser apagados")
    A("")
    A("Cada frame tem, no rodapé, um grupo chamado `NOTA-ANALISE` (faixa escura com os requisitos "
      "atendidos e as decisões pendentes). Ele existe para a apresentação e para a reunião de "
      "requisitos. Se quiser mostrar só a interface, selecione o grupo na camada e apague — em um "
      "clique por frame. A tela `22-login` também tem o grupo `ATALHOS-PROTOTIPO`, com os botões de "
      "simulação de perfil.")
    A("")
    A("## 2. Inventário de frames")
    A("")
    A("| # | Frame | Tela | Módulo | Requisitos | Dimensões |")
    A("|---|---|---|---|---|---|")
    mod_nome = {m[0]: m[1] for m in MODULOS}
    for num, arq, titulo, mod, rf in INV:
        d = dims.get(arq)
        dim = "%d × %d" % (d[0], d[1]) if d else "-"
        A("| %s | `%s` | %s | %s | %s | %s |" % (num, arq, titulo, mod_nome[mod], rf, dim))
    A("")
    A("## 3. Ligações do protótipo (%d)" % len(LINKS))
    A("")
    A("Monte estas ligações no modo Prototype. A coluna **Elemento** indica o que deve receber o link.")
    A("")
    atual = None
    for org, elem, dst, obs in LINKS:
        if org != atual:
            atual = org
            t = TELA_POR_NUM[org]
            A("")
            A("### De `%s` — %s" % (t[1], t[2]))
            A("")
            A("| Elemento clicável | Frame de destino | Observação |")
            A("|---|---|---|")
        td = TELA_POR_NUM[dst]
        A("| %s | `%s` | %s |" % (elem, td[1], obs or "—"))
    A("")
    A("## 4. Roteiro sugerido para a apresentação")
    A("")
    roteiro = [
        ("Abertura", "56-mapa-de-navegacao", "Mostrar o mapa: 57 telas, 5 módulos, o que cada um cobre."),
        ("O portal público", "01-home", "Vitrine de cursos, notícias, busca rápida e acessos rápidos."),
        ("Agenda e filtros", "02-cursos-vitrine → 03 → 04", "Filtros por mês, tema e público; aba de realizados."),
        ("Página do curso", "05 → 06 → 07", "Ementa, professor, cronograma e turmas."),
        ("Inscrição", "05 → 22 → 24 → 25 → 30 → 32", "Fluxo completo do aluno novo até a confirmação."),
        ("Sem vaga", "30 → 31 → 33", "Turma esgotada, outra turma com vaga e fila de espera."),
        ("Área do aluno", "29 → 34 → 35 → 36 → 37", "Meus cursos, cancelamento, materiais e certificados."),
        ("Certificação", "37 → 21 → 17 → 18 / 19", "Certificado, código de autenticidade e validação pública."),
        ("Área do gestor", "39 → 40 → 41 → 42 → 43 → 44", "Cursos, turmas, inscrições e log de cancelamento."),
        ("Operação", "45 → 46 → 47", "Fila de espera, frequência e emissão de certificados."),
        ("Conteúdo", "48 → 49 → 50 → 51 → 52", "Professores, notícias, acervo, parceiras e relatórios."),
        ("Professor", "53 → 54 → 55", "Acesso restrito: alunos inscritos e upload de materiais."),
        ("Fechamento", "57-decisoes-em-reuniao", "As 14 decisões que precisam ser fechadas na reunião."),
    ]
    A("| Momento | Frames | O que mostrar |")
    A("|---|---|---|")
    for a, bq, c in roteiro:
        A("| %s | `%s` | %s |" % (a, bq, c))
    A("")
    A("## 5. Decisões pendentes")
    A("")
    A("Estão detalhadas no frame `57-decisoes-em-reuniao` e resumidas em `decisoes-em-reuniao.md`.")
    A("")
    return "\n".join(L) + "\n"


def build_matriz():
    L = []
    A = L.append
    A("# Matriz de rastreabilidade — requisitos × telas")
    A("")
    A("Portal da Escola do Legislativo · Câmara Municipal do Recife · processo nº 3096/2025")
    A("")
    itens = [
        ("Estrutura · HOME", "Aba de cursos e eventos (carrossel), aba de notícias em destaque, barra "
         "de busca rápida, ícones de acesso rápido Validar Certificado e Área do Aluno", "01, 16"),
        ("Estrutura · A ESCOLA", "Quem Somos, História, Legislação e Transparência (Parcerias/Convênios)",
         "10, 11, 12, 13"),
        ("Estrutura · ACERVO/BIBLIOTECA", "Publicações, Manuais, Legislações", "14, 50"),
        ("Estrutura · ÁREA DO ALUNO", "Meus Cursos, Meus Certificados, Atualizar meus dados",
         "29, 34, 36, 37, 38"),
        ("Estrutura · ÁREA DO GESTOR", "Gerenciamento de cursos, inscrições e emissão de certificados",
         "39 a 52"),
        ("Estrutura · ÁREA DO PROFESSOR", "Upload de materiais e consulta da lista de alunos inscritos",
         "53, 54, 55"),
        ("Estrutura · CONTATO", "E-mail, endereço e telefone de contato", "15, rodapé de todas as telas"),
        ("Ator · Aluno", "Realiza inscrições, acessa materiais e certificados", "24, 30 a 38"),
        ("Ator · Gestor da Escola", "Cria cursos, gerencia inscrições, lança presença, emite "
         "certificados, insere notícias e materiais, mantém o portal", "39 a 52"),
        ("Ator · Professor", "Vê sua lista de alunos e envia materiais dos cursos vinculados",
         "53, 54, 55"),
        ("RF 1", "Vitrine de cursos e eventos: cards com capa, título, data, carga horária, etiqueta de "
         "status e de formato, botão de detalhes; aba de concluídos; filtros por mês, tema e público",
         "01, 02, 03, 04"),
        ("RF 2", "Página de detalhe do curso: Ementa, Sobre o Professor, Cronograma e botão Inscrever-se",
         "05, 06, 07"),
        ("RF 3", "Aba de notícias com notícias em destaque cadastradas pelo gestor", "01, 08, 09, 49"),
        ("RF 4", "Validação de certificado: código único, QR Code, reCAPTCHA, Cenário A e Cenário B",
         "17, 18, 19, 20, 21, 37, 47"),
        ("RF 5", "Login: identificador, senha oculta, manter sessão, erro genérico, bloqueio, "
         "recuperação de senha com token temporário", "22, 23, 26, 27, 28"),
        ("RF 6", "Cadastro do aluno: nome, CPF, e-mail, telefone, tipo de vínculo, matrícula "
         "condicional e senha com hash", "24, 25, 38"),
        ("RF 7", "Inscrição no curso: verificação de login, escolha de turma, checagem de vagas, "
         "checagem de inscrição existente e gravação com status Confirmada", "30, 31, 32"),
        ("RF 8", "Lista de espera automática, com ordem de chegada", "31, 33, 45"),
        ("RF 9", "Cancelar inscrição pelo aluno, com confirmação e aviso de liberação da vaga", "34, 35"),
        ("RF 10", "Gestão da fila de espera pelo gestor, com convocação e prazo", "45"),
        ("RF 11", "Cancelar inscrição pelo gestor, com confirmação, aviso e registro em log", "43, 44"),
        ("RF 12", "Gestão de cursos", "40, 41"),
        ("RF 13", "Gestão de turmas e inscrições", "42, 43"),
        ("RF 14", "Controle de frequência", "46, 36"),
        ("RF 15", "Emissão de certificados", "47, 37"),
        ("RF 16", "Gestão de professores", "48, 06"),
        ("RF 17", "Gestão de conteúdo do portal", "49, 50, 51"),
        ("Necessidade do usuário", "Divulgar a agenda de cursos e eventos", "01, 02, 03, 04"),
        ("Necessidade do usuário", "Permitir o recebimento de inscrições", "30, 31, 32, 33, 43"),
        ("Necessidade do usuário", "Links para escolas do legislativo parceiras", "01, 13, 51"),
        ("Necessidade do usuário", "Feed de notícias", "01, 08, 09, 49"),
        ("Necessidade do usuário", "Composição da Escola", "10"),
        ("Necessidade do usuário", "Lista de instrumentos jurídicos formalizados", "12, 51"),
        ("Automação de processos", "Substituir controles manuais de inscrição, vagas e listas de "
         "presença", "42, 43, 45, 46, 52"),
    ]
    A("| Requisito / item do documento | O que foi previsto | Telas |")
    A("|---|---|---|")
    for a, bq, c in itens:
        A("| **%s** | %s | %s |" % (a, bq, c))
    A("")
    A("## Decisões pendentes por tela")
    A("")
    A("| # | Requisito | Decisão | Telas |")
    A("|---|---|---|---|")
    for num, rf, perg, _a, _b, telas in DECISOES:
        A("| %s | %s | %s | %s |" % (num, rf, perg, telas))
    A("")
    return "\n".join(L) + "\n"


def build_decisoes():
    L = []
    A = L.append
    A("# Decisões em reunião — Portal da Escola do Legislativo")
    A("")
    A("Pontos marcados como `[DECISÃO EM REUNIÃO]` no documento preliminar de especificação de "
      "requisitos, mais um item complementar levantado durante a prototipação (D14).")
    A("")
    A("Cada decisão indica em quais telas do protótipo a escolha aparece, para conferência durante "
      "a reunião.")
    A("")
    for num, rf, perg, oa, ob, telas in DECISOES:
        A("## %s · %s — %s" % (num, rf, perg))
        A("")
        A("- **Opção A:** %s" % oa)
        A("- **Opção B:** %s" % ob)
        A("- **Telas:** %s" % telas)
        A("- **Decisão tomada:** ______________________________")
        A("")
    return "\n".join(L) + "\n"


def build_preview(dims):
    cards = []
    mod_nome = {m[0]: m[1] for m in MODULOS}
    cor = {"publico": "#1263A5", "auth": "#B8862B", "aluno": "#1B7A57",
           "gestor": "#5A4A96", "prof": "#1D6F73", "apoio": "#64778A"}
    atual = None
    for num, arq, titulo, mod, rf in INV:
        if mod != atual:
            atual = mod
            cards.append('</div><h2 style="border-color:%s">%s</h2><div class="grid">'
                         % (cor[mod], mod_nome[mod]))
        d = dims.get(arq, (0, 0, 0))
        cards.append(
            '<figure><a href="figma-telas/%s.svg" target="_blank">'
            '<img src="figma-telas/%s.svg" alt="%s" loading="lazy"></a>'
            '<figcaption><b style="color:%s">%s</b> %s<span>%s · %d × %d</span></figcaption></figure>'
            % (arq, arq, titulo, cor[mod], num, titulo, rf, d[0], d[1]))
    html = """<!doctype html>
<html lang="pt-BR"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Protótipo · Portal da Escola do Legislativo</title>
<style>
*{box-sizing:border-box}
body{margin:0;background:#F3F6FA;color:#14232F;
     font:15px/1.5 -apple-system,Segoe UI,Roboto,Arial,sans-serif}
header{background:#0E2C4B;color:#fff;padding:34px 48px;border-bottom:4px solid #B8862B}
header h1{margin:0 0 6px;font-size:26px}
header p{margin:0;color:#B7C7D6;font-size:14px}
main{padding:32px 48px 80px;max-width:1800px;margin:0 auto}
h2{font-size:17px;margin:44px 0 18px;padding-left:12px;border-left:5px solid #1263A5}
.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(330px,1fr));gap:22px}
figure{margin:0;background:#fff;border:1px solid #DBE3EC;border-radius:10px;overflow:hidden}
figure img{width:100%;display:block;background:#fff;border-bottom:1px solid #EDF1F6;
           max-height:520px;object-fit:cover;object-position:top}
figcaption{padding:12px 14px;font-size:13px;line-height:1.45}
figcaption b{margin-right:6px}
figcaption span{display:block;color:#64778A;font-size:11.5px;margin-top:3px}
a{text-decoration:none;color:inherit}
</style></head><body>
<header><h1>Portal da Escola do Legislativo — protótipo de telas</h1>
<p>Câmara Municipal do Recife · Divisão de Informática · processo nº 3096/2025 ·
__N__ frames · clique em qualquer tela para abrir em tamanho real</p></header>
<main><div class="grid">__CARDS__</div></main></body></html>
""".replace("__N__", str(len(INV))).replace(
        "__CARDS__", "".join(cards)[len("</div>"):] + "</div>")
    return html


def main():
    dims, hots = build_svgs()
    faltando = [t[1] for t in INV if t[1] not in dims]
    sobrando = [k for k in dims if k not in [t[1] for t in INV]]
    w(os.path.join(RAIZ, "guia-navegacao-figma.md"),
      build_guia(dims, sum(len(v) for v in hots.values())))
    w(os.path.join(RAIZ, "matriz-requisitos-telas.md"), build_matriz())
    w(os.path.join(RAIZ, "decisoes-em-reuniao.md"), build_decisoes())
    w(os.path.join(RAIZ, "preview.html"), build_preview(dims))
    w(os.path.join(RAIZ, "prototipo.html"), proto_html.build(dims, hots))
    print("SVGs gerados: %d" % len(dims))
    if faltando:
        print("!! no inventario mas nao gerados:", faltando)
    if sobrando:
        print("!! gerados mas fora do inventario:", sobrando)
    print("areas clicaveis: %d" % sum(len(v) for v in hots.values()))
    print("documentos: prototipo.html, preview.html, guia-navegacao-figma.md, "
          "matriz-requisitos-telas.md, decisoes-em-reuniao.md")


if __name__ == "__main__":
    main()
