# Documento de Modelos

## Descrição 

>Este documento descreve o modelo conceitual do software e é composto por um conjunto de Entidades e seus relacionamentos. Pode ser feito com Diagramas de Classes da UML ou com outras metodologias de modelagem como Modelagem Entidade - Relacionamento. Deve conter o modelo de Dados e caso necessário um dicionário de dados.

## Modelo Conceitual

![Modelo Conceitual](https://github.com/JFmaia/BsIn/blob/main/images/umlproj.PNG)

### Descrição das Entidades

| Entidade | Descrição |
| -------- | :-------: |
| Usuário  | O usuário é uma entidade que aproveitara a aplicação explorandoa e usufruindo das informações oferecidas, podendo ele também contribuir, com seus comentarios e sugestões de posts. |
| Adiministrador | Sendo como um moderador, podendo fazer tudo na aplicação desde criar a excluir, claro com a máxima cautela, moderando e também dando direitos a outras pessoas para ajudar e escrever post, sendo esses os autores. |
| Autor | O autor tem direitos, para fazer post, cadastrar laboratório, evento, projetos e notícias, mas não podendo excluir usuarios e nem claro os adms. |
| Notícias | Uma informação em destaque no site onde terá para todos verem, tendo o titulo do autor, data e descrição, podendo tbm ser feitos comentários nela. |
| Evento | Evento como já dito pode ser uma data especial, uma comemoração ou uam reunião, como a semana do bsi, onde temos palestras, coffe break e minicursos, tendo assim suas descrição, data de inicio e fim. |
| Laboratório | Os laboratórios são os lugares onde muitos alunos e professores usam para fazer e estudar seus projetos, seja de extensão ou pesquisa, claro com alguem tomando conta de tudo sendo o responsavel e criador do laboratório. |
| Projeto | Projetos fazem parte de um laboratório, com seus membros, orientador e supervisor, tendo vagas ou não, podem ser de extesão ou pesquisa. |

## Dicionário de Dados
### Usuário 
| Atributo | classe | Tipo | Tamanho | Descrição |
| -------- | ------ | ---- | ------- | --------- |
| nomeUsuár| Determinante | Texto | 50 | Nome do usuário ao realizar login |
| senhaUsuár | Simples | Texto | 30 | Senha do usuário |
| statusLog | Multivalorado |
| dataCadastr | Simples | Data | | Formato dd/mm/aaaa | 
| email | Simples | Texto | 50 | Email do usuário | 

### Noticias
| Atributo | classe | Tipo | Tamanho | Descrição |
| -------- | ------ | ---- | ------- | --------- |
|nomeAutor | Simples | Texto | 50 |  |
| tituloNoticia | Simples | Texto |  |  
| dataPubli | Simples | Data |  | Formato dd/mm/aaaa |

### Autor
| Atributo | classe | Tipo | Tamanho | Descrição |
| -------- | ------ | ---- | ------- | --------- |
| permissaoAdm | Simples | Boleano |

### Administrador 
| Atributo | classe | Tipo | Tamanho | Descrição |
| -------- | ------ | ---- | ------- | --------- |
| nomeAdm | simples | Texto | 50 |
| senhaAdm | simples | Texto | 50 |

### Laboratório
| Atributo | classe | Tipo | Tamanho | Descrição |
| -------- | ------ | ---- | ------- | --------- |
| nomeLaboratorio | Simples | Texto |
| NomeCoordenador | Simples | Texto |

### Evento
| Atributo | classe | Tipo | Tamanho | Descrição |
| -------- | ------ | ---- | ------- | --------- |
| nomeCoordenadorEvento | Simples | Texto | 50 |
| nomeEvento | Simples | Texto | 50 |
| dataInicio | Simples | Data | | Formato dd/mm/aaaa|
| dataEncerramento | Simples | Data | | Formato dd/mm/aaaa|
| Gratuito | Simples | boleano | 

### Projeto
| Atributo | classe | Tipo | Tamanho | Descrição |
| -------- | ------ | ---- | ------- | --------- |
| nomeCoordProjeto | Simples | Texto | 50 |
| nomeProjeto | Simples | Texto | 50 |
| objetivoProjeto | Simples | Texto | 200 |
| dataInicio | Simples | Data | | Formato dd/mm/aaaa|


### Referências

(coloque aqui, artigos, livros e sites utilizados e citados no documento).

[Link para o Documento de Visão.](https://github.com/JFmaia/BsIn/blob/main/docs/Documento_de_visao.md)









