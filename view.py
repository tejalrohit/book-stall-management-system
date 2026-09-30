def View(books, customers, sales_details):

    print("Enter 1 to display all book details:")
    print("Enter 2 to display customer details:")
    print("Enter 3 to display sales details")

    ans = int(input("Enter your choice:"))

    if ans == 1:

        flag = 0

        for k in books:
            print(k)
            flag = 1

        if flag == 0:
            print("Not found")

    elif ans == 2:

        flag = 0

        print("Enter A: if you want to display details of a specific customer")
        print("Enter B: if you want to display details of all customers")

        a = input("Enter your choice:")

        if a == 'A':

            name = input("Enter customer name:")

            for k in customers:
                if k[1] == name:
                    print(k)
                    flag = 1

            if flag == 0:
                print("Not found")

        elif a == 'B':

            for k in customers:
                print(k)
                flag = 1

            if flag == 0:
                print("Not found")

        else:
            print("Invalid choice")

    elif ans == 3:

        flag = 0
        Total = 0

        print("Enter A: if you want to display sales details of a specific book")
        print("Enter B: if you want to display all sales details")
        print("Enter C: if you want to display sales details on a specific date")

        a = input("Enter your choice:")

        if a == 'A':

            ID = input("Enter book ID:")

            for k in sales_details:
                if k[0] == ID:
                    print(k)
                    Total += float(k[5])
                    flag = 1

            print("Total amount=", Total)

            if flag == 0:
                print("Not found")

        elif a == 'B':

            for k in sales_details:
                print(k)
                Total += float(k[5])
                flag = 1

            print("Total amount=", Total)

            if flag == 0:
                print("Not found")

        elif a == 'C':

            date = input("Enter date:")

            for k in sales_details:
                if k[3] == date:
                    print(k)
                    Total += float(k[5])
                    flag = 1

            print("Total amount=", Total)

            if flag == 0:
                print("Not found")

        else:
            print("Invalid choice!")

    else:
        print("Invalid choice")
