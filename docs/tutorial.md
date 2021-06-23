# Tutorial

Clone o projeto (se for membro) ou Fork o projeto (git clone);

## Passo 1

> Sempre atualize o branch main antes de tudo, então na linha de comando use __git pull__ ;

## Passo 2

> Crie um novo branch para trabalhar em funcionalidade (feat) ou em correção de bugs (fix) ou em documentação (doc), etc. Use a nomeclatura feat/issueXX ou fix/bugXX. Sempre estando inicialmente no branch main Comando: __git checkout -b feat/issueXX__ ;

## Passo 3

> Faça commits no branch indicando o id da issue no final. Coloque mensagens curtas e significativas: __git commit -m "Minha mensagem curta e significativa #id"__ ;

## Passo 4

> Faça push do seu branch para o repositório remoto: __git push origin feat/issueXX__ ;

## Passo 5

> Crie um pull request (PR) do seu branch para o branch main ou dev;

> Aguarde a revisão do pull request (PR). Caso precise de ajustes basta fazer novos commits no branch. O PR será automaticamente atualizado;

## Passo 6
Quando o PR  for aprovado alguém (gerente ou líder) fará o merge do PR:
 
> git checkout main 

> git merge feat/issueXX

## Passo 7

Atualizando sua branch com as atualizações da main, primeiro entre e sua branch exemplo: __git checkout feat/issueXX__ logo depois utilize esses comandos abaixo;

> git fetch origin

> git rebase origin/main
