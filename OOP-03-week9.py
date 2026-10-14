import pickle
class Book:
    def __init__(self):
        self.book_id = ""
        self.title = ""
        self.author_id = ""
        self.publisher = ""
        self.year_of_publication = ""

    def create_new_Book(self):
        self.book_id = input("Enter Book ID: ")
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
        self.author_id = ""
        self.name = ""
        self.affiliation = ""
        self.year_of_publication = ""

    def create_new_Author(self):
        self.author_id = input("Enter Author ID: ")
        self.name = input("Enter Author Name: ")
        self.affiliation = input("Enter Affiliation: ")
        self.year_of_publication = input("Enter Year of Publication: ")

    def display_Author(self):
        print(self.author_id)
        print(self.name)
        print(self.affiliation)
        print(self.year_of_publication)


class User:
    def __init__(self):
        self.user_id = ""
        self.name = ""
        self.password = ""
        self.phone = ""
        self.email_id = ""
        self.booksborrowed = ""

    def create_new_User(self):
        self.user_id = input("Enter User ID: ")
        self.name = input("Enter User Name: ")
        self.password = input("Enter User Password: ")
        self.phone = input("Enter User Phone Number: ")
        self.email_id = input("Enter User Email ID: ")
        self.booksborrowed = input("Enter Books borrowed: ")

    def display_User(self):
        print(self.user_id)
        print(self.name)
        print(self.password)
        print(self.phone)
        print(self.email_id)
        print(self.booksborrowed)

while True:
    print("Welcome to Faculty")
    print("Enter your choice:")
    print("1. Create new Book")
    print("2. Create new Author")
    print("3. Create new User")
    print("4. Display Book")
    print("5. Display Author")
    print("6. Display User")
    print("7. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        book = Book()
        book.create_new_Book()
        book_file = open("mybooks.dat", "ab")
        pickle.dump(book, book_file)
        book_file.close()


    elif choice == "2":
        author = Author()
        author.create_new_Author()
        author_file = open("myauthors.dat", "ab")
        pickle.dump(author, author_file)
        author_file.close()

    elif choice == "3":
        user = User()
        user.create_new_User()
        user_file = open("myusers.dat", "ab")
        pickle.dump(user, user_file)
        user_file.close()

    elif choice == "4":
        read_book_file = open("mybooks.dat", "rb")
        display_books = pickle.load(read_book_file)
        for book in display_books:
            book.display_Book()
        read_book_file.close()

    elif choice == "5":
        for author in Authors:
            read_author_file = open("myauthors.dat", "rb")
            display_author = pickle.load(read_author_file)
            pickle.dump(display_author, author_file)

    elif choice == "6":
        for user in Users:
            read_user_file = open("myusers.dat", "rb")
            display_user = pickle.load(read_user_file)
            pickle.dump(display_user, user_file)

    elif choice == "7":
        break