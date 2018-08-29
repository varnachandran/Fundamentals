import unittest


def can_two_movies_fill_flight(movie_lengths, flight_length):

    # Determine if two movie runtimes add up to the flight length
    movie_buffer=set()
    for movie_length in movie_lengths:
        if flight_length-movie_length in movie_buffer:
            return True
        else:
            movie_buffer.add(movie_length)

    return False
# Tests

class Test(unittest.TestCase):

    def test_short_flight(self):
        result = can_two_movies_fill_flight([1, 4], 8)
        self.assertFalse(result)

    def test_long_flight(self):
        result = can_two_movies_fill_flight([2, 4], 6)
        self.assertTrue(result)

    def test_one_movie_half_flight_length(self):
        result = can_two_movies_fill_flight([3, 8], 6)
        self.assertFalse(result)

    def test_two_movies_half_flight_length(self):
        result = can_two_movies_fill_flight([3, 8, 3], 6)
        self.assertTrue(result)

    def test_lots_of_possible_pairs(self):
        result = can_two_movies_fill_flight([1, 2, 3, 4, 5, 6], 7)
        self.assertTrue(result)

    def test_only_one_movie(self):
        result = can_two_movies_fill_flight([6], 6)
        self.assertFalse(result)

    def test_no_movies(self):
        result = can_two_movies_fill_flight([1], 2)
        self.assertFalse(result)


if __name__ == '__main__':
    unittest.main()