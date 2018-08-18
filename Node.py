class Node:
    def __init__(self,value):
        self.value=value
        self.next=None

class LinkedList:
    def __init__(self,head=None):
        self.head=head
    def append_node(self,node):
        if not self.head:
            self.head=node
        else:
            current_node=self.head
            while current_node.next:
                current_node=current_node.next
            current_node.next=node

    def get_position(self, position):
        current_node = self.head
        for i in range(position-1):
            if current_node.next:

                current_node = current_node.next
            else:
                return None
        return current_node
    def insert_node(self,node,position):
        if not self.head:
            self.head=node
        else:
            current_node=self.head
            prev_node=None
            for i in range(0,position-1):
                prev_node = current_node
                current_node=current_node.next
            if current_node:
                node.next=current_node
            if prev_node:
                prev_node.next=node

    def delete(self, value):
        current_node=self.head
        previous_node=None
        while current_node.value is not None:
            if current_node.value!=value:
                previous_node=current_node
                current_node=current_node.next
            else:
                previous_node.next=current_node.next










"""The LinkedList code from before is provided below.
Add three functions to the LinkedList.
"get_position" returns the element at a certain position.
The "insert" function will add an element to a particular
spot in the list.
"delete" will delete the first element with that
particular value.
Then, use "Test Run" and "Submit" to run the test cases
at the bottom."""



node1=Node(100)
node2=Node(200)
nodetoinsert=Node(115)

linked_list=LinkedList()
linked_list.append_node(node1)
linked_list.append_node(node2)
print(linked_list.get_position(1))
print(linked_list.get_position(2))
linked_list.insert_node(nodetoinsert,5)
print(linked_list.get_position(3).value)
