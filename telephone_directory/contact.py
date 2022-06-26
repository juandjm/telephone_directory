class Contact:
    name = str
    number = int

    def __init__(self, name, number) -> None:
        self.name = name
        self.number = number

    def edit_name(self):
        self.name = input('Ingrese el nuevo nombre: ')

    def edit_number(self):
        try:
            self.number = int(input('Ingrese el nuevo número: '))
        except ValueError:
            print('Ingrese un número válido')

    def show_contact(self):
        print('Nombre: {} | Teléfono: {}'.format(self.name, self.number))