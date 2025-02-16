#  Dictionary
Aperson = {
    "first_name": "John",
    "last_name": "Doe",
    "age": 23,
    "jobs": ["Software Engineer", "Teacher"],
    # "job": "Teacher"  # Duplicate key will be overwritten
}
# Dictionary type because key-value pair
print(f"Type of Aperson is: {type(Aperson)}")
print(f"Person is:{Aperson}")

# print(f"---------Copy in dictionary---------")
# person = Aperson
# print(f"Other person is also:{person}")

# print(f"---------After changing first name in Aperson---------")
# Aperson["first_name"]="Bheshraj"
# print(f"Person is:{Aperson}")
# print(f"Other person is also:{person}")
# #the first name is changed in both....copied

# print(f"---------After changing first name in person---------")
# person["first_name"]="Achinaru"
# print(f"Person is:{person}")
# print(f"Other person is also:{Aperson}")
# #the first name is changed in both...copied


# person = Aperson.copy()
# print(f"Other person is also:{person}")


# print(f"---------After changing first name in Aperson---------")
# Aperson["first_name"]="Bheshraj"
# print(f"Person is:{Aperson}")
# print(f"Other person is also:{person}")
# #the first name is not changed in new variable....


# print(f"---------After changing first name in person---------")
# person["first_name"]="Achinaru"
# print(f"Person is:{person}")
# print(f"Other person is also:{Aperson}")
# #the first name is not changed in both...


# person = dict(Aperson)
# print(f"Other person is also:{person}")


# print(f"---------After changing first name in Aperson---------")
# Aperson["first_name"]="Bheshraj"
# print(f"Person is:{Aperson}")
# print(f"Other person is also:{person}")


print(f"---------------Loops in dictionary------------------")
print("--------All the key in Aperson dictionary--------------")
for k in Aperson:
    print(k)

print("--------All the key using keys method--------------")

for k in Aperson.keys():
    print(k)


print(f"----------All the value in Aperson dictionary---------")

for k in Aperson:
    print(Aperson[k])

print("--------All the values using values method--------------")

for k in Aperson.values():
    print(k)


print("--------All the key-values using items method--------------")

for k in Aperson.items():
    print(k)
print("---All the key-values using items method in formatted method---")

for k,v in Aperson.items():
    print(k,v)