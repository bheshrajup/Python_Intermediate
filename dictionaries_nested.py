# ---------------Nested Dictionary----------------

# people = {
#     # "count": 2,

#     # a key will act as dictionary inside the dictionary
#     "person1": {
#         "name": "John",
#         "age": 25
#     },
#     "person2": {
#         "name": "David",
#         "age": 21
#     },
# }

##### Defining each dictionary and nesting them inside main dictionary
person1 = {
    "name": "John",
    "age": 25
}
person2 = {
    "name": "David",
    "age": 21
}
people = {
    "person1": person1,
    "person2": person2
}

print(f"People are:{people}")

# ----Accessing the value of nested dictionaries---
print(f"{people['person1']}")
print(f"{people['person2']}")

# --Accesing inside the nested dictionaries--
print(f"Person1 name is=> {people['person1']['name']}")
print(f"Person2 name is=> {people['person2']['name']}")


# Loops in nested dictionaries
print(f"------Show Items------")
for k, item in people.items():
    # print(k)
    # print(item)
    print(f"{k}:{item}")


