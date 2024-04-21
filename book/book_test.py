from book import Book
import unittest


class TestBook(unittest.TestCase):
    def setUp(self):
        self.book = Book("Wiedźmin", "Sapkowski", 1997)

    def test_1_get_info(self):
        text_correct = "Tytuł: Wiedźmin Autor: Sapkowski Rok: 1997"
        text_result = self.book.get_info()
        self.assertEqual(text_correct, text_result)

    def test_2_change_title(self):
        self.book.change_title("Miecz przeznaczenia")
        # text_correct = 'Tytuł: Miecz przeznaczenia Autor: Sapkowski Rok: 1997'
        # text_result = self.book.get_info()
        # self.assertEqual(text_correct, text_result)
        text_correct = "Miecz przeznaczenia"
        text_result = self.book.title
        self.assertEqual(text_correct, text_result)

    def test_3_change_author(self):
        self.book.change_author("Mickiewicz")
        text_correct = "Mickiewicz"
        text_result = self.book.author
        self.assertEqual(text_correct, text_result)

    def test_4_change_year(self):
        self.book.change_year(1800)
        text_correct = 1800
        text_result = self.book.year
        self.assertEqual(text_correct, text_result)


if __name__ == '__main__':
    unittest.main()
