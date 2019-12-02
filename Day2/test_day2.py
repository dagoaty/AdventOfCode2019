import unittest

from day2 import restore_state, run_opscode, run_chunk

class TestOps(unittest.TestCase):
    def test_restore_state(self):
        """
        Test restoring state works
        """
        data = [10, 15, 20, 25, 30]

        result = restore_state(data)
        self.assertEqual(result[1], 12)
        self.assertEqual(result[2], 2)


    def test_run_opscode(self):
        """
        Test full opscode run
        """
        inputs1 = [1, 0, 0, 0, 99]
        inputs2 = [2, 3, 0, 3, 99]
        inputs3 = [2, 4, 4, 5, 99, 0]
        inputs4 = [1, 1, 1, 4, 99, 5, 6, 0, 99]
        result1 = run_opscode(inputs1)
        result2 = run_opscode(inputs2)
        result3 = run_opscode(inputs3)
        result4 = run_opscode(inputs4)
        self.assertEqual(result1[0], 2)
        self.assertEqual(result2[0], 2)
        self.assertEqual(result3[0], 2)
        self.assertEqual(result4[0], 30)


    def test_run_chunk(self):
        """
        Test chunk processing
        """
        inputs = [1,2,3,4,5,6]
        chunk1 = [1,2,3]
        chunk2 = [2,3,4]
        result1 = run_chunk(chunk1, inputs)
        result2 = run_chunk(chunk2, inputs)
        self.assertEqual(result1, 7)
        self.assertEqual(result2, 20)


if __name__ == '__main__':
    unittest.main()
