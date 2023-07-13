from threading import *
from time import sleep
li=[]
def thread_condition():
    obj.acquire()
    for i in range(1,5):
        li.append (i)
        sleep(1)
        print("code will be excurte")
        print(li)
    obj.notify()    
    obj.release()

def consume():
    obj.acquire()
    obj.wait(1)
    obj.release()
    print("this is consume")


obj=Condition() 
t1=Thread(target=thread_condition)
t2=Thread(target=consume)
t1.start()
t2.start()        
  















obj=Event()    