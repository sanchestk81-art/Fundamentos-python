def calcular_media():
    soma = 0
    quantidade = 0

    numero = int(input("Digite um número (0 para parar): "))

    while numero != 0:
        soma = soma + numero
        quantidade = quantidade + 1

        numero = int(input("Digite um número (0 para parar): "))

    media = soma / quantidade

    print("A média é:", media)


calcular_media()