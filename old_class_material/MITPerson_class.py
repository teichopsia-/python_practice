# Building inheritance

class MITPerson(Person):
    nextIdNum = 0 #next ID number to assing
    
    def __init__(self, name):
        Person.__init__(self, name) #initialize Person attributes
        # new MITPerson atrribute: a unique ID number
        self.idNum = MITPerson.nextIdNum
        MITPerson.nextIdNum += 1
        
    def getIdNum(self):
        return self.idNum
        
    def __It__(self, other):
        return self.idNum < other.idNum
        
class Student(MITPerson):   
    pass
        
class UG(Student): #UG = under graduate   ###------
    def __init__(self, name, classYear):
        MITPerson.__init__(self, name)
        self.year = classYear
        
    def getClass(self):   # getter method
        return self.year
    
class Grad(Student): ##----
    pass
    
class TransferStudent(Student):
    pass
    
def isStudent(obj):
    return isinstance(obj, Student) 
