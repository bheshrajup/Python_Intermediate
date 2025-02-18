# ------------Lambda functions-------------

# general function
# def sum(x,y):
#     return x+y

# #anonymous function
# sum_lambda = lambda x,y: x+y

# print(f"10+20 using regular function sum=> {sum(10,20)}")
# print(f"10+20 using lambda function sum=> {sum_lambda(10,20)}")


# square = lambda x: x**2
# print(f"Square of 2 is :{square(2)}")

numbers = [1, 2, 3, 4]
squared_number = list(map(lambda x: x ** 2, numbers))
print(f"Squared_number are=>{squared_number}")

evenLambda=lambda x: x % 2 == 0
# evenNumbers = list(filter(lambda x: x % 2 == 0, numbers))
evenNumbers = list(filter(evenLambda, numbers))
print(f"Even numbers are=>{evenNumbers}")



