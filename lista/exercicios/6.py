def encontrar_produto(produtos, produto):
    posicao = produtos.index(produto)
    return posicao


lista = ["Arroz", "Feijão", "Macarrão"]

print(encontrar_produto(lista, "Feijão"))

encontrar_produto(lista, "Arroz")