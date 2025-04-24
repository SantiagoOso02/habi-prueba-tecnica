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

    def test_should_filter_properties_by_year(self):
        filters = {"year": 2020}
        result = get_properties(filters)

        for prop in result:
            self.assertEqual(prop["year"], 2020)

    def test_should_filter_properties_by_city(self):
        filters = {"city": "bogota"}
        result = get_properties(filters)

        for prop in result:
            self.assertEqual(prop["city"], "bogota")

    def test_should_filter_properties_by_status(self):
        filters = {"status": "en_venta"}
        result = get_properties(filters)

        for prop in result:
            self.assertEqual(prop["status"], "en_venta")

    def test_should_filter_properties_by_multiple_fields(self):
        filters = {
            "year": 2020,
            "city": "bogota",
            "status": "pre_venta"
        }

        result = get_properties(filters)

        for prop in result:
            self.assertEqual(prop["year"], 2020)
            self.assertEqual(prop["city"], "bogota")
            self.assertEqual(prop["status"], "pre_venta")

if __name__ == "__main__":
    unittest.main()