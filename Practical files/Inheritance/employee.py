class Person:
    number_of_people = 0 #class attribiute
    
    def __init__(self, name):
        self.name = name
        Person.add_people() 
    
    @classmethod  #Class methods
    def number_of_people_(cls):
        return cls.number_of_people()
    
    @classmethod
    def add_people(cls):
        cls.number_of_people += 1
        
p1 = Person("Harrison")
p2 = Person("Wekesa")
print(Person.number_of_people)