# Como criar uma tabela com dados aleatórios contendo o nome dos municípios de Santa Catarina

## Passos:

1. No Power Query do Power BI, clique em "Nova Fonte" e selecione "Web".
2. Insira o link do IBGE que contém o nome dos municípios: https://www.ibge.gov.br/explica/codigos-dos-municipios.php#SC.
3. A tabela do estado de Santa Catarina é a de número 25.
4. Note que o Power BI já trouxe a tabela configurada corretamente para você, contendo os nomes dos primeiros municípios. Alguns nomes (por exemplo, "AAbdon Batista", "BBalneário Arroio do Silva") possuem a primeira letra duplicada. Isso se deve ao formato da tabela disponibilizada pelo IBGE.

## Como corrigir a duplicação de letras:

Para arrumar os nomes manualmente seria muito trabalhoso. Por isso, utilize o código DAX abaixo para criar uma coluna que remove o caractere duplicado no início dos nomes de municípios. Esse código vai verificar se a primeira letra está duplicada e, se for o caso, remover a duplicação.

### Código DAX:

= Table.AddColumn(#"Tipo Alterado", "nome", each 
    if Text.Start([Municípios de Santa Catarina], 1) = Text.Middle([Municípios de Santa Catarina], 1, 1) 
    then Text.Middle([Municípios de Santa Catarina], 1) 
    else [Municípios de Santa Catarina], 
    type text)

### Explicação do código:

- `Text.Start([Municípios de Santa Catarina], 1)`: Pega a primeira letra do nome do município.
- `Text.Middle([Municípios de Santa Catarina], 1, 1)`: Pega a segunda letra do nome.
- O código verifica se a primeira letra é igual à segunda.
- Se forem iguais, remove a primeira letra duplicada, deixando o nome correto.
- Se não forem iguais, mantém o nome original.

## Gerar dados aleatórios:

Depois de ajustar os nomes dos municípios, você pode gerar dados aleatórios para cada um. Para isso, crie uma nova coluna com valores aleatórios utilizando a função `Number.RandomBetween()`.

### Exemplo de coluna com valores aleatórios:

Number.RandomBetween(10000, 50000)

Essa função vai gerar números inteiros aleatórios entre 10.000 e 50.000, que podem ser utilizados como dados complementares, como população, índices ou outros.

### Dica:

Após criar a coluna com valores aleatórios, lembre-se de formatá-la como "Número Inteiro" no Power Query.

Agora você tem uma tabela de municípios de Santa Catarina corrigida e com dados aleatórios prontos para análise!
