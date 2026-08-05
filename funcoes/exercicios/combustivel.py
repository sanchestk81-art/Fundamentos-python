def combustivel():
    distancia = float(input("Digite a distancia percorrida:"))
    combustivel = float(input("Digite o valor do combustivel:"))
    consumo = distancia / combustivel
    print(f"O seu consumo é de: {consumo}")

combustivel()