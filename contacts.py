import json
import os

FILE_NAME = "contacts.json"

# ---------------- FILE HANDLING ----------------
def load_contacts():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as f:
            return json.load(f)
    return []

def save_contacts():
    with open(FILE_NAME, "w") as f:
        json.dump(contacts, f, indent=4)

# ---------------- VALIDATION ----------------
def valid_phone():
    while True:
        phone = input("Enter phone (10 digits) or 'q' to cancel: ")

        if phone.lower() == 'q':
            return None

        if not (phone.isdigit() and len(phone) == 10):
            print("❌ Must be exactly 10 digits.")
            continue

        if len(set(phone)) == 1:
            print("❌ Invalid (same digits not allowed).")
            continue

        return phone


def valid_email():
    while True:
        email = input("Enter email (or 'q' to cancel): ")

        if email.lower() == 'q':
            return None

        if "@" in email and "." in email:
            return email
        else:
            print("❌ Invalid email format.")

# ---------------- FEATURES ----------------
def add_contact():
    name = input("Enter name (or 'q' to cancel): ")
    if name.lower() == 'q':
        print("❌ Cancelled.")
        return

    phone = valid_phone()
    if phone is None:
        print("❌ Cancelled.")
        return

    email = valid_email()
    if email is None:
        print("❌ Cancelled.")
        return

    address = input("Enter address (or 'q' to cancel): ")
    if address.lower() == 'q':
        print("❌ Cancelled.")
        return

    contacts.append({
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    })

    save_contacts()
    print("✅ Contact added & saved!")

def view_contacts():
    if not contacts:
        print("📭 No contacts found.")
    else:
        print("\n📒 Contact List:")
        for i, c in enumerate(contacts):
            print(f"{i+1}. {c['name']} - {c['phone']}")

def search_contact():
    search = input("Search name or phone: ").lower()
    found = False

    for c in contacts:
        if search in c["name"].lower() or search in c["phone"]:
            print("\n🔍 Found:")
            print("Name   :", c["name"])
            print("Phone  :", c["phone"])
            print("Email  :", c["email"])
            print("Address:", c["address"])
            found = True

    if not found:
        print("❌ Not found.")

def update_contact():
    view_contacts()
    try:
        i = int(input("Enter contact number: ")) - 1

        if 0 <= i < len(contacts):
            contacts[i]["name"] = input("New name: ")
            phone = valid_phone()
            if phone is None:
                print("❌ Cancelled.")
                return
            contacts[i]["phone"] = phone

            email = valid_email()
            if email is None:
                print("❌ Cancelled.")
                return
            contacts[i]["email"] = email

            contacts[i]["address"] = input("New address: ")

            save_contacts()
            print("✅ Updated & saved!")
        else:
            print("❌ Invalid choice.")
    except ValueError:
        print("❌ Enter valid number.")

def delete_contact():
    view_contacts()
    try:
        i = int(input("Enter contact number: ")) - 1

        if 0 <= i < len(contacts):
            removed = contacts.pop(i)
            save_contacts()
            print(f"🗑️ Deleted: {removed['name']}")
        else:
            print("❌ Invalid choice.")
    except ValueError:
        print("❌ Enter valid number.")

# ---------------- MAIN PROGRAM ----------------
contacts = load_contacts()

try:
    while True:
        print("\n=== 📱 Contact Book ===")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            update_contact()
        elif choice == "5":
            delete_contact()
        elif choice == "6":
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid choice.")

except KeyboardInterrupt:
    print("\n👋 Program stopped safely!")