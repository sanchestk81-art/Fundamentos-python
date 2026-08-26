def adicionar_nota(notas, nota):
    notas.append(nota)
    return notas


def remover_nota(notas, nota):
    notas.remove(nota)
    return notas


def media_notas(notas):
    media = sum(notas) / len(notas)
    return media


notas = [7, 8, 9]

print(adicionar_nota(notas, 10))

print(remover_nota(notas, 8))

print("Média:", media_notas(notas))

adicionar_nota(notas, 10)
remover_nota(notas, 8)
media_notas()