def pares():
    while True:
        numero = int(input('Digite o primeiro numero: '))

        for numero in range(1, numero + 1):
            if numero % 2 == 0:
                print(f'Seus numeros pares {numero}')

pares()