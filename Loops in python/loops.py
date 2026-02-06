# for loop
for i in range(9): # i=0 i<9 i++
    print(i)

for i in range(1,9,2): # i=1 i<9 i+=2
    print(i)

i = 1
while i<9:      # i=0 i<9 i++
    print(i)
    i+=1

l = [1,2,3,6,78,9,20]
for i in l:
    print(i)

T = (2,"manoj",8.09,"hello")
for i in T:
    print(i)

str = "I am Manoj"
for i in str:
    print(i)

list = [1,2,7,10,30]
for i in list:
    print(i)
else:
    print('done')

for i in range(11):
    if(i%2 == 0):
        continue
    print(i)

for i in range(11):
    if (i%2 !=0):
        break
    print(i)

for i in range(1,11):
    pass

for i in range(10,0,-1):
    print(i)