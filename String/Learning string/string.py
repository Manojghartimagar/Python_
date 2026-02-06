name = "Manoj"      #way to write string and string is immutable
address = 'Rolpa'
school = '''Jana sewa'''

#slice the string
 
nameShort = name[0:4] # 0 to 3 not include 4 index string 
nameShort2 = name[-5:-1] # -5 to -1 not include -1 index string where -5 equvalent to 0and -1 to 4

print(nameShort)
print(nameShort2)

#Slicing with skip value
word = "Kathmandu"
word1 = word[0:9:4] # skip 3 character n-1
print(word1)
print(word[:9]) #[:9] = [0:9]
print(word[0:]) # [0:]= [0:9]
