
import re

contact_fields = []
contact_list = {}


def add_contact():
    global contact_fields
    global contact_list
    print("Add new contact...")

    contact_data = []
    email = ""

    for field in contact_fields:
        if field == "Email":
            while True:
                email = input("Enter email address: ")
                if validate_email(email):
                    break
        else:
            field = input(f"Enter {field}: ")
            if field == "/end":
                while len(contact_data) < len(contact_fields) - 1:
                    contact_data.append("")
                break
            else:
                contact_data.append(field)

    contact_list[email] = contact_data
    print(f"Added contact for {email}: {contact_data}")
    
    update_backup()


def edit_contact():
    global contact_fields
    global contact_list
    pass


def delete_contact():
    global contact_fields
    global contact_list
    pass


def search_contact():
    global contact_fields
    global contact_list
    pass


def dispaly_contacts():
    global contact_fields
    global contact_list
    
    for contact, details in contact_list.items():
        details_string = ""
        field_num = 1
        for field_detail in details:
            details_string += contact_fields[field_num] + " - " + field_detail + " | "
            field_num += 1

        print(f"{contact}: {details_string}")


def export_contacts():
    global contact_fields
    global contact_list
    pass


def import_contacts():
    global contact_fields
    global contact_list
    pass


def quit_app():
    print("Thank you for using Contact Manager by Marko Gidej!")
    exit()


def update_backup():
    pass

def validate_email(email_string):
    global contact_fields
    global contact_list

    if not re.search(r"[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}", email_string):
        print("Must be a valid email format!")
        return False

    if email_string in contact_list.keys():
        print(f"Contact with email of \'{email_string}\' already exists! Try using Edit instead.")
        return False
    
    return True

def main ():
    global contact_fields
    global contact_list

    try:
        with open("Files/contact_list.txt", "r") as file:
            lines = file.readlines()
            contact_fields = lines[0].strip().split("|")

            line_items = []
            line_counter = 1
            while line_counter < len(lines):
                line_items.append(lines[line_counter].strip().split("|"))
                line_counter += 1
            for line in line_items:
                contact_list[line[0]] = line[1:]

            print(contact_fields)
            for key, item in contact_list.items():
                print(f"{key}, {item}")

    except Exception as e:
        print(e)
        print("Base file corrupt!")

    while True:
        print("Welcome to the Contact Management System!\n")
        print("Menu:")
        print("1. Add a new contact")
        print("2. Edit an existing contact")
        print("3. Delete a contact")
        print("4. Search for a contact")
        print("5. Display all contacts")
        print("6. Export contacts to a text file")
        print("7. Import contacts from a text file")
        print("8. Quit")

        choice = input()

        if choice == "1":
            add_contact()
        elif choice == "2":
            edit_contact()
        elif choice == "3":
            delete_contact()
        elif choice == "4":
            search_contact()
        elif choice == "5":
            dispaly_contacts()
        elif choice == "6":
            export_contacts()
        elif choice == "7":
            import_contacts()
        elif choice == "8":
            quit_app()
        else:
            print("Please enter a number 1-8!")


main()