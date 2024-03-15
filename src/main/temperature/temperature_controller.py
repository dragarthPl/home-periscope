from fastapi import Request

from attrs import asdict
from fastapi_injector import Injected
from fastapi_utils.cbv import cbv
from fastapi_utils.inferring_router import InferringRouter

from main.temperature.heating_temperature_repository import IHeatingTemperatureRepository
from main.temperature.mixer_temperature_repository import IMixerTemperatureRepository
from main.temperature.temperature import Temperature
from main.temperature.water_heater_temperature_repository import IWaterHeaterTemperatureRepository

temperature_router = InferringRouter(tags=["DashboardController"])


@cbv(temperature_router)
class TemperatureController:
    heating_temperature_repository: IHeatingTemperatureRepository = Injected(IHeatingTemperatureRepository)
    water_heater_temperature_repository: IWaterHeaterTemperatureRepository = Injected(IWaterHeaterTemperatureRepository)
    mixer_temperature_repository: IMixerTemperatureRepository = Injected(IMixerTemperatureRepository)

    @temperature_router.get("/api/heating_temperature")
    async def heating_temperature(self, request: Request):
        temperature: Temperature = await self.heating_temperature_repository.get_temperature()
        if temperature:
            return asdict(temperature)
        else:
            return {
                "current": None,
                "max_temperature": None,
                "min_temperature": None,
            }

    @temperature_router.get("/api/water_heater_temperature")
    async def water_heater_temperature(self, request: Request):
        temperature: Temperature = await self.water_heater_temperature_repository.get_temperature()
        if temperature:
            return asdict(temperature)
        else:
            return {
                "current": None,
                "max_temperature": None,
                "min_temperature": None,
            }

    @temperature_router.get("/api/mixer_temperature")
    async def mixer_temperature(self, request: Request):
        temperature: Temperature = await self.mixer_temperature_repository.get_temperature()
        if temperature:
            return asdict(temperature)
        else:
            return {
                "current": None,
                "max_temperature": None,
                "min_temperature": None,
            }