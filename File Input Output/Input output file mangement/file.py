# f = open("file.txt")
# data = f.read()
# print(data)
# f.close()

f = open("myfile.txt","w")
f.write("Manoj gharti magar")
f.close()

f = open("morefile.txt","r")
line = f.readline()
while line !="":
    print(line,end="")
    line=f.readline()
f.close()

with open("file.txt","r") as f:
    print(f.read())