import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel, ConfigDict

app = FastAPI(
    title="model_trainer",
    docs_url="/api/openapi",
    openapi_url="/api/openapi.json",
)


class StatusResponse(BaseModel):
    status: str

    model_config = ConfigDict(
        json_schema_extra={"examples": [{"status": "App healthy"}]}
    )
@app.get("/")
async def root():
    # Реализуйте метод получения информации о статусе сервиса.
    return


## Реализуйте роутер с префиксом /api/v1/models
app.include_router()

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)