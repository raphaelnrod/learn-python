
class Game:

    def __init__(self, nome):
        self._nome = nome.title()

    def __str__(self):
        title = f"Bem vindo ao jogo da {self._nome.upper()}"
        size = len(title)
        side = int((38 - size) / 2)
        top_bottom = '****************************************'
        middle = f'*{"".ljust(side)}{title}{"".ljust(side)}*'
        return f'{top_bottom}\n{middle}\n{top_bottom}'

