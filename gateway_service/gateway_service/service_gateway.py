from fastapi import APIRouter, status, HTTPException
from fastapi.responses import JSONResponse
from typing import List, Dict
from loguru import logger
import requests


gateway_router = APIRouter(prefix="/models", tags=["models"])

SERVICES = ['service_1', 'service_2']
VERSION_STR: str = "v1"
BASE_URL: str = f"/api/{VERSION_STR}"

# the names should correspond to Kubernetes services
SERVICE_TO_HOST_MAP={'service_1': "http://ml-service1",
                     'service_2': "http://ml-service2"}


@gateway_router.on_event("startup")
async def on_startup() -> None:
    """Actions on starting up the service

    Returns
    -------

    """

    # make checks

    logger.info("Start-up for gateway_service...")
    logger.info("Done...")


@gateway_router.get("/",
                    response_model=Dict[str, str])
def root() -> JSONResponse:
    return JSONResponse(status_code=status.HTTP_200_OK,
                        content={"message": "Hello from Kubernetes 101 gateway_service"})


@gateway_router.get(
    "/services",
    summary="Returns a list of the available models",
    response_model=List[str],
)
async def get_services() -> JSONResponse:
    """

    Parameters
    ----------
    Returns
    -------

    JSONResponse with a list of the available service
    """

    return JSONResponse(status_code=status.HTTP_200_OK,
                        content=["service_1", "service_1"])


@gateway_router.get("/services/{service_name}")
async def get_service(service_name: str) -> JSONResponse:

    """Returns a prediction about the given image

    Parameters
    ----------
    service_name: The service name to forward the call

    Returns
    -------

    JSONResponse
    """

    if service_name not in SERVICES:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail=f"Service name {service_name} not in {SERVICES}")

    if service_name == 'service_1':
        service_id = 'service-1'
    elif service_name == 'service_2':
        service_id = 'service-2'


    url = f'{SERVICE_TO_HOST_MAP[service_name]}{BASE_URL}/{service_id}'

    print(f"Service URL accessed {url}")
    response = requests.get(url=url)
    return response.json()

