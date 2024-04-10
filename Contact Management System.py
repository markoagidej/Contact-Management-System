
import re
import datetime

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
        elif field == "Group":
            group_toggle()
        else:
            field = input(f"Enter {field}: ")
            if field == "/end":
                while len(contact_data) < len(contact_fields) - 1:
                    contact_data.append("")
                break
            else:
                contact_data.append(field)
    else:
        answer = input("Type 'yes' to create a new field: ")
        if answer == 'yes':
            contact_data.append(new_field())

    contact_list[email] = contact_data
    print(f"Added contact for {email}: {contact_data}")
    
    update_backup()


def edit_contact():
    global contact_fields
    global contact_list
    
    while True:
        edit = input("Enter the email of the contact you would like to edit: ")
        if edit in contact_list:

            contact_field_len = len(contact_fields)

            while True:
                try:
                    field_counter = 0
                    print("Which field would you like to edit?")
                    for field in contact_fields:
                        print(f"{field_counter + 1}. {field}")
                        field_counter += 1
                    else:
                        print(f"{field_counter + 1}. New Field")
                    choice = int(input())
                    choice_index = choice - 1

                    if choice_index > contact_field_len or choice_index < 0:
                        print(f"Choose a number between 1 and {contact_field_len}!")
                        continue

                    break
                except:
                    print(f"Choose a number between 1 and {contact_field_len}!")
                    continue

            if choice_index == 0:
                while True:
                    conversion = input("Would you like to [o]verwrite this email or create a contact with [d]uplicated data? (o/d)")
                    if conversion == "o" or conversion == "d":
                        break
                    else:
                        print("Enter 'o' to overwrite email, or 'd' to create a new contact with duplicate data.")
                        continue
                
                while True:
                    new_email = input("Enter the new email: ")
                    if validate_email(new_email):
                        break

                if conversion == "o":
                    contact_list[new_email] = contact_list[edit]
                    del contact_list[edit]
                elif conversion == "d":
                    contact_list[new_email] = contact_list[edit]

                print(f"Contact for {new_email} created!")
                break
            elif choice_index == contact_field_len:
                new_field_data = new_field()
                contact_list[edit][choice_index - 1] = new_field_data
                break
            else:
                new_input = input(f"Enter new data for {edit} in {contact_fields[choice_index]}: ")
                contact_list[edit][choice_index - 1] = new_input
                print(f"Set {contact_fields[choice_index]} for contact {edit} as: {new_input}")
                break

        else:
            print(f"{edit} is not a contact in your list!")
            continue


def delete_contact(to_delete):
    global contact_fields
    global contact_list
    
    if to_delete in contact_list:
        print("Are you sure you would like to delete this contact (y/n):")
        details_string = ""
        field_num = 1
        for field_detail in contact_list[to_delete]:
            details_string += contact_fields[field_num] + " - " + field_detail + " | "
            field_num += 1
        print(f"{to_delete}: {details_string}")

        answer = input()
        if answer == "y":
            del contact_list[to_delete]
            print(f"Deleted {to_delete} from contacts!")
        else:
            print("No contacts deleted!")

    else:
        print(f"There is no contact with the email of {to_delete}!")


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
    
    current_datetime = datetime.datetime.now()
    formatted_date = current_datetime.strftime("%Y-%m-%d %H-%M-%S")
    filename = "Contact_List " + str(formatted_date) +".txt"
    with open(f"Files\\Exports\\{filename}", 'w') as file:
        file.write("|".join(contact_fields))
        for contact, details in contact_list.items():
            file.write("\n" + "|".join((contact, "|".join(details))))

    print(f"Saved {filename} to Files/Exports folder!")


def import_contacts():
    global contact_fields
    global contact_list
    pass


def quit_app():
    print("Thank you for using Contact Manager by Marko Gidej!")
    exit()


def update_backup():
    global contact_fields
    global contact_list
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


def group_toggle():
    global contact_fields
    global contact_list
    pass


def new_field():
    global contact_fields
    global contact_list

    while True:
        field_name = input("Enter a title for the new field: ")
        if field_name not in contact_fields:
            contact_fields.append(field_name)
            print(f"New field, {field_name}, created!")
            field_detail = input(f"Enter data for {field_name}: ")
            for detail in contact_list.values():
                detail.append("")
            return field_detail
        else:
            print("That field already exists! Try a different field title.")
            continue


def debugger():
    global contact_fields
    global contact_list

    contact_fields.append("new")
    for detail in contact_list.values():
        detail.append("")


def main ():
    global contact_fields
    global contact_list

    try:
        with open("Files\\contact_list.txt", "r") as file:
            lines = file.readlines()
            contact_fields = lines[0].strip().split("|")

            line_items = []
            line_counter = 1
            while line_counter < len(lines):
                line_items.append(lines[line_counter].strip().split("|"))
                line_counter += 1
            for line in line_items:
                contact_list[line[0]] = line[1:]

    except Exception as e:
        print(e)
        print("Base file corrupt!")

        
    print("Welcome to the Contact Management System!\n")

    while True:
        print("Menu:")
        print("1. Add a new contact")
        print("2. Edit an existing contact")
        print("3. Delete a contact")
        print("4. Search for a contact")
        print("5. Display all contacts")
        print("6. Export contacts to a text file")
        print("7. Import contacts from a text file")
        print("8. Quit")
        # print("9. debugger")

        choice = input()

        if choice == "1":
            add_contact()
        elif choice == "2":
            edit_contact()
        elif choice == "3":
            delete_contact(input("Enter the email of the contact you want to delete: "))
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
        # elif choice == "9":
        #     debugger()
        else:
            print("Please enter a number 1-8!")


main()