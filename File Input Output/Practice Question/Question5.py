# Write a program to find out the line number where python is present in paragraph.

# Program to find the line numbers where "python" is present

with open("Python.txt", "r") as f:
    for count, line in enumerate(f, start=1):
        if "python" in line.lower():
            print("Python present in Line", count)

