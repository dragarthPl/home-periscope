from abc import ABC, abstractmethod

from injector import inject
from redis import Redis

from main.flame_size.flame_size import FlameSize


class IFlameSizeRepository(ABC):
    @abstractmethod
    async def get_level(self) -> FlameSize:
        pass


class FlameSizeRepository(IFlameSizeRepository):
    __redis: Redis

    @inject
    def __init__(self, redis: Redis):
        self.__redis = redis

    async def get_level(self) -> FlameSize:
        stove_data = self.__redis.hgetall("stove_data")
        return FlameSize(int(float(stove_data["optical_temp"])))
