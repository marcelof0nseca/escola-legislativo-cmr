# Guia de navegacao no Figma

Este projeto agora tem as telas separadas na pasta `figma-telas/`.

Importe os SVGs no Figma, transforme cada tela em um Frame e mantenha estes nomes:

- `01-home`
- `02-cursos-e-eventos`
- `03-detalhe-do-curso`
- `04-inscricao`
- `05-login-e-cadastro`
- `06-area-do-aluno`
- `07-cadastro-do-aluno`
- `08-validar-certificado`
- `09-painel-do-gestor`
- `10-area-do-professor`
- `11-paginas-publicas`
- `12-recuperar-senha`

No modo Prototype do Figma, selecione o botao/area clicavel e configure:

`On click` -> `Navigate to` -> frame de destino -> animacao `Instant` ou `Smart Animate`.

## Fluxo principal do aluno

| Tela de origem | Botao/area clicavel | Destino no Figma | Observacao |
|---|---|---|---|
| `01-home` | Menu `Cursos` | `02-cursos-e-eventos` | Entrada principal para agenda. |
| `01-home` | Card `Detalhes` do curso aberto | `03-detalhe-do-curso` | Mostra a pagina do curso. |
| `01-home` | `Agenda do semestre` | `02-cursos-e-eventos` | Atalho para lista de cursos. |
| `02-cursos-e-eventos` | `Home` | `01-home` | Voltar para pagina inicial. |
| `02-cursos-e-eventos` | `Detalhes` em Processo Legislativo | `03-detalhe-do-curso` | Abre o curso selecionado. |
| `03-detalhe-do-curso` | `Voltar` | `02-cursos-e-eventos` | Retorna para agenda. |
| `03-detalhe-do-curso` | `Inscrever-se` | `04-inscricao` | Inicio da inscricao. |
| `04-inscricao` | `Fazer login` | `05-login-e-cadastro` | Caminho quando usuario ainda nao esta logado. |
| `04-inscricao` | `Confirmar inscricao` | `06-area-do-aluno` | Caminho quando usuario ja esta logado. |
| `05-login-e-cadastro` | `Entrar` | `06-area-do-aluno` | Login comum do aluno. |
| `05-login-e-cadastro` | `Criar cadastro` | `07-cadastro-do-aluno` | Novo aluno. |
| `07-cadastro-do-aluno` | `Cadastrar` | `06-area-do-aluno` | Cadastro concluido e inscricao confirmada. |
| `06-area-do-aluno` | `Sair` | `01-home` | Encerra sessao e volta ao publico. |

## Fluxo de certificado

| Tela de origem | Botao/area clicavel | Destino no Figma | Observacao |
|---|---|---|---|
| `01-home` | `Validar certificado` | `08-validar-certificado` | Consulta publica. |
| `08-validar-certificado` | `Pesquisar` | `08-validar-certificado` | Para prototipo simples, manter na mesma tela mostrando resultado valido/invalido. |
| `01-home` | `Area do aluno` | `06-area-do-aluno` | Acesso rapido ao historico e certificados. |

Sugestao para ficar mais claro para apresentacao: duplique `08-validar-certificado` no Figma e crie dois frames separados, `08a-certificado-valido` e `08b-certificado-invalido`. Depois conecte:

- `Pesquisar` com codigo preenchido -> `08a-certificado-valido`
- `Pesquisar` com codigo errado -> `08b-certificado-invalido`

## Fluxos publicos

| Tela de origem | Botao/area clicavel | Destino no Figma | Observacao |
|---|---|---|---|
| `01-home` | Menu `Escola` | `11-paginas-publicas` | Conteudo institucional. |
| `01-home` | Menu `Acervo` | `11-paginas-publicas` | Biblioteca/publicacoes. |
| `01-home` | Menu `Noticias` | `11-paginas-publicas` | Noticias do portal. |
| `01-home` | Menu `Contato` | `11-paginas-publicas` | Dados de contato. |
| `01-home` | `Nova parceria formalizada` | `11-paginas-publicas` | Exemplo de noticia. |
| `01-home` | `Publicacoes recentes` | `11-paginas-publicas` | Exemplo de acervo. |

Sugestao para apresentacao ao chefe: duplique `11-paginas-publicas` em frames separados se quiser mostrar cada menu com mais precisao:

- `11a-a-escola`
- `11b-acervo`
- `11c-parcerias`
- `11d-noticias`
- `11e-contato`

## Fluxos restritos

| Tela de origem | Botao/area clicavel | Destino no Figma | Observacao |
|---|---|---|---|
| `01-home` | `Entrar` | `05-login-e-cadastro` | Acesso geral. |
| `05-login-e-cadastro` | `Gestor` | `09-painel-do-gestor` | Simulacao de perfil gestor. |
| `05-login-e-cadastro` | `Professor` | `10-area-do-professor` | Simulacao de perfil professor. |
| `05-login-e-cadastro` | `Aluno` | `06-area-do-aluno` | Simulacao de perfil aluno. |
| `05-login-e-cadastro` | `Esqueci minha senha` | `12-recuperar-senha` | Recuperacao de acesso. |
| `12-recuperar-senha` | `Enviar link` | `05-login-e-cadastro` | Depois do envio, volta ao login. |

## Navegacoes extras recomendadas

Estas nao precisam estar todas prontas visualmente, mas ajudam o chefe a entender o fluxo:

| Tela | Elemento | Destino recomendado |
|---|---|---|
| `02-cursos-e-eventos` | `Filtrar` | `02-cursos-e-eventos`, com lista filtrada |
| `02-cursos-e-eventos` | `Lista espera` | `04-inscricao` |
| `03-detalhe-do-curso` | Abas `Ementa`, `Professor`, `Cronograma` | Variantes duplicadas de `03-detalhe-do-curso` |
| `04-inscricao` | `Selecionar` turma | `04-inscricao`, com turma marcada |
| `04-inscricao` | `Fila espera` | `05-login-e-cadastro` ou `06-area-do-aluno` |
| `06-area-do-aluno` | `Cancelar` | Modal/overlay de confirmacao |
| `06-area-do-aluno` | `Baixar` certificado | Overlay simples de download concluido |
| `06-area-do-aluno` | `Atualizar meus dados` | Duplicar `07-cadastro-do-aluno` como edicao de perfil |
| `09-painel-do-gestor` | Menu lateral `Cursos` | Frame de gestao de cursos |
| `09-painel-do-gestor` | Menu lateral `Inscricoes` | Frame de inscricoes e fila |
| `09-painel-do-gestor` | Menu lateral `Certificados` | Frame de emissao de certificados |
| `10-area-do-professor` | `Cursos vinculados` | Frame com lista de alunos |
| `10-area-do-professor` | `Materiais` | Frame de upload/lista de materiais |

## Importante

As setas desenhadas no SVG sao apenas indicacao visual de fluxo. No Figma, quem redireciona e o link criado manualmente no painel `Prototype`, sempre a partir do botao/area clicavel para o Frame de destino.
