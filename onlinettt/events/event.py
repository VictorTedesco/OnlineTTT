from enum import Enum


class Event:

    def __init__(self, event_name: str):
        self.__event_name = event_name
        self.__event_result = EventResult.DEFAULT

    @staticmethod
    def call_event(self):
        if self.get_event_result == EventResult.ALLOW or EventResult.DEFAULT:
            self.on_call()
        else:
            return

    def on_call(self):
        pass

    def get_event_result(self):
        return self.__event_result

    def set_event_result(self, event_result: EventResult):
        self.__event_result = event_result


class EventResult(Enum):
    ALLOW = 0
    DEFAULT = 1
    DENY = 2


class Cancellable:
    __cancelled: bool

    def is_cancelled(self):
        return self.__cancelled

    def set_cancelled(self, cancelled: bool):
        self.__cancelled = cancelled
