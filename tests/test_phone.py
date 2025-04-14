import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from app.services.phone import validate_phone
from app.models.phone import PhoneResponse

class TestPhoneValidation(unittest.TestCase):

    def test_valid_mobile_plain(self):
        result = validate_phone("612345678")
        self.assertTrue(result.valid)
        self.assertEqual(result.type, "móvil")

    def test_valid_landline_plain(self):
        result = validate_phone("912345678")
        self.assertTrue(result.valid)
        self.assertEqual(result.type, "fijo")

    def test_valid_mobile_with_spaces(self):
        result = validate_phone("+34 612 345 678")
        self.assertTrue(result.valid)
        self.assertEqual(result.type, "móvil")

    def test_valid_landline_with_dots(self):
        result = validate_phone("034.912.345.678")
        self.assertTrue(result.valid)
        self.assertEqual(result.type, "fijo")

    def test_valid_mobile_with_hyphens(self):
        result = validate_phone("34-612-345-678")
        self.assertTrue(result.valid)
        self.assertEqual(result.type, "móvil")

    def test_invalid_too_short(self):
        result = validate_phone("61234")
        self.assertFalse(result.valid)

    def test_invalid_too_long(self):
        result = validate_phone("61234567890")
        self.assertFalse(result.valid)

    def test_invalid_country_code(self):
        result = validate_phone("+33 612 345 678")  # Francia
        self.assertFalse(result.valid)

    def test_invalid_start_digit(self):
        result = validate_phone("512345678")  # No empieza por 6/7/8/9
        self.assertFalse(result.valid)

    def test_invalid_characters(self):
        result = validate_phone("61A34567B")
        self.assertFalse(result.valid)

if __name__ == "__main__":
    unittest.main()
