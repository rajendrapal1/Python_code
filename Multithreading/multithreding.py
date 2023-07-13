from threading import Thread,current_thread

# def fun(a,b):
#     print("threding",a,b)

# t=Thread(target=fun,args=(11,22))
# t.start()

# def child_thred():
#     for i in range(5):
#         print("child thread=",i)

# t=Thread(target=child_thred)
# t.start()
# for j in range(5):
#     print("this is main thread=",j)



# current thread of threding
def disp():
   # print("this is ",current_thread())
     print("child thread=",current_thread().getName())
     print(current_thread().setName("set in thread current data"))
     print(current_thread().getName())   

td=Thread(target=disp,)
td.start()
#print("child chread=",current_thread())
print(current_thread().getName())
print(current_thread().setName("main thread_of_set_ data")) 
print("get current data =",current_thread().getName())   
