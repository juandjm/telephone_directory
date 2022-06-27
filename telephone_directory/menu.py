import os
from directory import Directory

def main_menu():
    print("""
    1. Agregar Contacto
    2. Editar Contacto
    3. Eliminar Contacto
    4. Llamar contacto
    5. Ver lista de contactos
    6. Salir
    """)

def user_menu_input():
    user = int(input('Elige una opción: '))
    return user

def user_choice(contacts, option):
    if option == 1:
        contacts.contact_creator()
    elif option == 2:
        contacts.edit_contact_input()
    elif option == 3:
        pass
    elif option == 4:
        pass
    elif option == 5:
        contacts.show_contacts()
    elif option == 6:
        option = -1
        return option

def exit_message():
    print('¡Hasta pronto!')

def run():
    opt = 0
    contacts = []
    contact_list = Directory(contacts)
    while opt >= 0:
        main_menu()
        opt = user_menu_input()
        user_choice(contact_list, opt)
        if opt == 6:
            break
    exit_message()


if __name__ == '__main__':
    run()