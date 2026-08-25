def contagem_regressiva(numero):
    while numero >= 0:
        print(numero)
        numero = numero - 1


numero = int(input("Digite um número: "))

contagem_regressiva(numero)