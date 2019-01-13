import unittest

def product_except_index(numbers):
    length = len(numbers)

    prod = [1] * length

    for i in range(1, length):
        prod[i] = prod[i-1] * numbers[i-1]

    current_prod = numbers[length-1]

    for i in range(length-2, -1, -1):
        prod[i] = prod[i] * current_prod
        current_prod= current_prod * numbers[i]
    return prod

class Test(unittest.TestCase):
    def test_should_return_correct_results(self):
        numbers = [6, 1, 2, 3, 4, 5, 7]
        result = product_except_index(numbers)
        self.assertEqual(result, [840, 5040, 2520, 1680, 1260, 1008, 720])


if __name__ == '__main__':
    unittest.main()
