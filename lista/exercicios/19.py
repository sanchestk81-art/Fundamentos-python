def adicionar_nota(notas, nota):
    notas.append(nota)
    return notas


def inserir_nota(notas, nota, posicao):
    notas.insert(posicao, nota)
    return notas


def adicionar_varias(notas, novas_notas):
    notas.extend(novas_notas)
    return notas


def remover_nota(notas, nota):
    notas.remove(nota)
    return notas


def remover_ultima(notas):
    return notas.pop()


def encontrar_nota(notas, nota):
    return notas.index(nota)


def quantidade_notas(notas):
    return len(notas)


def ordenar_notas(notas):
    return sorted(notas)


def inverter_notas(notas):
    return list(reversed(notas))


def somar_notas(notas):
    return sum(notas)


def media_notas(notas):
    return sum(notas) / len(notas)


notas = [7.5, 6.0, 8.5, 9.0, 5.5]


print("1 - Adicionar:", adicionar_nota(notas, 8.0))

print("2 - Inserir:", inserir_nota(notas, 7.0, 2))

print("3 - Adicionar várias:", adicionar_varias(notas, [6.5, 9.5]))

print("4 - Remover:", remover_nota(notas, 6.0))

print("5 - Última nota removida:", remover_ultima(notas))

print("6 - Posição da nota:", encontrar_nota(notas, 8.5))

print("7 - Quantidade:", quantidade_notas(notas))

print("8 - Notas ordenadas:", ordenar_notas(notas))

print("9 - Ordem inversa:", inverter_notas(notas))

print("10 - Soma:", somar_notas(notas))

print("11 - Média:", media_notas(notas))

adicionar_nota(notas, 8.0)
media_notas(notas)