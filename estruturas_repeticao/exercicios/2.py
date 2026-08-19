def contando():
    while True:
        num_1 = int(input('Digite o primeiro numero: '))
        num_2 = int(input('Digite o segundo numero: '))
        if num_1 <= 0 and num_2 <= 0:
            print ('numeros incontaveis')
            break
        else:
            for i in range(num_1, num_2):
                print(f'contando {i}')
            break


contando()