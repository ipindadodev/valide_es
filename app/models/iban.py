from pydantic import BaseModel, Field
from pydantic.config import ConfigDict

class IbanRequest(BaseModel):
    value: str = Field(..., description="Número IBAN español a validar", json_schema_extra={"example": "ES9121000418450200051332"})

    model_config = ConfigDict(
        json_schema_extra={
            "examples": [
                {"value": "ES9121000418450200051332"}
            ]
        }
    )

class IbanResponse(BaseModel):
    valid: bool
    message: str
