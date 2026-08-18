def maior_menor():
    numero1 = int(input("Digite um valor: "))
    numero2 = int(input("Digite outro valor: "))
    if numero1 > numero2:
        print('O primeiro valor é maior que o outro')
    elif numero1 == numero2:
        print('Os dois numeros são iguais')
    else:
        print('o segundo valor é maior que o primeiro')

maior_menor()