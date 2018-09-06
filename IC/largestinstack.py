import unittest


class Stack(object):

    def __init__(self):
        """Initialize an empty stack"""
        self.items = []

    def push(self, item):
        """Push new item to stack"""
        self.items.append(item)

    def pop(self):
        """Remove and return last item"""
        # If the stack is empty, return None
        # (it would also be reasonable to throw an exception)
        if not self.items:
            return None

        return self.items.pop()

    def peek(self):
        """See what the last item is"""
        if not self.items:
            return None
        return self.items[-1]


class MaxStack(object):

    # Implement the push, pop, and get_max methods

    def __init__(self):
        self.max_stack= Stack()
        self.maxs = Stack()


    def push(self, item):
        self.max_stack.push(item)
        if self.maxs.peek() is None or item >= self.maxs.peek():
                self.maxs.push(item)

    def pop(self):
        item_popped = self.max_stack.pop()
        if item_popped == self.maxs.peek():
            self.maxs.pop()
        return item_popped

    def get_max(self):
        return self.maxs.peek()




class Test(unittest.TestCase):
    def test_should_return_maximum(self):
        my_stack = MaxStack()
        my_stack.push(5)
        my_stack.push(71)
        my_stack.push(10)
        my_stack.push(1)
        my_stack.pop()

        maximum_value = my_stack.get_max()

        self.assertEqual(maximum_value, 71)

    def test_stack_usage(self):
        max_stack = MaxStack()

        max_stack.push(5)

        actual = max_stack.get_max()
        expected = 5
        self.assertEqual(actual, expected)

        max_stack.push(4)
        max_stack.push(7)
        max_stack.push(7)
        max_stack.push(8)

        actual = max_stack.get_max()
        expected = 8
        self.assertEqual(actual, expected)

        actual = max_stack.pop()
        expected = 8
        self.assertEqual(actual, expected)

        actual = max_stack.get_max()
        expected = 7
        self.assertEqual(actual, expected)

        actual = max_stack.pop()
        expected = 7
        self.assertEqual(actual, expected)

        actual = max_stack.get_max()
        expected = 7
        self.assertEqual(actual, expected)

        actual = max_stack.pop()
        expected = 7
        self.assertEqual(actual, expected)

        actual = max_stack.get_max()
        expected = 5
        self.assertEqual(actual, expected)

        actual = max_stack.pop()
        expected = 4
        self.assertEqual(actual, expected)

        actual = max_stack.get_max()
        expected = 5
        self.assertEqual(actual, expected)

if __name__=='__main__':
    unittest.main
