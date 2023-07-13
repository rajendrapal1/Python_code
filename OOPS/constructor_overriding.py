class student():
    def __init__(self):
        self.st_fee=1000
        print("parent constructor")
    def sho_mth(self):
        print("parent method")
class son(student):
    def __init__(self):
        print("child class constructor") 
    def chile_mth(self):
        print("this is child method")    
obj=student()        
obj=son()                   
obj.chile_mth()
obj.sho_mth()