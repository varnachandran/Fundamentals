import unittest


def merge_lists(my_list, alices_list):
    # Combine the sorted lists into one large sorted list
    merged_list = [None] * (len(my_list) + len(alices_list))
    i = 0
    j = 0
    counter = 0
    while counter < len(merged_list):
        has_my_list_reached_max = i >= len(my_list)
        has_alices_list_reached_max = j >= len(alices_list)

        if not has_my_list_reached_max and ( has_alices_list_reached_max or my_list[i] < alices_list[j]):
            merged_list[counter] = my_list[i]
            i = i + 1
        else:
            merged_list[counter] = alices_list[j]
            j = j + 1
        counter = counter + 1

    return merged_list

# Tests

class Test(unittest.TestCase):

    def test_both_lists_are_empty(self):
        actual = merge_lists([], [])
        expected = []
        self.assertEqual(actual, expected)

    def test_first_list_is_empty(self):
        actual = merge_lists([], [1, 2, 3])
        expected = [1, 2, 3]
        self.assertEqual(actual, expected)

    def test_second_list_is_empty(self):
        actual = merge_lists([5, 6, 7], [])
        expected = [5, 6, 7]
        self.assertEqual(actual, expected)

    def test_both_lists_have_some_numbers(self):
        actual = merge_lists([2, 4, 6], [1, 3, 7])
        expected = [1, 2, 3, 4, 6, 7]
        self.assertEqual(actual, expected)

    def test_lists_are_different_lengths(self):
        actual = merge_lists([2, 4, 6, 8], [1, 7])
        expected = [1, 2, 4, 6, 7, 8]
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()