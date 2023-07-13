def double(bonus):
    return bonus * 2


bonuses = [100, 200, 300]

iterator = map(double, bonuses)# map function apply hole list in each element  and return an object
print(iterator) 
for i in iterator:
    print(i)

# with lambad fun
a=[1,2,3,4,5,6,7]
sav=map(lambda x:x*2,a)
lis=list(sav)
print(lis)

############################
names = ['david', 'peter', 'jenifer']
new_names = map(lambda name: name.capitalize(), names)
print(list(new_names))
