def numeros_positivos():
    digite = float(input("Digite um numero: "))
    if digite >= 1:
        print('o seu numero é um numero positivo')
    elif digite == 0:
        print('O seu numero é 0, um numero neutro')
    elif digite  <= -1:
        print('O seu numero é um numero negativo')

numeros_positivos()