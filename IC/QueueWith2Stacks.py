import unittest

class Stack:
    def __init__(self):
        self.items=[]

    def pop(self):
        if self.items:
            return self.items.pop()
        return None

    def push(self, item):
        if item:
            self.items.append(item)
        else:
            raise Exception('Item cannot be Empty')

    def peek(self):
        """See what the last item is"""
        if not self.items:
            return None
        return self.items[-1]


class QueueTwoStacks(object):

    # Implement the enqueue and dequeue methods
    def __init__(self):
        self.queue = [Stack(), Stack()]
    def enqueue(self, item):
        self.queue[0].push(item)

    def dequeue(self):
        if not self.queue[1].items:

            while self.queue[0].items:
                item = self.queue[0].pop()
                self.queue[1].push(item)
        if self.queue[1].peek():

            return self.queue[1].pop()
        raise Exception('Queue empty')


# Tests

class Test(unittest.TestCase):

    def test_queue_usage(self):
        queue = QueueTwoStacks()

        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)

        actual = queue.dequeue()
        expected = 1
        self.assertEqual(actual, expected)

        actual = queue.dequeue()
        expected = 2
        self.assertEqual(actual, expected)

        queue.enqueue(4)

        actual = queue.dequeue()
        expected = 3
        self.assertEqual(actual, expected)

        actual = queue.dequeue()
        expected = 4
        self.assertEqual(actual, expected)

        with self.assertRaises(Exception):
            queue.dequeue()