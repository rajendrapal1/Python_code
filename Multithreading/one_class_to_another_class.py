class Student_1():
    def __init__(self,name,roll):
        self.name=name
        self.roll=roll
    
    def Mthode_1(self):
        print(self.name,self.roll) 
    
#PASS VALUES ONE CLASS TO AN  OTHER CLASS
class student_2():
    @staticmethod
    def mth_static(value):
        print(value.name,value.roll)
        value.Mthode_1()
        
     


obj=Student_1('raj',1)
student_2.mth_static(obj)   




