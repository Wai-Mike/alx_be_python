class Book:
    """
    A Book class representing a book in the library system.
    Contains public attributes for title and author, and a private attribute
    to track checkout status.
    """
    
    def __init__(self, title, author):
        """
        Initialize a Book with title and author.
        
        Args:
            title (str): The title of the book
            author (str): The author of the book
        """
        self.title = title
        self.author = author
        self._is_checked_out = False
    
    def check_out(self):
        """
        Check out the book (mark as unavailable).
        
        Returns:
            bool: True if successfully checked out, False if already checked out
        """
        if self._is_checked_out:
            return False
        else:
            self._is_checked_out = True
            return True
    
    def return_book(self):
        """
        Return the book (mark as available).
        
        Returns:
            bool: True if successfully returned, False if already available
        """
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        else:
            return False
    
    def is_available(self):
        """
        Check if the book is available for checkout.
        
        Returns:
            bool: True if available, False if checked out
        """
        return not self._is_checked_out
    
    def __str__(self):
        """
        String representation of the book.
        
        Returns:
            str: Formatted string with title and author
        """
        return f"{self.title} by {self.author}"


class Library:
    """
    A Library class that manages a collection of books.
    Uses a private list to store Book instances and provides methods
    for book management operations.
    """
    
    def __init__(self):
        """Initialize an empty library."""
        self._books = []
    
    def add_book(self, book):
        """
        Add a book to the library collection.
        
        Args:
            book (Book): The book instance to add to the library
        """
        self._books.append(book)
    
    def check_out_book(self, title):
        """
        Check out a book by its title.
        
        Args:
            title (str): The title of the book to check out
            
        Returns:
            bool: True if successfully checked out, False if not found or already checked out
        """
        for book in self._books:
            if book.title == title:
                return book.check_out()
        return False
    
    def return_book(self, title):
        """
        Return a book by its title.
        
        Args:
            title (str): The title of the book to return
            
        Returns:
            bool: True if successfully returned, False if not found or already available
        """
        for book in self._books:
            if book.title == title:
                return book.return_book()
        return False
    
    def list_available_books(self):
        """
        List all available books in the library.
        Prints each available book on a separate line.
        """
        available_books = [book for book in self._books if book.is_available()]
        
        if not available_books:
            print("No books are currently available.")
        else:
            for book in available_books:
                print(book)
    
    def get_all_books(self):
        """
        Get all books in the library (both available and checked out).
        
        Returns:
            list: List of all Book instances in the library
        """
        return self._books.copy()
    
    def get_book_count(self):
        """
        Get the total number of books in the library.
        
        Returns:
            int: Total number of books
        """
        return len(self._books)
    
    def get_available_count(self):
        """
        Get the number of available books in the library.
        
        Returns:
            int: Number of available books
        """
        return len([book for book in self._books if book.is_available()])
