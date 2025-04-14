from fastapi import APIRouter, HTTPException
from app.models.nif import NifRequest, NifResponse
from app.services.nif import validate_nif

router = APIRouter()

@router.post(
    "/",
    response_model=NifResponse,
    summary="Validar NIF/NIE/CIF",
    description="Valida un NIF, NIE o CIF español y devuelve su validez, tipo e información adicional.",
    responses={
        400: {
            "description": "Solicitud incorrecta. El valor no coincide con ningún formato válido de identificador español."
        }
    }
)
def validate_nif_endpoint(data: NifRequest):
    try:
        return validate_nif(data.value)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
