contacts = {
    "A": {"Kim": "0123", "Porche": "45366"},
    "B": {"Kinn": "9876", "Duanwu": "47282"},
    "C": {"Daisy": "45637", "Niao": "09123"}
}

def display_contacts():
    print("\nContacts:")
    for group, people in contacts.items():
        print(f"\n Group {group}:")
        for name, number in people.items():
            print(f"   {name}: {number}")
    print()

def add_new_contact():
    group = input("Enter group: ")
    name = input("Enter contact name: ")
    number = input("Enter contact number: ")
    contacts.setdefault(group, {})[name] = number
    print(f"{name} added to Group {group}.")

def remove_contact():
    group = input("Enter group: ")
    name = input("Enter name to delete: ")
    if group in contacts and name in contacts[group]:
        del contacts[group][name]
        print(f"{name} deleted from Group {group}.")
    else:
        print("Contact not found.")

def update_contact():
    group = input("Enter group: ")
    name = input("Enter name to update: ")
    if group in contacts and name in contacts[group]:
        number = input("Enter new number: ")
        contacts[group][name] = number
        print(f"{name}'s number updated.")
    else:
        print("Contact not found.")

def menu():
    while True:
        print("\nMenu:")
        print("1. Display Contacts")
        print("2. Add new Contact")
        print("3. Delete Contact")
        print("4. Update Contact")
        print("5. Exit")

        choice = input("Choose an option: ")
        if choice == "1":
           display_contacts()
        elif choice == "2":
            add_new_contact()
        elif choice == "3":
            remove_contact()
        elif choice == "4":
            update_contact()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

menu()