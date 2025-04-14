import re
from app.models.nif import NifResponse

def validate_nif(value: str) -> NifResponse:
    value = _sanitize_identifier(value)

    if re.fullmatch(r"\d{8}[A-Z]", value):
        return _validate_dni(value)
    if re.fullmatch(r"[XYZ]\d{7}[A-Z]", value):
        return _validate_nie(value)
    if re.fullmatch(r"[ABCDEFGHJKLMNPQRSUVW]\d{7}[0-9A-J]", value):
        return _validate_business_nif(value)

    raise ValueError("Formato de NIF no reconocido")

def _sanitize_identifier(identifier: str) -> str:
    return re.sub(r"[^A-Z0-9]", "", identifier.upper().strip())

def _validate_dni(dni: str) -> NifResponse:
    valid_letters = "TRWAGMYFPDXBNJZSQVHLCKE"
    number = int(dni[:-1])
    correct_letter = valid_letters[number % 23]
    is_valid = correct_letter == dni[-1]
    return NifResponse(
        type="DNI",
        valid=is_valid,
        message="DNI válido" if is_valid else "DNI no válido. Por favor, revise los datos introducidos."
    )

def _validate_nie(nie: str) -> NifResponse:
    mapping = {'X': '0', 'Y': '1', 'Z': '2'}
    numeric = mapping[nie[0]] + nie[1:-1]
    correct_letter = "TRWAGMYFPDXBNJZSQVHLCKE"[int(numeric) % 23]
    is_valid = correct_letter == nie[-1]
    return NifResponse(
        type="NIE",
        valid=is_valid,
        message="NIE válido" if is_valid else "NIE no válido. Por favor, revise los datos introducidos."
    )

def _validate_business_nif(nif: str) -> NifResponse:
    control_letter_table = "JABCDEFGHI"
    first_letter = nif[0]
    digits = nif[1:-1]
    control_char = nif[-1]

    if not digits.isdigit() or len(digits) != 7:
        return NifResponse(
            type="NIF empresa",
            valid=False,
            message="NIF de empresa no válido. Por favor, revise los datos introducidos."
        )

    # Suma de posiciones pares
    even_sum = sum(int(digits[i]) for i in range(1, 7, 2))

    # Suma de posiciones impares tras multiplicar por 2 y sumar dígitos
    odd_sum = 0
    for i in range(0, 7, 2):
        double = int(digits[i]) * 2
        odd_sum += double if double < 10 else double - 9

    total = even_sum + odd_sum
    control_digit = (10 - (total % 10)) % 10
    expected_letter = control_letter_table[control_digit]
    expected_digit = str(control_digit)

    if first_letter in "PQRSNW":  # Solo letra
        is_valid = control_char == expected_letter
    elif first_letter in "ABEH":  # Solo dígito
        is_valid = control_char == expected_digit
    else:  # Ambos posibles
        is_valid = control_char == expected_letter or control_char == expected_digit

    return NifResponse(
        type="NIF empresa",
        valid=is_valid,
        message="NIF de empresa válido" if is_valid else "NIF de empresa no válido. Por favor, revise los datos introducidos."
    )

