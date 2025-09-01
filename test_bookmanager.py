from os import remove
import unittest
from book import Book
from bookmanager import BookManager

class TestBookManager(unittest.TestCase):
    def setUp(self):
        self.bookmanager = BookManager()

    def test_add_book(self):
        """Test menambahkan buku"""
        book = Book("Pemrograman", "Andi", 2020)
        self.bookmanager.add_book(book)
        self.assertEqual(1, self.bookmanager.get_book_count())

    def test_remove_existing_book(self):
        """Test menghapus buku yang ada"""
        book = Book("Basis Data", "Erlangga", 2021)
        self.bookmanager.add_book(book)

        removed = self.bookmanager.remove_book("Basis Data")
        self.assertTrue(removed)
        self.assertEqual(0, self.bookmanager.get_book_count())

    # Lengkapi Unit Test dibawah untuk buku yang memang tidak terdapat pada list
    def test_remove_non_existing_book(self):
        book = Book("Dunia Shopie", "Jostein Gaarder", 1994)
        self.bookmanager.add_book(book)

        removed = self.bookmanager.remove_book("Misteri Soliter")
        self.assertFalse(removed)
        self.assertEqual(1, self.bookmanager.get_book_count())

    # Lengkapi Unit Test dibawah untuk bmenacri buku berdasarkan penulis
    def test_find_books_by_author(self):
        book1 = Book("No Longer Human", "Osamu Dazai", 1948)
        book2 = Book("The Setting Sun", "Osamu Dazai", 1939)
        book3 = Book("Dunia Shopie", "Jostein Gaarder", 1994)
        book4 = Book("Janji", "Tere Liye", 2013)
        self.bookmanager.add_book(book1)
        self.bookmanager.add_book(book2)
        self.bookmanager.add_book(book3)
        self.bookmanager.add_book(book4)

        result = self.bookmanager.find_books_by_author("Osamu Dazai")
        self.assertEqual(2, len(result))
        self.assertIn(book1, result)
        self.assertIn(book2, result)

    # Lengkapi Unit Test dibawah untuk seluruh buku yang ada di dalam list
    def test_get_all_books(self):
        book1 = Book("Sagaras", "Tere Liye", 2018)
        book2 = Book("Animal Farm", "George Orwell", 1945)
        self.bookmanager.add_book(book1)
        self.bookmanager.add_book(book2)

        all_books = self.bookmanager.get_all_books()
        self.assertEqual(2, len(all_books))
        self.assertIn(book1, all_books)
        self.assertIn(book2, all_books)

if __name__ == '__main__':
    unittest.main()
