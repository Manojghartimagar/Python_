#Write a program to store seven fruits in a ist entered by the user.
fruits = []
for i in range(7):
    fruit = input(f"Enter fruit {i+1} name: ")
    fruits.append(fruit)
print(f"Your list is:\n{fruits}")
