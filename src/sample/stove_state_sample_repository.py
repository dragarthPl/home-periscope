from pyplumio.const import DeviceState

from main.stove_state.stove_state import StoveState
from main.stove_state.stove_state_repository import IStoveStateRepository


class StoveStateSampleRepository(IStoveStateRepository):
    async def get_state(self) -> StoveState:
        return StoveState(DeviceState.STABILIZATION)
