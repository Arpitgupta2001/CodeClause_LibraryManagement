# CodeClause_LibraryManagement
In this code, a GUI window is created using Tkinter to build a simple library management system. It consists of an entry field to input the book title and author, an "Add Book" button to add the book to the library, a listbox to display the list of books, and a "Remove Book" button to remove a selected book from the list.

The add_book method is called when the "Add Book" button is clicked. It retrieves the title and author from the entry fields, checks if both fields are filled, creates a book entry in the format "Title: {title} | Author: {author}", inserts it into the listbox, and clears the entry fields. If either the title or author field is empty, it displays a warning message using the messagebox module.

The remove_book method is called when the "Remove Book" button is clicked. It retrieves the index of the selected book in the listbox, deletes the selected book entry from the listbox, and if no book is selected, it displays a warning message.

Note that this is a basic example and doesn't include advanced features like database integration, book details editing, or searching capabilities. Those features can be added based on specific requirements and complexity.
