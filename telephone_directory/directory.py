from contact import Contact
from menu import Menu

def run():
    person = Contact('Juan David', 3057859716)
    print(vars(person))
    person = Menu.edit_contact(person.name, person.number)
    print(vars(person))

if __name__ == '__main__':
    run()