def login():
    email = "seuemail@gmail.com"
    senha = "1234"

    print('Seja bem vindo!')
    login = input('digite seu email:')
    password = input('digite sua senha:')

    if login == email and password == senha:
        print("login ok")
    else:
        print("login errado")

login()