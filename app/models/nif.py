from pydantic import BaseModel, Field

class NifRequest(BaseModel):
    value: str = Field(..., description="DNI, NIE o NIF a validar")

    class Config:
        json_schema_extra = {
            "example": {
                "value": "12345678Z"
            }
        }

class NifResponse(BaseModel):
    type: str
    valid: bool
    message: str
