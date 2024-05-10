from fastapi_injector import Injected
from fastapi_utils.cbv import cbv
from fastapi_utils.inferring_router import InferringRouter

from main.summer_mode.summer_mode import SummerMode

from main.summer_mode.summer_mode_repository import ISummerModeRepository

summer_mode_router = InferringRouter(tags=["SummerModeController"])


@cbv(summer_mode_router)
class SummerModeController:
    summer_mode_repository: ISummerModeRepository = Injected(ISummerModeRepository)

    @summer_mode_router.get("/api/summer_mode")
    async def summer_mode(self) -> str:
        summer_mode: SummerMode = await self.summer_mode_repository.get_summer_mode()
        if summer_mode:
            return summer_mode.get_mode()
        else:
            return SummerMode.UNKNOWN
