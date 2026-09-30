def SearchBook(books):
    flag = 0

    ans = input("Search book details by Title(A)/by ID(B):")

    if ans == 'A':
        title = input("Enter title of the book to be searched:")

        for k in books:
            if k[1] == title:
                print(k)
                flag = 1

        if flag == 0:
            print("Not found")

    elif ans == 'B':
        ID = input("Enter ID of the book to be searched:")

        for k in books:
            if k[0] == ID:
                print(k)
                flag = 1

        if flag == 0:
            print("Not found")

    else:
        print("Invalid choice!")
