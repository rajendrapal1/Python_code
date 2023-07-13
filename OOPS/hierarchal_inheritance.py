class Father():
    def __init__(self):
        print("parent class")
    def fat_method(self):
        print("father method")

class Son(Father):
    def __init__(self):
        super().__init__()
        print("son class")
    def son_mth(self):
        print("son method")


class Child(Father):
    def __init__(self):
        super().__init__()
        print("child_class")
    def child_mth(self):
        print("child method")    

obj=Child()
obj.child_mth()
obj=Son()

