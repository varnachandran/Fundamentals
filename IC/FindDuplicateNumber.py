import unittest

def find_duplicate_number(numbers):
    if not numbers:
        raise Exception('Empty list')

    sum_numbers = numbers[0]
    max_number = numbers[0]

    for index in range(1, len(numbers)):
        sum_numbers = sum_numbers + numbers[index]
        max_number = max(max_number, numbers[index])

    expected_sum = max_number*(max_number+1)/2

    duplicate_number = sum_numbers - expected_sum

    return duplicate_number

class Test(unittest.TestCase):
    def test_empty_list_should_throw_exception(self):
        with self.assertRaises(Exception):
            find_duplicate_number()

    def test_with_range_2(self):
        numbers = [1,2,2]
        result = find_duplicate_number(numbers)
        self.assertEqual(result, 2)

    def test_medium_list(self):
        actual = find_duplicate_number([4, 1, 3, 4, 2])
        expected = 4
        self.assertEqual(actual, expected)

    def test_long_list(self):
        actual = find_duplicate_number([1, 5, 9, 7, 2, 6, 3, 8, 2, 4])
        expected = 2
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()

