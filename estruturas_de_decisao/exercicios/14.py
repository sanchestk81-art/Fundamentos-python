def sistema_votacao():
    print('Olá, sejabem vindo ao sistema de votação')
    idade = int(input('Para indicarmos sua categoria diga: Qual a sua idade?'))
    if  idade <=16:
        print(f'Vejo que você tem menos de 16 anos, infelizmente você não pode votar')
    elif idade ==16 or idade ==17:
        print(f'vejo quie você tem {idade}, seu voto é opcional')
    elif idade ==18 or idade >=69:
        print(f'vejo que você tem {idade},você é obrigado a votar')
    elif idade <=70:
        print(f'Vejo que você tem {idade}, seu voto é opcional')

sistema_votacao()