import logging
import sys
from pathlib import Path
from typing import Callable

import uvicorn
from fastapi_injector import attach_injector
from injector import Injector, Binder
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from loguru import logger

from main.core.configuration import Configuration
from main.core.container import container
from main.core.sample_container import sample_container
from main.dashboard.dashboard_controller import dashboard_router
from main.stove_state.stove_state_controller import stove_state_router
from main.temperature.temperature_controller import temperature_router


class HomePeriscope:
    application: FastAPI

    def __init__(self, configure: Callable[[Binder], None]):
        a_injector = Injector([configure])
        self.application = FastAPI()
        self.application.mount("/static", StaticFiles(directory=self.find_static_folder()), name="static")
        self.application.include_router(dashboard_router)
        self.application.include_router(temperature_router)
        self.application.include_router(temperature_router)
        self.application.include_router(stove_state_router)
        self.application.state.injector = a_injector
        attach_injector(self.application, a_injector)

    def find_static_folder(self) -> Path:
        return Path(__file__).parent.parent.parent.joinpath("static", "static")

    @classmethod
    def create_app(cls, configure: Callable[[Binder], None]) -> FastAPI:
        return cls(configure).application


configuration = Configuration()
if configuration.features.file_logging:
    default_logging_level: str = logging.getLevelName(logging.INFO)
    logger.remove()
    logger.add(
        sys.stdout,
        level=default_logging_level,
        colorize=True,
        format="{time} {level} {message}",
    )
    logger.add(
        "logs/home_periscope.log",
        rotation="24 hours",
        retention="3 days",
        level=default_logging_level,
        format="{time} {level} {message}",
    )

if configuration.features.demo_mode:
    application = HomePeriscope.create_app(sample_container)
else:
    application = HomePeriscope.create_app(container)


if __name__ == '__main__':
    uvicorn.run("home_periscope:application", host="0.0.0.0", port=5000, log_level="trace", reload=True)
