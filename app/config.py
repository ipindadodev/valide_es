import os
from pydantic import BaseModel
from functools import lru_cache

class Settings(BaseModel):
    app_name: str = "Valide.es API"
    version: str = "1.0.0"
    debug: bool = os.getenv("DEBUG", "false").lower() == "true"
    allowed_hosts: list[str] = ["*"]
    docs_url: str = "/docs"
    openapi_url: str = "/openapi.json"

@lru_cache()
def get_settings():
    return Settings()

