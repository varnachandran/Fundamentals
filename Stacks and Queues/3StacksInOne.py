import unittest


class MultiStack:
    def __init__(self, max_size_of_each_stack):
        self.number_of_stacks = 3
        self.max_size_of_each_stack = max_size_of_each_stack
        self.array = [0] * max_size_of_each_stack *3
        self.size_of_stacks = [0] * self.number_of_stacks

    def push(self, item, stack_number):
        if self.size_of_stacks[stack_number-1] == self.max_size_of_each_stack:
            return -1

        self.array[(stack_number -1) * self.max_size_of_each_stack + self.size_of_stacks[stack_number-1]] = item
        self.size_of_stacks[stack_number-1] = self.size_of_stacks[stack_number-1] + 1

    def pop(self, stack_number):
        if stack_number > self.number_of_stacks or stack_number <= 0:
            return -1
        item = self.array.pop((stack_number-1)*self.max_size_of_each_stack-1 + self.size_of_stacks[stack_number-1])
        self.size_of_stacks[stack_number-1] = self.size_of_stacks[stack_number-1] - 1
        return item


class Test(unittest.TestCase):
    def test_creation_should_be_successful(self):
        stack = MultiStack(150)
        self.assertEqual(stack.max_size_of_each_stack, 150)
        self.assertEqual(stack.size_of_stacks, [0]*3)

    def test_pushing_item_to_a_full_stack_should_not_be_successful(self):
        stack = MultiStack(5)
        for i in range(5):
            stack.push(23, 3)
        self.assertEqual(stack.push(23, 3), -1)

    def test_pushing_item_to_a_stack_should_be_successful(self):
        stack = MultiStack(5)
        for i in range(5):
            stack.push(23, 3)

        self.assertEqual(stack.size_of_stacks[2], 5)

    def test_popping_item_should_be_successful(self):
        stack = MultiStack(5)
        for i in range(5):
            stack.push(23+i, 3)
        self.assertEqual(27, stack.pop(3))
        self.assertEqual(stack.size_of_stacks[2], 4)

if __name__== '__main__':
    unittest.main()