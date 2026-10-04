class BookNotAvailableError(Exception):
    pass
try:
    book_available = False
    if not book_available:
        raise BookNotAvailableError("Book is not available")
    print("Book is available")
except BookNotAvailableError as e:
    print("Error:", e)