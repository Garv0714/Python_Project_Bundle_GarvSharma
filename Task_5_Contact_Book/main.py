#password is "codsoft@123"
import json
import os
import csv
from datetime import datetime
from getpass import getpass

FILE_NAME = 'contacts.json'

def load_contacts():
    if not os.path.exists(FILE_NAME):
        return []
    with open(FILE_NAME, 'r') as file:
        return json.load(file)

def save_contacts(contacts):
    with open(FILE_NAME, 'w') as file:
        json.dump(contacts, file, indent=4)

def add_contact():
    contact = {
        'name': input("Name: ").strip(),
        'phone': input("Phone: ").strip(),
        'email': input("Email: ").strip(),
        'category': input("Category (Family/Friends/Work/Other): ").strip(),
        'added_on': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    contacts = load_contacts()
    contacts.append(contact)
    save_contacts(contacts)
    print("✅ Contact added successfully!\n")

def view_contacts():
    contacts = load_contacts()
    if not contacts:
        print("❌ No contacts found.\n")
        return
    for idx, c in enumerate(contacts, 1):
        print(f"{idx}. {c['name']} | {c['phone']} | {c['email']} | {c['category']} | Added: {c['added_on']}")
    print()

def search_contact():
    query = input("Search by name, phone or email: ").strip().lower()
    contacts = load_contacts()
    results = [c for c in contacts if query in c['name'].lower() or query in c['phone'] or query in c['email'].lower()]
    if results:
        for c in results:
            print(f"{c['name']} | {c['phone']} | {c['email']} | {c['category']}")
    else:
        print("❌ No matching contact found.")
    print()

def delete_contact():
    name = input("Enter name to delete: ").strip().lower()
    contacts = load_contacts()
    updated = [c for c in contacts if c['name'].lower() != name]
    if len(updated) == len(contacts):
        print("❌ No contact found with that name.")
    else:
        save_contacts(updated)
        print("🗑️ Contact deleted successfully.")
    print()

def update_contact():
    name = input("Enter name to update: ").strip().lower()
    contacts = load_contacts()
    for contact in contacts:
        if contact['name'].lower() == name:
            print("Leave blank to skip updating a field.")
            contact['phone'] = input(f"New phone ({contact['phone']}): ").strip() or contact['phone']
            contact['email'] = input(f"New email ({contact['email']}): ").strip() or contact['email']
            contact['category'] = input(f"New category ({contact['category']}): ").strip() or contact['category']
            save_contacts(contacts)
            print("✅ Contact updated!\n")
            return
    print("❌ Contact not found.\n")

def export_to_csv():
    contacts = load_contacts()
    with open('contacts_export.csv', 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['name', 'phone', 'email', 'category', 'added_on'])
        writer.writeheader()
        writer.writerows(contacts)
    print("📤 Exported to contacts_export.csv\n")

def import_from_csv():
    try:
        with open('contacts_import.csv', 'r') as file:
            reader = csv.DictReader(file)
            new_contacts = list(reader)
        contacts = load_contacts()
        contacts.extend(new_contacts)
        save_contacts(contacts)
        print("📥 Imported contacts from contacts_import.csv\n")
    except FileNotFoundError:
        print("❌ contacts_import.csv not found.\n")

def sort_contacts():
    contacts = load_contacts()
    if not contacts:
        print("❌ No contacts to sort.\n")
        return
    contacts.sort(key=lambda x: x['name'].lower())
    for c in contacts:
        print(f"{c['name']} | {c['phone']} | {c['email']} | {c['category']}")
    print()

def secure_mode():
    password = input("Enter access password: ")
    if password != "codsoft@123":
        print("🚫 Incorrect password.")
        exit()
    print("✅ Access granted!\n")

def main():
    secure_mode()

    while True:
        print("""
📒 Contact Book Manager - Menu
1. Add Contact
2. View Contacts
3. Search Contact
4. Update Contact
5. Delete Contact
6. Export to CSV
7. Import from CSV
8. Sort Contacts by Name
9. Exit
""")
        choice = input("Enter choice (1-9): ").strip()
        match choice:
            case '1': add_contact()
            case '2': view_contacts()
            case '3': search_contact()
            case '4': update_contact()
            case '5': delete_contact()
            case '6': export_to_csv()
            case '7': import_from_csv()
            case '8': sort_contacts()
            case '9': print("👋 Bye!"); break
            case _: print("❌ Invalid option.\n")

if __name__ == "__main__":
    main()
