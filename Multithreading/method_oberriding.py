class Addition():
    def mth (self,a,b):
        print("add to number=",a+b)



class Subtruction(Addition):
    def mth (self,a,b):
        super().mth(10,20)  # use with supper method
        
        print("subruction=",a-b) 


obj=Subtruction()
obj.mth(10,5)       
          