def adicionar_convidados(convidados, novos_convidados):
    convidados.extend(novos_convidados)
    return convidados


lista = ["Ana", "Carlos"]
novos = ["João", "Maria", "Pedro"]

print(adicionar_convidados(lista, novos))
adicionar_convidados(lista, novos)
