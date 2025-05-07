import pickle #saving and loading

# Load the contact book from a file
def load_contacts():
    try:
        with open("contacts.pkl", "rb") as file:
            return pickle.load(file)
    except FileNotFoundError:
        return {}

# Save the contact book to a file
def save_contacts(contacts):
    with open("contacts.pkl", "wb") as file:
        pickle.dump(contacts, file)

# Main contact book program
def main():
    contact_book = load_contacts()  # Dictionary to store contacts

    while True:
        print("\n--- Contact Book Menu ---")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Save Contacts")
        print("4. Exit")

        choice = input("Choose an option (1-4): ")

        if choice == "1":
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            contact_book[name] = phone
            print("Contact added.")

        elif choice == "2":
            if contact_book:
                print("\n--- Contacts ---")
                for name, phone in contact_book.items():
                    print(f"{name}: {phone}")
            else:
                print("No contacts yet.")

        elif choice == "3":
            save_contacts(contact_book)
            print("Contacts saved to file.")

        elif choice == "4":
            save_contacts(contact_book)
            print("Contacts saved. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")

if __name__ == "__main__":
    main()
