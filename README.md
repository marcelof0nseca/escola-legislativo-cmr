# Portal da Escola do Legislativo — protótipo de telas

Protótipo funcional das telas do **Portal da Escola do Legislativo da Câmara Municipal do Recife**,
elaborado pela Divisão de Informática a partir do documento preliminar de especificação de
requisitos (processo nº 3096/2025).

São **57 telas** cobrindo os 17 requisitos funcionais, a estrutura de conteúdo do portal, os três
atores do sistema (Aluno, Gestor da Escola e Professor) e as 14 decisões que dependem de reunião.

---

## Como ver o protótipo

### 1. Navegando pelo navegador (recomendado para apresentar)

Abra **`prototipo.html`**. Não precisa de servidor nem de instalação — funciona com duplo clique,
ou com o *Live Server* do VS Code.

| Recurso | Como usar |
|---|---|
| Navegar | Clique nos botões, menus, abas e cards da própria tela |
| Ver o que é clicável | Botão **Áreas clicáveis** no topo, ou tecla `H` |
| Descobrir os cliques | Clique numa área vazia: os pontos de clique piscam |
| Pular para uma tela | Lista suspensa no topo, agrupada por módulo |
| Tela anterior / próxima | Setas do topo ou `←` `→` do teclado |
| Link direto | `prototipo.html#30` abre a tela 30 |

São **1.112 áreas clicáveis** ligando as 57 telas.

### 2. Em galeria

Abra **`preview.html`** para ver todas as telas lado a lado, agrupadas por módulo.

### 3. No Figma

Arraste **todos** os arquivos de `figma-telas/` para dentro de um arquivo do Figma. Cada `.svg`
vira um **Frame** com o nome correto, pronto para receber as ligações no modo *Prototype*.
O passo a passo e a tabela com as 129 ligações estão em
[`guia-navegacao-figma.md`](guia-navegacao-figma.md).

---

## Estrutura do repositório

```
figma-telas/                 57 SVGs — um por tela, prontos para o Figma
gerador/                     código que gera as telas (Python, sem dependências)
prototipo.html               protótipo clicável e navegável
preview.html                 galeria com todas as telas
guia-navegacao-figma.md      importação no Figma + 129 ligações + roteiro de apresentação
matriz-requisitos-telas.md   rastreabilidade requisito × tela
decisoes-em-reuniao.md       as 14 decisões pendentes, com opções A/B
_backup-v1/                  primeira versão dos wireframes (histórico)
```

## As 57 telas

| Módulo | Telas | Cobre |
|---|---|---|
| Público | 01–21 | RF 1 a RF 4, HOME, A ESCOLA, ACERVO, CONTATO, busca rápida |
| Autenticação | 22–28 | RF 5 e RF 6 |
| Área do Aluno | 29–38 | RF 7, RF 8, RF 9 e a estrutura da Área do Aluno |
| Área do Gestor | 39–52 | RF 10 a RF 17 |
| Área do Professor | 53–55 | Alunos inscritos e upload de materiais |
| Apoio à reunião | 56–57 | Mapa de navegação e painel de decisões |

Cada tela traz, no rodapé, uma faixa `NOTA-ANALISE` com os requisitos atendidos e as decisões
pendentes daquela tela. É um grupo nomeado: no Figma, dá para selecioná-lo na lista de camadas e
apagar em um clique, caso queira mostrar só a interface.

---

## Regerar as telas

As telas **não** são editadas à mão: são geradas por script. Para alterar qualquer uma, edite o
código em `gerador/` e rode:

```bash
python gerador/build.py
```

O comando reescreve os 57 SVGs, o `prototipo.html`, o `preview.html` e os três documentos em
Markdown. Requer apenas Python 3 — sem bibliotecas externas.

| Arquivo | Papel |
|---|---|
| `ds.py` | Paleta, tipografia, primitivas de SVG e ícones |
| `comp.py` | Componentes (botões, campos, tabelas, cabeçalho, rodapé, menu lateral) |
| `blocks.py` | Blocos compostos (card de curso, card de notícia, certificado, QR) |
| `t_pub1.py` `t_pub2.py` `t_auth.py` `t_aluno.py` `t_gestor.py` `t_prof.py` `t_apoio.py` | As telas |
| `dados.py` | Inventário das telas, ligações de navegação e decisões pendentes |
| `build.py` | Monta tudo e escreve os arquivos finais |
| `proto_html.py` | Gera o protótipo clicável |

As áreas clicáveis do `prototipo.html` são registradas automaticamente durante a geração
(parâmetro `to=` nos botões e links), então nunca saem do lugar quando o layout muda.

---

Câmara Municipal do Recife · Divisão de Informática
Rua Princesa Isabel, 410 — 1º andar — Boa Vista — Recife/PE
