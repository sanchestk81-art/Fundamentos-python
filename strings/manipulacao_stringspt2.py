#dividir uma string em partes
import urllib


def separar_nome(nome_completo):
    partes = nome_completo.split(' ')
    return partes

nome_completo = input('digite seu nome completo: ')
print(f'nome em partes: {separar_nome(nome_completo)}')

#juntar strings
def criar_nome_completo(partes):
    nome_completo = ''.join(partes)
    return nome_completo

partes_nome = ["Theodoro", "Pozenato", "Sanches"]
print(f'A junção das partes do nome é: {criar_nome_completo(partes_nome)}')

#verificar o inicio e o final de uma string
def analisar_url(url):
    com_https = url.startswith('https://')
    termina_com_br = url.startswith('http://')
    return com_https, termina_com_br
url = input('digite um link para analisar: ')
tem_https, termina_com_br = analisar_url(url)
print(f'utiliza https? {tem_https}')
print(f'utiliza br? {termina_com_br}')

#verificar se a string contem somente numeros
def validade_idade(idade):
    idade_validar = idade.isdigit()
    if idade_validar:
        print(f'O valor digitado é uma idade valida:')
    else:
        print('digite somente numeros!')

idade= input('digite sua idade: ')
validade_idade(idade)

#verificar se a string contem somente letras
def validade_nome(nome):
    nome_valido= nome.isalpha()
    if nome_valido:
        print("O nome digitado é valido")
    else:
        print('O nome deve conter apenas letras!')

nome = input('digite seu nome: ')
validade_nome(nome)