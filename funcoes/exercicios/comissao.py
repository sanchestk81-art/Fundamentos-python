def comissao():
    salario = float(input("Digite o seu salario: "))
    vendas = float(input("Digite o valor de vendas: "))
    percentual = float(input("Digite o percentual de comissao: "))
    salario_final = salario + (salario * percentual)
    print(f"O seu salário final é {salario_final}")

comissao()