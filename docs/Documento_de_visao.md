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
| RF001 - Manter Autores | Cadastro de autor,alterar, consultar e deletar autor. | Administrador |
| RF002 - Manter Usurário | O usuario se cadastrará na aplicação, poderá alterar seus dados, consultar seu perfil e se desejar excluir seu cadastro. | Usuário |
| RF003 - Manter Post| Poderá ser cadastrado, alterado, consultado, excluido, tendo também um status de aprovado ou em analise, pois os usuários irão poder fazer post, mas serão analisado podendo ou não ser aceito. | Administrador |
| RF004 - Manter Comentarios | Os comentatios serão criados, podendo ser alterados, consultados e excluidos, pois tendo qualquer ameaça,preconceito(racismo,maxismo,homofobia, etc..) | Administrador/Usuário |
| RF005 - Manter Evento | O evento será criado pelo administrador, podendo ser alterado, consultado e excluido. | Administrador |
| RF006 - Manter Projetos | O projeto será criado pelo administrador, podendo ser alterado, consultado e excluido. | Administrador |
| RF007 - Manter Noticias | A notícia será criado pelo administrador, podendo ser alterado, consultado e excluido. | Administrador |
| RF008 - Manter Laboratórios | O laboratório será criado pelo administrador, podendo ser alterado, consultado e excluido. | Administrador |

### Modelo Conceitual

Abaixo apresentamos o modelo conceitual usando o __YUML__.
![Modelo Conceitual](https://github.com/JFmaia/BsIn/blob/main/images/umlproj.PNG)

#### Descrição das Entidades

| Entidade | Descrição |
| -------- | :-------: |
| Usuário  | O usuário é uma entidade que aproveitara a aplicação explorandoa e usufruindo das informações oferecidas, podendo ele também contribuir, com seus comentarios e sugestões de posts. |
| Adiministrador | Sendo como um moderador, podendo fazer tudo na aplicação desde criar a excluir, claro com a máxima cautela, moderando e também dando direitos a outras pessoas para ajudar e escrever post, sendo esses os autores. |
| Autor | O autor tem direitos, para fazer post, cadastrar laboratório, evento, projetos e notícias, mas não podendo excluir usuarios e nem claro os adms. |
| Notícia | Uma informação em destaque no site onde terá para todos verem, tendo o titulo do autor, data e descrição, podendo tbm ser feitos comentários nela. |
| Evento | Evento como já dito pode ser uma data especial, uma comemoração ou uam reunião, como a semana do bsi, onde temos palestras, coffe break e minicursos, tendo assim suas descrição, data de inicio e fim. |
| Laboratórios | Os laboratórios são os lugares onde muitos alunos e professores usam para fazer e estudar seus projetos, seja de extensão ou pesquisa, claro com alguem tomando conta de tudo sendo o responsavel e criador do laboratório. |
| Projetos | Projetos fazem parte de um laboratório, com seus membros, orientador e supervisor, tendo vagas ou não, podem ser de extesão ou pesquisa. |

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









