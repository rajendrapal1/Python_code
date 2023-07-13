class father():
    def __init__(self) :
        super().__init__()
        print("father class constructor")
    def mthF(self):
        print("father class method")


class mother():
    def __init__(self):
        super().__init__()
        print("mother class constructor")
    def mthM(self):
        print("mother class method")   

class child(father,mother):
    def __init__(self):
        super().__init__()
        print("child classs constructor")
    def mthC():
        print("child method")
        
obj=child()
obj.mthF()    
obj.mthM()     