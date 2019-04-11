
def show_magicians(magicians):
    for magician in magicians:
        print(magician)


def make_great(magicians):
    #create empty list to put the greats in
    great_magicians = []

    #adding the great to magicians and appending to great_magicians
    while magicians:
        magician = magicians.pop()
        great_magician = magician + ' The Great'
        great_magicians.append(great_magician)

    for great_magician in great_magicians:
        magicians.append(great_magician)

    return magicians


magicians = ['Bob', 'Steve', 'Roger']
show_magicians(magicians)

print('\nGreat magicians: ')
great_magicians = make_great(magicians[:])
show_magicians(great_magicians)

print('\nOriginal Magicians: ')
show_magicians(magicians)



