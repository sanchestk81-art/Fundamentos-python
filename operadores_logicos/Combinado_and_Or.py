#operador and r or
def show ():
    POSSUI_INGRESSO = True
    idade = int(input("Qual a sua idade?"))
    nome_esta_na_lista = bool(input("Seu nome está na lista?"))


    posso_entrar = idade >= 18 and (nome_esta_na_lista or POSSUI_INGRESSO)
    print(f"VOu conseguir entrar no show?{posso_entrar}")

show()