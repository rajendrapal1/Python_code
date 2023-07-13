#using class with paramiter

from threading import Thread ,current_thread
class Ticut():
    def __init__(self,available_sheet):
        self.available_sheet=available_sheet


    def sheet(self,needsheet): 
        print("availabesheet=",self.available_sheet)


        if needsheet<=self.available_sheet:
            name=current_thread().name
            print(f'{needsheet} sheat are book  {name}')
            self.available_sheet-= needsheet
        else:
            print("all seat are alloted")    

obj1=Ticut(1)
obj2=Ticut(2)
t1=Thread(target=obj1.sheet,args=(1,), name='raj')
t2=Thread(target=obj2.sheet,args=(3,),name='ram')
t2.start()
t1.start()




