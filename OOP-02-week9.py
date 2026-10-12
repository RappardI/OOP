import pickle

class Author:
    def display_Author(self):

    s1 = Author()
    s1.create_new_Author()
    s1.display_Author()

file1 = open("myAuthors.dat", "ab")
pickle.dump(s1, file1)
file1.close()

file2 = open("myAuthors.dat", "rb")
while(1):
    try:
        data = pickle.load(file2)
        print(data.name)
        print(data.id)
        print(data.major)

    except EOFError:
        break
file2.close()