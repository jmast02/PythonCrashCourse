pets = []

pet = {
    'name' : 'charlie',
    'owner': 'jon',
    'type': 'dog'
}

pets.append(pet)

pet = {
    'name': 'bozo',
    'owner': 'steve',
    'type': 'dog'
}

pets.append(pet)

# print pets list
print(pets)


#grab each individual pet
for pet in pets:
    print(f"\nHere is what I know about {pet['owner'].title()}'s pet:")
#iterate through the individual pet's keys and values
    for k , v in pet.items():
        print(f"\t{k}: {v}.")






