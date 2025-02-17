# -----------Functions---------------


# Creating a function
def hello():
    print(f"Hello from hello() function!")


def showMessage(msg):
    print(msg)

def sum(number1, number2):
    result = number1+ number2
    print(f"The sum of two numbers is => {result}")

# calling hello() function
hello()
showMessage("Hello from the parameter!")
x = 10
y = 10
showMessage(f"x+y={x+y}")
print(f"x+y={x+y}")

sum(3,4)
sum("Bheshraj","Upadhyaya")