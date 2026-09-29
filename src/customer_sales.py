def customer(customers):

    while True:

        Sno = int(input("Enter serial number:"))
        name = input("Enter customer name:")
        phone = input("Enter phone number:")
        email = input("Enter email:")

        customers.append([Sno, name, phone, email])

        ans = input('Do you want to add more customer details?(y/n):')

        if ans == 'n':
            break


def sales(sales_details):

    while True:

        ID = input("Enter Book ID:")
        name = input("Enter book name:")
        no = int(input("Enter invoice number:"))
        Date = input("Enter date:")
        cu = input("Enter customer name:")
        Amt = input("Enter amount:")

        sales_details.append([ID, name, no, Date, cu, Amt])

        ans = input('Do you want to add more sales details?(y/n):')

        if ans == 'n':
            break
