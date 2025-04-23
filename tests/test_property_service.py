import unittest
from src.services.property_service import get_properties

class TestGetProperties(unittest.TestCase):
    
    def test_should_return_a_list(self):
        filters = {}
        result = get_properties(filters)
        self.assertIsInstance(result, list)
    
    def test_should_only_return_properties_with_allowed_statuses(self):
        filters = {}
        result = get_properties(filters)

        allowed_statuses = {"pre_venta", "en_venta", "vendido"}
        for prop in result:
            self.assertIn(prop["status"], allowed_statuses)

if __name__ == "__main__":
    unittest.main()