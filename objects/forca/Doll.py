import utils


class Doll:

    def __init__(self):
        self.__char = self.__initial_char()

    def print(self):
        for curr in self.__char:
            print(curr)

    def __assemble_char(self, current, attempt):
        a = "attempt" + str(attempt)
        c = self.__doll_config().get(a)
        current[c[0]] = utils.replacer(current[c[0]], c[1], c[2])
        return current

    @property
    def char(self):
        return self.__char

    def update_char(self, errors):
        self.__char = self.__assemble_char(self.__char, errors)

    @staticmethod
    def __initial_char():
        return [
            " _____     ",
            "|     |    ",
            "|         ",
            "|         ",
            "|         ",
            "|          ",
        ]

    @staticmethod
    def __doll_config():
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




