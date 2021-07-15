# Plano de Iteração

> Este plano de iteração será usando como exemplo da disciplina Engenharia de Software II.

## Calendário da Interações

| Interação | Data início | Data final | Apresentação | Gerente | Detalhes |
| --------- | :---------: | :--------: | :----------: | :-----: | :------: |
| It1 | 18/06/2021 | 30/06/2021 | 29/06/2021 | Gerente 1 (José Flávio) | Criar Documento de Visão, Modelos e Plano de Interação e Release. |
| It2 | 31/06/2021 | 12/07/2021 | 11/07/2021 | Gerente 2 (Flávio Roberto) | Detalhar US00, Implementar US00, Detalhar US01 e US02. |
| It3 | 13/07/2021 | 28/07/2021 | 27/07/2021 | Gerente 3 ("") | Implementar US01 e US02, Detalhar US03 e US04, Testar US00. |
| It4 | 29/07/2021 | 12/08/2021 | 11/08/2021 | Gerente 4 ("") |  |
| It5 | 13/07/2021 | 24/08/2021 | 23/08/2021 | Gerente 5 ("") |  |
| It6 | 25/08/2021 | 08/09/2021 | 07/09/2021 | Gerente 6 ("") |  |

- Observação 1: Cada Iteração de ser cadastrada como Milestones no GitHub.
- Observação 2: Use este repositório como Modelo.

## Descrição das Tarefas em cada Iteração

### T01 - Iteração 1 - Planejamento

A Iteração 1 começou dia 18/06/2021 e vai até 25/06/2021. As atividades dessa tarefa são:

- Criar repositório do projeto no GitHub com .gitignore para a linguagem do projeto;
- Definir tecnologia do projeto e colocar no README.md do repositório;
- Postar o link de tutoriais com a tecnologia do seu projeto no fórum do sigaa e colocar no README.md;
- Criação do Documento de Visão no formato Markdown, crie um diretório "docs no repositório;
  - Deve conter lista de requisitos funcionais, requisitos não funcionais, perfil de usuários e tabela de riscos;
- Criação do Documento de Modelos com o Modelo Conceitual, Modelo de Dados e o Dicionário de Dados, no formato Markdown, coloque no diretório "docs" do repositório;
- Coloque links para a documentação no README.md do repositório;
- Colocar Estrutura inicial do Projeto no repositório;

Nesta iteração temos atividades diferentes para dois perfis Gerentes e Analistas:

#### Gerentes

- Criar Milestones para a Iteração 1;
- Definir e descrever as tarefas (issues) da Iteração 1 (milestone) e alocar as issues para cada membro da equipe;
- Definir que parte do Documento de Visão cada membro da equipe vai preparar;
- Definir que parte do Documento de Modelos cada membro da equipe vai preparar;
- Criar o repositório de software no GitHub;
- Fechar tarefas quando elas forem concluída;

#### Analista

- Trabalhar nas tarefas e realizar pequenos commits marcando com a hashtag da issue;
- Enviar commits da parte do Documento de Visão que preparou;
- Enviar commits da parte do Documento de Modelos que preparou;
- Avisar ao gerente quando concluir uma tarefa;

O gerente deve enviar nesta tarefa o link do repositório e o link dos dois documentos no SIGAA.

> OBS: A cada mudança de gerente tem que ser colocado o detalhamento da Interação que o Gerente faz parte.



### T02 - Iteração 2 - Inicialização

As atividades da **Iteração 2** são:

* Atualização do **Documento de Visão**, pode adicionar requisitos funcionais, se necessário;
* Atualização do **Documento User Stories** com a lista de User Stories, pode adicionar *User Stories* se necessário.
  * Deve ser detalhado pelo menos **mais dois User Stories**;
  * Deve ser implementado pelo menos **dois User Stories**;
  * Um User Story pode ser formado de um ou mais requisitos funcionais;
  * Um dos User Stories a ser implementado é o User Story *base* definido na Iteração anterior;
* Criar o **Documento da Arquitetura** apenas com o modelo (imagem) da *Arquitetura Geral do Sistema* e descreva cada parte desta arquitetura;
  * Ainda não precisa ser o Documento Arquitetural completo, mas a arquitetura geral do sistemas deste a tela até a base de dados;
  * [Modelo em Markdown](doc-arquitetura.md)
  * [Modelo do Google Docs](https://docs.google.com/document/d/1i80vPaInPi5lSpI7rk4QExnO86iEmrsHBfmYRy6RDSM/edit?usp=sharing);
* Criar **Documento do Tamanho Funcional** com *Análise de Pontos de Função - APF*;
  * [Modelo em Markdown](doc-apf.md)
  * [Modelo do Google Docs](https://docs.google.com/document/d/1s4bMbrpQt9RF6tymXvI0HHfQO14hMyL08UxmX1eH82s/edit?usp=sharing);
  * Faça a contagem indicativa do tamanho funcional do software;
  * Faça a contagem detalhada do tamanho funcional dos User Stories detalhados;
* Criar documento com o **Termo de Abertura do Projeto - TAP**, no google docs
  * O termo de abertura deve ser feito só no google drive.
  * Pesquise modelos deste documento para comparar;
  * [Modelo do Google Docs](https://docs.google.com/document/d/1huAQAJZqdNiqcEudpXUQJ2KaIQAGT65Wpqqx-LT8ZCs/edit?usp=sharing);

#### Gerentes It02

* Criar Milestones da Iteração 2;
* Definir e descrever as tarefas (issues) da Iteração 2 (milestones) e
alocar as issues para cada membro da equipe;
* Definir qual User Story cada membro da equipe vai especificar/detalhar;
  * Detalhar ou Especificar um US é criar a descrição (estória do usuário) e os testes de aceitação;
* Definir quem vai construir a Arquitetura Geral do Sistema que faz parte do **Documento Projeto Arquitetural** e o que cada membro da equipe vai preparar;
* O gerente deve fazer a contagem indicativa do tamanho funcional de Projeto;
* Definir quem vai fazer a contagem detalhada do tamanho funcional de cada User Story;
* Fechar tarefas se concluída;

#### Analistas It02

* Trabalhar nas tarefas e realizar pequenos commits marcando com a hashtag da issue;
* Enviar commits do User Story que detalhou;
* Enviar commits da contagem do User Story que detalhou;
* Enviar commits das outras tarefas;
* Avisar ao gerente quando concluir uma tarefa;

#### Desenvolvedor It02

* Trabalhar nas tarefas e realizar pequenos commits marcando com a hashtag da issue;
* Enviar commits da implementação do User Story;
* Enviar commits da implementação de **Testes de Unidade** do User Story que implementou;
* Avisar ao gerente quando concluir uma tarefa;

#### Testador It02

* Trabalhar nas tarefas e realizar pequenos commits marcando com a hashtag da issue;
* Executar cada teste de aceitação do User Story, anotando o resultado em um Markdown dos Resultados dos Testes de Aceitação;
* Cadastrar issues de bugs caso os Testes de Aceitação não passem;
* Avisar ao gerente quando concluir uma tarefa;

