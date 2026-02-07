class student:
    a = 1

    @classmethod #used to show only class attribute value instead of inatence value (s.a = 45)
    def show(self):
        print(f"The class value is {self.a}")

s = student()
s.a = 45
s.show()