class student:
    name = "Manoj"
    Language  = "English"
    Level = "Bachelor"

s = student()
s.address = "Rolpa"
print(s.name,s.Language,s.Level,s.address)
  
#Here address is object(instance) attribute and name,languare level is class atributes.
s.name = "Rohan"
print(s.name)  #object(instance) attribute > priority than class attribute.