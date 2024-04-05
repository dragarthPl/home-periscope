from redis import Redis
from injector import Binder

from main.core.configuration import Configuration
from main.stove_state.stove_state_repository import StoveStateRepository, IStoveStateRepository
from main.temperature.heating_temperature_repository import IHeatingTemperatureRepository, HeatingTemperatureRepository
from main.temperature.mixer_temperature_repository import IMixerTemperatureRepository, MixerTemperatureRepository
from main.temperature.water_heater_temperature_repository import IWaterHeaterTemperatureRepository, \
    WaterHeaterTemperatureRepository


def container(binder: Binder) -> None:
    configuration = Configuration()
    binder.bind(IMixerTemperatureRepository, to=MixerTemperatureRepository)  # type: ignore[type-abstract]
    binder.bind(IWaterHeaterTemperatureRepository, to=WaterHeaterTemperatureRepository)  # type: ignore[type-abstract]
    binder.bind(IHeatingTemperatureRepository, to=HeatingTemperatureRepository)  # type: ignore[type-abstract]
    binder.bind(IStoveStateRepository, to=StoveStateRepository)  # type: ignore[type-abstract]
    binder.bind(Redis, to=Redis(host=configuration.redis_ip, port=configuration.redis_port, decode_responses=True))  # type: ignore[type-abstract]
