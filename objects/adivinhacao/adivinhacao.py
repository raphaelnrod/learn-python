from objects.Game import Game
import random


class Adivinhacao(Game):

    def __init__(self):
        super().__init__("Adivinhação")
        self.__level = self.__set_level()
        self.__max_number = self.__get_game_lvl(self.__level)[0]
        self.__max_attempts = self.__get_game_lvl(self.__level)[1]
        self.__secret_number = random.randint(1, self.__max_number)
        self.attempt = 1
        self.score = 5_000

    @property
    def secret_number(self):
        return self.__secret_number

    @property
    def max_number(self):
        return self.__max_number

    def update_score(self, shot):
        self.score -= self.__calc_score(shot)

    def has_attempts_available(self):
        return self.attempt <= self.__max_attempts

    def print_tip(self):
        print(f'Você não adivinhou o numero secreto que é {self.__secret_number}. GAME OVER HAHAHAHA')

    def print_winner(self):
        print("Voce acertou! O número secreto é: ", self.secret_number)
        if self.attempt == 1:
            print("Voce fez a pontuação máxima de", self.score, "ao acertar de primeira! PARABENS...")
        else:
            print("Você fez", self.score, "pontos em", self.attempt, "tentativas no jogo...")

    def print_looser(self):
        print(f'Você não adivinhou o numero secreto que é {self.__secret_number}. GAME OVER HAHAHAHA')

    def print_round(self):
        print(f'Rodada {self.attempt} de {self.__max_attempts}')

    def update_game_round(self, shot):
        self.attempt += 1
        print("Voce não adivinhou o número!")
        print("DICA: Seu chute está", self.__what_close_number_is(shot), '\n')
        self.update_score(shot)

    def __calc_score(self, shot):
        return int((10 / abs(shot - self.__secret_number) * self.__level) * self.attempt)

    def __what_close_number_is(self, shot):
        value = abs(shot - self.__secret_number)
        if value <= round(self.__max_number * 0.02): return "EXTREMAMENTE QUENTE!!!"
        if round(self.__max_number * 0.02) < value <= round(self.__max_number * 0.05): return "MUITO QUENTE!"
        if round(self.__max_number * 0.05) < value <= round(self.__max_number * 0.15): return "QUENTE!"
        if round(self.__max_number * 0.15) < value <= round(self.__max_number * 0.25): return "MORNO!"
        if round(self.__max_number * 0.25) < value <= round(self.__max_number * 0.4): return "FRIO!"
        if value > round(self.__max_number * 0.4): return "MUITO FRIO!"

    def __set_level(self):
        print("Escolha o nivel do jogo...")
        try:
            lvl = int(input("(1) Fácil (2) Médio (3) Difícil (4) Mestre (5) LENDARIO\nOpção: "))
            if lvl < 1 or lvl > 5: raise ValueError
        except ValueError:
            print("Você escolheu um nível inexistente! Tente Novamente...")
            return self.__set_level()
        return lvl

    @staticmethod
    def __get_game_lvl(lvl):
        # returns [max_number, max_attempts]
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
