#possional arg 
def fun(a,b):
    c=a+b
    print(c)
obj=fun(10,20)    # number are agumetn must be importent 

#keyword argument

#  arder are not importent but number are argumet must be importent
def fun(a,b):
    c=a+b
    print(c)
obj=fun(b=10,a=20)    

# variable lenth argument

def fun(*n):
    total=0
    for i in n:
        print(i)
obj=fun(10,20,30,40)   

#keyword lenth argument
def fun(**n):
    
    for k,i  in n.items():
        
        print(f'{k},{i}')
obj=fun(a=2,b=4,c=5,d=8)        

# difalt argument
 
def fun(a="raj", b=9):
    print(f"{a},{b}")
obj=fun(a=10,b=10)
print(obj)

# or number of  argument must be  importent but order are not importent 
def fun(name="raj",city="surat"):
    print(f"{city},{name}")

obj=fun(name="ram",city="payagraj")