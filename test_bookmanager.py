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
        """Test mencari buku berdasarkan author"""

    # Lengkapi Unit Test dibawah untuk seluruh buku yang ada di dalam list
    def test_get_all_books(self):
        """Test mendapatkan semua buku"""

if __name__ == '__main__':
    unittest.main()
