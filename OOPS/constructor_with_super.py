class Mobile():
    def __init__(self):
        print("parent class cunstructor")
    def pr_mthod(self):
        print("parent method")
class son(Mobile):
    def __init__(self):
        super().__init__()
        super().pr_mthod()
        print("child class constructor")
    def chi_constructor(self):
        print("child class method") 
obj=son()


# pass paramiter in a constructor
class Student1():

    def __init__(self,mony):
        self.mony=mony
        print("parent constructor=",self.mony)

class Student2(Student1):

    def __init__(self,fee):
        self.fee=fee
        super().__init__(1000)
        print("child constructor=",self.fee)        


    def chi_mth(self):
        print("this is child method")

obj=Student2(1000)                