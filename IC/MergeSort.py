import unittest


def merge_sort(items):
    if len(items) is 0:
        return []
    if len(items) == 1:
        return items
    else:
        mid = len(items) / 2
        left = merge_sort(items[:mid])
        right = merge_sort(items[mid:])

        sorted_list = merge_helper(left, right)

    return sorted_list


def merge_helper(left, right):
    new_list = []
    total_length = len(left) + len(right)

    while len(new_list) < total_length:
        if left and (not right or left[0] < right[0]):
            new_list.append(left.pop(0))
        else:
            new_list.append((right.pop(0)))
    return new_list


class Test(unittest.TestCase):
    def test_mergesort_should_be_successful_with_two_items(self):
        list_to_be_sorted = [2, 1]
        self.assertEqual([1, 2], merge_sort(list_to_be_sorted))

    def test_mergesort_should_return_empty_with_no_items(self):
        list_to_be_sorted = []
        self.assertEqual([], merge_sort(list_to_be_sorted))

    def test_mergesort_should_be_successful_with_even_items(self):
        list_to_be_sorted = [2, 1, 8, 0, 12, 6]
        self.assertEqual([0, 1, 2, 6, 8, 12], merge_sort(list_to_be_sorted))

    def test_mergesort_should_be_successful_with_even_items(self):
        list_to_be_sorted = [2, 1, 8, 0, 12, 6, 5]
        self.assertEqual([0, 1, 2, 5, 6, 8, 12], merge_sort(list_to_be_sorted))


if __name__ == '__main__':
    unittest.main()
