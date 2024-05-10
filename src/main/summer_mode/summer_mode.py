from typing import Final


class SummerMode:
    SUMMER: Final[str] = "Lato"
    WINTER: Final[str] = "Zima"
    UNKNOWN: Final[str] = "Nieznany"

    __mode: int

    def __init__(self, mode: int):
        self.__mode = mode

    def get_mode(self):
        if self.__mode == 1:
            return self.SUMMER
        else:
            return self.WINTER
