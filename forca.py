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


def open_word_file():
    word_file = "./palavras.txt"
    return utils.remove_duplicates(open(word_file).read().splitlines())


def get_random_word_from_list(l):
    random.shuffle(l)
    return l[0]


def assemble_char(current, attempt):
    if attempt == 1:
        current[2] = util.replacer(current[2], "(o_o)", 4)
    if attempt == 2:
        current[3] = util.replacer(current[3], "/", 4)
    if attempt == 3:
        current[3] = util.replacer(current[3], " | ", 5)
    if attempt == 4:
        current[3] = util.replacer(current[3], " \\", 7)
    if attempt == 5:
        current[4] = util.replacer(current[4], "|", 6)
    if attempt == 6:
        current[5] = util.replacer(current[5], "/", 5)
    if attempt == 7:
        current[5] = util.replacer(current[5], " \\", 6)
    return current


def play():
    print("Bem vindo ao jogo da Forca!")
    game_word = ''
    words_list = open_word_file()
    secret_word = get_random_word_from_list(words_list).upper()
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
        if errors > 6:
            hanged = True
        attempt += 1
        if not game_word.__contains__('_'):
            achieved = True

    if hanged:
        print("Você foi enforcado! GAME OVER HAHAHA")
    else:
        print("Você acertou a palavra secreta: {} em {} tentativas. PARABÉNS!".format(secret_word, attempt))


if __name__ == "__main__":
    play()
