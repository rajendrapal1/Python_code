# #abstract class difine behabior of an other class and we can not creat an object .

from  abc import ABC,abstractclassmethod
class Father (ABC):
    @abstractclassmethod
    def fun(self):
        pass
    def mth(self,a,b):
        self.a=a
        self.b=b
        print("add to number=",a+b)
        print("concreat method")


class child(Father):
    def fun(self):
        print("child class")
        print("difine abstruct class")
    
obj=child()
obj.fun()  
obj.mth(10,20)



####################
from abc import ABC,abstractmethod
class Collage(ABC):
    @abstractmethod
    def library(self):
        pass
    def concreat_mth(self):
        print(" library of collage")

class Depart_ment(Collage):
    def library(self):
        print("department") 

class Mca_department(Collage):
    def library(self):
        print("mca department")

class Bca(Collage):
    def library(self):
        print("bca department")

obj=Depart_ment()
obj.library()     
obj.concreat_mth() 
obj2=Mca_department()
obj2.library()
obj2.concreat_mth()
obj3=Bca()
obj3.library()
obj3.concreat_mth()
                  

