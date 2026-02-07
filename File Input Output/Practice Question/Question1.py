#Write a program to read the text from a given file 'poems.txt' and find out whether file contains the word "twinkle".

with open("poems.txt","r") as f:
    poems = f.read()
    if("twinkle" in poems):
        print("Twinkle word present in poems.")
    else:
        print("Twinkle word do not present in poems.")