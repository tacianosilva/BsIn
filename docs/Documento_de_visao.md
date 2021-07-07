# Documento de Visão

## Descrição do Projeto

> O BsIn é uma aplicação web, que tem o objetivo de proporcionar aos estudantes do curso de BSI da UFRN-CERES informação sobre o curso, como curiosidades, dicas, tutoriais que ajudaram no seu percurso,informações dos eventos que ocorrem no curso, além das informações dos laboratorios do curso, seus membros e projetos abertos, dando a oportunidade de sé candidatar a tal projeto. 

## Equipe e Definição de Papéis

| Membro    | Papel     | Email     |
| --------- |:---------:|:---------:|
| Flavio Roberto | Analista, Desenvolvedor | flaviovorthrox@yahoo.com.br|
| Gabriel Gonçalo | Analista, Desenvolvedor |  |
| José Flávio | Gerente, Desenvolvedor | jfmaia741@gmail.com |
| Pedro Henrique | Analista, Desenvolvedor | p.h.t.s30@gmail.com |

### Matriz de Competências

| Membro    | Competêcia    |
| --------- |:---------:    |
| Flavio Roberto | Desenvolvedor Python Django, Android Java |
| Gabriel Gonçalo | Desenvolvedor Python, Django, C |
| José Flávio | Gestão, Desenvolvedor Dart, Flutter, VScode, Python, Django, Markdown |
| Pedro Henrique | Desenvolvedor Python Django, C, Java  |

## Perfis dos Usuários

O sistema poderá ser utilizado por diversos usuários. Temos os seguintes perfis/atores:
| Perfil   | Descrição   |
| ---------|:---------:  |
| Administrador | Este usuário podera realizar qualquer função. |
| Usuário | Este usuário podera comentar post, vê laboratorios e projetos, vê eventos existentes, vê noticias e solicitar criação de post. |


## Lista de Requisitos Funcionais

| Requisitos | Descrição | Ator |
| ---------- | :-------: | :--: |
| RF001 - Cadastrar Usuário | O usuário terá como atributos, nome, senha, status, dataCadastro, email, foto, statusAutor,mod, ele poderá realizar comentarios e solicitação de Post. | Usuário |
| RF002 - Alterar Usuário | O usuário poderá alterar seus dados esses que são, nome, senha, email, foto. | Usuário |
| RF003 - Perfil Usuário | O usuário poderá ver seus dados esses que são, nome, senha, email, foto e se ele é um autor ou administrador. | Usuário |
| RF004 - Deletar Usuário | O usuário poderá deletar sua conta no site, excluindo seus dados . | Usuário |
| RF005 - Cadastrar Autores | O administrador cadastrará um autor, dando permisão para ele, com a permisão o autor poderá fazer posts, cadastros de eventos, cadastros de laboratórios, cadastro de projetos e publicar notícias. | Administrador |
| RF006 - Deletar Autores | O administrador irá tirar os diretos de autor de um usuario. | Administrador |
| RF007 - Cadastrar Post | Cadastrar um post requer os atributos, titulo, descrição, imagem(opcional), dataPost, autor, comentarios. | Administrador/Autor |
| RF008 - Alterar Post | Alterar um post mudanças nos atributos, titulo, descrição, imagem(opcional). | Administrador/Autor |
| RF009 - Listar Posts | Será uma funcionalidade onde listará todos os posts e seus comentarios para o administrador, autor e usuário, claro que para o administrador terá a opção de deletar e para o autor só de alterar. | Administrador/Autor/Usuário |
| RF010 - Deletar Post | Poderá ser deletado um post, sé o post tiver sido ofensivo, com coteudo improprio e com qualquer tipo de preconceito. | Administrador |
| RF011 - Analisar Post | Todo post criado por um usuario para um post deve passar pela analise de um administrador para poder entrar no ar. | Administrador |
| RF012 - Solicitação de Post | O usuário pode fazer uma solicitação de post, que seria a criação de um post que fica na espera da aceitação do administrador. | Usuário |
| RF013 - Cadastrar Evento | Evento tem como atributos, nomeCordEvento, title, dataInicio, dataFinal, descrição, imagem(opcional), isFree. | Administrador/Autor |
| RF014 - Alterar Evento | Em evento pode ser alterado, nomeCordEvento, title, dataInicio, dataFinal, descrição, imagem(opcional), isFree. | Administrador/Autor |
| RF015 - Listar Eventos | Será uma funcionalidade onde listará todos os eventos criados para o administrador, autor e usuário, claro que para o administrador terá a opção de deletar e para o autor só de alterar. | Administrador/Autor/Usuário |
| RF016 - Deletar Eventos | Deletar evento também só é feito pelo administrador. | Administrador |
| RF017 - Cadastrar Laboratório | Ao cadastrar laboratório terá os atributos, nomeLab, nomeCord, membros, projetos, descrição, dataInicio. | Administrador/Autor |
| RF018 - Alterar Laboratório | Alterar laboratório poderá alterar os atributos, nomeLab, nomeCord, membros, projetos, descrição, dataInicio. | Administrador/Autor |
| RF019 - Listar Laboratórios |Será uma funcionalidade onde listará todos os laboratórios criados para o administrador, autor e usuário, claro que para o administrador terá a opção de deletar e para o autor só de alterar. | Administrador/Autor/Usuário |
| RF020 - Deletar Laboratório |  Deletar Laboratório também só é feito pelo administrador. | Administrador |
| RF021 - Cadastrar Projeto | Cadastrar projeto tem como atributos, nomeProj, nomeCord, descrição, dataInicio, status, membros. | Administrador/Autor |
| RF022 - Alterar Projeto | Alterar projeto pode mudar os atributos, nomeProj, nomeCord, descrição, dataInicio, status, membros. | Administrador/Autor |
| RF023 - Listar Projetos | Será uma funcionalidade onde listará todos os projetos criados para o administrador, autor e usuário, claro que para o administrador terá a opção de deletar e para o autor só de alterar. | Administrador/Autor/Usuário |
| RF024 - Deletar Projeto | Deletar projeto também só é feito pelo administrador. | Administrador |
| RF025 - Cadastrar Notícia | Cadastrar notícia tem como atributos, title, nomeAutor, dataPubli, comentarios, descrição. | Administrador/Autor |
| RF026 - Alterar Notícia | Alterar notícia tem como alterar os atributos, title, nomeAutor e descrição. | Administrador/Autor |
| RF027 - Listar Notícias | Será uma funcionalidade onde listará todos os notícias criadas para o administrador, autor e usuário, claro que para o administrador terá a opção de deletar e para o autor só de alterar. | Administrador/Autor/Usuário |
| RF028 - Deletar Notícia | Deletar notícia também só é feito pelo administrador. | Administrador |


