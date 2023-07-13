from functools import reduce # reduce function return only single values 

scores = [75, 65, 80, 95, 50]

total = reduce(lambda a, b: a + b, scores)

print(total)

# with function
def fun(a,b):
    print(f"{a},{b},{a}+{b}= {a+b}")
    return a+b

scores1=reduce(fun,scores) # hear pass function name second list name 

print(scores1)

#####################################
a=reduce(lambda x,y:x+y,scores)
print(a)