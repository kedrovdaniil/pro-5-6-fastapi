import asyncio
from typing import Any, Optional

# Константы
PROCESSES_COUNT = "processes_count"
INFERENCE_MODELS = "inference_models"

# Глобальный объект состояния
class ServiceState:
    def __init__(self):
        self.state = {
            PROCESSES_COUNT: 1,
            INFERENCE_MODELS: [], # inference field. example: [{model_id: str, model: <loaded_model>}]
        }

    def get_state(self) -> Any:
        return self.state

    def set_state(self, new_state: str) -> None:
        self.state = new_state

    def get_state_item(self, item_id: str, default: Optional[Any] = None) -> Any:
        return self.state[item_id] if item_id in self.state else default

    def set_state_item(self, item_id: str, value: Any) -> None:
        self.state[item_id] = value

service_state = ServiceState()
state_lock = asyncio.Lock()