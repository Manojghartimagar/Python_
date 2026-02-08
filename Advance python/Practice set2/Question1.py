# Write a program to input name, marks and phone number of a student and format it using the format functiion like below:
# "The name of the student is Harry his marks are 27 and phone number is 9876896530"

def format(name,marks,number):
    return "The name of the student is {} His marks are {} and Phone number is {}".format(name,marks,number)

print(format("Manoj",90,9087654390))