class Example():
    a = 10
    def add(self, a):
        self.a = a #this will create an instance variable a that shadows the class variable a

exc = Example()
print(exc.a)
exc.add(20)
print(exc.a)