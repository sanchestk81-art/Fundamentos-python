def adicionar_cliente(fila, cliente):
    fila.append(cliente)

adicionar_cliente(fila, cliente)


def atender_cliente(fila):
    cliente = fila.pop(0)
    return cliente


fila = []

continuar = "s"

while continuar == "s":
    cliente = input("Digite o nome do cliente: ")
    adicionar_cliente(fila, cliente)

    continuar = input("Deseja adicionar outro cliente? (s/n): ")


print("\nFila:", fila)

while len(fila) > 0:
    print("Cliente atendido:", atender_cliente(fila))
atender_cliente(fila)