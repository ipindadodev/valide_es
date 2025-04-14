from fastapi import FastAPI
from app.api import nif

app = FastAPI(
    title="Valide.es API",
    description="Validación de identificadores comunes españoles (NIF, CIF, IBAN, teléfono, CP)",
    version="1.0.0",
)

app.include_router(nif.router, prefix="/nif", tags=["NIF/DNI/NIE"])
app.include_router(nif.router, prefix="/iban", tags=["IBAN"])
app.include_router(nif.router, prefix="/telefono", tags=["Teléfono"])
app.include_router(nif.router, prefix="/cp", tags=["Código postal"])
@app.get("/")
async def root():
    return {"message": "Welcome to the Valide.es API! Check the documentation at /docs"}
    