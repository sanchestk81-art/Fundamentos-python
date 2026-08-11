def energia():
    kWh = int(input('Digite o valor por kWh: '))
    preco = int(input('digite o valor do kWh:'))
    calculo = kWh * preco
    print(f'O valor da conta é de R${calculo:.2f}')

energia()