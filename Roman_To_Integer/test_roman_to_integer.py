import unittest
from Roman_To_Integer.Roman_to_integer import Solution


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()


    def test_roman_returns_correct_value(self):
        value = self.solution.roman("X")
        self.assertEqual(10, value)

    def test_add_all_characters_returns_added_values(self):
        value = self.solution.add_all_characters("XX")
        self.assertEqual(20, value)

    def test_subtract_all_values_subtracts_values(self):
        value = self.solution.subtract_values("XXIV")
        self.assertEqual(24, value)

if __name__ == '__main__':
    unittest.main()
