from to_do_list import List
import unittest


class ToDoListTest(unittest.TestCase):
    def setUp(self):
        self.list = List()

    def test_1_add_task(self):
        self.assertEqual(self.list.add_task(), self.list.tasks)

    def test_2_remove_task(self):
        self.assertEqual(self.list.remove_task(), self.list.tasks)

    def test_3_mark_task_as_done(self):
        pass

    def test_4_get_all_tasks(self):
        self.assertEqual(self.list.get_all_tasks(), self.list.tasks)


if __name__ == '__main__':
    unittest.main()
