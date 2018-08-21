import unittest

def check_if_rotation(string1,string2):
    if len(string1) != len(string2):
        return False
    concatenated_string=string1+string1
    return check_if_substring(concatenated_string,string2)



def check_if_substring(main_string, sub_string):
    return sub_string in main_string



class Test(unittest.TestCase):
    def testcase_should_return_true_for_rotated_string(self):
        actual_result=check_if_rotation('apple', 'pleap')
        self.assertEqual(actual_result, True)

    def testcase_should_return_false_for_non_rotated_string(self):
        actual_result=check_if_rotation('apple', 'ppale')
        self.assertEqual(actual_result, False)

if __name__=='__main__':
    unittest.main()