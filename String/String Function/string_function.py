name = "mahesh"
print(len(name)) #count total Character
print(name.endswith("h"))
print(name.capitalize()) #Mahesh
print(name.upper().startswith("M")) #True
print(name.lower().endswith('h')) #True
print(name.center(0))
name = " Manoj "
print(name.strip())# used to remove space

string = "My name is Mahesh"
print(string.replace("Mahesh","Manoj")) #My name is Manoj

fruits = "Apple,Mango,Orange"
print(type(fruits.split()))#used to convert string into list ex ['Apple,Mango,Orange']
print("-".join(fruits)) #A-p-p-l-e-,-M-a-n-g-o-,-O-r-a-n-g-e

#find()used to find the index of string and index() used to find index of string if string not found then find returns -1 and index return error

print(string.find("name")) #3
print(string.index("name")) #3

print(string.find("z")) #-1
#print(string.index("z")) ValueError: substring not found

print(fruits.lower().count("a")) #3

s = "hello word"
print(s.capitalize())  #Hello word
print(s.title())        #Hello Word

print("123".isdigit())
print("asd123".isalnum())
print("ads".isalpha())

# important
# split()
# strip()
# replace()
# lower()/upper()
# find()
# slicing