class First(object):
    def __init__(self):
        super(First, self).__init__() #Super() used in base classes where we need to do somethings in a child then complete the initialization in the parent
        print("first")
        
class Second(object):
    def __init__(self):
        super(Second, self).__init__()
        print("Second")
        
class Third(object):
    def __init__(self):
        super(Third, self).__init__()
        print("Third")
        
Third(); #Call third class constructor