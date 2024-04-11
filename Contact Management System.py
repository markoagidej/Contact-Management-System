
import re
import datetime
import os

contact_fields = []
contact_list = {}
CONTACT_GROUPS = {
    "Friends": False,
    "Family": False,
    "Work": False
    }

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
        elif field == "Groups":
            contact_data.append(group_toggle())
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
    update_backup()
    print(f"Added contact for {email}: {contact_data}")


def edit_contact():
    global contact_fields
    global contact_list
    
    while True:
        edit = input("Enter the email of the contact you would like to edit: ")
        if edit in contact_list:

            contact_field_len = len(contact_fields)

            while True:
                try:
                    field_counter = 1
                    print("Which field would you like to edit?")
                    for field in contact_fields:
                        print(f"{field_counter}. {field}")
                        field_counter += 1
                    else:
                        print(f"{field_counter}. New Field")
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
                update_backup()
                break
            elif choice_index == 5:
                contact_list[edit][4] = group_toggle(edit)
                update_backup()
                break
            elif choice_index == contact_field_len:
                new_field_data = new_field()
                contact_list[edit][choice_index - 1] = new_field_data
                update_backup()
                break
            else:
                new_input = input(f"Enter new data for {edit} in {contact_fields[choice_index]}: ")
                contact_list[edit][choice_index - 1] = new_input
                print(f"Set {contact_fields[choice_index]} for contact {edit} as: {new_input}")
                update_backup()
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
            update_backup()
        else:
            print("No contacts deleted!")

    else:
        print(f"There is no contact with the email of {to_delete}!")


def search_contact():
    global contact_fields
    global contact_list
    
    field_label = 1
    for field in contact_fields:
        print(f"{field_label}. {field}")
        field_label += 1

    while True:
        answer = int(input("Which field would you like to search by?: "))
        if answer > 0 or answer <= len(contact_fields):
            break
        else:
            print(f"Input a number between 1 and {len(contact_fields)}")
            continue

    answer_field_index = answer - 1
    search = input("What would you like to search for?: ")
    search_lowered = search.lower()
    return_list = []
    if answer_field_index == 0:
        for email in contact_list.keys():
            email_lowered = email.lower()
            if search_lowered in email_lowered:
                return_list.append(email)
    else:
        for email, detail in contact_list.items():
            detail_lowered = detail[answer_field_index - 1].lower()
            if search_lowered in detail_lowered:
                return_list.append([email, detail[answer_field_index - 1]])
        
    if return_list:
        print(f"Found matches for \'{search}\' in \'{contact_fields[answer - 1]}\' of the following contacts:")
        for result in return_list:
            print(result)
    else:
        print("No matches found!")


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
    filename = "Contact_List_" + str(formatted_date) +".txt"
    with open(f"Files\\Exports\\{filename}", 'w') as file:
        file.write("|".join(contact_fields))
        for contact, details in contact_list.items():
            file.write("\n" + "|".join((contact, "|".join(details))))

    print(f"Saved {filename} to Files\Exports folder!")


