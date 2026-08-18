def temperatura():
    temperatura = int(input("Digite a temperatura em celcius: "))
    if temperatura <= 15:
        print('Frio')
    elif temperatura == 15 or temperatura <= 25:
        print('Agradável')
    elif temperatura >= 25:
        print('Quente')
temperatura()