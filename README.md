## Lista de Compras - Relatório

Link: https://lista-compras-ignacio.herokuapp.com/
Inicialmente comecei a pesquisar sobre o que eu poderia fazer, queria algo simples, mas que fosse "útil" para fazer sentido.
Pensei em extrair o conteúdo de uma API externa e criar um site com isso, mas não encontrei nenhuma que me fizesse ter uma grande ideia, então acabei optando por fazer algo bem comum, um to do list.
Porém, para não ficar tão comum, fiz uma alteração e acabei criando um site simples de lista de compras, o qual o usuário consegue adicionar itens para comprar, ler essa lista, mudar os itens e apagar quando necessário (basicamente um CRUD).

Lendo a documentação do django achei bem tranquilo, mesmo assim fiz um curso rápido na alura pra ter uma ajuda. Rapidamente consegui criar a tela inicial e fazer aparecer os itens do banco. Depois fui fazer a parte de adicionar os itens. Escolhi o postgresql por já ter uma certa familiaridade e ter ótima compatibilidade.
Tive um pouco de dificuldade nessa parte porque demorei para entender como os formulários funcionavam em django. Acabei tendo que usar bootstrap por não conseguir deixar bonitinho o formulário sem ele e uma biblioteca, mas no final deu certo.
Depois disso, como tinha tempo, pensei em melhorar e tornar realmente em um crud, criando as ações de alterar e apagar os dados. Não foi nada difícil, acabei quebrando um pouco a cabeça porque estava retornando os dados pro lugar errado e criava os itens duas vezes no banco, mas depois que resolvi isso, ficou bem tranquilo e consegui terminar.

Após acabar, pesquisei alguns vídeos de hospedagem gratuita, já que nunca tinha usado, escolhi heroku por recomendação de vocês e por ser bem objetivo e fácil de usar. Em menos de 20 minutos, a página já estava online e pronta.
