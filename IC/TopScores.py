import unittest


def sort_scores(unsorted_scores, highest_possible_score):
    # Sort the scores in O(n) time

    my_list = [0] * 101
    for score in unsorted_scores:
        my_list[score] += 1

    sorted_list = []
    for index in range(100, 0, -1):
        for i in range(my_list[index]):
            sorted_list.append(index)
    return sorted_list


# Tests

class Test(unittest.TestCase):

    def test_no_scores(self):
        actual = sort_scores([], 100)
        expected = []
        self.assertEqual(actual, expected)

    def test_one_score(self):
        actual = sort_scores([55], 100)
        expected = [55]
        self.assertEqual(actual, expected)

    def test_two_scores(self):
        actual = sort_scores([30, 60], 100)
        expected = [60, 30]
        self.assertEqual(actual, expected)

    def test_many_scores(self):
        actual = sort_scores([37, 89, 41, 65, 91, 53], 100)
        expected = [91, 89, 65, 53, 41, 37]
        self.assertEqual(actual, expected)

    def test_repeated_scores(self):
        actual = sort_scores([20, 10, 30, 30, 10, 20], 100)
        expected = [30, 30, 20, 20, 10, 10]
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()