class duck():
    def dock(self):
        print("duck class")
class horse():
    def dock(self):
        print("horse method")
def function_call(ob):                
    ob.dock()
ob=horse()
function_call(ob)    