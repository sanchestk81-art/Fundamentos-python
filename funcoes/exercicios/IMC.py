def IMC ():
    peso = float(input("Qual o seu peso?"))
    altura = float(input("Qual a sua altura?"))
    calculo = peso / (altura * altura)
    print(f'O seu IMC é de {calculo}')

IMC()