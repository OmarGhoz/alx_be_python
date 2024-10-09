class Book:
    def __init__(self, title, author, year):
        """
        Constructor to initialize the Book instance.
        Args:
            title (str): The title of the book.
            author (str): The author of the book.
            year (int): The publication year of the book.
        """
        self.title = title
        self.author = author
        self.year = year

    def __del__(self):
        """
        Destructor to print a message when the Book instance is deleted.
        """
        print(f"Deleting {self.title}")

    def __str__(self):
        """
        String representation of the book for readability.
        Returns:
            str: Human-readable string format.
        """
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        """
        Official representation of the Book instance.
        Returns:
            str: String format that could recreate the Book object.
        """
        return f"Book('{self.title}', '{self.author}', {self.year})"
