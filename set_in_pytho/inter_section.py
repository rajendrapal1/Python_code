
s1 = {'Python', 'Java', 'C++'}
s2 = {'C#', 'Java', 'C++'}

s = s1.intersection(s2)

print(s)

#union
u1={1,2,3,4}
u2={3,1,5}
result=u1.union(u2)
print(result)

#difirence //s1 and s2 ,set one of elelemt are not available the that set are available
u1={1,2,3,4}
u2={3,1,5}
result=u1.difference(u2)
print(result)

# symmetric diffirence

symm1={1,2,3,4,5}  #symmetric difference get element set 1 and set2 are not maches .
symm2={6,4,2,3}
result=symm1 .symmetric_difference(symm2) 
print(result)

#or 
s1 = {'Python', 'Java', 'C++'}
s2 = {'C#', 'Java', 'C++'}

s = s1 ^ s2
print(s)

#is subset  => return true and false

numbers = {1, 2, 3, 4, 5}
numb={1,2,3}

print(numbers.issubset(numb))
print(numb.issubset(numbers))
# using subset operator
d=numbers <= numb
print(d)
# 
c=numb <= numbers
print(c)

#is superset

st1={190,20,30,40,50,4}
st2={20,30,4}
result=st2 .issuperset(st1)
result2=st1 .issuperset(st2)
print(result)
print(result2)

#isdisjoint method
a={1,2,3,4}
b={31,41,5}
print(a.isdisjoint(b))

#or 
a={"python","djanog","numpy"}
d={"numpy","plask"}
print("is_disjoint=",a.isdisjoint(d))

