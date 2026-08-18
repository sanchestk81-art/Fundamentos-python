def caixa_eletronico():
    saldo_disponivel = int(input('Qual o seu saldo?'))
    sacar = int(input('Quanto você quer sacar?'))

    if saldo_disponivel <= sacar:
        print('Seu saldo é insuficiente')
    elif saldo_disponivel >= sacar:
        print('saque realizado')
        total = (saldo_disponivel - sacar)
        print('seu saldodisponivel agora é de {total}')
caixa_eletronico()
    
