from threading import *
class Ticut():
    def __init__(self,available):
        self.available=available

        self.l=Lock()  # lock method and run synchronizationaly other thread are not working  till when this thread are not release.this lock are releas
                       # then work on this method 
    
    def mth_book_ticut(self,need_ticut):
        self.l.acquire()  # acquire method are lockd  in side code
        print("available ticut=",self.available)
        if need_ticut<=self.available:
            name=current_thread().name
            print(f"{need_ticut} ticut is book name is = {name}")
        else:
            print("seat are not impaty")
        self.l.release() # release method coad are release.

obj=Ticut(2)
t1=Thread(target=obj.mth_book_ticut,args=(1,),name="raj")
t2=Thread(target=obj.mth_book_ticut,args=(2,),name="aman")
t3=Thread(target=obj.mth_book_ticut,args=(3,),name="ram")
t1.start()

t2.start()

t3.start()            

