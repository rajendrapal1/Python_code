for x in range(5):
    for y in range(5):
        if y>1:
            break
        else:
            print(f'{x},{y}')


#turnary operator
age=int(input("inter a number=",)) 
if age>22 :
     price=20
else:
    price=30 
print(f" price is {price}")        

##############################
age=int(input("inter a age=",))
a=price1=20 if age>19 else 30
print(a)