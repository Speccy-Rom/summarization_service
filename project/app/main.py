from fastapi import FastAPI, Depends

from .config import get_settings, Settings

app = FastAPI()


@app.get("/ping")
def pong(settings: Settings = Depends(get_settings)):
    return {
        "ping": "pong!",
        "environment": settings.environment,
        "testing": settings.testing
    }
