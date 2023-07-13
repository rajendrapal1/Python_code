# class collage():
#     def __init__(self,name,fee):
#         self.name=name
#         self.fee=fee
  
#     def set_method(self,fee): 

#         if self.fee<100:
#             print("you can give the exam..=",)

#         self. fee=fee

#     def get_method(self):
#         return self.fee
    
#     sav_data=property(fget=get_method,fset=set_method)

    
# obj=collage('rajendra',100)
# obj.set_method(200)
# print(obj.fee)
# print(obj.__dict__)

print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
# using decorator function

class Student():
    def __init__(self,name,roll,mark):
        self .name=name
        self.roll=roll
        self.mark=mark

    
    def set_mth(self,name):
        if name=="raj":
            print("you are student of iics collage")
        self.name=name    
    
    @property
    def get_method(self):
        return self.name
    
    @property
    def get_matks(self):
        return self.mark

obj=Student('rajendra',1,90)
obj.set_mth('raj')
print(obj.get_method)
print(obj.get_matks)


print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> example=2")
#example (2)>

class Person:
    def __init__(self, name, age):
        self.name = name
        self._age = age

    @property
    def age(self):
        return self._age

    @age.setter  #The setter() method accepts  a callable and returns another callable (a property object).
    def set_age(self, value):
        if value <= 10:
            raise ValueError('The age must be positive')
        self._age = value
    
obj=Person('python',22)
b=obj.age
print(b)
obj.set_age=23
b=obj.age
print(b)
obj.set_age=200
print(obj.age)

    