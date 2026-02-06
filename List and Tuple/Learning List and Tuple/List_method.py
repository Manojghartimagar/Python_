list = ["Manoj","Mango",47,45.65,True]
list.append(2) #list method does not return new list but string always return new string and append used to add datatype in last of the list

print(list)

l = [1,2,3,4,8,1,5]
l.sort()
print(l)

print(l.count(1))

print(l.index(2))

l.insert(1,0)
print(l)

print(l.pop())

l.remove(5)
print(l)

l.reverse()
print(l)

l.extend([12,34,45])
print(l)

newlist = list.copy()
print(newlist)

(l.extend(list))
print(l)

l.reverse()
print(l)

l.clear()
print(l)