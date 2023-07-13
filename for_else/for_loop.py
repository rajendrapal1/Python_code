# people = [{'name': 'John', 'age': 25},
#         {'name': 'Jane', 'age': 22},
#         {'name': 'Peter', 'age': 30},
#         {'name': 'Jenifer', 'age': 28}]

# name = input('Enter a name:')


# found = False
# for person in people:
#     if person['name'] == name:
#         found = True
#         print(person)
#         break

# if not found:
#     print(f'{name} not found!')

#[{'name': 'John', 'age': 25},

#######################################################
person=[
        {'name': 'Jane', 'age': 22},
        {'name': 'Peter', 'age': 30},
        {'name': 'Jenifer', 'age': 28}
        ]
seatch=False
age=int(input("enter a age=",))
for i in person:
    if i['age']==age:
        print(i)
        break
if not seatch:
    print(f'{age} not search age')
