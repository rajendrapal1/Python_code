a=10
def fun1():
    
    a=100    
    print("loacale variable access=",a)
    a=globals() ['a']
    print("gloabe variable access in side fun.. with gloabes_function=",a)
    
def fun2():
    b=200
    print(b) 

print("out side fun access_gloable_var=",a)

obj=fun1()
obj=(fun2())