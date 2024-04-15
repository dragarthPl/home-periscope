from abc import ABC, abstractmethod

import pyplumio
from injector import inject
from redis import Redis

from main.core.configuration import Configuration
from main.stove_state.stove_state import StoveState


class IStoveStateRepository(ABC):
    @abstractmethod
    async def get_state(self) -> StoveState:
        pass


class StoveStateRepository(IStoveStateRepository):
    stream_ip: str
    stream_port: int
    min_temperature: int
    max_temperature: int
    __redis: Redis

    @inject
    def __init__(self, configuration: Configuration, redis: Redis):
        self.__redis = redis
        self.stream_ip = configuration.stream_ip
        self.stream_port = configuration.stream_port
        self.min_temperature = configuration.default_minimum_temperature
        self.max_temperature = configuration.default_maximum_temperature

    # split-environments
    async def get_state(self) -> StoveState:
        stove_data = self.__redis.hgetall("stove_data")
        return StoveState(int(stove_data.get("state", 0)))