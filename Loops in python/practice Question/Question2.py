#Write a program to greet all the person names stored in a  list l1 and which starts with S 
l1 = ["Harry","Soham","Sachin","Rahul"]
for iteam in l1:
    if((iteam.lower()).startswith("s")):
        print(f"Good Morning {iteam}")
    else:
        continue