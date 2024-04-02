
from fastapi_utils.cbv import cbv

from fastapi import Request
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory='static')

from fastapi_utils.inferring_router import InferringRouter

dashboard_router = InferringRouter(tags=["DashboardController"])


@cbv(dashboard_router)
class DashboardController:

    @dashboard_router.get("/")
    async def main(self, request: Request):  # type: ignore[no-untyped-def]
        result = "Enter your name"
        return templates.TemplateResponse(
            "index.html", context={"request": request, "result": result}
        )
