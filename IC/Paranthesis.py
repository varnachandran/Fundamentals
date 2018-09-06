import unittest


def get_closing_paren(sentence, opening_paren_index):
    # Find the position of the matching closing parenthesis
    count_left = 0

    for index in range(opening_paren_index, len(sentence)):
        if sentence[index] == '(':
            count_left += 1
        elif sentence[index] == ')':
            count_left -=1
        if count_left==0:
            return index

    raise Exception('Unequal paranthesis')

# Tests

class Test(unittest.TestCase):

    def test_all_openers_then_closers(self):
        actual = get_closing_paren('((((()))))', 2)
        expected = 7
        self.assertEqual(actual, expected)

    def test_mixed_openers_and_closers(self):
        actual = get_closing_paren('()()((()()))', 5)
        expected = 10
        self.assertEqual(actual, expected)

    def test_no_matching_closer(self):
        with self.assertRaises(Exception):
            get_closing_paren('()(()', 2)


if __name__=='__main__':
    unittest.main
