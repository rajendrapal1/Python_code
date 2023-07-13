# # Gloable variable
# a=10
# def fun():
#     a=0    # now treated as a loacale variable code will be excute .for this situation we are gloable keyword
#     a=a+20
#     b=90
#     print(a)
#     print(b)
# obj=fun()
# print("*****************")
# ###########################
# a=100
# def fun():
#     global a
#     a=a+1
#     print(a)
# obj=fun()    
# print("***************")
############################

a=10
def fun():
    global a
    a=a
    while(a>0):
        
        
        print(a)

        a=a-1   # gloable variable we can not assigne same variable name so for we have to assigne obj.
obj=fun()  

