import adivinhacao
import forca


def game_over():
    print("Fim de jogo !")
    restart = input("Deseja iniciar novo jogo? Digite S para reiniciar: ")
    print('\n')
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

    if option == 2: adivinhacao.play()
    if option == 1: forca.play()
    print('\n')
    game_over()


if __name__ == '__main__':
    main()
