'''def make_shirt(size = 'large', text = 'I love Python'):
    print(f'I would like a size {size} that says "{text}".')

make_shirt()


def describe_city(city, country = 'USA'):
    print(f"{city.title()}, is in {country}.")


describe_city('boston')

#optional argument, we place at the end, set it to False with empty strings
def full_name(first, last, middle = ''):
    if middle:
        full = (f"{first} {middle} {last}")
    else:
        full = (f"{first} {last}")
    return full.title()

user1 = full_name('jon', 'mast', 'edward')
print(user1)'''


def get_formatted_name(first, last):
    full_name = (f"{first} {last}")
    return full_name.title()


while True:
    print('Please tell me your name \nEnter "q" to quit.')

    f_name = input('Enter your first name: ')
    if f_name.lower() == 'q':
        break
    l_name = input('Enter your last name: ')
    if l_name.lower() == 'q':
        break

    formatted_name = get_formatted_name(f_name, l_name)
    print(formatted_name)


