east = ['New York', 'New Jersey']
west = ['San Diego', 'San Francisco']

cities = east + west
print(cities)


# append()
east = ['New York', 'New Jersey']
north=['pakistab','bangladesh']
east.append(north)
print(east)



city = [['San Francisco', 900_000]]
cities = city + city

print(cities)

name=[[['raj','utter','pradesh']]]
name1=name +name +name
print(name1)

###########################
city = [['San Francisco', 900_000]]
cities = city + city

print(cities)
print(cities[0])
print(cities[1])
print(id(cities[0]) == id(cities[1]))  # True

city[0][1] = 1_000_000
print(cities)