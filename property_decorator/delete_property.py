#delete property 

#from pprint import pprint


class Person:
    def __init__(self, name):
        self._name = name

    @property  #access the property of class instance variable and modify and return. 
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if value.strip() == '':
            raise ValueError('name cannot be empty')
        self._name = value

    @name.deleter
    def name(self):
        del self._name

obj=Person('django')   
obj.name='python language'
                       
                                                  
print(obj.name)    
print(obj.__dict__)
print(obj.name)
del obj.name
print(obj.__dict__)
