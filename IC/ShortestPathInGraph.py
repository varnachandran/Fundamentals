import unittest
from collections import deque

def bfs_get_path(graph, start, end):
    if start==end:
        return [start]
    if start not in graph or end not in graph:
        raise Exception("Node/s not in graph")

    nodes_to_visit=deque()
    nodes_to_visit.append(start)

    how_we_arrived_at_node={start: None}

    while len(nodes_to_visit):
        current_node = nodes_to_visit.popleft()

        if current_node==end:
            path= reconstruct_path(start, end, how_we_arrived_at_node)
            return path

        for neighbour in graph[current_node]:
            if neighbour not in how_we_arrived_at_node:
                nodes_to_visit.append(neighbour)
                how_we_arrived_at_node[neighbour] = current_node

def reconstruct_path(start, end, how_we_arrived_at_node):
    path=[]
    result= end

    path.append(result)
    while result != start:
        result= how_we_arrived_at_node[result]
        path.append(result)

    return path[::-1]


# Tests

class Test(unittest.TestCase):

    def setUp(self):
        self.graph = {
            'a': ['c', 'b', 'd'],
            'b': ['a', 'd'],
            'c': ['a', 'e'],
            'd': ['a', 'b'],
            'e': ['c'],
            'f': ['g'],
            'g': ['f'],
        }

    def test_two_hop_path_1(self):
        actual = bfs_get_path(self.graph, 'a', 'e')
        expected = ['a', 'c', 'e']
        self.assertEqual(actual, expected)

    def test_two_hop_path_2(self):
        actual = bfs_get_path(self.graph, 'd', 'c')
        expected = ['d', 'a', 'c']
        self.assertEqual(actual, expected)

    def test_one_hop_path_1(self):
        actual = bfs_get_path(self.graph, 'a', 'c')
        expected = ['a', 'c']
        self.assertEqual(actual, expected)

    def test_one_hop_path_2(self):
        actual = bfs_get_path(self.graph, 'f', 'g')
        expected = ['f', 'g']
        self.assertEqual(actual, expected)

    def test_one_hop_path_3(self):
        actual = bfs_get_path(self.graph, 'g', 'f')
        expected = ['g', 'f']
        self.assertEqual(actual, expected)

    def test_zero_hop_path(self):
        actual = bfs_get_path(self.graph, 'a', 'a')
        expected = ['a']
        self.assertEqual(actual, expected)

    def test_no_path(self):
        actual = bfs_get_path(self.graph, 'a', 'f')
        expected = None
        self.assertEqual(actual, expected)

    def test_start_node_not_present(self):
        with self.assertRaises(Exception):
            bfs_get_path(self.graph, 'h', 'a')

    def test_end_node_not_present(self):
        with self.assertRaises(Exception):
            bfs_get_path(self.graph, 'a', 'h')


if __name__=='__main__':
    unittest.main()