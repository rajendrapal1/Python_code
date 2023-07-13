from threading import Thread
from queue import Queue 
from time import sleep
class producer:
    def __init__(self):
        self.q=Queue()

    def   Produce(self):

        for i in range(1,5):
            print("items producer=",i)
            self.q.put(i)     
            sleep(1)
            print(self.q)
            
                
            print("producer")

class cunsumer:
    def __init__(self,pro):
        self.pro=pro
        

    def consume(self):
        for i in range(1,5):
            print("get the data=",self.pro.q.get(i))

            
obj1=producer()
obj2=cunsumer(obj1)

t1=Thread(target=obj1.Produce)
t2=Thread(target=obj2 .consume)



t1.start()
t2.start()
       



