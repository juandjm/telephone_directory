from contact import Contact

class Directory:
    contact_list = {}

    def __init__(self, contact_list: dict) -> None:
        self.contact_list = contact_list

    def contact_name(self):
        contact_name = input('Ingrese el nombre del contacto: ')
        return contact_name

    def contact_number(self):
        contact_number = int(input('Ingrese el numero del contacto: '))
        return contact_number

    def contact_creator(self):
        new_contact = self.contact_creator_validator()
        self.contact_list[new_contact.name] = new_contact.number

    def contact_creator_validator(self):
        opt = 1
        while opt == 1:
            name = self.contact_name()
            number = self.contact_number()
            opt = self.contact_creator_validator_message(name, number)
        new_contact = Contact(name, number)
        return new_contact

    def contact_creator_validator_message(self, name: str, number: int) -> int:
        print('Nombre: {} | Número: {}'.format(name, number))
        print('¿Desea guardar el contacto? 1. Sí  2. No')
        try:
            opt = int(input('Opción: '))
            if opt == 1 or opt == 2:
                return opt
            else:
                assert ValueError('Ingrese una opción válida')
            
        except ValueError:
            print('Ingrese una opción válida')

    def show_contacts(self):
        i = 0
        for key, value in self.contact_list:
            i += 1
            print('{}. Nombre: {} | Número: {}'.format(i, key, value))


contacts = {}
xd = Directory(contacts)

xd.contact_creator()

xd.show_contacts()
