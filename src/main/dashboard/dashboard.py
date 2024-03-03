from fastapi_utils.cbv import cbv

from fastapi import Request
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory='static')

from fastapi_utils.inferring_router import InferringRouter

dashboard_router = InferringRouter(tags=["DashboardController"])


@cbv(dashboard_router)
class DashboardController:

    @dashboard_router.get("/")
    async def main(self, request: Request):
        result = "Enter your name"
        breakpoint()
        return templates.TemplateResponse(
            "index.html", context={"request": request, "result": result}
        )
