def mostrar_numero_while():
    contador = 0
    while contador <= 10:
        contador += 1
        print(f'contagem atual: {contador}')

#mostrar_numero_while()
def contagem_regrassiva():
    valor_contagem = int(input('Digite um numero maior que 10:'))
    if valor_contagem < 10:
        print("valor invalido")
    else:
        while valor_contagem >= 1:
            print(f'contagem regressica: {valor_contagem}')
            valor_contagem -= 1
        print('Decolando!!')

#contagem_regrassiva()

def soma_com_while():
    while True:
        num_1 = int(input('Digite o primeiro valor: '))
        num_2 = int(input('Digite o segundo valor: '))

        if num_1 == 0:
            print('função da soma errada, esse numero não é valido')
            break
        else:
            soma= num_1 + num_2
            print(f'O resultadoda soma é {soma}')

#soma_com_while()