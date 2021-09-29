class Library:
    def __init__(self, books=None, librarian=None):
        self.__books = books
        self.__librarian = librarian

    def __find_book_by_author(self, name_author):
        for book in self.__books:
            if book.get_author() == name_author:
                print("[INFO] Книга с таким автором найдена!")
                return book
        print("[INFO] Книги с таким автором нет!")
        return None

    def __find_book_by_book(self, name_book):
        for book in self.__books:
            if book.get_name() == name_book:
                print("[INFO] Книга с таким названием найдена!")
                return book
        print("[INFO] Книги с таким названием нет!")
        return None

    def find_book(self, name_book='', name_author=''):
        if name_book == name_author == '':
            print("[ERROR] Пустые значения!")
            return None

        if name_book == '':
            return self.__find_book_by_author(name_author)

        if name_author == '':
            return self.__find_book_by_book(name_book)

        for book in self.__books:
            if book.get_name() == name_book and book.get_author() == name_author:
                print("[INFO] Книга с таким названием и автором найдена!")
                return book
        print("[INFO] Книги с таким названием и автором нет!")
        return None


class Librarian:
    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name


class Book:
    def __init__(self, name="", author=""):
        self.__name = name
        self.__author = author

    def get_name(self):
        return self.__name

    def get_author(self):
        return self.__author


class Author:
    def __init__(self, name):
        self.__name = name


class Visitor:
    __book = None

    def __init__(self):
        pass

    def read_book(self, book):
        self.__book = book
        print("[INFO] Посетитель читает книгу...")


if __name__ == "__main__":
    books = []
    for i in range(100):
        books.append(Book(f'book_{i}', f'author_{i}'))
        # print(books[i].get_name(), ' ', books[i].get_author())

    for i in books:
        print(i.get_name(), ' ', i.get_author())

    librarian = Librarian('Татьяна Викторовна')

    library = Library(books, librarian)

    visitor = Visitor()

    print("-"*30)
    answer = input("Как искать книгу? \n"
                   "1. По названию\n"
                   "2. По автору\n"
                   "3. По названию и автору\n"
                   "Укажите цифрой: ")
    name, author = "", ""
    if answer == "1":
        name = input("Введите название книги: ")
    elif answer == "2":
        author = input("Введите имя автора: ")
    elif answer == "3":
        name = input("Введите название книги: ")
        author = input("Введите имя автора: ")
    else:
        print("[ERROR] Неверное значение!!")
        exit(404)

    book = library.find_book(name, author)
    if book is not None:
        visitor.read_book(book)