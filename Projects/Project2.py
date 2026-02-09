# 1. Student Management System (File Based)
# Features:
# Add student (name, roll, marks)
# Update / delete student
# Search by name or roll
# Store data in text/CSV file
# Show topper
# Concepts Used:
# dictionary → store student data
# list → multiple students
# file handling → save/load
# function → add(), update(), search()

def add(n):
    if n == 0:
        noOfStudent=int(input("Enter how many student do you want to add: "))
    else:
        noOfStudent=n
    for i in range(noOfStudent):
        name = input(f"Enter name of student: ")
        roll = int(input(f"Roll no of {name}: "))
        mark = float(input(f"Marks obtained by {name}: "))
        with open("Student.txt","r") as f:
            content = f.readline()
            while content != "":
                if name.lower() in content.lower() and str(roll) in content and str(mark) in content:
                    print("Alredy exits Enter information of another student ! ")
                    add(noOfStudent-i)
                content =f.readline()

            else:
                student = {
                "name": name.capitalize(),
                "roll": roll,
                "marks":mark
                }
        
                with open("Student.txt","a") as f:
                    f.write( f"\nInformation of {name} \n")
                    f.write(str(student))
        
def update():
    choice = int(input("What do you want to update\n 1. name \n2. Roll no\n 3. Marks:"))
    match(choice):
        case 1:
            name = input("Enter new name: ")
            roll = input("Enter Roll no: ")
            mark = input("Enter Marks: ")

            
            
            count = 0
            count1 = 0
            with open("Student.txt","r") as f:
                fullcontent = f.read()

                with open("student1.txt","w") as g:
                    g.write(fullcontent)

                content = f.readline()
                while content !="":
                    count+=count
                    if roll in content:
                        break
                    content = f.readline()
                
            with open("student1.txt","r") as g:
                with open("Student.txt","w") as f:
                    c = g.readline()
                    while c != "":
                        count1+=1
                        if(count == count1 and count == count1 + 1):
                            student = {
                            "name": name.capitalize(),
                            "roll": roll,
                            "marks":mark
                            }
                            f.write( f"Information of {name} \n")
                            f.write(str(student))
                        else:
                            f.write(c)

                        


print("Which operation are you doing?")
print("1. Add\n2. Update\n3. Delete")
choice = int(input(""))

match(choice):
    case 1:
        add(0)
    case 2:
        update()
    case 3:
        delete()
    case __:
        print("Invalid Number: ")


