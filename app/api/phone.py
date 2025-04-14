from fastapi import APIRouter, HTTPException
from app.models.phone import PhoneRequest, PhoneResponse
from app.services.phone import validate_phone

router = APIRouter()

@router.post(
    "/",
    response_model=PhoneResponse,
    summary="Validar número de teléfono",
    description="Valida un número de teléfono español (móvil o fijo) y devuelve su validez, tipo e información adicional.",
    responses={
        400: {
            "description": "Solicitud incorrecta. El valor no es un número de teléfono válido."
        }
    }
)
def validate_phone_endpoint(data: PhoneRequest):
    try:
        return validate_phone(data.value)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
