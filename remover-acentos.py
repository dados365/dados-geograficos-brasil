import os
import sys
import json
import unicodedata

def remover_acentos(texto):
    return ''.join(
        c for c in unicodedata.normalize('NFKD', texto)
        if not unicodedata.combining(c)
    )

def remover_acentos_description(obj):
    if isinstance(obj, dict):
        for chave in obj:
            if chave == "description" and isinstance(obj[chave], str):
                obj[chave] = remover_acentos(obj[chave])
            else:
                remover_acentos_description(obj[chave])
    elif isinstance(obj, list):
        for item in obj:
            remover_acentos_description(item)

def processar_arquivos(diretorio, extensao):
    for raiz, _, arquivos in os.walk(diretorio):
        for nome_arquivo in arquivos:
            if nome_arquivo.endswith(extensao):
                caminho_arquivo = os.path.join(raiz, nome_arquivo)
                try:
                    with open(caminho_arquivo, 'r', encoding='utf-8') as f:
                        dados = json.load(f)

                    remover_acentos_description(dados)

                    with open(caminho_arquivo, 'w', encoding='utf-8') as f:
                        json.dump(dados, f, ensure_ascii=False, indent=2)

                    print(f"Acentos removidos em: {caminho_arquivo}")
                except Exception as e:
                    print(f"Erro ao processar {caminho_arquivo}: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Uso: python remove_acentos_topojson.py <diretorio> <extensao>")
        print("Remove acentos do campo 'description' - para remover acentos de outros locais há a necessidade de ajustes")
        print("Exemplo: python remove_acentos_topojson.py ./dados .json")
        sys.exit(1)

    diretorio_alvo = sys.argv[1]
    extensao_alvo = sys.argv[2]

    if not extensao_alvo.startswith("."):
        extensao_alvo = "." + extensao_alvo

    processar_arquivos(diretorio_alvo, extensao_alvo)
