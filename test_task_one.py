import unittest
import task_one

class TestAscendingFunction(unittest.TestCase):
    def test_that_function_is_not_null(self):
        self.assertIsNotNone(task_one.sort_in_ascending_order)


    def test_function_ascending_order(self):
        list1 = [56, 76, 4, 8, 20, 36]
        result = [4, 8, 20, 36, 56, 76]
        self.assertEqual(task_one.sort_in_ascending_order(list1),result)
