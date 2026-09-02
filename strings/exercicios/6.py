def contar_letra(frase, letra):
    return frase.count(letra)


frase = input("Digite uma frase: ")
letra = input("Digite uma letra: ")

print(contar_letra(frase, letra))
contar_letra(frase, letra)