# Write a program to input eight numbers from the user and display all the unique numbers(once).
s = set()
i = 0
while i<8:
    num = int(input(f"Enter {i+1} number: "))
    s.add(num)
    i+=1
print(s)