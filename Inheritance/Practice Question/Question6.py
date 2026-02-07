# Override the __len__() method on vector of problem 5 to display the dimention of the vector. 

class complex:
    def __init__(self,x,y):
        self.real = x
        self.img =  y

    def display(self):
        print(f"The complex number is {self.real} + {self.img}i")

    def __len__(self):
        return 2

    



c1 = complex(1,4)
c1.display()
print(len(c1))
