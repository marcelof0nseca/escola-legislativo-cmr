# Guia de navegação no Figma — Portal da Escola do Legislativo

Câmara Municipal do Recife · Divisão de Informática · processo nº 3096/2025

São **57 frames** na pasta `figma-telas/`, cobrindo todos os requisitos do documento preliminar de especificação.

## 0. Ver o protótipo navegando (sem Figma)

Abra **`prototipo.html`** no navegador (duplo clique, ou botão direito → *Open with Live Server* no VS Code). Ele já vem navegável: os botões, menus, abas e cards são clicáveis e levam para a tela de destino, com **1112 áreas clicáveis** distribuídas nas 57 telas.

| Recurso | Como usar |
|---|---|
| Navegar | Clique nos botões, menus, abas e cards da própria tela |
| Ver o que é clicável | Botão **Áreas clicáveis** no topo, ou tecla `H` |
| Descobrir os cliques | Clique em qualquer área vazia: os pontos de clique piscam |
| Pular para uma tela | Lista suspensa no topo, agrupada por módulo |
| Tela anterior / próxima | Setas do topo ou `←` `→` do teclado |
| Link direto para uma tela | `prototipo.html#30` abre a tela 30 |

`preview.html` é diferente: mostra as 57 telas lado a lado, em galeria, para conferência rápida.

> Os arquivos `.svg` sozinhos **não** são navegáveis — são imagens. Quem dá a navegação é o `prototipo.html` (no navegador) ou o modo Prototype do Figma (item 3 abaixo).

## 1. Como importar no Figma

1. Crie um arquivo novo no Figma (`Design file`).
2. Selecione **todos** os arquivos `.svg` da pasta `figma-telas/` e arraste para dentro do canvas.
3. Cada arquivo vira **um Frame** já com o nome correto (`01-home`, `02-cursos-vitrine`, ...).
   Se algum vier como Group, selecione e use `Selection to frame` (Shift+A) mantendo o nome.
4. Organize os frames em colunas por módulo — a ordem numérica já segue o fluxo.
5. Aba **Prototype** → selecione o botão/área clicável → arraste a setinha até o frame de destino
   → `On click` · `Navigate to` · `Instant` (ou `Smart Animate`).

> Dica: para telas com modal (35 e 44), use `Open overlay` em vez de `Navigate to` se quiser o efeito de sobreposição.

### Grupos que podem ser apagados

Cada frame tem, no rodapé, um grupo chamado `NOTA-ANALISE` (faixa escura com os requisitos atendidos e as decisões pendentes). Ele existe para a apresentação e para a reunião de requisitos. Se quiser mostrar só a interface, selecione o grupo na camada e apague — em um clique por frame. A tela `22-login` também tem o grupo `ATALHOS-PROTOTIPO`, com os botões de simulação de perfil.

## 2. Inventário de frames

