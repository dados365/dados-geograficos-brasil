# CicloSul — site fictício para IC-05

Site estático de uma empresa fictícia de bicicletas compartilhadas em Florianópolis, criado para atividade de coleta e monitoramento de informações (scraping) na disciplina CIN7903.

## Publicar no GitHub Pages
1. Crie um repositório (ex.: `ciclosul`).
2. Envie todos os arquivos desta pasta para a raiz do repositório.
3. Em **Settings → Pages**, escolha **Deploy from a branch**, branch `main`, pasta `/ (root)`.

## Campos preparados para scraping
- `#preco-avulso`
- `#preco-mensal`
- `#preco-anual`
- `#preco-promocional`
- `#validade-promocao`
- `#total-bicicletas`
- `#total-ebikes`
- `#total-estacoes`
- `#total-bairros`
- `#titulo-expansao`
- `#texto-expansao`
- `#ultima-atualizacao`

Também há atributos `data-scrape` para permitir seletores alternativos.

## Sugestão para a aula
Use este commit como linha de base. Depois altere alguns valores no HTML e faça novo commit. O monitor dos estudantes deve detectar apenas mudanças relevantes previamente definidas.

### Mudanças sugeridas para a segunda rodada
- mensal: `39,90` → `44,90`
- bicicletas: `428` → `451`
- e-bikes: `96` → `124`
- estações: `37` → `41`
- expansão: incluir Ingleses
- última atualização: mudar sempre (ruído proposital)

> Todo o conteúdo e a marca CicloSul são fictícios e destinados exclusivamente a fins didáticos.
