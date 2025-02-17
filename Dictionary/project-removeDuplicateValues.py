# ------------Remove duplicate values in a directory--------------

my_dict = {
    "a": 1,
    "b": 2,
    "c": 3,
    "d": 1
}
print(f"My dict is :{my_dict}")

#create a new dictionary variable
new_dict={}

#Loop through each item in my_dict
for key,value in my_dict.items():
    #check for existence of a value in the new_dict
    if value not in new_dict.values():
        new_dict[key]=value #add item to new_dict
print(f"New dict is=>{new_dict}")