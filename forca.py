import utils
import utils as util
import random


def initial_char():
    return [
        " _____     ",
        "|     |    ",
        "|         ",
        "|         ",
        "|         ",
        "|          ",
    ]


def print_char(doll_char):
    for curr in doll_char: print(curr)


def get_secret_word():
    words_file = open("words/palavras.txt").read().splitlines()
    random.shuffle(words_file)
    tip = words_file[0]
    word_list = open("words/{}.txt".format(tip)).read().splitlines()
    random.shuffle(word_list)
    secret_word = word_list[0]
    return {'tip': tip, 'secret': secret_word}


def doll_config():
    # configuracao para montagem do boneco sendo enforcado
    # primeira tuple = numero da linha da matriz do desenho a ser alterada
    # segunda tuple = string da parte do boneco
    # terceira tuple = index (horizontalmente) onde vai ser feito o replace para uma parte do corpo do boneco
    return {
        "attempt1": (2, "(o_o)", 4),
        "attempt2": (3, "/", 4),
        "attempt3": (3, " | ", 5),
        "attempt4": (3, " \\", 7),
        "attempt5": (4, "|", 6),
        "attempt6": (5, "/", 5),
        "attempt7": (5, " \\", 6),
    }


def assemble_char(current, attempt):
    a = "attempt" + str(attempt)
    c = doll_config().get(a)
    current[c[0]] = util.replacer(current[c[0]], c[1], c[2])
    return current


def play():
    print("Bem vindo ao jogo da Forca!")
    game_word = ''
    secret_tip = get_secret_word()
    secret_word = secret_tip.get('secret').upper()
    tip_word = secret_tip.get('tip').upper()
    if len(secret_word.split()) > 1:
        compost = secret_word.split()
        idx = len(compost)
        for i in range(idx):
            game_word = game_word + ''.ljust(len(compost[i])).replace(' ', '_')
            if i != idx:
                game_word = game_word + " "
    else:
        game_word = ''.ljust(len(secret_word)).replace(' ', '_')

    hanged = False
    achieved = False
    print("A palavra secreta possui {} letras!".format(len(secret_word)))
    print("FIQUE ATENTO! A dica é: {}!".format(tip_word))
    doll_char = initial_char()
    print_char(doll_char)
    print("Progresso:", game_word)
    attempt = 1
    errors = 0
    used_char = []

    while not achieved and not hanged:
        shot = input("Escolha uma letra: ").upper()
        if len(shot) > 1:
            print("Escolha apenas UMA letra!")
            continue
        if used_char.__contains__(shot):
            print("Você já escolheu essa letra! Tente novamente...")
            continue

        used_char.append(shot)
        index = 0
        matches = False
        for letter in secret_word:
            if shot == letter:
                game_word = util.replacer(game_word, letter, index)
                matches = True
            index += 1
            if index >= len(secret_word):
                if matches:
                    print("Você acertou a letra: {}\n".format(shot.upper()))
                else:
                    print("A palavra secreta não possui a letra: {}\n".format(shot.upper()))
                    errors += 1
                    doll_char = assemble_char(doll_char, errors)

        print_char(doll_char)
        print("Progresso:", game_word)
        print("Letras já usadas:", " ".join(used_char), "\n")
        hanged = errors > 6
        attempt += 1
        achieved = not game_word.__contains__('_')

    if hanged:
        print("Você foi enforcado! GAME OVER HAHAHA")
    else:
        print("Você acertou a palavra secreta: {} em {} tentativas. PARABÉNS!".format(secret_word, attempt))


if __name__ == "__main__":
    play()
