# Cálculo do Tamanho Funcional com APF

## Contagem Indicativa (Ci)

Na contagem indicativa só é necessário analisar os **ALIs** (Arquivos Lógicos Internos) com o valor de **35 PF** cada 
e os **AIEs** (Arquivos de Interface Externa) com o valor de **15 PF** cada.

| ALI/AIE           | Entidades Relacionadas     |  PF  |
|------------------ |--------------------------- |------|
| AIE Administrador | Administrador              |  15  |
| AIE Autor         | Autor                      |  15  |
| ALI Usuário       | Usuário                    |  35  |
| ALI Evento        | Evento                     |  35  |
| ALI Laboratório   | Laboratório                |  35  |
| ALI Post          | Post                       |  35  |
| ALI Notícia       | Notícia                    |  35  |
| ALI Projeto       | Projeto                    |  35  |
| ALI Comentario    | Comentario                 |  35  |


Tamanho Funcional **Ci = 275 PF** ( (275 -35%) PF < Ci <= (275 +35%) PF)
7 ALI * 35 PF= 245
2 AIE * 15 PF= 30 
DFP= 275 PF


### Duração e custo considerando produtividade 8h/PF e Ci = 275 PF 
275 PF * 8h/PF= 2200H
2200h/8h = 275 Dias


### Duração e custo considerando produtividade 1h/PF e Ci = 178,75 PF


## Contagem Estimativa (Ce)

Na Ce todas as funções de dados são classificados como baixa complexidade.

| ALI/AIE           | Entidades Relacionadas     | PF |
|------------------ |--------------------------- |----|
| AIE Administrador | Administrador              | 5  |
| AIE Autor         | Autor                      | 5  |
| ALI Usuário       | Usuário                    | 7  |
| ALI Evento        | Evento                     | 7  |
| ALI Laboratório   | Laboratório                | 7  |
| ALI Post          | Post                       | 7  |
| ALI Notícia       | Notícia                    | 7  |
| ALI Projeto       | Projeto                    | 7  |
| ALI Comentario    | Comentario                 | 7  |
|                   | Total de Dados             | 59 |


Na Ce todas as operações elementares são classificadas como de média complexidade: 
**EE** tem 4 PF, **CE** tem 4 PF e **SE** tem 5 PF. 


| Operação                | Tipo | Complexidade    |  PF  |
|-------------------------|------|-----------------|------|
| Cadastrar Usuário       |  EE  | Média           |  4   |
| Alterar Usuário         |  EE  | Média           |  4   |
| Listar Usúarios         |  CE  | Média           |  4   |
| Deletar Usúario         |  EE  | Média           |  4   |
| Banir Usúario           |  EE  | Média           |  4   |
| Cadastrar Autor         |  EE  | Média           |  4   |
| Alterar Autor           |  EE  | Média           |  4   |
| Deletar Autor           |  EE  | Média           |  4   |
| Cadastrar Post          |  EE  | Média           |  4   |
| Alterar Post            |  EE  | Média           |  4   |
| Listar Posts            |  SE  | Média           |  5   |
| Analisar Post           |  CE  | Média           |  4   |
| Solicitação de Post     |  EE  | Média           |  4   |
| Deletar Post            |  EE  | Média           |  4   |
| Cadastrar Laboratório   |  EE  | Média           |  4   |
| Alterar Laboratório     |  EE  | Média           |  4   |
| Listar Laboratório      |  SE  | Média           |  5   |
| Deletar Laboratório     |  EE  | Média           |  4   |
| Cadastrar Evento        |  EE  | Média           |  4   |
| Alterar Evento          |  EE  | Média           |  4   |
| Listar Evento           |  CE  | Média           |  4   |
| Deletar Evento          |  EE  | Média           |  4   |
| Cadastrar Projeto       |  EE  | Média           |  4   |
| Alterar Projeto         |  EE  | Média           |  4   |
| Listar Projeto          |  SE  | Média           |  5   |
| Deletar Evento          |  EE  | Média           |  4   |
| Cadastrar Notícia       |  EE  | Média           |  4   |
| Alterar Notícia         |  EE  | Média           |  4   |
| Listar Notícias         |  SE  | Média           |  5   |
| Deletar Notícia         |  EE  | Média           |  4   |
| Fazer Comentario        |  EE  | Média           |  4   |
| Alterar Comentario      |  EE  | Média           |  4   |
| Listar Comentarios do Post |  CE  | Média           |  4   |
| Listar Comentarios da Notícia |  CE  | Média           |  4   |
| Deletar Comentario      |  EE  | Média           |  4   |
| Buscar Posts            |  SE  | Média           |  5   |
|                         |      | Total           |  149  |

Tamanho Funcional: Dados + Operações

__Ce__ = 59 PF + 149 PF = 208


## Contagem Detalhada
