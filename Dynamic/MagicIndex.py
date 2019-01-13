import unittest
def get_magic_index(array):
    for i in range(len(array)):
        if array[i]==i:
            return i
def get_magic_index_recursion(array):
    length= len(array)
    #return get_index(array,0,length-1)
    index = get_index_not_unique(array,0,length-1)
    if index >=0:
        return index

def get_index(array,start, end):
    mid = (start+end)/2
    if start>end:
        return
    if array[mid] == mid:
        return mid
    if array[mid] > mid:
        return get_index(array,start, mid-1)
    else:
        return get_index(array,mid+1, end)

def get_index_not_unique(array, start, end):
    if start > end:
        return -1
    mid=(start+end)/2

    if array[mid] == mid:
        return mid

    left= get_index_not_unique(array, start, min(array[mid],mid-1))
    if left >=0:
        return left

    right= get_index_not_unique(array,max(array[mid],mid+1), end)
    return right

print(get_magic_index_recursion([-10,-5,1,2,2,3,4,7,9,12,13]))

class Test(unittest.TestCase):
    def test_should_return_right_index(self):
        result=get_magic_index_recursion([-10,-5,1,2,2,3,4,7,9,12,13])
        self.assertEqual(result, 7)
    def test_should_return_none(self):
        result=get_magic_index_recursion([-10,-5,1,2,2,3,4,8,9,12,13])
        self.assertEqual(result, None)
if __name__=='__main__':
    unittest.main()