
def fun(a):  # docstring we can difine function,and method we can write discription..... 
    """this is docstring is 
    in python"""
    print(a*2)
fun(10)
print(fun.__doc__)

##################
#issubset
a={1,2,3,4,5} # a set all element maching in  b set then return trur. 
b={1,2,3}
print(a.issubset(b))

#super set{}
a={2,3,4,5}
b={2,3,4} #specify element available in set a then return true.
print(a.issuperset(b))
print(a.issuperset(b))

