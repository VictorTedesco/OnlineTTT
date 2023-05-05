from onlinettt.player import Player


class Board:

    def __init__(self, players: [Player, Player]):
        self.__table = [None for _ in range(9)]
        self.__players = players

    def get_symbol(self, position: int):
        if position > 9:
            return
        return self.__table[position - 1]

    def set_symbol(self, position: int, new_element):
        if position > 9:
            return
        self.__table[position - 1] = new_element

    def get_players(self):
        return self.__players
