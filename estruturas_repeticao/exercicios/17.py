
def jogo_adivinhacao(numero_secreto):
    palpite = 0

    while palpite != numero_secreto:
        palpite = int(input("Digite um palpite: "))

        if palpite < numero_secreto:
            print("O número é maior!")

        elif palpite > numero_secreto:
            print("O número é menor!")

        else:
            print("Você acertou!")


jogo_adivinhacao(10)