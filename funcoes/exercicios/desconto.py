def desconto():
    produto = float(input("Digite o valor do produto:"))
    desconto = int(input("Digite a porcentagem de desconto:"))
    calculo = produto - (produto * desconto/100)
    print(f"O seu desconto é de: {calculo}")

desconto()