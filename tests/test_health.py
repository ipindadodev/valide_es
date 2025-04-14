import unittest
import json
import sys
import os
from app.api.health import health_check
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

class TestHealthCheck(unittest.TestCase):

    def test_health_check_response(self):
        response = health_check()
        self.assertEqual(response.status_code, 200)

        data = json.loads(response.body)
        self.assertEqual(data["status"], "ok")
        self.assertEqual(data["service"], "Valide.es API")
        self.assertIn("funcionando", data["message"])

if __name__ == "__main__":
    unittest.main()