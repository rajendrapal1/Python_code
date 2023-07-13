from threading import Thread
# class myclass(Thread):
    
#     def __init__(self,a):
#         Thread.__init__(self)
#         print("child thread",a)
#     def child():
#        pass   

# obj=myclass(10)
# obj.start()

# print(obj)
# print("main thred")

# creating threding my child class
class myclass2():
    def fun(self,a,b):
        print("child class",a,b)
obj=myclass2()        
t=Thread(target=obj.fun,args=(10,20))  
t.start()
      
