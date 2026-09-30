def AddBooks(books):
    while True:
        ID = input("Enter book id:")
        title = input("Enter title of the book:")
        aut = input("Enter author name:")
        pr = input("Enter price of the book:")
        qty = int(input("Enter number of books available(quantity):"))
        shelf = int(input("Enter shelf number:"))

        books.append([ID, title, aut, pr, qty, shelf])

        ans = input('Do you want to add more books?(y/n):')
        if ans == 'n':
            break


def RemoveBooks(books):
    ans = input("Delete book by title(A)/by book id(B)/Delete all book details(C):")

    if ans == 'A':
        name = input("Enter name of the book to be deleted:")

        for k in books:
            if k[1] == name:
                books.remove(k)

        print("Deleted!!")

    elif ans == 'B':
        ID = input("Enter book id of the book to be deleted:")

        for k in books:
            if k[0] == ID:
                books.remove(k)

        print("Deleted!!")

    elif ans == 'C':
        books.clear()
        print("Details of all books Deleted!!")

    else:
        print("Invalid choice!!")
