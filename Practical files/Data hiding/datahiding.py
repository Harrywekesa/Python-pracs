class JustCounter:
    __secretcount = 0 # Naming with double _ so that they will not be directly visible to outsiders
    
    def count(self):
        self.__secretcount += 1
        print(self.__secretcount)
        
    counter = JustCounter()
    counter.count()
    #print(counter.__secretcount)
    print(counter._Justcounter__secretcount)