class library:
  def __init__(self):
    self.no_of_books = 0
    self.books = []

  def addbook(self, name_of_book):
    self.books.append(name_of_book)
    self.no_of_books = len(self.books)
    

  def removebook(self, name_of_book):
    self.books.remove(name_of_book)
    self.no_of_books = len(self.books)
    

  def showinfo(self):
    print(f"Total number of books are {self.no_of_books}")
    print(f"Books are {self.books}")

book = library()

book.addbook("java")
book.showinfo()

