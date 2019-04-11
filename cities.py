cities = {
    'Coral Springs': {
        'location': 'florida',
        'population': 2345
    },
    'Los Angeles': {
        'location': 'california',
        'population': 4738
    },
    'Manhattan': {
        'location': 'new york',
        'population': 4545
    }
}

for place, info in cities.items():
    print(f"City name {place}: ")
    print(f"\tIs located in the state of {info['location'].title()}, with a population of {info['population']}.")