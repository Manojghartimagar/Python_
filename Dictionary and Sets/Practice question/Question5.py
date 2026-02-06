# Create an empty dictionary. Allow 4 friends to enter their favourite language as values and use key an their names . Assume that the names are unique
dic = {}
i = 0
while i<4:
    name = input("Enter your name: ")
    language = input("Enter your favourite language: ")
    dic.setdefault(name,language)  #Insert only if key does not already exist”
    i+=1

print(dic)