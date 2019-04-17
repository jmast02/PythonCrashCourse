class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = (f"{str(self.year)} {self.make} {self.model}")
        return long_name.title()

    def read_odometer(self):
        print(f"This car has {str(self.odometer_reading)} miles on it.")

    def update_odometer(self, miles):
        if miles >= self.odometer_reading:
            self.odometer_reading = miles
        else:
            print('You can not roll back an odometer')

    def increment_odometer(self, miles):
        self.odometer_reading += miles


class Electric_car(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()

    def describe_battery(self):
        print(f"This car has a {str(self.battery_size)} kWh battery.")


class Battery():
    def __init__(self, battery_size = 70):
        self.battery_size = battery_size

    def describe_battery(self):
        print (f"This car has a {str(self.battery_size)} kWh battery.")

    def get_range(self):
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270

        message = (f"This car can go approximately {str(range)}"
                   f" miles on a full charge. ")
        print(message)

    def upgrade_battery(self):
        if self.battery_size != 85:
            self.battery_size = 85
        else:
            print('battery already upgraded.')

my_tesla = Electric_car('tesla', 'model s', 2016)
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
my_tesla.battery.upgrade_battery()
my_tesla.battery.get_range()
