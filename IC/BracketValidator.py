import unittest


def is_valid(code):
    # Determine if the input code is valid

    openers = {'(': 0, '{': 1, '[': 2}
    closers = {')': 0, '}': 1, ']': 2}

    par_stack = []
    for letter in code:
        if letter in openers:
            par_stack.append(letter)
        elif letter in closers:
            if not par_stack:
                return False
            current = par_stack.pop()
            if openers[current] != closers[letter]:
                return False
    if len(par_stack) == 0:
        return True
    return False


# Tests

class Test(unittest.TestCase):

    def test_valid_short_code(self):
        result = is_valid('()')
        self.assertTrue(result)

    def test_valid_longer_code(self):
        result = is_valid('([]{[]})[]{{}()}')
        self.assertTrue(result)

    def test_interleaved_openers_and_closers(self):
        result = is_valid('([)]')
        self.assertFalse(result)

    def test_mismatched_opener_and_closer(self):
        result = is_valid('([][]}')
        self.assertFalse(result)

    def test_missing_closer(self):
        result = is_valid('[[]()')
        self.assertFalse(result)

    def test_extra_closer(self):
        result = is_valid('[[]]())')
        self.assertFalse(result)

    def test_empty_string(self):
        result = is_valid('')
        self.assertTrue(result)


if __name__ == '__main__':
    unittest.main