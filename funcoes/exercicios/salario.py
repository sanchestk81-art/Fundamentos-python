def salario():
    valor_horas = float(input("Digite O valor das horas:"))
    horas_trabalhadas = int(input("digite quantas horas você trabalhou:"))
    total = valor_horas * horas_trabalhadas
    print(f"O seu salario é de R${total:.2f}")

salario()
