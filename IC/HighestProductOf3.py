import unittest


def highest_product_of_3(list_of_ints):
    # Calculate the highest product of three numbers
    if len(list_of_ints) < 3:
        raise Exception("Cannot be less than 3")

    max_product_3 = list_of_ints[0] * list_of_ints[1] * list_of_ints[2]

    max_product_2 = max(list_of_ints[0] * list_of_ints[1],
                        list_of_ints[0] * list_of_ints[2],
                        list_of_ints[1] * list_of_ints[2])

    min_product_2 = min(list_of_ints[0] * list_of_ints[1],
                        list_of_ints[0] * list_of_ints[2],
                        list_of_ints[1] * list_of_ints[2])

    max_int = max(list_of_ints[0], list_of_ints[1], list_of_ints[2])

    min_int = min(list_of_ints[0], list_of_ints[1], list_of_ints[2])

    for index in range(3,len(list_of_ints)):
        current_int = list_of_ints[index]
        current_max_product3= max(max_product_2 * current_int, min_product_2*current_int)

        max_product_3 = max(current_max_product3, max_product_3)

        current_max_product2 = max(current_int * max_int , current_int * min_int)

        max_product_2 = max(current_max_product2, max_product_2)

        current_min_product_2 = min(current_int * min_int, current_int * max_int)

        min_product_2 = min(current_min_product_2, min_product_2)

        max_int = max(current_int, max_int)
        min_int = min(current_int, min_int)
    return max_product_3


# Tests

class Test(unittest.TestCase):

    def test_short_list(self):
        actual = highest_product_of_3([1, 2, 3, 4])
        expected = 24
        self.assertEqual(expected, actual)

    def test_longer_list(self):
        actual = highest_product_of_3([6, 1, 3, 5, 7, 8, 2])
        expected = 336
        self.assertEqual(expected, actual)

    def test_list_has_one_negative(self):
        actual = highest_product_of_3([-5, 4, 8, 2, 3])
        expected = 96
        self.assertEqual(expected, actual)

    def test_list_has_two_negatives(self):
        actual = highest_product_of_3([-10, 1, 3, 2, -10])
        expected = 300
        self.assertEqual(expected, actual)

    def test_list_is_all_negatives(self):
        actual = highest_product_of_3([-5, -1, -3, -2])
        expected = -6
        self.assertEqual(expected, actual)

    def test_error_with_empty_list(self):
        with self.assertRaises(Exception):
            highest_product_of_3([])

    def test_error_with_one_number(self):
        with self.assertRaises(Exception):
            highest_product_of_3([1])

    def test_error_with_two_numbers(self):
        with self.assertRaises(Exception):
            highest_product_of_3([1, 1])


if __name__ == '__main__':
    unittest.main()