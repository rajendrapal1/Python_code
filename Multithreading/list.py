# num1=0
# def recursion_fun(num):
    
#     num=num 
#     if num<20:
#         if num%2 != 0:
#             num1=num
#             print(num1)

#         recursion_fun(num+1)
# recursion_fun(5)        
# def fun(n):

#     if n>0:

#         return n + fun (n-1)
    
#     return 0
# obj=fun(100)

# print(obj)    

# def fun(n):
#      return n + fun(n-1) if n>0 else 0

    
# obj=fun(100)
# print(obj)
# dic={
#     'name':'raj',
#     'roll':2,
#     'course':'bca'
# }
#dic['name']='ramu'
# print(dic.items())
# print(dic.keys())

# print(dic)
# a=['raj','pal']
# l=list(map(lambda x :x*2,a))
# l1=list(map(lambda x:x.upper(),a))
# print(l1)

# print(l)

# a=[1,2,3,4,5,6]
# b=[]
# for i in a:
#     b.append (i*2)

# print(b)    
# lis=[i*2 for i in a ]
# print(lis)

a1={
    'name':"raj",
    'roll':2,
    'city':'surat'
}
b={}
for i,j in a1.items():
    b[i]=j
    
print(f"index={b}")    
########################################
a={
    'mango':101,
    'banana':200,
    'apple':301,
    'greps':400
 }
lis1={ite:i*2 for (ite,i)in a.items()}     # kyes() and value() are both print 
lis2= { i  for (i) in a.values() if i%2==0 } # even value only print
print(lis1)
print(lis2)
# using  for loop print the element greterthen >200
sav={}
for k,v in a.items():
    if v>200:
     sav[k]=v
print(sav)    

# usging  dict comprehention
lis4={k:v for (k,v) in a.items() if v>200}
print(lis4)
