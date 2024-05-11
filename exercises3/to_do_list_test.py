from to_do_list import ToDoList
import unittest


class ToDoListTest(unittest.TestCase):
    # def setUp(self):
    #     self.list = List()
    @classmethod
    def setUpClass(cls):
        cls.list = ToDoList()

    def test_1_add_task(self):
        # metoda nam zwraca numer idka, jaki został dodany, więc może być sprawdzenie, czy liczba elementów w liście
        # równa się numerowi zadania? Czy zawiera wszystkie elementy: id, treść i czy done?
        pass

    def test_2_remove_task(self):
        pass

    def test_3_mark_task_as_done(self):
        pass

    def test_4_get_all_tasks(self):
        pass


if __name__ == '__main__':
    unittest.main()
