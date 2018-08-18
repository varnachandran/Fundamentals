class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BST(object):
    def __init__(self, root):
        self.root = Node(root)

    def insert(self, new_val):
        self.root = self.iter_insert(self.root,new_val)


    def search(self, find_val):
        return self.iter_search(self.root,find_val)

    def iter_insert(self,start,value_to_insert):
        if not start:
            return Node(value_to_insert)
        else:
            if value_to_insert <= start.value:
                start.left = self.iter_insert(start.left,value_to_insert)
            else:
                start.right = self.iter_insert(start.right,value_to_insert)
        return start

    def iter_search(self,start,value):
        if start:
            if start.value==value:
                return True
            elif value <= start.value:
                return self.iter_search(start.left, value)
            else:
                return self.iter_search(start.right, value)
        else:
            return False


# Set up tree
tree = BST(4)

# Insert elements
tree.insert(2)
tree.insert(1)
tree.insert(3)
tree.insert(5)

# Check search
# Should be True
print tree.search(1)
# Should be False
print tree.search(6)