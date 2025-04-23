import unittest
from src.services.property_service import get_properties

class TestGetProperties(unittest.TestCase):
    
    def test_should_return_a_list(self):
        filters = {}
        result = get_properties(filters)
        self.assertIsInstance(result, list)

if __name__ == "__main__":
    unittest.main()