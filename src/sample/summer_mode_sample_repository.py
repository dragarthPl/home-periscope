from main.summer_mode.summer_mode import SummerMode
from main.summer_mode.summer_mode_repository import ISummerModeRepository


class SummerModeSampleRepository(ISummerModeRepository):
    async def get_summer_mode(self) -> SummerMode:
        return SummerMode(1)
