import json

filename = 'favorite_num.json'

try:
    with open(filename) as f:
        #loading favorite number
        num = json.load(f)
except FileNotFoundError:
    # if no favorite number, lets create one
    num = input('What is your favorite number? ')
    with open(filename, 'w') as f:
        json.dump(num, f)
        print('We now know your favorite number is', num)
else:
    #if there was already a favorite number
    print('We already knew your favorite number was', num)






