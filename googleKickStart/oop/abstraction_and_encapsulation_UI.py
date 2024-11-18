class Library:
    def __init__(self, books):
        self.books = books
    def display_available_books(self):
        print(f"The available books: {self.books}")
    def lend_book(self, book):
        self.books.remove(book)
    def add_book(self, book):
        self.books.append(book)
class Customer:
    def __init__(self):
        self.books = []
    def borrow_book(self, library):
        book = input("Enter the name of the book you want to borrow: ")
        if book in library.books:
            library.lend_book(book)
            self.books.append(book)
            print(f"You have borrowed: {book}")
        else:
            print(f"The requested book: '{book}' is not available in the library")
    def return_book(self, library):
        book = input("Enter the name of the book you want to return: ")
        if book in self.books:
            library.add_book(book)
            self.books.remove(book)
            print(f"You have returned: {book}")
        else:
            print(f"This book: '{book}' doesn't exist in your library")

library = Library(['book 1', 'book 2', 'book 3', 'book 4', 'book 5', 'book 6', 'book 7', 'book 8', 'book 9', 'book 10'])
customer = Customer()

while True:
    print('Enter 1 to display the available books')
    print('Enter 2 to borrow a book')
    print('Enter 3 to return a book')
    print('Enter any other number to leave the library')
    user_input = int(input("Your choice: "))
    match user_input:
        case 1:
            library.display_available_books()
        case 2:
            customer.borrow_book(library)
        case 3:
            customer.return_book(library)
        case _:
            print("See you later :)")
            quit()