#Operador OR

def posso_comprar():
    TEM_CARTAO= False
    tem_dinheiro = bool(input(f'Você tem tem dinheiro para comprar?'))
    atorizado = tem_dinheiro or TEM_CARTAO

    print (f'Vou comer um MC donalds hoje? {atorizado}')

posso_comprar()