def validar_senha(senha_correta):
    tentativas = 0

    while tentativas < 3:
        senha = input("Digite a senha: ")

        if senha == senha_correta:
            print("Acesso permitido")
            return

        tentativas = tentativas + 1

    print("Acesso bloqueado")


validar_senha("1234")