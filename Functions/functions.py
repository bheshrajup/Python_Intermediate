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

def sum(number1=2, number2=3):  # default parameter value
    result = number1 + number2
    print(f"The sum of two numbers is => {result}")


def subtract(number1=2, number2=3):  # default parameter value
    result = number1 - number2
    print(f"The difference of two numbers is => {result}")


def showValues(*values):  # Arbitary arguments(*args)
    for item in values:
        print(item)


def showKeywordValues(**kwargs):  # Arbitary keyword arguments
    for item in kwargs.items():
        print(item)


# sum([1,2,3],[4,5,6])
sum("Hello", "world")
sum("HI", "hello")
# # sum([1,2,3],(4,5,6)) #error

sum(5)  # considered for number1, the number2 have default value
# sum() error

# What if i want to pass value for number2 not make number1 default parameter
# sum(4) want to use 4 for number2
sum(number2=4)  # keyword(named) arguments are used(kwargs)

subtract()
subtract(5, 6)
subtract(number1=30, number2=10)

showValues(1, 2, 2, 4, 5, 6, 7, 8)
showValues("hello", "friend", 1, 2, 3, 4)


showKeywordValues(name="John", age=20, job="Student")
showKeywordValues()

showValues()