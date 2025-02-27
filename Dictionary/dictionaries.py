# ..................Dictionary.............#
# A dictionary is a collection of key-value pairs.
# Each key is connected to a value, and you can use a key to access the value associated with that key.
# A key’s value can be a number, a string, a list, or even another dictionary.
# In fact, you can use any object that you can create in Python as a value in a dictionary.
# In Python, a dictionary is wrapped in braces, {}, with
# a series of key-value pairs inside the braces, as shown in the earlier example:
# alien_0 = {'color': 'green', 'points': 5}
# A key-value pair is a set of values associated with each other.
# When you provide a key, Python returns the value associated with that key.
# Every key is connected to its value by a colon, and individual key-value pairs are separated by commas.


# set
person = {
    "John",
    "Doe",
    23,
}

# Set type because no key-value pair
print(f"Type of person is: {type(person)}")

# Dictionary
Aperson = {
    "first_name": "John",
    "last_name": "Doe",
    "age": 23,
    "jobs":["Software Engineer","Teacher"],
    # "job": "Teacher"  # Duplicate key will be overwritten
}
# Dictionary type because key-value pair
print(f"Type of Aperson is: {type(Aperson)}")
print(f"Person is:{Aperson}")

print(f"--------------Access to dictionary items-----------------")

first_name = Aperson["first_name"]
print(f"First name is{first_name}")
print(f"First name is {Aperson['first_name']}")

lastName = Aperson.get("last_name")
print(f"Last name is {lastName}")
print(f"Jobs are {Aperson['jobs']}")

print(f"------Access to key in a dictionary-------")
print(f"The person's keys are: {Aperson.keys()}")
print(f"The person's values are: {Aperson.values()}")

Aperson["grade"] = "Master" #Add value to the dictionary
print(f"The person's keys are: {Aperson.keys()}")
print(f"The person's values are: {Aperson.values()}")
print(f"The person's items are: {Aperson.items()}") #gives the key value pair output

Aperson["age"]=20 #update
print(f"After changing the value of age=>{Aperson}")

Aperson.update({"height":170}) #add
print(f"After adding height=>{Aperson}")

Aperson.update({"age":21}) #update
print(f"After updating the age=>{Aperson}")

#Updating multiple key-value at once using comma
Aperson.update({"first_name":"Bheshraj","last_name":"Upadhyaya"})
print(f"After updating the first and last name at once=> {Aperson}")

Aperson["age"]=15 #update

if Aperson["age"]>12 and Aperson["age"]<20:
    print(f"The data of a person is a teenager")

if Aperson["height"]>100:
    print(f"The person is tall")

# print(f"Using a keyname that is not present=>{Aperson.get("hairColor","blue")}")

print(f"--------------Check for existence of key name---------------")

if "points" in Aperson:
    print(f"The point key exists")
else:
    print(f"The point key doesn't exist")



# person2 = dict(
#     first_name="John",
#     last_name="Doe",
#     age=23,
#     job="Software Engineer",)
# # job="Teacher" )#Duplicate key will not allowed

# # Dictionary type because key-value pair
# print(f"Type of Aperson is: {type(person2)}")
# print(f"Person is:{[person2]}")
# # cannot use number for key
# # 10="Ten" #SyntaxError: can't assign to literal
# # underscore is allowed
# # _10="Ten" #No error


