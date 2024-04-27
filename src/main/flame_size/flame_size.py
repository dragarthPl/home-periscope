from attrs import define, field


@define
class FlameSize:
    __value_percentage: int = field(alias="value_percentage")

    @property
    def value_percentage(self) -> str:
        return f"{self.__value_percentage}%"

