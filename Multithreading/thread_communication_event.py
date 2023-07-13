from threading import Thread,Event
from time import sleep

def Signal():
    sleep (1)
    e.set()  #  IF SET METHOD ARE TRUE THEN WAIT METHOD GET UNBLOCK

    print(" signal is green..")
    sleep(6)

    print("signal is red you can not go")
    e.clear()


def Traific():    
    e.wait() # set unblock this method 
    while e.is_set(): # is_set return true 
       print("YOU CAN GO NOW ............")
       sleep(1)
    print("program is done")    


t1=Thread(target=Signal)
t2=Thread(target=Traific)
e=Event()   
t1.start()
t2.start()
   

