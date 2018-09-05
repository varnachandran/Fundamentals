import unittest


def change_possibilities(amount_left, denominations):
    ways_to_make_amounts = [0] * (amount_left+1)
    ways_to_make_amounts[0] = 1

    for coin in denominations:
        for index in range(coin, amount_left+1):
            ways_to_make_amounts[index] = ways_to_make_amounts[index] + ways_to_make_amounts[index-coin]
    return ways_to_make_amounts[amount_left]

def min_number_of_denominations(amount, denominations):
    min_denominations_for_amount = [float('inf')] * (amount+1)
    min_denominations_for_amount[0] = 0
    for coin in denominations:
        for index in range(coin, amount+1):
            min_denominations_for_amount[index] = min(min_denominations_for_amount[index], 1+min_denominations_for_amount[index-coin])
    return min_denominations_for_amount[amount]



# Tests

class Test(unittest.TestCase):

    def test_sample_input(self):
        actual = change_possibilities(4, (2, 3, 5))
        expected = 4
        self.assertEqual(actual, expected)

    def test_one_way_to_make_zero_cents(self):
        actual = change_possibilities(0, (1, 2))
        expected = 1
        self.assertEqual(actual, expected)

    def test_no_ways_if_no_coins(self):
        actual = change_possibilities(1, ())
        expected = 0
        self.assertEqual(actual, expected)

    def test_big_coin_value(self):
        actual = change_possibilities(5, (25, 50))
        expected = 0
        self.assertEqual(actual, expected)

    def test_big_target_amount(self):
        actual = change_possibilities(50, (5, 10))
        expected = 6
        self.assertEqual(actual, expected)

    def test_change_for_one_dollar(self):
        actual = change_possibilities(100, (1, 5, 10, 25, 50))
        expected = 292
        self.assertEqual(actual, expected)

    def test_minimum_denominations(self):
        actual = min_number_of_denominations(100,(1, 5, 10, 25, 50))
        expected =2
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()