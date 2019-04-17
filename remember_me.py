import json

def greet_user():
    '''Greet user by name'''
    username = get_stored_username()
    if username:
        correct = input('is this the correct username? (y/n)')
        if correct == 'y':
            print('Welcome back', username)
        else:
            username = get_new_username()
            print('We will remember you next time', username)
    else:
        username = get_new_username()
        print('We will remember you next time, ', username)

def get_stored_username():
    '''get stored username if available'''
    filename = 'username.json'
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_username():
    '''prompt for new username'''
    username = input('Enter name: ')
    filename = 'username.json'
    with open(filename, 'w') as f:
        json.dump(username, f)
    return username

greet_user()