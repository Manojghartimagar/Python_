a = (1,2,3,4,5,"Manoj","Mango") 
print(a.count(5))
print(a.index(4))
print(a[:7:2])
print(len(a))
b = (6,7,8)
print(a + b) #(1, 2, 3, 4, 5, 'Manoj', 'Mango', 6, 7, 8)
print(b * 3) #(6, 7, 8, 6, 7, 8, 6, 7, 8)
print(6 in b) #True