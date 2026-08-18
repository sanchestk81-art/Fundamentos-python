def IMC():
    altura = float (input('Qual a sua altura?'))
    peso = float(input('Qual o seu peso?'))
    IMC = peso / (altura * altura)

    if IMC < 18.5:
        print('você está abaixo do peso, procure um médico')
    elif IMC ==18.5 or IMC <= 24,9:
        print('Seu peso está normal, continue assim')
    elif IMC = 25 or IMC = 29.9:
        print('Você está com sobrepeso, procure um médico')
    elif IMC > 30:
        print('Voce está com obesidade, procure um médico')


IMC ()
