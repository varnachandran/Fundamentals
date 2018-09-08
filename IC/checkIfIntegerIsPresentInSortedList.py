import unittest


def contains(numbers, number):
    length = len(numbers)
    if not length:
        return False

    i = -1
    j = length
    mid = (i + j) / 2

    while i+1 < j:

        if number == numbers[mid]:
            return True
        if number < numbers[mid]:
            j = mid
        elif number > numbers[mid]:
            i = mid
        mid = (i + j) / 2
    return False

def contains_recursion(numbers, number):
    if not numbers:
        return False
    lower = 0
    upper = len(numbers)
    return contains_helper(numbers, number, lower, upper)

def contains_helper(numbers, number, lower, upper):
     if upper-lower == 1:
        if numbers[lower] == number:
            return True
        return False
     mid = (upper + lower)/2

     return contains_helper(numbers, number, lower, mid) or contains_helper(numbers, number, mid, upper)


# Tests

class Test(unittest.TestCase):

    def test_empty_list(self):
        result = contains_recursion([], 1)
        self.assertFalse(result)

    def test_one_item_list_number_present(self):
        result = contains_recursion([1], 1)
        self.assertTrue(result)

    def test_one_item_list_number_absent(self):
        result = contains_recursion([1], 2)
        self.assertFalse(result)

    def test_small_list_number_present(self):
        result = contains_recursion([2, 4, 6], 4)
        self.assertTrue(result)

    def test_small_list_number_absent(self):
        result = contains_recursion([2, 4, 6], 5)
        self.assertFalse(result)

    def test_large_list_number_present(self):
        result = contains_recursion([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 8)
        self.assertTrue(result)

    def test_large_list_number_absent(self):
        result = contains_recursion([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 0)
        self.assertFalse(result)

    def test_large_list_number_first(self):
        result = contains_recursion([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 1)
        self.assertTrue(result)

    def test_large_list_number_last(self):
        result = contains_recursion([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10)
        self.assertTrue(result)


if __name__ == '__main__':
    unittest.main()