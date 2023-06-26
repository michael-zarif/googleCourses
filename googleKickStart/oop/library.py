class Library:
    def __init__(self, books):
        self.books = books
    def display_available_books(self):
        return self.books
    def lend_book(self, book):
        self.books.remove(book)
    def add_book(self, book):
        self.books.append(book)
class Customer:
    def __init__(self):
        self.books = []
    def borrow_book(self, library, books):
        for book in books:
            if book in library.books:
                library.lend_book(book)
                self.books.append(book)
            else:
                print(f"The requested book: '{book}' is not available in the library")
    def return_book(self, library, books):
        for book in books:
            if book in self.books:
                library.add_book(book)
                self.books.remove(book)
            else:
                print(f"This book: '{book}' doesn't exist in your library")

lib1 = Library(['book 1', 'book 2', 'book 3', 'book 4', 'book 5', 'book 6', 'book 7', 'book 8', 'book 9', 'book 10'])
cust1 = Customer()
cust2 = Customer()
print(f'Current lib1 books count: {len(lib1.display_available_books())}, cust1 books count: {len(cust1.books)}, cust2 books count: {len(cust2.books)}')
cust1.borrow_book(lib1, ['book 1', 'book 3'])
print(f'Current lib1 books count: {len(lib1.display_available_books())}, cust1 books count: {len(cust1.books)}, cust2 books count: {len(cust2.books)}')
cust2.borrow_book(lib1, ['book 2', 'book 3'])
print(f'Current lib1 books count: {len(lib1.display_available_books())}, cust1 books count: {len(cust1.books)}, cust2 books count: {len(cust2.books)}')
cust1.return_book(lib1, ['book 3'])
print(f'Current lib1 books count: {len(lib1.display_available_books())}, cust1 books count: {len(cust1.books)}, cust2 books count: {len(cust2.books)}')
cust2.borrow_book(lib1, ['book 3', 'book 4'])
print(f'Current lib1 books count: {len(lib1.display_available_books())}, cust1 books count: {len(cust1.books)}, cust2 books count: {len(cust2.books)}')