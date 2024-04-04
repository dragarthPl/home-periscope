from typing import Any

import redis
import asyncio
import pyplumio
from pyplumio.devices.mixer import Mixer
from pyplumio.structures.ecomax_parameters import EcomaxParameter


class StreamStoveData:
    __ip_stove_driver: str
    __port_stove_driver: int
    __redis_connect: redis.Redis

    def __init__(
        self,
        ip_stove_driver: str,
        port_stove_driver: int,
        redis_ip: str,
        redis_port: int
    ):
        self.__ip_stove_driver = ip_stove_driver
        self.__port_stove_driver = port_stove_driver
        self.__redis_connect = redis.Redis(host=redis_ip, port=redis_port, decode_responses=True)

    @staticmethod
    def extract_value(parameter: EcomaxParameter | None):
        if parameter:
            return parameter.value
        return None

    def map_stove_data_to_hash_map(self, data: dict[str, Any], mixer: dict[str, Any]) -> None:
        data_map = {
            'fan_power_percentage': self.extract_value(data.get('min_fan_power', None)),
            'state': self.extract_value(data.get('state', None)),
            'feeder_temp': data['feeder_temp'],
            'optical_temp': data['optical_temp'],

            'heating_target': data['heating_target'],
            'heating_status': data['heating_status'],

            'heating_temp': data['heating_temp'],
            'heating_target_temp': self.extract_value(data['heating_target_temp']),
            'min_heating_target_temp': self.extract_value(data['min_heating_target_temp']),
            'max_heating_target_temp': self.extract_value(data['max_heating_target_temp']),

            'water_heater_target': data['water_heater_target'],
            'water_heater_temp': data['water_heater_temp'],
            'water_heater_target_temp': self.extract_value(data.get('water_heater_target_temp', None)),
            'min_water_heater_target_temp': self.extract_value(data.get('min_water_heater_target_temp', None)),
            'max_water_heater_target_temp': self.extract_value(data.get('max_water_heater_target_temp', None)),

            'mixer_target_temp': mixer.get('target_temp', None),
            'mixer_current_temp': mixer.get('current_temp', None),
            'min_mixer_temp': self.extract_value(mixer.get('min_target_temp', None)),
            'max_mixer_temp': self.extract_value(mixer.get('max_target_temp', None)),

        }
        self.__redis_connect.hset(
            'stove_data',
            mapping=data_map
        )

    async def stream(self):
        async with pyplumio.open_tcp_connection(self.__ip_stove_driver, self.__port_stove_driver) as conn:
            while True:
                ecomax = await conn.get("ecomax")
                await ecomax.wait_for("regdata")
                mixers = await ecomax.get("mixers")
                mixer: Mixer = mixers[0]
                self.map_stove_data_to_hash_map(ecomax.data, mixer.data)
                await asyncio.sleep(1)

if __name__ == '__main__':
    stream_ip = "192.168.1.236"
    stream_port = 9801
    stream_stove_data = StreamStoveData(
        ip_stove_driver=stream_ip,
        port_stove_driver=stream_port,
        redis_ip="localhost",
        redis_port=6379
    )
    asyncio.run(stream_stove_data.stream())