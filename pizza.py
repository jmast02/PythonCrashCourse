pizza = ['pepperoni', 'cheese', 'bacon']

for topping in pizza:
    print("I love " + topping + " on my pizza.")

print('\nI really love pizzaaaaaaa!')

friends_pizza = pizza[:]

pizza.append('sausage')
friends_pizza.append('peppers')

print(pizza)
print(friends_pizza)