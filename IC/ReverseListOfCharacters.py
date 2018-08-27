import unittest


def reverse(list_of_chars):
    # Reverse the input list of chars in place

    for index in range(len(list_of_chars)/2):
        list_of_chars[index], list_of_chars[-1 -index] = list_of_chars[-1 -index], list_of_chars[index]


# Tests

class Test(unittest.TestCase):

    def test_empty_string(self):
        list_of_chars = []
        reverse(list_of_chars)
        expected = []
        self.assertEqual(list_of_chars, expected)

    def test_single_character_string(self):
        list_of_chars = ['A']
        reverse(list_of_chars)
        expected = ['A']
        self.assertEqual(list_of_chars, expected)

    def test_longer_string(self):
        list_of_chars = ['A', 'B', 'C', 'D', 'E']
        reverse(list_of_chars)
        expected = ['E', 'D', 'C', 'B', 'A']
        self.assertEqual(expected, list_of_chars)

    def test_longer_string_even_characters(self):
        list_of_chars = ['A', 'B', 'C', 'D', 'E', 'F']
        reverse(list_of_chars)
        expected = ['F', 'E', 'D', 'C', 'B', 'A']
        self.assertEqual(expected, list_of_chars)

if __name__ == '__main__':
    unittest.main()
