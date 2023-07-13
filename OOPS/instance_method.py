class abc:
    def __init__(self,name,roll) -> None:
       #instance variable     
        self.name=name
        self.roll=roll
    def method_1(self): # instance method
        print(self.name,self.roll)
obj=abc('raj',1)
obj.method_1()  
