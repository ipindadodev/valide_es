from fastapi import APIRouter, HTTPException
from app.models.iban import IbanRequest, IbanResponse
from app.services.iban import validate_iban

router = APIRouter()

@router.post(
    "/",
    response_model=IbanResponse,
    summary="Validar IBAN español",
    description="Valida un número IBAN con prefijo 'ES' y estructura válida según la normativa SEPA.",
    responses={
        400: {"description": "Solicitud incorrecta. El IBAN proporcionado no es válido."}
    }
)
def validate_iban_endpoint(data: IbanRequest):
    try:
        return validate_iban(data.value)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
