import pymysql


class ToDoList:
    def __init__(self, db):
        self.db = db
        self.cursor = self.db.cursor(pymysql.cursors.DictCursor)
        # pymysql.cursors.DictCursor > czyli przekształcaj na słownik zwrotkę z tabeli- zwraca wtedy z nazwami kolumn:
        # [{'id': 1, 'task': 'Pierwsze zadanie', 'done': 0}, {'id': 2, 'task': 'Drugie zadanie', 'done': 1},
        # {'id': 3, 'task': 'Trzecie zadanie', 'done': 0}]

    def add_task(self, task):
        # sql = INSERT INTO tasks (id, task, done) VALUES (NULL, 'Pierwsze zadanie', '0')
        # ale id jest autoinkrementowane, więc będzie dodawane i tak po kolei z automatu, więc wystarczy tak:
        # sql = INSERT INTO tasks(task, done) VALUES ('Pierwsze zadanie', '0')
        # sql = "INSERT INTO tasks (task, done) VALUES ('+tasks+', 0)" -> ale jest security issue, bo podatne na
        # iniekcje kodu
        # schemat dodawanego rekordu:
        sql = "INSERT INTO tasks (task, done) VALUES (%s, %s)"
        # bindowanie danych, żeby zabezpieczyć przed insertowaniem dowolnego stringa
        self.cursor.execute(sql, (task, False))
        self.db.commit()
        # wcześniej mieliśmy w zwrotce id dodanego zadania, więc teraz też:
        return self.cursor.lastrowid

    # auto inkrementacja- baza danych sama dodaje kolejne idki d kolejnych rekordów, indeksuje od 1 później

    def remove_task(self, task_id):
        sql = "DELETE FROM tasks WHERE id = %s"
        self.cursor.execute(sql, (task_id))
        self.db.commit()

    def mark_task_as_done(self, task_id):
        sql = "UPDATE tasks SET done = TRUE WHERE id = %s"
        self.cursor.execute(sql, (task_id))
        self.db.commit()

    def get_all_tasks(self):
        sql = "SELECT * FROM tasks"
        self.cursor.execute(sql)
        return self.cursor.fetchall()


if __name__ == '__main__':
    db = pymysql.connect(host='localhost', user='root', password='', db='todolist')
    todolist = ToDoList(db)

    print(todolist.get_all_tasks())
    task_id = todolist.add_task('Kolejne zadanie')
    print(todolist.get_all_tasks())
    todolist.mark_task_as_done(task_id)
    print(todolist.get_all_tasks())
    todolist.remove_task(task_id)
    print(todolist.get_all_tasks())
    # zamknięcie połączenia z bazą
    db.close()

# query do stworzenia bazy danych:
# CREATE TABLE todolist.tasks (id INT NOT NULL AUTO_INCREMENT , task TEXT NOT NULL ,
# done BOOLEAN NULL DEFAULT FALSE , PRIMARY KEY (id)) ENGINE = InnoDB;

# INSERT INTO tasks (id, task, done) VALUES ('1', 'Pierwsze zadanie', '0');
