from injector import Binder

from main.stove_state.stove_state_repository import IStoveStateRepository
from main.temperature.heating_temperature_repository import IHeatingTemperatureRepository
from main.temperature.mixer_temperature_repository import IMixerTemperatureRepository
from main.temperature.water_heater_temperature_repository import IWaterHeaterTemperatureRepository
from main.flame_size.flame_size_repository import IFlameSizeRepository
from main.summer_mode.summer_mode_repository import ISummerModeRepository
from sample.heating_temperature_sample_repository import HeatingTemperatureSampleRepository
from sample.mixer_temperature_sample_repository import MixerTemperatureSampleRepository
from sample.stove_state_sample_repository import StoveStateSampleRepository
from sample.water_heater_sample_temperature_repository import WaterHeaterTemperatureSampleRepository
from sample.flame_size_sample_repository import FlameSizeSampleRepository
from sample.summer_mode_sample_repository import SummerModeSampleRepository


def sample_container(binder: Binder) -> None:
    binder.bind(IMixerTemperatureRepository, to=MixerTemperatureSampleRepository)  # type: ignore[type-abstract]
    binder.bind(IWaterHeaterTemperatureRepository, to=WaterHeaterTemperatureSampleRepository)  # type: ignore[type-abstract]
    binder.bind(IHeatingTemperatureRepository, to=HeatingTemperatureSampleRepository)  # type: ignore[type-abstract]
    binder.bind(IStoveStateRepository, to=StoveStateSampleRepository)  # type: ignore[type-abstract]
    binder.bind(IFlameSizeRepository, to=FlameSizeSampleRepository)  # type: ignore[type-abstract]
    binder.bind(ISummerModeRepository, to=SummerModeSampleRepository)  # type: ignore[type-abstract]
