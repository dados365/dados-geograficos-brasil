Topojson BR - Brasil
=====================

Este projeto contém arquivos no formato TopoJSON com os perímetros dos municípios brasileiros divididos por estado, convertidos a partir de GeoJSON. Esses arquivos são ideais para uso direto no Power BI na criação de **mapas coropléticos de formas**.

> Conversão realizada por **Amanda Larissa de Araujo Pantoja** como contribuição para a comunidade de dados.


### Criar mapa coroplético do Estado de Santa Catarina em PowerBI
[mapa-coropletico-santa-catarina-powerbi.md](mapa-coropletico-santa-catarina-powerbi.md)


### Região Norte
* AC / Acre - [topojson/topojson-12-mun.json](topojson/topojson-12-mun.json)
* AM / Amazonas - [topojson/topojson-13-mun.json](topojson/topojson-13-mun.json)
* AP / Amapá - [topojson/topojson-16-mun.json](topojson/topojson-16-mun.json)
* PA / Pará  - [topojson/topojson-15-mun.json](topojson/topojson-15-mun.json)
* RO / Rondônia - [topojson/topojson-11-mun.json](topojson/topojson-11-mun.json)
* RR / Roraima - [topojson/topojson-14-mun.json](topojson/topojson-14-mun.json)
* TO / Tocantins - [topojson/topojson-17-mun.json](topojson/topojson-17-mun.json)

### Região Nordeste
* AL / Alagoas - [topojson/topojson-27-mun.json](topojson/topojson-27-mun.json)
* BA / Bahia - [topojson/topojson-29-mun.json](topojson/topojson-29-mun.json)
* CE / Ceará - [topojson/topojson-23-mun.json](topojson/topojson-23-mun.json)
* MA / Maranhão - [topojson/topojson-21-mun.json](topojson/topojson-21-mun.json)
* PB / Paraíba - [topojson/topojson-25-mun.json](topojson/topojson-25-mun.json)
* PE / Pernambuco - [topojson/topojson-26-mun.json](topojson/topojson-26-mun.json)
* PI / Piauí - [topojson/topojson-22-mun.json](topojson/topojson-22-mun.json)
* RN / Rio Grande do Norte - [topojson/topojson-24-mun.json](topojson/topojson-24-mun.json)
* SE / Sergipe - [topojson/topojson-28-mun.json](topojson/topojson-28-mun.json)

### Região Sudeste
* ES / Espírito Santo - [topojson/topojson-32-mun.json](topojson/topojson-32-mun.json)
* MG / Minas Gerais - [topojson/topojson-31-mun.json](topojson/topojson-31-mun.json)
* RJ / Rio de Janeiro - [topojson/topojson-33-mun.json](topojson/topojson-33-mun.json)
* SP / São Paulo - [topojson/topojson-35-mun.json](topojson/topojson-35-mun.json)

### Região Sul
* PR / Paraná - [topojson/topojson-41-mun.json](topojson/topojson-41-mun.json)
* RS / Rio Grande do Sul - [topojson/topojson-43-mun.json](topojson/topojson-43-mun.json)
* SC / Santa Catarina - [topojson/topojson-42-mun.json](topojson/topojson-42-mun.json)

### Região Centro-Oeste
* DF / Distrito Federal - [topojson/topojson-53-mun.json](topojson/topojson-53-mun.json) 
* GO / Goiás - [topojson/topojson-52-mun.json](topojson/topojson-52-mun.json)
* MT / Mato Grosso - [topojson/topojson-51-mun.json](topojson/topojson-51-mun.json)
* MS / Mato Grosso do Sul - [topojson/topojson-50-mun.json](topojson/topojson-50-mun.json)

---

### Como utilizar no Power BI

1. No Power BI Desktop, clique em **"Obter Dados" > "Arquivo JSON"**.
2. Selecione o arquivo `.topojson` desejado.
3. Configure a visualização de **mapa de formas personalizadas (Shape Map)**.
4. Relacione a coluna de código do município (`id` ou `description`, conforme estrutura do arquivo) com sua base de dados.

### Licença
Creative Commons [CC0 1.0 Universal](https://creativecommons.org/publicdomain/zero/1.0/)


### Palavras-chave
BR, Brasil, Brazil, mapa, map, mapas, maps, TopoJSON, geo, GIS, Power BI, coroplético, município
