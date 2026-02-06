# write the program to calculate the grade of a student.

marks = int(input("Enter marks you obtained: "))
if(marks>90 and marks<=100):
    print("Your grade is A+")

elif(marks>80 and marks<=90):
    print("Your grade is A")

elif(marks>70 and marks<=80):
    print("Your grade is B+")

elif(marks>60 and marks<=70):
    print("Your grade is B")

elif(marks>50 and marks<=60):
    print("Your grade is C+")

elif(marks>40 and marks<=50):
    print("Your grade is C")

elif(marks>0 and marks<=40):
    print("Your fail.")

else:
    print("Invalid marks.")
