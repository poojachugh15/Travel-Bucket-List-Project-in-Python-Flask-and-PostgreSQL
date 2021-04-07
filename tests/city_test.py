import unittest
from models.city import City
from models.country import Country

class TestCity(unittest.TestCase):
    
    def setUp(self):
        self.city = City("London", "United Kindom")

    def test_city_has_name(self):
        self.assertEqual("London", self.city.name)
        
    def test_city_visited_starts_false(self):
        self.assertEqual(False, self.city.visited)

    def test_can_mark_city_visited(self):
        self.city.mark_visited()
        self.assertEqual(True, self.city.visited)