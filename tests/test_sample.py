from unittest import TestCase

import sample


class Test(TestCase):
    def test_count_number_occurrence(self):
        list1 = [1,2,2,3,2,4,5]
        self.assertEqual([3,2],sample.count_number_occurrence(list1))
