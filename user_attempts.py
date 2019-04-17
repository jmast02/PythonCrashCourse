class User():

    def __init__(self, first_name, last_name, location, age):
        #initialize name, location, age attributes (then added a login attempts attribute, set to 0.
        self.first_name = first_name
        self.last_name = last_name
        self.location = location
        self.age = age
        self.login_attempts = 0

    def describe_user(self):
        #created a general formatted profile string tying together all parameters.
        print(f"User Profile: {self.first_name.title()} {self.last_name.title()} is {str(self.age)}"
              f" years old, and lives in {self.location.title()}.")

    def greet_user(self):
        print('Welcome back,', self.first_name.title())

    def increment_login_attempts(self):
        # increment login attempts by 1
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

steve = User('steve', 'jones', 'baltimore', 27)
steve.increment_login_attempts()
print(steve.login_attempts)
steve.increment_login_attempts()
steve.increment_login_attempts()
print(steve.login_attempts)
steve.reset_login_attempts()
print(steve.login_attempts)
