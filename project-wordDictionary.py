'''
###Problem Statement of the project
Ask user to enter a word in input
Look up for that word in the dictionary and show the meaning
'''

# ------------------Simple Word dictionary--------------------

# dictionary = {
#     "algorithm": "A step-by-step procedure to solve a problem.",
#     "variable": "A storage location identified by a memory address and an associated symbolic name.",
#     "function": "A block of reusable code that performs a specific task.",
#     "loop": "A control structure that allows repeated execution of a block of code.",
#     "dictionary": "A collection of key-value pairs in Python.",
#     "tuple": "An immutable ordered collection of elements in Python.",
#     "list": "A mutable, ordered collection of elements in Python.",
#     "string": "A sequence of characters enclosed in quotes.",
#     "integer": "A whole number without a fractional component.",
#     "float": "A number that has a decimal point or is in exponential form.",
#     "boolean": "A data type that can hold one of two values: True or False.",
#     "class": "A blueprint for creating objects in object-oriented programming.",
#     "object": "An instance of a class containing attributes and methods.",
#     "exception": "An error detected during execution that disrupts the normal flow of the program.",
#     "module": "A file containing Python code that can be imported and reused.",
#     "package": "A collection of modules organized in directories.",
#     "inheritance": "A feature in OOP where a class derives properties from another class.",
#     "recursion": "A function that calls itself in its definition.",
#     "lambda": "An anonymous function in Python.",
#     "API": "A set of functions and procedures allowing access to an application or service."
# }



#we cannot use space but can be used in above condition
dictionary = dict(
    algorithm="A step-by-step procedure to solve a problem.",
    variable="A storage location identified by a memory address and an associated symbolic name.",
    function="A block of reusable code that performs a specific task.",
    loop="A control structure that allows repeated execution of a block of code.",
    dictionary="A collection of key-value pairs in Python.",
    tuple="An immutable ordered collection of elements in Python.",
    list="A mutable, ordered collection of elements in Python.",
    string="A sequence of characters enclosed in quotes.",
    integer="A whole number without a fractional component.",
    float="A number that has a decimal point or is in exponential form.",
    boolean="A data type that can hold one of two values: True or False.",
    classes="A blueprint for creating objects in object-oriented programming.",
    object="An instance of a class containing attributes and methods.",
    exception="An error detected during execution that disrupts the normal flow of the program.",
    module="A file containing Python code that can be imported and reused.",
    package="A collection of modules organized in directories.",
    inheritance="A feature in OOP where a class derives properties from another class.",
    recursion="A function that calls itself in its definition.",
    lambdas="An anonymous function in Python.",
    API="A set of functions and procedures allowing access to an application or service."
)

# get user input
word = input("Enter the word to find the meaning=>").lower()

# look up for the user input in the dictionary
if word in dictionary:
    print(f"The meaning of {word} is=> '{dictionary[word]}'")
else:
    print(f"The word {word} doesn't exist in the dictionary")


# The drawback is that the dictionary is case sensitive
# It will give the meaning of 'lambda' but not "Lambda"
# to remove this drawback we used lower() method to convert input string into the lower case.
