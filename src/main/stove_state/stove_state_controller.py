from fastapi_injector import Injected
from fastapi_utils.cbv import cbv
from fastapi_utils.inferring_router import InferringRouter

from main.stove_state.stove_state import StoveState
from main.stove_state.stove_state_repository import IStoveStateRepository

stove_state_router = InferringRouter(tags=["StoveStateController"])


@cbv(stove_state_router)
class StoveStateController:
    stove_state_repository: IStoveStateRepository = Injected(IStoveStateRepository)

    @stove_state_router.get("/api/stove_state")
    async def stove_state(self) -> dict[str, str]:
        stove_state: StoveState = await self.stove_state_repository.get_state()
        return {
            "stove_state": str(stove_state)
        }