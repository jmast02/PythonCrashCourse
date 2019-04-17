class Restaurants():
    def __init__(self, restaurant_name, cuisine_type):
        # initialize restaurant and cuisine attributes
        self.restaurant = restaurant_name
        self.cuisine = cuisine_type

    def describe_restaurant(self):
        print(f"{self.restaurant.title()} serves {self.cuisine.title()} food.")

    def open_restuarant(self):
        print(f"{self.restaurant.title()} is open!")


#creating an instance my_restaurant
my_restaurant = Restaurants('Tijuana taxi co.', 'mexican')
my_restaurant.describe_restaurant()
my_restaurant.open_restuarant()


print('\n')
#create a new instance for joes restaurant
joes_restaurant = Restaurants('olive garden', 'italian')
joes_restaurant.describe_restaurant()


#one more instance for fun
print('\n')
steves_restaurant = Restaurants('Benihana', 'japanese')
steves_restaurant.describe_restaurant()