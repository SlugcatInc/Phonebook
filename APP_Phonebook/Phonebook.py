import json

def load_data():
    try:
        with open('phonebook.json', 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        data = {}
    
    return data

def save_data(data):
    with open('phonebook.json', 'w') as file:
        json.dump(data, file)

def view_contacts(data):
    for name, number in data.items():
        print(f'{name}: {number}')

def add_contact(data, name, number):
    data[name] = number
    save_data(data)
    print('Contact added successfully.')

def search_contact(data, name):
    if name in data:
        print(f'{name}: {data[name]}')
    else:
        print('Contact not found.')

def delete_contact(data, name):
    if name in data:
        del data[name]
        save_data(data)
        print('Contact deleted successfully.')
    else:
        print('Contact not found.')

def modify_contact(data, name, new_number):
    if name in data:
        data[name] = new_number
        save_data(data)
        print('Contact modified successfully.')
    else:
        print('Contact not found.')

def main():
    data = load_data()
    
    while True:
        print('Phonebook Menu:')
        print('1. View Contacts')
        print('2. Add Contact')
        print('3. Search Contact')
        print('4. Delete Contact')
        print('5. Modify Contact')
        print('6. Exit')
        
        choice = input('Enter your choice: ')

        if choice == '1':
            view_contacts(data)
        elif choice == '2':
            name = input('Enter contact name: ')
            number = input('Enter contact number: ')
            add_contact(data, name, number)
        elif choice == '3':
            name = input('Enter contact name: ')
            search_contact(data, name)
        elif choice == '4':
            name = input('Enter contact name: ')
            delete_contact(data, name)
        elif choice == '5':
            name = input('Enter contact name: ')
            new_number = input('Enter new contact number: ')
            modify_contact(data, name, new_number)
        elif choice == '6':
            break
        else:
            print('Invalid choice. Please try again.')
    
if __name__ == '__main__':
    main()