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

print(f"-----------Using pop method---------------")
Aperson.pop("jobs") 
print(f"Person is:{Aperson}")

# Aperson.pop("Age") 
# print(f"Person is:{Aperson}") #error due to case-sensitive

print(f"-----------Adding an item---------------")

Aperson["points"]=10.5
print(f"Person is:{Aperson}")

print(f"-----------Using popitem method---------------")

Aperson.popitem() #no need to specify key....it will remove the last added item
print(f"Person is:{Aperson}")

# print(f"-----------Using del keyword---------------")
# del Aperson["age"]
# print(f"Person is:{Aperson}") #age is removed

# print(f"-----------Using del keyword without key name---------------")
# del Aperson #this will remove the whole dictionary
# print(f"Person is:{Aperson}") #it will not print because the dictionary variable is already removed

print(f"-----------Using clear method---------------")
Aperson.clear() #this will clear the key value inside the dictionary
print(f"Person is:{Aperson}") #empty 




