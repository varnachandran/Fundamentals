import unittest




def get_permutations(string):
    if len(string) <= 1:
        return set([string])

    string_excluding_last = string[:-1]
    last_letter = string[-1]

    permutation_of_string_excluding_last = get_permutations(string_excluding_last)
    permutation_set = set()

    for word in permutation_of_string_excluding_last:
        for i in range(len(string_excluding_last) + 1):
            permutation_set.add(word[:i] + last_letter + word[i:])
    return permutation_set


# Tests

class Test(unittest.TestCase):

    def test_empty_string(self):
        actual = get_permutations('')
        expected = set([''])
        self.assertEqual(actual, expected)

    def test_one_character_string(self):
        actual = get_permutations('a')
        expected = set(['a'])
        self.assertEqual(actual, expected)

    def test_two_character_string(self):
        actual = get_permutations('ab')
        expected = set(['ab', 'ba'])
        self.assertEqual(actual, expected)

    def test_three_character_string(self):
        actual = get_permutations('abc')
        expected = set(['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
