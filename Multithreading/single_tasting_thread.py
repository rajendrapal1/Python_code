from threading import Thread
from time import sleep
class myclass():
    def fun(self):
        self.q1()
        self.q2()
        self.q3()

    def q1(self):
        print("question_1")
        sleep (3)
    def q2(self):
        print("question_2")
        sleep(3)
    def q3(self):
        
        print("question_3")            
ob=myclass()
t=Thread(target=ob.fun,)
t.start()        
print("mane thread")