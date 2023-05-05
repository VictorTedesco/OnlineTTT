from onlinettt.events.event import Event, Cancellable
from onlinettt.match import Match


class MatchEvent(Event):

    def __init__(self, match: Match, event_name: str):
        super().__init__(event_name)
        self.__match = match

    def get_match(self):
        return self.__match


class MatchStartEvent(Event, Cancellable):

    def __init__(self):
        super().__init__("Match Start Event")

    def on_call(self):
        return


class MatchEndEvent(Event, Cancellable):

    def __init__(self):
        super().__init__("Match End Event")

    def on_call(self):
        return
