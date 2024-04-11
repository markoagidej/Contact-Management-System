Link to GitHub Repository:
https://github.com/markoagidej/Contact-Management-System

# Contact Manager by Marko Gidej

## Overview:

This is a useful app for keeping track of a list of contacts!

Each contact contains multiple fields for information, as listed below. Email is the only unique and required field!
1. E-mail (unique and required)
2. Name
3. Phone Number
4. Address
5. Notes
5. Groups

Groups work differently than the other fields! Scroll tot he bottom of this and read "Grouping" for more info.
Additionally, you have the option to add your own fields when creating or editing a contact!

After launching the app, you will be presented with a menu which has 8 options. Simply type the number of the option you would like to perform and hit ENTER.
The menu options are as follows:
1. Add a new contact
2. Edit an existing contact
3. Delete a contact
4. Search for a contact
5. Display all contacts
6. Export contacts to a text file
7. Import/Restore contacts from a text file
8. Quit

### 1. Add a new contact

When adding a new contact, you will first be prompted to enter a valid email address.
If the address is valid and does not already exist in your contacts, you will then be asked to fill in each of the remaining fields (which can remain empty if you wish).
If you enter a non-valid email or that email is already in your contacts, you will recieve the corresponding error messege.
At this point you will also have the option to create your own contact field with a (y/n) prompt.
Entering 'y' will prompt you for the name of your new field then the data you would like to enter. Entering anything else will finish making the contact.
> ***NOTE:*** Any custom field you enter will now show up as an option when creatign a new contact! 
At any time after entering a valid email address you can type '/end' to leave the rest of the field empty


### 2. Edit an existing contact

You will be prompted to enter the email of the contact you would like to edit.
You will then be asked which contact field you would like edit.
Here there will also be an option to create a new field. This new field will be created as an empty entry for every other contact in your list!
If you select email, a new contact will be made with a copy of all of the existing fields. You will be asked if you would like to keep or delete the original contact.
It is not possible to edit the email to an email which already exists for another contact!

### 3. Delete a contact

Simply enter the email of the contact you would like to delete!
There will be a confirmation messege with all the contacts info, to which you must reply (y/n).

### 4. Search for a contact

It is possible to search for a contact via any of the contact fields!
After choosing this option, you must pick which field you would like to search.
> ***NOTE:*** The search will look for anythign which contains tour input, so you may recieve a list of contacts!

### 5. Display all contacts

View a list of all your conacts.
Before viewing the list, you will be asked if you would like the list to be sorted by a certain field.

### 6. Export contacts to a text file

Save the contacts you have added to a .txt file to be imported by someone else using this app!
These will appear in the "Files\Exports" folder.

### 7. Import/Restore contacts from a text file

If you need to have the same contacts as someone else who uses this app, import their .txt file to add those contacts to your own list!
The first choice for this option is to either import another file, or load the latest backup.
> When restoring a backup, it will delete any changes you currently have and match the data in the resotre file exactly!
To import a file, you must type the name of the file. Some example file are included!
If there are duplicate contacts, you will be asked to either keep yours, or overwrite from the incoming file.
Custom fields will also be merged into your file! If there is a field with teh same name, letter-case will match the imported file!

### 8. Quit

Exit the app. Thanks for using!

## Other Features

In addition to the actions you can take from the main menu, this program has a couple other features!

### Backup and Restoring Functionality

Whenever you make a change to your contact data, the change will be reflected in a backup file.
You can reload all of your data from the latest backup by using the Import/Restore menu option.

### Grouping

Groups can be assigned to contacts to enhance you searching capabilities.
Contacts can belong to any number of the predefined groups (or none!):
1. Friends
2. Family
3. Work
When making changes to a contact's Groups, selection will be toggled on or off.


Thanks for using my app!

Link to GitHub Repository:
https://github.com/markoagidej/Contact-Management-System