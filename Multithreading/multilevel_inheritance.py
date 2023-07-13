#multilevel_inheritance

class father():
    def __init__(self) :
        print("parent class")
    def mth_father(self):
        print("father method") 

class son(father):
    def __init__(self):
        #super().__init__()        
        print("son cunstructor")
    def son_method(self):
        print("son method")    
class child(son):
    def __init__(self):
        print("child class")
    def child_method(self):
        print("child method") 

obj=child()
obj.mth_father()
obj.son_method()
obj.child_method()
                

#constructor with super method
class Father():
    def __init__(self,name) :
        self.name=name
        print("Father clss",self.name)

    def Fath_method(self):
        print("father method") 

class Son(Father):
    def __init__(self,name):
        self.name=name
        super().__init__()
        print("son constructor",self.name)

    def Son_method(self):
        print("son methd")

class Child(Son):
    def __init__(self,name):
        self.name=name
        # super().__init__()
        print("child constructor",self.name)
    def child_method(self):
        print("child method") 

obj=Child('raj')            
obj.child_method()