# Zadanie 3*:
# Utwórz klasę TodoList, która pozwoli na zarządzanie listą zadań do wykonania. Napisz testy jednostkowe.
#
# Kroki:
# Utwórz szkielet klasy:
# Metody: add_task, remove_task, mark_task_as_done, get_all_tasks.
# Napisz testy jednostkowe:
# Test dla dodania nowego zadania do listy.
# Test dla usunięcia zadania z listy.
# Test dla oznaczenia zadania jako wykonane.
# Test dla otrzymywania listy wszystkich zadań.
# Implementuj metody klasy:
# Uzupełnij metody zarządzania zadaniami, aby wszystkie testy przeszły pomyślnie.

class List:
    def __init__(self):
        self.tasks = ["Do the laundry", "Buy some groceries", "Go for a walk"]

    def add_task(self):
        new_task = input("Dodaj nowe zadanie: ")
        self.tasks.append(new_task)
        return self.tasks

    def remove_task(self):
        self.tasks.pop(int(input("Które zadanie chcesz usunąć?: ")))
        return self.tasks

    def mark_task_as_done(self):
        pass

    def get_all_tasks(self):
        print(self.tasks)
        return self.tasks

