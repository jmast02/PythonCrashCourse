favorite_places = {
    'steve': ['london', 'paris'],
    'joe': ['france', 'egypt']
}

for name, places in favorite_places.items():
    print(f"{name.title()}'s favorite places are :")
    for place in places:
        print(f"\t{place.title()}")