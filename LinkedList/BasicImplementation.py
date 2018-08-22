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

    def delete_node(self, node_value_to_delete):
        if not(node_value_to_delete) or not(self.head):
            return -1

        current = self.head
        previous = None
        while current:
            if current.value == node_value_to_delete:
                if previous:
                    previous.next = current.next
                    current.next= None
                else:
                    self.head = self.head.next
                break

            else:
                previous = current
                current = current.next
        return -1

    def remove_duplicates(self):
        my_set=set()

        current= self.head
        previous= None

        while current:
            if current.value not in my_set:
                my_set.add(current.value)
                previous=current

            else:
                previous.next = current.next
            current = current.next





class Test(unittest.TestCase):
    def setUp(self):
        self.node = Node(1)
        self.linked_list = LinkedList(self.node)

    def testcase_should_create_node_in_linkedlist(self):

        self.assertEqual(self.linked_list.head, self.node)

    def testcase_should_append_node_to_linkedlist(self):


        node2= Node(2)
        self.linked_list.append_node(node2)
        self.assertEqual(self.linked_list.head.next, node2)

    def testcase_deleting_head_should_be_successful(self):
        node2 = Node(2)
        self.linked_list.append_node(node2)

        self.linked_list.delete_node(1)
        self.assertEqual(self.linked_list.head, node2)

    def testcase_deleting_tail_node_should_be_successful(self):
        node2 = Node(2)
        self.linked_list.append_node(node2)

        self.linked_list.delete_node(2)
        self.assertEqual(self.linked_list.head, self.node)
        self.assertEqual(self.linked_list.head.next, None)

    def testcase_deleting_only_node_should_be_successful(self):

        self.linked_list.delete_node(1)
        self.assertEqual(self.linked_list.head, None)

    def testcase_deleting_incorrect_node_should_not_be_successful(self):

        return_value=self.linked_list.delete_node(5)
        self.assertEqual(return_value, -1)

    def testcase_removing_duplicates_should_be_successful(self):
        node2= Node(2)
        self.linked_list.append_node(node2)
        node3= Node(1)
        self.linked_list.append_node(node3)

        self.linked_list.remove_duplicates()
        self.assertEqual(self.linked_list.head.next.next, None)


if __name__=='__main__':
    unittest.main()