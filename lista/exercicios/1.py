def mostrar_nomes(nomes):
    for nome in nomes:
        print(f"O nome da lista é: {nome}")

lista_nomes = ["Oscar", "Kishan", "Bucky", "Lian"]
mostrar_nomes(lista_nomes)

#Adiocionando nomenovo na lista
def adcionar_nome(nomes, nome):
    nomes.append(nome)
    print(f'o nome adicionado foi: {nome}')

adcionar_nome(lista_nomes, "Steve")