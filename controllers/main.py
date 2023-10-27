import os
import pydantic
from helpers.sum import sum

PROJECT_NAME = os.getenv("PROJECT_NAME")

class GenericMessageResponse(pydantic.BaseModel):
    message: str

class HealthCheckResponse(pydantic.BaseModel):
    status: str

class SumRequest(pydantic.BaseModel):
    firstValue: int
    secondValue: int

class SumResponse(pydantic.BaseModel):
    value: int

def publicRoute() -> GenericMessageResponse:
    return { "message": f"Public Route {PROJECT_NAME}." }

def healthCheck() -> HealthCheckResponse:
    return { "status": "UP" }

def handleSum(body: SumRequest) -> SumResponse:
    value = sum(body.firstValue, body.secondValue)
    return { "value": value }