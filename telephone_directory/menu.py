from contact import Contact

class Menu():
    contact_list = {}

    # def __init__(self, contact):
    #     self.contact = contact

    def edit_contact(name: str, number: int):
        print('El nombre actual del contacto es ' + name)
        Contact.edit_contact_name(name)
        print('El número actual del contacto es ' + str(number))
        Contact.edit_contact_number(number)
