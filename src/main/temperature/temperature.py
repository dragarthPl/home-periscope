from attrs import define


@define
class Temperature:
    max_temperature: int
    min_temperature: int
    current: int

    @staticmethod
    def from_dict(data: dict) -> "Temperature":
        return Temperature(
            max_temperature=data.get("max_temperature"),
            min_temperature=data.get("min_temperature"),
            current=data.get("current"),
        )
