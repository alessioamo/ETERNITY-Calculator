from enum import Enum, auto


class PossibleEvents(Enum):
    CLEAR_BUTTON_PRESSED = auto()
    FUNCTION_BUTTON_PRESSED = auto()


class EventManager:

    events = {}

    @classmethod
    def Register(cls, event, functionToExecute):
        if not (event in cls.events.keys()):
            cls.events[event] = []

        cls.events[event].append(functionToExecute)

    @classmethod
    def Notify(cls, event, param=None):
        if event in cls.events.keys():
            for function in cls.events[event]:
                function(param)
