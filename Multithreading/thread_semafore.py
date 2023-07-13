#using shemaphore method

from threading import *

class Ticut():
    def __init__(self,available_sheet):
        self.available_sheet=available_sheet

        self.l=Semaphore(1)

    def sheet(self,needsheet): 

        self.l.acquire()

        print("availabesheet=",self.available_sheet)
        if needsheet<=self.available_sheet:
            name=current_thread().name
            print(f'{needsheet} sheat are book  {name}')
            self.available_sheet-= needsheet
        else:
            print("all seat are alloted")   


        self.l.release()     

obj1=Ticut(1)
obj2=Ticut(2)
obj3=Ticut(4)
t1=Thread(target=obj1.sheet,args=(1,), name='raj')
t2=Thread(target=obj2.sheet,args=(2,),name='ram')
t3=Thread(target=obj3.sheet,args=(3,),name='ram')

t1.start()
t2.start()
t3.start()




