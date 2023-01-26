import adivinhacao
import forca


def start(game):
    if game == 2: adivinhacao.play()
    if game == 1: forca.play()
    print('\n')
    return game_over()


def choose_game():
    print("(1) Forca (2) Adivinhação")
    try:
        opt = int(input("Digite sua opção: "))
        if opt != 1 and opt != 2: raise ValueError
    except ValueError:
        print("Você escolheu uma opção inexistente. Tente novamente...")
        return choose_game()
    return opt


def game_over():
    print("Fim de jogo !")
    restart = input("Deseja iniciar novo jogo? Digite S para reiniciar: ")
    print('\n')
    return restart.upper() == "S"


def main():
    print("***********************************")
    print("***** Escolha algo para jogar *****")
    print("***********************************\n")

    if start(choose_game()):
        main()


if __name__ == '__main__':
    main()
