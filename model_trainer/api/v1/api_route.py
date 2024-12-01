from typing import Union, Dict

from fastapi import APIRouter
from http import HTTPStatus

from pydantic import BaseModel

models = {}

router = APIRouter()




class ModelListResponse(BaseModel):
    # Список словарей
    models:

# API endpoints
@router.post("/fit", status_code=HTTPStatus.CREATED)
async def fit(request:""):
    # Реализуйте логику обучения и сохранения модели.
    # Обратите внимание на формат входных данных.
    # Обучать Нужно логистическую и линейную регрессии.

@router.post("/load", response_model='')
async def load(request: LoadRequest):
    # Реализуйте загрузку обученной модели для инференса.
    # Загрузить можно ми минимум
    return

@router.get("/get_status")
async def get_status():
    # Получение списка  загруженных для инференса моделей
    return


@router.post("/unload", response_model=UnloadResponse)
async def unload(
):
    # Реализуйте апи выгружающее загруженную модель по id идентификатору модели.
    return

@router.post("/predict")
async def predict(request:):
    # Реализуйте инференс одной из загруженных моделей
    return

@router.get("/list_models", response_model='')
async def list_models():
    # Реализуйте получения списка обученных моделей
    return ModelListResponse()


@router.delete("/remove/{model_id}", response_model="")
async def remove():
    # Удаление обученной модели из списка по id модели
    return


# Реализуйте Delete метод remove_all