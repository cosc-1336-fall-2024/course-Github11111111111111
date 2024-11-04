#Homework 7

import unittest
from src.homework.g_lists_and_tuples.lists import get_lowest_list_value, get_highest_list_value

class Test_Config(unittest.TestCase):

def test_get_lowest_list_value():
    numbers = [8, 10, 1, 50, 20]
    expected_lowest = 1
    result = get_lowest_list_value(numbers)
    
def test_get_highest_list_value():
    numbers = [8, 10, 1, 50, 20]
    expected_highest = 50
    result = get_highest_list_value(numbers)
    



