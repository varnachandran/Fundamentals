import unittest

def fib(n):
    # Compute the nth Fibonacci number
    if n < 0:
        raise Exception('Cannot be less than 0')

    if n in [0, 1]:
        return n

    first = 0
    second = 1

    for i in xrange(n):
        result = first + second
        second = first
        first = result

    return result


# Tests

class Test(unittest.TestCase):

    def test_zeroth_fibonacci(self):
        actual = fib(0)
        expected = 0
        self.assertEqual(actual, expected)

    def test_first_fibonacci(self):
        actual = fib(1)
        expected = 1
        self.assertEqual(actual, expected)

    def test_second_fibonacci(self):
        actual = fib(2)
        expected = 1
        self.assertEqual(actual, expected)

    def test_third_fibonacci(self):
        actual = fib(3)
        expected = 2
        self.assertEqual(actual, expected)

    def test_fifth_fibonacci(self):
        actual = fib(5)
        expected = 5
        self.assertEqual(actual, expected)

    def test_tenth_fibonacci(self):
        actual = fib(10)
        expected = 55
        self.assertEqual(actual, expected)

    def test_negative_fibonacci(self):
        with self.assertRaises(Exception):
            fib(-1)


if __name__ == '__main__':
    unittest.main()
