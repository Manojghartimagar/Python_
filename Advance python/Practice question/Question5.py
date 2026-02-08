# Write a program to open there files 1.txt, 2.txt and 3.txt .If any of these files are present a message without exiting the progrm must be printed prompying the same.

files = ["1.txt", "2.txt", "3.txt"]

for file in files:
    try:
        f = open(file, "r")
        print(f"{file} opened successfully")
        f.close()

    except FileNotFoundError:
        print(f"{file} is not present")
