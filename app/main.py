from fastapi import FastAPI
from app.api.nif import router as nif_router
from app.api.iban import router as iban_router
from app.api.phone import router as phone_router



app = FastAPI(
    title="Valide.es API",
    description="Validación de identificadores comunes españoles (NIF, CIF, IBAN, teléfono, CP)",
    version="1.0.0",
)

# Routers registrados correctamente
app.include_router(nif_router, prefix="/nif", tags=["NIF/DNI/NIE"])
app.include_router(iban_router, prefix="/iban", tags=["IBAN"])
app.include_router(phone_router, prefix="/phone", tags=["Teléfono"])

@app.get("/")
async def root():
    return {
        "message": "Bienvenido a la API de Valide.es. Accede a la documentación interactiva en /docs"
    }
