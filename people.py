people = {
    'Jon': {
        'age': 26,
        'city': 'coral springs'
    },
    'callie': {
        'age': 27,
        'city':  'coral springs'
    }
}

for person, info in people.items():
    print("\nName:", person)

    print("\tInfo:", info['age'], ",", end=' ')
    print(info['city'].title())



