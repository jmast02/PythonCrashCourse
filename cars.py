def make_car(manufacturer, make, **user_info):
    car = {}
    car['manufacturer'] = manufacturer
    car['make'] = make
    for k, v in user_info.items():
        car[k] = v
    return car

bobs_car = make_car('ford', 'mustang', year = '1992', color = 'red')

print(bobs_car)
