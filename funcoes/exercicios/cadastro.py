
def cadastro():
    print('=========================Cadastro==============================')
    nome = input('Digite seu nome: ')
    idade = int(input('Digite sua idade: '))
    profissao = input('Digite seu profissao: ')
    cidade = input('Digite sua cidade: ')

    print(f'Olá {nome} você tem {idade} anos. A sua profissão é {profissao} você mora em {cidade}.')
    print(f'==========================================================================')

cadastro()
