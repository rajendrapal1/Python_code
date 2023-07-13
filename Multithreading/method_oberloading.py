class father():
    def fun(self,a=None,b=None,c=None):
        if (a!=None and b!=None and c!=None):
            s=a+b+c
        elif  (a!=None and b!=None):
            s=a+b
                 
        return s    

obj=father()
print(obj.fun(10,20,30))
print(obj.fun(10,20))
