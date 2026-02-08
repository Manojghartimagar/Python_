try:
    a = int(input("Enter your age: "))
    

except Exception as e:
    print("e")
    print(e)

else:
    print(a)
    print("Thank You!")