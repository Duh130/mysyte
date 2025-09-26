try:
    with open("teste.txt", "r", encoding="utf-16") as f:
        conteudo = f.read()
    print("Arquivo lido com sucesso!")
    print("Primeiras linhas do arquivo:")
    print(conteudo[:200])
except Exception as e:
    print("Erro ao ler o arquivo:", e)
