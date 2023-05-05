from onlinettt.board import Board
from onlinettt.player import Player


class Match:

    def __init__(self, board: Board, players: [Player, Player]):
        self.__board = board
        self.__players = players

    def get_board(self):
        return self.__board

    def get_player(self):
        return self.__players