| # | Frame | Tela | Módulo | Requisitos | Dimensões |
|---|---|---|---|---|---|
| 01 | `01-home` | Home do portal | MÓDULO PÚBLICO | RF 1, RF 3, RF 4 | 1440 × 3359 |
| 02 | `02-cursos-vitrine` | Vitrine de cursos e eventos | MÓDULO PÚBLICO | RF 1 | 1440 × 2164 |
| 03 | `03-cursos-filtros-aplicados` | Vitrine com filtros aplicados | MÓDULO PÚBLICO | RF 1 | 1440 × 1714 |
| 04 | `04-cursos-realizados` | Cursos e eventos realizados | MÓDULO PÚBLICO | RF 1 | 1440 × 1664 |
| 05 | `05-curso-detalhe-ementa` | Detalhe do curso - Ementa | MÓDULO PÚBLICO | RF 2 | 1440 × 2007 |
| 06 | `06-curso-detalhe-professor` | Detalhe do curso - Professor | MÓDULO PÚBLICO | RF 2, RF 16 | 1440 × 1818 |
| 07 | `07-curso-detalhe-cronograma-turmas` | Detalhe - Cronograma e turmas | MÓDULO PÚBLICO | RF 2, RF 13 | 1440 × 1987 |
| 08 | `08-noticias-lista` | Notícias | MÓDULO PÚBLICO | RF 3 | 1440 × 2102 |
| 09 | `09-noticia-detalhe` | Notícia aberta | MÓDULO PÚBLICO | RF 3 | 1440 × 1934 |
| 10 | `10-escola-quem-somos` | A Escola - Quem Somos | MÓDULO PÚBLICO | Estrutura | 1440 × 1908 |
| 11 | `11-escola-historia` | A Escola - História | MÓDULO PÚBLICO | Estrutura | 1440 × 1956 |
| 12 | `12-escola-legislacao-transparencia` | Legislação e Transparência | MÓDULO PÚBLICO | Estrutura | 1440 × 1910 |
| 13 | `13-escolas-parceiras` | Escolas parceiras | MÓDULO PÚBLICO | Estrutura | 1440 × 1630 |
| 14 | `14-acervo-biblioteca` | Acervo / Biblioteca | MÓDULO PÚBLICO | Estrutura | 1440 × 1948 |
| 15 | `15-contato` | Contato | MÓDULO PÚBLICO | Estrutura | 1440 × 1694 |
| 16 | `16-busca-resultados` | Resultados da busca | MÓDULO PÚBLICO | Busca rápida | 1440 × 1758 |
| 17 | `17-validar-certificado` | Validar certificado | MÓDULO PÚBLICO | RF 4 | 1440 × 1652 |
| 18 | `18-certificado-valido` | Certificado válido (Cenário B) | MÓDULO PÚBLICO | RF 4 | 1440 × 1708 |
| 19 | `19-certificado-invalido` | Certificado inválido (Cenário A) | MÓDULO PÚBLICO | RF 4 | 1440 × 1434 |
| 20 | `20-certificado-pdf-opcao1-codigo` | PDF do certificado - Opção 1 | MÓDULO PÚBLICO | RF 4 | 1440 × 1543 |
| 21 | `21-certificado-pdf-opcao2-qrcode` | PDF do certificado - Opção 2 | MÓDULO PÚBLICO | RF 4 | 1440 × 1589 |
| 22 | `22-login` | Login | AUTENTICAÇÃO | RF 5 | 1440 × 1436 |
| 23 | `23-login-erro-e-bloqueio` | Login com erro e bloqueio | AUTENTICAÇÃO | RF 5 | 1440 × 1223 |
| 24 | `24-cadastro-aluno` | Cadastro do aluno | AUTENTICAÇÃO | RF 6 | 1440 × 2085 |
| 25 | `25-cadastro-confirmacao` | Cadastro concluído | AUTENTICAÇÃO | RF 5, RF 6 | 1440 × 1430 |
| 26 | `26-senha-esqueci` | Esqueci minha senha | AUTENTICAÇÃO | RF 5 | 1440 × 942 |
| 27 | `27-senha-link-enviado` | Link de recuperação enviado | AUTENTICAÇÃO | RF 5 | 1440 × 942 |
| 28 | `28-senha-nova` | Criar nova senha | AUTENTICAÇÃO | RF 5 | 1440 × 1042 |
| 29 | `29-aluno-painel` | Painel do aluno | ÁREA DO ALUNO | Estrutura | 1440 × 1872 |
| 30 | `30-aluno-inscricao-selecionar-turma` | Inscrição - escolher turma | ÁREA DO ALUNO | RF 7 | 1440 × 1835 |
| 31 | `31-aluno-inscricao-sem-vaga-outra-turma` | Inscrição - turma esgotada | ÁREA DO ALUNO | RF 7, RF 8 | 1440 × 1604 |
| 32 | `32-aluno-inscricao-confirmada` | Inscrição confirmada | ÁREA DO ALUNO | RF 7 | 1440 × 1526 |
| 33 | `33-aluno-lista-espera-confirmada` | Entrou na lista de espera | ÁREA DO ALUNO | RF 8 | 1440 × 1588 |
| 34 | `34-aluno-meus-cursos` | Meus cursos | ÁREA DO ALUNO | RF 7, RF 8, RF 9 | 1440 × 1752 |
| 35 | `35-aluno-cancelar-inscricao` | Cancelar inscrição (aluno) | ÁREA DO ALUNO | RF 9 | 1440 × 1752 |
| 36 | `36-aluno-sala-do-curso-materiais` | Sala do curso e materiais | ÁREA DO ALUNO | RF 2, RF 14 | 1440 × 2021 |
| 37 | `37-aluno-meus-certificados` | Meus certificados | ÁREA DO ALUNO | RF 4, RF 15 | 1440 × 1860 |
| 38 | `38-aluno-atualizar-dados` | Atualizar meus dados | ÁREA DO ALUNO | RF 6 | 1440 × 1626 |
| 39 | `39-gestor-painel` | Painel do gestor | ÁREA DO GESTOR | RF 10-17 | 1440 × 1326 |
| 40 | `40-gestor-cursos-lista` | Gestão de cursos | ÁREA DO GESTOR | RF 12 | 1440 × 1186 |
| 41 | `41-gestor-curso-cadastro` | Cadastro de curso | ÁREA DO GESTOR | RF 12 | 1440 × 1206 |
| 42 | `42-gestor-turmas` | Gestão de turmas | ÁREA DO GESTOR | RF 13 | 1440 × 1380 |
| 43 | `43-gestor-inscricoes` | Gestão de inscrições | ÁREA DO GESTOR | RF 11, RF 13 | 1440 × 1186 |
| 44 | `44-gestor-cancelar-inscricao-log` | Cancelar inscrição + log | ÁREA DO GESTOR | RF 11 | 1440 × 1186 |
| 45 | `45-gestor-fila-espera` | Gestão da fila de espera | ÁREA DO GESTOR | RF 8, RF 10 | 1440 × 1286 |
| 46 | `46-gestor-frequencia` | Controle de frequência | ÁREA DO GESTOR | RF 14 | 1440 × 1277 |
| 47 | `47-gestor-certificados-emissao` | Emissão de certificados | ÁREA DO GESTOR | RF 4, RF 15 | 1440 × 1381 |
| 48 | `48-gestor-professores` | Gestão de professores | ÁREA DO GESTOR | RF 16 | 1440 × 1482 |
| 49 | `49-gestor-conteudo-noticias` | Conteúdo - Notícias | ÁREA DO GESTOR | RF 3, RF 17 | 1440 × 1580 |
| 50 | `50-gestor-conteudo-acervo` | Conteúdo - Acervo | ÁREA DO GESTOR | RF 17 | 1440 × 1362 |
| 51 | `51-gestor-conteudo-parceiras-e-paginas` | Conteúdo - Parceiras e páginas | ÁREA DO GESTOR | RF 17 | 1440 × 1490 |
| 52 | `52-gestor-relatorios` | Relatórios e indicadores | ÁREA DO GESTOR | RF 12-15 | 1440 × 1330 |
| 53 | `53-professor-painel` | Painel do professor | ÁREA DO PROFESSOR | Estrutura | 1440 × 1242 |
| 54 | `54-professor-alunos-inscritos` | Alunos inscritos | ÁREA DO PROFESSOR | Estrutura | 1440 × 1312 |
| 55 | `55-professor-materiais-upload` | Materiais do curso | ÁREA DO PROFESSOR | Estrutura | 1440 × 1266 |
| 56 | `56-mapa-de-navegacao` | Mapa de navegação | APOIO À REUNIÃO | - | 2000 × 1830 |
| 57 | `57-decisoes-em-reuniao` | Decisões em reunião | APOIO À REUNIÃO | - | 1440 × 2688 |

