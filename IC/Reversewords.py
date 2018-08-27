import unittest


def reverse_words(message):
    # Decode the message by reversing the words
    if message is None or len(message) is 0:
        return ['']
    reverse_single_word(message, 0, len(message)-1)
    starting_index = 0

    for index in range(len(message)+1):
        if index is len(message) or message[index] is ' ':
            reverse_single_word(message,starting_index, index-1)
            starting_index = index + 1

def reverse_single_word(string,start_index, end_index):
    while start_index < end_index:
        string[start_index], string[end_index] = string[end_index], string[start_index]
        start_index = start_index + 1
        end_index = end_index - 1


# Tests

class Test(unittest.TestCase):

    def test_one_word(self):
        message = list('vault')
        reverse_words(message)
        expected = list('vault')
        self.assertEqual(message, expected)

    def test_two_words(self):
        message = list('thief cake')
        reverse_words(message)
        expected = list('cake thief')
        self.assertEqual(message, expected)

    def test_three_words(self):
        message = list('one another get')
        reverse_words(message)
        expected = list('get another one')
        self.assertEqual(message, expected)

    def test_multiple_words_same_length(self):
        message = list('rat the ate cat the')
        reverse_words(message)
        expected = list('the cat ate the rat')
        self.assertEqual(message, expected)

    def test_multiple_words_different_lengths(self):
        message = list('yummy is cake bundt chocolate')
        reverse_words(message)
        expected = list('chocolate bundt cake is yummy')
        self.assertEqual(message, expected)

    def test_empty_string(self):
        message = list('')
        reverse_words(message)
        expected = list('')
        self.assertEqual(message, expected)


if __name__ == '__main__':
    unittest.main()
