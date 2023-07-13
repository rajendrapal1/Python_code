#frozenset ->frozen set imutable we can not chenge .in set order is not mentane.
skills = {'Problem solving', 'Software design', 'Python programming'}
skills = frozenset(skills)

#skills.add(100) # error
#print(skills)
for i in skills:
    print(i)

#enumirate function

set1={'software','company','hcl','tcs'}
for i ,k in enumerate(set1):
    print(f'{i},{k}')