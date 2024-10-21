def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return"ПОМИЛКА: Неправильний формат. Будь ласка, введіть ім'я і номер телефону."
        except IndexError:
            return "ПОМИЛКА: Недостатньо аргументів для команди."
        except KeyError:
            return "ПОМИЛКА: Контакт не знайдено."
    return inner

def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, args

@input_error
def add_contact(args, contacts):
    if len(args) != 2:
        raise ValueError
    name, phone = args
    contacts[name] = phone
    return "Contact added."

@input_error
def change_contact(args, contacts):
    if len(args) != 2:
        raise ValueError
    name, new_phone = args
    if name not in contacts:
        raise KeyError
    contacts[name] = new_phone
    return "Contact updated."

@input_error
def show_phone(args, contacts):
    if len(args) != 1:
        raise IndexError
    name = args[0]
    if name in contacts:
        return f"Мобільний телефон для {name}: {contacts[name]}"
    else:
        raise KeyError
    
    
@input_error
def show_all(args, contacts):
    if not contacts:
        return("Немає збережених контактів")
    resoult = ("Всі збережені контакти:\n")
    for name, phone in contacts.items():
        resoult += f"{name} {phone}\n"
    return resoult.strip()
 
    

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)
        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))  
        elif command == "phone":
            print(show_phone(args, contacts))  
        elif command == "all":
            print(show_all(args, contacts))        
        else:
            print("Invalid command.")    
if __name__ == "__main__":
   main()            
