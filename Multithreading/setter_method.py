class student:
    def __init__(self) :
        self.name="raj"
    def mth(self):
        self.name="ram"
        print(self.name)
obj=student() 
obj.mth()           

# setter ,method with parmiter
class model():
    def __init__(self,name,price):
        self.name=name
        self.price=price
        
    def mth(self):
        print(self.name,self.price)
obj=model("toata",2000)
obj.mth()            