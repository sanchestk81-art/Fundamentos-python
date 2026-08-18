def classificacao_velocidade():
    velocidade = int(input('Qual a sua velocidade?'))
    if velocidade >= 60:
        print('velocidade permitida')
    elif velocidade <=61 or velocidade >=80:
        print('atenção velocidade acima do permitido')
    elif velocidade <=80:
        print('multa por excesso de velocidade')
classificacao_velocidade()