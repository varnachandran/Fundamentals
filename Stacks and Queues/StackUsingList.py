import unittest


class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0

    def top(self):
        return self.items[-1]


class Test(unittest.TestCase):
    def test_constructor_should_create_empty_stack(self):
        stack= Stack()
        self.assertEqual(len(stack.items), 0)

    def test_push_should_add_items_to_stack(self):
        stack = Stack()
        stack.push(23)
        stack.push(14)
        self.assertEqual(len(stack.items), 2)

    def test_pop_should_return_last_item_pushed(self):
        stack = Stack()
        stack.push(23)
        stack.push(14)
        last_item = stack.pop()
        self.assertEqual(last_item, 14)
        self.assertEqual(len(stack.items), 1)

    def test_top_should_return_top_item_on_stack(self):
        stack = Stack()
        stack.push(23)
        stack.push(14)
        top_item = stack.top()
        self.assertEqual(top_item, 14)


if __name__== '__main__':
    unittest.main()
