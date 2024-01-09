class Dog (object):
    def __init__(self, name, age): #constructor
        self.name = name
        self.age=age
    def speak (self):
        print("Hi I'm", self.name, "and I am", self.age, "years old!")
    def change_age(self, age):
        self.age = age
    def add_weight(self, weight):
        self.weight = weight
    

anderson = Dog('Anderson', 35)
fred = Dog("Fred", 5)
anderson.change_age(3)
anderson.add_weight(input("What's your weight? "))

anderson.speak()
fred.speak()

print(anderson.age) #to access an instance, just call that parameter
print(anderson.weight)