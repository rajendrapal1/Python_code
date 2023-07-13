class School:
    def __init__(self):
        self.name="ram"
        self.fee=100
        self.ob = self.collage() # inner class object create here

    def method_1(self):
        print(self.name,self.fee)

    class collage():
        def __init__(self) :
            self.inn_name="rajendra"
            self.fee=1000
        def mth_collage(self):
            print(self.inn_name,self.fee)

obj=School()
obj.method_1()
obj.ob.mth_collage() # call inner class method

print(obj.ob.inn_name)
print(obj.ob.fee)