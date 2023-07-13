# a={
#     "name":"raj",
#     "roll":2,
#     "city":"surat"
# }
# print(a['name'],a['roll'])

# # get method
# print(a.get('name'))

# with for loop 
dic={
    'mango':100,
    'banana':200,
    'grapes':300,
    'orange':330
}
stor={}
for k,v in dic.items():
    if v>200:
        stor[k]=v
print(stor)
################### with dict comprehention
dict1={k :v for (k ,v) in dic.items() if v>200 }
print(dict1)