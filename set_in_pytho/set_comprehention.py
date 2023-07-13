set1={'python',"django","numpy"}
st=set()
for i in set1:
    st.add(i.upper())
print(st) 

#set comprehention
stc={x.upper() for x in set1 }
print(stc)

#with map function()
st1={'django','pip','pygame'}
s=set(map(lambda x:x.upper(),st1))

k=set({a.upper() for a in st1 if a!='pip'}) #set comprehention
print(s)
print(k)
