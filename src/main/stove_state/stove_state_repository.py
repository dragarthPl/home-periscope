from abc import ABC, abstractmethod

import pyplumio
from injector import inject

from main.core.configuration import Configuration
from main.stove_state.stove_state import StoveState
from main.temperature.temperature import Temperature


class IStoveStateRepository(ABC):
    @abstractmethod
    async def get_state(self) -> Temperature:
        pass


class StoveStateRepository(IStoveStateRepository):
    stream_ip: str
    stream_port: int
    min_temperature: int
    max_temperature: int

    @inject
    def __init__(self, configuration: Configuration):
        self.stream_ip = configuration.stream_ip
        self.stream_port = configuration.stream_port
        self.min_temperature = configuration.default_minimum_temperature
        self.max_temperature = configuration.default_maximum_temperature

    # split-environments
    async def get_state(self) -> StoveState:
        async with pyplumio.open_tcp_connection(self.stream_ip, self.stream_port) as conn:
            ecomax = await conn.get("ecomax")
            state = await ecomax.get("state")
            return StoveState(state)
