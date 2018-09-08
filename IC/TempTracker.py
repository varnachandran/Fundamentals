import unittest


class TempTracker:
    def __init__(self):
        self.items = []
        self.min = None
        self.max = None
        self.mean = None
        self.mode = None
        self.sum = None
        self.temp_count = [None]*120
        self.max_count = None

    def insert(self, item):
        if not self.items:

            self.min = item
            self.max = item
            self.mean = item
            self.sum = item
        else:
            self.min = min(item, self.min)
            self.max = max(item, self.max)
            self.sum = self.sum + item
            self.mean = self.sum/(len(self.items) + 1)

        self.items.append(item)
        if self.temp_count[item]:
            self.temp_count[item] = self.temp_count[item] + 1
        else:
            self.temp_count[item] = 1
        if not self.max_count:
            self.max_count = item
        elif self.temp_count[self.max_count] < self.temp_count[item]:
            self.max_count = item


    def get_max(self):
        return self.max

    def get_min(self):
        return self.min

    def get_mean(self):
        return self.mean

    def get_mode(self):
        return self.max_count

class Test(unittest.TestCase):

    def test_tracker_usage(self):
        tracker = TempTracker()

        tracker.insert(50)
        msg = 'failed on first temp recorded'
        self.assertEqual(tracker.get_max(), 50, msg='max ' + msg)
        self.assertEqual(tracker.get_min(), 50, msg='min ' + msg)
        self.assertEqual(tracker.get_mean(), 50.0, msg='mean ' + msg)
        self.assertEqual(tracker.get_mode(), 50, msg='mode ' + msg)

        tracker.insert(80)
        msg = 'failed on higher temp recorded'
        self.assertEqual(tracker.get_max(), 80, msg='max ' + msg)
        self.assertEqual(tracker.get_min(), 50, msg='min ' + msg)
        self.assertEqual(tracker.get_mean(), 65.0, msg='mean ' + msg)
        self.assertIn(tracker.get_mode(), [50, 80], msg='mode ' + msg)

        tracker.insert(80)
        msg = 'failed on third temp recorded'
        self.assertEqual(tracker.get_max(), 80, msg='max ' + msg)
        self.assertEqual(tracker.get_min(), 50, msg='min ' + msg)
        self.assertEqual(tracker.get_mean(), 70.0, msg='mean ' + msg)
        self.assertEqual(tracker.get_mode(), 80, msg='mode ' + msg)

        tracker.insert(30)
        msg = 'failed on lower temp recorded'
        self.assertEqual(tracker.get_max(), 80, msg='max ' + msg)
        self.assertEqual(tracker.get_min(), 30, msg='min ' + msg)
        self.assertEqual(tracker.get_mean(), 60.0, msg='mean ' + msg)
        self.assertEqual(tracker.get_mode(), 80, msg='mode ' + msg)

if __name__=='__main__':
    unittest.main()