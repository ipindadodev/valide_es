import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from app.services.nif import validate_nif
from app.models.nif import NifResponse

class TestNIFValidation(unittest.TestCase):

    def test_valid_dni(self):
        result = validate_nif("12345678Z")
        self.assertEqual(result.type, "DNI")
        self.assertTrue(result.valid)

    def test_invalid_dni(self):
        result = validate_nif("12345678A")
        self.assertEqual(result.type, "DNI")
        self.assertFalse(result.valid)

    def test_valid_nie(self):
        result = validate_nif("X1234567L")
        self.assertEqual(result.type, "NIE")
        self.assertTrue(result.valid)

    def test_invalid_nie(self):
        result = validate_nif("Z1234567A")
        self.assertEqual(result.type, "NIE")
        self.assertFalse(result.valid)

    def test_valid_cif_digit(self):
        result = validate_nif("A58818501")
        self.assertEqual(result.type, "NIF empresa")
        self.assertTrue(result.valid)

    def test_valid_cif_letter(self):
        result = validate_nif("P2807900B")
        self.assertEqual(result.type, "NIF empresa")
        self.assertTrue(result.valid)

    def test_valid_cif_with_hyphens(self):
        result = validate_nif("A-5881850-1")
        self.assertEqual(result.type, "NIF empresa")
        self.assertTrue(result.valid)

    def test_valid_dni_with_hyphens(self):
        result = validate_nif("1234-5678-Z")
        self.assertEqual(result.type, "DNI")
        self.assertTrue(result.valid)

    def test_valid_nie_with_spaces(self):
        result = validate_nif("   y1234567x ")
        self.assertEqual(result.type, "NIE")
        self.assertTrue(result.valid)

    def test_invalid_format(self):
        with self.assertRaises(ValueError):
            validate_nif("ABC123")

if __name__ == "__main__":
    unittest.main()
