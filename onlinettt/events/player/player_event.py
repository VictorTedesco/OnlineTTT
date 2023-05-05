from onlinettt.events.event import Event, Cancellable
from onlinettt.player import Player


class PlayerEvent(Event):

    def __init__(self, player: Player, event_name: str):
        super().__init__(event_name)
        self.player = player


class PlayerJoinEvent(PlayerEvent):

    def __init__(self, player: Player):
        super().__init__(player, "Player Join Event")


class PlayerQuitEvent(PlayerEvent):

    def __init__(self, player: Player):
        super().__init__(player, "Player Quit Event")

    def on_call(self):
        return
        # TODO: Send a message to the other player


class PlayerClickOnBoardEvent(PlayerEvent, Cancellable):

    def __init__(self, player: Player, position: int):
        super().__init__(player, "Player Click On Board Event")
        self.position = position
