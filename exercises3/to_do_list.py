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

class ToDoList:
    def __init__(self):
        self.tasks = []
        self.current_id = 0

    # def add_task(self):
    #     new_task = input("Dodaj nowe zadanie: ")
    #     self.tasks.append(new_task)
    #     return self.tasks
    #
    # def remove_task(self):
    #     self.tasks.pop(int(input("Które zadanie chcesz usunąć?: ")))
    #     return self.tasks
    #
    # def mark_task_as_done(self):
    #     pass
    #
    # def get_all_tasks(self):
    #     print(self.tasks)
    #     return self.tasks

    def add_task(self, task):
        self.current_id += 1
        self.tasks.append({'id': self.current_id, 'task': task, 'done': False})
        return self.current_id

    # będziemy później robić bazę danych pod to
    # auto inkrementacja- baza danych sama dodaje kolejne idki d kolejnych rekordów, indeksuje od 1 później

    def remove_task(self, task_id):
        new_tasks = []
        for task in self.tasks:
            if task['id'] != task_id:
                new_tasks.append(task)
            self.tasks = new_tasks

    def mark_task_as_done(self, task_id):
        for task in self.tasks:
            if task['id'] == task_id:
                task['done'] = True
                break

    # self.tasks[task_id-1] ['done'] = True
    # to nie zadziała, bo mamy możliwość usunięcia i task_id oznaczy 'done' na konkretnym indeksie z listy,
    # a nie id, którym chcemy oznaczyć jako done, a używając wyżej tego ifa szukamy elementu z konkretnym id
    # w liście

    def get_all_tasks(self):
        return self.tasks


if __name__ == '__main__':
    todolist = ToDoList()
    # print(todolist.get_all_tasks())
    todolist.add_task('Zadanie testowe')
    # print(todolist.get_all_tasks())
    # [{'id': 1, 'task': 'Zadanie testowe', 'done': False}]
    todolist.add_task('Kolejne zadanie')
    # print(todolist.get_all_tasks())
    # [{'id': 1, 'task': 'Zadanie testowe', 'done': False}, {'id': 2, 'task': 'Kolejne zadanie', 'done': False}]
    todolist.remove_task(1)
    # print(todolist.get_all_tasks())
    # [{'id': 2, 'task': 'Kolejne zadanie', 'done': False}]
    todolist.mark_task_as_done(2)
    # print(todolist.get_all_tasks())
    # [{'id': 2, 'task': 'Kolejne zadanie', 'done': True}]
    todolist.add_task('Następne zadanie')
    todolist.add_task('jeszcze jedno zadanie')
    # print (todolist.get_all_tasks())
    # [{'id': 2, 'task': 'Kolejne zadanie', 'done': True}, {'id': 3, 'task': 'Następne zadanie', 'done': False},
    # {'id': 4, 'task': 'jeszcze jedno zadanie', 'done': False}]
    todolist.remove_task(4)
    todolist.add_task('Nowe zadanie')
    print(todolist.get_all_tasks())
    # [{'id': 2, 'task': 'Kolejne zadanie', 'done': True}, {'id': 3, 'task': 'Następne zadanie', 'done': False},
    # {'id': 5, 'task': 'Nowe zadanie', 'done': False}]
