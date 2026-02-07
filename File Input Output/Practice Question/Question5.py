# Write a program to find out the line number where python is present in paragraph.

with open("Python.txt","r") as f:
    count = 1
    line = f.readline().lower()
    while(line != ""):
        if("python" in line):
            print("Python present in Line ",count)
        count+=1
        line = f.readline().lower()