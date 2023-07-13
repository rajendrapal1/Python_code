a=['python','django','apple']
print(a[:2])
print(a[1:3])
b=a[1:2]=['c++','c']
print(b)
print(a)

colors = ['red', 'green', 'blue', 'orange']

s = slice(0, 4, 2)
t = s.indices(len(colors))

for index in range(*t):
    print(colors[index])

