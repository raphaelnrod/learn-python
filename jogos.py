import adivinhacao as adv_game
import forca as forca_game


def game_over():
    print("Fim de jogo !")
    restart = input("Deseja iniciar novo jogo? Digite S para reiniciar: ")
    if restart.upper() == "S": main()


def choose_game():
    print("(1) Forca (2) Adivinhação")
    try:
        opt = int(input("Digite sua opção: "))
        if opt != 1 and opt != 2: raise ValueError
    except ValueError:
        print("Você escolheu uma opção inexistente. Tente novamente...")
        return choose_game()
    return opt


def main():
    print("***********************************")
    print("***** Escolha algo para jogar *****")
    print("***********************************\n")
    option = choose_game()

    if option == 1: forca_game.jogo_da_forca()
    if option == 2: adv_game.jogo_adivinhacao()
    print('\n')
    game_over()
    print('\n')


if __name__ == '__main__':
    main()
