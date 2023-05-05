from enum import Enum


class Event:

    def __init__(self, event_name: str):
        self.event_name = event_name


class EventResult(Enum):
    ALLOW = 0
    DEFAULT = 1
    DENY = 2


class Cancellable:
    cancelled: bool

    def is_cancelled(self):
        return self.cancelled

    def set_cancelled(self, cancelled: bool):
        self.cancelled = cancelled
