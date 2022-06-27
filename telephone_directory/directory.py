import os
from contact import Contact

class Directory:
    contact_info = {}
    contact_list = []

    def __init__(self, contact_list) -> None:
        self.contact_list = contact_list

    # Creates the contact name
    def contact_name(self):
        contact_name = input('Ingrese el nombre del contacto: ')
        return contact_name

    # Creates the contact number
    def contact_number(self):
        contact_number = int(input('Ingrese el numero del contacto: '))
        return contact_number

    # Registers a contact in the contacts array
    def contact_creator(self):
        new_contact = self.contact_creator_validator()
        new_contact = self.contact_info(new_contact.name, new_contact.number)
        self.contact_list.append(new_contact)

    # Base of teh contact input validator
    def contact_creator_validator(self):
        opt = 1
        while opt == 1:
            name = self.contact_name()
            number = self.contact_number()
            opt = self.contact_creator_validator_message(name, number)
        new_contact = Contact(name, number)
        return new_contact

    # Validates the contact input
    def contact_creator_validator_message(self, name: str, number: int) -> int:
        print('Nombre: {} | Número: {}'.format(name, number))
        print('¿Desea guardar el contacto? 1. Sí  2. No')
        try:
            opt = int(input('Opción: '))
            if opt == 1:
                opt = 0
                return opt
            elif opt == 2:
                opt = 1
                return opt
            else:
                assert ValueError('Ingrese una opción válida')
            
        except ValueError:
            print('Ingrese una opción válida')

    # Show all the contacts in the contacts array
    def show_contacts(self):
        for contact in self.contact_list:
            for key, value in contact.items():
                print('{}: {}'.format(key, value))
            print('---------')

    # Creates the contact dictionary
    def contact_info(self, name, number):
        contact_dict = {
            'Name':name,
            'Number':number
        }
        return contact_dict

    # Edits a contact
    def edit_contact_message(self):
        index = 1
        print('Sus contactos acuales son:')
        for contact in self.contact_list:
            print('{}. {}'.format(index, contact["Name"]))
            index += 1

    # Edits a contact name and number 
    def contact_selector(self, index):
        self.contact_list[index]
        print('Datos actuales: Nombre->{} | Número->{}'.format(self.contact_list[index].get('Name'), self.contact_list[index].get('Number')))
        self.contact_list[index]['Name'] = input('Nuevo Nombre: ')
        self.contact_list[index]['Number'] = int(input('Nuevo Numero: '))

    # Edit contact main menu
    def edit_contact_input(self):
        self.edit_contact_message()
        option = int(input('Elija una opción: ')) - 1
        self.contact_selector(option)


