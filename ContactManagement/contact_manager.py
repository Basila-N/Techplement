
import os

# File to store contacts
CONTACT_FILE = "contacts.txt"


#  Function to load contacts from file
def load_contacts():
    contacts = {}
    if os.path.exists(CONTACT_FILE):
        with open(CONTACT_FILE, "r") as file:
            for line in file:
                name, phone, email = line.strip().split(",")
                contacts[name] = {"phone": phone, "email": email}
    return contacts


#  Function to save contacts to file
def save_contacts(contacts):
    with open(CONTACT_FILE, "w") as file:
        for name, info in contacts.items():
            file.write(f"{name},{info['phone']},{info['email']}\n")


#  Function to add a contact
def add_contact(contacts):
    name = input("Enter name: ").strip()
    
    if name in contacts:
        print("Contact already exists!")
        return
    
    phone = input("Enter phone number: ").strip()
    email = input("Enter email address: ").strip()
    
    contacts[name] = {"phone": phone, "email": email}
    print(f"Contact {name} added successfully!")


#  Function to search for a contact
def search_contact(contacts):
    name = input("Enter name to search: ").strip()
    
    if name in contacts:
        print("\n--- Contact Found ---")
        print(f"Name: {name}")
        print(f"Phone: {contacts[name]['phone']}")
        print(f"Email: {contacts[name]['email']}")
    else:
        print("Contact not found.")


#  Function to update a contact
def update_contact(contacts):
    name = input("Enter name to update: ").strip()
    
    if name in contacts:
        print("\n--- Update Contact ---")
        phone = input("Enter new phone number: ").strip()
        email = input("Enter new email address: ").strip()
        
        contacts[name] = {"phone": phone, "email": email}
        print(f"Contact {name} updated successfully!")
    else:
        print("Contact not found.")


#  Function to delete a contact
def delete_contact(contacts):
    name = input("Enter name to delete: ").strip()
    
    if name in contacts:
        del contacts[name]
        print(f"Contact {name} deleted successfully!")
    else:
        print("Contact not found.")


#  Function to display all contacts
def display_contacts(contacts):
    if contacts:
        print("\n--- All Contacts ---")
        for name, info in contacts.items():
            print(f"Name: {name}")
            print(f"Phone: {info['phone']}")
            print(f"Email: {info['email']}")
            print("--------------------")
    else:
        print("No contacts available.")


#  Main Program Loop
def main():
    contacts = load_contacts()
    
    while True:
        print("\nContact Management System")
        print("1. Add Contact")
        print("2. Search Contact")
        print("3. Update Contact")
        print("4. Delete Contact")
        print("5. Display All Contacts")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            search_contact(contacts)
        elif choice == "3":
            update_contact(contacts)
        elif choice == "4":
            delete_contact(contacts)
        elif choice == "5":
            display_contacts(contacts)
        elif choice == "6":
            save_contacts(contacts)
            print("Contacts saved. Exiting...")
            break
        else:
            print("Invalid option. Please try again.")


#  Run the program
if __name__ == "__main__":
    main()
