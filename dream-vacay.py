responses = {}

polling_active = True

while polling_active:


    name = input('\nWhat is your name? ')
    vacay = input('Where would you like to go on vacation to? ')

    responses[name] = vacay

    repeat = input('Is anybody else taking the poll? (Y/N)').upper()
    if repeat == 'n'.upper():
        polling_active = False

print('---Poll Results---')

for name, vacay in responses.items():
    print(f"{name.title()}, would like to go to {vacay.title()}.")

print(responses)
