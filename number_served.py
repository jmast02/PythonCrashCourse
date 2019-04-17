class Restaurant():

    def __init__(self, restaurant_name, cuisine_type):
        # initialize restaurant and cuisine attributes
        self.restaurant = restaurant_name
        self.cuisine = cuisine_type
        # created new attribute to tell us how many customers were served.
        self.number_served = 0

    def describe_restaurant(self):
        print(f"{self.restaurant.title()} serves {self.cuisine.title()} food.")

    def open_restuarant(self):
        print(f"{self.restaurant.title()} is open!")

    def set_number_served(self, number_served):
        #updates number of customers served
        self.number_served = number_served

    def increment_number_served(self, additional_customers_served):
        #adding more customers to total served so far today.
        self.number_served += additional_customers_served







jons_restaurant = Restaurant('Tijuana', 'Mexican')

# 0 served to start the day
print(jons_restaurant.number_served)

# 20 served so far today
jons_restaurant.set_number_served(20)

print(jons_restaurant.number_served)

#added 30 customers to our 20 customers.
jons_restaurant.increment_number_served(30)

print(jons_restaurant.number_served)

