import tkinter as tk
from tkinter import messagebox

class LibraryManagementSystem:
    def __init__(self, window):
        self.window = window
        self.window.title("Library Management System")

        # Create and pack the book title label and entry
        self.title_label = tk.Label(window, text="Book Title:")
        self.title_label.pack()
        self.title_entry = tk.Entry(window)
        self.title_entry.pack()

        # Create and pack the book author label and entry
        self.author_label = tk.Label(window, text="Author:")
        self.author_label.pack()
        self.author_entry = tk.Entry(window)
        self.author_entry.pack()

        # Create and pack the add book button
        self.add_book_button = tk.Button(window, text="Add Book", command=self.add_book)
        self.add_book_button.pack()

        # Create and pack the book listbox
        self.book_listbox = tk.Listbox(window, width=50)
        self.book_listbox.pack()

        # Create and pack the remove book button
        self.remove_book_button = tk.Button(window, text="Remove Book", command=self.remove_book)
        self.remove_book_button.pack()

    def add_book(self):
        title = self.title_entry.get()
        author = self.author_entry.get()
        if title and author:
            book = f"Title: {title} | Author: {author}"
            self.book_listbox.insert(tk.END, book)
            self.title_entry.delete(0, tk.END)
            self.author_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Invalid Input", "Please enter book title and author.")

    def remove_book(self):
        selected_index = self.book_listbox.curselection()
        if selected_index:
            self.book_listbox.delete(selected_index)
        else:
            messagebox.showwarning("No Book Selected", "Please select a book to remove.")

# Create the main window
window = tk.Tk()

# Create the library management system
lms = LibraryManagementSystem(window)

# Start the main loop
window.mainloop()
