import json
import os
from datetime import datetime
from typing import Any

import click
from loguru import logger

import redis
import asyncio
import pyplumio
from pyplumio.const import DeviceState
from pyplumio.devices.ecomax import EcoMAX
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
    def extract_value(parameter: EcomaxParameter | None) -> int | float:
        if isinstance(parameter, DeviceState):
            return parameter.value
        if isinstance(parameter, (float, int)):
            return parameter
        if parameter:
            return parameter.value
        return -1

    def map_stove_data_to_hash_map(self, data: dict[str, Any], mixer: dict[str, Any]) -> None:
        data_map = {
            'state': self.extract_value(data.get('state', None)),
            'feeder_temp': self.extract_value(data.get('feeder_temp', None)),
            'optical_temp': self.extract_value(data.get('optical_temp', None)),  # Procent płomienia

            'heating_target': self.extract_value(data.get('heating_target', None)),
            'heating_status': self.extract_value(data.get('heating_status', None)),

            'heating_temp': self.extract_value(data.get('heating_temp', None)),
            'heating_target_temp': self.extract_value(data.get('heating_target_temp', None)),
            'min_heating_target_temp': self.extract_value(data.get('min_heating_target_temp', None)),
            'max_heating_target_temp': self.extract_value(data.get('max_heating_target_temp', None)),

            'water_heater_target': self.extract_value(data.get('water_heater_target', None)),
            'water_heater_temp': self.extract_value(data.get('water_heater_temp', None)),
            'water_heater_target_temp': self.extract_value(data.get('water_heater_target_temp', None)),
            'min_water_heater_target_temp': self.extract_value(data.get('min_water_heater_target_temp', None)),
            'max_water_heater_target_temp': self.extract_value(data.get('max_water_heater_target_temp', None)),

            'mixer_target_temp': self.extract_value(mixer.get('target_temp', None)),
            'mixer_current_temp': self.extract_value(mixer.get('current_temp', None)),
            'min_mixer_temp': self.extract_value(mixer.get('min_target_temp', None)),
            'max_mixer_temp': self.extract_value(mixer.get('max_target_temp', None)),

            'summer_mode': self.extract_value(data.get('summer_mode', None)),

            'timestamp': int(float(datetime.now().timestamp()))

        }
        self.__redis_connect.hset(
            'stove_data',
            mapping=data_map
        )

    async def send_data_to_controller(self, ecomax: EcoMAX, command: dict[str, str]) -> None:
        await ecomax.set(command.get("parameter"), command.get("value"))

    async def write_if_command(self, ecomax: EcoMAX, mixer: Mixer, pubsub) -> None:
        command_str = pubsub.get_message()
        command = json.loads(command_str) if command_str else None
        if command:
            component = command.get("component")
            logger.debug(f"Command {command}")
            if component == "ecomax":
                await self.send_data_to_controller(ecomax, command)

    async def stream(self) -> None:
        logger.info("Start streaming data to redis")
        pubsub = self.__redis_connect.pubsub()
        pubsub.subscribe('command-channel')
        async with pyplumio.open_tcp_connection(self.__ip_stove_driver, self.__port_stove_driver) as conn:
            counter = 0
            logger.info("Infinitive loop for streaming data to redis")
            while True:
                ecomax = await conn.get("ecomax")
                logger.debug("Connected to ecomax")
                await ecomax.wait_for("regdata")
                logger.debug("Received regdata")
                mixers = await ecomax.get("mixers")
                logger.debug("Received mixers")
                mixer: Mixer = mixers[0]
                self.map_stove_data_to_hash_map(ecomax.data, mixer.data)
                await self.write_if_command(ecomax, mixer, pubsub)

                await asyncio.sleep(1)
                if counter > 15:
                    counter = 0
                    logger.debug("Streaming to redis is alive")
                counter += 1


@click.command()
@click.option('--stream_ip', envvar="STREAM_IP", help="The IP address of the stove driver")
@click.option('--stream_port', envvar="STREAM_PORT", help="The port of the stove driver")
@click.option(
    '--redis_ip',
    envvar="REDIS_IP",
    default="localhost",
    help="The IP address of the redis server",
)
@click.option(
    '--redis_port',
    envvar="REDIS_PORT",
    default=6379,
    help="The port of the redis server",
)
def cli(stream_ip: str, stream_port: int, redis_ip: str, redis_port: int):
    stream_stove_data = StreamStoveData(
        ip_stove_driver=stream_ip,
        port_stove_driver=stream_port,
        redis_ip=redis_ip,
        redis_port=redis_port
    )
    asyncio.run(stream_stove_data.stream())


if __name__ == '__main__':
    cli()
