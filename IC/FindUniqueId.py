import unittest


def find_unique_delivery_id(delivery_ids):
    # Find the one unique ID in the list
    if not delivery_ids:
        raise Exception('Empty delivery_ids')
    result = delivery_ids[0]

    for i in range(1, len(delivery_ids)):
        result = result ^ delivery_ids[i]

    return result

class Test(unittest.TestCase):
    def test_should_return_with_one_id(self):
        delivery_ids=[1]
        result = find_unique_delivery_id(delivery_ids)
        self.assertEqual(result, 1)

    def test_should_return_with_many_ids(self):
        delivery_ids=[1, 2, 3, 2, 1]
        result = find_unique_delivery_id(delivery_ids)
        self.assertEqual(result, 3)

    def test_should_return_with_no_id(self):
        delivery_ids=[]
        with self.assertRaises(Exception):
            find_unique_delivery_id(delivery_ids)

    def test_one_drone(self):
        actual = find_unique_delivery_id([1])
        expected = 1
        self.assertEqual(actual, expected)

    def test_unique_id_comes_first(self):
        actual = find_unique_delivery_id([1, 2, 2])
        expected = 1
        self.assertEqual(actual, expected)

    def test_unique_id_comes_last(self):
        actual = find_unique_delivery_id([3, 3, 2, 2, 1])
        expected = 1
        self.assertEqual(actual, expected)

    def test_unique_id_in_middle(self):
        actual = find_unique_delivery_id([3, 2, 1, 2, 3])
        expected = 1
        self.assertEqual(actual, expected)

    def test_many_drones(self):
        actual = find_unique_delivery_id([2, 5, 4, 8, 6, 3, 1, 4, 2, 3, 6, 5, 1])
        expected = 8
        self.assertEqual(actual, expected)


if __name__=='__main__':
    unittest.main()