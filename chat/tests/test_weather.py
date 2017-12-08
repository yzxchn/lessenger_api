from django.test import TestCase
from .. import weather as wt

class TestWeatherQuery(TestCase):
    def setUp(self):
        self.loc1 = "Boston"
        self.loc2 = "94114"
        self.loc3 = "San Francisco"
        self.locx = "xng5a!d"

    def test_getting_location(self):
        c1 = wt.get_coordinates(self.loc1)
        c2 = wt.get_coordinates(self.loc2)
        c3 = wt.get_coordinates(self.loc3)
        cx = wt.get_coordinates(self.locx)
        self.assertIsNotNone(c1)
        self.assertIsNotNone(c2)
        self.assertIsNotNone(c3)
        self.assertIsNone(cx)

    def test_getting_weather(self):
        w1 = wt.get_darksky_weather(self.loc1)
        w2 = wt.get_darksky_weather(self.loc2)
        w3 = wt.get_darksky_weather(self.loc3)
        with self.assertRaises(wt.LocationNotFoundError): 
            wt.get_darksky_weather(self.locx)
        self.assertIsNotNone(w1)
        self.assertIsNotNone(w2)
        self.assertIsNotNone(w3)
