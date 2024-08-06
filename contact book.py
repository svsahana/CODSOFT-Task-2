import json

# Define the filename for storing contacts
CONTACTS_FILE = 'contacts.json'


def load_contacts():
    try:
        with open(CONTACTS_FILE, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}


def save_contacts(contacts):
    with open(CONTACTS_FILE, 'w') as file:
        json.dump(contacts, file, indent=4)


def add_contact(contacts):
    name = input("Enter contact name: ")
    phone = input("Enter contact phone: ")
    email = input("Enter contact email: ")
    street = input("Enter contact street address: ")
    city = input("Enter contact city: ")
    state = input("Enter contact state: ")
    zip_code = input("Enter contact ZIP code: ")

    contact_id = str(len(contacts) + 1)
    contacts[contact_id] = {
        'name': name,
        'phone': phone,
        'email': email,
        'address': {
            'street': street,
            'city': city,
            'state': state,
            'zip_code': zip_code
        }
    }
    save_contacts(contacts)
    print("Contact added successfully!")


def view_contacts(contacts):
    if not contacts:
        print("No contacts found.")
        return

    for contact_id, contact_info in contacts.items():
        print(f"ID: {contact_id}")
        print(f"Name: {contact_info['name']}")
        print(f"Phone: {contact_info['phone']}")
        print(f"Email: {contact_info['email']}")
        print(
            f"Address: {contact_info['address']['street']}, {contact_info['address']['city']}, {contact_info['address']['state']} {contact_info['address']['zip_code']}")
        print()


def search_contact(contacts):
    search_name = input("Enter the name of the contact to search: ").lower()
    found = False
    for contact_id, contact_info in contacts.items():
        if search_name in contact_info['name'].lower():
            print(f"ID: {contact_id}")
            print(f"Name: {contact_info['name']}")
            print(f"Phone: {contact_info['phone']}")
            print(f"Email: {contact_info['email']}")
            print(
                f"Address: {contact_info['address']['street']}, {contact_info['address']['city']}, {contact_info['address']['state']} {contact_info['address']['zip_code']}")
            print()
            found = True
    if not found:
        print("Contact not found.")


def update_contact(contacts):
    contact_id = input("Enter the ID of the contact to update: ")
    if contact_id not in contacts:
        print("Contact not found.")
        return

    name = input("Enter new contact name: ")
    phone = input("Enter new contact phone: ")
    email = input("Enter new contact email: ")
    street = input("Enter new contact street address: ")
    city = input("Enter new contact city: ")
    state = input("Enter new contact state: ")
    zip_code = input("Enter new contact ZIP code: ")

    contacts[contact_id] = {
        'name': name,
        'phone': phone,
        'email': email,
        'address': {
            'street': street,
            'city': city,
            'state': state,
            'zip_code': zip_code
        }
    }
    save_contacts(contacts)
    print("Contact updated successfully!")


def delete_contact(contacts):
    contact_id = input("Enter the ID of the contact to delete: ")
    if contact_id in contacts:
        del contacts[contact_id]
        save_contacts(contacts)
        print("Contact deleted successfully!")
    else:
        print("Contact not found.")


def main():
    contacts = load_contacts()

    while True:
        print("\nContact Book Menu:")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            view_contacts(contacts)
        elif choice == '3':
            search_contact(contacts)
        elif choice == '4':
            update_contact(contacts)
        elif choice == '5':
            delete_contact(contacts)
        elif choice == '6':
            print("Exiting the Contact Book. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