## 3. Ligações do protótipo (129)

Monte estas ligações no modo Prototype. A coluna **Elemento** indica o que deve receber o link.


### De `01-home` — Home do portal

| Elemento clicável | Frame de destino | Observação |
|---|---|---|
| Menu 'Cursos e Eventos' / botão 'Ver agenda completa' | `02-cursos-vitrine` | Entrada da agenda |
| Botão 'Ver detalhes' de um card de curso | `05-curso-detalhe-ementa` | Abre a página do curso |
| Aba 'Cursos e eventos realizados' | `04-cursos-realizados` | Aba de concluídos do RF 1 |
| Acesso rápido 'Validar certificado' | `17-validar-certificado` | Ícone de acesso rápido |
| Acesso rápido 'Área do Aluno' | `22-login` | Exige login |
| Acesso rápido 'Agenda de cursos' | `02-cursos-vitrine` | — |
| Acesso rápido 'Acervo / Biblioteca' | `14-acervo-biblioteca` | — |
| Botão 'Buscar' da barra de busca rápida | `16-busca-resultados` | Busca por texto simples |
| Link 'Ver todas as notícias' | `08-noticias-lista` | — |
| Card de notícia 'Ler notícia completa' | `09-noticia-detalhe` | — |
| Link 'Ver todas as parcerias' / card de escola parceira | `13-escolas-parceiras` | — |
| Link 'Ver todos os instrumentos' | `12-escola-legislacao-transparencia` | — |
| Link 'Ir para o acervo' | `14-acervo-biblioteca` | — |
| Menu 'A Escola' | `10-escola-quem-somos` | — |
| Menu 'Notícias' | `08-noticias-lista` | — |
| Menu 'Contato' | `15-contato` | — |
| Botão 'Entrar / Cadastre-se' do cabeçalho | `22-login` | Vale para todas as páginas públicas |

