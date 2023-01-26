from objects.forca.Forca import Forca
from objects.forca.Doll import Doll


def play():
    forca = Forca()
    word = forca.word
    doll = Doll()
    print(forca)

    hanged = False
    achieved = False
    forca.print_word_tip()
    doll.print()
    forca.print_progress()
    used_char = []

    while not achieved and not hanged:
        shot = input("Escolha uma letra: ").upper()
        if len(shot) > 1:
            print("Escolha apenas UMA letra!")
            continue
        if shot in used_char:
            print("Você já escolheu essa letra! Tente novamente...")
            continue

        used_char.append(shot)
        find_letter_in_word(word, shot, forca, doll)
        doll.print()
        forca.print_progress()
        print("Letras já usadas:", " ".join(used_char), "\n")
        hanged = forca.errors > 6
        forca.attempt += 1
        achieved = word.is_progress_done()

    forca.print_looser() if hanged else forca.print_winner()


def find_letter_in_word(word, shot, forca, doll):
    matches = False
    index = 0
    for letter in word.secret_word:
        if shot == letter:
            word.update_progress(letter, index)
            matches = True
        index += 1
        if index >= len(word.secret_word):
            if matches:
                print(f"Você acertou a letra: {shot.upper()}\n")
            else:
                print(f"A palavra secreta não possui a letra: {shot.upper()}\n")
                forca.errors += 1
                doll.update_char(forca.errors)


if __name__ == "__main__":
    play()
