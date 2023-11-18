from fastapi import APIRouter, status
from fastapi.responses import JSONResponse
from typing import Dict
from loguru import logger


service_2_router = APIRouter(prefix="/service-2", tags=["models"])


@service_2_router.on_event("startup")
async def on_startup() -> None:
    """Actions on starting up the service
    Returns
    -------
    """
    logger.info("Start-up for service_2...")
    logger.info("Done...")


@service_2_router.get("/")
def root() -> JSONResponse:
    return JSONResponse(status_code=status.HTTP_200_OK,
                        content={"message": "Hello from Kubernetes 101 service_2"})


@service_2_router.get(
    "/service-2",
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
                        content={"message": "Hello from service-2"})




