scores = [70, 60, 80, 90, 50]

filtered = []

for score in scores:
    if score >= 70:
        filtered.append(score)

print(filtered)

#filter fun
fil=filter(lambda x :x>60 ,scores)
print(list(fil))

##################################################

countries = [
    ['China', 94015977],
    ['United States', 329877505],
    ['India', 1326093247],
    ['Indonesia', 267026366],
    ['Bangladesh', 162650853],
    ['Pakistan', 233500636],
    ['Nigeria', 214028302],
    ['Brazil', 21171597],
    ['Russia', 141722205],
    ['Mexico', 128649565]
]

populated = filter(lambda c: c[1] > 300000000, countries)

print(list(populated))
