# Como criar uma tabela com dados aleatórios contendo o nome dos municípios do Brasil

## Passos:

1. No Power BI, vá para **"Obter Dados"** e selecione **"Arquivo CSV"**.
2. Escolha o arquivo `municipios-com-e-sem-acentos.csv`, que já contém a lista dos municípios do Brasil, tanto com quanto sem acentuação, pronta para uso como dimensão.
3. A tabela será carregada com colunas como `id`, `nome_acentuado`, `nome_sem_acentos` e `estado`.

> ✅ Como o arquivo já foi processado previamente, não é necessário corrigir nomes com letras duplicadas nem extrair dados diretamente do site do IBGE.

## Gerar dados aleatórios:

Depois de carregar a tabela, você pode gerar dados aleatórios para cada município. Para isso, crie uma nova coluna com valores aleatórios utilizando a função `Number.RandomBetween()`.

### Exemplo de coluna com valores aleatórios:

```m
Number.RandomBetween(10000, 50000)
