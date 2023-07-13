class abc():
    def __init__(self) :
        self.name="python"
        self.fee=1000
    def __str__(self):
        return self.name
    def __eq__(self,other):
        return self.name==self.name
    
    
obj=abc()

print(str(obj))        
print(obj)
        



#####################################

#__eq__ method
# 
# 
class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def __eq__(self, other):
        if isinstance(other, Person):
            return self.age == other.age

        return False


john = Person('John', 'Doe', 25)
jane = Person('Jane', 'Doe', 25)
mary = Person('Mary', 'Doe', 27)

print(john == jane)  # True
print(john == mary)  # False


john = Person('John', 'Doe', 25)
print(john == 20)  # False   


