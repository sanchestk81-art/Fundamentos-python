# converter texto para maiuscula e minusculas
def formatar_nome(nome):
    #nome maiusculo
    nome_maiusculo = nome.upper() # função interna que recebe o texto e transforma ele em letras maiusculas
   # nome minusculo
    nome_minusculo = nome.lower() # função que recebe o texto e diminui as letras

    #nome com a primeira letra maiuscula
    nome_camel_case = nome.capitalize()

    return (nome_maiusculo, nome_minusculo, nome_camel_case)
#nome = input('Digite o nome do aluno: ')
#print (formatar_nome(nome)[1])

#banana, batata, cebola + formatar_nome(nome)
#print (f"nome maiusculo: {banana}")
#print(f'nome minusculo: {batata}')
#print(f'nome Camel Case: {cebola}')

#remover espaços desnecessários
def limpar_texto(texto):
    #remove os espaços no final e no inicio do
    texto_limpo = texto.strip()
    #remove espaços da esquerda .lstrip
    #remove os espaços da direia .rstrip
    return texto_limpo

texto1 = '  SOS     '
print(f' texto antes: {texto1}')
print (f" texto depois:{limpar_texto(texto1)}")

#substituir palavras
def trocar_cidade(texto):
    texto_trocado = texto.replace('Sao paulo', 'Piracicaba')

    return texto_trocado
cidade = 'Eu moro em Sao paulo'
print(trocar_cidade(cidade))

#contar caracteres ou ocorrencias
def analizar_texto(texto):
    caracter = len(texto)
    quantidade_letras = texto.lower().count('a')

    return quantidade_letras, caracter

texto2 = input('digite uma frase')
letra = input('digite uma letras')
caracter,letra = analizar_texto(texto2, letra)

print(f'total de caracteres: {caracter}')
print(f'total de letras: {letra}')

#verificar se uma palavra está presente
def verificar_palavra(frase, palavra):
    palavra_presente = palavra.lower() in frase.lower()
    # Retorna um booleano(true ou false)
    return palavra_presente

frase = input('digite uma frase')
palavra = input('digite uma palavra')
print(f'A palavra está presente na frase? {verificar_palavra(frase, palavra)}')

#encontrar a posição de uma palavra
def encontrar_posicao(frase, palavra):
    posicao_palavra = frase.lower().find(palavra.lower)
    return posicao_palavra
frase2 = input('digite uma frase')
palavra2 = input('digite uma palavra')
print(f' A posição da palavra é {encontrar_posicao(frase2, palavra2)}')

