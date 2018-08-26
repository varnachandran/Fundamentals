"""Implementing stack with push, pop and min in O(1)"""

import unittest
class Stack:
    def __init__(self):
        self.items = []
        self.minimum = None

    def push(self, item):
        if self.minimum is None:
            self.minimum = item
        if item < self.minimum:
            self.minimum = item
        self.items.append(item)

    def pop(self):
        self.items.pop()

    def min(self):
        return self.minimum

class Test(unittest.TestCase):
    def test_pushing_should_be_successful(self):
        stack = Stack()
        stack.push(9)
        self.assertEquals(1, len(stack.items))

    def test_min_should_return_correct_item(self):
        stack=Stack()
        stack.push(9)
        stack.push(3)
        stack.push(-1)
        stack.push(10)
        self.assertEqual(-1, stack.min())

if __name__=='__main__':
    unittest.main()