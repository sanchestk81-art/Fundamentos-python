from ctypes.macholib.dyld import DEFAULT_LIBRARY_FALLBACK


def ingresso():
    print('Bem vindo ao cinema!')
    idade = int (input("Para comerçar a compra, digite sua idade para vermos quanto vai custar seu ingresso"))
    if idade <=5:
        print(f"vejo que você tem {idade} anos, seu ingresso é gratuito")
        print('Obrigado por usar o cinema, até a proxima')
    elif idade >=6 and idade <=12:
        print(f'vejo que você tem {idade}, seu ingresso é de R$ 10,00')
        print('Obrigado por usar o cinema, até a proxima')
    elif idade >=13 and idade <=59:
        print(f'vejo que você tem {idade}, o ingresso tem o valor de R$ 20,00')
        print('Obrigado por usar o cinema, até a proxima')
    elif idade >=60:
        print(f'vejo que você tem {idade}, o seu ingresso é gratuito')
        print('Obrigado por usar o cinema, até a proxima')
ingresso()
