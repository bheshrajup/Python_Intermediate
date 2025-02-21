# # # ---------Classes in python------------
# # class Student:
# #     name = "John"  # attribute

# #     def __init__(self, name):
# #         self.name=name


# # student1 = Student("Samir")  # create an object
# # # student2 = Student()  # create another object

# # print(f"student1.name=>{student1.name}")

# # numbers = [1, 2, 3]
# # numbers.pop(1)
# # print(numbers)


# class Car:
#     def __init__(self, model, year):
#         self.model = model
#         self.year = year

#     def displayInfo(self): #self can be written as anything here self it works as self
#         print(f"The car is {self.model} {self.year}")


# myCar = Car("Corolla", 2022)
# # print(f"My car is=> {myCar.model} {myCar.year}")
# myCar.displayInfo()

# yourCar=Car("Mustang",2025)
# yourCar.displayInfo()

class Person:
    def __init__(self,name,age):
        self.name=name
        self.age =age

    def greet(self):
        print(f"Hi, I am {self.name} and I am {self.age} years old.")


person1 = Person("John",22)
person1.greet()

person2 = Person("James",25)
person2.greet()

print(f"####After changing the person1 name value####")

person1.name="Roy"
person1.greet()

person2.greet()