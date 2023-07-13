mountains = [
    ['Makalu', 8485],
    ['Lhotse', 8516],
    ['Kanchendzonga', 8586],
    ['K2', 8611],
    ['Everest', 8848]
]

highest_mountains = [m for m in mountains if m[1] > 8600]

print(highest_mountains)

#even number
li=[1,2,3,4,5,6,7]
b=[i for i in li if i%2==0] # list comprehention represent creating of new list that eterable of object
print(b)
