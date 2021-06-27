class  Animal:
    'multilevel inheritance'
    def eat(self):
        print("Eating...")
    
class Dog(Animal):
    def bark(self):
        print("Barking...")
        
class BabyDog(Dog):
    def weep(self):
        print("weeping...")
        
d = BabyDog()
d.eat()
d.bark()
d.weep()