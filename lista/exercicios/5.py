def remover_item(itens, posicao):
    removido = itens.pop(posicao)
    return removido


lista = ["Lápis", "Caneta", "Borracha"]

print(remover_item(lista, 1))

remover_item()