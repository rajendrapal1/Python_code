#property method
class Person:
    def __init__(self, name, age):
        self.name = name
        self._age = age #private  instance variable. 

    def get_age(self):
        return self._age ,self.name

    age = property(fget=get_age)  # property method access class object of properties and call method. 

obj=Person('python',22)    
print(obj.age)
print("person class end hear........................................................")
print(">>>>>>>>>>>>>>>>>>>>>>>>>>")
print("property method with @decorator start hear----------")

####################################################################################################################

#property method decorator method

class circle():
    def __init__(self,name,roll):
        self .name=name
        self.roll=roll
    
    @property           # property is pree difine method take the method as a argument modify method return it.
    def mthd(self):
        return (f"student_name= {self.name}   student_roll= {self.roll}")    

obj=circle('raj',1)

print(obj.mthd)




