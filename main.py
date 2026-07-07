from tkinter import *
from tkinter import messagebox

books = []

def add_book():
    book = book_entry.get()

    if book == "":
        messagebox.showwarning("Warning", "Enter Book Name")
        return

    books.append({"name": book, "status": "Available"})
    update_list()
    book_entry.delete(0, END)

def search_book():
    book = book_entry.get().lower()

    for item in books:
        if item["name"].lower() == book:
            messagebox.showinfo(
                "Book Found",
                f'Book: {item["name"]}\nStatus: {item["status"]}'
            )
            return

    messagebox.showerror("Error", "Book Not Found")

def issue_book():
    selected = listbox.curselection()

    if not selected:
        messagebox.showwarning("Warning", "Select a Book")
        return

    index = selected[0]
    books[index]["status"] = "Issued"
    update_list()

def return_book():
    selected = listbox.curselection()

    if not selected:
        messagebox.showwarning("Warning", "Select a Book")
        return

    index = selected[0]
    books[index]["status"] = "Available"
    update_list()

def delete_book():
    selected = listbox.curselection()

    if not selected:
        messagebox.showwarning("Warning", "Select a Book")
        return

    index = selected[0]
    books.pop(index)
    update_list()

def update_list():
    listbox.delete(0, END)

    for book in books:
        listbox.insert(
            END,
            f"{book['name']} - {book['status']}"
        )

root = Tk()
root.title("Library Management System")
root.geometry("600x500")

title = Label(
    root,
    text="Library Management System",
    font=("Arial", 18, "bold")
)
title.pack(pady=10)

book_entry = Entry(root, width=40)
book_entry.pack(pady=10)

Button(root, text="Add Book", width=15,
       command=add_book).pack(pady=5)

Button(root, text="Search Book", width=15,
       command=search_book).pack(pady=5)

Button(root, text="Issue Book", width=15,
       command=issue_book).pack(pady=5)

Button(root, text="Return Book", width=15,
       command=return_book).pack(pady=5)

Button(root, text="Delete Book", width=15,
       command=delete_book).pack(pady=5)

listbox = Listbox(root, width=60, height=12)
listbox.pack(pady=20)

root.mainloop()