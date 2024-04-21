import json
from abc import ABC, abstractmethod

from injector import inject
from redis import Redis

from main.core.configuration import Configuration
from main.temperature.temperature import Temperature


class IHeatingTemperatureRepository(ABC):
    @abstractmethod
    async def get_temperature(self) -> Temperature:
        pass

    @abstractmethod
    async def set_temperature(self, temperature: int) -> bool:
        pass


class HeatingTemperatureRepository(IHeatingTemperatureRepository):
    stream_ip: str
    stream_port: int
    __redis: Redis

    @inject
    def __init__(self, configuration: Configuration, redis: Redis):
        self.stream_ip = configuration.stream_ip
        self.stream_port = configuration.stream_port
        self.__redis = redis

    async def get_temperature(self) -> Temperature:
        stove_data = self.__redis.hgetall("stove_data")
        return Temperature.from_dict({
            'max_temperature': int(stove_data.get("max_heating_target_temp")),
            'min_temperature': int(stove_data.get("min_heating_target_temp")),
            'target_temperature': int(stove_data.get("heating_target_temp")),
            'current': int(float(stove_data.get("heating_temp"))),
            'timestamp': int(float(stove_data.get("timestamp"))),
        })

    async def set_temperature(self, temperature: int) -> bool:
        command = {
            "component": "ecomax",
            "parameter": "heating_target_temp",
            "value": temperature,
        }
        try:
            self.__redis.lpush("stove_command", json.dumps(command))
        except Exception:
            return False
        return True
