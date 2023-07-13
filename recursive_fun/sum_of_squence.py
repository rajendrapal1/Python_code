# def fun(a):
    
#     if a>0:
#         print(a ,end=" ")
        
#     else:    
#         return a
#     fun(a-1) 

# obj=fun(10)   

#print(obj)

# even number

# def fun1(n):
#     n=n-1

#     if n>0:
#       print(n)  
#       fun1(n)   
  
# obj=fun1(100)    


# ##############
# def sum(n):

#     if n==0:
#         return 0
#     else:
#         n+=n
#         return n

#         return n +  sum(n-1)


# result = sum(100)
# print(result)

# ###################
def even(n):
    if n==0:
        return 0
    else:
        if n%2==0:
            
            
            print(n)

    return even( n-1)   
sav=0     
obj=even(10)  
         

