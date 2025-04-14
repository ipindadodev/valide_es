import re
from app.models.iban import IbanResponse

def validate_iban(value: str) -> IbanResponse:
    value = re.sub(r"[\s\-]", "", value.upper())

    if not value.startswith("ES"):
        return IbanResponse(
            valid=False,
            message="Solo se admite validación de IBAN españoles (ES)."
        )

    if len(value) != 24:
        return IbanResponse(
            valid=False,
            message="IBAN no válido. Debe tener 24 caracteres y comenzar por 'ES'."
        )

    if not re.fullmatch(r"ES\d{22}", value):
        return IbanResponse(
            valid=False,
            message="IBAN no válido. El formato debe ser ES seguido de 22 dígitos."
        )

    # Mover los 4 primeros caracteres al final
    rearranged = value[4:] + value[:4]

    # Convertir letras a números (A=10, ..., Z=35)
    numeric = ""
    for char in rearranged:
        numeric += str(ord(char) - 55) if char.isalpha() else char

    # Validación por módulo 97
    is_valid = int(numeric) % 97 == 1

    return IbanResponse(
        valid=is_valid,
        message="IBAN válido" if is_valid else "IBAN no válido. Por favor, revise los datos introducidos."
    )