import data
import lab5
import unittest


# Write your test cases for each part below.

class TestCases(unittest.TestCase):
    # Part 1
    #    Part 1 tests should be in data_tests.py.

    # Part 2
    #    Part 2 tests should be in data_tests.py.

    # Part 3: Test cases for time_add function
    def test_time_add_1(self):
        time1 = data.Time(1, 20, 30)
        time2 = data.Time(2, 40, 45)
        result = lab5.time_add(time1, time2)
        self.assertEqual(result.hour, 4)
        self.assertEqual(result.minute, 1)
        self.assertEqual(result.second, 15)

    def test_time_add_2(self):
        time1 = data.Time(12, 59, 59)
        time2 = data.Time(0, 0, 2)
        result = lab5.time_add(time1, time2)
        self.assertEqual(result.hour, 13)
        self.assertEqual(result.minute, 0)
        self.assertEqual(result.second, 1)

    # Part 4: Test cases for is_descending function
    def test_is_descending_1(self):
        self.assertTrue(lab5.is_descending([5.0, 3.5, 2.0, 1.0]))

    def test_is_descending_2(self):
        self.assertFalse(lab5.is_descending([1.0, 2.0, 3.5, 4.5]))

    # Part 5: Test cases for largest_between function
    def test_largest_between_1(self):
        nums = [10, 20, 30, 25, 15]
        self.assertEqual(lab5.largest_between(nums, 1, 3), 2)

    def test_largest_between_2(self):
        nums = [10, 20, 5, 30, 25, 15]
        self.assertEqual(lab5.largest_between(nums, 0, 5), 3)

    # Part 6: Test cases for furthest_from_origin function
    def test_furthest_from_origin_1(self):
        points = [data.Point(1, 1), data.Point(3, 4), data.Point(5, 12)]
        self.assertEqual(lab5.furthest_from_origin(points), 2)

    def test_furthest_from_origin_2(self):
        points = [data.Point(0, 0)]
        self.assertEqual(lab5.furthest_from_origin(points), 0)


if __name__ == '__main__':
    unittest.main()
