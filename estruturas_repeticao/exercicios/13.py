def mostrar_primos(inicio, fim):
    for numero in range(inicio, fim + 1):
        if numero < 2:
            continue

        primo = True

        for i in range(2, numero):
            if numero % i == 0:
                primo = False

        if primo:
            print(numero)


mostrar_primos(1, 20)