from pathlib import Path


def parse_input(user_input):
    parts = user_input.strip().split()
    if not parts:
        return "", []

    command, *args = parts
    return command.lower(), args


def add_contact(args, contacts):
    if len(args) != 2:
        return "Give me name and phone please."

    name, phone = args
    contacts[name] = phone
    return "Contact added."


def change_contact(args, contacts):
    if len(args) != 2:
        return "Give me name and phone please."

    name, phone = args
    if name not in contacts:
        return "Contact not found."

    contacts[name] = phone
    return "Contact updated."


def show_phone(args, contacts):
    if len(args) != 1:
        return "Give me name please."

    name = args[0]
    return contacts.get(name, "Contact not found.")


def show_all(contacts):
    if not contacts:
        return "No contacts saved."

    return "\n".join(f"{name}: {phone}" for name, phone in contacts.items())


def load_contacts(file_path):
    path = Path(file_path)
    if not path.exists():
        return {}

    contacts = {}
    with path.open("r", encoding="utf-8") as file:
        for line in file:
            record = line.strip()
            if not record:
                continue

            name, phone = record.split("\t", 1)
            contacts[name] = phone

    return contacts


def save_contacts(file_path, contacts):
    path = Path(file_path)
    with path.open("w", encoding="utf-8") as file:
        for name, phone in contacts.items():
            file.write(f"{name}\t{phone}\n")
