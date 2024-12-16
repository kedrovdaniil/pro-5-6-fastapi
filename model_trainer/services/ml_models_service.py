import os
import pickle
import shutil
import time as t

from fastapi import HTTPException
from sklearn.linear_model import LinearRegression, LogisticRegression

from model_trainer.serializers.exceptions import PredictException
from model_trainer.serializers.models import FitRequest, FitResponse, LoadRequest, LoadResponse, PredictRequest, \
    PredictionResponse, UnloadRequest, UnloadResponse, GetStatusResponse, ListModelsResponse, RemoveResponse, \
    RemoveAllResponse
from model_trainer.services.state_service import service_state, INFERENCE_MODELS
from model_trainer.services.storage_service import save_model_to_dir, remove_model_from_dir, load_models_from_dir
from model_trainer.settings.config import MODELS_DIR, MAX_INFERENCE_MODELS

def fit_model(request: FitRequest) -> FitResponse:
    ml_model_type = request.config.get('ml_model_type')
    X = request.X
    y = request.y
    model_id = request.config.get('id')
    hyperparameters = request.config.get('hyperparameters')

    model_path = os.path.join(MODELS_DIR, f"{model_id}.pkl")

    if os.path.exists(model_path):
        raise HTTPException(status_code=422, detail="Model ID already exists.")

    if ml_model_type == "linear":
        model = LinearRegression(**hyperparameters)
        model_type = "LinearRegression"
    elif ml_model_type == "logistic":
        model = LogisticRegression(**hyperparameters)
        model_type = "LogisticRegression"
    else:
        raise HTTPException(status_code=422, detail="Unsupported model type.")

    learned_model = model.fit(X, y)

    # save to storage
    save_model_to_dir(learned_model, model_id, model_type)

    t.sleep(60)

    return FitResponse(message=f"Model '{model_id}' trained and saved.")

def load_model(request: LoadRequest):
    model_id = request.id

    inference_models = service_state.get_state_item(INFERENCE_MODELS)
    model_path = os.path.join(MODELS_DIR, f"{model_id}.pkl")

    if any(m.get('model_id') == model_id for m in inference_models):
        raise HTTPException(status_code=422, detail="Model already loaded.")

    if len(inference_models) >= MAX_INFERENCE_MODELS:
        raise HTTPException(status_code=422, detail="Max inference models loaded.")

    if not os.path.exists(model_path):
        raise HTTPException(status_code=422, detail="Model not found.")

    with open(model_path, "rb") as f:
        inference_models.append({'model_id': model_id, 'model': pickle.load(f)})

    return LoadResponse(message=f"Model '{model_id}' loaded for inference.")

def predict_model(request: PredictRequest):
    model_id = request.id
    X = request.X

    inference_models = service_state.get_state_item(INFERENCE_MODELS)
    if not inference_models:
        raise HTTPException(status_code=422, detail="No models loaded.")

    model_obj = next(filter(lambda m: m.get('model_id') == model_id, inference_models), None)
    if model_obj is None:
        raise HTTPException(status_code=422, detail=f"Model with id '{model_id}' not found in memory.")

    model = model_obj.get('model')

    try:
        predictions = model.predict(X)
    except Exception as e:
        raise PredictException(msg=str(e), type="prediction_error")

    return PredictionResponse(predictions=predictions.tolist())

def unload_model(request: UnloadRequest):
    model_id = request.id

    inference_models = service_state.get_state_item(INFERENCE_MODELS)

    model = next(filter(lambda m: m.get('model_id') == model_id, inference_models), None)
    if model is None:
        raise HTTPException(status_code=422, detail=f"Model with id '{model_id}' was not loaded.")

    # filter model
    new_inference_models = list(filter(lambda m: m.get('model_id') != model_id, inference_models))

    # update state
    service_state.set_state_item(INFERENCE_MODELS, new_inference_models)

    return UnloadResponse(message=f"Model '{model_id}' unloaded.")

def get_status_models():
    inference_models = service_state.get_state_item(INFERENCE_MODELS)

    if not inference_models:
        return GetStatusResponse(status="No models loaded.")

    status_message = f"Models: {list(map(lambda m: m.get('model_id'), inference_models))}"
    return GetStatusResponse(status=status_message)

def get_list_models():
    return ListModelsResponse(models=load_models_from_dir())

def remove_model(model_id: str):
    # проверяем и удаляем модель из инференс зоны
    inference_models = service_state.get_state_item(INFERENCE_MODELS)

    model_with_id_exists_in_inference = len(list(map(lambda m: m.get('model_id') == model_id, inference_models))) > 0
    if model_with_id_exists_in_inference:
        service_state.set_state_item(INFERENCE_MODELS, filter(lambda m: m.get('model_id') != model_id, inference_models))

    # удаляем модель из storage
    remove_model_from_dir(model_id)

    return RemoveResponse(message=f"Model '{model_id}' removed")

def remove_all_models():
    for filename in os.listdir(MODELS_DIR):
        file_path = os.path.join(MODELS_DIR, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))

    service_state.set_state_item(INFERENCE_MODELS, [])

    return RemoveAllResponse(message="All models removed.")