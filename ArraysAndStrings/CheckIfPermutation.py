import unittest

def check_if_strings_are_permutations(string1, string2):
    if len(string1) != len(string2):
        return False
    string1=string1.lower()
    string2= string2.lower()


    letters_count=[0]*128

    for letter in string1:
        if letters_count[ord(letter)]:
            letters_count[ord(letter)]= letters_count[ord(letter)] +1
        else:
            letters_count[ord(letter)]=1

    for letter in string2:
        letters_count[ord(letter)] = letters_count[ord(letter)] -1
        if letters_count[ord(letter)] <0:
            return False
    return True

class Test(unittest.TestCase):
    def test_should_return_true_for_permutations(self):
        result= check_if_strings_are_permutations('bag','gba')
        self.assertEqual(result, True)
    def test_should_return_false_for_nonpemutations(self):
        result = check_if_strings_are_permutations('bag', 'acd')
        self.assertEqual(result, False)

if __name__=='__main__':
    unittest.main()