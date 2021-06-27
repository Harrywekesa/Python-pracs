class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def show(self):    
        print("I am {} and I am {} years old".format(self.name, self.age))
        
class Cat(Pet):
    def speak(self):
        print("Meowing...")
        
    def show(self):    
        print("I am {} and I am {} years old".format(self.name, self.age))
        
class Dog(Pet):
    def speak(self):
        print("Barking...")
        
p = Pet("Harry", 20)
p.show()
c = Cat("Bill", 12)
c.show()
d = Dog("Jill", 10)
d.show()

d.speak()
c.speak()