### De `02-cursos-vitrine` — Vitrine de cursos e eventos

| Elemento clicável | Frame de destino | Observação |
|---|---|---|
| Botão 'Aplicar' da barra de filtros | `03-cursos-filtros-aplicados` | Mostra o resultado filtrado |
| Aba 'Cursos e eventos realizados' | `04-cursos-realizados` | — |
| Botão 'Ver detalhes' de um card | `05-curso-detalhe-ementa` | — |
| Logo / menu 'Home' | `01-home` | — |

### De `03-cursos-filtros-aplicados` — Vitrine com filtros aplicados

| Elemento clicável | Frame de destino | Observação |
|---|---|---|
| Link 'Limpar filtros' | `02-cursos-vitrine` | — |
| Botão 'Ver detalhes' de um card | `05-curso-detalhe-ementa` | — |

### De `04-cursos-realizados` — Cursos e eventos realizados

| Elemento clicável | Frame de destino | Observação |
|---|---|---|
| Aba 'Com inscrições abertas' | `02-cursos-vitrine` | — |
| Botão 'Ver informações' de um card | `05-curso-detalhe-ementa` | — |

### De `05-curso-detalhe-ementa` — Detalhe do curso - Ementa

| Elemento clicável | Frame de destino | Observação |
|---|---|---|
| Aba 'Sobre o professor' | `06-curso-detalhe-professor` | — |
| Aba 'Cronograma e turmas' | `07-curso-detalhe-cronograma-turmas` | — |
| Botão 'Inscrever-se neste curso' (usuário deslogado) | `22-login` | RF 7: redireciona ao login |
| Botão 'Inscrever-se neste curso' (usuário logado) | `30-aluno-inscricao-selecionar-turma` | RF 7: vai escolher a turma |
| Link 'Ir para a validação de certificados' | `17-validar-certificado` | — |

### De `06-curso-detalhe-professor` — Detalhe do curso - Professor

| Elemento clicável | Frame de destino | Observação |
|---|---|---|
| Aba 'O que você vai aprender' | `05-curso-detalhe-ementa` | — |
| Aba 'Cronograma e turmas' | `07-curso-detalhe-cronograma-turmas` | — |

### De `07-curso-detalhe-cronograma-turmas` — Detalhe - Cronograma e turmas

| Elemento clicável | Frame de destino | Observação |
|---|---|---|
| Aba 'O que você vai aprender' | `05-curso-detalhe-ementa` | — |
| Aba 'Sobre o professor' | `06-curso-detalhe-professor` | — |
| Botão 'Inscrever-se neste curso' | `30-aluno-inscricao-selecionar-turma` | — |

