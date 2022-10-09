from collections import UserDict


class Field:
    pass

class Name(Field):
    def __init__(self, value):
        self.value = value

class Phone(Field):
    def __init__(self, value):
        self.value = value

class Record(Field):
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def remove_phone(self, remove_phone):
        for phone in self.phones:
            if phone.value == remove_phone:
                self.phones.remove(phone)
                return f'The phone {remove_phone} has been removed'
    def change_phone(self, old_phone, new_phone):
        for phone in self.phones:
            if phone.value == old_phone:
                self.add_phone(new_phone)
                self.phones.remove(phone)
                return f'The phone {old_phone} has been changed to {new_phone}'
     
class AddressBook(UserDict):
    def add_record(self, record: Record):
        self.data[record.name.value] = record
    def show_record(self, name):
        list = []
        for el in self.data[name].phones:
            list.append(el)
        return f'The contact: {Name} has phones: {list}'

 

a =  AddressBook()   

def input_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)    
        except KeyError:
            print('Enter user name:')
        except ValueError:
            print('Enter correct type:')
        except IndexError:
            print('Give me name and phone please:')
    return wrapper


@input_error
def add(func_arg):
    Record(func_arg[0]).add_phone(func_arg[1])
    a.add_record(Record(func_arg[0]))
    return 'A new contact has been added'

@input_error
def change(func_arg):
    Record(func_arg[0]).change_phone(func_arg[1], func_arg[2])
    return f'The phone: {func_arg[1]} has been changes to {func_arg[2]}'

@input_error
def remove(func_arg):
    Record(func_arg[0]).remove_phone(func_arg[1])
    return f'The phone: {func_arg[1]} has been removed'

@input_error
def phone(func_arg):
    a.show_record(func_arg[0])


@input_error
def show_all(_=None):
    return a.data

@input_error
def hello(_=None):
    return 'How can I help you?'
    
@input_error
def exit(_=None):
    return 'Good bye!'  


commands = {
'add':add,
'good bye':exit,
'close':exit,
'exit':exit,
'hello':hello,
'show all':show_all,
'change':change,
'phone':phone,
'remove':remove,}


def main():
    while True:

        print('Enter command:')
        
        input_string = input().lower()


        if input_string.split()[0] in commands and len(input_string.split()) > 1:

            print(commands[input_string.split()[0]](input_string.split()[1:]))
            
        elif input_string in commands:
            
            print(commands[input_string](input_string))
            
            if commands[input_string](input_string) == "Good bye!":
                break


if __name__ == '__main__':
    main() 