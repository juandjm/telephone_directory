class Contact:
    name = str
    number = int
    email = str
    company = str

    def __init__(self):
        self.name = input('Ingrese el nombre: ')
        self.number = int(input('Ingrese el número: '))

    def edit_contact_name(self):
        self.name = input('Escriba el nuevo nombre: ')

    def edit_contact_number(self):
        self.number = str(input('Escriba el nuevo número: '))

