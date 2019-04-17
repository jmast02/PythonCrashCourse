class Restaurant():

    def __init__(self, restaurant_name, cuisine_type):
        # initialize restaurant and cuisine attributes
        self.restaurant = restaurant_name
        self.cuisine = cuisine_type
        # created new attribute to tell us how many customers were served.
        self.number_served = 0

    def describe_restaurant(self):
        print(f"{self.restaurant.title()} serves {self.cuisine.title()}.")

    def open_restuarant(self):
        print(f"{self.restaurant.title()} is open!")

    def set_number_served(self, number_served):
        #updates number of customers served
        self.number_served = number_served

    def increment_number_served(self, additional_customers_served):
        #adding more customers to total served so far today.
        self.number_served += additional_customers_served


class Ice_Cream_Stand(Restaurant):
    #created child class for Ice cream restuarants. inherits Restaurant.
    def __init__(self, restaurant_name, cuisine_type= 'Ice Cream'):
        super().__init__(restaurant_name, cuisine_type)
        #created empty list to store flavors
        self.flavors = []


    def display_flavors(self):
        print(f"This restaurant has these flavors:")
        for flavor in self.flavors:
            print('-', flavor.title())


'''kilwins = Ice_Cream_Stand('Kilwins')
kilwins.flavors = ['vanilla', 'chocolate']
kilwins.describe_restaurant()
kilwins.display_flavors()'''



