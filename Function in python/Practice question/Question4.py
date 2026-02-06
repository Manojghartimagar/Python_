# Write a python function to remove a given word from a list and strip it at the same time.

words = ["Nepal","Kathmandu","India","Delhi","America","New york"]
print(words)
word = (input("Enter the word to remove: ")).capitalize()

def remove(word):
    words.remove(word)
    print(words)

remove(word)