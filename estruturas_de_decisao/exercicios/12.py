def senha():
    senha = ("python123")
    digite = input('Seja bem vindo ao sistema, digite a senha para acessar: ')
    if digite == senha:
        print('Bem vindo usuário')
    else:
        print('Senha incorreta')
senha()