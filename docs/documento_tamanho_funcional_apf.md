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

*Zorrin*
Tamanho Funcional **Ci = 275 PF** ( (275 -35%) PF < Ci <= (275 +35%) PF)

*Zorrin*
### Duração e custo considerando produtividade 8h/PF e Ci = 275 PF 

*Gabriel*
### Duração e custo considerando produtividade 1h/PF e Ci = (275 -35%) PF

| Entidades Relacionadas     |  PF  | Duração | Custo para o projeto| 
|--------------------------- |------| ------- | --------------------|
| Administrador              |  15  |   15h   |       R$ 81         |
| Autor                      |  15  |   15h   |       R$ 81         |
| Usuário                    |  35  |   35h   |       R$ 189        |
| Evento                     |  35  |   35h   |       R$ 189        |
| Laboratório                |  35  |   35h   |       R$ 189        |
| Post                       |  35  |   35h   |       R$ 189        |
| Notícia                    |  35  |   35h   |       R$ 189        |
| Projeto                    |  35  |   35h   |       R$ 189        |
| Comentario                 |  35  |   35h   |       R$ 189        |
| Total                      |  275 |   275h  |       R$ 1485       |


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


*Zorrin*, *Gabriel*
Na Ce todas as operações elementares são classificadas como de média complexidade: 
**EE** tem 4 PF, **CE** tem 4 PF e **SE** tem 5 PF. 


| Operação                | Tipo | Complexidade    |  PF  |
|-------------------------|------|-----------------|------|


Tamanho Funcional: Dados + Operações


## Contagem Detalhada