### De `08-noticias-lista` — Notícias

| Elemento clicável | Frame de destino | Observação |
|---|---|---|
| Card de notícia / botão 'Ler notícia' | `09-noticia-detalhe` | — |

### De `09-noticia-detalhe` — Notícia aberta

| Elemento clicável | Frame de destino | Observação |
|---|---|---|
| Botão 'Voltar' | `08-noticias-lista` | — |

### De `10-escola-quem-somos` — A Escola - Quem Somos

| Elemento clicável | Frame de destino | Observação |
|---|---|---|
| Aba 'História' | `11-escola-historia` | — |
| Aba 'Legislação e Transparência' | `12-escola-legislacao-transparencia` | — |
| Aba 'Escolas parceiras' | `13-escolas-parceiras` | — |

### De `11-escola-historia` — A Escola - História

| Elemento clicável | Frame de destino | Observação |
|---|---|---|
| Aba 'Quem Somos' | `10-escola-quem-somos` | — |

### De `12-escola-legislacao-transparencia` — Legislação e Transparência

| Elemento clicável | Frame de destino | Observação |
|---|---|---|
| Aba 'Escolas parceiras' | `13-escolas-parceiras` | — |

### De `13-escolas-parceiras` — Escolas parceiras

| Elemento clicável | Frame de destino | Observação |
|---|---|---|
| Aba 'Quem Somos' | `10-escola-quem-somos` | — |

### De `16-busca-resultados` — Resultados da busca

| Elemento clicável | Frame de destino | Observação |
|---|---|---|
| Resultado do tipo curso | `05-curso-detalhe-ementa` | — |
| Resultado do tipo notícia | `09-noticia-detalhe` | — |
| Resultado do tipo acervo | `14-acervo-biblioteca` | — |

### De `17-validar-certificado` — Validar certificado

| Elemento clicável | Frame de destino | Observação |
|---|---|---|
| Botão 'Validar certificado' com código correto | `18-certificado-valido` | Cenário B do RF 4 |
| Botão 'Validar certificado' com código errado | `19-certificado-invalido` | Cenário A do RF 4 |

### De `18-certificado-valido` — Certificado válido (Cenário B)

| Elemento clicável | Frame de destino | Observação |
|---|---|---|
| Botão 'Validar outro código' | `17-validar-certificado` | — |

### De `19-certificado-invalido` — Certificado inválido (Cenário A)

| Elemento clicável | Frame de destino | Observação |
|---|---|---|
| Botão 'Validar novamente' | `18-certificado-valido` | — |

### De `22-login` — Login

| Elemento clicável | Frame de destino | Observação |
|---|---|---|
| Botão 'Entrar' (sucesso) | `29-aluno-painel` | RF 5 Cenário A |
| Botão 'Entrar' (credencial errada) | `23-login-erro-e-bloqueio` | RF 5 Cenário B |
| Atalho do protótipo 'Entrar como Aluno' | `29-aluno-painel` | — |
| Atalho do protótipo 'Entrar como Gestor' | `39-gestor-painel` | — |
| Atalho do protótipo 'Entrar como Professor' | `53-professor-painel` | — |
| Link 'Esqueci minha senha' | `26-senha-esqueci` | — |
| Link 'Cadastre-se' | `24-cadastro-aluno` | — |
| Link 'Voltar ao portal' | `01-home` | — |

### De `23-login-erro-e-bloqueio` — Login com erro e bloqueio

| Elemento clicável | Frame de destino | Observação |
|---|---|---|
| Botão 'Entrar' (agora correto) | `29-aluno-painel` | — |
| Link 'Esqueci minha senha' | `26-senha-esqueci` | — |

### De `24-cadastro-aluno` — Cadastro do aluno

| Elemento clicável | Frame de destino | Observação |
|---|---|---|
| Botão 'Criar meu cadastro' | `25-cadastro-confirmacao` | — |
| Botão 'Ir para o login' | `22-login` | — |

