def triangulo():
    primeiro = int(input('Primeiro valor: '))
    segundo = int(input('Segundo valor: '))
    terceiro = int(input('Terceiro valor: '))

    if primeiro == segundo == terceiro:
        print('seu triangulo é um equilatero')
    elif primeiro == segundo != terceiro:
        print('Seu triangulo é um isóceles')
    elif primeiro != segundo != terceiro:
        print('Seu triangulo é um escaleno')
triangulo()