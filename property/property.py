class student():
    def __init__(self,name ,fee):
        self.name=name
        self._fee=fee

    def set_fee(self,fee):

        if fee<1000:

            print("condition is true so raise error")
            raise ("you can not attent classs")
        self._fee=fee   
    def get_value(self):
        return self._fee
       
    st=property(fset=set_fee,fget=get_value)   
       
obj=student('raj',103)
print(student.st)
print(obj.__dict__)


#########################################
from pprint import pprint


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def set_age(self, age):
        if age <= 0:
            raise ValueError('The age must be positive')
        self._age = age

    def get_age(self):
        return self._age

    age = property(fget=get_age, fset=set_age)


print(Person.age)

john = Person('John', 18)
pprint(john.__dict__)

john.age = 19
pprint(Person.__dict__)






# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.set_age(age)

#     def set_age(self, age):
#         if age <= 0:
#             print("set classs excuted")
#             raise ValueError('The age must be positive')
#         self._age = age

#     def get_age(self):
#         return self._age
    
# john = Person('John', 18)
# john.set_age(19)



# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age


#     def set_age(self, age):
#         if age <= 0:
#             raise ValueError('The age must be positive')
#         self._age = age


#     def get_age(self):
#         return self._age

#     age = property(fget=get_age, fset=set_age)
#     print(type(age))


# print(Person.age)    
# obj=Person('raj',22)
# print("age will be print",obj.age)
# print(obj.__dict__) #       __dict__ store the instance attribute of from obj
# print(Person.__dict__)
