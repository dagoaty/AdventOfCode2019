import unittest

from day1 import calc_fuel, total_fuel

class TestCalc(unittest.TestCase):
    def test_calc_fuel(self):
        """
        Test calculating individual module fuel needs
        """
        data = {12: 2, 14: 2, 1969: 654, 100756: 33583}

        for test_item in data.keys():
            result = calc_fuel(test_item)
            self.assertEqual(result, data[test_item])

    def test_total_fuel(self):
        """
        Test calulating total cumulative fuel
        """
        data = {14: 2, 1969: 966, 100756: 50346}
        for test_item in data.keys():
            result = total_fuel([test_item])
            self.assertEqual(result, data[test_item])

if __name__ == '__main__':
    unittest.main()
