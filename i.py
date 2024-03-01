from abc import ABC, abstractmethod

class search(ABC):
    @abstractmethod
    def search_books(self, book_name):
        print("searching books")

class Borrow(ABC):
    @abstractmethod
    def borrow_books(self, book_name):
        print("borrowing books")

    @abstractmethod
    def return_books(self, book_name):
        print("returning books")

class AddDelete(ABC):
    @abstractmethod
    def add_books(self, book_name):
        print("adding books")

    @abstractmethod
    def delete_books(self, book_name):
        print("deleting books")

class Librarian(search, Borrow, AddDelete):
    def __init__(self):
        print("Librarian class object created")

    def search_books(self, book_name):
        print(f"searching book {book_name} in catalog")
    
    def borrow_books(self, book_name):
        print(f"borrowing book {book_name} from catalog")
    
    def return_books(self, book_name):
        print("returning book to catalog")
    
    def add_books(self, book_name):
        print(f"adding book {book_name} to catalog")
    
    def delete_books(self, book_name):
        print("deleting books from catalog")
    
    def generate_report(self): 
        print("generating report")

class LibraryMember(search, Borrow):
    def __init__(self):
        print("LibraryMember created")

    def search_books(self, book_name):
        print(f"searching book {book_name} in catalog")
    
    def borrow_books(self, book_name, user_name):
        print(f"{user_name} borrowing book {book_name} from catalog")
    
    def return_books(self, book_name, user_name):
        print(f"{user_name} returning book {book_name} to catalog")


# sample usage
def main():
    librarian = Librarian()
    librarian.search_books("Python")
    librarian.borrow_books("Python")
        
    librarian.add_books("The Bible")

    member = LibraryMember()
    member.search_books("Python")

    member.borrow_books("Python", "John")

if __name__ == "__main__":
    main()