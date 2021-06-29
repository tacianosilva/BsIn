# Documento de Modelos

## Descrição 

>Este documento descreve o modelo conceitual do software e é composto por um conjunto de Entidades e seus relacionamentos. Pode ser feito com Diagramas de Classes da UML ou com outras metodologias de modelagem como Modelagem Entidade - Relacionamento. Deve conter o modelo de Dados e caso necessário um dicionário de dados.

## Modelo Conceitual

[Link para o modelo](https://whimsical.com/2bn9CaFL7wd13ZWvYS2Ekd@2Ux7TurymMmgVQB5Ls7w)

### Descrição das Entidades

Descrição sucinta das entidades presentes no sistema.

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









