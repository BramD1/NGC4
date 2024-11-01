# library_catalog.py

class Book:
    """
    Represents a book in the library.

    Attributes:
        title (str): The title of the book.
        author (str): The author of the book.
        identifier (str): A unique identifier for the book.
    """
    def __init__(self, title, author, identifier):
        """
        Initializes a Book instance with a title, author, and unique identifier.

        Args:
            title (str): The title of the book.
            author (str): The author of the book.
            identifier (str): A unique identifier for the book.
        """
        self.title = title
        self.author = author
        self.identifier = identifier


class LibraryCatalog:
    """
    Manages a catalog of books with functionalities to add, search, remove, and display books.

    Attributes:
        catalog (dict): A dictionary to store books with the book identifier as the key.
    """
    def __init__(self):
        """
        Initializes an empty catalog.
        """
        self.catalog = {}

    def add_book(self, book):
        """
        Adds a book to the catalog if it does not already exist.

        Args:
            book (Book): The book to be added to the catalog.

        Raises:
            ValueError: If a book with the same identifier already exists in the catalog.
        """
        if book.identifier in self.catalog:
            raise ValueError("A book with this identifier already exists.")
        self.catalog[book.identifier] = book
        print(f"Book '{book.title}' by {book.author} added successfully.")

    def search_by_title(self, title):
        """
        Searches for books in the catalog by title.

        Args:
            title (str): The title to search for.

        Returns:
            list: A list of books that match the title.
        """
        return [book for book in self.catalog.values() if title.lower() in book.title.lower()]

    def search_by_author(self, author):
        """
        Searches for books in the catalog by author.

        Args:
            author (str): The author to search for.

        Returns:
            list: A list of books that match the author.
        """
        return [book for book in self.catalog.values() if author.lower() in book.author.lower()]

    def remove_book(self, identifier):
        """
        Removes a book from the catalog by its identifier.

        Args:
            identifier (str): The unique identifier of the book to remove.

        Raises:
            KeyError: If the book with the identifier is not found.
        """
        if identifier not in self.catalog:
            raise KeyError("Book not found in catalog.")
        del self.catalog[identifier]
        print(f"Book with ID '{identifier}' has been removed from the catalog.")

    def display_catalog(self):
        """
        Displays all books in the catalog.

        Returns:
            list: A list of tuples containing book details (title, author, identifier).
        """
        if not self.catalog:
            print("The catalog is empty.")
            return []
        
        for book in self.catalog.values():
            print(f"ID: {book.identifier}, Title: '{book.title}', Author: {book.author}")
