def prestacao():
    valor = int(input('Digite o valor: '))
    parcelas = int(input('Digite o numero de parcelas: '))
    calculo = valor / parcelas
    print(f'o valor de cada parcela é de {calculo}')

prestacao()
