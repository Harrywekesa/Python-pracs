class Student: #defining class
    'Common base class for all students'
    student_count = 0 #class variable accessible to all instances of the class
    
    def __init__(self, name, id): # class constructor
        self.name = name
        self.id = id
        Student.student_count =+ 1
        
    def printStudentData(self):  #Other class methods declared as normal functions
        print('Name : ', self.name, 'Id : ', self.id)
        
s = Student("Harrison wekesa", 2034)
d = Student('Nathan Lomin', 2042)
e = Student("Brian Kimutai", 2220)

s.printStudentData() #Accessing class attributes using the dot operator
d.printStudentData() #Accessing class attributes using the dot operator
e.printStudentData()

print("Total students : ", Student.student_count)
