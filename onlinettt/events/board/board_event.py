from onlinettt.board import Board
from onlinettt.events.event import Event, Cancellable
from onlinettt.player import Player


class BoardEvent(Event):

    def __init__(self, board: Board, event_name: str):
        super().__init__(event_name)
        self.board = board


class BoardUpdateEvent(BoardEvent, Cancellable):

    def __init__(self, board: Board):
        super().__init__(board, "Board Update Event")

    def on_call(self, board: Board):
        if self.cancelled is True:
            return
        # TODO: Draw for the client the updated board.


class BoardResetEvent(BoardEvent, Cancellable):

    def __init__(self, board: Board):
        super().__init__(board, "Board Reset Event")

    def on_call(self, board: Board):
        if self.cancelled is True:
            return
        board.table = []
