def city_country(city, country, population = ''):
    """Return a string like 'Santiago, Chile - population = 1000'."""
    if population:
        output = city.title() + ', ' + country.title()
        output += ' - population ' + str(population)
        return output
    else:
        return city.title() + ', ' + country.title()

spain = city_country('madrid', 'spain', 1000)
print(spain)
