#--------Recursion--------

#Factorial => 3! = 3*2*1 (factorial is only for integer)
# n!= n*(n-1)

def factorial(n): #regular function
    result = 1
    
    for i in range(1,n+1): #0 to n and 1 to n+1 is same
        # result=result*i
        result*=i 
    return result

def recursive_function(number):
    #n!=n*(n-1)*(n-2)*..........*2*1
    if (number==0):
        return 1
    return number*recursive_function(number-1)


num = int(input("Please enter a number:"))
print(f"{num}! is {factorial(num)}")
print(f"{num}! is {recursive_function(num)}")


