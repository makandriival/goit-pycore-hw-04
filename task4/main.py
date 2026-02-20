from pathlib import Path

from helpers import (
    parse_input,
    add_contact,
    change_contact,
    show_phone,
    show_all,
    load_contacts,
    save_contacts,
)

def main():
    contacts_file = Path(__file__).with_name("contacts.txt")
    contacts = load_contacts(contacts_file)
    print("Welcome to the assistant bot!")

    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

        if not command:
            print("Invalid command.")
            continue

        if command in ["close", "exit"]:
            print("Good bye!")
            break

        if command == "hello":
            print("How can I help you?")
        elif command == "add":
            result = add_contact(args, contacts)
            if result == "Contact added.":
                save_contacts(contacts_file, contacts)
            print(result)
        elif command == "change":
            result = change_contact(args, contacts)
            if result == "Contact updated.":
                save_contacts(contacts_file, contacts)
            print(result)
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()