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

    def remove_duplicates_without_additional_buffer(self):
        if not self.head:
            return -1

        current = self.head

        while current:
            previous = current
            runner = current.next

            while runner:
                if runner.value == current.value:
                    previous.next = runner.next

                previous = previous.next
                runner = runner.next
            current = current.next

    def get_nth_to_last_element_without_recursion(self, n):
        if not self.head:
            return -1

        current = self.head
        runner = self.head

        for i in range(n):
            if not runner:
                return -1
            runner = runner.next

        while runner.next is not None:
            current = current.next
            runner = runner.next
        return current.next.value

    def find_n_to_last(self, n):
        """Returns nth to last element from the linked list."""
        node = self.head
        count = [0]
        return self.find_n_to_last_helper(node, n - 1, count)

    def find_n_to_last_helper(self, node, n, count):
        if not node:
            return None

        result = self.find_n_to_last_helper(node.next, n, count)
        if count[0] == n:
            result = node.value

        count[0] += 1
        return result

    def get_nth_node_from_last(self, n):
        (count, result)= self.get_nth_node_from_last_helper(self.head, n-1)
        return result

    def get_nth_node_from_last_helper(self, current, n):
        if current is None:
            return (0, None)
        (count, result) = self.get_nth_node_from_last_helper(current.next, n)
        if count==n:
            result = current.value
        count= count+1
        return (count, result)

    def delete_element_in_middle(self):
        if self.head is None:
            return -1
        current = self.head
        p2position=0

        while current.next is not None:
            current= current.next
            p2position = p2position+1

        p1 = self.head
        previous = None
        p1position = 0
        while p2position != p1position:
            previous= p1
            p1 = p1.next
            p1position = p1position+1
            p2position = p2position-1
        if p1.next:
            previous.next = p1.next
            p1.next = None
        else:
            self.head = None


class Test(unittest.TestCase):
    def setUp(self):
        self.node = Node(1)
        self.linked_list = LinkedList(self.node)

    def return_items(self):
        list=[]
        current = self.linked_list.head
        while current:
            list.append(current.value)
            current = current.next
        return list

    def create_list_with_duplicate_values(self):
        node2 = Node(2)
        self.linked_list.append_node(node2)

        node3 = Node(1)
        self.linked_list.append_node(node3)

        node4 = Node(3)
        self.linked_list.append_node(node4)

        node5 = Node(2)
        self.linked_list.append_node(node5)

        node6 = Node(6)
        self.linked_list.append_node(node6)

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

    def testcase_removing_duplicates_without_buffer_should_be_successful(self):
        self.create_list_with_duplicate_values()
        self.linked_list.remove_duplicates_without_additional_buffer()

        expected_list_of_values=[1,2,3,6]

        current= self.linked_list.head
        actual_list=[]

        while current:
            actual_list.append(current.value)
            current =current.next

        self.assertEqual(expected_list_of_values, actual_list)

    def testcase_get_nth_to_last_element_without_recursion_should_return_correctly(self):
        self.create_list_with_duplicate_values()
        node9=Node(9)
        node11=Node(11)
        self.linked_list.append_node(node9)
        self.linked_list.append_node(node11)
        #nth_to_last_element = self.linked_list.get_nth_node_from_last(5)
        nth_to_last_element = self.linked_list.get_nth_node_from_last(8)
        self.assertEqual(1, nth_to_last_element)

    def testcase_get_nth_to_last_element_without_recursion_should_return_negative_one(self):
        self.linked_list = LinkedList()
        nth_to_last_element = self.linked_list.get_nth_to_last_element_without_recursion(5)
        self.assertEqual(-1, nth_to_last_element)

    def testcase_get_nth_to_last_element_with_recursion_should_return_negative_one_when_n_is_larger_than_size(self):
        self.create_list_with_duplicate_values()
        nth_to_last_element = self.linked_list.get_nth_to_last_element_without_recursion(15)
        self.assertEqual(-1, nth_to_last_element)

    def testcase_deleting_node_in_middle_should_return_correctly(self):
        self.create_list_with_duplicate_values()
        node9=Node(9)
        self.linked_list.append_node(node9)
        self.linked_list.delete_element_in_middle()
        elements_in_list = self.return_items()
        self.assertEqual(elements_in_list, [1, 2, 1, 2, 6, 9])

if __name__=='__main__':
    unittest.main()