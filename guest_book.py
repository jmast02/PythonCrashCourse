filename = 'guest_book.txt'

while True:
    name = input('Name: ')
    if name == 'quit':
        break
    else:
        with open(filename, 'a') as file_object:
            file_object.write(name + '\n')
            print(f"{name}, you have been added to the guest book.")


