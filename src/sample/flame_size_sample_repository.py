from main.flame_size.flame_size import FlameSize
from main.flame_size.flame_size_repository import IFlameSizeRepository


class FlameSizeSampleRepository(IFlameSizeRepository):
    async def get_level(self) -> FlameSize:
        return FlameSize(30)
