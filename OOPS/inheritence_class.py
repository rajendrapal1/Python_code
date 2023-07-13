class Father():
    a=5000
    def mthe(self):
        self.name="raj"
    @classmethod
    def mth_class(cls):
        print(cls.a)
    def show(self):
        self.mony=1000
        print("parent properties",self.mony)

    @staticmethod
    def mth_static():
        a=8000
        print("static method",a)


class son(Father):
    def show_son(self):
        self.many=2000
        print("son propertiese",self.many)

obj=son()
obj.show_son()
obj.show()
obj.mthe()
obj.mth_class() 
#call with class name
son.mth_class()
obj.mth_static()


