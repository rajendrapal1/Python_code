from threading import Thread
class abc(Thread):
    def run(self): # run method autometicaly excuted when startmethod will be create.
        for i in range(5):
            print("child thread")
t=abc()
t.start()
t.join()        # join method if we want to print before child thread then  we are use in join
#
# this is mane thread 
for j in range(5):
    print("mane thread excute")
