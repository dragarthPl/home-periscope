from abc import ABC, abstractmethod

from injector import inject
from redis import Redis

from main.core.configuration import Configuration
from main.summer_mode.summer_mode import SummerMode


class ISummerModeRepository(ABC):
    @abstractmethod
    async def get_state(self) -> SummerMode:
        pass


class SummerModeRepository(ISummerModeRepository):
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
    async def get_state(self) -> SummerMode:
        stove_data = self.__redis.hgetall("stove_data")
        return SummerMode(int(stove_data.get("summer_mode", 0)))
