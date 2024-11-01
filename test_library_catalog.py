# test_library_catalog.py

import unittest
from library_catalog import Book, LibraryCatalog

class TestLibraryCatalog(unittest.TestCase):
    def setUp(self):
        """
        Set up a new LibraryCatalog instance and a sample book before each test.
        """
        self.catalog = LibraryCatalog()
        self.book1 = Book("Python Programming", "John Doe", "001")
        self.book2 = Book("Data Science with Python", "Jane Smith", "002")
        self.catalog.add_book(self.book1)
        self.catalog.add_book(self.book2)

    def test_add_book(self):
        """
        Test adding a new book to the catalog.
        """
        book3 = Book("Machine Learning Basics", "Sam Brown", "003")
        self.catalog.add_book(book3)
        self.assertIn("003", self.catalog.catalog)
        with self.assertRaises(ValueError):
            self.catalog.add_book(book3)

    def test_search_by_title(self):
        """
        Test searching for books by title.
        """
        results = self.catalog.search_by_title("Python")
        self.assertEqual(len(results), 2)
        self.assertIn(self.book1, results)

    def test_search_by_author(self):
        """
        Test searching for books by author.
        """
        results = self.catalog.search_by_author("Jane")
        self.assertEqual(len(results), 1)
        self.assertIn(self.book2, results)

    def test_remove_book(self):
        """
        Test removing a book from the catalog by identifier.
        """
        self.catalog.remove_book("002")
        self.assertNotIn("002", self.catalog.catalog)
        with self.assertRaises(KeyError):
            self.catalog.remove_book("999")  # Non-existent ID

    def test_display_catalog(self):
        """
        Test displaying all books in the catalog.
        """
        output = self.catalog.display_catalog()
        self.assertIsInstance(output, list)
        self.assertEqual(len(output), 2)  # Assuming two books are initially added
        self.assertEqual(output[0]["ID"], "001")
        self.assertEqual(output[1]["Title"], "Python Programming")


if __name__ == "__main__":
    unittest.main()
