import random

# Read in all the words in one go
with open("input.txt") as f:
    words = f.read()

# TODO: analyze which words can follow other words
# Your code here
ht = {}
print(str(words))
words = str(words).split(" ")
for word in words:
    print(word)

# TODO: construct 5 random sentences
# Your code here

