import random
import os


def print_date(dia, mes, ano):
    print(dia, mes, ano, sep="/")


def print_type(var, var_name):
    print('The', var_name, "is a type of:", type(var))


def frio_ou_quente(numero_correto, chute):
    value = abs(chute - numero_correto)
    if value <= 3: return "MUITO QUENTE"
    if 3 < value <= 8: return "QUENTE!"
    if 8 < value <= 15: return "MORNO!"
    if 15 < value <= 25: return "FRIO!"
    if value > 25: return "MUITO FRIO!"


def calcular_pontos(diferenca, tentativa):
    return int((1000/ diferenca)/tentativa)


def jogo_adivinhacao():
    print("Bem vindo ao jogo de Adivinhação!")
    max_numero = 50
    numero_secreto = random.randint(1, max_numero)
    pontos = 0
    tentativa = 1;
    # print(numero_secreto)

    while True:

        try:
            chute = int(input("Digite seu numero de 1 a " + str(max_numero) + ": "))
        except ValueError:
            print("Voce digitou algo que não é um numero, tente novamente...")
            continue
        if chute > max_numero:
            print("Voce digitou um numero maior que o limite da adivinhação!")
            continue
        if numero_secreto == chute:
            print("Voce acertou! O número secreto é: ", numero_secreto)
            if tentativa == 0:
                print("Voce fez a pontuação máxima ao acertar de primeira! PARABENS...")
            else:
                print("Você fez", int((pontos/tentativa) * 100), "pontos em", tentativa, "tentativas no jogo...")
            print("Fim de jogo !")
            restart = input("Deseja reiniciar o jogo? Digite S para reiniciar: ")
            if restart.upper() == "S": return True
            else: return False

        else:
            print("Voce não adivinhou o número!")
            print("DICA: Seu chute está", frio_ou_quente(numero_secreto, chute), '\n')
            tentativa = tentativa + 1
            pontos = pontos + calcular_pontos(abs(chute - numero_secreto), tentativa)
            print("pontuacao da rodada:", calcular_pontos(abs(chute - numero_secreto), tentativa))
            print(tentativa, ":", pontos)



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    comecar_novamente = jogo_adivinhacao()
    while comecar_novamente:
        print('\n\n')
        comecar_novamente = jogo_adivinhacao()
