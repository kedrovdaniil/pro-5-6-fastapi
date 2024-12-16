from typing import Union, Dict, Any

from fastapi import APIRouter
from http import HTTPStatus

from model_trainer.serializers.models import FitRequest, LoadRequest, FitResponse, RemoveAllResponse, RemoveResponse, \
    PredictRequest, UnloadResponse, PredictionResponse, LoadResponse, GetStatusResponse, ListModelsResponse, \
    UnloadRequest
from model_trainer.services.ml_models_service import fit_model, load_model, remove_all_models, remove_model, \
    unload_model, get_status_models, get_list_models, predict_model

router = APIRouter()

# API endpoints
@router.post("/fit", status_code=HTTPStatus.CREATED)
async def fit(request: FitRequest):
    # Реализуйте логику обучения и сохранения модели.
    # Обратите внимание на формат входных данных.
    # Обучать Нужно логистическую и линейную регрессии.
    return fit_model(request)

@router.post("/load", response_model=LoadResponse)
async def load(request: LoadRequest):
    # Реализуйте загрузку обученной модели для инференса.
    # Загрузить можно ми минимум
    return load_model(request)

@router.get("/get_status", response_model=GetStatusResponse)
async def get_status():
    return get_status_models()


@router.post("/unload", response_model=UnloadResponse)
async def unload(request: UnloadRequest):
    # Реализуйте апи выгружающее загруженную модель по id идентификатору модели.
    return unload_model(request)

@router.post("/predict", response_model=PredictionResponse)
async def predict(request: PredictRequest):
    # Реализуйте инференс одной из загруженных моделей
    return predict_model(request)

@router.get("/list_models", response_model=ListModelsResponse)
async def list_models():
    # Реализуйте получения списка обученных моделей
    # return ModelListResponse()
    return get_list_models()

@router.delete("/remove/{model_id}", response_model=RemoveResponse)
async def remove(model_id: str):
    # Удаление обученной модели из списка по id модели
    return remove_model(model_id)

# Реализуйте Delete метод remove_all
@router.delete("/remove_all", response_model=RemoveAllResponse)
async def remove_all():
    return remove_all_models()