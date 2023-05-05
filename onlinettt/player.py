class Player:

    def __init__(self, name: str, symbol: str, first_to_play: bool):
        self.__name = name
        self.__wins = 0
        self.first_to_play = first_to_play
        if symbol == 'X' or symbol == 'O':
            self.__symbol = symbol
        else:
            raise ValueError("O simbolo do jogador é diferente de X ou de O")

    def get_name(self):
        return self.__name

    def get_symbol(self):
        return self.__symbol

    def get_wins(self):
        return self.__wins

    def increment_wins(self):
        self.__wins += 1
