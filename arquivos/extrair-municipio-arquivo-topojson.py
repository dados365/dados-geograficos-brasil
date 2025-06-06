import os
import json
import csv

PASTA_TOPOJSON = "./topojson"  # ajuste conforme necessário

uf_para_estado = {
    "11": "Rondônia", "12": "Acre", "13": "Amazonas", "14": "Roraima", "15": "Pará",
    "16": "Amapá", "17": "Tocantins", "21": "Maranhão", "22": "Piauí", "23": "Ceará",
    "24": "Rio Grande do Norte", "25": "Paraíba", "26": "Pernambuco", "27": "Alagoas",
    "28": "Sergipe", "29": "Bahia", "31": "Minas Gerais", "32": "Espírito Santo",
    "33": "Rio de Janeiro", "35": "São Paulo", "41": "Paraná", "42": "Santa Catarina",
    "43": "Rio Grande do Sul", "50": "Mato Grosso do Sul", "51": "Mato Grosso",
    "52": "Goiás", "53": "Distrito Federal"
}

dados = []

for nome_arquivo in sorted(os.listdir(PASTA_TOPOJSON)):
    if nome_arquivo.endswith("-mun.json"):
        print(f"Lendo: {nome_arquivo}...")
        cod_uf = nome_arquivo.split("-")[1]
        estado = uf_para_estado.get(cod_uf, "Desconhecido")
        caminho_arquivo = os.path.join(PASTA_TOPOJSON, nome_arquivo)

        try:
            with open(caminho_arquivo, encoding="utf-8") as f:
                conteudo = json.load(f)

            objetos = conteudo.get("objects", {})
            if not objetos:
                print(f"[!] Nenhum objeto encontrado em {nome_arquivo}")
                continue

            nome_objeto = next(iter(objetos))
            geometries = objetos[nome_objeto].get("geometries", [])

            if not geometries:
                print(f"[!] Nenhuma geometria encontrada em {nome_arquivo}")
                continue

            for feature in geometries:
                props = feature.get("properties", {})
                dados.append({
                    "id": props.get("id"),
                    "name": props.get("name"),
                    "description": props.get("description"),
                    "estado": estado
                })
        except Exception as e:
            print(f"[ERRO] Falha ao processar {nome_arquivo}: {e}")

# Exportar para CSV
with open("municipios.csv", "w", newline="", encoding="utf-8") as csvfile:
    campos = ["id", "name", "description", "estado"]
    writer = csv.DictWriter(csvfile, fieldnames=campos)
    writer.writeheader()
    writer.writerows(dados)

print(f"\n✅ {len(dados)} municípios salvos em municipios.csv")
