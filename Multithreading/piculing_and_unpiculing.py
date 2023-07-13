import pickle

class prical_module():
    def __init__(self,name,roll,sity):
        self.name=name
        self.roll=roll
        self.sity=sity
    def mth(self):
        print(f'{self.name},roll_number={self.roll},student_sity={self.sity}')

#pickling to consvert class object to bite string (dump method) and import pickl module
with open("stu.dat",mode="wb") as f:
    obj=prical_module("raj",1,'surat')
    pickle.dump(obj,f)


# unpickling
# unpicaling bite string to convert class object.(use load method for read data)
with open('stu.dat', mode="rb")as f:
    ob=pickle.load(f)
    ob.mth()
 


