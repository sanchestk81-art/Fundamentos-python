#operador and
from operator import truediv


def pode_difrigir():
    idade = int(input('Digite sua idade: '))
    TEM_HABILITACAO = True

    atorizado = idade >=18 and TEM_HABILITACAO

    print(f'Usuário pode dirigir? {atorizado}')

pode_difrigir()


