import unittest

class LinkedListNode:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, head = None):
        self.head = head

    def append_node(self, node):
        if not self.head:
            self.head = node
        else:
            current = self.head

            while current.next:
                current = current.next

            current.next = node

    def is_cycle(self):
        pointer1 = self.head
        pointer2 = self.head

        while pointer1.next and pointer2.next.next:
            pointer1 = pointer1.next
            pointer2 = pointer2.next.next

            if pointer1 is pointer2:
                return True

        return False



class Test(unittest.TestCase):
    def test_creating_single_node_Linked_List(self):
        node1 = LinkedListNode(1)

        linked_list = LinkedList(node1)

        self.assertEqual(linked_list.head.value, 1)
        self.assertEqual(linked_list.head.next, None)

    def test_creating_single_node_Linked_List(self):
        node1 = LinkedListNode(1)

        linked_list = LinkedList(node1)

        node2= LinkedListNode(22)

        linked_list.append_node(node2)

        self.assertEqual(linked_list.head.next, node2)

    def test_cycle_should_return_true(self):
        node1 = LinkedListNode(1)

        linked_list = LinkedList(node1)

        node2 = LinkedListNode(2)

        linked_list.append_node(node2)

        node3 = LinkedListNode(3)
        linked_list.append_node(node3)

        node4 = LinkedListNode(4)
        linked_list.append_node(node4)

        linked_list.append_node(node2)

        is_cycle = linked_list.is_cycle()

        self.assertTrue(is_cycle)

    def test_non_cycle_should_return_false(self):
        node1 = LinkedListNode(1)

        linked_list = LinkedList(node1)

        node2 = LinkedListNode(22)

        linked_list.append_node(node2)

        is_cycle = linked_list.is_cycle()

        self.assertFalse(is_cycle)

if __name__=='__main__':
    unittest.main()