#!/usr/bin/env python3
"""
Extended test script for the Library Management System.
This script demonstrates additional functionality and edge cases.
"""

from library_management import Book, Library

def test_library_system():
    """Test the Library Management System with various scenarios."""
    print("=== Library Management System Testing ===\n")
    
    # Create library and books
    library = Library()
    
    # Add multiple books
    books = [
        Book("Brave New World", "Aldous Huxley"),
        Book("1984", "George Orwell"),
        Book("To Kill a Mockingbird", "Harper Lee"),
        Book("The Great Gatsby", "F. Scott Fitzgerald"),
        Book("Pride and Prejudice", "Jane Austen")
    ]
    
    for book in books:
        library.add_book(book)
    
    print(f"Added {library.get_book_count()} books to the library.")
    print(f"Available books: {library.get_available_count()}")
    print()
    
    # Test initial state
    print("1. Initial available books:")
    library.list_available_books()
    print()
    
    # Test checking out books
    print("2. Checking out '1984' and 'The Great Gatsby':")
    result1 = library.check_out_book("1984")
    result2 = library.check_out_book("The Great Gatsby")
    print(f"Checked out '1984': {result1}")
    print(f"Checked out 'The Great Gatsby': {result2}")
    print(f"Available books: {library.get_available_count()}")
    library.list_available_books()
    print()
    
    # Test checking out already checked out book
    print("3. Trying to check out '1984' again:")
    result = library.check_out_book("1984")
    print(f"Result: {result}")
    print()
    
    # Test checking out non-existent book
    print("4. Trying to check out non-existent book 'Harry Potter':")
    result = library.check_out_book("Harry Potter")
    print(f"Result: {result}")
    print()
    
    # Test returning a book
    print("5. Returning '1984':")
    result = library.return_book("1984")
    print(f"Result: {result}")
    print(f"Available books: {library.get_available_count()}")
    library.list_available_books()
    print()
    
    # Test returning already available book
    print("6. Trying to return '1984' again:")
    result = library.return_book("1984")
    print(f"Result: {result}")
    print()
    
    # Test returning non-existent book
    print("7. Trying to return non-existent book 'Harry Potter':")
    result = library.return_book("Harry Potter")
    print(f"Result: {result}")
    print()
    
    # Test final state
    print("8. Final available books:")
    library.list_available_books()
    print(f"Total books: {library.get_book_count()}")
    print(f"Available books: {library.get_available_count()}")
    print(f"Checked out books: {library.get_book_count() - library.get_available_count()}")

def test_book_class():
    """Test the Book class functionality."""
    print("\n=== Book Class Testing ===\n")
    
    # Create a book
    book = Book("Test Book", "Test Author")
    print(f"Created book: {book}")
    print(f"Is available: {book.is_available()}")
    print()
    
    # Test checking out
    print("Checking out the book:")
    result = book.check_out()
    print(f"Check out result: {result}")
    print(f"Is available: {book.is_available()}")
    print()
    
    # Test checking out again
    print("Trying to check out again:")
    result = book.check_out()
    print(f"Check out result: {result}")
    print()
    
    # Test returning
    print("Returning the book:")
    result = book.return_book()
    print(f"Return result: {result}")
    print(f"Is available: {book.is_available()}")
    print()
    
    # Test returning again
    print("Trying to return again:")
    result = book.return_book()
    print(f"Return result: {result}")

if __name__ == "__main__":
    test_library_system()
    test_book_class()
