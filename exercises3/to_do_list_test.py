from to_do_list import ToDoList
import unittest


class ToDoListTest(unittest.TestCase):
    # def setUp(self):
    #     self.list = List()
    # class method nam pozwala na to, że efekt każdego testu zostaje zachowane do następnego
    @classmethod
    def setUpClass(cls):
        cls.todolist = ToDoList()

    def test_0_get_all_tasks(self):
        self.assertEqual(0, len(self.todolist.get_all_tasks()))

    def test_1_add_task(self):
        size = len(self.todolist.get_all_tasks())
        # self.assertEqual(0, len(self.todolist.get_all_tasks()))
        test_id = self.todolist.add_task("Zadanie 1")
        self.assertEqual(size + 1, len(self.todolist.get_all_tasks()))
        # self.assertEqual({'id': 1, 'task': "Zadanie 1", "done": False}, self.todolist.get_all_tasks()[0])
        # Zastąpienie asercji wyżej trzema asercjami sprawdzającymi wartości dodane w pojedynczych kluczach:
        self.assertEqual(test_id, self.todolist.get_all_tasks()[-1]['id'])
        self.assertEqual("Zadanie 1", self.todolist.get_all_tasks()[-1]['task'])
        self.assertEqual(False, self.todolist.get_all_tasks()[-1]['done'])

    def test_2_remove_task(self):
        size = len(self.todolist.get_all_tasks())
        test_id = self.todolist.add_task("Zadanie 2")
        self.assertEqual(size + 1, len(self.todolist.get_all_tasks()))
        self.todolist.remove_task(test_id)
        self.assertEqual(size, len(self.todolist.get_all_tasks()))

    def test_3_mark_task_as_done(self):
        test_id = self.todolist.add_task("Zadanie 3")
        # Sprawdzenie, że przed wykonaniem metody mark as done, mamy na liście w ostatnim indeksie [-1] z kluczem 'done'
        # połączoną wartość false
        self.assertFalse(self.todolist.get_all_tasks()[-1]['done'])
        # wykonanie metody mark as done
        self.todolist.mark_task_as_done(test_id)
        # i sprawdzenie już, że zmieniła nam się wartość z false na true
        self.assertTrue(self.todolist.get_all_tasks()[-1]['done'])
        # self.skipTest('not done yet')


if __name__ == '__main__':
    unittest.main()
