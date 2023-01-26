from objects.forca.Word import Word
from objects.Game import Game


class Forca(Game):

    def __init__(self):
        super().__init__('Forca')
        self.__word = Word()
        self.__score = 1000
        self.errors = 0
        self.attempt = 1

    @property
    def word(self):
        return self.__word

    def print_word_tip(self):
        print("A palavra secreta possui {} letras!".format(len(self.__word.secret_word)))
        print("FIQUE ATENTO! A dica é: {}!".format(self.__word.tip))

    def print_progress(self):
        print("Progresso:", self.__word.progress)

    def print_looser(self):
        print("Você foi enforcado! GAME OVER HAHAHA")
        print(f"Você fez {self.__score}")

    def print_winner(self):
        print(f"Você acertou a palavra secreta: {self.__word.secret_word} em {self.attempt} tentativas. PARABÉNS!")

