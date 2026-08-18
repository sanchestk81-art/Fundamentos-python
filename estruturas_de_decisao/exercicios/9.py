def calculadora():
    numero1 = int(input("Digite o primeiro numero: "))
    numero2 = int(input("Digite o segundo numero: "))
    operador = int(input("Digite 1 para soma, 2 para subtração, 3 para multiplicação ou 4 para divisão"))
    calcular = 0

    if operador == 1:
        calcular = numero1 + numero2
        print(f'O resultado da sua conta é {calcular}')
    elif operador == 2:
        calcular = numero1 - numero2
        print(f'O resultado da sua conta é{calcular}')
    elif operador == 3:
        calcular = numero1 * numero2
        print(f'O resultado da sua conta é{calcular}')
    elif operador == 4:
        calcular = numero1 / numero2
        print(f'O resultado da sua conta é{calcular}')
calculadora()