def adicionar_produtos(compras, produtos):
    compras.extend(produtos)
    return compras
adicionar_produtos(compras, produtos)


def cancelar_compra(compras, produto):
    compras.remove(produto)
    return compras


compras = ["Arroz", "Feijão"]

produtos = ["Macarrão", "Leite", "Pão"]

print(adicionar_produtos(compras, produtos))

print(cancelar_compra(compras, "Leite"))
cancelar_compra(compras, produtos)