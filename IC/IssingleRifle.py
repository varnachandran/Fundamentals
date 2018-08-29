import unittest


def is_single_riffle(half1, half2, shuffled_deck):
    # Check if the shuffled deck is a single riffle of the halves
    count = 0
    half1_index = 0
    half2_index = 0
    while count < len(shuffled_deck):
        has_half1_exhausted = half1_index >= len(half1)
        has_half2_exhausted = half2_index >= len(half2)
        if not has_half1_exhausted and (half1[half1_index] == shuffled_deck[count]):
            half1_index = half1_index + 1
        elif not has_half2_exhausted and (half2[half2_index] == shuffled_deck[count]):
            half2_index = half2_index + 1
        else:
            return False
        count = count + 1

    return True


# Tests

class Test(unittest.TestCase):

    def test_both_halves_are_the_same_length(self):
        result = is_single_riffle([1, 4, 5], [2, 3, 6], [1, 2, 3, 4, 5, 6])
        self.assertTrue(result)

    def test_halves_are_different_lengths(self):
        result = is_single_riffle([1, 5], [2, 3, 6], [1, 2, 6, 3, 5])
        self.assertFalse(result)

    def test_one_half_is_empty(self):
        result = is_single_riffle([], [2, 3, 6], [2, 3, 6])
        self.assertTrue(result)

    def test_shuffled_deck_is_missing_cards(self):
        result = is_single_riffle([1, 5], [2, 3, 6], [1, 6, 3, 5])
        self.assertFalse(result)

    def test_shuffled_deck_has_extra_cards(self):
        result = is_single_riffle([1, 5], [2, 3, 6], [1, 2, 3, 5, 6, 8])
        self.assertFalse(result)


if __name__ == '__main__':
    unittest.main()