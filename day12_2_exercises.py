class Book:

	def __init__(self, title, author, is_borrowed = False):
		self.title = title
		self.author = author
		self.is_borrowed = is_borrowed

	def borrow(self):
		self.is_borrowed = True

	def return_book(self):
		self.is_borrowed = False

class Library:

	def __init__(self, books = []):
		self.books = books

	def add_book(self, book):
		self.books.append(book)

	def show_available_books(self):
		for book in self.books:
			if book.is_borrowed == False:
				print(f"{book.title} by {book.author}")

book1 = Book("Lords of the Rings", "Billy gate")
book2 = Book("Crazy Island", "Idan Widad", True)


lib = Library()
lib.add_book(book1)
book2.return_book()
lib.add_book(book2)
lib.show_available_books()
print(lib.books)
