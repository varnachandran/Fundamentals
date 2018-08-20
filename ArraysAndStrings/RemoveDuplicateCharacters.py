"""3 Design an algorithm and write code to remove the duplicate characters in a string
without using any additional buffer. NOTE: One or two additional variables are fine.
An extra copy of the array is not.
FOLLOW UP
Write the test cases for this method"""

import unittest

def remove_duplicate_characters(string):
    return ''.join(sorted(set(string), key=string.index))

def remove_duplicate_characters2(string):
    checker=0
    counter=0
    newstring=[None]*len(string)
    for letter in string:
        value=ord(letter)- ord('a')
        if not( checker & (1<<value)) >0:
            newstring[counter]=letter
            counter=counter+1
            checker = checker+ (1<<value)

    newstring= [x for x in newstring if x is not None]
    return ''.join(newstring)



class blah(unittest.TestCase):

    def testcase_with_duplicate_characters(self):
        string='duplicated'
        updated_string=remove_duplicate_characters(string)
        self.assertEqual(updated_string,'duplicate')

    def testcase_with_duplicate_characters2(self):
        string='duplicated'
        updated_string=remove_duplicate_characters2(string)
        self.assertEqual(updated_string,'duplicate')


if __name__=='__main__':    
    unittest.main()

