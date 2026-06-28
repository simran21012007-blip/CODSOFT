# ==========================================
#         CONTACT BOOK APPLICATION
# ==========================================

contacts = []


def add_contact():
    print("\n--- Add New Contact ---")
    name = input("Enter Name: ").strip().title()
    while True:
       phone = input("Enter 10-digit Phone Number: ").strip()

       if phone.isdigit() and len(phone) == 10:
        break
       else:
           print("Invalid phone number! Please enter exactly 10 digits.")
    while True:
       email = input("Enter Email: ")

       if "@" in email and "." in email:
         break
       else:
          print("Invalid email! Please enter a valid email address.")
    address = input("Enter Address: ")

    contact = {
        "Name": name,
        "Phone": phone,
        "Email": email,
        "Address": address
    }

    contacts.append(contact)
    print("\nContact saved successfully!")


def view_contacts():
    print("\n--- Contact List ---")

    if not contacts:
        print("No contacts found.")
        return

    print("-" * 60)
    print("{:<5} {:<20} {:<15}".format("No.", "Name", "Phone"))
    print("-" * 60)

    for i, contact in enumerate(sorted(contacts, key=lambda x: x["Name"]), start=1):
        print("{:<5} {:<20} {:<15}".format(
            i,
            contact["Name"],
            contact["Phone"]
        ))
    print("-" * 60)
    print(f"Total Contacts: {len(contacts)}")


def search_contact():
    print("\n--- Search Contact ---")

    keyword = input("Enter Name, Phone or Email: ").strip().lower()

    found = False

    for contact in contacts:
      if (
           keyword in contact["Name"].lower()
            or keyword in contact["Phone"]
            or keyword in contact["Email"].lower()
        ):
            print("\nContact Found")
            print("-" * 30)
            print("Name    :", contact["Name"])
            print("Phone   :", contact["Phone"])
            print("Email   :", contact["Email"])
            print("Address :", contact["Address"])
            found = True

    if not found:
        print("Contact not found.")


def update_contact():
    print("\n--- Update Contact ---")

    phone = input("Enter Phone Number of Contact: ")

    for contact in contacts:
        if contact["Phone"] == phone:
             print("This phone number already exists.")
             return

        new_name = input("New Name: ")
        while True:
                new_phone = input("New 10-digit Phone Number (Leave blank to keep old): ")

                if new_phone == "":
                  break
                elif new_phone.isdigit() and len(new_phone) == 10:
                  break
                else:
                   print("Invalid phone number! Please enter exactly 10 digits.")
        new_email = input("New Email: ")
        new_address = input("New Address: ")

        if new_name:
            contact["Name"] = new_name
        if new_phone:
            contact["Phone"] = new_phone
        if new_email:
            contact["Email"] = new_email
        if new_address:
            contact["Address"] = new_address

            print("\nContact updated successfully!")
            return

    print("Contact not found.")


def delete_contact():
    print("\n--- Delete Contact ---")

    phone = input("Enter Phone Number: ")

    for contact in contacts:
        if contact["Phone"] == phone:

            confirm = input("Are you sure you want to delete this contact? (Y/N): ").upper()

            if confirm == "Y":
                contacts.remove(contact)
                print("Contact deleted successfully!")
            else:
                print("Deletion cancelled.")

            return

    print("Contact not found.")

def display_menu():
    print("\n" + "=" * 45)
    print("         MY CONTACT BOOK")
    print("=" * 45)
    print("1. Add Contact")
    print("2. View Contact List")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")
    print("=" * 45)


while True:
    display_menu()

    choice = input("Enter your choice (1-6): ")

    if choice == "1":
        add_contact()

    elif choice == "2":
        view_contacts()

    elif choice == "3":
        search_contact()

    elif choice == "4":
        update_contact()

    elif choice == "5":
        delete_contact()

    elif choice == "6":
       confirm = input("Do you really want to exit? (Y/N): ").upper()

       if confirm == "Y":
           print("\nThank you for using Contact Book!")
           break
       else:
           print("Returning to the main menu...")

    else:
        print("\nInvalid choice! Please enter a number between 1 and 6.")