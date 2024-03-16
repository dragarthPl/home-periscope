from abc import ABC, abstractmethod

import pyplumio
from injector import inject

from pyplumio.devices.mixer import Mixer

from main.core.configuration import Configuration
from main.temperature.temperature import Temperature


class IMixerTemperatureRepository(ABC):
    @abstractmethod
    async def get_temperature(self) -> Temperature:
        pass


class MixerTemperatureRepository(IMixerTemperatureRepository):
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

    async def get_temperature(self) -> Temperature:
        async with pyplumio.open_tcp_connection(self.stream_ip, self.stream_port) as conn:
            ecomax = await conn.get("ecomax")
            mixers = await ecomax.get("mixers")
            mixer: Mixer = mixers[0]
            print(mixer.data)
            mixer_target_temp = await mixer.get("target_temp")
            return Temperature.from_dict({
                'max_temperature': self.max_temperature,
                'min_temperature': self.min_temperature,
                'target_temperature': mixer_target_temp,
                'current': int(mixer.current_temp),
            })
