class Model():
    def __init__(self) -> None:
        pass
    # withought argument
    @staticmethod
    def mth_1():
        print("withought argument")
# with argument
    @staticmethod 
    def mth_static(name,roll):
        nam=name
        roll=roll
        print(name,roll)

obj=Model()
obj.mth_1()
obj.mth_static('ram',12)  # we call with object name
Model.mth_static("raj",4) # we cam call with class name