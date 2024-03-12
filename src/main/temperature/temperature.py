from attrs import define


@define
class Temperature:
    max_temperature: int | None
    min_temperature: int | None
    target_temperature: int | None
    current: int | None

    @staticmethod
    def from_dict(data: dict) -> "Temperature":
        return Temperature(
            max_temperature=data.get("max_temperature", None),
            min_temperature=data.get("min_temperature", None),
            target_temperature=data.get("target_temperature", None),
            current=data.get("current", None),
        )

    def to_dict(self) -> dict[str, int | None]:
        return {
            "max_temperature": self.max_temperature,
            "min_temperature": self.min_temperature,
            "target_temperature": self.target_temperature,
            "current": self.current,
        }
