from contextlib import asynccontextmanager
from pathlib import Path

import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel, ConfigDict
from fastapi.middleware.cors import CORSMiddleware

from model_trainer.api.v1.api_route import router
from model_trainer.services.storage_service import load_models_from_dir
from model_trainer.settings.config import MODELS_DIR

@asynccontextmanager
async def lifespan(app: FastAPI):
    load_models_from_dir()
    yield

app = FastAPI(
    title="model_trainer",
    docs_url="/api/openapi",
    openapi_url="/api/openapi.json",
    lifespan=lifespan
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

Path(MODELS_DIR).mkdir(parents=True, exist_ok=True)

class StatusResponse(BaseModel):
    status: str

    model_config = ConfigDict(
        json_schema_extra={"examples": [{"status": "App healthy"}]}
    )
@app.get("/")
async def root() -> StatusResponse:
    # Реализуйте метод получения информации о статусе сервиса.
    return StatusResponse(status="App healthy")

## Реализуйте роутер с префиксом /api/v1/models
app.include_router(prefix="/api/v1/models", router=router)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)