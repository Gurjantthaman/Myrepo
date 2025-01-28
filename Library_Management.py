import tkinter as tk
from tkinter import messagebox

class Library:
    def __init__(self, listOfBooks):
        self.books = listOfBooks
        self.issuedBooks = []  # Keep track of issued books

    def displayAvailableBooks(self):
        return self.books

    def borrowBook(self, bookName):
        if bookName in self.books:
            self.books.remove(bookName)
            self.issuedBooks.append(bookName)
            return True
        else:
            return False



-
    def returnBook(self, bookName):
        if bookName in self.issuedBooks:
            self.issuedBooks.remove(bookName)
            self.books.append(bookName)
            return True
        else:
            return False

class Student:
    def __init__(self, name):
        self.name = name

    def requestBook(self, bookName):
        return bookName

    def returnBook(self, bookName):
        return bookName

class LibraryApp:
    def __init__(self, root, library):
        self.root = root
        self.library = library
        self.student = Student(name="Student")

        self.root.title("Library System")
        self.root.geometry("500x400")

        self.label = tk.Label(self.root, text="Welcome to Central Library", font=("Arial", 16))
        self.label.pack(pady=20)

        self.list_books_button = tk.Button(self.root, text="List All Books", command=self.display_books)
        self.list_books_button.pack(pady=10)

        self.borrow_button = tk.Button(self.root, text="Borrow a Book", command=self.borrow_book)
        self.borrow_button.pack(pady=10)

        self.return_button = tk.Button(self.root, text="Return a Book", command=self.return_book)
        self.return_button.pack(pady=10)

        self.exit_button = tk.Button(self.root, text="Exit", command=self.exit_program)
        self.exit_button.pack(pady=20)

        self.book_name_entry = tk.Entry(self.root)
        self.book_name_entry.pack(pady=10)

    def display_books(self):
        books = self.library.displayAvailableBooks()
        book_list = "\n".join(books)
        messagebox.showinfo("Available Books", f"Books available in the library:\n{book_list}")

    def borrow_book(self):
        book_name = self.book_name_entry.get()
        if not book_name:
            messagebox.showerror("Error", "Please enter the book name.")
            return
        if self.library.borrowBook(book_name):
            messagebox.showinfo("Success", f"You have borrowed {book_name}. Please return it in 30 days.")
        else:
            messagebox.showerror("Error", "Sorry, the book is not available.")

    def return_book(self):
        book_name = self.book_name_entry.get()
        if not book_name:
            messagebox.showerror("Error", "Please enter the book name.")
            return
        if self.library.returnBook(book_name):
            messagebox.showinfo("Success", f"Thank you for returning {book_name}.")
        else:
            messagebox.showerror("Error", "You have not borrowed this book or the book does not exist.")

    def exit_program(self):
        messagebox.showinfo("Goodbye", "Thanks for visiting the library. Have a great day!")
        self.root.quit()

if __name__ == "__main__":
    centralLibrary = Library(["DSA", "Python", "Django", "Java", "C++"])

    root = tk.Tk()
    app = LibraryApp(root, centralLibrary)
    root.mainloop()
