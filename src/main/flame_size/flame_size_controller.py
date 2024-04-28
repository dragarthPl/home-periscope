from fastapi_injector import Injected
from fastapi_utils.cbv import cbv
from fastapi_utils.inferring_router import InferringRouter

from main.flame_size.flame_size import FlameSize
from main.flame_size.flame_size_repository import IFlameSizeRepository

flame_size_router = InferringRouter(tags=["FlameSizeController"])


@cbv(flame_size_router)
class FlameSizeController:
    flame_size_repository: IFlameSizeRepository = Injected(IFlameSizeRepository)

    @flame_size_router.get("/api/flame_size")
    async def flame_size(self) -> dict[str, str]:
        flame_size: FlameSize = await self.flame_size_repository.get_level()
        return {
            "flame_size": flame_size.value_percentage
        }
