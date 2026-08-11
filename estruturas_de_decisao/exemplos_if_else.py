def aluno_aprovado ():
    nota1 = float(input('Digite a primeira nota: '))
    nota2 = float(input('Digite a segunda nota: '))
    media = nota1 + nota2 / 2
    if media >= 6:
        print('Sua media foi aprovada')
    else:
        print('Sua media foi reprovada')

#aluno_aprovado()



def login ():
    email = "sanches@gmail.com"
    senha = "1234"
    codigo_secreto = "OscarP81"

    email_input = input('Digite o seu email: ')
    senha_input = input('Digite sua senha: ')

    if email_input == email and senha_input == senha:
        print("usuario logado!")
        acessar_adimin = input("deseja acessar area administrativa (digite sim ou não) ?")
        if acessar_adimin == "sim":
            codigo_secreto_input = input("Digite o seu codigo secreto: ")
            if codigo_secreto_input == codigo_secreto:
                print("acesso liberado!")
            else:
                print("codigo errado! Acesso negado! Voa piranha!")
        elif acessar_adimin == "não":
            print("Ok, usuário comum selecionado")
            print("Seja bem vindo!")
    else:
        print("senha ou email incorreto")

login()


