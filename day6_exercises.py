contacts = {}

for i in range(3):
    contact_name = input("Enter contact name: ")
    contact_no = input("Enter contact number: ")
    contacts[contact_name] = contact_no

search = input("Enter contact name you want the number: ")
print(contacts.get(search, "Contact not found"))


