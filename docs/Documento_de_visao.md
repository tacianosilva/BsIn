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
| RF001 - Manter cadastro de Autores | Cadastro dos Autores/Administradores dos Site | Administrador |
| RF002 - Manter cadastro de Usurário | O usuario se cadastrará na aplicação, no cadastro de usuario tem nome, e-mail, matricula, senha e celular. | Usuário |
| RF003 - Manter cadastro de Post| Post terá codigo, autor ,titulo, data, descrição, imagem. | Administrador |
| RF004 - Manter cadastro para os Comentarios | Administrar os comentarios: autorizar ou apagar-los. | Administrador |
| RF005 - Manter cadastro de Evento | O evento tem codigo, titulo, data, descrição, imagem, palestras, mini-cursos, oficinas e link. | Administrador |
| RF006 - Manter cadastro de Projetos | O projeto tem codigo, titulo, autores, descrição , estado, candidatos,supervisor e orientador. | Administrador |
| RF007 - Manter cadastro de Noticias | Divulgar noticias com links externos tendo assim codigo, autor, titulo, descrição e link. | Administrador |
| RF008 - Manter cadastro de Comentarios | O Usuário poderá fazer um comentario, edita-lo ou exclui-lo.| Usuário |
| RF009 - Manter cadastro de Laboratórios | O laboratório tem codigo, titulo, encarregados, descrição, projetos, membros. | Administrador |
| RF010 - Manter solicitação de post| A solicitação terá, codigo, autor ,titulo, data, descrição, imagem e será solicitado pelo usuário. | Usuário |


### Modelo Conceitual

Abaixo apresentamos o modelo conceitual usando o __YUML__.
![Modelo Conceitual](https://github.com/JFmaia/BsIn/blob/main/images/umlproj.PNG)

#### Descrição das Entidades

...

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









