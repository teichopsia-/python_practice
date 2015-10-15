import datetime

class Person(object):
    """
    Create a person called name 
    """
    def __init__(self, name):
        self.name = name
        self.birthday = None
        self.lastName = name.split(' ')[-1]
        
    def getLastName(self):
        """ return self's last name """
        return self.lastName
        
    def setBirthday(self, month, day, year):
        ''' set self's birthday to birthdate '''
        self.birthday = datetime.date(year, month, day)
        
    def getAge(self):
        ''' return self's current age in days '''
        if self.birthday == None:
            raise ValueError
        return (datetime.date.today() - self.birthday).days
        
    def __lt__(self, other):
        ''' To be able to use the less than operator on objects,
        one must use the magic method __lt__
        '''
        if self.lastName == other.lastName:
            return self.name < other.name
        return self.lastName < other.lastName
        
    def __str__(self):
        ''' return self's name '''
        return self.name
        
# MitPerson will inherit from the PersonClass
class MitPerson(Person):
    nextIdNum = 0
    
    def __init__(self, name):
        Person.__init__(self, name) #Initialize Person attributes
        # new MITPerson attribute: a unique ID number
        self.idNum = MitPerson.nextIdNum
        MitPerson.nextIdNum += 1
        
    def getIdNum(self):
        return self.idNum
        
    # sorting Mit people using their ID numbers, not name.
    def __lt__(self, other):
        return self.idNum < other.idNum
