def remover_produto(produtos, produto):
    produtos.remove(produto)
    return produtos


lista = ["Arroz", "Feijão", "Macarrão"]

print(remover_produto(lista, "Feijão"))

remover_produto(lista, "Arroz")