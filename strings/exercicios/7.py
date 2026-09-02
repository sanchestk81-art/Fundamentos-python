def procurar_palavra(frase, palavra):
    return palavra.find(palavra)

frase = input('digite uma frase: ')
palavra = input('digite uma palavra a ser encontrada: ')
print(f"A palavra está na posição: {palavra.find(palavra)}")
procurar_palavra(palavra)
