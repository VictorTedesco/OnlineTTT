from onlinettt.board import Board
from onlinettt.events.event import Event, Cancellable


class BoardEvent(Event):

    def __init__(self, board: Board, event_name: str):
        super().__init__(event_name)
        self.__board = board

    def get_board(self):
        return self.__board


class BoardChangeSymbolEvent(BoardEvent, Cancellable):

    def __init__(self, board: Board, position: int, symbol: str):
        super().__init__(board, "Board Change Symbol Event")
        self.__position = position
        self.__symbol = symbol

    def on_call(self):
        board_update = BoardUpdateEvent(self.get_board())
        if self.get_position() > 9:
            raise ValueError("A posição do elemento é maior do que 9.")

        if self.get_symbol() == 'X' or self.get_symbol() == 'O':
            self.get_board().set_symbol(self.get_position(), self.get_symbol())
        else:
            raise ValueError("O simbolo do jogador é diferente de X ou de O.")

        if self.get_board().get_symbol(self.get_position()) is not None:
            board_update.set_cancelled(True)
        Event.call_event(board_update)

    def get_position(self):
        return self.__position

    def set_position(self, position: int):
        self.__position = position

    def get_symbol(self):
        return self.__symbol


class BoardUpdateEvent(BoardEvent, Cancellable):

    def __init__(self, board: Board):
        super().__init__(board, "Board Update Event")

    def on_call(self):
        if self.is_cancelled() is True:
            return
        # TODO: Draw for the client the updated board.


class BoardResetEvent(BoardEvent, Cancellable):

    def __init__(self, board: Board):
        super().__init__(board, "Board Reset Event")

    def on_call(self):
        if self.is_cancelled() is True:
            return
        for i in range(9):
            self.get_board().set_symbol(i, None)
