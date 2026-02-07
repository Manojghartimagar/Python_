# Write a program to generate multiplication tables from 2 to 20 and write it to the different files.txt there files in  a folder for a 13 year old.

age = int(input("Enter your age: "))

if age >= 13:
    with open("Multiplication.txt", "a") as g:

        for i in range(2, 21):
            g.write(f"\n==== Table of {i} ====\n")

            for j in range(1, 11):
                g.write(f"{i} * {j} = {i*j}\n")

    print("Multiplication tables saved successfully!")

else:
    print("You are not eligible.")
