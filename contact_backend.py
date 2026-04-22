# file: contact_backend.py

import json
import os

FILE_NAME = "contacts.json"

def load_contacts():
    if not os.path.exists(FILE_NAME):
        return []
    with open(FILE_NAME, "r") as f:
        return json.load(f)

def save_contacts(contacts):
    with open(FILE_NAME, "w") as f:
        json.dump(contacts, f, indent=4)

def add_contact(name, phone, email, address):
    contacts = load_contacts()
    contacts.append({
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    })
    save_contacts(contacts)

def get_contacts():
    return load_contacts()

def delete_contact(index):
    contacts = load_contacts()
    if 0 <= index < len(contacts):
        contacts.pop(index)
        save_contacts(contacts)

def update_contact(index, name, phone, email, address):
    contacts = load_contacts()
    if 0 <= index < len(contacts):
        contacts[index] = {
            "name": name,
            "phone": phone,
            "email": email,
            "address": address
        }
        save_contacts(contacts)

def search_contact(keyword):
    contacts = load_contacts()
    result = []
    for c in contacts:
        if keyword.lower() in c["name"].lower() or keyword in c["phone"]:
            result.append(c)
    return result
