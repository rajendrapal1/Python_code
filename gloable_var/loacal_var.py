#loacle variable
a=10               #  gloable variable we can use in side function and out side function any where.
def fun():
    x=20                   # loacle var we can not use out side the function.
    print("loacal var",x)

    #print("gloable_var=",a)
    a=0 
    a=a+1   # loacal variable name and gloable variable name not be same name becouse a triet as loacal variable. we will get error

   
    print(a)
obj=fun()    
# of


name="state bank"
def fun():
    emp_name="rk"
    
    name=name  # golable variable we can not assine same varable name inside function 
    print(emp_name)
    print(name)

obj=fun()

#loacle variable
def fun():
    a=10
    b=90
    print|(a)
    print(b)
def fun1():
    print(b) # loacle varibale we can not access out side the functon (error)
obj=fun()
obj=fun1()        
