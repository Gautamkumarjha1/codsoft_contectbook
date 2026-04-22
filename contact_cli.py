# file: contact_cli.py

from contact_backend import *

def show_contacts(contacts):
    if not contacts:
        print("No contacts found.")
        return
    for i, c in enumerate(contacts):
        print(f"{i}. {c['name']} | {c['phone']} | {c['email']} | {c['address']}")

def main():
    while True:
        print("\n=== CONTACT BOOK CLI ===")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            name = input("Name: ")
            phone = input("Phone: ")
            email = input("Email: ")
            address = input("Address: ")
            add_contact(name, phone, email, address)

        elif choice == "2":
            show_contacts(get_contacts())

        elif choice == "3":
            keyword = input("Enter name/phone: ")
            show_contacts(search_contact(keyword))

        elif choice == "4":
            show_contacts(get_contacts())
            idx = int(input("Enter index to update: "))
            name = input("New Name: ")
            phone = input("New Phone: ")
            email = input("New Email: ")
            address = input("New Address: ")
            update_contact(idx, name, phone, email, address)

        elif choice == "5":
            show_contacts(get_contacts())
            idx = int(input("Enter index to delete: "))
            delete_contact(idx)

        elif choice == "6":
            break

        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
