# 🗺️ Tutorial: Como Criar um Mapa Coroplético Personalizado a Partir de uma Imagem

Este guia ensina a transformar uma imagem personalizada (por exemplo, uma silhueta ou forma artística) em um **mapa coroplético interativo**, pronto para uso no **Power BI** ou outras ferramentas de visualização.

---

## 🔹 Etapa 1: Criar e Preparar a Imagem

1. Crie ou desenhe a forma desejada (por exemplo, o contorno de uma pessoa, objeto ou logotipo).  
2. Garanta que o desenho **não contenha linhas sobrepostas ou intersecções**, para evitar erros de vetorização.  
3. Exporte o resultado final em formato **PNG** com fundo transparente.

---

## 🔹 Etapa 2: Converter PNG para DXF

1. Acesse o site [https://convertio.co/png-dxf/](https://convertio.co/png-dxf/).  
2. Envie o arquivo PNG criado anteriormente.  
3. Faça a conversão e baixe o arquivo **DXF** (formato vetorial compatível com CAD e QGIS).  

💡 **Dica:** quanto maior a resolução da imagem original, melhor será a precisão das bordas na conversão vetorial.

---

## 🔹 Etapa 3: Importar e Configurar no QGIS

1. Abra o **QGIS**.  
2. Vá em **Camada → Adicionar Camada → Adicionar Camada Vetorial**.  
3. Selecione o arquivo **DXF** convertido.  
4. Verifique se as formas aparecem corretamente no mapa.  
5. Se necessário, use a ferramenta **Editar Geometrias** para corrigir pequenas imperfeições (como linhas abertas).

---

## 🔹 Etapa 4: Adicionar Atributos

1. Crie uma nova camada vetorial a partir do DXF, se desejar editar e salvar em formato próprio do QGIS.  
2. Adicione campos de atributos como:
   - `ID` (identificador numérico)
   - `Nome` (nome da área ou parte do desenho)
   - `Valor` (variável que será visualizada no mapa coroplético)  
3. Preencha esses campos manualmente ou importe de uma planilha CSV.

---

## 🔹 Etapa 5: Exportar para Shapefile

1. Clique com o botão direito na camada vetorial.  
2. Escolha **Exportar → Salvar Feições Como...**.  
3. Selecione o formato **ESRI Shapefile (.shp)**.  
4. Defina o local de salvamento e confirme o sistema de coordenadas (ex: **WGS 84**).  
5. Clique em **OK** para gerar o arquivo SHP.

---

## 🔹 Etapa 6: Converter para TopoJSON

1. Vá até o site [MapShaper.org](https://mapshaper.org/).  
2. Faça o upload de todos os arquivos do Shapefile (`.shp`, `.shx`, `.dbf`, etc.).  
3. Visualize o mapa e verifique se está correto.  
4. Clique em **Export** → selecione **TopoJSON**.  
5. Baixe o arquivo final.

---

## 🔹 Etapa 7: Importar no Power BI

1. Abra o **Power BI Desktop**.  
2. Adicione um **visual de mapa personalizado** (como o “Shape Map” ou “Mapbox”).  
3. Carregue o arquivo **TopoJSON** exportado do MapShaper.  
4. Relacione os campos de **ID** ou **Nome** da camada aos seus dados.  
5. Configure as cores e legendas para criar seu **mapa coroplético personalizado**.

---

## ✅ Resumo Final

| Etapa | Ação | Ferramenta |
|-------|------|-------------|
| 1 | Criar imagem sem intersecções e exportar em PNG | Editor de imagem |
| 2 | Converter PNG → DXF | [Convertio](https://convertio.co/png-dxf/) |
| 3 | Importar e ajustar | QGIS |
| 4 | Definir atributos | QGIS |
| 5 | Exportar como Shapefile | QGIS |
| 6 | Converter SHP → TopoJSON | [MapShaper.org](https://mapshaper.org/) |
| 7 | Visualizar o mapa | Power BI |

---

✨ Agora você possui um **mapa coroplético totalmente personalizado**, criado a partir de qualquer imagem vetorizável e pronto para análise visual no Power BI!

