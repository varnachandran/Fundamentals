import unittest

def find_largest_recursion(current):
    if not current:
        return None
    if not current.right:
        return current.value
    return find_largest_recursion(current.right)


def find_largest_iteration(root_node):
    while root_node:
        if not root_node.right:
            return root_node.value
        root_node= root_node.right

def find_second_largest_iteration(current):
    if not current or(not current.left and not current.right):
        raise Exception('Lesser items than expected in the tree')

    while current:
        if not current.right and current.left:
            return find_largest_iteration(current.left)
        if current.right and not current.right.right and not current.right.left:
            return current.value
        current= current.right

def find_second_largest(root_node):
    if (root_node is None or
            (root_node.left is None and root_node.right is None)):
        raise ValueError('Tree must have at least 2 nodes')

    # Case: we're currently at largest, and largest has a left subtree,
    # so 2nd largest is largest in said subtree
    if root_node.left and not root_node.right:
        return find_largest_recursion(root_node.left)

    # Case: we're at parent of largest, and largest has no left subtree,
    # so 2nd largest must be current node
    if (root_node.right and
            not root_node.right.left and
            not root_node.right.right):
        return root_node.value

    # Otherwise: step right
    return find_second_largest(root_node.right)


# Tests

class Test(unittest.TestCase):
    class BinaryTreeNode(object):

        def __init__(self, value):
            self.value = value
            self.left = None
            self.right = None

        def insert_left(self, value):
            self.left = Test.BinaryTreeNode(value)
            return self.left

        def insert_right(self, value):
            self.right = Test.BinaryTreeNode(value)
            return self.right

    def test_full_tree(self):
        tree = Test.BinaryTreeNode(50)
        left = tree.insert_left(30)
        right = tree.insert_right(70)
        left.insert_left(10)
        left.insert_right(40)
        right.insert_left(60)
        right.insert_right(80)
        actual = find_second_largest_iteration(tree)
        expected = 70
        self.assertEqual(actual, expected)

    def test_largest_has_a_left_child(self):
        tree = Test.BinaryTreeNode(50)
        left = tree.insert_left(30)
        right = tree.insert_right(70)
        left.insert_left(10)
        left.insert_right(40)
        right.insert_left(60)
        actual = find_second_largest_iteration(tree)
        expected = 60
        self.assertEqual(actual, expected)

    def test_largest_has_a_left_subtree(self):
        tree = Test.BinaryTreeNode(50)
        left = tree.insert_left(30)
        right = tree.insert_right(70)
        left.insert_left(10)
        left.insert_right(40)
        right_left = right.insert_left(60)
        right_left_left = right_left.insert_left(55)
        right_left.insert_right(65)
        right_left_left.insert_right(58)
        actual = find_second_largest_iteration(tree)
        expected = 65
        self.assertEqual(actual, expected)

    def test_second_largest_is_root_node(self):
        tree = Test.BinaryTreeNode(50)
        left = tree.insert_left(30)
        tree.insert_right(70)
        left.insert_left(10)
        left.insert_right(40)
        actual = find_second_largest_iteration(tree)
        expected = 50
        self.assertEqual(actual, expected)

    def test_descending_linked_list(self):
        tree = Test.BinaryTreeNode(50)
        left = tree.insert_left(40)
        left_left = left.insert_left(30)
        left_left_left = left_left.insert_left(20)
        left_left_left.insert_left(10)
        actual = find_second_largest_iteration(tree)
        expected = 40
        self.assertEqual(actual, expected)

    def test_ascending_linked_list(self):
        tree = Test.BinaryTreeNode(50)
        right = tree.insert_right(60)
        right_right = right.insert_right(70)
        right_right.insert_right(80)
        actual = find_second_largest_iteration(tree)
        expected = 70
        self.assertEqual(actual, expected)

    def test_error_when_tree_has_one_node(self):
        tree = Test.BinaryTreeNode(50)
        with self.assertRaises(Exception):
            find_second_largest(tree)

    def test_error_when_tree_is_empty(self):
        with self.assertRaises(Exception):
            find_second_largest(None)


if __name__ == '__main__':
    unittest.main()