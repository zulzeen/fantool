import unittest

import sort_city

class TestIsCity(unittest.TestCase):
    """
    Test class for the "is_city" function
    """
    def test_is_city(self):
        fantoir_entry = "770001    HACHERES-LA-FORET               N  3      000075400000000000000 00000001987001"
        response = sort_city.is_city(fantoir_entry)

        self.assertEqual(response, True)

    def test_is_direction(self):
        fantoir_entry = "770        SEINE ET MARNE                                  00000000000000 00000000000000"
        response = sort_city.is_city(fantoir_entry)

        self.assertEqual(response, False)

    def test_is_street(self):
        fantoir_entry = "7700010120ARUE DU CHATEAU D EAU           N  3  0          00000000000000 00000001987001               000911   EAU"
        response = sort_city.is_city(fantoir_entry)

        self.assertEqual(response, False)

class TestIsStreet(unittest.TestCase):
    """
    Test class for the "is_city" function
    """
    def test_is_city(self):
        fantoir_entry = "770001    HACHERES-LA-FORET               N  3      000075400000000000000 00000001987001"
        response = sort_city.is_street(fantoir_entry)

        self.assertEqual(response, False)

    def test_is_direction(self):
        fantoir_entry = "770        SEINE ET MARNE                                  00000000000000 00000000000000"
        response = sort_city.is_street(fantoir_entry)

        self.assertEqual(response, False)

    def test_is_street(self):
        fantoir_entry = "7700010120ARUE DU CHATEAU D EAU           N  3  0          00000000000000 00000001987001               000911   EAU"
        response = sort_city.is_street(fantoir_entry)

        self.assertEqual(response, True)

if __name__ == '__main__':
    unittest.main()