### Modelo Conceitual

Abaixo apresentamos o modelo conceitual usando o __YUML__.
![Modelo Conceitual](https://github.com/JFmaia/BsIn/blob/main/images/umlproj.PNG)

#### Descrição das Entidades

| Entidade | Descrição |
| -------- | :-------: |
| Usuário  | O usuário é uma entidade que aproveitara a aplicação explorandoa e usufruindo das informações oferecidas, podendo ele também contribuir, com seus comentarios e sugestões de posts. |
| Adiministrador | Sendo como um moderador, podendo fazer tudo na aplicação desde criar a excluir, claro com a máxima cautela, moderando e também dando direitos a outras pessoas para ajudar e escrever post, sendo esses os autores. |
| Autor | O autor tem direitos, para fazer post, cadastrar laboratório, evento, projetos e notícias, mas não podendo excluir usuarios e nem claro os adms. |
| Notícias | Uma informação em destaque no site onde terá para todos verem, tendo o titulo do autor, data e descrição, podendo tbm ser feitos comentários nela. |
| Evento | Evento como já dito pode ser uma data especial, uma comemoração ou uam reunião, como a semana do bsi, onde temos palestras, coffe break e minicursos, tendo assim suas descrição, data de inicio e fim. |
| Laboratório | Os laboratórios são os lugares onde muitos alunos e professores usam para fazer e estudar seus projetos, seja de extensão ou pesquisa, claro com alguem tomando conta de tudo sendo o responsavel e criador do laboratório. |
| Projeto | Projetos fazem parte de um laboratório, com seus membros, orientador e supervisor, tendo vagas ou não, podem ser de extesão ou pesquisa. |

## Lista de Requisitos Não-Funcionais

| Identificador | Nome | Categoria | Descrição |
| ------------- | :--: | :-------: | :-------: |
| RNF001 | Acessibilidade via navegador | Usabilidade | O sistema será construido para rodar em ambiente web |
| RNF002 | Agilidade no atendimento | Disponibilidade | Todas as perguntas passarão por um curto prazo de avaliação, e se tiver relevância, será encaminhado para o forum de perguntas |
| RNF003 | Privacidade ao cliente | Ética | O sistema não fornecerá quaisquer dados de caráter privativo |

## Riscos

Tabela com o mapeamento dos riscos do projeto, as possíveis soluções e os responsáveis.

| Data    | Risco   | Prioridade    | Responsável   | Status    | Providências/Solução      |
| ------- | ------- | ------------- | ------------- | --------- | ------------------------- |
| 20/06/2021 | Não aprendizado das ferramentas utilizadas pelos componentes do grupo | Alta | Todos | Vigente | Reforçar estudos sobre as ferramentas e aulas com a integrante que conhece a ferramenta | 
| 20/06/2021 | Divisão de tarefas mal sucedida | Baixa | Gerente | Vigente | Acompanhar de perto o desenvolvimento de cada membro da equipe |
| 20/06/2021 | Implementação de protótipo com as tecnologias | Alta | Todos | Resolvido | Encontrar tutorial com a maioria da tecnologia e implementar um caso base do sistema |
| 20/06/2021 | Ausênsia por qualquer motivo de um membro | Média | Gerente | Vigente | Planejar o cronograma tendo em base a agenda do projeto, realocando tarefas para os outros membros e prorrogando a data de finalização |
| 20/06/2021 | Ausência por qualquer motivo do cliente | Média | Gerentes | Vigente | Planejar o cronograma tendo em base a agenda do cliente |


### Referências

[Link 1](https://docs.google.com/document/d/1cxzXiWN149Nq5htoB88HZVE0GmWTnHemAwHrNYXif98/edit)
[Link 2](https://github.com/tacianosilva/eng-software-2)









