# ------------Word Frequency--------------

# user input
sentence = input("Enter the sentence=> ").lower().split()


# dictionary to store words
word_count = {}

for word in sentence:
    # if word in word_count:
    word_count[word] = 1+word_count.get(word,0)
# print(f"Word count=>{word_count}")

print(f"----------Word frequency------------")

for word, count in word_count.items():
    print(f"No. of {word} in given sentence is {count}")