def classificação():
    nota = int(input("Digite uma nota para avaliação: "))
    if nota >= 0 or nota == 4 :
        print("Insuficiente")
    if nota == 5 or nota == 6:
        print("Regular")
    if nota == 7 or nota == 8:
        print("bom")
    if nota == 9 or nota == 10:
        print("execelente")
classificação()
