# Matriz de rastreabilidade — requisitos × telas

Portal da Escola do Legislativo · Câmara Municipal do Recife · processo nº 3096/2025

| Requisito / item do documento | O que foi previsto | Telas |
|---|---|---|
| **Estrutura · HOME** | Aba de cursos e eventos (carrossel), aba de notícias em destaque, barra de busca rápida, ícones de acesso rápido Validar Certificado e Área do Aluno | 01, 16 |
| **Estrutura · A ESCOLA** | Quem Somos, História, Legislação e Transparência (Parcerias/Convênios) | 10, 11, 12, 13 |
| **Estrutura · ACERVO/BIBLIOTECA** | Publicações, Manuais, Legislações | 14, 50 |
| **Estrutura · ÁREA DO ALUNO** | Meus Cursos, Meus Certificados, Atualizar meus dados | 29, 34, 36, 37, 38 |
| **Estrutura · ÁREA DO GESTOR** | Gerenciamento de cursos, inscrições e emissão de certificados | 39 a 52 |
| **Estrutura · ÁREA DO PROFESSOR** | Upload de materiais e consulta da lista de alunos inscritos | 53, 54, 55 |
| **Estrutura · CONTATO** | E-mail, endereço e telefone de contato | 15, rodapé de todas as telas |
| **Ator · Aluno** | Realiza inscrições, acessa materiais e certificados | 24, 30 a 38 |
| **Ator · Gestor da Escola** | Cria cursos, gerencia inscrições, lança presença, emite certificados, insere notícias e materiais, mantém o portal | 39 a 52 |
| **Ator · Professor** | Vê sua lista de alunos e envia materiais dos cursos vinculados | 53, 54, 55 |
| **RF 1** | Vitrine de cursos e eventos: cards com capa, título, data, carga horária, etiqueta de status e de formato, botão de detalhes; aba de concluídos; filtros por mês, tema e público | 01, 02, 03, 04 |
| **RF 2** | Página de detalhe do curso: Ementa, Sobre o Professor, Cronograma e botão Inscrever-se | 05, 06, 07 |
| **RF 3** | Aba de notícias com notícias em destaque cadastradas pelo gestor | 01, 08, 09, 49 |
| **RF 4** | Validação de certificado: código único, QR Code, reCAPTCHA, Cenário A e Cenário B | 17, 18, 19, 20, 21, 37, 47 |
| **RF 5** | Login: identificador, senha oculta, manter sessão, erro genérico, bloqueio, recuperação de senha com token temporário | 22, 23, 26, 27, 28 |
| **RF 6** | Cadastro do aluno: nome, CPF, e-mail, telefone, tipo de vínculo, matrícula condicional e senha com hash | 24, 25, 38 |
| **RF 7** | Inscrição no curso: verificação de login, escolha de turma, checagem de vagas, checagem de inscrição existente e gravação com status Confirmada | 30, 31, 32 |
| **RF 8** | Lista de espera automática, com ordem de chegada | 31, 33, 45 |
| **RF 9** | Cancelar inscrição pelo aluno, com confirmação e aviso de liberação da vaga | 34, 35 |
| **RF 10** | Gestão da fila de espera pelo gestor, com convocação e prazo | 45 |
| **RF 11** | Cancelar inscrição pelo gestor, com confirmação, aviso e registro em log | 43, 44 |
| **RF 12** | Gestão de cursos | 40, 41 |
| **RF 13** | Gestão de turmas e inscrições | 42, 43 |
| **RF 14** | Controle de frequência | 46, 36 |
| **RF 15** | Emissão de certificados | 47, 37 |
| **RF 16** | Gestão de professores | 48, 06 |
| **RF 17** | Gestão de conteúdo do portal | 49, 50, 51 |
| **Necessidade do usuário** | Divulgar a agenda de cursos e eventos | 01, 02, 03, 04 |
| **Necessidade do usuário** | Permitir o recebimento de inscrições | 30, 31, 32, 33, 43 |
| **Necessidade do usuário** | Links para escolas do legislativo parceiras | 01, 13, 51 |
| **Necessidade do usuário** | Feed de notícias | 01, 08, 09, 49 |
| **Necessidade do usuário** | Composição da Escola | 10 |
| **Necessidade do usuário** | Lista de instrumentos jurídicos formalizados | 12, 51 |
| **Automação de processos** | Substituir controles manuais de inscrição, vagas e listas de presença | 42, 43, 45, 46, 52 |

## Decisões pendentes por tela

| # | Requisito | Decisão | Telas |
|---|---|---|---|
| D1 | RF 2 | Para eventos online ou híbridos, de que forma o link deve ser disponibilizado? | 05, 32, 36 |
| D2 | RF 2 | Como deve acontecer um curso online? | 05, 36 |
| D3 | RF 3 | Como as notícias em destaque chegam à página inicial? | 01, 49 |
| D4 | RF 4 | Qual formato de validação será impresso no PDF do certificado? | 20, 21, 47 |
| D5 | RF 4 | Quais dados aparecem na tela de sucesso da validação (LGPD)? | 18 |
| D6 | RF 5 | Qual será o identificador principal de acesso (login)? | 22, 23, 24, 26 |
| D7 | RF 5 | Como será o login dos servidores da Câmara Municipal do Recife? | 22 |
| D8 | RF 5 | Haverá política de bloqueio contra ataque de força bruta? | 23 |
| D9 | RF 6 | Qual será o modelo de acesso do aluno? | 24, 29, 34, 37 |
| D10 | RF 6 | Confirmar os dados coletados no cadastro do aluno (finalidade LGPD). | 24, 38 |
| D11 | RF 7 | O mesmo aluno pode se inscrever em mais de uma turma do mesmo curso? | 30, 34 |
| D12 | RF 10 | Quando surgir vaga, como a fila de espera é chamada? | 33, 45 |
| D13 | RF 13 | Um curso pode ter várias turmas? Como divulgar dias e horários? | 07, 30, 42 |
| D14 | RF 14 | Qual a frequência mínima para emissão do certificado? | 46, 47 |

