class Book:
    def __init__(self):
        self.book_id = ""
        self.title = ""
        self.author_id = ""
        self.publisher = ""
        self.year_of_publication = ""
    def create_new_Book(self):
        self.book_id = input("Enter Book ID : ")
        self.title = input("Enter Book Title: ")
        self.author_id = input("Enter Author ID: ")
        self.publisher = input("Enter Publisher: ")
        self.year_of_publication = input("Enter Year of Publication: ")

    def display_Book(self):
        print(self.book_id)
        print(self.title)
        print(self.author_id)
        print(self.publisher)
        print(self.year_of_publication)


class Author:
    def __init__(self):
        self.ID = ""

    def create_new_Author(self):
        self.author_id = ""
        self.name = ""
        self.affiliation = ""
        self.year_of_publication = ""

    def display_Author(self):
        self.author_id = input("Enter Author ID: ")
        self.name = input("Enter Author Name: ")
        self.affiliation = input("Enter Affiliation: ")
        self.year_of_publication = input("Enter Year of Publication: ")


class User:
    def __init__(self):
        self.ID = ""

    def create_new_User(self):
        self.user_id = ""
        self.name = ""
        self.password = ""
        self.phone = ""
        self.email_id = ""
        self.booksborrowed = ""

    def display_User(self):
        self.user_id = input("Enter User ID: ")
        self.name = input("Enter User Name: ")
        self.password = input("Enter User Password: ")
        self.phone = input("Enter User Phone Number: ")
        self.email_id = input("Enter User Email ID: ")
        self.booksborrowed = input("Enter Books borrowed: ")

Books = []
Authors = []
Users = []

while (True):
    print("Welcome to Faculty")
    print("Enter your choice:")
    print("1. Create new Book")
    print("2. Create new Author")
    print("3. Create new User")
    print("4. Display Book")
    print("5. Display Author")
    print("6. Display User")
    print("5. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        book = Book()
        book.create_new_Book()
        Books.append(book)
    elif choice == "2":
        create_new_author
    elif choice == "3":
        create_new_User()
    elif choice == "4":
        display_Book()
    elif choice == "5":
        display_Autho()
    elif choice == "6":
        display_User()
    elif choice == "6":
        break

