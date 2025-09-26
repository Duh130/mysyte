# blog/utils.py
import chardet


def ler_arquivo_seguro(caminho_arquivo):
    with open(caminho_arquivo, "rb") as f:
        raw_data = f.read()
        resultado = chardet.detect(raw_data)
        encoding = resultado['encoding']

    with open(caminho_arquivo, "r", encoding=encoding) as f:
        conteudo = f.read()

    return conteudo
