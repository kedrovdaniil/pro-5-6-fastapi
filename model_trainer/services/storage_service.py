import os
import pickle
import re

from model_trainer.serializers.models import MLModelEnum
from model_trainer.settings.config import MODELS_DIR

def load_models_from_dir():
    filenames = [
        os.path.splitext(file)[0]
        for file in os.listdir(MODELS_DIR)
        if os.path.isfile(os.path.join(MODELS_DIR, file))
    ]
    return filenames

def save_model_to_dir(model: MLModelEnum, model_id: str, type: str):
    model_path = os.path.join(MODELS_DIR, f"{model_id}.pkl")
    with open(model_path, "wb") as f:
        pickle.dump(model, f)

def remove_model_from_dir(model_id: str):
    model_path = os.path.join(MODELS_DIR, f"{model_id}.pkl")

    if os.path.isfile(model_path):
        os.remove(model_path)
    else:
        raise FileNotFoundError