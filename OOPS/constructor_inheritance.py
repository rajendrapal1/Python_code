class Father():

    def __init__(self) :
        self.sal=2000
        print(self.sal)

    def show(self):
        self.name="rak"
        self.price=4000 
        print(self.name,self.price)

class child(Father):
    def child_mth(self):
        self.child_name="ram"
        print(self.child_name) 

# obj=child()                  
# obj.show()
# obj.child_mth()


#pairamiter in constructor inheritance
class Father():
    def __init__(self,n):
        self.n=n
        print(self.n)

    def mth(self):
        self.fee=1000
        print(self.fee)
class son(Father):
    def mth_of_son(self):
        print("son of method")
obj=son('raj')      
obj.mth()
              