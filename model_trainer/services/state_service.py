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
            INFERENCE_MODELS: [], # example: [{model_id: str, model: <loaded_model>}]
        }

    def _get_state(self) -> dict:
        return dict(self.state)

    def _set_state(self, new_state: Any) -> None:
        self.state.clear()
        self.state.update(new_state)

    def get_state_item(self, item_id: str, default: Optional[Any] = None) -> Any:
        return self.state[item_id] if item_id in self.state else default
        # value = read_from_state_file(item_id)
        # print('get_state_item value:', value)
        # return value if value is not None else default

    def set_state_item(self, item_id: str, value: Any) -> None:
        self.state[item_id] = value
        # print('set_state_item item_id, value:', item_id, value)
        # write_to_state_file(item_id, value)

# state_lock = asyncio.Lock()
service_state = ServiceState()

