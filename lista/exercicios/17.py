def vender_produto(estoque, produto):
    if produto in estoque:
        estoque.remove(produto)
        print("Produto vendido!")
    else:
        print("Produto não está disponível.")

    return estoque


estoque = ["Mouse", "Teclado", "Monitor", "Webcam"]

estoque = vender_produto(estoque, "Mouse")

print(estoque)

vender_produto()