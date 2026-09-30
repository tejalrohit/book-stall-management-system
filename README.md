# Book Management System

## 1. Project Overview

The **Book Management System** is a Python-based application designed to manage books, customers, and sales details in a simple and organized way.

The project allows users to add and manage book information such as book ID, title, author, price, quantity, and shelf number. It provides a basic system for maintaining book records and can be extended with additional library or bookstore management features.

## 2. Features

- Add new books to the system
- Store book ID, title, author, price, quantity, and shelf number
- Manage book records using Python lists
- Manage customer details
- Store sales details
- Display and manage stored information
- Simple menu-driven interaction
- Easy to understand and use
- Suitable for basic bookstore/library management

## 3. Technologies and Tools Used

### Programming Language
- **Python**

### Development Tools
- **Visual Studio Code**
- **Git**
- **GitHub**

### Concepts Used
- Python functions
- Lists
- Loops
- Conditional statements
- User input
- File handling/modules (if implemented)
- Basic data management

## 4. Project Structure

```text
Book-Management-System/
│
├── README.md
├── statement.md
├── main.py
├── books.py
├── customers.py
├── sales.py
└── ...
```

*The exact file names may vary depending on the modules used in the project.*

## 5. Installation and Running

### Step 1: Install Python

Download and install Python from the official Python website.

Make sure Python is added to the system PATH during installation.

### Step 2: Clone the Repository

Open Command Prompt or Terminal and run:

```bash
git clone <your-github-repository-url>
```

### Step 3: Open the Project

Move into the project folder:

```bash
cd Book-Management-System
```

Open the folder in Visual Studio Code.

### Step 4: Run the Program

Run the main Python file:

```bash
python main.py
```

If your system uses `python3`, use:

```bash
python3 main.py
```

## 6. How to Use

1. Start the program.
2. Select the required option from the menu.
3. Enter the requested information.
4. For adding a book, enter:
   - Book ID
   - Book title
   - Author name
   - Price
   - Quantity
   - Shelf number
5. The information will be stored in the appropriate list.
6. Continue using the menu to perform other available operations.
7. Exit the program when finished.

## 7. Testing Instructions

The project can be tested by running the program and checking each available feature.

### Test Case 1: Add a Book

Enter valid book details:

```text
Book ID: B101
Title: Python Basics
Author: John Smith
Price: 450
Quantity: 10
Shelf Number: 5
```

Check whether the book is successfully added.

### Test Case 2: Multiple Books

Add more than one book and verify that all records are stored correctly.

### Test Case 3: Quantity

Enter different quantities and verify that the program stores the correct quantity.

### Test Case 4: Invalid Input

Try entering an invalid value where a number is required and check how the program handles the input.

### Test Case 5: Menu Operations

Test each option provided by the main menu and verify that the expected output is displayed.

## 8. Screenshots

Screenshots of the following can be added here:

- Main menu
- Adding a new book
- Displaying book records
- Customer management
- Sales details
- Program output

Example:

```text
![Main Menu](screenshots/main-menu.png)
![Book Entry](screenshots/add-book.png)
![Output](screenshots/output.png)
```

## 9. Future Enhancements

The project can be improved by adding:

- Search books by ID or title
- Update book information
- Delete book records
- Customer management
- Sales and billing system
- File/database storage
- Login and authentication
- Graphical user interface
- MySQL database integration

## 10. Conclusion

The Book Management System provides a simple way to manage book-related information using Python. The project demonstrates fundamental programming concepts such as functions, lists, loops, conditional statements, and user input.

It can serve as a foundation for developing a more advanced bookstore or library management application.
