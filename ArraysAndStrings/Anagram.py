"""method to decide if two strings are anagrams or not"""

import unittest
def check_if_anagram(string1,string2):
    if len(string1) != len(string2):
        return False
    if sorted(string1) != sorted(string2):
        return False
    return True

def check_if_anagram_using_dict(string1,string2):
    if len(string1) != len(string2):
        return False
    mydict1={}
    mydict2={}
    for index,letter in enumerate(string1):
        if letter not in mydict1:
            mydict1[letter]=1
        else:
            mydict1[letter]=mydict1[letter]+1
        if string2[index] not in mydict2:
            mydict2[string2[index]]=1
        else:
            mydict2[string2[index]]+=1
    for key,value in mydict1.items():
        if mydict1[key] !=mydict2[key]:
            return False
    return True

class Test(unittest.TestCase):    

    def testcase_anagrams_should_return_true(self):
        string1='pride'
        string2='riped'

        is_anagram = check_if_anagram_using_dict(string1,string2)

        self.assertEqual(is_anagram,True)

    def testcase_non_anagrams_should_return_False(self):
        string1='abc'
        string2='aac'

        is_anagram=check_if_anagram_using_dict(string1,string2)

        self.assertEqual(is_anagram,False)


if __name__=='__main__':    
    unittest.main()
