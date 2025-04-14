from fastapi import APIRouter
from fastapi.responses import JSONResponse

router = APIRouter()

@router.get(
    "/",
    summary="Estado del servicio",
    description="Comprueba si el microservicio está en funcionamiento.",
    response_description="OK si el servicio responde correctamente.",
)
def health_check():
    return JSONResponse(
        status_code=200,
        content={
            "status": "ok",
            "service": "Valide.es API",
            "message": "El servicio está funcionando correctamente."
        }
    )
