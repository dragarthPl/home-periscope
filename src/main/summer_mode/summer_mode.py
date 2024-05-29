from typing import Final


class SummerMode:
    SUMMER: Final[str] = "Lato"
    WINTER: Final[str] = "Zima"
    UNKNOWN: Final[str] = "Nieznany"

    __mode: int

    def __init__(self, mode: int):
        self.__mode = mode

    @classmethod
    def from_mode_string(cls, mode: str) -> 'SummerMode':
        if mode == cls.SUMMER:
            return SummerMode(1)
        elif mode == cls.WINTER:
            return SummerMode(0)
        else:
            raise Exception("Unknown summer mode")

    def get_mode(self):
        if self.__mode == 1:
            return {
                "summer_mode": self.SUMMER
            }
        elif self.__mode == 0:
            return {
                "summer_mode": self.WINTER
            }
        else:
            raise Exception("Unknown summer mode")
