import unittest
from models.country import Country

class TestCountry(unittest.TestCase):
    
    def setUp(self):
        self.country = Country("United Kingdom")

    def test_country_has_name(self):
        self.assertEqual("United Kingdom", self.country.name)

    def test_country_visited_starts_false(self):
        self.assertEqual(False, self.country.visited)

    def test_can_mark_country_visited(self):
        self.country.mark_visited()
        self.assertEqual(True, self.country.visited)