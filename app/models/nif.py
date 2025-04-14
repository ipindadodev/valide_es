from pydantic import BaseModel, Field
from pydantic.config import ConfigDict

class NifRequest(BaseModel):
    value: str = Field(..., json_schema_extra={"example": "12345678Z"}, description="DNI, NIE o NIF a validar")

    model_config = ConfigDict(
        json_schema_extra={
            "examples": [{"value": "12345678Z"}]
        }
    )

class NifResponse(BaseModel):
    type: str
    valid: bool
    message: str
