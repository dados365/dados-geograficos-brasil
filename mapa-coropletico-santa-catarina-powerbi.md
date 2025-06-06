# Instruções para Criar um Mapa Coroplético Personalizado do Estado de Santa Catarina no Power BI

Estas instruções explicam como criar um mapa coroplético personalizado para o estado de Santa Catarina utilizando um arquivo TopoJSON no Power BI.

## Requisitos:
- Power BI Desktop instalado.
- Arquivo de mapa no formato **TopoJSON** do estado de Santa Catarina.

 * **SC / Santa Catarina** - [topojson-42-mun.json](topojson/topojson-42-mun.json)


  - Se o mapa estiver em GeoJSON ou Shapefile, você pode convertê-lo usando a ferramenta **Map Shaper**.
  - O formato do arquivo está no formato **GeoJSON**:
    * **SC / Santa Catarina** - [geojson/geojs-42-mun.json](geojson/geojs-42-mun.json)





## Passos:

### 1. Obter o Arquivo de Mapa no Formato TopoJSON
1.1. Se o arquivo de mapa de Santa Catarina estiver em um formato diferente (GeoJSON ou Shapefile):
  - Acesse o site [Map Shaper](https://mapshaper.org/).
  - Faça upload do seu arquivo GeoJSON ou Shapefile.
  - Selecione **Exportar** e escolha **TopoJSON** como o formato de saída.
  - Baixe o arquivo TopoJSON.

### 2. Adicionar o Visual do Mapa de Formas no Power BI
2.1. Abra o Power BI Desktop.

2.2. No painel **Visualizações**, clique no ícone do **Mapa de Formas** (Shape Map).

2.3. Insira os dados que deseja exibir no mapa (ex.: municípios de Santa Catarina e seus valores).

### 3. Carregar o Mapa Personalizado
3.1. Com o visual do **Mapa de Formas** selecionado, vá para o **Painel de Formatação** (ícone de rolo de pintura).

3.2. Expanda a seção **Configurações de Mapa**.

3.3. Na opção **Mapa Personalizado**, selecione **Adicionar um Tipo de Mapa**.

3.4. Carregue o arquivo TopoJSON do estado de Santa Catarina.

### 4. Vincular os Dados ao Mapa
4.1. Após carregar o TopoJSON, verifique se os dados estão mapeados corretamente.

4.2. No campo **Local**, selecione a coluna com nomes ou códigos geográficos correspondentes às regiões no arquivo TopoJSON.

4.3. No campo **Valores**, adicione os dados que deseja visualizar no mapa.

### 5. Configurar Escala de Cores
5.1. No **Painel de Formatação**, vá até a seção **Cores dos Dados**.

5.2. Ajuste a escala de cores, definindo cores mais claras para valores baixos e cores mais escuras para valores altos.

### 6. Adicionar a Legenda
6.1. Expanda a seção **Legenda** no **Painel de Formatação**.

6.2. Ative a legenda e configure a posição e o título.

### 7. Publicar ou Salvar o Relatório
7.1. Salve o relatório no Power BI Desktop ou publique no Power BI Service para compartilhamento.

## Observações:
- Certifique-se de que as regiões no arquivo TopoJSON estejam vinculadas corretamente aos seus dados.
- Utilize ferramentas de mapeamento para corrigir possíveis problemas de compatibilidade no arquivo TopoJSON.

## Fonte:
[Power BI Shape Map Documentation](https://learn.microsoft.com/pt-br/power-bi/visuals/desktop-shape-map)

