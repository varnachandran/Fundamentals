import unittest

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, head = None):
        self.head = head

    def append_node(self, new_node):
        if not self.head:
            self.head =  new_node
        else:
            current = self.head
            while current.next:
                current= current.next
            current.next = new_node


class Test(unittest.TestCase):
    def testcase_should_create_node_in_linkedlist(self):
        node=Node(1)
        linked_list= LinkedList(node)
        self.assertEqual(linked_list.head, node)

    def testcase_should_append_node_to_linkedlist(self):
        node= Node(1)
        linked_list = LinkedList(node)

        node2= Node(2)
        linked_list.append_node(node2)
        self.assertEqual(linked_list.head.next, node2)

if __name__=='__main__':
    unittest.main()