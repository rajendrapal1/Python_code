a=[1,2,3,4,5]
li=[10,20]
print(a[0])
print(a[-1])
b=a[0]=100 # list are mutable
print(b)
#append()
a.append(100)
print(" append()add element end of lis",a)
#extend method
a.extend(li)
print("extend method add all element end of list=",a)
# remove -> remove spacific element of a list
a.remove(5)
print(a)
#index ->
aa=['raj' ,'ram']
b=aa.index('raj')
inde=a.index(3)
print("index=",inde)
print("index is=",b)

#insert -> insert the element of spacific positon of list
numbers = [1, 3, 2, 7, 9, 4]
numbers.insert(2, 100)

print(numbers)
# reverse
numbers.reverse()
print(numbers)

# pop method() -> pop method remove the element of end of list 
numbers.pop()
print(numbers) 
