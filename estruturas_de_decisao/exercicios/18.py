def frete ():
    valor= int (input('Digite o valor da sua compra: '))

    if valor >= 100:
        print('seu frete é de R$20,00')
    elif valor <= 101 or valor >= 300:
        print('seu frete é de R$10,00')
    elif valor >= 100:
        print('Seu frete é grátis')
frete()