### De `25-cadastro-confirmacao` — Cadastro concluído

| Elemento clicável | Frame de destino | Observação |
|---|---|---|
| Botão 'Continuar a inscrição no curso' | `30-aluno-inscricao-selecionar-turma` | RF 5 Cenário A: volta para a inscrição |
| Botão 'Ir para Área do Aluno' | `29-aluno-painel` | — |
| Botão 'Início' | `01-home` | — |

### De `26-senha-esqueci` — Esqueci minha senha

| Elemento clicável | Frame de destino | Observação |
|---|---|---|
| Botão 'Enviar link de recuperação' | `27-senha-link-enviado` | — |

### De `27-senha-link-enviado` — Link de recuperação enviado

| Elemento clicável | Frame de destino | Observação |
|---|---|---|
| Botão 'Voltar para o login' | `22-login` | — |
| Link do e-mail (simular clique) | `28-senha-nova` | Token válido por 2 horas |

### De `28-senha-nova` — Criar nova senha

| Elemento clicável | Frame de destino | Observação |
|---|---|---|
| Botão 'Salvar nova senha' | `22-login` | — |

### De `29-aluno-painel` — Painel do aluno

| Elemento clicável | Frame de destino | Observação |
|---|---|---|
| Aba 'Meus cursos' | `34-aluno-meus-cursos` | — |
| Aba 'Meus certificados' | `37-aluno-meus-certificados` | — |
| Aba 'Meus dados' / botão 'Atualizar meus dados' | `38-aluno-atualizar-dados` | — |
| Link 'Acessar' de uma próxima atividade | `36-aluno-sala-do-curso-materiais` | — |
| Botão 'Ir para validação' | `17-validar-certificado` | — |
| Botão 'Sair da conta' | `01-home` | — |

### De `30-aluno-inscricao-selecionar-turma` — Inscrição - escolher turma

| Elemento clicável | Frame de destino | Observação |
|---|---|---|
| Botão 'Confirmar inscrição' (com vaga) | `32-aluno-inscricao-confirmada` | RF 7: grava status Confirmada |
| Seleção da turma esgotada | `31-aluno-inscricao-sem-vaga-outra-turma` | RF 7: sem vaga na turma |
| Botão 'Cancelar e voltar ao curso' | `05-curso-detalhe-ementa` | — |

### De `31-aluno-inscricao-sem-vaga-outra-turma` — Inscrição - turma esgotada

| Elemento clicável | Frame de destino | Observação |
|---|---|---|
| Botão 'Escolher' de uma turma com vaga | `30-aluno-inscricao-selecionar-turma` | — |
| Botão 'Entrar na lista de espera' | `33-aluno-lista-espera-confirmada` | RF 8 |

### De `32-aluno-inscricao-confirmada` — Inscrição confirmada

| Elemento clicável | Frame de destino | Observação |
|---|---|---|
| Botão 'Ir para Meus Cursos' | `34-aluno-meus-cursos` | — |
| Botão 'Ver outros cursos' | `02-cursos-vitrine` | — |

### De `33-aluno-lista-espera-confirmada` — Entrou na lista de espera

| Elemento clicável | Frame de destino | Observação |
|---|---|---|
| Botão 'Ir para Meus Cursos' | `34-aluno-meus-cursos` | — |
| Botão 'Ver outras turmas' | `07-curso-detalhe-cronograma-turmas` | — |

### De `34-aluno-meus-cursos` — Meus cursos

| Elemento clicável | Frame de destino | Observação |
|---|---|---|
| Botão 'Cancelar' de uma inscrição | `35-aluno-cancelar-inscricao` | RF 9: abre a confirmação |
| Botão 'Acessar curso' | `36-aluno-sala-do-curso-materiais` | — |
| Botão 'Certificado' | `37-aluno-meus-certificados` | — |

### De `35-aluno-cancelar-inscricao` — Cancelar inscrição (aluno)

| Elemento clicável | Frame de destino | Observação |
|---|---|---|
| Botão 'Sim, cancelar inscrição' | `34-aluno-meus-cursos` | Volta com a inscrição cancelada |
| Botão 'Manter' | `34-aluno-meus-cursos` | — |

