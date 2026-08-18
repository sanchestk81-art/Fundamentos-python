def desconto():
    compra = float(input("Digite o valor da compra para calcular o desconto: "))
    if compra <= 100:
        print('Infelizmente sua compra não tem nenhum desconto')
    elif compra >= 101 or compra <= 500:
        print('Sua compra tem o desconto de 10%')
        desconto10 = (compra * 10) / 100
        calcular = compra - desconto10
        print(f'Assim sua compra diminui para: {calcular}')
    elif compra <= 500:
        print('Sua compra ganha 15% de desconto')
        desconto15 = (compra * 15) / 100
        calcular = compra - desconto15
        print(f'Assim sua compra tem o valor de: {calcular}')
desconto()