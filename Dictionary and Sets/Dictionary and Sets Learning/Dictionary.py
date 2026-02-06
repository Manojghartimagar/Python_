marks = {   #Here manoj,mahesh and krishna are used as index for dictionary marks
    "manoj":90,  #property of dictionary is unordered,mutable,indexed no dublicate key
    "Mahesh":89,
    "Krishna":88
}

print(marks["manoj"])
print(marks)
print(type(marks))
print(marks.keys())
print(marks.values())
print(marks.items())
marks.update({"manoj":99, "sita":95})#if exist key then update oderwise create new one
print(marks)

print(marks.get("manoj9",0))# print none or default value(0) if present 
#print(marks["manoj9"])# return error

print(marks.pop("manoj"))
print(marks)

print(marks.popitem())
print(marks.clear())
newmarks = marks.copy()
print(newmarks)

sub =newmarks.setdefault("books","Nepali")
print(newmarks)
print(sub)