import unittest
from src.homework.e_functions.value_return import get_hour, get_hours
from src.homework.e_functions.value_return import get_minutes
from src.homework.e_functions.value_return import get_seconds



class Test_Config(unittest.TestCase):

    def test_get_hour_epoch(self):
        self.assertEqual(23, get_hours(1727585298))
      

    def test_get_minutes_epoch(self):
        self.assertEqual(23, get_minutes(1727585298))
       

    def test_get_seconds_epoch(self):
        self.assertEqual(23, get_seconds(1727585298))
        