# class stu():
#     def __init__(self) :
#         self.name="raj"
#         self .roll=2
    
#     def mth(self):
#         print(self.name) 
#         print(self.roll)  
#     def __len__(self):
#         return len(self.name)     
#     def __str__(self):
#         return self.name
    
    

# obj=stu()
# print(obj)
# print(len(obj))
# print(str(obj))

print("+++++++++++++++++++++++++++")
########################################
class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def __repr__(self):
        return f'Person("{self.first_name}","{self.last_name}",{self.age})'
    
obj=Person('python','django',22)
print(repr(obj))    