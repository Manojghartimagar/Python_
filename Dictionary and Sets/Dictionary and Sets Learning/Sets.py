s = set()     #mutable no iteams dublicate
print(type(s)) #property of set isf unordered unindexed no way to change iteams 

set = {1,2 ,3,4,6,8,9,10}
set.add(68)
print(set)
print(len(set))

set.remove(4) #erroe gives
set.discard(4) #no error gives


print(set)
print(set.pop())

print(set.union({1,2,3}))
print(set.intersection({1,2,3,4}))

set.clear()

#a.subset(b)
#b.superset(a)