from abc import ABC ,abstractmethod

class collage(ABC):
    @abstractmethod             # inter face method we can not create object and we can not make concreat method
    def department1(self):
        pass

    @abstractmethod   #inter_facemethod
    def department2(self):
        pass

class school1(collage):
    def department1(self):
        print("bachaler of application")

class school2(school1):
    def department2(self):
        print("master of computer application")

# obj=school2()
# obj.department2()
obj1=school2()
obj1.department2()



