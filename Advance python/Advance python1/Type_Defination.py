n:int = 5             # assinged to integer
name : str = "Manoj"  # assinged to string

def sum(a : int,b : int) -> int:
    return a + b

print(f"The sum of 5 and 6 is {sum(5,6)}")



from typing import List,Tuple,Union,Dict

number: list[int] = [1,2,3,4]
print(number)

person: list[int,str] = ["Manoj",47]

print(person)

student: Dict[int,str] = {"Manoj":47,"Pappu":48}

print(student)

identifier: Union[str,int] = "345hk"
print(identifier)