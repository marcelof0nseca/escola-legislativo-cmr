# Decisões em reunião — Portal da Escola do Legislativo

Pontos marcados como `[DECISÃO EM REUNIÃO]` no documento preliminar de especificação de requisitos, mais um item complementar levantado durante a prototipação (D14).

Cada decisão indica em quais telas do protótipo a escolha aparece, para conferência durante a reunião.

## D1 · RF 2 — Para eventos online ou híbridos, de que forma o link deve ser disponibilizado?

- **Opção A:** Opção 1 - Link exibido na própria página de detalhes do curso, visível a qualquer visitante.
- **Opção B:** Opção 2 - Link liberado somente após o aluno realizar a inscrição no portal.
- **Telas:** 05, 32, 36
- **Decisão tomada:** ______________________________

## D2 · RF 2 — Como deve acontecer um curso online?

- **Opção A:** Transmissão em plataforma externa (Meet, Teams, YouTube), com link publicado pelo portal.
- **Opção B:** Ambiente próprio dentro do portal, com sala virtual e registro de acesso.
- **Telas:** 05, 36
- **Decisão tomada:** ______________________________

## D3 · RF 3 — Como as notícias em destaque chegam à página inicial?

- **Opção A:** O gestor marca manualmente quais notícias ficam em destaque e em que ordem.
- **Opção B:** O portal exibe automaticamente as N notícias mais recentes por data de cadastro.
- **Telas:** 01, 49
- **Decisão tomada:** ______________________________

## D4 · RF 4 — Qual formato de validação será impresso no PDF do certificado?

- **Opção A:** Opção 1 - Apenas o código alfanumérico e o link do portal (digitação manual).
- **Opção B:** Opção 2 - Código alfanumérico + QR Code, com validação instantânea pela câmera.
- **Telas:** 20, 21, 47
- **Decisão tomada:** ______________________________

## D5 · RF 4 — Quais dados aparecem na tela de sucesso da validação (LGPD)?

- **Opção A:** Nome completo, CPF mascarado, curso, carga horária e data de conclusão.
- **Opção B:** Acrescentar a matrícula nos casos de servidores da Casa.
- **Telas:** 18
- **Decisão tomada:** ______________________________

## D6 · RF 5 — Qual será o identificador principal de acesso (login)?

- **Opção A:** Opção 1 (recomendada) - CPF. Garante unicidade e evita contas duplicadas.
- **Opção B:** Opção 2 - E-mail. Padrão de mercado, mas o usuário pode trocar e perder o histórico.
- **Telas:** 22, 23, 24, 26
- **Decisão tomada:** ______________________________

## D7 · RF 5 — Como será o login dos servidores da Câmara Municipal do Recife?

- **Opção A:** Integração com a rede interna via LDAP / Active Directory (Single Sign-On).
- **Opção B:** Banco de senhas isolado no portal: o servidor cria e gerencia uma senha nova.
- **Telas:** 22
- **Decisão tomada:** ______________________________

## D8 · RF 5 — Haverá política de bloqueio contra ataque de força bruta?

- **Opção A:** Sim - bloquear a conta por 30 minutos após 5 tentativas consecutivas malsucedidas.
- **Opção B:** Definir outro número de tentativas e outro tempo de bloqueio.
- **Telas:** 23
- **Decisão tomada:** ______________________________

## D9 · RF 6 — Qual será o modelo de acesso do aluno?

- **Opção A:** Opção 1 - Cadastro único com login e senha, com Área do Aluno, histórico e certificados.
- **Opção B:** Opção 2 - Formulário aberto a cada curso, sem histórico e sem área do aluno.
- **Telas:** 24, 29, 34, 37
- **Decisão tomada:** ______________________________

## D10 · RF 6 — Confirmar os dados coletados no cadastro do aluno (finalidade LGPD).

- **Opção A:** Nome, CPF, e-mail, telefone/WhatsApp, tipo de vínculo, matrícula (condicional) e senha.
- **Opção B:** Retirar ou acrescentar campos após análise de finalidade específica.
- **Telas:** 24, 38
- **Decisão tomada:** ______________________________

## D11 · RF 7 — O mesmo aluno pode se inscrever em mais de uma turma do mesmo curso?

- **Opção A:** Não - uma inscrição ativa por curso, liberando vaga para mais pessoas.
- **Opção B:** Sim - permitido, por exemplo para reposição de conteúdo.
- **Telas:** 30, 34
- **Decisão tomada:** ______________________________

## D12 · RF 10 — Quando surgir vaga, como a fila de espera é chamada?

- **Opção A:** Opção 1 - O sistema avisa o próximo por e-mail e dá 24h para assumir a vaga.
- **Opção B:** Opção 2 - Manual: alguém da Escola entra em contato com o próximo da fila.
- **Telas:** 33, 45
- **Decisão tomada:** ______________________________

## D13 · RF 13 — Um curso pode ter várias turmas? Como divulgar dias e horários?

- **Opção A:** Sim - cada turma com período, horário, local, professor e vagas próprios, exibidos na página do curso.
- **Opção B:** Não - um curso equivale a uma única turma.
- **Telas:** 07, 30, 42
- **Decisão tomada:** ______________________________

## D14 · RF 14 — Qual a frequência mínima para emissão do certificado?

- **Opção A:** 75% da carga horária (proposta do protótipo).
- **Opção B:** Outro percentual, com ou sem avaliação de aproveitamento.
- **Telas:** 46, 47
- **Decisão tomada:** ______________________________

