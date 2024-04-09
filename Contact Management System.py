
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
    while True:
        print("Welcome to the Contact Management System!\n\n")
        print("Menu:\n")
        print("1. Add a new contact\n")
        print("2. Edit an existing contact\n")
        print("3. Delete a contact\n")
        print("4. Search for a contact\n")
        print("5. Display all contacts\n")
        print("6. Export contacts to a text file\n")
        print("7. Import contacts from a text file\n")
        print("8. Quit\n")

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