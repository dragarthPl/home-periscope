from pathlib import Path

import uvicorn
from fastapi_injector import attach_injector
from injector import Injector
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from main.dashboard.dashboard_controller import dashboard_router
from main.temperature.heating_temperature_repository import IHeatingTemperatureRepository, HeatingTemperatureRepository
from main.temperature.mixer_temperature_repository import IMixerTemperatureRepository, MixerTemperatureRepository
from main.temperature.temperature_controller import temperature_router
from main.temperature.water_heater_temperature_repository import IWaterHeaterTemperatureRepository, \
    WaterHeaterTemperatureRepository


def configure(binder):
    binder.bind(IMixerTemperatureRepository, to=MixerTemperatureRepository)
    binder.bind(IWaterHeaterTemperatureRepository, to=WaterHeaterTemperatureRepository)
    binder.bind(IHeatingTemperatureRepository, to=HeatingTemperatureRepository)


class HomePeriscope:
    app: FastAPI

    def __init__(self, configure):
        a_injector = Injector([configure])
        self.app = FastAPI()
        self.app.mount("/static", StaticFiles(directory=self.find_static_folder()), name="static")
        self.app.include_router(dashboard_router)
        self.app.include_router(temperature_router)
        self.app.state.injector = a_injector
        attach_injector(self.app, a_injector)

    def find_static_folder(self):
        return Path(__file__).parent.parent.parent.joinpath("static", "static")

    @classmethod
    def create_app(cls, configure) -> FastAPI:
        return cls(configure).app


app = HomePeriscope.create_app(configure)


if __name__ == '__main__':
    uvicorn.run("home_periscope:app", host="0.0.0.0", port=5000, log_level="trace", reload=True)
