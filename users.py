class User():

    def __init__(self, first_name, last_name, location, age):
        #initialize name, location, age attributes
        self.first_name = first_name
        self.last_name = last_name
        self.location = location
        self.age = age

    def describe_user(self):
        #created a general formatted profile string tying together all parameters.
        print(f"User Profile: {self.first_name.title()} {self.last_name.title()} is {str(self.age)}"
              f" years old, and lives in {self.location.title()}.")

    def greet_user(self):
        print('Welcome back,', self.first_name.title())


#created an instance 'jon' for the class User
jon = User('jon', 'mast', 'florida', 26)
jon.describe_user()
jon.greet_user()

#another instance
scott = User('scott', 'mast', 'fort myers, florida', 30)
scott.describe_user()
scott.greet_user()

