from onlinettt.board import Board
from onlinettt.events.board.board_event import BoardChangeSymbolEvent
from onlinettt.events.event import Event, Cancellable
from onlinettt.player import Player


class PlayerEvent(Event):

    def __init__(self, player: Player, event_name: str):
        super().__init__(event_name)
        self.__player = player

    def get_player(self):
        return self.__player


class PlayerJoinEvent(PlayerEvent):

    def __init__(self, player: Player):
        super().__init__(player, "Player Join Event")

    def on_call(self):
        return
        # TODO: Send a message to the other player
        # TODO: Check if two players are online to start the game


class PlayerQuitEvent(PlayerEvent):

    def __init__(self, player: Player):
        super().__init__(player, "Player Quit Event")

    def on_call(self):
        return
        # TODO: Send a message to the other player


class PlayerClickOnBoardEvent(PlayerEvent, Cancellable):

    def __init__(self, player: Player, board: Board, position: int):
        super().__init__(player, "Player Click On Board Event")
        self.board = board
        self.position = position

    def on_call(self):
        if self.is_cancelled() is True:
            return
        board_change_symbol = BoardChangeSymbolEvent(self.board, self.position, self.__player.get_symbol())