def import_contacts():
    global contact_fields
    global contact_list

    while True:
        answer = input("Would you like to [i]mport a file or [r]estore the latest backup? (i/r)")
        if answer == "r":
            filelist = os.listdir("Files\\Backups")
            if filelist:
                filelist.sort()                
                try:
                    with open(f"Files\\Backups\\{filelist[-1]}", "r") as file:
                        lines = file.readlines()
                        contact_fields = lines[0].strip().split("|")

                        line_items = []
                        line_counter = 1
                        while line_counter < len(lines):
                            line_items.append(lines[line_counter].strip().split("|"))
                            line_counter += 1
                        for line in line_items:
                            contact_list[line[0]] = line[1:]
                    print(f"Restored from file {filelist[-1]}!")
                except Exception as e:
                    print(e)
                    print("Base file corrupt!")

            else:
                print("No backups found!")
                return

            return
        elif answer == "i":
            break
        else:
            print("Enter 'i' to import, or 'r' to restore the last backup!")
            continue

    filename = input("Enter the name with extension of file you would like to import (import_example.txt for grading assignment):")
    
    try:
        with open(f"Files\\{filename}", "r") as file:
            lines = file.readlines()
            new_contact_fields = lines[0].strip().split("|")
            new_contact_list = {}

            line_items = []
            line_counter = 1
            while line_counter < len(lines):
                line_items.append(lines[line_counter].strip().split("|"))
                line_counter += 1
            for line in line_items:
                new_contact_list[line[0]] = line[1:]
    except FileNotFoundError:
        print("Filename does not exist!")
        return
    except:
        print("Could not open file")
        return

    # compare field list
    if len(new_contact_fields) > 6 or len(contact_fields) > 6:
        if len(new_contact_fields) > 6:
            new_field_ext = new_contact_fields[6:]
            new_field_ext_lower = []
            for field in new_field_ext:
                new_field_ext_lower.append(field.lower())
        else:
            new_field_ext = []
            new_field_ext_lower = []

        if len(contact_fields) > 6:
            contact_fields_ext = contact_fields[6:]
            contact_fields_ext_lower = []
            for field in contact_fields_ext:
                contact_fields_ext_lower.append(field.lower())
        else:
            contact_fields_ext = []
            contact_fields_ext_lower = []
    
        # add fields missing from current contact list to current (also the import casing will always take precedence)
        new_ext_field_index = 0
        for new_field_lower in new_field_ext_lower:
            if new_field_lower in contact_fields_ext_lower:
                old_index = 6 + contact_fields_ext_lower.index(new_field_lower)
                contact_fields[old_index] = new_field_ext[new_ext_field_index]
                new_ext_field_index += 1
            else:
                contact_fields_ext.append(new_field_ext[new_ext_field_index])
                for contact in contact_list.keys():
                    contact_list[contact].append('')
                new_ext_field_index += 1

        # add fields missing from new contact list to new
        for field_lower in contact_fields_ext_lower:
            if field_lower not in new_field_ext_lower:
                for new_contact in new_contact_list.keys():
                    new_contact_list[new_contact].append('')

        base_contact = contact_fields[0:6]
        contact_fields = base_contact + contact_fields_ext        

    # compare all emails
    email_dupe = False
    for email in contact_list:
        for new_email in new_contact_list:
            if email.lower() == new_email.lower():
                email_dupe = True
                break
            if email_dupe:
                break

    if email_dupe:
        print("Duplicate emails detected in imported file!")
        print("Would you like to [o]verwrite your data or [k]eep it (o/k)")
        while True:
            answer = input()
            if answer == "o":
                for new_email, new_details in new_contact_list.items():
                    contact_list[new_email] = new_details
                break
            elif answer == "k":
                for new_email, new_details in new_contact_list.items():
                    if new_email not in contact_list:
                        contact_list[new_email] = new_details
                break
            else:
                print("You must enter 'o'(overwrite) or 'k'(keep)!")
    else:
        for new_email, new_details in new_contact_list.items():
            contact_list[new_email] = new_details

    update_backup()


def quit_app():
    print("Thank you for using Contact Manager by Marko Gidej!")
    exit()


def update_backup():
    global contact_fields
    global contact_list

    current_datetime = datetime.datetime.now()
    formatted_date = current_datetime.strftime("%Y-%m-%d %H-%M-%S")
    filename = "Contact_List_BACKUP_" + str(formatted_date) +".txt"
    with open(f"Files\\Backups\\{filename}", 'w') as file:
        file.write("|".join(contact_fields))
        for contact, details in contact_list.items():
            file.write("\n" + "|".join((contact, "|".join(details))))


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


def group_toggle(email_string = ''):
    global contact_fields
    global contact_list
    global CONTACT_GROUPS

    if email_string:
        group_list = contact_list[email_string][4].split(",")

        groups_this = CONTACT_GROUPS
        for group in group_list:
            if group in groups_this:
                groups_this[group] = True

        if group_list[0]:
            print(f"{email_string} belongs to these groups:")
            for group in group_list:
                print(group)
        else:
            print(f"{email_string} does not belong to any groups!")

    else:
        groups_this = CONTACT_GROUPS

    while True:
        print("1. Friends")
        print("2. Family")
        print("3. Work")
        print("4. Finish")
        while True:
            answer = int(input("Enter the number of the group you would like to toggle: "))
            if answer < 1 or answer > 4:
                print("Enter a number between 1 and 4!")
                continue
            else:
                break

        if answer == 1:
            if groups_this["Friends"]:
                groups_this["Friends"] = False
            else:
                groups_this["Friends"] = True
        elif answer == 2:
            if groups_this["Family"]:
                groups_this["Family"] = False
            else:
                groups_this["Family"] = True
        elif answer == 3:
            if groups_this["Work"]:
                groups_this["Work"] = False
            else:
                groups_this["Work"] = True
        else:
            break

        print("Now belongs to these groups:")
        for group, value in groups_this.items():
            if value:
                print(group)                
                
    print("Finally set to these groups:")
    for group, value in groups_this.items():
        if value:
            print(group)

    entry = ''
    for group in groups_this:
        if entry:
            if groups_this[group]:
                entry += f",{group}"
        else:
            if groups_this[group]:
                entry += group
    return entry


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
        print("7. Import/Restore from a text file")
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