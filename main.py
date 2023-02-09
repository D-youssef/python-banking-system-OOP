# Simple Banking system using OOP

# Parent Class: User
class User():
    def __init__(self,name,age,gender,job):
        self.name = name
        self.age = age
        self.gender = gender
        self.job = job

    # function show user's details
    def show_details(self):
        print("Personal Details")
        print("")
        print("Name: ", self.name)
        print("Age: ", self.age)
        print("Gender: ", self.gender)
        print("Job: ", self.job)
        print("")

# Child Class: Bank
class Bank(User):
    def __init__(self,name,age,gender,job):
        super().__init__(name,age,gender,job) # to inherit from User class
        self.balance = 0

    # function to see deposit
    def deposit(self,amount):
        self.amount = amount
        self.balance = self.balance + amount
        print("Account has been updated: £", self.balance)

    # function to withraw funds
    def withraw(self,amount):
        self.amount = amount
        if self.amount > self.balance:
            print("Invalid withraw balance available is: £", self.balance)
        else:
            self.balance = self.balance - self.amount
            print("Balance after withraw: £", self.balance)

    # function to see balance 
    def view_balance(self):
        self.show_details()
        print("Account balance: £", self.balance)



# test to verify
user = Bank("David", "34", "Male", "Doctor")
user.show_details()
user.deposit(100)
user.withraw(110)
user.view_balance()


