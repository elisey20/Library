class Library:
    def __init__(self, books=None, librarian=""):
        self.__books = books
        self.__librarian = librarian


class Librarian:
    pass


class Book:
    def __init__(self, name="", author=""):
        self.__name = name
        self.__author = author


class Author:
    def __init__(self, name):
        self.__name = name


class Visitor:
    def __init__(self):
        pass

    def find_book(self, name_author):
        pass

    def find_book(self, name_book):
        pass


if __name__ == "__main__":

    library = Library()
