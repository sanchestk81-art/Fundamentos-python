def contar_pares(inicio, fim):
    pares = 0

    for numero in range(inicio, fim + 1):
        if numero % 2 == 0:
            pares = pares + 1

    return pares


print(contar_pares(1, 10))