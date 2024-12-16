from enum import Enum
from typing import Any

from pydantic import BaseModel


class MLModelEnum(str, Enum):
    linear = "linear"
    logistic = "logistic"

class ModelConfig(BaseModel):
    id: str
    ml_model_type: MLModelEnum
    hyperparameters: dict[str, Any] # ???

class FitRequest(BaseModel):
    X: Any
    y: Any
    config: Any # ModelConfig

class FitResponse(BaseModel):
    message: str

class PredictRequest(BaseModel):
    id: str
    X: list[list[float]]

class PredictionResponse(BaseModel):
    predictions: list[float]

class LoadRequest(BaseModel):
    id: str

class LoadResponse(BaseModel):
    message: str

class UnloadRequest(BaseModel):
    id: str

class UnloadResponse(BaseModel):
    message: str

class GetStatusResponse(BaseModel):
    status: str

class ListModelsResponse(BaseModel):
    models: list[Any]

class RemoveRequest(BaseModel):
    model_id: str

class RemoveResponse(BaseModel):
    message: str

class RemoveAllResponse(BaseModel):
    message: str