### De `36-aluno-sala-do-curso-materiais` — Sala do curso e materiais

| Elemento clicável | Frame de destino | Observação |
|---|---|---|
| Botão 'Cancelar minha inscrição' | `35-aluno-cancelar-inscricao` | — |

### De `37-aluno-meus-certificados` — Meus certificados

| Elemento clicável | Frame de destino | Observação |
|---|---|---|
| Botão 'Validar' | `17-validar-certificado` | — |
| Botão 'Baixar PDF' | `21-certificado-pdf-opcao2-qrcode` | Abre o modelo do certificado |

### De `38-aluno-atualizar-dados` — Atualizar meus dados

| Elemento clicável | Frame de destino | Observação |
|---|---|---|
| Botão 'Salvar alterações' | `29-aluno-painel` | — |

### De `39-gestor-painel` — Painel do gestor

| Elemento clicável | Frame de destino | Observação |
|---|---|---|
| Menu lateral 'Cursos' | `40-gestor-cursos-lista` | — |
| Menu lateral 'Turmas' | `42-gestor-turmas` | — |
| Menu lateral 'Inscrições' | `43-gestor-inscricoes` | — |
| Menu lateral 'Fila de espera' | `45-gestor-fila-espera` | — |
| Menu lateral 'Frequência' | `46-gestor-frequencia` | — |
| Menu lateral 'Certificados' | `47-gestor-certificados-emissao` | — |
| Menu lateral 'Professores' | `48-gestor-professores` | — |
| Menu lateral 'Conteúdo do portal' | `49-gestor-conteudo-noticias` | — |
| Menu lateral 'Relatórios' | `52-gestor-relatorios` | — |
| Botão 'Novo curso' | `41-gestor-curso-cadastro` | — |
| Pendência 'Lançar frequência' | `46-gestor-frequencia` | — |
| Pendência 'Emitir 30 certificados' | `47-gestor-certificados-emissao` | — |
| Pendência 'Chamar 3 alunos da fila' | `45-gestor-fila-espera` | — |

### De `40-gestor-cursos-lista` — Gestão de cursos

| Elemento clicável | Frame de destino | Observação |
|---|---|---|
| Botão 'Novo curso' / ícone de editar | `41-gestor-curso-cadastro` | — |
| Ícone de inscritos (bonequinhos) | `43-gestor-inscricoes` | — |
| Ícone de visualizar (olho) | `05-curso-detalhe-ementa` | Mostra como o público vê |

### De `41-gestor-curso-cadastro` — Cadastro de curso

| Elemento clicável | Frame de destino | Observação |
|---|---|---|
| Botão 'Salvar e continuar' | `42-gestor-turmas` | Passo 2: turmas e vagas |

### De `42-gestor-turmas` — Gestão de turmas

| Elemento clicável | Frame de destino | Observação |
|---|---|---|
| Ícone de inscritos de uma turma | `43-gestor-inscricoes` | — |

### De `43-gestor-inscricoes` — Gestão de inscrições

| Elemento clicável | Frame de destino | Observação |
|---|---|---|
| Botão 'Cancelar' de uma inscrição | `44-gestor-cancelar-inscricao-log` | RF 11 |
| Botão 'Chamar' de quem está na fila | `45-gestor-fila-espera` | — |

### De `44-gestor-cancelar-inscricao-log` — Cancelar inscrição + log

| Elemento clicável | Frame de destino | Observação |
|---|---|---|
| Botão 'Confirmar cancelamento' / 'Voltar' | `43-gestor-inscricoes` | — |

### De `45-gestor-fila-espera` — Gestão da fila de espera

| Elemento clicável | Frame de destino | Observação |
|---|---|---|
| Botão 'Chamar agora' | `43-gestor-inscricoes` | — |

### De `46-gestor-frequencia` — Controle de frequência

| Elemento clicável | Frame de destino | Observação |
|---|---|---|
| Botão 'Salvar frequência' | `47-gestor-certificados-emissao` | Libera a emissão |

