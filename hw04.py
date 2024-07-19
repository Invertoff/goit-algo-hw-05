def input_error(func):
    """
    Decorator for handling input errors.
    """
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Error: Contact not found."
        except ValueError as ve:
            return str(ve)
        except IndexError:
            return "Error: Missing arguments."
    return inner


def parse_input(user_input):
    """
    Separates string input from user into command and args.

    Args: 
        user_input (str): Input from user.

    Returns:
        tuple: Command and list of args. 
    """
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, args


@input_error
def add_contact(args, contacts):
    """
    Adds new contact to contact dict.

    Args:
        args (list): List containing name and phone.
        contacts (dict): Dictionary to store contacts.

    Returns:
        str: Message regarding program completion.
    """
    if len(args) != 2:
        raise ValueError("Error: Command format is 'add [name] [phone]'")
    name, phone = args
    contacts[name] = phone
    return "Contact added."


@input_error
def change_contact(args, contacts):
    """
    Changes a telephone number for existing contact.

    Args:
        args (list): List containing name and new phone.
        contacts (dict): Dictionary to store contacts.

    Returns:
        str: Message regarding program completion.
    """
    if len(args) != 2:
        raise ValueError("Error: Command format is 'change [name] [new phone]'")
    name, new_phone = args
    if name in contacts:
        contacts[name] = new_phone
        return "Contact updated."
    else:
        raise KeyError


@input_error
def show_phone(args, contacts):
    """
    Shows telephone number for selected contact.

    Args:
        args (list): List containing name.
        contacts (dict): Dictionary to store contacts.

    Returns: 
        str: Telephone number or error message.
    """
    if len(args) != 1:
        raise ValueError("Error: Command format is 'phone [name]'")
    name = args[0]
    if name in contacts:
        return contacts[name]
    else:
        raise KeyError


@input_error
def show_all(args, contacts):
    """
    Shows all saved telephone numbers.

    Args:
        args (list): Empty list, not used.
        contacts (dict): Dictionary to store contacts.

    Returns: 
        str: All contacts list or error message if no contacts found.
    """
    if not contacts:
        return "No contacts found."
    result = [f"{name}: {phone}" for name, phone in contacts.items()]
    return "\n".join(result)


def main():
    """
    Main cycle of the program, processing user inputs and calling specified functions.
    """
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        try:
            user_input = input("Enter a command: ")
            command, args = parse_input(user_input)
            if command in ["close", "exit"]:
                print("Good bye!")
                break
            elif command == "hello":
                print("How can I help you?")
            elif command == "add":
                print(add_contact(args, contacts))
            elif command == "change":
                print(change_contact(args, contacts))
            elif command == "phone":
                print(show_phone(args, contacts))
            elif command == "all":
                print(show_all(args, contacts))
            else:
                print("Invalid command.")
        except Exception:
            print("Your input was empty or invalid, please try again.")


if __name__ == "__main__":
    main()
