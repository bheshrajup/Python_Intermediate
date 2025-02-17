# -----------------Merging dictionaries-------------


# Dictionary1
dict1 = {
    "a": 1,
    "b": 2,
    "c": 3
}

# Dictionary2
dict2 = {
    "a": 3,
    "d": 5,
    "e": 6,
    "f": 7
}

# What happen if two dictionary have same key ...what will happen after merging
print(f"-------Before merging---------")
print(f"Dict1 is=>{dict1}")
print(f"Dict2 is=>{dict2}")

# #Let's merge dict2 into dict1
# dict1.update(dict2)

# print(f"-------After merging dict2 into dict 1---------")
# print(f"Dict1 is=>{dict1}")
# print(f"Dict2 is=>{dict2}")


#This will change value of either dict1 and dict2 and the changed value will be used further
# Let's merge dict1 into dict2
# dict2.update(dict1)

# print(f"-------After merging dict2 into dict 2---------")
# print(f"Dict1 is=>{dict1}")
# print(f"Dict2 is=>{dict2}")

# merged_dict = {**dict1,**dict2} #dict2 is merged into dict1
# print(f"Merged dict is=>{merged_dict}")

merged_dict = {**dict2,**dict1} #dict1 is merged into dict2
print(f"Merged dict is=>{merged_dict}")
#The value of dict1 and dict2 is not changed
print(f"Dict1 is=>{dict1}")
print(f"Dict2 is=>{dict2}")


'''
#Merging dictionary applications
-Combining configuration settings
-Aggregating API responses
-Merging Inventory data
-Combining user permissions
-Logging system data
-Machine learning models
'''