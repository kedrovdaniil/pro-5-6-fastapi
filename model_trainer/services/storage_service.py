# import json
import os
import pickle

from model_trainer.serializers.models import MLModelEnum
from model_trainer.settings.config import MODELS_DIR

# SERVICE_STATE_DIR = 'memory'
# STATE_FILENAME = 'state.json'

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

# def read_from_state_file(key: str) -> str:
#     file_path = os.path.join(SERVICE_STATE_DIR, STATE_FILENAME)
#
#     if not os.path.exists(file_path):
#         init_state_file()
#
#     with open(file_path, "r") as f:
#         content = f.read()
#         json_content = json.loads(content) if content.strip() else {}
#         print('json_content:', json_content, type(json_content))
#
#         if key not in json_content:
#             raise KeyError(f"Key '{key}' not found in state file.")
#
#         return json_content[key]
#
# def write_to_state_file(key: str, value: str) -> None:
#     file_path = os.path.join(SERVICE_STATE_DIR, STATE_FILENAME)
#
#     if not os.path.exists(file_path):
#         init_state_file()
#
#     with open(file_path, "r+") as f:
#         content = f.read()
#         json_content = json.loads(content) if content.strip() else {}
#
#         json_content[key] = value
#
#         f.seek(0)  # Сбрасываем указатель в начало файла
#         f.truncate()  # Удаляем содержимое файла
#         f.write(json.dumps(json_content, indent=4))  # Записываем JSON
#
# def init_state_file():
#     file_path = os.path.join(SERVICE_STATE_DIR, STATE_FILENAME)
#
#     if not os.path.exists(SERVICE_STATE_DIR):
#         os.mkdir(SERVICE_STATE_DIR)
#
#     if not os.path.exists(file_path):
#         init_state = {
#             PROCESSES_COUNT: 1,
#             INFERENCE_MODELS: [],  # inference field. example: [{model_id: str, model: <loaded_model>}]
#         }
#
#         with open(file_path, "w", encoding="utf-8") as state_file:
#             json.dump(init_state, state_file, indent=4, ensure_ascii=False)
#
# def remove_state_file():
#     file_path = os.path.join(SERVICE_STATE_DIR, STATE_FILENAME)
#     os.remove(file_path)