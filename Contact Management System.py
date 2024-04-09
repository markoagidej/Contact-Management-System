
import re

contact_fields = []
contact_list = {}


def add_contact():
    pass


def edit_contact():
    pass


def deelte_contact():
    pass


def search_contact():
    pass


def disaplys_contacts():
    pass


def export_contacts():
    pass


def import_contacts():
    pass


def quit_app():
    print("Thank you for using Contact Manager by Marko Gidej!")
    exit()


def update_backup():
    pass


def main ():
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
            deelte_contact()
        elif choice == "4":
            search_contact()
        elif choice == "5":
            disaplys_contacts()
        elif choice == "6":
            export_contacts()
        elif choice == "7":
            import_contacts()
        elif choice == "8":
            quit_app()
        else:
            print("Please enter a number 1-8!")


main()