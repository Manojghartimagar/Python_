# Write a program to find out the line number where python is present in paragraph.

with open("Python.txt","r") as f:
    count = 1
    line = f.readline()
    while(line != ""):
        if("python" in line.lower()):
            print("Python present in Line\n",count)
            count+=1
            line = f.readline()
        else:
            line = f.readline()
