from abc import ABC, abstractmethod

import pyplumio
from injector import inject

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

    @inject
    def __init__(self, configuration: Configuration):
        self.stream_ip = configuration.stream_ip
        self.stream_port = configuration.stream_port

    async def get_temperature(self) -> Temperature:
        async with pyplumio.open_tcp_connection(self.stream_ip, self.stream_port) as conn:
            ecomax = await conn.get("ecomax")
            heating_target_temp = await ecomax.get("heating_target_temp")
            heating_temp = await ecomax.get("heating_temp")
            return Temperature.from_dict({
                'max_temperature': heating_target_temp.max_value,
                'min_temperature': heating_target_temp.min_value,
                'target_temperature': heating_target_temp.value,
                'current': int(heating_temp),
            })

    async def set_temperature(self, temperature: int) -> bool:
        async with pyplumio.open_tcp_connection(self.stream_ip, self.stream_port) as conn:
            ecomax = await conn.get("ecomax")
            result = bool(await ecomax.set("heating_target_temp", temperature))
            return result
        return False
