'''  *
    ***
   *****  '''

n = 3
for i in range(1,n+1):
    print(" " * (n-i), end="")
    print("*" * (2*i-1))

'''
***
* *
***
'''
n = 3

for i in range(n):
    for j in range(n):
        if i == 0 or i == n-1 or j == 0 or j == n-1:
            print("*", end="")
        else:
            print(" ", end="")
    print()

