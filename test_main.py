import unittest
from main import is_fancode_city, get_completed_percentage

class TestMain(unittest.TestCase):

    def test_is_fancode_city(self):
        user_in_fancode = {
            'address': {'geo': {'lat': '-10', 'lng': '50'}}
        }
        user_not_in_fancode = {
            'address': {'geo': {'lat': '10', 'lng': '50'}}
        }
        self.assertTrue(is_fancode_city(user_in_fancode))
        self.assertFalse(is_fancode_city(user_not_in_fancode))

    def test_get_completed_percentage(self):
        todos = [
            {'userId': 1, 'completed': True},
            {'userId': 1, 'completed': False},
            {'userId': 1, 'completed': True},
            {'userId': 2, 'completed': True}
        ]
        self.assertEqual(get_completed_percentage(1, todos), 66.66666666666666)
        self.assertEqual(get_completed_percentage(2, todos), 100)
        self.assertEqual(get_completed_percentage(3, todos), 0)

if __name__ == "__main__":
    unittest.main()
