def faixa_etaria():
    idade = int(input("Digite sua idade: "))
    if idade == 0 or idade <= 12:
        print('criança')
    elif idade == 13 or idade <= 17:
        print('adolecente')
    elif idade == 18 or idade <= 59:
        print('adulto')
    elif idade >= 60:
        print('idoso')
faixa_etaria()