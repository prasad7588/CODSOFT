contacts = []

def add_contact():
    name = input("Enter contact's name: ")
    phone = input("Enter contact's phone number: ")
    email = input("Enter contact's email: ")
    address = input("Enter contact's address: ")

    contact = {
        'Name': name,
        'Phone': phone,
        'Email': email,
        'Address': address
    }

    contacts.append(contact)
    print("Contact added successfully!")

def view_contacts():
    if not contacts:
        print("No contacts found.")
        return

    print("\nContact List:")
    for index, contact in enumerate(contacts, start=1):
        print(f"{index}. Name: {contact['Name']} - Phone: {contact['Phone']}")

def search_contact():
    keyword = input("Enter name or phone number to search: ")
    found = False

    for contact in contacts:
        if keyword.lower() in contact['Name'].lower() or keyword in contact['Phone']:
            print(f"Name: {contact['Name']}")
            print(f"Phone: {contact['Phone']}")
            print(f"Email: {contact['Email']}")
            print(f"Address: {contact['Address']}")
            found = True

    if not found:
        print("Contact not found.")

def update_contact():
    keyword = input("Enter the name or phone number of the contact to update: ")
    found = False

    for contact in contacts:
        if keyword.lower() in contact['Name'].lower() or keyword in contact['Phone']:
            contact['Name'] = input("Enter updated name: ")
            contact['Phone'] = input("Enter updated phone number: ")
            contact['Email'] = input("Enter updated email: ")
            contact['Address'] = input("Enter updated address: ")
            print("Contact updated successfully!")
            found = True

    if not found:
        print("Contact not found.")

def delete_contact():
    keyword = input("Enter the name or phone number of the contact to delete: ")
    found = False

    for contact in contacts[:]:
        if keyword.lower() in contact['Name'].lower() or keyword in contact['Phone']:
            contacts.remove(contact)
            print("Contact deleted successfully!")
            found = True

    if not found:
        print("Contact not found.")

def display_menu():
    print("\nContact Management System")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

while True:
    display_menu()
    choice = input("Enter your choice: ")

    if choice == '1':
        add_contact()
    elif choice == '2':
        view_contacts()
    elif choice == '3':
        search_contact()
    elif choice == '4':
        update_contact()
    elif choice == '5':
        delete_contact()
    elif choice == '6':
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a valid option.")
