import uvicorn
from fastapi_injector import attach_injector
from injector import Injector
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from dashboard.dashboard import dashboard_router


def configure(binder):
    pass


class HomePeriscope:
    app: FastAPI

    def __init__(self):
        a_injector = Injector([configure])
        self.app = FastAPI()
        self.app.mount("/static", StaticFiles(directory="static/static"), name="static")
        self.app.include_router(dashboard_router)
        self.app.state.injector = a_injector
        attach_injector(self.app, a_injector)

    @classmethod
    def create_app(cls) -> FastAPI:
        return cls().app


app = HomePeriscope().create_app()


if __name__ == '__main__':
    uvicorn.run("home_periscope:app", host="0.0.0.0", port=5000, log_level="trace", reload=True)
