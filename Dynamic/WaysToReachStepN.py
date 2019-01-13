import unittest
def ways_to_reach_step_n(n):
    if n<0:
        return 0
    if n==0:
        return 1
    return ways_to_reach_step_n(n-1) + ways_to_reach_step_n(n-2) + ways_to_reach_step_n(n-3)

def count_ways(n):
    try:
        memo
    except NameError:
        memo={}
    if n<0:
        return 0
    if n==0:
        return 1
    if n in memo:
        return memo[n]
    memo[n]= count_ways(n-1) + count_ways(n-2) + count_ways(n-3)
    return memo[n]



class Test(unittest.TestCase):
    def test_should_return_correct_number(self):
        result= ways_to_reach_step_n(3)
        self.assertEqual(result, 4)
    def test_should_return_correct_number_dynamic(self):
        result= count_ways(3)
        self.assertEqual(result, 4)
if __name__=='__main__':
    unittest.main()