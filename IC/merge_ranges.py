import unittest


def merge_ranges(meetings):
    sorted_meetings = sorted(meetings)

    merged_meetings=[]
    current_start = sorted_meetings[0][0]
    current_end = sorted_meetings[0][1]
    merged_meetings.append((current_start, current_end))

    for start, end in sorted_meetings[1:]:
        if start <= current_end:

            current_end = current_end if current_end> end else end
            merged_meetings[-1] = (current_start, current_end)
        else:
            merged_meetings.append((start, end))
        current_start =merged_meetings[-1][0]
        current_end = merged_meetings[-1][1]

    return merged_meetings




# Tests

class Test(unittest.TestCase):

    def test_meetings_overlap(self):
        actual = merge_ranges([(1, 3), (2, 4)])
        expected = [(1, 4)]
        self.assertEqual(actual, expected)

    def test_meetings_touch(self):
        actual = merge_ranges([(5, 6), (6, 8)])
        expected = [(5, 8)]
        self.assertEqual(actual, expected)

    def test_meeting_contains_other_meeting(self):
        actual = merge_ranges([(1, 8), (2, 5)])
        expected = [(1, 8)]
        self.assertEqual(actual, expected)

    def test_meetings_stay_separate(self):
        actual = merge_ranges([(1, 3), (4, 8)])
        expected = [(1, 3), (4, 8)]
        self.assertEqual(actual, expected)

    def test_multiple_merged_meetings(self):
            actual = merge_ranges([(1, 4), (2, 5), (5, 8)])
            expected = [(1, 8)]
            self.assertEqual(actual, expected)

    def test_meetings_not_sorted(self):
            actual = merge_ranges([(5, 8), (1, 4), (6, 8)])
            expected = [(1, 4), (5, 8)]
            self.assertEqual(actual, expected)

    def test_sample_input(self):
            actual = merge_ranges([(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)])
            expected = [(0, 1), (3, 8), (9, 12)]
            self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()
