import random

def print_date(dia, mes, ano):
    print(dia, mes, ano, sep="/")


def print_type(var, var_name):
    print('The', var_name, "is a type of:", type(var))


def frio_ou_quente(numero_correto, chute, ):
    value = abs(chute - numero_correto)
    if value <= 3: return "MUITO QUENTE"
    if 3 < value <= 8: return "QUENTE!"
    if 8 < value <= 15: return "MORNO!"
    if 15 < value <= 25: return "FRIO!"
    if value > 25: return "MUITO FRIO!"


def calcular_pontos(diferenca, tentativa):
    return int((100 / diferenca) * tentativa)

def nivel_jogo():
    print("Escolha o nivel do jogo...")
    nivel = int(input("(1) Fácil (2) Médio (3) Difícil (4) Mestre (5) LENDARIO\nOpção: "))
    if nivel < 1 or nivel > 5:
        print("Você escolheu um nível inexistente! Tente Novamente...")
        return nivel_jogo()
    return nivel

def game_over():
    print("Fim de jogo !")
    restart = input("Deseja reiniciar o jogo? Digite S para reiniciar: ")
    return restart.upper() == "S"

def jogo_adivinhacao():
    print("Bem vindo ao jogo de Adivinhação!")
    lvl = nivel_jogo()
    max_numero = 0
    max_rodada = 0
    pontos = 5_000

    if lvl == 1:
        max_numero = 50
        max_rodada = 18
    elif lvl == 2:
        max_numero = 100
        max_rodada = 12
    elif lvl == 3:
        max_numero = 200
        max_rodada = 10
    elif lvl == 4:
        max_numero = 300
        max_rodada = 8
    else:
        max_numero = 500
        max_rodada = 5

    numero_secreto = random.randint(1, max_numero)
    tentativa = 1

    # for rodada in range(1, max_rodada):
    while True:

        try:
            if tentativa == max_rodada + 1:
                print("Você não adivinhou o numero secreto que é {}. GAME OVER HAHAHAHA".format(numero_secreto))
                return game_over()
            print("Rodada {} de {}".format(tentativa, max_rodada))
            chute = int(input("Digite seu numero de 1 a " + str(max_numero) + ": "))
        except ValueError:
            print("Voce digitou algo que não é um numero, tente novamente...")
            continue

        if chute < 1 or chute > max_numero:
            print("Voce digitou um numero fora do limite da adivinhação!")
            continue

        if numero_secreto == chute:
            print("Voce acertou! O número secreto é: ", numero_secreto)
            if tentativa == 0:
                print("Voce fez a pontuação máxima de", pontos, "ao acertar de primeira! PARABENS...")
            else:
                print("Você fez", pontos, "pontos em", tentativa, "tentativas no jogo...")
                return game_over()
        else:
            tentativa = tentativa + 1
            if tentativa > max_rodada: continue
            print("Voce não adivinhou o número!")
            print("DICA: Seu chute está", frio_ou_quente(numero_secreto, chute), '\n')
            pontos = pontos - calcular_pontos(abs(chute - numero_secreto), tentativa)

def format_number():
    formatado = "R$ {:7.2f}".format(24.541)
    print(formatado)
    formatado2 = "R$ {:7.2f}".format(1114.54)
    print(formatado2)
    formatado3 = "R$ {:7.2f}".format(4.54)
    print(formatado3)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    ativar_jogo = True
    #format_number()

    if ativar_jogo:
        comecar_novamente = jogo_adivinhacao()
        while comecar_novamente:
            print('\n\n')
            comecar_novamente = jogo_adivinhacao()
