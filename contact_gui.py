# file: contact_gui.py

import tkinter as tk
from tkinter import messagebox
from contact_backend import *

def refresh():
    listbox.delete(0, tk.END)
    for i, c in enumerate(get_contacts()):
        listbox.insert(tk.END, f"{i}. {c['name']} | {c['phone']}")

def add():
    add_contact(
        name_entry.get(),
        phone_entry.get(),
        email_entry.get(),
        address_entry.get()
    )
    refresh()

def delete():
    try:
        index = listbox.curselection()[0]
        delete_contact(index)
        refresh()
    except:
        messagebox.showerror("Error", "Select a contact")

def update():
    try:
        index = listbox.curselection()[0]
        update_contact(
            index,
            name_entry.get(),
            phone_entry.get(),
            email_entry.get(),
            address_entry.get()
        )
        refresh()
    except:
        messagebox.showerror("Error", "Select a contact")

def search():
    keyword = search_entry.get()
    listbox.delete(0, tk.END)
    for i, c in enumerate(search_contact(keyword)):
        listbox.insert(tk.END, f"{i}. {c['name']} | {c['phone']}")

# GUI setup
root = tk.Tk()
root.title("Contact Book")

tk.Label(root, text="Name").pack()
name_entry = tk.Entry(root)
name_entry.pack()

tk.Label(root, text="Phone").pack()
phone_entry = tk.Entry(root)
phone_entry.pack()

tk.Label(root, text="Email").pack()
email_entry = tk.Entry(root)
email_entry.pack()

tk.Label(root, text="Address").pack()
address_entry = tk.Entry(root)
address_entry.pack()

tk.Button(root, text="Add Contact", command=add).pack(pady=5)

listbox = tk.Listbox(root, width=50)
listbox.pack()

tk.Button(root, text="Delete", command=delete).pack()
tk.Button(root, text="Update", command=update).pack()

tk.Label(root, text="Search").pack()
search_entry = tk.Entry(root)
search_entry.pack()

tk.Button(root, text="Search", command=search).pack()

refresh()
root.mainloop()
