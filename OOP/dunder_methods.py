#-------Dunder method---------

class Person:
    def __init__(self,name,age):
        self.name=name
        self.age =age

    def greet(self):
        print(f"Hi, I am {self.name} and I am {self.age} years old.")
    
    def __str__(self):
        return f"{self.name} is {self.age} years old"

person1 = Person("David",20)
print(f"Person1 is = '{person1}'")