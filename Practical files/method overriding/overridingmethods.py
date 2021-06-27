class Parent: #defining parent class
    def myMethod(self):
        print("Calling parent method")
        
class Child(Parent): # defining child class
    def myMethod(self):
        print("Calling child method")
        
c = Child() # instance of child
c.myMethod() # child calls overriden method