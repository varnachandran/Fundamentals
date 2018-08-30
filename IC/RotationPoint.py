import unittest


def find_rotation_point(words):
    # Find the rotation point in the list
    start=0
    end= len(words)-1

    while start < end:
        middle = (start + end) / 2
        if rotation_helper(words[start], words[middle]):
            end=middle

        else:
            start=middle
        if start + 1 == end:
            return end




def rotation_helper(word1, word2):
    for j in range(len(word1)):
        if ord(word1[j]) > ord(word2[j]):
            return True
        elif ord(word1[j]) < ord(word2[j]):
            break
    return False


# Tests

class Test(unittest.TestCase):

    def test_small_list(self):
        actual = find_rotation_point(['cape', 'cake'])
        expected = 1
        self.assertEqual(actual, expected)

    def test_medium_list(self):
        actual = find_rotation_point(['grape', 'orange', 'plum',
                                      'radish', 'apple'])
        expected = 4
        self.assertEqual(actual, expected)

    def test_large_list(self):
        actual = find_rotation_point(['ptolemaic', 'retrograde', 'supplant',
                                      'undulate', 'xenoepist', 'asymptote',
                                      'babka', 'banoffee', 'engender',
                                      'karpatka', 'othellolagkage'])
        expected = 5
        self.assertEqual(actual, expected)

    # Are we missing any edge cases?


if __name__=='__main__':
    unittest.main()