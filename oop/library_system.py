# Base Class - Book
class Book:
    def __init__(self, title, author):
        """
        Constructor for Book class
        Args:
            title (str): Title of the book
            author (str): Author of the book
        """
        self.title = title
        self.author = author

    def __str__(self):
        """
        String representation for Book
        Returns:
            str: Details of the book in a human-readable format
        """
        return f"Book: {self.title} by {self.author}"


# Derived Class - EBook
class EBook(Book):
    def __init__(self, title, author, file_size):
        """
        Constructor for EBook class, extends Book class
        Args:
            title (str): Title of the e-book
            author (str): Author of the e-book
            file_size (int): Size of the e-book file in KB
        """
        super().__init__(title, author)
        self.file_size = file_size

    def __str__(self):
        """
        String representation for EBook
        Returns:
            str: Details of the e-book, including file size
        """
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"


# Derived Class - PrintBook
class PrintBook(Book):
    def __init__(self, title, author, page_count):
        """
        Constructor for PrintBook class, extends Book class
        Args:
            title (str): Title of the print book
            author (str): Author of the print book
            page_count (int): Number of pages in the book
        """
        super().__init__(title, author)
        self.page_count = page_count

    def __str__(self):
        """
        String representation for PrintBook
        Returns:
            str: Details of the print book, including page count
        """
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"


# Composition - Library Class
class Library:
    def __init__(self):
        """
        Constructor for Library class
        Initializes an empty list to store books
        """
        self.books = []

    def add_book(self, book):
        """
        Method to add a book to the library
        Args:
            book (Book): An instance of Book, EBook, or PrintBook
        """
        self.books.append(book)

    def list_books(self):
        """
        Method to list all books in the library with their details
        """
        for book in self.books:
            print(book)
