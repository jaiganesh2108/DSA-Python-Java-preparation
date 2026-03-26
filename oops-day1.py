class Person:
    def __init__(self, name, age=18): #default value for age is 18 if not provided
        self.name = name
        self.age = age

p1 = Person("John") #since age is not provided, it will take the default value of 18
p2 = Person("jane", 24) #since age is provided, it will take the value of 24
print(p1.name, p1.age)
print(p2.name, p2.age)