#Write a program to store seven fruits in a ist entered by the user.
list = []
for i in range(0,7):
    fruit = input(f"Enter {i+1} Fruits name: ")
    list.insert(i,fruit)
print(f"Your list is\n{list}")