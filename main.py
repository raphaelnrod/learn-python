import random


def print_date(dia, mes, ano):
    print(dia, mes, ano, sep="/")


def print_type(var, var_name):
    print('The', var_name, "is a type of:", type(var))


def frio_ou_quente(numero_correto, chute, max_numero):
    value = abs(chute - numero_correto)
    if value <= round(max_numero * 0.02): return "EXTREMAMENTE QUENTE!!!"
    if round(max_numero * 0.02) < value <= round(max_numero * 0.05): return "MUITO QUENTE!"
    if round(max_numero * 0.05) < value <= round(max_numero * 0.15): return "QUENTE!"
    if round(max_numero * 0.15) < value <= round(max_numero * 0.25): return "MORNO!"
    if round(max_numero * 0.25) < value <= round(max_numero * 0.4): return "FRIO!"
    if value > round(max_numero * 0.4): return "MUITO FRIO!"


def calcular_pontos(diferenca, tentativa, lvl):
    return int((100 / diferenca * lvl) * tentativa)


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


def get_game_lvl(lvl):
    # returns [max_numero, max_rodada]
    if lvl == 1:
        return [50, 18]
    elif lvl == 2:
        return [100, 12]
    elif lvl == 3:
        return [200, 10]
    elif lvl == 4:
        return [300, 8]
    else:
        return [500, 5]


def jogo_adivinhacao():
    print("Bem vindo ao jogo de Adivinhação!")
    lvl = nivel_jogo()
    pontos = 5_000

    max_numero = get_game_lvl(lvl)[0]
    max_rodada = get_game_lvl(lvl)[1]

    numero_secreto = random.randint(1, max_numero)
    tentativa = 1
    print(numero_secreto)

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
            print("DICA: Seu chute está", frio_ou_quente(numero_secreto, chute, max_numero), '\n')
            pontos = pontos - calcular_pontos(abs(chute - numero_secreto), tentativa, lvl)


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
    # format_number()

    if ativar_jogo:
        comecar_novamente = jogo_adivinhacao()
        while comecar_novamente:
            print('\n\n')
            comecar_novamente = jogo_adivinhacao()
