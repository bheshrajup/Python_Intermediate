#---------Character Frequency-------------

sentence = input("Enter the sentence=>").lower()

char_count={}

for char in sentence:
    if char.isalpha(): #check if character is a letter
        char_count[char]=1+char_count.get(char,0)


for char,count in char_count.items():
    print(f"'{char}':{count}")