import math



class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2
obj=Circle(2) 
b=obj.area()
print(b)

print(obj.area())


#example=(2)=>


class calculate():
    def __init__(self,name,fee):
      self.fee=fee
      self.name=name

    @property
    def mth_fee(self):
        return self.fee + 10000 ,self.name

obj=calculate('python',2000)
ob=obj.mth_fee
print(ob)     
print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> ")
print("circle class here")
#Example-(3)




class Circle:
    def __init__(self, radius):
        self._radius = radius
        self._area = None

    @property
    def radius(self):
        return self._radius

    @radius.setter  #access the property of class instance variable and return
    def radius(self, value):
        if value < 0:
            raise ValueError('Radius must be positive')

        if value != self._radius:
            self._radius = value
            self._area = None

    @property
    def area(self):
        if self._area is None:
            self._area = math.pi * self.radius ** 2

        return self._area
    
obj=Circle(10) 
obj.radius=30
print(obj.radius)
print(obj.area) 
 

print()