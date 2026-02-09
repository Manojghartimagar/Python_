with open("Student.txt") as f:
    content = f.readline()
    while(content!=""):
        print(content)
        print(type(content))
        content = f.readline()