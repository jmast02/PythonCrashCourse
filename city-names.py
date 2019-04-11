def city_country(city, country):
    city_and_country = f"{city}, {country}"
    return city_and_country.title()

chile = city_country('santiago', 'chile')
print(chile)

finland = city_country('helsinki', 'finland')
print(finland)

greece = city_country('athens', 'greece')
print(greece)