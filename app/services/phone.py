# app/services/phone.py
import re
from app.models.phone import PhoneResponse

def validate_phone(value: str) -> PhoneResponse:
    # Eliminar espacios, guiones, puntos y paréntesis
    cleaned = re.sub(r"[\s\-.()]+", "", value)

    # Eliminar prefijo internacional válido
    if cleaned.startswith("+034"):
        cleaned = cleaned[4:]
    elif cleaned.startswith("+34"):
        cleaned = cleaned[3:]
    elif cleaned.startswith("034"):
        cleaned = cleaned[3:]
    elif cleaned.startswith("34"):
        cleaned = cleaned[2:]

    # Comprobar longitud y tipo de número
    if not re.fullmatch(r"[6789]\d{8}", cleaned):
        return PhoneResponse(
            type="desconocido",
            valid=False,
            message="Teléfono no válido. Debe ser un número nacional de 9 cifras que empiece por 6, 7, 8 o 9."
        )

    tipo = "móvil" if cleaned.startswith(("6", "7")) else "fijo"

    return PhoneResponse(
        type=tipo,
        valid=True,
        message=f"Teléfono {tipo} válido"
    )