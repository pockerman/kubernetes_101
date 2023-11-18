from fastapi import APIRouter, status
from fastapi.responses import JSONResponse
from typing import Dict
from loguru import logger


service_1_router = APIRouter(prefix="/service-1", tags=["models"])


@service_1_router.on_event("startup")
async def on_startup() -> None:
    """Actions on starting up the service

    Returns
    -------
    """
    logger.info("Start-up for service_1...")
    logger.info("Done...")


@service_1_router.get("/")
def root()->JSONResponse:
    return JSONResponse(status_code=status.HTTP_200_OK,
                        content={"message": "Hello from Kubernetes 101 service_1"})


@service_1_router.get(
    "/service-1",
    response_model=Dict[str, str],
)
async def get_service() -> JSONResponse:
    """

    Parameters
    ----------
    Returns
    -------

    JSONResponse
    """

    return JSONResponse(status_code=status.HTTP_200_OK,
                        content={"message": "Hello from service-1"})




