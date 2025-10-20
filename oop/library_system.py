class Book:
    def __init__(self, title, author):
        """Initialize the base Book class."""
        self.title = title
        self.author = author

    def __str__(self):
        """Return a string representation of the book."""
        return f"Book: {self.title} by {self.author}"


class EBook(Book):
    def __init__(self, title, author, file_size):
        """Initialize an EBook, calling the base class constructor."""
        super().__init__(title, author)
        self.file_size = file_size

    def __str__(self):
        """Return a string representation of an EBook."""
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"


class PrintBook(Book):
    def __init__(self, title, author, page_count):
        """Initialize a PrintBook, calling the base class constructor."""
        super().__init__(title, author)
        self.page_count = page_count

    def __str__(self):
        """Return a string representation of a PrintBook."""
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"


class Library:
    def __init__(self):
        """Initialize the Library with an empty book collection."""
        self.books = []

    def add_book(self, book):
        """Add a book (Book, EBook, or PrintBook) to the library."""
        self.books.append(book)

    def list_books(self):
        """List all books currently in the library."""
        for book in self.books:
            print(book)