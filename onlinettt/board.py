from onlinettt.player import Player


class Board:

    def __init__(self, players: [Player, Player]):
        self.table = []
        for i in range(9):
            self.table.append(None)
        self.players = players

    def get_element_on_position(self, position: int):
        if position > 9:
            raise ValueError("A posição do elemento é maior do que 9.")
        return self.table[position - 1]

    def set_element_on_position(self, position: int, new_element):
        if position > 9:
            raise ValueError("A posição do elemento é maior do que 9.")

        if self.table[position - 1] is not None:
            raise

        if new_element == 'X' or new_element == 'O':
            self.table[position - 1] = new_element
        else:
            raise ValueError("O simbolo do jogador é diferente de X ou de O.")

        self.update_board()

    def draw_board(self):
        return

    def update_board(self):
        return
