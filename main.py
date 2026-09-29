from books import AddBooks, RemoveBooks
from edit import EditBooks
from search import SearchBook
from view import View
from customer_sales import customer, sales


books = []
customers = []
sales_details = []


print("Enter 1 to insert new book")
print("Enter 2 to remove or delete books")
print("Enter 3 to edit/update a specific book details")
print("Enter 4 to search for the details of a specific book")
print("Enter 5 to display customer/sales/all book details")
print("Enter 6 to input customer details")
print("Enter 7 to input sales details")
print("Enter 8 to quit")

ch = int(input("Enter your choice:"))

while True:

    if ch == 1:
        AddBooks(books)

    elif ch == 2:
        RemoveBooks(books)

    elif ch == 3:
        EditBooks(books)

    elif ch == 4:
        SearchBook(books)

    elif ch == 5:
        View(books, customers, sales_details)

    elif ch == 6:
        customer(customers)

    elif ch == 7:
        sales(sales_details)

    elif ch == 8:
        break

    else:
        print("Invalid choice!!!")

    ch = int(input("Enter new choice:"))
