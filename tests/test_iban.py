import unittest
import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from app.services.iban import validate_iban
from app.models.iban import IbanResponse


class TestIBANValidation(unittest.TestCase):

    def test_valid_iban(self):
        result = validate_iban("ES9121000418450200051332")  # IBAN válido
        self.assertIsInstance(result, IbanResponse)
        self.assertTrue(result.valid)
        self.assertEqual(result.message, "IBAN válido")

    def test_valid_iban_with_spaces(self):
        result = validate_iban("ES91 2100 0418 4502 0005 1332")
        self.assertTrue(result.valid)

    def test_valid_iban_with_hyphens(self):
        result = validate_iban("ES91-2100-0418-4502-0005-1332")
        self.assertTrue(result.valid)

    def test_invalid_iban_wrong_checksum(self):
        result = validate_iban("ES9121000418450200051333")  # último dígito mal
        self.assertFalse(result.valid)
        self.assertEqual(result.message, "IBAN no válido. Por favor, revise los datos introducidos.")

    def test_invalid_iban_wrong_country(self):
        result = validate_iban("FR1420041010050500013M02606")
        self.assertFalse(result.valid)
        self.assertEqual(result.message, "Solo se admite validación de IBAN españoles (ES).")

    def test_invalid_iban_short(self):
        result = validate_iban("ES91")
        self.assertFalse(result.valid)

    def test_invalid_iban_format(self):
        result = validate_iban("ES91-2100-04XX-4502-0005-1332")
        self.assertFalse(result.valid)

    def test_iban_with_lowercase(self):
        result = validate_iban("es9121000418450200051332")
        self.assertTrue(result.valid)

    def test_iban_with_leading_trailing_spaces(self):
        result = validate_iban("   ES9121000418450200051332   ")
        self.assertTrue(result.valid)

    def test_empty_iban(self):
        result = validate_iban("")
        self.assertFalse(result.valid)

if __name__ == "__main__":
    unittest.main()
