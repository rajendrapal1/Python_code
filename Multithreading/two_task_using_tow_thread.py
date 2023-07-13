from threading import Thread
class Hotel():
    def __init__(self,t):
        self.t=t
    def fun(self):
        for i in range(5):
         
         print("take order=",self.t,i)
obj1=Hotel("take oreder of customers")
obj2=Hotel("serve order of customer")

t1=Thread(target=obj1.fun())
t2=Thread(target=obj2.fun,)
t1.start()
t2.start()