### De `47-gestor-certificados-emissao` — Emissão de certificados

| Elemento clicável | Frame de destino | Observação |
|---|---|---|
| Botão 'Editar modelo do certificado' | `21-certificado-pdf-opcao2-qrcode` | — |

### De `49-gestor-conteudo-noticias` — Conteúdo - Notícias

| Elemento clicável | Frame de destino | Observação |
|---|---|---|
| Aba 'Acervo / Biblioteca' | `50-gestor-conteudo-acervo` | — |
| Aba 'Escolas parceiras e páginas' | `51-gestor-conteudo-parceiras-e-paginas` | — |

### De `50-gestor-conteudo-acervo` — Conteúdo - Acervo

| Elemento clicável | Frame de destino | Observação |
|---|---|---|
| Aba 'Notícias' | `49-gestor-conteudo-noticias` | — |

### De `51-gestor-conteudo-parceiras-e-paginas` — Conteúdo - Parceiras e páginas

| Elemento clicável | Frame de destino | Observação |
|---|---|---|
| Aba 'Notícias' | `49-gestor-conteudo-noticias` | — |

### De `53-professor-painel` — Painel do professor

| Elemento clicável | Frame de destino | Observação |
|---|---|---|
| Botão 'Ver alunos' de uma turma | `54-professor-alunos-inscritos` | — |
| Botão 'Materiais' de uma turma | `55-professor-materiais-upload` | — |
| Menu lateral 'Alunos inscritos' | `54-professor-alunos-inscritos` | — |
| Menu lateral 'Materiais' | `55-professor-materiais-upload` | — |

### De `54-professor-alunos-inscritos` — Alunos inscritos

| Elemento clicável | Frame de destino | Observação |
|---|---|---|
| Menu lateral 'Painel' | `53-professor-painel` | — |
| Menu lateral 'Materiais' | `55-professor-materiais-upload` | — |

### De `55-professor-materiais-upload` — Materiais do curso

| Elemento clicável | Frame de destino | Observação |
|---|---|---|
| Menu lateral 'Painel' | `53-professor-painel` | — |
| Menu lateral 'Alunos inscritos' | `54-professor-alunos-inscritos` | — |

## 4. Roteiro sugerido para a apresentação

| Momento | Frames | O que mostrar |
|---|---|---|
| Abertura | `56-mapa-de-navegacao` | Mostrar o mapa: 57 telas, 5 módulos, o que cada um cobre. |
| O portal público | `01-home` | Vitrine de cursos, notícias, busca rápida e acessos rápidos. |
| Agenda e filtros | `02-cursos-vitrine → 03 → 04` | Filtros por mês, tema e público; aba de realizados. |
| Página do curso | `05 → 06 → 07` | Ementa, professor, cronograma e turmas. |
| Inscrição | `05 → 22 → 24 → 25 → 30 → 32` | Fluxo completo do aluno novo até a confirmação. |
| Sem vaga | `30 → 31 → 33` | Turma esgotada, outra turma com vaga e fila de espera. |
| Área do aluno | `29 → 34 → 35 → 36 → 37` | Meus cursos, cancelamento, materiais e certificados. |
| Certificação | `37 → 21 → 17 → 18 / 19` | Certificado, código de autenticidade e validação pública. |
| Área do gestor | `39 → 40 → 41 → 42 → 43 → 44` | Cursos, turmas, inscrições e log de cancelamento. |
| Operação | `45 → 46 → 47` | Fila de espera, frequência e emissão de certificados. |
| Conteúdo | `48 → 49 → 50 → 51 → 52` | Professores, notícias, acervo, parceiras e relatórios. |
| Professor | `53 → 54 → 55` | Acesso restrito: alunos inscritos e upload de materiais. |
| Fechamento | `57-decisoes-em-reuniao` | As 14 decisões que precisam ser fechadas na reunião. |

## 5. Decisões pendentes

Estão detalhadas no frame `57-decisoes-em-reuniao` e resumidas em `decisoes-em-reuniao.md`.

