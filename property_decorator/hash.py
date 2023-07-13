class hash_cl():
    def __init__(self,name,roll) :
        self.name=name
        self.roll=roll

obj1=hash_cl('raj',1)
obj2=hash_cl('ram',2)  

print(hash(obj1))
print(hash(obj2))   



import math


class Circle:
    def __init__(self, radius):
        self.radius = radius

    @property
    def area(self):
        return math.pi * self.radius ** 2


c = Circle(10)
print(c.area)