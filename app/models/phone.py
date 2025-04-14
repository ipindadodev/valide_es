from pydantic import BaseModel, Field
from pydantic.config import ConfigDict

class PhoneRequest(BaseModel):
    value: str = Field(
        ...,
        description="Número de teléfono nacional español (fijo o móvil). Acepta los siguientes formatos:\n"
                    "- 612345678\n"
                    "- 612 345 678\n"
                    "- 612-345-678\n"
                    "- +34 612345678\n"
                    "- +34 612-345-678\n"
                    "- 034612345678\n"
                    "- 34.612.345.678"
    )

    model_config = ConfigDict(
        json_schema_extra={
            "examples": [
                {"value": "612345678"},
                {"value": "612 345 678"},
                {"value": "612-345-678"},
                {"value": "+34 612345678"},
                {"value": "+34 612-345-678"},
                {"value": "034612345678"},
                {"value": "34.612.345.678"},
            ]
        }
    )

class PhoneResponse(BaseModel):
    type: str
    valid: bool
    message: str
