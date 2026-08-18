def classificacao_numero():
    numero = (int(input("digite seu valor")))

    if (numero>= 1):
        print('o seu numero é um numero positivo')
    elif numero == 0:
        print('O seu numero é 0, um numero neutro')
    elif numero  <= -1:
        print('O seu numero é um numero negativo')


    if numero % 2 == 0:
        print('Seu numero é um numero par')
    elif numero % 2 == 1:
        print('Seu numero é um numero impar')

classificacao_numero()