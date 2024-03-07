from fastapi import Request

from attrs import asdict
from fastapi_injector import Injected
from fastapi_utils.cbv import cbv
from fastapi_utils.inferring_router import InferringRouter

from main.temperature.heating_temperature_repository import HeatingTemperatureRepository
from main.temperature.temperature import Temperature

temperature_router = InferringRouter(tags=["DashboardController"])


@cbv(temperature_router)
class TemperatureController:
    heating_temperature_repository: HeatingTemperatureRepository = Injected(HeatingTemperatureRepository)


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
