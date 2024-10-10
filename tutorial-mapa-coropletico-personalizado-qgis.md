# Tutorial: Como criar um Mapa Coroplético Customizado de uma Pessoa

## Passos:

### 1. Copiar a Imagem
Primeiro, você precisará de uma imagem da pessoa que você deseja transformar em um mapa coroplético. A imagem pode ser uma foto de rosto ou qualquer parte do corpo que você deseja usar.

1. Encontre ou crie a imagem da pessoa.
2. Copie a imagem para seu computador em um formato compatível, como `.png` ou `.jpg`.

### 2. Abrir a Imagem no QGIS
Agora, vamos usar o **QGIS** (um software de sistema de informações geográficas) para transformar essa imagem em um mapa:

1. Abra o **QGIS**.
2. Vá até o menu **Camada** e selecione **Adicionar Camada** > **Adicionar Camada de Raster**.
3. Navegue até a imagem que você copiou e selecione-a. Clique em **Abrir**.
4. A imagem agora aparecerá no QGIS como uma camada raster.

### 3. Desenhar as Áreas no Mapa
Você precisa desenhar as regiões ou formas de interesse na imagem para criar polígonos que serão usados no mapa coroplético.

1. No menu de **Camadas**, crie uma nova camada vetorial para desenhar suas áreas:
   - Vá até **Camada** > **Criar Camada** > **Nova Camada de Feições**.
   - Escolha **Polígono** como tipo de geometria.
   - Adicione os campos que você deseja, como **Nome** ou **ID**.
   - Clique em **OK** para criar a nova camada.
2. Com a nova camada selecionada, clique em **Alternar Edição** na barra de ferramentas.
3. Use a ferramenta de desenho de polígonos (**Desenhar Polígono**) para traçar áreas específicas sobre a imagem. Cada área desenhada será uma feição única no mapa.
4. Nomeie as regiões ou áreas ao preencher os atributos após desenhar cada polígono.
5. Quando terminar de desenhar as áreas, clique em **Salvar Edições** e **Alternar Edição** para finalizar o desenho.

### 4. Exportar para SHP (Shapefile)
Agora que você desenhou os polígonos que representam as regiões da imagem, você precisará exportá-los como um Shapefile (`.shp`).

1. No painel de **Camadas**, clique com o botão direito na camada de polígonos criada.
2. Selecione **Exportar** > **Salvar Feições Como...**.
3. Escolha o formato **ESRI Shapefile** (`.shp`).
4. Nomeie o arquivo e escolha o local onde deseja salvá-lo.
5. Certifique-se de que o sistema de coordenadas (CRS) esteja correto. O padrão geralmente é **WGS 84**.
6. Clique em **OK** para exportar.

### 5. Converter o SHP para TopoJSON usando MapShaper
Agora, precisamos converter o Shapefile para o formato **TopoJSON**, que é o formato preferido para usar em ferramentas de visualização web, como Power BI ou outras plataformas de mapeamento.

1. Vá até o site [MapShaper](https://mapshaper.org/).
2. Clique em **Upload** e carregue o Shapefile exportado do QGIS. Você precisa carregar todos os arquivos relacionados ao SHP (`.shp`, `.shx`, `.dbf`, etc.).
3. Após carregar o Shapefile, você verá o mapa no MapShaper.
4. Clique em **Export** na parte superior.
5. No menu de exportação, escolha **TopoJSON** como o formato de exportação.
6. Clique em **Export** para baixar o arquivo **TopoJSON**.

### 6. Usar o TopoJSON em um Mapa Coroplético
Agora que você tem o arquivo TopoJSON, você pode usá-lo em ferramentas de visualização como Power BI ou D3.js para criar um mapa coroplético.

1. Abra o **Power BI** (ou outra ferramenta de sua escolha).
2. Carregue o arquivo TopoJSON na visualização de mapa.
3. Vincule os dados que você deseja visualizar, como valores numéricos ou categorias para as áreas desenhadas.

---

## Resumo:
- Copiar a imagem da pessoa.
- Abrir a imagem no QGIS como uma camada raster.
- Criar uma nova camada vetorial para desenhar as regiões de interesse.
- Desenhar os polígonos nas áreas desejadas.
- Exportar os polígonos como Shapefile (`.shp`).
- Converter o arquivo SHP para TopoJSON usando o [MapShaper](https://mapshaper.org/).
- Usar o arquivo TopoJSON em uma ferramenta de visualização para criar um mapa coroplético.

Agora você pode criar um mapa coroplético personalizado de uma pessoa, visualizando os dados sobre as áreas que você desenhou.
