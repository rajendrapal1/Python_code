# age=int(input("enter a number=",))
# if age>20:
#     print("you are aligible")
# else:
#     print("you are not elegible")
        
##################################################
#if elif,else


# age=input("inte a age=",)
# myage=int(age)
# if myage<5:
#     print("your ticut price_rs =",myage) 
# elif myage>10:
#     print("you price rs=",myage)
# else:
#     print("more the 10 rs= ",)    
####################################################

#with while


college=[
    {'collage':'iics','fee':1000},
    {'collage':'kpii','fee':2000},
    {'collage':'mth','fee':300}

]

college1=input("iner a collage=",)
index1=0
lenth=len(college)

while index1<lenth:
     item=college[index1]
     if item['collage']==college1:
          
        print(  item['collage'], item['fee'] )   

     else:
         print("collage are not machages") 

     index1+=1
