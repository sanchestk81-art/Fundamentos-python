def caixa_eletronico(valor):
    notas = [100, 50, 20, 10, 5, 2]

    for nota in notas:
        quantidade = 0

        while valor >= nota:
            valor = valor - nota
            quantidade = quantidade + 1

        if quantidade > 0:
            print(quantidade, "nota(s) de", nota)


caixa_eletronico(187)