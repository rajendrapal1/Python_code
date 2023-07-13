from threading import Thread
from time import sleep
class Daeman_thread(Thread):
    def __init__(self) :
        pass
    def daeman(self):

        print("this is daemanset")

obj=Daeman_thread()
t=Thread(target=obj.daeman)

print("befor set daeman=", t.isDaemon())

t.setDaemon(True)
print("after set_daemanset=",t.isDaemon())

t.start()

