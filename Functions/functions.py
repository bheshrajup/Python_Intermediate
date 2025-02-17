# -----------Functions---------------


# Creating a function
def hello():
    print(f"Hello from hello() function!")


def showMessage(msg):
    print(msg)

# def sum(number1, number2):
#     result = number1+ number2
#     print(f"The sum of two numbers is => {result}")

# calling hello() function
hello()
showMessage("Hello from the parameter!")
x = 10
y = 10
showMessage(f"x+y={x+y}")
print(f"x+y={x+y}")

# sum(3,4)
# sum("Bheshraj","Upadhyaya")


# def sum(number1: int, number2:int): #parameterized 
#     result = number1+ number2
#     print(f"The sum of two numbers is => {result}")

# def sum(number1: int, number2:int=2): #default parameter value
#     result = number1+ number2
#     print(f"The sum of two numbers is => {result}")

def sum(number1=2, number2=3): #default parameter value
    result = number1+ number2
    print(f"The sum of two numbers is => {result}")


# sum([1,2,3],[4,5,6])
sum("Hello","world")
sum("HI","hello") 
# # sum([1,2,3],(4,5,6)) #error

sum(5)  #considered for number1, the number2 have default value
# sum() error 

#What if i want to pass value for number2 not make number1 default parameter

