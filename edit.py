def EditBooks(books):
    FLAG = 0

    ans = input("Update book details by title(A)/book id(B):")

    def choice():
        if ans == 'A':
            print("What do you want to update?")
            print("ID(1),author(2),price(3),quantity(4),shelfno(5)")
            print("Hint:type the details what you want to update as a list")
            print("Eg:- [1,5] you can update ID and shelf number")

            name = input("Enter title of the book to update book details:")
            return name

        elif ans == 'B':
            print("What do you want to update?")
            print("title(1),author(2),price(3),quantity(4),shelfno(5)")
            print("Hint:type the details what you want to update as a list")
            print("Eg:- [1,5] you can update Title and shelf number")

            ID = input("Enter ID of the book to update book details:")
            return ID

        else:
            return None

    ch = choice()

    if ch == None:
        print("Invalid choice!")

    if ch != None:

        for k in books:

            if k[0] == ch or k[1] == ch:
                FLAG = 1
                break

        if FLAG == 1:

            a = eval(input("Enter the choices(list):"))

            for k in a:

                if k == 1 and ans == 'A':
                    ID = input("Enter new book id:")

                    for book in books:
                        if book[1] == ch:
                            book[0] = ID

                    print("Updated!")

                elif k == 1 and ans == 'B':
                    title = input("Enter new book Title:")

                    for book in books:
                        if book[0] == ch:
                            book[1] = title

                    print("Updated!")

                elif k == 2:
                    aut = input("Enter new author name:")

                    for book in books:
                        if ans == 'A' and book[1] == ch:
                            book[2] = aut

                        elif ans == 'B' and book[0] == ch:
                            book[2] = aut

                    print("Updated!")

                elif k == 3:
                    pr = float(input("Enter new price:"))

                    for book in books:
                        if ans == 'A' and book[1] == ch:
                            book[3] = pr

                        elif ans == 'B' and book[0] == ch:
                            book[3] = pr

                    print("Updated!")

                elif k == 4:
                    qty = int(input("Enter new quantity:"))

                    for book in books:
                        if ans == 'A' and book[1] == ch:
                            book[4] = qty

                        elif ans == 'B' and book[0] == ch:
                            book[4] = qty

                    print("Updated!")

                elif k == 5:
                    shelf = int(input("Enter new shelf number:"))

                    for book in books:
                        if ans == 'A' and book[1] == ch:
                            book[5] = shelf

                        elif ans == 'B' and book[0] == ch:
                            book[5] = shelf

                    print("Updated!")

                else:
                    print(k, 'is an invalid choice')

        if FLAG == 0:
            print("Invalid choice!")
