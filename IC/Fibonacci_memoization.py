import unittest


def find_nth_fibonacci_number(n):
    if n is None:
        raise Exception('Input a valid value')
    if 1 <= n <= 2:
        return 1
    memo = {}
    if n in memo:
        return memo[n]

    result = find_nth_fibonacci_number(n - 1) + find_nth_fibonacci_number(n - 2)

    memo[n] = result

    return result


class Test(unittest.TestCase):
    def test_first_should_return_one(self):
        n = 1
        result = find_nth_fibonacci_number(n)

        self.assertEqual(result, 1)

    def test_should_raise_exception(self):
        with self.assertRaises(Exception):
            find_nth_fibonacci_number()

    def test_should_return_successfully(self):
        n = 5
        result = find_nth_fibonacci_number(n)

        self.assertEqual(result, 5)


if __name__ == '__main__':
    unittest.main()
