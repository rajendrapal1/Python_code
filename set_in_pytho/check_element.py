a={2,3,4,5,6,6}
b=2
if b in a:
  
  print(a)
d=50
if d not in a:
  print(d)


# add method ->add the element in set ,order in not aplicable in set
a={10,20,30,40}
a.add(100)
a.add(200)
print(a)

#remove
skills = {'Problem solving', 'Software design', 'Python programming'}
skills.remove('Software design')

print(skills)

#discard  > remove element if in set  element are not available then did't get error.
skills = {'Problem solving', 'Software design', 'Python programming'}
skills.discard('Problem solving==')
print(skills)

#clear method()->remove the all element in set
a={1,2,3,}
a.clear()
print(a)

