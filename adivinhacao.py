import random
from objects.adivinhacao.adivinhacao import Adivinhacao


def play():
    game = Adivinhacao()
    print(game)

    # for rodada in range(1, max_rodada):
    while True:

        try:
            game.print_round()
            shot = int(input("Digite seu numero de 1 a " + str(game.max_number) + ": "))
        except ValueError:
            print("Voce digitou algo que não é um numero, tente novamente...")
            continue

        if shot < 1 or shot > game.max_number:
            print("Voce digitou um numero fora do limite da adivinhação!")
            continue

        if game.secret_number == shot:
            game.print_winner()
            break
        else:
            if not game.has_attempts_available():
                game.print_looser()
                break
            game.update_game_round(shot)
